_K='degrees Centigrade'
_J='NotificationType'
_I='percentage'
_H='normalOpen'
_G='normalClose'
_F='read-write'
_E='off'
_D='on'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier',_J,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_J,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Delta_ObjectIdentity=ObjectIdentity
delta=_Delta_ObjectIdentity((1,3,6,1,4,1,2254))
_Ups_ObjectIdentity=ObjectIdentity
ups=_Ups_ObjectIdentity((1,3,6,1,4,1,2254,2))
_Sensor_ObjectIdentity=ObjectIdentity
sensor=_Sensor_ObjectIdentity((1,3,6,1,4,1,2254,2,500))
_DsensorMonitor_ObjectIdentity=ObjectIdentity
dsensorMonitor=_DsensorMonitor_ObjectIdentity((1,3,6,1,4,1,2254,2,500,1))
_DsensorTemperature_Type=Integer32
_DsensorTemperature_Object=MibScalar
dsensorTemperature=_DsensorTemperature_Object((1,3,6,1,4,1,2254,2,500,1,1),_DsensorTemperature_Type())
dsensorTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:dsensorTemperature.setStatus(_A)
if mibBuilder.loadTexts:dsensorTemperature.setUnits(_K)
_DsensorHumidity_Type=Integer32
_DsensorHumidity_Object=MibScalar
dsensorHumidity=_DsensorHumidity_Object((1,3,6,1,4,1,2254,2,500,1,2),_DsensorHumidity_Type())
dsensorHumidity.setMaxAccess(_C)
if mibBuilder.loadTexts:dsensorHumidity.setStatus(_A)
if mibBuilder.loadTexts:dsensorHumidity.setUnits(_I)
class _DsensorWarnOverTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DsensorWarnOverTemperature_Type.__name__=_B
_DsensorWarnOverTemperature_Object=MibScalar
dsensorWarnOverTemperature=_DsensorWarnOverTemperature_Object((1,3,6,1,4,1,2254,2,500,1,3),_DsensorWarnOverTemperature_Type())
dsensorWarnOverTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:dsensorWarnOverTemperature.setStatus(_A)
class _DsensorWarnOverHumidity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DsensorWarnOverHumidity_Type.__name__=_B
_DsensorWarnOverHumidity_Object=MibScalar
dsensorWarnOverHumidity=_DsensorWarnOverHumidity_Object((1,3,6,1,4,1,2254,2,500,1,4),_DsensorWarnOverHumidity_Type())
dsensorWarnOverHumidity.setMaxAccess(_C)
if mibBuilder.loadTexts:dsensorWarnOverHumidity.setStatus(_A)
class _DsensorAlarmOverTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DsensorAlarmOverTemperature_Type.__name__=_B
_DsensorAlarmOverTemperature_Object=MibScalar
dsensorAlarmOverTemperature=_DsensorAlarmOverTemperature_Object((1,3,6,1,4,1,2254,2,500,1,5),_DsensorAlarmOverTemperature_Type())
dsensorAlarmOverTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:dsensorAlarmOverTemperature.setStatus(_A)
class _DsensorAlarmOverHumidity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DsensorAlarmOverHumidity_Type.__name__=_B
_DsensorAlarmOverHumidity_Object=MibScalar
dsensorAlarmOverHumidity=_DsensorAlarmOverHumidity_Object((1,3,6,1,4,1,2254,2,500,1,6),_DsensorAlarmOverHumidity_Type())
dsensorAlarmOverHumidity.setMaxAccess(_C)
if mibBuilder.loadTexts:dsensorAlarmOverHumidity.setStatus(_A)
class _DsensorAlarmRelay1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DsensorAlarmRelay1_Type.__name__=_B
_DsensorAlarmRelay1_Object=MibScalar
dsensorAlarmRelay1=_DsensorAlarmRelay1_Object((1,3,6,1,4,1,2254,2,500,1,7),_DsensorAlarmRelay1_Type())
dsensorAlarmRelay1.setMaxAccess(_C)
if mibBuilder.loadTexts:dsensorAlarmRelay1.setStatus(_A)
class _DsensorAlarmRelay2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DsensorAlarmRelay2_Type.__name__=_B
_DsensorAlarmRelay2_Object=MibScalar
dsensorAlarmRelay2=_DsensorAlarmRelay2_Object((1,3,6,1,4,1,2254,2,500,1,8),_DsensorAlarmRelay2_Type())
dsensorAlarmRelay2.setMaxAccess(_C)
if mibBuilder.loadTexts:dsensorAlarmRelay2.setStatus(_A)
class _DsensorAlarmRelay3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DsensorAlarmRelay3_Type.__name__=_B
_DsensorAlarmRelay3_Object=MibScalar
dsensorAlarmRelay3=_DsensorAlarmRelay3_Object((1,3,6,1,4,1,2254,2,500,1,9),_DsensorAlarmRelay3_Type())
dsensorAlarmRelay3.setMaxAccess(_C)
if mibBuilder.loadTexts:dsensorAlarmRelay3.setStatus(_A)
class _DsensorAlarmRelay4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_D,1),(_E,2)))
_DsensorAlarmRelay4_Type.__name__=_B
_DsensorAlarmRelay4_Object=MibScalar
dsensorAlarmRelay4=_DsensorAlarmRelay4_Object((1,3,6,1,4,1,2254,2,500,1,10),_DsensorAlarmRelay4_Type())
dsensorAlarmRelay4.setMaxAccess(_C)
if mibBuilder.loadTexts:dsensorAlarmRelay4.setStatus(_A)
_DsensorConfigure_ObjectIdentity=ObjectIdentity
dsensorConfigure=_DsensorConfigure_ObjectIdentity((1,3,6,1,4,1,2254,2,500,2))
_DsensorSetTemperatureWarnLimit_Type=Integer32
_DsensorSetTemperatureWarnLimit_Object=MibScalar
dsensorSetTemperatureWarnLimit=_DsensorSetTemperatureWarnLimit_Object((1,3,6,1,4,1,2254,2,500,2,1),_DsensorSetTemperatureWarnLimit_Type())
dsensorSetTemperatureWarnLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:dsensorSetTemperatureWarnLimit.setStatus(_A)
if mibBuilder.loadTexts:dsensorSetTemperatureWarnLimit.setUnits('Degrees Centigrade')
_DsensorSetHumidityWarnLimit_Type=Integer32
_DsensorSetHumidityWarnLimit_Object=MibScalar
dsensorSetHumidityWarnLimit=_DsensorSetHumidityWarnLimit_Object((1,3,6,1,4,1,2254,2,500,2,2),_DsensorSetHumidityWarnLimit_Type())
dsensorSetHumidityWarnLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:dsensorSetHumidityWarnLimit.setStatus(_A)
if mibBuilder.loadTexts:dsensorSetHumidityWarnLimit.setUnits(_I)
_DsensorSetTemperatureAlarmLimit_Type=Integer32
_DsensorSetTemperatureAlarmLimit_Object=MibScalar
dsensorSetTemperatureAlarmLimit=_DsensorSetTemperatureAlarmLimit_Object((1,3,6,1,4,1,2254,2,500,2,3),_DsensorSetTemperatureAlarmLimit_Type())
dsensorSetTemperatureAlarmLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:dsensorSetTemperatureAlarmLimit.setStatus(_A)
if mibBuilder.loadTexts:dsensorSetTemperatureAlarmLimit.setUnits(_K)
_DsensorSetHumidityAlarmLimit_Type=Integer32
_DsensorSetHumidityAlarmLimit_Object=MibScalar
dsensorSetHumidityAlarmLimit=_DsensorSetHumidityAlarmLimit_Object((1,3,6,1,4,1,2254,2,500,2,4),_DsensorSetHumidityAlarmLimit_Type())
dsensorSetHumidityAlarmLimit.setMaxAccess(_F)
if mibBuilder.loadTexts:dsensorSetHumidityAlarmLimit.setStatus(_A)
if mibBuilder.loadTexts:dsensorSetHumidityAlarmLimit.setUnits(_I)
class _DsensorSetRelay1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DsensorSetRelay1_Type.__name__=_B
_DsensorSetRelay1_Object=MibScalar
dsensorSetRelay1=_DsensorSetRelay1_Object((1,3,6,1,4,1,2254,2,500,2,5),_DsensorSetRelay1_Type())
dsensorSetRelay1.setMaxAccess(_F)
if mibBuilder.loadTexts:dsensorSetRelay1.setStatus(_A)
class _DsensorSetRelay2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DsensorSetRelay2_Type.__name__=_B
_DsensorSetRelay2_Object=MibScalar
dsensorSetRelay2=_DsensorSetRelay2_Object((1,3,6,1,4,1,2254,2,500,2,6),_DsensorSetRelay2_Type())
dsensorSetRelay2.setMaxAccess(_F)
if mibBuilder.loadTexts:dsensorSetRelay2.setStatus(_A)
class _DsensorSetRelay3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DsensorSetRelay3_Type.__name__=_B
_DsensorSetRelay3_Object=MibScalar
dsensorSetRelay3=_DsensorSetRelay3_Object((1,3,6,1,4,1,2254,2,500,2,7),_DsensorSetRelay3_Type())
dsensorSetRelay3.setMaxAccess(_F)
if mibBuilder.loadTexts:dsensorSetRelay3.setStatus(_A)
class _DsensorSetRelay4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_DsensorSetRelay4_Type.__name__=_B
_DsensorSetRelay4_Object=MibScalar
dsensorSetRelay4=_DsensorSetRelay4_Object((1,3,6,1,4,1,2254,2,500,2,8),_DsensorSetRelay4_Type())
dsensorSetRelay4.setMaxAccess(_F)
if mibBuilder.loadTexts:dsensorSetRelay4.setStatus(_A)
_DsensorTraps_ObjectIdentity=ObjectIdentity
dsensorTraps=_DsensorTraps_ObjectIdentity((1,3,6,1,4,1,2254,2,500,20))
dsensorCommunicationLost=NotificationType((1,3,6,1,4,1,2254,2,500,20,0,1))
if mibBuilder.loadTexts:dsensorCommunicationLost.setStatus('')
dsensorCommunicationEstablished=NotificationType((1,3,6,1,4,1,2254,2,500,20,0,2))
if mibBuilder.loadTexts:dsensorCommunicationEstablished.setStatus('')
dsensorOverWarningTemperature=NotificationType((1,3,6,1,4,1,2254,2,500,20,0,3))
if mibBuilder.loadTexts:dsensorOverWarningTemperature.setStatus('')
dsensorNoLongerOverWarningTemperature=NotificationType((1,3,6,1,4,1,2254,2,500,20,0,4))
if mibBuilder.loadTexts:dsensorNoLongerOverWarningTemperature.setStatus('')
dsensorOverAlarmTemperature=NotificationType((1,3,6,1,4,1,2254,2,500,20,0,5))
if mibBuilder.loadTexts:dsensorOverAlarmTemperature.setStatus('')
dsensorNoLongerOverAlarmTemperature=NotificationType((1,3,6,1,4,1,2254,2,500,20,0,6))
if mibBuilder.loadTexts:dsensorNoLongerOverAlarmTemperature.setStatus('')
dsensorOverWarningHumidity=NotificationType((1,3,6,1,4,1,2254,2,500,20,0,7))
if mibBuilder.loadTexts:dsensorOverWarningHumidity.setStatus('')
dsensorNoLongerOverWarningHumidity=NotificationType((1,3,6,1,4,1,2254,2,500,20,0,8))
if mibBuilder.loadTexts:dsensorNoLongerOverWarningHumidity.setStatus('')
dsensorOverAlarmHumidity=NotificationType((1,3,6,1,4,1,2254,2,500,20,0,9))
if mibBuilder.loadTexts:dsensorOverAlarmHumidity.setStatus('')
dsensorNoLongerOverAlarmHumidity=NotificationType((1,3,6,1,4,1,2254,2,500,20,0,10))
if mibBuilder.loadTexts:dsensorNoLongerOverAlarmHumidity.setStatus('')
dsensorRelay1Alarm=NotificationType((1,3,6,1,4,1,2254,2,500,20,0,11))
if mibBuilder.loadTexts:dsensorRelay1Alarm.setStatus('')
dsensorRelay1Normal=NotificationType((1,3,6,1,4,1,2254,2,500,20,0,12))
if mibBuilder.loadTexts:dsensorRelay1Normal.setStatus('')
dsensorRelay2Alarm=NotificationType((1,3,6,1,4,1,2254,2,500,20,0,13))
if mibBuilder.loadTexts:dsensorRelay2Alarm.setStatus('')
dsensorRelay2Normal=NotificationType((1,3,6,1,4,1,2254,2,500,20,0,14))
if mibBuilder.loadTexts:dsensorRelay2Normal.setStatus('')
dsensorRelay3Alarm=NotificationType((1,3,6,1,4,1,2254,2,500,20,0,15))
if mibBuilder.loadTexts:dsensorRelay3Alarm.setStatus('')
dsensorRelay3Normal=NotificationType((1,3,6,1,4,1,2254,2,500,20,0,16))
if mibBuilder.loadTexts:dsensorRelay3Normal.setStatus('')
dsensorRelay4Alarm=NotificationType((1,3,6,1,4,1,2254,2,500,20,0,17))
if mibBuilder.loadTexts:dsensorRelay4Alarm.setStatus('')
dsensorRelay4Normal=NotificationType((1,3,6,1,4,1,2254,2,500,20,0,18))
if mibBuilder.loadTexts:dsensorRelay4Normal.setStatus('')
mibBuilder.exportSymbols('DeltaSensor-MIB',**{'delta':delta,'ups':ups,'sensor':sensor,'dsensorMonitor':dsensorMonitor,'dsensorTemperature':dsensorTemperature,'dsensorHumidity':dsensorHumidity,'dsensorWarnOverTemperature':dsensorWarnOverTemperature,'dsensorWarnOverHumidity':dsensorWarnOverHumidity,'dsensorAlarmOverTemperature':dsensorAlarmOverTemperature,'dsensorAlarmOverHumidity':dsensorAlarmOverHumidity,'dsensorAlarmRelay1':dsensorAlarmRelay1,'dsensorAlarmRelay2':dsensorAlarmRelay2,'dsensorAlarmRelay3':dsensorAlarmRelay3,'dsensorAlarmRelay4':dsensorAlarmRelay4,'dsensorConfigure':dsensorConfigure,'dsensorSetTemperatureWarnLimit':dsensorSetTemperatureWarnLimit,'dsensorSetHumidityWarnLimit':dsensorSetHumidityWarnLimit,'dsensorSetTemperatureAlarmLimit':dsensorSetTemperatureAlarmLimit,'dsensorSetHumidityAlarmLimit':dsensorSetHumidityAlarmLimit,'dsensorSetRelay1':dsensorSetRelay1,'dsensorSetRelay2':dsensorSetRelay2,'dsensorSetRelay3':dsensorSetRelay3,'dsensorSetRelay4':dsensorSetRelay4,'dsensorTraps':dsensorTraps,'dsensorCommunicationLost':dsensorCommunicationLost,'dsensorCommunicationEstablished':dsensorCommunicationEstablished,'dsensorOverWarningTemperature':dsensorOverWarningTemperature,'dsensorNoLongerOverWarningTemperature':dsensorNoLongerOverWarningTemperature,'dsensorOverAlarmTemperature':dsensorOverAlarmTemperature,'dsensorNoLongerOverAlarmTemperature':dsensorNoLongerOverAlarmTemperature,'dsensorOverWarningHumidity':dsensorOverWarningHumidity,'dsensorNoLongerOverWarningHumidity':dsensorNoLongerOverWarningHumidity,'dsensorOverAlarmHumidity':dsensorOverAlarmHumidity,'dsensorNoLongerOverAlarmHumidity':dsensorNoLongerOverAlarmHumidity,'dsensorRelay1Alarm':dsensorRelay1Alarm,'dsensorRelay1Normal':dsensorRelay1Normal,'dsensorRelay2Alarm':dsensorRelay2Alarm,'dsensorRelay2Normal':dsensorRelay2Normal,'dsensorRelay3Alarm':dsensorRelay3Alarm,'dsensorRelay3Normal':dsensorRelay3Normal,'dsensorRelay4Alarm':dsensorRelay4Alarm,'dsensorRelay4Normal':dsensorRelay4Normal})