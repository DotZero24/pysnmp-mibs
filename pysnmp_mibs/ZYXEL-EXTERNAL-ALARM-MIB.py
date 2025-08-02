_C='zyExternalAlarmTrapAlarmId'
_B='ZYXEL-EXTERNAL-ALARM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelExternalAlarm=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,25))
_ZyxelExternalAlarmTrapInfoObjects_ObjectIdentity=ObjectIdentity
zyxelExternalAlarmTrapInfoObjects=_ZyxelExternalAlarmTrapInfoObjects_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,25,1))
_ZyExternalAlarmTrapAlarmId_Type=Integer32
_ZyExternalAlarmTrapAlarmId_Object=MibScalar
zyExternalAlarmTrapAlarmId=_ZyExternalAlarmTrapAlarmId_Object((1,3,6,1,4,1,890,1,15,3,25,1,1),_ZyExternalAlarmTrapAlarmId_Type())
zyExternalAlarmTrapAlarmId.setMaxAccess('read-only')
if mibBuilder.loadTexts:zyExternalAlarmTrapAlarmId.setStatus(_A)
_ZyxelExternalAlarmNotifications_ObjectIdentity=ObjectIdentity
zyxelExternalAlarmNotifications=_ZyxelExternalAlarmNotifications_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,25,2))
zyExternalAlarmDetect=NotificationType((1,3,6,1,4,1,890,1,15,3,25,2,1))
zyExternalAlarmDetect.setObjects((_B,_C))
if mibBuilder.loadTexts:zyExternalAlarmDetect.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zyxelExternalAlarm':zyxelExternalAlarm,'zyxelExternalAlarmTrapInfoObjects':zyxelExternalAlarmTrapInfoObjects,_C:zyExternalAlarmTrapAlarmId,'zyxelExternalAlarmNotifications':zyxelExternalAlarmNotifications,'zyExternalAlarmDetect':zyExternalAlarmDetect})