_P='gwDescr'
_O='tempProbeDescr'
_N='memDescr'
_M='cpuDescr'
_L='inProgress'
_K='success'
_J='failed'
_I='MX-DIGITAL-PRODUCTS-MIB'
_H='noOp'
_G='DisplayString'
_F='current'
_E='OctetString'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrix,=mibBuilder.importSymbols('MX-SMI','mediatrix')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
snmpTraps,=mibBuilder.importSymbols('SNMPv2-MIB','snmpTraps')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
AutonomousType,DisplayString,PhysAddress,RowStatus,TextualConvention,TestAndIncr,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType',_G,'PhysAddress','RowStatus','TextualConvention','TestAndIncr','TimeStamp','TruthValue')
mediatrixDigitalProducts=ModuleIdentity((1,3,6,1,4,1,4935,3))
if mibBuilder.loadTexts:mediatrixDigitalProducts.setRevisions(('1902-08-07 10:00',))
_Sysinfo_ObjectIdentity=ObjectIdentity
sysinfo=_Sysinfo_ObjectIdentity((1,3,6,1,4,1,4935,3,1))
class _SerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,12))
_SerialNumber_Type.__name__=_G
_SerialNumber_Object=MibScalar
serialNumber=_SerialNumber_Object((1,3,6,1,4,1,4935,3,1,1),_SerialNumber_Type())
serialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:serialNumber.setStatus(_F)
class _HwRelease_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_HwRelease_Type.__name__=_G
_HwRelease_Object=MibScalar
hwRelease=_HwRelease_Object((1,3,6,1,4,1,4935,3,1,3),_HwRelease_Type())
hwRelease.setMaxAccess(_B)
if mibBuilder.loadTexts:hwRelease.setStatus(_F)
class _HwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_HwVersion_Type.__name__=_G
_HwVersion_Object=MibScalar
hwVersion=_HwVersion_Object((1,3,6,1,4,1,4935,3,1,4),_HwVersion_Type())
hwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hwVersion.setStatus(_F)
class _SwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwVersion_Type.__name__=_G
_SwVersion_Object=MibScalar
swVersion=_SwVersion_Object((1,3,6,1,4,1,4935,3,1,5),_SwVersion_Type())
swVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:swVersion.setStatus(_F)
class _ProductName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ProductName_Type.__name__=_G
_ProductName_Object=MibScalar
productName=_ProductName_Object((1,3,6,1,4,1,4935,3,1,6),_ProductName_Type())
productName.setMaxAccess(_B)
if mibBuilder.loadTexts:productName.setStatus(_F)
_Admin_ObjectIdentity=ObjectIdentity
admin=_Admin_ObjectIdentity((1,3,6,1,4,1,4935,3,2))
class _DeviceReload_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),('reload',1)))
_DeviceReload_Type.__name__=_D
_DeviceReload_Object=MibScalar
deviceReload=_DeviceReload_Object((1,3,6,1,4,1,4935,3,2,1),_DeviceReload_Type())
deviceReload.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceReload.setStatus(_A)
class _SaveRunningConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),('saveConfiguration',1)))
_SaveRunningConfig_Type.__name__=_D
_SaveRunningConfig_Object=MibScalar
saveRunningConfig=_SaveRunningConfig_Object((1,3,6,1,4,1,4935,3,2,2),_SaveRunningConfig_Type())
saveRunningConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:saveRunningConfig.setStatus(_A)
_Config_ObjectIdentity=ObjectIdentity
config=_Config_ObjectIdentity((1,3,6,1,4,1,4935,3,3))
_StartupConfigUpload_ObjectIdentity=ObjectIdentity
startupConfigUpload=_StartupConfigUpload_ObjectIdentity((1,3,6,1,4,1,4935,3,3,1))
class _UploadExecute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),('uploadConfiguration',1)))
_UploadExecute_Type.__name__=_D
_UploadExecute_Object=MibScalar
uploadExecute=_UploadExecute_Object((1,3,6,1,4,1,4935,3,3,1,1),_UploadExecute_Type())
uploadExecute.setMaxAccess(_C)
if mibBuilder.loadTexts:uploadExecute.setStatus(_A)
class _UploadTftpServerAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_UploadTftpServerAddress_Type.__name__=_E
_UploadTftpServerAddress_Object=MibScalar
uploadTftpServerAddress=_UploadTftpServerAddress_Object((1,3,6,1,4,1,4935,3,3,1,2),_UploadTftpServerAddress_Type())
uploadTftpServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:uploadTftpServerAddress.setStatus(_A)
class _UploadTftpServerPort_Type(Integer32):defaultValue=69;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_UploadTftpServerPort_Type.__name__=_D
_UploadTftpServerPort_Object=MibScalar
uploadTftpServerPort=_UploadTftpServerPort_Object((1,3,6,1,4,1,4935,3,3,1,3),_UploadTftpServerPort_Type())
uploadTftpServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:uploadTftpServerPort.setStatus(_A)
class _UploadTftpServerPath_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_UploadTftpServerPath_Type.__name__=_E
_UploadTftpServerPath_Object=MibScalar
uploadTftpServerPath=_UploadTftpServerPath_Object((1,3,6,1,4,1,4935,3,3,1,4),_UploadTftpServerPath_Type())
uploadTftpServerPath.setMaxAccess(_C)
if mibBuilder.loadTexts:uploadTftpServerPath.setStatus(_A)
class _UploadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2)))
_UploadStatus_Type.__name__=_D
_UploadStatus_Object=MibScalar
uploadStatus=_UploadStatus_Object((1,3,6,1,4,1,4935,3,3,1,5),_UploadStatus_Type())
uploadStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:uploadStatus.setStatus(_A)
_StartupConfigDownload_ObjectIdentity=ObjectIdentity
startupConfigDownload=_StartupConfigDownload_ObjectIdentity((1,3,6,1,4,1,4935,3,3,2))
class _DownloadExecute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),('downloadConfiguration',1)))
_DownloadExecute_Type.__name__=_D
_DownloadExecute_Object=MibScalar
downloadExecute=_DownloadExecute_Object((1,3,6,1,4,1,4935,3,3,2,1),_DownloadExecute_Type())
downloadExecute.setMaxAccess(_C)
if mibBuilder.loadTexts:downloadExecute.setStatus(_A)
class _DownloadTftpServerAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_DownloadTftpServerAddress_Type.__name__=_E
_DownloadTftpServerAddress_Object=MibScalar
downloadTftpServerAddress=_DownloadTftpServerAddress_Object((1,3,6,1,4,1,4935,3,3,2,2),_DownloadTftpServerAddress_Type())
downloadTftpServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:downloadTftpServerAddress.setStatus(_A)
class _DownloadTftpServerPort_Type(Integer32):defaultValue=69;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DownloadTftpServerPort_Type.__name__=_D
_DownloadTftpServerPort_Object=MibScalar
downloadTftpServerPort=_DownloadTftpServerPort_Object((1,3,6,1,4,1,4935,3,3,2,3),_DownloadTftpServerPort_Type())
downloadTftpServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:downloadTftpServerPort.setStatus(_F)
class _DownloadTftpServerPath_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_DownloadTftpServerPath_Type.__name__=_E
_DownloadTftpServerPath_Object=MibScalar
downloadTftpServerPath=_DownloadTftpServerPath_Object((1,3,6,1,4,1,4935,3,3,2,4),_DownloadTftpServerPath_Type())
downloadTftpServerPath.setMaxAccess(_C)
if mibBuilder.loadTexts:downloadTftpServerPath.setStatus(_A)
class _DownloadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2)))
_DownloadStatus_Type.__name__=_D
_DownloadStatus_Object=MibScalar
downloadStatus=_DownloadStatus_Object((1,3,6,1,4,1,4935,3,3,2,5),_DownloadStatus_Type())
downloadStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:downloadStatus.setStatus(_A)
_Firmware_ObjectIdentity=ObjectIdentity
firmware=_Firmware_ObjectIdentity((1,3,6,1,4,1,4935,3,4))
class _FirmwareLoadExecute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_H,0),('loadFirmware',1)))
_FirmwareLoadExecute_Type.__name__=_D
_FirmwareLoadExecute_Object=MibScalar
firmwareLoadExecute=_FirmwareLoadExecute_Object((1,3,6,1,4,1,4935,3,4,1),_FirmwareLoadExecute_Type())
firmwareLoadExecute.setMaxAccess(_C)
if mibBuilder.loadTexts:firmwareLoadExecute.setStatus(_A)
class _FirmwareTftpServerAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_FirmwareTftpServerAddress_Type.__name__=_E
_FirmwareTftpServerAddress_Object=MibScalar
firmwareTftpServerAddress=_FirmwareTftpServerAddress_Object((1,3,6,1,4,1,4935,3,4,2),_FirmwareTftpServerAddress_Type())
firmwareTftpServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:firmwareTftpServerAddress.setStatus(_A)
class _FirmwareTftpServerPort_Type(Integer32):defaultValue=69;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FirmwareTftpServerPort_Type.__name__=_D
_FirmwareTftpServerPort_Object=MibScalar
firmwareTftpServerPort=_FirmwareTftpServerPort_Object((1,3,6,1,4,1,4935,3,4,3),_FirmwareTftpServerPort_Type())
firmwareTftpServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:firmwareTftpServerPort.setStatus(_F)
class _FirmwareTftpServerPath_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_FirmwareTftpServerPath_Type.__name__=_E
_FirmwareTftpServerPath_Object=MibScalar
firmwareTftpServerPath=_FirmwareTftpServerPath_Object((1,3,6,1,4,1,4935,3,4,4),_FirmwareTftpServerPath_Type())
firmwareTftpServerPath.setMaxAccess(_C)
if mibBuilder.loadTexts:firmwareTftpServerPath.setStatus(_A)
class _FirmwareLoadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),(_K,1),(_L,2)))
_FirmwareLoadStatus_Type.__name__=_D
_FirmwareLoadStatus_Object=MibScalar
firmwareLoadStatus=_FirmwareLoadStatus_Object((1,3,6,1,4,1,4935,3,4,5),_FirmwareLoadStatus_Type())
firmwareLoadStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:firmwareLoadStatus.setStatus(_A)
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,4935,3,5))
_Mediatrix1400_2400_ObjectIdentity=ObjectIdentity
mediatrix1400_2400=_Mediatrix1400_2400_ObjectIdentity((1,3,6,1,4,1,4935,3,5,2))
_Mediatrix1500_1600_2500_2600_ObjectIdentity=ObjectIdentity
mediatrix1500_1600_2500_2600=_Mediatrix1500_1600_2500_2600_ObjectIdentity((1,3,6,1,4,1,4935,3,5,3))
_Performance_ObjectIdentity=ObjectIdentity
performance=_Performance_ObjectIdentity((1,3,6,1,4,1,4935,3,70))
_Cpu_ObjectIdentity=ObjectIdentity
cpu=_Cpu_ObjectIdentity((1,3,6,1,4,1,4935,3,70,10))
_CpuNumber_Type=Integer32
_CpuNumber_Object=MibScalar
cpuNumber=_CpuNumber_Object((1,3,6,1,4,1,4935,3,70,10,1),_CpuNumber_Type())
cpuNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuNumber.setStatus(_A)
_CpuTable_Object=MibTable
cpuTable=_CpuTable_Object((1,3,6,1,4,1,4935,3,70,10,2))
if mibBuilder.loadTexts:cpuTable.setStatus(_A)
_CpuEntry_Object=MibTableRow
cpuEntry=_CpuEntry_Object((1,3,6,1,4,1,4935,3,70,10,2,1))
cpuEntry.setIndexNames((0,_I,_M))
if mibBuilder.loadTexts:cpuEntry.setStatus(_A)
_CpuDescr_Type=DisplayString
_CpuDescr_Object=MibTableColumn
cpuDescr=_CpuDescr_Object((1,3,6,1,4,1,4935,3,70,10,2,1,1),_CpuDescr_Type())
cpuDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuDescr.setStatus(_A)
_CpuWorkloadCurrent_Type=Gauge32
_CpuWorkloadCurrent_Object=MibTableColumn
cpuWorkloadCurrent=_CpuWorkloadCurrent_Object((1,3,6,1,4,1,4935,3,70,10,2,1,2),_CpuWorkloadCurrent_Type())
cpuWorkloadCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuWorkloadCurrent.setStatus(_A)
_CpuWorkload1MinuteAverage_Type=Gauge32
_CpuWorkload1MinuteAverage_Object=MibTableColumn
cpuWorkload1MinuteAverage=_CpuWorkload1MinuteAverage_Object((1,3,6,1,4,1,4935,3,70,10,2,1,3),_CpuWorkload1MinuteAverage_Type())
cpuWorkload1MinuteAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuWorkload1MinuteAverage.setStatus(_A)
_CpuWorkload5MinuteAverage_Type=Gauge32
_CpuWorkload5MinuteAverage_Object=MibTableColumn
cpuWorkload5MinuteAverage=_CpuWorkload5MinuteAverage_Object((1,3,6,1,4,1,4935,3,70,10,2,1,4),_CpuWorkload5MinuteAverage_Type())
cpuWorkload5MinuteAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuWorkload5MinuteAverage.setStatus(_A)
_Memory_ObjectIdentity=ObjectIdentity
memory=_Memory_ObjectIdentity((1,3,6,1,4,1,4935,3,70,20))
_MemoryPoolNumber_Type=Integer32
_MemoryPoolNumber_Object=MibScalar
memoryPoolNumber=_MemoryPoolNumber_Object((1,3,6,1,4,1,4935,3,70,20,1),_MemoryPoolNumber_Type())
memoryPoolNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryPoolNumber.setStatus(_A)
_MemoryPoolTable_Object=MibTable
memoryPoolTable=_MemoryPoolTable_Object((1,3,6,1,4,1,4935,3,70,20,2))
if mibBuilder.loadTexts:memoryPoolTable.setStatus(_A)
_MemoryPoolEntry_Object=MibTableRow
memoryPoolEntry=_MemoryPoolEntry_Object((1,3,6,1,4,1,4935,3,70,20,2,1))
memoryPoolEntry.setIndexNames((0,_I,_N))
if mibBuilder.loadTexts:memoryPoolEntry.setStatus(_A)
_MemDescr_Type=DisplayString
_MemDescr_Object=MibTableColumn
memDescr=_MemDescr_Object((1,3,6,1,4,1,4935,3,70,20,2,1,1),_MemDescr_Type())
memDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:memDescr.setStatus(_A)
_MemTotalBytes_Type=Integer32
_MemTotalBytes_Object=MibTableColumn
memTotalBytes=_MemTotalBytes_Object((1,3,6,1,4,1,4935,3,70,20,2,1,2),_MemTotalBytes_Type())
memTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:memTotalBytes.setStatus('optional')
_MemAllocatedBytes_Type=Integer32
_MemAllocatedBytes_Object=MibTableColumn
memAllocatedBytes=_MemAllocatedBytes_Object((1,3,6,1,4,1,4935,3,70,20,2,1,3),_MemAllocatedBytes_Type())
memAllocatedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:memAllocatedBytes.setStatus(_A)
_MemFreeBytes_Type=Integer32
_MemFreeBytes_Object=MibTableColumn
memFreeBytes=_MemFreeBytes_Object((1,3,6,1,4,1,4935,3,70,20,2,1,4),_MemFreeBytes_Type())
memFreeBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:memFreeBytes.setStatus(_A)
_MemLargestFreeBlock_Type=Integer32
_MemLargestFreeBlock_Object=MibTableColumn
memLargestFreeBlock=_MemLargestFreeBlock_Object((1,3,6,1,4,1,4935,3,70,20,2,1,5),_MemLargestFreeBlock_Type())
memLargestFreeBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:memLargestFreeBlock.setStatus(_A)
_MemAllocatedBlocks_Type=Integer32
_MemAllocatedBlocks_Object=MibTableColumn
memAllocatedBlocks=_MemAllocatedBlocks_Object((1,3,6,1,4,1,4935,3,70,20,2,1,6),_MemAllocatedBlocks_Type())
memAllocatedBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:memAllocatedBlocks.setStatus(_A)
_MemFreeBlocks_Type=Integer32
_MemFreeBlocks_Object=MibTableColumn
memFreeBlocks=_MemFreeBlocks_Object((1,3,6,1,4,1,4935,3,70,20,2,1,7),_MemFreeBlocks_Type())
memFreeBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:memFreeBlocks.setStatus(_A)
_Temperature_ObjectIdentity=ObjectIdentity
temperature=_Temperature_ObjectIdentity((1,3,6,1,4,1,4935,3,70,30))
_TempProbeNumber_Type=Integer32
_TempProbeNumber_Object=MibScalar
tempProbeNumber=_TempProbeNumber_Object((1,3,6,1,4,1,4935,3,70,30,1),_TempProbeNumber_Type())
tempProbeNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:tempProbeNumber.setStatus(_A)
_TempProbeTable_Object=MibTable
tempProbeTable=_TempProbeTable_Object((1,3,6,1,4,1,4935,3,70,30,2))
if mibBuilder.loadTexts:tempProbeTable.setStatus(_A)
_TempProbeEntry_Object=MibTableRow
tempProbeEntry=_TempProbeEntry_Object((1,3,6,1,4,1,4935,3,70,30,2,1))
tempProbeEntry.setIndexNames((0,_I,_O))
if mibBuilder.loadTexts:tempProbeEntry.setStatus(_A)
_TempProbeDescr_Type=DisplayString
_TempProbeDescr_Object=MibTableColumn
tempProbeDescr=_TempProbeDescr_Object((1,3,6,1,4,1,4935,3,70,30,2,1,1),_TempProbeDescr_Type())
tempProbeDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:tempProbeDescr.setStatus(_A)
_CurrentDegreesCelsius_Type=Gauge32
_CurrentDegreesCelsius_Object=MibTableColumn
currentDegreesCelsius=_CurrentDegreesCelsius_Object((1,3,6,1,4,1,4935,3,70,30,2,1,2),_CurrentDegreesCelsius_Type())
currentDegreesCelsius.setMaxAccess(_B)
if mibBuilder.loadTexts:currentDegreesCelsius.setStatus(_A)
_Gateway_ObjectIdentity=ObjectIdentity
gateway=_Gateway_ObjectIdentity((1,3,6,1,4,1,4935,3,70,40))
_GwNumber_Type=Integer32
_GwNumber_Object=MibScalar
gwNumber=_GwNumber_Object((1,3,6,1,4,1,4935,3,70,40,1),_GwNumber_Type())
gwNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:gwNumber.setStatus(_A)
_GwTable_Object=MibTable
gwTable=_GwTable_Object((1,3,6,1,4,1,4935,3,70,40,2))
if mibBuilder.loadTexts:gwTable.setStatus(_A)
_GwEntry_Object=MibTableRow
gwEntry=_GwEntry_Object((1,3,6,1,4,1,4935,3,70,40,2,1))
gwEntry.setIndexNames((0,_I,_P))
if mibBuilder.loadTexts:gwEntry.setStatus(_A)
_GwDescr_Type=DisplayString
_GwDescr_Object=MibTableColumn
gwDescr=_GwDescr_Object((1,3,6,1,4,1,4935,3,70,40,2,1,1),_GwDescr_Type())
gwDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:gwDescr.setStatus(_A)
_GwCurrentConnectedCalls_Type=Gauge32
_GwCurrentConnectedCalls_Object=MibTableColumn
gwCurrentConnectedCalls=_GwCurrentConnectedCalls_Object((1,3,6,1,4,1,4935,3,70,40,2,1,2),_GwCurrentConnectedCalls_Type())
gwCurrentConnectedCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:gwCurrentConnectedCalls.setStatus(_A)
_GwCurrentOngoingCalls_Type=Gauge32
_GwCurrentOngoingCalls_Object=MibTableColumn
gwCurrentOngoingCalls=_GwCurrentOngoingCalls_Object((1,3,6,1,4,1,4935,3,70,40,2,1,3),_GwCurrentOngoingCalls_Type())
gwCurrentOngoingCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:gwCurrentOngoingCalls.setStatus(_A)
_GwTotalAccumulatedCalls_Type=Counter32
_GwTotalAccumulatedCalls_Object=MibTableColumn
gwTotalAccumulatedCalls=_GwTotalAccumulatedCalls_Object((1,3,6,1,4,1,4935,3,70,40,2,1,4),_GwTotalAccumulatedCalls_Type())
gwTotalAccumulatedCalls.setMaxAccess(_B)
if mibBuilder.loadTexts:gwTotalAccumulatedCalls.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'mediatrixDigitalProducts':mediatrixDigitalProducts,'sysinfo':sysinfo,'serialNumber':serialNumber,'hwRelease':hwRelease,'hwVersion':hwVersion,'swVersion':swVersion,'productName':productName,'admin':admin,'deviceReload':deviceReload,'saveRunningConfig':saveRunningConfig,'config':config,'startupConfigUpload':startupConfigUpload,'uploadExecute':uploadExecute,'uploadTftpServerAddress':uploadTftpServerAddress,'uploadTftpServerPort':uploadTftpServerPort,'uploadTftpServerPath':uploadTftpServerPath,'uploadStatus':uploadStatus,'startupConfigDownload':startupConfigDownload,'downloadExecute':downloadExecute,'downloadTftpServerAddress':downloadTftpServerAddress,'downloadTftpServerPort':downloadTftpServerPort,'downloadTftpServerPath':downloadTftpServerPath,'downloadStatus':downloadStatus,'firmware':firmware,'firmwareLoadExecute':firmwareLoadExecute,'firmwareTftpServerAddress':firmwareTftpServerAddress,'firmwareTftpServerPort':firmwareTftpServerPort,'firmwareTftpServerPath':firmwareTftpServerPath,'firmwareLoadStatus':firmwareLoadStatus,'products':products,'mediatrix1400-2400':mediatrix1400_2400,'mediatrix1500-1600-2500-2600':mediatrix1500_1600_2500_2600,'performance':performance,'cpu':cpu,'cpuNumber':cpuNumber,'cpuTable':cpuTable,'cpuEntry':cpuEntry,_M:cpuDescr,'cpuWorkloadCurrent':cpuWorkloadCurrent,'cpuWorkload1MinuteAverage':cpuWorkload1MinuteAverage,'cpuWorkload5MinuteAverage':cpuWorkload5MinuteAverage,'memory':memory,'memoryPoolNumber':memoryPoolNumber,'memoryPoolTable':memoryPoolTable,'memoryPoolEntry':memoryPoolEntry,_N:memDescr,'memTotalBytes':memTotalBytes,'memAllocatedBytes':memAllocatedBytes,'memFreeBytes':memFreeBytes,'memLargestFreeBlock':memLargestFreeBlock,'memAllocatedBlocks':memAllocatedBlocks,'memFreeBlocks':memFreeBlocks,'temperature':temperature,'tempProbeNumber':tempProbeNumber,'tempProbeTable':tempProbeTable,'tempProbeEntry':tempProbeEntry,_O:tempProbeDescr,'currentDegreesCelsius':currentDegreesCelsius,'gateway':gateway,'gwNumber':gwNumber,'gwTable':gwTable,'gwEntry':gwEntry,_P:gwDescr,'gwCurrentConnectedCalls':gwCurrentConnectedCalls,'gwCurrentOngoingCalls':gwCurrentOngoingCalls,'gwTotalAccumulatedCalls':gwTotalAccumulatedCalls})