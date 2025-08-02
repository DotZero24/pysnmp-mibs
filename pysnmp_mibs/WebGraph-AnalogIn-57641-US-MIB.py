_M='wtWebGraphAnalogIn57641DiagErrorMessage'
_L='wtWebGraphAnalogIn57641DiagErrorIndex'
_K='NotificationType'
_J='wtWebGraphAnalogIn57641AlarmNo'
_I='wtWebGraphAnalogIn57641SensorNo'
_H='wtWebGraphAnalogIn57641AlarmClearTrapText'
_G='wtWebGraphAnalogIn57641AlarmTrapText'
_F='OctetString'
_E='read-only'
_D='Integer32'
_C='WebGraph-AnalogIn-57641-US-MIB'
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
_WtWebGraphAnalogIn57641_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641=_WtWebGraphAnalogIn57641_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10))
_WtWebGraphAnalogIn57641Inventory_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641Inventory=_WtWebGraphAnalogIn57641Inventory_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,1))
class _WtWebGraphAnalogIn57641Sensors_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_WtWebGraphAnalogIn57641Sensors_Type.__name__=_D
_WtWebGraphAnalogIn57641Sensors_Object=MibScalar
wtWebGraphAnalogIn57641Sensors=_WtWebGraphAnalogIn57641Sensors_Object((1,3,6,1,4,1,5040,1,2,10,1,1),_WtWebGraphAnalogIn57641Sensors_Type())
wtWebGraphAnalogIn57641Sensors.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641Sensors.setStatus(_A)
_WtWebGraphAnalogIn57641SensorTable_Object=MibTable
wtWebGraphAnalogIn57641SensorTable=_WtWebGraphAnalogIn57641SensorTable_Object((1,3,6,1,4,1,5040,1,2,10,1,2))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SensorTable.setStatus(_A)
_WtWebGraphAnalogIn57641SensorEntry_Object=MibTableRow
wtWebGraphAnalogIn57641SensorEntry=_WtWebGraphAnalogIn57641SensorEntry_Object((1,3,6,1,4,1,5040,1,2,10,1,2,1))
wtWebGraphAnalogIn57641SensorEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SensorEntry.setStatus(_A)
class _WtWebGraphAnalogIn57641SensorNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_WtWebGraphAnalogIn57641SensorNo_Type.__name__=_D
_WtWebGraphAnalogIn57641SensorNo_Object=MibTableColumn
wtWebGraphAnalogIn57641SensorNo=_WtWebGraphAnalogIn57641SensorNo_Object((1,3,6,1,4,1,5040,1,2,10,1,2,1,1),_WtWebGraphAnalogIn57641SensorNo_Type())
wtWebGraphAnalogIn57641SensorNo.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SensorNo.setStatus(_A)
_WtWebGraphAnalogIn57641ValuesTable_Object=MibTable
wtWebGraphAnalogIn57641ValuesTable=_WtWebGraphAnalogIn57641ValuesTable_Object((1,3,6,1,4,1,5040,1,2,10,1,3))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641ValuesTable.setStatus(_A)
_WtWebGraphAnalogIn57641ValuesEntry_Object=MibTableRow
wtWebGraphAnalogIn57641ValuesEntry=_WtWebGraphAnalogIn57641ValuesEntry_Object((1,3,6,1,4,1,5040,1,2,10,1,3,1))
wtWebGraphAnalogIn57641ValuesEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641ValuesEntry.setStatus(_A)
class _WtWebGraphAnalogIn57641Values_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_WtWebGraphAnalogIn57641Values_Type.__name__=_F
_WtWebGraphAnalogIn57641Values_Object=MibTableColumn
wtWebGraphAnalogIn57641Values=_WtWebGraphAnalogIn57641Values_Object((1,3,6,1,4,1,5040,1,2,10,1,3,1,1),_WtWebGraphAnalogIn57641Values_Type())
wtWebGraphAnalogIn57641Values.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641Values.setStatus(_A)
_WtWebGraphAnalogIn57641BinaryValuesTable_Object=MibTable
wtWebGraphAnalogIn57641BinaryValuesTable=_WtWebGraphAnalogIn57641BinaryValuesTable_Object((1,3,6,1,4,1,5040,1,2,10,1,4))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641BinaryValuesTable.setStatus(_A)
_WtWebGraphAnalogIn57641BinaryValuesEntry_Object=MibTableRow
wtWebGraphAnalogIn57641BinaryValuesEntry=_WtWebGraphAnalogIn57641BinaryValuesEntry_Object((1,3,6,1,4,1,5040,1,2,10,1,4,1))
wtWebGraphAnalogIn57641BinaryValuesEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641BinaryValuesEntry.setStatus(_A)
_WtWebGraphAnalogIn57641BinaryValues_Type=Integer32
_WtWebGraphAnalogIn57641BinaryValues_Object=MibTableColumn
wtWebGraphAnalogIn57641BinaryValues=_WtWebGraphAnalogIn57641BinaryValues_Object((1,3,6,1,4,1,5040,1,2,10,1,4,1,1),_WtWebGraphAnalogIn57641BinaryValues_Type())
wtWebGraphAnalogIn57641BinaryValues.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641BinaryValues.setStatus(_A)
_WtWebGraphAnalogIn57641SessCntrl_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641SessCntrl=_WtWebGraphAnalogIn57641SessCntrl_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,2))
_WtWebGraphAnalogIn57641SessCntrlPassword_Type=OctetString
_WtWebGraphAnalogIn57641SessCntrlPassword_Object=MibScalar
wtWebGraphAnalogIn57641SessCntrlPassword=_WtWebGraphAnalogIn57641SessCntrlPassword_Object((1,3,6,1,4,1,5040,1,2,10,2,1),_WtWebGraphAnalogIn57641SessCntrlPassword_Type())
wtWebGraphAnalogIn57641SessCntrlPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SessCntrlPassword.setStatus(_A)
class _WtWebGraphAnalogIn57641SessCntrlConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('wtWebGraphAnalogIn57641SessCntrl-NoSession',0),('wtWebGraphAnalogIn57641SessCntrl-Session',1)))
_WtWebGraphAnalogIn57641SessCntrlConfigMode_Type.__name__=_D
_WtWebGraphAnalogIn57641SessCntrlConfigMode_Object=MibScalar
wtWebGraphAnalogIn57641SessCntrlConfigMode=_WtWebGraphAnalogIn57641SessCntrlConfigMode_Object((1,3,6,1,4,1,5040,1,2,10,2,2),_WtWebGraphAnalogIn57641SessCntrlConfigMode_Type())
wtWebGraphAnalogIn57641SessCntrlConfigMode.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SessCntrlConfigMode.setStatus(_A)
_WtWebGraphAnalogIn57641SessCntrlLogout_Type=Integer32
_WtWebGraphAnalogIn57641SessCntrlLogout_Object=MibScalar
wtWebGraphAnalogIn57641SessCntrlLogout=_WtWebGraphAnalogIn57641SessCntrlLogout_Object((1,3,6,1,4,1,5040,1,2,10,2,3),_WtWebGraphAnalogIn57641SessCntrlLogout_Type())
wtWebGraphAnalogIn57641SessCntrlLogout.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SessCntrlLogout.setStatus(_A)
_WtWebGraphAnalogIn57641SessCntrlAdminPassword_Type=OctetString
_WtWebGraphAnalogIn57641SessCntrlAdminPassword_Object=MibScalar
wtWebGraphAnalogIn57641SessCntrlAdminPassword=_WtWebGraphAnalogIn57641SessCntrlAdminPassword_Object((1,3,6,1,4,1,5040,1,2,10,2,4),_WtWebGraphAnalogIn57641SessCntrlAdminPassword_Type())
wtWebGraphAnalogIn57641SessCntrlAdminPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SessCntrlAdminPassword.setStatus(_A)
_WtWebGraphAnalogIn57641SessCntrlConfigPassword_Type=OctetString
_WtWebGraphAnalogIn57641SessCntrlConfigPassword_Object=MibScalar
wtWebGraphAnalogIn57641SessCntrlConfigPassword=_WtWebGraphAnalogIn57641SessCntrlConfigPassword_Object((1,3,6,1,4,1,5040,1,2,10,2,5),_WtWebGraphAnalogIn57641SessCntrlConfigPassword_Type())
wtWebGraphAnalogIn57641SessCntrlConfigPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SessCntrlConfigPassword.setStatus(_A)
_WtWebGraphAnalogIn57641Config_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641Config=_WtWebGraphAnalogIn57641Config_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,3))
_WtWebGraphAnalogIn57641Device_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641Device=_WtWebGraphAnalogIn57641Device_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,3,1))
_WtWebGraphAnalogIn57641Text_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641Text=_WtWebGraphAnalogIn57641Text_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,3,1,1))
_WtWebGraphAnalogIn57641DeviceName_Type=OctetString
_WtWebGraphAnalogIn57641DeviceName_Object=MibScalar
wtWebGraphAnalogIn57641DeviceName=_WtWebGraphAnalogIn57641DeviceName_Object((1,3,6,1,4,1,5040,1,2,10,3,1,1,1),_WtWebGraphAnalogIn57641DeviceName_Type())
wtWebGraphAnalogIn57641DeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641DeviceName.setStatus(_A)
_WtWebGraphAnalogIn57641DeviceText_Type=OctetString
_WtWebGraphAnalogIn57641DeviceText_Object=MibScalar
wtWebGraphAnalogIn57641DeviceText=_WtWebGraphAnalogIn57641DeviceText_Object((1,3,6,1,4,1,5040,1,2,10,3,1,1,2),_WtWebGraphAnalogIn57641DeviceText_Type())
wtWebGraphAnalogIn57641DeviceText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641DeviceText.setStatus(_A)
_WtWebGraphAnalogIn57641DeviceLocation_Type=OctetString
_WtWebGraphAnalogIn57641DeviceLocation_Object=MibScalar
wtWebGraphAnalogIn57641DeviceLocation=_WtWebGraphAnalogIn57641DeviceLocation_Object((1,3,6,1,4,1,5040,1,2,10,3,1,1,3),_WtWebGraphAnalogIn57641DeviceLocation_Type())
wtWebGraphAnalogIn57641DeviceLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641DeviceLocation.setStatus(_A)
_WtWebGraphAnalogIn57641DeviceContact_Type=OctetString
_WtWebGraphAnalogIn57641DeviceContact_Object=MibScalar
wtWebGraphAnalogIn57641DeviceContact=_WtWebGraphAnalogIn57641DeviceContact_Object((1,3,6,1,4,1,5040,1,2,10,3,1,1,4),_WtWebGraphAnalogIn57641DeviceContact_Type())
wtWebGraphAnalogIn57641DeviceContact.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641DeviceContact.setStatus(_A)
_WtWebGraphAnalogIn57641TimeDate_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641TimeDate=_WtWebGraphAnalogIn57641TimeDate_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,3,1,2))
_WtWebGraphAnalogIn57641TimeZone_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641TimeZone=_WtWebGraphAnalogIn57641TimeZone_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,3,1,2,1))
_WtWebGraphAnalogIn57641TzOffsetHrs_Type=Integer32
_WtWebGraphAnalogIn57641TzOffsetHrs_Object=MibScalar
wtWebGraphAnalogIn57641TzOffsetHrs=_WtWebGraphAnalogIn57641TzOffsetHrs_Object((1,3,6,1,4,1,5040,1,2,10,3,1,2,1,1),_WtWebGraphAnalogIn57641TzOffsetHrs_Type())
wtWebGraphAnalogIn57641TzOffsetHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641TzOffsetHrs.setStatus(_A)
_WtWebGraphAnalogIn57641TzOffsetMin_Type=Integer32
_WtWebGraphAnalogIn57641TzOffsetMin_Object=MibScalar
wtWebGraphAnalogIn57641TzOffsetMin=_WtWebGraphAnalogIn57641TzOffsetMin_Object((1,3,6,1,4,1,5040,1,2,10,3,1,2,1,2),_WtWebGraphAnalogIn57641TzOffsetMin_Type())
wtWebGraphAnalogIn57641TzOffsetMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641TzOffsetMin.setStatus(_A)
class _WtWebGraphAnalogIn57641TzEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalogIn57641TzEnable_Type.__name__=_F
_WtWebGraphAnalogIn57641TzEnable_Object=MibScalar
wtWebGraphAnalogIn57641TzEnable=_WtWebGraphAnalogIn57641TzEnable_Object((1,3,6,1,4,1,5040,1,2,10,3,1,2,1,3),_WtWebGraphAnalogIn57641TzEnable_Type())
wtWebGraphAnalogIn57641TzEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641TzEnable.setStatus(_A)
_WtWebGraphAnalogIn57641StTzOffsetHrs_Type=Integer32
_WtWebGraphAnalogIn57641StTzOffsetHrs_Object=MibScalar
wtWebGraphAnalogIn57641StTzOffsetHrs=_WtWebGraphAnalogIn57641StTzOffsetHrs_Object((1,3,6,1,4,1,5040,1,2,10,3,1,2,1,4),_WtWebGraphAnalogIn57641StTzOffsetHrs_Type())
wtWebGraphAnalogIn57641StTzOffsetHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641StTzOffsetHrs.setStatus(_A)
_WtWebGraphAnalogIn57641StTzOffsetMin_Type=Integer32
_WtWebGraphAnalogIn57641StTzOffsetMin_Object=MibScalar
wtWebGraphAnalogIn57641StTzOffsetMin=_WtWebGraphAnalogIn57641StTzOffsetMin_Object((1,3,6,1,4,1,5040,1,2,10,3,1,2,1,5),_WtWebGraphAnalogIn57641StTzOffsetMin_Type())
wtWebGraphAnalogIn57641StTzOffsetMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641StTzOffsetMin.setStatus(_A)
class _WtWebGraphAnalogIn57641StTzEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalogIn57641StTzEnable_Type.__name__=_F
_WtWebGraphAnalogIn57641StTzEnable_Object=MibScalar
wtWebGraphAnalogIn57641StTzEnable=_WtWebGraphAnalogIn57641StTzEnable_Object((1,3,6,1,4,1,5040,1,2,10,3,1,2,1,6),_WtWebGraphAnalogIn57641StTzEnable_Type())
wtWebGraphAnalogIn57641StTzEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641StTzEnable.setStatus(_A)
class _WtWebGraphAnalogIn57641StTzStartMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('wtWebGraphAnalogIn57641StartMonth-January',1),('wtWebGraphAnalogIn57641StartMonth-February',2),('wtWebGraphAnalogIn57641StartMonth-March',3),('wtWebGraphAnalogIn57641StartMonth-April',4),('wtWebGraphAnalogIn57641StartMonth-May',5),('wtWebGraphAnalogIn57641StartMonth-June',6),('wtWebGraphAnalogIn57641StartMonth-July',7),('wtWebGraphAnalogIn57641StartMonth-August',8),('wtWebGraphAnalogIn57641StartMonth-September',9),('wtWebGraphAnalogIn57641StartMonth-October',10),('wtWebGraphAnalogIn57641StartMonth-November',11),('wtWebGraphAnalogIn57641StartMonth-December',12)))
_WtWebGraphAnalogIn57641StTzStartMonth_Type.__name__=_D
_WtWebGraphAnalogIn57641StTzStartMonth_Object=MibScalar
wtWebGraphAnalogIn57641StTzStartMonth=_WtWebGraphAnalogIn57641StTzStartMonth_Object((1,3,6,1,4,1,5040,1,2,10,3,1,2,1,7),_WtWebGraphAnalogIn57641StTzStartMonth_Type())
wtWebGraphAnalogIn57641StTzStartMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641StTzStartMonth.setStatus(_A)
class _WtWebGraphAnalogIn57641StTzStartMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('wtWebGraphAnalogIn57641StartMode-first',1),('wtWebGraphAnalogIn57641StartMode-second',2),('wtWebGraphAnalogIn57641StartMode-third',3),('wtWebGraphAnalogIn57641StartMode-fourth',4),('wtWebGraphAnalogIn57641StartMode-last',5)))
_WtWebGraphAnalogIn57641StTzStartMode_Type.__name__=_D
_WtWebGraphAnalogIn57641StTzStartMode_Object=MibScalar
wtWebGraphAnalogIn57641StTzStartMode=_WtWebGraphAnalogIn57641StTzStartMode_Object((1,3,6,1,4,1,5040,1,2,10,3,1,2,1,8),_WtWebGraphAnalogIn57641StTzStartMode_Type())
wtWebGraphAnalogIn57641StTzStartMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641StTzStartMode.setStatus(_A)
class _WtWebGraphAnalogIn57641StTzStartWday_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('wtWebGraphAnalogIn57641StartWday-Sunday',1),('wtWebGraphAnalogIn57641StartWday-Monday',2),('wtWebGraphAnalogIn57641StartWday-Tuesday',3),('wtWebGraphAnalogIn57641StartWday-Thursday',4),('wtWebGraphAnalogIn57641StartWday-Wednesday',5),('wtWebGraphAnalogIn57641StartWday-Friday',6),('wtWebGraphAnalogIn57641StartWday-Saturday',7)))
_WtWebGraphAnalogIn57641StTzStartWday_Type.__name__=_D
_WtWebGraphAnalogIn57641StTzStartWday_Object=MibScalar
wtWebGraphAnalogIn57641StTzStartWday=_WtWebGraphAnalogIn57641StTzStartWday_Object((1,3,6,1,4,1,5040,1,2,10,3,1,2,1,9),_WtWebGraphAnalogIn57641StTzStartWday_Type())
wtWebGraphAnalogIn57641StTzStartWday.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641StTzStartWday.setStatus(_A)
_WtWebGraphAnalogIn57641StTzStartHrs_Type=Integer32
_WtWebGraphAnalogIn57641StTzStartHrs_Object=MibScalar
wtWebGraphAnalogIn57641StTzStartHrs=_WtWebGraphAnalogIn57641StTzStartHrs_Object((1,3,6,1,4,1,5040,1,2,10,3,1,2,1,10),_WtWebGraphAnalogIn57641StTzStartHrs_Type())
wtWebGraphAnalogIn57641StTzStartHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641StTzStartHrs.setStatus(_A)
_WtWebGraphAnalogIn57641StTzStartMin_Type=Integer32
_WtWebGraphAnalogIn57641StTzStartMin_Object=MibScalar
wtWebGraphAnalogIn57641StTzStartMin=_WtWebGraphAnalogIn57641StTzStartMin_Object((1,3,6,1,4,1,5040,1,2,10,3,1,2,1,11),_WtWebGraphAnalogIn57641StTzStartMin_Type())
wtWebGraphAnalogIn57641StTzStartMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641StTzStartMin.setStatus(_A)
class _WtWebGraphAnalogIn57641StTzStopMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('wtWebGraphAnalogIn57641StopMonth-January',1),('wtWebGraphAnalogIn57641StopMonth-February',2),('wtWebGraphAnalogIn57641StopMonth-March',3),('wtWebGraphAnalogIn57641StopMonth-April',4),('wtWebGraphAnalogIn57641StopMonth-May',5),('wtWebGraphAnalogIn57641StopMonth-June',6),('wtWebGraphAnalogIn57641StopMonth-July',7),('wtWebGraphAnalogIn57641StopMonth-August',8),('wtWebGraphAnalogIn57641StopMonth-September',9),('wtWebGraphAnalogIn57641StopMonth-October',10),('wtWebGraphAnalogIn57641StopMonth-November',11),('wtWebGraphAnalogIn57641StopMonth-December',12)))
_WtWebGraphAnalogIn57641StTzStopMonth_Type.__name__=_D
_WtWebGraphAnalogIn57641StTzStopMonth_Object=MibScalar
wtWebGraphAnalogIn57641StTzStopMonth=_WtWebGraphAnalogIn57641StTzStopMonth_Object((1,3,6,1,4,1,5040,1,2,10,3,1,2,1,12),_WtWebGraphAnalogIn57641StTzStopMonth_Type())
wtWebGraphAnalogIn57641StTzStopMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641StTzStopMonth.setStatus(_A)
class _WtWebGraphAnalogIn57641StTzStopMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('wtWebGraphAnalogIn57641StopMode-first',1),('wtWebGraphAnalogIn57641StopMode-second',2),('wtWebGraphAnalogIn57641StopMode-third',3),('wtWebGraphAnalogIn57641StopMode-fourth',4),('wtWebGraphAnalogIn57641StopMode-last',5)))
_WtWebGraphAnalogIn57641StTzStopMode_Type.__name__=_D
_WtWebGraphAnalogIn57641StTzStopMode_Object=MibScalar
wtWebGraphAnalogIn57641StTzStopMode=_WtWebGraphAnalogIn57641StTzStopMode_Object((1,3,6,1,4,1,5040,1,2,10,3,1,2,1,13),_WtWebGraphAnalogIn57641StTzStopMode_Type())
wtWebGraphAnalogIn57641StTzStopMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641StTzStopMode.setStatus(_A)
class _WtWebGraphAnalogIn57641StTzStopWday_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('wtWebGraphAnalogIn57641StopWday-Sunday',1),('wtWebGraphAnalogIn57641StopWday-Monday',2),('wtWebGraphAnalogIn57641StopWday-Tuesday',3),('wtWebGraphAnalogIn57641StopWday-Thursday',4),('wtWebGraphAnalogIn57641StopWday-Wednesday',5),('wtWebGraphAnalogIn57641StopWday-Friday',6),('wtWebGraphAnalogIn57641StopWday-Saturday',7)))
_WtWebGraphAnalogIn57641StTzStopWday_Type.__name__=_D
_WtWebGraphAnalogIn57641StTzStopWday_Object=MibScalar
wtWebGraphAnalogIn57641StTzStopWday=_WtWebGraphAnalogIn57641StTzStopWday_Object((1,3,6,1,4,1,5040,1,2,10,3,1,2,1,14),_WtWebGraphAnalogIn57641StTzStopWday_Type())
wtWebGraphAnalogIn57641StTzStopWday.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641StTzStopWday.setStatus(_A)
_WtWebGraphAnalogIn57641StTzStopHrs_Type=Integer32
_WtWebGraphAnalogIn57641StTzStopHrs_Object=MibScalar
wtWebGraphAnalogIn57641StTzStopHrs=_WtWebGraphAnalogIn57641StTzStopHrs_Object((1,3,6,1,4,1,5040,1,2,10,3,1,2,1,15),_WtWebGraphAnalogIn57641StTzStopHrs_Type())
wtWebGraphAnalogIn57641StTzStopHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641StTzStopHrs.setStatus(_A)
_WtWebGraphAnalogIn57641StTzStopMin_Type=Integer32
_WtWebGraphAnalogIn57641StTzStopMin_Object=MibScalar
wtWebGraphAnalogIn57641StTzStopMin=_WtWebGraphAnalogIn57641StTzStopMin_Object((1,3,6,1,4,1,5040,1,2,10,3,1,2,1,16),_WtWebGraphAnalogIn57641StTzStopMin_Type())
wtWebGraphAnalogIn57641StTzStopMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641StTzStopMin.setStatus(_A)
_WtWebGraphAnalogIn57641TimeServer_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641TimeServer=_WtWebGraphAnalogIn57641TimeServer_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,3,1,2,2))
_WtWebGraphAnalogIn57641TimeServer1_Type=OctetString
_WtWebGraphAnalogIn57641TimeServer1_Object=MibScalar
wtWebGraphAnalogIn57641TimeServer1=_WtWebGraphAnalogIn57641TimeServer1_Object((1,3,6,1,4,1,5040,1,2,10,3,1,2,2,1),_WtWebGraphAnalogIn57641TimeServer1_Type())
wtWebGraphAnalogIn57641TimeServer1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641TimeServer1.setStatus(_A)
_WtWebGraphAnalogIn57641TimeServer2_Type=OctetString
_WtWebGraphAnalogIn57641TimeServer2_Object=MibScalar
wtWebGraphAnalogIn57641TimeServer2=_WtWebGraphAnalogIn57641TimeServer2_Object((1,3,6,1,4,1,5040,1,2,10,3,1,2,2,2),_WtWebGraphAnalogIn57641TimeServer2_Type())
wtWebGraphAnalogIn57641TimeServer2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641TimeServer2.setStatus(_A)
class _WtWebGraphAnalogIn57641TsEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalogIn57641TsEnable_Type.__name__=_F
_WtWebGraphAnalogIn57641TsEnable_Object=MibScalar
wtWebGraphAnalogIn57641TsEnable=_WtWebGraphAnalogIn57641TsEnable_Object((1,3,6,1,4,1,5040,1,2,10,3,1,2,2,3),_WtWebGraphAnalogIn57641TsEnable_Type())
wtWebGraphAnalogIn57641TsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641TsEnable.setStatus(_A)
_WtWebGraphAnalogIn57641TsSyncTime_Type=Integer32
_WtWebGraphAnalogIn57641TsSyncTime_Object=MibScalar
wtWebGraphAnalogIn57641TsSyncTime=_WtWebGraphAnalogIn57641TsSyncTime_Object((1,3,6,1,4,1,5040,1,2,10,3,1,2,2,4),_WtWebGraphAnalogIn57641TsSyncTime_Type())
wtWebGraphAnalogIn57641TsSyncTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641TsSyncTime.setStatus(_A)
_WtWebGraphAnalogIn57641DeviceClock_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641DeviceClock=_WtWebGraphAnalogIn57641DeviceClock_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,3,1,2,3))
class _WtWebGraphAnalogIn57641ClockHrs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_WtWebGraphAnalogIn57641ClockHrs_Type.__name__=_D
_WtWebGraphAnalogIn57641ClockHrs_Object=MibScalar
wtWebGraphAnalogIn57641ClockHrs=_WtWebGraphAnalogIn57641ClockHrs_Object((1,3,6,1,4,1,5040,1,2,10,3,1,2,3,1),_WtWebGraphAnalogIn57641ClockHrs_Type())
wtWebGraphAnalogIn57641ClockHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641ClockHrs.setStatus(_A)
class _WtWebGraphAnalogIn57641ClockMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_WtWebGraphAnalogIn57641ClockMin_Type.__name__=_D
_WtWebGraphAnalogIn57641ClockMin_Object=MibScalar
wtWebGraphAnalogIn57641ClockMin=_WtWebGraphAnalogIn57641ClockMin_Object((1,3,6,1,4,1,5040,1,2,10,3,1,2,3,2),_WtWebGraphAnalogIn57641ClockMin_Type())
wtWebGraphAnalogIn57641ClockMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641ClockMin.setStatus(_A)
class _WtWebGraphAnalogIn57641ClockDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_WtWebGraphAnalogIn57641ClockDay_Type.__name__=_D
_WtWebGraphAnalogIn57641ClockDay_Object=MibScalar
wtWebGraphAnalogIn57641ClockDay=_WtWebGraphAnalogIn57641ClockDay_Object((1,3,6,1,4,1,5040,1,2,10,3,1,2,3,3),_WtWebGraphAnalogIn57641ClockDay_Type())
wtWebGraphAnalogIn57641ClockDay.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641ClockDay.setStatus(_A)
class _WtWebGraphAnalogIn57641ClockMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('wtWebGraphAnalogIn57641ClockMonth-January',1),('wtWebGraphAnalogIn57641ClockMonth-February',2),('wtWebGraphAnalogIn57641ClockMonth-March',3),('wtWebGraphAnalogIn57641ClockMonth-April',4),('wtWebGraphAnalogIn57641ClockMonth-May',5),('wtWebGraphAnalogIn57641ClockMonth-June',6),('wtWebGraphAnalogIn57641ClockMonth-July',7),('wtWebGraphAnalogIn57641ClockMonth-August',8),('wtWebGraphAnalogIn57641ClockMonth-September',9),('wtWebGraphAnalogIn57641ClockMonth-October',10),('wtWebGraphAnalogIn57641ClockMonth-November',11),('wtWebGraphAnalogIn57641ClockMonth-December',12)))
_WtWebGraphAnalogIn57641ClockMonth_Type.__name__=_D
_WtWebGraphAnalogIn57641ClockMonth_Object=MibScalar
wtWebGraphAnalogIn57641ClockMonth=_WtWebGraphAnalogIn57641ClockMonth_Object((1,3,6,1,4,1,5040,1,2,10,3,1,2,3,4),_WtWebGraphAnalogIn57641ClockMonth_Type())
wtWebGraphAnalogIn57641ClockMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641ClockMonth.setStatus(_A)
class _WtWebGraphAnalogIn57641ClockYear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtWebGraphAnalogIn57641ClockYear_Type.__name__=_D
_WtWebGraphAnalogIn57641ClockYear_Object=MibScalar
wtWebGraphAnalogIn57641ClockYear=_WtWebGraphAnalogIn57641ClockYear_Object((1,3,6,1,4,1,5040,1,2,10,3,1,2,3,5),_WtWebGraphAnalogIn57641ClockYear_Type())
wtWebGraphAnalogIn57641ClockYear.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641ClockYear.setStatus(_A)
_WtWebGraphAnalogIn57641Basic_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641Basic=_WtWebGraphAnalogIn57641Basic_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,3,1,3))
_WtWebGraphAnalogIn57641Network_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641Network=_WtWebGraphAnalogIn57641Network_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,3,1,3,1))
_WtWebGraphAnalogIn57641IpAddress_Type=IpAddress
_WtWebGraphAnalogIn57641IpAddress_Object=MibScalar
wtWebGraphAnalogIn57641IpAddress=_WtWebGraphAnalogIn57641IpAddress_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,1,1),_WtWebGraphAnalogIn57641IpAddress_Type())
wtWebGraphAnalogIn57641IpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641IpAddress.setStatus(_A)
_WtWebGraphAnalogIn57641SubnetMask_Type=IpAddress
_WtWebGraphAnalogIn57641SubnetMask_Object=MibScalar
wtWebGraphAnalogIn57641SubnetMask=_WtWebGraphAnalogIn57641SubnetMask_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,1,2),_WtWebGraphAnalogIn57641SubnetMask_Type())
wtWebGraphAnalogIn57641SubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SubnetMask.setStatus(_A)
_WtWebGraphAnalogIn57641Gateway_Type=IpAddress
_WtWebGraphAnalogIn57641Gateway_Object=MibScalar
wtWebGraphAnalogIn57641Gateway=_WtWebGraphAnalogIn57641Gateway_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,1,3),_WtWebGraphAnalogIn57641Gateway_Type())
wtWebGraphAnalogIn57641Gateway.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641Gateway.setStatus(_A)
_WtWebGraphAnalogIn57641DnsServer1_Type=OctetString
_WtWebGraphAnalogIn57641DnsServer1_Object=MibScalar
wtWebGraphAnalogIn57641DnsServer1=_WtWebGraphAnalogIn57641DnsServer1_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,1,4),_WtWebGraphAnalogIn57641DnsServer1_Type())
wtWebGraphAnalogIn57641DnsServer1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641DnsServer1.setStatus(_A)
_WtWebGraphAnalogIn57641DnsServer2_Type=OctetString
_WtWebGraphAnalogIn57641DnsServer2_Object=MibScalar
wtWebGraphAnalogIn57641DnsServer2=_WtWebGraphAnalogIn57641DnsServer2_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,1,5),_WtWebGraphAnalogIn57641DnsServer2_Type())
wtWebGraphAnalogIn57641DnsServer2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641DnsServer2.setStatus(_A)
_WtWebGraphAnalogIn57641AddConfig_Type=OctetString
_WtWebGraphAnalogIn57641AddConfig_Object=MibScalar
wtWebGraphAnalogIn57641AddConfig=_WtWebGraphAnalogIn57641AddConfig_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,1,6),_WtWebGraphAnalogIn57641AddConfig_Type())
wtWebGraphAnalogIn57641AddConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AddConfig.setStatus(_A)
_WtWebGraphAnalogIn57641HTTP_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641HTTP=_WtWebGraphAnalogIn57641HTTP_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,3,1,3,2))
_WtWebGraphAnalogIn57641Startup_Type=OctetString
_WtWebGraphAnalogIn57641Startup_Object=MibScalar
wtWebGraphAnalogIn57641Startup=_WtWebGraphAnalogIn57641Startup_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,2,1),_WtWebGraphAnalogIn57641Startup_Type())
wtWebGraphAnalogIn57641Startup.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641Startup.setStatus(_A)
_WtWebGraphAnalogIn57641GetHeaderEnable_Type=OctetString
_WtWebGraphAnalogIn57641GetHeaderEnable_Object=MibScalar
wtWebGraphAnalogIn57641GetHeaderEnable=_WtWebGraphAnalogIn57641GetHeaderEnable_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,2,2),_WtWebGraphAnalogIn57641GetHeaderEnable_Type())
wtWebGraphAnalogIn57641GetHeaderEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641GetHeaderEnable.setStatus(_A)
class _WtWebGraphAnalogIn57641HttpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphAnalogIn57641HttpPort_Type.__name__=_D
_WtWebGraphAnalogIn57641HttpPort_Object=MibScalar
wtWebGraphAnalogIn57641HttpPort=_WtWebGraphAnalogIn57641HttpPort_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,2,3),_WtWebGraphAnalogIn57641HttpPort_Type())
wtWebGraphAnalogIn57641HttpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641HttpPort.setStatus(_A)
_WtWebGraphAnalogIn57641Mail_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641Mail=_WtWebGraphAnalogIn57641Mail_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,3,1,3,3))
_WtWebGraphAnalogIn57641MailAdName_Type=OctetString
_WtWebGraphAnalogIn57641MailAdName_Object=MibScalar
wtWebGraphAnalogIn57641MailAdName=_WtWebGraphAnalogIn57641MailAdName_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,3,1),_WtWebGraphAnalogIn57641MailAdName_Type())
wtWebGraphAnalogIn57641MailAdName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641MailAdName.setStatus(_A)
_WtWebGraphAnalogIn57641MailReply_Type=OctetString
_WtWebGraphAnalogIn57641MailReply_Object=MibScalar
wtWebGraphAnalogIn57641MailReply=_WtWebGraphAnalogIn57641MailReply_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,3,2),_WtWebGraphAnalogIn57641MailReply_Type())
wtWebGraphAnalogIn57641MailReply.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641MailReply.setStatus(_A)
_WtWebGraphAnalogIn57641MailServer_Type=OctetString
_WtWebGraphAnalogIn57641MailServer_Object=MibScalar
wtWebGraphAnalogIn57641MailServer=_WtWebGraphAnalogIn57641MailServer_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,3,3),_WtWebGraphAnalogIn57641MailServer_Type())
wtWebGraphAnalogIn57641MailServer.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641MailServer.setStatus(_A)
_WtWebioAn1MailEnable_Type=OctetString
_WtWebioAn1MailEnable_Object=MibScalar
wtWebioAn1MailEnable=_WtWebioAn1MailEnable_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,3,4),_WtWebioAn1MailEnable_Type())
wtWebioAn1MailEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebioAn1MailEnable.setStatus(_A)
class _WtWebGraphAnalogIn57641MailAuthentication_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalogIn57641MailAuthentication_Type.__name__=_F
_WtWebGraphAnalogIn57641MailAuthentication_Object=MibScalar
wtWebGraphAnalogIn57641MailAuthentication=_WtWebGraphAnalogIn57641MailAuthentication_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,3,5),_WtWebGraphAnalogIn57641MailAuthentication_Type())
wtWebGraphAnalogIn57641MailAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641MailAuthentication.setStatus(_A)
_WtWebGraphAnalogIn57641MailAuthUser_Type=OctetString
_WtWebGraphAnalogIn57641MailAuthUser_Object=MibScalar
wtWebGraphAnalogIn57641MailAuthUser=_WtWebGraphAnalogIn57641MailAuthUser_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,3,6),_WtWebGraphAnalogIn57641MailAuthUser_Type())
wtWebGraphAnalogIn57641MailAuthUser.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641MailAuthUser.setStatus(_A)
_WtWebGraphAnalogIn57641MailAuthPassword_Type=OctetString
_WtWebGraphAnalogIn57641MailAuthPassword_Object=MibScalar
wtWebGraphAnalogIn57641MailAuthPassword=_WtWebGraphAnalogIn57641MailAuthPassword_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,3,7),_WtWebGraphAnalogIn57641MailAuthPassword_Type())
wtWebGraphAnalogIn57641MailAuthPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641MailAuthPassword.setStatus(_A)
_WtWebGraphAnalogIn57641MailPop3Server_Type=OctetString
_WtWebGraphAnalogIn57641MailPop3Server_Object=MibScalar
wtWebGraphAnalogIn57641MailPop3Server=_WtWebGraphAnalogIn57641MailPop3Server_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,3,8),_WtWebGraphAnalogIn57641MailPop3Server_Type())
wtWebGraphAnalogIn57641MailPop3Server.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641MailPop3Server.setStatus(_A)
_WtWebGraphAnalogIn57641SNMP_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641SNMP=_WtWebGraphAnalogIn57641SNMP_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,3,1,3,4))
_WtWebGraphAnalogIn57641SnmpCommunityStringRead_Type=OctetString
_WtWebGraphAnalogIn57641SnmpCommunityStringRead_Object=MibScalar
wtWebGraphAnalogIn57641SnmpCommunityStringRead=_WtWebGraphAnalogIn57641SnmpCommunityStringRead_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,4,1),_WtWebGraphAnalogIn57641SnmpCommunityStringRead_Type())
wtWebGraphAnalogIn57641SnmpCommunityStringRead.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SnmpCommunityStringRead.setStatus(_A)
_WtWebGraphAnalogIn57641SnmpCommunityStringReadWrite_Type=OctetString
_WtWebGraphAnalogIn57641SnmpCommunityStringReadWrite_Object=MibScalar
wtWebGraphAnalogIn57641SnmpCommunityStringReadWrite=_WtWebGraphAnalogIn57641SnmpCommunityStringReadWrite_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,4,2),_WtWebGraphAnalogIn57641SnmpCommunityStringReadWrite_Type())
wtWebGraphAnalogIn57641SnmpCommunityStringReadWrite.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SnmpCommunityStringReadWrite.setStatus(_A)
_WtWebGraphAnalogIn57641SystemTrapManagerIP_Type=OctetString
_WtWebGraphAnalogIn57641SystemTrapManagerIP_Object=MibScalar
wtWebGraphAnalogIn57641SystemTrapManagerIP=_WtWebGraphAnalogIn57641SystemTrapManagerIP_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,4,3),_WtWebGraphAnalogIn57641SystemTrapManagerIP_Type())
wtWebGraphAnalogIn57641SystemTrapManagerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SystemTrapManagerIP.setStatus(_A)
class _WtWebGraphAnalogIn57641SystemTrapEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalogIn57641SystemTrapEnable_Type.__name__=_F
_WtWebGraphAnalogIn57641SystemTrapEnable_Object=MibScalar
wtWebGraphAnalogIn57641SystemTrapEnable=_WtWebGraphAnalogIn57641SystemTrapEnable_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,4,4),_WtWebGraphAnalogIn57641SystemTrapEnable_Type())
wtWebGraphAnalogIn57641SystemTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SystemTrapEnable.setStatus(_A)
_WtWebGraphAnalogIn57641SnmpEnable_Type=OctetString
_WtWebGraphAnalogIn57641SnmpEnable_Object=MibScalar
wtWebGraphAnalogIn57641SnmpEnable=_WtWebGraphAnalogIn57641SnmpEnable_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,4,5),_WtWebGraphAnalogIn57641SnmpEnable_Type())
wtWebGraphAnalogIn57641SnmpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SnmpEnable.setStatus(_A)
_WtWebGraphAnalogIn57641SnmpCommunityStringTrap_Type=OctetString
_WtWebGraphAnalogIn57641SnmpCommunityStringTrap_Object=MibScalar
wtWebGraphAnalogIn57641SnmpCommunityStringTrap=_WtWebGraphAnalogIn57641SnmpCommunityStringTrap_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,4,6),_WtWebGraphAnalogIn57641SnmpCommunityStringTrap_Type())
wtWebGraphAnalogIn57641SnmpCommunityStringTrap.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SnmpCommunityStringTrap.setStatus(_A)
_WtWebGraphAnalogIn57641UDP_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641UDP=_WtWebGraphAnalogIn57641UDP_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,3,1,3,5))
class _WtWebGraphAnalogIn57641UdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphAnalogIn57641UdpPort_Type.__name__=_D
_WtWebGraphAnalogIn57641UdpPort_Object=MibScalar
wtWebGraphAnalogIn57641UdpPort=_WtWebGraphAnalogIn57641UdpPort_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,5,1),_WtWebGraphAnalogIn57641UdpPort_Type())
wtWebGraphAnalogIn57641UdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641UdpPort.setStatus(_A)
_WtWebGraphAnalogIn57641UdpEnable_Type=OctetString
_WtWebGraphAnalogIn57641UdpEnable_Object=MibScalar
wtWebGraphAnalogIn57641UdpEnable=_WtWebGraphAnalogIn57641UdpEnable_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,5,2),_WtWebGraphAnalogIn57641UdpEnable_Type())
wtWebGraphAnalogIn57641UdpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641UdpEnable.setStatus(_A)
_WtWebGraphAnalogIn57641Syslog_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641Syslog=_WtWebGraphAnalogIn57641Syslog_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,3,1,3,6))
_WtWebGraphAnalogIn57641SyslogServerIP_Type=OctetString
_WtWebGraphAnalogIn57641SyslogServerIP_Object=MibScalar
wtWebGraphAnalogIn57641SyslogServerIP=_WtWebGraphAnalogIn57641SyslogServerIP_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,6,1),_WtWebGraphAnalogIn57641SyslogServerIP_Type())
wtWebGraphAnalogIn57641SyslogServerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SyslogServerIP.setStatus(_A)
_WtWebGraphAnalogIn57641SyslogServerPort_Type=Integer32
_WtWebGraphAnalogIn57641SyslogServerPort_Object=MibScalar
wtWebGraphAnalogIn57641SyslogServerPort=_WtWebGraphAnalogIn57641SyslogServerPort_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,6,2),_WtWebGraphAnalogIn57641SyslogServerPort_Type())
wtWebGraphAnalogIn57641SyslogServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SyslogServerPort.setStatus(_A)
class _WtWebGraphAnalogIn57641SyslogSystemMessagesEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalogIn57641SyslogSystemMessagesEnable_Type.__name__=_F
_WtWebGraphAnalogIn57641SyslogSystemMessagesEnable_Object=MibScalar
wtWebGraphAnalogIn57641SyslogSystemMessagesEnable=_WtWebGraphAnalogIn57641SyslogSystemMessagesEnable_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,6,3),_WtWebGraphAnalogIn57641SyslogSystemMessagesEnable_Type())
wtWebGraphAnalogIn57641SyslogSystemMessagesEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SyslogSystemMessagesEnable.setStatus(_A)
_WtWebGraphAnalogIn57641SyslogEnable_Type=OctetString
_WtWebGraphAnalogIn57641SyslogEnable_Object=MibScalar
wtWebGraphAnalogIn57641SyslogEnable=_WtWebGraphAnalogIn57641SyslogEnable_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,6,4),_WtWebGraphAnalogIn57641SyslogEnable_Type())
wtWebGraphAnalogIn57641SyslogEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SyslogEnable.setStatus(_A)
_WtWebGraphAnalogIn57641FTP_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641FTP=_WtWebGraphAnalogIn57641FTP_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,3,1,3,7))
_WtWebGraphAnalogIn57641FTPServerIP_Type=OctetString
_WtWebGraphAnalogIn57641FTPServerIP_Object=MibScalar
wtWebGraphAnalogIn57641FTPServerIP=_WtWebGraphAnalogIn57641FTPServerIP_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,7,1),_WtWebGraphAnalogIn57641FTPServerIP_Type())
wtWebGraphAnalogIn57641FTPServerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641FTPServerIP.setStatus(_A)
_WtWebGraphAnalogIn57641FTPServerControlPort_Type=Integer32
_WtWebGraphAnalogIn57641FTPServerControlPort_Object=MibScalar
wtWebGraphAnalogIn57641FTPServerControlPort=_WtWebGraphAnalogIn57641FTPServerControlPort_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,7,2),_WtWebGraphAnalogIn57641FTPServerControlPort_Type())
wtWebGraphAnalogIn57641FTPServerControlPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641FTPServerControlPort.setStatus(_A)
_WtWebGraphAnalogIn57641FTPUserName_Type=OctetString
_WtWebGraphAnalogIn57641FTPUserName_Object=MibScalar
wtWebGraphAnalogIn57641FTPUserName=_WtWebGraphAnalogIn57641FTPUserName_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,7,3),_WtWebGraphAnalogIn57641FTPUserName_Type())
wtWebGraphAnalogIn57641FTPUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641FTPUserName.setStatus(_A)
_WtWebGraphAnalogIn57641FTPPassword_Type=OctetString
_WtWebGraphAnalogIn57641FTPPassword_Object=MibScalar
wtWebGraphAnalogIn57641FTPPassword=_WtWebGraphAnalogIn57641FTPPassword_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,7,4),_WtWebGraphAnalogIn57641FTPPassword_Type())
wtWebGraphAnalogIn57641FTPPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641FTPPassword.setStatus(_A)
_WtWebGraphAnalogIn57641FTPAccount_Type=OctetString
_WtWebGraphAnalogIn57641FTPAccount_Object=MibScalar
wtWebGraphAnalogIn57641FTPAccount=_WtWebGraphAnalogIn57641FTPAccount_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,7,5),_WtWebGraphAnalogIn57641FTPAccount_Type())
wtWebGraphAnalogIn57641FTPAccount.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641FTPAccount.setStatus(_A)
_WtWebGraphAnalogIn57641FTPOption_Type=OctetString
_WtWebGraphAnalogIn57641FTPOption_Object=MibScalar
wtWebGraphAnalogIn57641FTPOption=_WtWebGraphAnalogIn57641FTPOption_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,7,6),_WtWebGraphAnalogIn57641FTPOption_Type())
wtWebGraphAnalogIn57641FTPOption.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641FTPOption.setStatus(_A)
_WtWebGraphAnalogIn57641FTPEnable_Type=OctetString
_WtWebGraphAnalogIn57641FTPEnable_Object=MibScalar
wtWebGraphAnalogIn57641FTPEnable=_WtWebGraphAnalogIn57641FTPEnable_Object((1,3,6,1,4,1,5040,1,2,10,3,1,3,7,7),_WtWebGraphAnalogIn57641FTPEnable_Type())
wtWebGraphAnalogIn57641FTPEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641FTPEnable.setStatus(_A)
_WtWebGraphAnalogIn57641Datalogger_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641Datalogger=_WtWebGraphAnalogIn57641Datalogger_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,3,1,4))
class _WtWebGraphAnalogIn57641LoggerTimebase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('wtWebGraphAnalogIn57641Datalogger-1Min',1),('wtWebGraphAnalogIn57641Datalogger-5Min',2),('wtWebGraphAnalogIn57641Datalogger-15Min',3),('wtWebGraphAnalogIn57641Datalogger-60Min',4)))
_WtWebGraphAnalogIn57641LoggerTimebase_Type.__name__=_D
_WtWebGraphAnalogIn57641LoggerTimebase_Object=MibScalar
wtWebGraphAnalogIn57641LoggerTimebase=_WtWebGraphAnalogIn57641LoggerTimebase_Object((1,3,6,1,4,1,5040,1,2,10,3,1,4,1),_WtWebGraphAnalogIn57641LoggerTimebase_Type())
wtWebGraphAnalogIn57641LoggerTimebase.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641LoggerTimebase.setStatus(_A)
class _WtWebGraphAnalogIn57641LoggerSensorSel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalogIn57641LoggerSensorSel_Type.__name__=_F
_WtWebGraphAnalogIn57641LoggerSensorSel_Object=MibScalar
wtWebGraphAnalogIn57641LoggerSensorSel=_WtWebGraphAnalogIn57641LoggerSensorSel_Object((1,3,6,1,4,1,5040,1,2,10,3,1,4,2),_WtWebGraphAnalogIn57641LoggerSensorSel_Type())
wtWebGraphAnalogIn57641LoggerSensorSel.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641LoggerSensorSel.setStatus(_A)
class _WtWebGraphAnalogIn57641DisplaySensorSel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalogIn57641DisplaySensorSel_Type.__name__=_F
_WtWebGraphAnalogIn57641DisplaySensorSel_Object=MibScalar
wtWebGraphAnalogIn57641DisplaySensorSel=_WtWebGraphAnalogIn57641DisplaySensorSel_Object((1,3,6,1,4,1,5040,1,2,10,3,1,4,3),_WtWebGraphAnalogIn57641DisplaySensorSel_Type())
wtWebGraphAnalogIn57641DisplaySensorSel.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641DisplaySensorSel.setStatus(_A)
_WtWebGraphAnalogIn57641SensorColorTable_Object=MibTable
wtWebGraphAnalogIn57641SensorColorTable=_WtWebGraphAnalogIn57641SensorColorTable_Object((1,3,6,1,4,1,5040,1,2,10,3,1,4,4))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SensorColorTable.setStatus(_A)
_WtWebGraphAnalogIn57641SensorColorEntry_Object=MibTableRow
wtWebGraphAnalogIn57641SensorColorEntry=_WtWebGraphAnalogIn57641SensorColorEntry_Object((1,3,6,1,4,1,5040,1,2,10,3,1,4,4,1))
wtWebGraphAnalogIn57641SensorColorEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SensorColorEntry.setStatus(_A)
class _WtWebGraphAnalogIn57641SensorColor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_WtWebGraphAnalogIn57641SensorColor_Type.__name__=_F
_WtWebGraphAnalogIn57641SensorColor_Object=MibTableColumn
wtWebGraphAnalogIn57641SensorColor=_WtWebGraphAnalogIn57641SensorColor_Object((1,3,6,1,4,1,5040,1,2,10,3,1,4,4,1,1),_WtWebGraphAnalogIn57641SensorColor_Type())
wtWebGraphAnalogIn57641SensorColor.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SensorColor.setStatus(_A)
_WtWebGraphAnalogIn57641AutoScaleEnable_Type=OctetString
_WtWebGraphAnalogIn57641AutoScaleEnable_Object=MibScalar
wtWebGraphAnalogIn57641AutoScaleEnable=_WtWebGraphAnalogIn57641AutoScaleEnable_Object((1,3,6,1,4,1,5040,1,2,10,3,1,4,5),_WtWebGraphAnalogIn57641AutoScaleEnable_Type())
wtWebGraphAnalogIn57641AutoScaleEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AutoScaleEnable.setStatus(_A)
_WtWebGraphAnalogIn57641VerticalUpperLimit_Type=OctetString
_WtWebGraphAnalogIn57641VerticalUpperLimit_Object=MibScalar
wtWebGraphAnalogIn57641VerticalUpperLimit=_WtWebGraphAnalogIn57641VerticalUpperLimit_Object((1,3,6,1,4,1,5040,1,2,10,3,1,4,6),_WtWebGraphAnalogIn57641VerticalUpperLimit_Type())
wtWebGraphAnalogIn57641VerticalUpperLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641VerticalUpperLimit.setStatus(_A)
_WtWebGraphAnalogIn57641VerticalLowerLimit_Type=OctetString
_WtWebGraphAnalogIn57641VerticalLowerLimit_Object=MibScalar
wtWebGraphAnalogIn57641VerticalLowerLimit=_WtWebGraphAnalogIn57641VerticalLowerLimit_Object((1,3,6,1,4,1,5040,1,2,10,3,1,4,7),_WtWebGraphAnalogIn57641VerticalLowerLimit_Type())
wtWebGraphAnalogIn57641VerticalLowerLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641VerticalLowerLimit.setStatus(_A)
class _WtWebGraphAnalogIn57641HorizontalZoom_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('wtWebGraphAnalogIn57641Zoom-25min',1),('wtWebGraphAnalogIn57641Zoom-75min',2),('wtWebGraphAnalogIn57641Zoom-5hrs',3),('wtWebGraphAnalogIn57641Zoom-30hrs',4),('wtWebGraphAnalogIn57641Zoom-5days',5),('wtWebGraphAnalogIn57641Zoom-25days',6)))
_WtWebGraphAnalogIn57641HorizontalZoom_Type.__name__=_D
_WtWebGraphAnalogIn57641HorizontalZoom_Object=MibScalar
wtWebGraphAnalogIn57641HorizontalZoom=_WtWebGraphAnalogIn57641HorizontalZoom_Object((1,3,6,1,4,1,5040,1,2,10,3,1,4,8),_WtWebGraphAnalogIn57641HorizontalZoom_Type())
wtWebGraphAnalogIn57641HorizontalZoom.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641HorizontalZoom.setStatus(_A)
_WtWebGraphAnalogIn57641Alarm_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641Alarm=_WtWebGraphAnalogIn57641Alarm_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,3,1,5))
class _WtWebGraphAnalogIn57641AlarmCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_WtWebGraphAnalogIn57641AlarmCount_Type.__name__=_D
_WtWebGraphAnalogIn57641AlarmCount_Object=MibScalar
wtWebGraphAnalogIn57641AlarmCount=_WtWebGraphAnalogIn57641AlarmCount_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,1),_WtWebGraphAnalogIn57641AlarmCount_Type())
wtWebGraphAnalogIn57641AlarmCount.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmCount.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmIfTable_Object=MibTable
wtWebGraphAnalogIn57641AlarmIfTable=_WtWebGraphAnalogIn57641AlarmIfTable_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,2))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmIfTable.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmIfEntry_Object=MibTableRow
wtWebGraphAnalogIn57641AlarmIfEntry=_WtWebGraphAnalogIn57641AlarmIfEntry_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,2,1))
wtWebGraphAnalogIn57641AlarmIfEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmIfEntry.setStatus(_A)
class _WtWebGraphAnalogIn57641AlarmNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_WtWebGraphAnalogIn57641AlarmNo_Type.__name__=_D
_WtWebGraphAnalogIn57641AlarmNo_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmNo=_WtWebGraphAnalogIn57641AlarmNo_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,2,1,1),_WtWebGraphAnalogIn57641AlarmNo_Type())
wtWebGraphAnalogIn57641AlarmNo.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmNo.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmTable_Object=MibTable
wtWebGraphAnalogIn57641AlarmTable=_WtWebGraphAnalogIn57641AlarmTable_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmTable.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmEntry_Object=MibTableRow
wtWebGraphAnalogIn57641AlarmEntry=_WtWebGraphAnalogIn57641AlarmEntry_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1))
wtWebGraphAnalogIn57641AlarmEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmEntry.setStatus(_A)
class _WtWebGraphAnalogIn57641AlarmTrigger_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalogIn57641AlarmTrigger_Type.__name__=_F
_WtWebGraphAnalogIn57641AlarmTrigger_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmTrigger=_WtWebGraphAnalogIn57641AlarmTrigger_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,1),_WtWebGraphAnalogIn57641AlarmTrigger_Type())
wtWebGraphAnalogIn57641AlarmTrigger.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmTrigger.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmMin_Type=OctetString
_WtWebGraphAnalogIn57641AlarmMin_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmMin=_WtWebGraphAnalogIn57641AlarmMin_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,2),_WtWebGraphAnalogIn57641AlarmMin_Type())
wtWebGraphAnalogIn57641AlarmMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmMin.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmMax_Type=OctetString
_WtWebGraphAnalogIn57641AlarmMax_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmMax=_WtWebGraphAnalogIn57641AlarmMax_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,3),_WtWebGraphAnalogIn57641AlarmMax_Type())
wtWebGraphAnalogIn57641AlarmMax.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmMax.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmHysteresis_Type=OctetString
_WtWebGraphAnalogIn57641AlarmHysteresis_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmHysteresis=_WtWebGraphAnalogIn57641AlarmHysteresis_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,4),_WtWebGraphAnalogIn57641AlarmHysteresis_Type())
wtWebGraphAnalogIn57641AlarmHysteresis.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmHysteresis.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmDelay_Type=OctetString
_WtWebGraphAnalogIn57641AlarmDelay_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmDelay=_WtWebGraphAnalogIn57641AlarmDelay_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,5),_WtWebGraphAnalogIn57641AlarmDelay_Type())
wtWebGraphAnalogIn57641AlarmDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmDelay.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmInterval_Type=OctetString
_WtWebGraphAnalogIn57641AlarmInterval_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmInterval=_WtWebGraphAnalogIn57641AlarmInterval_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,6),_WtWebGraphAnalogIn57641AlarmInterval_Type())
wtWebGraphAnalogIn57641AlarmInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmInterval.setStatus(_A)
class _WtWebGraphAnalogIn57641AlarmEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalogIn57641AlarmEnable_Type.__name__=_F
_WtWebGraphAnalogIn57641AlarmEnable_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmEnable=_WtWebGraphAnalogIn57641AlarmEnable_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,7),_WtWebGraphAnalogIn57641AlarmEnable_Type())
wtWebGraphAnalogIn57641AlarmEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmEnable.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmEMailAddr_Type=OctetString
_WtWebGraphAnalogIn57641AlarmEMailAddr_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmEMailAddr=_WtWebGraphAnalogIn57641AlarmEMailAddr_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,8),_WtWebGraphAnalogIn57641AlarmEMailAddr_Type())
wtWebGraphAnalogIn57641AlarmEMailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmEMailAddr.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmMailSubject_Type=OctetString
_WtWebGraphAnalogIn57641AlarmMailSubject_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmMailSubject=_WtWebGraphAnalogIn57641AlarmMailSubject_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,9),_WtWebGraphAnalogIn57641AlarmMailSubject_Type())
wtWebGraphAnalogIn57641AlarmMailSubject.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmMailSubject.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmMailText_Type=OctetString
_WtWebGraphAnalogIn57641AlarmMailText_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmMailText=_WtWebGraphAnalogIn57641AlarmMailText_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,10),_WtWebGraphAnalogIn57641AlarmMailText_Type())
wtWebGraphAnalogIn57641AlarmMailText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmMailText.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmManagerIP_Type=OctetString
_WtWebGraphAnalogIn57641AlarmManagerIP_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmManagerIP=_WtWebGraphAnalogIn57641AlarmManagerIP_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,11),_WtWebGraphAnalogIn57641AlarmManagerIP_Type())
wtWebGraphAnalogIn57641AlarmManagerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmManagerIP.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmTrapText_Type=OctetString
_WtWebGraphAnalogIn57641AlarmTrapText_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmTrapText=_WtWebGraphAnalogIn57641AlarmTrapText_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,12),_WtWebGraphAnalogIn57641AlarmTrapText_Type())
wtWebGraphAnalogIn57641AlarmTrapText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmTrapText.setStatus(_A)
class _WtWebGraphAnalogIn57641AlarmMailOptions_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalogIn57641AlarmMailOptions_Type.__name__=_F
_WtWebGraphAnalogIn57641AlarmMailOptions_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmMailOptions=_WtWebGraphAnalogIn57641AlarmMailOptions_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,13),_WtWebGraphAnalogIn57641AlarmMailOptions_Type())
wtWebGraphAnalogIn57641AlarmMailOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmMailOptions.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmTcpIpAddr_Type=OctetString
_WtWebGraphAnalogIn57641AlarmTcpIpAddr_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmTcpIpAddr=_WtWebGraphAnalogIn57641AlarmTcpIpAddr_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,14),_WtWebGraphAnalogIn57641AlarmTcpIpAddr_Type())
wtWebGraphAnalogIn57641AlarmTcpIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmTcpIpAddr.setStatus(_A)
class _WtWebGraphAnalogIn57641AlarmTcpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphAnalogIn57641AlarmTcpPort_Type.__name__=_D
_WtWebGraphAnalogIn57641AlarmTcpPort_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmTcpPort=_WtWebGraphAnalogIn57641AlarmTcpPort_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,15),_WtWebGraphAnalogIn57641AlarmTcpPort_Type())
wtWebGraphAnalogIn57641AlarmTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmTcpPort.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmTcpText_Type=OctetString
_WtWebGraphAnalogIn57641AlarmTcpText_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmTcpText=_WtWebGraphAnalogIn57641AlarmTcpText_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,16),_WtWebGraphAnalogIn57641AlarmTcpText_Type())
wtWebGraphAnalogIn57641AlarmTcpText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmTcpText.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmClearMailSubject_Type=OctetString
_WtWebGraphAnalogIn57641AlarmClearMailSubject_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmClearMailSubject=_WtWebGraphAnalogIn57641AlarmClearMailSubject_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,17),_WtWebGraphAnalogIn57641AlarmClearMailSubject_Type())
wtWebGraphAnalogIn57641AlarmClearMailSubject.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmClearMailSubject.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmClearMailText_Type=OctetString
_WtWebGraphAnalogIn57641AlarmClearMailText_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmClearMailText=_WtWebGraphAnalogIn57641AlarmClearMailText_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,18),_WtWebGraphAnalogIn57641AlarmClearMailText_Type())
wtWebGraphAnalogIn57641AlarmClearMailText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmClearMailText.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmClearTrapText_Type=OctetString
_WtWebGraphAnalogIn57641AlarmClearTrapText_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmClearTrapText=_WtWebGraphAnalogIn57641AlarmClearTrapText_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,19),_WtWebGraphAnalogIn57641AlarmClearTrapText_Type())
wtWebGraphAnalogIn57641AlarmClearTrapText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmClearTrapText.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmClearTcpText_Type=OctetString
_WtWebGraphAnalogIn57641AlarmClearTcpText_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmClearTcpText=_WtWebGraphAnalogIn57641AlarmClearTcpText_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,20),_WtWebGraphAnalogIn57641AlarmClearTcpText_Type())
wtWebGraphAnalogIn57641AlarmClearTcpText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmClearTcpText.setStatus(_A)
_WtWebGraphAnalogIn57641Alarm2Min_Type=OctetString
_WtWebGraphAnalogIn57641Alarm2Min_Object=MibTableColumn
wtWebGraphAnalogIn57641Alarm2Min=_WtWebGraphAnalogIn57641Alarm2Min_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,21),_WtWebGraphAnalogIn57641Alarm2Min_Type())
wtWebGraphAnalogIn57641Alarm2Min.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641Alarm2Min.setStatus(_A)
_WtWebGraphAnalogIn57641Alarm2Max_Type=OctetString
_WtWebGraphAnalogIn57641Alarm2Max_Object=MibTableColumn
wtWebGraphAnalogIn57641Alarm2Max=_WtWebGraphAnalogIn57641Alarm2Max_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,22),_WtWebGraphAnalogIn57641Alarm2Max_Type())
wtWebGraphAnalogIn57641Alarm2Max.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641Alarm2Max.setStatus(_A)
_WtWebGraphAnalogIn57641Alarm2Hysteresis_Type=OctetString
_WtWebGraphAnalogIn57641Alarm2Hysteresis_Object=MibTableColumn
wtWebGraphAnalogIn57641Alarm2Hysteresis=_WtWebGraphAnalogIn57641Alarm2Hysteresis_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,23),_WtWebGraphAnalogIn57641Alarm2Hysteresis_Type())
wtWebGraphAnalogIn57641Alarm2Hysteresis.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641Alarm2Hysteresis.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmSyslogIpAddr_Type=IpAddress
_WtWebGraphAnalogIn57641AlarmSyslogIpAddr_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmSyslogIpAddr=_WtWebGraphAnalogIn57641AlarmSyslogIpAddr_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,24),_WtWebGraphAnalogIn57641AlarmSyslogIpAddr_Type())
wtWebGraphAnalogIn57641AlarmSyslogIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmSyslogIpAddr.setStatus(_A)
class _WtWebGraphAnalogIn57641AlarmSyslogPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphAnalogIn57641AlarmSyslogPort_Type.__name__=_D
_WtWebGraphAnalogIn57641AlarmSyslogPort_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmSyslogPort=_WtWebGraphAnalogIn57641AlarmSyslogPort_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,25),_WtWebGraphAnalogIn57641AlarmSyslogPort_Type())
wtWebGraphAnalogIn57641AlarmSyslogPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmSyslogPort.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmSyslogText_Type=OctetString
_WtWebGraphAnalogIn57641AlarmSyslogText_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmSyslogText=_WtWebGraphAnalogIn57641AlarmSyslogText_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,26),_WtWebGraphAnalogIn57641AlarmSyslogText_Type())
wtWebGraphAnalogIn57641AlarmSyslogText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmSyslogText.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmSyslogClearText_Type=OctetString
_WtWebGraphAnalogIn57641AlarmSyslogClearText_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmSyslogClearText=_WtWebGraphAnalogIn57641AlarmSyslogClearText_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,27),_WtWebGraphAnalogIn57641AlarmSyslogClearText_Type())
wtWebGraphAnalogIn57641AlarmSyslogClearText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmSyslogClearText.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmFtpDataPort_Type=OctetString
_WtWebGraphAnalogIn57641AlarmFtpDataPort_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmFtpDataPort=_WtWebGraphAnalogIn57641AlarmFtpDataPort_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,28),_WtWebGraphAnalogIn57641AlarmFtpDataPort_Type())
wtWebGraphAnalogIn57641AlarmFtpDataPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmFtpDataPort.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmFtpFileName_Type=OctetString
_WtWebGraphAnalogIn57641AlarmFtpFileName_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmFtpFileName=_WtWebGraphAnalogIn57641AlarmFtpFileName_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,29),_WtWebGraphAnalogIn57641AlarmFtpFileName_Type())
wtWebGraphAnalogIn57641AlarmFtpFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmFtpFileName.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmFtpText_Type=OctetString
_WtWebGraphAnalogIn57641AlarmFtpText_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmFtpText=_WtWebGraphAnalogIn57641AlarmFtpText_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,30),_WtWebGraphAnalogIn57641AlarmFtpText_Type())
wtWebGraphAnalogIn57641AlarmFtpText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmFtpText.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmFtpClearText_Type=OctetString
_WtWebGraphAnalogIn57641AlarmFtpClearText_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmFtpClearText=_WtWebGraphAnalogIn57641AlarmFtpClearText_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,31),_WtWebGraphAnalogIn57641AlarmFtpClearText_Type())
wtWebGraphAnalogIn57641AlarmFtpClearText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmFtpClearText.setStatus(_A)
class _WtWebGraphAnalogIn57641AlarmFtpOption_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalogIn57641AlarmFtpOption_Type.__name__=_F
_WtWebGraphAnalogIn57641AlarmFtpOption_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmFtpOption=_WtWebGraphAnalogIn57641AlarmFtpOption_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,32),_WtWebGraphAnalogIn57641AlarmFtpOption_Type())
wtWebGraphAnalogIn57641AlarmFtpOption.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmFtpOption.setStatus(_A)
_WtWebGraphAnalogIn57641AlarmTimerCron_Type=OctetString
_WtWebGraphAnalogIn57641AlarmTimerCron_Object=MibTableColumn
wtWebGraphAnalogIn57641AlarmTimerCron=_WtWebGraphAnalogIn57641AlarmTimerCron_Object((1,3,6,1,4,1,5040,1,2,10,3,1,5,3,1,33),_WtWebGraphAnalogIn57641AlarmTimerCron_Type())
wtWebGraphAnalogIn57641AlarmTimerCron.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlarmTimerCron.setStatus(_A)
_WtWebGraphAnalogIn57641Graphics_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641Graphics=_WtWebGraphAnalogIn57641Graphics_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,3,1,6))
_WtWebGraphAnalogIn57641GraphicsBase_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641GraphicsBase=_WtWebGraphAnalogIn57641GraphicsBase_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,3,1,6,1))
_WtWebGraphAnalogIn57641GraphicsBaseEnable_Type=OctetString
_WtWebGraphAnalogIn57641GraphicsBaseEnable_Object=MibScalar
wtWebGraphAnalogIn57641GraphicsBaseEnable=_WtWebGraphAnalogIn57641GraphicsBaseEnable_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,1,1),_WtWebGraphAnalogIn57641GraphicsBaseEnable_Type())
wtWebGraphAnalogIn57641GraphicsBaseEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641GraphicsBaseEnable.setStatus(_A)
_WtWebGraphAnalogIn57641GraphicsBaseWidth_Type=Integer32
_WtWebGraphAnalogIn57641GraphicsBaseWidth_Object=MibScalar
wtWebGraphAnalogIn57641GraphicsBaseWidth=_WtWebGraphAnalogIn57641GraphicsBaseWidth_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,1,2),_WtWebGraphAnalogIn57641GraphicsBaseWidth_Type())
wtWebGraphAnalogIn57641GraphicsBaseWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641GraphicsBaseWidth.setStatus(_A)
_WtWebGraphAnalogIn57641GraphicsBaseHeight_Type=Integer32
_WtWebGraphAnalogIn57641GraphicsBaseHeight_Object=MibScalar
wtWebGraphAnalogIn57641GraphicsBaseHeight=_WtWebGraphAnalogIn57641GraphicsBaseHeight_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,1,3),_WtWebGraphAnalogIn57641GraphicsBaseHeight_Type())
wtWebGraphAnalogIn57641GraphicsBaseHeight.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641GraphicsBaseHeight.setStatus(_A)
class _WtWebGraphAnalogIn57641GraphicsBaseFrameColor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_WtWebGraphAnalogIn57641GraphicsBaseFrameColor_Type.__name__=_F
_WtWebGraphAnalogIn57641GraphicsBaseFrameColor_Object=MibScalar
wtWebGraphAnalogIn57641GraphicsBaseFrameColor=_WtWebGraphAnalogIn57641GraphicsBaseFrameColor_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,1,4),_WtWebGraphAnalogIn57641GraphicsBaseFrameColor_Type())
wtWebGraphAnalogIn57641GraphicsBaseFrameColor.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641GraphicsBaseFrameColor.setStatus(_A)
class _WtWebGraphAnalogIn57641GraphicsBaseBackgroundColor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_WtWebGraphAnalogIn57641GraphicsBaseBackgroundColor_Type.__name__=_F
_WtWebGraphAnalogIn57641GraphicsBaseBackgroundColor_Object=MibScalar
wtWebGraphAnalogIn57641GraphicsBaseBackgroundColor=_WtWebGraphAnalogIn57641GraphicsBaseBackgroundColor_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,1,5),_WtWebGraphAnalogIn57641GraphicsBaseBackgroundColor_Type())
wtWebGraphAnalogIn57641GraphicsBaseBackgroundColor.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641GraphicsBaseBackgroundColor.setStatus(_A)
_WtWebGraphAnalogIn57641GraphicsBasePollingrate_Type=Integer32
_WtWebGraphAnalogIn57641GraphicsBasePollingrate_Object=MibScalar
wtWebGraphAnalogIn57641GraphicsBasePollingrate=_WtWebGraphAnalogIn57641GraphicsBasePollingrate_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,1,6),_WtWebGraphAnalogIn57641GraphicsBasePollingrate_Type())
wtWebGraphAnalogIn57641GraphicsBasePollingrate.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641GraphicsBasePollingrate.setStatus(_A)
_WtWebGraphAnalogIn57641GraphicsSelect_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641GraphicsSelect=_WtWebGraphAnalogIn57641GraphicsSelect_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,3,1,6,2))
class _WtWebGraphAnalogIn57641GraphicsSelectDisplaySensorSel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalogIn57641GraphicsSelectDisplaySensorSel_Type.__name__=_F
_WtWebGraphAnalogIn57641GraphicsSelectDisplaySensorSel_Object=MibScalar
wtWebGraphAnalogIn57641GraphicsSelectDisplaySensorSel=_WtWebGraphAnalogIn57641GraphicsSelectDisplaySensorSel_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,2,1),_WtWebGraphAnalogIn57641GraphicsSelectDisplaySensorSel_Type())
wtWebGraphAnalogIn57641GraphicsSelectDisplaySensorSel.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641GraphicsSelectDisplaySensorSel.setStatus(_A)
class _WtWebGraphAnalogIn57641GraphicsSelectDisplayShowExtrem_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalogIn57641GraphicsSelectDisplayShowExtrem_Type.__name__=_F
_WtWebGraphAnalogIn57641GraphicsSelectDisplayShowExtrem_Object=MibScalar
wtWebGraphAnalogIn57641GraphicsSelectDisplayShowExtrem=_WtWebGraphAnalogIn57641GraphicsSelectDisplayShowExtrem_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,2,2),_WtWebGraphAnalogIn57641GraphicsSelectDisplayShowExtrem_Type())
wtWebGraphAnalogIn57641GraphicsSelectDisplayShowExtrem.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641GraphicsSelectDisplayShowExtrem.setStatus(_A)
_WtWebGraphAnalogIn57641SensorColor2Table_Object=MibTable
wtWebGraphAnalogIn57641SensorColor2Table=_WtWebGraphAnalogIn57641SensorColor2Table_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,2,3))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SensorColor2Table.setStatus(_A)
_WtWebGraphAnalogIn57641SensorColor2Entry_Object=MibTableRow
wtWebGraphAnalogIn57641SensorColor2Entry=_WtWebGraphAnalogIn57641SensorColor2Entry_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,2,3,1))
wtWebGraphAnalogIn57641SensorColor2Entry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SensorColor2Entry.setStatus(_A)
class _WtWebGraphAnalogIn57641GraphicsSensorColor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_WtWebGraphAnalogIn57641GraphicsSensorColor_Type.__name__=_F
_WtWebGraphAnalogIn57641GraphicsSensorColor_Object=MibTableColumn
wtWebGraphAnalogIn57641GraphicsSensorColor=_WtWebGraphAnalogIn57641GraphicsSensorColor_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,2,3,1,1),_WtWebGraphAnalogIn57641GraphicsSensorColor_Type())
wtWebGraphAnalogIn57641GraphicsSensorColor.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641GraphicsSensorColor.setStatus(_A)
_WtWebGraphAnalogIn57641GraphicsSelectScale_Type=OctetString
_WtWebGraphAnalogIn57641GraphicsSelectScale_Object=MibTableColumn
wtWebGraphAnalogIn57641GraphicsSelectScale=_WtWebGraphAnalogIn57641GraphicsSelectScale_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,2,3,1,2),_WtWebGraphAnalogIn57641GraphicsSelectScale_Type())
wtWebGraphAnalogIn57641GraphicsSelectScale.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641GraphicsSelectScale.setStatus(_A)
_WtWebGraphAnalogIn57641GraphicsScale_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641GraphicsScale=_WtWebGraphAnalogIn57641GraphicsScale_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,3,1,6,3))
_WtWebGraphAnalogIn57641GraphicsScaleAutoScaleEnable_Type=OctetString
_WtWebGraphAnalogIn57641GraphicsScaleAutoScaleEnable_Object=MibScalar
wtWebGraphAnalogIn57641GraphicsScaleAutoScaleEnable=_WtWebGraphAnalogIn57641GraphicsScaleAutoScaleEnable_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,3,1),_WtWebGraphAnalogIn57641GraphicsScaleAutoScaleEnable_Type())
wtWebGraphAnalogIn57641GraphicsScaleAutoScaleEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641GraphicsScaleAutoScaleEnable.setStatus(_A)
_WtWebGraphAnalogIn57641GraphicsScaleAutoFitEnable_Type=OctetString
_WtWebGraphAnalogIn57641GraphicsScaleAutoFitEnable_Object=MibScalar
wtWebGraphAnalogIn57641GraphicsScaleAutoFitEnable=_WtWebGraphAnalogIn57641GraphicsScaleAutoFitEnable_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,3,2),_WtWebGraphAnalogIn57641GraphicsScaleAutoFitEnable_Type())
wtWebGraphAnalogIn57641GraphicsScaleAutoFitEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641GraphicsScaleAutoFitEnable.setStatus(_A)
_WtWebGraphAnalogIn57641GraphicsScale1Min_Type=Integer32
_WtWebGraphAnalogIn57641GraphicsScale1Min_Object=MibScalar
wtWebGraphAnalogIn57641GraphicsScale1Min=_WtWebGraphAnalogIn57641GraphicsScale1Min_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,3,3),_WtWebGraphAnalogIn57641GraphicsScale1Min_Type())
wtWebGraphAnalogIn57641GraphicsScale1Min.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641GraphicsScale1Min.setStatus(_A)
_WtWebGraphAnalogIn57641GraphicsScale2Min_Type=Integer32
_WtWebGraphAnalogIn57641GraphicsScale2Min_Object=MibScalar
wtWebGraphAnalogIn57641GraphicsScale2Min=_WtWebGraphAnalogIn57641GraphicsScale2Min_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,3,4),_WtWebGraphAnalogIn57641GraphicsScale2Min_Type())
wtWebGraphAnalogIn57641GraphicsScale2Min.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641GraphicsScale2Min.setStatus(_A)
_WtWebGraphAnalogIn57641GraphicsScale3Min_Type=Integer32
_WtWebGraphAnalogIn57641GraphicsScale3Min_Object=MibScalar
wtWebGraphAnalogIn57641GraphicsScale3Min=_WtWebGraphAnalogIn57641GraphicsScale3Min_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,3,5),_WtWebGraphAnalogIn57641GraphicsScale3Min_Type())
wtWebGraphAnalogIn57641GraphicsScale3Min.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641GraphicsScale3Min.setStatus(_A)
_WtWebGraphAnalogIn57641GraphicsScale4Min_Type=Integer32
_WtWebGraphAnalogIn57641GraphicsScale4Min_Object=MibScalar
wtWebGraphAnalogIn57641GraphicsScale4Min=_WtWebGraphAnalogIn57641GraphicsScale4Min_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,3,6),_WtWebGraphAnalogIn57641GraphicsScale4Min_Type())
wtWebGraphAnalogIn57641GraphicsScale4Min.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641GraphicsScale4Min.setStatus(_A)
_WtWebGraphAnalogIn57641GraphicsScale1Max_Type=Integer32
_WtWebGraphAnalogIn57641GraphicsScale1Max_Object=MibScalar
wtWebGraphAnalogIn57641GraphicsScale1Max=_WtWebGraphAnalogIn57641GraphicsScale1Max_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,3,7),_WtWebGraphAnalogIn57641GraphicsScale1Max_Type())
wtWebGraphAnalogIn57641GraphicsScale1Max.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641GraphicsScale1Max.setStatus(_A)
_WtWebGraphAnalogIn57641GraphicsScale2Max_Type=Integer32
_WtWebGraphAnalogIn57641GraphicsScale2Max_Object=MibScalar
wtWebGraphAnalogIn57641GraphicsScale2Max=_WtWebGraphAnalogIn57641GraphicsScale2Max_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,3,8),_WtWebGraphAnalogIn57641GraphicsScale2Max_Type())
wtWebGraphAnalogIn57641GraphicsScale2Max.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641GraphicsScale2Max.setStatus(_A)
_WtWebGraphAnalogIn57641GraphicsScale3Max_Type=Integer32
_WtWebGraphAnalogIn57641GraphicsScale3Max_Object=MibScalar
wtWebGraphAnalogIn57641GraphicsScale3Max=_WtWebGraphAnalogIn57641GraphicsScale3Max_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,3,9),_WtWebGraphAnalogIn57641GraphicsScale3Max_Type())
wtWebGraphAnalogIn57641GraphicsScale3Max.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641GraphicsScale3Max.setStatus(_A)
_WtWebGraphAnalogIn57641GraphicsScale4Max_Type=Integer32
_WtWebGraphAnalogIn57641GraphicsScale4Max_Object=MibScalar
wtWebGraphAnalogIn57641GraphicsScale4Max=_WtWebGraphAnalogIn57641GraphicsScale4Max_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,3,10),_WtWebGraphAnalogIn57641GraphicsScale4Max_Type())
wtWebGraphAnalogIn57641GraphicsScale4Max.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641GraphicsScale4Max.setStatus(_A)
_WtWebGraphAnalogIn57641GraphicsScale1Unit_Type=OctetString
_WtWebGraphAnalogIn57641GraphicsScale1Unit_Object=MibScalar
wtWebGraphAnalogIn57641GraphicsScale1Unit=_WtWebGraphAnalogIn57641GraphicsScale1Unit_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,3,11),_WtWebGraphAnalogIn57641GraphicsScale1Unit_Type())
wtWebGraphAnalogIn57641GraphicsScale1Unit.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641GraphicsScale1Unit.setStatus(_A)
_WtWebGraphAnalogIn57641GraphicsScale2Unit_Type=OctetString
_WtWebGraphAnalogIn57641GraphicsScale2Unit_Object=MibScalar
wtWebGraphAnalogIn57641GraphicsScale2Unit=_WtWebGraphAnalogIn57641GraphicsScale2Unit_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,3,12),_WtWebGraphAnalogIn57641GraphicsScale2Unit_Type())
wtWebGraphAnalogIn57641GraphicsScale2Unit.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641GraphicsScale2Unit.setStatus(_A)
_WtWebGraphAnalogIn57641GraphicsScale3Unit_Type=OctetString
_WtWebGraphAnalogIn57641GraphicsScale3Unit_Object=MibScalar
wtWebGraphAnalogIn57641GraphicsScale3Unit=_WtWebGraphAnalogIn57641GraphicsScale3Unit_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,3,13),_WtWebGraphAnalogIn57641GraphicsScale3Unit_Type())
wtWebGraphAnalogIn57641GraphicsScale3Unit.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641GraphicsScale3Unit.setStatus(_A)
_WtWebGraphAnalogIn57641GraphicsScale4Unit_Type=OctetString
_WtWebGraphAnalogIn57641GraphicsScale4Unit_Object=MibScalar
wtWebGraphAnalogIn57641GraphicsScale4Unit=_WtWebGraphAnalogIn57641GraphicsScale4Unit_Object((1,3,6,1,4,1,5040,1,2,10,3,1,6,3,14),_WtWebGraphAnalogIn57641GraphicsScale4Unit_Type())
wtWebGraphAnalogIn57641GraphicsScale4Unit.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641GraphicsScale4Unit.setStatus(_A)
_WtWebGraphAnalogIn57641Ports_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641Ports=_WtWebGraphAnalogIn57641Ports_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,3,2))
_WtWebGraphAnalogIn57641PortTable_Object=MibTable
wtWebGraphAnalogIn57641PortTable=_WtWebGraphAnalogIn57641PortTable_Object((1,3,6,1,4,1,5040,1,2,10,3,2,1))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641PortTable.setStatus(_A)
_WtWebGraphAnalogIn57641PortEntry_Object=MibTableRow
wtWebGraphAnalogIn57641PortEntry=_WtWebGraphAnalogIn57641PortEntry_Object((1,3,6,1,4,1,5040,1,2,10,3,2,1,1))
wtWebGraphAnalogIn57641PortEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641PortEntry.setStatus(_A)
_WtWebGraphAnalogIn57641PortName_Type=OctetString
_WtWebGraphAnalogIn57641PortName_Object=MibTableColumn
wtWebGraphAnalogIn57641PortName=_WtWebGraphAnalogIn57641PortName_Object((1,3,6,1,4,1,5040,1,2,10,3,2,1,1,1),_WtWebGraphAnalogIn57641PortName_Type())
wtWebGraphAnalogIn57641PortName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641PortName.setStatus(_A)
_WtWebGraphAnalogIn57641PortText_Type=OctetString
_WtWebGraphAnalogIn57641PortText_Object=MibTableColumn
wtWebGraphAnalogIn57641PortText=_WtWebGraphAnalogIn57641PortText_Object((1,3,6,1,4,1,5040,1,2,10,3,2,1,1,2),_WtWebGraphAnalogIn57641PortText_Type())
wtWebGraphAnalogIn57641PortText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641PortText.setStatus(_A)
_WtWebGraphAnalogIn57641PortOffset1_Type=OctetString
_WtWebGraphAnalogIn57641PortOffset1_Object=MibTableColumn
wtWebGraphAnalogIn57641PortOffset1=_WtWebGraphAnalogIn57641PortOffset1_Object((1,3,6,1,4,1,5040,1,2,10,3,2,1,1,3),_WtWebGraphAnalogIn57641PortOffset1_Type())
wtWebGraphAnalogIn57641PortOffset1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641PortOffset1.setStatus(_A)
_WtWebGraphAnalogIn57641SetPoint1_Type=OctetString
_WtWebGraphAnalogIn57641SetPoint1_Object=MibTableColumn
wtWebGraphAnalogIn57641SetPoint1=_WtWebGraphAnalogIn57641SetPoint1_Object((1,3,6,1,4,1,5040,1,2,10,3,2,1,1,4),_WtWebGraphAnalogIn57641SetPoint1_Type())
wtWebGraphAnalogIn57641SetPoint1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SetPoint1.setStatus(_A)
_WtWebGraphAnalogIn57641PortOffset2_Type=OctetString
_WtWebGraphAnalogIn57641PortOffset2_Object=MibTableColumn
wtWebGraphAnalogIn57641PortOffset2=_WtWebGraphAnalogIn57641PortOffset2_Object((1,3,6,1,4,1,5040,1,2,10,3,2,1,1,5),_WtWebGraphAnalogIn57641PortOffset2_Type())
wtWebGraphAnalogIn57641PortOffset2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641PortOffset2.setStatus(_A)
_WtWebGraphAnalogIn57641SetPoint2_Type=OctetString
_WtWebGraphAnalogIn57641SetPoint2_Object=MibTableColumn
wtWebGraphAnalogIn57641SetPoint2=_WtWebGraphAnalogIn57641SetPoint2_Object((1,3,6,1,4,1,5040,1,2,10,3,2,1,1,6),_WtWebGraphAnalogIn57641SetPoint2_Type())
wtWebGraphAnalogIn57641SetPoint2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641SetPoint2.setStatus(_A)
_WtWebGraphAnalogIn57641PortComment_Type=OctetString
_WtWebGraphAnalogIn57641PortComment_Object=MibTableColumn
wtWebGraphAnalogIn57641PortComment=_WtWebGraphAnalogIn57641PortComment_Object((1,3,6,1,4,1,5040,1,2,10,3,2,1,1,7),_WtWebGraphAnalogIn57641PortComment_Type())
wtWebGraphAnalogIn57641PortComment.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641PortComment.setStatus(_A)
class _WtWebGraphAnalogIn57641PortSensorSelect_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalogIn57641PortSensorSelect_Type.__name__=_F
_WtWebGraphAnalogIn57641PortSensorSelect_Object=MibTableColumn
wtWebGraphAnalogIn57641PortSensorSelect=_WtWebGraphAnalogIn57641PortSensorSelect_Object((1,3,6,1,4,1,5040,1,2,10,3,2,1,1,8),_WtWebGraphAnalogIn57641PortSensorSelect_Type())
wtWebGraphAnalogIn57641PortSensorSelect.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641PortSensorSelect.setStatus(_A)
_WtWebGraphAnalogIn57641PortUnit_Type=OctetString
_WtWebGraphAnalogIn57641PortUnit_Object=MibTableColumn
wtWebGraphAnalogIn57641PortUnit=_WtWebGraphAnalogIn57641PortUnit_Object((1,3,6,1,4,1,5040,1,2,10,3,2,1,1,9),_WtWebGraphAnalogIn57641PortUnit_Type())
wtWebGraphAnalogIn57641PortUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641PortUnit.setStatus(_A)
_WtWebGraphAnalogIn57641PortScale0_Type=OctetString
_WtWebGraphAnalogIn57641PortScale0_Object=MibTableColumn
wtWebGraphAnalogIn57641PortScale0=_WtWebGraphAnalogIn57641PortScale0_Object((1,3,6,1,4,1,5040,1,2,10,3,2,1,1,10),_WtWebGraphAnalogIn57641PortScale0_Type())
wtWebGraphAnalogIn57641PortScale0.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641PortScale0.setStatus(_A)
_WtWebGraphAnalogIn57641PortScale100_Type=OctetString
_WtWebGraphAnalogIn57641PortScale100_Object=MibTableColumn
wtWebGraphAnalogIn57641PortScale100=_WtWebGraphAnalogIn57641PortScale100_Object((1,3,6,1,4,1,5040,1,2,10,3,2,1,1,11),_WtWebGraphAnalogIn57641PortScale100_Type())
wtWebGraphAnalogIn57641PortScale100.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641PortScale100.setStatus(_A)
_WtWebGraphAnalogIn57641Manufact_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641Manufact=_WtWebGraphAnalogIn57641Manufact_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,3,3))
_WtWebGraphAnalogIn57641MfName_Type=OctetString
_WtWebGraphAnalogIn57641MfName_Object=MibScalar
wtWebGraphAnalogIn57641MfName=_WtWebGraphAnalogIn57641MfName_Object((1,3,6,1,4,1,5040,1,2,10,3,3,1),_WtWebGraphAnalogIn57641MfName_Type())
wtWebGraphAnalogIn57641MfName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641MfName.setStatus(_A)
_WtWebGraphAnalogIn57641MfAddr_Type=OctetString
_WtWebGraphAnalogIn57641MfAddr_Object=MibScalar
wtWebGraphAnalogIn57641MfAddr=_WtWebGraphAnalogIn57641MfAddr_Object((1,3,6,1,4,1,5040,1,2,10,3,3,2),_WtWebGraphAnalogIn57641MfAddr_Type())
wtWebGraphAnalogIn57641MfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641MfAddr.setStatus(_A)
_WtWebGraphAnalogIn57641MfHotline_Type=OctetString
_WtWebGraphAnalogIn57641MfHotline_Object=MibScalar
wtWebGraphAnalogIn57641MfHotline=_WtWebGraphAnalogIn57641MfHotline_Object((1,3,6,1,4,1,5040,1,2,10,3,3,3),_WtWebGraphAnalogIn57641MfHotline_Type())
wtWebGraphAnalogIn57641MfHotline.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641MfHotline.setStatus(_A)
_WtWebGraphAnalogIn57641MfInternet_Type=OctetString
_WtWebGraphAnalogIn57641MfInternet_Object=MibScalar
wtWebGraphAnalogIn57641MfInternet=_WtWebGraphAnalogIn57641MfInternet_Object((1,3,6,1,4,1,5040,1,2,10,3,3,4),_WtWebGraphAnalogIn57641MfInternet_Type())
wtWebGraphAnalogIn57641MfInternet.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641MfInternet.setStatus(_A)
_WtWebGraphAnalogIn57641MfDeviceTyp_Type=OctetString
_WtWebGraphAnalogIn57641MfDeviceTyp_Object=MibScalar
wtWebGraphAnalogIn57641MfDeviceTyp=_WtWebGraphAnalogIn57641MfDeviceTyp_Object((1,3,6,1,4,1,5040,1,2,10,3,3,5),_WtWebGraphAnalogIn57641MfDeviceTyp_Type())
wtWebGraphAnalogIn57641MfDeviceTyp.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641MfDeviceTyp.setStatus(_A)
_WtWebGraphAnalogIn57641MfOrderNo_Type=OctetString
_WtWebGraphAnalogIn57641MfOrderNo_Object=MibScalar
wtWebGraphAnalogIn57641MfOrderNo=_WtWebGraphAnalogIn57641MfOrderNo_Object((1,3,6,1,4,1,5040,1,2,10,3,3,6),_WtWebGraphAnalogIn57641MfOrderNo_Type())
wtWebGraphAnalogIn57641MfOrderNo.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641MfOrderNo.setStatus(_A)
_WtWebGraphAnalogIn57641Diag_ObjectIdentity=ObjectIdentity
wtWebGraphAnalogIn57641Diag=_WtWebGraphAnalogIn57641Diag_ObjectIdentity((1,3,6,1,4,1,5040,1,2,10,4))
_WtWebGraphAnalogIn57641DiagErrorCount_Type=Integer32
_WtWebGraphAnalogIn57641DiagErrorCount_Object=MibScalar
wtWebGraphAnalogIn57641DiagErrorCount=_WtWebGraphAnalogIn57641DiagErrorCount_Object((1,3,6,1,4,1,5040,1,2,10,4,1),_WtWebGraphAnalogIn57641DiagErrorCount_Type())
wtWebGraphAnalogIn57641DiagErrorCount.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641DiagErrorCount.setStatus(_A)
_WtWebGraphAnalogIn57641DiagBinaryError_Type=OctetString
_WtWebGraphAnalogIn57641DiagBinaryError_Object=MibScalar
wtWebGraphAnalogIn57641DiagBinaryError=_WtWebGraphAnalogIn57641DiagBinaryError_Object((1,3,6,1,4,1,5040,1,2,10,4,2),_WtWebGraphAnalogIn57641DiagBinaryError_Type())
wtWebGraphAnalogIn57641DiagBinaryError.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641DiagBinaryError.setStatus(_A)
_WtWebGraphAnalogIn57641DiagErrorIndex_Type=Integer32
_WtWebGraphAnalogIn57641DiagErrorIndex_Object=MibScalar
wtWebGraphAnalogIn57641DiagErrorIndex=_WtWebGraphAnalogIn57641DiagErrorIndex_Object((1,3,6,1,4,1,5040,1,2,10,4,3),_WtWebGraphAnalogIn57641DiagErrorIndex_Type())
wtWebGraphAnalogIn57641DiagErrorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641DiagErrorIndex.setStatus(_A)
_WtWebGraphAnalogIn57641DiagErrorMessage_Type=OctetString
_WtWebGraphAnalogIn57641DiagErrorMessage_Object=MibScalar
wtWebGraphAnalogIn57641DiagErrorMessage=_WtWebGraphAnalogIn57641DiagErrorMessage_Object((1,3,6,1,4,1,5040,1,2,10,4,4),_WtWebGraphAnalogIn57641DiagErrorMessage_Type())
wtWebGraphAnalogIn57641DiagErrorMessage.setMaxAccess(_E)
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641DiagErrorMessage.setStatus(_A)
_WtWebGraphAnalogIn57641DiagErrorClear_Type=Integer32
_WtWebGraphAnalogIn57641DiagErrorClear_Object=MibScalar
wtWebGraphAnalogIn57641DiagErrorClear=_WtWebGraphAnalogIn57641DiagErrorClear_Object((1,3,6,1,4,1,5040,1,2,10,4,5),_WtWebGraphAnalogIn57641DiagErrorClear_Type())
wtWebGraphAnalogIn57641DiagErrorClear.setMaxAccess('write-only')
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641DiagErrorClear.setStatus(_A)
wtWebGraphAnalogIn57641Alert1=NotificationType((1,3,6,1,4,1,5040,1,2,10,0,31))
wtWebGraphAnalogIn57641Alert1.setObjects((_C,_G))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641Alert1.setStatus('')
wtWebGraphAnalogIn57641Alert2=NotificationType((1,3,6,1,4,1,5040,1,2,10,0,32))
wtWebGraphAnalogIn57641Alert2.setObjects((_C,_G))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641Alert2.setStatus('')
wtWebGraphAnalogIn57641Alert3=NotificationType((1,3,6,1,4,1,5040,1,2,10,0,33))
wtWebGraphAnalogIn57641Alert3.setObjects((_C,_G))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641Alert3.setStatus('')
wtWebGraphAnalogIn57641Alert4=NotificationType((1,3,6,1,4,1,5040,1,2,10,0,34))
wtWebGraphAnalogIn57641Alert4.setObjects((_C,_G))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641Alert4.setStatus('')
wtWebGraphAnalogIn57641Alert5=NotificationType((1,3,6,1,4,1,5040,1,2,10,0,35))
wtWebGraphAnalogIn57641Alert5.setObjects((_C,_G))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641Alert5.setStatus('')
wtWebGraphAnalogIn57641Alert6=NotificationType((1,3,6,1,4,1,5040,1,2,10,0,36))
wtWebGraphAnalogIn57641Alert6.setObjects((_C,_G))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641Alert6.setStatus('')
wtWebGraphAnalogIn57641Alert7=NotificationType((1,3,6,1,4,1,5040,1,2,10,0,37))
wtWebGraphAnalogIn57641Alert7.setObjects((_C,_G))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641Alert7.setStatus('')
wtWebGraphAnalogIn57641Alert8=NotificationType((1,3,6,1,4,1,5040,1,2,10,0,38))
wtWebGraphAnalogIn57641Alert8.setObjects((_C,_G))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641Alert8.setStatus('')
wtWebGraphAnalogIn57641Alert9=NotificationType((1,3,6,1,4,1,5040,1,2,10,0,91))
wtWebGraphAnalogIn57641Alert9.setObjects((_C,_H))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641Alert9.setStatus('')
wtWebGraphAnalogIn57641Alert10=NotificationType((1,3,6,1,4,1,5040,1,2,10,0,92))
wtWebGraphAnalogIn57641Alert10.setObjects((_C,_H))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641Alert10.setStatus('')
wtWebGraphAnalogIn57641Alert11=NotificationType((1,3,6,1,4,1,5040,1,2,10,0,93))
wtWebGraphAnalogIn57641Alert11.setObjects((_C,_H))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641Alert11.setStatus('')
wtWebGraphAnalogIn57641Alert12=NotificationType((1,3,6,1,4,1,5040,1,2,10,0,94))
wtWebGraphAnalogIn57641Alert12.setObjects((_C,_H))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641Alert12.setStatus('')
wtWebGraphAnalogIn57641Alert13=NotificationType((1,3,6,1,4,1,5040,1,2,10,0,95))
wtWebGraphAnalogIn57641Alert13.setObjects((_C,_H))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641Alert13.setStatus('')
wtWebGraphAnalogIn57641Alert14=NotificationType((1,3,6,1,4,1,5040,1,2,10,0,96))
wtWebGraphAnalogIn57641Alert14.setObjects((_C,_H))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641Alert14.setStatus('')
wtWebGraphAnalogIn57641Alert15=NotificationType((1,3,6,1,4,1,5040,1,2,10,0,97))
wtWebGraphAnalogIn57641Alert15.setObjects((_C,_H))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641Alert15.setStatus('')
wtWebGraphAnalogIn57641Alert16=NotificationType((1,3,6,1,4,1,5040,1,2,10,0,98))
wtWebGraphAnalogIn57641Alert16.setObjects((_C,_H))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641Alert16.setStatus('')
wtWebGraphAnalogIn57641AlertDiag=NotificationType((1,3,6,1,4,1,5040,1,2,10,0,110))
wtWebGraphAnalogIn57641AlertDiag.setObjects(*((_C,_L),(_C,_M)))
if mibBuilder.loadTexts:wtWebGraphAnalogIn57641AlertDiag.setStatus('')
mibBuilder.exportSymbols(_C,**{'wut':wut,'wtComServer':wtComServer,'wtWebio':wtWebio,'wtWebGraphAnalogIn57641':wtWebGraphAnalogIn57641,'wtWebGraphAnalogIn57641Alert1':wtWebGraphAnalogIn57641Alert1,'wtWebGraphAnalogIn57641Alert2':wtWebGraphAnalogIn57641Alert2,'wtWebGraphAnalogIn57641Alert3':wtWebGraphAnalogIn57641Alert3,'wtWebGraphAnalogIn57641Alert4':wtWebGraphAnalogIn57641Alert4,'wtWebGraphAnalogIn57641Alert5':wtWebGraphAnalogIn57641Alert5,'wtWebGraphAnalogIn57641Alert6':wtWebGraphAnalogIn57641Alert6,'wtWebGraphAnalogIn57641Alert7':wtWebGraphAnalogIn57641Alert7,'wtWebGraphAnalogIn57641Alert8':wtWebGraphAnalogIn57641Alert8,'wtWebGraphAnalogIn57641Alert9':wtWebGraphAnalogIn57641Alert9,'wtWebGraphAnalogIn57641Alert10':wtWebGraphAnalogIn57641Alert10,'wtWebGraphAnalogIn57641Alert11':wtWebGraphAnalogIn57641Alert11,'wtWebGraphAnalogIn57641Alert12':wtWebGraphAnalogIn57641Alert12,'wtWebGraphAnalogIn57641Alert13':wtWebGraphAnalogIn57641Alert13,'wtWebGraphAnalogIn57641Alert14':wtWebGraphAnalogIn57641Alert14,'wtWebGraphAnalogIn57641Alert15':wtWebGraphAnalogIn57641Alert15,'wtWebGraphAnalogIn57641Alert16':wtWebGraphAnalogIn57641Alert16,'wtWebGraphAnalogIn57641AlertDiag':wtWebGraphAnalogIn57641AlertDiag,'wtWebGraphAnalogIn57641Inventory':wtWebGraphAnalogIn57641Inventory,'wtWebGraphAnalogIn57641Sensors':wtWebGraphAnalogIn57641Sensors,'wtWebGraphAnalogIn57641SensorTable':wtWebGraphAnalogIn57641SensorTable,'wtWebGraphAnalogIn57641SensorEntry':wtWebGraphAnalogIn57641SensorEntry,_I:wtWebGraphAnalogIn57641SensorNo,'wtWebGraphAnalogIn57641ValuesTable':wtWebGraphAnalogIn57641ValuesTable,'wtWebGraphAnalogIn57641ValuesEntry':wtWebGraphAnalogIn57641ValuesEntry,'wtWebGraphAnalogIn57641Values':wtWebGraphAnalogIn57641Values,'wtWebGraphAnalogIn57641BinaryValuesTable':wtWebGraphAnalogIn57641BinaryValuesTable,'wtWebGraphAnalogIn57641BinaryValuesEntry':wtWebGraphAnalogIn57641BinaryValuesEntry,'wtWebGraphAnalogIn57641BinaryValues':wtWebGraphAnalogIn57641BinaryValues,'wtWebGraphAnalogIn57641SessCntrl':wtWebGraphAnalogIn57641SessCntrl,'wtWebGraphAnalogIn57641SessCntrlPassword':wtWebGraphAnalogIn57641SessCntrlPassword,'wtWebGraphAnalogIn57641SessCntrlConfigMode':wtWebGraphAnalogIn57641SessCntrlConfigMode,'wtWebGraphAnalogIn57641SessCntrlLogout':wtWebGraphAnalogIn57641SessCntrlLogout,'wtWebGraphAnalogIn57641SessCntrlAdminPassword':wtWebGraphAnalogIn57641SessCntrlAdminPassword,'wtWebGraphAnalogIn57641SessCntrlConfigPassword':wtWebGraphAnalogIn57641SessCntrlConfigPassword,'wtWebGraphAnalogIn57641Config':wtWebGraphAnalogIn57641Config,'wtWebGraphAnalogIn57641Device':wtWebGraphAnalogIn57641Device,'wtWebGraphAnalogIn57641Text':wtWebGraphAnalogIn57641Text,'wtWebGraphAnalogIn57641DeviceName':wtWebGraphAnalogIn57641DeviceName,'wtWebGraphAnalogIn57641DeviceText':wtWebGraphAnalogIn57641DeviceText,'wtWebGraphAnalogIn57641DeviceLocation':wtWebGraphAnalogIn57641DeviceLocation,'wtWebGraphAnalogIn57641DeviceContact':wtWebGraphAnalogIn57641DeviceContact,'wtWebGraphAnalogIn57641TimeDate':wtWebGraphAnalogIn57641TimeDate,'wtWebGraphAnalogIn57641TimeZone':wtWebGraphAnalogIn57641TimeZone,'wtWebGraphAnalogIn57641TzOffsetHrs':wtWebGraphAnalogIn57641TzOffsetHrs,'wtWebGraphAnalogIn57641TzOffsetMin':wtWebGraphAnalogIn57641TzOffsetMin,'wtWebGraphAnalogIn57641TzEnable':wtWebGraphAnalogIn57641TzEnable,'wtWebGraphAnalogIn57641StTzOffsetHrs':wtWebGraphAnalogIn57641StTzOffsetHrs,'wtWebGraphAnalogIn57641StTzOffsetMin':wtWebGraphAnalogIn57641StTzOffsetMin,'wtWebGraphAnalogIn57641StTzEnable':wtWebGraphAnalogIn57641StTzEnable,'wtWebGraphAnalogIn57641StTzStartMonth':wtWebGraphAnalogIn57641StTzStartMonth,'wtWebGraphAnalogIn57641StTzStartMode':wtWebGraphAnalogIn57641StTzStartMode,'wtWebGraphAnalogIn57641StTzStartWday':wtWebGraphAnalogIn57641StTzStartWday,'wtWebGraphAnalogIn57641StTzStartHrs':wtWebGraphAnalogIn57641StTzStartHrs,'wtWebGraphAnalogIn57641StTzStartMin':wtWebGraphAnalogIn57641StTzStartMin,'wtWebGraphAnalogIn57641StTzStopMonth':wtWebGraphAnalogIn57641StTzStopMonth,'wtWebGraphAnalogIn57641StTzStopMode':wtWebGraphAnalogIn57641StTzStopMode,'wtWebGraphAnalogIn57641StTzStopWday':wtWebGraphAnalogIn57641StTzStopWday,'wtWebGraphAnalogIn57641StTzStopHrs':wtWebGraphAnalogIn57641StTzStopHrs,'wtWebGraphAnalogIn57641StTzStopMin':wtWebGraphAnalogIn57641StTzStopMin,'wtWebGraphAnalogIn57641TimeServer':wtWebGraphAnalogIn57641TimeServer,'wtWebGraphAnalogIn57641TimeServer1':wtWebGraphAnalogIn57641TimeServer1,'wtWebGraphAnalogIn57641TimeServer2':wtWebGraphAnalogIn57641TimeServer2,'wtWebGraphAnalogIn57641TsEnable':wtWebGraphAnalogIn57641TsEnable,'wtWebGraphAnalogIn57641TsSyncTime':wtWebGraphAnalogIn57641TsSyncTime,'wtWebGraphAnalogIn57641DeviceClock':wtWebGraphAnalogIn57641DeviceClock,'wtWebGraphAnalogIn57641ClockHrs':wtWebGraphAnalogIn57641ClockHrs,'wtWebGraphAnalogIn57641ClockMin':wtWebGraphAnalogIn57641ClockMin,'wtWebGraphAnalogIn57641ClockDay':wtWebGraphAnalogIn57641ClockDay,'wtWebGraphAnalogIn57641ClockMonth':wtWebGraphAnalogIn57641ClockMonth,'wtWebGraphAnalogIn57641ClockYear':wtWebGraphAnalogIn57641ClockYear,'wtWebGraphAnalogIn57641Basic':wtWebGraphAnalogIn57641Basic,'wtWebGraphAnalogIn57641Network':wtWebGraphAnalogIn57641Network,'wtWebGraphAnalogIn57641IpAddress':wtWebGraphAnalogIn57641IpAddress,'wtWebGraphAnalogIn57641SubnetMask':wtWebGraphAnalogIn57641SubnetMask,'wtWebGraphAnalogIn57641Gateway':wtWebGraphAnalogIn57641Gateway,'wtWebGraphAnalogIn57641DnsServer1':wtWebGraphAnalogIn57641DnsServer1,'wtWebGraphAnalogIn57641DnsServer2':wtWebGraphAnalogIn57641DnsServer2,'wtWebGraphAnalogIn57641AddConfig':wtWebGraphAnalogIn57641AddConfig,'wtWebGraphAnalogIn57641HTTP':wtWebGraphAnalogIn57641HTTP,'wtWebGraphAnalogIn57641Startup':wtWebGraphAnalogIn57641Startup,'wtWebGraphAnalogIn57641GetHeaderEnable':wtWebGraphAnalogIn57641GetHeaderEnable,'wtWebGraphAnalogIn57641HttpPort':wtWebGraphAnalogIn57641HttpPort,'wtWebGraphAnalogIn57641Mail':wtWebGraphAnalogIn57641Mail,'wtWebGraphAnalogIn57641MailAdName':wtWebGraphAnalogIn57641MailAdName,'wtWebGraphAnalogIn57641MailReply':wtWebGraphAnalogIn57641MailReply,'wtWebGraphAnalogIn57641MailServer':wtWebGraphAnalogIn57641MailServer,'wtWebioAn1MailEnable':wtWebioAn1MailEnable,'wtWebGraphAnalogIn57641MailAuthentication':wtWebGraphAnalogIn57641MailAuthentication,'wtWebGraphAnalogIn57641MailAuthUser':wtWebGraphAnalogIn57641MailAuthUser,'wtWebGraphAnalogIn57641MailAuthPassword':wtWebGraphAnalogIn57641MailAuthPassword,'wtWebGraphAnalogIn57641MailPop3Server':wtWebGraphAnalogIn57641MailPop3Server,'wtWebGraphAnalogIn57641SNMP':wtWebGraphAnalogIn57641SNMP,'wtWebGraphAnalogIn57641SnmpCommunityStringRead':wtWebGraphAnalogIn57641SnmpCommunityStringRead,'wtWebGraphAnalogIn57641SnmpCommunityStringReadWrite':wtWebGraphAnalogIn57641SnmpCommunityStringReadWrite,'wtWebGraphAnalogIn57641SystemTrapManagerIP':wtWebGraphAnalogIn57641SystemTrapManagerIP,'wtWebGraphAnalogIn57641SystemTrapEnable':wtWebGraphAnalogIn57641SystemTrapEnable,'wtWebGraphAnalogIn57641SnmpEnable':wtWebGraphAnalogIn57641SnmpEnable,'wtWebGraphAnalogIn57641SnmpCommunityStringTrap':wtWebGraphAnalogIn57641SnmpCommunityStringTrap,'wtWebGraphAnalogIn57641UDP':wtWebGraphAnalogIn57641UDP,'wtWebGraphAnalogIn57641UdpPort':wtWebGraphAnalogIn57641UdpPort,'wtWebGraphAnalogIn57641UdpEnable':wtWebGraphAnalogIn57641UdpEnable,'wtWebGraphAnalogIn57641Syslog':wtWebGraphAnalogIn57641Syslog,'wtWebGraphAnalogIn57641SyslogServerIP':wtWebGraphAnalogIn57641SyslogServerIP,'wtWebGraphAnalogIn57641SyslogServerPort':wtWebGraphAnalogIn57641SyslogServerPort,'wtWebGraphAnalogIn57641SyslogSystemMessagesEnable':wtWebGraphAnalogIn57641SyslogSystemMessagesEnable,'wtWebGraphAnalogIn57641SyslogEnable':wtWebGraphAnalogIn57641SyslogEnable,'wtWebGraphAnalogIn57641FTP':wtWebGraphAnalogIn57641FTP,'wtWebGraphAnalogIn57641FTPServerIP':wtWebGraphAnalogIn57641FTPServerIP,'wtWebGraphAnalogIn57641FTPServerControlPort':wtWebGraphAnalogIn57641FTPServerControlPort,'wtWebGraphAnalogIn57641FTPUserName':wtWebGraphAnalogIn57641FTPUserName,'wtWebGraphAnalogIn57641FTPPassword':wtWebGraphAnalogIn57641FTPPassword,'wtWebGraphAnalogIn57641FTPAccount':wtWebGraphAnalogIn57641FTPAccount,'wtWebGraphAnalogIn57641FTPOption':wtWebGraphAnalogIn57641FTPOption,'wtWebGraphAnalogIn57641FTPEnable':wtWebGraphAnalogIn57641FTPEnable,'wtWebGraphAnalogIn57641Datalogger':wtWebGraphAnalogIn57641Datalogger,'wtWebGraphAnalogIn57641LoggerTimebase':wtWebGraphAnalogIn57641LoggerTimebase,'wtWebGraphAnalogIn57641LoggerSensorSel':wtWebGraphAnalogIn57641LoggerSensorSel,'wtWebGraphAnalogIn57641DisplaySensorSel':wtWebGraphAnalogIn57641DisplaySensorSel,'wtWebGraphAnalogIn57641SensorColorTable':wtWebGraphAnalogIn57641SensorColorTable,'wtWebGraphAnalogIn57641SensorColorEntry':wtWebGraphAnalogIn57641SensorColorEntry,'wtWebGraphAnalogIn57641SensorColor':wtWebGraphAnalogIn57641SensorColor,'wtWebGraphAnalogIn57641AutoScaleEnable':wtWebGraphAnalogIn57641AutoScaleEnable,'wtWebGraphAnalogIn57641VerticalUpperLimit':wtWebGraphAnalogIn57641VerticalUpperLimit,'wtWebGraphAnalogIn57641VerticalLowerLimit':wtWebGraphAnalogIn57641VerticalLowerLimit,'wtWebGraphAnalogIn57641HorizontalZoom':wtWebGraphAnalogIn57641HorizontalZoom,'wtWebGraphAnalogIn57641Alarm':wtWebGraphAnalogIn57641Alarm,'wtWebGraphAnalogIn57641AlarmCount':wtWebGraphAnalogIn57641AlarmCount,'wtWebGraphAnalogIn57641AlarmIfTable':wtWebGraphAnalogIn57641AlarmIfTable,'wtWebGraphAnalogIn57641AlarmIfEntry':wtWebGraphAnalogIn57641AlarmIfEntry,_J:wtWebGraphAnalogIn57641AlarmNo,'wtWebGraphAnalogIn57641AlarmTable':wtWebGraphAnalogIn57641AlarmTable,'wtWebGraphAnalogIn57641AlarmEntry':wtWebGraphAnalogIn57641AlarmEntry,'wtWebGraphAnalogIn57641AlarmTrigger':wtWebGraphAnalogIn57641AlarmTrigger,'wtWebGraphAnalogIn57641AlarmMin':wtWebGraphAnalogIn57641AlarmMin,'wtWebGraphAnalogIn57641AlarmMax':wtWebGraphAnalogIn57641AlarmMax,'wtWebGraphAnalogIn57641AlarmHysteresis':wtWebGraphAnalogIn57641AlarmHysteresis,'wtWebGraphAnalogIn57641AlarmDelay':wtWebGraphAnalogIn57641AlarmDelay,'wtWebGraphAnalogIn57641AlarmInterval':wtWebGraphAnalogIn57641AlarmInterval,'wtWebGraphAnalogIn57641AlarmEnable':wtWebGraphAnalogIn57641AlarmEnable,'wtWebGraphAnalogIn57641AlarmEMailAddr':wtWebGraphAnalogIn57641AlarmEMailAddr,'wtWebGraphAnalogIn57641AlarmMailSubject':wtWebGraphAnalogIn57641AlarmMailSubject,'wtWebGraphAnalogIn57641AlarmMailText':wtWebGraphAnalogIn57641AlarmMailText,'wtWebGraphAnalogIn57641AlarmManagerIP':wtWebGraphAnalogIn57641AlarmManagerIP,_G:wtWebGraphAnalogIn57641AlarmTrapText,'wtWebGraphAnalogIn57641AlarmMailOptions':wtWebGraphAnalogIn57641AlarmMailOptions,'wtWebGraphAnalogIn57641AlarmTcpIpAddr':wtWebGraphAnalogIn57641AlarmTcpIpAddr,'wtWebGraphAnalogIn57641AlarmTcpPort':wtWebGraphAnalogIn57641AlarmTcpPort,'wtWebGraphAnalogIn57641AlarmTcpText':wtWebGraphAnalogIn57641AlarmTcpText,'wtWebGraphAnalogIn57641AlarmClearMailSubject':wtWebGraphAnalogIn57641AlarmClearMailSubject,'wtWebGraphAnalogIn57641AlarmClearMailText':wtWebGraphAnalogIn57641AlarmClearMailText,_H:wtWebGraphAnalogIn57641AlarmClearTrapText,'wtWebGraphAnalogIn57641AlarmClearTcpText':wtWebGraphAnalogIn57641AlarmClearTcpText,'wtWebGraphAnalogIn57641Alarm2Min':wtWebGraphAnalogIn57641Alarm2Min,'wtWebGraphAnalogIn57641Alarm2Max':wtWebGraphAnalogIn57641Alarm2Max,'wtWebGraphAnalogIn57641Alarm2Hysteresis':wtWebGraphAnalogIn57641Alarm2Hysteresis,'wtWebGraphAnalogIn57641AlarmSyslogIpAddr':wtWebGraphAnalogIn57641AlarmSyslogIpAddr,'wtWebGraphAnalogIn57641AlarmSyslogPort':wtWebGraphAnalogIn57641AlarmSyslogPort,'wtWebGraphAnalogIn57641AlarmSyslogText':wtWebGraphAnalogIn57641AlarmSyslogText,'wtWebGraphAnalogIn57641AlarmSyslogClearText':wtWebGraphAnalogIn57641AlarmSyslogClearText,'wtWebGraphAnalogIn57641AlarmFtpDataPort':wtWebGraphAnalogIn57641AlarmFtpDataPort,'wtWebGraphAnalogIn57641AlarmFtpFileName':wtWebGraphAnalogIn57641AlarmFtpFileName,'wtWebGraphAnalogIn57641AlarmFtpText':wtWebGraphAnalogIn57641AlarmFtpText,'wtWebGraphAnalogIn57641AlarmFtpClearText':wtWebGraphAnalogIn57641AlarmFtpClearText,'wtWebGraphAnalogIn57641AlarmFtpOption':wtWebGraphAnalogIn57641AlarmFtpOption,'wtWebGraphAnalogIn57641AlarmTimerCron':wtWebGraphAnalogIn57641AlarmTimerCron,'wtWebGraphAnalogIn57641Graphics':wtWebGraphAnalogIn57641Graphics,'wtWebGraphAnalogIn57641GraphicsBase':wtWebGraphAnalogIn57641GraphicsBase,'wtWebGraphAnalogIn57641GraphicsBaseEnable':wtWebGraphAnalogIn57641GraphicsBaseEnable,'wtWebGraphAnalogIn57641GraphicsBaseWidth':wtWebGraphAnalogIn57641GraphicsBaseWidth,'wtWebGraphAnalogIn57641GraphicsBaseHeight':wtWebGraphAnalogIn57641GraphicsBaseHeight,'wtWebGraphAnalogIn57641GraphicsBaseFrameColor':wtWebGraphAnalogIn57641GraphicsBaseFrameColor,'wtWebGraphAnalogIn57641GraphicsBaseBackgroundColor':wtWebGraphAnalogIn57641GraphicsBaseBackgroundColor,'wtWebGraphAnalogIn57641GraphicsBasePollingrate':wtWebGraphAnalogIn57641GraphicsBasePollingrate,'wtWebGraphAnalogIn57641GraphicsSelect':wtWebGraphAnalogIn57641GraphicsSelect,'wtWebGraphAnalogIn57641GraphicsSelectDisplaySensorSel':wtWebGraphAnalogIn57641GraphicsSelectDisplaySensorSel,'wtWebGraphAnalogIn57641GraphicsSelectDisplayShowExtrem':wtWebGraphAnalogIn57641GraphicsSelectDisplayShowExtrem,'wtWebGraphAnalogIn57641SensorColor2Table':wtWebGraphAnalogIn57641SensorColor2Table,'wtWebGraphAnalogIn57641SensorColor2Entry':wtWebGraphAnalogIn57641SensorColor2Entry,'wtWebGraphAnalogIn57641GraphicsSensorColor':wtWebGraphAnalogIn57641GraphicsSensorColor,'wtWebGraphAnalogIn57641GraphicsSelectScale':wtWebGraphAnalogIn57641GraphicsSelectScale,'wtWebGraphAnalogIn57641GraphicsScale':wtWebGraphAnalogIn57641GraphicsScale,'wtWebGraphAnalogIn57641GraphicsScaleAutoScaleEnable':wtWebGraphAnalogIn57641GraphicsScaleAutoScaleEnable,'wtWebGraphAnalogIn57641GraphicsScaleAutoFitEnable':wtWebGraphAnalogIn57641GraphicsScaleAutoFitEnable,'wtWebGraphAnalogIn57641GraphicsScale1Min':wtWebGraphAnalogIn57641GraphicsScale1Min,'wtWebGraphAnalogIn57641GraphicsScale2Min':wtWebGraphAnalogIn57641GraphicsScale2Min,'wtWebGraphAnalogIn57641GraphicsScale3Min':wtWebGraphAnalogIn57641GraphicsScale3Min,'wtWebGraphAnalogIn57641GraphicsScale4Min':wtWebGraphAnalogIn57641GraphicsScale4Min,'wtWebGraphAnalogIn57641GraphicsScale1Max':wtWebGraphAnalogIn57641GraphicsScale1Max,'wtWebGraphAnalogIn57641GraphicsScale2Max':wtWebGraphAnalogIn57641GraphicsScale2Max,'wtWebGraphAnalogIn57641GraphicsScale3Max':wtWebGraphAnalogIn57641GraphicsScale3Max,'wtWebGraphAnalogIn57641GraphicsScale4Max':wtWebGraphAnalogIn57641GraphicsScale4Max,'wtWebGraphAnalogIn57641GraphicsScale1Unit':wtWebGraphAnalogIn57641GraphicsScale1Unit,'wtWebGraphAnalogIn57641GraphicsScale2Unit':wtWebGraphAnalogIn57641GraphicsScale2Unit,'wtWebGraphAnalogIn57641GraphicsScale3Unit':wtWebGraphAnalogIn57641GraphicsScale3Unit,'wtWebGraphAnalogIn57641GraphicsScale4Unit':wtWebGraphAnalogIn57641GraphicsScale4Unit,'wtWebGraphAnalogIn57641Ports':wtWebGraphAnalogIn57641Ports,'wtWebGraphAnalogIn57641PortTable':wtWebGraphAnalogIn57641PortTable,'wtWebGraphAnalogIn57641PortEntry':wtWebGraphAnalogIn57641PortEntry,'wtWebGraphAnalogIn57641PortName':wtWebGraphAnalogIn57641PortName,'wtWebGraphAnalogIn57641PortText':wtWebGraphAnalogIn57641PortText,'wtWebGraphAnalogIn57641PortOffset1':wtWebGraphAnalogIn57641PortOffset1,'wtWebGraphAnalogIn57641SetPoint1':wtWebGraphAnalogIn57641SetPoint1,'wtWebGraphAnalogIn57641PortOffset2':wtWebGraphAnalogIn57641PortOffset2,'wtWebGraphAnalogIn57641SetPoint2':wtWebGraphAnalogIn57641SetPoint2,'wtWebGraphAnalogIn57641PortComment':wtWebGraphAnalogIn57641PortComment,'wtWebGraphAnalogIn57641PortSensorSelect':wtWebGraphAnalogIn57641PortSensorSelect,'wtWebGraphAnalogIn57641PortUnit':wtWebGraphAnalogIn57641PortUnit,'wtWebGraphAnalogIn57641PortScale0':wtWebGraphAnalogIn57641PortScale0,'wtWebGraphAnalogIn57641PortScale100':wtWebGraphAnalogIn57641PortScale100,'wtWebGraphAnalogIn57641Manufact':wtWebGraphAnalogIn57641Manufact,'wtWebGraphAnalogIn57641MfName':wtWebGraphAnalogIn57641MfName,'wtWebGraphAnalogIn57641MfAddr':wtWebGraphAnalogIn57641MfAddr,'wtWebGraphAnalogIn57641MfHotline':wtWebGraphAnalogIn57641MfHotline,'wtWebGraphAnalogIn57641MfInternet':wtWebGraphAnalogIn57641MfInternet,'wtWebGraphAnalogIn57641MfDeviceTyp':wtWebGraphAnalogIn57641MfDeviceTyp,'wtWebGraphAnalogIn57641MfOrderNo':wtWebGraphAnalogIn57641MfOrderNo,'wtWebGraphAnalogIn57641Diag':wtWebGraphAnalogIn57641Diag,'wtWebGraphAnalogIn57641DiagErrorCount':wtWebGraphAnalogIn57641DiagErrorCount,'wtWebGraphAnalogIn57641DiagBinaryError':wtWebGraphAnalogIn57641DiagBinaryError,_L:wtWebGraphAnalogIn57641DiagErrorIndex,_M:wtWebGraphAnalogIn57641DiagErrorMessage,'wtWebGraphAnalogIn57641DiagErrorClear':wtWebGraphAnalogIn57641DiagErrorClear})