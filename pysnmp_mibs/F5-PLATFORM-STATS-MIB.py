_AP='platformFantrayGroup'
_AO='platformFwVersionGroup'
_AN='platformFpgaGroup'
_AM='platformMemGroup'
_AL='platformTempGroup'
_AK='platformDiskGroup'
_AJ='platformCPUGroup'
_AI='fan-12-speed'
_AH='fan-11-speed'
_AG='fan-10-speed'
_AF='fan-9-speed'
_AE='fan-8-speed'
_AD='fan-7-speed'
_AC='fan-6-speed'
_AB='fan-5-speed'
_AA='fan-4-speed'
_A9='fan-3-speed'
_A8='fan-2-speed'
_A7='fan-1-speed'
_A6='fwUpdateStatus'
_A5='configurable'
_A4='fwVersion'
_A3='fpgaVersion'
_A2='memPlatformUsed'
_A1='memPlatformTotal'
_A0='memPercentageUsed'
_z='memAvailable'
_y='tempMaximum'
_x='tempMinimum'
_w='tempAverage'
_v='tempCurrent'
_u='diskWriteLatencyMs'
_t='diskWriteBytes'
_s='diskWriteMerged'
_r='diskWriteIops'
_q='diskReadLatencyMs'
_p='diskReadBytes'
_o='diskReadMerged'
_n='diskReadIops'
_m='diskTotalIops'
_l='diskPercentageUsed'
_k='diskType'
_j='diskSize'
_i='diskSerialNo'
_h='diskVersion'
_g='diskVendor'
_f='diskModel'
_e='coreTotal5minAvg'
_d='coreTotal1minAvg'
_c='coreTotal5secAvg'
_b='coreCurrent'
_a='cpuTotal5minAvg'
_Z='cpuTotal1minAvg'
_Y='cpuTotal5secAvg'
_X='cpuCurrent'
_W='cpuCore'
_V='cpuModelName'
_U='cpuThreadCnt'
_T='cpuStepping'
_S='cpuFreq'
_R='cpuCoreCnt'
_Q='cpuCacheSize'
_P='fwName'
_O='fpgaIndex'
_N='IOPs'
_M='coreIndex'
_L='cpuIndex'
_K='centigrade'
_J='diskName'
_I='Integer32'
_H='bytes'
_G='percentage'
_F='RPM'
_E='index'
_D='DisplayString'
_C='read-only'
_B='F5-PLATFORM-STATS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
f5Compliance,platform=mibBuilder.importSymbols('F5-COMMON-SMI-MIB','f5Compliance','platform')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention','TruthValue')
f5PlatformStats=ModuleIdentity((1,3,6,1,4,1,12276,1,2))
class PlatformStatsIndex(TextualConvention,OctetString):status=_A;displayHint='1t';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
class String(DisplayString):status=_A;displayHint='1t';subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_F5PlatformStatsObjects_ObjectIdentity=ObjectIdentity
f5PlatformStatsObjects=_F5PlatformStatsObjects_ObjectIdentity((1,3,6,1,4,1,12276,1,2,1))
_PlatformCpuStatsTable_ObjectIdentity=ObjectIdentity
platformCpuStatsTable=_PlatformCpuStatsTable_ObjectIdentity((1,3,6,1,4,1,12276,1,2,1,1))
_CpuProcessorStatsTable_Object=MibTable
cpuProcessorStatsTable=_CpuProcessorStatsTable_Object((1,3,6,1,4,1,12276,1,2,1,1,1))
if mibBuilder.loadTexts:cpuProcessorStatsTable.setStatus(_A)
_CpuProcessorStatsEntry_Object=MibTableRow
cpuProcessorStatsEntry=_CpuProcessorStatsEntry_Object((1,3,6,1,4,1,12276,1,2,1,1,1,1))
cpuProcessorStatsEntry.setIndexNames((0,_B,_E),(0,_B,_L))
if mibBuilder.loadTexts:cpuProcessorStatsEntry.setStatus(_A)
_Index_Type=PlatformStatsIndex
_Index_Object=MibTableColumn
index=_Index_Object((1,3,6,1,4,1,12276,1,2,1,1,1,1,1),_Index_Type())
index.setMaxAccess(_C)
if mibBuilder.loadTexts:index.setStatus(_A)
class _CpuIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CpuIndex_Type.__name__=_I
_CpuIndex_Object=MibTableColumn
cpuIndex=_CpuIndex_Object((1,3,6,1,4,1,12276,1,2,1,1,1,1,2),_CpuIndex_Type())
cpuIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuIndex.setStatus(_A)
_CpuCacheSize_Type=String
_CpuCacheSize_Object=MibTableColumn
cpuCacheSize=_CpuCacheSize_Object((1,3,6,1,4,1,12276,1,2,1,1,1,1,3),_CpuCacheSize_Type())
cpuCacheSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuCacheSize.setStatus(_A)
_CpuCoreCnt_Type=String
_CpuCoreCnt_Object=MibTableColumn
cpuCoreCnt=_CpuCoreCnt_Object((1,3,6,1,4,1,12276,1,2,1,1,1,1,4),_CpuCoreCnt_Type())
cpuCoreCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuCoreCnt.setStatus(_A)
_CpuFreq_Type=String
_CpuFreq_Object=MibTableColumn
cpuFreq=_CpuFreq_Object((1,3,6,1,4,1,12276,1,2,1,1,1,1,5),_CpuFreq_Type())
cpuFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuFreq.setStatus(_A)
_CpuStepping_Type=String
_CpuStepping_Object=MibTableColumn
cpuStepping=_CpuStepping_Object((1,3,6,1,4,1,12276,1,2,1,1,1,1,6),_CpuStepping_Type())
cpuStepping.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuStepping.setStatus(_A)
_CpuThreadCnt_Type=String
_CpuThreadCnt_Object=MibTableColumn
cpuThreadCnt=_CpuThreadCnt_Object((1,3,6,1,4,1,12276,1,2,1,1,1,1,7),_CpuThreadCnt_Type())
cpuThreadCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuThreadCnt.setStatus(_A)
_CpuModelName_Type=String
_CpuModelName_Object=MibTableColumn
cpuModelName=_CpuModelName_Object((1,3,6,1,4,1,12276,1,2,1,1,1,1,8),_CpuModelName_Type())
cpuModelName.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuModelName.setStatus(_A)
_CpuUtilizationStatsTable_Object=MibTable
cpuUtilizationStatsTable=_CpuUtilizationStatsTable_Object((1,3,6,1,4,1,12276,1,2,1,1,2))
if mibBuilder.loadTexts:cpuUtilizationStatsTable.setStatus(_A)
_CpuUtilizationStatsEntry_Object=MibTableRow
cpuUtilizationStatsEntry=_CpuUtilizationStatsEntry_Object((1,3,6,1,4,1,12276,1,2,1,1,2,1))
cpuUtilizationStatsEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:cpuUtilizationStatsEntry.setStatus(_A)
class _CpuCore_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_CpuCore_Type.__name__=_D
_CpuCore_Object=MibTableColumn
cpuCore=_CpuCore_Object((1,3,6,1,4,1,12276,1,2,1,1,2,1,1),_CpuCore_Type())
cpuCore.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuCore.setStatus(_A)
_CpuCurrent_Type=Integer32
_CpuCurrent_Object=MibTableColumn
cpuCurrent=_CpuCurrent_Object((1,3,6,1,4,1,12276,1,2,1,1,2,1,2),_CpuCurrent_Type())
cpuCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuCurrent.setStatus(_A)
if mibBuilder.loadTexts:cpuCurrent.setUnits(_G)
_CpuTotal5secAvg_Type=Integer32
_CpuTotal5secAvg_Object=MibTableColumn
cpuTotal5secAvg=_CpuTotal5secAvg_Object((1,3,6,1,4,1,12276,1,2,1,1,2,1,3),_CpuTotal5secAvg_Type())
cpuTotal5secAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuTotal5secAvg.setStatus(_A)
if mibBuilder.loadTexts:cpuTotal5secAvg.setUnits(_G)
_CpuTotal1minAvg_Type=Integer32
_CpuTotal1minAvg_Object=MibTableColumn
cpuTotal1minAvg=_CpuTotal1minAvg_Object((1,3,6,1,4,1,12276,1,2,1,1,2,1,4),_CpuTotal1minAvg_Type())
cpuTotal1minAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuTotal1minAvg.setStatus(_A)
if mibBuilder.loadTexts:cpuTotal1minAvg.setUnits(_G)
_CpuTotal5minAvg_Type=Integer32
_CpuTotal5minAvg_Object=MibTableColumn
cpuTotal5minAvg=_CpuTotal5minAvg_Object((1,3,6,1,4,1,12276,1,2,1,1,2,1,5),_CpuTotal5minAvg_Type())
cpuTotal5minAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:cpuTotal5minAvg.setStatus(_A)
if mibBuilder.loadTexts:cpuTotal5minAvg.setUnits(_G)
_CpuCoreStatsTable_Object=MibTable
cpuCoreStatsTable=_CpuCoreStatsTable_Object((1,3,6,1,4,1,12276,1,2,1,1,3))
if mibBuilder.loadTexts:cpuCoreStatsTable.setStatus(_A)
_CpuCoreStatsEntry_Object=MibTableRow
cpuCoreStatsEntry=_CpuCoreStatsEntry_Object((1,3,6,1,4,1,12276,1,2,1,1,3,1))
cpuCoreStatsEntry.setIndexNames((0,_B,_E),(0,_B,_M))
if mibBuilder.loadTexts:cpuCoreStatsEntry.setStatus(_A)
class _CoreIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CoreIndex_Type.__name__=_I
_CoreIndex_Object=MibTableColumn
coreIndex=_CoreIndex_Object((1,3,6,1,4,1,12276,1,2,1,1,3,1,1),_CoreIndex_Type())
coreIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:coreIndex.setStatus(_A)
class _CoreName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_CoreName_Type.__name__=_D
_CoreName_Object=MibTableColumn
coreName=_CoreName_Object((1,3,6,1,4,1,12276,1,2,1,1,3,1,2),_CoreName_Type())
coreName.setMaxAccess(_C)
if mibBuilder.loadTexts:coreName.setStatus(_A)
_CoreCurrent_Type=Integer32
_CoreCurrent_Object=MibTableColumn
coreCurrent=_CoreCurrent_Object((1,3,6,1,4,1,12276,1,2,1,1,3,1,3),_CoreCurrent_Type())
coreCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:coreCurrent.setStatus(_A)
if mibBuilder.loadTexts:coreCurrent.setUnits(_G)
_CoreTotal5secAvg_Type=Integer32
_CoreTotal5secAvg_Object=MibTableColumn
coreTotal5secAvg=_CoreTotal5secAvg_Object((1,3,6,1,4,1,12276,1,2,1,1,3,1,4),_CoreTotal5secAvg_Type())
coreTotal5secAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:coreTotal5secAvg.setStatus(_A)
if mibBuilder.loadTexts:coreTotal5secAvg.setUnits(_G)
_CoreTotal1minAvg_Type=Integer32
_CoreTotal1minAvg_Object=MibTableColumn
coreTotal1minAvg=_CoreTotal1minAvg_Object((1,3,6,1,4,1,12276,1,2,1,1,3,1,5),_CoreTotal1minAvg_Type())
coreTotal1minAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:coreTotal1minAvg.setStatus(_A)
if mibBuilder.loadTexts:coreTotal1minAvg.setUnits(_G)
_CoreTotal5minAvg_Type=Integer32
_CoreTotal5minAvg_Object=MibTableColumn
coreTotal5minAvg=_CoreTotal5minAvg_Object((1,3,6,1,4,1,12276,1,2,1,1,3,1,6),_CoreTotal5minAvg_Type())
coreTotal5minAvg.setMaxAccess(_C)
if mibBuilder.loadTexts:coreTotal5minAvg.setStatus(_A)
if mibBuilder.loadTexts:coreTotal5minAvg.setUnits(_G)
_PlatformDiskStatsTable_ObjectIdentity=ObjectIdentity
platformDiskStatsTable=_PlatformDiskStatsTable_ObjectIdentity((1,3,6,1,4,1,12276,1,2,1,2))
_DiskInfoTable_Object=MibTable
diskInfoTable=_DiskInfoTable_Object((1,3,6,1,4,1,12276,1,2,1,2,1))
if mibBuilder.loadTexts:diskInfoTable.setStatus(_A)
_DiskInfoEntry_Object=MibTableRow
diskInfoEntry=_DiskInfoEntry_Object((1,3,6,1,4,1,12276,1,2,1,2,1,1))
diskInfoEntry.setIndexNames((0,_B,_E),(0,_B,_J))
if mibBuilder.loadTexts:diskInfoEntry.setStatus(_A)
class _DiskName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_DiskName_Type.__name__=_D
_DiskName_Object=MibTableColumn
diskName=_DiskName_Object((1,3,6,1,4,1,12276,1,2,1,2,1,1,2),_DiskName_Type())
diskName.setMaxAccess(_C)
if mibBuilder.loadTexts:diskName.setStatus(_A)
class _DiskModel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_DiskModel_Type.__name__=_D
_DiskModel_Object=MibTableColumn
diskModel=_DiskModel_Object((1,3,6,1,4,1,12276,1,2,1,2,1,1,3),_DiskModel_Type())
diskModel.setMaxAccess(_C)
if mibBuilder.loadTexts:diskModel.setStatus(_A)
class _DiskVendor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_DiskVendor_Type.__name__=_D
_DiskVendor_Object=MibTableColumn
diskVendor=_DiskVendor_Object((1,3,6,1,4,1,12276,1,2,1,2,1,1,4),_DiskVendor_Type())
diskVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:diskVendor.setStatus(_A)
class _DiskVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_DiskVersion_Type.__name__=_D
_DiskVersion_Object=MibTableColumn
diskVersion=_DiskVersion_Object((1,3,6,1,4,1,12276,1,2,1,2,1,1,5),_DiskVersion_Type())
diskVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:diskVersion.setStatus(_A)
class _DiskSerialNo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_DiskSerialNo_Type.__name__=_D
_DiskSerialNo_Object=MibTableColumn
diskSerialNo=_DiskSerialNo_Object((1,3,6,1,4,1,12276,1,2,1,2,1,1,6),_DiskSerialNo_Type())
diskSerialNo.setMaxAccess(_C)
if mibBuilder.loadTexts:diskSerialNo.setStatus(_A)
class _DiskSize_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_DiskSize_Type.__name__=_D
_DiskSize_Object=MibTableColumn
diskSize=_DiskSize_Object((1,3,6,1,4,1,12276,1,2,1,2,1,1,7),_DiskSize_Type())
diskSize.setMaxAccess(_C)
if mibBuilder.loadTexts:diskSize.setStatus(_A)
class _DiskType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_DiskType_Type.__name__=_D
_DiskType_Object=MibTableColumn
diskType=_DiskType_Object((1,3,6,1,4,1,12276,1,2,1,2,1,1,8),_DiskType_Type())
diskType.setMaxAccess(_C)
if mibBuilder.loadTexts:diskType.setStatus(_A)
_DiskUtilizationStatsTable_Object=MibTable
diskUtilizationStatsTable=_DiskUtilizationStatsTable_Object((1,3,6,1,4,1,12276,1,2,1,2,2))
if mibBuilder.loadTexts:diskUtilizationStatsTable.setStatus(_A)
_DiskUtilizationStatsEntry_Object=MibTableRow
diskUtilizationStatsEntry=_DiskUtilizationStatsEntry_Object((1,3,6,1,4,1,12276,1,2,1,2,2,1))
diskUtilizationStatsEntry.setIndexNames((0,_B,_E),(0,_B,_J))
if mibBuilder.loadTexts:diskUtilizationStatsEntry.setStatus(_A)
class _DiskPercentageUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_DiskPercentageUsed_Type.__name__=_I
_DiskPercentageUsed_Object=MibTableColumn
diskPercentageUsed=_DiskPercentageUsed_Object((1,3,6,1,4,1,12276,1,2,1,2,2,1,3),_DiskPercentageUsed_Type())
diskPercentageUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:diskPercentageUsed.setStatus(_A)
if mibBuilder.loadTexts:diskPercentageUsed.setUnits(_G)
_DiskTotalIops_Type=Counter64
_DiskTotalIops_Object=MibTableColumn
diskTotalIops=_DiskTotalIops_Object((1,3,6,1,4,1,12276,1,2,1,2,2,1,4),_DiskTotalIops_Type())
diskTotalIops.setMaxAccess(_C)
if mibBuilder.loadTexts:diskTotalIops.setStatus(_A)
if mibBuilder.loadTexts:diskTotalIops.setUnits(_N)
_DiskReadIops_Type=Counter64
_DiskReadIops_Object=MibTableColumn
diskReadIops=_DiskReadIops_Object((1,3,6,1,4,1,12276,1,2,1,2,2,1,5),_DiskReadIops_Type())
diskReadIops.setMaxAccess(_C)
if mibBuilder.loadTexts:diskReadIops.setStatus(_A)
if mibBuilder.loadTexts:diskReadIops.setUnits(_N)
_DiskReadMerged_Type=Counter64
_DiskReadMerged_Object=MibTableColumn
diskReadMerged=_DiskReadMerged_Object((1,3,6,1,4,1,12276,1,2,1,2,2,1,6),_DiskReadMerged_Type())
diskReadMerged.setMaxAccess(_C)
if mibBuilder.loadTexts:diskReadMerged.setStatus(_A)
_DiskReadBytes_Type=Counter64
_DiskReadBytes_Object=MibTableColumn
diskReadBytes=_DiskReadBytes_Object((1,3,6,1,4,1,12276,1,2,1,2,2,1,7),_DiskReadBytes_Type())
diskReadBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:diskReadBytes.setStatus(_A)
if mibBuilder.loadTexts:diskReadBytes.setUnits(_H)
_DiskReadLatencyMs_Type=Counter64
_DiskReadLatencyMs_Object=MibTableColumn
diskReadLatencyMs=_DiskReadLatencyMs_Object((1,3,6,1,4,1,12276,1,2,1,2,2,1,8),_DiskReadLatencyMs_Type())
diskReadLatencyMs.setMaxAccess(_C)
if mibBuilder.loadTexts:diskReadLatencyMs.setStatus(_A)
if mibBuilder.loadTexts:diskReadLatencyMs.setUnits('ms')
_DiskWriteIops_Type=Counter64
_DiskWriteIops_Object=MibTableColumn
diskWriteIops=_DiskWriteIops_Object((1,3,6,1,4,1,12276,1,2,1,2,2,1,9),_DiskWriteIops_Type())
diskWriteIops.setMaxAccess(_C)
if mibBuilder.loadTexts:diskWriteIops.setStatus(_A)
if mibBuilder.loadTexts:diskWriteIops.setUnits(_N)
_DiskWriteMerged_Type=Counter64
_DiskWriteMerged_Object=MibTableColumn
diskWriteMerged=_DiskWriteMerged_Object((1,3,6,1,4,1,12276,1,2,1,2,2,1,10),_DiskWriteMerged_Type())
diskWriteMerged.setMaxAccess(_C)
if mibBuilder.loadTexts:diskWriteMerged.setStatus(_A)
_DiskWriteBytes_Type=Counter64
_DiskWriteBytes_Object=MibTableColumn
diskWriteBytes=_DiskWriteBytes_Object((1,3,6,1,4,1,12276,1,2,1,2,2,1,11),_DiskWriteBytes_Type())
diskWriteBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:diskWriteBytes.setStatus(_A)
if mibBuilder.loadTexts:diskWriteBytes.setUnits(_H)
_DiskWriteLatencyMs_Type=Counter64
_DiskWriteLatencyMs_Object=MibTableColumn
diskWriteLatencyMs=_DiskWriteLatencyMs_Object((1,3,6,1,4,1,12276,1,2,1,2,2,1,12),_DiskWriteLatencyMs_Type())
diskWriteLatencyMs.setMaxAccess(_C)
if mibBuilder.loadTexts:diskWriteLatencyMs.setStatus(_A)
if mibBuilder.loadTexts:diskWriteLatencyMs.setUnits('ms')
_PlatformTemperatureTable_ObjectIdentity=ObjectIdentity
platformTemperatureTable=_PlatformTemperatureTable_ObjectIdentity((1,3,6,1,4,1,12276,1,2,1,3))
_TemperatureStatsTable_Object=MibTable
temperatureStatsTable=_TemperatureStatsTable_Object((1,3,6,1,4,1,12276,1,2,1,3,1))
if mibBuilder.loadTexts:temperatureStatsTable.setStatus(_A)
_TemperatureStatsEntry_Object=MibTableRow
temperatureStatsEntry=_TemperatureStatsEntry_Object((1,3,6,1,4,1,12276,1,2,1,3,1,1))
temperatureStatsEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:temperatureStatsEntry.setStatus(_A)
class _TempCurrent_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_TempCurrent_Type.__name__=_D
_TempCurrent_Object=MibTableColumn
tempCurrent=_TempCurrent_Object((1,3,6,1,4,1,12276,1,2,1,3,1,1,2),_TempCurrent_Type())
tempCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:tempCurrent.setStatus(_A)
if mibBuilder.loadTexts:tempCurrent.setUnits(_K)
class _TempAverage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_TempAverage_Type.__name__=_D
_TempAverage_Object=MibTableColumn
tempAverage=_TempAverage_Object((1,3,6,1,4,1,12276,1,2,1,3,1,1,3),_TempAverage_Type())
tempAverage.setMaxAccess(_C)
if mibBuilder.loadTexts:tempAverage.setStatus(_A)
if mibBuilder.loadTexts:tempAverage.setUnits(_K)
class _TempMinimum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_TempMinimum_Type.__name__=_D
_TempMinimum_Object=MibTableColumn
tempMinimum=_TempMinimum_Object((1,3,6,1,4,1,12276,1,2,1,3,1,1,4),_TempMinimum_Type())
tempMinimum.setMaxAccess(_C)
if mibBuilder.loadTexts:tempMinimum.setStatus(_A)
if mibBuilder.loadTexts:tempMinimum.setUnits(_K)
class _TempMaximum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_TempMaximum_Type.__name__=_D
_TempMaximum_Object=MibTableColumn
tempMaximum=_TempMaximum_Object((1,3,6,1,4,1,12276,1,2,1,3,1,1,5),_TempMaximum_Type())
tempMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:tempMaximum.setStatus(_A)
if mibBuilder.loadTexts:tempMaximum.setUnits(_K)
_PlatformMemoryStatsTable_ObjectIdentity=ObjectIdentity
platformMemoryStatsTable=_PlatformMemoryStatsTable_ObjectIdentity((1,3,6,1,4,1,12276,1,2,1,4))
_MemoryStatsTable_Object=MibTable
memoryStatsTable=_MemoryStatsTable_Object((1,3,6,1,4,1,12276,1,2,1,4,1))
if mibBuilder.loadTexts:memoryStatsTable.setStatus(_A)
_MemoryStatsEntry_Object=MibTableRow
memoryStatsEntry=_MemoryStatsEntry_Object((1,3,6,1,4,1,12276,1,2,1,4,1,1))
memoryStatsEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:memoryStatsEntry.setStatus(_A)
_MemAvailable_Type=Counter64
_MemAvailable_Object=MibTableColumn
memAvailable=_MemAvailable_Object((1,3,6,1,4,1,12276,1,2,1,4,1,1,2),_MemAvailable_Type())
memAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:memAvailable.setStatus(_A)
if mibBuilder.loadTexts:memAvailable.setUnits(_H)
_MemFree_Type=Counter64
_MemFree_Object=MibTableColumn
memFree=_MemFree_Object((1,3,6,1,4,1,12276,1,2,1,4,1,1,3),_MemFree_Type())
memFree.setMaxAccess(_C)
if mibBuilder.loadTexts:memFree.setStatus(_A)
if mibBuilder.loadTexts:memFree.setUnits(_H)
class _MemPercentageUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_MemPercentageUsed_Type.__name__=_I
_MemPercentageUsed_Object=MibTableColumn
memPercentageUsed=_MemPercentageUsed_Object((1,3,6,1,4,1,12276,1,2,1,4,1,1,4),_MemPercentageUsed_Type())
memPercentageUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:memPercentageUsed.setStatus(_A)
if mibBuilder.loadTexts:memPercentageUsed.setUnits(_G)
_MemPlatformTotal_Type=Counter64
_MemPlatformTotal_Object=MibTableColumn
memPlatformTotal=_MemPlatformTotal_Object((1,3,6,1,4,1,12276,1,2,1,4,1,1,5),_MemPlatformTotal_Type())
memPlatformTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:memPlatformTotal.setStatus(_A)
if mibBuilder.loadTexts:memPlatformTotal.setUnits(_H)
_MemPlatformUsed_Type=Counter64
_MemPlatformUsed_Object=MibTableColumn
memPlatformUsed=_MemPlatformUsed_Object((1,3,6,1,4,1,12276,1,2,1,4,1,1,6),_MemPlatformUsed_Type())
memPlatformUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:memPlatformUsed.setStatus(_A)
if mibBuilder.loadTexts:memPlatformUsed.setUnits(_H)
_PlatformFpgaTable_ObjectIdentity=ObjectIdentity
platformFpgaTable=_PlatformFpgaTable_ObjectIdentity((1,3,6,1,4,1,12276,1,2,1,5))
_FpgaTable_Object=MibTable
fpgaTable=_FpgaTable_Object((1,3,6,1,4,1,12276,1,2,1,5,1))
if mibBuilder.loadTexts:fpgaTable.setStatus(_A)
_FpgaEntry_Object=MibTableRow
fpgaEntry=_FpgaEntry_Object((1,3,6,1,4,1,12276,1,2,1,5,1,1))
fpgaEntry.setIndexNames((0,_B,_E),(0,_B,_O))
if mibBuilder.loadTexts:fpgaEntry.setStatus(_A)
class _FpgaIndex_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_FpgaIndex_Type.__name__=_D
_FpgaIndex_Object=MibTableColumn
fpgaIndex=_FpgaIndex_Object((1,3,6,1,4,1,12276,1,2,1,5,1,1,1),_FpgaIndex_Type())
fpgaIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fpgaIndex.setStatus(_A)
class _FpgaVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_FpgaVersion_Type.__name__=_D
_FpgaVersion_Object=MibTableColumn
fpgaVersion=_FpgaVersion_Object((1,3,6,1,4,1,12276,1,2,1,5,1,1,2),_FpgaVersion_Type())
fpgaVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:fpgaVersion.setStatus(_A)
_PlatformFwTable_ObjectIdentity=ObjectIdentity
platformFwTable=_PlatformFwTable_ObjectIdentity((1,3,6,1,4,1,12276,1,2,1,6))
_FwTable_Object=MibTable
fwTable=_FwTable_Object((1,3,6,1,4,1,12276,1,2,1,6,1))
if mibBuilder.loadTexts:fwTable.setStatus(_A)
_FwEntry_Object=MibTableRow
fwEntry=_FwEntry_Object((1,3,6,1,4,1,12276,1,2,1,6,1,1))
fwEntry.setIndexNames((0,_B,_E),(0,_B,_P))
if mibBuilder.loadTexts:fwEntry.setStatus(_A)
class _FwName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_FwName_Type.__name__=_D
_FwName_Object=MibTableColumn
fwName=_FwName_Object((1,3,6,1,4,1,12276,1,2,1,6,1,1,1),_FwName_Type())
fwName.setMaxAccess(_C)
if mibBuilder.loadTexts:fwName.setStatus(_A)
class _FwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_FwVersion_Type.__name__=_D
_FwVersion_Object=MibTableColumn
fwVersion=_FwVersion_Object((1,3,6,1,4,1,12276,1,2,1,6,1,1,2),_FwVersion_Type())
fwVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:fwVersion.setStatus(_A)
_Configurable_Type=TruthValue
_Configurable_Object=MibTableColumn
configurable=_Configurable_Object((1,3,6,1,4,1,12276,1,2,1,6,1,1,3),_Configurable_Type())
configurable.setMaxAccess(_C)
if mibBuilder.loadTexts:configurable.setStatus(_A)
class _FwUpdateStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_FwUpdateStatus_Type.__name__=_D
_FwUpdateStatus_Object=MibTableColumn
fwUpdateStatus=_FwUpdateStatus_Object((1,3,6,1,4,1,12276,1,2,1,6,1,1,4),_FwUpdateStatus_Type())
fwUpdateStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fwUpdateStatus.setStatus(_A)
_PlatformFantrayTable_ObjectIdentity=ObjectIdentity
platformFantrayTable=_PlatformFantrayTable_ObjectIdentity((1,3,6,1,4,1,12276,1,2,1,7))
_FantrayStatsTable_Object=MibTable
fantrayStatsTable=_FantrayStatsTable_Object((1,3,6,1,4,1,12276,1,2,1,7,1))
if mibBuilder.loadTexts:fantrayStatsTable.setStatus(_A)
_FantrayStatsEntry_Object=MibTableRow
fantrayStatsEntry=_FantrayStatsEntry_Object((1,3,6,1,4,1,12276,1,2,1,7,1,1))
fantrayStatsEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:fantrayStatsEntry.setStatus(_A)
_Fan_1_speed_Type=Integer32
_Fan_1_speed_Object=MibTableColumn
fan_1_speed=_Fan_1_speed_Object((1,3,6,1,4,1,12276,1,2,1,7,1,1,1),_Fan_1_speed_Type())
fan_1_speed.setMaxAccess(_C)
if mibBuilder.loadTexts:fan_1_speed.setStatus(_A)
if mibBuilder.loadTexts:fan_1_speed.setUnits(_F)
_Fan_2_speed_Type=Integer32
_Fan_2_speed_Object=MibTableColumn
fan_2_speed=_Fan_2_speed_Object((1,3,6,1,4,1,12276,1,2,1,7,1,1,2),_Fan_2_speed_Type())
fan_2_speed.setMaxAccess(_C)
if mibBuilder.loadTexts:fan_2_speed.setStatus(_A)
if mibBuilder.loadTexts:fan_2_speed.setUnits(_F)
_Fan_3_speed_Type=Integer32
_Fan_3_speed_Object=MibTableColumn
fan_3_speed=_Fan_3_speed_Object((1,3,6,1,4,1,12276,1,2,1,7,1,1,3),_Fan_3_speed_Type())
fan_3_speed.setMaxAccess(_C)
if mibBuilder.loadTexts:fan_3_speed.setStatus(_A)
if mibBuilder.loadTexts:fan_3_speed.setUnits(_F)
_Fan_4_speed_Type=Integer32
_Fan_4_speed_Object=MibTableColumn
fan_4_speed=_Fan_4_speed_Object((1,3,6,1,4,1,12276,1,2,1,7,1,1,4),_Fan_4_speed_Type())
fan_4_speed.setMaxAccess(_C)
if mibBuilder.loadTexts:fan_4_speed.setStatus(_A)
if mibBuilder.loadTexts:fan_4_speed.setUnits(_F)
_Fan_5_speed_Type=Integer32
_Fan_5_speed_Object=MibTableColumn
fan_5_speed=_Fan_5_speed_Object((1,3,6,1,4,1,12276,1,2,1,7,1,1,5),_Fan_5_speed_Type())
fan_5_speed.setMaxAccess(_C)
if mibBuilder.loadTexts:fan_5_speed.setStatus(_A)
if mibBuilder.loadTexts:fan_5_speed.setUnits(_F)
_Fan_6_speed_Type=Integer32
_Fan_6_speed_Object=MibTableColumn
fan_6_speed=_Fan_6_speed_Object((1,3,6,1,4,1,12276,1,2,1,7,1,1,6),_Fan_6_speed_Type())
fan_6_speed.setMaxAccess(_C)
if mibBuilder.loadTexts:fan_6_speed.setStatus(_A)
if mibBuilder.loadTexts:fan_6_speed.setUnits(_F)
_Fan_7_speed_Type=Integer32
_Fan_7_speed_Object=MibTableColumn
fan_7_speed=_Fan_7_speed_Object((1,3,6,1,4,1,12276,1,2,1,7,1,1,7),_Fan_7_speed_Type())
fan_7_speed.setMaxAccess(_C)
if mibBuilder.loadTexts:fan_7_speed.setStatus(_A)
if mibBuilder.loadTexts:fan_7_speed.setUnits(_F)
_Fan_8_speed_Type=Integer32
_Fan_8_speed_Object=MibTableColumn
fan_8_speed=_Fan_8_speed_Object((1,3,6,1,4,1,12276,1,2,1,7,1,1,8),_Fan_8_speed_Type())
fan_8_speed.setMaxAccess(_C)
if mibBuilder.loadTexts:fan_8_speed.setStatus(_A)
if mibBuilder.loadTexts:fan_8_speed.setUnits(_F)
_Fan_9_speed_Type=Integer32
_Fan_9_speed_Object=MibTableColumn
fan_9_speed=_Fan_9_speed_Object((1,3,6,1,4,1,12276,1,2,1,7,1,1,9),_Fan_9_speed_Type())
fan_9_speed.setMaxAccess(_C)
if mibBuilder.loadTexts:fan_9_speed.setStatus(_A)
if mibBuilder.loadTexts:fan_9_speed.setUnits(_F)
_Fan_10_speed_Type=Integer32
_Fan_10_speed_Object=MibTableColumn
fan_10_speed=_Fan_10_speed_Object((1,3,6,1,4,1,12276,1,2,1,7,1,1,10),_Fan_10_speed_Type())
fan_10_speed.setMaxAccess(_C)
if mibBuilder.loadTexts:fan_10_speed.setStatus(_A)
if mibBuilder.loadTexts:fan_10_speed.setUnits(_F)
_Fan_11_speed_Type=Integer32
_Fan_11_speed_Object=MibTableColumn
fan_11_speed=_Fan_11_speed_Object((1,3,6,1,4,1,12276,1,2,1,7,1,1,11),_Fan_11_speed_Type())
fan_11_speed.setMaxAccess(_C)
if mibBuilder.loadTexts:fan_11_speed.setStatus(_A)
if mibBuilder.loadTexts:fan_11_speed.setUnits(_F)
_Fan_12_speed_Type=Integer32
_Fan_12_speed_Object=MibTableColumn
fan_12_speed=_Fan_12_speed_Object((1,3,6,1,4,1,12276,1,2,1,7,1,1,12),_Fan_12_speed_Type())
fan_12_speed.setMaxAccess(_C)
if mibBuilder.loadTexts:fan_12_speed.setStatus(_A)
if mibBuilder.loadTexts:fan_12_speed.setUnits(_F)
_PlatformConformance_ObjectIdentity=ObjectIdentity
platformConformance=_PlatformConformance_ObjectIdentity((1,3,6,1,4,1,12276,1,2,2))
_PlatformGroups_ObjectIdentity=ObjectIdentity
platformGroups=_PlatformGroups_ObjectIdentity((1,3,6,1,4,1,12276,1,2,2,1))
_PlatformCompliances_ObjectIdentity=ObjectIdentity
platformCompliances=_PlatformCompliances_ObjectIdentity((1,3,6,1,4,1,12276,1,2,2,2))
platformCPUGroup=ObjectGroup((1,3,6,1,4,1,12276,1,2,2,1,1))
platformCPUGroup.setObjects(*((_B,_E),(_B,_L),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_M),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:platformCPUGroup.setStatus(_A)
platformDiskGroup=ObjectGroup((1,3,6,1,4,1,12276,1,2,2,1,2))
platformDiskGroup.setObjects(*((_B,_J),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:platformDiskGroup.setStatus(_A)
platformTempGroup=ObjectGroup((1,3,6,1,4,1,12276,1,2,2,1,3))
platformTempGroup.setObjects(*((_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:platformTempGroup.setStatus(_A)
platformMemGroup=ObjectGroup((1,3,6,1,4,1,12276,1,2,2,1,4))
platformMemGroup.setObjects(*((_B,_z),(_B,'memFree'),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:platformMemGroup.setStatus(_A)
platformFpgaGroup=ObjectGroup((1,3,6,1,4,1,12276,1,2,2,1,5))
platformFpgaGroup.setObjects(*((_B,_O),(_B,_A3)))
if mibBuilder.loadTexts:platformFpgaGroup.setStatus(_A)
platformFwVersionGroup=ObjectGroup((1,3,6,1,4,1,12276,1,2,2,1,6))
platformFwVersionGroup.setObjects(*((_B,_P),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:platformFwVersionGroup.setStatus(_A)
platformFantrayGroup=ObjectGroup((1,3,6,1,4,1,12276,1,2,2,1,7))
platformFantrayGroup.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI)))
if mibBuilder.loadTexts:platformFantrayGroup.setStatus(_A)
platformCompliance=ModuleCompliance((1,3,6,1,4,1,12276,1,2,2,2,1))
platformCompliance.setObjects(*((_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP)))
if mibBuilder.loadTexts:platformCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'PlatformStatsIndex':PlatformStatsIndex,'String':String,'f5PlatformStats':f5PlatformStats,'f5PlatformStatsObjects':f5PlatformStatsObjects,'platformCpuStatsTable':platformCpuStatsTable,'cpuProcessorStatsTable':cpuProcessorStatsTable,'cpuProcessorStatsEntry':cpuProcessorStatsEntry,_E:index,_L:cpuIndex,_Q:cpuCacheSize,_R:cpuCoreCnt,_S:cpuFreq,_T:cpuStepping,_U:cpuThreadCnt,_V:cpuModelName,'cpuUtilizationStatsTable':cpuUtilizationStatsTable,'cpuUtilizationStatsEntry':cpuUtilizationStatsEntry,_W:cpuCore,_X:cpuCurrent,_Y:cpuTotal5secAvg,_Z:cpuTotal1minAvg,_a:cpuTotal5minAvg,'cpuCoreStatsTable':cpuCoreStatsTable,'cpuCoreStatsEntry':cpuCoreStatsEntry,_M:coreIndex,'coreName':coreName,_b:coreCurrent,_c:coreTotal5secAvg,_d:coreTotal1minAvg,_e:coreTotal5minAvg,'platformDiskStatsTable':platformDiskStatsTable,'diskInfoTable':diskInfoTable,'diskInfoEntry':diskInfoEntry,_J:diskName,_f:diskModel,_g:diskVendor,_h:diskVersion,_i:diskSerialNo,_j:diskSize,_k:diskType,'diskUtilizationStatsTable':diskUtilizationStatsTable,'diskUtilizationStatsEntry':diskUtilizationStatsEntry,_l:diskPercentageUsed,_m:diskTotalIops,_n:diskReadIops,_o:diskReadMerged,_p:diskReadBytes,_q:diskReadLatencyMs,_r:diskWriteIops,_s:diskWriteMerged,_t:diskWriteBytes,_u:diskWriteLatencyMs,'platformTemperatureTable':platformTemperatureTable,'temperatureStatsTable':temperatureStatsTable,'temperatureStatsEntry':temperatureStatsEntry,_v:tempCurrent,_w:tempAverage,_x:tempMinimum,_y:tempMaximum,'platformMemoryStatsTable':platformMemoryStatsTable,'memoryStatsTable':memoryStatsTable,'memoryStatsEntry':memoryStatsEntry,_z:memAvailable,'memFree':memFree,_A0:memPercentageUsed,_A1:memPlatformTotal,_A2:memPlatformUsed,'platformFpgaTable':platformFpgaTable,'fpgaTable':fpgaTable,'fpgaEntry':fpgaEntry,_O:fpgaIndex,_A3:fpgaVersion,'platformFwTable':platformFwTable,'fwTable':fwTable,'fwEntry':fwEntry,_P:fwName,_A4:fwVersion,_A5:configurable,_A6:fwUpdateStatus,'platformFantrayTable':platformFantrayTable,'fantrayStatsTable':fantrayStatsTable,'fantrayStatsEntry':fantrayStatsEntry,_A7:fan_1_speed,_A8:fan_2_speed,_A9:fan_3_speed,_AA:fan_4_speed,_AB:fan_5_speed,_AC:fan_6_speed,_AD:fan_7_speed,_AE:fan_8_speed,_AF:fan_9_speed,_AG:fan_10_speed,_AH:fan_11_speed,_AI:fan_12_speed,'platformConformance':platformConformance,'platformGroups':platformGroups,_AJ:platformCPUGroup,_AK:platformDiskGroup,_AL:platformTempGroup,_AM:platformMemGroup,_AN:platformFpgaGroup,_AO:platformFwVersionGroup,_AP:platformFantrayGroup,'platformCompliances':platformCompliances,'platformCompliance':platformCompliance})