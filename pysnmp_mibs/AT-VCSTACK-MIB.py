_O='vcstackRole'
_N='accessible-for-notify'
_M='learntNeighbour'
_L='discoveringNeighbour'
_K='neighbourIncompatible'
_J='notConfigured'
_I='vcstackStkPortName'
_H='vcstackResiliencyLinkInterfaceName'
_G='vcstackNbrMemberId'
_F='Unsigned32'
_E='vcstackId'
_D='Integer32'
_C='AT-VCSTACK-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sysinfo,=mibBuilder.importSymbols('AT-SMI-MIB','sysinfo')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention','TruthValue')
vcstack=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,3,13))
if mibBuilder.loadTexts:vcstack.setRevisions(('2009-06-08 00:00','2008-03-19 00:00'))
class _VcstackStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normalOperation',1),('operatingInFailoverState',2),('standaloneUnit',3),('ringTopologyBroken',4)))
_VcstackStatus_Type.__name__=_D
_VcstackStatus_Object=MibScalar
vcstackStatus=_VcstackStatus_Object((1,3,6,1,4,1,207,8,4,4,3,13,1),_VcstackStatus_Type())
vcstackStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackStatus.setStatus(_A)
class _VcstackOperationalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_VcstackOperationalStatus_Type.__name__=_D
_VcstackOperationalStatus_Object=MibScalar
vcstackOperationalStatus=_VcstackOperationalStatus_Object((1,3,6,1,4,1,207,8,4,4,3,13,2),_VcstackOperationalStatus_Type())
vcstackOperationalStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackOperationalStatus.setStatus(_A)
_VcstackMgmtVlanId_Type=Integer32
_VcstackMgmtVlanId_Object=MibScalar
vcstackMgmtVlanId=_VcstackMgmtVlanId_Object((1,3,6,1,4,1,207,8,4,4,3,13,3),_VcstackMgmtVlanId_Type())
vcstackMgmtVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackMgmtVlanId.setStatus(_A)
_VcstackMgmtVlanSubnetAddr_Type=IpAddress
_VcstackMgmtVlanSubnetAddr_Object=MibScalar
vcstackMgmtVlanSubnetAddr=_VcstackMgmtVlanSubnetAddr_Object((1,3,6,1,4,1,207,8,4,4,3,13,4),_VcstackMgmtVlanSubnetAddr_Type())
vcstackMgmtVlanSubnetAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackMgmtVlanSubnetAddr.setStatus(_A)
_VcstackTable_Object=MibTable
vcstackTable=_VcstackTable_Object((1,3,6,1,4,1,207,8,4,4,3,13,5))
if mibBuilder.loadTexts:vcstackTable.setStatus(_A)
_VcstackEntry_Object=MibTableRow
vcstackEntry=_VcstackEntry_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1))
vcstackEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:vcstackEntry.setStatus(_A)
class _VcstackId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_VcstackId_Type.__name__=_F
_VcstackId_Object=MibTableColumn
vcstackId=_VcstackId_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1,1),_VcstackId_Type())
vcstackId.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackId.setStatus(_A)
class _VcstackPendingId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_VcstackPendingId_Type.__name__=_F
_VcstackPendingId_Object=MibTableColumn
vcstackPendingId=_VcstackPendingId_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1,2),_VcstackPendingId_Type())
vcstackPendingId.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackPendingId.setStatus(_A)
_VcstackMacAddr_Type=MacAddress
_VcstackMacAddr_Object=MibTableColumn
vcstackMacAddr=_VcstackMacAddr_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1,3),_VcstackMacAddr_Type())
vcstackMacAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackMacAddr.setStatus(_A)
class _VcstackPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VcstackPriority_Type.__name__=_F
_VcstackPriority_Object=MibTableColumn
vcstackPriority=_VcstackPriority_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1,4),_VcstackPriority_Type())
vcstackPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackPriority.setStatus(_A)
class _VcstackRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('leaving',1),('discovering',2),('synchronizing',3),('backupMember',4),('pendingMaster',5),('disabledMaster',6),('fallbackMaster',7),('activeMaster',8)))
_VcstackRole_Type.__name__=_D
_VcstackRole_Object=MibTableColumn
vcstackRole=_VcstackRole_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1,5),_VcstackRole_Type())
vcstackRole.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackRole.setStatus(_A)
_VcstackLastRoleChange_Type=DisplayString
_VcstackLastRoleChange_Object=MibTableColumn
vcstackLastRoleChange=_VcstackLastRoleChange_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1,6),_VcstackLastRoleChange_Type())
vcstackLastRoleChange.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackLastRoleChange.setStatus(_A)
_VcstackHostname_Type=DisplayString
_VcstackHostname_Object=MibTableColumn
vcstackHostname=_VcstackHostname_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1,7),_VcstackHostname_Type())
vcstackHostname.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackHostname.setStatus(_A)
_VcstackProductType_Type=DisplayString
_VcstackProductType_Object=MibTableColumn
vcstackProductType=_VcstackProductType_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1,8),_VcstackProductType_Type())
vcstackProductType.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackProductType.setStatus(_A)
_VcstackSWVersionAutoSync_Type=TruthValue
_VcstackSWVersionAutoSync_Object=MibTableColumn
vcstackSWVersionAutoSync=_VcstackSWVersionAutoSync_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1,9),_VcstackSWVersionAutoSync_Type())
vcstackSWVersionAutoSync.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackSWVersionAutoSync.setStatus(_A)
class _VcstackFallbackConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fileExists',1),('fileNotFound',2),(_J,3)))
_VcstackFallbackConfigStatus_Type.__name__=_D
_VcstackFallbackConfigStatus_Object=MibTableColumn
vcstackFallbackConfigStatus=_VcstackFallbackConfigStatus_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1,10),_VcstackFallbackConfigStatus_Type())
vcstackFallbackConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackFallbackConfigStatus.setStatus(_A)
_VcstackFallbackConfigFilename_Type=DisplayString
_VcstackFallbackConfigFilename_Object=MibTableColumn
vcstackFallbackConfigFilename=_VcstackFallbackConfigFilename_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1,11),_VcstackFallbackConfigFilename_Type())
vcstackFallbackConfigFilename.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackFallbackConfigFilename.setStatus(_A)
class _VcstackResiliencyLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('configured',1),('successful',2),('failed',3),(_J,4)))
_VcstackResiliencyLinkStatus_Type.__name__=_D
_VcstackResiliencyLinkStatus_Object=MibTableColumn
vcstackResiliencyLinkStatus=_VcstackResiliencyLinkStatus_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1,12),_VcstackResiliencyLinkStatus_Type())
vcstackResiliencyLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackResiliencyLinkStatus.setStatus(_A)
_VcstackResiliencyLinkInterfaceName_Type=DisplayString
_VcstackResiliencyLinkInterfaceName_Object=MibTableColumn
vcstackResiliencyLinkInterfaceName=_VcstackResiliencyLinkInterfaceName_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1,13),_VcstackResiliencyLinkInterfaceName_Type())
vcstackResiliencyLinkInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackResiliencyLinkInterfaceName.setStatus(_A)
class _VcstackActiveStkHardware_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('xemStk',1),('builtinStackingPorts',2),('none',3)))
_VcstackActiveStkHardware_Type.__name__=_D
_VcstackActiveStkHardware_Object=MibTableColumn
vcstackActiveStkHardware=_VcstackActiveStkHardware_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1,14),_VcstackActiveStkHardware_Type())
vcstackActiveStkHardware.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackActiveStkHardware.setStatus(_A)
class _VcstackStkPort1Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('down',1),(_K,2),(_L,3),(_M,4)))
_VcstackStkPort1Status_Type.__name__=_D
_VcstackStkPort1Status_Object=MibTableColumn
vcstackStkPort1Status=_VcstackStkPort1Status_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1,15),_VcstackStkPort1Status_Type())
vcstackStkPort1Status.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackStkPort1Status.setStatus(_A)
class _VcstackStkPort1NeighbourId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_VcstackStkPort1NeighbourId_Type.__name__=_F
_VcstackStkPort1NeighbourId_Object=MibTableColumn
vcstackStkPort1NeighbourId=_VcstackStkPort1NeighbourId_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1,16),_VcstackStkPort1NeighbourId_Type())
vcstackStkPort1NeighbourId.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackStkPort1NeighbourId.setStatus(_A)
class _VcstackStkPort2Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('down',1),(_K,2),(_L,3),(_M,4)))
_VcstackStkPort2Status_Type.__name__=_D
_VcstackStkPort2Status_Object=MibTableColumn
vcstackStkPort2Status=_VcstackStkPort2Status_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1,17),_VcstackStkPort2Status_Type())
vcstackStkPort2Status.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackStkPort2Status.setStatus(_A)
class _VcstackStkPort2NeighbourId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_VcstackStkPort2NeighbourId_Type.__name__=_F
_VcstackStkPort2NeighbourId_Object=MibTableColumn
vcstackStkPort2NeighbourId=_VcstackStkPort2NeighbourId_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1,18),_VcstackStkPort2NeighbourId_Type())
vcstackStkPort2NeighbourId.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackStkPort2NeighbourId.setStatus(_A)
_VcstackNumMembersJoined_Type=Counter32
_VcstackNumMembersJoined_Object=MibTableColumn
vcstackNumMembersJoined=_VcstackNumMembersJoined_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1,19),_VcstackNumMembersJoined_Type())
vcstackNumMembersJoined.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackNumMembersJoined.setStatus(_A)
_VcstackNumMembersLeft_Type=Counter32
_VcstackNumMembersLeft_Object=MibTableColumn
vcstackNumMembersLeft=_VcstackNumMembersLeft_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1,20),_VcstackNumMembersLeft_Type())
vcstackNumMembersLeft.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackNumMembersLeft.setStatus(_A)
_VcstackNumIdConflict_Type=Counter32
_VcstackNumIdConflict_Object=MibTableColumn
vcstackNumIdConflict=_VcstackNumIdConflict_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1,21),_VcstackNumIdConflict_Type())
vcstackNumIdConflict.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackNumIdConflict.setStatus(_A)
_VcstackNumMasterConflict_Type=Counter32
_VcstackNumMasterConflict_Object=MibTableColumn
vcstackNumMasterConflict=_VcstackNumMasterConflict_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1,22),_VcstackNumMasterConflict_Type())
vcstackNumMasterConflict.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackNumMasterConflict.setStatus(_A)
_VcstackNumMasterFailover_Type=Counter32
_VcstackNumMasterFailover_Object=MibTableColumn
vcstackNumMasterFailover=_VcstackNumMasterFailover_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1,23),_VcstackNumMasterFailover_Type())
vcstackNumMasterFailover.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackNumMasterFailover.setStatus(_A)
_VcstackNumStkPort1NbrIncompatible_Type=Counter32
_VcstackNumStkPort1NbrIncompatible_Object=MibTableColumn
vcstackNumStkPort1NbrIncompatible=_VcstackNumStkPort1NbrIncompatible_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1,24),_VcstackNumStkPort1NbrIncompatible_Type())
vcstackNumStkPort1NbrIncompatible.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackNumStkPort1NbrIncompatible.setStatus(_A)
_VcstackNumStkPort2NbrIncompatible_Type=Counter32
_VcstackNumStkPort2NbrIncompatible_Object=MibTableColumn
vcstackNumStkPort2NbrIncompatible=_VcstackNumStkPort2NbrIncompatible_Object((1,3,6,1,4,1,207,8,4,4,3,13,5,1,25),_VcstackNumStkPort2NbrIncompatible_Type())
vcstackNumStkPort2NbrIncompatible.setMaxAccess(_B)
if mibBuilder.loadTexts:vcstackNumStkPort2NbrIncompatible.setStatus(_A)
_VcstackTraps_ObjectIdentity=ObjectIdentity
vcstackTraps=_VcstackTraps_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,3,13,6))
class _VcstackNbrMemberId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_VcstackNbrMemberId_Type.__name__=_F
_VcstackNbrMemberId_Object=MibScalar
vcstackNbrMemberId=_VcstackNbrMemberId_Object((1,3,6,1,4,1,207,8,4,4,3,13,6,8),_VcstackNbrMemberId_Type())
vcstackNbrMemberId.setMaxAccess(_N)
if mibBuilder.loadTexts:vcstackNbrMemberId.setStatus(_A)
_VcstackStkPortName_Type=DisplayString
_VcstackStkPortName_Object=MibScalar
vcstackStkPortName=_VcstackStkPortName_Object((1,3,6,1,4,1,207,8,4,4,3,13,6,9),_VcstackStkPortName_Type())
vcstackStkPortName.setMaxAccess(_N)
if mibBuilder.loadTexts:vcstackStkPortName.setStatus(_A)
vcstackRoleChange=NotificationType((1,3,6,1,4,1,207,8,4,4,3,13,6,1))
vcstackRoleChange.setObjects(*((_C,_E),(_C,_O)))
if mibBuilder.loadTexts:vcstackRoleChange.setStatus(_A)
vcstackMemberJoin=NotificationType((1,3,6,1,4,1,207,8,4,4,3,13,6,2))
vcstackMemberJoin.setObjects(*((_C,_E),(_C,_G)))
if mibBuilder.loadTexts:vcstackMemberJoin.setStatus(_A)
vcstackMemberLeave=NotificationType((1,3,6,1,4,1,207,8,4,4,3,13,6,3))
vcstackMemberLeave.setObjects(*((_C,_E),(_C,_G)))
if mibBuilder.loadTexts:vcstackMemberLeave.setStatus(_A)
vcstackResiliencyLinkHealthCheckReceiving=NotificationType((1,3,6,1,4,1,207,8,4,4,3,13,6,4))
vcstackResiliencyLinkHealthCheckReceiving.setObjects(*((_C,_E),(_C,_H)))
if mibBuilder.loadTexts:vcstackResiliencyLinkHealthCheckReceiving.setStatus(_A)
vcstackResiliencyLinkHealthCheckTimeOut=NotificationType((1,3,6,1,4,1,207,8,4,4,3,13,6,5))
vcstackResiliencyLinkHealthCheckTimeOut.setObjects(*((_C,_E),(_C,_H)))
if mibBuilder.loadTexts:vcstackResiliencyLinkHealthCheckTimeOut.setStatus(_A)
vcstackStkPortLinkUp=NotificationType((1,3,6,1,4,1,207,8,4,4,3,13,6,6))
vcstackStkPortLinkUp.setObjects(*((_C,_E),(_C,_I)))
if mibBuilder.loadTexts:vcstackStkPortLinkUp.setStatus(_A)
vcstackStkPortLinkDown=NotificationType((1,3,6,1,4,1,207,8,4,4,3,13,6,7))
vcstackStkPortLinkDown.setObjects(*((_C,_E),(_C,_I)))
if mibBuilder.loadTexts:vcstackStkPortLinkDown.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'vcstack':vcstack,'vcstackStatus':vcstackStatus,'vcstackOperationalStatus':vcstackOperationalStatus,'vcstackMgmtVlanId':vcstackMgmtVlanId,'vcstackMgmtVlanSubnetAddr':vcstackMgmtVlanSubnetAddr,'vcstackTable':vcstackTable,'vcstackEntry':vcstackEntry,_E:vcstackId,'vcstackPendingId':vcstackPendingId,'vcstackMacAddr':vcstackMacAddr,'vcstackPriority':vcstackPriority,_O:vcstackRole,'vcstackLastRoleChange':vcstackLastRoleChange,'vcstackHostname':vcstackHostname,'vcstackProductType':vcstackProductType,'vcstackSWVersionAutoSync':vcstackSWVersionAutoSync,'vcstackFallbackConfigStatus':vcstackFallbackConfigStatus,'vcstackFallbackConfigFilename':vcstackFallbackConfigFilename,'vcstackResiliencyLinkStatus':vcstackResiliencyLinkStatus,_H:vcstackResiliencyLinkInterfaceName,'vcstackActiveStkHardware':vcstackActiveStkHardware,'vcstackStkPort1Status':vcstackStkPort1Status,'vcstackStkPort1NeighbourId':vcstackStkPort1NeighbourId,'vcstackStkPort2Status':vcstackStkPort2Status,'vcstackStkPort2NeighbourId':vcstackStkPort2NeighbourId,'vcstackNumMembersJoined':vcstackNumMembersJoined,'vcstackNumMembersLeft':vcstackNumMembersLeft,'vcstackNumIdConflict':vcstackNumIdConflict,'vcstackNumMasterConflict':vcstackNumMasterConflict,'vcstackNumMasterFailover':vcstackNumMasterFailover,'vcstackNumStkPort1NbrIncompatible':vcstackNumStkPort1NbrIncompatible,'vcstackNumStkPort2NbrIncompatible':vcstackNumStkPort2NbrIncompatible,'vcstackTraps':vcstackTraps,'vcstackRoleChange':vcstackRoleChange,'vcstackMemberJoin':vcstackMemberJoin,'vcstackMemberLeave':vcstackMemberLeave,'vcstackResiliencyLinkHealthCheckReceiving':vcstackResiliencyLinkHealthCheckReceiving,'vcstackResiliencyLinkHealthCheckTimeOut':vcstackResiliencyLinkHealthCheckTimeOut,'vcstackStkPortLinkUp':vcstackStkPortLinkUp,'vcstackStkPortLinkDown':vcstackStkPortLinkDown,_G:vcstackNbrMemberId,_I:vcstackStkPortName})