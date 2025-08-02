_H='ctPPCBadPktsRxIndex'
_G='ctPPCBadPktsQ'
_F='ctPPCBadPktsTxQIndex'
_E='ctPPCBadPktsTxIndex'
_D='Integer32'
_C='CTRON-PPC-BAD-PACKETS-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctFWDebug,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctFWDebug')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtPPCBadPkts_ObjectIdentity=ObjectIdentity
ctPPCBadPkts=_CtPPCBadPkts_ObjectIdentity((1,3,6,1,4,1,52,4,2,29,1))
_CtPPCBadPktsTotalTx_Type=Integer32
_CtPPCBadPktsTotalTx_Object=MibScalar
ctPPCBadPktsTotalTx=_CtPPCBadPktsTotalTx_Object((1,3,6,1,4,1,52,4,2,29,1,1),_CtPPCBadPktsTotalTx_Type())
ctPPCBadPktsTotalTx.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPPCBadPktsTotalTx.setStatus(_A)
_CtPPCBadPktsTotalRx_Type=Integer32
_CtPPCBadPktsTotalRx_Object=MibScalar
ctPPCBadPktsTotalRx=_CtPPCBadPktsTotalRx_Object((1,3,6,1,4,1,52,4,2,29,1,2),_CtPPCBadPktsTotalRx_Type())
ctPPCBadPktsTotalRx.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPPCBadPktsTotalRx.setStatus(_A)
_CtPPCBadPktsTxTable_Object=MibTable
ctPPCBadPktsTxTable=_CtPPCBadPktsTxTable_Object((1,3,6,1,4,1,52,4,2,29,1,3))
if mibBuilder.loadTexts:ctPPCBadPktsTxTable.setStatus(_A)
_CtPPCBadPktsTxEntry_Object=MibTableRow
ctPPCBadPktsTxEntry=_CtPPCBadPktsTxEntry_Object((1,3,6,1,4,1,52,4,2,29,1,3,1))
ctPPCBadPktsTxEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:ctPPCBadPktsTxEntry.setStatus(_A)
_CtPPCBadPktsTxIndex_Type=Integer32
_CtPPCBadPktsTxIndex_Object=MibTableColumn
ctPPCBadPktsTxIndex=_CtPPCBadPktsTxIndex_Object((1,3,6,1,4,1,52,4,2,29,1,3,1,1),_CtPPCBadPktsTxIndex_Type())
ctPPCBadPktsTxIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPPCBadPktsTxIndex.setStatus(_A)
_CtPPCBadPktsTxQueues_Type=Integer32
_CtPPCBadPktsTxQueues_Object=MibTableColumn
ctPPCBadPktsTxQueues=_CtPPCBadPktsTxQueues_Object((1,3,6,1,4,1,52,4,2,29,1,3,1,2),_CtPPCBadPktsTxQueues_Type())
ctPPCBadPktsTxQueues.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPPCBadPktsTxQueues.setStatus(_A)
_CtPPCBadPktsTxFulls_Type=Integer32
_CtPPCBadPktsTxFulls_Object=MibTableColumn
ctPPCBadPktsTxFulls=_CtPPCBadPktsTxFulls_Object((1,3,6,1,4,1,52,4,2,29,1,3,1,3),_CtPPCBadPktsTxFulls_Type())
ctPPCBadPktsTxFulls.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPPCBadPktsTxFulls.setStatus(_A)
_CtPPCBadPktsTxQDepthTable_Object=MibTable
ctPPCBadPktsTxQDepthTable=_CtPPCBadPktsTxQDepthTable_Object((1,3,6,1,4,1,52,4,2,29,1,4))
if mibBuilder.loadTexts:ctPPCBadPktsTxQDepthTable.setStatus(_A)
_CtPPCBadPktsTxQDepthEntry_Object=MibTableRow
ctPPCBadPktsTxQDepthEntry=_CtPPCBadPktsTxQDepthEntry_Object((1,3,6,1,4,1,52,4,2,29,1,4,1))
ctPPCBadPktsTxQDepthEntry.setIndexNames((0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:ctPPCBadPktsTxQDepthEntry.setStatus(_A)
_CtPPCBadPktsTxQIndex_Type=Integer32
_CtPPCBadPktsTxQIndex_Object=MibTableColumn
ctPPCBadPktsTxQIndex=_CtPPCBadPktsTxQIndex_Object((1,3,6,1,4,1,52,4,2,29,1,4,1,1),_CtPPCBadPktsTxQIndex_Type())
ctPPCBadPktsTxQIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPPCBadPktsTxQIndex.setStatus(_A)
class _CtPPCBadPktsQ_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_CtPPCBadPktsQ_Type.__name__=_D
_CtPPCBadPktsQ_Object=MibTableColumn
ctPPCBadPktsQ=_CtPPCBadPktsQ_Object((1,3,6,1,4,1,52,4,2,29,1,4,1,2),_CtPPCBadPktsQ_Type())
ctPPCBadPktsQ.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPPCBadPktsQ.setStatus(_A)
_CtPPCBadPktsTxQDepth_Type=Integer32
_CtPPCBadPktsTxQDepth_Object=MibTableColumn
ctPPCBadPktsTxQDepth=_CtPPCBadPktsTxQDepth_Object((1,3,6,1,4,1,52,4,2,29,1,4,1,3),_CtPPCBadPktsTxQDepth_Type())
ctPPCBadPktsTxQDepth.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPPCBadPktsTxQDepth.setStatus(_A)
_CtPPCBadPktsRxTable_Object=MibTable
ctPPCBadPktsRxTable=_CtPPCBadPktsRxTable_Object((1,3,6,1,4,1,52,4,2,29,1,5))
if mibBuilder.loadTexts:ctPPCBadPktsRxTable.setStatus(_A)
_CtPPCBadPktsRxEntry_Object=MibTableRow
ctPPCBadPktsRxEntry=_CtPPCBadPktsRxEntry_Object((1,3,6,1,4,1,52,4,2,29,1,5,1))
ctPPCBadPktsRxEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:ctPPCBadPktsRxEntry.setStatus(_A)
_CtPPCBadPktsRxIndex_Type=Integer32
_CtPPCBadPktsRxIndex_Object=MibTableColumn
ctPPCBadPktsRxIndex=_CtPPCBadPktsRxIndex_Object((1,3,6,1,4,1,52,4,2,29,1,5,1,1),_CtPPCBadPktsRxIndex_Type())
ctPPCBadPktsRxIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPPCBadPktsRxIndex.setStatus(_A)
_CtPPCBadPktsRxTotalErrors_Type=Integer32
_CtPPCBadPktsRxTotalErrors_Object=MibTableColumn
ctPPCBadPktsRxTotalErrors=_CtPPCBadPktsRxTotalErrors_Object((1,3,6,1,4,1,52,4,2,29,1,5,1,2),_CtPPCBadPktsRxTotalErrors_Type())
ctPPCBadPktsRxTotalErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPPCBadPktsRxTotalErrors.setStatus(_A)
_CtPPCBadPktsRxDescHigh_Type=Integer32
_CtPPCBadPktsRxDescHigh_Object=MibTableColumn
ctPPCBadPktsRxDescHigh=_CtPPCBadPktsRxDescHigh_Object((1,3,6,1,4,1,52,4,2,29,1,5,1,3),_CtPPCBadPktsRxDescHigh_Type())
ctPPCBadPktsRxDescHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPPCBadPktsRxDescHigh.setStatus(_A)
_CtPPCBadPktsRxDescLow_Type=Integer32
_CtPPCBadPktsRxDescLow_Object=MibTableColumn
ctPPCBadPktsRxDescLow=_CtPPCBadPktsRxDescLow_Object((1,3,6,1,4,1,52,4,2,29,1,5,1,4),_CtPPCBadPktsRxDescLow_Type())
ctPPCBadPktsRxDescLow.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPPCBadPktsRxDescLow.setStatus(_A)
_CtPPCBadPktsRxDaSa0_Type=Integer32
_CtPPCBadPktsRxDaSa0_Object=MibTableColumn
ctPPCBadPktsRxDaSa0=_CtPPCBadPktsRxDaSa0_Object((1,3,6,1,4,1,52,4,2,29,1,5,1,5),_CtPPCBadPktsRxDaSa0_Type())
ctPPCBadPktsRxDaSa0.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPPCBadPktsRxDaSa0.setStatus(_A)
_CtPPCBadPktsRxDaSa1_Type=Integer32
_CtPPCBadPktsRxDaSa1_Object=MibTableColumn
ctPPCBadPktsRxDaSa1=_CtPPCBadPktsRxDaSa1_Object((1,3,6,1,4,1,52,4,2,29,1,5,1,6),_CtPPCBadPktsRxDaSa1_Type())
ctPPCBadPktsRxDaSa1.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPPCBadPktsRxDaSa1.setStatus(_A)
_CtPPCBadPktsRxDaSa2_Type=Integer32
_CtPPCBadPktsRxDaSa2_Object=MibTableColumn
ctPPCBadPktsRxDaSa2=_CtPPCBadPktsRxDaSa2_Object((1,3,6,1,4,1,52,4,2,29,1,5,1,7),_CtPPCBadPktsRxDaSa2_Type())
ctPPCBadPktsRxDaSa2.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPPCBadPktsRxDaSa2.setStatus(_A)
_CtPPCBadPktsRxData_Type=Integer32
_CtPPCBadPktsRxData_Object=MibTableColumn
ctPPCBadPktsRxData=_CtPPCBadPktsRxData_Object((1,3,6,1,4,1,52,4,2,29,1,5,1,8),_CtPPCBadPktsRxData_Type())
ctPPCBadPktsRxData.setMaxAccess(_B)
if mibBuilder.loadTexts:ctPPCBadPktsRxData.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ctPPCBadPkts':ctPPCBadPkts,'ctPPCBadPktsTotalTx':ctPPCBadPktsTotalTx,'ctPPCBadPktsTotalRx':ctPPCBadPktsTotalRx,'ctPPCBadPktsTxTable':ctPPCBadPktsTxTable,'ctPPCBadPktsTxEntry':ctPPCBadPktsTxEntry,_E:ctPPCBadPktsTxIndex,'ctPPCBadPktsTxQueues':ctPPCBadPktsTxQueues,'ctPPCBadPktsTxFulls':ctPPCBadPktsTxFulls,'ctPPCBadPktsTxQDepthTable':ctPPCBadPktsTxQDepthTable,'ctPPCBadPktsTxQDepthEntry':ctPPCBadPktsTxQDepthEntry,_F:ctPPCBadPktsTxQIndex,_G:ctPPCBadPktsQ,'ctPPCBadPktsTxQDepth':ctPPCBadPktsTxQDepth,'ctPPCBadPktsRxTable':ctPPCBadPktsRxTable,'ctPPCBadPktsRxEntry':ctPPCBadPktsRxEntry,_H:ctPPCBadPktsRxIndex,'ctPPCBadPktsRxTotalErrors':ctPPCBadPktsRxTotalErrors,'ctPPCBadPktsRxDescHigh':ctPPCBadPktsRxDescHigh,'ctPPCBadPktsRxDescLow':ctPPCBadPktsRxDescLow,'ctPPCBadPktsRxDaSa0':ctPPCBadPktsRxDaSa0,'ctPPCBadPktsRxDaSa1':ctPPCBadPktsRxDaSa1,'ctPPCBadPktsRxDaSa2':ctPPCBadPktsRxDaSa2,'ctPPCBadPktsRxData':ctPPCBadPktsRxData})