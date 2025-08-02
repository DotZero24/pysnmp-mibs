_K='chassisRole'
_J='chassisNodeId'
_I='unknown'
_H='chassisCardSlot'
_G='accessible-for-notify'
_F='slotNumber'
_E='Unsigned32'
_D='Integer32'
_C='AT-CHASSIS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sysinfo,=mibBuilder.importSymbols('AT-SMI-MIB','sysinfo')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
chassis=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,3,23))
if mibBuilder.loadTexts:chassis.setRevisions(('2014-06-09 00:00','2014-05-26 00:00','2014-04-16 00:00','2012-05-15 00:00','2011-09-26 00:00'))
_ChassisNotifications_ObjectIdentity=ObjectIdentity
chassisNotifications=_ChassisNotifications_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,23,0))
class _SlotNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_SlotNumber_Type.__name__=_E
_SlotNumber_Object=MibScalar
slotNumber=_SlotNumber_Object((1,3,6,1,4,1,207,8,4,4,3,23,0,4),_SlotNumber_Type())
slotNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:slotNumber.setStatus(_A)
class _ChassisRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('leaving',1),('discovering',2),('synchronizing',3),('standbyMember',4),('pendingMaster',5),('disabledMaster',6),('activeMaster',7)))
_ChassisRole_Type.__name__=_D
_ChassisRole_Object=MibScalar
chassisRole=_ChassisRole_Object((1,3,6,1,4,1,207,8,4,4,3,23,0,5),_ChassisRole_Type())
chassisRole.setMaxAccess(_G)
if mibBuilder.loadTexts:chassisRole.setStatus(_A)
_ChassisCardTable_Object=MibTable
chassisCardTable=_ChassisCardTable_Object((1,3,6,1,4,1,207,8,4,4,3,23,1))
if mibBuilder.loadTexts:chassisCardTable.setStatus(_A)
_ChassisCardEntry_Object=MibTableRow
chassisCardEntry=_ChassisCardEntry_Object((1,3,6,1,4,1,207,8,4,4,3,23,1,1))
chassisCardEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:chassisCardEntry.setStatus(_A)
class _ChassisCardSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_ChassisCardSlot_Type.__name__=_D
_ChassisCardSlot_Object=MibTableColumn
chassisCardSlot=_ChassisCardSlot_Object((1,3,6,1,4,1,207,8,4,4,3,23,1,1,1),_ChassisCardSlot_Type())
chassisCardSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisCardSlot.setStatus(_A)
_ChassisCardBoardOID_Type=ObjectIdentifier
_ChassisCardBoardOID_Object=MibTableColumn
chassisCardBoardOID=_ChassisCardBoardOID_Object((1,3,6,1,4,1,207,8,4,4,3,23,1,1,2),_ChassisCardBoardOID_Type())
chassisCardBoardOID.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisCardBoardOID.setStatus(_A)
_ChassisCardName_Type=DisplayString
_ChassisCardName_Object=MibTableColumn
chassisCardName=_ChassisCardName_Object((1,3,6,1,4,1,207,8,4,4,3,23,1,1,3),_ChassisCardName_Type())
chassisCardName.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisCardName.setStatus(_A)
class _ChassisCardState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_I,1),('configuring',2),('syncing',3),('online',4),('syncingFirmware',5),('joining',6),('incompatibleSW',7),('disabled',8),('initializing',9),('booting',10),('unsupportedHW',11),('provisioned',12)))
_ChassisCardState_Type.__name__=_D
_ChassisCardState_Object=MibTableColumn
chassisCardState=_ChassisCardState_Object((1,3,6,1,4,1,207,8,4,4,3,23,1,1,4),_ChassisCardState_Type())
chassisCardState.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisCardState.setStatus(_A)
class _ChassisCardControllerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('active',2),('standby',3)))
_ChassisCardControllerState_Type.__name__=_D
_ChassisCardControllerState_Object=MibTableColumn
chassisCardControllerState=_ChassisCardControllerState_Object((1,3,6,1,4,1,207,8,4,4,3,23,1,1,5),_ChassisCardControllerState_Type())
chassisCardControllerState.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisCardControllerState.setStatus(_A)
_ChassiCardSwVersion_Type=DisplayString
_ChassiCardSwVersion_Object=MibTableColumn
chassiCardSwVersion=_ChassiCardSwVersion_Object((1,3,6,1,4,1,207,8,4,4,3,23,1,1,6),_ChassiCardSwVersion_Type())
chassiCardSwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:chassiCardSwVersion.setStatus(_A)
_ChassisMappingTable_Object=MibTable
chassisMappingTable=_ChassisMappingTable_Object((1,3,6,1,4,1,207,8,4,4,3,23,2))
if mibBuilder.loadTexts:chassisMappingTable.setStatus(_A)
_ChassisMappingEntry_Object=MibTableRow
chassisMappingEntry=_ChassisMappingEntry_Object((1,3,6,1,4,1,207,8,4,4,3,23,2,1))
chassisMappingEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:chassisMappingEntry.setStatus(_A)
class _ChassisNodeId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,24))
_ChassisNodeId_Type.__name__=_E
_ChassisNodeId_Object=MibTableColumn
chassisNodeId=_ChassisNodeId_Object((1,3,6,1,4,1,207,8,4,4,3,23,2,1,1),_ChassisNodeId_Type())
chassisNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisNodeId.setStatus(_A)
class _ChassisVCSMemberId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_ChassisVCSMemberId_Type.__name__=_E
_ChassisVCSMemberId_Object=MibTableColumn
chassisVCSMemberId=_ChassisVCSMemberId_Object((1,3,6,1,4,1,207,8,4,4,3,23,2,1,2),_ChassisVCSMemberId_Type())
chassisVCSMemberId.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisVCSMemberId.setStatus(_A)
class _ChassisSlotNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_ChassisSlotNumber_Type.__name__=_E
_ChassisSlotNumber_Object=MibTableColumn
chassisSlotNumber=_ChassisSlotNumber_Object((1,3,6,1,4,1,207,8,4,4,3,23,2,1,3),_ChassisSlotNumber_Type())
chassisSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisSlotNumber.setStatus(_A)
_ChassisNodeDisplayString_Type=DisplayString
_ChassisNodeDisplayString_Object=MibTableColumn
chassisNodeDisplayString=_ChassisNodeDisplayString_Object((1,3,6,1,4,1,207,8,4,4,3,23,2,1,4),_ChassisNodeDisplayString_Type())
chassisNodeDisplayString.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisNodeDisplayString.setStatus(_A)
_ChassisNodeStateString_Type=DisplayString
_ChassisNodeStateString_Object=MibTableColumn
chassisNodeStateString=_ChassisNodeStateString_Object((1,3,6,1,4,1,207,8,4,4,3,23,2,1,5),_ChassisNodeStateString_Type())
chassisNodeStateString.setMaxAccess(_B)
if mibBuilder.loadTexts:chassisNodeStateString.setStatus(_A)
chassisCardRoleChangeNotify=NotificationType((1,3,6,1,4,1,207,8,4,4,3,23,0,1))
chassisCardRoleChangeNotify.setObjects(*((_C,_F),(_C,_K)))
if mibBuilder.loadTexts:chassisCardRoleChangeNotify.setStatus(_A)
chassisCardJoinNotify=NotificationType((1,3,6,1,4,1,207,8,4,4,3,23,0,2))
chassisCardJoinNotify.setObjects((_C,_F))
if mibBuilder.loadTexts:chassisCardJoinNotify.setStatus(_A)
chassisCardLeaveNotify=NotificationType((1,3,6,1,4,1,207,8,4,4,3,23,0,3))
chassisCardLeaveNotify.setObjects((_C,_F))
if mibBuilder.loadTexts:chassisCardLeaveNotify.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'chassis':chassis,'chassisNotifications':chassisNotifications,'chassisCardRoleChangeNotify':chassisCardRoleChangeNotify,'chassisCardJoinNotify':chassisCardJoinNotify,'chassisCardLeaveNotify':chassisCardLeaveNotify,_F:slotNumber,_K:chassisRole,'chassisCardTable':chassisCardTable,'chassisCardEntry':chassisCardEntry,_H:chassisCardSlot,'chassisCardBoardOID':chassisCardBoardOID,'chassisCardName':chassisCardName,'chassisCardState':chassisCardState,'chassisCardControllerState':chassisCardControllerState,'chassiCardSwVersion':chassiCardSwVersion,'chassisMappingTable':chassisMappingTable,'chassisMappingEntry':chassisMappingEntry,_J:chassisNodeId,'chassisVCSMemberId':chassisVCSMemberId,'chassisSlotNumber':chassisSlotNumber,'chassisNodeDisplayString':chassisNodeDisplayString,'chassisNodeStateString':chassisNodeStateString})