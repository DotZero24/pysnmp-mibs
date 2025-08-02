_Y='portCarPort'
_X='snmpRemoteEngineID'
_W='snmpPrivateNotifyType'
_V='snmpComm2ViewIndex'
_U='musrIndex'
_T='controlTeminal'
_S='controlIpMask'
_R='controlIpAddress'
_Q='saveFailed'
_P='saveInProgress'
_O='sysIfManageVLANVid'
_N='mandatory'
_M='SnmpAdminString'
_L='OctetString'
_K='noop'
_J='read-create'
_I='not-accessible'
_H='disable'
_G='enable'
_F='QTECH-GBNPlatformOAM-MIB'
_E='read-only'
_D='DisplayString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PortList,dot1qStaticMulticastEntry=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','dot1qStaticMulticastEntry')
gbnPlatform,=mibBuilder.importSymbols('QTECH-MASTER-MIB','gbnPlatform')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
gbnPlatformOAM=ModuleIdentity((1,3,6,1,4,1,27514,1,2,1,1))
if mibBuilder.loadTexts:gbnPlatformOAM.setRevisions(('1900-11-02 00:00',))
_GbnPlatformOAMSysIf_ObjectIdentity=ObjectIdentity
gbnPlatformOAMSysIf=_GbnPlatformOAMSysIf_ObjectIdentity((1,3,6,1,4,1,27514,1,2,1,1,1))
_SysIfMACAddr_Type=MacAddress
_SysIfMACAddr_Object=MibScalar
sysIfMACAddr=_SysIfMACAddr_Object((1,3,6,1,4,1,27514,1,2,1,1,1,1),_SysIfMACAddr_Type())
sysIfMACAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:sysIfMACAddr.setStatus(_A)
_SysIfIpAddress_Type=IpAddress
_SysIfIpAddress_Object=MibScalar
sysIfIpAddress=_SysIfIpAddress_Object((1,3,6,1,4,1,27514,1,2,1,1,1,2),_SysIfIpAddress_Type())
sysIfIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sysIfIpAddress.setStatus(_A)
_SysIfIPGateAddress_Type=IpAddress
_SysIfIPGateAddress_Object=MibScalar
sysIfIPGateAddress=_SysIfIPGateAddress_Object((1,3,6,1,4,1,27514,1,2,1,1,1,3),_SysIfIPGateAddress_Type())
sysIfIPGateAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:sysIfIPGateAddress.setStatus(_A)
_SysIfIPNetMask_Type=IpAddress
_SysIfIPNetMask_Object=MibScalar
sysIfIPNetMask=_SysIfIPNetMask_Object((1,3,6,1,4,1,27514,1,2,1,1,1,4),_SysIfIPNetMask_Type())
sysIfIPNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:sysIfIPNetMask.setStatus(_A)
class _SysIfIPStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('notModified',1),('modified',2),('restore',3),('apply',4)))
_SysIfIPStatus_Type.__name__=_C
_SysIfIPStatus_Object=MibScalar
sysIfIPStatus=_SysIfIPStatus_Object((1,3,6,1,4,1,27514,1,2,1,1,1,5),_SysIfIPStatus_Type())
sysIfIPStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sysIfIPStatus.setStatus(_A)
class _SysIfBOOTPOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SysIfBOOTPOnOff_Type.__name__=_C
_SysIfBOOTPOnOff_Object=MibScalar
sysIfBOOTPOnOff=_SysIfBOOTPOnOff_Object((1,3,6,1,4,1,27514,1,2,1,1,1,7),_SysIfBOOTPOnOff_Type())
sysIfBOOTPOnOff.setMaxAccess(_B)
if mibBuilder.loadTexts:sysIfBOOTPOnOff.setStatus(_A)
class _SysIfDHCPOnOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SysIfDHCPOnOff_Type.__name__=_C
_SysIfDHCPOnOff_Object=MibScalar
sysIfDHCPOnOff=_SysIfDHCPOnOff_Object((1,3,6,1,4,1,27514,1,2,1,1,1,8),_SysIfDHCPOnOff_Type())
sysIfDHCPOnOff.setMaxAccess(_B)
if mibBuilder.loadTexts:sysIfDHCPOnOff.setStatus(_A)
_SysIfManageVLANTbale_Object=MibTable
sysIfManageVLANTbale=_SysIfManageVLANTbale_Object((1,3,6,1,4,1,27514,1,2,1,1,1,9))
if mibBuilder.loadTexts:sysIfManageVLANTbale.setStatus(_N)
_SysIfManageVLANEntry_Object=MibTableRow
sysIfManageVLANEntry=_SysIfManageVLANEntry_Object((1,3,6,1,4,1,27514,1,2,1,1,1,9,1))
sysIfManageVLANEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:sysIfManageVLANEntry.setStatus(_N)
_SysIfManageVLANVid_Type=Integer32
_SysIfManageVLANVid_Object=MibTableColumn
sysIfManageVLANVid=_SysIfManageVLANVid_Object((1,3,6,1,4,1,27514,1,2,1,1,1,9,1,1),_SysIfManageVLANVid_Type())
sysIfManageVLANVid.setMaxAccess(_E)
if mibBuilder.loadTexts:sysIfManageVLANVid.setStatus(_A)
_SysIfManageVLANRowStatus_Type=RowStatus
_SysIfManageVLANRowStatus_Object=MibTableColumn
sysIfManageVLANRowStatus=_SysIfManageVLANRowStatus_Object((1,3,6,1,4,1,27514,1,2,1,1,1,9,1,2),_SysIfManageVLANRowStatus_Type())
sysIfManageVLANRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sysIfManageVLANRowStatus.setStatus(_A)
_GbnPlatformOAMSystem_ObjectIdentity=ObjectIdentity
gbnPlatformOAMSystem=_GbnPlatformOAMSystem_ObjectIdentity((1,3,6,1,4,1,27514,1,2,1,1,2))
class _SoftwarePlate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_SoftwarePlate_Type.__name__=_D
_SoftwarePlate_Object=MibScalar
softwarePlate=_SoftwarePlate_Object((1,3,6,1,4,1,27514,1,2,1,1,2,1),_SoftwarePlate_Type())
softwarePlate.setMaxAccess(_E)
if mibBuilder.loadTexts:softwarePlate.setStatus(_A)
class _SoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_SoftwareVersion_Type.__name__=_D
_SoftwareVersion_Object=MibScalar
softwareVersion=_SoftwareVersion_Object((1,3,6,1,4,1,27514,1,2,1,1,2,2),_SoftwareVersion_Type())
softwareVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:softwareVersion.setStatus(_A)
class _SoftwareCompliedTimeE_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_SoftwareCompliedTimeE_Type.__name__=_D
_SoftwareCompliedTimeE_Object=MibScalar
softwareCompliedTimeE=_SoftwareCompliedTimeE_Object((1,3,6,1,4,1,27514,1,2,1,1,2,3),_SoftwareCompliedTimeE_Type())
softwareCompliedTimeE.setMaxAccess(_E)
if mibBuilder.loadTexts:softwareCompliedTimeE.setStatus(_A)
class _SoftwareCompliedTimeC_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_SoftwareCompliedTimeC_Type.__name__=_D
_SoftwareCompliedTimeC_Object=MibScalar
softwareCompliedTimeC=_SoftwareCompliedTimeC_Object((1,3,6,1,4,1,27514,1,2,1,1,2,4),_SoftwareCompliedTimeC_Type())
softwareCompliedTimeC.setMaxAccess(_E)
if mibBuilder.loadTexts:softwareCompliedTimeC.setStatus(_A)
class _CpuDescrition_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_CpuDescrition_Type.__name__=_D
_CpuDescrition_Object=MibScalar
cpuDescrition=_CpuDescrition_Object((1,3,6,1,4,1,27514,1,2,1,1,2,5),_CpuDescrition_Type())
cpuDescrition.setMaxAccess(_E)
if mibBuilder.loadTexts:cpuDescrition.setStatus(_A)
class _SdramDescrition_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_SdramDescrition_Type.__name__=_D
_SdramDescrition_Object=MibScalar
sdramDescrition=_SdramDescrition_Object((1,3,6,1,4,1,27514,1,2,1,1,2,6),_SdramDescrition_Type())
sdramDescrition.setMaxAccess(_E)
if mibBuilder.loadTexts:sdramDescrition.setStatus(_A)
class _FlashDescrition_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_FlashDescrition_Type.__name__=_D
_FlashDescrition_Object=MibScalar
flashDescrition=_FlashDescrition_Object((1,3,6,1,4,1,27514,1,2,1,1,2,7),_FlashDescrition_Type())
flashDescrition.setMaxAccess(_E)
if mibBuilder.loadTexts:flashDescrition.setStatus(_A)
class _HardwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_HardwareVersion_Type.__name__=_D
_HardwareVersion_Object=MibScalar
hardwareVersion=_HardwareVersion_Object((1,3,6,1,4,1,27514,1,2,1,1,2,8),_HardwareVersion_Type())
hardwareVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:hardwareVersion.setStatus(_A)
class _BootromVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_BootromVersion_Type.__name__=_D
_BootromVersion_Object=MibScalar
bootromVersion=_BootromVersion_Object((1,3,6,1,4,1,27514,1,2,1,1,2,9),_BootromVersion_Type())
bootromVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:bootromVersion.setStatus(_A)
class _HostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HostName_Type.__name__=_D
_HostName_Object=MibScalar
hostName=_HostName_Object((1,3,6,1,4,1,27514,1,2,1,1,2,10),_HostName_Type())
hostName.setMaxAccess(_B)
if mibBuilder.loadTexts:hostName.setStatus(_A)
class _CpuIdle_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CpuIdle_Type.__name__=_C
_CpuIdle_Object=MibScalar
cpuIdle=_CpuIdle_Object((1,3,6,1,4,1,27514,1,2,1,1,2,11),_CpuIdle_Type())
cpuIdle.setMaxAccess(_E)
if mibBuilder.loadTexts:cpuIdle.setStatus(_A)
_MemorySize_Type=Integer32
_MemorySize_Object=MibScalar
memorySize=_MemorySize_Object((1,3,6,1,4,1,27514,1,2,1,1,2,12),_MemorySize_Type())
memorySize.setMaxAccess(_E)
if mibBuilder.loadTexts:memorySize.setStatus(_A)
_MemoryIdle_Type=Integer32
_MemoryIdle_Object=MibScalar
memoryIdle=_MemoryIdle_Object((1,3,6,1,4,1,27514,1,2,1,1,2,13),_MemoryIdle_Type())
memoryIdle.setMaxAccess(_E)
if mibBuilder.loadTexts:memoryIdle.setStatus(_A)
_SystemClock_ObjectIdentity=ObjectIdentity
systemClock=_SystemClock_ObjectIdentity((1,3,6,1,4,1,27514,1,2,1,1,2,14))
_ClockTime_Type=Unsigned32
_ClockTime_Object=MibScalar
clockTime=_ClockTime_Object((1,3,6,1,4,1,27514,1,2,1,1,2,14,1),_ClockTime_Type())
clockTime.setMaxAccess(_B)
if mibBuilder.loadTexts:clockTime.setStatus(_A)
class _TimeZoneName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_TimeZoneName_Type.__name__=_D
_TimeZoneName_Object=MibScalar
timeZoneName=_TimeZoneName_Object((1,3,6,1,4,1,27514,1,2,1,1,2,14,2),_TimeZoneName_Type())
timeZoneName.setMaxAccess(_B)
if mibBuilder.loadTexts:timeZoneName.setStatus(_A)
class _TimeZoneOffset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86399))
_TimeZoneOffset_Type.__name__=_C
_TimeZoneOffset_Object=MibScalar
timeZoneOffset=_TimeZoneOffset_Object((1,3,6,1,4,1,27514,1,2,1,1,2,14,3),_TimeZoneOffset_Type())
timeZoneOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:timeZoneOffset.setStatus(_A)
_OffsetNegFlag_Type=TruthValue
_OffsetNegFlag_Object=MibScalar
offsetNegFlag=_OffsetNegFlag_Object((1,3,6,1,4,1,27514,1,2,1,1,2,14,4),_OffsetNegFlag_Type())
offsetNegFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:offsetNegFlag.setStatus(_A)
_ProductName_Type=DisplayString
_ProductName_Object=MibScalar
productName=_ProductName_Object((1,3,6,1,4,1,27514,1,2,1,1,2,15),_ProductName_Type())
productName.setMaxAccess(_B)
if mibBuilder.loadTexts:productName.setStatus(_A)
class _SystemReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('reset',2),('resetToDefaults',3)))
_SystemReset_Type.__name__=_C
_SystemReset_Object=MibScalar
systemReset=_SystemReset_Object((1,3,6,1,4,1,27514,1,2,1,1,2,16),_SystemReset_Type())
systemReset.setMaxAccess(_B)
if mibBuilder.loadTexts:systemReset.setStatus(_A)
class _WriteConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('save',2),(_P,3),(_Q,4)))
_WriteConfig_Type.__name__=_C
_WriteConfig_Object=MibScalar
writeConfig=_WriteConfig_Object((1,3,6,1,4,1,27514,1,2,1,1,2,17),_WriteConfig_Type())
writeConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:writeConfig.setStatus(_A)
_SaveNMInterfaceConfig_ObjectIdentity=ObjectIdentity
saveNMInterfaceConfig=_SaveNMInterfaceConfig_ObjectIdentity((1,3,6,1,4,1,27514,1,2,1,1,2,18))
class _NmInterfaceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_NmInterfaceId_Type.__name__=_C
_NmInterfaceId_Object=MibScalar
nmInterfaceId=_NmInterfaceId_Object((1,3,6,1,4,1,27514,1,2,1,1,2,18,1),_NmInterfaceId_Type())
nmInterfaceId.setMaxAccess(_B)
if mibBuilder.loadTexts:nmInterfaceId.setStatus(_A)
_NmInterfaceIpAddress_Type=IpAddress
_NmInterfaceIpAddress_Object=MibScalar
nmInterfaceIpAddress=_NmInterfaceIpAddress_Object((1,3,6,1,4,1,27514,1,2,1,1,2,18,2),_NmInterfaceIpAddress_Type())
nmInterfaceIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nmInterfaceIpAddress.setStatus(_A)
_NmInterfaceNetMask_Type=IpAddress
_NmInterfaceNetMask_Object=MibScalar
nmInterfaceNetMask=_NmInterfaceNetMask_Object((1,3,6,1,4,1,27514,1,2,1,1,2,18,3),_NmInterfaceNetMask_Type())
nmInterfaceNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:nmInterfaceNetMask.setStatus(_A)
_NmInterfaceGateAddress_Type=IpAddress
_NmInterfaceGateAddress_Object=MibScalar
nmInterfaceGateAddress=_NmInterfaceGateAddress_Object((1,3,6,1,4,1,27514,1,2,1,1,2,18,4),_NmInterfaceGateAddress_Type())
nmInterfaceGateAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nmInterfaceGateAddress.setStatus(_A)
class _WriteNMInterfaceConifig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('saveNmconfig',1))
_WriteNMInterfaceConifig_Type.__name__=_C
_WriteNMInterfaceConifig_Object=MibScalar
writeNMInterfaceConifig=_WriteNMInterfaceConifig_Object((1,3,6,1,4,1,27514,1,2,1,1,2,18,5),_WriteNMInterfaceConifig_Type())
writeNMInterfaceConifig.setMaxAccess(_B)
if mibBuilder.loadTexts:writeNMInterfaceConifig.setStatus(_A)
class _WriteNMInterfaceConifigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('saveSuccess',1),(_P,2),(_Q,3),('noInterface',4),('noIpAddress',5),('differentSubnet',6),('noInterfaceParameter',7),('noIpAddressParameter',8),('noMaskParameter',9),('noGatewayParameter',10),('invalidIpOrMask',11)))
_WriteNMInterfaceConifigStatus_Type.__name__=_C
_WriteNMInterfaceConifigStatus_Object=MibScalar
writeNMInterfaceConifigStatus=_WriteNMInterfaceConifigStatus_Object((1,3,6,1,4,1,27514,1,2,1,1,2,18,6),_WriteNMInterfaceConifigStatus_Type())
writeNMInterfaceConifigStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:writeNMInterfaceConifigStatus.setStatus(_A)
class _ProdSerialNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_ProdSerialNo_Type.__name__=_D
_ProdSerialNo_Object=MibScalar
prodSerialNo=_ProdSerialNo_Object((1,3,6,1,4,1,27514,1,2,1,1,2,19),_ProdSerialNo_Type())
prodSerialNo.setMaxAccess(_E)
if mibBuilder.loadTexts:prodSerialNo.setStatus(_A)
_CpuBusyStatus_Type=TruthValue
_CpuBusyStatus_Object=MibScalar
cpuBusyStatus=_CpuBusyStatus_Object((1,3,6,1,4,1,27514,1,2,1,1,2,20),_CpuBusyStatus_Type())
cpuBusyStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cpuBusyStatus.setStatus(_A)
_CpuBusyAlarmEnable_Type=TruthValue
_CpuBusyAlarmEnable_Object=MibScalar
cpuBusyAlarmEnable=_CpuBusyAlarmEnable_Object((1,3,6,1,4,1,27514,1,2,1,1,2,21),_CpuBusyAlarmEnable_Type())
cpuBusyAlarmEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuBusyAlarmEnable.setStatus(_A)
_CpuBusyThreshold_Type=Integer32
_CpuBusyThreshold_Object=MibScalar
cpuBusyThreshold=_CpuBusyThreshold_Object((1,3,6,1,4,1,27514,1,2,1,1,2,22),_CpuBusyThreshold_Type())
cpuBusyThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuBusyThreshold.setStatus(_A)
_CpuUnbusyThreshold_Type=Integer32
_CpuUnbusyThreshold_Object=MibScalar
cpuUnbusyThreshold=_CpuUnbusyThreshold_Object((1,3,6,1,4,1,27514,1,2,1,1,2,23),_CpuUnbusyThreshold_Type())
cpuUnbusyThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuUnbusyThreshold.setStatus(_A)
_CpuStatusTrap_ObjectIdentity=ObjectIdentity
cpuStatusTrap=_CpuStatusTrap_ObjectIdentity((1,3,6,1,4,1,27514,1,2,1,1,2,24))
_GbnPlatformOAMIpAccessControl_ObjectIdentity=ObjectIdentity
gbnPlatformOAMIpAccessControl=_GbnPlatformOAMIpAccessControl_ObjectIdentity((1,3,6,1,4,1,27514,1,2,1,1,3))
_IpAccessControlTable_Object=MibTable
ipAccessControlTable=_IpAccessControlTable_Object((1,3,6,1,4,1,27514,1,2,1,1,3,1))
if mibBuilder.loadTexts:ipAccessControlTable.setStatus(_A)
_IpAccessControlEntry_Object=MibTableRow
ipAccessControlEntry=_IpAccessControlEntry_Object((1,3,6,1,4,1,27514,1,2,1,1,3,1,1))
ipAccessControlEntry.setIndexNames((0,_F,_R),(0,_F,_S),(0,_F,_T))
if mibBuilder.loadTexts:ipAccessControlEntry.setStatus(_A)
_ControlIpAddress_Type=IpAddress
_ControlIpAddress_Object=MibTableColumn
controlIpAddress=_ControlIpAddress_Object((1,3,6,1,4,1,27514,1,2,1,1,3,1,1,1),_ControlIpAddress_Type())
controlIpAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:controlIpAddress.setStatus(_A)
_ControlIpMask_Type=IpAddress
_ControlIpMask_Object=MibTableColumn
controlIpMask=_ControlIpMask_Object((1,3,6,1,4,1,27514,1,2,1,1,3,1,1,2),_ControlIpMask_Type())
controlIpMask.setMaxAccess(_E)
if mibBuilder.loadTexts:controlIpMask.setStatus(_A)
class _ControlTeminal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('snmp',1),('web',2),('telnet',3)))
_ControlTeminal_Type.__name__=_C
_ControlTeminal_Object=MibTableColumn
controlTeminal=_ControlTeminal_Object((1,3,6,1,4,1,27514,1,2,1,1,3,1,1,3),_ControlTeminal_Type())
controlTeminal.setMaxAccess(_E)
if mibBuilder.loadTexts:controlTeminal.setStatus(_A)
class _ControlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('destroy',2)))
_ControlStatus_Type.__name__=_C
_ControlStatus_Object=MibTableColumn
controlStatus=_ControlStatus_Object((1,3,6,1,4,1,27514,1,2,1,1,3,1,1,4),_ControlStatus_Type())
controlStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:controlStatus.setStatus(_A)
_GbnPlatformOAMWatchDog_ObjectIdentity=ObjectIdentity
gbnPlatformOAMWatchDog=_GbnPlatformOAMWatchDog_ObjectIdentity((1,3,6,1,4,1,27514,1,2,1,1,4))
class _SoftDogProxy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SoftDogProxy_Type.__name__=_C
_SoftDogProxy_Object=MibScalar
softDogProxy=_SoftDogProxy_Object((1,3,6,1,4,1,27514,1,2,1,1,4,1),_SoftDogProxy_Type())
softDogProxy.setMaxAccess(_B)
if mibBuilder.loadTexts:softDogProxy.setStatus(_A)
_GbnPlatformOAMMuser_ObjectIdentity=ObjectIdentity
gbnPlatformOAMMuser=_GbnPlatformOAMMuser_ObjectIdentity((1,3,6,1,4,1,27514,1,2,1,1,5))
_MusrTable_Object=MibTable
musrTable=_MusrTable_Object((1,3,6,1,4,1,27514,1,2,1,1,5,1))
if mibBuilder.loadTexts:musrTable.setStatus(_A)
_MusrEntry_Object=MibTableRow
musrEntry=_MusrEntry_Object((1,3,6,1,4,1,27514,1,2,1,1,5,1,1))
musrEntry.setIndexNames((0,_F,_U))
if mibBuilder.loadTexts:musrEntry.setStatus(_A)
class _MusrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_MusrIndex_Type.__name__=_C
_MusrIndex_Object=MibTableColumn
musrIndex=_MusrIndex_Object((1,3,6,1,4,1,27514,1,2,1,1,5,1,1,1),_MusrIndex_Type())
musrIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:musrIndex.setStatus(_A)
class _MusrName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MusrName_Type.__name__=_D
_MusrName_Object=MibTableColumn
musrName=_MusrName_Object((1,3,6,1,4,1,27514,1,2,1,1,5,1,1,2),_MusrName_Type())
musrName.setMaxAccess(_B)
if mibBuilder.loadTexts:musrName.setStatus(_A)
class _MusrPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_MusrPassword_Type.__name__=_D
_MusrPassword_Object=MibTableColumn
musrPassword=_MusrPassword_Object((1,3,6,1,4,1,27514,1,2,1,1,5,1,1,3),_MusrPassword_Type())
musrPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:musrPassword.setStatus(_A)
class _MusrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('normalUser',0),('superUser',1)))
_MusrType_Type.__name__=_C
_MusrType_Object=MibTableColumn
musrType=_MusrType_Object((1,3,6,1,4,1,27514,1,2,1,1,5,1,1,4),_MusrType_Type())
musrType.setMaxAccess(_B)
if mibBuilder.loadTexts:musrType.setStatus(_A)
class _MusrRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MusrRowStatus_Type.__name__=_C
_MusrRowStatus_Object=MibTableColumn
musrRowStatus=_MusrRowStatus_Object((1,3,6,1,4,1,27514,1,2,1,1,5,1,1,5),_MusrRowStatus_Type())
musrRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:musrRowStatus.setStatus(_A)
class _ManageUserAuthenType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('locacl',1),('radius',2),('radiusFailLocal',3)))
_ManageUserAuthenType_Type.__name__=_C
_ManageUserAuthenType_Object=MibScalar
manageUserAuthenType=_ManageUserAuthenType_Object((1,3,6,1,4,1,27514,1,2,1,1,5,2),_ManageUserAuthenType_Type())
manageUserAuthenType.setMaxAccess(_B)
if mibBuilder.loadTexts:manageUserAuthenType.setStatus(_A)
class _ManageUserAuthenRadiusName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ManageUserAuthenRadiusName_Type.__name__=_D
_ManageUserAuthenRadiusName_Object=MibScalar
manageUserAuthenRadiusName=_ManageUserAuthenRadiusName_Object((1,3,6,1,4,1,27514,1,2,1,1,5,3),_ManageUserAuthenRadiusName_Type())
manageUserAuthenRadiusName.setMaxAccess(_B)
if mibBuilder.loadTexts:manageUserAuthenRadiusName.setStatus(_A)
class _ManageUserAuthChallegeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('chap',1),('pap',2)))
_ManageUserAuthChallegeType_Type.__name__=_C
_ManageUserAuthChallegeType_Object=MibScalar
manageUserAuthChallegeType=_ManageUserAuthChallegeType_Object((1,3,6,1,4,1,27514,1,2,1,1,5,4),_ManageUserAuthChallegeType_Type())
manageUserAuthChallegeType.setMaxAccess(_B)
if mibBuilder.loadTexts:manageUserAuthChallegeType.setStatus(_A)
_GbnPlatformOAMUpDownLoad_ObjectIdentity=ObjectIdentity
gbnPlatformOAMUpDownLoad=_GbnPlatformOAMUpDownLoad_ObjectIdentity((1,3,6,1,4,1,27514,1,2,1,1,6))
_LoadTftpAddress_Type=IpAddress
_LoadTftpAddress_Object=MibScalar
loadTftpAddress=_LoadTftpAddress_Object((1,3,6,1,4,1,27514,1,2,1,1,6,1),_LoadTftpAddress_Type())
loadTftpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:loadTftpAddress.setStatus(_A)
class _LoadTftpFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_LoadTftpFileName_Type.__name__=_D
_LoadTftpFileName_Object=MibScalar
loadTftpFileName=_LoadTftpFileName_Object((1,3,6,1,4,1,27514,1,2,1,1,6,2),_LoadTftpFileName_Type())
loadTftpFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:loadTftpFileName.setStatus(_A)
class _LoadType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('application',1),('normalBootRom',2),('configuration',3),('bootCode',4),('alarm',5),('syslog',6),('wholeBootRom',7)))
_LoadType_Type.__name__=_C
_LoadType_Object=MibScalar
loadType=_LoadType_Object((1,3,6,1,4,1,27514,1,2,1,1,6,3),_LoadType_Type())
loadType.setMaxAccess(_B)
if mibBuilder.loadTexts:loadType.setStatus(_A)
class _LoadExecute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_K,1),('downloadTftp',2),('uploadTftp',3),('downloadFtp',4),('uploadFtp',5),('downloadXmodem',6)))
_LoadExecute_Type.__name__=_C
_LoadExecute_Object=MibScalar
loadExecute=_LoadExecute_Object((1,3,6,1,4,1,27514,1,2,1,1,6,4),_LoadExecute_Type())
loadExecute.setMaxAccess(_B)
if mibBuilder.loadTexts:loadExecute.setStatus(_A)
class _LoadExecuteStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('notStarted',1),('inProgressTftp',2),('successTftp',3),('errorConnectionTftp',4),('errorFilenameTftp',5),('errorFaultTftp',6),('inProgressFtp',7),('successFtp',8),('errorConnectionFtp',9),('errorFilenameFtp',10),('errorFaultFtp',11),('inProgressXmodem',12),('successXmodem',13),('errorConnectionXmodem',14),('errorFilenameXmodem',15),('errorFaultXmodem',16)))
_LoadExecuteStatus_Type.__name__=_C
_LoadExecuteStatus_Object=MibScalar
loadExecuteStatus=_LoadExecuteStatus_Object((1,3,6,1,4,1,27514,1,2,1,1,6,5),_LoadExecuteStatus_Type())
loadExecuteStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:loadExecuteStatus.setStatus(_A)
_LoadFtpAddress_Type=IpAddress
_LoadFtpAddress_Object=MibScalar
loadFtpAddress=_LoadFtpAddress_Object((1,3,6,1,4,1,27514,1,2,1,1,6,6),_LoadFtpAddress_Type())
loadFtpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:loadFtpAddress.setStatus(_A)
class _LoadFtpFileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_LoadFtpFileName_Type.__name__=_D
_LoadFtpFileName_Object=MibScalar
loadFtpFileName=_LoadFtpFileName_Object((1,3,6,1,4,1,27514,1,2,1,1,6,7),_LoadFtpFileName_Type())
loadFtpFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:loadFtpFileName.setStatus(_A)
class _LoadFtpUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_LoadFtpUserName_Type.__name__=_D
_LoadFtpUserName_Object=MibScalar
loadFtpUserName=_LoadFtpUserName_Object((1,3,6,1,4,1,27514,1,2,1,1,6,8),_LoadFtpUserName_Type())
loadFtpUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:loadFtpUserName.setStatus(_A)
class _LoadFtpUserPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_LoadFtpUserPassword_Type.__name__=_D
_LoadFtpUserPassword_Object=MibScalar
loadFtpUserPassword=_LoadFtpUserPassword_Object((1,3,6,1,4,1,27514,1,2,1,1,6,9),_LoadFtpUserPassword_Type())
loadFtpUserPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:loadFtpUserPassword.setStatus(_A)
_GbnPlatformOAMSnmp_ObjectIdentity=ObjectIdentity
gbnPlatformOAMSnmp=_GbnPlatformOAMSnmp_ObjectIdentity((1,3,6,1,4,1,27514,1,2,1,1,7))
_SnmpCommunityToViewTable_Object=MibTable
snmpCommunityToViewTable=_SnmpCommunityToViewTable_Object((1,3,6,1,4,1,27514,1,2,1,1,7,1))
if mibBuilder.loadTexts:snmpCommunityToViewTable.setStatus(_A)
_SnmpCommunityToViewEntry_Object=MibTableRow
snmpCommunityToViewEntry=_SnmpCommunityToViewEntry_Object((1,3,6,1,4,1,27514,1,2,1,1,7,1,1))
snmpCommunityToViewEntry.setIndexNames((0,_F,_V))
if mibBuilder.loadTexts:snmpCommunityToViewEntry.setStatus(_A)
class _SnmpComm2ViewIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_SnmpComm2ViewIndex_Type.__name__=_C
_SnmpComm2ViewIndex_Object=MibTableColumn
snmpComm2ViewIndex=_SnmpComm2ViewIndex_Object((1,3,6,1,4,1,27514,1,2,1,1,7,1,1,1),_SnmpComm2ViewIndex_Type())
snmpComm2ViewIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:snmpComm2ViewIndex.setStatus(_A)
class _SnmpComm2ViewCommName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_SnmpComm2ViewCommName_Type.__name__=_D
_SnmpComm2ViewCommName_Object=MibTableColumn
snmpComm2ViewCommName=_SnmpComm2ViewCommName_Object((1,3,6,1,4,1,27514,1,2,1,1,7,1,1,2),_SnmpComm2ViewCommName_Type())
snmpComm2ViewCommName.setMaxAccess(_J)
if mibBuilder.loadTexts:snmpComm2ViewCommName.setStatus(_A)
class _SnmpComm2ViewViewName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SnmpComm2ViewViewName_Type.__name__=_M
_SnmpComm2ViewViewName_Object=MibTableColumn
snmpComm2ViewViewName=_SnmpComm2ViewViewName_Object((1,3,6,1,4,1,27514,1,2,1,1,7,1,1,3),_SnmpComm2ViewViewName_Type())
snmpComm2ViewViewName.setMaxAccess(_J)
if mibBuilder.loadTexts:snmpComm2ViewViewName.setStatus(_A)
class _SnmpComm2ViewPermission_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('readOnly',1),('readWrite',2)))
_SnmpComm2ViewPermission_Type.__name__=_C
_SnmpComm2ViewPermission_Object=MibTableColumn
snmpComm2ViewPermission=_SnmpComm2ViewPermission_Object((1,3,6,1,4,1,27514,1,2,1,1,7,1,1,4),_SnmpComm2ViewPermission_Type())
snmpComm2ViewPermission.setMaxAccess(_J)
if mibBuilder.loadTexts:snmpComm2ViewPermission.setStatus(_A)
_SnmpComm2ViewRowStatus_Type=RowStatus
_SnmpComm2ViewRowStatus_Object=MibTableColumn
snmpComm2ViewRowStatus=_SnmpComm2ViewRowStatus_Object((1,3,6,1,4,1,27514,1,2,1,1,7,1,1,5),_SnmpComm2ViewRowStatus_Type())
snmpComm2ViewRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:snmpComm2ViewRowStatus.setStatus(_A)
_SnmpNotifyTypeTable_Object=MibTable
snmpNotifyTypeTable=_SnmpNotifyTypeTable_Object((1,3,6,1,4,1,27514,1,2,1,1,7,2))
if mibBuilder.loadTexts:snmpNotifyTypeTable.setStatus(_A)
_SnmpNotifyTypeEntry_Object=MibTableRow
snmpNotifyTypeEntry=_SnmpNotifyTypeEntry_Object((1,3,6,1,4,1,27514,1,2,1,1,7,2,1))
snmpNotifyTypeEntry.setIndexNames((0,_F,_W))
if mibBuilder.loadTexts:snmpNotifyTypeEntry.setStatus(_A)
class _SnmpPrivateNotifyType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SnmpPrivateNotifyType_Type.__name__=_D
_SnmpPrivateNotifyType_Object=MibTableColumn
snmpPrivateNotifyType=_SnmpPrivateNotifyType_Object((1,3,6,1,4,1,27514,1,2,1,1,7,2,1,1),_SnmpPrivateNotifyType_Type())
snmpPrivateNotifyType.setMaxAccess(_E)
if mibBuilder.loadTexts:snmpPrivateNotifyType.setStatus(_A)
class _SnmpNotifyTypeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SnmpNotifyTypeStatus_Type.__name__=_C
_SnmpNotifyTypeStatus_Object=MibTableColumn
snmpNotifyTypeStatus=_SnmpNotifyTypeStatus_Object((1,3,6,1,4,1,27514,1,2,1,1,7,2,1,2),_SnmpNotifyTypeStatus_Type())
snmpNotifyTypeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpNotifyTypeStatus.setStatus(_A)
_GbnPlatformOAMSnmpNotifyType_ObjectIdentity=ObjectIdentity
gbnPlatformOAMSnmpNotifyType=_GbnPlatformOAMSnmpNotifyType_ObjectIdentity((1,3,6,1,4,1,27514,1,2,1,1,7,3))
class _SnmpTrapSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_SnmpTrapSource_Type.__name__=_C
_SnmpTrapSource_Object=MibScalar
snmpTrapSource=_SnmpTrapSource_Object((1,3,6,1,4,1,27514,1,2,1,1,7,4),_SnmpTrapSource_Type())
snmpTrapSource.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpTrapSource.setStatus(_A)
_SnmpRemoteEngineTable_Object=MibTable
snmpRemoteEngineTable=_SnmpRemoteEngineTable_Object((1,3,6,1,4,1,27514,1,2,1,1,7,5))
if mibBuilder.loadTexts:snmpRemoteEngineTable.setStatus(_A)
_SnmpRemoteEngineEntry_Object=MibTableRow
snmpRemoteEngineEntry=_SnmpRemoteEngineEntry_Object((1,3,6,1,4,1,27514,1,2,1,1,7,5,1))
snmpRemoteEngineEntry.setIndexNames((0,_F,_X))
if mibBuilder.loadTexts:snmpRemoteEngineEntry.setStatus(_A)
_SnmpRemoteEngineID_Type=DisplayString
_SnmpRemoteEngineID_Object=MibTableColumn
snmpRemoteEngineID=_SnmpRemoteEngineID_Object((1,3,6,1,4,1,27514,1,2,1,1,7,5,1,1),_SnmpRemoteEngineID_Type())
snmpRemoteEngineID.setMaxAccess(_I)
if mibBuilder.loadTexts:snmpRemoteEngineID.setStatus(_A)
class _SnmpRemoteHostTAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_SnmpRemoteHostTAddr_Type.__name__=_L
_SnmpRemoteHostTAddr_Object=MibTableColumn
snmpRemoteHostTAddr=_SnmpRemoteHostTAddr_Object((1,3,6,1,4,1,27514,1,2,1,1,7,5,1,2),_SnmpRemoteHostTAddr_Type())
snmpRemoteHostTAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpRemoteHostTAddr.setStatus(_A)
class _SnmpDeleteRemoteEngineTableRow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('deleteRow',1))
_SnmpDeleteRemoteEngineTableRow_Type.__name__=_C
_SnmpDeleteRemoteEngineTableRow_Object=MibTableColumn
snmpDeleteRemoteEngineTableRow=_SnmpDeleteRemoteEngineTableRow_Object((1,3,6,1,4,1,27514,1,2,1,1,7,5,1,3),_SnmpDeleteRemoteEngineTableRow_Type())
snmpDeleteRemoteEngineTableRow.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpDeleteRemoteEngineTableRow.setStatus(_A)
class _SnmpTrapSourceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_SnmpTrapSourceType_Type.__name__=_C
_SnmpTrapSourceType_Object=MibScalar
snmpTrapSourceType=_SnmpTrapSourceType_Object((1,3,6,1,4,1,27514,1,2,1,1,7,6),_SnmpTrapSourceType_Type())
snmpTrapSourceType.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpTrapSourceType.setStatus(_A)
_GbnPlatformOAMSntpClient_ObjectIdentity=ObjectIdentity
gbnPlatformOAMSntpClient=_GbnPlatformOAMSntpClient_ObjectIdentity((1,3,6,1,4,1,27514,1,2,1,1,8))
_GbnPlatformOAMSyslog_ObjectIdentity=ObjectIdentity
gbnPlatformOAMSyslog=_GbnPlatformOAMSyslog_ObjectIdentity((1,3,6,1,4,1,27514,1,2,1,1,9))
_GbnPlatformOAMPortCar_ObjectIdentity=ObjectIdentity
gbnPlatformOAMPortCar=_GbnPlatformOAMPortCar_ObjectIdentity((1,3,6,1,4,1,27514,1,2,1,1,10))
_PortCarTable_Object=MibTable
portCarTable=_PortCarTable_Object((1,3,6,1,4,1,27514,1,2,1,1,10,1))
if mibBuilder.loadTexts:portCarTable.setStatus(_A)
_PortCarEntry_Object=MibTableRow
portCarEntry=_PortCarEntry_Object((1,3,6,1,4,1,27514,1,2,1,1,10,1,1))
portCarEntry.setIndexNames((0,_F,_Y))
if mibBuilder.loadTexts:portCarEntry.setStatus(_A)
class _PortCarPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,26))
_PortCarPort_Type.__name__=_C
_PortCarPort_Object=MibTableColumn
portCarPort=_PortCarPort_Object((1,3,6,1,4,1,27514,1,2,1,1,10,1,1,1),_PortCarPort_Type())
portCarPort.setMaxAccess(_I)
if mibBuilder.loadTexts:portCarPort.setStatus(_A)
_PortCarEnable_Type=TruthValue
_PortCarEnable_Object=MibTableColumn
portCarEnable=_PortCarEnable_Object((1,3,6,1,4,1,27514,1,2,1,1,10,1,1,2),_PortCarEnable_Type())
portCarEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:portCarEnable.setStatus(_A)
_PortCarGlobalEnable_Type=TruthValue
_PortCarGlobalEnable_Object=MibScalar
portCarGlobalEnable=_PortCarGlobalEnable_Object((1,3,6,1,4,1,27514,1,2,1,1,10,2),_PortCarGlobalEnable_Type())
portCarGlobalEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:portCarGlobalEnable.setStatus(_A)
_PortCarOpenTime_Type=Integer32
_PortCarOpenTime_Object=MibScalar
portCarOpenTime=_PortCarOpenTime_Object((1,3,6,1,4,1,27514,1,2,1,1,10,3),_PortCarOpenTime_Type())
portCarOpenTime.setMaxAccess(_B)
if mibBuilder.loadTexts:portCarOpenTime.setStatus(_A)
_DiscardBpdu_Type=Integer32
_DiscardBpdu_Object=MibScalar
discardBpdu=_DiscardBpdu_Object((1,3,6,1,4,1,27514,1,2,1,1,10,4),_DiscardBpdu_Type())
discardBpdu.setMaxAccess(_B)
if mibBuilder.loadTexts:discardBpdu.setStatus(_A)
_PortCarRate_Type=Integer32
_PortCarRate_Object=MibScalar
portCarRate=_PortCarRate_Object((1,3,6,1,4,1,27514,1,2,1,1,10,5),_PortCarRate_Type())
portCarRate.setMaxAccess(_B)
if mibBuilder.loadTexts:portCarRate.setStatus(_A)
_GbnPlatformOAMSsh_ObjectIdentity=ObjectIdentity
gbnPlatformOAMSsh=_GbnPlatformOAMSsh_ObjectIdentity((1,3,6,1,4,1,27514,1,2,1,1,11))
_GbnPlatformOAMMailalarm_ObjectIdentity=ObjectIdentity
gbnPlatformOAMMailalarm=_GbnPlatformOAMMailalarm_ObjectIdentity((1,3,6,1,4,1,27514,1,2,1,1,12))
cpuBusyTrap=NotificationType((1,3,6,1,4,1,27514,1,2,1,1,2,24,1))
if mibBuilder.loadTexts:cpuBusyTrap.setStatus(_A)
cpuUnbusyTrap=NotificationType((1,3,6,1,4,1,27514,1,2,1,1,2,24,2))
if mibBuilder.loadTexts:cpuUnbusyTrap.setStatus(_A)
snmpNotifyTypeSaveConfiguration=NotificationType((1,3,6,1,4,1,27514,1,2,1,1,7,3,1))
if mibBuilder.loadTexts:snmpNotifyTypeSaveConfiguration.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'gbnPlatformOAM':gbnPlatformOAM,'gbnPlatformOAMSysIf':gbnPlatformOAMSysIf,'sysIfMACAddr':sysIfMACAddr,'sysIfIpAddress':sysIfIpAddress,'sysIfIPGateAddress':sysIfIPGateAddress,'sysIfIPNetMask':sysIfIPNetMask,'sysIfIPStatus':sysIfIPStatus,'sysIfBOOTPOnOff':sysIfBOOTPOnOff,'sysIfDHCPOnOff':sysIfDHCPOnOff,'sysIfManageVLANTbale':sysIfManageVLANTbale,'sysIfManageVLANEntry':sysIfManageVLANEntry,_O:sysIfManageVLANVid,'sysIfManageVLANRowStatus':sysIfManageVLANRowStatus,'gbnPlatformOAMSystem':gbnPlatformOAMSystem,'softwarePlate':softwarePlate,'softwareVersion':softwareVersion,'softwareCompliedTimeE':softwareCompliedTimeE,'softwareCompliedTimeC':softwareCompliedTimeC,'cpuDescrition':cpuDescrition,'sdramDescrition':sdramDescrition,'flashDescrition':flashDescrition,'hardwareVersion':hardwareVersion,'bootromVersion':bootromVersion,'hostName':hostName,'cpuIdle':cpuIdle,'memorySize':memorySize,'memoryIdle':memoryIdle,'systemClock':systemClock,'clockTime':clockTime,'timeZoneName':timeZoneName,'timeZoneOffset':timeZoneOffset,'offsetNegFlag':offsetNegFlag,'productName':productName,'systemReset':systemReset,'writeConfig':writeConfig,'saveNMInterfaceConfig':saveNMInterfaceConfig,'nmInterfaceId':nmInterfaceId,'nmInterfaceIpAddress':nmInterfaceIpAddress,'nmInterfaceNetMask':nmInterfaceNetMask,'nmInterfaceGateAddress':nmInterfaceGateAddress,'writeNMInterfaceConifig':writeNMInterfaceConifig,'writeNMInterfaceConifigStatus':writeNMInterfaceConifigStatus,'prodSerialNo':prodSerialNo,'cpuBusyStatus':cpuBusyStatus,'cpuBusyAlarmEnable':cpuBusyAlarmEnable,'cpuBusyThreshold':cpuBusyThreshold,'cpuUnbusyThreshold':cpuUnbusyThreshold,'cpuStatusTrap':cpuStatusTrap,'cpuBusyTrap':cpuBusyTrap,'cpuUnbusyTrap':cpuUnbusyTrap,'gbnPlatformOAMIpAccessControl':gbnPlatformOAMIpAccessControl,'ipAccessControlTable':ipAccessControlTable,'ipAccessControlEntry':ipAccessControlEntry,_R:controlIpAddress,_S:controlIpMask,_T:controlTeminal,'controlStatus':controlStatus,'gbnPlatformOAMWatchDog':gbnPlatformOAMWatchDog,'softDogProxy':softDogProxy,'gbnPlatformOAMMuser':gbnPlatformOAMMuser,'musrTable':musrTable,'musrEntry':musrEntry,_U:musrIndex,'musrName':musrName,'musrPassword':musrPassword,'musrType':musrType,'musrRowStatus':musrRowStatus,'manageUserAuthenType':manageUserAuthenType,'manageUserAuthenRadiusName':manageUserAuthenRadiusName,'manageUserAuthChallegeType':manageUserAuthChallegeType,'gbnPlatformOAMUpDownLoad':gbnPlatformOAMUpDownLoad,'loadTftpAddress':loadTftpAddress,'loadTftpFileName':loadTftpFileName,'loadType':loadType,'loadExecute':loadExecute,'loadExecuteStatus':loadExecuteStatus,'loadFtpAddress':loadFtpAddress,'loadFtpFileName':loadFtpFileName,'loadFtpUserName':loadFtpUserName,'loadFtpUserPassword':loadFtpUserPassword,'gbnPlatformOAMSnmp':gbnPlatformOAMSnmp,'snmpCommunityToViewTable':snmpCommunityToViewTable,'snmpCommunityToViewEntry':snmpCommunityToViewEntry,_V:snmpComm2ViewIndex,'snmpComm2ViewCommName':snmpComm2ViewCommName,'snmpComm2ViewViewName':snmpComm2ViewViewName,'snmpComm2ViewPermission':snmpComm2ViewPermission,'snmpComm2ViewRowStatus':snmpComm2ViewRowStatus,'snmpNotifyTypeTable':snmpNotifyTypeTable,'snmpNotifyTypeEntry':snmpNotifyTypeEntry,_W:snmpPrivateNotifyType,'snmpNotifyTypeStatus':snmpNotifyTypeStatus,'gbnPlatformOAMSnmpNotifyType':gbnPlatformOAMSnmpNotifyType,'snmpNotifyTypeSaveConfiguration':snmpNotifyTypeSaveConfiguration,'snmpTrapSource':snmpTrapSource,'snmpRemoteEngineTable':snmpRemoteEngineTable,'snmpRemoteEngineEntry':snmpRemoteEngineEntry,_X:snmpRemoteEngineID,'snmpRemoteHostTAddr':snmpRemoteHostTAddr,'snmpDeleteRemoteEngineTableRow':snmpDeleteRemoteEngineTableRow,'snmpTrapSourceType':snmpTrapSourceType,'gbnPlatformOAMSntpClient':gbnPlatformOAMSntpClient,'gbnPlatformOAMSyslog':gbnPlatformOAMSyslog,'gbnPlatformOAMPortCar':gbnPlatformOAMPortCar,'portCarTable':portCarTable,'portCarEntry':portCarEntry,_Y:portCarPort,'portCarEnable':portCarEnable,'portCarGlobalEnable':portCarGlobalEnable,'portCarOpenTime':portCarOpenTime,'discardBpdu':discardBpdu,'portCarRate':portCarRate,'gbnPlatformOAMSsh':gbnPlatformOAMSsh,'gbnPlatformOAMMailalarm':gbnPlatformOAMMailalarm})