_N='wtWebGraphAnalog57761DiagErrorMessage'
_M='wtWebGraphAnalog57761DiagErrorIndex'
_L='NotificationType'
_K='wtWebGraphAnalog57761AlarmNo'
_J='wtWebGraphAnalog57761BinaryModeNo'
_I='wtWebGraphAnalog57761SensorNo'
_H='wtWebGraphAnalog57761AlarmClearTrapText'
_G='wtWebGraphAnalog57761AlarmTrapText'
_F='read-only'
_E='WebGraph-AnalogIO-57761-US-MIB'
_D='OctetString'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_L,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_L,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Wut_ObjectIdentity=ObjectIdentity
wut=_Wut_ObjectIdentity((1,3,6,1,4,1,5040))
_WtComServer_ObjectIdentity=ObjectIdentity
wtComServer=_WtComServer_ObjectIdentity((1,3,6,1,4,1,5040,1))
_WtWebio_ObjectIdentity=ObjectIdentity
wtWebio=_WtWebio_ObjectIdentity((1,3,6,1,4,1,5040,1,2))
_WtWebGraphAnalog57761_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761=_WtWebGraphAnalog57761_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28))
_WtWebGraphAnalog57761Inventory_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761Inventory=_WtWebGraphAnalog57761Inventory_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,1))
class _WtWebGraphAnalog57761Sensors_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_WtWebGraphAnalog57761Sensors_Type.__name__=_C
_WtWebGraphAnalog57761Sensors_Object=MibScalar
wtWebGraphAnalog57761Sensors=_WtWebGraphAnalog57761Sensors_Object((1,3,6,1,4,1,5040,1,2,28,1,1),_WtWebGraphAnalog57761Sensors_Type())
wtWebGraphAnalog57761Sensors.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphAnalog57761Sensors.setStatus(_A)
_WtWebGraphAnalog57761SensorTable_Object=MibTable
wtWebGraphAnalog57761SensorTable=_WtWebGraphAnalog57761SensorTable_Object((1,3,6,1,4,1,5040,1,2,28,1,2))
if mibBuilder.loadTexts:wtWebGraphAnalog57761SensorTable.setStatus(_A)
_WtWebGraphAnalog57761SensorEntry_Object=MibTableRow
wtWebGraphAnalog57761SensorEntry=_WtWebGraphAnalog57761SensorEntry_Object((1,3,6,1,4,1,5040,1,2,28,1,2,1))
wtWebGraphAnalog57761SensorEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:wtWebGraphAnalog57761SensorEntry.setStatus(_A)
class _WtWebGraphAnalog57761SensorNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_WtWebGraphAnalog57761SensorNo_Type.__name__=_C
_WtWebGraphAnalog57761SensorNo_Object=MibTableColumn
wtWebGraphAnalog57761SensorNo=_WtWebGraphAnalog57761SensorNo_Object((1,3,6,1,4,1,5040,1,2,28,1,2,1,1),_WtWebGraphAnalog57761SensorNo_Type())
wtWebGraphAnalog57761SensorNo.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphAnalog57761SensorNo.setStatus(_A)
_WtWebGraphAnalog57761ValuesTable_Object=MibTable
wtWebGraphAnalog57761ValuesTable=_WtWebGraphAnalog57761ValuesTable_Object((1,3,6,1,4,1,5040,1,2,28,1,3))
if mibBuilder.loadTexts:wtWebGraphAnalog57761ValuesTable.setStatus(_A)
_WtWebGraphAnalog57761ValuesEntry_Object=MibTableRow
wtWebGraphAnalog57761ValuesEntry=_WtWebGraphAnalog57761ValuesEntry_Object((1,3,6,1,4,1,5040,1,2,28,1,3,1))
wtWebGraphAnalog57761ValuesEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:wtWebGraphAnalog57761ValuesEntry.setStatus(_A)
class _WtWebGraphAnalog57761Values_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_WtWebGraphAnalog57761Values_Type.__name__=_D
_WtWebGraphAnalog57761Values_Object=MibTableColumn
wtWebGraphAnalog57761Values=_WtWebGraphAnalog57761Values_Object((1,3,6,1,4,1,5040,1,2,28,1,3,1,1),_WtWebGraphAnalog57761Values_Type())
wtWebGraphAnalog57761Values.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761Values.setStatus(_A)
_WtWebGraphAnalog57761BinaryValuesTable_Object=MibTable
wtWebGraphAnalog57761BinaryValuesTable=_WtWebGraphAnalog57761BinaryValuesTable_Object((1,3,6,1,4,1,5040,1,2,28,1,4))
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryValuesTable.setStatus(_A)
_WtWebGraphAnalog57761BinaryValuesEntry_Object=MibTableRow
wtWebGraphAnalog57761BinaryValuesEntry=_WtWebGraphAnalog57761BinaryValuesEntry_Object((1,3,6,1,4,1,5040,1,2,28,1,4,1))
wtWebGraphAnalog57761BinaryValuesEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryValuesEntry.setStatus(_A)
_WtWebGraphAnalog57761BinaryValues_Type=Integer32
_WtWebGraphAnalog57761BinaryValues_Object=MibTableColumn
wtWebGraphAnalog57761BinaryValues=_WtWebGraphAnalog57761BinaryValues_Object((1,3,6,1,4,1,5040,1,2,28,1,4,1,1),_WtWebGraphAnalog57761BinaryValues_Type())
wtWebGraphAnalog57761BinaryValues.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryValues.setStatus(_A)
_WtWebGraphAnalog57761ValuesPointTable_Object=MibTable
wtWebGraphAnalog57761ValuesPointTable=_WtWebGraphAnalog57761ValuesPointTable_Object((1,3,6,1,4,1,5040,1,2,28,1,8))
if mibBuilder.loadTexts:wtWebGraphAnalog57761ValuesPointTable.setStatus(_A)
_WtWebGraphAnalog57761ValuesPointEntry_Object=MibTableRow
wtWebGraphAnalog57761ValuesPointEntry=_WtWebGraphAnalog57761ValuesPointEntry_Object((1,3,6,1,4,1,5040,1,2,28,1,8,1))
wtWebGraphAnalog57761ValuesPointEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:wtWebGraphAnalog57761ValuesPointEntry.setStatus(_A)
class _WtWebGraphAnalog57761ValuesPoint_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(5,5));fixedLength=5
_WtWebGraphAnalog57761ValuesPoint_Type.__name__=_D
_WtWebGraphAnalog57761ValuesPoint_Object=MibTableColumn
wtWebGraphAnalog57761ValuesPoint=_WtWebGraphAnalog57761ValuesPoint_Object((1,3,6,1,4,1,5040,1,2,28,1,8,1,1),_WtWebGraphAnalog57761ValuesPoint_Type())
wtWebGraphAnalog57761ValuesPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761ValuesPoint.setStatus(_A)
_WtWebGraphAnalog57761SessCntrl_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761SessCntrl=_WtWebGraphAnalog57761SessCntrl_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,2))
_WtWebGraphAnalog57761SessCntrlPassword_Type=OctetString
_WtWebGraphAnalog57761SessCntrlPassword_Object=MibScalar
wtWebGraphAnalog57761SessCntrlPassword=_WtWebGraphAnalog57761SessCntrlPassword_Object((1,3,6,1,4,1,5040,1,2,28,2,1),_WtWebGraphAnalog57761SessCntrlPassword_Type())
wtWebGraphAnalog57761SessCntrlPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761SessCntrlPassword.setStatus(_A)
class _WtWebGraphAnalog57761SessCntrlConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('wtWebGraphAnalog57761SessCntrl-NoSession',0),('wtWebGraphAnalog57761SessCntrl-Session',1)))
_WtWebGraphAnalog57761SessCntrlConfigMode_Type.__name__=_C
_WtWebGraphAnalog57761SessCntrlConfigMode_Object=MibScalar
wtWebGraphAnalog57761SessCntrlConfigMode=_WtWebGraphAnalog57761SessCntrlConfigMode_Object((1,3,6,1,4,1,5040,1,2,28,2,2),_WtWebGraphAnalog57761SessCntrlConfigMode_Type())
wtWebGraphAnalog57761SessCntrlConfigMode.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphAnalog57761SessCntrlConfigMode.setStatus(_A)
_WtWebGraphAnalog57761SessCntrlLogout_Type=Integer32
_WtWebGraphAnalog57761SessCntrlLogout_Object=MibScalar
wtWebGraphAnalog57761SessCntrlLogout=_WtWebGraphAnalog57761SessCntrlLogout_Object((1,3,6,1,4,1,5040,1,2,28,2,3),_WtWebGraphAnalog57761SessCntrlLogout_Type())
wtWebGraphAnalog57761SessCntrlLogout.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761SessCntrlLogout.setStatus(_A)
_WtWebGraphAnalog57761SessCntrlAdminPassword_Type=OctetString
_WtWebGraphAnalog57761SessCntrlAdminPassword_Object=MibScalar
wtWebGraphAnalog57761SessCntrlAdminPassword=_WtWebGraphAnalog57761SessCntrlAdminPassword_Object((1,3,6,1,4,1,5040,1,2,28,2,4),_WtWebGraphAnalog57761SessCntrlAdminPassword_Type())
wtWebGraphAnalog57761SessCntrlAdminPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761SessCntrlAdminPassword.setStatus(_A)
_WtWebGraphAnalog57761SessCntrlConfigPassword_Type=OctetString
_WtWebGraphAnalog57761SessCntrlConfigPassword_Object=MibScalar
wtWebGraphAnalog57761SessCntrlConfigPassword=_WtWebGraphAnalog57761SessCntrlConfigPassword_Object((1,3,6,1,4,1,5040,1,2,28,2,5),_WtWebGraphAnalog57761SessCntrlConfigPassword_Type())
wtWebGraphAnalog57761SessCntrlConfigPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761SessCntrlConfigPassword.setStatus(_A)
_WtWebGraphAnalog57761Config_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761Config=_WtWebGraphAnalog57761Config_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3))
_WtWebGraphAnalog57761Device_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761Device=_WtWebGraphAnalog57761Device_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,1))
_WtWebGraphAnalog57761Text_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761Text=_WtWebGraphAnalog57761Text_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,1,1))
_WtWebGraphAnalog57761DeviceName_Type=OctetString
_WtWebGraphAnalog57761DeviceName_Object=MibScalar
wtWebGraphAnalog57761DeviceName=_WtWebGraphAnalog57761DeviceName_Object((1,3,6,1,4,1,5040,1,2,28,3,1,1,1),_WtWebGraphAnalog57761DeviceName_Type())
wtWebGraphAnalog57761DeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761DeviceName.setStatus(_A)
_WtWebGraphAnalog57761DeviceText_Type=OctetString
_WtWebGraphAnalog57761DeviceText_Object=MibScalar
wtWebGraphAnalog57761DeviceText=_WtWebGraphAnalog57761DeviceText_Object((1,3,6,1,4,1,5040,1,2,28,3,1,1,2),_WtWebGraphAnalog57761DeviceText_Type())
wtWebGraphAnalog57761DeviceText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761DeviceText.setStatus(_A)
_WtWebGraphAnalog57761DeviceLocation_Type=OctetString
_WtWebGraphAnalog57761DeviceLocation_Object=MibScalar
wtWebGraphAnalog57761DeviceLocation=_WtWebGraphAnalog57761DeviceLocation_Object((1,3,6,1,4,1,5040,1,2,28,3,1,1,3),_WtWebGraphAnalog57761DeviceLocation_Type())
wtWebGraphAnalog57761DeviceLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761DeviceLocation.setStatus(_A)
_WtWebGraphAnalog57761DeviceContact_Type=OctetString
_WtWebGraphAnalog57761DeviceContact_Object=MibScalar
wtWebGraphAnalog57761DeviceContact=_WtWebGraphAnalog57761DeviceContact_Object((1,3,6,1,4,1,5040,1,2,28,3,1,1,4),_WtWebGraphAnalog57761DeviceContact_Type())
wtWebGraphAnalog57761DeviceContact.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761DeviceContact.setStatus(_A)
_WtWebGraphAnalog57761TimeDate_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761TimeDate=_WtWebGraphAnalog57761TimeDate_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,1,2))
_WtWebGraphAnalog57761TimeZone_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761TimeZone=_WtWebGraphAnalog57761TimeZone_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,1,2,1))
_WtWebGraphAnalog57761TzOffsetHrs_Type=Integer32
_WtWebGraphAnalog57761TzOffsetHrs_Object=MibScalar
wtWebGraphAnalog57761TzOffsetHrs=_WtWebGraphAnalog57761TzOffsetHrs_Object((1,3,6,1,4,1,5040,1,2,28,3,1,2,1,1),_WtWebGraphAnalog57761TzOffsetHrs_Type())
wtWebGraphAnalog57761TzOffsetHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761TzOffsetHrs.setStatus(_A)
_WtWebGraphAnalog57761TzOffsetMin_Type=Integer32
_WtWebGraphAnalog57761TzOffsetMin_Object=MibScalar
wtWebGraphAnalog57761TzOffsetMin=_WtWebGraphAnalog57761TzOffsetMin_Object((1,3,6,1,4,1,5040,1,2,28,3,1,2,1,2),_WtWebGraphAnalog57761TzOffsetMin_Type())
wtWebGraphAnalog57761TzOffsetMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761TzOffsetMin.setStatus(_A)
class _WtWebGraphAnalog57761TzEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761TzEnable_Type.__name__=_D
_WtWebGraphAnalog57761TzEnable_Object=MibScalar
wtWebGraphAnalog57761TzEnable=_WtWebGraphAnalog57761TzEnable_Object((1,3,6,1,4,1,5040,1,2,28,3,1,2,1,3),_WtWebGraphAnalog57761TzEnable_Type())
wtWebGraphAnalog57761TzEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761TzEnable.setStatus(_A)
_WtWebGraphAnalog57761StTzOffsetHrs_Type=Integer32
_WtWebGraphAnalog57761StTzOffsetHrs_Object=MibScalar
wtWebGraphAnalog57761StTzOffsetHrs=_WtWebGraphAnalog57761StTzOffsetHrs_Object((1,3,6,1,4,1,5040,1,2,28,3,1,2,1,4),_WtWebGraphAnalog57761StTzOffsetHrs_Type())
wtWebGraphAnalog57761StTzOffsetHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761StTzOffsetHrs.setStatus(_A)
_WtWebGraphAnalog57761StTzOffsetMin_Type=Integer32
_WtWebGraphAnalog57761StTzOffsetMin_Object=MibScalar
wtWebGraphAnalog57761StTzOffsetMin=_WtWebGraphAnalog57761StTzOffsetMin_Object((1,3,6,1,4,1,5040,1,2,28,3,1,2,1,5),_WtWebGraphAnalog57761StTzOffsetMin_Type())
wtWebGraphAnalog57761StTzOffsetMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761StTzOffsetMin.setStatus(_A)
class _WtWebGraphAnalog57761StTzEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761StTzEnable_Type.__name__=_D
_WtWebGraphAnalog57761StTzEnable_Object=MibScalar
wtWebGraphAnalog57761StTzEnable=_WtWebGraphAnalog57761StTzEnable_Object((1,3,6,1,4,1,5040,1,2,28,3,1,2,1,6),_WtWebGraphAnalog57761StTzEnable_Type())
wtWebGraphAnalog57761StTzEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761StTzEnable.setStatus(_A)
class _WtWebGraphAnalog57761StTzStartMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('wtWebGraphAnalog57761StartMonth-January',1),('wtWebGraphAnalog57761StartMonth-February',2),('wtWebGraphAnalog57761StartMonth-March',3),('wtWebGraphAnalog57761StartMonth-April',4),('wtWebGraphAnalog57761StartMonth-May',5),('wtWebGraphAnalog57761StartMonth-June',6),('wtWebGraphAnalog57761StartMonth-July',7),('wtWebGraphAnalog57761StartMonth-August',8),('wtWebGraphAnalog57761StartMonth-September',9),('wtWebGraphAnalog57761StartMonth-October',10),('wtWebGraphAnalog57761StartMonth-November',11),('wtWebGraphAnalog57761StartMonth-December',12)))
_WtWebGraphAnalog57761StTzStartMonth_Type.__name__=_C
_WtWebGraphAnalog57761StTzStartMonth_Object=MibScalar
wtWebGraphAnalog57761StTzStartMonth=_WtWebGraphAnalog57761StTzStartMonth_Object((1,3,6,1,4,1,5040,1,2,28,3,1,2,1,7),_WtWebGraphAnalog57761StTzStartMonth_Type())
wtWebGraphAnalog57761StTzStartMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761StTzStartMonth.setStatus(_A)
class _WtWebGraphAnalog57761StTzStartMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('wtWebGraphAnalog57761StartMode-first',1),('wtWebGraphAnalog57761StartMode-second',2),('wtWebGraphAnalog57761StartMode-third',3),('wtWebGraphAnalog57761StartMode-fourth',4),('wtWebGraphAnalog57761StartMode-last',5)))
_WtWebGraphAnalog57761StTzStartMode_Type.__name__=_C
_WtWebGraphAnalog57761StTzStartMode_Object=MibScalar
wtWebGraphAnalog57761StTzStartMode=_WtWebGraphAnalog57761StTzStartMode_Object((1,3,6,1,4,1,5040,1,2,28,3,1,2,1,8),_WtWebGraphAnalog57761StTzStartMode_Type())
wtWebGraphAnalog57761StTzStartMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761StTzStartMode.setStatus(_A)
class _WtWebGraphAnalog57761StTzStartWday_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('wtWebGraphAnalog57761StartWday-Sunday',1),('wtWebGraphAnalog57761StartWday-Monday',2),('wtWebGraphAnalog57761StartWday-Tuesday',3),('wtWebGraphAnalog57761StartWday-Thursday',4),('wtWebGraphAnalog57761StartWday-Wednesday',5),('wtWebGraphAnalog57761StartWday-Friday',6),('wtWebGraphAnalog57761StartWday-Saturday',7)))
_WtWebGraphAnalog57761StTzStartWday_Type.__name__=_C
_WtWebGraphAnalog57761StTzStartWday_Object=MibScalar
wtWebGraphAnalog57761StTzStartWday=_WtWebGraphAnalog57761StTzStartWday_Object((1,3,6,1,4,1,5040,1,2,28,3,1,2,1,9),_WtWebGraphAnalog57761StTzStartWday_Type())
wtWebGraphAnalog57761StTzStartWday.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761StTzStartWday.setStatus(_A)
_WtWebGraphAnalog57761StTzStartHrs_Type=Integer32
_WtWebGraphAnalog57761StTzStartHrs_Object=MibScalar
wtWebGraphAnalog57761StTzStartHrs=_WtWebGraphAnalog57761StTzStartHrs_Object((1,3,6,1,4,1,5040,1,2,28,3,1,2,1,10),_WtWebGraphAnalog57761StTzStartHrs_Type())
wtWebGraphAnalog57761StTzStartHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761StTzStartHrs.setStatus(_A)
_WtWebGraphAnalog57761StTzStartMin_Type=Integer32
_WtWebGraphAnalog57761StTzStartMin_Object=MibScalar
wtWebGraphAnalog57761StTzStartMin=_WtWebGraphAnalog57761StTzStartMin_Object((1,3,6,1,4,1,5040,1,2,28,3,1,2,1,11),_WtWebGraphAnalog57761StTzStartMin_Type())
wtWebGraphAnalog57761StTzStartMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761StTzStartMin.setStatus(_A)
class _WtWebGraphAnalog57761StTzStopMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('wtWebGraphAnalog57761StopMonth-January',1),('wtWebGraphAnalog57761StopMonth-February',2),('wtWebGraphAnalog57761StopMonth-March',3),('wtWebGraphAnalog57761StopMonth-April',4),('wtWebGraphAnalog57761StopMonth-May',5),('wtWebGraphAnalog57761StopMonth-June',6),('wtWebGraphAnalog57761StopMonth-July',7),('wtWebGraphAnalog57761StopMonth-August',8),('wtWebGraphAnalog57761StopMonth-September',9),('wtWebGraphAnalog57761StopMonth-October',10),('wtWebGraphAnalog57761StopMonth-November',11),('wtWebGraphAnalog57761StopMonth-December',12)))
_WtWebGraphAnalog57761StTzStopMonth_Type.__name__=_C
_WtWebGraphAnalog57761StTzStopMonth_Object=MibScalar
wtWebGraphAnalog57761StTzStopMonth=_WtWebGraphAnalog57761StTzStopMonth_Object((1,3,6,1,4,1,5040,1,2,28,3,1,2,1,12),_WtWebGraphAnalog57761StTzStopMonth_Type())
wtWebGraphAnalog57761StTzStopMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761StTzStopMonth.setStatus(_A)
class _WtWebGraphAnalog57761StTzStopMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('wtWebGraphAnalog57761StopMode-first',1),('wtWebGraphAnalog57761StopMode-second',2),('wtWebGraphAnalog57761StopMode-third',3),('wtWebGraphAnalog57761StopMode-fourth',4),('wtWebGraphAnalog57761StopMode-last',5)))
_WtWebGraphAnalog57761StTzStopMode_Type.__name__=_C
_WtWebGraphAnalog57761StTzStopMode_Object=MibScalar
wtWebGraphAnalog57761StTzStopMode=_WtWebGraphAnalog57761StTzStopMode_Object((1,3,6,1,4,1,5040,1,2,28,3,1,2,1,13),_WtWebGraphAnalog57761StTzStopMode_Type())
wtWebGraphAnalog57761StTzStopMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761StTzStopMode.setStatus(_A)
class _WtWebGraphAnalog57761StTzStopWday_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('wtWebGraphAnalog57761StopWday-Sunday',1),('wtWebGraphAnalog57761StopWday-Monday',2),('wtWebGraphAnalog57761StopWday-Tuesday',3),('wtWebGraphAnalog57761StopWday-Thursday',4),('wtWebGraphAnalog57761StopWday-Wednesday',5),('wtWebGraphAnalog57761StopWday-Friday',6),('wtWebGraphAnalog57761StopWday-Saturday',7)))
_WtWebGraphAnalog57761StTzStopWday_Type.__name__=_C
_WtWebGraphAnalog57761StTzStopWday_Object=MibScalar
wtWebGraphAnalog57761StTzStopWday=_WtWebGraphAnalog57761StTzStopWday_Object((1,3,6,1,4,1,5040,1,2,28,3,1,2,1,14),_WtWebGraphAnalog57761StTzStopWday_Type())
wtWebGraphAnalog57761StTzStopWday.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761StTzStopWday.setStatus(_A)
_WtWebGraphAnalog57761StTzStopHrs_Type=Integer32
_WtWebGraphAnalog57761StTzStopHrs_Object=MibScalar
wtWebGraphAnalog57761StTzStopHrs=_WtWebGraphAnalog57761StTzStopHrs_Object((1,3,6,1,4,1,5040,1,2,28,3,1,2,1,15),_WtWebGraphAnalog57761StTzStopHrs_Type())
wtWebGraphAnalog57761StTzStopHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761StTzStopHrs.setStatus(_A)
_WtWebGraphAnalog57761StTzStopMin_Type=Integer32
_WtWebGraphAnalog57761StTzStopMin_Object=MibScalar
wtWebGraphAnalog57761StTzStopMin=_WtWebGraphAnalog57761StTzStopMin_Object((1,3,6,1,4,1,5040,1,2,28,3,1,2,1,16),_WtWebGraphAnalog57761StTzStopMin_Type())
wtWebGraphAnalog57761StTzStopMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761StTzStopMin.setStatus(_A)
_WtWebGraphAnalog57761TimeServer_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761TimeServer=_WtWebGraphAnalog57761TimeServer_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,1,2,2))
_WtWebGraphAnalog57761TimeServer1_Type=OctetString
_WtWebGraphAnalog57761TimeServer1_Object=MibScalar
wtWebGraphAnalog57761TimeServer1=_WtWebGraphAnalog57761TimeServer1_Object((1,3,6,1,4,1,5040,1,2,28,3,1,2,2,1),_WtWebGraphAnalog57761TimeServer1_Type())
wtWebGraphAnalog57761TimeServer1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761TimeServer1.setStatus(_A)
_WtWebGraphAnalog57761TimeServer2_Type=OctetString
_WtWebGraphAnalog57761TimeServer2_Object=MibScalar
wtWebGraphAnalog57761TimeServer2=_WtWebGraphAnalog57761TimeServer2_Object((1,3,6,1,4,1,5040,1,2,28,3,1,2,2,2),_WtWebGraphAnalog57761TimeServer2_Type())
wtWebGraphAnalog57761TimeServer2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761TimeServer2.setStatus(_A)
class _WtWebGraphAnalog57761TsEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761TsEnable_Type.__name__=_D
_WtWebGraphAnalog57761TsEnable_Object=MibScalar
wtWebGraphAnalog57761TsEnable=_WtWebGraphAnalog57761TsEnable_Object((1,3,6,1,4,1,5040,1,2,28,3,1,2,2,3),_WtWebGraphAnalog57761TsEnable_Type())
wtWebGraphAnalog57761TsEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761TsEnable.setStatus(_A)
_WtWebGraphAnalog57761TsSyncTime_Type=Integer32
_WtWebGraphAnalog57761TsSyncTime_Object=MibScalar
wtWebGraphAnalog57761TsSyncTime=_WtWebGraphAnalog57761TsSyncTime_Object((1,3,6,1,4,1,5040,1,2,28,3,1,2,2,4),_WtWebGraphAnalog57761TsSyncTime_Type())
wtWebGraphAnalog57761TsSyncTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761TsSyncTime.setStatus(_A)
_WtWebGraphAnalog57761DeviceClock_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761DeviceClock=_WtWebGraphAnalog57761DeviceClock_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,1,2,3))
class _WtWebGraphAnalog57761ClockHrs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_WtWebGraphAnalog57761ClockHrs_Type.__name__=_C
_WtWebGraphAnalog57761ClockHrs_Object=MibScalar
wtWebGraphAnalog57761ClockHrs=_WtWebGraphAnalog57761ClockHrs_Object((1,3,6,1,4,1,5040,1,2,28,3,1,2,3,1),_WtWebGraphAnalog57761ClockHrs_Type())
wtWebGraphAnalog57761ClockHrs.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761ClockHrs.setStatus(_A)
class _WtWebGraphAnalog57761ClockMin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_WtWebGraphAnalog57761ClockMin_Type.__name__=_C
_WtWebGraphAnalog57761ClockMin_Object=MibScalar
wtWebGraphAnalog57761ClockMin=_WtWebGraphAnalog57761ClockMin_Object((1,3,6,1,4,1,5040,1,2,28,3,1,2,3,2),_WtWebGraphAnalog57761ClockMin_Type())
wtWebGraphAnalog57761ClockMin.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761ClockMin.setStatus(_A)
class _WtWebGraphAnalog57761ClockDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_WtWebGraphAnalog57761ClockDay_Type.__name__=_C
_WtWebGraphAnalog57761ClockDay_Object=MibScalar
wtWebGraphAnalog57761ClockDay=_WtWebGraphAnalog57761ClockDay_Object((1,3,6,1,4,1,5040,1,2,28,3,1,2,3,3),_WtWebGraphAnalog57761ClockDay_Type())
wtWebGraphAnalog57761ClockDay.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761ClockDay.setStatus(_A)
class _WtWebGraphAnalog57761ClockMonth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('wtWebGraphAnalog57761ClockMonth-January',1),('wtWebGraphAnalog57761ClockMonth-February',2),('wtWebGraphAnalog57761ClockMonth-March',3),('wtWebGraphAnalog57761ClockMonth-April',4),('wtWebGraphAnalog57761ClockMonth-May',5),('wtWebGraphAnalog57761ClockMonth-June',6),('wtWebGraphAnalog57761ClockMonth-July',7),('wtWebGraphAnalog57761ClockMonth-August',8),('wtWebGraphAnalog57761ClockMonth-September',9),('wtWebGraphAnalog57761ClockMonth-October',10),('wtWebGraphAnalog57761ClockMonth-November',11),('wtWebGraphAnalog57761ClockMonth-December',12)))
_WtWebGraphAnalog57761ClockMonth_Type.__name__=_C
_WtWebGraphAnalog57761ClockMonth_Object=MibScalar
wtWebGraphAnalog57761ClockMonth=_WtWebGraphAnalog57761ClockMonth_Object((1,3,6,1,4,1,5040,1,2,28,3,1,2,3,4),_WtWebGraphAnalog57761ClockMonth_Type())
wtWebGraphAnalog57761ClockMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761ClockMonth.setStatus(_A)
class _WtWebGraphAnalog57761ClockYear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtWebGraphAnalog57761ClockYear_Type.__name__=_C
_WtWebGraphAnalog57761ClockYear_Object=MibScalar
wtWebGraphAnalog57761ClockYear=_WtWebGraphAnalog57761ClockYear_Object((1,3,6,1,4,1,5040,1,2,28,3,1,2,3,5),_WtWebGraphAnalog57761ClockYear_Type())
wtWebGraphAnalog57761ClockYear.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761ClockYear.setStatus(_A)
_WtWebGraphAnalog57761Basic_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761Basic=_WtWebGraphAnalog57761Basic_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,1,3))
_WtWebGraphAnalog57761Network_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761Network=_WtWebGraphAnalog57761Network_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,1,3,1))
_WtWebGraphAnalog57761IpAddress_Type=IpAddress
_WtWebGraphAnalog57761IpAddress_Object=MibScalar
wtWebGraphAnalog57761IpAddress=_WtWebGraphAnalog57761IpAddress_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,1,1),_WtWebGraphAnalog57761IpAddress_Type())
wtWebGraphAnalog57761IpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761IpAddress.setStatus(_A)
_WtWebGraphAnalog57761SubnetMask_Type=IpAddress
_WtWebGraphAnalog57761SubnetMask_Object=MibScalar
wtWebGraphAnalog57761SubnetMask=_WtWebGraphAnalog57761SubnetMask_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,1,2),_WtWebGraphAnalog57761SubnetMask_Type())
wtWebGraphAnalog57761SubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761SubnetMask.setStatus(_A)
_WtWebGraphAnalog57761Gateway_Type=IpAddress
_WtWebGraphAnalog57761Gateway_Object=MibScalar
wtWebGraphAnalog57761Gateway=_WtWebGraphAnalog57761Gateway_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,1,3),_WtWebGraphAnalog57761Gateway_Type())
wtWebGraphAnalog57761Gateway.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761Gateway.setStatus(_A)
_WtWebGraphAnalog57761DnsServer1_Type=OctetString
_WtWebGraphAnalog57761DnsServer1_Object=MibScalar
wtWebGraphAnalog57761DnsServer1=_WtWebGraphAnalog57761DnsServer1_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,1,4),_WtWebGraphAnalog57761DnsServer1_Type())
wtWebGraphAnalog57761DnsServer1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761DnsServer1.setStatus(_A)
_WtWebGraphAnalog57761DnsServer2_Type=OctetString
_WtWebGraphAnalog57761DnsServer2_Object=MibScalar
wtWebGraphAnalog57761DnsServer2=_WtWebGraphAnalog57761DnsServer2_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,1,5),_WtWebGraphAnalog57761DnsServer2_Type())
wtWebGraphAnalog57761DnsServer2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761DnsServer2.setStatus(_A)
_WtWebGraphAnalog57761AddConfig_Type=OctetString
_WtWebGraphAnalog57761AddConfig_Object=MibScalar
wtWebGraphAnalog57761AddConfig=_WtWebGraphAnalog57761AddConfig_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,1,6),_WtWebGraphAnalog57761AddConfig_Type())
wtWebGraphAnalog57761AddConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AddConfig.setStatus(_A)
_WtWebGraphAnalog57761HTTP_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761HTTP=_WtWebGraphAnalog57761HTTP_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,1,3,2))
_WtWebGraphAnalog57761Startup_Type=OctetString
_WtWebGraphAnalog57761Startup_Object=MibScalar
wtWebGraphAnalog57761Startup=_WtWebGraphAnalog57761Startup_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,2,1),_WtWebGraphAnalog57761Startup_Type())
wtWebGraphAnalog57761Startup.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761Startup.setStatus(_A)
_WtWebGraphAnalog57761GetHeaderEnable_Type=OctetString
_WtWebGraphAnalog57761GetHeaderEnable_Object=MibScalar
wtWebGraphAnalog57761GetHeaderEnable=_WtWebGraphAnalog57761GetHeaderEnable_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,2,2),_WtWebGraphAnalog57761GetHeaderEnable_Type())
wtWebGraphAnalog57761GetHeaderEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761GetHeaderEnable.setStatus(_A)
class _WtWebGraphAnalog57761HttpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphAnalog57761HttpPort_Type.__name__=_C
_WtWebGraphAnalog57761HttpPort_Object=MibScalar
wtWebGraphAnalog57761HttpPort=_WtWebGraphAnalog57761HttpPort_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,2,3),_WtWebGraphAnalog57761HttpPort_Type())
wtWebGraphAnalog57761HttpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761HttpPort.setStatus(_A)
_WtWebGraphAnalog57761Mail_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761Mail=_WtWebGraphAnalog57761Mail_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,1,3,3))
_WtWebGraphAnalog57761MailAdName_Type=OctetString
_WtWebGraphAnalog57761MailAdName_Object=MibScalar
wtWebGraphAnalog57761MailAdName=_WtWebGraphAnalog57761MailAdName_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,3,1),_WtWebGraphAnalog57761MailAdName_Type())
wtWebGraphAnalog57761MailAdName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MailAdName.setStatus(_A)
_WtWebGraphAnalog57761MailReply_Type=OctetString
_WtWebGraphAnalog57761MailReply_Object=MibScalar
wtWebGraphAnalog57761MailReply=_WtWebGraphAnalog57761MailReply_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,3,2),_WtWebGraphAnalog57761MailReply_Type())
wtWebGraphAnalog57761MailReply.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MailReply.setStatus(_A)
_WtWebGraphAnalog57761MailServer_Type=OctetString
_WtWebGraphAnalog57761MailServer_Object=MibScalar
wtWebGraphAnalog57761MailServer=_WtWebGraphAnalog57761MailServer_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,3,3),_WtWebGraphAnalog57761MailServer_Type())
wtWebGraphAnalog57761MailServer.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MailServer.setStatus(_A)
_WtWebioAn1MailEnable_Type=OctetString
_WtWebioAn1MailEnable_Object=MibScalar
wtWebioAn1MailEnable=_WtWebioAn1MailEnable_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,3,4),_WtWebioAn1MailEnable_Type())
wtWebioAn1MailEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebioAn1MailEnable.setStatus(_A)
class _WtWebGraphAnalog57761MailAuthentication_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761MailAuthentication_Type.__name__=_D
_WtWebGraphAnalog57761MailAuthentication_Object=MibScalar
wtWebGraphAnalog57761MailAuthentication=_WtWebGraphAnalog57761MailAuthentication_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,3,5),_WtWebGraphAnalog57761MailAuthentication_Type())
wtWebGraphAnalog57761MailAuthentication.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MailAuthentication.setStatus(_A)
_WtWebGraphAnalog57761MailAuthUser_Type=OctetString
_WtWebGraphAnalog57761MailAuthUser_Object=MibScalar
wtWebGraphAnalog57761MailAuthUser=_WtWebGraphAnalog57761MailAuthUser_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,3,6),_WtWebGraphAnalog57761MailAuthUser_Type())
wtWebGraphAnalog57761MailAuthUser.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MailAuthUser.setStatus(_A)
_WtWebGraphAnalog57761MailAuthPassword_Type=OctetString
_WtWebGraphAnalog57761MailAuthPassword_Object=MibScalar
wtWebGraphAnalog57761MailAuthPassword=_WtWebGraphAnalog57761MailAuthPassword_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,3,7),_WtWebGraphAnalog57761MailAuthPassword_Type())
wtWebGraphAnalog57761MailAuthPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MailAuthPassword.setStatus(_A)
_WtWebGraphAnalog57761MailPop3Server_Type=OctetString
_WtWebGraphAnalog57761MailPop3Server_Object=MibScalar
wtWebGraphAnalog57761MailPop3Server=_WtWebGraphAnalog57761MailPop3Server_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,3,8),_WtWebGraphAnalog57761MailPop3Server_Type())
wtWebGraphAnalog57761MailPop3Server.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MailPop3Server.setStatus(_A)
_WtWebGraphAnalog57761SNMP_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761SNMP=_WtWebGraphAnalog57761SNMP_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,1,3,4))
_WtWebGraphAnalog57761SnmpCommunityStringRead_Type=OctetString
_WtWebGraphAnalog57761SnmpCommunityStringRead_Object=MibScalar
wtWebGraphAnalog57761SnmpCommunityStringRead=_WtWebGraphAnalog57761SnmpCommunityStringRead_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,4,1),_WtWebGraphAnalog57761SnmpCommunityStringRead_Type())
wtWebGraphAnalog57761SnmpCommunityStringRead.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761SnmpCommunityStringRead.setStatus(_A)
_WtWebGraphAnalog57761SnmpCommunityStringReadWrite_Type=OctetString
_WtWebGraphAnalog57761SnmpCommunityStringReadWrite_Object=MibScalar
wtWebGraphAnalog57761SnmpCommunityStringReadWrite=_WtWebGraphAnalog57761SnmpCommunityStringReadWrite_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,4,2),_WtWebGraphAnalog57761SnmpCommunityStringReadWrite_Type())
wtWebGraphAnalog57761SnmpCommunityStringReadWrite.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761SnmpCommunityStringReadWrite.setStatus(_A)
_WtWebGraphAnalog57761SystemTrapManagerIP_Type=OctetString
_WtWebGraphAnalog57761SystemTrapManagerIP_Object=MibScalar
wtWebGraphAnalog57761SystemTrapManagerIP=_WtWebGraphAnalog57761SystemTrapManagerIP_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,4,3),_WtWebGraphAnalog57761SystemTrapManagerIP_Type())
wtWebGraphAnalog57761SystemTrapManagerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761SystemTrapManagerIP.setStatus(_A)
class _WtWebGraphAnalog57761SystemTrapEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761SystemTrapEnable_Type.__name__=_D
_WtWebGraphAnalog57761SystemTrapEnable_Object=MibScalar
wtWebGraphAnalog57761SystemTrapEnable=_WtWebGraphAnalog57761SystemTrapEnable_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,4,4),_WtWebGraphAnalog57761SystemTrapEnable_Type())
wtWebGraphAnalog57761SystemTrapEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761SystemTrapEnable.setStatus(_A)
_WtWebGraphAnalog57761SnmpEnable_Type=OctetString
_WtWebGraphAnalog57761SnmpEnable_Object=MibScalar
wtWebGraphAnalog57761SnmpEnable=_WtWebGraphAnalog57761SnmpEnable_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,4,5),_WtWebGraphAnalog57761SnmpEnable_Type())
wtWebGraphAnalog57761SnmpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761SnmpEnable.setStatus(_A)
_WtWebGraphAnalog57761SnmpCommunityStringTrap_Type=OctetString
_WtWebGraphAnalog57761SnmpCommunityStringTrap_Object=MibScalar
wtWebGraphAnalog57761SnmpCommunityStringTrap=_WtWebGraphAnalog57761SnmpCommunityStringTrap_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,4,6),_WtWebGraphAnalog57761SnmpCommunityStringTrap_Type())
wtWebGraphAnalog57761SnmpCommunityStringTrap.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761SnmpCommunityStringTrap.setStatus(_A)
_WtWebGraphAnalog57761SnmpSystemTrapManagerPort_Type=Integer32
_WtWebGraphAnalog57761SnmpSystemTrapManagerPort_Object=MibScalar
wtWebGraphAnalog57761SnmpSystemTrapManagerPort=_WtWebGraphAnalog57761SnmpSystemTrapManagerPort_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,4,7),_WtWebGraphAnalog57761SnmpSystemTrapManagerPort_Type())
wtWebGraphAnalog57761SnmpSystemTrapManagerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761SnmpSystemTrapManagerPort.setStatus(_A)
_WtWebGraphAnalog57761UDP_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761UDP=_WtWebGraphAnalog57761UDP_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,1,3,5))
class _WtWebGraphAnalog57761UdpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphAnalog57761UdpPort_Type.__name__=_C
_WtWebGraphAnalog57761UdpPort_Object=MibScalar
wtWebGraphAnalog57761UdpPort=_WtWebGraphAnalog57761UdpPort_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,5,1),_WtWebGraphAnalog57761UdpPort_Type())
wtWebGraphAnalog57761UdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761UdpPort.setStatus(_A)
_WtWebGraphAnalog57761UdpEnable_Type=OctetString
_WtWebGraphAnalog57761UdpEnable_Object=MibScalar
wtWebGraphAnalog57761UdpEnable=_WtWebGraphAnalog57761UdpEnable_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,5,2),_WtWebGraphAnalog57761UdpEnable_Type())
wtWebGraphAnalog57761UdpEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761UdpEnable.setStatus(_A)
_WtWebGraphAnalog57761Syslog_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761Syslog=_WtWebGraphAnalog57761Syslog_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,1,3,6))
_WtWebGraphAnalog57761SyslogServerIP_Type=OctetString
_WtWebGraphAnalog57761SyslogServerIP_Object=MibScalar
wtWebGraphAnalog57761SyslogServerIP=_WtWebGraphAnalog57761SyslogServerIP_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,6,1),_WtWebGraphAnalog57761SyslogServerIP_Type())
wtWebGraphAnalog57761SyslogServerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761SyslogServerIP.setStatus(_A)
_WtWebGraphAnalog57761SyslogServerPort_Type=Integer32
_WtWebGraphAnalog57761SyslogServerPort_Object=MibScalar
wtWebGraphAnalog57761SyslogServerPort=_WtWebGraphAnalog57761SyslogServerPort_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,6,2),_WtWebGraphAnalog57761SyslogServerPort_Type())
wtWebGraphAnalog57761SyslogServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761SyslogServerPort.setStatus(_A)
class _WtWebGraphAnalog57761SyslogSystemMessagesEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761SyslogSystemMessagesEnable_Type.__name__=_D
_WtWebGraphAnalog57761SyslogSystemMessagesEnable_Object=MibScalar
wtWebGraphAnalog57761SyslogSystemMessagesEnable=_WtWebGraphAnalog57761SyslogSystemMessagesEnable_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,6,3),_WtWebGraphAnalog57761SyslogSystemMessagesEnable_Type())
wtWebGraphAnalog57761SyslogSystemMessagesEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761SyslogSystemMessagesEnable.setStatus(_A)
_WtWebGraphAnalog57761SyslogEnable_Type=OctetString
_WtWebGraphAnalog57761SyslogEnable_Object=MibScalar
wtWebGraphAnalog57761SyslogEnable=_WtWebGraphAnalog57761SyslogEnable_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,6,4),_WtWebGraphAnalog57761SyslogEnable_Type())
wtWebGraphAnalog57761SyslogEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761SyslogEnable.setStatus(_A)
_WtWebGraphAnalog57761FTP_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761FTP=_WtWebGraphAnalog57761FTP_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,1,3,7))
_WtWebGraphAnalog57761FTPServerIP_Type=OctetString
_WtWebGraphAnalog57761FTPServerIP_Object=MibScalar
wtWebGraphAnalog57761FTPServerIP=_WtWebGraphAnalog57761FTPServerIP_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,7,1),_WtWebGraphAnalog57761FTPServerIP_Type())
wtWebGraphAnalog57761FTPServerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761FTPServerIP.setStatus(_A)
_WtWebGraphAnalog57761FTPServerControlPort_Type=Integer32
_WtWebGraphAnalog57761FTPServerControlPort_Object=MibScalar
wtWebGraphAnalog57761FTPServerControlPort=_WtWebGraphAnalog57761FTPServerControlPort_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,7,2),_WtWebGraphAnalog57761FTPServerControlPort_Type())
wtWebGraphAnalog57761FTPServerControlPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761FTPServerControlPort.setStatus(_A)
_WtWebGraphAnalog57761FTPUserName_Type=OctetString
_WtWebGraphAnalog57761FTPUserName_Object=MibScalar
wtWebGraphAnalog57761FTPUserName=_WtWebGraphAnalog57761FTPUserName_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,7,3),_WtWebGraphAnalog57761FTPUserName_Type())
wtWebGraphAnalog57761FTPUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761FTPUserName.setStatus(_A)
_WtWebGraphAnalog57761FTPPassword_Type=OctetString
_WtWebGraphAnalog57761FTPPassword_Object=MibScalar
wtWebGraphAnalog57761FTPPassword=_WtWebGraphAnalog57761FTPPassword_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,7,4),_WtWebGraphAnalog57761FTPPassword_Type())
wtWebGraphAnalog57761FTPPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761FTPPassword.setStatus(_A)
_WtWebGraphAnalog57761FTPAccount_Type=OctetString
_WtWebGraphAnalog57761FTPAccount_Object=MibScalar
wtWebGraphAnalog57761FTPAccount=_WtWebGraphAnalog57761FTPAccount_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,7,5),_WtWebGraphAnalog57761FTPAccount_Type())
wtWebGraphAnalog57761FTPAccount.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761FTPAccount.setStatus(_A)
_WtWebGraphAnalog57761FTPOption_Type=OctetString
_WtWebGraphAnalog57761FTPOption_Object=MibScalar
wtWebGraphAnalog57761FTPOption=_WtWebGraphAnalog57761FTPOption_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,7,6),_WtWebGraphAnalog57761FTPOption_Type())
wtWebGraphAnalog57761FTPOption.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761FTPOption.setStatus(_A)
_WtWebGraphAnalog57761FTPEnable_Type=OctetString
_WtWebGraphAnalog57761FTPEnable_Object=MibScalar
wtWebGraphAnalog57761FTPEnable=_WtWebGraphAnalog57761FTPEnable_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,7,7),_WtWebGraphAnalog57761FTPEnable_Type())
wtWebGraphAnalog57761FTPEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761FTPEnable.setStatus(_A)
_WtWebGraphAnalog57761Language_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761Language=_WtWebGraphAnalog57761Language_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,1,3,8))
_WtWebGraphAnalog57761LanguageSelect_Type=OctetString
_WtWebGraphAnalog57761LanguageSelect_Object=MibScalar
wtWebGraphAnalog57761LanguageSelect=_WtWebGraphAnalog57761LanguageSelect_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,8,1),_WtWebGraphAnalog57761LanguageSelect_Type())
wtWebGraphAnalog57761LanguageSelect.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761LanguageSelect.setStatus(_A)
_WtWebGraphAnalog57761Binary_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761Binary=_WtWebGraphAnalog57761Binary_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,1,3,9))
class _WtWebGraphAnalog57761BinaryModeCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_WtWebGraphAnalog57761BinaryModeCount_Type.__name__=_C
_WtWebGraphAnalog57761BinaryModeCount_Object=MibScalar
wtWebGraphAnalog57761BinaryModeCount=_WtWebGraphAnalog57761BinaryModeCount_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,1),_WtWebGraphAnalog57761BinaryModeCount_Type())
wtWebGraphAnalog57761BinaryModeCount.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryModeCount.setStatus(_A)
_WtWebGraphAnalog57761BinaryIfTable_Object=MibTable
wtWebGraphAnalog57761BinaryIfTable=_WtWebGraphAnalog57761BinaryIfTable_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,2))
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryIfTable.setStatus(_A)
_WtWebGraphAnalog57761BinaryIfEntry_Object=MibTableRow
wtWebGraphAnalog57761BinaryIfEntry=_WtWebGraphAnalog57761BinaryIfEntry_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,2,1))
wtWebGraphAnalog57761BinaryIfEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryIfEntry.setStatus(_A)
class _WtWebGraphAnalog57761BinaryModeNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_WtWebGraphAnalog57761BinaryModeNo_Type.__name__=_C
_WtWebGraphAnalog57761BinaryModeNo_Object=MibTableColumn
wtWebGraphAnalog57761BinaryModeNo=_WtWebGraphAnalog57761BinaryModeNo_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,2,1,1),_WtWebGraphAnalog57761BinaryModeNo_Type())
wtWebGraphAnalog57761BinaryModeNo.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryModeNo.setStatus(_A)
_WtWebGraphAnalog57761BinaryTable_Object=MibTable
wtWebGraphAnalog57761BinaryTable=_WtWebGraphAnalog57761BinaryTable_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3))
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryTable.setStatus(_A)
_WtWebGraphAnalog57761BinaryEntry_Object=MibTableRow
wtWebGraphAnalog57761BinaryEntry=_WtWebGraphAnalog57761BinaryEntry_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1))
wtWebGraphAnalog57761BinaryEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryEntry.setStatus(_A)
class _WtWebGraphAnalog57761BinaryOperationMode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761BinaryOperationMode_Type.__name__=_D
_WtWebGraphAnalog57761BinaryOperationMode_Object=MibTableColumn
wtWebGraphAnalog57761BinaryOperationMode=_WtWebGraphAnalog57761BinaryOperationMode_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,1),_WtWebGraphAnalog57761BinaryOperationMode_Type())
wtWebGraphAnalog57761BinaryOperationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryOperationMode.setStatus(_A)
class _WtWebGraphAnalog57761BinaryTcpServerLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphAnalog57761BinaryTcpServerLocalPort_Type.__name__=_C
_WtWebGraphAnalog57761BinaryTcpServerLocalPort_Object=MibTableColumn
wtWebGraphAnalog57761BinaryTcpServerLocalPort=_WtWebGraphAnalog57761BinaryTcpServerLocalPort_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,2),_WtWebGraphAnalog57761BinaryTcpServerLocalPort_Type())
wtWebGraphAnalog57761BinaryTcpServerLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryTcpServerLocalPort.setStatus(_A)
class _WtWebGraphAnalog57761BinaryTcpServerInputTrigger_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761BinaryTcpServerInputTrigger_Type.__name__=_D
_WtWebGraphAnalog57761BinaryTcpServerInputTrigger_Object=MibTableColumn
wtWebGraphAnalog57761BinaryTcpServerInputTrigger=_WtWebGraphAnalog57761BinaryTcpServerInputTrigger_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,3),_WtWebGraphAnalog57761BinaryTcpServerInputTrigger_Type())
wtWebGraphAnalog57761BinaryTcpServerInputTrigger.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryTcpServerInputTrigger.setStatus(_A)
class _WtWebGraphAnalog57761BinaryTcpServerApplicationMode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761BinaryTcpServerApplicationMode_Type.__name__=_D
_WtWebGraphAnalog57761BinaryTcpServerApplicationMode_Object=MibTableColumn
wtWebGraphAnalog57761BinaryTcpServerApplicationMode=_WtWebGraphAnalog57761BinaryTcpServerApplicationMode_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,4),_WtWebGraphAnalog57761BinaryTcpServerApplicationMode_Type())
wtWebGraphAnalog57761BinaryTcpServerApplicationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryTcpServerApplicationMode.setStatus(_A)
class _WtWebGraphAnalog57761BinaryTcpClientLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphAnalog57761BinaryTcpClientLocalPort_Type.__name__=_C
_WtWebGraphAnalog57761BinaryTcpClientLocalPort_Object=MibTableColumn
wtWebGraphAnalog57761BinaryTcpClientLocalPort=_WtWebGraphAnalog57761BinaryTcpClientLocalPort_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,5),_WtWebGraphAnalog57761BinaryTcpClientLocalPort_Type())
wtWebGraphAnalog57761BinaryTcpClientLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryTcpClientLocalPort.setStatus(_A)
class _WtWebGraphAnalog57761BinaryTcpClientServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphAnalog57761BinaryTcpClientServerPort_Type.__name__=_C
_WtWebGraphAnalog57761BinaryTcpClientServerPort_Object=MibTableColumn
wtWebGraphAnalog57761BinaryTcpClientServerPort=_WtWebGraphAnalog57761BinaryTcpClientServerPort_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,6),_WtWebGraphAnalog57761BinaryTcpClientServerPort_Type())
wtWebGraphAnalog57761BinaryTcpClientServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryTcpClientServerPort.setStatus(_A)
_WtWebGraphAnalog57761BinaryTcpClientServerIpAddr_Type=OctetString
_WtWebGraphAnalog57761BinaryTcpClientServerIpAddr_Object=MibTableColumn
wtWebGraphAnalog57761BinaryTcpClientServerIpAddr=_WtWebGraphAnalog57761BinaryTcpClientServerIpAddr_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,7),_WtWebGraphAnalog57761BinaryTcpClientServerIpAddr_Type())
wtWebGraphAnalog57761BinaryTcpClientServerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryTcpClientServerIpAddr.setStatus(_A)
_WtWebGraphAnalog57761BinaryTcpClientServerPassword_Type=OctetString
_WtWebGraphAnalog57761BinaryTcpClientServerPassword_Object=MibTableColumn
wtWebGraphAnalog57761BinaryTcpClientServerPassword=_WtWebGraphAnalog57761BinaryTcpClientServerPassword_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,8),_WtWebGraphAnalog57761BinaryTcpClientServerPassword_Type())
wtWebGraphAnalog57761BinaryTcpClientServerPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryTcpClientServerPassword.setStatus(_A)
_WtWebGraphAnalog57761BinaryTcpClientInactivity_Type=Integer32
_WtWebGraphAnalog57761BinaryTcpClientInactivity_Object=MibTableColumn
wtWebGraphAnalog57761BinaryTcpClientInactivity=_WtWebGraphAnalog57761BinaryTcpClientInactivity_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,9),_WtWebGraphAnalog57761BinaryTcpClientInactivity_Type())
wtWebGraphAnalog57761BinaryTcpClientInactivity.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryTcpClientInactivity.setStatus(_A)
class _WtWebGraphAnalog57761BinaryTcpClientInputTrigger_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761BinaryTcpClientInputTrigger_Type.__name__=_D
_WtWebGraphAnalog57761BinaryTcpClientInputTrigger_Object=MibTableColumn
wtWebGraphAnalog57761BinaryTcpClientInputTrigger=_WtWebGraphAnalog57761BinaryTcpClientInputTrigger_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,10),_WtWebGraphAnalog57761BinaryTcpClientInputTrigger_Type())
wtWebGraphAnalog57761BinaryTcpClientInputTrigger.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryTcpClientInputTrigger.setStatus(_A)
class _WtWebGraphAnalog57761BinaryTcpClientInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtWebGraphAnalog57761BinaryTcpClientInterval_Type.__name__=_C
_WtWebGraphAnalog57761BinaryTcpClientInterval_Object=MibTableColumn
wtWebGraphAnalog57761BinaryTcpClientInterval=_WtWebGraphAnalog57761BinaryTcpClientInterval_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,11),_WtWebGraphAnalog57761BinaryTcpClientInterval_Type())
wtWebGraphAnalog57761BinaryTcpClientInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryTcpClientInterval.setStatus(_A)
class _WtWebGraphAnalog57761BinaryTcpClientApplicationMode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761BinaryTcpClientApplicationMode_Type.__name__=_D
_WtWebGraphAnalog57761BinaryTcpClientApplicationMode_Object=MibTableColumn
wtWebGraphAnalog57761BinaryTcpClientApplicationMode=_WtWebGraphAnalog57761BinaryTcpClientApplicationMode_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,12),_WtWebGraphAnalog57761BinaryTcpClientApplicationMode_Type())
wtWebGraphAnalog57761BinaryTcpClientApplicationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryTcpClientApplicationMode.setStatus(_A)
class _WtWebGraphAnalog57761BinaryUdpPeerLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphAnalog57761BinaryUdpPeerLocalPort_Type.__name__=_C
_WtWebGraphAnalog57761BinaryUdpPeerLocalPort_Object=MibTableColumn
wtWebGraphAnalog57761BinaryUdpPeerLocalPort=_WtWebGraphAnalog57761BinaryUdpPeerLocalPort_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,13),_WtWebGraphAnalog57761BinaryUdpPeerLocalPort_Type())
wtWebGraphAnalog57761BinaryUdpPeerLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryUdpPeerLocalPort.setStatus(_A)
class _WtWebGraphAnalog57761BinaryUdpPeerRemotePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphAnalog57761BinaryUdpPeerRemotePort_Type.__name__=_C
_WtWebGraphAnalog57761BinaryUdpPeerRemotePort_Object=MibTableColumn
wtWebGraphAnalog57761BinaryUdpPeerRemotePort=_WtWebGraphAnalog57761BinaryUdpPeerRemotePort_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,14),_WtWebGraphAnalog57761BinaryUdpPeerRemotePort_Type())
wtWebGraphAnalog57761BinaryUdpPeerRemotePort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryUdpPeerRemotePort.setStatus(_A)
_WtWebGraphAnalog57761BinaryUdpPeerRemoteIpAddr_Type=OctetString
_WtWebGraphAnalog57761BinaryUdpPeerRemoteIpAddr_Object=MibTableColumn
wtWebGraphAnalog57761BinaryUdpPeerRemoteIpAddr=_WtWebGraphAnalog57761BinaryUdpPeerRemoteIpAddr_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,15),_WtWebGraphAnalog57761BinaryUdpPeerRemoteIpAddr_Type())
wtWebGraphAnalog57761BinaryUdpPeerRemoteIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryUdpPeerRemoteIpAddr.setStatus(_A)
class _WtWebGraphAnalog57761BinaryUdpPeerInputTrigger_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761BinaryUdpPeerInputTrigger_Type.__name__=_D
_WtWebGraphAnalog57761BinaryUdpPeerInputTrigger_Object=MibTableColumn
wtWebGraphAnalog57761BinaryUdpPeerInputTrigger=_WtWebGraphAnalog57761BinaryUdpPeerInputTrigger_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,16),_WtWebGraphAnalog57761BinaryUdpPeerInputTrigger_Type())
wtWebGraphAnalog57761BinaryUdpPeerInputTrigger.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryUdpPeerInputTrigger.setStatus(_A)
class _WtWebGraphAnalog57761BinaryUdpPeerInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WtWebGraphAnalog57761BinaryUdpPeerInterval_Type.__name__=_C
_WtWebGraphAnalog57761BinaryUdpPeerInterval_Object=MibTableColumn
wtWebGraphAnalog57761BinaryUdpPeerInterval=_WtWebGraphAnalog57761BinaryUdpPeerInterval_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,17),_WtWebGraphAnalog57761BinaryUdpPeerInterval_Type())
wtWebGraphAnalog57761BinaryUdpPeerInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryUdpPeerInterval.setStatus(_A)
class _WtWebGraphAnalog57761BinaryUdpPeerApplicationMode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761BinaryUdpPeerApplicationMode_Type.__name__=_D
_WtWebGraphAnalog57761BinaryUdpPeerApplicationMode_Object=MibTableColumn
wtWebGraphAnalog57761BinaryUdpPeerApplicationMode=_WtWebGraphAnalog57761BinaryUdpPeerApplicationMode_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,18),_WtWebGraphAnalog57761BinaryUdpPeerApplicationMode_Type())
wtWebGraphAnalog57761BinaryUdpPeerApplicationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryUdpPeerApplicationMode.setStatus(_A)
class _WtWebGraphAnalog57761BinaryConnectedPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphAnalog57761BinaryConnectedPort_Type.__name__=_C
_WtWebGraphAnalog57761BinaryConnectedPort_Object=MibTableColumn
wtWebGraphAnalog57761BinaryConnectedPort=_WtWebGraphAnalog57761BinaryConnectedPort_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,19),_WtWebGraphAnalog57761BinaryConnectedPort_Type())
wtWebGraphAnalog57761BinaryConnectedPort.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryConnectedPort.setStatus(_A)
_WtWebGraphAnalog57761BinaryConnectedIpAddr_Type=IpAddress
_WtWebGraphAnalog57761BinaryConnectedIpAddr_Object=MibTableColumn
wtWebGraphAnalog57761BinaryConnectedIpAddr=_WtWebGraphAnalog57761BinaryConnectedIpAddr_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,20),_WtWebGraphAnalog57761BinaryConnectedIpAddr_Type())
wtWebGraphAnalog57761BinaryConnectedIpAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryConnectedIpAddr.setStatus(_A)
class _WtWebGraphAnalog57761BinaryTcpServerClientHttpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphAnalog57761BinaryTcpServerClientHttpPort_Type.__name__=_C
_WtWebGraphAnalog57761BinaryTcpServerClientHttpPort_Object=MibTableColumn
wtWebGraphAnalog57761BinaryTcpServerClientHttpPort=_WtWebGraphAnalog57761BinaryTcpServerClientHttpPort_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,21),_WtWebGraphAnalog57761BinaryTcpServerClientHttpPort_Type())
wtWebGraphAnalog57761BinaryTcpServerClientHttpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryTcpServerClientHttpPort.setStatus(_A)
class _WtWebGraphAnalog57761BinaryTcpClientServerHttpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphAnalog57761BinaryTcpClientServerHttpPort_Type.__name__=_C
_WtWebGraphAnalog57761BinaryTcpClientServerHttpPort_Object=MibTableColumn
wtWebGraphAnalog57761BinaryTcpClientServerHttpPort=_WtWebGraphAnalog57761BinaryTcpClientServerHttpPort_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,22),_WtWebGraphAnalog57761BinaryTcpClientServerHttpPort_Type())
wtWebGraphAnalog57761BinaryTcpClientServerHttpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryTcpClientServerHttpPort.setStatus(_A)
_WtWebGraphAnalog57761BinaryTcpServerHysteresis1_Type=OctetString
_WtWebGraphAnalog57761BinaryTcpServerHysteresis1_Object=MibTableColumn
wtWebGraphAnalog57761BinaryTcpServerHysteresis1=_WtWebGraphAnalog57761BinaryTcpServerHysteresis1_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,23),_WtWebGraphAnalog57761BinaryTcpServerHysteresis1_Type())
wtWebGraphAnalog57761BinaryTcpServerHysteresis1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryTcpServerHysteresis1.setStatus(_A)
_WtWebGraphAnalog57761BinaryTcpServerHysteresis2_Type=OctetString
_WtWebGraphAnalog57761BinaryTcpServerHysteresis2_Object=MibTableColumn
wtWebGraphAnalog57761BinaryTcpServerHysteresis2=_WtWebGraphAnalog57761BinaryTcpServerHysteresis2_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,24),_WtWebGraphAnalog57761BinaryTcpServerHysteresis2_Type())
wtWebGraphAnalog57761BinaryTcpServerHysteresis2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryTcpServerHysteresis2.setStatus(_A)
_WtWebGraphAnalog57761BinaryTcpClientHysteresis1_Type=OctetString
_WtWebGraphAnalog57761BinaryTcpClientHysteresis1_Object=MibTableColumn
wtWebGraphAnalog57761BinaryTcpClientHysteresis1=_WtWebGraphAnalog57761BinaryTcpClientHysteresis1_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,25),_WtWebGraphAnalog57761BinaryTcpClientHysteresis1_Type())
wtWebGraphAnalog57761BinaryTcpClientHysteresis1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryTcpClientHysteresis1.setStatus(_A)
_WtWebGraphAnalog57761BinaryTcpClientHysteresis2_Type=OctetString
_WtWebGraphAnalog57761BinaryTcpClientHysteresis2_Object=MibTableColumn
wtWebGraphAnalog57761BinaryTcpClientHysteresis2=_WtWebGraphAnalog57761BinaryTcpClientHysteresis2_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,26),_WtWebGraphAnalog57761BinaryTcpClientHysteresis2_Type())
wtWebGraphAnalog57761BinaryTcpClientHysteresis2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryTcpClientHysteresis2.setStatus(_A)
_WtWebGraphAnalog57761BinaryUdpPeerHysteresis1_Type=OctetString
_WtWebGraphAnalog57761BinaryUdpPeerHysteresis1_Object=MibTableColumn
wtWebGraphAnalog57761BinaryUdpPeerHysteresis1=_WtWebGraphAnalog57761BinaryUdpPeerHysteresis1_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,27),_WtWebGraphAnalog57761BinaryUdpPeerHysteresis1_Type())
wtWebGraphAnalog57761BinaryUdpPeerHysteresis1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryUdpPeerHysteresis1.setStatus(_A)
_WtWebGraphAnalog57761BinaryUdpPeerHysteresis2_Type=OctetString
_WtWebGraphAnalog57761BinaryUdpPeerHysteresis2_Object=MibTableColumn
wtWebGraphAnalog57761BinaryUdpPeerHysteresis2=_WtWebGraphAnalog57761BinaryUdpPeerHysteresis2_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,28),_WtWebGraphAnalog57761BinaryUdpPeerHysteresis2_Type())
wtWebGraphAnalog57761BinaryUdpPeerHysteresis2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryUdpPeerHysteresis2.setStatus(_A)
_WtWebGraphAnalog57761BinaryTcpClientServerUserName_Type=OctetString
_WtWebGraphAnalog57761BinaryTcpClientServerUserName_Object=MibTableColumn
wtWebGraphAnalog57761BinaryTcpClientServerUserName=_WtWebGraphAnalog57761BinaryTcpClientServerUserName_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,9,3,1,29),_WtWebGraphAnalog57761BinaryTcpClientServerUserName_Type())
wtWebGraphAnalog57761BinaryTcpClientServerUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761BinaryTcpClientServerUserName.setStatus(_A)
_WtWebGraphAnalog57761MQTT_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761MQTT=_WtWebGraphAnalog57761MQTT_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,1,3,12))
_WtWebGraphAnalog57761MQTTEnable_Type=OctetString
_WtWebGraphAnalog57761MQTTEnable_Object=MibScalar
wtWebGraphAnalog57761MQTTEnable=_WtWebGraphAnalog57761MQTTEnable_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,12,1),_WtWebGraphAnalog57761MQTTEnable_Type())
wtWebGraphAnalog57761MQTTEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MQTTEnable.setStatus(_A)
_WtWebGraphAnalog57761MQTTBrockerIP_Type=OctetString
_WtWebGraphAnalog57761MQTTBrockerIP_Object=MibScalar
wtWebGraphAnalog57761MQTTBrockerIP=_WtWebGraphAnalog57761MQTTBrockerIP_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,12,2),_WtWebGraphAnalog57761MQTTBrockerIP_Type())
wtWebGraphAnalog57761MQTTBrockerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MQTTBrockerIP.setStatus(_A)
_WtWebGraphAnalog57761MQTTUserName_Type=OctetString
_WtWebGraphAnalog57761MQTTUserName_Object=MibScalar
wtWebGraphAnalog57761MQTTUserName=_WtWebGraphAnalog57761MQTTUserName_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,12,3),_WtWebGraphAnalog57761MQTTUserName_Type())
wtWebGraphAnalog57761MQTTUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MQTTUserName.setStatus(_A)
_WtWebGraphAnalog57761MQTTPassword_Type=OctetString
_WtWebGraphAnalog57761MQTTPassword_Object=MibScalar
wtWebGraphAnalog57761MQTTPassword=_WtWebGraphAnalog57761MQTTPassword_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,12,4),_WtWebGraphAnalog57761MQTTPassword_Type())
wtWebGraphAnalog57761MQTTPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MQTTPassword.setStatus(_A)
_WtWebGraphAnalog57761MQTTLocalPort_Type=Integer32
_WtWebGraphAnalog57761MQTTLocalPort_Object=MibScalar
wtWebGraphAnalog57761MQTTLocalPort=_WtWebGraphAnalog57761MQTTLocalPort_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,12,5),_WtWebGraphAnalog57761MQTTLocalPort_Type())
wtWebGraphAnalog57761MQTTLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MQTTLocalPort.setStatus(_A)
_WtWebGraphAnalog57761MQTTBrokerServerPort_Type=Integer32
_WtWebGraphAnalog57761MQTTBrokerServerPort_Object=MibScalar
wtWebGraphAnalog57761MQTTBrokerServerPort=_WtWebGraphAnalog57761MQTTBrokerServerPort_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,12,6),_WtWebGraphAnalog57761MQTTBrokerServerPort_Type())
wtWebGraphAnalog57761MQTTBrokerServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MQTTBrokerServerPort.setStatus(_A)
_WtWebGraphAnalog57761MQTTInterval_Type=Integer32
_WtWebGraphAnalog57761MQTTInterval_Object=MibScalar
wtWebGraphAnalog57761MQTTInterval=_WtWebGraphAnalog57761MQTTInterval_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,12,7),_WtWebGraphAnalog57761MQTTInterval_Type())
wtWebGraphAnalog57761MQTTInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MQTTInterval.setStatus(_A)
_WtWebGraphAnalog57761MQTTLastWillEnable_Type=OctetString
_WtWebGraphAnalog57761MQTTLastWillEnable_Object=MibScalar
wtWebGraphAnalog57761MQTTLastWillEnable=_WtWebGraphAnalog57761MQTTLastWillEnable_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,12,8),_WtWebGraphAnalog57761MQTTLastWillEnable_Type())
wtWebGraphAnalog57761MQTTLastWillEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MQTTLastWillEnable.setStatus(_A)
_WtWebGraphAnalog57761MQTTLastWillTopic_Type=OctetString
_WtWebGraphAnalog57761MQTTLastWillTopic_Object=MibScalar
wtWebGraphAnalog57761MQTTLastWillTopic=_WtWebGraphAnalog57761MQTTLastWillTopic_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,12,9),_WtWebGraphAnalog57761MQTTLastWillTopic_Type())
wtWebGraphAnalog57761MQTTLastWillTopic.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MQTTLastWillTopic.setStatus(_A)
_WtWebGraphAnalog57761MQTTLastWillMsg_Type=OctetString
_WtWebGraphAnalog57761MQTTLastWillMsg_Object=MibScalar
wtWebGraphAnalog57761MQTTLastWillMsg=_WtWebGraphAnalog57761MQTTLastWillMsg_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,12,10),_WtWebGraphAnalog57761MQTTLastWillMsg_Type())
wtWebGraphAnalog57761MQTTLastWillMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MQTTLastWillMsg.setStatus(_A)
class _WtWebGraphAnalog57761MQTTLastWillQoS_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761MQTTLastWillQoS_Type.__name__=_D
_WtWebGraphAnalog57761MQTTLastWillQoS_Object=MibScalar
wtWebGraphAnalog57761MQTTLastWillQoS=_WtWebGraphAnalog57761MQTTLastWillQoS_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,12,11),_WtWebGraphAnalog57761MQTTLastWillQoS_Type())
wtWebGraphAnalog57761MQTTLastWillQoS.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MQTTLastWillQoS.setStatus(_A)
class _WtWebGraphAnalog57761MQTTLastWillRetain_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761MQTTLastWillRetain_Type.__name__=_D
_WtWebGraphAnalog57761MQTTLastWillRetain_Object=MibScalar
wtWebGraphAnalog57761MQTTLastWillRetain=_WtWebGraphAnalog57761MQTTLastWillRetain_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,12,12),_WtWebGraphAnalog57761MQTTLastWillRetain_Type())
wtWebGraphAnalog57761MQTTLastWillRetain.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MQTTLastWillRetain.setStatus(_A)
_WtWebGraphAnalog57761MQTTLastWillConnectEnable_Type=OctetString
_WtWebGraphAnalog57761MQTTLastWillConnectEnable_Object=MibScalar
wtWebGraphAnalog57761MQTTLastWillConnectEnable=_WtWebGraphAnalog57761MQTTLastWillConnectEnable_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,12,13),_WtWebGraphAnalog57761MQTTLastWillConnectEnable_Type())
wtWebGraphAnalog57761MQTTLastWillConnectEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MQTTLastWillConnectEnable.setStatus(_A)
_WtWebGraphAnalog57761MQTTLastWillConnectMsg_Type=OctetString
_WtWebGraphAnalog57761MQTTLastWillConnectMsg_Object=MibScalar
wtWebGraphAnalog57761MQTTLastWillConnectMsg=_WtWebGraphAnalog57761MQTTLastWillConnectMsg_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,12,14),_WtWebGraphAnalog57761MQTTLastWillConnectMsg_Type())
wtWebGraphAnalog57761MQTTLastWillConnectMsg.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MQTTLastWillConnectMsg.setStatus(_A)
_WtWebGraphAnalog57761REST_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761REST=_WtWebGraphAnalog57761REST_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,1,3,13))
_WtWebGraphAnalog57761RESTEnable_Type=OctetString
_WtWebGraphAnalog57761RESTEnable_Object=MibScalar
wtWebGraphAnalog57761RESTEnable=_WtWebGraphAnalog57761RESTEnable_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,13,1),_WtWebGraphAnalog57761RESTEnable_Type())
wtWebGraphAnalog57761RESTEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761RESTEnable.setStatus(_A)
_WtWebGraphAnalog57761RESTDigestAuthEnable_Type=OctetString
_WtWebGraphAnalog57761RESTDigestAuthEnable_Object=MibScalar
wtWebGraphAnalog57761RESTDigestAuthEnable=_WtWebGraphAnalog57761RESTDigestAuthEnable_Object((1,3,6,1,4,1,5040,1,2,28,3,1,3,13,2),_WtWebGraphAnalog57761RESTDigestAuthEnable_Type())
wtWebGraphAnalog57761RESTDigestAuthEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761RESTDigestAuthEnable.setStatus(_A)
_WtWebGraphAnalog57761Datalogger_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761Datalogger=_WtWebGraphAnalog57761Datalogger_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,1,4))
class _WtWebGraphAnalog57761LoggerTimebase_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('wtWebGraphAnalog57761Datalogger-15Sec',1),('wtWebGraphAnalog57761Datalogger-30Sec',2),('wtWebGraphAnalog57761Datalogger-1Min',3),('wtWebGraphAnalog57761Datalogger-5Min',4),('wtWebGraphAnalog57761Datalogger-15Min',5),('wtWebGraphAnalog57761Datalogger-60Min',6)))
_WtWebGraphAnalog57761LoggerTimebase_Type.__name__=_C
_WtWebGraphAnalog57761LoggerTimebase_Object=MibScalar
wtWebGraphAnalog57761LoggerTimebase=_WtWebGraphAnalog57761LoggerTimebase_Object((1,3,6,1,4,1,5040,1,2,28,3,1,4,1),_WtWebGraphAnalog57761LoggerTimebase_Type())
wtWebGraphAnalog57761LoggerTimebase.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761LoggerTimebase.setStatus(_A)
class _WtWebGraphAnalog57761LoggerSensorSel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761LoggerSensorSel_Type.__name__=_D
_WtWebGraphAnalog57761LoggerSensorSel_Object=MibScalar
wtWebGraphAnalog57761LoggerSensorSel=_WtWebGraphAnalog57761LoggerSensorSel_Object((1,3,6,1,4,1,5040,1,2,28,3,1,4,2),_WtWebGraphAnalog57761LoggerSensorSel_Type())
wtWebGraphAnalog57761LoggerSensorSel.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761LoggerSensorSel.setStatus(_A)
_WtWebGraphAnalog57761Alarm_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761Alarm=_WtWebGraphAnalog57761Alarm_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,1,5))
class _WtWebGraphAnalog57761AlarmCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_WtWebGraphAnalog57761AlarmCount_Type.__name__=_C
_WtWebGraphAnalog57761AlarmCount_Object=MibScalar
wtWebGraphAnalog57761AlarmCount=_WtWebGraphAnalog57761AlarmCount_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,1),_WtWebGraphAnalog57761AlarmCount_Type())
wtWebGraphAnalog57761AlarmCount.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmCount.setStatus(_A)
_WtWebGraphAnalog57761AlarmIfTable_Object=MibTable
wtWebGraphAnalog57761AlarmIfTable=_WtWebGraphAnalog57761AlarmIfTable_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,2))
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmIfTable.setStatus(_A)
_WtWebGraphAnalog57761AlarmIfEntry_Object=MibTableRow
wtWebGraphAnalog57761AlarmIfEntry=_WtWebGraphAnalog57761AlarmIfEntry_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,2,1))
wtWebGraphAnalog57761AlarmIfEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmIfEntry.setStatus(_A)
class _WtWebGraphAnalog57761AlarmNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_WtWebGraphAnalog57761AlarmNo_Type.__name__=_C
_WtWebGraphAnalog57761AlarmNo_Object=MibTableColumn
wtWebGraphAnalog57761AlarmNo=_WtWebGraphAnalog57761AlarmNo_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,2,1,1),_WtWebGraphAnalog57761AlarmNo_Type())
wtWebGraphAnalog57761AlarmNo.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmNo.setStatus(_A)
_WtWebGraphAnalog57761AlarmTable_Object=MibTable
wtWebGraphAnalog57761AlarmTable=_WtWebGraphAnalog57761AlarmTable_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3))
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmTable.setStatus(_A)
_WtWebGraphAnalog57761AlarmEntry_Object=MibTableRow
wtWebGraphAnalog57761AlarmEntry=_WtWebGraphAnalog57761AlarmEntry_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1))
wtWebGraphAnalog57761AlarmEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmEntry.setStatus(_A)
class _WtWebGraphAnalog57761AlarmTrigger_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761AlarmTrigger_Type.__name__=_D
_WtWebGraphAnalog57761AlarmTrigger_Object=MibTableColumn
wtWebGraphAnalog57761AlarmTrigger=_WtWebGraphAnalog57761AlarmTrigger_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,1),_WtWebGraphAnalog57761AlarmTrigger_Type())
wtWebGraphAnalog57761AlarmTrigger.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmTrigger.setStatus(_A)
_WtWebGraphAnalog57761AlarmMin1_Type=OctetString
_WtWebGraphAnalog57761AlarmMin1_Object=MibTableColumn
wtWebGraphAnalog57761AlarmMin1=_WtWebGraphAnalog57761AlarmMin1_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,2),_WtWebGraphAnalog57761AlarmMin1_Type())
wtWebGraphAnalog57761AlarmMin1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmMin1.setStatus(_A)
_WtWebGraphAnalog57761AlarmMax1_Type=OctetString
_WtWebGraphAnalog57761AlarmMax1_Object=MibTableColumn
wtWebGraphAnalog57761AlarmMax1=_WtWebGraphAnalog57761AlarmMax1_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,3),_WtWebGraphAnalog57761AlarmMax1_Type())
wtWebGraphAnalog57761AlarmMax1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmMax1.setStatus(_A)
_WtWebGraphAnalog57761AlarmHysteresis1_Type=OctetString
_WtWebGraphAnalog57761AlarmHysteresis1_Object=MibTableColumn
wtWebGraphAnalog57761AlarmHysteresis1=_WtWebGraphAnalog57761AlarmHysteresis1_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,4),_WtWebGraphAnalog57761AlarmHysteresis1_Type())
wtWebGraphAnalog57761AlarmHysteresis1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmHysteresis1.setStatus(_A)
_WtWebGraphAnalog57761AlarmDelay_Type=OctetString
_WtWebGraphAnalog57761AlarmDelay_Object=MibTableColumn
wtWebGraphAnalog57761AlarmDelay=_WtWebGraphAnalog57761AlarmDelay_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,5),_WtWebGraphAnalog57761AlarmDelay_Type())
wtWebGraphAnalog57761AlarmDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmDelay.setStatus(_A)
_WtWebGraphAnalog57761AlarmInterval_Type=OctetString
_WtWebGraphAnalog57761AlarmInterval_Object=MibTableColumn
wtWebGraphAnalog57761AlarmInterval=_WtWebGraphAnalog57761AlarmInterval_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,6),_WtWebGraphAnalog57761AlarmInterval_Type())
wtWebGraphAnalog57761AlarmInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmInterval.setStatus(_A)
class _WtWebGraphAnalog57761AlarmEnable_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761AlarmEnable_Type.__name__=_D
_WtWebGraphAnalog57761AlarmEnable_Object=MibTableColumn
wtWebGraphAnalog57761AlarmEnable=_WtWebGraphAnalog57761AlarmEnable_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,7),_WtWebGraphAnalog57761AlarmEnable_Type())
wtWebGraphAnalog57761AlarmEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmEnable.setStatus(_A)
_WtWebGraphAnalog57761AlarmEMailAddr_Type=OctetString
_WtWebGraphAnalog57761AlarmEMailAddr_Object=MibTableColumn
wtWebGraphAnalog57761AlarmEMailAddr=_WtWebGraphAnalog57761AlarmEMailAddr_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,8),_WtWebGraphAnalog57761AlarmEMailAddr_Type())
wtWebGraphAnalog57761AlarmEMailAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmEMailAddr.setStatus(_A)
_WtWebGraphAnalog57761AlarmMailSubject_Type=OctetString
_WtWebGraphAnalog57761AlarmMailSubject_Object=MibTableColumn
wtWebGraphAnalog57761AlarmMailSubject=_WtWebGraphAnalog57761AlarmMailSubject_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,9),_WtWebGraphAnalog57761AlarmMailSubject_Type())
wtWebGraphAnalog57761AlarmMailSubject.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmMailSubject.setStatus(_A)
_WtWebGraphAnalog57761AlarmMailText_Type=OctetString
_WtWebGraphAnalog57761AlarmMailText_Object=MibTableColumn
wtWebGraphAnalog57761AlarmMailText=_WtWebGraphAnalog57761AlarmMailText_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,10),_WtWebGraphAnalog57761AlarmMailText_Type())
wtWebGraphAnalog57761AlarmMailText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmMailText.setStatus(_A)
_WtWebGraphAnalog57761AlarmManagerIP_Type=OctetString
_WtWebGraphAnalog57761AlarmManagerIP_Object=MibTableColumn
wtWebGraphAnalog57761AlarmManagerIP=_WtWebGraphAnalog57761AlarmManagerIP_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,11),_WtWebGraphAnalog57761AlarmManagerIP_Type())
wtWebGraphAnalog57761AlarmManagerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmManagerIP.setStatus(_A)
_WtWebGraphAnalog57761AlarmTrapText_Type=OctetString
_WtWebGraphAnalog57761AlarmTrapText_Object=MibTableColumn
wtWebGraphAnalog57761AlarmTrapText=_WtWebGraphAnalog57761AlarmTrapText_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,12),_WtWebGraphAnalog57761AlarmTrapText_Type())
wtWebGraphAnalog57761AlarmTrapText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmTrapText.setStatus(_A)
class _WtWebGraphAnalog57761AlarmMailOptions_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761AlarmMailOptions_Type.__name__=_D
_WtWebGraphAnalog57761AlarmMailOptions_Object=MibTableColumn
wtWebGraphAnalog57761AlarmMailOptions=_WtWebGraphAnalog57761AlarmMailOptions_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,13),_WtWebGraphAnalog57761AlarmMailOptions_Type())
wtWebGraphAnalog57761AlarmMailOptions.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmMailOptions.setStatus(_A)
_WtWebGraphAnalog57761AlarmTcpIpAddr_Type=OctetString
_WtWebGraphAnalog57761AlarmTcpIpAddr_Object=MibTableColumn
wtWebGraphAnalog57761AlarmTcpIpAddr=_WtWebGraphAnalog57761AlarmTcpIpAddr_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,14),_WtWebGraphAnalog57761AlarmTcpIpAddr_Type())
wtWebGraphAnalog57761AlarmTcpIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmTcpIpAddr.setStatus(_A)
class _WtWebGraphAnalog57761AlarmTcpPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphAnalog57761AlarmTcpPort_Type.__name__=_C
_WtWebGraphAnalog57761AlarmTcpPort_Object=MibTableColumn
wtWebGraphAnalog57761AlarmTcpPort=_WtWebGraphAnalog57761AlarmTcpPort_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,15),_WtWebGraphAnalog57761AlarmTcpPort_Type())
wtWebGraphAnalog57761AlarmTcpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmTcpPort.setStatus(_A)
_WtWebGraphAnalog57761AlarmTcpText_Type=OctetString
_WtWebGraphAnalog57761AlarmTcpText_Object=MibTableColumn
wtWebGraphAnalog57761AlarmTcpText=_WtWebGraphAnalog57761AlarmTcpText_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,16),_WtWebGraphAnalog57761AlarmTcpText_Type())
wtWebGraphAnalog57761AlarmTcpText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmTcpText.setStatus(_A)
_WtWebGraphAnalog57761AlarmClearMailSubject_Type=OctetString
_WtWebGraphAnalog57761AlarmClearMailSubject_Object=MibTableColumn
wtWebGraphAnalog57761AlarmClearMailSubject=_WtWebGraphAnalog57761AlarmClearMailSubject_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,17),_WtWebGraphAnalog57761AlarmClearMailSubject_Type())
wtWebGraphAnalog57761AlarmClearMailSubject.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmClearMailSubject.setStatus(_A)
_WtWebGraphAnalog57761AlarmClearMailText_Type=OctetString
_WtWebGraphAnalog57761AlarmClearMailText_Object=MibTableColumn
wtWebGraphAnalog57761AlarmClearMailText=_WtWebGraphAnalog57761AlarmClearMailText_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,18),_WtWebGraphAnalog57761AlarmClearMailText_Type())
wtWebGraphAnalog57761AlarmClearMailText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmClearMailText.setStatus(_A)
_WtWebGraphAnalog57761AlarmClearTrapText_Type=OctetString
_WtWebGraphAnalog57761AlarmClearTrapText_Object=MibTableColumn
wtWebGraphAnalog57761AlarmClearTrapText=_WtWebGraphAnalog57761AlarmClearTrapText_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,19),_WtWebGraphAnalog57761AlarmClearTrapText_Type())
wtWebGraphAnalog57761AlarmClearTrapText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmClearTrapText.setStatus(_A)
_WtWebGraphAnalog57761AlarmClearTcpText_Type=OctetString
_WtWebGraphAnalog57761AlarmClearTcpText_Object=MibTableColumn
wtWebGraphAnalog57761AlarmClearTcpText=_WtWebGraphAnalog57761AlarmClearTcpText_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,20),_WtWebGraphAnalog57761AlarmClearTcpText_Type())
wtWebGraphAnalog57761AlarmClearTcpText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmClearTcpText.setStatus(_A)
_WtWebGraphAnalog57761AlarmMin2_Type=OctetString
_WtWebGraphAnalog57761AlarmMin2_Object=MibTableColumn
wtWebGraphAnalog57761AlarmMin2=_WtWebGraphAnalog57761AlarmMin2_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,21),_WtWebGraphAnalog57761AlarmMin2_Type())
wtWebGraphAnalog57761AlarmMin2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmMin2.setStatus(_A)
_WtWebGraphAnalog57761AlarmMax2_Type=OctetString
_WtWebGraphAnalog57761AlarmMax2_Object=MibTableColumn
wtWebGraphAnalog57761AlarmMax2=_WtWebGraphAnalog57761AlarmMax2_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,22),_WtWebGraphAnalog57761AlarmMax2_Type())
wtWebGraphAnalog57761AlarmMax2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmMax2.setStatus(_A)
_WtWebGraphAnalog57761AlarmHysteresis2_Type=OctetString
_WtWebGraphAnalog57761AlarmHysteresis2_Object=MibTableColumn
wtWebGraphAnalog57761AlarmHysteresis2=_WtWebGraphAnalog57761AlarmHysteresis2_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,23),_WtWebGraphAnalog57761AlarmHysteresis2_Type())
wtWebGraphAnalog57761AlarmHysteresis2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmHysteresis2.setStatus(_A)
_WtWebGraphAnalog57761AlarmSyslogIpAddr_Type=OctetString
_WtWebGraphAnalog57761AlarmSyslogIpAddr_Object=MibTableColumn
wtWebGraphAnalog57761AlarmSyslogIpAddr=_WtWebGraphAnalog57761AlarmSyslogIpAddr_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,24),_WtWebGraphAnalog57761AlarmSyslogIpAddr_Type())
wtWebGraphAnalog57761AlarmSyslogIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmSyslogIpAddr.setStatus(_A)
class _WtWebGraphAnalog57761AlarmSyslogPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphAnalog57761AlarmSyslogPort_Type.__name__=_C
_WtWebGraphAnalog57761AlarmSyslogPort_Object=MibTableColumn
wtWebGraphAnalog57761AlarmSyslogPort=_WtWebGraphAnalog57761AlarmSyslogPort_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,25),_WtWebGraphAnalog57761AlarmSyslogPort_Type())
wtWebGraphAnalog57761AlarmSyslogPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmSyslogPort.setStatus(_A)
_WtWebGraphAnalog57761AlarmSyslogText_Type=OctetString
_WtWebGraphAnalog57761AlarmSyslogText_Object=MibTableColumn
wtWebGraphAnalog57761AlarmSyslogText=_WtWebGraphAnalog57761AlarmSyslogText_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,26),_WtWebGraphAnalog57761AlarmSyslogText_Type())
wtWebGraphAnalog57761AlarmSyslogText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmSyslogText.setStatus(_A)
_WtWebGraphAnalog57761AlarmSyslogClearText_Type=OctetString
_WtWebGraphAnalog57761AlarmSyslogClearText_Object=MibTableColumn
wtWebGraphAnalog57761AlarmSyslogClearText=_WtWebGraphAnalog57761AlarmSyslogClearText_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,27),_WtWebGraphAnalog57761AlarmSyslogClearText_Type())
wtWebGraphAnalog57761AlarmSyslogClearText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmSyslogClearText.setStatus(_A)
_WtWebGraphAnalog57761AlarmFtpDataPort_Type=OctetString
_WtWebGraphAnalog57761AlarmFtpDataPort_Object=MibTableColumn
wtWebGraphAnalog57761AlarmFtpDataPort=_WtWebGraphAnalog57761AlarmFtpDataPort_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,28),_WtWebGraphAnalog57761AlarmFtpDataPort_Type())
wtWebGraphAnalog57761AlarmFtpDataPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmFtpDataPort.setStatus(_A)
_WtWebGraphAnalog57761AlarmFtpFileName_Type=OctetString
_WtWebGraphAnalog57761AlarmFtpFileName_Object=MibTableColumn
wtWebGraphAnalog57761AlarmFtpFileName=_WtWebGraphAnalog57761AlarmFtpFileName_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,29),_WtWebGraphAnalog57761AlarmFtpFileName_Type())
wtWebGraphAnalog57761AlarmFtpFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmFtpFileName.setStatus(_A)
_WtWebGraphAnalog57761AlarmFtpText_Type=OctetString
_WtWebGraphAnalog57761AlarmFtpText_Object=MibTableColumn
wtWebGraphAnalog57761AlarmFtpText=_WtWebGraphAnalog57761AlarmFtpText_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,30),_WtWebGraphAnalog57761AlarmFtpText_Type())
wtWebGraphAnalog57761AlarmFtpText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmFtpText.setStatus(_A)
_WtWebGraphAnalog57761AlarmFtpClearText_Type=OctetString
_WtWebGraphAnalog57761AlarmFtpClearText_Object=MibTableColumn
wtWebGraphAnalog57761AlarmFtpClearText=_WtWebGraphAnalog57761AlarmFtpClearText_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,31),_WtWebGraphAnalog57761AlarmFtpClearText_Type())
wtWebGraphAnalog57761AlarmFtpClearText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmFtpClearText.setStatus(_A)
class _WtWebGraphAnalog57761AlarmFtpOption_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761AlarmFtpOption_Type.__name__=_D
_WtWebGraphAnalog57761AlarmFtpOption_Object=MibTableColumn
wtWebGraphAnalog57761AlarmFtpOption=_WtWebGraphAnalog57761AlarmFtpOption_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,32),_WtWebGraphAnalog57761AlarmFtpOption_Type())
wtWebGraphAnalog57761AlarmFtpOption.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmFtpOption.setStatus(_A)
_WtWebGraphAnalog57761AlarmTimerCron_Type=OctetString
_WtWebGraphAnalog57761AlarmTimerCron_Object=MibTableColumn
wtWebGraphAnalog57761AlarmTimerCron=_WtWebGraphAnalog57761AlarmTimerCron_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,33),_WtWebGraphAnalog57761AlarmTimerCron_Type())
wtWebGraphAnalog57761AlarmTimerCron.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmTimerCron.setStatus(_A)
_WtWebGraphAnalog57761AlarmName_Type=OctetString
_WtWebGraphAnalog57761AlarmName_Object=MibTableColumn
wtWebGraphAnalog57761AlarmName=_WtWebGraphAnalog57761AlarmName_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,39),_WtWebGraphAnalog57761AlarmName_Type())
wtWebGraphAnalog57761AlarmName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmName.setStatus(_A)
_WtWebGraphAnalog57761AlarmActive_Type=OctetString
_WtWebGraphAnalog57761AlarmActive_Object=MibTableColumn
wtWebGraphAnalog57761AlarmActive=_WtWebGraphAnalog57761AlarmActive_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,40),_WtWebGraphAnalog57761AlarmActive_Type())
wtWebGraphAnalog57761AlarmActive.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmActive.setStatus(_A)
_WtWebGraphAnalog57761AlarmHttpReqAuthEnable_Type=OctetString
_WtWebGraphAnalog57761AlarmHttpReqAuthEnable_Object=MibTableColumn
wtWebGraphAnalog57761AlarmHttpReqAuthEnable=_WtWebGraphAnalog57761AlarmHttpReqAuthEnable_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,61),_WtWebGraphAnalog57761AlarmHttpReqAuthEnable_Type())
wtWebGraphAnalog57761AlarmHttpReqAuthEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmHttpReqAuthEnable.setStatus(_A)
_WtWebGraphAnalog57761AlarmHttpReqAuthUser_Type=OctetString
_WtWebGraphAnalog57761AlarmHttpReqAuthUser_Object=MibTableColumn
wtWebGraphAnalog57761AlarmHttpReqAuthUser=_WtWebGraphAnalog57761AlarmHttpReqAuthUser_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,62),_WtWebGraphAnalog57761AlarmHttpReqAuthUser_Type())
wtWebGraphAnalog57761AlarmHttpReqAuthUser.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmHttpReqAuthUser.setStatus(_A)
_WtWebGraphAnalog57761AlarmHttpReqAuthPassword_Type=OctetString
_WtWebGraphAnalog57761AlarmHttpReqAuthPassword_Object=MibTableColumn
wtWebGraphAnalog57761AlarmHttpReqAuthPassword=_WtWebGraphAnalog57761AlarmHttpReqAuthPassword_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,63),_WtWebGraphAnalog57761AlarmHttpReqAuthPassword_Type())
wtWebGraphAnalog57761AlarmHttpReqAuthPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmHttpReqAuthPassword.setStatus(_A)
_WtWebGraphAnalog57761AlarmHttpReqSetUrl_Type=OctetString
_WtWebGraphAnalog57761AlarmHttpReqSetUrl_Object=MibTableColumn
wtWebGraphAnalog57761AlarmHttpReqSetUrl=_WtWebGraphAnalog57761AlarmHttpReqSetUrl_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,64),_WtWebGraphAnalog57761AlarmHttpReqSetUrl_Type())
wtWebGraphAnalog57761AlarmHttpReqSetUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmHttpReqSetUrl.setStatus(_A)
_WtWebGraphAnalog57761AlarmHttpReqClearUrl_Type=OctetString
_WtWebGraphAnalog57761AlarmHttpReqClearUrl_Object=MibTableColumn
wtWebGraphAnalog57761AlarmHttpReqClearUrl=_WtWebGraphAnalog57761AlarmHttpReqClearUrl_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,65),_WtWebGraphAnalog57761AlarmHttpReqClearUrl_Type())
wtWebGraphAnalog57761AlarmHttpReqClearUrl.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmHttpReqClearUrl.setStatus(_A)
class _WtWebGraphAnalog57761AlarmHttpReqServerPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WtWebGraphAnalog57761AlarmHttpReqServerPort_Type.__name__=_C
_WtWebGraphAnalog57761AlarmHttpReqServerPort_Object=MibTableColumn
wtWebGraphAnalog57761AlarmHttpReqServerPort=_WtWebGraphAnalog57761AlarmHttpReqServerPort_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,66),_WtWebGraphAnalog57761AlarmHttpReqServerPort_Type())
wtWebGraphAnalog57761AlarmHttpReqServerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmHttpReqServerPort.setStatus(_A)
_WtWebGraphAnalog57761AlarmMqttTopicPath_Type=OctetString
_WtWebGraphAnalog57761AlarmMqttTopicPath_Object=MibTableColumn
wtWebGraphAnalog57761AlarmMqttTopicPath=_WtWebGraphAnalog57761AlarmMqttTopicPath_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,67),_WtWebGraphAnalog57761AlarmMqttTopicPath_Type())
wtWebGraphAnalog57761AlarmMqttTopicPath.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmMqttTopicPath.setStatus(_A)
_WtWebGraphAnalog57761AlarmMqttTopicSetTopic_Type=OctetString
_WtWebGraphAnalog57761AlarmMqttTopicSetTopic_Object=MibTableColumn
wtWebGraphAnalog57761AlarmMqttTopicSetTopic=_WtWebGraphAnalog57761AlarmMqttTopicSetTopic_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,68),_WtWebGraphAnalog57761AlarmMqttTopicSetTopic_Type())
wtWebGraphAnalog57761AlarmMqttTopicSetTopic.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmMqttTopicSetTopic.setStatus(_A)
_WtWebGraphAnalog57761AlarmMqttTopicClear_Type=OctetString
_WtWebGraphAnalog57761AlarmMqttTopicClear_Object=MibTableColumn
wtWebGraphAnalog57761AlarmMqttTopicClear=_WtWebGraphAnalog57761AlarmMqttTopicClear_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,69),_WtWebGraphAnalog57761AlarmMqttTopicClear_Type())
wtWebGraphAnalog57761AlarmMqttTopicClear.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmMqttTopicClear.setStatus(_A)
_WtWebGraphAnalog57761AlarmSensorLostSelection_Type=OctetString
_WtWebGraphAnalog57761AlarmSensorLostSelection_Object=MibTableColumn
wtWebGraphAnalog57761AlarmSensorLostSelection=_WtWebGraphAnalog57761AlarmSensorLostSelection_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,70),_WtWebGraphAnalog57761AlarmSensorLostSelection_Type())
wtWebGraphAnalog57761AlarmSensorLostSelection.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmSensorLostSelection.setStatus(_A)
_WtWebGraphAnalog57761AlarmLimitWindow_Type=OctetString
_WtWebGraphAnalog57761AlarmLimitWindow_Object=MibTableColumn
wtWebGraphAnalog57761AlarmLimitWindow=_WtWebGraphAnalog57761AlarmLimitWindow_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,71),_WtWebGraphAnalog57761AlarmLimitWindow_Type())
wtWebGraphAnalog57761AlarmLimitWindow.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmLimitWindow.setStatus(_A)
_WtWebGraphAnalog57761AlarmSnmpManagerPort_Type=Integer32
_WtWebGraphAnalog57761AlarmSnmpManagerPort_Object=MibTableColumn
wtWebGraphAnalog57761AlarmSnmpManagerPort=_WtWebGraphAnalog57761AlarmSnmpManagerPort_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,76),_WtWebGraphAnalog57761AlarmSnmpManagerPort_Type())
wtWebGraphAnalog57761AlarmSnmpManagerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmSnmpManagerPort.setStatus(_A)
class _WtWebGraphAnalog57761AlarmMqttQoS_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761AlarmMqttQoS_Type.__name__=_D
_WtWebGraphAnalog57761AlarmMqttQoS_Object=MibTableColumn
wtWebGraphAnalog57761AlarmMqttQoS=_WtWebGraphAnalog57761AlarmMqttQoS_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,77),_WtWebGraphAnalog57761AlarmMqttQoS_Type())
wtWebGraphAnalog57761AlarmMqttQoS.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmMqttQoS.setStatus(_A)
class _WtWebGraphAnalog57761AlarmMqttRetain_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761AlarmMqttRetain_Type.__name__=_D
_WtWebGraphAnalog57761AlarmMqttRetain_Object=MibTableColumn
wtWebGraphAnalog57761AlarmMqttRetain=_WtWebGraphAnalog57761AlarmMqttRetain_Object((1,3,6,1,4,1,5040,1,2,28,3,1,5,3,1,78),_WtWebGraphAnalog57761AlarmMqttRetain_Type())
wtWebGraphAnalog57761AlarmMqttRetain.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlarmMqttRetain.setStatus(_A)
_WtWebGraphAnalog57761Graphics_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761Graphics=_WtWebGraphAnalog57761Graphics_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,1,6))
_WtWebGraphAnalog57761GraphicsBase_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761GraphicsBase=_WtWebGraphAnalog57761GraphicsBase_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,1,6,1))
_WtWebGraphAnalog57761GraphicsBaseEnable_Type=OctetString
_WtWebGraphAnalog57761GraphicsBaseEnable_Object=MibScalar
wtWebGraphAnalog57761GraphicsBaseEnable=_WtWebGraphAnalog57761GraphicsBaseEnable_Object((1,3,6,1,4,1,5040,1,2,28,3,1,6,1,1),_WtWebGraphAnalog57761GraphicsBaseEnable_Type())
wtWebGraphAnalog57761GraphicsBaseEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761GraphicsBaseEnable.setStatus(_A)
_WtWebGraphAnalog57761GraphicsBaseWidth_Type=Integer32
_WtWebGraphAnalog57761GraphicsBaseWidth_Object=MibScalar
wtWebGraphAnalog57761GraphicsBaseWidth=_WtWebGraphAnalog57761GraphicsBaseWidth_Object((1,3,6,1,4,1,5040,1,2,28,3,1,6,1,2),_WtWebGraphAnalog57761GraphicsBaseWidth_Type())
wtWebGraphAnalog57761GraphicsBaseWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761GraphicsBaseWidth.setStatus(_A)
_WtWebGraphAnalog57761GraphicsBaseHeight_Type=Integer32
_WtWebGraphAnalog57761GraphicsBaseHeight_Object=MibScalar
wtWebGraphAnalog57761GraphicsBaseHeight=_WtWebGraphAnalog57761GraphicsBaseHeight_Object((1,3,6,1,4,1,5040,1,2,28,3,1,6,1,3),_WtWebGraphAnalog57761GraphicsBaseHeight_Type())
wtWebGraphAnalog57761GraphicsBaseHeight.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761GraphicsBaseHeight.setStatus(_A)
class _WtWebGraphAnalog57761GraphicsBaseFrameColor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_WtWebGraphAnalog57761GraphicsBaseFrameColor_Type.__name__=_D
_WtWebGraphAnalog57761GraphicsBaseFrameColor_Object=MibScalar
wtWebGraphAnalog57761GraphicsBaseFrameColor=_WtWebGraphAnalog57761GraphicsBaseFrameColor_Object((1,3,6,1,4,1,5040,1,2,28,3,1,6,1,4),_WtWebGraphAnalog57761GraphicsBaseFrameColor_Type())
wtWebGraphAnalog57761GraphicsBaseFrameColor.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761GraphicsBaseFrameColor.setStatus(_A)
class _WtWebGraphAnalog57761GraphicsBaseBackgroundColor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_WtWebGraphAnalog57761GraphicsBaseBackgroundColor_Type.__name__=_D
_WtWebGraphAnalog57761GraphicsBaseBackgroundColor_Object=MibScalar
wtWebGraphAnalog57761GraphicsBaseBackgroundColor=_WtWebGraphAnalog57761GraphicsBaseBackgroundColor_Object((1,3,6,1,4,1,5040,1,2,28,3,1,6,1,5),_WtWebGraphAnalog57761GraphicsBaseBackgroundColor_Type())
wtWebGraphAnalog57761GraphicsBaseBackgroundColor.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761GraphicsBaseBackgroundColor.setStatus(_A)
_WtWebGraphAnalog57761GraphicsBasePollingrate_Type=Integer32
_WtWebGraphAnalog57761GraphicsBasePollingrate_Object=MibScalar
wtWebGraphAnalog57761GraphicsBasePollingrate=_WtWebGraphAnalog57761GraphicsBasePollingrate_Object((1,3,6,1,4,1,5040,1,2,28,3,1,6,1,6),_WtWebGraphAnalog57761GraphicsBasePollingrate_Type())
wtWebGraphAnalog57761GraphicsBasePollingrate.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761GraphicsBasePollingrate.setStatus(_A)
_WtWebGraphAnalog57761GraphicsSelect_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761GraphicsSelect=_WtWebGraphAnalog57761GraphicsSelect_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,1,6,2))
class _WtWebGraphAnalog57761GraphicsSelectDisplaySensorSel_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761GraphicsSelectDisplaySensorSel_Type.__name__=_D
_WtWebGraphAnalog57761GraphicsSelectDisplaySensorSel_Object=MibScalar
wtWebGraphAnalog57761GraphicsSelectDisplaySensorSel=_WtWebGraphAnalog57761GraphicsSelectDisplaySensorSel_Object((1,3,6,1,4,1,5040,1,2,28,3,1,6,2,1),_WtWebGraphAnalog57761GraphicsSelectDisplaySensorSel_Type())
wtWebGraphAnalog57761GraphicsSelectDisplaySensorSel.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761GraphicsSelectDisplaySensorSel.setStatus(_A)
class _WtWebGraphAnalog57761GraphicsSelectDisplayShowExtrem_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761GraphicsSelectDisplayShowExtrem_Type.__name__=_D
_WtWebGraphAnalog57761GraphicsSelectDisplayShowExtrem_Object=MibScalar
wtWebGraphAnalog57761GraphicsSelectDisplayShowExtrem=_WtWebGraphAnalog57761GraphicsSelectDisplayShowExtrem_Object((1,3,6,1,4,1,5040,1,2,28,3,1,6,2,2),_WtWebGraphAnalog57761GraphicsSelectDisplayShowExtrem_Type())
wtWebGraphAnalog57761GraphicsSelectDisplayShowExtrem.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761GraphicsSelectDisplayShowExtrem.setStatus(_A)
_WtWebGraphAnalog57761SensorColor2Table_Object=MibTable
wtWebGraphAnalog57761SensorColor2Table=_WtWebGraphAnalog57761SensorColor2Table_Object((1,3,6,1,4,1,5040,1,2,28,3,1,6,2,3))
if mibBuilder.loadTexts:wtWebGraphAnalog57761SensorColor2Table.setStatus(_A)
_WtWebGraphAnalog57761SensorColor2Entry_Object=MibTableRow
wtWebGraphAnalog57761SensorColor2Entry=_WtWebGraphAnalog57761SensorColor2Entry_Object((1,3,6,1,4,1,5040,1,2,28,3,1,6,2,3,1))
wtWebGraphAnalog57761SensorColor2Entry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:wtWebGraphAnalog57761SensorColor2Entry.setStatus(_A)
class _WtWebGraphAnalog57761GraphicsSensorColor_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_WtWebGraphAnalog57761GraphicsSensorColor_Type.__name__=_D
_WtWebGraphAnalog57761GraphicsSensorColor_Object=MibTableColumn
wtWebGraphAnalog57761GraphicsSensorColor=_WtWebGraphAnalog57761GraphicsSensorColor_Object((1,3,6,1,4,1,5040,1,2,28,3,1,6,2,3,1,1),_WtWebGraphAnalog57761GraphicsSensorColor_Type())
wtWebGraphAnalog57761GraphicsSensorColor.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761GraphicsSensorColor.setStatus(_A)
_WtWebGraphAnalog57761GraphicsSelectScale_Type=OctetString
_WtWebGraphAnalog57761GraphicsSelectScale_Object=MibTableColumn
wtWebGraphAnalog57761GraphicsSelectScale=_WtWebGraphAnalog57761GraphicsSelectScale_Object((1,3,6,1,4,1,5040,1,2,28,3,1,6,2,3,1,2),_WtWebGraphAnalog57761GraphicsSelectScale_Type())
wtWebGraphAnalog57761GraphicsSelectScale.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761GraphicsSelectScale.setStatus(_A)
_WtWebGraphAnalog57761GraphicsScale_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761GraphicsScale=_WtWebGraphAnalog57761GraphicsScale_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,1,6,3))
_WtWebGraphAnalog57761GraphicsScaleAutoScaleEnable_Type=OctetString
_WtWebGraphAnalog57761GraphicsScaleAutoScaleEnable_Object=MibScalar
wtWebGraphAnalog57761GraphicsScaleAutoScaleEnable=_WtWebGraphAnalog57761GraphicsScaleAutoScaleEnable_Object((1,3,6,1,4,1,5040,1,2,28,3,1,6,3,1),_WtWebGraphAnalog57761GraphicsScaleAutoScaleEnable_Type())
wtWebGraphAnalog57761GraphicsScaleAutoScaleEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761GraphicsScaleAutoScaleEnable.setStatus(_A)
_WtWebGraphAnalog57761GraphicsScaleAutoFitEnable_Type=OctetString
_WtWebGraphAnalog57761GraphicsScaleAutoFitEnable_Object=MibScalar
wtWebGraphAnalog57761GraphicsScaleAutoFitEnable=_WtWebGraphAnalog57761GraphicsScaleAutoFitEnable_Object((1,3,6,1,4,1,5040,1,2,28,3,1,6,3,2),_WtWebGraphAnalog57761GraphicsScaleAutoFitEnable_Type())
wtWebGraphAnalog57761GraphicsScaleAutoFitEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761GraphicsScaleAutoFitEnable.setStatus(_A)
_WtWebGraphAnalog57761GraphicsScale1Min_Type=Integer32
_WtWebGraphAnalog57761GraphicsScale1Min_Object=MibScalar
wtWebGraphAnalog57761GraphicsScale1Min=_WtWebGraphAnalog57761GraphicsScale1Min_Object((1,3,6,1,4,1,5040,1,2,28,3,1,6,3,3),_WtWebGraphAnalog57761GraphicsScale1Min_Type())
wtWebGraphAnalog57761GraphicsScale1Min.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphAnalog57761GraphicsScale1Min.setStatus(_A)
_WtWebGraphAnalog57761GraphicsScale2Min_Type=Integer32
_WtWebGraphAnalog57761GraphicsScale2Min_Object=MibScalar
wtWebGraphAnalog57761GraphicsScale2Min=_WtWebGraphAnalog57761GraphicsScale2Min_Object((1,3,6,1,4,1,5040,1,2,28,3,1,6,3,4),_WtWebGraphAnalog57761GraphicsScale2Min_Type())
wtWebGraphAnalog57761GraphicsScale2Min.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphAnalog57761GraphicsScale2Min.setStatus(_A)
_WtWebGraphAnalog57761GraphicsScale1Max_Type=Integer32
_WtWebGraphAnalog57761GraphicsScale1Max_Object=MibScalar
wtWebGraphAnalog57761GraphicsScale1Max=_WtWebGraphAnalog57761GraphicsScale1Max_Object((1,3,6,1,4,1,5040,1,2,28,3,1,6,3,7),_WtWebGraphAnalog57761GraphicsScale1Max_Type())
wtWebGraphAnalog57761GraphicsScale1Max.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphAnalog57761GraphicsScale1Max.setStatus(_A)
_WtWebGraphAnalog57761GraphicsScale2Max_Type=Integer32
_WtWebGraphAnalog57761GraphicsScale2Max_Object=MibScalar
wtWebGraphAnalog57761GraphicsScale2Max=_WtWebGraphAnalog57761GraphicsScale2Max_Object((1,3,6,1,4,1,5040,1,2,28,3,1,6,3,8),_WtWebGraphAnalog57761GraphicsScale2Max_Type())
wtWebGraphAnalog57761GraphicsScale2Max.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphAnalog57761GraphicsScale2Max.setStatus(_A)
_WtWebGraphAnalog57761GraphicsScale1Unit_Type=OctetString
_WtWebGraphAnalog57761GraphicsScale1Unit_Object=MibScalar
wtWebGraphAnalog57761GraphicsScale1Unit=_WtWebGraphAnalog57761GraphicsScale1Unit_Object((1,3,6,1,4,1,5040,1,2,28,3,1,6,3,11),_WtWebGraphAnalog57761GraphicsScale1Unit_Type())
wtWebGraphAnalog57761GraphicsScale1Unit.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphAnalog57761GraphicsScale1Unit.setStatus(_A)
_WtWebGraphAnalog57761GraphicsScale2Unit_Type=OctetString
_WtWebGraphAnalog57761GraphicsScale2Unit_Object=MibScalar
wtWebGraphAnalog57761GraphicsScale2Unit=_WtWebGraphAnalog57761GraphicsScale2Unit_Object((1,3,6,1,4,1,5040,1,2,28,3,1,6,3,12),_WtWebGraphAnalog57761GraphicsScale2Unit_Type())
wtWebGraphAnalog57761GraphicsScale2Unit.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphAnalog57761GraphicsScale2Unit.setStatus(_A)
_WtWebGraphAnalog57761Ports_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761Ports=_WtWebGraphAnalog57761Ports_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,2))
_WtWebGraphAnalog57761PortTable_Object=MibTable
wtWebGraphAnalog57761PortTable=_WtWebGraphAnalog57761PortTable_Object((1,3,6,1,4,1,5040,1,2,28,3,2,1))
if mibBuilder.loadTexts:wtWebGraphAnalog57761PortTable.setStatus(_A)
_WtWebGraphAnalog57761PortEntry_Object=MibTableRow
wtWebGraphAnalog57761PortEntry=_WtWebGraphAnalog57761PortEntry_Object((1,3,6,1,4,1,5040,1,2,28,3,2,1,1))
wtWebGraphAnalog57761PortEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:wtWebGraphAnalog57761PortEntry.setStatus(_A)
_WtWebGraphAnalog57761PortName_Type=OctetString
_WtWebGraphAnalog57761PortName_Object=MibTableColumn
wtWebGraphAnalog57761PortName=_WtWebGraphAnalog57761PortName_Object((1,3,6,1,4,1,5040,1,2,28,3,2,1,1,1),_WtWebGraphAnalog57761PortName_Type())
wtWebGraphAnalog57761PortName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761PortName.setStatus(_A)
_WtWebGraphAnalog57761PortText_Type=OctetString
_WtWebGraphAnalog57761PortText_Object=MibTableColumn
wtWebGraphAnalog57761PortText=_WtWebGraphAnalog57761PortText_Object((1,3,6,1,4,1,5040,1,2,28,3,2,1,1,2),_WtWebGraphAnalog57761PortText_Type())
wtWebGraphAnalog57761PortText.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761PortText.setStatus(_A)
_WtWebGraphAnalog57761PortOffset1_Type=OctetString
_WtWebGraphAnalog57761PortOffset1_Object=MibTableColumn
wtWebGraphAnalog57761PortOffset1=_WtWebGraphAnalog57761PortOffset1_Object((1,3,6,1,4,1,5040,1,2,28,3,2,1,1,3),_WtWebGraphAnalog57761PortOffset1_Type())
wtWebGraphAnalog57761PortOffset1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761PortOffset1.setStatus(_A)
_WtWebGraphAnalog57761SetPoint1_Type=OctetString
_WtWebGraphAnalog57761SetPoint1_Object=MibTableColumn
wtWebGraphAnalog57761SetPoint1=_WtWebGraphAnalog57761SetPoint1_Object((1,3,6,1,4,1,5040,1,2,28,3,2,1,1,4),_WtWebGraphAnalog57761SetPoint1_Type())
wtWebGraphAnalog57761SetPoint1.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761SetPoint1.setStatus(_A)
_WtWebGraphAnalog57761PortOffset2_Type=OctetString
_WtWebGraphAnalog57761PortOffset2_Object=MibTableColumn
wtWebGraphAnalog57761PortOffset2=_WtWebGraphAnalog57761PortOffset2_Object((1,3,6,1,4,1,5040,1,2,28,3,2,1,1,5),_WtWebGraphAnalog57761PortOffset2_Type())
wtWebGraphAnalog57761PortOffset2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761PortOffset2.setStatus(_A)
_WtWebGraphAnalog57761SetPoint2_Type=OctetString
_WtWebGraphAnalog57761SetPoint2_Object=MibTableColumn
wtWebGraphAnalog57761SetPoint2=_WtWebGraphAnalog57761SetPoint2_Object((1,3,6,1,4,1,5040,1,2,28,3,2,1,1,6),_WtWebGraphAnalog57761SetPoint2_Type())
wtWebGraphAnalog57761SetPoint2.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761SetPoint2.setStatus(_A)
_WtWebGraphAnalog57761PortComment_Type=OctetString
_WtWebGraphAnalog57761PortComment_Object=MibTableColumn
wtWebGraphAnalog57761PortComment=_WtWebGraphAnalog57761PortComment_Object((1,3,6,1,4,1,5040,1,2,28,3,2,1,1,7),_WtWebGraphAnalog57761PortComment_Type())
wtWebGraphAnalog57761PortComment.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761PortComment.setStatus(_A)
class _WtWebGraphAnalog57761PortSensorSelect_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761PortSensorSelect_Type.__name__=_D
_WtWebGraphAnalog57761PortSensorSelect_Object=MibTableColumn
wtWebGraphAnalog57761PortSensorSelect=_WtWebGraphAnalog57761PortSensorSelect_Object((1,3,6,1,4,1,5040,1,2,28,3,2,1,1,8),_WtWebGraphAnalog57761PortSensorSelect_Type())
wtWebGraphAnalog57761PortSensorSelect.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761PortSensorSelect.setStatus(_A)
_WtWebGraphAnalog57761PortUnit_Type=OctetString
_WtWebGraphAnalog57761PortUnit_Object=MibTableColumn
wtWebGraphAnalog57761PortUnit=_WtWebGraphAnalog57761PortUnit_Object((1,3,6,1,4,1,5040,1,2,28,3,2,1,1,9),_WtWebGraphAnalog57761PortUnit_Type())
wtWebGraphAnalog57761PortUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761PortUnit.setStatus(_A)
_WtWebGraphAnalog57761PortScale0_Type=OctetString
_WtWebGraphAnalog57761PortScale0_Object=MibTableColumn
wtWebGraphAnalog57761PortScale0=_WtWebGraphAnalog57761PortScale0_Object((1,3,6,1,4,1,5040,1,2,28,3,2,1,1,10),_WtWebGraphAnalog57761PortScale0_Type())
wtWebGraphAnalog57761PortScale0.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761PortScale0.setStatus(_A)
_WtWebGraphAnalog57761PortScale100_Type=OctetString
_WtWebGraphAnalog57761PortScale100_Object=MibTableColumn
wtWebGraphAnalog57761PortScale100=_WtWebGraphAnalog57761PortScale100_Object((1,3,6,1,4,1,5040,1,2,28,3,2,1,1,11),_WtWebGraphAnalog57761PortScale100_Type())
wtWebGraphAnalog57761PortScale100.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761PortScale100.setStatus(_A)
class _WtWebGraphAnalog57761PortOutputMode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761PortOutputMode_Type.__name__=_D
_WtWebGraphAnalog57761PortOutputMode_Object=MibTableColumn
wtWebGraphAnalog57761PortOutputMode=_WtWebGraphAnalog57761PortOutputMode_Object((1,3,6,1,4,1,5040,1,2,28,3,2,1,1,12),_WtWebGraphAnalog57761PortOutputMode_Type())
wtWebGraphAnalog57761PortOutputMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761PortOutputMode.setStatus(_A)
class _WtWebGraphAnalog57761PortInputMode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_WtWebGraphAnalog57761PortInputMode_Type.__name__=_D
_WtWebGraphAnalog57761PortInputMode_Object=MibTableColumn
wtWebGraphAnalog57761PortInputMode=_WtWebGraphAnalog57761PortInputMode_Object((1,3,6,1,4,1,5040,1,2,28,3,2,1,1,13),_WtWebGraphAnalog57761PortInputMode_Type())
wtWebGraphAnalog57761PortInputMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761PortInputMode.setStatus(_A)
_WtWebGraphAnalog57761PortPresetValue_Type=OctetString
_WtWebGraphAnalog57761PortPresetValue_Object=MibTableColumn
wtWebGraphAnalog57761PortPresetValue=_WtWebGraphAnalog57761PortPresetValue_Object((1,3,6,1,4,1,5040,1,2,28,3,2,1,1,16),_WtWebGraphAnalog57761PortPresetValue_Type())
wtWebGraphAnalog57761PortPresetValue.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761PortPresetValue.setStatus(_A)
_WtWebGraphAnalog57761Manufact_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761Manufact=_WtWebGraphAnalog57761Manufact_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,3,3))
_WtWebGraphAnalog57761MfName_Type=OctetString
_WtWebGraphAnalog57761MfName_Object=MibScalar
wtWebGraphAnalog57761MfName=_WtWebGraphAnalog57761MfName_Object((1,3,6,1,4,1,5040,1,2,28,3,3,1),_WtWebGraphAnalog57761MfName_Type())
wtWebGraphAnalog57761MfName.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MfName.setStatus(_A)
_WtWebGraphAnalog57761MfAddr_Type=OctetString
_WtWebGraphAnalog57761MfAddr_Object=MibScalar
wtWebGraphAnalog57761MfAddr=_WtWebGraphAnalog57761MfAddr_Object((1,3,6,1,4,1,5040,1,2,28,3,3,2),_WtWebGraphAnalog57761MfAddr_Type())
wtWebGraphAnalog57761MfAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MfAddr.setStatus(_A)
_WtWebGraphAnalog57761MfHotline_Type=OctetString
_WtWebGraphAnalog57761MfHotline_Object=MibScalar
wtWebGraphAnalog57761MfHotline=_WtWebGraphAnalog57761MfHotline_Object((1,3,6,1,4,1,5040,1,2,28,3,3,3),_WtWebGraphAnalog57761MfHotline_Type())
wtWebGraphAnalog57761MfHotline.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MfHotline.setStatus(_A)
_WtWebGraphAnalog57761MfInternet_Type=OctetString
_WtWebGraphAnalog57761MfInternet_Object=MibScalar
wtWebGraphAnalog57761MfInternet=_WtWebGraphAnalog57761MfInternet_Object((1,3,6,1,4,1,5040,1,2,28,3,3,4),_WtWebGraphAnalog57761MfInternet_Type())
wtWebGraphAnalog57761MfInternet.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MfInternet.setStatus(_A)
_WtWebGraphAnalog57761MfDeviceTyp_Type=OctetString
_WtWebGraphAnalog57761MfDeviceTyp_Object=MibScalar
wtWebGraphAnalog57761MfDeviceTyp=_WtWebGraphAnalog57761MfDeviceTyp_Object((1,3,6,1,4,1,5040,1,2,28,3,3,5),_WtWebGraphAnalog57761MfDeviceTyp_Type())
wtWebGraphAnalog57761MfDeviceTyp.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MfDeviceTyp.setStatus(_A)
_WtWebGraphAnalog57761MfOrderNo_Type=OctetString
_WtWebGraphAnalog57761MfOrderNo_Object=MibScalar
wtWebGraphAnalog57761MfOrderNo=_WtWebGraphAnalog57761MfOrderNo_Object((1,3,6,1,4,1,5040,1,2,28,3,3,6),_WtWebGraphAnalog57761MfOrderNo_Type())
wtWebGraphAnalog57761MfOrderNo.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761MfOrderNo.setStatus(_A)
_WtWebGraphAnalog57761Diag_ObjectIdentity=ObjectIdentity
wtWebGraphAnalog57761Diag=_WtWebGraphAnalog57761Diag_ObjectIdentity((1,3,6,1,4,1,5040,1,2,28,4))
_WtWebGraphAnalog57761DiagErrorCount_Type=Integer32
_WtWebGraphAnalog57761DiagErrorCount_Object=MibScalar
wtWebGraphAnalog57761DiagErrorCount=_WtWebGraphAnalog57761DiagErrorCount_Object((1,3,6,1,4,1,5040,1,2,28,4,1),_WtWebGraphAnalog57761DiagErrorCount_Type())
wtWebGraphAnalog57761DiagErrorCount.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphAnalog57761DiagErrorCount.setStatus(_A)
_WtWebGraphAnalog57761DiagBinaryError_Type=OctetString
_WtWebGraphAnalog57761DiagBinaryError_Object=MibScalar
wtWebGraphAnalog57761DiagBinaryError=_WtWebGraphAnalog57761DiagBinaryError_Object((1,3,6,1,4,1,5040,1,2,28,4,2),_WtWebGraphAnalog57761DiagBinaryError_Type())
wtWebGraphAnalog57761DiagBinaryError.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphAnalog57761DiagBinaryError.setStatus(_A)
_WtWebGraphAnalog57761DiagErrorIndex_Type=Integer32
_WtWebGraphAnalog57761DiagErrorIndex_Object=MibScalar
wtWebGraphAnalog57761DiagErrorIndex=_WtWebGraphAnalog57761DiagErrorIndex_Object((1,3,6,1,4,1,5040,1,2,28,4,3),_WtWebGraphAnalog57761DiagErrorIndex_Type())
wtWebGraphAnalog57761DiagErrorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wtWebGraphAnalog57761DiagErrorIndex.setStatus(_A)
_WtWebGraphAnalog57761DiagErrorMessage_Type=OctetString
_WtWebGraphAnalog57761DiagErrorMessage_Object=MibScalar
wtWebGraphAnalog57761DiagErrorMessage=_WtWebGraphAnalog57761DiagErrorMessage_Object((1,3,6,1,4,1,5040,1,2,28,4,4),_WtWebGraphAnalog57761DiagErrorMessage_Type())
wtWebGraphAnalog57761DiagErrorMessage.setMaxAccess(_F)
if mibBuilder.loadTexts:wtWebGraphAnalog57761DiagErrorMessage.setStatus(_A)
_WtWebGraphAnalog57761DiagErrorClear_Type=Integer32
_WtWebGraphAnalog57761DiagErrorClear_Object=MibScalar
wtWebGraphAnalog57761DiagErrorClear=_WtWebGraphAnalog57761DiagErrorClear_Object((1,3,6,1,4,1,5040,1,2,28,4,5),_WtWebGraphAnalog57761DiagErrorClear_Type())
wtWebGraphAnalog57761DiagErrorClear.setMaxAccess('write-only')
if mibBuilder.loadTexts:wtWebGraphAnalog57761DiagErrorClear.setStatus(_A)
wtWebGraphAnalog57761Alert1=NotificationType((1,3,6,1,4,1,5040,1,2,28,0,31))
wtWebGraphAnalog57761Alert1.setObjects((_E,_G))
if mibBuilder.loadTexts:wtWebGraphAnalog57761Alert1.setStatus('')
wtWebGraphAnalog57761Alert2=NotificationType((1,3,6,1,4,1,5040,1,2,28,0,32))
wtWebGraphAnalog57761Alert2.setObjects((_E,_G))
if mibBuilder.loadTexts:wtWebGraphAnalog57761Alert2.setStatus('')
wtWebGraphAnalog57761Alert3=NotificationType((1,3,6,1,4,1,5040,1,2,28,0,33))
wtWebGraphAnalog57761Alert3.setObjects((_E,_G))
if mibBuilder.loadTexts:wtWebGraphAnalog57761Alert3.setStatus('')
wtWebGraphAnalog57761Alert4=NotificationType((1,3,6,1,4,1,5040,1,2,28,0,34))
wtWebGraphAnalog57761Alert4.setObjects((_E,_G))
if mibBuilder.loadTexts:wtWebGraphAnalog57761Alert4.setStatus('')
wtWebGraphAnalog57761Alert5=NotificationType((1,3,6,1,4,1,5040,1,2,28,0,35))
wtWebGraphAnalog57761Alert5.setObjects((_E,_G))
if mibBuilder.loadTexts:wtWebGraphAnalog57761Alert5.setStatus('')
wtWebGraphAnalog57761Alert6=NotificationType((1,3,6,1,4,1,5040,1,2,28,0,36))
wtWebGraphAnalog57761Alert6.setObjects((_E,_G))
if mibBuilder.loadTexts:wtWebGraphAnalog57761Alert6.setStatus('')
wtWebGraphAnalog57761Alert7=NotificationType((1,3,6,1,4,1,5040,1,2,28,0,37))
wtWebGraphAnalog57761Alert7.setObjects((_E,_G))
if mibBuilder.loadTexts:wtWebGraphAnalog57761Alert7.setStatus('')
wtWebGraphAnalog57761Alert8=NotificationType((1,3,6,1,4,1,5040,1,2,28,0,38))
wtWebGraphAnalog57761Alert8.setObjects((_E,_G))
if mibBuilder.loadTexts:wtWebGraphAnalog57761Alert8.setStatus('')
wtWebGraphAnalog57761AlertReport=NotificationType((1,3,6,1,4,1,5040,1,2,28,0,39))
wtWebGraphAnalog57761AlertReport.setObjects((_E,_G))
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlertReport.setStatus('')
wtWebGraphAnalog57761Alert9=NotificationType((1,3,6,1,4,1,5040,1,2,28,0,91))
wtWebGraphAnalog57761Alert9.setObjects((_E,_H))
if mibBuilder.loadTexts:wtWebGraphAnalog57761Alert9.setStatus('')
wtWebGraphAnalog57761Alert10=NotificationType((1,3,6,1,4,1,5040,1,2,28,0,92))
wtWebGraphAnalog57761Alert10.setObjects((_E,_H))
if mibBuilder.loadTexts:wtWebGraphAnalog57761Alert10.setStatus('')
wtWebGraphAnalog57761Alert11=NotificationType((1,3,6,1,4,1,5040,1,2,28,0,93))
wtWebGraphAnalog57761Alert11.setObjects((_E,_H))
if mibBuilder.loadTexts:wtWebGraphAnalog57761Alert11.setStatus('')
wtWebGraphAnalog57761Alert12=NotificationType((1,3,6,1,4,1,5040,1,2,28,0,94))
wtWebGraphAnalog57761Alert12.setObjects((_E,_H))
if mibBuilder.loadTexts:wtWebGraphAnalog57761Alert12.setStatus('')
wtWebGraphAnalog57761Alert13=NotificationType((1,3,6,1,4,1,5040,1,2,28,0,95))
wtWebGraphAnalog57761Alert13.setObjects((_E,_H))
if mibBuilder.loadTexts:wtWebGraphAnalog57761Alert13.setStatus('')
wtWebGraphAnalog57761Alert14=NotificationType((1,3,6,1,4,1,5040,1,2,28,0,96))
wtWebGraphAnalog57761Alert14.setObjects((_E,_H))
if mibBuilder.loadTexts:wtWebGraphAnalog57761Alert14.setStatus('')
wtWebGraphAnalog57761Alert15=NotificationType((1,3,6,1,4,1,5040,1,2,28,0,97))
wtWebGraphAnalog57761Alert15.setObjects((_E,_H))
if mibBuilder.loadTexts:wtWebGraphAnalog57761Alert15.setStatus('')
wtWebGraphAnalog57761Alert16=NotificationType((1,3,6,1,4,1,5040,1,2,28,0,98))
wtWebGraphAnalog57761Alert16.setObjects((_E,_H))
if mibBuilder.loadTexts:wtWebGraphAnalog57761Alert16.setStatus('')
wtWebGraphAnalog57761AlertDiag=NotificationType((1,3,6,1,4,1,5040,1,2,28,0,110))
wtWebGraphAnalog57761AlertDiag.setObjects(*((_E,_M),(_E,_N)))
if mibBuilder.loadTexts:wtWebGraphAnalog57761AlertDiag.setStatus('')
mibBuilder.exportSymbols(_E,**{'wut':wut,'wtComServer':wtComServer,'wtWebio':wtWebio,'wtWebGraphAnalog57761':wtWebGraphAnalog57761,'wtWebGraphAnalog57761Alert1':wtWebGraphAnalog57761Alert1,'wtWebGraphAnalog57761Alert2':wtWebGraphAnalog57761Alert2,'wtWebGraphAnalog57761Alert3':wtWebGraphAnalog57761Alert3,'wtWebGraphAnalog57761Alert4':wtWebGraphAnalog57761Alert4,'wtWebGraphAnalog57761Alert5':wtWebGraphAnalog57761Alert5,'wtWebGraphAnalog57761Alert6':wtWebGraphAnalog57761Alert6,'wtWebGraphAnalog57761Alert7':wtWebGraphAnalog57761Alert7,'wtWebGraphAnalog57761Alert8':wtWebGraphAnalog57761Alert8,'wtWebGraphAnalog57761AlertReport':wtWebGraphAnalog57761AlertReport,'wtWebGraphAnalog57761Alert9':wtWebGraphAnalog57761Alert9,'wtWebGraphAnalog57761Alert10':wtWebGraphAnalog57761Alert10,'wtWebGraphAnalog57761Alert11':wtWebGraphAnalog57761Alert11,'wtWebGraphAnalog57761Alert12':wtWebGraphAnalog57761Alert12,'wtWebGraphAnalog57761Alert13':wtWebGraphAnalog57761Alert13,'wtWebGraphAnalog57761Alert14':wtWebGraphAnalog57761Alert14,'wtWebGraphAnalog57761Alert15':wtWebGraphAnalog57761Alert15,'wtWebGraphAnalog57761Alert16':wtWebGraphAnalog57761Alert16,'wtWebGraphAnalog57761AlertDiag':wtWebGraphAnalog57761AlertDiag,'wtWebGraphAnalog57761Inventory':wtWebGraphAnalog57761Inventory,'wtWebGraphAnalog57761Sensors':wtWebGraphAnalog57761Sensors,'wtWebGraphAnalog57761SensorTable':wtWebGraphAnalog57761SensorTable,'wtWebGraphAnalog57761SensorEntry':wtWebGraphAnalog57761SensorEntry,_I:wtWebGraphAnalog57761SensorNo,'wtWebGraphAnalog57761ValuesTable':wtWebGraphAnalog57761ValuesTable,'wtWebGraphAnalog57761ValuesEntry':wtWebGraphAnalog57761ValuesEntry,'wtWebGraphAnalog57761Values':wtWebGraphAnalog57761Values,'wtWebGraphAnalog57761BinaryValuesTable':wtWebGraphAnalog57761BinaryValuesTable,'wtWebGraphAnalog57761BinaryValuesEntry':wtWebGraphAnalog57761BinaryValuesEntry,'wtWebGraphAnalog57761BinaryValues':wtWebGraphAnalog57761BinaryValues,'wtWebGraphAnalog57761ValuesPointTable':wtWebGraphAnalog57761ValuesPointTable,'wtWebGraphAnalog57761ValuesPointEntry':wtWebGraphAnalog57761ValuesPointEntry,'wtWebGraphAnalog57761ValuesPoint':wtWebGraphAnalog57761ValuesPoint,'wtWebGraphAnalog57761SessCntrl':wtWebGraphAnalog57761SessCntrl,'wtWebGraphAnalog57761SessCntrlPassword':wtWebGraphAnalog57761SessCntrlPassword,'wtWebGraphAnalog57761SessCntrlConfigMode':wtWebGraphAnalog57761SessCntrlConfigMode,'wtWebGraphAnalog57761SessCntrlLogout':wtWebGraphAnalog57761SessCntrlLogout,'wtWebGraphAnalog57761SessCntrlAdminPassword':wtWebGraphAnalog57761SessCntrlAdminPassword,'wtWebGraphAnalog57761SessCntrlConfigPassword':wtWebGraphAnalog57761SessCntrlConfigPassword,'wtWebGraphAnalog57761Config':wtWebGraphAnalog57761Config,'wtWebGraphAnalog57761Device':wtWebGraphAnalog57761Device,'wtWebGraphAnalog57761Text':wtWebGraphAnalog57761Text,'wtWebGraphAnalog57761DeviceName':wtWebGraphAnalog57761DeviceName,'wtWebGraphAnalog57761DeviceText':wtWebGraphAnalog57761DeviceText,'wtWebGraphAnalog57761DeviceLocation':wtWebGraphAnalog57761DeviceLocation,'wtWebGraphAnalog57761DeviceContact':wtWebGraphAnalog57761DeviceContact,'wtWebGraphAnalog57761TimeDate':wtWebGraphAnalog57761TimeDate,'wtWebGraphAnalog57761TimeZone':wtWebGraphAnalog57761TimeZone,'wtWebGraphAnalog57761TzOffsetHrs':wtWebGraphAnalog57761TzOffsetHrs,'wtWebGraphAnalog57761TzOffsetMin':wtWebGraphAnalog57761TzOffsetMin,'wtWebGraphAnalog57761TzEnable':wtWebGraphAnalog57761TzEnable,'wtWebGraphAnalog57761StTzOffsetHrs':wtWebGraphAnalog57761StTzOffsetHrs,'wtWebGraphAnalog57761StTzOffsetMin':wtWebGraphAnalog57761StTzOffsetMin,'wtWebGraphAnalog57761StTzEnable':wtWebGraphAnalog57761StTzEnable,'wtWebGraphAnalog57761StTzStartMonth':wtWebGraphAnalog57761StTzStartMonth,'wtWebGraphAnalog57761StTzStartMode':wtWebGraphAnalog57761StTzStartMode,'wtWebGraphAnalog57761StTzStartWday':wtWebGraphAnalog57761StTzStartWday,'wtWebGraphAnalog57761StTzStartHrs':wtWebGraphAnalog57761StTzStartHrs,'wtWebGraphAnalog57761StTzStartMin':wtWebGraphAnalog57761StTzStartMin,'wtWebGraphAnalog57761StTzStopMonth':wtWebGraphAnalog57761StTzStopMonth,'wtWebGraphAnalog57761StTzStopMode':wtWebGraphAnalog57761StTzStopMode,'wtWebGraphAnalog57761StTzStopWday':wtWebGraphAnalog57761StTzStopWday,'wtWebGraphAnalog57761StTzStopHrs':wtWebGraphAnalog57761StTzStopHrs,'wtWebGraphAnalog57761StTzStopMin':wtWebGraphAnalog57761StTzStopMin,'wtWebGraphAnalog57761TimeServer':wtWebGraphAnalog57761TimeServer,'wtWebGraphAnalog57761TimeServer1':wtWebGraphAnalog57761TimeServer1,'wtWebGraphAnalog57761TimeServer2':wtWebGraphAnalog57761TimeServer2,'wtWebGraphAnalog57761TsEnable':wtWebGraphAnalog57761TsEnable,'wtWebGraphAnalog57761TsSyncTime':wtWebGraphAnalog57761TsSyncTime,'wtWebGraphAnalog57761DeviceClock':wtWebGraphAnalog57761DeviceClock,'wtWebGraphAnalog57761ClockHrs':wtWebGraphAnalog57761ClockHrs,'wtWebGraphAnalog57761ClockMin':wtWebGraphAnalog57761ClockMin,'wtWebGraphAnalog57761ClockDay':wtWebGraphAnalog57761ClockDay,'wtWebGraphAnalog57761ClockMonth':wtWebGraphAnalog57761ClockMonth,'wtWebGraphAnalog57761ClockYear':wtWebGraphAnalog57761ClockYear,'wtWebGraphAnalog57761Basic':wtWebGraphAnalog57761Basic,'wtWebGraphAnalog57761Network':wtWebGraphAnalog57761Network,'wtWebGraphAnalog57761IpAddress':wtWebGraphAnalog57761IpAddress,'wtWebGraphAnalog57761SubnetMask':wtWebGraphAnalog57761SubnetMask,'wtWebGraphAnalog57761Gateway':wtWebGraphAnalog57761Gateway,'wtWebGraphAnalog57761DnsServer1':wtWebGraphAnalog57761DnsServer1,'wtWebGraphAnalog57761DnsServer2':wtWebGraphAnalog57761DnsServer2,'wtWebGraphAnalog57761AddConfig':wtWebGraphAnalog57761AddConfig,'wtWebGraphAnalog57761HTTP':wtWebGraphAnalog57761HTTP,'wtWebGraphAnalog57761Startup':wtWebGraphAnalog57761Startup,'wtWebGraphAnalog57761GetHeaderEnable':wtWebGraphAnalog57761GetHeaderEnable,'wtWebGraphAnalog57761HttpPort':wtWebGraphAnalog57761HttpPort,'wtWebGraphAnalog57761Mail':wtWebGraphAnalog57761Mail,'wtWebGraphAnalog57761MailAdName':wtWebGraphAnalog57761MailAdName,'wtWebGraphAnalog57761MailReply':wtWebGraphAnalog57761MailReply,'wtWebGraphAnalog57761MailServer':wtWebGraphAnalog57761MailServer,'wtWebioAn1MailEnable':wtWebioAn1MailEnable,'wtWebGraphAnalog57761MailAuthentication':wtWebGraphAnalog57761MailAuthentication,'wtWebGraphAnalog57761MailAuthUser':wtWebGraphAnalog57761MailAuthUser,'wtWebGraphAnalog57761MailAuthPassword':wtWebGraphAnalog57761MailAuthPassword,'wtWebGraphAnalog57761MailPop3Server':wtWebGraphAnalog57761MailPop3Server,'wtWebGraphAnalog57761SNMP':wtWebGraphAnalog57761SNMP,'wtWebGraphAnalog57761SnmpCommunityStringRead':wtWebGraphAnalog57761SnmpCommunityStringRead,'wtWebGraphAnalog57761SnmpCommunityStringReadWrite':wtWebGraphAnalog57761SnmpCommunityStringReadWrite,'wtWebGraphAnalog57761SystemTrapManagerIP':wtWebGraphAnalog57761SystemTrapManagerIP,'wtWebGraphAnalog57761SystemTrapEnable':wtWebGraphAnalog57761SystemTrapEnable,'wtWebGraphAnalog57761SnmpEnable':wtWebGraphAnalog57761SnmpEnable,'wtWebGraphAnalog57761SnmpCommunityStringTrap':wtWebGraphAnalog57761SnmpCommunityStringTrap,'wtWebGraphAnalog57761SnmpSystemTrapManagerPort':wtWebGraphAnalog57761SnmpSystemTrapManagerPort,'wtWebGraphAnalog57761UDP':wtWebGraphAnalog57761UDP,'wtWebGraphAnalog57761UdpPort':wtWebGraphAnalog57761UdpPort,'wtWebGraphAnalog57761UdpEnable':wtWebGraphAnalog57761UdpEnable,'wtWebGraphAnalog57761Syslog':wtWebGraphAnalog57761Syslog,'wtWebGraphAnalog57761SyslogServerIP':wtWebGraphAnalog57761SyslogServerIP,'wtWebGraphAnalog57761SyslogServerPort':wtWebGraphAnalog57761SyslogServerPort,'wtWebGraphAnalog57761SyslogSystemMessagesEnable':wtWebGraphAnalog57761SyslogSystemMessagesEnable,'wtWebGraphAnalog57761SyslogEnable':wtWebGraphAnalog57761SyslogEnable,'wtWebGraphAnalog57761FTP':wtWebGraphAnalog57761FTP,'wtWebGraphAnalog57761FTPServerIP':wtWebGraphAnalog57761FTPServerIP,'wtWebGraphAnalog57761FTPServerControlPort':wtWebGraphAnalog57761FTPServerControlPort,'wtWebGraphAnalog57761FTPUserName':wtWebGraphAnalog57761FTPUserName,'wtWebGraphAnalog57761FTPPassword':wtWebGraphAnalog57761FTPPassword,'wtWebGraphAnalog57761FTPAccount':wtWebGraphAnalog57761FTPAccount,'wtWebGraphAnalog57761FTPOption':wtWebGraphAnalog57761FTPOption,'wtWebGraphAnalog57761FTPEnable':wtWebGraphAnalog57761FTPEnable,'wtWebGraphAnalog57761Language':wtWebGraphAnalog57761Language,'wtWebGraphAnalog57761LanguageSelect':wtWebGraphAnalog57761LanguageSelect,'wtWebGraphAnalog57761Binary':wtWebGraphAnalog57761Binary,'wtWebGraphAnalog57761BinaryModeCount':wtWebGraphAnalog57761BinaryModeCount,'wtWebGraphAnalog57761BinaryIfTable':wtWebGraphAnalog57761BinaryIfTable,'wtWebGraphAnalog57761BinaryIfEntry':wtWebGraphAnalog57761BinaryIfEntry,_J:wtWebGraphAnalog57761BinaryModeNo,'wtWebGraphAnalog57761BinaryTable':wtWebGraphAnalog57761BinaryTable,'wtWebGraphAnalog57761BinaryEntry':wtWebGraphAnalog57761BinaryEntry,'wtWebGraphAnalog57761BinaryOperationMode':wtWebGraphAnalog57761BinaryOperationMode,'wtWebGraphAnalog57761BinaryTcpServerLocalPort':wtWebGraphAnalog57761BinaryTcpServerLocalPort,'wtWebGraphAnalog57761BinaryTcpServerInputTrigger':wtWebGraphAnalog57761BinaryTcpServerInputTrigger,'wtWebGraphAnalog57761BinaryTcpServerApplicationMode':wtWebGraphAnalog57761BinaryTcpServerApplicationMode,'wtWebGraphAnalog57761BinaryTcpClientLocalPort':wtWebGraphAnalog57761BinaryTcpClientLocalPort,'wtWebGraphAnalog57761BinaryTcpClientServerPort':wtWebGraphAnalog57761BinaryTcpClientServerPort,'wtWebGraphAnalog57761BinaryTcpClientServerIpAddr':wtWebGraphAnalog57761BinaryTcpClientServerIpAddr,'wtWebGraphAnalog57761BinaryTcpClientServerPassword':wtWebGraphAnalog57761BinaryTcpClientServerPassword,'wtWebGraphAnalog57761BinaryTcpClientInactivity':wtWebGraphAnalog57761BinaryTcpClientInactivity,'wtWebGraphAnalog57761BinaryTcpClientInputTrigger':wtWebGraphAnalog57761BinaryTcpClientInputTrigger,'wtWebGraphAnalog57761BinaryTcpClientInterval':wtWebGraphAnalog57761BinaryTcpClientInterval,'wtWebGraphAnalog57761BinaryTcpClientApplicationMode':wtWebGraphAnalog57761BinaryTcpClientApplicationMode,'wtWebGraphAnalog57761BinaryUdpPeerLocalPort':wtWebGraphAnalog57761BinaryUdpPeerLocalPort,'wtWebGraphAnalog57761BinaryUdpPeerRemotePort':wtWebGraphAnalog57761BinaryUdpPeerRemotePort,'wtWebGraphAnalog57761BinaryUdpPeerRemoteIpAddr':wtWebGraphAnalog57761BinaryUdpPeerRemoteIpAddr,'wtWebGraphAnalog57761BinaryUdpPeerInputTrigger':wtWebGraphAnalog57761BinaryUdpPeerInputTrigger,'wtWebGraphAnalog57761BinaryUdpPeerInterval':wtWebGraphAnalog57761BinaryUdpPeerInterval,'wtWebGraphAnalog57761BinaryUdpPeerApplicationMode':wtWebGraphAnalog57761BinaryUdpPeerApplicationMode,'wtWebGraphAnalog57761BinaryConnectedPort':wtWebGraphAnalog57761BinaryConnectedPort,'wtWebGraphAnalog57761BinaryConnectedIpAddr':wtWebGraphAnalog57761BinaryConnectedIpAddr,'wtWebGraphAnalog57761BinaryTcpServerClientHttpPort':wtWebGraphAnalog57761BinaryTcpServerClientHttpPort,'wtWebGraphAnalog57761BinaryTcpClientServerHttpPort':wtWebGraphAnalog57761BinaryTcpClientServerHttpPort,'wtWebGraphAnalog57761BinaryTcpServerHysteresis1':wtWebGraphAnalog57761BinaryTcpServerHysteresis1,'wtWebGraphAnalog57761BinaryTcpServerHysteresis2':wtWebGraphAnalog57761BinaryTcpServerHysteresis2,'wtWebGraphAnalog57761BinaryTcpClientHysteresis1':wtWebGraphAnalog57761BinaryTcpClientHysteresis1,'wtWebGraphAnalog57761BinaryTcpClientHysteresis2':wtWebGraphAnalog57761BinaryTcpClientHysteresis2,'wtWebGraphAnalog57761BinaryUdpPeerHysteresis1':wtWebGraphAnalog57761BinaryUdpPeerHysteresis1,'wtWebGraphAnalog57761BinaryUdpPeerHysteresis2':wtWebGraphAnalog57761BinaryUdpPeerHysteresis2,'wtWebGraphAnalog57761BinaryTcpClientServerUserName':wtWebGraphAnalog57761BinaryTcpClientServerUserName,'wtWebGraphAnalog57761MQTT':wtWebGraphAnalog57761MQTT,'wtWebGraphAnalog57761MQTTEnable':wtWebGraphAnalog57761MQTTEnable,'wtWebGraphAnalog57761MQTTBrockerIP':wtWebGraphAnalog57761MQTTBrockerIP,'wtWebGraphAnalog57761MQTTUserName':wtWebGraphAnalog57761MQTTUserName,'wtWebGraphAnalog57761MQTTPassword':wtWebGraphAnalog57761MQTTPassword,'wtWebGraphAnalog57761MQTTLocalPort':wtWebGraphAnalog57761MQTTLocalPort,'wtWebGraphAnalog57761MQTTBrokerServerPort':wtWebGraphAnalog57761MQTTBrokerServerPort,'wtWebGraphAnalog57761MQTTInterval':wtWebGraphAnalog57761MQTTInterval,'wtWebGraphAnalog57761MQTTLastWillEnable':wtWebGraphAnalog57761MQTTLastWillEnable,'wtWebGraphAnalog57761MQTTLastWillTopic':wtWebGraphAnalog57761MQTTLastWillTopic,'wtWebGraphAnalog57761MQTTLastWillMsg':wtWebGraphAnalog57761MQTTLastWillMsg,'wtWebGraphAnalog57761MQTTLastWillQoS':wtWebGraphAnalog57761MQTTLastWillQoS,'wtWebGraphAnalog57761MQTTLastWillRetain':wtWebGraphAnalog57761MQTTLastWillRetain,'wtWebGraphAnalog57761MQTTLastWillConnectEnable':wtWebGraphAnalog57761MQTTLastWillConnectEnable,'wtWebGraphAnalog57761MQTTLastWillConnectMsg':wtWebGraphAnalog57761MQTTLastWillConnectMsg,'wtWebGraphAnalog57761REST':wtWebGraphAnalog57761REST,'wtWebGraphAnalog57761RESTEnable':wtWebGraphAnalog57761RESTEnable,'wtWebGraphAnalog57761RESTDigestAuthEnable':wtWebGraphAnalog57761RESTDigestAuthEnable,'wtWebGraphAnalog57761Datalogger':wtWebGraphAnalog57761Datalogger,'wtWebGraphAnalog57761LoggerTimebase':wtWebGraphAnalog57761LoggerTimebase,'wtWebGraphAnalog57761LoggerSensorSel':wtWebGraphAnalog57761LoggerSensorSel,'wtWebGraphAnalog57761Alarm':wtWebGraphAnalog57761Alarm,'wtWebGraphAnalog57761AlarmCount':wtWebGraphAnalog57761AlarmCount,'wtWebGraphAnalog57761AlarmIfTable':wtWebGraphAnalog57761AlarmIfTable,'wtWebGraphAnalog57761AlarmIfEntry':wtWebGraphAnalog57761AlarmIfEntry,_K:wtWebGraphAnalog57761AlarmNo,'wtWebGraphAnalog57761AlarmTable':wtWebGraphAnalog57761AlarmTable,'wtWebGraphAnalog57761AlarmEntry':wtWebGraphAnalog57761AlarmEntry,'wtWebGraphAnalog57761AlarmTrigger':wtWebGraphAnalog57761AlarmTrigger,'wtWebGraphAnalog57761AlarmMin1':wtWebGraphAnalog57761AlarmMin1,'wtWebGraphAnalog57761AlarmMax1':wtWebGraphAnalog57761AlarmMax1,'wtWebGraphAnalog57761AlarmHysteresis1':wtWebGraphAnalog57761AlarmHysteresis1,'wtWebGraphAnalog57761AlarmDelay':wtWebGraphAnalog57761AlarmDelay,'wtWebGraphAnalog57761AlarmInterval':wtWebGraphAnalog57761AlarmInterval,'wtWebGraphAnalog57761AlarmEnable':wtWebGraphAnalog57761AlarmEnable,'wtWebGraphAnalog57761AlarmEMailAddr':wtWebGraphAnalog57761AlarmEMailAddr,'wtWebGraphAnalog57761AlarmMailSubject':wtWebGraphAnalog57761AlarmMailSubject,'wtWebGraphAnalog57761AlarmMailText':wtWebGraphAnalog57761AlarmMailText,'wtWebGraphAnalog57761AlarmManagerIP':wtWebGraphAnalog57761AlarmManagerIP,_G:wtWebGraphAnalog57761AlarmTrapText,'wtWebGraphAnalog57761AlarmMailOptions':wtWebGraphAnalog57761AlarmMailOptions,'wtWebGraphAnalog57761AlarmTcpIpAddr':wtWebGraphAnalog57761AlarmTcpIpAddr,'wtWebGraphAnalog57761AlarmTcpPort':wtWebGraphAnalog57761AlarmTcpPort,'wtWebGraphAnalog57761AlarmTcpText':wtWebGraphAnalog57761AlarmTcpText,'wtWebGraphAnalog57761AlarmClearMailSubject':wtWebGraphAnalog57761AlarmClearMailSubject,'wtWebGraphAnalog57761AlarmClearMailText':wtWebGraphAnalog57761AlarmClearMailText,_H:wtWebGraphAnalog57761AlarmClearTrapText,'wtWebGraphAnalog57761AlarmClearTcpText':wtWebGraphAnalog57761AlarmClearTcpText,'wtWebGraphAnalog57761AlarmMin2':wtWebGraphAnalog57761AlarmMin2,'wtWebGraphAnalog57761AlarmMax2':wtWebGraphAnalog57761AlarmMax2,'wtWebGraphAnalog57761AlarmHysteresis2':wtWebGraphAnalog57761AlarmHysteresis2,'wtWebGraphAnalog57761AlarmSyslogIpAddr':wtWebGraphAnalog57761AlarmSyslogIpAddr,'wtWebGraphAnalog57761AlarmSyslogPort':wtWebGraphAnalog57761AlarmSyslogPort,'wtWebGraphAnalog57761AlarmSyslogText':wtWebGraphAnalog57761AlarmSyslogText,'wtWebGraphAnalog57761AlarmSyslogClearText':wtWebGraphAnalog57761AlarmSyslogClearText,'wtWebGraphAnalog57761AlarmFtpDataPort':wtWebGraphAnalog57761AlarmFtpDataPort,'wtWebGraphAnalog57761AlarmFtpFileName':wtWebGraphAnalog57761AlarmFtpFileName,'wtWebGraphAnalog57761AlarmFtpText':wtWebGraphAnalog57761AlarmFtpText,'wtWebGraphAnalog57761AlarmFtpClearText':wtWebGraphAnalog57761AlarmFtpClearText,'wtWebGraphAnalog57761AlarmFtpOption':wtWebGraphAnalog57761AlarmFtpOption,'wtWebGraphAnalog57761AlarmTimerCron':wtWebGraphAnalog57761AlarmTimerCron,'wtWebGraphAnalog57761AlarmName':wtWebGraphAnalog57761AlarmName,'wtWebGraphAnalog57761AlarmActive':wtWebGraphAnalog57761AlarmActive,'wtWebGraphAnalog57761AlarmHttpReqAuthEnable':wtWebGraphAnalog57761AlarmHttpReqAuthEnable,'wtWebGraphAnalog57761AlarmHttpReqAuthUser':wtWebGraphAnalog57761AlarmHttpReqAuthUser,'wtWebGraphAnalog57761AlarmHttpReqAuthPassword':wtWebGraphAnalog57761AlarmHttpReqAuthPassword,'wtWebGraphAnalog57761AlarmHttpReqSetUrl':wtWebGraphAnalog57761AlarmHttpReqSetUrl,'wtWebGraphAnalog57761AlarmHttpReqClearUrl':wtWebGraphAnalog57761AlarmHttpReqClearUrl,'wtWebGraphAnalog57761AlarmHttpReqServerPort':wtWebGraphAnalog57761AlarmHttpReqServerPort,'wtWebGraphAnalog57761AlarmMqttTopicPath':wtWebGraphAnalog57761AlarmMqttTopicPath,'wtWebGraphAnalog57761AlarmMqttTopicSetTopic':wtWebGraphAnalog57761AlarmMqttTopicSetTopic,'wtWebGraphAnalog57761AlarmMqttTopicClear':wtWebGraphAnalog57761AlarmMqttTopicClear,'wtWebGraphAnalog57761AlarmSensorLostSelection':wtWebGraphAnalog57761AlarmSensorLostSelection,'wtWebGraphAnalog57761AlarmLimitWindow':wtWebGraphAnalog57761AlarmLimitWindow,'wtWebGraphAnalog57761AlarmSnmpManagerPort':wtWebGraphAnalog57761AlarmSnmpManagerPort,'wtWebGraphAnalog57761AlarmMqttQoS':wtWebGraphAnalog57761AlarmMqttQoS,'wtWebGraphAnalog57761AlarmMqttRetain':wtWebGraphAnalog57761AlarmMqttRetain,'wtWebGraphAnalog57761Graphics':wtWebGraphAnalog57761Graphics,'wtWebGraphAnalog57761GraphicsBase':wtWebGraphAnalog57761GraphicsBase,'wtWebGraphAnalog57761GraphicsBaseEnable':wtWebGraphAnalog57761GraphicsBaseEnable,'wtWebGraphAnalog57761GraphicsBaseWidth':wtWebGraphAnalog57761GraphicsBaseWidth,'wtWebGraphAnalog57761GraphicsBaseHeight':wtWebGraphAnalog57761GraphicsBaseHeight,'wtWebGraphAnalog57761GraphicsBaseFrameColor':wtWebGraphAnalog57761GraphicsBaseFrameColor,'wtWebGraphAnalog57761GraphicsBaseBackgroundColor':wtWebGraphAnalog57761GraphicsBaseBackgroundColor,'wtWebGraphAnalog57761GraphicsBasePollingrate':wtWebGraphAnalog57761GraphicsBasePollingrate,'wtWebGraphAnalog57761GraphicsSelect':wtWebGraphAnalog57761GraphicsSelect,'wtWebGraphAnalog57761GraphicsSelectDisplaySensorSel':wtWebGraphAnalog57761GraphicsSelectDisplaySensorSel,'wtWebGraphAnalog57761GraphicsSelectDisplayShowExtrem':wtWebGraphAnalog57761GraphicsSelectDisplayShowExtrem,'wtWebGraphAnalog57761SensorColor2Table':wtWebGraphAnalog57761SensorColor2Table,'wtWebGraphAnalog57761SensorColor2Entry':wtWebGraphAnalog57761SensorColor2Entry,'wtWebGraphAnalog57761GraphicsSensorColor':wtWebGraphAnalog57761GraphicsSensorColor,'wtWebGraphAnalog57761GraphicsSelectScale':wtWebGraphAnalog57761GraphicsSelectScale,'wtWebGraphAnalog57761GraphicsScale':wtWebGraphAnalog57761GraphicsScale,'wtWebGraphAnalog57761GraphicsScaleAutoScaleEnable':wtWebGraphAnalog57761GraphicsScaleAutoScaleEnable,'wtWebGraphAnalog57761GraphicsScaleAutoFitEnable':wtWebGraphAnalog57761GraphicsScaleAutoFitEnable,'wtWebGraphAnalog57761GraphicsScale1Min':wtWebGraphAnalog57761GraphicsScale1Min,'wtWebGraphAnalog57761GraphicsScale2Min':wtWebGraphAnalog57761GraphicsScale2Min,'wtWebGraphAnalog57761GraphicsScale1Max':wtWebGraphAnalog57761GraphicsScale1Max,'wtWebGraphAnalog57761GraphicsScale2Max':wtWebGraphAnalog57761GraphicsScale2Max,'wtWebGraphAnalog57761GraphicsScale1Unit':wtWebGraphAnalog57761GraphicsScale1Unit,'wtWebGraphAnalog57761GraphicsScale2Unit':wtWebGraphAnalog57761GraphicsScale2Unit,'wtWebGraphAnalog57761Ports':wtWebGraphAnalog57761Ports,'wtWebGraphAnalog57761PortTable':wtWebGraphAnalog57761PortTable,'wtWebGraphAnalog57761PortEntry':wtWebGraphAnalog57761PortEntry,'wtWebGraphAnalog57761PortName':wtWebGraphAnalog57761PortName,'wtWebGraphAnalog57761PortText':wtWebGraphAnalog57761PortText,'wtWebGraphAnalog57761PortOffset1':wtWebGraphAnalog57761PortOffset1,'wtWebGraphAnalog57761SetPoint1':wtWebGraphAnalog57761SetPoint1,'wtWebGraphAnalog57761PortOffset2':wtWebGraphAnalog57761PortOffset2,'wtWebGraphAnalog57761SetPoint2':wtWebGraphAnalog57761SetPoint2,'wtWebGraphAnalog57761PortComment':wtWebGraphAnalog57761PortComment,'wtWebGraphAnalog57761PortSensorSelect':wtWebGraphAnalog57761PortSensorSelect,'wtWebGraphAnalog57761PortUnit':wtWebGraphAnalog57761PortUnit,'wtWebGraphAnalog57761PortScale0':wtWebGraphAnalog57761PortScale0,'wtWebGraphAnalog57761PortScale100':wtWebGraphAnalog57761PortScale100,'wtWebGraphAnalog57761PortOutputMode':wtWebGraphAnalog57761PortOutputMode,'wtWebGraphAnalog57761PortInputMode':wtWebGraphAnalog57761PortInputMode,'wtWebGraphAnalog57761PortPresetValue':wtWebGraphAnalog57761PortPresetValue,'wtWebGraphAnalog57761Manufact':wtWebGraphAnalog57761Manufact,'wtWebGraphAnalog57761MfName':wtWebGraphAnalog57761MfName,'wtWebGraphAnalog57761MfAddr':wtWebGraphAnalog57761MfAddr,'wtWebGraphAnalog57761MfHotline':wtWebGraphAnalog57761MfHotline,'wtWebGraphAnalog57761MfInternet':wtWebGraphAnalog57761MfInternet,'wtWebGraphAnalog57761MfDeviceTyp':wtWebGraphAnalog57761MfDeviceTyp,'wtWebGraphAnalog57761MfOrderNo':wtWebGraphAnalog57761MfOrderNo,'wtWebGraphAnalog57761Diag':wtWebGraphAnalog57761Diag,'wtWebGraphAnalog57761DiagErrorCount':wtWebGraphAnalog57761DiagErrorCount,'wtWebGraphAnalog57761DiagBinaryError':wtWebGraphAnalog57761DiagBinaryError,_M:wtWebGraphAnalog57761DiagErrorIndex,_N:wtWebGraphAnalog57761DiagErrorMessage,'wtWebGraphAnalog57761DiagErrorClear':wtWebGraphAnalog57761DiagErrorClear})