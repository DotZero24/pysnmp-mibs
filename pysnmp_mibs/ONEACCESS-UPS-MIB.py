_E='Integer32'
_D='oacUpsAlarmDescr'
_C='ONEACCESS-UPS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
oacExpIMManagement,=mibBuilder.importSymbols('ONEACCESS-GLOBAL-REG','oacExpIMManagement')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
AutonomousType,DisplayString,PhysAddress,TextualConvention,TestAndIncr,TimeInterval,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','TextualConvention','TestAndIncr','TimeInterval','TimeStamp')
oacUpsMIB=ModuleIdentity((1,3,6,1,4,1,13191,10,3,4,1225))
_OacUpsMIBObjects_ObjectIdentity=ObjectIdentity
oacUpsMIBObjects=_OacUpsMIBObjects_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,1225,1))
_OacUpsBattery_ObjectIdentity=ObjectIdentity
oacUpsBattery=_OacUpsBattery_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,1225,1,1))
class _OacUpsBatteryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('batteryNormal',2),('batteryLow',3),('batteryDepleted',4)))
_OacUpsBatteryStatus_Type.__name__=_E
_OacUpsBatteryStatus_Object=MibScalar
oacUpsBatteryStatus=_OacUpsBatteryStatus_Object((1,3,6,1,4,1,13191,10,3,4,1225,1,1,1),_OacUpsBatteryStatus_Type())
oacUpsBatteryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:oacUpsBatteryStatus.setStatus(_A)
_OacUpsAlarm_ObjectIdentity=ObjectIdentity
oacUpsAlarm=_OacUpsAlarm_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,1225,1,2))
_OacUpsAlarmsPresent_Type=Gauge32
_OacUpsAlarmsPresent_Object=MibScalar
oacUpsAlarmsPresent=_OacUpsAlarmsPresent_Object((1,3,6,1,4,1,13191,10,3,4,1225,1,2,1),_OacUpsAlarmsPresent_Type())
oacUpsAlarmsPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:oacUpsAlarmsPresent.setStatus(_A)
_OacUpsAlarmDescr_Type=AutonomousType
_OacUpsAlarmDescr_Object=MibScalar
oacUpsAlarmDescr=_OacUpsAlarmDescr_Object((1,3,6,1,4,1,13191,10,3,4,1225,1,2,2),_OacUpsAlarmDescr_Type())
oacUpsAlarmDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:oacUpsAlarmDescr.setStatus(_A)
_OacUpsAlarmTime_Type=TimeStamp
_OacUpsAlarmTime_Object=MibScalar
oacUpsAlarmTime=_OacUpsAlarmTime_Object((1,3,6,1,4,1,13191,10,3,4,1225,1,2,3),_OacUpsAlarmTime_Type())
oacUpsAlarmTime.setMaxAccess(_B)
if mibBuilder.loadTexts:oacUpsAlarmTime.setStatus(_A)
_OacUpsTraps_ObjectIdentity=ObjectIdentity
oacUpsTraps=_OacUpsTraps_ObjectIdentity((1,3,6,1,4,1,13191,10,3,4,1225,2))
oacUpsTrapAlarmEntryAdded=NotificationType((1,3,6,1,4,1,13191,10,3,4,1225,2,0))
oacUpsTrapAlarmEntryAdded.setObjects((_C,_D))
if mibBuilder.loadTexts:oacUpsTrapAlarmEntryAdded.setStatus(_A)
oacUpsTrapAlarmEntryRemoved=NotificationType((1,3,6,1,4,1,13191,10,3,4,1225,2,1))
oacUpsTrapAlarmEntryRemoved.setObjects((_C,_D))
if mibBuilder.loadTexts:oacUpsTrapAlarmEntryRemoved.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'oacUpsMIB':oacUpsMIB,'oacUpsMIBObjects':oacUpsMIBObjects,'oacUpsBattery':oacUpsBattery,'oacUpsBatteryStatus':oacUpsBatteryStatus,'oacUpsAlarm':oacUpsAlarm,'oacUpsAlarmsPresent':oacUpsAlarmsPresent,_D:oacUpsAlarmDescr,'oacUpsAlarmTime':oacUpsAlarmTime,'oacUpsTraps':oacUpsTraps,'oacUpsTrapAlarmEntryAdded':oacUpsTrapAlarmEntryAdded,'oacUpsTrapAlarmEntryRemoved':oacUpsTrapAlarmEntryRemoved})