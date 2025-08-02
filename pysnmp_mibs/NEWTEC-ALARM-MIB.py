_i='ntcAlmConfGrpV1Standard'
_h='ntcAlmLogSequenceNumber'
_g='ntcAlmLogProbableCause'
_f='ntcAlmLogDescription'
_e='ntcAlmLogSource'
_d='ntcAlmLogCount'
_c='ntcAlmLogTime'
_b='ntcAlmLogSeverity'
_a='ntcAlmLogState'
_Z='ntcAlmLogName'
_Y='ntcAlmHistoryProbableCause'
_X='ntcAlmHistoryDescription'
_W='ntcAlmHistorySource'
_V='ntcAlmHistoryCount'
_U='ntcAlmHistoryTime'
_T='ntcAlmHistorySeverity'
_S='ntcAlmActiveProbableCause'
_R='ntcAlmActiveDescription'
_Q='ntcAlmActiveSource'
_P='ntcAlmActiveCount'
_O='ntcAlmActiveTime'
_N='ntcAlmActiveSeverity'
_M='ntcAlmDefinitionDescription'
_L='ntcAlmDefinitionSeverity'
_K='ntcAlmReset'
_J='ntcAlmLogLogIndex'
_I='ntcAlmHistoryName'
_H='ntcAlmActiveName'
_G='ntcAlmDefinitionName'
_F='Integer32'
_E='not-accessible'
_D='DisplayString'
_C='read-only'
_B='NEWTEC-ALARM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcAlarmState,NtcSystemTime=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcAlarmState','NtcSystemTime')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
ntcAlarm=ModuleIdentity((1,3,6,1,4,1,5835,5,2,200))
if mibBuilder.loadTexts:ntcAlarm.setRevisions(('2014-09-09 09:00','2014-03-18 12:00','2013-03-27 10:00','2012-06-28 12:00'))
_NtcAlmObjects_ObjectIdentity=ObjectIdentity
ntcAlmObjects=_NtcAlmObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,200,1))
if mibBuilder.loadTexts:ntcAlmObjects.setStatus(_A)
class _NtcAlmReset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('reset',1)))
_NtcAlmReset_Type.__name__=_F
_NtcAlmReset_Object=MibScalar
ntcAlmReset=_NtcAlmReset_Object((1,3,6,1,4,1,5835,5,2,200,1,1),_NtcAlmReset_Type())
ntcAlmReset.setMaxAccess('read-write')
if mibBuilder.loadTexts:ntcAlmReset.setStatus(_A)
_NtcAlmDefinitionTable_Object=MibTable
ntcAlmDefinitionTable=_NtcAlmDefinitionTable_Object((1,3,6,1,4,1,5835,5,2,200,1,2))
if mibBuilder.loadTexts:ntcAlmDefinitionTable.setStatus(_A)
_NtcAlmDefinitionEntry_Object=MibTableRow
ntcAlmDefinitionEntry=_NtcAlmDefinitionEntry_Object((1,3,6,1,4,1,5835,5,2,200,1,2,1))
ntcAlmDefinitionEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:ntcAlmDefinitionEntry.setStatus(_A)
class _NtcAlmDefinitionName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_NtcAlmDefinitionName_Type.__name__=_D
_NtcAlmDefinitionName_Object=MibTableColumn
ntcAlmDefinitionName=_NtcAlmDefinitionName_Object((1,3,6,1,4,1,5835,5,2,200,1,2,1,1),_NtcAlmDefinitionName_Type())
ntcAlmDefinitionName.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcAlmDefinitionName.setStatus(_A)
class _NtcAlmDefinitionSeverity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtcAlmDefinitionSeverity_Type.__name__=_D
_NtcAlmDefinitionSeverity_Object=MibTableColumn
ntcAlmDefinitionSeverity=_NtcAlmDefinitionSeverity_Object((1,3,6,1,4,1,5835,5,2,200,1,2,1,2),_NtcAlmDefinitionSeverity_Type())
ntcAlmDefinitionSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAlmDefinitionSeverity.setStatus(_A)
_NtcAlmDefinitionDescription_Type=DisplayString
_NtcAlmDefinitionDescription_Object=MibTableColumn
ntcAlmDefinitionDescription=_NtcAlmDefinitionDescription_Object((1,3,6,1,4,1,5835,5,2,200,1,2,1,3),_NtcAlmDefinitionDescription_Type())
ntcAlmDefinitionDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAlmDefinitionDescription.setStatus(_A)
_NtcAlmActiveTable_Object=MibTable
ntcAlmActiveTable=_NtcAlmActiveTable_Object((1,3,6,1,4,1,5835,5,2,200,1,3))
if mibBuilder.loadTexts:ntcAlmActiveTable.setStatus(_A)
_NtcAlmActiveEntry_Object=MibTableRow
ntcAlmActiveEntry=_NtcAlmActiveEntry_Object((1,3,6,1,4,1,5835,5,2,200,1,3,1))
ntcAlmActiveEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:ntcAlmActiveEntry.setStatus(_A)
class _NtcAlmActiveName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_NtcAlmActiveName_Type.__name__=_D
_NtcAlmActiveName_Object=MibTableColumn
ntcAlmActiveName=_NtcAlmActiveName_Object((1,3,6,1,4,1,5835,5,2,200,1,3,1,1),_NtcAlmActiveName_Type())
ntcAlmActiveName.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcAlmActiveName.setStatus(_A)
class _NtcAlmActiveSeverity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtcAlmActiveSeverity_Type.__name__=_D
_NtcAlmActiveSeverity_Object=MibTableColumn
ntcAlmActiveSeverity=_NtcAlmActiveSeverity_Object((1,3,6,1,4,1,5835,5,2,200,1,3,1,2),_NtcAlmActiveSeverity_Type())
ntcAlmActiveSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAlmActiveSeverity.setStatus(_A)
_NtcAlmActiveTime_Type=NtcSystemTime
_NtcAlmActiveTime_Object=MibTableColumn
ntcAlmActiveTime=_NtcAlmActiveTime_Object((1,3,6,1,4,1,5835,5,2,200,1,3,1,3),_NtcAlmActiveTime_Type())
ntcAlmActiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAlmActiveTime.setStatus(_A)
_NtcAlmActiveCount_Type=Counter32
_NtcAlmActiveCount_Object=MibTableColumn
ntcAlmActiveCount=_NtcAlmActiveCount_Object((1,3,6,1,4,1,5835,5,2,200,1,3,1,4),_NtcAlmActiveCount_Type())
ntcAlmActiveCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAlmActiveCount.setStatus(_A)
class _NtcAlmActiveSource_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NtcAlmActiveSource_Type.__name__=_D
_NtcAlmActiveSource_Object=MibTableColumn
ntcAlmActiveSource=_NtcAlmActiveSource_Object((1,3,6,1,4,1,5835,5,2,200,1,3,1,5),_NtcAlmActiveSource_Type())
ntcAlmActiveSource.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAlmActiveSource.setStatus(_A)
_NtcAlmActiveDescription_Type=DisplayString
_NtcAlmActiveDescription_Object=MibTableColumn
ntcAlmActiveDescription=_NtcAlmActiveDescription_Object((1,3,6,1,4,1,5835,5,2,200,1,3,1,6),_NtcAlmActiveDescription_Type())
ntcAlmActiveDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAlmActiveDescription.setStatus(_A)
class _NtcAlmActiveProbableCause_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NtcAlmActiveProbableCause_Type.__name__=_D
_NtcAlmActiveProbableCause_Object=MibTableColumn
ntcAlmActiveProbableCause=_NtcAlmActiveProbableCause_Object((1,3,6,1,4,1,5835,5,2,200,1,3,1,7),_NtcAlmActiveProbableCause_Type())
ntcAlmActiveProbableCause.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAlmActiveProbableCause.setStatus(_A)
_NtcAlmHistoryTable_Object=MibTable
ntcAlmHistoryTable=_NtcAlmHistoryTable_Object((1,3,6,1,4,1,5835,5,2,200,1,4))
if mibBuilder.loadTexts:ntcAlmHistoryTable.setStatus(_A)
_NtcAlmHistoryEntry_Object=MibTableRow
ntcAlmHistoryEntry=_NtcAlmHistoryEntry_Object((1,3,6,1,4,1,5835,5,2,200,1,4,1))
ntcAlmHistoryEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:ntcAlmHistoryEntry.setStatus(_A)
class _NtcAlmHistoryName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_NtcAlmHistoryName_Type.__name__=_D
_NtcAlmHistoryName_Object=MibTableColumn
ntcAlmHistoryName=_NtcAlmHistoryName_Object((1,3,6,1,4,1,5835,5,2,200,1,4,1,1),_NtcAlmHistoryName_Type())
ntcAlmHistoryName.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcAlmHistoryName.setStatus(_A)
class _NtcAlmHistorySeverity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtcAlmHistorySeverity_Type.__name__=_D
_NtcAlmHistorySeverity_Object=MibTableColumn
ntcAlmHistorySeverity=_NtcAlmHistorySeverity_Object((1,3,6,1,4,1,5835,5,2,200,1,4,1,2),_NtcAlmHistorySeverity_Type())
ntcAlmHistorySeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAlmHistorySeverity.setStatus(_A)
_NtcAlmHistoryTime_Type=NtcSystemTime
_NtcAlmHistoryTime_Object=MibTableColumn
ntcAlmHistoryTime=_NtcAlmHistoryTime_Object((1,3,6,1,4,1,5835,5,2,200,1,4,1,3),_NtcAlmHistoryTime_Type())
ntcAlmHistoryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAlmHistoryTime.setStatus(_A)
_NtcAlmHistoryCount_Type=Counter32
_NtcAlmHistoryCount_Object=MibTableColumn
ntcAlmHistoryCount=_NtcAlmHistoryCount_Object((1,3,6,1,4,1,5835,5,2,200,1,4,1,4),_NtcAlmHistoryCount_Type())
ntcAlmHistoryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAlmHistoryCount.setStatus(_A)
class _NtcAlmHistorySource_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NtcAlmHistorySource_Type.__name__=_D
_NtcAlmHistorySource_Object=MibTableColumn
ntcAlmHistorySource=_NtcAlmHistorySource_Object((1,3,6,1,4,1,5835,5,2,200,1,4,1,5),_NtcAlmHistorySource_Type())
ntcAlmHistorySource.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAlmHistorySource.setStatus(_A)
_NtcAlmHistoryDescription_Type=DisplayString
_NtcAlmHistoryDescription_Object=MibTableColumn
ntcAlmHistoryDescription=_NtcAlmHistoryDescription_Object((1,3,6,1,4,1,5835,5,2,200,1,4,1,6),_NtcAlmHistoryDescription_Type())
ntcAlmHistoryDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAlmHistoryDescription.setStatus(_A)
class _NtcAlmHistoryProbableCause_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NtcAlmHistoryProbableCause_Type.__name__=_D
_NtcAlmHistoryProbableCause_Object=MibTableColumn
ntcAlmHistoryProbableCause=_NtcAlmHistoryProbableCause_Object((1,3,6,1,4,1,5835,5,2,200,1,4,1,7),_NtcAlmHistoryProbableCause_Type())
ntcAlmHistoryProbableCause.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAlmHistoryProbableCause.setStatus(_A)
_NtcAlmLogTable_Object=MibTable
ntcAlmLogTable=_NtcAlmLogTable_Object((1,3,6,1,4,1,5835,5,2,200,1,5))
if mibBuilder.loadTexts:ntcAlmLogTable.setStatus(_A)
_NtcAlmLogEntry_Object=MibTableRow
ntcAlmLogEntry=_NtcAlmLogEntry_Object((1,3,6,1,4,1,5835,5,2,200,1,5,1))
ntcAlmLogEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:ntcAlmLogEntry.setStatus(_A)
_NtcAlmLogLogIndex_Type=Unsigned32
_NtcAlmLogLogIndex_Object=MibTableColumn
ntcAlmLogLogIndex=_NtcAlmLogLogIndex_Object((1,3,6,1,4,1,5835,5,2,200,1,5,1,1),_NtcAlmLogLogIndex_Type())
ntcAlmLogLogIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ntcAlmLogLogIndex.setStatus(_A)
class _NtcAlmLogName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_NtcAlmLogName_Type.__name__=_D
_NtcAlmLogName_Object=MibTableColumn
ntcAlmLogName=_NtcAlmLogName_Object((1,3,6,1,4,1,5835,5,2,200,1,5,1,2),_NtcAlmLogName_Type())
ntcAlmLogName.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAlmLogName.setStatus(_A)
_NtcAlmLogState_Type=NtcAlarmState
_NtcAlmLogState_Object=MibTableColumn
ntcAlmLogState=_NtcAlmLogState_Object((1,3,6,1,4,1,5835,5,2,200,1,5,1,3),_NtcAlmLogState_Type())
ntcAlmLogState.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAlmLogState.setStatus(_A)
class _NtcAlmLogSeverity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NtcAlmLogSeverity_Type.__name__=_D
_NtcAlmLogSeverity_Object=MibTableColumn
ntcAlmLogSeverity=_NtcAlmLogSeverity_Object((1,3,6,1,4,1,5835,5,2,200,1,5,1,4),_NtcAlmLogSeverity_Type())
ntcAlmLogSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAlmLogSeverity.setStatus(_A)
_NtcAlmLogTime_Type=NtcSystemTime
_NtcAlmLogTime_Object=MibTableColumn
ntcAlmLogTime=_NtcAlmLogTime_Object((1,3,6,1,4,1,5835,5,2,200,1,5,1,5),_NtcAlmLogTime_Type())
ntcAlmLogTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAlmLogTime.setStatus(_A)
_NtcAlmLogCount_Type=Counter32
_NtcAlmLogCount_Object=MibTableColumn
ntcAlmLogCount=_NtcAlmLogCount_Object((1,3,6,1,4,1,5835,5,2,200,1,5,1,6),_NtcAlmLogCount_Type())
ntcAlmLogCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAlmLogCount.setStatus(_A)
class _NtcAlmLogSource_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NtcAlmLogSource_Type.__name__=_D
_NtcAlmLogSource_Object=MibTableColumn
ntcAlmLogSource=_NtcAlmLogSource_Object((1,3,6,1,4,1,5835,5,2,200,1,5,1,7),_NtcAlmLogSource_Type())
ntcAlmLogSource.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAlmLogSource.setStatus(_A)
_NtcAlmLogDescription_Type=DisplayString
_NtcAlmLogDescription_Object=MibTableColumn
ntcAlmLogDescription=_NtcAlmLogDescription_Object((1,3,6,1,4,1,5835,5,2,200,1,5,1,8),_NtcAlmLogDescription_Type())
ntcAlmLogDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAlmLogDescription.setStatus(_A)
class _NtcAlmLogProbableCause_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_NtcAlmLogProbableCause_Type.__name__=_D
_NtcAlmLogProbableCause_Object=MibTableColumn
ntcAlmLogProbableCause=_NtcAlmLogProbableCause_Object((1,3,6,1,4,1,5835,5,2,200,1,5,1,9),_NtcAlmLogProbableCause_Type())
ntcAlmLogProbableCause.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAlmLogProbableCause.setStatus(_A)
_NtcAlmLogSequenceNumber_Type=Counter32
_NtcAlmLogSequenceNumber_Object=MibTableColumn
ntcAlmLogSequenceNumber=_NtcAlmLogSequenceNumber_Object((1,3,6,1,4,1,5835,5,2,200,1,5,1,10),_NtcAlmLogSequenceNumber_Type())
ntcAlmLogSequenceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcAlmLogSequenceNumber.setStatus(_A)
_NtcAlmConformance_ObjectIdentity=ObjectIdentity
ntcAlmConformance=_NtcAlmConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,200,2))
if mibBuilder.loadTexts:ntcAlmConformance.setStatus(_A)
_NtcAlmConfCompliance_ObjectIdentity=ObjectIdentity
ntcAlmConfCompliance=_NtcAlmConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,200,2,1))
if mibBuilder.loadTexts:ntcAlmConfCompliance.setStatus(_A)
_NtcAlmConfGroup_ObjectIdentity=ObjectIdentity
ntcAlmConfGroup=_NtcAlmConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,200,2,2))
if mibBuilder.loadTexts:ntcAlmConfGroup.setStatus(_A)
ntcAlmConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,200,2,2,1))
ntcAlmConfGrpV1Standard.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:ntcAlmConfGrpV1Standard.setStatus(_A)
ntcAlmConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,200,2,1,1))
ntcAlmConfCompV1Standard.setObjects((_B,_i))
if mibBuilder.loadTexts:ntcAlmConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcAlarm':ntcAlarm,'ntcAlmObjects':ntcAlmObjects,_K:ntcAlmReset,'ntcAlmDefinitionTable':ntcAlmDefinitionTable,'ntcAlmDefinitionEntry':ntcAlmDefinitionEntry,_G:ntcAlmDefinitionName,_L:ntcAlmDefinitionSeverity,_M:ntcAlmDefinitionDescription,'ntcAlmActiveTable':ntcAlmActiveTable,'ntcAlmActiveEntry':ntcAlmActiveEntry,_H:ntcAlmActiveName,_N:ntcAlmActiveSeverity,_O:ntcAlmActiveTime,_P:ntcAlmActiveCount,_Q:ntcAlmActiveSource,_R:ntcAlmActiveDescription,_S:ntcAlmActiveProbableCause,'ntcAlmHistoryTable':ntcAlmHistoryTable,'ntcAlmHistoryEntry':ntcAlmHistoryEntry,_I:ntcAlmHistoryName,_T:ntcAlmHistorySeverity,_U:ntcAlmHistoryTime,_V:ntcAlmHistoryCount,_W:ntcAlmHistorySource,_X:ntcAlmHistoryDescription,_Y:ntcAlmHistoryProbableCause,'ntcAlmLogTable':ntcAlmLogTable,'ntcAlmLogEntry':ntcAlmLogEntry,_J:ntcAlmLogLogIndex,_Z:ntcAlmLogName,_a:ntcAlmLogState,_b:ntcAlmLogSeverity,_c:ntcAlmLogTime,_d:ntcAlmLogCount,_e:ntcAlmLogSource,_f:ntcAlmLogDescription,_g:ntcAlmLogProbableCause,_h:ntcAlmLogSequenceNumber,'ntcAlmConformance':ntcAlmConformance,'ntcAlmConfCompliance':ntcAlmConfCompliance,'ntcAlmConfCompV1Standard':ntcAlmConfCompV1Standard,'ntcAlmConfGroup':ntcAlmConfGroup,_i:ntcAlmConfGrpV1Standard})