_e='cpqOsProcessIndex'
_d='cpqOsTcpIndex'
_c='cpqOsNetworkInterfaceIndex'
_b='cpqOsPhysicalDiskIndex'
_a='NotificationType'
_Z='cpqOsLogicalDiskBusyTimePercent'
_Y='cpqOsLogicalDiskInstance'
_X='cpqOsPageFileUsagePercent'
_W='cpqOsPagingFileInstance'
_V='cpqOsCacheCopyReadHitsPercent'
_U='cpqOsCacheInstance'
_T='cpqOsCpuTimePercent'
_S='cpqOsCpuInstance'
_R='cpqOsLogicalDiskIndex'
_Q='cpqOsPagingFileIndex'
_P='cpqOsCacheIndex'
_O='cpqOsCpuIndex'
_N='read-write'
_M='sysName'
_L='SNMPv2-MIB'
_K='cpqHoTrapFlags'
_J='CPQHOST-MIB'
_I='DisplayString'
_H='failed'
_G='degraded'
_F='ok'
_E='other'
_D='Integer32'
_C='CPQOS-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,cpqHoTrapFlags=mibBuilder.importSymbols(_J,'compaq',_K)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_L,_M)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_a,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_a,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
_CpqWinOsMgmt_ObjectIdentity=ObjectIdentity
cpqWinOsMgmt=_CpqWinOsMgmt_ObjectIdentity((1,3,6,1,4,1,232,19))
_CpqOsMibRev_ObjectIdentity=ObjectIdentity
cpqOsMibRev=_CpqOsMibRev_ObjectIdentity((1,3,6,1,4,1,232,19,1))
class _CpqOsMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqOsMibRevMajor_Type.__name__=_D
_CpqOsMibRevMajor_Object=MibScalar
cpqOsMibRevMajor=_CpqOsMibRevMajor_Object((1,3,6,1,4,1,232,19,1,1),_CpqOsMibRevMajor_Type())
cpqOsMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsMibRevMajor.setStatus(_A)
class _CpqOsMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqOsMibRevMinor_Type.__name__=_D
_CpqOsMibRevMinor_Object=MibScalar
cpqOsMibRevMinor=_CpqOsMibRevMinor_Object((1,3,6,1,4,1,232,19,1,2),_CpqOsMibRevMinor_Type())
cpqOsMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsMibRevMinor.setStatus(_A)
class _CpqOsMibCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_CpqOsMibCondition_Type.__name__=_D
_CpqOsMibCondition_Object=MibScalar
cpqOsMibCondition=_CpqOsMibCondition_Object((1,3,6,1,4,1,232,19,1,3),_CpqOsMibCondition_Type())
cpqOsMibCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsMibCondition.setStatus(_A)
_CpqOsComponent_ObjectIdentity=ObjectIdentity
cpqOsComponent=_CpqOsComponent_ObjectIdentity((1,3,6,1,4,1,232,19,2))
_CpqOsInterface_ObjectIdentity=ObjectIdentity
cpqOsInterface=_CpqOsInterface_ObjectIdentity((1,3,6,1,4,1,232,19,2,1))
_CpqOsCommon_ObjectIdentity=ObjectIdentity
cpqOsCommon=_CpqOsCommon_ObjectIdentity((1,3,6,1,4,1,232,19,2,1,4))
class _CpqOsCommonPollFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqOsCommonPollFreq_Type.__name__=_D
_CpqOsCommonPollFreq_Object=MibScalar
cpqOsCommonPollFreq=_CpqOsCommonPollFreq_Object((1,3,6,1,4,1,232,19,2,1,4,1),_CpqOsCommonPollFreq_Type())
cpqOsCommonPollFreq.setMaxAccess(_N)
if mibBuilder.loadTexts:cpqOsCommonPollFreq.setStatus(_A)
_CpqOsSystem_ObjectIdentity=ObjectIdentity
cpqOsSystem=_CpqOsSystem_ObjectIdentity((1,3,6,1,4,1,232,19,2,2))
class _CpqOsSystemStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_CpqOsSystemStatus_Type.__name__=_D
_CpqOsSystemStatus_Object=MibScalar
cpqOsSystemStatus=_CpqOsSystemStatus_Object((1,3,6,1,4,1,232,19,2,2,1),_CpqOsSystemStatus_Type())
cpqOsSystemStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsSystemStatus.setStatus(_A)
class _CpqOsSystemUpTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqOsSystemUpTime_Type.__name__=_I
_CpqOsSystemUpTime_Object=MibScalar
cpqOsSystemUpTime=_CpqOsSystemUpTime_Object((1,3,6,1,4,1,232,19,2,2,2),_CpqOsSystemUpTime_Type())
cpqOsSystemUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsSystemUpTime.setStatus(_A)
_CpqOsSystemThreads_Type=Integer32
_CpqOsSystemThreads_Object=MibScalar
cpqOsSystemThreads=_CpqOsSystemThreads_Object((1,3,6,1,4,1,232,19,2,2,3),_CpqOsSystemThreads_Type())
cpqOsSystemThreads.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsSystemThreads.setStatus(_A)
_CpqOsSysContextSwitchesPersec_Type=Integer32
_CpqOsSysContextSwitchesPersec_Object=MibScalar
cpqOsSysContextSwitchesPersec=_CpqOsSysContextSwitchesPersec_Object((1,3,6,1,4,1,232,19,2,2,4),_CpqOsSysContextSwitchesPersec_Type())
cpqOsSysContextSwitchesPersec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsSysContextSwitchesPersec.setStatus(_A)
_CpqOsSysCpuQueueLength_Type=Integer32
_CpqOsSysCpuQueueLength_Object=MibScalar
cpqOsSysCpuQueueLength=_CpqOsSysCpuQueueLength_Object((1,3,6,1,4,1,232,19,2,2,5),_CpqOsSysCpuQueueLength_Type())
cpqOsSysCpuQueueLength.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsSysCpuQueueLength.setStatus(_A)
_CpqOsSysProcesses_Type=Integer32
_CpqOsSysProcesses_Object=MibScalar
cpqOsSysProcesses=_CpqOsSysProcesses_Object((1,3,6,1,4,1,232,19,2,2,6),_CpqOsSysProcesses_Type())
cpqOsSysProcesses.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsSysProcesses.setStatus(_A)
_CpqOsSysRegistryInUsePercent_Type=Integer32
_CpqOsSysRegistryInUsePercent_Object=MibScalar
cpqOsSysRegistryInUsePercent=_CpqOsSysRegistryInUsePercent_Object((1,3,6,1,4,1,232,19,2,2,7),_CpqOsSysRegistryInUsePercent_Type())
cpqOsSysRegistryInUsePercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsSysRegistryInUsePercent.setStatus(_A)
_CpqOsProcessor_ObjectIdentity=ObjectIdentity
cpqOsProcessor=_CpqOsProcessor_ObjectIdentity((1,3,6,1,4,1,232,19,2,3))
class _CpqOsProcessorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_CpqOsProcessorStatus_Type.__name__=_D
_CpqOsProcessorStatus_Object=MibScalar
cpqOsProcessorStatus=_CpqOsProcessorStatus_Object((1,3,6,1,4,1,232,19,2,3,1),_CpqOsProcessorStatus_Type())
cpqOsProcessorStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsProcessorStatus.setStatus(_A)
_CpqOsProcessorTable_Object=MibTable
cpqOsProcessorTable=_CpqOsProcessorTable_Object((1,3,6,1,4,1,232,19,2,3,2))
if mibBuilder.loadTexts:cpqOsProcessorTable.setStatus(_A)
_CpqOsProcessorEntry_Object=MibTableRow
cpqOsProcessorEntry=_CpqOsProcessorEntry_Object((1,3,6,1,4,1,232,19,2,3,2,1))
cpqOsProcessorEntry.setIndexNames((0,_C,_O))
if mibBuilder.loadTexts:cpqOsProcessorEntry.setStatus(_A)
_CpqOsCpuIndex_Type=Integer32
_CpqOsCpuIndex_Object=MibTableColumn
cpqOsCpuIndex=_CpqOsCpuIndex_Object((1,3,6,1,4,1,232,19,2,3,2,1,1),_CpqOsCpuIndex_Type())
cpqOsCpuIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsCpuIndex.setStatus(_A)
class _CpqOsCpuInstance_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqOsCpuInstance_Type.__name__=_I
_CpqOsCpuInstance_Object=MibTableColumn
cpqOsCpuInstance=_CpqOsCpuInstance_Object((1,3,6,1,4,1,232,19,2,3,2,1,2),_CpqOsCpuInstance_Type())
cpqOsCpuInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsCpuInstance.setStatus(_A)
_CpqOsCpuInterruptsPerSec_Type=Integer32
_CpqOsCpuInterruptsPerSec_Object=MibTableColumn
cpqOsCpuInterruptsPerSec=_CpqOsCpuInterruptsPerSec_Object((1,3,6,1,4,1,232,19,2,3,2,1,3),_CpqOsCpuInterruptsPerSec_Type())
cpqOsCpuInterruptsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsCpuInterruptsPerSec.setStatus(_A)
_CpqOsCpuTimePercent_Type=Integer32
_CpqOsCpuTimePercent_Object=MibTableColumn
cpqOsCpuTimePercent=_CpqOsCpuTimePercent_Object((1,3,6,1,4,1,232,19,2,3,2,1,4),_CpqOsCpuTimePercent_Type())
cpqOsCpuTimePercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsCpuTimePercent.setStatus(_A)
_CpqOsWarCpuTimePercent_Type=Integer32
_CpqOsWarCpuTimePercent_Object=MibTableColumn
cpqOsWarCpuTimePercent=_CpqOsWarCpuTimePercent_Object((1,3,6,1,4,1,232,19,2,3,2,1,5),_CpqOsWarCpuTimePercent_Type())
cpqOsWarCpuTimePercent.setMaxAccess(_N)
if mibBuilder.loadTexts:cpqOsWarCpuTimePercent.setStatus(_A)
_CpqOsCriCpuTimePercent_Type=Integer32
_CpqOsCriCpuTimePercent_Object=MibTableColumn
cpqOsCriCpuTimePercent=_CpqOsCriCpuTimePercent_Object((1,3,6,1,4,1,232,19,2,3,2,1,6),_CpqOsCriCpuTimePercent_Type())
cpqOsCriCpuTimePercent.setMaxAccess(_N)
if mibBuilder.loadTexts:cpqOsCriCpuTimePercent.setStatus(_A)
_CpqOsCpuUserTimePercent_Type=Integer32
_CpqOsCpuUserTimePercent_Object=MibTableColumn
cpqOsCpuUserTimePercent=_CpqOsCpuUserTimePercent_Object((1,3,6,1,4,1,232,19,2,3,2,1,7),_CpqOsCpuUserTimePercent_Type())
cpqOsCpuUserTimePercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsCpuUserTimePercent.setStatus(_A)
_CpqOsCpuPrivilegedTimePercent_Type=Integer32
_CpqOsCpuPrivilegedTimePercent_Object=MibTableColumn
cpqOsCpuPrivilegedTimePercent=_CpqOsCpuPrivilegedTimePercent_Object((1,3,6,1,4,1,232,19,2,3,2,1,8),_CpqOsCpuPrivilegedTimePercent_Type())
cpqOsCpuPrivilegedTimePercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsCpuPrivilegedTimePercent.setStatus(_A)
class _CpqOsCpuCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_CpqOsCpuCondition_Type.__name__=_D
_CpqOsCpuCondition_Object=MibTableColumn
cpqOsCpuCondition=_CpqOsCpuCondition_Object((1,3,6,1,4,1,232,19,2,3,2,1,9),_CpqOsCpuCondition_Type())
cpqOsCpuCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsCpuCondition.setStatus(_A)
_CpqOsCpuPercentDPCTime_Type=Integer32
_CpqOsCpuPercentDPCTime_Object=MibTableColumn
cpqOsCpuPercentDPCTime=_CpqOsCpuPercentDPCTime_Object((1,3,6,1,4,1,232,19,2,3,2,1,10),_CpqOsCpuPercentDPCTime_Type())
cpqOsCpuPercentDPCTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsCpuPercentDPCTime.setStatus(_A)
_CpqOsCpuPercentInterruptTime_Type=Integer32
_CpqOsCpuPercentInterruptTime_Object=MibTableColumn
cpqOsCpuPercentInterruptTime=_CpqOsCpuPercentInterruptTime_Object((1,3,6,1,4,1,232,19,2,3,2,1,11),_CpqOsCpuPercentInterruptTime_Type())
cpqOsCpuPercentInterruptTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsCpuPercentInterruptTime.setStatus(_A)
_CpqOsMemory_ObjectIdentity=ObjectIdentity
cpqOsMemory=_CpqOsMemory_ObjectIdentity((1,3,6,1,4,1,232,19,2,4))
class _CpqOsMemoryStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_CpqOsMemoryStatus_Type.__name__=_D
_CpqOsMemoryStatus_Object=MibScalar
cpqOsMemoryStatus=_CpqOsMemoryStatus_Object((1,3,6,1,4,1,232,19,2,4,1),_CpqOsMemoryStatus_Type())
cpqOsMemoryStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsMemoryStatus.setStatus(_A)
_CpqOsMemAvailableKBytes_Type=Integer32
_CpqOsMemAvailableKBytes_Object=MibScalar
cpqOsMemAvailableKBytes=_CpqOsMemAvailableKBytes_Object((1,3,6,1,4,1,232,19,2,4,2),_CpqOsMemAvailableKBytes_Type())
cpqOsMemAvailableKBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsMemAvailableKBytes.setStatus(_A)
_CpqOsMemPagesPerSec_Type=Integer32
_CpqOsMemPagesPerSec_Object=MibScalar
cpqOsMemPagesPerSec=_CpqOsMemPagesPerSec_Object((1,3,6,1,4,1,232,19,2,4,3),_CpqOsMemPagesPerSec_Type())
cpqOsMemPagesPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsMemPagesPerSec.setStatus(_A)
_CpqOsMemPagesInputPerSec_Type=Integer32
_CpqOsMemPagesInputPerSec_Object=MibScalar
cpqOsMemPagesInputPerSec=_CpqOsMemPagesInputPerSec_Object((1,3,6,1,4,1,232,19,2,4,4),_CpqOsMemPagesInputPerSec_Type())
cpqOsMemPagesInputPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsMemPagesInputPerSec.setStatus(_A)
_CpqOsMemPagesOutputPerSec_Type=Integer32
_CpqOsMemPagesOutputPerSec_Object=MibScalar
cpqOsMemPagesOutputPerSec=_CpqOsMemPagesOutputPerSec_Object((1,3,6,1,4,1,232,19,2,4,5),_CpqOsMemPagesOutputPerSec_Type())
cpqOsMemPagesOutputPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsMemPagesOutputPerSec.setStatus(_A)
_CpqOsMemPageFaultsPerSec_Type=Integer32
_CpqOsMemPageFaultsPerSec_Object=MibScalar
cpqOsMemPageFaultsPerSec=_CpqOsMemPageFaultsPerSec_Object((1,3,6,1,4,1,232,19,2,4,6),_CpqOsMemPageFaultsPerSec_Type())
cpqOsMemPageFaultsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsMemPageFaultsPerSec.setStatus(_A)
_CpqOsMemCacheFaultsPerSec_Type=Integer32
_CpqOsMemCacheFaultsPerSec_Object=MibScalar
cpqOsMemCacheFaultsPerSec=_CpqOsMemCacheFaultsPerSec_Object((1,3,6,1,4,1,232,19,2,4,7),_CpqOsMemCacheFaultsPerSec_Type())
cpqOsMemCacheFaultsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsMemCacheFaultsPerSec.setStatus(_A)
_CpqOsMemPageReadsPerSecx1000_Type=Integer32
_CpqOsMemPageReadsPerSecx1000_Object=MibScalar
cpqOsMemPageReadsPerSecx1000=_CpqOsMemPageReadsPerSecx1000_Object((1,3,6,1,4,1,232,19,2,4,8),_CpqOsMemPageReadsPerSecx1000_Type())
cpqOsMemPageReadsPerSecx1000.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsMemPageReadsPerSecx1000.setStatus(_A)
_CpqOsMemPageWritesPerSecx1000_Type=Integer32
_CpqOsMemPageWritesPerSecx1000_Object=MibScalar
cpqOsMemPageWritesPerSecx1000=_CpqOsMemPageWritesPerSecx1000_Object((1,3,6,1,4,1,232,19,2,4,9),_CpqOsMemPageWritesPerSecx1000_Type())
cpqOsMemPageWritesPerSecx1000.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsMemPageWritesPerSecx1000.setStatus(_A)
_CpqOsMemPoolNonpagedBytes_Type=Integer32
_CpqOsMemPoolNonpagedBytes_Object=MibScalar
cpqOsMemPoolNonpagedBytes=_CpqOsMemPoolNonpagedBytes_Object((1,3,6,1,4,1,232,19,2,4,10),_CpqOsMemPoolNonpagedBytes_Type())
cpqOsMemPoolNonpagedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsMemPoolNonpagedBytes.setStatus(_A)
_CpqOsMemCacheBytes_Type=Integer32
_CpqOsMemCacheBytes_Object=MibScalar
cpqOsMemCacheBytes=_CpqOsMemCacheBytes_Object((1,3,6,1,4,1,232,19,2,4,11),_CpqOsMemCacheBytes_Type())
cpqOsMemCacheBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsMemCacheBytes.setStatus(_A)
_CpqOsCache_ObjectIdentity=ObjectIdentity
cpqOsCache=_CpqOsCache_ObjectIdentity((1,3,6,1,4,1,232,19,2,5))
class _CpqOsCacheStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_CpqOsCacheStatus_Type.__name__=_D
_CpqOsCacheStatus_Object=MibScalar
cpqOsCacheStatus=_CpqOsCacheStatus_Object((1,3,6,1,4,1,232,19,2,5,1),_CpqOsCacheStatus_Type())
cpqOsCacheStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsCacheStatus.setStatus(_A)
_CpqOsCacheTable_Object=MibTable
cpqOsCacheTable=_CpqOsCacheTable_Object((1,3,6,1,4,1,232,19,2,5,2))
if mibBuilder.loadTexts:cpqOsCacheTable.setStatus(_A)
_CpqOsCacheEntry_Object=MibTableRow
cpqOsCacheEntry=_CpqOsCacheEntry_Object((1,3,6,1,4,1,232,19,2,5,2,1))
cpqOsCacheEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:cpqOsCacheEntry.setStatus(_A)
_CpqOsCacheIndex_Type=Integer32
_CpqOsCacheIndex_Object=MibTableColumn
cpqOsCacheIndex=_CpqOsCacheIndex_Object((1,3,6,1,4,1,232,19,2,5,2,1,1),_CpqOsCacheIndex_Type())
cpqOsCacheIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsCacheIndex.setStatus(_A)
class _CpqOsCacheInstance_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqOsCacheInstance_Type.__name__=_I
_CpqOsCacheInstance_Object=MibTableColumn
cpqOsCacheInstance=_CpqOsCacheInstance_Object((1,3,6,1,4,1,232,19,2,5,2,1,2),_CpqOsCacheInstance_Type())
cpqOsCacheInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsCacheInstance.setStatus(_A)
_CpqOsCacheCopyReadHitsPercent_Type=Integer32
_CpqOsCacheCopyReadHitsPercent_Object=MibTableColumn
cpqOsCacheCopyReadHitsPercent=_CpqOsCacheCopyReadHitsPercent_Object((1,3,6,1,4,1,232,19,2,5,2,1,3),_CpqOsCacheCopyReadHitsPercent_Type())
cpqOsCacheCopyReadHitsPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsCacheCopyReadHitsPercent.setStatus(_A)
_CpqOsWarCacheCopyReadHitsPercent_Type=Integer32
_CpqOsWarCacheCopyReadHitsPercent_Object=MibTableColumn
cpqOsWarCacheCopyReadHitsPercent=_CpqOsWarCacheCopyReadHitsPercent_Object((1,3,6,1,4,1,232,19,2,5,2,1,4),_CpqOsWarCacheCopyReadHitsPercent_Type())
cpqOsWarCacheCopyReadHitsPercent.setMaxAccess(_N)
if mibBuilder.loadTexts:cpqOsWarCacheCopyReadHitsPercent.setStatus(_A)
_CpqOsCriCacheCopyReadHitsPercent_Type=Integer32
_CpqOsCriCacheCopyReadHitsPercent_Object=MibTableColumn
cpqOsCriCacheCopyReadHitsPercent=_CpqOsCriCacheCopyReadHitsPercent_Object((1,3,6,1,4,1,232,19,2,5,2,1,5),_CpqOsCriCacheCopyReadHitsPercent_Type())
cpqOsCriCacheCopyReadHitsPercent.setMaxAccess(_N)
if mibBuilder.loadTexts:cpqOsCriCacheCopyReadHitsPercent.setStatus(_A)
_CpqOsCacheCopyReadsPerSec_Type=Integer32
_CpqOsCacheCopyReadsPerSec_Object=MibTableColumn
cpqOsCacheCopyReadsPerSec=_CpqOsCacheCopyReadsPerSec_Object((1,3,6,1,4,1,232,19,2,5,2,1,6),_CpqOsCacheCopyReadsPerSec_Type())
cpqOsCacheCopyReadsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsCacheCopyReadsPerSec.setStatus(_A)
class _CpqOsCacheCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_CpqOsCacheCondition_Type.__name__=_D
_CpqOsCacheCondition_Object=MibTableColumn
cpqOsCacheCondition=_CpqOsCacheCondition_Object((1,3,6,1,4,1,232,19,2,5,2,1,7),_CpqOsCacheCondition_Type())
cpqOsCacheCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsCacheCondition.setStatus(_A)
_CpqOsPagingFile_ObjectIdentity=ObjectIdentity
cpqOsPagingFile=_CpqOsPagingFile_ObjectIdentity((1,3,6,1,4,1,232,19,2,6))
class _CpqOsPagingFileStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_CpqOsPagingFileStatus_Type.__name__=_D
_CpqOsPagingFileStatus_Object=MibScalar
cpqOsPagingFileStatus=_CpqOsPagingFileStatus_Object((1,3,6,1,4,1,232,19,2,6,1),_CpqOsPagingFileStatus_Type())
cpqOsPagingFileStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsPagingFileStatus.setStatus(_A)
_CpqOsPagingFileTable_Object=MibTable
cpqOsPagingFileTable=_CpqOsPagingFileTable_Object((1,3,6,1,4,1,232,19,2,6,2))
if mibBuilder.loadTexts:cpqOsPagingFileTable.setStatus(_A)
_CpqOsPagingFileEntry_Object=MibTableRow
cpqOsPagingFileEntry=_CpqOsPagingFileEntry_Object((1,3,6,1,4,1,232,19,2,6,2,1))
cpqOsPagingFileEntry.setIndexNames((0,_C,_Q))
if mibBuilder.loadTexts:cpqOsPagingFileEntry.setStatus(_A)
_CpqOsPagingFileIndex_Type=Integer32
_CpqOsPagingFileIndex_Object=MibTableColumn
cpqOsPagingFileIndex=_CpqOsPagingFileIndex_Object((1,3,6,1,4,1,232,19,2,6,2,1,1),_CpqOsPagingFileIndex_Type())
cpqOsPagingFileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsPagingFileIndex.setStatus(_A)
class _CpqOsPagingFileInstance_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqOsPagingFileInstance_Type.__name__=_I
_CpqOsPagingFileInstance_Object=MibTableColumn
cpqOsPagingFileInstance=_CpqOsPagingFileInstance_Object((1,3,6,1,4,1,232,19,2,6,2,1,2),_CpqOsPagingFileInstance_Type())
cpqOsPagingFileInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsPagingFileInstance.setStatus(_A)
_CpqOsPageFileUsagePercent_Type=Integer32
_CpqOsPageFileUsagePercent_Object=MibTableColumn
cpqOsPageFileUsagePercent=_CpqOsPageFileUsagePercent_Object((1,3,6,1,4,1,232,19,2,6,2,1,3),_CpqOsPageFileUsagePercent_Type())
cpqOsPageFileUsagePercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsPageFileUsagePercent.setStatus(_A)
_CpqOsWarPageFileUsagePercent_Type=Integer32
_CpqOsWarPageFileUsagePercent_Object=MibTableColumn
cpqOsWarPageFileUsagePercent=_CpqOsWarPageFileUsagePercent_Object((1,3,6,1,4,1,232,19,2,6,2,1,4),_CpqOsWarPageFileUsagePercent_Type())
cpqOsWarPageFileUsagePercent.setMaxAccess(_N)
if mibBuilder.loadTexts:cpqOsWarPageFileUsagePercent.setStatus(_A)
_CpqOsCriPageFileUsagePercent_Type=Integer32
_CpqOsCriPageFileUsagePercent_Object=MibTableColumn
cpqOsCriPageFileUsagePercent=_CpqOsCriPageFileUsagePercent_Object((1,3,6,1,4,1,232,19,2,6,2,1,5),_CpqOsCriPageFileUsagePercent_Type())
cpqOsCriPageFileUsagePercent.setMaxAccess(_N)
if mibBuilder.loadTexts:cpqOsCriPageFileUsagePercent.setStatus(_A)
class _CpqOsPagingFileCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_CpqOsPagingFileCondition_Type.__name__=_D
_CpqOsPagingFileCondition_Object=MibTableColumn
cpqOsPagingFileCondition=_CpqOsPagingFileCondition_Object((1,3,6,1,4,1,232,19,2,6,2,1,6),_CpqOsPagingFileCondition_Type())
cpqOsPagingFileCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsPagingFileCondition.setStatus(_A)
_CpqOsPagingFileOSManaged_Type=Integer32
_CpqOsPagingFileOSManaged_Object=MibScalar
cpqOsPagingFileOSManaged=_CpqOsPagingFileOSManaged_Object((1,3,6,1,4,1,232,19,2,6,3),_CpqOsPagingFileOSManaged_Type())
cpqOsPagingFileOSManaged.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsPagingFileOSManaged.setStatus(_A)
_CpqOsPhysicalDisk_ObjectIdentity=ObjectIdentity
cpqOsPhysicalDisk=_CpqOsPhysicalDisk_ObjectIdentity((1,3,6,1,4,1,232,19,2,7))
class _CpqOsPhysicalDiskStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_CpqOsPhysicalDiskStatus_Type.__name__=_D
_CpqOsPhysicalDiskStatus_Object=MibScalar
cpqOsPhysicalDiskStatus=_CpqOsPhysicalDiskStatus_Object((1,3,6,1,4,1,232,19,2,7,1),_CpqOsPhysicalDiskStatus_Type())
cpqOsPhysicalDiskStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsPhysicalDiskStatus.setStatus(_A)
_CpqOsPhysicalDiskTable_Object=MibTable
cpqOsPhysicalDiskTable=_CpqOsPhysicalDiskTable_Object((1,3,6,1,4,1,232,19,2,7,2))
if mibBuilder.loadTexts:cpqOsPhysicalDiskTable.setStatus(_A)
_CpqOsPhysicalDiskEntry_Object=MibTableRow
cpqOsPhysicalDiskEntry=_CpqOsPhysicalDiskEntry_Object((1,3,6,1,4,1,232,19,2,7,2,1))
cpqOsPhysicalDiskEntry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:cpqOsPhysicalDiskEntry.setStatus(_A)
_CpqOsPhysicalDiskIndex_Type=Integer32
_CpqOsPhysicalDiskIndex_Object=MibTableColumn
cpqOsPhysicalDiskIndex=_CpqOsPhysicalDiskIndex_Object((1,3,6,1,4,1,232,19,2,7,2,1,1),_CpqOsPhysicalDiskIndex_Type())
cpqOsPhysicalDiskIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsPhysicalDiskIndex.setStatus(_A)
class _CpqOsPhysicalDiskInstance_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqOsPhysicalDiskInstance_Type.__name__=_I
_CpqOsPhysicalDiskInstance_Object=MibTableColumn
cpqOsPhysicalDiskInstance=_CpqOsPhysicalDiskInstance_Object((1,3,6,1,4,1,232,19,2,7,2,1,2),_CpqOsPhysicalDiskInstance_Type())
cpqOsPhysicalDiskInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsPhysicalDiskInstance.setStatus(_A)
_CpqOsPhysicalDiskQueueLength_Type=Integer32
_CpqOsPhysicalDiskQueueLength_Object=MibTableColumn
cpqOsPhysicalDiskQueueLength=_CpqOsPhysicalDiskQueueLength_Object((1,3,6,1,4,1,232,19,2,7,2,1,3),_CpqOsPhysicalDiskQueueLength_Type())
cpqOsPhysicalDiskQueueLength.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsPhysicalDiskQueueLength.setStatus(_A)
_CpqOsPhysicalDiskBusyTimePercent_Type=Integer32
_CpqOsPhysicalDiskBusyTimePercent_Object=MibTableColumn
cpqOsPhysicalDiskBusyTimePercent=_CpqOsPhysicalDiskBusyTimePercent_Object((1,3,6,1,4,1,232,19,2,7,2,1,4),_CpqOsPhysicalDiskBusyTimePercent_Type())
cpqOsPhysicalDiskBusyTimePercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsPhysicalDiskBusyTimePercent.setStatus(_A)
class _CpqOsPhysicalDiskCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_CpqOsPhysicalDiskCondition_Type.__name__=_D
_CpqOsPhysicalDiskCondition_Object=MibTableColumn
cpqOsPhysicalDiskCondition=_CpqOsPhysicalDiskCondition_Object((1,3,6,1,4,1,232,19,2,7,2,1,5),_CpqOsPhysicalDiskCondition_Type())
cpqOsPhysicalDiskCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsPhysicalDiskCondition.setStatus(_A)
_CpqOsPhysicalDiskBytesPersec_Type=Integer32
_CpqOsPhysicalDiskBytesPersec_Object=MibTableColumn
cpqOsPhysicalDiskBytesPersec=_CpqOsPhysicalDiskBytesPersec_Object((1,3,6,1,4,1,232,19,2,7,2,1,6),_CpqOsPhysicalDiskBytesPersec_Type())
cpqOsPhysicalDiskBytesPersec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsPhysicalDiskBytesPersec.setStatus(_A)
_CpqOsPhysicalDiskTransfersPersecx1000_Type=Integer32
_CpqOsPhysicalDiskTransfersPersecx1000_Object=MibTableColumn
cpqOsPhysicalDiskTransfersPersecx1000=_CpqOsPhysicalDiskTransfersPersecx1000_Object((1,3,6,1,4,1,232,19,2,7,2,1,7),_CpqOsPhysicalDiskTransfersPersecx1000_Type())
cpqOsPhysicalDiskTransfersPersecx1000.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsPhysicalDiskTransfersPersecx1000.setStatus(_A)
_CpqOsPhysicalDiskReadsPersecx1000_Type=Integer32
_CpqOsPhysicalDiskReadsPersecx1000_Object=MibTableColumn
cpqOsPhysicalDiskReadsPersecx1000=_CpqOsPhysicalDiskReadsPersecx1000_Object((1,3,6,1,4,1,232,19,2,7,2,1,8),_CpqOsPhysicalDiskReadsPersecx1000_Type())
cpqOsPhysicalDiskReadsPersecx1000.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsPhysicalDiskReadsPersecx1000.setStatus(_A)
_CpqOsPhysicalDiskWritesPersecx1000_Type=Integer32
_CpqOsPhysicalDiskWritesPersecx1000_Object=MibTableColumn
cpqOsPhysicalDiskWritesPersecx1000=_CpqOsPhysicalDiskWritesPersecx1000_Object((1,3,6,1,4,1,232,19,2,7,2,1,9),_CpqOsPhysicalDiskWritesPersecx1000_Type())
cpqOsPhysicalDiskWritesPersecx1000.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsPhysicalDiskWritesPersecx1000.setStatus(_A)
_CpqOsPhysicalDiskReadBytesPersec_Type=Integer32
_CpqOsPhysicalDiskReadBytesPersec_Object=MibTableColumn
cpqOsPhysicalDiskReadBytesPersec=_CpqOsPhysicalDiskReadBytesPersec_Object((1,3,6,1,4,1,232,19,2,7,2,1,10),_CpqOsPhysicalDiskReadBytesPersec_Type())
cpqOsPhysicalDiskReadBytesPersec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsPhysicalDiskReadBytesPersec.setStatus(_A)
_CpqOsPhysicalDiskWriteBytesPersec_Type=Integer32
_CpqOsPhysicalDiskWriteBytesPersec_Object=MibTableColumn
cpqOsPhysicalDiskWriteBytesPersec=_CpqOsPhysicalDiskWriteBytesPersec_Object((1,3,6,1,4,1,232,19,2,7,2,1,11),_CpqOsPhysicalDiskWriteBytesPersec_Type())
cpqOsPhysicalDiskWriteBytesPersec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsPhysicalDiskWriteBytesPersec.setStatus(_A)
_CpqOsPhysicalDiskAvgDisksecPerReadx10000_Type=Integer32
_CpqOsPhysicalDiskAvgDisksecPerReadx10000_Object=MibTableColumn
cpqOsPhysicalDiskAvgDisksecPerReadx10000=_CpqOsPhysicalDiskAvgDisksecPerReadx10000_Object((1,3,6,1,4,1,232,19,2,7,2,1,12),_CpqOsPhysicalDiskAvgDisksecPerReadx10000_Type())
cpqOsPhysicalDiskAvgDisksecPerReadx10000.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsPhysicalDiskAvgDisksecPerReadx10000.setStatus(_A)
_CpqOsPhysicalDiskAvgDisksecPerWritex10000_Type=Integer32
_CpqOsPhysicalDiskAvgDisksecPerWritex10000_Object=MibTableColumn
cpqOsPhysicalDiskAvgDisksecPerWritex10000=_CpqOsPhysicalDiskAvgDisksecPerWritex10000_Object((1,3,6,1,4,1,232,19,2,7,2,1,13),_CpqOsPhysicalDiskAvgDisksecPerWritex10000_Type())
cpqOsPhysicalDiskAvgDisksecPerWritex10000.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsPhysicalDiskAvgDisksecPerWritex10000.setStatus(_A)
_CpqOsPhysicalDiskCurrentDiskQueueLength_Type=Integer32
_CpqOsPhysicalDiskCurrentDiskQueueLength_Object=MibTableColumn
cpqOsPhysicalDiskCurrentDiskQueueLength=_CpqOsPhysicalDiskCurrentDiskQueueLength_Object((1,3,6,1,4,1,232,19,2,7,2,1,14),_CpqOsPhysicalDiskCurrentDiskQueueLength_Type())
cpqOsPhysicalDiskCurrentDiskQueueLength.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsPhysicalDiskCurrentDiskQueueLength.setStatus(_A)
_CpqOsLogicalDisk_ObjectIdentity=ObjectIdentity
cpqOsLogicalDisk=_CpqOsLogicalDisk_ObjectIdentity((1,3,6,1,4,1,232,19,2,8))
class _CpqOsLogicalDiskStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_CpqOsLogicalDiskStatus_Type.__name__=_D
_CpqOsLogicalDiskStatus_Object=MibScalar
cpqOsLogicalDiskStatus=_CpqOsLogicalDiskStatus_Object((1,3,6,1,4,1,232,19,2,8,1),_CpqOsLogicalDiskStatus_Type())
cpqOsLogicalDiskStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsLogicalDiskStatus.setStatus(_A)
_CpqOsLogicalDiskTable_Object=MibTable
cpqOsLogicalDiskTable=_CpqOsLogicalDiskTable_Object((1,3,6,1,4,1,232,19,2,8,2))
if mibBuilder.loadTexts:cpqOsLogicalDiskTable.setStatus(_A)
_CpqOsLogicalDiskEntry_Object=MibTableRow
cpqOsLogicalDiskEntry=_CpqOsLogicalDiskEntry_Object((1,3,6,1,4,1,232,19,2,8,2,1))
cpqOsLogicalDiskEntry.setIndexNames((0,_C,_R))
if mibBuilder.loadTexts:cpqOsLogicalDiskEntry.setStatus(_A)
_CpqOsLogicalDiskIndex_Type=Integer32
_CpqOsLogicalDiskIndex_Object=MibTableColumn
cpqOsLogicalDiskIndex=_CpqOsLogicalDiskIndex_Object((1,3,6,1,4,1,232,19,2,8,2,1,1),_CpqOsLogicalDiskIndex_Type())
cpqOsLogicalDiskIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsLogicalDiskIndex.setStatus(_A)
class _CpqOsLogicalDiskInstance_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqOsLogicalDiskInstance_Type.__name__=_I
_CpqOsLogicalDiskInstance_Object=MibTableColumn
cpqOsLogicalDiskInstance=_CpqOsLogicalDiskInstance_Object((1,3,6,1,4,1,232,19,2,8,2,1,2),_CpqOsLogicalDiskInstance_Type())
cpqOsLogicalDiskInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsLogicalDiskInstance.setStatus(_A)
_CpqOsLogicalDiskFreeSpaceMBytes_Type=Integer32
_CpqOsLogicalDiskFreeSpaceMBytes_Object=MibTableColumn
cpqOsLogicalDiskFreeSpaceMBytes=_CpqOsLogicalDiskFreeSpaceMBytes_Object((1,3,6,1,4,1,232,19,2,8,2,1,3),_CpqOsLogicalDiskFreeSpaceMBytes_Type())
cpqOsLogicalDiskFreeSpaceMBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsLogicalDiskFreeSpaceMBytes.setStatus(_A)
_CpqOsLogicalDiskFreeSpacePercent_Type=Integer32
_CpqOsLogicalDiskFreeSpacePercent_Object=MibTableColumn
cpqOsLogicalDiskFreeSpacePercent=_CpqOsLogicalDiskFreeSpacePercent_Object((1,3,6,1,4,1,232,19,2,8,2,1,4),_CpqOsLogicalDiskFreeSpacePercent_Type())
cpqOsLogicalDiskFreeSpacePercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsLogicalDiskFreeSpacePercent.setStatus(_A)
_CpqOsLogicalDiskQueueLength_Type=Integer32
_CpqOsLogicalDiskQueueLength_Object=MibTableColumn
cpqOsLogicalDiskQueueLength=_CpqOsLogicalDiskQueueLength_Object((1,3,6,1,4,1,232,19,2,8,2,1,5),_CpqOsLogicalDiskQueueLength_Type())
cpqOsLogicalDiskQueueLength.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsLogicalDiskQueueLength.setStatus(_A)
_CpqOsLogicalDiskBusyTimePercent_Type=Integer32
_CpqOsLogicalDiskBusyTimePercent_Object=MibTableColumn
cpqOsLogicalDiskBusyTimePercent=_CpqOsLogicalDiskBusyTimePercent_Object((1,3,6,1,4,1,232,19,2,8,2,1,6),_CpqOsLogicalDiskBusyTimePercent_Type())
cpqOsLogicalDiskBusyTimePercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsLogicalDiskBusyTimePercent.setStatus(_A)
_CpqOsWarLogicalDiskBusyTimePercent_Type=Integer32
_CpqOsWarLogicalDiskBusyTimePercent_Object=MibTableColumn
cpqOsWarLogicalDiskBusyTimePercent=_CpqOsWarLogicalDiskBusyTimePercent_Object((1,3,6,1,4,1,232,19,2,8,2,1,7),_CpqOsWarLogicalDiskBusyTimePercent_Type())
cpqOsWarLogicalDiskBusyTimePercent.setMaxAccess(_N)
if mibBuilder.loadTexts:cpqOsWarLogicalDiskBusyTimePercent.setStatus(_A)
_CpqOsCriLogicalDiskBusyTimePercent_Type=Integer32
_CpqOsCriLogicalDiskBusyTimePercent_Object=MibTableColumn
cpqOsCriLogicalDiskBusyTimePercent=_CpqOsCriLogicalDiskBusyTimePercent_Object((1,3,6,1,4,1,232,19,2,8,2,1,8),_CpqOsCriLogicalDiskBusyTimePercent_Type())
cpqOsCriLogicalDiskBusyTimePercent.setMaxAccess(_N)
if mibBuilder.loadTexts:cpqOsCriLogicalDiskBusyTimePercent.setStatus(_A)
class _CpqOsLogicalDiskCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_CpqOsLogicalDiskCondition_Type.__name__=_D
_CpqOsLogicalDiskCondition_Object=MibTableColumn
cpqOsLogicalDiskCondition=_CpqOsLogicalDiskCondition_Object((1,3,6,1,4,1,232,19,2,8,2,1,9),_CpqOsLogicalDiskCondition_Type())
cpqOsLogicalDiskCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsLogicalDiskCondition.setStatus(_A)
_CpqOsServer_ObjectIdentity=ObjectIdentity
cpqOsServer=_CpqOsServer_ObjectIdentity((1,3,6,1,4,1,232,19,2,9))
class _CpqOsServerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_CpqOsServerStatus_Type.__name__=_D
_CpqOsServerStatus_Object=MibScalar
cpqOsServerStatus=_CpqOsServerStatus_Object((1,3,6,1,4,1,232,19,2,9,1),_CpqOsServerStatus_Type())
cpqOsServerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsServerStatus.setStatus(_A)
_CpqOsServerTotalNetworkUtilizationBytesPerSec_Type=Integer32
_CpqOsServerTotalNetworkUtilizationBytesPerSec_Object=MibScalar
cpqOsServerTotalNetworkUtilizationBytesPerSec=_CpqOsServerTotalNetworkUtilizationBytesPerSec_Object((1,3,6,1,4,1,232,19,2,9,2),_CpqOsServerTotalNetworkUtilizationBytesPerSec_Type())
cpqOsServerTotalNetworkUtilizationBytesPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsServerTotalNetworkUtilizationBytesPerSec.setStatus(_A)
_CpqOsServerSessions_Type=Integer32
_CpqOsServerSessions_Object=MibScalar
cpqOsServerSessions=_CpqOsServerSessions_Object((1,3,6,1,4,1,232,19,2,9,3),_CpqOsServerSessions_Type())
cpqOsServerSessions.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsServerSessions.setStatus(_A)
_CpqOsServerAccessPermissionErrors_Type=Integer32
_CpqOsServerAccessPermissionErrors_Object=MibScalar
cpqOsServerAccessPermissionErrors=_CpqOsServerAccessPermissionErrors_Object((1,3,6,1,4,1,232,19,2,9,4),_CpqOsServerAccessPermissionErrors_Type())
cpqOsServerAccessPermissionErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsServerAccessPermissionErrors.setStatus(_A)
_CpqOsServerAccessGrantedErrors_Type=Integer32
_CpqOsServerAccessGrantedErrors_Object=MibScalar
cpqOsServerAccessGrantedErrors=_CpqOsServerAccessGrantedErrors_Object((1,3,6,1,4,1,232,19,2,9,5),_CpqOsServerAccessGrantedErrors_Type())
cpqOsServerAccessGrantedErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsServerAccessGrantedErrors.setStatus(_A)
_CpqOsServerLogonErrors_Type=Integer32
_CpqOsServerLogonErrors_Object=MibScalar
cpqOsServerLogonErrors=_CpqOsServerLogonErrors_Object((1,3,6,1,4,1,232,19,2,9,6),_CpqOsServerLogonErrors_Type())
cpqOsServerLogonErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsServerLogonErrors.setStatus(_A)
_CpqOsServerSessionsErroredOut_Type=Integer32
_CpqOsServerSessionsErroredOut_Object=MibScalar
cpqOsServerSessionsErroredOut=_CpqOsServerSessionsErroredOut_Object((1,3,6,1,4,1,232,19,2,9,7),_CpqOsServerSessionsErroredOut_Type())
cpqOsServerSessionsErroredOut.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsServerSessionsErroredOut.setStatus(_A)
_CpqOsServerContextBlocksQueuePerSec_Type=Integer32
_CpqOsServerContextBlocksQueuePerSec_Object=MibScalar
cpqOsServerContextBlocksQueuePerSec=_CpqOsServerContextBlocksQueuePerSec_Object((1,3,6,1,4,1,232,19,2,9,8),_CpqOsServerContextBlocksQueuePerSec_Type())
cpqOsServerContextBlocksQueuePerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsServerContextBlocksQueuePerSec.setStatus(_A)
_CpqOsNetworkInterface_ObjectIdentity=ObjectIdentity
cpqOsNetworkInterface=_CpqOsNetworkInterface_ObjectIdentity((1,3,6,1,4,1,232,19,2,10))
class _CpqOsNetworkInterfaceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_CpqOsNetworkInterfaceStatus_Type.__name__=_D
_CpqOsNetworkInterfaceStatus_Object=MibScalar
cpqOsNetworkInterfaceStatus=_CpqOsNetworkInterfaceStatus_Object((1,3,6,1,4,1,232,19,2,10,1),_CpqOsNetworkInterfaceStatus_Type())
cpqOsNetworkInterfaceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsNetworkInterfaceStatus.setStatus(_A)
_CpqOsNetworkInterfaceTable_Object=MibTable
cpqOsNetworkInterfaceTable=_CpqOsNetworkInterfaceTable_Object((1,3,6,1,4,1,232,19,2,10,2))
if mibBuilder.loadTexts:cpqOsNetworkInterfaceTable.setStatus(_A)
_CpqOsNetworkInterfaceEntry_Object=MibTableRow
cpqOsNetworkInterfaceEntry=_CpqOsNetworkInterfaceEntry_Object((1,3,6,1,4,1,232,19,2,10,2,1))
cpqOsNetworkInterfaceEntry.setIndexNames((0,_C,_c))
if mibBuilder.loadTexts:cpqOsNetworkInterfaceEntry.setStatus(_A)
_CpqOsNetworkInterfaceIndex_Type=Integer32
_CpqOsNetworkInterfaceIndex_Object=MibTableColumn
cpqOsNetworkInterfaceIndex=_CpqOsNetworkInterfaceIndex_Object((1,3,6,1,4,1,232,19,2,10,2,1,1),_CpqOsNetworkInterfaceIndex_Type())
cpqOsNetworkInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsNetworkInterfaceIndex.setStatus(_A)
class _CpqOsNetworkInterfaceInstance_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqOsNetworkInterfaceInstance_Type.__name__=_I
_CpqOsNetworkInterfaceInstance_Object=MibTableColumn
cpqOsNetworkInterfaceInstance=_CpqOsNetworkInterfaceInstance_Object((1,3,6,1,4,1,232,19,2,10,2,1,2),_CpqOsNetworkInterfaceInstance_Type())
cpqOsNetworkInterfaceInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsNetworkInterfaceInstance.setStatus(_A)
_CpqOsNetworkTotalBytesPerSec_Type=Integer32
_CpqOsNetworkTotalBytesPerSec_Object=MibTableColumn
cpqOsNetworkTotalBytesPerSec=_CpqOsNetworkTotalBytesPerSec_Object((1,3,6,1,4,1,232,19,2,10,2,1,3),_CpqOsNetworkTotalBytesPerSec_Type())
cpqOsNetworkTotalBytesPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsNetworkTotalBytesPerSec.setStatus(_A)
_CpqOsNetworkPacketsPerSec_Type=Integer32
_CpqOsNetworkPacketsPerSec_Object=MibTableColumn
cpqOsNetworkPacketsPerSec=_CpqOsNetworkPacketsPerSec_Object((1,3,6,1,4,1,232,19,2,10,2,1,4),_CpqOsNetworkPacketsPerSec_Type())
cpqOsNetworkPacketsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsNetworkPacketsPerSec.setStatus(_A)
_CpqOsNetworkOutputQueueLength_Type=Integer32
_CpqOsNetworkOutputQueueLength_Object=MibTableColumn
cpqOsNetworkOutputQueueLength=_CpqOsNetworkOutputQueueLength_Object((1,3,6,1,4,1,232,19,2,10,2,1,5),_CpqOsNetworkOutputQueueLength_Type())
cpqOsNetworkOutputQueueLength.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsNetworkOutputQueueLength.setStatus(_A)
_CpqOsNetworkPktOutboundErrors_Type=Integer32
_CpqOsNetworkPktOutboundErrors_Object=MibTableColumn
cpqOsNetworkPktOutboundErrors=_CpqOsNetworkPktOutboundErrors_Object((1,3,6,1,4,1,232,19,2,10,2,1,6),_CpqOsNetworkPktOutboundErrors_Type())
cpqOsNetworkPktOutboundErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsNetworkPktOutboundErrors.setStatus(_A)
_CpqOsNetworkPktReceiveErrors_Type=Integer32
_CpqOsNetworkPktReceiveErrors_Object=MibTableColumn
cpqOsNetworkPktReceiveErrors=_CpqOsNetworkPktReceiveErrors_Object((1,3,6,1,4,1,232,19,2,10,2,1,7),_CpqOsNetworkPktReceiveErrors_Type())
cpqOsNetworkPktReceiveErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsNetworkPktReceiveErrors.setStatus(_A)
_CpqOsNetworkCurrentBandWidth_Type=Integer32
_CpqOsNetworkCurrentBandWidth_Object=MibTableColumn
cpqOsNetworkCurrentBandWidth=_CpqOsNetworkCurrentBandWidth_Object((1,3,6,1,4,1,232,19,2,10,2,1,8),_CpqOsNetworkCurrentBandWidth_Type())
cpqOsNetworkCurrentBandWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsNetworkCurrentBandWidth.setStatus(_A)
class _CpqOsNetworkInterfaceCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_CpqOsNetworkInterfaceCondition_Type.__name__=_D
_CpqOsNetworkInterfaceCondition_Object=MibTableColumn
cpqOsNetworkInterfaceCondition=_CpqOsNetworkInterfaceCondition_Object((1,3,6,1,4,1,232,19,2,10,2,1,9),_CpqOsNetworkInterfaceCondition_Type())
cpqOsNetworkInterfaceCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsNetworkInterfaceCondition.setStatus(_A)
_CpqOsNetworkBytesSentPersec_Type=Integer32
_CpqOsNetworkBytesSentPersec_Object=MibTableColumn
cpqOsNetworkBytesSentPersec=_CpqOsNetworkBytesSentPersec_Object((1,3,6,1,4,1,232,19,2,10,2,1,10),_CpqOsNetworkBytesSentPersec_Type())
cpqOsNetworkBytesSentPersec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsNetworkBytesSentPersec.setStatus(_A)
_CpqOsNetworkBytesReceivedPersec_Type=Integer32
_CpqOsNetworkBytesReceivedPersec_Object=MibTableColumn
cpqOsNetworkBytesReceivedPersec=_CpqOsNetworkBytesReceivedPersec_Object((1,3,6,1,4,1,232,19,2,10,2,1,11),_CpqOsNetworkBytesReceivedPersec_Type())
cpqOsNetworkBytesReceivedPersec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsNetworkBytesReceivedPersec.setStatus(_A)
_CpqOsNetworkPacketsSentPersecx1000_Type=Integer32
_CpqOsNetworkPacketsSentPersecx1000_Object=MibTableColumn
cpqOsNetworkPacketsSentPersecx1000=_CpqOsNetworkPacketsSentPersecx1000_Object((1,3,6,1,4,1,232,19,2,10,2,1,12),_CpqOsNetworkPacketsSentPersecx1000_Type())
cpqOsNetworkPacketsSentPersecx1000.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsNetworkPacketsSentPersecx1000.setStatus(_A)
_CpqOsNetworkPacketsReceivedPersecx1000_Type=Integer32
_CpqOsNetworkPacketsReceivedPersecx1000_Object=MibTableColumn
cpqOsNetworkPacketsReceivedPersecx1000=_CpqOsNetworkPacketsReceivedPersecx1000_Object((1,3,6,1,4,1,232,19,2,10,2,1,13),_CpqOsNetworkPacketsReceivedPersecx1000_Type())
cpqOsNetworkPacketsReceivedPersecx1000.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsNetworkPacketsReceivedPersecx1000.setStatus(_A)
_CpqOsTcp_ObjectIdentity=ObjectIdentity
cpqOsTcp=_CpqOsTcp_ObjectIdentity((1,3,6,1,4,1,232,19,2,11))
class _CpqOsTcpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_CpqOsTcpStatus_Type.__name__=_D
_CpqOsTcpStatus_Object=MibScalar
cpqOsTcpStatus=_CpqOsTcpStatus_Object((1,3,6,1,4,1,232,19,2,11,1),_CpqOsTcpStatus_Type())
cpqOsTcpStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsTcpStatus.setStatus(_A)
_CpqOsTcpTable_Object=MibTable
cpqOsTcpTable=_CpqOsTcpTable_Object((1,3,6,1,4,1,232,19,2,11,2))
if mibBuilder.loadTexts:cpqOsTcpTable.setStatus(_A)
_CpqOsTcpEntry_Object=MibTableRow
cpqOsTcpEntry=_CpqOsTcpEntry_Object((1,3,6,1,4,1,232,19,2,11,2,1))
cpqOsTcpEntry.setIndexNames((0,_C,_d))
if mibBuilder.loadTexts:cpqOsTcpEntry.setStatus(_A)
_CpqOsTcpIndex_Type=Integer32
_CpqOsTcpIndex_Object=MibTableColumn
cpqOsTcpIndex=_CpqOsTcpIndex_Object((1,3,6,1,4,1,232,19,2,11,2,1,1),_CpqOsTcpIndex_Type())
cpqOsTcpIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsTcpIndex.setStatus(_A)
class _CpqOsTcpInstance_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqOsTcpInstance_Type.__name__=_I
_CpqOsTcpInstance_Object=MibTableColumn
cpqOsTcpInstance=_CpqOsTcpInstance_Object((1,3,6,1,4,1,232,19,2,11,2,1,2),_CpqOsTcpInstance_Type())
cpqOsTcpInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsTcpInstance.setStatus(_A)
_CpqOsTcpActiveConnections_Type=Integer32
_CpqOsTcpActiveConnections_Object=MibTableColumn
cpqOsTcpActiveConnections=_CpqOsTcpActiveConnections_Object((1,3,6,1,4,1,232,19,2,11,2,1,3),_CpqOsTcpActiveConnections_Type())
cpqOsTcpActiveConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsTcpActiveConnections.setStatus(_A)
_CpqOsTcpEstablishedConections_Type=Integer32
_CpqOsTcpEstablishedConections_Object=MibTableColumn
cpqOsTcpEstablishedConections=_CpqOsTcpEstablishedConections_Object((1,3,6,1,4,1,232,19,2,11,2,1,4),_CpqOsTcpEstablishedConections_Type())
cpqOsTcpEstablishedConections.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsTcpEstablishedConections.setStatus(_A)
_CpqOsTcpSegmentsPerSec_Type=Integer32
_CpqOsTcpSegmentsPerSec_Object=MibTableColumn
cpqOsTcpSegmentsPerSec=_CpqOsTcpSegmentsPerSec_Object((1,3,6,1,4,1,232,19,2,11,2,1,5),_CpqOsTcpSegmentsPerSec_Type())
cpqOsTcpSegmentsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsTcpSegmentsPerSec.setStatus(_A)
_CpqOsTcpRetransmittedSegmentsPerSec_Type=Integer32
_CpqOsTcpRetransmittedSegmentsPerSec_Object=MibTableColumn
cpqOsTcpRetransmittedSegmentsPerSec=_CpqOsTcpRetransmittedSegmentsPerSec_Object((1,3,6,1,4,1,232,19,2,11,2,1,6),_CpqOsTcpRetransmittedSegmentsPerSec_Type())
cpqOsTcpRetransmittedSegmentsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsTcpRetransmittedSegmentsPerSec.setStatus(_A)
_CpqOsTcpConnectionFailures_Type=Integer32
_CpqOsTcpConnectionFailures_Object=MibTableColumn
cpqOsTcpConnectionFailures=_CpqOsTcpConnectionFailures_Object((1,3,6,1,4,1,232,19,2,11,2,1,7),_CpqOsTcpConnectionFailures_Type())
cpqOsTcpConnectionFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsTcpConnectionFailures.setStatus(_A)
class _CpqOsTcpCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_CpqOsTcpCondition_Type.__name__=_D
_CpqOsTcpCondition_Object=MibTableColumn
cpqOsTcpCondition=_CpqOsTcpCondition_Object((1,3,6,1,4,1,232,19,2,11,2,1,8),_CpqOsTcpCondition_Type())
cpqOsTcpCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsTcpCondition.setStatus(_A)
_CpqOsProcess_ObjectIdentity=ObjectIdentity
cpqOsProcess=_CpqOsProcess_ObjectIdentity((1,3,6,1,4,1,232,19,2,12))
class _CpqOsProcessStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_CpqOsProcessStatus_Type.__name__=_D
_CpqOsProcessStatus_Object=MibScalar
cpqOsProcessStatus=_CpqOsProcessStatus_Object((1,3,6,1,4,1,232,19,2,12,1),_CpqOsProcessStatus_Type())
cpqOsProcessStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsProcessStatus.setStatus(_A)
_CpqOsProcessTable_Object=MibTable
cpqOsProcessTable=_CpqOsProcessTable_Object((1,3,6,1,4,1,232,19,2,12,2))
if mibBuilder.loadTexts:cpqOsProcessTable.setStatus(_A)
_CpqOsProcessEntry_Object=MibTableRow
cpqOsProcessEntry=_CpqOsProcessEntry_Object((1,3,6,1,4,1,232,19,2,12,2,1))
cpqOsProcessEntry.setIndexNames((0,_C,_e))
if mibBuilder.loadTexts:cpqOsProcessEntry.setStatus(_A)
_CpqOsProcessIndex_Type=Integer32
_CpqOsProcessIndex_Object=MibTableColumn
cpqOsProcessIndex=_CpqOsProcessIndex_Object((1,3,6,1,4,1,232,19,2,12,2,1,1),_CpqOsProcessIndex_Type())
cpqOsProcessIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsProcessIndex.setStatus(_A)
class _CpqOsProcessInstance_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqOsProcessInstance_Type.__name__=_I
_CpqOsProcessInstance_Object=MibTableColumn
cpqOsProcessInstance=_CpqOsProcessInstance_Object((1,3,6,1,4,1,232,19,2,12,2,1,2),_CpqOsProcessInstance_Type())
cpqOsProcessInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsProcessInstance.setStatus(_A)
_CpqOsProcessThreadCount_Type=Integer32
_CpqOsProcessThreadCount_Object=MibTableColumn
cpqOsProcessThreadCount=_CpqOsProcessThreadCount_Object((1,3,6,1,4,1,232,19,2,12,2,1,3),_CpqOsProcessThreadCount_Type())
cpqOsProcessThreadCount.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsProcessThreadCount.setStatus(_A)
_CpqOsProcessPrivateBytes_Type=Integer32
_CpqOsProcessPrivateBytes_Object=MibTableColumn
cpqOsProcessPrivateBytes=_CpqOsProcessPrivateBytes_Object((1,3,6,1,4,1,232,19,2,12,2,1,4),_CpqOsProcessPrivateBytes_Type())
cpqOsProcessPrivateBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsProcessPrivateBytes.setStatus(_A)
_CpqOsProcessPageFileBytes_Type=Integer32
_CpqOsProcessPageFileBytes_Object=MibTableColumn
cpqOsProcessPageFileBytes=_CpqOsProcessPageFileBytes_Object((1,3,6,1,4,1,232,19,2,12,2,1,5),_CpqOsProcessPageFileBytes_Type())
cpqOsProcessPageFileBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsProcessPageFileBytes.setStatus(_A)
_CpqOsProcessWorkingSet_Type=Integer32
_CpqOsProcessWorkingSet_Object=MibTableColumn
cpqOsProcessWorkingSet=_CpqOsProcessWorkingSet_Object((1,3,6,1,4,1,232,19,2,12,2,1,6),_CpqOsProcessWorkingSet_Type())
cpqOsProcessWorkingSet.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsProcessWorkingSet.setStatus(_A)
_CpqOsProcessCpuTimePercent_Type=Integer32
_CpqOsProcessCpuTimePercent_Object=MibTableColumn
cpqOsProcessCpuTimePercent=_CpqOsProcessCpuTimePercent_Object((1,3,6,1,4,1,232,19,2,12,2,1,7),_CpqOsProcessCpuTimePercent_Type())
cpqOsProcessCpuTimePercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsProcessCpuTimePercent.setStatus(_A)
_CpqOsProcessPrivilegedTimePercent_Type=Integer32
_CpqOsProcessPrivilegedTimePercent_Object=MibTableColumn
cpqOsProcessPrivilegedTimePercent=_CpqOsProcessPrivilegedTimePercent_Object((1,3,6,1,4,1,232,19,2,12,2,1,8),_CpqOsProcessPrivilegedTimePercent_Type())
cpqOsProcessPrivilegedTimePercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsProcessPrivilegedTimePercent.setStatus(_A)
_CpqOsProcessPageFaultsPerSec_Type=Integer32
_CpqOsProcessPageFaultsPerSec_Object=MibTableColumn
cpqOsProcessPageFaultsPerSec=_CpqOsProcessPageFaultsPerSec_Object((1,3,6,1,4,1,232,19,2,12,2,1,9),_CpqOsProcessPageFaultsPerSec_Type())
cpqOsProcessPageFaultsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsProcessPageFaultsPerSec.setStatus(_A)
class _CpqOsProcessCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3),(_H,4)))
_CpqOsProcessCondition_Type.__name__=_D
_CpqOsProcessCondition_Object=MibTableColumn
cpqOsProcessCondition=_CpqOsProcessCondition_Object((1,3,6,1,4,1,232,19,2,12,2,1,10),_CpqOsProcessCondition_Type())
cpqOsProcessCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqOsProcessCondition.setStatus(_A)
cpqOsCpuTimeDegraded=NotificationType((1,3,6,1,4,1,232,0,19001))
cpqOsCpuTimeDegraded.setObjects(*((_L,_M),(_J,_K),(_C,_O),(_C,_S),(_C,_T)))
if mibBuilder.loadTexts:cpqOsCpuTimeDegraded.setStatus('')
cpqOsCpuTimeFailed=NotificationType((1,3,6,1,4,1,232,0,19002))
cpqOsCpuTimeFailed.setObjects(*((_L,_M),(_J,_K),(_C,_O),(_C,_S),(_C,_T)))
if mibBuilder.loadTexts:cpqOsCpuTimeFailed.setStatus('')
cpqOsCacheCopyReadHitsDegraded=NotificationType((1,3,6,1,4,1,232,0,19003))
cpqOsCacheCopyReadHitsDegraded.setObjects(*((_L,_M),(_J,_K),(_C,_P),(_C,_U),(_C,_V)))
if mibBuilder.loadTexts:cpqOsCacheCopyReadHitsDegraded.setStatus('')
cpqOsCacheCopyReadHitsFailed=NotificationType((1,3,6,1,4,1,232,0,19004))
cpqOsCacheCopyReadHitsFailed.setObjects(*((_L,_M),(_J,_K),(_C,_P),(_C,_U),(_C,_V)))
if mibBuilder.loadTexts:cpqOsCacheCopyReadHitsFailed.setStatus('')
cpqOsPageFileUsageDegraded=NotificationType((1,3,6,1,4,1,232,0,19005))
cpqOsPageFileUsageDegraded.setObjects(*((_L,_M),(_J,_K),(_C,_Q),(_C,_W),(_C,_X)))
if mibBuilder.loadTexts:cpqOsPageFileUsageDegraded.setStatus('')
cpqOsPageFileUsageFailed=NotificationType((1,3,6,1,4,1,232,0,19006))
cpqOsPageFileUsageFailed.setObjects(*((_L,_M),(_J,_K),(_C,_Q),(_C,_W),(_C,_X)))
if mibBuilder.loadTexts:cpqOsPageFileUsageFailed.setStatus('')
cpqOsLogicalDiskBusyTimeDegraded=NotificationType((1,3,6,1,4,1,232,0,19007))
cpqOsLogicalDiskBusyTimeDegraded.setObjects(*((_L,_M),(_J,_K),(_C,_R),(_C,_Y),(_C,_Z)))
if mibBuilder.loadTexts:cpqOsLogicalDiskBusyTimeDegraded.setStatus('')
cpqOsLogicalDiskBusyTimeFailed=NotificationType((1,3,6,1,4,1,232,0,19008))
cpqOsLogicalDiskBusyTimeFailed.setObjects(*((_L,_M),(_J,_K),(_C,_R),(_C,_Y),(_C,_Z)))
if mibBuilder.loadTexts:cpqOsLogicalDiskBusyTimeFailed.setStatus('')
mibBuilder.exportSymbols(_C,**{'cpqOsCpuTimeDegraded':cpqOsCpuTimeDegraded,'cpqOsCpuTimeFailed':cpqOsCpuTimeFailed,'cpqOsCacheCopyReadHitsDegraded':cpqOsCacheCopyReadHitsDegraded,'cpqOsCacheCopyReadHitsFailed':cpqOsCacheCopyReadHitsFailed,'cpqOsPageFileUsageDegraded':cpqOsPageFileUsageDegraded,'cpqOsPageFileUsageFailed':cpqOsPageFileUsageFailed,'cpqOsLogicalDiskBusyTimeDegraded':cpqOsLogicalDiskBusyTimeDegraded,'cpqOsLogicalDiskBusyTimeFailed':cpqOsLogicalDiskBusyTimeFailed,'cpqWinOsMgmt':cpqWinOsMgmt,'cpqOsMibRev':cpqOsMibRev,'cpqOsMibRevMajor':cpqOsMibRevMajor,'cpqOsMibRevMinor':cpqOsMibRevMinor,'cpqOsMibCondition':cpqOsMibCondition,'cpqOsComponent':cpqOsComponent,'cpqOsInterface':cpqOsInterface,'cpqOsCommon':cpqOsCommon,'cpqOsCommonPollFreq':cpqOsCommonPollFreq,'cpqOsSystem':cpqOsSystem,'cpqOsSystemStatus':cpqOsSystemStatus,'cpqOsSystemUpTime':cpqOsSystemUpTime,'cpqOsSystemThreads':cpqOsSystemThreads,'cpqOsSysContextSwitchesPersec':cpqOsSysContextSwitchesPersec,'cpqOsSysCpuQueueLength':cpqOsSysCpuQueueLength,'cpqOsSysProcesses':cpqOsSysProcesses,'cpqOsSysRegistryInUsePercent':cpqOsSysRegistryInUsePercent,'cpqOsProcessor':cpqOsProcessor,'cpqOsProcessorStatus':cpqOsProcessorStatus,'cpqOsProcessorTable':cpqOsProcessorTable,'cpqOsProcessorEntry':cpqOsProcessorEntry,_O:cpqOsCpuIndex,_S:cpqOsCpuInstance,'cpqOsCpuInterruptsPerSec':cpqOsCpuInterruptsPerSec,_T:cpqOsCpuTimePercent,'cpqOsWarCpuTimePercent':cpqOsWarCpuTimePercent,'cpqOsCriCpuTimePercent':cpqOsCriCpuTimePercent,'cpqOsCpuUserTimePercent':cpqOsCpuUserTimePercent,'cpqOsCpuPrivilegedTimePercent':cpqOsCpuPrivilegedTimePercent,'cpqOsCpuCondition':cpqOsCpuCondition,'cpqOsCpuPercentDPCTime':cpqOsCpuPercentDPCTime,'cpqOsCpuPercentInterruptTime':cpqOsCpuPercentInterruptTime,'cpqOsMemory':cpqOsMemory,'cpqOsMemoryStatus':cpqOsMemoryStatus,'cpqOsMemAvailableKBytes':cpqOsMemAvailableKBytes,'cpqOsMemPagesPerSec':cpqOsMemPagesPerSec,'cpqOsMemPagesInputPerSec':cpqOsMemPagesInputPerSec,'cpqOsMemPagesOutputPerSec':cpqOsMemPagesOutputPerSec,'cpqOsMemPageFaultsPerSec':cpqOsMemPageFaultsPerSec,'cpqOsMemCacheFaultsPerSec':cpqOsMemCacheFaultsPerSec,'cpqOsMemPageReadsPerSecx1000':cpqOsMemPageReadsPerSecx1000,'cpqOsMemPageWritesPerSecx1000':cpqOsMemPageWritesPerSecx1000,'cpqOsMemPoolNonpagedBytes':cpqOsMemPoolNonpagedBytes,'cpqOsMemCacheBytes':cpqOsMemCacheBytes,'cpqOsCache':cpqOsCache,'cpqOsCacheStatus':cpqOsCacheStatus,'cpqOsCacheTable':cpqOsCacheTable,'cpqOsCacheEntry':cpqOsCacheEntry,_P:cpqOsCacheIndex,_U:cpqOsCacheInstance,_V:cpqOsCacheCopyReadHitsPercent,'cpqOsWarCacheCopyReadHitsPercent':cpqOsWarCacheCopyReadHitsPercent,'cpqOsCriCacheCopyReadHitsPercent':cpqOsCriCacheCopyReadHitsPercent,'cpqOsCacheCopyReadsPerSec':cpqOsCacheCopyReadsPerSec,'cpqOsCacheCondition':cpqOsCacheCondition,'cpqOsPagingFile':cpqOsPagingFile,'cpqOsPagingFileStatus':cpqOsPagingFileStatus,'cpqOsPagingFileTable':cpqOsPagingFileTable,'cpqOsPagingFileEntry':cpqOsPagingFileEntry,_Q:cpqOsPagingFileIndex,_W:cpqOsPagingFileInstance,_X:cpqOsPageFileUsagePercent,'cpqOsWarPageFileUsagePercent':cpqOsWarPageFileUsagePercent,'cpqOsCriPageFileUsagePercent':cpqOsCriPageFileUsagePercent,'cpqOsPagingFileCondition':cpqOsPagingFileCondition,'cpqOsPagingFileOSManaged':cpqOsPagingFileOSManaged,'cpqOsPhysicalDisk':cpqOsPhysicalDisk,'cpqOsPhysicalDiskStatus':cpqOsPhysicalDiskStatus,'cpqOsPhysicalDiskTable':cpqOsPhysicalDiskTable,'cpqOsPhysicalDiskEntry':cpqOsPhysicalDiskEntry,_b:cpqOsPhysicalDiskIndex,'cpqOsPhysicalDiskInstance':cpqOsPhysicalDiskInstance,'cpqOsPhysicalDiskQueueLength':cpqOsPhysicalDiskQueueLength,'cpqOsPhysicalDiskBusyTimePercent':cpqOsPhysicalDiskBusyTimePercent,'cpqOsPhysicalDiskCondition':cpqOsPhysicalDiskCondition,'cpqOsPhysicalDiskBytesPersec':cpqOsPhysicalDiskBytesPersec,'cpqOsPhysicalDiskTransfersPersecx1000':cpqOsPhysicalDiskTransfersPersecx1000,'cpqOsPhysicalDiskReadsPersecx1000':cpqOsPhysicalDiskReadsPersecx1000,'cpqOsPhysicalDiskWritesPersecx1000':cpqOsPhysicalDiskWritesPersecx1000,'cpqOsPhysicalDiskReadBytesPersec':cpqOsPhysicalDiskReadBytesPersec,'cpqOsPhysicalDiskWriteBytesPersec':cpqOsPhysicalDiskWriteBytesPersec,'cpqOsPhysicalDiskAvgDisksecPerReadx10000':cpqOsPhysicalDiskAvgDisksecPerReadx10000,'cpqOsPhysicalDiskAvgDisksecPerWritex10000':cpqOsPhysicalDiskAvgDisksecPerWritex10000,'cpqOsPhysicalDiskCurrentDiskQueueLength':cpqOsPhysicalDiskCurrentDiskQueueLength,'cpqOsLogicalDisk':cpqOsLogicalDisk,'cpqOsLogicalDiskStatus':cpqOsLogicalDiskStatus,'cpqOsLogicalDiskTable':cpqOsLogicalDiskTable,'cpqOsLogicalDiskEntry':cpqOsLogicalDiskEntry,_R:cpqOsLogicalDiskIndex,_Y:cpqOsLogicalDiskInstance,'cpqOsLogicalDiskFreeSpaceMBytes':cpqOsLogicalDiskFreeSpaceMBytes,'cpqOsLogicalDiskFreeSpacePercent':cpqOsLogicalDiskFreeSpacePercent,'cpqOsLogicalDiskQueueLength':cpqOsLogicalDiskQueueLength,_Z:cpqOsLogicalDiskBusyTimePercent,'cpqOsWarLogicalDiskBusyTimePercent':cpqOsWarLogicalDiskBusyTimePercent,'cpqOsCriLogicalDiskBusyTimePercent':cpqOsCriLogicalDiskBusyTimePercent,'cpqOsLogicalDiskCondition':cpqOsLogicalDiskCondition,'cpqOsServer':cpqOsServer,'cpqOsServerStatus':cpqOsServerStatus,'cpqOsServerTotalNetworkUtilizationBytesPerSec':cpqOsServerTotalNetworkUtilizationBytesPerSec,'cpqOsServerSessions':cpqOsServerSessions,'cpqOsServerAccessPermissionErrors':cpqOsServerAccessPermissionErrors,'cpqOsServerAccessGrantedErrors':cpqOsServerAccessGrantedErrors,'cpqOsServerLogonErrors':cpqOsServerLogonErrors,'cpqOsServerSessionsErroredOut':cpqOsServerSessionsErroredOut,'cpqOsServerContextBlocksQueuePerSec':cpqOsServerContextBlocksQueuePerSec,'cpqOsNetworkInterface':cpqOsNetworkInterface,'cpqOsNetworkInterfaceStatus':cpqOsNetworkInterfaceStatus,'cpqOsNetworkInterfaceTable':cpqOsNetworkInterfaceTable,'cpqOsNetworkInterfaceEntry':cpqOsNetworkInterfaceEntry,_c:cpqOsNetworkInterfaceIndex,'cpqOsNetworkInterfaceInstance':cpqOsNetworkInterfaceInstance,'cpqOsNetworkTotalBytesPerSec':cpqOsNetworkTotalBytesPerSec,'cpqOsNetworkPacketsPerSec':cpqOsNetworkPacketsPerSec,'cpqOsNetworkOutputQueueLength':cpqOsNetworkOutputQueueLength,'cpqOsNetworkPktOutboundErrors':cpqOsNetworkPktOutboundErrors,'cpqOsNetworkPktReceiveErrors':cpqOsNetworkPktReceiveErrors,'cpqOsNetworkCurrentBandWidth':cpqOsNetworkCurrentBandWidth,'cpqOsNetworkInterfaceCondition':cpqOsNetworkInterfaceCondition,'cpqOsNetworkBytesSentPersec':cpqOsNetworkBytesSentPersec,'cpqOsNetworkBytesReceivedPersec':cpqOsNetworkBytesReceivedPersec,'cpqOsNetworkPacketsSentPersecx1000':cpqOsNetworkPacketsSentPersecx1000,'cpqOsNetworkPacketsReceivedPersecx1000':cpqOsNetworkPacketsReceivedPersecx1000,'cpqOsTcp':cpqOsTcp,'cpqOsTcpStatus':cpqOsTcpStatus,'cpqOsTcpTable':cpqOsTcpTable,'cpqOsTcpEntry':cpqOsTcpEntry,_d:cpqOsTcpIndex,'cpqOsTcpInstance':cpqOsTcpInstance,'cpqOsTcpActiveConnections':cpqOsTcpActiveConnections,'cpqOsTcpEstablishedConections':cpqOsTcpEstablishedConections,'cpqOsTcpSegmentsPerSec':cpqOsTcpSegmentsPerSec,'cpqOsTcpRetransmittedSegmentsPerSec':cpqOsTcpRetransmittedSegmentsPerSec,'cpqOsTcpConnectionFailures':cpqOsTcpConnectionFailures,'cpqOsTcpCondition':cpqOsTcpCondition,'cpqOsProcess':cpqOsProcess,'cpqOsProcessStatus':cpqOsProcessStatus,'cpqOsProcessTable':cpqOsProcessTable,'cpqOsProcessEntry':cpqOsProcessEntry,_e:cpqOsProcessIndex,'cpqOsProcessInstance':cpqOsProcessInstance,'cpqOsProcessThreadCount':cpqOsProcessThreadCount,'cpqOsProcessPrivateBytes':cpqOsProcessPrivateBytes,'cpqOsProcessPageFileBytes':cpqOsProcessPageFileBytes,'cpqOsProcessWorkingSet':cpqOsProcessWorkingSet,'cpqOsProcessCpuTimePercent':cpqOsProcessCpuTimePercent,'cpqOsProcessPrivilegedTimePercent':cpqOsProcessPrivilegedTimePercent,'cpqOsProcessPageFaultsPerSec':cpqOsProcessPageFaultsPerSec,'cpqOsProcessCondition':cpqOsProcessCondition})