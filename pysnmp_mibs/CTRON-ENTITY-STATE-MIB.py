_O='ctEntStateNotificationsGroup'
_N='ctEntStateGroup'
_M='ctEntStateOperDisabled'
_L='ctEntStateOperEnabled'
_K='ctEntStateStandby'
_J='ctEntStateUsage'
_I='ctEntStateOper'
_H='ctEntStateLastChanged'
_G='entPhysicalIndex'
_F='ENTITY-MIB'
_E='ctEntStateAlarm'
_D='ctEntStateAdmin'
_C='read-only'
_B='current'
_A='CTRON-ENTITY-STATE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EntityAdminState,EntityAlarmStatus,EntityOperState,EntityStandbyStatus,EntityUsageState=mibBuilder.importSymbols('CTRON-ENTITY-STATE-TC-MIB','EntityAdminState','EntityAlarmStatus','EntityOperState','EntityStandbyStatus','EntityUsageState')
ctEntityStateMib,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctEntityStateMib')
entPhysicalIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
ctEntityStateMIB=ModuleIdentity((1,3,6,1,4,1,52,4,2,31,1))
if mibBuilder.loadTexts:ctEntityStateMIB.setRevisions(('2005-01-23 00:00',))
_CtEntStateNotifications_ObjectIdentity=ObjectIdentity
ctEntStateNotifications=_CtEntStateNotifications_ObjectIdentity((1,3,6,1,4,1,52,4,2,31,1,0))
_CtEntStateObjects_ObjectIdentity=ObjectIdentity
ctEntStateObjects=_CtEntStateObjects_ObjectIdentity((1,3,6,1,4,1,52,4,2,31,1,1))
_CtEntStateTable_Object=MibTable
ctEntStateTable=_CtEntStateTable_Object((1,3,6,1,4,1,52,4,2,31,1,1,1))
if mibBuilder.loadTexts:ctEntStateTable.setStatus(_B)
_CtEntStateEntry_Object=MibTableRow
ctEntStateEntry=_CtEntStateEntry_Object((1,3,6,1,4,1,52,4,2,31,1,1,1,1))
ctEntStateEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:ctEntStateEntry.setStatus(_B)
_CtEntStateLastChanged_Type=DateAndTime
_CtEntStateLastChanged_Object=MibTableColumn
ctEntStateLastChanged=_CtEntStateLastChanged_Object((1,3,6,1,4,1,52,4,2,31,1,1,1,1,1),_CtEntStateLastChanged_Type())
ctEntStateLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:ctEntStateLastChanged.setStatus(_B)
_CtEntStateAdmin_Type=EntityAdminState
_CtEntStateAdmin_Object=MibTableColumn
ctEntStateAdmin=_CtEntStateAdmin_Object((1,3,6,1,4,1,52,4,2,31,1,1,1,1,2),_CtEntStateAdmin_Type())
ctEntStateAdmin.setMaxAccess('read-write')
if mibBuilder.loadTexts:ctEntStateAdmin.setStatus(_B)
_CtEntStateOper_Type=EntityOperState
_CtEntStateOper_Object=MibTableColumn
ctEntStateOper=_CtEntStateOper_Object((1,3,6,1,4,1,52,4,2,31,1,1,1,1,3),_CtEntStateOper_Type())
ctEntStateOper.setMaxAccess(_C)
if mibBuilder.loadTexts:ctEntStateOper.setStatus(_B)
_CtEntStateUsage_Type=EntityUsageState
_CtEntStateUsage_Object=MibTableColumn
ctEntStateUsage=_CtEntStateUsage_Object((1,3,6,1,4,1,52,4,2,31,1,1,1,1,4),_CtEntStateUsage_Type())
ctEntStateUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:ctEntStateUsage.setStatus(_B)
_CtEntStateAlarm_Type=EntityAlarmStatus
_CtEntStateAlarm_Object=MibTableColumn
ctEntStateAlarm=_CtEntStateAlarm_Object((1,3,6,1,4,1,52,4,2,31,1,1,1,1,5),_CtEntStateAlarm_Type())
ctEntStateAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:ctEntStateAlarm.setStatus(_B)
_CtEntStateStandby_Type=EntityStandbyStatus
_CtEntStateStandby_Object=MibTableColumn
ctEntStateStandby=_CtEntStateStandby_Object((1,3,6,1,4,1,52,4,2,31,1,1,1,1,6),_CtEntStateStandby_Type())
ctEntStateStandby.setMaxAccess(_C)
if mibBuilder.loadTexts:ctEntStateStandby.setStatus(_B)
_CtEntStateConformance_ObjectIdentity=ObjectIdentity
ctEntStateConformance=_CtEntStateConformance_ObjectIdentity((1,3,6,1,4,1,52,4,2,31,1,2))
_CtEntStateCompliances_ObjectIdentity=ObjectIdentity
ctEntStateCompliances=_CtEntStateCompliances_ObjectIdentity((1,3,6,1,4,1,52,4,2,31,1,2,1))
_CtEntStateGroups_ObjectIdentity=ObjectIdentity
ctEntStateGroups=_CtEntStateGroups_ObjectIdentity((1,3,6,1,4,1,52,4,2,31,1,2,2))
ctEntStateGroup=ObjectGroup((1,3,6,1,4,1,52,4,2,31,1,2,2,1))
ctEntStateGroup.setObjects(*((_A,_H),(_A,_D),(_A,_I),(_A,_J),(_A,_E),(_A,_K)))
if mibBuilder.loadTexts:ctEntStateGroup.setStatus(_B)
ctEntStateOperEnabled=NotificationType((1,3,6,1,4,1,52,4,2,31,1,0,1))
ctEntStateOperEnabled.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:ctEntStateOperEnabled.setStatus(_B)
ctEntStateOperDisabled=NotificationType((1,3,6,1,4,1,52,4,2,31,1,0,2))
ctEntStateOperDisabled.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:ctEntStateOperDisabled.setStatus(_B)
ctEntStateNotificationsGroup=NotificationGroup((1,3,6,1,4,1,52,4,2,31,1,2,2,2))
ctEntStateNotificationsGroup.setObjects(*((_A,_L),(_A,_M)))
if mibBuilder.loadTexts:ctEntStateNotificationsGroup.setStatus(_B)
ctEntStateCompliance=ModuleCompliance((1,3,6,1,4,1,52,4,2,31,1,2,1,1))
ctEntStateCompliance.setObjects(*((_A,_N),(_A,_O)))
if mibBuilder.loadTexts:ctEntStateCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ctEntityStateMIB':ctEntityStateMIB,'ctEntStateNotifications':ctEntStateNotifications,_L:ctEntStateOperEnabled,_M:ctEntStateOperDisabled,'ctEntStateObjects':ctEntStateObjects,'ctEntStateTable':ctEntStateTable,'ctEntStateEntry':ctEntStateEntry,_H:ctEntStateLastChanged,_D:ctEntStateAdmin,_I:ctEntStateOper,_J:ctEntStateUsage,_E:ctEntStateAlarm,_K:ctEntStateStandby,'ctEntStateConformance':ctEntStateConformance,'ctEntStateCompliances':ctEntStateCompliances,'ctEntStateCompliance':ctEntStateCompliance,'ctEntStateGroups':ctEntStateGroups,_N:ctEntStateGroup,_O:ctEntStateNotificationsGroup})