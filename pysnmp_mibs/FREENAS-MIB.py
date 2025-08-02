_P='alertMessage'
_O='alertLevel'
_N='interfaceTopHostIndex'
_M='interfaceIndex'
_L='hddTempIndex'
_K='zvolIndex'
_J='datasetIndex'
_I='zpoolIndex'
_H='alertId'
_G='read-write'
_F='Bytes'
_E='not-accessible'
_D='FREENAS-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
freeNas=ModuleIdentity((1,3,6,1,4,1,50536))
if mibBuilder.loadTexts:freeNas.setRevisions(('2020-10-20 00:00',))
class ZPoolHealthType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('online',0),('degraded',1),('faulted',2),('offline',3),('unavail',4),('removed',5)))
class AlertLevelType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('info',1),('notice',2),('warning',3),('error',4),('critical',5),('alert',6),('emergency',7)))
_Zfs_ObjectIdentity=ObjectIdentity
zfs=_Zfs_ObjectIdentity((1,3,6,1,4,1,50536,1))
_Zpool_ObjectIdentity=ObjectIdentity
zpool=_Zpool_ObjectIdentity((1,3,6,1,4,1,50536,1,1))
_ZpoolTable_Object=MibTable
zpoolTable=_ZpoolTable_Object((1,3,6,1,4,1,50536,1,1,1))
if mibBuilder.loadTexts:zpoolTable.setStatus(_A)
_ZpoolEntry_Object=MibTableRow
zpoolEntry=_ZpoolEntry_Object((1,3,6,1,4,1,50536,1,1,1,1))
zpoolEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:zpoolEntry.setStatus(_A)
class _ZpoolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ZpoolIndex_Type.__name__=_C
_ZpoolIndex_Object=MibTableColumn
zpoolIndex=_ZpoolIndex_Object((1,3,6,1,4,1,50536,1,1,1,1,1),_ZpoolIndex_Type())
zpoolIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zpoolIndex.setStatus(_A)
_ZpoolDescr_Type=DisplayString
_ZpoolDescr_Object=MibTableColumn
zpoolDescr=_ZpoolDescr_Object((1,3,6,1,4,1,50536,1,1,1,1,2),_ZpoolDescr_Type())
zpoolDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:zpoolDescr.setStatus(_A)
class _ZpoolAllocationUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ZpoolAllocationUnits_Type.__name__=_C
_ZpoolAllocationUnits_Object=MibTableColumn
zpoolAllocationUnits=_ZpoolAllocationUnits_Object((1,3,6,1,4,1,50536,1,1,1,1,3),_ZpoolAllocationUnits_Type())
zpoolAllocationUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:zpoolAllocationUnits.setStatus(_A)
if mibBuilder.loadTexts:zpoolAllocationUnits.setUnits(_F)
class _ZpoolSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ZpoolSize_Type.__name__=_C
_ZpoolSize_Object=MibTableColumn
zpoolSize=_ZpoolSize_Object((1,3,6,1,4,1,50536,1,1,1,1,4),_ZpoolSize_Type())
zpoolSize.setMaxAccess(_G)
if mibBuilder.loadTexts:zpoolSize.setStatus(_A)
class _ZpoolUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ZpoolUsed_Type.__name__=_C
_ZpoolUsed_Object=MibTableColumn
zpoolUsed=_ZpoolUsed_Object((1,3,6,1,4,1,50536,1,1,1,1,5),_ZpoolUsed_Type())
zpoolUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:zpoolUsed.setStatus(_A)
class _ZpoolAvailable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ZpoolAvailable_Type.__name__=_C
_ZpoolAvailable_Object=MibTableColumn
zpoolAvailable=_ZpoolAvailable_Object((1,3,6,1,4,1,50536,1,1,1,1,6),_ZpoolAvailable_Type())
zpoolAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:zpoolAvailable.setStatus(_A)
_ZpoolHealth_Type=ZPoolHealthType
_ZpoolHealth_Object=MibTableColumn
zpoolHealth=_ZpoolHealth_Object((1,3,6,1,4,1,50536,1,1,1,1,7),_ZpoolHealth_Type())
zpoolHealth.setMaxAccess(_B)
if mibBuilder.loadTexts:zpoolHealth.setStatus(_A)
_ZpoolReadOps_Type=Counter64
_ZpoolReadOps_Object=MibTableColumn
zpoolReadOps=_ZpoolReadOps_Object((1,3,6,1,4,1,50536,1,1,1,1,8),_ZpoolReadOps_Type())
zpoolReadOps.setMaxAccess(_B)
if mibBuilder.loadTexts:zpoolReadOps.setStatus(_A)
_ZpoolWriteOps_Type=Counter64
_ZpoolWriteOps_Object=MibTableColumn
zpoolWriteOps=_ZpoolWriteOps_Object((1,3,6,1,4,1,50536,1,1,1,1,9),_ZpoolWriteOps_Type())
zpoolWriteOps.setMaxAccess(_B)
if mibBuilder.loadTexts:zpoolWriteOps.setStatus(_A)
_ZpoolReadBytes_Type=Counter64
_ZpoolReadBytes_Object=MibTableColumn
zpoolReadBytes=_ZpoolReadBytes_Object((1,3,6,1,4,1,50536,1,1,1,1,10),_ZpoolReadBytes_Type())
zpoolReadBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:zpoolReadBytes.setStatus(_A)
_ZpoolWriteBytes_Type=Counter64
_ZpoolWriteBytes_Object=MibTableColumn
zpoolWriteBytes=_ZpoolWriteBytes_Object((1,3,6,1,4,1,50536,1,1,1,1,11),_ZpoolWriteBytes_Type())
zpoolWriteBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:zpoolWriteBytes.setStatus(_A)
_ZpoolReadOps1sec_Type=Counter64
_ZpoolReadOps1sec_Object=MibTableColumn
zpoolReadOps1sec=_ZpoolReadOps1sec_Object((1,3,6,1,4,1,50536,1,1,1,1,12),_ZpoolReadOps1sec_Type())
zpoolReadOps1sec.setMaxAccess(_B)
if mibBuilder.loadTexts:zpoolReadOps1sec.setStatus(_A)
_ZpoolWriteOps1sec_Type=Counter64
_ZpoolWriteOps1sec_Object=MibTableColumn
zpoolWriteOps1sec=_ZpoolWriteOps1sec_Object((1,3,6,1,4,1,50536,1,1,1,1,13),_ZpoolWriteOps1sec_Type())
zpoolWriteOps1sec.setMaxAccess(_B)
if mibBuilder.loadTexts:zpoolWriteOps1sec.setStatus(_A)
_ZpoolReadBytes1sec_Type=Counter64
_ZpoolReadBytes1sec_Object=MibTableColumn
zpoolReadBytes1sec=_ZpoolReadBytes1sec_Object((1,3,6,1,4,1,50536,1,1,1,1,14),_ZpoolReadBytes1sec_Type())
zpoolReadBytes1sec.setMaxAccess(_B)
if mibBuilder.loadTexts:zpoolReadBytes1sec.setStatus(_A)
_ZpoolWriteBytes1sec_Type=Counter64
_ZpoolWriteBytes1sec_Object=MibTableColumn
zpoolWriteBytes1sec=_ZpoolWriteBytes1sec_Object((1,3,6,1,4,1,50536,1,1,1,1,15),_ZpoolWriteBytes1sec_Type())
zpoolWriteBytes1sec.setMaxAccess(_B)
if mibBuilder.loadTexts:zpoolWriteBytes1sec.setStatus(_A)
_Dataset_ObjectIdentity=ObjectIdentity
dataset=_Dataset_ObjectIdentity((1,3,6,1,4,1,50536,1,2))
_DatasetTable_Object=MibTable
datasetTable=_DatasetTable_Object((1,3,6,1,4,1,50536,1,2,1))
if mibBuilder.loadTexts:datasetTable.setStatus(_A)
_DatasetEntry_Object=MibTableRow
datasetEntry=_DatasetEntry_Object((1,3,6,1,4,1,50536,1,2,1,1))
datasetEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:datasetEntry.setStatus(_A)
class _DatasetIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DatasetIndex_Type.__name__=_C
_DatasetIndex_Object=MibTableColumn
datasetIndex=_DatasetIndex_Object((1,3,6,1,4,1,50536,1,2,1,1,1),_DatasetIndex_Type())
datasetIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:datasetIndex.setStatus(_A)
_DatasetDescr_Type=DisplayString
_DatasetDescr_Object=MibTableColumn
datasetDescr=_DatasetDescr_Object((1,3,6,1,4,1,50536,1,2,1,1,2),_DatasetDescr_Type())
datasetDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:datasetDescr.setStatus(_A)
class _DatasetAllocationUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DatasetAllocationUnits_Type.__name__=_C
_DatasetAllocationUnits_Object=MibTableColumn
datasetAllocationUnits=_DatasetAllocationUnits_Object((1,3,6,1,4,1,50536,1,2,1,1,3),_DatasetAllocationUnits_Type())
datasetAllocationUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:datasetAllocationUnits.setStatus(_A)
if mibBuilder.loadTexts:datasetAllocationUnits.setUnits(_F)
class _DatasetSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DatasetSize_Type.__name__=_C
_DatasetSize_Object=MibTableColumn
datasetSize=_DatasetSize_Object((1,3,6,1,4,1,50536,1,2,1,1,4),_DatasetSize_Type())
datasetSize.setMaxAccess(_G)
if mibBuilder.loadTexts:datasetSize.setStatus(_A)
class _DatasetUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DatasetUsed_Type.__name__=_C
_DatasetUsed_Object=MibTableColumn
datasetUsed=_DatasetUsed_Object((1,3,6,1,4,1,50536,1,2,1,1,5),_DatasetUsed_Type())
datasetUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:datasetUsed.setStatus(_A)
class _DatasetAvailable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_DatasetAvailable_Type.__name__=_C
_DatasetAvailable_Object=MibTableColumn
datasetAvailable=_DatasetAvailable_Object((1,3,6,1,4,1,50536,1,2,1,1,6),_DatasetAvailable_Type())
datasetAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:datasetAvailable.setStatus(_A)
_Zvol_ObjectIdentity=ObjectIdentity
zvol=_Zvol_ObjectIdentity((1,3,6,1,4,1,50536,1,3))
_ZvolTable_Object=MibTable
zvolTable=_ZvolTable_Object((1,3,6,1,4,1,50536,1,3,1))
if mibBuilder.loadTexts:zvolTable.setStatus(_A)
_ZvolEntry_Object=MibTableRow
zvolEntry=_ZvolEntry_Object((1,3,6,1,4,1,50536,1,3,1,1))
zvolEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:zvolEntry.setStatus(_A)
class _ZvolIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ZvolIndex_Type.__name__=_C
_ZvolIndex_Object=MibTableColumn
zvolIndex=_ZvolIndex_Object((1,3,6,1,4,1,50536,1,3,1,1,1),_ZvolIndex_Type())
zvolIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:zvolIndex.setStatus(_A)
_ZvolDescr_Type=DisplayString
_ZvolDescr_Object=MibTableColumn
zvolDescr=_ZvolDescr_Object((1,3,6,1,4,1,50536,1,3,1,1,2),_ZvolDescr_Type())
zvolDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:zvolDescr.setStatus(_A)
class _ZvolAllocationUnits_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ZvolAllocationUnits_Type.__name__=_C
_ZvolAllocationUnits_Object=MibTableColumn
zvolAllocationUnits=_ZvolAllocationUnits_Object((1,3,6,1,4,1,50536,1,3,1,1,3),_ZvolAllocationUnits_Type())
zvolAllocationUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:zvolAllocationUnits.setStatus(_A)
if mibBuilder.loadTexts:zvolAllocationUnits.setUnits(_F)
class _ZvolSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ZvolSize_Type.__name__=_C
_ZvolSize_Object=MibTableColumn
zvolSize=_ZvolSize_Object((1,3,6,1,4,1,50536,1,3,1,1,4),_ZvolSize_Type())
zvolSize.setMaxAccess(_G)
if mibBuilder.loadTexts:zvolSize.setStatus(_A)
class _ZvolUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ZvolUsed_Type.__name__=_C
_ZvolUsed_Object=MibTableColumn
zvolUsed=_ZvolUsed_Object((1,3,6,1,4,1,50536,1,3,1,1,5),_ZvolUsed_Type())
zvolUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:zvolUsed.setStatus(_A)
class _ZvolAvailable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ZvolAvailable_Type.__name__=_C
_ZvolAvailable_Object=MibTableColumn
zvolAvailable=_ZvolAvailable_Object((1,3,6,1,4,1,50536,1,3,1,1,6),_ZvolAvailable_Type())
zvolAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:zvolAvailable.setStatus(_A)
class _ZvolReferenced_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ZvolReferenced_Type.__name__=_C
_ZvolReferenced_Object=MibTableColumn
zvolReferenced=_ZvolReferenced_Object((1,3,6,1,4,1,50536,1,3,1,1,7),_ZvolReferenced_Type())
zvolReferenced.setMaxAccess(_B)
if mibBuilder.loadTexts:zvolReferenced.setStatus(_A)
_Arc_ObjectIdentity=ObjectIdentity
arc=_Arc_ObjectIdentity((1,3,6,1,4,1,50536,1,4))
_ZfsArcSize_Type=Gauge32
_ZfsArcSize_Object=MibScalar
zfsArcSize=_ZfsArcSize_Object((1,3,6,1,4,1,50536,1,4,1),_ZfsArcSize_Type())
zfsArcSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zfsArcSize.setStatus(_A)
_ZfsArcMeta_Type=Gauge32
_ZfsArcMeta_Object=MibScalar
zfsArcMeta=_ZfsArcMeta_Object((1,3,6,1,4,1,50536,1,4,2),_ZfsArcMeta_Type())
zfsArcMeta.setMaxAccess(_B)
if mibBuilder.loadTexts:zfsArcMeta.setStatus(_A)
_ZfsArcData_Type=Gauge32
_ZfsArcData_Object=MibScalar
zfsArcData=_ZfsArcData_Object((1,3,6,1,4,1,50536,1,4,3),_ZfsArcData_Type())
zfsArcData.setMaxAccess(_B)
if mibBuilder.loadTexts:zfsArcData.setStatus(_A)
_ZfsArcHits_Type=Gauge32
_ZfsArcHits_Object=MibScalar
zfsArcHits=_ZfsArcHits_Object((1,3,6,1,4,1,50536,1,4,4),_ZfsArcHits_Type())
zfsArcHits.setMaxAccess(_B)
if mibBuilder.loadTexts:zfsArcHits.setStatus(_A)
_ZfsArcMisses_Type=Gauge32
_ZfsArcMisses_Object=MibScalar
zfsArcMisses=_ZfsArcMisses_Object((1,3,6,1,4,1,50536,1,4,5),_ZfsArcMisses_Type())
zfsArcMisses.setMaxAccess(_B)
if mibBuilder.loadTexts:zfsArcMisses.setStatus(_A)
_ZfsArcC_Type=Gauge32
_ZfsArcC_Object=MibScalar
zfsArcC=_ZfsArcC_Object((1,3,6,1,4,1,50536,1,4,6),_ZfsArcC_Type())
zfsArcC.setMaxAccess(_B)
if mibBuilder.loadTexts:zfsArcC.setStatus(_A)
_ZfsArcP_Type=Gauge32
_ZfsArcP_Object=MibScalar
zfsArcP=_ZfsArcP_Object((1,3,6,1,4,1,50536,1,4,7),_ZfsArcP_Type())
zfsArcP.setMaxAccess(_B)
if mibBuilder.loadTexts:zfsArcP.setStatus(_A)
_ZfsArcMissPercent_Type=DisplayString
_ZfsArcMissPercent_Object=MibScalar
zfsArcMissPercent=_ZfsArcMissPercent_Object((1,3,6,1,4,1,50536,1,4,8),_ZfsArcMissPercent_Type())
zfsArcMissPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:zfsArcMissPercent.setStatus(_A)
_ZfsArcCacheHitRatio_Type=DisplayString
_ZfsArcCacheHitRatio_Object=MibScalar
zfsArcCacheHitRatio=_ZfsArcCacheHitRatio_Object((1,3,6,1,4,1,50536,1,4,9),_ZfsArcCacheHitRatio_Type())
zfsArcCacheHitRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:zfsArcCacheHitRatio.setStatus(_A)
_ZfsArcCacheMissRatio_Type=DisplayString
_ZfsArcCacheMissRatio_Object=MibScalar
zfsArcCacheMissRatio=_ZfsArcCacheMissRatio_Object((1,3,6,1,4,1,50536,1,4,10),_ZfsArcCacheMissRatio_Type())
zfsArcCacheMissRatio.setMaxAccess(_B)
if mibBuilder.loadTexts:zfsArcCacheMissRatio.setStatus(_A)
_L2arc_ObjectIdentity=ObjectIdentity
l2arc=_L2arc_ObjectIdentity((1,3,6,1,4,1,50536,1,5))
_ZfsL2ArcHits_Type=Counter32
_ZfsL2ArcHits_Object=MibScalar
zfsL2ArcHits=_ZfsL2ArcHits_Object((1,3,6,1,4,1,50536,1,5,1),_ZfsL2ArcHits_Type())
zfsL2ArcHits.setMaxAccess(_B)
if mibBuilder.loadTexts:zfsL2ArcHits.setStatus(_A)
_ZfsL2ArcMisses_Type=Counter32
_ZfsL2ArcMisses_Object=MibScalar
zfsL2ArcMisses=_ZfsL2ArcMisses_Object((1,3,6,1,4,1,50536,1,5,2),_ZfsL2ArcMisses_Type())
zfsL2ArcMisses.setMaxAccess(_B)
if mibBuilder.loadTexts:zfsL2ArcMisses.setStatus(_A)
_ZfsL2ArcRead_Type=Counter32
_ZfsL2ArcRead_Object=MibScalar
zfsL2ArcRead=_ZfsL2ArcRead_Object((1,3,6,1,4,1,50536,1,5,3),_ZfsL2ArcRead_Type())
zfsL2ArcRead.setMaxAccess(_B)
if mibBuilder.loadTexts:zfsL2ArcRead.setStatus(_A)
_ZfsL2ArcWrite_Type=Counter32
_ZfsL2ArcWrite_Object=MibScalar
zfsL2ArcWrite=_ZfsL2ArcWrite_Object((1,3,6,1,4,1,50536,1,5,4),_ZfsL2ArcWrite_Type())
zfsL2ArcWrite.setMaxAccess(_B)
if mibBuilder.loadTexts:zfsL2ArcWrite.setStatus(_A)
_ZfsL2ArcSize_Type=Gauge32
_ZfsL2ArcSize_Object=MibScalar
zfsL2ArcSize=_ZfsL2ArcSize_Object((1,3,6,1,4,1,50536,1,5,5),_ZfsL2ArcSize_Type())
zfsL2ArcSize.setMaxAccess(_B)
if mibBuilder.loadTexts:zfsL2ArcSize.setStatus(_A)
_Zil_ObjectIdentity=ObjectIdentity
zil=_Zil_ObjectIdentity((1,3,6,1,4,1,50536,1,6))
_ZfsZilstatOps1sec_Type=Counter64
_ZfsZilstatOps1sec_Object=MibScalar
zfsZilstatOps1sec=_ZfsZilstatOps1sec_Object((1,3,6,1,4,1,50536,1,6,1),_ZfsZilstatOps1sec_Type())
zfsZilstatOps1sec.setMaxAccess(_B)
if mibBuilder.loadTexts:zfsZilstatOps1sec.setStatus(_A)
_ZfsZilstatOps5sec_Type=Counter64
_ZfsZilstatOps5sec_Object=MibScalar
zfsZilstatOps5sec=_ZfsZilstatOps5sec_Object((1,3,6,1,4,1,50536,1,6,2),_ZfsZilstatOps5sec_Type())
zfsZilstatOps5sec.setMaxAccess(_B)
if mibBuilder.loadTexts:zfsZilstatOps5sec.setStatus(_A)
_ZfsZilstatOps10sec_Type=Counter64
_ZfsZilstatOps10sec_Object=MibScalar
zfsZilstatOps10sec=_ZfsZilstatOps10sec_Object((1,3,6,1,4,1,50536,1,6,3),_ZfsZilstatOps10sec_Type())
zfsZilstatOps10sec.setMaxAccess(_B)
if mibBuilder.loadTexts:zfsZilstatOps10sec.setStatus(_A)
_Notifications_ObjectIdentity=ObjectIdentity
notifications=_Notifications_ObjectIdentity((1,3,6,1,4,1,50536,2))
_NotificationPrefix_ObjectIdentity=ObjectIdentity
notificationPrefix=_NotificationPrefix_ObjectIdentity((1,3,6,1,4,1,50536,2,1))
_NotificationObjects_ObjectIdentity=ObjectIdentity
notificationObjects=_NotificationObjects_ObjectIdentity((1,3,6,1,4,1,50536,2,2))
_AlertId_Type=DisplayString
_AlertId_Object=MibScalar
alertId=_AlertId_Object((1,3,6,1,4,1,50536,2,2,1),_AlertId_Type())
alertId.setMaxAccess(_B)
if mibBuilder.loadTexts:alertId.setStatus(_A)
_AlertLevel_Type=AlertLevelType
_AlertLevel_Object=MibScalar
alertLevel=_AlertLevel_Object((1,3,6,1,4,1,50536,2,2,2),_AlertLevel_Type())
alertLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:alertLevel.setStatus(_A)
_AlertMessage_Type=DisplayString
_AlertMessage_Object=MibScalar
alertMessage=_AlertMessage_Object((1,3,6,1,4,1,50536,2,2,3),_AlertMessage_Type())
alertMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:alertMessage.setStatus(_A)
_HddTempTable_Object=MibTable
hddTempTable=_HddTempTable_Object((1,3,6,1,4,1,50536,3))
if mibBuilder.loadTexts:hddTempTable.setStatus(_A)
_HddTempEntry_Object=MibTableRow
hddTempEntry=_HddTempEntry_Object((1,3,6,1,4,1,50536,3,1))
hddTempEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:hddTempEntry.setStatus(_A)
class _HddTempIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HddTempIndex_Type.__name__=_C
_HddTempIndex_Object=MibTableColumn
hddTempIndex=_HddTempIndex_Object((1,3,6,1,4,1,50536,3,1,1),_HddTempIndex_Type())
hddTempIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hddTempIndex.setStatus(_A)
_HddTempDevice_Type=DisplayString
_HddTempDevice_Object=MibTableColumn
hddTempDevice=_HddTempDevice_Object((1,3,6,1,4,1,50536,3,1,2),_HddTempDevice_Type())
hddTempDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:hddTempDevice.setStatus(_A)
_HddTempValue_Type=Gauge32
_HddTempValue_Object=MibTableColumn
hddTempValue=_HddTempValue_Object((1,3,6,1,4,1,50536,3,1,3),_HddTempValue_Type())
hddTempValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hddTempValue.setStatus(_A)
_Iftop_ObjectIdentity=ObjectIdentity
iftop=_Iftop_ObjectIdentity((1,3,6,1,4,1,50536,4))
_InterfaceTable_Object=MibTable
interfaceTable=_InterfaceTable_Object((1,3,6,1,4,1,50536,4,1))
if mibBuilder.loadTexts:interfaceTable.setStatus(_A)
_InterfaceEntry_Object=MibTableRow
interfaceEntry=_InterfaceEntry_Object((1,3,6,1,4,1,50536,4,1,1))
interfaceEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:interfaceEntry.setStatus(_A)
class _InterfaceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_InterfaceIndex_Type.__name__=_C
_InterfaceIndex_Object=MibTableColumn
interfaceIndex=_InterfaceIndex_Object((1,3,6,1,4,1,50536,4,1,1,1),_InterfaceIndex_Type())
interfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceIndex.setStatus(_A)
_InterfaceName_Type=DisplayString
_InterfaceName_Object=MibTableColumn
interfaceName=_InterfaceName_Object((1,3,6,1,4,1,50536,4,1,1,2),_InterfaceName_Type())
interfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceName.setStatus(_A)
_InterfaceTopHostTable_Object=MibTable
interfaceTopHostTable=_InterfaceTopHostTable_Object((1,3,6,1,4,1,50536,4,2))
if mibBuilder.loadTexts:interfaceTopHostTable.setStatus(_A)
_InterfaceTopHostEntry_Object=MibTableRow
interfaceTopHostEntry=_InterfaceTopHostEntry_Object((1,3,6,1,4,1,50536,4,2,1))
interfaceTopHostEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:interfaceTopHostEntry.setStatus(_A)
class _InterfaceTopHostIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_InterfaceTopHostIndex_Type.__name__=_C
_InterfaceTopHostIndex_Object=MibTableColumn
interfaceTopHostIndex=_InterfaceTopHostIndex_Object((1,3,6,1,4,1,50536,4,2,1,1),_InterfaceTopHostIndex_Type())
interfaceTopHostIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceTopHostIndex.setStatus(_A)
_InterfaceTopHostInterfaceName_Type=DisplayString
_InterfaceTopHostInterfaceName_Object=MibTableColumn
interfaceTopHostInterfaceName=_InterfaceTopHostInterfaceName_Object((1,3,6,1,4,1,50536,4,2,1,2),_InterfaceTopHostInterfaceName_Type())
interfaceTopHostInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceTopHostInterfaceName.setStatus(_A)
_InterfaceTopHostLocalAddress_Type=DisplayString
_InterfaceTopHostLocalAddress_Object=MibTableColumn
interfaceTopHostLocalAddress=_InterfaceTopHostLocalAddress_Object((1,3,6,1,4,1,50536,4,2,1,3),_InterfaceTopHostLocalAddress_Type())
interfaceTopHostLocalAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceTopHostLocalAddress.setStatus(_A)
class _InterfaceTopHostLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_InterfaceTopHostLocalPort_Type.__name__=_C
_InterfaceTopHostLocalPort_Object=MibTableColumn
interfaceTopHostLocalPort=_InterfaceTopHostLocalPort_Object((1,3,6,1,4,1,50536,4,2,1,4),_InterfaceTopHostLocalPort_Type())
interfaceTopHostLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceTopHostLocalPort.setStatus(_A)
_InterfaceTopHostRemoteAddress_Type=DisplayString
_InterfaceTopHostRemoteAddress_Object=MibTableColumn
interfaceTopHostRemoteAddress=_InterfaceTopHostRemoteAddress_Object((1,3,6,1,4,1,50536,4,2,1,5),_InterfaceTopHostRemoteAddress_Type())
interfaceTopHostRemoteAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceTopHostRemoteAddress.setStatus(_A)
class _InterfaceTopHostRemotePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_InterfaceTopHostRemotePort_Type.__name__=_C
_InterfaceTopHostRemotePort_Object=MibTableColumn
interfaceTopHostRemotePort=_InterfaceTopHostRemotePort_Object((1,3,6,1,4,1,50536,4,2,1,6),_InterfaceTopHostRemotePort_Type())
interfaceTopHostRemotePort.setMaxAccess(_B)
if mibBuilder.loadTexts:interfaceTopHostRemotePort.setStatus(_A)
class _InLast2s_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_InLast2s_Type.__name__=_C
_InLast2s_Object=MibTableColumn
inLast2s=_InLast2s_Object((1,3,6,1,4,1,50536,4,2,1,7),_InLast2s_Type())
inLast2s.setMaxAccess(_B)
if mibBuilder.loadTexts:inLast2s.setStatus(_A)
class _OutLast2s_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OutLast2s_Type.__name__=_C
_OutLast2s_Object=MibTableColumn
outLast2s=_OutLast2s_Object((1,3,6,1,4,1,50536,4,2,1,8),_OutLast2s_Type())
outLast2s.setMaxAccess(_B)
if mibBuilder.loadTexts:outLast2s.setStatus(_A)
class _InLast10s_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_InLast10s_Type.__name__=_C
_InLast10s_Object=MibTableColumn
inLast10s=_InLast10s_Object((1,3,6,1,4,1,50536,4,2,1,9),_InLast10s_Type())
inLast10s.setMaxAccess(_B)
if mibBuilder.loadTexts:inLast10s.setStatus(_A)
class _OutLast10s_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OutLast10s_Type.__name__=_C
_OutLast10s_Object=MibTableColumn
outLast10s=_OutLast10s_Object((1,3,6,1,4,1,50536,4,2,1,10),_OutLast10s_Type())
outLast10s.setMaxAccess(_B)
if mibBuilder.loadTexts:outLast10s.setStatus(_A)
class _InLast40s_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_InLast40s_Type.__name__=_C
_InLast40s_Object=MibTableColumn
inLast40s=_InLast40s_Object((1,3,6,1,4,1,50536,4,2,1,11),_InLast40s_Type())
inLast40s.setMaxAccess(_B)
if mibBuilder.loadTexts:inLast40s.setStatus(_A)
class _OutLast40s_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_OutLast40s_Type.__name__=_C
_OutLast40s_Object=MibTableColumn
outLast40s=_OutLast40s_Object((1,3,6,1,4,1,50536,4,2,1,12),_OutLast40s_Type())
outLast40s.setMaxAccess(_B)
if mibBuilder.loadTexts:outLast40s.setStatus(_A)
alert=NotificationType((1,3,6,1,4,1,50536,2,1,1))
alert.setObjects(*((_D,_H),(_D,_O),(_D,_P)))
if mibBuilder.loadTexts:alert.setStatus(_A)
alertCancellation=NotificationType((1,3,6,1,4,1,50536,2,1,2))
alertCancellation.setObjects((_D,_H))
if mibBuilder.loadTexts:alertCancellation.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ZPoolHealthType':ZPoolHealthType,'AlertLevelType':AlertLevelType,'freeNas':freeNas,'zfs':zfs,'zpool':zpool,'zpoolTable':zpoolTable,'zpoolEntry':zpoolEntry,_I:zpoolIndex,'zpoolDescr':zpoolDescr,'zpoolAllocationUnits':zpoolAllocationUnits,'zpoolSize':zpoolSize,'zpoolUsed':zpoolUsed,'zpoolAvailable':zpoolAvailable,'zpoolHealth':zpoolHealth,'zpoolReadOps':zpoolReadOps,'zpoolWriteOps':zpoolWriteOps,'zpoolReadBytes':zpoolReadBytes,'zpoolWriteBytes':zpoolWriteBytes,'zpoolReadOps1sec':zpoolReadOps1sec,'zpoolWriteOps1sec':zpoolWriteOps1sec,'zpoolReadBytes1sec':zpoolReadBytes1sec,'zpoolWriteBytes1sec':zpoolWriteBytes1sec,'dataset':dataset,'datasetTable':datasetTable,'datasetEntry':datasetEntry,_J:datasetIndex,'datasetDescr':datasetDescr,'datasetAllocationUnits':datasetAllocationUnits,'datasetSize':datasetSize,'datasetUsed':datasetUsed,'datasetAvailable':datasetAvailable,'zvol':zvol,'zvolTable':zvolTable,'zvolEntry':zvolEntry,_K:zvolIndex,'zvolDescr':zvolDescr,'zvolAllocationUnits':zvolAllocationUnits,'zvolSize':zvolSize,'zvolUsed':zvolUsed,'zvolAvailable':zvolAvailable,'zvolReferenced':zvolReferenced,'arc':arc,'zfsArcSize':zfsArcSize,'zfsArcMeta':zfsArcMeta,'zfsArcData':zfsArcData,'zfsArcHits':zfsArcHits,'zfsArcMisses':zfsArcMisses,'zfsArcC':zfsArcC,'zfsArcP':zfsArcP,'zfsArcMissPercent':zfsArcMissPercent,'zfsArcCacheHitRatio':zfsArcCacheHitRatio,'zfsArcCacheMissRatio':zfsArcCacheMissRatio,'l2arc':l2arc,'zfsL2ArcHits':zfsL2ArcHits,'zfsL2ArcMisses':zfsL2ArcMisses,'zfsL2ArcRead':zfsL2ArcRead,'zfsL2ArcWrite':zfsL2ArcWrite,'zfsL2ArcSize':zfsL2ArcSize,'zil':zil,'zfsZilstatOps1sec':zfsZilstatOps1sec,'zfsZilstatOps5sec':zfsZilstatOps5sec,'zfsZilstatOps10sec':zfsZilstatOps10sec,'notifications':notifications,'notificationPrefix':notificationPrefix,'alert':alert,'alertCancellation':alertCancellation,'notificationObjects':notificationObjects,_H:alertId,_O:alertLevel,_P:alertMessage,'hddTempTable':hddTempTable,'hddTempEntry':hddTempEntry,_L:hddTempIndex,'hddTempDevice':hddTempDevice,'hddTempValue':hddTempValue,'iftop':iftop,'interfaceTable':interfaceTable,'interfaceEntry':interfaceEntry,_M:interfaceIndex,'interfaceName':interfaceName,'interfaceTopHostTable':interfaceTopHostTable,'interfaceTopHostEntry':interfaceTopHostEntry,_N:interfaceTopHostIndex,'interfaceTopHostInterfaceName':interfaceTopHostInterfaceName,'interfaceTopHostLocalAddress':interfaceTopHostLocalAddress,'interfaceTopHostLocalPort':interfaceTopHostLocalPort,'interfaceTopHostRemoteAddress':interfaceTopHostRemoteAddress,'interfaceTopHostRemotePort':interfaceTopHostRemotePort,'inLast2s':inLast2s,'outLast2s':outLast2s,'inLast10s':inLast10s,'outLast10s':outLast10s,'inLast40s':inLast40s,'outLast40s':outLast40s})