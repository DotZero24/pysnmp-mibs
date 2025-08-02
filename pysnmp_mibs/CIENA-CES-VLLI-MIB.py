_N='cienaCesVlliActionGroupId'
_M='cienaCesVlliInstanceGroupId'
_L='cienaCesVlliInstanceName'
_K='cienaCesVlliInstanceGroupName'
_J='accessible-for-notify'
_I='cienaGlobalSeverity'
_H='cienaGlobalMacAddress'
_G='cienaCesVlliInstanceId'
_F='cienaCesVlliInstanceGrpId'
_E='CIENA-GLOBAL-MIB'
_D='Integer32'
_C='CIENA-CES-VLLI-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaGlobalMacAddress,cienaGlobalSeverity=mibBuilder.importSymbols(_E,_H,_I)
cienaCesConfig,cienaCesNotifications=mibBuilder.importSymbols('CIENA-SMI','cienaCesConfig','cienaCesNotifications')
CienaGlobalState,=mibBuilder.importSymbols('CIENA-TC','CienaGlobalState')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cienaCesVlliMIB=ModuleIdentity((1,3,6,1,4,1,1271,2,1,23))
if mibBuilder.loadTexts:cienaCesVlliMIB.setRevisions(('2017-06-07 00:00','2012-02-28 00:00'))
class VlliAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('portShut',1),('portUnshut',2),('ccmStop',3),('ccmResume',4)))
class VlliLastEvent(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unknown',1),('fault',2),('recovery',3),('adminFault',4),('adminRecovery',5)))
_CienaCesVlliMIBObjects_ObjectIdentity=ObjectIdentity
cienaCesVlliMIBObjects=_CienaCesVlliMIBObjects_ObjectIdentity((1,3,6,1,4,1,1271,2,1,23,1))
_CienaCesVlli_ObjectIdentity=ObjectIdentity
cienaCesVlli=_CienaCesVlli_ObjectIdentity((1,3,6,1,4,1,1271,2,1,23,1,1))
_CienaCesVlliAdminState_Type=CienaGlobalState
_CienaCesVlliAdminState_Object=MibScalar
cienaCesVlliAdminState=_CienaCesVlliAdminState_Object((1,3,6,1,4,1,1271,2,1,23,1,1,1),_CienaCesVlliAdminState_Type())
cienaCesVlliAdminState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliAdminState.setStatus(_A)
_CienaCesVlliInstanceGroupTable_Object=MibTable
cienaCesVlliInstanceGroupTable=_CienaCesVlliInstanceGroupTable_Object((1,3,6,1,4,1,1271,2,1,23,1,1,2))
if mibBuilder.loadTexts:cienaCesVlliInstanceGroupTable.setStatus(_A)
_CienaCesVlliInstanceGroupEntry_Object=MibTableRow
cienaCesVlliInstanceGroupEntry=_CienaCesVlliInstanceGroupEntry_Object((1,3,6,1,4,1,1271,2,1,23,1,1,2,1))
cienaCesVlliInstanceGroupEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:cienaCesVlliInstanceGroupEntry.setStatus(_A)
class _CienaCesVlliInstanceGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_CienaCesVlliInstanceGroupId_Type.__name__=_D
_CienaCesVlliInstanceGroupId_Object=MibTableColumn
cienaCesVlliInstanceGroupId=_CienaCesVlliInstanceGroupId_Object((1,3,6,1,4,1,1271,2,1,23,1,1,2,1,1),_CienaCesVlliInstanceGroupId_Type())
cienaCesVlliInstanceGroupId.setMaxAccess(_J)
if mibBuilder.loadTexts:cienaCesVlliInstanceGroupId.setStatus(_A)
_CienaCesVlliInstanceGroupName_Type=DisplayString
_CienaCesVlliInstanceGroupName_Object=MibTableColumn
cienaCesVlliInstanceGroupName=_CienaCesVlliInstanceGroupName_Object((1,3,6,1,4,1,1271,2,1,23,1,1,2,1,2),_CienaCesVlliInstanceGroupName_Type())
cienaCesVlliInstanceGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliInstanceGroupName.setStatus(_A)
class _CienaCesVlliInstanceGroupDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unidirectional',1),('bidirectional',2)))
_CienaCesVlliInstanceGroupDirection_Type.__name__=_D
_CienaCesVlliInstanceGroupDirection_Object=MibTableColumn
cienaCesVlliInstanceGroupDirection=_CienaCesVlliInstanceGroupDirection_Object((1,3,6,1,4,1,1271,2,1,23,1,1,2,1,3),_CienaCesVlliInstanceGroupDirection_Type())
cienaCesVlliInstanceGroupDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliInstanceGroupDirection.setStatus(_A)
class _CienaCesVlliInstanceGroupTrigger_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('any',1),('all',2)))
_CienaCesVlliInstanceGroupTrigger_Type.__name__=_D
_CienaCesVlliInstanceGroupTrigger_Object=MibTableColumn
cienaCesVlliInstanceGroupTrigger=_CienaCesVlliInstanceGroupTrigger_Object((1,3,6,1,4,1,1271,2,1,23,1,1,2,1,4),_CienaCesVlliInstanceGroupTrigger_Type())
cienaCesVlliInstanceGroupTrigger.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliInstanceGroupTrigger.setStatus(_A)
_CienaCesVlliInstanceGroupState_Type=CienaGlobalState
_CienaCesVlliInstanceGroupState_Object=MibTableColumn
cienaCesVlliInstanceGroupState=_CienaCesVlliInstanceGroupState_Object((1,3,6,1,4,1,1271,2,1,23,1,1,2,1,5),_CienaCesVlliInstanceGroupState_Type())
cienaCesVlliInstanceGroupState.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliInstanceGroupState.setStatus(_A)
_CienaCesVlliActionGroupTable_Object=MibTable
cienaCesVlliActionGroupTable=_CienaCesVlliActionGroupTable_Object((1,3,6,1,4,1,1271,2,1,23,1,1,3))
if mibBuilder.loadTexts:cienaCesVlliActionGroupTable.setStatus(_A)
_CienaCesVlliActionGroupEntry_Object=MibTableRow
cienaCesVlliActionGroupEntry=_CienaCesVlliActionGroupEntry_Object((1,3,6,1,4,1,1271,2,1,23,1,1,3,1))
cienaCesVlliActionGroupEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:cienaCesVlliActionGroupEntry.setStatus(_A)
class _CienaCesVlliActionGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_CienaCesVlliActionGroupId_Type.__name__=_D
_CienaCesVlliActionGroupId_Object=MibTableColumn
cienaCesVlliActionGroupId=_CienaCesVlliActionGroupId_Object((1,3,6,1,4,1,1271,2,1,23,1,1,3,1,1),_CienaCesVlliActionGroupId_Type())
cienaCesVlliActionGroupId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cienaCesVlliActionGroupId.setStatus(_A)
_CienaCesVlliActionGroupName_Type=DisplayString
_CienaCesVlliActionGroupName_Object=MibTableColumn
cienaCesVlliActionGroupName=_CienaCesVlliActionGroupName_Object((1,3,6,1,4,1,1271,2,1,23,1,1,3,1,2),_CienaCesVlliActionGroupName_Type())
cienaCesVlliActionGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliActionGroupName.setStatus(_A)
_CienaCesVlliActRecoveryPreceOne_Type=VlliAction
_CienaCesVlliActRecoveryPreceOne_Object=MibTableColumn
cienaCesVlliActRecoveryPreceOne=_CienaCesVlliActRecoveryPreceOne_Object((1,3,6,1,4,1,1271,2,1,23,1,1,3,1,3),_CienaCesVlliActRecoveryPreceOne_Type())
cienaCesVlliActRecoveryPreceOne.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliActRecoveryPreceOne.setStatus(_A)
_CienaCesVlliActRecoveryPreceTwo_Type=VlliAction
_CienaCesVlliActRecoveryPreceTwo_Object=MibTableColumn
cienaCesVlliActRecoveryPreceTwo=_CienaCesVlliActRecoveryPreceTwo_Object((1,3,6,1,4,1,1271,2,1,23,1,1,3,1,4),_CienaCesVlliActRecoveryPreceTwo_Type())
cienaCesVlliActRecoveryPreceTwo.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliActRecoveryPreceTwo.setStatus(_A)
_CienaCesVlliActRecoveryPreceThree_Type=VlliAction
_CienaCesVlliActRecoveryPreceThree_Object=MibTableColumn
cienaCesVlliActRecoveryPreceThree=_CienaCesVlliActRecoveryPreceThree_Object((1,3,6,1,4,1,1271,2,1,23,1,1,3,1,5),_CienaCesVlliActRecoveryPreceThree_Type())
cienaCesVlliActRecoveryPreceThree.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliActRecoveryPreceThree.setStatus(_A)
_CienaCesVlliActRecoveryPreceFour_Type=VlliAction
_CienaCesVlliActRecoveryPreceFour_Object=MibTableColumn
cienaCesVlliActRecoveryPreceFour=_CienaCesVlliActRecoveryPreceFour_Object((1,3,6,1,4,1,1271,2,1,23,1,1,3,1,6),_CienaCesVlliActRecoveryPreceFour_Type())
cienaCesVlliActRecoveryPreceFour.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliActRecoveryPreceFour.setStatus(_A)
_CienaCesVlliActRecoveryPreceFive_Type=VlliAction
_CienaCesVlliActRecoveryPreceFive_Object=MibTableColumn
cienaCesVlliActRecoveryPreceFive=_CienaCesVlliActRecoveryPreceFive_Object((1,3,6,1,4,1,1271,2,1,23,1,1,3,1,7),_CienaCesVlliActRecoveryPreceFive_Type())
cienaCesVlliActRecoveryPreceFive.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliActRecoveryPreceFive.setStatus(_A)
_CienaCesVlliActRecoveryPreceSix_Type=VlliAction
_CienaCesVlliActRecoveryPreceSix_Object=MibTableColumn
cienaCesVlliActRecoveryPreceSix=_CienaCesVlliActRecoveryPreceSix_Object((1,3,6,1,4,1,1271,2,1,23,1,1,3,1,8),_CienaCesVlliActRecoveryPreceSix_Type())
cienaCesVlliActRecoveryPreceSix.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliActRecoveryPreceSix.setStatus(_A)
_CienaCesVlliActRecoveryPreceSeven_Type=VlliAction
_CienaCesVlliActRecoveryPreceSeven_Object=MibTableColumn
cienaCesVlliActRecoveryPreceSeven=_CienaCesVlliActRecoveryPreceSeven_Object((1,3,6,1,4,1,1271,2,1,23,1,1,3,1,9),_CienaCesVlliActRecoveryPreceSeven_Type())
cienaCesVlliActRecoveryPreceSeven.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliActRecoveryPreceSeven.setStatus(_A)
_CienaCesVlliActRecoveryPreceEight_Type=VlliAction
_CienaCesVlliActRecoveryPreceEight_Object=MibTableColumn
cienaCesVlliActRecoveryPreceEight=_CienaCesVlliActRecoveryPreceEight_Object((1,3,6,1,4,1,1271,2,1,23,1,1,3,1,10),_CienaCesVlliActRecoveryPreceEight_Type())
cienaCesVlliActRecoveryPreceEight.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliActRecoveryPreceEight.setStatus(_A)
_CienaCesVlliActFaultPreceOne_Type=VlliAction
_CienaCesVlliActFaultPreceOne_Object=MibTableColumn
cienaCesVlliActFaultPreceOne=_CienaCesVlliActFaultPreceOne_Object((1,3,6,1,4,1,1271,2,1,23,1,1,3,1,11),_CienaCesVlliActFaultPreceOne_Type())
cienaCesVlliActFaultPreceOne.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliActFaultPreceOne.setStatus(_A)
_CienaCesVlliActFaultPreceTwo_Type=VlliAction
_CienaCesVlliActFaultPreceTwo_Object=MibTableColumn
cienaCesVlliActFaultPreceTwo=_CienaCesVlliActFaultPreceTwo_Object((1,3,6,1,4,1,1271,2,1,23,1,1,3,1,12),_CienaCesVlliActFaultPreceTwo_Type())
cienaCesVlliActFaultPreceTwo.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliActFaultPreceTwo.setStatus(_A)
_CienaCesVlliActFaultPreceThree_Type=VlliAction
_CienaCesVlliActFaultPreceThree_Object=MibTableColumn
cienaCesVlliActFaultPreceThree=_CienaCesVlliActFaultPreceThree_Object((1,3,6,1,4,1,1271,2,1,23,1,1,3,1,13),_CienaCesVlliActFaultPreceThree_Type())
cienaCesVlliActFaultPreceThree.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliActFaultPreceThree.setStatus(_A)
_CienaCesVlliActFaultPreceFour_Type=VlliAction
_CienaCesVlliActFaultPreceFour_Object=MibTableColumn
cienaCesVlliActFaultPreceFour=_CienaCesVlliActFaultPreceFour_Object((1,3,6,1,4,1,1271,2,1,23,1,1,3,1,14),_CienaCesVlliActFaultPreceFour_Type())
cienaCesVlliActFaultPreceFour.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliActFaultPreceFour.setStatus(_A)
_CienaCesVlliActFaultPreceFive_Type=VlliAction
_CienaCesVlliActFaultPreceFive_Object=MibTableColumn
cienaCesVlliActFaultPreceFive=_CienaCesVlliActFaultPreceFive_Object((1,3,6,1,4,1,1271,2,1,23,1,1,3,1,15),_CienaCesVlliActFaultPreceFive_Type())
cienaCesVlliActFaultPreceFive.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliActFaultPreceFive.setStatus(_A)
_CienaCesVlliActFaultPreceSix_Type=VlliAction
_CienaCesVlliActFaultPreceSix_Object=MibTableColumn
cienaCesVlliActFaultPreceSix=_CienaCesVlliActFaultPreceSix_Object((1,3,6,1,4,1,1271,2,1,23,1,1,3,1,16),_CienaCesVlliActFaultPreceSix_Type())
cienaCesVlliActFaultPreceSix.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliActFaultPreceSix.setStatus(_A)
_CienaCesVlliActFaultPreceSeven_Type=VlliAction
_CienaCesVlliActFaultPreceSeven_Object=MibTableColumn
cienaCesVlliActFaultPreceSeven=_CienaCesVlliActFaultPreceSeven_Object((1,3,6,1,4,1,1271,2,1,23,1,1,3,1,17),_CienaCesVlliActFaultPreceSeven_Type())
cienaCesVlliActFaultPreceSeven.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliActFaultPreceSeven.setStatus(_A)
_CienaCesVlliActFaultPreceEight_Type=VlliAction
_CienaCesVlliActFaultPreceEight_Object=MibTableColumn
cienaCesVlliActFaultPreceEight=_CienaCesVlliActFaultPreceEight_Object((1,3,6,1,4,1,1271,2,1,23,1,1,3,1,18),_CienaCesVlliActFaultPreceEight_Type())
cienaCesVlliActFaultPreceEight.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliActFaultPreceEight.setStatus(_A)
_CienaCesVlliInstanceTable_Object=MibTable
cienaCesVlliInstanceTable=_CienaCesVlliInstanceTable_Object((1,3,6,1,4,1,1271,2,1,23,1,1,4))
if mibBuilder.loadTexts:cienaCesVlliInstanceTable.setStatus(_A)
_CienaCesVlliInstanceEntry_Object=MibTableRow
cienaCesVlliInstanceEntry=_CienaCesVlliInstanceEntry_Object((1,3,6,1,4,1,1271,2,1,23,1,1,4,1))
cienaCesVlliInstanceEntry.setIndexNames((0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:cienaCesVlliInstanceEntry.setStatus(_A)
class _CienaCesVlliInstanceGrpId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_CienaCesVlliInstanceGrpId_Type.__name__=_D
_CienaCesVlliInstanceGrpId_Object=MibTableColumn
cienaCesVlliInstanceGrpId=_CienaCesVlliInstanceGrpId_Object((1,3,6,1,4,1,1271,2,1,23,1,1,4,1,1),_CienaCesVlliInstanceGrpId_Type())
cienaCesVlliInstanceGrpId.setMaxAccess(_J)
if mibBuilder.loadTexts:cienaCesVlliInstanceGrpId.setStatus(_A)
class _CienaCesVlliInstanceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_CienaCesVlliInstanceId_Type.__name__=_D
_CienaCesVlliInstanceId_Object=MibTableColumn
cienaCesVlliInstanceId=_CienaCesVlliInstanceId_Object((1,3,6,1,4,1,1271,2,1,23,1,1,4,1,2),_CienaCesVlliInstanceId_Type())
cienaCesVlliInstanceId.setMaxAccess(_J)
if mibBuilder.loadTexts:cienaCesVlliInstanceId.setStatus(_A)
class _CienaCesVlliInstanceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('destination',1),('source',2)))
_CienaCesVlliInstanceMode_Type.__name__=_D
_CienaCesVlliInstanceMode_Object=MibTableColumn
cienaCesVlliInstanceMode=_CienaCesVlliInstanceMode_Object((1,3,6,1,4,1,1271,2,1,23,1,1,4,1,3),_CienaCesVlliInstanceMode_Type())
cienaCesVlliInstanceMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliInstanceMode.setStatus(_A)
class _CienaCesVlliInstanceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('port',1),('cfm',2)))
_CienaCesVlliInstanceType_Type.__name__=_D
_CienaCesVlliInstanceType_Object=MibTableColumn
cienaCesVlliInstanceType=_CienaCesVlliInstanceType_Object((1,3,6,1,4,1,1271,2,1,23,1,1,4,1,4),_CienaCesVlliInstanceType_Type())
cienaCesVlliInstanceType.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliInstanceType.setStatus(_A)
_CienaCesVlliInstanceName_Type=DisplayString
_CienaCesVlliInstanceName_Object=MibTableColumn
cienaCesVlliInstanceName=_CienaCesVlliInstanceName_Object((1,3,6,1,4,1,1271,2,1,23,1,1,4,1,5),_CienaCesVlliInstanceName_Type())
cienaCesVlliInstanceName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliInstanceName.setStatus(_A)
_CienaCesVlliInstanceActionName_Type=DisplayString
_CienaCesVlliInstanceActionName_Object=MibTableColumn
cienaCesVlliInstanceActionName=_CienaCesVlliInstanceActionName_Object((1,3,6,1,4,1,1271,2,1,23,1,1,4,1,6),_CienaCesVlliInstanceActionName_Type())
cienaCesVlliInstanceActionName.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliInstanceActionName.setStatus(_A)
_CienaCesVlliInstanceLastEvent_Type=VlliLastEvent
_CienaCesVlliInstanceLastEvent_Object=MibTableColumn
cienaCesVlliInstanceLastEvent=_CienaCesVlliInstanceLastEvent_Object((1,3,6,1,4,1,1271,2,1,23,1,1,4,1,7),_CienaCesVlliInstanceLastEvent_Type())
cienaCesVlliInstanceLastEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:cienaCesVlliInstanceLastEvent.setStatus(_A)
_CienaCesVlliMIBConformance_ObjectIdentity=ObjectIdentity
cienaCesVlliMIBConformance=_CienaCesVlliMIBConformance_ObjectIdentity((1,3,6,1,4,1,1271,2,1,23,3))
_CienaCesVlliMIBCompliances_ObjectIdentity=ObjectIdentity
cienaCesVlliMIBCompliances=_CienaCesVlliMIBCompliances_ObjectIdentity((1,3,6,1,4,1,1271,2,1,23,3,1))
_CienaCesVlliMIBGroups_ObjectIdentity=ObjectIdentity
cienaCesVlliMIBGroups=_CienaCesVlliMIBGroups_ObjectIdentity((1,3,6,1,4,1,1271,2,1,23,3,2))
_CienaCesVlliNotificationPrefix_ObjectIdentity=ObjectIdentity
cienaCesVlliNotificationPrefix=_CienaCesVlliNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,1271,2,2,99))
_CienaCesVlliNotifications_ObjectIdentity=ObjectIdentity
cienaCesVlliNotifications=_CienaCesVlliNotifications_ObjectIdentity((1,3,6,1,4,1,1271,2,2,99,0))
cienaCesVlliFaultTrap=NotificationType((1,3,6,1,4,1,1271,2,2,99,0,1))
cienaCesVlliFaultTrap.setObjects(*((_E,_I),(_E,_H),(_C,_F),(_C,_G),(_C,_K),(_C,_L)))
if mibBuilder.loadTexts:cienaCesVlliFaultTrap.setStatus(_A)
cienaCesVlliRecoveryTrap=NotificationType((1,3,6,1,4,1,1271,2,2,99,0,2))
cienaCesVlliRecoveryTrap.setObjects(*((_E,_I),(_E,_H),(_C,_F),(_C,_G),(_C,_K),(_C,_L)))
if mibBuilder.loadTexts:cienaCesVlliRecoveryTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'VlliAction':VlliAction,'VlliLastEvent':VlliLastEvent,'cienaCesVlliMIB':cienaCesVlliMIB,'cienaCesVlliMIBObjects':cienaCesVlliMIBObjects,'cienaCesVlli':cienaCesVlli,'cienaCesVlliAdminState':cienaCesVlliAdminState,'cienaCesVlliInstanceGroupTable':cienaCesVlliInstanceGroupTable,'cienaCesVlliInstanceGroupEntry':cienaCesVlliInstanceGroupEntry,_M:cienaCesVlliInstanceGroupId,_K:cienaCesVlliInstanceGroupName,'cienaCesVlliInstanceGroupDirection':cienaCesVlliInstanceGroupDirection,'cienaCesVlliInstanceGroupTrigger':cienaCesVlliInstanceGroupTrigger,'cienaCesVlliInstanceGroupState':cienaCesVlliInstanceGroupState,'cienaCesVlliActionGroupTable':cienaCesVlliActionGroupTable,'cienaCesVlliActionGroupEntry':cienaCesVlliActionGroupEntry,_N:cienaCesVlliActionGroupId,'cienaCesVlliActionGroupName':cienaCesVlliActionGroupName,'cienaCesVlliActRecoveryPreceOne':cienaCesVlliActRecoveryPreceOne,'cienaCesVlliActRecoveryPreceTwo':cienaCesVlliActRecoveryPreceTwo,'cienaCesVlliActRecoveryPreceThree':cienaCesVlliActRecoveryPreceThree,'cienaCesVlliActRecoveryPreceFour':cienaCesVlliActRecoveryPreceFour,'cienaCesVlliActRecoveryPreceFive':cienaCesVlliActRecoveryPreceFive,'cienaCesVlliActRecoveryPreceSix':cienaCesVlliActRecoveryPreceSix,'cienaCesVlliActRecoveryPreceSeven':cienaCesVlliActRecoveryPreceSeven,'cienaCesVlliActRecoveryPreceEight':cienaCesVlliActRecoveryPreceEight,'cienaCesVlliActFaultPreceOne':cienaCesVlliActFaultPreceOne,'cienaCesVlliActFaultPreceTwo':cienaCesVlliActFaultPreceTwo,'cienaCesVlliActFaultPreceThree':cienaCesVlliActFaultPreceThree,'cienaCesVlliActFaultPreceFour':cienaCesVlliActFaultPreceFour,'cienaCesVlliActFaultPreceFive':cienaCesVlliActFaultPreceFive,'cienaCesVlliActFaultPreceSix':cienaCesVlliActFaultPreceSix,'cienaCesVlliActFaultPreceSeven':cienaCesVlliActFaultPreceSeven,'cienaCesVlliActFaultPreceEight':cienaCesVlliActFaultPreceEight,'cienaCesVlliInstanceTable':cienaCesVlliInstanceTable,'cienaCesVlliInstanceEntry':cienaCesVlliInstanceEntry,_F:cienaCesVlliInstanceGrpId,_G:cienaCesVlliInstanceId,'cienaCesVlliInstanceMode':cienaCesVlliInstanceMode,'cienaCesVlliInstanceType':cienaCesVlliInstanceType,_L:cienaCesVlliInstanceName,'cienaCesVlliInstanceActionName':cienaCesVlliInstanceActionName,'cienaCesVlliInstanceLastEvent':cienaCesVlliInstanceLastEvent,'cienaCesVlliMIBConformance':cienaCesVlliMIBConformance,'cienaCesVlliMIBCompliances':cienaCesVlliMIBCompliances,'cienaCesVlliMIBGroups':cienaCesVlliMIBGroups,'cienaCesVlliNotificationPrefix':cienaCesVlliNotificationPrefix,'cienaCesVlliNotifications':cienaCesVlliNotifications,'cienaCesVlliFaultTrap':cienaCesVlliFaultTrap,'cienaCesVlliRecoveryTrap':cienaCesVlliRecoveryTrap})