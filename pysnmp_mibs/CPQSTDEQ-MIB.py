_As='cpqSePciePhySlot'
_Ar='cpqSePCIeEraseFailureType'
_Aq='cpqSePCIeDiskSerialNumber'
_Ap='cpqSePCIeDiskWearStatus'
_Ao='cpqSePCIeDiskCondition'
_An='cpqSeUSBPortDeviceFailedSlot'
_Am='cpqSeUSBPortDeviceWriteThreshold'
_Al='cpqSeUSBPortDeviceWriteErrorCount'
_Ak='cpqSeUSBPortDeviceReadThreshold'
_Aj='cpqSeUSBPortDeviceReadErrorCount'
_Ai='cpqSeCpuPowerpodStatus'
_Ah='cpqSeCpuStatus'
_Ag='cpqSeCpuCacheSize'
_Af='cpqSeLEDIndex'
_Ae='cpqSeComplexCellSlotStatusIndex'
_Ad='cpqSeCabinetUnitIndex'
_Ac='cpqSeIOCUnitIndex'
_Ab='cpqSeCellUnitIndex'
_Aa='cpqSePciMemoryIndex'
_AZ='cpqSePciMemoryFunctionIndex'
_AY='cpqSePciMemoryDeviceNumberIndex'
_AX='cpqSePciMemoryBusNumberIndex'
_AW='cpqSePciSlotDeviceNumberIndex'
_AV='cpqSePciSlotBusNumberIndex'
_AU='cpqSeFixedDiskIndex'
_AT='cpqSeFloppyDiskIndex'
_AS='cpqSeParallelPortIndex'
_AR='cpqSeSerialPortIndex'
_AQ='cpqSeOptRomAddrIndex'
_AP='cpqSeEisaInitAllocIndex'
_AO='cpqSeEisaInitFunctIndex'
_AN='cpqSeEisaInitSlotIndex'
_AM='cpqSeEisaFreeFormFunctIndex'
_AL='cpqSeEisaFreeFormSlotIndex'
_AK='cpqSeEisaPortAllocIndex'
_AJ='cpqSeEisaPortFunctIndex'
_AI='cpqSeEisaPortSlotIndex'
_AH='cpqSeEisaDmaAllocIndex'
_AG='cpqSeEisaDmaFunctIndex'
_AF='cpqSeEisaDmaSlotIndex'
_AE='cpqSeEisaIntAllocIndex'
_AD='cpqSeEisaIntFunctIndex'
_AC='cpqSeEisaIntSlotIndex'
_AB='cpqSeEisaMemAllocIndex'
_AA='cpqSeEisaMemFunctIndex'
_A9='cpqSeEisaMemSlotIndex'
_A8='cpqSeEisaFunctIndex'
_A7='cpqSeEisaFunctSlotIndex'
_A6='cpqSeEisaSlotIndex'
_A5='cpqSeCpuCacheLevelIndex'
_A4='cpqSeCpuCacheUnitIndex'
_A3='cpqSeFpuChipIndex'
_A2='cpqSeFpuUnitIndex'
_A1='cpqSeOsCommonModuleIndex'
_A0='NotificationType'
_z='cpqSePciHwLocation'
_y='cpqSePCIeDiskThresholdTemperature'
_x='cpqSePCIeDiskCurrentTemperature'
_w='cpqSeUSBPortDeviceLastSlotWithError'
_v='cpqSeCpuHwLocation'
_u='cpqSeCpuStep'
_t='cpqSeCpuName'
_s='cpqSePCCardProductInfo'
_r='cpqSePCCardDeviceInfo'
_q='enabled'
_p='cpqSeCpuExtSpeed'
_o='cpqSeCpuSpeed'
_n='cpqSePciFunctIndex'
_m='cpqSePciFunctDeviceNumberIndex'
_l='cpqSePciFunctBusNumberIndex'
_k='shareable'
_j='nonshareable'
_i='disabled'
_h='true'
_g='false'
_f='cpqSePCIeDiskHwLocation'
_e='cpqSeCpuSocketNumber'
_d='cpqSeCpuSlot'
_c='cpqSeCpuUnitIndex'
_b='cpqSeUSBPortDevicePartNumber'
_a='cpqSeUSBPortDeviceSerialNumber'
_Z='cpqSeUSBPortDeviceFWVersion'
_Y='cpqSeUSBPortDeviceModel'
_X='cpqSePCCardSlotIndex'
_W='cpqSePCIeDiskPCIFunctionIndex'
_V='cpqSePCIeDiskPCIDeviceIndex'
_U='cpqSePCIeDiskPCIBusIndex'
_T='read-write'
_S='cpqSeUSBPortDeviceName'
_R='deprecated'
_Q='cpqSeUSBPortIndex'
_P='degraded'
_O='failed'
_N='ok'
_M='OctetString'
_L='other'
_K='unknown'
_J='sysName'
_I='SNMPv2-MIB'
_H='cpqHoTrapFlags'
_G='CPQHOST-MIB'
_F='DisplayString'
_E='Integer32'
_D='optional'
_C='CPQSTDEQ-MIB'
_B='mandatory'
_A='read-only'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_M,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,cpqHoTrapFlags=mibBuilder.importSymbols(_G,'compaq',_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_I,_J)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier',_A0,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_A0,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
class TruthValue(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_g,1),(_h,2)))
_CpqStdEquipment_ObjectIdentity=ObjectIdentity
cpqStdEquipment=_CpqStdEquipment_ObjectIdentity((1,3,6,1,4,1,232,1))
_CpqSeMibRev_ObjectIdentity=ObjectIdentity
cpqSeMibRev=_CpqSeMibRev_ObjectIdentity((1,3,6,1,4,1,232,1,1))
class _CpqSeMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqSeMibRevMajor_Type.__name__=_E
_CpqSeMibRevMajor_Object=MibScalar
cpqSeMibRevMajor=_CpqSeMibRevMajor_Object((1,3,6,1,4,1,232,1,1,1),_CpqSeMibRevMajor_Type())
cpqSeMibRevMajor.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeMibRevMajor.setStatus(_B)
class _CpqSeMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeMibRevMinor_Type.__name__=_E
_CpqSeMibRevMinor_Object=MibScalar
cpqSeMibRevMinor=_CpqSeMibRevMinor_Object((1,3,6,1,4,1,232,1,1,2),_CpqSeMibRevMinor_Type())
cpqSeMibRevMinor.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeMibRevMinor.setStatus(_B)
class _CpqSeMibCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_N,2),(_P,3),(_O,4)))
_CpqSeMibCondition_Type.__name__=_E
_CpqSeMibCondition_Object=MibScalar
cpqSeMibCondition=_CpqSeMibCondition_Object((1,3,6,1,4,1,232,1,1,3),_CpqSeMibCondition_Type())
cpqSeMibCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeMibCondition.setStatus(_B)
_CpqSeComponent_ObjectIdentity=ObjectIdentity
cpqSeComponent=_CpqSeComponent_ObjectIdentity((1,3,6,1,4,1,232,1,2))
_CpqSeInterface_ObjectIdentity=ObjectIdentity
cpqSeInterface=_CpqSeInterface_ObjectIdentity((1,3,6,1,4,1,232,1,2,1))
_CpqSeOsCommon_ObjectIdentity=ObjectIdentity
cpqSeOsCommon=_CpqSeOsCommon_ObjectIdentity((1,3,6,1,4,1,232,1,2,1,4))
class _CpqSeOsCommonPollFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeOsCommonPollFreq_Type.__name__=_E
_CpqSeOsCommonPollFreq_Object=MibScalar
cpqSeOsCommonPollFreq=_CpqSeOsCommonPollFreq_Object((1,3,6,1,4,1,232,1,2,1,4,1),_CpqSeOsCommonPollFreq_Type())
cpqSeOsCommonPollFreq.setMaxAccess(_T)
if mibBuilder.loadTexts:cpqSeOsCommonPollFreq.setStatus(_B)
_CpqSeOsCommonModuleTable_Object=MibTable
cpqSeOsCommonModuleTable=_CpqSeOsCommonModuleTable_Object((1,3,6,1,4,1,232,1,2,1,4,2))
if mibBuilder.loadTexts:cpqSeOsCommonModuleTable.setStatus(_R)
_CpqSeOsCommonModuleEntry_Object=MibTableRow
cpqSeOsCommonModuleEntry=_CpqSeOsCommonModuleEntry_Object((1,3,6,1,4,1,232,1,2,1,4,2,1))
cpqSeOsCommonModuleEntry.setIndexNames((0,_C,_A1))
if mibBuilder.loadTexts:cpqSeOsCommonModuleEntry.setStatus(_R)
class _CpqSeOsCommonModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeOsCommonModuleIndex_Type.__name__=_E
_CpqSeOsCommonModuleIndex_Object=MibTableColumn
cpqSeOsCommonModuleIndex=_CpqSeOsCommonModuleIndex_Object((1,3,6,1,4,1,232,1,2,1,4,2,1,1),_CpqSeOsCommonModuleIndex_Type())
cpqSeOsCommonModuleIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeOsCommonModuleIndex.setStatus(_R)
class _CpqSeOsCommonModuleName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeOsCommonModuleName_Type.__name__=_F
_CpqSeOsCommonModuleName_Object=MibTableColumn
cpqSeOsCommonModuleName=_CpqSeOsCommonModuleName_Object((1,3,6,1,4,1,232,1,2,1,4,2,1,2),_CpqSeOsCommonModuleName_Type())
cpqSeOsCommonModuleName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeOsCommonModuleName.setStatus(_R)
class _CpqSeOsCommonModuleVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_CpqSeOsCommonModuleVersion_Type.__name__=_F
_CpqSeOsCommonModuleVersion_Object=MibTableColumn
cpqSeOsCommonModuleVersion=_CpqSeOsCommonModuleVersion_Object((1,3,6,1,4,1,232,1,2,1,4,2,1,3),_CpqSeOsCommonModuleVersion_Type())
cpqSeOsCommonModuleVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeOsCommonModuleVersion.setStatus(_R)
class _CpqSeOsCommonModuleDate_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqSeOsCommonModuleDate_Type.__name__=_M
_CpqSeOsCommonModuleDate_Object=MibTableColumn
cpqSeOsCommonModuleDate=_CpqSeOsCommonModuleDate_Object((1,3,6,1,4,1,232,1,2,1,4,2,1,4),_CpqSeOsCommonModuleDate_Type())
cpqSeOsCommonModuleDate.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeOsCommonModuleDate.setStatus(_R)
class _CpqSeOsCommonModulePurpose_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeOsCommonModulePurpose_Type.__name__=_F
_CpqSeOsCommonModulePurpose_Object=MibTableColumn
cpqSeOsCommonModulePurpose=_CpqSeOsCommonModulePurpose_Object((1,3,6,1,4,1,232,1,2,1,4,2,1,5),_CpqSeOsCommonModulePurpose_Type())
cpqSeOsCommonModulePurpose.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeOsCommonModulePurpose.setStatus(_R)
_CpqSeProcessor_ObjectIdentity=ObjectIdentity
cpqSeProcessor=_CpqSeProcessor_ObjectIdentity((1,3,6,1,4,1,232,1,2,2))
_CpqSeCpuTable_Object=MibTable
cpqSeCpuTable=_CpqSeCpuTable_Object((1,3,6,1,4,1,232,1,2,2,1))
if mibBuilder.loadTexts:cpqSeCpuTable.setStatus(_B)
_CpqSeCpuEntry_Object=MibTableRow
cpqSeCpuEntry=_CpqSeCpuEntry_Object((1,3,6,1,4,1,232,1,2,2,1,1))
cpqSeCpuEntry.setIndexNames((0,_C,_c))
if mibBuilder.loadTexts:cpqSeCpuEntry.setStatus(_B)
class _CpqSeCpuUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeCpuUnitIndex_Type.__name__=_E
_CpqSeCpuUnitIndex_Object=MibTableColumn
cpqSeCpuUnitIndex=_CpqSeCpuUnitIndex_Object((1,3,6,1,4,1,232,1,2,2,1,1,1),_CpqSeCpuUnitIndex_Type())
cpqSeCpuUnitIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuUnitIndex.setStatus(_B)
class _CpqSeCpuSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeCpuSlot_Type.__name__=_E
_CpqSeCpuSlot_Object=MibTableColumn
cpqSeCpuSlot=_CpqSeCpuSlot_Object((1,3,6,1,4,1,232,1,2,2,1,1,2),_CpqSeCpuSlot_Type())
cpqSeCpuSlot.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuSlot.setStatus(_B)
class _CpqSeCpuName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeCpuName_Type.__name__=_F
_CpqSeCpuName_Object=MibTableColumn
cpqSeCpuName=_CpqSeCpuName_Object((1,3,6,1,4,1,232,1,2,2,1,1,3),_CpqSeCpuName_Type())
cpqSeCpuName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuName.setStatus(_B)
class _CpqSeCpuSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeCpuSpeed_Type.__name__=_E
_CpqSeCpuSpeed_Object=MibTableColumn
cpqSeCpuSpeed=_CpqSeCpuSpeed_Object((1,3,6,1,4,1,232,1,2,2,1,1,4),_CpqSeCpuSpeed_Type())
cpqSeCpuSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuSpeed.setStatus(_B)
class _CpqSeCpuStep_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeCpuStep_Type.__name__=_E
_CpqSeCpuStep_Object=MibTableColumn
cpqSeCpuStep=_CpqSeCpuStep_Object((1,3,6,1,4,1,232,1,2,2,1,1,5),_CpqSeCpuStep_Type())
cpqSeCpuStep.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuStep.setStatus(_B)
class _CpqSeCpuStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_K,1),(_N,2),(_P,3),(_O,4),(_i,5)))
_CpqSeCpuStatus_Type.__name__=_E
_CpqSeCpuStatus_Object=MibTableColumn
cpqSeCpuStatus=_CpqSeCpuStatus_Object((1,3,6,1,4,1,232,1,2,2,1,1,6),_CpqSeCpuStatus_Type())
cpqSeCpuStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuStatus.setStatus(_B)
class _CpqSeCpuExtSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeCpuExtSpeed_Type.__name__=_E
_CpqSeCpuExtSpeed_Object=MibTableColumn
cpqSeCpuExtSpeed=_CpqSeCpuExtSpeed_Object((1,3,6,1,4,1,232,1,2,2,1,1,7),_CpqSeCpuExtSpeed_Type())
cpqSeCpuExtSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuExtSpeed.setStatus(_B)
class _CpqSeCpuDesigner_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_K,1),('intel',2),('amd',3),('cyrix',4),('ti',5),('nexgen',6),('compaq',7),('samsung',8),('mitsubishi',9),('mips',10)))
_CpqSeCpuDesigner_Type.__name__=_E
_CpqSeCpuDesigner_Object=MibTableColumn
cpqSeCpuDesigner=_CpqSeCpuDesigner_Object((1,3,6,1,4,1,232,1,2,2,1,1,8),_CpqSeCpuDesigner_Type())
cpqSeCpuDesigner.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuDesigner.setStatus(_B)
class _CpqSeCpuSocketNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeCpuSocketNumber_Type.__name__=_E
_CpqSeCpuSocketNumber_Object=MibTableColumn
cpqSeCpuSocketNumber=_CpqSeCpuSocketNumber_Object((1,3,6,1,4,1,232,1,2,2,1,1,9),_CpqSeCpuSocketNumber_Type())
cpqSeCpuSocketNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuSocketNumber.setStatus(_B)
class _CpqSeCpuThreshPassed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unsupported',1),(_g,2),(_h,3)))
_CpqSeCpuThreshPassed_Type.__name__=_E
_CpqSeCpuThreshPassed_Object=MibTableColumn
cpqSeCpuThreshPassed=_CpqSeCpuThreshPassed_Object((1,3,6,1,4,1,232,1,2,2,1,1,10),_CpqSeCpuThreshPassed_Type())
cpqSeCpuThreshPassed.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuThreshPassed.setStatus(_B)
class _CpqSeCpuHwLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeCpuHwLocation_Type.__name__=_F
_CpqSeCpuHwLocation_Object=MibTableColumn
cpqSeCpuHwLocation=_CpqSeCpuHwLocation_Object((1,3,6,1,4,1,232,1,2,2,1,1,11),_CpqSeCpuHwLocation_Type())
cpqSeCpuHwLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuHwLocation.setStatus(_D)
class _CpqSeCpuCellTablePtr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_CpqSeCpuCellTablePtr_Type.__name__=_E
_CpqSeCpuCellTablePtr_Object=MibTableColumn
cpqSeCpuCellTablePtr=_CpqSeCpuCellTablePtr_Object((1,3,6,1,4,1,232,1,2,2,1,1,12),_CpqSeCpuCellTablePtr_Type())
cpqSeCpuCellTablePtr.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuCellTablePtr.setStatus(_D)
class _CpqSeCpuPowerpodStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notfailed',1),(_O,2)))
_CpqSeCpuPowerpodStatus_Type.__name__=_E
_CpqSeCpuPowerpodStatus_Object=MibTableColumn
cpqSeCpuPowerpodStatus=_CpqSeCpuPowerpodStatus_Object((1,3,6,1,4,1,232,1,2,2,1,1,13),_CpqSeCpuPowerpodStatus_Type())
cpqSeCpuPowerpodStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuPowerpodStatus.setStatus(_D)
class _CpqSeCpuArchitectureRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeCpuArchitectureRevision_Type.__name__=_F
_CpqSeCpuArchitectureRevision_Object=MibTableColumn
cpqSeCpuArchitectureRevision=_CpqSeCpuArchitectureRevision_Object((1,3,6,1,4,1,232,1,2,2,1,1,14),_CpqSeCpuArchitectureRevision_Type())
cpqSeCpuArchitectureRevision.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuArchitectureRevision.setStatus(_D)
_CpqSeCpuCore_Type=Integer32
_CpqSeCpuCore_Object=MibTableColumn
cpqSeCpuCore=_CpqSeCpuCore_Object((1,3,6,1,4,1,232,1,2,2,1,1,15),_CpqSeCpuCore_Type())
cpqSeCpuCore.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuCore.setStatus(_D)
class _CpqSeCPUSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeCPUSerialNumber_Type.__name__=_F
_CpqSeCPUSerialNumber_Object=MibTableColumn
cpqSeCPUSerialNumber=_CpqSeCPUSerialNumber_Object((1,3,6,1,4,1,232,1,2,2,1,1,16),_CpqSeCPUSerialNumber_Type())
cpqSeCPUSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCPUSerialNumber.setStatus(_D)
class _CpqSeCPUPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeCPUPartNumber_Type.__name__=_F
_CpqSeCPUPartNumber_Object=MibTableColumn
cpqSeCPUPartNumber=_CpqSeCPUPartNumber_Object((1,3,6,1,4,1,232,1,2,2,1,1,17),_CpqSeCPUPartNumber_Type())
cpqSeCPUPartNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCPUPartNumber.setStatus(_D)
class _CpqSeCPUSerialNumberMfgr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeCPUSerialNumberMfgr_Type.__name__=_F
_CpqSeCPUSerialNumberMfgr_Object=MibTableColumn
cpqSeCPUSerialNumberMfgr=_CpqSeCPUSerialNumberMfgr_Object((1,3,6,1,4,1,232,1,2,2,1,1,18),_CpqSeCPUSerialNumberMfgr_Type())
cpqSeCPUSerialNumberMfgr.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCPUSerialNumberMfgr.setStatus(_D)
class _CpqSeCPUPartNumberMfgr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeCPUPartNumberMfgr_Type.__name__=_F
_CpqSeCPUPartNumberMfgr_Object=MibTableColumn
cpqSeCPUPartNumberMfgr=_CpqSeCPUPartNumberMfgr_Object((1,3,6,1,4,1,232,1,2,2,1,1,19),_CpqSeCPUPartNumberMfgr_Type())
cpqSeCPUPartNumberMfgr.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCPUPartNumberMfgr.setStatus(_D)
class _CpqSeCPUCoreIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeCPUCoreIndex_Type.__name__=_E
_CpqSeCPUCoreIndex_Object=MibTableColumn
cpqSeCPUCoreIndex=_CpqSeCPUCoreIndex_Object((1,3,6,1,4,1,232,1,2,2,1,1,20),_CpqSeCPUCoreIndex_Type())
cpqSeCPUCoreIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCPUCoreIndex.setStatus(_D)
class _CpqSeCPUMaxSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeCPUMaxSpeed_Type.__name__=_E
_CpqSeCPUMaxSpeed_Object=MibTableColumn
cpqSeCPUMaxSpeed=_CpqSeCPUMaxSpeed_Object((1,3,6,1,4,1,232,1,2,2,1,1,21),_CpqSeCPUMaxSpeed_Type())
cpqSeCPUMaxSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCPUMaxSpeed.setStatus(_D)
class _CpqSeCPUCoreThreadIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeCPUCoreThreadIndex_Type.__name__=_E
_CpqSeCPUCoreThreadIndex_Object=MibTableColumn
cpqSeCPUCoreThreadIndex=_CpqSeCPUCoreThreadIndex_Object((1,3,6,1,4,1,232,1,2,2,1,1,22),_CpqSeCPUCoreThreadIndex_Type())
cpqSeCPUCoreThreadIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCPUCoreThreadIndex.setStatus(_D)
class _CpqSeCPUChipGenerationName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeCPUChipGenerationName_Type.__name__=_F
_CpqSeCPUChipGenerationName_Object=MibTableColumn
cpqSeCPUChipGenerationName=_CpqSeCPUChipGenerationName_Object((1,3,6,1,4,1,232,1,2,2,1,1,23),_CpqSeCPUChipGenerationName_Type())
cpqSeCPUChipGenerationName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCPUChipGenerationName.setStatus(_D)
class _CpqSeCPUMultiThreadStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_q,2),(_i,3)))
_CpqSeCPUMultiThreadStatus_Type.__name__=_E
_CpqSeCPUMultiThreadStatus_Object=MibTableColumn
cpqSeCPUMultiThreadStatus=_CpqSeCPUMultiThreadStatus_Object((1,3,6,1,4,1,232,1,2,2,1,1,24),_CpqSeCPUMultiThreadStatus_Type())
cpqSeCPUMultiThreadStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCPUMultiThreadStatus.setStatus(_D)
class _CpqSeCPUCoreMaxThreads_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeCPUCoreMaxThreads_Type.__name__=_E
_CpqSeCPUCoreMaxThreads_Object=MibTableColumn
cpqSeCPUCoreMaxThreads=_CpqSeCPUCoreMaxThreads_Object((1,3,6,1,4,1,232,1,2,2,1,1,25),_CpqSeCPUCoreMaxThreads_Type())
cpqSeCPUCoreMaxThreads.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCPUCoreMaxThreads.setStatus(_D)
class _CpqSeCpuLowPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('lowpowered',2),('normalpowered',3),('highpowered',4)))
_CpqSeCpuLowPowerStatus_Type.__name__=_E
_CpqSeCpuLowPowerStatus_Object=MibTableColumn
cpqSeCpuLowPowerStatus=_CpqSeCpuLowPowerStatus_Object((1,3,6,1,4,1,232,1,2,2,1,1,26),_CpqSeCpuLowPowerStatus_Type())
cpqSeCpuLowPowerStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuLowPowerStatus.setStatus(_B)
class _CpqSeCpuPrimary_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_g,2),(_h,3)))
_CpqSeCpuPrimary_Type.__name__=_E
_CpqSeCpuPrimary_Object=MibTableColumn
cpqSeCpuPrimary=_CpqSeCpuPrimary_Object((1,3,6,1,4,1,232,1,2,2,1,1,27),_CpqSeCpuPrimary_Type())
cpqSeCpuPrimary.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuPrimary.setStatus(_B)
_CpqSeCpuCoreSteppingText_Type=DisplayString
_CpqSeCpuCoreSteppingText_Object=MibTableColumn
cpqSeCpuCoreSteppingText=_CpqSeCpuCoreSteppingText_Object((1,3,6,1,4,1,232,1,2,2,1,1,28),_CpqSeCpuCoreSteppingText_Type())
cpqSeCpuCoreSteppingText.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuCoreSteppingText.setStatus(_D)
_CpqSeCpuCurrentPerformanceState_Type=Integer32
_CpqSeCpuCurrentPerformanceState_Object=MibTableColumn
cpqSeCpuCurrentPerformanceState=_CpqSeCpuCurrentPerformanceState_Object((1,3,6,1,4,1,232,1,2,2,1,1,29),_CpqSeCpuCurrentPerformanceState_Type())
cpqSeCpuCurrentPerformanceState.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuCurrentPerformanceState.setStatus(_D)
_CpqSeCpuMinPerformanceState_Type=Integer32
_CpqSeCpuMinPerformanceState_Object=MibTableColumn
cpqSeCpuMinPerformanceState=_CpqSeCpuMinPerformanceState_Object((1,3,6,1,4,1,232,1,2,2,1,1,30),_CpqSeCpuMinPerformanceState_Type())
cpqSeCpuMinPerformanceState.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuMinPerformanceState.setStatus(_D)
_CpqSeCpuMaxPerformanceState_Type=Integer32
_CpqSeCpuMaxPerformanceState_Object=MibTableColumn
cpqSeCpuMaxPerformanceState=_CpqSeCpuMaxPerformanceState_Object((1,3,6,1,4,1,232,1,2,2,1,1,31),_CpqSeCpuMaxPerformanceState_Type())
cpqSeCpuMaxPerformanceState.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuMaxPerformanceState.setStatus(_D)
_CpqSeFpuTable_Object=MibTable
cpqSeFpuTable=_CpqSeFpuTable_Object((1,3,6,1,4,1,232,1,2,2,2))
if mibBuilder.loadTexts:cpqSeFpuTable.setStatus(_B)
_CpqSeFpuEntry_Object=MibTableRow
cpqSeFpuEntry=_CpqSeFpuEntry_Object((1,3,6,1,4,1,232,1,2,2,2,1))
cpqSeFpuEntry.setIndexNames((0,_C,_A2),(0,_C,_A3))
if mibBuilder.loadTexts:cpqSeFpuEntry.setStatus(_B)
class _CpqSeFpuUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeFpuUnitIndex_Type.__name__=_E
_CpqSeFpuUnitIndex_Object=MibTableColumn
cpqSeFpuUnitIndex=_CpqSeFpuUnitIndex_Object((1,3,6,1,4,1,232,1,2,2,2,1,1),_CpqSeFpuUnitIndex_Type())
cpqSeFpuUnitIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeFpuUnitIndex.setStatus(_B)
class _CpqSeFpuChipIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeFpuChipIndex_Type.__name__=_E
_CpqSeFpuChipIndex_Object=MibTableColumn
cpqSeFpuChipIndex=_CpqSeFpuChipIndex_Object((1,3,6,1,4,1,232,1,2,2,2,1,2),_CpqSeFpuChipIndex_Type())
cpqSeFpuChipIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeFpuChipIndex.setStatus(_B)
class _CpqSeFpuSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeFpuSlot_Type.__name__=_E
_CpqSeFpuSlot_Object=MibTableColumn
cpqSeFpuSlot=_CpqSeFpuSlot_Object((1,3,6,1,4,1,232,1,2,2,2,1,3),_CpqSeFpuSlot_Type())
cpqSeFpuSlot.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeFpuSlot.setStatus(_B)
class _CpqSeFpuName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeFpuName_Type.__name__=_F
_CpqSeFpuName_Object=MibTableColumn
cpqSeFpuName=_CpqSeFpuName_Object((1,3,6,1,4,1,232,1,2,2,2,1,4),_CpqSeFpuName_Type())
cpqSeFpuName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeFpuName.setStatus(_B)
class _CpqSeFpuSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeFpuSpeed_Type.__name__=_E
_CpqSeFpuSpeed_Object=MibTableColumn
cpqSeFpuSpeed=_CpqSeFpuSpeed_Object((1,3,6,1,4,1,232,1,2,2,2,1,5),_CpqSeFpuSpeed_Type())
cpqSeFpuSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeFpuSpeed.setStatus(_B)
class _CpqSeFpuType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('embedded',2),('external',3)))
_CpqSeFpuType_Type.__name__=_E
_CpqSeFpuType_Object=MibTableColumn
cpqSeFpuType=_CpqSeFpuType_Object((1,3,6,1,4,1,232,1,2,2,2,1,6),_CpqSeFpuType_Type())
cpqSeFpuType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeFpuType.setStatus(_B)
class _CpqSeFpuHwLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeFpuHwLocation_Type.__name__=_F
_CpqSeFpuHwLocation_Object=MibTableColumn
cpqSeFpuHwLocation=_CpqSeFpuHwLocation_Object((1,3,6,1,4,1,232,1,2,2,2,1,7),_CpqSeFpuHwLocation_Type())
cpqSeFpuHwLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeFpuHwLocation.setStatus(_D)
_CpqSeCpuCacheTable_Object=MibTable
cpqSeCpuCacheTable=_CpqSeCpuCacheTable_Object((1,3,6,1,4,1,232,1,2,2,3))
if mibBuilder.loadTexts:cpqSeCpuCacheTable.setStatus(_B)
_CpqSeCpuCacheEntry_Object=MibTableRow
cpqSeCpuCacheEntry=_CpqSeCpuCacheEntry_Object((1,3,6,1,4,1,232,1,2,2,3,1))
cpqSeCpuCacheEntry.setIndexNames((0,_C,_A4),(0,_C,_A5))
if mibBuilder.loadTexts:cpqSeCpuCacheEntry.setStatus(_B)
class _CpqSeCpuCacheUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeCpuCacheUnitIndex_Type.__name__=_E
_CpqSeCpuCacheUnitIndex_Object=MibTableColumn
cpqSeCpuCacheUnitIndex=_CpqSeCpuCacheUnitIndex_Object((1,3,6,1,4,1,232,1,2,2,3,1,1),_CpqSeCpuCacheUnitIndex_Type())
cpqSeCpuCacheUnitIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuCacheUnitIndex.setStatus(_B)
class _CpqSeCpuCacheLevelIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeCpuCacheLevelIndex_Type.__name__=_E
_CpqSeCpuCacheLevelIndex_Object=MibTableColumn
cpqSeCpuCacheLevelIndex=_CpqSeCpuCacheLevelIndex_Object((1,3,6,1,4,1,232,1,2,2,3,1,2),_CpqSeCpuCacheLevelIndex_Type())
cpqSeCpuCacheLevelIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuCacheLevelIndex.setStatus(_B)
class _CpqSeCpuCacheSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqSeCpuCacheSize_Type.__name__=_E
_CpqSeCpuCacheSize_Object=MibTableColumn
cpqSeCpuCacheSize=_CpqSeCpuCacheSize_Object((1,3,6,1,4,1,232,1,2,2,3,1,3),_CpqSeCpuCacheSize_Type())
cpqSeCpuCacheSize.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuCacheSize.setStatus(_B)
class _CpqSeCpuCacheSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeCpuCacheSpeed_Type.__name__=_E
_CpqSeCpuCacheSpeed_Object=MibTableColumn
cpqSeCpuCacheSpeed=_CpqSeCpuCacheSpeed_Object((1,3,6,1,4,1,232,1,2,2,3,1,4),_CpqSeCpuCacheSpeed_Type())
cpqSeCpuCacheSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuCacheSpeed.setStatus(_B)
class _CpqSeCpuCacheStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_N,2),(_P,3),(_O,4)))
_CpqSeCpuCacheStatus_Type.__name__=_E
_CpqSeCpuCacheStatus_Object=MibTableColumn
cpqSeCpuCacheStatus=_CpqSeCpuCacheStatus_Object((1,3,6,1,4,1,232,1,2,2,3,1,5),_CpqSeCpuCacheStatus_Type())
cpqSeCpuCacheStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuCacheStatus.setStatus(_B)
class _CpqSeCpuCacheWritePolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('write-back',2),('write-through',3),('variesWithMemoryAddress',4)))
_CpqSeCpuCacheWritePolicy_Type.__name__=_E
_CpqSeCpuCacheWritePolicy_Object=MibTableColumn
cpqSeCpuCacheWritePolicy=_CpqSeCpuCacheWritePolicy_Object((1,3,6,1,4,1,232,1,2,2,3,1,6),_CpqSeCpuCacheWritePolicy_Type())
cpqSeCpuCacheWritePolicy.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuCacheWritePolicy.setStatus(_B)
class _CpqSeCpuCacheHwLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeCpuCacheHwLocation_Type.__name__=_F
_CpqSeCpuCacheHwLocation_Object=MibTableColumn
cpqSeCpuCacheHwLocation=_CpqSeCpuCacheHwLocation_Object((1,3,6,1,4,1,232,1,2,2,3,1,7),_CpqSeCpuCacheHwLocation_Type())
cpqSeCpuCacheHwLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuCacheHwLocation.setStatus(_D)
class _CpqSeCpuCacheCpuSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeCpuCacheCpuSlot_Type.__name__=_E
_CpqSeCpuCacheCpuSlot_Object=MibTableColumn
cpqSeCpuCacheCpuSlot=_CpqSeCpuCacheCpuSlot_Object((1,3,6,1,4,1,232,1,2,2,3,1,8),_CpqSeCpuCacheCpuSlot_Type())
cpqSeCpuCacheCpuSlot.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuCacheCpuSlot.setStatus(_D)
_CpqSeCpuCacheCpuCoreIndex_Type=Integer32
_CpqSeCpuCacheCpuCoreIndex_Object=MibTableColumn
cpqSeCpuCacheCpuCoreIndex=_CpqSeCpuCacheCpuCoreIndex_Object((1,3,6,1,4,1,232,1,2,2,3,1,9),_CpqSeCpuCacheCpuCoreIndex_Type())
cpqSeCpuCacheCpuCoreIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuCacheCpuCoreIndex.setStatus(_D)
class _CpqSeCpuCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_N,2),(_P,3),(_O,4)))
_CpqSeCpuCondition_Type.__name__=_E
_CpqSeCpuCondition_Object=MibScalar
cpqSeCpuCondition=_CpqSeCpuCondition_Object((1,3,6,1,4,1,232,1,2,2,4),_CpqSeCpuCondition_Type())
cpqSeCpuCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCpuCondition.setStatus(_B)
_CpqSeMemory_ObjectIdentity=ObjectIdentity
cpqSeMemory=_CpqSeMemory_ObjectIdentity((1,3,6,1,4,1,232,1,2,3))
class _CpqSeBaseMem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeBaseMem_Type.__name__=_E
_CpqSeBaseMem_Object=MibScalar
cpqSeBaseMem=_CpqSeBaseMem_Object((1,3,6,1,4,1,232,1,2,3,1),_CpqSeBaseMem_Type())
cpqSeBaseMem.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeBaseMem.setStatus(_B)
class _CpqSeTotalMem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqSeTotalMem_Type.__name__=_E
_CpqSeTotalMem_Object=MibScalar
cpqSeTotalMem=_CpqSeTotalMem_Object((1,3,6,1,4,1,232,1,2,3,2),_CpqSeTotalMem_Type())
cpqSeTotalMem.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeTotalMem.setStatus(_B)
class _CpqSeTotalMemMB_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqSeTotalMemMB_Type.__name__=_E
_CpqSeTotalMemMB_Object=MibScalar
cpqSeTotalMemMB=_CpqSeTotalMemMB_Object((1,3,6,1,4,1,232,1,2,3,3),_CpqSeTotalMemMB_Type())
cpqSeTotalMemMB.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeTotalMemMB.setStatus(_B)
_CpqSeIsaCmos_ObjectIdentity=ObjectIdentity
cpqSeIsaCmos=_CpqSeIsaCmos_ObjectIdentity((1,3,6,1,4,1,232,1,2,4))
class _CpqSeIsaCmosRaw_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_CpqSeIsaCmosRaw_Type.__name__=_M
_CpqSeIsaCmosRaw_Object=MibScalar
cpqSeIsaCmosRaw=_CpqSeIsaCmosRaw_Object((1,3,6,1,4,1,232,1,2,4,1),_CpqSeIsaCmosRaw_Type())
cpqSeIsaCmosRaw.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeIsaCmosRaw.setStatus(_B)
_CpqSeEisaNvram_ObjectIdentity=ObjectIdentity
cpqSeEisaNvram=_CpqSeEisaNvram_ObjectIdentity((1,3,6,1,4,1,232,1,2,5))
_CpqSeEisaSlotTable_Object=MibTable
cpqSeEisaSlotTable=_CpqSeEisaSlotTable_Object((1,3,6,1,4,1,232,1,2,5,1))
if mibBuilder.loadTexts:cpqSeEisaSlotTable.setStatus(_B)
_CpqSeEisaSlotEntry_Object=MibTableRow
cpqSeEisaSlotEntry=_CpqSeEisaSlotEntry_Object((1,3,6,1,4,1,232,1,2,5,1,1))
cpqSeEisaSlotEntry.setIndexNames((0,_C,_A6))
if mibBuilder.loadTexts:cpqSeEisaSlotEntry.setStatus(_B)
class _CpqSeEisaSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeEisaSlotIndex_Type.__name__=_E
_CpqSeEisaSlotIndex_Object=MibTableColumn
cpqSeEisaSlotIndex=_CpqSeEisaSlotIndex_Object((1,3,6,1,4,1,232,1,2,5,1,1,1),_CpqSeEisaSlotIndex_Type())
cpqSeEisaSlotIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaSlotIndex.setStatus(_B)
class _CpqSeEisaSlotRaw_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(12,12));fixedLength=12
_CpqSeEisaSlotRaw_Type.__name__=_M
_CpqSeEisaSlotRaw_Object=MibTableColumn
cpqSeEisaSlotRaw=_CpqSeEisaSlotRaw_Object((1,3,6,1,4,1,232,1,2,5,1,1,2),_CpqSeEisaSlotRaw_Type())
cpqSeEisaSlotRaw.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaSlotRaw.setStatus(_B)
class _CpqSeEisaSlotBoardId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(7,7));fixedLength=7
_CpqSeEisaSlotBoardId_Type.__name__=_F
_CpqSeEisaSlotBoardId_Object=MibTableColumn
cpqSeEisaSlotBoardId=_CpqSeEisaSlotBoardId_Object((1,3,6,1,4,1,232,1,2,5,1,1,3),_CpqSeEisaSlotBoardId_Type())
cpqSeEisaSlotBoardId.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaSlotBoardId.setStatus(_B)
class _CpqSeEisaSlotBoardName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeEisaSlotBoardName_Type.__name__=_F
_CpqSeEisaSlotBoardName_Object=MibTableColumn
cpqSeEisaSlotBoardName=_CpqSeEisaSlotBoardName_Object((1,3,6,1,4,1,232,1,2,5,1,1,4),_CpqSeEisaSlotBoardName_Type())
cpqSeEisaSlotBoardName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaSlotBoardName.setStatus(_B)
class _CpqSeEisaSlotCfRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_CpqSeEisaSlotCfRev_Type.__name__=_F
_CpqSeEisaSlotCfRev_Object=MibTableColumn
cpqSeEisaSlotCfRev=_CpqSeEisaSlotCfRev_Object((1,3,6,1,4,1,232,1,2,5,1,1,5),_CpqSeEisaSlotCfRev_Type())
cpqSeEisaSlotCfRev.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaSlotCfRev.setStatus(_B)
class _CpqSeEisaSlotType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_K,1),('isa8Bit',2),('isa16Bit',3),('eisa32Bit',4),('eisaBusMaster32Bit',5),(_L,6),('reserved',7),('reserved2',8)))
_CpqSeEisaSlotType_Type.__name__=_E
_CpqSeEisaSlotType_Object=MibTableColumn
cpqSeEisaSlotType=_CpqSeEisaSlotType_Object((1,3,6,1,4,1,232,1,2,5,1,1,6),_CpqSeEisaSlotType_Type())
cpqSeEisaSlotType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaSlotType.setStatus(_B)
_CpqSeEisaFunctTable_Object=MibTable
cpqSeEisaFunctTable=_CpqSeEisaFunctTable_Object((1,3,6,1,4,1,232,1,2,5,2))
if mibBuilder.loadTexts:cpqSeEisaFunctTable.setStatus(_B)
_CpqSeEisaFunctEntry_Object=MibTableRow
cpqSeEisaFunctEntry=_CpqSeEisaFunctEntry_Object((1,3,6,1,4,1,232,1,2,5,2,1))
cpqSeEisaFunctEntry.setIndexNames((0,_C,_A7),(0,_C,_A8))
if mibBuilder.loadTexts:cpqSeEisaFunctEntry.setStatus(_B)
class _CpqSeEisaFunctSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeEisaFunctSlotIndex_Type.__name__=_E
_CpqSeEisaFunctSlotIndex_Object=MibTableColumn
cpqSeEisaFunctSlotIndex=_CpqSeEisaFunctSlotIndex_Object((1,3,6,1,4,1,232,1,2,5,2,1,1),_CpqSeEisaFunctSlotIndex_Type())
cpqSeEisaFunctSlotIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaFunctSlotIndex.setStatus(_B)
class _CpqSeEisaFunctIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeEisaFunctIndex_Type.__name__=_E
_CpqSeEisaFunctIndex_Object=MibTableColumn
cpqSeEisaFunctIndex=_CpqSeEisaFunctIndex_Object((1,3,6,1,4,1,232,1,2,5,2,1,2),_CpqSeEisaFunctIndex_Type())
cpqSeEisaFunctIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaFunctIndex.setStatus(_B)
class _CpqSeEisaFunctStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_i,2),(_q,3)))
_CpqSeEisaFunctStatus_Type.__name__=_E
_CpqSeEisaFunctStatus_Object=MibTableColumn
cpqSeEisaFunctStatus=_CpqSeEisaFunctStatus_Object((1,3,6,1,4,1,232,1,2,5,2,1,3),_CpqSeEisaFunctStatus_Type())
cpqSeEisaFunctStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaFunctStatus.setStatus(_B)
class _CpqSeEisaFunctType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CpqSeEisaFunctType_Type.__name__=_F
_CpqSeEisaFunctType_Object=MibTableColumn
cpqSeEisaFunctType=_CpqSeEisaFunctType_Object((1,3,6,1,4,1,232,1,2,5,2,1,4),_CpqSeEisaFunctType_Type())
cpqSeEisaFunctType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaFunctType.setStatus(_B)
class _CpqSeEisaFunctCfgRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,5))
_CpqSeEisaFunctCfgRev_Type.__name__=_F
_CpqSeEisaFunctCfgRev_Object=MibTableColumn
cpqSeEisaFunctCfgRev=_CpqSeEisaFunctCfgRev_Object((1,3,6,1,4,1,232,1,2,5,2,1,5),_CpqSeEisaFunctCfgRev_Type())
cpqSeEisaFunctCfgRev.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaFunctCfgRev.setStatus(_B)
class _CpqSeEisaFunctSels_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,26))
_CpqSeEisaFunctSels_Type.__name__=_M
_CpqSeEisaFunctSels_Object=MibTableColumn
cpqSeEisaFunctSels=_CpqSeEisaFunctSels_Object((1,3,6,1,4,1,232,1,2,5,2,1,6),_CpqSeEisaFunctSels_Type())
cpqSeEisaFunctSels.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaFunctSels.setStatus(_B)
class _CpqSeEisaFunctInfo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeEisaFunctInfo_Type.__name__=_E
_CpqSeEisaFunctInfo_Object=MibTableColumn
cpqSeEisaFunctInfo=_CpqSeEisaFunctInfo_Object((1,3,6,1,4,1,232,1,2,5,2,1,7),_CpqSeEisaFunctInfo_Type())
cpqSeEisaFunctInfo.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaFunctInfo.setStatus(_B)
_CpqSeEisaMemTable_Object=MibTable
cpqSeEisaMemTable=_CpqSeEisaMemTable_Object((1,3,6,1,4,1,232,1,2,5,3))
if mibBuilder.loadTexts:cpqSeEisaMemTable.setStatus(_B)
_CpqSeEisaMemEntry_Object=MibTableRow
cpqSeEisaMemEntry=_CpqSeEisaMemEntry_Object((1,3,6,1,4,1,232,1,2,5,3,1))
cpqSeEisaMemEntry.setIndexNames((0,_C,_A9),(0,_C,_AA),(0,_C,_AB))
if mibBuilder.loadTexts:cpqSeEisaMemEntry.setStatus(_B)
class _CpqSeEisaMemSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeEisaMemSlotIndex_Type.__name__=_E
_CpqSeEisaMemSlotIndex_Object=MibTableColumn
cpqSeEisaMemSlotIndex=_CpqSeEisaMemSlotIndex_Object((1,3,6,1,4,1,232,1,2,5,3,1,1),_CpqSeEisaMemSlotIndex_Type())
cpqSeEisaMemSlotIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaMemSlotIndex.setStatus(_B)
class _CpqSeEisaMemFunctIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeEisaMemFunctIndex_Type.__name__=_E
_CpqSeEisaMemFunctIndex_Object=MibTableColumn
cpqSeEisaMemFunctIndex=_CpqSeEisaMemFunctIndex_Object((1,3,6,1,4,1,232,1,2,5,3,1,2),_CpqSeEisaMemFunctIndex_Type())
cpqSeEisaMemFunctIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaMemFunctIndex.setStatus(_B)
class _CpqSeEisaMemAllocIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeEisaMemAllocIndex_Type.__name__=_E
_CpqSeEisaMemAllocIndex_Object=MibTableColumn
cpqSeEisaMemAllocIndex=_CpqSeEisaMemAllocIndex_Object((1,3,6,1,4,1,232,1,2,5,3,1,3),_CpqSeEisaMemAllocIndex_Type())
cpqSeEisaMemAllocIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaMemAllocIndex.setStatus(_B)
_CpqSeEisaMemStartAddr_Type=Integer32
_CpqSeEisaMemStartAddr_Object=MibTableColumn
cpqSeEisaMemStartAddr=_CpqSeEisaMemStartAddr_Object((1,3,6,1,4,1,232,1,2,5,3,1,4),_CpqSeEisaMemStartAddr_Type())
cpqSeEisaMemStartAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaMemStartAddr.setStatus(_B)
class _CpqSeEisaMemSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqSeEisaMemSize_Type.__name__=_E
_CpqSeEisaMemSize_Object=MibTableColumn
cpqSeEisaMemSize=_CpqSeEisaMemSize_Object((1,3,6,1,4,1,232,1,2,5,3,1,5),_CpqSeEisaMemSize_Type())
cpqSeEisaMemSize.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaMemSize.setStatus(_B)
class _CpqSeEisaMemShare_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_j,1),(_k,2)))
_CpqSeEisaMemShare_Type.__name__=_E
_CpqSeEisaMemShare_Object=MibTableColumn
cpqSeEisaMemShare=_CpqSeEisaMemShare_Object((1,3,6,1,4,1,232,1,2,5,3,1,6),_CpqSeEisaMemShare_Type())
cpqSeEisaMemShare.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaMemShare.setStatus(_B)
class _CpqSeEisaMemType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('systemBaseOrExtended',1),('expanded',2),('virtual',3),(_L,4)))
_CpqSeEisaMemType_Type.__name__=_E
_CpqSeEisaMemType_Object=MibTableColumn
cpqSeEisaMemType=_CpqSeEisaMemType_Object((1,3,6,1,4,1,232,1,2,5,3,1,7),_CpqSeEisaMemType_Type())
cpqSeEisaMemType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaMemType.setStatus(_B)
class _CpqSeEisaMemCache_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notCached',1),('writeThroughCached',2),('writeBackCached',3)))
_CpqSeEisaMemCache_Type.__name__=_E
_CpqSeEisaMemCache_Object=MibTableColumn
cpqSeEisaMemCache=_CpqSeEisaMemCache_Object((1,3,6,1,4,1,232,1,2,5,3,1,8),_CpqSeEisaMemCache_Type())
cpqSeEisaMemCache.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaMemCache.setStatus(_B)
class _CpqSeEisaMemAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('readOnly',1),('readWrite',2)))
_CpqSeEisaMemAccess_Type.__name__=_E
_CpqSeEisaMemAccess_Object=MibTableColumn
cpqSeEisaMemAccess=_CpqSeEisaMemAccess_Object((1,3,6,1,4,1,232,1,2,5,3,1,9),_CpqSeEisaMemAccess_Type())
cpqSeEisaMemAccess.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaMemAccess.setStatus(_B)
class _CpqSeEisaMemDecode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_CpqSeEisaMemDecode_Type.__name__=_E
_CpqSeEisaMemDecode_Object=MibTableColumn
cpqSeEisaMemDecode=_CpqSeEisaMemDecode_Object((1,3,6,1,4,1,232,1,2,5,3,1,10),_CpqSeEisaMemDecode_Type())
cpqSeEisaMemDecode.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaMemDecode.setStatus(_B)
class _CpqSeEisaMemDataSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_CpqSeEisaMemDataSize_Type.__name__=_E
_CpqSeEisaMemDataSize_Object=MibTableColumn
cpqSeEisaMemDataSize=_CpqSeEisaMemDataSize_Object((1,3,6,1,4,1,232,1,2,5,3,1,11),_CpqSeEisaMemDataSize_Type())
cpqSeEisaMemDataSize.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaMemDataSize.setStatus(_B)
_CpqSeEisaIntTable_Object=MibTable
cpqSeEisaIntTable=_CpqSeEisaIntTable_Object((1,3,6,1,4,1,232,1,2,5,4))
if mibBuilder.loadTexts:cpqSeEisaIntTable.setStatus(_B)
_CpqSeEisaIntEntry_Object=MibTableRow
cpqSeEisaIntEntry=_CpqSeEisaIntEntry_Object((1,3,6,1,4,1,232,1,2,5,4,1))
cpqSeEisaIntEntry.setIndexNames((0,_C,_AC),(0,_C,_AD),(0,_C,_AE))
if mibBuilder.loadTexts:cpqSeEisaIntEntry.setStatus(_B)
class _CpqSeEisaIntSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeEisaIntSlotIndex_Type.__name__=_E
_CpqSeEisaIntSlotIndex_Object=MibTableColumn
cpqSeEisaIntSlotIndex=_CpqSeEisaIntSlotIndex_Object((1,3,6,1,4,1,232,1,2,5,4,1,1),_CpqSeEisaIntSlotIndex_Type())
cpqSeEisaIntSlotIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaIntSlotIndex.setStatus(_B)
class _CpqSeEisaIntFunctIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeEisaIntFunctIndex_Type.__name__=_E
_CpqSeEisaIntFunctIndex_Object=MibTableColumn
cpqSeEisaIntFunctIndex=_CpqSeEisaIntFunctIndex_Object((1,3,6,1,4,1,232,1,2,5,4,1,2),_CpqSeEisaIntFunctIndex_Type())
cpqSeEisaIntFunctIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaIntFunctIndex.setStatus(_B)
class _CpqSeEisaIntAllocIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeEisaIntAllocIndex_Type.__name__=_E
_CpqSeEisaIntAllocIndex_Object=MibTableColumn
cpqSeEisaIntAllocIndex=_CpqSeEisaIntAllocIndex_Object((1,3,6,1,4,1,232,1,2,5,4,1,3),_CpqSeEisaIntAllocIndex_Type())
cpqSeEisaIntAllocIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaIntAllocIndex.setStatus(_B)
class _CpqSeEisaIntNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeEisaIntNum_Type.__name__=_E
_CpqSeEisaIntNum_Object=MibTableColumn
cpqSeEisaIntNum=_CpqSeEisaIntNum_Object((1,3,6,1,4,1,232,1,2,5,4,1,4),_CpqSeEisaIntNum_Type())
cpqSeEisaIntNum.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaIntNum.setStatus(_B)
class _CpqSeEisaIntShare_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_j,1),(_k,2)))
_CpqSeEisaIntShare_Type.__name__=_E
_CpqSeEisaIntShare_Object=MibTableColumn
cpqSeEisaIntShare=_CpqSeEisaIntShare_Object((1,3,6,1,4,1,232,1,2,5,4,1,5),_CpqSeEisaIntShare_Type())
cpqSeEisaIntShare.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaIntShare.setStatus(_B)
class _CpqSeEisaIntTrigger_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('edge',1),('level',2)))
_CpqSeEisaIntTrigger_Type.__name__=_E
_CpqSeEisaIntTrigger_Object=MibTableColumn
cpqSeEisaIntTrigger=_CpqSeEisaIntTrigger_Object((1,3,6,1,4,1,232,1,2,5,4,1,6),_CpqSeEisaIntTrigger_Type())
cpqSeEisaIntTrigger.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaIntTrigger.setStatus(_B)
_CpqSeEisaDmaTable_Object=MibTable
cpqSeEisaDmaTable=_CpqSeEisaDmaTable_Object((1,3,6,1,4,1,232,1,2,5,5))
if mibBuilder.loadTexts:cpqSeEisaDmaTable.setStatus(_B)
_CpqSeEisaDmaEntry_Object=MibTableRow
cpqSeEisaDmaEntry=_CpqSeEisaDmaEntry_Object((1,3,6,1,4,1,232,1,2,5,5,1))
cpqSeEisaDmaEntry.setIndexNames((0,_C,_AF),(0,_C,_AG),(0,_C,_AH))
if mibBuilder.loadTexts:cpqSeEisaDmaEntry.setStatus(_B)
class _CpqSeEisaDmaSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeEisaDmaSlotIndex_Type.__name__=_E
_CpqSeEisaDmaSlotIndex_Object=MibTableColumn
cpqSeEisaDmaSlotIndex=_CpqSeEisaDmaSlotIndex_Object((1,3,6,1,4,1,232,1,2,5,5,1,1),_CpqSeEisaDmaSlotIndex_Type())
cpqSeEisaDmaSlotIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaDmaSlotIndex.setStatus(_B)
class _CpqSeEisaDmaFunctIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeEisaDmaFunctIndex_Type.__name__=_E
_CpqSeEisaDmaFunctIndex_Object=MibTableColumn
cpqSeEisaDmaFunctIndex=_CpqSeEisaDmaFunctIndex_Object((1,3,6,1,4,1,232,1,2,5,5,1,2),_CpqSeEisaDmaFunctIndex_Type())
cpqSeEisaDmaFunctIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaDmaFunctIndex.setStatus(_B)
class _CpqSeEisaDmaAllocIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeEisaDmaAllocIndex_Type.__name__=_E
_CpqSeEisaDmaAllocIndex_Object=MibTableColumn
cpqSeEisaDmaAllocIndex=_CpqSeEisaDmaAllocIndex_Object((1,3,6,1,4,1,232,1,2,5,5,1,3),_CpqSeEisaDmaAllocIndex_Type())
cpqSeEisaDmaAllocIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaDmaAllocIndex.setStatus(_B)
class _CpqSeEisaDmaChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeEisaDmaChannel_Type.__name__=_E
_CpqSeEisaDmaChannel_Object=MibTableColumn
cpqSeEisaDmaChannel=_CpqSeEisaDmaChannel_Object((1,3,6,1,4,1,232,1,2,5,5,1,4),_CpqSeEisaDmaChannel_Type())
cpqSeEisaDmaChannel.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaDmaChannel.setStatus(_B)
class _CpqSeEisaDmaShare_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_j,1),(_k,2)))
_CpqSeEisaDmaShare_Type.__name__=_E
_CpqSeEisaDmaShare_Object=MibTableColumn
cpqSeEisaDmaShare=_CpqSeEisaDmaShare_Object((1,3,6,1,4,1,232,1,2,5,5,1,5),_CpqSeEisaDmaShare_Type())
cpqSeEisaDmaShare.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaDmaShare.setStatus(_B)
class _CpqSeEisaDmaTiming_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('isaTiming',1),('typeA',2),('typeB',3),('burstTypeC',4)))
_CpqSeEisaDmaTiming_Type.__name__=_E
_CpqSeEisaDmaTiming_Object=MibTableColumn
cpqSeEisaDmaTiming=_CpqSeEisaDmaTiming_Object((1,3,6,1,4,1,232,1,2,5,5,1,6),_CpqSeEisaDmaTiming_Type())
cpqSeEisaDmaTiming.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaDmaTiming.setStatus(_B)
class _CpqSeEisaDmaXfer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeEisaDmaXfer_Type.__name__=_E
_CpqSeEisaDmaXfer_Object=MibTableColumn
cpqSeEisaDmaXfer=_CpqSeEisaDmaXfer_Object((1,3,6,1,4,1,232,1,2,5,5,1,7),_CpqSeEisaDmaXfer_Type())
cpqSeEisaDmaXfer.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaDmaXfer.setStatus(_B)
class _CpqSeEisaDmaXferCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('byte',1),('word',2)))
_CpqSeEisaDmaXferCount_Type.__name__=_E
_CpqSeEisaDmaXferCount_Object=MibTableColumn
cpqSeEisaDmaXferCount=_CpqSeEisaDmaXferCount_Object((1,3,6,1,4,1,232,1,2,5,5,1,8),_CpqSeEisaDmaXferCount_Type())
cpqSeEisaDmaXferCount.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaDmaXferCount.setStatus(_B)
_CpqSeEisaPortTable_Object=MibTable
cpqSeEisaPortTable=_CpqSeEisaPortTable_Object((1,3,6,1,4,1,232,1,2,5,6))
if mibBuilder.loadTexts:cpqSeEisaPortTable.setStatus(_B)
_CpqSeEisaPortEntry_Object=MibTableRow
cpqSeEisaPortEntry=_CpqSeEisaPortEntry_Object((1,3,6,1,4,1,232,1,2,5,6,1))
cpqSeEisaPortEntry.setIndexNames((0,_C,_AI),(0,_C,_AJ),(0,_C,_AK))
if mibBuilder.loadTexts:cpqSeEisaPortEntry.setStatus(_B)
class _CpqSeEisaPortSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeEisaPortSlotIndex_Type.__name__=_E
_CpqSeEisaPortSlotIndex_Object=MibTableColumn
cpqSeEisaPortSlotIndex=_CpqSeEisaPortSlotIndex_Object((1,3,6,1,4,1,232,1,2,5,6,1,1),_CpqSeEisaPortSlotIndex_Type())
cpqSeEisaPortSlotIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaPortSlotIndex.setStatus(_B)
class _CpqSeEisaPortFunctIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeEisaPortFunctIndex_Type.__name__=_E
_CpqSeEisaPortFunctIndex_Object=MibTableColumn
cpqSeEisaPortFunctIndex=_CpqSeEisaPortFunctIndex_Object((1,3,6,1,4,1,232,1,2,5,6,1,2),_CpqSeEisaPortFunctIndex_Type())
cpqSeEisaPortFunctIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaPortFunctIndex.setStatus(_B)
class _CpqSeEisaPortAllocIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeEisaPortAllocIndex_Type.__name__=_E
_CpqSeEisaPortAllocIndex_Object=MibTableColumn
cpqSeEisaPortAllocIndex=_CpqSeEisaPortAllocIndex_Object((1,3,6,1,4,1,232,1,2,5,6,1,3),_CpqSeEisaPortAllocIndex_Type())
cpqSeEisaPortAllocIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaPortAllocIndex.setStatus(_B)
_CpqSeEisaPortAddr_Type=Integer32
_CpqSeEisaPortAddr_Object=MibTableColumn
cpqSeEisaPortAddr=_CpqSeEisaPortAddr_Object((1,3,6,1,4,1,232,1,2,5,6,1,4),_CpqSeEisaPortAddr_Type())
cpqSeEisaPortAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaPortAddr.setStatus(_B)
class _CpqSeEisaPortShare_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_j,1),(_k,2)))
_CpqSeEisaPortShare_Type.__name__=_E
_CpqSeEisaPortShare_Object=MibTableColumn
cpqSeEisaPortShare=_CpqSeEisaPortShare_Object((1,3,6,1,4,1,232,1,2,5,6,1,5),_CpqSeEisaPortShare_Type())
cpqSeEisaPortShare.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaPortShare.setStatus(_B)
class _CpqSeEisaPortSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeEisaPortSize_Type.__name__=_E
_CpqSeEisaPortSize_Object=MibTableColumn
cpqSeEisaPortSize=_CpqSeEisaPortSize_Object((1,3,6,1,4,1,232,1,2,5,6,1,6),_CpqSeEisaPortSize_Type())
cpqSeEisaPortSize.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaPortSize.setStatus(_B)
_CpqSeEisaFreeFormTable_Object=MibTable
cpqSeEisaFreeFormTable=_CpqSeEisaFreeFormTable_Object((1,3,6,1,4,1,232,1,2,5,7))
if mibBuilder.loadTexts:cpqSeEisaFreeFormTable.setStatus(_B)
_CpqSeEisaFreeFormEntry_Object=MibTableRow
cpqSeEisaFreeFormEntry=_CpqSeEisaFreeFormEntry_Object((1,3,6,1,4,1,232,1,2,5,7,1))
cpqSeEisaFreeFormEntry.setIndexNames((0,_C,_AL),(0,_C,_AM))
if mibBuilder.loadTexts:cpqSeEisaFreeFormEntry.setStatus(_B)
class _CpqSeEisaFreeFormSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeEisaFreeFormSlotIndex_Type.__name__=_E
_CpqSeEisaFreeFormSlotIndex_Object=MibTableColumn
cpqSeEisaFreeFormSlotIndex=_CpqSeEisaFreeFormSlotIndex_Object((1,3,6,1,4,1,232,1,2,5,7,1,1),_CpqSeEisaFreeFormSlotIndex_Type())
cpqSeEisaFreeFormSlotIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaFreeFormSlotIndex.setStatus(_B)
class _CpqSeEisaFreeFormFunctIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeEisaFreeFormFunctIndex_Type.__name__=_E
_CpqSeEisaFreeFormFunctIndex_Object=MibTableColumn
cpqSeEisaFreeFormFunctIndex=_CpqSeEisaFreeFormFunctIndex_Object((1,3,6,1,4,1,232,1,2,5,7,1,2),_CpqSeEisaFreeFormFunctIndex_Type())
cpqSeEisaFreeFormFunctIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaFreeFormFunctIndex.setStatus(_B)
class _CpqSeEisaFreeFormValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,205))
_CpqSeEisaFreeFormValue_Type.__name__=_M
_CpqSeEisaFreeFormValue_Object=MibTableColumn
cpqSeEisaFreeFormValue=_CpqSeEisaFreeFormValue_Object((1,3,6,1,4,1,232,1,2,5,7,1,3),_CpqSeEisaFreeFormValue_Type())
cpqSeEisaFreeFormValue.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaFreeFormValue.setStatus(_B)
_CpqSeEisaInitTable_Object=MibTable
cpqSeEisaInitTable=_CpqSeEisaInitTable_Object((1,3,6,1,4,1,232,1,2,5,8))
if mibBuilder.loadTexts:cpqSeEisaInitTable.setStatus(_B)
_CpqSeEisaInitEntry_Object=MibTableRow
cpqSeEisaInitEntry=_CpqSeEisaInitEntry_Object((1,3,6,1,4,1,232,1,2,5,8,1))
cpqSeEisaInitEntry.setIndexNames((0,_C,_AN),(0,_C,_AO),(0,_C,_AP))
if mibBuilder.loadTexts:cpqSeEisaInitEntry.setStatus(_B)
class _CpqSeEisaInitSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeEisaInitSlotIndex_Type.__name__=_E
_CpqSeEisaInitSlotIndex_Object=MibTableColumn
cpqSeEisaInitSlotIndex=_CpqSeEisaInitSlotIndex_Object((1,3,6,1,4,1,232,1,2,5,8,1,1),_CpqSeEisaInitSlotIndex_Type())
cpqSeEisaInitSlotIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaInitSlotIndex.setStatus(_B)
class _CpqSeEisaInitFunctIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeEisaInitFunctIndex_Type.__name__=_E
_CpqSeEisaInitFunctIndex_Object=MibTableColumn
cpqSeEisaInitFunctIndex=_CpqSeEisaInitFunctIndex_Object((1,3,6,1,4,1,232,1,2,5,8,1,2),_CpqSeEisaInitFunctIndex_Type())
cpqSeEisaInitFunctIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaInitFunctIndex.setStatus(_B)
class _CpqSeEisaInitAllocIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeEisaInitAllocIndex_Type.__name__=_E
_CpqSeEisaInitAllocIndex_Object=MibTableColumn
cpqSeEisaInitAllocIndex=_CpqSeEisaInitAllocIndex_Object((1,3,6,1,4,1,232,1,2,5,8,1,3),_CpqSeEisaInitAllocIndex_Type())
cpqSeEisaInitAllocIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaInitAllocIndex.setStatus(_B)
class _CpqSeEisaInitUseMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('useValueOnly',1),('useValueAndMask',2)))
_CpqSeEisaInitUseMask_Type.__name__=_E
_CpqSeEisaInitUseMask_Object=MibTableColumn
cpqSeEisaInitUseMask=_CpqSeEisaInitUseMask_Object((1,3,6,1,4,1,232,1,2,5,8,1,4),_CpqSeEisaInitUseMask_Type())
cpqSeEisaInitUseMask.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaInitUseMask.setStatus(_B)
class _CpqSeEisaInitAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),('eightBitAddress',2),('sixteenBitAddress',3),('thirtyTwoBitAddress',4)))
_CpqSeEisaInitAccess_Type.__name__=_E
_CpqSeEisaInitAccess_Object=MibTableColumn
cpqSeEisaInitAccess=_CpqSeEisaInitAccess_Object((1,3,6,1,4,1,232,1,2,5,8,1,5),_CpqSeEisaInitAccess_Type())
cpqSeEisaInitAccess.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaInitAccess.setStatus(_B)
_CpqSeEisaInitAddr_Type=Integer32
_CpqSeEisaInitAddr_Object=MibTableColumn
cpqSeEisaInitAddr=_CpqSeEisaInitAddr_Object((1,3,6,1,4,1,232,1,2,5,8,1,6),_CpqSeEisaInitAddr_Type())
cpqSeEisaInitAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaInitAddr.setStatus(_B)
_CpqSeEisaInitValue_Type=Integer32
_CpqSeEisaInitValue_Object=MibTableColumn
cpqSeEisaInitValue=_CpqSeEisaInitValue_Object((1,3,6,1,4,1,232,1,2,5,8,1,7),_CpqSeEisaInitValue_Type())
cpqSeEisaInitValue.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaInitValue.setStatus(_B)
_CpqSeEisaInitMask_Type=Integer32
_CpqSeEisaInitMask_Object=MibTableColumn
cpqSeEisaInitMask=_CpqSeEisaInitMask_Object((1,3,6,1,4,1,232,1,2,5,8,1,8),_CpqSeEisaInitMask_Type())
cpqSeEisaInitMask.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeEisaInitMask.setStatus(_B)
_CpqSeRom_ObjectIdentity=ObjectIdentity
cpqSeRom=_CpqSeRom_ObjectIdentity((1,3,6,1,4,1,232,1,2,6))
class _CpqSeSysRomVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeSysRomVer_Type.__name__=_F
_CpqSeSysRomVer_Object=MibScalar
cpqSeSysRomVer=_CpqSeSysRomVer_Object((1,3,6,1,4,1,232,1,2,6,1),_CpqSeSysRomVer_Type())
cpqSeSysRomVer.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeSysRomVer.setStatus(_B)
_CpqSeOptRomTable_Object=MibTable
cpqSeOptRomTable=_CpqSeOptRomTable_Object((1,3,6,1,4,1,232,1,2,6,2))
if mibBuilder.loadTexts:cpqSeOptRomTable.setStatus(_B)
_CpqSeOptRomEntry_Object=MibTableRow
cpqSeOptRomEntry=_CpqSeOptRomEntry_Object((1,3,6,1,4,1,232,1,2,6,2,1))
cpqSeOptRomEntry.setIndexNames((0,_C,_AQ))
if mibBuilder.loadTexts:cpqSeOptRomEntry.setStatus(_B)
class _CpqSeOptRomAddrIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CpqSeOptRomAddrIndex_Type.__name__=_E
_CpqSeOptRomAddrIndex_Object=MibTableColumn
cpqSeOptRomAddrIndex=_CpqSeOptRomAddrIndex_Object((1,3,6,1,4,1,232,1,2,6,2,1,1),_CpqSeOptRomAddrIndex_Type())
cpqSeOptRomAddrIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeOptRomAddrIndex.setStatus(_B)
class _CpqSeOptRomSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqSeOptRomSize_Type.__name__=_E
_CpqSeOptRomSize_Object=MibTableColumn
cpqSeOptRomSize=_CpqSeOptRomSize_Object((1,3,6,1,4,1,232,1,2,6,2,1,2),_CpqSeOptRomSize_Type())
cpqSeOptRomSize.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeOptRomSize.setStatus(_B)
class _CpqSeBiosRomDataRaw_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(256,256));fixedLength=256
_CpqSeBiosRomDataRaw_Type.__name__=_M
_CpqSeBiosRomDataRaw_Object=MibScalar
cpqSeBiosRomDataRaw=_CpqSeBiosRomDataRaw_Object((1,3,6,1,4,1,232,1,2,6,3),_CpqSeBiosRomDataRaw_Type())
cpqSeBiosRomDataRaw.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeBiosRomDataRaw.setStatus(_B)
class _CpqSeRedundantSysRomVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeRedundantSysRomVer_Type.__name__=_F
_CpqSeRedundantSysRomVer_Object=MibScalar
cpqSeRedundantSysRomVer=_CpqSeRedundantSysRomVer_Object((1,3,6,1,4,1,232,1,2,6,4),_CpqSeRedundantSysRomVer_Type())
cpqSeRedundantSysRomVer.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeRedundantSysRomVer.setStatus(_B)
class _CpqSeSmbiosVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeSmbiosVer_Type.__name__=_F
_CpqSeSmbiosVer_Object=MibScalar
cpqSeSmbiosVer=_CpqSeSmbiosVer_Object((1,3,6,1,4,1,232,1,2,6,5),_CpqSeSmbiosVer_Type())
cpqSeSmbiosVer.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeSmbiosVer.setStatus(_B)
class _CpqSeMPFwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeMPFwVer_Type.__name__=_F
_CpqSeMPFwVer_Object=MibScalar
cpqSeMPFwVer=_CpqSeMPFwVer_Object((1,3,6,1,4,1,232,1,2,6,6),_CpqSeMPFwVer_Type())
cpqSeMPFwVer.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeMPFwVer.setStatus(_D)
class _CpqSeBMCFwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeBMCFwVer_Type.__name__=_F
_CpqSeBMCFwVer_Object=MibScalar
cpqSeBMCFwVer=_CpqSeBMCFwVer_Object((1,3,6,1,4,1,232,1,2,6,7),_CpqSeBMCFwVer_Type())
cpqSeBMCFwVer.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeBMCFwVer.setStatus(_D)
class _CpqSeHPVMFwVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeHPVMFwVer_Type.__name__=_F
_CpqSeHPVMFwVer_Object=MibScalar
cpqSeHPVMFwVer=_CpqSeHPVMFwVer_Object((1,3,6,1,4,1,232,1,2,6,8),_CpqSeHPVMFwVer_Type())
cpqSeHPVMFwVer.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeHPVMFwVer.setStatus(_D)
_CpqSeKeyboard_ObjectIdentity=ObjectIdentity
cpqSeKeyboard=_CpqSeKeyboard_ObjectIdentity((1,3,6,1,4,1,232,1,2,7))
class _CpqSeKeyboardDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeKeyboardDesc_Type.__name__=_F
_CpqSeKeyboardDesc_Object=MibScalar
cpqSeKeyboardDesc=_CpqSeKeyboardDesc_Object((1,3,6,1,4,1,232,1,2,7,1),_CpqSeKeyboardDesc_Type())
cpqSeKeyboardDesc.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeKeyboardDesc.setStatus(_B)
_CpqSeVideo_ObjectIdentity=ObjectIdentity
cpqSeVideo=_CpqSeVideo_ObjectIdentity((1,3,6,1,4,1,232,1,2,8))
class _CpqSeVideoDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeVideoDesc_Type.__name__=_F
_CpqSeVideoDesc_Object=MibScalar
cpqSeVideoDesc=_CpqSeVideoDesc_Object((1,3,6,1,4,1,232,1,2,8,1),_CpqSeVideoDesc_Type())
cpqSeVideoDesc.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeVideoDesc.setStatus(_B)
_CpqSeSerialPort_ObjectIdentity=ObjectIdentity
cpqSeSerialPort=_CpqSeSerialPort_ObjectIdentity((1,3,6,1,4,1,232,1,2,9))
_CpqSeSerialPortTable_Object=MibTable
cpqSeSerialPortTable=_CpqSeSerialPortTable_Object((1,3,6,1,4,1,232,1,2,9,1))
if mibBuilder.loadTexts:cpqSeSerialPortTable.setStatus(_B)
_CpqSeSerialPortEntry_Object=MibTableRow
cpqSeSerialPortEntry=_CpqSeSerialPortEntry_Object((1,3,6,1,4,1,232,1,2,9,1,1))
cpqSeSerialPortEntry.setIndexNames((0,_C,_AR))
if mibBuilder.loadTexts:cpqSeSerialPortEntry.setStatus(_B)
class _CpqSeSerialPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeSerialPortIndex_Type.__name__=_E
_CpqSeSerialPortIndex_Object=MibTableColumn
cpqSeSerialPortIndex=_CpqSeSerialPortIndex_Object((1,3,6,1,4,1,232,1,2,9,1,1,1),_CpqSeSerialPortIndex_Type())
cpqSeSerialPortIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeSerialPortIndex.setStatus(_B)
_CpqSeSerialPortAddr_Type=Integer32
_CpqSeSerialPortAddr_Object=MibTableColumn
cpqSeSerialPortAddr=_CpqSeSerialPortAddr_Object((1,3,6,1,4,1,232,1,2,9,1,1,2),_CpqSeSerialPortAddr_Type())
cpqSeSerialPortAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeSerialPortAddr.setStatus(_B)
class _CpqSeSerialPortDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeSerialPortDesc_Type.__name__=_F
_CpqSeSerialPortDesc_Object=MibTableColumn
cpqSeSerialPortDesc=_CpqSeSerialPortDesc_Object((1,3,6,1,4,1,232,1,2,9,1,1,3),_CpqSeSerialPortDesc_Type())
cpqSeSerialPortDesc.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeSerialPortDesc.setStatus(_B)
class _CpqSeSerialPortHwLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeSerialPortHwLocation_Type.__name__=_F
_CpqSeSerialPortHwLocation_Object=MibTableColumn
cpqSeSerialPortHwLocation=_CpqSeSerialPortHwLocation_Object((1,3,6,1,4,1,232,1,2,9,1,1,4),_CpqSeSerialPortHwLocation_Type())
cpqSeSerialPortHwLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeSerialPortHwLocation.setStatus(_D)
_CpqSeParallelPort_ObjectIdentity=ObjectIdentity
cpqSeParallelPort=_CpqSeParallelPort_ObjectIdentity((1,3,6,1,4,1,232,1,2,10))
_CpqSeParallelPortTable_Object=MibTable
cpqSeParallelPortTable=_CpqSeParallelPortTable_Object((1,3,6,1,4,1,232,1,2,10,1))
if mibBuilder.loadTexts:cpqSeParallelPortTable.setStatus(_B)
_CpqSeParallelPortEntry_Object=MibTableRow
cpqSeParallelPortEntry=_CpqSeParallelPortEntry_Object((1,3,6,1,4,1,232,1,2,10,1,1))
cpqSeParallelPortEntry.setIndexNames((0,_C,_AS))
if mibBuilder.loadTexts:cpqSeParallelPortEntry.setStatus(_B)
class _CpqSeParallelPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeParallelPortIndex_Type.__name__=_E
_CpqSeParallelPortIndex_Object=MibTableColumn
cpqSeParallelPortIndex=_CpqSeParallelPortIndex_Object((1,3,6,1,4,1,232,1,2,10,1,1,1),_CpqSeParallelPortIndex_Type())
cpqSeParallelPortIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeParallelPortIndex.setStatus(_B)
_CpqSeParallelPortAddr_Type=Integer32
_CpqSeParallelPortAddr_Object=MibTableColumn
cpqSeParallelPortAddr=_CpqSeParallelPortAddr_Object((1,3,6,1,4,1,232,1,2,10,1,1,2),_CpqSeParallelPortAddr_Type())
cpqSeParallelPortAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeParallelPortAddr.setStatus(_B)
class _CpqSeParallelPortDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeParallelPortDesc_Type.__name__=_F
_CpqSeParallelPortDesc_Object=MibTableColumn
cpqSeParallelPortDesc=_CpqSeParallelPortDesc_Object((1,3,6,1,4,1,232,1,2,10,1,1,3),_CpqSeParallelPortDesc_Type())
cpqSeParallelPortDesc.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeParallelPortDesc.setStatus(_B)
class _CpqSeParrallelPortHwLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeParrallelPortHwLocation_Type.__name__=_F
_CpqSeParrallelPortHwLocation_Object=MibTableColumn
cpqSeParrallelPortHwLocation=_CpqSeParrallelPortHwLocation_Object((1,3,6,1,4,1,232,1,2,10,1,1,4),_CpqSeParrallelPortHwLocation_Type())
cpqSeParrallelPortHwLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeParrallelPortHwLocation.setStatus(_D)
_CpqSeFloppyDisk_ObjectIdentity=ObjectIdentity
cpqSeFloppyDisk=_CpqSeFloppyDisk_ObjectIdentity((1,3,6,1,4,1,232,1,2,11))
_CpqSeFloppyDiskTable_Object=MibTable
cpqSeFloppyDiskTable=_CpqSeFloppyDiskTable_Object((1,3,6,1,4,1,232,1,2,11,1))
if mibBuilder.loadTexts:cpqSeFloppyDiskTable.setStatus(_B)
_CpqSeFloppyDiskEntry_Object=MibTableRow
cpqSeFloppyDiskEntry=_CpqSeFloppyDiskEntry_Object((1,3,6,1,4,1,232,1,2,11,1,1))
cpqSeFloppyDiskEntry.setIndexNames((0,_C,_AT))
if mibBuilder.loadTexts:cpqSeFloppyDiskEntry.setStatus(_B)
class _CpqSeFloppyDiskIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeFloppyDiskIndex_Type.__name__=_E
_CpqSeFloppyDiskIndex_Object=MibTableColumn
cpqSeFloppyDiskIndex=_CpqSeFloppyDiskIndex_Object((1,3,6,1,4,1,232,1,2,11,1,1,1),_CpqSeFloppyDiskIndex_Type())
cpqSeFloppyDiskIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeFloppyDiskIndex.setStatus(_B)
class _CpqSeFloppyDiskType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_L,1),('drive360k',2),('drive1200k',3),('drive720k',4),('drive1440k',5),('drive120mb',6)))
_CpqSeFloppyDiskType_Type.__name__=_E
_CpqSeFloppyDiskType_Object=MibTableColumn
cpqSeFloppyDiskType=_CpqSeFloppyDiskType_Object((1,3,6,1,4,1,232,1,2,11,1,1,2),_CpqSeFloppyDiskType_Type())
cpqSeFloppyDiskType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeFloppyDiskType.setStatus(_B)
class _CpqSeFloppyDiskHwLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeFloppyDiskHwLocation_Type.__name__=_F
_CpqSeFloppyDiskHwLocation_Object=MibTableColumn
cpqSeFloppyDiskHwLocation=_CpqSeFloppyDiskHwLocation_Object((1,3,6,1,4,1,232,1,2,11,1,1,3),_CpqSeFloppyDiskHwLocation_Type())
cpqSeFloppyDiskHwLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeFloppyDiskHwLocation.setStatus(_D)
_CpqSeFixedDisk_ObjectIdentity=ObjectIdentity
cpqSeFixedDisk=_CpqSeFixedDisk_ObjectIdentity((1,3,6,1,4,1,232,1,2,12))
_CpqSeFixedDiskTable_Object=MibTable
cpqSeFixedDiskTable=_CpqSeFixedDiskTable_Object((1,3,6,1,4,1,232,1,2,12,1))
if mibBuilder.loadTexts:cpqSeFixedDiskTable.setStatus(_B)
_CpqSeFixedDiskEntry_Object=MibTableRow
cpqSeFixedDiskEntry=_CpqSeFixedDiskEntry_Object((1,3,6,1,4,1,232,1,2,12,1,1))
cpqSeFixedDiskEntry.setIndexNames((0,_C,_AU))
if mibBuilder.loadTexts:cpqSeFixedDiskEntry.setStatus(_B)
class _CpqSeFixedDiskIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeFixedDiskIndex_Type.__name__=_E
_CpqSeFixedDiskIndex_Object=MibTableColumn
cpqSeFixedDiskIndex=_CpqSeFixedDiskIndex_Object((1,3,6,1,4,1,232,1,2,12,1,1,1),_CpqSeFixedDiskIndex_Type())
cpqSeFixedDiskIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeFixedDiskIndex.setStatus(_B)
class _CpqSeFixedDiskType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqSeFixedDiskType_Type.__name__=_E
_CpqSeFixedDiskType_Object=MibTableColumn
cpqSeFixedDiskType=_CpqSeFixedDiskType_Object((1,3,6,1,4,1,232,1,2,12,1,1,2),_CpqSeFixedDiskType_Type())
cpqSeFixedDiskType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeFixedDiskType.setStatus(_B)
class _CpqSeFixedDiskCyls_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqSeFixedDiskCyls_Type.__name__=_E
_CpqSeFixedDiskCyls_Object=MibTableColumn
cpqSeFixedDiskCyls=_CpqSeFixedDiskCyls_Object((1,3,6,1,4,1,232,1,2,12,1,1,3),_CpqSeFixedDiskCyls_Type())
cpqSeFixedDiskCyls.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeFixedDiskCyls.setStatus(_B)
class _CpqSeFixedDiskHeads_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqSeFixedDiskHeads_Type.__name__=_E
_CpqSeFixedDiskHeads_Object=MibTableColumn
cpqSeFixedDiskHeads=_CpqSeFixedDiskHeads_Object((1,3,6,1,4,1,232,1,2,12,1,1,4),_CpqSeFixedDiskHeads_Type())
cpqSeFixedDiskHeads.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeFixedDiskHeads.setStatus(_B)
class _CpqSeFixedDiskSectors_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqSeFixedDiskSectors_Type.__name__=_E
_CpqSeFixedDiskSectors_Object=MibTableColumn
cpqSeFixedDiskSectors=_CpqSeFixedDiskSectors_Object((1,3,6,1,4,1,232,1,2,12,1,1,5),_CpqSeFixedDiskSectors_Type())
cpqSeFixedDiskSectors.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeFixedDiskSectors.setStatus(_B)
class _CpqSeFixedDiskCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CpqSeFixedDiskCapacity_Type.__name__=_E
_CpqSeFixedDiskCapacity_Object=MibTableColumn
cpqSeFixedDiskCapacity=_CpqSeFixedDiskCapacity_Object((1,3,6,1,4,1,232,1,2,12,1,1,6),_CpqSeFixedDiskCapacity_Type())
cpqSeFixedDiskCapacity.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeFixedDiskCapacity.setStatus(_B)
class _CpqSeFixedDiskHwLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeFixedDiskHwLocation_Type.__name__=_F
_CpqSeFixedDiskHwLocation_Object=MibTableColumn
cpqSeFixedDiskHwLocation=_CpqSeFixedDiskHwLocation_Object((1,3,6,1,4,1,232,1,2,12,1,1,7),_CpqSeFixedDiskHwLocation_Type())
cpqSeFixedDiskHwLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeFixedDiskHwLocation.setStatus(_D)
_CpqSePci_ObjectIdentity=ObjectIdentity
cpqSePci=_CpqSePci_ObjectIdentity((1,3,6,1,4,1,232,1,2,13))
_CpqSePciSlotTable_Object=MibTable
cpqSePciSlotTable=_CpqSePciSlotTable_Object((1,3,6,1,4,1,232,1,2,13,1))
if mibBuilder.loadTexts:cpqSePciSlotTable.setStatus(_B)
_CpqSePciSlotEntry_Object=MibTableRow
cpqSePciSlotEntry=_CpqSePciSlotEntry_Object((1,3,6,1,4,1,232,1,2,13,1,1))
cpqSePciSlotEntry.setIndexNames((0,_C,_AV),(0,_C,_AW))
if mibBuilder.loadTexts:cpqSePciSlotEntry.setStatus(_B)
_CpqSePciSlotBusNumberIndex_Type=Integer32
_CpqSePciSlotBusNumberIndex_Object=MibTableColumn
cpqSePciSlotBusNumberIndex=_CpqSePciSlotBusNumberIndex_Object((1,3,6,1,4,1,232,1,2,13,1,1,1),_CpqSePciSlotBusNumberIndex_Type())
cpqSePciSlotBusNumberIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciSlotBusNumberIndex.setStatus(_B)
class _CpqSePciSlotDeviceNumberIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSePciSlotDeviceNumberIndex_Type.__name__=_E
_CpqSePciSlotDeviceNumberIndex_Object=MibTableColumn
cpqSePciSlotDeviceNumberIndex=_CpqSePciSlotDeviceNumberIndex_Object((1,3,6,1,4,1,232,1,2,13,1,1,2),_CpqSePciSlotDeviceNumberIndex_Type())
cpqSePciSlotDeviceNumberIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciSlotDeviceNumberIndex.setStatus(_B)
class _CpqSePciPhysSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSePciPhysSlot_Type.__name__=_E
_CpqSePciPhysSlot_Object=MibTableColumn
cpqSePciPhysSlot=_CpqSePciPhysSlot_Object((1,3,6,1,4,1,232,1,2,13,1,1,3),_CpqSePciPhysSlot_Type())
cpqSePciPhysSlot.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciPhysSlot.setStatus(_B)
class _CpqSePciSlotSubSystemID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_CpqSePciSlotSubSystemID_Type.__name__=_M
_CpqSePciSlotSubSystemID_Object=MibTableColumn
cpqSePciSlotSubSystemID=_CpqSePciSlotSubSystemID_Object((1,3,6,1,4,1,232,1,2,13,1,1,4),_CpqSePciSlotSubSystemID_Type())
cpqSePciSlotSubSystemID.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciSlotSubSystemID.setStatus(_B)
class _CpqSePciSlotBoardName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSePciSlotBoardName_Type.__name__=_F
_CpqSePciSlotBoardName_Object=MibTableColumn
cpqSePciSlotBoardName=_CpqSePciSlotBoardName_Object((1,3,6,1,4,1,232,1,2,13,1,1,5),_CpqSePciSlotBoardName_Type())
cpqSePciSlotBoardName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciSlotBoardName.setStatus(_B)
class _CpqSePciSlotWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*((_L,1),(_K,2),('thirtyTwoBit',3),('sixtyFourBit',4),('oneTwentyEightBit',5),('x1',6),('x2',7),('x4',8),('x8',9),('x12',10),('x16',11),('x32',12)))
_CpqSePciSlotWidth_Type.__name__=_E
_CpqSePciSlotWidth_Object=MibTableColumn
cpqSePciSlotWidth=_CpqSePciSlotWidth_Object((1,3,6,1,4,1,232,1,2,13,1,1,6),_CpqSePciSlotWidth_Type())
cpqSePciSlotWidth.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciSlotWidth.setStatus(_B)
class _CpqSePciSlotSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_K,2),('thirtyThreeMHz',3),('sixtySixMHz',4)))
_CpqSePciSlotSpeed_Type.__name__=_E
_CpqSePciSlotSpeed_Object=MibTableColumn
cpqSePciSlotSpeed=_CpqSePciSlotSpeed_Object((1,3,6,1,4,1,232,1,2,13,1,1,7),_CpqSePciSlotSpeed_Type())
cpqSePciSlotSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciSlotSpeed.setStatus(_R)
_CpqSePciSlotExtendedInfo_Type=Integer32
_CpqSePciSlotExtendedInfo_Object=MibTableColumn
cpqSePciSlotExtendedInfo=_CpqSePciSlotExtendedInfo_Object((1,3,6,1,4,1,232,1,2,13,1,1,8),_CpqSePciSlotExtendedInfo_Type())
cpqSePciSlotExtendedInfo.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciSlotExtendedInfo.setStatus(_B)
class _CpqSePciSlotType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_L,1),(_K,2),('pci',3),('pci66',4),('pcix',5),('pciexpress',6),('U2',7),('M2',8)))
_CpqSePciSlotType_Type.__name__=_E
_CpqSePciSlotType_Object=MibTableColumn
cpqSePciSlotType=_CpqSePciSlotType_Object((1,3,6,1,4,1,232,1,2,13,1,1,9),_CpqSePciSlotType_Type())
cpqSePciSlotType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciSlotType.setStatus(_B)
class _CpqSePciSlotCurrentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),(_K,2),('pci',3),('pci66',4),('pcix',5)))
_CpqSePciSlotCurrentMode_Type.__name__=_E
_CpqSePciSlotCurrentMode_Object=MibTableColumn
cpqSePciSlotCurrentMode=_CpqSePciSlotCurrentMode_Object((1,3,6,1,4,1,232,1,2,13,1,1,10),_CpqSePciSlotCurrentMode_Type())
cpqSePciSlotCurrentMode.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciSlotCurrentMode.setStatus(_B)
_CpqSePciMaxSlotSpeed_Type=Integer32
_CpqSePciMaxSlotSpeed_Object=MibTableColumn
cpqSePciMaxSlotSpeed=_CpqSePciMaxSlotSpeed_Object((1,3,6,1,4,1,232,1,2,13,1,1,11),_CpqSePciMaxSlotSpeed_Type())
cpqSePciMaxSlotSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciMaxSlotSpeed.setStatus(_B)
_CpqSePciXMaxSlotSpeed_Type=Integer32
_CpqSePciXMaxSlotSpeed_Object=MibTableColumn
cpqSePciXMaxSlotSpeed=_CpqSePciXMaxSlotSpeed_Object((1,3,6,1,4,1,232,1,2,13,1,1,12),_CpqSePciXMaxSlotSpeed_Type())
cpqSePciXMaxSlotSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciXMaxSlotSpeed.setStatus(_B)
_CpqSePciCurrentSlotSpeed_Type=Integer32
_CpqSePciCurrentSlotSpeed_Object=MibTableColumn
cpqSePciCurrentSlotSpeed=_CpqSePciCurrentSlotSpeed_Object((1,3,6,1,4,1,232,1,2,13,1,1,13),_CpqSePciCurrentSlotSpeed_Type())
cpqSePciCurrentSlotSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciCurrentSlotSpeed.setStatus(_B)
class _CpqSePciHwLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSePciHwLocation_Type.__name__=_F
_CpqSePciHwLocation_Object=MibTableColumn
cpqSePciHwLocation=_CpqSePciHwLocation_Object((1,3,6,1,4,1,232,1,2,13,1,1,14),_CpqSePciHwLocation_Type())
cpqSePciHwLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciHwLocation.setStatus(_D)
class _CpqSePciSlotIOCTablePtr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,19))
_CpqSePciSlotIOCTablePtr_Type.__name__=_E
_CpqSePciSlotIOCTablePtr_Object=MibTableColumn
cpqSePciSlotIOCTablePtr=_CpqSePciSlotIOCTablePtr_Object((1,3,6,1,4,1,232,1,2,13,1,1,15),_CpqSePciSlotIOCTablePtr_Type())
cpqSePciSlotIOCTablePtr.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciSlotIOCTablePtr.setStatus(_B)
_CpqSePciSlotHeaderType_Type=Integer32
_CpqSePciSlotHeaderType_Object=MibTableColumn
cpqSePciSlotHeaderType=_CpqSePciSlotHeaderType_Object((1,3,6,1,4,1,232,1,2,13,1,1,16),_CpqSePciSlotHeaderType_Type())
cpqSePciSlotHeaderType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciSlotHeaderType.setStatus(_B)
class _CpqSePciIsSlot0Embedded_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_g,2)))
_CpqSePciIsSlot0Embedded_Type.__name__=_E
_CpqSePciIsSlot0Embedded_Object=MibTableColumn
cpqSePciIsSlot0Embedded=_CpqSePciIsSlot0Embedded_Object((1,3,6,1,4,1,232,1,2,13,1,1,17),_CpqSePciIsSlot0Embedded_Type())
cpqSePciIsSlot0Embedded.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciIsSlot0Embedded.setStatus(_D)
_CpqSePcieSlotMaxLinkSpeed_Type=Integer32
_CpqSePcieSlotMaxLinkSpeed_Object=MibTableColumn
cpqSePcieSlotMaxLinkSpeed=_CpqSePcieSlotMaxLinkSpeed_Object((1,3,6,1,4,1,232,1,2,13,1,1,18),_CpqSePcieSlotMaxLinkSpeed_Type())
cpqSePcieSlotMaxLinkSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePcieSlotMaxLinkSpeed.setStatus(_D)
_CpqSePcieSlotMaxLinkWidth_Type=Integer32
_CpqSePcieSlotMaxLinkWidth_Object=MibTableColumn
cpqSePcieSlotMaxLinkWidth=_CpqSePcieSlotMaxLinkWidth_Object((1,3,6,1,4,1,232,1,2,13,1,1,19),_CpqSePcieSlotMaxLinkWidth_Type())
cpqSePcieSlotMaxLinkWidth.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePcieSlotMaxLinkWidth.setStatus(_D)
_CpqSePciFunctTable_Object=MibTable
cpqSePciFunctTable=_CpqSePciFunctTable_Object((1,3,6,1,4,1,232,1,2,13,2))
if mibBuilder.loadTexts:cpqSePciFunctTable.setStatus(_B)
_CpqSePciFunctEntry_Object=MibTableRow
cpqSePciFunctEntry=_CpqSePciFunctEntry_Object((1,3,6,1,4,1,232,1,2,13,2,1))
cpqSePciFunctEntry.setIndexNames((0,_C,_l),(0,_C,_m),(0,_C,_n))
if mibBuilder.loadTexts:cpqSePciFunctEntry.setStatus(_B)
_CpqSePciFunctBusNumberIndex_Type=Integer32
_CpqSePciFunctBusNumberIndex_Object=MibTableColumn
cpqSePciFunctBusNumberIndex=_CpqSePciFunctBusNumberIndex_Object((1,3,6,1,4,1,232,1,2,13,2,1,1),_CpqSePciFunctBusNumberIndex_Type())
cpqSePciFunctBusNumberIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciFunctBusNumberIndex.setStatus(_B)
class _CpqSePciFunctDeviceNumberIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSePciFunctDeviceNumberIndex_Type.__name__=_E
_CpqSePciFunctDeviceNumberIndex_Object=MibTableColumn
cpqSePciFunctDeviceNumberIndex=_CpqSePciFunctDeviceNumberIndex_Object((1,3,6,1,4,1,232,1,2,13,2,1,2),_CpqSePciFunctDeviceNumberIndex_Type())
cpqSePciFunctDeviceNumberIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciFunctDeviceNumberIndex.setStatus(_B)
class _CpqSePciFunctIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CpqSePciFunctIndex_Type.__name__=_E
_CpqSePciFunctIndex_Object=MibTableColumn
cpqSePciFunctIndex=_CpqSePciFunctIndex_Object((1,3,6,1,4,1,232,1,2,13,2,1,3),_CpqSePciFunctIndex_Type())
cpqSePciFunctIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciFunctIndex.setStatus(_B)
class _CpqSePciFunctClassCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_CpqSePciFunctClassCode_Type.__name__=_M
_CpqSePciFunctClassCode_Object=MibTableColumn
cpqSePciFunctClassCode=_CpqSePciFunctClassCode_Object((1,3,6,1,4,1,232,1,2,13,2,1,4),_CpqSePciFunctClassCode_Type())
cpqSePciFunctClassCode.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciFunctClassCode.setStatus(_B)
class _CpqSePciFunctClassDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CpqSePciFunctClassDescription_Type.__name__=_F
_CpqSePciFunctClassDescription_Object=MibTableColumn
cpqSePciFunctClassDescription=_CpqSePciFunctClassDescription_Object((1,3,6,1,4,1,232,1,2,13,2,1,5),_CpqSePciFunctClassDescription_Type())
cpqSePciFunctClassDescription.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciFunctClassDescription.setStatus(_B)
class _CpqSePciFunctDeviceID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSePciFunctDeviceID_Type.__name__=_E
_CpqSePciFunctDeviceID_Object=MibTableColumn
cpqSePciFunctDeviceID=_CpqSePciFunctDeviceID_Object((1,3,6,1,4,1,232,1,2,13,2,1,6),_CpqSePciFunctDeviceID_Type())
cpqSePciFunctDeviceID.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciFunctDeviceID.setStatus(_B)
class _CpqSePciFunctVendorID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSePciFunctVendorID_Type.__name__=_E
_CpqSePciFunctVendorID_Object=MibTableColumn
cpqSePciFunctVendorID=_CpqSePciFunctVendorID_Object((1,3,6,1,4,1,232,1,2,13,2,1,7),_CpqSePciFunctVendorID_Type())
cpqSePciFunctVendorID.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciFunctVendorID.setStatus(_B)
class _CpqSePciFunctRevID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSePciFunctRevID_Type.__name__=_E
_CpqSePciFunctRevID_Object=MibTableColumn
cpqSePciFunctRevID=_CpqSePciFunctRevID_Object((1,3,6,1,4,1,232,1,2,13,2,1,8),_CpqSePciFunctRevID_Type())
cpqSePciFunctRevID.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciFunctRevID.setStatus(_B)
class _CpqSePciFunctIntLine_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSePciFunctIntLine_Type.__name__=_E
_CpqSePciFunctIntLine_Object=MibTableColumn
cpqSePciFunctIntLine=_CpqSePciFunctIntLine_Object((1,3,6,1,4,1,232,1,2,13,2,1,9),_CpqSePciFunctIntLine_Type())
cpqSePciFunctIntLine.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciFunctIntLine.setStatus(_B)
class _CpqSePciFunctDevStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),(_q,2),(_i,3)))
_CpqSePciFunctDevStatus_Type.__name__=_E
_CpqSePciFunctDevStatus_Object=MibTableColumn
cpqSePciFunctDevStatus=_CpqSePciFunctDevStatus_Object((1,3,6,1,4,1,232,1,2,13,2,1,10),_CpqSePciFunctDevStatus_Type())
cpqSePciFunctDevStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciFunctDevStatus.setStatus(_B)
class _CpqSePciFunctHwLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSePciFunctHwLocation_Type.__name__=_F
_CpqSePciFunctHwLocation_Object=MibTableColumn
cpqSePciFunctHwLocation=_CpqSePciFunctHwLocation_Object((1,3,6,1,4,1,232,1,2,13,2,1,11),_CpqSePciFunctHwLocation_Type())
cpqSePciFunctHwLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciFunctHwLocation.setStatus(_D)
_CpqSePcieFunctNegotiatedLinkSpeed_Type=Integer32
_CpqSePcieFunctNegotiatedLinkSpeed_Object=MibTableColumn
cpqSePcieFunctNegotiatedLinkSpeed=_CpqSePcieFunctNegotiatedLinkSpeed_Object((1,3,6,1,4,1,232,1,2,13,2,1,12),_CpqSePcieFunctNegotiatedLinkSpeed_Type())
cpqSePcieFunctNegotiatedLinkSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePcieFunctNegotiatedLinkSpeed.setStatus(_D)
_CpqSePcieFunctNegotiatedLinkWidth_Type=Integer32
_CpqSePcieFunctNegotiatedLinkWidth_Object=MibTableColumn
cpqSePcieFunctNegotiatedLinkWidth=_CpqSePcieFunctNegotiatedLinkWidth_Object((1,3,6,1,4,1,232,1,2,13,2,1,13),_CpqSePcieFunctNegotiatedLinkWidth_Type())
cpqSePcieFunctNegotiatedLinkWidth.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePcieFunctNegotiatedLinkWidth.setStatus(_D)
_CpqSePcieFunctMaxLinkSpeed_Type=Integer32
_CpqSePcieFunctMaxLinkSpeed_Object=MibTableColumn
cpqSePcieFunctMaxLinkSpeed=_CpqSePcieFunctMaxLinkSpeed_Object((1,3,6,1,4,1,232,1,2,13,2,1,14),_CpqSePcieFunctMaxLinkSpeed_Type())
cpqSePcieFunctMaxLinkSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePcieFunctMaxLinkSpeed.setStatus(_D)
_CpqSePcieFunctMaxLinkWidth_Type=Integer32
_CpqSePcieFunctMaxLinkWidth_Object=MibTableColumn
cpqSePcieFunctMaxLinkWidth=_CpqSePcieFunctMaxLinkWidth_Object((1,3,6,1,4,1,232,1,2,13,2,1,15),_CpqSePcieFunctMaxLinkWidth_Type())
cpqSePcieFunctMaxLinkWidth.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePcieFunctMaxLinkWidth.setStatus(_D)
_CpqSePciMemoryTable_Object=MibTable
cpqSePciMemoryTable=_CpqSePciMemoryTable_Object((1,3,6,1,4,1,232,1,2,13,3))
if mibBuilder.loadTexts:cpqSePciMemoryTable.setStatus(_B)
_CpqSePciMemoryEntry_Object=MibTableRow
cpqSePciMemoryEntry=_CpqSePciMemoryEntry_Object((1,3,6,1,4,1,232,1,2,13,3,1))
cpqSePciMemoryEntry.setIndexNames((0,_C,_AX),(0,_C,_AY),(0,_C,_AZ),(0,_C,_Aa))
if mibBuilder.loadTexts:cpqSePciMemoryEntry.setStatus(_B)
_CpqSePciMemoryBusNumberIndex_Type=Integer32
_CpqSePciMemoryBusNumberIndex_Object=MibTableColumn
cpqSePciMemoryBusNumberIndex=_CpqSePciMemoryBusNumberIndex_Object((1,3,6,1,4,1,232,1,2,13,3,1,1),_CpqSePciMemoryBusNumberIndex_Type())
cpqSePciMemoryBusNumberIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciMemoryBusNumberIndex.setStatus(_B)
class _CpqSePciMemoryDeviceNumberIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSePciMemoryDeviceNumberIndex_Type.__name__=_E
_CpqSePciMemoryDeviceNumberIndex_Object=MibTableColumn
cpqSePciMemoryDeviceNumberIndex=_CpqSePciMemoryDeviceNumberIndex_Object((1,3,6,1,4,1,232,1,2,13,3,1,2),_CpqSePciMemoryDeviceNumberIndex_Type())
cpqSePciMemoryDeviceNumberIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciMemoryDeviceNumberIndex.setStatus(_B)
class _CpqSePciMemoryFunctionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CpqSePciMemoryFunctionIndex_Type.__name__=_E
_CpqSePciMemoryFunctionIndex_Object=MibTableColumn
cpqSePciMemoryFunctionIndex=_CpqSePciMemoryFunctionIndex_Object((1,3,6,1,4,1,232,1,2,13,3,1,3),_CpqSePciMemoryFunctionIndex_Type())
cpqSePciMemoryFunctionIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciMemoryFunctionIndex.setStatus(_B)
class _CpqSePciMemoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6))
_CpqSePciMemoryIndex_Type.__name__=_E
_CpqSePciMemoryIndex_Object=MibTableColumn
cpqSePciMemoryIndex=_CpqSePciMemoryIndex_Object((1,3,6,1,4,1,232,1,2,13,3,1,4),_CpqSePciMemoryIndex_Type())
cpqSePciMemoryIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciMemoryIndex.setStatus(_B)
_CpqSePciMemoryBaseAddr_Type=Integer32
_CpqSePciMemoryBaseAddr_Object=MibTableColumn
cpqSePciMemoryBaseAddr=_CpqSePciMemoryBaseAddr_Object((1,3,6,1,4,1,232,1,2,13,3,1,5),_CpqSePciMemoryBaseAddr_Type())
cpqSePciMemoryBaseAddr.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciMemoryBaseAddr.setStatus(_B)
class _CpqSePciMemoryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('io',2),('memory-mapped',3),('exp-rom',4)))
_CpqSePciMemoryType_Type.__name__=_E
_CpqSePciMemoryType_Object=MibTableColumn
cpqSePciMemoryType=_CpqSePciMemoryType_Object((1,3,6,1,4,1,232,1,2,13,3,1,6),_CpqSePciMemoryType_Type())
cpqSePciMemoryType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciMemoryType.setStatus(_B)
_CpqSePciMemorySize_Type=Integer32
_CpqSePciMemorySize_Object=MibTableColumn
cpqSePciMemorySize=_CpqSePciMemorySize_Object((1,3,6,1,4,1,232,1,2,13,3,1,7),_CpqSePciMemorySize_Type())
cpqSePciMemorySize.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciMemorySize.setStatus(_B)
class _CpqSePciMemoryHwLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSePciMemoryHwLocation_Type.__name__=_F
_CpqSePciMemoryHwLocation_Object=MibTableColumn
cpqSePciMemoryHwLocation=_CpqSePciMemoryHwLocation_Object((1,3,6,1,4,1,232,1,2,13,3,1,8),_CpqSePciMemoryHwLocation_Type())
cpqSePciMemoryHwLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciMemoryHwLocation.setStatus(_D)
class _CpqSePciSegmentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),('single-segment',2),('multi-segment',3),('auto-segment',4)))
_CpqSePciSegmentMode_Type.__name__=_E
_CpqSePciSegmentMode_Object=MibScalar
cpqSePciSegmentMode=_CpqSePciSegmentMode_Object((1,3,6,1,4,1,232,1,2,13,4),_CpqSePciSegmentMode_Type())
cpqSePciSegmentMode.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciSegmentMode.setStatus(_D)
class _CpqSePciePhySlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSePciePhySlot_Type.__name__=_E
_CpqSePciePhySlot_Object=MibScalar
cpqSePciePhySlot=_CpqSePciePhySlot_Object((1,3,6,1,4,1,232,1,2,13,5),_CpqSePciePhySlot_Type())
cpqSePciePhySlot.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePciePhySlot.setStatus(_B)
_CpqSePCCard_ObjectIdentity=ObjectIdentity
cpqSePCCard=_CpqSePCCard_ObjectIdentity((1,3,6,1,4,1,232,1,2,14))
_CpqSePCCardSlotTable_Object=MibTable
cpqSePCCardSlotTable=_CpqSePCCardSlotTable_Object((1,3,6,1,4,1,232,1,2,14,1))
if mibBuilder.loadTexts:cpqSePCCardSlotTable.setStatus(_B)
_CpqSePCCardSlotEntry_Object=MibTableRow
cpqSePCCardSlotEntry=_CpqSePCCardSlotEntry_Object((1,3,6,1,4,1,232,1,2,14,1,1))
cpqSePCCardSlotEntry.setIndexNames((0,_C,_X))
if mibBuilder.loadTexts:cpqSePCCardSlotEntry.setStatus(_B)
_CpqSePCCardSlotIndex_Type=Integer32
_CpqSePCCardSlotIndex_Object=MibTableColumn
cpqSePCCardSlotIndex=_CpqSePCCardSlotIndex_Object((1,3,6,1,4,1,232,1,2,14,1,1,1),_CpqSePCCardSlotIndex_Type())
cpqSePCCardSlotIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCCardSlotIndex.setStatus(_B)
class _CpqSePCCardCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_N,2),(_P,3),(_O,4)))
_CpqSePCCardCondition_Type.__name__=_E
_CpqSePCCardCondition_Object=MibTableColumn
cpqSePCCardCondition=_CpqSePCCardCondition_Object((1,3,6,1,4,1,232,1,2,14,1,1,2),_CpqSePCCardCondition_Type())
cpqSePCCardCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCCardCondition.setStatus(_B)
class _CpqSePCCardPhysLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,40))
_CpqSePCCardPhysLocation_Type.__name__=_F
_CpqSePCCardPhysLocation_Object=MibTableColumn
cpqSePCCardPhysLocation=_CpqSePCCardPhysLocation_Object((1,3,6,1,4,1,232,1,2,14,1,1,3),_CpqSePCCardPhysLocation_Type())
cpqSePCCardPhysLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCCardPhysLocation.setStatus(_B)
_CpqSePCCardSlotType_Type=Integer32
_CpqSePCCardSlotType_Object=MibTableColumn
cpqSePCCardSlotType=_CpqSePCCardSlotType_Object((1,3,6,1,4,1,232,1,2,14,1,1,4),_CpqSePCCardSlotType_Type())
cpqSePCCardSlotType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCCardSlotType.setStatus(_B)
class _CpqSePCCardSlotWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_L,1),(_K,2),('width8bit',3),('width16bit',4),('width32bit',5),('width64bit',6),('width128bit',7)))
_CpqSePCCardSlotWidth_Type.__name__=_E
_CpqSePCCardSlotWidth_Object=MibTableColumn
cpqSePCCardSlotWidth=_CpqSePCCardSlotWidth_Object((1,3,6,1,4,1,232,1,2,14,1,1,5),_CpqSePCCardSlotWidth_Type())
cpqSePCCardSlotWidth.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCCardSlotWidth.setStatus(_B)
_CpqSePCCardSlotThermalCapacity_Type=Integer32
_CpqSePCCardSlotThermalCapacity_Object=MibTableColumn
cpqSePCCardSlotThermalCapacity=_CpqSePCCardSlotThermalCapacity_Object((1,3,6,1,4,1,232,1,2,14,1,1,6),_CpqSePCCardSlotThermalCapacity_Type())
cpqSePCCardSlotThermalCapacity.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCCardSlotThermalCapacity.setStatus(_B)
class _CpqSePCCardSlotThermalSensor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSePCCardSlotThermalSensor_Type.__name__=_E
_CpqSePCCardSlotThermalSensor_Object=MibTableColumn
cpqSePCCardSlotThermalSensor=_CpqSePCCardSlotThermalSensor_Object((1,3,6,1,4,1,232,1,2,14,1,1,7),_CpqSePCCardSlotThermalSensor_Type())
cpqSePCCardSlotThermalSensor.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCCardSlotThermalSensor.setStatus(_B)
class _CpqSePCCardSlotPowerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('on',2),('off',3)))
_CpqSePCCardSlotPowerState_Type.__name__=_E
_CpqSePCCardSlotPowerState_Object=MibTableColumn
cpqSePCCardSlotPowerState=_CpqSePCCardSlotPowerState_Object((1,3,6,1,4,1,232,1,2,14,1,1,8),_CpqSePCCardSlotPowerState_Type())
cpqSePCCardSlotPowerState.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCCardSlotPowerState.setStatus(_B)
class _CpqSePCCardStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_N,2),('thermalDegraded',3),('thermalFailure',4)))
_CpqSePCCardStatus_Type.__name__=_E
_CpqSePCCardStatus_Object=MibTableColumn
cpqSePCCardStatus=_CpqSePCCardStatus_Object((1,3,6,1,4,1,232,1,2,14,1,1,9),_CpqSePCCardStatus_Type())
cpqSePCCardStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCCardStatus.setStatus(_B)
class _CpqSePCCardDeviceInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CpqSePCCardDeviceInfo_Type.__name__=_F
_CpqSePCCardDeviceInfo_Object=MibTableColumn
cpqSePCCardDeviceInfo=_CpqSePCCardDeviceInfo_Object((1,3,6,1,4,1,232,1,2,14,1,1,10),_CpqSePCCardDeviceInfo_Type())
cpqSePCCardDeviceInfo.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCCardDeviceInfo.setStatus(_B)
class _CpqSePCCardProductInfo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CpqSePCCardProductInfo_Type.__name__=_F
_CpqSePCCardProductInfo_Object=MibTableColumn
cpqSePCCardProductInfo=_CpqSePCCardProductInfo_Object((1,3,6,1,4,1,232,1,2,14,1,1,11),_CpqSePCCardProductInfo_Type())
cpqSePCCardProductInfo.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCCardProductInfo.setStatus(_B)
class _CpqSePCCardSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CpqSePCCardSerialNumber_Type.__name__=_F
_CpqSePCCardSerialNumber_Object=MibTableColumn
cpqSePCCardSerialNumber=_CpqSePCCardSerialNumber_Object((1,3,6,1,4,1,232,1,2,14,1,1,12),_CpqSePCCardSerialNumber_Type())
cpqSePCCardSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCCardSerialNumber.setStatus(_B)
class _CpqSePCCardAssetTag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CpqSePCCardAssetTag_Type.__name__=_F
_CpqSePCCardAssetTag_Object=MibTableColumn
cpqSePCCardAssetTag=_CpqSePCCardAssetTag_Object((1,3,6,1,4,1,232,1,2,14,1,1,13),_CpqSePCCardAssetTag_Type())
cpqSePCCardAssetTag.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCCardAssetTag.setStatus(_B)
_CpqSeUSBPort_ObjectIdentity=ObjectIdentity
cpqSeUSBPort=_CpqSeUSBPort_ObjectIdentity((1,3,6,1,4,1,232,1,2,15))
_CpqSeUSBPortTable_Object=MibTable
cpqSeUSBPortTable=_CpqSeUSBPortTable_Object((1,3,6,1,4,1,232,1,2,15,1))
if mibBuilder.loadTexts:cpqSeUSBPortTable.setStatus(_B)
_CpqSeUSBPortEntry_Object=MibTableRow
cpqSeUSBPortEntry=_CpqSeUSBPortEntry_Object((1,3,6,1,4,1,232,1,2,15,1,1))
cpqSeUSBPortEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:cpqSeUSBPortEntry.setStatus(_B)
class _CpqSeUSBPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqSeUSBPortIndex_Type.__name__=_E
_CpqSeUSBPortIndex_Object=MibTableColumn
cpqSeUSBPortIndex=_CpqSeUSBPortIndex_Object((1,3,6,1,4,1,232,1,2,15,1,1,1),_CpqSeUSBPortIndex_Type())
cpqSeUSBPortIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeUSBPortIndex.setStatus(_B)
class _CpqSeUSBPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('usbPort',2),('sdPort',3)))
_CpqSeUSBPortType_Type.__name__=_E
_CpqSeUSBPortType_Object=MibTableColumn
cpqSeUSBPortType=_CpqSeUSBPortType_Object((1,3,6,1,4,1,232,1,2,15,1,1,2),_CpqSeUSBPortType_Type())
cpqSeUSBPortType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeUSBPortType.setStatus(_B)
class _CpqSeUSBPortHwLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeUSBPortHwLocation_Type.__name__=_F
_CpqSeUSBPortHwLocation_Object=MibTableColumn
cpqSeUSBPortHwLocation=_CpqSeUSBPortHwLocation_Object((1,3,6,1,4,1,232,1,2,15,1,1,3),_CpqSeUSBPortHwLocation_Type())
cpqSeUSBPortHwLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeUSBPortHwLocation.setStatus(_D)
class _CpqSeUSBPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('notPopulated',2),('populated',3)))
_CpqSeUSBPortStatus_Type.__name__=_E
_CpqSeUSBPortStatus_Object=MibTableColumn
cpqSeUSBPortStatus=_CpqSeUSBPortStatus_Object((1,3,6,1,4,1,232,1,2,15,1,1,4),_CpqSeUSBPortStatus_Type())
cpqSeUSBPortStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeUSBPortStatus.setStatus(_B)
class _CpqSeUSBPortDeviceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeUSBPortDeviceName_Type.__name__=_F
_CpqSeUSBPortDeviceName_Object=MibTableColumn
cpqSeUSBPortDeviceName=_CpqSeUSBPortDeviceName_Object((1,3,6,1,4,1,232,1,2,15,1,1,5),_CpqSeUSBPortDeviceName_Type())
cpqSeUSBPortDeviceName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeUSBPortDeviceName.setStatus(_D)
_CpqSeUSBPortDeviceCapacity_Type=Integer32
_CpqSeUSBPortDeviceCapacity_Object=MibTableColumn
cpqSeUSBPortDeviceCapacity=_CpqSeUSBPortDeviceCapacity_Object((1,3,6,1,4,1,232,1,2,15,1,1,6),_CpqSeUSBPortDeviceCapacity_Type())
cpqSeUSBPortDeviceCapacity.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeUSBPortDeviceCapacity.setStatus(_D)
class _CpqSeUSBPortDeviceManufacturer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeUSBPortDeviceManufacturer_Type.__name__=_F
_CpqSeUSBPortDeviceManufacturer_Object=MibTableColumn
cpqSeUSBPortDeviceManufacturer=_CpqSeUSBPortDeviceManufacturer_Object((1,3,6,1,4,1,232,1,2,15,1,1,7),_CpqSeUSBPortDeviceManufacturer_Type())
cpqSeUSBPortDeviceManufacturer.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeUSBPortDeviceManufacturer.setStatus(_D)
class _CpqSeUSBPortDeviceModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeUSBPortDeviceModel_Type.__name__=_F
_CpqSeUSBPortDeviceModel_Object=MibTableColumn
cpqSeUSBPortDeviceModel=_CpqSeUSBPortDeviceModel_Object((1,3,6,1,4,1,232,1,2,15,1,1,8),_CpqSeUSBPortDeviceModel_Type())
cpqSeUSBPortDeviceModel.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeUSBPortDeviceModel.setStatus(_D)
class _CpqSeUSBPortDeviceFWVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeUSBPortDeviceFWVersion_Type.__name__=_F
_CpqSeUSBPortDeviceFWVersion_Object=MibTableColumn
cpqSeUSBPortDeviceFWVersion=_CpqSeUSBPortDeviceFWVersion_Object((1,3,6,1,4,1,232,1,2,15,1,1,9),_CpqSeUSBPortDeviceFWVersion_Type())
cpqSeUSBPortDeviceFWVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeUSBPortDeviceFWVersion.setStatus(_D)
class _CpqSeUSBPortDeviceSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeUSBPortDeviceSerialNumber_Type.__name__=_F
_CpqSeUSBPortDeviceSerialNumber_Object=MibTableColumn
cpqSeUSBPortDeviceSerialNumber=_CpqSeUSBPortDeviceSerialNumber_Object((1,3,6,1,4,1,232,1,2,15,1,1,10),_CpqSeUSBPortDeviceSerialNumber_Type())
cpqSeUSBPortDeviceSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeUSBPortDeviceSerialNumber.setStatus(_D)
class _CpqSeUSBPortDevicePartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeUSBPortDevicePartNumber_Type.__name__=_F
_CpqSeUSBPortDevicePartNumber_Object=MibTableColumn
cpqSeUSBPortDevicePartNumber=_CpqSeUSBPortDevicePartNumber_Object((1,3,6,1,4,1,232,1,2,15,1,1,11),_CpqSeUSBPortDevicePartNumber_Type())
cpqSeUSBPortDevicePartNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeUSBPortDevicePartNumber.setStatus(_D)
class _CpqSeUSBPortDeviceCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_CpqSeUSBPortDeviceCount_Type.__name__=_E
_CpqSeUSBPortDeviceCount_Object=MibTableColumn
cpqSeUSBPortDeviceCount=_CpqSeUSBPortDeviceCount_Object((1,3,6,1,4,1,232,1,2,15,1,1,12),_CpqSeUSBPortDeviceCount_Type())
cpqSeUSBPortDeviceCount.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeUSBPortDeviceCount.setStatus(_D)
class _CpqSeUSBPortDeviceReadErrorCount_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_CpqSeUSBPortDeviceReadErrorCount_Type.__name__=_M
_CpqSeUSBPortDeviceReadErrorCount_Object=MibTableColumn
cpqSeUSBPortDeviceReadErrorCount=_CpqSeUSBPortDeviceReadErrorCount_Object((1,3,6,1,4,1,232,1,2,15,1,1,13),_CpqSeUSBPortDeviceReadErrorCount_Type())
cpqSeUSBPortDeviceReadErrorCount.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeUSBPortDeviceReadErrorCount.setStatus(_D)
class _CpqSeUSBPortDeviceWriteErrorCount_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_CpqSeUSBPortDeviceWriteErrorCount_Type.__name__=_M
_CpqSeUSBPortDeviceWriteErrorCount_Object=MibTableColumn
cpqSeUSBPortDeviceWriteErrorCount=_CpqSeUSBPortDeviceWriteErrorCount_Object((1,3,6,1,4,1,232,1,2,15,1,1,14),_CpqSeUSBPortDeviceWriteErrorCount_Type())
cpqSeUSBPortDeviceWriteErrorCount.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeUSBPortDeviceWriteErrorCount.setStatus(_D)
class _CpqSeUSBPortDeviceReadThreshold_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_CpqSeUSBPortDeviceReadThreshold_Type.__name__=_M
_CpqSeUSBPortDeviceReadThreshold_Object=MibTableColumn
cpqSeUSBPortDeviceReadThreshold=_CpqSeUSBPortDeviceReadThreshold_Object((1,3,6,1,4,1,232,1,2,15,1,1,15),_CpqSeUSBPortDeviceReadThreshold_Type())
cpqSeUSBPortDeviceReadThreshold.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeUSBPortDeviceReadThreshold.setStatus(_D)
class _CpqSeUSBPortDeviceWriteThreshold_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_CpqSeUSBPortDeviceWriteThreshold_Type.__name__=_M
_CpqSeUSBPortDeviceWriteThreshold_Object=MibTableColumn
cpqSeUSBPortDeviceWriteThreshold=_CpqSeUSBPortDeviceWriteThreshold_Object((1,3,6,1,4,1,232,1,2,15,1,1,16),_CpqSeUSBPortDeviceWriteThreshold_Type())
cpqSeUSBPortDeviceWriteThreshold.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeUSBPortDeviceWriteThreshold.setStatus(_D)
class _CpqSeUSBPortDeviceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_N,2),(_P,3),(_O,4)))
_CpqSeUSBPortDeviceStatus_Type.__name__=_E
_CpqSeUSBPortDeviceStatus_Object=MibTableColumn
cpqSeUSBPortDeviceStatus=_CpqSeUSBPortDeviceStatus_Object((1,3,6,1,4,1,232,1,2,15,1,1,17),_CpqSeUSBPortDeviceStatus_Type())
cpqSeUSBPortDeviceStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeUSBPortDeviceStatus.setStatus(_D)
class _CpqSeUSBPortDeviceFeature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('redundancy-capable',1),('standard',2)))
_CpqSeUSBPortDeviceFeature_Type.__name__=_E
_CpqSeUSBPortDeviceFeature_Object=MibTableColumn
cpqSeUSBPortDeviceFeature=_CpqSeUSBPortDeviceFeature_Object((1,3,6,1,4,1,232,1,2,15,1,1,18),_CpqSeUSBPortDeviceFeature_Type())
cpqSeUSBPortDeviceFeature.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeUSBPortDeviceFeature.setStatus(_D)
_CpqSeUSBPortDeviceFailedSlot_Type=Integer32
_CpqSeUSBPortDeviceFailedSlot_Object=MibTableColumn
cpqSeUSBPortDeviceFailedSlot=_CpqSeUSBPortDeviceFailedSlot_Object((1,3,6,1,4,1,232,1,2,15,1,1,19),_CpqSeUSBPortDeviceFailedSlot_Type())
cpqSeUSBPortDeviceFailedSlot.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeUSBPortDeviceFailedSlot.setStatus(_B)
_CpqSeUSBPortDeviceLastSlotWithError_Type=Integer32
_CpqSeUSBPortDeviceLastSlotWithError_Object=MibTableColumn
cpqSeUSBPortDeviceLastSlotWithError=_CpqSeUSBPortDeviceLastSlotWithError_Object((1,3,6,1,4,1,232,1,2,15,1,1,20),_CpqSeUSBPortDeviceLastSlotWithError_Type())
cpqSeUSBPortDeviceLastSlotWithError.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeUSBPortDeviceLastSlotWithError.setStatus(_B)
class _CpqSeUSBPortDeviceFaultTolerance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('none',2),('mirroring',3)))
_CpqSeUSBPortDeviceFaultTolerance_Type.__name__=_E
_CpqSeUSBPortDeviceFaultTolerance_Object=MibTableColumn
cpqSeUSBPortDeviceFaultTolerance=_CpqSeUSBPortDeviceFaultTolerance_Object((1,3,6,1,4,1,232,1,2,15,1,1,21),_CpqSeUSBPortDeviceFaultTolerance_Type())
cpqSeUSBPortDeviceFaultTolerance.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeUSBPortDeviceFaultTolerance.setStatus(_D)
class _CpqSeUSBPortDevicePresent_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2))
_CpqSeUSBPortDevicePresent_Type.__name__=_M
_CpqSeUSBPortDevicePresent_Object=MibTableColumn
cpqSeUSBPortDevicePresent=_CpqSeUSBPortDevicePresent_Object((1,3,6,1,4,1,232,1,2,15,1,1,22),_CpqSeUSBPortDevicePresent_Type())
cpqSeUSBPortDevicePresent.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeUSBPortDevicePresent.setStatus(_D)
_CpqSeCell_ObjectIdentity=ObjectIdentity
cpqSeCell=_CpqSeCell_ObjectIdentity((1,3,6,1,4,1,232,1,2,16))
_CpqSeCellTable_Object=MibTable
cpqSeCellTable=_CpqSeCellTable_Object((1,3,6,1,4,1,232,1,2,16,1))
if mibBuilder.loadTexts:cpqSeCellTable.setStatus(_D)
_CpqSeCellEntry_Object=MibTableRow
cpqSeCellEntry=_CpqSeCellEntry_Object((1,3,6,1,4,1,232,1,2,16,1,1))
cpqSeCellEntry.setIndexNames((0,_C,_Ab))
if mibBuilder.loadTexts:cpqSeCellEntry.setStatus(_D)
class _CpqSeCellUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_CpqSeCellUnitIndex_Type.__name__=_E
_CpqSeCellUnitIndex_Object=MibTableColumn
cpqSeCellUnitIndex=_CpqSeCellUnitIndex_Object((1,3,6,1,4,1,232,1,2,16,1,1,1),_CpqSeCellUnitIndex_Type())
cpqSeCellUnitIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCellUnitIndex.setStatus(_D)
class _CpqSeCellCabinetNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_CpqSeCellCabinetNumber_Type.__name__=_E
_CpqSeCellCabinetNumber_Object=MibTableColumn
cpqSeCellCabinetNumber=_CpqSeCellCabinetNumber_Object((1,3,6,1,4,1,232,1,2,16,1,1,2),_CpqSeCellCabinetNumber_Type())
cpqSeCellCabinetNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCellCabinetNumber.setStatus(_D)
class _CpqSeCellCellNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_CpqSeCellCellNumber_Type.__name__=_E
_CpqSeCellCellNumber_Object=MibTableColumn
cpqSeCellCellNumber=_CpqSeCellCellNumber_Object((1,3,6,1,4,1,232,1,2,16,1,1,3),_CpqSeCellCellNumber_Type())
cpqSeCellCellNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCellCellNumber.setStatus(_D)
class _CpqSeCellIOCTablePtr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,19))
_CpqSeCellIOCTablePtr_Type.__name__=_E
_CpqSeCellIOCTablePtr_Object=MibTableColumn
cpqSeCellIOCTablePtr=_CpqSeCellIOCTablePtr_Object((1,3,6,1,4,1,232,1,2,16,1,1,4),_CpqSeCellIOCTablePtr_Type())
cpqSeCellIOCTablePtr.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCellIOCTablePtr.setStatus(_D)
class _CpqSeCellPDHCFirmwareRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeCellPDHCFirmwareRevision_Type.__name__=_F
_CpqSeCellPDHCFirmwareRevision_Object=MibTableColumn
cpqSeCellPDHCFirmwareRevision=_CpqSeCellPDHCFirmwareRevision_Object((1,3,6,1,4,1,232,1,2,16,1,1,5),_CpqSeCellPDHCFirmwareRevision_Type())
cpqSeCellPDHCFirmwareRevision.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCellPDHCFirmwareRevision.setStatus(_D)
class _CpqSeCellSysFwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeCellSysFwVersion_Type.__name__=_F
_CpqSeCellSysFwVersion_Object=MibTableColumn
cpqSeCellSysFwVersion=_CpqSeCellSysFwVersion_Object((1,3,6,1,4,1,232,1,2,16,1,1,6),_CpqSeCellSysFwVersion_Type())
cpqSeCellSysFwVersion.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCellSysFwVersion.setStatus(_D)
_CpqSeCellBootInhibited_Type=TruthValue
_CpqSeCellBootInhibited_Object=MibTableColumn
cpqSeCellBootInhibited=_CpqSeCellBootInhibited_Object((1,3,6,1,4,1,232,1,2,16,1,1,7),_CpqSeCellBootInhibited_Type())
cpqSeCellBootInhibited.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCellBootInhibited.setStatus(_D)
_CpqSeCellToScanBusConnectionStatus_Type=Integer32
_CpqSeCellToScanBusConnectionStatus_Object=MibTableColumn
cpqSeCellToScanBusConnectionStatus=_CpqSeCellToScanBusConnectionStatus_Object((1,3,6,1,4,1,232,1,2,16,1,1,8),_CpqSeCellToScanBusConnectionStatus_Type())
cpqSeCellToScanBusConnectionStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCellToScanBusConnectionStatus.setStatus(_D)
_CpqSeCellHasCoreIO_Type=TruthValue
_CpqSeCellHasCoreIO_Object=MibTableColumn
cpqSeCellHasCoreIO=_CpqSeCellHasCoreIO_Object((1,3,6,1,4,1,232,1,2,16,1,1,9),_CpqSeCellHasCoreIO_Type())
cpqSeCellHasCoreIO.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCellHasCoreIO.setStatus(_D)
_CpqSeCellBoardSpeed_Type=Integer32
_CpqSeCellBoardSpeed_Object=MibTableColumn
cpqSeCellBoardSpeed=_CpqSeCellBoardSpeed_Object((1,3,6,1,4,1,232,1,2,16,1,1,10),_CpqSeCellBoardSpeed_Type())
cpqSeCellBoardSpeed.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCellBoardSpeed.setStatus(_D)
_CpqSeCellPresent_Type=TruthValue
_CpqSeCellPresent_Object=MibTableColumn
cpqSeCellPresent=_CpqSeCellPresent_Object((1,3,6,1,4,1,232,1,2,16,1,1,11),_CpqSeCellPresent_Type())
cpqSeCellPresent.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCellPresent.setStatus(_D)
_CpqSeCellHasPower_Type=TruthValue
_CpqSeCellHasPower_Object=MibTableColumn
cpqSeCellHasPower=_CpqSeCellHasPower_Object((1,3,6,1,4,1,232,1,2,16,1,1,12),_CpqSeCellHasPower_Type())
cpqSeCellHasPower.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCellHasPower.setStatus(_D)
_CpqSeCellReadyForReconfig_Type=TruthValue
_CpqSeCellReadyForReconfig_Object=MibTableColumn
cpqSeCellReadyForReconfig=_CpqSeCellReadyForReconfig_Object((1,3,6,1,4,1,232,1,2,16,1,1,13),_CpqSeCellReadyForReconfig_Type())
cpqSeCellReadyForReconfig.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCellReadyForReconfig.setStatus(_D)
_CpqSeCellTotalMemory_Type=Integer32
_CpqSeCellTotalMemory_Object=MibTableColumn
cpqSeCellTotalMemory=_CpqSeCellTotalMemory_Object((1,3,6,1,4,1,232,1,2,16,1,1,14),_CpqSeCellTotalMemory_Type())
cpqSeCellTotalMemory.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCellTotalMemory.setStatus(_D)
_CpqSeCellLEDState_Type=Integer32
_CpqSeCellLEDState_Object=MibTableColumn
cpqSeCellLEDState=_CpqSeCellLEDState_Object((1,3,6,1,4,1,232,1,2,16,1,1,15),_CpqSeCellLEDState_Type())
cpqSeCellLEDState.setMaxAccess(_T)
if mibBuilder.loadTexts:cpqSeCellLEDState.setStatus(_D)
_CpqSeCellState_Type=Integer32
_CpqSeCellState_Object=MibTableColumn
cpqSeCellState=_CpqSeCellState_Object((1,3,6,1,4,1,232,1,2,16,1,1,16),_CpqSeCellState_Type())
cpqSeCellState.setMaxAccess(_T)
if mibBuilder.loadTexts:cpqSeCellState.setStatus(_D)
_CpqSeCellCLMRequestPercentage_Type=Integer32
_CpqSeCellCLMRequestPercentage_Object=MibTableColumn
cpqSeCellCLMRequestPercentage=_CpqSeCellCLMRequestPercentage_Object((1,3,6,1,4,1,232,1,2,16,1,1,17),_CpqSeCellCLMRequestPercentage_Type())
cpqSeCellCLMRequestPercentage.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCellCLMRequestPercentage.setStatus(_D)
_CpqSeCellCLMRequestSize_Type=Integer32
_CpqSeCellCLMRequestSize_Object=MibTableColumn
cpqSeCellCLMRequestSize=_CpqSeCellCLMRequestSize_Object((1,3,6,1,4,1,232,1,2,16,1,1,18),_CpqSeCellCLMRequestSize_Type())
cpqSeCellCLMRequestSize.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCellCLMRequestSize.setStatus(_D)
_CpqSeCellCLMAllocatedSize_Type=Integer32
_CpqSeCellCLMAllocatedSize_Object=MibTableColumn
cpqSeCellCLMAllocatedSize=_CpqSeCellCLMAllocatedSize_Object((1,3,6,1,4,1,232,1,2,16,1,1,19),_CpqSeCellCLMAllocatedSize_Type())
cpqSeCellCLMAllocatedSize.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCellCLMAllocatedSize.setStatus(_D)
_CpqSeCellInterleaveAllocatedSize_Type=Integer32
_CpqSeCellInterleaveAllocatedSize_Object=MibTableColumn
cpqSeCellInterleaveAllocatedSize=_CpqSeCellInterleaveAllocatedSize_Object((1,3,6,1,4,1,232,1,2,16,1,1,20),_CpqSeCellInterleaveAllocatedSize_Type())
cpqSeCellInterleaveAllocatedSize.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCellInterleaveAllocatedSize.setStatus(_D)
_CpqSeCellHasInterleaveMem_Type=Integer32
_CpqSeCellHasInterleaveMem_Object=MibTableColumn
cpqSeCellHasInterleaveMem=_CpqSeCellHasInterleaveMem_Object((1,3,6,1,4,1,232,1,2,16,1,1,21),_CpqSeCellHasInterleaveMem_Type())
cpqSeCellHasInterleaveMem.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCellHasInterleaveMem.setStatus(_D)
class _CpqSeCellSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeCellSerialNumber_Type.__name__=_F
_CpqSeCellSerialNumber_Object=MibTableColumn
cpqSeCellSerialNumber=_CpqSeCellSerialNumber_Object((1,3,6,1,4,1,232,1,2,16,1,1,22),_CpqSeCellSerialNumber_Type())
cpqSeCellSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCellSerialNumber.setStatus(_D)
class _CpqSeCellCLMCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_N,2),(_P,3),(_O,4)))
_CpqSeCellCLMCondition_Type.__name__=_E
_CpqSeCellCLMCondition_Object=MibTableColumn
cpqSeCellCLMCondition=_CpqSeCellCLMCondition_Object((1,3,6,1,4,1,232,1,2,16,1,1,23),_CpqSeCellCLMCondition_Type())
cpqSeCellCLMCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCellCLMCondition.setStatus(_D)
_CpqSeIOC_ObjectIdentity=ObjectIdentity
cpqSeIOC=_CpqSeIOC_ObjectIdentity((1,3,6,1,4,1,232,1,2,17))
_CpqSeIOCTable_Object=MibTable
cpqSeIOCTable=_CpqSeIOCTable_Object((1,3,6,1,4,1,232,1,2,17,1))
if mibBuilder.loadTexts:cpqSeIOCTable.setStatus(_D)
_CpqSeIOCEntry_Object=MibTableRow
cpqSeIOCEntry=_CpqSeIOCEntry_Object((1,3,6,1,4,1,232,1,2,17,1,1))
cpqSeIOCEntry.setIndexNames((0,_C,_Ac))
if mibBuilder.loadTexts:cpqSeIOCEntry.setStatus(_D)
class _CpqSeIOCUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,19))
_CpqSeIOCUnitIndex_Type.__name__=_E
_CpqSeIOCUnitIndex_Object=MibTableColumn
cpqSeIOCUnitIndex=_CpqSeIOCUnitIndex_Object((1,3,6,1,4,1,232,1,2,17,1,1,1),_CpqSeIOCUnitIndex_Type())
cpqSeIOCUnitIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeIOCUnitIndex.setStatus(_D)
class _CpqSeIOCCabinetNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpqSeIOCCabinetNumber_Type.__name__=_E
_CpqSeIOCCabinetNumber_Object=MibTableColumn
cpqSeIOCCabinetNumber=_CpqSeIOCCabinetNumber_Object((1,3,6,1,4,1,232,1,2,17,1,1,2),_CpqSeIOCCabinetNumber_Type())
cpqSeIOCCabinetNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeIOCCabinetNumber.setStatus(_D)
class _CpqSeIOCBayNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_CpqSeIOCBayNumber_Type.__name__=_E
_CpqSeIOCBayNumber_Object=MibTableColumn
cpqSeIOCBayNumber=_CpqSeIOCBayNumber_Object((1,3,6,1,4,1,232,1,2,17,1,1,3),_CpqSeIOCBayNumber_Type())
cpqSeIOCBayNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeIOCBayNumber.setStatus(_D)
class _CpqSeIOCIOCNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_CpqSeIOCIOCNumber_Type.__name__=_E
_CpqSeIOCIOCNumber_Object=MibTableColumn
cpqSeIOCIOCNumber=_CpqSeIOCIOCNumber_Object((1,3,6,1,4,1,232,1,2,17,1,1,4),_CpqSeIOCIOCNumber_Type())
cpqSeIOCIOCNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeIOCIOCNumber.setStatus(_D)
class _CpqSeIOCPowerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('powered-off',2),('powered-on',3)))
_CpqSeIOCPowerState_Type.__name__=_E
_CpqSeIOCPowerState_Object=MibTableColumn
cpqSeIOCPowerState=_CpqSeIOCPowerState_Object((1,3,6,1,4,1,232,1,2,17,1,1,5),_CpqSeIOCPowerState_Type())
cpqSeIOCPowerState.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeIOCPowerState.setStatus(_D)
_CpqSeIOCLEDState_Type=Integer32
_CpqSeIOCLEDState_Object=MibTableColumn
cpqSeIOCLEDState=_CpqSeIOCLEDState_Object((1,3,6,1,4,1,232,1,2,17,1,1,6),_CpqSeIOCLEDState_Type())
cpqSeIOCLEDState.setMaxAccess(_T)
if mibBuilder.loadTexts:cpqSeIOCLEDState.setStatus(_D)
_CpqSePartition_ObjectIdentity=ObjectIdentity
cpqSePartition=_CpqSePartition_ObjectIdentity((1,3,6,1,4,1,232,1,2,18))
_CpqSePartitionTotalCPU_Type=Integer32
_CpqSePartitionTotalCPU_Object=MibScalar
cpqSePartitionTotalCPU=_CpqSePartitionTotalCPU_Object((1,3,6,1,4,1,232,1,2,18,1),_CpqSePartitionTotalCPU_Type())
cpqSePartitionTotalCPU.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePartitionTotalCPU.setStatus(_D)
_CpqSePartitionAvailableCellSlots_Type=Integer32
_CpqSePartitionAvailableCellSlots_Object=MibScalar
cpqSePartitionAvailableCellSlots=_CpqSePartitionAvailableCellSlots_Object((1,3,6,1,4,1,232,1,2,18,2),_CpqSePartitionAvailableCellSlots_Type())
cpqSePartitionAvailableCellSlots.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePartitionAvailableCellSlots.setStatus(_D)
_CpqSePartitionInstalledCells_Type=Integer32
_CpqSePartitionInstalledCells_Object=MibScalar
cpqSePartitionInstalledCells=_CpqSePartitionInstalledCells_Object((1,3,6,1,4,1,232,1,2,18,3),_CpqSePartitionInstalledCells_Type())
cpqSePartitionInstalledCells.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePartitionInstalledCells.setStatus(_D)
_CpqSePartitionPoweredOnCells_Type=Integer32
_CpqSePartitionPoweredOnCells_Object=MibScalar
cpqSePartitionPoweredOnCells=_CpqSePartitionPoweredOnCells_Object((1,3,6,1,4,1,232,1,2,18,4),_CpqSePartitionPoweredOnCells_Type())
cpqSePartitionPoweredOnCells.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePartitionPoweredOnCells.setStatus(_D)
_CpqSePartitionReadyForReconfigCells_Type=Integer32
_CpqSePartitionReadyForReconfigCells_Object=MibScalar
cpqSePartitionReadyForReconfigCells=_CpqSePartitionReadyForReconfigCells_Object((1,3,6,1,4,1,232,1,2,18,5),_CpqSePartitionReadyForReconfigCells_Type())
cpqSePartitionReadyForReconfigCells.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePartitionReadyForReconfigCells.setStatus(_D)
_CpqSePartitionMemInterleavingType_Type=Integer32
_CpqSePartitionMemInterleavingType_Object=MibScalar
cpqSePartitionMemInterleavingType=_CpqSePartitionMemInterleavingType_Object((1,3,6,1,4,1,232,1,2,18,6),_CpqSePartitionMemInterleavingType_Type())
cpqSePartitionMemInterleavingType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePartitionMemInterleavingType.setStatus(_D)
class _CpqSePartitionName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSePartitionName_Type.__name__=_F
_CpqSePartitionName_Object=MibScalar
cpqSePartitionName=_CpqSePartitionName_Object((1,3,6,1,4,1,232,1,2,18,7),_CpqSePartitionName_Type())
cpqSePartitionName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePartitionName.setStatus(_D)
_CpqSePartitionCoreCell_Type=Integer32
_CpqSePartitionCoreCell_Object=MibScalar
cpqSePartitionCoreCell=_CpqSePartitionCoreCell_Object((1,3,6,1,4,1,232,1,2,18,8),_CpqSePartitionCoreCell_Type())
cpqSePartitionCoreCell.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePartitionCoreCell.setStatus(_D)
_CpqSePartitionCoreCellCabinet_Type=Integer32
_CpqSePartitionCoreCellCabinet_Object=MibScalar
cpqSePartitionCoreCellCabinet=_CpqSePartitionCoreCellCabinet_Object((1,3,6,1,4,1,232,1,2,18,9),_CpqSePartitionCoreCellCabinet_Type())
cpqSePartitionCoreCellCabinet.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePartitionCoreCellCabinet.setStatus(_D)
_CpqSePartitionCLMRequestPercentage_Type=Integer32
_CpqSePartitionCLMRequestPercentage_Object=MibScalar
cpqSePartitionCLMRequestPercentage=_CpqSePartitionCLMRequestPercentage_Object((1,3,6,1,4,1,232,1,2,18,10),_CpqSePartitionCLMRequestPercentage_Type())
cpqSePartitionCLMRequestPercentage.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePartitionCLMRequestPercentage.setStatus(_D)
_CpqSePartitionCLMRequestSize_Type=Integer32
_CpqSePartitionCLMRequestSize_Object=MibScalar
cpqSePartitionCLMRequestSize=_CpqSePartitionCLMRequestSize_Object((1,3,6,1,4,1,232,1,2,18,11),_CpqSePartitionCLMRequestSize_Type())
cpqSePartitionCLMRequestSize.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePartitionCLMRequestSize.setStatus(_D)
_CpqSePartitionCLMAllocatedSize_Type=Integer32
_CpqSePartitionCLMAllocatedSize_Object=MibScalar
cpqSePartitionCLMAllocatedSize=_CpqSePartitionCLMAllocatedSize_Object((1,3,6,1,4,1,232,1,2,18,12),_CpqSePartitionCLMAllocatedSize_Type())
cpqSePartitionCLMAllocatedSize.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePartitionCLMAllocatedSize.setStatus(_D)
_CpqSePartitionInterleaveAllocatedSize_Type=Integer32
_CpqSePartitionInterleaveAllocatedSize_Object=MibScalar
cpqSePartitionInterleaveAllocatedSize=_CpqSePartitionInterleaveAllocatedSize_Object((1,3,6,1,4,1,232,1,2,18,13),_CpqSePartitionInterleaveAllocatedSize_Type())
cpqSePartitionInterleaveAllocatedSize.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePartitionInterleaveAllocatedSize.setStatus(_D)
_CpqSePartitionHasInterleaveMem_Type=Integer32
_CpqSePartitionHasInterleaveMem_Object=MibScalar
cpqSePartitionHasInterleaveMem=_CpqSePartitionHasInterleaveMem_Object((1,3,6,1,4,1,232,1,2,18,14),_CpqSePartitionHasInterleaveMem_Type())
cpqSePartitionHasInterleaveMem.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePartitionHasInterleaveMem.setStatus(_D)
_CpqSePartitionNumber_Type=Integer32
_CpqSePartitionNumber_Object=MibScalar
cpqSePartitionNumber=_CpqSePartitionNumber_Object((1,3,6,1,4,1,232,1,2,18,15),_CpqSePartitionNumber_Type())
cpqSePartitionNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePartitionNumber.setStatus(_D)
_CpqSeCabinet_ObjectIdentity=ObjectIdentity
cpqSeCabinet=_CpqSeCabinet_ObjectIdentity((1,3,6,1,4,1,232,1,2,19))
_CpqSeCabinetTable_Object=MibTable
cpqSeCabinetTable=_CpqSeCabinetTable_Object((1,3,6,1,4,1,232,1,2,19,1))
if mibBuilder.loadTexts:cpqSeCabinetTable.setStatus(_D)
_CpqSeCabinetEntry_Object=MibTableRow
cpqSeCabinetEntry=_CpqSeCabinetEntry_Object((1,3,6,1,4,1,232,1,2,19,1,1))
cpqSeCabinetEntry.setIndexNames((0,_C,_Ad))
if mibBuilder.loadTexts:cpqSeCabinetEntry.setStatus(_D)
class _CpqSeCabinetUnitIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_CpqSeCabinetUnitIndex_Type.__name__=_E
_CpqSeCabinetUnitIndex_Object=MibTableColumn
cpqSeCabinetUnitIndex=_CpqSeCabinetUnitIndex_Object((1,3,6,1,4,1,232,1,2,19,1,1,1),_CpqSeCabinetUnitIndex_Type())
cpqSeCabinetUnitIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCabinetUnitIndex.setStatus(_D)
_CpqSeCabinetCPULED_Type=TruthValue
_CpqSeCabinetCPULED_Object=MibTableColumn
cpqSeCabinetCPULED=_CpqSeCabinetCPULED_Object((1,3,6,1,4,1,232,1,2,19,1,1,2),_CpqSeCabinetCPULED_Type())
cpqSeCabinetCPULED.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCabinetCPULED.setStatus(_D)
_CpqSeCabinetIOXLED_Type=TruthValue
_CpqSeCabinetIOXLED_Object=MibTableColumn
cpqSeCabinetIOXLED=_CpqSeCabinetIOXLED_Object((1,3,6,1,4,1,232,1,2,19,1,1,3),_CpqSeCabinetIOXLED_Type())
cpqSeCabinetIOXLED.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCabinetIOXLED.setStatus(_D)
_CpqSeCabinetTypeNum_Type=Integer32
_CpqSeCabinetTypeNum_Object=MibTableColumn
cpqSeCabinetTypeNum=_CpqSeCabinetTypeNum_Object((1,3,6,1,4,1,232,1,2,19,1,1,4),_CpqSeCabinetTypeNum_Type())
cpqSeCabinetTypeNum.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeCabinetTypeNum.setStatus(_D)
_CpqSeCabinetLED_Type=Integer32
_CpqSeCabinetLED_Object=MibTableColumn
cpqSeCabinetLED=_CpqSeCabinetLED_Object((1,3,6,1,4,1,232,1,2,19,1,1,5),_CpqSeCabinetLED_Type())
cpqSeCabinetLED.setMaxAccess(_T)
if mibBuilder.loadTexts:cpqSeCabinetLED.setStatus(_D)
_CpqSeComplex_ObjectIdentity=ObjectIdentity
cpqSeComplex=_CpqSeComplex_ObjectIdentity((1,3,6,1,4,1,232,1,2,20))
class _CpqSeComplexUUID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeComplexUUID_Type.__name__=_F
_CpqSeComplexUUID_Object=MibScalar
cpqSeComplexUUID=_CpqSeComplexUUID_Object((1,3,6,1,4,1,232,1,2,20,1),_CpqSeComplexUUID_Type())
cpqSeComplexUUID.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeComplexUUID.setStatus(_D)
class _CpqSeComplexTotalCabinet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_CpqSeComplexTotalCabinet_Type.__name__=_E
_CpqSeComplexTotalCabinet_Object=MibScalar
cpqSeComplexTotalCabinet=_CpqSeComplexTotalCabinet_Object((1,3,6,1,4,1,232,1,2,20,2),_CpqSeComplexTotalCabinet_Type())
cpqSeComplexTotalCabinet.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeComplexTotalCabinet.setStatus(_D)
class _CpqSeComplexComputeCabinet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_CpqSeComplexComputeCabinet_Type.__name__=_E
_CpqSeComplexComputeCabinet_Object=MibScalar
cpqSeComplexComputeCabinet=_CpqSeComplexComputeCabinet_Object((1,3,6,1,4,1,232,1,2,20,3),_CpqSeComplexComputeCabinet_Type())
cpqSeComplexComputeCabinet.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeComplexComputeCabinet.setStatus(_D)
class _CpqSeComplexIOXCabinet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_CpqSeComplexIOXCabinet_Type.__name__=_E
_CpqSeComplexIOXCabinet_Object=MibScalar
cpqSeComplexIOXCabinet=_CpqSeComplexIOXCabinet_Object((1,3,6,1,4,1,232,1,2,20,4),_CpqSeComplexIOXCabinet_Type())
cpqSeComplexIOXCabinet.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeComplexIOXCabinet.setStatus(_D)
class _CpqSeComplexName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeComplexName_Type.__name__=_F
_CpqSeComplexName_Object=MibScalar
cpqSeComplexName=_CpqSeComplexName_Object((1,3,6,1,4,1,232,1,2,20,5),_CpqSeComplexName_Type())
cpqSeComplexName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeComplexName.setStatus(_D)
_CpqSeComplexLockedProperty_Type=Integer32
_CpqSeComplexLockedProperty_Object=MibScalar
cpqSeComplexLockedProperty=_CpqSeComplexLockedProperty_Object((1,3,6,1,4,1,232,1,2,20,6),_CpqSeComplexLockedProperty_Type())
cpqSeComplexLockedProperty.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeComplexLockedProperty.setStatus(_D)
_CpqSeComplexCellSlotStatusTable_Object=MibTable
cpqSeComplexCellSlotStatusTable=_CpqSeComplexCellSlotStatusTable_Object((1,3,6,1,4,1,232,1,2,20,7))
if mibBuilder.loadTexts:cpqSeComplexCellSlotStatusTable.setStatus(_D)
_CpqSeComplexCellSlotStatusEntry_Object=MibTableRow
cpqSeComplexCellSlotStatusEntry=_CpqSeComplexCellSlotStatusEntry_Object((1,3,6,1,4,1,232,1,2,20,7,1))
cpqSeComplexCellSlotStatusEntry.setIndexNames((0,_C,_Ae))
if mibBuilder.loadTexts:cpqSeComplexCellSlotStatusEntry.setStatus(_D)
_CpqSeComplexCellSlotStatusIndex_Type=Integer32
_CpqSeComplexCellSlotStatusIndex_Object=MibTableColumn
cpqSeComplexCellSlotStatusIndex=_CpqSeComplexCellSlotStatusIndex_Object((1,3,6,1,4,1,232,1,2,20,7,1,1),_CpqSeComplexCellSlotStatusIndex_Type())
cpqSeComplexCellSlotStatusIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeComplexCellSlotStatusIndex.setStatus(_D)
_CpqSeComplexCellSlotStatusCabinetNo_Type=Integer32
_CpqSeComplexCellSlotStatusCabinetNo_Object=MibTableColumn
cpqSeComplexCellSlotStatusCabinetNo=_CpqSeComplexCellSlotStatusCabinetNo_Object((1,3,6,1,4,1,232,1,2,20,7,1,2),_CpqSeComplexCellSlotStatusCabinetNo_Type())
cpqSeComplexCellSlotStatusCabinetNo.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeComplexCellSlotStatusCabinetNo.setStatus(_D)
_CpqSeComplexCellSlotStatusSlotNo_Type=Integer32
_CpqSeComplexCellSlotStatusSlotNo_Object=MibTableColumn
cpqSeComplexCellSlotStatusSlotNo=_CpqSeComplexCellSlotStatusSlotNo_Object((1,3,6,1,4,1,232,1,2,20,7,1,3),_CpqSeComplexCellSlotStatusSlotNo_Type())
cpqSeComplexCellSlotStatusSlotNo.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeComplexCellSlotStatusSlotNo.setStatus(_D)
class _CpqSeComplexCellSlotStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_K,1),('active',2),('inactive',3),('assigned-powered-off',4),('free-powered-on',5),('free-powered-off',6),('empty',7)))
_CpqSeComplexCellSlotStatus_Type.__name__=_E
_CpqSeComplexCellSlotStatus_Object=MibTableColumn
cpqSeComplexCellSlotStatus=_CpqSeComplexCellSlotStatus_Object((1,3,6,1,4,1,232,1,2,20,7,1,4),_CpqSeComplexCellSlotStatus_Type())
cpqSeComplexCellSlotStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeComplexCellSlotStatus.setStatus(_D)
_CpqSeComplexCellSlotPartitionNo_Type=Integer32
_CpqSeComplexCellSlotPartitionNo_Object=MibTableColumn
cpqSeComplexCellSlotPartitionNo=_CpqSeComplexCellSlotPartitionNo_Object((1,3,6,1,4,1,232,1,2,20,7,1,5),_CpqSeComplexCellSlotPartitionNo_Type())
cpqSeComplexCellSlotPartitionNo.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeComplexCellSlotPartitionNo.setStatus(_D)
class _CpqSeComplexCellSlotPartitionName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeComplexCellSlotPartitionName_Type.__name__=_F
_CpqSeComplexCellSlotPartitionName_Object=MibTableColumn
cpqSeComplexCellSlotPartitionName=_CpqSeComplexCellSlotPartitionName_Object((1,3,6,1,4,1,232,1,2,20,7,1,6),_CpqSeComplexCellSlotPartitionName_Type())
cpqSeComplexCellSlotPartitionName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeComplexCellSlotPartitionName.setStatus(_D)
_CpqSeLED_ObjectIdentity=ObjectIdentity
cpqSeLED=_CpqSeLED_ObjectIdentity((1,3,6,1,4,1,232,1,2,21))
_CpqSeLEDTable_Object=MibTable
cpqSeLEDTable=_CpqSeLEDTable_Object((1,3,6,1,4,1,232,1,2,21,1))
if mibBuilder.loadTexts:cpqSeLEDTable.setStatus(_D)
_CpqSeLEDEntry_Object=MibTableRow
cpqSeLEDEntry=_CpqSeLEDEntry_Object((1,3,6,1,4,1,232,1,2,21,1,1))
cpqSeLEDEntry.setIndexNames((0,_C,_Af))
if mibBuilder.loadTexts:cpqSeLEDEntry.setStatus(_D)
class _CpqSeLEDIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSeLEDIndex_Type.__name__=_E
_CpqSeLEDIndex_Object=MibTableColumn
cpqSeLEDIndex=_CpqSeLEDIndex_Object((1,3,6,1,4,1,232,1,2,21,1,1,1),_CpqSeLEDIndex_Type())
cpqSeLEDIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeLEDIndex.setStatus(_D)
_CpqSeLEDState_Type=Integer32
_CpqSeLEDState_Object=MibTableColumn
cpqSeLEDState=_CpqSeLEDState_Object((1,3,6,1,4,1,232,1,2,21,1,1,2),_CpqSeLEDState_Type())
cpqSeLEDState.setMaxAccess(_T)
if mibBuilder.loadTexts:cpqSeLEDState.setStatus(_D)
_CpqSeLEDStateDuration_Type=Integer32
_CpqSeLEDStateDuration_Object=MibTableColumn
cpqSeLEDStateDuration=_CpqSeLEDStateDuration_Object((1,3,6,1,4,1,232,1,2,21,1,1,3),_CpqSeLEDStateDuration_Type())
cpqSeLEDStateDuration.setMaxAccess(_T)
if mibBuilder.loadTexts:cpqSeLEDStateDuration.setStatus(_D)
_CpqSeLEDLocationType_Type=Integer32
_CpqSeLEDLocationType_Object=MibTableColumn
cpqSeLEDLocationType=_CpqSeLEDLocationType_Object((1,3,6,1,4,1,232,1,2,21,1,1,4),_CpqSeLEDLocationType_Type())
cpqSeLEDLocationType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeLEDLocationType.setStatus(_D)
class _CpqSeLEDDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeLEDDescription_Type.__name__=_F
_CpqSeLEDDescription_Object=MibTableColumn
cpqSeLEDDescription=_CpqSeLEDDescription_Object((1,3,6,1,4,1,232,1,2,21,1,1,5),_CpqSeLEDDescription_Type())
cpqSeLEDDescription.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeLEDDescription.setStatus(_D)
class _CpqSeLEDHardwareLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeLEDHardwareLocation_Type.__name__=_F
_CpqSeLEDHardwareLocation_Object=MibTableColumn
cpqSeLEDHardwareLocation=_CpqSeLEDHardwareLocation_Object((1,3,6,1,4,1,232,1,2,21,1,1,6),_CpqSeLEDHardwareLocation_Type())
cpqSeLEDHardwareLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeLEDHardwareLocation.setStatus(_D)
_CpqSeUSBDevice_ObjectIdentity=ObjectIdentity
cpqSeUSBDevice=_CpqSeUSBDevice_ObjectIdentity((1,3,6,1,4,1,232,1,2,22))
class _CpqSeUSBDeviceType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeUSBDeviceType_Type.__name__=_F
_CpqSeUSBDeviceType_Object=MibScalar
cpqSeUSBDeviceType=_CpqSeUSBDeviceType_Object((1,3,6,1,4,1,232,1,2,22,1),_CpqSeUSBDeviceType_Type())
cpqSeUSBDeviceType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeUSBDeviceType.setStatus(_D)
class _CpqSeUSBDeviceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSeUSBDeviceName_Type.__name__=_F
_CpqSeUSBDeviceName_Object=MibScalar
cpqSeUSBDeviceName=_CpqSeUSBDeviceName_Object((1,3,6,1,4,1,232,1,2,22,2),_CpqSeUSBDeviceName_Type())
cpqSeUSBDeviceName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSeUSBDeviceName.setStatus(_D)
_CpqSePCIeDisk_ObjectIdentity=ObjectIdentity
cpqSePCIeDisk=_CpqSePCIeDisk_ObjectIdentity((1,3,6,1,4,1,232,1,2,23))
_CpqSePCIeDiskTable_Object=MibTable
cpqSePCIeDiskTable=_CpqSePCIeDiskTable_Object((1,3,6,1,4,1,232,1,2,23,1))
if mibBuilder.loadTexts:cpqSePCIeDiskTable.setStatus(_D)
_CpqSePCIeDiskEntry_Object=MibTableRow
cpqSePCIeDiskEntry=_CpqSePCIeDiskEntry_Object((1,3,6,1,4,1,232,1,2,23,1,1))
cpqSePCIeDiskEntry.setIndexNames((0,_C,_U),(0,_C,_V),(0,_C,_W))
if mibBuilder.loadTexts:cpqSePCIeDiskEntry.setStatus(_D)
class _CpqSePCIeDiskPCIBusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSePCIeDiskPCIBusIndex_Type.__name__=_E
_CpqSePCIeDiskPCIBusIndex_Object=MibTableColumn
cpqSePCIeDiskPCIBusIndex=_CpqSePCIeDiskPCIBusIndex_Object((1,3,6,1,4,1,232,1,2,23,1,1,1),_CpqSePCIeDiskPCIBusIndex_Type())
cpqSePCIeDiskPCIBusIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCIeDiskPCIBusIndex.setStatus(_D)
class _CpqSePCIeDiskPCIDeviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSePCIeDiskPCIDeviceIndex_Type.__name__=_E
_CpqSePCIeDiskPCIDeviceIndex_Object=MibTableColumn
cpqSePCIeDiskPCIDeviceIndex=_CpqSePCIeDiskPCIDeviceIndex_Object((1,3,6,1,4,1,232,1,2,23,1,1,2),_CpqSePCIeDiskPCIDeviceIndex_Type())
cpqSePCIeDiskPCIDeviceIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCIeDiskPCIDeviceIndex.setStatus(_D)
class _CpqSePCIeDiskPCIFunctionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqSePCIeDiskPCIFunctionIndex_Type.__name__=_E
_CpqSePCIeDiskPCIFunctionIndex_Object=MibTableColumn
cpqSePCIeDiskPCIFunctionIndex=_CpqSePCIeDiskPCIFunctionIndex_Object((1,3,6,1,4,1,232,1,2,23,1,1,3),_CpqSePCIeDiskPCIFunctionIndex_Type())
cpqSePCIeDiskPCIFunctionIndex.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCIeDiskPCIFunctionIndex.setStatus(_D)
class _CpqSePCIeDiskModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSePCIeDiskModel_Type.__name__=_F
_CpqSePCIeDiskModel_Object=MibTableColumn
cpqSePCIeDiskModel=_CpqSePCIeDiskModel_Object((1,3,6,1,4,1,232,1,2,23,1,1,4),_CpqSePCIeDiskModel_Type())
cpqSePCIeDiskModel.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCIeDiskModel.setStatus(_D)
class _CpqSePCIeDiskFwRev_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSePCIeDiskFwRev_Type.__name__=_F
_CpqSePCIeDiskFwRev_Object=MibTableColumn
cpqSePCIeDiskFwRev=_CpqSePCIeDiskFwRev_Object((1,3,6,1,4,1,232,1,2,23,1,1,5),_CpqSePCIeDiskFwRev_Type())
cpqSePCIeDiskFwRev.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCIeDiskFwRev.setStatus(_D)
class _CpqSePCIeDiskSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSePCIeDiskSerialNumber_Type.__name__=_F
_CpqSePCIeDiskSerialNumber_Object=MibTableColumn
cpqSePCIeDiskSerialNumber=_CpqSePCIeDiskSerialNumber_Object((1,3,6,1,4,1,232,1,2,23,1,1,6),_CpqSePCIeDiskSerialNumber_Type())
cpqSePCIeDiskSerialNumber.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCIeDiskSerialNumber.setStatus(_D)
_CpqSePCIeDiskCapacityMB_Type=Gauge32
_CpqSePCIeDiskCapacityMB_Object=MibTableColumn
cpqSePCIeDiskCapacityMB=_CpqSePCIeDiskCapacityMB_Object((1,3,6,1,4,1,232,1,2,23,1,1,7),_CpqSePCIeDiskCapacityMB_Type())
cpqSePCIeDiskCapacityMB.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCIeDiskCapacityMB.setStatus(_D)
class _CpqSePCIeDiskCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_K,1),(_N,2),(_P,3),(_O,4),('inserted',5),('removed',6),('invalid',7)))
_CpqSePCIeDiskCondition_Type.__name__=_E
_CpqSePCIeDiskCondition_Object=MibTableColumn
cpqSePCIeDiskCondition=_CpqSePCIeDiskCondition_Object((1,3,6,1,4,1,232,1,2,23,1,1,8),_CpqSePCIeDiskCondition_Type())
cpqSePCIeDiskCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCIeDiskCondition.setStatus(_D)
_CpqSePCIeDiskCurrentTemperature_Type=Integer32
_CpqSePCIeDiskCurrentTemperature_Object=MibTableColumn
cpqSePCIeDiskCurrentTemperature=_CpqSePCIeDiskCurrentTemperature_Object((1,3,6,1,4,1,232,1,2,23,1,1,9),_CpqSePCIeDiskCurrentTemperature_Type())
cpqSePCIeDiskCurrentTemperature.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCIeDiskCurrentTemperature.setStatus(_D)
_CpqSePCIeDiskThresholdTemperature_Type=Integer32
_CpqSePCIeDiskThresholdTemperature_Object=MibTableColumn
cpqSePCIeDiskThresholdTemperature=_CpqSePCIeDiskThresholdTemperature_Object((1,3,6,1,4,1,232,1,2,23,1,1,10),_CpqSePCIeDiskThresholdTemperature_Type())
cpqSePCIeDiskThresholdTemperature.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCIeDiskThresholdTemperature.setStatus(_D)
class _CpqSePCIeDiskHwLocation_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSePCIeDiskHwLocation_Type.__name__=_F
_CpqSePCIeDiskHwLocation_Object=MibTableColumn
cpqSePCIeDiskHwLocation=_CpqSePCIeDiskHwLocation_Object((1,3,6,1,4,1,232,1,2,23,1,1,11),_CpqSePCIeDiskHwLocation_Type())
cpqSePCIeDiskHwLocation.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCIeDiskHwLocation.setStatus(_D)
class _CpqSePCIeDiskOsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CpqSePCIeDiskOsName_Type.__name__=_F
_CpqSePCIeDiskOsName_Object=MibTableColumn
cpqSePCIeDiskOsName=_CpqSePCIeDiskOsName_Object((1,3,6,1,4,1,232,1,2,23,1,1,12),_CpqSePCIeDiskOsName_Type())
cpqSePCIeDiskOsName.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCIeDiskOsName.setStatus(_D)
class _CpqSePCIeDiskWearStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_L,1),(_N,2),('fiftySixDayThreshold',3),('fivePercentThreshold',4),('twoPercentThreshold',5),('ssdWearOut',6)))
_CpqSePCIeDiskWearStatus_Type.__name__=_E
_CpqSePCIeDiskWearStatus_Object=MibTableColumn
cpqSePCIeDiskWearStatus=_CpqSePCIeDiskWearStatus_Object((1,3,6,1,4,1,232,1,2,23,1,1,13),_CpqSePCIeDiskWearStatus_Type())
cpqSePCIeDiskWearStatus.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCIeDiskWearStatus.setStatus(_D)
_CpqSePCIeDiskPowerOnHours_Type=Counter32
_CpqSePCIeDiskPowerOnHours_Object=MibTableColumn
cpqSePCIeDiskPowerOnHours=_CpqSePCIeDiskPowerOnHours_Object((1,3,6,1,4,1,232,1,2,23,1,1,14),_CpqSePCIeDiskPowerOnHours_Type())
cpqSePCIeDiskPowerOnHours.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCIeDiskPowerOnHours.setStatus(_D)
_CpqSePCIeDiskPercntEndrnceUsed_Type=Gauge32
_CpqSePCIeDiskPercntEndrnceUsed_Object=MibTableColumn
cpqSePCIeDiskPercntEndrnceUsed=_CpqSePCIeDiskPercntEndrnceUsed_Object((1,3,6,1,4,1,232,1,2,23,1,1,15),_CpqSePCIeDiskPercntEndrnceUsed_Type())
cpqSePCIeDiskPercntEndrnceUsed.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCIeDiskPercntEndrnceUsed.setStatus(_D)
class _CpqSePCIeDiskTableCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_K,1),(_N,2),(_P,3),(_O,4)))
_CpqSePCIeDiskTableCondition_Type.__name__=_E
_CpqSePCIeDiskTableCondition_Object=MibScalar
cpqSePCIeDiskTableCondition=_CpqSePCIeDiskTableCondition_Object((1,3,6,1,4,1,232,1,2,23,2),_CpqSePCIeDiskTableCondition_Type())
cpqSePCIeDiskTableCondition.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCIeDiskTableCondition.setStatus(_D)
class _CpqSePCIeEraseFailureType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('secureEraseFailed',1),('secureEraseNotSupported',2),('noEraseSupported',3)))
_CpqSePCIeEraseFailureType_Type.__name__=_E
_CpqSePCIeEraseFailureType_Object=MibScalar
cpqSePCIeEraseFailureType=_CpqSePCIeEraseFailureType_Object((1,3,6,1,4,1,232,1,2,23,3),_CpqSePCIeEraseFailureType_Type())
cpqSePCIeEraseFailureType.setMaxAccess(_A)
if mibBuilder.loadTexts:cpqSePCIeEraseFailureType.setStatus(_B)
cpqSeCpuThresholdPassed=NotificationType((1,3,6,1,4,1,232,0,1001))
cpqSeCpuThresholdPassed.setObjects(*((_I,_J),(_G,_H),(_C,_d),(_C,_e)))
if mibBuilder.loadTexts:cpqSeCpuThresholdPassed.setStatus('')
cpqSePCCardThermalDegraded=NotificationType((1,3,6,1,4,1,232,0,1002))
cpqSePCCardThermalDegraded.setObjects(*((_I,_J),(_G,_H),(_C,_r),(_C,_s),(_C,_X)))
if mibBuilder.loadTexts:cpqSePCCardThermalDegraded.setStatus('')
cpqSePCCardThermalFailure=NotificationType((1,3,6,1,4,1,232,0,1003))
cpqSePCCardThermalFailure.setObjects(*((_I,_J),(_G,_H),(_C,_r),(_C,_s),(_C,_X)))
if mibBuilder.loadTexts:cpqSePCCardThermalFailure.setStatus('')
cpqSePCCardThermalSafe=NotificationType((1,3,6,1,4,1,232,0,1004))
cpqSePCCardThermalSafe.setObjects(*((_I,_J),(_G,_H),(_C,_X)))
if mibBuilder.loadTexts:cpqSePCCardThermalSafe.setStatus('')
cpqSe2CpuThresholdPassed=NotificationType((1,3,6,1,4,1,232,0,1005))
cpqSe2CpuThresholdPassed.setObjects(*((_I,_J),(_G,_H),(_C,_d),(_C,_e),(_C,_o),(_C,_p),(_C,_Ag)))
if mibBuilder.loadTexts:cpqSe2CpuThresholdPassed.setStatus('')
cpqSeCpuStatusChange=NotificationType((1,3,6,1,4,1,232,0,1006))
cpqSeCpuStatusChange.setObjects(*((_I,_J),(_G,_H),(_C,_c),(_C,_d),(_C,_t),(_C,_o),(_C,_u),(_C,_Ah),(_C,_p),(_C,_e),(_C,_v)))
if mibBuilder.loadTexts:cpqSeCpuStatusChange.setStatus('')
cpqSeCpuPowerPodstatusChange=NotificationType((1,3,6,1,4,1,232,0,1007))
cpqSeCpuPowerPodstatusChange.setObjects(*((_I,_J),(_G,_H),(_C,_c),(_C,_d),(_C,_t),(_C,_o),(_C,_u),(_C,_Ai),(_C,_p),(_C,_e),(_C,_v)))
if mibBuilder.loadTexts:cpqSeCpuPowerPodstatusChange.setStatus('')
cpqSeUSBStorageDeviceAttached=NotificationType((1,3,6,1,4,1,232,0,1008))
cpqSeUSBStorageDeviceAttached.setObjects(*((_I,_J),(_G,_H),(_C,_Q),(_C,_S)))
if mibBuilder.loadTexts:cpqSeUSBStorageDeviceAttached.setStatus('')
cpqSeUSBStorageDeviceRemoved=NotificationType((1,3,6,1,4,1,232,0,1009))
cpqSeUSBStorageDeviceRemoved.setObjects(*((_I,_J),(_G,_H),(_C,_Q),(_C,_S)))
if mibBuilder.loadTexts:cpqSeUSBStorageDeviceRemoved.setStatus('')
cpqSeUSBStorageDeviceReadErrorOccurred=NotificationType((1,3,6,1,4,1,232,0,1010))
cpqSeUSBStorageDeviceReadErrorOccurred.setObjects(*((_I,_J),(_G,_H),(_C,_Q),(_C,_S),(_C,_Y),(_C,_Z),(_C,_a),(_C,_b),(_C,_Aj),(_C,_Ak),(_C,_w)))
if mibBuilder.loadTexts:cpqSeUSBStorageDeviceReadErrorOccurred.setStatus('')
cpqSeUSBStorageDeviceWriteErrorOccurred=NotificationType((1,3,6,1,4,1,232,0,1011))
cpqSeUSBStorageDeviceWriteErrorOccurred.setObjects(*((_I,_J),(_G,_H),(_C,_Q),(_C,_S),(_C,_Y),(_C,_Z),(_C,_a),(_C,_b),(_C,_Al),(_C,_Am),(_C,_w)))
if mibBuilder.loadTexts:cpqSeUSBStorageDeviceWriteErrorOccurred.setStatus('')
cpqSeUSBStorageDeviceRedundancyLost=NotificationType((1,3,6,1,4,1,232,0,1012))
cpqSeUSBStorageDeviceRedundancyLost.setObjects(*((_I,_J),(_G,_H),(_C,_Q),(_C,_S),(_C,_Y),(_C,_Z),(_C,_a),(_C,_b),(_C,_An)))
if mibBuilder.loadTexts:cpqSeUSBStorageDeviceRedundancyLost.setStatus('')
cpqSeUSBStorageDeviceRedundancyRestored=NotificationType((1,3,6,1,4,1,232,0,1013))
cpqSeUSBStorageDeviceRedundancyRestored.setObjects(*((_I,_J),(_G,_H),(_C,_Q),(_C,_S),(_C,_Y),(_C,_Z),(_C,_a),(_C,_b)))
if mibBuilder.loadTexts:cpqSeUSBStorageDeviceRedundancyRestored.setStatus('')
cpqSeUSBStorageDeviceSyncFailed=NotificationType((1,3,6,1,4,1,232,0,1014))
cpqSeUSBStorageDeviceSyncFailed.setObjects(*((_I,_J),(_G,_H),(_C,_Q),(_C,_S),(_C,_Y),(_C,_Z),(_C,_a),(_C,_b)))
if mibBuilder.loadTexts:cpqSeUSBStorageDeviceSyncFailed.setStatus('')
cpqSePCIeDiskTemperatureFailed=NotificationType((1,3,6,1,4,1,232,0,1015))
cpqSePCIeDiskTemperatureFailed.setObjects(*((_I,_J),(_G,_H),(_C,_U),(_C,_V),(_C,_W),(_C,_x),(_C,_y),(_C,_f)))
if mibBuilder.loadTexts:cpqSePCIeDiskTemperatureFailed.setStatus('')
cpqSePCIeDiskTemperatureOk=NotificationType((1,3,6,1,4,1,232,0,1016))
cpqSePCIeDiskTemperatureOk.setObjects(*((_I,_J),(_G,_H),(_C,_U),(_C,_V),(_C,_W),(_C,_x),(_C,_y),(_C,_f)))
if mibBuilder.loadTexts:cpqSePCIeDiskTemperatureOk.setStatus('')
cpqSePCIeDiskConditionChange=NotificationType((1,3,6,1,4,1,232,0,1017))
cpqSePCIeDiskConditionChange.setObjects(*((_I,_J),(_G,_H),(_C,_U),(_C,_V),(_C,_W),(_C,_Ao),(_C,_f)))
if mibBuilder.loadTexts:cpqSePCIeDiskConditionChange.setStatus('')
cpqSePCIeDiskWearStatusChange=NotificationType((1,3,6,1,4,1,232,0,1018))
cpqSePCIeDiskWearStatusChange.setObjects(*((_I,_J),(_G,_H),(_C,_U),(_C,_V),(_C,_W),(_C,_Ap),(_C,_f)))
if mibBuilder.loadTexts:cpqSePCIeDiskWearStatusChange.setStatus('')
cpqSePciDeviceAddedOrPoweredOn=NotificationType((1,3,6,1,4,1,232,0,1019))
cpqSePciDeviceAddedOrPoweredOn.setObjects(*((_I,_J),(_G,_H),(_C,_l),(_C,_m),(_C,_n)))
if mibBuilder.loadTexts:cpqSePciDeviceAddedOrPoweredOn.setStatus('')
cpqSePciDeviceRemovedOrPoweredOff=NotificationType((1,3,6,1,4,1,232,0,1020))
cpqSePciDeviceRemovedOrPoweredOff.setObjects(*((_I,_J),(_G,_H),(_C,_l),(_C,_m),(_C,_n)))
if mibBuilder.loadTexts:cpqSePciDeviceRemovedOrPoweredOff.setStatus('')
cpqSeNVMeSecureEraseFailed=NotificationType((1,3,6,1,4,1,232,0,1021))
cpqSeNVMeSecureEraseFailed.setObjects(*((_I,_J),(_G,_H),(_C,_U),(_C,_V),(_C,_W),(_C,_Aq),(_C,_Ar)))
if mibBuilder.loadTexts:cpqSeNVMeSecureEraseFailed.setStatus('')
cpqSePcieTrainingFailed=NotificationType((1,3,6,1,4,1,232,0,1022))
cpqSePcieTrainingFailed.setObjects(*((_I,_J),(_G,_H),(_C,_As)))
if mibBuilder.loadTexts:cpqSePcieTrainingFailed.setStatus('')
cpqSePciResetFail=NotificationType((1,3,6,1,4,1,232,0,1023))
cpqSePciResetFail.setObjects(*((_I,_J),(_G,_H),(_C,_X)))
if mibBuilder.loadTexts:cpqSePciResetFail.setStatus('')
cpqSeSecureBootAuthFail=NotificationType((1,3,6,1,4,1,232,0,1024))
cpqSeSecureBootAuthFail.setObjects(*((_I,_J),(_G,_H),(_C,_z)))
if mibBuilder.loadTexts:cpqSeSecureBootAuthFail.setStatus('')
cpqSeSecureBootCertAuthFail=NotificationType((1,3,6,1,4,1,232,0,1025))
cpqSeSecureBootCertAuthFail.setObjects(*((_I,_J),(_G,_H),(_C,_z)))
if mibBuilder.loadTexts:cpqSeSecureBootCertAuthFail.setStatus('')
cpqSeCpuUncorrectableError=NotificationType((1,3,6,1,4,1,232,0,1026))
cpqSeCpuUncorrectableError.setObjects(*((_I,_J),(_G,_H),(_C,_c)))
if mibBuilder.loadTexts:cpqSeCpuUncorrectableError.setStatus('')
cpqSeInternalCpuError=NotificationType((1,3,6,1,4,1,232,0,1027))
cpqSeInternalCpuError.setObjects(*((_I,_J),(_G,_H)))
if mibBuilder.loadTexts:cpqSeInternalCpuError.setStatus('')
mibBuilder.exportSymbols(_C,**{'TruthValue':TruthValue,'cpqSeCpuThresholdPassed':cpqSeCpuThresholdPassed,'cpqSePCCardThermalDegraded':cpqSePCCardThermalDegraded,'cpqSePCCardThermalFailure':cpqSePCCardThermalFailure,'cpqSePCCardThermalSafe':cpqSePCCardThermalSafe,'cpqSe2CpuThresholdPassed':cpqSe2CpuThresholdPassed,'cpqSeCpuStatusChange':cpqSeCpuStatusChange,'cpqSeCpuPowerPodstatusChange':cpqSeCpuPowerPodstatusChange,'cpqSeUSBStorageDeviceAttached':cpqSeUSBStorageDeviceAttached,'cpqSeUSBStorageDeviceRemoved':cpqSeUSBStorageDeviceRemoved,'cpqSeUSBStorageDeviceReadErrorOccurred':cpqSeUSBStorageDeviceReadErrorOccurred,'cpqSeUSBStorageDeviceWriteErrorOccurred':cpqSeUSBStorageDeviceWriteErrorOccurred,'cpqSeUSBStorageDeviceRedundancyLost':cpqSeUSBStorageDeviceRedundancyLost,'cpqSeUSBStorageDeviceRedundancyRestored':cpqSeUSBStorageDeviceRedundancyRestored,'cpqSeUSBStorageDeviceSyncFailed':cpqSeUSBStorageDeviceSyncFailed,'cpqSePCIeDiskTemperatureFailed':cpqSePCIeDiskTemperatureFailed,'cpqSePCIeDiskTemperatureOk':cpqSePCIeDiskTemperatureOk,'cpqSePCIeDiskConditionChange':cpqSePCIeDiskConditionChange,'cpqSePCIeDiskWearStatusChange':cpqSePCIeDiskWearStatusChange,'cpqSePciDeviceAddedOrPoweredOn':cpqSePciDeviceAddedOrPoweredOn,'cpqSePciDeviceRemovedOrPoweredOff':cpqSePciDeviceRemovedOrPoweredOff,'cpqSeNVMeSecureEraseFailed':cpqSeNVMeSecureEraseFailed,'cpqSePcieTrainingFailed':cpqSePcieTrainingFailed,'cpqSePciResetFail':cpqSePciResetFail,'cpqSeSecureBootAuthFail':cpqSeSecureBootAuthFail,'cpqSeSecureBootCertAuthFail':cpqSeSecureBootCertAuthFail,'cpqSeCpuUncorrectableError':cpqSeCpuUncorrectableError,'cpqSeInternalCpuError':cpqSeInternalCpuError,'cpqStdEquipment':cpqStdEquipment,'cpqSeMibRev':cpqSeMibRev,'cpqSeMibRevMajor':cpqSeMibRevMajor,'cpqSeMibRevMinor':cpqSeMibRevMinor,'cpqSeMibCondition':cpqSeMibCondition,'cpqSeComponent':cpqSeComponent,'cpqSeInterface':cpqSeInterface,'cpqSeOsCommon':cpqSeOsCommon,'cpqSeOsCommonPollFreq':cpqSeOsCommonPollFreq,'cpqSeOsCommonModuleTable':cpqSeOsCommonModuleTable,'cpqSeOsCommonModuleEntry':cpqSeOsCommonModuleEntry,_A1:cpqSeOsCommonModuleIndex,'cpqSeOsCommonModuleName':cpqSeOsCommonModuleName,'cpqSeOsCommonModuleVersion':cpqSeOsCommonModuleVersion,'cpqSeOsCommonModuleDate':cpqSeOsCommonModuleDate,'cpqSeOsCommonModulePurpose':cpqSeOsCommonModulePurpose,'cpqSeProcessor':cpqSeProcessor,'cpqSeCpuTable':cpqSeCpuTable,'cpqSeCpuEntry':cpqSeCpuEntry,_c:cpqSeCpuUnitIndex,_d:cpqSeCpuSlot,_t:cpqSeCpuName,_o:cpqSeCpuSpeed,_u:cpqSeCpuStep,_Ah:cpqSeCpuStatus,_p:cpqSeCpuExtSpeed,'cpqSeCpuDesigner':cpqSeCpuDesigner,_e:cpqSeCpuSocketNumber,'cpqSeCpuThreshPassed':cpqSeCpuThreshPassed,_v:cpqSeCpuHwLocation,'cpqSeCpuCellTablePtr':cpqSeCpuCellTablePtr,_Ai:cpqSeCpuPowerpodStatus,'cpqSeCpuArchitectureRevision':cpqSeCpuArchitectureRevision,'cpqSeCpuCore':cpqSeCpuCore,'cpqSeCPUSerialNumber':cpqSeCPUSerialNumber,'cpqSeCPUPartNumber':cpqSeCPUPartNumber,'cpqSeCPUSerialNumberMfgr':cpqSeCPUSerialNumberMfgr,'cpqSeCPUPartNumberMfgr':cpqSeCPUPartNumberMfgr,'cpqSeCPUCoreIndex':cpqSeCPUCoreIndex,'cpqSeCPUMaxSpeed':cpqSeCPUMaxSpeed,'cpqSeCPUCoreThreadIndex':cpqSeCPUCoreThreadIndex,'cpqSeCPUChipGenerationName':cpqSeCPUChipGenerationName,'cpqSeCPUMultiThreadStatus':cpqSeCPUMultiThreadStatus,'cpqSeCPUCoreMaxThreads':cpqSeCPUCoreMaxThreads,'cpqSeCpuLowPowerStatus':cpqSeCpuLowPowerStatus,'cpqSeCpuPrimary':cpqSeCpuPrimary,'cpqSeCpuCoreSteppingText':cpqSeCpuCoreSteppingText,'cpqSeCpuCurrentPerformanceState':cpqSeCpuCurrentPerformanceState,'cpqSeCpuMinPerformanceState':cpqSeCpuMinPerformanceState,'cpqSeCpuMaxPerformanceState':cpqSeCpuMaxPerformanceState,'cpqSeFpuTable':cpqSeFpuTable,'cpqSeFpuEntry':cpqSeFpuEntry,_A2:cpqSeFpuUnitIndex,_A3:cpqSeFpuChipIndex,'cpqSeFpuSlot':cpqSeFpuSlot,'cpqSeFpuName':cpqSeFpuName,'cpqSeFpuSpeed':cpqSeFpuSpeed,'cpqSeFpuType':cpqSeFpuType,'cpqSeFpuHwLocation':cpqSeFpuHwLocation,'cpqSeCpuCacheTable':cpqSeCpuCacheTable,'cpqSeCpuCacheEntry':cpqSeCpuCacheEntry,_A4:cpqSeCpuCacheUnitIndex,_A5:cpqSeCpuCacheLevelIndex,_Ag:cpqSeCpuCacheSize,'cpqSeCpuCacheSpeed':cpqSeCpuCacheSpeed,'cpqSeCpuCacheStatus':cpqSeCpuCacheStatus,'cpqSeCpuCacheWritePolicy':cpqSeCpuCacheWritePolicy,'cpqSeCpuCacheHwLocation':cpqSeCpuCacheHwLocation,'cpqSeCpuCacheCpuSlot':cpqSeCpuCacheCpuSlot,'cpqSeCpuCacheCpuCoreIndex':cpqSeCpuCacheCpuCoreIndex,'cpqSeCpuCondition':cpqSeCpuCondition,'cpqSeMemory':cpqSeMemory,'cpqSeBaseMem':cpqSeBaseMem,'cpqSeTotalMem':cpqSeTotalMem,'cpqSeTotalMemMB':cpqSeTotalMemMB,'cpqSeIsaCmos':cpqSeIsaCmos,'cpqSeIsaCmosRaw':cpqSeIsaCmosRaw,'cpqSeEisaNvram':cpqSeEisaNvram,'cpqSeEisaSlotTable':cpqSeEisaSlotTable,'cpqSeEisaSlotEntry':cpqSeEisaSlotEntry,_A6:cpqSeEisaSlotIndex,'cpqSeEisaSlotRaw':cpqSeEisaSlotRaw,'cpqSeEisaSlotBoardId':cpqSeEisaSlotBoardId,'cpqSeEisaSlotBoardName':cpqSeEisaSlotBoardName,'cpqSeEisaSlotCfRev':cpqSeEisaSlotCfRev,'cpqSeEisaSlotType':cpqSeEisaSlotType,'cpqSeEisaFunctTable':cpqSeEisaFunctTable,'cpqSeEisaFunctEntry':cpqSeEisaFunctEntry,_A7:cpqSeEisaFunctSlotIndex,_A8:cpqSeEisaFunctIndex,'cpqSeEisaFunctStatus':cpqSeEisaFunctStatus,'cpqSeEisaFunctType':cpqSeEisaFunctType,'cpqSeEisaFunctCfgRev':cpqSeEisaFunctCfgRev,'cpqSeEisaFunctSels':cpqSeEisaFunctSels,'cpqSeEisaFunctInfo':cpqSeEisaFunctInfo,'cpqSeEisaMemTable':cpqSeEisaMemTable,'cpqSeEisaMemEntry':cpqSeEisaMemEntry,_A9:cpqSeEisaMemSlotIndex,_AA:cpqSeEisaMemFunctIndex,_AB:cpqSeEisaMemAllocIndex,'cpqSeEisaMemStartAddr':cpqSeEisaMemStartAddr,'cpqSeEisaMemSize':cpqSeEisaMemSize,'cpqSeEisaMemShare':cpqSeEisaMemShare,'cpqSeEisaMemType':cpqSeEisaMemType,'cpqSeEisaMemCache':cpqSeEisaMemCache,'cpqSeEisaMemAccess':cpqSeEisaMemAccess,'cpqSeEisaMemDecode':cpqSeEisaMemDecode,'cpqSeEisaMemDataSize':cpqSeEisaMemDataSize,'cpqSeEisaIntTable':cpqSeEisaIntTable,'cpqSeEisaIntEntry':cpqSeEisaIntEntry,_AC:cpqSeEisaIntSlotIndex,_AD:cpqSeEisaIntFunctIndex,_AE:cpqSeEisaIntAllocIndex,'cpqSeEisaIntNum':cpqSeEisaIntNum,'cpqSeEisaIntShare':cpqSeEisaIntShare,'cpqSeEisaIntTrigger':cpqSeEisaIntTrigger,'cpqSeEisaDmaTable':cpqSeEisaDmaTable,'cpqSeEisaDmaEntry':cpqSeEisaDmaEntry,_AF:cpqSeEisaDmaSlotIndex,_AG:cpqSeEisaDmaFunctIndex,_AH:cpqSeEisaDmaAllocIndex,'cpqSeEisaDmaChannel':cpqSeEisaDmaChannel,'cpqSeEisaDmaShare':cpqSeEisaDmaShare,'cpqSeEisaDmaTiming':cpqSeEisaDmaTiming,'cpqSeEisaDmaXfer':cpqSeEisaDmaXfer,'cpqSeEisaDmaXferCount':cpqSeEisaDmaXferCount,'cpqSeEisaPortTable':cpqSeEisaPortTable,'cpqSeEisaPortEntry':cpqSeEisaPortEntry,_AI:cpqSeEisaPortSlotIndex,_AJ:cpqSeEisaPortFunctIndex,_AK:cpqSeEisaPortAllocIndex,'cpqSeEisaPortAddr':cpqSeEisaPortAddr,'cpqSeEisaPortShare':cpqSeEisaPortShare,'cpqSeEisaPortSize':cpqSeEisaPortSize,'cpqSeEisaFreeFormTable':cpqSeEisaFreeFormTable,'cpqSeEisaFreeFormEntry':cpqSeEisaFreeFormEntry,_AL:cpqSeEisaFreeFormSlotIndex,_AM:cpqSeEisaFreeFormFunctIndex,'cpqSeEisaFreeFormValue':cpqSeEisaFreeFormValue,'cpqSeEisaInitTable':cpqSeEisaInitTable,'cpqSeEisaInitEntry':cpqSeEisaInitEntry,_AN:cpqSeEisaInitSlotIndex,_AO:cpqSeEisaInitFunctIndex,_AP:cpqSeEisaInitAllocIndex,'cpqSeEisaInitUseMask':cpqSeEisaInitUseMask,'cpqSeEisaInitAccess':cpqSeEisaInitAccess,'cpqSeEisaInitAddr':cpqSeEisaInitAddr,'cpqSeEisaInitValue':cpqSeEisaInitValue,'cpqSeEisaInitMask':cpqSeEisaInitMask,'cpqSeRom':cpqSeRom,'cpqSeSysRomVer':cpqSeSysRomVer,'cpqSeOptRomTable':cpqSeOptRomTable,'cpqSeOptRomEntry':cpqSeOptRomEntry,_AQ:cpqSeOptRomAddrIndex,'cpqSeOptRomSize':cpqSeOptRomSize,'cpqSeBiosRomDataRaw':cpqSeBiosRomDataRaw,'cpqSeRedundantSysRomVer':cpqSeRedundantSysRomVer,'cpqSeSmbiosVer':cpqSeSmbiosVer,'cpqSeMPFwVer':cpqSeMPFwVer,'cpqSeBMCFwVer':cpqSeBMCFwVer,'cpqSeHPVMFwVer':cpqSeHPVMFwVer,'cpqSeKeyboard':cpqSeKeyboard,'cpqSeKeyboardDesc':cpqSeKeyboardDesc,'cpqSeVideo':cpqSeVideo,'cpqSeVideoDesc':cpqSeVideoDesc,'cpqSeSerialPort':cpqSeSerialPort,'cpqSeSerialPortTable':cpqSeSerialPortTable,'cpqSeSerialPortEntry':cpqSeSerialPortEntry,_AR:cpqSeSerialPortIndex,'cpqSeSerialPortAddr':cpqSeSerialPortAddr,'cpqSeSerialPortDesc':cpqSeSerialPortDesc,'cpqSeSerialPortHwLocation':cpqSeSerialPortHwLocation,'cpqSeParallelPort':cpqSeParallelPort,'cpqSeParallelPortTable':cpqSeParallelPortTable,'cpqSeParallelPortEntry':cpqSeParallelPortEntry,_AS:cpqSeParallelPortIndex,'cpqSeParallelPortAddr':cpqSeParallelPortAddr,'cpqSeParallelPortDesc':cpqSeParallelPortDesc,'cpqSeParrallelPortHwLocation':cpqSeParrallelPortHwLocation,'cpqSeFloppyDisk':cpqSeFloppyDisk,'cpqSeFloppyDiskTable':cpqSeFloppyDiskTable,'cpqSeFloppyDiskEntry':cpqSeFloppyDiskEntry,_AT:cpqSeFloppyDiskIndex,'cpqSeFloppyDiskType':cpqSeFloppyDiskType,'cpqSeFloppyDiskHwLocation':cpqSeFloppyDiskHwLocation,'cpqSeFixedDisk':cpqSeFixedDisk,'cpqSeFixedDiskTable':cpqSeFixedDiskTable,'cpqSeFixedDiskEntry':cpqSeFixedDiskEntry,_AU:cpqSeFixedDiskIndex,'cpqSeFixedDiskType':cpqSeFixedDiskType,'cpqSeFixedDiskCyls':cpqSeFixedDiskCyls,'cpqSeFixedDiskHeads':cpqSeFixedDiskHeads,'cpqSeFixedDiskSectors':cpqSeFixedDiskSectors,'cpqSeFixedDiskCapacity':cpqSeFixedDiskCapacity,'cpqSeFixedDiskHwLocation':cpqSeFixedDiskHwLocation,'cpqSePci':cpqSePci,'cpqSePciSlotTable':cpqSePciSlotTable,'cpqSePciSlotEntry':cpqSePciSlotEntry,_AV:cpqSePciSlotBusNumberIndex,_AW:cpqSePciSlotDeviceNumberIndex,'cpqSePciPhysSlot':cpqSePciPhysSlot,'cpqSePciSlotSubSystemID':cpqSePciSlotSubSystemID,'cpqSePciSlotBoardName':cpqSePciSlotBoardName,'cpqSePciSlotWidth':cpqSePciSlotWidth,'cpqSePciSlotSpeed':cpqSePciSlotSpeed,'cpqSePciSlotExtendedInfo':cpqSePciSlotExtendedInfo,'cpqSePciSlotType':cpqSePciSlotType,'cpqSePciSlotCurrentMode':cpqSePciSlotCurrentMode,'cpqSePciMaxSlotSpeed':cpqSePciMaxSlotSpeed,'cpqSePciXMaxSlotSpeed':cpqSePciXMaxSlotSpeed,'cpqSePciCurrentSlotSpeed':cpqSePciCurrentSlotSpeed,_z:cpqSePciHwLocation,'cpqSePciSlotIOCTablePtr':cpqSePciSlotIOCTablePtr,'cpqSePciSlotHeaderType':cpqSePciSlotHeaderType,'cpqSePciIsSlot0Embedded':cpqSePciIsSlot0Embedded,'cpqSePcieSlotMaxLinkSpeed':cpqSePcieSlotMaxLinkSpeed,'cpqSePcieSlotMaxLinkWidth':cpqSePcieSlotMaxLinkWidth,'cpqSePciFunctTable':cpqSePciFunctTable,'cpqSePciFunctEntry':cpqSePciFunctEntry,_l:cpqSePciFunctBusNumberIndex,_m:cpqSePciFunctDeviceNumberIndex,_n:cpqSePciFunctIndex,'cpqSePciFunctClassCode':cpqSePciFunctClassCode,'cpqSePciFunctClassDescription':cpqSePciFunctClassDescription,'cpqSePciFunctDeviceID':cpqSePciFunctDeviceID,'cpqSePciFunctVendorID':cpqSePciFunctVendorID,'cpqSePciFunctRevID':cpqSePciFunctRevID,'cpqSePciFunctIntLine':cpqSePciFunctIntLine,'cpqSePciFunctDevStatus':cpqSePciFunctDevStatus,'cpqSePciFunctHwLocation':cpqSePciFunctHwLocation,'cpqSePcieFunctNegotiatedLinkSpeed':cpqSePcieFunctNegotiatedLinkSpeed,'cpqSePcieFunctNegotiatedLinkWidth':cpqSePcieFunctNegotiatedLinkWidth,'cpqSePcieFunctMaxLinkSpeed':cpqSePcieFunctMaxLinkSpeed,'cpqSePcieFunctMaxLinkWidth':cpqSePcieFunctMaxLinkWidth,'cpqSePciMemoryTable':cpqSePciMemoryTable,'cpqSePciMemoryEntry':cpqSePciMemoryEntry,_AX:cpqSePciMemoryBusNumberIndex,_AY:cpqSePciMemoryDeviceNumberIndex,_AZ:cpqSePciMemoryFunctionIndex,_Aa:cpqSePciMemoryIndex,'cpqSePciMemoryBaseAddr':cpqSePciMemoryBaseAddr,'cpqSePciMemoryType':cpqSePciMemoryType,'cpqSePciMemorySize':cpqSePciMemorySize,'cpqSePciMemoryHwLocation':cpqSePciMemoryHwLocation,'cpqSePciSegmentMode':cpqSePciSegmentMode,_As:cpqSePciePhySlot,'cpqSePCCard':cpqSePCCard,'cpqSePCCardSlotTable':cpqSePCCardSlotTable,'cpqSePCCardSlotEntry':cpqSePCCardSlotEntry,_X:cpqSePCCardSlotIndex,'cpqSePCCardCondition':cpqSePCCardCondition,'cpqSePCCardPhysLocation':cpqSePCCardPhysLocation,'cpqSePCCardSlotType':cpqSePCCardSlotType,'cpqSePCCardSlotWidth':cpqSePCCardSlotWidth,'cpqSePCCardSlotThermalCapacity':cpqSePCCardSlotThermalCapacity,'cpqSePCCardSlotThermalSensor':cpqSePCCardSlotThermalSensor,'cpqSePCCardSlotPowerState':cpqSePCCardSlotPowerState,'cpqSePCCardStatus':cpqSePCCardStatus,_r:cpqSePCCardDeviceInfo,_s:cpqSePCCardProductInfo,'cpqSePCCardSerialNumber':cpqSePCCardSerialNumber,'cpqSePCCardAssetTag':cpqSePCCardAssetTag,'cpqSeUSBPort':cpqSeUSBPort,'cpqSeUSBPortTable':cpqSeUSBPortTable,'cpqSeUSBPortEntry':cpqSeUSBPortEntry,_Q:cpqSeUSBPortIndex,'cpqSeUSBPortType':cpqSeUSBPortType,'cpqSeUSBPortHwLocation':cpqSeUSBPortHwLocation,'cpqSeUSBPortStatus':cpqSeUSBPortStatus,_S:cpqSeUSBPortDeviceName,'cpqSeUSBPortDeviceCapacity':cpqSeUSBPortDeviceCapacity,'cpqSeUSBPortDeviceManufacturer':cpqSeUSBPortDeviceManufacturer,_Y:cpqSeUSBPortDeviceModel,_Z:cpqSeUSBPortDeviceFWVersion,_a:cpqSeUSBPortDeviceSerialNumber,_b:cpqSeUSBPortDevicePartNumber,'cpqSeUSBPortDeviceCount':cpqSeUSBPortDeviceCount,_Aj:cpqSeUSBPortDeviceReadErrorCount,_Al:cpqSeUSBPortDeviceWriteErrorCount,_Ak:cpqSeUSBPortDeviceReadThreshold,_Am:cpqSeUSBPortDeviceWriteThreshold,'cpqSeUSBPortDeviceStatus':cpqSeUSBPortDeviceStatus,'cpqSeUSBPortDeviceFeature':cpqSeUSBPortDeviceFeature,_An:cpqSeUSBPortDeviceFailedSlot,_w:cpqSeUSBPortDeviceLastSlotWithError,'cpqSeUSBPortDeviceFaultTolerance':cpqSeUSBPortDeviceFaultTolerance,'cpqSeUSBPortDevicePresent':cpqSeUSBPortDevicePresent,'cpqSeCell':cpqSeCell,'cpqSeCellTable':cpqSeCellTable,'cpqSeCellEntry':cpqSeCellEntry,_Ab:cpqSeCellUnitIndex,'cpqSeCellCabinetNumber':cpqSeCellCabinetNumber,'cpqSeCellCellNumber':cpqSeCellCellNumber,'cpqSeCellIOCTablePtr':cpqSeCellIOCTablePtr,'cpqSeCellPDHCFirmwareRevision':cpqSeCellPDHCFirmwareRevision,'cpqSeCellSysFwVersion':cpqSeCellSysFwVersion,'cpqSeCellBootInhibited':cpqSeCellBootInhibited,'cpqSeCellToScanBusConnectionStatus':cpqSeCellToScanBusConnectionStatus,'cpqSeCellHasCoreIO':cpqSeCellHasCoreIO,'cpqSeCellBoardSpeed':cpqSeCellBoardSpeed,'cpqSeCellPresent':cpqSeCellPresent,'cpqSeCellHasPower':cpqSeCellHasPower,'cpqSeCellReadyForReconfig':cpqSeCellReadyForReconfig,'cpqSeCellTotalMemory':cpqSeCellTotalMemory,'cpqSeCellLEDState':cpqSeCellLEDState,'cpqSeCellState':cpqSeCellState,'cpqSeCellCLMRequestPercentage':cpqSeCellCLMRequestPercentage,'cpqSeCellCLMRequestSize':cpqSeCellCLMRequestSize,'cpqSeCellCLMAllocatedSize':cpqSeCellCLMAllocatedSize,'cpqSeCellInterleaveAllocatedSize':cpqSeCellInterleaveAllocatedSize,'cpqSeCellHasInterleaveMem':cpqSeCellHasInterleaveMem,'cpqSeCellSerialNumber':cpqSeCellSerialNumber,'cpqSeCellCLMCondition':cpqSeCellCLMCondition,'cpqSeIOC':cpqSeIOC,'cpqSeIOCTable':cpqSeIOCTable,'cpqSeIOCEntry':cpqSeIOCEntry,_Ac:cpqSeIOCUnitIndex,'cpqSeIOCCabinetNumber':cpqSeIOCCabinetNumber,'cpqSeIOCBayNumber':cpqSeIOCBayNumber,'cpqSeIOCIOCNumber':cpqSeIOCIOCNumber,'cpqSeIOCPowerState':cpqSeIOCPowerState,'cpqSeIOCLEDState':cpqSeIOCLEDState,'cpqSePartition':cpqSePartition,'cpqSePartitionTotalCPU':cpqSePartitionTotalCPU,'cpqSePartitionAvailableCellSlots':cpqSePartitionAvailableCellSlots,'cpqSePartitionInstalledCells':cpqSePartitionInstalledCells,'cpqSePartitionPoweredOnCells':cpqSePartitionPoweredOnCells,'cpqSePartitionReadyForReconfigCells':cpqSePartitionReadyForReconfigCells,'cpqSePartitionMemInterleavingType':cpqSePartitionMemInterleavingType,'cpqSePartitionName':cpqSePartitionName,'cpqSePartitionCoreCell':cpqSePartitionCoreCell,'cpqSePartitionCoreCellCabinet':cpqSePartitionCoreCellCabinet,'cpqSePartitionCLMRequestPercentage':cpqSePartitionCLMRequestPercentage,'cpqSePartitionCLMRequestSize':cpqSePartitionCLMRequestSize,'cpqSePartitionCLMAllocatedSize':cpqSePartitionCLMAllocatedSize,'cpqSePartitionInterleaveAllocatedSize':cpqSePartitionInterleaveAllocatedSize,'cpqSePartitionHasInterleaveMem':cpqSePartitionHasInterleaveMem,'cpqSePartitionNumber':cpqSePartitionNumber,'cpqSeCabinet':cpqSeCabinet,'cpqSeCabinetTable':cpqSeCabinetTable,'cpqSeCabinetEntry':cpqSeCabinetEntry,_Ad:cpqSeCabinetUnitIndex,'cpqSeCabinetCPULED':cpqSeCabinetCPULED,'cpqSeCabinetIOXLED':cpqSeCabinetIOXLED,'cpqSeCabinetTypeNum':cpqSeCabinetTypeNum,'cpqSeCabinetLED':cpqSeCabinetLED,'cpqSeComplex':cpqSeComplex,'cpqSeComplexUUID':cpqSeComplexUUID,'cpqSeComplexTotalCabinet':cpqSeComplexTotalCabinet,'cpqSeComplexComputeCabinet':cpqSeComplexComputeCabinet,'cpqSeComplexIOXCabinet':cpqSeComplexIOXCabinet,'cpqSeComplexName':cpqSeComplexName,'cpqSeComplexLockedProperty':cpqSeComplexLockedProperty,'cpqSeComplexCellSlotStatusTable':cpqSeComplexCellSlotStatusTable,'cpqSeComplexCellSlotStatusEntry':cpqSeComplexCellSlotStatusEntry,_Ae:cpqSeComplexCellSlotStatusIndex,'cpqSeComplexCellSlotStatusCabinetNo':cpqSeComplexCellSlotStatusCabinetNo,'cpqSeComplexCellSlotStatusSlotNo':cpqSeComplexCellSlotStatusSlotNo,'cpqSeComplexCellSlotStatus':cpqSeComplexCellSlotStatus,'cpqSeComplexCellSlotPartitionNo':cpqSeComplexCellSlotPartitionNo,'cpqSeComplexCellSlotPartitionName':cpqSeComplexCellSlotPartitionName,'cpqSeLED':cpqSeLED,'cpqSeLEDTable':cpqSeLEDTable,'cpqSeLEDEntry':cpqSeLEDEntry,_Af:cpqSeLEDIndex,'cpqSeLEDState':cpqSeLEDState,'cpqSeLEDStateDuration':cpqSeLEDStateDuration,'cpqSeLEDLocationType':cpqSeLEDLocationType,'cpqSeLEDDescription':cpqSeLEDDescription,'cpqSeLEDHardwareLocation':cpqSeLEDHardwareLocation,'cpqSeUSBDevice':cpqSeUSBDevice,'cpqSeUSBDeviceType':cpqSeUSBDeviceType,'cpqSeUSBDeviceName':cpqSeUSBDeviceName,'cpqSePCIeDisk':cpqSePCIeDisk,'cpqSePCIeDiskTable':cpqSePCIeDiskTable,'cpqSePCIeDiskEntry':cpqSePCIeDiskEntry,_U:cpqSePCIeDiskPCIBusIndex,_V:cpqSePCIeDiskPCIDeviceIndex,_W:cpqSePCIeDiskPCIFunctionIndex,'cpqSePCIeDiskModel':cpqSePCIeDiskModel,'cpqSePCIeDiskFwRev':cpqSePCIeDiskFwRev,_Aq:cpqSePCIeDiskSerialNumber,'cpqSePCIeDiskCapacityMB':cpqSePCIeDiskCapacityMB,_Ao:cpqSePCIeDiskCondition,_x:cpqSePCIeDiskCurrentTemperature,_y:cpqSePCIeDiskThresholdTemperature,_f:cpqSePCIeDiskHwLocation,'cpqSePCIeDiskOsName':cpqSePCIeDiskOsName,_Ap:cpqSePCIeDiskWearStatus,'cpqSePCIeDiskPowerOnHours':cpqSePCIeDiskPowerOnHours,'cpqSePCIeDiskPercntEndrnceUsed':cpqSePCIeDiskPercntEndrnceUsed,'cpqSePCIeDiskTableCondition':cpqSePCIeDiskTableCondition,_Ar:cpqSePCIeEraseFailureType})