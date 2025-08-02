_M='wtWebGraphThermoBaroDiagErrorMessage'
_L='wtWebGraphThermoBaroDiagErrorIndex'
_K='NotificationType'
_J='wtWebGraphThermoBaroAlarmNo'
_I='wtWebGraphThermoBaroSensorNo'
_H='wtWebGraphThermoBaroAlarmClearTrapText'
_G='wtWebGraphThermoBaroAlarmTrapText'
_F='OctetString'
_E='read-only'
_D='Integer32'
_C='WebGraph-Thermo-Hygro-Barometer-US-MIB'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_K,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_K,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Wut_ObjectIdentity=ObjectIdentity
wut=_Wut_ObjectIdentity((1,3,6,1,4,1,5040))
_WtComServer_ObjectIdentity=ObjectIdentity
wtComServer=_WtComServer_ObjectIdentity((1,3,6,1,4,1,5040,1))
_WtWebio_ObjectIdentity=ObjectIdentity
wtWebio=_WtWebio_ObjectIdentity((1,3,6,1,4,1,5040,1,2))
_WtWebGraphThermoBaro_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaro=_WtWebGraphThermoBaro_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37))
_WtWebGraphThermoBaroTemp_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroTemp=_WtWebGraphThermoBaroTemp_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,1))
class _WtWebGraphThermoBaroSensors_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_WtWebGraphThermoBaroSensors_Type.__name__=_D
_WtWebGraphThermoBaroSensors_Object=MibScalar
wtWebGraphThermoBaroSensors=_WtWebGraphThermoBaroSensors_Object((1,3,6,1,4,1,5040,1,2,37,1,1),_WtWebGraphThermoBaroSensors_Type())
wtWebGraphThermoBaroSensors.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphThermoBaroSensors.setStatus(_A)
_WtWebGraphThermoBaroSensorTable_Object=MibTable
wtWebGraphThermoBaroSensorTable=_WtWebGraphThermoBaroSensorTable_Object((1,3,6,1,4,1,5040,1,2,37,1,2))
if mibBuilder.loadTexts:wtWebGraphThermoBaroSensorTable.setStatus(_A)
_WtWebGraphThermoBaroSensorEntry_Object=MibTableRow
wtWebGraphThermoBaroSensorEntry=_WtWebGraphThermoBaroSensorEntry_Object((1,3,6,1,4,1,5040,1,2,37,1,2,1))
wtWebGraphThermoBaroSensorEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:wtWebGraphThermoBaroSensorEntry.setStatus(_A)
class _WtWebGraphThermoBaroSensorNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_WtWebGraphThermoBaroSensorNo_Type.__name__=_D
_WtWebGraphThermoBaroSensorNo_Object=MibTableColumn
wtWebGraphThermoBaroSensorNo=_WtWebGraphThermoBaroSensorNo_Object((1,3,6,1,4,1,5040,1,2,37,1,2,1,1),_WtWebGraphThermoBaroSensorNo_Type())
wtWebGraphThermoBaroSensorNo.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphThermoBaroSensorNo.setStatus(_A)
_WtWebGraphThermoBaroTempValueTable_Object=MibTable
wtWebGraphThermoBaroTempValueTable=_WtWebGraphThermoBaroTempValueTable_Object((1,3,6,1,4,1,5040,1,2,37,1,3))
if mibBuilder.loadTexts:wtWebGraphThermoBaroTempValueTable.setStatus(_A)
_WtWebGraphThermoBaroTempValueEntry_Object=MibTableRow
wtWebGraphThermoBaroTempValueEntry=_WtWebGraphThermoBaroTempValueEntry_Object((1,3,6,1,4,1,5040,1,2,37,1,3,1))
wtWebGraphThermoBaroTempValueEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:wtWebGraphThermoBaroTempValueEntry.setStatus(_A)
class _WtWebGraphThermoBaroTempValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_WtWebGraphThermoBaroTempValue_Type.__name__=_F
_WtWebGraphThermoBaroTempValue_Object=MibTableColumn
wtWebGraphThermoBaroTempValue=_WtWebGraphThermoBaroTempValue_Object((1,3,6,1,4,1,5040,1,2,37,1,3,1,1),_WtWebGraphThermoBaroTempValue_Type())
wtWebGraphThermoBaroTempValue.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphThermoBaroTempValue.setStatus(_A)
_WtWebGraphThermoBaroBinaryTempValueTable_Object=MibTable
wtWebGraphThermoBaroBinaryTempValueTable=_WtWebGraphThermoBaroBinaryTempValueTable_Object((1,3,6,1,4,1,5040,1,2,37,1,4))
if mibBuilder.loadTexts:wtWebGraphThermoBaroBinaryTempValueTable.setStatus(_A)
_WtWebGraphThermoBaroBinaryTempValueEntry_Object=MibTableRow
wtWebGraphThermoBaroBinaryTempValueEntry=_WtWebGraphThermoBaroBinaryTempValueEntry_Object((1,3,6,1,4,1,5040,1,2,37,1,4,1))
wtWebGraphThermoBaroBinaryTempValueEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:wtWebGraphThermoBaroBinaryTempValueEntry.setStatus(_A)
_WtWebGraphThermoBaroBinaryTempValue_Type=Integer32
_WtWebGraphThermoBaroBinaryTempValue_Object=MibTableColumn
wtWebGraphThermoBaroBinaryTempValue=_WtWebGraphThermoBaroBinaryTempValue_Object((1,3,6,1,4,1,5040,1,2,37,1,4,1,1),_WtWebGraphThermoBaroBinaryTempValue_Type())
wtWebGraphThermoBaroBinaryTempValue.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphThermoBaroBinaryTempValue.setStatus(_A)
_WtWebGraphThermoBaroTempValuePktTable_Object=MibTable
wtWebGraphThermoBaroTempValuePktTable=_WtWebGraphThermoBaroTempValuePktTable_Object((1,3,6,1,4,1,5040,1,2,37,1,8))
if mibBuilder.loadTexts:wtWebGraphThermoBaroTempValuePktTable.setStatus(_A)
_WtWebGraphThermoBaroTempValuePktEntry_Object=MibTableRow
wtWebGraphThermoBaroTempValuePktEntry=_WtWebGraphThermoBaroTempValuePktEntry_Object((1,3,6,1,4,1,5040,1,2,37,1,8,1))
wtWebGraphThermoBaroTempValuePktEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:wtWebGraphThermoBaroTempValuePktEntry.setStatus(_A)
class _WtWebGraphThermoBaroTempValuePkt_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_WtWebGraphThermoBaroTempValuePkt_Type.__name__=_F
_WtWebGraphThermoBaroTempValuePkt_Object=MibTableColumn
wtWebGraphThermoBaroTempValuePkt=_WtWebGraphThermoBaroTempValuePkt_Object((1,3,6,1,4,1,5040,1,2,37,1,8,1,1),_WtWebGraphThermoBaroTempValuePkt_Type())
wtWebGraphThermoBaroTempValuePkt.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphThermoBaroTempValuePkt.setStatus(_A)
_WtWebGraphThermoBaroSessCntrl_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroSessCntrl=_WtWebGraphThermoBaroSessCntrl_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,2))
_WtWebGraphThermoBaroSessCntrlPassword_Type=OctetString
_WtWebGraphThermoBaroSessCntrlPassword_Object=MibScalar
wtWebGraphThermoBaroSessCntrlPassword=_WtWebGraphThermoBaroSessCntrlPassword_Object((1,3,6,1,4,1,5040,1,2,37,2,1),_WtWebGraphThermoBaroSessCntrlPassword_Type())
wtWebGraphThermoBaroSessCntrlPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroSessCntrlPassword.setStatus(_A)
class _WtWebGraphThermoBaroSessCntrlConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('wtWebGraphThermoBaroSessCntrl-NoSession',0),('wtWebGraphThermoBaroSessCntrl-Session',1)))
_WtWebGraphThermoBaroSessCntrlConfigMode_Type.__name__=_D
_WtWebGraphThermoBaroSessCntrlConfigMode_Object=MibScalar
wtWebGraphThermoBaroSessCntrlConfigMode=_WtWebGraphThermoBaroSessCntrlConfigMode_Object((1,3,6,1,4,1,5040,1,2,37,2,2),_WtWebGraphThermoBaroSessCntrlConfigMode_Type())
wtWebGraphThermoBaroSessCntrlConfigMode.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphThermoBaroSessCntrlConfigMode.setStatus(_A)
_WtWebGraphThermoBaroSessCntrlLogout_Type=Integer32
_WtWebGraphThermoBaroSessCntrlLogout_Object=MibScalar
wtWebGraphThermoBaroSessCntrlLogout=_WtWebGraphThermoBaroSessCntrlLogout_Object((1,3,6,1,4,1,5040,1,2,37,2,3),_WtWebGraphThermoBaroSessCntrlLogout_Type())
wtWebGraphThermoBaroSessCntrlLogout.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroSessCntrlLogout.setStatus(_A)
_WtWebGraphThermoBaroSessCntrlAdminPassword_Type=OctetString
_WtWebGraphThermoBaroSessCntrlAdminPassword_Object=MibScalar
wtWebGraphThermoBaroSessCntrlAdminPassword=_WtWebGraphThermoBaroSessCntrlAdminPassword_Object((1,3,6,1,4,1,5040,1,2,37,2,4),_WtWebGraphThermoBaroSessCntrlAdminPassword_Type())
wtWebGraphThermoBaroSessCntrlAdminPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroSessCntrlAdminPassword.setStatus(_A)
_WtWebGraphThermoBaroSessCntrlConfigPassword_Type=OctetString
_WtWebGraphThermoBaroSessCntrlConfigPassword_Object=MibScalar
wtWebGraphThermoBaroSessCntrlConfigPassword=_WtWebGraphThermoBaroSessCntrlConfigPassword_Object((1,3,6,1,4,1,5040,1,2,37,2,5),_WtWebGraphThermoBaroSessCntrlConfigPassword_Type())
wtWebGraphThermoBaroSessCntrlConfigPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroSessCntrlConfigPassword.setStatus(_A)
_WtWebGraphThermoBaroConfig_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroConfig=_WtWebGraphThermoBaroConfig_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3))
_WtWebGraphThermoBaroDevice_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroDevice=_WtWebGraphThermoBaroDevice_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,1))
_WtWebGraphThermoBaroText_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroText=_WtWebGraphThermoBaroText_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,1,1))
_WtWebGraphThermoBaroDeviceName_Type=OctetString
_WtWebGraphThermoBaroDeviceName_Object=MibScalar
wtWebGraphThermoBaroDeviceName=_WtWebGraphThermoBaroDeviceName_Object((1,3,6,1,4,1,5040,1,2,37,3,1,1,1),_WtWebGraphThermoBaroDeviceName_Type())
wtWebGraphThermoBaroDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroDeviceName.setStatus(_A)
_WtWebGraphThermoBaroDeviceText_Type=OctetString
_WtWebGraphThermoBaroDeviceText_Object=MibScalar
wtWebGraphThermoBaroDeviceText=_WtWebGraphThermoBaroDeviceText_Object((1,3,6,1,4,1,5040,1,2,37,3,1,1,2),_WtWebGraphThermoBaroDeviceText_Type())
wtWebGraphThermoBaroDeviceText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroDeviceText.setStatus(_A)
_WtWebGraphThermoBaroDeviceLocation_Type=OctetString
_WtWebGraphThermoBaroDeviceLocation_Object=MibScalar
wtWebGraphThermoBaroDeviceLocation=_WtWebGraphThermoBaroDeviceLocation_Object((1,3,6,1,4,1,5040,1,2,37,3,1,1,3),_WtWebGraphThermoBaroDeviceLocation_Type())
wtWebGraphThermoBaroDeviceLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroDeviceLocation.setStatus(_A)
_WtWebGraphThermoBaroDeviceContact_Type=OctetString
_WtWebGraphThermoBaroDeviceContact_Object=MibScalar
wtWebGraphThermoBaroDeviceContact=_WtWebGraphThermoBaroDeviceContact_Object((1,3,6,1,4,1,5040,1,2,37,3,1,1,4),_WtWebGraphThermoBaroDeviceContact_Type())
wtWebGraphThermoBaroDeviceContact.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroDeviceContact.setStatus(_A)
_WtWebGraphThermoBaroTimeDate_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroTimeDate=_WtWebGraphThermoBaroTimeDate_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,1,2))
_WtWebGraphThermoBaroTimeZone_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroTimeZone=_WtWebGraphThermoBaroTimeZone_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,1,2,1))
_WtWebGraphThermoBaroTzOffsetHrs_Type=Integer32
_WtWebGraphThermoBaroTzOffsetHrs_Object=MibScalar
wtWebGraphThermoBaroTzOffsetHrs=_WtWebGraphThermoBaroTzOffsetHrs_Object((1,3,6,1,4,1,5040,1,2,37,3,1,2,1,1),_WtWebGraphThermoBaroTzOffsetHrs_Type())
wtWebGraphThermoBaroTzOffsetHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroTzOffsetHrs.setStatus(_A)
_WtWebGraphThermoBaroTzOffsetMin_Type=Integer32
_WtWebGraphThermoBaroTzOffsetMin_Object=MibScalar
wtWebGraphThermoBaroTzOffsetMin=_WtWebGraphThermoBaroTzOffsetMin_Object((1,3,6,1,4,1,5040,1,2,37,3,1,2,1,2),_WtWebGraphThermoBaroTzOffsetMin_Type())
wtWebGraphThermoBaroTzOffsetMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroTzOffsetMin.setStatus(_A)
class _WtWebGraphThermoBaroTzEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoBaroTzEnable_Type.__name__=_F
_WtWebGraphThermoBaroTzEnable_Object=MibScalar
wtWebGraphThermoBaroTzEnable=_WtWebGraphThermoBaroTzEnable_Object((1,3,6,1,4,1,5040,1,2,37,3,1,2,1,3),_WtWebGraphThermoBaroTzEnable_Type())
wtWebGraphThermoBaroTzEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroTzEnable.setStatus(_A)
_WtWebGraphThermoBaroStTzOffsetHrs_Type=Integer32
_WtWebGraphThermoBaroStTzOffsetHrs_Object=MibScalar
wtWebGraphThermoBaroStTzOffsetHrs=_WtWebGraphThermoBaroStTzOffsetHrs_Object((1,3,6,1,4,1,5040,1,2,37,3,1,2,1,4),_WtWebGraphThermoBaroStTzOffsetHrs_Type())
wtWebGraphThermoBaroStTzOffsetHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroStTzOffsetHrs.setStatus(_A)
_WtWebGraphThermoBaroStTzOffsetMin_Type=Integer32
_WtWebGraphThermoBaroStTzOffsetMin_Object=MibScalar
wtWebGraphThermoBaroStTzOffsetMin=_WtWebGraphThermoBaroStTzOffsetMin_Object((1,3,6,1,4,1,5040,1,2,37,3,1,2,1,5),_WtWebGraphThermoBaroStTzOffsetMin_Type())
wtWebGraphThermoBaroStTzOffsetMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroStTzOffsetMin.setStatus(_A)
class _WtWebGraphThermoBaroStTzEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoBaroStTzEnable_Type.__name__=_F
_WtWebGraphThermoBaroStTzEnable_Object=MibScalar
wtWebGraphThermoBaroStTzEnable=_WtWebGraphThermoBaroStTzEnable_Object((1,3,6,1,4,1,5040,1,2,37,3,1,2,1,6),_WtWebGraphThermoBaroStTzEnable_Type())
wtWebGraphThermoBaroStTzEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroStTzEnable.setStatus(_A)
class _WtWebGraphThermoBaroStTzStartMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('wtWebGraphThermoBaroStartMonth-January',1),('wtWebGraphThermoBaroStartMonth-February',2),('wtWebGraphThermoBaroStartMonth-March',3),('wtWebGraphThermoBaroStartMonth-April',4),('wtWebGraphThermoBaroStartMonth-May',5),('wtWebGraphThermoBaroStartMonth-June',6),('wtWebGraphThermoBaroStartMonth-July',7),('wtWebGraphThermoBaroStartMonth-August',8),('wtWebGraphThermoBaroStartMonth-September',9),('wtWebGraphThermoBaroStartMonth-October',10),('wtWebGraphThermoBaroStartMonth-November',11),('wtWebGraphThermoBaroStartMonth-December',12)))
_WtWebGraphThermoBaroStTzStartMonth_Type.__name__=_D
_WtWebGraphThermoBaroStTzStartMonth_Object=MibScalar
wtWebGraphThermoBaroStTzStartMonth=_WtWebGraphThermoBaroStTzStartMonth_Object((1,3,6,1,4,1,5040,1,2,37,3,1,2,1,7),_WtWebGraphThermoBaroStTzStartMonth_Type())
wtWebGraphThermoBaroStTzStartMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroStTzStartMonth.setStatus(_A)
class _WtWebGraphThermoBaroStTzStartMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('wtWebGraphThermoBaroStartMode-first',1),('wtWebGraphThermoBaroStartMode-second',2),('wtWebGraphThermoBaroStartMode-third',3),('wtWebGraphThermoBaroStartMode-fourth',4),('wtWebGraphThermoBaroStartMode-last',5)))
_WtWebGraphThermoBaroStTzStartMode_Type.__name__=_D
_WtWebGraphThermoBaroStTzStartMode_Object=MibScalar
wtWebGraphThermoBaroStTzStartMode=_WtWebGraphThermoBaroStTzStartMode_Object((1,3,6,1,4,1,5040,1,2,37,3,1,2,1,8),_WtWebGraphThermoBaroStTzStartMode_Type())
wtWebGraphThermoBaroStTzStartMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroStTzStartMode.setStatus(_A)
class _WtWebGraphThermoBaroStTzStartWday_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('wtWebGraphThermoBaroStartWday-Sunday',1),('wtWebGraphThermoBaroStartWday-Monday',2),('wtWebGraphThermoBaroStartWday-Tuesday',3),('wtWebGraphThermoBaroStartWday-Thursday',4),('wtWebGraphThermoBaroStartWday-Wednesday',5),('wtWebGraphThermoBaroStartWday-Friday',6),('wtWebGraphThermoBaroStartWday-Saturday',7)))
_WtWebGraphThermoBaroStTzStartWday_Type.__name__=_D
_WtWebGraphThermoBaroStTzStartWday_Object=MibScalar
wtWebGraphThermoBaroStTzStartWday=_WtWebGraphThermoBaroStTzStartWday_Object((1,3,6,1,4,1,5040,1,2,37,3,1,2,1,9),_WtWebGraphThermoBaroStTzStartWday_Type())
wtWebGraphThermoBaroStTzStartWday.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroStTzStartWday.setStatus(_A)
_WtWebGraphThermoBaroStTzStartHrs_Type=Integer32
_WtWebGraphThermoBaroStTzStartHrs_Object=MibScalar
wtWebGraphThermoBaroStTzStartHrs=_WtWebGraphThermoBaroStTzStartHrs_Object((1,3,6,1,4,1,5040,1,2,37,3,1,2,1,10),_WtWebGraphThermoBaroStTzStartHrs_Type())
wtWebGraphThermoBaroStTzStartHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroStTzStartHrs.setStatus(_A)
_WtWebGraphThermoBaroStTzStartMin_Type=Integer32
_WtWebGraphThermoBaroStTzStartMin_Object=MibScalar
wtWebGraphThermoBaroStTzStartMin=_WtWebGraphThermoBaroStTzStartMin_Object((1,3,6,1,4,1,5040,1,2,37,3,1,2,1,11),_WtWebGraphThermoBaroStTzStartMin_Type())
wtWebGraphThermoBaroStTzStartMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroStTzStartMin.setStatus(_A)
class _WtWebGraphThermoBaroStTzStopMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('wtWebGraphThermoBaroStopMonth-January',1),('wtWebGraphThermoBaroStopMonth-February',2),('wtWebGraphThermoBaroStopMonth-March',3),('wtWebGraphThermoBaroStopMonth-April',4),('wtWebGraphThermoBaroStopMonth-May',5),('wtWebGraphThermoBaroStopMonth-June',6),('wtWebGraphThermoBaroStopMonth-July',7),('wtWebGraphThermoBaroStopMonth-August',8),('wtWebGraphThermoBaroStopMonth-September',9),('wtWebGraphThermoBaroStopMonth-October',10),('wtWebGraphThermoBaroStopMonth-November',11),('wtWebGraphThermoBaroStopMonth-December',12)))
_WtWebGraphThermoBaroStTzStopMonth_Type.__name__=_D
_WtWebGraphThermoBaroStTzStopMonth_Object=MibScalar
wtWebGraphThermoBaroStTzStopMonth=_WtWebGraphThermoBaroStTzStopMonth_Object((1,3,6,1,4,1,5040,1,2,37,3,1,2,1,12),_WtWebGraphThermoBaroStTzStopMonth_Type())
wtWebGraphThermoBaroStTzStopMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroStTzStopMonth.setStatus(_A)
class _WtWebGraphThermoBaroStTzStopMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('wtWebGraphThermoBaroStopMode-first',1),('wtWebGraphThermoBaroStopMode-second',2),('wtWebGraphThermoBaroStopMode-third',3),('wtWebGraphThermoBaroStopMode-fourth',4),('wtWebGraphThermoBaroStopMode-last',5)))
_WtWebGraphThermoBaroStTzStopMode_Type.__name__=_D
_WtWebGraphThermoBaroStTzStopMode_Object=MibScalar
wtWebGraphThermoBaroStTzStopMode=_WtWebGraphThermoBaroStTzStopMode_Object((1,3,6,1,4,1,5040,1,2,37,3,1,2,1,13),_WtWebGraphThermoBaroStTzStopMode_Type())
wtWebGraphThermoBaroStTzStopMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroStTzStopMode.setStatus(_A)
class _WtWebGraphThermoBaroStTzStopWday_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('wtWebGraphThermoBaroStopWday-Sunday',1),('wtWebGraphThermoBaroStopWday-Monday',2),('wtWebGraphThermoBaroStopWday-Tuesday',3),('wtWebGraphThermoBaroStopWday-Thursday',4),('wtWebGraphThermoBaroStopWday-Wednesday',5),('wtWebGraphThermoBaroStopWday-Friday',6),('wtWebGraphThermoBaroStopWday-Saturday',7)))
_WtWebGraphThermoBaroStTzStopWday_Type.__name__=_D
_WtWebGraphThermoBaroStTzStopWday_Object=MibScalar
wtWebGraphThermoBaroStTzStopWday=_WtWebGraphThermoBaroStTzStopWday_Object((1,3,6,1,4,1,5040,1,2,37,3,1,2,1,14),_WtWebGraphThermoBaroStTzStopWday_Type())
wtWebGraphThermoBaroStTzStopWday.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroStTzStopWday.setStatus(_A)
_WtWebGraphThermoBaroStTzStopHrs_Type=Integer32
_WtWebGraphThermoBaroStTzStopHrs_Object=MibScalar
wtWebGraphThermoBaroStTzStopHrs=_WtWebGraphThermoBaroStTzStopHrs_Object((1,3,6,1,4,1,5040,1,2,37,3,1,2,1,15),_WtWebGraphThermoBaroStTzStopHrs_Type())
wtWebGraphThermoBaroStTzStopHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroStTzStopHrs.setStatus(_A)
_WtWebGraphThermoBaroStTzStopMin_Type=Integer32
_WtWebGraphThermoBaroStTzStopMin_Object=MibScalar
wtWebGraphThermoBaroStTzStopMin=_WtWebGraphThermoBaroStTzStopMin_Object((1,3,6,1,4,1,5040,1,2,37,3,1,2,1,16),_WtWebGraphThermoBaroStTzStopMin_Type())
wtWebGraphThermoBaroStTzStopMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroStTzStopMin.setStatus(_A)
_WtWebGraphThermoBaroTimeServer_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroTimeServer=_WtWebGraphThermoBaroTimeServer_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,1,2,2))
_WtWebGraphThermoBaroTimeServer1_Type=OctetString
_WtWebGraphThermoBaroTimeServer1_Object=MibScalar
wtWebGraphThermoBaroTimeServer1=_WtWebGraphThermoBaroTimeServer1_Object((1,3,6,1,4,1,5040,1,2,37,3,1,2,2,1),_WtWebGraphThermoBaroTimeServer1_Type())
wtWebGraphThermoBaroTimeServer1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroTimeServer1.setStatus(_A)
_WtWebGraphThermoBaroTimeServer2_Type=OctetString
_WtWebGraphThermoBaroTimeServer2_Object=MibScalar
wtWebGraphThermoBaroTimeServer2=_WtWebGraphThermoBaroTimeServer2_Object((1,3,6,1,4,1,5040,1,2,37,3,1,2,2,2),_WtWebGraphThermoBaroTimeServer2_Type())
wtWebGraphThermoBaroTimeServer2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroTimeServer2.setStatus(_A)
class _WtWebGraphThermoBaroTsEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoBaroTsEnable_Type.__name__=_F
_WtWebGraphThermoBaroTsEnable_Object=MibScalar
wtWebGraphThermoBaroTsEnable=_WtWebGraphThermoBaroTsEnable_Object((1,3,6,1,4,1,5040,1,2,37,3,1,2,2,3),_WtWebGraphThermoBaroTsEnable_Type())
wtWebGraphThermoBaroTsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroTsEnable.setStatus(_A)
_WtWebGraphThermoBaroTsSyncTime_Type=Integer32
_WtWebGraphThermoBaroTsSyncTime_Object=MibScalar
wtWebGraphThermoBaroTsSyncTime=_WtWebGraphThermoBaroTsSyncTime_Object((1,3,6,1,4,1,5040,1,2,37,3,1,2,2,4),_WtWebGraphThermoBaroTsSyncTime_Type())
wtWebGraphThermoBaroTsSyncTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroTsSyncTime.setStatus(_A)
_WtWebGraphThermoBaroDeviceClock_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroDeviceClock=_WtWebGraphThermoBaroDeviceClock_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,1,2,3))
class _WtWebGraphThermoBaroClockHrs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_WtWebGraphThermoBaroClockHrs_Type.__name__=_D
_WtWebGraphThermoBaroClockHrs_Object=MibScalar
wtWebGraphThermoBaroClockHrs=_WtWebGraphThermoBaroClockHrs_Object((1,3,6,1,4,1,5040,1,2,37,3,1,2,3,1),_WtWebGraphThermoBaroClockHrs_Type())
wtWebGraphThermoBaroClockHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroClockHrs.setStatus(_A)
class _WtWebGraphThermoBaroClockMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_WtWebGraphThermoBaroClockMin_Type.__name__=_D
_WtWebGraphThermoBaroClockMin_Object=MibScalar
wtWebGraphThermoBaroClockMin=_WtWebGraphThermoBaroClockMin_Object((1,3,6,1,4,1,5040,1,2,37,3,1,2,3,2),_WtWebGraphThermoBaroClockMin_Type())
wtWebGraphThermoBaroClockMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroClockMin.setStatus(_A)
class _WtWebGraphThermoBaroClockDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_WtWebGraphThermoBaroClockDay_Type.__name__=_D
_WtWebGraphThermoBaroClockDay_Object=MibScalar
wtWebGraphThermoBaroClockDay=_WtWebGraphThermoBaroClockDay_Object((1,3,6,1,4,1,5040,1,2,37,3,1,2,3,3),_WtWebGraphThermoBaroClockDay_Type())
wtWebGraphThermoBaroClockDay.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroClockDay.setStatus(_A)
class _WtWebGraphThermoBaroClockMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('wtWebGraphThermoBaroClockMonth-January',1),('wtWebGraphThermoBaroClockMonth-February',2),('wtWebGraphThermoBaroClockMonth-March',3),('wtWebGraphThermoBaroClockMonth-April',4),('wtWebGraphThermoBaroClockMonth-May',5),('wtWebGraphThermoBaroClockMonth-June',6),('wtWebGraphThermoBaroClockMonth-July',7),('wtWebGraphThermoBaroClockMonth-August',8),('wtWebGraphThermoBaroClockMonth-September',9),('wtWebGraphThermoBaroClockMonth-October',10),('wtWebGraphThermoBaroClockMonth-November',11),('wtWebGraphThermoBaroClockMonth-December',12)))
_WtWebGraphThermoBaroClockMonth_Type.__name__=_D
_WtWebGraphThermoBaroClockMonth_Object=MibScalar
wtWebGraphThermoBaroClockMonth=_WtWebGraphThermoBaroClockMonth_Object((1,3,6,1,4,1,5040,1,2,37,3,1,2,3,4),_WtWebGraphThermoBaroClockMonth_Type())
wtWebGraphThermoBaroClockMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroClockMonth.setStatus(_A)
class _WtWebGraphThermoBaroClockYear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtWebGraphThermoBaroClockYear_Type.__name__=_D
_WtWebGraphThermoBaroClockYear_Object=MibScalar
wtWebGraphThermoBaroClockYear=_WtWebGraphThermoBaroClockYear_Object((1,3,6,1,4,1,5040,1,2,37,3,1,2,3,5),_WtWebGraphThermoBaroClockYear_Type())
wtWebGraphThermoBaroClockYear.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroClockYear.setStatus(_A)
_WtWebGraphThermoBaroBasic_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroBasic=_WtWebGraphThermoBaroBasic_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,1,3))
_WtWebGraphThermoBaroNetwork_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroNetwork=_WtWebGraphThermoBaroNetwork_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,1,3,1))
_WtWebGraphThermoBaroIpAddress_Type=IpAddress
_WtWebGraphThermoBaroIpAddress_Object=MibScalar
wtWebGraphThermoBaroIpAddress=_WtWebGraphThermoBaroIpAddress_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,1,1),_WtWebGraphThermoBaroIpAddress_Type())
wtWebGraphThermoBaroIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroIpAddress.setStatus(_A)
_WtWebGraphThermoBaroSubnetMask_Type=IpAddress
_WtWebGraphThermoBaroSubnetMask_Object=MibScalar
wtWebGraphThermoBaroSubnetMask=_WtWebGraphThermoBaroSubnetMask_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,1,2),_WtWebGraphThermoBaroSubnetMask_Type())
wtWebGraphThermoBaroSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroSubnetMask.setStatus(_A)
_WtWebGraphThermoBaroGateway_Type=IpAddress
_WtWebGraphThermoBaroGateway_Object=MibScalar
wtWebGraphThermoBaroGateway=_WtWebGraphThermoBaroGateway_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,1,3),_WtWebGraphThermoBaroGateway_Type())
wtWebGraphThermoBaroGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGateway.setStatus(_A)
_WtWebGraphThermoBaroDnsServer1_Type=OctetString
_WtWebGraphThermoBaroDnsServer1_Object=MibScalar
wtWebGraphThermoBaroDnsServer1=_WtWebGraphThermoBaroDnsServer1_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,1,4),_WtWebGraphThermoBaroDnsServer1_Type())
wtWebGraphThermoBaroDnsServer1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroDnsServer1.setStatus(_A)
_WtWebGraphThermoBaroDnsServer2_Type=OctetString
_WtWebGraphThermoBaroDnsServer2_Object=MibScalar
wtWebGraphThermoBaroDnsServer2=_WtWebGraphThermoBaroDnsServer2_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,1,5),_WtWebGraphThermoBaroDnsServer2_Type())
wtWebGraphThermoBaroDnsServer2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroDnsServer2.setStatus(_A)
_WtWebGraphThermoBaroAddConfig_Type=OctetString
_WtWebGraphThermoBaroAddConfig_Object=MibScalar
wtWebGraphThermoBaroAddConfig=_WtWebGraphThermoBaroAddConfig_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,1,6),_WtWebGraphThermoBaroAddConfig_Type())
wtWebGraphThermoBaroAddConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAddConfig.setStatus(_A)
_WtWebGraphThermoBaroHTTP_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroHTTP=_WtWebGraphThermoBaroHTTP_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,1,3,2))
_WtWebGraphThermoBaroStartup_Type=OctetString
_WtWebGraphThermoBaroStartup_Object=MibScalar
wtWebGraphThermoBaroStartup=_WtWebGraphThermoBaroStartup_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,2,1),_WtWebGraphThermoBaroStartup_Type())
wtWebGraphThermoBaroStartup.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroStartup.setStatus(_A)
_WtWebGraphThermoBaroGetHeaderEnable_Type=OctetString
_WtWebGraphThermoBaroGetHeaderEnable_Object=MibScalar
wtWebGraphThermoBaroGetHeaderEnable=_WtWebGraphThermoBaroGetHeaderEnable_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,2,2),_WtWebGraphThermoBaroGetHeaderEnable_Type())
wtWebGraphThermoBaroGetHeaderEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGetHeaderEnable.setStatus(_A)
class _WtWebGraphThermoBaroHttpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphThermoBaroHttpPort_Type.__name__=_D
_WtWebGraphThermoBaroHttpPort_Object=MibScalar
wtWebGraphThermoBaroHttpPort=_WtWebGraphThermoBaroHttpPort_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,2,3),_WtWebGraphThermoBaroHttpPort_Type())
wtWebGraphThermoBaroHttpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroHttpPort.setStatus(_A)
_WtWebGraphThermoBaroMail_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroMail=_WtWebGraphThermoBaroMail_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,1,3,3))
_WtWebGraphThermoBaroMailAdName_Type=OctetString
_WtWebGraphThermoBaroMailAdName_Object=MibScalar
wtWebGraphThermoBaroMailAdName=_WtWebGraphThermoBaroMailAdName_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,3,1),_WtWebGraphThermoBaroMailAdName_Type())
wtWebGraphThermoBaroMailAdName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroMailAdName.setStatus(_A)
_WtWebGraphThermoBaroMailReply_Type=OctetString
_WtWebGraphThermoBaroMailReply_Object=MibScalar
wtWebGraphThermoBaroMailReply=_WtWebGraphThermoBaroMailReply_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,3,2),_WtWebGraphThermoBaroMailReply_Type())
wtWebGraphThermoBaroMailReply.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroMailReply.setStatus(_A)
_WtWebGraphThermoBaroMailServer_Type=OctetString
_WtWebGraphThermoBaroMailServer_Object=MibScalar
wtWebGraphThermoBaroMailServer=_WtWebGraphThermoBaroMailServer_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,3,3),_WtWebGraphThermoBaroMailServer_Type())
wtWebGraphThermoBaroMailServer.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroMailServer.setStatus(_A)
_WtWebioAn1MailEnable_Type=OctetString
_WtWebioAn1MailEnable_Object=MibScalar
wtWebioAn1MailEnable=_WtWebioAn1MailEnable_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,3,4),_WtWebioAn1MailEnable_Type())
wtWebioAn1MailEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebioAn1MailEnable.setStatus(_A)
class _WtWebGraphThermoBaroMailAuthentication_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoBaroMailAuthentication_Type.__name__=_F
_WtWebGraphThermoBaroMailAuthentication_Object=MibScalar
wtWebGraphThermoBaroMailAuthentication=_WtWebGraphThermoBaroMailAuthentication_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,3,5),_WtWebGraphThermoBaroMailAuthentication_Type())
wtWebGraphThermoBaroMailAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroMailAuthentication.setStatus(_A)
_WtWebGraphThermoBaroMailAuthUser_Type=OctetString
_WtWebGraphThermoBaroMailAuthUser_Object=MibScalar
wtWebGraphThermoBaroMailAuthUser=_WtWebGraphThermoBaroMailAuthUser_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,3,6),_WtWebGraphThermoBaroMailAuthUser_Type())
wtWebGraphThermoBaroMailAuthUser.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroMailAuthUser.setStatus(_A)
_WtWebGraphThermoBaroMailAuthPassword_Type=OctetString
_WtWebGraphThermoBaroMailAuthPassword_Object=MibScalar
wtWebGraphThermoBaroMailAuthPassword=_WtWebGraphThermoBaroMailAuthPassword_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,3,7),_WtWebGraphThermoBaroMailAuthPassword_Type())
wtWebGraphThermoBaroMailAuthPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroMailAuthPassword.setStatus(_A)
_WtWebGraphThermoBaroMailPop3Server_Type=OctetString
_WtWebGraphThermoBaroMailPop3Server_Object=MibScalar
wtWebGraphThermoBaroMailPop3Server=_WtWebGraphThermoBaroMailPop3Server_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,3,8),_WtWebGraphThermoBaroMailPop3Server_Type())
wtWebGraphThermoBaroMailPop3Server.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroMailPop3Server.setStatus(_A)
_WtWebGraphThermoBaroSNMP_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroSNMP=_WtWebGraphThermoBaroSNMP_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,1,3,4))
_WtWebGraphThermoBaroSnmpCommunityStringRead_Type=OctetString
_WtWebGraphThermoBaroSnmpCommunityStringRead_Object=MibScalar
wtWebGraphThermoBaroSnmpCommunityStringRead=_WtWebGraphThermoBaroSnmpCommunityStringRead_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,4,1),_WtWebGraphThermoBaroSnmpCommunityStringRead_Type())
wtWebGraphThermoBaroSnmpCommunityStringRead.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroSnmpCommunityStringRead.setStatus(_A)
_WtWebGraphThermoBaroSnmpCommunityStringReadWrite_Type=OctetString
_WtWebGraphThermoBaroSnmpCommunityStringReadWrite_Object=MibScalar
wtWebGraphThermoBaroSnmpCommunityStringReadWrite=_WtWebGraphThermoBaroSnmpCommunityStringReadWrite_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,4,2),_WtWebGraphThermoBaroSnmpCommunityStringReadWrite_Type())
wtWebGraphThermoBaroSnmpCommunityStringReadWrite.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroSnmpCommunityStringReadWrite.setStatus(_A)
_WtWebGraphThermoBaroSystemTrapManagerIP_Type=OctetString
_WtWebGraphThermoBaroSystemTrapManagerIP_Object=MibScalar
wtWebGraphThermoBaroSystemTrapManagerIP=_WtWebGraphThermoBaroSystemTrapManagerIP_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,4,3),_WtWebGraphThermoBaroSystemTrapManagerIP_Type())
wtWebGraphThermoBaroSystemTrapManagerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroSystemTrapManagerIP.setStatus(_A)
class _WtWebGraphThermoBaroSystemTrapEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoBaroSystemTrapEnable_Type.__name__=_F
_WtWebGraphThermoBaroSystemTrapEnable_Object=MibScalar
wtWebGraphThermoBaroSystemTrapEnable=_WtWebGraphThermoBaroSystemTrapEnable_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,4,4),_WtWebGraphThermoBaroSystemTrapEnable_Type())
wtWebGraphThermoBaroSystemTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroSystemTrapEnable.setStatus(_A)
_WtWebGraphThermoBaroSnmpEnable_Type=OctetString
_WtWebGraphThermoBaroSnmpEnable_Object=MibScalar
wtWebGraphThermoBaroSnmpEnable=_WtWebGraphThermoBaroSnmpEnable_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,4,5),_WtWebGraphThermoBaroSnmpEnable_Type())
wtWebGraphThermoBaroSnmpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroSnmpEnable.setStatus(_A)
_WtWebGraphThermoBaroSnmpCommunityStringTrap_Type=OctetString
_WtWebGraphThermoBaroSnmpCommunityStringTrap_Object=MibScalar
wtWebGraphThermoBaroSnmpCommunityStringTrap=_WtWebGraphThermoBaroSnmpCommunityStringTrap_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,4,6),_WtWebGraphThermoBaroSnmpCommunityStringTrap_Type())
wtWebGraphThermoBaroSnmpCommunityStringTrap.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroSnmpCommunityStringTrap.setStatus(_A)
_WtWebGraphThermoBaroUDP_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroUDP=_WtWebGraphThermoBaroUDP_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,1,3,5))
class _WtWebGraphThermoBaroUdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphThermoBaroUdpPort_Type.__name__=_D
_WtWebGraphThermoBaroUdpPort_Object=MibScalar
wtWebGraphThermoBaroUdpPort=_WtWebGraphThermoBaroUdpPort_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,5,1),_WtWebGraphThermoBaroUdpPort_Type())
wtWebGraphThermoBaroUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroUdpPort.setStatus(_A)
_WtWebGraphThermoBaroUdpEnable_Type=OctetString
_WtWebGraphThermoBaroUdpEnable_Object=MibScalar
wtWebGraphThermoBaroUdpEnable=_WtWebGraphThermoBaroUdpEnable_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,5,2),_WtWebGraphThermoBaroUdpEnable_Type())
wtWebGraphThermoBaroUdpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroUdpEnable.setStatus(_A)
_WtWebGraphThermoBaroSyslog_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroSyslog=_WtWebGraphThermoBaroSyslog_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,1,3,6))
_WtWebGraphThermoBaroSyslogServerIP_Type=OctetString
_WtWebGraphThermoBaroSyslogServerIP_Object=MibScalar
wtWebGraphThermoBaroSyslogServerIP=_WtWebGraphThermoBaroSyslogServerIP_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,6,1),_WtWebGraphThermoBaroSyslogServerIP_Type())
wtWebGraphThermoBaroSyslogServerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroSyslogServerIP.setStatus(_A)
_WtWebGraphThermoBaroSyslogServerPort_Type=Integer32
_WtWebGraphThermoBaroSyslogServerPort_Object=MibScalar
wtWebGraphThermoBaroSyslogServerPort=_WtWebGraphThermoBaroSyslogServerPort_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,6,2),_WtWebGraphThermoBaroSyslogServerPort_Type())
wtWebGraphThermoBaroSyslogServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroSyslogServerPort.setStatus(_A)
class _WtWebGraphThermoBaroSyslogSystemMessagesEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoBaroSyslogSystemMessagesEnable_Type.__name__=_F
_WtWebGraphThermoBaroSyslogSystemMessagesEnable_Object=MibScalar
wtWebGraphThermoBaroSyslogSystemMessagesEnable=_WtWebGraphThermoBaroSyslogSystemMessagesEnable_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,6,3),_WtWebGraphThermoBaroSyslogSystemMessagesEnable_Type())
wtWebGraphThermoBaroSyslogSystemMessagesEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroSyslogSystemMessagesEnable.setStatus(_A)
_WtWebGraphThermoBaroSyslogEnable_Type=OctetString
_WtWebGraphThermoBaroSyslogEnable_Object=MibScalar
wtWebGraphThermoBaroSyslogEnable=_WtWebGraphThermoBaroSyslogEnable_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,6,4),_WtWebGraphThermoBaroSyslogEnable_Type())
wtWebGraphThermoBaroSyslogEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroSyslogEnable.setStatus(_A)
_WtWebGraphThermoBaroFTP_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroFTP=_WtWebGraphThermoBaroFTP_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,1,3,7))
_WtWebGraphThermoBaroFTPServerIP_Type=OctetString
_WtWebGraphThermoBaroFTPServerIP_Object=MibScalar
wtWebGraphThermoBaroFTPServerIP=_WtWebGraphThermoBaroFTPServerIP_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,7,1),_WtWebGraphThermoBaroFTPServerIP_Type())
wtWebGraphThermoBaroFTPServerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroFTPServerIP.setStatus(_A)
_WtWebGraphThermoBaroFTPServerControlPort_Type=Integer32
_WtWebGraphThermoBaroFTPServerControlPort_Object=MibScalar
wtWebGraphThermoBaroFTPServerControlPort=_WtWebGraphThermoBaroFTPServerControlPort_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,7,2),_WtWebGraphThermoBaroFTPServerControlPort_Type())
wtWebGraphThermoBaroFTPServerControlPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroFTPServerControlPort.setStatus(_A)
_WtWebGraphThermoBaroFTPUserName_Type=OctetString
_WtWebGraphThermoBaroFTPUserName_Object=MibScalar
wtWebGraphThermoBaroFTPUserName=_WtWebGraphThermoBaroFTPUserName_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,7,3),_WtWebGraphThermoBaroFTPUserName_Type())
wtWebGraphThermoBaroFTPUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroFTPUserName.setStatus(_A)
_WtWebGraphThermoBaroFTPPassword_Type=OctetString
_WtWebGraphThermoBaroFTPPassword_Object=MibScalar
wtWebGraphThermoBaroFTPPassword=_WtWebGraphThermoBaroFTPPassword_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,7,4),_WtWebGraphThermoBaroFTPPassword_Type())
wtWebGraphThermoBaroFTPPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroFTPPassword.setStatus(_A)
_WtWebGraphThermoBaroFTPAccount_Type=OctetString
_WtWebGraphThermoBaroFTPAccount_Object=MibScalar
wtWebGraphThermoBaroFTPAccount=_WtWebGraphThermoBaroFTPAccount_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,7,5),_WtWebGraphThermoBaroFTPAccount_Type())
wtWebGraphThermoBaroFTPAccount.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroFTPAccount.setStatus(_A)
_WtWebGraphThermoBaroFTPOption_Type=OctetString
_WtWebGraphThermoBaroFTPOption_Object=MibScalar
wtWebGraphThermoBaroFTPOption=_WtWebGraphThermoBaroFTPOption_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,7,6),_WtWebGraphThermoBaroFTPOption_Type())
wtWebGraphThermoBaroFTPOption.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroFTPOption.setStatus(_A)
_WtWebGraphThermoBaroFTPEnable_Type=OctetString
_WtWebGraphThermoBaroFTPEnable_Object=MibScalar
wtWebGraphThermoBaroFTPEnable=_WtWebGraphThermoBaroFTPEnable_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,7,7),_WtWebGraphThermoBaroFTPEnable_Type())
wtWebGraphThermoBaroFTPEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroFTPEnable.setStatus(_A)
_WtWebGraphThermoBaroRSS_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroRSS=_WtWebGraphThermoBaroRSS_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,1,3,8))
_WtWebGraphThermoBaroRSSChannelTitle_Type=OctetString
_WtWebGraphThermoBaroRSSChannelTitle_Object=MibScalar
wtWebGraphThermoBaroRSSChannelTitle=_WtWebGraphThermoBaroRSSChannelTitle_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,8,1),_WtWebGraphThermoBaroRSSChannelTitle_Type())
wtWebGraphThermoBaroRSSChannelTitle.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroRSSChannelTitle.setStatus(_A)
_WtWebGraphThermoBaroRSSChannelLink_Type=OctetString
_WtWebGraphThermoBaroRSSChannelLink_Object=MibScalar
wtWebGraphThermoBaroRSSChannelLink=_WtWebGraphThermoBaroRSSChannelLink_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,8,2),_WtWebGraphThermoBaroRSSChannelLink_Type())
wtWebGraphThermoBaroRSSChannelLink.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroRSSChannelLink.setStatus(_A)
_WtWebGraphThermoBaroRSSChannelDescription_Type=OctetString
_WtWebGraphThermoBaroRSSChannelDescription_Object=MibScalar
wtWebGraphThermoBaroRSSChannelDescription=_WtWebGraphThermoBaroRSSChannelDescription_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,8,3),_WtWebGraphThermoBaroRSSChannelDescription_Type())
wtWebGraphThermoBaroRSSChannelDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroRSSChannelDescription.setStatus(_A)
_WtWebGraphThermoBaroRSSChannelImage_Type=OctetString
_WtWebGraphThermoBaroRSSChannelImage_Object=MibScalar
wtWebGraphThermoBaroRSSChannelImage=_WtWebGraphThermoBaroRSSChannelImage_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,8,4),_WtWebGraphThermoBaroRSSChannelImage_Type())
wtWebGraphThermoBaroRSSChannelImage.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroRSSChannelImage.setStatus(_A)
_WtWebGraphThermoBaroRSSChannelImageTitle_Type=OctetString
_WtWebGraphThermoBaroRSSChannelImageTitle_Object=MibScalar
wtWebGraphThermoBaroRSSChannelImageTitle=_WtWebGraphThermoBaroRSSChannelImageTitle_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,8,5),_WtWebGraphThermoBaroRSSChannelImageTitle_Type())
wtWebGraphThermoBaroRSSChannelImageTitle.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroRSSChannelImageTitle.setStatus(_A)
_WtWebGraphThermoBaroRSSChannelImageLink_Type=OctetString
_WtWebGraphThermoBaroRSSChannelImageLink_Object=MibScalar
wtWebGraphThermoBaroRSSChannelImageLink=_WtWebGraphThermoBaroRSSChannelImageLink_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,8,6),_WtWebGraphThermoBaroRSSChannelImageLink_Type())
wtWebGraphThermoBaroRSSChannelImageLink.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroRSSChannelImageLink.setStatus(_A)
_WtWebGraphThermoBaroRSSChannelItemTitle_Type=OctetString
_WtWebGraphThermoBaroRSSChannelItemTitle_Object=MibScalar
wtWebGraphThermoBaroRSSChannelItemTitle=_WtWebGraphThermoBaroRSSChannelItemTitle_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,8,7),_WtWebGraphThermoBaroRSSChannelItemTitle_Type())
wtWebGraphThermoBaroRSSChannelItemTitle.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroRSSChannelItemTitle.setStatus(_A)
_WtWebGraphThermoBaroRSSChannelItemLink_Type=OctetString
_WtWebGraphThermoBaroRSSChannelItemLink_Object=MibScalar
wtWebGraphThermoBaroRSSChannelItemLink=_WtWebGraphThermoBaroRSSChannelItemLink_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,8,8),_WtWebGraphThermoBaroRSSChannelItemLink_Type())
wtWebGraphThermoBaroRSSChannelItemLink.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroRSSChannelItemLink.setStatus(_A)
_WtWebGraphThermoBaroRSSChannelItemDescription_Type=OctetString
_WtWebGraphThermoBaroRSSChannelItemDescription_Object=MibScalar
wtWebGraphThermoBaroRSSChannelItemDescription=_WtWebGraphThermoBaroRSSChannelItemDescription_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,8,9),_WtWebGraphThermoBaroRSSChannelItemDescription_Type())
wtWebGraphThermoBaroRSSChannelItemDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroRSSChannelItemDescription.setStatus(_A)
_WtWebGraphThermoBaroRSSChannelItemQuantity_Type=OctetString
_WtWebGraphThermoBaroRSSChannelItemQuantity_Object=MibScalar
wtWebGraphThermoBaroRSSChannelItemQuantity=_WtWebGraphThermoBaroRSSChannelItemQuantity_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,8,10),_WtWebGraphThermoBaroRSSChannelItemQuantity_Type())
wtWebGraphThermoBaroRSSChannelItemQuantity.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroRSSChannelItemQuantity.setStatus(_A)
_WtWebGraphThermoBaroLanguage_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroLanguage=_WtWebGraphThermoBaroLanguage_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,1,3,9))
_WtWebGraphThermoBaroLanguageSelect_Type=OctetString
_WtWebGraphThermoBaroLanguageSelect_Object=MibScalar
wtWebGraphThermoBaroLanguageSelect=_WtWebGraphThermoBaroLanguageSelect_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,9,1),_WtWebGraphThermoBaroLanguageSelect_Type())
wtWebGraphThermoBaroLanguageSelect.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroLanguageSelect.setStatus(_A)
_WtWebGraphThermoBaroMQTT_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroMQTT=_WtWebGraphThermoBaroMQTT_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,1,3,12))
_WtWebGraphThermoBaroMQTTEnable_Type=OctetString
_WtWebGraphThermoBaroMQTTEnable_Object=MibScalar
wtWebGraphThermoBaroMQTTEnable=_WtWebGraphThermoBaroMQTTEnable_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,12,1),_WtWebGraphThermoBaroMQTTEnable_Type())
wtWebGraphThermoBaroMQTTEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroMQTTEnable.setStatus(_A)
_WtWebGraphThermoBaroMQTTBrockerIP_Type=OctetString
_WtWebGraphThermoBaroMQTTBrockerIP_Object=MibScalar
wtWebGraphThermoBaroMQTTBrockerIP=_WtWebGraphThermoBaroMQTTBrockerIP_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,12,2),_WtWebGraphThermoBaroMQTTBrockerIP_Type())
wtWebGraphThermoBaroMQTTBrockerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroMQTTBrockerIP.setStatus(_A)
_WtWebGraphThermoBaroMQTTUserName_Type=OctetString
_WtWebGraphThermoBaroMQTTUserName_Object=MibScalar
wtWebGraphThermoBaroMQTTUserName=_WtWebGraphThermoBaroMQTTUserName_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,12,3),_WtWebGraphThermoBaroMQTTUserName_Type())
wtWebGraphThermoBaroMQTTUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroMQTTUserName.setStatus(_A)
_WtWebGraphThermoBaroMQTTPassword_Type=OctetString
_WtWebGraphThermoBaroMQTTPassword_Object=MibScalar
wtWebGraphThermoBaroMQTTPassword=_WtWebGraphThermoBaroMQTTPassword_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,12,4),_WtWebGraphThermoBaroMQTTPassword_Type())
wtWebGraphThermoBaroMQTTPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroMQTTPassword.setStatus(_A)
_WtWebGraphThermoBaroMQTTLocalPort_Type=Integer32
_WtWebGraphThermoBaroMQTTLocalPort_Object=MibScalar
wtWebGraphThermoBaroMQTTLocalPort=_WtWebGraphThermoBaroMQTTLocalPort_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,12,5),_WtWebGraphThermoBaroMQTTLocalPort_Type())
wtWebGraphThermoBaroMQTTLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroMQTTLocalPort.setStatus(_A)
_WtWebGraphThermoBaroMQTTBrokerServerPort_Type=Integer32
_WtWebGraphThermoBaroMQTTBrokerServerPort_Object=MibScalar
wtWebGraphThermoBaroMQTTBrokerServerPort=_WtWebGraphThermoBaroMQTTBrokerServerPort_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,12,6),_WtWebGraphThermoBaroMQTTBrokerServerPort_Type())
wtWebGraphThermoBaroMQTTBrokerServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroMQTTBrokerServerPort.setStatus(_A)
_WtWebGraphThermoBaroMQTTInterval_Type=Integer32
_WtWebGraphThermoBaroMQTTInterval_Object=MibScalar
wtWebGraphThermoBaroMQTTInterval=_WtWebGraphThermoBaroMQTTInterval_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,12,7),_WtWebGraphThermoBaroMQTTInterval_Type())
wtWebGraphThermoBaroMQTTInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroMQTTInterval.setStatus(_A)
_WtWebGraphThermoBaroREST_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroREST=_WtWebGraphThermoBaroREST_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,1,3,13))
_WtWebGraphThermoBaroRESTEnable_Type=OctetString
_WtWebGraphThermoBaroRESTEnable_Object=MibScalar
wtWebGraphThermoBaroRESTEnable=_WtWebGraphThermoBaroRESTEnable_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,13,1),_WtWebGraphThermoBaroRESTEnable_Type())
wtWebGraphThermoBaroRESTEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroRESTEnable.setStatus(_A)
_WtWebGraphThermoBaroRESTDigestAuthEnable_Type=OctetString
_WtWebGraphThermoBaroRESTDigestAuthEnable_Object=MibScalar
wtWebGraphThermoBaroRESTDigestAuthEnable=_WtWebGraphThermoBaroRESTDigestAuthEnable_Object((1,3,6,1,4,1,5040,1,2,37,3,1,3,13,2),_WtWebGraphThermoBaroRESTDigestAuthEnable_Type())
wtWebGraphThermoBaroRESTDigestAuthEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroRESTDigestAuthEnable.setStatus(_A)
_WtWebGraphThermoBaroDatalogger_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroDatalogger=_WtWebGraphThermoBaroDatalogger_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,1,4))
class _WtWebGraphThermoBaroLoggerTimebase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('wtWebGraphThermoBaroDatalogger-1Min',1),('wtWebGraphThermoBaroDatalogger-5Min',2),('wtWebGraphThermoBaroDatalogger-15Min',3),('wtWebGraphThermoBaroDatalogger-60Min',4)))
_WtWebGraphThermoBaroLoggerTimebase_Type.__name__=_D
_WtWebGraphThermoBaroLoggerTimebase_Object=MibScalar
wtWebGraphThermoBaroLoggerTimebase=_WtWebGraphThermoBaroLoggerTimebase_Object((1,3,6,1,4,1,5040,1,2,37,3,1,4,1),_WtWebGraphThermoBaroLoggerTimebase_Type())
wtWebGraphThermoBaroLoggerTimebase.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroLoggerTimebase.setStatus(_A)
class _WtWebGraphThermoBaroLoggerSensorSel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoBaroLoggerSensorSel_Type.__name__=_F
_WtWebGraphThermoBaroLoggerSensorSel_Object=MibScalar
wtWebGraphThermoBaroLoggerSensorSel=_WtWebGraphThermoBaroLoggerSensorSel_Object((1,3,6,1,4,1,5040,1,2,37,3,1,4,2),_WtWebGraphThermoBaroLoggerSensorSel_Type())
wtWebGraphThermoBaroLoggerSensorSel.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroLoggerSensorSel.setStatus(_A)
_WtWebGraphThermoBaroAlarm_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroAlarm=_WtWebGraphThermoBaroAlarm_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,1,5))
class _WtWebGraphThermoBaroAlarmCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_WtWebGraphThermoBaroAlarmCount_Type.__name__=_D
_WtWebGraphThermoBaroAlarmCount_Object=MibScalar
wtWebGraphThermoBaroAlarmCount=_WtWebGraphThermoBaroAlarmCount_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,1),_WtWebGraphThermoBaroAlarmCount_Type())
wtWebGraphThermoBaroAlarmCount.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmCount.setStatus(_A)
_WtWebGraphThermoBaroAlarmIfTable_Object=MibTable
wtWebGraphThermoBaroAlarmIfTable=_WtWebGraphThermoBaroAlarmIfTable_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,2))
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmIfTable.setStatus(_A)
_WtWebGraphThermoBaroAlarmIfEntry_Object=MibTableRow
wtWebGraphThermoBaroAlarmIfEntry=_WtWebGraphThermoBaroAlarmIfEntry_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,2,1))
wtWebGraphThermoBaroAlarmIfEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmIfEntry.setStatus(_A)
class _WtWebGraphThermoBaroAlarmNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_WtWebGraphThermoBaroAlarmNo_Type.__name__=_D
_WtWebGraphThermoBaroAlarmNo_Object=MibTableColumn
wtWebGraphThermoBaroAlarmNo=_WtWebGraphThermoBaroAlarmNo_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,2,1,1),_WtWebGraphThermoBaroAlarmNo_Type())
wtWebGraphThermoBaroAlarmNo.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmNo.setStatus(_A)
_WtWebGraphThermoBaroAlarmTable_Object=MibTable
wtWebGraphThermoBaroAlarmTable=_WtWebGraphThermoBaroAlarmTable_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3))
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmTable.setStatus(_A)
_WtWebGraphThermoBaroAlarmEntry_Object=MibTableRow
wtWebGraphThermoBaroAlarmEntry=_WtWebGraphThermoBaroAlarmEntry_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1))
wtWebGraphThermoBaroAlarmEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmEntry.setStatus(_A)
class _WtWebGraphThermoBaroAlarmTrigger_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoBaroAlarmTrigger_Type.__name__=_F
_WtWebGraphThermoBaroAlarmTrigger_Object=MibTableColumn
wtWebGraphThermoBaroAlarmTrigger=_WtWebGraphThermoBaroAlarmTrigger_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,1),_WtWebGraphThermoBaroAlarmTrigger_Type())
wtWebGraphThermoBaroAlarmTrigger.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmTrigger.setStatus(_A)
_WtWebGraphThermoBaroAlarmMin_Type=OctetString
_WtWebGraphThermoBaroAlarmMin_Object=MibTableColumn
wtWebGraphThermoBaroAlarmMin=_WtWebGraphThermoBaroAlarmMin_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,2),_WtWebGraphThermoBaroAlarmMin_Type())
wtWebGraphThermoBaroAlarmMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmMin.setStatus(_A)
_WtWebGraphThermoBaroAlarmMax_Type=OctetString
_WtWebGraphThermoBaroAlarmMax_Object=MibTableColumn
wtWebGraphThermoBaroAlarmMax=_WtWebGraphThermoBaroAlarmMax_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,3),_WtWebGraphThermoBaroAlarmMax_Type())
wtWebGraphThermoBaroAlarmMax.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmMax.setStatus(_A)
_WtWebGraphThermoBaroAlarmHysteresis_Type=OctetString
_WtWebGraphThermoBaroAlarmHysteresis_Object=MibTableColumn
wtWebGraphThermoBaroAlarmHysteresis=_WtWebGraphThermoBaroAlarmHysteresis_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,4),_WtWebGraphThermoBaroAlarmHysteresis_Type())
wtWebGraphThermoBaroAlarmHysteresis.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmHysteresis.setStatus(_A)
_WtWebGraphThermoBaroAlarmDelay_Type=OctetString
_WtWebGraphThermoBaroAlarmDelay_Object=MibTableColumn
wtWebGraphThermoBaroAlarmDelay=_WtWebGraphThermoBaroAlarmDelay_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,5),_WtWebGraphThermoBaroAlarmDelay_Type())
wtWebGraphThermoBaroAlarmDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmDelay.setStatus(_A)
_WtWebGraphThermoBaroAlarmInterval_Type=OctetString
_WtWebGraphThermoBaroAlarmInterval_Object=MibTableColumn
wtWebGraphThermoBaroAlarmInterval=_WtWebGraphThermoBaroAlarmInterval_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,6),_WtWebGraphThermoBaroAlarmInterval_Type())
wtWebGraphThermoBaroAlarmInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmInterval.setStatus(_A)
class _WtWebGraphThermoBaroAlarmEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoBaroAlarmEnable_Type.__name__=_F
_WtWebGraphThermoBaroAlarmEnable_Object=MibTableColumn
wtWebGraphThermoBaroAlarmEnable=_WtWebGraphThermoBaroAlarmEnable_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,7),_WtWebGraphThermoBaroAlarmEnable_Type())
wtWebGraphThermoBaroAlarmEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmEnable.setStatus(_A)
_WtWebGraphThermoBaroAlarmEMailAddr_Type=OctetString
_WtWebGraphThermoBaroAlarmEMailAddr_Object=MibTableColumn
wtWebGraphThermoBaroAlarmEMailAddr=_WtWebGraphThermoBaroAlarmEMailAddr_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,8),_WtWebGraphThermoBaroAlarmEMailAddr_Type())
wtWebGraphThermoBaroAlarmEMailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmEMailAddr.setStatus(_A)
_WtWebGraphThermoBaroAlarmMailSubject_Type=OctetString
_WtWebGraphThermoBaroAlarmMailSubject_Object=MibTableColumn
wtWebGraphThermoBaroAlarmMailSubject=_WtWebGraphThermoBaroAlarmMailSubject_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,9),_WtWebGraphThermoBaroAlarmMailSubject_Type())
wtWebGraphThermoBaroAlarmMailSubject.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmMailSubject.setStatus(_A)
_WtWebGraphThermoBaroAlarmMailText_Type=OctetString
_WtWebGraphThermoBaroAlarmMailText_Object=MibTableColumn
wtWebGraphThermoBaroAlarmMailText=_WtWebGraphThermoBaroAlarmMailText_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,10),_WtWebGraphThermoBaroAlarmMailText_Type())
wtWebGraphThermoBaroAlarmMailText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmMailText.setStatus(_A)
_WtWebGraphThermoBaroAlarmManagerIP_Type=OctetString
_WtWebGraphThermoBaroAlarmManagerIP_Object=MibTableColumn
wtWebGraphThermoBaroAlarmManagerIP=_WtWebGraphThermoBaroAlarmManagerIP_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,11),_WtWebGraphThermoBaroAlarmManagerIP_Type())
wtWebGraphThermoBaroAlarmManagerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmManagerIP.setStatus(_A)
_WtWebGraphThermoBaroAlarmTrapText_Type=OctetString
_WtWebGraphThermoBaroAlarmTrapText_Object=MibTableColumn
wtWebGraphThermoBaroAlarmTrapText=_WtWebGraphThermoBaroAlarmTrapText_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,12),_WtWebGraphThermoBaroAlarmTrapText_Type())
wtWebGraphThermoBaroAlarmTrapText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmTrapText.setStatus(_A)
class _WtWebGraphThermoBaroAlarmMailOptions_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoBaroAlarmMailOptions_Type.__name__=_F
_WtWebGraphThermoBaroAlarmMailOptions_Object=MibTableColumn
wtWebGraphThermoBaroAlarmMailOptions=_WtWebGraphThermoBaroAlarmMailOptions_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,13),_WtWebGraphThermoBaroAlarmMailOptions_Type())
wtWebGraphThermoBaroAlarmMailOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmMailOptions.setStatus(_A)
_WtWebGraphThermoBaroAlarmTcpIpAddr_Type=OctetString
_WtWebGraphThermoBaroAlarmTcpIpAddr_Object=MibTableColumn
wtWebGraphThermoBaroAlarmTcpIpAddr=_WtWebGraphThermoBaroAlarmTcpIpAddr_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,14),_WtWebGraphThermoBaroAlarmTcpIpAddr_Type())
wtWebGraphThermoBaroAlarmTcpIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmTcpIpAddr.setStatus(_A)
class _WtWebGraphThermoBaroAlarmTcpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphThermoBaroAlarmTcpPort_Type.__name__=_D
_WtWebGraphThermoBaroAlarmTcpPort_Object=MibTableColumn
wtWebGraphThermoBaroAlarmTcpPort=_WtWebGraphThermoBaroAlarmTcpPort_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,15),_WtWebGraphThermoBaroAlarmTcpPort_Type())
wtWebGraphThermoBaroAlarmTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmTcpPort.setStatus(_A)
_WtWebGraphThermoBaroAlarmTcpText_Type=OctetString
_WtWebGraphThermoBaroAlarmTcpText_Object=MibTableColumn
wtWebGraphThermoBaroAlarmTcpText=_WtWebGraphThermoBaroAlarmTcpText_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,16),_WtWebGraphThermoBaroAlarmTcpText_Type())
wtWebGraphThermoBaroAlarmTcpText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmTcpText.setStatus(_A)
_WtWebGraphThermoBaroAlarmClearMailSubject_Type=OctetString
_WtWebGraphThermoBaroAlarmClearMailSubject_Object=MibTableColumn
wtWebGraphThermoBaroAlarmClearMailSubject=_WtWebGraphThermoBaroAlarmClearMailSubject_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,17),_WtWebGraphThermoBaroAlarmClearMailSubject_Type())
wtWebGraphThermoBaroAlarmClearMailSubject.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmClearMailSubject.setStatus(_A)
_WtWebGraphThermoBaroAlarmClearMailText_Type=OctetString
_WtWebGraphThermoBaroAlarmClearMailText_Object=MibTableColumn
wtWebGraphThermoBaroAlarmClearMailText=_WtWebGraphThermoBaroAlarmClearMailText_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,18),_WtWebGraphThermoBaroAlarmClearMailText_Type())
wtWebGraphThermoBaroAlarmClearMailText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmClearMailText.setStatus(_A)
_WtWebGraphThermoBaroAlarmClearTrapText_Type=OctetString
_WtWebGraphThermoBaroAlarmClearTrapText_Object=MibTableColumn
wtWebGraphThermoBaroAlarmClearTrapText=_WtWebGraphThermoBaroAlarmClearTrapText_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,19),_WtWebGraphThermoBaroAlarmClearTrapText_Type())
wtWebGraphThermoBaroAlarmClearTrapText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmClearTrapText.setStatus(_A)
_WtWebGraphThermoBaroAlarmClearTcpText_Type=OctetString
_WtWebGraphThermoBaroAlarmClearTcpText_Object=MibTableColumn
wtWebGraphThermoBaroAlarmClearTcpText=_WtWebGraphThermoBaroAlarmClearTcpText_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,20),_WtWebGraphThermoBaroAlarmClearTcpText_Type())
wtWebGraphThermoBaroAlarmClearTcpText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmClearTcpText.setStatus(_A)
_WtWebGraphThermoBaroAlarmDeltaTemp_Type=OctetString
_WtWebGraphThermoBaroAlarmDeltaTemp_Object=MibTableColumn
wtWebGraphThermoBaroAlarmDeltaTemp=_WtWebGraphThermoBaroAlarmDeltaTemp_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,21),_WtWebGraphThermoBaroAlarmDeltaTemp_Type())
wtWebGraphThermoBaroAlarmDeltaTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmDeltaTemp.setStatus(_A)
_WtWebGraphThermoBaroAlarmRHMin_Type=OctetString
_WtWebGraphThermoBaroAlarmRHMin_Object=MibTableColumn
wtWebGraphThermoBaroAlarmRHMin=_WtWebGraphThermoBaroAlarmRHMin_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,22),_WtWebGraphThermoBaroAlarmRHMin_Type())
wtWebGraphThermoBaroAlarmRHMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmRHMin.setStatus(_A)
_WtWebGraphThermoBaroAlarmRHMax_Type=OctetString
_WtWebGraphThermoBaroAlarmRHMax_Object=MibTableColumn
wtWebGraphThermoBaroAlarmRHMax=_WtWebGraphThermoBaroAlarmRHMax_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,23),_WtWebGraphThermoBaroAlarmRHMax_Type())
wtWebGraphThermoBaroAlarmRHMax.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmRHMax.setStatus(_A)
_WtWebGraphThermoBaroAlarmRHHysteresis_Type=OctetString
_WtWebGraphThermoBaroAlarmRHHysteresis_Object=MibTableColumn
wtWebGraphThermoBaroAlarmRHHysteresis=_WtWebGraphThermoBaroAlarmRHHysteresis_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,24),_WtWebGraphThermoBaroAlarmRHHysteresis_Type())
wtWebGraphThermoBaroAlarmRHHysteresis.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmRHHysteresis.setStatus(_A)
_WtWebGraphThermoBaroAlarmAHMin_Type=OctetString
_WtWebGraphThermoBaroAlarmAHMin_Object=MibTableColumn
wtWebGraphThermoBaroAlarmAHMin=_WtWebGraphThermoBaroAlarmAHMin_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,25),_WtWebGraphThermoBaroAlarmAHMin_Type())
wtWebGraphThermoBaroAlarmAHMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmAHMin.setStatus(_A)
_WtWebGraphThermoBaroAlarmAHMax_Type=OctetString
_WtWebGraphThermoBaroAlarmAHMax_Object=MibTableColumn
wtWebGraphThermoBaroAlarmAHMax=_WtWebGraphThermoBaroAlarmAHMax_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,26),_WtWebGraphThermoBaroAlarmAHMax_Type())
wtWebGraphThermoBaroAlarmAHMax.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmAHMax.setStatus(_A)
_WtWebGraphThermoBaroAlarmSyslogIpAddr_Type=IpAddress
_WtWebGraphThermoBaroAlarmSyslogIpAddr_Object=MibTableColumn
wtWebGraphThermoBaroAlarmSyslogIpAddr=_WtWebGraphThermoBaroAlarmSyslogIpAddr_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,27),_WtWebGraphThermoBaroAlarmSyslogIpAddr_Type())
wtWebGraphThermoBaroAlarmSyslogIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmSyslogIpAddr.setStatus(_A)
class _WtWebGraphThermoBaroAlarmSyslogPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphThermoBaroAlarmSyslogPort_Type.__name__=_D
_WtWebGraphThermoBaroAlarmSyslogPort_Object=MibTableColumn
wtWebGraphThermoBaroAlarmSyslogPort=_WtWebGraphThermoBaroAlarmSyslogPort_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,28),_WtWebGraphThermoBaroAlarmSyslogPort_Type())
wtWebGraphThermoBaroAlarmSyslogPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmSyslogPort.setStatus(_A)
_WtWebGraphThermoBaroAlarmSyslogText_Type=OctetString
_WtWebGraphThermoBaroAlarmSyslogText_Object=MibTableColumn
wtWebGraphThermoBaroAlarmSyslogText=_WtWebGraphThermoBaroAlarmSyslogText_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,29),_WtWebGraphThermoBaroAlarmSyslogText_Type())
wtWebGraphThermoBaroAlarmSyslogText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmSyslogText.setStatus(_A)
_WtWebGraphThermoBaroAlarmSyslogClearText_Type=OctetString
_WtWebGraphThermoBaroAlarmSyslogClearText_Object=MibTableColumn
wtWebGraphThermoBaroAlarmSyslogClearText=_WtWebGraphThermoBaroAlarmSyslogClearText_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,30),_WtWebGraphThermoBaroAlarmSyslogClearText_Type())
wtWebGraphThermoBaroAlarmSyslogClearText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmSyslogClearText.setStatus(_A)
_WtWebGraphThermoBaroAlarmFtpDataPort_Type=OctetString
_WtWebGraphThermoBaroAlarmFtpDataPort_Object=MibTableColumn
wtWebGraphThermoBaroAlarmFtpDataPort=_WtWebGraphThermoBaroAlarmFtpDataPort_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,31),_WtWebGraphThermoBaroAlarmFtpDataPort_Type())
wtWebGraphThermoBaroAlarmFtpDataPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmFtpDataPort.setStatus(_A)
_WtWebGraphThermoBaroAlarmFtpFileName_Type=OctetString
_WtWebGraphThermoBaroAlarmFtpFileName_Object=MibTableColumn
wtWebGraphThermoBaroAlarmFtpFileName=_WtWebGraphThermoBaroAlarmFtpFileName_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,32),_WtWebGraphThermoBaroAlarmFtpFileName_Type())
wtWebGraphThermoBaroAlarmFtpFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmFtpFileName.setStatus(_A)
_WtWebGraphThermoBaroAlarmFtpText_Type=OctetString
_WtWebGraphThermoBaroAlarmFtpText_Object=MibTableColumn
wtWebGraphThermoBaroAlarmFtpText=_WtWebGraphThermoBaroAlarmFtpText_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,33),_WtWebGraphThermoBaroAlarmFtpText_Type())
wtWebGraphThermoBaroAlarmFtpText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmFtpText.setStatus(_A)
_WtWebGraphThermoBaroAlarmFtpClearText_Type=OctetString
_WtWebGraphThermoBaroAlarmFtpClearText_Object=MibTableColumn
wtWebGraphThermoBaroAlarmFtpClearText=_WtWebGraphThermoBaroAlarmFtpClearText_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,34),_WtWebGraphThermoBaroAlarmFtpClearText_Type())
wtWebGraphThermoBaroAlarmFtpClearText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmFtpClearText.setStatus(_A)
class _WtWebGraphThermoBaroAlarmFtpOption_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoBaroAlarmFtpOption_Type.__name__=_F
_WtWebGraphThermoBaroAlarmFtpOption_Object=MibTableColumn
wtWebGraphThermoBaroAlarmFtpOption=_WtWebGraphThermoBaroAlarmFtpOption_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,35),_WtWebGraphThermoBaroAlarmFtpOption_Type())
wtWebGraphThermoBaroAlarmFtpOption.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmFtpOption.setStatus(_A)
_WtWebGraphThermoBaroAlarmTimerCron_Type=OctetString
_WtWebGraphThermoBaroAlarmTimerCron_Object=MibTableColumn
wtWebGraphThermoBaroAlarmTimerCron=_WtWebGraphThermoBaroAlarmTimerCron_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,36),_WtWebGraphThermoBaroAlarmTimerCron_Type())
wtWebGraphThermoBaroAlarmTimerCron.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmTimerCron.setStatus(_A)
_WtWebGraphThermoBaroAlarmName_Type=OctetString
_WtWebGraphThermoBaroAlarmName_Object=MibTableColumn
wtWebGraphThermoBaroAlarmName=_WtWebGraphThermoBaroAlarmName_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,39),_WtWebGraphThermoBaroAlarmName_Type())
wtWebGraphThermoBaroAlarmName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmName.setStatus(_A)
_WtWebGraphThermoBaroAlarmActive_Type=OctetString
_WtWebGraphThermoBaroAlarmActive_Object=MibTableColumn
wtWebGraphThermoBaroAlarmActive=_WtWebGraphThermoBaroAlarmActive_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,40),_WtWebGraphThermoBaroAlarmActive_Type())
wtWebGraphThermoBaroAlarmActive.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmActive.setStatus(_A)
_WtWebGraphThermoBaroAlarmHttpReqAuthEnable_Type=OctetString
_WtWebGraphThermoBaroAlarmHttpReqAuthEnable_Object=MibTableColumn
wtWebGraphThermoBaroAlarmHttpReqAuthEnable=_WtWebGraphThermoBaroAlarmHttpReqAuthEnable_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,61),_WtWebGraphThermoBaroAlarmHttpReqAuthEnable_Type())
wtWebGraphThermoBaroAlarmHttpReqAuthEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmHttpReqAuthEnable.setStatus(_A)
_WtWebGraphThermoBaroAlarmHttpReqAuthUser_Type=OctetString
_WtWebGraphThermoBaroAlarmHttpReqAuthUser_Object=MibTableColumn
wtWebGraphThermoBaroAlarmHttpReqAuthUser=_WtWebGraphThermoBaroAlarmHttpReqAuthUser_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,62),_WtWebGraphThermoBaroAlarmHttpReqAuthUser_Type())
wtWebGraphThermoBaroAlarmHttpReqAuthUser.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmHttpReqAuthUser.setStatus(_A)
_WtWebGraphThermoBaroAlarmHttpReqAuthPassword_Type=OctetString
_WtWebGraphThermoBaroAlarmHttpReqAuthPassword_Object=MibTableColumn
wtWebGraphThermoBaroAlarmHttpReqAuthPassword=_WtWebGraphThermoBaroAlarmHttpReqAuthPassword_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,63),_WtWebGraphThermoBaroAlarmHttpReqAuthPassword_Type())
wtWebGraphThermoBaroAlarmHttpReqAuthPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmHttpReqAuthPassword.setStatus(_A)
_WtWebGraphThermoBaroAlarmHttpReqSetUrl_Type=OctetString
_WtWebGraphThermoBaroAlarmHttpReqSetUrl_Object=MibTableColumn
wtWebGraphThermoBaroAlarmHttpReqSetUrl=_WtWebGraphThermoBaroAlarmHttpReqSetUrl_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,64),_WtWebGraphThermoBaroAlarmHttpReqSetUrl_Type())
wtWebGraphThermoBaroAlarmHttpReqSetUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmHttpReqSetUrl.setStatus(_A)
_WtWebGraphThermoBaroAlarmHttpReqClearUrl_Type=OctetString
_WtWebGraphThermoBaroAlarmHttpReqClearUrl_Object=MibTableColumn
wtWebGraphThermoBaroAlarmHttpReqClearUrl=_WtWebGraphThermoBaroAlarmHttpReqClearUrl_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,65),_WtWebGraphThermoBaroAlarmHttpReqClearUrl_Type())
wtWebGraphThermoBaroAlarmHttpReqClearUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmHttpReqClearUrl.setStatus(_A)
class _WtWebGraphThermoBaroAlarmHttpReqServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphThermoBaroAlarmHttpReqServerPort_Type.__name__=_D
_WtWebGraphThermoBaroAlarmHttpReqServerPort_Object=MibTableColumn
wtWebGraphThermoBaroAlarmHttpReqServerPort=_WtWebGraphThermoBaroAlarmHttpReqServerPort_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,66),_WtWebGraphThermoBaroAlarmHttpReqServerPort_Type())
wtWebGraphThermoBaroAlarmHttpReqServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmHttpReqServerPort.setStatus(_A)
_WtWebGraphThermoBaroAlarmMqttTopicPath_Type=OctetString
_WtWebGraphThermoBaroAlarmMqttTopicPath_Object=MibTableColumn
wtWebGraphThermoBaroAlarmMqttTopicPath=_WtWebGraphThermoBaroAlarmMqttTopicPath_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,67),_WtWebGraphThermoBaroAlarmMqttTopicPath_Type())
wtWebGraphThermoBaroAlarmMqttTopicPath.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmMqttTopicPath.setStatus(_A)
_WtWebGraphThermoBaroAlarmMqttTopicSetTopic_Type=OctetString
_WtWebGraphThermoBaroAlarmMqttTopicSetTopic_Object=MibTableColumn
wtWebGraphThermoBaroAlarmMqttTopicSetTopic=_WtWebGraphThermoBaroAlarmMqttTopicSetTopic_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,68),_WtWebGraphThermoBaroAlarmMqttTopicSetTopic_Type())
wtWebGraphThermoBaroAlarmMqttTopicSetTopic.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmMqttTopicSetTopic.setStatus(_A)
_WtWebGraphThermoBaroAlarmMqttTopicClear_Type=OctetString
_WtWebGraphThermoBaroAlarmMqttTopicClear_Object=MibTableColumn
wtWebGraphThermoBaroAlarmMqttTopicClear=_WtWebGraphThermoBaroAlarmMqttTopicClear_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,69),_WtWebGraphThermoBaroAlarmMqttTopicClear_Type())
wtWebGraphThermoBaroAlarmMqttTopicClear.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmMqttTopicClear.setStatus(_A)
_WtWebGraphThermoBaroAlarmSensorLostSelection_Type=OctetString
_WtWebGraphThermoBaroAlarmSensorLostSelection_Object=MibTableColumn
wtWebGraphThermoBaroAlarmSensorLostSelection=_WtWebGraphThermoBaroAlarmSensorLostSelection_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,70),_WtWebGraphThermoBaroAlarmSensorLostSelection_Type())
wtWebGraphThermoBaroAlarmSensorLostSelection.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmSensorLostSelection.setStatus(_A)
_WtWebGraphThermoBaroAlarmLimitWindow_Type=OctetString
_WtWebGraphThermoBaroAlarmLimitWindow_Object=MibTableColumn
wtWebGraphThermoBaroAlarmLimitWindow=_WtWebGraphThermoBaroAlarmLimitWindow_Object((1,3,6,1,4,1,5040,1,2,37,3,1,5,3,1,71),_WtWebGraphThermoBaroAlarmLimitWindow_Type())
wtWebGraphThermoBaroAlarmLimitWindow.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlarmLimitWindow.setStatus(_A)
_WtWebGraphThermoBaroGraphics_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroGraphics=_WtWebGraphThermoBaroGraphics_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,1,6))
_WtWebGraphThermoBaroGraphicsBase_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroGraphicsBase=_WtWebGraphThermoBaroGraphicsBase_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,1,6,1))
_WtWebGraphThermoBaroGraphicsBaseEnable_Type=OctetString
_WtWebGraphThermoBaroGraphicsBaseEnable_Object=MibScalar
wtWebGraphThermoBaroGraphicsBaseEnable=_WtWebGraphThermoBaroGraphicsBaseEnable_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,1,1),_WtWebGraphThermoBaroGraphicsBaseEnable_Type())
wtWebGraphThermoBaroGraphicsBaseEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGraphicsBaseEnable.setStatus(_A)
_WtWebGraphThermoBaroGraphicsBaseWidth_Type=Integer32
_WtWebGraphThermoBaroGraphicsBaseWidth_Object=MibScalar
wtWebGraphThermoBaroGraphicsBaseWidth=_WtWebGraphThermoBaroGraphicsBaseWidth_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,1,2),_WtWebGraphThermoBaroGraphicsBaseWidth_Type())
wtWebGraphThermoBaroGraphicsBaseWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGraphicsBaseWidth.setStatus(_A)
_WtWebGraphThermoBaroGraphicsBaseHeight_Type=Integer32
_WtWebGraphThermoBaroGraphicsBaseHeight_Object=MibScalar
wtWebGraphThermoBaroGraphicsBaseHeight=_WtWebGraphThermoBaroGraphicsBaseHeight_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,1,3),_WtWebGraphThermoBaroGraphicsBaseHeight_Type())
wtWebGraphThermoBaroGraphicsBaseHeight.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGraphicsBaseHeight.setStatus(_A)
class _WtWebGraphThermoBaroGraphicsBaseFrameColor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_WtWebGraphThermoBaroGraphicsBaseFrameColor_Type.__name__=_F
_WtWebGraphThermoBaroGraphicsBaseFrameColor_Object=MibScalar
wtWebGraphThermoBaroGraphicsBaseFrameColor=_WtWebGraphThermoBaroGraphicsBaseFrameColor_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,1,4),_WtWebGraphThermoBaroGraphicsBaseFrameColor_Type())
wtWebGraphThermoBaroGraphicsBaseFrameColor.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGraphicsBaseFrameColor.setStatus(_A)
class _WtWebGraphThermoBaroGraphicsBaseBackgroundColor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_WtWebGraphThermoBaroGraphicsBaseBackgroundColor_Type.__name__=_F
_WtWebGraphThermoBaroGraphicsBaseBackgroundColor_Object=MibScalar
wtWebGraphThermoBaroGraphicsBaseBackgroundColor=_WtWebGraphThermoBaroGraphicsBaseBackgroundColor_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,1,5),_WtWebGraphThermoBaroGraphicsBaseBackgroundColor_Type())
wtWebGraphThermoBaroGraphicsBaseBackgroundColor.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGraphicsBaseBackgroundColor.setStatus(_A)
_WtWebGraphThermoBaroGraphicsBasePollingrate_Type=Integer32
_WtWebGraphThermoBaroGraphicsBasePollingrate_Object=MibScalar
wtWebGraphThermoBaroGraphicsBasePollingrate=_WtWebGraphThermoBaroGraphicsBasePollingrate_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,1,6),_WtWebGraphThermoBaroGraphicsBasePollingrate_Type())
wtWebGraphThermoBaroGraphicsBasePollingrate.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGraphicsBasePollingrate.setStatus(_A)
_WtWebGraphThermoBaroGraphicsSelect_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroGraphicsSelect=_WtWebGraphThermoBaroGraphicsSelect_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,1,6,2))
class _WtWebGraphThermoBaroGraphicsSelectDisplaySensorSel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoBaroGraphicsSelectDisplaySensorSel_Type.__name__=_F
_WtWebGraphThermoBaroGraphicsSelectDisplaySensorSel_Object=MibScalar
wtWebGraphThermoBaroGraphicsSelectDisplaySensorSel=_WtWebGraphThermoBaroGraphicsSelectDisplaySensorSel_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,2,1),_WtWebGraphThermoBaroGraphicsSelectDisplaySensorSel_Type())
wtWebGraphThermoBaroGraphicsSelectDisplaySensorSel.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGraphicsSelectDisplaySensorSel.setStatus(_A)
class _WtWebGraphThermoBaroGraphicsSelectDisplayShowExtrem_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoBaroGraphicsSelectDisplayShowExtrem_Type.__name__=_F
_WtWebGraphThermoBaroGraphicsSelectDisplayShowExtrem_Object=MibScalar
wtWebGraphThermoBaroGraphicsSelectDisplayShowExtrem=_WtWebGraphThermoBaroGraphicsSelectDisplayShowExtrem_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,2,2),_WtWebGraphThermoBaroGraphicsSelectDisplayShowExtrem_Type())
wtWebGraphThermoBaroGraphicsSelectDisplayShowExtrem.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGraphicsSelectDisplayShowExtrem.setStatus(_A)
_WtWebGraphThermoBaroSensorColorTable_Object=MibTable
wtWebGraphThermoBaroSensorColorTable=_WtWebGraphThermoBaroSensorColorTable_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,2,3))
if mibBuilder.loadTexts:wtWebGraphThermoBaroSensorColorTable.setStatus(_A)
_WtWebGraphThermoBaroSensorColorEntry_Object=MibTableRow
wtWebGraphThermoBaroSensorColorEntry=_WtWebGraphThermoBaroSensorColorEntry_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,2,3,1))
wtWebGraphThermoBaroSensorColorEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:wtWebGraphThermoBaroSensorColorEntry.setStatus(_A)
class _WtWebGraphThermoBaroGraphicsSensorColor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_WtWebGraphThermoBaroGraphicsSensorColor_Type.__name__=_F
_WtWebGraphThermoBaroGraphicsSensorColor_Object=MibTableColumn
wtWebGraphThermoBaroGraphicsSensorColor=_WtWebGraphThermoBaroGraphicsSensorColor_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,2,3,1,1),_WtWebGraphThermoBaroGraphicsSensorColor_Type())
wtWebGraphThermoBaroGraphicsSensorColor.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGraphicsSensorColor.setStatus(_A)
_WtWebGraphThermoBaroGraphicsSelectScale_Type=OctetString
_WtWebGraphThermoBaroGraphicsSelectScale_Object=MibTableColumn
wtWebGraphThermoBaroGraphicsSelectScale=_WtWebGraphThermoBaroGraphicsSelectScale_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,2,3,1,2),_WtWebGraphThermoBaroGraphicsSelectScale_Type())
wtWebGraphThermoBaroGraphicsSelectScale.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGraphicsSelectScale.setStatus(_A)
_WtWebGraphThermoBaroGraphicsScale_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroGraphicsScale=_WtWebGraphThermoBaroGraphicsScale_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,1,6,3))
_WtWebGraphThermoBaroGraphicsScaleAutoScaleEnable_Type=OctetString
_WtWebGraphThermoBaroGraphicsScaleAutoScaleEnable_Object=MibScalar
wtWebGraphThermoBaroGraphicsScaleAutoScaleEnable=_WtWebGraphThermoBaroGraphicsScaleAutoScaleEnable_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,3,1),_WtWebGraphThermoBaroGraphicsScaleAutoScaleEnable_Type())
wtWebGraphThermoBaroGraphicsScaleAutoScaleEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGraphicsScaleAutoScaleEnable.setStatus(_A)
_WtWebGraphThermoBaroGraphicsScaleAutoFitEnable_Type=OctetString
_WtWebGraphThermoBaroGraphicsScaleAutoFitEnable_Object=MibScalar
wtWebGraphThermoBaroGraphicsScaleAutoFitEnable=_WtWebGraphThermoBaroGraphicsScaleAutoFitEnable_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,3,2),_WtWebGraphThermoBaroGraphicsScaleAutoFitEnable_Type())
wtWebGraphThermoBaroGraphicsScaleAutoFitEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGraphicsScaleAutoFitEnable.setStatus(_A)
_WtWebGraphThermoBaroGraphicsScale1Min_Type=Integer32
_WtWebGraphThermoBaroGraphicsScale1Min_Object=MibScalar
wtWebGraphThermoBaroGraphicsScale1Min=_WtWebGraphThermoBaroGraphicsScale1Min_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,3,3),_WtWebGraphThermoBaroGraphicsScale1Min_Type())
wtWebGraphThermoBaroGraphicsScale1Min.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGraphicsScale1Min.setStatus(_A)
_WtWebGraphThermoBaroGraphicsScale2Min_Type=Integer32
_WtWebGraphThermoBaroGraphicsScale2Min_Object=MibScalar
wtWebGraphThermoBaroGraphicsScale2Min=_WtWebGraphThermoBaroGraphicsScale2Min_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,3,4),_WtWebGraphThermoBaroGraphicsScale2Min_Type())
wtWebGraphThermoBaroGraphicsScale2Min.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGraphicsScale2Min.setStatus(_A)
_WtWebGraphThermoBaroGraphicsScale3Min_Type=Integer32
_WtWebGraphThermoBaroGraphicsScale3Min_Object=MibScalar
wtWebGraphThermoBaroGraphicsScale3Min=_WtWebGraphThermoBaroGraphicsScale3Min_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,3,5),_WtWebGraphThermoBaroGraphicsScale3Min_Type())
wtWebGraphThermoBaroGraphicsScale3Min.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGraphicsScale3Min.setStatus(_A)
_WtWebGraphThermoBaroGraphicsScale4Min_Type=Integer32
_WtWebGraphThermoBaroGraphicsScale4Min_Object=MibScalar
wtWebGraphThermoBaroGraphicsScale4Min=_WtWebGraphThermoBaroGraphicsScale4Min_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,3,6),_WtWebGraphThermoBaroGraphicsScale4Min_Type())
wtWebGraphThermoBaroGraphicsScale4Min.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGraphicsScale4Min.setStatus(_A)
_WtWebGraphThermoBaroGraphicsScale1Max_Type=Integer32
_WtWebGraphThermoBaroGraphicsScale1Max_Object=MibScalar
wtWebGraphThermoBaroGraphicsScale1Max=_WtWebGraphThermoBaroGraphicsScale1Max_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,3,7),_WtWebGraphThermoBaroGraphicsScale1Max_Type())
wtWebGraphThermoBaroGraphicsScale1Max.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGraphicsScale1Max.setStatus(_A)
_WtWebGraphThermoBaroGraphicsScale2Max_Type=Integer32
_WtWebGraphThermoBaroGraphicsScale2Max_Object=MibScalar
wtWebGraphThermoBaroGraphicsScale2Max=_WtWebGraphThermoBaroGraphicsScale2Max_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,3,8),_WtWebGraphThermoBaroGraphicsScale2Max_Type())
wtWebGraphThermoBaroGraphicsScale2Max.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGraphicsScale2Max.setStatus(_A)
_WtWebGraphThermoBaroGraphicsScale3Max_Type=Integer32
_WtWebGraphThermoBaroGraphicsScale3Max_Object=MibScalar
wtWebGraphThermoBaroGraphicsScale3Max=_WtWebGraphThermoBaroGraphicsScale3Max_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,3,9),_WtWebGraphThermoBaroGraphicsScale3Max_Type())
wtWebGraphThermoBaroGraphicsScale3Max.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGraphicsScale3Max.setStatus(_A)
_WtWebGraphThermoBaroGraphicsScale4Max_Type=Integer32
_WtWebGraphThermoBaroGraphicsScale4Max_Object=MibScalar
wtWebGraphThermoBaroGraphicsScale4Max=_WtWebGraphThermoBaroGraphicsScale4Max_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,3,10),_WtWebGraphThermoBaroGraphicsScale4Max_Type())
wtWebGraphThermoBaroGraphicsScale4Max.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGraphicsScale4Max.setStatus(_A)
_WtWebGraphThermoBaroGraphicsScale1Unit_Type=OctetString
_WtWebGraphThermoBaroGraphicsScale1Unit_Object=MibScalar
wtWebGraphThermoBaroGraphicsScale1Unit=_WtWebGraphThermoBaroGraphicsScale1Unit_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,3,11),_WtWebGraphThermoBaroGraphicsScale1Unit_Type())
wtWebGraphThermoBaroGraphicsScale1Unit.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGraphicsScale1Unit.setStatus(_A)
_WtWebGraphThermoBaroGraphicsScale2Unit_Type=OctetString
_WtWebGraphThermoBaroGraphicsScale2Unit_Object=MibScalar
wtWebGraphThermoBaroGraphicsScale2Unit=_WtWebGraphThermoBaroGraphicsScale2Unit_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,3,12),_WtWebGraphThermoBaroGraphicsScale2Unit_Type())
wtWebGraphThermoBaroGraphicsScale2Unit.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGraphicsScale2Unit.setStatus(_A)
_WtWebGraphThermoBaroGraphicsScale3Unit_Type=OctetString
_WtWebGraphThermoBaroGraphicsScale3Unit_Object=MibScalar
wtWebGraphThermoBaroGraphicsScale3Unit=_WtWebGraphThermoBaroGraphicsScale3Unit_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,3,13),_WtWebGraphThermoBaroGraphicsScale3Unit_Type())
wtWebGraphThermoBaroGraphicsScale3Unit.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGraphicsScale3Unit.setStatus(_A)
_WtWebGraphThermoBaroGraphicsScale4Unit_Type=OctetString
_WtWebGraphThermoBaroGraphicsScale4Unit_Object=MibScalar
wtWebGraphThermoBaroGraphicsScale4Unit=_WtWebGraphThermoBaroGraphicsScale4Unit_Object((1,3,6,1,4,1,5040,1,2,37,3,1,6,3,14),_WtWebGraphThermoBaroGraphicsScale4Unit_Type())
wtWebGraphThermoBaroGraphicsScale4Unit.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphThermoBaroGraphicsScale4Unit.setStatus(_A)
_WtWebGraphThermoBaroPorts_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroPorts=_WtWebGraphThermoBaroPorts_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,2))
_WtWebGraphThermoBaroPortTable_Object=MibTable
wtWebGraphThermoBaroPortTable=_WtWebGraphThermoBaroPortTable_Object((1,3,6,1,4,1,5040,1,2,37,3,2,1))
if mibBuilder.loadTexts:wtWebGraphThermoBaroPortTable.setStatus(_A)
_WtWebGraphThermoBaroPortEntry_Object=MibTableRow
wtWebGraphThermoBaroPortEntry=_WtWebGraphThermoBaroPortEntry_Object((1,3,6,1,4,1,5040,1,2,37,3,2,1,1))
wtWebGraphThermoBaroPortEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:wtWebGraphThermoBaroPortEntry.setStatus(_A)
_WtWebGraphThermoBaroPortName_Type=OctetString
_WtWebGraphThermoBaroPortName_Object=MibTableColumn
wtWebGraphThermoBaroPortName=_WtWebGraphThermoBaroPortName_Object((1,3,6,1,4,1,5040,1,2,37,3,2,1,1,1),_WtWebGraphThermoBaroPortName_Type())
wtWebGraphThermoBaroPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroPortName.setStatus(_A)
_WtWebGraphThermoBaroPortText_Type=OctetString
_WtWebGraphThermoBaroPortText_Object=MibTableColumn
wtWebGraphThermoBaroPortText=_WtWebGraphThermoBaroPortText_Object((1,3,6,1,4,1,5040,1,2,37,3,2,1,1,2),_WtWebGraphThermoBaroPortText_Type())
wtWebGraphThermoBaroPortText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroPortText.setStatus(_A)
_WtWebGraphThermoBaroPortOffset1_Type=OctetString
_WtWebGraphThermoBaroPortOffset1_Object=MibTableColumn
wtWebGraphThermoBaroPortOffset1=_WtWebGraphThermoBaroPortOffset1_Object((1,3,6,1,4,1,5040,1,2,37,3,2,1,1,3),_WtWebGraphThermoBaroPortOffset1_Type())
wtWebGraphThermoBaroPortOffset1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroPortOffset1.setStatus(_A)
_WtWebGraphThermoBaroPortTemperature1_Type=OctetString
_WtWebGraphThermoBaroPortTemperature1_Object=MibTableColumn
wtWebGraphThermoBaroPortTemperature1=_WtWebGraphThermoBaroPortTemperature1_Object((1,3,6,1,4,1,5040,1,2,37,3,2,1,1,4),_WtWebGraphThermoBaroPortTemperature1_Type())
wtWebGraphThermoBaroPortTemperature1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroPortTemperature1.setStatus(_A)
_WtWebGraphThermoBaroPortOffset2_Type=OctetString
_WtWebGraphThermoBaroPortOffset2_Object=MibTableColumn
wtWebGraphThermoBaroPortOffset2=_WtWebGraphThermoBaroPortOffset2_Object((1,3,6,1,4,1,5040,1,2,37,3,2,1,1,5),_WtWebGraphThermoBaroPortOffset2_Type())
wtWebGraphThermoBaroPortOffset2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroPortOffset2.setStatus(_A)
_WtWebGraphThermoBaroPortTemperature2_Type=OctetString
_WtWebGraphThermoBaroPortTemperature2_Object=MibTableColumn
wtWebGraphThermoBaroPortTemperature2=_WtWebGraphThermoBaroPortTemperature2_Object((1,3,6,1,4,1,5040,1,2,37,3,2,1,1,6),_WtWebGraphThermoBaroPortTemperature2_Type())
wtWebGraphThermoBaroPortTemperature2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroPortTemperature2.setStatus(_A)
_WtWebGraphThermoBaroPortComment_Type=OctetString
_WtWebGraphThermoBaroPortComment_Object=MibTableColumn
wtWebGraphThermoBaroPortComment=_WtWebGraphThermoBaroPortComment_Object((1,3,6,1,4,1,5040,1,2,37,3,2,1,1,7),_WtWebGraphThermoBaroPortComment_Type())
wtWebGraphThermoBaroPortComment.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroPortComment.setStatus(_A)
_WtWebGraphThermoBaroPortAltidude_Type=OctetString
_WtWebGraphThermoBaroPortAltidude_Object=MibScalar
wtWebGraphThermoBaroPortAltidude=_WtWebGraphThermoBaroPortAltidude_Object((1,3,6,1,4,1,5040,1,2,37,3,2,2),_WtWebGraphThermoBaroPortAltidude_Type())
wtWebGraphThermoBaroPortAltidude.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroPortAltidude.setStatus(_A)
_WtWebGraphThermoBaroManufact_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroManufact=_WtWebGraphThermoBaroManufact_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,3,3))
_WtWebGraphThermoBaroMfName_Type=OctetString
_WtWebGraphThermoBaroMfName_Object=MibScalar
wtWebGraphThermoBaroMfName=_WtWebGraphThermoBaroMfName_Object((1,3,6,1,4,1,5040,1,2,37,3,3,1),_WtWebGraphThermoBaroMfName_Type())
wtWebGraphThermoBaroMfName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroMfName.setStatus(_A)
_WtWebGraphThermoBaroMfAddr_Type=OctetString
_WtWebGraphThermoBaroMfAddr_Object=MibScalar
wtWebGraphThermoBaroMfAddr=_WtWebGraphThermoBaroMfAddr_Object((1,3,6,1,4,1,5040,1,2,37,3,3,2),_WtWebGraphThermoBaroMfAddr_Type())
wtWebGraphThermoBaroMfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroMfAddr.setStatus(_A)
_WtWebGraphThermoBaroMfHotline_Type=OctetString
_WtWebGraphThermoBaroMfHotline_Object=MibScalar
wtWebGraphThermoBaroMfHotline=_WtWebGraphThermoBaroMfHotline_Object((1,3,6,1,4,1,5040,1,2,37,3,3,3),_WtWebGraphThermoBaroMfHotline_Type())
wtWebGraphThermoBaroMfHotline.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroMfHotline.setStatus(_A)
_WtWebGraphThermoBaroMfInternet_Type=OctetString
_WtWebGraphThermoBaroMfInternet_Object=MibScalar
wtWebGraphThermoBaroMfInternet=_WtWebGraphThermoBaroMfInternet_Object((1,3,6,1,4,1,5040,1,2,37,3,3,4),_WtWebGraphThermoBaroMfInternet_Type())
wtWebGraphThermoBaroMfInternet.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroMfInternet.setStatus(_A)
_WtWebGraphThermoBaroMfDeviceTyp_Type=OctetString
_WtWebGraphThermoBaroMfDeviceTyp_Object=MibScalar
wtWebGraphThermoBaroMfDeviceTyp=_WtWebGraphThermoBaroMfDeviceTyp_Object((1,3,6,1,4,1,5040,1,2,37,3,3,5),_WtWebGraphThermoBaroMfDeviceTyp_Type())
wtWebGraphThermoBaroMfDeviceTyp.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroMfDeviceTyp.setStatus(_A)
_WtWebGraphThermoBaroMfOrderNo_Type=OctetString
_WtWebGraphThermoBaroMfOrderNo_Object=MibScalar
wtWebGraphThermoBaroMfOrderNo=_WtWebGraphThermoBaroMfOrderNo_Object((1,3,6,1,4,1,5040,1,2,37,3,3,6),_WtWebGraphThermoBaroMfOrderNo_Type())
wtWebGraphThermoBaroMfOrderNo.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroMfOrderNo.setStatus(_A)
_WtWebGraphThermoBaroDiag_ObjectIdentity=ObjectIdentity
wtWebGraphThermoBaroDiag=_WtWebGraphThermoBaroDiag_ObjectIdentity((1,3,6,1,4,1,5040,1,2,37,4))
_WtWebGraphThermoBaroDiagErrorCount_Type=Integer32
_WtWebGraphThermoBaroDiagErrorCount_Object=MibScalar
wtWebGraphThermoBaroDiagErrorCount=_WtWebGraphThermoBaroDiagErrorCount_Object((1,3,6,1,4,1,5040,1,2,37,4,1),_WtWebGraphThermoBaroDiagErrorCount_Type())
wtWebGraphThermoBaroDiagErrorCount.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphThermoBaroDiagErrorCount.setStatus(_A)
_WtWebGraphThermoBaroDiagBinaryError_Type=OctetString
_WtWebGraphThermoBaroDiagBinaryError_Object=MibScalar
wtWebGraphThermoBaroDiagBinaryError=_WtWebGraphThermoBaroDiagBinaryError_Object((1,3,6,1,4,1,5040,1,2,37,4,2),_WtWebGraphThermoBaroDiagBinaryError_Type())
wtWebGraphThermoBaroDiagBinaryError.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphThermoBaroDiagBinaryError.setStatus(_A)
_WtWebGraphThermoBaroDiagErrorIndex_Type=Integer32
_WtWebGraphThermoBaroDiagErrorIndex_Object=MibScalar
wtWebGraphThermoBaroDiagErrorIndex=_WtWebGraphThermoBaroDiagErrorIndex_Object((1,3,6,1,4,1,5040,1,2,37,4,3),_WtWebGraphThermoBaroDiagErrorIndex_Type())
wtWebGraphThermoBaroDiagErrorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoBaroDiagErrorIndex.setStatus(_A)
_WtWebGraphThermoBaroDiagErrorMessage_Type=OctetString
_WtWebGraphThermoBaroDiagErrorMessage_Object=MibScalar
wtWebGraphThermoBaroDiagErrorMessage=_WtWebGraphThermoBaroDiagErrorMessage_Object((1,3,6,1,4,1,5040,1,2,37,4,4),_WtWebGraphThermoBaroDiagErrorMessage_Type())
wtWebGraphThermoBaroDiagErrorMessage.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphThermoBaroDiagErrorMessage.setStatus(_A)
_WtWebGraphThermoBaroDiagErrorClear_Type=Integer32
_WtWebGraphThermoBaroDiagErrorClear_Object=MibScalar
wtWebGraphThermoBaroDiagErrorClear=_WtWebGraphThermoBaroDiagErrorClear_Object((1,3,6,1,4,1,5040,1,2,37,4,5),_WtWebGraphThermoBaroDiagErrorClear_Type())
wtWebGraphThermoBaroDiagErrorClear.setMaxAccess('write-only')
if mibBuilder.loadTexts:wtWebGraphThermoBaroDiagErrorClear.setStatus(_A)
wtWebGraphThermoBaroAlert1=NotificationType((1,3,6,1,4,1,5040,1,2,37,0,31))
wtWebGraphThermoBaroAlert1.setObjects((_C,_G))
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlert1.setStatus('')
wtWebGraphThermoBaroAlert2=NotificationType((1,3,6,1,4,1,5040,1,2,37,0,32))
wtWebGraphThermoBaroAlert2.setObjects((_C,_G))
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlert2.setStatus('')
wtWebGraphThermoBaroAlert3=NotificationType((1,3,6,1,4,1,5040,1,2,37,0,33))
wtWebGraphThermoBaroAlert3.setObjects((_C,_G))
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlert3.setStatus('')
wtWebGraphThermoBaroAlert4=NotificationType((1,3,6,1,4,1,5040,1,2,37,0,34))
wtWebGraphThermoBaroAlert4.setObjects((_C,_G))
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlert4.setStatus('')
wtWebGraphThermoBaroAlert5=NotificationType((1,3,6,1,4,1,5040,1,2,37,0,35))
wtWebGraphThermoBaroAlert5.setObjects((_C,_G))
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlert5.setStatus('')
wtWebGraphThermoBaroAlert6=NotificationType((1,3,6,1,4,1,5040,1,2,37,0,36))
wtWebGraphThermoBaroAlert6.setObjects((_C,_G))
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlert6.setStatus('')
wtWebGraphThermoBaroAlert7=NotificationType((1,3,6,1,4,1,5040,1,2,37,0,37))
wtWebGraphThermoBaroAlert7.setObjects((_C,_G))
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlert7.setStatus('')
wtWebGraphThermoBaroAlert8=NotificationType((1,3,6,1,4,1,5040,1,2,37,0,38))
wtWebGraphThermoBaroAlert8.setObjects((_C,_G))
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlert8.setStatus('')
wtWebGraphThermoBaroAlert9=NotificationType((1,3,6,1,4,1,5040,1,2,37,0,91))
wtWebGraphThermoBaroAlert9.setObjects((_C,_H))
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlert9.setStatus('')
wtWebGraphThermoBaroAlert10=NotificationType((1,3,6,1,4,1,5040,1,2,37,0,92))
wtWebGraphThermoBaroAlert10.setObjects((_C,_H))
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlert10.setStatus('')
wtWebGraphThermoBaroAlert11=NotificationType((1,3,6,1,4,1,5040,1,2,37,0,93))
wtWebGraphThermoBaroAlert11.setObjects((_C,_H))
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlert11.setStatus('')
wtWebGraphThermoBaroAlert12=NotificationType((1,3,6,1,4,1,5040,1,2,37,0,94))
wtWebGraphThermoBaroAlert12.setObjects((_C,_H))
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlert12.setStatus('')
wtWebGraphThermoBaroAlert13=NotificationType((1,3,6,1,4,1,5040,1,2,37,0,95))
wtWebGraphThermoBaroAlert13.setObjects((_C,_H))
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlert13.setStatus('')
wtWebGraphThermoBaroAlert14=NotificationType((1,3,6,1,4,1,5040,1,2,37,0,96))
wtWebGraphThermoBaroAlert14.setObjects((_C,_H))
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlert14.setStatus('')
wtWebGraphThermoBaroAlert15=NotificationType((1,3,6,1,4,1,5040,1,2,37,0,97))
wtWebGraphThermoBaroAlert15.setObjects((_C,_H))
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlert15.setStatus('')
wtWebGraphThermoBaroAlert16=NotificationType((1,3,6,1,4,1,5040,1,2,37,0,98))
wtWebGraphThermoBaroAlert16.setObjects((_C,_H))
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlert16.setStatus('')
wtWebGraphThermoBaroAlertDiag=NotificationType((1,3,6,1,4,1,5040,1,2,37,0,110))
wtWebGraphThermoBaroAlertDiag.setObjects(*((_C,_L),(_C,_M)))
if mibBuilder.loadTexts:wtWebGraphThermoBaroAlertDiag.setStatus('')
mibBuilder.exportSymbols(_C,**{'wut':wut,'wtComServer':wtComServer,'wtWebio':wtWebio,'wtWebGraphThermoBaro':wtWebGraphThermoBaro,'wtWebGraphThermoBaroAlert1':wtWebGraphThermoBaroAlert1,'wtWebGraphThermoBaroAlert2':wtWebGraphThermoBaroAlert2,'wtWebGraphThermoBaroAlert3':wtWebGraphThermoBaroAlert3,'wtWebGraphThermoBaroAlert4':wtWebGraphThermoBaroAlert4,'wtWebGraphThermoBaroAlert5':wtWebGraphThermoBaroAlert5,'wtWebGraphThermoBaroAlert6':wtWebGraphThermoBaroAlert6,'wtWebGraphThermoBaroAlert7':wtWebGraphThermoBaroAlert7,'wtWebGraphThermoBaroAlert8':wtWebGraphThermoBaroAlert8,'wtWebGraphThermoBaroAlert9':wtWebGraphThermoBaroAlert9,'wtWebGraphThermoBaroAlert10':wtWebGraphThermoBaroAlert10,'wtWebGraphThermoBaroAlert11':wtWebGraphThermoBaroAlert11,'wtWebGraphThermoBaroAlert12':wtWebGraphThermoBaroAlert12,'wtWebGraphThermoBaroAlert13':wtWebGraphThermoBaroAlert13,'wtWebGraphThermoBaroAlert14':wtWebGraphThermoBaroAlert14,'wtWebGraphThermoBaroAlert15':wtWebGraphThermoBaroAlert15,'wtWebGraphThermoBaroAlert16':wtWebGraphThermoBaroAlert16,'wtWebGraphThermoBaroAlertDiag':wtWebGraphThermoBaroAlertDiag,'wtWebGraphThermoBaroTemp':wtWebGraphThermoBaroTemp,'wtWebGraphThermoBaroSensors':wtWebGraphThermoBaroSensors,'wtWebGraphThermoBaroSensorTable':wtWebGraphThermoBaroSensorTable,'wtWebGraphThermoBaroSensorEntry':wtWebGraphThermoBaroSensorEntry,_I:wtWebGraphThermoBaroSensorNo,'wtWebGraphThermoBaroTempValueTable':wtWebGraphThermoBaroTempValueTable,'wtWebGraphThermoBaroTempValueEntry':wtWebGraphThermoBaroTempValueEntry,'wtWebGraphThermoBaroTempValue':wtWebGraphThermoBaroTempValue,'wtWebGraphThermoBaroBinaryTempValueTable':wtWebGraphThermoBaroBinaryTempValueTable,'wtWebGraphThermoBaroBinaryTempValueEntry':wtWebGraphThermoBaroBinaryTempValueEntry,'wtWebGraphThermoBaroBinaryTempValue':wtWebGraphThermoBaroBinaryTempValue,'wtWebGraphThermoBaroTempValuePktTable':wtWebGraphThermoBaroTempValuePktTable,'wtWebGraphThermoBaroTempValuePktEntry':wtWebGraphThermoBaroTempValuePktEntry,'wtWebGraphThermoBaroTempValuePkt':wtWebGraphThermoBaroTempValuePkt,'wtWebGraphThermoBaroSessCntrl':wtWebGraphThermoBaroSessCntrl,'wtWebGraphThermoBaroSessCntrlPassword':wtWebGraphThermoBaroSessCntrlPassword,'wtWebGraphThermoBaroSessCntrlConfigMode':wtWebGraphThermoBaroSessCntrlConfigMode,'wtWebGraphThermoBaroSessCntrlLogout':wtWebGraphThermoBaroSessCntrlLogout,'wtWebGraphThermoBaroSessCntrlAdminPassword':wtWebGraphThermoBaroSessCntrlAdminPassword,'wtWebGraphThermoBaroSessCntrlConfigPassword':wtWebGraphThermoBaroSessCntrlConfigPassword,'wtWebGraphThermoBaroConfig':wtWebGraphThermoBaroConfig,'wtWebGraphThermoBaroDevice':wtWebGraphThermoBaroDevice,'wtWebGraphThermoBaroText':wtWebGraphThermoBaroText,'wtWebGraphThermoBaroDeviceName':wtWebGraphThermoBaroDeviceName,'wtWebGraphThermoBaroDeviceText':wtWebGraphThermoBaroDeviceText,'wtWebGraphThermoBaroDeviceLocation':wtWebGraphThermoBaroDeviceLocation,'wtWebGraphThermoBaroDeviceContact':wtWebGraphThermoBaroDeviceContact,'wtWebGraphThermoBaroTimeDate':wtWebGraphThermoBaroTimeDate,'wtWebGraphThermoBaroTimeZone':wtWebGraphThermoBaroTimeZone,'wtWebGraphThermoBaroTzOffsetHrs':wtWebGraphThermoBaroTzOffsetHrs,'wtWebGraphThermoBaroTzOffsetMin':wtWebGraphThermoBaroTzOffsetMin,'wtWebGraphThermoBaroTzEnable':wtWebGraphThermoBaroTzEnable,'wtWebGraphThermoBaroStTzOffsetHrs':wtWebGraphThermoBaroStTzOffsetHrs,'wtWebGraphThermoBaroStTzOffsetMin':wtWebGraphThermoBaroStTzOffsetMin,'wtWebGraphThermoBaroStTzEnable':wtWebGraphThermoBaroStTzEnable,'wtWebGraphThermoBaroStTzStartMonth':wtWebGraphThermoBaroStTzStartMonth,'wtWebGraphThermoBaroStTzStartMode':wtWebGraphThermoBaroStTzStartMode,'wtWebGraphThermoBaroStTzStartWday':wtWebGraphThermoBaroStTzStartWday,'wtWebGraphThermoBaroStTzStartHrs':wtWebGraphThermoBaroStTzStartHrs,'wtWebGraphThermoBaroStTzStartMin':wtWebGraphThermoBaroStTzStartMin,'wtWebGraphThermoBaroStTzStopMonth':wtWebGraphThermoBaroStTzStopMonth,'wtWebGraphThermoBaroStTzStopMode':wtWebGraphThermoBaroStTzStopMode,'wtWebGraphThermoBaroStTzStopWday':wtWebGraphThermoBaroStTzStopWday,'wtWebGraphThermoBaroStTzStopHrs':wtWebGraphThermoBaroStTzStopHrs,'wtWebGraphThermoBaroStTzStopMin':wtWebGraphThermoBaroStTzStopMin,'wtWebGraphThermoBaroTimeServer':wtWebGraphThermoBaroTimeServer,'wtWebGraphThermoBaroTimeServer1':wtWebGraphThermoBaroTimeServer1,'wtWebGraphThermoBaroTimeServer2':wtWebGraphThermoBaroTimeServer2,'wtWebGraphThermoBaroTsEnable':wtWebGraphThermoBaroTsEnable,'wtWebGraphThermoBaroTsSyncTime':wtWebGraphThermoBaroTsSyncTime,'wtWebGraphThermoBaroDeviceClock':wtWebGraphThermoBaroDeviceClock,'wtWebGraphThermoBaroClockHrs':wtWebGraphThermoBaroClockHrs,'wtWebGraphThermoBaroClockMin':wtWebGraphThermoBaroClockMin,'wtWebGraphThermoBaroClockDay':wtWebGraphThermoBaroClockDay,'wtWebGraphThermoBaroClockMonth':wtWebGraphThermoBaroClockMonth,'wtWebGraphThermoBaroClockYear':wtWebGraphThermoBaroClockYear,'wtWebGraphThermoBaroBasic':wtWebGraphThermoBaroBasic,'wtWebGraphThermoBaroNetwork':wtWebGraphThermoBaroNetwork,'wtWebGraphThermoBaroIpAddress':wtWebGraphThermoBaroIpAddress,'wtWebGraphThermoBaroSubnetMask':wtWebGraphThermoBaroSubnetMask,'wtWebGraphThermoBaroGateway':wtWebGraphThermoBaroGateway,'wtWebGraphThermoBaroDnsServer1':wtWebGraphThermoBaroDnsServer1,'wtWebGraphThermoBaroDnsServer2':wtWebGraphThermoBaroDnsServer2,'wtWebGraphThermoBaroAddConfig':wtWebGraphThermoBaroAddConfig,'wtWebGraphThermoBaroHTTP':wtWebGraphThermoBaroHTTP,'wtWebGraphThermoBaroStartup':wtWebGraphThermoBaroStartup,'wtWebGraphThermoBaroGetHeaderEnable':wtWebGraphThermoBaroGetHeaderEnable,'wtWebGraphThermoBaroHttpPort':wtWebGraphThermoBaroHttpPort,'wtWebGraphThermoBaroMail':wtWebGraphThermoBaroMail,'wtWebGraphThermoBaroMailAdName':wtWebGraphThermoBaroMailAdName,'wtWebGraphThermoBaroMailReply':wtWebGraphThermoBaroMailReply,'wtWebGraphThermoBaroMailServer':wtWebGraphThermoBaroMailServer,'wtWebioAn1MailEnable':wtWebioAn1MailEnable,'wtWebGraphThermoBaroMailAuthentication':wtWebGraphThermoBaroMailAuthentication,'wtWebGraphThermoBaroMailAuthUser':wtWebGraphThermoBaroMailAuthUser,'wtWebGraphThermoBaroMailAuthPassword':wtWebGraphThermoBaroMailAuthPassword,'wtWebGraphThermoBaroMailPop3Server':wtWebGraphThermoBaroMailPop3Server,'wtWebGraphThermoBaroSNMP':wtWebGraphThermoBaroSNMP,'wtWebGraphThermoBaroSnmpCommunityStringRead':wtWebGraphThermoBaroSnmpCommunityStringRead,'wtWebGraphThermoBaroSnmpCommunityStringReadWrite':wtWebGraphThermoBaroSnmpCommunityStringReadWrite,'wtWebGraphThermoBaroSystemTrapManagerIP':wtWebGraphThermoBaroSystemTrapManagerIP,'wtWebGraphThermoBaroSystemTrapEnable':wtWebGraphThermoBaroSystemTrapEnable,'wtWebGraphThermoBaroSnmpEnable':wtWebGraphThermoBaroSnmpEnable,'wtWebGraphThermoBaroSnmpCommunityStringTrap':wtWebGraphThermoBaroSnmpCommunityStringTrap,'wtWebGraphThermoBaroUDP':wtWebGraphThermoBaroUDP,'wtWebGraphThermoBaroUdpPort':wtWebGraphThermoBaroUdpPort,'wtWebGraphThermoBaroUdpEnable':wtWebGraphThermoBaroUdpEnable,'wtWebGraphThermoBaroSyslog':wtWebGraphThermoBaroSyslog,'wtWebGraphThermoBaroSyslogServerIP':wtWebGraphThermoBaroSyslogServerIP,'wtWebGraphThermoBaroSyslogServerPort':wtWebGraphThermoBaroSyslogServerPort,'wtWebGraphThermoBaroSyslogSystemMessagesEnable':wtWebGraphThermoBaroSyslogSystemMessagesEnable,'wtWebGraphThermoBaroSyslogEnable':wtWebGraphThermoBaroSyslogEnable,'wtWebGraphThermoBaroFTP':wtWebGraphThermoBaroFTP,'wtWebGraphThermoBaroFTPServerIP':wtWebGraphThermoBaroFTPServerIP,'wtWebGraphThermoBaroFTPServerControlPort':wtWebGraphThermoBaroFTPServerControlPort,'wtWebGraphThermoBaroFTPUserName':wtWebGraphThermoBaroFTPUserName,'wtWebGraphThermoBaroFTPPassword':wtWebGraphThermoBaroFTPPassword,'wtWebGraphThermoBaroFTPAccount':wtWebGraphThermoBaroFTPAccount,'wtWebGraphThermoBaroFTPOption':wtWebGraphThermoBaroFTPOption,'wtWebGraphThermoBaroFTPEnable':wtWebGraphThermoBaroFTPEnable,'wtWebGraphThermoBaroRSS':wtWebGraphThermoBaroRSS,'wtWebGraphThermoBaroRSSChannelTitle':wtWebGraphThermoBaroRSSChannelTitle,'wtWebGraphThermoBaroRSSChannelLink':wtWebGraphThermoBaroRSSChannelLink,'wtWebGraphThermoBaroRSSChannelDescription':wtWebGraphThermoBaroRSSChannelDescription,'wtWebGraphThermoBaroRSSChannelImage':wtWebGraphThermoBaroRSSChannelImage,'wtWebGraphThermoBaroRSSChannelImageTitle':wtWebGraphThermoBaroRSSChannelImageTitle,'wtWebGraphThermoBaroRSSChannelImageLink':wtWebGraphThermoBaroRSSChannelImageLink,'wtWebGraphThermoBaroRSSChannelItemTitle':wtWebGraphThermoBaroRSSChannelItemTitle,'wtWebGraphThermoBaroRSSChannelItemLink':wtWebGraphThermoBaroRSSChannelItemLink,'wtWebGraphThermoBaroRSSChannelItemDescription':wtWebGraphThermoBaroRSSChannelItemDescription,'wtWebGraphThermoBaroRSSChannelItemQuantity':wtWebGraphThermoBaroRSSChannelItemQuantity,'wtWebGraphThermoBaroLanguage':wtWebGraphThermoBaroLanguage,'wtWebGraphThermoBaroLanguageSelect':wtWebGraphThermoBaroLanguageSelect,'wtWebGraphThermoBaroMQTT':wtWebGraphThermoBaroMQTT,'wtWebGraphThermoBaroMQTTEnable':wtWebGraphThermoBaroMQTTEnable,'wtWebGraphThermoBaroMQTTBrockerIP':wtWebGraphThermoBaroMQTTBrockerIP,'wtWebGraphThermoBaroMQTTUserName':wtWebGraphThermoBaroMQTTUserName,'wtWebGraphThermoBaroMQTTPassword':wtWebGraphThermoBaroMQTTPassword,'wtWebGraphThermoBaroMQTTLocalPort':wtWebGraphThermoBaroMQTTLocalPort,'wtWebGraphThermoBaroMQTTBrokerServerPort':wtWebGraphThermoBaroMQTTBrokerServerPort,'wtWebGraphThermoBaroMQTTInterval':wtWebGraphThermoBaroMQTTInterval,'wtWebGraphThermoBaroREST':wtWebGraphThermoBaroREST,'wtWebGraphThermoBaroRESTEnable':wtWebGraphThermoBaroRESTEnable,'wtWebGraphThermoBaroRESTDigestAuthEnable':wtWebGraphThermoBaroRESTDigestAuthEnable,'wtWebGraphThermoBaroDatalogger':wtWebGraphThermoBaroDatalogger,'wtWebGraphThermoBaroLoggerTimebase':wtWebGraphThermoBaroLoggerTimebase,'wtWebGraphThermoBaroLoggerSensorSel':wtWebGraphThermoBaroLoggerSensorSel,'wtWebGraphThermoBaroAlarm':wtWebGraphThermoBaroAlarm,'wtWebGraphThermoBaroAlarmCount':wtWebGraphThermoBaroAlarmCount,'wtWebGraphThermoBaroAlarmIfTable':wtWebGraphThermoBaroAlarmIfTable,'wtWebGraphThermoBaroAlarmIfEntry':wtWebGraphThermoBaroAlarmIfEntry,_J:wtWebGraphThermoBaroAlarmNo,'wtWebGraphThermoBaroAlarmTable':wtWebGraphThermoBaroAlarmTable,'wtWebGraphThermoBaroAlarmEntry':wtWebGraphThermoBaroAlarmEntry,'wtWebGraphThermoBaroAlarmTrigger':wtWebGraphThermoBaroAlarmTrigger,'wtWebGraphThermoBaroAlarmMin':wtWebGraphThermoBaroAlarmMin,'wtWebGraphThermoBaroAlarmMax':wtWebGraphThermoBaroAlarmMax,'wtWebGraphThermoBaroAlarmHysteresis':wtWebGraphThermoBaroAlarmHysteresis,'wtWebGraphThermoBaroAlarmDelay':wtWebGraphThermoBaroAlarmDelay,'wtWebGraphThermoBaroAlarmInterval':wtWebGraphThermoBaroAlarmInterval,'wtWebGraphThermoBaroAlarmEnable':wtWebGraphThermoBaroAlarmEnable,'wtWebGraphThermoBaroAlarmEMailAddr':wtWebGraphThermoBaroAlarmEMailAddr,'wtWebGraphThermoBaroAlarmMailSubject':wtWebGraphThermoBaroAlarmMailSubject,'wtWebGraphThermoBaroAlarmMailText':wtWebGraphThermoBaroAlarmMailText,'wtWebGraphThermoBaroAlarmManagerIP':wtWebGraphThermoBaroAlarmManagerIP,_G:wtWebGraphThermoBaroAlarmTrapText,'wtWebGraphThermoBaroAlarmMailOptions':wtWebGraphThermoBaroAlarmMailOptions,'wtWebGraphThermoBaroAlarmTcpIpAddr':wtWebGraphThermoBaroAlarmTcpIpAddr,'wtWebGraphThermoBaroAlarmTcpPort':wtWebGraphThermoBaroAlarmTcpPort,'wtWebGraphThermoBaroAlarmTcpText':wtWebGraphThermoBaroAlarmTcpText,'wtWebGraphThermoBaroAlarmClearMailSubject':wtWebGraphThermoBaroAlarmClearMailSubject,'wtWebGraphThermoBaroAlarmClearMailText':wtWebGraphThermoBaroAlarmClearMailText,_H:wtWebGraphThermoBaroAlarmClearTrapText,'wtWebGraphThermoBaroAlarmClearTcpText':wtWebGraphThermoBaroAlarmClearTcpText,'wtWebGraphThermoBaroAlarmDeltaTemp':wtWebGraphThermoBaroAlarmDeltaTemp,'wtWebGraphThermoBaroAlarmRHMin':wtWebGraphThermoBaroAlarmRHMin,'wtWebGraphThermoBaroAlarmRHMax':wtWebGraphThermoBaroAlarmRHMax,'wtWebGraphThermoBaroAlarmRHHysteresis':wtWebGraphThermoBaroAlarmRHHysteresis,'wtWebGraphThermoBaroAlarmAHMin':wtWebGraphThermoBaroAlarmAHMin,'wtWebGraphThermoBaroAlarmAHMax':wtWebGraphThermoBaroAlarmAHMax,'wtWebGraphThermoBaroAlarmSyslogIpAddr':wtWebGraphThermoBaroAlarmSyslogIpAddr,'wtWebGraphThermoBaroAlarmSyslogPort':wtWebGraphThermoBaroAlarmSyslogPort,'wtWebGraphThermoBaroAlarmSyslogText':wtWebGraphThermoBaroAlarmSyslogText,'wtWebGraphThermoBaroAlarmSyslogClearText':wtWebGraphThermoBaroAlarmSyslogClearText,'wtWebGraphThermoBaroAlarmFtpDataPort':wtWebGraphThermoBaroAlarmFtpDataPort,'wtWebGraphThermoBaroAlarmFtpFileName':wtWebGraphThermoBaroAlarmFtpFileName,'wtWebGraphThermoBaroAlarmFtpText':wtWebGraphThermoBaroAlarmFtpText,'wtWebGraphThermoBaroAlarmFtpClearText':wtWebGraphThermoBaroAlarmFtpClearText,'wtWebGraphThermoBaroAlarmFtpOption':wtWebGraphThermoBaroAlarmFtpOption,'wtWebGraphThermoBaroAlarmTimerCron':wtWebGraphThermoBaroAlarmTimerCron,'wtWebGraphThermoBaroAlarmName':wtWebGraphThermoBaroAlarmName,'wtWebGraphThermoBaroAlarmActive':wtWebGraphThermoBaroAlarmActive,'wtWebGraphThermoBaroAlarmHttpReqAuthEnable':wtWebGraphThermoBaroAlarmHttpReqAuthEnable,'wtWebGraphThermoBaroAlarmHttpReqAuthUser':wtWebGraphThermoBaroAlarmHttpReqAuthUser,'wtWebGraphThermoBaroAlarmHttpReqAuthPassword':wtWebGraphThermoBaroAlarmHttpReqAuthPassword,'wtWebGraphThermoBaroAlarmHttpReqSetUrl':wtWebGraphThermoBaroAlarmHttpReqSetUrl,'wtWebGraphThermoBaroAlarmHttpReqClearUrl':wtWebGraphThermoBaroAlarmHttpReqClearUrl,'wtWebGraphThermoBaroAlarmHttpReqServerPort':wtWebGraphThermoBaroAlarmHttpReqServerPort,'wtWebGraphThermoBaroAlarmMqttTopicPath':wtWebGraphThermoBaroAlarmMqttTopicPath,'wtWebGraphThermoBaroAlarmMqttTopicSetTopic':wtWebGraphThermoBaroAlarmMqttTopicSetTopic,'wtWebGraphThermoBaroAlarmMqttTopicClear':wtWebGraphThermoBaroAlarmMqttTopicClear,'wtWebGraphThermoBaroAlarmSensorLostSelection':wtWebGraphThermoBaroAlarmSensorLostSelection,'wtWebGraphThermoBaroAlarmLimitWindow':wtWebGraphThermoBaroAlarmLimitWindow,'wtWebGraphThermoBaroGraphics':wtWebGraphThermoBaroGraphics,'wtWebGraphThermoBaroGraphicsBase':wtWebGraphThermoBaroGraphicsBase,'wtWebGraphThermoBaroGraphicsBaseEnable':wtWebGraphThermoBaroGraphicsBaseEnable,'wtWebGraphThermoBaroGraphicsBaseWidth':wtWebGraphThermoBaroGraphicsBaseWidth,'wtWebGraphThermoBaroGraphicsBaseHeight':wtWebGraphThermoBaroGraphicsBaseHeight,'wtWebGraphThermoBaroGraphicsBaseFrameColor':wtWebGraphThermoBaroGraphicsBaseFrameColor,'wtWebGraphThermoBaroGraphicsBaseBackgroundColor':wtWebGraphThermoBaroGraphicsBaseBackgroundColor,'wtWebGraphThermoBaroGraphicsBasePollingrate':wtWebGraphThermoBaroGraphicsBasePollingrate,'wtWebGraphThermoBaroGraphicsSelect':wtWebGraphThermoBaroGraphicsSelect,'wtWebGraphThermoBaroGraphicsSelectDisplaySensorSel':wtWebGraphThermoBaroGraphicsSelectDisplaySensorSel,'wtWebGraphThermoBaroGraphicsSelectDisplayShowExtrem':wtWebGraphThermoBaroGraphicsSelectDisplayShowExtrem,'wtWebGraphThermoBaroSensorColorTable':wtWebGraphThermoBaroSensorColorTable,'wtWebGraphThermoBaroSensorColorEntry':wtWebGraphThermoBaroSensorColorEntry,'wtWebGraphThermoBaroGraphicsSensorColor':wtWebGraphThermoBaroGraphicsSensorColor,'wtWebGraphThermoBaroGraphicsSelectScale':wtWebGraphThermoBaroGraphicsSelectScale,'wtWebGraphThermoBaroGraphicsScale':wtWebGraphThermoBaroGraphicsScale,'wtWebGraphThermoBaroGraphicsScaleAutoScaleEnable':wtWebGraphThermoBaroGraphicsScaleAutoScaleEnable,'wtWebGraphThermoBaroGraphicsScaleAutoFitEnable':wtWebGraphThermoBaroGraphicsScaleAutoFitEnable,'wtWebGraphThermoBaroGraphicsScale1Min':wtWebGraphThermoBaroGraphicsScale1Min,'wtWebGraphThermoBaroGraphicsScale2Min':wtWebGraphThermoBaroGraphicsScale2Min,'wtWebGraphThermoBaroGraphicsScale3Min':wtWebGraphThermoBaroGraphicsScale3Min,'wtWebGraphThermoBaroGraphicsScale4Min':wtWebGraphThermoBaroGraphicsScale4Min,'wtWebGraphThermoBaroGraphicsScale1Max':wtWebGraphThermoBaroGraphicsScale1Max,'wtWebGraphThermoBaroGraphicsScale2Max':wtWebGraphThermoBaroGraphicsScale2Max,'wtWebGraphThermoBaroGraphicsScale3Max':wtWebGraphThermoBaroGraphicsScale3Max,'wtWebGraphThermoBaroGraphicsScale4Max':wtWebGraphThermoBaroGraphicsScale4Max,'wtWebGraphThermoBaroGraphicsScale1Unit':wtWebGraphThermoBaroGraphicsScale1Unit,'wtWebGraphThermoBaroGraphicsScale2Unit':wtWebGraphThermoBaroGraphicsScale2Unit,'wtWebGraphThermoBaroGraphicsScale3Unit':wtWebGraphThermoBaroGraphicsScale3Unit,'wtWebGraphThermoBaroGraphicsScale4Unit':wtWebGraphThermoBaroGraphicsScale4Unit,'wtWebGraphThermoBaroPorts':wtWebGraphThermoBaroPorts,'wtWebGraphThermoBaroPortTable':wtWebGraphThermoBaroPortTable,'wtWebGraphThermoBaroPortEntry':wtWebGraphThermoBaroPortEntry,'wtWebGraphThermoBaroPortName':wtWebGraphThermoBaroPortName,'wtWebGraphThermoBaroPortText':wtWebGraphThermoBaroPortText,'wtWebGraphThermoBaroPortOffset1':wtWebGraphThermoBaroPortOffset1,'wtWebGraphThermoBaroPortTemperature1':wtWebGraphThermoBaroPortTemperature1,'wtWebGraphThermoBaroPortOffset2':wtWebGraphThermoBaroPortOffset2,'wtWebGraphThermoBaroPortTemperature2':wtWebGraphThermoBaroPortTemperature2,'wtWebGraphThermoBaroPortComment':wtWebGraphThermoBaroPortComment,'wtWebGraphThermoBaroPortAltidude':wtWebGraphThermoBaroPortAltidude,'wtWebGraphThermoBaroManufact':wtWebGraphThermoBaroManufact,'wtWebGraphThermoBaroMfName':wtWebGraphThermoBaroMfName,'wtWebGraphThermoBaroMfAddr':wtWebGraphThermoBaroMfAddr,'wtWebGraphThermoBaroMfHotline':wtWebGraphThermoBaroMfHotline,'wtWebGraphThermoBaroMfInternet':wtWebGraphThermoBaroMfInternet,'wtWebGraphThermoBaroMfDeviceTyp':wtWebGraphThermoBaroMfDeviceTyp,'wtWebGraphThermoBaroMfOrderNo':wtWebGraphThermoBaroMfOrderNo,'wtWebGraphThermoBaroDiag':wtWebGraphThermoBaroDiag,'wtWebGraphThermoBaroDiagErrorCount':wtWebGraphThermoBaroDiagErrorCount,'wtWebGraphThermoBaroDiagBinaryError':wtWebGraphThermoBaroDiagBinaryError,_L:wtWebGraphThermoBaroDiagErrorIndex,_M:wtWebGraphThermoBaroDiagErrorMessage,'wtWebGraphThermoBaroDiagErrorClear':wtWebGraphThermoBaroDiagErrorClear})