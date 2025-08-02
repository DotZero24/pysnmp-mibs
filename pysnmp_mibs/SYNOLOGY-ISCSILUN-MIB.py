_Y='synologyiSCSILUNGroup'
_X='iSCSILUNThinProvisionVolFreeMBs'
_W='iSCSILUNDiskLatencyAvg'
_V='iSCSILUNType'
_U='iSCSILUNQueueDepth'
_T='iSCSILUNIoSizeWrite'
_S='iSCSILUNIoSizeRead'
_R='iSCSILUNNetworkLatencyRx'
_Q='iSCSILUNNetworkLatencyTx'
_P='iSCSILUNDiskLatencyWrite'
_O='iSCSILUNDiskLatencyRead'
_N='iSCSILUNIopsWrite'
_M='iSCSILUNIopsRead'
_L='iSCSILUNThroughputWriteLow'
_K='iSCSILUNThroughputWriteHigh'
_J='iSCSILUNThroughputReadLow'
_I='iSCSILUNThroughputReadHigh'
_H='iSCSILUNName'
_G='iSCSILUNUUID'
_F='iSCSILUNInfoIndex'
_E='Integer32'
_D='OctetString'
_C='read-only'
_B='SYNOLOGY-ISCSILUN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
synologyiSCSILUN=ModuleIdentity((1,3,6,1,4,1,6574,104))
if mibBuilder.loadTexts:synologyiSCSILUN.setRevisions(('2020-08-12 00:00',))
_Synology_ObjectIdentity=ObjectIdentity
synology=_Synology_ObjectIdentity((1,3,6,1,4,1,6574))
_ISCSILUNTable_Object=MibTable
iSCSILUNTable=_ISCSILUNTable_Object((1,3,6,1,4,1,6574,104,1))
if mibBuilder.loadTexts:iSCSILUNTable.setStatus(_A)
_ISCSILUNEntry_Object=MibTableRow
iSCSILUNEntry=_ISCSILUNEntry_Object((1,3,6,1,4,1,6574,104,1,1))
iSCSILUNEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:iSCSILUNEntry.setStatus(_A)
class _ISCSILUNInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ISCSILUNInfoIndex_Type.__name__=_E
_ISCSILUNInfoIndex_Object=MibTableColumn
iSCSILUNInfoIndex=_ISCSILUNInfoIndex_Object((1,3,6,1,4,1,6574,104,1,1,1),_ISCSILUNInfoIndex_Type())
iSCSILUNInfoIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:iSCSILUNInfoIndex.setStatus(_A)
class _ISCSILUNUUID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ISCSILUNUUID_Type.__name__=_D
_ISCSILUNUUID_Object=MibTableColumn
iSCSILUNUUID=_ISCSILUNUUID_Object((1,3,6,1,4,1,6574,104,1,1,2),_ISCSILUNUUID_Type())
iSCSILUNUUID.setMaxAccess(_C)
if mibBuilder.loadTexts:iSCSILUNUUID.setStatus(_A)
class _ISCSILUNName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ISCSILUNName_Type.__name__=_D
_ISCSILUNName_Object=MibTableColumn
iSCSILUNName=_ISCSILUNName_Object((1,3,6,1,4,1,6574,104,1,1,3),_ISCSILUNName_Type())
iSCSILUNName.setMaxAccess(_C)
if mibBuilder.loadTexts:iSCSILUNName.setStatus(_A)
_ISCSILUNThroughputReadHigh_Type=Integer32
_ISCSILUNThroughputReadHigh_Object=MibTableColumn
iSCSILUNThroughputReadHigh=_ISCSILUNThroughputReadHigh_Object((1,3,6,1,4,1,6574,104,1,1,4),_ISCSILUNThroughputReadHigh_Type())
iSCSILUNThroughputReadHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:iSCSILUNThroughputReadHigh.setStatus(_A)
_ISCSILUNThroughputReadLow_Type=Integer32
_ISCSILUNThroughputReadLow_Object=MibTableColumn
iSCSILUNThroughputReadLow=_ISCSILUNThroughputReadLow_Object((1,3,6,1,4,1,6574,104,1,1,5),_ISCSILUNThroughputReadLow_Type())
iSCSILUNThroughputReadLow.setMaxAccess(_C)
if mibBuilder.loadTexts:iSCSILUNThroughputReadLow.setStatus(_A)
_ISCSILUNThroughputWriteHigh_Type=Integer32
_ISCSILUNThroughputWriteHigh_Object=MibTableColumn
iSCSILUNThroughputWriteHigh=_ISCSILUNThroughputWriteHigh_Object((1,3,6,1,4,1,6574,104,1,1,6),_ISCSILUNThroughputWriteHigh_Type())
iSCSILUNThroughputWriteHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:iSCSILUNThroughputWriteHigh.setStatus(_A)
_ISCSILUNThroughputWriteLow_Type=Integer32
_ISCSILUNThroughputWriteLow_Object=MibTableColumn
iSCSILUNThroughputWriteLow=_ISCSILUNThroughputWriteLow_Object((1,3,6,1,4,1,6574,104,1,1,7),_ISCSILUNThroughputWriteLow_Type())
iSCSILUNThroughputWriteLow.setMaxAccess(_C)
if mibBuilder.loadTexts:iSCSILUNThroughputWriteLow.setStatus(_A)
_ISCSILUNIopsRead_Type=Integer32
_ISCSILUNIopsRead_Object=MibTableColumn
iSCSILUNIopsRead=_ISCSILUNIopsRead_Object((1,3,6,1,4,1,6574,104,1,1,8),_ISCSILUNIopsRead_Type())
iSCSILUNIopsRead.setMaxAccess(_C)
if mibBuilder.loadTexts:iSCSILUNIopsRead.setStatus(_A)
_ISCSILUNIopsWrite_Type=Integer32
_ISCSILUNIopsWrite_Object=MibTableColumn
iSCSILUNIopsWrite=_ISCSILUNIopsWrite_Object((1,3,6,1,4,1,6574,104,1,1,9),_ISCSILUNIopsWrite_Type())
iSCSILUNIopsWrite.setMaxAccess(_C)
if mibBuilder.loadTexts:iSCSILUNIopsWrite.setStatus(_A)
_ISCSILUNDiskLatencyRead_Type=Integer32
_ISCSILUNDiskLatencyRead_Object=MibTableColumn
iSCSILUNDiskLatencyRead=_ISCSILUNDiskLatencyRead_Object((1,3,6,1,4,1,6574,104,1,1,10),_ISCSILUNDiskLatencyRead_Type())
iSCSILUNDiskLatencyRead.setMaxAccess(_C)
if mibBuilder.loadTexts:iSCSILUNDiskLatencyRead.setStatus(_A)
_ISCSILUNDiskLatencyWrite_Type=Integer32
_ISCSILUNDiskLatencyWrite_Object=MibTableColumn
iSCSILUNDiskLatencyWrite=_ISCSILUNDiskLatencyWrite_Object((1,3,6,1,4,1,6574,104,1,1,11),_ISCSILUNDiskLatencyWrite_Type())
iSCSILUNDiskLatencyWrite.setMaxAccess(_C)
if mibBuilder.loadTexts:iSCSILUNDiskLatencyWrite.setStatus(_A)
_ISCSILUNNetworkLatencyTx_Type=Integer32
_ISCSILUNNetworkLatencyTx_Object=MibTableColumn
iSCSILUNNetworkLatencyTx=_ISCSILUNNetworkLatencyTx_Object((1,3,6,1,4,1,6574,104,1,1,12),_ISCSILUNNetworkLatencyTx_Type())
iSCSILUNNetworkLatencyTx.setMaxAccess(_C)
if mibBuilder.loadTexts:iSCSILUNNetworkLatencyTx.setStatus(_A)
_ISCSILUNNetworkLatencyRx_Type=Integer32
_ISCSILUNNetworkLatencyRx_Object=MibTableColumn
iSCSILUNNetworkLatencyRx=_ISCSILUNNetworkLatencyRx_Object((1,3,6,1,4,1,6574,104,1,1,13),_ISCSILUNNetworkLatencyRx_Type())
iSCSILUNNetworkLatencyRx.setMaxAccess(_C)
if mibBuilder.loadTexts:iSCSILUNNetworkLatencyRx.setStatus(_A)
_ISCSILUNIoSizeRead_Type=Integer32
_ISCSILUNIoSizeRead_Object=MibTableColumn
iSCSILUNIoSizeRead=_ISCSILUNIoSizeRead_Object((1,3,6,1,4,1,6574,104,1,1,14),_ISCSILUNIoSizeRead_Type())
iSCSILUNIoSizeRead.setMaxAccess(_C)
if mibBuilder.loadTexts:iSCSILUNIoSizeRead.setStatus(_A)
_ISCSILUNIoSizeWrite_Type=Integer32
_ISCSILUNIoSizeWrite_Object=MibTableColumn
iSCSILUNIoSizeWrite=_ISCSILUNIoSizeWrite_Object((1,3,6,1,4,1,6574,104,1,1,15),_ISCSILUNIoSizeWrite_Type())
iSCSILUNIoSizeWrite.setMaxAccess(_C)
if mibBuilder.loadTexts:iSCSILUNIoSizeWrite.setStatus(_A)
_ISCSILUNQueueDepth_Type=Integer32
_ISCSILUNQueueDepth_Object=MibTableColumn
iSCSILUNQueueDepth=_ISCSILUNQueueDepth_Object((1,3,6,1,4,1,6574,104,1,1,16),_ISCSILUNQueueDepth_Type())
iSCSILUNQueueDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:iSCSILUNQueueDepth.setStatus(_A)
class _ISCSILUNType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ISCSILUNType_Type.__name__=_D
_ISCSILUNType_Object=MibTableColumn
iSCSILUNType=_ISCSILUNType_Object((1,3,6,1,4,1,6574,104,1,1,17),_ISCSILUNType_Type())
iSCSILUNType.setMaxAccess(_C)
if mibBuilder.loadTexts:iSCSILUNType.setStatus(_A)
_ISCSILUNDiskLatencyAvg_Type=Integer32
_ISCSILUNDiskLatencyAvg_Object=MibTableColumn
iSCSILUNDiskLatencyAvg=_ISCSILUNDiskLatencyAvg_Object((1,3,6,1,4,1,6574,104,1,1,18),_ISCSILUNDiskLatencyAvg_Type())
iSCSILUNDiskLatencyAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:iSCSILUNDiskLatencyAvg.setStatus(_A)
_ISCSILUNThinProvisionVolFreeMBs_Type=Integer32
_ISCSILUNThinProvisionVolFreeMBs_Object=MibTableColumn
iSCSILUNThinProvisionVolFreeMBs=_ISCSILUNThinProvisionVolFreeMBs_Object((1,3,6,1,4,1,6574,104,1,1,19),_ISCSILUNThinProvisionVolFreeMBs_Type())
iSCSILUNThinProvisionVolFreeMBs.setMaxAccess(_C)
if mibBuilder.loadTexts:iSCSILUNThinProvisionVolFreeMBs.setStatus(_A)
_SynologyiSCSILUNConformance_ObjectIdentity=ObjectIdentity
synologyiSCSILUNConformance=_SynologyiSCSILUNConformance_ObjectIdentity((1,3,6,1,4,1,6574,104,2))
_SynologyiSCSILUNCompliances_ObjectIdentity=ObjectIdentity
synologyiSCSILUNCompliances=_SynologyiSCSILUNCompliances_ObjectIdentity((1,3,6,1,4,1,6574,104,2,1))
_SynologyiSCSILUNGroups_ObjectIdentity=ObjectIdentity
synologyiSCSILUNGroups=_SynologyiSCSILUNGroups_ObjectIdentity((1,3,6,1,4,1,6574,104,2,2))
synologyiSCSILUNGroup=ObjectGroup((1,3,6,1,4,1,6574,104,2,2,1))
synologyiSCSILUNGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:synologyiSCSILUNGroup.setStatus(_A)
synologyiSCSILUNCompliance=ModuleCompliance((1,3,6,1,4,1,6574,104,2,1,1))
synologyiSCSILUNCompliance.setObjects((_B,_Y))
if mibBuilder.loadTexts:synologyiSCSILUNCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'synology':synology,'synologyiSCSILUN':synologyiSCSILUN,'iSCSILUNTable':iSCSILUNTable,'iSCSILUNEntry':iSCSILUNEntry,_F:iSCSILUNInfoIndex,_G:iSCSILUNUUID,_H:iSCSILUNName,_I:iSCSILUNThroughputReadHigh,_J:iSCSILUNThroughputReadLow,_K:iSCSILUNThroughputWriteHigh,_L:iSCSILUNThroughputWriteLow,_M:iSCSILUNIopsRead,_N:iSCSILUNIopsWrite,_O:iSCSILUNDiskLatencyRead,_P:iSCSILUNDiskLatencyWrite,_Q:iSCSILUNNetworkLatencyTx,_R:iSCSILUNNetworkLatencyRx,_S:iSCSILUNIoSizeRead,_T:iSCSILUNIoSizeWrite,_U:iSCSILUNQueueDepth,_V:iSCSILUNType,_W:iSCSILUNDiskLatencyAvg,_X:iSCSILUNThinProvisionVolFreeMBs,'synologyiSCSILUNConformance':synologyiSCSILUNConformance,'synologyiSCSILUNCompliances':synologyiSCSILUNCompliances,'synologyiSCSILUNCompliance':synologyiSCSILUNCompliance,'synologyiSCSILUNGroups':synologyiSCSILUNGroups,_Y:synologyiSCSILUNGroup})