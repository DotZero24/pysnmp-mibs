_i='vcModuleGroup2'
_h='vcModPortProtectionConditionCleared'
_g='vcModPortProtectionConditionDetected'
_f='vcModPortBpduLoopCleared'
_e='vcModPortBpduLoopDetected'
_d='vcModPortOutputErrorsDown'
_c='vcModPortOutputErrorsUp'
_b='vcModPortInputErrorsDown'
_a='vcModPortInputErrorsUp'
_Z='vcModPortOutputUtilizationDown'
_Y='vcModPortOutputUtilizationUp'
_X='vcModPortInputUtilizationDown'
_W='vcModPortInputUtilizationUp'
_V='deprecated'
_U='Integer32'
_T='vcModPortStatusNotificationsGroup'
_S='vcModPortThresholdNotificationsGroup'
_R='vcModuleGroup'
_Q='vcModulePortProtectionStatus'
_P='vcModulePortBpduLoopStatus'
_O='vcSwitchMemParityErrorNonCorrectableCount'
_N='vcModuleDomainPrimaryAddressIpv6'
_M='vcModuleDomainPrimaryAddress'
_L='vcModuleDomainPrimaryAddressType'
_K='vcModuleDomainName'
_J='ifOutErrors'
_I='ifInErrors'
_H='vcSwitchMemParityErrorCount'
_G='vcModuleRole'
_F='vcModulePort'
_E='read-only'
_D='ifIndex'
_C='IF-MIB'
_B='current'
_A='HPVCMODULE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,ifInErrors,ifIndex,ifOutErrors=mibBuilder.importSymbols(_C,'InterfaceIndex',_I,_D,_J)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mib_2,zeroDotZero=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_U,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mib-2','zeroDotZero')
DisplayString,PhysAddress,RowPointer,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','TextualConvention','TruthValue')
TransportAddress,TransportAddressType=mibBuilder.importSymbols('TRANSPORT-ADDRESS-MIB','TransportAddress','TransportAddressType')
vcModuleMIB=ModuleIdentity((1,3,6,1,4,1,11,5,7,5,2,3))
if mibBuilder.loadTexts:vcModuleMIB.setRevisions(('2020-04-14 00:00','2019-01-29 00:00','2016-03-21 00:00','2014-01-29 00:00','2013-11-07 00:00','2012-09-22 00:00','2012-08-19 00:00','2011-02-01 00:00','2009-02-18 00:00','2008-10-08 00:00'))
class VcModuleRole(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unintegrated',1),('primaryProtected',2),('primaryUnprotected',3),('standby',4),('other',5)))
class VcEnclosureRole(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unknown',1),('primary',2),('secondary',3)))
class VcModuleType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('vcModuleEnet',1),('vcModuleFC',2),('vcModuleOther',3)))
class VcModulePortBpduLoopStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ok',1),('loop-detected',2)))
class VcModulePortProtectionStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ok',1),('pause-flood-detected',2),('in-pause-condition',3)))
_Hp_ObjectIdentity=ObjectIdentity
hp=_Hp_ObjectIdentity((1,3,6,1,4,1,11))
_HpSysMgt_ObjectIdentity=ObjectIdentity
hpSysMgt=_HpSysMgt_ObjectIdentity((1,3,6,1,4,1,11,5))
_HpEmbeddedServerMgt_ObjectIdentity=ObjectIdentity
hpEmbeddedServerMgt=_HpEmbeddedServerMgt_ObjectIdentity((1,3,6,1,4,1,11,5,7))
_HpModuleMgmtProc_ObjectIdentity=ObjectIdentity
hpModuleMgmtProc=_HpModuleMgmtProc_ObjectIdentity((1,3,6,1,4,1,11,5,7,5))
_VirtualConnect_ObjectIdentity=ObjectIdentity
virtualConnect=_VirtualConnect_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2))
_VcModuleMIBObjects_ObjectIdentity=ObjectIdentity
vcModuleMIBObjects=_VcModuleMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,3,1))
_VcModuleObjects_ObjectIdentity=ObjectIdentity
vcModuleObjects=_VcModuleObjects_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,3,1,1))
_VcModuleDomainName_Type=SnmpAdminString
_VcModuleDomainName_Object=MibScalar
vcModuleDomainName=_VcModuleDomainName_Object((1,3,6,1,4,1,11,5,7,5,2,3,1,1,1),_VcModuleDomainName_Type())
vcModuleDomainName.setMaxAccess(_E)
if mibBuilder.loadTexts:vcModuleDomainName.setStatus(_B)
_VcModuleRole_Type=VcModuleRole
_VcModuleRole_Object=MibScalar
vcModuleRole=_VcModuleRole_Object((1,3,6,1,4,1,11,5,7,5,2,3,1,1,2),_VcModuleRole_Type())
vcModuleRole.setMaxAccess(_E)
if mibBuilder.loadTexts:vcModuleRole.setStatus(_B)
_VcModuleDomainPrimaryAddressType_Type=TransportAddressType
_VcModuleDomainPrimaryAddressType_Object=MibScalar
vcModuleDomainPrimaryAddressType=_VcModuleDomainPrimaryAddressType_Object((1,3,6,1,4,1,11,5,7,5,2,3,1,1,3),_VcModuleDomainPrimaryAddressType_Type())
vcModuleDomainPrimaryAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:vcModuleDomainPrimaryAddressType.setStatus(_B)
_VcModuleDomainPrimaryAddress_Type=TransportAddress
_VcModuleDomainPrimaryAddress_Object=MibScalar
vcModuleDomainPrimaryAddress=_VcModuleDomainPrimaryAddress_Object((1,3,6,1,4,1,11,5,7,5,2,3,1,1,4),_VcModuleDomainPrimaryAddress_Type())
vcModuleDomainPrimaryAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:vcModuleDomainPrimaryAddress.setStatus(_B)
_VcModuleEnclosureRole_Type=VcEnclosureRole
_VcModuleEnclosureRole_Object=MibScalar
vcModuleEnclosureRole=_VcModuleEnclosureRole_Object((1,3,6,1,4,1,11,5,7,5,2,3,1,1,5),_VcModuleEnclosureRole_Type())
vcModuleEnclosureRole.setMaxAccess(_E)
if mibBuilder.loadTexts:vcModuleEnclosureRole.setStatus(_B)
_VcModulePortTable_Object=MibTable
vcModulePortTable=_VcModulePortTable_Object((1,3,6,1,4,1,11,5,7,5,2,3,1,1,6))
if mibBuilder.loadTexts:vcModulePortTable.setStatus(_B)
_VcModulePortEntry_Object=MibTableRow
vcModulePortEntry=_VcModulePortEntry_Object((1,3,6,1,4,1,11,5,7,5,2,3,1,1,6,1))
vcModulePortEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:vcModulePortEntry.setStatus(_B)
class _VcModulePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_VcModulePort_Type.__name__=_U
_VcModulePort_Object=MibTableColumn
vcModulePort=_VcModulePort_Object((1,3,6,1,4,1,11,5,7,5,2,3,1,1,6,1,1),_VcModulePort_Type())
vcModulePort.setMaxAccess(_E)
if mibBuilder.loadTexts:vcModulePort.setStatus(_B)
_VcModulePortIfIndex_Type=InterfaceIndex
_VcModulePortIfIndex_Object=MibTableColumn
vcModulePortIfIndex=_VcModulePortIfIndex_Object((1,3,6,1,4,1,11,5,7,5,2,3,1,1,6,1,2),_VcModulePortIfIndex_Type())
vcModulePortIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:vcModulePortIfIndex.setStatus(_B)
_VcModulePortBpduLoopStatus_Type=VcModulePortBpduLoopStatus
_VcModulePortBpduLoopStatus_Object=MibTableColumn
vcModulePortBpduLoopStatus=_VcModulePortBpduLoopStatus_Object((1,3,6,1,4,1,11,5,7,5,2,3,1,1,6,1,3),_VcModulePortBpduLoopStatus_Type())
vcModulePortBpduLoopStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:vcModulePortBpduLoopStatus.setStatus(_B)
_VcModulePortProtectionStatus_Type=VcModulePortProtectionStatus
_VcModulePortProtectionStatus_Object=MibTableColumn
vcModulePortProtectionStatus=_VcModulePortProtectionStatus_Object((1,3,6,1,4,1,11,5,7,5,2,3,1,1,6,1,4),_VcModulePortProtectionStatus_Type())
vcModulePortProtectionStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:vcModulePortProtectionStatus.setStatus(_B)
_VcModuleDomainPrimaryAddressIpv6_Type=TransportAddress
_VcModuleDomainPrimaryAddressIpv6_Object=MibScalar
vcModuleDomainPrimaryAddressIpv6=_VcModuleDomainPrimaryAddressIpv6_Object((1,3,6,1,4,1,11,5,7,5,2,3,1,1,7),_VcModuleDomainPrimaryAddressIpv6_Type())
vcModuleDomainPrimaryAddressIpv6.setMaxAccess(_E)
if mibBuilder.loadTexts:vcModuleDomainPrimaryAddressIpv6.setStatus(_B)
_VcSwitchMemParityErrorCount_Type=Counter32
_VcSwitchMemParityErrorCount_Object=MibScalar
vcSwitchMemParityErrorCount=_VcSwitchMemParityErrorCount_Object((1,3,6,1,4,1,11,5,7,5,2,3,1,1,8),_VcSwitchMemParityErrorCount_Type())
vcSwitchMemParityErrorCount.setMaxAccess(_E)
if mibBuilder.loadTexts:vcSwitchMemParityErrorCount.setStatus(_B)
_VcSwitchMemParityErrorNonCorrectableCount_Type=Counter32
_VcSwitchMemParityErrorNonCorrectableCount_Object=MibScalar
vcSwitchMemParityErrorNonCorrectableCount=_VcSwitchMemParityErrorNonCorrectableCount_Object((1,3,6,1,4,1,11,5,7,5,2,3,1,1,9),_VcSwitchMemParityErrorNonCorrectableCount_Type())
vcSwitchMemParityErrorNonCorrectableCount.setMaxAccess(_E)
if mibBuilder.loadTexts:vcSwitchMemParityErrorNonCorrectableCount.setStatus(_B)
_VcModuleMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
vcModuleMIBNotificationPrefix=_VcModuleMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,3,2))
_VcModuleMIBNotifications_ObjectIdentity=ObjectIdentity
vcModuleMIBNotifications=_VcModuleMIBNotifications_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,3,2,0))
_VcModuleMIBNotificationObjects_ObjectIdentity=ObjectIdentity
vcModuleMIBNotificationObjects=_VcModuleMIBNotificationObjects_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,3,2,1))
_VcModuleMIBConformance_ObjectIdentity=ObjectIdentity
vcModuleMIBConformance=_VcModuleMIBConformance_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,3,3))
_VcModuleMIBCompliances_ObjectIdentity=ObjectIdentity
vcModuleMIBCompliances=_VcModuleMIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,3,3,1))
_VcModuleMIBGroups_ObjectIdentity=ObjectIdentity
vcModuleMIBGroups=_VcModuleMIBGroups_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,2,3,3,2))
vcModuleGroup=ObjectGroup((1,3,6,1,4,1,11,5,7,5,2,3,3,2,1))
vcModuleGroup.setObjects(*((_A,_K),(_A,_G),(_A,_L),(_A,_M),(_A,_N),(_A,_H)))
if mibBuilder.loadTexts:vcModuleGroup.setStatus(_V)
vcModuleGroup2=ObjectGroup((1,3,6,1,4,1,11,5,7,5,2,3,3,2,4))
vcModuleGroup2.setObjects(*((_A,_K),(_A,_G),(_A,_L),(_A,_M),(_A,_N),(_A,_H),(_A,_O)))
if mibBuilder.loadTexts:vcModuleGroup2.setStatus(_B)
vcModuleDomainRoleChange=NotificationType((1,3,6,1,4,1,11,5,7,5,2,3,2,0,1))
vcModuleDomainRoleChange.setObjects((_A,_G))
if mibBuilder.loadTexts:vcModuleDomainRoleChange.setStatus(_B)
vcSwitchMemParityErrorEvent=NotificationType((1,3,6,1,4,1,11,5,7,5,2,3,2,0,2))
vcSwitchMemParityErrorEvent.setObjects((_A,_H))
if mibBuilder.loadTexts:vcSwitchMemParityErrorEvent.setStatus(_B)
vcSwitchMemParityErrorNonCorrectableEvent=NotificationType((1,3,6,1,4,1,11,5,7,5,2,3,2,0,3))
vcSwitchMemParityErrorNonCorrectableEvent.setObjects(*((_A,_O),(_A,'cpqHoFwVerLocation')))
if mibBuilder.loadTexts:vcSwitchMemParityErrorNonCorrectableEvent.setStatus(_B)
vcModPortInputUtilizationUp=NotificationType((1,3,6,1,4,1,11,5,7,5,2,3,2,0,11))
vcModPortInputUtilizationUp.setObjects((_C,_D))
if mibBuilder.loadTexts:vcModPortInputUtilizationUp.setStatus(_B)
vcModPortInputUtilizationDown=NotificationType((1,3,6,1,4,1,11,5,7,5,2,3,2,0,12))
vcModPortInputUtilizationDown.setObjects((_C,_D))
if mibBuilder.loadTexts:vcModPortInputUtilizationDown.setStatus(_B)
vcModPortOutputUtilizationUp=NotificationType((1,3,6,1,4,1,11,5,7,5,2,3,2,0,13))
vcModPortOutputUtilizationUp.setObjects((_C,_D))
if mibBuilder.loadTexts:vcModPortOutputUtilizationUp.setStatus(_B)
vcModPortOutputUtilizationDown=NotificationType((1,3,6,1,4,1,11,5,7,5,2,3,2,0,14))
vcModPortOutputUtilizationDown.setObjects((_C,_D))
if mibBuilder.loadTexts:vcModPortOutputUtilizationDown.setStatus(_B)
vcModPortInputErrorsUp=NotificationType((1,3,6,1,4,1,11,5,7,5,2,3,2,0,15))
vcModPortInputErrorsUp.setObjects(*((_C,_D),(_C,_I)))
if mibBuilder.loadTexts:vcModPortInputErrorsUp.setStatus(_B)
vcModPortInputErrorsDown=NotificationType((1,3,6,1,4,1,11,5,7,5,2,3,2,0,16))
vcModPortInputErrorsDown.setObjects(*((_C,_D),(_C,_I)))
if mibBuilder.loadTexts:vcModPortInputErrorsDown.setStatus(_B)
vcModPortOutputErrorsUp=NotificationType((1,3,6,1,4,1,11,5,7,5,2,3,2,0,17))
vcModPortOutputErrorsUp.setObjects(*((_C,_D),(_C,_J)))
if mibBuilder.loadTexts:vcModPortOutputErrorsUp.setStatus(_B)
vcModPortOutputErrorsDown=NotificationType((1,3,6,1,4,1,11,5,7,5,2,3,2,0,18))
vcModPortOutputErrorsDown.setObjects(*((_C,_D),(_C,_J)))
if mibBuilder.loadTexts:vcModPortOutputErrorsDown.setStatus(_B)
vcModPortBpduLoopDetected=NotificationType((1,3,6,1,4,1,11,5,7,5,2,3,2,0,19))
vcModPortBpduLoopDetected.setObjects(*((_C,_D),(_A,_F),(_A,_P)))
if mibBuilder.loadTexts:vcModPortBpduLoopDetected.setStatus(_B)
vcModPortBpduLoopCleared=NotificationType((1,3,6,1,4,1,11,5,7,5,2,3,2,0,20))
vcModPortBpduLoopCleared.setObjects(*((_C,_D),(_A,_F),(_A,_P)))
if mibBuilder.loadTexts:vcModPortBpduLoopCleared.setStatus(_B)
vcModPortProtectionConditionDetected=NotificationType((1,3,6,1,4,1,11,5,7,5,2,3,2,0,21))
vcModPortProtectionConditionDetected.setObjects(*((_C,_D),(_A,_F),(_A,_Q)))
if mibBuilder.loadTexts:vcModPortProtectionConditionDetected.setStatus(_B)
vcModPortProtectionConditionCleared=NotificationType((1,3,6,1,4,1,11,5,7,5,2,3,2,0,22))
vcModPortProtectionConditionCleared.setObjects(*((_C,_D),(_A,_F),(_A,_Q)))
if mibBuilder.loadTexts:vcModPortProtectionConditionCleared.setStatus(_B)
vcModPortThresholdNotificationsGroup=NotificationGroup((1,3,6,1,4,1,11,5,7,5,2,3,3,2,2))
vcModPortThresholdNotificationsGroup.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:vcModPortThresholdNotificationsGroup.setStatus(_B)
vcModPortStatusNotificationsGroup=NotificationGroup((1,3,6,1,4,1,11,5,7,5,2,3,3,2,3))
vcModPortStatusNotificationsGroup.setObjects(*((_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:vcModPortStatusNotificationsGroup.setStatus(_B)
vcModuleMIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,5,7,5,2,3,3,1,1))
vcModuleMIBCompliance.setObjects(*((_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:vcModuleMIBCompliance.setStatus(_V)
vcModuleMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,11,5,7,5,2,3,3,1,2))
vcModuleMIBCompliance2.setObjects(*((_A,_R),(_A,_S),(_A,_T),(_A,_i)))
if mibBuilder.loadTexts:vcModuleMIBCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'VcModuleRole':VcModuleRole,'VcEnclosureRole':VcEnclosureRole,'VcModuleType':VcModuleType,'VcModulePortBpduLoopStatus':VcModulePortBpduLoopStatus,'VcModulePortProtectionStatus':VcModulePortProtectionStatus,'hp':hp,'hpSysMgt':hpSysMgt,'hpEmbeddedServerMgt':hpEmbeddedServerMgt,'hpModuleMgmtProc':hpModuleMgmtProc,'virtualConnect':virtualConnect,'vcModuleMIB':vcModuleMIB,'vcModuleMIBObjects':vcModuleMIBObjects,'vcModuleObjects':vcModuleObjects,_K:vcModuleDomainName,_G:vcModuleRole,_L:vcModuleDomainPrimaryAddressType,_M:vcModuleDomainPrimaryAddress,'vcModuleEnclosureRole':vcModuleEnclosureRole,'vcModulePortTable':vcModulePortTable,'vcModulePortEntry':vcModulePortEntry,_F:vcModulePort,'vcModulePortIfIndex':vcModulePortIfIndex,_P:vcModulePortBpduLoopStatus,_Q:vcModulePortProtectionStatus,_N:vcModuleDomainPrimaryAddressIpv6,_H:vcSwitchMemParityErrorCount,_O:vcSwitchMemParityErrorNonCorrectableCount,'vcModuleMIBNotificationPrefix':vcModuleMIBNotificationPrefix,'vcModuleMIBNotifications':vcModuleMIBNotifications,'vcModuleDomainRoleChange':vcModuleDomainRoleChange,'vcSwitchMemParityErrorEvent':vcSwitchMemParityErrorEvent,'vcSwitchMemParityErrorNonCorrectableEvent':vcSwitchMemParityErrorNonCorrectableEvent,_W:vcModPortInputUtilizationUp,_X:vcModPortInputUtilizationDown,_Y:vcModPortOutputUtilizationUp,_Z:vcModPortOutputUtilizationDown,_a:vcModPortInputErrorsUp,_b:vcModPortInputErrorsDown,_c:vcModPortOutputErrorsUp,_d:vcModPortOutputErrorsDown,_e:vcModPortBpduLoopDetected,_f:vcModPortBpduLoopCleared,_g:vcModPortProtectionConditionDetected,_h:vcModPortProtectionConditionCleared,'vcModuleMIBNotificationObjects':vcModuleMIBNotificationObjects,'vcModuleMIBConformance':vcModuleMIBConformance,'vcModuleMIBCompliances':vcModuleMIBCompliances,'vcModuleMIBCompliance':vcModuleMIBCompliance,'vcModuleMIBCompliance2':vcModuleMIBCompliance2,'vcModuleMIBGroups':vcModuleMIBGroups,_R:vcModuleGroup,_S:vcModPortThresholdNotificationsGroup,_T:vcModPortStatusNotificationsGroup,_i:vcModuleGroup2})