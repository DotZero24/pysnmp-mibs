_E='dns343DiskNum'
_D='dns343VolumeNum'
_C='DNS343-MIB'
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
modelID=_ModelID_ObjectIdentity((1,3,6,1,4,1,171,50,1,4))
_SubmodelID_ObjectIdentity=ObjectIdentity
submodelID=_SubmodelID_ObjectIdentity((1,3,6,1,4,1,171,50,1,4,1))
_NasAgent_ObjectIdentity=ObjectIdentity
nasAgent=_NasAgent_ObjectIdentity((1,3,6,1,4,1,171,50,1,4,1,1))
_Dns343AgentVer_Type=DisplayString
_Dns343AgentVer_Object=MibScalar
dns343AgentVer=_Dns343AgentVer_Object((1,3,6,1,4,1,171,50,1,4,1,1,1),_Dns343AgentVer_Type())
dns343AgentVer.setMaxAccess(_B)
if mibBuilder.loadTexts:dns343AgentVer.setStatus(_A)
_Dns343SoftwareVersion_Type=DisplayString
_Dns343SoftwareVersion_Object=MibScalar
dns343SoftwareVersion=_Dns343SoftwareVersion_Object((1,3,6,1,4,1,171,50,1,4,1,1,2),_Dns343SoftwareVersion_Type())
dns343SoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:dns343SoftwareVersion.setStatus(_A)
_Dns343HostName_Type=DisplayString
_Dns343HostName_Object=MibScalar
dns343HostName=_Dns343HostName_Object((1,3,6,1,4,1,171,50,1,4,1,1,3),_Dns343HostName_Type())
dns343HostName.setMaxAccess(_B)
if mibBuilder.loadTexts:dns343HostName.setStatus(_A)
_Dns343DHCPServer_Type=DisplayString
_Dns343DHCPServer_Object=MibScalar
dns343DHCPServer=_Dns343DHCPServer_Object((1,3,6,1,4,1,171,50,1,4,1,1,4),_Dns343DHCPServer_Type())
dns343DHCPServer.setMaxAccess(_B)
if mibBuilder.loadTexts:dns343DHCPServer.setStatus(_A)
_Dns343FTPServer_Type=DisplayString
_Dns343FTPServer_Object=MibScalar
dns343FTPServer=_Dns343FTPServer_Object((1,3,6,1,4,1,171,50,1,4,1,1,5),_Dns343FTPServer_Type())
dns343FTPServer.setMaxAccess(_B)
if mibBuilder.loadTexts:dns343FTPServer.setStatus(_A)
_Dns343NetType_Type=DisplayString
_Dns343NetType_Object=MibScalar
dns343NetType=_Dns343NetType_Object((1,3,6,1,4,1,171,50,1,4,1,1,6),_Dns343NetType_Type())
dns343NetType.setMaxAccess(_B)
if mibBuilder.loadTexts:dns343NetType.setStatus(_A)
_Dns343Temperature_Type=DisplayString
_Dns343Temperature_Object=MibScalar
dns343Temperature=_Dns343Temperature_Object((1,3,6,1,4,1,171,50,1,4,1,1,7),_Dns343Temperature_Type())
dns343Temperature.setMaxAccess(_B)
if mibBuilder.loadTexts:dns343Temperature.setStatus(_A)
_Dns343FanStatus_Type=DisplayString
_Dns343FanStatus_Object=MibScalar
dns343FanStatus=_Dns343FanStatus_Object((1,3,6,1,4,1,171,50,1,4,1,1,8),_Dns343FanStatus_Type())
dns343FanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:dns343FanStatus.setStatus(_A)
_Dns343VolumeTable_Object=MibTable
dns343VolumeTable=_Dns343VolumeTable_Object((1,3,6,1,4,1,171,50,1,4,1,1,9))
if mibBuilder.loadTexts:dns343VolumeTable.setStatus(_A)
_Dns343VolumeEntry_Object=MibTableRow
dns343VolumeEntry=_Dns343VolumeEntry_Object((1,3,6,1,4,1,171,50,1,4,1,1,9,1))
dns343VolumeEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:dns343VolumeEntry.setStatus(_A)
_Dns343VolumeNum_Type=Integer32
_Dns343VolumeNum_Object=MibTableColumn
dns343VolumeNum=_Dns343VolumeNum_Object((1,3,6,1,4,1,171,50,1,4,1,1,9,1,1),_Dns343VolumeNum_Type())
dns343VolumeNum.setMaxAccess(_B)
if mibBuilder.loadTexts:dns343VolumeNum.setStatus(_A)
_Dns343VolumeName_Type=DisplayString
_Dns343VolumeName_Object=MibTableColumn
dns343VolumeName=_Dns343VolumeName_Object((1,3,6,1,4,1,171,50,1,4,1,1,9,1,2),_Dns343VolumeName_Type())
dns343VolumeName.setMaxAccess(_B)
if mibBuilder.loadTexts:dns343VolumeName.setStatus(_A)
_Dns343VolumeFsType_Type=DisplayString
_Dns343VolumeFsType_Object=MibTableColumn
dns343VolumeFsType=_Dns343VolumeFsType_Object((1,3,6,1,4,1,171,50,1,4,1,1,9,1,3),_Dns343VolumeFsType_Type())
dns343VolumeFsType.setMaxAccess(_B)
if mibBuilder.loadTexts:dns343VolumeFsType.setStatus(_A)
_Dns343VolumeRaidLevel_Type=DisplayString
_Dns343VolumeRaidLevel_Object=MibTableColumn
dns343VolumeRaidLevel=_Dns343VolumeRaidLevel_Object((1,3,6,1,4,1,171,50,1,4,1,1,9,1,4),_Dns343VolumeRaidLevel_Type())
dns343VolumeRaidLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:dns343VolumeRaidLevel.setStatus(_A)
_Dns343VolumeSize_Type=DisplayString
_Dns343VolumeSize_Object=MibTableColumn
dns343VolumeSize=_Dns343VolumeSize_Object((1,3,6,1,4,1,171,50,1,4,1,1,9,1,5),_Dns343VolumeSize_Type())
dns343VolumeSize.setMaxAccess(_B)
if mibBuilder.loadTexts:dns343VolumeSize.setStatus(_A)
_Dns343VolumeFreeSpace_Type=DisplayString
_Dns343VolumeFreeSpace_Object=MibTableColumn
dns343VolumeFreeSpace=_Dns343VolumeFreeSpace_Object((1,3,6,1,4,1,171,50,1,4,1,1,9,1,6),_Dns343VolumeFreeSpace_Type())
dns343VolumeFreeSpace.setMaxAccess(_B)
if mibBuilder.loadTexts:dns343VolumeFreeSpace.setStatus(_A)
_Dns343DiskTable_Object=MibTable
dns343DiskTable=_Dns343DiskTable_Object((1,3,6,1,4,1,171,50,1,4,1,1,10))
if mibBuilder.loadTexts:dns343DiskTable.setStatus(_A)
_Dns343DiskEntry_Object=MibTableRow
dns343DiskEntry=_Dns343DiskEntry_Object((1,3,6,1,4,1,171,50,1,4,1,1,10,1))
dns343DiskEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:dns343DiskEntry.setStatus(_A)
_Dns343DiskNum_Type=Integer32
_Dns343DiskNum_Object=MibTableColumn
dns343DiskNum=_Dns343DiskNum_Object((1,3,6,1,4,1,171,50,1,4,1,1,10,1,1),_Dns343DiskNum_Type())
dns343DiskNum.setMaxAccess(_B)
if mibBuilder.loadTexts:dns343DiskNum.setStatus(_A)
_Dns343DiskVendor_Type=DisplayString
_Dns343DiskVendor_Object=MibTableColumn
dns343DiskVendor=_Dns343DiskVendor_Object((1,3,6,1,4,1,171,50,1,4,1,1,10,1,2),_Dns343DiskVendor_Type())
dns343DiskVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:dns343DiskVendor.setStatus(_A)
_Dns343DiskModel_Type=DisplayString
_Dns343DiskModel_Object=MibTableColumn
dns343DiskModel=_Dns343DiskModel_Object((1,3,6,1,4,1,171,50,1,4,1,1,10,1,3),_Dns343DiskModel_Type())
dns343DiskModel.setMaxAccess(_B)
if mibBuilder.loadTexts:dns343DiskModel.setStatus(_A)
_Dns343DiskSerialNumber_Type=DisplayString
_Dns343DiskSerialNumber_Object=MibTableColumn
dns343DiskSerialNumber=_Dns343DiskSerialNumber_Object((1,3,6,1,4,1,171,50,1,4,1,1,10,1,4),_Dns343DiskSerialNumber_Type())
dns343DiskSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:dns343DiskSerialNumber.setStatus(_A)
_Dns343DiskTemperature_Type=DisplayString
_Dns343DiskTemperature_Object=MibTableColumn
dns343DiskTemperature=_Dns343DiskTemperature_Object((1,3,6,1,4,1,171,50,1,4,1,1,10,1,5),_Dns343DiskTemperature_Type())
dns343DiskTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:dns343DiskTemperature.setStatus(_A)
_Dns343DiskCapacity_Type=DisplayString
_Dns343DiskCapacity_Object=MibTableColumn
dns343DiskCapacity=_Dns343DiskCapacity_Object((1,3,6,1,4,1,171,50,1,4,1,1,10,1,6),_Dns343DiskCapacity_Type())
dns343DiskCapacity.setMaxAccess(_B)
if mibBuilder.loadTexts:dns343DiskCapacity.setStatus(_A)
_NotifyEvts_ObjectIdentity=ObjectIdentity
notifyEvts=_NotifyEvts_ObjectIdentity((1,3,6,1,4,1,171,50,1,4,1,1,200))
notifyPasswdChanged=NotificationType((1,3,6,1,4,1,171,50,1,4,1,1,200,1))
if mibBuilder.loadTexts:notifyPasswdChanged.setStatus(_A)
notifyFirmwareUpgraded=NotificationType((1,3,6,1,4,1,171,50,1,4,1,1,200,2))
if mibBuilder.loadTexts:notifyFirmwareUpgraded.setStatus(_A)
notifyNetworkChanged=NotificationType((1,3,6,1,4,1,171,50,1,4,1,1,200,3))
if mibBuilder.loadTexts:notifyNetworkChanged.setStatus(_A)
notifyTemperatureExceeded=NotificationType((1,3,6,1,4,1,171,50,1,4,1,1,200,4))
if mibBuilder.loadTexts:notifyTemperatureExceeded.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'d-link':d_link,'productID':productID,'projectID':projectID,'modelID':modelID,'submodelID':submodelID,'nasAgent':nasAgent,'dns343AgentVer':dns343AgentVer,'dns343SoftwareVersion':dns343SoftwareVersion,'dns343HostName':dns343HostName,'dns343DHCPServer':dns343DHCPServer,'dns343FTPServer':dns343FTPServer,'dns343NetType':dns343NetType,'dns343Temperature':dns343Temperature,'dns343FanStatus':dns343FanStatus,'dns343VolumeTable':dns343VolumeTable,'dns343VolumeEntry':dns343VolumeEntry,_D:dns343VolumeNum,'dns343VolumeName':dns343VolumeName,'dns343VolumeFsType':dns343VolumeFsType,'dns343VolumeRaidLevel':dns343VolumeRaidLevel,'dns343VolumeSize':dns343VolumeSize,'dns343VolumeFreeSpace':dns343VolumeFreeSpace,'dns343DiskTable':dns343DiskTable,'dns343DiskEntry':dns343DiskEntry,_E:dns343DiskNum,'dns343DiskVendor':dns343DiskVendor,'dns343DiskModel':dns343DiskModel,'dns343DiskSerialNumber':dns343DiskSerialNumber,'dns343DiskTemperature':dns343DiskTemperature,'dns343DiskCapacity':dns343DiskCapacity,'notifyEvts':notifyEvts,'notifyPasswdChanged':notifyPasswdChanged,'notifyFirmwareUpgraded':notifyFirmwareUpgraded,'notifyNetworkChanged':notifyNetworkChanged,'notifyTemperatureExceeded':notifyTemperatureExceeded})