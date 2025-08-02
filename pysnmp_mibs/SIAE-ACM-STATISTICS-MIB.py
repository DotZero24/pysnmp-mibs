_N='notActive'
_M='DisplayString'
_L='acmsIntervalId'
_K='acmsTpProfileId'
_J='not-accessible'
_I='AlarmSeverityCode'
_H='read-write'
_G='read-create'
_F='acmsTpLinkPolId'
_E='acmsTpLinkId'
_D='Integer32'
_C='read-only'
_B='SIAE-ACM-STATISTICS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AlarmSeverityCode,AlarmStatus=mibBuilder.importSymbols('SIAE-ALARM-MIB',_I,'AlarmStatus')
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_M,'PhysAddress','RowStatus','TextualConvention')
acmStats=ModuleIdentity((1,3,6,1,4,1,3373,1103,75))
if mibBuilder.loadTexts:acmStats.setRevisions(('2016-09-13 00:00','2014-11-05 00:00','2014-02-11 00:00'))
class AcmProfile(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33)));namedValues=NamedValues(*(('unavailable',1),('downshift',2),('upshift',3),('acmBPSKstrong',4),('acmBPSK',5),('acm4QAMstrong',6),('acm4QAM',7),('acm8PSKstrong',8),('acm8PSK',9),('acm16QAMstrong',10),('acm16QAM',11),('acm32QAMstrong',12),('acm32QAM',13),('acm64QAMstrong',14),('acm64QAM',15),('acm128QAMstrong',16),('acm128QAM',17),('acm256QAMstrong',18),('acm256QAM',19),('acm512QAMstrong',20),('acm512QAM',21),('acm1024QAMstrong',22),('acm1024QAM',23),('acm2048QAMstrong',24),('acm2048QAM',25),('acm4096QAMstrong',26),('acm4096QAM',27),('acm4FQAM',28),('acm4HQAM',29),('acm4QAMlowpower',30),('acm32QAMlowpower',31),('acm64QAMlowpower',32),('acm128QAMlowpower',33)))
_AcmsMibVersion_Type=Integer32
_AcmsMibVersion_Object=MibScalar
acmsMibVersion=_AcmsMibVersion_Object((1,3,6,1,4,1,3373,1103,75,1),_AcmsMibVersion_Type())
acmsMibVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:acmsMibVersion.setStatus(_A)
_AcmsTpLinkTable_Object=MibTable
acmsTpLinkTable=_AcmsTpLinkTable_Object((1,3,6,1,4,1,3373,1103,75,2))
if mibBuilder.loadTexts:acmsTpLinkTable.setStatus(_A)
_AcmsTpLinkRecord_Object=MibTableRow
acmsTpLinkRecord=_AcmsTpLinkRecord_Object((1,3,6,1,4,1,3373,1103,75,2,1))
acmsTpLinkRecord.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:acmsTpLinkRecord.setStatus(_A)
_AcmsTpLinkId_Type=Integer32
_AcmsTpLinkId_Object=MibTableColumn
acmsTpLinkId=_AcmsTpLinkId_Object((1,3,6,1,4,1,3373,1103,75,2,1,1),_AcmsTpLinkId_Type())
acmsTpLinkId.setMaxAccess(_J)
if mibBuilder.loadTexts:acmsTpLinkId.setStatus(_A)
_AcmsTpLinkPolId_Type=Integer32
_AcmsTpLinkPolId_Object=MibTableColumn
acmsTpLinkPolId=_AcmsTpLinkPolId_Object((1,3,6,1,4,1,3373,1103,75,2,1,2),_AcmsTpLinkPolId_Type())
acmsTpLinkPolId.setMaxAccess(_J)
if mibBuilder.loadTexts:acmsTpLinkPolId.setStatus(_A)
class _AcmsTpLinkStartStop_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
_AcmsTpLinkStartStop_Type.__name__=_D
_AcmsTpLinkStartStop_Object=MibTableColumn
acmsTpLinkStartStop=_AcmsTpLinkStartStop_Object((1,3,6,1,4,1,3373,1103,75,2,1,3),_AcmsTpLinkStartStop_Type())
acmsTpLinkStartStop.setMaxAccess(_G)
if mibBuilder.loadTexts:acmsTpLinkStartStop.setStatus(_A)
class _AcmsTpLinkLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_AcmsTpLinkLabel_Type.__name__=_M
_AcmsTpLinkLabel_Object=MibTableColumn
acmsTpLinkLabel=_AcmsTpLinkLabel_Object((1,3,6,1,4,1,3373,1103,75,2,1,4),_AcmsTpLinkLabel_Type())
acmsTpLinkLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:acmsTpLinkLabel.setStatus(_A)
_AcmsTpLinkRowStatus_Type=RowStatus
_AcmsTpLinkRowStatus_Object=MibTableColumn
acmsTpLinkRowStatus=_AcmsTpLinkRowStatus_Object((1,3,6,1,4,1,3373,1103,75,2,1,5),_AcmsTpLinkRowStatus_Type())
acmsTpLinkRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:acmsTpLinkRowStatus.setStatus(_A)
_AcmsTpProfileTable_Object=MibTable
acmsTpProfileTable=_AcmsTpProfileTable_Object((1,3,6,1,4,1,3373,1103,75,3))
if mibBuilder.loadTexts:acmsTpProfileTable.setStatus(_A)
_AcmsTpProfileRecord_Object=MibTableRow
acmsTpProfileRecord=_AcmsTpProfileRecord_Object((1,3,6,1,4,1,3373,1103,75,3,1))
acmsTpProfileRecord.setIndexNames((0,_B,_E),(0,_B,_F),(0,_B,_K))
if mibBuilder.loadTexts:acmsTpProfileRecord.setStatus(_A)
_AcmsTpProfileId_Type=AcmProfile
_AcmsTpProfileId_Object=MibTableColumn
acmsTpProfileId=_AcmsTpProfileId_Object((1,3,6,1,4,1,3373,1103,75,3,1,1),_AcmsTpProfileId_Type())
acmsTpProfileId.setMaxAccess(_J)
if mibBuilder.loadTexts:acmsTpProfileId.setStatus(_A)
_AcmsTpProfile15mAlarm_Type=AlarmStatus
_AcmsTpProfile15mAlarm_Object=MibTableColumn
acmsTpProfile15mAlarm=_AcmsTpProfile15mAlarm_Object((1,3,6,1,4,1,3373,1103,75,3,1,2),_AcmsTpProfile15mAlarm_Type())
acmsTpProfile15mAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:acmsTpProfile15mAlarm.setStatus(_A)
_AcmsTpProfile24hAlarm_Type=AlarmStatus
_AcmsTpProfile24hAlarm_Object=MibTableColumn
acmsTpProfile24hAlarm=_AcmsTpProfile24hAlarm_Object((1,3,6,1,4,1,3373,1103,75,3,1,3),_AcmsTpProfile24hAlarm_Type())
acmsTpProfile24hAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:acmsTpProfile24hAlarm.setStatus(_A)
_AcmsTpProfile15mThreshold_Type=Integer32
_AcmsTpProfile15mThreshold_Object=MibTableColumn
acmsTpProfile15mThreshold=_AcmsTpProfile15mThreshold_Object((1,3,6,1,4,1,3373,1103,75,3,1,4),_AcmsTpProfile15mThreshold_Type())
acmsTpProfile15mThreshold.setMaxAccess(_G)
if mibBuilder.loadTexts:acmsTpProfile15mThreshold.setStatus(_A)
_AcmsTpProfile24hThreshold_Type=Integer32
_AcmsTpProfile24hThreshold_Object=MibTableColumn
acmsTpProfile24hThreshold=_AcmsTpProfile24hThreshold_Object((1,3,6,1,4,1,3373,1103,75,3,1,5),_AcmsTpProfile24hThreshold_Type())
acmsTpProfile24hThreshold.setMaxAccess(_G)
if mibBuilder.loadTexts:acmsTpProfile24hThreshold.setStatus(_A)
_AcmsTpProfileRowStatus_Type=RowStatus
_AcmsTpProfileRowStatus_Object=MibTableColumn
acmsTpProfileRowStatus=_AcmsTpProfileRowStatus_Object((1,3,6,1,4,1,3373,1103,75,3,1,6),_AcmsTpProfileRowStatus_Type())
acmsTpProfileRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:acmsTpProfileRowStatus.setStatus(_A)
_AcmsTpMaintTable_Object=MibTable
acmsTpMaintTable=_AcmsTpMaintTable_Object((1,3,6,1,4,1,3373,1103,75,4))
if mibBuilder.loadTexts:acmsTpMaintTable.setStatus(_A)
_AcmsTpMaintRecord_Object=MibTableRow
acmsTpMaintRecord=_AcmsTpMaintRecord_Object((1,3,6,1,4,1,3373,1103,75,4,1))
acmsTpMaintRecord.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:acmsTpMaintRecord.setStatus(_A)
class _AcmsTpMaintCounterClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),('clear',1)))
_AcmsTpMaintCounterClear_Type.__name__=_D
_AcmsTpMaintCounterClear_Object=MibTableColumn
acmsTpMaintCounterClear=_AcmsTpMaintCounterClear_Object((1,3,6,1,4,1,3373,1103,75,4,1,1),_AcmsTpMaintCounterClear_Type())
acmsTpMaintCounterClear.setMaxAccess(_H)
if mibBuilder.loadTexts:acmsTpMaintCounterClear.setStatus(_A)
class _AcmsTpMaintAlarmClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_N,0),('clear',1)))
_AcmsTpMaintAlarmClear_Type.__name__=_D
_AcmsTpMaintAlarmClear_Object=MibTableColumn
acmsTpMaintAlarmClear=_AcmsTpMaintAlarmClear_Object((1,3,6,1,4,1,3373,1103,75,4,1,2),_AcmsTpMaintAlarmClear_Type())
acmsTpMaintAlarmClear.setMaxAccess(_H)
if mibBuilder.loadTexts:acmsTpMaintAlarmClear.setStatus(_A)
_AcmsIntervalTable_Object=MibTable
acmsIntervalTable=_AcmsIntervalTable_Object((1,3,6,1,4,1,3373,1103,75,5))
if mibBuilder.loadTexts:acmsIntervalTable.setStatus(_A)
_AcmsIntervalRecord_Object=MibTableRow
acmsIntervalRecord=_AcmsIntervalRecord_Object((1,3,6,1,4,1,3373,1103,75,5,1))
acmsIntervalRecord.setIndexNames((0,_B,_E),(0,_B,_F),(0,_B,_L))
if mibBuilder.loadTexts:acmsIntervalRecord.setStatus(_A)
class _AcmsIntervalId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,19))
_AcmsIntervalId_Type.__name__=_D
_AcmsIntervalId_Object=MibTableColumn
acmsIntervalId=_AcmsIntervalId_Object((1,3,6,1,4,1,3373,1103,75,5,1,1),_AcmsIntervalId_Type())
acmsIntervalId.setMaxAccess(_C)
if mibBuilder.loadTexts:acmsIntervalId.setStatus(_A)
class _AcmsIntervalType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('daily',1),('fifteen-min',2)))
_AcmsIntervalType_Type.__name__=_D
_AcmsIntervalType_Object=MibTableColumn
acmsIntervalType=_AcmsIntervalType_Object((1,3,6,1,4,1,3373,1103,75,5,1,2),_AcmsIntervalType_Type())
acmsIntervalType.setMaxAccess(_C)
if mibBuilder.loadTexts:acmsIntervalType.setStatus(_A)
class _AcmsIntervalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('meaningless',1),('meaningfull',2),('incomplete',3),('dummy',4),('lost',5),('restarted',6)))
_AcmsIntervalStatus_Type.__name__=_D
_AcmsIntervalStatus_Object=MibTableColumn
acmsIntervalStatus=_AcmsIntervalStatus_Object((1,3,6,1,4,1,3373,1103,75,5,1,3),_AcmsIntervalStatus_Type())
acmsIntervalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:acmsIntervalStatus.setStatus(_A)
_AcmsIntervalTimeStamp_Type=Unsigned32
_AcmsIntervalTimeStamp_Object=MibTableColumn
acmsIntervalTimeStamp=_AcmsIntervalTimeStamp_Object((1,3,6,1,4,1,3373,1103,75,5,1,4),_AcmsIntervalTimeStamp_Type())
acmsIntervalTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:acmsIntervalTimeStamp.setStatus(_A)
_AcmsProfileCounterTable_Object=MibTable
acmsProfileCounterTable=_AcmsProfileCounterTable_Object((1,3,6,1,4,1,3373,1103,75,6))
if mibBuilder.loadTexts:acmsProfileCounterTable.setStatus(_A)
_AcmsProfileCounterRecord_Object=MibTableRow
acmsProfileCounterRecord=_AcmsProfileCounterRecord_Object((1,3,6,1,4,1,3373,1103,75,6,1))
acmsProfileCounterRecord.setIndexNames((0,_B,_E),(0,_B,_F),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:acmsProfileCounterRecord.setStatus(_A)
_AcmsProfileCounterValue_Type=Counter32
_AcmsProfileCounterValue_Object=MibTableColumn
acmsProfileCounterValue=_AcmsProfileCounterValue_Object((1,3,6,1,4,1,3373,1103,75,6,1,1),_AcmsProfileCounterValue_Type())
acmsProfileCounterValue.setMaxAccess(_C)
if mibBuilder.loadTexts:acmsProfileCounterValue.setStatus(_A)
class _AcmsTpProfile15mAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_AcmsTpProfile15mAlarmSeverityCode_Type.__name__=_I
_AcmsTpProfile15mAlarmSeverityCode_Object=MibScalar
acmsTpProfile15mAlarmSeverityCode=_AcmsTpProfile15mAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,75,7),_AcmsTpProfile15mAlarmSeverityCode_Type())
acmsTpProfile15mAlarmSeverityCode.setMaxAccess(_H)
if mibBuilder.loadTexts:acmsTpProfile15mAlarmSeverityCode.setStatus(_A)
class _AcmsTpProfile24hAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_AcmsTpProfile24hAlarmSeverityCode_Type.__name__=_I
_AcmsTpProfile24hAlarmSeverityCode_Object=MibScalar
acmsTpProfile24hAlarmSeverityCode=_AcmsTpProfile24hAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,75,8),_AcmsTpProfile24hAlarmSeverityCode_Type())
acmsTpProfile24hAlarmSeverityCode.setMaxAccess(_H)
if mibBuilder.loadTexts:acmsTpProfile24hAlarmSeverityCode.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AcmProfile':AcmProfile,'acmStats':acmStats,'acmsMibVersion':acmsMibVersion,'acmsTpLinkTable':acmsTpLinkTable,'acmsTpLinkRecord':acmsTpLinkRecord,_E:acmsTpLinkId,_F:acmsTpLinkPolId,'acmsTpLinkStartStop':acmsTpLinkStartStop,'acmsTpLinkLabel':acmsTpLinkLabel,'acmsTpLinkRowStatus':acmsTpLinkRowStatus,'acmsTpProfileTable':acmsTpProfileTable,'acmsTpProfileRecord':acmsTpProfileRecord,_K:acmsTpProfileId,'acmsTpProfile15mAlarm':acmsTpProfile15mAlarm,'acmsTpProfile24hAlarm':acmsTpProfile24hAlarm,'acmsTpProfile15mThreshold':acmsTpProfile15mThreshold,'acmsTpProfile24hThreshold':acmsTpProfile24hThreshold,'acmsTpProfileRowStatus':acmsTpProfileRowStatus,'acmsTpMaintTable':acmsTpMaintTable,'acmsTpMaintRecord':acmsTpMaintRecord,'acmsTpMaintCounterClear':acmsTpMaintCounterClear,'acmsTpMaintAlarmClear':acmsTpMaintAlarmClear,'acmsIntervalTable':acmsIntervalTable,'acmsIntervalRecord':acmsIntervalRecord,_L:acmsIntervalId,'acmsIntervalType':acmsIntervalType,'acmsIntervalStatus':acmsIntervalStatus,'acmsIntervalTimeStamp':acmsIntervalTimeStamp,'acmsProfileCounterTable':acmsProfileCounterTable,'acmsProfileCounterRecord':acmsProfileCounterRecord,'acmsProfileCounterValue':acmsProfileCounterValue,'acmsTpProfile15mAlarmSeverityCode':acmsTpProfile15mAlarmSeverityCode,'acmsTpProfile24hAlarmSeverityCode':acmsTpProfile24hAlarmSeverityCode})