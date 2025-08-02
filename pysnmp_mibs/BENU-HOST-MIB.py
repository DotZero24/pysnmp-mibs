_K='bSWTaskDiedReason'
_J='bSWProcessAvgCPUUsageHighThreshold'
_I='bSWProcessAvgCPUUsageLowThreshold'
_H='bSWTaskIndex'
_G='Integer32'
_F='bSWProcessID'
_E='bSWProcessName'
_D='accessible-for-notify'
_C='BENU-HOST-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
benuPlatform,=mibBuilder.importSymbols('BENU-PLATFORM-MIB','benuPlatform')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bHostMIB=ModuleIdentity((1,3,6,1,4,1,39406,1,5))
if mibBuilder.loadTexts:bHostMIB.setRevisions(('2015-11-03 00:00','2015-04-28 00:00','2015-04-27 00:00','2015-01-05 00:00','2015-01-04 00:00','2014-12-17 00:00','2014-09-22 00:00','2014-03-21 00:00','2013-05-27 00:00'))
_BHostNotifObjects_ObjectIdentity=ObjectIdentity
bHostNotifObjects=_BHostNotifObjects_ObjectIdentity((1,3,6,1,4,1,39406,1,5,0))
if mibBuilder.loadTexts:bHostNotifObjects.setStatus(_A)
_BHostMIBObjects_ObjectIdentity=ObjectIdentity
bHostMIBObjects=_BHostMIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,1,5,1))
if mibBuilder.loadTexts:bHostMIBObjects.setStatus(_A)
_BSWTaskInfoTable_Object=MibTable
bSWTaskInfoTable=_BSWTaskInfoTable_Object((1,3,6,1,4,1,39406,1,5,1,1))
if mibBuilder.loadTexts:bSWTaskInfoTable.setStatus(_A)
_BSWTaskInfoEntry_Object=MibTableRow
bSWTaskInfoEntry=_BSWTaskInfoEntry_Object((1,3,6,1,4,1,39406,1,5,1,1,1))
bSWTaskInfoEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:bSWTaskInfoEntry.setStatus(_A)
_BSWTaskIndex_Type=Integer32
_BSWTaskIndex_Object=MibTableColumn
bSWTaskIndex=_BSWTaskIndex_Object((1,3,6,1,4,1,39406,1,5,1,1,1,1),_BSWTaskIndex_Type())
bSWTaskIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:bSWTaskIndex.setStatus(_A)
_BSWTaskName_Type=DisplayString
_BSWTaskName_Object=MibTableColumn
bSWTaskName=_BSWTaskName_Object((1,3,6,1,4,1,39406,1,5,1,1,1,2),_BSWTaskName_Type())
bSWTaskName.setMaxAccess(_B)
if mibBuilder.loadTexts:bSWTaskName.setStatus(_A)
_BSWTaskProcessID_Type=Unsigned32
_BSWTaskProcessID_Object=MibTableColumn
bSWTaskProcessID=_BSWTaskProcessID_Object((1,3,6,1,4,1,39406,1,5,1,1,1,3),_BSWTaskProcessID_Type())
bSWTaskProcessID.setMaxAccess(_B)
if mibBuilder.loadTexts:bSWTaskProcessID.setStatus(_A)
_BSWTaskLoadIntervalDuration_Type=Unsigned32
_BSWTaskLoadIntervalDuration_Object=MibTableColumn
bSWTaskLoadIntervalDuration=_BSWTaskLoadIntervalDuration_Object((1,3,6,1,4,1,39406,1,5,1,1,1,4),_BSWTaskLoadIntervalDuration_Type())
bSWTaskLoadIntervalDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:bSWTaskLoadIntervalDuration.setStatus(_A)
_BSWTaskRunStateTime_Type=TimeTicks
_BSWTaskRunStateTime_Object=MibTableColumn
bSWTaskRunStateTime=_BSWTaskRunStateTime_Object((1,3,6,1,4,1,39406,1,5,1,1,1,5),_BSWTaskRunStateTime_Type())
bSWTaskRunStateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bSWTaskRunStateTime.setStatus(_A)
_BSWTaskCPUUsage_Type=Unsigned32
_BSWTaskCPUUsage_Object=MibTableColumn
bSWTaskCPUUsage=_BSWTaskCPUUsage_Object((1,3,6,1,4,1,39406,1,5,1,1,1,6),_BSWTaskCPUUsage_Type())
bSWTaskCPUUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:bSWTaskCPUUsage.setStatus(_A)
_BSWTaskAvgCPUUsage_Type=Unsigned32
_BSWTaskAvgCPUUsage_Object=MibTableColumn
bSWTaskAvgCPUUsage=_BSWTaskAvgCPUUsage_Object((1,3,6,1,4,1,39406,1,5,1,1,1,7),_BSWTaskAvgCPUUsage_Type())
bSWTaskAvgCPUUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:bSWTaskAvgCPUUsage.setStatus(_A)
_BSWTaskMaxCPUUsage_Type=Unsigned32
_BSWTaskMaxCPUUsage_Object=MibTableColumn
bSWTaskMaxCPUUsage=_BSWTaskMaxCPUUsage_Object((1,3,6,1,4,1,39406,1,5,1,1,1,8),_BSWTaskMaxCPUUsage_Type())
bSWTaskMaxCPUUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:bSWTaskMaxCPUUsage.setStatus(_A)
_BSWTaskCodeSegmentSize_Type=Unsigned32
_BSWTaskCodeSegmentSize_Object=MibTableColumn
bSWTaskCodeSegmentSize=_BSWTaskCodeSegmentSize_Object((1,3,6,1,4,1,39406,1,5,1,1,1,9),_BSWTaskCodeSegmentSize_Type())
bSWTaskCodeSegmentSize.setMaxAccess(_B)
if mibBuilder.loadTexts:bSWTaskCodeSegmentSize.setStatus(_A)
_BSWTaskDataSegmentSize_Type=Unsigned32
_BSWTaskDataSegmentSize_Object=MibTableColumn
bSWTaskDataSegmentSize=_BSWTaskDataSegmentSize_Object((1,3,6,1,4,1,39406,1,5,1,1,1,10),_BSWTaskDataSegmentSize_Type())
bSWTaskDataSegmentSize.setMaxAccess(_B)
if mibBuilder.loadTexts:bSWTaskDataSegmentSize.setStatus(_A)
_BSWTaskResidentPhyMem_Type=Unsigned32
_BSWTaskResidentPhyMem_Object=MibTableColumn
bSWTaskResidentPhyMem=_BSWTaskResidentPhyMem_Object((1,3,6,1,4,1,39406,1,5,1,1,1,11),_BSWTaskResidentPhyMem_Type())
bSWTaskResidentPhyMem.setMaxAccess(_B)
if mibBuilder.loadTexts:bSWTaskResidentPhyMem.setStatus(_A)
_BSWTaskVirtMemUsage_Type=Unsigned32
_BSWTaskVirtMemUsage_Object=MibTableColumn
bSWTaskVirtMemUsage=_BSWTaskVirtMemUsage_Object((1,3,6,1,4,1,39406,1,5,1,1,1,12),_BSWTaskVirtMemUsage_Type())
bSWTaskVirtMemUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:bSWTaskVirtMemUsage.setStatus(_A)
_BSWTaskSharedMem_Type=Unsigned32
_BSWTaskSharedMem_Object=MibTableColumn
bSWTaskSharedMem=_BSWTaskSharedMem_Object((1,3,6,1,4,1,39406,1,5,1,1,1,13),_BSWTaskSharedMem_Type())
bSWTaskSharedMem.setMaxAccess(_B)
if mibBuilder.loadTexts:bSWTaskSharedMem.setStatus(_A)
_BSWTaskVirtMemPeakUsage_Type=Unsigned32
_BSWTaskVirtMemPeakUsage_Object=MibTableColumn
bSWTaskVirtMemPeakUsage=_BSWTaskVirtMemPeakUsage_Object((1,3,6,1,4,1,39406,1,5,1,1,1,14),_BSWTaskVirtMemPeakUsage_Type())
bSWTaskVirtMemPeakUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:bSWTaskVirtMemPeakUsage.setStatus(_A)
_BSWTaskAvgCPUUsageHighThreshold_Type=Unsigned32
_BSWTaskAvgCPUUsageHighThreshold_Object=MibTableColumn
bSWTaskAvgCPUUsageHighThreshold=_BSWTaskAvgCPUUsageHighThreshold_Object((1,3,6,1,4,1,39406,1,5,1,1,1,15),_BSWTaskAvgCPUUsageHighThreshold_Type())
bSWTaskAvgCPUUsageHighThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:bSWTaskAvgCPUUsageHighThreshold.setStatus(_A)
_BSWTaskAvgCPUUsageLowThreshold_Type=Unsigned32
_BSWTaskAvgCPUUsageLowThreshold_Object=MibTableColumn
bSWTaskAvgCPUUsageLowThreshold=_BSWTaskAvgCPUUsageLowThreshold_Object((1,3,6,1,4,1,39406,1,5,1,1,1,16),_BSWTaskAvgCPUUsageLowThreshold_Type())
bSWTaskAvgCPUUsageLowThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:bSWTaskAvgCPUUsageLowThreshold.setStatus(_A)
_BSWTaskCPUUsageLimit_Type=Unsigned32
_BSWTaskCPUUsageLimit_Object=MibTableColumn
bSWTaskCPUUsageLimit=_BSWTaskCPUUsageLimit_Object((1,3,6,1,4,1,39406,1,5,1,1,1,17),_BSWTaskCPUUsageLimit_Type())
bSWTaskCPUUsageLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:bSWTaskCPUUsageLimit.setStatus(_A)
_BSWTaskRestartLimit_Type=Unsigned32
_BSWTaskRestartLimit_Object=MibTableColumn
bSWTaskRestartLimit=_BSWTaskRestartLimit_Object((1,3,6,1,4,1,39406,1,5,1,1,1,18),_BSWTaskRestartLimit_Type())
bSWTaskRestartLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:bSWTaskRestartLimit.setStatus(_A)
class _BSWTaskRestartability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_BSWTaskRestartability_Type.__name__=_G
_BSWTaskRestartability_Object=MibTableColumn
bSWTaskRestartability=_BSWTaskRestartability_Object((1,3,6,1,4,1,39406,1,5,1,1,1,19),_BSWTaskRestartability_Type())
bSWTaskRestartability.setMaxAccess(_B)
if mibBuilder.loadTexts:bSWTaskRestartability.setStatus(_A)
_BSWTaskRestartCount_Type=Unsigned32
_BSWTaskRestartCount_Object=MibTableColumn
bSWTaskRestartCount=_BSWTaskRestartCount_Object((1,3,6,1,4,1,39406,1,5,1,1,1,20),_BSWTaskRestartCount_Type())
bSWTaskRestartCount.setMaxAccess(_B)
if mibBuilder.loadTexts:bSWTaskRestartCount.setStatus(_A)
_BSysTotalMem_Type=Unsigned32
_BSysTotalMem_Object=MibScalar
bSysTotalMem=_BSysTotalMem_Object((1,3,6,1,4,1,39406,1,5,1,2),_BSysTotalMem_Type())
bSysTotalMem.setMaxAccess(_B)
if mibBuilder.loadTexts:bSysTotalMem.setStatus(_A)
_BSysMemUsed_Type=Unsigned32
_BSysMemUsed_Object=MibScalar
bSysMemUsed=_BSysMemUsed_Object((1,3,6,1,4,1,39406,1,5,1,3),_BSysMemUsed_Type())
bSysMemUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:bSysMemUsed.setStatus(_A)
_BSysMemFree_Type=Unsigned32
_BSysMemFree_Object=MibScalar
bSysMemFree=_BSysMemFree_Object((1,3,6,1,4,1,39406,1,5,1,4),_BSysMemFree_Type())
bSysMemFree.setMaxAccess(_B)
if mibBuilder.loadTexts:bSysMemFree.setStatus(_A)
_BSysTotalCPUUtilAvailable_Type=Unsigned32
_BSysTotalCPUUtilAvailable_Object=MibScalar
bSysTotalCPUUtilAvailable=_BSysTotalCPUUtilAvailable_Object((1,3,6,1,4,1,39406,1,5,1,5),_BSysTotalCPUUtilAvailable_Type())
bSysTotalCPUUtilAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:bSysTotalCPUUtilAvailable.setStatus(_A)
_BSysAvgCPUUtil15Sec_Type=Unsigned32
_BSysAvgCPUUtil15Sec_Object=MibScalar
bSysAvgCPUUtil15Sec=_BSysAvgCPUUtil15Sec_Object((1,3,6,1,4,1,39406,1,5,1,6),_BSysAvgCPUUtil15Sec_Type())
bSysAvgCPUUtil15Sec.setMaxAccess(_B)
if mibBuilder.loadTexts:bSysAvgCPUUtil15Sec.setStatus(_A)
_BSysAvgCPUUtil1Min_Type=Unsigned32
_BSysAvgCPUUtil1Min_Object=MibScalar
bSysAvgCPUUtil1Min=_BSysAvgCPUUtil1Min_Object((1,3,6,1,4,1,39406,1,5,1,7),_BSysAvgCPUUtil1Min_Type())
bSysAvgCPUUtil1Min.setMaxAccess(_B)
if mibBuilder.loadTexts:bSysAvgCPUUtil1Min.setStatus(_A)
_BSysAvgCPUUtil5Min_Type=Unsigned32
_BSysAvgCPUUtil5Min_Object=MibScalar
bSysAvgCPUUtil5Min=_BSysAvgCPUUtil5Min_Object((1,3,6,1,4,1,39406,1,5,1,8),_BSysAvgCPUUtil5Min_Type())
bSysAvgCPUUtil5Min.setMaxAccess(_B)
if mibBuilder.loadTexts:bSysAvgCPUUtil5Min.setStatus(_A)
_BCPUMonInterval_Type=Unsigned32
_BCPUMonInterval_Object=MibScalar
bCPUMonInterval=_BCPUMonInterval_Object((1,3,6,1,4,1,39406,1,5,1,9),_BCPUMonInterval_Type())
bCPUMonInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:bCPUMonInterval.setStatus(_A)
if mibBuilder.loadTexts:bCPUMonInterval.setUnits('seconds')
_BHostNotifVariables_ObjectIdentity=ObjectIdentity
bHostNotifVariables=_BHostNotifVariables_ObjectIdentity((1,3,6,1,4,1,39406,1,5,2))
if mibBuilder.loadTexts:bHostNotifVariables.setStatus(_A)
class _BSWTaskDiedReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cpuUsageLimitReached',1),('unKnown',2)))
_BSWTaskDiedReason_Type.__name__=_G
_BSWTaskDiedReason_Object=MibScalar
bSWTaskDiedReason=_BSWTaskDiedReason_Object((1,3,6,1,4,1,39406,1,5,2,1),_BSWTaskDiedReason_Type())
bSWTaskDiedReason.setMaxAccess(_D)
if mibBuilder.loadTexts:bSWTaskDiedReason.setStatus(_A)
_BSWProcessName_Type=DisplayString
_BSWProcessName_Object=MibScalar
bSWProcessName=_BSWProcessName_Object((1,3,6,1,4,1,39406,1,5,2,2),_BSWProcessName_Type())
bSWProcessName.setMaxAccess(_D)
if mibBuilder.loadTexts:bSWProcessName.setStatus(_A)
_BSWProcessID_Type=Unsigned32
_BSWProcessID_Object=MibScalar
bSWProcessID=_BSWProcessID_Object((1,3,6,1,4,1,39406,1,5,2,3),_BSWProcessID_Type())
bSWProcessID.setMaxAccess(_D)
if mibBuilder.loadTexts:bSWProcessID.setStatus(_A)
_BSWProcessAvgCPUUsageLowThreshold_Type=Unsigned32
_BSWProcessAvgCPUUsageLowThreshold_Object=MibScalar
bSWProcessAvgCPUUsageLowThreshold=_BSWProcessAvgCPUUsageLowThreshold_Object((1,3,6,1,4,1,39406,1,5,2,4),_BSWProcessAvgCPUUsageLowThreshold_Type())
bSWProcessAvgCPUUsageLowThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:bSWProcessAvgCPUUsageLowThreshold.setStatus(_A)
_BSWProcessAvgCPUUsageHighThreshold_Type=Unsigned32
_BSWProcessAvgCPUUsageHighThreshold_Object=MibScalar
bSWProcessAvgCPUUsageHighThreshold=_BSWProcessAvgCPUUsageHighThreshold_Object((1,3,6,1,4,1,39406,1,5,2,5),_BSWProcessAvgCPUUsageHighThreshold_Type())
bSWProcessAvgCPUUsageHighThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:bSWProcessAvgCPUUsageHighThreshold.setStatus(_A)
bSWTaskAvgCPUUsageLow=NotificationType((1,3,6,1,4,1,39406,1,5,0,1))
bSWTaskAvgCPUUsageLow.setObjects(*((_C,_E),(_C,_F),(_C,_I)))
if mibBuilder.loadTexts:bSWTaskAvgCPUUsageLow.setStatus(_A)
bSWTaskAvgCPUUsageHigh=NotificationType((1,3,6,1,4,1,39406,1,5,0,2))
bSWTaskAvgCPUUsageHigh.setObjects(*((_C,_E),(_C,_F),(_C,_J)))
if mibBuilder.loadTexts:bSWTaskAvgCPUUsageHigh.setStatus(_A)
bSWTaskDied=NotificationType((1,3,6,1,4,1,39406,1,5,0,3))
bSWTaskDied.setObjects(*((_C,_E),(_C,_F),(_C,_K)))
if mibBuilder.loadTexts:bSWTaskDied.setStatus(_A)
bSWTaskRestartLimitReached=NotificationType((1,3,6,1,4,1,39406,1,5,0,4))
bSWTaskRestartLimitReached.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:bSWTaskRestartLimitReached.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'bHostMIB':bHostMIB,'bHostNotifObjects':bHostNotifObjects,'bSWTaskAvgCPUUsageLow':bSWTaskAvgCPUUsageLow,'bSWTaskAvgCPUUsageHigh':bSWTaskAvgCPUUsageHigh,'bSWTaskDied':bSWTaskDied,'bSWTaskRestartLimitReached':bSWTaskRestartLimitReached,'bHostMIBObjects':bHostMIBObjects,'bSWTaskInfoTable':bSWTaskInfoTable,'bSWTaskInfoEntry':bSWTaskInfoEntry,_H:bSWTaskIndex,'bSWTaskName':bSWTaskName,'bSWTaskProcessID':bSWTaskProcessID,'bSWTaskLoadIntervalDuration':bSWTaskLoadIntervalDuration,'bSWTaskRunStateTime':bSWTaskRunStateTime,'bSWTaskCPUUsage':bSWTaskCPUUsage,'bSWTaskAvgCPUUsage':bSWTaskAvgCPUUsage,'bSWTaskMaxCPUUsage':bSWTaskMaxCPUUsage,'bSWTaskCodeSegmentSize':bSWTaskCodeSegmentSize,'bSWTaskDataSegmentSize':bSWTaskDataSegmentSize,'bSWTaskResidentPhyMem':bSWTaskResidentPhyMem,'bSWTaskVirtMemUsage':bSWTaskVirtMemUsage,'bSWTaskSharedMem':bSWTaskSharedMem,'bSWTaskVirtMemPeakUsage':bSWTaskVirtMemPeakUsage,'bSWTaskAvgCPUUsageHighThreshold':bSWTaskAvgCPUUsageHighThreshold,'bSWTaskAvgCPUUsageLowThreshold':bSWTaskAvgCPUUsageLowThreshold,'bSWTaskCPUUsageLimit':bSWTaskCPUUsageLimit,'bSWTaskRestartLimit':bSWTaskRestartLimit,'bSWTaskRestartability':bSWTaskRestartability,'bSWTaskRestartCount':bSWTaskRestartCount,'bSysTotalMem':bSysTotalMem,'bSysMemUsed':bSysMemUsed,'bSysMemFree':bSysMemFree,'bSysTotalCPUUtilAvailable':bSysTotalCPUUtilAvailable,'bSysAvgCPUUtil15Sec':bSysAvgCPUUtil15Sec,'bSysAvgCPUUtil1Min':bSysAvgCPUUtil1Min,'bSysAvgCPUUtil5Min':bSysAvgCPUUtil5Min,'bCPUMonInterval':bCPUMonInterval,'bHostNotifVariables':bHostNotifVariables,_K:bSWTaskDiedReason,_E:bSWProcessName,_F:bSWProcessID,_I:bSWProcessAvgCPUUsageLowThreshold,_J:bSWProcessAvgCPUUsageHighThreshold})