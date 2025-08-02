_L='mwApNeighborDetailsTableIndex'
_K='mwApNeighborTableIndex'
_J='mwTopoStaapTableIndex'
_I='mwTopoStaTableIndex'
_H='mwTopoApapTableIndex'
_G='mwTopoApTableIndex'
_F='mwApDiscoveredTableIndex'
_E='mwApAssignedTableIndex'
_D='not-accessible'
_C='MERU-TOPOLOGY-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
mwConfiguration,=mibBuilder.importSymbols('MERU-SMI','mwConfiguration')
MwlApIfModeType,MwlApType,MwlAssociationState,MwlCapabilityModeBits,MwlEncryptionAlgorithm,MwlOnOffSwitch=mibBuilder.importSymbols('MERU-TC','MwlApIfModeType','MwlApType','MwlAssociationState','MwlCapabilityModeBits','MwlEncryptionAlgorithm','MwlOnOffSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp','TruthValue')
mwTopology=ModuleIdentity((1,3,6,1,4,1,15983,1,1,4,13))
_MwApAssignedTable_Object=MibTable
mwApAssignedTable=_MwApAssignedTable_Object((1,3,6,1,4,1,15983,1,1,4,13,1))
if mibBuilder.loadTexts:mwApAssignedTable.setStatus(_A)
_MwApAssignedEntry_Object=MibTableRow
mwApAssignedEntry=_MwApAssignedEntry_Object((1,3,6,1,4,1,15983,1,1,4,13,1,1))
mwApAssignedEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:mwApAssignedEntry.setStatus(_A)
_MwApAssignedTableIndex_Type=Integer32
_MwApAssignedTableIndex_Object=MibTableColumn
mwApAssignedTableIndex=_MwApAssignedTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,13,1,1,1),_MwApAssignedTableIndex_Type())
mwApAssignedTableIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mwApAssignedTableIndex.setStatus(_A)
_MwApAssignedApMac_Type=MacAddress
_MwApAssignedApMac_Object=MibTableColumn
mwApAssignedApMac=_MwApAssignedApMac_Object((1,3,6,1,4,1,15983,1,1,4,13,1,1,2),_MwApAssignedApMac_Type())
mwApAssignedApMac.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApAssignedApMac.setStatus(_A)
_MwApAssignedEssid_Type=DisplayString
_MwApAssignedEssid_Object=MibTableColumn
mwApAssignedEssid=_MwApAssignedEssid_Object((1,3,6,1,4,1,15983,1,1,4,13,1,1,3),_MwApAssignedEssid_Type())
mwApAssignedEssid.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApAssignedEssid.setStatus(_A)
_MwApAssigneddbState_Type=MwlAssociationState
_MwApAssigneddbState_Object=MibTableColumn
mwApAssigneddbState=_MwApAssigneddbState_Object((1,3,6,1,4,1,15983,1,1,4,13,1,1,4),_MwApAssigneddbState_Type())
mwApAssigneddbState.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApAssigneddbState.setStatus(_A)
_MwApAssignedPrevRssi_Type=Integer32
_MwApAssignedPrevRssi_Object=MibTableColumn
mwApAssignedPrevRssi=_MwApAssignedPrevRssi_Object((1,3,6,1,4,1,15983,1,1,4,13,1,1,5),_MwApAssignedPrevRssi_Type())
mwApAssignedPrevRssi.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApAssignedPrevRssi.setStatus(_A)
_MwApAssignedRxPackets_Type=Unsigned32
_MwApAssignedRxPackets_Object=MibTableColumn
mwApAssignedRxPackets=_MwApAssignedRxPackets_Object((1,3,6,1,4,1,15983,1,1,4,13,1,1,6),_MwApAssignedRxPackets_Type())
mwApAssignedRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApAssignedRxPackets.setStatus(_A)
_MwApAssignedTxPackets_Type=Unsigned32
_MwApAssignedTxPackets_Object=MibTableColumn
mwApAssignedTxPackets=_MwApAssignedTxPackets_Object((1,3,6,1,4,1,15983,1,1,4,13,1,1,7),_MwApAssignedTxPackets_Type())
mwApAssignedTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApAssignedTxPackets.setStatus(_A)
_MwApAssignedRadioType_Type=MwlApIfModeType
_MwApAssignedRadioType_Object=MibTableColumn
mwApAssignedRadioType=_MwApAssignedRadioType_Object((1,3,6,1,4,1,15983,1,1,4,13,1,1,8),_MwApAssignedRadioType_Type())
mwApAssignedRadioType.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApAssignedRadioType.setStatus(_A)
_MwApAssignedAuthKeyType_Type=MwlEncryptionAlgorithm
_MwApAssignedAuthKeyType_Object=MibTableColumn
mwApAssignedAuthKeyType=_MwApAssignedAuthKeyType_Object((1,3,6,1,4,1,15983,1,1,4,13,1,1,9),_MwApAssignedAuthKeyType_Type())
mwApAssignedAuthKeyType.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApAssignedAuthKeyType.setStatus(_A)
_MwApAssignedCurrentRssi_Type=Integer32
_MwApAssignedCurrentRssi_Object=MibTableColumn
mwApAssignedCurrentRssi=_MwApAssignedCurrentRssi_Object((1,3,6,1,4,1,15983,1,1,4,13,1,1,10),_MwApAssignedCurrentRssi_Type())
mwApAssignedCurrentRssi.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApAssignedCurrentRssi.setStatus(_A)
_MwApAssignedNmsApNodeId_Type=Integer32
_MwApAssignedNmsApNodeId_Object=MibTableColumn
mwApAssignedNmsApNodeId=_MwApAssignedNmsApNodeId_Object((1,3,6,1,4,1,15983,1,1,4,13,1,1,11),_MwApAssignedNmsApNodeId_Type())
mwApAssignedNmsApNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApAssignedNmsApNodeId.setStatus(_A)
_MwApAssignedApDeviceType_Type=MwlApType
_MwApAssignedApDeviceType_Object=MibTableColumn
mwApAssignedApDeviceType=_MwApAssignedApDeviceType_Object((1,3,6,1,4,1,15983,1,1,4,13,1,1,12),_MwApAssignedApDeviceType_Type())
mwApAssignedApDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApAssignedApDeviceType.setStatus(_A)
_MwApAssignedLastActivity_Type=TimeTicks
_MwApAssignedLastActivity_Object=MibTableColumn
mwApAssignedLastActivity=_MwApAssignedLastActivity_Object((1,3,6,1,4,1,15983,1,1,4,13,1,1,13),_MwApAssignedLastActivity_Type())
mwApAssignedLastActivity.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApAssignedLastActivity.setStatus(_A)
_MwApAssignedNmsApNodeName_Type=DisplayString
_MwApAssignedNmsApNodeName_Object=MibTableColumn
mwApAssignedNmsApNodeName=_MwApAssignedNmsApNodeName_Object((1,3,6,1,4,1,15983,1,1,4,13,1,1,14),_MwApAssignedNmsApNodeName_Type())
mwApAssignedNmsApNodeName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApAssignedNmsApNodeName.setStatus(_A)
_MwApAssignedVirtualPort_Type=MacAddress
_MwApAssignedVirtualPort_Object=MibTableColumn
mwApAssignedVirtualPort=_MwApAssignedVirtualPort_Object((1,3,6,1,4,1,15983,1,1,4,13,1,1,15),_MwApAssignedVirtualPort_Type())
mwApAssignedVirtualPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApAssignedVirtualPort.setStatus(_A)
_MwApAssignedCapabilities_Type=MwlCapabilityModeBits
_MwApAssignedCapabilities_Object=MibTableColumn
mwApAssignedCapabilities=_MwApAssignedCapabilities_Object((1,3,6,1,4,1,15983,1,1,4,13,1,1,16),_MwApAssignedCapabilities_Type())
mwApAssignedCapabilities.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApAssignedCapabilities.setStatus(_A)
_MwApDiscoveredTable_Object=MibTable
mwApDiscoveredTable=_MwApDiscoveredTable_Object((1,3,6,1,4,1,15983,1,1,4,13,2))
if mibBuilder.loadTexts:mwApDiscoveredTable.setStatus(_A)
_MwApDiscoveredEntry_Object=MibTableRow
mwApDiscoveredEntry=_MwApDiscoveredEntry_Object((1,3,6,1,4,1,15983,1,1,4,13,2,1))
mwApDiscoveredEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:mwApDiscoveredEntry.setStatus(_A)
_MwApDiscoveredTableIndex_Type=Integer32
_MwApDiscoveredTableIndex_Object=MibTableColumn
mwApDiscoveredTableIndex=_MwApDiscoveredTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,13,2,1,1),_MwApDiscoveredTableIndex_Type())
mwApDiscoveredTableIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mwApDiscoveredTableIndex.setStatus(_A)
_MwApDiscoveredApMac_Type=MacAddress
_MwApDiscoveredApMac_Object=MibTableColumn
mwApDiscoveredApMac=_MwApDiscoveredApMac_Object((1,3,6,1,4,1,15983,1,1,4,13,2,1,2),_MwApDiscoveredApMac_Type())
mwApDiscoveredApMac.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApDiscoveredApMac.setStatus(_A)
_MwApDiscoveredEssid_Type=DisplayString
_MwApDiscoveredEssid_Object=MibTableColumn
mwApDiscoveredEssid=_MwApDiscoveredEssid_Object((1,3,6,1,4,1,15983,1,1,4,13,2,1,3),_MwApDiscoveredEssid_Type())
mwApDiscoveredEssid.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApDiscoveredEssid.setStatus(_A)
_MwApDiscoveredBssid_Type=MacAddress
_MwApDiscoveredBssid_Object=MibTableColumn
mwApDiscoveredBssid=_MwApDiscoveredBssid_Object((1,3,6,1,4,1,15983,1,1,4,13,2,1,4),_MwApDiscoveredBssid_Type())
mwApDiscoveredBssid.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApDiscoveredBssid.setStatus(_A)
_MwApDiscoveredChannel_Type=Unsigned32
_MwApDiscoveredChannel_Object=MibTableColumn
mwApDiscoveredChannel=_MwApDiscoveredChannel_Object((1,3,6,1,4,1,15983,1,1,4,13,2,1,5),_MwApDiscoveredChannel_Type())
mwApDiscoveredChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApDiscoveredChannel.setStatus(_A)
_MwApDiscoveredPrevRssi_Type=Integer32
_MwApDiscoveredPrevRssi_Object=MibTableColumn
mwApDiscoveredPrevRssi=_MwApDiscoveredPrevRssi_Object((1,3,6,1,4,1,15983,1,1,4,13,2,1,6),_MwApDiscoveredPrevRssi_Type())
mwApDiscoveredPrevRssi.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApDiscoveredPrevRssi.setStatus(_A)
_MwApDiscoveredRxPackets_Type=Unsigned32
_MwApDiscoveredRxPackets_Object=MibTableColumn
mwApDiscoveredRxPackets=_MwApDiscoveredRxPackets_Object((1,3,6,1,4,1,15983,1,1,4,13,2,1,7),_MwApDiscoveredRxPackets_Type())
mwApDiscoveredRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApDiscoveredRxPackets.setStatus(_A)
_MwApDiscoveredRadioType_Type=MwlApIfModeType
_MwApDiscoveredRadioType_Object=MibTableColumn
mwApDiscoveredRadioType=_MwApDiscoveredRadioType_Object((1,3,6,1,4,1,15983,1,1,4,13,2,1,8),_MwApDiscoveredRadioType_Type())
mwApDiscoveredRadioType.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApDiscoveredRadioType.setStatus(_A)
_MwApDiscoveredWiredRogue_Type=MwlOnOffSwitch
_MwApDiscoveredWiredRogue_Object=MibTableColumn
mwApDiscoveredWiredRogue=_MwApDiscoveredWiredRogue_Object((1,3,6,1,4,1,15983,1,1,4,13,2,1,9),_MwApDiscoveredWiredRogue_Type())
mwApDiscoveredWiredRogue.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApDiscoveredWiredRogue.setStatus(_A)
_MwApDiscoveredCurrentRssi_Type=Integer32
_MwApDiscoveredCurrentRssi_Object=MibTableColumn
mwApDiscoveredCurrentRssi=_MwApDiscoveredCurrentRssi_Object((1,3,6,1,4,1,15983,1,1,4,13,2,1,10),_MwApDiscoveredCurrentRssi_Type())
mwApDiscoveredCurrentRssi.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApDiscoveredCurrentRssi.setStatus(_A)
_MwApDiscoveredNmsApNodeId_Type=Integer32
_MwApDiscoveredNmsApNodeId_Object=MibTableColumn
mwApDiscoveredNmsApNodeId=_MwApDiscoveredNmsApNodeId_Object((1,3,6,1,4,1,15983,1,1,4,13,2,1,11),_MwApDiscoveredNmsApNodeId_Type())
mwApDiscoveredNmsApNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApDiscoveredNmsApNodeId.setStatus(_A)
_MwApDiscoveredApDeviceType_Type=MwlApType
_MwApDiscoveredApDeviceType_Object=MibTableColumn
mwApDiscoveredApDeviceType=_MwApDiscoveredApDeviceType_Object((1,3,6,1,4,1,15983,1,1,4,13,2,1,12),_MwApDiscoveredApDeviceType_Type())
mwApDiscoveredApDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApDiscoveredApDeviceType.setStatus(_A)
_MwApDiscoveredLastActivity_Type=TimeTicks
_MwApDiscoveredLastActivity_Object=MibTableColumn
mwApDiscoveredLastActivity=_MwApDiscoveredLastActivity_Object((1,3,6,1,4,1,15983,1,1,4,13,2,1,13),_MwApDiscoveredLastActivity_Type())
mwApDiscoveredLastActivity.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApDiscoveredLastActivity.setStatus(_A)
_MwApDiscoveredNmsApNodeName_Type=DisplayString
_MwApDiscoveredNmsApNodeName_Object=MibTableColumn
mwApDiscoveredNmsApNodeName=_MwApDiscoveredNmsApNodeName_Object((1,3,6,1,4,1,15983,1,1,4,13,2,1,14),_MwApDiscoveredNmsApNodeName_Type())
mwApDiscoveredNmsApNodeName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApDiscoveredNmsApNodeName.setStatus(_A)
_MwApDiscoveredConfirmedChannel_Type=Unsigned32
_MwApDiscoveredConfirmedChannel_Object=MibTableColumn
mwApDiscoveredConfirmedChannel=_MwApDiscoveredConfirmedChannel_Object((1,3,6,1,4,1,15983,1,1,4,13,2,1,15),_MwApDiscoveredConfirmedChannel_Type())
mwApDiscoveredConfirmedChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApDiscoveredConfirmedChannel.setStatus(_A)
_MwTopoApTable_Object=MibTable
mwTopoApTable=_MwTopoApTable_Object((1,3,6,1,4,1,15983,1,1,4,13,4))
if mibBuilder.loadTexts:mwTopoApTable.setStatus(_A)
_MwTopoApEntry_Object=MibTableRow
mwTopoApEntry=_MwTopoApEntry_Object((1,3,6,1,4,1,15983,1,1,4,13,4,1))
mwTopoApEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:mwTopoApEntry.setStatus(_A)
_MwTopoApTableIndex_Type=Integer32
_MwTopoApTableIndex_Object=MibTableColumn
mwTopoApTableIndex=_MwTopoApTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,13,4,1,1),_MwTopoApTableIndex_Type())
mwTopoApTableIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mwTopoApTableIndex.setStatus(_A)
_MwTopoApNodeId_Type=Unsigned32
_MwTopoApNodeId_Object=MibTableColumn
mwTopoApNodeId=_MwTopoApNodeId_Object((1,3,6,1,4,1,15983,1,1,4,13,4,1,2),_MwTopoApNodeId_Type())
mwTopoApNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTopoApNodeId.setStatus(_A)
_MwTopoApNodeName_Type=DisplayString
_MwTopoApNodeName_Object=MibTableColumn
mwTopoApNodeName=_MwTopoApNodeName_Object((1,3,6,1,4,1,15983,1,1,4,13,4,1,3),_MwTopoApNodeName_Type())
mwTopoApNodeName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTopoApNodeName.setStatus(_A)
_MwTopoApAttachedCount_Type=Unsigned32
_MwTopoApAttachedCount_Object=MibTableColumn
mwTopoApAttachedCount=_MwTopoApAttachedCount_Object((1,3,6,1,4,1,15983,1,1,4,13,4,1,4),_MwTopoApAttachedCount_Type())
mwTopoApAttachedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTopoApAttachedCount.setStatus(_A)
_MwTopoApAssignedCount_Type=Unsigned32
_MwTopoApAssignedCount_Object=MibTableColumn
mwTopoApAssignedCount=_MwTopoApAssignedCount_Object((1,3,6,1,4,1,15983,1,1,4,13,4,1,5),_MwTopoApAssignedCount_Type())
mwTopoApAssignedCount.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTopoApAssignedCount.setStatus(_A)
_MwTopoApNeighborsCount_Type=Unsigned32
_MwTopoApNeighborsCount_Object=MibTableColumn
mwTopoApNeighborsCount=_MwTopoApNeighborsCount_Object((1,3,6,1,4,1,15983,1,1,4,13,4,1,6),_MwTopoApNeighborsCount_Type())
mwTopoApNeighborsCount.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTopoApNeighborsCount.setStatus(_A)
_MwTopoApResourceRequest_Type=Unsigned32
_MwTopoApResourceRequest_Object=MibTableColumn
mwTopoApResourceRequest=_MwTopoApResourceRequest_Object((1,3,6,1,4,1,15983,1,1,4,13,4,1,7),_MwTopoApResourceRequest_Type())
mwTopoApResourceRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTopoApResourceRequest.setStatus(_A)
_MwTopoApResourceAllocated_Type=Unsigned32
_MwTopoApResourceAllocated_Object=MibTableColumn
mwTopoApResourceAllocated=_MwTopoApResourceAllocated_Object((1,3,6,1,4,1,15983,1,1,4,13,4,1,8),_MwTopoApResourceAllocated_Type())
mwTopoApResourceAllocated.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTopoApResourceAllocated.setStatus(_A)
_MwTopoApapTable_Object=MibTable
mwTopoApapTable=_MwTopoApapTable_Object((1,3,6,1,4,1,15983,1,1,4,13,5))
if mibBuilder.loadTexts:mwTopoApapTable.setStatus(_A)
_MwTopoApapEntry_Object=MibTableRow
mwTopoApapEntry=_MwTopoApapEntry_Object((1,3,6,1,4,1,15983,1,1,4,13,5,1))
mwTopoApapEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:mwTopoApapEntry.setStatus(_A)
_MwTopoApapTableIndex_Type=Integer32
_MwTopoApapTableIndex_Object=MibTableColumn
mwTopoApapTableIndex=_MwTopoApapTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,13,5,1,1),_MwTopoApapTableIndex_Type())
mwTopoApapTableIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mwTopoApapTableIndex.setStatus(_A)
_MwTopoApapHeadId_Type=Unsigned32
_MwTopoApapHeadId_Object=MibTableColumn
mwTopoApapHeadId=_MwTopoApapHeadId_Object((1,3,6,1,4,1,15983,1,1,4,13,5,1,2),_MwTopoApapHeadId_Type())
mwTopoApapHeadId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTopoApapHeadId.setStatus(_A)
_MwTopoApapTailId_Type=Unsigned32
_MwTopoApapTailId_Object=MibTableColumn
mwTopoApapTailId=_MwTopoApapTailId_Object((1,3,6,1,4,1,15983,1,1,4,13,5,1,3),_MwTopoApapTailId_Type())
mwTopoApapTailId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTopoApapTailId.setStatus(_A)
_MwTopoApapHeadName_Type=DisplayString
_MwTopoApapHeadName_Object=MibTableColumn
mwTopoApapHeadName=_MwTopoApapHeadName_Object((1,3,6,1,4,1,15983,1,1,4,13,5,1,4),_MwTopoApapHeadName_Type())
mwTopoApapHeadName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTopoApapHeadName.setStatus(_A)
_MwTopoApapTailName_Type=DisplayString
_MwTopoApapTailName_Object=MibTableColumn
mwTopoApapTailName=_MwTopoApapTailName_Object((1,3,6,1,4,1,15983,1,1,4,13,5,1,5),_MwTopoApapTailName_Type())
mwTopoApapTailName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTopoApapTailName.setStatus(_A)
_MwTopoStaTable_Object=MibTable
mwTopoStaTable=_MwTopoStaTable_Object((1,3,6,1,4,1,15983,1,1,4,13,6))
if mibBuilder.loadTexts:mwTopoStaTable.setStatus(_A)
_MwTopoStaEntry_Object=MibTableRow
mwTopoStaEntry=_MwTopoStaEntry_Object((1,3,6,1,4,1,15983,1,1,4,13,6,1))
mwTopoStaEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:mwTopoStaEntry.setStatus(_A)
_MwTopoStaTableIndex_Type=Integer32
_MwTopoStaTableIndex_Object=MibTableColumn
mwTopoStaTableIndex=_MwTopoStaTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,13,6,1,1),_MwTopoStaTableIndex_Type())
mwTopoStaTableIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mwTopoStaTableIndex.setStatus(_A)
_MwTopoStaBssId_Type=MacAddress
_MwTopoStaBssId_Object=MibTableColumn
mwTopoStaBssId=_MwTopoStaBssId_Object((1,3,6,1,4,1,15983,1,1,4,13,6,1,2),_MwTopoStaBssId_Type())
mwTopoStaBssId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTopoStaBssId.setStatus(_A)
_MwTopoStaMssId_Type=MacAddress
_MwTopoStaMssId_Object=MibTableColumn
mwTopoStaMssId=_MwTopoStaMssId_Object((1,3,6,1,4,1,15983,1,1,4,13,6,1,3),_MwTopoStaMssId_Type())
mwTopoStaMssId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTopoStaMssId.setStatus(_A)
_MwTopoStaMacAddress_Type=MacAddress
_MwTopoStaMacAddress_Object=MibTableColumn
mwTopoStaMacAddress=_MwTopoStaMacAddress_Object((1,3,6,1,4,1,15983,1,1,4,13,6,1,4),_MwTopoStaMacAddress_Type())
mwTopoStaMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTopoStaMacAddress.setStatus(_A)
_MwTopoStaAssocState_Type=MwlAssociationState
_MwTopoStaAssocState_Object=MibTableColumn
mwTopoStaAssocState=_MwTopoStaAssocState_Object((1,3,6,1,4,1,15983,1,1,4,13,6,1,5),_MwTopoStaAssocState_Type())
mwTopoStaAssocState.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTopoStaAssocState.setStatus(_A)
_MwTopoStaAssignedAp_Type=Unsigned32
_MwTopoStaAssignedAp_Object=MibTableColumn
mwTopoStaAssignedAp=_MwTopoStaAssignedAp_Object((1,3,6,1,4,1,15983,1,1,4,13,6,1,6),_MwTopoStaAssignedAp_Type())
mwTopoStaAssignedAp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTopoStaAssignedAp.setStatus(_A)
_MwTopoStaHandoffTime_Type=DateAndTime
_MwTopoStaHandoffTime_Object=MibTableColumn
mwTopoStaHandoffTime=_MwTopoStaHandoffTime_Object((1,3,6,1,4,1,15983,1,1,4,13,6,1,7),_MwTopoStaHandoffTime_Type())
mwTopoStaHandoffTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTopoStaHandoffTime.setStatus(_A)
_MwTopoStaLastActiveTime_Type=DateAndTime
_MwTopoStaLastActiveTime_Object=MibTableColumn
mwTopoStaLastActiveTime=_MwTopoStaLastActiveTime_Object((1,3,6,1,4,1,15983,1,1,4,13,6,1,8),_MwTopoStaLastActiveTime_Type())
mwTopoStaLastActiveTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTopoStaLastActiveTime.setStatus(_A)
_MwTopoStaAssignedApName_Type=DisplayString
_MwTopoStaAssignedApName_Object=MibTableColumn
mwTopoStaAssignedApName=_MwTopoStaAssignedApName_Object((1,3,6,1,4,1,15983,1,1,4,13,6,1,9),_MwTopoStaAssignedApName_Type())
mwTopoStaAssignedApName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTopoStaAssignedApName.setStatus(_A)
_MwTopoStaapTable_Object=MibTable
mwTopoStaapTable=_MwTopoStaapTable_Object((1,3,6,1,4,1,15983,1,1,4,13,7))
if mibBuilder.loadTexts:mwTopoStaapTable.setStatus(_A)
_MwTopoStaapEntry_Object=MibTableRow
mwTopoStaapEntry=_MwTopoStaapEntry_Object((1,3,6,1,4,1,15983,1,1,4,13,7,1))
mwTopoStaapEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:mwTopoStaapEntry.setStatus(_A)
_MwTopoStaapTableIndex_Type=Integer32
_MwTopoStaapTableIndex_Object=MibTableColumn
mwTopoStaapTableIndex=_MwTopoStaapTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,13,7,1,1),_MwTopoStaapTableIndex_Type())
mwTopoStaapTableIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mwTopoStaapTableIndex.setStatus(_A)
_MwTopoStaapRssi_Type=Integer32
_MwTopoStaapRssi_Object=MibTableColumn
mwTopoStaapRssi=_MwTopoStaapRssi_Object((1,3,6,1,4,1,15983,1,1,4,13,7,1,2),_MwTopoStaapRssi_Type())
mwTopoStaapRssi.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTopoStaapRssi.setStatus(_A)
_MwTopoStaapStaId_Type=MacAddress
_MwTopoStaapStaId_Object=MibTableColumn
mwTopoStaapStaId=_MwTopoStaapStaId_Object((1,3,6,1,4,1,15983,1,1,4,13,7,1,3),_MwTopoStaapStaId_Type())
mwTopoStaapStaId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTopoStaapStaId.setStatus(_A)
_MwTopoStaapApId_Type=Unsigned32
_MwTopoStaapApId_Object=MibTableColumn
mwTopoStaapApId=_MwTopoStaapApId_Object((1,3,6,1,4,1,15983,1,1,4,13,7,1,4),_MwTopoStaapApId_Type())
mwTopoStaapApId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTopoStaapApId.setStatus(_A)
_MwTopoStaapApName_Type=DisplayString
_MwTopoStaapApName_Object=MibTableColumn
mwTopoStaapApName=_MwTopoStaapApName_Object((1,3,6,1,4,1,15983,1,1,4,13,7,1,5),_MwTopoStaapApName_Type())
mwTopoStaapApName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTopoStaapApName.setStatus(_A)
_MwTopoStaapAssigned_Type=MwlOnOffSwitch
_MwTopoStaapAssigned_Object=MibTableColumn
mwTopoStaapAssigned=_MwTopoStaapAssigned_Object((1,3,6,1,4,1,15983,1,1,4,13,7,1,6),_MwTopoStaapAssigned_Type())
mwTopoStaapAssigned.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTopoStaapAssigned.setStatus(_A)
_MwApNeighborTable_Object=MibTable
mwApNeighborTable=_MwApNeighborTable_Object((1,3,6,1,4,1,15983,1,1,4,13,8))
if mibBuilder.loadTexts:mwApNeighborTable.setStatus(_A)
_MwApNeighborEntry_Object=MibTableRow
mwApNeighborEntry=_MwApNeighborEntry_Object((1,3,6,1,4,1,15983,1,1,4,13,8,1))
mwApNeighborEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:mwApNeighborEntry.setStatus(_A)
_MwApNeighborTableIndex_Type=Integer32
_MwApNeighborTableIndex_Object=MibTableColumn
mwApNeighborTableIndex=_MwApNeighborTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,13,8,1,1),_MwApNeighborTableIndex_Type())
mwApNeighborTableIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mwApNeighborTableIndex.setStatus(_A)
_MwApNeighborNmsApNodeId_Type=Integer32
_MwApNeighborNmsApNodeId_Object=MibTableColumn
mwApNeighborNmsApNodeId=_MwApNeighborNmsApNodeId_Object((1,3,6,1,4,1,15983,1,1,4,13,8,1,2),_MwApNeighborNmsApNodeId_Type())
mwApNeighborNmsApNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApNeighborNmsApNodeId.setStatus(_A)
_MwApNeighborNmsApInterfaceId_Type=Integer32
_MwApNeighborNmsApInterfaceId_Object=MibTableColumn
mwApNeighborNmsApInterfaceId=_MwApNeighborNmsApInterfaceId_Object((1,3,6,1,4,1,15983,1,1,4,13,8,1,3),_MwApNeighborNmsApInterfaceId_Type())
mwApNeighborNmsApInterfaceId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApNeighborNmsApInterfaceId.setStatus(_A)
_MwApNeighborApMac_Type=MacAddress
_MwApNeighborApMac_Object=MibTableColumn
mwApNeighborApMac=_MwApNeighborApMac_Object((1,3,6,1,4,1,15983,1,1,4,13,8,1,4),_MwApNeighborApMac_Type())
mwApNeighborApMac.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApNeighborApMac.setStatus(_A)
_MwApNeighborChannel_Type=Unsigned32
_MwApNeighborChannel_Object=MibTableColumn
mwApNeighborChannel=_MwApNeighborChannel_Object((1,3,6,1,4,1,15983,1,1,4,13,8,1,5),_MwApNeighborChannel_Type())
mwApNeighborChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApNeighborChannel.setStatus(_A)
_MwApNeighborNeighborApId_Type=Integer32
_MwApNeighborNeighborApId_Object=MibTableColumn
mwApNeighborNeighborApId=_MwApNeighborNeighborApId_Object((1,3,6,1,4,1,15983,1,1,4,13,8,1,6),_MwApNeighborNeighborApId_Type())
mwApNeighborNeighborApId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApNeighborNeighborApId.setStatus(_A)
_MwApNeighborNeighborApMac_Type=MacAddress
_MwApNeighborNeighborApMac_Object=MibTableColumn
mwApNeighborNeighborApMac=_MwApNeighborNeighborApMac_Object((1,3,6,1,4,1,15983,1,1,4,13,8,1,7),_MwApNeighborNeighborApMac_Type())
mwApNeighborNeighborApMac.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApNeighborNeighborApMac.setStatus(_A)
_MwApNeighborNeighborApControllerIndex_Type=Integer32
_MwApNeighborNeighborApControllerIndex_Object=MibTableColumn
mwApNeighborNeighborApControllerIndex=_MwApNeighborNeighborApControllerIndex_Object((1,3,6,1,4,1,15983,1,1,4,13,8,1,8),_MwApNeighborNeighborApControllerIndex_Type())
mwApNeighborNeighborApControllerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApNeighborNeighborApControllerIndex.setStatus(_A)
_MwApNeighborNeighborApCurrentRssi_Type=Integer32
_MwApNeighborNeighborApCurrentRssi_Object=MibTableColumn
mwApNeighborNeighborApCurrentRssi=_MwApNeighborNeighborApCurrentRssi_Object((1,3,6,1,4,1,15983,1,1,4,13,8,1,9),_MwApNeighborNeighborApCurrentRssi_Type())
mwApNeighborNeighborApCurrentRssi.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApNeighborNeighborApCurrentRssi.setStatus(_A)
_MwApNeighborDetailsTable_Object=MibTable
mwApNeighborDetailsTable=_MwApNeighborDetailsTable_Object((1,3,6,1,4,1,15983,1,1,4,13,9))
if mibBuilder.loadTexts:mwApNeighborDetailsTable.setStatus(_A)
_MwApNeighborDetailsEntry_Object=MibTableRow
mwApNeighborDetailsEntry=_MwApNeighborDetailsEntry_Object((1,3,6,1,4,1,15983,1,1,4,13,9,1))
mwApNeighborDetailsEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:mwApNeighborDetailsEntry.setStatus(_A)
_MwApNeighborDetailsTableIndex_Type=Integer32
_MwApNeighborDetailsTableIndex_Object=MibTableColumn
mwApNeighborDetailsTableIndex=_MwApNeighborDetailsTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,13,9,1,1),_MwApNeighborDetailsTableIndex_Type())
mwApNeighborDetailsTableIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mwApNeighborDetailsTableIndex.setStatus(_A)
_MwApNeighborDetailsNmsApNodeId_Type=Integer32
_MwApNeighborDetailsNmsApNodeId_Object=MibTableColumn
mwApNeighborDetailsNmsApNodeId=_MwApNeighborDetailsNmsApNodeId_Object((1,3,6,1,4,1,15983,1,1,4,13,9,1,2),_MwApNeighborDetailsNmsApNodeId_Type())
mwApNeighborDetailsNmsApNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApNeighborDetailsNmsApNodeId.setStatus(_A)
_MwApNeighborDetailsNmsApInterfaceId_Type=Integer32
_MwApNeighborDetailsNmsApInterfaceId_Object=MibTableColumn
mwApNeighborDetailsNmsApInterfaceId=_MwApNeighborDetailsNmsApInterfaceId_Object((1,3,6,1,4,1,15983,1,1,4,13,9,1,3),_MwApNeighborDetailsNmsApInterfaceId_Type())
mwApNeighborDetailsNmsApInterfaceId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApNeighborDetailsNmsApInterfaceId.setStatus(_A)
_MwApNeighborDetailsChannel_Type=Unsigned32
_MwApNeighborDetailsChannel_Object=MibTableColumn
mwApNeighborDetailsChannel=_MwApNeighborDetailsChannel_Object((1,3,6,1,4,1,15983,1,1,4,13,9,1,4),_MwApNeighborDetailsChannel_Type())
mwApNeighborDetailsChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApNeighborDetailsChannel.setStatus(_A)
_MwApNeighborDetailsLocalAp_Type=Integer32
_MwApNeighborDetailsLocalAp_Object=MibTableColumn
mwApNeighborDetailsLocalAp=_MwApNeighborDetailsLocalAp_Object((1,3,6,1,4,1,15983,1,1,4,13,9,1,5),_MwApNeighborDetailsLocalAp_Type())
mwApNeighborDetailsLocalAp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApNeighborDetailsLocalAp.setStatus(_A)
_MwApNeighborDetailsRemoteAp_Type=Integer32
_MwApNeighborDetailsRemoteAp_Object=MibTableColumn
mwApNeighborDetailsRemoteAp=_MwApNeighborDetailsRemoteAp_Object((1,3,6,1,4,1,15983,1,1,4,13,9,1,6),_MwApNeighborDetailsRemoteAp_Type())
mwApNeighborDetailsRemoteAp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApNeighborDetailsRemoteAp.setStatus(_A)
_MwApNeighborDetailsRssiLevel1_Type=Integer32
_MwApNeighborDetailsRssiLevel1_Object=MibTableColumn
mwApNeighborDetailsRssiLevel1=_MwApNeighborDetailsRssiLevel1_Object((1,3,6,1,4,1,15983,1,1,4,13,9,1,7),_MwApNeighborDetailsRssiLevel1_Type())
mwApNeighborDetailsRssiLevel1.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApNeighborDetailsRssiLevel1.setStatus(_A)
_MwApNeighborDetailsRssiLevel2_Type=Integer32
_MwApNeighborDetailsRssiLevel2_Object=MibTableColumn
mwApNeighborDetailsRssiLevel2=_MwApNeighborDetailsRssiLevel2_Object((1,3,6,1,4,1,15983,1,1,4,13,9,1,8),_MwApNeighborDetailsRssiLevel2_Type())
mwApNeighborDetailsRssiLevel2.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApNeighborDetailsRssiLevel2.setStatus(_A)
_MwApNeighborDetailsRssiLevel3_Type=Integer32
_MwApNeighborDetailsRssiLevel3_Object=MibTableColumn
mwApNeighborDetailsRssiLevel3=_MwApNeighborDetailsRssiLevel3_Object((1,3,6,1,4,1,15983,1,1,4,13,9,1,9),_MwApNeighborDetailsRssiLevel3_Type())
mwApNeighborDetailsRssiLevel3.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApNeighborDetailsRssiLevel3.setStatus(_A)
_MwApNeighborDetailsRssiLevel4_Type=Integer32
_MwApNeighborDetailsRssiLevel4_Object=MibTableColumn
mwApNeighborDetailsRssiLevel4=_MwApNeighborDetailsRssiLevel4_Object((1,3,6,1,4,1,15983,1,1,4,13,9,1,10),_MwApNeighborDetailsRssiLevel4_Type())
mwApNeighborDetailsRssiLevel4.setMaxAccess(_B)
if mibBuilder.loadTexts:mwApNeighborDetailsRssiLevel4.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'mwTopology':mwTopology,'mwApAssignedTable':mwApAssignedTable,'mwApAssignedEntry':mwApAssignedEntry,_E:mwApAssignedTableIndex,'mwApAssignedApMac':mwApAssignedApMac,'mwApAssignedEssid':mwApAssignedEssid,'mwApAssigneddbState':mwApAssigneddbState,'mwApAssignedPrevRssi':mwApAssignedPrevRssi,'mwApAssignedRxPackets':mwApAssignedRxPackets,'mwApAssignedTxPackets':mwApAssignedTxPackets,'mwApAssignedRadioType':mwApAssignedRadioType,'mwApAssignedAuthKeyType':mwApAssignedAuthKeyType,'mwApAssignedCurrentRssi':mwApAssignedCurrentRssi,'mwApAssignedNmsApNodeId':mwApAssignedNmsApNodeId,'mwApAssignedApDeviceType':mwApAssignedApDeviceType,'mwApAssignedLastActivity':mwApAssignedLastActivity,'mwApAssignedNmsApNodeName':mwApAssignedNmsApNodeName,'mwApAssignedVirtualPort':mwApAssignedVirtualPort,'mwApAssignedCapabilities':mwApAssignedCapabilities,'mwApDiscoveredTable':mwApDiscoveredTable,'mwApDiscoveredEntry':mwApDiscoveredEntry,_F:mwApDiscoveredTableIndex,'mwApDiscoveredApMac':mwApDiscoveredApMac,'mwApDiscoveredEssid':mwApDiscoveredEssid,'mwApDiscoveredBssid':mwApDiscoveredBssid,'mwApDiscoveredChannel':mwApDiscoveredChannel,'mwApDiscoveredPrevRssi':mwApDiscoveredPrevRssi,'mwApDiscoveredRxPackets':mwApDiscoveredRxPackets,'mwApDiscoveredRadioType':mwApDiscoveredRadioType,'mwApDiscoveredWiredRogue':mwApDiscoveredWiredRogue,'mwApDiscoveredCurrentRssi':mwApDiscoveredCurrentRssi,'mwApDiscoveredNmsApNodeId':mwApDiscoveredNmsApNodeId,'mwApDiscoveredApDeviceType':mwApDiscoveredApDeviceType,'mwApDiscoveredLastActivity':mwApDiscoveredLastActivity,'mwApDiscoveredNmsApNodeName':mwApDiscoveredNmsApNodeName,'mwApDiscoveredConfirmedChannel':mwApDiscoveredConfirmedChannel,'mwTopoApTable':mwTopoApTable,'mwTopoApEntry':mwTopoApEntry,_G:mwTopoApTableIndex,'mwTopoApNodeId':mwTopoApNodeId,'mwTopoApNodeName':mwTopoApNodeName,'mwTopoApAttachedCount':mwTopoApAttachedCount,'mwTopoApAssignedCount':mwTopoApAssignedCount,'mwTopoApNeighborsCount':mwTopoApNeighborsCount,'mwTopoApResourceRequest':mwTopoApResourceRequest,'mwTopoApResourceAllocated':mwTopoApResourceAllocated,'mwTopoApapTable':mwTopoApapTable,'mwTopoApapEntry':mwTopoApapEntry,_H:mwTopoApapTableIndex,'mwTopoApapHeadId':mwTopoApapHeadId,'mwTopoApapTailId':mwTopoApapTailId,'mwTopoApapHeadName':mwTopoApapHeadName,'mwTopoApapTailName':mwTopoApapTailName,'mwTopoStaTable':mwTopoStaTable,'mwTopoStaEntry':mwTopoStaEntry,_I:mwTopoStaTableIndex,'mwTopoStaBssId':mwTopoStaBssId,'mwTopoStaMssId':mwTopoStaMssId,'mwTopoStaMacAddress':mwTopoStaMacAddress,'mwTopoStaAssocState':mwTopoStaAssocState,'mwTopoStaAssignedAp':mwTopoStaAssignedAp,'mwTopoStaHandoffTime':mwTopoStaHandoffTime,'mwTopoStaLastActiveTime':mwTopoStaLastActiveTime,'mwTopoStaAssignedApName':mwTopoStaAssignedApName,'mwTopoStaapTable':mwTopoStaapTable,'mwTopoStaapEntry':mwTopoStaapEntry,_J:mwTopoStaapTableIndex,'mwTopoStaapRssi':mwTopoStaapRssi,'mwTopoStaapStaId':mwTopoStaapStaId,'mwTopoStaapApId':mwTopoStaapApId,'mwTopoStaapApName':mwTopoStaapApName,'mwTopoStaapAssigned':mwTopoStaapAssigned,'mwApNeighborTable':mwApNeighborTable,'mwApNeighborEntry':mwApNeighborEntry,_K:mwApNeighborTableIndex,'mwApNeighborNmsApNodeId':mwApNeighborNmsApNodeId,'mwApNeighborNmsApInterfaceId':mwApNeighborNmsApInterfaceId,'mwApNeighborApMac':mwApNeighborApMac,'mwApNeighborChannel':mwApNeighborChannel,'mwApNeighborNeighborApId':mwApNeighborNeighborApId,'mwApNeighborNeighborApMac':mwApNeighborNeighborApMac,'mwApNeighborNeighborApControllerIndex':mwApNeighborNeighborApControllerIndex,'mwApNeighborNeighborApCurrentRssi':mwApNeighborNeighborApCurrentRssi,'mwApNeighborDetailsTable':mwApNeighborDetailsTable,'mwApNeighborDetailsEntry':mwApNeighborDetailsEntry,_L:mwApNeighborDetailsTableIndex,'mwApNeighborDetailsNmsApNodeId':mwApNeighborDetailsNmsApNodeId,'mwApNeighborDetailsNmsApInterfaceId':mwApNeighborDetailsNmsApInterfaceId,'mwApNeighborDetailsChannel':mwApNeighborDetailsChannel,'mwApNeighborDetailsLocalAp':mwApNeighborDetailsLocalAp,'mwApNeighborDetailsRemoteAp':mwApNeighborDetailsRemoteAp,'mwApNeighborDetailsRssiLevel1':mwApNeighborDetailsRssiLevel1,'mwApNeighborDetailsRssiLevel2':mwApNeighborDetailsRssiLevel2,'mwApNeighborDetailsRssiLevel3':mwApNeighborDetailsRssiLevel3,'mwApNeighborDetailsRssiLevel4':mwApNeighborDetailsRssiLevel4})