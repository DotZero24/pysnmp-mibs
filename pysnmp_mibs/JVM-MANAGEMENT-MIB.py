_BE='jvmJITCompilerTimeStatGroup'
_BD='jvmJITCompilerBasicGroup'
_BC='jvmRuntimeBootCPGroup'
_BB='jvmThreadInstanceBlockGroup'
_BA='jvmThreadInstanceCpuGroup'
_B9='jvmLowMemoryCollectNotifGroup'
_B8='jvmLowMemoryUsageNotifGroup'
_B7='jvmMemPoolCollectMonitoringGroup'
_B6='jvmMemPoolMonitoringGroup'
_B5='jvmOSGroup'
_B4='jvmRuntimeBasicGroup'
_B3='jvmThreadInstanceBasicGroup'
_B2='jvmThreadBasicGroup'
_B1='jvmMemMgrPoolRelationGroup'
_B0='jvmMemPoolCollectUsageGroup'
_A_='jvmMemPoolPeakUsageGroup'
_Az='jvmMemPoolUsageGroup'
_Ay='jvmMemPoolBasicGroup'
_Ax='jvmMemGCGroup'
_Aw='jvmMemManagerGroup'
_Av='jvmMemorySetGroup'
_Au='jvmMemoryNonHeapUsageGroup'
_At='jvmMemoryHeapUsageGroup'
_As='jvmMemoryBasicGroup'
_Ar='jvmClassLoadingSetGroup'
_Aq='jvmClassLoadingBasicGroup'
_Ap='jvmLowMemoryPoolCollectNotif'
_Ao='jvmLowMemoryPoolUsageNotif'
_An='jvmOSProcessorCount'
_Am='jvmOSVersion'
_Al='jvmOSArch'
_Ak='jvmOSName'
_Aj='jvmJITCompilerTimeMs'
_Ai='jvmJITCompilerTimeMonitoring'
_Ah='jvmJITCompilerName'
_Ag='jvmRTBootClassPathItem'
_Af='jvmRTLibraryPathItem'
_Ae='jvmRTClassPathItem'
_Ad='jvmRTInputArgsItem'
_Ac='jvmRTInputArgsCount'
_Ab='jvmRTBootClassPathSupport'
_Aa='jvmRTStartTimeMs'
_AZ='jvmRTUptimeMs'
_AY='jvmRTManagementSpecVersion'
_AX='jvmRTSpecVersion'
_AW='jvmRTSpecVendor'
_AV='jvmRTSpecName'
_AU='jvmRTVMVersion'
_AT='jvmRTVMVendor'
_AS='jvmRTVMName'
_AR='jvmRTName'
_AQ='jvmThreadInstWaitTimeMs'
_AP='jvmThreadInstWaitCount'
_AO='jvmThreadInstBlockTimeMs'
_AN='jvmThreadInstBlockCount'
_AM='jvmThreadInstCpuTimeNs'
_AL='jvmThreadInstLockOwnerPtr'
_AK='jvmThreadInstLockName'
_AJ='jvmThreadInstName'
_AI='jvmThreadInstState'
_AH='jvmThreadInstId'
_AG='jvmThreadPeakCountReset'
_AF='jvmThreadCpuTimeMonitoring'
_AE='jvmThreadContentionMonitoring'
_AD='jvmThreadTotalStartedCount'
_AC='jvmThreadPeakCount'
_AB='jvmThreadDaemonCount'
_AA='jvmThreadCount'
_A9='jvmMemMgrRelPoolName'
_A8='jvmMemMgrRelManagerName'
_A7='jvmMemPoolCollectThreshold'
_A6='jvmMemPoolCollectMaxSize'
_A5='jvmMemPoolCollectCommitted'
_A4='jvmMemPoolPeakMaxSize'
_A3='jvmMemPoolPeakCommitted'
_A2='jvmMemPoolPeakUsed'
_A1='jvmMemPoolMaxSize'
_A0='jvmMemPoolCommitted'
_z='jvmMemPoolInitSize'
_y='jvmMemPoolThreshold'
_x='jvmMemPoolCollectThreshdSupport'
_w='jvmMemPoolThreshdSupport'
_v='jvmMemPoolPeakReset'
_u='jvmMemPoolState'
_t='jvmMemPoolType'
_s='jvmMemGCTimeMs'
_r='jvmMemGCCount'
_q='jvmMemManagerState'
_p='jvmMemManagerName'
_o='jvmMemoryGCCall'
_n='jvmMemoryGCVerboseLevel'
_m='jvmMemoryNonHeapMaxSize'
_l='jvmMemoryNonHeapCommitted'
_k='jvmMemoryNonHeapUsed'
_j='jvmMemoryNonHeapInitSize'
_i='jvmMemoryHeapMaxSize'
_h='jvmMemoryHeapCommitted'
_g='jvmMemoryHeapUsed'
_f='jvmMemoryHeapInitSize'
_e='jvmMemoryPendingFinalCount'
_d='jvmClassesVerboseLevel'
_c='jvmClassesUnloadedCount'
_b='jvmClassesTotalLoadedCount'
_a='jvmClassesLoadedCount'
_Z='jvmRTLibraryPathIndex'
_Y='jvmRTClassPathIndex'
_X='jvmRTBootClassPathIndex'
_W='jvmRTInputArgsIndex'
_V='jvmThreadInstIndex'
_U='JvmTimeMillis64TC'
_T='JvmVerboseLevelTC'
_S='supported'
_R='Integer32'
_Q='jvmMemPoolCollectThreshdCount'
_P='jvmMemPoolCollectUsed'
_O='jvmMemPoolUsed'
_N='jvmMemPoolThreshdCount'
_M='JvmUnsigned64TC'
_L='jvmMemPoolIndex'
_K='unsupported'
_J='255a'
_I='jvmMemPoolName'
_H='jvmMemManagerIndex'
_G='not-accessible'
_F='milliseconds'
_E='read-write'
_D='bytes'
_C='read-only'
_B='JVM-MANAGEMENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_R,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowPointer,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowPointer','TextualConvention')
jvmMgtMIB=ModuleIdentity((1,3,6,1,4,1,42,2,145,3,163,1))
if mibBuilder.loadTexts:jvmMgtMIB.setRevisions(('2004-03-04 18:00',))
class JvmUnsigned64TC(TextualConvention,Counter64):status=_A
class JvmJavaObjectNameTC(TextualConvention,OctetString):status=_A;displayHint=_J;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1023))
class JvmPathElementTC(TextualConvention,OctetString):status=_A;displayHint=_J;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1023))
class JvmArgValueTC(TextualConvention,OctetString):status=_A;displayHint=_J;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1023))
class JvmVerboseLevelTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('silent',1),('verbose',2)))
class JvmImplSupportStateTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_S,2)))
class JvmImplOptFeatureStateTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4)));namedValues=NamedValues(*((_K,1),('enabled',3),('disabled',4)))
class JvmTimeMillis64TC(TextualConvention,Counter64):status=_A
class JvmTimeNanos64TC(TextualConvention,Counter64):status=_A
class JvmPositive32TC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class JvmManagedMemoryTypeTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('nonheap',1),('heap',2)))
class JvmValidityStateTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('invalid',1),('valid',2)))
class JvmThreadStateTC(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('inNative',1),('suspended',2),('newThread',3),('runnable',4),('blocked',5),('terminated',6),('waiting',7),('timedWaiting',8),('other',9)))
class JvmIndex64TC(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_Sun_ObjectIdentity=ObjectIdentity
sun=_Sun_ObjectIdentity((1,3,6,1,4,1,42))
_Jmgt_ObjectIdentity=ObjectIdentity
jmgt=_Jmgt_ObjectIdentity((1,3,6,1,4,1,42,2,145))
_Standard_ObjectIdentity=ObjectIdentity
standard=_Standard_ObjectIdentity((1,3,6,1,4,1,42,2,145,3))
_JvmMgtMIBObjects_ObjectIdentity=ObjectIdentity
jvmMgtMIBObjects=_JvmMgtMIBObjects_ObjectIdentity((1,3,6,1,4,1,42,2,145,3,163,1,1))
_JvmClassLoading_ObjectIdentity=ObjectIdentity
jvmClassLoading=_JvmClassLoading_ObjectIdentity((1,3,6,1,4,1,42,2,145,3,163,1,1,1))
_JvmClassesLoadedCount_Type=Gauge32
_JvmClassesLoadedCount_Object=MibScalar
jvmClassesLoadedCount=_JvmClassesLoadedCount_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,1,1),_JvmClassesLoadedCount_Type())
jvmClassesLoadedCount.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmClassesLoadedCount.setStatus(_A)
_JvmClassesTotalLoadedCount_Type=Counter64
_JvmClassesTotalLoadedCount_Object=MibScalar
jvmClassesTotalLoadedCount=_JvmClassesTotalLoadedCount_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,1,2),_JvmClassesTotalLoadedCount_Type())
jvmClassesTotalLoadedCount.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmClassesTotalLoadedCount.setStatus(_A)
_JvmClassesUnloadedCount_Type=Counter64
_JvmClassesUnloadedCount_Object=MibScalar
jvmClassesUnloadedCount=_JvmClassesUnloadedCount_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,1,3),_JvmClassesUnloadedCount_Type())
jvmClassesUnloadedCount.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmClassesUnloadedCount.setStatus(_A)
class _JvmClassesVerboseLevel_Type(JvmVerboseLevelTC):defaultValue=1
_JvmClassesVerboseLevel_Type.__name__=_T
_JvmClassesVerboseLevel_Object=MibScalar
jvmClassesVerboseLevel=_JvmClassesVerboseLevel_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,1,4),_JvmClassesVerboseLevel_Type())
jvmClassesVerboseLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:jvmClassesVerboseLevel.setStatus(_A)
_JvmMemory_ObjectIdentity=ObjectIdentity
jvmMemory=_JvmMemory_ObjectIdentity((1,3,6,1,4,1,42,2,145,3,163,1,1,2))
_JvmMemoryPendingFinalCount_Type=Gauge32
_JvmMemoryPendingFinalCount_Object=MibScalar
jvmMemoryPendingFinalCount=_JvmMemoryPendingFinalCount_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,1),_JvmMemoryPendingFinalCount_Type())
jvmMemoryPendingFinalCount.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemoryPendingFinalCount.setStatus(_A)
_JvmMemoryGCVerboseLevel_Type=JvmVerboseLevelTC
_JvmMemoryGCVerboseLevel_Object=MibScalar
jvmMemoryGCVerboseLevel=_JvmMemoryGCVerboseLevel_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,2),_JvmMemoryGCVerboseLevel_Type())
jvmMemoryGCVerboseLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:jvmMemoryGCVerboseLevel.setStatus(_A)
class _JvmMemoryGCCall_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_K,1),(_S,2),('start',3),('started',4),('failed',5)))
_JvmMemoryGCCall_Type.__name__=_R
_JvmMemoryGCCall_Object=MibScalar
jvmMemoryGCCall=_JvmMemoryGCCall_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,3),_JvmMemoryGCCall_Type())
jvmMemoryGCCall.setMaxAccess(_E)
if mibBuilder.loadTexts:jvmMemoryGCCall.setStatus(_A)
_JvmMemoryHeapInitSize_Type=JvmUnsigned64TC
_JvmMemoryHeapInitSize_Object=MibScalar
jvmMemoryHeapInitSize=_JvmMemoryHeapInitSize_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,10),_JvmMemoryHeapInitSize_Type())
jvmMemoryHeapInitSize.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemoryHeapInitSize.setStatus(_A)
if mibBuilder.loadTexts:jvmMemoryHeapInitSize.setUnits(_D)
_JvmMemoryHeapUsed_Type=JvmUnsigned64TC
_JvmMemoryHeapUsed_Object=MibScalar
jvmMemoryHeapUsed=_JvmMemoryHeapUsed_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,11),_JvmMemoryHeapUsed_Type())
jvmMemoryHeapUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemoryHeapUsed.setStatus(_A)
if mibBuilder.loadTexts:jvmMemoryHeapUsed.setUnits(_D)
_JvmMemoryHeapCommitted_Type=JvmUnsigned64TC
_JvmMemoryHeapCommitted_Object=MibScalar
jvmMemoryHeapCommitted=_JvmMemoryHeapCommitted_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,12),_JvmMemoryHeapCommitted_Type())
jvmMemoryHeapCommitted.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemoryHeapCommitted.setStatus(_A)
if mibBuilder.loadTexts:jvmMemoryHeapCommitted.setUnits(_D)
_JvmMemoryHeapMaxSize_Type=JvmUnsigned64TC
_JvmMemoryHeapMaxSize_Object=MibScalar
jvmMemoryHeapMaxSize=_JvmMemoryHeapMaxSize_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,13),_JvmMemoryHeapMaxSize_Type())
jvmMemoryHeapMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemoryHeapMaxSize.setStatus(_A)
if mibBuilder.loadTexts:jvmMemoryHeapMaxSize.setUnits(_D)
_JvmMemoryNonHeapInitSize_Type=JvmUnsigned64TC
_JvmMemoryNonHeapInitSize_Object=MibScalar
jvmMemoryNonHeapInitSize=_JvmMemoryNonHeapInitSize_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,20),_JvmMemoryNonHeapInitSize_Type())
jvmMemoryNonHeapInitSize.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemoryNonHeapInitSize.setStatus(_A)
if mibBuilder.loadTexts:jvmMemoryNonHeapInitSize.setUnits(_D)
_JvmMemoryNonHeapUsed_Type=JvmUnsigned64TC
_JvmMemoryNonHeapUsed_Object=MibScalar
jvmMemoryNonHeapUsed=_JvmMemoryNonHeapUsed_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,21),_JvmMemoryNonHeapUsed_Type())
jvmMemoryNonHeapUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemoryNonHeapUsed.setStatus(_A)
if mibBuilder.loadTexts:jvmMemoryNonHeapUsed.setUnits(_D)
_JvmMemoryNonHeapCommitted_Type=JvmUnsigned64TC
_JvmMemoryNonHeapCommitted_Object=MibScalar
jvmMemoryNonHeapCommitted=_JvmMemoryNonHeapCommitted_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,22),_JvmMemoryNonHeapCommitted_Type())
jvmMemoryNonHeapCommitted.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemoryNonHeapCommitted.setStatus(_A)
if mibBuilder.loadTexts:jvmMemoryNonHeapCommitted.setUnits(_D)
_JvmMemoryNonHeapMaxSize_Type=JvmUnsigned64TC
_JvmMemoryNonHeapMaxSize_Object=MibScalar
jvmMemoryNonHeapMaxSize=_JvmMemoryNonHeapMaxSize_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,23),_JvmMemoryNonHeapMaxSize_Type())
jvmMemoryNonHeapMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemoryNonHeapMaxSize.setStatus(_A)
if mibBuilder.loadTexts:jvmMemoryNonHeapMaxSize.setUnits(_D)
_JvmMemManagerTable_Object=MibTable
jvmMemManagerTable=_JvmMemManagerTable_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,100))
if mibBuilder.loadTexts:jvmMemManagerTable.setStatus(_A)
_JvmMemManagerEntry_Object=MibTableRow
jvmMemManagerEntry=_JvmMemManagerEntry_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,100,1))
jvmMemManagerEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:jvmMemManagerEntry.setStatus(_A)
_JvmMemManagerIndex_Type=JvmPositive32TC
_JvmMemManagerIndex_Object=MibTableColumn
jvmMemManagerIndex=_JvmMemManagerIndex_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,100,1,1),_JvmMemManagerIndex_Type())
jvmMemManagerIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:jvmMemManagerIndex.setStatus(_A)
_JvmMemManagerName_Type=JvmJavaObjectNameTC
_JvmMemManagerName_Object=MibTableColumn
jvmMemManagerName=_JvmMemManagerName_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,100,1,2),_JvmMemManagerName_Type())
jvmMemManagerName.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemManagerName.setStatus(_A)
_JvmMemManagerState_Type=JvmValidityStateTC
_JvmMemManagerState_Object=MibTableColumn
jvmMemManagerState=_JvmMemManagerState_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,100,1,3),_JvmMemManagerState_Type())
jvmMemManagerState.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemManagerState.setStatus(_A)
_JvmMemGCTable_Object=MibTable
jvmMemGCTable=_JvmMemGCTable_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,101))
if mibBuilder.loadTexts:jvmMemGCTable.setStatus(_A)
_JvmMemGCEntry_Object=MibTableRow
jvmMemGCEntry=_JvmMemGCEntry_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,101,1))
jvmMemGCEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:jvmMemGCEntry.setStatus(_A)
_JvmMemGCCount_Type=Counter64
_JvmMemGCCount_Object=MibTableColumn
jvmMemGCCount=_JvmMemGCCount_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,101,1,2),_JvmMemGCCount_Type())
jvmMemGCCount.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemGCCount.setStatus(_A)
class _JvmMemGCTimeMs_Type(JvmTimeMillis64TC):defaultValue=0
_JvmMemGCTimeMs_Type.__name__=_U
_JvmMemGCTimeMs_Object=MibTableColumn
jvmMemGCTimeMs=_JvmMemGCTimeMs_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,101,1,3),_JvmMemGCTimeMs_Type())
jvmMemGCTimeMs.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemGCTimeMs.setStatus(_A)
if mibBuilder.loadTexts:jvmMemGCTimeMs.setUnits(_F)
_JvmMemPoolTable_Object=MibTable
jvmMemPoolTable=_JvmMemPoolTable_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,110))
if mibBuilder.loadTexts:jvmMemPoolTable.setStatus(_A)
_JvmMemPoolEntry_Object=MibTableRow
jvmMemPoolEntry=_JvmMemPoolEntry_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,110,1))
jvmMemPoolEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:jvmMemPoolEntry.setStatus(_A)
_JvmMemPoolIndex_Type=JvmPositive32TC
_JvmMemPoolIndex_Object=MibTableColumn
jvmMemPoolIndex=_JvmMemPoolIndex_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,110,1,1),_JvmMemPoolIndex_Type())
jvmMemPoolIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:jvmMemPoolIndex.setStatus(_A)
_JvmMemPoolName_Type=JvmJavaObjectNameTC
_JvmMemPoolName_Object=MibTableColumn
jvmMemPoolName=_JvmMemPoolName_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,110,1,2),_JvmMemPoolName_Type())
jvmMemPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemPoolName.setStatus(_A)
_JvmMemPoolType_Type=JvmManagedMemoryTypeTC
_JvmMemPoolType_Object=MibTableColumn
jvmMemPoolType=_JvmMemPoolType_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,110,1,3),_JvmMemPoolType_Type())
jvmMemPoolType.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemPoolType.setStatus(_A)
_JvmMemPoolState_Type=JvmValidityStateTC
_JvmMemPoolState_Object=MibTableColumn
jvmMemPoolState=_JvmMemPoolState_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,110,1,4),_JvmMemPoolState_Type())
jvmMemPoolState.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemPoolState.setStatus(_A)
_JvmMemPoolPeakReset_Type=JvmTimeMillis64TC
_JvmMemPoolPeakReset_Object=MibTableColumn
jvmMemPoolPeakReset=_JvmMemPoolPeakReset_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,110,1,5),_JvmMemPoolPeakReset_Type())
jvmMemPoolPeakReset.setMaxAccess(_E)
if mibBuilder.loadTexts:jvmMemPoolPeakReset.setStatus(_A)
if mibBuilder.loadTexts:jvmMemPoolPeakReset.setUnits(_F)
_JvmMemPoolInitSize_Type=JvmUnsigned64TC
_JvmMemPoolInitSize_Object=MibTableColumn
jvmMemPoolInitSize=_JvmMemPoolInitSize_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,110,1,10),_JvmMemPoolInitSize_Type())
jvmMemPoolInitSize.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemPoolInitSize.setStatus(_A)
if mibBuilder.loadTexts:jvmMemPoolInitSize.setUnits(_D)
_JvmMemPoolUsed_Type=JvmUnsigned64TC
_JvmMemPoolUsed_Object=MibTableColumn
jvmMemPoolUsed=_JvmMemPoolUsed_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,110,1,11),_JvmMemPoolUsed_Type())
jvmMemPoolUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemPoolUsed.setStatus(_A)
if mibBuilder.loadTexts:jvmMemPoolUsed.setUnits(_D)
_JvmMemPoolCommitted_Type=JvmUnsigned64TC
_JvmMemPoolCommitted_Object=MibTableColumn
jvmMemPoolCommitted=_JvmMemPoolCommitted_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,110,1,12),_JvmMemPoolCommitted_Type())
jvmMemPoolCommitted.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemPoolCommitted.setStatus(_A)
if mibBuilder.loadTexts:jvmMemPoolCommitted.setUnits(_D)
_JvmMemPoolMaxSize_Type=JvmUnsigned64TC
_JvmMemPoolMaxSize_Object=MibTableColumn
jvmMemPoolMaxSize=_JvmMemPoolMaxSize_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,110,1,13),_JvmMemPoolMaxSize_Type())
jvmMemPoolMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemPoolMaxSize.setStatus(_A)
if mibBuilder.loadTexts:jvmMemPoolMaxSize.setUnits(_D)
_JvmMemPoolPeakUsed_Type=JvmUnsigned64TC
_JvmMemPoolPeakUsed_Object=MibTableColumn
jvmMemPoolPeakUsed=_JvmMemPoolPeakUsed_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,110,1,21),_JvmMemPoolPeakUsed_Type())
jvmMemPoolPeakUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemPoolPeakUsed.setStatus(_A)
if mibBuilder.loadTexts:jvmMemPoolPeakUsed.setUnits(_D)
_JvmMemPoolPeakCommitted_Type=JvmUnsigned64TC
_JvmMemPoolPeakCommitted_Object=MibTableColumn
jvmMemPoolPeakCommitted=_JvmMemPoolPeakCommitted_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,110,1,22),_JvmMemPoolPeakCommitted_Type())
jvmMemPoolPeakCommitted.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemPoolPeakCommitted.setStatus(_A)
if mibBuilder.loadTexts:jvmMemPoolPeakCommitted.setUnits(_D)
_JvmMemPoolPeakMaxSize_Type=JvmUnsigned64TC
_JvmMemPoolPeakMaxSize_Object=MibTableColumn
jvmMemPoolPeakMaxSize=_JvmMemPoolPeakMaxSize_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,110,1,23),_JvmMemPoolPeakMaxSize_Type())
jvmMemPoolPeakMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemPoolPeakMaxSize.setStatus(_A)
if mibBuilder.loadTexts:jvmMemPoolPeakMaxSize.setUnits(_D)
_JvmMemPoolCollectUsed_Type=JvmUnsigned64TC
_JvmMemPoolCollectUsed_Object=MibTableColumn
jvmMemPoolCollectUsed=_JvmMemPoolCollectUsed_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,110,1,31),_JvmMemPoolCollectUsed_Type())
jvmMemPoolCollectUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemPoolCollectUsed.setStatus(_A)
if mibBuilder.loadTexts:jvmMemPoolCollectUsed.setUnits(_D)
_JvmMemPoolCollectCommitted_Type=JvmUnsigned64TC
_JvmMemPoolCollectCommitted_Object=MibTableColumn
jvmMemPoolCollectCommitted=_JvmMemPoolCollectCommitted_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,110,1,32),_JvmMemPoolCollectCommitted_Type())
jvmMemPoolCollectCommitted.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemPoolCollectCommitted.setStatus(_A)
if mibBuilder.loadTexts:jvmMemPoolCollectCommitted.setUnits(_D)
_JvmMemPoolCollectMaxSize_Type=JvmUnsigned64TC
_JvmMemPoolCollectMaxSize_Object=MibTableColumn
jvmMemPoolCollectMaxSize=_JvmMemPoolCollectMaxSize_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,110,1,33),_JvmMemPoolCollectMaxSize_Type())
jvmMemPoolCollectMaxSize.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemPoolCollectMaxSize.setStatus(_A)
if mibBuilder.loadTexts:jvmMemPoolCollectMaxSize.setUnits(_D)
class _JvmMemPoolThreshold_Type(JvmUnsigned64TC):defaultValue=0
_JvmMemPoolThreshold_Type.__name__=_M
_JvmMemPoolThreshold_Object=MibTableColumn
jvmMemPoolThreshold=_JvmMemPoolThreshold_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,110,1,110),_JvmMemPoolThreshold_Type())
jvmMemPoolThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:jvmMemPoolThreshold.setStatus(_A)
if mibBuilder.loadTexts:jvmMemPoolThreshold.setUnits(_D)
_JvmMemPoolThreshdCount_Type=Counter64
_JvmMemPoolThreshdCount_Object=MibTableColumn
jvmMemPoolThreshdCount=_JvmMemPoolThreshdCount_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,110,1,111),_JvmMemPoolThreshdCount_Type())
jvmMemPoolThreshdCount.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemPoolThreshdCount.setStatus(_A)
_JvmMemPoolThreshdSupport_Type=JvmImplSupportStateTC
_JvmMemPoolThreshdSupport_Object=MibTableColumn
jvmMemPoolThreshdSupport=_JvmMemPoolThreshdSupport_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,110,1,112),_JvmMemPoolThreshdSupport_Type())
jvmMemPoolThreshdSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemPoolThreshdSupport.setStatus(_A)
class _JvmMemPoolCollectThreshold_Type(JvmUnsigned64TC):defaultValue=0
_JvmMemPoolCollectThreshold_Type.__name__=_M
_JvmMemPoolCollectThreshold_Object=MibTableColumn
jvmMemPoolCollectThreshold=_JvmMemPoolCollectThreshold_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,110,1,131),_JvmMemPoolCollectThreshold_Type())
jvmMemPoolCollectThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:jvmMemPoolCollectThreshold.setStatus(_A)
if mibBuilder.loadTexts:jvmMemPoolCollectThreshold.setUnits(_D)
_JvmMemPoolCollectThreshdCount_Type=Counter64
_JvmMemPoolCollectThreshdCount_Object=MibTableColumn
jvmMemPoolCollectThreshdCount=_JvmMemPoolCollectThreshdCount_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,110,1,132),_JvmMemPoolCollectThreshdCount_Type())
jvmMemPoolCollectThreshdCount.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemPoolCollectThreshdCount.setStatus(_A)
_JvmMemPoolCollectThreshdSupport_Type=JvmImplSupportStateTC
_JvmMemPoolCollectThreshdSupport_Object=MibTableColumn
jvmMemPoolCollectThreshdSupport=_JvmMemPoolCollectThreshdSupport_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,110,1,133),_JvmMemPoolCollectThreshdSupport_Type())
jvmMemPoolCollectThreshdSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemPoolCollectThreshdSupport.setStatus(_A)
_JvmMemMgrPoolRelTable_Object=MibTable
jvmMemMgrPoolRelTable=_JvmMemMgrPoolRelTable_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,120))
if mibBuilder.loadTexts:jvmMemMgrPoolRelTable.setStatus(_A)
_JvmMemMgrPoolRelEntry_Object=MibTableRow
jvmMemMgrPoolRelEntry=_JvmMemMgrPoolRelEntry_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,120,1))
jvmMemMgrPoolRelEntry.setIndexNames((0,_B,_H),(0,_B,_L))
if mibBuilder.loadTexts:jvmMemMgrPoolRelEntry.setStatus(_A)
_JvmMemMgrRelManagerName_Type=JvmJavaObjectNameTC
_JvmMemMgrRelManagerName_Object=MibTableColumn
jvmMemMgrRelManagerName=_JvmMemMgrRelManagerName_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,120,1,2),_JvmMemMgrRelManagerName_Type())
jvmMemMgrRelManagerName.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemMgrRelManagerName.setStatus(_A)
_JvmMemMgrRelPoolName_Type=JvmJavaObjectNameTC
_JvmMemMgrRelPoolName_Object=MibTableColumn
jvmMemMgrRelPoolName=_JvmMemMgrRelPoolName_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,2,120,1,3),_JvmMemMgrRelPoolName_Type())
jvmMemMgrRelPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmMemMgrRelPoolName.setStatus(_A)
_JvmThreading_ObjectIdentity=ObjectIdentity
jvmThreading=_JvmThreading_ObjectIdentity((1,3,6,1,4,1,42,2,145,3,163,1,1,3))
_JvmThreadCount_Type=Gauge32
_JvmThreadCount_Object=MibScalar
jvmThreadCount=_JvmThreadCount_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,3,1),_JvmThreadCount_Type())
jvmThreadCount.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmThreadCount.setStatus(_A)
_JvmThreadDaemonCount_Type=Gauge32
_JvmThreadDaemonCount_Object=MibScalar
jvmThreadDaemonCount=_JvmThreadDaemonCount_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,3,2),_JvmThreadDaemonCount_Type())
jvmThreadDaemonCount.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmThreadDaemonCount.setStatus(_A)
_JvmThreadPeakCount_Type=Counter32
_JvmThreadPeakCount_Object=MibScalar
jvmThreadPeakCount=_JvmThreadPeakCount_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,3,3),_JvmThreadPeakCount_Type())
jvmThreadPeakCount.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmThreadPeakCount.setStatus(_A)
_JvmThreadTotalStartedCount_Type=Counter64
_JvmThreadTotalStartedCount_Object=MibScalar
jvmThreadTotalStartedCount=_JvmThreadTotalStartedCount_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,3,4),_JvmThreadTotalStartedCount_Type())
jvmThreadTotalStartedCount.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmThreadTotalStartedCount.setStatus(_A)
_JvmThreadContentionMonitoring_Type=JvmImplOptFeatureStateTC
_JvmThreadContentionMonitoring_Object=MibScalar
jvmThreadContentionMonitoring=_JvmThreadContentionMonitoring_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,3,5),_JvmThreadContentionMonitoring_Type())
jvmThreadContentionMonitoring.setMaxAccess(_E)
if mibBuilder.loadTexts:jvmThreadContentionMonitoring.setStatus(_A)
_JvmThreadCpuTimeMonitoring_Type=JvmImplOptFeatureStateTC
_JvmThreadCpuTimeMonitoring_Object=MibScalar
jvmThreadCpuTimeMonitoring=_JvmThreadCpuTimeMonitoring_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,3,6),_JvmThreadCpuTimeMonitoring_Type())
jvmThreadCpuTimeMonitoring.setMaxAccess(_E)
if mibBuilder.loadTexts:jvmThreadCpuTimeMonitoring.setStatus(_A)
_JvmThreadPeakCountReset_Type=JvmTimeMillis64TC
_JvmThreadPeakCountReset_Object=MibScalar
jvmThreadPeakCountReset=_JvmThreadPeakCountReset_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,3,7),_JvmThreadPeakCountReset_Type())
jvmThreadPeakCountReset.setMaxAccess(_E)
if mibBuilder.loadTexts:jvmThreadPeakCountReset.setStatus(_A)
if mibBuilder.loadTexts:jvmThreadPeakCountReset.setUnits(_F)
_JvmThreadInstanceTable_Object=MibTable
jvmThreadInstanceTable=_JvmThreadInstanceTable_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,3,10))
if mibBuilder.loadTexts:jvmThreadInstanceTable.setStatus(_A)
_JvmThreadInstanceEntry_Object=MibTableRow
jvmThreadInstanceEntry=_JvmThreadInstanceEntry_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,3,10,1))
jvmThreadInstanceEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:jvmThreadInstanceEntry.setStatus(_A)
_JvmThreadInstIndex_Type=JvmIndex64TC
_JvmThreadInstIndex_Object=MibTableColumn
jvmThreadInstIndex=_JvmThreadInstIndex_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,3,10,1,1),_JvmThreadInstIndex_Type())
jvmThreadInstIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:jvmThreadInstIndex.setStatus(_A)
_JvmThreadInstId_Type=JvmUnsigned64TC
_JvmThreadInstId_Object=MibTableColumn
jvmThreadInstId=_JvmThreadInstId_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,3,10,1,2),_JvmThreadInstId_Type())
jvmThreadInstId.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmThreadInstId.setStatus(_A)
_JvmThreadInstState_Type=JvmThreadStateTC
_JvmThreadInstState_Object=MibTableColumn
jvmThreadInstState=_JvmThreadInstState_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,3,10,1,3),_JvmThreadInstState_Type())
jvmThreadInstState.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmThreadInstState.setStatus(_A)
_JvmThreadInstBlockCount_Type=Counter64
_JvmThreadInstBlockCount_Object=MibTableColumn
jvmThreadInstBlockCount=_JvmThreadInstBlockCount_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,3,10,1,4),_JvmThreadInstBlockCount_Type())
jvmThreadInstBlockCount.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmThreadInstBlockCount.setStatus(_A)
_JvmThreadInstBlockTimeMs_Type=JvmTimeMillis64TC
_JvmThreadInstBlockTimeMs_Object=MibTableColumn
jvmThreadInstBlockTimeMs=_JvmThreadInstBlockTimeMs_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,3,10,1,5),_JvmThreadInstBlockTimeMs_Type())
jvmThreadInstBlockTimeMs.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmThreadInstBlockTimeMs.setStatus(_A)
if mibBuilder.loadTexts:jvmThreadInstBlockTimeMs.setUnits(_F)
_JvmThreadInstWaitCount_Type=Counter64
_JvmThreadInstWaitCount_Object=MibTableColumn
jvmThreadInstWaitCount=_JvmThreadInstWaitCount_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,3,10,1,6),_JvmThreadInstWaitCount_Type())
jvmThreadInstWaitCount.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmThreadInstWaitCount.setStatus(_A)
_JvmThreadInstWaitTimeMs_Type=JvmTimeMillis64TC
_JvmThreadInstWaitTimeMs_Object=MibTableColumn
jvmThreadInstWaitTimeMs=_JvmThreadInstWaitTimeMs_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,3,10,1,7),_JvmThreadInstWaitTimeMs_Type())
jvmThreadInstWaitTimeMs.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmThreadInstWaitTimeMs.setStatus(_A)
if mibBuilder.loadTexts:jvmThreadInstWaitTimeMs.setUnits(_F)
_JvmThreadInstCpuTimeNs_Type=JvmTimeNanos64TC
_JvmThreadInstCpuTimeNs_Object=MibTableColumn
jvmThreadInstCpuTimeNs=_JvmThreadInstCpuTimeNs_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,3,10,1,8),_JvmThreadInstCpuTimeNs_Type())
jvmThreadInstCpuTimeNs.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmThreadInstCpuTimeNs.setStatus(_A)
if mibBuilder.loadTexts:jvmThreadInstCpuTimeNs.setUnits('nanoseconds')
_JvmThreadInstName_Type=JvmJavaObjectNameTC
_JvmThreadInstName_Object=MibTableColumn
jvmThreadInstName=_JvmThreadInstName_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,3,10,1,9),_JvmThreadInstName_Type())
jvmThreadInstName.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmThreadInstName.setStatus(_A)
_JvmThreadInstLockName_Type=JvmJavaObjectNameTC
_JvmThreadInstLockName_Object=MibTableColumn
jvmThreadInstLockName=_JvmThreadInstLockName_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,3,10,1,10),_JvmThreadInstLockName_Type())
jvmThreadInstLockName.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmThreadInstLockName.setStatus(_A)
_JvmThreadInstLockOwnerPtr_Type=RowPointer
_JvmThreadInstLockOwnerPtr_Object=MibTableColumn
jvmThreadInstLockOwnerPtr=_JvmThreadInstLockOwnerPtr_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,3,10,1,11),_JvmThreadInstLockOwnerPtr_Type())
jvmThreadInstLockOwnerPtr.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmThreadInstLockOwnerPtr.setStatus(_A)
_JvmRuntime_ObjectIdentity=ObjectIdentity
jvmRuntime=_JvmRuntime_ObjectIdentity((1,3,6,1,4,1,42,2,145,3,163,1,1,4))
_JvmRTName_Type=DisplayString
_JvmRTName_Object=MibScalar
jvmRTName=_JvmRTName_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,1),_JvmRTName_Type())
jvmRTName.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmRTName.setStatus(_A)
_JvmRTVMName_Type=JvmJavaObjectNameTC
_JvmRTVMName_Object=MibScalar
jvmRTVMName=_JvmRTVMName_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,2),_JvmRTVMName_Type())
jvmRTVMName.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmRTVMName.setStatus(_A)
_JvmRTVMVendor_Type=DisplayString
_JvmRTVMVendor_Object=MibScalar
jvmRTVMVendor=_JvmRTVMVendor_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,3),_JvmRTVMVendor_Type())
jvmRTVMVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmRTVMVendor.setStatus(_A)
_JvmRTVMVersion_Type=DisplayString
_JvmRTVMVersion_Object=MibScalar
jvmRTVMVersion=_JvmRTVMVersion_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,4),_JvmRTVMVersion_Type())
jvmRTVMVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmRTVMVersion.setStatus(_A)
_JvmRTSpecName_Type=DisplayString
_JvmRTSpecName_Object=MibScalar
jvmRTSpecName=_JvmRTSpecName_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,5),_JvmRTSpecName_Type())
jvmRTSpecName.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmRTSpecName.setStatus(_A)
_JvmRTSpecVendor_Type=DisplayString
_JvmRTSpecVendor_Object=MibScalar
jvmRTSpecVendor=_JvmRTSpecVendor_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,6),_JvmRTSpecVendor_Type())
jvmRTSpecVendor.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmRTSpecVendor.setStatus(_A)
_JvmRTSpecVersion_Type=DisplayString
_JvmRTSpecVersion_Object=MibScalar
jvmRTSpecVersion=_JvmRTSpecVersion_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,7),_JvmRTSpecVersion_Type())
jvmRTSpecVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmRTSpecVersion.setStatus(_A)
_JvmRTManagementSpecVersion_Type=DisplayString
_JvmRTManagementSpecVersion_Object=MibScalar
jvmRTManagementSpecVersion=_JvmRTManagementSpecVersion_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,8),_JvmRTManagementSpecVersion_Type())
jvmRTManagementSpecVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmRTManagementSpecVersion.setStatus(_A)
_JvmRTBootClassPathSupport_Type=JvmImplSupportStateTC
_JvmRTBootClassPathSupport_Object=MibScalar
jvmRTBootClassPathSupport=_JvmRTBootClassPathSupport_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,9),_JvmRTBootClassPathSupport_Type())
jvmRTBootClassPathSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmRTBootClassPathSupport.setStatus(_A)
_JvmRTInputArgsCount_Type=JvmPositive32TC
_JvmRTInputArgsCount_Object=MibScalar
jvmRTInputArgsCount=_JvmRTInputArgsCount_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,10),_JvmRTInputArgsCount_Type())
jvmRTInputArgsCount.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmRTInputArgsCount.setStatus(_A)
_JvmRTUptimeMs_Type=JvmTimeMillis64TC
_JvmRTUptimeMs_Object=MibScalar
jvmRTUptimeMs=_JvmRTUptimeMs_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,11),_JvmRTUptimeMs_Type())
jvmRTUptimeMs.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmRTUptimeMs.setStatus(_A)
if mibBuilder.loadTexts:jvmRTUptimeMs.setUnits(_F)
_JvmRTStartTimeMs_Type=JvmTimeMillis64TC
_JvmRTStartTimeMs_Object=MibScalar
jvmRTStartTimeMs=_JvmRTStartTimeMs_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,12),_JvmRTStartTimeMs_Type())
jvmRTStartTimeMs.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmRTStartTimeMs.setStatus(_A)
if mibBuilder.loadTexts:jvmRTStartTimeMs.setUnits(_F)
_JvmRTInputArgsTable_Object=MibTable
jvmRTInputArgsTable=_JvmRTInputArgsTable_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,20))
if mibBuilder.loadTexts:jvmRTInputArgsTable.setStatus(_A)
_JvmRTInputArgsEntry_Object=MibTableRow
jvmRTInputArgsEntry=_JvmRTInputArgsEntry_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,20,1))
jvmRTInputArgsEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:jvmRTInputArgsEntry.setStatus(_A)
_JvmRTInputArgsIndex_Type=JvmPositive32TC
_JvmRTInputArgsIndex_Object=MibTableColumn
jvmRTInputArgsIndex=_JvmRTInputArgsIndex_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,20,1,1),_JvmRTInputArgsIndex_Type())
jvmRTInputArgsIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:jvmRTInputArgsIndex.setStatus(_A)
_JvmRTInputArgsItem_Type=JvmArgValueTC
_JvmRTInputArgsItem_Object=MibTableColumn
jvmRTInputArgsItem=_JvmRTInputArgsItem_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,20,1,2),_JvmRTInputArgsItem_Type())
jvmRTInputArgsItem.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmRTInputArgsItem.setStatus(_A)
_JvmRTBootClassPathTable_Object=MibTable
jvmRTBootClassPathTable=_JvmRTBootClassPathTable_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,21))
if mibBuilder.loadTexts:jvmRTBootClassPathTable.setStatus(_A)
_JvmRTBootClassPathEntry_Object=MibTableRow
jvmRTBootClassPathEntry=_JvmRTBootClassPathEntry_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,21,1))
jvmRTBootClassPathEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:jvmRTBootClassPathEntry.setStatus(_A)
_JvmRTBootClassPathIndex_Type=JvmPositive32TC
_JvmRTBootClassPathIndex_Object=MibTableColumn
jvmRTBootClassPathIndex=_JvmRTBootClassPathIndex_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,21,1,1),_JvmRTBootClassPathIndex_Type())
jvmRTBootClassPathIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:jvmRTBootClassPathIndex.setStatus(_A)
_JvmRTBootClassPathItem_Type=JvmPathElementTC
_JvmRTBootClassPathItem_Object=MibTableColumn
jvmRTBootClassPathItem=_JvmRTBootClassPathItem_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,21,1,2),_JvmRTBootClassPathItem_Type())
jvmRTBootClassPathItem.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmRTBootClassPathItem.setStatus(_A)
_JvmRTClassPathTable_Object=MibTable
jvmRTClassPathTable=_JvmRTClassPathTable_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,22))
if mibBuilder.loadTexts:jvmRTClassPathTable.setStatus(_A)
_JvmRTClassPathEntry_Object=MibTableRow
jvmRTClassPathEntry=_JvmRTClassPathEntry_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,22,1))
jvmRTClassPathEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:jvmRTClassPathEntry.setStatus(_A)
_JvmRTClassPathIndex_Type=JvmPositive32TC
_JvmRTClassPathIndex_Object=MibTableColumn
jvmRTClassPathIndex=_JvmRTClassPathIndex_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,22,1,1),_JvmRTClassPathIndex_Type())
jvmRTClassPathIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:jvmRTClassPathIndex.setStatus(_A)
_JvmRTClassPathItem_Type=JvmPathElementTC
_JvmRTClassPathItem_Object=MibTableColumn
jvmRTClassPathItem=_JvmRTClassPathItem_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,22,1,2),_JvmRTClassPathItem_Type())
jvmRTClassPathItem.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmRTClassPathItem.setStatus(_A)
_JvmRTLibraryPathTable_Object=MibTable
jvmRTLibraryPathTable=_JvmRTLibraryPathTable_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,23))
if mibBuilder.loadTexts:jvmRTLibraryPathTable.setStatus(_A)
_JvmRTLibraryPathEntry_Object=MibTableRow
jvmRTLibraryPathEntry=_JvmRTLibraryPathEntry_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,23,1))
jvmRTLibraryPathEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:jvmRTLibraryPathEntry.setStatus(_A)
_JvmRTLibraryPathIndex_Type=JvmPositive32TC
_JvmRTLibraryPathIndex_Object=MibTableColumn
jvmRTLibraryPathIndex=_JvmRTLibraryPathIndex_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,23,1,1),_JvmRTLibraryPathIndex_Type())
jvmRTLibraryPathIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:jvmRTLibraryPathIndex.setStatus(_A)
_JvmRTLibraryPathItem_Type=JvmPathElementTC
_JvmRTLibraryPathItem_Object=MibTableColumn
jvmRTLibraryPathItem=_JvmRTLibraryPathItem_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,4,23,1,2),_JvmRTLibraryPathItem_Type())
jvmRTLibraryPathItem.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmRTLibraryPathItem.setStatus(_A)
_JvmCompilation_ObjectIdentity=ObjectIdentity
jvmCompilation=_JvmCompilation_ObjectIdentity((1,3,6,1,4,1,42,2,145,3,163,1,1,5))
_JvmJITCompilerName_Type=JvmJavaObjectNameTC
_JvmJITCompilerName_Object=MibScalar
jvmJITCompilerName=_JvmJITCompilerName_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,5,1),_JvmJITCompilerName_Type())
jvmJITCompilerName.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmJITCompilerName.setStatus(_A)
_JvmJITCompilerTimeMs_Type=JvmTimeMillis64TC
_JvmJITCompilerTimeMs_Object=MibScalar
jvmJITCompilerTimeMs=_JvmJITCompilerTimeMs_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,5,2),_JvmJITCompilerTimeMs_Type())
jvmJITCompilerTimeMs.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmJITCompilerTimeMs.setStatus(_A)
if mibBuilder.loadTexts:jvmJITCompilerTimeMs.setUnits(_F)
_JvmJITCompilerTimeMonitoring_Type=JvmImplSupportStateTC
_JvmJITCompilerTimeMonitoring_Object=MibScalar
jvmJITCompilerTimeMonitoring=_JvmJITCompilerTimeMonitoring_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,5,3),_JvmJITCompilerTimeMonitoring_Type())
jvmJITCompilerTimeMonitoring.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmJITCompilerTimeMonitoring.setStatus(_A)
_JvmOS_ObjectIdentity=ObjectIdentity
jvmOS=_JvmOS_ObjectIdentity((1,3,6,1,4,1,42,2,145,3,163,1,1,6))
_JvmOSName_Type=JvmJavaObjectNameTC
_JvmOSName_Object=MibScalar
jvmOSName=_JvmOSName_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,6,1),_JvmOSName_Type())
jvmOSName.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmOSName.setStatus(_A)
_JvmOSArch_Type=DisplayString
_JvmOSArch_Object=MibScalar
jvmOSArch=_JvmOSArch_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,6,2),_JvmOSArch_Type())
jvmOSArch.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmOSArch.setStatus(_A)
_JvmOSVersion_Type=DisplayString
_JvmOSVersion_Object=MibScalar
jvmOSVersion=_JvmOSVersion_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,6,3),_JvmOSVersion_Type())
jvmOSVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmOSVersion.setStatus(_A)
_JvmOSProcessorCount_Type=Integer32
_JvmOSProcessorCount_Object=MibScalar
jvmOSProcessorCount=_JvmOSProcessorCount_Object((1,3,6,1,4,1,42,2,145,3,163,1,1,6,4),_JvmOSProcessorCount_Type())
jvmOSProcessorCount.setMaxAccess(_C)
if mibBuilder.loadTexts:jvmOSProcessorCount.setStatus(_A)
_JvmMgtMIBNotifications_ObjectIdentity=ObjectIdentity
jvmMgtMIBNotifications=_JvmMgtMIBNotifications_ObjectIdentity((1,3,6,1,4,1,42,2,145,3,163,1,2))
_JvmMgtMIBMemoryNotifs_ObjectIdentity=ObjectIdentity
jvmMgtMIBMemoryNotifs=_JvmMgtMIBMemoryNotifs_ObjectIdentity((1,3,6,1,4,1,42,2,145,3,163,1,2,2))
_JvmMgtMIBLowMemoryNotifs_ObjectIdentity=ObjectIdentity
jvmMgtMIBLowMemoryNotifs=_JvmMgtMIBLowMemoryNotifs_ObjectIdentity((1,3,6,1,4,1,42,2,145,3,163,1,2,2,1))
_JvmLowMemoryPrefix_ObjectIdentity=ObjectIdentity
jvmLowMemoryPrefix=_JvmLowMemoryPrefix_ObjectIdentity((1,3,6,1,4,1,42,2,145,3,163,1,2,2,1,0))
_JvmMgtMIBConformance_ObjectIdentity=ObjectIdentity
jvmMgtMIBConformance=_JvmMgtMIBConformance_ObjectIdentity((1,3,6,1,4,1,42,2,145,3,163,1,3))
_JvmMgtMIBCompliances_ObjectIdentity=ObjectIdentity
jvmMgtMIBCompliances=_JvmMgtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,42,2,145,3,163,1,3,1))
_JvmMgtMIBGroups_ObjectIdentity=ObjectIdentity
jvmMgtMIBGroups=_JvmMgtMIBGroups_ObjectIdentity((1,3,6,1,4,1,42,2,145,3,163,1,3,2))
_JvmClassLoadingGroups_ObjectIdentity=ObjectIdentity
jvmClassLoadingGroups=_JvmClassLoadingGroups_ObjectIdentity((1,3,6,1,4,1,42,2,145,3,163,1,3,2,1))
_JvmMemoryGroups_ObjectIdentity=ObjectIdentity
jvmMemoryGroups=_JvmMemoryGroups_ObjectIdentity((1,3,6,1,4,1,42,2,145,3,163,1,3,2,2))
_JvmMemPoolGroups_ObjectIdentity=ObjectIdentity
jvmMemPoolGroups=_JvmMemPoolGroups_ObjectIdentity((1,3,6,1,4,1,42,2,145,3,163,1,3,2,2,7))
_JvmThreadGroups_ObjectIdentity=ObjectIdentity
jvmThreadGroups=_JvmThreadGroups_ObjectIdentity((1,3,6,1,4,1,42,2,145,3,163,1,3,2,3))
_JvmThreadInstanceGroups_ObjectIdentity=ObjectIdentity
jvmThreadInstanceGroups=_JvmThreadInstanceGroups_ObjectIdentity((1,3,6,1,4,1,42,2,145,3,163,1,3,2,3,2))
_JvmRuntimeGroups_ObjectIdentity=ObjectIdentity
jvmRuntimeGroups=_JvmRuntimeGroups_ObjectIdentity((1,3,6,1,4,1,42,2,145,3,163,1,3,2,4))
_JvmJITCompilerGroups_ObjectIdentity=ObjectIdentity
jvmJITCompilerGroups=_JvmJITCompilerGroups_ObjectIdentity((1,3,6,1,4,1,42,2,145,3,163,1,3,2,5))
jvmClassLoadingBasicGroup=ObjectGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,1,1))
jvmClassLoadingBasicGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:jvmClassLoadingBasicGroup.setStatus(_A)
jvmClassLoadingSetGroup=ObjectGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,1,2))
jvmClassLoadingSetGroup.setObjects((_B,_d))
if mibBuilder.loadTexts:jvmClassLoadingSetGroup.setStatus(_A)
jvmMemoryBasicGroup=ObjectGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,2,1))
jvmMemoryBasicGroup.setObjects((_B,_e))
if mibBuilder.loadTexts:jvmMemoryBasicGroup.setStatus(_A)
jvmMemoryHeapUsageGroup=ObjectGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,2,2))
jvmMemoryHeapUsageGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:jvmMemoryHeapUsageGroup.setStatus(_A)
jvmMemoryNonHeapUsageGroup=ObjectGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,2,3))
jvmMemoryNonHeapUsageGroup.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:jvmMemoryNonHeapUsageGroup.setStatus(_A)
jvmMemorySetGroup=ObjectGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,2,4))
jvmMemorySetGroup.setObjects(*((_B,_n),(_B,_o)))
if mibBuilder.loadTexts:jvmMemorySetGroup.setStatus(_A)
jvmMemManagerGroup=ObjectGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,2,5))
jvmMemManagerGroup.setObjects(*((_B,_p),(_B,_q)))
if mibBuilder.loadTexts:jvmMemManagerGroup.setStatus(_A)
jvmMemGCGroup=ObjectGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,2,6))
jvmMemGCGroup.setObjects(*((_B,_r),(_B,_s)))
if mibBuilder.loadTexts:jvmMemGCGroup.setStatus(_A)
jvmMemPoolBasicGroup=ObjectGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,2,7,1))
jvmMemPoolBasicGroup.setObjects(*((_B,_I),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:jvmMemPoolBasicGroup.setStatus(_A)
jvmMemPoolMonitoringGroup=ObjectGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,2,7,2))
jvmMemPoolMonitoringGroup.setObjects(*((_B,_y),(_B,_N)))
if mibBuilder.loadTexts:jvmMemPoolMonitoringGroup.setStatus(_A)
jvmMemPoolUsageGroup=ObjectGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,2,7,3))
jvmMemPoolUsageGroup.setObjects(*((_B,_z),(_B,_O),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:jvmMemPoolUsageGroup.setStatus(_A)
jvmMemPoolPeakUsageGroup=ObjectGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,2,7,4))
jvmMemPoolPeakUsageGroup.setObjects(*((_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:jvmMemPoolPeakUsageGroup.setStatus(_A)
jvmMemPoolCollectUsageGroup=ObjectGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,2,7,5))
jvmMemPoolCollectUsageGroup.setObjects(*((_B,_P),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:jvmMemPoolCollectUsageGroup.setStatus(_A)
jvmMemPoolCollectMonitoringGroup=ObjectGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,2,7,6))
jvmMemPoolCollectMonitoringGroup.setObjects(*((_B,_A7),(_B,_Q)))
if mibBuilder.loadTexts:jvmMemPoolCollectMonitoringGroup.setStatus(_A)
jvmMemMgrPoolRelationGroup=ObjectGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,2,8))
jvmMemMgrPoolRelationGroup.setObjects(*((_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:jvmMemMgrPoolRelationGroup.setStatus(_A)
jvmThreadBasicGroup=ObjectGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,3,1))
jvmThreadBasicGroup.setObjects(*((_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:jvmThreadBasicGroup.setStatus(_A)
jvmThreadInstanceBasicGroup=ObjectGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,3,2,1))
jvmThreadInstanceBasicGroup.setObjects(*((_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:jvmThreadInstanceBasicGroup.setStatus(_A)
jvmThreadInstanceCpuGroup=ObjectGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,3,2,2))
jvmThreadInstanceCpuGroup.setObjects((_B,_AM))
if mibBuilder.loadTexts:jvmThreadInstanceCpuGroup.setStatus(_A)
jvmThreadInstanceBlockGroup=ObjectGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,3,2,3))
jvmThreadInstanceBlockGroup.setObjects(*((_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ)))
if mibBuilder.loadTexts:jvmThreadInstanceBlockGroup.setStatus(_A)
jvmRuntimeBasicGroup=ObjectGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,4,1))
jvmRuntimeBasicGroup.setObjects(*((_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af)))
if mibBuilder.loadTexts:jvmRuntimeBasicGroup.setStatus(_A)
jvmRuntimeBootCPGroup=ObjectGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,4,2))
jvmRuntimeBootCPGroup.setObjects((_B,_Ag))
if mibBuilder.loadTexts:jvmRuntimeBootCPGroup.setStatus(_A)
jvmJITCompilerBasicGroup=ObjectGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,5,1))
jvmJITCompilerBasicGroup.setObjects(*((_B,_Ah),(_B,_Ai)))
if mibBuilder.loadTexts:jvmJITCompilerBasicGroup.setStatus(_A)
jvmJITCompilerTimeStatGroup=ObjectGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,5,2))
jvmJITCompilerTimeStatGroup.setObjects((_B,_Aj))
if mibBuilder.loadTexts:jvmJITCompilerTimeStatGroup.setStatus(_A)
jvmOSGroup=ObjectGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,6))
jvmOSGroup.setObjects(*((_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An)))
if mibBuilder.loadTexts:jvmOSGroup.setStatus(_A)
jvmLowMemoryPoolUsageNotif=NotificationType((1,3,6,1,4,1,42,2,145,3,163,1,2,2,1,0,1))
jvmLowMemoryPoolUsageNotif.setObjects(*((_B,_I),(_B,_O),(_B,_N)))
if mibBuilder.loadTexts:jvmLowMemoryPoolUsageNotif.setStatus(_A)
jvmLowMemoryPoolCollectNotif=NotificationType((1,3,6,1,4,1,42,2,145,3,163,1,2,2,1,0,2))
jvmLowMemoryPoolCollectNotif.setObjects(*((_B,_I),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:jvmLowMemoryPoolCollectNotif.setStatus(_A)
jvmLowMemoryUsageNotifGroup=NotificationGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,7))
jvmLowMemoryUsageNotifGroup.setObjects((_B,_Ao))
if mibBuilder.loadTexts:jvmLowMemoryUsageNotifGroup.setStatus(_A)
jvmLowMemoryCollectNotifGroup=NotificationGroup((1,3,6,1,4,1,42,2,145,3,163,1,3,2,8))
jvmLowMemoryCollectNotifGroup.setObjects((_B,_Ap))
if mibBuilder.loadTexts:jvmLowMemoryCollectNotifGroup.setStatus(_A)
jvmManagementCompliance=ModuleCompliance((1,3,6,1,4,1,42,2,145,3,163,1,3,1,1))
jvmManagementCompliance.setObjects(*((_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0),(_B,_B1),(_B,_B2),(_B,_B3),(_B,_B4),(_B,_B5),(_B,_B6),(_B,_B7),(_B,_B8),(_B,_B9),(_B,_BA),(_B,_BB),(_B,_BC),(_B,_BD),(_B,_BE)))
if mibBuilder.loadTexts:jvmManagementCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_M:JvmUnsigned64TC,'JvmJavaObjectNameTC':JvmJavaObjectNameTC,'JvmPathElementTC':JvmPathElementTC,'JvmArgValueTC':JvmArgValueTC,_T:JvmVerboseLevelTC,'JvmImplSupportStateTC':JvmImplSupportStateTC,'JvmImplOptFeatureStateTC':JvmImplOptFeatureStateTC,_U:JvmTimeMillis64TC,'JvmTimeNanos64TC':JvmTimeNanos64TC,'JvmPositive32TC':JvmPositive32TC,'JvmManagedMemoryTypeTC':JvmManagedMemoryTypeTC,'JvmValidityStateTC':JvmValidityStateTC,'JvmThreadStateTC':JvmThreadStateTC,'JvmIndex64TC':JvmIndex64TC,'sun':sun,'jmgt':jmgt,'standard':standard,'jvmMgtMIB':jvmMgtMIB,'jvmMgtMIBObjects':jvmMgtMIBObjects,'jvmClassLoading':jvmClassLoading,_a:jvmClassesLoadedCount,_b:jvmClassesTotalLoadedCount,_c:jvmClassesUnloadedCount,_d:jvmClassesVerboseLevel,'jvmMemory':jvmMemory,_e:jvmMemoryPendingFinalCount,_n:jvmMemoryGCVerboseLevel,_o:jvmMemoryGCCall,_f:jvmMemoryHeapInitSize,_g:jvmMemoryHeapUsed,_h:jvmMemoryHeapCommitted,_i:jvmMemoryHeapMaxSize,_j:jvmMemoryNonHeapInitSize,_k:jvmMemoryNonHeapUsed,_l:jvmMemoryNonHeapCommitted,_m:jvmMemoryNonHeapMaxSize,'jvmMemManagerTable':jvmMemManagerTable,'jvmMemManagerEntry':jvmMemManagerEntry,_H:jvmMemManagerIndex,_p:jvmMemManagerName,_q:jvmMemManagerState,'jvmMemGCTable':jvmMemGCTable,'jvmMemGCEntry':jvmMemGCEntry,_r:jvmMemGCCount,_s:jvmMemGCTimeMs,'jvmMemPoolTable':jvmMemPoolTable,'jvmMemPoolEntry':jvmMemPoolEntry,_L:jvmMemPoolIndex,_I:jvmMemPoolName,_t:jvmMemPoolType,_u:jvmMemPoolState,_v:jvmMemPoolPeakReset,_z:jvmMemPoolInitSize,_O:jvmMemPoolUsed,_A0:jvmMemPoolCommitted,_A1:jvmMemPoolMaxSize,_A2:jvmMemPoolPeakUsed,_A3:jvmMemPoolPeakCommitted,_A4:jvmMemPoolPeakMaxSize,_P:jvmMemPoolCollectUsed,_A5:jvmMemPoolCollectCommitted,_A6:jvmMemPoolCollectMaxSize,_y:jvmMemPoolThreshold,_N:jvmMemPoolThreshdCount,_w:jvmMemPoolThreshdSupport,_A7:jvmMemPoolCollectThreshold,_Q:jvmMemPoolCollectThreshdCount,_x:jvmMemPoolCollectThreshdSupport,'jvmMemMgrPoolRelTable':jvmMemMgrPoolRelTable,'jvmMemMgrPoolRelEntry':jvmMemMgrPoolRelEntry,_A8:jvmMemMgrRelManagerName,_A9:jvmMemMgrRelPoolName,'jvmThreading':jvmThreading,_AA:jvmThreadCount,_AB:jvmThreadDaemonCount,_AC:jvmThreadPeakCount,_AD:jvmThreadTotalStartedCount,_AE:jvmThreadContentionMonitoring,_AF:jvmThreadCpuTimeMonitoring,_AG:jvmThreadPeakCountReset,'jvmThreadInstanceTable':jvmThreadInstanceTable,'jvmThreadInstanceEntry':jvmThreadInstanceEntry,_V:jvmThreadInstIndex,_AH:jvmThreadInstId,_AI:jvmThreadInstState,_AN:jvmThreadInstBlockCount,_AO:jvmThreadInstBlockTimeMs,_AP:jvmThreadInstWaitCount,_AQ:jvmThreadInstWaitTimeMs,_AM:jvmThreadInstCpuTimeNs,_AJ:jvmThreadInstName,_AK:jvmThreadInstLockName,_AL:jvmThreadInstLockOwnerPtr,'jvmRuntime':jvmRuntime,_AR:jvmRTName,_AS:jvmRTVMName,_AT:jvmRTVMVendor,_AU:jvmRTVMVersion,_AV:jvmRTSpecName,_AW:jvmRTSpecVendor,_AX:jvmRTSpecVersion,_AY:jvmRTManagementSpecVersion,_Ab:jvmRTBootClassPathSupport,_Ac:jvmRTInputArgsCount,_AZ:jvmRTUptimeMs,_Aa:jvmRTStartTimeMs,'jvmRTInputArgsTable':jvmRTInputArgsTable,'jvmRTInputArgsEntry':jvmRTInputArgsEntry,_W:jvmRTInputArgsIndex,_Ad:jvmRTInputArgsItem,'jvmRTBootClassPathTable':jvmRTBootClassPathTable,'jvmRTBootClassPathEntry':jvmRTBootClassPathEntry,_X:jvmRTBootClassPathIndex,_Ag:jvmRTBootClassPathItem,'jvmRTClassPathTable':jvmRTClassPathTable,'jvmRTClassPathEntry':jvmRTClassPathEntry,_Y:jvmRTClassPathIndex,_Ae:jvmRTClassPathItem,'jvmRTLibraryPathTable':jvmRTLibraryPathTable,'jvmRTLibraryPathEntry':jvmRTLibraryPathEntry,_Z:jvmRTLibraryPathIndex,_Af:jvmRTLibraryPathItem,'jvmCompilation':jvmCompilation,_Ah:jvmJITCompilerName,_Aj:jvmJITCompilerTimeMs,_Ai:jvmJITCompilerTimeMonitoring,'jvmOS':jvmOS,_Ak:jvmOSName,_Al:jvmOSArch,_Am:jvmOSVersion,_An:jvmOSProcessorCount,'jvmMgtMIBNotifications':jvmMgtMIBNotifications,'jvmMgtMIBMemoryNotifs':jvmMgtMIBMemoryNotifs,'jvmMgtMIBLowMemoryNotifs':jvmMgtMIBLowMemoryNotifs,'jvmLowMemoryPrefix':jvmLowMemoryPrefix,_Ao:jvmLowMemoryPoolUsageNotif,_Ap:jvmLowMemoryPoolCollectNotif,'jvmMgtMIBConformance':jvmMgtMIBConformance,'jvmMgtMIBCompliances':jvmMgtMIBCompliances,'jvmManagementCompliance':jvmManagementCompliance,'jvmMgtMIBGroups':jvmMgtMIBGroups,'jvmClassLoadingGroups':jvmClassLoadingGroups,_Aq:jvmClassLoadingBasicGroup,_Ar:jvmClassLoadingSetGroup,'jvmMemoryGroups':jvmMemoryGroups,_As:jvmMemoryBasicGroup,_At:jvmMemoryHeapUsageGroup,_Au:jvmMemoryNonHeapUsageGroup,_Av:jvmMemorySetGroup,_Aw:jvmMemManagerGroup,_Ax:jvmMemGCGroup,'jvmMemPoolGroups':jvmMemPoolGroups,_Ay:jvmMemPoolBasicGroup,_B6:jvmMemPoolMonitoringGroup,_Az:jvmMemPoolUsageGroup,_A_:jvmMemPoolPeakUsageGroup,_B0:jvmMemPoolCollectUsageGroup,_B7:jvmMemPoolCollectMonitoringGroup,_B1:jvmMemMgrPoolRelationGroup,'jvmThreadGroups':jvmThreadGroups,_B2:jvmThreadBasicGroup,'jvmThreadInstanceGroups':jvmThreadInstanceGroups,_B3:jvmThreadInstanceBasicGroup,_BA:jvmThreadInstanceCpuGroup,_BB:jvmThreadInstanceBlockGroup,'jvmRuntimeGroups':jvmRuntimeGroups,_B4:jvmRuntimeBasicGroup,_BC:jvmRuntimeBootCPGroup,'jvmJITCompilerGroups':jvmJITCompilerGroups,_BD:jvmJITCompilerBasicGroup,_BE:jvmJITCompilerTimeStatGroup,_B5:jvmOSGroup,_B8:jvmLowMemoryUsageNotifGroup,_B9:jvmLowMemoryCollectNotifGroup})