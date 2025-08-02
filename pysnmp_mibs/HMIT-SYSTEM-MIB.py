_Z='memIndex'
_Y='cpuTemperatureIndex'
_X='cpuCoreId'
_W='cpuIndex'
_V='fanIndex'
_U='fanInfoIndex'
_T='fanCardIndex'
_S='normal'
_R='powerIndex'
_Q='portIndex'
_P='portSubSlotIndex'
_O='portSlotIndex'
_N='subSlotIndex'
_M='subSlotParentIndex'
_L='mpuIndex'
_K='read-write'
_J='off'
_I='on'
_H='offline'
_G='online'
_F='Gauge32'
_E='HMIT-SYSTEM-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmITMgmt,=mibBuilder.importSymbols('HMIT-SMI','hmITMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_F,_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TruthValue')
hmITSystemMib=ModuleIdentity((1,3,6,1,4,1,248,100,1,3,600))
if mibBuilder.loadTexts:hmITSystemMib.setRevisions(('2010-01-08 17:00',))
_HmITSystemTrap_ObjectIdentity=ObjectIdentity
hmITSystemTrap=_HmITSystemTrap_ObjectIdentity((1,3,6,1,4,1,248,100,1,3,600,0))
_HmITSysInfoMib_ObjectIdentity=ObjectIdentity
hmITSysInfoMib=_HmITSysInfoMib_ObjectIdentity((1,3,6,1,4,1,248,100,1,3,600,1))
class _SysVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SysVoltage_Type.__name__=_C
_SysVoltage_Object=MibScalar
sysVoltage=_SysVoltage_Object((1,3,6,1,4,1,248,100,1,3,600,1,1),_SysVoltage_Type())
sysVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:sysVoltage.setStatus(_A)
if mibBuilder.loadTexts:sysVoltage.setUnits('mV')
class _SysCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SysCurrent_Type.__name__=_C
_SysCurrent_Object=MibScalar
sysCurrent=_SysCurrent_Object((1,3,6,1,4,1,248,100,1,3,600,1,2),_SysCurrent_Type())
sysCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:sysCurrent.setStatus(_A)
if mibBuilder.loadTexts:sysCurrent.setUnits('mA')
_HmITSysMpuMib_ObjectIdentity=ObjectIdentity
hmITSysMpuMib=_HmITSysMpuMib_ObjectIdentity((1,3,6,1,4,1,248,100,1,3,600,2))
_MpuInfoTable_Object=MibTable
mpuInfoTable=_MpuInfoTable_Object((1,3,6,1,4,1,248,100,1,3,600,2,1))
if mibBuilder.loadTexts:mpuInfoTable.setStatus(_A)
_MpuInfoEntry_Object=MibTableRow
mpuInfoEntry=_MpuInfoEntry_Object((1,3,6,1,4,1,248,100,1,3,600,2,1,1))
mpuInfoEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:mpuInfoEntry.setStatus(_A)
class _MpuIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MpuIndex_Type.__name__=_C
_MpuIndex_Object=MibTableColumn
mpuIndex=_MpuIndex_Object((1,3,6,1,4,1,248,100,1,3,600,2,1,1,1),_MpuIndex_Type())
mpuIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mpuIndex.setStatus(_A)
class _MpuType_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MpuType_Type.__name__=_F
_MpuType_Object=MibTableColumn
mpuType=_MpuType_Object((1,3,6,1,4,1,248,100,1,3,600,2,1,1,2),_MpuType_Type())
mpuType.setMaxAccess(_B)
if mibBuilder.loadTexts:mpuType.setStatus(_A)
class _MpuDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_MpuDescription_Type.__name__=_D
_MpuDescription_Object=MibTableColumn
mpuDescription=_MpuDescription_Object((1,3,6,1,4,1,248,100,1,3,600,2,1,1,3),_MpuDescription_Type())
mpuDescription.setMaxAccess(_K)
if mibBuilder.loadTexts:mpuDescription.setStatus(_A)
class _MpuSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_MpuSerialNumber_Type.__name__=_D
_MpuSerialNumber_Object=MibTableColumn
mpuSerialNumber=_MpuSerialNumber_Object((1,3,6,1,4,1,248,100,1,3,600,2,1,1,4),_MpuSerialNumber_Type())
mpuSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:mpuSerialNumber.setStatus(_A)
class _MpuSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_MpuSoftwareVersion_Type.__name__=_D
_MpuSoftwareVersion_Object=MibTableColumn
mpuSoftwareVersion=_MpuSoftwareVersion_Object((1,3,6,1,4,1,248,100,1,3,600,2,1,1,5),_MpuSoftwareVersion_Type())
mpuSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mpuSoftwareVersion.setStatus(_A)
_MpuHardwareVersion_Type=DisplayString
_MpuHardwareVersion_Object=MibTableColumn
mpuHardwareVersion=_MpuHardwareVersion_Object((1,3,6,1,4,1,248,100,1,3,600,2,1,1,6),_MpuHardwareVersion_Type())
mpuHardwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mpuHardwareVersion.setStatus(_A)
_MpuFPGAVersion_Type=DisplayString
_MpuFPGAVersion_Object=MibTableColumn
mpuFPGAVersion=_MpuFPGAVersion_Object((1,3,6,1,4,1,248,100,1,3,600,2,1,1,7),_MpuFPGAVersion_Type())
mpuFPGAVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mpuFPGAVersion.setStatus(_A)
class _MpuMonitorVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_MpuMonitorVersion_Type.__name__=_D
_MpuMonitorVersion_Object=MibTableColumn
mpuMonitorVersion=_MpuMonitorVersion_Object((1,3,6,1,4,1,248,100,1,3,600,2,1,1,8),_MpuMonitorVersion_Type())
mpuMonitorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mpuMonitorVersion.setStatus(_A)
class _MpuCMMSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_MpuCMMSoftwareVersion_Type.__name__=_D
_MpuCMMSoftwareVersion_Object=MibTableColumn
mpuCMMSoftwareVersion=_MpuCMMSoftwareVersion_Object((1,3,6,1,4,1,248,100,1,3,600,2,1,1,9),_MpuCMMSoftwareVersion_Type())
mpuCMMSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mpuCMMSoftwareVersion.setStatus(_A)
class _MpuCMMHardwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_MpuCMMHardwareVersion_Type.__name__=_D
_MpuCMMHardwareVersion_Object=MibTableColumn
mpuCMMHardwareVersion=_MpuCMMHardwareVersion_Object((1,3,6,1,4,1,248,100,1,3,600,2,1,1,10),_MpuCMMHardwareVersion_Type())
mpuCMMHardwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mpuCMMHardwareVersion.setStatus(_A)
class _MpuCMMMonitorVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_MpuCMMMonitorVersion_Type.__name__=_D
_MpuCMMMonitorVersion_Object=MibTableColumn
mpuCMMMonitorVersion=_MpuCMMMonitorVersion_Object((1,3,6,1,4,1,248,100,1,3,600,2,1,1,11),_MpuCMMMonitorVersion_Type())
mpuCMMMonitorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:mpuCMMMonitorVersion.setStatus(_A)
_MpuFlashTotalBytes_Type=Counter64
_MpuFlashTotalBytes_Object=MibTableColumn
mpuFlashTotalBytes=_MpuFlashTotalBytes_Object((1,3,6,1,4,1,248,100,1,3,600,2,1,1,12),_MpuFlashTotalBytes_Type())
mpuFlashTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:mpuFlashTotalBytes.setStatus(_A)
_MpuFlashLeftBytes_Type=Counter64
_MpuFlashLeftBytes_Object=MibTableColumn
mpuFlashLeftBytes=_MpuFlashLeftBytes_Object((1,3,6,1,4,1,248,100,1,3,600,2,1,1,13),_MpuFlashLeftBytes_Type())
mpuFlashLeftBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:mpuFlashLeftBytes.setStatus(_A)
class _MpuWorkingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('master',1),('slave',2),('doubleRouter',3)))
_MpuWorkingMode_Type.__name__=_C
_MpuWorkingMode_Object=MibTableColumn
mpuWorkingMode=_MpuWorkingMode_Object((1,3,6,1,4,1,248,100,1,3,600,2,1,1,14),_MpuWorkingMode_Type())
mpuWorkingMode.setMaxAccess(_B)
if mibBuilder.loadTexts:mpuWorkingMode.setStatus(_A)
class _MpuOnlineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MpuOnlineStatus_Type.__name__=_C
_MpuOnlineStatus_Object=MibTableColumn
mpuOnlineStatus=_MpuOnlineStatus_Object((1,3,6,1,4,1,248,100,1,3,600,2,1,1,15),_MpuOnlineStatus_Type())
mpuOnlineStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpuOnlineStatus.setStatus(_A)
class _MpuWorkingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_MpuWorkingStatus_Type.__name__=_C
_MpuWorkingStatus_Object=MibTableColumn
mpuWorkingStatus=_MpuWorkingStatus_Object((1,3,6,1,4,1,248,100,1,3,600,2,1,1,16),_MpuWorkingStatus_Type())
mpuWorkingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpuWorkingStatus.setStatus(_A)
class _MpuPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_MpuPowerStatus_Type.__name__=_C
_MpuPowerStatus_Object=MibTableColumn
mpuPowerStatus=_MpuPowerStatus_Object((1,3,6,1,4,1,248,100,1,3,600,2,1,1,17),_MpuPowerStatus_Type())
mpuPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpuPowerStatus.setStatus(_A)
class _MpuSynchronizationStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('batchSync',1),('realtimeSync',2),('noSlave',3),('abnormal',4)))
_MpuSynchronizationStatus_Type.__name__=_C
_MpuSynchronizationStatus_Object=MibTableColumn
mpuSynchronizationStatus=_MpuSynchronizationStatus_Object((1,3,6,1,4,1,248,100,1,3,600,2,1,1,18),_MpuSynchronizationStatus_Type())
mpuSynchronizationStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpuSynchronizationStatus.setStatus(_A)
class _MpuCFStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MpuCFStatus_Type.__name__=_C
_MpuCFStatus_Object=MibTableColumn
mpuCFStatus=_MpuCFStatus_Object((1,3,6,1,4,1,248,100,1,3,600,2,1,1,19),_MpuCFStatus_Type())
mpuCFStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mpuCFStatus.setStatus(_A)
class _MpuTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,1000))
_MpuTemperature_Type.__name__=_C
_MpuTemperature_Object=MibTableColumn
mpuTemperature=_MpuTemperature_Object((1,3,6,1,4,1,248,100,1,3,600,2,1,1,20),_MpuTemperature_Type())
mpuTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:mpuTemperature.setStatus(_A)
class _MpuSubSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MpuSubSlotNumber_Type.__name__=_C
_MpuSubSlotNumber_Object=MibTableColumn
mpuSubSlotNumber=_MpuSubSlotNumber_Object((1,3,6,1,4,1,248,100,1,3,600,2,1,1,21),_MpuSubSlotNumber_Type())
mpuSubSlotNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:mpuSubSlotNumber.setStatus(_A)
class _HmITSysMpuUserSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HmITSysMpuUserSerialNumber_Type.__name__=_D
_HmITSysMpuUserSerialNumber_Object=MibTableColumn
hmITSysMpuUserSerialNumber=_HmITSysMpuUserSerialNumber_Object((1,3,6,1,4,1,248,100,1,3,600,2,1,1,22),_HmITSysMpuUserSerialNumber_Type())
hmITSysMpuUserSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hmITSysMpuUserSerialNumber.setStatus(_A)
class _MpuModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MpuModel_Type.__name__=_D
_MpuModel_Object=MibTableColumn
mpuModel=_MpuModel_Object((1,3,6,1,4,1,248,100,1,3,600,2,1,1,23),_MpuModel_Type())
mpuModel.setMaxAccess(_B)
if mibBuilder.loadTexts:mpuModel.setStatus(_A)
_HmITSysSubSlotMib_ObjectIdentity=ObjectIdentity
hmITSysSubSlotMib=_HmITSysSubSlotMib_ObjectIdentity((1,3,6,1,4,1,248,100,1,3,600,5))
_SubSlotTable_Object=MibTable
subSlotTable=_SubSlotTable_Object((1,3,6,1,4,1,248,100,1,3,600,5,1))
if mibBuilder.loadTexts:subSlotTable.setStatus(_A)
_SubSlotEntry_Object=MibTableRow
subSlotEntry=_SubSlotEntry_Object((1,3,6,1,4,1,248,100,1,3,600,5,1,1))
subSlotEntry.setIndexNames((0,_E,_M),(0,_E,_N))
if mibBuilder.loadTexts:subSlotEntry.setStatus(_A)
class _SubSlotParentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SubSlotParentIndex_Type.__name__=_C
_SubSlotParentIndex_Object=MibTableColumn
subSlotParentIndex=_SubSlotParentIndex_Object((1,3,6,1,4,1,248,100,1,3,600,5,1,1,1),_SubSlotParentIndex_Type())
subSlotParentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:subSlotParentIndex.setStatus(_A)
class _SubSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SubSlotIndex_Type.__name__=_C
_SubSlotIndex_Object=MibTableColumn
subSlotIndex=_SubSlotIndex_Object((1,3,6,1,4,1,248,100,1,3,600,5,1,1,2),_SubSlotIndex_Type())
subSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:subSlotIndex.setStatus(_A)
class _SubSlotCardType_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SubSlotCardType_Type.__name__=_F
_SubSlotCardType_Object=MibTableColumn
subSlotCardType=_SubSlotCardType_Object((1,3,6,1,4,1,248,100,1,3,600,5,1,1,3),_SubSlotCardType_Type())
subSlotCardType.setMaxAccess(_B)
if mibBuilder.loadTexts:subSlotCardType.setStatus(_A)
class _SubSlotPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SubSlotPortNumber_Type.__name__=_C
_SubSlotPortNumber_Object=MibTableColumn
subSlotPortNumber=_SubSlotPortNumber_Object((1,3,6,1,4,1,248,100,1,3,600,5,1,1,4),_SubSlotPortNumber_Type())
subSlotPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:subSlotPortNumber.setStatus(_A)
class _SubSlotOnlineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_SubSlotOnlineStatus_Type.__name__=_C
_SubSlotOnlineStatus_Object=MibTableColumn
subSlotOnlineStatus=_SubSlotOnlineStatus_Object((1,3,6,1,4,1,248,100,1,3,600,5,1,1,5),_SubSlotOnlineStatus_Type())
subSlotOnlineStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:subSlotOnlineStatus.setStatus(_A)
_HmITSysPortMib_ObjectIdentity=ObjectIdentity
hmITSysPortMib=_HmITSysPortMib_ObjectIdentity((1,3,6,1,4,1,248,100,1,3,600,6))
_PortInfoTable_Object=MibTable
portInfoTable=_PortInfoTable_Object((1,3,6,1,4,1,248,100,1,3,600,6,1))
if mibBuilder.loadTexts:portInfoTable.setStatus(_A)
_PortInfoEntry_Object=MibTableRow
portInfoEntry=_PortInfoEntry_Object((1,3,6,1,4,1,248,100,1,3,600,6,1,1))
portInfoEntry.setIndexNames((0,_E,_O),(0,_E,_P),(0,_E,_Q))
if mibBuilder.loadTexts:portInfoEntry.setStatus(_A)
class _PortSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PortSlotIndex_Type.__name__=_C
_PortSlotIndex_Object=MibTableColumn
portSlotIndex=_PortSlotIndex_Object((1,3,6,1,4,1,248,100,1,3,600,6,1,1,1),_PortSlotIndex_Type())
portSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:portSlotIndex.setStatus(_A)
class _PortSubSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PortSubSlotIndex_Type.__name__=_C
_PortSubSlotIndex_Object=MibTableColumn
portSubSlotIndex=_PortSubSlotIndex_Object((1,3,6,1,4,1,248,100,1,3,600,6,1,1,2),_PortSubSlotIndex_Type())
portSubSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:portSubSlotIndex.setStatus(_A)
class _PortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PortIndex_Type.__name__=_C
_PortIndex_Object=MibTableColumn
portIndex=_PortIndex_Object((1,3,6,1,4,1,248,100,1,3,600,6,1,1,3),_PortIndex_Type())
portIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:portIndex.setStatus(_A)
class _PortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('copper',1),('fiber',2)))
_PortType_Type.__name__=_C
_PortType_Object=MibTableColumn
portType=_PortType_Object((1,3,6,1,4,1,248,100,1,3,600,6,1,1,4),_PortType_Type())
portType.setMaxAccess(_B)
if mibBuilder.loadTexts:portType.setStatus(_A)
class _PortLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('loop',3)))
_PortLinkStatus_Type.__name__=_C
_PortLinkStatus_Object=MibTableColumn
portLinkStatus=_PortLinkStatus_Object((1,3,6,1,4,1,248,100,1,3,600,6,1,1,5),_PortLinkStatus_Type())
portLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:portLinkStatus.setStatus(_A)
class _PortOnlineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_PortOnlineStatus_Type.__name__=_C
_PortOnlineStatus_Object=MibTableColumn
portOnlineStatus=_PortOnlineStatus_Object((1,3,6,1,4,1,248,100,1,3,600,6,1,1,6),_PortOnlineStatus_Type())
portOnlineStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:portOnlineStatus.setStatus(_A)
_HmITSysPowerMib_ObjectIdentity=ObjectIdentity
hmITSysPowerMib=_HmITSysPowerMib_ObjectIdentity((1,3,6,1,4,1,248,100,1,3,600,7))
_PowerInfoTable_Object=MibTable
powerInfoTable=_PowerInfoTable_Object((1,3,6,1,4,1,248,100,1,3,600,7,1))
if mibBuilder.loadTexts:powerInfoTable.setStatus(_A)
_PowerInfoEntry_Object=MibTableRow
powerInfoEntry=_PowerInfoEntry_Object((1,3,6,1,4,1,248,100,1,3,600,7,1,1))
powerInfoEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:powerInfoEntry.setStatus(_A)
class _PowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PowerIndex_Type.__name__=_C
_PowerIndex_Object=MibTableColumn
powerIndex=_PowerIndex_Object((1,3,6,1,4,1,248,100,1,3,600,7,1,1,1),_PowerIndex_Type())
powerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:powerIndex.setStatus(_A)
class _PowerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('alternatingNonIntelligent',1),('directNonIntelligent',2),('alternatingIntelligent',3),('directIntelligent',4)))
_PowerType_Type.__name__=_C
_PowerType_Object=MibTableColumn
powerType=_PowerType_Object((1,3,6,1,4,1,248,100,1,3,600,7,1,1,2),_PowerType_Type())
powerType.setMaxAccess(_B)
if mibBuilder.loadTexts:powerType.setStatus(_A)
class _PowerDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_PowerDescription_Type.__name__=_D
_PowerDescription_Object=MibTableColumn
powerDescription=_PowerDescription_Object((1,3,6,1,4,1,248,100,1,3,600,7,1,1,3),_PowerDescription_Type())
powerDescription.setMaxAccess(_K)
if mibBuilder.loadTexts:powerDescription.setStatus(_A)
class _PowerSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_PowerSerialNumber_Type.__name__=_D
_PowerSerialNumber_Object=MibTableColumn
powerSerialNumber=_PowerSerialNumber_Object((1,3,6,1,4,1,248,100,1,3,600,7,1,1,4),_PowerSerialNumber_Type())
powerSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:powerSerialNumber.setStatus(_A)
class _PowerCMMSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_PowerCMMSoftwareVersion_Type.__name__=_D
_PowerCMMSoftwareVersion_Object=MibTableColumn
powerCMMSoftwareVersion=_PowerCMMSoftwareVersion_Object((1,3,6,1,4,1,248,100,1,3,600,7,1,1,5),_PowerCMMSoftwareVersion_Type())
powerCMMSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:powerCMMSoftwareVersion.setStatus(_A)
class _PowerCMMHardwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_PowerCMMHardwareVersion_Type.__name__=_D
_PowerCMMHardwareVersion_Object=MibTableColumn
powerCMMHardwareVersion=_PowerCMMHardwareVersion_Object((1,3,6,1,4,1,248,100,1,3,600,7,1,1,6),_PowerCMMHardwareVersion_Type())
powerCMMHardwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:powerCMMHardwareVersion.setStatus(_A)
class _PowerCMMMonitorVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_PowerCMMMonitorVersion_Type.__name__=_D
_PowerCMMMonitorVersion_Object=MibTableColumn
powerCMMMonitorVersion=_PowerCMMMonitorVersion_Object((1,3,6,1,4,1,248,100,1,3,600,7,1,1,7),_PowerCMMMonitorVersion_Type())
powerCMMMonitorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:powerCMMMonitorVersion.setStatus(_A)
class _PowerOnlineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_PowerOnlineStatus_Type.__name__=_C
_PowerOnlineStatus_Object=MibTableColumn
powerOnlineStatus=_PowerOnlineStatus_Object((1,3,6,1,4,1,248,100,1,3,600,7,1,1,8),_PowerOnlineStatus_Type())
powerOnlineStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:powerOnlineStatus.setStatus(_A)
class _PowerWorkingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_PowerWorkingStatus_Type.__name__=_C
_PowerWorkingStatus_Object=MibTableColumn
powerWorkingStatus=_PowerWorkingStatus_Object((1,3,6,1,4,1,248,100,1,3,600,7,1,1,9),_PowerWorkingStatus_Type())
powerWorkingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:powerWorkingStatus.setStatus(_A)
class _PowerAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),('alarm',2)))
_PowerAlarmStatus_Type.__name__=_C
_PowerAlarmStatus_Object=MibTableColumn
powerAlarmStatus=_PowerAlarmStatus_Object((1,3,6,1,4,1,248,100,1,3,600,7,1,1,10),_PowerAlarmStatus_Type())
powerAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:powerAlarmStatus.setStatus(_A)
class _PowerVoltageInput_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PowerVoltageInput_Type.__name__=_C
_PowerVoltageInput_Object=MibTableColumn
powerVoltageInput=_PowerVoltageInput_Object((1,3,6,1,4,1,248,100,1,3,600,7,1,1,11),_PowerVoltageInput_Type())
powerVoltageInput.setMaxAccess(_B)
if mibBuilder.loadTexts:powerVoltageInput.setStatus(_A)
if mibBuilder.loadTexts:powerVoltageInput.setUnits('mV')
class _PowerVoltageOutput_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PowerVoltageOutput_Type.__name__=_C
_PowerVoltageOutput_Object=MibTableColumn
powerVoltageOutput=_PowerVoltageOutput_Object((1,3,6,1,4,1,248,100,1,3,600,7,1,1,12),_PowerVoltageOutput_Type())
powerVoltageOutput.setMaxAccess(_B)
if mibBuilder.loadTexts:powerVoltageOutput.setStatus(_A)
if mibBuilder.loadTexts:powerVoltageOutput.setUnits('mV')
class _PowerCurrentInput_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PowerCurrentInput_Type.__name__=_C
_PowerCurrentInput_Object=MibTableColumn
powerCurrentInput=_PowerCurrentInput_Object((1,3,6,1,4,1,248,100,1,3,600,7,1,1,13),_PowerCurrentInput_Type())
powerCurrentInput.setMaxAccess(_B)
if mibBuilder.loadTexts:powerCurrentInput.setStatus(_A)
if mibBuilder.loadTexts:powerCurrentInput.setUnits('mA')
class _PowerCurrentOutput_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PowerCurrentOutput_Type.__name__=_C
_PowerCurrentOutput_Object=MibTableColumn
powerCurrentOutput=_PowerCurrentOutput_Object((1,3,6,1,4,1,248,100,1,3,600,7,1,1,14),_PowerCurrentOutput_Type())
powerCurrentOutput.setMaxAccess(_B)
if mibBuilder.loadTexts:powerCurrentOutput.setStatus(_A)
if mibBuilder.loadTexts:powerCurrentOutput.setUnits('mA')
class _PowerUserSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_PowerUserSerialNumber_Type.__name__=_D
_PowerUserSerialNumber_Object=MibTableColumn
powerUserSerialNumber=_PowerUserSerialNumber_Object((1,3,6,1,4,1,248,100,1,3,600,7,1,1,15),_PowerUserSerialNumber_Type())
powerUserSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:powerUserSerialNumber.setStatus(_A)
class _PowerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_PowerName_Type.__name__=_D
_PowerName_Object=MibTableColumn
powerName=_PowerName_Object((1,3,6,1,4,1,248,100,1,3,600,7,1,1,16),_PowerName_Type())
powerName.setMaxAccess(_B)
if mibBuilder.loadTexts:powerName.setStatus(_A)
_HmITSysFanCardMib_ObjectIdentity=ObjectIdentity
hmITSysFanCardMib=_HmITSysFanCardMib_ObjectIdentity((1,3,6,1,4,1,248,100,1,3,600,8))
_FanCardInfoTable_Object=MibTable
fanCardInfoTable=_FanCardInfoTable_Object((1,3,6,1,4,1,248,100,1,3,600,8,1))
if mibBuilder.loadTexts:fanCardInfoTable.setStatus(_A)
_FanCardInfoEntry_Object=MibTableRow
fanCardInfoEntry=_FanCardInfoEntry_Object((1,3,6,1,4,1,248,100,1,3,600,8,1,1))
fanCardInfoEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:fanCardInfoEntry.setStatus(_A)
class _FanCardIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FanCardIndex_Type.__name__=_C
_FanCardIndex_Object=MibTableColumn
fanCardIndex=_FanCardIndex_Object((1,3,6,1,4,1,248,100,1,3,600,8,1,1,1),_FanCardIndex_Type())
fanCardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fanCardIndex.setStatus(_A)
class _FanCardDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FanCardDescription_Type.__name__=_D
_FanCardDescription_Object=MibTableColumn
fanCardDescription=_FanCardDescription_Object((1,3,6,1,4,1,248,100,1,3,600,8,1,1,2),_FanCardDescription_Type())
fanCardDescription.setMaxAccess(_K)
if mibBuilder.loadTexts:fanCardDescription.setStatus(_A)
class _FanCardSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_FanCardSerialNumber_Type.__name__=_D
_FanCardSerialNumber_Object=MibTableColumn
fanCardSerialNumber=_FanCardSerialNumber_Object((1,3,6,1,4,1,248,100,1,3,600,8,1,1,3),_FanCardSerialNumber_Type())
fanCardSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fanCardSerialNumber.setStatus(_A)
class _FanCardCMMSoftwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_FanCardCMMSoftwareVersion_Type.__name__=_D
_FanCardCMMSoftwareVersion_Object=MibTableColumn
fanCardCMMSoftwareVersion=_FanCardCMMSoftwareVersion_Object((1,3,6,1,4,1,248,100,1,3,600,8,1,1,4),_FanCardCMMSoftwareVersion_Type())
fanCardCMMSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fanCardCMMSoftwareVersion.setStatus(_A)
class _FanCardCMMHardwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_FanCardCMMHardwareVersion_Type.__name__=_D
_FanCardCMMHardwareVersion_Object=MibTableColumn
fanCardCMMHardwareVersion=_FanCardCMMHardwareVersion_Object((1,3,6,1,4,1,248,100,1,3,600,8,1,1,5),_FanCardCMMHardwareVersion_Type())
fanCardCMMHardwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fanCardCMMHardwareVersion.setStatus(_A)
class _FanCardCMMMonitorVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_FanCardCMMMonitorVersion_Type.__name__=_D
_FanCardCMMMonitorVersion_Object=MibTableColumn
fanCardCMMMonitorVersion=_FanCardCMMMonitorVersion_Object((1,3,6,1,4,1,248,100,1,3,600,8,1,1,6),_FanCardCMMMonitorVersion_Type())
fanCardCMMMonitorVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fanCardCMMMonitorVersion.setStatus(_A)
class _FanCardOnlineStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FanCardOnlineStatus_Type.__name__=_C
_FanCardOnlineStatus_Object=MibTableColumn
fanCardOnlineStatus=_FanCardOnlineStatus_Object((1,3,6,1,4,1,248,100,1,3,600,8,1,1,7),_FanCardOnlineStatus_Type())
fanCardOnlineStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fanCardOnlineStatus.setStatus(_A)
class _FanCardWorkingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_FanCardWorkingStatus_Type.__name__=_C
_FanCardWorkingStatus_Object=MibTableColumn
fanCardWorkingStatus=_FanCardWorkingStatus_Object((1,3,6,1,4,1,248,100,1,3,600,8,1,1,8),_FanCardWorkingStatus_Type())
fanCardWorkingStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fanCardWorkingStatus.setStatus(_A)
class _FanCardAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),('alarm',2)))
_FanCardAlarmStatus_Type.__name__=_C
_FanCardAlarmStatus_Object=MibTableColumn
fanCardAlarmStatus=_FanCardAlarmStatus_Object((1,3,6,1,4,1,248,100,1,3,600,8,1,1,9),_FanCardAlarmStatus_Type())
fanCardAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fanCardAlarmStatus.setStatus(_A)
class _FanCardGrps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FanCardGrps_Type.__name__=_C
_FanCardGrps_Object=MibTableColumn
fanCardGrps=_FanCardGrps_Object((1,3,6,1,4,1,248,100,1,3,600,8,1,1,10),_FanCardGrps_Type())
fanCardGrps.setMaxAccess(_B)
if mibBuilder.loadTexts:fanCardGrps.setStatus(_A)
class _FanCardNumPerGrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FanCardNumPerGrp_Type.__name__=_C
_FanCardNumPerGrp_Object=MibTableColumn
fanCardNumPerGrp=_FanCardNumPerGrp_Object((1,3,6,1,4,1,248,100,1,3,600,8,1,1,11),_FanCardNumPerGrp_Type())
fanCardNumPerGrp.setMaxAccess(_B)
if mibBuilder.loadTexts:fanCardNumPerGrp.setStatus(_A)
class _FanCardUserSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_FanCardUserSerialNumber_Type.__name__=_D
_FanCardUserSerialNumber_Object=MibTableColumn
fanCardUserSerialNumber=_FanCardUserSerialNumber_Object((1,3,6,1,4,1,248,100,1,3,600,8,1,1,12),_FanCardUserSerialNumber_Type())
fanCardUserSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:fanCardUserSerialNumber.setStatus(_A)
class _FanCardName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_FanCardName_Type.__name__=_D
_FanCardName_Object=MibTableColumn
fanCardName=_FanCardName_Object((1,3,6,1,4,1,248,100,1,3,600,8,1,1,13),_FanCardName_Type())
fanCardName.setMaxAccess(_B)
if mibBuilder.loadTexts:fanCardName.setStatus(_A)
_FanInfoTable_Object=MibTable
fanInfoTable=_FanInfoTable_Object((1,3,6,1,4,1,248,100,1,3,600,8,2))
if mibBuilder.loadTexts:fanInfoTable.setStatus(_A)
_FanInfoEntry_Object=MibTableRow
fanInfoEntry=_FanInfoEntry_Object((1,3,6,1,4,1,248,100,1,3,600,8,2,1))
fanInfoEntry.setIndexNames((0,_E,_U),(0,_E,_V))
if mibBuilder.loadTexts:fanInfoEntry.setStatus(_A)
class _FanInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FanInfoIndex_Type.__name__=_C
_FanInfoIndex_Object=MibTableColumn
fanInfoIndex=_FanInfoIndex_Object((1,3,6,1,4,1,248,100,1,3,600,8,2,1,1),_FanInfoIndex_Type())
fanInfoIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fanInfoIndex.setStatus(_A)
class _FanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FanIndex_Type.__name__=_C
_FanIndex_Object=MibTableColumn
fanIndex=_FanIndex_Object((1,3,6,1,4,1,248,100,1,3,600,8,2,1,2),_FanIndex_Type())
fanIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fanIndex.setStatus(_A)
class _FanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FanStatus_Type.__name__=_C
_FanStatus_Object=MibTableColumn
fanStatus=_FanStatus_Object((1,3,6,1,4,1,248,100,1,3,600,8,2,1,3),_FanStatus_Type())
fanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fanStatus.setStatus(_A)
class _FanSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_FanSpeed_Type.__name__=_C
_FanSpeed_Object=MibTableColumn
fanSpeed=_FanSpeed_Object((1,3,6,1,4,1,248,100,1,3,600,8,2,1,4),_FanSpeed_Type())
fanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:fanSpeed.setStatus(_A)
_HmITSysCpuMib_ObjectIdentity=ObjectIdentity
hmITSysCpuMib=_HmITSysCpuMib_ObjectIdentity((1,3,6,1,4,1,248,100,1,3,600,9))
_CpuUtilizationTable_Object=MibTable
cpuUtilizationTable=_CpuUtilizationTable_Object((1,3,6,1,4,1,248,100,1,3,600,9,1))
if mibBuilder.loadTexts:cpuUtilizationTable.setStatus(_A)
_CpuUtilizationEntry_Object=MibTableRow
cpuUtilizationEntry=_CpuUtilizationEntry_Object((1,3,6,1,4,1,248,100,1,3,600,9,1,1))
cpuUtilizationEntry.setIndexNames((0,_E,_W),(0,_E,_X))
if mibBuilder.loadTexts:cpuUtilizationEntry.setStatus(_A)
class _CpuIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CpuIndex_Type.__name__=_C
_CpuIndex_Object=MibTableColumn
cpuIndex=_CpuIndex_Object((1,3,6,1,4,1,248,100,1,3,600,9,1,1,1),_CpuIndex_Type())
cpuIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuIndex.setStatus(_A)
class _CpuCoreId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CpuCoreId_Type.__name__=_C
_CpuCoreId_Object=MibTableColumn
cpuCoreId=_CpuCoreId_Object((1,3,6,1,4,1,248,100,1,3,600,9,1,1,2),_CpuCoreId_Type())
cpuCoreId.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreId.setStatus(_A)
class _CpuCoreUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CpuCoreUtilization_Type.__name__=_C
_CpuCoreUtilization_Object=MibTableColumn
cpuCoreUtilization=_CpuCoreUtilization_Object((1,3,6,1,4,1,248,100,1,3,600,9,1,1,3),_CpuCoreUtilization_Type())
cpuCoreUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuCoreUtilization.setStatus(_A)
if mibBuilder.loadTexts:cpuCoreUtilization.setUnits('%')
class _CpuPeakUtilizationPerMinute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CpuPeakUtilizationPerMinute_Type.__name__=_C
_CpuPeakUtilizationPerMinute_Object=MibTableColumn
cpuPeakUtilizationPerMinute=_CpuPeakUtilizationPerMinute_Object((1,3,6,1,4,1,248,100,1,3,600,9,1,1,4),_CpuPeakUtilizationPerMinute_Type())
cpuPeakUtilizationPerMinute.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuPeakUtilizationPerMinute.setStatus(_A)
if mibBuilder.loadTexts:cpuPeakUtilizationPerMinute.setUnits('%')
_CpuTemperatureTable_Object=MibTable
cpuTemperatureTable=_CpuTemperatureTable_Object((1,3,6,1,4,1,248,100,1,3,600,9,2))
if mibBuilder.loadTexts:cpuTemperatureTable.setStatus(_A)
_CpuTemperatureEntry_Object=MibTableRow
cpuTemperatureEntry=_CpuTemperatureEntry_Object((1,3,6,1,4,1,248,100,1,3,600,9,2,1))
cpuTemperatureEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:cpuTemperatureEntry.setStatus(_A)
class _CpuTemperatureIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CpuTemperatureIndex_Type.__name__=_C
_CpuTemperatureIndex_Object=MibTableColumn
cpuTemperatureIndex=_CpuTemperatureIndex_Object((1,3,6,1,4,1,248,100,1,3,600,9,2,1,1),_CpuTemperatureIndex_Type())
cpuTemperatureIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuTemperatureIndex.setStatus(_A)
class _CpuTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-100,1000))
_CpuTemperature_Type.__name__=_C
_CpuTemperature_Object=MibTableColumn
cpuTemperature=_CpuTemperature_Object((1,3,6,1,4,1,248,100,1,3,600,9,2,1,2),_CpuTemperature_Type())
cpuTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:cpuTemperature.setStatus(_A)
if mibBuilder.loadTexts:cpuTemperature.setUnits("'C")
_HmITSysMemoryMib_ObjectIdentity=ObjectIdentity
hmITSysMemoryMib=_HmITSysMemoryMib_ObjectIdentity((1,3,6,1,4,1,248,100,1,3,600,10))
_MemoryTable_Object=MibTable
memoryTable=_MemoryTable_Object((1,3,6,1,4,1,248,100,1,3,600,10,1))
if mibBuilder.loadTexts:memoryTable.setStatus(_A)
_MemoryEntry_Object=MibTableRow
memoryEntry=_MemoryEntry_Object((1,3,6,1,4,1,248,100,1,3,600,10,1,1))
memoryEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:memoryEntry.setStatus(_A)
class _MemIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MemIndex_Type.__name__=_C
_MemIndex_Object=MibTableColumn
memIndex=_MemIndex_Object((1,3,6,1,4,1,248,100,1,3,600,10,1,1,1),_MemIndex_Type())
memIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:memIndex.setStatus(_A)
class _MemBytesFree_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MemBytesFree_Type.__name__=_F
_MemBytesFree_Object=MibTableColumn
memBytesFree=_MemBytesFree_Object((1,3,6,1,4,1,248,100,1,3,600,10,1,1,2),_MemBytesFree_Type())
memBytesFree.setMaxAccess(_B)
if mibBuilder.loadTexts:memBytesFree.setStatus(_A)
class _MemBlocksFree_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MemBlocksFree_Type.__name__=_F
_MemBlocksFree_Object=MibTableColumn
memBlocksFree=_MemBlocksFree_Object((1,3,6,1,4,1,248,100,1,3,600,10,1,1,3),_MemBlocksFree_Type())
memBlocksFree.setMaxAccess(_B)
if mibBuilder.loadTexts:memBlocksFree.setStatus(_A)
class _MemAvgBlockSizeFree_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MemAvgBlockSizeFree_Type.__name__=_F
_MemAvgBlockSizeFree_Object=MibTableColumn
memAvgBlockSizeFree=_MemAvgBlockSizeFree_Object((1,3,6,1,4,1,248,100,1,3,600,10,1,1,4),_MemAvgBlockSizeFree_Type())
memAvgBlockSizeFree.setMaxAccess(_B)
if mibBuilder.loadTexts:memAvgBlockSizeFree.setStatus(_A)
class _MemMaxBlockSizeFree_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MemMaxBlockSizeFree_Type.__name__=_F
_MemMaxBlockSizeFree_Object=MibTableColumn
memMaxBlockSizeFree=_MemMaxBlockSizeFree_Object((1,3,6,1,4,1,248,100,1,3,600,10,1,1,5),_MemMaxBlockSizeFree_Type())
memMaxBlockSizeFree.setMaxAccess(_B)
if mibBuilder.loadTexts:memMaxBlockSizeFree.setStatus(_A)
class _MemBytesAlloc_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MemBytesAlloc_Type.__name__=_F
_MemBytesAlloc_Object=MibTableColumn
memBytesAlloc=_MemBytesAlloc_Object((1,3,6,1,4,1,248,100,1,3,600,10,1,1,6),_MemBytesAlloc_Type())
memBytesAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:memBytesAlloc.setStatus(_A)
class _MemBlocksAlloc_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MemBlocksAlloc_Type.__name__=_F
_MemBlocksAlloc_Object=MibTableColumn
memBlocksAlloc=_MemBlocksAlloc_Object((1,3,6,1,4,1,248,100,1,3,600,10,1,1,7),_MemBlocksAlloc_Type())
memBlocksAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:memBlocksAlloc.setStatus(_A)
class _MemAvgBlockSizeAlloc_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MemAvgBlockSizeAlloc_Type.__name__=_F
_MemAvgBlockSizeAlloc_Object=MibTableColumn
memAvgBlockSizeAlloc=_MemAvgBlockSizeAlloc_Object((1,3,6,1,4,1,248,100,1,3,600,10,1,1,8),_MemAvgBlockSizeAlloc_Type())
memAvgBlockSizeAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:memAvgBlockSizeAlloc.setStatus(_A)
class _MemTotalBytes_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MemTotalBytes_Type.__name__=_F
_MemTotalBytes_Object=MibTableColumn
memTotalBytes=_MemTotalBytes_Object((1,3,6,1,4,1,248,100,1,3,600,10,1,1,9),_MemTotalBytes_Type())
memTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:memTotalBytes.setStatus(_A)
class _MemUtilization_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_MemUtilization_Type.__name__=_F
_MemUtilization_Object=MibTableColumn
memUtilization=_MemUtilization_Object((1,3,6,1,4,1,248,100,1,3,600,10,1,1,10),_MemUtilization_Type())
memUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:memUtilization.setStatus(_A)
if mibBuilder.loadTexts:memUtilization.setUnits('%')
class _CacheUtilization_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CacheUtilization_Type.__name__=_F
_CacheUtilization_Object=MibTableColumn
cacheUtilization=_CacheUtilization_Object((1,3,6,1,4,1,248,100,1,3,600,10,1,1,11),_CacheUtilization_Type())
cacheUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:cacheUtilization.setStatus(_A)
if mibBuilder.loadTexts:cacheUtilization.setUnits('%')
_MemKBytesFree_Type=Counter64
_MemKBytesFree_Object=MibTableColumn
memKBytesFree=_MemKBytesFree_Object((1,3,6,1,4,1,248,100,1,3,600,10,1,1,12),_MemKBytesFree_Type())
memKBytesFree.setMaxAccess(_B)
if mibBuilder.loadTexts:memKBytesFree.setStatus(_A)
_MemKBytesAlloc_Type=Counter64
_MemKBytesAlloc_Object=MibTableColumn
memKBytesAlloc=_MemKBytesAlloc_Object((1,3,6,1,4,1,248,100,1,3,600,10,1,1,13),_MemKBytesAlloc_Type())
memKBytesAlloc.setMaxAccess(_B)
if mibBuilder.loadTexts:memKBytesAlloc.setStatus(_A)
_MemTotalKBytes_Type=Counter64
_MemTotalKBytes_Object=MibTableColumn
memTotalKBytes=_MemTotalKBytes_Object((1,3,6,1,4,1,248,100,1,3,600,10,1,1,14),_MemTotalKBytes_Type())
memTotalKBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:memTotalKBytes.setStatus(_A)
hmITSysMemUtilizationAlarm=NotificationType((1,3,6,1,4,1,248,100,1,3,600,0,5))
if mibBuilder.loadTexts:hmITSysMemUtilizationAlarm.setStatus(_A)
hmITSysCpuUtilizationAlarm=NotificationType((1,3,6,1,4,1,248,100,1,3,600,0,6))
if mibBuilder.loadTexts:hmITSysCpuUtilizationAlarm.setStatus(_A)
hmITSysCacheUtilizationAlarm=NotificationType((1,3,6,1,4,1,248,100,1,3,600,0,7))
if mibBuilder.loadTexts:hmITSysCacheUtilizationAlarm.setStatus(_A)
hmITSysMpuCoreNormalAlarm=NotificationType((1,3,6,1,4,1,248,100,1,3,600,0,18))
if mibBuilder.loadTexts:hmITSysMpuCoreNormalAlarm.setStatus(_A)
hmITSysMpuBoardWarnAlarm=NotificationType((1,3,6,1,4,1,248,100,1,3,600,0,19))
if mibBuilder.loadTexts:hmITSysMpuBoardWarnAlarm.setStatus(_A)
hmITSysMpuBoardNormalAlarm=NotificationType((1,3,6,1,4,1,248,100,1,3,600,0,20))
if mibBuilder.loadTexts:hmITSysMpuBoardNormalAlarm.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hmITSystemMib':hmITSystemMib,'hmITSystemTrap':hmITSystemTrap,'hmITSysMemUtilizationAlarm':hmITSysMemUtilizationAlarm,'hmITSysCpuUtilizationAlarm':hmITSysCpuUtilizationAlarm,'hmITSysCacheUtilizationAlarm':hmITSysCacheUtilizationAlarm,'hmITSysMpuCoreNormalAlarm':hmITSysMpuCoreNormalAlarm,'hmITSysMpuBoardWarnAlarm':hmITSysMpuBoardWarnAlarm,'hmITSysMpuBoardNormalAlarm':hmITSysMpuBoardNormalAlarm,'hmITSysInfoMib':hmITSysInfoMib,'sysVoltage':sysVoltage,'sysCurrent':sysCurrent,'hmITSysMpuMib':hmITSysMpuMib,'mpuInfoTable':mpuInfoTable,'mpuInfoEntry':mpuInfoEntry,_L:mpuIndex,'mpuType':mpuType,'mpuDescription':mpuDescription,'mpuSerialNumber':mpuSerialNumber,'mpuSoftwareVersion':mpuSoftwareVersion,'mpuHardwareVersion':mpuHardwareVersion,'mpuFPGAVersion':mpuFPGAVersion,'mpuMonitorVersion':mpuMonitorVersion,'mpuCMMSoftwareVersion':mpuCMMSoftwareVersion,'mpuCMMHardwareVersion':mpuCMMHardwareVersion,'mpuCMMMonitorVersion':mpuCMMMonitorVersion,'mpuFlashTotalBytes':mpuFlashTotalBytes,'mpuFlashLeftBytes':mpuFlashLeftBytes,'mpuWorkingMode':mpuWorkingMode,'mpuOnlineStatus':mpuOnlineStatus,'mpuWorkingStatus':mpuWorkingStatus,'mpuPowerStatus':mpuPowerStatus,'mpuSynchronizationStatus':mpuSynchronizationStatus,'mpuCFStatus':mpuCFStatus,'mpuTemperature':mpuTemperature,'mpuSubSlotNumber':mpuSubSlotNumber,'hmITSysMpuUserSerialNumber':hmITSysMpuUserSerialNumber,'mpuModel':mpuModel,'hmITSysSubSlotMib':hmITSysSubSlotMib,'subSlotTable':subSlotTable,'subSlotEntry':subSlotEntry,_M:subSlotParentIndex,_N:subSlotIndex,'subSlotCardType':subSlotCardType,'subSlotPortNumber':subSlotPortNumber,'subSlotOnlineStatus':subSlotOnlineStatus,'hmITSysPortMib':hmITSysPortMib,'portInfoTable':portInfoTable,'portInfoEntry':portInfoEntry,_O:portSlotIndex,_P:portSubSlotIndex,_Q:portIndex,'portType':portType,'portLinkStatus':portLinkStatus,'portOnlineStatus':portOnlineStatus,'hmITSysPowerMib':hmITSysPowerMib,'powerInfoTable':powerInfoTable,'powerInfoEntry':powerInfoEntry,_R:powerIndex,'powerType':powerType,'powerDescription':powerDescription,'powerSerialNumber':powerSerialNumber,'powerCMMSoftwareVersion':powerCMMSoftwareVersion,'powerCMMHardwareVersion':powerCMMHardwareVersion,'powerCMMMonitorVersion':powerCMMMonitorVersion,'powerOnlineStatus':powerOnlineStatus,'powerWorkingStatus':powerWorkingStatus,'powerAlarmStatus':powerAlarmStatus,'powerVoltageInput':powerVoltageInput,'powerVoltageOutput':powerVoltageOutput,'powerCurrentInput':powerCurrentInput,'powerCurrentOutput':powerCurrentOutput,'powerUserSerialNumber':powerUserSerialNumber,'powerName':powerName,'hmITSysFanCardMib':hmITSysFanCardMib,'fanCardInfoTable':fanCardInfoTable,'fanCardInfoEntry':fanCardInfoEntry,_T:fanCardIndex,'fanCardDescription':fanCardDescription,'fanCardSerialNumber':fanCardSerialNumber,'fanCardCMMSoftwareVersion':fanCardCMMSoftwareVersion,'fanCardCMMHardwareVersion':fanCardCMMHardwareVersion,'fanCardCMMMonitorVersion':fanCardCMMMonitorVersion,'fanCardOnlineStatus':fanCardOnlineStatus,'fanCardWorkingStatus':fanCardWorkingStatus,'fanCardAlarmStatus':fanCardAlarmStatus,'fanCardGrps':fanCardGrps,'fanCardNumPerGrp':fanCardNumPerGrp,'fanCardUserSerialNumber':fanCardUserSerialNumber,'fanCardName':fanCardName,'fanInfoTable':fanInfoTable,'fanInfoEntry':fanInfoEntry,_U:fanInfoIndex,_V:fanIndex,'fanStatus':fanStatus,'fanSpeed':fanSpeed,'hmITSysCpuMib':hmITSysCpuMib,'cpuUtilizationTable':cpuUtilizationTable,'cpuUtilizationEntry':cpuUtilizationEntry,_W:cpuIndex,_X:cpuCoreId,'cpuCoreUtilization':cpuCoreUtilization,'cpuPeakUtilizationPerMinute':cpuPeakUtilizationPerMinute,'cpuTemperatureTable':cpuTemperatureTable,'cpuTemperatureEntry':cpuTemperatureEntry,_Y:cpuTemperatureIndex,'cpuTemperature':cpuTemperature,'hmITSysMemoryMib':hmITSysMemoryMib,'memoryTable':memoryTable,'memoryEntry':memoryEntry,_Z:memIndex,'memBytesFree':memBytesFree,'memBlocksFree':memBlocksFree,'memAvgBlockSizeFree':memAvgBlockSizeFree,'memMaxBlockSizeFree':memMaxBlockSizeFree,'memBytesAlloc':memBytesAlloc,'memBlocksAlloc':memBlocksAlloc,'memAvgBlockSizeAlloc':memAvgBlockSizeAlloc,'memTotalBytes':memTotalBytes,'memUtilization':memUtilization,'cacheUtilization':cacheUtilization,'memKBytesFree':memKBytesFree,'memKBytesAlloc':memKBytesAlloc,'memTotalKBytes':memTotalKBytes})