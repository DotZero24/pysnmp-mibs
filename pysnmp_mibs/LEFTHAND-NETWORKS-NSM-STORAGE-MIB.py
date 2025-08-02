_AM='lefthandNetworksNsmStorageGroup'
_AL='storageOsRaidRowStatus'
_AK='storageOsRaidMode'
_AJ='storageRaidDeviceRowStatus'
_AI='storageRaidParityInitState'
_AH='storageRaidChunkSize'
_AG='storageRaidSuperBlock'
_AF='storageRaidSpareDiskCount'
_AE='storageDeviceRowStatus'
_AD='storageDeviceChain'
_AC='storageDeviceCapacityInBytes'
_AB='storageOsRaidState'
_AA='storageOsRaidSize'
_A9='storageOsRaidDevice'
_A8='storageOsRaidName'
_A7='storageOsRaidCount'
_A6='storageRaidStatsIoLatencyWrite'
_A5='storageRaidStatsIoLatencyRead'
_A4='storageRaidStatsQDepthTotal'
_A3='storageRaidStatsKbytesWrite'
_A2='storageRaidStatsKbytesRead'
_A1='storageRaidStatsIOsWrite'
_A0='storageRaidStatsIOsRead'
_z='storageRaidMaximumSpeed'
_y='storageRaidMinimumSpeed'
_x='storageRaidState'
_w='storageRaidStatus'
_v='storageRaidCapacity'
_u='storageRaidMode'
_t='storageRaidDescription'
_s='storageRaidDeviceStatus'
_r='storageRaidDeviceState'
_q='storageRaidRebuildTime'
_p='storageRaidRebuildPercent'
_o='storageRaidDeviceParityInitState'
_n='storageRaidDeviceCapacity'
_m='storageRaidDevice'
_l='storageRaidDisks'
_k='storageRaidDiskCount'
_j='storageRaidLevel'
_i='storageRaidDeviceName'
_h='storageRaidCount'
_g='storageDeviceStatus'
_f='storageDeviceState'
_e='storageDeviceHotRemovable'
_d='storageDeviceCapacity'
_c='storageDeviceSmartHealthStatus'
_b='storageDeviceSmartHealth'
_a='storageDeviceFirmwareVersion'
_Z='storageDeviceRaidDevice'
_Y='storageDeviceName'
_X='storageDeviceLabel'
_W='storageDeviceTemperatureStatus'
_V='storageDeviceTemperatureLimit'
_U='storageDeviceTemperatureCritical'
_T='storageDeviceTemperature'
_S='storageDeviceSerialNumber'
_R='storageDeviceMode'
_Q='storageDeviceClass'
_P='storageDeviceModel'
_O='storageDeviceCount'
_N='storageOsRaidIndex'
_M='storageRaidIndex'
_L='storageDeviceIndex'
_K='operations'
_J='Celsius'
_I='not-accessible'
_H='MB'
_G='fail'
_F='pass'
_E='Integer32'
_D='obsolete'
_C='read-only'
_B='current'
_A='LEFTHAND-NETWORKS-NSM-STORAGE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
lhnModules,lhnNsm=mibBuilder.importSymbols('LEFTHAND-NETWORKS-GLOBAL-REG-MIB','lhnModules','lhnNsm')
lhnNsmStorage,=mibBuilder.importSymbols('LEFTHAND-NETWORKS-NSM-MIB','lhnNsmStorage')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
lhnNsmStorageModule=ModuleIdentity((1,3,6,1,4,1,9804,2,1,5))
if mibBuilder.loadTexts:lhnNsmStorageModule.setRevisions(('2013-11-21 00:00','2013-06-25 00:00','2012-09-04 00:00','2011-06-21 00:00','2010-09-07 00:00','2010-07-19 00:00','2009-11-20 00:00','2009-03-10 00:00','2008-01-24 00:00'))
_LhnNsmStorageModuleConformance_ObjectIdentity=ObjectIdentity
lhnNsmStorageModuleConformance=_LhnNsmStorageModuleConformance_ObjectIdentity((1,3,6,1,4,1,9804,2,1,5,1))
_LhnNsmStorageModuleCompliances_ObjectIdentity=ObjectIdentity
lhnNsmStorageModuleCompliances=_LhnNsmStorageModuleCompliances_ObjectIdentity((1,3,6,1,4,1,9804,2,1,5,1,1))
_LhnNsmStorageModuleGroups_ObjectIdentity=ObjectIdentity
lhnNsmStorageModuleGroups=_LhnNsmStorageModuleGroups_ObjectIdentity((1,3,6,1,4,1,9804,2,1,5,1,2))
_StorageDeviceCount_Type=Integer32
_StorageDeviceCount_Object=MibScalar
storageDeviceCount=_StorageDeviceCount_Object((1,3,6,1,4,1,9804,3,1,1,2,4,1),_StorageDeviceCount_Type())
storageDeviceCount.setMaxAccess(_C)
if mibBuilder.loadTexts:storageDeviceCount.setStatus(_B)
_StorageDeviceTable_Object=MibTable
storageDeviceTable=_StorageDeviceTable_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2))
if mibBuilder.loadTexts:storageDeviceTable.setStatus(_B)
_StorageDeviceEntry_Object=MibTableRow
storageDeviceEntry=_StorageDeviceEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1))
storageDeviceEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:storageDeviceEntry.setStatus(_B)
_StorageDeviceIndex_Type=Unsigned32
_StorageDeviceIndex_Object=MibTableColumn
storageDeviceIndex=_StorageDeviceIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,1),_StorageDeviceIndex_Type())
storageDeviceIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:storageDeviceIndex.setStatus(_B)
_StorageDeviceModel_Type=DisplayString
_StorageDeviceModel_Object=MibTableColumn
storageDeviceModel=_StorageDeviceModel_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,2),_StorageDeviceModel_Type())
storageDeviceModel.setMaxAccess(_C)
if mibBuilder.loadTexts:storageDeviceModel.setStatus(_B)
_StorageDeviceClass_Type=DisplayString
_StorageDeviceClass_Object=MibTableColumn
storageDeviceClass=_StorageDeviceClass_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,3),_StorageDeviceClass_Type())
storageDeviceClass.setMaxAccess(_C)
if mibBuilder.loadTexts:storageDeviceClass.setStatus(_B)
_StorageDeviceCapacityInBytes_Type=CounterBasedGauge64
_StorageDeviceCapacityInBytes_Object=MibTableColumn
storageDeviceCapacityInBytes=_StorageDeviceCapacityInBytes_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,4),_StorageDeviceCapacityInBytes_Type())
storageDeviceCapacityInBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:storageDeviceCapacityInBytes.setStatus(_D)
if mibBuilder.loadTexts:storageDeviceCapacityInBytes.setUnits('Blocks (512 bytes)')
_StorageDeviceMode_Type=DisplayString
_StorageDeviceMode_Object=MibTableColumn
storageDeviceMode=_StorageDeviceMode_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,5),_StorageDeviceMode_Type())
storageDeviceMode.setMaxAccess(_C)
if mibBuilder.loadTexts:storageDeviceMode.setStatus(_B)
_StorageDeviceChain_Type=DisplayString
_StorageDeviceChain_Object=MibTableColumn
storageDeviceChain=_StorageDeviceChain_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,6),_StorageDeviceChain_Type())
storageDeviceChain.setMaxAccess(_C)
if mibBuilder.loadTexts:storageDeviceChain.setStatus(_D)
_StorageDeviceSerialNumber_Type=DisplayString
_StorageDeviceSerialNumber_Object=MibTableColumn
storageDeviceSerialNumber=_StorageDeviceSerialNumber_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,7),_StorageDeviceSerialNumber_Type())
storageDeviceSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:storageDeviceSerialNumber.setStatus(_B)
_StorageDeviceTemperature_Type=Gauge32
_StorageDeviceTemperature_Object=MibTableColumn
storageDeviceTemperature=_StorageDeviceTemperature_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,9),_StorageDeviceTemperature_Type())
storageDeviceTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:storageDeviceTemperature.setStatus(_B)
if mibBuilder.loadTexts:storageDeviceTemperature.setUnits(_J)
_StorageDeviceTemperatureCritical_Type=Integer32
_StorageDeviceTemperatureCritical_Object=MibTableColumn
storageDeviceTemperatureCritical=_StorageDeviceTemperatureCritical_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,10),_StorageDeviceTemperatureCritical_Type())
storageDeviceTemperatureCritical.setMaxAccess(_C)
if mibBuilder.loadTexts:storageDeviceTemperatureCritical.setStatus(_B)
if mibBuilder.loadTexts:storageDeviceTemperatureCritical.setUnits(_J)
_StorageDeviceTemperatureLimit_Type=Integer32
_StorageDeviceTemperatureLimit_Object=MibTableColumn
storageDeviceTemperatureLimit=_StorageDeviceTemperatureLimit_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,11),_StorageDeviceTemperatureLimit_Type())
storageDeviceTemperatureLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:storageDeviceTemperatureLimit.setStatus(_B)
if mibBuilder.loadTexts:storageDeviceTemperatureLimit.setUnits(_J)
class _StorageDeviceTemperatureStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_StorageDeviceTemperatureStatus_Type.__name__=_E
_StorageDeviceTemperatureStatus_Object=MibTableColumn
storageDeviceTemperatureStatus=_StorageDeviceTemperatureStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,12),_StorageDeviceTemperatureStatus_Type())
storageDeviceTemperatureStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:storageDeviceTemperatureStatus.setStatus(_B)
_StorageDeviceLabel_Type=DisplayString
_StorageDeviceLabel_Object=MibTableColumn
storageDeviceLabel=_StorageDeviceLabel_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,13),_StorageDeviceLabel_Type())
storageDeviceLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:storageDeviceLabel.setStatus(_B)
_StorageDeviceName_Type=DisplayString
_StorageDeviceName_Object=MibTableColumn
storageDeviceName=_StorageDeviceName_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,14),_StorageDeviceName_Type())
storageDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:storageDeviceName.setStatus(_B)
_StorageDeviceRaidDevice_Type=DisplayString
_StorageDeviceRaidDevice_Object=MibTableColumn
storageDeviceRaidDevice=_StorageDeviceRaidDevice_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,15),_StorageDeviceRaidDevice_Type())
storageDeviceRaidDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:storageDeviceRaidDevice.setStatus(_B)
_StorageDeviceFirmwareVersion_Type=DisplayString
_StorageDeviceFirmwareVersion_Object=MibTableColumn
storageDeviceFirmwareVersion=_StorageDeviceFirmwareVersion_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,16),_StorageDeviceFirmwareVersion_Type())
storageDeviceFirmwareVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:storageDeviceFirmwareVersion.setStatus(_B)
_StorageDeviceSmartHealth_Type=DisplayString
_StorageDeviceSmartHealth_Object=MibTableColumn
storageDeviceSmartHealth=_StorageDeviceSmartHealth_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,17),_StorageDeviceSmartHealth_Type())
storageDeviceSmartHealth.setMaxAccess(_C)
if mibBuilder.loadTexts:storageDeviceSmartHealth.setStatus(_B)
class _StorageDeviceSmartHealthStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_StorageDeviceSmartHealthStatus_Type.__name__=_E
_StorageDeviceSmartHealthStatus_Object=MibTableColumn
storageDeviceSmartHealthStatus=_StorageDeviceSmartHealthStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,18),_StorageDeviceSmartHealthStatus_Type())
storageDeviceSmartHealthStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:storageDeviceSmartHealthStatus.setStatus(_B)
_StorageDeviceCapacity_Type=Integer32
_StorageDeviceCapacity_Object=MibTableColumn
storageDeviceCapacity=_StorageDeviceCapacity_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,19),_StorageDeviceCapacity_Type())
storageDeviceCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:storageDeviceCapacity.setStatus(_B)
if mibBuilder.loadTexts:storageDeviceCapacity.setUnits(_H)
_StorageDeviceHotRemovable_Type=TruthValue
_StorageDeviceHotRemovable_Object=MibTableColumn
storageDeviceHotRemovable=_StorageDeviceHotRemovable_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,20),_StorageDeviceHotRemovable_Type())
storageDeviceHotRemovable.setMaxAccess(_C)
if mibBuilder.loadTexts:storageDeviceHotRemovable.setStatus(_B)
_StorageDeviceState_Type=DisplayString
_StorageDeviceState_Object=MibTableColumn
storageDeviceState=_StorageDeviceState_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,90),_StorageDeviceState_Type())
storageDeviceState.setMaxAccess(_C)
if mibBuilder.loadTexts:storageDeviceState.setStatus(_B)
class _StorageDeviceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_StorageDeviceStatus_Type.__name__=_E
_StorageDeviceStatus_Object=MibTableColumn
storageDeviceStatus=_StorageDeviceStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,91),_StorageDeviceStatus_Type())
storageDeviceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:storageDeviceStatus.setStatus(_B)
_StorageDeviceRowStatus_Type=RowStatus
_StorageDeviceRowStatus_Object=MibTableColumn
storageDeviceRowStatus=_StorageDeviceRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,4,2,1,99),_StorageDeviceRowStatus_Type())
storageDeviceRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:storageDeviceRowStatus.setStatus(_D)
_StorageRaidCount_Type=Integer32
_StorageRaidCount_Object=MibScalar
storageRaidCount=_StorageRaidCount_Object((1,3,6,1,4,1,9804,3,1,1,2,4,3),_StorageRaidCount_Type())
storageRaidCount.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidCount.setStatus(_B)
_StorageRaidTable_Object=MibTable
storageRaidTable=_StorageRaidTable_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4))
if mibBuilder.loadTexts:storageRaidTable.setStatus(_B)
_StorageRaidEntry_Object=MibTableRow
storageRaidEntry=_StorageRaidEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1))
storageRaidEntry.setIndexNames((0,_A,_M))
if mibBuilder.loadTexts:storageRaidEntry.setStatus(_B)
_StorageRaidIndex_Type=Unsigned32
_StorageRaidIndex_Object=MibTableColumn
storageRaidIndex=_StorageRaidIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1,1),_StorageRaidIndex_Type())
storageRaidIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:storageRaidIndex.setStatus(_B)
_StorageRaidDeviceName_Type=DisplayString
_StorageRaidDeviceName_Object=MibTableColumn
storageRaidDeviceName=_StorageRaidDeviceName_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1,2),_StorageRaidDeviceName_Type())
storageRaidDeviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidDeviceName.setStatus(_B)
_StorageRaidLevel_Type=DisplayString
_StorageRaidLevel_Object=MibTableColumn
storageRaidLevel=_StorageRaidLevel_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1,3),_StorageRaidLevel_Type())
storageRaidLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidLevel.setStatus(_B)
_StorageRaidDiskCount_Type=Integer32
_StorageRaidDiskCount_Object=MibTableColumn
storageRaidDiskCount=_StorageRaidDiskCount_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1,4),_StorageRaidDiskCount_Type())
storageRaidDiskCount.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidDiskCount.setStatus(_B)
_StorageRaidSpareDiskCount_Type=Integer32
_StorageRaidSpareDiskCount_Object=MibTableColumn
storageRaidSpareDiskCount=_StorageRaidSpareDiskCount_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1,5),_StorageRaidSpareDiskCount_Type())
storageRaidSpareDiskCount.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidSpareDiskCount.setStatus(_D)
_StorageRaidSuperBlock_Type=TruthValue
_StorageRaidSuperBlock_Object=MibTableColumn
storageRaidSuperBlock=_StorageRaidSuperBlock_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1,6),_StorageRaidSuperBlock_Type())
storageRaidSuperBlock.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidSuperBlock.setStatus(_D)
_StorageRaidChunkSize_Type=Integer32
_StorageRaidChunkSize_Object=MibTableColumn
storageRaidChunkSize=_StorageRaidChunkSize_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1,7),_StorageRaidChunkSize_Type())
storageRaidChunkSize.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidChunkSize.setStatus(_D)
if mibBuilder.loadTexts:storageRaidChunkSize.setUnits('Kbytes')
_StorageRaidDisks_Type=DisplayString
_StorageRaidDisks_Object=MibTableColumn
storageRaidDisks=_StorageRaidDisks_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1,8),_StorageRaidDisks_Type())
storageRaidDisks.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidDisks.setStatus(_B)
_StorageRaidDevice_Type=DisplayString
_StorageRaidDevice_Object=MibTableColumn
storageRaidDevice=_StorageRaidDevice_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1,9),_StorageRaidDevice_Type())
storageRaidDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidDevice.setStatus(_B)
_StorageRaidDeviceCapacity_Type=Integer32
_StorageRaidDeviceCapacity_Object=MibTableColumn
storageRaidDeviceCapacity=_StorageRaidDeviceCapacity_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1,10),_StorageRaidDeviceCapacity_Type())
storageRaidDeviceCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidDeviceCapacity.setStatus(_B)
if mibBuilder.loadTexts:storageRaidDeviceCapacity.setUnits(_H)
_StorageRaidDeviceParityInitState_Type=DisplayString
_StorageRaidDeviceParityInitState_Object=MibTableColumn
storageRaidDeviceParityInitState=_StorageRaidDeviceParityInitState_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1,11),_StorageRaidDeviceParityInitState_Type())
storageRaidDeviceParityInitState.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidDeviceParityInitState.setStatus(_B)
_StorageRaidRebuildPercent_Type=Gauge32
_StorageRaidRebuildPercent_Object=MibTableColumn
storageRaidRebuildPercent=_StorageRaidRebuildPercent_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1,12),_StorageRaidRebuildPercent_Type())
storageRaidRebuildPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidRebuildPercent.setStatus(_B)
if mibBuilder.loadTexts:storageRaidRebuildPercent.setUnits('%')
_StorageRaidRebuildTime_Type=Gauge32
_StorageRaidRebuildTime_Object=MibTableColumn
storageRaidRebuildTime=_StorageRaidRebuildTime_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1,13),_StorageRaidRebuildTime_Type())
storageRaidRebuildTime.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidRebuildTime.setStatus(_B)
if mibBuilder.loadTexts:storageRaidRebuildTime.setUnits('minutes')
_StorageRaidDeviceState_Type=DisplayString
_StorageRaidDeviceState_Object=MibTableColumn
storageRaidDeviceState=_StorageRaidDeviceState_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1,90),_StorageRaidDeviceState_Type())
storageRaidDeviceState.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidDeviceState.setStatus(_B)
class _StorageRaidDeviceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_StorageRaidDeviceStatus_Type.__name__=_E
_StorageRaidDeviceStatus_Object=MibTableColumn
storageRaidDeviceStatus=_StorageRaidDeviceStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1,91),_StorageRaidDeviceStatus_Type())
storageRaidDeviceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidDeviceStatus.setStatus(_B)
_StorageRaidDeviceRowStatus_Type=RowStatus
_StorageRaidDeviceRowStatus_Object=MibTableColumn
storageRaidDeviceRowStatus=_StorageRaidDeviceRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,4,4,1,99),_StorageRaidDeviceRowStatus_Type())
storageRaidDeviceRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidDeviceRowStatus.setStatus(_D)
_StorageRaidDescription_Type=DisplayString
_StorageRaidDescription_Object=MibScalar
storageRaidDescription=_StorageRaidDescription_Object((1,3,6,1,4,1,9804,3,1,1,2,4,5),_StorageRaidDescription_Type())
storageRaidDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidDescription.setStatus(_B)
_StorageRaidMode_Type=DisplayString
_StorageRaidMode_Object=MibScalar
storageRaidMode=_StorageRaidMode_Object((1,3,6,1,4,1,9804,3,1,1,2,4,7),_StorageRaidMode_Type())
storageRaidMode.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidMode.setStatus(_B)
_StorageRaidCapacity_Type=Integer32
_StorageRaidCapacity_Object=MibScalar
storageRaidCapacity=_StorageRaidCapacity_Object((1,3,6,1,4,1,9804,3,1,1,2,4,8),_StorageRaidCapacity_Type())
storageRaidCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidCapacity.setStatus(_B)
if mibBuilder.loadTexts:storageRaidCapacity.setUnits(_H)
class _StorageRaidStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_StorageRaidStatus_Type.__name__=_E
_StorageRaidStatus_Object=MibScalar
storageRaidStatus=_StorageRaidStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,4,11),_StorageRaidStatus_Type())
storageRaidStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidStatus.setStatus(_B)
_StorageRaidState_Type=DisplayString
_StorageRaidState_Object=MibScalar
storageRaidState=_StorageRaidState_Object((1,3,6,1,4,1,9804,3,1,1,2,4,12),_StorageRaidState_Type())
storageRaidState.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidState.setStatus(_B)
_StorageRaidMinimumSpeed_Type=DisplayString
_StorageRaidMinimumSpeed_Object=MibScalar
storageRaidMinimumSpeed=_StorageRaidMinimumSpeed_Object((1,3,6,1,4,1,9804,3,1,1,2,4,13),_StorageRaidMinimumSpeed_Type())
storageRaidMinimumSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidMinimumSpeed.setStatus(_B)
_StorageRaidMaximumSpeed_Type=DisplayString
_StorageRaidMaximumSpeed_Object=MibScalar
storageRaidMaximumSpeed=_StorageRaidMaximumSpeed_Object((1,3,6,1,4,1,9804,3,1,1,2,4,14),_StorageRaidMaximumSpeed_Type())
storageRaidMaximumSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidMaximumSpeed.setStatus(_B)
class _StorageRaidParityInitState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('complete',1),('inProgress',2),('notApplicable',3)))
_StorageRaidParityInitState_Type.__name__=_E
_StorageRaidParityInitState_Object=MibScalar
storageRaidParityInitState=_StorageRaidParityInitState_Object((1,3,6,1,4,1,9804,3,1,1,2,4,15),_StorageRaidParityInitState_Type())
storageRaidParityInitState.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidParityInitState.setStatus(_D)
_StorageRaidStatsIOsRead_Type=Counter64
_StorageRaidStatsIOsRead_Object=MibScalar
storageRaidStatsIOsRead=_StorageRaidStatsIOsRead_Object((1,3,6,1,4,1,9804,3,1,1,2,4,16),_StorageRaidStatsIOsRead_Type())
storageRaidStatsIOsRead.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidStatsIOsRead.setStatus(_B)
if mibBuilder.loadTexts:storageRaidStatsIOsRead.setUnits(_K)
_StorageRaidStatsIOsWrite_Type=Counter64
_StorageRaidStatsIOsWrite_Object=MibScalar
storageRaidStatsIOsWrite=_StorageRaidStatsIOsWrite_Object((1,3,6,1,4,1,9804,3,1,1,2,4,17),_StorageRaidStatsIOsWrite_Type())
storageRaidStatsIOsWrite.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidStatsIOsWrite.setStatus(_B)
if mibBuilder.loadTexts:storageRaidStatsIOsWrite.setUnits(_K)
_StorageRaidStatsKbytesRead_Type=Counter64
_StorageRaidStatsKbytesRead_Object=MibScalar
storageRaidStatsKbytesRead=_StorageRaidStatsKbytesRead_Object((1,3,6,1,4,1,9804,3,1,1,2,4,19),_StorageRaidStatsKbytesRead_Type())
storageRaidStatsKbytesRead.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidStatsKbytesRead.setStatus(_B)
if mibBuilder.loadTexts:storageRaidStatsKbytesRead.setUnits('kB')
_StorageRaidStatsKbytesWrite_Type=Counter64
_StorageRaidStatsKbytesWrite_Object=MibScalar
storageRaidStatsKbytesWrite=_StorageRaidStatsKbytesWrite_Object((1,3,6,1,4,1,9804,3,1,1,2,4,20),_StorageRaidStatsKbytesWrite_Type())
storageRaidStatsKbytesWrite.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidStatsKbytesWrite.setStatus(_B)
if mibBuilder.loadTexts:storageRaidStatsKbytesWrite.setUnits('kB')
_StorageRaidStatsQDepthTotal_Type=Gauge32
_StorageRaidStatsQDepthTotal_Object=MibScalar
storageRaidStatsQDepthTotal=_StorageRaidStatsQDepthTotal_Object((1,3,6,1,4,1,9804,3,1,1,2,4,22),_StorageRaidStatsQDepthTotal_Type())
storageRaidStatsQDepthTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidStatsQDepthTotal.setStatus(_B)
if mibBuilder.loadTexts:storageRaidStatsQDepthTotal.setUnits(_K)
_StorageRaidStatsIoLatencyRead_Type=Counter64
_StorageRaidStatsIoLatencyRead_Object=MibScalar
storageRaidStatsIoLatencyRead=_StorageRaidStatsIoLatencyRead_Object((1,3,6,1,4,1,9804,3,1,1,2,4,23),_StorageRaidStatsIoLatencyRead_Type())
storageRaidStatsIoLatencyRead.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidStatsIoLatencyRead.setStatus(_B)
if mibBuilder.loadTexts:storageRaidStatsIoLatencyRead.setUnits('ms')
_StorageRaidStatsIoLatencyWrite_Type=Counter64
_StorageRaidStatsIoLatencyWrite_Object=MibScalar
storageRaidStatsIoLatencyWrite=_StorageRaidStatsIoLatencyWrite_Object((1,3,6,1,4,1,9804,3,1,1,2,4,24),_StorageRaidStatsIoLatencyWrite_Type())
storageRaidStatsIoLatencyWrite.setMaxAccess(_C)
if mibBuilder.loadTexts:storageRaidStatsIoLatencyWrite.setStatus(_B)
if mibBuilder.loadTexts:storageRaidStatsIoLatencyWrite.setUnits('ms')
_StorageOsRaidCount_Type=Integer32
_StorageOsRaidCount_Object=MibScalar
storageOsRaidCount=_StorageOsRaidCount_Object((1,3,6,1,4,1,9804,3,1,1,2,4,50),_StorageOsRaidCount_Type())
storageOsRaidCount.setMaxAccess(_C)
if mibBuilder.loadTexts:storageOsRaidCount.setStatus(_B)
_StorageOsRaidTable_Object=MibTable
storageOsRaidTable=_StorageOsRaidTable_Object((1,3,6,1,4,1,9804,3,1,1,2,4,51))
if mibBuilder.loadTexts:storageOsRaidTable.setStatus(_B)
_StorageOsRaidEntry_Object=MibTableRow
storageOsRaidEntry=_StorageOsRaidEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,4,51,1))
storageOsRaidEntry.setIndexNames((0,_A,_N))
if mibBuilder.loadTexts:storageOsRaidEntry.setStatus(_B)
_StorageOsRaidIndex_Type=Unsigned32
_StorageOsRaidIndex_Object=MibTableColumn
storageOsRaidIndex=_StorageOsRaidIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,4,51,1,1),_StorageOsRaidIndex_Type())
storageOsRaidIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:storageOsRaidIndex.setStatus(_B)
_StorageOsRaidName_Type=DisplayString
_StorageOsRaidName_Object=MibTableColumn
storageOsRaidName=_StorageOsRaidName_Object((1,3,6,1,4,1,9804,3,1,1,2,4,51,1,2),_StorageOsRaidName_Type())
storageOsRaidName.setMaxAccess(_C)
if mibBuilder.loadTexts:storageOsRaidName.setStatus(_B)
_StorageOsRaidDevice_Type=DisplayString
_StorageOsRaidDevice_Object=MibTableColumn
storageOsRaidDevice=_StorageOsRaidDevice_Object((1,3,6,1,4,1,9804,3,1,1,2,4,51,1,3),_StorageOsRaidDevice_Type())
storageOsRaidDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:storageOsRaidDevice.setStatus(_B)
_StorageOsRaidMode_Type=DisplayString
_StorageOsRaidMode_Object=MibTableColumn
storageOsRaidMode=_StorageOsRaidMode_Object((1,3,6,1,4,1,9804,3,1,1,2,4,51,1,4),_StorageOsRaidMode_Type())
storageOsRaidMode.setMaxAccess(_C)
if mibBuilder.loadTexts:storageOsRaidMode.setStatus(_D)
_StorageOsRaidSize_Type=Integer32
_StorageOsRaidSize_Object=MibTableColumn
storageOsRaidSize=_StorageOsRaidSize_Object((1,3,6,1,4,1,9804,3,1,1,2,4,51,1,5),_StorageOsRaidSize_Type())
storageOsRaidSize.setMaxAccess(_C)
if mibBuilder.loadTexts:storageOsRaidSize.setStatus(_B)
if mibBuilder.loadTexts:storageOsRaidSize.setUnits(_H)
_StorageOsRaidState_Type=DisplayString
_StorageOsRaidState_Object=MibTableColumn
storageOsRaidState=_StorageOsRaidState_Object((1,3,6,1,4,1,9804,3,1,1,2,4,51,1,90),_StorageOsRaidState_Type())
storageOsRaidState.setMaxAccess(_C)
if mibBuilder.loadTexts:storageOsRaidState.setStatus(_B)
_StorageOsRaidRowStatus_Type=RowStatus
_StorageOsRaidRowStatus_Object=MibTableColumn
storageOsRaidRowStatus=_StorageOsRaidRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,4,51,1,99),_StorageOsRaidRowStatus_Type())
storageOsRaidRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:storageOsRaidRowStatus.setStatus(_D)
lefthandNetworksNsmStorageGroup=ObjectGroup((1,3,6,1,4,1,9804,2,1,5,1,2,1))
lefthandNetworksNsmStorageGroup.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:lefthandNetworksNsmStorageGroup.setStatus(_B)
lefthandNetworksNsmStorageGroupObsolete=ObjectGroup((1,3,6,1,4,1,9804,2,1,5,1,2,2))
lefthandNetworksNsmStorageGroupObsolete.setObjects(*((_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL)))
if mibBuilder.loadTexts:lefthandNetworksNsmStorageGroupObsolete.setStatus(_D)
lefthandNetworksNsmStorageMibCompliance=ModuleCompliance((1,3,6,1,4,1,9804,2,1,5,1,1,1))
lefthandNetworksNsmStorageMibCompliance.setObjects((_A,_AM))
if mibBuilder.loadTexts:lefthandNetworksNsmStorageMibCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'lhnNsmStorageModule':lhnNsmStorageModule,'lhnNsmStorageModuleConformance':lhnNsmStorageModuleConformance,'lhnNsmStorageModuleCompliances':lhnNsmStorageModuleCompliances,'lefthandNetworksNsmStorageMibCompliance':lefthandNetworksNsmStorageMibCompliance,'lhnNsmStorageModuleGroups':lhnNsmStorageModuleGroups,_AM:lefthandNetworksNsmStorageGroup,'lefthandNetworksNsmStorageGroupObsolete':lefthandNetworksNsmStorageGroupObsolete,_O:storageDeviceCount,'storageDeviceTable':storageDeviceTable,'storageDeviceEntry':storageDeviceEntry,_L:storageDeviceIndex,_P:storageDeviceModel,_Q:storageDeviceClass,_AC:storageDeviceCapacityInBytes,_R:storageDeviceMode,_AD:storageDeviceChain,_S:storageDeviceSerialNumber,_T:storageDeviceTemperature,_U:storageDeviceTemperatureCritical,_V:storageDeviceTemperatureLimit,_W:storageDeviceTemperatureStatus,_X:storageDeviceLabel,_Y:storageDeviceName,_Z:storageDeviceRaidDevice,_a:storageDeviceFirmwareVersion,_b:storageDeviceSmartHealth,_c:storageDeviceSmartHealthStatus,_d:storageDeviceCapacity,_e:storageDeviceHotRemovable,_f:storageDeviceState,_g:storageDeviceStatus,_AE:storageDeviceRowStatus,_h:storageRaidCount,'storageRaidTable':storageRaidTable,'storageRaidEntry':storageRaidEntry,_M:storageRaidIndex,_i:storageRaidDeviceName,_j:storageRaidLevel,_k:storageRaidDiskCount,_AF:storageRaidSpareDiskCount,_AG:storageRaidSuperBlock,_AH:storageRaidChunkSize,_l:storageRaidDisks,_m:storageRaidDevice,_n:storageRaidDeviceCapacity,_o:storageRaidDeviceParityInitState,_p:storageRaidRebuildPercent,_q:storageRaidRebuildTime,_r:storageRaidDeviceState,_s:storageRaidDeviceStatus,_AJ:storageRaidDeviceRowStatus,_t:storageRaidDescription,_u:storageRaidMode,_v:storageRaidCapacity,_w:storageRaidStatus,_x:storageRaidState,_y:storageRaidMinimumSpeed,_z:storageRaidMaximumSpeed,_AI:storageRaidParityInitState,_A0:storageRaidStatsIOsRead,_A1:storageRaidStatsIOsWrite,_A2:storageRaidStatsKbytesRead,_A3:storageRaidStatsKbytesWrite,_A4:storageRaidStatsQDepthTotal,_A5:storageRaidStatsIoLatencyRead,_A6:storageRaidStatsIoLatencyWrite,_A7:storageOsRaidCount,'storageOsRaidTable':storageOsRaidTable,'storageOsRaidEntry':storageOsRaidEntry,_N:storageOsRaidIndex,_A8:storageOsRaidName,_A9:storageOsRaidDevice,_AK:storageOsRaidMode,_AA:storageOsRaidSize,_AB:storageOsRaidState,_AL:storageOsRaidRowStatus})