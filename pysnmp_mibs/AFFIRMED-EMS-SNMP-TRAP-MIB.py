_I='current'
_H='affirmedAlarmSourceId'
_G='affirmedAlarmSeverity'
_F='affirmedAlarmSeqId'
_E='affirmedAlarmRefSeqId'
_D='affirmedAlarmDetails'
_C='affirmedAlarmDateTime'
_B='affirmedAlarmChassisName'
_A='AFFIRMED-ALARM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
affirmedAlarmChassisName,affirmedAlarmDateTime,affirmedAlarmDetails,affirmedAlarmRefSeqId,affirmedAlarmSeqId,affirmedAlarmSeverity,affirmedAlarmSourceId=mibBuilder.importSymbols(_A,_B,_C,_D,_E,_F,_G,_H)
affirmedSnmp,affirmedSnmpNotifications=mibBuilder.importSymbols('AFFIRMED-SNMP-MIB','affirmedSnmp','affirmedSnmpNotifications')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
affirmedSnmpTraps=ModuleIdentity((1,3,6,1,4,1,37963,4,0,5))
_AffirmedSnmpTrapsScalars_ObjectIdentity=ObjectIdentity
affirmedSnmpTrapsScalars=_AffirmedSnmpTrapsScalars_ObjectIdentity((1,3,6,1,4,1,37963,4,0,5,1))
_AffirmedSnmpTrapsTables_ObjectIdentity=ObjectIdentity
affirmedSnmpTrapsTables=_AffirmedSnmpTrapsTables_ObjectIdentity((1,3,6,1,4,1,37963,4,0,5,2))
_AffirmedSnmpTrapsNotifications_ObjectIdentity=ObjectIdentity
affirmedSnmpTrapsNotifications=_AffirmedSnmpTrapsNotifications_ObjectIdentity((1,3,6,1,4,1,37963,4,0,5,3))
_AffirmedSnmpTrapsNotificationPrefix_ObjectIdentity=ObjectIdentity
affirmedSnmpTrapsNotificationPrefix=_AffirmedSnmpTrapsNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,37963,4,0,5,3,0))
_AffirmedSnmpTrapsNotificationObjects_ObjectIdentity=ObjectIdentity
affirmedSnmpTrapsNotificationObjects=_AffirmedSnmpTrapsNotificationObjects_ObjectIdentity((1,3,6,1,4,1,37963,4,0,5,3,1))
emsDBReplicationDown=NotificationType((1,3,6,1,4,1,37963,4,0,5,3,0,1))
emsDBReplicationDown.setObjects(*((_A,_F),(_A,_C),(_A,_B),(_A,_H),(_A,_G),(_A,_E),(_A,_D)))
if mibBuilder.loadTexts:emsDBReplicationDown.setStatus(_I)
emsDBReplicationLagBehind=NotificationType((1,3,6,1,4,1,37963,4,0,5,3,0,2))
emsDBReplicationLagBehind.setObjects(*((_A,_F),(_A,_C),(_A,_B),(_A,_H),(_A,_G),(_A,_E),(_A,_D)))
if mibBuilder.loadTexts:emsDBReplicationLagBehind.setStatus(_I)
mibBuilder.exportSymbols('AFFIRMED-EMS-SNMP-TRAP-MIB',**{'affirmedSnmpTraps':affirmedSnmpTraps,'affirmedSnmpTrapsScalars':affirmedSnmpTrapsScalars,'affirmedSnmpTrapsTables':affirmedSnmpTrapsTables,'affirmedSnmpTrapsNotifications':affirmedSnmpTrapsNotifications,'affirmedSnmpTrapsNotificationPrefix':affirmedSnmpTrapsNotificationPrefix,'emsDBReplicationDown':emsDBReplicationDown,'emsDBReplicationLagBehind':emsDBReplicationLagBehind,'affirmedSnmpTrapsNotificationObjects':affirmedSnmpTrapsNotificationObjects})