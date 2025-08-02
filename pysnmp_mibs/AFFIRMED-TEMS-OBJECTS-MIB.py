_M='perfMetricThresholdIndex'
_L='temsServerSnmpManagerIndex'
_K='temsServerPerfStatsIndex'
_J='temsServerActiveAlarmIndex'
_I='temsServerResourceTypeIndex'
_H='Unsigned32'
_G='temsServerPerfMetricsIndex'
_F='temsServerResourceIndex'
_E='not-accessible'
_D='read-create'
_C='AFFIRMED-TEMS-OBJECTS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
affirmedSnmpObjects,=mibBuilder.importSymbols('AFFIRMED-TEMS-SNMP-MIB','affirmedSnmpObjects')
AlarmLevel,ResourceAdminStatus,ThresholdType=mibBuilder.importSymbols('AFFIRMED-TEMS-TC-MIB','AlarmLevel','ResourceAdminStatus','ThresholdType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
affirmedTemsObjects=ModuleIdentity((1,3,6,1,4,1,37963,6,2,1))
if mibBuilder.loadTexts:affirmedTemsObjects.setRevisions(('2008-03-14 11:14',))
_TemsServerSystemGroup_ObjectIdentity=ObjectIdentity
temsServerSystemGroup=_TemsServerSystemGroup_ObjectIdentity((1,3,6,1,4,1,37963,6,2,1,1))
_TemsServerDetails_ObjectIdentity=ObjectIdentity
temsServerDetails=_TemsServerDetails_ObjectIdentity((1,3,6,1,4,1,37963,6,2,1,1,1))
_TemsServerId_Type=Unsigned32
_TemsServerId_Object=MibScalar
temsServerId=_TemsServerId_Object((1,3,6,1,4,1,37963,6,2,1,1,1,1),_TemsServerId_Type())
temsServerId.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerId.setStatus(_A)
_TemsServerName_Type=DisplayString
_TemsServerName_Object=MibScalar
temsServerName=_TemsServerName_Object((1,3,6,1,4,1,37963,6,2,1,1,1,2),_TemsServerName_Type())
temsServerName.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerName.setStatus(_A)
_TemsServerRunningVersion_Type=DisplayString
_TemsServerRunningVersion_Object=MibScalar
temsServerRunningVersion=_TemsServerRunningVersion_Object((1,3,6,1,4,1,37963,6,2,1,1,1,3),_TemsServerRunningVersion_Type())
temsServerRunningVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerRunningVersion.setStatus(_A)
_TemsServerDeployedLocation_Type=DisplayString
_TemsServerDeployedLocation_Object=MibScalar
temsServerDeployedLocation=_TemsServerDeployedLocation_Object((1,3,6,1,4,1,37963,6,2,1,1,1,4),_TemsServerDeployedLocation_Type())
temsServerDeployedLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerDeployedLocation.setStatus(_A)
_TemsServerResourceGroup_ObjectIdentity=ObjectIdentity
temsServerResourceGroup=_TemsServerResourceGroup_ObjectIdentity((1,3,6,1,4,1,37963,6,2,1,2))
_TemsServerResourceTypeTable_Object=MibTable
temsServerResourceTypeTable=_TemsServerResourceTypeTable_Object((1,3,6,1,4,1,37963,6,2,1,2,1))
if mibBuilder.loadTexts:temsServerResourceTypeTable.setStatus(_A)
_TemsServerResourceTypeEntry_Object=MibTableRow
temsServerResourceTypeEntry=_TemsServerResourceTypeEntry_Object((1,3,6,1,4,1,37963,6,2,1,2,1,1))
temsServerResourceTypeEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:temsServerResourceTypeEntry.setStatus(_A)
_TemsServerResourceTypeIndex_Type=Unsigned32
_TemsServerResourceTypeIndex_Object=MibTableColumn
temsServerResourceTypeIndex=_TemsServerResourceTypeIndex_Object((1,3,6,1,4,1,37963,6,2,1,2,1,1,1),_TemsServerResourceTypeIndex_Type())
temsServerResourceTypeIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:temsServerResourceTypeIndex.setStatus(_A)
_TemsServerResourceType_Type=DisplayString
_TemsServerResourceType_Object=MibTableColumn
temsServerResourceType=_TemsServerResourceType_Object((1,3,6,1,4,1,37963,6,2,1,2,1,1,2),_TemsServerResourceType_Type())
temsServerResourceType.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerResourceType.setStatus(_A)
_TemsServerResourceTable_Object=MibTable
temsServerResourceTable=_TemsServerResourceTable_Object((1,3,6,1,4,1,37963,6,2,1,2,2))
if mibBuilder.loadTexts:temsServerResourceTable.setStatus(_A)
_TemsServerResourceEntry_Object=MibTableRow
temsServerResourceEntry=_TemsServerResourceEntry_Object((1,3,6,1,4,1,37963,6,2,1,2,2,1))
temsServerResourceEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:temsServerResourceEntry.setStatus(_A)
_TemsServerResourceIndex_Type=Unsigned32
_TemsServerResourceIndex_Object=MibTableColumn
temsServerResourceIndex=_TemsServerResourceIndex_Object((1,3,6,1,4,1,37963,6,2,1,2,2,1,1),_TemsServerResourceIndex_Type())
temsServerResourceIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:temsServerResourceIndex.setStatus(_A)
_TemsServerResourceName_Type=DisplayString
_TemsServerResourceName_Object=MibTableColumn
temsServerResourceName=_TemsServerResourceName_Object((1,3,6,1,4,1,37963,6,2,1,2,2,1,2),_TemsServerResourceName_Type())
temsServerResourceName.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerResourceName.setStatus(_A)
_TemsServerResourceTypeId_Type=Unsigned32
_TemsServerResourceTypeId_Object=MibTableColumn
temsServerResourceTypeId=_TemsServerResourceTypeId_Object((1,3,6,1,4,1,37963,6,2,1,2,2,1,3),_TemsServerResourceTypeId_Type())
temsServerResourceTypeId.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerResourceTypeId.setStatus(_A)
_TemsServerResourceIpAddress_Type=IpAddress
_TemsServerResourceIpAddress_Object=MibTableColumn
temsServerResourceIpAddress=_TemsServerResourceIpAddress_Object((1,3,6,1,4,1,37963,6,2,1,2,2,1,4),_TemsServerResourceIpAddress_Type())
temsServerResourceIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerResourceIpAddress.setStatus(_A)
_TemsServerResourceAdminStatus_Type=ResourceAdminStatus
_TemsServerResourceAdminStatus_Object=MibTableColumn
temsServerResourceAdminStatus=_TemsServerResourceAdminStatus_Object((1,3,6,1,4,1,37963,6,2,1,2,2,1,5),_TemsServerResourceAdminStatus_Type())
temsServerResourceAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerResourceAdminStatus.setStatus(_A)
_TemsServerAlarmGroup_ObjectIdentity=ObjectIdentity
temsServerAlarmGroup=_TemsServerAlarmGroup_ObjectIdentity((1,3,6,1,4,1,37963,6,2,1,3))
_TemsServerActiveAlarmTable_Object=MibTable
temsServerActiveAlarmTable=_TemsServerActiveAlarmTable_Object((1,3,6,1,4,1,37963,6,2,1,3,2))
if mibBuilder.loadTexts:temsServerActiveAlarmTable.setStatus(_A)
_TemsServerActiveAlarmEntry_Object=MibTableRow
temsServerActiveAlarmEntry=_TemsServerActiveAlarmEntry_Object((1,3,6,1,4,1,37963,6,2,1,3,2,1))
temsServerActiveAlarmEntry.setIndexNames((0,_C,_J),(0,_C,_F))
if mibBuilder.loadTexts:temsServerActiveAlarmEntry.setStatus(_A)
_TemsServerActiveAlarmIndex_Type=Unsigned32
_TemsServerActiveAlarmIndex_Object=MibTableColumn
temsServerActiveAlarmIndex=_TemsServerActiveAlarmIndex_Object((1,3,6,1,4,1,37963,6,2,1,3,2,1,1),_TemsServerActiveAlarmIndex_Type())
temsServerActiveAlarmIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:temsServerActiveAlarmIndex.setStatus(_A)
_TemsServerActiveAlarmSource_Type=DisplayString
_TemsServerActiveAlarmSource_Object=MibTableColumn
temsServerActiveAlarmSource=_TemsServerActiveAlarmSource_Object((1,3,6,1,4,1,37963,6,2,1,3,2,1,2),_TemsServerActiveAlarmSource_Type())
temsServerActiveAlarmSource.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerActiveAlarmSource.setStatus(_A)
_TemsServerActiveAlarmCategory_Type=DisplayString
_TemsServerActiveAlarmCategory_Object=MibTableColumn
temsServerActiveAlarmCategory=_TemsServerActiveAlarmCategory_Object((1,3,6,1,4,1,37963,6,2,1,3,2,1,3),_TemsServerActiveAlarmCategory_Type())
temsServerActiveAlarmCategory.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerActiveAlarmCategory.setStatus(_A)
_TemsServerActiveAlarmSeverity_Type=AlarmLevel
_TemsServerActiveAlarmSeverity_Object=MibTableColumn
temsServerActiveAlarmSeverity=_TemsServerActiveAlarmSeverity_Object((1,3,6,1,4,1,37963,6,2,1,3,2,1,4),_TemsServerActiveAlarmSeverity_Type())
temsServerActiveAlarmSeverity.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerActiveAlarmSeverity.setStatus(_A)
_TemsServerActiveAlarmMessage_Type=DisplayString
_TemsServerActiveAlarmMessage_Object=MibTableColumn
temsServerActiveAlarmMessage=_TemsServerActiveAlarmMessage_Object((1,3,6,1,4,1,37963,6,2,1,3,2,1,5),_TemsServerActiveAlarmMessage_Type())
temsServerActiveAlarmMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerActiveAlarmMessage.setStatus(_A)
_TemsServerActiveAlarmRemedy_Type=DisplayString
_TemsServerActiveAlarmRemedy_Object=MibTableColumn
temsServerActiveAlarmRemedy=_TemsServerActiveAlarmRemedy_Object((1,3,6,1,4,1,37963,6,2,1,3,2,1,6),_TemsServerActiveAlarmRemedy_Type())
temsServerActiveAlarmRemedy.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerActiveAlarmRemedy.setStatus(_A)
_TemsServerActiveAlarmOwner_Type=DisplayString
_TemsServerActiveAlarmOwner_Object=MibTableColumn
temsServerActiveAlarmOwner=_TemsServerActiveAlarmOwner_Object((1,3,6,1,4,1,37963,6,2,1,3,2,1,7),_TemsServerActiveAlarmOwner_Type())
temsServerActiveAlarmOwner.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerActiveAlarmOwner.setStatus(_A)
_TemsServerActiveAlarmCreatedTime_Type=DateAndTime
_TemsServerActiveAlarmCreatedTime_Object=MibTableColumn
temsServerActiveAlarmCreatedTime=_TemsServerActiveAlarmCreatedTime_Object((1,3,6,1,4,1,37963,6,2,1,3,2,1,8),_TemsServerActiveAlarmCreatedTime_Type())
temsServerActiveAlarmCreatedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerActiveAlarmCreatedTime.setStatus(_A)
_TemsServerActiveAlarmUpdatedTime_Type=DateAndTime
_TemsServerActiveAlarmUpdatedTime_Object=MibTableColumn
temsServerActiveAlarmUpdatedTime=_TemsServerActiveAlarmUpdatedTime_Object((1,3,6,1,4,1,37963,6,2,1,3,2,1,9),_TemsServerActiveAlarmUpdatedTime_Type())
temsServerActiveAlarmUpdatedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerActiveAlarmUpdatedTime.setStatus(_A)
_TemsServerActiveAlarmClearedTime_Type=DateAndTime
_TemsServerActiveAlarmClearedTime_Object=MibTableColumn
temsServerActiveAlarmClearedTime=_TemsServerActiveAlarmClearedTime_Object((1,3,6,1,4,1,37963,6,2,1,3,2,1,10),_TemsServerActiveAlarmClearedTime_Type())
temsServerActiveAlarmClearedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerActiveAlarmClearedTime.setStatus(_A)
_TemsServerActiveAlarmAckStatus_Type=TruthValue
_TemsServerActiveAlarmAckStatus_Object=MibTableColumn
temsServerActiveAlarmAckStatus=_TemsServerActiveAlarmAckStatus_Object((1,3,6,1,4,1,37963,6,2,1,3,2,1,11),_TemsServerActiveAlarmAckStatus_Type())
temsServerActiveAlarmAckStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerActiveAlarmAckStatus.setStatus(_A)
_TemsServerActiveAlarmAckTime_Type=DateAndTime
_TemsServerActiveAlarmAckTime_Object=MibTableColumn
temsServerActiveAlarmAckTime=_TemsServerActiveAlarmAckTime_Object((1,3,6,1,4,1,37963,6,2,1,3,2,1,12),_TemsServerActiveAlarmAckTime_Type())
temsServerActiveAlarmAckTime.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerActiveAlarmAckTime.setStatus(_A)
_TemsServerActiveAlarmAdditionalInfo_Type=DisplayString
_TemsServerActiveAlarmAdditionalInfo_Object=MibTableColumn
temsServerActiveAlarmAdditionalInfo=_TemsServerActiveAlarmAdditionalInfo_Object((1,3,6,1,4,1,37963,6,2,1,3,2,1,13),_TemsServerActiveAlarmAdditionalInfo_Type())
temsServerActiveAlarmAdditionalInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerActiveAlarmAdditionalInfo.setStatus(_A)
_TemsServerActiveAlarmNEIndex_Type=Unsigned32
_TemsServerActiveAlarmNEIndex_Object=MibTableColumn
temsServerActiveAlarmNEIndex=_TemsServerActiveAlarmNEIndex_Object((1,3,6,1,4,1,37963,6,2,1,3,2,1,14),_TemsServerActiveAlarmNEIndex_Type())
temsServerActiveAlarmNEIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerActiveAlarmNEIndex.setStatus(_A)
_TemsServerActiveAlarmNESeqNumber_Type=Unsigned32
_TemsServerActiveAlarmNESeqNumber_Object=MibTableColumn
temsServerActiveAlarmNESeqNumber=_TemsServerActiveAlarmNESeqNumber_Object((1,3,6,1,4,1,37963,6,2,1,3,2,1,15),_TemsServerActiveAlarmNESeqNumber_Type())
temsServerActiveAlarmNESeqNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerActiveAlarmNESeqNumber.setStatus(_A)
_TemsServerActiveAlarmTrapOid_Type=DisplayString
_TemsServerActiveAlarmTrapOid_Object=MibTableColumn
temsServerActiveAlarmTrapOid=_TemsServerActiveAlarmTrapOid_Object((1,3,6,1,4,1,37963,6,2,1,3,2,1,16),_TemsServerActiveAlarmTrapOid_Type())
temsServerActiveAlarmTrapOid.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerActiveAlarmTrapOid.setStatus(_A)
_TemsServerStatsGroup_ObjectIdentity=ObjectIdentity
temsServerStatsGroup=_TemsServerStatsGroup_ObjectIdentity((1,3,6,1,4,1,37963,6,2,1,4))
_TemsServerPerfMetricsTable_Object=MibTable
temsServerPerfMetricsTable=_TemsServerPerfMetricsTable_Object((1,3,6,1,4,1,37963,6,2,1,4,1))
if mibBuilder.loadTexts:temsServerPerfMetricsTable.setStatus(_A)
_TemsServerPerfMetricsEntry_Object=MibTableRow
temsServerPerfMetricsEntry=_TemsServerPerfMetricsEntry_Object((1,3,6,1,4,1,37963,6,2,1,4,1,1))
temsServerPerfMetricsEntry.setIndexNames((0,_C,_G),(0,_C,_I))
if mibBuilder.loadTexts:temsServerPerfMetricsEntry.setStatus(_A)
_TemsServerPerfMetricsIndex_Type=Unsigned32
_TemsServerPerfMetricsIndex_Object=MibTableColumn
temsServerPerfMetricsIndex=_TemsServerPerfMetricsIndex_Object((1,3,6,1,4,1,37963,6,2,1,4,1,1,1),_TemsServerPerfMetricsIndex_Type())
temsServerPerfMetricsIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:temsServerPerfMetricsIndex.setStatus(_A)
_TemsServerPerfMetric_Type=DisplayString
_TemsServerPerfMetric_Object=MibTableColumn
temsServerPerfMetric=_TemsServerPerfMetric_Object((1,3,6,1,4,1,37963,6,2,1,4,1,1,2),_TemsServerPerfMetric_Type())
temsServerPerfMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerPerfMetric.setStatus(_A)
_TemsServerPerfMetricPollingInterval_Type=Unsigned32
_TemsServerPerfMetricPollingInterval_Object=MibTableColumn
temsServerPerfMetricPollingInterval=_TemsServerPerfMetricPollingInterval_Object((1,3,6,1,4,1,37963,6,2,1,4,1,1,3),_TemsServerPerfMetricPollingInterval_Type())
temsServerPerfMetricPollingInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerPerfMetricPollingInterval.setStatus(_A)
_TemsServerPerfStatsTable_Object=MibTable
temsServerPerfStatsTable=_TemsServerPerfStatsTable_Object((1,3,6,1,4,1,37963,6,2,1,4,2))
if mibBuilder.loadTexts:temsServerPerfStatsTable.setStatus(_A)
_TemsServerPerfStatsEntry_Object=MibTableRow
temsServerPerfStatsEntry=_TemsServerPerfStatsEntry_Object((1,3,6,1,4,1,37963,6,2,1,4,2,1))
temsServerPerfStatsEntry.setIndexNames((0,_C,_G),(0,_C,_F),(0,_C,_K))
if mibBuilder.loadTexts:temsServerPerfStatsEntry.setStatus(_A)
_TemsServerPerfStatsIndex_Type=Unsigned32
_TemsServerPerfStatsIndex_Object=MibTableColumn
temsServerPerfStatsIndex=_TemsServerPerfStatsIndex_Object((1,3,6,1,4,1,37963,6,2,1,4,2,1,1),_TemsServerPerfStatsIndex_Type())
temsServerPerfStatsIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:temsServerPerfStatsIndex.setStatus(_A)
_TemsServerPerfMetricCollectedTime_Type=DateAndTime
_TemsServerPerfMetricCollectedTime_Object=MibTableColumn
temsServerPerfMetricCollectedTime=_TemsServerPerfMetricCollectedTime_Object((1,3,6,1,4,1,37963,6,2,1,4,2,1,2),_TemsServerPerfMetricCollectedTime_Type())
temsServerPerfMetricCollectedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerPerfMetricCollectedTime.setStatus(_A)
_TemsServerPerfMetricCollectedValue_Type=Integer32
_TemsServerPerfMetricCollectedValue_Object=MibTableColumn
temsServerPerfMetricCollectedValue=_TemsServerPerfMetricCollectedValue_Object((1,3,6,1,4,1,37963,6,2,1,4,2,1,3),_TemsServerPerfMetricCollectedValue_Type())
temsServerPerfMetricCollectedValue.setMaxAccess(_B)
if mibBuilder.loadTexts:temsServerPerfMetricCollectedValue.setStatus(_A)
_TemsServerConfigGroup_ObjectIdentity=ObjectIdentity
temsServerConfigGroup=_TemsServerConfigGroup_ObjectIdentity((1,3,6,1,4,1,37963,6,2,1,5))
_TemsServerSnmpManagerTable_Object=MibTable
temsServerSnmpManagerTable=_TemsServerSnmpManagerTable_Object((1,3,6,1,4,1,37963,6,2,1,5,1))
if mibBuilder.loadTexts:temsServerSnmpManagerTable.setStatus(_A)
_TemsServerSnmpManagerEntry_Object=MibTableRow
temsServerSnmpManagerEntry=_TemsServerSnmpManagerEntry_Object((1,3,6,1,4,1,37963,6,2,1,5,1,1))
temsServerSnmpManagerEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:temsServerSnmpManagerEntry.setStatus(_A)
class _TemsServerSnmpManagerIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_TemsServerSnmpManagerIndex_Type.__name__=_H
_TemsServerSnmpManagerIndex_Object=MibTableColumn
temsServerSnmpManagerIndex=_TemsServerSnmpManagerIndex_Object((1,3,6,1,4,1,37963,6,2,1,5,1,1,1),_TemsServerSnmpManagerIndex_Type())
temsServerSnmpManagerIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:temsServerSnmpManagerIndex.setStatus(_A)
_TemsServerSnmpManagerIpAddress_Type=IpAddress
_TemsServerSnmpManagerIpAddress_Object=MibTableColumn
temsServerSnmpManagerIpAddress=_TemsServerSnmpManagerIpAddress_Object((1,3,6,1,4,1,37963,6,2,1,5,1,1,2),_TemsServerSnmpManagerIpAddress_Type())
temsServerSnmpManagerIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:temsServerSnmpManagerIpAddress.setStatus(_A)
class _TemsServerSnmpManagerTrapPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65327))
_TemsServerSnmpManagerTrapPort_Type.__name__=_H
_TemsServerSnmpManagerTrapPort_Object=MibTableColumn
temsServerSnmpManagerTrapPort=_TemsServerSnmpManagerTrapPort_Object((1,3,6,1,4,1,37963,6,2,1,5,1,1,3),_TemsServerSnmpManagerTrapPort_Type())
temsServerSnmpManagerTrapPort.setMaxAccess(_D)
if mibBuilder.loadTexts:temsServerSnmpManagerTrapPort.setStatus(_A)
_TemsServerSnmpManagerTrapCommunity_Type=DisplayString
_TemsServerSnmpManagerTrapCommunity_Object=MibTableColumn
temsServerSnmpManagerTrapCommunity=_TemsServerSnmpManagerTrapCommunity_Object((1,3,6,1,4,1,37963,6,2,1,5,1,1,4),_TemsServerSnmpManagerTrapCommunity_Type())
temsServerSnmpManagerTrapCommunity.setMaxAccess(_D)
if mibBuilder.loadTexts:temsServerSnmpManagerTrapCommunity.setStatus(_A)
_TemsServerSnmpManagerRowStatus_Type=RowStatus
_TemsServerSnmpManagerRowStatus_Object=MibTableColumn
temsServerSnmpManagerRowStatus=_TemsServerSnmpManagerRowStatus_Object((1,3,6,1,4,1,37963,6,2,1,5,1,1,5),_TemsServerSnmpManagerRowStatus_Type())
temsServerSnmpManagerRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:temsServerSnmpManagerRowStatus.setStatus(_A)
_PerfMetricThresholdTable_Object=MibTable
perfMetricThresholdTable=_PerfMetricThresholdTable_Object((1,3,6,1,4,1,37963,6,2,1,5,2))
if mibBuilder.loadTexts:perfMetricThresholdTable.setStatus(_A)
_PerfMetricThresholdEntry_Object=MibTableRow
perfMetricThresholdEntry=_PerfMetricThresholdEntry_Object((1,3,6,1,4,1,37963,6,2,1,5,2,1))
perfMetricThresholdEntry.setIndexNames((0,_C,_G),(0,_C,_M))
if mibBuilder.loadTexts:perfMetricThresholdEntry.setStatus(_A)
_PerfMetricThresholdIndex_Type=Unsigned32
_PerfMetricThresholdIndex_Object=MibTableColumn
perfMetricThresholdIndex=_PerfMetricThresholdIndex_Object((1,3,6,1,4,1,37963,6,2,1,5,2,1,1),_PerfMetricThresholdIndex_Type())
perfMetricThresholdIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:perfMetricThresholdIndex.setStatus(_A)
_PerfMetricThresholdType_Type=ThresholdType
_PerfMetricThresholdType_Object=MibTableColumn
perfMetricThresholdType=_PerfMetricThresholdType_Object((1,3,6,1,4,1,37963,6,2,1,5,2,1,2),_PerfMetricThresholdType_Type())
perfMetricThresholdType.setMaxAccess(_D)
if mibBuilder.loadTexts:perfMetricThresholdType.setStatus(_A)
_PerfMetricCriticalThreshold_Type=Integer32
_PerfMetricCriticalThreshold_Object=MibTableColumn
perfMetricCriticalThreshold=_PerfMetricCriticalThreshold_Object((1,3,6,1,4,1,37963,6,2,1,5,2,1,3),_PerfMetricCriticalThreshold_Type())
perfMetricCriticalThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:perfMetricCriticalThreshold.setStatus(_A)
_PerfMetricMajorThreshold_Type=Integer32
_PerfMetricMajorThreshold_Object=MibTableColumn
perfMetricMajorThreshold=_PerfMetricMajorThreshold_Object((1,3,6,1,4,1,37963,6,2,1,5,2,1,4),_PerfMetricMajorThreshold_Type())
perfMetricMajorThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:perfMetricMajorThreshold.setStatus(_A)
_PerfMetricMinorThreshold_Type=Integer32
_PerfMetricMinorThreshold_Object=MibTableColumn
perfMetricMinorThreshold=_PerfMetricMinorThreshold_Object((1,3,6,1,4,1,37963,6,2,1,5,2,1,5),_PerfMetricMinorThreshold_Type())
perfMetricMinorThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:perfMetricMinorThreshold.setStatus(_A)
_PerfMetricCriticalRearm_Type=Integer32
_PerfMetricCriticalRearm_Object=MibTableColumn
perfMetricCriticalRearm=_PerfMetricCriticalRearm_Object((1,3,6,1,4,1,37963,6,2,1,5,2,1,6),_PerfMetricCriticalRearm_Type())
perfMetricCriticalRearm.setMaxAccess(_D)
if mibBuilder.loadTexts:perfMetricCriticalRearm.setStatus(_A)
_PerfMetricMajorRearm_Type=Integer32
_PerfMetricMajorRearm_Object=MibTableColumn
perfMetricMajorRearm=_PerfMetricMajorRearm_Object((1,3,6,1,4,1,37963,6,2,1,5,2,1,7),_PerfMetricMajorRearm_Type())
perfMetricMajorRearm.setMaxAccess(_D)
if mibBuilder.loadTexts:perfMetricMajorRearm.setStatus(_A)
_PerfMetricMinorRearm_Type=Integer32
_PerfMetricMinorRearm_Object=MibTableColumn
perfMetricMinorRearm=_PerfMetricMinorRearm_Object((1,3,6,1,4,1,37963,6,2,1,5,2,1,8),_PerfMetricMinorRearm_Type())
perfMetricMinorRearm.setMaxAccess(_D)
if mibBuilder.loadTexts:perfMetricMinorRearm.setStatus(_A)
_PerfMetricClearThreshold_Type=Integer32
_PerfMetricClearThreshold_Object=MibTableColumn
perfMetricClearThreshold=_PerfMetricClearThreshold_Object((1,3,6,1,4,1,37963,6,2,1,5,2,1,9),_PerfMetricClearThreshold_Type())
perfMetricClearThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:perfMetricClearThreshold.setStatus(_A)
_PerfMetricThresholdRowStatus_Type=RowStatus
_PerfMetricThresholdRowStatus_Object=MibTableColumn
perfMetricThresholdRowStatus=_PerfMetricThresholdRowStatus_Object((1,3,6,1,4,1,37963,6,2,1,5,2,1,10),_PerfMetricThresholdRowStatus_Type())
perfMetricThresholdRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:perfMetricThresholdRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'affirmedTemsObjects':affirmedTemsObjects,'temsServerSystemGroup':temsServerSystemGroup,'temsServerDetails':temsServerDetails,'temsServerId':temsServerId,'temsServerName':temsServerName,'temsServerRunningVersion':temsServerRunningVersion,'temsServerDeployedLocation':temsServerDeployedLocation,'temsServerResourceGroup':temsServerResourceGroup,'temsServerResourceTypeTable':temsServerResourceTypeTable,'temsServerResourceTypeEntry':temsServerResourceTypeEntry,_I:temsServerResourceTypeIndex,'temsServerResourceType':temsServerResourceType,'temsServerResourceTable':temsServerResourceTable,'temsServerResourceEntry':temsServerResourceEntry,_F:temsServerResourceIndex,'temsServerResourceName':temsServerResourceName,'temsServerResourceTypeId':temsServerResourceTypeId,'temsServerResourceIpAddress':temsServerResourceIpAddress,'temsServerResourceAdminStatus':temsServerResourceAdminStatus,'temsServerAlarmGroup':temsServerAlarmGroup,'temsServerActiveAlarmTable':temsServerActiveAlarmTable,'temsServerActiveAlarmEntry':temsServerActiveAlarmEntry,_J:temsServerActiveAlarmIndex,'temsServerActiveAlarmSource':temsServerActiveAlarmSource,'temsServerActiveAlarmCategory':temsServerActiveAlarmCategory,'temsServerActiveAlarmSeverity':temsServerActiveAlarmSeverity,'temsServerActiveAlarmMessage':temsServerActiveAlarmMessage,'temsServerActiveAlarmRemedy':temsServerActiveAlarmRemedy,'temsServerActiveAlarmOwner':temsServerActiveAlarmOwner,'temsServerActiveAlarmCreatedTime':temsServerActiveAlarmCreatedTime,'temsServerActiveAlarmUpdatedTime':temsServerActiveAlarmUpdatedTime,'temsServerActiveAlarmClearedTime':temsServerActiveAlarmClearedTime,'temsServerActiveAlarmAckStatus':temsServerActiveAlarmAckStatus,'temsServerActiveAlarmAckTime':temsServerActiveAlarmAckTime,'temsServerActiveAlarmAdditionalInfo':temsServerActiveAlarmAdditionalInfo,'temsServerActiveAlarmNEIndex':temsServerActiveAlarmNEIndex,'temsServerActiveAlarmNESeqNumber':temsServerActiveAlarmNESeqNumber,'temsServerActiveAlarmTrapOid':temsServerActiveAlarmTrapOid,'temsServerStatsGroup':temsServerStatsGroup,'temsServerPerfMetricsTable':temsServerPerfMetricsTable,'temsServerPerfMetricsEntry':temsServerPerfMetricsEntry,_G:temsServerPerfMetricsIndex,'temsServerPerfMetric':temsServerPerfMetric,'temsServerPerfMetricPollingInterval':temsServerPerfMetricPollingInterval,'temsServerPerfStatsTable':temsServerPerfStatsTable,'temsServerPerfStatsEntry':temsServerPerfStatsEntry,_K:temsServerPerfStatsIndex,'temsServerPerfMetricCollectedTime':temsServerPerfMetricCollectedTime,'temsServerPerfMetricCollectedValue':temsServerPerfMetricCollectedValue,'temsServerConfigGroup':temsServerConfigGroup,'temsServerSnmpManagerTable':temsServerSnmpManagerTable,'temsServerSnmpManagerEntry':temsServerSnmpManagerEntry,_L:temsServerSnmpManagerIndex,'temsServerSnmpManagerIpAddress':temsServerSnmpManagerIpAddress,'temsServerSnmpManagerTrapPort':temsServerSnmpManagerTrapPort,'temsServerSnmpManagerTrapCommunity':temsServerSnmpManagerTrapCommunity,'temsServerSnmpManagerRowStatus':temsServerSnmpManagerRowStatus,'perfMetricThresholdTable':perfMetricThresholdTable,'perfMetricThresholdEntry':perfMetricThresholdEntry,_M:perfMetricThresholdIndex,'perfMetricThresholdType':perfMetricThresholdType,'perfMetricCriticalThreshold':perfMetricCriticalThreshold,'perfMetricMajorThreshold':perfMetricMajorThreshold,'perfMetricMinorThreshold':perfMetricMinorThreshold,'perfMetricCriticalRearm':perfMetricCriticalRearm,'perfMetricMajorRearm':perfMetricMajorRearm,'perfMetricMinorRearm':perfMetricMinorRearm,'perfMetricClearThreshold':perfMetricClearThreshold,'perfMetricThresholdRowStatus':perfMetricThresholdRowStatus})