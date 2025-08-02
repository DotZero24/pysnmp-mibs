_H='Kbytes / sec'
_G='storageRaidIndex'
_F='storageDeviceIndex'
_E='read-write'
_D='LEFTHAND-NETWORKS-NUS-COMMON-STORAGE-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lhnModules,=mibBuilder.importSymbols('LEFTHAND-NETWORKS-GLOBAL-REG','lhnModules')
lhnNusCommonStorage,=mibBuilder.importSymbols('LEFTHAND-NETWORKS-NUS-COMMON-MIB','lhnNusCommonStorage')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
lhnNusCommonStorageModule=ModuleIdentity((1,3,6,1,4,1,9804,1,1,8))
_StorageDeviceCount_Type=Integer32
_StorageDeviceCount_Object=MibScalar
storageDeviceCount=_StorageDeviceCount_Object((1,3,6,1,4,1,9804,3,1,1,2,4,1),_StorageDeviceCount_Type())
storageDeviceCount.setMaxAccess(_B)
if mibBuilder.loadTexts:storageDeviceCount.setStatus(_A)
_StorageDeviceTable_Object=MibTable
storageDeviceTable=_StorageDeviceTable_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2))
if mibBuilder.loadTexts:storageDeviceTable.setStatus(_A)
_StorageDeviceEntry_Object=MibTableRow
storageDeviceEntry=_StorageDeviceEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1))
storageDeviceEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:storageDeviceEntry.setStatus(_A)
_StorageDeviceIndex_Type=Integer32
_StorageDeviceIndex_Object=MibTableColumn
storageDeviceIndex=_StorageDeviceIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,1),_StorageDeviceIndex_Type())
storageDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:storageDeviceIndex.setStatus(_A)
_StorageDeviceModel_Type=OctetString
_StorageDeviceModel_Object=MibTableColumn
storageDeviceModel=_StorageDeviceModel_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,2),_StorageDeviceModel_Type())
storageDeviceModel.setMaxAccess(_B)
if mibBuilder.loadTexts:storageDeviceModel.setStatus(_A)
_StorageDeviceClass_Type=OctetString
_StorageDeviceClass_Object=MibTableColumn
storageDeviceClass=_StorageDeviceClass_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,3),_StorageDeviceClass_Type())
storageDeviceClass.setMaxAccess(_B)
if mibBuilder.loadTexts:storageDeviceClass.setStatus(_A)
_StorageDeviceCapacity_Type=Counter64
_StorageDeviceCapacity_Object=MibTableColumn
storageDeviceCapacity=_StorageDeviceCapacity_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,4),_StorageDeviceCapacity_Type())
storageDeviceCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:storageDeviceCapacity.setStatus(_A)
if mibBuilder.loadTexts:storageDeviceCapacity.setUnits('Blocks (512 bytes)')
_StorageDeviceStatus_Type=OctetString
_StorageDeviceStatus_Object=MibTableColumn
storageDeviceStatus=_StorageDeviceStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,5),_StorageDeviceStatus_Type())
storageDeviceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:storageDeviceStatus.setStatus(_A)
_StorageDeviceChain_Type=OctetString
_StorageDeviceChain_Object=MibTableColumn
storageDeviceChain=_StorageDeviceChain_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,6),_StorageDeviceChain_Type())
storageDeviceChain.setMaxAccess(_B)
if mibBuilder.loadTexts:storageDeviceChain.setStatus(_A)
_StorageDeviceSerialNo_Type=OctetString
_StorageDeviceSerialNo_Object=MibTableColumn
storageDeviceSerialNo=_StorageDeviceSerialNo_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,7),_StorageDeviceSerialNo_Type())
storageDeviceSerialNo.setMaxAccess(_B)
if mibBuilder.loadTexts:storageDeviceSerialNo.setStatus(_A)
_StorageDeviceBayStatus_Type=OctetString
_StorageDeviceBayStatus_Object=MibTableColumn
storageDeviceBayStatus=_StorageDeviceBayStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,8),_StorageDeviceBayStatus_Type())
storageDeviceBayStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:storageDeviceBayStatus.setStatus(_A)
_StorageDeviceTemperature_Type=Integer32
_StorageDeviceTemperature_Object=MibTableColumn
storageDeviceTemperature=_StorageDeviceTemperature_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,9),_StorageDeviceTemperature_Type())
storageDeviceTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:storageDeviceTemperature.setStatus(_A)
_StorageRaidCount_Type=Integer32
_StorageRaidCount_Object=MibScalar
storageRaidCount=_StorageRaidCount_Object((1,3,6,1,4,1,9804,3,1,1,2,4,3),_StorageRaidCount_Type())
storageRaidCount.setMaxAccess(_B)
if mibBuilder.loadTexts:storageRaidCount.setStatus(_A)
_StorageRaidTable_Object=MibTable
storageRaidTable=_StorageRaidTable_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4))
if mibBuilder.loadTexts:storageRaidTable.setStatus(_A)
_StorageRaidEntry_Object=MibTableRow
storageRaidEntry=_StorageRaidEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1))
storageRaidEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:storageRaidEntry.setStatus(_A)
_StorageRaidIndex_Type=Integer32
_StorageRaidIndex_Object=MibTableColumn
storageRaidIndex=_StorageRaidIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1,1),_StorageRaidIndex_Type())
storageRaidIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:storageRaidIndex.setStatus(_A)
_StorageRaidDeviceName_Type=OctetString
_StorageRaidDeviceName_Object=MibTableColumn
storageRaidDeviceName=_StorageRaidDeviceName_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1,2),_StorageRaidDeviceName_Type())
storageRaidDeviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:storageRaidDeviceName.setStatus(_A)
_StorageRaidLevel_Type=Integer32
_StorageRaidLevel_Object=MibTableColumn
storageRaidLevel=_StorageRaidLevel_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1,3),_StorageRaidLevel_Type())
storageRaidLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:storageRaidLevel.setStatus(_A)
_StorageRaidDiskCount_Type=Integer32
_StorageRaidDiskCount_Object=MibTableColumn
storageRaidDiskCount=_StorageRaidDiskCount_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1,4),_StorageRaidDiskCount_Type())
storageRaidDiskCount.setMaxAccess(_B)
if mibBuilder.loadTexts:storageRaidDiskCount.setStatus(_A)
_StorageRaidSpareDiskCount_Type=Integer32
_StorageRaidSpareDiskCount_Object=MibTableColumn
storageRaidSpareDiskCount=_StorageRaidSpareDiskCount_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1,5),_StorageRaidSpareDiskCount_Type())
storageRaidSpareDiskCount.setMaxAccess(_B)
if mibBuilder.loadTexts:storageRaidSpareDiskCount.setStatus(_A)
_StorageRaidSuperBlock_Type=TruthValue
_StorageRaidSuperBlock_Object=MibTableColumn
storageRaidSuperBlock=_StorageRaidSuperBlock_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1,6),_StorageRaidSuperBlock_Type())
storageRaidSuperBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:storageRaidSuperBlock.setStatus(_A)
_StorageRaidChunkSize_Type=Integer32
_StorageRaidChunkSize_Object=MibTableColumn
storageRaidChunkSize=_StorageRaidChunkSize_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1,7),_StorageRaidChunkSize_Type())
storageRaidChunkSize.setMaxAccess(_B)
if mibBuilder.loadTexts:storageRaidChunkSize.setStatus(_A)
if mibBuilder.loadTexts:storageRaidChunkSize.setUnits('Kbytes')
_StorageRaidDisks_Type=OctetString
_StorageRaidDisks_Object=MibTableColumn
storageRaidDisks=_StorageRaidDisks_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1,8),_StorageRaidDisks_Type())
storageRaidDisks.setMaxAccess(_B)
if mibBuilder.loadTexts:storageRaidDisks.setStatus(_A)
class _StorageRaidConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noRaid',1),('stripe',2),('mirror',3),('mirrorAndStripe',4)))
_StorageRaidConfiguration_Type.__name__=_C
_StorageRaidConfiguration_Object=MibScalar
storageRaidConfiguration=_StorageRaidConfiguration_Object((1,3,6,1,4,1,9804,3,1,1,2,4,5),_StorageRaidConfiguration_Type())
storageRaidConfiguration.setMaxAccess(_E)
if mibBuilder.loadTexts:storageRaidConfiguration.setStatus(_A)
class _StorageRaidStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('normal',1),('rebuilding',2),('degraded',3),('notRebuilding',4),('off',5)))
_StorageRaidStatus_Type.__name__=_C
_StorageRaidStatus_Object=MibScalar
storageRaidStatus=_StorageRaidStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,4,7),_StorageRaidStatus_Type())
storageRaidStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:storageRaidStatus.setStatus(_A)
_StorageRaidMinimumSpeed_Type=Integer32
_StorageRaidMinimumSpeed_Object=MibScalar
storageRaidMinimumSpeed=_StorageRaidMinimumSpeed_Object((1,3,6,1,4,1,9804,3,1,1,2,4,8),_StorageRaidMinimumSpeed_Type())
storageRaidMinimumSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:storageRaidMinimumSpeed.setStatus(_A)
if mibBuilder.loadTexts:storageRaidMinimumSpeed.setUnits(_H)
_StorageRaidMaximumSpeed_Type=Integer32
_StorageRaidMaximumSpeed_Object=MibScalar
storageRaidMaximumSpeed=_StorageRaidMaximumSpeed_Object((1,3,6,1,4,1,9804,3,1,1,2,4,9),_StorageRaidMaximumSpeed_Type())
storageRaidMaximumSpeed.setMaxAccess(_E)
if mibBuilder.loadTexts:storageRaidMaximumSpeed.setStatus(_A)
if mibBuilder.loadTexts:storageRaidMaximumSpeed.setUnits(_H)
mibBuilder.exportSymbols(_D,**{'lhnNusCommonStorageModule':lhnNusCommonStorageModule,'storageDeviceCount':storageDeviceCount,'storageDeviceTable':storageDeviceTable,'storageDeviceEntry':storageDeviceEntry,_F:storageDeviceIndex,'storageDeviceModel':storageDeviceModel,'storageDeviceClass':storageDeviceClass,'storageDeviceCapacity':storageDeviceCapacity,'storageDeviceStatus':storageDeviceStatus,'storageDeviceChain':storageDeviceChain,'storageDeviceSerialNo':storageDeviceSerialNo,'storageDeviceBayStatus':storageDeviceBayStatus,'storageDeviceTemperature':storageDeviceTemperature,'storageRaidCount':storageRaidCount,'storageRaidTable':storageRaidTable,'storageRaidEntry':storageRaidEntry,_G:storageRaidIndex,'storageRaidDeviceName':storageRaidDeviceName,'storageRaidLevel':storageRaidLevel,'storageRaidDiskCount':storageRaidDiskCount,'storageRaidSpareDiskCount':storageRaidSpareDiskCount,'storageRaidSuperBlock':storageRaidSuperBlock,'storageRaidChunkSize':storageRaidChunkSize,'storageRaidDisks':storageRaidDisks,'storageRaidConfiguration':storageRaidConfiguration,'storageRaidStatus':storageRaidStatus,'storageRaidMinimumSpeed':storageRaidMinimumSpeed,'storageRaidMaximumSpeed':storageRaidMaximumSpeed})