_q='cbAcceleratorHostIPAddress'
_p='cbAcceleratorHostIPAddressType'
_o='cbAcceleratorIpAddress'
_n='cbAcceleratorIpAddressType'
_m='cbHostIPAddress'
_l='cbHostIPAddressType'
_k='cbIpAddress'
_j='cbIpAddressType'
_i='nsHostIPAddress'
_h='nsHostIPAddressType'
_g='nsIpAddress'
_f='nsIpAddressType'
_e='xenIpAddress'
_d='xenIpAddressType'
_c='hmHostIPAddress'
_b='hmHostIPAddressType'
_a='hmName'
_Z='interfaceHostIPAddress'
_Y='interfaceHostIPAddressType'
_X='interfaceMappedPort'
_W='srHostIPAddress'
_V='srHostIPAddressType'
_U='srBayNumber'
_T='srName'
_S='diskHostIPAddress'
_R='diskHostIPAddressType'
_Q='diskName'
_P='softwareResourceHostIPAddress'
_O='softwareResourceHostIPAddressType'
_N='softwareResourceName'
_M='hardwareResourceHostIPAddress'
_L='hardwareResourceHostIPAddressType'
_K='hardwareResourceName'
_J='accessible-for-notify'
_I='thresholdValue'
_H='currentValue'
_G='entityName'
_F='severity'
_E='eventMessage'
_D='source'
_C='read-only'
_B='current'
_A='SDX-ROOT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
netScaler=ModuleIdentity((1,3,6,1,4,1,5951))
_SdxRoot_ObjectIdentity=ObjectIdentity
sdxRoot=_SdxRoot_ObjectIdentity((1,3,6,1,4,1,5951,6))
_SdxEventGroup_ObjectIdentity=ObjectIdentity
sdxEventGroup=_SdxEventGroup_ObjectIdentity((1,3,6,1,4,1,5951,6,1))
_EventVarBindOids_ObjectIdentity=ObjectIdentity
eventVarBindOids=_EventVarBindOids_ObjectIdentity((1,3,6,1,4,1,5951,6,1,1))
_Source_Type=OctetString
_Source_Object=MibScalar
source=_Source_Object((1,3,6,1,4,1,5951,6,1,1,1),_Source_Type())
source.setMaxAccess(_J)
if mibBuilder.loadTexts:source.setStatus(_B)
_EntityName_Type=OctetString
_EntityName_Object=MibScalar
entityName=_EntityName_Object((1,3,6,1,4,1,5951,6,1,1,2),_EntityName_Type())
entityName.setMaxAccess(_J)
if mibBuilder.loadTexts:entityName.setStatus(_B)
_EntityType_Type=OctetString
_EntityType_Object=MibScalar
entityType=_EntityType_Object((1,3,6,1,4,1,5951,6,1,1,3),_EntityType_Type())
entityType.setMaxAccess(_J)
if mibBuilder.loadTexts:entityType.setStatus(_B)
_EventMessage_Type=OctetString
_EventMessage_Object=MibScalar
eventMessage=_EventMessage_Object((1,3,6,1,4,1,5951,6,1,1,4),_EventMessage_Type())
eventMessage.setMaxAccess(_J)
if mibBuilder.loadTexts:eventMessage.setStatus(_B)
_ThresholdValue_Type=OctetString
_ThresholdValue_Object=MibScalar
thresholdValue=_ThresholdValue_Object((1,3,6,1,4,1,5951,6,1,1,5),_ThresholdValue_Type())
thresholdValue.setMaxAccess(_J)
if mibBuilder.loadTexts:thresholdValue.setStatus(_B)
_CurrentValue_Type=OctetString
_CurrentValue_Object=MibScalar
currentValue=_CurrentValue_Object((1,3,6,1,4,1,5951,6,1,1,6),_CurrentValue_Type())
currentValue.setMaxAccess(_J)
if mibBuilder.loadTexts:currentValue.setStatus(_B)
_Severity_Type=OctetString
_Severity_Object=MibScalar
severity=_Severity_Object((1,3,6,1,4,1,5951,6,1,1,7),_Severity_Type())
severity.setMaxAccess(_J)
if mibBuilder.loadTexts:severity.setStatus(_B)
_MpsEvents_ObjectIdentity=ObjectIdentity
mpsEvents=_MpsEvents_ObjectIdentity((1,3,6,1,4,1,5951,6,1,2))
_SystemGroup_ObjectIdentity=ObjectIdentity
systemGroup=_SystemGroup_ObjectIdentity((1,3,6,1,4,1,5951,6,2))
_SystemPlatform_Type=OctetString
_SystemPlatform_Object=MibScalar
systemPlatform=_SystemPlatform_Object((1,3,6,1,4,1,5951,6,2,1),_SystemPlatform_Type())
systemPlatform.setMaxAccess(_C)
if mibBuilder.loadTexts:systemPlatform.setStatus(_B)
_SystemProduct_Type=OctetString
_SystemProduct_Object=MibScalar
systemProduct=_SystemProduct_Object((1,3,6,1,4,1,5951,6,2,2),_SystemProduct_Type())
systemProduct.setMaxAccess(_C)
if mibBuilder.loadTexts:systemProduct.setStatus(_B)
_SystemBuildNumber_Type=OctetString
_SystemBuildNumber_Object=MibScalar
systemBuildNumber=_SystemBuildNumber_Object((1,3,6,1,4,1,5951,6,2,3),_SystemBuildNumber_Type())
systemBuildNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:systemBuildNumber.setStatus(_B)
_SystemSvmIPAddressType_Type=InetAddressType
_SystemSvmIPAddressType_Object=MibScalar
systemSvmIPAddressType=_SystemSvmIPAddressType_Object((1,3,6,1,4,1,5951,6,2,4),_SystemSvmIPAddressType_Type())
systemSvmIPAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:systemSvmIPAddressType.setStatus(_B)
_SystemSvmIPAddress_Type=InetAddress
_SystemSvmIPAddress_Object=MibScalar
systemSvmIPAddress=_SystemSvmIPAddress_Object((1,3,6,1,4,1,5951,6,2,5),_SystemSvmIPAddress_Type())
systemSvmIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:systemSvmIPAddress.setStatus(_B)
_SystemXenIPAddressType_Type=InetAddressType
_SystemXenIPAddressType_Object=MibScalar
systemXenIPAddressType=_SystemXenIPAddressType_Object((1,3,6,1,4,1,5951,6,2,6),_SystemXenIPAddressType_Type())
systemXenIPAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:systemXenIPAddressType.setStatus(_B)
_SystemXenIPAddress_Type=InetAddress
_SystemXenIPAddress_Object=MibScalar
systemXenIPAddress=_SystemXenIPAddress_Object((1,3,6,1,4,1,5951,6,2,7),_SystemXenIPAddress_Type())
systemXenIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:systemXenIPAddress.setStatus(_B)
_SystemNetmaskType_Type=InetAddressType
_SystemNetmaskType_Object=MibScalar
systemNetmaskType=_SystemNetmaskType_Object((1,3,6,1,4,1,5951,6,2,8),_SystemNetmaskType_Type())
systemNetmaskType.setMaxAccess(_C)
if mibBuilder.loadTexts:systemNetmaskType.setStatus(_B)
_SystemNetmask_Type=InetAddress
_SystemNetmask_Object=MibScalar
systemNetmask=_SystemNetmask_Object((1,3,6,1,4,1,5951,6,2,9),_SystemNetmask_Type())
systemNetmask.setMaxAccess(_C)
if mibBuilder.loadTexts:systemNetmask.setStatus(_B)
_SystemGatewayType_Type=InetAddressType
_SystemGatewayType_Object=MibScalar
systemGatewayType=_SystemGatewayType_Object((1,3,6,1,4,1,5951,6,2,10),_SystemGatewayType_Type())
systemGatewayType.setMaxAccess(_C)
if mibBuilder.loadTexts:systemGatewayType.setStatus(_B)
_SystemGateway_Type=InetAddress
_SystemGateway_Object=MibScalar
systemGateway=_SystemGateway_Object((1,3,6,1,4,1,5951,6,2,11),_SystemGateway_Type())
systemGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:systemGateway.setStatus(_B)
_SystemNetworkInterface_Type=OctetString
_SystemNetworkInterface_Object=MibScalar
systemNetworkInterface=_SystemNetworkInterface_Object((1,3,6,1,4,1,5951,6,2,12),_SystemNetworkInterface_Type())
systemNetworkInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:systemNetworkInterface.setStatus(_B)
_SystemDns_Type=OctetString
_SystemDns_Object=MibScalar
systemDns=_SystemDns_Object((1,3,6,1,4,1,5951,6,2,13),_SystemDns_Type())
systemDns.setMaxAccess(_C)
if mibBuilder.loadTexts:systemDns.setStatus(_B)
_SystemSysId_Type=OctetString
_SystemSysId_Object=MibScalar
systemSysId=_SystemSysId_Object((1,3,6,1,4,1,5951,6,2,15),_SystemSysId_Type())
systemSysId.setMaxAccess(_C)
if mibBuilder.loadTexts:systemSysId.setStatus(_B)
_SystemSerial_Type=OctetString
_SystemSerial_Object=MibScalar
systemSerial=_SystemSerial_Object((1,3,6,1,4,1,5951,6,2,16),_SystemSerial_Type())
systemSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:systemSerial.setStatus(_B)
_SystemCurrentTime_Type=Integer32
_SystemCurrentTime_Object=MibScalar
systemCurrentTime=_SystemCurrentTime_Object((1,3,6,1,4,1,5951,6,2,17),_SystemCurrentTime_Type())
systemCurrentTime.setMaxAccess(_C)
if mibBuilder.loadTexts:systemCurrentTime.setStatus(_B)
_SystemUptime_Type=OctetString
_SystemUptime_Object=MibScalar
systemUptime=_SystemUptime_Object((1,3,6,1,4,1,5951,6,2,18),_SystemUptime_Type())
systemUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:systemUptime.setStatus(_B)
_SystemBiosVersion_Type=OctetString
_SystemBiosVersion_Object=MibScalar
systemBiosVersion=_SystemBiosVersion_Object((1,3,6,1,4,1,5951,6,2,19),_SystemBiosVersion_Type())
systemBiosVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:systemBiosVersion.setStatus(_B)
_SystemMaxThroughput_Type=OctetString
_SystemMaxThroughput_Object=MibScalar
systemMaxThroughput=_SystemMaxThroughput_Object((1,3,6,1,4,1,5951,6,2,20),_SystemMaxThroughput_Type())
systemMaxThroughput.setMaxAccess(_C)
if mibBuilder.loadTexts:systemMaxThroughput.setStatus(_B)
_SystemAvailableThroughput_Type=OctetString
_SystemAvailableThroughput_Object=MibScalar
systemAvailableThroughput=_SystemAvailableThroughput_Object((1,3,6,1,4,1,5951,6,2,21),_SystemAvailableThroughput_Type())
systemAvailableThroughput.setMaxAccess(_C)
if mibBuilder.loadTexts:systemAvailableThroughput.setStatus(_B)
_SystemHostId_Type=OctetString
_SystemHostId_Object=MibScalar
systemHostId=_SystemHostId_Object((1,3,6,1,4,1,5951,6,2,22),_SystemHostId_Type())
systemHostId.setMaxAccess(_C)
if mibBuilder.loadTexts:systemHostId.setStatus(_B)
_SystemCustomID_Type=OctetString
_SystemCustomID_Object=MibScalar
systemCustomID=_SystemCustomID_Object((1,3,6,1,4,1,5951,6,2,23),_SystemCustomID_Type())
systemCustomID.setMaxAccess(_C)
if mibBuilder.loadTexts:systemCustomID.setStatus(_B)
_SystemCpuUsage_Type=OctetString
_SystemCpuUsage_Object=MibScalar
systemCpuUsage=_SystemCpuUsage_Object((1,3,6,1,4,1,5951,6,2,24),_SystemCpuUsage_Type())
systemCpuUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:systemCpuUsage.setStatus(_B)
_SystemMemoryUsage_Type=OctetString
_SystemMemoryUsage_Object=MibScalar
systemMemoryUsage=_SystemMemoryUsage_Object((1,3,6,1,4,1,5951,6,2,25),_SystemMemoryUsage_Type())
systemMemoryUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:systemMemoryUsage.setStatus(_B)
_SystemDiskUsage_Type=OctetString
_SystemDiskUsage_Object=MibScalar
systemDiskUsage=_SystemDiskUsage_Object((1,3,6,1,4,1,5951,6,2,26),_SystemDiskUsage_Type())
systemDiskUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:systemDiskUsage.setStatus(_B)
_SysHealthGroup_ObjectIdentity=ObjectIdentity
sysHealthGroup=_SysHealthGroup_ObjectIdentity((1,3,6,1,4,1,5951,6,2,1000))
_HardwareResourceTable_Object=MibTable
hardwareResourceTable=_HardwareResourceTable_Object((1,3,6,1,4,1,5951,6,2,1000,1))
if mibBuilder.loadTexts:hardwareResourceTable.setStatus(_B)
_HardwareResourceEntry_Object=MibTableRow
hardwareResourceEntry=_HardwareResourceEntry_Object((1,3,6,1,4,1,5951,6,2,1000,1,1))
hardwareResourceEntry.setIndexNames((0,_A,_K),(0,_A,_L),(0,_A,_M))
if mibBuilder.loadTexts:hardwareResourceEntry.setStatus(_B)
_HardwareResourceName_Type=OctetString
_HardwareResourceName_Object=MibTableColumn
hardwareResourceName=_HardwareResourceName_Object((1,3,6,1,4,1,5951,6,2,1000,1,1,1),_HardwareResourceName_Type())
hardwareResourceName.setMaxAccess(_C)
if mibBuilder.loadTexts:hardwareResourceName.setStatus(_B)
_HardwareResourceHostIPAddressType_Type=InetAddressType
_HardwareResourceHostIPAddressType_Object=MibTableColumn
hardwareResourceHostIPAddressType=_HardwareResourceHostIPAddressType_Object((1,3,6,1,4,1,5951,6,2,1000,1,1,2),_HardwareResourceHostIPAddressType_Type())
hardwareResourceHostIPAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:hardwareResourceHostIPAddressType.setStatus(_B)
_HardwareResourceHostIPAddress_Type=InetAddress
_HardwareResourceHostIPAddress_Object=MibTableColumn
hardwareResourceHostIPAddress=_HardwareResourceHostIPAddress_Object((1,3,6,1,4,1,5951,6,2,1000,1,1,3),_HardwareResourceHostIPAddress_Type())
hardwareResourceHostIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hardwareResourceHostIPAddress.setStatus(_B)
_HardwareResourceCurrentValue_Type=OctetString
_HardwareResourceCurrentValue_Object=MibTableColumn
hardwareResourceCurrentValue=_HardwareResourceCurrentValue_Object((1,3,6,1,4,1,5951,6,2,1000,1,1,4),_HardwareResourceCurrentValue_Type())
hardwareResourceCurrentValue.setMaxAccess(_C)
if mibBuilder.loadTexts:hardwareResourceCurrentValue.setStatus(_B)
_HardwareResourceExpectedValue_Type=OctetString
_HardwareResourceExpectedValue_Object=MibTableColumn
hardwareResourceExpectedValue=_HardwareResourceExpectedValue_Object((1,3,6,1,4,1,5951,6,2,1000,1,1,5),_HardwareResourceExpectedValue_Type())
hardwareResourceExpectedValue.setMaxAccess(_C)
if mibBuilder.loadTexts:hardwareResourceExpectedValue.setStatus(_B)
_HardwareResourceUnit_Type=OctetString
_HardwareResourceUnit_Object=MibTableColumn
hardwareResourceUnit=_HardwareResourceUnit_Object((1,3,6,1,4,1,5951,6,2,1000,1,1,6),_HardwareResourceUnit_Type())
hardwareResourceUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:hardwareResourceUnit.setStatus(_B)
_HardwareResourceStatus_Type=OctetString
_HardwareResourceStatus_Object=MibTableColumn
hardwareResourceStatus=_HardwareResourceStatus_Object((1,3,6,1,4,1,5951,6,2,1000,1,1,7),_HardwareResourceStatus_Type())
hardwareResourceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hardwareResourceStatus.setStatus(_B)
_SoftwareResourceTable_Object=MibTable
softwareResourceTable=_SoftwareResourceTable_Object((1,3,6,1,4,1,5951,6,2,1000,2))
if mibBuilder.loadTexts:softwareResourceTable.setStatus(_B)
_SoftwareResourceEntry_Object=MibTableRow
softwareResourceEntry=_SoftwareResourceEntry_Object((1,3,6,1,4,1,5951,6,2,1000,2,1))
softwareResourceEntry.setIndexNames((0,_A,_N),(0,_A,_O),(0,_A,_P))
if mibBuilder.loadTexts:softwareResourceEntry.setStatus(_B)
_SoftwareResourceName_Type=OctetString
_SoftwareResourceName_Object=MibTableColumn
softwareResourceName=_SoftwareResourceName_Object((1,3,6,1,4,1,5951,6,2,1000,2,1,1),_SoftwareResourceName_Type())
softwareResourceName.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareResourceName.setStatus(_B)
_SoftwareResourceHostIPAddressType_Type=InetAddressType
_SoftwareResourceHostIPAddressType_Object=MibTableColumn
softwareResourceHostIPAddressType=_SoftwareResourceHostIPAddressType_Object((1,3,6,1,4,1,5951,6,2,1000,2,1,2),_SoftwareResourceHostIPAddressType_Type())
softwareResourceHostIPAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareResourceHostIPAddressType.setStatus(_B)
_SoftwareResourceHostIPAddress_Type=InetAddress
_SoftwareResourceHostIPAddress_Object=MibTableColumn
softwareResourceHostIPAddress=_SoftwareResourceHostIPAddress_Object((1,3,6,1,4,1,5951,6,2,1000,2,1,3),_SoftwareResourceHostIPAddress_Type())
softwareResourceHostIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareResourceHostIPAddress.setStatus(_B)
_SoftwareResourceCurrentValue_Type=OctetString
_SoftwareResourceCurrentValue_Object=MibTableColumn
softwareResourceCurrentValue=_SoftwareResourceCurrentValue_Object((1,3,6,1,4,1,5951,6,2,1000,2,1,4),_SoftwareResourceCurrentValue_Type())
softwareResourceCurrentValue.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareResourceCurrentValue.setStatus(_B)
_SoftwareResourceExpectedValue_Type=OctetString
_SoftwareResourceExpectedValue_Object=MibTableColumn
softwareResourceExpectedValue=_SoftwareResourceExpectedValue_Object((1,3,6,1,4,1,5951,6,2,1000,2,1,5),_SoftwareResourceExpectedValue_Type())
softwareResourceExpectedValue.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareResourceExpectedValue.setStatus(_B)
_SoftwareResourceUnit_Type=OctetString
_SoftwareResourceUnit_Object=MibTableColumn
softwareResourceUnit=_SoftwareResourceUnit_Object((1,3,6,1,4,1,5951,6,2,1000,2,1,6),_SoftwareResourceUnit_Type())
softwareResourceUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareResourceUnit.setStatus(_B)
_SoftwareResourceStatus_Type=OctetString
_SoftwareResourceStatus_Object=MibTableColumn
softwareResourceStatus=_SoftwareResourceStatus_Object((1,3,6,1,4,1,5951,6,2,1000,2,1,7),_SoftwareResourceStatus_Type())
softwareResourceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:softwareResourceStatus.setStatus(_B)
_DiskTable_Object=MibTable
diskTable=_DiskTable_Object((1,3,6,1,4,1,5951,6,2,1000,3))
if mibBuilder.loadTexts:diskTable.setStatus(_B)
_DiskEntry_Object=MibTableRow
diskEntry=_DiskEntry_Object((1,3,6,1,4,1,5951,6,2,1000,3,1))
diskEntry.setIndexNames((0,_A,_Q),(0,_A,_R),(0,_A,_S))
if mibBuilder.loadTexts:diskEntry.setStatus(_B)
_DiskName_Type=OctetString
_DiskName_Object=MibTableColumn
diskName=_DiskName_Object((1,3,6,1,4,1,5951,6,2,1000,3,1,1),_DiskName_Type())
diskName.setMaxAccess(_C)
if mibBuilder.loadTexts:diskName.setStatus(_B)
_DiskHostIPAddressType_Type=InetAddressType
_DiskHostIPAddressType_Object=MibTableColumn
diskHostIPAddressType=_DiskHostIPAddressType_Object((1,3,6,1,4,1,5951,6,2,1000,3,1,2),_DiskHostIPAddressType_Type())
diskHostIPAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:diskHostIPAddressType.setStatus(_B)
_DiskHostIPAddress_Type=InetAddress
_DiskHostIPAddress_Object=MibTableColumn
diskHostIPAddress=_DiskHostIPAddress_Object((1,3,6,1,4,1,5951,6,2,1000,3,1,3),_DiskHostIPAddress_Type())
diskHostIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:diskHostIPAddress.setStatus(_B)
_DiskTransactionRate_Type=OctetString
_DiskTransactionRate_Object=MibTableColumn
diskTransactionRate=_DiskTransactionRate_Object((1,3,6,1,4,1,5951,6,2,1000,3,1,4),_DiskTransactionRate_Type())
diskTransactionRate.setMaxAccess(_C)
if mibBuilder.loadTexts:diskTransactionRate.setStatus(_B)
_DiskBlockReadRate_Type=OctetString
_DiskBlockReadRate_Object=MibTableColumn
diskBlockReadRate=_DiskBlockReadRate_Object((1,3,6,1,4,1,5951,6,2,1000,3,1,5),_DiskBlockReadRate_Type())
diskBlockReadRate.setMaxAccess(_C)
if mibBuilder.loadTexts:diskBlockReadRate.setStatus(_B)
_DiskBlockWriteRate_Type=OctetString
_DiskBlockWriteRate_Object=MibTableColumn
diskBlockWriteRate=_DiskBlockWriteRate_Object((1,3,6,1,4,1,5951,6,2,1000,3,1,6),_DiskBlockWriteRate_Type())
diskBlockWriteRate.setMaxAccess(_C)
if mibBuilder.loadTexts:diskBlockWriteRate.setStatus(_B)
_DiskTotalBlocksRead_Type=OctetString
_DiskTotalBlocksRead_Object=MibTableColumn
diskTotalBlocksRead=_DiskTotalBlocksRead_Object((1,3,6,1,4,1,5951,6,2,1000,3,1,7),_DiskTotalBlocksRead_Type())
diskTotalBlocksRead.setMaxAccess(_C)
if mibBuilder.loadTexts:diskTotalBlocksRead.setStatus(_B)
_DiskTotalBlocksWritten_Type=OctetString
_DiskTotalBlocksWritten_Object=MibTableColumn
diskTotalBlocksWritten=_DiskTotalBlocksWritten_Object((1,3,6,1,4,1,5951,6,2,1000,3,1,8),_DiskTotalBlocksWritten_Type())
diskTotalBlocksWritten.setMaxAccess(_C)
if mibBuilder.loadTexts:diskTotalBlocksWritten.setStatus(_B)
_DiskUtilized_Type=OctetString
_DiskUtilized_Object=MibTableColumn
diskUtilized=_DiskUtilized_Object((1,3,6,1,4,1,5951,6,2,1000,3,1,9),_DiskUtilized_Type())
diskUtilized.setMaxAccess(_C)
if mibBuilder.loadTexts:diskUtilized.setStatus(_B)
_DiskSize_Type=OctetString
_DiskSize_Object=MibTableColumn
diskSize=_DiskSize_Object((1,3,6,1,4,1,5951,6,2,1000,3,1,10),_DiskSize_Type())
diskSize.setMaxAccess(_C)
if mibBuilder.loadTexts:diskSize.setStatus(_B)
_DiskBayNumber_Type=OctetString
_DiskBayNumber_Object=MibTableColumn
diskBayNumber=_DiskBayNumber_Object((1,3,6,1,4,1,5951,6,2,1000,3,1,11),_DiskBayNumber_Type())
diskBayNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:diskBayNumber.setStatus(_B)
_SrTable_Object=MibTable
srTable=_SrTable_Object((1,3,6,1,4,1,5951,6,2,1000,4))
if mibBuilder.loadTexts:srTable.setStatus(_B)
_SrEntry_Object=MibTableRow
srEntry=_SrEntry_Object((1,3,6,1,4,1,5951,6,2,1000,4,1))
srEntry.setIndexNames((0,_A,_T),(0,_A,_U),(0,_A,_V),(0,_A,_W))
if mibBuilder.loadTexts:srEntry.setStatus(_B)
_SrName_Type=OctetString
_SrName_Object=MibTableColumn
srName=_SrName_Object((1,3,6,1,4,1,5951,6,2,1000,4,1,1),_SrName_Type())
srName.setMaxAccess(_C)
if mibBuilder.loadTexts:srName.setStatus(_B)
_SrBayNumber_Type=OctetString
_SrBayNumber_Object=MibTableColumn
srBayNumber=_SrBayNumber_Object((1,3,6,1,4,1,5951,6,2,1000,4,1,2),_SrBayNumber_Type())
srBayNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:srBayNumber.setStatus(_B)
_SrHostIPAddressType_Type=InetAddressType
_SrHostIPAddressType_Object=MibTableColumn
srHostIPAddressType=_SrHostIPAddressType_Object((1,3,6,1,4,1,5951,6,2,1000,4,1,3),_SrHostIPAddressType_Type())
srHostIPAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:srHostIPAddressType.setStatus(_B)
_SrHostIPAddress_Type=InetAddress
_SrHostIPAddress_Object=MibTableColumn
srHostIPAddress=_SrHostIPAddress_Object((1,3,6,1,4,1,5951,6,2,1000,4,1,4),_SrHostIPAddress_Type())
srHostIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:srHostIPAddress.setStatus(_B)
_SrUtilized_Type=OctetString
_SrUtilized_Object=MibTableColumn
srUtilized=_SrUtilized_Object((1,3,6,1,4,1,5951,6,2,1000,4,1,5),_SrUtilized_Type())
srUtilized.setMaxAccess(_C)
if mibBuilder.loadTexts:srUtilized.setStatus(_B)
_SrSize_Type=OctetString
_SrSize_Object=MibTableColumn
srSize=_SrSize_Object((1,3,6,1,4,1,5951,6,2,1000,4,1,6),_SrSize_Type())
srSize.setMaxAccess(_C)
if mibBuilder.loadTexts:srSize.setStatus(_B)
_SrStatus_Type=OctetString
_SrStatus_Object=MibTableColumn
srStatus=_SrStatus_Object((1,3,6,1,4,1,5951,6,2,1000,4,1,7),_SrStatus_Type())
srStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:srStatus.setStatus(_B)
_InterfaceTable_Object=MibTable
interfaceTable=_InterfaceTable_Object((1,3,6,1,4,1,5951,6,2,1000,5))
if mibBuilder.loadTexts:interfaceTable.setStatus(_B)
_InterfaceEntry_Object=MibTableRow
interfaceEntry=_InterfaceEntry_Object((1,3,6,1,4,1,5951,6,2,1000,5,1))
interfaceEntry.setIndexNames((0,_A,_X),(0,_A,_Y),(0,_A,_Z))
if mibBuilder.loadTexts:interfaceEntry.setStatus(_B)
_InterfacePort_Type=OctetString
_InterfacePort_Object=MibTableColumn
interfacePort=_InterfacePort_Object((1,3,6,1,4,1,5951,6,2,1000,5,1,1),_InterfacePort_Type())
interfacePort.setMaxAccess(_C)
if mibBuilder.loadTexts:interfacePort.setStatus(_B)
_InterfaceHostIPAddressType_Type=InetAddressType
_InterfaceHostIPAddressType_Object=MibTableColumn
interfaceHostIPAddressType=_InterfaceHostIPAddressType_Object((1,3,6,1,4,1,5951,6,2,1000,5,1,2),_InterfaceHostIPAddressType_Type())
interfaceHostIPAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:interfaceHostIPAddressType.setStatus(_B)
_InterfaceHostIPAddress_Type=InetAddress
_InterfaceHostIPAddress_Object=MibTableColumn
interfaceHostIPAddress=_InterfaceHostIPAddress_Object((1,3,6,1,4,1,5951,6,2,1000,5,1,3),_InterfaceHostIPAddress_Type())
interfaceHostIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:interfaceHostIPAddress.setStatus(_B)
_InterfaceState_Type=OctetString
_InterfaceState_Object=MibTableColumn
interfaceState=_InterfaceState_Object((1,3,6,1,4,1,5951,6,2,1000,5,1,4),_InterfaceState_Type())
interfaceState.setMaxAccess(_C)
if mibBuilder.loadTexts:interfaceState.setStatus(_B)
_InterfaceRxPackets_Type=OctetString
_InterfaceRxPackets_Object=MibTableColumn
interfaceRxPackets=_InterfaceRxPackets_Object((1,3,6,1,4,1,5951,6,2,1000,5,1,5),_InterfaceRxPackets_Type())
interfaceRxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:interfaceRxPackets.setStatus(_B)
_InterfaceTxPackets_Type=OctetString
_InterfaceTxPackets_Object=MibTableColumn
interfaceTxPackets=_InterfaceTxPackets_Object((1,3,6,1,4,1,5951,6,2,1000,5,1,6),_InterfaceTxPackets_Type())
interfaceTxPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:interfaceTxPackets.setStatus(_B)
_InterfaceRxBytes_Type=OctetString
_InterfaceRxBytes_Object=MibTableColumn
interfaceRxBytes=_InterfaceRxBytes_Object((1,3,6,1,4,1,5951,6,2,1000,5,1,7),_InterfaceRxBytes_Type())
interfaceRxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:interfaceRxBytes.setStatus(_B)
_InterfaceTxBytes_Type=OctetString
_InterfaceTxBytes_Object=MibTableColumn
interfaceTxBytes=_InterfaceTxBytes_Object((1,3,6,1,4,1,5951,6,2,1000,5,1,8),_InterfaceTxBytes_Type())
interfaceTxBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:interfaceTxBytes.setStatus(_B)
_InterfaceRxErrors_Type=OctetString
_InterfaceRxErrors_Object=MibTableColumn
interfaceRxErrors=_InterfaceRxErrors_Object((1,3,6,1,4,1,5951,6,2,1000,5,1,9),_InterfaceRxErrors_Type())
interfaceRxErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:interfaceRxErrors.setStatus(_B)
_InterfaceTxErrors_Type=OctetString
_InterfaceTxErrors_Object=MibTableColumn
interfaceTxErrors=_InterfaceTxErrors_Object((1,3,6,1,4,1,5951,6,2,1000,5,1,10),_InterfaceTxErrors_Type())
interfaceTxErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:interfaceTxErrors.setStatus(_B)
_InterfaceVfTotal_Type=Integer32
_InterfaceVfTotal_Object=MibTableColumn
interfaceVfTotal=_InterfaceVfTotal_Object((1,3,6,1,4,1,5951,6,2,1000,5,1,11),_InterfaceVfTotal_Type())
interfaceVfTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:interfaceVfTotal.setStatus(_B)
_InterfaceVfAssigned_Type=Integer32
_InterfaceVfAssigned_Object=MibTableColumn
interfaceVfAssigned=_InterfaceVfAssigned_Object((1,3,6,1,4,1,5951,6,2,1000,5,1,12),_InterfaceVfAssigned_Type())
interfaceVfAssigned.setMaxAccess(_C)
if mibBuilder.loadTexts:interfaceVfAssigned.setStatus(_B)
_InterfaceMappedPort_Type=OctetString
_InterfaceMappedPort_Object=MibTableColumn
interfaceMappedPort=_InterfaceMappedPort_Object((1,3,6,1,4,1,5951,6,2,1000,5,1,13),_InterfaceMappedPort_Type())
interfaceMappedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:interfaceMappedPort.setStatus(_B)
_HealthMonitoringTable_Object=MibTable
healthMonitoringTable=_HealthMonitoringTable_Object((1,3,6,1,4,1,5951,6,2,1000,6))
if mibBuilder.loadTexts:healthMonitoringTable.setStatus(_B)
_HealthMonitoringEntry_Object=MibTableRow
healthMonitoringEntry=_HealthMonitoringEntry_Object((1,3,6,1,4,1,5951,6,2,1000,6,1))
healthMonitoringEntry.setIndexNames((0,_A,_a),(0,_A,_b),(0,_A,_c))
if mibBuilder.loadTexts:healthMonitoringEntry.setStatus(_B)
_HmName_Type=OctetString
_HmName_Object=MibTableColumn
hmName=_HmName_Object((1,3,6,1,4,1,5951,6,2,1000,6,1,1),_HmName_Type())
hmName.setMaxAccess(_C)
if mibBuilder.loadTexts:hmName.setStatus(_B)
_HmHostIPAddressType_Type=InetAddressType
_HmHostIPAddressType_Object=MibTableColumn
hmHostIPAddressType=_HmHostIPAddressType_Object((1,3,6,1,4,1,5951,6,2,1000,6,1,2),_HmHostIPAddressType_Type())
hmHostIPAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:hmHostIPAddressType.setStatus(_B)
_HmHostIPAddress_Type=InetAddress
_HmHostIPAddress_Object=MibTableColumn
hmHostIPAddress=_HmHostIPAddress_Object((1,3,6,1,4,1,5951,6,2,1000,6,1,3),_HmHostIPAddress_Type())
hmHostIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hmHostIPAddress.setStatus(_B)
_HmStatus_Type=OctetString
_HmStatus_Object=MibTableColumn
hmStatus=_HmStatus_Object((1,3,6,1,4,1,5951,6,2,1000,6,1,4),_HmStatus_Type())
hmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hmStatus.setStatus(_B)
_HmNoOfFailures_Type=Integer32
_HmNoOfFailures_Object=MibTableColumn
hmNoOfFailures=_HmNoOfFailures_Object((1,3,6,1,4,1,5951,6,2,1000,6,1,5),_HmNoOfFailures_Type())
hmNoOfFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:hmNoOfFailures.setStatus(_B)
_HmUnit_Type=OctetString
_HmUnit_Object=MibTableColumn
hmUnit=_HmUnit_Object((1,3,6,1,4,1,5951,6,2,1000,6,1,6),_HmUnit_Type())
hmUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:hmUnit.setStatus(_B)
_HmCurrentValue_Type=OctetString
_HmCurrentValue_Object=MibTableColumn
hmCurrentValue=_HmCurrentValue_Object((1,3,6,1,4,1,5951,6,2,1000,6,1,7),_HmCurrentValue_Type())
hmCurrentValue.setMaxAccess(_C)
if mibBuilder.loadTexts:hmCurrentValue.setStatus(_B)
_DeviceGroup_ObjectIdentity=ObjectIdentity
deviceGroup=_DeviceGroup_ObjectIdentity((1,3,6,1,4,1,5951,6,3))
_XenTable_Object=MibTable
xenTable=_XenTable_Object((1,3,6,1,4,1,5951,6,3,1))
if mibBuilder.loadTexts:xenTable.setStatus(_B)
_XenEntry_Object=MibTableRow
xenEntry=_XenEntry_Object((1,3,6,1,4,1,5951,6,3,1,1))
xenEntry.setIndexNames((0,_A,_d),(0,_A,_e))
if mibBuilder.loadTexts:xenEntry.setStatus(_B)
_XenIpAddressType_Type=InetAddressType
_XenIpAddressType_Object=MibTableColumn
xenIpAddressType=_XenIpAddressType_Object((1,3,6,1,4,1,5951,6,3,1,1,1),_XenIpAddressType_Type())
xenIpAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:xenIpAddressType.setStatus(_B)
_XenIpAddress_Type=InetAddress
_XenIpAddress_Object=MibTableColumn
xenIpAddress=_XenIpAddress_Object((1,3,6,1,4,1,5951,6,3,1,1,2),_XenIpAddress_Type())
xenIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:xenIpAddress.setStatus(_B)
_XenHostname_Type=OctetString
_XenHostname_Object=MibTableColumn
xenHostname=_XenHostname_Object((1,3,6,1,4,1,5951,6,3,1,1,3),_XenHostname_Type())
xenHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:xenHostname.setStatus(_B)
_XenDescription_Type=OctetString
_XenDescription_Object=MibTableColumn
xenDescription=_XenDescription_Object((1,3,6,1,4,1,5951,6,3,1,1,4),_XenDescription_Type())
xenDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:xenDescription.setStatus(_B)
_XenVersion_Type=OctetString
_XenVersion_Object=MibTableColumn
xenVersion=_XenVersion_Object((1,3,6,1,4,1,5951,6,3,1,1,5),_XenVersion_Type())
xenVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:xenVersion.setStatus(_B)
_XenUuid_Type=OctetString
_XenUuid_Object=MibTableColumn
xenUuid=_XenUuid_Object((1,3,6,1,4,1,5951,6,3,1,1,6),_XenUuid_Type())
xenUuid.setMaxAccess(_C)
if mibBuilder.loadTexts:xenUuid.setStatus(_B)
_XenNumberOfCPU_Type=Integer32
_XenNumberOfCPU_Object=MibTableColumn
xenNumberOfCPU=_XenNumberOfCPU_Object((1,3,6,1,4,1,5951,6,3,1,1,7),_XenNumberOfCPU_Type())
xenNumberOfCPU.setMaxAccess(_C)
if mibBuilder.loadTexts:xenNumberOfCPU.setStatus(_B)
_XenCpuUsage_Type=OctetString
_XenCpuUsage_Object=MibTableColumn
xenCpuUsage=_XenCpuUsage_Object((1,3,6,1,4,1,5951,6,3,1,1,8),_XenCpuUsage_Type())
xenCpuUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:xenCpuUsage.setStatus(_B)
_XenMemoryTotal_Type=OctetString
_XenMemoryTotal_Object=MibTableColumn
xenMemoryTotal=_XenMemoryTotal_Object((1,3,6,1,4,1,5951,6,3,1,1,9),_XenMemoryTotal_Type())
xenMemoryTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:xenMemoryTotal.setStatus(_B)
_XenMemoryFree_Type=OctetString
_XenMemoryFree_Object=MibTableColumn
xenMemoryFree=_XenMemoryFree_Object((1,3,6,1,4,1,5951,6,3,1,1,10),_XenMemoryFree_Type())
xenMemoryFree.setMaxAccess(_C)
if mibBuilder.loadTexts:xenMemoryFree.setStatus(_B)
_XenMemoryUsage_Type=OctetString
_XenMemoryUsage_Object=MibTableColumn
xenMemoryUsage=_XenMemoryUsage_Object((1,3,6,1,4,1,5951,6,3,1,1,11),_XenMemoryUsage_Type())
xenMemoryUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:xenMemoryUsage.setStatus(_B)
_XenTx_Type=OctetString
_XenTx_Object=MibTableColumn
xenTx=_XenTx_Object((1,3,6,1,4,1,5951,6,3,1,1,12),_XenTx_Type())
xenTx.setMaxAccess(_C)
if mibBuilder.loadTexts:xenTx.setStatus(_B)
_XenRx_Type=OctetString
_XenRx_Object=MibTableColumn
xenRx=_XenRx_Object((1,3,6,1,4,1,5951,6,3,1,1,13),_XenRx_Type())
xenRx.setMaxAccess(_C)
if mibBuilder.loadTexts:xenRx.setStatus(_B)
_XenUptime_Type=OctetString
_XenUptime_Object=MibTableColumn
xenUptime=_XenUptime_Object((1,3,6,1,4,1,5951,6,3,1,1,14),_XenUptime_Type())
xenUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:xenUptime.setStatus(_B)
_XenSslCoresTotal_Type=Integer32
_XenSslCoresTotal_Object=MibTableColumn
xenSslCoresTotal=_XenSslCoresTotal_Object((1,3,6,1,4,1,5951,6,3,1,1,15),_XenSslCoresTotal_Type())
xenSslCoresTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:xenSslCoresTotal.setStatus(_B)
_XenIscsiIQN_Type=OctetString
_XenIscsiIQN_Object=MibTableColumn
xenIscsiIQN=_XenIscsiIQN_Object((1,3,6,1,4,1,5951,6,3,1,1,16),_XenIscsiIQN_Type())
xenIscsiIQN.setMaxAccess(_C)
if mibBuilder.loadTexts:xenIscsiIQN.setStatus(_B)
_XenEdition_Type=OctetString
_XenEdition_Object=MibTableColumn
xenEdition=_XenEdition_Object((1,3,6,1,4,1,5951,6,3,1,1,17),_XenEdition_Type())
xenEdition.setMaxAccess(_C)
if mibBuilder.loadTexts:xenEdition.setStatus(_B)
_XenExpiry_Type=OctetString
_XenExpiry_Object=MibTableColumn
xenExpiry=_XenExpiry_Object((1,3,6,1,4,1,5951,6,3,1,1,18),_XenExpiry_Type())
xenExpiry.setMaxAccess(_C)
if mibBuilder.loadTexts:xenExpiry.setStatus(_B)
_XenProductCode_Type=OctetString
_XenProductCode_Object=MibTableColumn
xenProductCode=_XenProductCode_Object((1,3,6,1,4,1,5951,6,3,1,1,19),_XenProductCode_Type())
xenProductCode.setMaxAccess(_C)
if mibBuilder.loadTexts:xenProductCode.setStatus(_B)
_XenSerialNumber_Type=OctetString
_XenSerialNumber_Object=MibTableColumn
xenSerialNumber=_XenSerialNumber_Object((1,3,6,1,4,1,5951,6,3,1,1,20),_XenSerialNumber_Type())
xenSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:xenSerialNumber.setStatus(_B)
_XenVersionLong_Type=OctetString
_XenVersionLong_Object=MibTableColumn
xenVersionLong=_XenVersionLong_Object((1,3,6,1,4,1,5951,6,3,1,1,21),_XenVersionLong_Type())
xenVersionLong.setMaxAccess(_C)
if mibBuilder.loadTexts:xenVersionLong.setStatus(_B)
_XenVersionShort_Type=OctetString
_XenVersionShort_Object=MibTableColumn
xenVersionShort=_XenVersionShort_Object((1,3,6,1,4,1,5951,6,3,1,1,22),_XenVersionShort_Type())
xenVersionShort.setMaxAccess(_C)
if mibBuilder.loadTexts:xenVersionShort.setStatus(_B)
_XenBuildNumber_Type=OctetString
_XenBuildNumber_Object=MibTableColumn
xenBuildNumber=_XenBuildNumber_Object((1,3,6,1,4,1,5951,6,3,1,1,23),_XenBuildNumber_Type())
xenBuildNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:xenBuildNumber.setStatus(_B)
_XenBuildDate_Type=OctetString
_XenBuildDate_Object=MibTableColumn
xenBuildDate=_XenBuildDate_Object((1,3,6,1,4,1,5951,6,3,1,1,24),_XenBuildDate_Type())
xenBuildDate.setMaxAccess(_C)
if mibBuilder.loadTexts:xenBuildDate.setStatus(_B)
_XenNumberOfCPUCores_Type=Integer32
_XenNumberOfCPUCores_Object=MibTableColumn
xenNumberOfCPUCores=_XenNumberOfCPUCores_Object((1,3,6,1,4,1,5951,6,3,1,1,25),_XenNumberOfCPUCores_Type())
xenNumberOfCPUCores.setMaxAccess(_C)
if mibBuilder.loadTexts:xenNumberOfCPUCores.setStatus(_B)
_NetscalerTable_Object=MibTable
netscalerTable=_NetscalerTable_Object((1,3,6,1,4,1,5951,6,3,2))
if mibBuilder.loadTexts:netscalerTable.setStatus(_B)
_NetscalerEntry_Object=MibTableRow
netscalerEntry=_NetscalerEntry_Object((1,3,6,1,4,1,5951,6,3,2,1))
netscalerEntry.setIndexNames((0,_A,_f),(0,_A,_g),(0,_A,_h),(0,_A,_i))
if mibBuilder.loadTexts:netscalerEntry.setStatus(_B)
_NsIpAddressType_Type=InetAddressType
_NsIpAddressType_Object=MibTableColumn
nsIpAddressType=_NsIpAddressType_Object((1,3,6,1,4,1,5951,6,3,2,1,1),_NsIpAddressType_Type())
nsIpAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:nsIpAddressType.setStatus(_B)
_NsIpAddress_Type=InetAddress
_NsIpAddress_Object=MibTableColumn
nsIpAddress=_NsIpAddress_Object((1,3,6,1,4,1,5951,6,3,2,1,2),_NsIpAddress_Type())
nsIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:nsIpAddress.setStatus(_B)
_NsHostIPAddressType_Type=InetAddressType
_NsHostIPAddressType_Object=MibTableColumn
nsHostIPAddressType=_NsHostIPAddressType_Object((1,3,6,1,4,1,5951,6,3,2,1,3),_NsHostIPAddressType_Type())
nsHostIPAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:nsHostIPAddressType.setStatus(_B)
_NsHostIPAddress_Type=InetAddress
_NsHostIPAddress_Object=MibTableColumn
nsHostIPAddress=_NsHostIPAddress_Object((1,3,6,1,4,1,5951,6,3,2,1,4),_NsHostIPAddress_Type())
nsHostIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:nsHostIPAddress.setStatus(_B)
_NsProfileName_Type=OctetString
_NsProfileName_Object=MibTableColumn
nsProfileName=_NsProfileName_Object((1,3,6,1,4,1,5951,6,3,2,1,5),_NsProfileName_Type())
nsProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:nsProfileName.setStatus(_B)
_NsName_Type=OctetString
_NsName_Object=MibTableColumn
nsName=_NsName_Object((1,3,6,1,4,1,5951,6,3,2,1,6),_NsName_Type())
nsName.setMaxAccess(_C)
if mibBuilder.loadTexts:nsName.setStatus(_B)
_NsNetmaskType_Type=InetAddressType
_NsNetmaskType_Object=MibTableColumn
nsNetmaskType=_NsNetmaskType_Object((1,3,6,1,4,1,5951,6,3,2,1,7),_NsNetmaskType_Type())
nsNetmaskType.setMaxAccess(_C)
if mibBuilder.loadTexts:nsNetmaskType.setStatus(_B)
_NsNetmask_Type=InetAddress
_NsNetmask_Object=MibTableColumn
nsNetmask=_NsNetmask_Object((1,3,6,1,4,1,5951,6,3,2,1,8),_NsNetmask_Type())
nsNetmask.setMaxAccess(_C)
if mibBuilder.loadTexts:nsNetmask.setStatus(_B)
_NsGatewayType_Type=InetAddressType
_NsGatewayType_Object=MibTableColumn
nsGatewayType=_NsGatewayType_Object((1,3,6,1,4,1,5951,6,3,2,1,9),_NsGatewayType_Type())
nsGatewayType.setMaxAccess(_C)
if mibBuilder.loadTexts:nsGatewayType.setStatus(_B)
_NsGateway_Type=InetAddress
_NsGateway_Object=MibTableColumn
nsGateway=_NsGateway_Object((1,3,6,1,4,1,5951,6,3,2,1,10),_NsGateway_Type())
nsGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:nsGateway.setStatus(_B)
_NsHostname_Type=OctetString
_NsHostname_Object=MibTableColumn
nsHostname=_NsHostname_Object((1,3,6,1,4,1,5951,6,3,2,1,11),_NsHostname_Type())
nsHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:nsHostname.setStatus(_B)
_NsDescription_Type=OctetString
_NsDescription_Object=MibTableColumn
nsDescription=_NsDescription_Object((1,3,6,1,4,1,5951,6,3,2,1,12),_NsDescription_Type())
nsDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:nsDescription.setStatus(_B)
_NsVersion_Type=OctetString
_NsVersion_Object=MibTableColumn
nsVersion=_NsVersion_Object((1,3,6,1,4,1,5951,6,3,2,1,13),_NsVersion_Type())
nsVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:nsVersion.setStatus(_B)
_NsUuid_Type=OctetString
_NsUuid_Object=MibTableColumn
nsUuid=_NsUuid_Object((1,3,6,1,4,1,5951,6,3,2,1,14),_NsUuid_Type())
nsUuid.setMaxAccess(_C)
if mibBuilder.loadTexts:nsUuid.setStatus(_B)
_NsInstanceState_Type=OctetString
_NsInstanceState_Object=MibTableColumn
nsInstanceState=_NsInstanceState_Object((1,3,6,1,4,1,5951,6,3,2,1,15),_NsInstanceState_Type())
nsInstanceState.setMaxAccess(_C)
if mibBuilder.loadTexts:nsInstanceState.setStatus(_B)
_NsVirtualFunctions_Type=OctetString
_NsVirtualFunctions_Object=MibTableColumn
nsVirtualFunctions=_NsVirtualFunctions_Object((1,3,6,1,4,1,5951,6,3,2,1,16),_NsVirtualFunctions_Type())
nsVirtualFunctions.setMaxAccess(_C)
if mibBuilder.loadTexts:nsVirtualFunctions.setStatus(_B)
_NsSslVirtualFunctions_Type=OctetString
_NsSslVirtualFunctions_Object=MibTableColumn
nsSslVirtualFunctions=_NsSslVirtualFunctions_Object((1,3,6,1,4,1,5951,6,3,2,1,17),_NsSslVirtualFunctions_Type())
nsSslVirtualFunctions.setMaxAccess(_C)
if mibBuilder.loadTexts:nsSslVirtualFunctions.setStatus(_B)
_NsVmState_Type=OctetString
_NsVmState_Object=MibTableColumn
nsVmState=_NsVmState_Object((1,3,6,1,4,1,5951,6,3,2,1,18),_NsVmState_Type())
nsVmState.setMaxAccess(_C)
if mibBuilder.loadTexts:nsVmState.setStatus(_B)
_NsNumberOfCPU_Type=Integer32
_NsNumberOfCPU_Object=MibTableColumn
nsNumberOfCPU=_NsNumberOfCPU_Object((1,3,6,1,4,1,5951,6,3,2,1,19),_NsNumberOfCPU_Type())
nsNumberOfCPU.setMaxAccess(_C)
if mibBuilder.loadTexts:nsNumberOfCPU.setStatus(_B)
_NsVmMemoryTotal_Type=OctetString
_NsVmMemoryTotal_Object=MibTableColumn
nsVmMemoryTotal=_NsVmMemoryTotal_Object((1,3,6,1,4,1,5951,6,3,2,1,21),_NsVmMemoryTotal_Type())
nsVmMemoryTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:nsVmMemoryTotal.setStatus(_B)
_NsUptime_Type=OctetString
_NsUptime_Object=MibTableColumn
nsUptime=_NsUptime_Object((1,3,6,1,4,1,5951,6,3,2,1,26),_NsUptime_Type())
nsUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:nsUptime.setStatus(_B)
_NsNumberOfSSLCores_Type=Integer32
_NsNumberOfSSLCores_Object=MibTableColumn
nsNumberOfSSLCores=_NsNumberOfSSLCores_Object((1,3,6,1,4,1,5951,6,3,2,1,27),_NsNumberOfSSLCores_Type())
nsNumberOfSSLCores.setMaxAccess(_C)
if mibBuilder.loadTexts:nsNumberOfSSLCores.setStatus(_B)
_NsCpuCoreMgmt_Type=OctetString
_NsCpuCoreMgmt_Object=MibTableColumn
nsCpuCoreMgmt=_NsCpuCoreMgmt_Object((1,3,6,1,4,1,5951,6,3,2,1,28),_NsCpuCoreMgmt_Type())
nsCpuCoreMgmt.setMaxAccess(_C)
if mibBuilder.loadTexts:nsCpuCoreMgmt.setStatus(_B)
_NsCpuCorePE_Type=OctetString
_NsCpuCorePE_Object=MibTableColumn
nsCpuCorePE=_NsCpuCorePE_Object((1,3,6,1,4,1,5951,6,3,2,1,29),_NsCpuCorePE_Type())
nsCpuCorePE.setMaxAccess(_C)
if mibBuilder.loadTexts:nsCpuCorePE.setStatus(_B)
_NsVmDescription_Type=OctetString
_NsVmDescription_Object=MibTableColumn
nsVmDescription=_NsVmDescription_Object((1,3,6,1,4,1,5951,6,3,2,1,30),_NsVmDescription_Type())
nsVmDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:nsVmDescription.setStatus(_B)
_NsThroughput_Type=OctetString
_NsThroughput_Object=MibTableColumn
nsThroughput=_NsThroughput_Object((1,3,6,1,4,1,5951,6,3,2,1,31),_NsThroughput_Type())
nsThroughput.setMaxAccess(_C)
if mibBuilder.loadTexts:nsThroughput.setStatus(_B)
_NsNumberOfCores_Type=Integer32
_NsNumberOfCores_Object=MibTableColumn
nsNumberOfCores=_NsNumberOfCores_Object((1,3,6,1,4,1,5951,6,3,2,1,32),_NsNumberOfCores_Type())
nsNumberOfCores.setMaxAccess(_C)
if mibBuilder.loadTexts:nsNumberOfCores.setStatus(_B)
_NsNsCPUUsage_Type=OctetString
_NsNsCPUUsage_Object=MibTableColumn
nsNsCPUUsage=_NsNsCPUUsage_Object((1,3,6,1,4,1,5951,6,3,2,1,33),_NsNsCPUUsage_Type())
nsNsCPUUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:nsNsCPUUsage.setStatus(_B)
_NsNsMemoryUsage_Type=OctetString
_NsNsMemoryUsage_Object=MibTableColumn
nsNsMemoryUsage=_NsNsMemoryUsage_Object((1,3,6,1,4,1,5951,6,3,2,1,35),_NsNsMemoryUsage_Type())
nsNsMemoryUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:nsNsMemoryUsage.setStatus(_B)
_NsNsTx_Type=OctetString
_NsNsTx_Object=MibTableColumn
nsNsTx=_NsNsTx_Object((1,3,6,1,4,1,5951,6,3,2,1,36),_NsNsTx_Type())
nsNsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:nsNsTx.setStatus(_B)
_NsNsRx_Type=OctetString
_NsNsRx_Object=MibTableColumn
nsNsRx=_NsNsRx_Object((1,3,6,1,4,1,5951,6,3,2,1,37),_NsNsRx_Type())
nsNsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:nsNsRx.setStatus(_B)
_NsHttpReq_Type=OctetString
_NsHttpReq_Object=MibTableColumn
nsHttpReq=_NsHttpReq_Object((1,3,6,1,4,1,5951,6,3,2,1,38),_NsHttpReq_Type())
nsHttpReq.setMaxAccess(_C)
if mibBuilder.loadTexts:nsHttpReq.setStatus(_B)
_NsUpsince_Type=OctetString
_NsUpsince_Object=MibTableColumn
nsUpsince=_NsUpsince_Object((1,3,6,1,4,1,5951,6,3,2,1,39),_NsUpsince_Type())
nsUpsince.setMaxAccess(_C)
if mibBuilder.loadTexts:nsUpsince.setStatus(_B)
_NsLicense_Type=OctetString
_NsLicense_Object=MibTableColumn
nsLicense=_NsLicense_Object((1,3,6,1,4,1,5951,6,3,2,1,40),_NsLicense_Type())
nsLicense.setMaxAccess(_C)
if mibBuilder.loadTexts:nsLicense.setStatus(_B)
_NsHaMasterState_Type=OctetString
_NsHaMasterState_Object=MibTableColumn
nsHaMasterState=_NsHaMasterState_Object((1,3,6,1,4,1,5951,6,3,2,1,41),_NsHaMasterState_Type())
nsHaMasterState.setMaxAccess(_C)
if mibBuilder.loadTexts:nsHaMasterState.setStatus(_B)
_NsHaIPAddressType_Type=InetAddressType
_NsHaIPAddressType_Object=MibTableColumn
nsHaIPAddressType=_NsHaIPAddressType_Object((1,3,6,1,4,1,5951,6,3,2,1,42),_NsHaIPAddressType_Type())
nsHaIPAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:nsHaIPAddressType.setStatus(_B)
_NsHaIPAddress_Type=InetAddress
_NsHaIPAddress_Object=MibTableColumn
nsHaIPAddress=_NsHaIPAddress_Object((1,3,6,1,4,1,5951,6,3,2,1,43),_NsHaIPAddress_Type())
nsHaIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:nsHaIPAddress.setStatus(_B)
_NsNodeState_Type=OctetString
_NsNodeState_Object=MibTableColumn
nsNodeState=_NsNodeState_Object((1,3,6,1,4,1,5951,6,3,2,1,44),_NsNodeState_Type())
nsNodeState.setMaxAccess(_C)
if mibBuilder.loadTexts:nsNodeState.setStatus(_B)
_NsHaSync_Type=OctetString
_NsHaSync_Object=MibTableColumn
nsHaSync=_NsHaSync_Object((1,3,6,1,4,1,5951,6,3,2,1,45),_NsHaSync_Type())
nsHaSync.setMaxAccess(_C)
if mibBuilder.loadTexts:nsHaSync.setStatus(_B)
_NsPps_Type=OctetString
_NsPps_Object=MibTableColumn
nsPps=_NsPps_Object((1,3,6,1,4,1,5951,6,3,2,1,46),_NsPps_Type())
nsPps.setMaxAccess(_C)
if mibBuilder.loadTexts:nsPps.setStatus(_B)
_NsNumberOfSslCoresUp_Type=Integer32
_NsNumberOfSslCoresUp_Object=MibTableColumn
nsNumberOfSslCoresUp=_NsNumberOfSslCoresUp_Object((1,3,6,1,4,1,5951,6,3,2,1,47),_NsNumberOfSslCoresUp_Type())
nsNumberOfSslCoresUp.setMaxAccess(_C)
if mibBuilder.loadTexts:nsNumberOfSslCoresUp.setStatus(_B)
_NsIfOby1_Type=OctetString
_NsIfOby1_Object=MibTableColumn
nsIfOby1=_NsIfOby1_Object((1,3,6,1,4,1,5951,6,3,2,1,48),_NsIfOby1_Type())
nsIfOby1.setMaxAccess(_C)
if mibBuilder.loadTexts:nsIfOby1.setStatus(_B)
_NsIf0by2_Type=OctetString
_NsIf0by2_Object=MibTableColumn
nsIf0by2=_NsIf0by2_Object((1,3,6,1,4,1,5951,6,3,2,1,49),_NsIf0by2_Type())
nsIf0by2.setMaxAccess(_C)
if mibBuilder.loadTexts:nsIf0by2.setStatus(_B)
_NsNsVLANId_Type=Integer32
_NsNsVLANId_Object=MibTableColumn
nsNsVLANId=_NsNsVLANId_Object((1,3,6,1,4,1,5951,6,3,2,1,50),_NsNsVLANId_Type())
nsNsVLANId.setMaxAccess(_C)
if mibBuilder.loadTexts:nsNsVLANId.setStatus(_B)
_NsNsVLANTagged_Type=OctetString
_NsNsVLANTagged_Object=MibTableColumn
nsNsVLANTagged=_NsNsVLANTagged_Object((1,3,6,1,4,1,5951,6,3,2,1,51),_NsNsVLANTagged_Type())
nsNsVLANTagged.setMaxAccess(_C)
if mibBuilder.loadTexts:nsNsVLANTagged.setStatus(_B)
_NsVlanType_Type=Integer32
_NsVlanType_Object=MibTableColumn
nsVlanType=_NsVlanType_Object((1,3,6,1,4,1,5951,6,3,2,1,52),_NsVlanType_Type())
nsVlanType.setMaxAccess(_C)
if mibBuilder.loadTexts:nsVlanType.setStatus(_B)
_NetscalerSDWANInstanceTable_Object=MibTable
netscalerSDWANInstanceTable=_NetscalerSDWANInstanceTable_Object((1,3,6,1,4,1,5951,6,3,3))
if mibBuilder.loadTexts:netscalerSDWANInstanceTable.setStatus(_B)
_NetscalerSDWANInstanceEntry_Object=MibTableRow
netscalerSDWANInstanceEntry=_NetscalerSDWANInstanceEntry_Object((1,3,6,1,4,1,5951,6,3,3,1))
netscalerSDWANInstanceEntry.setIndexNames((0,_A,_j),(0,_A,_k),(0,_A,_l),(0,_A,_m))
if mibBuilder.loadTexts:netscalerSDWANInstanceEntry.setStatus(_B)
_CbIpAddressType_Type=InetAddressType
_CbIpAddressType_Object=MibTableColumn
cbIpAddressType=_CbIpAddressType_Object((1,3,6,1,4,1,5951,6,3,3,1,1),_CbIpAddressType_Type())
cbIpAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cbIpAddressType.setStatus(_B)
_CbIpAddress_Type=InetAddress
_CbIpAddress_Object=MibTableColumn
cbIpAddress=_CbIpAddress_Object((1,3,6,1,4,1,5951,6,3,3,1,2),_CbIpAddress_Type())
cbIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cbIpAddress.setStatus(_B)
_CbHostIPAddressType_Type=InetAddressType
_CbHostIPAddressType_Object=MibTableColumn
cbHostIPAddressType=_CbHostIPAddressType_Object((1,3,6,1,4,1,5951,6,3,3,1,3),_CbHostIPAddressType_Type())
cbHostIPAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cbHostIPAddressType.setStatus(_B)
_CbHostIPAddress_Type=InetAddress
_CbHostIPAddress_Object=MibTableColumn
cbHostIPAddress=_CbHostIPAddress_Object((1,3,6,1,4,1,5951,6,3,3,1,4),_CbHostIPAddress_Type())
cbHostIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cbHostIPAddress.setStatus(_B)
_CbProfileName_Type=OctetString
_CbProfileName_Object=MibTableColumn
cbProfileName=_CbProfileName_Object((1,3,6,1,4,1,5951,6,3,3,1,5),_CbProfileName_Type())
cbProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:cbProfileName.setStatus(_B)
_CbName_Type=OctetString
_CbName_Object=MibTableColumn
cbName=_CbName_Object((1,3,6,1,4,1,5951,6,3,3,1,6),_CbName_Type())
cbName.setMaxAccess(_C)
if mibBuilder.loadTexts:cbName.setStatus(_B)
_CbNetmaskType_Type=InetAddressType
_CbNetmaskType_Object=MibTableColumn
cbNetmaskType=_CbNetmaskType_Object((1,3,6,1,4,1,5951,6,3,3,1,7),_CbNetmaskType_Type())
cbNetmaskType.setMaxAccess(_C)
if mibBuilder.loadTexts:cbNetmaskType.setStatus(_B)
_CbNetmask_Type=InetAddress
_CbNetmask_Object=MibTableColumn
cbNetmask=_CbNetmask_Object((1,3,6,1,4,1,5951,6,3,3,1,8),_CbNetmask_Type())
cbNetmask.setMaxAccess(_C)
if mibBuilder.loadTexts:cbNetmask.setStatus(_B)
_CbGatewayType_Type=InetAddressType
_CbGatewayType_Object=MibTableColumn
cbGatewayType=_CbGatewayType_Object((1,3,6,1,4,1,5951,6,3,3,1,9),_CbGatewayType_Type())
cbGatewayType.setMaxAccess(_C)
if mibBuilder.loadTexts:cbGatewayType.setStatus(_B)
_CbGateway_Type=InetAddress
_CbGateway_Object=MibTableColumn
cbGateway=_CbGateway_Object((1,3,6,1,4,1,5951,6,3,3,1,10),_CbGateway_Type())
cbGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:cbGateway.setStatus(_B)
_CbHostname_Type=OctetString
_CbHostname_Object=MibTableColumn
cbHostname=_CbHostname_Object((1,3,6,1,4,1,5951,6,3,3,1,11),_CbHostname_Type())
cbHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:cbHostname.setStatus(_B)
_CbDescription_Type=OctetString
_CbDescription_Object=MibTableColumn
cbDescription=_CbDescription_Object((1,3,6,1,4,1,5951,6,3,3,1,12),_CbDescription_Type())
cbDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cbDescription.setStatus(_B)
_CbVersion_Type=OctetString
_CbVersion_Object=MibTableColumn
cbVersion=_CbVersion_Object((1,3,6,1,4,1,5951,6,3,3,1,13),_CbVersion_Type())
cbVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cbVersion.setStatus(_B)
_CbInstanceState_Type=OctetString
_CbInstanceState_Object=MibTableColumn
cbInstanceState=_CbInstanceState_Object((1,3,6,1,4,1,5951,6,3,3,1,14),_CbInstanceState_Type())
cbInstanceState.setMaxAccess(_C)
if mibBuilder.loadTexts:cbInstanceState.setStatus(_B)
_CbUuid_Type=OctetString
_CbUuid_Object=MibTableColumn
cbUuid=_CbUuid_Object((1,3,6,1,4,1,5951,6,3,3,1,15),_CbUuid_Type())
cbUuid.setMaxAccess(_C)
if mibBuilder.loadTexts:cbUuid.setStatus(_B)
_CbVirtualFunctions_Type=OctetString
_CbVirtualFunctions_Object=MibTableColumn
cbVirtualFunctions=_CbVirtualFunctions_Object((1,3,6,1,4,1,5951,6,3,3,1,16),_CbVirtualFunctions_Type())
cbVirtualFunctions.setMaxAccess(_C)
if mibBuilder.loadTexts:cbVirtualFunctions.setStatus(_B)
_CbVmState_Type=OctetString
_CbVmState_Object=MibTableColumn
cbVmState=_CbVmState_Object((1,3,6,1,4,1,5951,6,3,3,1,17),_CbVmState_Type())
cbVmState.setMaxAccess(_C)
if mibBuilder.loadTexts:cbVmState.setStatus(_B)
_CbNumberOfCPU_Type=Integer32
_CbNumberOfCPU_Object=MibTableColumn
cbNumberOfCPU=_CbNumberOfCPU_Object((1,3,6,1,4,1,5951,6,3,3,1,18),_CbNumberOfCPU_Type())
cbNumberOfCPU.setMaxAccess(_C)
if mibBuilder.loadTexts:cbNumberOfCPU.setStatus(_B)
_CbVmCPUUsage_Type=OctetString
_CbVmCPUUsage_Object=MibTableColumn
cbVmCPUUsage=_CbVmCPUUsage_Object((1,3,6,1,4,1,5951,6,3,3,1,19),_CbVmCPUUsage_Type())
cbVmCPUUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cbVmCPUUsage.setStatus(_B)
_CbVmMemoryTotal_Type=OctetString
_CbVmMemoryTotal_Object=MibTableColumn
cbVmMemoryTotal=_CbVmMemoryTotal_Object((1,3,6,1,4,1,5951,6,3,3,1,20),_CbVmMemoryTotal_Type())
cbVmMemoryTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cbVmMemoryTotal.setStatus(_B)
_CbVmMemoryFree_Type=OctetString
_CbVmMemoryFree_Object=MibTableColumn
cbVmMemoryFree=_CbVmMemoryFree_Object((1,3,6,1,4,1,5951,6,3,3,1,21),_CbVmMemoryFree_Type())
cbVmMemoryFree.setMaxAccess(_C)
if mibBuilder.loadTexts:cbVmMemoryFree.setStatus(_B)
_CbVmMemoryUsage_Type=OctetString
_CbVmMemoryUsage_Object=MibTableColumn
cbVmMemoryUsage=_CbVmMemoryUsage_Object((1,3,6,1,4,1,5951,6,3,3,1,22),_CbVmMemoryUsage_Type())
cbVmMemoryUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cbVmMemoryUsage.setStatus(_B)
_CbUptime_Type=OctetString
_CbUptime_Object=MibTableColumn
cbUptime=_CbUptime_Object((1,3,6,1,4,1,5951,6,3,3,1,25),_CbUptime_Type())
cbUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:cbUptime.setStatus(_B)
_CbDiskAllocation_Type=OctetString
_CbDiskAllocation_Object=MibTableColumn
cbDiskAllocation=_CbDiskAllocation_Object((1,3,6,1,4,1,5951,6,3,3,1,30),_CbDiskAllocation_Type())
cbDiskAllocation.setMaxAccess(_C)
if mibBuilder.loadTexts:cbDiskAllocation.setStatus(_B)
_CbAPAIPADDRESSType_Type=InetAddressType
_CbAPAIPADDRESSType_Object=MibTableColumn
cbAPAIPADDRESSType=_CbAPAIPADDRESSType_Object((1,3,6,1,4,1,5951,6,3,3,1,47),_CbAPAIPADDRESSType_Type())
cbAPAIPADDRESSType.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAPAIPADDRESSType.setStatus(_B)
_CbAPAIPADDRESS_Type=InetAddress
_CbAPAIPADDRESS_Object=MibTableColumn
cbAPAIPADDRESS=_CbAPAIPADDRESS_Object((1,3,6,1,4,1,5951,6,3,3,1,48),_CbAPAIPADDRESS_Type())
cbAPAIPADDRESS.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAPAIPADDRESS.setStatus(_B)
_CbAPANetMaskType_Type=InetAddressType
_CbAPANetMaskType_Object=MibTableColumn
cbAPANetMaskType=_CbAPANetMaskType_Object((1,3,6,1,4,1,5951,6,3,3,1,49),_CbAPANetMaskType_Type())
cbAPANetMaskType.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAPANetMaskType.setStatus(_B)
_CbAPANetMask_Type=InetAddress
_CbAPANetMask_Object=MibTableColumn
cbAPANetMask=_CbAPANetMask_Object((1,3,6,1,4,1,5951,6,3,3,1,50),_CbAPANetMask_Type())
cbAPANetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAPANetMask.setStatus(_B)
_CbAPAGatewayType_Type=InetAddressType
_CbAPAGatewayType_Object=MibTableColumn
cbAPAGatewayType=_CbAPAGatewayType_Object((1,3,6,1,4,1,5951,6,3,3,1,51),_CbAPAGatewayType_Type())
cbAPAGatewayType.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAPAGatewayType.setStatus(_B)
_CbAPAGateway_Type=InetAddress
_CbAPAGateway_Object=MibTableColumn
cbAPAGateway=_CbAPAGateway_Object((1,3,6,1,4,1,5951,6,3,3,1,52),_CbAPAGateway_Type())
cbAPAGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAPAGateway.setStatus(_B)
_CbPluginIPADDRESSType_Type=InetAddressType
_CbPluginIPADDRESSType_Object=MibTableColumn
cbPluginIPADDRESSType=_CbPluginIPADDRESSType_Object((1,3,6,1,4,1,5951,6,3,3,1,53),_CbPluginIPADDRESSType_Type())
cbPluginIPADDRESSType.setMaxAccess(_C)
if mibBuilder.loadTexts:cbPluginIPADDRESSType.setStatus(_B)
_CbPluginIPADDRESS_Type=InetAddress
_CbPluginIPADDRESS_Object=MibTableColumn
cbPluginIPADDRESS=_CbPluginIPADDRESS_Object((1,3,6,1,4,1,5951,6,3,3,1,54),_CbPluginIPADDRESS_Type())
cbPluginIPADDRESS.setMaxAccess(_C)
if mibBuilder.loadTexts:cbPluginIPADDRESS.setStatus(_B)
_CbMgmtIPAddressType_Type=InetAddressType
_CbMgmtIPAddressType_Object=MibTableColumn
cbMgmtIPAddressType=_CbMgmtIPAddressType_Object((1,3,6,1,4,1,5951,6,3,3,1,57),_CbMgmtIPAddressType_Type())
cbMgmtIPAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cbMgmtIPAddressType.setStatus(_B)
_CbMgmtIPAddress_Type=InetAddress
_CbMgmtIPAddress_Object=MibTableColumn
cbMgmtIPAddress=_CbMgmtIPAddress_Object((1,3,6,1,4,1,5951,6,3,3,1,58),_CbMgmtIPAddress_Type())
cbMgmtIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cbMgmtIPAddress.setStatus(_B)
_NetscalerSDWANAcceleratorTable_Object=MibTable
netscalerSDWANAcceleratorTable=_NetscalerSDWANAcceleratorTable_Object((1,3,6,1,4,1,5951,6,3,4))
if mibBuilder.loadTexts:netscalerSDWANAcceleratorTable.setStatus(_B)
_NetscalerSDWANAcceleratorEntry_Object=MibTableRow
netscalerSDWANAcceleratorEntry=_NetscalerSDWANAcceleratorEntry_Object((1,3,6,1,4,1,5951,6,3,4,1))
netscalerSDWANAcceleratorEntry.setIndexNames((0,_A,_n),(0,_A,_o),(0,_A,_p),(0,_A,_q))
if mibBuilder.loadTexts:netscalerSDWANAcceleratorEntry.setStatus(_B)
_CbAcceleratorIpAddressType_Type=InetAddressType
_CbAcceleratorIpAddressType_Object=MibTableColumn
cbAcceleratorIpAddressType=_CbAcceleratorIpAddressType_Object((1,3,6,1,4,1,5951,6,3,4,1,1),_CbAcceleratorIpAddressType_Type())
cbAcceleratorIpAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAcceleratorIpAddressType.setStatus(_B)
_CbAcceleratorIpAddress_Type=InetAddress
_CbAcceleratorIpAddress_Object=MibTableColumn
cbAcceleratorIpAddress=_CbAcceleratorIpAddress_Object((1,3,6,1,4,1,5951,6,3,4,1,2),_CbAcceleratorIpAddress_Type())
cbAcceleratorIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAcceleratorIpAddress.setStatus(_B)
_CbAcceleratorHostIPAddressType_Type=InetAddressType
_CbAcceleratorHostIPAddressType_Object=MibTableColumn
cbAcceleratorHostIPAddressType=_CbAcceleratorHostIPAddressType_Object((1,3,6,1,4,1,5951,6,3,4,1,3),_CbAcceleratorHostIPAddressType_Type())
cbAcceleratorHostIPAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAcceleratorHostIPAddressType.setStatus(_B)
_CbAcceleratorHostIPAddress_Type=InetAddress
_CbAcceleratorHostIPAddress_Object=MibTableColumn
cbAcceleratorHostIPAddress=_CbAcceleratorHostIPAddress_Object((1,3,6,1,4,1,5951,6,3,4,1,4),_CbAcceleratorHostIPAddress_Type())
cbAcceleratorHostIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAcceleratorHostIPAddress.setStatus(_B)
_CbAcceleratorProfileName_Type=OctetString
_CbAcceleratorProfileName_Object=MibTableColumn
cbAcceleratorProfileName=_CbAcceleratorProfileName_Object((1,3,6,1,4,1,5951,6,3,4,1,5),_CbAcceleratorProfileName_Type())
cbAcceleratorProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAcceleratorProfileName.setStatus(_B)
_CbAcceleratorName_Type=OctetString
_CbAcceleratorName_Object=MibTableColumn
cbAcceleratorName=_CbAcceleratorName_Object((1,3,6,1,4,1,5951,6,3,4,1,6),_CbAcceleratorName_Type())
cbAcceleratorName.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAcceleratorName.setStatus(_B)
_CbAcceleratorNetmaskType_Type=InetAddressType
_CbAcceleratorNetmaskType_Object=MibTableColumn
cbAcceleratorNetmaskType=_CbAcceleratorNetmaskType_Object((1,3,6,1,4,1,5951,6,3,4,1,7),_CbAcceleratorNetmaskType_Type())
cbAcceleratorNetmaskType.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAcceleratorNetmaskType.setStatus(_B)
_CbAcceleratorNetmask_Type=InetAddress
_CbAcceleratorNetmask_Object=MibTableColumn
cbAcceleratorNetmask=_CbAcceleratorNetmask_Object((1,3,6,1,4,1,5951,6,3,4,1,8),_CbAcceleratorNetmask_Type())
cbAcceleratorNetmask.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAcceleratorNetmask.setStatus(_B)
_CbAcceleratorGatewayType_Type=InetAddressType
_CbAcceleratorGatewayType_Object=MibTableColumn
cbAcceleratorGatewayType=_CbAcceleratorGatewayType_Object((1,3,6,1,4,1,5951,6,3,4,1,9),_CbAcceleratorGatewayType_Type())
cbAcceleratorGatewayType.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAcceleratorGatewayType.setStatus(_B)
_CbAcceleratorGateway_Type=InetAddress
_CbAcceleratorGateway_Object=MibTableColumn
cbAcceleratorGateway=_CbAcceleratorGateway_Object((1,3,6,1,4,1,5951,6,3,4,1,10),_CbAcceleratorGateway_Type())
cbAcceleratorGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAcceleratorGateway.setStatus(_B)
_CbAcceleratorHostname_Type=OctetString
_CbAcceleratorHostname_Object=MibTableColumn
cbAcceleratorHostname=_CbAcceleratorHostname_Object((1,3,6,1,4,1,5951,6,3,4,1,11),_CbAcceleratorHostname_Type())
cbAcceleratorHostname.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAcceleratorHostname.setStatus(_B)
_CbAcceleratorDescription_Type=OctetString
_CbAcceleratorDescription_Object=MibTableColumn
cbAcceleratorDescription=_CbAcceleratorDescription_Object((1,3,6,1,4,1,5951,6,3,4,1,12),_CbAcceleratorDescription_Type())
cbAcceleratorDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAcceleratorDescription.setStatus(_B)
_CbAcceleratorVersion_Type=OctetString
_CbAcceleratorVersion_Object=MibTableColumn
cbAcceleratorVersion=_CbAcceleratorVersion_Object((1,3,6,1,4,1,5951,6,3,4,1,13),_CbAcceleratorVersion_Type())
cbAcceleratorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAcceleratorVersion.setStatus(_B)
_CbAcceleratorInstanceState_Type=OctetString
_CbAcceleratorInstanceState_Object=MibTableColumn
cbAcceleratorInstanceState=_CbAcceleratorInstanceState_Object((1,3,6,1,4,1,5951,6,3,4,1,14),_CbAcceleratorInstanceState_Type())
cbAcceleratorInstanceState.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAcceleratorInstanceState.setStatus(_B)
_CbAcceleratorUuid_Type=OctetString
_CbAcceleratorUuid_Object=MibTableColumn
cbAcceleratorUuid=_CbAcceleratorUuid_Object((1,3,6,1,4,1,5951,6,3,4,1,15),_CbAcceleratorUuid_Type())
cbAcceleratorUuid.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAcceleratorUuid.setStatus(_B)
_CbAcceleratorVmState_Type=OctetString
_CbAcceleratorVmState_Object=MibTableColumn
cbAcceleratorVmState=_CbAcceleratorVmState_Object((1,3,6,1,4,1,5951,6,3,4,1,16),_CbAcceleratorVmState_Type())
cbAcceleratorVmState.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAcceleratorVmState.setStatus(_B)
_CbAcceleratorNumberOfCPU_Type=Integer32
_CbAcceleratorNumberOfCPU_Object=MibTableColumn
cbAcceleratorNumberOfCPU=_CbAcceleratorNumberOfCPU_Object((1,3,6,1,4,1,5951,6,3,4,1,17),_CbAcceleratorNumberOfCPU_Type())
cbAcceleratorNumberOfCPU.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAcceleratorNumberOfCPU.setStatus(_B)
_CbAcceleratorVmCPUUsage_Type=OctetString
_CbAcceleratorVmCPUUsage_Object=MibTableColumn
cbAcceleratorVmCPUUsage=_CbAcceleratorVmCPUUsage_Object((1,3,6,1,4,1,5951,6,3,4,1,18),_CbAcceleratorVmCPUUsage_Type())
cbAcceleratorVmCPUUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAcceleratorVmCPUUsage.setStatus(_B)
_CbAcceleratorVmMemoryTotal_Type=OctetString
_CbAcceleratorVmMemoryTotal_Object=MibTableColumn
cbAcceleratorVmMemoryTotal=_CbAcceleratorVmMemoryTotal_Object((1,3,6,1,4,1,5951,6,3,4,1,19),_CbAcceleratorVmMemoryTotal_Type())
cbAcceleratorVmMemoryTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAcceleratorVmMemoryTotal.setStatus(_B)
_CbAcceleratorVmMemoryFree_Type=OctetString
_CbAcceleratorVmMemoryFree_Object=MibTableColumn
cbAcceleratorVmMemoryFree=_CbAcceleratorVmMemoryFree_Object((1,3,6,1,4,1,5951,6,3,4,1,20),_CbAcceleratorVmMemoryFree_Type())
cbAcceleratorVmMemoryFree.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAcceleratorVmMemoryFree.setStatus(_B)
_CbAcceleratorVmMemoryUsage_Type=OctetString
_CbAcceleratorVmMemoryUsage_Object=MibTableColumn
cbAcceleratorVmMemoryUsage=_CbAcceleratorVmMemoryUsage_Object((1,3,6,1,4,1,5951,6,3,4,1,21),_CbAcceleratorVmMemoryUsage_Type())
cbAcceleratorVmMemoryUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAcceleratorVmMemoryUsage.setStatus(_B)
_CbAcceleratorUptime_Type=OctetString
_CbAcceleratorUptime_Object=MibTableColumn
cbAcceleratorUptime=_CbAcceleratorUptime_Object((1,3,6,1,4,1,5951,6,3,4,1,24),_CbAcceleratorUptime_Type())
cbAcceleratorUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAcceleratorUptime.setStatus(_B)
_CbAcceleratorIpList_Type=OctetString
_CbAcceleratorIpList_Object=MibTableColumn
cbAcceleratorIpList=_CbAcceleratorIpList_Object((1,3,6,1,4,1,5951,6,3,4,1,31),_CbAcceleratorIpList_Type())
cbAcceleratorIpList.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAcceleratorIpList.setStatus(_B)
_CbAcceleratorMgmtIPAddressType_Type=InetAddressType
_CbAcceleratorMgmtIPAddressType_Object=MibTableColumn
cbAcceleratorMgmtIPAddressType=_CbAcceleratorMgmtIPAddressType_Object((1,3,6,1,4,1,5951,6,3,4,1,38),_CbAcceleratorMgmtIPAddressType_Type())
cbAcceleratorMgmtIPAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAcceleratorMgmtIPAddressType.setStatus(_B)
_CbAcceleratorMgmtIPAddress_Type=InetAddress
_CbAcceleratorMgmtIPAddress_Object=MibTableColumn
cbAcceleratorMgmtIPAddress=_CbAcceleratorMgmtIPAddress_Object((1,3,6,1,4,1,5951,6,3,4,1,39),_CbAcceleratorMgmtIPAddress_Type())
cbAcceleratorMgmtIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cbAcceleratorMgmtIPAddress.setStatus(_B)
cpuUsageHigh=NotificationType((1,3,6,1,4,1,5951,6,1,2,1))
cpuUsageHigh.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_H),(_A,_I),(_A,_F)))
if mibBuilder.loadTexts:cpuUsageHigh.setStatus(_B)
cpuUsageNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,2))
cpuUsageNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_H),(_A,_I),(_A,_F)))
if mibBuilder.loadTexts:cpuUsageNormal.setStatus(_B)
memoryUsageHigh=NotificationType((1,3,6,1,4,1,5951,6,1,2,3))
memoryUsageHigh.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_H),(_A,_I),(_A,_F)))
if mibBuilder.loadTexts:memoryUsageHigh.setStatus(_B)
memoryUsageNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,4))
memoryUsageNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_H),(_A,_I),(_A,_F)))
if mibBuilder.loadTexts:memoryUsageNormal.setStatus(_B)
xenHttpFailed=NotificationType((1,3,6,1,4,1,5951,6,1,2,5))
xenHttpFailed.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:xenHttpFailed.setStatus(_B)
xenHttpNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,6))
xenHttpNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:xenHttpNormal.setStatus(_B)
xenSshFailed=NotificationType((1,3,6,1,4,1,5951,6,1,2,7))
xenSshFailed.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:xenSshFailed.setStatus(_B)
xenSshNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,8))
xenSshNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:xenSshNormal.setStatus(_B)
xenApiFailed=NotificationType((1,3,6,1,4,1,5951,6,1,2,9))
xenApiFailed.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:xenApiFailed.setStatus(_B)
xenApiNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,10))
xenApiNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:xenApiNormal.setStatus(_B)
xenPingFailed=NotificationType((1,3,6,1,4,1,5951,6,1,2,11))
xenPingFailed.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:xenPingFailed.setStatus(_B)
xenPingNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,12))
xenPingNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:xenPingNormal.setStatus(_B)
ipmiStateError=NotificationType((1,3,6,1,4,1,5951,6,1,2,13))
ipmiStateError.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:ipmiStateError.setStatus(_B)
ipmiStateNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,14))
ipmiStateNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:ipmiStateNormal.setStatus(_B)
bmcFirmwareVersionError=NotificationType((1,3,6,1,4,1,5951,6,1,2,15))
bmcFirmwareVersionError.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:bmcFirmwareVersionError.setStatus(_B)
bmcFirmwareVersionNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,16))
bmcFirmwareVersionNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:bmcFirmwareVersionNormal.setStatus(_B)
resourceStateError=NotificationType((1,3,6,1,4,1,5951,6,1,2,17))
resourceStateError.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:resourceStateError.setStatus(_B)
resourceStateNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,18))
resourceStateNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:resourceStateNormal.setStatus(_B)
fanSpeedError=NotificationType((1,3,6,1,4,1,5951,6,1,2,19))
fanSpeedError.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_H),(_A,_F)))
if mibBuilder.loadTexts:fanSpeedError.setStatus(_B)
fanSpeedNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,20))
fanSpeedNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_H),(_A,_F)))
if mibBuilder.loadTexts:fanSpeedNormal.setStatus(_B)
cpuTempError=NotificationType((1,3,6,1,4,1,5951,6,1,2,21))
cpuTempError.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_H),(_A,_F)))
if mibBuilder.loadTexts:cpuTempError.setStatus(_B)
cpuTempNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,22))
cpuTempNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_H),(_A,_F)))
if mibBuilder.loadTexts:cpuTempNormal.setStatus(_B)
systemTempError=NotificationType((1,3,6,1,4,1,5951,6,1,2,23))
systemTempError.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_H),(_A,_F)))
if mibBuilder.loadTexts:systemTempError.setStatus(_B)
systemTempNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,24))
systemTempNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_H),(_A,_F)))
if mibBuilder.loadTexts:systemTempNormal.setStatus(_B)
voltageError=NotificationType((1,3,6,1,4,1,5951,6,1,2,25))
voltageError.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_H),(_A,_F)))
if mibBuilder.loadTexts:voltageError.setStatus(_B)
voltageNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,26))
voltageNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_H),(_A,_F)))
if mibBuilder.loadTexts:voltageNormal.setStatus(_B)
powerSupplyFailed=NotificationType((1,3,6,1,4,1,5951,6,1,2,27))
powerSupplyFailed.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:powerSupplyFailed.setStatus(_B)
powerSupplyNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,28))
powerSupplyNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:powerSupplyNormal.setStatus(_B)
healthCounterError=NotificationType((1,3,6,1,4,1,5951,6,1,2,31))
healthCounterError.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_H),(_A,_F)))
if mibBuilder.loadTexts:healthCounterError.setStatus(_B)
healthCounterNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,32))
healthCounterNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_H),(_A,_F)))
if mibBuilder.loadTexts:healthCounterNormal.setStatus(_B)
interfaceDown=NotificationType((1,3,6,1,4,1,5951,6,1,2,33))
interfaceDown.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:interfaceDown.setStatus(_B)
interfaceUp=NotificationType((1,3,6,1,4,1,5951,6,1,2,34))
interfaceUp.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:interfaceUp.setStatus(_B)
diskUtilizationHigh=NotificationType((1,3,6,1,4,1,5951,6,1,2,35))
diskUtilizationHigh.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_H),(_A,_I),(_A,_F)))
if mibBuilder.loadTexts:diskUtilizationHigh.setStatus(_B)
diskUtilizationNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,36))
diskUtilizationNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_H),(_A,_I),(_A,_F)))
if mibBuilder.loadTexts:diskUtilizationNormal.setStatus(_B)
srStatusError=NotificationType((1,3,6,1,4,1,5951,6,1,2,37))
srStatusError.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:srStatusError.setStatus(_B)
srStatusNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,38))
srStatusNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:srStatusNormal.setStatus(_B)
subSystemDown=NotificationType((1,3,6,1,4,1,5951,6,1,2,43))
subSystemDown.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:subSystemDown.setStatus(_B)
subSystemUp=NotificationType((1,3,6,1,4,1,5951,6,1,2,44))
subSystemUp.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:subSystemUp.setStatus(_B)
subSystemFailed=NotificationType((1,3,6,1,4,1,5951,6,1,2,45))
subSystemFailed.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:subSystemFailed.setStatus(_B)
mpsDown=NotificationType((1,3,6,1,4,1,5951,6,1,2,46))
mpsDown.setObjects(*((_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:mpsDown.setStatus(_B)
mpsUp=NotificationType((1,3,6,1,4,1,5951,6,1,2,47))
mpsUp.setObjects(*((_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:mpsUp.setStatus(_B)
passwordRecoveryFailed=NotificationType((1,3,6,1,4,1,5951,6,1,2,48))
passwordRecoveryFailed.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:passwordRecoveryFailed.setStatus(_B)
passwordRecoverySuccess=NotificationType((1,3,6,1,4,1,5951,6,1,2,49))
passwordRecoverySuccess.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:passwordRecoverySuccess.setStatus(_B)
deviceAdded=NotificationType((1,3,6,1,4,1,5951,6,1,2,50))
deviceAdded.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:deviceAdded.setStatus(_B)
deviceRemoved=NotificationType((1,3,6,1,4,1,5951,6,1,2,51))
deviceRemoved.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:deviceRemoved.setStatus(_B)
deviceModified=NotificationType((1,3,6,1,4,1,5951,6,1,2,52))
deviceModified.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:deviceModified.setStatus(_B)
devicePowerStateChanged=NotificationType((1,3,6,1,4,1,5951,6,1,2,53))
devicePowerStateChanged.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:devicePowerStateChanged.setStatus(_B)
deviceStateChanged=NotificationType((1,3,6,1,4,1,5951,6,1,2,54))
deviceStateChanged.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:deviceStateChanged.setStatus(_B)
deviceBootFailed=NotificationType((1,3,6,1,4,1,5951,6,1,2,55))
deviceBootFailed.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:deviceBootFailed.setStatus(_B)
deviceRebootFailed=NotificationType((1,3,6,1,4,1,5951,6,1,2,56))
deviceRebootFailed.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:deviceRebootFailed.setStatus(_B)
backupFailed=NotificationType((1,3,6,1,4,1,5951,6,1,2,58))
backupFailed.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:backupFailed.setStatus(_B)
networkConfigChanged=NotificationType((1,3,6,1,4,1,5951,6,1,2,62))
networkConfigChanged.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:networkConfigChanged.setStatus(_B)
loginFailure=NotificationType((1,3,6,1,4,1,5951,6,1,2,71))
loginFailure.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:loginFailure.setStatus(_B)
inventoryFailed=NotificationType((1,3,6,1,4,1,5951,6,1,2,72))
inventoryFailed.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:inventoryFailed.setStatus(_B)
healthMonitorPluginError=NotificationType((1,3,6,1,4,1,5951,6,1,2,73))
healthMonitorPluginError.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:healthMonitorPluginError.setStatus(_B)
healthMonitorPluginNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,74))
healthMonitorPluginNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E)))
if mibBuilder.loadTexts:healthMonitorPluginNormal.setStatus(_B)
versionMatrixMisMatch=NotificationType((1,3,6,1,4,1,5951,6,1,2,75))
versionMatrixMisMatch.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:versionMatrixMisMatch.setStatus(_B)
logicalDriveFailed=NotificationType((1,3,6,1,4,1,5951,6,1,2,76))
logicalDriveFailed.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_H),(_A,_F)))
if mibBuilder.loadTexts:logicalDriveFailed.setStatus(_B)
physicalDriveFailed=NotificationType((1,3,6,1,4,1,5951,6,1,2,77))
physicalDriveFailed.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_H),(_A,_F)))
if mibBuilder.loadTexts:physicalDriveFailed.setStatus(_B)
trapConfigFailure=NotificationType((1,3,6,1,4,1,5951,6,1,2,78))
trapConfigFailure.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:trapConfigFailure.setStatus(_B)
pooledLicenseGrace=NotificationType((1,3,6,1,4,1,5951,6,1,2,80))
pooledLicenseGrace.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:pooledLicenseGrace.setStatus(_B)
pooledLicenseGraceNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,81))
pooledLicenseGraceNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:pooledLicenseGraceNormal.setStatus(_B)
pooledLicenseCapacityPartial=NotificationType((1,3,6,1,4,1,5951,6,1,2,82))
pooledLicenseCapacityPartial.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:pooledLicenseCapacityPartial.setStatus(_B)
pooledLicenseCapacityNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,83))
pooledLicenseCapacityNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:pooledLicenseCapacityNormal.setStatus(_B)
sslCertThresholdBreached=NotificationType((1,3,6,1,4,1,5951,6,1,2,96))
sslCertThresholdBreached.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:sslCertThresholdBreached.setStatus(_B)
sslCertThresholdNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,97))
sslCertThresholdNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:sslCertThresholdNormal.setStatus(_B)
inventoryUp=NotificationType((1,3,6,1,4,1,5951,6,1,2,101))
inventoryUp.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:inventoryUp.setStatus(_B)
logicalDriveNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,102))
logicalDriveNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_H),(_A,_F)))
if mibBuilder.loadTexts:logicalDriveNormal.setStatus(_B)
physicalDriveNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,103))
physicalDriveNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_H),(_A,_F)))
if mibBuilder.loadTexts:physicalDriveNormal.setStatus(_B)
deviceBooted=NotificationType((1,3,6,1,4,1,5951,6,1,2,104))
deviceBooted.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:deviceBooted.setStatus(_B)
deviceRebooted=NotificationType((1,3,6,1,4,1,5951,6,1,2,105))
deviceRebooted.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:deviceRebooted.setStatus(_B)
hsmStateError=NotificationType((1,3,6,1,4,1,5951,6,1,2,145))
hsmStateError.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:hsmStateError.setStatus(_B)
hsmStateNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,146))
hsmStateNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:hsmStateNormal.setStatus(_B)
sdxVersionMismatchError=NotificationType((1,3,6,1,4,1,5951,6,1,2,147))
sdxVersionMismatchError.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:sdxVersionMismatchError.setStatus(_B)
sdxVersionMismatchNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,148))
sdxVersionMismatchNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:sdxVersionMismatchNormal.setStatus(_B)
HypervisorDiskUtilizationHigh=NotificationType((1,3,6,1,4,1,5951,6,1,2,149))
HypervisorDiskUtilizationHigh.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_H),(_A,_I),(_A,_F)))
if mibBuilder.loadTexts:HypervisorDiskUtilizationHigh.setStatus(_B)
HypervisorDiskUtilizationNormal=NotificationType((1,3,6,1,4,1,5951,6,1,2,150))
HypervisorDiskUtilizationNormal.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_H),(_A,_I),(_A,_F)))
if mibBuilder.loadTexts:HypervisorDiskUtilizationNormal.setStatus(_B)
pooledLicenseGraceCritical=NotificationType((1,3,6,1,4,1,5951,6,1,2,151))
pooledLicenseGraceCritical.setObjects(*((_A,_D),(_A,_G),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:pooledLicenseGraceCritical.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'netScaler':netScaler,'sdxRoot':sdxRoot,'sdxEventGroup':sdxEventGroup,'eventVarBindOids':eventVarBindOids,_D:source,_G:entityName,'entityType':entityType,_E:eventMessage,_I:thresholdValue,_H:currentValue,_F:severity,'mpsEvents':mpsEvents,'cpuUsageHigh':cpuUsageHigh,'cpuUsageNormal':cpuUsageNormal,'memoryUsageHigh':memoryUsageHigh,'memoryUsageNormal':memoryUsageNormal,'xenHttpFailed':xenHttpFailed,'xenHttpNormal':xenHttpNormal,'xenSshFailed':xenSshFailed,'xenSshNormal':xenSshNormal,'xenApiFailed':xenApiFailed,'xenApiNormal':xenApiNormal,'xenPingFailed':xenPingFailed,'xenPingNormal':xenPingNormal,'ipmiStateError':ipmiStateError,'ipmiStateNormal':ipmiStateNormal,'bmcFirmwareVersionError':bmcFirmwareVersionError,'bmcFirmwareVersionNormal':bmcFirmwareVersionNormal,'resourceStateError':resourceStateError,'resourceStateNormal':resourceStateNormal,'fanSpeedError':fanSpeedError,'fanSpeedNormal':fanSpeedNormal,'cpuTempError':cpuTempError,'cpuTempNormal':cpuTempNormal,'systemTempError':systemTempError,'systemTempNormal':systemTempNormal,'voltageError':voltageError,'voltageNormal':voltageNormal,'powerSupplyFailed':powerSupplyFailed,'powerSupplyNormal':powerSupplyNormal,'healthCounterError':healthCounterError,'healthCounterNormal':healthCounterNormal,'interfaceDown':interfaceDown,'interfaceUp':interfaceUp,'diskUtilizationHigh':diskUtilizationHigh,'diskUtilizationNormal':diskUtilizationNormal,'srStatusError':srStatusError,'srStatusNormal':srStatusNormal,'subSystemDown':subSystemDown,'subSystemUp':subSystemUp,'subSystemFailed':subSystemFailed,'mpsDown':mpsDown,'mpsUp':mpsUp,'passwordRecoveryFailed':passwordRecoveryFailed,'passwordRecoverySuccess':passwordRecoverySuccess,'deviceAdded':deviceAdded,'deviceRemoved':deviceRemoved,'deviceModified':deviceModified,'devicePowerStateChanged':devicePowerStateChanged,'deviceStateChanged':deviceStateChanged,'deviceBootFailed':deviceBootFailed,'deviceRebootFailed':deviceRebootFailed,'backupFailed':backupFailed,'networkConfigChanged':networkConfigChanged,'loginFailure':loginFailure,'inventoryFailed':inventoryFailed,'healthMonitorPluginError':healthMonitorPluginError,'healthMonitorPluginNormal':healthMonitorPluginNormal,'versionMatrixMisMatch':versionMatrixMisMatch,'logicalDriveFailed':logicalDriveFailed,'physicalDriveFailed':physicalDriveFailed,'trapConfigFailure':trapConfigFailure,'pooledLicenseGrace':pooledLicenseGrace,'pooledLicenseGraceNormal':pooledLicenseGraceNormal,'pooledLicenseCapacityPartial':pooledLicenseCapacityPartial,'pooledLicenseCapacityNormal':pooledLicenseCapacityNormal,'sslCertThresholdBreached':sslCertThresholdBreached,'sslCertThresholdNormal':sslCertThresholdNormal,'inventoryUp':inventoryUp,'logicalDriveNormal':logicalDriveNormal,'physicalDriveNormal':physicalDriveNormal,'deviceBooted':deviceBooted,'deviceRebooted':deviceRebooted,'hsmStateError':hsmStateError,'hsmStateNormal':hsmStateNormal,'sdxVersionMismatchError':sdxVersionMismatchError,'sdxVersionMismatchNormal':sdxVersionMismatchNormal,'HypervisorDiskUtilizationHigh':HypervisorDiskUtilizationHigh,'HypervisorDiskUtilizationNormal':HypervisorDiskUtilizationNormal,'pooledLicenseGraceCritical':pooledLicenseGraceCritical,'systemGroup':systemGroup,'systemPlatform':systemPlatform,'systemProduct':systemProduct,'systemBuildNumber':systemBuildNumber,'systemSvmIPAddressType':systemSvmIPAddressType,'systemSvmIPAddress':systemSvmIPAddress,'systemXenIPAddressType':systemXenIPAddressType,'systemXenIPAddress':systemXenIPAddress,'systemNetmaskType':systemNetmaskType,'systemNetmask':systemNetmask,'systemGatewayType':systemGatewayType,'systemGateway':systemGateway,'systemNetworkInterface':systemNetworkInterface,'systemDns':systemDns,'systemSysId':systemSysId,'systemSerial':systemSerial,'systemCurrentTime':systemCurrentTime,'systemUptime':systemUptime,'systemBiosVersion':systemBiosVersion,'systemMaxThroughput':systemMaxThroughput,'systemAvailableThroughput':systemAvailableThroughput,'systemHostId':systemHostId,'systemCustomID':systemCustomID,'systemCpuUsage':systemCpuUsage,'systemMemoryUsage':systemMemoryUsage,'systemDiskUsage':systemDiskUsage,'sysHealthGroup':sysHealthGroup,'hardwareResourceTable':hardwareResourceTable,'hardwareResourceEntry':hardwareResourceEntry,_K:hardwareResourceName,_L:hardwareResourceHostIPAddressType,_M:hardwareResourceHostIPAddress,'hardwareResourceCurrentValue':hardwareResourceCurrentValue,'hardwareResourceExpectedValue':hardwareResourceExpectedValue,'hardwareResourceUnit':hardwareResourceUnit,'hardwareResourceStatus':hardwareResourceStatus,'softwareResourceTable':softwareResourceTable,'softwareResourceEntry':softwareResourceEntry,_N:softwareResourceName,_O:softwareResourceHostIPAddressType,_P:softwareResourceHostIPAddress,'softwareResourceCurrentValue':softwareResourceCurrentValue,'softwareResourceExpectedValue':softwareResourceExpectedValue,'softwareResourceUnit':softwareResourceUnit,'softwareResourceStatus':softwareResourceStatus,'diskTable':diskTable,'diskEntry':diskEntry,_Q:diskName,_R:diskHostIPAddressType,_S:diskHostIPAddress,'diskTransactionRate':diskTransactionRate,'diskBlockReadRate':diskBlockReadRate,'diskBlockWriteRate':diskBlockWriteRate,'diskTotalBlocksRead':diskTotalBlocksRead,'diskTotalBlocksWritten':diskTotalBlocksWritten,'diskUtilized':diskUtilized,'diskSize':diskSize,'diskBayNumber':diskBayNumber,'srTable':srTable,'srEntry':srEntry,_T:srName,_U:srBayNumber,_V:srHostIPAddressType,_W:srHostIPAddress,'srUtilized':srUtilized,'srSize':srSize,'srStatus':srStatus,'interfaceTable':interfaceTable,'interfaceEntry':interfaceEntry,'interfacePort':interfacePort,_Y:interfaceHostIPAddressType,_Z:interfaceHostIPAddress,'interfaceState':interfaceState,'interfaceRxPackets':interfaceRxPackets,'interfaceTxPackets':interfaceTxPackets,'interfaceRxBytes':interfaceRxBytes,'interfaceTxBytes':interfaceTxBytes,'interfaceRxErrors':interfaceRxErrors,'interfaceTxErrors':interfaceTxErrors,'interfaceVfTotal':interfaceVfTotal,'interfaceVfAssigned':interfaceVfAssigned,_X:interfaceMappedPort,'healthMonitoringTable':healthMonitoringTable,'healthMonitoringEntry':healthMonitoringEntry,_a:hmName,_b:hmHostIPAddressType,_c:hmHostIPAddress,'hmStatus':hmStatus,'hmNoOfFailures':hmNoOfFailures,'hmUnit':hmUnit,'hmCurrentValue':hmCurrentValue,'deviceGroup':deviceGroup,'xenTable':xenTable,'xenEntry':xenEntry,_d:xenIpAddressType,_e:xenIpAddress,'xenHostname':xenHostname,'xenDescription':xenDescription,'xenVersion':xenVersion,'xenUuid':xenUuid,'xenNumberOfCPU':xenNumberOfCPU,'xenCpuUsage':xenCpuUsage,'xenMemoryTotal':xenMemoryTotal,'xenMemoryFree':xenMemoryFree,'xenMemoryUsage':xenMemoryUsage,'xenTx':xenTx,'xenRx':xenRx,'xenUptime':xenUptime,'xenSslCoresTotal':xenSslCoresTotal,'xenIscsiIQN':xenIscsiIQN,'xenEdition':xenEdition,'xenExpiry':xenExpiry,'xenProductCode':xenProductCode,'xenSerialNumber':xenSerialNumber,'xenVersionLong':xenVersionLong,'xenVersionShort':xenVersionShort,'xenBuildNumber':xenBuildNumber,'xenBuildDate':xenBuildDate,'xenNumberOfCPUCores':xenNumberOfCPUCores,'netscalerTable':netscalerTable,'netscalerEntry':netscalerEntry,_f:nsIpAddressType,_g:nsIpAddress,_h:nsHostIPAddressType,_i:nsHostIPAddress,'nsProfileName':nsProfileName,'nsName':nsName,'nsNetmaskType':nsNetmaskType,'nsNetmask':nsNetmask,'nsGatewayType':nsGatewayType,'nsGateway':nsGateway,'nsHostname':nsHostname,'nsDescription':nsDescription,'nsVersion':nsVersion,'nsUuid':nsUuid,'nsInstanceState':nsInstanceState,'nsVirtualFunctions':nsVirtualFunctions,'nsSslVirtualFunctions':nsSslVirtualFunctions,'nsVmState':nsVmState,'nsNumberOfCPU':nsNumberOfCPU,'nsVmMemoryTotal':nsVmMemoryTotal,'nsUptime':nsUptime,'nsNumberOfSSLCores':nsNumberOfSSLCores,'nsCpuCoreMgmt':nsCpuCoreMgmt,'nsCpuCorePE':nsCpuCorePE,'nsVmDescription':nsVmDescription,'nsThroughput':nsThroughput,'nsNumberOfCores':nsNumberOfCores,'nsNsCPUUsage':nsNsCPUUsage,'nsNsMemoryUsage':nsNsMemoryUsage,'nsNsTx':nsNsTx,'nsNsRx':nsNsRx,'nsHttpReq':nsHttpReq,'nsUpsince':nsUpsince,'nsLicense':nsLicense,'nsHaMasterState':nsHaMasterState,'nsHaIPAddressType':nsHaIPAddressType,'nsHaIPAddress':nsHaIPAddress,'nsNodeState':nsNodeState,'nsHaSync':nsHaSync,'nsPps':nsPps,'nsNumberOfSslCoresUp':nsNumberOfSslCoresUp,'nsIfOby1':nsIfOby1,'nsIf0by2':nsIf0by2,'nsNsVLANId':nsNsVLANId,'nsNsVLANTagged':nsNsVLANTagged,'nsVlanType':nsVlanType,'netscalerSDWANInstanceTable':netscalerSDWANInstanceTable,'netscalerSDWANInstanceEntry':netscalerSDWANInstanceEntry,_j:cbIpAddressType,_k:cbIpAddress,_l:cbHostIPAddressType,_m:cbHostIPAddress,'cbProfileName':cbProfileName,'cbName':cbName,'cbNetmaskType':cbNetmaskType,'cbNetmask':cbNetmask,'cbGatewayType':cbGatewayType,'cbGateway':cbGateway,'cbHostname':cbHostname,'cbDescription':cbDescription,'cbVersion':cbVersion,'cbInstanceState':cbInstanceState,'cbUuid':cbUuid,'cbVirtualFunctions':cbVirtualFunctions,'cbVmState':cbVmState,'cbNumberOfCPU':cbNumberOfCPU,'cbVmCPUUsage':cbVmCPUUsage,'cbVmMemoryTotal':cbVmMemoryTotal,'cbVmMemoryFree':cbVmMemoryFree,'cbVmMemoryUsage':cbVmMemoryUsage,'cbUptime':cbUptime,'cbDiskAllocation':cbDiskAllocation,'cbAPAIPADDRESSType':cbAPAIPADDRESSType,'cbAPAIPADDRESS':cbAPAIPADDRESS,'cbAPANetMaskType':cbAPANetMaskType,'cbAPANetMask':cbAPANetMask,'cbAPAGatewayType':cbAPAGatewayType,'cbAPAGateway':cbAPAGateway,'cbPluginIPADDRESSType':cbPluginIPADDRESSType,'cbPluginIPADDRESS':cbPluginIPADDRESS,'cbMgmtIPAddressType':cbMgmtIPAddressType,'cbMgmtIPAddress':cbMgmtIPAddress,'netscalerSDWANAcceleratorTable':netscalerSDWANAcceleratorTable,'netscalerSDWANAcceleratorEntry':netscalerSDWANAcceleratorEntry,_n:cbAcceleratorIpAddressType,_o:cbAcceleratorIpAddress,_p:cbAcceleratorHostIPAddressType,_q:cbAcceleratorHostIPAddress,'cbAcceleratorProfileName':cbAcceleratorProfileName,'cbAcceleratorName':cbAcceleratorName,'cbAcceleratorNetmaskType':cbAcceleratorNetmaskType,'cbAcceleratorNetmask':cbAcceleratorNetmask,'cbAcceleratorGatewayType':cbAcceleratorGatewayType,'cbAcceleratorGateway':cbAcceleratorGateway,'cbAcceleratorHostname':cbAcceleratorHostname,'cbAcceleratorDescription':cbAcceleratorDescription,'cbAcceleratorVersion':cbAcceleratorVersion,'cbAcceleratorInstanceState':cbAcceleratorInstanceState,'cbAcceleratorUuid':cbAcceleratorUuid,'cbAcceleratorVmState':cbAcceleratorVmState,'cbAcceleratorNumberOfCPU':cbAcceleratorNumberOfCPU,'cbAcceleratorVmCPUUsage':cbAcceleratorVmCPUUsage,'cbAcceleratorVmMemoryTotal':cbAcceleratorVmMemoryTotal,'cbAcceleratorVmMemoryFree':cbAcceleratorVmMemoryFree,'cbAcceleratorVmMemoryUsage':cbAcceleratorVmMemoryUsage,'cbAcceleratorUptime':cbAcceleratorUptime,'cbAcceleratorIpList':cbAcceleratorIpList,'cbAcceleratorMgmtIPAddressType':cbAcceleratorMgmtIPAddressType,'cbAcceleratorMgmtIPAddress':cbAcceleratorMgmtIPAddress})