_a='qtechSyncStatsGroup'
_Z='qtechSyncStatsTxUnderrunErrors'
_Y='qtechSyncStatsTxFrameTooLongErrors'
_X='qtechSyncStatsTxClockErrors'
_W='qtechSyncStatsTxRingFullDropsErrors'
_V='qtechSyncStatsTxOctets'
_U='qtechSyncStatsTxFrames'
_T='qtechSyncStatsRxRcvrOverrunErrors'
_S='qtechSyncStatsRxCrcErrors'
_R='qtechSyncStatsRxAbortErrors'
_Q='qtechSyncStatsRxFrameOctetAlignErrors'
_P='qtechSyncStatsRxFrameTooLongErrors'
_O='qtechSyncStatsRxDpllErrors'
_N='qtechSyncStatsRxClockErrors'
_M='qtechSyncStatsRxReplenFails'
_L='qtechSyncStatsRxOctets'
_K='qtechSyncStatsRxFrames'
_J='qtechSyncStatsPortState'
_I='qtechSyncStatsIfIndex'
_H='qtechSyncStatsRowStatus'
_G='qtechSyncStatsChannel'
_F='qtechSyncStatsConn'
_E='qtechSyncStatsSlot'
_D='Integer32'
_C='read-only'
_B='current'
_A='QTECH-SYNC-STATS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
qtechSyncStatsMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,51))
if mibBuilder.loadTexts:qtechSyncStatsMIB.setRevisions(('2009-05-20 14:56',))
_QtechSyncStatsMibObjects_ObjectIdentity=ObjectIdentity
qtechSyncStatsMibObjects=_QtechSyncStatsMibObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,51,1))
_QtechStatsSyncGlobal_ObjectIdentity=ObjectIdentity
qtechStatsSyncGlobal=_QtechStatsSyncGlobal_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,51,1,1))
_QtechSyncStatsTable_Object=MibTable
qtechSyncStatsTable=_QtechSyncStatsTable_Object((1,3,6,1,4,1,27514,1,1,10,2,51,1,2))
if mibBuilder.loadTexts:qtechSyncStatsTable.setStatus(_B)
_QtechSyncStatsEntry_Object=MibTableRow
qtechSyncStatsEntry=_QtechSyncStatsEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,51,1,2,1))
qtechSyncStatsEntry.setIndexNames((0,_A,_E),(0,_A,_F),(0,_A,_G))
if mibBuilder.loadTexts:qtechSyncStatsEntry.setStatus(_B)
_QtechSyncStatsRowStatus_Type=RowStatus
_QtechSyncStatsRowStatus_Object=MibTableColumn
qtechSyncStatsRowStatus=_QtechSyncStatsRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,51,1,2,1,1),_QtechSyncStatsRowStatus_Type())
qtechSyncStatsRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:qtechSyncStatsRowStatus.setStatus(_B)
class _QtechSyncStatsSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_QtechSyncStatsSlot_Type.__name__=_D
_QtechSyncStatsSlot_Object=MibTableColumn
qtechSyncStatsSlot=_QtechSyncStatsSlot_Object((1,3,6,1,4,1,27514,1,1,10,2,51,1,2,1,2),_QtechSyncStatsSlot_Type())
qtechSyncStatsSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSyncStatsSlot.setStatus(_B)
class _QtechSyncStatsConn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_QtechSyncStatsConn_Type.__name__=_D
_QtechSyncStatsConn_Object=MibTableColumn
qtechSyncStatsConn=_QtechSyncStatsConn_Object((1,3,6,1,4,1,27514,1,1,10,2,51,1,2,1,3),_QtechSyncStatsConn_Type())
qtechSyncStatsConn.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSyncStatsConn.setStatus(_B)
class _QtechSyncStatsChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_QtechSyncStatsChannel_Type.__name__=_D
_QtechSyncStatsChannel_Object=MibTableColumn
qtechSyncStatsChannel=_QtechSyncStatsChannel_Object((1,3,6,1,4,1,27514,1,1,10,2,51,1,2,1,4),_QtechSyncStatsChannel_Type())
qtechSyncStatsChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSyncStatsChannel.setStatus(_B)
_QtechSyncStatsIfIndex_Type=InterfaceIndex
_QtechSyncStatsIfIndex_Object=MibTableColumn
qtechSyncStatsIfIndex=_QtechSyncStatsIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,51,1,2,1,5),_QtechSyncStatsIfIndex_Type())
qtechSyncStatsIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSyncStatsIfIndex.setStatus(_B)
class _QtechSyncStatsPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('init',1),('running',2),('up',3),('down',4)))
_QtechSyncStatsPortState_Type.__name__=_D
_QtechSyncStatsPortState_Object=MibTableColumn
qtechSyncStatsPortState=_QtechSyncStatsPortState_Object((1,3,6,1,4,1,27514,1,1,10,2,51,1,2,1,6),_QtechSyncStatsPortState_Type())
qtechSyncStatsPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSyncStatsPortState.setStatus(_B)
_QtechSyncStatsRxFrames_Type=Counter32
_QtechSyncStatsRxFrames_Object=MibTableColumn
qtechSyncStatsRxFrames=_QtechSyncStatsRxFrames_Object((1,3,6,1,4,1,27514,1,1,10,2,51,1,2,1,7),_QtechSyncStatsRxFrames_Type())
qtechSyncStatsRxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSyncStatsRxFrames.setStatus(_B)
_QtechSyncStatsRxOctets_Type=Counter32
_QtechSyncStatsRxOctets_Object=MibTableColumn
qtechSyncStatsRxOctets=_QtechSyncStatsRxOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,51,1,2,1,8),_QtechSyncStatsRxOctets_Type())
qtechSyncStatsRxOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSyncStatsRxOctets.setStatus(_B)
_QtechSyncStatsRxReplenFails_Type=Counter32
_QtechSyncStatsRxReplenFails_Object=MibTableColumn
qtechSyncStatsRxReplenFails=_QtechSyncStatsRxReplenFails_Object((1,3,6,1,4,1,27514,1,1,10,2,51,1,2,1,9),_QtechSyncStatsRxReplenFails_Type())
qtechSyncStatsRxReplenFails.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSyncStatsRxReplenFails.setStatus(_B)
_QtechSyncStatsRxClockErrors_Type=Counter32
_QtechSyncStatsRxClockErrors_Object=MibTableColumn
qtechSyncStatsRxClockErrors=_QtechSyncStatsRxClockErrors_Object((1,3,6,1,4,1,27514,1,1,10,2,51,1,2,1,10),_QtechSyncStatsRxClockErrors_Type())
qtechSyncStatsRxClockErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSyncStatsRxClockErrors.setStatus(_B)
_QtechSyncStatsRxDpllErrors_Type=Counter32
_QtechSyncStatsRxDpllErrors_Object=MibTableColumn
qtechSyncStatsRxDpllErrors=_QtechSyncStatsRxDpllErrors_Object((1,3,6,1,4,1,27514,1,1,10,2,51,1,2,1,11),_QtechSyncStatsRxDpllErrors_Type())
qtechSyncStatsRxDpllErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSyncStatsRxDpllErrors.setStatus(_B)
_QtechSyncStatsRxFrameTooLongErrors_Type=Counter32
_QtechSyncStatsRxFrameTooLongErrors_Object=MibTableColumn
qtechSyncStatsRxFrameTooLongErrors=_QtechSyncStatsRxFrameTooLongErrors_Object((1,3,6,1,4,1,27514,1,1,10,2,51,1,2,1,12),_QtechSyncStatsRxFrameTooLongErrors_Type())
qtechSyncStatsRxFrameTooLongErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSyncStatsRxFrameTooLongErrors.setStatus(_B)
_QtechSyncStatsRxFrameOctetAlignErrors_Type=Counter32
_QtechSyncStatsRxFrameOctetAlignErrors_Object=MibTableColumn
qtechSyncStatsRxFrameOctetAlignErrors=_QtechSyncStatsRxFrameOctetAlignErrors_Object((1,3,6,1,4,1,27514,1,1,10,2,51,1,2,1,13),_QtechSyncStatsRxFrameOctetAlignErrors_Type())
qtechSyncStatsRxFrameOctetAlignErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSyncStatsRxFrameOctetAlignErrors.setStatus(_B)
_QtechSyncStatsRxAbortErrors_Type=Counter32
_QtechSyncStatsRxAbortErrors_Object=MibTableColumn
qtechSyncStatsRxAbortErrors=_QtechSyncStatsRxAbortErrors_Object((1,3,6,1,4,1,27514,1,1,10,2,51,1,2,1,14),_QtechSyncStatsRxAbortErrors_Type())
qtechSyncStatsRxAbortErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSyncStatsRxAbortErrors.setStatus(_B)
_QtechSyncStatsRxCrcErrors_Type=Counter32
_QtechSyncStatsRxCrcErrors_Object=MibTableColumn
qtechSyncStatsRxCrcErrors=_QtechSyncStatsRxCrcErrors_Object((1,3,6,1,4,1,27514,1,1,10,2,51,1,2,1,15),_QtechSyncStatsRxCrcErrors_Type())
qtechSyncStatsRxCrcErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSyncStatsRxCrcErrors.setStatus(_B)
_QtechSyncStatsRxRcvrOverrunErrors_Type=Counter32
_QtechSyncStatsRxRcvrOverrunErrors_Object=MibTableColumn
qtechSyncStatsRxRcvrOverrunErrors=_QtechSyncStatsRxRcvrOverrunErrors_Object((1,3,6,1,4,1,27514,1,1,10,2,51,1,2,1,16),_QtechSyncStatsRxRcvrOverrunErrors_Type())
qtechSyncStatsRxRcvrOverrunErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSyncStatsRxRcvrOverrunErrors.setStatus(_B)
_QtechSyncStatsTxFrames_Type=Counter32
_QtechSyncStatsTxFrames_Object=MibTableColumn
qtechSyncStatsTxFrames=_QtechSyncStatsTxFrames_Object((1,3,6,1,4,1,27514,1,1,10,2,51,1,2,1,17),_QtechSyncStatsTxFrames_Type())
qtechSyncStatsTxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSyncStatsTxFrames.setStatus(_B)
_QtechSyncStatsTxOctets_Type=Counter32
_QtechSyncStatsTxOctets_Object=MibTableColumn
qtechSyncStatsTxOctets=_QtechSyncStatsTxOctets_Object((1,3,6,1,4,1,27514,1,1,10,2,51,1,2,1,18),_QtechSyncStatsTxOctets_Type())
qtechSyncStatsTxOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSyncStatsTxOctets.setStatus(_B)
_QtechSyncStatsTxRingFullDropsErrors_Type=Counter32
_QtechSyncStatsTxRingFullDropsErrors_Object=MibTableColumn
qtechSyncStatsTxRingFullDropsErrors=_QtechSyncStatsTxRingFullDropsErrors_Object((1,3,6,1,4,1,27514,1,1,10,2,51,1,2,1,19),_QtechSyncStatsTxRingFullDropsErrors_Type())
qtechSyncStatsTxRingFullDropsErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSyncStatsTxRingFullDropsErrors.setStatus(_B)
_QtechSyncStatsTxClockErrors_Type=Counter32
_QtechSyncStatsTxClockErrors_Object=MibTableColumn
qtechSyncStatsTxClockErrors=_QtechSyncStatsTxClockErrors_Object((1,3,6,1,4,1,27514,1,1,10,2,51,1,2,1,20),_QtechSyncStatsTxClockErrors_Type())
qtechSyncStatsTxClockErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSyncStatsTxClockErrors.setStatus(_B)
_QtechSyncStatsTxFrameTooLongErrors_Type=Counter32
_QtechSyncStatsTxFrameTooLongErrors_Object=MibTableColumn
qtechSyncStatsTxFrameTooLongErrors=_QtechSyncStatsTxFrameTooLongErrors_Object((1,3,6,1,4,1,27514,1,1,10,2,51,1,2,1,21),_QtechSyncStatsTxFrameTooLongErrors_Type())
qtechSyncStatsTxFrameTooLongErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSyncStatsTxFrameTooLongErrors.setStatus(_B)
_QtechSyncStatsTxUnderrunErrors_Type=Counter32
_QtechSyncStatsTxUnderrunErrors_Object=MibTableColumn
qtechSyncStatsTxUnderrunErrors=_QtechSyncStatsTxUnderrunErrors_Object((1,3,6,1,4,1,27514,1,1,10,2,51,1,2,1,22),_QtechSyncStatsTxUnderrunErrors_Type())
qtechSyncStatsTxUnderrunErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSyncStatsTxUnderrunErrors.setStatus(_B)
_QtechSyncStatsMibConformance_ObjectIdentity=ObjectIdentity
qtechSyncStatsMibConformance=_QtechSyncStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,51,2))
_QtechSyncStatsMibCompliances_ObjectIdentity=ObjectIdentity
qtechSyncStatsMibCompliances=_QtechSyncStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,51,2,1))
_QtechSyncStatsMibGroups_ObjectIdentity=ObjectIdentity
qtechSyncStatsMibGroups=_QtechSyncStatsMibGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,51,2,2))
qtechSyncStatsGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,51,2,2,1))
qtechSyncStatsGroup.setObjects(*((_A,_H),(_A,_E),(_A,_F),(_A,_G),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:qtechSyncStatsGroup.setStatus(_B)
qtechSyncStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,51,2,1,1))
qtechSyncStatsMibCompliance.setObjects((_A,_a))
if mibBuilder.loadTexts:qtechSyncStatsMibCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'qtechSyncStatsMIB':qtechSyncStatsMIB,'qtechSyncStatsMibObjects':qtechSyncStatsMibObjects,'qtechStatsSyncGlobal':qtechStatsSyncGlobal,'qtechSyncStatsTable':qtechSyncStatsTable,'qtechSyncStatsEntry':qtechSyncStatsEntry,_H:qtechSyncStatsRowStatus,_E:qtechSyncStatsSlot,_F:qtechSyncStatsConn,_G:qtechSyncStatsChannel,_I:qtechSyncStatsIfIndex,_J:qtechSyncStatsPortState,_K:qtechSyncStatsRxFrames,_L:qtechSyncStatsRxOctets,_M:qtechSyncStatsRxReplenFails,_N:qtechSyncStatsRxClockErrors,_O:qtechSyncStatsRxDpllErrors,_P:qtechSyncStatsRxFrameTooLongErrors,_Q:qtechSyncStatsRxFrameOctetAlignErrors,_R:qtechSyncStatsRxAbortErrors,_S:qtechSyncStatsRxCrcErrors,_T:qtechSyncStatsRxRcvrOverrunErrors,_U:qtechSyncStatsTxFrames,_V:qtechSyncStatsTxOctets,_W:qtechSyncStatsTxRingFullDropsErrors,_X:qtechSyncStatsTxClockErrors,_Y:qtechSyncStatsTxFrameTooLongErrors,_Z:qtechSyncStatsTxUnderrunErrors,'qtechSyncStatsMibConformance':qtechSyncStatsMibConformance,'qtechSyncStatsMibCompliances':qtechSyncStatsMibCompliances,'qtechSyncStatsMibCompliance':qtechSyncStatsMibCompliance,'qtechSyncStatsMibGroups':qtechSyncStatsMibGroups,_a:qtechSyncStatsGroup})