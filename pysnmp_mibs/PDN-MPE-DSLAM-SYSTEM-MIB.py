_s='mpeDslamDeprecatedNotificationsGroup'
_r='mpeDslamDeprecatedObjectsGroup'
_q='mpeEntityExtPowerFailureNotificationGroup'
_p='mpeEntPhysicalExtNotificationObjectGroup'
_o='mpeEntPhysicalExtGroup'
_n='mpeSysDevDslamAlarmRelayGroup'
_m='mpeEntityExtNotificationGroup'
_l='mpeSysDevDslamAlarmStateGroup'
_k='mpeAlarmRelayInputContactStateChanged'
_j='mpePowerSourceBOperational'
_i='mpePowerSourceAOperational'
_h='mpePowerSourceBFailure'
_g='mpePowerSourceAFailure'
_f='mpeFanEntityModuleOperational'
_e='mpeFanEntityModuleFailure'
_d='mpeAlarmRelayInputStateChanged'
_c='mpeEntPhysicalExtEntityChanged'
_b='mpeEntPhysicalExtEntityDeleted'
_a='mpeEntPhysicalExtEntityCreated'
_Z='mpeNonSupportedChassis'
_Y='mpeNonSupportedMCC'
_X='mpeDeviceFailureCleared'
_W='mpeDeviceFailure'
_V='mpeCcn'
_U='mpeEntPhysicalExtOperStatus'
_T='mpeEntPhysicalExtAdminStatus'
_S='mpeEntPhysicalExtLocation'
_R='mpeEntPhysicalExtUpTime'
_Q='mpeEntExtAlarm'
_P='mpeEntPhysicalExtEntry'
_O='mpeEntExtAlarmEntry'
_N='accessible-for-notify'
_M='testing'
_L='mpeAlarmRelayInputContactState'
_K='mpeAlarmRelayEquipIndex'
_J='mpeAlarmRelayState'
_I='read-write'
_H='read-only'
_G='mpeSysObjectID'
_F='PDN-MPE-MIB2-MIB'
_E='deprecated'
_D='entPhysicalIndex'
_C='ENTITY-MIB'
_B='current'
_A='PDN-MPE-DSLAM-SYSTEM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalEntry,entPhysicalIndex=mibBuilder.importSymbols(_C,'entPhysicalEntry',_D)
pdn_mpe,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-mpe')
mpeSysObjectID,=mibBuilder.importSymbols(_F,_G)
ContactState,=mibBuilder.importSymbols('PDN-TC','ContactState')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
mpe_dslam=ModuleIdentity((1,3,6,1,4,1,1795,2,24,12,24))
if mibBuilder.loadTexts:mpe_dslam.setRevisions(('2004-05-13 14:00','2005-04-08 14:00','2003-06-06 00:00','2003-04-25 00:00','2003-04-18 00:00','2003-03-20 15:00','2003-03-07 00:00','2002-10-25 00:00','2002-08-15 00:00','2002-02-21 00:00','2002-01-28 00:00','2000-01-22 00:00'))
class MpeEntExtAdminStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_M,3)))
class MpeEntExtOperStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('up',1),('down',2),(_M,3),('unknown',4),('dormant',5),('notPresent',6),('reserved1',7)))
_MpeSysDevDslamMIBObjects_ObjectIdentity=ObjectIdentity
mpeSysDevDslamMIBObjects=_MpeSysDevDslamMIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,24,1))
_MpeEntExtAlarms_ObjectIdentity=ObjectIdentity
mpeEntExtAlarms=_MpeEntExtAlarms_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,24,1,1))
_MpeEntExtAlarmTable_Object=MibTable
mpeEntExtAlarmTable=_MpeEntExtAlarmTable_Object((1,3,6,1,4,1,1795,2,24,12,24,1,1,1))
if mibBuilder.loadTexts:mpeEntExtAlarmTable.setStatus(_B)
_MpeEntExtAlarmEntry_Object=MibTableRow
mpeEntExtAlarmEntry=_MpeEntExtAlarmEntry_Object((1,3,6,1,4,1,1795,2,24,12,24,1,1,1,1))
if mibBuilder.loadTexts:mpeEntExtAlarmEntry.setStatus(_B)
_MpeEntExtAlarm_Type=TruthValue
_MpeEntExtAlarm_Object=MibTableColumn
mpeEntExtAlarm=_MpeEntExtAlarm_Object((1,3,6,1,4,1,1795,2,24,12,24,1,1,1,1,1),_MpeEntExtAlarm_Type())
mpeEntExtAlarm.setMaxAccess(_H)
if mibBuilder.loadTexts:mpeEntExtAlarm.setStatus(_B)
_MpeAlarmRelay_ObjectIdentity=ObjectIdentity
mpeAlarmRelay=_MpeAlarmRelay_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,24,1,2))
_MpeAlarmRelayEquipIndex_Type=Integer32
_MpeAlarmRelayEquipIndex_Object=MibScalar
mpeAlarmRelayEquipIndex=_MpeAlarmRelayEquipIndex_Object((1,3,6,1,4,1,1795,2,24,12,24,1,2,1),_MpeAlarmRelayEquipIndex_Type())
mpeAlarmRelayEquipIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:mpeAlarmRelayEquipIndex.setStatus(_E)
_MpeAlarmRelayInputContactState_Type=ContactState
_MpeAlarmRelayInputContactState_Object=MibScalar
mpeAlarmRelayInputContactState=_MpeAlarmRelayInputContactState_Object((1,3,6,1,4,1,1795,2,24,12,24,1,2,2),_MpeAlarmRelayInputContactState_Type())
mpeAlarmRelayInputContactState.setMaxAccess(_N)
if mibBuilder.loadTexts:mpeAlarmRelayInputContactState.setStatus(_E)
_MpeAlarmRelayTable_Object=MibTable
mpeAlarmRelayTable=_MpeAlarmRelayTable_Object((1,3,6,1,4,1,1795,2,24,12,24,1,2,3))
if mibBuilder.loadTexts:mpeAlarmRelayTable.setStatus(_B)
_MpeAlarmRelayEntry_Object=MibTableRow
mpeAlarmRelayEntry=_MpeAlarmRelayEntry_Object((1,3,6,1,4,1,1795,2,24,12,24,1,2,3,1))
mpeAlarmRelayEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:mpeAlarmRelayEntry.setStatus(_B)
_MpeAlarmRelayState_Type=ContactState
_MpeAlarmRelayState_Object=MibTableColumn
mpeAlarmRelayState=_MpeAlarmRelayState_Object((1,3,6,1,4,1,1795,2,24,12,24,1,2,3,1,1),_MpeAlarmRelayState_Type())
mpeAlarmRelayState.setMaxAccess(_I)
if mibBuilder.loadTexts:mpeAlarmRelayState.setStatus(_B)
_MpeEntExtMibObjects_ObjectIdentity=ObjectIdentity
mpeEntExtMibObjects=_MpeEntExtMibObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,24,1,3))
_MpeEntPhysicalExtTable_Object=MibTable
mpeEntPhysicalExtTable=_MpeEntPhysicalExtTable_Object((1,3,6,1,4,1,1795,2,24,12,24,1,3,1))
if mibBuilder.loadTexts:mpeEntPhysicalExtTable.setStatus(_B)
_MpeEntPhysicalExtEntry_Object=MibTableRow
mpeEntPhysicalExtEntry=_MpeEntPhysicalExtEntry_Object((1,3,6,1,4,1,1795,2,24,12,24,1,3,1,1))
if mibBuilder.loadTexts:mpeEntPhysicalExtEntry.setStatus(_B)
_MpeEntPhysicalExtUpTime_Type=TimeTicks
_MpeEntPhysicalExtUpTime_Object=MibTableColumn
mpeEntPhysicalExtUpTime=_MpeEntPhysicalExtUpTime_Object((1,3,6,1,4,1,1795,2,24,12,24,1,3,1,1,1),_MpeEntPhysicalExtUpTime_Type())
mpeEntPhysicalExtUpTime.setMaxAccess(_H)
if mibBuilder.loadTexts:mpeEntPhysicalExtUpTime.setStatus(_B)
_MpeEntPhysicalExtLocation_Type=SnmpAdminString
_MpeEntPhysicalExtLocation_Object=MibTableColumn
mpeEntPhysicalExtLocation=_MpeEntPhysicalExtLocation_Object((1,3,6,1,4,1,1795,2,24,12,24,1,3,1,1,2),_MpeEntPhysicalExtLocation_Type())
mpeEntPhysicalExtLocation.setMaxAccess(_I)
if mibBuilder.loadTexts:mpeEntPhysicalExtLocation.setStatus(_B)
_MpeEntPhysicalExtAdminStatus_Type=MpeEntExtAdminStatus
_MpeEntPhysicalExtAdminStatus_Object=MibTableColumn
mpeEntPhysicalExtAdminStatus=_MpeEntPhysicalExtAdminStatus_Object((1,3,6,1,4,1,1795,2,24,12,24,1,3,1,1,3),_MpeEntPhysicalExtAdminStatus_Type())
mpeEntPhysicalExtAdminStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:mpeEntPhysicalExtAdminStatus.setStatus(_B)
_MpeEntPhysicalExtOperStatus_Type=MpeEntExtOperStatus
_MpeEntPhysicalExtOperStatus_Object=MibTableColumn
mpeEntPhysicalExtOperStatus=_MpeEntPhysicalExtOperStatus_Object((1,3,6,1,4,1,1795,2,24,12,24,1,3,1,1,4),_MpeEntPhysicalExtOperStatus_Type())
mpeEntPhysicalExtOperStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:mpeEntPhysicalExtOperStatus.setStatus(_B)
_MpeSysDevDslamMIBTraps_ObjectIdentity=ObjectIdentity
mpeSysDevDslamMIBTraps=_MpeSysDevDslamMIBTraps_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,24,2))
_MpeSysDevDslamMIBNotifications_ObjectIdentity=ObjectIdentity
mpeSysDevDslamMIBNotifications=_MpeSysDevDslamMIBNotifications_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,24,2,0))
_MpeSysDevDslamConformance_ObjectIdentity=ObjectIdentity
mpeSysDevDslamConformance=_MpeSysDevDslamConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,24,3))
_MpeSysDevDslamGroups_ObjectIdentity=ObjectIdentity
mpeSysDevDslamGroups=_MpeSysDevDslamGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,24,3,1))
_MpeSysDevDslamCompliances_ObjectIdentity=ObjectIdentity
mpeSysDevDslamCompliances=_MpeSysDevDslamCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,24,3,2))
_MpeSysDevDslamDeprecatedGroup_ObjectIdentity=ObjectIdentity
mpeSysDevDslamDeprecatedGroup=_MpeSysDevDslamDeprecatedGroup_ObjectIdentity((1,3,6,1,4,1,1795,2,24,12,24,3,3))
entPhysicalEntry.registerAugmentions((_A,_O))
mpeEntExtAlarmEntry.setIndexNames(*entPhysicalEntry.getIndexNames())
entPhysicalEntry.registerAugmentions((_A,_P))
mpeEntPhysicalExtEntry.setIndexNames(*entPhysicalEntry.getIndexNames())
mpeSysDevDslamAlarmStateGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,12,24,3,1,1))
mpeSysDevDslamAlarmStateGroup.setObjects((_A,_Q))
if mibBuilder.loadTexts:mpeSysDevDslamAlarmStateGroup.setStatus(_B)
mpeSysDevDslamAlarmRelayGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,12,24,3,1,3))
mpeSysDevDslamAlarmRelayGroup.setObjects((_A,_J))
if mibBuilder.loadTexts:mpeSysDevDslamAlarmRelayGroup.setStatus(_B)
mpeEntPhysicalExtGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,12,24,3,1,4))
mpeEntPhysicalExtGroup.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:mpeEntPhysicalExtGroup.setStatus(_B)
mpeEntPhysicalExtNotificationObjectGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,12,24,3,1,5))
mpeEntPhysicalExtNotificationObjectGroup.setObjects((_C,_D))
if mibBuilder.loadTexts:mpeEntPhysicalExtNotificationObjectGroup.setStatus(_B)
mpeDslamDeprecatedObjectsGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,12,24,3,3,1))
mpeDslamDeprecatedObjectsGroup.setObjects(*((_A,_K),(_A,_L)))
if mibBuilder.loadTexts:mpeDslamDeprecatedObjectsGroup.setStatus(_E)
mpeAlarmRelayInputStateChanged=NotificationType((1,3,6,1,4,1,1795,2,24,12,24,2,0,26))
mpeAlarmRelayInputStateChanged.setObjects((_A,_J))
if mibBuilder.loadTexts:mpeAlarmRelayInputStateChanged.setStatus(_B)
mpeFanEntityModuleFailure=NotificationType((1,3,6,1,4,1,1795,2,24,12,24,2,0,27))
mpeFanEntityModuleFailure.setObjects((_C,_D))
if mibBuilder.loadTexts:mpeFanEntityModuleFailure.setStatus(_B)
mpeFanEntityModuleOperational=NotificationType((1,3,6,1,4,1,1795,2,24,12,24,2,0,28))
mpeFanEntityModuleOperational.setObjects((_C,_D))
if mibBuilder.loadTexts:mpeFanEntityModuleOperational.setStatus(_B)
mpePowerSourceAFailure=NotificationType((1,3,6,1,4,1,1795,2,24,12,24,2,0,29))
mpePowerSourceAFailure.setObjects((_C,_D))
if mibBuilder.loadTexts:mpePowerSourceAFailure.setStatus(_B)
mpePowerSourceBFailure=NotificationType((1,3,6,1,4,1,1795,2,24,12,24,2,0,30))
mpePowerSourceBFailure.setObjects((_C,_D))
if mibBuilder.loadTexts:mpePowerSourceBFailure.setStatus(_B)
mpePowerSourceAOperational=NotificationType((1,3,6,1,4,1,1795,2,24,12,24,2,0,31))
mpePowerSourceAOperational.setObjects((_C,_D))
if mibBuilder.loadTexts:mpePowerSourceAOperational.setStatus(_B)
mpePowerSourceBOperational=NotificationType((1,3,6,1,4,1,1795,2,24,12,24,2,0,32))
mpePowerSourceBOperational.setObjects((_C,_D))
if mibBuilder.loadTexts:mpePowerSourceBOperational.setStatus(_B)
mpeCcn=NotificationType((1,3,6,1,4,1,1795,2,24,12,24,2,7))
mpeCcn.setObjects((_C,_D))
if mibBuilder.loadTexts:mpeCcn.setStatus(_B)
mpeDeviceFailure=NotificationType((1,3,6,1,4,1,1795,2,24,12,24,2,15))
mpeDeviceFailure.setObjects((_C,_D))
if mibBuilder.loadTexts:mpeDeviceFailure.setStatus(_B)
mpeDeviceFailureCleared=NotificationType((1,3,6,1,4,1,1795,2,24,12,24,2,16))
mpeDeviceFailureCleared.setObjects((_C,_D))
if mibBuilder.loadTexts:mpeDeviceFailureCleared.setStatus(_B)
mpeNonSupportedMCC=NotificationType((1,3,6,1,4,1,1795,2,24,12,24,2,20))
mpeNonSupportedMCC.setObjects((_F,_G))
if mibBuilder.loadTexts:mpeNonSupportedMCC.setStatus(_B)
mpeNonSupportedChassis=NotificationType((1,3,6,1,4,1,1795,2,24,12,24,2,21))
mpeNonSupportedChassis.setObjects((_F,_G))
if mibBuilder.loadTexts:mpeNonSupportedChassis.setStatus(_B)
mpeAlarmRelayInputContactStateChanged=NotificationType((1,3,6,1,4,1,1795,2,24,12,24,2,22))
mpeAlarmRelayInputContactStateChanged.setObjects(*((_A,_K),(_A,_L)))
if mibBuilder.loadTexts:mpeAlarmRelayInputContactStateChanged.setStatus(_E)
mpeEntPhysicalExtEntityCreated=NotificationType((1,3,6,1,4,1,1795,2,24,12,24,2,23))
mpeEntPhysicalExtEntityCreated.setObjects((_C,_D))
if mibBuilder.loadTexts:mpeEntPhysicalExtEntityCreated.setStatus(_B)
mpeEntPhysicalExtEntityDeleted=NotificationType((1,3,6,1,4,1,1795,2,24,12,24,2,24))
mpeEntPhysicalExtEntityDeleted.setObjects((_C,_D))
if mibBuilder.loadTexts:mpeEntPhysicalExtEntityDeleted.setStatus(_B)
mpeEntPhysicalExtEntityChanged=NotificationType((1,3,6,1,4,1,1795,2,24,12,24,2,25))
mpeEntPhysicalExtEntityChanged.setObjects((_C,_D))
if mibBuilder.loadTexts:mpeEntPhysicalExtEntityChanged.setStatus(_B)
mpeEntityExtNotificationGroup=NotificationGroup((1,3,6,1,4,1,1795,2,24,12,24,3,1,2))
mpeEntityExtNotificationGroup.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:mpeEntityExtNotificationGroup.setStatus(_B)
mpeEntityExtPowerFailureNotificationGroup=NotificationGroup((1,3,6,1,4,1,1795,2,24,12,24,3,1,6))
mpeEntityExtPowerFailureNotificationGroup.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j)))
if mibBuilder.loadTexts:mpeEntityExtPowerFailureNotificationGroup.setStatus(_B)
mpeDslamDeprecatedNotificationsGroup=NotificationGroup((1,3,6,1,4,1,1795,2,24,12,24,3,3,2))
mpeDslamDeprecatedNotificationsGroup.setObjects((_A,_k))
if mibBuilder.loadTexts:mpeDslamDeprecatedNotificationsGroup.setStatus(_E)
mpeSysDevDslamAlarmCompliances=ModuleCompliance((1,3,6,1,4,1,1795,2,24,12,24,3,2,1))
mpeSysDevDslamAlarmCompliances.setObjects(*((_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:mpeSysDevDslamAlarmCompliances.setStatus(_B)
mpeSysDevDslamAlarmDeprecatedCompliances=ModuleCompliance((1,3,6,1,4,1,1795,2,24,12,24,3,2,2))
mpeSysDevDslamAlarmDeprecatedCompliances.setObjects(*((_A,_r),(_A,_s)))
if mibBuilder.loadTexts:mpeSysDevDslamAlarmDeprecatedCompliances.setStatus(_E)
mibBuilder.exportSymbols(_A,**{'MpeEntExtAdminStatus':MpeEntExtAdminStatus,'MpeEntExtOperStatus':MpeEntExtOperStatus,'mpe-dslam':mpe_dslam,'mpeSysDevDslamMIBObjects':mpeSysDevDslamMIBObjects,'mpeEntExtAlarms':mpeEntExtAlarms,'mpeEntExtAlarmTable':mpeEntExtAlarmTable,_O:mpeEntExtAlarmEntry,_Q:mpeEntExtAlarm,'mpeAlarmRelay':mpeAlarmRelay,_K:mpeAlarmRelayEquipIndex,_L:mpeAlarmRelayInputContactState,'mpeAlarmRelayTable':mpeAlarmRelayTable,'mpeAlarmRelayEntry':mpeAlarmRelayEntry,_J:mpeAlarmRelayState,'mpeEntExtMibObjects':mpeEntExtMibObjects,'mpeEntPhysicalExtTable':mpeEntPhysicalExtTable,_P:mpeEntPhysicalExtEntry,_R:mpeEntPhysicalExtUpTime,_S:mpeEntPhysicalExtLocation,_T:mpeEntPhysicalExtAdminStatus,_U:mpeEntPhysicalExtOperStatus,'mpeSysDevDslamMIBTraps':mpeSysDevDslamMIBTraps,'mpeSysDevDslamMIBNotifications':mpeSysDevDslamMIBNotifications,_d:mpeAlarmRelayInputStateChanged,_e:mpeFanEntityModuleFailure,_f:mpeFanEntityModuleOperational,_g:mpePowerSourceAFailure,_h:mpePowerSourceBFailure,_i:mpePowerSourceAOperational,_j:mpePowerSourceBOperational,_V:mpeCcn,_W:mpeDeviceFailure,_X:mpeDeviceFailureCleared,_Y:mpeNonSupportedMCC,_Z:mpeNonSupportedChassis,_k:mpeAlarmRelayInputContactStateChanged,_a:mpeEntPhysicalExtEntityCreated,_b:mpeEntPhysicalExtEntityDeleted,_c:mpeEntPhysicalExtEntityChanged,'mpeSysDevDslamConformance':mpeSysDevDslamConformance,'mpeSysDevDslamGroups':mpeSysDevDslamGroups,_l:mpeSysDevDslamAlarmStateGroup,_m:mpeEntityExtNotificationGroup,_n:mpeSysDevDslamAlarmRelayGroup,_o:mpeEntPhysicalExtGroup,_p:mpeEntPhysicalExtNotificationObjectGroup,_q:mpeEntityExtPowerFailureNotificationGroup,'mpeSysDevDslamCompliances':mpeSysDevDslamCompliances,'mpeSysDevDslamAlarmCompliances':mpeSysDevDslamAlarmCompliances,'mpeSysDevDslamAlarmDeprecatedCompliances':mpeSysDevDslamAlarmDeprecatedCompliances,'mpeSysDevDslamDeprecatedGroup':mpeSysDevDslamDeprecatedGroup,_r:mpeDslamDeprecatedObjectsGroup,_s:mpeDslamDeprecatedNotificationsGroup})