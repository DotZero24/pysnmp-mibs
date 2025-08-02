_Q='eltexStorageThresholdIndex'
_P='read-write'
_O='SyslogSeverity'
_N='EltexPercent'
_M='eltexStorageThresholdValue'
_L='eltexStorageThresholdRelation'
_K='eltexStorageThresholdSeverity'
_J='eltexStoragePartitionFreePercent'
_I='eltexStoragePartitionIndex'
_H='not-accessible'
_G='eltexStorageDeviceIndex'
_F='TruthValue'
_E='read-create'
_D='bytes'
_C='read-only'
_B='ELTEX-STORAGE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltexLtd,=mibBuilder.importSymbols('ELTEX-SMI-ACTUAL','eltexLtd')
EltexPercent,EltexThresholdRelation=mibBuilder.importSymbols('ELTEX-TC',_N,'EltexThresholdRelation')
PhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_F)
SyslogSeverity,=mibBuilder.importSymbols('SYSLOG-TC-MIB',_O)
eltexStorageMIB=ModuleIdentity((1,3,6,1,4,1,35265,39))
if mibBuilder.loadTexts:eltexStorageMIB.setRevisions(('2017-05-02 00:00',))
class EltexStorageType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ramfs',1),('spi',2),('raw-nand',3),('sata',4),('sd-card',5),('usb',6)))
_EltexStorageMIBObjects_ObjectIdentity=ObjectIdentity
eltexStorageMIBObjects=_EltexStorageMIBObjects_ObjectIdentity((1,3,6,1,4,1,35265,39,1))
_EltexStorageDevice_ObjectIdentity=ObjectIdentity
eltexStorageDevice=_EltexStorageDevice_ObjectIdentity((1,3,6,1,4,1,35265,39,1,1))
_EltexStorageDeviceTable_Object=MibTable
eltexStorageDeviceTable=_EltexStorageDeviceTable_Object((1,3,6,1,4,1,35265,39,1,1,1))
if mibBuilder.loadTexts:eltexStorageDeviceTable.setStatus(_A)
_EltexStorageDeviceEntry_Object=MibTableRow
eltexStorageDeviceEntry=_EltexStorageDeviceEntry_Object((1,3,6,1,4,1,35265,39,1,1,1,1))
eltexStorageDeviceEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:eltexStorageDeviceEntry.setStatus(_A)
_EltexStorageDeviceIndex_Type=Unsigned32
_EltexStorageDeviceIndex_Object=MibTableColumn
eltexStorageDeviceIndex=_EltexStorageDeviceIndex_Object((1,3,6,1,4,1,35265,39,1,1,1,1,1),_EltexStorageDeviceIndex_Type())
eltexStorageDeviceIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:eltexStorageDeviceIndex.setStatus(_A)
_EltexStorageDevicePhysicalIndex_Type=PhysicalIndex
_EltexStorageDevicePhysicalIndex_Object=MibTableColumn
eltexStorageDevicePhysicalIndex=_EltexStorageDevicePhysicalIndex_Object((1,3,6,1,4,1,35265,39,1,1,1,1,2),_EltexStorageDevicePhysicalIndex_Type())
eltexStorageDevicePhysicalIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexStorageDevicePhysicalIndex.setStatus(_A)
_EltexStorageDeviceType_Type=EltexStorageType
_EltexStorageDeviceType_Object=MibTableColumn
eltexStorageDeviceType=_EltexStorageDeviceType_Object((1,3,6,1,4,1,35265,39,1,1,1,1,3),_EltexStorageDeviceType_Type())
eltexStorageDeviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexStorageDeviceType.setStatus(_A)
_EltexStorageDeviceSize_Type=Gauge32
_EltexStorageDeviceSize_Object=MibTableColumn
eltexStorageDeviceSize=_EltexStorageDeviceSize_Object((1,3,6,1,4,1,35265,39,1,1,1,1,4),_EltexStorageDeviceSize_Type())
eltexStorageDeviceSize.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexStorageDeviceSize.setStatus(_A)
if mibBuilder.loadTexts:eltexStorageDeviceSize.setUnits(_D)
_EltexStorageDeviceSizeOverflow_Type=Gauge32
_EltexStorageDeviceSizeOverflow_Object=MibTableColumn
eltexStorageDeviceSizeOverflow=_EltexStorageDeviceSizeOverflow_Object((1,3,6,1,4,1,35265,39,1,1,1,1,5),_EltexStorageDeviceSizeOverflow_Type())
eltexStorageDeviceSizeOverflow.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexStorageDeviceSizeOverflow.setStatus(_A)
if mibBuilder.loadTexts:eltexStorageDeviceSizeOverflow.setUnits(_D)
_EltexStorageDeviceHCSize_Type=Counter64
_EltexStorageDeviceHCSize_Object=MibTableColumn
eltexStorageDeviceHCSize=_EltexStorageDeviceHCSize_Object((1,3,6,1,4,1,35265,39,1,1,1,1,6),_EltexStorageDeviceHCSize_Type())
eltexStorageDeviceHCSize.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexStorageDeviceHCSize.setStatus(_A)
if mibBuilder.loadTexts:eltexStorageDeviceHCSize.setUnits(_D)
_EltexStorageDeviceRemovable_Type=TruthValue
_EltexStorageDeviceRemovable_Object=MibTableColumn
eltexStorageDeviceRemovable=_EltexStorageDeviceRemovable_Object((1,3,6,1,4,1,35265,39,1,1,1,1,7),_EltexStorageDeviceRemovable_Type())
eltexStorageDeviceRemovable.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexStorageDeviceRemovable.setStatus(_A)
_EltexStoragePartitionTable_Object=MibTable
eltexStoragePartitionTable=_EltexStoragePartitionTable_Object((1,3,6,1,4,1,35265,39,1,1,2))
if mibBuilder.loadTexts:eltexStoragePartitionTable.setStatus(_A)
_EltexStoragePartitionEntry_Object=MibTableRow
eltexStoragePartitionEntry=_EltexStoragePartitionEntry_Object((1,3,6,1,4,1,35265,39,1,1,2,1))
eltexStoragePartitionEntry.setIndexNames((0,_B,_G),(0,_B,_I))
if mibBuilder.loadTexts:eltexStoragePartitionEntry.setStatus(_A)
_EltexStoragePartitionIndex_Type=Gauge32
_EltexStoragePartitionIndex_Object=MibTableColumn
eltexStoragePartitionIndex=_EltexStoragePartitionIndex_Object((1,3,6,1,4,1,35265,39,1,1,2,1,1),_EltexStoragePartitionIndex_Type())
eltexStoragePartitionIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:eltexStoragePartitionIndex.setStatus(_A)
_EltexStoragePartitionTotal_Type=Gauge32
_EltexStoragePartitionTotal_Object=MibTableColumn
eltexStoragePartitionTotal=_EltexStoragePartitionTotal_Object((1,3,6,1,4,1,35265,39,1,1,2,1,2),_EltexStoragePartitionTotal_Type())
eltexStoragePartitionTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexStoragePartitionTotal.setStatus(_A)
if mibBuilder.loadTexts:eltexStoragePartitionTotal.setUnits(_D)
_EltexStoragePartitionTotalOverflow_Type=Gauge32
_EltexStoragePartitionTotalOverflow_Object=MibTableColumn
eltexStoragePartitionTotalOverflow=_EltexStoragePartitionTotalOverflow_Object((1,3,6,1,4,1,35265,39,1,1,2,1,3),_EltexStoragePartitionTotalOverflow_Type())
eltexStoragePartitionTotalOverflow.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexStoragePartitionTotalOverflow.setStatus(_A)
if mibBuilder.loadTexts:eltexStoragePartitionTotalOverflow.setUnits(_D)
_EltexStoragePartitionHCTotal_Type=Counter64
_EltexStoragePartitionHCTotal_Object=MibTableColumn
eltexStoragePartitionHCTotal=_EltexStoragePartitionHCTotal_Object((1,3,6,1,4,1,35265,39,1,1,2,1,4),_EltexStoragePartitionHCTotal_Type())
eltexStoragePartitionHCTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexStoragePartitionHCTotal.setStatus(_A)
if mibBuilder.loadTexts:eltexStoragePartitionHCTotal.setUnits(_D)
_EltexStoragePartitionFreePercent_Type=EltexPercent
_EltexStoragePartitionFreePercent_Object=MibTableColumn
eltexStoragePartitionFreePercent=_EltexStoragePartitionFreePercent_Object((1,3,6,1,4,1,35265,39,1,1,2,1,5),_EltexStoragePartitionFreePercent_Type())
eltexStoragePartitionFreePercent.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexStoragePartitionFreePercent.setStatus(_A)
_EltexStoragePartitionFree_Type=Gauge32
_EltexStoragePartitionFree_Object=MibTableColumn
eltexStoragePartitionFree=_EltexStoragePartitionFree_Object((1,3,6,1,4,1,35265,39,1,1,2,1,6),_EltexStoragePartitionFree_Type())
eltexStoragePartitionFree.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexStoragePartitionFree.setStatus(_A)
if mibBuilder.loadTexts:eltexStoragePartitionFree.setUnits(_D)
_EltexStoragePartitionFreeOverflow_Type=Gauge32
_EltexStoragePartitionFreeOverflow_Object=MibTableColumn
eltexStoragePartitionFreeOverflow=_EltexStoragePartitionFreeOverflow_Object((1,3,6,1,4,1,35265,39,1,1,2,1,7),_EltexStoragePartitionFreeOverflow_Type())
eltexStoragePartitionFreeOverflow.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexStoragePartitionFreeOverflow.setStatus(_A)
if mibBuilder.loadTexts:eltexStoragePartitionFreeOverflow.setUnits(_D)
_EltexStoragePartitionHCFree_Type=Counter64
_EltexStoragePartitionHCFree_Object=MibTableColumn
eltexStoragePartitionHCFree=_EltexStoragePartitionHCFree_Object((1,3,6,1,4,1,35265,39,1,1,2,1,8),_EltexStoragePartitionHCFree_Type())
eltexStoragePartitionHCFree.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexStoragePartitionHCFree.setStatus(_A)
if mibBuilder.loadTexts:eltexStoragePartitionHCFree.setUnits(_D)
_EltexStoragePartitionThresholdFreeIndex_Type=Unsigned32
_EltexStoragePartitionThresholdFreeIndex_Object=MibTableColumn
eltexStoragePartitionThresholdFreeIndex=_EltexStoragePartitionThresholdFreeIndex_Object((1,3,6,1,4,1,35265,39,1,1,2,1,9),_EltexStoragePartitionThresholdFreeIndex_Type())
eltexStoragePartitionThresholdFreeIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexStoragePartitionThresholdFreeIndex.setStatus(_A)
_EltexStorageThreshold_ObjectIdentity=ObjectIdentity
eltexStorageThreshold=_EltexStorageThreshold_ObjectIdentity((1,3,6,1,4,1,35265,39,1,2))
class _EltexStorageThresholdNotificationGlobalEnable_Type(TruthValue):defaultValue=2
_EltexStorageThresholdNotificationGlobalEnable_Type.__name__=_F
_EltexStorageThresholdNotificationGlobalEnable_Object=MibScalar
eltexStorageThresholdNotificationGlobalEnable=_EltexStorageThresholdNotificationGlobalEnable_Object((1,3,6,1,4,1,35265,39,1,2,1),_EltexStorageThresholdNotificationGlobalEnable_Type())
eltexStorageThresholdNotificationGlobalEnable.setMaxAccess(_P)
if mibBuilder.loadTexts:eltexStorageThresholdNotificationGlobalEnable.setStatus(_A)
class _EltexStorageThresholdRecoveryNotificationGlobalEnable_Type(TruthValue):defaultValue=2
_EltexStorageThresholdRecoveryNotificationGlobalEnable_Type.__name__=_F
_EltexStorageThresholdRecoveryNotificationGlobalEnable_Object=MibScalar
eltexStorageThresholdRecoveryNotificationGlobalEnable=_EltexStorageThresholdRecoveryNotificationGlobalEnable_Object((1,3,6,1,4,1,35265,39,1,2,2),_EltexStorageThresholdRecoveryNotificationGlobalEnable_Type())
eltexStorageThresholdRecoveryNotificationGlobalEnable.setMaxAccess(_P)
if mibBuilder.loadTexts:eltexStorageThresholdRecoveryNotificationGlobalEnable.setStatus(_A)
_EltexStorageThresholdTable_Object=MibTable
eltexStorageThresholdTable=_EltexStorageThresholdTable_Object((1,3,6,1,4,1,35265,39,1,2,3))
if mibBuilder.loadTexts:eltexStorageThresholdTable.setStatus(_A)
_EltexStorageThresholdEntry_Object=MibTableRow
eltexStorageThresholdEntry=_EltexStorageThresholdEntry_Object((1,3,6,1,4,1,35265,39,1,2,3,1))
eltexStorageThresholdEntry.setIndexNames((0,_B,_G),(0,_B,_I),(0,_B,_Q))
if mibBuilder.loadTexts:eltexStorageThresholdEntry.setStatus(_A)
_EltexStorageThresholdIndex_Type=Unsigned32
_EltexStorageThresholdIndex_Object=MibTableColumn
eltexStorageThresholdIndex=_EltexStorageThresholdIndex_Object((1,3,6,1,4,1,35265,39,1,2,3,1,1),_EltexStorageThresholdIndex_Type())
eltexStorageThresholdIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:eltexStorageThresholdIndex.setStatus(_A)
_EltexStorageThresholdRowStatus_Type=RowStatus
_EltexStorageThresholdRowStatus_Object=MibTableColumn
eltexStorageThresholdRowStatus=_EltexStorageThresholdRowStatus_Object((1,3,6,1,4,1,35265,39,1,2,3,1,2),_EltexStorageThresholdRowStatus_Type())
eltexStorageThresholdRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:eltexStorageThresholdRowStatus.setStatus(_A)
_EltexStorageThresholdValue_Type=EltexPercent
_EltexStorageThresholdValue_Object=MibTableColumn
eltexStorageThresholdValue=_EltexStorageThresholdValue_Object((1,3,6,1,4,1,35265,39,1,2,3,1,3),_EltexStorageThresholdValue_Type())
eltexStorageThresholdValue.setMaxAccess(_E)
if mibBuilder.loadTexts:eltexStorageThresholdValue.setStatus(_A)
class _EltexStorageThresholdFlappingInterval_Type(EltexPercent):defaultValue=0
_EltexStorageThresholdFlappingInterval_Type.__name__=_N
_EltexStorageThresholdFlappingInterval_Object=MibTableColumn
eltexStorageThresholdFlappingInterval=_EltexStorageThresholdFlappingInterval_Object((1,3,6,1,4,1,35265,39,1,2,3,1,4),_EltexStorageThresholdFlappingInterval_Type())
eltexStorageThresholdFlappingInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:eltexStorageThresholdFlappingInterval.setStatus(_A)
class _EltexStorageThresholdSeverity_Type(SyslogSeverity):defaultValue=1
_EltexStorageThresholdSeverity_Type.__name__=_O
_EltexStorageThresholdSeverity_Object=MibTableColumn
eltexStorageThresholdSeverity=_EltexStorageThresholdSeverity_Object((1,3,6,1,4,1,35265,39,1,2,3,1,5),_EltexStorageThresholdSeverity_Type())
eltexStorageThresholdSeverity.setMaxAccess(_E)
if mibBuilder.loadTexts:eltexStorageThresholdSeverity.setStatus(_A)
_EltexStorageThresholdRelation_Type=EltexThresholdRelation
_EltexStorageThresholdRelation_Object=MibTableColumn
eltexStorageThresholdRelation=_EltexStorageThresholdRelation_Object((1,3,6,1,4,1,35265,39,1,2,3,1,6),_EltexStorageThresholdRelation_Type())
eltexStorageThresholdRelation.setMaxAccess(_E)
if mibBuilder.loadTexts:eltexStorageThresholdRelation.setStatus(_A)
class _EltexStorageThresholdNotificationEnable_Type(TruthValue):defaultValue=1
_EltexStorageThresholdNotificationEnable_Type.__name__=_F
_EltexStorageThresholdNotificationEnable_Object=MibTableColumn
eltexStorageThresholdNotificationEnable=_EltexStorageThresholdNotificationEnable_Object((1,3,6,1,4,1,35265,39,1,2,3,1,7),_EltexStorageThresholdNotificationEnable_Type())
eltexStorageThresholdNotificationEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:eltexStorageThresholdNotificationEnable.setStatus(_A)
class _EltexStorageThresholdRecoveryNotificationEnable_Type(TruthValue):defaultValue=1
_EltexStorageThresholdRecoveryNotificationEnable_Type.__name__=_F
_EltexStorageThresholdRecoveryNotificationEnable_Object=MibTableColumn
eltexStorageThresholdRecoveryNotificationEnable=_EltexStorageThresholdRecoveryNotificationEnable_Object((1,3,6,1,4,1,35265,39,1,2,3,1,8),_EltexStorageThresholdRecoveryNotificationEnable_Type())
eltexStorageThresholdRecoveryNotificationEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:eltexStorageThresholdRecoveryNotificationEnable.setStatus(_A)
_EltexStorageThresholdEvaluation_Type=TruthValue
_EltexStorageThresholdEvaluation_Object=MibTableColumn
eltexStorageThresholdEvaluation=_EltexStorageThresholdEvaluation_Object((1,3,6,1,4,1,35265,39,1,2,3,1,9),_EltexStorageThresholdEvaluation_Type())
eltexStorageThresholdEvaluation.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexStorageThresholdEvaluation.setStatus(_A)
_EltexStorageMIBNotification_ObjectIdentity=ObjectIdentity
eltexStorageMIBNotification=_EltexStorageMIBNotification_ObjectIdentity((1,3,6,1,4,1,35265,39,2))
_EltexStorageMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
eltexStorageMIBNotificationPrefix=_EltexStorageMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,35265,39,2,0))
eltexStorageFreeMemoryThresholdNotification=NotificationType((1,3,6,1,4,1,35265,39,2,0,1))
eltexStorageFreeMemoryThresholdNotification.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:eltexStorageFreeMemoryThresholdNotification.setStatus(_A)
eltexStorageFreeMemoryThresholdRecoveryNotification=NotificationType((1,3,6,1,4,1,35265,39,2,0,2))
eltexStorageFreeMemoryThresholdRecoveryNotification.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:eltexStorageFreeMemoryThresholdRecoveryNotification.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'EltexStorageType':EltexStorageType,'eltexStorageMIB':eltexStorageMIB,'eltexStorageMIBObjects':eltexStorageMIBObjects,'eltexStorageDevice':eltexStorageDevice,'eltexStorageDeviceTable':eltexStorageDeviceTable,'eltexStorageDeviceEntry':eltexStorageDeviceEntry,_G:eltexStorageDeviceIndex,'eltexStorageDevicePhysicalIndex':eltexStorageDevicePhysicalIndex,'eltexStorageDeviceType':eltexStorageDeviceType,'eltexStorageDeviceSize':eltexStorageDeviceSize,'eltexStorageDeviceSizeOverflow':eltexStorageDeviceSizeOverflow,'eltexStorageDeviceHCSize':eltexStorageDeviceHCSize,'eltexStorageDeviceRemovable':eltexStorageDeviceRemovable,'eltexStoragePartitionTable':eltexStoragePartitionTable,'eltexStoragePartitionEntry':eltexStoragePartitionEntry,_I:eltexStoragePartitionIndex,'eltexStoragePartitionTotal':eltexStoragePartitionTotal,'eltexStoragePartitionTotalOverflow':eltexStoragePartitionTotalOverflow,'eltexStoragePartitionHCTotal':eltexStoragePartitionHCTotal,_J:eltexStoragePartitionFreePercent,'eltexStoragePartitionFree':eltexStoragePartitionFree,'eltexStoragePartitionFreeOverflow':eltexStoragePartitionFreeOverflow,'eltexStoragePartitionHCFree':eltexStoragePartitionHCFree,'eltexStoragePartitionThresholdFreeIndex':eltexStoragePartitionThresholdFreeIndex,'eltexStorageThreshold':eltexStorageThreshold,'eltexStorageThresholdNotificationGlobalEnable':eltexStorageThresholdNotificationGlobalEnable,'eltexStorageThresholdRecoveryNotificationGlobalEnable':eltexStorageThresholdRecoveryNotificationGlobalEnable,'eltexStorageThresholdTable':eltexStorageThresholdTable,'eltexStorageThresholdEntry':eltexStorageThresholdEntry,_Q:eltexStorageThresholdIndex,'eltexStorageThresholdRowStatus':eltexStorageThresholdRowStatus,_M:eltexStorageThresholdValue,'eltexStorageThresholdFlappingInterval':eltexStorageThresholdFlappingInterval,_K:eltexStorageThresholdSeverity,_L:eltexStorageThresholdRelation,'eltexStorageThresholdNotificationEnable':eltexStorageThresholdNotificationEnable,'eltexStorageThresholdRecoveryNotificationEnable':eltexStorageThresholdRecoveryNotificationEnable,'eltexStorageThresholdEvaluation':eltexStorageThresholdEvaluation,'eltexStorageMIBNotification':eltexStorageMIBNotification,'eltexStorageMIBNotificationPrefix':eltexStorageMIBNotificationPrefix,'eltexStorageFreeMemoryThresholdNotification':eltexStorageFreeMemoryThresholdNotification,'eltexStorageFreeMemoryThresholdRecoveryNotification':eltexStorageFreeMemoryThresholdRecoveryNotification})