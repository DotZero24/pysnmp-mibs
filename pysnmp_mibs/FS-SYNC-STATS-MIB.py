_a='fsSyncStatsGroup'
_Z='fsSyncStatsTxUnderrunErrors'
_Y='fsSyncStatsTxFrameTooLongErrors'
_X='fsSyncStatsTxClockErrors'
_W='fsSyncStatsTxRingFullDropsErrors'
_V='fsSyncStatsTxOctets'
_U='fsSyncStatsTxFrames'
_T='fsSyncStatsRxRcvrOverrunErrors'
_S='fsSyncStatsRxCrcErrors'
_R='fsSyncStatsRxAbortErrors'
_Q='fsSyncStatsRxFrameOctetAlignErrors'
_P='fsSyncStatsRxFrameTooLongErrors'
_O='fsSyncStatsRxDpllErrors'
_N='fsSyncStatsRxClockErrors'
_M='fsSyncStatsRxReplenFails'
_L='fsSyncStatsRxOctets'
_K='fsSyncStatsRxFrames'
_J='fsSyncStatsPortState'
_I='fsSyncStatsIfIndex'
_H='fsSyncStatsRowStatus'
_G='fsSyncStatsChannel'
_F='fsSyncStatsConn'
_E='fsSyncStatsSlot'
_D='Integer32'
_C='read-only'
_B='current'
_A='FS-SYNC-STATS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fsSyncStatsMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,51))
if mibBuilder.loadTexts:fsSyncStatsMIB.setRevisions(('2009-05-20 14:56',))
_FsSyncStatsMibObjects_ObjectIdentity=ObjectIdentity
fsSyncStatsMibObjects=_FsSyncStatsMibObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,51,1))
_FsStatsSyncGlobal_ObjectIdentity=ObjectIdentity
fsStatsSyncGlobal=_FsStatsSyncGlobal_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,51,1,1))
_FsSyncStatsTable_Object=MibTable
fsSyncStatsTable=_FsSyncStatsTable_Object((1,3,6,1,4,1,52642,1,1,10,2,51,1,2))
if mibBuilder.loadTexts:fsSyncStatsTable.setStatus(_B)
_FsSyncStatsEntry_Object=MibTableRow
fsSyncStatsEntry=_FsSyncStatsEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,51,1,2,1))
fsSyncStatsEntry.setIndexNames((0,_A,_E),(0,_A,_F),(0,_A,_G))
if mibBuilder.loadTexts:fsSyncStatsEntry.setStatus(_B)
_FsSyncStatsRowStatus_Type=RowStatus
_FsSyncStatsRowStatus_Object=MibTableColumn
fsSyncStatsRowStatus=_FsSyncStatsRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,51,1,2,1,1),_FsSyncStatsRowStatus_Type())
fsSyncStatsRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:fsSyncStatsRowStatus.setStatus(_B)
class _FsSyncStatsSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsSyncStatsSlot_Type.__name__=_D
_FsSyncStatsSlot_Object=MibTableColumn
fsSyncStatsSlot=_FsSyncStatsSlot_Object((1,3,6,1,4,1,52642,1,1,10,2,51,1,2,1,2),_FsSyncStatsSlot_Type())
fsSyncStatsSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSyncStatsSlot.setStatus(_B)
class _FsSyncStatsConn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsSyncStatsConn_Type.__name__=_D
_FsSyncStatsConn_Object=MibTableColumn
fsSyncStatsConn=_FsSyncStatsConn_Object((1,3,6,1,4,1,52642,1,1,10,2,51,1,2,1,3),_FsSyncStatsConn_Type())
fsSyncStatsConn.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSyncStatsConn.setStatus(_B)
class _FsSyncStatsChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsSyncStatsChannel_Type.__name__=_D
_FsSyncStatsChannel_Object=MibTableColumn
fsSyncStatsChannel=_FsSyncStatsChannel_Object((1,3,6,1,4,1,52642,1,1,10,2,51,1,2,1,4),_FsSyncStatsChannel_Type())
fsSyncStatsChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSyncStatsChannel.setStatus(_B)
_FsSyncStatsIfIndex_Type=InterfaceIndex
_FsSyncStatsIfIndex_Object=MibTableColumn
fsSyncStatsIfIndex=_FsSyncStatsIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,51,1,2,1,5),_FsSyncStatsIfIndex_Type())
fsSyncStatsIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSyncStatsIfIndex.setStatus(_B)
class _FsSyncStatsPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('init',1),('running',2),('up',3),('down',4)))
_FsSyncStatsPortState_Type.__name__=_D
_FsSyncStatsPortState_Object=MibTableColumn
fsSyncStatsPortState=_FsSyncStatsPortState_Object((1,3,6,1,4,1,52642,1,1,10,2,51,1,2,1,6),_FsSyncStatsPortState_Type())
fsSyncStatsPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSyncStatsPortState.setStatus(_B)
_FsSyncStatsRxFrames_Type=Counter32
_FsSyncStatsRxFrames_Object=MibTableColumn
fsSyncStatsRxFrames=_FsSyncStatsRxFrames_Object((1,3,6,1,4,1,52642,1,1,10,2,51,1,2,1,7),_FsSyncStatsRxFrames_Type())
fsSyncStatsRxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSyncStatsRxFrames.setStatus(_B)
_FsSyncStatsRxOctets_Type=Counter32
_FsSyncStatsRxOctets_Object=MibTableColumn
fsSyncStatsRxOctets=_FsSyncStatsRxOctets_Object((1,3,6,1,4,1,52642,1,1,10,2,51,1,2,1,8),_FsSyncStatsRxOctets_Type())
fsSyncStatsRxOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSyncStatsRxOctets.setStatus(_B)
_FsSyncStatsRxReplenFails_Type=Counter32
_FsSyncStatsRxReplenFails_Object=MibTableColumn
fsSyncStatsRxReplenFails=_FsSyncStatsRxReplenFails_Object((1,3,6,1,4,1,52642,1,1,10,2,51,1,2,1,9),_FsSyncStatsRxReplenFails_Type())
fsSyncStatsRxReplenFails.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSyncStatsRxReplenFails.setStatus(_B)
_FsSyncStatsRxClockErrors_Type=Counter32
_FsSyncStatsRxClockErrors_Object=MibTableColumn
fsSyncStatsRxClockErrors=_FsSyncStatsRxClockErrors_Object((1,3,6,1,4,1,52642,1,1,10,2,51,1,2,1,10),_FsSyncStatsRxClockErrors_Type())
fsSyncStatsRxClockErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSyncStatsRxClockErrors.setStatus(_B)
_FsSyncStatsRxDpllErrors_Type=Counter32
_FsSyncStatsRxDpllErrors_Object=MibTableColumn
fsSyncStatsRxDpllErrors=_FsSyncStatsRxDpllErrors_Object((1,3,6,1,4,1,52642,1,1,10,2,51,1,2,1,11),_FsSyncStatsRxDpllErrors_Type())
fsSyncStatsRxDpllErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSyncStatsRxDpllErrors.setStatus(_B)
_FsSyncStatsRxFrameTooLongErrors_Type=Counter32
_FsSyncStatsRxFrameTooLongErrors_Object=MibTableColumn
fsSyncStatsRxFrameTooLongErrors=_FsSyncStatsRxFrameTooLongErrors_Object((1,3,6,1,4,1,52642,1,1,10,2,51,1,2,1,12),_FsSyncStatsRxFrameTooLongErrors_Type())
fsSyncStatsRxFrameTooLongErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSyncStatsRxFrameTooLongErrors.setStatus(_B)
_FsSyncStatsRxFrameOctetAlignErrors_Type=Counter32
_FsSyncStatsRxFrameOctetAlignErrors_Object=MibTableColumn
fsSyncStatsRxFrameOctetAlignErrors=_FsSyncStatsRxFrameOctetAlignErrors_Object((1,3,6,1,4,1,52642,1,1,10,2,51,1,2,1,13),_FsSyncStatsRxFrameOctetAlignErrors_Type())
fsSyncStatsRxFrameOctetAlignErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSyncStatsRxFrameOctetAlignErrors.setStatus(_B)
_FsSyncStatsRxAbortErrors_Type=Counter32
_FsSyncStatsRxAbortErrors_Object=MibTableColumn
fsSyncStatsRxAbortErrors=_FsSyncStatsRxAbortErrors_Object((1,3,6,1,4,1,52642,1,1,10,2,51,1,2,1,14),_FsSyncStatsRxAbortErrors_Type())
fsSyncStatsRxAbortErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSyncStatsRxAbortErrors.setStatus(_B)
_FsSyncStatsRxCrcErrors_Type=Counter32
_FsSyncStatsRxCrcErrors_Object=MibTableColumn
fsSyncStatsRxCrcErrors=_FsSyncStatsRxCrcErrors_Object((1,3,6,1,4,1,52642,1,1,10,2,51,1,2,1,15),_FsSyncStatsRxCrcErrors_Type())
fsSyncStatsRxCrcErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSyncStatsRxCrcErrors.setStatus(_B)
_FsSyncStatsRxRcvrOverrunErrors_Type=Counter32
_FsSyncStatsRxRcvrOverrunErrors_Object=MibTableColumn
fsSyncStatsRxRcvrOverrunErrors=_FsSyncStatsRxRcvrOverrunErrors_Object((1,3,6,1,4,1,52642,1,1,10,2,51,1,2,1,16),_FsSyncStatsRxRcvrOverrunErrors_Type())
fsSyncStatsRxRcvrOverrunErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSyncStatsRxRcvrOverrunErrors.setStatus(_B)
_FsSyncStatsTxFrames_Type=Counter32
_FsSyncStatsTxFrames_Object=MibTableColumn
fsSyncStatsTxFrames=_FsSyncStatsTxFrames_Object((1,3,6,1,4,1,52642,1,1,10,2,51,1,2,1,17),_FsSyncStatsTxFrames_Type())
fsSyncStatsTxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSyncStatsTxFrames.setStatus(_B)
_FsSyncStatsTxOctets_Type=Counter32
_FsSyncStatsTxOctets_Object=MibTableColumn
fsSyncStatsTxOctets=_FsSyncStatsTxOctets_Object((1,3,6,1,4,1,52642,1,1,10,2,51,1,2,1,18),_FsSyncStatsTxOctets_Type())
fsSyncStatsTxOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSyncStatsTxOctets.setStatus(_B)
_FsSyncStatsTxRingFullDropsErrors_Type=Counter32
_FsSyncStatsTxRingFullDropsErrors_Object=MibTableColumn
fsSyncStatsTxRingFullDropsErrors=_FsSyncStatsTxRingFullDropsErrors_Object((1,3,6,1,4,1,52642,1,1,10,2,51,1,2,1,19),_FsSyncStatsTxRingFullDropsErrors_Type())
fsSyncStatsTxRingFullDropsErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSyncStatsTxRingFullDropsErrors.setStatus(_B)
_FsSyncStatsTxClockErrors_Type=Counter32
_FsSyncStatsTxClockErrors_Object=MibTableColumn
fsSyncStatsTxClockErrors=_FsSyncStatsTxClockErrors_Object((1,3,6,1,4,1,52642,1,1,10,2,51,1,2,1,20),_FsSyncStatsTxClockErrors_Type())
fsSyncStatsTxClockErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSyncStatsTxClockErrors.setStatus(_B)
_FsSyncStatsTxFrameTooLongErrors_Type=Counter32
_FsSyncStatsTxFrameTooLongErrors_Object=MibTableColumn
fsSyncStatsTxFrameTooLongErrors=_FsSyncStatsTxFrameTooLongErrors_Object((1,3,6,1,4,1,52642,1,1,10,2,51,1,2,1,21),_FsSyncStatsTxFrameTooLongErrors_Type())
fsSyncStatsTxFrameTooLongErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSyncStatsTxFrameTooLongErrors.setStatus(_B)
_FsSyncStatsTxUnderrunErrors_Type=Counter32
_FsSyncStatsTxUnderrunErrors_Object=MibTableColumn
fsSyncStatsTxUnderrunErrors=_FsSyncStatsTxUnderrunErrors_Object((1,3,6,1,4,1,52642,1,1,10,2,51,1,2,1,22),_FsSyncStatsTxUnderrunErrors_Type())
fsSyncStatsTxUnderrunErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSyncStatsTxUnderrunErrors.setStatus(_B)
_FsSyncStatsMibConformance_ObjectIdentity=ObjectIdentity
fsSyncStatsMibConformance=_FsSyncStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,51,2))
_FsSyncStatsMibCompliances_ObjectIdentity=ObjectIdentity
fsSyncStatsMibCompliances=_FsSyncStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,51,2,1))
_FsSyncStatsMibGroups_ObjectIdentity=ObjectIdentity
fsSyncStatsMibGroups=_FsSyncStatsMibGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,51,2,2))
fsSyncStatsGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,51,2,2,1))
fsSyncStatsGroup.setObjects(*((_A,_H),(_A,_E),(_A,_F),(_A,_G),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:fsSyncStatsGroup.setStatus(_B)
fsSyncStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,51,2,1,1))
fsSyncStatsMibCompliance.setObjects((_A,_a))
if mibBuilder.loadTexts:fsSyncStatsMibCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'fsSyncStatsMIB':fsSyncStatsMIB,'fsSyncStatsMibObjects':fsSyncStatsMibObjects,'fsStatsSyncGlobal':fsStatsSyncGlobal,'fsSyncStatsTable':fsSyncStatsTable,'fsSyncStatsEntry':fsSyncStatsEntry,_H:fsSyncStatsRowStatus,_E:fsSyncStatsSlot,_F:fsSyncStatsConn,_G:fsSyncStatsChannel,_I:fsSyncStatsIfIndex,_J:fsSyncStatsPortState,_K:fsSyncStatsRxFrames,_L:fsSyncStatsRxOctets,_M:fsSyncStatsRxReplenFails,_N:fsSyncStatsRxClockErrors,_O:fsSyncStatsRxDpllErrors,_P:fsSyncStatsRxFrameTooLongErrors,_Q:fsSyncStatsRxFrameOctetAlignErrors,_R:fsSyncStatsRxAbortErrors,_S:fsSyncStatsRxCrcErrors,_T:fsSyncStatsRxRcvrOverrunErrors,_U:fsSyncStatsTxFrames,_V:fsSyncStatsTxOctets,_W:fsSyncStatsTxRingFullDropsErrors,_X:fsSyncStatsTxClockErrors,_Y:fsSyncStatsTxFrameTooLongErrors,_Z:fsSyncStatsTxUnderrunErrors,'fsSyncStatsMibConformance':fsSyncStatsMibConformance,'fsSyncStatsMibCompliances':fsSyncStatsMibCompliances,'fsSyncStatsMibCompliance':fsSyncStatsMibCompliance,'fsSyncStatsMibGroups':fsSyncStatsMibGroups,_a:fsSyncStatsGroup})