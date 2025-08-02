_I='oraDbLibraryCacheIndex'
_H='oraDbDataFileIndex'
_G='oraDbTablespaceIndex'
_F='ORADB-MIB'
_E='Integer32'
_D='rdbmsDbIndex'
_C='RDBMS-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rdbmsDbIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','experimental','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class DateAndTime(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,11))
class TruthValue(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_Oracle_ObjectIdentity=ObjectIdentity
oracle=_Oracle_ObjectIdentity((1,3,6,1,4,1,111))
_OraDbMIB_ObjectIdentity=ObjectIdentity
oraDbMIB=_OraDbMIB_ObjectIdentity((1,3,6,1,4,1,111,4))
_OraDbObjects_ObjectIdentity=ObjectIdentity
oraDbObjects=_OraDbObjects_ObjectIdentity((1,3,6,1,4,1,111,4,1))
_OraDbSysTable_Object=MibTable
oraDbSysTable=_OraDbSysTable_Object((1,3,6,1,4,1,111,4,1,1))
if mibBuilder.loadTexts:oraDbSysTable.setStatus(_A)
_OraDbSysEntry_Object=MibTableRow
oraDbSysEntry=_OraDbSysEntry_Object((1,3,6,1,4,1,111,4,1,1,1))
oraDbSysEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:oraDbSysEntry.setStatus(_A)
_OraDbSysConsistentChanges_Type=Counter32
_OraDbSysConsistentChanges_Object=MibTableColumn
oraDbSysConsistentChanges=_OraDbSysConsistentChanges_Object((1,3,6,1,4,1,111,4,1,1,1,1),_OraDbSysConsistentChanges_Type())
oraDbSysConsistentChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSysConsistentChanges.setStatus(_A)
_OraDbSysConsistentGets_Type=Counter32
_OraDbSysConsistentGets_Object=MibTableColumn
oraDbSysConsistentGets=_OraDbSysConsistentGets_Object((1,3,6,1,4,1,111,4,1,1,1,2),_OraDbSysConsistentGets_Type())
oraDbSysConsistentGets.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSysConsistentGets.setStatus(_A)
_OraDbSysDbBlockChanges_Type=Counter32
_OraDbSysDbBlockChanges_Object=MibTableColumn
oraDbSysDbBlockChanges=_OraDbSysDbBlockChanges_Object((1,3,6,1,4,1,111,4,1,1,1,3),_OraDbSysDbBlockChanges_Type())
oraDbSysDbBlockChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSysDbBlockChanges.setStatus(_A)
_OraDbSysDbBlockGets_Type=Counter32
_OraDbSysDbBlockGets_Object=MibTableColumn
oraDbSysDbBlockGets=_OraDbSysDbBlockGets_Object((1,3,6,1,4,1,111,4,1,1,1,4),_OraDbSysDbBlockGets_Type())
oraDbSysDbBlockGets.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSysDbBlockGets.setStatus(_A)
_OraDbSysFreeBufferInspected_Type=Counter32
_OraDbSysFreeBufferInspected_Object=MibTableColumn
oraDbSysFreeBufferInspected=_OraDbSysFreeBufferInspected_Object((1,3,6,1,4,1,111,4,1,1,1,5),_OraDbSysFreeBufferInspected_Type())
oraDbSysFreeBufferInspected.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSysFreeBufferInspected.setStatus(_A)
_OraDbSysFreeBufferRequested_Type=Counter32
_OraDbSysFreeBufferRequested_Object=MibTableColumn
oraDbSysFreeBufferRequested=_OraDbSysFreeBufferRequested_Object((1,3,6,1,4,1,111,4,1,1,1,6),_OraDbSysFreeBufferRequested_Type())
oraDbSysFreeBufferRequested.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSysFreeBufferRequested.setStatus(_A)
_OraDbSysParseCount_Type=Counter32
_OraDbSysParseCount_Object=MibTableColumn
oraDbSysParseCount=_OraDbSysParseCount_Object((1,3,6,1,4,1,111,4,1,1,1,7),_OraDbSysParseCount_Type())
oraDbSysParseCount.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSysParseCount.setStatus(_A)
_OraDbSysPhysReads_Type=Counter32
_OraDbSysPhysReads_Object=MibTableColumn
oraDbSysPhysReads=_OraDbSysPhysReads_Object((1,3,6,1,4,1,111,4,1,1,1,8),_OraDbSysPhysReads_Type())
oraDbSysPhysReads.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSysPhysReads.setStatus(_A)
_OraDbSysPhysWrites_Type=Counter32
_OraDbSysPhysWrites_Object=MibTableColumn
oraDbSysPhysWrites=_OraDbSysPhysWrites_Object((1,3,6,1,4,1,111,4,1,1,1,9),_OraDbSysPhysWrites_Type())
oraDbSysPhysWrites.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSysPhysWrites.setStatus(_A)
_OraDbSysRedoEntries_Type=Counter32
_OraDbSysRedoEntries_Object=MibTableColumn
oraDbSysRedoEntries=_OraDbSysRedoEntries_Object((1,3,6,1,4,1,111,4,1,1,1,10),_OraDbSysRedoEntries_Type())
oraDbSysRedoEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSysRedoEntries.setStatus(_A)
_OraDbSysRedoLogSpaceRequests_Type=Counter32
_OraDbSysRedoLogSpaceRequests_Object=MibTableColumn
oraDbSysRedoLogSpaceRequests=_OraDbSysRedoLogSpaceRequests_Object((1,3,6,1,4,1,111,4,1,1,1,11),_OraDbSysRedoLogSpaceRequests_Type())
oraDbSysRedoLogSpaceRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSysRedoLogSpaceRequests.setStatus(_A)
_OraDbSysRedoSyncWrites_Type=Counter32
_OraDbSysRedoSyncWrites_Object=MibTableColumn
oraDbSysRedoSyncWrites=_OraDbSysRedoSyncWrites_Object((1,3,6,1,4,1,111,4,1,1,1,12),_OraDbSysRedoSyncWrites_Type())
oraDbSysRedoSyncWrites.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSysRedoSyncWrites.setStatus(_A)
_OraDbSysSortsDisk_Type=Counter32
_OraDbSysSortsDisk_Object=MibTableColumn
oraDbSysSortsDisk=_OraDbSysSortsDisk_Object((1,3,6,1,4,1,111,4,1,1,1,13),_OraDbSysSortsDisk_Type())
oraDbSysSortsDisk.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSysSortsDisk.setStatus(_A)
_OraDbSysSortsMemory_Type=Counter32
_OraDbSysSortsMemory_Object=MibTableColumn
oraDbSysSortsMemory=_OraDbSysSortsMemory_Object((1,3,6,1,4,1,111,4,1,1,1,14),_OraDbSysSortsMemory_Type())
oraDbSysSortsMemory.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSysSortsMemory.setStatus(_A)
_OraDbSysSortsRows_Type=Counter32
_OraDbSysSortsRows_Object=MibTableColumn
oraDbSysSortsRows=_OraDbSysSortsRows_Object((1,3,6,1,4,1,111,4,1,1,1,15),_OraDbSysSortsRows_Type())
oraDbSysSortsRows.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSysSortsRows.setStatus(_A)
_OraDbSysTableFetchRowid_Type=Counter32
_OraDbSysTableFetchRowid_Object=MibTableColumn
oraDbSysTableFetchRowid=_OraDbSysTableFetchRowid_Object((1,3,6,1,4,1,111,4,1,1,1,16),_OraDbSysTableFetchRowid_Type())
oraDbSysTableFetchRowid.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSysTableFetchRowid.setStatus(_A)
_OraDbSysTableFetchContinuedRow_Type=Counter32
_OraDbSysTableFetchContinuedRow_Object=MibTableColumn
oraDbSysTableFetchContinuedRow=_OraDbSysTableFetchContinuedRow_Object((1,3,6,1,4,1,111,4,1,1,1,17),_OraDbSysTableFetchContinuedRow_Type())
oraDbSysTableFetchContinuedRow.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSysTableFetchContinuedRow.setStatus(_A)
_OraDbSysTableScanBlocks_Type=Counter32
_OraDbSysTableScanBlocks_Object=MibTableColumn
oraDbSysTableScanBlocks=_OraDbSysTableScanBlocks_Object((1,3,6,1,4,1,111,4,1,1,1,18),_OraDbSysTableScanBlocks_Type())
oraDbSysTableScanBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSysTableScanBlocks.setStatus(_A)
_OraDbSysTableScanRows_Type=Counter32
_OraDbSysTableScanRows_Object=MibTableColumn
oraDbSysTableScanRows=_OraDbSysTableScanRows_Object((1,3,6,1,4,1,111,4,1,1,1,19),_OraDbSysTableScanRows_Type())
oraDbSysTableScanRows.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSysTableScanRows.setStatus(_A)
_OraDbSysTableScansLong_Type=Counter32
_OraDbSysTableScansLong_Object=MibTableColumn
oraDbSysTableScansLong=_OraDbSysTableScansLong_Object((1,3,6,1,4,1,111,4,1,1,1,20),_OraDbSysTableScansLong_Type())
oraDbSysTableScansLong.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSysTableScansLong.setStatus(_A)
_OraDbSysTableScansShort_Type=Counter32
_OraDbSysTableScansShort_Object=MibTableColumn
oraDbSysTableScansShort=_OraDbSysTableScansShort_Object((1,3,6,1,4,1,111,4,1,1,1,21),_OraDbSysTableScansShort_Type())
oraDbSysTableScansShort.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSysTableScansShort.setStatus(_A)
_OraDbSysUserCalls_Type=Counter32
_OraDbSysUserCalls_Object=MibTableColumn
oraDbSysUserCalls=_OraDbSysUserCalls_Object((1,3,6,1,4,1,111,4,1,1,1,22),_OraDbSysUserCalls_Type())
oraDbSysUserCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSysUserCalls.setStatus(_A)
_OraDbSysUserCommits_Type=Counter32
_OraDbSysUserCommits_Object=MibTableColumn
oraDbSysUserCommits=_OraDbSysUserCommits_Object((1,3,6,1,4,1,111,4,1,1,1,23),_OraDbSysUserCommits_Type())
oraDbSysUserCommits.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSysUserCommits.setStatus(_A)
_OraDbSysUserRollbacks_Type=Counter32
_OraDbSysUserRollbacks_Object=MibTableColumn
oraDbSysUserRollbacks=_OraDbSysUserRollbacks_Object((1,3,6,1,4,1,111,4,1,1,1,24),_OraDbSysUserRollbacks_Type())
oraDbSysUserRollbacks.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSysUserRollbacks.setStatus(_A)
_OraDbSysWriteRequests_Type=Counter32
_OraDbSysWriteRequests_Object=MibTableColumn
oraDbSysWriteRequests=_OraDbSysWriteRequests_Object((1,3,6,1,4,1,111,4,1,1,1,25),_OraDbSysWriteRequests_Type())
oraDbSysWriteRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSysWriteRequests.setStatus(_A)
_OraDbTablespaceTable_Object=MibTable
oraDbTablespaceTable=_OraDbTablespaceTable_Object((1,3,6,1,4,1,111,4,1,2))
if mibBuilder.loadTexts:oraDbTablespaceTable.setStatus(_A)
_OraDbTablespaceEntry_Object=MibTableRow
oraDbTablespaceEntry=_OraDbTablespaceEntry_Object((1,3,6,1,4,1,111,4,1,2,1))
oraDbTablespaceEntry.setIndexNames((0,_C,_D),(0,_F,_G))
if mibBuilder.loadTexts:oraDbTablespaceEntry.setStatus(_A)
_OraDbTablespaceIndex_Type=Integer32
_OraDbTablespaceIndex_Object=MibTableColumn
oraDbTablespaceIndex=_OraDbTablespaceIndex_Object((1,3,6,1,4,1,111,4,1,2,1,1),_OraDbTablespaceIndex_Type())
oraDbTablespaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbTablespaceIndex.setStatus(_A)
_OraDbTablespaceName_Type=DisplayString
_OraDbTablespaceName_Object=MibTableColumn
oraDbTablespaceName=_OraDbTablespaceName_Object((1,3,6,1,4,1,111,4,1,2,1,2),_OraDbTablespaceName_Type())
oraDbTablespaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbTablespaceName.setStatus(_A)
class _OraDbTablespaceSizeAllocated_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_OraDbTablespaceSizeAllocated_Type.__name__=_E
_OraDbTablespaceSizeAllocated_Object=MibTableColumn
oraDbTablespaceSizeAllocated=_OraDbTablespaceSizeAllocated_Object((1,3,6,1,4,1,111,4,1,2,1,3),_OraDbTablespaceSizeAllocated_Type())
oraDbTablespaceSizeAllocated.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbTablespaceSizeAllocated.setStatus(_A)
class _OraDbTablespaceSizeUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_OraDbTablespaceSizeUsed_Type.__name__=_E
_OraDbTablespaceSizeUsed_Object=MibTableColumn
oraDbTablespaceSizeUsed=_OraDbTablespaceSizeUsed_Object((1,3,6,1,4,1,111,4,1,2,1,4),_OraDbTablespaceSizeUsed_Type())
oraDbTablespaceSizeUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbTablespaceSizeUsed.setStatus(_A)
class _OraDbTablespaceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('online',1),('offline',2),('invalid',3)))
_OraDbTablespaceState_Type.__name__=_E
_OraDbTablespaceState_Object=MibTableColumn
oraDbTablespaceState=_OraDbTablespaceState_Object((1,3,6,1,4,1,111,4,1,2,1,5),_OraDbTablespaceState_Type())
oraDbTablespaceState.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbTablespaceState.setStatus(_A)
class _OraDbTablespaceLargestAvailableChunk_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_OraDbTablespaceLargestAvailableChunk_Type.__name__=_E
_OraDbTablespaceLargestAvailableChunk_Object=MibTableColumn
oraDbTablespaceLargestAvailableChunk=_OraDbTablespaceLargestAvailableChunk_Object((1,3,6,1,4,1,111,4,1,2,1,6),_OraDbTablespaceLargestAvailableChunk_Type())
oraDbTablespaceLargestAvailableChunk.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbTablespaceLargestAvailableChunk.setStatus(_A)
_OraDbDataFileTable_Object=MibTable
oraDbDataFileTable=_OraDbDataFileTable_Object((1,3,6,1,4,1,111,4,1,3))
if mibBuilder.loadTexts:oraDbDataFileTable.setStatus(_A)
_OraDbDataFileEntry_Object=MibTableRow
oraDbDataFileEntry=_OraDbDataFileEntry_Object((1,3,6,1,4,1,111,4,1,3,1))
oraDbDataFileEntry.setIndexNames((0,_C,_D),(0,_F,_H))
if mibBuilder.loadTexts:oraDbDataFileEntry.setStatus(_A)
_OraDbDataFileIndex_Type=Integer32
_OraDbDataFileIndex_Object=MibTableColumn
oraDbDataFileIndex=_OraDbDataFileIndex_Object((1,3,6,1,4,1,111,4,1,3,1,1),_OraDbDataFileIndex_Type())
oraDbDataFileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbDataFileIndex.setStatus(_A)
_OraDbDataFileName_Type=DisplayString
_OraDbDataFileName_Object=MibTableColumn
oraDbDataFileName=_OraDbDataFileName_Object((1,3,6,1,4,1,111,4,1,3,1,2),_OraDbDataFileName_Type())
oraDbDataFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbDataFileName.setStatus(_A)
class _OraDbDataFileSizeAllocated_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_OraDbDataFileSizeAllocated_Type.__name__=_E
_OraDbDataFileSizeAllocated_Object=MibTableColumn
oraDbDataFileSizeAllocated=_OraDbDataFileSizeAllocated_Object((1,3,6,1,4,1,111,4,1,3,1,3),_OraDbDataFileSizeAllocated_Type())
oraDbDataFileSizeAllocated.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbDataFileSizeAllocated.setStatus(_A)
_OraDbDataFileDiskReads_Type=Counter32
_OraDbDataFileDiskReads_Object=MibTableColumn
oraDbDataFileDiskReads=_OraDbDataFileDiskReads_Object((1,3,6,1,4,1,111,4,1,3,1,4),_OraDbDataFileDiskReads_Type())
oraDbDataFileDiskReads.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbDataFileDiskReads.setStatus(_A)
_OraDbDataFileDiskWrites_Type=Counter32
_OraDbDataFileDiskWrites_Object=MibTableColumn
oraDbDataFileDiskWrites=_OraDbDataFileDiskWrites_Object((1,3,6,1,4,1,111,4,1,3,1,5),_OraDbDataFileDiskWrites_Type())
oraDbDataFileDiskWrites.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbDataFileDiskWrites.setStatus(_A)
_OraDbDataFileDiskReadBlocks_Type=Counter32
_OraDbDataFileDiskReadBlocks_Object=MibTableColumn
oraDbDataFileDiskReadBlocks=_OraDbDataFileDiskReadBlocks_Object((1,3,6,1,4,1,111,4,1,3,1,6),_OraDbDataFileDiskReadBlocks_Type())
oraDbDataFileDiskReadBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbDataFileDiskReadBlocks.setStatus(_A)
_OraDbDataFileDiskWrittenBlocks_Type=Counter32
_OraDbDataFileDiskWrittenBlocks_Object=MibTableColumn
oraDbDataFileDiskWrittenBlocks=_OraDbDataFileDiskWrittenBlocks_Object((1,3,6,1,4,1,111,4,1,3,1,7),_OraDbDataFileDiskWrittenBlocks_Type())
oraDbDataFileDiskWrittenBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbDataFileDiskWrittenBlocks.setStatus(_A)
_OraDbDataFileDiskReadTimeTicks_Type=Counter32
_OraDbDataFileDiskReadTimeTicks_Object=MibTableColumn
oraDbDataFileDiskReadTimeTicks=_OraDbDataFileDiskReadTimeTicks_Object((1,3,6,1,4,1,111,4,1,3,1,8),_OraDbDataFileDiskReadTimeTicks_Type())
oraDbDataFileDiskReadTimeTicks.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbDataFileDiskReadTimeTicks.setStatus(_A)
_OraDbDataFileDiskWriteTimeTicks_Type=Counter32
_OraDbDataFileDiskWriteTimeTicks_Object=MibTableColumn
oraDbDataFileDiskWriteTimeTicks=_OraDbDataFileDiskWriteTimeTicks_Object((1,3,6,1,4,1,111,4,1,3,1,9),_OraDbDataFileDiskWriteTimeTicks_Type())
oraDbDataFileDiskWriteTimeTicks.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbDataFileDiskWriteTimeTicks.setStatus(_A)
_OraDbLibraryCacheTable_Object=MibTable
oraDbLibraryCacheTable=_OraDbLibraryCacheTable_Object((1,3,6,1,4,1,111,4,1,4))
if mibBuilder.loadTexts:oraDbLibraryCacheTable.setStatus(_A)
_OraDbLibraryCacheEntry_Object=MibTableRow
oraDbLibraryCacheEntry=_OraDbLibraryCacheEntry_Object((1,3,6,1,4,1,111,4,1,4,1))
oraDbLibraryCacheEntry.setIndexNames((0,_C,_D),(0,_F,_I))
if mibBuilder.loadTexts:oraDbLibraryCacheEntry.setStatus(_A)
_OraDbLibraryCacheIndex_Type=Integer32
_OraDbLibraryCacheIndex_Object=MibTableColumn
oraDbLibraryCacheIndex=_OraDbLibraryCacheIndex_Object((1,3,6,1,4,1,111,4,1,4,1,1),_OraDbLibraryCacheIndex_Type())
oraDbLibraryCacheIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbLibraryCacheIndex.setStatus(_A)
_OraDbLibraryCacheNameSpace_Type=DisplayString
_OraDbLibraryCacheNameSpace_Object=MibTableColumn
oraDbLibraryCacheNameSpace=_OraDbLibraryCacheNameSpace_Object((1,3,6,1,4,1,111,4,1,4,1,2),_OraDbLibraryCacheNameSpace_Type())
oraDbLibraryCacheNameSpace.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbLibraryCacheNameSpace.setStatus(_A)
_OraDbLibraryCacheGets_Type=Counter32
_OraDbLibraryCacheGets_Object=MibTableColumn
oraDbLibraryCacheGets=_OraDbLibraryCacheGets_Object((1,3,6,1,4,1,111,4,1,4,1,3),_OraDbLibraryCacheGets_Type())
oraDbLibraryCacheGets.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbLibraryCacheGets.setStatus(_A)
_OraDbLibraryCacheGetHits_Type=Counter32
_OraDbLibraryCacheGetHits_Object=MibTableColumn
oraDbLibraryCacheGetHits=_OraDbLibraryCacheGetHits_Object((1,3,6,1,4,1,111,4,1,4,1,4),_OraDbLibraryCacheGetHits_Type())
oraDbLibraryCacheGetHits.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbLibraryCacheGetHits.setStatus(_A)
_OraDbLibraryCachePins_Type=Counter32
_OraDbLibraryCachePins_Object=MibTableColumn
oraDbLibraryCachePins=_OraDbLibraryCachePins_Object((1,3,6,1,4,1,111,4,1,4,1,5),_OraDbLibraryCachePins_Type())
oraDbLibraryCachePins.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbLibraryCachePins.setStatus(_A)
_OraDbLibraryCachePinHits_Type=Counter32
_OraDbLibraryCachePinHits_Object=MibTableColumn
oraDbLibraryCachePinHits=_OraDbLibraryCachePinHits_Object((1,3,6,1,4,1,111,4,1,4,1,6),_OraDbLibraryCachePinHits_Type())
oraDbLibraryCachePinHits.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbLibraryCachePinHits.setStatus(_A)
_OraDbLibraryCacheReloads_Type=Counter32
_OraDbLibraryCacheReloads_Object=MibTableColumn
oraDbLibraryCacheReloads=_OraDbLibraryCacheReloads_Object((1,3,6,1,4,1,111,4,1,4,1,7),_OraDbLibraryCacheReloads_Type())
oraDbLibraryCacheReloads.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbLibraryCacheReloads.setStatus(_A)
_OraDbLibraryCacheInvalidations_Type=Counter32
_OraDbLibraryCacheInvalidations_Object=MibTableColumn
oraDbLibraryCacheInvalidations=_OraDbLibraryCacheInvalidations_Object((1,3,6,1,4,1,111,4,1,4,1,8),_OraDbLibraryCacheInvalidations_Type())
oraDbLibraryCacheInvalidations.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbLibraryCacheInvalidations.setStatus(_A)
_OraDbLibraryCacheSumTable_Object=MibTable
oraDbLibraryCacheSumTable=_OraDbLibraryCacheSumTable_Object((1,3,6,1,4,1,111,4,1,5))
if mibBuilder.loadTexts:oraDbLibraryCacheSumTable.setStatus(_A)
_OraDbLibraryCacheSumEntry_Object=MibTableRow
oraDbLibraryCacheSumEntry=_OraDbLibraryCacheSumEntry_Object((1,3,6,1,4,1,111,4,1,5,1))
oraDbLibraryCacheSumEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:oraDbLibraryCacheSumEntry.setStatus(_A)
_OraDbLibraryCacheSumGets_Type=Counter32
_OraDbLibraryCacheSumGets_Object=MibTableColumn
oraDbLibraryCacheSumGets=_OraDbLibraryCacheSumGets_Object((1,3,6,1,4,1,111,4,1,5,1,1),_OraDbLibraryCacheSumGets_Type())
oraDbLibraryCacheSumGets.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbLibraryCacheSumGets.setStatus(_A)
_OraDbLibraryCacheSumGetHits_Type=Counter32
_OraDbLibraryCacheSumGetHits_Object=MibTableColumn
oraDbLibraryCacheSumGetHits=_OraDbLibraryCacheSumGetHits_Object((1,3,6,1,4,1,111,4,1,5,1,2),_OraDbLibraryCacheSumGetHits_Type())
oraDbLibraryCacheSumGetHits.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbLibraryCacheSumGetHits.setStatus(_A)
_OraDbLibraryCacheSumPins_Type=Counter32
_OraDbLibraryCacheSumPins_Object=MibTableColumn
oraDbLibraryCacheSumPins=_OraDbLibraryCacheSumPins_Object((1,3,6,1,4,1,111,4,1,5,1,3),_OraDbLibraryCacheSumPins_Type())
oraDbLibraryCacheSumPins.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbLibraryCacheSumPins.setStatus(_A)
_OraDbLibraryCacheSumPinHits_Type=Counter32
_OraDbLibraryCacheSumPinHits_Object=MibTableColumn
oraDbLibraryCacheSumPinHits=_OraDbLibraryCacheSumPinHits_Object((1,3,6,1,4,1,111,4,1,5,1,4),_OraDbLibraryCacheSumPinHits_Type())
oraDbLibraryCacheSumPinHits.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbLibraryCacheSumPinHits.setStatus(_A)
_OraDbLibraryCacheSumReloads_Type=Counter32
_OraDbLibraryCacheSumReloads_Object=MibTableColumn
oraDbLibraryCacheSumReloads=_OraDbLibraryCacheSumReloads_Object((1,3,6,1,4,1,111,4,1,5,1,5),_OraDbLibraryCacheSumReloads_Type())
oraDbLibraryCacheSumReloads.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbLibraryCacheSumReloads.setStatus(_A)
_OraDbLibraryCacheSumInvalidations_Type=Counter32
_OraDbLibraryCacheSumInvalidations_Object=MibTableColumn
oraDbLibraryCacheSumInvalidations=_OraDbLibraryCacheSumInvalidations_Object((1,3,6,1,4,1,111,4,1,5,1,6),_OraDbLibraryCacheSumInvalidations_Type())
oraDbLibraryCacheSumInvalidations.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbLibraryCacheSumInvalidations.setStatus(_A)
_OraDbSGATable_Object=MibTable
oraDbSGATable=_OraDbSGATable_Object((1,3,6,1,4,1,111,4,1,6))
if mibBuilder.loadTexts:oraDbSGATable.setStatus(_A)
_OraDbSGAEntry_Object=MibTableRow
oraDbSGAEntry=_OraDbSGAEntry_Object((1,3,6,1,4,1,111,4,1,6,1))
oraDbSGAEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:oraDbSGAEntry.setStatus(_A)
_OraDbSGAFixedSize_Type=Integer32
_OraDbSGAFixedSize_Object=MibTableColumn
oraDbSGAFixedSize=_OraDbSGAFixedSize_Object((1,3,6,1,4,1,111,4,1,6,1,1),_OraDbSGAFixedSize_Type())
oraDbSGAFixedSize.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSGAFixedSize.setStatus(_A)
_OraDbSGAVariableSize_Type=Integer32
_OraDbSGAVariableSize_Object=MibTableColumn
oraDbSGAVariableSize=_OraDbSGAVariableSize_Object((1,3,6,1,4,1,111,4,1,6,1,2),_OraDbSGAVariableSize_Type())
oraDbSGAVariableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSGAVariableSize.setStatus(_A)
_OraDbSGADatabaseBuffers_Type=Integer32
_OraDbSGADatabaseBuffers_Object=MibTableColumn
oraDbSGADatabaseBuffers=_OraDbSGADatabaseBuffers_Object((1,3,6,1,4,1,111,4,1,6,1,3),_OraDbSGADatabaseBuffers_Type())
oraDbSGADatabaseBuffers.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSGADatabaseBuffers.setStatus(_A)
_OraDbSGARedoBuffers_Type=Integer32
_OraDbSGARedoBuffers_Object=MibTableColumn
oraDbSGARedoBuffers=_OraDbSGARedoBuffers_Object((1,3,6,1,4,1,111,4,1,6,1,4),_OraDbSGARedoBuffers_Type())
oraDbSGARedoBuffers.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbSGARedoBuffers.setStatus(_A)
_OraDbConfigTable_Object=MibTable
oraDbConfigTable=_OraDbConfigTable_Object((1,3,6,1,4,1,111,4,1,7))
if mibBuilder.loadTexts:oraDbConfigTable.setStatus(_A)
_OraDbConfigEntry_Object=MibTableRow
oraDbConfigEntry=_OraDbConfigEntry_Object((1,3,6,1,4,1,111,4,1,7,1))
oraDbConfigEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:oraDbConfigEntry.setStatus(_A)
_OraDbConfigDbBlockBuffers_Type=Integer32
_OraDbConfigDbBlockBuffers_Object=MibTableColumn
oraDbConfigDbBlockBuffers=_OraDbConfigDbBlockBuffers_Object((1,3,6,1,4,1,111,4,1,7,1,1),_OraDbConfigDbBlockBuffers_Type())
oraDbConfigDbBlockBuffers.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigDbBlockBuffers.setStatus(_A)
_OraDbConfigDbBlockCkptBatch_Type=Integer32
_OraDbConfigDbBlockCkptBatch_Object=MibTableColumn
oraDbConfigDbBlockCkptBatch=_OraDbConfigDbBlockCkptBatch_Object((1,3,6,1,4,1,111,4,1,7,1,2),_OraDbConfigDbBlockCkptBatch_Type())
oraDbConfigDbBlockCkptBatch.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigDbBlockCkptBatch.setStatus(_A)
_OraDbConfigDbBlockSize_Type=Integer32
_OraDbConfigDbBlockSize_Object=MibTableColumn
oraDbConfigDbBlockSize=_OraDbConfigDbBlockSize_Object((1,3,6,1,4,1,111,4,1,7,1,3),_OraDbConfigDbBlockSize_Type())
oraDbConfigDbBlockSize.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigDbBlockSize.setStatus(_A)
_OraDbConfigDbFileSimWrites_Type=Integer32
_OraDbConfigDbFileSimWrites_Object=MibTableColumn
oraDbConfigDbFileSimWrites=_OraDbConfigDbFileSimWrites_Object((1,3,6,1,4,1,111,4,1,7,1,4),_OraDbConfigDbFileSimWrites_Type())
oraDbConfigDbFileSimWrites.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigDbFileSimWrites.setStatus(_A)
_OraDbConfigDbMultiBlockReadCount_Type=Integer32
_OraDbConfigDbMultiBlockReadCount_Object=MibTableColumn
oraDbConfigDbMultiBlockReadCount=_OraDbConfigDbMultiBlockReadCount_Object((1,3,6,1,4,1,111,4,1,7,1,5),_OraDbConfigDbMultiBlockReadCount_Type())
oraDbConfigDbMultiBlockReadCount.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigDbMultiBlockReadCount.setStatus(_A)
_OraDbConfigDistLockTimeout_Type=Integer32
_OraDbConfigDistLockTimeout_Object=MibTableColumn
oraDbConfigDistLockTimeout=_OraDbConfigDistLockTimeout_Object((1,3,6,1,4,1,111,4,1,7,1,6),_OraDbConfigDistLockTimeout_Type())
oraDbConfigDistLockTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigDistLockTimeout.setStatus(_A)
_OraDbConfigDistRecoveryConnectHold_Type=Integer32
_OraDbConfigDistRecoveryConnectHold_Object=MibTableColumn
oraDbConfigDistRecoveryConnectHold=_OraDbConfigDistRecoveryConnectHold_Object((1,3,6,1,4,1,111,4,1,7,1,7),_OraDbConfigDistRecoveryConnectHold_Type())
oraDbConfigDistRecoveryConnectHold.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigDistRecoveryConnectHold.setStatus(_A)
_OraDbConfigDistTransactions_Type=Integer32
_OraDbConfigDistTransactions_Object=MibTableColumn
oraDbConfigDistTransactions=_OraDbConfigDistTransactions_Object((1,3,6,1,4,1,111,4,1,7,1,8),_OraDbConfigDistTransactions_Type())
oraDbConfigDistTransactions.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigDistTransactions.setStatus(_A)
_OraDbConfigLogArchiveBufferSize_Type=Integer32
_OraDbConfigLogArchiveBufferSize_Object=MibTableColumn
oraDbConfigLogArchiveBufferSize=_OraDbConfigLogArchiveBufferSize_Object((1,3,6,1,4,1,111,4,1,7,1,9),_OraDbConfigLogArchiveBufferSize_Type())
oraDbConfigLogArchiveBufferSize.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigLogArchiveBufferSize.setStatus(_A)
_OraDbConfigLogArchiveBuffers_Type=Integer32
_OraDbConfigLogArchiveBuffers_Object=MibTableColumn
oraDbConfigLogArchiveBuffers=_OraDbConfigLogArchiveBuffers_Object((1,3,6,1,4,1,111,4,1,7,1,10),_OraDbConfigLogArchiveBuffers_Type())
oraDbConfigLogArchiveBuffers.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigLogArchiveBuffers.setStatus(_A)
_OraDbConfigLogBuffer_Type=Integer32
_OraDbConfigLogBuffer_Object=MibTableColumn
oraDbConfigLogBuffer=_OraDbConfigLogBuffer_Object((1,3,6,1,4,1,111,4,1,7,1,11),_OraDbConfigLogBuffer_Type())
oraDbConfigLogBuffer.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigLogBuffer.setStatus(_A)
_OraDbConfigLogCheckpointInterval_Type=Integer32
_OraDbConfigLogCheckpointInterval_Object=MibTableColumn
oraDbConfigLogCheckpointInterval=_OraDbConfigLogCheckpointInterval_Object((1,3,6,1,4,1,111,4,1,7,1,12),_OraDbConfigLogCheckpointInterval_Type())
oraDbConfigLogCheckpointInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigLogCheckpointInterval.setStatus(_A)
_OraDbConfigLogCheckpointTimeout_Type=Integer32
_OraDbConfigLogCheckpointTimeout_Object=MibTableColumn
oraDbConfigLogCheckpointTimeout=_OraDbConfigLogCheckpointTimeout_Object((1,3,6,1,4,1,111,4,1,7,1,13),_OraDbConfigLogCheckpointTimeout_Type())
oraDbConfigLogCheckpointTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigLogCheckpointTimeout.setStatus(_A)
_OraDbConfigLogFiles_Type=Integer32
_OraDbConfigLogFiles_Object=MibTableColumn
oraDbConfigLogFiles=_OraDbConfigLogFiles_Object((1,3,6,1,4,1,111,4,1,7,1,14),_OraDbConfigLogFiles_Type())
oraDbConfigLogFiles.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigLogFiles.setStatus(_A)
_OraDbConfigMaxRollbackSegments_Type=Integer32
_OraDbConfigMaxRollbackSegments_Object=MibTableColumn
oraDbConfigMaxRollbackSegments=_OraDbConfigMaxRollbackSegments_Object((1,3,6,1,4,1,111,4,1,7,1,15),_OraDbConfigMaxRollbackSegments_Type())
oraDbConfigMaxRollbackSegments.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigMaxRollbackSegments.setStatus(_A)
_OraDbConfigMTSMaxDispatchers_Type=Integer32
_OraDbConfigMTSMaxDispatchers_Object=MibTableColumn
oraDbConfigMTSMaxDispatchers=_OraDbConfigMTSMaxDispatchers_Object((1,3,6,1,4,1,111,4,1,7,1,16),_OraDbConfigMTSMaxDispatchers_Type())
oraDbConfigMTSMaxDispatchers.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigMTSMaxDispatchers.setStatus(_A)
_OraDbConfigMTSMaxServers_Type=Integer32
_OraDbConfigMTSMaxServers_Object=MibTableColumn
oraDbConfigMTSMaxServers=_OraDbConfigMTSMaxServers_Object((1,3,6,1,4,1,111,4,1,7,1,17),_OraDbConfigMTSMaxServers_Type())
oraDbConfigMTSMaxServers.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigMTSMaxServers.setStatus(_A)
_OraDbConfigMTSServers_Type=Integer32
_OraDbConfigMTSServers_Object=MibTableColumn
oraDbConfigMTSServers=_OraDbConfigMTSServers_Object((1,3,6,1,4,1,111,4,1,7,1,18),_OraDbConfigMTSServers_Type())
oraDbConfigMTSServers.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigMTSServers.setStatus(_A)
_OraDbConfigOpenCursors_Type=Integer32
_OraDbConfigOpenCursors_Object=MibTableColumn
oraDbConfigOpenCursors=_OraDbConfigOpenCursors_Object((1,3,6,1,4,1,111,4,1,7,1,19),_OraDbConfigOpenCursors_Type())
oraDbConfigOpenCursors.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigOpenCursors.setStatus(_A)
_OraDbConfigOpenLinks_Type=Integer32
_OraDbConfigOpenLinks_Object=MibTableColumn
oraDbConfigOpenLinks=_OraDbConfigOpenLinks_Object((1,3,6,1,4,1,111,4,1,7,1,20),_OraDbConfigOpenLinks_Type())
oraDbConfigOpenLinks.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigOpenLinks.setStatus(_A)
_OraDbConfigOptimizerMode_Type=DisplayString
_OraDbConfigOptimizerMode_Object=MibTableColumn
oraDbConfigOptimizerMode=_OraDbConfigOptimizerMode_Object((1,3,6,1,4,1,111,4,1,7,1,21),_OraDbConfigOptimizerMode_Type())
oraDbConfigOptimizerMode.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigOptimizerMode.setStatus(_A)
_OraDbConfigProcesses_Type=Integer32
_OraDbConfigProcesses_Object=MibTableColumn
oraDbConfigProcesses=_OraDbConfigProcesses_Object((1,3,6,1,4,1,111,4,1,7,1,22),_OraDbConfigProcesses_Type())
oraDbConfigProcesses.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigProcesses.setStatus(_A)
_OraDbConfigSerializable_Type=TruthValue
_OraDbConfigSerializable_Object=MibTableColumn
oraDbConfigSerializable=_OraDbConfigSerializable_Object((1,3,6,1,4,1,111,4,1,7,1,23),_OraDbConfigSerializable_Type())
oraDbConfigSerializable.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigSerializable.setStatus(_A)
_OraDbConfigSessions_Type=Integer32
_OraDbConfigSessions_Object=MibTableColumn
oraDbConfigSessions=_OraDbConfigSessions_Object((1,3,6,1,4,1,111,4,1,7,1,24),_OraDbConfigSessions_Type())
oraDbConfigSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigSessions.setStatus(_A)
_OraDbConfigSharedPool_Type=Integer32
_OraDbConfigSharedPool_Object=MibTableColumn
oraDbConfigSharedPool=_OraDbConfigSharedPool_Object((1,3,6,1,4,1,111,4,1,7,1,25),_OraDbConfigSharedPool_Type())
oraDbConfigSharedPool.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigSharedPool.setStatus(_A)
_OraDbConfigSortAreaSize_Type=Integer32
_OraDbConfigSortAreaSize_Object=MibTableColumn
oraDbConfigSortAreaSize=_OraDbConfigSortAreaSize_Object((1,3,6,1,4,1,111,4,1,7,1,26),_OraDbConfigSortAreaSize_Type())
oraDbConfigSortAreaSize.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigSortAreaSize.setStatus(_A)
_OraDbConfigSortAreaRetainedSize_Type=Integer32
_OraDbConfigSortAreaRetainedSize_Object=MibTableColumn
oraDbConfigSortAreaRetainedSize=_OraDbConfigSortAreaRetainedSize_Object((1,3,6,1,4,1,111,4,1,7,1,27),_OraDbConfigSortAreaRetainedSize_Type())
oraDbConfigSortAreaRetainedSize.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigSortAreaRetainedSize.setStatus(_A)
_OraDbConfigTransactions_Type=Integer32
_OraDbConfigTransactions_Object=MibTableColumn
oraDbConfigTransactions=_OraDbConfigTransactions_Object((1,3,6,1,4,1,111,4,1,7,1,28),_OraDbConfigTransactions_Type())
oraDbConfigTransactions.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigTransactions.setStatus(_A)
_OraDbConfigTransactionsPerRollback_Type=Integer32
_OraDbConfigTransactionsPerRollback_Object=MibTableColumn
oraDbConfigTransactionsPerRollback=_OraDbConfigTransactionsPerRollback_Object((1,3,6,1,4,1,111,4,1,7,1,29),_OraDbConfigTransactionsPerRollback_Type())
oraDbConfigTransactionsPerRollback.setMaxAccess(_B)
if mibBuilder.loadTexts:oraDbConfigTransactionsPerRollback.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'DateAndTime':DateAndTime,'TruthValue':TruthValue,'oracle':oracle,'oraDbMIB':oraDbMIB,'oraDbObjects':oraDbObjects,'oraDbSysTable':oraDbSysTable,'oraDbSysEntry':oraDbSysEntry,'oraDbSysConsistentChanges':oraDbSysConsistentChanges,'oraDbSysConsistentGets':oraDbSysConsistentGets,'oraDbSysDbBlockChanges':oraDbSysDbBlockChanges,'oraDbSysDbBlockGets':oraDbSysDbBlockGets,'oraDbSysFreeBufferInspected':oraDbSysFreeBufferInspected,'oraDbSysFreeBufferRequested':oraDbSysFreeBufferRequested,'oraDbSysParseCount':oraDbSysParseCount,'oraDbSysPhysReads':oraDbSysPhysReads,'oraDbSysPhysWrites':oraDbSysPhysWrites,'oraDbSysRedoEntries':oraDbSysRedoEntries,'oraDbSysRedoLogSpaceRequests':oraDbSysRedoLogSpaceRequests,'oraDbSysRedoSyncWrites':oraDbSysRedoSyncWrites,'oraDbSysSortsDisk':oraDbSysSortsDisk,'oraDbSysSortsMemory':oraDbSysSortsMemory,'oraDbSysSortsRows':oraDbSysSortsRows,'oraDbSysTableFetchRowid':oraDbSysTableFetchRowid,'oraDbSysTableFetchContinuedRow':oraDbSysTableFetchContinuedRow,'oraDbSysTableScanBlocks':oraDbSysTableScanBlocks,'oraDbSysTableScanRows':oraDbSysTableScanRows,'oraDbSysTableScansLong':oraDbSysTableScansLong,'oraDbSysTableScansShort':oraDbSysTableScansShort,'oraDbSysUserCalls':oraDbSysUserCalls,'oraDbSysUserCommits':oraDbSysUserCommits,'oraDbSysUserRollbacks':oraDbSysUserRollbacks,'oraDbSysWriteRequests':oraDbSysWriteRequests,'oraDbTablespaceTable':oraDbTablespaceTable,'oraDbTablespaceEntry':oraDbTablespaceEntry,_G:oraDbTablespaceIndex,'oraDbTablespaceName':oraDbTablespaceName,'oraDbTablespaceSizeAllocated':oraDbTablespaceSizeAllocated,'oraDbTablespaceSizeUsed':oraDbTablespaceSizeUsed,'oraDbTablespaceState':oraDbTablespaceState,'oraDbTablespaceLargestAvailableChunk':oraDbTablespaceLargestAvailableChunk,'oraDbDataFileTable':oraDbDataFileTable,'oraDbDataFileEntry':oraDbDataFileEntry,_H:oraDbDataFileIndex,'oraDbDataFileName':oraDbDataFileName,'oraDbDataFileSizeAllocated':oraDbDataFileSizeAllocated,'oraDbDataFileDiskReads':oraDbDataFileDiskReads,'oraDbDataFileDiskWrites':oraDbDataFileDiskWrites,'oraDbDataFileDiskReadBlocks':oraDbDataFileDiskReadBlocks,'oraDbDataFileDiskWrittenBlocks':oraDbDataFileDiskWrittenBlocks,'oraDbDataFileDiskReadTimeTicks':oraDbDataFileDiskReadTimeTicks,'oraDbDataFileDiskWriteTimeTicks':oraDbDataFileDiskWriteTimeTicks,'oraDbLibraryCacheTable':oraDbLibraryCacheTable,'oraDbLibraryCacheEntry':oraDbLibraryCacheEntry,_I:oraDbLibraryCacheIndex,'oraDbLibraryCacheNameSpace':oraDbLibraryCacheNameSpace,'oraDbLibraryCacheGets':oraDbLibraryCacheGets,'oraDbLibraryCacheGetHits':oraDbLibraryCacheGetHits,'oraDbLibraryCachePins':oraDbLibraryCachePins,'oraDbLibraryCachePinHits':oraDbLibraryCachePinHits,'oraDbLibraryCacheReloads':oraDbLibraryCacheReloads,'oraDbLibraryCacheInvalidations':oraDbLibraryCacheInvalidations,'oraDbLibraryCacheSumTable':oraDbLibraryCacheSumTable,'oraDbLibraryCacheSumEntry':oraDbLibraryCacheSumEntry,'oraDbLibraryCacheSumGets':oraDbLibraryCacheSumGets,'oraDbLibraryCacheSumGetHits':oraDbLibraryCacheSumGetHits,'oraDbLibraryCacheSumPins':oraDbLibraryCacheSumPins,'oraDbLibraryCacheSumPinHits':oraDbLibraryCacheSumPinHits,'oraDbLibraryCacheSumReloads':oraDbLibraryCacheSumReloads,'oraDbLibraryCacheSumInvalidations':oraDbLibraryCacheSumInvalidations,'oraDbSGATable':oraDbSGATable,'oraDbSGAEntry':oraDbSGAEntry,'oraDbSGAFixedSize':oraDbSGAFixedSize,'oraDbSGAVariableSize':oraDbSGAVariableSize,'oraDbSGADatabaseBuffers':oraDbSGADatabaseBuffers,'oraDbSGARedoBuffers':oraDbSGARedoBuffers,'oraDbConfigTable':oraDbConfigTable,'oraDbConfigEntry':oraDbConfigEntry,'oraDbConfigDbBlockBuffers':oraDbConfigDbBlockBuffers,'oraDbConfigDbBlockCkptBatch':oraDbConfigDbBlockCkptBatch,'oraDbConfigDbBlockSize':oraDbConfigDbBlockSize,'oraDbConfigDbFileSimWrites':oraDbConfigDbFileSimWrites,'oraDbConfigDbMultiBlockReadCount':oraDbConfigDbMultiBlockReadCount,'oraDbConfigDistLockTimeout':oraDbConfigDistLockTimeout,'oraDbConfigDistRecoveryConnectHold':oraDbConfigDistRecoveryConnectHold,'oraDbConfigDistTransactions':oraDbConfigDistTransactions,'oraDbConfigLogArchiveBufferSize':oraDbConfigLogArchiveBufferSize,'oraDbConfigLogArchiveBuffers':oraDbConfigLogArchiveBuffers,'oraDbConfigLogBuffer':oraDbConfigLogBuffer,'oraDbConfigLogCheckpointInterval':oraDbConfigLogCheckpointInterval,'oraDbConfigLogCheckpointTimeout':oraDbConfigLogCheckpointTimeout,'oraDbConfigLogFiles':oraDbConfigLogFiles,'oraDbConfigMaxRollbackSegments':oraDbConfigMaxRollbackSegments,'oraDbConfigMTSMaxDispatchers':oraDbConfigMTSMaxDispatchers,'oraDbConfigMTSMaxServers':oraDbConfigMTSMaxServers,'oraDbConfigMTSServers':oraDbConfigMTSServers,'oraDbConfigOpenCursors':oraDbConfigOpenCursors,'oraDbConfigOpenLinks':oraDbConfigOpenLinks,'oraDbConfigOptimizerMode':oraDbConfigOptimizerMode,'oraDbConfigProcesses':oraDbConfigProcesses,'oraDbConfigSerializable':oraDbConfigSerializable,'oraDbConfigSessions':oraDbConfigSessions,'oraDbConfigSharedPool':oraDbConfigSharedPool,'oraDbConfigSortAreaSize':oraDbConfigSortAreaSize,'oraDbConfigSortAreaRetainedSize':oraDbConfigSortAreaRetainedSize,'oraDbConfigTransactions':oraDbConfigTransactions,'oraDbConfigTransactionsPerRollback':oraDbConfigTransactionsPerRollback})