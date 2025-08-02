_M='wtWebGraphThermoHygroDiagErrorMessage'
_L='wtWebGraphThermoHygroDiagErrorIndex'
_K='NotificationType'
_J='wtWebGraphThermoHygroAlarmNo'
_I='wtWebGraphThermoHygroSensorNo'
_H='wtWebGraphThermoHygroAlarmClearTrapText'
_G='wtWebGraphThermoHygroAlarmTrapText'
_F='read-only'
_E='Integer32'
_D='OctetString'
_C='WebGraph-Thermo-Hygrometer-US-MIB'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier',_K,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_K,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Wut_ObjectIdentity=ObjectIdentity
wut=_Wut_ObjectIdentity((1,3,6,1,4,1,5040))
_WtComServer_ObjectIdentity=ObjectIdentity
wtComServer=_WtComServer_ObjectIdentity((1,3,6,1,4,1,5040,1))
_WtWebio_ObjectIdentity=ObjectIdentity
wtWebio=_WtWebio_ObjectIdentity((1,3,6,1,4,1,5040,1,2))
_WtWebGraphThermoHygro_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygro=_WtWebGraphThermoHygro_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42))
_WtWebGraphThermoHygroTemp_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroTemp=_WtWebGraphThermoHygroTemp_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,1))
class _WtWebGraphThermoHygroSensors_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_WtWebGraphThermoHygroSensors_Type.__name__=_E
_WtWebGraphThermoHygroSensors_Object=MibScalar
wtWebGraphThermoHygroSensors=_WtWebGraphThermoHygroSensors_Object((1,3,6,1,4,1,5040,1,2,42,1,1),_WtWebGraphThermoHygroSensors_Type())
wtWebGraphThermoHygroSensors.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphThermoHygroSensors.setStatus(_A)
_WtWebGraphThermoHygroSensorTable_Object=MibTable
wtWebGraphThermoHygroSensorTable=_WtWebGraphThermoHygroSensorTable_Object((1,3,6,1,4,1,5040,1,2,42,1,2))
if mibBuilder.loadTexts:wtWebGraphThermoHygroSensorTable.setStatus(_A)
_WtWebGraphThermoHygroSensorEntry_Object=MibTableRow
wtWebGraphThermoHygroSensorEntry=_WtWebGraphThermoHygroSensorEntry_Object((1,3,6,1,4,1,5040,1,2,42,1,2,1))
wtWebGraphThermoHygroSensorEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:wtWebGraphThermoHygroSensorEntry.setStatus(_A)
class _WtWebGraphThermoHygroSensorNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_WtWebGraphThermoHygroSensorNo_Type.__name__=_E
_WtWebGraphThermoHygroSensorNo_Object=MibTableColumn
wtWebGraphThermoHygroSensorNo=_WtWebGraphThermoHygroSensorNo_Object((1,3,6,1,4,1,5040,1,2,42,1,2,1,1),_WtWebGraphThermoHygroSensorNo_Type())
wtWebGraphThermoHygroSensorNo.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphThermoHygroSensorNo.setStatus(_A)
_WtWebGraphThermoHygroTempValueTable_Object=MibTable
wtWebGraphThermoHygroTempValueTable=_WtWebGraphThermoHygroTempValueTable_Object((1,3,6,1,4,1,5040,1,2,42,1,3))
if mibBuilder.loadTexts:wtWebGraphThermoHygroTempValueTable.setStatus(_A)
_WtWebGraphThermoHygroTempValueEntry_Object=MibTableRow
wtWebGraphThermoHygroTempValueEntry=_WtWebGraphThermoHygroTempValueEntry_Object((1,3,6,1,4,1,5040,1,2,42,1,3,1))
wtWebGraphThermoHygroTempValueEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:wtWebGraphThermoHygroTempValueEntry.setStatus(_A)
class _WtWebGraphThermoHygroTempValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_WtWebGraphThermoHygroTempValue_Type.__name__=_D
_WtWebGraphThermoHygroTempValue_Object=MibTableColumn
wtWebGraphThermoHygroTempValue=_WtWebGraphThermoHygroTempValue_Object((1,3,6,1,4,1,5040,1,2,42,1,3,1,1),_WtWebGraphThermoHygroTempValue_Type())
wtWebGraphThermoHygroTempValue.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphThermoHygroTempValue.setStatus(_A)
_WtWebGraphThermoHygroBinaryTempValueTable_Object=MibTable
wtWebGraphThermoHygroBinaryTempValueTable=_WtWebGraphThermoHygroBinaryTempValueTable_Object((1,3,6,1,4,1,5040,1,2,42,1,4))
if mibBuilder.loadTexts:wtWebGraphThermoHygroBinaryTempValueTable.setStatus(_A)
_WtWebGraphThermoHygroBinaryTempValueEntry_Object=MibTableRow
wtWebGraphThermoHygroBinaryTempValueEntry=_WtWebGraphThermoHygroBinaryTempValueEntry_Object((1,3,6,1,4,1,5040,1,2,42,1,4,1))
wtWebGraphThermoHygroBinaryTempValueEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:wtWebGraphThermoHygroBinaryTempValueEntry.setStatus(_A)
_WtWebGraphThermoHygroBinaryTempValue_Type=Integer32
_WtWebGraphThermoHygroBinaryTempValue_Object=MibTableColumn
wtWebGraphThermoHygroBinaryTempValue=_WtWebGraphThermoHygroBinaryTempValue_Object((1,3,6,1,4,1,5040,1,2,42,1,4,1,1),_WtWebGraphThermoHygroBinaryTempValue_Type())
wtWebGraphThermoHygroBinaryTempValue.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphThermoHygroBinaryTempValue.setStatus(_A)
_WtWebGraphThermoHygroTempValuePktTable_Object=MibTable
wtWebGraphThermoHygroTempValuePktTable=_WtWebGraphThermoHygroTempValuePktTable_Object((1,3,6,1,4,1,5040,1,2,42,1,8))
if mibBuilder.loadTexts:wtWebGraphThermoHygroTempValuePktTable.setStatus(_A)
_WtWebGraphThermoHygroTempValuePktEntry_Object=MibTableRow
wtWebGraphThermoHygroTempValuePktEntry=_WtWebGraphThermoHygroTempValuePktEntry_Object((1,3,6,1,4,1,5040,1,2,42,1,8,1))
wtWebGraphThermoHygroTempValuePktEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:wtWebGraphThermoHygroTempValuePktEntry.setStatus(_A)
class _WtWebGraphThermoHygroTempValuePkt_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_WtWebGraphThermoHygroTempValuePkt_Type.__name__=_D
_WtWebGraphThermoHygroTempValuePkt_Object=MibTableColumn
wtWebGraphThermoHygroTempValuePkt=_WtWebGraphThermoHygroTempValuePkt_Object((1,3,6,1,4,1,5040,1,2,42,1,8,1,1),_WtWebGraphThermoHygroTempValuePkt_Type())
wtWebGraphThermoHygroTempValuePkt.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphThermoHygroTempValuePkt.setStatus(_A)
_WtWebGraphThermoHygroSessCntrl_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroSessCntrl=_WtWebGraphThermoHygroSessCntrl_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,2))
_WtWebGraphThermoHygroSessCntrlPassword_Type=OctetString
_WtWebGraphThermoHygroSessCntrlPassword_Object=MibScalar
wtWebGraphThermoHygroSessCntrlPassword=_WtWebGraphThermoHygroSessCntrlPassword_Object((1,3,6,1,4,1,5040,1,2,42,2,1),_WtWebGraphThermoHygroSessCntrlPassword_Type())
wtWebGraphThermoHygroSessCntrlPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroSessCntrlPassword.setStatus(_A)
class _WtWebGraphThermoHygroSessCntrlConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('wtWebGraphThermoHygroSessCntrl-NoSession',0),('wtWebGraphThermoHygroSessCntrl-Session',1)))
_WtWebGraphThermoHygroSessCntrlConfigMode_Type.__name__=_E
_WtWebGraphThermoHygroSessCntrlConfigMode_Object=MibScalar
wtWebGraphThermoHygroSessCntrlConfigMode=_WtWebGraphThermoHygroSessCntrlConfigMode_Object((1,3,6,1,4,1,5040,1,2,42,2,2),_WtWebGraphThermoHygroSessCntrlConfigMode_Type())
wtWebGraphThermoHygroSessCntrlConfigMode.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphThermoHygroSessCntrlConfigMode.setStatus(_A)
_WtWebGraphThermoHygroSessCntrlLogout_Type=Integer32
_WtWebGraphThermoHygroSessCntrlLogout_Object=MibScalar
wtWebGraphThermoHygroSessCntrlLogout=_WtWebGraphThermoHygroSessCntrlLogout_Object((1,3,6,1,4,1,5040,1,2,42,2,3),_WtWebGraphThermoHygroSessCntrlLogout_Type())
wtWebGraphThermoHygroSessCntrlLogout.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroSessCntrlLogout.setStatus(_A)
_WtWebGraphThermoHygroSessCntrlAdminPassword_Type=OctetString
_WtWebGraphThermoHygroSessCntrlAdminPassword_Object=MibScalar
wtWebGraphThermoHygroSessCntrlAdminPassword=_WtWebGraphThermoHygroSessCntrlAdminPassword_Object((1,3,6,1,4,1,5040,1,2,42,2,4),_WtWebGraphThermoHygroSessCntrlAdminPassword_Type())
wtWebGraphThermoHygroSessCntrlAdminPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroSessCntrlAdminPassword.setStatus(_A)
_WtWebGraphThermoHygroSessCntrlConfigPassword_Type=OctetString
_WtWebGraphThermoHygroSessCntrlConfigPassword_Object=MibScalar
wtWebGraphThermoHygroSessCntrlConfigPassword=_WtWebGraphThermoHygroSessCntrlConfigPassword_Object((1,3,6,1,4,1,5040,1,2,42,2,5),_WtWebGraphThermoHygroSessCntrlConfigPassword_Type())
wtWebGraphThermoHygroSessCntrlConfigPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroSessCntrlConfigPassword.setStatus(_A)
_WtWebGraphThermoHygroConfig_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroConfig=_WtWebGraphThermoHygroConfig_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3))
_WtWebGraphThermoHygroDevice_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroDevice=_WtWebGraphThermoHygroDevice_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,1))
_WtWebGraphThermoHygroText_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroText=_WtWebGraphThermoHygroText_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,1,1))
_WtWebGraphThermoHygroDeviceName_Type=OctetString
_WtWebGraphThermoHygroDeviceName_Object=MibScalar
wtWebGraphThermoHygroDeviceName=_WtWebGraphThermoHygroDeviceName_Object((1,3,6,1,4,1,5040,1,2,42,3,1,1,1),_WtWebGraphThermoHygroDeviceName_Type())
wtWebGraphThermoHygroDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroDeviceName.setStatus(_A)
_WtWebGraphThermoHygroDeviceText_Type=OctetString
_WtWebGraphThermoHygroDeviceText_Object=MibScalar
wtWebGraphThermoHygroDeviceText=_WtWebGraphThermoHygroDeviceText_Object((1,3,6,1,4,1,5040,1,2,42,3,1,1,2),_WtWebGraphThermoHygroDeviceText_Type())
wtWebGraphThermoHygroDeviceText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroDeviceText.setStatus(_A)
_WtWebGraphThermoHygroDeviceLocation_Type=OctetString
_WtWebGraphThermoHygroDeviceLocation_Object=MibScalar
wtWebGraphThermoHygroDeviceLocation=_WtWebGraphThermoHygroDeviceLocation_Object((1,3,6,1,4,1,5040,1,2,42,3,1,1,3),_WtWebGraphThermoHygroDeviceLocation_Type())
wtWebGraphThermoHygroDeviceLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroDeviceLocation.setStatus(_A)
_WtWebGraphThermoHygroDeviceContact_Type=OctetString
_WtWebGraphThermoHygroDeviceContact_Object=MibScalar
wtWebGraphThermoHygroDeviceContact=_WtWebGraphThermoHygroDeviceContact_Object((1,3,6,1,4,1,5040,1,2,42,3,1,1,4),_WtWebGraphThermoHygroDeviceContact_Type())
wtWebGraphThermoHygroDeviceContact.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroDeviceContact.setStatus(_A)
_WtWebGraphThermoHygroTimeDate_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroTimeDate=_WtWebGraphThermoHygroTimeDate_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,1,2))
_WtWebGraphThermoHygroTimeZone_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroTimeZone=_WtWebGraphThermoHygroTimeZone_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,1,2,1))
_WtWebGraphThermoHygroTzOffsetHrs_Type=Integer32
_WtWebGraphThermoHygroTzOffsetHrs_Object=MibScalar
wtWebGraphThermoHygroTzOffsetHrs=_WtWebGraphThermoHygroTzOffsetHrs_Object((1,3,6,1,4,1,5040,1,2,42,3,1,2,1,1),_WtWebGraphThermoHygroTzOffsetHrs_Type())
wtWebGraphThermoHygroTzOffsetHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroTzOffsetHrs.setStatus(_A)
_WtWebGraphThermoHygroTzOffsetMin_Type=Integer32
_WtWebGraphThermoHygroTzOffsetMin_Object=MibScalar
wtWebGraphThermoHygroTzOffsetMin=_WtWebGraphThermoHygroTzOffsetMin_Object((1,3,6,1,4,1,5040,1,2,42,3,1,2,1,2),_WtWebGraphThermoHygroTzOffsetMin_Type())
wtWebGraphThermoHygroTzOffsetMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroTzOffsetMin.setStatus(_A)
class _WtWebGraphThermoHygroTzEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoHygroTzEnable_Type.__name__=_D
_WtWebGraphThermoHygroTzEnable_Object=MibScalar
wtWebGraphThermoHygroTzEnable=_WtWebGraphThermoHygroTzEnable_Object((1,3,6,1,4,1,5040,1,2,42,3,1,2,1,3),_WtWebGraphThermoHygroTzEnable_Type())
wtWebGraphThermoHygroTzEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroTzEnable.setStatus(_A)
_WtWebGraphThermoHygroStTzOffsetHrs_Type=Integer32
_WtWebGraphThermoHygroStTzOffsetHrs_Object=MibScalar
wtWebGraphThermoHygroStTzOffsetHrs=_WtWebGraphThermoHygroStTzOffsetHrs_Object((1,3,6,1,4,1,5040,1,2,42,3,1,2,1,4),_WtWebGraphThermoHygroStTzOffsetHrs_Type())
wtWebGraphThermoHygroStTzOffsetHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroStTzOffsetHrs.setStatus(_A)
_WtWebGraphThermoHygroStTzOffsetMin_Type=Integer32
_WtWebGraphThermoHygroStTzOffsetMin_Object=MibScalar
wtWebGraphThermoHygroStTzOffsetMin=_WtWebGraphThermoHygroStTzOffsetMin_Object((1,3,6,1,4,1,5040,1,2,42,3,1,2,1,5),_WtWebGraphThermoHygroStTzOffsetMin_Type())
wtWebGraphThermoHygroStTzOffsetMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroStTzOffsetMin.setStatus(_A)
class _WtWebGraphThermoHygroStTzEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoHygroStTzEnable_Type.__name__=_D
_WtWebGraphThermoHygroStTzEnable_Object=MibScalar
wtWebGraphThermoHygroStTzEnable=_WtWebGraphThermoHygroStTzEnable_Object((1,3,6,1,4,1,5040,1,2,42,3,1,2,1,6),_WtWebGraphThermoHygroStTzEnable_Type())
wtWebGraphThermoHygroStTzEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroStTzEnable.setStatus(_A)
class _WtWebGraphThermoHygroStTzStartMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('wtWebGraphThermoHygroStartMonth-January',1),('wtWebGraphThermoHygroStartMonth-February',2),('wtWebGraphThermoHygroStartMonth-March',3),('wtWebGraphThermoHygroStartMonth-April',4),('wtWebGraphThermoHygroStartMonth-May',5),('wtWebGraphThermoHygroStartMonth-June',6),('wtWebGraphThermoHygroStartMonth-July',7),('wtWebGraphThermoHygroStartMonth-August',8),('wtWebGraphThermoHygroStartMonth-September',9),('wtWebGraphThermoHygroStartMonth-October',10),('wtWebGraphThermoHygroStartMonth-November',11),('wtWebGraphThermoHygroStartMonth-December',12)))
_WtWebGraphThermoHygroStTzStartMonth_Type.__name__=_E
_WtWebGraphThermoHygroStTzStartMonth_Object=MibScalar
wtWebGraphThermoHygroStTzStartMonth=_WtWebGraphThermoHygroStTzStartMonth_Object((1,3,6,1,4,1,5040,1,2,42,3,1,2,1,7),_WtWebGraphThermoHygroStTzStartMonth_Type())
wtWebGraphThermoHygroStTzStartMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroStTzStartMonth.setStatus(_A)
class _WtWebGraphThermoHygroStTzStartMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('wtWebGraphThermoHygroStartMode-first',1),('wtWebGraphThermoHygroStartMode-second',2),('wtWebGraphThermoHygroStartMode-third',3),('wtWebGraphThermoHygroStartMode-fourth',4),('wtWebGraphThermoHygroStartMode-last',5)))
_WtWebGraphThermoHygroStTzStartMode_Type.__name__=_E
_WtWebGraphThermoHygroStTzStartMode_Object=MibScalar
wtWebGraphThermoHygroStTzStartMode=_WtWebGraphThermoHygroStTzStartMode_Object((1,3,6,1,4,1,5040,1,2,42,3,1,2,1,8),_WtWebGraphThermoHygroStTzStartMode_Type())
wtWebGraphThermoHygroStTzStartMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroStTzStartMode.setStatus(_A)
class _WtWebGraphThermoHygroStTzStartWday_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('wtWebGraphThermoHygroStartWday-Sunday',1),('wtWebGraphThermoHygroStartWday-Monday',2),('wtWebGraphThermoHygroStartWday-Tuesday',3),('wtWebGraphThermoHygroStartWday-Thursday',4),('wtWebGraphThermoHygroStartWday-Wednesday',5),('wtWebGraphThermoHygroStartWday-Friday',6),('wtWebGraphThermoHygroStartWday-Saturday',7)))
_WtWebGraphThermoHygroStTzStartWday_Type.__name__=_E
_WtWebGraphThermoHygroStTzStartWday_Object=MibScalar
wtWebGraphThermoHygroStTzStartWday=_WtWebGraphThermoHygroStTzStartWday_Object((1,3,6,1,4,1,5040,1,2,42,3,1,2,1,9),_WtWebGraphThermoHygroStTzStartWday_Type())
wtWebGraphThermoHygroStTzStartWday.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroStTzStartWday.setStatus(_A)
_WtWebGraphThermoHygroStTzStartHrs_Type=Integer32
_WtWebGraphThermoHygroStTzStartHrs_Object=MibScalar
wtWebGraphThermoHygroStTzStartHrs=_WtWebGraphThermoHygroStTzStartHrs_Object((1,3,6,1,4,1,5040,1,2,42,3,1,2,1,10),_WtWebGraphThermoHygroStTzStartHrs_Type())
wtWebGraphThermoHygroStTzStartHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroStTzStartHrs.setStatus(_A)
_WtWebGraphThermoHygroStTzStartMin_Type=Integer32
_WtWebGraphThermoHygroStTzStartMin_Object=MibScalar
wtWebGraphThermoHygroStTzStartMin=_WtWebGraphThermoHygroStTzStartMin_Object((1,3,6,1,4,1,5040,1,2,42,3,1,2,1,11),_WtWebGraphThermoHygroStTzStartMin_Type())
wtWebGraphThermoHygroStTzStartMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroStTzStartMin.setStatus(_A)
class _WtWebGraphThermoHygroStTzStopMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('wtWebGraphThermoHygroStopMonth-January',1),('wtWebGraphThermoHygroStopMonth-February',2),('wtWebGraphThermoHygroStopMonth-March',3),('wtWebGraphThermoHygroStopMonth-April',4),('wtWebGraphThermoHygroStopMonth-May',5),('wtWebGraphThermoHygroStopMonth-June',6),('wtWebGraphThermoHygroStopMonth-July',7),('wtWebGraphThermoHygroStopMonth-August',8),('wtWebGraphThermoHygroStopMonth-September',9),('wtWebGraphThermoHygroStopMonth-October',10),('wtWebGraphThermoHygroStopMonth-November',11),('wtWebGraphThermoHygroStopMonth-December',12)))
_WtWebGraphThermoHygroStTzStopMonth_Type.__name__=_E
_WtWebGraphThermoHygroStTzStopMonth_Object=MibScalar
wtWebGraphThermoHygroStTzStopMonth=_WtWebGraphThermoHygroStTzStopMonth_Object((1,3,6,1,4,1,5040,1,2,42,3,1,2,1,12),_WtWebGraphThermoHygroStTzStopMonth_Type())
wtWebGraphThermoHygroStTzStopMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroStTzStopMonth.setStatus(_A)
class _WtWebGraphThermoHygroStTzStopMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('wtWebGraphThermoHygroStopMode-first',1),('wtWebGraphThermoHygroStopMode-second',2),('wtWebGraphThermoHygroStopMode-third',3),('wtWebGraphThermoHygroStopMode-fourth',4),('wtWebGraphThermoHygroStopMode-last',5)))
_WtWebGraphThermoHygroStTzStopMode_Type.__name__=_E
_WtWebGraphThermoHygroStTzStopMode_Object=MibScalar
wtWebGraphThermoHygroStTzStopMode=_WtWebGraphThermoHygroStTzStopMode_Object((1,3,6,1,4,1,5040,1,2,42,3,1,2,1,13),_WtWebGraphThermoHygroStTzStopMode_Type())
wtWebGraphThermoHygroStTzStopMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroStTzStopMode.setStatus(_A)
class _WtWebGraphThermoHygroStTzStopWday_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('wtWebGraphThermoHygroStopWday-Sunday',1),('wtWebGraphThermoHygroStopWday-Monday',2),('wtWebGraphThermoHygroStopWday-Tuesday',3),('wtWebGraphThermoHygroStopWday-Thursday',4),('wtWebGraphThermoHygroStopWday-Wednesday',5),('wtWebGraphThermoHygroStopWday-Friday',6),('wtWebGraphThermoHygroStopWday-Saturday',7)))
_WtWebGraphThermoHygroStTzStopWday_Type.__name__=_E
_WtWebGraphThermoHygroStTzStopWday_Object=MibScalar
wtWebGraphThermoHygroStTzStopWday=_WtWebGraphThermoHygroStTzStopWday_Object((1,3,6,1,4,1,5040,1,2,42,3,1,2,1,14),_WtWebGraphThermoHygroStTzStopWday_Type())
wtWebGraphThermoHygroStTzStopWday.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroStTzStopWday.setStatus(_A)
_WtWebGraphThermoHygroStTzStopHrs_Type=Integer32
_WtWebGraphThermoHygroStTzStopHrs_Object=MibScalar
wtWebGraphThermoHygroStTzStopHrs=_WtWebGraphThermoHygroStTzStopHrs_Object((1,3,6,1,4,1,5040,1,2,42,3,1,2,1,15),_WtWebGraphThermoHygroStTzStopHrs_Type())
wtWebGraphThermoHygroStTzStopHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroStTzStopHrs.setStatus(_A)
_WtWebGraphThermoHygroStTzStopMin_Type=Integer32
_WtWebGraphThermoHygroStTzStopMin_Object=MibScalar
wtWebGraphThermoHygroStTzStopMin=_WtWebGraphThermoHygroStTzStopMin_Object((1,3,6,1,4,1,5040,1,2,42,3,1,2,1,16),_WtWebGraphThermoHygroStTzStopMin_Type())
wtWebGraphThermoHygroStTzStopMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroStTzStopMin.setStatus(_A)
_WtWebGraphThermoHygroTimeServer_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroTimeServer=_WtWebGraphThermoHygroTimeServer_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,1,2,2))
_WtWebGraphThermoHygroTimeServer1_Type=OctetString
_WtWebGraphThermoHygroTimeServer1_Object=MibScalar
wtWebGraphThermoHygroTimeServer1=_WtWebGraphThermoHygroTimeServer1_Object((1,3,6,1,4,1,5040,1,2,42,3,1,2,2,1),_WtWebGraphThermoHygroTimeServer1_Type())
wtWebGraphThermoHygroTimeServer1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroTimeServer1.setStatus(_A)
_WtWebGraphThermoHygroTimeServer2_Type=OctetString
_WtWebGraphThermoHygroTimeServer2_Object=MibScalar
wtWebGraphThermoHygroTimeServer2=_WtWebGraphThermoHygroTimeServer2_Object((1,3,6,1,4,1,5040,1,2,42,3,1,2,2,2),_WtWebGraphThermoHygroTimeServer2_Type())
wtWebGraphThermoHygroTimeServer2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroTimeServer2.setStatus(_A)
class _WtWebGraphThermoHygroTsEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoHygroTsEnable_Type.__name__=_D
_WtWebGraphThermoHygroTsEnable_Object=MibScalar
wtWebGraphThermoHygroTsEnable=_WtWebGraphThermoHygroTsEnable_Object((1,3,6,1,4,1,5040,1,2,42,3,1,2,2,3),_WtWebGraphThermoHygroTsEnable_Type())
wtWebGraphThermoHygroTsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroTsEnable.setStatus(_A)
_WtWebGraphThermoHygroTsSyncTime_Type=Integer32
_WtWebGraphThermoHygroTsSyncTime_Object=MibScalar
wtWebGraphThermoHygroTsSyncTime=_WtWebGraphThermoHygroTsSyncTime_Object((1,3,6,1,4,1,5040,1,2,42,3,1,2,2,4),_WtWebGraphThermoHygroTsSyncTime_Type())
wtWebGraphThermoHygroTsSyncTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroTsSyncTime.setStatus(_A)
_WtWebGraphThermoHygroDeviceClock_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroDeviceClock=_WtWebGraphThermoHygroDeviceClock_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,1,2,3))
class _WtWebGraphThermoHygroClockHrs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_WtWebGraphThermoHygroClockHrs_Type.__name__=_E
_WtWebGraphThermoHygroClockHrs_Object=MibScalar
wtWebGraphThermoHygroClockHrs=_WtWebGraphThermoHygroClockHrs_Object((1,3,6,1,4,1,5040,1,2,42,3,1,2,3,1),_WtWebGraphThermoHygroClockHrs_Type())
wtWebGraphThermoHygroClockHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroClockHrs.setStatus(_A)
class _WtWebGraphThermoHygroClockMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_WtWebGraphThermoHygroClockMin_Type.__name__=_E
_WtWebGraphThermoHygroClockMin_Object=MibScalar
wtWebGraphThermoHygroClockMin=_WtWebGraphThermoHygroClockMin_Object((1,3,6,1,4,1,5040,1,2,42,3,1,2,3,2),_WtWebGraphThermoHygroClockMin_Type())
wtWebGraphThermoHygroClockMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroClockMin.setStatus(_A)
class _WtWebGraphThermoHygroClockDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_WtWebGraphThermoHygroClockDay_Type.__name__=_E
_WtWebGraphThermoHygroClockDay_Object=MibScalar
wtWebGraphThermoHygroClockDay=_WtWebGraphThermoHygroClockDay_Object((1,3,6,1,4,1,5040,1,2,42,3,1,2,3,3),_WtWebGraphThermoHygroClockDay_Type())
wtWebGraphThermoHygroClockDay.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroClockDay.setStatus(_A)
class _WtWebGraphThermoHygroClockMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('wtWebGraphThermoHygroClockMonth-January',1),('wtWebGraphThermoHygroClockMonth-February',2),('wtWebGraphThermoHygroClockMonth-March',3),('wtWebGraphThermoHygroClockMonth-April',4),('wtWebGraphThermoHygroClockMonth-May',5),('wtWebGraphThermoHygroClockMonth-June',6),('wtWebGraphThermoHygroClockMonth-July',7),('wtWebGraphThermoHygroClockMonth-August',8),('wtWebGraphThermoHygroClockMonth-September',9),('wtWebGraphThermoHygroClockMonth-October',10),('wtWebGraphThermoHygroClockMonth-November',11),('wtWebGraphThermoHygroClockMonth-December',12)))
_WtWebGraphThermoHygroClockMonth_Type.__name__=_E
_WtWebGraphThermoHygroClockMonth_Object=MibScalar
wtWebGraphThermoHygroClockMonth=_WtWebGraphThermoHygroClockMonth_Object((1,3,6,1,4,1,5040,1,2,42,3,1,2,3,4),_WtWebGraphThermoHygroClockMonth_Type())
wtWebGraphThermoHygroClockMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroClockMonth.setStatus(_A)
class _WtWebGraphThermoHygroClockYear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtWebGraphThermoHygroClockYear_Type.__name__=_E
_WtWebGraphThermoHygroClockYear_Object=MibScalar
wtWebGraphThermoHygroClockYear=_WtWebGraphThermoHygroClockYear_Object((1,3,6,1,4,1,5040,1,2,42,3,1,2,3,5),_WtWebGraphThermoHygroClockYear_Type())
wtWebGraphThermoHygroClockYear.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroClockYear.setStatus(_A)
_WtWebGraphThermoHygroBasic_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroBasic=_WtWebGraphThermoHygroBasic_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,1,3))
_WtWebGraphThermoHygroNetwork_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroNetwork=_WtWebGraphThermoHygroNetwork_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,1,3,1))
_WtWebGraphThermoHygroIpAddress_Type=IpAddress
_WtWebGraphThermoHygroIpAddress_Object=MibScalar
wtWebGraphThermoHygroIpAddress=_WtWebGraphThermoHygroIpAddress_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,1,1),_WtWebGraphThermoHygroIpAddress_Type())
wtWebGraphThermoHygroIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroIpAddress.setStatus(_A)
_WtWebGraphThermoHygroSubnetMask_Type=IpAddress
_WtWebGraphThermoHygroSubnetMask_Object=MibScalar
wtWebGraphThermoHygroSubnetMask=_WtWebGraphThermoHygroSubnetMask_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,1,2),_WtWebGraphThermoHygroSubnetMask_Type())
wtWebGraphThermoHygroSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroSubnetMask.setStatus(_A)
_WtWebGraphThermoHygroGateway_Type=IpAddress
_WtWebGraphThermoHygroGateway_Object=MibScalar
wtWebGraphThermoHygroGateway=_WtWebGraphThermoHygroGateway_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,1,3),_WtWebGraphThermoHygroGateway_Type())
wtWebGraphThermoHygroGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGateway.setStatus(_A)
_WtWebGraphThermoHygroDnsServer1_Type=OctetString
_WtWebGraphThermoHygroDnsServer1_Object=MibScalar
wtWebGraphThermoHygroDnsServer1=_WtWebGraphThermoHygroDnsServer1_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,1,4),_WtWebGraphThermoHygroDnsServer1_Type())
wtWebGraphThermoHygroDnsServer1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroDnsServer1.setStatus(_A)
_WtWebGraphThermoHygroDnsServer2_Type=OctetString
_WtWebGraphThermoHygroDnsServer2_Object=MibScalar
wtWebGraphThermoHygroDnsServer2=_WtWebGraphThermoHygroDnsServer2_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,1,5),_WtWebGraphThermoHygroDnsServer2_Type())
wtWebGraphThermoHygroDnsServer2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroDnsServer2.setStatus(_A)
_WtWebGraphThermoHygroAddConfig_Type=OctetString
_WtWebGraphThermoHygroAddConfig_Object=MibScalar
wtWebGraphThermoHygroAddConfig=_WtWebGraphThermoHygroAddConfig_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,1,6),_WtWebGraphThermoHygroAddConfig_Type())
wtWebGraphThermoHygroAddConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAddConfig.setStatus(_A)
_WtWebGraphThermoHygroHTTP_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroHTTP=_WtWebGraphThermoHygroHTTP_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,1,3,2))
_WtWebGraphThermoHygroStartup_Type=OctetString
_WtWebGraphThermoHygroStartup_Object=MibScalar
wtWebGraphThermoHygroStartup=_WtWebGraphThermoHygroStartup_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,2,1),_WtWebGraphThermoHygroStartup_Type())
wtWebGraphThermoHygroStartup.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroStartup.setStatus(_A)
_WtWebGraphThermoHygroGetHeaderEnable_Type=OctetString
_WtWebGraphThermoHygroGetHeaderEnable_Object=MibScalar
wtWebGraphThermoHygroGetHeaderEnable=_WtWebGraphThermoHygroGetHeaderEnable_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,2,2),_WtWebGraphThermoHygroGetHeaderEnable_Type())
wtWebGraphThermoHygroGetHeaderEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGetHeaderEnable.setStatus(_A)
class _WtWebGraphThermoHygroHttpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphThermoHygroHttpPort_Type.__name__=_E
_WtWebGraphThermoHygroHttpPort_Object=MibScalar
wtWebGraphThermoHygroHttpPort=_WtWebGraphThermoHygroHttpPort_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,2,3),_WtWebGraphThermoHygroHttpPort_Type())
wtWebGraphThermoHygroHttpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroHttpPort.setStatus(_A)
_WtWebGraphThermoHygroMail_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroMail=_WtWebGraphThermoHygroMail_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,1,3,3))
_WtWebGraphThermoHygroMailAdName_Type=OctetString
_WtWebGraphThermoHygroMailAdName_Object=MibScalar
wtWebGraphThermoHygroMailAdName=_WtWebGraphThermoHygroMailAdName_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,3,1),_WtWebGraphThermoHygroMailAdName_Type())
wtWebGraphThermoHygroMailAdName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMailAdName.setStatus(_A)
_WtWebGraphThermoHygroMailReply_Type=OctetString
_WtWebGraphThermoHygroMailReply_Object=MibScalar
wtWebGraphThermoHygroMailReply=_WtWebGraphThermoHygroMailReply_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,3,2),_WtWebGraphThermoHygroMailReply_Type())
wtWebGraphThermoHygroMailReply.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMailReply.setStatus(_A)
_WtWebGraphThermoHygroMailServer_Type=OctetString
_WtWebGraphThermoHygroMailServer_Object=MibScalar
wtWebGraphThermoHygroMailServer=_WtWebGraphThermoHygroMailServer_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,3,3),_WtWebGraphThermoHygroMailServer_Type())
wtWebGraphThermoHygroMailServer.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMailServer.setStatus(_A)
_WtWebioAn1MailEnable_Type=OctetString
_WtWebioAn1MailEnable_Object=MibScalar
wtWebioAn1MailEnable=_WtWebioAn1MailEnable_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,3,4),_WtWebioAn1MailEnable_Type())
wtWebioAn1MailEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebioAn1MailEnable.setStatus(_A)
class _WtWebGraphThermoHygroMailAuthentication_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoHygroMailAuthentication_Type.__name__=_D
_WtWebGraphThermoHygroMailAuthentication_Object=MibScalar
wtWebGraphThermoHygroMailAuthentication=_WtWebGraphThermoHygroMailAuthentication_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,3,5),_WtWebGraphThermoHygroMailAuthentication_Type())
wtWebGraphThermoHygroMailAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMailAuthentication.setStatus(_A)
_WtWebGraphThermoHygroMailAuthUser_Type=OctetString
_WtWebGraphThermoHygroMailAuthUser_Object=MibScalar
wtWebGraphThermoHygroMailAuthUser=_WtWebGraphThermoHygroMailAuthUser_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,3,6),_WtWebGraphThermoHygroMailAuthUser_Type())
wtWebGraphThermoHygroMailAuthUser.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMailAuthUser.setStatus(_A)
_WtWebGraphThermoHygroMailAuthPassword_Type=OctetString
_WtWebGraphThermoHygroMailAuthPassword_Object=MibScalar
wtWebGraphThermoHygroMailAuthPassword=_WtWebGraphThermoHygroMailAuthPassword_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,3,7),_WtWebGraphThermoHygroMailAuthPassword_Type())
wtWebGraphThermoHygroMailAuthPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMailAuthPassword.setStatus(_A)
_WtWebGraphThermoHygroMailPop3Server_Type=OctetString
_WtWebGraphThermoHygroMailPop3Server_Object=MibScalar
wtWebGraphThermoHygroMailPop3Server=_WtWebGraphThermoHygroMailPop3Server_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,3,8),_WtWebGraphThermoHygroMailPop3Server_Type())
wtWebGraphThermoHygroMailPop3Server.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMailPop3Server.setStatus(_A)
_WtWebGraphThermoHygroSNMP_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroSNMP=_WtWebGraphThermoHygroSNMP_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,1,3,4))
_WtWebGraphThermoHygroSnmpCommunityStringRead_Type=OctetString
_WtWebGraphThermoHygroSnmpCommunityStringRead_Object=MibScalar
wtWebGraphThermoHygroSnmpCommunityStringRead=_WtWebGraphThermoHygroSnmpCommunityStringRead_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,4,1),_WtWebGraphThermoHygroSnmpCommunityStringRead_Type())
wtWebGraphThermoHygroSnmpCommunityStringRead.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroSnmpCommunityStringRead.setStatus(_A)
_WtWebGraphThermoHygroSnmpCommunityStringReadWrite_Type=OctetString
_WtWebGraphThermoHygroSnmpCommunityStringReadWrite_Object=MibScalar
wtWebGraphThermoHygroSnmpCommunityStringReadWrite=_WtWebGraphThermoHygroSnmpCommunityStringReadWrite_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,4,2),_WtWebGraphThermoHygroSnmpCommunityStringReadWrite_Type())
wtWebGraphThermoHygroSnmpCommunityStringReadWrite.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroSnmpCommunityStringReadWrite.setStatus(_A)
_WtWebGraphThermoHygroSystemTrapManagerIP_Type=OctetString
_WtWebGraphThermoHygroSystemTrapManagerIP_Object=MibScalar
wtWebGraphThermoHygroSystemTrapManagerIP=_WtWebGraphThermoHygroSystemTrapManagerIP_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,4,3),_WtWebGraphThermoHygroSystemTrapManagerIP_Type())
wtWebGraphThermoHygroSystemTrapManagerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroSystemTrapManagerIP.setStatus(_A)
class _WtWebGraphThermoHygroSystemTrapEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoHygroSystemTrapEnable_Type.__name__=_D
_WtWebGraphThermoHygroSystemTrapEnable_Object=MibScalar
wtWebGraphThermoHygroSystemTrapEnable=_WtWebGraphThermoHygroSystemTrapEnable_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,4,4),_WtWebGraphThermoHygroSystemTrapEnable_Type())
wtWebGraphThermoHygroSystemTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroSystemTrapEnable.setStatus(_A)
_WtWebGraphThermoHygroSnmpEnable_Type=OctetString
_WtWebGraphThermoHygroSnmpEnable_Object=MibScalar
wtWebGraphThermoHygroSnmpEnable=_WtWebGraphThermoHygroSnmpEnable_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,4,5),_WtWebGraphThermoHygroSnmpEnable_Type())
wtWebGraphThermoHygroSnmpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroSnmpEnable.setStatus(_A)
_WtWebGraphThermoHygroSnmpCommunityStringTrap_Type=OctetString
_WtWebGraphThermoHygroSnmpCommunityStringTrap_Object=MibScalar
wtWebGraphThermoHygroSnmpCommunityStringTrap=_WtWebGraphThermoHygroSnmpCommunityStringTrap_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,4,6),_WtWebGraphThermoHygroSnmpCommunityStringTrap_Type())
wtWebGraphThermoHygroSnmpCommunityStringTrap.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroSnmpCommunityStringTrap.setStatus(_A)
_WtWebGraphThermoHygroSnmpSystemTrapManagerPort_Type=Integer32
_WtWebGraphThermoHygroSnmpSystemTrapManagerPort_Object=MibScalar
wtWebGraphThermoHygroSnmpSystemTrapManagerPort=_WtWebGraphThermoHygroSnmpSystemTrapManagerPort_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,4,7),_WtWebGraphThermoHygroSnmpSystemTrapManagerPort_Type())
wtWebGraphThermoHygroSnmpSystemTrapManagerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroSnmpSystemTrapManagerPort.setStatus(_A)
_WtWebGraphThermoHygroUDP_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroUDP=_WtWebGraphThermoHygroUDP_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,1,3,5))
class _WtWebGraphThermoHygroUdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphThermoHygroUdpPort_Type.__name__=_E
_WtWebGraphThermoHygroUdpPort_Object=MibScalar
wtWebGraphThermoHygroUdpPort=_WtWebGraphThermoHygroUdpPort_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,5,1),_WtWebGraphThermoHygroUdpPort_Type())
wtWebGraphThermoHygroUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroUdpPort.setStatus(_A)
_WtWebGraphThermoHygroUdpEnable_Type=OctetString
_WtWebGraphThermoHygroUdpEnable_Object=MibScalar
wtWebGraphThermoHygroUdpEnable=_WtWebGraphThermoHygroUdpEnable_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,5,2),_WtWebGraphThermoHygroUdpEnable_Type())
wtWebGraphThermoHygroUdpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroUdpEnable.setStatus(_A)
_WtWebGraphThermoHygroSyslog_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroSyslog=_WtWebGraphThermoHygroSyslog_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,1,3,6))
_WtWebGraphThermoHygroSyslogServerIP_Type=OctetString
_WtWebGraphThermoHygroSyslogServerIP_Object=MibScalar
wtWebGraphThermoHygroSyslogServerIP=_WtWebGraphThermoHygroSyslogServerIP_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,6,1),_WtWebGraphThermoHygroSyslogServerIP_Type())
wtWebGraphThermoHygroSyslogServerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroSyslogServerIP.setStatus(_A)
_WtWebGraphThermoHygroSyslogServerPort_Type=Integer32
_WtWebGraphThermoHygroSyslogServerPort_Object=MibScalar
wtWebGraphThermoHygroSyslogServerPort=_WtWebGraphThermoHygroSyslogServerPort_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,6,2),_WtWebGraphThermoHygroSyslogServerPort_Type())
wtWebGraphThermoHygroSyslogServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroSyslogServerPort.setStatus(_A)
class _WtWebGraphThermoHygroSyslogSystemMessagesEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoHygroSyslogSystemMessagesEnable_Type.__name__=_D
_WtWebGraphThermoHygroSyslogSystemMessagesEnable_Object=MibScalar
wtWebGraphThermoHygroSyslogSystemMessagesEnable=_WtWebGraphThermoHygroSyslogSystemMessagesEnable_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,6,3),_WtWebGraphThermoHygroSyslogSystemMessagesEnable_Type())
wtWebGraphThermoHygroSyslogSystemMessagesEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroSyslogSystemMessagesEnable.setStatus(_A)
_WtWebGraphThermoHygroSyslogEnable_Type=OctetString
_WtWebGraphThermoHygroSyslogEnable_Object=MibScalar
wtWebGraphThermoHygroSyslogEnable=_WtWebGraphThermoHygroSyslogEnable_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,6,4),_WtWebGraphThermoHygroSyslogEnable_Type())
wtWebGraphThermoHygroSyslogEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroSyslogEnable.setStatus(_A)
_WtWebGraphThermoHygroFTP_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroFTP=_WtWebGraphThermoHygroFTP_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,1,3,7))
_WtWebGraphThermoHygroFTPServerIP_Type=OctetString
_WtWebGraphThermoHygroFTPServerIP_Object=MibScalar
wtWebGraphThermoHygroFTPServerIP=_WtWebGraphThermoHygroFTPServerIP_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,7,1),_WtWebGraphThermoHygroFTPServerIP_Type())
wtWebGraphThermoHygroFTPServerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroFTPServerIP.setStatus(_A)
_WtWebGraphThermoHygroFTPServerControlPort_Type=Integer32
_WtWebGraphThermoHygroFTPServerControlPort_Object=MibScalar
wtWebGraphThermoHygroFTPServerControlPort=_WtWebGraphThermoHygroFTPServerControlPort_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,7,2),_WtWebGraphThermoHygroFTPServerControlPort_Type())
wtWebGraphThermoHygroFTPServerControlPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroFTPServerControlPort.setStatus(_A)
_WtWebGraphThermoHygroFTPUserName_Type=OctetString
_WtWebGraphThermoHygroFTPUserName_Object=MibScalar
wtWebGraphThermoHygroFTPUserName=_WtWebGraphThermoHygroFTPUserName_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,7,3),_WtWebGraphThermoHygroFTPUserName_Type())
wtWebGraphThermoHygroFTPUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroFTPUserName.setStatus(_A)
_WtWebGraphThermoHygroFTPPassword_Type=OctetString
_WtWebGraphThermoHygroFTPPassword_Object=MibScalar
wtWebGraphThermoHygroFTPPassword=_WtWebGraphThermoHygroFTPPassword_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,7,4),_WtWebGraphThermoHygroFTPPassword_Type())
wtWebGraphThermoHygroFTPPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroFTPPassword.setStatus(_A)
_WtWebGraphThermoHygroFTPAccount_Type=OctetString
_WtWebGraphThermoHygroFTPAccount_Object=MibScalar
wtWebGraphThermoHygroFTPAccount=_WtWebGraphThermoHygroFTPAccount_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,7,5),_WtWebGraphThermoHygroFTPAccount_Type())
wtWebGraphThermoHygroFTPAccount.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroFTPAccount.setStatus(_A)
_WtWebGraphThermoHygroFTPOption_Type=OctetString
_WtWebGraphThermoHygroFTPOption_Object=MibScalar
wtWebGraphThermoHygroFTPOption=_WtWebGraphThermoHygroFTPOption_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,7,6),_WtWebGraphThermoHygroFTPOption_Type())
wtWebGraphThermoHygroFTPOption.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroFTPOption.setStatus(_A)
_WtWebGraphThermoHygroFTPEnable_Type=OctetString
_WtWebGraphThermoHygroFTPEnable_Object=MibScalar
wtWebGraphThermoHygroFTPEnable=_WtWebGraphThermoHygroFTPEnable_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,7,7),_WtWebGraphThermoHygroFTPEnable_Type())
wtWebGraphThermoHygroFTPEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroFTPEnable.setStatus(_A)
_WtWebGraphThermoHygroRSS_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroRSS=_WtWebGraphThermoHygroRSS_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,1,3,8))
_WtWebGraphThermoHygroRSSChannelTitle_Type=OctetString
_WtWebGraphThermoHygroRSSChannelTitle_Object=MibScalar
wtWebGraphThermoHygroRSSChannelTitle=_WtWebGraphThermoHygroRSSChannelTitle_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,8,1),_WtWebGraphThermoHygroRSSChannelTitle_Type())
wtWebGraphThermoHygroRSSChannelTitle.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroRSSChannelTitle.setStatus(_A)
_WtWebGraphThermoHygroRSSChannelLink_Type=OctetString
_WtWebGraphThermoHygroRSSChannelLink_Object=MibScalar
wtWebGraphThermoHygroRSSChannelLink=_WtWebGraphThermoHygroRSSChannelLink_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,8,2),_WtWebGraphThermoHygroRSSChannelLink_Type())
wtWebGraphThermoHygroRSSChannelLink.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroRSSChannelLink.setStatus(_A)
_WtWebGraphThermoHygroRSSChannelDescription_Type=OctetString
_WtWebGraphThermoHygroRSSChannelDescription_Object=MibScalar
wtWebGraphThermoHygroRSSChannelDescription=_WtWebGraphThermoHygroRSSChannelDescription_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,8,3),_WtWebGraphThermoHygroRSSChannelDescription_Type())
wtWebGraphThermoHygroRSSChannelDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroRSSChannelDescription.setStatus(_A)
_WtWebGraphThermoHygroRSSChannelImage_Type=OctetString
_WtWebGraphThermoHygroRSSChannelImage_Object=MibScalar
wtWebGraphThermoHygroRSSChannelImage=_WtWebGraphThermoHygroRSSChannelImage_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,8,4),_WtWebGraphThermoHygroRSSChannelImage_Type())
wtWebGraphThermoHygroRSSChannelImage.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroRSSChannelImage.setStatus(_A)
_WtWebGraphThermoHygroRSSChannelImageTitle_Type=OctetString
_WtWebGraphThermoHygroRSSChannelImageTitle_Object=MibScalar
wtWebGraphThermoHygroRSSChannelImageTitle=_WtWebGraphThermoHygroRSSChannelImageTitle_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,8,5),_WtWebGraphThermoHygroRSSChannelImageTitle_Type())
wtWebGraphThermoHygroRSSChannelImageTitle.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroRSSChannelImageTitle.setStatus(_A)
_WtWebGraphThermoHygroRSSChannelImageLink_Type=OctetString
_WtWebGraphThermoHygroRSSChannelImageLink_Object=MibScalar
wtWebGraphThermoHygroRSSChannelImageLink=_WtWebGraphThermoHygroRSSChannelImageLink_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,8,6),_WtWebGraphThermoHygroRSSChannelImageLink_Type())
wtWebGraphThermoHygroRSSChannelImageLink.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroRSSChannelImageLink.setStatus(_A)
_WtWebGraphThermoHygroRSSChannelItemTitle_Type=OctetString
_WtWebGraphThermoHygroRSSChannelItemTitle_Object=MibScalar
wtWebGraphThermoHygroRSSChannelItemTitle=_WtWebGraphThermoHygroRSSChannelItemTitle_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,8,7),_WtWebGraphThermoHygroRSSChannelItemTitle_Type())
wtWebGraphThermoHygroRSSChannelItemTitle.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroRSSChannelItemTitle.setStatus(_A)
_WtWebGraphThermoHygroRSSChannelItemLink_Type=OctetString
_WtWebGraphThermoHygroRSSChannelItemLink_Object=MibScalar
wtWebGraphThermoHygroRSSChannelItemLink=_WtWebGraphThermoHygroRSSChannelItemLink_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,8,8),_WtWebGraphThermoHygroRSSChannelItemLink_Type())
wtWebGraphThermoHygroRSSChannelItemLink.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroRSSChannelItemLink.setStatus(_A)
_WtWebGraphThermoHygroRSSChannelItemDescription_Type=OctetString
_WtWebGraphThermoHygroRSSChannelItemDescription_Object=MibScalar
wtWebGraphThermoHygroRSSChannelItemDescription=_WtWebGraphThermoHygroRSSChannelItemDescription_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,8,9),_WtWebGraphThermoHygroRSSChannelItemDescription_Type())
wtWebGraphThermoHygroRSSChannelItemDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroRSSChannelItemDescription.setStatus(_A)
_WtWebGraphThermoHygroRSSChannelItemQuantity_Type=OctetString
_WtWebGraphThermoHygroRSSChannelItemQuantity_Object=MibScalar
wtWebGraphThermoHygroRSSChannelItemQuantity=_WtWebGraphThermoHygroRSSChannelItemQuantity_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,8,10),_WtWebGraphThermoHygroRSSChannelItemQuantity_Type())
wtWebGraphThermoHygroRSSChannelItemQuantity.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroRSSChannelItemQuantity.setStatus(_A)
_WtWebGraphThermoHygroLanguage_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroLanguage=_WtWebGraphThermoHygroLanguage_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,1,3,9))
_WtWebGraphThermoHygroLanguageSelect_Type=OctetString
_WtWebGraphThermoHygroLanguageSelect_Object=MibScalar
wtWebGraphThermoHygroLanguageSelect=_WtWebGraphThermoHygroLanguageSelect_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,9,1),_WtWebGraphThermoHygroLanguageSelect_Type())
wtWebGraphThermoHygroLanguageSelect.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroLanguageSelect.setStatus(_A)
_WtWebGraphThermoHygroMQTT_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroMQTT=_WtWebGraphThermoHygroMQTT_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,1,3,12))
_WtWebGraphThermoHygroMQTTEnable_Type=OctetString
_WtWebGraphThermoHygroMQTTEnable_Object=MibScalar
wtWebGraphThermoHygroMQTTEnable=_WtWebGraphThermoHygroMQTTEnable_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,12,1),_WtWebGraphThermoHygroMQTTEnable_Type())
wtWebGraphThermoHygroMQTTEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMQTTEnable.setStatus(_A)
_WtWebGraphThermoHygroMQTTBrockerIP_Type=OctetString
_WtWebGraphThermoHygroMQTTBrockerIP_Object=MibScalar
wtWebGraphThermoHygroMQTTBrockerIP=_WtWebGraphThermoHygroMQTTBrockerIP_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,12,2),_WtWebGraphThermoHygroMQTTBrockerIP_Type())
wtWebGraphThermoHygroMQTTBrockerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMQTTBrockerIP.setStatus(_A)
_WtWebGraphThermoHygroMQTTUserName_Type=OctetString
_WtWebGraphThermoHygroMQTTUserName_Object=MibScalar
wtWebGraphThermoHygroMQTTUserName=_WtWebGraphThermoHygroMQTTUserName_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,12,3),_WtWebGraphThermoHygroMQTTUserName_Type())
wtWebGraphThermoHygroMQTTUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMQTTUserName.setStatus(_A)
_WtWebGraphThermoHygroMQTTPassword_Type=OctetString
_WtWebGraphThermoHygroMQTTPassword_Object=MibScalar
wtWebGraphThermoHygroMQTTPassword=_WtWebGraphThermoHygroMQTTPassword_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,12,4),_WtWebGraphThermoHygroMQTTPassword_Type())
wtWebGraphThermoHygroMQTTPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMQTTPassword.setStatus(_A)
_WtWebGraphThermoHygroMQTTLocalPort_Type=Integer32
_WtWebGraphThermoHygroMQTTLocalPort_Object=MibScalar
wtWebGraphThermoHygroMQTTLocalPort=_WtWebGraphThermoHygroMQTTLocalPort_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,12,5),_WtWebGraphThermoHygroMQTTLocalPort_Type())
wtWebGraphThermoHygroMQTTLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMQTTLocalPort.setStatus(_A)
_WtWebGraphThermoHygroMQTTBrokerServerPort_Type=Integer32
_WtWebGraphThermoHygroMQTTBrokerServerPort_Object=MibScalar
wtWebGraphThermoHygroMQTTBrokerServerPort=_WtWebGraphThermoHygroMQTTBrokerServerPort_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,12,6),_WtWebGraphThermoHygroMQTTBrokerServerPort_Type())
wtWebGraphThermoHygroMQTTBrokerServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMQTTBrokerServerPort.setStatus(_A)
_WtWebGraphThermoHygroMQTTInterval_Type=Integer32
_WtWebGraphThermoHygroMQTTInterval_Object=MibScalar
wtWebGraphThermoHygroMQTTInterval=_WtWebGraphThermoHygroMQTTInterval_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,12,7),_WtWebGraphThermoHygroMQTTInterval_Type())
wtWebGraphThermoHygroMQTTInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMQTTInterval.setStatus(_A)
_WtWebGraphThermoHygroMQTTLastWillEnable_Type=OctetString
_WtWebGraphThermoHygroMQTTLastWillEnable_Object=MibScalar
wtWebGraphThermoHygroMQTTLastWillEnable=_WtWebGraphThermoHygroMQTTLastWillEnable_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,12,8),_WtWebGraphThermoHygroMQTTLastWillEnable_Type())
wtWebGraphThermoHygroMQTTLastWillEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMQTTLastWillEnable.setStatus(_A)
_WtWebGraphThermoHygroMQTTLastWillTopic_Type=OctetString
_WtWebGraphThermoHygroMQTTLastWillTopic_Object=MibScalar
wtWebGraphThermoHygroMQTTLastWillTopic=_WtWebGraphThermoHygroMQTTLastWillTopic_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,12,9),_WtWebGraphThermoHygroMQTTLastWillTopic_Type())
wtWebGraphThermoHygroMQTTLastWillTopic.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMQTTLastWillTopic.setStatus(_A)
_WtWebGraphThermoHygroMQTTLastWillMsg_Type=OctetString
_WtWebGraphThermoHygroMQTTLastWillMsg_Object=MibScalar
wtWebGraphThermoHygroMQTTLastWillMsg=_WtWebGraphThermoHygroMQTTLastWillMsg_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,12,10),_WtWebGraphThermoHygroMQTTLastWillMsg_Type())
wtWebGraphThermoHygroMQTTLastWillMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMQTTLastWillMsg.setStatus(_A)
class _WtWebGraphThermoHygroMQTTLastWillQoS_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoHygroMQTTLastWillQoS_Type.__name__=_D
_WtWebGraphThermoHygroMQTTLastWillQoS_Object=MibScalar
wtWebGraphThermoHygroMQTTLastWillQoS=_WtWebGraphThermoHygroMQTTLastWillQoS_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,12,11),_WtWebGraphThermoHygroMQTTLastWillQoS_Type())
wtWebGraphThermoHygroMQTTLastWillQoS.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMQTTLastWillQoS.setStatus(_A)
class _WtWebGraphThermoHygroMQTTLastWillRetain_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoHygroMQTTLastWillRetain_Type.__name__=_D
_WtWebGraphThermoHygroMQTTLastWillRetain_Object=MibScalar
wtWebGraphThermoHygroMQTTLastWillRetain=_WtWebGraphThermoHygroMQTTLastWillRetain_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,12,12),_WtWebGraphThermoHygroMQTTLastWillRetain_Type())
wtWebGraphThermoHygroMQTTLastWillRetain.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMQTTLastWillRetain.setStatus(_A)
_WtWebGraphThermoHygroMQTTLastWillConnectEnable_Type=OctetString
_WtWebGraphThermoHygroMQTTLastWillConnectEnable_Object=MibScalar
wtWebGraphThermoHygroMQTTLastWillConnectEnable=_WtWebGraphThermoHygroMQTTLastWillConnectEnable_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,12,13),_WtWebGraphThermoHygroMQTTLastWillConnectEnable_Type())
wtWebGraphThermoHygroMQTTLastWillConnectEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMQTTLastWillConnectEnable.setStatus(_A)
_WtWebGraphThermoHygroMQTTLastWillConnectMsg_Type=OctetString
_WtWebGraphThermoHygroMQTTLastWillConnectMsg_Object=MibScalar
wtWebGraphThermoHygroMQTTLastWillConnectMsg=_WtWebGraphThermoHygroMQTTLastWillConnectMsg_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,12,14),_WtWebGraphThermoHygroMQTTLastWillConnectMsg_Type())
wtWebGraphThermoHygroMQTTLastWillConnectMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMQTTLastWillConnectMsg.setStatus(_A)
_WtWebGraphThermoHygroREST_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroREST=_WtWebGraphThermoHygroREST_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,1,3,13))
_WtWebGraphThermoHygroRESTEnable_Type=OctetString
_WtWebGraphThermoHygroRESTEnable_Object=MibScalar
wtWebGraphThermoHygroRESTEnable=_WtWebGraphThermoHygroRESTEnable_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,13,1),_WtWebGraphThermoHygroRESTEnable_Type())
wtWebGraphThermoHygroRESTEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroRESTEnable.setStatus(_A)
_WtWebGraphThermoHygroRESTDigestAuthEnable_Type=OctetString
_WtWebGraphThermoHygroRESTDigestAuthEnable_Object=MibScalar
wtWebGraphThermoHygroRESTDigestAuthEnable=_WtWebGraphThermoHygroRESTDigestAuthEnable_Object((1,3,6,1,4,1,5040,1,2,42,3,1,3,13,2),_WtWebGraphThermoHygroRESTDigestAuthEnable_Type())
wtWebGraphThermoHygroRESTDigestAuthEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroRESTDigestAuthEnable.setStatus(_A)
_WtWebGraphThermoHygroDatalogger_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroDatalogger=_WtWebGraphThermoHygroDatalogger_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,1,4))
class _WtWebGraphThermoHygroLoggerTimebase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('wtWebGraphThermoHygroDatalogger-1Min',1),('wtWebGraphThermoHygroDatalogger-5Min',2),('wtWebGraphThermoHygroDatalogger-15Min',3),('wtWebGraphThermoHygroDatalogger-60Min',4)))
_WtWebGraphThermoHygroLoggerTimebase_Type.__name__=_E
_WtWebGraphThermoHygroLoggerTimebase_Object=MibScalar
wtWebGraphThermoHygroLoggerTimebase=_WtWebGraphThermoHygroLoggerTimebase_Object((1,3,6,1,4,1,5040,1,2,42,3,1,4,1),_WtWebGraphThermoHygroLoggerTimebase_Type())
wtWebGraphThermoHygroLoggerTimebase.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroLoggerTimebase.setStatus(_A)
class _WtWebGraphThermoHygroLoggerSensorSel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoHygroLoggerSensorSel_Type.__name__=_D
_WtWebGraphThermoHygroLoggerSensorSel_Object=MibScalar
wtWebGraphThermoHygroLoggerSensorSel=_WtWebGraphThermoHygroLoggerSensorSel_Object((1,3,6,1,4,1,5040,1,2,42,3,1,4,2),_WtWebGraphThermoHygroLoggerSensorSel_Type())
wtWebGraphThermoHygroLoggerSensorSel.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroLoggerSensorSel.setStatus(_A)
_WtWebGraphThermoHygroAlarm_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroAlarm=_WtWebGraphThermoHygroAlarm_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,1,5))
class _WtWebGraphThermoHygroAlarmCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_WtWebGraphThermoHygroAlarmCount_Type.__name__=_E
_WtWebGraphThermoHygroAlarmCount_Object=MibScalar
wtWebGraphThermoHygroAlarmCount=_WtWebGraphThermoHygroAlarmCount_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,1),_WtWebGraphThermoHygroAlarmCount_Type())
wtWebGraphThermoHygroAlarmCount.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmCount.setStatus(_A)
_WtWebGraphThermoHygroAlarmIfTable_Object=MibTable
wtWebGraphThermoHygroAlarmIfTable=_WtWebGraphThermoHygroAlarmIfTable_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,2))
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmIfTable.setStatus(_A)
_WtWebGraphThermoHygroAlarmIfEntry_Object=MibTableRow
wtWebGraphThermoHygroAlarmIfEntry=_WtWebGraphThermoHygroAlarmIfEntry_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,2,1))
wtWebGraphThermoHygroAlarmIfEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmIfEntry.setStatus(_A)
class _WtWebGraphThermoHygroAlarmNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_WtWebGraphThermoHygroAlarmNo_Type.__name__=_E
_WtWebGraphThermoHygroAlarmNo_Object=MibTableColumn
wtWebGraphThermoHygroAlarmNo=_WtWebGraphThermoHygroAlarmNo_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,2,1,1),_WtWebGraphThermoHygroAlarmNo_Type())
wtWebGraphThermoHygroAlarmNo.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmNo.setStatus(_A)
_WtWebGraphThermoHygroAlarmTable_Object=MibTable
wtWebGraphThermoHygroAlarmTable=_WtWebGraphThermoHygroAlarmTable_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3))
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmTable.setStatus(_A)
_WtWebGraphThermoHygroAlarmEntry_Object=MibTableRow
wtWebGraphThermoHygroAlarmEntry=_WtWebGraphThermoHygroAlarmEntry_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1))
wtWebGraphThermoHygroAlarmEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmEntry.setStatus(_A)
class _WtWebGraphThermoHygroAlarmTrigger_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoHygroAlarmTrigger_Type.__name__=_D
_WtWebGraphThermoHygroAlarmTrigger_Object=MibTableColumn
wtWebGraphThermoHygroAlarmTrigger=_WtWebGraphThermoHygroAlarmTrigger_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,1),_WtWebGraphThermoHygroAlarmTrigger_Type())
wtWebGraphThermoHygroAlarmTrigger.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmTrigger.setStatus(_A)
_WtWebGraphThermoHygroAlarmMin_Type=OctetString
_WtWebGraphThermoHygroAlarmMin_Object=MibTableColumn
wtWebGraphThermoHygroAlarmMin=_WtWebGraphThermoHygroAlarmMin_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,2),_WtWebGraphThermoHygroAlarmMin_Type())
wtWebGraphThermoHygroAlarmMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmMin.setStatus(_A)
_WtWebGraphThermoHygroAlarmMax_Type=OctetString
_WtWebGraphThermoHygroAlarmMax_Object=MibTableColumn
wtWebGraphThermoHygroAlarmMax=_WtWebGraphThermoHygroAlarmMax_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,3),_WtWebGraphThermoHygroAlarmMax_Type())
wtWebGraphThermoHygroAlarmMax.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmMax.setStatus(_A)
_WtWebGraphThermoHygroAlarmHysteresis_Type=OctetString
_WtWebGraphThermoHygroAlarmHysteresis_Object=MibTableColumn
wtWebGraphThermoHygroAlarmHysteresis=_WtWebGraphThermoHygroAlarmHysteresis_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,4),_WtWebGraphThermoHygroAlarmHysteresis_Type())
wtWebGraphThermoHygroAlarmHysteresis.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmHysteresis.setStatus(_A)
_WtWebGraphThermoHygroAlarmDelay_Type=OctetString
_WtWebGraphThermoHygroAlarmDelay_Object=MibTableColumn
wtWebGraphThermoHygroAlarmDelay=_WtWebGraphThermoHygroAlarmDelay_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,5),_WtWebGraphThermoHygroAlarmDelay_Type())
wtWebGraphThermoHygroAlarmDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmDelay.setStatus(_A)
_WtWebGraphThermoHygroAlarmInterval_Type=OctetString
_WtWebGraphThermoHygroAlarmInterval_Object=MibTableColumn
wtWebGraphThermoHygroAlarmInterval=_WtWebGraphThermoHygroAlarmInterval_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,6),_WtWebGraphThermoHygroAlarmInterval_Type())
wtWebGraphThermoHygroAlarmInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmInterval.setStatus(_A)
class _WtWebGraphThermoHygroAlarmEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoHygroAlarmEnable_Type.__name__=_D
_WtWebGraphThermoHygroAlarmEnable_Object=MibTableColumn
wtWebGraphThermoHygroAlarmEnable=_WtWebGraphThermoHygroAlarmEnable_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,7),_WtWebGraphThermoHygroAlarmEnable_Type())
wtWebGraphThermoHygroAlarmEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmEnable.setStatus(_A)
_WtWebGraphThermoHygroAlarmEMailAddr_Type=OctetString
_WtWebGraphThermoHygroAlarmEMailAddr_Object=MibTableColumn
wtWebGraphThermoHygroAlarmEMailAddr=_WtWebGraphThermoHygroAlarmEMailAddr_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,8),_WtWebGraphThermoHygroAlarmEMailAddr_Type())
wtWebGraphThermoHygroAlarmEMailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmEMailAddr.setStatus(_A)
_WtWebGraphThermoHygroAlarmMailSubject_Type=OctetString
_WtWebGraphThermoHygroAlarmMailSubject_Object=MibTableColumn
wtWebGraphThermoHygroAlarmMailSubject=_WtWebGraphThermoHygroAlarmMailSubject_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,9),_WtWebGraphThermoHygroAlarmMailSubject_Type())
wtWebGraphThermoHygroAlarmMailSubject.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmMailSubject.setStatus(_A)
_WtWebGraphThermoHygroAlarmMailText_Type=OctetString
_WtWebGraphThermoHygroAlarmMailText_Object=MibTableColumn
wtWebGraphThermoHygroAlarmMailText=_WtWebGraphThermoHygroAlarmMailText_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,10),_WtWebGraphThermoHygroAlarmMailText_Type())
wtWebGraphThermoHygroAlarmMailText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmMailText.setStatus(_A)
_WtWebGraphThermoHygroAlarmManagerIP_Type=OctetString
_WtWebGraphThermoHygroAlarmManagerIP_Object=MibTableColumn
wtWebGraphThermoHygroAlarmManagerIP=_WtWebGraphThermoHygroAlarmManagerIP_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,11),_WtWebGraphThermoHygroAlarmManagerIP_Type())
wtWebGraphThermoHygroAlarmManagerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmManagerIP.setStatus(_A)
_WtWebGraphThermoHygroAlarmTrapText_Type=OctetString
_WtWebGraphThermoHygroAlarmTrapText_Object=MibTableColumn
wtWebGraphThermoHygroAlarmTrapText=_WtWebGraphThermoHygroAlarmTrapText_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,12),_WtWebGraphThermoHygroAlarmTrapText_Type())
wtWebGraphThermoHygroAlarmTrapText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmTrapText.setStatus(_A)
class _WtWebGraphThermoHygroAlarmMailOptions_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoHygroAlarmMailOptions_Type.__name__=_D
_WtWebGraphThermoHygroAlarmMailOptions_Object=MibTableColumn
wtWebGraphThermoHygroAlarmMailOptions=_WtWebGraphThermoHygroAlarmMailOptions_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,13),_WtWebGraphThermoHygroAlarmMailOptions_Type())
wtWebGraphThermoHygroAlarmMailOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmMailOptions.setStatus(_A)
_WtWebGraphThermoHygroAlarmTcpIpAddr_Type=OctetString
_WtWebGraphThermoHygroAlarmTcpIpAddr_Object=MibTableColumn
wtWebGraphThermoHygroAlarmTcpIpAddr=_WtWebGraphThermoHygroAlarmTcpIpAddr_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,14),_WtWebGraphThermoHygroAlarmTcpIpAddr_Type())
wtWebGraphThermoHygroAlarmTcpIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmTcpIpAddr.setStatus(_A)
class _WtWebGraphThermoHygroAlarmTcpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphThermoHygroAlarmTcpPort_Type.__name__=_E
_WtWebGraphThermoHygroAlarmTcpPort_Object=MibTableColumn
wtWebGraphThermoHygroAlarmTcpPort=_WtWebGraphThermoHygroAlarmTcpPort_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,15),_WtWebGraphThermoHygroAlarmTcpPort_Type())
wtWebGraphThermoHygroAlarmTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmTcpPort.setStatus(_A)
_WtWebGraphThermoHygroAlarmTcpText_Type=OctetString
_WtWebGraphThermoHygroAlarmTcpText_Object=MibTableColumn
wtWebGraphThermoHygroAlarmTcpText=_WtWebGraphThermoHygroAlarmTcpText_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,16),_WtWebGraphThermoHygroAlarmTcpText_Type())
wtWebGraphThermoHygroAlarmTcpText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmTcpText.setStatus(_A)
_WtWebGraphThermoHygroAlarmClearMailSubject_Type=OctetString
_WtWebGraphThermoHygroAlarmClearMailSubject_Object=MibTableColumn
wtWebGraphThermoHygroAlarmClearMailSubject=_WtWebGraphThermoHygroAlarmClearMailSubject_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,17),_WtWebGraphThermoHygroAlarmClearMailSubject_Type())
wtWebGraphThermoHygroAlarmClearMailSubject.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmClearMailSubject.setStatus(_A)
_WtWebGraphThermoHygroAlarmClearMailText_Type=OctetString
_WtWebGraphThermoHygroAlarmClearMailText_Object=MibTableColumn
wtWebGraphThermoHygroAlarmClearMailText=_WtWebGraphThermoHygroAlarmClearMailText_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,18),_WtWebGraphThermoHygroAlarmClearMailText_Type())
wtWebGraphThermoHygroAlarmClearMailText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmClearMailText.setStatus(_A)
_WtWebGraphThermoHygroAlarmClearTrapText_Type=OctetString
_WtWebGraphThermoHygroAlarmClearTrapText_Object=MibTableColumn
wtWebGraphThermoHygroAlarmClearTrapText=_WtWebGraphThermoHygroAlarmClearTrapText_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,19),_WtWebGraphThermoHygroAlarmClearTrapText_Type())
wtWebGraphThermoHygroAlarmClearTrapText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmClearTrapText.setStatus(_A)
_WtWebGraphThermoHygroAlarmClearTcpText_Type=OctetString
_WtWebGraphThermoHygroAlarmClearTcpText_Object=MibTableColumn
wtWebGraphThermoHygroAlarmClearTcpText=_WtWebGraphThermoHygroAlarmClearTcpText_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,20),_WtWebGraphThermoHygroAlarmClearTcpText_Type())
wtWebGraphThermoHygroAlarmClearTcpText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmClearTcpText.setStatus(_A)
_WtWebGraphThermoHygroAlarmDeltaTemp_Type=OctetString
_WtWebGraphThermoHygroAlarmDeltaTemp_Object=MibTableColumn
wtWebGraphThermoHygroAlarmDeltaTemp=_WtWebGraphThermoHygroAlarmDeltaTemp_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,21),_WtWebGraphThermoHygroAlarmDeltaTemp_Type())
wtWebGraphThermoHygroAlarmDeltaTemp.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmDeltaTemp.setStatus(_A)
_WtWebGraphThermoHygroAlarmRHMin_Type=OctetString
_WtWebGraphThermoHygroAlarmRHMin_Object=MibTableColumn
wtWebGraphThermoHygroAlarmRHMin=_WtWebGraphThermoHygroAlarmRHMin_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,22),_WtWebGraphThermoHygroAlarmRHMin_Type())
wtWebGraphThermoHygroAlarmRHMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmRHMin.setStatus(_A)
_WtWebGraphThermoHygroAlarmRHMax_Type=OctetString
_WtWebGraphThermoHygroAlarmRHMax_Object=MibTableColumn
wtWebGraphThermoHygroAlarmRHMax=_WtWebGraphThermoHygroAlarmRHMax_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,23),_WtWebGraphThermoHygroAlarmRHMax_Type())
wtWebGraphThermoHygroAlarmRHMax.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmRHMax.setStatus(_A)
_WtWebGraphThermoHygroAlarmRHHysteresis_Type=OctetString
_WtWebGraphThermoHygroAlarmRHHysteresis_Object=MibTableColumn
wtWebGraphThermoHygroAlarmRHHysteresis=_WtWebGraphThermoHygroAlarmRHHysteresis_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,24),_WtWebGraphThermoHygroAlarmRHHysteresis_Type())
wtWebGraphThermoHygroAlarmRHHysteresis.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmRHHysteresis.setStatus(_A)
_WtWebGraphThermoHygroAlarmAHMin_Type=OctetString
_WtWebGraphThermoHygroAlarmAHMin_Object=MibTableColumn
wtWebGraphThermoHygroAlarmAHMin=_WtWebGraphThermoHygroAlarmAHMin_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,25),_WtWebGraphThermoHygroAlarmAHMin_Type())
wtWebGraphThermoHygroAlarmAHMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmAHMin.setStatus(_A)
_WtWebGraphThermoHygroAlarmAHMax_Type=OctetString
_WtWebGraphThermoHygroAlarmAHMax_Object=MibTableColumn
wtWebGraphThermoHygroAlarmAHMax=_WtWebGraphThermoHygroAlarmAHMax_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,26),_WtWebGraphThermoHygroAlarmAHMax_Type())
wtWebGraphThermoHygroAlarmAHMax.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmAHMax.setStatus(_A)
_WtWebGraphThermoHygroAlarmSyslogIpAddr_Type=OctetString
_WtWebGraphThermoHygroAlarmSyslogIpAddr_Object=MibTableColumn
wtWebGraphThermoHygroAlarmSyslogIpAddr=_WtWebGraphThermoHygroAlarmSyslogIpAddr_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,27),_WtWebGraphThermoHygroAlarmSyslogIpAddr_Type())
wtWebGraphThermoHygroAlarmSyslogIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmSyslogIpAddr.setStatus(_A)
class _WtWebGraphThermoHygroAlarmSyslogPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphThermoHygroAlarmSyslogPort_Type.__name__=_E
_WtWebGraphThermoHygroAlarmSyslogPort_Object=MibTableColumn
wtWebGraphThermoHygroAlarmSyslogPort=_WtWebGraphThermoHygroAlarmSyslogPort_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,28),_WtWebGraphThermoHygroAlarmSyslogPort_Type())
wtWebGraphThermoHygroAlarmSyslogPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmSyslogPort.setStatus(_A)
_WtWebGraphThermoHygroAlarmSyslogText_Type=OctetString
_WtWebGraphThermoHygroAlarmSyslogText_Object=MibTableColumn
wtWebGraphThermoHygroAlarmSyslogText=_WtWebGraphThermoHygroAlarmSyslogText_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,29),_WtWebGraphThermoHygroAlarmSyslogText_Type())
wtWebGraphThermoHygroAlarmSyslogText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmSyslogText.setStatus(_A)
_WtWebGraphThermoHygroAlarmSyslogClearText_Type=OctetString
_WtWebGraphThermoHygroAlarmSyslogClearText_Object=MibTableColumn
wtWebGraphThermoHygroAlarmSyslogClearText=_WtWebGraphThermoHygroAlarmSyslogClearText_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,30),_WtWebGraphThermoHygroAlarmSyslogClearText_Type())
wtWebGraphThermoHygroAlarmSyslogClearText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmSyslogClearText.setStatus(_A)
_WtWebGraphThermoHygroAlarmFtpDataPort_Type=OctetString
_WtWebGraphThermoHygroAlarmFtpDataPort_Object=MibTableColumn
wtWebGraphThermoHygroAlarmFtpDataPort=_WtWebGraphThermoHygroAlarmFtpDataPort_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,31),_WtWebGraphThermoHygroAlarmFtpDataPort_Type())
wtWebGraphThermoHygroAlarmFtpDataPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmFtpDataPort.setStatus(_A)
_WtWebGraphThermoHygroAlarmFtpFileName_Type=OctetString
_WtWebGraphThermoHygroAlarmFtpFileName_Object=MibTableColumn
wtWebGraphThermoHygroAlarmFtpFileName=_WtWebGraphThermoHygroAlarmFtpFileName_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,32),_WtWebGraphThermoHygroAlarmFtpFileName_Type())
wtWebGraphThermoHygroAlarmFtpFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmFtpFileName.setStatus(_A)
_WtWebGraphThermoHygroAlarmFtpText_Type=OctetString
_WtWebGraphThermoHygroAlarmFtpText_Object=MibTableColumn
wtWebGraphThermoHygroAlarmFtpText=_WtWebGraphThermoHygroAlarmFtpText_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,33),_WtWebGraphThermoHygroAlarmFtpText_Type())
wtWebGraphThermoHygroAlarmFtpText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmFtpText.setStatus(_A)
_WtWebGraphThermoHygroAlarmFtpClearText_Type=OctetString
_WtWebGraphThermoHygroAlarmFtpClearText_Object=MibTableColumn
wtWebGraphThermoHygroAlarmFtpClearText=_WtWebGraphThermoHygroAlarmFtpClearText_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,34),_WtWebGraphThermoHygroAlarmFtpClearText_Type())
wtWebGraphThermoHygroAlarmFtpClearText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmFtpClearText.setStatus(_A)
class _WtWebGraphThermoHygroAlarmFtpOption_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoHygroAlarmFtpOption_Type.__name__=_D
_WtWebGraphThermoHygroAlarmFtpOption_Object=MibTableColumn
wtWebGraphThermoHygroAlarmFtpOption=_WtWebGraphThermoHygroAlarmFtpOption_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,35),_WtWebGraphThermoHygroAlarmFtpOption_Type())
wtWebGraphThermoHygroAlarmFtpOption.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmFtpOption.setStatus(_A)
_WtWebGraphThermoHygroAlarmTimerCron_Type=OctetString
_WtWebGraphThermoHygroAlarmTimerCron_Object=MibTableColumn
wtWebGraphThermoHygroAlarmTimerCron=_WtWebGraphThermoHygroAlarmTimerCron_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,36),_WtWebGraphThermoHygroAlarmTimerCron_Type())
wtWebGraphThermoHygroAlarmTimerCron.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmTimerCron.setStatus(_A)
_WtWebGraphThermoHygroAlarmName_Type=OctetString
_WtWebGraphThermoHygroAlarmName_Object=MibTableColumn
wtWebGraphThermoHygroAlarmName=_WtWebGraphThermoHygroAlarmName_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,39),_WtWebGraphThermoHygroAlarmName_Type())
wtWebGraphThermoHygroAlarmName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmName.setStatus(_A)
_WtWebGraphThermoHygroAlarmActive_Type=OctetString
_WtWebGraphThermoHygroAlarmActive_Object=MibTableColumn
wtWebGraphThermoHygroAlarmActive=_WtWebGraphThermoHygroAlarmActive_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,40),_WtWebGraphThermoHygroAlarmActive_Type())
wtWebGraphThermoHygroAlarmActive.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmActive.setStatus(_A)
_WtWebGraphThermoHygroAlarmHttpReqAuthEnable_Type=OctetString
_WtWebGraphThermoHygroAlarmHttpReqAuthEnable_Object=MibTableColumn
wtWebGraphThermoHygroAlarmHttpReqAuthEnable=_WtWebGraphThermoHygroAlarmHttpReqAuthEnable_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,61),_WtWebGraphThermoHygroAlarmHttpReqAuthEnable_Type())
wtWebGraphThermoHygroAlarmHttpReqAuthEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmHttpReqAuthEnable.setStatus(_A)
_WtWebGraphThermoHygroAlarmHttpReqAuthUser_Type=OctetString
_WtWebGraphThermoHygroAlarmHttpReqAuthUser_Object=MibTableColumn
wtWebGraphThermoHygroAlarmHttpReqAuthUser=_WtWebGraphThermoHygroAlarmHttpReqAuthUser_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,62),_WtWebGraphThermoHygroAlarmHttpReqAuthUser_Type())
wtWebGraphThermoHygroAlarmHttpReqAuthUser.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmHttpReqAuthUser.setStatus(_A)
_WtWebGraphThermoHygroAlarmHttpReqAuthPassword_Type=OctetString
_WtWebGraphThermoHygroAlarmHttpReqAuthPassword_Object=MibTableColumn
wtWebGraphThermoHygroAlarmHttpReqAuthPassword=_WtWebGraphThermoHygroAlarmHttpReqAuthPassword_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,63),_WtWebGraphThermoHygroAlarmHttpReqAuthPassword_Type())
wtWebGraphThermoHygroAlarmHttpReqAuthPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmHttpReqAuthPassword.setStatus(_A)
_WtWebGraphThermoHygroAlarmHttpReqSetUrl_Type=OctetString
_WtWebGraphThermoHygroAlarmHttpReqSetUrl_Object=MibTableColumn
wtWebGraphThermoHygroAlarmHttpReqSetUrl=_WtWebGraphThermoHygroAlarmHttpReqSetUrl_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,64),_WtWebGraphThermoHygroAlarmHttpReqSetUrl_Type())
wtWebGraphThermoHygroAlarmHttpReqSetUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmHttpReqSetUrl.setStatus(_A)
_WtWebGraphThermoHygroAlarmHttpReqClearUrl_Type=OctetString
_WtWebGraphThermoHygroAlarmHttpReqClearUrl_Object=MibTableColumn
wtWebGraphThermoHygroAlarmHttpReqClearUrl=_WtWebGraphThermoHygroAlarmHttpReqClearUrl_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,65),_WtWebGraphThermoHygroAlarmHttpReqClearUrl_Type())
wtWebGraphThermoHygroAlarmHttpReqClearUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmHttpReqClearUrl.setStatus(_A)
class _WtWebGraphThermoHygroAlarmHttpReqServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphThermoHygroAlarmHttpReqServerPort_Type.__name__=_E
_WtWebGraphThermoHygroAlarmHttpReqServerPort_Object=MibTableColumn
wtWebGraphThermoHygroAlarmHttpReqServerPort=_WtWebGraphThermoHygroAlarmHttpReqServerPort_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,66),_WtWebGraphThermoHygroAlarmHttpReqServerPort_Type())
wtWebGraphThermoHygroAlarmHttpReqServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmHttpReqServerPort.setStatus(_A)
_WtWebGraphThermoHygroAlarmMqttTopicPath_Type=OctetString
_WtWebGraphThermoHygroAlarmMqttTopicPath_Object=MibTableColumn
wtWebGraphThermoHygroAlarmMqttTopicPath=_WtWebGraphThermoHygroAlarmMqttTopicPath_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,67),_WtWebGraphThermoHygroAlarmMqttTopicPath_Type())
wtWebGraphThermoHygroAlarmMqttTopicPath.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmMqttTopicPath.setStatus(_A)
_WtWebGraphThermoHygroAlarmMqttTopicSetTopic_Type=OctetString
_WtWebGraphThermoHygroAlarmMqttTopicSetTopic_Object=MibTableColumn
wtWebGraphThermoHygroAlarmMqttTopicSetTopic=_WtWebGraphThermoHygroAlarmMqttTopicSetTopic_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,68),_WtWebGraphThermoHygroAlarmMqttTopicSetTopic_Type())
wtWebGraphThermoHygroAlarmMqttTopicSetTopic.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmMqttTopicSetTopic.setStatus(_A)
_WtWebGraphThermoHygroAlarmMqttTopicClear_Type=OctetString
_WtWebGraphThermoHygroAlarmMqttTopicClear_Object=MibTableColumn
wtWebGraphThermoHygroAlarmMqttTopicClear=_WtWebGraphThermoHygroAlarmMqttTopicClear_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,69),_WtWebGraphThermoHygroAlarmMqttTopicClear_Type())
wtWebGraphThermoHygroAlarmMqttTopicClear.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmMqttTopicClear.setStatus(_A)
_WtWebGraphThermoHygroAlarmSensorLostSelection_Type=OctetString
_WtWebGraphThermoHygroAlarmSensorLostSelection_Object=MibTableColumn
wtWebGraphThermoHygroAlarmSensorLostSelection=_WtWebGraphThermoHygroAlarmSensorLostSelection_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,70),_WtWebGraphThermoHygroAlarmSensorLostSelection_Type())
wtWebGraphThermoHygroAlarmSensorLostSelection.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmSensorLostSelection.setStatus(_A)
_WtWebGraphThermoHygroAlarmLimitWindow_Type=OctetString
_WtWebGraphThermoHygroAlarmLimitWindow_Object=MibTableColumn
wtWebGraphThermoHygroAlarmLimitWindow=_WtWebGraphThermoHygroAlarmLimitWindow_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,71),_WtWebGraphThermoHygroAlarmLimitWindow_Type())
wtWebGraphThermoHygroAlarmLimitWindow.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmLimitWindow.setStatus(_A)
_WtWebGraphThermoHygroAlarmSnmpManagerPort_Type=Integer32
_WtWebGraphThermoHygroAlarmSnmpManagerPort_Object=MibTableColumn
wtWebGraphThermoHygroAlarmSnmpManagerPort=_WtWebGraphThermoHygroAlarmSnmpManagerPort_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,76),_WtWebGraphThermoHygroAlarmSnmpManagerPort_Type())
wtWebGraphThermoHygroAlarmSnmpManagerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmSnmpManagerPort.setStatus(_A)
class _WtWebGraphThermoHygroAlarmMqttQoS_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoHygroAlarmMqttQoS_Type.__name__=_D
_WtWebGraphThermoHygroAlarmMqttQoS_Object=MibTableColumn
wtWebGraphThermoHygroAlarmMqttQoS=_WtWebGraphThermoHygroAlarmMqttQoS_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,77),_WtWebGraphThermoHygroAlarmMqttQoS_Type())
wtWebGraphThermoHygroAlarmMqttQoS.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmMqttQoS.setStatus(_A)
class _WtWebGraphThermoHygroAlarmMqttRetain_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoHygroAlarmMqttRetain_Type.__name__=_D
_WtWebGraphThermoHygroAlarmMqttRetain_Object=MibTableColumn
wtWebGraphThermoHygroAlarmMqttRetain=_WtWebGraphThermoHygroAlarmMqttRetain_Object((1,3,6,1,4,1,5040,1,2,42,3,1,5,3,1,78),_WtWebGraphThermoHygroAlarmMqttRetain_Type())
wtWebGraphThermoHygroAlarmMqttRetain.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlarmMqttRetain.setStatus(_A)
_WtWebGraphThermoHygroGraphics_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroGraphics=_WtWebGraphThermoHygroGraphics_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,1,6))
_WtWebGraphThermoHygroGraphicsBase_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroGraphicsBase=_WtWebGraphThermoHygroGraphicsBase_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,1,6,1))
_WtWebGraphThermoHygroGraphicsBaseEnable_Type=OctetString
_WtWebGraphThermoHygroGraphicsBaseEnable_Object=MibScalar
wtWebGraphThermoHygroGraphicsBaseEnable=_WtWebGraphThermoHygroGraphicsBaseEnable_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,1,1),_WtWebGraphThermoHygroGraphicsBaseEnable_Type())
wtWebGraphThermoHygroGraphicsBaseEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGraphicsBaseEnable.setStatus(_A)
_WtWebGraphThermoHygroGraphicsBaseWidth_Type=Integer32
_WtWebGraphThermoHygroGraphicsBaseWidth_Object=MibScalar
wtWebGraphThermoHygroGraphicsBaseWidth=_WtWebGraphThermoHygroGraphicsBaseWidth_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,1,2),_WtWebGraphThermoHygroGraphicsBaseWidth_Type())
wtWebGraphThermoHygroGraphicsBaseWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGraphicsBaseWidth.setStatus(_A)
_WtWebGraphThermoHygroGraphicsBaseHeight_Type=Integer32
_WtWebGraphThermoHygroGraphicsBaseHeight_Object=MibScalar
wtWebGraphThermoHygroGraphicsBaseHeight=_WtWebGraphThermoHygroGraphicsBaseHeight_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,1,3),_WtWebGraphThermoHygroGraphicsBaseHeight_Type())
wtWebGraphThermoHygroGraphicsBaseHeight.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGraphicsBaseHeight.setStatus(_A)
class _WtWebGraphThermoHygroGraphicsBaseFrameColor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_WtWebGraphThermoHygroGraphicsBaseFrameColor_Type.__name__=_D
_WtWebGraphThermoHygroGraphicsBaseFrameColor_Object=MibScalar
wtWebGraphThermoHygroGraphicsBaseFrameColor=_WtWebGraphThermoHygroGraphicsBaseFrameColor_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,1,4),_WtWebGraphThermoHygroGraphicsBaseFrameColor_Type())
wtWebGraphThermoHygroGraphicsBaseFrameColor.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGraphicsBaseFrameColor.setStatus(_A)
class _WtWebGraphThermoHygroGraphicsBaseBackgroundColor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_WtWebGraphThermoHygroGraphicsBaseBackgroundColor_Type.__name__=_D
_WtWebGraphThermoHygroGraphicsBaseBackgroundColor_Object=MibScalar
wtWebGraphThermoHygroGraphicsBaseBackgroundColor=_WtWebGraphThermoHygroGraphicsBaseBackgroundColor_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,1,5),_WtWebGraphThermoHygroGraphicsBaseBackgroundColor_Type())
wtWebGraphThermoHygroGraphicsBaseBackgroundColor.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGraphicsBaseBackgroundColor.setStatus(_A)
_WtWebGraphThermoHygroGraphicsBasePollingrate_Type=Integer32
_WtWebGraphThermoHygroGraphicsBasePollingrate_Object=MibScalar
wtWebGraphThermoHygroGraphicsBasePollingrate=_WtWebGraphThermoHygroGraphicsBasePollingrate_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,1,6),_WtWebGraphThermoHygroGraphicsBasePollingrate_Type())
wtWebGraphThermoHygroGraphicsBasePollingrate.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGraphicsBasePollingrate.setStatus(_A)
_WtWebGraphThermoHygroGraphicsSelect_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroGraphicsSelect=_WtWebGraphThermoHygroGraphicsSelect_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,1,6,2))
class _WtWebGraphThermoHygroGraphicsSelectDisplaySensorSel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoHygroGraphicsSelectDisplaySensorSel_Type.__name__=_D
_WtWebGraphThermoHygroGraphicsSelectDisplaySensorSel_Object=MibScalar
wtWebGraphThermoHygroGraphicsSelectDisplaySensorSel=_WtWebGraphThermoHygroGraphicsSelectDisplaySensorSel_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,2,1),_WtWebGraphThermoHygroGraphicsSelectDisplaySensorSel_Type())
wtWebGraphThermoHygroGraphicsSelectDisplaySensorSel.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGraphicsSelectDisplaySensorSel.setStatus(_A)
class _WtWebGraphThermoHygroGraphicsSelectDisplayShowExtrem_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphThermoHygroGraphicsSelectDisplayShowExtrem_Type.__name__=_D
_WtWebGraphThermoHygroGraphicsSelectDisplayShowExtrem_Object=MibScalar
wtWebGraphThermoHygroGraphicsSelectDisplayShowExtrem=_WtWebGraphThermoHygroGraphicsSelectDisplayShowExtrem_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,2,2),_WtWebGraphThermoHygroGraphicsSelectDisplayShowExtrem_Type())
wtWebGraphThermoHygroGraphicsSelectDisplayShowExtrem.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGraphicsSelectDisplayShowExtrem.setStatus(_A)
_WtWebGraphThermoHygroSensorColorTable_Object=MibTable
wtWebGraphThermoHygroSensorColorTable=_WtWebGraphThermoHygroSensorColorTable_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,2,3))
if mibBuilder.loadTexts:wtWebGraphThermoHygroSensorColorTable.setStatus(_A)
_WtWebGraphThermoHygroSensorColorEntry_Object=MibTableRow
wtWebGraphThermoHygroSensorColorEntry=_WtWebGraphThermoHygroSensorColorEntry_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,2,3,1))
wtWebGraphThermoHygroSensorColorEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:wtWebGraphThermoHygroSensorColorEntry.setStatus(_A)
class _WtWebGraphThermoHygroGraphicsSensorColor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_WtWebGraphThermoHygroGraphicsSensorColor_Type.__name__=_D
_WtWebGraphThermoHygroGraphicsSensorColor_Object=MibTableColumn
wtWebGraphThermoHygroGraphicsSensorColor=_WtWebGraphThermoHygroGraphicsSensorColor_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,2,3,1,1),_WtWebGraphThermoHygroGraphicsSensorColor_Type())
wtWebGraphThermoHygroGraphicsSensorColor.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGraphicsSensorColor.setStatus(_A)
_WtWebGraphThermoHygroGraphicsSelectScale_Type=OctetString
_WtWebGraphThermoHygroGraphicsSelectScale_Object=MibTableColumn
wtWebGraphThermoHygroGraphicsSelectScale=_WtWebGraphThermoHygroGraphicsSelectScale_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,2,3,1,2),_WtWebGraphThermoHygroGraphicsSelectScale_Type())
wtWebGraphThermoHygroGraphicsSelectScale.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGraphicsSelectScale.setStatus(_A)
_WtWebGraphThermoHygroGraphicsScale_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroGraphicsScale=_WtWebGraphThermoHygroGraphicsScale_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,1,6,3))
_WtWebGraphThermoHygroGraphicsScaleAutoScaleEnable_Type=OctetString
_WtWebGraphThermoHygroGraphicsScaleAutoScaleEnable_Object=MibScalar
wtWebGraphThermoHygroGraphicsScaleAutoScaleEnable=_WtWebGraphThermoHygroGraphicsScaleAutoScaleEnable_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,3,1),_WtWebGraphThermoHygroGraphicsScaleAutoScaleEnable_Type())
wtWebGraphThermoHygroGraphicsScaleAutoScaleEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGraphicsScaleAutoScaleEnable.setStatus(_A)
_WtWebGraphThermoHygroGraphicsScaleAutoFitEnable_Type=OctetString
_WtWebGraphThermoHygroGraphicsScaleAutoFitEnable_Object=MibScalar
wtWebGraphThermoHygroGraphicsScaleAutoFitEnable=_WtWebGraphThermoHygroGraphicsScaleAutoFitEnable_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,3,2),_WtWebGraphThermoHygroGraphicsScaleAutoFitEnable_Type())
wtWebGraphThermoHygroGraphicsScaleAutoFitEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGraphicsScaleAutoFitEnable.setStatus(_A)
_WtWebGraphThermoHygroGraphicsScale1Min_Type=Integer32
_WtWebGraphThermoHygroGraphicsScale1Min_Object=MibScalar
wtWebGraphThermoHygroGraphicsScale1Min=_WtWebGraphThermoHygroGraphicsScale1Min_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,3,3),_WtWebGraphThermoHygroGraphicsScale1Min_Type())
wtWebGraphThermoHygroGraphicsScale1Min.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGraphicsScale1Min.setStatus(_A)
_WtWebGraphThermoHygroGraphicsScale2Min_Type=Integer32
_WtWebGraphThermoHygroGraphicsScale2Min_Object=MibScalar
wtWebGraphThermoHygroGraphicsScale2Min=_WtWebGraphThermoHygroGraphicsScale2Min_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,3,4),_WtWebGraphThermoHygroGraphicsScale2Min_Type())
wtWebGraphThermoHygroGraphicsScale2Min.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGraphicsScale2Min.setStatus(_A)
_WtWebGraphThermoHygroGraphicsScale3Min_Type=Integer32
_WtWebGraphThermoHygroGraphicsScale3Min_Object=MibScalar
wtWebGraphThermoHygroGraphicsScale3Min=_WtWebGraphThermoHygroGraphicsScale3Min_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,3,5),_WtWebGraphThermoHygroGraphicsScale3Min_Type())
wtWebGraphThermoHygroGraphicsScale3Min.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGraphicsScale3Min.setStatus(_A)
_WtWebGraphThermoHygroGraphicsScale4Min_Type=Integer32
_WtWebGraphThermoHygroGraphicsScale4Min_Object=MibScalar
wtWebGraphThermoHygroGraphicsScale4Min=_WtWebGraphThermoHygroGraphicsScale4Min_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,3,6),_WtWebGraphThermoHygroGraphicsScale4Min_Type())
wtWebGraphThermoHygroGraphicsScale4Min.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGraphicsScale4Min.setStatus(_A)
_WtWebGraphThermoHygroGraphicsScale1Max_Type=Integer32
_WtWebGraphThermoHygroGraphicsScale1Max_Object=MibScalar
wtWebGraphThermoHygroGraphicsScale1Max=_WtWebGraphThermoHygroGraphicsScale1Max_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,3,7),_WtWebGraphThermoHygroGraphicsScale1Max_Type())
wtWebGraphThermoHygroGraphicsScale1Max.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGraphicsScale1Max.setStatus(_A)
_WtWebGraphThermoHygroGraphicsScale2Max_Type=Integer32
_WtWebGraphThermoHygroGraphicsScale2Max_Object=MibScalar
wtWebGraphThermoHygroGraphicsScale2Max=_WtWebGraphThermoHygroGraphicsScale2Max_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,3,8),_WtWebGraphThermoHygroGraphicsScale2Max_Type())
wtWebGraphThermoHygroGraphicsScale2Max.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGraphicsScale2Max.setStatus(_A)
_WtWebGraphThermoHygroGraphicsScale3Max_Type=Integer32
_WtWebGraphThermoHygroGraphicsScale3Max_Object=MibScalar
wtWebGraphThermoHygroGraphicsScale3Max=_WtWebGraphThermoHygroGraphicsScale3Max_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,3,9),_WtWebGraphThermoHygroGraphicsScale3Max_Type())
wtWebGraphThermoHygroGraphicsScale3Max.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGraphicsScale3Max.setStatus(_A)
_WtWebGraphThermoHygroGraphicsScale4Max_Type=Integer32
_WtWebGraphThermoHygroGraphicsScale4Max_Object=MibScalar
wtWebGraphThermoHygroGraphicsScale4Max=_WtWebGraphThermoHygroGraphicsScale4Max_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,3,10),_WtWebGraphThermoHygroGraphicsScale4Max_Type())
wtWebGraphThermoHygroGraphicsScale4Max.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGraphicsScale4Max.setStatus(_A)
_WtWebGraphThermoHygroGraphicsScale1Unit_Type=OctetString
_WtWebGraphThermoHygroGraphicsScale1Unit_Object=MibScalar
wtWebGraphThermoHygroGraphicsScale1Unit=_WtWebGraphThermoHygroGraphicsScale1Unit_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,3,11),_WtWebGraphThermoHygroGraphicsScale1Unit_Type())
wtWebGraphThermoHygroGraphicsScale1Unit.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGraphicsScale1Unit.setStatus(_A)
_WtWebGraphThermoHygroGraphicsScale2Unit_Type=OctetString
_WtWebGraphThermoHygroGraphicsScale2Unit_Object=MibScalar
wtWebGraphThermoHygroGraphicsScale2Unit=_WtWebGraphThermoHygroGraphicsScale2Unit_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,3,12),_WtWebGraphThermoHygroGraphicsScale2Unit_Type())
wtWebGraphThermoHygroGraphicsScale2Unit.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGraphicsScale2Unit.setStatus(_A)
_WtWebGraphThermoHygroGraphicsScale3Unit_Type=OctetString
_WtWebGraphThermoHygroGraphicsScale3Unit_Object=MibScalar
wtWebGraphThermoHygroGraphicsScale3Unit=_WtWebGraphThermoHygroGraphicsScale3Unit_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,3,13),_WtWebGraphThermoHygroGraphicsScale3Unit_Type())
wtWebGraphThermoHygroGraphicsScale3Unit.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGraphicsScale3Unit.setStatus(_A)
_WtWebGraphThermoHygroGraphicsScale4Unit_Type=OctetString
_WtWebGraphThermoHygroGraphicsScale4Unit_Object=MibScalar
wtWebGraphThermoHygroGraphicsScale4Unit=_WtWebGraphThermoHygroGraphicsScale4Unit_Object((1,3,6,1,4,1,5040,1,2,42,3,1,6,3,14),_WtWebGraphThermoHygroGraphicsScale4Unit_Type())
wtWebGraphThermoHygroGraphicsScale4Unit.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphThermoHygroGraphicsScale4Unit.setStatus(_A)
_WtWebGraphThermoHygroPorts_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroPorts=_WtWebGraphThermoHygroPorts_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,2))
_WtWebGraphThermoHygroPortTable_Object=MibTable
wtWebGraphThermoHygroPortTable=_WtWebGraphThermoHygroPortTable_Object((1,3,6,1,4,1,5040,1,2,42,3,2,1))
if mibBuilder.loadTexts:wtWebGraphThermoHygroPortTable.setStatus(_A)
_WtWebGraphThermoHygroPortEntry_Object=MibTableRow
wtWebGraphThermoHygroPortEntry=_WtWebGraphThermoHygroPortEntry_Object((1,3,6,1,4,1,5040,1,2,42,3,2,1,1))
wtWebGraphThermoHygroPortEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:wtWebGraphThermoHygroPortEntry.setStatus(_A)
_WtWebGraphThermoHygroPortName_Type=OctetString
_WtWebGraphThermoHygroPortName_Object=MibTableColumn
wtWebGraphThermoHygroPortName=_WtWebGraphThermoHygroPortName_Object((1,3,6,1,4,1,5040,1,2,42,3,2,1,1,1),_WtWebGraphThermoHygroPortName_Type())
wtWebGraphThermoHygroPortName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroPortName.setStatus(_A)
_WtWebGraphThermoHygroPortText_Type=OctetString
_WtWebGraphThermoHygroPortText_Object=MibTableColumn
wtWebGraphThermoHygroPortText=_WtWebGraphThermoHygroPortText_Object((1,3,6,1,4,1,5040,1,2,42,3,2,1,1,2),_WtWebGraphThermoHygroPortText_Type())
wtWebGraphThermoHygroPortText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroPortText.setStatus(_A)
_WtWebGraphThermoHygroPortOffset1_Type=OctetString
_WtWebGraphThermoHygroPortOffset1_Object=MibTableColumn
wtWebGraphThermoHygroPortOffset1=_WtWebGraphThermoHygroPortOffset1_Object((1,3,6,1,4,1,5040,1,2,42,3,2,1,1,3),_WtWebGraphThermoHygroPortOffset1_Type())
wtWebGraphThermoHygroPortOffset1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroPortOffset1.setStatus(_A)
_WtWebGraphThermoHygroPortTemperature1_Type=OctetString
_WtWebGraphThermoHygroPortTemperature1_Object=MibTableColumn
wtWebGraphThermoHygroPortTemperature1=_WtWebGraphThermoHygroPortTemperature1_Object((1,3,6,1,4,1,5040,1,2,42,3,2,1,1,4),_WtWebGraphThermoHygroPortTemperature1_Type())
wtWebGraphThermoHygroPortTemperature1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroPortTemperature1.setStatus(_A)
_WtWebGraphThermoHygroPortOffset2_Type=OctetString
_WtWebGraphThermoHygroPortOffset2_Object=MibTableColumn
wtWebGraphThermoHygroPortOffset2=_WtWebGraphThermoHygroPortOffset2_Object((1,3,6,1,4,1,5040,1,2,42,3,2,1,1,5),_WtWebGraphThermoHygroPortOffset2_Type())
wtWebGraphThermoHygroPortOffset2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroPortOffset2.setStatus(_A)
_WtWebGraphThermoHygroPortTemperature2_Type=OctetString
_WtWebGraphThermoHygroPortTemperature2_Object=MibTableColumn
wtWebGraphThermoHygroPortTemperature2=_WtWebGraphThermoHygroPortTemperature2_Object((1,3,6,1,4,1,5040,1,2,42,3,2,1,1,6),_WtWebGraphThermoHygroPortTemperature2_Type())
wtWebGraphThermoHygroPortTemperature2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroPortTemperature2.setStatus(_A)
_WtWebGraphThermoHygroPortComment_Type=OctetString
_WtWebGraphThermoHygroPortComment_Object=MibTableColumn
wtWebGraphThermoHygroPortComment=_WtWebGraphThermoHygroPortComment_Object((1,3,6,1,4,1,5040,1,2,42,3,2,1,1,7),_WtWebGraphThermoHygroPortComment_Type())
wtWebGraphThermoHygroPortComment.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroPortComment.setStatus(_A)
_WtWebGraphThermoHygroPortAltidude_Type=OctetString
_WtWebGraphThermoHygroPortAltidude_Object=MibScalar
wtWebGraphThermoHygroPortAltidude=_WtWebGraphThermoHygroPortAltidude_Object((1,3,6,1,4,1,5040,1,2,42,3,2,2),_WtWebGraphThermoHygroPortAltidude_Type())
wtWebGraphThermoHygroPortAltidude.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroPortAltidude.setStatus(_A)
_WtWebGraphThermoHygroManufact_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroManufact=_WtWebGraphThermoHygroManufact_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,3,3))
_WtWebGraphThermoHygroMfName_Type=OctetString
_WtWebGraphThermoHygroMfName_Object=MibScalar
wtWebGraphThermoHygroMfName=_WtWebGraphThermoHygroMfName_Object((1,3,6,1,4,1,5040,1,2,42,3,3,1),_WtWebGraphThermoHygroMfName_Type())
wtWebGraphThermoHygroMfName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMfName.setStatus(_A)
_WtWebGraphThermoHygroMfAddr_Type=OctetString
_WtWebGraphThermoHygroMfAddr_Object=MibScalar
wtWebGraphThermoHygroMfAddr=_WtWebGraphThermoHygroMfAddr_Object((1,3,6,1,4,1,5040,1,2,42,3,3,2),_WtWebGraphThermoHygroMfAddr_Type())
wtWebGraphThermoHygroMfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMfAddr.setStatus(_A)
_WtWebGraphThermoHygroMfHotline_Type=OctetString
_WtWebGraphThermoHygroMfHotline_Object=MibScalar
wtWebGraphThermoHygroMfHotline=_WtWebGraphThermoHygroMfHotline_Object((1,3,6,1,4,1,5040,1,2,42,3,3,3),_WtWebGraphThermoHygroMfHotline_Type())
wtWebGraphThermoHygroMfHotline.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMfHotline.setStatus(_A)
_WtWebGraphThermoHygroMfInternet_Type=OctetString
_WtWebGraphThermoHygroMfInternet_Object=MibScalar
wtWebGraphThermoHygroMfInternet=_WtWebGraphThermoHygroMfInternet_Object((1,3,6,1,4,1,5040,1,2,42,3,3,4),_WtWebGraphThermoHygroMfInternet_Type())
wtWebGraphThermoHygroMfInternet.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMfInternet.setStatus(_A)
_WtWebGraphThermoHygroMfDeviceTyp_Type=OctetString
_WtWebGraphThermoHygroMfDeviceTyp_Object=MibScalar
wtWebGraphThermoHygroMfDeviceTyp=_WtWebGraphThermoHygroMfDeviceTyp_Object((1,3,6,1,4,1,5040,1,2,42,3,3,5),_WtWebGraphThermoHygroMfDeviceTyp_Type())
wtWebGraphThermoHygroMfDeviceTyp.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMfDeviceTyp.setStatus(_A)
_WtWebGraphThermoHygroMfOrderNo_Type=OctetString
_WtWebGraphThermoHygroMfOrderNo_Object=MibScalar
wtWebGraphThermoHygroMfOrderNo=_WtWebGraphThermoHygroMfOrderNo_Object((1,3,6,1,4,1,5040,1,2,42,3,3,6),_WtWebGraphThermoHygroMfOrderNo_Type())
wtWebGraphThermoHygroMfOrderNo.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroMfOrderNo.setStatus(_A)
_WtWebGraphThermoHygroDiag_ObjectIdentity=ObjectIdentity
wtWebGraphThermoHygroDiag=_WtWebGraphThermoHygroDiag_ObjectIdentity((1,3,6,1,4,1,5040,1,2,42,4))
_WtWebGraphThermoHygroDiagErrorCount_Type=Integer32
_WtWebGraphThermoHygroDiagErrorCount_Object=MibScalar
wtWebGraphThermoHygroDiagErrorCount=_WtWebGraphThermoHygroDiagErrorCount_Object((1,3,6,1,4,1,5040,1,2,42,4,1),_WtWebGraphThermoHygroDiagErrorCount_Type())
wtWebGraphThermoHygroDiagErrorCount.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphThermoHygroDiagErrorCount.setStatus(_A)
_WtWebGraphThermoHygroDiagBinaryError_Type=OctetString
_WtWebGraphThermoHygroDiagBinaryError_Object=MibScalar
wtWebGraphThermoHygroDiagBinaryError=_WtWebGraphThermoHygroDiagBinaryError_Object((1,3,6,1,4,1,5040,1,2,42,4,2),_WtWebGraphThermoHygroDiagBinaryError_Type())
wtWebGraphThermoHygroDiagBinaryError.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphThermoHygroDiagBinaryError.setStatus(_A)
_WtWebGraphThermoHygroDiagErrorIndex_Type=Integer32
_WtWebGraphThermoHygroDiagErrorIndex_Object=MibScalar
wtWebGraphThermoHygroDiagErrorIndex=_WtWebGraphThermoHygroDiagErrorIndex_Object((1,3,6,1,4,1,5040,1,2,42,4,3),_WtWebGraphThermoHygroDiagErrorIndex_Type())
wtWebGraphThermoHygroDiagErrorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphThermoHygroDiagErrorIndex.setStatus(_A)
_WtWebGraphThermoHygroDiagErrorMessage_Type=OctetString
_WtWebGraphThermoHygroDiagErrorMessage_Object=MibScalar
wtWebGraphThermoHygroDiagErrorMessage=_WtWebGraphThermoHygroDiagErrorMessage_Object((1,3,6,1,4,1,5040,1,2,42,4,4),_WtWebGraphThermoHygroDiagErrorMessage_Type())
wtWebGraphThermoHygroDiagErrorMessage.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphThermoHygroDiagErrorMessage.setStatus(_A)
_WtWebGraphThermoHygroDiagErrorClear_Type=Integer32
_WtWebGraphThermoHygroDiagErrorClear_Object=MibScalar
wtWebGraphThermoHygroDiagErrorClear=_WtWebGraphThermoHygroDiagErrorClear_Object((1,3,6,1,4,1,5040,1,2,42,4,5),_WtWebGraphThermoHygroDiagErrorClear_Type())
wtWebGraphThermoHygroDiagErrorClear.setMaxAccess('write-only')
if mibBuilder.loadTexts:wtWebGraphThermoHygroDiagErrorClear.setStatus(_A)
wtWebGraphThermoHygroAlert1=NotificationType((1,3,6,1,4,1,5040,1,2,42,0,31))
wtWebGraphThermoHygroAlert1.setObjects((_C,_G))
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlert1.setStatus('')
wtWebGraphThermoHygroAlert2=NotificationType((1,3,6,1,4,1,5040,1,2,42,0,32))
wtWebGraphThermoHygroAlert2.setObjects((_C,_G))
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlert2.setStatus('')
wtWebGraphThermoHygroAlert3=NotificationType((1,3,6,1,4,1,5040,1,2,42,0,33))
wtWebGraphThermoHygroAlert3.setObjects((_C,_G))
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlert3.setStatus('')
wtWebGraphThermoHygroAlert4=NotificationType((1,3,6,1,4,1,5040,1,2,42,0,34))
wtWebGraphThermoHygroAlert4.setObjects((_C,_G))
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlert4.setStatus('')
wtWebGraphThermoHygroAlert5=NotificationType((1,3,6,1,4,1,5040,1,2,42,0,35))
wtWebGraphThermoHygroAlert5.setObjects((_C,_G))
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlert5.setStatus('')
wtWebGraphThermoHygroAlert6=NotificationType((1,3,6,1,4,1,5040,1,2,42,0,36))
wtWebGraphThermoHygroAlert6.setObjects((_C,_G))
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlert6.setStatus('')
wtWebGraphThermoHygroAlert7=NotificationType((1,3,6,1,4,1,5040,1,2,42,0,37))
wtWebGraphThermoHygroAlert7.setObjects((_C,_G))
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlert7.setStatus('')
wtWebGraphThermoHygroAlert8=NotificationType((1,3,6,1,4,1,5040,1,2,42,0,38))
wtWebGraphThermoHygroAlert8.setObjects((_C,_G))
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlert8.setStatus('')
wtWebGraphThermoHygroAlert9=NotificationType((1,3,6,1,4,1,5040,1,2,42,0,91))
wtWebGraphThermoHygroAlert9.setObjects((_C,_H))
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlert9.setStatus('')
wtWebGraphThermoHygroAlert10=NotificationType((1,3,6,1,4,1,5040,1,2,42,0,92))
wtWebGraphThermoHygroAlert10.setObjects((_C,_H))
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlert10.setStatus('')
wtWebGraphThermoHygroAlert11=NotificationType((1,3,6,1,4,1,5040,1,2,42,0,93))
wtWebGraphThermoHygroAlert11.setObjects((_C,_H))
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlert11.setStatus('')
wtWebGraphThermoHygroAlert12=NotificationType((1,3,6,1,4,1,5040,1,2,42,0,94))
wtWebGraphThermoHygroAlert12.setObjects((_C,_H))
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlert12.setStatus('')
wtWebGraphThermoHygroAlert13=NotificationType((1,3,6,1,4,1,5040,1,2,42,0,95))
wtWebGraphThermoHygroAlert13.setObjects((_C,_H))
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlert13.setStatus('')
wtWebGraphThermoHygroAlert14=NotificationType((1,3,6,1,4,1,5040,1,2,42,0,96))
wtWebGraphThermoHygroAlert14.setObjects((_C,_H))
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlert14.setStatus('')
wtWebGraphThermoHygroAlert15=NotificationType((1,3,6,1,4,1,5040,1,2,42,0,97))
wtWebGraphThermoHygroAlert15.setObjects((_C,_H))
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlert15.setStatus('')
wtWebGraphThermoHygroAlert16=NotificationType((1,3,6,1,4,1,5040,1,2,42,0,98))
wtWebGraphThermoHygroAlert16.setObjects((_C,_H))
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlert16.setStatus('')
wtWebGraphThermoHygroAlertDiag=NotificationType((1,3,6,1,4,1,5040,1,2,42,0,110))
wtWebGraphThermoHygroAlertDiag.setObjects(*((_C,_L),(_C,_M)))
if mibBuilder.loadTexts:wtWebGraphThermoHygroAlertDiag.setStatus('')
mibBuilder.exportSymbols(_C,**{'wut':wut,'wtComServer':wtComServer,'wtWebio':wtWebio,'wtWebGraphThermoHygro':wtWebGraphThermoHygro,'wtWebGraphThermoHygroAlert1':wtWebGraphThermoHygroAlert1,'wtWebGraphThermoHygroAlert2':wtWebGraphThermoHygroAlert2,'wtWebGraphThermoHygroAlert3':wtWebGraphThermoHygroAlert3,'wtWebGraphThermoHygroAlert4':wtWebGraphThermoHygroAlert4,'wtWebGraphThermoHygroAlert5':wtWebGraphThermoHygroAlert5,'wtWebGraphThermoHygroAlert6':wtWebGraphThermoHygroAlert6,'wtWebGraphThermoHygroAlert7':wtWebGraphThermoHygroAlert7,'wtWebGraphThermoHygroAlert8':wtWebGraphThermoHygroAlert8,'wtWebGraphThermoHygroAlert9':wtWebGraphThermoHygroAlert9,'wtWebGraphThermoHygroAlert10':wtWebGraphThermoHygroAlert10,'wtWebGraphThermoHygroAlert11':wtWebGraphThermoHygroAlert11,'wtWebGraphThermoHygroAlert12':wtWebGraphThermoHygroAlert12,'wtWebGraphThermoHygroAlert13':wtWebGraphThermoHygroAlert13,'wtWebGraphThermoHygroAlert14':wtWebGraphThermoHygroAlert14,'wtWebGraphThermoHygroAlert15':wtWebGraphThermoHygroAlert15,'wtWebGraphThermoHygroAlert16':wtWebGraphThermoHygroAlert16,'wtWebGraphThermoHygroAlertDiag':wtWebGraphThermoHygroAlertDiag,'wtWebGraphThermoHygroTemp':wtWebGraphThermoHygroTemp,'wtWebGraphThermoHygroSensors':wtWebGraphThermoHygroSensors,'wtWebGraphThermoHygroSensorTable':wtWebGraphThermoHygroSensorTable,'wtWebGraphThermoHygroSensorEntry':wtWebGraphThermoHygroSensorEntry,_I:wtWebGraphThermoHygroSensorNo,'wtWebGraphThermoHygroTempValueTable':wtWebGraphThermoHygroTempValueTable,'wtWebGraphThermoHygroTempValueEntry':wtWebGraphThermoHygroTempValueEntry,'wtWebGraphThermoHygroTempValue':wtWebGraphThermoHygroTempValue,'wtWebGraphThermoHygroBinaryTempValueTable':wtWebGraphThermoHygroBinaryTempValueTable,'wtWebGraphThermoHygroBinaryTempValueEntry':wtWebGraphThermoHygroBinaryTempValueEntry,'wtWebGraphThermoHygroBinaryTempValue':wtWebGraphThermoHygroBinaryTempValue,'wtWebGraphThermoHygroTempValuePktTable':wtWebGraphThermoHygroTempValuePktTable,'wtWebGraphThermoHygroTempValuePktEntry':wtWebGraphThermoHygroTempValuePktEntry,'wtWebGraphThermoHygroTempValuePkt':wtWebGraphThermoHygroTempValuePkt,'wtWebGraphThermoHygroSessCntrl':wtWebGraphThermoHygroSessCntrl,'wtWebGraphThermoHygroSessCntrlPassword':wtWebGraphThermoHygroSessCntrlPassword,'wtWebGraphThermoHygroSessCntrlConfigMode':wtWebGraphThermoHygroSessCntrlConfigMode,'wtWebGraphThermoHygroSessCntrlLogout':wtWebGraphThermoHygroSessCntrlLogout,'wtWebGraphThermoHygroSessCntrlAdminPassword':wtWebGraphThermoHygroSessCntrlAdminPassword,'wtWebGraphThermoHygroSessCntrlConfigPassword':wtWebGraphThermoHygroSessCntrlConfigPassword,'wtWebGraphThermoHygroConfig':wtWebGraphThermoHygroConfig,'wtWebGraphThermoHygroDevice':wtWebGraphThermoHygroDevice,'wtWebGraphThermoHygroText':wtWebGraphThermoHygroText,'wtWebGraphThermoHygroDeviceName':wtWebGraphThermoHygroDeviceName,'wtWebGraphThermoHygroDeviceText':wtWebGraphThermoHygroDeviceText,'wtWebGraphThermoHygroDeviceLocation':wtWebGraphThermoHygroDeviceLocation,'wtWebGraphThermoHygroDeviceContact':wtWebGraphThermoHygroDeviceContact,'wtWebGraphThermoHygroTimeDate':wtWebGraphThermoHygroTimeDate,'wtWebGraphThermoHygroTimeZone':wtWebGraphThermoHygroTimeZone,'wtWebGraphThermoHygroTzOffsetHrs':wtWebGraphThermoHygroTzOffsetHrs,'wtWebGraphThermoHygroTzOffsetMin':wtWebGraphThermoHygroTzOffsetMin,'wtWebGraphThermoHygroTzEnable':wtWebGraphThermoHygroTzEnable,'wtWebGraphThermoHygroStTzOffsetHrs':wtWebGraphThermoHygroStTzOffsetHrs,'wtWebGraphThermoHygroStTzOffsetMin':wtWebGraphThermoHygroStTzOffsetMin,'wtWebGraphThermoHygroStTzEnable':wtWebGraphThermoHygroStTzEnable,'wtWebGraphThermoHygroStTzStartMonth':wtWebGraphThermoHygroStTzStartMonth,'wtWebGraphThermoHygroStTzStartMode':wtWebGraphThermoHygroStTzStartMode,'wtWebGraphThermoHygroStTzStartWday':wtWebGraphThermoHygroStTzStartWday,'wtWebGraphThermoHygroStTzStartHrs':wtWebGraphThermoHygroStTzStartHrs,'wtWebGraphThermoHygroStTzStartMin':wtWebGraphThermoHygroStTzStartMin,'wtWebGraphThermoHygroStTzStopMonth':wtWebGraphThermoHygroStTzStopMonth,'wtWebGraphThermoHygroStTzStopMode':wtWebGraphThermoHygroStTzStopMode,'wtWebGraphThermoHygroStTzStopWday':wtWebGraphThermoHygroStTzStopWday,'wtWebGraphThermoHygroStTzStopHrs':wtWebGraphThermoHygroStTzStopHrs,'wtWebGraphThermoHygroStTzStopMin':wtWebGraphThermoHygroStTzStopMin,'wtWebGraphThermoHygroTimeServer':wtWebGraphThermoHygroTimeServer,'wtWebGraphThermoHygroTimeServer1':wtWebGraphThermoHygroTimeServer1,'wtWebGraphThermoHygroTimeServer2':wtWebGraphThermoHygroTimeServer2,'wtWebGraphThermoHygroTsEnable':wtWebGraphThermoHygroTsEnable,'wtWebGraphThermoHygroTsSyncTime':wtWebGraphThermoHygroTsSyncTime,'wtWebGraphThermoHygroDeviceClock':wtWebGraphThermoHygroDeviceClock,'wtWebGraphThermoHygroClockHrs':wtWebGraphThermoHygroClockHrs,'wtWebGraphThermoHygroClockMin':wtWebGraphThermoHygroClockMin,'wtWebGraphThermoHygroClockDay':wtWebGraphThermoHygroClockDay,'wtWebGraphThermoHygroClockMonth':wtWebGraphThermoHygroClockMonth,'wtWebGraphThermoHygroClockYear':wtWebGraphThermoHygroClockYear,'wtWebGraphThermoHygroBasic':wtWebGraphThermoHygroBasic,'wtWebGraphThermoHygroNetwork':wtWebGraphThermoHygroNetwork,'wtWebGraphThermoHygroIpAddress':wtWebGraphThermoHygroIpAddress,'wtWebGraphThermoHygroSubnetMask':wtWebGraphThermoHygroSubnetMask,'wtWebGraphThermoHygroGateway':wtWebGraphThermoHygroGateway,'wtWebGraphThermoHygroDnsServer1':wtWebGraphThermoHygroDnsServer1,'wtWebGraphThermoHygroDnsServer2':wtWebGraphThermoHygroDnsServer2,'wtWebGraphThermoHygroAddConfig':wtWebGraphThermoHygroAddConfig,'wtWebGraphThermoHygroHTTP':wtWebGraphThermoHygroHTTP,'wtWebGraphThermoHygroStartup':wtWebGraphThermoHygroStartup,'wtWebGraphThermoHygroGetHeaderEnable':wtWebGraphThermoHygroGetHeaderEnable,'wtWebGraphThermoHygroHttpPort':wtWebGraphThermoHygroHttpPort,'wtWebGraphThermoHygroMail':wtWebGraphThermoHygroMail,'wtWebGraphThermoHygroMailAdName':wtWebGraphThermoHygroMailAdName,'wtWebGraphThermoHygroMailReply':wtWebGraphThermoHygroMailReply,'wtWebGraphThermoHygroMailServer':wtWebGraphThermoHygroMailServer,'wtWebioAn1MailEnable':wtWebioAn1MailEnable,'wtWebGraphThermoHygroMailAuthentication':wtWebGraphThermoHygroMailAuthentication,'wtWebGraphThermoHygroMailAuthUser':wtWebGraphThermoHygroMailAuthUser,'wtWebGraphThermoHygroMailAuthPassword':wtWebGraphThermoHygroMailAuthPassword,'wtWebGraphThermoHygroMailPop3Server':wtWebGraphThermoHygroMailPop3Server,'wtWebGraphThermoHygroSNMP':wtWebGraphThermoHygroSNMP,'wtWebGraphThermoHygroSnmpCommunityStringRead':wtWebGraphThermoHygroSnmpCommunityStringRead,'wtWebGraphThermoHygroSnmpCommunityStringReadWrite':wtWebGraphThermoHygroSnmpCommunityStringReadWrite,'wtWebGraphThermoHygroSystemTrapManagerIP':wtWebGraphThermoHygroSystemTrapManagerIP,'wtWebGraphThermoHygroSystemTrapEnable':wtWebGraphThermoHygroSystemTrapEnable,'wtWebGraphThermoHygroSnmpEnable':wtWebGraphThermoHygroSnmpEnable,'wtWebGraphThermoHygroSnmpCommunityStringTrap':wtWebGraphThermoHygroSnmpCommunityStringTrap,'wtWebGraphThermoHygroSnmpSystemTrapManagerPort':wtWebGraphThermoHygroSnmpSystemTrapManagerPort,'wtWebGraphThermoHygroUDP':wtWebGraphThermoHygroUDP,'wtWebGraphThermoHygroUdpPort':wtWebGraphThermoHygroUdpPort,'wtWebGraphThermoHygroUdpEnable':wtWebGraphThermoHygroUdpEnable,'wtWebGraphThermoHygroSyslog':wtWebGraphThermoHygroSyslog,'wtWebGraphThermoHygroSyslogServerIP':wtWebGraphThermoHygroSyslogServerIP,'wtWebGraphThermoHygroSyslogServerPort':wtWebGraphThermoHygroSyslogServerPort,'wtWebGraphThermoHygroSyslogSystemMessagesEnable':wtWebGraphThermoHygroSyslogSystemMessagesEnable,'wtWebGraphThermoHygroSyslogEnable':wtWebGraphThermoHygroSyslogEnable,'wtWebGraphThermoHygroFTP':wtWebGraphThermoHygroFTP,'wtWebGraphThermoHygroFTPServerIP':wtWebGraphThermoHygroFTPServerIP,'wtWebGraphThermoHygroFTPServerControlPort':wtWebGraphThermoHygroFTPServerControlPort,'wtWebGraphThermoHygroFTPUserName':wtWebGraphThermoHygroFTPUserName,'wtWebGraphThermoHygroFTPPassword':wtWebGraphThermoHygroFTPPassword,'wtWebGraphThermoHygroFTPAccount':wtWebGraphThermoHygroFTPAccount,'wtWebGraphThermoHygroFTPOption':wtWebGraphThermoHygroFTPOption,'wtWebGraphThermoHygroFTPEnable':wtWebGraphThermoHygroFTPEnable,'wtWebGraphThermoHygroRSS':wtWebGraphThermoHygroRSS,'wtWebGraphThermoHygroRSSChannelTitle':wtWebGraphThermoHygroRSSChannelTitle,'wtWebGraphThermoHygroRSSChannelLink':wtWebGraphThermoHygroRSSChannelLink,'wtWebGraphThermoHygroRSSChannelDescription':wtWebGraphThermoHygroRSSChannelDescription,'wtWebGraphThermoHygroRSSChannelImage':wtWebGraphThermoHygroRSSChannelImage,'wtWebGraphThermoHygroRSSChannelImageTitle':wtWebGraphThermoHygroRSSChannelImageTitle,'wtWebGraphThermoHygroRSSChannelImageLink':wtWebGraphThermoHygroRSSChannelImageLink,'wtWebGraphThermoHygroRSSChannelItemTitle':wtWebGraphThermoHygroRSSChannelItemTitle,'wtWebGraphThermoHygroRSSChannelItemLink':wtWebGraphThermoHygroRSSChannelItemLink,'wtWebGraphThermoHygroRSSChannelItemDescription':wtWebGraphThermoHygroRSSChannelItemDescription,'wtWebGraphThermoHygroRSSChannelItemQuantity':wtWebGraphThermoHygroRSSChannelItemQuantity,'wtWebGraphThermoHygroLanguage':wtWebGraphThermoHygroLanguage,'wtWebGraphThermoHygroLanguageSelect':wtWebGraphThermoHygroLanguageSelect,'wtWebGraphThermoHygroMQTT':wtWebGraphThermoHygroMQTT,'wtWebGraphThermoHygroMQTTEnable':wtWebGraphThermoHygroMQTTEnable,'wtWebGraphThermoHygroMQTTBrockerIP':wtWebGraphThermoHygroMQTTBrockerIP,'wtWebGraphThermoHygroMQTTUserName':wtWebGraphThermoHygroMQTTUserName,'wtWebGraphThermoHygroMQTTPassword':wtWebGraphThermoHygroMQTTPassword,'wtWebGraphThermoHygroMQTTLocalPort':wtWebGraphThermoHygroMQTTLocalPort,'wtWebGraphThermoHygroMQTTBrokerServerPort':wtWebGraphThermoHygroMQTTBrokerServerPort,'wtWebGraphThermoHygroMQTTInterval':wtWebGraphThermoHygroMQTTInterval,'wtWebGraphThermoHygroMQTTLastWillEnable':wtWebGraphThermoHygroMQTTLastWillEnable,'wtWebGraphThermoHygroMQTTLastWillTopic':wtWebGraphThermoHygroMQTTLastWillTopic,'wtWebGraphThermoHygroMQTTLastWillMsg':wtWebGraphThermoHygroMQTTLastWillMsg,'wtWebGraphThermoHygroMQTTLastWillQoS':wtWebGraphThermoHygroMQTTLastWillQoS,'wtWebGraphThermoHygroMQTTLastWillRetain':wtWebGraphThermoHygroMQTTLastWillRetain,'wtWebGraphThermoHygroMQTTLastWillConnectEnable':wtWebGraphThermoHygroMQTTLastWillConnectEnable,'wtWebGraphThermoHygroMQTTLastWillConnectMsg':wtWebGraphThermoHygroMQTTLastWillConnectMsg,'wtWebGraphThermoHygroREST':wtWebGraphThermoHygroREST,'wtWebGraphThermoHygroRESTEnable':wtWebGraphThermoHygroRESTEnable,'wtWebGraphThermoHygroRESTDigestAuthEnable':wtWebGraphThermoHygroRESTDigestAuthEnable,'wtWebGraphThermoHygroDatalogger':wtWebGraphThermoHygroDatalogger,'wtWebGraphThermoHygroLoggerTimebase':wtWebGraphThermoHygroLoggerTimebase,'wtWebGraphThermoHygroLoggerSensorSel':wtWebGraphThermoHygroLoggerSensorSel,'wtWebGraphThermoHygroAlarm':wtWebGraphThermoHygroAlarm,'wtWebGraphThermoHygroAlarmCount':wtWebGraphThermoHygroAlarmCount,'wtWebGraphThermoHygroAlarmIfTable':wtWebGraphThermoHygroAlarmIfTable,'wtWebGraphThermoHygroAlarmIfEntry':wtWebGraphThermoHygroAlarmIfEntry,_J:wtWebGraphThermoHygroAlarmNo,'wtWebGraphThermoHygroAlarmTable':wtWebGraphThermoHygroAlarmTable,'wtWebGraphThermoHygroAlarmEntry':wtWebGraphThermoHygroAlarmEntry,'wtWebGraphThermoHygroAlarmTrigger':wtWebGraphThermoHygroAlarmTrigger,'wtWebGraphThermoHygroAlarmMin':wtWebGraphThermoHygroAlarmMin,'wtWebGraphThermoHygroAlarmMax':wtWebGraphThermoHygroAlarmMax,'wtWebGraphThermoHygroAlarmHysteresis':wtWebGraphThermoHygroAlarmHysteresis,'wtWebGraphThermoHygroAlarmDelay':wtWebGraphThermoHygroAlarmDelay,'wtWebGraphThermoHygroAlarmInterval':wtWebGraphThermoHygroAlarmInterval,'wtWebGraphThermoHygroAlarmEnable':wtWebGraphThermoHygroAlarmEnable,'wtWebGraphThermoHygroAlarmEMailAddr':wtWebGraphThermoHygroAlarmEMailAddr,'wtWebGraphThermoHygroAlarmMailSubject':wtWebGraphThermoHygroAlarmMailSubject,'wtWebGraphThermoHygroAlarmMailText':wtWebGraphThermoHygroAlarmMailText,'wtWebGraphThermoHygroAlarmManagerIP':wtWebGraphThermoHygroAlarmManagerIP,_G:wtWebGraphThermoHygroAlarmTrapText,'wtWebGraphThermoHygroAlarmMailOptions':wtWebGraphThermoHygroAlarmMailOptions,'wtWebGraphThermoHygroAlarmTcpIpAddr':wtWebGraphThermoHygroAlarmTcpIpAddr,'wtWebGraphThermoHygroAlarmTcpPort':wtWebGraphThermoHygroAlarmTcpPort,'wtWebGraphThermoHygroAlarmTcpText':wtWebGraphThermoHygroAlarmTcpText,'wtWebGraphThermoHygroAlarmClearMailSubject':wtWebGraphThermoHygroAlarmClearMailSubject,'wtWebGraphThermoHygroAlarmClearMailText':wtWebGraphThermoHygroAlarmClearMailText,_H:wtWebGraphThermoHygroAlarmClearTrapText,'wtWebGraphThermoHygroAlarmClearTcpText':wtWebGraphThermoHygroAlarmClearTcpText,'wtWebGraphThermoHygroAlarmDeltaTemp':wtWebGraphThermoHygroAlarmDeltaTemp,'wtWebGraphThermoHygroAlarmRHMin':wtWebGraphThermoHygroAlarmRHMin,'wtWebGraphThermoHygroAlarmRHMax':wtWebGraphThermoHygroAlarmRHMax,'wtWebGraphThermoHygroAlarmRHHysteresis':wtWebGraphThermoHygroAlarmRHHysteresis,'wtWebGraphThermoHygroAlarmAHMin':wtWebGraphThermoHygroAlarmAHMin,'wtWebGraphThermoHygroAlarmAHMax':wtWebGraphThermoHygroAlarmAHMax,'wtWebGraphThermoHygroAlarmSyslogIpAddr':wtWebGraphThermoHygroAlarmSyslogIpAddr,'wtWebGraphThermoHygroAlarmSyslogPort':wtWebGraphThermoHygroAlarmSyslogPort,'wtWebGraphThermoHygroAlarmSyslogText':wtWebGraphThermoHygroAlarmSyslogText,'wtWebGraphThermoHygroAlarmSyslogClearText':wtWebGraphThermoHygroAlarmSyslogClearText,'wtWebGraphThermoHygroAlarmFtpDataPort':wtWebGraphThermoHygroAlarmFtpDataPort,'wtWebGraphThermoHygroAlarmFtpFileName':wtWebGraphThermoHygroAlarmFtpFileName,'wtWebGraphThermoHygroAlarmFtpText':wtWebGraphThermoHygroAlarmFtpText,'wtWebGraphThermoHygroAlarmFtpClearText':wtWebGraphThermoHygroAlarmFtpClearText,'wtWebGraphThermoHygroAlarmFtpOption':wtWebGraphThermoHygroAlarmFtpOption,'wtWebGraphThermoHygroAlarmTimerCron':wtWebGraphThermoHygroAlarmTimerCron,'wtWebGraphThermoHygroAlarmName':wtWebGraphThermoHygroAlarmName,'wtWebGraphThermoHygroAlarmActive':wtWebGraphThermoHygroAlarmActive,'wtWebGraphThermoHygroAlarmHttpReqAuthEnable':wtWebGraphThermoHygroAlarmHttpReqAuthEnable,'wtWebGraphThermoHygroAlarmHttpReqAuthUser':wtWebGraphThermoHygroAlarmHttpReqAuthUser,'wtWebGraphThermoHygroAlarmHttpReqAuthPassword':wtWebGraphThermoHygroAlarmHttpReqAuthPassword,'wtWebGraphThermoHygroAlarmHttpReqSetUrl':wtWebGraphThermoHygroAlarmHttpReqSetUrl,'wtWebGraphThermoHygroAlarmHttpReqClearUrl':wtWebGraphThermoHygroAlarmHttpReqClearUrl,'wtWebGraphThermoHygroAlarmHttpReqServerPort':wtWebGraphThermoHygroAlarmHttpReqServerPort,'wtWebGraphThermoHygroAlarmMqttTopicPath':wtWebGraphThermoHygroAlarmMqttTopicPath,'wtWebGraphThermoHygroAlarmMqttTopicSetTopic':wtWebGraphThermoHygroAlarmMqttTopicSetTopic,'wtWebGraphThermoHygroAlarmMqttTopicClear':wtWebGraphThermoHygroAlarmMqttTopicClear,'wtWebGraphThermoHygroAlarmSensorLostSelection':wtWebGraphThermoHygroAlarmSensorLostSelection,'wtWebGraphThermoHygroAlarmLimitWindow':wtWebGraphThermoHygroAlarmLimitWindow,'wtWebGraphThermoHygroAlarmSnmpManagerPort':wtWebGraphThermoHygroAlarmSnmpManagerPort,'wtWebGraphThermoHygroAlarmMqttQoS':wtWebGraphThermoHygroAlarmMqttQoS,'wtWebGraphThermoHygroAlarmMqttRetain':wtWebGraphThermoHygroAlarmMqttRetain,'wtWebGraphThermoHygroGraphics':wtWebGraphThermoHygroGraphics,'wtWebGraphThermoHygroGraphicsBase':wtWebGraphThermoHygroGraphicsBase,'wtWebGraphThermoHygroGraphicsBaseEnable':wtWebGraphThermoHygroGraphicsBaseEnable,'wtWebGraphThermoHygroGraphicsBaseWidth':wtWebGraphThermoHygroGraphicsBaseWidth,'wtWebGraphThermoHygroGraphicsBaseHeight':wtWebGraphThermoHygroGraphicsBaseHeight,'wtWebGraphThermoHygroGraphicsBaseFrameColor':wtWebGraphThermoHygroGraphicsBaseFrameColor,'wtWebGraphThermoHygroGraphicsBaseBackgroundColor':wtWebGraphThermoHygroGraphicsBaseBackgroundColor,'wtWebGraphThermoHygroGraphicsBasePollingrate':wtWebGraphThermoHygroGraphicsBasePollingrate,'wtWebGraphThermoHygroGraphicsSelect':wtWebGraphThermoHygroGraphicsSelect,'wtWebGraphThermoHygroGraphicsSelectDisplaySensorSel':wtWebGraphThermoHygroGraphicsSelectDisplaySensorSel,'wtWebGraphThermoHygroGraphicsSelectDisplayShowExtrem':wtWebGraphThermoHygroGraphicsSelectDisplayShowExtrem,'wtWebGraphThermoHygroSensorColorTable':wtWebGraphThermoHygroSensorColorTable,'wtWebGraphThermoHygroSensorColorEntry':wtWebGraphThermoHygroSensorColorEntry,'wtWebGraphThermoHygroGraphicsSensorColor':wtWebGraphThermoHygroGraphicsSensorColor,'wtWebGraphThermoHygroGraphicsSelectScale':wtWebGraphThermoHygroGraphicsSelectScale,'wtWebGraphThermoHygroGraphicsScale':wtWebGraphThermoHygroGraphicsScale,'wtWebGraphThermoHygroGraphicsScaleAutoScaleEnable':wtWebGraphThermoHygroGraphicsScaleAutoScaleEnable,'wtWebGraphThermoHygroGraphicsScaleAutoFitEnable':wtWebGraphThermoHygroGraphicsScaleAutoFitEnable,'wtWebGraphThermoHygroGraphicsScale1Min':wtWebGraphThermoHygroGraphicsScale1Min,'wtWebGraphThermoHygroGraphicsScale2Min':wtWebGraphThermoHygroGraphicsScale2Min,'wtWebGraphThermoHygroGraphicsScale3Min':wtWebGraphThermoHygroGraphicsScale3Min,'wtWebGraphThermoHygroGraphicsScale4Min':wtWebGraphThermoHygroGraphicsScale4Min,'wtWebGraphThermoHygroGraphicsScale1Max':wtWebGraphThermoHygroGraphicsScale1Max,'wtWebGraphThermoHygroGraphicsScale2Max':wtWebGraphThermoHygroGraphicsScale2Max,'wtWebGraphThermoHygroGraphicsScale3Max':wtWebGraphThermoHygroGraphicsScale3Max,'wtWebGraphThermoHygroGraphicsScale4Max':wtWebGraphThermoHygroGraphicsScale4Max,'wtWebGraphThermoHygroGraphicsScale1Unit':wtWebGraphThermoHygroGraphicsScale1Unit,'wtWebGraphThermoHygroGraphicsScale2Unit':wtWebGraphThermoHygroGraphicsScale2Unit,'wtWebGraphThermoHygroGraphicsScale3Unit':wtWebGraphThermoHygroGraphicsScale3Unit,'wtWebGraphThermoHygroGraphicsScale4Unit':wtWebGraphThermoHygroGraphicsScale4Unit,'wtWebGraphThermoHygroPorts':wtWebGraphThermoHygroPorts,'wtWebGraphThermoHygroPortTable':wtWebGraphThermoHygroPortTable,'wtWebGraphThermoHygroPortEntry':wtWebGraphThermoHygroPortEntry,'wtWebGraphThermoHygroPortName':wtWebGraphThermoHygroPortName,'wtWebGraphThermoHygroPortText':wtWebGraphThermoHygroPortText,'wtWebGraphThermoHygroPortOffset1':wtWebGraphThermoHygroPortOffset1,'wtWebGraphThermoHygroPortTemperature1':wtWebGraphThermoHygroPortTemperature1,'wtWebGraphThermoHygroPortOffset2':wtWebGraphThermoHygroPortOffset2,'wtWebGraphThermoHygroPortTemperature2':wtWebGraphThermoHygroPortTemperature2,'wtWebGraphThermoHygroPortComment':wtWebGraphThermoHygroPortComment,'wtWebGraphThermoHygroPortAltidude':wtWebGraphThermoHygroPortAltidude,'wtWebGraphThermoHygroManufact':wtWebGraphThermoHygroManufact,'wtWebGraphThermoHygroMfName':wtWebGraphThermoHygroMfName,'wtWebGraphThermoHygroMfAddr':wtWebGraphThermoHygroMfAddr,'wtWebGraphThermoHygroMfHotline':wtWebGraphThermoHygroMfHotline,'wtWebGraphThermoHygroMfInternet':wtWebGraphThermoHygroMfInternet,'wtWebGraphThermoHygroMfDeviceTyp':wtWebGraphThermoHygroMfDeviceTyp,'wtWebGraphThermoHygroMfOrderNo':wtWebGraphThermoHygroMfOrderNo,'wtWebGraphThermoHygroDiag':wtWebGraphThermoHygroDiag,'wtWebGraphThermoHygroDiagErrorCount':wtWebGraphThermoHygroDiagErrorCount,'wtWebGraphThermoHygroDiagBinaryError':wtWebGraphThermoHygroDiagBinaryError,_L:wtWebGraphThermoHygroDiagErrorIndex,_M:wtWebGraphThermoHygroDiagErrorMessage,'wtWebGraphThermoHygroDiagErrorClear':wtWebGraphThermoHygroDiagErrorClear})