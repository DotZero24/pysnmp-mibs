_S='voltIndex'
_R='tempIndex'
_Q='fanIndex'
_P='usbIndex'
_O='diskIndex'
_N='conIndex'
_M='bkupIndex'
_L='ioIndex'
_K='enterprises'
_J='eventText'
_I='eventID'
_H='deviceName'
_G='deviceDescr'
_F='DisplayString'
_E='Integer32'
_D='not-accessible'
_C='IOMEGANAS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32',_K,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
lenovoemc=ModuleIdentity((1,3,6,1,4,1,11369))
if mibBuilder.loadTexts:lenovoemc.setRevisions(('2007-03-01 10:11',))
_Org_ObjectIdentity=ObjectIdentity
org=_Org_ObjectIdentity((1,3))
_Dod_ObjectIdentity=ObjectIdentity
dod=_Dod_ObjectIdentity((1,3,6))
_Internet_ObjectIdentity=ObjectIdentity
internet=_Internet_ObjectIdentity((1,3,6,1))
_Private_ObjectIdentity=ObjectIdentity
private=_Private_ObjectIdentity((1,3,6,1,4))
_Enterprises_ObjectIdentity=ObjectIdentity
enterprises=_Enterprises_ObjectIdentity((1,3,6,1,4,1))
_IomegaNAS_ObjectIdentity=ObjectIdentity
iomegaNAS=_IomegaNAS_ObjectIdentity((1,3,6,1,4,1,11369,10))
_IomegaNASInfo_ObjectIdentity=ObjectIdentity
iomegaNASInfo=_IomegaNASInfo_ObjectIdentity((1,3,6,1,4,1,11369,10,1))
class _DeviceDescr_Type(DisplayString):defaultValue=OctetString('Iomega NAS BOX');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DeviceDescr_Type.__name__=_F
_DeviceDescr_Object=MibScalar
deviceDescr=_DeviceDescr_Object((1,3,6,1,4,1,11369,10,1,1),_DeviceDescr_Type())
deviceDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceDescr.setStatus(_A)
_DeviceName_Type=DisplayString
_DeviceName_Object=MibScalar
deviceName=_DeviceName_Object((1,3,6,1,4,1,11369,10,1,2),_DeviceName_Type())
deviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceName.setStatus(_A)
_NetConfig_ObjectIdentity=ObjectIdentity
netConfig=_NetConfig_ObjectIdentity((1,3,6,1,4,1,11369,10,1,3))
_Dns0_Type=IpAddress
_Dns0_Object=MibScalar
dns0=_Dns0_Object((1,3,6,1,4,1,11369,10,1,3,1),_Dns0_Type())
dns0.setMaxAccess(_B)
if mibBuilder.loadTexts:dns0.setStatus(_A)
_Dns1_Type=IpAddress
_Dns1_Object=MibScalar
dns1=_Dns1_Object((1,3,6,1,4,1,11369,10,1,3,2),_Dns1_Type())
dns1.setMaxAccess(_B)
if mibBuilder.loadTexts:dns1.setStatus(_A)
_Wins0_Type=IpAddress
_Wins0_Object=MibScalar
wins0=_Wins0_Object((1,3,6,1,4,1,11369,10,1,3,3),_Wins0_Type())
wins0.setMaxAccess(_B)
if mibBuilder.loadTexts:wins0.setStatus(_A)
_Wins1_Type=IpAddress
_Wins1_Object=MibScalar
wins1=_Wins1_Object((1,3,6,1,4,1,11369,10,1,3,4),_Wins1_Type())
wins1.setMaxAccess(_B)
if mibBuilder.loadTexts:wins1.setStatus(_A)
_SystemPerformance_ObjectIdentity=ObjectIdentity
systemPerformance=_SystemPerformance_ObjectIdentity((1,3,6,1,4,1,11369,10,2))
_IoTable_Object=MibTable
ioTable=_IoTable_Object((1,3,6,1,4,1,11369,10,2,1))
if mibBuilder.loadTexts:ioTable.setStatus(_A)
_IoEntry_Object=MibTableRow
ioEntry=_IoEntry_Object((1,3,6,1,4,1,11369,10,2,1,1))
ioEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:ioEntry.setStatus(_A)
_IoIndex_Type=Integer32
_IoIndex_Object=MibTableColumn
ioIndex=_IoIndex_Object((1,3,6,1,4,1,11369,10,2,1,1,1),_IoIndex_Type())
ioIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ioIndex.setStatus(_A)
_DiskName_Type=OctetString
_DiskName_Object=MibTableColumn
diskName=_DiskName_Object((1,3,6,1,4,1,11369,10,2,1,1,2),_DiskName_Type())
diskName.setMaxAccess(_B)
if mibBuilder.loadTexts:diskName.setStatus(_A)
_IoMgrs_Type=OctetString
_IoMgrs_Object=MibTableColumn
ioMgrs=_IoMgrs_Object((1,3,6,1,4,1,11369,10,2,1,1,3),_IoMgrs_Type())
ioMgrs.setMaxAccess(_B)
if mibBuilder.loadTexts:ioMgrs.setStatus(_A)
_IoMgws_Type=OctetString
_IoMgws_Object=MibTableColumn
ioMgws=_IoMgws_Object((1,3,6,1,4,1,11369,10,2,1,1,4),_IoMgws_Type())
ioMgws.setMaxAccess(_B)
if mibBuilder.loadTexts:ioMgws.setStatus(_A)
_IoReqrs_Type=OctetString
_IoReqrs_Object=MibTableColumn
ioReqrs=_IoReqrs_Object((1,3,6,1,4,1,11369,10,2,1,1,5),_IoReqrs_Type())
ioReqrs.setMaxAccess(_B)
if mibBuilder.loadTexts:ioReqrs.setStatus(_A)
_IoReqws_Type=OctetString
_IoReqws_Object=MibTableColumn
ioReqws=_IoReqws_Object((1,3,6,1,4,1,11369,10,2,1,1,6),_IoReqws_Type())
ioReqws.setMaxAccess(_B)
if mibBuilder.loadTexts:ioReqws.setStatus(_A)
_IoKbrs_Type=OctetString
_IoKbrs_Object=MibTableColumn
ioKbrs=_IoKbrs_Object((1,3,6,1,4,1,11369,10,2,1,1,7),_IoKbrs_Type())
ioKbrs.setMaxAccess(_B)
if mibBuilder.loadTexts:ioKbrs.setStatus(_A)
_IoKbws_Type=OctetString
_IoKbws_Object=MibTableColumn
ioKbws=_IoKbws_Object((1,3,6,1,4,1,11369,10,2,1,1,8),_IoKbws_Type())
ioKbws.setMaxAccess(_B)
if mibBuilder.loadTexts:ioKbws.setStatus(_A)
_IoAvgQueue_Type=OctetString
_IoAvgQueue_Object=MibTableColumn
ioAvgQueue=_IoAvgQueue_Object((1,3,6,1,4,1,11369,10,2,1,1,9),_IoAvgQueue_Type())
ioAvgQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:ioAvgQueue.setStatus(_A)
_IoAvgWait_Type=OctetString
_IoAvgWait_Object=MibTableColumn
ioAvgWait=_IoAvgWait_Object((1,3,6,1,4,1,11369,10,2,1,1,10),_IoAvgWait_Type())
ioAvgWait.setMaxAccess(_B)
if mibBuilder.loadTexts:ioAvgWait.setStatus(_A)
_IoAvgSvc_Type=OctetString
_IoAvgSvc_Object=MibTableColumn
ioAvgSvc=_IoAvgSvc_Object((1,3,6,1,4,1,11369,10,2,1,1,11),_IoAvgSvc_Type())
ioAvgSvc.setMaxAccess(_B)
if mibBuilder.loadTexts:ioAvgSvc.setStatus(_A)
_IoAvgUtil_Type=OctetString
_IoAvgUtil_Object=MibTableColumn
ioAvgUtil=_IoAvgUtil_Object((1,3,6,1,4,1,11369,10,2,1,1,12),_IoAvgUtil_Type())
ioAvgUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:ioAvgUtil.setStatus(_A)
_IoCpuTime_Type=OctetString
_IoCpuTime_Object=MibTableColumn
ioCpuTime=_IoCpuTime_Object((1,3,6,1,4,1,11369,10,2,1,1,13),_IoCpuTime_Type())
ioCpuTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ioCpuTime.setStatus(_A)
_IomegaNASFunctionStatus_ObjectIdentity=ObjectIdentity
iomegaNASFunctionStatus=_IomegaNASFunctionStatus_ObjectIdentity((1,3,6,1,4,1,11369,10,3))
_BkupTable_Object=MibTable
bkupTable=_BkupTable_Object((1,3,6,1,4,1,11369,10,3,1))
if mibBuilder.loadTexts:bkupTable.setStatus(_A)
_BkupEntry_Object=MibTableRow
bkupEntry=_BkupEntry_Object((1,3,6,1,4,1,11369,10,3,1,1))
bkupEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:bkupEntry.setStatus(_A)
_BkupIndex_Type=Integer32
_BkupIndex_Object=MibTableColumn
bkupIndex=_BkupIndex_Object((1,3,6,1,4,1,11369,10,3,1,1,1),_BkupIndex_Type())
bkupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:bkupIndex.setStatus(_A)
_BkupClient_Type=OctetString
_BkupClient_Object=MibTableColumn
bkupClient=_BkupClient_Object((1,3,6,1,4,1,11369,10,3,1,1,2),_BkupClient_Type())
bkupClient.setMaxAccess(_B)
if mibBuilder.loadTexts:bkupClient.setStatus(_A)
_BkupltStatus_Type=OctetString
_BkupltStatus_Object=MibTableColumn
bkupltStatus=_BkupltStatus_Object((1,3,6,1,4,1,11369,10,3,1,1,3),_BkupltStatus_Type())
bkupltStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:bkupltStatus.setStatus(_A)
_BkupTotalSpace_Type=OctetString
_BkupTotalSpace_Object=MibTableColumn
bkupTotalSpace=_BkupTotalSpace_Object((1,3,6,1,4,1,11369,10,3,1,1,4),_BkupTotalSpace_Type())
bkupTotalSpace.setMaxAccess(_B)
if mibBuilder.loadTexts:bkupTotalSpace.setStatus(_A)
_RemoteAccess_ObjectIdentity=ObjectIdentity
remoteAccess=_RemoteAccess_ObjectIdentity((1,3,6,1,4,1,11369,10,3,2))
_RaEnabled_Type=Integer32
_RaEnabled_Object=MibScalar
raEnabled=_RaEnabled_Object((1,3,6,1,4,1,11369,10,3,2,1),_RaEnabled_Type())
raEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:raEnabled.setStatus(_A)
_ConTable_Object=MibTable
conTable=_ConTable_Object((1,3,6,1,4,1,11369,10,3,3))
if mibBuilder.loadTexts:conTable.setStatus(_A)
_ConEntry_Object=MibTableRow
conEntry=_ConEntry_Object((1,3,6,1,4,1,11369,10,3,3,1))
conEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:conEntry.setStatus(_A)
class _ConIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_ConIndex_Type.__name__=_E
_ConIndex_Object=MibTableColumn
conIndex=_ConIndex_Object((1,3,6,1,4,1,11369,10,3,3,1,1),_ConIndex_Type())
conIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:conIndex.setStatus(_A)
class _ConCount_Type(Integer32):defaultValue=0
_ConCount_Type.__name__=_E
_ConCount_Object=MibTableColumn
conCount=_ConCount_Object((1,3,6,1,4,1,11369,10,3,3,1,2),_ConCount_Type())
conCount.setMaxAccess(_B)
if mibBuilder.loadTexts:conCount.setStatus(_A)
_ConProtocol_Type=DisplayString
_ConProtocol_Object=MibTableColumn
conProtocol=_ConProtocol_Object((1,3,6,1,4,1,11369,10,3,3,1,3),_ConProtocol_Type())
conProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:conProtocol.setStatus(_A)
_MediaService_ObjectIdentity=ObjectIdentity
mediaService=_MediaService_ObjectIdentity((1,3,6,1,4,1,11369,10,3,4))
_MediaServiceEnabled_Type=Integer32
_MediaServiceEnabled_Object=MibScalar
mediaServiceEnabled=_MediaServiceEnabled_Object((1,3,6,1,4,1,11369,10,3,4,1),_MediaServiceEnabled_Type())
mediaServiceEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:mediaServiceEnabled.setStatus(_A)
_IomegaNASStorage_ObjectIdentity=ObjectIdentity
iomegaNASStorage=_IomegaNASStorage_ObjectIdentity((1,3,6,1,4,1,11369,10,4))
_RaidStatus_Type=OctetString
_RaidStatus_Object=MibScalar
raidStatus=_RaidStatus_Object((1,3,6,1,4,1,11369,10,4,1),_RaidStatus_Type())
raidStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:raidStatus.setStatus(_A)
class _RaidLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_RaidLevel_Type.__name__=_E
_RaidLevel_Object=MibScalar
raidLevel=_RaidLevel_Object((1,3,6,1,4,1,11369,10,4,2),_RaidLevel_Type())
raidLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:raidLevel.setStatus(_A)
_DiskTable_Object=MibTable
diskTable=_DiskTable_Object((1,3,6,1,4,1,11369,10,4,3))
if mibBuilder.loadTexts:diskTable.setStatus(_A)
_DiskEntry_Object=MibTableRow
diskEntry=_DiskEntry_Object((1,3,6,1,4,1,11369,10,4,3,1))
diskEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:diskEntry.setStatus(_A)
class _DiskIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_DiskIndex_Type.__name__=_E
_DiskIndex_Object=MibTableColumn
diskIndex=_DiskIndex_Object((1,3,6,1,4,1,11369,10,4,3,1,1),_DiskIndex_Type())
diskIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:diskIndex.setStatus(_A)
_DiskID_Type=OctetString
_DiskID_Object=MibTableColumn
diskID=_DiskID_Object((1,3,6,1,4,1,11369,10,4,3,1,2),_DiskID_Type())
diskID.setMaxAccess(_B)
if mibBuilder.loadTexts:diskID.setStatus(_A)
_DiskSize_Type=OctetString
_DiskSize_Object=MibTableColumn
diskSize=_DiskSize_Object((1,3,6,1,4,1,11369,10,4,3,1,3),_DiskSize_Type())
diskSize.setMaxAccess(_B)
if mibBuilder.loadTexts:diskSize.setStatus(_A)
_DiskStatus_Type=OctetString
_DiskStatus_Object=MibTableColumn
diskStatus=_DiskStatus_Object((1,3,6,1,4,1,11369,10,4,3,1,4),_DiskStatus_Type())
diskStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:diskStatus.setStatus(_A)
_IomegaNASDevice_ObjectIdentity=ObjectIdentity
iomegaNASDevice=_IomegaNASDevice_ObjectIdentity((1,3,6,1,4,1,11369,10,5))
_UsbTable_Object=MibTable
usbTable=_UsbTable_Object((1,3,6,1,4,1,11369,10,5,1))
if mibBuilder.loadTexts:usbTable.setStatus(_A)
_UsbEntry_Object=MibTableRow
usbEntry=_UsbEntry_Object((1,3,6,1,4,1,11369,10,5,1,1))
usbEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:usbEntry.setStatus(_A)
_UsbIndex_Type=Integer32
_UsbIndex_Object=MibTableColumn
usbIndex=_UsbIndex_Object((1,3,6,1,4,1,11369,10,5,1,1,1),_UsbIndex_Type())
usbIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:usbIndex.setStatus(_A)
class _UsbManufacture_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UsbManufacture_Type.__name__=_F
_UsbManufacture_Object=MibTableColumn
usbManufacture=_UsbManufacture_Object((1,3,6,1,4,1,11369,10,5,1,1,2),_UsbManufacture_Type())
usbManufacture.setMaxAccess(_B)
if mibBuilder.loadTexts:usbManufacture.setStatus(_A)
class _UsbModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_UsbModel_Type.__name__=_F
_UsbModel_Object=MibTableColumn
usbModel=_UsbModel_Object((1,3,6,1,4,1,11369,10,5,1,1,3),_UsbModel_Type())
usbModel.setMaxAccess(_B)
if mibBuilder.loadTexts:usbModel.setStatus(_A)
_UsbType_Type=Integer32
_UsbType_Object=MibTableColumn
usbType=_UsbType_Object((1,3,6,1,4,1,11369,10,5,1,1,4),_UsbType_Type())
usbType.setMaxAccess(_B)
if mibBuilder.loadTexts:usbType.setStatus(_A)
_IomegaNASSensor_ObjectIdentity=ObjectIdentity
iomegaNASSensor=_IomegaNASSensor_ObjectIdentity((1,3,6,1,4,1,11369,10,6))
_FanTable_Object=MibTable
fanTable=_FanTable_Object((1,3,6,1,4,1,11369,10,6,1))
if mibBuilder.loadTexts:fanTable.setStatus(_A)
_FanEntry_Object=MibTableRow
fanEntry=_FanEntry_Object((1,3,6,1,4,1,11369,10,6,1,1))
fanEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:fanEntry.setStatus(_A)
_FanIndex_Type=Integer32
_FanIndex_Object=MibTableColumn
fanIndex=_FanIndex_Object((1,3,6,1,4,1,11369,10,6,1,1,1),_FanIndex_Type())
fanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fanIndex.setStatus(_A)
_FanName_Type=DisplayString
_FanName_Object=MibTableColumn
fanName=_FanName_Object((1,3,6,1,4,1,11369,10,6,1,1,2),_FanName_Type())
fanName.setMaxAccess(_B)
if mibBuilder.loadTexts:fanName.setStatus(_A)
_FanValue_Type=Gauge32
_FanValue_Object=MibTableColumn
fanValue=_FanValue_Object((1,3,6,1,4,1,11369,10,6,1,1,3),_FanValue_Type())
fanValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fanValue.setStatus(_A)
_TempTable_Object=MibTable
tempTable=_TempTable_Object((1,3,6,1,4,1,11369,10,6,2))
if mibBuilder.loadTexts:tempTable.setStatus(_A)
_TempEntry_Object=MibTableRow
tempEntry=_TempEntry_Object((1,3,6,1,4,1,11369,10,6,2,1))
tempEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:tempEntry.setStatus(_A)
_TempIndex_Type=Integer32
_TempIndex_Object=MibTableColumn
tempIndex=_TempIndex_Object((1,3,6,1,4,1,11369,10,6,2,1,1),_TempIndex_Type())
tempIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tempIndex.setStatus(_A)
_TempName_Type=DisplayString
_TempName_Object=MibTableColumn
tempName=_TempName_Object((1,3,6,1,4,1,11369,10,6,2,1,2),_TempName_Type())
tempName.setMaxAccess(_B)
if mibBuilder.loadTexts:tempName.setStatus(_A)
_TempValue_Type=Gauge32
_TempValue_Object=MibTableColumn
tempValue=_TempValue_Object((1,3,6,1,4,1,11369,10,6,2,1,3),_TempValue_Type())
tempValue.setMaxAccess(_B)
if mibBuilder.loadTexts:tempValue.setStatus(_A)
_VoltTable_Object=MibTable
voltTable=_VoltTable_Object((1,3,6,1,4,1,11369,10,6,3))
if mibBuilder.loadTexts:voltTable.setStatus(_A)
_VoltEntry_Object=MibTableRow
voltEntry=_VoltEntry_Object((1,3,6,1,4,1,11369,10,6,3,1))
voltEntry.setIndexNames((0,_C,_S))
if mibBuilder.loadTexts:voltEntry.setStatus(_A)
_VoltIndex_Type=Integer32
_VoltIndex_Object=MibTableColumn
voltIndex=_VoltIndex_Object((1,3,6,1,4,1,11369,10,6,3,1,1),_VoltIndex_Type())
voltIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:voltIndex.setStatus(_A)
_VoltName_Type=DisplayString
_VoltName_Object=MibTableColumn
voltName=_VoltName_Object((1,3,6,1,4,1,11369,10,6,3,1,2),_VoltName_Type())
voltName.setMaxAccess(_B)
if mibBuilder.loadTexts:voltName.setStatus(_A)
_VoltValue_Type=Gauge32
_VoltValue_Object=MibTableColumn
voltValue=_VoltValue_Object((1,3,6,1,4,1,11369,10,6,3,1,3),_VoltValue_Type())
voltValue.setMaxAccess(_B)
if mibBuilder.loadTexts:voltValue.setStatus(_A)
_IomegaNASEvent_ObjectIdentity=ObjectIdentity
iomegaNASEvent=_IomegaNASEvent_ObjectIdentity((1,3,6,1,4,1,11369,10,7))
_EventID_Type=DisplayString
_EventID_Object=MibScalar
eventID=_EventID_Object((1,3,6,1,4,1,11369,10,7,1),_EventID_Type())
eventID.setMaxAccess(_B)
if mibBuilder.loadTexts:eventID.setStatus(_A)
_EventText_Type=DisplayString
_EventText_Object=MibScalar
eventText=_EventText_Object((1,3,6,1,4,1,11369,10,7,2),_EventText_Type())
eventText.setMaxAccess(_B)
if mibBuilder.loadTexts:eventText.setStatus(_A)
_IomegaNASNotifications_ObjectIdentity=ObjectIdentity
iomegaNASNotifications=_IomegaNASNotifications_ObjectIdentity((1,3,6,1,4,1,11369,10,8))
iomegaNASNotificationError=NotificationType((1,3,6,1,4,1,11369,10,8,1))
iomegaNASNotificationError.setObjects(*((_C,_G),(_C,_H),(_C,_I),(_C,_J)))
if mibBuilder.loadTexts:iomegaNASNotificationError.setStatus(_A)
iomegaNASNotificationWarn=NotificationType((1,3,6,1,4,1,11369,10,8,2))
iomegaNASNotificationWarn.setObjects(*((_C,_G),(_C,_H),(_C,_I),(_C,_J)))
if mibBuilder.loadTexts:iomegaNASNotificationWarn.setStatus(_A)
iomegaNASNotificationInfo=NotificationType((1,3,6,1,4,1,11369,10,8,3))
iomegaNASNotificationInfo.setObjects(*((_C,_G),(_C,_H),(_C,_I),(_C,_J)))
if mibBuilder.loadTexts:iomegaNASNotificationInfo.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'org':org,'dod':dod,'internet':internet,'private':private,_K:enterprises,'lenovoemc':lenovoemc,'iomegaNAS':iomegaNAS,'iomegaNASInfo':iomegaNASInfo,_G:deviceDescr,_H:deviceName,'netConfig':netConfig,'dns0':dns0,'dns1':dns1,'wins0':wins0,'wins1':wins1,'systemPerformance':systemPerformance,'ioTable':ioTable,'ioEntry':ioEntry,_L:ioIndex,'diskName':diskName,'ioMgrs':ioMgrs,'ioMgws':ioMgws,'ioReqrs':ioReqrs,'ioReqws':ioReqws,'ioKbrs':ioKbrs,'ioKbws':ioKbws,'ioAvgQueue':ioAvgQueue,'ioAvgWait':ioAvgWait,'ioAvgSvc':ioAvgSvc,'ioAvgUtil':ioAvgUtil,'ioCpuTime':ioCpuTime,'iomegaNASFunctionStatus':iomegaNASFunctionStatus,'bkupTable':bkupTable,'bkupEntry':bkupEntry,_M:bkupIndex,'bkupClient':bkupClient,'bkupltStatus':bkupltStatus,'bkupTotalSpace':bkupTotalSpace,'remoteAccess':remoteAccess,'raEnabled':raEnabled,'conTable':conTable,'conEntry':conEntry,_N:conIndex,'conCount':conCount,'conProtocol':conProtocol,'mediaService':mediaService,'mediaServiceEnabled':mediaServiceEnabled,'iomegaNASStorage':iomegaNASStorage,'raidStatus':raidStatus,'raidLevel':raidLevel,'diskTable':diskTable,'diskEntry':diskEntry,_O:diskIndex,'diskID':diskID,'diskSize':diskSize,'diskStatus':diskStatus,'iomegaNASDevice':iomegaNASDevice,'usbTable':usbTable,'usbEntry':usbEntry,_P:usbIndex,'usbManufacture':usbManufacture,'usbModel':usbModel,'usbType':usbType,'iomegaNASSensor':iomegaNASSensor,'fanTable':fanTable,'fanEntry':fanEntry,_Q:fanIndex,'fanName':fanName,'fanValue':fanValue,'tempTable':tempTable,'tempEntry':tempEntry,_R:tempIndex,'tempName':tempName,'tempValue':tempValue,'voltTable':voltTable,'voltEntry':voltEntry,_S:voltIndex,'voltName':voltName,'voltValue':voltValue,'iomegaNASEvent':iomegaNASEvent,_I:eventID,_J:eventText,'iomegaNASNotifications':iomegaNASNotifications,'iomegaNASNotificationError':iomegaNASNotificationError,'iomegaNASNotificationWarn':iomegaNASNotificationWarn,'iomegaNASNotificationInfo':iomegaNASNotificationInfo})