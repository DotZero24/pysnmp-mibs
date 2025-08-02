_X='zxAnPmLogCtrlMetricInstIndex'
_W='zxAnPmLogCtrlMetric'
_V='zxAnPmHisMetricInstIndex'
_U='zxAnPmHisMetric'
_T='zxAnPmCtrlIndex'
_S='zxAnPmFallingAlarmThreshold'
_R='zxAnPmRisingAlarmThreshold'
_Q='zxAnPmFallingWarningThreshold'
_P='zxAnPmRisingWarningThreshold'
_O='disable'
_N='enable'
_M='DisplayString'
_L='read-only'
_K='zxAnPmCtrlSamplingType'
_J='zxAnPmCtrlStatisticalInterval'
_I='zxAnPmHisStatisticalValue'
_H='zxAnPmThresholdMetric'
_G='zxAnPmThresholdMetricInstIndex'
_F='not-accessible'
_E='read-write'
_D='Integer32'
_C='read-create'
_B='ZTE-AN-PERF-MGMT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_M,'PhysAddress','RowStatus','TextualConvention','TruthValue')
zxAn,=mibBuilder.importSymbols('ZTE-AN-TC-MIB','zxAn')
zxAnPerfMgmtMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,189))
_ZxAnPerfMgmtObjects_ObjectIdentity=ObjectIdentity
zxAnPerfMgmtObjects=_ZxAnPerfMgmtObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,189,1))
_ZxAnPmCtrlTable_Object=MibTable
zxAnPmCtrlTable=_ZxAnPmCtrlTable_Object((1,3,6,1,4,1,3902,1015,189,1,1))
if mibBuilder.loadTexts:zxAnPmCtrlTable.setStatus(_A)
_ZxAnPmCtrlEntry_Object=MibTableRow
zxAnPmCtrlEntry=_ZxAnPmCtrlEntry_Object((1,3,6,1,4,1,3902,1015,189,1,1,1))
zxAnPmCtrlEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:zxAnPmCtrlEntry.setStatus(_A)
_ZxAnPmCtrlIndex_Type=Integer32
_ZxAnPmCtrlIndex_Object=MibTableColumn
zxAnPmCtrlIndex=_ZxAnPmCtrlIndex_Object((1,3,6,1,4,1,3902,1015,189,1,1,1,1),_ZxAnPmCtrlIndex_Type())
zxAnPmCtrlIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnPmCtrlIndex.setStatus(_A)
_ZxAnPmCtrlDesc_Type=DisplayString
_ZxAnPmCtrlDesc_Object=MibTableColumn
zxAnPmCtrlDesc=_ZxAnPmCtrlDesc_Object((1,3,6,1,4,1,3902,1015,189,1,1,1,2),_ZxAnPmCtrlDesc_Type())
zxAnPmCtrlDesc.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPmCtrlDesc.setStatus(_A)
_ZxAnPmCtrlMetric_Type=ObjectIdentifier
_ZxAnPmCtrlMetric_Object=MibTableColumn
zxAnPmCtrlMetric=_ZxAnPmCtrlMetric_Object((1,3,6,1,4,1,3902,1015,189,1,1,1,3),_ZxAnPmCtrlMetric_Type())
zxAnPmCtrlMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPmCtrlMetric.setStatus(_A)
_ZxAnPmCtrlMetricInstIndex_Type=ObjectIdentifier
_ZxAnPmCtrlMetricInstIndex_Object=MibTableColumn
zxAnPmCtrlMetricInstIndex=_ZxAnPmCtrlMetricInstIndex_Object((1,3,6,1,4,1,3902,1015,189,1,1,1,4),_ZxAnPmCtrlMetricInstIndex_Type())
zxAnPmCtrlMetricInstIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPmCtrlMetricInstIndex.setStatus(_A)
class _ZxAnPmCtrlAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('start',1),('stop',2),('resetCounter',3)))
_ZxAnPmCtrlAdminStatus_Type.__name__=_D
_ZxAnPmCtrlAdminStatus_Object=MibTableColumn
zxAnPmCtrlAdminStatus=_ZxAnPmCtrlAdminStatus_Object((1,3,6,1,4,1,3902,1015,189,1,1,1,5),_ZxAnPmCtrlAdminStatus_Type())
zxAnPmCtrlAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPmCtrlAdminStatus.setStatus(_A)
class _ZxAnPmCtrlBucketsRequested_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ZxAnPmCtrlBucketsRequested_Type.__name__=_D
_ZxAnPmCtrlBucketsRequested_Object=MibTableColumn
zxAnPmCtrlBucketsRequested=_ZxAnPmCtrlBucketsRequested_Object((1,3,6,1,4,1,3902,1015,189,1,1,1,6),_ZxAnPmCtrlBucketsRequested_Type())
zxAnPmCtrlBucketsRequested.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPmCtrlBucketsRequested.setStatus(_A)
class _ZxAnPmCtrlBucketsGranted_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ZxAnPmCtrlBucketsGranted_Type.__name__=_D
_ZxAnPmCtrlBucketsGranted_Object=MibTableColumn
zxAnPmCtrlBucketsGranted=_ZxAnPmCtrlBucketsGranted_Object((1,3,6,1,4,1,3902,1015,189,1,1,1,7),_ZxAnPmCtrlBucketsGranted_Type())
zxAnPmCtrlBucketsGranted.setMaxAccess(_L)
if mibBuilder.loadTexts:zxAnPmCtrlBucketsGranted.setStatus(_A)
class _ZxAnPmCtrlSamplingInterval_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_ZxAnPmCtrlSamplingInterval_Type.__name__=_D
_ZxAnPmCtrlSamplingInterval_Object=MibTableColumn
zxAnPmCtrlSamplingInterval=_ZxAnPmCtrlSamplingInterval_Object((1,3,6,1,4,1,3902,1015,189,1,1,1,8),_ZxAnPmCtrlSamplingInterval_Type())
zxAnPmCtrlSamplingInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPmCtrlSamplingInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnPmCtrlSamplingInterval.setUnits('Seconds')
_ZxAnPmCtrlRowStatus_Type=RowStatus
_ZxAnPmCtrlRowStatus_Object=MibTableColumn
zxAnPmCtrlRowStatus=_ZxAnPmCtrlRowStatus_Object((1,3,6,1,4,1,3902,1015,189,1,1,1,9),_ZxAnPmCtrlRowStatus_Type())
zxAnPmCtrlRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPmCtrlRowStatus.setStatus(_A)
class _ZxAnPmCtrlSamplingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('absoluteValue',1),('deltaValue',2)))
_ZxAnPmCtrlSamplingType_Type.__name__=_D
_ZxAnPmCtrlSamplingType_Object=MibTableColumn
zxAnPmCtrlSamplingType=_ZxAnPmCtrlSamplingType_Object((1,3,6,1,4,1,3902,1015,189,1,1,1,10),_ZxAnPmCtrlSamplingType_Type())
zxAnPmCtrlSamplingType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPmCtrlSamplingType.setStatus(_A)
class _ZxAnPmCtrlStatisticalInterval_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_ZxAnPmCtrlStatisticalInterval_Type.__name__=_D
_ZxAnPmCtrlStatisticalInterval_Object=MibTableColumn
zxAnPmCtrlStatisticalInterval=_ZxAnPmCtrlStatisticalInterval_Object((1,3,6,1,4,1,3902,1015,189,1,1,1,11),_ZxAnPmCtrlStatisticalInterval_Type())
zxAnPmCtrlStatisticalInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPmCtrlStatisticalInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnPmCtrlStatisticalInterval.setUnits('Minutes')
_ZxAnPmSpareIndex_Type=Integer32
_ZxAnPmSpareIndex_Object=MibScalar
zxAnPmSpareIndex=_ZxAnPmSpareIndex_Object((1,3,6,1,4,1,3902,1015,189,1,2),_ZxAnPmSpareIndex_Type())
zxAnPmSpareIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:zxAnPmSpareIndex.setStatus(_A)
_ZxAnPmHisTable_Object=MibTable
zxAnPmHisTable=_ZxAnPmHisTable_Object((1,3,6,1,4,1,3902,1015,189,1,31))
if mibBuilder.loadTexts:zxAnPmHisTable.setStatus(_A)
_ZxAnPmHisEntry_Object=MibTableRow
zxAnPmHisEntry=_ZxAnPmHisEntry_Object((1,3,6,1,4,1,3902,1015,189,1,31,1))
zxAnPmHisEntry.setIndexNames((0,_B,_U),(0,_B,_V))
if mibBuilder.loadTexts:zxAnPmHisEntry.setStatus(_A)
_ZxAnPmHisMetric_Type=ObjectIdentifier
_ZxAnPmHisMetric_Object=MibTableColumn
zxAnPmHisMetric=_ZxAnPmHisMetric_Object((1,3,6,1,4,1,3902,1015,189,1,31,1,1),_ZxAnPmHisMetric_Type())
zxAnPmHisMetric.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnPmHisMetric.setStatus(_A)
_ZxAnPmHisMetricInstIndex_Type=ObjectIdentifier
_ZxAnPmHisMetricInstIndex_Object=MibTableColumn
zxAnPmHisMetricInstIndex=_ZxAnPmHisMetricInstIndex_Object((1,3,6,1,4,1,3902,1015,189,1,31,1,2),_ZxAnPmHisMetricInstIndex_Type())
zxAnPmHisMetricInstIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnPmHisMetricInstIndex.setStatus(_A)
_ZxAnPmHisStatisticalValue_Type=Counter64
_ZxAnPmHisStatisticalValue_Object=MibTableColumn
zxAnPmHisStatisticalValue=_ZxAnPmHisStatisticalValue_Object((1,3,6,1,4,1,3902,1015,189,1,31,1,3),_ZxAnPmHisStatisticalValue_Type())
zxAnPmHisStatisticalValue.setMaxAccess(_L)
if mibBuilder.loadTexts:zxAnPmHisStatisticalValue.setStatus(_A)
_ZxAnPmThresholdTable_Object=MibTable
zxAnPmThresholdTable=_ZxAnPmThresholdTable_Object((1,3,6,1,4,1,3902,1015,189,1,32))
if mibBuilder.loadTexts:zxAnPmThresholdTable.setStatus(_A)
_ZxAnPmThresholdEntry_Object=MibTableRow
zxAnPmThresholdEntry=_ZxAnPmThresholdEntry_Object((1,3,6,1,4,1,3902,1015,189,1,32,1))
zxAnPmThresholdEntry.setIndexNames((0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:zxAnPmThresholdEntry.setStatus(_A)
_ZxAnPmThresholdMetricInstIndex_Type=ObjectIdentifier
_ZxAnPmThresholdMetricInstIndex_Object=MibTableColumn
zxAnPmThresholdMetricInstIndex=_ZxAnPmThresholdMetricInstIndex_Object((1,3,6,1,4,1,3902,1015,189,1,32,1,1),_ZxAnPmThresholdMetricInstIndex_Type())
zxAnPmThresholdMetricInstIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnPmThresholdMetricInstIndex.setStatus(_A)
_ZxAnPmThresholdMetric_Type=ObjectIdentifier
_ZxAnPmThresholdMetric_Object=MibTableColumn
zxAnPmThresholdMetric=_ZxAnPmThresholdMetric_Object((1,3,6,1,4,1,3902,1015,189,1,32,1,2),_ZxAnPmThresholdMetric_Type())
zxAnPmThresholdMetric.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnPmThresholdMetric.setStatus(_A)
class _ZxAnPmEventTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_ZxAnPmEventTrapEnable_Type.__name__=_D
_ZxAnPmEventTrapEnable_Object=MibTableColumn
zxAnPmEventTrapEnable=_ZxAnPmEventTrapEnable_Object((1,3,6,1,4,1,3902,1015,189,1,32,1,3),_ZxAnPmEventTrapEnable_Type())
zxAnPmEventTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPmEventTrapEnable.setStatus(_A)
_ZxAnPmRisingWarningThreshold_Type=Counter64
_ZxAnPmRisingWarningThreshold_Object=MibTableColumn
zxAnPmRisingWarningThreshold=_ZxAnPmRisingWarningThreshold_Object((1,3,6,1,4,1,3902,1015,189,1,32,1,4),_ZxAnPmRisingWarningThreshold_Type())
zxAnPmRisingWarningThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPmRisingWarningThreshold.setStatus(_A)
_ZxAnPmRisingAlarmThreshold_Type=Counter64
_ZxAnPmRisingAlarmThreshold_Object=MibTableColumn
zxAnPmRisingAlarmThreshold=_ZxAnPmRisingAlarmThreshold_Object((1,3,6,1,4,1,3902,1015,189,1,32,1,5),_ZxAnPmRisingAlarmThreshold_Type())
zxAnPmRisingAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPmRisingAlarmThreshold.setStatus(_A)
_ZxAnPmFallingWarningThreshold_Type=Counter64
_ZxAnPmFallingWarningThreshold_Object=MibTableColumn
zxAnPmFallingWarningThreshold=_ZxAnPmFallingWarningThreshold_Object((1,3,6,1,4,1,3902,1015,189,1,32,1,6),_ZxAnPmFallingWarningThreshold_Type())
zxAnPmFallingWarningThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPmFallingWarningThreshold.setStatus(_A)
_ZxAnPmFallingAlarmThreshold_Type=Counter64
_ZxAnPmFallingAlarmThreshold_Object=MibTableColumn
zxAnPmFallingAlarmThreshold=_ZxAnPmFallingAlarmThreshold_Object((1,3,6,1,4,1,3902,1015,189,1,32,1,7),_ZxAnPmFallingAlarmThreshold_Type())
zxAnPmFallingAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPmFallingAlarmThreshold.setStatus(_A)
_ZxAnPmThresholdRowStatus_Type=RowStatus
_ZxAnPmThresholdRowStatus_Object=MibTableColumn
zxAnPmThresholdRowStatus=_ZxAnPmThresholdRowStatus_Object((1,3,6,1,4,1,3902,1015,189,1,32,1,31),_ZxAnPmThresholdRowStatus_Type())
zxAnPmThresholdRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPmThresholdRowStatus.setStatus(_A)
_ZxAnPerfLogMgmtObjects_ObjectIdentity=ObjectIdentity
zxAnPerfLogMgmtObjects=_ZxAnPerfLogMgmtObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,189,2))
class _ZxAnPmLogAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_ZxAnPmLogAdminStatus_Type.__name__=_D
_ZxAnPmLogAdminStatus_Object=MibScalar
zxAnPmLogAdminStatus=_ZxAnPmLogAdminStatus_Object((1,3,6,1,4,1,3902,1015,189,2,1),_ZxAnPmLogAdminStatus_Type())
zxAnPmLogAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPmLogAdminStatus.setStatus(_A)
_ZxAnPmLogMaxRecordRows_Type=Integer32
_ZxAnPmLogMaxRecordRows_Object=MibScalar
zxAnPmLogMaxRecordRows=_ZxAnPmLogMaxRecordRows_Object((1,3,6,1,4,1,3902,1015,189,2,2),_ZxAnPmLogMaxRecordRows_Type())
zxAnPmLogMaxRecordRows.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPmLogMaxRecordRows.setStatus(_A)
class _ZxAnPmLogManualReportAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('report',1))
_ZxAnPmLogManualReportAction_Type.__name__=_D
_ZxAnPmLogManualReportAction_Object=MibScalar
zxAnPmLogManualReportAction=_ZxAnPmLogManualReportAction_Object((1,3,6,1,4,1,3902,1015,189,2,3),_ZxAnPmLogManualReportAction_Type())
zxAnPmLogManualReportAction.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPmLogManualReportAction.setStatus(_A)
_ZxAnPmLogManualReportStatus_Type=TruthValue
_ZxAnPmLogManualReportStatus_Object=MibScalar
zxAnPmLogManualReportStatus=_ZxAnPmLogManualReportStatus_Object((1,3,6,1,4,1,3902,1015,189,2,4),_ZxAnPmLogManualReportStatus_Type())
zxAnPmLogManualReportStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:zxAnPmLogManualReportStatus.setStatus(_A)
_ZxAnPmLogAutoReportMetric_Type=TruthValue
_ZxAnPmLogAutoReportMetric_Object=MibScalar
zxAnPmLogAutoReportMetric=_ZxAnPmLogAutoReportMetric_Object((1,3,6,1,4,1,3902,1015,189,2,5),_ZxAnPmLogAutoReportMetric_Type())
zxAnPmLogAutoReportMetric.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPmLogAutoReportMetric.setStatus(_A)
_ZxAnPmLogAutoReportInterval_Type=Integer32
_ZxAnPmLogAutoReportInterval_Object=MibScalar
zxAnPmLogAutoReportInterval=_ZxAnPmLogAutoReportInterval_Object((1,3,6,1,4,1,3902,1015,189,2,6),_ZxAnPmLogAutoReportInterval_Type())
zxAnPmLogAutoReportInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPmLogAutoReportInterval.setStatus(_A)
if mibBuilder.loadTexts:zxAnPmLogAutoReportInterval.setUnits('Minute')
_ZxAnPmLogReportFtpHost_Type=DisplayString
_ZxAnPmLogReportFtpHost_Object=MibScalar
zxAnPmLogReportFtpHost=_ZxAnPmLogReportFtpHost_Object((1,3,6,1,4,1,3902,1015,189,2,7),_ZxAnPmLogReportFtpHost_Type())
zxAnPmLogReportFtpHost.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPmLogReportFtpHost.setStatus(_A)
_ZxAnPmLogReportFtpPath_Type=DisplayString
_ZxAnPmLogReportFtpPath_Object=MibScalar
zxAnPmLogReportFtpPath=_ZxAnPmLogReportFtpPath_Object((1,3,6,1,4,1,3902,1015,189,2,8),_ZxAnPmLogReportFtpPath_Type())
zxAnPmLogReportFtpPath.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPmLogReportFtpPath.setStatus(_A)
_ZxAnPmLogReportFtpUser_Type=DisplayString
_ZxAnPmLogReportFtpUser_Object=MibScalar
zxAnPmLogReportFtpUser=_ZxAnPmLogReportFtpUser_Object((1,3,6,1,4,1,3902,1015,189,2,9),_ZxAnPmLogReportFtpUser_Type())
zxAnPmLogReportFtpUser.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPmLogReportFtpUser.setStatus(_A)
_ZxAnPmLogReportFtpPassword_Type=DisplayString
_ZxAnPmLogReportFtpPassword_Object=MibScalar
zxAnPmLogReportFtpPassword=_ZxAnPmLogReportFtpPassword_Object((1,3,6,1,4,1,3902,1015,189,2,10),_ZxAnPmLogReportFtpPassword_Type())
zxAnPmLogReportFtpPassword.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPmLogReportFtpPassword.setStatus(_A)
_ZxAnPmLogCtrlTable_Object=MibTable
zxAnPmLogCtrlTable=_ZxAnPmLogCtrlTable_Object((1,3,6,1,4,1,3902,1015,189,2,31))
if mibBuilder.loadTexts:zxAnPmLogCtrlTable.setStatus(_A)
_ZxAnPmLogCtrlEntry_Object=MibTableRow
zxAnPmLogCtrlEntry=_ZxAnPmLogCtrlEntry_Object((1,3,6,1,4,1,3902,1015,189,2,31,1))
zxAnPmLogCtrlEntry.setIndexNames((0,_B,_W),(0,_B,_X))
if mibBuilder.loadTexts:zxAnPmLogCtrlEntry.setStatus(_A)
_ZxAnPmLogCtrlMetric_Type=ObjectIdentifier
_ZxAnPmLogCtrlMetric_Object=MibTableColumn
zxAnPmLogCtrlMetric=_ZxAnPmLogCtrlMetric_Object((1,3,6,1,4,1,3902,1015,189,2,31,1,1),_ZxAnPmLogCtrlMetric_Type())
zxAnPmLogCtrlMetric.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnPmLogCtrlMetric.setStatus(_A)
_ZxAnPmLogCtrlMetricInstIndex_Type=ObjectIdentifier
_ZxAnPmLogCtrlMetricInstIndex_Object=MibTableColumn
zxAnPmLogCtrlMetricInstIndex=_ZxAnPmLogCtrlMetricInstIndex_Object((1,3,6,1,4,1,3902,1015,189,2,31,1,2),_ZxAnPmLogCtrlMetricInstIndex_Type())
zxAnPmLogCtrlMetricInstIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnPmLogCtrlMetricInstIndex.setStatus(_A)
class _ZxAnPmLoggingMetricAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_O,2)))
_ZxAnPmLoggingMetricAdminStatus_Type.__name__=_D
_ZxAnPmLoggingMetricAdminStatus_Object=MibTableColumn
zxAnPmLoggingMetricAdminStatus=_ZxAnPmLoggingMetricAdminStatus_Object((1,3,6,1,4,1,3902,1015,189,2,31,1,3),_ZxAnPmLoggingMetricAdminStatus_Type())
zxAnPmLoggingMetricAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPmLoggingMetricAdminStatus.setStatus(_A)
_ZxAnPmLogCtrlRowStatus_Type=RowStatus
_ZxAnPmLogCtrlRowStatus_Object=MibTableColumn
zxAnPmLogCtrlRowStatus=_ZxAnPmLogCtrlRowStatus_Object((1,3,6,1,4,1,3902,1015,189,2,31,1,31),_ZxAnPmLogCtrlRowStatus_Type())
zxAnPmLogCtrlRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnPmLogCtrlRowStatus.setStatus(_A)
_ZxAnPerfFileMgmtObjects_ObjectIdentity=ObjectIdentity
zxAnPerfFileMgmtObjects=_ZxAnPerfFileMgmtObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,189,3))
_ZxAnPerfRetrievalControlObjects_ObjectIdentity=ObjectIdentity
zxAnPerfRetrievalControlObjects=_ZxAnPerfRetrievalControlObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,189,3,1))
class _ZxAnPerfRetrievalTimeGranularity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('for15Minutes',1),('for24Hours',2)))
_ZxAnPerfRetrievalTimeGranularity_Type.__name__=_D
_ZxAnPerfRetrievalTimeGranularity_Object=MibScalar
zxAnPerfRetrievalTimeGranularity=_ZxAnPerfRetrievalTimeGranularity_Object((1,3,6,1,4,1,3902,1015,189,3,1,1),_ZxAnPerfRetrievalTimeGranularity_Type())
zxAnPerfRetrievalTimeGranularity.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPerfRetrievalTimeGranularity.setStatus(_A)
class _ZxAnPerfRetrievalStartTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_ZxAnPerfRetrievalStartTime_Type.__name__=_M
_ZxAnPerfRetrievalStartTime_Object=MibScalar
zxAnPerfRetrievalStartTime=_ZxAnPerfRetrievalStartTime_Object((1,3,6,1,4,1,3902,1015,189,3,1,2),_ZxAnPerfRetrievalStartTime_Type())
zxAnPerfRetrievalStartTime.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPerfRetrievalStartTime.setStatus(_A)
class _ZxAnPerfRetrievalEndTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_ZxAnPerfRetrievalEndTime_Type.__name__=_M
_ZxAnPerfRetrievalEndTime_Object=MibScalar
zxAnPerfRetrievalEndTime=_ZxAnPerfRetrievalEndTime_Object((1,3,6,1,4,1,3902,1015,189,3,1,3),_ZxAnPerfRetrievalEndTime_Type())
zxAnPerfRetrievalEndTime.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnPerfRetrievalEndTime.setStatus(_A)
_ZxAnPerfMgmtTrapObjects_ObjectIdentity=ObjectIdentity
zxAnPerfMgmtTrapObjects=_ZxAnPerfMgmtTrapObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,189,100))
zxAnPmMetricOverWarning=NotificationType((1,3,6,1,4,1,3902,1015,189,100,1))
zxAnPmMetricOverWarning.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:zxAnPmMetricOverWarning.setStatus(_A)
zxAnPmMetricOverWarningRestore=NotificationType((1,3,6,1,4,1,3902,1015,189,100,2))
zxAnPmMetricOverWarningRestore.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:zxAnPmMetricOverWarningRestore.setStatus(_A)
zxAnPmMetricOverAlarm=NotificationType((1,3,6,1,4,1,3902,1015,189,100,3))
zxAnPmMetricOverAlarm.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:zxAnPmMetricOverAlarm.setStatus(_A)
zxAnPmMetricOverAlarmRestore=NotificationType((1,3,6,1,4,1,3902,1015,189,100,4))
zxAnPmMetricOverAlarmRestore.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:zxAnPmMetricOverAlarmRestore.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zxAnPerfMgmtMib':zxAnPerfMgmtMib,'zxAnPerfMgmtObjects':zxAnPerfMgmtObjects,'zxAnPmCtrlTable':zxAnPmCtrlTable,'zxAnPmCtrlEntry':zxAnPmCtrlEntry,_T:zxAnPmCtrlIndex,'zxAnPmCtrlDesc':zxAnPmCtrlDesc,'zxAnPmCtrlMetric':zxAnPmCtrlMetric,'zxAnPmCtrlMetricInstIndex':zxAnPmCtrlMetricInstIndex,'zxAnPmCtrlAdminStatus':zxAnPmCtrlAdminStatus,'zxAnPmCtrlBucketsRequested':zxAnPmCtrlBucketsRequested,'zxAnPmCtrlBucketsGranted':zxAnPmCtrlBucketsGranted,'zxAnPmCtrlSamplingInterval':zxAnPmCtrlSamplingInterval,'zxAnPmCtrlRowStatus':zxAnPmCtrlRowStatus,_K:zxAnPmCtrlSamplingType,_J:zxAnPmCtrlStatisticalInterval,'zxAnPmSpareIndex':zxAnPmSpareIndex,'zxAnPmHisTable':zxAnPmHisTable,'zxAnPmHisEntry':zxAnPmHisEntry,_U:zxAnPmHisMetric,_V:zxAnPmHisMetricInstIndex,_I:zxAnPmHisStatisticalValue,'zxAnPmThresholdTable':zxAnPmThresholdTable,'zxAnPmThresholdEntry':zxAnPmThresholdEntry,_G:zxAnPmThresholdMetricInstIndex,_H:zxAnPmThresholdMetric,'zxAnPmEventTrapEnable':zxAnPmEventTrapEnable,_P:zxAnPmRisingWarningThreshold,_R:zxAnPmRisingAlarmThreshold,_Q:zxAnPmFallingWarningThreshold,_S:zxAnPmFallingAlarmThreshold,'zxAnPmThresholdRowStatus':zxAnPmThresholdRowStatus,'zxAnPerfLogMgmtObjects':zxAnPerfLogMgmtObjects,'zxAnPmLogAdminStatus':zxAnPmLogAdminStatus,'zxAnPmLogMaxRecordRows':zxAnPmLogMaxRecordRows,'zxAnPmLogManualReportAction':zxAnPmLogManualReportAction,'zxAnPmLogManualReportStatus':zxAnPmLogManualReportStatus,'zxAnPmLogAutoReportMetric':zxAnPmLogAutoReportMetric,'zxAnPmLogAutoReportInterval':zxAnPmLogAutoReportInterval,'zxAnPmLogReportFtpHost':zxAnPmLogReportFtpHost,'zxAnPmLogReportFtpPath':zxAnPmLogReportFtpPath,'zxAnPmLogReportFtpUser':zxAnPmLogReportFtpUser,'zxAnPmLogReportFtpPassword':zxAnPmLogReportFtpPassword,'zxAnPmLogCtrlTable':zxAnPmLogCtrlTable,'zxAnPmLogCtrlEntry':zxAnPmLogCtrlEntry,_W:zxAnPmLogCtrlMetric,_X:zxAnPmLogCtrlMetricInstIndex,'zxAnPmLoggingMetricAdminStatus':zxAnPmLoggingMetricAdminStatus,'zxAnPmLogCtrlRowStatus':zxAnPmLogCtrlRowStatus,'zxAnPerfFileMgmtObjects':zxAnPerfFileMgmtObjects,'zxAnPerfRetrievalControlObjects':zxAnPerfRetrievalControlObjects,'zxAnPerfRetrievalTimeGranularity':zxAnPerfRetrievalTimeGranularity,'zxAnPerfRetrievalStartTime':zxAnPerfRetrievalStartTime,'zxAnPerfRetrievalEndTime':zxAnPerfRetrievalEndTime,'zxAnPerfMgmtTrapObjects':zxAnPerfMgmtTrapObjects,'zxAnPmMetricOverWarning':zxAnPmMetricOverWarning,'zxAnPmMetricOverWarningRestore':zxAnPmMetricOverWarningRestore,'zxAnPmMetricOverAlarm':zxAnPmMetricOverAlarm,'zxAnPmMetricOverAlarmRestore':zxAnPmMetricOverAlarmRestore})