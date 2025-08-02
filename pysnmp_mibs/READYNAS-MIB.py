_W='psuMesg'
_V='smartMesg'
_U='backupMesg'
_T='upsMesg'
_S='sataMesg'
_R='snapshotMesg'
_Q='raidMesg'
_P='powerFailureMesg'
_O='tempFailureMesg'
_N='fanFailureMesg'
_M='psuNumber'
_L='volumeNumber'
_K='temperatureNumber'
_J='fanNumber'
_I='diskNumber'
_H='NotificationType'
_G='volumeMesg'
_F='Integer32'
_E='DisplayString'
_D='current'
_C='READYNAS-MIB'
_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier',_H,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_H,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
_Netgear_ObjectIdentity=ObjectIdentity
netgear=_Netgear_ObjectIdentity((1,3,6,1,4,1,4526))
_NasManager_ObjectIdentity=ObjectIdentity
nasManager=_NasManager_ObjectIdentity((1,3,6,1,4,1,4526,18))
class _NasMgrSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_NasMgrSoftwareVersion_Type.__name__=_E
_NasMgrSoftwareVersion_Object=MibScalar
nasMgrSoftwareVersion=_NasMgrSoftwareVersion_Object((1,3,6,1,4,1,4526,18,1),_NasMgrSoftwareVersion_Type())
nasMgrSoftwareVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:nasMgrSoftwareVersion.setStatus(_D)
_DiskTable_Object=MibTable
diskTable=_DiskTable_Object((1,3,6,1,4,1,4526,18,3))
if mibBuilder.loadTexts:diskTable.setStatus(_B)
_DiskEntry_Object=MibTableRow
diskEntry=_DiskEntry_Object((1,3,6,1,4,1,4526,18,3,1))
diskEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:diskEntry.setStatus(_B)
_DiskNumber_Type=Integer32
_DiskNumber_Object=MibTableColumn
diskNumber=_DiskNumber_Object((1,3,6,1,4,1,4526,18,3,1,1),_DiskNumber_Type())
diskNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:diskNumber.setStatus(_B)
_DiskChannel_Type=Integer32
_DiskChannel_Object=MibTableColumn
diskChannel=_DiskChannel_Object((1,3,6,1,4,1,4526,18,3,1,2),_DiskChannel_Type())
diskChannel.setMaxAccess(_A)
if mibBuilder.loadTexts:diskChannel.setStatus(_B)
_DiskModel_Type=DisplayString
_DiskModel_Object=MibTableColumn
diskModel=_DiskModel_Object((1,3,6,1,4,1,4526,18,3,1,3),_DiskModel_Type())
diskModel.setMaxAccess(_A)
if mibBuilder.loadTexts:diskModel.setStatus(_B)
_DiskState_Type=DisplayString
_DiskState_Object=MibTableColumn
diskState=_DiskState_Object((1,3,6,1,4,1,4526,18,3,1,4),_DiskState_Type())
diskState.setMaxAccess(_A)
if mibBuilder.loadTexts:diskState.setStatus(_B)
_DiskTemperature_Type=Integer32
_DiskTemperature_Object=MibTableColumn
diskTemperature=_DiskTemperature_Object((1,3,6,1,4,1,4526,18,3,1,5),_DiskTemperature_Type())
diskTemperature.setMaxAccess(_A)
if mibBuilder.loadTexts:diskTemperature.setStatus(_B)
_FanTable_Object=MibTable
fanTable=_FanTable_Object((1,3,6,1,4,1,4526,18,4))
if mibBuilder.loadTexts:fanTable.setStatus(_D)
_FanEntry_Object=MibTableRow
fanEntry=_FanEntry_Object((1,3,6,1,4,1,4526,18,4,1))
fanEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:fanEntry.setStatus(_D)
class _FanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000000))
_FanNumber_Type.__name__=_F
_FanNumber_Object=MibTableColumn
fanNumber=_FanNumber_Object((1,3,6,1,4,1,4526,18,4,1,1),_FanNumber_Type())
fanNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:fanNumber.setStatus(_B)
_FanRPM_Type=Integer32
_FanRPM_Object=MibTableColumn
fanRPM=_FanRPM_Object((1,3,6,1,4,1,4526,18,4,1,2),_FanRPM_Type())
fanRPM.setMaxAccess(_A)
if mibBuilder.loadTexts:fanRPM.setStatus(_B)
_FanType_Type=DisplayString
_FanType_Object=MibTableColumn
fanType=_FanType_Object((1,3,6,1,4,1,4526,18,4,1,3),_FanType_Type())
fanType.setMaxAccess(_A)
if mibBuilder.loadTexts:fanType.setStatus(_B)
_TemperatureTable_Object=MibTable
temperatureTable=_TemperatureTable_Object((1,3,6,1,4,1,4526,18,5))
if mibBuilder.loadTexts:temperatureTable.setStatus(_B)
_TemperatureEntry_Object=MibTableRow
temperatureEntry=_TemperatureEntry_Object((1,3,6,1,4,1,4526,18,5,1))
temperatureEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:temperatureEntry.setStatus(_B)
_TemperatureNumber_Type=Integer32
_TemperatureNumber_Object=MibTableColumn
temperatureNumber=_TemperatureNumber_Object((1,3,6,1,4,1,4526,18,5,1,1),_TemperatureNumber_Type())
temperatureNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:temperatureNumber.setStatus(_B)
_TemperatureValue_Type=Integer32
_TemperatureValue_Object=MibTableColumn
temperatureValue=_TemperatureValue_Object((1,3,6,1,4,1,4526,18,5,1,2),_TemperatureValue_Type())
temperatureValue.setMaxAccess(_A)
if mibBuilder.loadTexts:temperatureValue.setStatus(_B)
_TemperatureStatus_Type=DisplayString
_TemperatureStatus_Object=MibTableColumn
temperatureStatus=_TemperatureStatus_Object((1,3,6,1,4,1,4526,18,5,1,3),_TemperatureStatus_Type())
temperatureStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:temperatureStatus.setStatus(_B)
_VolumeTable_Object=MibTable
volumeTable=_VolumeTable_Object((1,3,6,1,4,1,4526,18,7))
if mibBuilder.loadTexts:volumeTable.setStatus(_B)
_VolumeEntry_Object=MibTableRow
volumeEntry=_VolumeEntry_Object((1,3,6,1,4,1,4526,18,7,1))
volumeEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:volumeEntry.setStatus(_B)
_VolumeNumber_Type=Integer32
_VolumeNumber_Object=MibTableColumn
volumeNumber=_VolumeNumber_Object((1,3,6,1,4,1,4526,18,7,1,1),_VolumeNumber_Type())
volumeNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:volumeNumber.setStatus(_B)
_VolumeName_Type=DisplayString
_VolumeName_Object=MibTableColumn
volumeName=_VolumeName_Object((1,3,6,1,4,1,4526,18,7,1,2),_VolumeName_Type())
volumeName.setMaxAccess(_A)
if mibBuilder.loadTexts:volumeName.setStatus(_B)
_VolumeRAIDLevel_Type=DisplayString
_VolumeRAIDLevel_Object=MibTableColumn
volumeRAIDLevel=_VolumeRAIDLevel_Object((1,3,6,1,4,1,4526,18,7,1,3),_VolumeRAIDLevel_Type())
volumeRAIDLevel.setMaxAccess(_A)
if mibBuilder.loadTexts:volumeRAIDLevel.setStatus(_B)
_VolumeStatus_Type=DisplayString
_VolumeStatus_Object=MibTableColumn
volumeStatus=_VolumeStatus_Object((1,3,6,1,4,1,4526,18,7,1,4),_VolumeStatus_Type())
volumeStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:volumeStatus.setStatus(_B)
_VolumeSize_Type=Integer32
_VolumeSize_Object=MibTableColumn
volumeSize=_VolumeSize_Object((1,3,6,1,4,1,4526,18,7,1,5),_VolumeSize_Type())
volumeSize.setMaxAccess(_A)
if mibBuilder.loadTexts:volumeSize.setStatus(_B)
_VolumeFreeSpace_Type=Integer32
_VolumeFreeSpace_Object=MibTableColumn
volumeFreeSpace=_VolumeFreeSpace_Object((1,3,6,1,4,1,4526,18,7,1,6),_VolumeFreeSpace_Type())
volumeFreeSpace.setMaxAccess(_A)
if mibBuilder.loadTexts:volumeFreeSpace.setStatus(_B)
_PsuTable_Object=MibTable
psuTable=_PsuTable_Object((1,3,6,1,4,1,4526,18,8))
if mibBuilder.loadTexts:psuTable.setStatus(_B)
_PsuEntry_Object=MibTableRow
psuEntry=_PsuEntry_Object((1,3,6,1,4,1,4526,18,8,1))
psuEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:psuEntry.setStatus(_B)
_PsuNumber_Type=Integer32
_PsuNumber_Object=MibTableColumn
psuNumber=_PsuNumber_Object((1,3,6,1,4,1,4526,18,8,1,1),_PsuNumber_Type())
psuNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:psuNumber.setStatus(_B)
_PsuDesc_Type=DisplayString
_PsuDesc_Object=MibTableColumn
psuDesc=_PsuDesc_Object((1,3,6,1,4,1,4526,18,8,1,2),_PsuDesc_Type())
psuDesc.setMaxAccess(_A)
if mibBuilder.loadTexts:psuDesc.setStatus(_B)
_PsuStatus_Type=DisplayString
_PsuStatus_Object=MibTableColumn
psuStatus=_PsuStatus_Object((1,3,6,1,4,1,4526,18,8,1,3),_PsuStatus_Type())
psuStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:psuStatus.setStatus(_B)
_AryMgrEvts_ObjectIdentity=ObjectIdentity
aryMgrEvts=_AryMgrEvts_ObjectIdentity((1,3,6,1,4,1,4526,18,200))
class _ControllerNameEv_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ControllerNameEv_Type.__name__=_E
_ControllerNameEv_Object=MibScalar
controllerNameEv=_ControllerNameEv_Object((1,3,6,1,4,1,4526,18,200,201),_ControllerNameEv_Type())
controllerNameEv.setMaxAccess(_A)
if mibBuilder.loadTexts:controllerNameEv.setStatus(_B)
class _ChannelNumberEv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_ChannelNumberEv_Type.__name__=_F
_ChannelNumberEv_Object=MibScalar
channelNumberEv=_ChannelNumberEv_Object((1,3,6,1,4,1,4526,18,200,202),_ChannelNumberEv_Type())
channelNumberEv.setMaxAccess(_A)
if mibBuilder.loadTexts:channelNumberEv.setStatus(_B)
class _TargetIDEv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_TargetIDEv_Type.__name__=_F
_TargetIDEv_Object=MibScalar
targetIDEv=_TargetIDEv_Object((1,3,6,1,4,1,4526,18,200,203),_TargetIDEv_Type())
targetIDEv.setMaxAccess(_A)
if mibBuilder.loadTexts:targetIDEv.setStatus(_B)
class _VirtualDiskNameEv_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_VirtualDiskNameEv_Type.__name__=_E
_VirtualDiskNameEv_Object=MibScalar
virtualDiskNameEv=_VirtualDiskNameEv_Object((1,3,6,1,4,1,4526,18,200,204),_VirtualDiskNameEv_Type())
virtualDiskNameEv.setMaxAccess(_A)
if mibBuilder.loadTexts:virtualDiskNameEv.setStatus(_B)
class _ArrayDiskNameEv_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ArrayDiskNameEv_Type.__name__=_E
_ArrayDiskNameEv_Object=MibScalar
arrayDiskNameEv=_ArrayDiskNameEv_Object((1,3,6,1,4,1,4526,18,200,205),_ArrayDiskNameEv_Type())
arrayDiskNameEv.setMaxAccess(_A)
if mibBuilder.loadTexts:arrayDiskNameEv.setStatus(_B)
class _OldVDConfigEv_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_OldVDConfigEv_Type.__name__=_E
_OldVDConfigEv_Object=MibScalar
oldVDConfigEv=_OldVDConfigEv_Object((1,3,6,1,4,1,4526,18,200,206),_OldVDConfigEv_Type())
oldVDConfigEv.setMaxAccess(_A)
if mibBuilder.loadTexts:oldVDConfigEv.setStatus(_B)
class _NewVDConfigEv_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_NewVDConfigEv_Type.__name__=_E
_NewVDConfigEv_Object=MibScalar
newVDConfigEv=_NewVDConfigEv_Object((1,3,6,1,4,1,4526,18,200,207),_NewVDConfigEv_Type())
newVDConfigEv.setMaxAccess(_A)
if mibBuilder.loadTexts:newVDConfigEv.setStatus(_B)
_EnclosureNumberEv_Type=Integer32
_EnclosureNumberEv_Object=MibScalar
enclosureNumberEv=_EnclosureNumberEv_Object((1,3,6,1,4,1,4526,18,200,208),_EnclosureNumberEv_Type())
enclosureNumberEv.setMaxAccess(_A)
if mibBuilder.loadTexts:enclosureNumberEv.setStatus(_B)
_UnitNumberEv_Type=Integer32
_UnitNumberEv_Object=MibScalar
unitNumberEv=_UnitNumberEv_Object((1,3,6,1,4,1,4526,18,200,209),_UnitNumberEv_Type())
unitNumberEv.setMaxAccess(_A)
if mibBuilder.loadTexts:unitNumberEv.setStatus(_B)
_EnclosureNameEv_Type=DisplayString
_EnclosureNameEv_Object=MibScalar
enclosureNameEv=_EnclosureNameEv_Object((1,3,6,1,4,1,4526,18,200,210),_EnclosureNameEv_Type())
enclosureNameEv.setMaxAccess(_A)
if mibBuilder.loadTexts:enclosureNameEv.setStatus(_B)
_UnitNameEv_Type=DisplayString
_UnitNameEv_Object=MibScalar
unitNameEv=_UnitNameEv_Object((1,3,6,1,4,1,4526,18,200,211),_UnitNameEv_Type())
unitNameEv.setMaxAccess(_A)
if mibBuilder.loadTexts:unitNameEv.setStatus(_B)
_TimeEv_Type=Integer32
_TimeEv_Object=MibScalar
timeEv=_TimeEv_Object((1,3,6,1,4,1,4526,18,200,212),_TimeEv_Type())
timeEv.setMaxAccess(_A)
if mibBuilder.loadTexts:timeEv.setStatus(_B)
_VolumeNameEv_Type=DisplayString
_VolumeNameEv_Object=MibScalar
volumeNameEv=_VolumeNameEv_Object((1,3,6,1,4,1,4526,18,200,213),_VolumeNameEv_Type())
volumeNameEv.setMaxAccess(_A)
if mibBuilder.loadTexts:volumeNameEv.setStatus(_B)
_NasTraps_ObjectIdentity=ObjectIdentity
nasTraps=_NasTraps_ObjectIdentity((1,3,6,1,4,1,4526,18,300))
_FanFailureMesg_Type=DisplayString
_FanFailureMesg_Object=MibScalar
fanFailureMesg=_FanFailureMesg_Object((1,3,6,1,4,1,4526,18,400),_FanFailureMesg_Type())
fanFailureMesg.setMaxAccess(_A)
if mibBuilder.loadTexts:fanFailureMesg.setStatus(_D)
_TempFailureMesg_Type=DisplayString
_TempFailureMesg_Object=MibScalar
tempFailureMesg=_TempFailureMesg_Object((1,3,6,1,4,1,4526,18,401),_TempFailureMesg_Type())
tempFailureMesg.setMaxAccess(_A)
if mibBuilder.loadTexts:tempFailureMesg.setStatus(_D)
_PowerFailureMesg_Type=DisplayString
_PowerFailureMesg_Object=MibScalar
powerFailureMesg=_PowerFailureMesg_Object((1,3,6,1,4,1,4526,18,402),_PowerFailureMesg_Type())
powerFailureMesg.setMaxAccess(_A)
if mibBuilder.loadTexts:powerFailureMesg.setStatus(_D)
_RaidMesg_Type=DisplayString
_RaidMesg_Object=MibScalar
raidMesg=_RaidMesg_Object((1,3,6,1,4,1,4526,18,403),_RaidMesg_Type())
raidMesg.setMaxAccess(_A)
if mibBuilder.loadTexts:raidMesg.setStatus(_D)
_SnapshotMesg_Type=DisplayString
_SnapshotMesg_Object=MibScalar
snapshotMesg=_SnapshotMesg_Object((1,3,6,1,4,1,4526,18,404),_SnapshotMesg_Type())
snapshotMesg.setMaxAccess(_A)
if mibBuilder.loadTexts:snapshotMesg.setStatus(_D)
_UpsMesg_Type=DisplayString
_UpsMesg_Object=MibScalar
upsMesg=_UpsMesg_Object((1,3,6,1,4,1,4526,18,405),_UpsMesg_Type())
upsMesg.setMaxAccess(_A)
if mibBuilder.loadTexts:upsMesg.setStatus(_D)
_SataMesg_Type=DisplayString
_SataMesg_Object=MibScalar
sataMesg=_SataMesg_Object((1,3,6,1,4,1,4526,18,406),_SataMesg_Type())
sataMesg.setMaxAccess(_A)
if mibBuilder.loadTexts:sataMesg.setStatus(_D)
_VolumeMesg_Type=DisplayString
_VolumeMesg_Object=MibScalar
volumeMesg=_VolumeMesg_Object((1,3,6,1,4,1,4526,18,407),_VolumeMesg_Type())
volumeMesg.setMaxAccess(_A)
if mibBuilder.loadTexts:volumeMesg.setStatus(_D)
_DiskTempWarningMesg_Type=DisplayString
_DiskTempWarningMesg_Object=MibScalar
diskTempWarningMesg=_DiskTempWarningMesg_Object((1,3,6,1,4,1,4526,18,408),_DiskTempWarningMesg_Type())
diskTempWarningMesg.setMaxAccess(_A)
if mibBuilder.loadTexts:diskTempWarningMesg.setStatus(_D)
_BackupMesg_Type=DisplayString
_BackupMesg_Object=MibScalar
backupMesg=_BackupMesg_Object((1,3,6,1,4,1,4526,18,409),_BackupMesg_Type())
backupMesg.setMaxAccess(_A)
if mibBuilder.loadTexts:backupMesg.setStatus(_D)
_SmartMesg_Type=DisplayString
_SmartMesg_Object=MibScalar
smartMesg=_SmartMesg_Object((1,3,6,1,4,1,4526,18,410),_SmartMesg_Type())
smartMesg.setMaxAccess(_A)
if mibBuilder.loadTexts:smartMesg.setStatus(_D)
_PsuMesg_Type=DisplayString
_PsuMesg_Object=MibScalar
psuMesg=_PsuMesg_Object((1,3,6,1,4,1,4526,18,411),_PsuMesg_Type())
psuMesg.setMaxAccess(_A)
if mibBuilder.loadTexts:psuMesg.setStatus(_D)
_ProductID_ObjectIdentity=ObjectIdentity
productID=_ProductID_ObjectIdentity((1,3,6,1,4,1,4526,100))
_ReadyNAS_ObjectIdentity=ObjectIdentity
readyNAS=_ReadyNAS_ObjectIdentity((1,3,6,1,4,1,4526,100,12))
fanFailure=NotificationType((1,3,6,1,4,1,4526,18,300,0,10))
fanFailure.setObjects((_C,_N))
if mibBuilder.loadTexts:fanFailure.setStatus('')
tempFailure=NotificationType((1,3,6,1,4,1,4526,18,300,0,20))
tempFailure.setObjects((_C,_O))
if mibBuilder.loadTexts:tempFailure.setStatus('')
powerVoltage=NotificationType((1,3,6,1,4,1,4526,18,300,0,30))
powerVoltage.setObjects((_C,_P))
if mibBuilder.loadTexts:powerVoltage.setStatus('')
raidEventNotice=NotificationType((1,3,6,1,4,1,4526,18,300,0,40))
raidEventNotice.setObjects((_C,_Q))
if mibBuilder.loadTexts:raidEventNotice.setStatus('')
snapshotEventNotice=NotificationType((1,3,6,1,4,1,4526,18,300,0,50))
snapshotEventNotice.setObjects((_C,_R))
if mibBuilder.loadTexts:snapshotEventNotice.setStatus('')
hotplugDiskNotice=NotificationType((1,3,6,1,4,1,4526,18,300,0,60))
hotplugDiskNotice.setObjects((_C,_S))
if mibBuilder.loadTexts:hotplugDiskNotice.setStatus('')
upsEventNotice=NotificationType((1,3,6,1,4,1,4526,18,300,0,70))
upsEventNotice.setObjects((_C,_T))
if mibBuilder.loadTexts:upsEventNotice.setStatus('')
volumeNotice=NotificationType((1,3,6,1,4,1,4526,18,300,0,80))
volumeNotice.setObjects((_C,_G))
if mibBuilder.loadTexts:volumeNotice.setStatus('')
diskTempWarning=NotificationType((1,3,6,1,4,1,4526,18,300,0,90))
diskTempWarning.setObjects((_C,_G))
if mibBuilder.loadTexts:diskTempWarning.setStatus('')
backupNotice=NotificationType((1,3,6,1,4,1,4526,18,300,0,100))
backupNotice.setObjects((_C,_U))
if mibBuilder.loadTexts:backupNotice.setStatus('')
diskSmartWarning=NotificationType((1,3,6,1,4,1,4526,18,300,0,110))
diskSmartWarning.setObjects((_C,_V))
if mibBuilder.loadTexts:diskSmartWarning.setStatus('')
psuWarning=NotificationType((1,3,6,1,4,1,4526,18,300,0,120))
psuWarning.setObjects((_C,_W))
if mibBuilder.loadTexts:psuWarning.setStatus('')
mibBuilder.exportSymbols(_C,**{'netgear':netgear,'nasManager':nasManager,'nasMgrSoftwareVersion':nasMgrSoftwareVersion,'diskTable':diskTable,'diskEntry':diskEntry,_I:diskNumber,'diskChannel':diskChannel,'diskModel':diskModel,'diskState':diskState,'diskTemperature':diskTemperature,'fanTable':fanTable,'fanEntry':fanEntry,_J:fanNumber,'fanRPM':fanRPM,'fanType':fanType,'temperatureTable':temperatureTable,'temperatureEntry':temperatureEntry,_K:temperatureNumber,'temperatureValue':temperatureValue,'temperatureStatus':temperatureStatus,'volumeTable':volumeTable,'volumeEntry':volumeEntry,_L:volumeNumber,'volumeName':volumeName,'volumeRAIDLevel':volumeRAIDLevel,'volumeStatus':volumeStatus,'volumeSize':volumeSize,'volumeFreeSpace':volumeFreeSpace,'psuTable':psuTable,'psuEntry':psuEntry,_M:psuNumber,'psuDesc':psuDesc,'psuStatus':psuStatus,'aryMgrEvts':aryMgrEvts,'controllerNameEv':controllerNameEv,'channelNumberEv':channelNumberEv,'targetIDEv':targetIDEv,'virtualDiskNameEv':virtualDiskNameEv,'arrayDiskNameEv':arrayDiskNameEv,'oldVDConfigEv':oldVDConfigEv,'newVDConfigEv':newVDConfigEv,'enclosureNumberEv':enclosureNumberEv,'unitNumberEv':unitNumberEv,'enclosureNameEv':enclosureNameEv,'unitNameEv':unitNameEv,'timeEv':timeEv,'volumeNameEv':volumeNameEv,'nasTraps':nasTraps,'fanFailure':fanFailure,'tempFailure':tempFailure,'powerVoltage':powerVoltage,'raidEventNotice':raidEventNotice,'snapshotEventNotice':snapshotEventNotice,'hotplugDiskNotice':hotplugDiskNotice,'upsEventNotice':upsEventNotice,'volumeNotice':volumeNotice,'diskTempWarning':diskTempWarning,'backupNotice':backupNotice,'diskSmartWarning':diskSmartWarning,'psuWarning':psuWarning,_N:fanFailureMesg,_O:tempFailureMesg,_P:powerFailureMesg,_Q:raidMesg,_R:snapshotMesg,_T:upsMesg,_S:sataMesg,_G:volumeMesg,'diskTempWarningMesg':diskTempWarningMesg,_U:backupMesg,_V:smartMesg,_W:psuMesg,'productID':productID,'readyNAS':readyNAS})