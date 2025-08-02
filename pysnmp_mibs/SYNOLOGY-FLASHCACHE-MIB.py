_T='flashCacheGroup'
_S='flashCacheSsdUuid'
_R='flashCacheWriteMissSsd'
_Q='flashCacheWriteSeqSkip'
_P='flashCacheReadSeqSkip'
_O='flashCacheWriteHitRate'
_N='flashCacheReadHitRate'
_M='flashCacheTotalWrite'
_L='flashCacheTotalRead'
_K='flashCacheDiskWrite'
_J='flashCacheDiskRead'
_I='flashCacheWriteHits'
_H='flashCacheReadHits'
_G='flashCacheSpaceDev'
_F='flashCacheSSDDev'
_E='flashCacheIndex'
_D='Integer32'
_C='read-only'
_B='SYNOLOGY-FLASHCACHE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
flashCache=ModuleIdentity((1,3,6,1,4,1,6574,103))
if mibBuilder.loadTexts:flashCache.setRevisions(('2014-07-17 00:00',))
_Synology_ObjectIdentity=ObjectIdentity
synology=_Synology_ObjectIdentity((1,3,6,1,4,1,6574))
_FlashCacheTable_Object=MibTable
flashCacheTable=_FlashCacheTable_Object((1,3,6,1,4,1,6574,103,1))
if mibBuilder.loadTexts:flashCacheTable.setStatus(_A)
_FlashCacheEntry_Object=MibTableRow
flashCacheEntry=_FlashCacheEntry_Object((1,3,6,1,4,1,6574,103,1,1))
flashCacheEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:flashCacheEntry.setStatus(_A)
class _FlashCacheIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FlashCacheIndex_Type.__name__=_D
_FlashCacheIndex_Object=MibTableColumn
flashCacheIndex=_FlashCacheIndex_Object((1,3,6,1,4,1,6574,103,1,1,1),_FlashCacheIndex_Type())
flashCacheIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:flashCacheIndex.setStatus(_A)
_FlashCacheSSDDev_Type=DisplayString
_FlashCacheSSDDev_Object=MibTableColumn
flashCacheSSDDev=_FlashCacheSSDDev_Object((1,3,6,1,4,1,6574,103,1,1,2),_FlashCacheSSDDev_Type())
flashCacheSSDDev.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCacheSSDDev.setStatus(_A)
_FlashCacheSpaceDev_Type=DisplayString
_FlashCacheSpaceDev_Object=MibTableColumn
flashCacheSpaceDev=_FlashCacheSpaceDev_Object((1,3,6,1,4,1,6574,103,1,1,3),_FlashCacheSpaceDev_Type())
flashCacheSpaceDev.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCacheSpaceDev.setStatus(_A)
_FlashCacheReadHits_Type=Counter64
_FlashCacheReadHits_Object=MibTableColumn
flashCacheReadHits=_FlashCacheReadHits_Object((1,3,6,1,4,1,6574,103,1,1,4),_FlashCacheReadHits_Type())
flashCacheReadHits.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCacheReadHits.setStatus(_A)
_FlashCacheWriteHits_Type=Counter64
_FlashCacheWriteHits_Object=MibTableColumn
flashCacheWriteHits=_FlashCacheWriteHits_Object((1,3,6,1,4,1,6574,103,1,1,5),_FlashCacheWriteHits_Type())
flashCacheWriteHits.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCacheWriteHits.setStatus(_A)
_FlashCacheDiskRead_Type=Counter64
_FlashCacheDiskRead_Object=MibTableColumn
flashCacheDiskRead=_FlashCacheDiskRead_Object((1,3,6,1,4,1,6574,103,1,1,6),_FlashCacheDiskRead_Type())
flashCacheDiskRead.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCacheDiskRead.setStatus(_A)
_FlashCacheDiskWrite_Type=Counter64
_FlashCacheDiskWrite_Object=MibTableColumn
flashCacheDiskWrite=_FlashCacheDiskWrite_Object((1,3,6,1,4,1,6574,103,1,1,7),_FlashCacheDiskWrite_Type())
flashCacheDiskWrite.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCacheDiskWrite.setStatus(_A)
_FlashCacheTotalRead_Type=Counter64
_FlashCacheTotalRead_Object=MibTableColumn
flashCacheTotalRead=_FlashCacheTotalRead_Object((1,3,6,1,4,1,6574,103,1,1,8),_FlashCacheTotalRead_Type())
flashCacheTotalRead.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCacheTotalRead.setStatus(_A)
_FlashCacheTotalWrite_Type=Counter64
_FlashCacheTotalWrite_Object=MibTableColumn
flashCacheTotalWrite=_FlashCacheTotalWrite_Object((1,3,6,1,4,1,6574,103,1,1,9),_FlashCacheTotalWrite_Type())
flashCacheTotalWrite.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCacheTotalWrite.setStatus(_A)
class _FlashCacheReadHitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FlashCacheReadHitRate_Type.__name__=_D
_FlashCacheReadHitRate_Object=MibTableColumn
flashCacheReadHitRate=_FlashCacheReadHitRate_Object((1,3,6,1,4,1,6574,103,1,1,10),_FlashCacheReadHitRate_Type())
flashCacheReadHitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCacheReadHitRate.setStatus(_A)
class _FlashCacheWriteHitRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FlashCacheWriteHitRate_Type.__name__=_D
_FlashCacheWriteHitRate_Object=MibTableColumn
flashCacheWriteHitRate=_FlashCacheWriteHitRate_Object((1,3,6,1,4,1,6574,103,1,1,11),_FlashCacheWriteHitRate_Type())
flashCacheWriteHitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCacheWriteHitRate.setStatus(_A)
_FlashCacheReadSeqSkip_Type=Counter64
_FlashCacheReadSeqSkip_Object=MibTableColumn
flashCacheReadSeqSkip=_FlashCacheReadSeqSkip_Object((1,3,6,1,4,1,6574,103,1,1,12),_FlashCacheReadSeqSkip_Type())
flashCacheReadSeqSkip.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCacheReadSeqSkip.setStatus(_A)
_FlashCacheWriteSeqSkip_Type=Counter64
_FlashCacheWriteSeqSkip_Object=MibTableColumn
flashCacheWriteSeqSkip=_FlashCacheWriteSeqSkip_Object((1,3,6,1,4,1,6574,103,1,1,13),_FlashCacheWriteSeqSkip_Type())
flashCacheWriteSeqSkip.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCacheWriteSeqSkip.setStatus(_A)
_FlashCacheWriteMissSsd_Type=Counter64
_FlashCacheWriteMissSsd_Object=MibTableColumn
flashCacheWriteMissSsd=_FlashCacheWriteMissSsd_Object((1,3,6,1,4,1,6574,103,1,1,14),_FlashCacheWriteMissSsd_Type())
flashCacheWriteMissSsd.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCacheWriteMissSsd.setStatus(_A)
_FlashCacheSsdUuid_Type=DisplayString
_FlashCacheSsdUuid_Object=MibTableColumn
flashCacheSsdUuid=_FlashCacheSsdUuid_Object((1,3,6,1,4,1,6574,103,1,1,15),_FlashCacheSsdUuid_Type())
flashCacheSsdUuid.setMaxAccess(_C)
if mibBuilder.loadTexts:flashCacheSsdUuid.setStatus(_A)
_FlashCacheConformance_ObjectIdentity=ObjectIdentity
flashCacheConformance=_FlashCacheConformance_ObjectIdentity((1,3,6,1,4,1,6574,103,2))
_FlashCacheCompliances_ObjectIdentity=ObjectIdentity
flashCacheCompliances=_FlashCacheCompliances_ObjectIdentity((1,3,6,1,4,1,6574,103,2,1))
_FlashCacheGroups_ObjectIdentity=ObjectIdentity
flashCacheGroups=_FlashCacheGroups_ObjectIdentity((1,3,6,1,4,1,6574,103,2,2))
flashCacheGroup=ObjectGroup((1,3,6,1,4,1,6574,103,2,2,1))
flashCacheGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:flashCacheGroup.setStatus(_A)
flashCacheCompliance=ModuleCompliance((1,3,6,1,4,1,6574,103,2,1,1))
flashCacheCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:flashCacheCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'synology':synology,'flashCache':flashCache,'flashCacheTable':flashCacheTable,'flashCacheEntry':flashCacheEntry,_E:flashCacheIndex,_F:flashCacheSSDDev,_G:flashCacheSpaceDev,_H:flashCacheReadHits,_I:flashCacheWriteHits,_J:flashCacheDiskRead,_K:flashCacheDiskWrite,_L:flashCacheTotalRead,_M:flashCacheTotalWrite,_N:flashCacheReadHitRate,_O:flashCacheWriteHitRate,_P:flashCacheReadSeqSkip,_Q:flashCacheWriteSeqSkip,_R:flashCacheWriteMissSsd,_S:flashCacheSsdUuid,'flashCacheConformance':flashCacheConformance,'flashCacheCompliances':flashCacheCompliances,'flashCacheCompliance':flashCacheCompliance,'flashCacheGroups':flashCacheGroups,_T:flashCacheGroup})