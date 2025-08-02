_W='nwtDiskName'
_V='nwtVolumeName'
_U='nwtCPUDescription'
_T='nwtHistorySampleIndex'
_S='nwtHistoryControlIndex'
_R='disabled'
_Q='enabled'
_P='nwtControlIndex'
_O='nwtControlAttributeClass'
_N='NotificationType'
_M='nwtQueueName'
_L='InternationalDisplayString'
_K='read-write'
_J='nwtInterfaceName'
_I='not-accessible'
_H='read-only'
_G='Integer32'
_F='nwtInterval'
_E='nwtThreshold'
_D='nwtTrapTime'
_C='nwtServerName'
_B='mandatory'
_A='NetWare-Server-Trend-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InternationalDisplayString,=mibBuilder.importSymbols('HOST-RESOURCES-MIB',_L)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier',_N,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_N,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class NWTime(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
class Seconds(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Novell_ObjectIdentity=ObjectIdentity
novell=_Novell_ObjectIdentity((1,3,6,1,4,1,23))
_MibDoc_ObjectIdentity=ObjectIdentity
mibDoc=_MibDoc_ObjectIdentity((1,3,6,1,4,1,23,2))
_NwTrend_ObjectIdentity=ObjectIdentity
nwTrend=_NwTrend_ObjectIdentity((1,3,6,1,4,1,23,2,26))
_NwtControl_ObjectIdentity=ObjectIdentity
nwtControl=_NwtControl_ObjectIdentity((1,3,6,1,4,1,23,2,26,1))
_NwtControlTable_Object=MibTable
nwtControlTable=_NwtControlTable_Object((1,3,6,1,4,1,23,2,26,1,1))
if mibBuilder.loadTexts:nwtControlTable.setStatus(_B)
_NwtControlEntry_Object=MibTableRow
nwtControlEntry=_NwtControlEntry_Object((1,3,6,1,4,1,23,2,26,1,1,1))
nwtControlEntry.setIndexNames((0,_A,_O),(0,_A,_P))
if mibBuilder.loadTexts:nwtControlEntry.setStatus(_B)
class _NwtControlAttributeClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27)));namedValues=NamedValues(*(('avgLoggedInUsers',1),('avgConnections',2),('fileReads',3),('fileWrites',4),('fileReadKBytes',5),('fileWriteKBytes',6),('lslInPackets',7),('lslOutPackets',8),('ncpRequests',9),('pctCpuUtilization',10),('pctCacheBuffers',11),('pctCodeAndDataMemory',12),('pctAllocatedMemory',13),('pctDirtyPacketReceiveBuffers',14),('physIfInPackets',15),('physIfOutPackets',16),('physIfInKBytes',17),('physIfOutKBytes',18),('queueAvgNumReadyJobs',19),('queueAvgNumReadyKBytes',20),('queueAvgNextJobWaitTime',21),('volumePctFreeSpace',22),('pctCacheHitRate',23),('diskPctFreeRedirectionArea',24),('serverProcesses',25),('noECBCount',26),('osPktRcvBuffer',27)))
_NwtControlAttributeClass_Type.__name__=_G
_NwtControlAttributeClass_Object=MibTableColumn
nwtControlAttributeClass=_NwtControlAttributeClass_Object((1,3,6,1,4,1,23,2,26,1,1,1,1),_NwtControlAttributeClass_Type())
nwtControlAttributeClass.setMaxAccess(_H)
if mibBuilder.loadTexts:nwtControlAttributeClass.setStatus(_B)
class _NwtControlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NwtControlIndex_Type.__name__=_G
_NwtControlIndex_Object=MibTableColumn
nwtControlIndex=_NwtControlIndex_Object((1,3,6,1,4,1,23,2,26,1,1,1,2),_NwtControlIndex_Type())
nwtControlIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:nwtControlIndex.setStatus(_B)
_NwtControlAttributeInstance_Type=InternationalDisplayString
_NwtControlAttributeInstance_Object=MibTableColumn
nwtControlAttributeInstance=_NwtControlAttributeInstance_Object((1,3,6,1,4,1,23,2,26,1,1,1,3),_NwtControlAttributeInstance_Type())
nwtControlAttributeInstance.setMaxAccess(_H)
if mibBuilder.loadTexts:nwtControlAttributeInstance.setStatus(_B)
class _NwtControlSampleInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('fiveSeconds',1),('tenSeconds',2),('fifteenSeconds',3),('thirtySeconds',4),('oneMinute',5),('fiveMinutes',6),('fifteenMinutes',7),('thirtyMinutes',8),('oneHour',9),('fourHours',10),('eightHours',11),('oneDay',12)))
_NwtControlSampleInterval_Type.__name__=_G
_NwtControlSampleInterval_Object=MibTableColumn
nwtControlSampleInterval=_NwtControlSampleInterval_Object((1,3,6,1,4,1,23,2,26,1,1,1,4),_NwtControlSampleInterval_Type())
nwtControlSampleInterval.setMaxAccess(_K)
if mibBuilder.loadTexts:nwtControlSampleInterval.setStatus(_B)
class _NwtControlSampleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('absoluteValue',1),('deltaValue',2),('averageValue',3)))
_NwtControlSampleType_Type.__name__=_G
_NwtControlSampleType_Object=MibTableColumn
nwtControlSampleType=_NwtControlSampleType_Object((1,3,6,1,4,1,23,2,26,1,1,1,5),_NwtControlSampleType_Type())
nwtControlSampleType.setMaxAccess(_H)
if mibBuilder.loadTexts:nwtControlSampleType.setStatus(_B)
_NwtControlSampleInvalidValue_Type=Integer32
_NwtControlSampleInvalidValue_Object=MibTableColumn
nwtControlSampleInvalidValue=_NwtControlSampleInvalidValue_Object((1,3,6,1,4,1,23,2,26,1,1,1,6),_NwtControlSampleInvalidValue_Type())
nwtControlSampleInvalidValue.setMaxAccess(_H)
if mibBuilder.loadTexts:nwtControlSampleInvalidValue.setStatus(_B)
_NwtControlLastSampleValue_Type=Integer32
_NwtControlLastSampleValue_Object=MibTableColumn
nwtControlLastSampleValue=_NwtControlLastSampleValue_Object((1,3,6,1,4,1,23,2,26,1,1,1,7),_NwtControlLastSampleValue_Type())
nwtControlLastSampleValue.setMaxAccess(_H)
if mibBuilder.loadTexts:nwtControlLastSampleValue.setStatus(_B)
_NwtControlReferenceTimeStamp_Type=NWTime
_NwtControlReferenceTimeStamp_Object=MibTableColumn
nwtControlReferenceTimeStamp=_NwtControlReferenceTimeStamp_Object((1,3,6,1,4,1,23,2,26,1,1,1,8),_NwtControlReferenceTimeStamp_Type())
nwtControlReferenceTimeStamp.setMaxAccess(_H)
if mibBuilder.loadTexts:nwtControlReferenceTimeStamp.setStatus(_B)
class _NwtControlThresholdState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_NwtControlThresholdState_Type.__name__=_G
_NwtControlThresholdState_Object=MibTableColumn
nwtControlThresholdState=_NwtControlThresholdState_Object((1,3,6,1,4,1,23,2,26,1,1,1,9),_NwtControlThresholdState_Type())
nwtControlThresholdState.setMaxAccess(_K)
if mibBuilder.loadTexts:nwtControlThresholdState.setStatus(_B)
class _NwtControlThresholdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('risingAlarm',1),('fallingAlarm',2)))
_NwtControlThresholdType_Type.__name__=_G
_NwtControlThresholdType_Object=MibTableColumn
nwtControlThresholdType=_NwtControlThresholdType_Object((1,3,6,1,4,1,23,2,26,1,1,1,10),_NwtControlThresholdType_Type())
nwtControlThresholdType.setMaxAccess(_H)
if mibBuilder.loadTexts:nwtControlThresholdType.setStatus(_B)
_NwtControlRisingThreshold_Type=Integer32
_NwtControlRisingThreshold_Object=MibTableColumn
nwtControlRisingThreshold=_NwtControlRisingThreshold_Object((1,3,6,1,4,1,23,2,26,1,1,1,11),_NwtControlRisingThreshold_Type())
nwtControlRisingThreshold.setMaxAccess(_K)
if mibBuilder.loadTexts:nwtControlRisingThreshold.setStatus(_B)
_NwtControlFallingThreshold_Type=Integer32
_NwtControlFallingThreshold_Object=MibTableColumn
nwtControlFallingThreshold=_NwtControlFallingThreshold_Object((1,3,6,1,4,1,23,2,26,1,1,1,12),_NwtControlFallingThreshold_Type())
nwtControlFallingThreshold.setMaxAccess(_K)
if mibBuilder.loadTexts:nwtControlFallingThreshold.setStatus(_B)
class _NwtControlHistoryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Q,1),(_R,2)))
_NwtControlHistoryState_Type.__name__=_G
_NwtControlHistoryState_Object=MibTableColumn
nwtControlHistoryState=_NwtControlHistoryState_Object((1,3,6,1,4,1,23,2,26,1,1,1,13),_NwtControlHistoryState_Type())
nwtControlHistoryState.setMaxAccess(_K)
if mibBuilder.loadTexts:nwtControlHistoryState.setStatus(_B)
class _NwtControlHistoryLastSampleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NwtControlHistoryLastSampleIndex_Type.__name__=_G
_NwtControlHistoryLastSampleIndex_Object=MibTableColumn
nwtControlHistoryLastSampleIndex=_NwtControlHistoryLastSampleIndex_Object((1,3,6,1,4,1,23,2,26,1,1,1,14),_NwtControlHistoryLastSampleIndex_Type())
nwtControlHistoryLastSampleIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:nwtControlHistoryLastSampleIndex.setStatus(_B)
class _NwtControlHistoryBucketsRequested_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NwtControlHistoryBucketsRequested_Type.__name__=_G
_NwtControlHistoryBucketsRequested_Object=MibTableColumn
nwtControlHistoryBucketsRequested=_NwtControlHistoryBucketsRequested_Object((1,3,6,1,4,1,23,2,26,1,1,1,15),_NwtControlHistoryBucketsRequested_Type())
nwtControlHistoryBucketsRequested.setMaxAccess(_K)
if mibBuilder.loadTexts:nwtControlHistoryBucketsRequested.setStatus(_B)
class _NwtControlHistoryBucketsGranted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_NwtControlHistoryBucketsGranted_Type.__name__=_G
_NwtControlHistoryBucketsGranted_Object=MibTableColumn
nwtControlHistoryBucketsGranted=_NwtControlHistoryBucketsGranted_Object((1,3,6,1,4,1,23,2,26,1,1,1,16),_NwtControlHistoryBucketsGranted_Type())
nwtControlHistoryBucketsGranted.setMaxAccess(_H)
if mibBuilder.loadTexts:nwtControlHistoryBucketsGranted.setStatus(_B)
class _NwtControlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),('invalid',2)))
_NwtControlStatus_Type.__name__=_G
_NwtControlStatus_Object=MibTableColumn
nwtControlStatus=_NwtControlStatus_Object((1,3,6,1,4,1,23,2,26,1,1,1,17),_NwtControlStatus_Type())
nwtControlStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:nwtControlStatus.setStatus(_B)
_NwtHistoryTable_Object=MibTable
nwtHistoryTable=_NwtHistoryTable_Object((1,3,6,1,4,1,23,2,26,1,2))
if mibBuilder.loadTexts:nwtHistoryTable.setStatus(_B)
_NwtHistoryEntry_Object=MibTableRow
nwtHistoryEntry=_NwtHistoryEntry_Object((1,3,6,1,4,1,23,2,26,1,2,1))
nwtHistoryEntry.setIndexNames((0,_A,_S),(0,_A,_T))
if mibBuilder.loadTexts:nwtHistoryEntry.setStatus(_B)
class _NwtHistoryControlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NwtHistoryControlIndex_Type.__name__=_G
_NwtHistoryControlIndex_Object=MibTableColumn
nwtHistoryControlIndex=_NwtHistoryControlIndex_Object((1,3,6,1,4,1,23,2,26,1,2,1,1),_NwtHistoryControlIndex_Type())
nwtHistoryControlIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:nwtHistoryControlIndex.setStatus(_B)
class _NwtHistorySampleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_NwtHistorySampleIndex_Type.__name__=_G
_NwtHistorySampleIndex_Object=MibTableColumn
nwtHistorySampleIndex=_NwtHistorySampleIndex_Object((1,3,6,1,4,1,23,2,26,1,2,1,2),_NwtHistorySampleIndex_Type())
nwtHistorySampleIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:nwtHistorySampleIndex.setStatus(_B)
_NwtHistorySampleValue_Type=Integer32
_NwtHistorySampleValue_Object=MibTableColumn
nwtHistorySampleValue=_NwtHistorySampleValue_Object((1,3,6,1,4,1,23,2,26,1,2,1,3),_NwtHistorySampleValue_Type())
nwtHistorySampleValue.setMaxAccess(_H)
if mibBuilder.loadTexts:nwtHistorySampleValue.setStatus(_B)
_NwtTrapInfo_ObjectIdentity=ObjectIdentity
nwtTrapInfo=_NwtTrapInfo_ObjectIdentity((1,3,6,1,4,1,23,2,26,2))
class _NwtServerName_Type(InternationalDisplayString):subtypeSpec=InternationalDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
_NwtServerName_Type.__name__=_L
_NwtServerName_Object=MibScalar
nwtServerName=_NwtServerName_Object((1,3,6,1,4,1,23,2,26,2,1),_NwtServerName_Type())
nwtServerName.setMaxAccess(_I)
if mibBuilder.loadTexts:nwtServerName.setStatus(_B)
_NwtTrapTime_Type=NWTime
_NwtTrapTime_Object=MibScalar
nwtTrapTime=_NwtTrapTime_Object((1,3,6,1,4,1,23,2,26,2,2),_NwtTrapTime_Type())
nwtTrapTime.setMaxAccess(_I)
if mibBuilder.loadTexts:nwtTrapTime.setStatus(_B)
_NwtThreshold_Type=Integer32
_NwtThreshold_Object=MibScalar
nwtThreshold=_NwtThreshold_Object((1,3,6,1,4,1,23,2,26,2,3),_NwtThreshold_Type())
nwtThreshold.setMaxAccess(_I)
if mibBuilder.loadTexts:nwtThreshold.setStatus(_B)
_NwtInterval_Type=Seconds
_NwtInterval_Object=MibScalar
nwtInterval=_NwtInterval_Object((1,3,6,1,4,1,23,2,26,2,4),_NwtInterval_Type())
nwtInterval.setMaxAccess(_I)
if mibBuilder.loadTexts:nwtInterval.setStatus(_B)
class _NwtInterfaceName_Type(InternationalDisplayString):subtypeSpec=InternationalDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NwtInterfaceName_Type.__name__=_L
_NwtInterfaceName_Object=MibScalar
nwtInterfaceName=_NwtInterfaceName_Object((1,3,6,1,4,1,23,2,26,2,5),_NwtInterfaceName_Type())
nwtInterfaceName.setMaxAccess(_I)
if mibBuilder.loadTexts:nwtInterfaceName.setStatus(_B)
_NwtQueueName_Type=InternationalDisplayString
_NwtQueueName_Object=MibScalar
nwtQueueName=_NwtQueueName_Object((1,3,6,1,4,1,23,2,26,2,6),_NwtQueueName_Type())
nwtQueueName.setMaxAccess(_I)
if mibBuilder.loadTexts:nwtQueueName.setStatus(_B)
class _NwtVolumeName_Type(InternationalDisplayString):subtypeSpec=InternationalDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NwtVolumeName_Type.__name__=_L
_NwtVolumeName_Object=MibScalar
nwtVolumeName=_NwtVolumeName_Object((1,3,6,1,4,1,23,2,26,2,7),_NwtVolumeName_Type())
nwtVolumeName.setMaxAccess(_I)
if mibBuilder.loadTexts:nwtVolumeName.setStatus(_B)
class _NwtDiskName_Type(InternationalDisplayString):subtypeSpec=InternationalDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NwtDiskName_Type.__name__=_L
_NwtDiskName_Object=MibScalar
nwtDiskName=_NwtDiskName_Object((1,3,6,1,4,1,23,2,26,2,8),_NwtDiskName_Type())
nwtDiskName.setMaxAccess(_I)
if mibBuilder.loadTexts:nwtDiskName.setStatus(_B)
_NwtCPUDescription_Type=InternationalDisplayString
_NwtCPUDescription_Object=MibScalar
nwtCPUDescription=_NwtCPUDescription_Object((1,3,6,1,4,1,23,2,26,2,9),_NwtCPUDescription_Type())
nwtCPUDescription.setMaxAccess(_I)
if mibBuilder.loadTexts:nwtCPUDescription.setStatus(_B)
nwtThresholdLoggedInUsers=NotificationType((1,3,6,1,4,1,23,2,26,0,1))
nwtThresholdLoggedInUsers.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:nwtThresholdLoggedInUsers.setStatus('')
nwtThresholdConnections=NotificationType((1,3,6,1,4,1,23,2,26,0,2))
nwtThresholdConnections.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:nwtThresholdConnections.setStatus('')
nwtThresholdFileReads=NotificationType((1,3,6,1,4,1,23,2,26,0,3))
nwtThresholdFileReads.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:nwtThresholdFileReads.setStatus('')
nwtThresholdFileWrites=NotificationType((1,3,6,1,4,1,23,2,26,0,4))
nwtThresholdFileWrites.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:nwtThresholdFileWrites.setStatus('')
nwtThresholdFileReadKBytes=NotificationType((1,3,6,1,4,1,23,2,26,0,5))
nwtThresholdFileReadKBytes.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:nwtThresholdFileReadKBytes.setStatus('')
nwtThresholdFileWriteKBytes=NotificationType((1,3,6,1,4,1,23,2,26,0,6))
nwtThresholdFileWriteKBytes.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:nwtThresholdFileWriteKBytes.setStatus('')
nwtThresholdLslInPackets=NotificationType((1,3,6,1,4,1,23,2,26,0,7))
nwtThresholdLslInPackets.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:nwtThresholdLslInPackets.setStatus('')
nwtThresholdLslOutPackets=NotificationType((1,3,6,1,4,1,23,2,26,0,8))
nwtThresholdLslOutPackets.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:nwtThresholdLslOutPackets.setStatus('')
nwtThresholdNcpRequests=NotificationType((1,3,6,1,4,1,23,2,26,0,9))
nwtThresholdNcpRequests.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:nwtThresholdNcpRequests.setStatus('')
nwtThresholdPctCpuUtilization=NotificationType((1,3,6,1,4,1,23,2,26,0,10))
nwtThresholdPctCpuUtilization.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_U)))
if mibBuilder.loadTexts:nwtThresholdPctCpuUtilization.setStatus('')
nwtThresholdPctCacheBuffers=NotificationType((1,3,6,1,4,1,23,2,26,0,11))
nwtThresholdPctCacheBuffers.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:nwtThresholdPctCacheBuffers.setStatus('')
nwtThresholdCodeAndDataMemory=NotificationType((1,3,6,1,4,1,23,2,26,0,12))
nwtThresholdCodeAndDataMemory.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:nwtThresholdCodeAndDataMemory.setStatus('')
nwtThresholdAllocatedMemory=NotificationType((1,3,6,1,4,1,23,2,26,0,13))
nwtThresholdAllocatedMemory.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:nwtThresholdAllocatedMemory.setStatus('')
nwtThresholdPctDirtyCacheBuffers=NotificationType((1,3,6,1,4,1,23,2,26,0,14))
nwtThresholdPctDirtyCacheBuffers.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:nwtThresholdPctDirtyCacheBuffers.setStatus('')
nwtThresholdPhysIfInPackets=NotificationType((1,3,6,1,4,1,23,2,26,0,15))
nwtThresholdPhysIfInPackets.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_J)))
if mibBuilder.loadTexts:nwtThresholdPhysIfInPackets.setStatus('')
nwtThresholdPhysIfOutPackets=NotificationType((1,3,6,1,4,1,23,2,26,0,16))
nwtThresholdPhysIfOutPackets.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_J)))
if mibBuilder.loadTexts:nwtThresholdPhysIfOutPackets.setStatus('')
nwtThresholdPhysIfInKBytes=NotificationType((1,3,6,1,4,1,23,2,26,0,17))
nwtThresholdPhysIfInKBytes.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_J)))
if mibBuilder.loadTexts:nwtThresholdPhysIfInKBytes.setStatus('')
nwtThresholdPhysIfOutKBytes=NotificationType((1,3,6,1,4,1,23,2,26,0,18))
nwtThresholdPhysIfOutKBytes.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_J)))
if mibBuilder.loadTexts:nwtThresholdPhysIfOutKBytes.setStatus('')
nwtThresholdQueueNumReadyJobs=NotificationType((1,3,6,1,4,1,23,2,26,0,19))
nwtThresholdQueueNumReadyJobs.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_M),(_A,_F)))
if mibBuilder.loadTexts:nwtThresholdQueueNumReadyJobs.setStatus('')
nwtThresholdQueueNumReadyKBytes=NotificationType((1,3,6,1,4,1,23,2,26,0,20))
nwtThresholdQueueNumReadyKBytes.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_M),(_A,_F)))
if mibBuilder.loadTexts:nwtThresholdQueueNumReadyKBytes.setStatus('')
nwtThresholdQueueNextJobWaitTime=NotificationType((1,3,6,1,4,1,23,2,26,0,21))
nwtThresholdQueueNextJobWaitTime.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_M)))
if mibBuilder.loadTexts:nwtThresholdQueueNextJobWaitTime.setStatus('')
nwtThresholdVolumePctFreeSpace=NotificationType((1,3,6,1,4,1,23,2,26,0,22))
nwtThresholdVolumePctFreeSpace.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_V)))
if mibBuilder.loadTexts:nwtThresholdVolumePctFreeSpace.setStatus('')
nwtThresholdPctCacheHitRate=NotificationType((1,3,6,1,4,1,23,2,26,0,23))
nwtThresholdPctCacheHitRate.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F)))
if mibBuilder.loadTexts:nwtThresholdPctCacheHitRate.setStatus('')
nwtThresholdDiskPctFreeRedirectionArea=NotificationType((1,3,6,1,4,1,23,2,26,0,24))
nwtThresholdDiskPctFreeRedirectionArea.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_W)))
if mibBuilder.loadTexts:nwtThresholdDiskPctFreeRedirectionArea.setStatus('')
nwtThresholdServerProcesses=NotificationType((1,3,6,1,4,1,23,2,26,0,25))
nwtThresholdServerProcesses.setObjects(*((_A,_C),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:nwtThresholdServerProcesses.setStatus('')
nwtThresholdNoECBCount=NotificationType((1,3,6,1,4,1,23,2,26,0,26))
nwtThresholdNoECBCount.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_J)))
if mibBuilder.loadTexts:nwtThresholdNoECBCount.setStatus('')
nwtThresholdOsPktRcvBuffer=NotificationType((1,3,6,1,4,1,23,2,26,0,27))
nwtThresholdOsPktRcvBuffer.setObjects(*((_A,_C),(_A,_D),(_A,_E),(_A,_F),(_A,_J)))
if mibBuilder.loadTexts:nwtThresholdOsPktRcvBuffer.setStatus('')
mibBuilder.exportSymbols(_A,**{'NWTime':NWTime,'Seconds':Seconds,'novell':novell,'mibDoc':mibDoc,'nwTrend':nwTrend,'nwtThresholdLoggedInUsers':nwtThresholdLoggedInUsers,'nwtThresholdConnections':nwtThresholdConnections,'nwtThresholdFileReads':nwtThresholdFileReads,'nwtThresholdFileWrites':nwtThresholdFileWrites,'nwtThresholdFileReadKBytes':nwtThresholdFileReadKBytes,'nwtThresholdFileWriteKBytes':nwtThresholdFileWriteKBytes,'nwtThresholdLslInPackets':nwtThresholdLslInPackets,'nwtThresholdLslOutPackets':nwtThresholdLslOutPackets,'nwtThresholdNcpRequests':nwtThresholdNcpRequests,'nwtThresholdPctCpuUtilization':nwtThresholdPctCpuUtilization,'nwtThresholdPctCacheBuffers':nwtThresholdPctCacheBuffers,'nwtThresholdCodeAndDataMemory':nwtThresholdCodeAndDataMemory,'nwtThresholdAllocatedMemory':nwtThresholdAllocatedMemory,'nwtThresholdPctDirtyCacheBuffers':nwtThresholdPctDirtyCacheBuffers,'nwtThresholdPhysIfInPackets':nwtThresholdPhysIfInPackets,'nwtThresholdPhysIfOutPackets':nwtThresholdPhysIfOutPackets,'nwtThresholdPhysIfInKBytes':nwtThresholdPhysIfInKBytes,'nwtThresholdPhysIfOutKBytes':nwtThresholdPhysIfOutKBytes,'nwtThresholdQueueNumReadyJobs':nwtThresholdQueueNumReadyJobs,'nwtThresholdQueueNumReadyKBytes':nwtThresholdQueueNumReadyKBytes,'nwtThresholdQueueNextJobWaitTime':nwtThresholdQueueNextJobWaitTime,'nwtThresholdVolumePctFreeSpace':nwtThresholdVolumePctFreeSpace,'nwtThresholdPctCacheHitRate':nwtThresholdPctCacheHitRate,'nwtThresholdDiskPctFreeRedirectionArea':nwtThresholdDiskPctFreeRedirectionArea,'nwtThresholdServerProcesses':nwtThresholdServerProcesses,'nwtThresholdNoECBCount':nwtThresholdNoECBCount,'nwtThresholdOsPktRcvBuffer':nwtThresholdOsPktRcvBuffer,'nwtControl':nwtControl,'nwtControlTable':nwtControlTable,'nwtControlEntry':nwtControlEntry,_O:nwtControlAttributeClass,_P:nwtControlIndex,'nwtControlAttributeInstance':nwtControlAttributeInstance,'nwtControlSampleInterval':nwtControlSampleInterval,'nwtControlSampleType':nwtControlSampleType,'nwtControlSampleInvalidValue':nwtControlSampleInvalidValue,'nwtControlLastSampleValue':nwtControlLastSampleValue,'nwtControlReferenceTimeStamp':nwtControlReferenceTimeStamp,'nwtControlThresholdState':nwtControlThresholdState,'nwtControlThresholdType':nwtControlThresholdType,'nwtControlRisingThreshold':nwtControlRisingThreshold,'nwtControlFallingThreshold':nwtControlFallingThreshold,'nwtControlHistoryState':nwtControlHistoryState,'nwtControlHistoryLastSampleIndex':nwtControlHistoryLastSampleIndex,'nwtControlHistoryBucketsRequested':nwtControlHistoryBucketsRequested,'nwtControlHistoryBucketsGranted':nwtControlHistoryBucketsGranted,'nwtControlStatus':nwtControlStatus,'nwtHistoryTable':nwtHistoryTable,'nwtHistoryEntry':nwtHistoryEntry,_S:nwtHistoryControlIndex,_T:nwtHistorySampleIndex,'nwtHistorySampleValue':nwtHistorySampleValue,'nwtTrapInfo':nwtTrapInfo,_C:nwtServerName,_D:nwtTrapTime,_E:nwtThreshold,_F:nwtInterval,_J:nwtInterfaceName,_M:nwtQueueName,_V:nwtVolumeName,_W:nwtDiskName,_U:nwtCPUDescription})