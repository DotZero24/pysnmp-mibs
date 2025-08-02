_O='pysmiFakeCol3'
_N='not-accessible'
_M='nwhrProtocolName'
_L='pysmiFakeCol2'
_K='nwhrPrinterID'
_J='nwhrAdapterIndex'
_I='OctetString'
_H='nwhrPhysicalPartitionIndex'
_G='InternationalDisplayString'
_F='hrDeviceIndex'
_E='HOST-RESOURCES-MIB'
_D='NetWare-Host-Ext-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hrDeviceIndex,=mibBuilder.importSymbols(_E,_F)
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class TransportDomain(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noAddress',1),('ipx',2),('ip',3),('appleTalkDDP',4)))
class TransportAddress(OctetString):0
class KBytes(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class InternationalDisplayString(OctetString):0
_Novell_ObjectIdentity=ObjectIdentity
novell=_Novell_ObjectIdentity((1,3,6,1,4,1,23))
_MibDoc_ObjectIdentity=ObjectIdentity
mibDoc=_MibDoc_ObjectIdentity((1,3,6,1,4,1,23,2))
_NwHostExtensions_ObjectIdentity=ObjectIdentity
nwHostExtensions=_NwHostExtensions_ObjectIdentity((1,3,6,1,4,1,23,2,27))
_NwhrStorage_ObjectIdentity=ObjectIdentity
nwhrStorage=_NwhrStorage_ObjectIdentity((1,3,6,1,4,1,23,2,27,2))
_NwhrStorageTypes_ObjectIdentity=ObjectIdentity
nwhrStorageTypes=_NwhrStorageTypes_ObjectIdentity((1,3,6,1,4,1,23,2,27,2,1))
_NwhrStorageVolume_ObjectIdentity=ObjectIdentity
nwhrStorageVolume=_NwhrStorageVolume_ObjectIdentity((1,3,6,1,4,1,23,2,27,2,1,1))
_NwhrStorageMemoryPermanent_ObjectIdentity=ObjectIdentity
nwhrStorageMemoryPermanent=_NwhrStorageMemoryPermanent_ObjectIdentity((1,3,6,1,4,1,23,2,27,2,1,2))
_NwhrStorageMemoryAlloc_ObjectIdentity=ObjectIdentity
nwhrStorageMemoryAlloc=_NwhrStorageMemoryAlloc_ObjectIdentity((1,3,6,1,4,1,23,2,27,2,1,3))
_NwhrStorageCacheBuffers_ObjectIdentity=ObjectIdentity
nwhrStorageCacheBuffers=_NwhrStorageCacheBuffers_ObjectIdentity((1,3,6,1,4,1,23,2,27,2,1,4))
_NwhrStorageCacheMovable_ObjectIdentity=ObjectIdentity
nwhrStorageCacheMovable=_NwhrStorageCacheMovable_ObjectIdentity((1,3,6,1,4,1,23,2,27,2,1,5))
_NwhrStorageCacheNonMovable_ObjectIdentity=ObjectIdentity
nwhrStorageCacheNonMovable=_NwhrStorageCacheNonMovable_ObjectIdentity((1,3,6,1,4,1,23,2,27,2,1,6))
_NwhrStorageCodeAndDataMemory_ObjectIdentity=ObjectIdentity
nwhrStorageCodeAndDataMemory=_NwhrStorageCodeAndDataMemory_ObjectIdentity((1,3,6,1,4,1,23,2,27,2,1,7))
_NwhrStorageDOSMemory_ObjectIdentity=ObjectIdentity
nwhrStorageDOSMemory=_NwhrStorageDOSMemory_ObjectIdentity((1,3,6,1,4,1,23,2,27,2,1,8))
_NwhrStorageIOEngineMemory_ObjectIdentity=ObjectIdentity
nwhrStorageIOEngineMemory=_NwhrStorageIOEngineMemory_ObjectIdentity((1,3,6,1,4,1,23,2,27,2,1,9))
_NwhrStorageMSEngineMemory_ObjectIdentity=ObjectIdentity
nwhrStorageMSEngineMemory=_NwhrStorageMSEngineMemory_ObjectIdentity((1,3,6,1,4,1,23,2,27,2,1,10))
_NwhrStorageUnclaimedMemory_ObjectIdentity=ObjectIdentity
nwhrStorageUnclaimedMemory=_NwhrStorageUnclaimedMemory_ObjectIdentity((1,3,6,1,4,1,23,2,27,2,1,11))
_NwhrDevice_ObjectIdentity=ObjectIdentity
nwhrDevice=_NwhrDevice_ObjectIdentity((1,3,6,1,4,1,23,2,27,3))
_NwhrDeviceTypes_ObjectIdentity=ObjectIdentity
nwhrDeviceTypes=_NwhrDeviceTypes_ObjectIdentity((1,3,6,1,4,1,23,2,27,3,1))
_NwhrDeviceMirroredServerLink_ObjectIdentity=ObjectIdentity
nwhrDeviceMirroredServerLink=_NwhrDeviceMirroredServerLink_ObjectIdentity((1,3,6,1,4,1,23,2,27,3,1,1))
_NwhrDeviceTable_Object=MibTable
nwhrDeviceTable=_NwhrDeviceTable_Object((1,3,6,1,4,1,23,2,27,3,2))
if mibBuilder.loadTexts:nwhrDeviceTable.setStatus(_A)
_NwhrDeviceEntry_Object=MibTableRow
nwhrDeviceEntry=_NwhrDeviceEntry_Object((1,3,6,1,4,1,23,2,27,3,2,1))
nwhrDeviceEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:nwhrDeviceEntry.setStatus(_A)
_NwhrDeviceAdapterIndex_Type=Integer32
_NwhrDeviceAdapterIndex_Object=MibTableColumn
nwhrDeviceAdapterIndex=_NwhrDeviceAdapterIndex_Object((1,3,6,1,4,1,23,2,27,3,2,1,1),_NwhrDeviceAdapterIndex_Type())
nwhrDeviceAdapterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrDeviceAdapterIndex.setStatus(_A)
_NwhrDeviceControllerNumber_Type=Integer32
_NwhrDeviceControllerNumber_Object=MibTableColumn
nwhrDeviceControllerNumber=_NwhrDeviceControllerNumber_Object((1,3,6,1,4,1,23,2,27,3,2,1,2),_NwhrDeviceControllerNumber_Type())
nwhrDeviceControllerNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrDeviceControllerNumber.setStatus(_A)
_NwhrDeviceNumber_Type=Integer32
_NwhrDeviceNumber_Object=MibTableColumn
nwhrDeviceNumber=_NwhrDeviceNumber_Object((1,3,6,1,4,1,23,2,27,3,2,1,3),_NwhrDeviceNumber_Type())
nwhrDeviceNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrDeviceNumber.setStatus(_A)
_NwhrProcessorCount_Type=Integer32
_NwhrProcessorCount_Object=MibScalar
nwhrProcessorCount=_NwhrProcessorCount_Object((1,3,6,1,4,1,23,2,27,3,3),_NwhrProcessorCount_Type())
nwhrProcessorCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrProcessorCount.setStatus(_A)
_NwhrPrinterCount_Type=Integer32
_NwhrPrinterCount_Object=MibScalar
nwhrPrinterCount=_NwhrPrinterCount_Object((1,3,6,1,4,1,23,2,27,3,4),_NwhrPrinterCount_Type())
nwhrPrinterCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrPrinterCount.setStatus(_A)
_NwhrDiskStorageCount_Type=Integer32
_NwhrDiskStorageCount_Object=MibScalar
nwhrDiskStorageCount=_NwhrDiskStorageCount_Object((1,3,6,1,4,1,23,2,27,3,5),_NwhrDiskStorageCount_Type())
nwhrDiskStorageCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrDiskStorageCount.setStatus(_A)
_NwhrDiskStorageTable_Object=MibTable
nwhrDiskStorageTable=_NwhrDiskStorageTable_Object((1,3,6,1,4,1,23,2,27,3,6))
if mibBuilder.loadTexts:nwhrDiskStorageTable.setStatus(_A)
_NwhrDiskStorageEntry_Object=MibTableRow
nwhrDiskStorageEntry=_NwhrDiskStorageEntry_Object((1,3,6,1,4,1,23,2,27,3,6,1))
nwhrDiskStorageEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:nwhrDiskStorageEntry.setStatus(_A)
_NwhrDiskStorageHeads_Type=Integer32
_NwhrDiskStorageHeads_Object=MibTableColumn
nwhrDiskStorageHeads=_NwhrDiskStorageHeads_Object((1,3,6,1,4,1,23,2,27,3,6,1,1),_NwhrDiskStorageHeads_Type())
nwhrDiskStorageHeads.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrDiskStorageHeads.setStatus(_A)
_NwhrDiskStorageCylinders_Type=Integer32
_NwhrDiskStorageCylinders_Object=MibTableColumn
nwhrDiskStorageCylinders=_NwhrDiskStorageCylinders_Object((1,3,6,1,4,1,23,2,27,3,6,1,2),_NwhrDiskStorageCylinders_Type())
nwhrDiskStorageCylinders.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrDiskStorageCylinders.setStatus(_A)
_NwhrDiskStorageSectorsPerTrack_Type=Integer32
_NwhrDiskStorageSectorsPerTrack_Object=MibTableColumn
nwhrDiskStorageSectorsPerTrack=_NwhrDiskStorageSectorsPerTrack_Object((1,3,6,1,4,1,23,2,27,3,6,1,3),_NwhrDiskStorageSectorsPerTrack_Type())
nwhrDiskStorageSectorsPerTrack.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrDiskStorageSectorsPerTrack.setStatus(_A)
_NwhrDiskStorageSectorSize_Type=Integer32
_NwhrDiskStorageSectorSize_Object=MibTableColumn
nwhrDiskStorageSectorSize=_NwhrDiskStorageSectorSize_Object((1,3,6,1,4,1,23,2,27,3,6,1,4),_NwhrDiskStorageSectorSize_Type())
nwhrDiskStorageSectorSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrDiskStorageSectorSize.setStatus(_A)
_NwhrDiskStorageBlockSize_Type=Integer32
_NwhrDiskStorageBlockSize_Object=MibTableColumn
nwhrDiskStorageBlockSize=_NwhrDiskStorageBlockSize_Object((1,3,6,1,4,1,23,2,27,3,6,1,5),_NwhrDiskStorageBlockSize_Type())
nwhrDiskStorageBlockSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrDiskStorageBlockSize.setStatus(_A)
_NwhrPhysicalPartitionTable_Object=MibTable
nwhrPhysicalPartitionTable=_NwhrPhysicalPartitionTable_Object((1,3,6,1,4,1,23,2,27,3,7))
if mibBuilder.loadTexts:nwhrPhysicalPartitionTable.setStatus(_A)
_NwhrPhysicalPartitionEntry_Object=MibTableRow
nwhrPhysicalPartitionEntry=_NwhrPhysicalPartitionEntry_Object((1,3,6,1,4,1,23,2,27,3,7,1))
nwhrPhysicalPartitionEntry.setIndexNames((0,_E,_F),(0,_D,_H))
if mibBuilder.loadTexts:nwhrPhysicalPartitionEntry.setStatus(_A)
class _NwhrPhysicalPartitionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NwhrPhysicalPartitionIndex_Type.__name__=_C
_NwhrPhysicalPartitionIndex_Object=MibTableColumn
nwhrPhysicalPartitionIndex=_NwhrPhysicalPartitionIndex_Object((1,3,6,1,4,1,23,2,27,3,7,1,1),_NwhrPhysicalPartitionIndex_Type())
nwhrPhysicalPartitionIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrPhysicalPartitionIndex.setStatus(_A)
class _NwhrPhysicalPartitionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('netWare',2),('dos',3),('inwDos',4)))
_NwhrPhysicalPartitionType_Type.__name__=_C
_NwhrPhysicalPartitionType_Object=MibTableColumn
nwhrPhysicalPartitionType=_NwhrPhysicalPartitionType_Object((1,3,6,1,4,1,23,2,27,3,7,1,2),_NwhrPhysicalPartitionType_Type())
nwhrPhysicalPartitionType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrPhysicalPartitionType.setStatus(_A)
class _NwhrPhysicalPartitionDescr_Type(InternationalDisplayString):subtypeSpec=InternationalDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_NwhrPhysicalPartitionDescr_Type.__name__=_G
_NwhrPhysicalPartitionDescr_Object=MibTableColumn
nwhrPhysicalPartitionDescr=_NwhrPhysicalPartitionDescr_Object((1,3,6,1,4,1,23,2,27,3,7,1,3),_NwhrPhysicalPartitionDescr_Type())
nwhrPhysicalPartitionDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrPhysicalPartitionDescr.setStatus(_A)
_NwhrPhysicalPartitionSize_Type=KBytes
_NwhrPhysicalPartitionSize_Object=MibTableColumn
nwhrPhysicalPartitionSize=_NwhrPhysicalPartitionSize_Object((1,3,6,1,4,1,23,2,27,3,7,1,4),_NwhrPhysicalPartitionSize_Type())
nwhrPhysicalPartitionSize.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrPhysicalPartitionSize.setStatus(_A)
_NwhrHotfixTable_Object=MibTable
nwhrHotfixTable=_NwhrHotfixTable_Object((1,3,6,1,4,1,23,2,27,3,8))
if mibBuilder.loadTexts:nwhrHotfixTable.setStatus(_A)
_NwhrHotfixEntry_Object=MibTableRow
nwhrHotfixEntry=_NwhrHotfixEntry_Object((1,3,6,1,4,1,23,2,27,3,8,1))
nwhrHotfixEntry.setIndexNames((0,_E,_F),(0,_D,_H))
if mibBuilder.loadTexts:nwhrHotfixEntry.setStatus(_A)
_NwhrHotfixUnits_Type=Integer32
_NwhrHotfixUnits_Object=MibTableColumn
nwhrHotfixUnits=_NwhrHotfixUnits_Object((1,3,6,1,4,1,23,2,27,3,8,1,1),_NwhrHotfixUnits_Type())
nwhrHotfixUnits.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrHotfixUnits.setStatus(_A)
_NwhrHotfixTotal_Type=Integer32
_NwhrHotfixTotal_Object=MibTableColumn
nwhrHotfixTotal=_NwhrHotfixTotal_Object((1,3,6,1,4,1,23,2,27,3,8,1,2),_NwhrHotfixTotal_Type())
nwhrHotfixTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrHotfixTotal.setStatus(_A)
_NwhrHotfixUsed_Type=Integer32
_NwhrHotfixUsed_Object=MibTableColumn
nwhrHotfixUsed=_NwhrHotfixUsed_Object((1,3,6,1,4,1,23,2,27,3,8,1,3),_NwhrHotfixUsed_Type())
nwhrHotfixUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrHotfixUsed.setStatus(_A)
_NwhrHotfixReserved_Type=Integer32
_NwhrHotfixReserved_Object=MibTableColumn
nwhrHotfixReserved=_NwhrHotfixReserved_Object((1,3,6,1,4,1,23,2,27,3,8,1,4),_NwhrHotfixReserved_Type())
nwhrHotfixReserved.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrHotfixReserved.setStatus(_A)
_NwhrAdapterCount_Type=Integer32
_NwhrAdapterCount_Object=MibScalar
nwhrAdapterCount=_NwhrAdapterCount_Object((1,3,6,1,4,1,23,2,27,3,9),_NwhrAdapterCount_Type())
nwhrAdapterCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrAdapterCount.setStatus(_A)
_NwhrAdapterTable_Object=MibTable
nwhrAdapterTable=_NwhrAdapterTable_Object((1,3,6,1,4,1,23,2,27,3,10))
if mibBuilder.loadTexts:nwhrAdapterTable.setStatus(_A)
_NwhrAdapterEntry_Object=MibTableRow
nwhrAdapterEntry=_NwhrAdapterEntry_Object((1,3,6,1,4,1,23,2,27,3,10,1))
nwhrAdapterEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:nwhrAdapterEntry.setStatus(_A)
_NwhrAdapterIndex_Type=Integer32
_NwhrAdapterIndex_Object=MibTableColumn
nwhrAdapterIndex=_NwhrAdapterIndex_Object((1,3,6,1,4,1,23,2,27,3,10,1,1),_NwhrAdapterIndex_Type())
nwhrAdapterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrAdapterIndex.setStatus(_A)
_NwhrAdapterType_Type=ObjectIdentifier
_NwhrAdapterType_Object=MibTableColumn
nwhrAdapterType=_NwhrAdapterType_Object((1,3,6,1,4,1,23,2,27,3,10,1,2),_NwhrAdapterType_Type())
nwhrAdapterType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrAdapterType.setStatus(_A)
class _NwhrAdapterDescr_Type(InternationalDisplayString):subtypeSpec=InternationalDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_NwhrAdapterDescr_Type.__name__=_G
_NwhrAdapterDescr_Object=MibTableColumn
nwhrAdapterDescr=_NwhrAdapterDescr_Object((1,3,6,1,4,1,23,2,27,3,10,1,3),_NwhrAdapterDescr_Type())
nwhrAdapterDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrAdapterDescr.setStatus(_A)
class _NwhrAdapterDriverDescr_Type(InternationalDisplayString):subtypeSpec=InternationalDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_NwhrAdapterDriverDescr_Type.__name__=_G
_NwhrAdapterDriverDescr_Object=MibTableColumn
nwhrAdapterDriverDescr=_NwhrAdapterDriverDescr_Object((1,3,6,1,4,1,23,2,27,3,10,1,4),_NwhrAdapterDriverDescr_Type())
nwhrAdapterDriverDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrAdapterDriverDescr.setStatus(_A)
_NwhrAdapterDriverMajorVer_Type=Integer32
_NwhrAdapterDriverMajorVer_Object=MibTableColumn
nwhrAdapterDriverMajorVer=_NwhrAdapterDriverMajorVer_Object((1,3,6,1,4,1,23,2,27,3,10,1,5),_NwhrAdapterDriverMajorVer_Type())
nwhrAdapterDriverMajorVer.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrAdapterDriverMajorVer.setStatus(_A)
_NwhrAdapterDriverMinorVer_Type=Integer32
_NwhrAdapterDriverMinorVer_Object=MibTableColumn
nwhrAdapterDriverMinorVer=_NwhrAdapterDriverMinorVer_Object((1,3,6,1,4,1,23,2,27,3,10,1,6),_NwhrAdapterDriverMinorVer_Type())
nwhrAdapterDriverMinorVer.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrAdapterDriverMinorVer.setStatus(_A)
_NwhrAdapterPort1_Type=Integer32
_NwhrAdapterPort1_Object=MibTableColumn
nwhrAdapterPort1=_NwhrAdapterPort1_Object((1,3,6,1,4,1,23,2,27,3,10,1,7),_NwhrAdapterPort1_Type())
nwhrAdapterPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrAdapterPort1.setStatus(_A)
_NwhrAdapterPort1Len_Type=Integer32
_NwhrAdapterPort1Len_Object=MibTableColumn
nwhrAdapterPort1Len=_NwhrAdapterPort1Len_Object((1,3,6,1,4,1,23,2,27,3,10,1,8),_NwhrAdapterPort1Len_Type())
nwhrAdapterPort1Len.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrAdapterPort1Len.setStatus(_A)
_NwhrAdapterPort2_Type=Integer32
_NwhrAdapterPort2_Object=MibTableColumn
nwhrAdapterPort2=_NwhrAdapterPort2_Object((1,3,6,1,4,1,23,2,27,3,10,1,9),_NwhrAdapterPort2_Type())
nwhrAdapterPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrAdapterPort2.setStatus(_A)
_NwhrAdapterPort2Len_Type=Integer32
_NwhrAdapterPort2Len_Object=MibTableColumn
nwhrAdapterPort2Len=_NwhrAdapterPort2Len_Object((1,3,6,1,4,1,23,2,27,3,10,1,10),_NwhrAdapterPort2Len_Type())
nwhrAdapterPort2Len.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrAdapterPort2Len.setStatus(_A)
_NwhrAdapterMem1_Type=Integer32
_NwhrAdapterMem1_Object=MibTableColumn
nwhrAdapterMem1=_NwhrAdapterMem1_Object((1,3,6,1,4,1,23,2,27,3,10,1,11),_NwhrAdapterMem1_Type())
nwhrAdapterMem1.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrAdapterMem1.setStatus(_A)
_NwhrAdapterMem1Len_Type=Integer32
_NwhrAdapterMem1Len_Object=MibTableColumn
nwhrAdapterMem1Len=_NwhrAdapterMem1Len_Object((1,3,6,1,4,1,23,2,27,3,10,1,12),_NwhrAdapterMem1Len_Type())
nwhrAdapterMem1Len.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrAdapterMem1Len.setStatus(_A)
_NwhrAdapterMem2_Type=Integer32
_NwhrAdapterMem2_Object=MibTableColumn
nwhrAdapterMem2=_NwhrAdapterMem2_Object((1,3,6,1,4,1,23,2,27,3,10,1,13),_NwhrAdapterMem2_Type())
nwhrAdapterMem2.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrAdapterMem2.setStatus(_A)
_NwhrAdapterMem2Len_Type=Integer32
_NwhrAdapterMem2Len_Object=MibTableColumn
nwhrAdapterMem2Len=_NwhrAdapterMem2Len_Object((1,3,6,1,4,1,23,2,27,3,10,1,14),_NwhrAdapterMem2Len_Type())
nwhrAdapterMem2Len.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrAdapterMem2Len.setStatus(_A)
class _NwhrAdapterDMA1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NwhrAdapterDMA1_Type.__name__=_C
_NwhrAdapterDMA1_Object=MibTableColumn
nwhrAdapterDMA1=_NwhrAdapterDMA1_Object((1,3,6,1,4,1,23,2,27,3,10,1,15),_NwhrAdapterDMA1_Type())
nwhrAdapterDMA1.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrAdapterDMA1.setStatus(_A)
class _NwhrAdapterDMA2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NwhrAdapterDMA2_Type.__name__=_C
_NwhrAdapterDMA2_Object=MibTableColumn
nwhrAdapterDMA2=_NwhrAdapterDMA2_Object((1,3,6,1,4,1,23,2,27,3,10,1,16),_NwhrAdapterDMA2_Type())
nwhrAdapterDMA2.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrAdapterDMA2.setStatus(_A)
class _NwhrAdapterInterrupt1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NwhrAdapterInterrupt1_Type.__name__=_C
_NwhrAdapterInterrupt1_Object=MibTableColumn
nwhrAdapterInterrupt1=_NwhrAdapterInterrupt1_Object((1,3,6,1,4,1,23,2,27,3,10,1,17),_NwhrAdapterInterrupt1_Type())
nwhrAdapterInterrupt1.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrAdapterInterrupt1.setStatus(_A)
class _NwhrAdapterInterrupt2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NwhrAdapterInterrupt2_Type.__name__=_C
_NwhrAdapterInterrupt2_Object=MibTableColumn
nwhrAdapterInterrupt2=_NwhrAdapterInterrupt2_Object((1,3,6,1,4,1,23,2,27,3,10,1,18),_NwhrAdapterInterrupt2_Type())
nwhrAdapterInterrupt2.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrAdapterInterrupt2.setStatus(_A)
class _NwhrAdapterSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NwhrAdapterSlot_Type.__name__=_C
_NwhrAdapterSlot_Object=MibTableColumn
nwhrAdapterSlot=_NwhrAdapterSlot_Object((1,3,6,1,4,1,23,2,27,3,10,1,19),_NwhrAdapterSlot_Type())
nwhrAdapterSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrAdapterSlot.setStatus(_A)
_NwhrAdapterDevices_Type=Integer32
_NwhrAdapterDevices_Object=MibTableColumn
nwhrAdapterDevices=_NwhrAdapterDevices_Object((1,3,6,1,4,1,23,2,27,3,10,1,20),_NwhrAdapterDevices_Type())
nwhrAdapterDevices.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrAdapterDevices.setStatus(_A)
_NwhrMslCount_Type=Integer32
_NwhrMslCount_Object=MibScalar
nwhrMslCount=_NwhrMslCount_Object((1,3,6,1,4,1,23,2,27,3,11),_NwhrMslCount_Type())
nwhrMslCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrMslCount.setStatus(_A)
_NwhrMslTable_Object=MibTable
nwhrMslTable=_NwhrMslTable_Object((1,3,6,1,4,1,23,2,27,3,12))
if mibBuilder.loadTexts:nwhrMslTable.setStatus(_A)
_NwhrMslEntry_Object=MibTableRow
nwhrMslEntry=_NwhrMslEntry_Object((1,3,6,1,4,1,23,2,27,3,12,1))
nwhrMslEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:nwhrMslEntry.setStatus(_A)
class _NwhrMslState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('offline',1),('startup',2),('standby',3),('active',4)))
_NwhrMslState_Type.__name__=_C
_NwhrMslState_Object=MibTableColumn
nwhrMslState=_NwhrMslState_Object((1,3,6,1,4,1,23,2,27,3,12,1,1),_NwhrMslState_Type())
nwhrMslState.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrMslState.setStatus(_A)
_NwhrMslSpeed_Type=Integer32
_NwhrMslSpeed_Object=MibTableColumn
nwhrMslSpeed=_NwhrMslSpeed_Object((1,3,6,1,4,1,23,2,27,3,12,1,2),_NwhrMslSpeed_Type())
nwhrMslSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrMslSpeed.setStatus(_A)
_NwhrMslSends_Type=Counter32
_NwhrMslSends_Object=MibTableColumn
nwhrMslSends=_NwhrMslSends_Object((1,3,6,1,4,1,23,2,27,3,12,1,3),_NwhrMslSends_Type())
nwhrMslSends.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrMslSends.setStatus(_A)
_NwhrMslReceives_Type=Counter32
_NwhrMslReceives_Object=MibTableColumn
nwhrMslReceives=_NwhrMslReceives_Object((1,3,6,1,4,1,23,2,27,3,12,1,4),_NwhrMslReceives_Type())
nwhrMslReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrMslReceives.setStatus(_A)
_NwhrMslInErrors_Type=Counter32
_NwhrMslInErrors_Object=MibTableColumn
nwhrMslInErrors=_NwhrMslInErrors_Object((1,3,6,1,4,1,23,2,27,3,12,1,5),_NwhrMslInErrors_Type())
nwhrMslInErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrMslInErrors.setStatus(_A)
_NwhrMslOutErrors_Type=Counter32
_NwhrMslOutErrors_Object=MibTableColumn
nwhrMslOutErrors=_NwhrMslOutErrors_Object((1,3,6,1,4,1,23,2,27,3,12,1,6),_NwhrMslOutErrors_Type())
nwhrMslOutErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrMslOutErrors.setStatus(_A)
_NwhrPrinterTable_Object=MibTable
nwhrPrinterTable=_NwhrPrinterTable_Object((1,3,6,1,4,1,23,2,27,3,13))
if mibBuilder.loadTexts:nwhrPrinterTable.setStatus(_A)
_NwhrPrinterEntry_Object=MibTableRow
nwhrPrinterEntry=_NwhrPrinterEntry_Object((1,3,6,1,4,1,23,2,27,3,13,1))
nwhrPrinterEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:nwhrPrinterEntry.setStatus(_A)
_NwhrPrinterID_Type=Integer32
_NwhrPrinterID_Object=MibTableColumn
nwhrPrinterID=_NwhrPrinterID_Object((1,3,6,1,4,1,23,2,27,3,13,1,1),_NwhrPrinterID_Type())
nwhrPrinterID.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrPrinterID.setStatus(_A)
class _NwhrPrinterType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('local',2),('netware',3),('unixware',4)))
_NwhrPrinterType_Type.__name__=_C
_NwhrPrinterType_Object=MibTableColumn
nwhrPrinterType=_NwhrPrinterType_Object((1,3,6,1,4,1,23,2,27,3,13,1,2),_NwhrPrinterType_Type())
nwhrPrinterType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrPrinterType.setStatus(_A)
_NwhrPrinterLocalName_Type=InternationalDisplayString
_NwhrPrinterLocalName_Object=MibTableColumn
nwhrPrinterLocalName=_NwhrPrinterLocalName_Object((1,3,6,1,4,1,23,2,27,3,13,1,3),_NwhrPrinterLocalName_Type())
nwhrPrinterLocalName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrPrinterLocalName.setStatus(_A)
_NwhrPrinterQueueName_Type=InternationalDisplayString
_NwhrPrinterQueueName_Object=MibTableColumn
nwhrPrinterQueueName=_NwhrPrinterQueueName_Object((1,3,6,1,4,1,23,2,27,3,13,1,4),_NwhrPrinterQueueName_Type())
nwhrPrinterQueueName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrPrinterQueueName.setStatus(_A)
_NwhrPrinterServerName_Type=InternationalDisplayString
_NwhrPrinterServerName_Object=MibTableColumn
nwhrPrinterServerName=_NwhrPrinterServerName_Object((1,3,6,1,4,1,23,2,27,3,13,1,5),_NwhrPrinterServerName_Type())
nwhrPrinterServerName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrPrinterServerName.setStatus(_A)
_NwhrPrinterTransportDomain_Type=TransportDomain
_NwhrPrinterTransportDomain_Object=MibTableColumn
nwhrPrinterTransportDomain=_NwhrPrinterTransportDomain_Object((1,3,6,1,4,1,23,2,27,3,13,1,6),_NwhrPrinterTransportDomain_Type())
nwhrPrinterTransportDomain.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrPrinterTransportDomain.setStatus(_A)
_NwhrPrinterTransportAddress_Type=TransportAddress
_NwhrPrinterTransportAddress_Object=MibTableColumn
nwhrPrinterTransportAddress=_NwhrPrinterTransportAddress_Object((1,3,6,1,4,1,23,2,27,3,13,1,7),_NwhrPrinterTransportAddress_Type())
nwhrPrinterTransportAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrPrinterTransportAddress.setStatus(_A)
class _NwhrPrinterDeviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NwhrPrinterDeviceIndex_Type.__name__=_C
_NwhrPrinterDeviceIndex_Object=MibTableColumn
nwhrPrinterDeviceIndex=_NwhrPrinterDeviceIndex_Object((1,3,6,1,4,1,23,2,27,3,13,1,8),_NwhrPrinterDeviceIndex_Type())
nwhrPrinterDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrPrinterDeviceIndex.setStatus(_A)
_NwhrOdi_ObjectIdentity=ObjectIdentity
nwhrOdi=_NwhrOdi_ObjectIdentity((1,3,6,1,4,1,23,2,27,10))
_NwhrLslOutPkts_Type=Counter32
_NwhrLslOutPkts_Object=MibScalar
nwhrLslOutPkts=_NwhrLslOutPkts_Object((1,3,6,1,4,1,23,2,27,10,1),_NwhrLslOutPkts_Type())
nwhrLslOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrLslOutPkts.setStatus(_A)
_NwhrLslInPkts_Type=Counter32
_NwhrLslInPkts_Object=MibScalar
nwhrLslInPkts=_NwhrLslInPkts_Object((1,3,6,1,4,1,23,2,27,10,2),_NwhrLslInPkts_Type())
nwhrLslInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrLslInPkts.setStatus(_A)
_NwhrLslUnclaimedPkts_Type=Counter32
_NwhrLslUnclaimedPkts_Object=MibScalar
nwhrLslUnclaimedPkts=_NwhrLslUnclaimedPkts_Object((1,3,6,1,4,1,23,2,27,10,3),_NwhrLslUnclaimedPkts_Type())
nwhrLslUnclaimedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrLslUnclaimedPkts.setStatus(_A)
_NwhrProtocolTable_Object=MibTable
nwhrProtocolTable=_NwhrProtocolTable_Object((1,3,6,1,4,1,23,2,27,10,4))
if mibBuilder.loadTexts:nwhrProtocolTable.setStatus(_A)
_NwhrProtocolEntry_Object=MibTableRow
nwhrProtocolEntry=_NwhrProtocolEntry_Object((1,3,6,1,4,1,23,2,27,10,4,1))
nwhrProtocolEntry.setIndexNames((0,_D,_L),(0,_D,_M))
if mibBuilder.loadTexts:nwhrProtocolEntry.setStatus(_A)
class _NwhrProtocolName_Type(InternationalDisplayString):subtypeSpec=InternationalDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_NwhrProtocolName_Type.__name__=_G
_NwhrProtocolName_Object=MibTableColumn
nwhrProtocolName=_NwhrProtocolName_Object((1,3,6,1,4,1,23,2,27,10,4,1,1),_NwhrProtocolName_Type())
nwhrProtocolName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrProtocolName.setStatus(_A)
class _NwhrProtocolID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_NwhrProtocolID_Type.__name__=_I
_NwhrProtocolID_Object=MibTableColumn
nwhrProtocolID=_NwhrProtocolID_Object((1,3,6,1,4,1,23,2,27,10,4,1,2),_NwhrProtocolID_Type())
nwhrProtocolID.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrProtocolID.setStatus(_A)
_NwhrProtocolAddress_Type=InternationalDisplayString
_NwhrProtocolAddress_Object=MibTableColumn
nwhrProtocolAddress=_NwhrProtocolAddress_Object((1,3,6,1,4,1,23,2,27,10,4,1,3),_NwhrProtocolAddress_Type())
nwhrProtocolAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrProtocolAddress.setStatus(_A)
_NwhrProtocolOutPkts_Type=Counter32
_NwhrProtocolOutPkts_Object=MibTableColumn
nwhrProtocolOutPkts=_NwhrProtocolOutPkts_Object((1,3,6,1,4,1,23,2,27,10,4,1,4),_NwhrProtocolOutPkts_Type())
nwhrProtocolOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrProtocolOutPkts.setStatus(_A)
_NwhrProtocolInPkts_Type=Counter32
_NwhrProtocolInPkts_Object=MibTableColumn
nwhrProtocolInPkts=_NwhrProtocolInPkts_Object((1,3,6,1,4,1,23,2,27,10,4,1,5),_NwhrProtocolInPkts_Type())
nwhrProtocolInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrProtocolInPkts.setStatus(_A)
_NwhrProtocolIgnoredPkts_Type=Counter32
_NwhrProtocolIgnoredPkts_Object=MibTableColumn
nwhrProtocolIgnoredPkts=_NwhrProtocolIgnoredPkts_Object((1,3,6,1,4,1,23,2,27,10,4,1,6),_NwhrProtocolIgnoredPkts_Type())
nwhrProtocolIgnoredPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrProtocolIgnoredPkts.setStatus(_A)
_NwhrProtocolFullName_Type=InternationalDisplayString
_NwhrProtocolFullName_Object=MibTableColumn
nwhrProtocolFullName=_NwhrProtocolFullName_Object((1,3,6,1,4,1,23,2,27,10,4,1,7),_NwhrProtocolFullName_Type())
nwhrProtocolFullName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrProtocolFullName.setStatus(_A)
_PysmiFakeCol2_Type=Integer32
_PysmiFakeCol2_Object=MibTableColumn
pysmiFakeCol2=_PysmiFakeCol2_Object((1,3,6,1,4,1,23,2,27,10,4,1,4294967295),_PysmiFakeCol2_Type())
pysmiFakeCol2.setMaxAccess(_N)
if mibBuilder.loadTexts:pysmiFakeCol2.setStatus(_A)
_NwhrIfTable_Object=MibTable
nwhrIfTable=_NwhrIfTable_Object((1,3,6,1,4,1,23,2,27,10,5))
if mibBuilder.loadTexts:nwhrIfTable.setStatus(_A)
_NwhrIfEntry_Object=MibTableRow
nwhrIfEntry=_NwhrIfEntry_Object((1,3,6,1,4,1,23,2,27,10,5,1))
nwhrIfEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:nwhrIfEntry.setStatus(_A)
_NwhrIfLogicalBoardNumber_Type=Integer32
_NwhrIfLogicalBoardNumber_Object=MibTableColumn
nwhrIfLogicalBoardNumber=_NwhrIfLogicalBoardNumber_Object((1,3,6,1,4,1,23,2,27,10,5,1,1),_NwhrIfLogicalBoardNumber_Type())
nwhrIfLogicalBoardNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrIfLogicalBoardNumber.setStatus(_A)
_NwhrIfFrameType_Type=InternationalDisplayString
_NwhrIfFrameType_Object=MibTableColumn
nwhrIfFrameType=_NwhrIfFrameType_Object((1,3,6,1,4,1,23,2,27,10,5,1,2),_NwhrIfFrameType_Type())
nwhrIfFrameType.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrIfFrameType.setStatus(_A)
class _NwhrIfLogicalBoardName_Type(InternationalDisplayString):subtypeSpec=InternationalDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,18))
_NwhrIfLogicalBoardName_Type.__name__=_G
_NwhrIfLogicalBoardName_Object=MibTableColumn
nwhrIfLogicalBoardName=_NwhrIfLogicalBoardName_Object((1,3,6,1,4,1,23,2,27,10,5,1,3),_NwhrIfLogicalBoardName_Type())
nwhrIfLogicalBoardName.setMaxAccess(_B)
if mibBuilder.loadTexts:nwhrIfLogicalBoardName.setStatus(_A)
_PysmiFakeCol3_Type=Integer32
_PysmiFakeCol3_Object=MibTableColumn
pysmiFakeCol3=_PysmiFakeCol3_Object((1,3,6,1,4,1,23,2,27,10,5,1,4294967295),_PysmiFakeCol3_Type())
pysmiFakeCol3.setMaxAccess(_N)
if mibBuilder.loadTexts:pysmiFakeCol3.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'TransportDomain':TransportDomain,'TransportAddress':TransportAddress,'KBytes':KBytes,_G:InternationalDisplayString,'novell':novell,'mibDoc':mibDoc,'nwHostExtensions':nwHostExtensions,'nwhrStorage':nwhrStorage,'nwhrStorageTypes':nwhrStorageTypes,'nwhrStorageVolume':nwhrStorageVolume,'nwhrStorageMemoryPermanent':nwhrStorageMemoryPermanent,'nwhrStorageMemoryAlloc':nwhrStorageMemoryAlloc,'nwhrStorageCacheBuffers':nwhrStorageCacheBuffers,'nwhrStorageCacheMovable':nwhrStorageCacheMovable,'nwhrStorageCacheNonMovable':nwhrStorageCacheNonMovable,'nwhrStorageCodeAndDataMemory':nwhrStorageCodeAndDataMemory,'nwhrStorageDOSMemory':nwhrStorageDOSMemory,'nwhrStorageIOEngineMemory':nwhrStorageIOEngineMemory,'nwhrStorageMSEngineMemory':nwhrStorageMSEngineMemory,'nwhrStorageUnclaimedMemory':nwhrStorageUnclaimedMemory,'nwhrDevice':nwhrDevice,'nwhrDeviceTypes':nwhrDeviceTypes,'nwhrDeviceMirroredServerLink':nwhrDeviceMirroredServerLink,'nwhrDeviceTable':nwhrDeviceTable,'nwhrDeviceEntry':nwhrDeviceEntry,'nwhrDeviceAdapterIndex':nwhrDeviceAdapterIndex,'nwhrDeviceControllerNumber':nwhrDeviceControllerNumber,'nwhrDeviceNumber':nwhrDeviceNumber,'nwhrProcessorCount':nwhrProcessorCount,'nwhrPrinterCount':nwhrPrinterCount,'nwhrDiskStorageCount':nwhrDiskStorageCount,'nwhrDiskStorageTable':nwhrDiskStorageTable,'nwhrDiskStorageEntry':nwhrDiskStorageEntry,'nwhrDiskStorageHeads':nwhrDiskStorageHeads,'nwhrDiskStorageCylinders':nwhrDiskStorageCylinders,'nwhrDiskStorageSectorsPerTrack':nwhrDiskStorageSectorsPerTrack,'nwhrDiskStorageSectorSize':nwhrDiskStorageSectorSize,'nwhrDiskStorageBlockSize':nwhrDiskStorageBlockSize,'nwhrPhysicalPartitionTable':nwhrPhysicalPartitionTable,'nwhrPhysicalPartitionEntry':nwhrPhysicalPartitionEntry,_H:nwhrPhysicalPartitionIndex,'nwhrPhysicalPartitionType':nwhrPhysicalPartitionType,'nwhrPhysicalPartitionDescr':nwhrPhysicalPartitionDescr,'nwhrPhysicalPartitionSize':nwhrPhysicalPartitionSize,'nwhrHotfixTable':nwhrHotfixTable,'nwhrHotfixEntry':nwhrHotfixEntry,'nwhrHotfixUnits':nwhrHotfixUnits,'nwhrHotfixTotal':nwhrHotfixTotal,'nwhrHotfixUsed':nwhrHotfixUsed,'nwhrHotfixReserved':nwhrHotfixReserved,'nwhrAdapterCount':nwhrAdapterCount,'nwhrAdapterTable':nwhrAdapterTable,'nwhrAdapterEntry':nwhrAdapterEntry,_J:nwhrAdapterIndex,'nwhrAdapterType':nwhrAdapterType,'nwhrAdapterDescr':nwhrAdapterDescr,'nwhrAdapterDriverDescr':nwhrAdapterDriverDescr,'nwhrAdapterDriverMajorVer':nwhrAdapterDriverMajorVer,'nwhrAdapterDriverMinorVer':nwhrAdapterDriverMinorVer,'nwhrAdapterPort1':nwhrAdapterPort1,'nwhrAdapterPort1Len':nwhrAdapterPort1Len,'nwhrAdapterPort2':nwhrAdapterPort2,'nwhrAdapterPort2Len':nwhrAdapterPort2Len,'nwhrAdapterMem1':nwhrAdapterMem1,'nwhrAdapterMem1Len':nwhrAdapterMem1Len,'nwhrAdapterMem2':nwhrAdapterMem2,'nwhrAdapterMem2Len':nwhrAdapterMem2Len,'nwhrAdapterDMA1':nwhrAdapterDMA1,'nwhrAdapterDMA2':nwhrAdapterDMA2,'nwhrAdapterInterrupt1':nwhrAdapterInterrupt1,'nwhrAdapterInterrupt2':nwhrAdapterInterrupt2,'nwhrAdapterSlot':nwhrAdapterSlot,'nwhrAdapterDevices':nwhrAdapterDevices,'nwhrMslCount':nwhrMslCount,'nwhrMslTable':nwhrMslTable,'nwhrMslEntry':nwhrMslEntry,'nwhrMslState':nwhrMslState,'nwhrMslSpeed':nwhrMslSpeed,'nwhrMslSends':nwhrMslSends,'nwhrMslReceives':nwhrMslReceives,'nwhrMslInErrors':nwhrMslInErrors,'nwhrMslOutErrors':nwhrMslOutErrors,'nwhrPrinterTable':nwhrPrinterTable,'nwhrPrinterEntry':nwhrPrinterEntry,_K:nwhrPrinterID,'nwhrPrinterType':nwhrPrinterType,'nwhrPrinterLocalName':nwhrPrinterLocalName,'nwhrPrinterQueueName':nwhrPrinterQueueName,'nwhrPrinterServerName':nwhrPrinterServerName,'nwhrPrinterTransportDomain':nwhrPrinterTransportDomain,'nwhrPrinterTransportAddress':nwhrPrinterTransportAddress,'nwhrPrinterDeviceIndex':nwhrPrinterDeviceIndex,'nwhrOdi':nwhrOdi,'nwhrLslOutPkts':nwhrLslOutPkts,'nwhrLslInPkts':nwhrLslInPkts,'nwhrLslUnclaimedPkts':nwhrLslUnclaimedPkts,'nwhrProtocolTable':nwhrProtocolTable,'nwhrProtocolEntry':nwhrProtocolEntry,_M:nwhrProtocolName,'nwhrProtocolID':nwhrProtocolID,'nwhrProtocolAddress':nwhrProtocolAddress,'nwhrProtocolOutPkts':nwhrProtocolOutPkts,'nwhrProtocolInPkts':nwhrProtocolInPkts,'nwhrProtocolIgnoredPkts':nwhrProtocolIgnoredPkts,'nwhrProtocolFullName':nwhrProtocolFullName,_L:pysmiFakeCol2,'nwhrIfTable':nwhrIfTable,'nwhrIfEntry':nwhrIfEntry,'nwhrIfLogicalBoardNumber':nwhrIfLogicalBoardNumber,'nwhrIfFrameType':nwhrIfFrameType,'nwhrIfLogicalBoardName':nwhrIfLogicalBoardName,_O:pysmiFakeCol3})