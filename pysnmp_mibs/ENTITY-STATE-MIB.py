_P='entStateNotificationsGroup'
_O='entStateGroup'
_N='entStateOperDisabled'
_M='entStateOperEnabled'
_L='entStateStandby'
_K='entStateUsage'
_J='entStateOper'
_I='entStateLastChanged'
_H='entPhysicalIndex'
_G='ENTITY-MIB'
_F='entStateAlarm'
_E='entStateAdmin'
_D='read-only'
_C='unknown'
_B='ENTITY-STATE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
entityStateMIB=ModuleIdentity((1,3,6,1,2,1,131))
if mibBuilder.loadTexts:entityStateMIB.setRevisions(('2006-09-06 00:00',))
class EntityAdminState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_C,1),('locked',2),('shuttingDown',3),('unlocked',4)))
class EntityOperState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_C,1),('disabled',2),('enabled',3),('testing',4)))
class EntityUsageState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_C,1),('idle',2),('active',3),('busy',4)))
class EntityAlarmStatus(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_C,0),('underRepair',1),('critical',2),('major',3),('minor',4),('warning',5),('indeterminate',6)))
class EntityStandbyStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_C,1),('hotStandby',2),('coldStandby',3),('providingService',4)))
_EntStateNotifications_ObjectIdentity=ObjectIdentity
entStateNotifications=_EntStateNotifications_ObjectIdentity((1,3,6,1,2,1,131,0))
_EntStateObjects_ObjectIdentity=ObjectIdentity
entStateObjects=_EntStateObjects_ObjectIdentity((1,3,6,1,2,1,131,1))
_EntStateTable_Object=MibTable
entStateTable=_EntStateTable_Object((1,3,6,1,2,1,131,1,1))
if mibBuilder.loadTexts:entStateTable.setStatus(_A)
_EntStateEntry_Object=MibTableRow
entStateEntry=_EntStateEntry_Object((1,3,6,1,2,1,131,1,1,1))
entStateEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:entStateEntry.setStatus(_A)
_EntStateLastChanged_Type=DateAndTime
_EntStateLastChanged_Object=MibTableColumn
entStateLastChanged=_EntStateLastChanged_Object((1,3,6,1,2,1,131,1,1,1,1),_EntStateLastChanged_Type())
entStateLastChanged.setMaxAccess(_D)
if mibBuilder.loadTexts:entStateLastChanged.setStatus(_A)
_EntStateAdmin_Type=EntityAdminState
_EntStateAdmin_Object=MibTableColumn
entStateAdmin=_EntStateAdmin_Object((1,3,6,1,2,1,131,1,1,1,2),_EntStateAdmin_Type())
entStateAdmin.setMaxAccess('read-write')
if mibBuilder.loadTexts:entStateAdmin.setStatus(_A)
_EntStateOper_Type=EntityOperState
_EntStateOper_Object=MibTableColumn
entStateOper=_EntStateOper_Object((1,3,6,1,2,1,131,1,1,1,3),_EntStateOper_Type())
entStateOper.setMaxAccess(_D)
if mibBuilder.loadTexts:entStateOper.setStatus(_A)
_EntStateUsage_Type=EntityUsageState
_EntStateUsage_Object=MibTableColumn
entStateUsage=_EntStateUsage_Object((1,3,6,1,2,1,131,1,1,1,4),_EntStateUsage_Type())
entStateUsage.setMaxAccess(_D)
if mibBuilder.loadTexts:entStateUsage.setStatus(_A)
_EntStateAlarm_Type=EntityAlarmStatus
_EntStateAlarm_Object=MibTableColumn
entStateAlarm=_EntStateAlarm_Object((1,3,6,1,2,1,131,1,1,1,5),_EntStateAlarm_Type())
entStateAlarm.setMaxAccess(_D)
if mibBuilder.loadTexts:entStateAlarm.setStatus(_A)
_EntStateStandby_Type=EntityStandbyStatus
_EntStateStandby_Object=MibTableColumn
entStateStandby=_EntStateStandby_Object((1,3,6,1,2,1,131,1,1,1,6),_EntStateStandby_Type())
entStateStandby.setMaxAccess(_D)
if mibBuilder.loadTexts:entStateStandby.setStatus(_A)
_EntStateConformance_ObjectIdentity=ObjectIdentity
entStateConformance=_EntStateConformance_ObjectIdentity((1,3,6,1,2,1,131,2))
_EntStateCompliances_ObjectIdentity=ObjectIdentity
entStateCompliances=_EntStateCompliances_ObjectIdentity((1,3,6,1,2,1,131,2,1))
_EntStateGroups_ObjectIdentity=ObjectIdentity
entStateGroups=_EntStateGroups_ObjectIdentity((1,3,6,1,2,1,131,2,2))
entStateGroup=ObjectGroup((1,3,6,1,2,1,131,2,2,1))
entStateGroup.setObjects(*((_B,_I),(_B,_E),(_B,_J),(_B,_K),(_B,_F),(_B,_L)))
if mibBuilder.loadTexts:entStateGroup.setStatus(_A)
entStateOperEnabled=NotificationType((1,3,6,1,2,1,131,0,1))
entStateOperEnabled.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:entStateOperEnabled.setStatus(_A)
entStateOperDisabled=NotificationType((1,3,6,1,2,1,131,0,2))
entStateOperDisabled.setObjects(*((_B,_E),(_B,_F)))
if mibBuilder.loadTexts:entStateOperDisabled.setStatus(_A)
entStateNotificationsGroup=NotificationGroup((1,3,6,1,2,1,131,2,2,2))
entStateNotificationsGroup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:entStateNotificationsGroup.setStatus(_A)
entStateCompliance=ModuleCompliance((1,3,6,1,2,1,131,2,1,1))
entStateCompliance.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:entStateCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'EntityAdminState':EntityAdminState,'EntityOperState':EntityOperState,'EntityUsageState':EntityUsageState,'EntityAlarmStatus':EntityAlarmStatus,'EntityStandbyStatus':EntityStandbyStatus,'entityStateMIB':entityStateMIB,'entStateNotifications':entStateNotifications,_M:entStateOperEnabled,_N:entStateOperDisabled,'entStateObjects':entStateObjects,'entStateTable':entStateTable,'entStateEntry':entStateEntry,_I:entStateLastChanged,_E:entStateAdmin,_J:entStateOper,_K:entStateUsage,_F:entStateAlarm,_L:entStateStandby,'entStateConformance':entStateConformance,'entStateCompliances':entStateCompliances,'entStateCompliance':entStateCompliance,'entStateGroups':entStateGroups,_O:entStateGroup,_P:entStateNotificationsGroup})