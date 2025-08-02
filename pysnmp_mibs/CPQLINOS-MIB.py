_J='cpqLinOsNetworkInterfaceIndex'
_I='cpqLinOsDiskMinorIndex'
_H='cpqLinOsDiskMajorIndex'
_G='cpqLinOsCpuIndex'
_F='NotificationType'
_E='CPQLINOS-MIB'
_D='DisplayString'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,=mibBuilder.importSymbols('CPQHOST-MIB','compaq')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols('SNMPv2-MIB','sysName')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_F,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_F,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
_CpqLinOsMgmt_ObjectIdentity=ObjectIdentity
cpqLinOsMgmt=_CpqLinOsMgmt_ObjectIdentity((1,3,6,1,4,1,232,23))
_CpqLinOsMibRev_ObjectIdentity=ObjectIdentity
cpqLinOsMibRev=_CpqLinOsMibRev_ObjectIdentity((1,3,6,1,4,1,232,23,1))
class _CpqLinOsMibRevMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CpqLinOsMibRevMajor_Type.__name__=_C
_CpqLinOsMibRevMajor_Object=MibScalar
cpqLinOsMibRevMajor=_CpqLinOsMibRevMajor_Object((1,3,6,1,4,1,232,23,1,1),_CpqLinOsMibRevMajor_Type())
cpqLinOsMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsMibRevMajor.setStatus(_A)
class _CpqLinOsMibRevMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqLinOsMibRevMinor_Type.__name__=_C
_CpqLinOsMibRevMinor_Object=MibScalar
cpqLinOsMibRevMinor=_CpqLinOsMibRevMinor_Object((1,3,6,1,4,1,232,23,1,2),_CpqLinOsMibRevMinor_Type())
cpqLinOsMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsMibRevMinor.setStatus(_A)
class _CpqLinOsMibCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('ok',2),('degraded',3),('failed',4)))
_CpqLinOsMibCondition_Type.__name__=_C
_CpqLinOsMibCondition_Object=MibScalar
cpqLinOsMibCondition=_CpqLinOsMibCondition_Object((1,3,6,1,4,1,232,23,1,3),_CpqLinOsMibCondition_Type())
cpqLinOsMibCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsMibCondition.setStatus(_A)
_CpqLinOsComponent_ObjectIdentity=ObjectIdentity
cpqLinOsComponent=_CpqLinOsComponent_ObjectIdentity((1,3,6,1,4,1,232,23,2))
_CpqLinOsInterface_ObjectIdentity=ObjectIdentity
cpqLinOsInterface=_CpqLinOsInterface_ObjectIdentity((1,3,6,1,4,1,232,23,2,1))
_CpqLinOsCommon_ObjectIdentity=ObjectIdentity
cpqLinOsCommon=_CpqLinOsCommon_ObjectIdentity((1,3,6,1,4,1,232,23,2,1,4))
class _CpqLinOsCommonPollFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CpqLinOsCommonPollFreq_Type.__name__=_C
_CpqLinOsCommonPollFreq_Object=MibScalar
cpqLinOsCommonPollFreq=_CpqLinOsCommonPollFreq_Object((1,3,6,1,4,1,232,23,2,1,4,1),_CpqLinOsCommonPollFreq_Type())
cpqLinOsCommonPollFreq.setMaxAccess('read-write')
if mibBuilder.loadTexts:cpqLinOsCommonPollFreq.setStatus(_A)
_CpqLinOsCommonLastObservedPollCycle_Type=Integer32
_CpqLinOsCommonLastObservedPollCycle_Object=MibScalar
cpqLinOsCommonLastObservedPollCycle=_CpqLinOsCommonLastObservedPollCycle_Object((1,3,6,1,4,1,232,23,2,1,4,2),_CpqLinOsCommonLastObservedPollCycle_Type())
cpqLinOsCommonLastObservedPollCycle.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsCommonLastObservedPollCycle.setStatus(_A)
_CpqLinOsCommonLastObservedTimeSec_Type=Integer32
_CpqLinOsCommonLastObservedTimeSec_Object=MibScalar
cpqLinOsCommonLastObservedTimeSec=_CpqLinOsCommonLastObservedTimeSec_Object((1,3,6,1,4,1,232,23,2,1,4,3),_CpqLinOsCommonLastObservedTimeSec_Type())
cpqLinOsCommonLastObservedTimeSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsCommonLastObservedTimeSec.setStatus(_A)
_CpqLinOsCommonLastObservedTimeMSec_Type=Integer32
_CpqLinOsCommonLastObservedTimeMSec_Object=MibScalar
cpqLinOsCommonLastObservedTimeMSec=_CpqLinOsCommonLastObservedTimeMSec_Object((1,3,6,1,4,1,232,23,2,1,4,4),_CpqLinOsCommonLastObservedTimeMSec_Type())
cpqLinOsCommonLastObservedTimeMSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsCommonLastObservedTimeMSec.setStatus(_A)
_CpqLinOsSystem_ObjectIdentity=ObjectIdentity
cpqLinOsSystem=_CpqLinOsSystem_ObjectIdentity((1,3,6,1,4,1,232,23,2,2))
class _CpqLinOsSystemUpTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqLinOsSystemUpTime_Type.__name__=_D
_CpqLinOsSystemUpTime_Object=MibScalar
cpqLinOsSystemUpTime=_CpqLinOsSystemUpTime_Object((1,3,6,1,4,1,232,23,2,2,2),_CpqLinOsSystemUpTime_Type())
cpqLinOsSystemUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsSystemUpTime.setStatus(_A)
_CpqLinOsSysContextSwitchesPersec_Type=Integer32
_CpqLinOsSysContextSwitchesPersec_Object=MibScalar
cpqLinOsSysContextSwitchesPersec=_CpqLinOsSysContextSwitchesPersec_Object((1,3,6,1,4,1,232,23,2,2,4),_CpqLinOsSysContextSwitchesPersec_Type())
cpqLinOsSysContextSwitchesPersec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsSysContextSwitchesPersec.setStatus(_A)
_CpqLinOsSysProcesses_Type=Integer32
_CpqLinOsSysProcesses_Object=MibScalar
cpqLinOsSysProcesses=_CpqLinOsSysProcesses_Object((1,3,6,1,4,1,232,23,2,2,6),_CpqLinOsSysProcesses_Type())
cpqLinOsSysProcesses.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsSysProcesses.setStatus(_A)
_CpqLinOsProcessor_ObjectIdentity=ObjectIdentity
cpqLinOsProcessor=_CpqLinOsProcessor_ObjectIdentity((1,3,6,1,4,1,232,23,2,3))
_CpqLinOsProcessorTable_Object=MibTable
cpqLinOsProcessorTable=_CpqLinOsProcessorTable_Object((1,3,6,1,4,1,232,23,2,3,2))
if mibBuilder.loadTexts:cpqLinOsProcessorTable.setStatus(_A)
_CpqLinOsProcessorEntry_Object=MibTableRow
cpqLinOsProcessorEntry=_CpqLinOsProcessorEntry_Object((1,3,6,1,4,1,232,23,2,3,2,1))
cpqLinOsProcessorEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:cpqLinOsProcessorEntry.setStatus(_A)
_CpqLinOsCpuIndex_Type=Integer32
_CpqLinOsCpuIndex_Object=MibTableColumn
cpqLinOsCpuIndex=_CpqLinOsCpuIndex_Object((1,3,6,1,4,1,232,23,2,3,2,1,1),_CpqLinOsCpuIndex_Type())
cpqLinOsCpuIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsCpuIndex.setStatus(_A)
class _CpqLinOsCpuInstance_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqLinOsCpuInstance_Type.__name__=_D
_CpqLinOsCpuInstance_Object=MibTableColumn
cpqLinOsCpuInstance=_CpqLinOsCpuInstance_Object((1,3,6,1,4,1,232,23,2,3,2,1,2),_CpqLinOsCpuInstance_Type())
cpqLinOsCpuInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsCpuInstance.setStatus(_A)
_CpqLinOsCpuInterruptsPerSec_Type=Integer32
_CpqLinOsCpuInterruptsPerSec_Object=MibTableColumn
cpqLinOsCpuInterruptsPerSec=_CpqLinOsCpuInterruptsPerSec_Object((1,3,6,1,4,1,232,23,2,3,2,1,3),_CpqLinOsCpuInterruptsPerSec_Type())
cpqLinOsCpuInterruptsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsCpuInterruptsPerSec.setStatus(_A)
_CpqLinOsCpuTimePercent_Type=Integer32
_CpqLinOsCpuTimePercent_Object=MibTableColumn
cpqLinOsCpuTimePercent=_CpqLinOsCpuTimePercent_Object((1,3,6,1,4,1,232,23,2,3,2,1,4),_CpqLinOsCpuTimePercent_Type())
cpqLinOsCpuTimePercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsCpuTimePercent.setStatus(_A)
_CpqLinOsCpuUserTimePercent_Type=Integer32
_CpqLinOsCpuUserTimePercent_Object=MibTableColumn
cpqLinOsCpuUserTimePercent=_CpqLinOsCpuUserTimePercent_Object((1,3,6,1,4,1,232,23,2,3,2,1,7),_CpqLinOsCpuUserTimePercent_Type())
cpqLinOsCpuUserTimePercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsCpuUserTimePercent.setStatus(_A)
_CpqLinOsCpuPrivilegedTimePercent_Type=Integer32
_CpqLinOsCpuPrivilegedTimePercent_Object=MibTableColumn
cpqLinOsCpuPrivilegedTimePercent=_CpqLinOsCpuPrivilegedTimePercent_Object((1,3,6,1,4,1,232,23,2,3,2,1,8),_CpqLinOsCpuPrivilegedTimePercent_Type())
cpqLinOsCpuPrivilegedTimePercent.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsCpuPrivilegedTimePercent.setStatus(_A)
_CpqLinOsMemory_ObjectIdentity=ObjectIdentity
cpqLinOsMemory=_CpqLinOsMemory_ObjectIdentity((1,3,6,1,4,1,232,23,2,4))
_CpqLinOsMemTotal_Type=Integer32
_CpqLinOsMemTotal_Object=MibScalar
cpqLinOsMemTotal=_CpqLinOsMemTotal_Object((1,3,6,1,4,1,232,23,2,4,2),_CpqLinOsMemTotal_Type())
cpqLinOsMemTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsMemTotal.setStatus(_A)
_CpqLinOsMemFree_Type=Integer32
_CpqLinOsMemFree_Object=MibScalar
cpqLinOsMemFree=_CpqLinOsMemFree_Object((1,3,6,1,4,1,232,23,2,4,3),_CpqLinOsMemFree_Type())
cpqLinOsMemFree.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsMemFree.setStatus(_A)
_CpqLinOsMemHighTotal_Type=Integer32
_CpqLinOsMemHighTotal_Object=MibScalar
cpqLinOsMemHighTotal=_CpqLinOsMemHighTotal_Object((1,3,6,1,4,1,232,23,2,4,4),_CpqLinOsMemHighTotal_Type())
cpqLinOsMemHighTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsMemHighTotal.setStatus(_A)
_CpqLinOsMemHighFree_Type=Integer32
_CpqLinOsMemHighFree_Object=MibScalar
cpqLinOsMemHighFree=_CpqLinOsMemHighFree_Object((1,3,6,1,4,1,232,23,2,4,5),_CpqLinOsMemHighFree_Type())
cpqLinOsMemHighFree.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsMemHighFree.setStatus(_A)
_CpqLinOsMemLowTotal_Type=Integer32
_CpqLinOsMemLowTotal_Object=MibScalar
cpqLinOsMemLowTotal=_CpqLinOsMemLowTotal_Object((1,3,6,1,4,1,232,23,2,4,6),_CpqLinOsMemLowTotal_Type())
cpqLinOsMemLowTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsMemLowTotal.setStatus(_A)
_CpqLinOsMemLowFree_Type=Integer32
_CpqLinOsMemLowFree_Object=MibScalar
cpqLinOsMemLowFree=_CpqLinOsMemLowFree_Object((1,3,6,1,4,1,232,23,2,4,7),_CpqLinOsMemLowFree_Type())
cpqLinOsMemLowFree.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsMemLowFree.setStatus(_A)
_CpqLinOsMemSwapTotal_Type=Integer32
_CpqLinOsMemSwapTotal_Object=MibScalar
cpqLinOsMemSwapTotal=_CpqLinOsMemSwapTotal_Object((1,3,6,1,4,1,232,23,2,4,8),_CpqLinOsMemSwapTotal_Type())
cpqLinOsMemSwapTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsMemSwapTotal.setStatus(_A)
_CpqLinOsMemSwapFree_Type=Integer32
_CpqLinOsMemSwapFree_Object=MibScalar
cpqLinOsMemSwapFree=_CpqLinOsMemSwapFree_Object((1,3,6,1,4,1,232,23,2,4,9),_CpqLinOsMemSwapFree_Type())
cpqLinOsMemSwapFree.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsMemSwapFree.setStatus(_A)
_CpqLinOsMemCached_Type=Integer32
_CpqLinOsMemCached_Object=MibScalar
cpqLinOsMemCached=_CpqLinOsMemCached_Object((1,3,6,1,4,1,232,23,2,4,10),_CpqLinOsMemCached_Type())
cpqLinOsMemCached.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsMemCached.setStatus(_A)
_CpqLinOsMemSwapCached_Type=Integer32
_CpqLinOsMemSwapCached_Object=MibScalar
cpqLinOsMemSwapCached=_CpqLinOsMemSwapCached_Object((1,3,6,1,4,1,232,23,2,4,11),_CpqLinOsMemSwapCached_Type())
cpqLinOsMemSwapCached.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsMemSwapCached.setStatus(_A)
_CpqLinOsMemActive_Type=Integer32
_CpqLinOsMemActive_Object=MibScalar
cpqLinOsMemActive=_CpqLinOsMemActive_Object((1,3,6,1,4,1,232,23,2,4,12),_CpqLinOsMemActive_Type())
cpqLinOsMemActive.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsMemActive.setStatus(_A)
_CpqLinOsMemInactiveDirty_Type=Integer32
_CpqLinOsMemInactiveDirty_Object=MibScalar
cpqLinOsMemInactiveDirty=_CpqLinOsMemInactiveDirty_Object((1,3,6,1,4,1,232,23,2,4,13),_CpqLinOsMemInactiveDirty_Type())
cpqLinOsMemInactiveDirty.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsMemInactiveDirty.setStatus(_A)
_CpqLinOsMemInactiveClean_Type=Integer32
_CpqLinOsMemInactiveClean_Object=MibScalar
cpqLinOsMemInactiveClean=_CpqLinOsMemInactiveClean_Object((1,3,6,1,4,1,232,23,2,4,14),_CpqLinOsMemInactiveClean_Type())
cpqLinOsMemInactiveClean.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsMemInactiveClean.setStatus(_A)
_CpqLinOsCache_ObjectIdentity=ObjectIdentity
cpqLinOsCache=_CpqLinOsCache_ObjectIdentity((1,3,6,1,4,1,232,23,2,5))
_CpqLinOsPagingFile_ObjectIdentity=ObjectIdentity
cpqLinOsPagingFile=_CpqLinOsPagingFile_ObjectIdentity((1,3,6,1,4,1,232,23,2,6))
_CpqLinOsSwapInPerSec_Type=Integer32
_CpqLinOsSwapInPerSec_Object=MibScalar
cpqLinOsSwapInPerSec=_CpqLinOsSwapInPerSec_Object((1,3,6,1,4,1,232,23,2,6,2),_CpqLinOsSwapInPerSec_Type())
cpqLinOsSwapInPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsSwapInPerSec.setStatus(_A)
_CpqLinOsSwapOutPerSec_Type=Integer32
_CpqLinOsSwapOutPerSec_Object=MibScalar
cpqLinOsSwapOutPerSec=_CpqLinOsSwapOutPerSec_Object((1,3,6,1,4,1,232,23,2,6,3),_CpqLinOsSwapOutPerSec_Type())
cpqLinOsSwapOutPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsSwapOutPerSec.setStatus(_A)
_CpqLinOsPageSwapInPerSec_Type=Integer32
_CpqLinOsPageSwapInPerSec_Object=MibScalar
cpqLinOsPageSwapInPerSec=_CpqLinOsPageSwapInPerSec_Object((1,3,6,1,4,1,232,23,2,6,4),_CpqLinOsPageSwapInPerSec_Type())
cpqLinOsPageSwapInPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsPageSwapInPerSec.setStatus(_A)
_CpqLinOsPageSwapOutPerSec_Type=Integer32
_CpqLinOsPageSwapOutPerSec_Object=MibScalar
cpqLinOsPageSwapOutPerSec=_CpqLinOsPageSwapOutPerSec_Object((1,3,6,1,4,1,232,23,2,6,5),_CpqLinOsPageSwapOutPerSec_Type())
cpqLinOsPageSwapOutPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsPageSwapOutPerSec.setStatus(_A)
_CpqLinOsMinFltPerSec_Type=Integer32
_CpqLinOsMinFltPerSec_Object=MibScalar
cpqLinOsMinFltPerSec=_CpqLinOsMinFltPerSec_Object((1,3,6,1,4,1,232,23,2,6,6),_CpqLinOsMinFltPerSec_Type())
cpqLinOsMinFltPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsMinFltPerSec.setStatus(_A)
_CpqLinOsMajFltPerSec_Type=Integer32
_CpqLinOsMajFltPerSec_Object=MibScalar
cpqLinOsMajFltPerSec=_CpqLinOsMajFltPerSec_Object((1,3,6,1,4,1,232,23,2,6,7),_CpqLinOsMajFltPerSec_Type())
cpqLinOsMajFltPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsMajFltPerSec.setStatus(_A)
_CpqLinOsDisk_ObjectIdentity=ObjectIdentity
cpqLinOsDisk=_CpqLinOsDisk_ObjectIdentity((1,3,6,1,4,1,232,23,2,7))
_CpqLinOsDiskTable_Object=MibTable
cpqLinOsDiskTable=_CpqLinOsDiskTable_Object((1,3,6,1,4,1,232,23,2,7,2))
if mibBuilder.loadTexts:cpqLinOsDiskTable.setStatus(_A)
_CpqLinOsDiskEntry_Object=MibTableRow
cpqLinOsDiskEntry=_CpqLinOsDiskEntry_Object((1,3,6,1,4,1,232,23,2,7,2,1))
cpqLinOsDiskEntry.setIndexNames((0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:cpqLinOsDiskEntry.setStatus(_A)
_CpqLinOsDiskMajorIndex_Type=Integer32
_CpqLinOsDiskMajorIndex_Object=MibTableColumn
cpqLinOsDiskMajorIndex=_CpqLinOsDiskMajorIndex_Object((1,3,6,1,4,1,232,23,2,7,2,1,1),_CpqLinOsDiskMajorIndex_Type())
cpqLinOsDiskMajorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsDiskMajorIndex.setStatus(_A)
_CpqLinOsDiskMinorIndex_Type=Integer32
_CpqLinOsDiskMinorIndex_Object=MibTableColumn
cpqLinOsDiskMinorIndex=_CpqLinOsDiskMinorIndex_Object((1,3,6,1,4,1,232,23,2,7,2,1,2),_CpqLinOsDiskMinorIndex_Type())
cpqLinOsDiskMinorIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsDiskMinorIndex.setStatus(_A)
class _CpqLinOsDiskName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqLinOsDiskName_Type.__name__=_D
_CpqLinOsDiskName_Object=MibTableColumn
cpqLinOsDiskName=_CpqLinOsDiskName_Object((1,3,6,1,4,1,232,23,2,7,2,1,3),_CpqLinOsDiskName_Type())
cpqLinOsDiskName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsDiskName.setStatus(_A)
_CpqLinOsDiskScsiIndex_Type=Integer32
_CpqLinOsDiskScsiIndex_Object=MibTableColumn
cpqLinOsDiskScsiIndex=_CpqLinOsDiskScsiIndex_Object((1,3,6,1,4,1,232,23,2,7,2,1,4),_CpqLinOsDiskScsiIndex_Type())
cpqLinOsDiskScsiIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsDiskScsiIndex.setStatus(_A)
_CpqLinOsDiskWriteIos_Type=Integer32
_CpqLinOsDiskWriteIos_Object=MibTableColumn
cpqLinOsDiskWriteIos=_CpqLinOsDiskWriteIos_Object((1,3,6,1,4,1,232,23,2,7,2,1,5),_CpqLinOsDiskWriteIos_Type())
cpqLinOsDiskWriteIos.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsDiskWriteIos.setStatus(_A)
_CpqLinOsDiskWriteMerges_Type=Integer32
_CpqLinOsDiskWriteMerges_Object=MibTableColumn
cpqLinOsDiskWriteMerges=_CpqLinOsDiskWriteMerges_Object((1,3,6,1,4,1,232,23,2,7,2,1,6),_CpqLinOsDiskWriteMerges_Type())
cpqLinOsDiskWriteMerges.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsDiskWriteMerges.setStatus(_A)
_CpqLinOsDiskWriteSectors_Type=Integer32
_CpqLinOsDiskWriteSectors_Object=MibTableColumn
cpqLinOsDiskWriteSectors=_CpqLinOsDiskWriteSectors_Object((1,3,6,1,4,1,232,23,2,7,2,1,7),_CpqLinOsDiskWriteSectors_Type())
cpqLinOsDiskWriteSectors.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsDiskWriteSectors.setStatus(_A)
_CpqLinOsDiskWriteDurationMs_Type=Integer32
_CpqLinOsDiskWriteDurationMs_Object=MibTableColumn
cpqLinOsDiskWriteDurationMs=_CpqLinOsDiskWriteDurationMs_Object((1,3,6,1,4,1,232,23,2,7,2,1,8),_CpqLinOsDiskWriteDurationMs_Type())
cpqLinOsDiskWriteDurationMs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsDiskWriteDurationMs.setStatus(_A)
_CpqLinOsDiskWriteIosPerSec_Type=Integer32
_CpqLinOsDiskWriteIosPerSec_Object=MibTableColumn
cpqLinOsDiskWriteIosPerSec=_CpqLinOsDiskWriteIosPerSec_Object((1,3,6,1,4,1,232,23,2,7,2,1,9),_CpqLinOsDiskWriteIosPerSec_Type())
cpqLinOsDiskWriteIosPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsDiskWriteIosPerSec.setStatus(_A)
_CpqLinOsDiskWriteSectorsPerSec_Type=Integer32
_CpqLinOsDiskWriteSectorsPerSec_Object=MibTableColumn
cpqLinOsDiskWriteSectorsPerSec=_CpqLinOsDiskWriteSectorsPerSec_Object((1,3,6,1,4,1,232,23,2,7,2,1,10),_CpqLinOsDiskWriteSectorsPerSec_Type())
cpqLinOsDiskWriteSectorsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsDiskWriteSectorsPerSec.setStatus(_A)
_CpqLinOsDiskWriteDurationMsPerIos_Type=Integer32
_CpqLinOsDiskWriteDurationMsPerIos_Object=MibTableColumn
cpqLinOsDiskWriteDurationMsPerIos=_CpqLinOsDiskWriteDurationMsPerIos_Object((1,3,6,1,4,1,232,23,2,7,2,1,11),_CpqLinOsDiskWriteDurationMsPerIos_Type())
cpqLinOsDiskWriteDurationMsPerIos.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsDiskWriteDurationMsPerIos.setStatus(_A)
_CpqLinOsDiskReadIos_Type=Integer32
_CpqLinOsDiskReadIos_Object=MibTableColumn
cpqLinOsDiskReadIos=_CpqLinOsDiskReadIos_Object((1,3,6,1,4,1,232,23,2,7,2,1,12),_CpqLinOsDiskReadIos_Type())
cpqLinOsDiskReadIos.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsDiskReadIos.setStatus(_A)
_CpqLinOsDiskReadMerges_Type=Integer32
_CpqLinOsDiskReadMerges_Object=MibTableColumn
cpqLinOsDiskReadMerges=_CpqLinOsDiskReadMerges_Object((1,3,6,1,4,1,232,23,2,7,2,1,13),_CpqLinOsDiskReadMerges_Type())
cpqLinOsDiskReadMerges.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsDiskReadMerges.setStatus(_A)
_CpqLinOsDiskReadSectors_Type=Integer32
_CpqLinOsDiskReadSectors_Object=MibTableColumn
cpqLinOsDiskReadSectors=_CpqLinOsDiskReadSectors_Object((1,3,6,1,4,1,232,23,2,7,2,1,14),_CpqLinOsDiskReadSectors_Type())
cpqLinOsDiskReadSectors.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsDiskReadSectors.setStatus(_A)
_CpqLinOsDiskReadDurationMs_Type=Integer32
_CpqLinOsDiskReadDurationMs_Object=MibTableColumn
cpqLinOsDiskReadDurationMs=_CpqLinOsDiskReadDurationMs_Object((1,3,6,1,4,1,232,23,2,7,2,1,15),_CpqLinOsDiskReadDurationMs_Type())
cpqLinOsDiskReadDurationMs.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsDiskReadDurationMs.setStatus(_A)
_CpqLinOsDiskReadIosPerSec_Type=Integer32
_CpqLinOsDiskReadIosPerSec_Object=MibTableColumn
cpqLinOsDiskReadIosPerSec=_CpqLinOsDiskReadIosPerSec_Object((1,3,6,1,4,1,232,23,2,7,2,1,16),_CpqLinOsDiskReadIosPerSec_Type())
cpqLinOsDiskReadIosPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsDiskReadIosPerSec.setStatus(_A)
_CpqLinOsDiskReadSectorsPerSec_Type=Integer32
_CpqLinOsDiskReadSectorsPerSec_Object=MibTableColumn
cpqLinOsDiskReadSectorsPerSec=_CpqLinOsDiskReadSectorsPerSec_Object((1,3,6,1,4,1,232,23,2,7,2,1,17),_CpqLinOsDiskReadSectorsPerSec_Type())
cpqLinOsDiskReadSectorsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsDiskReadSectorsPerSec.setStatus(_A)
_CpqLinOsDiskReadDurationMsPerIos_Type=Integer32
_CpqLinOsDiskReadDurationMsPerIos_Object=MibTableColumn
cpqLinOsDiskReadDurationMsPerIos=_CpqLinOsDiskReadDurationMsPerIos_Object((1,3,6,1,4,1,232,23,2,7,2,1,18),_CpqLinOsDiskReadDurationMsPerIos_Type())
cpqLinOsDiskReadDurationMsPerIos.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsDiskReadDurationMsPerIos.setStatus(_A)
_CpqLinOsNetworkInterface_ObjectIdentity=ObjectIdentity
cpqLinOsNetworkInterface=_CpqLinOsNetworkInterface_ObjectIdentity((1,3,6,1,4,1,232,23,2,10))
_CpqLinOsNetworkInterfaceTable_Object=MibTable
cpqLinOsNetworkInterfaceTable=_CpqLinOsNetworkInterfaceTable_Object((1,3,6,1,4,1,232,23,2,10,2))
if mibBuilder.loadTexts:cpqLinOsNetworkInterfaceTable.setStatus(_A)
_CpqLinOsNetworkInterfaceEntry_Object=MibTableRow
cpqLinOsNetworkInterfaceEntry=_CpqLinOsNetworkInterfaceEntry_Object((1,3,6,1,4,1,232,23,2,10,2,1))
cpqLinOsNetworkInterfaceEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:cpqLinOsNetworkInterfaceEntry.setStatus(_A)
_CpqLinOsNetworkInterfaceIndex_Type=Integer32
_CpqLinOsNetworkInterfaceIndex_Object=MibTableColumn
cpqLinOsNetworkInterfaceIndex=_CpqLinOsNetworkInterfaceIndex_Object((1,3,6,1,4,1,232,23,2,10,2,1,1),_CpqLinOsNetworkInterfaceIndex_Type())
cpqLinOsNetworkInterfaceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsNetworkInterfaceIndex.setStatus(_A)
class _CpqLinOsNetworkInterfaceName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CpqLinOsNetworkInterfaceName_Type.__name__=_D
_CpqLinOsNetworkInterfaceName_Object=MibTableColumn
cpqLinOsNetworkInterfaceName=_CpqLinOsNetworkInterfaceName_Object((1,3,6,1,4,1,232,23,2,10,2,1,2),_CpqLinOsNetworkInterfaceName_Type())
cpqLinOsNetworkInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsNetworkInterfaceName.setStatus(_A)
_CpqLinOsNetworkInterfaceTxBytes_Type=Integer32
_CpqLinOsNetworkInterfaceTxBytes_Object=MibTableColumn
cpqLinOsNetworkInterfaceTxBytes=_CpqLinOsNetworkInterfaceTxBytes_Object((1,3,6,1,4,1,232,23,2,10,2,1,3),_CpqLinOsNetworkInterfaceTxBytes_Type())
cpqLinOsNetworkInterfaceTxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsNetworkInterfaceTxBytes.setStatus(_A)
_CpqLinOsNetworkInterfaceTxPackets_Type=Integer32
_CpqLinOsNetworkInterfaceTxPackets_Object=MibTableColumn
cpqLinOsNetworkInterfaceTxPackets=_CpqLinOsNetworkInterfaceTxPackets_Object((1,3,6,1,4,1,232,23,2,10,2,1,4),_CpqLinOsNetworkInterfaceTxPackets_Type())
cpqLinOsNetworkInterfaceTxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsNetworkInterfaceTxPackets.setStatus(_A)
_CpqLinOsNetworkInterfaceTxBytesPerSec_Type=Integer32
_CpqLinOsNetworkInterfaceTxBytesPerSec_Object=MibTableColumn
cpqLinOsNetworkInterfaceTxBytesPerSec=_CpqLinOsNetworkInterfaceTxBytesPerSec_Object((1,3,6,1,4,1,232,23,2,10,2,1,5),_CpqLinOsNetworkInterfaceTxBytesPerSec_Type())
cpqLinOsNetworkInterfaceTxBytesPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsNetworkInterfaceTxBytesPerSec.setStatus(_A)
_CpqLinOsNetworkInterfaceTxPacketsPerSec_Type=Integer32
_CpqLinOsNetworkInterfaceTxPacketsPerSec_Object=MibTableColumn
cpqLinOsNetworkInterfaceTxPacketsPerSec=_CpqLinOsNetworkInterfaceTxPacketsPerSec_Object((1,3,6,1,4,1,232,23,2,10,2,1,6),_CpqLinOsNetworkInterfaceTxPacketsPerSec_Type())
cpqLinOsNetworkInterfaceTxPacketsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsNetworkInterfaceTxPacketsPerSec.setStatus(_A)
_CpqLinOsNetworkInterfaceRxBytes_Type=Integer32
_CpqLinOsNetworkInterfaceRxBytes_Object=MibTableColumn
cpqLinOsNetworkInterfaceRxBytes=_CpqLinOsNetworkInterfaceRxBytes_Object((1,3,6,1,4,1,232,23,2,10,2,1,7),_CpqLinOsNetworkInterfaceRxBytes_Type())
cpqLinOsNetworkInterfaceRxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsNetworkInterfaceRxBytes.setStatus(_A)
_CpqLinOsNetworkInterfaceRxPackets_Type=Integer32
_CpqLinOsNetworkInterfaceRxPackets_Object=MibTableColumn
cpqLinOsNetworkInterfaceRxPackets=_CpqLinOsNetworkInterfaceRxPackets_Object((1,3,6,1,4,1,232,23,2,10,2,1,8),_CpqLinOsNetworkInterfaceRxPackets_Type())
cpqLinOsNetworkInterfaceRxPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsNetworkInterfaceRxPackets.setStatus(_A)
_CpqLinOsNetworkInterfaceRxBytesPerSec_Type=Integer32
_CpqLinOsNetworkInterfaceRxBytesPerSec_Object=MibTableColumn
cpqLinOsNetworkInterfaceRxBytesPerSec=_CpqLinOsNetworkInterfaceRxBytesPerSec_Object((1,3,6,1,4,1,232,23,2,10,2,1,9),_CpqLinOsNetworkInterfaceRxBytesPerSec_Type())
cpqLinOsNetworkInterfaceRxBytesPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsNetworkInterfaceRxBytesPerSec.setStatus(_A)
_CpqLinOsNetworkInterfaceRxPacketsPerSec_Type=Integer32
_CpqLinOsNetworkInterfaceRxPacketsPerSec_Object=MibTableColumn
cpqLinOsNetworkInterfaceRxPacketsPerSec=_CpqLinOsNetworkInterfaceRxPacketsPerSec_Object((1,3,6,1,4,1,232,23,2,10,2,1,10),_CpqLinOsNetworkInterfaceRxPacketsPerSec_Type())
cpqLinOsNetworkInterfaceRxPacketsPerSec.setMaxAccess(_B)
if mibBuilder.loadTexts:cpqLinOsNetworkInterfaceRxPacketsPerSec.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'cpqLinOsMgmt':cpqLinOsMgmt,'cpqLinOsMibRev':cpqLinOsMibRev,'cpqLinOsMibRevMajor':cpqLinOsMibRevMajor,'cpqLinOsMibRevMinor':cpqLinOsMibRevMinor,'cpqLinOsMibCondition':cpqLinOsMibCondition,'cpqLinOsComponent':cpqLinOsComponent,'cpqLinOsInterface':cpqLinOsInterface,'cpqLinOsCommon':cpqLinOsCommon,'cpqLinOsCommonPollFreq':cpqLinOsCommonPollFreq,'cpqLinOsCommonLastObservedPollCycle':cpqLinOsCommonLastObservedPollCycle,'cpqLinOsCommonLastObservedTimeSec':cpqLinOsCommonLastObservedTimeSec,'cpqLinOsCommonLastObservedTimeMSec':cpqLinOsCommonLastObservedTimeMSec,'cpqLinOsSystem':cpqLinOsSystem,'cpqLinOsSystemUpTime':cpqLinOsSystemUpTime,'cpqLinOsSysContextSwitchesPersec':cpqLinOsSysContextSwitchesPersec,'cpqLinOsSysProcesses':cpqLinOsSysProcesses,'cpqLinOsProcessor':cpqLinOsProcessor,'cpqLinOsProcessorTable':cpqLinOsProcessorTable,'cpqLinOsProcessorEntry':cpqLinOsProcessorEntry,_G:cpqLinOsCpuIndex,'cpqLinOsCpuInstance':cpqLinOsCpuInstance,'cpqLinOsCpuInterruptsPerSec':cpqLinOsCpuInterruptsPerSec,'cpqLinOsCpuTimePercent':cpqLinOsCpuTimePercent,'cpqLinOsCpuUserTimePercent':cpqLinOsCpuUserTimePercent,'cpqLinOsCpuPrivilegedTimePercent':cpqLinOsCpuPrivilegedTimePercent,'cpqLinOsMemory':cpqLinOsMemory,'cpqLinOsMemTotal':cpqLinOsMemTotal,'cpqLinOsMemFree':cpqLinOsMemFree,'cpqLinOsMemHighTotal':cpqLinOsMemHighTotal,'cpqLinOsMemHighFree':cpqLinOsMemHighFree,'cpqLinOsMemLowTotal':cpqLinOsMemLowTotal,'cpqLinOsMemLowFree':cpqLinOsMemLowFree,'cpqLinOsMemSwapTotal':cpqLinOsMemSwapTotal,'cpqLinOsMemSwapFree':cpqLinOsMemSwapFree,'cpqLinOsMemCached':cpqLinOsMemCached,'cpqLinOsMemSwapCached':cpqLinOsMemSwapCached,'cpqLinOsMemActive':cpqLinOsMemActive,'cpqLinOsMemInactiveDirty':cpqLinOsMemInactiveDirty,'cpqLinOsMemInactiveClean':cpqLinOsMemInactiveClean,'cpqLinOsCache':cpqLinOsCache,'cpqLinOsPagingFile':cpqLinOsPagingFile,'cpqLinOsSwapInPerSec':cpqLinOsSwapInPerSec,'cpqLinOsSwapOutPerSec':cpqLinOsSwapOutPerSec,'cpqLinOsPageSwapInPerSec':cpqLinOsPageSwapInPerSec,'cpqLinOsPageSwapOutPerSec':cpqLinOsPageSwapOutPerSec,'cpqLinOsMinFltPerSec':cpqLinOsMinFltPerSec,'cpqLinOsMajFltPerSec':cpqLinOsMajFltPerSec,'cpqLinOsDisk':cpqLinOsDisk,'cpqLinOsDiskTable':cpqLinOsDiskTable,'cpqLinOsDiskEntry':cpqLinOsDiskEntry,_H:cpqLinOsDiskMajorIndex,_I:cpqLinOsDiskMinorIndex,'cpqLinOsDiskName':cpqLinOsDiskName,'cpqLinOsDiskScsiIndex':cpqLinOsDiskScsiIndex,'cpqLinOsDiskWriteIos':cpqLinOsDiskWriteIos,'cpqLinOsDiskWriteMerges':cpqLinOsDiskWriteMerges,'cpqLinOsDiskWriteSectors':cpqLinOsDiskWriteSectors,'cpqLinOsDiskWriteDurationMs':cpqLinOsDiskWriteDurationMs,'cpqLinOsDiskWriteIosPerSec':cpqLinOsDiskWriteIosPerSec,'cpqLinOsDiskWriteSectorsPerSec':cpqLinOsDiskWriteSectorsPerSec,'cpqLinOsDiskWriteDurationMsPerIos':cpqLinOsDiskWriteDurationMsPerIos,'cpqLinOsDiskReadIos':cpqLinOsDiskReadIos,'cpqLinOsDiskReadMerges':cpqLinOsDiskReadMerges,'cpqLinOsDiskReadSectors':cpqLinOsDiskReadSectors,'cpqLinOsDiskReadDurationMs':cpqLinOsDiskReadDurationMs,'cpqLinOsDiskReadIosPerSec':cpqLinOsDiskReadIosPerSec,'cpqLinOsDiskReadSectorsPerSec':cpqLinOsDiskReadSectorsPerSec,'cpqLinOsDiskReadDurationMsPerIos':cpqLinOsDiskReadDurationMsPerIos,'cpqLinOsNetworkInterface':cpqLinOsNetworkInterface,'cpqLinOsNetworkInterfaceTable':cpqLinOsNetworkInterfaceTable,'cpqLinOsNetworkInterfaceEntry':cpqLinOsNetworkInterfaceEntry,_J:cpqLinOsNetworkInterfaceIndex,'cpqLinOsNetworkInterfaceName':cpqLinOsNetworkInterfaceName,'cpqLinOsNetworkInterfaceTxBytes':cpqLinOsNetworkInterfaceTxBytes,'cpqLinOsNetworkInterfaceTxPackets':cpqLinOsNetworkInterfaceTxPackets,'cpqLinOsNetworkInterfaceTxBytesPerSec':cpqLinOsNetworkInterfaceTxBytesPerSec,'cpqLinOsNetworkInterfaceTxPacketsPerSec':cpqLinOsNetworkInterfaceTxPacketsPerSec,'cpqLinOsNetworkInterfaceRxBytes':cpqLinOsNetworkInterfaceRxBytes,'cpqLinOsNetworkInterfaceRxPackets':cpqLinOsNetworkInterfaceRxPackets,'cpqLinOsNetworkInterfaceRxBytesPerSec':cpqLinOsNetworkInterfaceRxBytesPerSec,'cpqLinOsNetworkInterfaceRxPacketsPerSec':cpqLinOsNetworkInterfaceRxPacketsPerSec})