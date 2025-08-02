_J='memoryPoolIndex'
_I='memoryIndex'
_H='Integer32'
_G='memoryPoolLowThreshold'
_F='memoryPoolHighThreshold'
_E='memoryPoolCurrUsage'
_D='read-write'
_C='WRI-MEMORY-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
wri,wriProducts=mibBuilder.importSymbols('WRI-SMI','wri','wriProducts')
msppMemory=ModuleIdentity((1,3,6,1,4,1,3807,1,8012,1,5))
if mibBuilder.loadTexts:msppMemory.setRevisions(('2010-01-11 00:00','2009-01-11 00:00'))
_Mspp_ObjectIdentity=ObjectIdentity
mspp=_Mspp_ObjectIdentity((1,3,6,1,4,1,3807,1,8012))
_MsppChassis_ObjectIdentity=ObjectIdentity
msppChassis=_MsppChassis_ObjectIdentity((1,3,6,1,4,1,3807,1,8012,1))
_MemoryTable_Object=MibTable
memoryTable=_MemoryTable_Object((1,3,6,1,4,1,3807,1,8012,1,5,1))
if mibBuilder.loadTexts:memoryTable.setStatus(_A)
_MemoryEntry_Object=MibTableRow
memoryEntry=_MemoryEntry_Object((1,3,6,1,4,1,3807,1,8012,1,5,1,1))
memoryEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:memoryEntry.setStatus(_A)
_MemoryIndex_Type=Integer32
_MemoryIndex_Object=MibTableColumn
memoryIndex=_MemoryIndex_Object((1,3,6,1,4,1,3807,1,8012,1,5,1,1,1),_MemoryIndex_Type())
memoryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryIndex.setStatus(_A)
_MemorySdramSize_Type=Counter32
_MemorySdramSize_Object=MibTableColumn
memorySdramSize=_MemorySdramSize_Object((1,3,6,1,4,1,3807,1,8012,1,5,1,1,2),_MemorySdramSize_Type())
memorySdramSize.setMaxAccess(_B)
if mibBuilder.loadTexts:memorySdramSize.setStatus(_A)
_MemorySdramUsed_Type=Counter32
_MemorySdramUsed_Object=MibTableColumn
memorySdramUsed=_MemorySdramUsed_Object((1,3,6,1,4,1,3807,1,8012,1,5,1,1,3),_MemorySdramUsed_Type())
memorySdramUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:memorySdramUsed.setStatus(_A)
_MemoryFlashSize_Type=Counter32
_MemoryFlashSize_Object=MibTableColumn
memoryFlashSize=_MemoryFlashSize_Object((1,3,6,1,4,1,3807,1,8012,1,5,1,1,4),_MemoryFlashSize_Type())
memoryFlashSize.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryFlashSize.setStatus(_A)
_MemoryFlashUsed_Type=Counter32
_MemoryFlashUsed_Object=MibTableColumn
memoryFlashUsed=_MemoryFlashUsed_Object((1,3,6,1,4,1,3807,1,8012,1,5,1,1,5),_MemoryFlashUsed_Type())
memoryFlashUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryFlashUsed.setStatus(_A)
_MemorySdramHThreshold_Type=Counter32
_MemorySdramHThreshold_Object=MibTableColumn
memorySdramHThreshold=_MemorySdramHThreshold_Object((1,3,6,1,4,1,3807,1,8012,1,5,1,1,6),_MemorySdramHThreshold_Type())
memorySdramHThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:memorySdramHThreshold.setStatus(_A)
_MemoryGeneral_ObjectIdentity=ObjectIdentity
memoryGeneral=_MemoryGeneral_ObjectIdentity((1,3,6,1,4,1,3807,1,8012,1,5,2))
_MemoryTrapEnable_Type=Integer32
_MemoryTrapEnable_Object=MibScalar
memoryTrapEnable=_MemoryTrapEnable_Object((1,3,6,1,4,1,3807,1,8012,1,5,2,1),_MemoryTrapEnable_Type())
memoryTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:memoryTrapEnable.setStatus(_A)
_MemoryMonitorEnable_Type=Integer32
_MemoryMonitorEnable_Object=MibScalar
memoryMonitorEnable=_MemoryMonitorEnable_Object((1,3,6,1,4,1,3807,1,8012,1,5,2,2),_MemoryMonitorEnable_Type())
memoryMonitorEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:memoryMonitorEnable.setStatus(_A)
_MemoryTrap_ObjectIdentity=ObjectIdentity
memoryTrap=_MemoryTrap_ObjectIdentity((1,3,6,1,4,1,3807,1,8012,1,5,3))
_MemoryPoolTable_Object=MibTable
memoryPoolTable=_MemoryPoolTable_Object((1,3,6,1,4,1,3807,1,8012,1,5,4))
if mibBuilder.loadTexts:memoryPoolTable.setStatus(_A)
_MemoryPoolEntry_Object=MibTableRow
memoryPoolEntry=_MemoryPoolEntry_Object((1,3,6,1,4,1,3807,1,8012,1,5,4,1))
memoryPoolEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:memoryPoolEntry.setStatus(_A)
_MemoryPoolIndex_Type=Unsigned32
_MemoryPoolIndex_Object=MibTableColumn
memoryPoolIndex=_MemoryPoolIndex_Object((1,3,6,1,4,1,3807,1,8012,1,5,4,1,1),_MemoryPoolIndex_Type())
memoryPoolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryPoolIndex.setStatus(_A)
_MemoryPoolDescr_Type=OctetString
_MemoryPoolDescr_Object=MibTableColumn
memoryPoolDescr=_MemoryPoolDescr_Object((1,3,6,1,4,1,3807,1,8012,1,5,4,1,2),_MemoryPoolDescr_Type())
memoryPoolDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryPoolDescr.setStatus(_A)
_MemoryPoolFreeBytesNum_Type=Counter32
_MemoryPoolFreeBytesNum_Object=MibTableColumn
memoryPoolFreeBytesNum=_MemoryPoolFreeBytesNum_Object((1,3,6,1,4,1,3807,1,8012,1,5,4,1,3),_MemoryPoolFreeBytesNum_Type())
memoryPoolFreeBytesNum.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryPoolFreeBytesNum.setStatus(_A)
_MemoryPoolFreeBlocksNum_Type=Counter32
_MemoryPoolFreeBlocksNum_Object=MibTableColumn
memoryPoolFreeBlocksNum=_MemoryPoolFreeBlocksNum_Object((1,3,6,1,4,1,3807,1,8012,1,5,4,1,4),_MemoryPoolFreeBlocksNum_Type())
memoryPoolFreeBlocksNum.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryPoolFreeBlocksNum.setStatus(_A)
_MemoryPoolFreeMaxBlockSize_Type=Counter32
_MemoryPoolFreeMaxBlockSize_Object=MibTableColumn
memoryPoolFreeMaxBlockSize=_MemoryPoolFreeMaxBlockSize_Object((1,3,6,1,4,1,3807,1,8012,1,5,4,1,5),_MemoryPoolFreeMaxBlockSize_Type())
memoryPoolFreeMaxBlockSize.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryPoolFreeMaxBlockSize.setStatus(_A)
_MemoryPoolMinBlockWords_Type=Counter32
_MemoryPoolMinBlockWords_Object=MibTableColumn
memoryPoolMinBlockWords=_MemoryPoolMinBlockWords_Object((1,3,6,1,4,1,3807,1,8012,1,5,4,1,6),_MemoryPoolMinBlockWords_Type())
memoryPoolMinBlockWords.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryPoolMinBlockWords.setStatus(_A)
_MemoryPoolAllocBytesNum_Type=Counter32
_MemoryPoolAllocBytesNum_Object=MibTableColumn
memoryPoolAllocBytesNum=_MemoryPoolAllocBytesNum_Object((1,3,6,1,4,1,3807,1,8012,1,5,4,1,7),_MemoryPoolAllocBytesNum_Type())
memoryPoolAllocBytesNum.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryPoolAllocBytesNum.setStatus(_A)
_MemoryPoolAllocBlocksNum_Type=Counter32
_MemoryPoolAllocBlocksNum_Object=MibTableColumn
memoryPoolAllocBlocksNum=_MemoryPoolAllocBlocksNum_Object((1,3,6,1,4,1,3807,1,8012,1,5,4,1,8),_MemoryPoolAllocBlocksNum_Type())
memoryPoolAllocBlocksNum.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryPoolAllocBlocksNum.setStatus(_A)
_MemoryPoolAllocBytesCumulate_Type=Counter32
_MemoryPoolAllocBytesCumulate_Object=MibTableColumn
memoryPoolAllocBytesCumulate=_MemoryPoolAllocBytesCumulate_Object((1,3,6,1,4,1,3807,1,8012,1,5,4,1,9),_MemoryPoolAllocBytesCumulate_Type())
memoryPoolAllocBytesCumulate.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryPoolAllocBytesCumulate.setStatus(_A)
_MemoryPoolAllocBlocksCumulate_Type=Counter32
_MemoryPoolAllocBlocksCumulate_Object=MibTableColumn
memoryPoolAllocBlocksCumulate=_MemoryPoolAllocBlocksCumulate_Object((1,3,6,1,4,1,3807,1,8012,1,5,4,1,10),_MemoryPoolAllocBlocksCumulate_Type())
memoryPoolAllocBlocksCumulate.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryPoolAllocBlocksCumulate.setStatus(_A)
_MemoryPoolTotalBytes_Type=Counter32
_MemoryPoolTotalBytes_Object=MibTableColumn
memoryPoolTotalBytes=_MemoryPoolTotalBytes_Object((1,3,6,1,4,1,3807,1,8012,1,5,4,1,11),_MemoryPoolTotalBytes_Type())
memoryPoolTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryPoolTotalBytes.setStatus(_A)
_MemoryPoolHighThreshold_Type=Integer32
_MemoryPoolHighThreshold_Object=MibTableColumn
memoryPoolHighThreshold=_MemoryPoolHighThreshold_Object((1,3,6,1,4,1,3807,1,8012,1,5,4,1,12),_MemoryPoolHighThreshold_Type())
memoryPoolHighThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:memoryPoolHighThreshold.setStatus(_A)
class _MemoryPoolTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_MemoryPoolTrapEnable_Type.__name__=_H
_MemoryPoolTrapEnable_Object=MibTableColumn
memoryPoolTrapEnable=_MemoryPoolTrapEnable_Object((1,3,6,1,4,1,3807,1,8012,1,5,4,1,13),_MemoryPoolTrapEnable_Type())
memoryPoolTrapEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:memoryPoolTrapEnable.setStatus(_A)
class _MemoryPoolStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normal',0),('highoverflow',1)))
_MemoryPoolStatus_Type.__name__=_H
_MemoryPoolStatus_Object=MibTableColumn
memoryPoolStatus=_MemoryPoolStatus_Object((1,3,6,1,4,1,3807,1,8012,1,5,4,1,14),_MemoryPoolStatus_Type())
memoryPoolStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryPoolStatus.setStatus(_A)
_MemoryPoolAllSetting_Type=OctetString
_MemoryPoolAllSetting_Object=MibTableColumn
memoryPoolAllSetting=_MemoryPoolAllSetting_Object((1,3,6,1,4,1,3807,1,8012,1,5,4,1,15),_MemoryPoolAllSetting_Type())
memoryPoolAllSetting.setMaxAccess(_D)
if mibBuilder.loadTexts:memoryPoolAllSetting.setStatus(_A)
_MemoryPoolAllocMaxBytesNum_Type=Integer32
_MemoryPoolAllocMaxBytesNum_Object=MibTableColumn
memoryPoolAllocMaxBytesNum=_MemoryPoolAllocMaxBytesNum_Object((1,3,6,1,4,1,3807,1,8012,1,5,4,1,16),_MemoryPoolAllocMaxBytesNum_Type())
memoryPoolAllocMaxBytesNum.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryPoolAllocMaxBytesNum.setStatus(_A)
_MemoryPoolLowThreshold_Type=Integer32
_MemoryPoolLowThreshold_Object=MibTableColumn
memoryPoolLowThreshold=_MemoryPoolLowThreshold_Object((1,3,6,1,4,1,3807,1,8012,1,5,4,1,17),_MemoryPoolLowThreshold_Type())
memoryPoolLowThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:memoryPoolLowThreshold.setStatus(_A)
_MemoryPoolCurrUsage_Type=Counter32
_MemoryPoolCurrUsage_Object=MibTableColumn
memoryPoolCurrUsage=_MemoryPoolCurrUsage_Object((1,3,6,1,4,1,3807,1,8012,1,5,4,1,18),_MemoryPoolCurrUsage_Type())
memoryPoolCurrUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryPoolCurrUsage.setStatus(_A)
_MemoryPoolIndexDescr_Type=OctetString
_MemoryPoolIndexDescr_Object=MibTableColumn
memoryPoolIndexDescr=_MemoryPoolIndexDescr_Object((1,3,6,1,4,1,3807,1,8012,1,5,4,1,19),_MemoryPoolIndexDescr_Type())
memoryPoolIndexDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryPoolIndexDescr.setStatus(_A)
memoryOverThreshold=NotificationType((1,3,6,1,4,1,3807,1,8012,1,5,3,1))
memoryOverThreshold.setObjects(*((_C,_E),(_C,_F),(_C,_G)))
if mibBuilder.loadTexts:memoryOverThreshold.setStatus(_A)
memoryUnderThreshold=NotificationType((1,3,6,1,4,1,3807,1,8012,1,5,3,2))
memoryUnderThreshold.setObjects(*((_C,_E),(_C,_F),(_C,_G)))
if mibBuilder.loadTexts:memoryUnderThreshold.setStatus(_A)
memoryRecoverThreshold=NotificationType((1,3,6,1,4,1,3807,1,8012,1,5,3,3))
memoryRecoverThreshold.setObjects(*((_C,_E),(_C,_F),(_C,_G)))
if mibBuilder.loadTexts:memoryRecoverThreshold.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'mspp':mspp,'msppChassis':msppChassis,'msppMemory':msppMemory,'memoryTable':memoryTable,'memoryEntry':memoryEntry,_I:memoryIndex,'memorySdramSize':memorySdramSize,'memorySdramUsed':memorySdramUsed,'memoryFlashSize':memoryFlashSize,'memoryFlashUsed':memoryFlashUsed,'memorySdramHThreshold':memorySdramHThreshold,'memoryGeneral':memoryGeneral,'memoryTrapEnable':memoryTrapEnable,'memoryMonitorEnable':memoryMonitorEnable,'memoryTrap':memoryTrap,'memoryOverThreshold':memoryOverThreshold,'memoryUnderThreshold':memoryUnderThreshold,'memoryRecoverThreshold':memoryRecoverThreshold,'memoryPoolTable':memoryPoolTable,'memoryPoolEntry':memoryPoolEntry,_J:memoryPoolIndex,'memoryPoolDescr':memoryPoolDescr,'memoryPoolFreeBytesNum':memoryPoolFreeBytesNum,'memoryPoolFreeBlocksNum':memoryPoolFreeBlocksNum,'memoryPoolFreeMaxBlockSize':memoryPoolFreeMaxBlockSize,'memoryPoolMinBlockWords':memoryPoolMinBlockWords,'memoryPoolAllocBytesNum':memoryPoolAllocBytesNum,'memoryPoolAllocBlocksNum':memoryPoolAllocBlocksNum,'memoryPoolAllocBytesCumulate':memoryPoolAllocBytesCumulate,'memoryPoolAllocBlocksCumulate':memoryPoolAllocBlocksCumulate,'memoryPoolTotalBytes':memoryPoolTotalBytes,_F:memoryPoolHighThreshold,'memoryPoolTrapEnable':memoryPoolTrapEnable,'memoryPoolStatus':memoryPoolStatus,'memoryPoolAllSetting':memoryPoolAllSetting,'memoryPoolAllocMaxBytesNum':memoryPoolAllocMaxBytesNum,_G:memoryPoolLowThreshold,_E:memoryPoolCurrUsage,'memoryPoolIndexDescr':memoryPoolIndexDescr})