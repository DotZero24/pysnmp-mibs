_g='hmPortSecAllowedGroupIDs'
_f='hmPortSecAllowedUserIPID'
_e='hmPortSecAllowedUserID'
_d='hmPortSecAction'
_c='hmPortSecPermission'
_b='hmPortSecMAExtendedIndex'
_a='hmPortSecMAPortID'
_Z='hmPortSecMASlotID'
_Y='hmPortSecExtPortID'
_X='hmPortSecExtSlotID'
_W='enabledWithWrongAddr'
_V='disabled'
_U='enabled'
_T='hmPortSecPortID'
_S='hmPortSecSlotID'
_R='hmUserID'
_Q='hmUserGroupMemberUserID'
_P='hmUserGroupMemberGroupID'
_O='hmUserGroupID'
_N='TextualConvention'
_M='OctetString'
_L='false'
_K='true'
_J='hmPortSecConnectedUserID'
_I='portDisable'
_H='trapOnly'
_G='none'
_F='not-accessible'
_E='read-only'
_D='read-write'
_C='USERGROUP-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmConfiguration,=mibBuilder.importSymbols('HMPRIV-MGMT-SNMP-MIB','hmConfiguration')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TextualConvention,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_N,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress',_N)
hmUserGroup=ModuleIdentity((1,3,6,1,4,1,248,14,3))
if mibBuilder.loadTexts:hmUserGroup.setRevisions(('2007-09-13 12:00',))
class MemberID(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_HmUserGroupEvent_ObjectIdentity=ObjectIdentity
hmUserGroupEvent=_HmUserGroupEvent_ObjectIdentity((1,3,6,1,4,1,248,14,3,0))
if mibBuilder.loadTexts:hmUserGroupEvent.setStatus(_A)
_HmUserGroupTable_Object=MibTable
hmUserGroupTable=_HmUserGroupTable_Object((1,3,6,1,4,1,248,14,3,1))
if mibBuilder.loadTexts:hmUserGroupTable.setStatus(_A)
_HmUserGroupEntry_Object=MibTableRow
hmUserGroupEntry=_HmUserGroupEntry_Object((1,3,6,1,4,1,248,14,3,1,1))
hmUserGroupEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:hmUserGroupEntry.setStatus(_A)
_HmUserGroupID_Type=Integer32
_HmUserGroupID_Object=MibTableColumn
hmUserGroupID=_HmUserGroupID_Object((1,3,6,1,4,1,248,14,3,1,1,1),_HmUserGroupID_Type())
hmUserGroupID.setMaxAccess(_E)
if mibBuilder.loadTexts:hmUserGroupID.setStatus(_A)
_HmUserGroupDescription_Type=DisplayString
_HmUserGroupDescription_Object=MibTableColumn
hmUserGroupDescription=_HmUserGroupDescription_Object((1,3,6,1,4,1,248,14,3,1,1,2),_HmUserGroupDescription_Type())
hmUserGroupDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:hmUserGroupDescription.setStatus(_A)
class _HmUserGroupRestricted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_HmUserGroupRestricted_Type.__name__=_B
_HmUserGroupRestricted_Object=MibTableColumn
hmUserGroupRestricted=_HmUserGroupRestricted_Object((1,3,6,1,4,1,248,14,3,1,1,3),_HmUserGroupRestricted_Type())
hmUserGroupRestricted.setMaxAccess(_D)
if mibBuilder.loadTexts:hmUserGroupRestricted.setStatus(_A)
class _HmUserGroupSecAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_HmUserGroupSecAction_Type.__name__=_B
_HmUserGroupSecAction_Object=MibTableColumn
hmUserGroupSecAction=_HmUserGroupSecAction_Object((1,3,6,1,4,1,248,14,3,1,1,4),_HmUserGroupSecAction_Type())
hmUserGroupSecAction.setMaxAccess(_D)
if mibBuilder.loadTexts:hmUserGroupSecAction.setStatus(_A)
_HmUserGroupMemberTable_Object=MibTable
hmUserGroupMemberTable=_HmUserGroupMemberTable_Object((1,3,6,1,4,1,248,14,3,2))
if mibBuilder.loadTexts:hmUserGroupMemberTable.setStatus(_A)
_HmUserGroupMemberEntry_Object=MibTableRow
hmUserGroupMemberEntry=_HmUserGroupMemberEntry_Object((1,3,6,1,4,1,248,14,3,2,1))
hmUserGroupMemberEntry.setIndexNames((0,_C,_P),(0,_C,_Q))
if mibBuilder.loadTexts:hmUserGroupMemberEntry.setStatus(_A)
_HmUserGroupMemberGroupID_Type=Integer32
_HmUserGroupMemberGroupID_Object=MibTableColumn
hmUserGroupMemberGroupID=_HmUserGroupMemberGroupID_Object((1,3,6,1,4,1,248,14,3,2,1,1),_HmUserGroupMemberGroupID_Type())
hmUserGroupMemberGroupID.setMaxAccess(_E)
if mibBuilder.loadTexts:hmUserGroupMemberGroupID.setStatus(_A)
_HmUserGroupMemberUserID_Type=MemberID
_HmUserGroupMemberUserID_Object=MibTableColumn
hmUserGroupMemberUserID=_HmUserGroupMemberUserID_Object((1,3,6,1,4,1,248,14,3,2,1,2),_HmUserGroupMemberUserID_Type())
hmUserGroupMemberUserID.setMaxAccess(_E)
if mibBuilder.loadTexts:hmUserGroupMemberUserID.setStatus(_A)
_HmUserTable_Object=MibTable
hmUserTable=_HmUserTable_Object((1,3,6,1,4,1,248,14,3,3))
if mibBuilder.loadTexts:hmUserTable.setStatus(_A)
_HmUserEntry_Object=MibTableRow
hmUserEntry=_HmUserEntry_Object((1,3,6,1,4,1,248,14,3,3,1))
hmUserEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:hmUserEntry.setStatus(_A)
_HmUserID_Type=MemberID
_HmUserID_Object=MibTableColumn
hmUserID=_HmUserID_Object((1,3,6,1,4,1,248,14,3,3,1,1),_HmUserID_Type())
hmUserID.setMaxAccess(_E)
if mibBuilder.loadTexts:hmUserID.setStatus(_A)
class _HmUserRestricted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_HmUserRestricted_Type.__name__=_B
_HmUserRestricted_Object=MibTableColumn
hmUserRestricted=_HmUserRestricted_Object((1,3,6,1,4,1,248,14,3,3,1,2),_HmUserRestricted_Type())
hmUserRestricted.setMaxAccess(_D)
if mibBuilder.loadTexts:hmUserRestricted.setStatus(_A)
_HmPortSecurityTable_Object=MibTable
hmPortSecurityTable=_HmPortSecurityTable_Object((1,3,6,1,4,1,248,14,3,4))
if mibBuilder.loadTexts:hmPortSecurityTable.setStatus(_A)
_HmPortSecurityEntry_Object=MibTableRow
hmPortSecurityEntry=_HmPortSecurityEntry_Object((1,3,6,1,4,1,248,14,3,4,1))
hmPortSecurityEntry.setIndexNames((0,_C,_S),(0,_C,_T))
if mibBuilder.loadTexts:hmPortSecurityEntry.setStatus(_A)
class _HmPortSecSlotID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_HmPortSecSlotID_Type.__name__=_B
_HmPortSecSlotID_Object=MibTableColumn
hmPortSecSlotID=_HmPortSecSlotID_Object((1,3,6,1,4,1,248,14,3,4,1,1),_HmPortSecSlotID_Type())
hmPortSecSlotID.setMaxAccess(_E)
if mibBuilder.loadTexts:hmPortSecSlotID.setStatus(_A)
class _HmPortSecPortID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_HmPortSecPortID_Type.__name__=_B
_HmPortSecPortID_Object=MibTableColumn
hmPortSecPortID=_HmPortSecPortID_Object((1,3,6,1,4,1,248,14,3,4,1,2),_HmPortSecPortID_Type())
hmPortSecPortID.setMaxAccess(_E)
if mibBuilder.loadTexts:hmPortSecPortID.setStatus(_A)
class _HmPortSecPermission_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('user',1),('group',2),('known',3),('world',4),('uplink',5)))
_HmPortSecPermission_Type.__name__=_B
_HmPortSecPermission_Object=MibTableColumn
hmPortSecPermission=_HmPortSecPermission_Object((1,3,6,1,4,1,248,14,3,4,1,3),_HmPortSecPermission_Type())
hmPortSecPermission.setMaxAccess(_D)
if mibBuilder.loadTexts:hmPortSecPermission.setStatus(_A)
_HmPortSecAllowedUserID_Type=MemberID
_HmPortSecAllowedUserID_Object=MibTableColumn
hmPortSecAllowedUserID=_HmPortSecAllowedUserID_Object((1,3,6,1,4,1,248,14,3,4,1,4),_HmPortSecAllowedUserID_Type())
hmPortSecAllowedUserID.setMaxAccess(_D)
if mibBuilder.loadTexts:hmPortSecAllowedUserID.setStatus(_A)
class _HmPortSecAllowedGroupIDs_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_HmPortSecAllowedGroupIDs_Type.__name__=_M
_HmPortSecAllowedGroupIDs_Object=MibTableColumn
hmPortSecAllowedGroupIDs=_HmPortSecAllowedGroupIDs_Object((1,3,6,1,4,1,248,14,3,4,1,5),_HmPortSecAllowedGroupIDs_Type())
hmPortSecAllowedGroupIDs.setMaxAccess(_D)
if mibBuilder.loadTexts:hmPortSecAllowedGroupIDs.setStatus(_A)
_HmPortSecConnectedUserID_Type=MemberID
_HmPortSecConnectedUserID_Object=MibTableColumn
hmPortSecConnectedUserID=_HmPortSecConnectedUserID_Object((1,3,6,1,4,1,248,14,3,4,1,6),_HmPortSecConnectedUserID_Type())
hmPortSecConnectedUserID.setMaxAccess(_E)
if mibBuilder.loadTexts:hmPortSecConnectedUserID.setStatus(_A)
class _HmPortSecAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3),('autoDisable',4)))
_HmPortSecAction_Type.__name__=_B
_HmPortSecAction_Object=MibTableColumn
hmPortSecAction=_HmPortSecAction_Object((1,3,6,1,4,1,248,14,3,4,1,7),_HmPortSecAction_Type())
hmPortSecAction.setMaxAccess(_D)
if mibBuilder.loadTexts:hmPortSecAction.setStatus(_A)
class _HmPortSecAutoReconfigure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_HmPortSecAutoReconfigure_Type.__name__=_B
_HmPortSecAutoReconfigure_Object=MibTableColumn
hmPortSecAutoReconfigure=_HmPortSecAutoReconfigure_Object((1,3,6,1,4,1,248,14,3,4,1,8),_HmPortSecAutoReconfigure_Type())
hmPortSecAutoReconfigure.setMaxAccess(_D)
if mibBuilder.loadTexts:hmPortSecAutoReconfigure.setStatus(_A)
class _HmPortSecPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),(_V,2),(_W,3)))
_HmPortSecPortStatus_Type.__name__=_B
_HmPortSecPortStatus_Object=MibTableColumn
hmPortSecPortStatus=_HmPortSecPortStatus_Object((1,3,6,1,4,1,248,14,3,4,1,9),_HmPortSecPortStatus_Type())
hmPortSecPortStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hmPortSecPortStatus.setStatus(_A)
_HmPortSecAllowedUserIPID_Type=IpAddress
_HmPortSecAllowedUserIPID_Object=MibTableColumn
hmPortSecAllowedUserIPID=_HmPortSecAllowedUserIPID_Object((1,3,6,1,4,1,248,14,3,4,1,10),_HmPortSecAllowedUserIPID_Type())
hmPortSecAllowedUserIPID.setMaxAccess(_D)
if mibBuilder.loadTexts:hmPortSecAllowedUserIPID.setStatus(_A)
class _HmPortSecDynamicLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,50))
_HmPortSecDynamicLimit_Type.__name__=_B
_HmPortSecDynamicLimit_Object=MibTableColumn
hmPortSecDynamicLimit=_HmPortSecDynamicLimit_Object((1,3,6,1,4,1,248,14,3,4,1,11),_HmPortSecDynamicLimit_Type())
hmPortSecDynamicLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:hmPortSecDynamicLimit.setStatus(_A)
_HmPortSecDynamicCount_Type=Integer32
_HmPortSecDynamicCount_Object=MibTableColumn
hmPortSecDynamicCount=_HmPortSecDynamicCount_Object((1,3,6,1,4,1,248,14,3,4,1,12),_HmPortSecDynamicCount_Type())
hmPortSecDynamicCount.setMaxAccess(_E)
if mibBuilder.loadTexts:hmPortSecDynamicCount.setStatus(_A)
class _HmUserGroupSecurityAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_HmUserGroupSecurityAction_Type.__name__=_B
_HmUserGroupSecurityAction_Object=MibScalar
hmUserGroupSecurityAction=_HmUserGroupSecurityAction_Object((1,3,6,1,4,1,248,14,3,5),_HmUserGroupSecurityAction_Type())
hmUserGroupSecurityAction.setMaxAccess(_D)
if mibBuilder.loadTexts:hmUserGroupSecurityAction.setStatus(_A)
class _HmUserGroupPortSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('macAddressBased',1),('ipAddressBased',2)))
_HmUserGroupPortSecurityMode_Type.__name__=_B
_HmUserGroupPortSecurityMode_Object=MibScalar
hmUserGroupPortSecurityMode=_HmUserGroupPortSecurityMode_Object((1,3,6,1,4,1,248,14,3,8),_HmUserGroupPortSecurityMode_Type())
hmUserGroupPortSecurityMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hmUserGroupPortSecurityMode.setStatus(_A)
_HmPortSecExtendedGroup_ObjectIdentity=ObjectIdentity
hmPortSecExtendedGroup=_HmPortSecExtendedGroup_ObjectIdentity((1,3,6,1,4,1,248,14,3,10))
_HmPortSecExtendedTable_Object=MibTable
hmPortSecExtendedTable=_HmPortSecExtendedTable_Object((1,3,6,1,4,1,248,14,3,10,1))
if mibBuilder.loadTexts:hmPortSecExtendedTable.setStatus(_A)
_HmPortSecExtendedEntry_Object=MibTableRow
hmPortSecExtendedEntry=_HmPortSecExtendedEntry_Object((1,3,6,1,4,1,248,14,3,10,1,1))
hmPortSecExtendedEntry.setIndexNames((0,_C,_X),(0,_C,_Y))
if mibBuilder.loadTexts:hmPortSecExtendedEntry.setStatus(_A)
class _HmPortSecExtSlotID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_HmPortSecExtSlotID_Type.__name__=_B
_HmPortSecExtSlotID_Object=MibTableColumn
hmPortSecExtSlotID=_HmPortSecExtSlotID_Object((1,3,6,1,4,1,248,14,3,10,1,1,1),_HmPortSecExtSlotID_Type())
hmPortSecExtSlotID.setMaxAccess(_F)
if mibBuilder.loadTexts:hmPortSecExtSlotID.setStatus(_A)
class _HmPortSecExtPortID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_HmPortSecExtPortID_Type.__name__=_B
_HmPortSecExtPortID_Object=MibTableColumn
hmPortSecExtPortID=_HmPortSecExtPortID_Object((1,3,6,1,4,1,248,14,3,10,1,1,2),_HmPortSecExtPortID_Type())
hmPortSecExtPortID.setMaxAccess(_F)
if mibBuilder.loadTexts:hmPortSecExtPortID.setStatus(_A)
class _HmPortSecExtAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_HmPortSecExtAction_Type.__name__=_B
_HmPortSecExtAction_Object=MibTableColumn
hmPortSecExtAction=_HmPortSecExtAction_Object((1,3,6,1,4,1,248,14,3,10,1,1,3),_HmPortSecExtAction_Type())
hmPortSecExtAction.setMaxAccess(_D)
if mibBuilder.loadTexts:hmPortSecExtAction.setStatus(_A)
class _HmPortSecExtPortStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_U,1),(_V,2),(_W,3)))
_HmPortSecExtPortStatus_Type.__name__=_B
_HmPortSecExtPortStatus_Object=MibTableColumn
hmPortSecExtPortStatus=_HmPortSecExtPortStatus_Object((1,3,6,1,4,1,248,14,3,10,1,1,4),_HmPortSecExtPortStatus_Type())
hmPortSecExtPortStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hmPortSecExtPortStatus.setStatus(_A)
_HmPortSecMultipleAdressesTable_Object=MibTable
hmPortSecMultipleAdressesTable=_HmPortSecMultipleAdressesTable_Object((1,3,6,1,4,1,248,14,3,10,2))
if mibBuilder.loadTexts:hmPortSecMultipleAdressesTable.setStatus(_A)
_HmPortSecMultipleAdressesEntry_Object=MibTableRow
hmPortSecMultipleAdressesEntry=_HmPortSecMultipleAdressesEntry_Object((1,3,6,1,4,1,248,14,3,10,2,1))
hmPortSecMultipleAdressesEntry.setIndexNames((0,_C,_Z),(0,_C,_a),(0,_C,_b))
if mibBuilder.loadTexts:hmPortSecMultipleAdressesEntry.setStatus(_A)
class _HmPortSecMASlotID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_HmPortSecMASlotID_Type.__name__=_B
_HmPortSecMASlotID_Object=MibTableColumn
hmPortSecMASlotID=_HmPortSecMASlotID_Object((1,3,6,1,4,1,248,14,3,10,2,1,1),_HmPortSecMASlotID_Type())
hmPortSecMASlotID.setMaxAccess(_F)
if mibBuilder.loadTexts:hmPortSecMASlotID.setStatus(_A)
class _HmPortSecMAPortID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_HmPortSecMAPortID_Type.__name__=_B
_HmPortSecMAPortID_Object=MibTableColumn
hmPortSecMAPortID=_HmPortSecMAPortID_Object((1,3,6,1,4,1,248,14,3,10,2,1,2),_HmPortSecMAPortID_Type())
hmPortSecMAPortID.setMaxAccess(_F)
if mibBuilder.loadTexts:hmPortSecMAPortID.setStatus(_A)
class _HmPortSecMAExtendedIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_HmPortSecMAExtendedIndex_Type.__name__=_B
_HmPortSecMAExtendedIndex_Object=MibTableColumn
hmPortSecMAExtendedIndex=_HmPortSecMAExtendedIndex_Object((1,3,6,1,4,1,248,14,3,10,2,1,3),_HmPortSecMAExtendedIndex_Type())
hmPortSecMAExtendedIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hmPortSecMAExtendedIndex.setStatus(_A)
_HmPortSecMAAllowedUserIDs_Type=MemberID
_HmPortSecMAAllowedUserIDs_Object=MibTableColumn
hmPortSecMAAllowedUserIDs=_HmPortSecMAAllowedUserIDs_Object((1,3,6,1,4,1,248,14,3,10,2,1,4),_HmPortSecMAAllowedUserIDs_Type())
hmPortSecMAAllowedUserIDs.setMaxAccess(_D)
if mibBuilder.loadTexts:hmPortSecMAAllowedUserIDs.setStatus(_A)
_HmPortSecMAAllowedUserIPIDs_Type=IpAddress
_HmPortSecMAAllowedUserIPIDs_Object=MibTableColumn
hmPortSecMAAllowedUserIPIDs=_HmPortSecMAAllowedUserIPIDs_Object((1,3,6,1,4,1,248,14,3,10,2,1,5),_HmPortSecMAAllowedUserIPIDs_Type())
hmPortSecMAAllowedUserIPIDs.setMaxAccess(_D)
if mibBuilder.loadTexts:hmPortSecMAAllowedUserIPIDs.setStatus(_A)
class _HmPortSecMAAllowedUserIDMask_Type(Integer32):defaultValue=48;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_HmPortSecMAAllowedUserIDMask_Type.__name__=_B
_HmPortSecMAAllowedUserIDMask_Object=MibTableColumn
hmPortSecMAAllowedUserIDMask=_HmPortSecMAAllowedUserIDMask_Object((1,3,6,1,4,1,248,14,3,10,2,1,6),_HmPortSecMAAllowedUserIDMask_Type())
hmPortSecMAAllowedUserIDMask.setMaxAccess(_D)
if mibBuilder.loadTexts:hmPortSecMAAllowedUserIDMask.setStatus(_A)
hmNewUserTrap=NotificationType((1,3,6,1,4,1,248,14,3,0,1))
hmNewUserTrap.setObjects((_C,_J))
if mibBuilder.loadTexts:hmNewUserTrap.setStatus(_A)
hmPortSecurityTrap=NotificationType((1,3,6,1,4,1,248,14,3,0,2))
hmPortSecurityTrap.setObjects(*((_C,_c),(_C,_d),(_C,_J),(_C,_e),(_C,_f),(_C,_g)))
if mibBuilder.loadTexts:hmPortSecurityTrap.setStatus(_A)
hmPortSecConfigErrorTrap=NotificationType((1,3,6,1,4,1,248,14,3,0,3))
hmPortSecConfigErrorTrap.setObjects((_C,_J))
if mibBuilder.loadTexts:hmPortSecConfigErrorTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'MemberID':MemberID,'hmUserGroup':hmUserGroup,'hmUserGroupEvent':hmUserGroupEvent,'hmNewUserTrap':hmNewUserTrap,'hmPortSecurityTrap':hmPortSecurityTrap,'hmPortSecConfigErrorTrap':hmPortSecConfigErrorTrap,'hmUserGroupTable':hmUserGroupTable,'hmUserGroupEntry':hmUserGroupEntry,_O:hmUserGroupID,'hmUserGroupDescription':hmUserGroupDescription,'hmUserGroupRestricted':hmUserGroupRestricted,'hmUserGroupSecAction':hmUserGroupSecAction,'hmUserGroupMemberTable':hmUserGroupMemberTable,'hmUserGroupMemberEntry':hmUserGroupMemberEntry,_P:hmUserGroupMemberGroupID,_Q:hmUserGroupMemberUserID,'hmUserTable':hmUserTable,'hmUserEntry':hmUserEntry,_R:hmUserID,'hmUserRestricted':hmUserRestricted,'hmPortSecurityTable':hmPortSecurityTable,'hmPortSecurityEntry':hmPortSecurityEntry,_S:hmPortSecSlotID,_T:hmPortSecPortID,_c:hmPortSecPermission,_e:hmPortSecAllowedUserID,_g:hmPortSecAllowedGroupIDs,_J:hmPortSecConnectedUserID,_d:hmPortSecAction,'hmPortSecAutoReconfigure':hmPortSecAutoReconfigure,'hmPortSecPortStatus':hmPortSecPortStatus,_f:hmPortSecAllowedUserIPID,'hmPortSecDynamicLimit':hmPortSecDynamicLimit,'hmPortSecDynamicCount':hmPortSecDynamicCount,'hmUserGroupSecurityAction':hmUserGroupSecurityAction,'hmUserGroupPortSecurityMode':hmUserGroupPortSecurityMode,'hmPortSecExtendedGroup':hmPortSecExtendedGroup,'hmPortSecExtendedTable':hmPortSecExtendedTable,'hmPortSecExtendedEntry':hmPortSecExtendedEntry,_X:hmPortSecExtSlotID,_Y:hmPortSecExtPortID,'hmPortSecExtAction':hmPortSecExtAction,'hmPortSecExtPortStatus':hmPortSecExtPortStatus,'hmPortSecMultipleAdressesTable':hmPortSecMultipleAdressesTable,'hmPortSecMultipleAdressesEntry':hmPortSecMultipleAdressesEntry,_Z:hmPortSecMASlotID,_a:hmPortSecMAPortID,_b:hmPortSecMAExtendedIndex,'hmPortSecMAAllowedUserIDs':hmPortSecMAAllowedUserIDs,'hmPortSecMAAllowedUserIPIDs':hmPortSecMAAllowedUserIPIDs,'hmPortSecMAAllowedUserIDMask':hmPortSecMAAllowedUserIDMask})