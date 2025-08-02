_q='cienaWsPlatformAlarmGroup'
_p='alarmStatisticsType'
_o='alarmStatisticsCumulative'
_n='alarmStatisticsCount'
_m='alarmStatisticsDisabled'
_l='alarmStatisticsActive'
_k='definedAlarmDescription'
_j='definedAlarmInstance'
_i='definedAlarmSeverity'
_h='definedAlarmCap'
_g='definedAlarmThreshold'
_f='definedAlarmActive'
_e='definedAlarmEnabled'
_d='definedAlarmTableId'
_c='historyAlarmMemberIdentifier'
_b='historyAlarmGroupIdentifier'
_a='historyAlarmSiteIdentifier'
_Z='historyAlarmDescription'
_Y='historyAlarmInstance'
_X='historyAlarmLocalDateTime'
_W='historyAlarmSeverity'
_V='historyAlarmTableId'
_U='historyAlarmInstanceId'
_T='historyAlarmReason'
_S='activeAlarmMemberIdentifier'
_R='activeAlarmGroupIdentifier'
_Q='activeAlarmSiteIdentifier'
_P='activeAlarmIntermittent'
_O='activeAlarmDescription'
_N='activeAlarmInstance'
_M='activeAlarmLocalDateTime'
_L='activeAlarmSeverity'
_K='activeAlarmTableId'
_J='activeAlarmAcknowledged'
_I='alarmStatisticsIndex'
_H='definedAlarmId'
_G='historyAlarmId'
_F='activeAlarmInstanceId'
_E='not-accessible'
_D='Integer32'
_C='read-only'
_B='CIENA-WS-PLATFORM-ALARM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaWsPlatformConfig,=mibBuilder.importSymbols('CIENA-WS-MIB','cienaWsPlatformConfig')
StringMaxl16,StringMaxl32,StringMaxl44=mibBuilder.importSymbols('CIENA-WS-PLATFORM-TYPEDEFS-MIB','StringMaxl16','StringMaxl32','StringMaxl44')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
cienaWsPlatformAlarmMIB=ModuleIdentity((1,3,6,1,4,1,1271,3,5,4))
if mibBuilder.loadTexts:cienaWsPlatformAlarmMIB.setRevisions(('2018-09-20 00:00','2018-08-14 00:00'))
class AlarmReason(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5,6,7,9,10)));namedValues=NamedValues(*(('reset',1),('set',2),('acknowledge',5),('clear',6),('delete',7),('config',9),('intermittent',10)))
class AlarmSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5,6,8)));namedValues=NamedValues(*(('cleared',1),('critical',3),('major',4),('minor',5),('warning',6),('info',8)))
_CienaWsPlatformAlarmObjects_ObjectIdentity=ObjectIdentity
cienaWsPlatformAlarmObjects=_CienaWsPlatformAlarmObjects_ObjectIdentity((1,3,6,1,4,1,1271,3,5,4,1))
_CienaWsPlatformAlarmConformance_ObjectIdentity=ObjectIdentity
cienaWsPlatformAlarmConformance=_CienaWsPlatformAlarmConformance_ObjectIdentity((1,3,6,1,4,1,1271,3,5,4,2))
_CienaWsPlatformAlarmGroups_ObjectIdentity=ObjectIdentity
cienaWsPlatformAlarmGroups=_CienaWsPlatformAlarmGroups_ObjectIdentity((1,3,6,1,4,1,1271,3,5,4,2,1))
_CienaWsPlatformAlarmCompliances_ObjectIdentity=ObjectIdentity
cienaWsPlatformAlarmCompliances=_CienaWsPlatformAlarmCompliances_ObjectIdentity((1,3,6,1,4,1,1271,3,5,4,2,2))
_ActiveAlarmTable_Object=MibTable
activeAlarmTable=_ActiveAlarmTable_Object((1,3,6,1,4,1,1271,3,5,4,3))
if mibBuilder.loadTexts:activeAlarmTable.setStatus(_A)
_ActiveAlarmEntry_Object=MibTableRow
activeAlarmEntry=_ActiveAlarmEntry_Object((1,3,6,1,4,1,1271,3,5,4,3,1))
activeAlarmEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:activeAlarmEntry.setStatus(_A)
class _ActiveAlarmInstanceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ActiveAlarmInstanceId_Type.__name__=_D
_ActiveAlarmInstanceId_Object=MibTableColumn
activeAlarmInstanceId=_ActiveAlarmInstanceId_Object((1,3,6,1,4,1,1271,3,5,4,3,1,1),_ActiveAlarmInstanceId_Type())
activeAlarmInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:activeAlarmInstanceId.setStatus(_A)
_ActiveAlarmAcknowledged_Type=TruthValue
_ActiveAlarmAcknowledged_Object=MibTableColumn
activeAlarmAcknowledged=_ActiveAlarmAcknowledged_Object((1,3,6,1,4,1,1271,3,5,4,3,1,2),_ActiveAlarmAcknowledged_Type())
activeAlarmAcknowledged.setMaxAccess(_C)
if mibBuilder.loadTexts:activeAlarmAcknowledged.setStatus(_A)
_ActiveAlarmTableId_Type=Unsigned32
_ActiveAlarmTableId_Object=MibTableColumn
activeAlarmTableId=_ActiveAlarmTableId_Object((1,3,6,1,4,1,1271,3,5,4,3,1,3),_ActiveAlarmTableId_Type())
activeAlarmTableId.setMaxAccess(_C)
if mibBuilder.loadTexts:activeAlarmTableId.setStatus(_A)
_ActiveAlarmSeverity_Type=AlarmSeverity
_ActiveAlarmSeverity_Object=MibTableColumn
activeAlarmSeverity=_ActiveAlarmSeverity_Object((1,3,6,1,4,1,1271,3,5,4,3,1,4),_ActiveAlarmSeverity_Type())
activeAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:activeAlarmSeverity.setStatus(_A)
_ActiveAlarmLocalDateTime_Type=StringMaxl32
_ActiveAlarmLocalDateTime_Object=MibTableColumn
activeAlarmLocalDateTime=_ActiveAlarmLocalDateTime_Object((1,3,6,1,4,1,1271,3,5,4,3,1,5),_ActiveAlarmLocalDateTime_Type())
activeAlarmLocalDateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:activeAlarmLocalDateTime.setStatus(_A)
_ActiveAlarmInstance_Type=StringMaxl32
_ActiveAlarmInstance_Object=MibTableColumn
activeAlarmInstance=_ActiveAlarmInstance_Object((1,3,6,1,4,1,1271,3,5,4,3,1,6),_ActiveAlarmInstance_Type())
activeAlarmInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:activeAlarmInstance.setStatus(_A)
_ActiveAlarmDescription_Type=StringMaxl44
_ActiveAlarmDescription_Object=MibTableColumn
activeAlarmDescription=_ActiveAlarmDescription_Object((1,3,6,1,4,1,1271,3,5,4,3,1,7),_ActiveAlarmDescription_Type())
activeAlarmDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:activeAlarmDescription.setStatus(_A)
_ActiveAlarmIntermittent_Type=TruthValue
_ActiveAlarmIntermittent_Object=MibTableColumn
activeAlarmIntermittent=_ActiveAlarmIntermittent_Object((1,3,6,1,4,1,1271,3,5,4,3,1,8),_ActiveAlarmIntermittent_Type())
activeAlarmIntermittent.setMaxAccess(_C)
if mibBuilder.loadTexts:activeAlarmIntermittent.setStatus(_A)
_ActiveAlarmSiteIdentifier_Type=Unsigned32
_ActiveAlarmSiteIdentifier_Object=MibTableColumn
activeAlarmSiteIdentifier=_ActiveAlarmSiteIdentifier_Object((1,3,6,1,4,1,1271,3,5,4,3,1,9),_ActiveAlarmSiteIdentifier_Type())
activeAlarmSiteIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:activeAlarmSiteIdentifier.setStatus(_A)
_ActiveAlarmGroupIdentifier_Type=Unsigned32
_ActiveAlarmGroupIdentifier_Object=MibTableColumn
activeAlarmGroupIdentifier=_ActiveAlarmGroupIdentifier_Object((1,3,6,1,4,1,1271,3,5,4,3,1,10),_ActiveAlarmGroupIdentifier_Type())
activeAlarmGroupIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:activeAlarmGroupIdentifier.setStatus(_A)
_ActiveAlarmMemberIdentifier_Type=Unsigned32
_ActiveAlarmMemberIdentifier_Object=MibTableColumn
activeAlarmMemberIdentifier=_ActiveAlarmMemberIdentifier_Object((1,3,6,1,4,1,1271,3,5,4,3,1,11),_ActiveAlarmMemberIdentifier_Type())
activeAlarmMemberIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:activeAlarmMemberIdentifier.setStatus(_A)
_HistoryAlarmTable_Object=MibTable
historyAlarmTable=_HistoryAlarmTable_Object((1,3,6,1,4,1,1271,3,5,4,4))
if mibBuilder.loadTexts:historyAlarmTable.setStatus(_A)
_HistoryAlarmEntry_Object=MibTableRow
historyAlarmEntry=_HistoryAlarmEntry_Object((1,3,6,1,4,1,1271,3,5,4,4,1))
historyAlarmEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:historyAlarmEntry.setStatus(_A)
class _HistoryAlarmId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HistoryAlarmId_Type.__name__=_D
_HistoryAlarmId_Object=MibTableColumn
historyAlarmId=_HistoryAlarmId_Object((1,3,6,1,4,1,1271,3,5,4,4,1,1),_HistoryAlarmId_Type())
historyAlarmId.setMaxAccess(_E)
if mibBuilder.loadTexts:historyAlarmId.setStatus(_A)
_HistoryAlarmReason_Type=AlarmReason
_HistoryAlarmReason_Object=MibTableColumn
historyAlarmReason=_HistoryAlarmReason_Object((1,3,6,1,4,1,1271,3,5,4,4,1,2),_HistoryAlarmReason_Type())
historyAlarmReason.setMaxAccess(_C)
if mibBuilder.loadTexts:historyAlarmReason.setStatus(_A)
_HistoryAlarmInstanceId_Type=Unsigned32
_HistoryAlarmInstanceId_Object=MibTableColumn
historyAlarmInstanceId=_HistoryAlarmInstanceId_Object((1,3,6,1,4,1,1271,3,5,4,4,1,3),_HistoryAlarmInstanceId_Type())
historyAlarmInstanceId.setMaxAccess(_C)
if mibBuilder.loadTexts:historyAlarmInstanceId.setStatus(_A)
_HistoryAlarmTableId_Type=Unsigned32
_HistoryAlarmTableId_Object=MibTableColumn
historyAlarmTableId=_HistoryAlarmTableId_Object((1,3,6,1,4,1,1271,3,5,4,4,1,4),_HistoryAlarmTableId_Type())
historyAlarmTableId.setMaxAccess(_C)
if mibBuilder.loadTexts:historyAlarmTableId.setStatus(_A)
_HistoryAlarmSeverity_Type=AlarmSeverity
_HistoryAlarmSeverity_Object=MibTableColumn
historyAlarmSeverity=_HistoryAlarmSeverity_Object((1,3,6,1,4,1,1271,3,5,4,4,1,5),_HistoryAlarmSeverity_Type())
historyAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:historyAlarmSeverity.setStatus(_A)
_HistoryAlarmLocalDateTime_Type=StringMaxl32
_HistoryAlarmLocalDateTime_Object=MibTableColumn
historyAlarmLocalDateTime=_HistoryAlarmLocalDateTime_Object((1,3,6,1,4,1,1271,3,5,4,4,1,6),_HistoryAlarmLocalDateTime_Type())
historyAlarmLocalDateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:historyAlarmLocalDateTime.setStatus(_A)
_HistoryAlarmInstance_Type=StringMaxl32
_HistoryAlarmInstance_Object=MibTableColumn
historyAlarmInstance=_HistoryAlarmInstance_Object((1,3,6,1,4,1,1271,3,5,4,4,1,7),_HistoryAlarmInstance_Type())
historyAlarmInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:historyAlarmInstance.setStatus(_A)
_HistoryAlarmDescription_Type=StringMaxl44
_HistoryAlarmDescription_Object=MibTableColumn
historyAlarmDescription=_HistoryAlarmDescription_Object((1,3,6,1,4,1,1271,3,5,4,4,1,8),_HistoryAlarmDescription_Type())
historyAlarmDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:historyAlarmDescription.setStatus(_A)
_HistoryAlarmSiteIdentifier_Type=Unsigned32
_HistoryAlarmSiteIdentifier_Object=MibTableColumn
historyAlarmSiteIdentifier=_HistoryAlarmSiteIdentifier_Object((1,3,6,1,4,1,1271,3,5,4,4,1,9),_HistoryAlarmSiteIdentifier_Type())
historyAlarmSiteIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:historyAlarmSiteIdentifier.setStatus(_A)
_HistoryAlarmGroupIdentifier_Type=Unsigned32
_HistoryAlarmGroupIdentifier_Object=MibTableColumn
historyAlarmGroupIdentifier=_HistoryAlarmGroupIdentifier_Object((1,3,6,1,4,1,1271,3,5,4,4,1,10),_HistoryAlarmGroupIdentifier_Type())
historyAlarmGroupIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:historyAlarmGroupIdentifier.setStatus(_A)
_HistoryAlarmMemberIdentifier_Type=Unsigned32
_HistoryAlarmMemberIdentifier_Object=MibTableColumn
historyAlarmMemberIdentifier=_HistoryAlarmMemberIdentifier_Object((1,3,6,1,4,1,1271,3,5,4,4,1,11),_HistoryAlarmMemberIdentifier_Type())
historyAlarmMemberIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:historyAlarmMemberIdentifier.setStatus(_A)
_DefinedAlarmTable_Object=MibTable
definedAlarmTable=_DefinedAlarmTable_Object((1,3,6,1,4,1,1271,3,5,4,5))
if mibBuilder.loadTexts:definedAlarmTable.setStatus(_A)
_DefinedAlarmEntry_Object=MibTableRow
definedAlarmEntry=_DefinedAlarmEntry_Object((1,3,6,1,4,1,1271,3,5,4,5,1))
definedAlarmEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:definedAlarmEntry.setStatus(_A)
class _DefinedAlarmId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DefinedAlarmId_Type.__name__=_D
_DefinedAlarmId_Object=MibTableColumn
definedAlarmId=_DefinedAlarmId_Object((1,3,6,1,4,1,1271,3,5,4,5,1,1),_DefinedAlarmId_Type())
definedAlarmId.setMaxAccess(_E)
if mibBuilder.loadTexts:definedAlarmId.setStatus(_A)
class _DefinedAlarmTableId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DefinedAlarmTableId_Type.__name__=_D
_DefinedAlarmTableId_Object=MibTableColumn
definedAlarmTableId=_DefinedAlarmTableId_Object((1,3,6,1,4,1,1271,3,5,4,5,1,2),_DefinedAlarmTableId_Type())
definedAlarmTableId.setMaxAccess(_C)
if mibBuilder.loadTexts:definedAlarmTableId.setStatus(_A)
_DefinedAlarmEnabled_Type=TruthValue
_DefinedAlarmEnabled_Object=MibTableColumn
definedAlarmEnabled=_DefinedAlarmEnabled_Object((1,3,6,1,4,1,1271,3,5,4,5,1,3),_DefinedAlarmEnabled_Type())
definedAlarmEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:definedAlarmEnabled.setStatus(_A)
_DefinedAlarmActive_Type=TruthValue
_DefinedAlarmActive_Object=MibTableColumn
definedAlarmActive=_DefinedAlarmActive_Object((1,3,6,1,4,1,1271,3,5,4,5,1,4),_DefinedAlarmActive_Type())
definedAlarmActive.setMaxAccess(_C)
if mibBuilder.loadTexts:definedAlarmActive.setStatus(_A)
_DefinedAlarmThreshold_Type=Unsigned32
_DefinedAlarmThreshold_Object=MibTableColumn
definedAlarmThreshold=_DefinedAlarmThreshold_Object((1,3,6,1,4,1,1271,3,5,4,5,1,5),_DefinedAlarmThreshold_Type())
definedAlarmThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:definedAlarmThreshold.setStatus(_A)
_DefinedAlarmCap_Type=Unsigned32
_DefinedAlarmCap_Object=MibTableColumn
definedAlarmCap=_DefinedAlarmCap_Object((1,3,6,1,4,1,1271,3,5,4,5,1,6),_DefinedAlarmCap_Type())
definedAlarmCap.setMaxAccess(_C)
if mibBuilder.loadTexts:definedAlarmCap.setStatus(_A)
_DefinedAlarmSeverity_Type=AlarmSeverity
_DefinedAlarmSeverity_Object=MibTableColumn
definedAlarmSeverity=_DefinedAlarmSeverity_Object((1,3,6,1,4,1,1271,3,5,4,5,1,7),_DefinedAlarmSeverity_Type())
definedAlarmSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:definedAlarmSeverity.setStatus(_A)
_DefinedAlarmInstance_Type=StringMaxl16
_DefinedAlarmInstance_Object=MibTableColumn
definedAlarmInstance=_DefinedAlarmInstance_Object((1,3,6,1,4,1,1271,3,5,4,5,1,8),_DefinedAlarmInstance_Type())
definedAlarmInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:definedAlarmInstance.setStatus(_A)
_DefinedAlarmDescription_Type=StringMaxl44
_DefinedAlarmDescription_Object=MibTableColumn
definedAlarmDescription=_DefinedAlarmDescription_Object((1,3,6,1,4,1,1271,3,5,4,5,1,9),_DefinedAlarmDescription_Type())
definedAlarmDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:definedAlarmDescription.setStatus(_A)
_AlarmStatisticsTable_Object=MibTable
alarmStatisticsTable=_AlarmStatisticsTable_Object((1,3,6,1,4,1,1271,3,5,4,6))
if mibBuilder.loadTexts:alarmStatisticsTable.setStatus(_A)
_AlarmStatisticsEntry_Object=MibTableRow
alarmStatisticsEntry=_AlarmStatisticsEntry_Object((1,3,6,1,4,1,1271,3,5,4,6,1))
alarmStatisticsEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:alarmStatisticsEntry.setStatus(_A)
class _AlarmStatisticsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AlarmStatisticsIndex_Type.__name__=_D
_AlarmStatisticsIndex_Object=MibTableColumn
alarmStatisticsIndex=_AlarmStatisticsIndex_Object((1,3,6,1,4,1,1271,3,5,4,6,1,1),_AlarmStatisticsIndex_Type())
alarmStatisticsIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:alarmStatisticsIndex.setStatus(_A)
_AlarmStatisticsActive_Type=TruthValue
_AlarmStatisticsActive_Object=MibTableColumn
alarmStatisticsActive=_AlarmStatisticsActive_Object((1,3,6,1,4,1,1271,3,5,4,6,1,2),_AlarmStatisticsActive_Type())
alarmStatisticsActive.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmStatisticsActive.setStatus(_A)
_AlarmStatisticsDisabled_Type=TruthValue
_AlarmStatisticsDisabled_Object=MibTableColumn
alarmStatisticsDisabled=_AlarmStatisticsDisabled_Object((1,3,6,1,4,1,1271,3,5,4,6,1,3),_AlarmStatisticsDisabled_Type())
alarmStatisticsDisabled.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmStatisticsDisabled.setStatus(_A)
_AlarmStatisticsCount_Type=Unsigned32
_AlarmStatisticsCount_Object=MibTableColumn
alarmStatisticsCount=_AlarmStatisticsCount_Object((1,3,6,1,4,1,1271,3,5,4,6,1,4),_AlarmStatisticsCount_Type())
alarmStatisticsCount.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmStatisticsCount.setStatus(_A)
_AlarmStatisticsCumulative_Type=Unsigned32
_AlarmStatisticsCumulative_Object=MibTableColumn
alarmStatisticsCumulative=_AlarmStatisticsCumulative_Object((1,3,6,1,4,1,1271,3,5,4,6,1,5),_AlarmStatisticsCumulative_Type())
alarmStatisticsCumulative.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmStatisticsCumulative.setStatus(_A)
_AlarmStatisticsType_Type=StringMaxl32
_AlarmStatisticsType_Object=MibTableColumn
alarmStatisticsType=_AlarmStatisticsType_Object((1,3,6,1,4,1,1271,3,5,4,6,1,6),_AlarmStatisticsType_Type())
alarmStatisticsType.setMaxAccess(_C)
if mibBuilder.loadTexts:alarmStatisticsType.setStatus(_A)
cienaWsPlatformAlarmGroup=ObjectGroup((1,3,6,1,4,1,1271,3,5,4,2,1,1))
cienaWsPlatformAlarmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:cienaWsPlatformAlarmGroup.setStatus(_A)
cienaWsPlatformAlarmCompliance=ModuleCompliance((1,3,6,1,4,1,1271,3,5,4,2,2,1))
cienaWsPlatformAlarmCompliance.setObjects((_B,_q))
if mibBuilder.loadTexts:cienaWsPlatformAlarmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AlarmReason':AlarmReason,'AlarmSeverity':AlarmSeverity,'cienaWsPlatformAlarmMIB':cienaWsPlatformAlarmMIB,'cienaWsPlatformAlarmObjects':cienaWsPlatformAlarmObjects,'cienaWsPlatformAlarmConformance':cienaWsPlatformAlarmConformance,'cienaWsPlatformAlarmGroups':cienaWsPlatformAlarmGroups,_q:cienaWsPlatformAlarmGroup,'cienaWsPlatformAlarmCompliances':cienaWsPlatformAlarmCompliances,'cienaWsPlatformAlarmCompliance':cienaWsPlatformAlarmCompliance,'activeAlarmTable':activeAlarmTable,'activeAlarmEntry':activeAlarmEntry,_F:activeAlarmInstanceId,_J:activeAlarmAcknowledged,_K:activeAlarmTableId,_L:activeAlarmSeverity,_M:activeAlarmLocalDateTime,_N:activeAlarmInstance,_O:activeAlarmDescription,_P:activeAlarmIntermittent,_Q:activeAlarmSiteIdentifier,_R:activeAlarmGroupIdentifier,_S:activeAlarmMemberIdentifier,'historyAlarmTable':historyAlarmTable,'historyAlarmEntry':historyAlarmEntry,_G:historyAlarmId,_T:historyAlarmReason,_U:historyAlarmInstanceId,_V:historyAlarmTableId,_W:historyAlarmSeverity,_X:historyAlarmLocalDateTime,_Y:historyAlarmInstance,_Z:historyAlarmDescription,_a:historyAlarmSiteIdentifier,_b:historyAlarmGroupIdentifier,_c:historyAlarmMemberIdentifier,'definedAlarmTable':definedAlarmTable,'definedAlarmEntry':definedAlarmEntry,_H:definedAlarmId,_d:definedAlarmTableId,_e:definedAlarmEnabled,_f:definedAlarmActive,_g:definedAlarmThreshold,_h:definedAlarmCap,_i:definedAlarmSeverity,_j:definedAlarmInstance,_k:definedAlarmDescription,'alarmStatisticsTable':alarmStatisticsTable,'alarmStatisticsEntry':alarmStatisticsEntry,_I:alarmStatisticsIndex,_l:alarmStatisticsActive,_m:alarmStatisticsDisabled,_n:alarmStatisticsCount,_o:alarmStatisticsCumulative,_p:alarmStatisticsType})