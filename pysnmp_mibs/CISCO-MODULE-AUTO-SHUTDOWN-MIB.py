_a='cmasNotificationsGroup2'
_Z='cmasModuleSysActionGroup'
_Y='cmasModuleSysActionNotif'
_X='cmasModuleAutoShutdown'
_W='cmasModuleSysActionNotifEnable'
_V='cmasMIBEnableNotification'
_U='cmasModuleLastResetTime'
_T='cmasModuleEnable'
_S='cmasPeriod'
_R='cmasFrequency'
_Q='accessible-for-notify'
_P='entPhysicalIndex'
_O='cmasNotificationsGroup'
_N='cmasNotificationEnableGroup'
_M='cmasModuleGroup'
_L='cmasModuleSysActionReason'
_K='cmasModuleSysAction'
_J='cmasModuleLastResetReason'
_I='cmasModuleNumResets'
_H='read-only'
_G='TruthValue'
_F='entPhysicalName'
_E='entPhysicalModelName'
_D='read-write'
_C='ENTITY-MIB'
_B='current'
_A='CISCO-MODULE-AUTO-SHUTDOWN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalIndex,entPhysicalModelName,entPhysicalName=mibBuilder.importSymbols(_C,_P,_E,_F)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention',_G)
ciscoModuleAutoShutdownMIB=ModuleIdentity((1,3,6,1,4,1,9,9,386))
if mibBuilder.loadTexts:ciscoModuleAutoShutdownMIB.setRevisions(('2008-03-12 00:00','2003-12-29 00:00'))
class CiscoModuleAutoShutSysAction(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('reset',2),('powerCycle',3),('powerDown',4)))
_CmasMIBNotifs_ObjectIdentity=ObjectIdentity
cmasMIBNotifs=_CmasMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,386,0))
_CmasMIBObjects_ObjectIdentity=ObjectIdentity
cmasMIBObjects=_CmasMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,386,1))
_CmasGlobal_ObjectIdentity=ObjectIdentity
cmasGlobal=_CmasGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,386,1,1))
_CmasFrequency_Type=Unsigned32
_CmasFrequency_Object=MibScalar
cmasFrequency=_CmasFrequency_Object((1,3,6,1,4,1,9,9,386,1,1,1),_CmasFrequency_Type())
cmasFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:cmasFrequency.setStatus(_B)
_CmasPeriod_Type=Unsigned32
_CmasPeriod_Object=MibScalar
cmasPeriod=_CmasPeriod_Object((1,3,6,1,4,1,9,9,386,1,1,2),_CmasPeriod_Type())
cmasPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:cmasPeriod.setStatus(_B)
if mibBuilder.loadTexts:cmasPeriod.setUnits('minutes')
_CmasNotifObjects_ObjectIdentity=ObjectIdentity
cmasNotifObjects=_CmasNotifObjects_ObjectIdentity((1,3,6,1,4,1,9,9,386,1,2))
class _CmasMIBEnableNotification_Type(TruthValue):defaultValue=2
_CmasMIBEnableNotification_Type.__name__=_G
_CmasMIBEnableNotification_Object=MibScalar
cmasMIBEnableNotification=_CmasMIBEnableNotification_Object((1,3,6,1,4,1,9,9,386,1,2,1),_CmasMIBEnableNotification_Type())
cmasMIBEnableNotification.setMaxAccess(_D)
if mibBuilder.loadTexts:cmasMIBEnableNotification.setStatus(_B)
class _CmasModuleSysActionNotifEnable_Type(TruthValue):defaultValue=2
_CmasModuleSysActionNotifEnable_Type.__name__=_G
_CmasModuleSysActionNotifEnable_Object=MibScalar
cmasModuleSysActionNotifEnable=_CmasModuleSysActionNotifEnable_Object((1,3,6,1,4,1,9,9,386,1,2,2),_CmasModuleSysActionNotifEnable_Type())
cmasModuleSysActionNotifEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cmasModuleSysActionNotifEnable.setStatus(_B)
_CmasModule_ObjectIdentity=ObjectIdentity
cmasModule=_CmasModule_ObjectIdentity((1,3,6,1,4,1,9,9,386,1,3))
_CmasModuleTable_Object=MibTable
cmasModuleTable=_CmasModuleTable_Object((1,3,6,1,4,1,9,9,386,1,3,1))
if mibBuilder.loadTexts:cmasModuleTable.setStatus(_B)
_CmasModuleEntry_Object=MibTableRow
cmasModuleEntry=_CmasModuleEntry_Object((1,3,6,1,4,1,9,9,386,1,3,1,1))
cmasModuleEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:cmasModuleEntry.setStatus(_B)
_CmasModuleEnable_Type=TruthValue
_CmasModuleEnable_Object=MibTableColumn
cmasModuleEnable=_CmasModuleEnable_Object((1,3,6,1,4,1,9,9,386,1,3,1,1,1),_CmasModuleEnable_Type())
cmasModuleEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cmasModuleEnable.setStatus(_B)
_CmasModuleNumResets_Type=Gauge32
_CmasModuleNumResets_Object=MibTableColumn
cmasModuleNumResets=_CmasModuleNumResets_Object((1,3,6,1,4,1,9,9,386,1,3,1,1,2),_CmasModuleNumResets_Type())
cmasModuleNumResets.setMaxAccess(_H)
if mibBuilder.loadTexts:cmasModuleNumResets.setStatus(_B)
_CmasModuleLastResetReason_Type=SnmpAdminString
_CmasModuleLastResetReason_Object=MibTableColumn
cmasModuleLastResetReason=_CmasModuleLastResetReason_Object((1,3,6,1,4,1,9,9,386,1,3,1,1,3),_CmasModuleLastResetReason_Type())
cmasModuleLastResetReason.setMaxAccess(_H)
if mibBuilder.loadTexts:cmasModuleLastResetReason.setStatus(_B)
_CmasModuleLastResetTime_Type=DateAndTime
_CmasModuleLastResetTime_Object=MibTableColumn
cmasModuleLastResetTime=_CmasModuleLastResetTime_Object((1,3,6,1,4,1,9,9,386,1,3,1,1,4),_CmasModuleLastResetTime_Type())
cmasModuleLastResetTime.setMaxAccess(_H)
if mibBuilder.loadTexts:cmasModuleLastResetTime.setStatus(_B)
_CmasModuleSysActionObjects_ObjectIdentity=ObjectIdentity
cmasModuleSysActionObjects=_CmasModuleSysActionObjects_ObjectIdentity((1,3,6,1,4,1,9,9,386,1,4))
_CmasModuleSysAction_Type=CiscoModuleAutoShutSysAction
_CmasModuleSysAction_Object=MibScalar
cmasModuleSysAction=_CmasModuleSysAction_Object((1,3,6,1,4,1,9,9,386,1,4,1),_CmasModuleSysAction_Type())
cmasModuleSysAction.setMaxAccess(_Q)
if mibBuilder.loadTexts:cmasModuleSysAction.setStatus(_B)
_CmasModuleSysActionReason_Type=SnmpAdminString
_CmasModuleSysActionReason_Object=MibScalar
cmasModuleSysActionReason=_CmasModuleSysActionReason_Object((1,3,6,1,4,1,9,9,386,1,4,2),_CmasModuleSysActionReason_Type())
cmasModuleSysActionReason.setMaxAccess(_Q)
if mibBuilder.loadTexts:cmasModuleSysActionReason.setStatus(_B)
_CmasMIBConformance_ObjectIdentity=ObjectIdentity
cmasMIBConformance=_CmasMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,386,2))
_CmasMIBCompliances_ObjectIdentity=ObjectIdentity
cmasMIBCompliances=_CmasMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,386,2,1))
_CmasMIBGroups_ObjectIdentity=ObjectIdentity
cmasMIBGroups=_CmasMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,386,2,2))
cmasModuleGroup=ObjectGroup((1,3,6,1,4,1,9,9,386,2,2,1))
cmasModuleGroup.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_I),(_A,_J),(_A,_U)))
if mibBuilder.loadTexts:cmasModuleGroup.setStatus(_B)
cmasNotificationEnableGroup=ObjectGroup((1,3,6,1,4,1,9,9,386,2,2,2))
cmasNotificationEnableGroup.setObjects((_A,_V))
if mibBuilder.loadTexts:cmasNotificationEnableGroup.setStatus(_B)
cmasModuleSysActionGroup=ObjectGroup((1,3,6,1,4,1,9,9,386,2,2,4))
cmasModuleSysActionGroup.setObjects(*((_A,_W),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:cmasModuleSysActionGroup.setStatus(_B)
cmasModuleAutoShutdown=NotificationType((1,3,6,1,4,1,9,9,386,0,1))
cmasModuleAutoShutdown.setObjects(*((_C,_F),(_C,_E),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:cmasModuleAutoShutdown.setStatus(_B)
cmasModuleSysActionNotif=NotificationType((1,3,6,1,4,1,9,9,386,0,2))
cmasModuleSysActionNotif.setObjects(*((_C,_F),(_C,_E),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:cmasModuleSysActionNotif.setStatus(_B)
cmasNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,386,2,2,3))
cmasNotificationsGroup.setObjects((_A,_X))
if mibBuilder.loadTexts:cmasNotificationsGroup.setStatus(_B)
cmasNotificationsGroup2=NotificationGroup((1,3,6,1,4,1,9,9,386,2,2,5))
cmasNotificationsGroup2.setObjects((_A,_Y))
if mibBuilder.loadTexts:cmasNotificationsGroup2.setStatus(_B)
cmasMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,386,2,1,1))
cmasMIBCompliance.setObjects(*((_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:cmasMIBCompliance.setStatus('deprecated')
cmasMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,386,2,1,2))
cmasMIBCompliance2.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:cmasMIBCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CiscoModuleAutoShutSysAction':CiscoModuleAutoShutSysAction,'ciscoModuleAutoShutdownMIB':ciscoModuleAutoShutdownMIB,'cmasMIBNotifs':cmasMIBNotifs,_X:cmasModuleAutoShutdown,_Y:cmasModuleSysActionNotif,'cmasMIBObjects':cmasMIBObjects,'cmasGlobal':cmasGlobal,_R:cmasFrequency,_S:cmasPeriod,'cmasNotifObjects':cmasNotifObjects,_V:cmasMIBEnableNotification,_W:cmasModuleSysActionNotifEnable,'cmasModule':cmasModule,'cmasModuleTable':cmasModuleTable,'cmasModuleEntry':cmasModuleEntry,_T:cmasModuleEnable,_I:cmasModuleNumResets,_J:cmasModuleLastResetReason,_U:cmasModuleLastResetTime,'cmasModuleSysActionObjects':cmasModuleSysActionObjects,_K:cmasModuleSysAction,_L:cmasModuleSysActionReason,'cmasMIBConformance':cmasMIBConformance,'cmasMIBCompliances':cmasMIBCompliances,'cmasMIBCompliance':cmasMIBCompliance,'cmasMIBCompliance2':cmasMIBCompliance2,'cmasMIBGroups':cmasMIBGroups,_M:cmasModuleGroup,_N:cmasNotificationEnableGroup,_O:cmasNotificationsGroup,_Z:cmasModuleSysActionGroup,_a:cmasNotificationsGroup2})