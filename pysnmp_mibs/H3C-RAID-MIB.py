_P='h3c3rdRaidUuid'
_O='not-accessible'
_N='h3cFreezeRaidUuid'
_M='minute'
_L='h3cRaidName'
_K='entPhysicalIndex'
_J='ENTITY-MIB'
_I='h3cRaidUuid'
_H='OctetString'
_G='H3cStorageEnableState'
_F='H3C-RAID-MIB'
_E='read-create'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_J,_K)
H3cRaidIDType,H3cStorageActionType,H3cStorageEnableState,H3cStorageOwnerType,h3cStorageRef=mibBuilder.importSymbols('H3C-STORAGE-REF-MIB','H3cRaidIDType','H3cStorageActionType',_G,'H3cStorageOwnerType','h3cStorageRef')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
h3cRaid=ModuleIdentity((1,3,6,1,4,1,2011,10,10,4))
_H3cRaidMibObjects_ObjectIdentity=ObjectIdentity
h3cRaidMibObjects=_H3cRaidMibObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,10,4,1))
_H3cRaidCapacityTable_ObjectIdentity=ObjectIdentity
h3cRaidCapacityTable=_H3cRaidCapacityTable_ObjectIdentity((1,3,6,1,4,1,2011,10,10,4,1,1))
_H3cPrimaryRaidCount_Type=Integer32
_H3cPrimaryRaidCount_Object=MibScalar
h3cPrimaryRaidCount=_H3cPrimaryRaidCount_Object((1,3,6,1,4,1,2011,10,10,4,1,1,1),_H3cPrimaryRaidCount_Type())
h3cPrimaryRaidCount.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cPrimaryRaidCount.setStatus(_A)
_H3cRaidTable_Object=MibTable
h3cRaidTable=_H3cRaidTable_Object((1,3,6,1,4,1,2011,10,10,4,1,2))
if mibBuilder.loadTexts:h3cRaidTable.setStatus(_A)
_H3cRaidEntry_Object=MibTableRow
h3cRaidEntry=_H3cRaidEntry_Object((1,3,6,1,4,1,2011,10,10,4,1,2,1))
h3cRaidEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:h3cRaidEntry.setStatus(_A)
class _H3cRaidName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_H3cRaidName_Type.__name__=_H
_H3cRaidName_Object=MibTableColumn
h3cRaidName=_H3cRaidName_Object((1,3,6,1,4,1,2011,10,10,4,1,2,1,1),_H3cRaidName_Type())
h3cRaidName.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:h3cRaidName.setStatus(_A)
_H3cRaidId_Type=Integer32
_H3cRaidId_Object=MibTableColumn
h3cRaidId=_H3cRaidId_Object((1,3,6,1,4,1,2011,10,10,4,1,2,1,2),_H3cRaidId_Type())
h3cRaidId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRaidId.setStatus(_A)
_H3cRaidUuid_Type=H3cRaidIDType
_H3cRaidUuid_Object=MibTableColumn
h3cRaidUuid=_H3cRaidUuid_Object((1,3,6,1,4,1,2011,10,10,4,1,2,1,3),_H3cRaidUuid_Type())
h3cRaidUuid.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRaidUuid.setStatus(_A)
class _H3cRaidLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('jbod',1),('raid0',2),('raid1',3),('raid2',4),('raid3',5),('raid4',6),('raid5',7),('raid6',8),('raid10',9),('raid50',10)))
_H3cRaidLevel_Type.__name__=_C
_H3cRaidLevel_Object=MibTableColumn
h3cRaidLevel=_H3cRaidLevel_Object((1,3,6,1,4,1,2011,10,10,4,1,2,1,4),_H3cRaidLevel_Type())
h3cRaidLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRaidLevel.setStatus(_A)
_H3cRaidTimestamp_Type=DateAndTime
_H3cRaidTimestamp_Object=MibTableColumn
h3cRaidTimestamp=_H3cRaidTimestamp_Object((1,3,6,1,4,1,2011,10,10,4,1,2,1,5),_H3cRaidTimestamp_Type())
h3cRaidTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRaidTimestamp.setStatus(_A)
class _H3cRaidDiskList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,256))
_H3cRaidDiskList_Type.__name__=_H
_H3cRaidDiskList_Object=MibTableColumn
h3cRaidDiskList=_H3cRaidDiskList_Object((1,3,6,1,4,1,2011,10,10,4,1,2,1,6),_H3cRaidDiskList_Type())
h3cRaidDiskList.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRaidDiskList.setStatus(_A)
_H3cRaidOwner_Type=H3cStorageOwnerType
_H3cRaidOwner_Object=MibTableColumn
h3cRaidOwner=_H3cRaidOwner_Object((1,3,6,1,4,1,2011,10,10,4,1,2,1,7),_H3cRaidOwner_Type())
h3cRaidOwner.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRaidOwner.setStatus(_A)
_H3cRaidSize_Type=Integer32
_H3cRaidSize_Object=MibTableColumn
h3cRaidSize=_H3cRaidSize_Object((1,3,6,1,4,1,2011,10,10,4,1,2,1,8),_H3cRaidSize_Type())
h3cRaidSize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRaidSize.setStatus(_A)
_H3cRaidFreeSize_Type=Integer32
_H3cRaidFreeSize_Object=MibTableColumn
h3cRaidFreeSize=_H3cRaidFreeSize_Object((1,3,6,1,4,1,2011,10,10,4,1,2,1,9),_H3cRaidFreeSize_Type())
h3cRaidFreeSize.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRaidFreeSize.setStatus(_A)
if mibBuilder.loadTexts:h3cRaidFreeSize.setUnits('MB')
_H3cRaidAutoSync_Type=TruthValue
_H3cRaidAutoSync_Object=MibTableColumn
h3cRaidAutoSync=_H3cRaidAutoSync_Object((1,3,6,1,4,1,2011,10,10,4,1,2,1,10),_H3cRaidAutoSync_Type())
h3cRaidAutoSync.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRaidAutoSync.setStatus(_A)
_H3cRaidRowStatus_Type=RowStatus
_H3cRaidRowStatus_Object=MibTableColumn
h3cRaidRowStatus=_H3cRaidRowStatus_Object((1,3,6,1,4,1,2011,10,10,4,1,2,1,11),_H3cRaidRowStatus_Type())
h3cRaidRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRaidRowStatus.setStatus(_A)
_H3cRaidManageTable_Object=MibTable
h3cRaidManageTable=_H3cRaidManageTable_Object((1,3,6,1,4,1,2011,10,10,4,1,3))
if mibBuilder.loadTexts:h3cRaidManageTable.setStatus(_A)
_H3cRaidManageEntry_Object=MibTableRow
h3cRaidManageEntry=_H3cRaidManageEntry_Object((1,3,6,1,4,1,2011,10,10,4,1,3,1))
h3cRaidManageEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:h3cRaidManageEntry.setStatus(_A)
class _H3cRaidLocationState_Type(H3cStorageEnableState):defaultValue=1
_H3cRaidLocationState_Type.__name__=_G
_H3cRaidLocationState_Object=MibTableColumn
h3cRaidLocationState=_H3cRaidLocationState_Object((1,3,6,1,4,1,2011,10,10,4,1,3,1,1),_H3cRaidLocationState_Type())
h3cRaidLocationState.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRaidLocationState.setStatus(_A)
class _H3cRaidAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('run',1),('pause',2),('rebuild',3),('invalid',4)))
_H3cRaidAction_Type.__name__=_C
_H3cRaidAction_Object=MibTableColumn
h3cRaidAction=_H3cRaidAction_Object((1,3,6,1,4,1,2011,10,10,4,1,3,1,2),_H3cRaidAction_Type())
h3cRaidAction.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRaidAction.setStatus(_A)
class _H3cRaidRunState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('degraded',2),('failed',3)))
_H3cRaidRunState_Type.__name__=_C
_H3cRaidRunState_Object=MibTableColumn
h3cRaidRunState=_H3cRaidRunState_Object((1,3,6,1,4,1,2011,10,10,4,1,3,1,3),_H3cRaidRunState_Type())
h3cRaidRunState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRaidRunState.setStatus(_A)
class _H3cRaidAutoRebuild_Type(H3cStorageEnableState):defaultValue=2
_H3cRaidAutoRebuild_Type.__name__=_G
_H3cRaidAutoRebuild_Object=MibTableColumn
h3cRaidAutoRebuild=_H3cRaidAutoRebuild_Object((1,3,6,1,4,1,2011,10,10,4,1,3,1,4),_H3cRaidAutoRebuild_Type())
h3cRaidAutoRebuild.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRaidAutoRebuild.setStatus(_A)
class _H3cRaidSyncPercentage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cRaidSyncPercentage_Type.__name__=_C
_H3cRaidSyncPercentage_Object=MibTableColumn
h3cRaidSyncPercentage=_H3cRaidSyncPercentage_Object((1,3,6,1,4,1,2011,10,10,4,1,3,1,5),_H3cRaidSyncPercentage_Type())
h3cRaidSyncPercentage.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRaidSyncPercentage.setStatus(_A)
class _H3cRaidHideState_Type(H3cStorageEnableState):defaultValue=2
_H3cRaidHideState_Type.__name__=_G
_H3cRaidHideState_Object=MibTableColumn
h3cRaidHideState=_H3cRaidHideState_Object((1,3,6,1,4,1,2011,10,10,4,1,3,1,6),_H3cRaidHideState_Type())
h3cRaidHideState.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRaidHideState.setStatus(_A)
_H3cRaidLvRestore_Type=H3cStorageActionType
_H3cRaidLvRestore_Object=MibTableColumn
h3cRaidLvRestore=_H3cRaidLvRestore_Object((1,3,6,1,4,1,2011,10,10,4,1,3,1,7),_H3cRaidLvRestore_Type())
h3cRaidLvRestore.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRaidLvRestore.setStatus(_A)
class _H3cRaidType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('virtualDevice',1),('directDevice',2),('serviceEnabledDevice',3),('unassigned',4)))
_H3cRaidType_Type.__name__=_C
_H3cRaidType_Object=MibTableColumn
h3cRaidType=_H3cRaidType_Object((1,3,6,1,4,1,2011,10,10,4,1,3,1,8),_H3cRaidType_Type())
h3cRaidType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRaidType.setStatus(_A)
_H3cRaidCacheTable_Object=MibTable
h3cRaidCacheTable=_H3cRaidCacheTable_Object((1,3,6,1,4,1,2011,10,10,4,1,4))
if mibBuilder.loadTexts:h3cRaidCacheTable.setStatus(_A)
_H3cRaidCacheEntry_Object=MibTableRow
h3cRaidCacheEntry=_H3cRaidCacheEntry_Object((1,3,6,1,4,1,2011,10,10,4,1,4,1))
h3cRaidCacheEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:h3cRaidCacheEntry.setStatus(_A)
class _H3cRaidReadCache_Type(H3cStorageEnableState):defaultValue=1
_H3cRaidReadCache_Type.__name__=_G
_H3cRaidReadCache_Object=MibTableColumn
h3cRaidReadCache=_H3cRaidReadCache_Object((1,3,6,1,4,1,2011,10,10,4,1,4,1,1),_H3cRaidReadCache_Type())
h3cRaidReadCache.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRaidReadCache.setStatus(_A)
class _H3cRaidReadCacheHitPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_H3cRaidReadCacheHitPeriod_Type.__name__=_C
_H3cRaidReadCacheHitPeriod_Object=MibTableColumn
h3cRaidReadCacheHitPeriod=_H3cRaidReadCacheHitPeriod_Object((1,3,6,1,4,1,2011,10,10,4,1,4,1,2),_H3cRaidReadCacheHitPeriod_Type())
h3cRaidReadCacheHitPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRaidReadCacheHitPeriod.setStatus(_A)
if mibBuilder.loadTexts:h3cRaidReadCacheHitPeriod.setUnits(_M)
class _H3cRaidReadCacheAverageRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cRaidReadCacheAverageRate_Type.__name__=_C
_H3cRaidReadCacheAverageRate_Object=MibTableColumn
h3cRaidReadCacheAverageRate=_H3cRaidReadCacheAverageRate_Object((1,3,6,1,4,1,2011,10,10,4,1,4,1,3),_H3cRaidReadCacheAverageRate_Type())
h3cRaidReadCacheAverageRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRaidReadCacheAverageRate.setStatus(_A)
class _H3cRaidReadCachePhaseRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cRaidReadCachePhaseRate_Type.__name__=_C
_H3cRaidReadCachePhaseRate_Object=MibTableColumn
h3cRaidReadCachePhaseRate=_H3cRaidReadCachePhaseRate_Object((1,3,6,1,4,1,2011,10,10,4,1,4,1,4),_H3cRaidReadCachePhaseRate_Type())
h3cRaidReadCachePhaseRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRaidReadCachePhaseRate.setStatus(_A)
class _H3cRaidWriteCache_Type(H3cStorageEnableState):defaultValue=1
_H3cRaidWriteCache_Type.__name__=_G
_H3cRaidWriteCache_Object=MibTableColumn
h3cRaidWriteCache=_H3cRaidWriteCache_Object((1,3,6,1,4,1,2011,10,10,4,1,4,1,5),_H3cRaidWriteCache_Type())
h3cRaidWriteCache.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRaidWriteCache.setStatus(_A)
class _H3cRaidWriteCacheHitPeriod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_H3cRaidWriteCacheHitPeriod_Type.__name__=_C
_H3cRaidWriteCacheHitPeriod_Object=MibTableColumn
h3cRaidWriteCacheHitPeriod=_H3cRaidWriteCacheHitPeriod_Object((1,3,6,1,4,1,2011,10,10,4,1,4,1,6),_H3cRaidWriteCacheHitPeriod_Type())
h3cRaidWriteCacheHitPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRaidWriteCacheHitPeriod.setStatus(_A)
if mibBuilder.loadTexts:h3cRaidWriteCacheHitPeriod.setUnits(_M)
class _H3cRaidWriteCacheAverageRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cRaidWriteCacheAverageRate_Type.__name__=_C
_H3cRaidWriteCacheAverageRate_Object=MibTableColumn
h3cRaidWriteCacheAverageRate=_H3cRaidWriteCacheAverageRate_Object((1,3,6,1,4,1,2011,10,10,4,1,4,1,7),_H3cRaidWriteCacheAverageRate_Type())
h3cRaidWriteCacheAverageRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRaidWriteCacheAverageRate.setStatus(_A)
class _H3cRaidWriteCachePhaseRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cRaidWriteCachePhaseRate_Type.__name__=_C
_H3cRaidWriteCachePhaseRate_Object=MibTableColumn
h3cRaidWriteCachePhaseRate=_H3cRaidWriteCachePhaseRate_Object((1,3,6,1,4,1,2011,10,10,4,1,4,1,8),_H3cRaidWriteCachePhaseRate_Type())
h3cRaidWriteCachePhaseRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cRaidWriteCachePhaseRate.setStatus(_A)
_H3cRaidWriteCacheFlush_Type=H3cStorageActionType
_H3cRaidWriteCacheFlush_Object=MibTableColumn
h3cRaidWriteCacheFlush=_H3cRaidWriteCacheFlush_Object((1,3,6,1,4,1,2011,10,10,4,1,4,1,9),_H3cRaidWriteCacheFlush_Type())
h3cRaidWriteCacheFlush.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cRaidWriteCacheFlush.setStatus(_A)
_H3cRaidSpareDiskTable_Object=MibTable
h3cRaidSpareDiskTable=_H3cRaidSpareDiskTable_Object((1,3,6,1,4,1,2011,10,10,4,1,5))
if mibBuilder.loadTexts:h3cRaidSpareDiskTable.setStatus(_A)
_H3cRaidSpareDiskEntry_Object=MibTableRow
h3cRaidSpareDiskEntry=_H3cRaidSpareDiskEntry_Object((1,3,6,1,4,1,2011,10,10,4,1,5,1))
h3cRaidSpareDiskEntry.setIndexNames((0,_F,_I),(0,_J,_K))
if mibBuilder.loadTexts:h3cRaidSpareDiskEntry.setStatus(_A)
_H3cRaidSpareDiskRowStatus_Type=RowStatus
_H3cRaidSpareDiskRowStatus_Object=MibTableColumn
h3cRaidSpareDiskRowStatus=_H3cRaidSpareDiskRowStatus_Object((1,3,6,1,4,1,2011,10,10,4,1,5,1,1),_H3cRaidSpareDiskRowStatus_Type())
h3cRaidSpareDiskRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cRaidSpareDiskRowStatus.setStatus(_A)
_H3cFreezeRaidTable_Object=MibTable
h3cFreezeRaidTable=_H3cFreezeRaidTable_Object((1,3,6,1,4,1,2011,10,10,4,1,6))
if mibBuilder.loadTexts:h3cFreezeRaidTable.setStatus(_A)
_H3cFreezeRaidEntry_Object=MibTableRow
h3cFreezeRaidEntry=_H3cFreezeRaidEntry_Object((1,3,6,1,4,1,2011,10,10,4,1,6,1))
h3cFreezeRaidEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:h3cFreezeRaidEntry.setStatus(_A)
_H3cFreezeRaidUuid_Type=H3cRaidIDType
_H3cFreezeRaidUuid_Object=MibTableColumn
h3cFreezeRaidUuid=_H3cFreezeRaidUuid_Object((1,3,6,1,4,1,2011,10,10,4,1,6,1,1),_H3cFreezeRaidUuid_Type())
h3cFreezeRaidUuid.setMaxAccess(_O)
if mibBuilder.loadTexts:h3cFreezeRaidUuid.setStatus(_A)
class _H3cFreezeRaidName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_H3cFreezeRaidName_Type.__name__=_H
_H3cFreezeRaidName_Object=MibTableColumn
h3cFreezeRaidName=_H3cFreezeRaidName_Object((1,3,6,1,4,1,2011,10,10,4,1,6,1,2),_H3cFreezeRaidName_Type())
h3cFreezeRaidName.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cFreezeRaidName.setStatus(_A)
_H3cFreezeRaidRowStatus_Type=RowStatus
_H3cFreezeRaidRowStatus_Object=MibTableColumn
h3cFreezeRaidRowStatus=_H3cFreezeRaidRowStatus_Object((1,3,6,1,4,1,2011,10,10,4,1,6,1,3),_H3cFreezeRaidRowStatus_Type())
h3cFreezeRaidRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cFreezeRaidRowStatus.setStatus(_A)
_H3c3rdRaidTable_Object=MibTable
h3c3rdRaidTable=_H3c3rdRaidTable_Object((1,3,6,1,4,1,2011,10,10,4,1,7))
if mibBuilder.loadTexts:h3c3rdRaidTable.setStatus(_A)
_H3c3rdRaidEntry_Object=MibTableRow
h3c3rdRaidEntry=_H3c3rdRaidEntry_Object((1,3,6,1,4,1,2011,10,10,4,1,7,1))
h3c3rdRaidEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:h3c3rdRaidEntry.setStatus(_A)
_H3c3rdRaidUuid_Type=H3cRaidIDType
_H3c3rdRaidUuid_Object=MibTableColumn
h3c3rdRaidUuid=_H3c3rdRaidUuid_Object((1,3,6,1,4,1,2011,10,10,4,1,7,1,1),_H3c3rdRaidUuid_Type())
h3c3rdRaidUuid.setMaxAccess(_O)
if mibBuilder.loadTexts:h3c3rdRaidUuid.setStatus(_A)
class _H3c3rdRaidName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_H3c3rdRaidName_Type.__name__=_H
_H3c3rdRaidName_Object=MibTableColumn
h3c3rdRaidName=_H3c3rdRaidName_Object((1,3,6,1,4,1,2011,10,10,4,1,7,1,2),_H3c3rdRaidName_Type())
h3c3rdRaidName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3c3rdRaidName.setStatus(_A)
_H3c3rdRaidOwner_Type=OctetString
_H3c3rdRaidOwner_Object=MibTableColumn
h3c3rdRaidOwner=_H3c3rdRaidOwner_Object((1,3,6,1,4,1,2011,10,10,4,1,7,1,3),_H3c3rdRaidOwner_Type())
h3c3rdRaidOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:h3c3rdRaidOwner.setStatus(_A)
_H3c3rdRaidImport_Type=H3cStorageOwnerType
_H3c3rdRaidImport_Object=MibTableColumn
h3c3rdRaidImport=_H3c3rdRaidImport_Object((1,3,6,1,4,1,2011,10,10,4,1,7,1,4),_H3c3rdRaidImport_Type())
h3c3rdRaidImport.setMaxAccess(_E)
if mibBuilder.loadTexts:h3c3rdRaidImport.setStatus(_A)
_H3c3rdRaidRowStatus_Type=RowStatus
_H3c3rdRaidRowStatus_Object=MibTableColumn
h3c3rdRaidRowStatus=_H3c3rdRaidRowStatus_Object((1,3,6,1,4,1,2011,10,10,4,1,7,1,5),_H3c3rdRaidRowStatus_Type())
h3c3rdRaidRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:h3c3rdRaidRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'h3cRaid':h3cRaid,'h3cRaidMibObjects':h3cRaidMibObjects,'h3cRaidCapacityTable':h3cRaidCapacityTable,'h3cPrimaryRaidCount':h3cPrimaryRaidCount,'h3cRaidTable':h3cRaidTable,'h3cRaidEntry':h3cRaidEntry,_L:h3cRaidName,'h3cRaidId':h3cRaidId,_I:h3cRaidUuid,'h3cRaidLevel':h3cRaidLevel,'h3cRaidTimestamp':h3cRaidTimestamp,'h3cRaidDiskList':h3cRaidDiskList,'h3cRaidOwner':h3cRaidOwner,'h3cRaidSize':h3cRaidSize,'h3cRaidFreeSize':h3cRaidFreeSize,'h3cRaidAutoSync':h3cRaidAutoSync,'h3cRaidRowStatus':h3cRaidRowStatus,'h3cRaidManageTable':h3cRaidManageTable,'h3cRaidManageEntry':h3cRaidManageEntry,'h3cRaidLocationState':h3cRaidLocationState,'h3cRaidAction':h3cRaidAction,'h3cRaidRunState':h3cRaidRunState,'h3cRaidAutoRebuild':h3cRaidAutoRebuild,'h3cRaidSyncPercentage':h3cRaidSyncPercentage,'h3cRaidHideState':h3cRaidHideState,'h3cRaidLvRestore':h3cRaidLvRestore,'h3cRaidType':h3cRaidType,'h3cRaidCacheTable':h3cRaidCacheTable,'h3cRaidCacheEntry':h3cRaidCacheEntry,'h3cRaidReadCache':h3cRaidReadCache,'h3cRaidReadCacheHitPeriod':h3cRaidReadCacheHitPeriod,'h3cRaidReadCacheAverageRate':h3cRaidReadCacheAverageRate,'h3cRaidReadCachePhaseRate':h3cRaidReadCachePhaseRate,'h3cRaidWriteCache':h3cRaidWriteCache,'h3cRaidWriteCacheHitPeriod':h3cRaidWriteCacheHitPeriod,'h3cRaidWriteCacheAverageRate':h3cRaidWriteCacheAverageRate,'h3cRaidWriteCachePhaseRate':h3cRaidWriteCachePhaseRate,'h3cRaidWriteCacheFlush':h3cRaidWriteCacheFlush,'h3cRaidSpareDiskTable':h3cRaidSpareDiskTable,'h3cRaidSpareDiskEntry':h3cRaidSpareDiskEntry,'h3cRaidSpareDiskRowStatus':h3cRaidSpareDiskRowStatus,'h3cFreezeRaidTable':h3cFreezeRaidTable,'h3cFreezeRaidEntry':h3cFreezeRaidEntry,_N:h3cFreezeRaidUuid,'h3cFreezeRaidName':h3cFreezeRaidName,'h3cFreezeRaidRowStatus':h3cFreezeRaidRowStatus,'h3c3rdRaidTable':h3c3rdRaidTable,'h3c3rdRaidEntry':h3c3rdRaidEntry,_P:h3c3rdRaidUuid,'h3c3rdRaidName':h3c3rdRaidName,'h3c3rdRaidOwner':h3c3rdRaidOwner,'h3c3rdRaidImport':h3c3rdRaidImport,'h3c3rdRaidRowStatus':h3c3rdRaidRowStatus})