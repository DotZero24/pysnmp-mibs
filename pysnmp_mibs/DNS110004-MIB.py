_P='aMAZONS3Num'
_O='iSCSIACLNum'
_N='iSCSILUNNum'
_M='iSCSITargetNum'
_L='uPSNum'
_K='logServerNum'
_J='iSONum'
_I='nFSNum'
_H='dFSNum'
_G='snapShotNum'
_F='volumeNum'
_E='diskNum'
_D='sysNum'
_C='DNS110004-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_D_link_ObjectIdentity=ObjectIdentity
d_link=_D_link_ObjectIdentity((1,3,6,1,4,1,171))
_ProductID_ObjectIdentity=ObjectIdentity
productID=_ProductID_ObjectIdentity((1,3,6,1,4,1,171,50))
_ProjectID_ObjectIdentity=ObjectIdentity
projectID=_ProjectID_ObjectIdentity((1,3,6,1,4,1,171,50,1))
_ModelID_ObjectIdentity=ObjectIdentity
modelID=_ModelID_ObjectIdentity((1,3,6,1,4,1,171,50,1,3))
_SubmodelID_ObjectIdentity=ObjectIdentity
submodelID=_SubmodelID_ObjectIdentity((1,3,6,1,4,1,171,50,1,3,1))
_NasAgent1100_ObjectIdentity=ObjectIdentity
nasAgent1100=_NasAgent1100_ObjectIdentity((1,3,6,1,4,1,171,50,1,3,1,1))
_NasAgentVer_Type=DisplayString
_NasAgentVer_Object=MibScalar
nasAgentVer=_NasAgentVer_Object((1,3,6,1,4,1,171,50,1,3,1,1,1),_NasAgentVer_Type())
nasAgentVer.setMaxAccess(_B)
if mibBuilder.loadTexts:nasAgentVer.setStatus(_A)
_SysTable_Object=MibTable
sysTable=_SysTable_Object((1,3,6,1,4,1,171,50,1,3,1,1,2))
if mibBuilder.loadTexts:sysTable.setStatus(_A)
_SysEntry_Object=MibTableRow
sysEntry=_SysEntry_Object((1,3,6,1,4,1,171,50,1,3,1,1,2,1))
sysEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:sysEntry.setStatus(_A)
_SysNum_Type=Integer32
_SysNum_Object=MibTableColumn
sysNum=_SysNum_Object((1,3,6,1,4,1,171,50,1,3,1,1,2,1,1),_SysNum_Type())
sysNum.setMaxAccess(_B)
if mibBuilder.loadTexts:sysNum.setStatus(_A)
_SysName_Type=DisplayString
_SysName_Object=MibTableColumn
sysName=_SysName_Object((1,3,6,1,4,1,171,50,1,3,1,1,2,1,2),_SysName_Type())
sysName.setMaxAccess(_B)
if mibBuilder.loadTexts:sysName.setStatus(_A)
_SysFWVer_Type=DisplayString
_SysFWVer_Object=MibTableColumn
sysFWVer=_SysFWVer_Object((1,3,6,1,4,1,171,50,1,3,1,1,2,1,3),_SysFWVer_Type())
sysFWVer.setMaxAccess(_B)
if mibBuilder.loadTexts:sysFWVer.setStatus(_A)
_SysNetType_Type=DisplayString
_SysNetType_Object=MibTableColumn
sysNetType=_SysNetType_Object((1,3,6,1,4,1,171,50,1,3,1,1,2,1,4),_SysNetType_Type())
sysNetType.setMaxAccess(_B)
if mibBuilder.loadTexts:sysNetType.setStatus(_A)
_SysFanSpeed_Type=DisplayString
_SysFanSpeed_Object=MibTableColumn
sysFanSpeed=_SysFanSpeed_Object((1,3,6,1,4,1,171,50,1,3,1,1,2,1,5),_SysFanSpeed_Type())
sysFanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:sysFanSpeed.setStatus(_A)
_SysTemperature_Type=DisplayString
_SysTemperature_Object=MibTableColumn
sysTemperature=_SysTemperature_Object((1,3,6,1,4,1,171,50,1,3,1,1,2,1,6),_SysTemperature_Type())
sysTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:sysTemperature.setStatus(_A)
_SysPrinterName_Type=DisplayString
_SysPrinterName_Object=MibTableColumn
sysPrinterName=_SysPrinterName_Object((1,3,6,1,4,1,171,50,1,3,1,1,2,1,7),_SysPrinterName_Type())
sysPrinterName.setMaxAccess(_B)
if mibBuilder.loadTexts:sysPrinterName.setStatus(_A)
_SysCIFS_Type=DisplayString
_SysCIFS_Object=MibTableColumn
sysCIFS=_SysCIFS_Object((1,3,6,1,4,1,171,50,1,3,1,1,2,1,8),_SysCIFS_Type())
sysCIFS.setMaxAccess(_B)
if mibBuilder.loadTexts:sysCIFS.setStatus(_A)
_SysFtpServer_Type=DisplayString
_SysFtpServer_Object=MibTableColumn
sysFtpServer=_SysFtpServer_Object((1,3,6,1,4,1,171,50,1,3,1,1,2,1,9),_SysFtpServer_Type())
sysFtpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:sysFtpServer.setStatus(_A)
_SysNFSServer_Type=DisplayString
_SysNFSServer_Object=MibTableColumn
sysNFSServer=_SysNFSServer_Object((1,3,6,1,4,1,171,50,1,3,1,1,2,1,10),_SysNFSServer_Type())
sysNFSServer.setMaxAccess(_B)
if mibBuilder.loadTexts:sysNFSServer.setStatus(_A)
_SysDFSServer_Type=DisplayString
_SysDFSServer_Object=MibTableColumn
sysDFSServer=_SysDFSServer_Object((1,3,6,1,4,1,171,50,1,3,1,1,2,1,11),_SysDFSServer_Type())
sysDFSServer.setMaxAccess(_B)
if mibBuilder.loadTexts:sysDFSServer.setStatus(_A)
_SysQuota_Type=DisplayString
_SysQuota_Object=MibTableColumn
sysQuota=_SysQuota_Object((1,3,6,1,4,1,171,50,1,3,1,1,2,1,12),_SysQuota_Type())
sysQuota.setMaxAccess(_B)
if mibBuilder.loadTexts:sysQuota.setStatus(_A)
_SysAFP_Type=DisplayString
_SysAFP_Object=MibTableColumn
sysAFP=_SysAFP_Object((1,3,6,1,4,1,171,50,1,3,1,1,2,1,13),_SysAFP_Type())
sysAFP.setMaxAccess(_B)
if mibBuilder.loadTexts:sysAFP.setStatus(_A)
_SysWebDAV_Type=DisplayString
_SysWebDAV_Object=MibTableColumn
sysWebDAV=_SysWebDAV_Object((1,3,6,1,4,1,171,50,1,3,1,1,2,1,14),_SysWebDAV_Type())
sysWebDAV.setMaxAccess(_B)
if mibBuilder.loadTexts:sysWebDAV.setStatus(_A)
_SysWebFileServer_Type=DisplayString
_SysWebFileServer_Object=MibTableColumn
sysWebFileServer=_SysWebFileServer_Object((1,3,6,1,4,1,171,50,1,3,1,1,2,1,15),_SysWebFileServer_Type())
sysWebFileServer.setMaxAccess(_B)
if mibBuilder.loadTexts:sysWebFileServer.setStatus(_A)
_SysiSCSITarget_Type=DisplayString
_SysiSCSITarget_Object=MibTableColumn
sysiSCSITarget=_SysiSCSITarget_Object((1,3,6,1,4,1,171,50,1,3,1,1,2,1,16),_SysiSCSITarget_Type())
sysiSCSITarget.setMaxAccess(_B)
if mibBuilder.loadTexts:sysiSCSITarget.setStatus(_A)
_SysiSNS_Type=DisplayString
_SysiSNS_Object=MibTableColumn
sysiSNS=_SysiSNS_Object((1,3,6,1,4,1,171,50,1,3,1,1,2,1,17),_SysiSNS_Type())
sysiSNS.setMaxAccess(_B)
if mibBuilder.loadTexts:sysiSNS.setStatus(_A)
_DiskTable_Object=MibTable
diskTable=_DiskTable_Object((1,3,6,1,4,1,171,50,1,3,1,1,3))
if mibBuilder.loadTexts:diskTable.setStatus(_A)
_DiskEntry_Object=MibTableRow
diskEntry=_DiskEntry_Object((1,3,6,1,4,1,171,50,1,3,1,1,3,1))
diskEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:diskEntry.setStatus(_A)
_DiskNum_Type=Integer32
_DiskNum_Object=MibTableColumn
diskNum=_DiskNum_Object((1,3,6,1,4,1,171,50,1,3,1,1,3,1,1),_DiskNum_Type())
diskNum.setMaxAccess(_B)
if mibBuilder.loadTexts:diskNum.setStatus(_A)
_DiskName_Type=DisplayString
_DiskName_Object=MibTableColumn
diskName=_DiskName_Object((1,3,6,1,4,1,171,50,1,3,1,1,3,1,2),_DiskName_Type())
diskName.setMaxAccess(_B)
if mibBuilder.loadTexts:diskName.setStatus(_A)
_DiskModel_Type=DisplayString
_DiskModel_Object=MibTableColumn
diskModel=_DiskModel_Object((1,3,6,1,4,1,171,50,1,3,1,1,3,1,3),_DiskModel_Type())
diskModel.setMaxAccess(_B)
if mibBuilder.loadTexts:diskModel.setStatus(_A)
_DiskTemperature_Type=DisplayString
_DiskTemperature_Object=MibTableColumn
diskTemperature=_DiskTemperature_Object((1,3,6,1,4,1,171,50,1,3,1,1,3,1,4),_DiskTemperature_Type())
diskTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:diskTemperature.setStatus(_A)
_DiskCapacity_Type=DisplayString
_DiskCapacity_Object=MibTableColumn
diskCapacity=_DiskCapacity_Object((1,3,6,1,4,1,171,50,1,3,1,1,3,1,5),_DiskCapacity_Type())
diskCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:diskCapacity.setStatus(_A)
_DiskStatus_Type=DisplayString
_DiskStatus_Object=MibTableColumn
diskStatus=_DiskStatus_Object((1,3,6,1,4,1,171,50,1,3,1,1,3,1,6),_DiskStatus_Type())
diskStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:diskStatus.setStatus(_A)
_VolumeTable_Object=MibTable
volumeTable=_VolumeTable_Object((1,3,6,1,4,1,171,50,1,3,1,1,4))
if mibBuilder.loadTexts:volumeTable.setStatus(_A)
_VolumeEntry_Object=MibTableRow
volumeEntry=_VolumeEntry_Object((1,3,6,1,4,1,171,50,1,3,1,1,4,1))
volumeEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:volumeEntry.setStatus(_A)
_VolumeNum_Type=Integer32
_VolumeNum_Object=MibTableColumn
volumeNum=_VolumeNum_Object((1,3,6,1,4,1,171,50,1,3,1,1,4,1,1),_VolumeNum_Type())
volumeNum.setMaxAccess(_B)
if mibBuilder.loadTexts:volumeNum.setStatus(_A)
_VolumeName_Type=DisplayString
_VolumeName_Object=MibTableColumn
volumeName=_VolumeName_Object((1,3,6,1,4,1,171,50,1,3,1,1,4,1,2),_VolumeName_Type())
volumeName.setMaxAccess(_B)
if mibBuilder.loadTexts:volumeName.setStatus(_A)
_VolumeEncryption_Type=DisplayString
_VolumeEncryption_Object=MibTableColumn
volumeEncryption=_VolumeEncryption_Object((1,3,6,1,4,1,171,50,1,3,1,1,4,1,3),_VolumeEncryption_Type())
volumeEncryption.setMaxAccess(_B)
if mibBuilder.loadTexts:volumeEncryption.setStatus(_A)
_VolumeFsType_Type=DisplayString
_VolumeFsType_Object=MibTableColumn
volumeFsType=_VolumeFsType_Object((1,3,6,1,4,1,171,50,1,3,1,1,4,1,4),_VolumeFsType_Type())
volumeFsType.setMaxAccess(_B)
if mibBuilder.loadTexts:volumeFsType.setStatus(_A)
_VolumeRaidLevel_Type=DisplayString
_VolumeRaidLevel_Object=MibTableColumn
volumeRaidLevel=_VolumeRaidLevel_Object((1,3,6,1,4,1,171,50,1,3,1,1,4,1,5),_VolumeRaidLevel_Type())
volumeRaidLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:volumeRaidLevel.setStatus(_A)
_VolumeSize_Type=DisplayString
_VolumeSize_Object=MibTableColumn
volumeSize=_VolumeSize_Object((1,3,6,1,4,1,171,50,1,3,1,1,4,1,6),_VolumeSize_Type())
volumeSize.setMaxAccess(_B)
if mibBuilder.loadTexts:volumeSize.setStatus(_A)
_VolumeFreeSpace_Type=DisplayString
_VolumeFreeSpace_Object=MibTableColumn
volumeFreeSpace=_VolumeFreeSpace_Object((1,3,6,1,4,1,171,50,1,3,1,1,4,1,7),_VolumeFreeSpace_Type())
volumeFreeSpace.setMaxAccess(_B)
if mibBuilder.loadTexts:volumeFreeSpace.setStatus(_A)
_VolumeState_Type=DisplayString
_VolumeState_Object=MibTableColumn
volumeState=_VolumeState_Object((1,3,6,1,4,1,171,50,1,3,1,1,4,1,8),_VolumeState_Type())
volumeState.setMaxAccess(_B)
if mibBuilder.loadTexts:volumeState.setStatus(_A)
_SnapShotTable_Object=MibTable
snapShotTable=_SnapShotTable_Object((1,3,6,1,4,1,171,50,1,3,1,1,5))
if mibBuilder.loadTexts:snapShotTable.setStatus(_A)
_SnapShotEntry_Object=MibTableRow
snapShotEntry=_SnapShotEntry_Object((1,3,6,1,4,1,171,50,1,3,1,1,5,1))
snapShotEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:snapShotEntry.setStatus(_A)
_SnapShotNum_Type=Integer32
_SnapShotNum_Object=MibTableColumn
snapShotNum=_SnapShotNum_Object((1,3,6,1,4,1,171,50,1,3,1,1,5,1,1),_SnapShotNum_Type())
snapShotNum.setMaxAccess(_B)
if mibBuilder.loadTexts:snapShotNum.setStatus(_A)
_SnapShotVolume_Type=DisplayString
_SnapShotVolume_Object=MibTableColumn
snapShotVolume=_SnapShotVolume_Object((1,3,6,1,4,1,171,50,1,3,1,1,5,1,2),_SnapShotVolume_Type())
snapShotVolume.setMaxAccess(_B)
if mibBuilder.loadTexts:snapShotVolume.setStatus(_A)
_SnapShotName_Type=DisplayString
_SnapShotName_Object=MibTableColumn
snapShotName=_SnapShotName_Object((1,3,6,1,4,1,171,50,1,3,1,1,5,1,3),_SnapShotName_Type())
snapShotName.setMaxAccess(_B)
if mibBuilder.loadTexts:snapShotName.setStatus(_A)
_SnapShotSchedule_Type=DisplayString
_SnapShotSchedule_Object=MibTableColumn
snapShotSchedule=_SnapShotSchedule_Object((1,3,6,1,4,1,171,50,1,3,1,1,5,1,4),_SnapShotSchedule_Type())
snapShotSchedule.setMaxAccess(_B)
if mibBuilder.loadTexts:snapShotSchedule.setStatus(_A)
_SnapShotCount_Type=DisplayString
_SnapShotCount_Object=MibTableColumn
snapShotCount=_SnapShotCount_Object((1,3,6,1,4,1,171,50,1,3,1,1,5,1,5),_SnapShotCount_Type())
snapShotCount.setMaxAccess(_B)
if mibBuilder.loadTexts:snapShotCount.setStatus(_A)
_SnapShotState_Type=DisplayString
_SnapShotState_Object=MibTableColumn
snapShotState=_SnapShotState_Object((1,3,6,1,4,1,171,50,1,3,1,1,5,1,6),_SnapShotState_Type())
snapShotState.setMaxAccess(_B)
if mibBuilder.loadTexts:snapShotState.setStatus(_A)
_SnapShotPath_Type=DisplayString
_SnapShotPath_Object=MibTableColumn
snapShotPath=_SnapShotPath_Object((1,3,6,1,4,1,171,50,1,3,1,1,5,1,7),_SnapShotPath_Type())
snapShotPath.setMaxAccess(_B)
if mibBuilder.loadTexts:snapShotPath.setStatus(_A)
_DFSTable_Object=MibTable
dFSTable=_DFSTable_Object((1,3,6,1,4,1,171,50,1,3,1,1,6))
if mibBuilder.loadTexts:dFSTable.setStatus(_A)
_DFSEntry_Object=MibTableRow
dFSEntry=_DFSEntry_Object((1,3,6,1,4,1,171,50,1,3,1,1,6,1))
dFSEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:dFSEntry.setStatus(_A)
_DFSNum_Type=Integer32
_DFSNum_Object=MibTableColumn
dFSNum=_DFSNum_Object((1,3,6,1,4,1,171,50,1,3,1,1,6,1,1),_DFSNum_Type())
dFSNum.setMaxAccess(_B)
if mibBuilder.loadTexts:dFSNum.setStatus(_A)
_DFSLShareName_Type=DisplayString
_DFSLShareName_Object=MibTableColumn
dFSLShareName=_DFSLShareName_Object((1,3,6,1,4,1,171,50,1,3,1,1,6,1,2),_DFSLShareName_Type())
dFSLShareName.setMaxAccess(_B)
if mibBuilder.loadTexts:dFSLShareName.setStatus(_A)
_DFSHost_Type=DisplayString
_DFSHost_Object=MibTableColumn
dFSHost=_DFSHost_Object((1,3,6,1,4,1,171,50,1,3,1,1,6,1,3),_DFSHost_Type())
dFSHost.setMaxAccess(_B)
if mibBuilder.loadTexts:dFSHost.setStatus(_A)
_DFSRSharefolder_Type=DisplayString
_DFSRSharefolder_Object=MibTableColumn
dFSRSharefolder=_DFSRSharefolder_Object((1,3,6,1,4,1,171,50,1,3,1,1,6,1,4),_DFSRSharefolder_Type())
dFSRSharefolder.setMaxAccess(_B)
if mibBuilder.loadTexts:dFSRSharefolder.setStatus(_A)
_NFSTable_Object=MibTable
nFSTable=_NFSTable_Object((1,3,6,1,4,1,171,50,1,3,1,1,7))
if mibBuilder.loadTexts:nFSTable.setStatus(_A)
_NFSEntry_Object=MibTableRow
nFSEntry=_NFSEntry_Object((1,3,6,1,4,1,171,50,1,3,1,1,7,1))
nFSEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:nFSEntry.setStatus(_A)
_NFSNum_Type=Integer32
_NFSNum_Object=MibTableColumn
nFSNum=_NFSNum_Object((1,3,6,1,4,1,171,50,1,3,1,1,7,1,1),_NFSNum_Type())
nFSNum.setMaxAccess(_B)
if mibBuilder.loadTexts:nFSNum.setStatus(_A)
_NFSMountPath_Type=DisplayString
_NFSMountPath_Object=MibTableColumn
nFSMountPath=_NFSMountPath_Object((1,3,6,1,4,1,171,50,1,3,1,1,7,1,2),_NFSMountPath_Type())
nFSMountPath.setMaxAccess(_B)
if mibBuilder.loadTexts:nFSMountPath.setStatus(_A)
_NFSHost_Type=DisplayString
_NFSHost_Object=MibTableColumn
nFSHost=_NFSHost_Object((1,3,6,1,4,1,171,50,1,3,1,1,7,1,3),_NFSHost_Type())
nFSHost.setMaxAccess(_B)
if mibBuilder.loadTexts:nFSHost.setStatus(_A)
_NFSPermission_Type=DisplayString
_NFSPermission_Object=MibTableColumn
nFSPermission=_NFSPermission_Object((1,3,6,1,4,1,171,50,1,3,1,1,7,1,4),_NFSPermission_Type())
nFSPermission.setMaxAccess(_B)
if mibBuilder.loadTexts:nFSPermission.setStatus(_A)
_NFSRootSquash_Type=DisplayString
_NFSRootSquash_Object=MibTableColumn
nFSRootSquash=_NFSRootSquash_Object((1,3,6,1,4,1,171,50,1,3,1,1,7,1,5),_NFSRootSquash_Type())
nFSRootSquash.setMaxAccess(_B)
if mibBuilder.loadTexts:nFSRootSquash.setStatus(_A)
_NFSStatus_Type=DisplayString
_NFSStatus_Object=MibTableColumn
nFSStatus=_NFSStatus_Object((1,3,6,1,4,1,171,50,1,3,1,1,7,1,6),_NFSStatus_Type())
nFSStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nFSStatus.setStatus(_A)
_ISOTable_Object=MibTable
iSOTable=_ISOTable_Object((1,3,6,1,4,1,171,50,1,3,1,1,8))
if mibBuilder.loadTexts:iSOTable.setStatus(_A)
_ISOEntry_Object=MibTableRow
iSOEntry=_ISOEntry_Object((1,3,6,1,4,1,171,50,1,3,1,1,8,1))
iSOEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:iSOEntry.setStatus(_A)
_ISONum_Type=Integer32
_ISONum_Object=MibTableColumn
iSONum=_ISONum_Object((1,3,6,1,4,1,171,50,1,3,1,1,8,1,1),_ISONum_Type())
iSONum.setMaxAccess(_B)
if mibBuilder.loadTexts:iSONum.setStatus(_A)
_ISOShareName_Type=DisplayString
_ISOShareName_Object=MibTableColumn
iSOShareName=_ISOShareName_Object((1,3,6,1,4,1,171,50,1,3,1,1,8,1,2),_ISOShareName_Type())
iSOShareName.setMaxAccess(_B)
if mibBuilder.loadTexts:iSOShareName.setStatus(_A)
_ISOPath_Type=DisplayString
_ISOPath_Object=MibTableColumn
iSOPath=_ISOPath_Object((1,3,6,1,4,1,171,50,1,3,1,1,8,1,3),_ISOPath_Type())
iSOPath.setMaxAccess(_B)
if mibBuilder.loadTexts:iSOPath.setStatus(_A)
_ISOStatus_Type=DisplayString
_ISOStatus_Object=MibTableColumn
iSOStatus=_ISOStatus_Object((1,3,6,1,4,1,171,50,1,3,1,1,8,1,4),_ISOStatus_Type())
iSOStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:iSOStatus.setStatus(_A)
_LogServerTable_Object=MibTable
logServerTable=_LogServerTable_Object((1,3,6,1,4,1,171,50,1,3,1,1,9))
if mibBuilder.loadTexts:logServerTable.setStatus(_A)
_LogServerEntry_Object=MibTableRow
logServerEntry=_LogServerEntry_Object((1,3,6,1,4,1,171,50,1,3,1,1,9,1))
logServerEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:logServerEntry.setStatus(_A)
_LogServerNum_Type=Integer32
_LogServerNum_Object=MibTableColumn
logServerNum=_LogServerNum_Object((1,3,6,1,4,1,171,50,1,3,1,1,9,1,1),_LogServerNum_Type())
logServerNum.setMaxAccess(_B)
if mibBuilder.loadTexts:logServerNum.setStatus(_A)
_LogServerRuleName_Type=DisplayString
_LogServerRuleName_Object=MibTableColumn
logServerRuleName=_LogServerRuleName_Object((1,3,6,1,4,1,171,50,1,3,1,1,9,1,2),_LogServerRuleName_Type())
logServerRuleName.setMaxAccess(_B)
if mibBuilder.loadTexts:logServerRuleName.setStatus(_A)
_LogServerLogfiles_Type=DisplayString
_LogServerLogfiles_Object=MibTableColumn
logServerLogfiles=_LogServerLogfiles_Object((1,3,6,1,4,1,171,50,1,3,1,1,9,1,3),_LogServerLogfiles_Type())
logServerLogfiles.setMaxAccess(_B)
if mibBuilder.loadTexts:logServerLogfiles.setStatus(_A)
_LogServerStatus_Type=DisplayString
_LogServerStatus_Object=MibTableColumn
logServerStatus=_LogServerStatus_Object((1,3,6,1,4,1,171,50,1,3,1,1,9,1,4),_LogServerStatus_Type())
logServerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:logServerStatus.setStatus(_A)
_UPSTable_Object=MibTable
uPSTable=_UPSTable_Object((1,3,6,1,4,1,171,50,1,3,1,1,10))
if mibBuilder.loadTexts:uPSTable.setStatus(_A)
_UPSEntry_Object=MibTableRow
uPSEntry=_UPSEntry_Object((1,3,6,1,4,1,171,50,1,3,1,1,10,1))
uPSEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:uPSEntry.setStatus(_A)
_UPSNum_Type=Integer32
_UPSNum_Object=MibTableColumn
uPSNum=_UPSNum_Object((1,3,6,1,4,1,171,50,1,3,1,1,10,1,1),_UPSNum_Type())
uPSNum.setMaxAccess(_B)
if mibBuilder.loadTexts:uPSNum.setStatus(_A)
_UPSDeviceInfo_Type=DisplayString
_UPSDeviceInfo_Object=MibTableColumn
uPSDeviceInfo=_UPSDeviceInfo_Object((1,3,6,1,4,1,171,50,1,3,1,1,10,1,2),_UPSDeviceInfo_Type())
uPSDeviceInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:uPSDeviceInfo.setStatus(_A)
_UPSProduct_Type=DisplayString
_UPSProduct_Object=MibTableColumn
uPSProduct=_UPSProduct_Object((1,3,6,1,4,1,171,50,1,3,1,1,10,1,3),_UPSProduct_Type())
uPSProduct.setMaxAccess(_B)
if mibBuilder.loadTexts:uPSProduct.setStatus(_A)
_UPSManufacturer_Type=DisplayString
_UPSManufacturer_Object=MibTableColumn
uPSManufacturer=_UPSManufacturer_Object((1,3,6,1,4,1,171,50,1,3,1,1,10,1,4),_UPSManufacturer_Type())
uPSManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:uPSManufacturer.setStatus(_A)
_UPSBattery_Type=DisplayString
_UPSBattery_Object=MibTableColumn
uPSBattery=_UPSBattery_Object((1,3,6,1,4,1,171,50,1,3,1,1,10,1,5),_UPSBattery_Type())
uPSBattery.setMaxAccess(_B)
if mibBuilder.loadTexts:uPSBattery.setStatus(_A)
_UPSState_Type=DisplayString
_UPSState_Object=MibTableColumn
uPSState=_UPSState_Object((1,3,6,1,4,1,171,50,1,3,1,1,10,1,6),_UPSState_Type())
uPSState.setMaxAccess(_B)
if mibBuilder.loadTexts:uPSState.setStatus(_A)
_UPSServerIP_Type=DisplayString
_UPSServerIP_Object=MibTableColumn
uPSServerIP=_UPSServerIP_Object((1,3,6,1,4,1,171,50,1,3,1,1,10,1,7),_UPSServerIP_Type())
uPSServerIP.setMaxAccess(_B)
if mibBuilder.loadTexts:uPSServerIP.setStatus(_A)
_UPSAllowedIP_Type=DisplayString
_UPSAllowedIP_Object=MibTableColumn
uPSAllowedIP=_UPSAllowedIP_Object((1,3,6,1,4,1,171,50,1,3,1,1,10,1,8),_UPSAllowedIP_Type())
uPSAllowedIP.setMaxAccess(_B)
if mibBuilder.loadTexts:uPSAllowedIP.setStatus(_A)
_VVTable_Object=MibTable
vVTable=_VVTable_Object((1,3,6,1,4,1,171,50,1,3,1,1,11))
if mibBuilder.loadTexts:vVTable.setStatus(_A)
_VVEntry_Object=MibTableRow
vVEntry=_VVEntry_Object((1,3,6,1,4,1,171,50,1,3,1,1,11,1))
vVEntry.setIndexNames((0,_C,'vVNum'))
if mibBuilder.loadTexts:vVEntry.setStatus(_A)
_VVNum_Type=Integer32
_VVNum_Object=MibTableColumn
vVNum=_VVNum_Object((1,3,6,1,4,1,171,50,1,3,1,1,11,1,1),_VVNum_Type())
vVNum.setMaxAccess(_B)
if mibBuilder.loadTexts:vVNum.setStatus(_A)
_VVTargetName_Type=DisplayString
_VVTargetName_Object=MibTableColumn
vVTargetName=_VVTargetName_Object((1,3,6,1,4,1,171,50,1,3,1,1,11,1,2),_VVTargetName_Type())
vVTargetName.setMaxAccess(_B)
if mibBuilder.loadTexts:vVTargetName.setStatus(_A)
_VVSharefolder_Type=DisplayString
_VVSharefolder_Object=MibTableColumn
vVSharefolder=_VVSharefolder_Object((1,3,6,1,4,1,171,50,1,3,1,1,11,1,3),_VVSharefolder_Type())
vVSharefolder.setMaxAccess(_B)
if mibBuilder.loadTexts:vVSharefolder.setStatus(_A)
_VVStatus_Type=DisplayString
_VVStatus_Object=MibTableColumn
vVStatus=_VVStatus_Object((1,3,6,1,4,1,171,50,1,3,1,1,11,1,4),_VVStatus_Type())
vVStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vVStatus.setStatus(_A)
_VVSize_Type=DisplayString
_VVSize_Object=MibTableColumn
vVSize=_VVSize_Object((1,3,6,1,4,1,171,50,1,3,1,1,11,1,5),_VVSize_Type())
vVSize.setMaxAccess(_B)
if mibBuilder.loadTexts:vVSize.setStatus(_A)
_ISCSITargetTable_Object=MibTable
iSCSITargetTable=_ISCSITargetTable_Object((1,3,6,1,4,1,171,50,1,3,1,1,12))
if mibBuilder.loadTexts:iSCSITargetTable.setStatus(_A)
_ISCSITargetEntry_Object=MibTableRow
iSCSITargetEntry=_ISCSITargetEntry_Object((1,3,6,1,4,1,171,50,1,3,1,1,12,1))
iSCSITargetEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:iSCSITargetEntry.setStatus(_A)
_ISCSITargetNum_Type=Integer32
_ISCSITargetNum_Object=MibTableColumn
iSCSITargetNum=_ISCSITargetNum_Object((1,3,6,1,4,1,171,50,1,3,1,1,12,1,1),_ISCSITargetNum_Type())
iSCSITargetNum.setMaxAccess(_B)
if mibBuilder.loadTexts:iSCSITargetNum.setStatus(_A)
_ISCSITargetIQN_Type=DisplayString
_ISCSITargetIQN_Object=MibTableColumn
iSCSITargetIQN=_ISCSITargetIQN_Object((1,3,6,1,4,1,171,50,1,3,1,1,12,1,2),_ISCSITargetIQN_Type())
iSCSITargetIQN.setMaxAccess(_B)
if mibBuilder.loadTexts:iSCSITargetIQN.setStatus(_A)
_ISCSITargetStatus_Type=DisplayString
_ISCSITargetStatus_Object=MibTableColumn
iSCSITargetStatus=_ISCSITargetStatus_Object((1,3,6,1,4,1,171,50,1,3,1,1,12,1,3),_ISCSITargetStatus_Type())
iSCSITargetStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:iSCSITargetStatus.setStatus(_A)
_ISCSILUNTable_Object=MibTable
iSCSILUNTable=_ISCSILUNTable_Object((1,3,6,1,4,1,171,50,1,3,1,1,13))
if mibBuilder.loadTexts:iSCSILUNTable.setStatus(_A)
_ISCSILUNEntry_Object=MibTableRow
iSCSILUNEntry=_ISCSILUNEntry_Object((1,3,6,1,4,1,171,50,1,3,1,1,13,1))
iSCSILUNEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:iSCSILUNEntry.setStatus(_A)
_ISCSILUNNum_Type=Integer32
_ISCSILUNNum_Object=MibTableColumn
iSCSILUNNum=_ISCSILUNNum_Object((1,3,6,1,4,1,171,50,1,3,1,1,13,1,1),_ISCSILUNNum_Type())
iSCSILUNNum.setMaxAccess(_B)
if mibBuilder.loadTexts:iSCSILUNNum.setStatus(_A)
_ISCSILUNName_Type=DisplayString
_ISCSILUNName_Object=MibTableColumn
iSCSILUNName=_ISCSILUNName_Object((1,3,6,1,4,1,171,50,1,3,1,1,13,1,2),_ISCSILUNName_Type())
iSCSILUNName.setMaxAccess(_B)
if mibBuilder.loadTexts:iSCSILUNName.setStatus(_A)
_ISCSILUNVolume_Type=DisplayString
_ISCSILUNVolume_Object=MibTableColumn
iSCSILUNVolume=_ISCSILUNVolume_Object((1,3,6,1,4,1,171,50,1,3,1,1,13,1,3),_ISCSILUNVolume_Type())
iSCSILUNVolume.setMaxAccess(_B)
if mibBuilder.loadTexts:iSCSILUNVolume.setStatus(_A)
_ISCSILUNSize_Type=DisplayString
_ISCSILUNSize_Object=MibTableColumn
iSCSILUNSize=_ISCSILUNSize_Object((1,3,6,1,4,1,171,50,1,3,1,1,13,1,4),_ISCSILUNSize_Type())
iSCSILUNSize.setMaxAccess(_B)
if mibBuilder.loadTexts:iSCSILUNSize.setStatus(_A)
_ISCSILUNStatus_Type=DisplayString
_ISCSILUNStatus_Object=MibTableColumn
iSCSILUNStatus=_ISCSILUNStatus_Object((1,3,6,1,4,1,171,50,1,3,1,1,13,1,5),_ISCSILUNStatus_Type())
iSCSILUNStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:iSCSILUNStatus.setStatus(_A)
_ISCSILUNMapping_Type=DisplayString
_ISCSILUNMapping_Object=MibTableColumn
iSCSILUNMapping=_ISCSILUNMapping_Object((1,3,6,1,4,1,171,50,1,3,1,1,13,1,6),_ISCSILUNMapping_Type())
iSCSILUNMapping.setMaxAccess(_B)
if mibBuilder.loadTexts:iSCSILUNMapping.setStatus(_A)
_ISCSIACLTable_Object=MibTable
iSCSIACLTable=_ISCSIACLTable_Object((1,3,6,1,4,1,171,50,1,3,1,1,14))
if mibBuilder.loadTexts:iSCSIACLTable.setStatus(_A)
_ISCSIACLEntry_Object=MibTableRow
iSCSIACLEntry=_ISCSIACLEntry_Object((1,3,6,1,4,1,171,50,1,3,1,1,14,1))
iSCSIACLEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:iSCSIACLEntry.setStatus(_A)
_ISCSIACLNum_Type=Integer32
_ISCSIACLNum_Object=MibTableColumn
iSCSIACLNum=_ISCSIACLNum_Object((1,3,6,1,4,1,171,50,1,3,1,1,14,1,1),_ISCSIACLNum_Type())
iSCSIACLNum.setMaxAccess(_B)
if mibBuilder.loadTexts:iSCSIACLNum.setStatus(_A)
_ISCSIACLName_Type=DisplayString
_ISCSIACLName_Object=MibTableColumn
iSCSIACLName=_ISCSIACLName_Object((1,3,6,1,4,1,171,50,1,3,1,1,14,1,2),_ISCSIACLName_Type())
iSCSIACLName.setMaxAccess(_B)
if mibBuilder.loadTexts:iSCSIACLName.setStatus(_A)
_ISCSIACLInitiator_Type=DisplayString
_ISCSIACLInitiator_Object=MibTableColumn
iSCSIACLInitiator=_ISCSIACLInitiator_Object((1,3,6,1,4,1,171,50,1,3,1,1,14,1,3),_ISCSIACLInitiator_Type())
iSCSIACLInitiator.setMaxAccess(_B)
if mibBuilder.loadTexts:iSCSIACLInitiator.setStatus(_A)
_AMAZONS3Table_Object=MibTable
aMAZONS3Table=_AMAZONS3Table_Object((1,3,6,1,4,1,171,50,1,3,1,1,15))
if mibBuilder.loadTexts:aMAZONS3Table.setStatus(_A)
_AMAZONS3Entry_Object=MibTableRow
aMAZONS3Entry=_AMAZONS3Entry_Object((1,3,6,1,4,1,171,50,1,3,1,1,15,1))
aMAZONS3Entry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:aMAZONS3Entry.setStatus(_A)
_AMAZONS3Num_Type=Integer32
_AMAZONS3Num_Object=MibTableColumn
aMAZONS3Num=_AMAZONS3Num_Object((1,3,6,1,4,1,171,50,1,3,1,1,15,1,1),_AMAZONS3Num_Type())
aMAZONS3Num.setMaxAccess(_B)
if mibBuilder.loadTexts:aMAZONS3Num.setStatus(_A)
_AMAZONS3Task_Type=DisplayString
_AMAZONS3Task_Object=MibTableColumn
aMAZONS3Task=_AMAZONS3Task_Object((1,3,6,1,4,1,171,50,1,3,1,1,15,1,2),_AMAZONS3Task_Type())
aMAZONS3Task.setMaxAccess(_B)
if mibBuilder.loadTexts:aMAZONS3Task.setStatus(_A)
_AMAZONS3Schedule_Type=DisplayString
_AMAZONS3Schedule_Object=MibTableColumn
aMAZONS3Schedule=_AMAZONS3Schedule_Object((1,3,6,1,4,1,171,50,1,3,1,1,15,1,3),_AMAZONS3Schedule_Type())
aMAZONS3Schedule.setMaxAccess(_B)
if mibBuilder.loadTexts:aMAZONS3Schedule.setStatus(_A)
_AMAZONS3Status_Type=DisplayString
_AMAZONS3Status_Object=MibTableColumn
aMAZONS3Status=_AMAZONS3Status_Object((1,3,6,1,4,1,171,50,1,3,1,1,15,1,4),_AMAZONS3Status_Type())
aMAZONS3Status.setMaxAccess(_B)
if mibBuilder.loadTexts:aMAZONS3Status.setStatus(_A)
_AMAZONS3Enable_Type=DisplayString
_AMAZONS3Enable_Object=MibTableColumn
aMAZONS3Enable=_AMAZONS3Enable_Object((1,3,6,1,4,1,171,50,1,3,1,1,15,1,5),_AMAZONS3Enable_Type())
aMAZONS3Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:aMAZONS3Enable.setStatus(_A)
_AMAZONS3BackupNow_Type=DisplayString
_AMAZONS3BackupNow_Object=MibTableColumn
aMAZONS3BackupNow=_AMAZONS3BackupNow_Object((1,3,6,1,4,1,171,50,1,3,1,1,15,1,6),_AMAZONS3BackupNow_Type())
aMAZONS3BackupNow.setMaxAccess(_B)
if mibBuilder.loadTexts:aMAZONS3BackupNow.setStatus(_A)
_AMAZONS3Restore_Type=DisplayString
_AMAZONS3Restore_Object=MibTableColumn
aMAZONS3Restore=_AMAZONS3Restore_Object((1,3,6,1,4,1,171,50,1,3,1,1,15,1,7),_AMAZONS3Restore_Type())
aMAZONS3Restore.setMaxAccess(_B)
if mibBuilder.loadTexts:aMAZONS3Restore.setStatus(_A)
_NotifyEvts_ObjectIdentity=ObjectIdentity
notifyEvts=_NotifyEvts_ObjectIdentity((1,3,6,1,4,1,171,50,1,3,1,1,200))
notifyPasswdChanged=NotificationType((1,3,6,1,4,1,171,50,1,3,1,1,200,1))
if mibBuilder.loadTexts:notifyPasswdChanged.setStatus(_A)
notifyNetworketh0Changed=NotificationType((1,3,6,1,4,1,171,50,1,3,1,1,200,2))
if mibBuilder.loadTexts:notifyNetworketh0Changed.setStatus(_A)
notifyNetworketh1Changed=NotificationType((1,3,6,1,4,1,171,50,1,3,1,1,200,3))
if mibBuilder.loadTexts:notifyNetworketh1Changed.setStatus(_A)
notifyTemperatureExceeded=NotificationType((1,3,6,1,4,1,171,50,1,3,1,1,200,4))
if mibBuilder.loadTexts:notifyTemperatureExceeded.setStatus(_A)
notifyPowerFailure=NotificationType((1,3,6,1,4,1,171,50,1,3,1,1,200,5))
if mibBuilder.loadTexts:notifyPowerFailure.setStatus(_A)
notifyFirmwareUpgraded=NotificationType((1,3,6,1,4,1,171,50,1,3,1,1,200,6))
if mibBuilder.loadTexts:notifyFirmwareUpgraded.setStatus(_A)
notifyDiskLost=NotificationType((1,3,6,1,4,1,171,50,1,3,1,1,200,7))
if mibBuilder.loadTexts:notifyDiskLost.setStatus(_A)
notifyDiskInsertion=NotificationType((1,3,6,1,4,1,171,50,1,3,1,1,200,8))
if mibBuilder.loadTexts:notifyDiskInsertion.setStatus(_A)
notifyRaidFailed=NotificationType((1,3,6,1,4,1,171,50,1,3,1,1,200,9))
if mibBuilder.loadTexts:notifyRaidFailed.setStatus(_A)
notifyVolumeCreateSuccess=NotificationType((1,3,6,1,4,1,171,50,1,3,1,1,200,10))
if mibBuilder.loadTexts:notifyVolumeCreateSuccess.setStatus(_A)
notifyVolumeCreateFailed=NotificationType((1,3,6,1,4,1,171,50,1,3,1,1,200,11))
if mibBuilder.loadTexts:notifyVolumeCreateFailed.setStatus(_A)
notifyVolumeRemoveSuccess=NotificationType((1,3,6,1,4,1,171,50,1,3,1,1,200,12))
if mibBuilder.loadTexts:notifyVolumeRemoveSuccess.setStatus(_A)
notifyVolumeRemoveFailed=NotificationType((1,3,6,1,4,1,171,50,1,3,1,1,200,13))
if mibBuilder.loadTexts:notifyVolumeRemoveFailed.setStatus(_A)
notifyVolumeStatusCrashed=NotificationType((1,3,6,1,4,1,171,50,1,3,1,1,200,14))
if mibBuilder.loadTexts:notifyVolumeStatusCrashed.setStatus(_A)
notifyVolumeStatusDegraded=NotificationType((1,3,6,1,4,1,171,50,1,3,1,1,200,15))
if mibBuilder.loadTexts:notifyVolumeStatusDegraded.setStatus(_A)
notifyVolumeStatusREBUILD=NotificationType((1,3,6,1,4,1,171,50,1,3,1,1,200,16))
if mibBuilder.loadTexts:notifyVolumeStatusREBUILD.setStatus(_A)
notifyVolumeStatusREBUILT=NotificationType((1,3,6,1,4,1,171,50,1,3,1,1,200,17))
if mibBuilder.loadTexts:notifyVolumeStatusREBUILT.setStatus(_A)
notifyHDFull=NotificationType((1,3,6,1,4,1,171,50,1,3,1,1,200,18))
if mibBuilder.loadTexts:notifyHDFull.setStatus(_A)
notifyVolumeSpace=NotificationType((1,3,6,1,4,1,171,50,1,3,1,1,200,19))
if mibBuilder.loadTexts:notifyVolumeSpace.setStatus(_A)
notifySeleftest=NotificationType((1,3,6,1,4,1,171,50,1,3,1,1,200,20))
if mibBuilder.loadTexts:notifySeleftest.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'d-link':d_link,'productID':productID,'projectID':projectID,'modelID':modelID,'submodelID':submodelID,'nasAgent1100':nasAgent1100,'nasAgentVer':nasAgentVer,'sysTable':sysTable,'sysEntry':sysEntry,_D:sysNum,'sysName':sysName,'sysFWVer':sysFWVer,'sysNetType':sysNetType,'sysFanSpeed':sysFanSpeed,'sysTemperature':sysTemperature,'sysPrinterName':sysPrinterName,'sysCIFS':sysCIFS,'sysFtpServer':sysFtpServer,'sysNFSServer':sysNFSServer,'sysDFSServer':sysDFSServer,'sysQuota':sysQuota,'sysAFP':sysAFP,'sysWebDAV':sysWebDAV,'sysWebFileServer':sysWebFileServer,'sysiSCSITarget':sysiSCSITarget,'sysiSNS':sysiSNS,'diskTable':diskTable,'diskEntry':diskEntry,_E:diskNum,'diskName':diskName,'diskModel':diskModel,'diskTemperature':diskTemperature,'diskCapacity':diskCapacity,'diskStatus':diskStatus,'volumeTable':volumeTable,'volumeEntry':volumeEntry,_F:volumeNum,'volumeName':volumeName,'volumeEncryption':volumeEncryption,'volumeFsType':volumeFsType,'volumeRaidLevel':volumeRaidLevel,'volumeSize':volumeSize,'volumeFreeSpace':volumeFreeSpace,'volumeState':volumeState,'snapShotTable':snapShotTable,'snapShotEntry':snapShotEntry,_G:snapShotNum,'snapShotVolume':snapShotVolume,'snapShotName':snapShotName,'snapShotSchedule':snapShotSchedule,'snapShotCount':snapShotCount,'snapShotState':snapShotState,'snapShotPath':snapShotPath,'dFSTable':dFSTable,'dFSEntry':dFSEntry,_H:dFSNum,'dFSLShareName':dFSLShareName,'dFSHost':dFSHost,'dFSRSharefolder':dFSRSharefolder,'nFSTable':nFSTable,'nFSEntry':nFSEntry,_I:nFSNum,'nFSMountPath':nFSMountPath,'nFSHost':nFSHost,'nFSPermission':nFSPermission,'nFSRootSquash':nFSRootSquash,'nFSStatus':nFSStatus,'iSOTable':iSOTable,'iSOEntry':iSOEntry,_J:iSONum,'iSOShareName':iSOShareName,'iSOPath':iSOPath,'iSOStatus':iSOStatus,'logServerTable':logServerTable,'logServerEntry':logServerEntry,_K:logServerNum,'logServerRuleName':logServerRuleName,'logServerLogfiles':logServerLogfiles,'logServerStatus':logServerStatus,'uPSTable':uPSTable,'uPSEntry':uPSEntry,_L:uPSNum,'uPSDeviceInfo':uPSDeviceInfo,'uPSProduct':uPSProduct,'uPSManufacturer':uPSManufacturer,'uPSBattery':uPSBattery,'uPSState':uPSState,'uPSServerIP':uPSServerIP,'uPSAllowedIP':uPSAllowedIP,'vVTable':vVTable,'vVEntry':vVEntry,'vVNum':vVNum,'vVTargetName':vVTargetName,'vVSharefolder':vVSharefolder,'vVStatus':vVStatus,'vVSize':vVSize,'iSCSITargetTable':iSCSITargetTable,'iSCSITargetEntry':iSCSITargetEntry,_M:iSCSITargetNum,'iSCSITargetIQN':iSCSITargetIQN,'iSCSITargetStatus':iSCSITargetStatus,'iSCSILUNTable':iSCSILUNTable,'iSCSILUNEntry':iSCSILUNEntry,_N:iSCSILUNNum,'iSCSILUNName':iSCSILUNName,'iSCSILUNVolume':iSCSILUNVolume,'iSCSILUNSize':iSCSILUNSize,'iSCSILUNStatus':iSCSILUNStatus,'iSCSILUNMapping':iSCSILUNMapping,'iSCSIACLTable':iSCSIACLTable,'iSCSIACLEntry':iSCSIACLEntry,_O:iSCSIACLNum,'iSCSIACLName':iSCSIACLName,'iSCSIACLInitiator':iSCSIACLInitiator,'aMAZONS3Table':aMAZONS3Table,'aMAZONS3Entry':aMAZONS3Entry,_P:aMAZONS3Num,'aMAZONS3Task':aMAZONS3Task,'aMAZONS3Schedule':aMAZONS3Schedule,'aMAZONS3Status':aMAZONS3Status,'aMAZONS3Enable':aMAZONS3Enable,'aMAZONS3BackupNow':aMAZONS3BackupNow,'aMAZONS3Restore':aMAZONS3Restore,'notifyEvts':notifyEvts,'notifyPasswdChanged':notifyPasswdChanged,'notifyNetworketh0Changed':notifyNetworketh0Changed,'notifyNetworketh1Changed':notifyNetworketh1Changed,'notifyTemperatureExceeded':notifyTemperatureExceeded,'notifyPowerFailure':notifyPowerFailure,'notifyFirmwareUpgraded':notifyFirmwareUpgraded,'notifyDiskLost':notifyDiskLost,'notifyDiskInsertion':notifyDiskInsertion,'notifyRaidFailed':notifyRaidFailed,'notifyVolumeCreateSuccess':notifyVolumeCreateSuccess,'notifyVolumeCreateFailed':notifyVolumeCreateFailed,'notifyVolumeRemoveSuccess':notifyVolumeRemoveSuccess,'notifyVolumeRemoveFailed':notifyVolumeRemoveFailed,'notifyVolumeStatusCrashed':notifyVolumeStatusCrashed,'notifyVolumeStatusDegraded':notifyVolumeStatusDegraded,'notifyVolumeStatusREBUILD':notifyVolumeStatusREBUILD,'notifyVolumeStatusREBUILT':notifyVolumeStatusREBUILT,'notifyHDFull':notifyHDFull,'notifyVolumeSpace':notifyVolumeSpace,'notifySeleftest':notifySeleftest})