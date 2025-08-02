_l='alarmTrapNumber'
_k='alarmTrapDescription'
_j='alarmObjectVal'
_i='alarmObjectId'
_h='alarmLogFTPStatus'
_g='alarmOid'
_f='alarmActiveObjectId'
_e='alarmLogRecordId'
_d='criticalTrapDisable'
_c='majorTrapDisable'
_b='minorTrapDisable'
_a='warningTrapDisable'
_Z='statusTrapDisable'
_Y='criticalTrapEnable'
_X='majorTrapEnable'
_W='minorTrapEnable'
_V='warningTrapEnable'
_U='statusTrapEnable'
_T='activeReportableCritical'
_S='activeReportableMajor'
_R='activeReportableMinor'
_Q='activeReportableWarning'
_P='activeReportableStatus'
_O='accessControlLoginIpAddress'
_N='SIAE-USER-MIB'
_M='ObjectIdentifier'
_L='OctetString'
_K='alarmIpSnmpAgentAddress'
_J='Unsigned32'
_I='accessible-for-notify'
_H='DisplayString'
_G='cleared'
_F='disable'
_E='SIAE-ALARM-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,_M)
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
siaeMib,siaeMicroelettronicaSpa=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib','siaeMicroelettronicaSpa')
accessControlLoginIpAddress,=mibBuilder.importSymbols(_N,_O)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
smalarm=ModuleIdentity((1,3,6,1,4,1,3373,1103,4))
if mibBuilder.loadTexts:smalarm.setRevisions(('2016-10-04 00:00','2015-07-17 00:00','2015-03-23 00:00','2015-03-16 00:00','2014-06-23 00:00','2014-03-03 00:00','2014-02-03 00:00','2013-04-16 00:00'))
class AlarmStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_G,1),(_P,2),(_Q,3),(_R,4),(_S,5),(_T,6)))
class AlarmSeverityCode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,18,19,20,21,22)));namedValues=NamedValues(*((_F,1),(_U,2),(_V,3),(_W,4),(_X,5),(_Y,6),(_Z,18),(_a,19),(_b,20),(_c,21),(_d,22)))
_AlarmTrap_ObjectIdentity=ObjectIdentity
alarmTrap=_AlarmTrap_ObjectIdentity((1,3,6,1,4,1,3373,1103,0))
class _AlarmMibVersion_Type(Integer32):defaultValue=1
_AlarmMibVersion_Type.__name__=_B
_AlarmMibVersion_Object=MibScalar
alarmMibVersion=_AlarmMibVersion_Object((1,3,6,1,4,1,3373,1103,4,1),_AlarmMibVersion_Type())
alarmMibVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmMibVersion.setStatus(_A)
_SiaeNotificationEntry_ObjectIdentity=ObjectIdentity
siaeNotificationEntry=_SiaeNotificationEntry_ObjectIdentity((1,3,6,1,4,1,3373,1103,4,2))
_AlarmObjectId_Type=ObjectIdentifier
_AlarmObjectId_Object=MibScalar
alarmObjectId=_AlarmObjectId_Object((1,3,6,1,4,1,3373,1103,4,2,1),_AlarmObjectId_Type())
alarmObjectId.setMaxAccess(_I)
if mibBuilder.loadTexts:alarmObjectId.setStatus(_A)
_AlarmObjectVal_Type=AlarmStatus
_AlarmObjectVal_Object=MibScalar
alarmObjectVal=_AlarmObjectVal_Object((1,3,6,1,4,1,3373,1103,4,2,2),_AlarmObjectVal_Type())
alarmObjectVal.setMaxAccess(_I)
if mibBuilder.loadTexts:alarmObjectVal.setStatus(_A)
class _AlarmTrapDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_AlarmTrapDescription_Type.__name__=_L
_AlarmTrapDescription_Object=MibScalar
alarmTrapDescription=_AlarmTrapDescription_Object((1,3,6,1,4,1,3373,1103,4,2,3),_AlarmTrapDescription_Type())
alarmTrapDescription.setMaxAccess(_I)
if mibBuilder.loadTexts:alarmTrapDescription.setStatus(_A)
_AlarmTrapNumber_Type=Unsigned32
_AlarmTrapNumber_Object=MibScalar
alarmTrapNumber=_AlarmTrapNumber_Object((1,3,6,1,4,1,3373,1103,4,2,4),_AlarmTrapNumber_Type())
alarmTrapNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmTrapNumber.setStatus(_A)
_AlarmIpSnmpAgentAddress_Type=IpAddress
_AlarmIpSnmpAgentAddress_Object=MibScalar
alarmIpSnmpAgentAddress=_AlarmIpSnmpAgentAddress_Object((1,3,6,1,4,1,3373,1103,4,2,5),_AlarmIpSnmpAgentAddress_Type())
alarmIpSnmpAgentAddress.setMaxAccess(_I)
if mibBuilder.loadTexts:alarmIpSnmpAgentAddress.setStatus(_A)
_AlarmLogTable_Object=MibTable
alarmLogTable=_AlarmLogTable_Object((1,3,6,1,4,1,3373,1103,4,3))
if mibBuilder.loadTexts:alarmLogTable.setStatus(_A)
_AlarmLogRecord_Object=MibTableRow
alarmLogRecord=_AlarmLogRecord_Object((1,3,6,1,4,1,3373,1103,4,3,1))
alarmLogRecord.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:alarmLogRecord.setStatus(_A)
_AlarmLogRecordId_Type=Integer32
_AlarmLogRecordId_Object=MibTableColumn
alarmLogRecordId=_AlarmLogRecordId_Object((1,3,6,1,4,1,3373,1103,4,3,1,1),_AlarmLogRecordId_Type())
alarmLogRecordId.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmLogRecordId.setStatus(_A)
_AlarmLogObjectId_Type=ObjectIdentifier
_AlarmLogObjectId_Object=MibTableColumn
alarmLogObjectId=_AlarmLogObjectId_Object((1,3,6,1,4,1,3373,1103,4,3,1,2),_AlarmLogObjectId_Type())
alarmLogObjectId.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmLogObjectId.setStatus(_A)
_AlarmLogObjectVal_Type=AlarmStatus
_AlarmLogObjectVal_Object=MibTableColumn
alarmLogObjectVal=_AlarmLogObjectVal_Object((1,3,6,1,4,1,3373,1103,4,3,1,3),_AlarmLogObjectVal_Type())
alarmLogObjectVal.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmLogObjectVal.setStatus(_A)
_AlarmLogObjectSev_Type=AlarmSeverityCode
_AlarmLogObjectSev_Object=MibTableColumn
alarmLogObjectSev=_AlarmLogObjectSev_Object((1,3,6,1,4,1,3373,1103,4,3,1,4),_AlarmLogObjectSev_Type())
alarmLogObjectSev.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmLogObjectSev.setStatus(_A)
class _AlarmLogDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_AlarmLogDescription_Type.__name__=_H
_AlarmLogDescription_Object=MibTableColumn
alarmLogDescription=_AlarmLogDescription_Object((1,3,6,1,4,1,3373,1103,4,3,1,5),_AlarmLogDescription_Type())
alarmLogDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmLogDescription.setStatus(_A)
_AlarmLogEventTime_Type=Unsigned32
_AlarmLogEventTime_Object=MibTableColumn
alarmLogEventTime=_AlarmLogEventTime_Object((1,3,6,1,4,1,3373,1103,4,3,1,6),_AlarmLogEventTime_Type())
alarmLogEventTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmLogEventTime.setStatus(_A)
class _AlarmLogActionRequest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('notActive',0),('delete',1),('read',2)))
_AlarmLogActionRequest_Type.__name__=_B
_AlarmLogActionRequest_Object=MibScalar
alarmLogActionRequest=_AlarmLogActionRequest_Object((1,3,6,1,4,1,3373,1103,4,4),_AlarmLogActionRequest_Type())
alarmLogActionRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmLogActionRequest.setStatus(_A)
class _AlarmLogFTPfile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AlarmLogFTPfile_Type.__name__=_H
_AlarmLogFTPfile_Object=MibScalar
alarmLogFTPfile=_AlarmLogFTPfile_Object((1,3,6,1,4,1,3373,1103,4,5),_AlarmLogFTPfile_Type())
alarmLogFTPfile.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmLogFTPfile.setStatus(_A)
class _AlarmLogAlarmSeverityEnable_Type(Integer32):defaultValue=31
_AlarmLogAlarmSeverityEnable_Type.__name__=_B
_AlarmLogAlarmSeverityEnable_Object=MibScalar
alarmLogAlarmSeverityEnable=_AlarmLogAlarmSeverityEnable_Object((1,3,6,1,4,1,3373,1103,4,6),_AlarmLogAlarmSeverityEnable_Type())
alarmLogAlarmSeverityEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmLogAlarmSeverityEnable.setStatus(_A)
class _AlarmLogStartHourEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_AlarmLogStartHourEnable_Type.__name__=_B
_AlarmLogStartHourEnable_Object=MibScalar
alarmLogStartHourEnable=_AlarmLogStartHourEnable_Object((1,3,6,1,4,1,3373,1103,4,7),_AlarmLogStartHourEnable_Type())
alarmLogStartHourEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmLogStartHourEnable.setStatus(_A)
class _AlarmLogEndHourEnable_Type(Integer32):defaultValue=23;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_AlarmLogEndHourEnable_Type.__name__=_B
_AlarmLogEndHourEnable_Object=MibScalar
alarmLogEndHourEnable=_AlarmLogEndHourEnable_Object((1,3,6,1,4,1,3373,1103,4,8),_AlarmLogEndHourEnable_Type())
alarmLogEndHourEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmLogEndHourEnable.setStatus(_A)
class _AlarmLogStartTimeFilter_Type(Unsigned32):defaultValue=0
_AlarmLogStartTimeFilter_Type.__name__=_J
_AlarmLogStartTimeFilter_Object=MibScalar
alarmLogStartTimeFilter=_AlarmLogStartTimeFilter_Object((1,3,6,1,4,1,3373,1103,4,9),_AlarmLogStartTimeFilter_Type())
alarmLogStartTimeFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmLogStartTimeFilter.setStatus(_A)
class _AlarmLogEndTimeFilter_Type(Unsigned32):defaultValue=0
_AlarmLogEndTimeFilter_Type.__name__=_J
_AlarmLogEndTimeFilter_Object=MibScalar
alarmLogEndTimeFilter=_AlarmLogEndTimeFilter_Object((1,3,6,1,4,1,3373,1103,4,10),_AlarmLogEndTimeFilter_Type())
alarmLogEndTimeFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmLogEndTimeFilter.setStatus(_A)
class _AlarmLogManagedObjectFilter_Type(ObjectIdentifier):defaultValue=1,3,6,1,4,1,3373
_AlarmLogManagedObjectFilter_Type.__name__=_M
_AlarmLogManagedObjectFilter_Object=MibScalar
alarmLogManagedObjectFilter=_AlarmLogManagedObjectFilter_Object((1,3,6,1,4,1,3373,1103,4,11),_AlarmLogManagedObjectFilter_Type())
alarmLogManagedObjectFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmLogManagedObjectFilter.setStatus(_A)
class _AlarmLogAlarmSeverityFilter_Type(Integer32):defaultValue=31
_AlarmLogAlarmSeverityFilter_Type.__name__=_B
_AlarmLogAlarmSeverityFilter_Object=MibScalar
alarmLogAlarmSeverityFilter=_AlarmLogAlarmSeverityFilter_Object((1,3,6,1,4,1,3373,1103,4,12),_AlarmLogAlarmSeverityFilter_Type())
alarmLogAlarmSeverityFilter.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmLogAlarmSeverityFilter.setStatus(_A)
class _AlarmLogFTPStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('transferring',1),('completed',2),('interrupted',3),('empty',4)))
_AlarmLogFTPStatus_Type.__name__=_B
_AlarmLogFTPStatus_Object=MibScalar
alarmLogFTPStatus=_AlarmLogFTPStatus_Object((1,3,6,1,4,1,3373,1103,4,14),_AlarmLogFTPStatus_Type())
alarmLogFTPStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmLogFTPStatus.setStatus(_A)
class _AlarmLogFTPStatusTrapNotification_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,34)));namedValues=NamedValues(*(('trapDisable',1),('trapEnable',2),('trapEnableWithACK',34)))
_AlarmLogFTPStatusTrapNotification_Type.__name__=_B
_AlarmLogFTPStatusTrapNotification_Object=MibScalar
alarmLogFTPStatusTrapNotification=_AlarmLogFTPStatusTrapNotification_Object((1,3,6,1,4,1,3373,1103,4,15),_AlarmLogFTPStatusTrapNotification_Type())
alarmLogFTPStatusTrapNotification.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmLogFTPStatusTrapNotification.setStatus(_A)
_AlarmLogLastEventTime_Type=Unsigned32
_AlarmLogLastEventTime_Object=MibScalar
alarmLogLastEventTime=_AlarmLogLastEventTime_Object((1,3,6,1,4,1,3373,1103,4,16),_AlarmLogLastEventTime_Type())
alarmLogLastEventTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmLogLastEventTime.setStatus(_A)
_AlarmActiveTable_Object=MibTable
alarmActiveTable=_AlarmActiveTable_Object((1,3,6,1,4,1,3373,1103,4,17))
if mibBuilder.loadTexts:alarmActiveTable.setStatus(_A)
_AlarmActiveRecord_Object=MibTableRow
alarmActiveRecord=_AlarmActiveRecord_Object((1,3,6,1,4,1,3373,1103,4,17,1))
alarmActiveRecord.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:alarmActiveRecord.setStatus(_A)
_AlarmActiveObjectId_Type=ObjectIdentifier
_AlarmActiveObjectId_Object=MibTableColumn
alarmActiveObjectId=_AlarmActiveObjectId_Object((1,3,6,1,4,1,3373,1103,4,17,1,1),_AlarmActiveObjectId_Type())
alarmActiveObjectId.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmActiveObjectId.setStatus(_A)
_AlarmActiveObjectVal_Type=AlarmStatus
_AlarmActiveObjectVal_Object=MibTableColumn
alarmActiveObjectVal=_AlarmActiveObjectVal_Object((1,3,6,1,4,1,3373,1103,4,17,1,2),_AlarmActiveObjectVal_Type())
alarmActiveObjectVal.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmActiveObjectVal.setStatus(_A)
class _AlarmActiveDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_AlarmActiveDescription_Type.__name__=_H
_AlarmActiveDescription_Object=MibTableColumn
alarmActiveDescription=_AlarmActiveDescription_Object((1,3,6,1,4,1,3373,1103,4,17,1,3),_AlarmActiveDescription_Type())
alarmActiveDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmActiveDescription.setStatus(_A)
_AlarmActiveEventTime_Type=Unsigned32
_AlarmActiveEventTime_Object=MibTableColumn
alarmActiveEventTime=_AlarmActiveEventTime_Object((1,3,6,1,4,1,3373,1103,4,17,1,4),_AlarmActiveEventTime_Type())
alarmActiveEventTime.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmActiveEventTime.setStatus(_A)
class _AlarmActiveFloodingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_AlarmActiveFloodingStatus_Type.__name__=_B
_AlarmActiveFloodingStatus_Object=MibTableColumn
alarmActiveFloodingStatus=_AlarmActiveFloodingStatus_Object((1,3,6,1,4,1,3373,1103,4,17,1,5),_AlarmActiveFloodingStatus_Type())
alarmActiveFloodingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmActiveFloodingStatus.setStatus(_A)
class _AlarmSyntesysCritical_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,6)));namedValues=NamedValues(*((_G,1),(_T,6)))
_AlarmSyntesysCritical_Type.__name__=_B
_AlarmSyntesysCritical_Object=MibScalar
alarmSyntesysCritical=_AlarmSyntesysCritical_Object((1,3,6,1,4,1,3373,1103,4,18),_AlarmSyntesysCritical_Type())
alarmSyntesysCritical.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmSyntesysCritical.setStatus(_A)
class _AlarmSyntesysCriticalSeverityCode_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,6,22)));namedValues=NamedValues(*((_F,1),(_Y,6),(_d,22)))
_AlarmSyntesysCriticalSeverityCode_Type.__name__=_B
_AlarmSyntesysCriticalSeverityCode_Object=MibScalar
alarmSyntesysCriticalSeverityCode=_AlarmSyntesysCriticalSeverityCode_Object((1,3,6,1,4,1,3373,1103,4,19),_AlarmSyntesysCriticalSeverityCode_Type())
alarmSyntesysCriticalSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmSyntesysCriticalSeverityCode.setStatus(_A)
class _AlarmSyntesysMajor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5)));namedValues=NamedValues(*((_G,1),(_S,5)))
_AlarmSyntesysMajor_Type.__name__=_B
_AlarmSyntesysMajor_Object=MibScalar
alarmSyntesysMajor=_AlarmSyntesysMajor_Object((1,3,6,1,4,1,3373,1103,4,20),_AlarmSyntesysMajor_Type())
alarmSyntesysMajor.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmSyntesysMajor.setStatus(_A)
class _AlarmSyntesysMajorSeverityCode_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,5,21)));namedValues=NamedValues(*((_F,1),(_X,5),(_c,21)))
_AlarmSyntesysMajorSeverityCode_Type.__name__=_B
_AlarmSyntesysMajorSeverityCode_Object=MibScalar
alarmSyntesysMajorSeverityCode=_AlarmSyntesysMajorSeverityCode_Object((1,3,6,1,4,1,3373,1103,4,21),_AlarmSyntesysMajorSeverityCode_Type())
alarmSyntesysMajorSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmSyntesysMajorSeverityCode.setStatus(_A)
class _AlarmSyntesysMinor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4)));namedValues=NamedValues(*((_G,1),(_R,4)))
_AlarmSyntesysMinor_Type.__name__=_B
_AlarmSyntesysMinor_Object=MibScalar
alarmSyntesysMinor=_AlarmSyntesysMinor_Object((1,3,6,1,4,1,3373,1103,4,22),_AlarmSyntesysMinor_Type())
alarmSyntesysMinor.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmSyntesysMinor.setStatus(_A)
class _AlarmSyntesysMinorSeverityCode_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,20)));namedValues=NamedValues(*((_F,1),(_W,4),(_b,20)))
_AlarmSyntesysMinorSeverityCode_Type.__name__=_B
_AlarmSyntesysMinorSeverityCode_Object=MibScalar
alarmSyntesysMinorSeverityCode=_AlarmSyntesysMinorSeverityCode_Object((1,3,6,1,4,1,3373,1103,4,23),_AlarmSyntesysMinorSeverityCode_Type())
alarmSyntesysMinorSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmSyntesysMinorSeverityCode.setStatus(_A)
class _AlarmSyntesysWarning_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3)));namedValues=NamedValues(*((_G,1),(_Q,3)))
_AlarmSyntesysWarning_Type.__name__=_B
_AlarmSyntesysWarning_Object=MibScalar
alarmSyntesysWarning=_AlarmSyntesysWarning_Object((1,3,6,1,4,1,3373,1103,4,24),_AlarmSyntesysWarning_Type())
alarmSyntesysWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmSyntesysWarning.setStatus(_A)
class _AlarmSyntesysWarningSeverityCode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,19)));namedValues=NamedValues(*((_F,1),(_V,3),(_a,19)))
_AlarmSyntesysWarningSeverityCode_Type.__name__=_B
_AlarmSyntesysWarningSeverityCode_Object=MibScalar
alarmSyntesysWarningSeverityCode=_AlarmSyntesysWarningSeverityCode_Object((1,3,6,1,4,1,3373,1103,4,25),_AlarmSyntesysWarningSeverityCode_Type())
alarmSyntesysWarningSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmSyntesysWarningSeverityCode.setStatus(_A)
class _AlarmSyntesysStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_P,2)))
_AlarmSyntesysStatus_Type.__name__=_B
_AlarmSyntesysStatus_Object=MibScalar
alarmSyntesysStatus=_AlarmSyntesysStatus_Object((1,3,6,1,4,1,3373,1103,4,26),_AlarmSyntesysStatus_Type())
alarmSyntesysStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmSyntesysStatus.setStatus(_A)
class _AlarmSyntesysStatusSeverityCode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,18)));namedValues=NamedValues(*((_F,1),(_U,2),(_Z,18)))
_AlarmSyntesysStatusSeverityCode_Type.__name__=_B
_AlarmSyntesysStatusSeverityCode_Object=MibScalar
alarmSyntesysStatusSeverityCode=_AlarmSyntesysStatusSeverityCode_Object((1,3,6,1,4,1,3373,1103,4,27),_AlarmSyntesysStatusSeverityCode_Type())
alarmSyntesysStatusSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmSyntesysStatusSeverityCode.setStatus(_A)
class _AlarmAntiFlooding_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),('enable',2)))
_AlarmAntiFlooding_Type.__name__=_B
_AlarmAntiFlooding_Object=MibScalar
alarmAntiFlooding=_AlarmAntiFlooding_Object((1,3,6,1,4,1,3373,1103,4,28),_AlarmAntiFlooding_Type())
alarmAntiFlooding.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmAntiFlooding.setStatus(_A)
class _AlarmAntiFloodingWindow_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,120))
_AlarmAntiFloodingWindow_Type.__name__=_B
_AlarmAntiFloodingWindow_Object=MibScalar
alarmAntiFloodingWindow=_AlarmAntiFloodingWindow_Object((1,3,6,1,4,1,3373,1103,4,29),_AlarmAntiFloodingWindow_Type())
alarmAntiFloodingWindow.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmAntiFloodingWindow.setStatus(_A)
class _AlarmAntiFloodingHighWater_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,10))
_AlarmAntiFloodingHighWater_Type.__name__=_B
_AlarmAntiFloodingHighWater_Object=MibScalar
alarmAntiFloodingHighWater=_AlarmAntiFloodingHighWater_Object((1,3,6,1,4,1,3373,1103,4,30),_AlarmAntiFloodingHighWater_Type())
alarmAntiFloodingHighWater.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmAntiFloodingHighWater.setStatus(_A)
class _AlarmAntiFloodingLowWater_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_AlarmAntiFloodingLowWater_Type.__name__=_B
_AlarmAntiFloodingLowWater_Object=MibScalar
alarmAntiFloodingLowWater=_AlarmAntiFloodingLowWater_Object((1,3,6,1,4,1,3373,1103,4,31),_AlarmAntiFloodingLowWater_Type())
alarmAntiFloodingLowWater.setMaxAccess(_D)
if mibBuilder.loadTexts:alarmAntiFloodingLowWater.setStatus(_A)
_AlarmItemTable_Object=MibTable
alarmItemTable=_AlarmItemTable_Object((1,3,6,1,4,1,3373,1103,4,32))
if mibBuilder.loadTexts:alarmItemTable.setStatus(_A)
_AlarmRecord_Object=MibTableRow
alarmRecord=_AlarmRecord_Object((1,3,6,1,4,1,3373,1103,4,32,1))
alarmRecord.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:alarmRecord.setStatus(_A)
_AlarmOid_Type=ObjectIdentifier
_AlarmOid_Object=MibTableColumn
alarmOid=_AlarmOid_Object((1,3,6,1,4,1,3373,1103,4,32,1,1),_AlarmOid_Type())
alarmOid.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmOid.setStatus(_A)
class _AlarmDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_AlarmDescription_Type.__name__=_H
_AlarmDescription_Object=MibTableColumn
alarmDescription=_AlarmDescription_Object((1,3,6,1,4,1,3373,1103,4,32,1,2),_AlarmDescription_Type())
alarmDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmDescription.setStatus(_A)
alarmLogFTPStatusTrap=NotificationType((1,3,6,1,4,1,3373,1103,0,401))
alarmLogFTPStatusTrap.setObjects(*((_E,_K),(_E,_h),(_N,_O)))
if mibBuilder.loadTexts:alarmLogFTPStatusTrap.setStatus(_A)
alarmTrapObject=NotificationType((1,3,6,1,4,1,3373,1103,0,3373))
alarmTrapObject.setObjects(*((_E,_K),(_E,_i),(_E,_j),(_E,_k),(_E,_l)))
if mibBuilder.loadTexts:alarmTrapObject.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'AlarmStatus':AlarmStatus,'AlarmSeverityCode':AlarmSeverityCode,'alarmTrap':alarmTrap,'alarmLogFTPStatusTrap':alarmLogFTPStatusTrap,'alarmTrapObject':alarmTrapObject,'smalarm':smalarm,'alarmMibVersion':alarmMibVersion,'siaeNotificationEntry':siaeNotificationEntry,_i:alarmObjectId,_j:alarmObjectVal,_k:alarmTrapDescription,_l:alarmTrapNumber,_K:alarmIpSnmpAgentAddress,'alarmLogTable':alarmLogTable,'alarmLogRecord':alarmLogRecord,_e:alarmLogRecordId,'alarmLogObjectId':alarmLogObjectId,'alarmLogObjectVal':alarmLogObjectVal,'alarmLogObjectSev':alarmLogObjectSev,'alarmLogDescription':alarmLogDescription,'alarmLogEventTime':alarmLogEventTime,'alarmLogActionRequest':alarmLogActionRequest,'alarmLogFTPfile':alarmLogFTPfile,'alarmLogAlarmSeverityEnable':alarmLogAlarmSeverityEnable,'alarmLogStartHourEnable':alarmLogStartHourEnable,'alarmLogEndHourEnable':alarmLogEndHourEnable,'alarmLogStartTimeFilter':alarmLogStartTimeFilter,'alarmLogEndTimeFilter':alarmLogEndTimeFilter,'alarmLogManagedObjectFilter':alarmLogManagedObjectFilter,'alarmLogAlarmSeverityFilter':alarmLogAlarmSeverityFilter,_h:alarmLogFTPStatus,'alarmLogFTPStatusTrapNotification':alarmLogFTPStatusTrapNotification,'alarmLogLastEventTime':alarmLogLastEventTime,'alarmActiveTable':alarmActiveTable,'alarmActiveRecord':alarmActiveRecord,_f:alarmActiveObjectId,'alarmActiveObjectVal':alarmActiveObjectVal,'alarmActiveDescription':alarmActiveDescription,'alarmActiveEventTime':alarmActiveEventTime,'alarmActiveFloodingStatus':alarmActiveFloodingStatus,'alarmSyntesysCritical':alarmSyntesysCritical,'alarmSyntesysCriticalSeverityCode':alarmSyntesysCriticalSeverityCode,'alarmSyntesysMajor':alarmSyntesysMajor,'alarmSyntesysMajorSeverityCode':alarmSyntesysMajorSeverityCode,'alarmSyntesysMinor':alarmSyntesysMinor,'alarmSyntesysMinorSeverityCode':alarmSyntesysMinorSeverityCode,'alarmSyntesysWarning':alarmSyntesysWarning,'alarmSyntesysWarningSeverityCode':alarmSyntesysWarningSeverityCode,'alarmSyntesysStatus':alarmSyntesysStatus,'alarmSyntesysStatusSeverityCode':alarmSyntesysStatusSeverityCode,'alarmAntiFlooding':alarmAntiFlooding,'alarmAntiFloodingWindow':alarmAntiFloodingWindow,'alarmAntiFloodingHighWater':alarmAntiFloodingHighWater,'alarmAntiFloodingLowWater':alarmAntiFloodingLowWater,'alarmItemTable':alarmItemTable,'alarmRecord':alarmRecord,_g:alarmOid,'alarmDescription':alarmDescription})