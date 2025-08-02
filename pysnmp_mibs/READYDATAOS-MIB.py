_X='psuWarningMesg'
_W='diskSmartWarningMesg'
_V='backupNoticeMesg'
_U='diskTempWarningMesg'
_T='volumeNoticeMesg'
_S='upsEventNoticeMesg'
_R='hotplugDiskNoticeMesg'
_Q='snapshotEventNoticeMesg'
_P='raidEventNoticeMesg'
_O='powerVoltageMesg'
_N='tempFailureMesg'
_M='fanFailureMesg'
_L='psuNumber'
_K='volumeNumber'
_J='temperatureNumber'
_I='fanNumber'
_H='diskNumber'
_G='NotificationType'
_F='Integer32'
_E='DisplayString'
_D='current'
_C='READYDATAOS-MIB'
_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier',_G,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_G,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
_Netgear_ObjectIdentity=ObjectIdentity
netgear=_Netgear_ObjectIdentity((1,3,6,1,4,1,4526))
_NgNasManager_ObjectIdentity=ObjectIdentity
ngNasManager=_NgNasManager_ObjectIdentity((1,3,6,1,4,1,4526,22))
class _NasMgrSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_NasMgrSoftwareVersion_Type.__name__=_E
_NasMgrSoftwareVersion_Object=MibScalar
nasMgrSoftwareVersion=_NasMgrSoftwareVersion_Object((1,3,6,1,4,1,4526,22,1),_NasMgrSoftwareVersion_Type())
nasMgrSoftwareVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:nasMgrSoftwareVersion.setStatus(_D)
_DiskTable_Object=MibTable
diskTable=_DiskTable_Object((1,3,6,1,4,1,4526,22,3))
if mibBuilder.loadTexts:diskTable.setStatus(_B)
_DiskEntry_Object=MibTableRow
diskEntry=_DiskEntry_Object((1,3,6,1,4,1,4526,22,3,1))
diskEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:diskEntry.setStatus(_B)
_DiskNumber_Type=Integer32
_DiskNumber_Object=MibTableColumn
diskNumber=_DiskNumber_Object((1,3,6,1,4,1,4526,22,3,1,1),_DiskNumber_Type())
diskNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:diskNumber.setStatus(_B)
_DiskID_Type=DisplayString
_DiskID_Object=MibTableColumn
diskID=_DiskID_Object((1,3,6,1,4,1,4526,22,3,1,2),_DiskID_Type())
diskID.setMaxAccess(_A)
if mibBuilder.loadTexts:diskID.setStatus(_B)
_DiskSlotName_Type=DisplayString
_DiskSlotName_Object=MibTableColumn
diskSlotName=_DiskSlotName_Object((1,3,6,1,4,1,4526,22,3,1,3),_DiskSlotName_Type())
diskSlotName.setMaxAccess(_A)
if mibBuilder.loadTexts:diskSlotName.setStatus(_B)
_DiskSerial_Type=DisplayString
_DiskSerial_Object=MibTableColumn
diskSerial=_DiskSerial_Object((1,3,6,1,4,1,4526,22,3,1,4),_DiskSerial_Type())
diskSerial.setMaxAccess(_A)
if mibBuilder.loadTexts:diskSerial.setStatus(_B)
_DiskModel_Type=DisplayString
_DiskModel_Object=MibTableColumn
diskModel=_DiskModel_Object((1,3,6,1,4,1,4526,22,3,1,5),_DiskModel_Type())
diskModel.setMaxAccess(_A)
if mibBuilder.loadTexts:diskModel.setStatus(_B)
_AtaError_Type=Integer32
_AtaError_Object=MibTableColumn
ataError=_AtaError_Object((1,3,6,1,4,1,4526,22,3,1,6),_AtaError_Type())
ataError.setMaxAccess(_A)
if mibBuilder.loadTexts:ataError.setStatus(_B)
_DiskCapacity_Type=DisplayString
_DiskCapacity_Object=MibTableColumn
diskCapacity=_DiskCapacity_Object((1,3,6,1,4,1,4526,22,3,1,7),_DiskCapacity_Type())
diskCapacity.setMaxAccess(_A)
if mibBuilder.loadTexts:diskCapacity.setStatus(_B)
_DiskInterface_Type=DisplayString
_DiskInterface_Object=MibTableColumn
diskInterface=_DiskInterface_Object((1,3,6,1,4,1,4526,22,3,1,8),_DiskInterface_Type())
diskInterface.setMaxAccess(_A)
if mibBuilder.loadTexts:diskInterface.setStatus(_B)
_DiskState_Type=DisplayString
_DiskState_Object=MibTableColumn
diskState=_DiskState_Object((1,3,6,1,4,1,4526,22,3,1,9),_DiskState_Type())
diskState.setMaxAccess(_A)
if mibBuilder.loadTexts:diskState.setStatus(_B)
_DiskTemperature_Type=Integer32
_DiskTemperature_Object=MibTableColumn
diskTemperature=_DiskTemperature_Object((1,3,6,1,4,1,4526,22,3,1,10),_DiskTemperature_Type())
diskTemperature.setMaxAccess(_A)
if mibBuilder.loadTexts:diskTemperature.setStatus(_B)
_FanTable_Object=MibTable
fanTable=_FanTable_Object((1,3,6,1,4,1,4526,22,4))
if mibBuilder.loadTexts:fanTable.setStatus(_D)
_FanEntry_Object=MibTableRow
fanEntry=_FanEntry_Object((1,3,6,1,4,1,4526,22,4,1))
fanEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:fanEntry.setStatus(_D)
class _FanNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000000))
_FanNumber_Type.__name__=_F
_FanNumber_Object=MibTableColumn
fanNumber=_FanNumber_Object((1,3,6,1,4,1,4526,22,4,1,1),_FanNumber_Type())
fanNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:fanNumber.setStatus(_B)
_FanRPM_Type=Integer32
_FanRPM_Object=MibTableColumn
fanRPM=_FanRPM_Object((1,3,6,1,4,1,4526,22,4,1,2),_FanRPM_Type())
fanRPM.setMaxAccess(_A)
if mibBuilder.loadTexts:fanRPM.setStatus(_B)
_FanStatus_Type=DisplayString
_FanStatus_Object=MibTableColumn
fanStatus=_FanStatus_Object((1,3,6,1,4,1,4526,22,4,1,3),_FanStatus_Type())
fanStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:fanStatus.setStatus(_B)
_FanType_Type=DisplayString
_FanType_Object=MibTableColumn
fanType=_FanType_Object((1,3,6,1,4,1,4526,22,4,1,4),_FanType_Type())
fanType.setMaxAccess(_A)
if mibBuilder.loadTexts:fanType.setStatus(_B)
_TemperatureTable_Object=MibTable
temperatureTable=_TemperatureTable_Object((1,3,6,1,4,1,4526,22,5))
if mibBuilder.loadTexts:temperatureTable.setStatus(_B)
_TemperatureEntry_Object=MibTableRow
temperatureEntry=_TemperatureEntry_Object((1,3,6,1,4,1,4526,22,5,1))
temperatureEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:temperatureEntry.setStatus(_B)
_TemperatureNumber_Type=Integer32
_TemperatureNumber_Object=MibTableColumn
temperatureNumber=_TemperatureNumber_Object((1,3,6,1,4,1,4526,22,5,1,1),_TemperatureNumber_Type())
temperatureNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:temperatureNumber.setStatus(_B)
_TemperatureValue_Type=Integer32
_TemperatureValue_Object=MibTableColumn
temperatureValue=_TemperatureValue_Object((1,3,6,1,4,1,4526,22,5,1,2),_TemperatureValue_Type())
temperatureValue.setMaxAccess(_A)
if mibBuilder.loadTexts:temperatureValue.setStatus(_B)
_TemperatureTyoe_Type=DisplayString
_TemperatureTyoe_Object=MibScalar
temperatureTyoe=_TemperatureTyoe_Object((1,3,6,1,4,1,4526,22,5,1,3),_TemperatureTyoe_Type())
temperatureTyoe.setMaxAccess(_A)
if mibBuilder.loadTexts:temperatureTyoe.setStatus(_B)
_TemperatureMin_Type=Integer32
_TemperatureMin_Object=MibTableColumn
temperatureMin=_TemperatureMin_Object((1,3,6,1,4,1,4526,22,5,1,4),_TemperatureMin_Type())
temperatureMin.setMaxAccess(_A)
if mibBuilder.loadTexts:temperatureMin.setStatus(_B)
_TemperatureMax_Type=Integer32
_TemperatureMax_Object=MibTableColumn
temperatureMax=_TemperatureMax_Object((1,3,6,1,4,1,4526,22,5,1,5),_TemperatureMax_Type())
temperatureMax.setMaxAccess(_A)
if mibBuilder.loadTexts:temperatureMax.setStatus(_B)
_VolumeTable_Object=MibTable
volumeTable=_VolumeTable_Object((1,3,6,1,4,1,4526,22,7))
if mibBuilder.loadTexts:volumeTable.setStatus(_B)
_VolumeEntry_Object=MibTableRow
volumeEntry=_VolumeEntry_Object((1,3,6,1,4,1,4526,22,7,1))
volumeEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:volumeEntry.setStatus(_B)
_VolumeNumber_Type=Integer32
_VolumeNumber_Object=MibTableColumn
volumeNumber=_VolumeNumber_Object((1,3,6,1,4,1,4526,22,7,1,1),_VolumeNumber_Type())
volumeNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:volumeNumber.setStatus(_B)
_VolumeName_Type=DisplayString
_VolumeName_Object=MibTableColumn
volumeName=_VolumeName_Object((1,3,6,1,4,1,4526,22,7,1,2),_VolumeName_Type())
volumeName.setMaxAccess(_A)
if mibBuilder.loadTexts:volumeName.setStatus(_B)
_VolumeRAIDLevel_Type=DisplayString
_VolumeRAIDLevel_Object=MibTableColumn
volumeRAIDLevel=_VolumeRAIDLevel_Object((1,3,6,1,4,1,4526,22,7,1,3),_VolumeRAIDLevel_Type())
volumeRAIDLevel.setMaxAccess(_A)
if mibBuilder.loadTexts:volumeRAIDLevel.setStatus(_B)
_VolumeStatus_Type=DisplayString
_VolumeStatus_Object=MibTableColumn
volumeStatus=_VolumeStatus_Object((1,3,6,1,4,1,4526,22,7,1,4),_VolumeStatus_Type())
volumeStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:volumeStatus.setStatus(_B)
_VolumeSize_Type=Integer32
_VolumeSize_Object=MibTableColumn
volumeSize=_VolumeSize_Object((1,3,6,1,4,1,4526,22,7,1,5),_VolumeSize_Type())
volumeSize.setMaxAccess(_A)
if mibBuilder.loadTexts:volumeSize.setStatus(_B)
_VolumeFreeSpace_Type=Integer32
_VolumeFreeSpace_Object=MibTableColumn
volumeFreeSpace=_VolumeFreeSpace_Object((1,3,6,1,4,1,4526,22,7,1,6),_VolumeFreeSpace_Type())
volumeFreeSpace.setMaxAccess(_A)
if mibBuilder.loadTexts:volumeFreeSpace.setStatus(_B)
_PsuTable_Object=MibTable
psuTable=_PsuTable_Object((1,3,6,1,4,1,4526,22,8))
if mibBuilder.loadTexts:psuTable.setStatus(_B)
_PsuEntry_Object=MibTableRow
psuEntry=_PsuEntry_Object((1,3,6,1,4,1,4526,22,8,1))
psuEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:psuEntry.setStatus(_B)
_PsuNumber_Type=Integer32
_PsuNumber_Object=MibTableColumn
psuNumber=_PsuNumber_Object((1,3,6,1,4,1,4526,22,8,1,1),_PsuNumber_Type())
psuNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:psuNumber.setStatus(_B)
_PsuDesc_Type=DisplayString
_PsuDesc_Object=MibTableColumn
psuDesc=_PsuDesc_Object((1,3,6,1,4,1,4526,22,8,1,2),_PsuDesc_Type())
psuDesc.setMaxAccess(_A)
if mibBuilder.loadTexts:psuDesc.setStatus(_B)
_PsuStatus_Type=DisplayString
_PsuStatus_Object=MibTableColumn
psuStatus=_PsuStatus_Object((1,3,6,1,4,1,4526,22,8,1,3),_PsuStatus_Type())
psuStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:psuStatus.setStatus(_B)
_AryMgrEvts_ObjectIdentity=ObjectIdentity
aryMgrEvts=_AryMgrEvts_ObjectIdentity((1,3,6,1,4,1,4526,22,200))
class _ControllerNameEv_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ControllerNameEv_Type.__name__=_E
_ControllerNameEv_Object=MibScalar
controllerNameEv=_ControllerNameEv_Object((1,3,6,1,4,1,4526,22,200,201),_ControllerNameEv_Type())
controllerNameEv.setMaxAccess(_A)
if mibBuilder.loadTexts:controllerNameEv.setStatus(_B)
class _ChannelNumberEv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_ChannelNumberEv_Type.__name__=_F
_ChannelNumberEv_Object=MibScalar
channelNumberEv=_ChannelNumberEv_Object((1,3,6,1,4,1,4526,22,200,202),_ChannelNumberEv_Type())
channelNumberEv.setMaxAccess(_A)
if mibBuilder.loadTexts:channelNumberEv.setStatus(_B)
class _TargetIDEv_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_TargetIDEv_Type.__name__=_F
_TargetIDEv_Object=MibScalar
targetIDEv=_TargetIDEv_Object((1,3,6,1,4,1,4526,22,200,203),_TargetIDEv_Type())
targetIDEv.setMaxAccess(_A)
if mibBuilder.loadTexts:targetIDEv.setStatus(_B)
class _VirtualDiskNameEv_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_VirtualDiskNameEv_Type.__name__=_E
_VirtualDiskNameEv_Object=MibScalar
virtualDiskNameEv=_VirtualDiskNameEv_Object((1,3,6,1,4,1,4526,22,200,204),_VirtualDiskNameEv_Type())
virtualDiskNameEv.setMaxAccess(_A)
if mibBuilder.loadTexts:virtualDiskNameEv.setStatus(_B)
class _ArrayDiskNameEv_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_ArrayDiskNameEv_Type.__name__=_E
_ArrayDiskNameEv_Object=MibScalar
arrayDiskNameEv=_ArrayDiskNameEv_Object((1,3,6,1,4,1,4526,22,200,205),_ArrayDiskNameEv_Type())
arrayDiskNameEv.setMaxAccess(_A)
if mibBuilder.loadTexts:arrayDiskNameEv.setStatus(_B)
class _OldVDConfigEv_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_OldVDConfigEv_Type.__name__=_E
_OldVDConfigEv_Object=MibScalar
oldVDConfigEv=_OldVDConfigEv_Object((1,3,6,1,4,1,4526,22,200,206),_OldVDConfigEv_Type())
oldVDConfigEv.setMaxAccess(_A)
if mibBuilder.loadTexts:oldVDConfigEv.setStatus(_B)
class _NewVDConfigEv_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_NewVDConfigEv_Type.__name__=_E
_NewVDConfigEv_Object=MibScalar
newVDConfigEv=_NewVDConfigEv_Object((1,3,6,1,4,1,4526,22,200,207),_NewVDConfigEv_Type())
newVDConfigEv.setMaxAccess(_A)
if mibBuilder.loadTexts:newVDConfigEv.setStatus(_B)
_EnclosureNumberEv_Type=Integer32
_EnclosureNumberEv_Object=MibScalar
enclosureNumberEv=_EnclosureNumberEv_Object((1,3,6,1,4,1,4526,22,200,208),_EnclosureNumberEv_Type())
enclosureNumberEv.setMaxAccess(_A)
if mibBuilder.loadTexts:enclosureNumberEv.setStatus(_B)
_UnitNumberEv_Type=Integer32
_UnitNumberEv_Object=MibScalar
unitNumberEv=_UnitNumberEv_Object((1,3,6,1,4,1,4526,22,200,209),_UnitNumberEv_Type())
unitNumberEv.setMaxAccess(_A)
if mibBuilder.loadTexts:unitNumberEv.setStatus(_B)
_EnclosureNameEv_Type=DisplayString
_EnclosureNameEv_Object=MibScalar
enclosureNameEv=_EnclosureNameEv_Object((1,3,6,1,4,1,4526,22,200,210),_EnclosureNameEv_Type())
enclosureNameEv.setMaxAccess(_A)
if mibBuilder.loadTexts:enclosureNameEv.setStatus(_B)
_UnitNameEv_Type=DisplayString
_UnitNameEv_Object=MibScalar
unitNameEv=_UnitNameEv_Object((1,3,6,1,4,1,4526,22,200,211),_UnitNameEv_Type())
unitNameEv.setMaxAccess(_A)
if mibBuilder.loadTexts:unitNameEv.setStatus(_B)
_TimeEv_Type=Integer32
_TimeEv_Object=MibScalar
timeEv=_TimeEv_Object((1,3,6,1,4,1,4526,22,200,212),_TimeEv_Type())
timeEv.setMaxAccess(_A)
if mibBuilder.loadTexts:timeEv.setStatus(_B)
_VolumeNameEv_Type=DisplayString
_VolumeNameEv_Object=MibScalar
volumeNameEv=_VolumeNameEv_Object((1,3,6,1,4,1,4526,22,200,213),_VolumeNameEv_Type())
volumeNameEv.setMaxAccess(_A)
if mibBuilder.loadTexts:volumeNameEv.setStatus(_B)
_NasTraps_ObjectIdentity=ObjectIdentity
nasTraps=_NasTraps_ObjectIdentity((1,3,6,1,4,1,4526,22,300))
_FanFailureMesg_Type=DisplayString
_FanFailureMesg_Object=MibScalar
fanFailureMesg=_FanFailureMesg_Object((1,3,6,1,4,1,4526,22,400),_FanFailureMesg_Type())
fanFailureMesg.setMaxAccess(_A)
if mibBuilder.loadTexts:fanFailureMesg.setStatus(_D)
_TempFailureMesg_Type=DisplayString
_TempFailureMesg_Object=MibScalar
tempFailureMesg=_TempFailureMesg_Object((1,3,6,1,4,1,4526,22,401),_TempFailureMesg_Type())
tempFailureMesg.setMaxAccess(_A)
if mibBuilder.loadTexts:tempFailureMesg.setStatus(_D)
_PowerVoltageMesg_Type=DisplayString
_PowerVoltageMesg_Object=MibScalar
powerVoltageMesg=_PowerVoltageMesg_Object((1,3,6,1,4,1,4526,22,402),_PowerVoltageMesg_Type())
powerVoltageMesg.setMaxAccess(_A)
if mibBuilder.loadTexts:powerVoltageMesg.setStatus(_D)
_RaidEventNoticeMesg_Type=DisplayString
_RaidEventNoticeMesg_Object=MibScalar
raidEventNoticeMesg=_RaidEventNoticeMesg_Object((1,3,6,1,4,1,4526,22,403),_RaidEventNoticeMesg_Type())
raidEventNoticeMesg.setMaxAccess(_A)
if mibBuilder.loadTexts:raidEventNoticeMesg.setStatus(_D)
_SnapshotEventNoticeMesg_Type=DisplayString
_SnapshotEventNoticeMesg_Object=MibScalar
snapshotEventNoticeMesg=_SnapshotEventNoticeMesg_Object((1,3,6,1,4,1,4526,22,404),_SnapshotEventNoticeMesg_Type())
snapshotEventNoticeMesg.setMaxAccess(_A)
if mibBuilder.loadTexts:snapshotEventNoticeMesg.setStatus(_D)
_UpsEventNoticeMesg_Type=DisplayString
_UpsEventNoticeMesg_Object=MibScalar
upsEventNoticeMesg=_UpsEventNoticeMesg_Object((1,3,6,1,4,1,4526,22,405),_UpsEventNoticeMesg_Type())
upsEventNoticeMesg.setMaxAccess(_A)
if mibBuilder.loadTexts:upsEventNoticeMesg.setStatus(_D)
_HotplugDiskNoticeMesg_Type=DisplayString
_HotplugDiskNoticeMesg_Object=MibScalar
hotplugDiskNoticeMesg=_HotplugDiskNoticeMesg_Object((1,3,6,1,4,1,4526,22,406),_HotplugDiskNoticeMesg_Type())
hotplugDiskNoticeMesg.setMaxAccess(_A)
if mibBuilder.loadTexts:hotplugDiskNoticeMesg.setStatus(_D)
_VolumeNoticeMesg_Type=DisplayString
_VolumeNoticeMesg_Object=MibScalar
volumeNoticeMesg=_VolumeNoticeMesg_Object((1,3,6,1,4,1,4526,22,407),_VolumeNoticeMesg_Type())
volumeNoticeMesg.setMaxAccess(_A)
if mibBuilder.loadTexts:volumeNoticeMesg.setStatus(_D)
_DiskTempWarningMesg_Type=DisplayString
_DiskTempWarningMesg_Object=MibScalar
diskTempWarningMesg=_DiskTempWarningMesg_Object((1,3,6,1,4,1,4526,22,408),_DiskTempWarningMesg_Type())
diskTempWarningMesg.setMaxAccess(_A)
if mibBuilder.loadTexts:diskTempWarningMesg.setStatus(_D)
_BackupNoticeMesg_Type=DisplayString
_BackupNoticeMesg_Object=MibScalar
backupNoticeMesg=_BackupNoticeMesg_Object((1,3,6,1,4,1,4526,22,409),_BackupNoticeMesg_Type())
backupNoticeMesg.setMaxAccess(_A)
if mibBuilder.loadTexts:backupNoticeMesg.setStatus(_D)
_DiskSmartWarningMesg_Type=DisplayString
_DiskSmartWarningMesg_Object=MibScalar
diskSmartWarningMesg=_DiskSmartWarningMesg_Object((1,3,6,1,4,1,4526,22,410),_DiskSmartWarningMesg_Type())
diskSmartWarningMesg.setMaxAccess(_A)
if mibBuilder.loadTexts:diskSmartWarningMesg.setStatus(_D)
_PsuWarningMesg_Type=DisplayString
_PsuWarningMesg_Object=MibScalar
psuWarningMesg=_PsuWarningMesg_Object((1,3,6,1,4,1,4526,22,411),_PsuWarningMesg_Type())
psuWarningMesg.setMaxAccess(_A)
if mibBuilder.loadTexts:psuWarningMesg.setStatus(_D)
_ProductID_ObjectIdentity=ObjectIdentity
productID=_ProductID_ObjectIdentity((1,3,6,1,4,1,4526,100))
_ReadyDATAOS_ObjectIdentity=ObjectIdentity
ReadyDATAOS=_ReadyDATAOS_ObjectIdentity((1,3,6,1,4,1,4526,100,15))
fanFailure=NotificationType((1,3,6,1,4,1,4526,22,300,0,10))
fanFailure.setObjects((_C,_M))
if mibBuilder.loadTexts:fanFailure.setStatus('')
tempFailure=NotificationType((1,3,6,1,4,1,4526,22,300,0,20))
tempFailure.setObjects((_C,_N))
if mibBuilder.loadTexts:tempFailure.setStatus('')
powerVoltage=NotificationType((1,3,6,1,4,1,4526,22,300,0,30))
powerVoltage.setObjects((_C,_O))
if mibBuilder.loadTexts:powerVoltage.setStatus('')
raidEventNotice=NotificationType((1,3,6,1,4,1,4526,22,300,0,40))
raidEventNotice.setObjects((_C,_P))
if mibBuilder.loadTexts:raidEventNotice.setStatus('')
snapshotEventNotice=NotificationType((1,3,6,1,4,1,4526,22,300,0,50))
snapshotEventNotice.setObjects((_C,_Q))
if mibBuilder.loadTexts:snapshotEventNotice.setStatus('')
hotplugDiskNotice=NotificationType((1,3,6,1,4,1,4526,22,300,0,60))
hotplugDiskNotice.setObjects((_C,_R))
if mibBuilder.loadTexts:hotplugDiskNotice.setStatus('')
upsEventNotice=NotificationType((1,3,6,1,4,1,4526,22,300,0,70))
upsEventNotice.setObjects((_C,_S))
if mibBuilder.loadTexts:upsEventNotice.setStatus('')
volumeNotice=NotificationType((1,3,6,1,4,1,4526,22,300,0,80))
volumeNotice.setObjects((_C,_T))
if mibBuilder.loadTexts:volumeNotice.setStatus('')
diskTempWarning=NotificationType((1,3,6,1,4,1,4526,22,300,0,90))
diskTempWarning.setObjects((_C,_U))
if mibBuilder.loadTexts:diskTempWarning.setStatus('')
backupNotice=NotificationType((1,3,6,1,4,1,4526,22,300,0,100))
backupNotice.setObjects((_C,_V))
if mibBuilder.loadTexts:backupNotice.setStatus('')
diskSmartWarning=NotificationType((1,3,6,1,4,1,4526,22,300,0,110))
diskSmartWarning.setObjects((_C,_W))
if mibBuilder.loadTexts:diskSmartWarning.setStatus('')
psuWarning=NotificationType((1,3,6,1,4,1,4526,22,300,0,120))
psuWarning.setObjects((_C,_X))
if mibBuilder.loadTexts:psuWarning.setStatus('')
mibBuilder.exportSymbols(_C,**{'netgear':netgear,'ngNasManager':ngNasManager,'nasMgrSoftwareVersion':nasMgrSoftwareVersion,'diskTable':diskTable,'diskEntry':diskEntry,_H:diskNumber,'diskID':diskID,'diskSlotName':diskSlotName,'diskSerial':diskSerial,'diskModel':diskModel,'ataError':ataError,'diskCapacity':diskCapacity,'diskInterface':diskInterface,'diskState':diskState,'diskTemperature':diskTemperature,'fanTable':fanTable,'fanEntry':fanEntry,_I:fanNumber,'fanRPM':fanRPM,'fanStatus':fanStatus,'fanType':fanType,'temperatureTable':temperatureTable,'temperatureEntry':temperatureEntry,_J:temperatureNumber,'temperatureValue':temperatureValue,'temperatureTyoe':temperatureTyoe,'temperatureMin':temperatureMin,'temperatureMax':temperatureMax,'volumeTable':volumeTable,'volumeEntry':volumeEntry,_K:volumeNumber,'volumeName':volumeName,'volumeRAIDLevel':volumeRAIDLevel,'volumeStatus':volumeStatus,'volumeSize':volumeSize,'volumeFreeSpace':volumeFreeSpace,'psuTable':psuTable,'psuEntry':psuEntry,_L:psuNumber,'psuDesc':psuDesc,'psuStatus':psuStatus,'aryMgrEvts':aryMgrEvts,'controllerNameEv':controllerNameEv,'channelNumberEv':channelNumberEv,'targetIDEv':targetIDEv,'virtualDiskNameEv':virtualDiskNameEv,'arrayDiskNameEv':arrayDiskNameEv,'oldVDConfigEv':oldVDConfigEv,'newVDConfigEv':newVDConfigEv,'enclosureNumberEv':enclosureNumberEv,'unitNumberEv':unitNumberEv,'enclosureNameEv':enclosureNameEv,'unitNameEv':unitNameEv,'timeEv':timeEv,'volumeNameEv':volumeNameEv,'nasTraps':nasTraps,'fanFailure':fanFailure,'tempFailure':tempFailure,'powerVoltage':powerVoltage,'raidEventNotice':raidEventNotice,'snapshotEventNotice':snapshotEventNotice,'hotplugDiskNotice':hotplugDiskNotice,'upsEventNotice':upsEventNotice,'volumeNotice':volumeNotice,'diskTempWarning':diskTempWarning,'backupNotice':backupNotice,'diskSmartWarning':diskSmartWarning,'psuWarning':psuWarning,_M:fanFailureMesg,_N:tempFailureMesg,_O:powerVoltageMesg,_P:raidEventNoticeMesg,_Q:snapshotEventNoticeMesg,_S:upsEventNoticeMesg,_R:hotplugDiskNoticeMesg,_T:volumeNoticeMesg,_U:diskTempWarningMesg,_V:backupNoticeMesg,_W:diskSmartWarningMesg,_X:psuWarningMesg,'productID':productID,'ReadyDATAOS':ReadyDATAOS})