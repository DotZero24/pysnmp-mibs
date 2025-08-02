_F='dns340LUPSNum'
_E='dns340LDiskNum'
_D='dns340LVolumeNum'
_C='DNS-340L-MIB'
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
modelID=_ModelID_ObjectIdentity((1,3,6,1,4,1,171,50,1,10))
_SubmodelID_ObjectIdentity=ObjectIdentity
submodelID=_SubmodelID_ObjectIdentity((1,3,6,1,4,1,171,50,1,10,1))
_NasAgent_ObjectIdentity=ObjectIdentity
nasAgent=_NasAgent_ObjectIdentity((1,3,6,1,4,1,171,50,1,10,1,1))
_Dns340LAgentVer_Type=DisplayString
_Dns340LAgentVer_Object=MibScalar
dns340LAgentVer=_Dns340LAgentVer_Object((1,3,6,1,4,1,171,50,1,10,1,1,1),_Dns340LAgentVer_Type())
dns340LAgentVer.setMaxAccess(_B)
if mibBuilder.loadTexts:dns340LAgentVer.setStatus(_A)
_Dns340LSoftwareVersion_Type=DisplayString
_Dns340LSoftwareVersion_Object=MibScalar
dns340LSoftwareVersion=_Dns340LSoftwareVersion_Object((1,3,6,1,4,1,171,50,1,10,1,1,2),_Dns340LSoftwareVersion_Type())
dns340LSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:dns340LSoftwareVersion.setStatus(_A)
_Dns340LHostName_Type=DisplayString
_Dns340LHostName_Object=MibScalar
dns340LHostName=_Dns340LHostName_Object((1,3,6,1,4,1,171,50,1,10,1,1,3),_Dns340LHostName_Type())
dns340LHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:dns340LHostName.setStatus(_A)
_Dns340LFTPServer_Type=DisplayString
_Dns340LFTPServer_Object=MibScalar
dns340LFTPServer=_Dns340LFTPServer_Object((1,3,6,1,4,1,171,50,1,10,1,1,5),_Dns340LFTPServer_Type())
dns340LFTPServer.setMaxAccess(_B)
if mibBuilder.loadTexts:dns340LFTPServer.setStatus(_A)
_Dns340LNetType_Type=DisplayString
_Dns340LNetType_Object=MibScalar
dns340LNetType=_Dns340LNetType_Object((1,3,6,1,4,1,171,50,1,10,1,1,6),_Dns340LNetType_Type())
dns340LNetType.setMaxAccess(_B)
if mibBuilder.loadTexts:dns340LNetType.setStatus(_A)
_Dns340LTemperature_Type=DisplayString
_Dns340LTemperature_Object=MibScalar
dns340LTemperature=_Dns340LTemperature_Object((1,3,6,1,4,1,171,50,1,10,1,1,7),_Dns340LTemperature_Type())
dns340LTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:dns340LTemperature.setStatus(_A)
_Dns340LFanStatus_Type=DisplayString
_Dns340LFanStatus_Object=MibScalar
dns340LFanStatus=_Dns340LFanStatus_Object((1,3,6,1,4,1,171,50,1,10,1,1,8),_Dns340LFanStatus_Type())
dns340LFanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dns340LFanStatus.setStatus(_A)
_Dns340LVolumeTable_Object=MibTable
dns340LVolumeTable=_Dns340LVolumeTable_Object((1,3,6,1,4,1,171,50,1,10,1,1,9))
if mibBuilder.loadTexts:dns340LVolumeTable.setStatus(_A)
_Dns340LVolumeEntry_Object=MibTableRow
dns340LVolumeEntry=_Dns340LVolumeEntry_Object((1,3,6,1,4,1,171,50,1,10,1,1,9,1))
dns340LVolumeEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:dns340LVolumeEntry.setStatus(_A)
_Dns340LVolumeNum_Type=Integer32
_Dns340LVolumeNum_Object=MibTableColumn
dns340LVolumeNum=_Dns340LVolumeNum_Object((1,3,6,1,4,1,171,50,1,10,1,1,9,1,1),_Dns340LVolumeNum_Type())
dns340LVolumeNum.setMaxAccess(_B)
if mibBuilder.loadTexts:dns340LVolumeNum.setStatus(_A)
_Dns340LVolumeName_Type=DisplayString
_Dns340LVolumeName_Object=MibTableColumn
dns340LVolumeName=_Dns340LVolumeName_Object((1,3,6,1,4,1,171,50,1,10,1,1,9,1,2),_Dns340LVolumeName_Type())
dns340LVolumeName.setMaxAccess(_B)
if mibBuilder.loadTexts:dns340LVolumeName.setStatus(_A)
_Dns340LVolumeFsType_Type=DisplayString
_Dns340LVolumeFsType_Object=MibTableColumn
dns340LVolumeFsType=_Dns340LVolumeFsType_Object((1,3,6,1,4,1,171,50,1,10,1,1,9,1,3),_Dns340LVolumeFsType_Type())
dns340LVolumeFsType.setMaxAccess(_B)
if mibBuilder.loadTexts:dns340LVolumeFsType.setStatus(_A)
_Dns340LVolumeRaidLevel_Type=DisplayString
_Dns340LVolumeRaidLevel_Object=MibTableColumn
dns340LVolumeRaidLevel=_Dns340LVolumeRaidLevel_Object((1,3,6,1,4,1,171,50,1,10,1,1,9,1,4),_Dns340LVolumeRaidLevel_Type())
dns340LVolumeRaidLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:dns340LVolumeRaidLevel.setStatus(_A)
_Dns340LVolumeSize_Type=DisplayString
_Dns340LVolumeSize_Object=MibTableColumn
dns340LVolumeSize=_Dns340LVolumeSize_Object((1,3,6,1,4,1,171,50,1,10,1,1,9,1,5),_Dns340LVolumeSize_Type())
dns340LVolumeSize.setMaxAccess(_B)
if mibBuilder.loadTexts:dns340LVolumeSize.setStatus(_A)
_Dns340LVolumeFreeSpace_Type=DisplayString
_Dns340LVolumeFreeSpace_Object=MibTableColumn
dns340LVolumeFreeSpace=_Dns340LVolumeFreeSpace_Object((1,3,6,1,4,1,171,50,1,10,1,1,9,1,6),_Dns340LVolumeFreeSpace_Type())
dns340LVolumeFreeSpace.setMaxAccess(_B)
if mibBuilder.loadTexts:dns340LVolumeFreeSpace.setStatus(_A)
_Dns340LDiskTable_Object=MibTable
dns340LDiskTable=_Dns340LDiskTable_Object((1,3,6,1,4,1,171,50,1,10,1,1,10))
if mibBuilder.loadTexts:dns340LDiskTable.setStatus(_A)
_Dns340LDiskEntry_Object=MibTableRow
dns340LDiskEntry=_Dns340LDiskEntry_Object((1,3,6,1,4,1,171,50,1,10,1,1,10,1))
dns340LDiskEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:dns340LDiskEntry.setStatus(_A)
_Dns340LDiskNum_Type=Integer32
_Dns340LDiskNum_Object=MibTableColumn
dns340LDiskNum=_Dns340LDiskNum_Object((1,3,6,1,4,1,171,50,1,10,1,1,10,1,1),_Dns340LDiskNum_Type())
dns340LDiskNum.setMaxAccess(_B)
if mibBuilder.loadTexts:dns340LDiskNum.setStatus(_A)
_Dns340LDiskVendor_Type=DisplayString
_Dns340LDiskVendor_Object=MibTableColumn
dns340LDiskVendor=_Dns340LDiskVendor_Object((1,3,6,1,4,1,171,50,1,10,1,1,10,1,2),_Dns340LDiskVendor_Type())
dns340LDiskVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:dns340LDiskVendor.setStatus(_A)
_Dns340LDiskModel_Type=DisplayString
_Dns340LDiskModel_Object=MibTableColumn
dns340LDiskModel=_Dns340LDiskModel_Object((1,3,6,1,4,1,171,50,1,10,1,1,10,1,3),_Dns340LDiskModel_Type())
dns340LDiskModel.setMaxAccess(_B)
if mibBuilder.loadTexts:dns340LDiskModel.setStatus(_A)
_Dns340LDiskSerialNumber_Type=DisplayString
_Dns340LDiskSerialNumber_Object=MibTableColumn
dns340LDiskSerialNumber=_Dns340LDiskSerialNumber_Object((1,3,6,1,4,1,171,50,1,10,1,1,10,1,4),_Dns340LDiskSerialNumber_Type())
dns340LDiskSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:dns340LDiskSerialNumber.setStatus(_A)
_Dns340LDiskTemperature_Type=DisplayString
_Dns340LDiskTemperature_Object=MibTableColumn
dns340LDiskTemperature=_Dns340LDiskTemperature_Object((1,3,6,1,4,1,171,50,1,10,1,1,10,1,5),_Dns340LDiskTemperature_Type())
dns340LDiskTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:dns340LDiskTemperature.setStatus(_A)
_Dns340LDiskCapacity_Type=DisplayString
_Dns340LDiskCapacity_Object=MibTableColumn
dns340LDiskCapacity=_Dns340LDiskCapacity_Object((1,3,6,1,4,1,171,50,1,10,1,1,10,1,6),_Dns340LDiskCapacity_Type())
dns340LDiskCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:dns340LDiskCapacity.setStatus(_A)
_Dns340LUPSTable_Object=MibTable
dns340LUPSTable=_Dns340LUPSTable_Object((1,3,6,1,4,1,171,50,1,10,1,1,11))
if mibBuilder.loadTexts:dns340LUPSTable.setStatus(_A)
_Dns340LUPSEntry_Object=MibTableRow
dns340LUPSEntry=_Dns340LUPSEntry_Object((1,3,6,1,4,1,171,50,1,10,1,1,11,1))
dns340LUPSEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:dns340LUPSEntry.setStatus(_A)
_Dns340LUPSNum_Type=Integer32
_Dns340LUPSNum_Object=MibTableColumn
dns340LUPSNum=_Dns340LUPSNum_Object((1,3,6,1,4,1,171,50,1,10,1,1,11,1,1),_Dns340LUPSNum_Type())
dns340LUPSNum.setMaxAccess(_B)
if mibBuilder.loadTexts:dns340LUPSNum.setStatus(_A)
_Dns340LUPSMode_Type=DisplayString
_Dns340LUPSMode_Object=MibTableColumn
dns340LUPSMode=_Dns340LUPSMode_Object((1,3,6,1,4,1,171,50,1,10,1,1,11,1,2),_Dns340LUPSMode_Type())
dns340LUPSMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dns340LUPSMode.setStatus(_A)
_Dns340LUPSManufacturer_Type=DisplayString
_Dns340LUPSManufacturer_Object=MibTableColumn
dns340LUPSManufacturer=_Dns340LUPSManufacturer_Object((1,3,6,1,4,1,171,50,1,10,1,1,11,1,3),_Dns340LUPSManufacturer_Type())
dns340LUPSManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:dns340LUPSManufacturer.setStatus(_A)
_Dns340LUPSProduct_Type=DisplayString
_Dns340LUPSProduct_Object=MibTableColumn
dns340LUPSProduct=_Dns340LUPSProduct_Object((1,3,6,1,4,1,171,50,1,10,1,1,11,1,4),_Dns340LUPSProduct_Type())
dns340LUPSProduct.setMaxAccess(_B)
if mibBuilder.loadTexts:dns340LUPSProduct.setStatus(_A)
_Dns340LUPSBatteryCharge_Type=DisplayString
_Dns340LUPSBatteryCharge_Object=MibTableColumn
dns340LUPSBatteryCharge=_Dns340LUPSBatteryCharge_Object((1,3,6,1,4,1,171,50,1,10,1,1,11,1,5),_Dns340LUPSBatteryCharge_Type())
dns340LUPSBatteryCharge.setMaxAccess(_B)
if mibBuilder.loadTexts:dns340LUPSBatteryCharge.setStatus(_A)
_Dns340LUPSStatus_Type=DisplayString
_Dns340LUPSStatus_Object=MibTableColumn
dns340LUPSStatus=_Dns340LUPSStatus_Object((1,3,6,1,4,1,171,50,1,10,1,1,11,1,6),_Dns340LUPSStatus_Type())
dns340LUPSStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dns340LUPSStatus.setStatus(_A)
_NotifyEvts_ObjectIdentity=ObjectIdentity
notifyEvts=_NotifyEvts_ObjectIdentity((1,3,6,1,4,1,171,50,1,10,1,1,200))
notifyPasswdChanged=NotificationType((1,3,6,1,4,1,171,50,1,10,1,1,200,1))
if mibBuilder.loadTexts:notifyPasswdChanged.setStatus(_A)
notifyFirmwareUpgraded=NotificationType((1,3,6,1,4,1,171,50,1,10,1,1,200,2))
if mibBuilder.loadTexts:notifyFirmwareUpgraded.setStatus(_A)
notifyNetworkChanged=NotificationType((1,3,6,1,4,1,171,50,1,10,1,1,200,3))
if mibBuilder.loadTexts:notifyNetworkChanged.setStatus(_A)
notifyTemperatureExceeded=NotificationType((1,3,6,1,4,1,171,50,1,10,1,1,200,4))
if mibBuilder.loadTexts:notifyTemperatureExceeded.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'d-link':d_link,'productID':productID,'projectID':projectID,'modelID':modelID,'submodelID':submodelID,'nasAgent':nasAgent,'dns340LAgentVer':dns340LAgentVer,'dns340LSoftwareVersion':dns340LSoftwareVersion,'dns340LHostName':dns340LHostName,'dns340LFTPServer':dns340LFTPServer,'dns340LNetType':dns340LNetType,'dns340LTemperature':dns340LTemperature,'dns340LFanStatus':dns340LFanStatus,'dns340LVolumeTable':dns340LVolumeTable,'dns340LVolumeEntry':dns340LVolumeEntry,_D:dns340LVolumeNum,'dns340LVolumeName':dns340LVolumeName,'dns340LVolumeFsType':dns340LVolumeFsType,'dns340LVolumeRaidLevel':dns340LVolumeRaidLevel,'dns340LVolumeSize':dns340LVolumeSize,'dns340LVolumeFreeSpace':dns340LVolumeFreeSpace,'dns340LDiskTable':dns340LDiskTable,'dns340LDiskEntry':dns340LDiskEntry,_E:dns340LDiskNum,'dns340LDiskVendor':dns340LDiskVendor,'dns340LDiskModel':dns340LDiskModel,'dns340LDiskSerialNumber':dns340LDiskSerialNumber,'dns340LDiskTemperature':dns340LDiskTemperature,'dns340LDiskCapacity':dns340LDiskCapacity,'dns340LUPSTable':dns340LUPSTable,'dns340LUPSEntry':dns340LUPSEntry,_F:dns340LUPSNum,'dns340LUPSMode':dns340LUPSMode,'dns340LUPSManufacturer':dns340LUPSManufacturer,'dns340LUPSProduct':dns340LUPSProduct,'dns340LUPSBatteryCharge':dns340LUPSBatteryCharge,'dns340LUPSStatus':dns340LUPSStatus,'notifyEvts':notifyEvts,'notifyPasswdChanged':notifyPasswdChanged,'notifyFirmwareUpgraded':notifyFirmwareUpgraded,'notifyNetworkChanged':notifyNetworkChanged,'notifyTemperatureExceeded':notifyTemperatureExceeded})