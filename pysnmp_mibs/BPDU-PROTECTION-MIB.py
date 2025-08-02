_L='swBpduProtectionRecoveryMethod'
_K='swBpduProtectionPortMode'
_J='read-only'
_I='attackCleared'
_H='attackDetected'
_G='disabled'
_F='enabled'
_E='swBpduProtectionPortIndex'
_D='BPDU-PROTECTION-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
swBpduProtectionMIB=ModuleIdentity((1,3,6,1,4,1,171,12,76))
_SwBpduProtectionCtrl_ObjectIdentity=ObjectIdentity
swBpduProtectionCtrl=_SwBpduProtectionCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,76,1))
class _SwBpduProtectionAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwBpduProtectionAdminState_Type.__name__=_B
_SwBpduProtectionAdminState_Object=MibScalar
swBpduProtectionAdminState=_SwBpduProtectionAdminState_Object((1,3,6,1,4,1,171,12,76,1,1),_SwBpduProtectionAdminState_Type())
swBpduProtectionAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:swBpduProtectionAdminState.setStatus(_A)
class _SwBpduProtectionRecoveryTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(60,1000000))
_SwBpduProtectionRecoveryTime_Type.__name__=_B
_SwBpduProtectionRecoveryTime_Object=MibScalar
swBpduProtectionRecoveryTime=_SwBpduProtectionRecoveryTime_Object((1,3,6,1,4,1,171,12,76,1,2),_SwBpduProtectionRecoveryTime_Type())
swBpduProtectionRecoveryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swBpduProtectionRecoveryTime.setStatus(_A)
class _SwBpduProtectionTrapMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),(_H,2),(_I,3),('both',4)))
_SwBpduProtectionTrapMode_Type.__name__=_B
_SwBpduProtectionTrapMode_Object=MibScalar
swBpduProtectionTrapMode=_SwBpduProtectionTrapMode_Object((1,3,6,1,4,1,171,12,76,1,3),_SwBpduProtectionTrapMode_Type())
swBpduProtectionTrapMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swBpduProtectionTrapMode.setStatus(_A)
class _SwBpduProtectionLogMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),(_H,2),(_I,3),('both',4)))
_SwBpduProtectionLogMode_Type.__name__=_B
_SwBpduProtectionLogMode_Object=MibScalar
swBpduProtectionLogMode=_SwBpduProtectionLogMode_Object((1,3,6,1,4,1,171,12,76,1,4),_SwBpduProtectionLogMode_Type())
swBpduProtectionLogMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swBpduProtectionLogMode.setStatus(_A)
_SwBpduProtectionInfo_ObjectIdentity=ObjectIdentity
swBpduProtectionInfo=_SwBpduProtectionInfo_ObjectIdentity((1,3,6,1,4,1,171,12,76,2))
_SwBpduProtectionMgmt_ObjectIdentity=ObjectIdentity
swBpduProtectionMgmt=_SwBpduProtectionMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,76,3))
_SwBpduProtectionPortTable_Object=MibTable
swBpduProtectionPortTable=_SwBpduProtectionPortTable_Object((1,3,6,1,4,1,171,12,76,3,1))
if mibBuilder.loadTexts:swBpduProtectionPortTable.setStatus(_A)
_SwBpduProtectionPortEntry_Object=MibTableRow
swBpduProtectionPortEntry=_SwBpduProtectionPortEntry_Object((1,3,6,1,4,1,171,12,76,3,1,1))
swBpduProtectionPortEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:swBpduProtectionPortEntry.setStatus(_A)
class _SwBpduProtectionPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwBpduProtectionPortIndex_Type.__name__=_B
_SwBpduProtectionPortIndex_Object=MibTableColumn
swBpduProtectionPortIndex=_SwBpduProtectionPortIndex_Object((1,3,6,1,4,1,171,12,76,3,1,1,1),_SwBpduProtectionPortIndex_Type())
swBpduProtectionPortIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:swBpduProtectionPortIndex.setStatus(_A)
class _SwBpduProtectionPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwBpduProtectionPortState_Type.__name__=_B
_SwBpduProtectionPortState_Object=MibTableColumn
swBpduProtectionPortState=_SwBpduProtectionPortState_Object((1,3,6,1,4,1,171,12,76,3,1,1,2),_SwBpduProtectionPortState_Type())
swBpduProtectionPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:swBpduProtectionPortState.setStatus(_A)
class _SwBpduProtectionPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('drop',1),('block',2),('shutdown',3)))
_SwBpduProtectionPortMode_Type.__name__=_B
_SwBpduProtectionPortMode_Object=MibTableColumn
swBpduProtectionPortMode=_SwBpduProtectionPortMode_Object((1,3,6,1,4,1,171,12,76,3,1,1,3),_SwBpduProtectionPortMode_Type())
swBpduProtectionPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swBpduProtectionPortMode.setStatus(_A)
class _SwBpduProtectionPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('underAttack',2)))
_SwBpduProtectionPortStatus_Type.__name__=_B
_SwBpduProtectionPortStatus_Object=MibTableColumn
swBpduProtectionPortStatus=_SwBpduProtectionPortStatus_Object((1,3,6,1,4,1,171,12,76,3,1,1,4),_SwBpduProtectionPortStatus_Type())
swBpduProtectionPortStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:swBpduProtectionPortStatus.setStatus(_A)
_SwBpduProtectionNotify_ObjectIdentity=ObjectIdentity
swBpduProtectionNotify=_SwBpduProtectionNotify_ObjectIdentity((1,3,6,1,4,1,171,12,76,4))
_SwBpduProtectionNotifyPrefix_ObjectIdentity=ObjectIdentity
swBpduProtectionNotifyPrefix=_SwBpduProtectionNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,171,12,76,4,0))
_SwBpduProtectionNotificationBidings_ObjectIdentity=ObjectIdentity
swBpduProtectionNotificationBidings=_SwBpduProtectionNotificationBidings_ObjectIdentity((1,3,6,1,4,1,171,12,76,4,2))
class _SwBpduProtectionRecoveryMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('automatically',1),('manually',2)))
_SwBpduProtectionRecoveryMethod_Type.__name__=_B
_SwBpduProtectionRecoveryMethod_Object=MibScalar
swBpduProtectionRecoveryMethod=_SwBpduProtectionRecoveryMethod_Object((1,3,6,1,4,1,171,12,76,4,2,1),_SwBpduProtectionRecoveryMethod_Type())
swBpduProtectionRecoveryMethod.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:swBpduProtectionRecoveryMethod.setStatus(_A)
swBpduProtectionUnderAttackingTrap=NotificationType((1,3,6,1,4,1,171,12,76,4,0,1))
swBpduProtectionUnderAttackingTrap.setObjects(*((_D,_E),(_D,_K)))
if mibBuilder.loadTexts:swBpduProtectionUnderAttackingTrap.setStatus(_A)
swBpduProtectionRecoveryTrap=NotificationType((1,3,6,1,4,1,171,12,76,4,0,2))
swBpduProtectionRecoveryTrap.setObjects(*((_D,_E),(_D,_L)))
if mibBuilder.loadTexts:swBpduProtectionRecoveryTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'swBpduProtectionMIB':swBpduProtectionMIB,'swBpduProtectionCtrl':swBpduProtectionCtrl,'swBpduProtectionAdminState':swBpduProtectionAdminState,'swBpduProtectionRecoveryTime':swBpduProtectionRecoveryTime,'swBpduProtectionTrapMode':swBpduProtectionTrapMode,'swBpduProtectionLogMode':swBpduProtectionLogMode,'swBpduProtectionInfo':swBpduProtectionInfo,'swBpduProtectionMgmt':swBpduProtectionMgmt,'swBpduProtectionPortTable':swBpduProtectionPortTable,'swBpduProtectionPortEntry':swBpduProtectionPortEntry,_E:swBpduProtectionPortIndex,'swBpduProtectionPortState':swBpduProtectionPortState,_K:swBpduProtectionPortMode,'swBpduProtectionPortStatus':swBpduProtectionPortStatus,'swBpduProtectionNotify':swBpduProtectionNotify,'swBpduProtectionNotifyPrefix':swBpduProtectionNotifyPrefix,'swBpduProtectionUnderAttackingTrap':swBpduProtectionUnderAttackingTrap,'swBpduProtectionRecoveryTrap':swBpduProtectionRecoveryTrap,'swBpduProtectionNotificationBidings':swBpduProtectionNotificationBidings,_L:swBpduProtectionRecoveryMethod})