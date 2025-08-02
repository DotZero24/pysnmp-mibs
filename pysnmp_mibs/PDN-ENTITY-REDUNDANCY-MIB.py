_a='pdnRedundancyGeneralGroup'
_Z='pdnRedunEventHwMissingHwFailure'
_Y='pdnRedunEventHwFailure'
_X='pdnRedunEventLinkDefect'
_W='pdnRedunEventCfgIncompatible'
_V='pdnRedunEventFwIncompatible'
_U='pdnRedunEventStandbyAlarmOrReset'
_T='pdnRedunEventHwIncompatible'
_S='pdnRedunEventNoActiveModule'
_R='pdnRedunEntityState'
_Q='pdnRedunNotificationEnable'
_P='pdnRedunCommand'
_O='pdnRedunGeneralNotificationEnable'
_N='pdnYCableSelection'
_M='pdnEntityRedundancySelection'
_L='disabled'
_K='enabled'
_J='noAlarm'
_I='read-only'
_H='Integer32'
_G='entPhysicalIndex'
_F='ENTITY-MIB'
_E='pdnRedunGeneralAlarmStatus'
_D='read-write'
_C='pdnRedunAlarmStatus'
_B='PDN-ENTITY-REDUNDANCY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_F,_G)
pdnEntityRedundancy,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdnEntityRedundancy')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pdnEntRedunMIB=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,41,1))
if mibBuilder.loadTexts:pdnEntRedunMIB.setRevisions(('2003-07-25 13:00','2003-05-22 10:00','2003-05-04 17:00','2003-03-03 15:00'))
class PdnRedunStates(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('activeState',1),('activeAlarmState',2),('standbyState',3),('standbyAlarmState',4)))
class PdnRedunCmd(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noCmd',1),('switch',2),('forcedswitch',3)))
class PdnRedunAlarmStatus(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_J,0),('linkDefect',1),('hwFailure',2),('hwMissing',3),('hwIncompatible',4),('fwIncompatible',5),('cfgIncompatible',6)))
class PdnRedunGeneralAlarmStatus(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_J,0),('noActiveModule',1),('standbyAlarmOrReset',2)))
_PdnEntityRedundancyMIBObjects_ObjectIdentity=ObjectIdentity
pdnEntityRedundancyMIBObjects=_PdnEntityRedundancyMIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,41,1,1))
class _PdnEntityRedundancySelection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_PdnEntityRedundancySelection_Type.__name__=_H
_PdnEntityRedundancySelection_Object=MibScalar
pdnEntityRedundancySelection=_PdnEntityRedundancySelection_Object((1,3,6,1,4,1,1795,2,24,2,41,1,1,1),_PdnEntityRedundancySelection_Type())
pdnEntityRedundancySelection.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnEntityRedundancySelection.setStatus(_A)
class _PdnYCableSelection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_PdnYCableSelection_Type.__name__=_H
_PdnYCableSelection_Object=MibScalar
pdnYCableSelection=_PdnYCableSelection_Object((1,3,6,1,4,1,1795,2,24,2,41,1,1,2),_PdnYCableSelection_Type())
pdnYCableSelection.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnYCableSelection.setStatus(_A)
_PdnRedunGeneralAlarmStatus_Type=PdnRedunGeneralAlarmStatus
_PdnRedunGeneralAlarmStatus_Object=MibScalar
pdnRedunGeneralAlarmStatus=_PdnRedunGeneralAlarmStatus_Object((1,3,6,1,4,1,1795,2,24,2,41,1,1,3),_PdnRedunGeneralAlarmStatus_Type())
pdnRedunGeneralAlarmStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:pdnRedunGeneralAlarmStatus.setStatus(_A)
_PdnRedunCmdTable_Object=MibTable
pdnRedunCmdTable=_PdnRedunCmdTable_Object((1,3,6,1,4,1,1795,2,24,2,41,1,1,4))
if mibBuilder.loadTexts:pdnRedunCmdTable.setStatus(_A)
_PdnRedunCmdEntry_Object=MibTableRow
pdnRedunCmdEntry=_PdnRedunCmdEntry_Object((1,3,6,1,4,1,1795,2,24,2,41,1,1,4,1))
pdnRedunCmdEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:pdnRedunCmdEntry.setStatus(_A)
_PdnRedunCommand_Type=PdnRedunCmd
_PdnRedunCommand_Object=MibTableColumn
pdnRedunCommand=_PdnRedunCommand_Object((1,3,6,1,4,1,1795,2,24,2,41,1,1,4,1,1),_PdnRedunCommand_Type())
pdnRedunCommand.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnRedunCommand.setStatus(_A)
_PdnRedunStatusTable_Object=MibTable
pdnRedunStatusTable=_PdnRedunStatusTable_Object((1,3,6,1,4,1,1795,2,24,2,41,1,1,5))
if mibBuilder.loadTexts:pdnRedunStatusTable.setStatus(_A)
_PdnRedunStatusEntry_Object=MibTableRow
pdnRedunStatusEntry=_PdnRedunStatusEntry_Object((1,3,6,1,4,1,1795,2,24,2,41,1,1,5,1))
pdnRedunStatusEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:pdnRedunStatusEntry.setStatus(_A)
_PdnRedunEntityState_Type=PdnRedunStates
_PdnRedunEntityState_Object=MibTableColumn
pdnRedunEntityState=_PdnRedunEntityState_Object((1,3,6,1,4,1,1795,2,24,2,41,1,1,5,1,1),_PdnRedunEntityState_Type())
pdnRedunEntityState.setMaxAccess(_I)
if mibBuilder.loadTexts:pdnRedunEntityState.setStatus(_A)
_PdnRedunAlarmStatus_Type=PdnRedunAlarmStatus
_PdnRedunAlarmStatus_Object=MibTableColumn
pdnRedunAlarmStatus=_PdnRedunAlarmStatus_Object((1,3,6,1,4,1,1795,2,24,2,41,1,1,5,1,2),_PdnRedunAlarmStatus_Type())
pdnRedunAlarmStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:pdnRedunAlarmStatus.setStatus(_A)
_PdnRedunNotificationEnable_Type=PdnRedunAlarmStatus
_PdnRedunNotificationEnable_Object=MibTableColumn
pdnRedunNotificationEnable=_PdnRedunNotificationEnable_Object((1,3,6,1,4,1,1795,2,24,2,41,1,1,5,1,3),_PdnRedunNotificationEnable_Type())
pdnRedunNotificationEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnRedunNotificationEnable.setStatus(_A)
_PdnRedunGeneralNotificationEnable_Type=PdnRedunGeneralAlarmStatus
_PdnRedunGeneralNotificationEnable_Object=MibScalar
pdnRedunGeneralNotificationEnable=_PdnRedunGeneralNotificationEnable_Object((1,3,6,1,4,1,1795,2,24,2,41,1,1,6),_PdnRedunGeneralNotificationEnable_Type())
pdnRedunGeneralNotificationEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnRedunGeneralNotificationEnable.setStatus(_A)
_PdnEntityRedundancyNotifications_ObjectIdentity=ObjectIdentity
pdnEntityRedundancyNotifications=_PdnEntityRedundancyNotifications_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,41,1,2))
_PdnRedunNotificationsPrefix_ObjectIdentity=ObjectIdentity
pdnRedunNotificationsPrefix=_PdnRedunNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,41,1,2,0))
_PdnEntityRedundancyConformance_ObjectIdentity=ObjectIdentity
pdnEntityRedundancyConformance=_PdnEntityRedundancyConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,41,1,3))
_PdnEntityRedundancyCompliances_ObjectIdentity=ObjectIdentity
pdnEntityRedundancyCompliances=_PdnEntityRedundancyCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,41,1,3,1))
_PdnEntityRedundancyGroups_ObjectIdentity=ObjectIdentity
pdnEntityRedundancyGroups=_PdnEntityRedundancyGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,41,1,3,2))
pdnRedundancyGeneralGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,41,1,3,2,1))
pdnRedundancyGeneralGroup.setObjects(*((_B,_M),(_B,_N),(_B,_E),(_B,_O)))
if mibBuilder.loadTexts:pdnRedundancyGeneralGroup.setStatus(_A)
pdnEntityRedundancyOptGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,41,1,3,2,2))
pdnEntityRedundancyOptGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_C)))
if mibBuilder.loadTexts:pdnEntityRedundancyOptGroup.setStatus(_A)
pdnRedunEventNoActiveModule=NotificationType((1,3,6,1,4,1,1795,2,24,2,41,1,2,0,1))
pdnRedunEventNoActiveModule.setObjects((_B,_E))
if mibBuilder.loadTexts:pdnRedunEventNoActiveModule.setStatus(_A)
pdnRedunEventHwIncompatible=NotificationType((1,3,6,1,4,1,1795,2,24,2,41,1,2,0,2))
pdnRedunEventHwIncompatible.setObjects((_B,_C))
if mibBuilder.loadTexts:pdnRedunEventHwIncompatible.setStatus(_A)
pdnRedunEventStandbyAlarmOrReset=NotificationType((1,3,6,1,4,1,1795,2,24,2,41,1,2,0,3))
pdnRedunEventStandbyAlarmOrReset.setObjects((_B,_E))
if mibBuilder.loadTexts:pdnRedunEventStandbyAlarmOrReset.setStatus(_A)
pdnRedunEventFwIncompatible=NotificationType((1,3,6,1,4,1,1795,2,24,2,41,1,2,0,4))
pdnRedunEventFwIncompatible.setObjects((_B,_C))
if mibBuilder.loadTexts:pdnRedunEventFwIncompatible.setStatus(_A)
pdnRedunEventCfgIncompatible=NotificationType((1,3,6,1,4,1,1795,2,24,2,41,1,2,0,5))
pdnRedunEventCfgIncompatible.setObjects((_B,_C))
if mibBuilder.loadTexts:pdnRedunEventCfgIncompatible.setStatus(_A)
pdnRedunEventLinkDefect=NotificationType((1,3,6,1,4,1,1795,2,24,2,41,1,2,0,6))
pdnRedunEventLinkDefect.setObjects((_B,_C))
if mibBuilder.loadTexts:pdnRedunEventLinkDefect.setStatus(_A)
pdnRedunEventHwFailure=NotificationType((1,3,6,1,4,1,1795,2,24,2,41,1,2,0,7))
pdnRedunEventHwFailure.setObjects((_B,_C))
if mibBuilder.loadTexts:pdnRedunEventHwFailure.setStatus(_A)
pdnRedunEventHwMissingHwFailure=NotificationType((1,3,6,1,4,1,1795,2,24,2,41,1,2,0,8))
pdnRedunEventHwMissingHwFailure.setObjects((_B,_C))
if mibBuilder.loadTexts:pdnRedunEventHwMissingHwFailure.setStatus(_A)
pdnEntityRedundancyEventGroup=NotificationGroup((1,3,6,1,4,1,1795,2,24,2,41,1,3,2,3))
pdnEntityRedundancyEventGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:pdnEntityRedundancyEventGroup.setStatus(_A)
pdnEntityRedundancyCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,41,1,3,1,1))
pdnEntityRedundancyCompliance.setObjects((_B,_a))
if mibBuilder.loadTexts:pdnEntityRedundancyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PdnRedunStates':PdnRedunStates,'PdnRedunCmd':PdnRedunCmd,'PdnRedunAlarmStatus':PdnRedunAlarmStatus,'PdnRedunGeneralAlarmStatus':PdnRedunGeneralAlarmStatus,'pdnEntRedunMIB':pdnEntRedunMIB,'pdnEntityRedundancyMIBObjects':pdnEntityRedundancyMIBObjects,_M:pdnEntityRedundancySelection,_N:pdnYCableSelection,_E:pdnRedunGeneralAlarmStatus,'pdnRedunCmdTable':pdnRedunCmdTable,'pdnRedunCmdEntry':pdnRedunCmdEntry,_P:pdnRedunCommand,'pdnRedunStatusTable':pdnRedunStatusTable,'pdnRedunStatusEntry':pdnRedunStatusEntry,_R:pdnRedunEntityState,_C:pdnRedunAlarmStatus,_Q:pdnRedunNotificationEnable,_O:pdnRedunGeneralNotificationEnable,'pdnEntityRedundancyNotifications':pdnEntityRedundancyNotifications,'pdnRedunNotificationsPrefix':pdnRedunNotificationsPrefix,_S:pdnRedunEventNoActiveModule,_T:pdnRedunEventHwIncompatible,_U:pdnRedunEventStandbyAlarmOrReset,_V:pdnRedunEventFwIncompatible,_W:pdnRedunEventCfgIncompatible,_X:pdnRedunEventLinkDefect,_Y:pdnRedunEventHwFailure,_Z:pdnRedunEventHwMissingHwFailure,'pdnEntityRedundancyConformance':pdnEntityRedundancyConformance,'pdnEntityRedundancyCompliances':pdnEntityRedundancyCompliances,'pdnEntityRedundancyCompliance':pdnEntityRedundancyCompliance,'pdnEntityRedundancyGroups':pdnEntityRedundancyGroups,_a:pdnRedundancyGeneralGroup,'pdnEntityRedundancyOptGroup':pdnEntityRedundancyOptGroup,'pdnEntityRedundancyEventGroup':pdnEntityRedundancyEventGroup})