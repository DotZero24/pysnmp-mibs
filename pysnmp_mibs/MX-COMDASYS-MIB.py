_Q='tempProbeDescr'
_P='memDescr'
_O='cpuDescr'
_N='inProgress'
_M='success'
_L='failed'
_K='daemonDescr'
_J='reload'
_I='DisplayString'
_H='OctetString'
_G='noOp'
_F='current'
_E='MX-COMDASYS-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrix,=mibBuilder.importSymbols('MX-SMI','mediatrix')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
snmpTraps,=mibBuilder.importSymbols('SNMPv2-MIB','snmpTraps')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
AutonomousType,DisplayString,PhysAddress,RowStatus,TextualConvention,TestAndIncr,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType',_I,'PhysAddress','RowStatus','TextualConvention','TestAndIncr','TimeStamp','TruthValue')
comdasysGW=ModuleIdentity((1,3,6,1,4,1,4935,4))
if mibBuilder.loadTexts:comdasysGW.setRevisions(('1921-04-08 10:00',))
_Sysinfo_ObjectIdentity=ObjectIdentity
sysinfo=_Sysinfo_ObjectIdentity((1,3,6,1,4,1,4935,4,1))
class _SwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_SwVersion_Type.__name__=_I
_SwVersion_Object=MibScalar
swVersion=_SwVersion_Object((1,3,6,1,4,1,4935,4,1,1),_SwVersion_Type())
swVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:swVersion.setStatus(_F)
class _ProductName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ProductName_Type.__name__=_I
_ProductName_Object=MibScalar
productName=_ProductName_Object((1,3,6,1,4,1,4935,4,1,2),_ProductName_Type())
productName.setMaxAccess(_B)
if mibBuilder.loadTexts:productName.setStatus(_F)
_Admin_ObjectIdentity=ObjectIdentity
admin=_Admin_ObjectIdentity((1,3,6,1,4,1,4935,4,2))
class _DeviceRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_J,1)))
_DeviceRestart_Type.__name__=_C
_DeviceRestart_Object=MibScalar
deviceRestart=_DeviceRestart_Object((1,3,6,1,4,1,4935,4,2,1),_DeviceRestart_Type())
deviceRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:deviceRestart.setStatus(_A)
_DaemonNumber_Type=Integer32
_DaemonNumber_Object=MibScalar
daemonNumber=_DaemonNumber_Object((1,3,6,1,4,1,4935,4,2,2),_DaemonNumber_Type())
daemonNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:daemonNumber.setStatus(_A)
_DaemonTable_Object=MibTable
daemonTable=_DaemonTable_Object((1,3,6,1,4,1,4935,4,2,3))
if mibBuilder.loadTexts:daemonTable.setStatus(_A)
_DaemonEntry_Object=MibTableRow
daemonEntry=_DaemonEntry_Object((1,3,6,1,4,1,4935,4,2,3,1))
daemonEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:daemonEntry.setStatus(_A)
_DaemonDescr_Type=DisplayString
_DaemonDescr_Object=MibTableColumn
daemonDescr=_DaemonDescr_Object((1,3,6,1,4,1,4935,4,2,3,1,1),_DaemonDescr_Type())
daemonDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:daemonDescr.setStatus(_A)
_DaemonStatus_Type=Gauge32
_DaemonStatus_Object=MibTableColumn
daemonStatus=_DaemonStatus_Object((1,3,6,1,4,1,4935,4,2,3,1,2),_DaemonStatus_Type())
daemonStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:daemonStatus.setStatus(_A)
class _DaemonRestart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_J,1)))
_DaemonRestart_Type.__name__=_C
_DaemonRestart_Object=MibTableColumn
daemonRestart=_DaemonRestart_Object((1,3,6,1,4,1,4935,4,2,3,1,3),_DaemonRestart_Type())
daemonRestart.setMaxAccess(_D)
if mibBuilder.loadTexts:daemonRestart.setStatus(_A)
_Config_ObjectIdentity=ObjectIdentity
config=_Config_ObjectIdentity((1,3,6,1,4,1,4935,4,3))
class _DownloadExecute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),('downloadConfiguration',1)))
_DownloadExecute_Type.__name__=_C
_DownloadExecute_Object=MibScalar
downloadExecute=_DownloadExecute_Object((1,3,6,1,4,1,4935,4,3,1),_DownloadExecute_Type())
downloadExecute.setMaxAccess(_D)
if mibBuilder.loadTexts:downloadExecute.setStatus(_A)
class _DownloadFtpServerAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_DownloadFtpServerAddress_Type.__name__=_H
_DownloadFtpServerAddress_Object=MibScalar
downloadFtpServerAddress=_DownloadFtpServerAddress_Object((1,3,6,1,4,1,4935,4,3,2),_DownloadFtpServerAddress_Type())
downloadFtpServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:downloadFtpServerAddress.setStatus(_A)
class _DownloadFtpServerPort_Type(Integer32):defaultValue=21;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DownloadFtpServerPort_Type.__name__=_C
_DownloadFtpServerPort_Object=MibScalar
downloadFtpServerPort=_DownloadFtpServerPort_Object((1,3,6,1,4,1,4935,4,3,3),_DownloadFtpServerPort_Type())
downloadFtpServerPort.setMaxAccess(_D)
if mibBuilder.loadTexts:downloadFtpServerPort.setStatus(_F)
class _DownloadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_L,0),(_M,1),(_N,2)))
_DownloadStatus_Type.__name__=_C
_DownloadStatus_Object=MibScalar
downloadStatus=_DownloadStatus_Object((1,3,6,1,4,1,4935,4,3,4),_DownloadStatus_Type())
downloadStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:downloadStatus.setStatus(_A)
_Firmware_ObjectIdentity=ObjectIdentity
firmware=_Firmware_ObjectIdentity((1,3,6,1,4,1,4935,4,4))
class _FirmwareLoadExecute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),('loadFirmware',1)))
_FirmwareLoadExecute_Type.__name__=_C
_FirmwareLoadExecute_Object=MibScalar
firmwareLoadExecute=_FirmwareLoadExecute_Object((1,3,6,1,4,1,4935,4,4,1),_FirmwareLoadExecute_Type())
firmwareLoadExecute.setMaxAccess(_D)
if mibBuilder.loadTexts:firmwareLoadExecute.setStatus(_A)
class _FirmwareFtpServerAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_FirmwareFtpServerAddress_Type.__name__=_H
_FirmwareFtpServerAddress_Object=MibScalar
firmwareFtpServerAddress=_FirmwareFtpServerAddress_Object((1,3,6,1,4,1,4935,4,4,2),_FirmwareFtpServerAddress_Type())
firmwareFtpServerAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:firmwareFtpServerAddress.setStatus(_A)
class _FirmwareFtpServerPort_Type(Integer32):defaultValue=21;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FirmwareFtpServerPort_Type.__name__=_C
_FirmwareFtpServerPort_Object=MibScalar
firmwareFtpServerPort=_FirmwareFtpServerPort_Object((1,3,6,1,4,1,4935,4,4,3),_FirmwareFtpServerPort_Type())
firmwareFtpServerPort.setMaxAccess(_D)
if mibBuilder.loadTexts:firmwareFtpServerPort.setStatus(_F)
class _FirmwareLoadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_L,0),(_M,1),(_N,2)))
_FirmwareLoadStatus_Type.__name__=_C
_FirmwareLoadStatus_Object=MibScalar
firmwareLoadStatus=_FirmwareLoadStatus_Object((1,3,6,1,4,1,4935,4,4,4),_FirmwareLoadStatus_Type())
firmwareLoadStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:firmwareLoadStatus.setStatus(_A)
_Performance_ObjectIdentity=ObjectIdentity
performance=_Performance_ObjectIdentity((1,3,6,1,4,1,4935,4,70))
_Cpu_ObjectIdentity=ObjectIdentity
cpu=_Cpu_ObjectIdentity((1,3,6,1,4,1,4935,4,70,10))
_CpuNumber_Type=Integer32
_CpuNumber_Object=MibScalar
cpuNumber=_CpuNumber_Object((1,3,6,1,4,1,4935,4,70,10,1),_CpuNumber_Type())
cpuNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuNumber.setStatus(_A)
_CpuTable_Object=MibTable
cpuTable=_CpuTable_Object((1,3,6,1,4,1,4935,4,70,10,2))
if mibBuilder.loadTexts:cpuTable.setStatus(_A)
_CpuEntry_Object=MibTableRow
cpuEntry=_CpuEntry_Object((1,3,6,1,4,1,4935,4,70,10,2,1))
cpuEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:cpuEntry.setStatus(_A)
_CpuDescr_Type=DisplayString
_CpuDescr_Object=MibTableColumn
cpuDescr=_CpuDescr_Object((1,3,6,1,4,1,4935,4,70,10,2,1,1),_CpuDescr_Type())
cpuDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuDescr.setStatus(_A)
_CpuWorkloadCurrent_Type=Gauge32
_CpuWorkloadCurrent_Object=MibTableColumn
cpuWorkloadCurrent=_CpuWorkloadCurrent_Object((1,3,6,1,4,1,4935,4,70,10,2,1,2),_CpuWorkloadCurrent_Type())
cpuWorkloadCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuWorkloadCurrent.setStatus(_A)
_CpuWorkload1MinuteAverage_Type=Gauge32
_CpuWorkload1MinuteAverage_Object=MibTableColumn
cpuWorkload1MinuteAverage=_CpuWorkload1MinuteAverage_Object((1,3,6,1,4,1,4935,4,70,10,2,1,3),_CpuWorkload1MinuteAverage_Type())
cpuWorkload1MinuteAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuWorkload1MinuteAverage.setStatus(_A)
_CpuWorkload5MinuteAverage_Type=Gauge32
_CpuWorkload5MinuteAverage_Object=MibTableColumn
cpuWorkload5MinuteAverage=_CpuWorkload5MinuteAverage_Object((1,3,6,1,4,1,4935,4,70,10,2,1,4),_CpuWorkload5MinuteAverage_Type())
cpuWorkload5MinuteAverage.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuWorkload5MinuteAverage.setStatus(_A)
_Memory_ObjectIdentity=ObjectIdentity
memory=_Memory_ObjectIdentity((1,3,6,1,4,1,4935,4,70,20))
_MemoryPoolNumber_Type=Integer32
_MemoryPoolNumber_Object=MibScalar
memoryPoolNumber=_MemoryPoolNumber_Object((1,3,6,1,4,1,4935,4,70,20,1),_MemoryPoolNumber_Type())
memoryPoolNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:memoryPoolNumber.setStatus(_A)
_MemoryPoolTable_Object=MibTable
memoryPoolTable=_MemoryPoolTable_Object((1,3,6,1,4,1,4935,4,70,20,2))
if mibBuilder.loadTexts:memoryPoolTable.setStatus(_A)
_MemoryPoolEntry_Object=MibTableRow
memoryPoolEntry=_MemoryPoolEntry_Object((1,3,6,1,4,1,4935,4,70,20,2,1))
memoryPoolEntry.setIndexNames((0,_E,_P))
if mibBuilder.loadTexts:memoryPoolEntry.setStatus(_A)
_MemDescr_Type=DisplayString
_MemDescr_Object=MibTableColumn
memDescr=_MemDescr_Object((1,3,6,1,4,1,4935,4,70,20,2,1,1),_MemDescr_Type())
memDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:memDescr.setStatus(_A)
_MemTotalBytes_Type=Integer32
_MemTotalBytes_Object=MibTableColumn
memTotalBytes=_MemTotalBytes_Object((1,3,6,1,4,1,4935,4,70,20,2,1,2),_MemTotalBytes_Type())
memTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:memTotalBytes.setStatus('optional')
_MemAllocatedBytes_Type=Integer32
_MemAllocatedBytes_Object=MibTableColumn
memAllocatedBytes=_MemAllocatedBytes_Object((1,3,6,1,4,1,4935,4,70,20,2,1,3),_MemAllocatedBytes_Type())
memAllocatedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:memAllocatedBytes.setStatus(_A)
_MemFreeBytes_Type=Integer32
_MemFreeBytes_Object=MibTableColumn
memFreeBytes=_MemFreeBytes_Object((1,3,6,1,4,1,4935,4,70,20,2,1,4),_MemFreeBytes_Type())
memFreeBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:memFreeBytes.setStatus(_A)
_MemLargestFreeBlock_Type=Integer32
_MemLargestFreeBlock_Object=MibTableColumn
memLargestFreeBlock=_MemLargestFreeBlock_Object((1,3,6,1,4,1,4935,4,70,20,2,1,5),_MemLargestFreeBlock_Type())
memLargestFreeBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:memLargestFreeBlock.setStatus(_A)
_MemAllocatedBlocks_Type=Integer32
_MemAllocatedBlocks_Object=MibTableColumn
memAllocatedBlocks=_MemAllocatedBlocks_Object((1,3,6,1,4,1,4935,4,70,20,2,1,6),_MemAllocatedBlocks_Type())
memAllocatedBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:memAllocatedBlocks.setStatus(_A)
_MemFreeBlocks_Type=Integer32
_MemFreeBlocks_Object=MibTableColumn
memFreeBlocks=_MemFreeBlocks_Object((1,3,6,1,4,1,4935,4,70,20,2,1,7),_MemFreeBlocks_Type())
memFreeBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:memFreeBlocks.setStatus(_A)
_Temperature_ObjectIdentity=ObjectIdentity
temperature=_Temperature_ObjectIdentity((1,3,6,1,4,1,4935,4,70,30))
_TempProbeNumber_Type=Integer32
_TempProbeNumber_Object=MibScalar
tempProbeNumber=_TempProbeNumber_Object((1,3,6,1,4,1,4935,4,70,30,1),_TempProbeNumber_Type())
tempProbeNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:tempProbeNumber.setStatus(_A)
_TempProbeTable_Object=MibTable
tempProbeTable=_TempProbeTable_Object((1,3,6,1,4,1,4935,4,70,30,2))
if mibBuilder.loadTexts:tempProbeTable.setStatus(_A)
_TempProbeEntry_Object=MibTableRow
tempProbeEntry=_TempProbeEntry_Object((1,3,6,1,4,1,4935,4,70,30,2,1))
tempProbeEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:tempProbeEntry.setStatus(_A)
_TempProbeDescr_Type=DisplayString
_TempProbeDescr_Object=MibTableColumn
tempProbeDescr=_TempProbeDescr_Object((1,3,6,1,4,1,4935,4,70,30,2,1,1),_TempProbeDescr_Type())
tempProbeDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:tempProbeDescr.setStatus(_A)
_CurrentDegreesCelsius_Type=Gauge32
_CurrentDegreesCelsius_Object=MibTableColumn
currentDegreesCelsius=_CurrentDegreesCelsius_Object((1,3,6,1,4,1,4935,4,70,30,2,1,2),_CurrentDegreesCelsius_Type())
currentDegreesCelsius.setMaxAccess(_B)
if mibBuilder.loadTexts:currentDegreesCelsius.setStatus(_A)
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,4935,4,90))
_Convergence_33xx_Biab_ObjectIdentity=ObjectIdentity
convergence_33xx_Biab=_Convergence_33xx_Biab_ObjectIdentity((1,3,6,1,4,1,4935,4,90,100))
_Convergence_1600_ObjectIdentity=ObjectIdentity
convergence_1600=_Convergence_1600_ObjectIdentity((1,3,6,1,4,1,4935,4,90,200))
_Convergence_2600_ObjectIdentity=ObjectIdentity
convergence_2600=_Convergence_2600_ObjectIdentity((1,3,6,1,4,1,4935,4,90,300))
_Convergence_3600_ObjectIdentity=ObjectIdentity
convergence_3600=_Convergence_3600_ObjectIdentity((1,3,6,1,4,1,4935,4,90,400))
_Convergence_4600_ObjectIdentity=ObjectIdentity
convergence_4600=_Convergence_4600_ObjectIdentity((1,3,6,1,4,1,4935,4,90,500))
_Fmc_2800_ObjectIdentity=ObjectIdentity
fmc_2800=_Fmc_2800_ObjectIdentity((1,3,6,1,4,1,4935,4,90,600))
_Fmc_3800_ObjectIdentity=ObjectIdentity
fmc_3800=_Fmc_3800_ObjectIdentity((1,3,6,1,4,1,4935,4,90,700))
_Fmc_4800_ObjectIdentity=ObjectIdentity
fmc_4800=_Fmc_4800_ObjectIdentity((1,3,6,1,4,1,4935,4,90,800))
mibBuilder.exportSymbols(_E,**{'comdasysGW':comdasysGW,'sysinfo':sysinfo,'swVersion':swVersion,'productName':productName,'admin':admin,'deviceRestart':deviceRestart,'daemonNumber':daemonNumber,'daemonTable':daemonTable,'daemonEntry':daemonEntry,_K:daemonDescr,'daemonStatus':daemonStatus,'daemonRestart':daemonRestart,'config':config,'downloadExecute':downloadExecute,'downloadFtpServerAddress':downloadFtpServerAddress,'downloadFtpServerPort':downloadFtpServerPort,'downloadStatus':downloadStatus,'firmware':firmware,'firmwareLoadExecute':firmwareLoadExecute,'firmwareFtpServerAddress':firmwareFtpServerAddress,'firmwareFtpServerPort':firmwareFtpServerPort,'firmwareLoadStatus':firmwareLoadStatus,'performance':performance,'cpu':cpu,'cpuNumber':cpuNumber,'cpuTable':cpuTable,'cpuEntry':cpuEntry,_O:cpuDescr,'cpuWorkloadCurrent':cpuWorkloadCurrent,'cpuWorkload1MinuteAverage':cpuWorkload1MinuteAverage,'cpuWorkload5MinuteAverage':cpuWorkload5MinuteAverage,'memory':memory,'memoryPoolNumber':memoryPoolNumber,'memoryPoolTable':memoryPoolTable,'memoryPoolEntry':memoryPoolEntry,_P:memDescr,'memTotalBytes':memTotalBytes,'memAllocatedBytes':memAllocatedBytes,'memFreeBytes':memFreeBytes,'memLargestFreeBlock':memLargestFreeBlock,'memAllocatedBlocks':memAllocatedBlocks,'memFreeBlocks':memFreeBlocks,'temperature':temperature,'tempProbeNumber':tempProbeNumber,'tempProbeTable':tempProbeTable,'tempProbeEntry':tempProbeEntry,_Q:tempProbeDescr,'currentDegreesCelsius':currentDegreesCelsius,'products':products,'convergence-33xx-Biab':convergence_33xx_Biab,'convergence-1600':convergence_1600,'convergence-2600':convergence_2600,'convergence-3600':convergence_3600,'convergence-4600':convergence_4600,'fmc-2800':fmc_2800,'fmc-3800':fmc_3800,'fmc-4800':fmc_4800})