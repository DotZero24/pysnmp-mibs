_W='adGenBondingPortStatusGroup'
_V='adGenBondingPortsGroup'
_U='adGenBondingGroupGroup'
_T='adGenBondingPortRxId'
_S='adGenBondingPortTxId'
_R='adGenBondingPortDiffDelay'
_Q='adGenBondingPortGroupState'
_P='adGenBondingPortsGroupMembership'
_O='adGenBondingGroupNumPorts'
_N='adGenBondingGroupPortsString'
_M='adGenBondingGroupRowStatus'
_L='adGenBondingGroupNumberNext'
_K='adGenBondingPortStatusPortIndex'
_J='adGenBondingPortsIndex'
_I='Integer32'
_H='read-create'
_G='not-accessible'
_F='adGenBondingGroupIndex'
_E='adGenSlotInfoIndex'
_D='ADTRAN-GENSLOT-MIB'
_C='read-only'
_B='ADTRAN-GENBONDING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenBondingID,=mibBuilder.importSymbols('ADTRAN-GENMINIDSLAM-MIB','adGenBondingID')
adGenSlotInfoIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
adGenBonding=ModuleIdentity((1,3,6,1,4,1,664,6,10000,61,4,1))
class AdGenBondingPort(TextualConvention,Integer32):status=_A
_AdGenBondingMib_ObjectIdentity=ObjectIdentity
adGenBondingMib=_AdGenBondingMib_ObjectIdentity((1,3,6,1,4,1,664,6,10000,61,4,1,1))
_AdGenBondingMibObjects_ObjectIdentity=ObjectIdentity
adGenBondingMibObjects=_AdGenBondingMibObjects_ObjectIdentity((1,3,6,1,4,1,664,6,10000,61,4,1,1,1))
_AdGenBondingSlotInfoTable_Object=MibTable
adGenBondingSlotInfoTable=_AdGenBondingSlotInfoTable_Object((1,3,6,1,4,1,664,6,10000,61,4,1,1,1,1))
if mibBuilder.loadTexts:adGenBondingSlotInfoTable.setStatus(_A)
_AdGenBondingSlotInfoEntry_Object=MibTableRow
adGenBondingSlotInfoEntry=_AdGenBondingSlotInfoEntry_Object((1,3,6,1,4,1,664,6,10000,61,4,1,1,1,1,1))
adGenBondingSlotInfoEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:adGenBondingSlotInfoEntry.setStatus(_A)
_AdGenBondingGroupNumberNext_Type=Integer32
_AdGenBondingGroupNumberNext_Object=MibTableColumn
adGenBondingGroupNumberNext=_AdGenBondingGroupNumberNext_Object((1,3,6,1,4,1,664,6,10000,61,4,1,1,1,1,1,1),_AdGenBondingGroupNumberNext_Type())
adGenBondingGroupNumberNext.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenBondingGroupNumberNext.setStatus(_A)
_AdGenGenBondingSlotStatus_Type=DisplayString
_AdGenGenBondingSlotStatus_Object=MibTableColumn
adGenGenBondingSlotStatus=_AdGenGenBondingSlotStatus_Object((1,3,6,1,4,1,664,6,10000,61,4,1,1,1,1,1,2),_AdGenGenBondingSlotStatus_Type())
adGenGenBondingSlotStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenGenBondingSlotStatus.setStatus(_A)
_AdGenBondingGroupTable_Object=MibTable
adGenBondingGroupTable=_AdGenBondingGroupTable_Object((1,3,6,1,4,1,664,6,10000,61,4,1,1,1,2))
if mibBuilder.loadTexts:adGenBondingGroupTable.setStatus(_A)
_AdGenBondingGroupEntry_Object=MibTableRow
adGenBondingGroupEntry=_AdGenBondingGroupEntry_Object((1,3,6,1,4,1,664,6,10000,61,4,1,1,1,2,1))
adGenBondingGroupEntry.setIndexNames((0,_D,_E),(0,_B,_F))
if mibBuilder.loadTexts:adGenBondingGroupEntry.setStatus(_A)
_AdGenBondingGroupIndex_Type=Integer32
_AdGenBondingGroupIndex_Object=MibTableColumn
adGenBondingGroupIndex=_AdGenBondingGroupIndex_Object((1,3,6,1,4,1,664,6,10000,61,4,1,1,1,2,1,1),_AdGenBondingGroupIndex_Type())
adGenBondingGroupIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenBondingGroupIndex.setStatus(_A)
_AdGenBondingGroupRowStatus_Type=RowStatus
_AdGenBondingGroupRowStatus_Object=MibTableColumn
adGenBondingGroupRowStatus=_AdGenBondingGroupRowStatus_Object((1,3,6,1,4,1,664,6,10000,61,4,1,1,1,2,1,2),_AdGenBondingGroupRowStatus_Type())
adGenBondingGroupRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenBondingGroupRowStatus.setStatus(_A)
_AdGenBondingGroupName_Type=DisplayString
_AdGenBondingGroupName_Object=MibTableColumn
adGenBondingGroupName=_AdGenBondingGroupName_Object((1,3,6,1,4,1,664,6,10000,61,4,1,1,1,2,1,3),_AdGenBondingGroupName_Type())
adGenBondingGroupName.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenBondingGroupName.setStatus(_A)
_AdGenBondingGroupPortsString_Type=DisplayString
_AdGenBondingGroupPortsString_Object=MibTableColumn
adGenBondingGroupPortsString=_AdGenBondingGroupPortsString_Object((1,3,6,1,4,1,664,6,10000,61,4,1,1,1,2,1,4),_AdGenBondingGroupPortsString_Type())
adGenBondingGroupPortsString.setMaxAccess(_H)
if mibBuilder.loadTexts:adGenBondingGroupPortsString.setStatus(_A)
_AdGenBondingGroupNumPorts_Type=Integer32
_AdGenBondingGroupNumPorts_Object=MibTableColumn
adGenBondingGroupNumPorts=_AdGenBondingGroupNumPorts_Object((1,3,6,1,4,1,664,6,10000,61,4,1,1,1,2,1,5),_AdGenBondingGroupNumPorts_Type())
adGenBondingGroupNumPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenBondingGroupNumPorts.setStatus(_A)
_AdGenBondingPortsTable_Object=MibTable
adGenBondingPortsTable=_AdGenBondingPortsTable_Object((1,3,6,1,4,1,664,6,10000,61,4,1,1,1,3))
if mibBuilder.loadTexts:adGenBondingPortsTable.setStatus(_A)
_AdGenBondingPortsEntry_Object=MibTableRow
adGenBondingPortsEntry=_AdGenBondingPortsEntry_Object((1,3,6,1,4,1,664,6,10000,61,4,1,1,1,3,1))
adGenBondingPortsEntry.setIndexNames((0,_D,_E),(0,_B,_J))
if mibBuilder.loadTexts:adGenBondingPortsEntry.setStatus(_A)
_AdGenBondingPortsIndex_Type=AdGenBondingPort
_AdGenBondingPortsIndex_Object=MibTableColumn
adGenBondingPortsIndex=_AdGenBondingPortsIndex_Object((1,3,6,1,4,1,664,6,10000,61,4,1,1,1,3,1,1),_AdGenBondingPortsIndex_Type())
adGenBondingPortsIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenBondingPortsIndex.setStatus(_A)
_AdGenBondingPortsGroupMembership_Type=Integer32
_AdGenBondingPortsGroupMembership_Object=MibTableColumn
adGenBondingPortsGroupMembership=_AdGenBondingPortsGroupMembership_Object((1,3,6,1,4,1,664,6,10000,61,4,1,1,1,3,1,2),_AdGenBondingPortsGroupMembership_Type())
adGenBondingPortsGroupMembership.setMaxAccess('read-write')
if mibBuilder.loadTexts:adGenBondingPortsGroupMembership.setStatus(_A)
_AdGenBondingPortStatusTable_Object=MibTable
adGenBondingPortStatusTable=_AdGenBondingPortStatusTable_Object((1,3,6,1,4,1,664,6,10000,61,4,1,1,1,4))
if mibBuilder.loadTexts:adGenBondingPortStatusTable.setStatus(_A)
_AdGenBondingPortStatusEntry_Object=MibTableRow
adGenBondingPortStatusEntry=_AdGenBondingPortStatusEntry_Object((1,3,6,1,4,1,664,6,10000,61,4,1,1,1,4,1))
adGenBondingPortStatusEntry.setIndexNames((0,_D,_E),(0,_B,_F),(0,_B,_K))
if mibBuilder.loadTexts:adGenBondingPortStatusEntry.setStatus(_A)
_AdGenBondingPortStatusPortIndex_Type=AdGenBondingPort
_AdGenBondingPortStatusPortIndex_Object=MibTableColumn
adGenBondingPortStatusPortIndex=_AdGenBondingPortStatusPortIndex_Object((1,3,6,1,4,1,664,6,10000,61,4,1,1,1,4,1,1),_AdGenBondingPortStatusPortIndex_Type())
adGenBondingPortStatusPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenBondingPortStatusPortIndex.setStatus(_A)
class _AdGenBondingPortGroupState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notProvisioned',1),('notUsable',2),('readyForTraffic',3),('carryingTraffic',4)))
_AdGenBondingPortGroupState_Type.__name__=_I
_AdGenBondingPortGroupState_Object=MibTableColumn
adGenBondingPortGroupState=_AdGenBondingPortGroupState_Object((1,3,6,1,4,1,664,6,10000,61,4,1,1,1,4,1,2),_AdGenBondingPortGroupState_Type())
adGenBondingPortGroupState.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenBondingPortGroupState.setStatus(_A)
_AdGenBondingPortDiffDelay_Type=Integer32
_AdGenBondingPortDiffDelay_Object=MibTableColumn
adGenBondingPortDiffDelay=_AdGenBondingPortDiffDelay_Object((1,3,6,1,4,1,664,6,10000,61,4,1,1,1,4,1,3),_AdGenBondingPortDiffDelay_Type())
adGenBondingPortDiffDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenBondingPortDiffDelay.setStatus(_A)
if mibBuilder.loadTexts:adGenBondingPortDiffDelay.setUnits('100 microseconds')
_AdGenBondingPortTxId_Type=Integer32
_AdGenBondingPortTxId_Object=MibTableColumn
adGenBondingPortTxId=_AdGenBondingPortTxId_Object((1,3,6,1,4,1,664,6,10000,61,4,1,1,1,4,1,4),_AdGenBondingPortTxId_Type())
adGenBondingPortTxId.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenBondingPortTxId.setStatus(_A)
_AdGenBondingPortRxId_Type=Integer32
_AdGenBondingPortRxId_Object=MibTableColumn
adGenBondingPortRxId=_AdGenBondingPortRxId_Object((1,3,6,1,4,1,664,6,10000,61,4,1,1,1,4,1,5),_AdGenBondingPortRxId_Type())
adGenBondingPortRxId.setMaxAccess(_C)
if mibBuilder.loadTexts:adGenBondingPortRxId.setStatus(_A)
_AdGenBondingMibConformance_ObjectIdentity=ObjectIdentity
adGenBondingMibConformance=_AdGenBondingMibConformance_ObjectIdentity((1,3,6,1,4,1,664,6,10000,61,4,1,1,2))
_AdGenBondingMibGroups_ObjectIdentity=ObjectIdentity
adGenBondingMibGroups=_AdGenBondingMibGroups_ObjectIdentity((1,3,6,1,4,1,664,6,10000,61,4,1,1,2,1))
_AdGenBondingMibCompliances_ObjectIdentity=ObjectIdentity
adGenBondingMibCompliances=_AdGenBondingMibCompliances_ObjectIdentity((1,3,6,1,4,1,664,6,10000,61,4,1,1,2,2))
adGenBondingGroupGroup=ObjectGroup((1,3,6,1,4,1,664,6,10000,61,4,1,1,2,1,1))
adGenBondingGroupGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:adGenBondingGroupGroup.setStatus(_A)
adGenBondingPortsGroup=ObjectGroup((1,3,6,1,4,1,664,6,10000,61,4,1,1,2,1,2))
adGenBondingPortsGroup.setObjects((_B,_P))
if mibBuilder.loadTexts:adGenBondingPortsGroup.setStatus(_A)
adGenBondingPortStatusGroup=ObjectGroup((1,3,6,1,4,1,664,6,10000,61,4,1,1,2,1,3))
adGenBondingPortStatusGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:adGenBondingPortStatusGroup.setStatus(_A)
adGenBondingMibCompliance=ModuleCompliance((1,3,6,1,4,1,664,6,10000,61,4,1,1,2,2,1))
adGenBondingMibCompliance.setObjects(*((_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:adGenBondingMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AdGenBondingPort':AdGenBondingPort,'adGenBonding':adGenBonding,'adGenBondingMib':adGenBondingMib,'adGenBondingMibObjects':adGenBondingMibObjects,'adGenBondingSlotInfoTable':adGenBondingSlotInfoTable,'adGenBondingSlotInfoEntry':adGenBondingSlotInfoEntry,_L:adGenBondingGroupNumberNext,'adGenGenBondingSlotStatus':adGenGenBondingSlotStatus,'adGenBondingGroupTable':adGenBondingGroupTable,'adGenBondingGroupEntry':adGenBondingGroupEntry,_F:adGenBondingGroupIndex,_M:adGenBondingGroupRowStatus,'adGenBondingGroupName':adGenBondingGroupName,_N:adGenBondingGroupPortsString,_O:adGenBondingGroupNumPorts,'adGenBondingPortsTable':adGenBondingPortsTable,'adGenBondingPortsEntry':adGenBondingPortsEntry,_J:adGenBondingPortsIndex,_P:adGenBondingPortsGroupMembership,'adGenBondingPortStatusTable':adGenBondingPortStatusTable,'adGenBondingPortStatusEntry':adGenBondingPortStatusEntry,_K:adGenBondingPortStatusPortIndex,_Q:adGenBondingPortGroupState,_R:adGenBondingPortDiffDelay,_S:adGenBondingPortTxId,_T:adGenBondingPortRxId,'adGenBondingMibConformance':adGenBondingMibConformance,'adGenBondingMibGroups':adGenBondingMibGroups,_U:adGenBondingGroupGroup,_V:adGenBondingPortsGroup,_W:adGenBondingPortStatusGroup,'adGenBondingMibCompliances':adGenBondingMibCompliances,'adGenBondingMibCompliance':adGenBondingMibCompliance})