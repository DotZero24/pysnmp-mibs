_H='mwTop10ApRxtxTableIndex'
_G='mwTop10ApProblemTableIndex'
_F='mwTop10ApStationRxtxTableIndex'
_E='mwTop10ApStationProblemTableIndex'
_D='not-accessible'
_C='MERU-TOP10-STATISTICS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
mwStatistics,=mibBuilder.importSymbols('MERU-SMI','mwStatistics')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp','TruthValue')
mwTop10Statistics=ModuleIdentity((1,3,6,1,4,1,15983,1,1,3,2))
_MwTop10ApStationProblemTable_Object=MibTable
mwTop10ApStationProblemTable=_MwTop10ApStationProblemTable_Object((1,3,6,1,4,1,15983,1,1,3,2,1))
if mibBuilder.loadTexts:mwTop10ApStationProblemTable.setStatus(_A)
_MwTop10ApStationProblemEntry_Object=MibTableRow
mwTop10ApStationProblemEntry=_MwTop10ApStationProblemEntry_Object((1,3,6,1,4,1,15983,1,1,3,2,1,1))
mwTop10ApStationProblemEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:mwTop10ApStationProblemEntry.setStatus(_A)
_MwTop10ApStationProblemTableIndex_Type=Integer32
_MwTop10ApStationProblemTableIndex_Object=MibTableColumn
mwTop10ApStationProblemTableIndex=_MwTop10ApStationProblemTableIndex_Object((1,3,6,1,4,1,15983,1,1,3,2,1,1,1),_MwTop10ApStationProblemTableIndex_Type())
mwTop10ApStationProblemTableIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mwTop10ApStationProblemTableIndex.setStatus(_A)
_MwTop10ApStationProblemApName_Type=DisplayString
_MwTop10ApStationProblemApName_Object=MibTableColumn
mwTop10ApStationProblemApName=_MwTop10ApStationProblemApName_Object((1,3,6,1,4,1,15983,1,1,3,2,1,1,2),_MwTop10ApStationProblemApName_Type())
mwTop10ApStationProblemApName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTop10ApStationProblemApName.setStatus(_A)
_MwTop10ApStationProblemIfIndex_Type=Integer32
_MwTop10ApStationProblemIfIndex_Object=MibTableColumn
mwTop10ApStationProblemIfIndex=_MwTop10ApStationProblemIfIndex_Object((1,3,6,1,4,1,15983,1,1,3,2,1,1,3),_MwTop10ApStationProblemIfIndex_Type())
mwTop10ApStationProblemIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTop10ApStationProblemIfIndex.setStatus(_A)
_MwTop10ApStationProblemWepErrors_Type=Unsigned32
_MwTop10ApStationProblemWepErrors_Object=MibTableColumn
mwTop10ApStationProblemWepErrors=_MwTop10ApStationProblemWepErrors_Object((1,3,6,1,4,1,15983,1,1,3,2,1,1,4),_MwTop10ApStationProblemWepErrors_Type())
mwTop10ApStationProblemWepErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTop10ApStationProblemWepErrors.setStatus(_A)
_MwTop10ApStationProblemNmsApNodeId_Type=Integer32
_MwTop10ApStationProblemNmsApNodeId_Object=MibTableColumn
mwTop10ApStationProblemNmsApNodeId=_MwTop10ApStationProblemNmsApNodeId_Object((1,3,6,1,4,1,15983,1,1,3,2,1,1,5),_MwTop10ApStationProblemNmsApNodeId_Type())
mwTop10ApStationProblemNmsApNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTop10ApStationProblemNmsApNodeId.setStatus(_A)
_MwTop10ApStationProblemStationIPAddress_Type=Ipv6Address
_MwTop10ApStationProblemStationIPAddress_Object=MibTableColumn
mwTop10ApStationProblemStationIPAddress=_MwTop10ApStationProblemStationIPAddress_Object((1,3,6,1,4,1,15983,1,1,3,2,1,1,6),_MwTop10ApStationProblemStationIPAddress_Type())
mwTop10ApStationProblemStationIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTop10ApStationProblemStationIPAddress.setStatus(_A)
_MwTop10ApStationProblemStationMacAddress_Type=MacAddress
_MwTop10ApStationProblemStationMacAddress_Object=MibTableColumn
mwTop10ApStationProblemStationMacAddress=_MwTop10ApStationProblemStationMacAddress_Object((1,3,6,1,4,1,15983,1,1,3,2,1,1,7),_MwTop10ApStationProblemStationMacAddress_Type())
mwTop10ApStationProblemStationMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTop10ApStationProblemStationMacAddress.setStatus(_A)
_MwTop10ApStationProblemStationIPv4Address_Type=IpAddress
_MwTop10ApStationProblemStationIPv4Address_Object=MibTableColumn
mwTop10ApStationProblemStationIPv4Address=_MwTop10ApStationProblemStationIPv4Address_Object((1,3,6,1,4,1,15983,1,1,3,2,1,1,9),_MwTop10ApStationProblemStationIPv4Address_Type())
mwTop10ApStationProblemStationIPv4Address.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTop10ApStationProblemStationIPv4Address.setStatus(_A)
_MwTop10ApStationRxtxTable_Object=MibTable
mwTop10ApStationRxtxTable=_MwTop10ApStationRxtxTable_Object((1,3,6,1,4,1,15983,1,1,3,2,2))
if mibBuilder.loadTexts:mwTop10ApStationRxtxTable.setStatus(_A)
_MwTop10ApStationRxtxEntry_Object=MibTableRow
mwTop10ApStationRxtxEntry=_MwTop10ApStationRxtxEntry_Object((1,3,6,1,4,1,15983,1,1,3,2,2,1))
mwTop10ApStationRxtxEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:mwTop10ApStationRxtxEntry.setStatus(_A)
_MwTop10ApStationRxtxTableIndex_Type=Integer32
_MwTop10ApStationRxtxTableIndex_Object=MibTableColumn
mwTop10ApStationRxtxTableIndex=_MwTop10ApStationRxtxTableIndex_Object((1,3,6,1,4,1,15983,1,1,3,2,2,1,1),_MwTop10ApStationRxtxTableIndex_Type())
mwTop10ApStationRxtxTableIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mwTop10ApStationRxtxTableIndex.setStatus(_A)
_MwTop10ApStationRxtxApName_Type=DisplayString
_MwTop10ApStationRxtxApName_Object=MibTableColumn
mwTop10ApStationRxtxApName=_MwTop10ApStationRxtxApName_Object((1,3,6,1,4,1,15983,1,1,3,2,2,1,2),_MwTop10ApStationRxtxApName_Type())
mwTop10ApStationRxtxApName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTop10ApStationRxtxApName.setStatus(_A)
_MwTop10ApStationRxtxIfIndex_Type=Integer32
_MwTop10ApStationRxtxIfIndex_Object=MibTableColumn
mwTop10ApStationRxtxIfIndex=_MwTop10ApStationRxtxIfIndex_Object((1,3,6,1,4,1,15983,1,1,3,2,2,1,3),_MwTop10ApStationRxtxIfIndex_Type())
mwTop10ApStationRxtxIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTop10ApStationRxtxIfIndex.setStatus(_A)
_MwTop10ApStationRxtxNmsApNodeId_Type=Integer32
_MwTop10ApStationRxtxNmsApNodeId_Object=MibTableColumn
mwTop10ApStationRxtxNmsApNodeId=_MwTop10ApStationRxtxNmsApNodeId_Object((1,3,6,1,4,1,15983,1,1,3,2,2,1,4),_MwTop10ApStationRxtxNmsApNodeId_Type())
mwTop10ApStationRxtxNmsApNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTop10ApStationRxtxNmsApNodeId.setStatus(_A)
_MwTop10ApStationRxtxRxPacketCount_Type=Unsigned32
_MwTop10ApStationRxtxRxPacketCount_Object=MibTableColumn
mwTop10ApStationRxtxRxPacketCount=_MwTop10ApStationRxtxRxPacketCount_Object((1,3,6,1,4,1,15983,1,1,3,2,2,1,5),_MwTop10ApStationRxtxRxPacketCount_Type())
mwTop10ApStationRxtxRxPacketCount.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTop10ApStationRxtxRxPacketCount.setStatus(_A)
_MwTop10ApStationRxtxTxPacketCount_Type=Unsigned32
_MwTop10ApStationRxtxTxPacketCount_Object=MibTableColumn
mwTop10ApStationRxtxTxPacketCount=_MwTop10ApStationRxtxTxPacketCount_Object((1,3,6,1,4,1,15983,1,1,3,2,2,1,6),_MwTop10ApStationRxtxTxPacketCount_Type())
mwTop10ApStationRxtxTxPacketCount.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTop10ApStationRxtxTxPacketCount.setStatus(_A)
_MwTop10ApStationRxtxStationIPAddress_Type=Ipv6Address
_MwTop10ApStationRxtxStationIPAddress_Object=MibTableColumn
mwTop10ApStationRxtxStationIPAddress=_MwTop10ApStationRxtxStationIPAddress_Object((1,3,6,1,4,1,15983,1,1,3,2,2,1,7),_MwTop10ApStationRxtxStationIPAddress_Type())
mwTop10ApStationRxtxStationIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTop10ApStationRxtxStationIPAddress.setStatus(_A)
_MwTop10ApStationRxtxStationMacAddress_Type=MacAddress
_MwTop10ApStationRxtxStationMacAddress_Object=MibTableColumn
mwTop10ApStationRxtxStationMacAddress=_MwTop10ApStationRxtxStationMacAddress_Object((1,3,6,1,4,1,15983,1,1,3,2,2,1,8),_MwTop10ApStationRxtxStationMacAddress_Type())
mwTop10ApStationRxtxStationMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTop10ApStationRxtxStationMacAddress.setStatus(_A)
_MwTop10ApStationRxtxStationIPv4Address_Type=IpAddress
_MwTop10ApStationRxtxStationIPv4Address_Object=MibTableColumn
mwTop10ApStationRxtxStationIPv4Address=_MwTop10ApStationRxtxStationIPv4Address_Object((1,3,6,1,4,1,15983,1,1,3,2,2,1,9),_MwTop10ApStationRxtxStationIPv4Address_Type())
mwTop10ApStationRxtxStationIPv4Address.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTop10ApStationRxtxStationIPv4Address.setStatus(_A)
_MwTop10ApProblemTable_Object=MibTable
mwTop10ApProblemTable=_MwTop10ApProblemTable_Object((1,3,6,1,4,1,15983,1,1,3,2,3))
if mibBuilder.loadTexts:mwTop10ApProblemTable.setStatus(_A)
_MwTop10ApProblemEntry_Object=MibTableRow
mwTop10ApProblemEntry=_MwTop10ApProblemEntry_Object((1,3,6,1,4,1,15983,1,1,3,2,3,1))
mwTop10ApProblemEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:mwTop10ApProblemEntry.setStatus(_A)
_MwTop10ApProblemTableIndex_Type=Integer32
_MwTop10ApProblemTableIndex_Object=MibTableColumn
mwTop10ApProblemTableIndex=_MwTop10ApProblemTableIndex_Object((1,3,6,1,4,1,15983,1,1,3,2,3,1,1),_MwTop10ApProblemTableIndex_Type())
mwTop10ApProblemTableIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mwTop10ApProblemTableIndex.setStatus(_A)
_MwTop10ApProblemApName_Type=DisplayString
_MwTop10ApProblemApName_Object=MibTableColumn
mwTop10ApProblemApName=_MwTop10ApProblemApName_Object((1,3,6,1,4,1,15983,1,1,3,2,3,1,2),_MwTop10ApProblemApName_Type())
mwTop10ApProblemApName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTop10ApProblemApName.setStatus(_A)
_MwTop10ApProblemTxLoss_Type=Unsigned32
_MwTop10ApProblemTxLoss_Object=MibTableColumn
mwTop10ApProblemTxLoss=_MwTop10ApProblemTxLoss_Object((1,3,6,1,4,1,15983,1,1,3,2,3,1,3),_MwTop10ApProblemTxLoss_Type())
mwTop10ApProblemTxLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTop10ApProblemTxLoss.setStatus(_A)
_MwTop10ApProblemIfIndex_Type=Integer32
_MwTop10ApProblemIfIndex_Object=MibTableColumn
mwTop10ApProblemIfIndex=_MwTop10ApProblemIfIndex_Object((1,3,6,1,4,1,15983,1,1,3,2,3,1,4),_MwTop10ApProblemIfIndex_Type())
mwTop10ApProblemIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTop10ApProblemIfIndex.setStatus(_A)
_MwTop10ApProblemNmsApNodeId_Type=Integer32
_MwTop10ApProblemNmsApNodeId_Object=MibTableColumn
mwTop10ApProblemNmsApNodeId=_MwTop10ApProblemNmsApNodeId_Object((1,3,6,1,4,1,15983,1,1,3,2,3,1,5),_MwTop10ApProblemNmsApNodeId_Type())
mwTop10ApProblemNmsApNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTop10ApProblemNmsApNodeId.setStatus(_A)
_MwTop10ApRxtxTable_Object=MibTable
mwTop10ApRxtxTable=_MwTop10ApRxtxTable_Object((1,3,6,1,4,1,15983,1,1,3,2,4))
if mibBuilder.loadTexts:mwTop10ApRxtxTable.setStatus(_A)
_MwTop10ApRxtxEntry_Object=MibTableRow
mwTop10ApRxtxEntry=_MwTop10ApRxtxEntry_Object((1,3,6,1,4,1,15983,1,1,3,2,4,1))
mwTop10ApRxtxEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:mwTop10ApRxtxEntry.setStatus(_A)
_MwTop10ApRxtxTableIndex_Type=Integer32
_MwTop10ApRxtxTableIndex_Object=MibTableColumn
mwTop10ApRxtxTableIndex=_MwTop10ApRxtxTableIndex_Object((1,3,6,1,4,1,15983,1,1,3,2,4,1,1),_MwTop10ApRxtxTableIndex_Type())
mwTop10ApRxtxTableIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:mwTop10ApRxtxTableIndex.setStatus(_A)
_MwTop10ApRxtxApName_Type=DisplayString
_MwTop10ApRxtxApName_Object=MibTableColumn
mwTop10ApRxtxApName=_MwTop10ApRxtxApName_Object((1,3,6,1,4,1,15983,1,1,3,2,4,1,2),_MwTop10ApRxtxApName_Type())
mwTop10ApRxtxApName.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTop10ApRxtxApName.setStatus(_A)
_MwTop10ApRxtxIfIndex_Type=Integer32
_MwTop10ApRxtxIfIndex_Object=MibTableColumn
mwTop10ApRxtxIfIndex=_MwTop10ApRxtxIfIndex_Object((1,3,6,1,4,1,15983,1,1,3,2,4,1,3),_MwTop10ApRxtxIfIndex_Type())
mwTop10ApRxtxIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTop10ApRxtxIfIndex.setStatus(_A)
_MwTop10ApRxtxNmsApNodeId_Type=Integer32
_MwTop10ApRxtxNmsApNodeId_Object=MibTableColumn
mwTop10ApRxtxNmsApNodeId=_MwTop10ApRxtxNmsApNodeId_Object((1,3,6,1,4,1,15983,1,1,3,2,4,1,4),_MwTop10ApRxtxNmsApNodeId_Type())
mwTop10ApRxtxNmsApNodeId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTop10ApRxtxNmsApNodeId.setStatus(_A)
_MwTop10ApRxtxTxFrameCount_Type=Unsigned32
_MwTop10ApRxtxTxFrameCount_Object=MibTableColumn
mwTop10ApRxtxTxFrameCount=_MwTop10ApRxtxTxFrameCount_Object((1,3,6,1,4,1,15983,1,1,3,2,4,1,5),_MwTop10ApRxtxTxFrameCount_Type())
mwTop10ApRxtxTxFrameCount.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTop10ApRxtxTxFrameCount.setStatus(_A)
_MwTop10ApRxtxRxUnicastFrameCount_Type=Unsigned32
_MwTop10ApRxtxRxUnicastFrameCount_Object=MibTableColumn
mwTop10ApRxtxRxUnicastFrameCount=_MwTop10ApRxtxRxUnicastFrameCount_Object((1,3,6,1,4,1,15983,1,1,3,2,4,1,6),_MwTop10ApRxtxRxUnicastFrameCount_Type())
mwTop10ApRxtxRxUnicastFrameCount.setMaxAccess(_B)
if mibBuilder.loadTexts:mwTop10ApRxtxRxUnicastFrameCount.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'mwTop10Statistics':mwTop10Statistics,'mwTop10ApStationProblemTable':mwTop10ApStationProblemTable,'mwTop10ApStationProblemEntry':mwTop10ApStationProblemEntry,_E:mwTop10ApStationProblemTableIndex,'mwTop10ApStationProblemApName':mwTop10ApStationProblemApName,'mwTop10ApStationProblemIfIndex':mwTop10ApStationProblemIfIndex,'mwTop10ApStationProblemWepErrors':mwTop10ApStationProblemWepErrors,'mwTop10ApStationProblemNmsApNodeId':mwTop10ApStationProblemNmsApNodeId,'mwTop10ApStationProblemStationIPAddress':mwTop10ApStationProblemStationIPAddress,'mwTop10ApStationProblemStationMacAddress':mwTop10ApStationProblemStationMacAddress,'mwTop10ApStationProblemStationIPv4Address':mwTop10ApStationProblemStationIPv4Address,'mwTop10ApStationRxtxTable':mwTop10ApStationRxtxTable,'mwTop10ApStationRxtxEntry':mwTop10ApStationRxtxEntry,_F:mwTop10ApStationRxtxTableIndex,'mwTop10ApStationRxtxApName':mwTop10ApStationRxtxApName,'mwTop10ApStationRxtxIfIndex':mwTop10ApStationRxtxIfIndex,'mwTop10ApStationRxtxNmsApNodeId':mwTop10ApStationRxtxNmsApNodeId,'mwTop10ApStationRxtxRxPacketCount':mwTop10ApStationRxtxRxPacketCount,'mwTop10ApStationRxtxTxPacketCount':mwTop10ApStationRxtxTxPacketCount,'mwTop10ApStationRxtxStationIPAddress':mwTop10ApStationRxtxStationIPAddress,'mwTop10ApStationRxtxStationMacAddress':mwTop10ApStationRxtxStationMacAddress,'mwTop10ApStationRxtxStationIPv4Address':mwTop10ApStationRxtxStationIPv4Address,'mwTop10ApProblemTable':mwTop10ApProblemTable,'mwTop10ApProblemEntry':mwTop10ApProblemEntry,_G:mwTop10ApProblemTableIndex,'mwTop10ApProblemApName':mwTop10ApProblemApName,'mwTop10ApProblemTxLoss':mwTop10ApProblemTxLoss,'mwTop10ApProblemIfIndex':mwTop10ApProblemIfIndex,'mwTop10ApProblemNmsApNodeId':mwTop10ApProblemNmsApNodeId,'mwTop10ApRxtxTable':mwTop10ApRxtxTable,'mwTop10ApRxtxEntry':mwTop10ApRxtxEntry,_H:mwTop10ApRxtxTableIndex,'mwTop10ApRxtxApName':mwTop10ApRxtxApName,'mwTop10ApRxtxIfIndex':mwTop10ApRxtxIfIndex,'mwTop10ApRxtxNmsApNodeId':mwTop10ApRxtxNmsApNodeId,'mwTop10ApRxtxTxFrameCount':mwTop10ApRxtxTxFrameCount,'mwTop10ApRxtxRxUnicastFrameCount':mwTop10ApRxtxRxUnicastFrameCount})