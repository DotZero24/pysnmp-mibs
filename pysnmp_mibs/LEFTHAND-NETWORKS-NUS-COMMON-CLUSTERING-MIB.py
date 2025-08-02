_X='seconds'
_W='clusSnapshotScheduleIndex'
_V='clusUnicastHostIndex'
_U='clusVolumeSnapshotACLIndex'
_T='remote'
_S='primary'
_R='clusClusterVolumeIndex'
_Q='clusVolumeACLIndex'
_P='faulty'
_O='clusClusterModuleIndex'
_N='clusModuleIndex'
_M='clusManagerIndex'
_L='clusAuthGroupIndex'
_K='clusVolumeSnapshotIndex'
_J='normal'
_I='clusClusterIndex'
_H='clusVolumeIndex'
_G='kbytes'
_F='Integer32'
_E='LEFTHAND-NETWORKS-NUS-COMMON-CLUSTERING-MIB'
_D='read-write'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lhnModules,=mibBuilder.importSymbols('LEFTHAND-NETWORKS-GLOBAL-REG','lhnModules')
lhnNusCommonClustering,=mibBuilder.importSymbols('LEFTHAND-NETWORKS-NUS-COMMON-MIB','lhnNusCommonClustering')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
lhnNusCommonClusteringModule=ModuleIdentity((1,3,6,1,4,1,9804,1,1,14))
class ClusPermissionBits(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('read',0),('write',1),('exclusive',2)))
_ClusMgmtGroupName_Type=OctetString
_ClusMgmtGroupName_Object=MibScalar
clusMgmtGroupName=_ClusMgmtGroupName_Object((1,3,6,1,4,1,9804,3,1,1,2,12,1),_ClusMgmtGroupName_Type())
clusMgmtGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:clusMgmtGroupName.setStatus(_A)
_ClusMgmtGroupIsEnabled_Type=TruthValue
_ClusMgmtGroupIsEnabled_Object=MibScalar
clusMgmtGroupIsEnabled=_ClusMgmtGroupIsEnabled_Object((1,3,6,1,4,1,9804,3,1,1,2,12,2),_ClusMgmtGroupIsEnabled_Type())
clusMgmtGroupIsEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:clusMgmtGroupIsEnabled.setStatus(_A)
_ClusMgmtGroupQuorum_Type=Integer32
_ClusMgmtGroupQuorum_Object=MibScalar
clusMgmtGroupQuorum=_ClusMgmtGroupQuorum_Object((1,3,6,1,4,1,9804,3,1,1,2,12,3),_ClusMgmtGroupQuorum_Type())
clusMgmtGroupQuorum.setMaxAccess(_D)
if mibBuilder.loadTexts:clusMgmtGroupQuorum.setStatus(_A)
_ClusMgmtGroupDescription_Type=OctetString
_ClusMgmtGroupDescription_Object=MibScalar
clusMgmtGroupDescription=_ClusMgmtGroupDescription_Object((1,3,6,1,4,1,9804,3,1,1,2,12,4),_ClusMgmtGroupDescription_Type())
clusMgmtGroupDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:clusMgmtGroupDescription.setStatus(_A)
_ClusMgmtGroupActiveManagerCount_Type=Integer32
_ClusMgmtGroupActiveManagerCount_Object=MibScalar
clusMgmtGroupActiveManagerCount=_ClusMgmtGroupActiveManagerCount_Object((1,3,6,1,4,1,9804,3,1,1,2,12,5),_ClusMgmtGroupActiveManagerCount_Type())
clusMgmtGroupActiveManagerCount.setMaxAccess(_B)
if mibBuilder.loadTexts:clusMgmtGroupActiveManagerCount.setStatus(_A)
_ClusMgmtGroupManagerCount_Type=Integer32
_ClusMgmtGroupManagerCount_Object=MibScalar
clusMgmtGroupManagerCount=_ClusMgmtGroupManagerCount_Object((1,3,6,1,4,1,9804,3,1,1,2,12,6),_ClusMgmtGroupManagerCount_Type())
clusMgmtGroupManagerCount.setMaxAccess(_B)
if mibBuilder.loadTexts:clusMgmtGroupManagerCount.setStatus(_A)
_ClusManagerTable_Object=MibTable
clusManagerTable=_ClusManagerTable_Object((1,3,6,1,4,1,9804,3,1,1,2,12,7))
if mibBuilder.loadTexts:clusManagerTable.setStatus(_A)
_ClusManagerEntry_Object=MibTableRow
clusManagerEntry=_ClusManagerEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,12,7,1))
clusManagerEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:clusManagerEntry.setStatus(_A)
_ClusManagerIndex_Type=Integer32
_ClusManagerIndex_Object=MibTableColumn
clusManagerIndex=_ClusManagerIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,12,7,1,1),_ClusManagerIndex_Type())
clusManagerIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:clusManagerIndex.setStatus(_A)
_ClusManagerName_Type=OctetString
_ClusManagerName_Object=MibTableColumn
clusManagerName=_ClusManagerName_Object((1,3,6,1,4,1,9804,3,1,1,2,12,7,1,2),_ClusManagerName_Type())
clusManagerName.setMaxAccess(_B)
if mibBuilder.loadTexts:clusManagerName.setStatus(_A)
_ClusManagerVersion_Type=OctetString
_ClusManagerVersion_Object=MibTableColumn
clusManagerVersion=_ClusManagerVersion_Object((1,3,6,1,4,1,9804,3,1,1,2,12,7,1,3),_ClusManagerVersion_Type())
clusManagerVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:clusManagerVersion.setStatus(_A)
_ClusManagerHostSerialNo_Type=OctetString
_ClusManagerHostSerialNo_Object=MibTableColumn
clusManagerHostSerialNo=_ClusManagerHostSerialNo_Object((1,3,6,1,4,1,9804,3,1,1,2,12,7,1,4),_ClusManagerHostSerialNo_Type())
clusManagerHostSerialNo.setMaxAccess(_D)
if mibBuilder.loadTexts:clusManagerHostSerialNo.setStatus(_A)
class _ClusManagerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_ClusManagerStatus_Type.__name__=_F
_ClusManagerStatus_Object=MibTableColumn
clusManagerStatus=_ClusManagerStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,12,7,1,5),_ClusManagerStatus_Type())
clusManagerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:clusManagerStatus.setStatus(_A)
_ClusManagerIsVirtual_Type=TruthValue
_ClusManagerIsVirtual_Object=MibTableColumn
clusManagerIsVirtual=_ClusManagerIsVirtual_Object((1,3,6,1,4,1,9804,3,1,1,2,12,7,1,7),_ClusManagerIsVirtual_Type())
clusManagerIsVirtual.setMaxAccess(_C)
if mibBuilder.loadTexts:clusManagerIsVirtual.setStatus(_A)
_ClusManagerRowStatus_Type=RowStatus
_ClusManagerRowStatus_Object=MibTableColumn
clusManagerRowStatus=_ClusManagerRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,12,7,1,8),_ClusManagerRowStatus_Type())
clusManagerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clusManagerRowStatus.setStatus(_A)
_ClusModuleCount_Type=Integer32
_ClusModuleCount_Object=MibScalar
clusModuleCount=_ClusModuleCount_Object((1,3,6,1,4,1,9804,3,1,1,2,12,8),_ClusModuleCount_Type())
clusModuleCount.setMaxAccess(_B)
if mibBuilder.loadTexts:clusModuleCount.setStatus(_A)
_ClusModuleTable_Object=MibTable
clusModuleTable=_ClusModuleTable_Object((1,3,6,1,4,1,9804,3,1,1,2,12,9))
if mibBuilder.loadTexts:clusModuleTable.setStatus(_A)
_ClusModuleEntry_Object=MibTableRow
clusModuleEntry=_ClusModuleEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,12,9,1))
clusModuleEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:clusModuleEntry.setStatus(_A)
_ClusModuleIndex_Type=Integer32
_ClusModuleIndex_Object=MibTableColumn
clusModuleIndex=_ClusModuleIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,12,9,1,1),_ClusModuleIndex_Type())
clusModuleIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:clusModuleIndex.setStatus(_A)
_ClusModuleName_Type=OctetString
_ClusModuleName_Object=MibTableColumn
clusModuleName=_ClusModuleName_Object((1,3,6,1,4,1,9804,3,1,1,2,12,9,1,2),_ClusModuleName_Type())
clusModuleName.setMaxAccess(_C)
if mibBuilder.loadTexts:clusModuleName.setStatus(_A)
_ClusModuleVersion_Type=OctetString
_ClusModuleVersion_Object=MibTableColumn
clusModuleVersion=_ClusModuleVersion_Object((1,3,6,1,4,1,9804,3,1,1,2,12,9,1,3),_ClusModuleVersion_Type())
clusModuleVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:clusModuleVersion.setStatus(_A)
_ClusModuleSerialNo_Type=OctetString
_ClusModuleSerialNo_Object=MibTableColumn
clusModuleSerialNo=_ClusModuleSerialNo_Object((1,3,6,1,4,1,9804,3,1,1,2,12,9,1,4),_ClusModuleSerialNo_Type())
clusModuleSerialNo.setMaxAccess(_C)
if mibBuilder.loadTexts:clusModuleSerialNo.setStatus(_A)
_ClusModuleTotalSize_Type=Counter64
_ClusModuleTotalSize_Object=MibTableColumn
clusModuleTotalSize=_ClusModuleTotalSize_Object((1,3,6,1,4,1,9804,3,1,1,2,12,9,1,5),_ClusModuleTotalSize_Type())
clusModuleTotalSize.setMaxAccess(_B)
if mibBuilder.loadTexts:clusModuleTotalSize.setStatus(_A)
if mibBuilder.loadTexts:clusModuleTotalSize.setUnits(_G)
_ClusModuleAvailSize_Type=Counter64
_ClusModuleAvailSize_Object=MibTableColumn
clusModuleAvailSize=_ClusModuleAvailSize_Object((1,3,6,1,4,1,9804,3,1,1,2,12,9,1,6),_ClusModuleAvailSize_Type())
clusModuleAvailSize.setMaxAccess(_B)
if mibBuilder.loadTexts:clusModuleAvailSize.setStatus(_A)
if mibBuilder.loadTexts:clusModuleAvailSize.setUnits(_G)
_ClusModuleIsManager_Type=TruthValue
_ClusModuleIsManager_Object=MibTableColumn
clusModuleIsManager=_ClusModuleIsManager_Object((1,3,6,1,4,1,9804,3,1,1,2,12,9,1,7),_ClusModuleIsManager_Type())
clusModuleIsManager.setMaxAccess(_C)
if mibBuilder.loadTexts:clusModuleIsManager.setStatus(_A)
_ClusModuleRaidConfiguration_Type=OctetString
_ClusModuleRaidConfiguration_Object=MibTableColumn
clusModuleRaidConfiguration=_ClusModuleRaidConfiguration_Object((1,3,6,1,4,1,9804,3,1,1,2,12,9,1,8),_ClusModuleRaidConfiguration_Type())
clusModuleRaidConfiguration.setMaxAccess(_B)
if mibBuilder.loadTexts:clusModuleRaidConfiguration.setStatus(_A)
_ClusModuleRaidStatus_Type=OctetString
_ClusModuleRaidStatus_Object=MibTableColumn
clusModuleRaidStatus=_ClusModuleRaidStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,12,9,1,9),_ClusModuleRaidStatus_Type())
clusModuleRaidStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:clusModuleRaidStatus.setStatus(_A)
class _ClusModuleStorageStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_ClusModuleStorageStatus_Type.__name__=_F
_ClusModuleStorageStatus_Object=MibTableColumn
clusModuleStorageStatus=_ClusModuleStorageStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,12,9,1,10),_ClusModuleStorageStatus_Type())
clusModuleStorageStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:clusModuleStorageStatus.setStatus(_A)
_ClusModuleStorageIsReady_Type=TruthValue
_ClusModuleStorageIsReady_Object=MibTableColumn
clusModuleStorageIsReady=_ClusModuleStorageIsReady_Object((1,3,6,1,4,1,9804,3,1,1,2,12,9,1,11),_ClusModuleStorageIsReady_Type())
clusModuleStorageIsReady.setMaxAccess(_B)
if mibBuilder.loadTexts:clusModuleStorageIsReady.setStatus(_A)
_ClusModuleCreationTime_Type=DateAndTime
_ClusModuleCreationTime_Object=MibTableColumn
clusModuleCreationTime=_ClusModuleCreationTime_Object((1,3,6,1,4,1,9804,3,1,1,2,12,9,1,12),_ClusModuleCreationTime_Type())
clusModuleCreationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:clusModuleCreationTime.setStatus(_A)
_ClusModuleDescription_Type=OctetString
_ClusModuleDescription_Object=MibTableColumn
clusModuleDescription=_ClusModuleDescription_Object((1,3,6,1,4,1,9804,3,1,1,2,12,9,1,13),_ClusModuleDescription_Type())
clusModuleDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:clusModuleDescription.setStatus(_A)
_ClusModuleClusterName_Type=OctetString
_ClusModuleClusterName_Object=MibTableColumn
clusModuleClusterName=_ClusModuleClusterName_Object((1,3,6,1,4,1,9804,3,1,1,2,12,9,1,14),_ClusModuleClusterName_Type())
clusModuleClusterName.setMaxAccess(_D)
if mibBuilder.loadTexts:clusModuleClusterName.setStatus(_A)
_ClusModuleRowStatus_Type=RowStatus
_ClusModuleRowStatus_Object=MibTableColumn
clusModuleRowStatus=_ClusModuleRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,12,9,1,15),_ClusModuleRowStatus_Type())
clusModuleRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clusModuleRowStatus.setStatus(_A)
_ClusClusterCount_Type=Integer32
_ClusClusterCount_Object=MibScalar
clusClusterCount=_ClusClusterCount_Object((1,3,6,1,4,1,9804,3,1,1,2,12,10),_ClusClusterCount_Type())
clusClusterCount.setMaxAccess(_B)
if mibBuilder.loadTexts:clusClusterCount.setStatus(_A)
_ClusClusterTable_Object=MibTable
clusClusterTable=_ClusClusterTable_Object((1,3,6,1,4,1,9804,3,1,1,2,12,11))
if mibBuilder.loadTexts:clusClusterTable.setStatus(_A)
_ClusClusterEntry_Object=MibTableRow
clusClusterEntry=_ClusClusterEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,12,11,1))
clusClusterEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:clusClusterEntry.setStatus(_A)
_ClusClusterIndex_Type=Integer32
_ClusClusterIndex_Object=MibTableColumn
clusClusterIndex=_ClusClusterIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,12,11,1,1),_ClusClusterIndex_Type())
clusClusterIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:clusClusterIndex.setStatus(_A)
_ClusClusterName_Type=OctetString
_ClusClusterName_Object=MibTableColumn
clusClusterName=_ClusClusterName_Object((1,3,6,1,4,1,9804,3,1,1,2,12,11,1,2),_ClusClusterName_Type())
clusClusterName.setMaxAccess(_D)
if mibBuilder.loadTexts:clusClusterName.setStatus(_A)
_ClusClusterModuleCount_Type=Counter32
_ClusClusterModuleCount_Object=MibTableColumn
clusClusterModuleCount=_ClusClusterModuleCount_Object((1,3,6,1,4,1,9804,3,1,1,2,12,11,1,3),_ClusClusterModuleCount_Type())
clusClusterModuleCount.setMaxAccess(_B)
if mibBuilder.loadTexts:clusClusterModuleCount.setStatus(_A)
_ClusClusterVolumeCount_Type=Counter32
_ClusClusterVolumeCount_Object=MibTableColumn
clusClusterVolumeCount=_ClusClusterVolumeCount_Object((1,3,6,1,4,1,9804,3,1,1,2,12,11,1,4),_ClusClusterVolumeCount_Type())
clusClusterVolumeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:clusClusterVolumeCount.setStatus(_A)
_ClusClusterDescription_Type=OctetString
_ClusClusterDescription_Object=MibTableColumn
clusClusterDescription=_ClusClusterDescription_Object((1,3,6,1,4,1,9804,3,1,1,2,12,11,1,5),_ClusClusterDescription_Type())
clusClusterDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:clusClusterDescription.setStatus(_A)
_ClusClusterRowStatus_Type=RowStatus
_ClusClusterRowStatus_Object=MibTableColumn
clusClusterRowStatus=_ClusClusterRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,12,11,1,6),_ClusClusterRowStatus_Type())
clusClusterRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clusClusterRowStatus.setStatus(_A)
_ClusClusterModuleTable_Object=MibTable
clusClusterModuleTable=_ClusClusterModuleTable_Object((1,3,6,1,4,1,9804,3,1,1,2,12,12))
if mibBuilder.loadTexts:clusClusterModuleTable.setStatus(_A)
_ClusClusterModuleEntry_Object=MibTableRow
clusClusterModuleEntry=_ClusClusterModuleEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,12,12,1))
clusClusterModuleEntry.setIndexNames((0,_E,_I),(0,_E,_O))
if mibBuilder.loadTexts:clusClusterModuleEntry.setStatus(_A)
_ClusClusterModuleIndex_Type=Integer32
_ClusClusterModuleIndex_Object=MibTableColumn
clusClusterModuleIndex=_ClusClusterModuleIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,12,12,1,1),_ClusClusterModuleIndex_Type())
clusClusterModuleIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:clusClusterModuleIndex.setStatus(_A)
_ClusClusterModuleName_Type=OctetString
_ClusClusterModuleName_Object=MibTableColumn
clusClusterModuleName=_ClusClusterModuleName_Object((1,3,6,1,4,1,9804,3,1,1,2,12,12,1,2),_ClusClusterModuleName_Type())
clusClusterModuleName.setMaxAccess(_C)
if mibBuilder.loadTexts:clusClusterModuleName.setStatus(_A)
_ClusClusterModuleSerialNo_Type=OctetString
_ClusClusterModuleSerialNo_Object=MibTableColumn
clusClusterModuleSerialNo=_ClusClusterModuleSerialNo_Object((1,3,6,1,4,1,9804,3,1,1,2,12,12,1,3),_ClusClusterModuleSerialNo_Type())
clusClusterModuleSerialNo.setMaxAccess(_C)
if mibBuilder.loadTexts:clusClusterModuleSerialNo.setStatus(_A)
_ClusClusterModuleIsHotSpare_Type=TruthValue
_ClusClusterModuleIsHotSpare_Object=MibTableColumn
clusClusterModuleIsHotSpare=_ClusClusterModuleIsHotSpare_Object((1,3,6,1,4,1,9804,3,1,1,2,12,12,1,4),_ClusClusterModuleIsHotSpare_Type())
clusClusterModuleIsHotSpare.setMaxAccess(_C)
if mibBuilder.loadTexts:clusClusterModuleIsHotSpare.setStatus(_A)
_ClusClusterModuleRowStatus_Type=RowStatus
_ClusClusterModuleRowStatus_Object=MibTableColumn
clusClusterModuleRowStatus=_ClusClusterModuleRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,12,12,1,5),_ClusClusterModuleRowStatus_Type())
clusClusterModuleRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clusClusterModuleRowStatus.setStatus(_A)
_ClusVolumeCount_Type=Integer32
_ClusVolumeCount_Object=MibScalar
clusVolumeCount=_ClusVolumeCount_Object((1,3,6,1,4,1,9804,3,1,1,2,12,13),_ClusVolumeCount_Type())
clusVolumeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:clusVolumeCount.setStatus(_A)
_ClusVolumeTable_Object=MibTable
clusVolumeTable=_ClusVolumeTable_Object((1,3,6,1,4,1,9804,3,1,1,2,12,14))
if mibBuilder.loadTexts:clusVolumeTable.setStatus(_A)
_ClusVolumeEntry_Object=MibTableRow
clusVolumeEntry=_ClusVolumeEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,12,14,1))
clusVolumeEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:clusVolumeEntry.setStatus(_A)
_ClusVolumeIndex_Type=Integer32
_ClusVolumeIndex_Object=MibTableColumn
clusVolumeIndex=_ClusVolumeIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,12,14,1,1),_ClusVolumeIndex_Type())
clusVolumeIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:clusVolumeIndex.setStatus(_A)
_ClusVolumeName_Type=OctetString
_ClusVolumeName_Object=MibTableColumn
clusVolumeName=_ClusVolumeName_Object((1,3,6,1,4,1,9804,3,1,1,2,12,14,1,2),_ClusVolumeName_Type())
clusVolumeName.setMaxAccess(_D)
if mibBuilder.loadTexts:clusVolumeName.setStatus(_A)
_ClusVolumeCreationTime_Type=DateAndTime
_ClusVolumeCreationTime_Object=MibTableColumn
clusVolumeCreationTime=_ClusVolumeCreationTime_Object((1,3,6,1,4,1,9804,3,1,1,2,12,14,1,3),_ClusVolumeCreationTime_Type())
clusVolumeCreationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:clusVolumeCreationTime.setStatus(_A)
_ClusVolumeDescription_Type=OctetString
_ClusVolumeDescription_Object=MibTableColumn
clusVolumeDescription=_ClusVolumeDescription_Object((1,3,6,1,4,1,9804,3,1,1,2,12,14,1,4),_ClusVolumeDescription_Type())
clusVolumeDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:clusVolumeDescription.setStatus(_A)
_ClusVolumeSize_Type=Counter64
_ClusVolumeSize_Object=MibTableColumn
clusVolumeSize=_ClusVolumeSize_Object((1,3,6,1,4,1,9804,3,1,1,2,12,14,1,5),_ClusVolumeSize_Type())
clusVolumeSize.setMaxAccess(_D)
if mibBuilder.loadTexts:clusVolumeSize.setStatus(_A)
if mibBuilder.loadTexts:clusVolumeSize.setUnits(_G)
_ClusVolumeSoftThreshold_Type=Counter64
_ClusVolumeSoftThreshold_Object=MibTableColumn
clusVolumeSoftThreshold=_ClusVolumeSoftThreshold_Object((1,3,6,1,4,1,9804,3,1,1,2,12,14,1,6),_ClusVolumeSoftThreshold_Type())
clusVolumeSoftThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:clusVolumeSoftThreshold.setStatus(_A)
if mibBuilder.loadTexts:clusVolumeSoftThreshold.setUnits(_G)
_ClusVolumeHardThreshold_Type=Counter64
_ClusVolumeHardThreshold_Object=MibTableColumn
clusVolumeHardThreshold=_ClusVolumeHardThreshold_Object((1,3,6,1,4,1,9804,3,1,1,2,12,14,1,7),_ClusVolumeHardThreshold_Type())
clusVolumeHardThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:clusVolumeHardThreshold.setStatus(_A)
if mibBuilder.loadTexts:clusVolumeHardThreshold.setUnits(_G)
_ClusVolumeReplicaCount_Type=Counter32
_ClusVolumeReplicaCount_Object=MibTableColumn
clusVolumeReplicaCount=_ClusVolumeReplicaCount_Object((1,3,6,1,4,1,9804,3,1,1,2,12,14,1,8),_ClusVolumeReplicaCount_Type())
clusVolumeReplicaCount.setMaxAccess(_D)
if mibBuilder.loadTexts:clusVolumeReplicaCount.setStatus(_A)
_ClusVolumeSnapshotCount_Type=Counter32
_ClusVolumeSnapshotCount_Object=MibTableColumn
clusVolumeSnapshotCount=_ClusVolumeSnapshotCount_Object((1,3,6,1,4,1,9804,3,1,1,2,12,14,1,9),_ClusVolumeSnapshotCount_Type())
clusVolumeSnapshotCount.setMaxAccess(_B)
if mibBuilder.loadTexts:clusVolumeSnapshotCount.setStatus(_A)
_ClusVolumeACLCount_Type=Counter32
_ClusVolumeACLCount_Object=MibTableColumn
clusVolumeACLCount=_ClusVolumeACLCount_Object((1,3,6,1,4,1,9804,3,1,1,2,12,14,1,10),_ClusVolumeACLCount_Type())
clusVolumeACLCount.setMaxAccess(_B)
if mibBuilder.loadTexts:clusVolumeACLCount.setStatus(_A)
_ClusVolumeClusterName_Type=OctetString
_ClusVolumeClusterName_Object=MibTableColumn
clusVolumeClusterName=_ClusVolumeClusterName_Object((1,3,6,1,4,1,9804,3,1,1,2,12,14,1,11),_ClusVolumeClusterName_Type())
clusVolumeClusterName.setMaxAccess(_D)
if mibBuilder.loadTexts:clusVolumeClusterName.setStatus(_A)
_ClusVolumeIsSoftThresholdExceeded_Type=TruthValue
_ClusVolumeIsSoftThresholdExceeded_Object=MibTableColumn
clusVolumeIsSoftThresholdExceeded=_ClusVolumeIsSoftThresholdExceeded_Object((1,3,6,1,4,1,9804,3,1,1,2,12,14,1,13),_ClusVolumeIsSoftThresholdExceeded_Type())
clusVolumeIsSoftThresholdExceeded.setMaxAccess(_B)
if mibBuilder.loadTexts:clusVolumeIsSoftThresholdExceeded.setStatus(_A)
_ClusVolumeIsHardThresholdExceeded_Type=TruthValue
_ClusVolumeIsHardThresholdExceeded_Object=MibTableColumn
clusVolumeIsHardThresholdExceeded=_ClusVolumeIsHardThresholdExceeded_Object((1,3,6,1,4,1,9804,3,1,1,2,12,14,1,14),_ClusVolumeIsHardThresholdExceeded_Type())
clusVolumeIsHardThresholdExceeded.setMaxAccess(_B)
if mibBuilder.loadTexts:clusVolumeIsHardThresholdExceeded.setStatus(_A)
class _ClusVolumeReplicationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_P,2)))
_ClusVolumeReplicationStatus_Type.__name__=_F
_ClusVolumeReplicationStatus_Object=MibTableColumn
clusVolumeReplicationStatus=_ClusVolumeReplicationStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,12,14,1,15),_ClusVolumeReplicationStatus_Type())
clusVolumeReplicationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:clusVolumeReplicationStatus.setStatus(_A)
_ClusVolumeIsRemoteIPCopy_Type=TruthValue
_ClusVolumeIsRemoteIPCopy_Object=MibTableColumn
clusVolumeIsRemoteIPCopy=_ClusVolumeIsRemoteIPCopy_Object((1,3,6,1,4,1,9804,3,1,1,2,12,14,1,16),_ClusVolumeIsRemoteIPCopy_Type())
clusVolumeIsRemoteIPCopy.setMaxAccess(_B)
if mibBuilder.loadTexts:clusVolumeIsRemoteIPCopy.setStatus(_A)
_ClusVolumeRemoteIPCopyFailureMessage_Type=OctetString
_ClusVolumeRemoteIPCopyFailureMessage_Object=MibTableColumn
clusVolumeRemoteIPCopyFailureMessage=_ClusVolumeRemoteIPCopyFailureMessage_Object((1,3,6,1,4,1,9804,3,1,1,2,12,14,1,17),_ClusVolumeRemoteIPCopyFailureMessage_Type())
clusVolumeRemoteIPCopyFailureMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:clusVolumeRemoteIPCopyFailureMessage.setStatus(_A)
_ClusVolumeRowStatus_Type=RowStatus
_ClusVolumeRowStatus_Object=MibTableColumn
clusVolumeRowStatus=_ClusVolumeRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,12,14,1,18),_ClusVolumeRowStatus_Type())
clusVolumeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clusVolumeRowStatus.setStatus(_A)
_ClusVolumeACLTable_Object=MibTable
clusVolumeACLTable=_ClusVolumeACLTable_Object((1,3,6,1,4,1,9804,3,1,1,2,12,15))
if mibBuilder.loadTexts:clusVolumeACLTable.setStatus(_A)
_ClusVolumeACLEntry_Object=MibTableRow
clusVolumeACLEntry=_ClusVolumeACLEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,12,15,1))
clusVolumeACLEntry.setIndexNames((0,_E,_H),(0,_E,_Q))
if mibBuilder.loadTexts:clusVolumeACLEntry.setStatus(_A)
_ClusVolumeACLIndex_Type=Integer32
_ClusVolumeACLIndex_Object=MibTableColumn
clusVolumeACLIndex=_ClusVolumeACLIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,12,15,1,1),_ClusVolumeACLIndex_Type())
clusVolumeACLIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:clusVolumeACLIndex.setStatus(_A)
_ClusVolumeACLAuthGroup_Type=OctetString
_ClusVolumeACLAuthGroup_Object=MibTableColumn
clusVolumeACLAuthGroup=_ClusVolumeACLAuthGroup_Object((1,3,6,1,4,1,9804,3,1,1,2,12,15,1,2),_ClusVolumeACLAuthGroup_Type())
clusVolumeACLAuthGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:clusVolumeACLAuthGroup.setStatus(_A)
_ClusVolumeACLPermissions_Type=ClusPermissionBits
_ClusVolumeACLPermissions_Object=MibTableColumn
clusVolumeACLPermissions=_ClusVolumeACLPermissions_Object((1,3,6,1,4,1,9804,3,1,1,2,12,15,1,3),_ClusVolumeACLPermissions_Type())
clusVolumeACLPermissions.setMaxAccess(_D)
if mibBuilder.loadTexts:clusVolumeACLPermissions.setStatus(_A)
_ClusVolumeACLRowStatus_Type=RowStatus
_ClusVolumeACLRowStatus_Object=MibTableColumn
clusVolumeACLRowStatus=_ClusVolumeACLRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,12,15,1,4),_ClusVolumeACLRowStatus_Type())
clusVolumeACLRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clusVolumeACLRowStatus.setStatus(_A)
_ClusClusterVolumeTable_Object=MibTable
clusClusterVolumeTable=_ClusClusterVolumeTable_Object((1,3,6,1,4,1,9804,3,1,1,2,12,16))
if mibBuilder.loadTexts:clusClusterVolumeTable.setStatus(_A)
_ClusClusterVolumeEntry_Object=MibTableRow
clusClusterVolumeEntry=_ClusClusterVolumeEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,12,16,1))
clusClusterVolumeEntry.setIndexNames((0,_E,_I),(0,_E,_R))
if mibBuilder.loadTexts:clusClusterVolumeEntry.setStatus(_A)
_ClusClusterVolumeIndex_Type=Integer32
_ClusClusterVolumeIndex_Object=MibTableColumn
clusClusterVolumeIndex=_ClusClusterVolumeIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,12,16,1,1),_ClusClusterVolumeIndex_Type())
clusClusterVolumeIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:clusClusterVolumeIndex.setStatus(_A)
_ClusClusterVolumeName_Type=OctetString
_ClusClusterVolumeName_Object=MibTableColumn
clusClusterVolumeName=_ClusClusterVolumeName_Object((1,3,6,1,4,1,9804,3,1,1,2,12,16,1,2),_ClusClusterVolumeName_Type())
clusClusterVolumeName.setMaxAccess(_C)
if mibBuilder.loadTexts:clusClusterVolumeName.setStatus(_A)
_ClusClusterVolumeRowStatus_Type=RowStatus
_ClusClusterVolumeRowStatus_Object=MibTableColumn
clusClusterVolumeRowStatus=_ClusClusterVolumeRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,12,16,1,3),_ClusClusterVolumeRowStatus_Type())
clusClusterVolumeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clusClusterVolumeRowStatus.setStatus(_A)
_ClusVolumeSnapshotTable_Object=MibTable
clusVolumeSnapshotTable=_ClusVolumeSnapshotTable_Object((1,3,6,1,4,1,9804,3,1,1,2,12,17))
if mibBuilder.loadTexts:clusVolumeSnapshotTable.setStatus(_A)
_ClusVolumeSnapshotEntry_Object=MibTableRow
clusVolumeSnapshotEntry=_ClusVolumeSnapshotEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,12,17,1))
clusVolumeSnapshotEntry.setIndexNames((0,_E,_H),(0,_E,_K))
if mibBuilder.loadTexts:clusVolumeSnapshotEntry.setStatus(_A)
_ClusVolumeSnapshotIndex_Type=Integer32
_ClusVolumeSnapshotIndex_Object=MibTableColumn
clusVolumeSnapshotIndex=_ClusVolumeSnapshotIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,12,17,1,1),_ClusVolumeSnapshotIndex_Type())
clusVolumeSnapshotIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:clusVolumeSnapshotIndex.setStatus(_A)
_ClusVolumeSnapshotName_Type=OctetString
_ClusVolumeSnapshotName_Object=MibTableColumn
clusVolumeSnapshotName=_ClusVolumeSnapshotName_Object((1,3,6,1,4,1,9804,3,1,1,2,12,17,1,2),_ClusVolumeSnapshotName_Type())
clusVolumeSnapshotName.setMaxAccess(_D)
if mibBuilder.loadTexts:clusVolumeSnapshotName.setStatus(_A)
_ClusVolumeSnapshotCreationTime_Type=DateAndTime
_ClusVolumeSnapshotCreationTime_Object=MibTableColumn
clusVolumeSnapshotCreationTime=_ClusVolumeSnapshotCreationTime_Object((1,3,6,1,4,1,9804,3,1,1,2,12,17,1,3),_ClusVolumeSnapshotCreationTime_Type())
clusVolumeSnapshotCreationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:clusVolumeSnapshotCreationTime.setStatus(_A)
_ClusVolumeSnapshotDescription_Type=OctetString
_ClusVolumeSnapshotDescription_Object=MibTableColumn
clusVolumeSnapshotDescription=_ClusVolumeSnapshotDescription_Object((1,3,6,1,4,1,9804,3,1,1,2,12,17,1,4),_ClusVolumeSnapshotDescription_Type())
clusVolumeSnapshotDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:clusVolumeSnapshotDescription.setStatus(_A)
_ClusVolumeSnapshotSize_Type=Counter64
_ClusVolumeSnapshotSize_Object=MibTableColumn
clusVolumeSnapshotSize=_ClusVolumeSnapshotSize_Object((1,3,6,1,4,1,9804,3,1,1,2,12,17,1,5),_ClusVolumeSnapshotSize_Type())
clusVolumeSnapshotSize.setMaxAccess(_B)
if mibBuilder.loadTexts:clusVolumeSnapshotSize.setStatus(_A)
if mibBuilder.loadTexts:clusVolumeSnapshotSize.setUnits(_G)
_ClusVolumeSnapshotSoftThreshold_Type=Counter64
_ClusVolumeSnapshotSoftThreshold_Object=MibTableColumn
clusVolumeSnapshotSoftThreshold=_ClusVolumeSnapshotSoftThreshold_Object((1,3,6,1,4,1,9804,3,1,1,2,12,17,1,6),_ClusVolumeSnapshotSoftThreshold_Type())
clusVolumeSnapshotSoftThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:clusVolumeSnapshotSoftThreshold.setStatus(_A)
if mibBuilder.loadTexts:clusVolumeSnapshotSoftThreshold.setUnits(_G)
_ClusVolumeSnapshotHardThreshold_Type=Counter64
_ClusVolumeSnapshotHardThreshold_Object=MibTableColumn
clusVolumeSnapshotHardThreshold=_ClusVolumeSnapshotHardThreshold_Object((1,3,6,1,4,1,9804,3,1,1,2,12,17,1,7),_ClusVolumeSnapshotHardThreshold_Type())
clusVolumeSnapshotHardThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:clusVolumeSnapshotHardThreshold.setStatus(_A)
if mibBuilder.loadTexts:clusVolumeSnapshotHardThreshold.setUnits(_G)
_ClusVolumeSnapshotACLCount_Type=Counter32
_ClusVolumeSnapshotACLCount_Object=MibTableColumn
clusVolumeSnapshotACLCount=_ClusVolumeSnapshotACLCount_Object((1,3,6,1,4,1,9804,3,1,1,2,12,17,1,8),_ClusVolumeSnapshotACLCount_Type())
clusVolumeSnapshotACLCount.setMaxAccess(_B)
if mibBuilder.loadTexts:clusVolumeSnapshotACLCount.setStatus(_A)
_ClusVolumeSnapshotScheduleName_Type=OctetString
_ClusVolumeSnapshotScheduleName_Object=MibTableColumn
clusVolumeSnapshotScheduleName=_ClusVolumeSnapshotScheduleName_Object((1,3,6,1,4,1,9804,3,1,1,2,12,17,1,10),_ClusVolumeSnapshotScheduleName_Type())
clusVolumeSnapshotScheduleName.setMaxAccess(_B)
if mibBuilder.loadTexts:clusVolumeSnapshotScheduleName.setStatus(_A)
_ClusVolumeSnapshotIsSoftThresholdExceeded_Type=TruthValue
_ClusVolumeSnapshotIsSoftThresholdExceeded_Object=MibTableColumn
clusVolumeSnapshotIsSoftThresholdExceeded=_ClusVolumeSnapshotIsSoftThresholdExceeded_Object((1,3,6,1,4,1,9804,3,1,1,2,12,17,1,12),_ClusVolumeSnapshotIsSoftThresholdExceeded_Type())
clusVolumeSnapshotIsSoftThresholdExceeded.setMaxAccess(_B)
if mibBuilder.loadTexts:clusVolumeSnapshotIsSoftThresholdExceeded.setStatus(_A)
_ClusVolumeSnapshotIsHardThresholdExceeded_Type=TruthValue
_ClusVolumeSnapshotIsHardThresholdExceeded_Object=MibTableColumn
clusVolumeSnapshotIsHardThresholdExceeded=_ClusVolumeSnapshotIsHardThresholdExceeded_Object((1,3,6,1,4,1,9804,3,1,1,2,12,17,1,13),_ClusVolumeSnapshotIsHardThresholdExceeded_Type())
clusVolumeSnapshotIsHardThresholdExceeded.setMaxAccess(_B)
if mibBuilder.loadTexts:clusVolumeSnapshotIsHardThresholdExceeded.setStatus(_A)
class _ClusVolumeSnapshotReplicationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_P,2)))
_ClusVolumeSnapshotReplicationStatus_Type.__name__=_F
_ClusVolumeSnapshotReplicationStatus_Object=MibTableColumn
clusVolumeSnapshotReplicationStatus=_ClusVolumeSnapshotReplicationStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,12,17,1,14),_ClusVolumeSnapshotReplicationStatus_Type())
clusVolumeSnapshotReplicationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:clusVolumeSnapshotReplicationStatus.setStatus(_A)
class _ClusVolumeSnapshotType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_ClusVolumeSnapshotType_Type.__name__=_F
_ClusVolumeSnapshotType_Object=MibTableColumn
clusVolumeSnapshotType=_ClusVolumeSnapshotType_Object((1,3,6,1,4,1,9804,3,1,1,2,12,17,1,15),_ClusVolumeSnapshotType_Type())
clusVolumeSnapshotType.setMaxAccess(_B)
if mibBuilder.loadTexts:clusVolumeSnapshotType.setStatus(_A)
class _ClusVolumeSnapshotCopyProgress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ClusVolumeSnapshotCopyProgress_Type.__name__=_F
_ClusVolumeSnapshotCopyProgress_Object=MibTableColumn
clusVolumeSnapshotCopyProgress=_ClusVolumeSnapshotCopyProgress_Object((1,3,6,1,4,1,9804,3,1,1,2,12,17,1,16),_ClusVolumeSnapshotCopyProgress_Type())
clusVolumeSnapshotCopyProgress.setMaxAccess(_B)
if mibBuilder.loadTexts:clusVolumeSnapshotCopyProgress.setStatus(_A)
if mibBuilder.loadTexts:clusVolumeSnapshotCopyProgress.setUnits('%')
_ClusVolumeSnapshotRowStatus_Type=RowStatus
_ClusVolumeSnapshotRowStatus_Object=MibTableColumn
clusVolumeSnapshotRowStatus=_ClusVolumeSnapshotRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,12,17,1,17),_ClusVolumeSnapshotRowStatus_Type())
clusVolumeSnapshotRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clusVolumeSnapshotRowStatus.setStatus(_A)
_ClusVolumeSnapshotACLTable_Object=MibTable
clusVolumeSnapshotACLTable=_ClusVolumeSnapshotACLTable_Object((1,3,6,1,4,1,9804,3,1,1,2,12,18))
if mibBuilder.loadTexts:clusVolumeSnapshotACLTable.setStatus(_A)
_ClusVolumeSnapshotACLEntry_Object=MibTableRow
clusVolumeSnapshotACLEntry=_ClusVolumeSnapshotACLEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,12,18,1))
clusVolumeSnapshotACLEntry.setIndexNames((0,_E,_H),(0,_E,_K),(0,_E,_U))
if mibBuilder.loadTexts:clusVolumeSnapshotACLEntry.setStatus(_A)
_ClusVolumeSnapshotACLIndex_Type=Integer32
_ClusVolumeSnapshotACLIndex_Object=MibTableColumn
clusVolumeSnapshotACLIndex=_ClusVolumeSnapshotACLIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,12,18,1,1),_ClusVolumeSnapshotACLIndex_Type())
clusVolumeSnapshotACLIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:clusVolumeSnapshotACLIndex.setStatus(_A)
_ClusVolumeSnapshotACLAuthGroup_Type=OctetString
_ClusVolumeSnapshotACLAuthGroup_Object=MibTableColumn
clusVolumeSnapshotACLAuthGroup=_ClusVolumeSnapshotACLAuthGroup_Object((1,3,6,1,4,1,9804,3,1,1,2,12,18,1,2),_ClusVolumeSnapshotACLAuthGroup_Type())
clusVolumeSnapshotACLAuthGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:clusVolumeSnapshotACLAuthGroup.setStatus(_A)
_ClusVolumeSnapshotACLPermission_Type=ClusPermissionBits
_ClusVolumeSnapshotACLPermission_Object=MibScalar
clusVolumeSnapshotACLPermission=_ClusVolumeSnapshotACLPermission_Object((1,3,6,1,4,1,9804,3,1,1,2,12,18,1,3),_ClusVolumeSnapshotACLPermission_Type())
clusVolumeSnapshotACLPermission.setMaxAccess(_D)
if mibBuilder.loadTexts:clusVolumeSnapshotACLPermission.setStatus(_A)
_ClusVolumeSnapshotACLRowStatus_Type=RowStatus
_ClusVolumeSnapshotACLRowStatus_Object=MibTableColumn
clusVolumeSnapshotACLRowStatus=_ClusVolumeSnapshotACLRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,12,18,1,4),_ClusVolumeSnapshotACLRowStatus_Type())
clusVolumeSnapshotACLRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clusVolumeSnapshotACLRowStatus.setStatus(_A)
_ClusAuthGroupCount_Type=Integer32
_ClusAuthGroupCount_Object=MibScalar
clusAuthGroupCount=_ClusAuthGroupCount_Object((1,3,6,1,4,1,9804,3,1,1,2,12,19),_ClusAuthGroupCount_Type())
clusAuthGroupCount.setMaxAccess(_B)
if mibBuilder.loadTexts:clusAuthGroupCount.setStatus(_A)
_ClusAuthGroupTable_Object=MibTable
clusAuthGroupTable=_ClusAuthGroupTable_Object((1,3,6,1,4,1,9804,3,1,1,2,12,20))
if mibBuilder.loadTexts:clusAuthGroupTable.setStatus(_A)
_ClusAuthGroupEntry_Object=MibTableRow
clusAuthGroupEntry=_ClusAuthGroupEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,12,20,1))
clusAuthGroupEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:clusAuthGroupEntry.setStatus(_A)
_ClusAuthGroupIndex_Type=Integer32
_ClusAuthGroupIndex_Object=MibTableColumn
clusAuthGroupIndex=_ClusAuthGroupIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,12,20,1,1),_ClusAuthGroupIndex_Type())
clusAuthGroupIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:clusAuthGroupIndex.setStatus(_A)
_ClusAuthGroupName_Type=OctetString
_ClusAuthGroupName_Object=MibTableColumn
clusAuthGroupName=_ClusAuthGroupName_Object((1,3,6,1,4,1,9804,3,1,1,2,12,20,1,2),_ClusAuthGroupName_Type())
clusAuthGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:clusAuthGroupName.setStatus(_A)
_ClusAuthGroupDescription_Type=OctetString
_ClusAuthGroupDescription_Object=MibTableColumn
clusAuthGroupDescription=_ClusAuthGroupDescription_Object((1,3,6,1,4,1,9804,3,1,1,2,12,20,1,3),_ClusAuthGroupDescription_Type())
clusAuthGroupDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:clusAuthGroupDescription.setStatus(_A)
_ClusAuthGroupAcceptAll_Type=TruthValue
_ClusAuthGroupAcceptAll_Object=MibTableColumn
clusAuthGroupAcceptAll=_ClusAuthGroupAcceptAll_Object((1,3,6,1,4,1,9804,3,1,1,2,12,20,1,4),_ClusAuthGroupAcceptAll_Type())
clusAuthGroupAcceptAll.setMaxAccess(_D)
if mibBuilder.loadTexts:clusAuthGroupAcceptAll.setStatus(_A)
_ClusAuthGroupAcceptNone_Type=TruthValue
_ClusAuthGroupAcceptNone_Object=MibTableColumn
clusAuthGroupAcceptNone=_ClusAuthGroupAcceptNone_Object((1,3,6,1,4,1,9804,3,1,1,2,12,20,1,5),_ClusAuthGroupAcceptNone_Type())
clusAuthGroupAcceptNone.setMaxAccess(_D)
if mibBuilder.loadTexts:clusAuthGroupAcceptNone.setStatus(_A)
_ClusAuthGroupAcceptSubnet_Type=TruthValue
_ClusAuthGroupAcceptSubnet_Object=MibTableColumn
clusAuthGroupAcceptSubnet=_ClusAuthGroupAcceptSubnet_Object((1,3,6,1,4,1,9804,3,1,1,2,12,20,1,6),_ClusAuthGroupAcceptSubnet_Type())
clusAuthGroupAcceptSubnet.setMaxAccess(_D)
if mibBuilder.loadTexts:clusAuthGroupAcceptSubnet.setStatus(_A)
_ClusAuthGroupSubnetCount_Type=Counter32
_ClusAuthGroupSubnetCount_Object=MibScalar
clusAuthGroupSubnetCount=_ClusAuthGroupSubnetCount_Object((1,3,6,1,4,1,9804,3,1,1,2,12,20,1,7),_ClusAuthGroupSubnetCount_Type())
clusAuthGroupSubnetCount.setMaxAccess(_C)
if mibBuilder.loadTexts:clusAuthGroupSubnetCount.setStatus(_A)
_ClusAuthGroupRowStatus_Type=RowStatus
_ClusAuthGroupRowStatus_Object=MibTableColumn
clusAuthGroupRowStatus=_ClusAuthGroupRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,12,20,1,8),_ClusAuthGroupRowStatus_Type())
clusAuthGroupRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clusAuthGroupRowStatus.setStatus(_A)
_ClusAuthGroupSubnetTable_Object=MibTable
clusAuthGroupSubnetTable=_ClusAuthGroupSubnetTable_Object((1,3,6,1,4,1,9804,3,1,1,2,12,21))
if mibBuilder.loadTexts:clusAuthGroupSubnetTable.setStatus(_A)
_ClusAuthGroupSubnetEntry_Object=MibTableRow
clusAuthGroupSubnetEntry=_ClusAuthGroupSubnetEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,12,21,1))
clusAuthGroupSubnetEntry.setIndexNames((0,_E,_L),(0,_E,'clusAuthGroupNetmaskIndex'))
if mibBuilder.loadTexts:clusAuthGroupSubnetEntry.setStatus(_A)
_ClusAuthGroupSubnetIndex_Type=Integer32
_ClusAuthGroupSubnetIndex_Object=MibTableColumn
clusAuthGroupSubnetIndex=_ClusAuthGroupSubnetIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,12,21,1,1),_ClusAuthGroupSubnetIndex_Type())
clusAuthGroupSubnetIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:clusAuthGroupSubnetIndex.setStatus(_A)
_ClusAuthGroupSubnetAddress_Type=IpAddress
_ClusAuthGroupSubnetAddress_Object=MibTableColumn
clusAuthGroupSubnetAddress=_ClusAuthGroupSubnetAddress_Object((1,3,6,1,4,1,9804,3,1,1,2,12,21,1,2),_ClusAuthGroupSubnetAddress_Type())
clusAuthGroupSubnetAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:clusAuthGroupSubnetAddress.setStatus(_A)
_ClusAuthGroupSubnetMask_Type=IpAddress
_ClusAuthGroupSubnetMask_Object=MibTableColumn
clusAuthGroupSubnetMask=_ClusAuthGroupSubnetMask_Object((1,3,6,1,4,1,9804,3,1,1,2,12,21,1,3),_ClusAuthGroupSubnetMask_Type())
clusAuthGroupSubnetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:clusAuthGroupSubnetMask.setStatus(_A)
_ClusAuthGroupSubnetRowStatus_Type=RowStatus
_ClusAuthGroupSubnetRowStatus_Object=MibTableColumn
clusAuthGroupSubnetRowStatus=_ClusAuthGroupSubnetRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,12,21,1,4),_ClusAuthGroupSubnetRowStatus_Type())
clusAuthGroupSubnetRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clusAuthGroupSubnetRowStatus.setStatus(_A)
class _ClusCommunicationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('multicast',1),('unicast',2),('multicastAndUnicast',3)))
_ClusCommunicationMode_Type.__name__=_F
_ClusCommunicationMode_Object=MibScalar
clusCommunicationMode=_ClusCommunicationMode_Object((1,3,6,1,4,1,9804,3,1,1,2,12,22),_ClusCommunicationMode_Type())
clusCommunicationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:clusCommunicationMode.setStatus(_A)
_ClusUnicastHostCount_Type=Integer32
_ClusUnicastHostCount_Object=MibScalar
clusUnicastHostCount=_ClusUnicastHostCount_Object((1,3,6,1,4,1,9804,3,1,1,2,12,23),_ClusUnicastHostCount_Type())
clusUnicastHostCount.setMaxAccess(_B)
if mibBuilder.loadTexts:clusUnicastHostCount.setStatus(_A)
_ClusUnicastHostTable_Object=MibTable
clusUnicastHostTable=_ClusUnicastHostTable_Object((1,3,6,1,4,1,9804,3,1,1,2,12,24))
if mibBuilder.loadTexts:clusUnicastHostTable.setStatus(_A)
_ClusUnicastHostEntry_Object=MibTableRow
clusUnicastHostEntry=_ClusUnicastHostEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,12,24,1))
clusUnicastHostEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:clusUnicastHostEntry.setStatus(_A)
_ClusUnicastHostIndex_Type=Integer32
_ClusUnicastHostIndex_Object=MibTableColumn
clusUnicastHostIndex=_ClusUnicastHostIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,12,24,1,1),_ClusUnicastHostIndex_Type())
clusUnicastHostIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:clusUnicastHostIndex.setStatus(_A)
_ClusUnicastHostName_Type=OctetString
_ClusUnicastHostName_Object=MibTableColumn
clusUnicastHostName=_ClusUnicastHostName_Object((1,3,6,1,4,1,9804,3,1,1,2,12,24,1,2),_ClusUnicastHostName_Type())
clusUnicastHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:clusUnicastHostName.setStatus(_A)
_ClusUnicastHostRowStatus_Type=RowStatus
_ClusUnicastHostRowStatus_Object=MibTableColumn
clusUnicastHostRowStatus=_ClusUnicastHostRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,12,24,1,3),_ClusUnicastHostRowStatus_Type())
clusUnicastHostRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clusUnicastHostRowStatus.setStatus(_A)
_ClusSnapshotScheduleCount_Type=Integer32
_ClusSnapshotScheduleCount_Object=MibScalar
clusSnapshotScheduleCount=_ClusSnapshotScheduleCount_Object((1,3,6,1,4,1,9804,3,1,1,2,12,25),_ClusSnapshotScheduleCount_Type())
clusSnapshotScheduleCount.setMaxAccess(_B)
if mibBuilder.loadTexts:clusSnapshotScheduleCount.setStatus(_A)
_ClusSnapshotScheduleTable_Object=MibTable
clusSnapshotScheduleTable=_ClusSnapshotScheduleTable_Object((1,3,6,1,4,1,9804,3,1,1,2,12,26))
if mibBuilder.loadTexts:clusSnapshotScheduleTable.setStatus(_A)
_ClusSnapshotScheduleEntry_Object=MibTableRow
clusSnapshotScheduleEntry=_ClusSnapshotScheduleEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,12,26,1))
clusSnapshotScheduleEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:clusSnapshotScheduleEntry.setStatus(_A)
_ClusSnapshotScheduleIndex_Type=Integer32
_ClusSnapshotScheduleIndex_Object=MibTableColumn
clusSnapshotScheduleIndex=_ClusSnapshotScheduleIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,12,26,1,1),_ClusSnapshotScheduleIndex_Type())
clusSnapshotScheduleIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:clusSnapshotScheduleIndex.setStatus(_A)
_ClusSnapshotScheduleName_Type=OctetString
_ClusSnapshotScheduleName_Object=MibTableColumn
clusSnapshotScheduleName=_ClusSnapshotScheduleName_Object((1,3,6,1,4,1,9804,3,1,1,2,12,26,1,2),_ClusSnapshotScheduleName_Type())
clusSnapshotScheduleName.setMaxAccess(_C)
if mibBuilder.loadTexts:clusSnapshotScheduleName.setStatus(_A)
_ClusSnapshotScheduleDescription_Type=OctetString
_ClusSnapshotScheduleDescription_Object=MibTableColumn
clusSnapshotScheduleDescription=_ClusSnapshotScheduleDescription_Object((1,3,6,1,4,1,9804,3,1,1,2,12,26,1,3),_ClusSnapshotScheduleDescription_Type())
clusSnapshotScheduleDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:clusSnapshotScheduleDescription.setStatus(_A)
_ClusSnapshotScheduleSoftThreshold_Type=Counter64
_ClusSnapshotScheduleSoftThreshold_Object=MibTableColumn
clusSnapshotScheduleSoftThreshold=_ClusSnapshotScheduleSoftThreshold_Object((1,3,6,1,4,1,9804,3,1,1,2,12,26,1,4),_ClusSnapshotScheduleSoftThreshold_Type())
clusSnapshotScheduleSoftThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:clusSnapshotScheduleSoftThreshold.setStatus(_A)
if mibBuilder.loadTexts:clusSnapshotScheduleSoftThreshold.setUnits(_G)
_ClusSnapshotScheduleHardThreshold_Type=Counter64
_ClusSnapshotScheduleHardThreshold_Object=MibTableColumn
clusSnapshotScheduleHardThreshold=_ClusSnapshotScheduleHardThreshold_Object((1,3,6,1,4,1,9804,3,1,1,2,12,26,1,5),_ClusSnapshotScheduleHardThreshold_Type())
clusSnapshotScheduleHardThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:clusSnapshotScheduleHardThreshold.setStatus(_A)
if mibBuilder.loadTexts:clusSnapshotScheduleHardThreshold.setUnits(_G)
_ClusSnapshotScheduleFirstCreationTime_Type=DateAndTime
_ClusSnapshotScheduleFirstCreationTime_Object=MibTableColumn
clusSnapshotScheduleFirstCreationTime=_ClusSnapshotScheduleFirstCreationTime_Object((1,3,6,1,4,1,9804,3,1,1,2,12,26,1,6),_ClusSnapshotScheduleFirstCreationTime_Type())
clusSnapshotScheduleFirstCreationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:clusSnapshotScheduleFirstCreationTime.setStatus(_A)
_ClusSnapshotScheduleFrequency_Type=Counter32
_ClusSnapshotScheduleFrequency_Object=MibTableColumn
clusSnapshotScheduleFrequency=_ClusSnapshotScheduleFrequency_Object((1,3,6,1,4,1,9804,3,1,1,2,12,26,1,7),_ClusSnapshotScheduleFrequency_Type())
clusSnapshotScheduleFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:clusSnapshotScheduleFrequency.setStatus(_A)
if mibBuilder.loadTexts:clusSnapshotScheduleFrequency.setUnits(_X)
_ClusSnapshotScheduleVolumeName_Type=OctetString
_ClusSnapshotScheduleVolumeName_Object=MibTableColumn
clusSnapshotScheduleVolumeName=_ClusSnapshotScheduleVolumeName_Object((1,3,6,1,4,1,9804,3,1,1,2,12,26,1,8),_ClusSnapshotScheduleVolumeName_Type())
clusSnapshotScheduleVolumeName.setMaxAccess(_C)
if mibBuilder.loadTexts:clusSnapshotScheduleVolumeName.setStatus(_A)
class _ClusSnapshotScheduleRetainType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('byTime',1),('byNumber',2)))
_ClusSnapshotScheduleRetainType_Type.__name__=_F
_ClusSnapshotScheduleRetainType_Object=MibTableColumn
clusSnapshotScheduleRetainType=_ClusSnapshotScheduleRetainType_Object((1,3,6,1,4,1,9804,3,1,1,2,12,26,1,9),_ClusSnapshotScheduleRetainType_Type())
clusSnapshotScheduleRetainType.setMaxAccess(_D)
if mibBuilder.loadTexts:clusSnapshotScheduleRetainType.setStatus(_A)
_ClusSnapshotScheduleRetainCount_Type=Counter32
_ClusSnapshotScheduleRetainCount_Object=MibTableColumn
clusSnapshotScheduleRetainCount=_ClusSnapshotScheduleRetainCount_Object((1,3,6,1,4,1,9804,3,1,1,2,12,26,1,10),_ClusSnapshotScheduleRetainCount_Type())
clusSnapshotScheduleRetainCount.setMaxAccess(_D)
if mibBuilder.loadTexts:clusSnapshotScheduleRetainCount.setStatus(_A)
_ClusSnapshotScheduleRetainTime_Type=Counter32
_ClusSnapshotScheduleRetainTime_Object=MibTableColumn
clusSnapshotScheduleRetainTime=_ClusSnapshotScheduleRetainTime_Object((1,3,6,1,4,1,9804,3,1,1,2,12,26,1,11),_ClusSnapshotScheduleRetainTime_Type())
clusSnapshotScheduleRetainTime.setMaxAccess(_D)
if mibBuilder.loadTexts:clusSnapshotScheduleRetainTime.setStatus(_A)
if mibBuilder.loadTexts:clusSnapshotScheduleRetainTime.setUnits(_X)
class _ClusSnapshotScheduleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_S,2),(_T,3)))
_ClusSnapshotScheduleType_Type.__name__=_F
_ClusSnapshotScheduleType_Object=MibTableColumn
clusSnapshotScheduleType=_ClusSnapshotScheduleType_Object((1,3,6,1,4,1,9804,3,1,1,2,12,26,1,13),_ClusSnapshotScheduleType_Type())
clusSnapshotScheduleType.setMaxAccess(_C)
if mibBuilder.loadTexts:clusSnapshotScheduleType.setStatus(_A)
_ClusSnapshotScheduleFailureMessage_Type=OctetString
_ClusSnapshotScheduleFailureMessage_Object=MibTableColumn
clusSnapshotScheduleFailureMessage=_ClusSnapshotScheduleFailureMessage_Object((1,3,6,1,4,1,9804,3,1,1,2,12,26,1,14),_ClusSnapshotScheduleFailureMessage_Type())
clusSnapshotScheduleFailureMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:clusSnapshotScheduleFailureMessage.setStatus(_A)
_ClusSnapshotScheduleRowStatus_Type=RowStatus
_ClusSnapshotScheduleRowStatus_Object=MibTableColumn
clusSnapshotScheduleRowStatus=_ClusSnapshotScheduleRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,12,26,1,15),_ClusSnapshotScheduleRowStatus_Type())
clusSnapshotScheduleRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:clusSnapshotScheduleRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'ClusPermissionBits':ClusPermissionBits,'lhnNusCommonClusteringModule':lhnNusCommonClusteringModule,'clusMgmtGroupName':clusMgmtGroupName,'clusMgmtGroupIsEnabled':clusMgmtGroupIsEnabled,'clusMgmtGroupQuorum':clusMgmtGroupQuorum,'clusMgmtGroupDescription':clusMgmtGroupDescription,'clusMgmtGroupActiveManagerCount':clusMgmtGroupActiveManagerCount,'clusMgmtGroupManagerCount':clusMgmtGroupManagerCount,'clusManagerTable':clusManagerTable,'clusManagerEntry':clusManagerEntry,_M:clusManagerIndex,'clusManagerName':clusManagerName,'clusManagerVersion':clusManagerVersion,'clusManagerHostSerialNo':clusManagerHostSerialNo,'clusManagerStatus':clusManagerStatus,'clusManagerIsVirtual':clusManagerIsVirtual,'clusManagerRowStatus':clusManagerRowStatus,'clusModuleCount':clusModuleCount,'clusModuleTable':clusModuleTable,'clusModuleEntry':clusModuleEntry,_N:clusModuleIndex,'clusModuleName':clusModuleName,'clusModuleVersion':clusModuleVersion,'clusModuleSerialNo':clusModuleSerialNo,'clusModuleTotalSize':clusModuleTotalSize,'clusModuleAvailSize':clusModuleAvailSize,'clusModuleIsManager':clusModuleIsManager,'clusModuleRaidConfiguration':clusModuleRaidConfiguration,'clusModuleRaidStatus':clusModuleRaidStatus,'clusModuleStorageStatus':clusModuleStorageStatus,'clusModuleStorageIsReady':clusModuleStorageIsReady,'clusModuleCreationTime':clusModuleCreationTime,'clusModuleDescription':clusModuleDescription,'clusModuleClusterName':clusModuleClusterName,'clusModuleRowStatus':clusModuleRowStatus,'clusClusterCount':clusClusterCount,'clusClusterTable':clusClusterTable,'clusClusterEntry':clusClusterEntry,_I:clusClusterIndex,'clusClusterName':clusClusterName,'clusClusterModuleCount':clusClusterModuleCount,'clusClusterVolumeCount':clusClusterVolumeCount,'clusClusterDescription':clusClusterDescription,'clusClusterRowStatus':clusClusterRowStatus,'clusClusterModuleTable':clusClusterModuleTable,'clusClusterModuleEntry':clusClusterModuleEntry,_O:clusClusterModuleIndex,'clusClusterModuleName':clusClusterModuleName,'clusClusterModuleSerialNo':clusClusterModuleSerialNo,'clusClusterModuleIsHotSpare':clusClusterModuleIsHotSpare,'clusClusterModuleRowStatus':clusClusterModuleRowStatus,'clusVolumeCount':clusVolumeCount,'clusVolumeTable':clusVolumeTable,'clusVolumeEntry':clusVolumeEntry,_H:clusVolumeIndex,'clusVolumeName':clusVolumeName,'clusVolumeCreationTime':clusVolumeCreationTime,'clusVolumeDescription':clusVolumeDescription,'clusVolumeSize':clusVolumeSize,'clusVolumeSoftThreshold':clusVolumeSoftThreshold,'clusVolumeHardThreshold':clusVolumeHardThreshold,'clusVolumeReplicaCount':clusVolumeReplicaCount,'clusVolumeSnapshotCount':clusVolumeSnapshotCount,'clusVolumeACLCount':clusVolumeACLCount,'clusVolumeClusterName':clusVolumeClusterName,'clusVolumeIsSoftThresholdExceeded':clusVolumeIsSoftThresholdExceeded,'clusVolumeIsHardThresholdExceeded':clusVolumeIsHardThresholdExceeded,'clusVolumeReplicationStatus':clusVolumeReplicationStatus,'clusVolumeIsRemoteIPCopy':clusVolumeIsRemoteIPCopy,'clusVolumeRemoteIPCopyFailureMessage':clusVolumeRemoteIPCopyFailureMessage,'clusVolumeRowStatus':clusVolumeRowStatus,'clusVolumeACLTable':clusVolumeACLTable,'clusVolumeACLEntry':clusVolumeACLEntry,_Q:clusVolumeACLIndex,'clusVolumeACLAuthGroup':clusVolumeACLAuthGroup,'clusVolumeACLPermissions':clusVolumeACLPermissions,'clusVolumeACLRowStatus':clusVolumeACLRowStatus,'clusClusterVolumeTable':clusClusterVolumeTable,'clusClusterVolumeEntry':clusClusterVolumeEntry,_R:clusClusterVolumeIndex,'clusClusterVolumeName':clusClusterVolumeName,'clusClusterVolumeRowStatus':clusClusterVolumeRowStatus,'clusVolumeSnapshotTable':clusVolumeSnapshotTable,'clusVolumeSnapshotEntry':clusVolumeSnapshotEntry,_K:clusVolumeSnapshotIndex,'clusVolumeSnapshotName':clusVolumeSnapshotName,'clusVolumeSnapshotCreationTime':clusVolumeSnapshotCreationTime,'clusVolumeSnapshotDescription':clusVolumeSnapshotDescription,'clusVolumeSnapshotSize':clusVolumeSnapshotSize,'clusVolumeSnapshotSoftThreshold':clusVolumeSnapshotSoftThreshold,'clusVolumeSnapshotHardThreshold':clusVolumeSnapshotHardThreshold,'clusVolumeSnapshotACLCount':clusVolumeSnapshotACLCount,'clusVolumeSnapshotScheduleName':clusVolumeSnapshotScheduleName,'clusVolumeSnapshotIsSoftThresholdExceeded':clusVolumeSnapshotIsSoftThresholdExceeded,'clusVolumeSnapshotIsHardThresholdExceeded':clusVolumeSnapshotIsHardThresholdExceeded,'clusVolumeSnapshotReplicationStatus':clusVolumeSnapshotReplicationStatus,'clusVolumeSnapshotType':clusVolumeSnapshotType,'clusVolumeSnapshotCopyProgress':clusVolumeSnapshotCopyProgress,'clusVolumeSnapshotRowStatus':clusVolumeSnapshotRowStatus,'clusVolumeSnapshotACLTable':clusVolumeSnapshotACLTable,'clusVolumeSnapshotACLEntry':clusVolumeSnapshotACLEntry,_U:clusVolumeSnapshotACLIndex,'clusVolumeSnapshotACLAuthGroup':clusVolumeSnapshotACLAuthGroup,'clusVolumeSnapshotACLPermission':clusVolumeSnapshotACLPermission,'clusVolumeSnapshotACLRowStatus':clusVolumeSnapshotACLRowStatus,'clusAuthGroupCount':clusAuthGroupCount,'clusAuthGroupTable':clusAuthGroupTable,'clusAuthGroupEntry':clusAuthGroupEntry,_L:clusAuthGroupIndex,'clusAuthGroupName':clusAuthGroupName,'clusAuthGroupDescription':clusAuthGroupDescription,'clusAuthGroupAcceptAll':clusAuthGroupAcceptAll,'clusAuthGroupAcceptNone':clusAuthGroupAcceptNone,'clusAuthGroupAcceptSubnet':clusAuthGroupAcceptSubnet,'clusAuthGroupSubnetCount':clusAuthGroupSubnetCount,'clusAuthGroupRowStatus':clusAuthGroupRowStatus,'clusAuthGroupSubnetTable':clusAuthGroupSubnetTable,'clusAuthGroupSubnetEntry':clusAuthGroupSubnetEntry,'clusAuthGroupSubnetIndex':clusAuthGroupSubnetIndex,'clusAuthGroupSubnetAddress':clusAuthGroupSubnetAddress,'clusAuthGroupSubnetMask':clusAuthGroupSubnetMask,'clusAuthGroupSubnetRowStatus':clusAuthGroupSubnetRowStatus,'clusCommunicationMode':clusCommunicationMode,'clusUnicastHostCount':clusUnicastHostCount,'clusUnicastHostTable':clusUnicastHostTable,'clusUnicastHostEntry':clusUnicastHostEntry,_V:clusUnicastHostIndex,'clusUnicastHostName':clusUnicastHostName,'clusUnicastHostRowStatus':clusUnicastHostRowStatus,'clusSnapshotScheduleCount':clusSnapshotScheduleCount,'clusSnapshotScheduleTable':clusSnapshotScheduleTable,'clusSnapshotScheduleEntry':clusSnapshotScheduleEntry,_W:clusSnapshotScheduleIndex,'clusSnapshotScheduleName':clusSnapshotScheduleName,'clusSnapshotScheduleDescription':clusSnapshotScheduleDescription,'clusSnapshotScheduleSoftThreshold':clusSnapshotScheduleSoftThreshold,'clusSnapshotScheduleHardThreshold':clusSnapshotScheduleHardThreshold,'clusSnapshotScheduleFirstCreationTime':clusSnapshotScheduleFirstCreationTime,'clusSnapshotScheduleFrequency':clusSnapshotScheduleFrequency,'clusSnapshotScheduleVolumeName':clusSnapshotScheduleVolumeName,'clusSnapshotScheduleRetainType':clusSnapshotScheduleRetainType,'clusSnapshotScheduleRetainCount':clusSnapshotScheduleRetainCount,'clusSnapshotScheduleRetainTime':clusSnapshotScheduleRetainTime,'clusSnapshotScheduleType':clusSnapshotScheduleType,'clusSnapshotScheduleFailureMessage':clusSnapshotScheduleFailureMessage,'clusSnapshotScheduleRowStatus':clusSnapshotScheduleRowStatus})