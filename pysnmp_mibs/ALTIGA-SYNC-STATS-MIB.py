_a='altigaSyncStatsGroup'
_Z='alSyncStatsTxUnderrunErrors'
_Y='alSyncStatsTxFrameTooLongErrors'
_X='alSyncStatsTxClockErrors'
_W='alSyncStatsTxRingFullDropsErrors'
_V='alSyncStatsTxOctets'
_U='alSyncStatsTxFrames'
_T='alSyncStatsRxRcvrOverrunErrors'
_S='alSyncStatsRxCrcErrors'
_R='alSyncStatsRxAbortErrors'
_Q='alSyncStatsRxFrameOctetAlignErrors'
_P='alSyncStatsRxFrameTooLongErrors'
_O='alSyncStatsRxDpllErrors'
_N='alSyncStatsRxClockErrors'
_M='alSyncStatsRxReplenFails'
_L='alSyncStatsRxOctets'
_K='alSyncStatsRxFrames'
_J='alSyncStatsPortState'
_I='alSyncStatsIfIndex'
_H='alSyncStatsRowStatus'
_G='alSyncStatsChannel'
_F='alSyncStatsConn'
_E='alSyncStatsSlot'
_D='Integer32'
_C='read-only'
_B='current'
_A='ALTIGA-SYNC-STATS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alSyncMibModule,=mibBuilder.importSymbols('ALTIGA-GLOBAL-REG','alSyncMibModule')
alStatsSync,alSyncGroup=mibBuilder.importSymbols('ALTIGA-MIB','alStatsSync','alSyncGroup')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
altigaSyncStatsMibModule=ModuleIdentity((1,3,6,1,4,1,3076,1,1,37,2))
if mibBuilder.loadTexts:altigaSyncStatsMibModule.setRevisions(('2002-09-05 13:00','2002-07-10 00:00'))
_AltigaSyncStatsMibConformance_ObjectIdentity=ObjectIdentity
altigaSyncStatsMibConformance=_AltigaSyncStatsMibConformance_ObjectIdentity((1,3,6,1,4,1,3076,1,1,37,2,1))
_AltigaSyncStatsMibCompliances_ObjectIdentity=ObjectIdentity
altigaSyncStatsMibCompliances=_AltigaSyncStatsMibCompliances_ObjectIdentity((1,3,6,1,4,1,3076,1,1,37,2,1,1))
_AlStatsSyncGlobal_ObjectIdentity=ObjectIdentity
alStatsSyncGlobal=_AlStatsSyncGlobal_ObjectIdentity((1,3,6,1,4,1,3076,2,1,2,32,1))
_AlSyncStatsTable_Object=MibTable
alSyncStatsTable=_AlSyncStatsTable_Object((1,3,6,1,4,1,3076,2,1,2,32,2))
if mibBuilder.loadTexts:alSyncStatsTable.setStatus(_B)
_AlSyncStatsEntry_Object=MibTableRow
alSyncStatsEntry=_AlSyncStatsEntry_Object((1,3,6,1,4,1,3076,2,1,2,32,2,1))
alSyncStatsEntry.setIndexNames((0,_A,_E),(0,_A,_F),(0,_A,_G))
if mibBuilder.loadTexts:alSyncStatsEntry.setStatus(_B)
_AlSyncStatsRowStatus_Type=RowStatus
_AlSyncStatsRowStatus_Object=MibTableColumn
alSyncStatsRowStatus=_AlSyncStatsRowStatus_Object((1,3,6,1,4,1,3076,2,1,2,32,2,1,1),_AlSyncStatsRowStatus_Type())
alSyncStatsRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:alSyncStatsRowStatus.setStatus(_B)
class _AlSyncStatsSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AlSyncStatsSlot_Type.__name__=_D
_AlSyncStatsSlot_Object=MibTableColumn
alSyncStatsSlot=_AlSyncStatsSlot_Object((1,3,6,1,4,1,3076,2,1,2,32,2,1,2),_AlSyncStatsSlot_Type())
alSyncStatsSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:alSyncStatsSlot.setStatus(_B)
class _AlSyncStatsConn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AlSyncStatsConn_Type.__name__=_D
_AlSyncStatsConn_Object=MibTableColumn
alSyncStatsConn=_AlSyncStatsConn_Object((1,3,6,1,4,1,3076,2,1,2,32,2,1,3),_AlSyncStatsConn_Type())
alSyncStatsConn.setMaxAccess(_C)
if mibBuilder.loadTexts:alSyncStatsConn.setStatus(_B)
class _AlSyncStatsChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_AlSyncStatsChannel_Type.__name__=_D
_AlSyncStatsChannel_Object=MibTableColumn
alSyncStatsChannel=_AlSyncStatsChannel_Object((1,3,6,1,4,1,3076,2,1,2,32,2,1,4),_AlSyncStatsChannel_Type())
alSyncStatsChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:alSyncStatsChannel.setStatus(_B)
_AlSyncStatsIfIndex_Type=InterfaceIndex
_AlSyncStatsIfIndex_Object=MibTableColumn
alSyncStatsIfIndex=_AlSyncStatsIfIndex_Object((1,3,6,1,4,1,3076,2,1,2,32,2,1,5),_AlSyncStatsIfIndex_Type())
alSyncStatsIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:alSyncStatsIfIndex.setStatus(_B)
class _AlSyncStatsPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('init',1),('running',2),('up',3),('down',4)))
_AlSyncStatsPortState_Type.__name__=_D
_AlSyncStatsPortState_Object=MibTableColumn
alSyncStatsPortState=_AlSyncStatsPortState_Object((1,3,6,1,4,1,3076,2,1,2,32,2,1,6),_AlSyncStatsPortState_Type())
alSyncStatsPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:alSyncStatsPortState.setStatus(_B)
_AlSyncStatsRxFrames_Type=Counter32
_AlSyncStatsRxFrames_Object=MibTableColumn
alSyncStatsRxFrames=_AlSyncStatsRxFrames_Object((1,3,6,1,4,1,3076,2,1,2,32,2,1,7),_AlSyncStatsRxFrames_Type())
alSyncStatsRxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:alSyncStatsRxFrames.setStatus(_B)
_AlSyncStatsRxOctets_Type=Counter32
_AlSyncStatsRxOctets_Object=MibTableColumn
alSyncStatsRxOctets=_AlSyncStatsRxOctets_Object((1,3,6,1,4,1,3076,2,1,2,32,2,1,8),_AlSyncStatsRxOctets_Type())
alSyncStatsRxOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alSyncStatsRxOctets.setStatus(_B)
_AlSyncStatsRxReplenFails_Type=Counter32
_AlSyncStatsRxReplenFails_Object=MibTableColumn
alSyncStatsRxReplenFails=_AlSyncStatsRxReplenFails_Object((1,3,6,1,4,1,3076,2,1,2,32,2,1,9),_AlSyncStatsRxReplenFails_Type())
alSyncStatsRxReplenFails.setMaxAccess(_C)
if mibBuilder.loadTexts:alSyncStatsRxReplenFails.setStatus(_B)
_AlSyncStatsRxClockErrors_Type=Counter32
_AlSyncStatsRxClockErrors_Object=MibTableColumn
alSyncStatsRxClockErrors=_AlSyncStatsRxClockErrors_Object((1,3,6,1,4,1,3076,2,1,2,32,2,1,10),_AlSyncStatsRxClockErrors_Type())
alSyncStatsRxClockErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:alSyncStatsRxClockErrors.setStatus(_B)
_AlSyncStatsRxDpllErrors_Type=Counter32
_AlSyncStatsRxDpllErrors_Object=MibTableColumn
alSyncStatsRxDpllErrors=_AlSyncStatsRxDpllErrors_Object((1,3,6,1,4,1,3076,2,1,2,32,2,1,11),_AlSyncStatsRxDpllErrors_Type())
alSyncStatsRxDpllErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:alSyncStatsRxDpllErrors.setStatus(_B)
_AlSyncStatsRxFrameTooLongErrors_Type=Counter32
_AlSyncStatsRxFrameTooLongErrors_Object=MibTableColumn
alSyncStatsRxFrameTooLongErrors=_AlSyncStatsRxFrameTooLongErrors_Object((1,3,6,1,4,1,3076,2,1,2,32,2,1,12),_AlSyncStatsRxFrameTooLongErrors_Type())
alSyncStatsRxFrameTooLongErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:alSyncStatsRxFrameTooLongErrors.setStatus(_B)
_AlSyncStatsRxFrameOctetAlignErrors_Type=Counter32
_AlSyncStatsRxFrameOctetAlignErrors_Object=MibTableColumn
alSyncStatsRxFrameOctetAlignErrors=_AlSyncStatsRxFrameOctetAlignErrors_Object((1,3,6,1,4,1,3076,2,1,2,32,2,1,13),_AlSyncStatsRxFrameOctetAlignErrors_Type())
alSyncStatsRxFrameOctetAlignErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:alSyncStatsRxFrameOctetAlignErrors.setStatus(_B)
_AlSyncStatsRxAbortErrors_Type=Counter32
_AlSyncStatsRxAbortErrors_Object=MibTableColumn
alSyncStatsRxAbortErrors=_AlSyncStatsRxAbortErrors_Object((1,3,6,1,4,1,3076,2,1,2,32,2,1,14),_AlSyncStatsRxAbortErrors_Type())
alSyncStatsRxAbortErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:alSyncStatsRxAbortErrors.setStatus(_B)
_AlSyncStatsRxCrcErrors_Type=Counter32
_AlSyncStatsRxCrcErrors_Object=MibTableColumn
alSyncStatsRxCrcErrors=_AlSyncStatsRxCrcErrors_Object((1,3,6,1,4,1,3076,2,1,2,32,2,1,15),_AlSyncStatsRxCrcErrors_Type())
alSyncStatsRxCrcErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:alSyncStatsRxCrcErrors.setStatus(_B)
_AlSyncStatsRxRcvrOverrunErrors_Type=Counter32
_AlSyncStatsRxRcvrOverrunErrors_Object=MibTableColumn
alSyncStatsRxRcvrOverrunErrors=_AlSyncStatsRxRcvrOverrunErrors_Object((1,3,6,1,4,1,3076,2,1,2,32,2,1,16),_AlSyncStatsRxRcvrOverrunErrors_Type())
alSyncStatsRxRcvrOverrunErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:alSyncStatsRxRcvrOverrunErrors.setStatus(_B)
_AlSyncStatsTxFrames_Type=Counter32
_AlSyncStatsTxFrames_Object=MibTableColumn
alSyncStatsTxFrames=_AlSyncStatsTxFrames_Object((1,3,6,1,4,1,3076,2,1,2,32,2,1,17),_AlSyncStatsTxFrames_Type())
alSyncStatsTxFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:alSyncStatsTxFrames.setStatus(_B)
_AlSyncStatsTxOctets_Type=Counter32
_AlSyncStatsTxOctets_Object=MibTableColumn
alSyncStatsTxOctets=_AlSyncStatsTxOctets_Object((1,3,6,1,4,1,3076,2,1,2,32,2,1,18),_AlSyncStatsTxOctets_Type())
alSyncStatsTxOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:alSyncStatsTxOctets.setStatus(_B)
_AlSyncStatsTxRingFullDropsErrors_Type=Counter32
_AlSyncStatsTxRingFullDropsErrors_Object=MibTableColumn
alSyncStatsTxRingFullDropsErrors=_AlSyncStatsTxRingFullDropsErrors_Object((1,3,6,1,4,1,3076,2,1,2,32,2,1,19),_AlSyncStatsTxRingFullDropsErrors_Type())
alSyncStatsTxRingFullDropsErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:alSyncStatsTxRingFullDropsErrors.setStatus(_B)
_AlSyncStatsTxClockErrors_Type=Counter32
_AlSyncStatsTxClockErrors_Object=MibTableColumn
alSyncStatsTxClockErrors=_AlSyncStatsTxClockErrors_Object((1,3,6,1,4,1,3076,2,1,2,32,2,1,20),_AlSyncStatsTxClockErrors_Type())
alSyncStatsTxClockErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:alSyncStatsTxClockErrors.setStatus(_B)
_AlSyncStatsTxFrameTooLongErrors_Type=Counter32
_AlSyncStatsTxFrameTooLongErrors_Object=MibTableColumn
alSyncStatsTxFrameTooLongErrors=_AlSyncStatsTxFrameTooLongErrors_Object((1,3,6,1,4,1,3076,2,1,2,32,2,1,21),_AlSyncStatsTxFrameTooLongErrors_Type())
alSyncStatsTxFrameTooLongErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:alSyncStatsTxFrameTooLongErrors.setStatus(_B)
_AlSyncStatsTxUnderrunErrors_Type=Counter32
_AlSyncStatsTxUnderrunErrors_Object=MibTableColumn
alSyncStatsTxUnderrunErrors=_AlSyncStatsTxUnderrunErrors_Object((1,3,6,1,4,1,3076,2,1,2,32,2,1,22),_AlSyncStatsTxUnderrunErrors_Type())
alSyncStatsTxUnderrunErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:alSyncStatsTxUnderrunErrors.setStatus(_B)
altigaSyncStatsGroup=ObjectGroup((1,3,6,1,4,1,3076,2,1,1,1,32,2))
altigaSyncStatsGroup.setObjects(*((_A,_H),(_A,_E),(_A,_F),(_A,_G),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:altigaSyncStatsGroup.setStatus(_B)
altigaSyncStatsMibCompliance=ModuleCompliance((1,3,6,1,4,1,3076,1,1,37,2,1,1,1))
altigaSyncStatsMibCompliance.setObjects((_A,_a))
if mibBuilder.loadTexts:altigaSyncStatsMibCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'altigaSyncStatsMibModule':altigaSyncStatsMibModule,'altigaSyncStatsMibConformance':altigaSyncStatsMibConformance,'altigaSyncStatsMibCompliances':altigaSyncStatsMibCompliances,'altigaSyncStatsMibCompliance':altigaSyncStatsMibCompliance,_a:altigaSyncStatsGroup,'alStatsSyncGlobal':alStatsSyncGlobal,'alSyncStatsTable':alSyncStatsTable,'alSyncStatsEntry':alSyncStatsEntry,_H:alSyncStatsRowStatus,_E:alSyncStatsSlot,_F:alSyncStatsConn,_G:alSyncStatsChannel,_I:alSyncStatsIfIndex,_J:alSyncStatsPortState,_K:alSyncStatsRxFrames,_L:alSyncStatsRxOctets,_M:alSyncStatsRxReplenFails,_N:alSyncStatsRxClockErrors,_O:alSyncStatsRxDpllErrors,_P:alSyncStatsRxFrameTooLongErrors,_Q:alSyncStatsRxFrameOctetAlignErrors,_R:alSyncStatsRxAbortErrors,_S:alSyncStatsRxCrcErrors,_T:alSyncStatsRxRcvrOverrunErrors,_U:alSyncStatsTxFrames,_V:alSyncStatsTxOctets,_W:alSyncStatsTxRingFullDropsErrors,_X:alSyncStatsTxClockErrors,_Y:alSyncStatsTxFrameTooLongErrors,_Z:alSyncStatsTxUnderrunErrors})