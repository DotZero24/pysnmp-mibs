_Q='read-only'
_P='fsMplsHLSPEgressLSRId'
_O='fsMplsHLSPIngressLSRId'
_N='fsMplsHLSPInstance'
_M='fsMplsHLSPIndex'
_L='read-write'
_K='fsMplsLSPMapSubTunnelEgressLSRId'
_J='fsMplsLSPMapSubTunnelIngressLSRId'
_I='fsMplsLSPMapSubTunnelInstance'
_H='fsMplsLSPMapSubTunnelIndex'
_G='fsMplsLSPMapTunnelEgressLSRId'
_F='fsMplsLSPMapTunnelIngressLSRId'
_E='fsMplsLSPMapTunnelInstance'
_D='fsMplsLSPMapTunnelIndex'
_C='not-accessible'
_B='Aricent-MPLS-HLSP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
MplsExtendedTunnelId,MplsTunnelIndex,MplsTunnelInstanceIndex=mibBuilder.importSymbols('MPLS-TC-STD-MIB','MplsExtendedTunnelId','MplsTunnelIndex','MplsTunnelInstanceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fsHlspMIB=ModuleIdentity((1,3,6,1,4,1,29601,2,58))
if mibBuilder.loadTexts:fsHlspMIB.setRevisions(('2012-09-05 00:00',))
_FsMplsHlspConfigObjects_ObjectIdentity=ObjectIdentity
fsMplsHlspConfigObjects=_FsMplsHlspConfigObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,58,1))
_FsMplsLSPMapTunnelTable_Object=MibTable
fsMplsLSPMapTunnelTable=_FsMplsLSPMapTunnelTable_Object((1,3,6,1,4,1,29601,2,58,1,1))
if mibBuilder.loadTexts:fsMplsLSPMapTunnelTable.setStatus(_A)
_FsMplsLSPMapTunnelEntry_Object=MibTableRow
fsMplsLSPMapTunnelEntry=_FsMplsLSPMapTunnelEntry_Object((1,3,6,1,4,1,29601,2,58,1,1,1))
fsMplsLSPMapTunnelEntry.setIndexNames((0,_B,_D),(0,_B,_E),(0,_B,_F),(0,_B,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:fsMplsLSPMapTunnelEntry.setStatus(_A)
_FsMplsLSPMapTunnelIndex_Type=MplsTunnelIndex
_FsMplsLSPMapTunnelIndex_Object=MibTableColumn
fsMplsLSPMapTunnelIndex=_FsMplsLSPMapTunnelIndex_Object((1,3,6,1,4,1,29601,2,58,1,1,1,1),_FsMplsLSPMapTunnelIndex_Type())
fsMplsLSPMapTunnelIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsLSPMapTunnelIndex.setStatus(_A)
_FsMplsLSPMapTunnelInstance_Type=MplsTunnelInstanceIndex
_FsMplsLSPMapTunnelInstance_Object=MibTableColumn
fsMplsLSPMapTunnelInstance=_FsMplsLSPMapTunnelInstance_Object((1,3,6,1,4,1,29601,2,58,1,1,1,2),_FsMplsLSPMapTunnelInstance_Type())
fsMplsLSPMapTunnelInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsLSPMapTunnelInstance.setStatus(_A)
_FsMplsLSPMapTunnelIngressLSRId_Type=MplsExtendedTunnelId
_FsMplsLSPMapTunnelIngressLSRId_Object=MibTableColumn
fsMplsLSPMapTunnelIngressLSRId=_FsMplsLSPMapTunnelIngressLSRId_Object((1,3,6,1,4,1,29601,2,58,1,1,1,3),_FsMplsLSPMapTunnelIngressLSRId_Type())
fsMplsLSPMapTunnelIngressLSRId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsLSPMapTunnelIngressLSRId.setStatus(_A)
_FsMplsLSPMapTunnelEgressLSRId_Type=MplsExtendedTunnelId
_FsMplsLSPMapTunnelEgressLSRId_Object=MibTableColumn
fsMplsLSPMapTunnelEgressLSRId=_FsMplsLSPMapTunnelEgressLSRId_Object((1,3,6,1,4,1,29601,2,58,1,1,1,4),_FsMplsLSPMapTunnelEgressLSRId_Type())
fsMplsLSPMapTunnelEgressLSRId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsLSPMapTunnelEgressLSRId.setStatus(_A)
_FsMplsLSPMapSubTunnelIndex_Type=MplsTunnelIndex
_FsMplsLSPMapSubTunnelIndex_Object=MibTableColumn
fsMplsLSPMapSubTunnelIndex=_FsMplsLSPMapSubTunnelIndex_Object((1,3,6,1,4,1,29601,2,58,1,1,1,5),_FsMplsLSPMapSubTunnelIndex_Type())
fsMplsLSPMapSubTunnelIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsLSPMapSubTunnelIndex.setStatus(_A)
_FsMplsLSPMapSubTunnelInstance_Type=MplsTunnelInstanceIndex
_FsMplsLSPMapSubTunnelInstance_Object=MibTableColumn
fsMplsLSPMapSubTunnelInstance=_FsMplsLSPMapSubTunnelInstance_Object((1,3,6,1,4,1,29601,2,58,1,1,1,6),_FsMplsLSPMapSubTunnelInstance_Type())
fsMplsLSPMapSubTunnelInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsLSPMapSubTunnelInstance.setStatus(_A)
_FsMplsLSPMapSubTunnelIngressLSRId_Type=MplsExtendedTunnelId
_FsMplsLSPMapSubTunnelIngressLSRId_Object=MibTableColumn
fsMplsLSPMapSubTunnelIngressLSRId=_FsMplsLSPMapSubTunnelIngressLSRId_Object((1,3,6,1,4,1,29601,2,58,1,1,1,7),_FsMplsLSPMapSubTunnelIngressLSRId_Type())
fsMplsLSPMapSubTunnelIngressLSRId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsLSPMapSubTunnelIngressLSRId.setStatus(_A)
_FsMplsLSPMapSubTunnelEgressLSRId_Type=MplsExtendedTunnelId
_FsMplsLSPMapSubTunnelEgressLSRId_Object=MibTableColumn
fsMplsLSPMapSubTunnelEgressLSRId=_FsMplsLSPMapSubTunnelEgressLSRId_Object((1,3,6,1,4,1,29601,2,58,1,1,1,8),_FsMplsLSPMapSubTunnelEgressLSRId_Type())
fsMplsLSPMapSubTunnelEgressLSRId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsLSPMapSubTunnelEgressLSRId.setStatus(_A)
_FsMplsLSPMaptunnelOperation_Type=Unsigned32
_FsMplsLSPMaptunnelOperation_Object=MibTableColumn
fsMplsLSPMaptunnelOperation=_FsMplsLSPMaptunnelOperation_Object((1,3,6,1,4,1,29601,2,58,1,1,1,9),_FsMplsLSPMaptunnelOperation_Type())
fsMplsLSPMaptunnelOperation.setMaxAccess(_L)
if mibBuilder.loadTexts:fsMplsLSPMaptunnelOperation.setStatus(_A)
_FsMplsLSPMaptunnelRowStatus_Type=RowStatus
_FsMplsLSPMaptunnelRowStatus_Object=MibTableColumn
fsMplsLSPMaptunnelRowStatus=_FsMplsLSPMaptunnelRowStatus_Object((1,3,6,1,4,1,29601,2,58,1,1,1,10),_FsMplsLSPMaptunnelRowStatus_Type())
fsMplsLSPMaptunnelRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:fsMplsLSPMaptunnelRowStatus.setStatus(_A)
_FsMplsHLSPTable_Object=MibTable
fsMplsHLSPTable=_FsMplsHLSPTable_Object((1,3,6,1,4,1,29601,2,58,1,2))
if mibBuilder.loadTexts:fsMplsHLSPTable.setStatus(_A)
_FsMplsHLSPEntry_Object=MibTableRow
fsMplsHLSPEntry=_FsMplsHLSPEntry_Object((1,3,6,1,4,1,29601,2,58,1,2,1))
fsMplsHLSPEntry.setIndexNames((0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:fsMplsHLSPEntry.setStatus(_A)
_FsMplsHLSPIndex_Type=MplsTunnelIndex
_FsMplsHLSPIndex_Object=MibTableColumn
fsMplsHLSPIndex=_FsMplsHLSPIndex_Object((1,3,6,1,4,1,29601,2,58,1,2,1,1),_FsMplsHLSPIndex_Type())
fsMplsHLSPIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsHLSPIndex.setStatus(_A)
_FsMplsHLSPInstance_Type=MplsTunnelInstanceIndex
_FsMplsHLSPInstance_Object=MibTableColumn
fsMplsHLSPInstance=_FsMplsHLSPInstance_Object((1,3,6,1,4,1,29601,2,58,1,2,1,2),_FsMplsHLSPInstance_Type())
fsMplsHLSPInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsHLSPInstance.setStatus(_A)
_FsMplsHLSPIngressLSRId_Type=MplsExtendedTunnelId
_FsMplsHLSPIngressLSRId_Object=MibTableColumn
fsMplsHLSPIngressLSRId=_FsMplsHLSPIngressLSRId_Object((1,3,6,1,4,1,29601,2,58,1,2,1,3),_FsMplsHLSPIngressLSRId_Type())
fsMplsHLSPIngressLSRId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsHLSPIngressLSRId.setStatus(_A)
_FsMplsHLSPEgressLSRId_Type=MplsExtendedTunnelId
_FsMplsHLSPEgressLSRId_Object=MibTableColumn
fsMplsHLSPEgressLSRId=_FsMplsHLSPEgressLSRId_Object((1,3,6,1,4,1,29601,2,58,1,2,1,4),_FsMplsHLSPEgressLSRId_Type())
fsMplsHLSPEgressLSRId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMplsHLSPEgressLSRId.setStatus(_A)
_FsMplsHLSPAvailableBW_Type=Unsigned32
_FsMplsHLSPAvailableBW_Object=MibTableColumn
fsMplsHLSPAvailableBW=_FsMplsHLSPAvailableBW_Object((1,3,6,1,4,1,29601,2,58,1,2,1,5),_FsMplsHLSPAvailableBW_Type())
fsMplsHLSPAvailableBW.setMaxAccess(_Q)
if mibBuilder.loadTexts:fsMplsHLSPAvailableBW.setStatus(_A)
_FsMplsHLSPNoOfStackedTunnels_Type=Unsigned32
_FsMplsHLSPNoOfStackedTunnels_Object=MibTableColumn
fsMplsHLSPNoOfStackedTunnels=_FsMplsHLSPNoOfStackedTunnels_Object((1,3,6,1,4,1,29601,2,58,1,2,1,6),_FsMplsHLSPNoOfStackedTunnels_Type())
fsMplsHLSPNoOfStackedTunnels.setMaxAccess(_Q)
if mibBuilder.loadTexts:fsMplsHLSPNoOfStackedTunnels.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsHlspMIB':fsHlspMIB,'fsMplsHlspConfigObjects':fsMplsHlspConfigObjects,'fsMplsLSPMapTunnelTable':fsMplsLSPMapTunnelTable,'fsMplsLSPMapTunnelEntry':fsMplsLSPMapTunnelEntry,_D:fsMplsLSPMapTunnelIndex,_E:fsMplsLSPMapTunnelInstance,_F:fsMplsLSPMapTunnelIngressLSRId,_G:fsMplsLSPMapTunnelEgressLSRId,_H:fsMplsLSPMapSubTunnelIndex,_I:fsMplsLSPMapSubTunnelInstance,_J:fsMplsLSPMapSubTunnelIngressLSRId,_K:fsMplsLSPMapSubTunnelEgressLSRId,'fsMplsLSPMaptunnelOperation':fsMplsLSPMaptunnelOperation,'fsMplsLSPMaptunnelRowStatus':fsMplsLSPMaptunnelRowStatus,'fsMplsHLSPTable':fsMplsHLSPTable,'fsMplsHLSPEntry':fsMplsHLSPEntry,_M:fsMplsHLSPIndex,_N:fsMplsHLSPInstance,_O:fsMplsHLSPIngressLSRId,_P:fsMplsHLSPEgressLSRId,'fsMplsHLSPAvailableBW':fsMplsHLSPAvailableBW,'fsMplsHLSPNoOfStackedTunnels':fsMplsHLSPNoOfStackedTunnels})