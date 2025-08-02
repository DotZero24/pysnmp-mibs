_L='notActive'
_K='pmG828CounterBlockId'
_J='pmG828TPointId'
_I='DisplayString'
_H='pmG828TpClassId'
_G='SIAE-PMG828-MIB'
_F='read-create'
_E='AlarmSeverityCode'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AlarmSeverityCode,AlarmStatus=mibBuilder.importSymbols('SIAE-ALARM-MIB',_E,'AlarmStatus')
siaeMib,=mibBuilder.importSymbols('SIAE-TREE-MIB','siaeMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','RowStatus','TextualConvention')
pmG828=ModuleIdentity((1,3,6,1,4,1,3373,1103,11))
if mibBuilder.loadTexts:pmG828.setRevisions(('2014-10-07 00:00','2014-02-03 00:00','2013-04-16 00:00'))
class _PmG828MibVersion_Type(Integer32):defaultValue=1
_PmG828MibVersion_Type.__name__=_C
_PmG828MibVersion_Object=MibScalar
pmG828MibVersion=_PmG828MibVersion_Object((1,3,6,1,4,1,3373,1103,11,1),_PmG828MibVersion_Type())
pmG828MibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:pmG828MibVersion.setStatus(_A)
_PmG828CounterTable_Object=MibTable
pmG828CounterTable=_PmG828CounterTable_Object((1,3,6,1,4,1,3373,1103,11,2))
if mibBuilder.loadTexts:pmG828CounterTable.setStatus(_A)
_PmG828CounterRecord_Object=MibTableRow
pmG828CounterRecord=_PmG828CounterRecord_Object((1,3,6,1,4,1,3373,1103,11,2,1))
pmG828CounterRecord.setIndexNames((0,_G,_J),(0,_G,_K))
if mibBuilder.loadTexts:pmG828CounterRecord.setStatus(_A)
_PmG828TPointId_Type=Integer32
_PmG828TPointId_Object=MibTableColumn
pmG828TPointId=_PmG828TPointId_Object((1,3,6,1,4,1,3373,1103,11,2,1,1),_PmG828TPointId_Type())
pmG828TPointId.setMaxAccess(_B)
if mibBuilder.loadTexts:pmG828TPointId.setStatus(_A)
_PmG828CounterBlockId_Type=Integer32
_PmG828CounterBlockId_Object=MibTableColumn
pmG828CounterBlockId=_PmG828CounterBlockId_Object((1,3,6,1,4,1,3373,1103,11,2,1,2),_PmG828CounterBlockId_Type())
pmG828CounterBlockId.setMaxAccess(_B)
if mibBuilder.loadTexts:pmG828CounterBlockId.setStatus(_A)
class _PmG828CounterBlockType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('daily',1),('fifteenMin',2)))
_PmG828CounterBlockType_Type.__name__=_C
_PmG828CounterBlockType_Object=MibTableColumn
pmG828CounterBlockType=_PmG828CounterBlockType_Object((1,3,6,1,4,1,3373,1103,11,2,1,3),_PmG828CounterBlockType_Type())
pmG828CounterBlockType.setMaxAccess(_B)
if mibBuilder.loadTexts:pmG828CounterBlockType.setStatus(_A)
class _PmG828CounterBlockStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('meaningless',1),('meaningfull',2),('incomplete',3),('dummy',4),('lost',5),('restarted',6)))
_PmG828CounterBlockStatus_Type.__name__=_C
_PmG828CounterBlockStatus_Object=MibTableColumn
pmG828CounterBlockStatus=_PmG828CounterBlockStatus_Object((1,3,6,1,4,1,3373,1103,11,2,1,4),_PmG828CounterBlockStatus_Type())
pmG828CounterBlockStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:pmG828CounterBlockStatus.setStatus(_A)
_PmG828CounterTimeStamp_Type=Unsigned32
_PmG828CounterTimeStamp_Object=MibTableColumn
pmG828CounterTimeStamp=_PmG828CounterTimeStamp_Object((1,3,6,1,4,1,3373,1103,11,2,1,5),_PmG828CounterTimeStamp_Type())
pmG828CounterTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:pmG828CounterTimeStamp.setStatus(_A)
_PmG828BBECounter_Type=Counter32
_PmG828BBECounter_Object=MibTableColumn
pmG828BBECounter=_PmG828BBECounter_Object((1,3,6,1,4,1,3373,1103,11,2,1,6),_PmG828BBECounter_Type())
pmG828BBECounter.setMaxAccess(_B)
if mibBuilder.loadTexts:pmG828BBECounter.setStatus(_A)
_PmG828ESCounter_Type=Counter32
_PmG828ESCounter_Object=MibTableColumn
pmG828ESCounter=_PmG828ESCounter_Object((1,3,6,1,4,1,3373,1103,11,2,1,7),_PmG828ESCounter_Type())
pmG828ESCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:pmG828ESCounter.setStatus(_A)
_PmG828SESCounter_Type=Counter32
_PmG828SESCounter_Object=MibTableColumn
pmG828SESCounter=_PmG828SESCounter_Object((1,3,6,1,4,1,3373,1103,11,2,1,8),_PmG828SESCounter_Type())
pmG828SESCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:pmG828SESCounter.setStatus(_A)
_PmG828UASCounter_Type=Counter32
_PmG828UASCounter_Object=MibTableColumn
pmG828UASCounter=_PmG828UASCounter_Object((1,3,6,1,4,1,3373,1103,11,2,1,9),_PmG828UASCounter_Type())
pmG828UASCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:pmG828UASCounter.setStatus(_A)
_PmG828SEPCounter_Type=Counter32
_PmG828SEPCounter_Object=MibTableColumn
pmG828SEPCounter=_PmG828SEPCounter_Object((1,3,6,1,4,1,3373,1103,11,2,1,10),_PmG828SEPCounter_Type())
pmG828SEPCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:pmG828SEPCounter.setStatus(_A)
_PmG828TpClassTable_Object=MibTable
pmG828TpClassTable=_PmG828TpClassTable_Object((1,3,6,1,4,1,3373,1103,11,3))
if mibBuilder.loadTexts:pmG828TpClassTable.setStatus(_A)
_PmG828TpClassRecord_Object=MibTableRow
pmG828TpClassRecord=_PmG828TpClassRecord_Object((1,3,6,1,4,1,3373,1103,11,3,1))
pmG828TpClassRecord.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:pmG828TpClassRecord.setStatus(_A)
_PmG828TpClassId_Type=Integer32
_PmG828TpClassId_Object=MibTableColumn
pmG828TpClassId=_PmG828TpClassId_Object((1,3,6,1,4,1,3373,1103,11,3,1,1),_PmG828TpClassId_Type())
pmG828TpClassId.setMaxAccess(_B)
if mibBuilder.loadTexts:pmG828TpClassId.setStatus(_A)
class _PmG828TpClassStartStop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
_PmG828TpClassStartStop_Type.__name__=_C
_PmG828TpClassStartStop_Object=MibTableColumn
pmG828TpClassStartStop=_PmG828TpClassStartStop_Object((1,3,6,1,4,1,3373,1103,11,3,1,2),_PmG828TpClassStartStop_Type())
pmG828TpClassStartStop.setMaxAccess(_F)
if mibBuilder.loadTexts:pmG828TpClassStartStop.setStatus(_A)
class _PmG828TpClassLabel_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_PmG828TpClassLabel_Type.__name__=_I
_PmG828TpClassLabel_Object=MibTableColumn
pmG828TpClassLabel=_PmG828TpClassLabel_Object((1,3,6,1,4,1,3373,1103,11,3,1,3),_PmG828TpClassLabel_Type())
pmG828TpClassLabel.setMaxAccess(_B)
if mibBuilder.loadTexts:pmG828TpClassLabel.setStatus(_A)
_PmG828TpClassTimeStamp_Type=Unsigned32
_PmG828TpClassTimeStamp_Object=MibTableColumn
pmG828TpClassTimeStamp=_PmG828TpClassTimeStamp_Object((1,3,6,1,4,1,3373,1103,11,3,1,4),_PmG828TpClassTimeStamp_Type())
pmG828TpClassTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:pmG828TpClassTimeStamp.setStatus(_A)
_PmG828TpClass15MEsAlarm_Type=AlarmStatus
_PmG828TpClass15MEsAlarm_Object=MibTableColumn
pmG828TpClass15MEsAlarm=_PmG828TpClass15MEsAlarm_Object((1,3,6,1,4,1,3373,1103,11,3,1,5),_PmG828TpClass15MEsAlarm_Type())
pmG828TpClass15MEsAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmG828TpClass15MEsAlarm.setStatus(_A)
_PmG828TpClass15MSesAlarm_Type=AlarmStatus
_PmG828TpClass15MSesAlarm_Object=MibTableColumn
pmG828TpClass15MSesAlarm=_PmG828TpClass15MSesAlarm_Object((1,3,6,1,4,1,3373,1103,11,3,1,6),_PmG828TpClass15MSesAlarm_Type())
pmG828TpClass15MSesAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmG828TpClass15MSesAlarm.setStatus(_A)
_PmG828TpClass15MSepAlarm_Type=AlarmStatus
_PmG828TpClass15MSepAlarm_Object=MibTableColumn
pmG828TpClass15MSepAlarm=_PmG828TpClass15MSepAlarm_Object((1,3,6,1,4,1,3373,1103,11,3,1,7),_PmG828TpClass15MSepAlarm_Type())
pmG828TpClass15MSepAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmG828TpClass15MSepAlarm.setStatus(_A)
_PmG828TpClass24HEsAlarm_Type=AlarmStatus
_PmG828TpClass24HEsAlarm_Object=MibTableColumn
pmG828TpClass24HEsAlarm=_PmG828TpClass24HEsAlarm_Object((1,3,6,1,4,1,3373,1103,11,3,1,8),_PmG828TpClass24HEsAlarm_Type())
pmG828TpClass24HEsAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmG828TpClass24HEsAlarm.setStatus(_A)
_PmG828TpClass24HSesAlarm_Type=AlarmStatus
_PmG828TpClass24HSesAlarm_Object=MibTableColumn
pmG828TpClass24HSesAlarm=_PmG828TpClass24HSesAlarm_Object((1,3,6,1,4,1,3373,1103,11,3,1,9),_PmG828TpClass24HSesAlarm_Type())
pmG828TpClass24HSesAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmG828TpClass24HSesAlarm.setStatus(_A)
_PmG828TpClass24HSepAlarm_Type=AlarmStatus
_PmG828TpClass24HSepAlarm_Object=MibTableColumn
pmG828TpClass24HSepAlarm=_PmG828TpClass24HSepAlarm_Object((1,3,6,1,4,1,3373,1103,11,3,1,10),_PmG828TpClass24HSepAlarm_Type())
pmG828TpClass24HSepAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmG828TpClass24HSepAlarm.setStatus(_A)
_PmG828TpClassUasAlarm_Type=AlarmStatus
_PmG828TpClassUasAlarm_Object=MibTableColumn
pmG828TpClassUasAlarm=_PmG828TpClassUasAlarm_Object((1,3,6,1,4,1,3373,1103,11,3,1,11),_PmG828TpClassUasAlarm_Type())
pmG828TpClassUasAlarm.setMaxAccess(_B)
if mibBuilder.loadTexts:pmG828TpClassUasAlarm.setStatus(_A)
class _PmG828TpClass15MEsThreshold_Type(Integer32):defaultValue=0
_PmG828TpClass15MEsThreshold_Type.__name__=_C
_PmG828TpClass15MEsThreshold_Object=MibTableColumn
pmG828TpClass15MEsThreshold=_PmG828TpClass15MEsThreshold_Object((1,3,6,1,4,1,3373,1103,11,3,1,12),_PmG828TpClass15MEsThreshold_Type())
pmG828TpClass15MEsThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:pmG828TpClass15MEsThreshold.setStatus(_A)
class _PmG828TpClass15MSesThreshold_Type(Integer32):defaultValue=0
_PmG828TpClass15MSesThreshold_Type.__name__=_C
_PmG828TpClass15MSesThreshold_Object=MibTableColumn
pmG828TpClass15MSesThreshold=_PmG828TpClass15MSesThreshold_Object((1,3,6,1,4,1,3373,1103,11,3,1,13),_PmG828TpClass15MSesThreshold_Type())
pmG828TpClass15MSesThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:pmG828TpClass15MSesThreshold.setStatus(_A)
class _PmG828TpClass15MSepThreshold_Type(Integer32):defaultValue=0
_PmG828TpClass15MSepThreshold_Type.__name__=_C
_PmG828TpClass15MSepThreshold_Object=MibTableColumn
pmG828TpClass15MSepThreshold=_PmG828TpClass15MSepThreshold_Object((1,3,6,1,4,1,3373,1103,11,3,1,14),_PmG828TpClass15MSepThreshold_Type())
pmG828TpClass15MSepThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:pmG828TpClass15MSepThreshold.setStatus(_A)
class _PmG828TpClass24HEsThreshold_Type(Integer32):defaultValue=0
_PmG828TpClass24HEsThreshold_Type.__name__=_C
_PmG828TpClass24HEsThreshold_Object=MibTableColumn
pmG828TpClass24HEsThreshold=_PmG828TpClass24HEsThreshold_Object((1,3,6,1,4,1,3373,1103,11,3,1,15),_PmG828TpClass24HEsThreshold_Type())
pmG828TpClass24HEsThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:pmG828TpClass24HEsThreshold.setStatus(_A)
class _PmG828TpClass24HSesThreshold_Type(Integer32):defaultValue=0
_PmG828TpClass24HSesThreshold_Type.__name__=_C
_PmG828TpClass24HSesThreshold_Object=MibTableColumn
pmG828TpClass24HSesThreshold=_PmG828TpClass24HSesThreshold_Object((1,3,6,1,4,1,3373,1103,11,3,1,16),_PmG828TpClass24HSesThreshold_Type())
pmG828TpClass24HSesThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:pmG828TpClass24HSesThreshold.setStatus(_A)
class _PmG828TpClass24HSepThreshold_Type(Integer32):defaultValue=0
_PmG828TpClass24HSepThreshold_Type.__name__=_C
_PmG828TpClass24HSepThreshold_Object=MibTableColumn
pmG828TpClass24HSepThreshold=_PmG828TpClass24HSepThreshold_Object((1,3,6,1,4,1,3373,1103,11,3,1,17),_PmG828TpClass24HSepThreshold_Type())
pmG828TpClass24HSepThreshold.setMaxAccess(_F)
if mibBuilder.loadTexts:pmG828TpClass24HSepThreshold.setStatus(_A)
_PmG828TpClassRowStatus_Type=RowStatus
_PmG828TpClassRowStatus_Object=MibTableColumn
pmG828TpClassRowStatus=_PmG828TpClassRowStatus_Object((1,3,6,1,4,1,3373,1103,11,3,1,18),_PmG828TpClassRowStatus_Type())
pmG828TpClassRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:pmG828TpClassRowStatus.setStatus(_A)
_PmG828TpMaintTable_Object=MibTable
pmG828TpMaintTable=_PmG828TpMaintTable_Object((1,3,6,1,4,1,3373,1103,11,4))
if mibBuilder.loadTexts:pmG828TpMaintTable.setStatus(_A)
_PmG828TpMaintRecord_Object=MibTableRow
pmG828TpMaintRecord=_PmG828TpMaintRecord_Object((1,3,6,1,4,1,3373,1103,11,4,1))
pmG828TpMaintRecord.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:pmG828TpMaintRecord.setStatus(_A)
class _PmG828TpMaintCounterClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),('clear',1)))
_PmG828TpMaintCounterClear_Type.__name__=_C
_PmG828TpMaintCounterClear_Object=MibTableColumn
pmG828TpMaintCounterClear=_PmG828TpMaintCounterClear_Object((1,3,6,1,4,1,3373,1103,11,4,1,1),_PmG828TpMaintCounterClear_Type())
pmG828TpMaintCounterClear.setMaxAccess(_D)
if mibBuilder.loadTexts:pmG828TpMaintCounterClear.setStatus(_A)
class _PmG828TpMaintAlarmClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),('clear',1)))
_PmG828TpMaintAlarmClear_Type.__name__=_C
_PmG828TpMaintAlarmClear_Object=MibTableColumn
pmG828TpMaintAlarmClear=_PmG828TpMaintAlarmClear_Object((1,3,6,1,4,1,3373,1103,11,4,1,2),_PmG828TpMaintAlarmClear_Type())
pmG828TpMaintAlarmClear.setMaxAccess(_D)
if mibBuilder.loadTexts:pmG828TpMaintAlarmClear.setStatus(_A)
class _PmG828NSesSetUAS_Type(Integer32):defaultValue=10
_PmG828NSesSetUAS_Type.__name__=_C
_PmG828NSesSetUAS_Object=MibScalar
pmG828NSesSetUAS=_PmG828NSesSetUAS_Object((1,3,6,1,4,1,3373,1103,11,5),_PmG828NSesSetUAS_Type())
pmG828NSesSetUAS.setMaxAccess(_D)
if mibBuilder.loadTexts:pmG828NSesSetUAS.setStatus(_A)
class _PmG828NSesResetUAS_Type(Integer32):defaultValue=10
_PmG828NSesResetUAS_Type.__name__=_C
_PmG828NSesResetUAS_Object=MibScalar
pmG828NSesResetUAS=_PmG828NSesResetUAS_Object((1,3,6,1,4,1,3373,1103,11,6),_PmG828NSesResetUAS_Type())
pmG828NSesResetUAS.setMaxAccess(_D)
if mibBuilder.loadTexts:pmG828NSesResetUAS.setStatus(_A)
class _PmG828TpClass15MEsAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_PmG828TpClass15MEsAlarmSeverityCode_Type.__name__=_E
_PmG828TpClass15MEsAlarmSeverityCode_Object=MibScalar
pmG828TpClass15MEsAlarmSeverityCode=_PmG828TpClass15MEsAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,11,7),_PmG828TpClass15MEsAlarmSeverityCode_Type())
pmG828TpClass15MEsAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:pmG828TpClass15MEsAlarmSeverityCode.setStatus(_A)
class _PmG828TpClass15MSesAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_PmG828TpClass15MSesAlarmSeverityCode_Type.__name__=_E
_PmG828TpClass15MSesAlarmSeverityCode_Object=MibScalar
pmG828TpClass15MSesAlarmSeverityCode=_PmG828TpClass15MSesAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,11,8),_PmG828TpClass15MSesAlarmSeverityCode_Type())
pmG828TpClass15MSesAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:pmG828TpClass15MSesAlarmSeverityCode.setStatus(_A)
class _PmG828TpClass24HEsAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_PmG828TpClass24HEsAlarmSeverityCode_Type.__name__=_E
_PmG828TpClass24HEsAlarmSeverityCode_Object=MibScalar
pmG828TpClass24HEsAlarmSeverityCode=_PmG828TpClass24HEsAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,11,9),_PmG828TpClass24HEsAlarmSeverityCode_Type())
pmG828TpClass24HEsAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:pmG828TpClass24HEsAlarmSeverityCode.setStatus(_A)
class _PmG828TpClass24HSesAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_PmG828TpClass24HSesAlarmSeverityCode_Type.__name__=_E
_PmG828TpClass24HSesAlarmSeverityCode_Object=MibScalar
pmG828TpClass24HSesAlarmSeverityCode=_PmG828TpClass24HSesAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,11,10),_PmG828TpClass24HSesAlarmSeverityCode_Type())
pmG828TpClass24HSesAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:pmG828TpClass24HSesAlarmSeverityCode.setStatus(_A)
class _PmG828TpClassUASAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_PmG828TpClassUASAlarmSeverityCode_Type.__name__=_E
_PmG828TpClassUASAlarmSeverityCode_Object=MibScalar
pmG828TpClassUASAlarmSeverityCode=_PmG828TpClassUASAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,11,11),_PmG828TpClassUASAlarmSeverityCode_Type())
pmG828TpClassUASAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:pmG828TpClassUASAlarmSeverityCode.setStatus(_A)
class _PmG828TpClass15MSepAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_PmG828TpClass15MSepAlarmSeverityCode_Type.__name__=_E
_PmG828TpClass15MSepAlarmSeverityCode_Object=MibScalar
pmG828TpClass15MSepAlarmSeverityCode=_PmG828TpClass15MSepAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,11,12),_PmG828TpClass15MSepAlarmSeverityCode_Type())
pmG828TpClass15MSepAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:pmG828TpClass15MSepAlarmSeverityCode.setStatus(_A)
class _PmG828TpClass24HSepAlarmSeverityCode_Type(AlarmSeverityCode):defaultValue=5
_PmG828TpClass24HSepAlarmSeverityCode_Type.__name__=_E
_PmG828TpClass24HSepAlarmSeverityCode_Object=MibScalar
pmG828TpClass24HSepAlarmSeverityCode=_PmG828TpClass24HSepAlarmSeverityCode_Object((1,3,6,1,4,1,3373,1103,11,13),_PmG828TpClass24HSepAlarmSeverityCode_Type())
pmG828TpClass24HSepAlarmSeverityCode.setMaxAccess(_D)
if mibBuilder.loadTexts:pmG828TpClass24HSepAlarmSeverityCode.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'pmG828':pmG828,'pmG828MibVersion':pmG828MibVersion,'pmG828CounterTable':pmG828CounterTable,'pmG828CounterRecord':pmG828CounterRecord,_J:pmG828TPointId,_K:pmG828CounterBlockId,'pmG828CounterBlockType':pmG828CounterBlockType,'pmG828CounterBlockStatus':pmG828CounterBlockStatus,'pmG828CounterTimeStamp':pmG828CounterTimeStamp,'pmG828BBECounter':pmG828BBECounter,'pmG828ESCounter':pmG828ESCounter,'pmG828SESCounter':pmG828SESCounter,'pmG828UASCounter':pmG828UASCounter,'pmG828SEPCounter':pmG828SEPCounter,'pmG828TpClassTable':pmG828TpClassTable,'pmG828TpClassRecord':pmG828TpClassRecord,_H:pmG828TpClassId,'pmG828TpClassStartStop':pmG828TpClassStartStop,'pmG828TpClassLabel':pmG828TpClassLabel,'pmG828TpClassTimeStamp':pmG828TpClassTimeStamp,'pmG828TpClass15MEsAlarm':pmG828TpClass15MEsAlarm,'pmG828TpClass15MSesAlarm':pmG828TpClass15MSesAlarm,'pmG828TpClass15MSepAlarm':pmG828TpClass15MSepAlarm,'pmG828TpClass24HEsAlarm':pmG828TpClass24HEsAlarm,'pmG828TpClass24HSesAlarm':pmG828TpClass24HSesAlarm,'pmG828TpClass24HSepAlarm':pmG828TpClass24HSepAlarm,'pmG828TpClassUasAlarm':pmG828TpClassUasAlarm,'pmG828TpClass15MEsThreshold':pmG828TpClass15MEsThreshold,'pmG828TpClass15MSesThreshold':pmG828TpClass15MSesThreshold,'pmG828TpClass15MSepThreshold':pmG828TpClass15MSepThreshold,'pmG828TpClass24HEsThreshold':pmG828TpClass24HEsThreshold,'pmG828TpClass24HSesThreshold':pmG828TpClass24HSesThreshold,'pmG828TpClass24HSepThreshold':pmG828TpClass24HSepThreshold,'pmG828TpClassRowStatus':pmG828TpClassRowStatus,'pmG828TpMaintTable':pmG828TpMaintTable,'pmG828TpMaintRecord':pmG828TpMaintRecord,'pmG828TpMaintCounterClear':pmG828TpMaintCounterClear,'pmG828TpMaintAlarmClear':pmG828TpMaintAlarmClear,'pmG828NSesSetUAS':pmG828NSesSetUAS,'pmG828NSesResetUAS':pmG828NSesResetUAS,'pmG828TpClass15MEsAlarmSeverityCode':pmG828TpClass15MEsAlarmSeverityCode,'pmG828TpClass15MSesAlarmSeverityCode':pmG828TpClass15MSesAlarmSeverityCode,'pmG828TpClass24HEsAlarmSeverityCode':pmG828TpClass24HEsAlarmSeverityCode,'pmG828TpClass24HSesAlarmSeverityCode':pmG828TpClass24HSesAlarmSeverityCode,'pmG828TpClassUASAlarmSeverityCode':pmG828TpClassUASAlarmSeverityCode,'pmG828TpClass15MSepAlarmSeverityCode':pmG828TpClass15MSepAlarmSeverityCode,'pmG828TpClass24HSepAlarmSeverityCode':pmG828TpClass24HSepAlarmSeverityCode})