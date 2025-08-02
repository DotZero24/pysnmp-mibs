_o='cienaWsAlarmGroup'
_n='cwsAlarmStatisticsType'
_m='cwsAlarmStatisticsCumulative'
_l='cwsAlarmStatisticsCount'
_k='cwsAlarmStatisticsDisabled'
_j='cwsAlarmStatisticsActive'
_i='cwsAlarmDefinedDescription'
_h='cwsAlarmDefinedInstance'
_g='cwsAlarmDefinedSeverity'
_f='cwsAlarmDefinedCap'
_e='cwsAlarmDefinedThreshold'
_d='cwsAlarmDefinedActive'
_c='cwsAlarmDefinedEnabled'
_b='cwsAlarmHistoryMemberIdentifier'
_a='cwsAlarmHistoryGroupIdentifier'
_Z='cwsAlarmHistorySiteIdentifier'
_Y='cwsAlarmHistoryDescription'
_X='cwsAlarmHistoryInstance'
_W='cwsAlarmHistoryLocalDateTime'
_V='cwsAlarmHistorySeverity'
_U='cwsAlarmHistoryAlarmTableId'
_T='cwsAlarmHistoryAlarmInstanceId'
_S='cwsAlarmHistoryReason'
_R='cwsAlarmActiveMemberIdentifier'
_Q='cwsAlarmActiveGroupIdentifier'
_P='cwsAlarmActiveSiteIdentifier'
_O='cwsAlarmActiveDescription'
_N='cwsAlarmActiveInstance'
_M='cwsAlarmActiveLocalDateTime'
_L='cwsAlarmActiveSeverity'
_K='cwsAlarmActiveAlarmTableId'
_J='cwsAlarmActiveAcknowledged'
_I='cwsAlarmStatisticsIndex'
_H='cwsAlarmDefinedAlarmTableId'
_G='cwsAlarmHistoryHistoryId'
_F='cwsAlarmActiveAlarmInstanceId'
_E='not-accessible'
_D='Integer32'
_C='read-only'
_B='CIENA-WS-ALARM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cienaWsConfig,=mibBuilder.importSymbols('CIENA-WS-MIB','cienaWsConfig')
StringMaxl16,StringMaxl32,StringMaxl44=mibBuilder.importSymbols('CIENA-WS-TYPEDEFS-MIB','StringMaxl16','StringMaxl32','StringMaxl44')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
cienaWsAlarmMIB=ModuleIdentity((1,3,6,1,4,1,1271,3,4,4))
if mibBuilder.loadTexts:cienaWsAlarmMIB.setRevisions(('2017-03-14 00:00','2016-12-12 00:00','2016-06-27 00:00','2015-05-20 00:00'))
class AlarmReason(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,5,6,7,9)));namedValues=NamedValues(*(('reset',1),('set',2),('acknowledge',5),('clear',6),('delete',7),('config',9)))
class AlarmSeverity(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4,5,6,8)));namedValues=NamedValues(*(('cleared',1),('critical',3),('major',4),('minor',5),('warning',6),('info',8)))
_CienaWsAlarmObjects_ObjectIdentity=ObjectIdentity
cienaWsAlarmObjects=_CienaWsAlarmObjects_ObjectIdentity((1,3,6,1,4,1,1271,3,4,4,1))
_CienaWsAlarmConformance_ObjectIdentity=ObjectIdentity
cienaWsAlarmConformance=_CienaWsAlarmConformance_ObjectIdentity((1,3,6,1,4,1,1271,3,4,4,2))
_CienaWsAlarmGroups_ObjectIdentity=ObjectIdentity
cienaWsAlarmGroups=_CienaWsAlarmGroups_ObjectIdentity((1,3,6,1,4,1,1271,3,4,4,2,1))
_CienaWsAlarmCompliances_ObjectIdentity=ObjectIdentity
cienaWsAlarmCompliances=_CienaWsAlarmCompliances_ObjectIdentity((1,3,6,1,4,1,1271,3,4,4,2,2))
_CwsAlarmActiveTable_Object=MibTable
cwsAlarmActiveTable=_CwsAlarmActiveTable_Object((1,3,6,1,4,1,1271,3,4,4,3))
if mibBuilder.loadTexts:cwsAlarmActiveTable.setStatus(_A)
_CwsAlarmActiveEntry_Object=MibTableRow
cwsAlarmActiveEntry=_CwsAlarmActiveEntry_Object((1,3,6,1,4,1,1271,3,4,4,3,1))
cwsAlarmActiveEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cwsAlarmActiveEntry.setStatus(_A)
class _CwsAlarmActiveAlarmInstanceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsAlarmActiveAlarmInstanceId_Type.__name__=_D
_CwsAlarmActiveAlarmInstanceId_Object=MibTableColumn
cwsAlarmActiveAlarmInstanceId=_CwsAlarmActiveAlarmInstanceId_Object((1,3,6,1,4,1,1271,3,4,4,3,1,1),_CwsAlarmActiveAlarmInstanceId_Type())
cwsAlarmActiveAlarmInstanceId.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsAlarmActiveAlarmInstanceId.setStatus(_A)
_CwsAlarmActiveAcknowledged_Type=TruthValue
_CwsAlarmActiveAcknowledged_Object=MibTableColumn
cwsAlarmActiveAcknowledged=_CwsAlarmActiveAcknowledged_Object((1,3,6,1,4,1,1271,3,4,4,3,1,2),_CwsAlarmActiveAcknowledged_Type())
cwsAlarmActiveAcknowledged.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmActiveAcknowledged.setStatus(_A)
_CwsAlarmActiveAlarmTableId_Type=Unsigned32
_CwsAlarmActiveAlarmTableId_Object=MibTableColumn
cwsAlarmActiveAlarmTableId=_CwsAlarmActiveAlarmTableId_Object((1,3,6,1,4,1,1271,3,4,4,3,1,3),_CwsAlarmActiveAlarmTableId_Type())
cwsAlarmActiveAlarmTableId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmActiveAlarmTableId.setStatus(_A)
_CwsAlarmActiveSeverity_Type=AlarmSeverity
_CwsAlarmActiveSeverity_Object=MibTableColumn
cwsAlarmActiveSeverity=_CwsAlarmActiveSeverity_Object((1,3,6,1,4,1,1271,3,4,4,3,1,4),_CwsAlarmActiveSeverity_Type())
cwsAlarmActiveSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmActiveSeverity.setStatus(_A)
_CwsAlarmActiveLocalDateTime_Type=StringMaxl32
_CwsAlarmActiveLocalDateTime_Object=MibTableColumn
cwsAlarmActiveLocalDateTime=_CwsAlarmActiveLocalDateTime_Object((1,3,6,1,4,1,1271,3,4,4,3,1,5),_CwsAlarmActiveLocalDateTime_Type())
cwsAlarmActiveLocalDateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmActiveLocalDateTime.setStatus(_A)
_CwsAlarmActiveInstance_Type=StringMaxl32
_CwsAlarmActiveInstance_Object=MibTableColumn
cwsAlarmActiveInstance=_CwsAlarmActiveInstance_Object((1,3,6,1,4,1,1271,3,4,4,3,1,6),_CwsAlarmActiveInstance_Type())
cwsAlarmActiveInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmActiveInstance.setStatus(_A)
_CwsAlarmActiveDescription_Type=StringMaxl44
_CwsAlarmActiveDescription_Object=MibTableColumn
cwsAlarmActiveDescription=_CwsAlarmActiveDescription_Object((1,3,6,1,4,1,1271,3,4,4,3,1,7),_CwsAlarmActiveDescription_Type())
cwsAlarmActiveDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmActiveDescription.setStatus(_A)
_CwsAlarmActiveSiteIdentifier_Type=Unsigned32
_CwsAlarmActiveSiteIdentifier_Object=MibTableColumn
cwsAlarmActiveSiteIdentifier=_CwsAlarmActiveSiteIdentifier_Object((1,3,6,1,4,1,1271,3,4,4,3,1,8),_CwsAlarmActiveSiteIdentifier_Type())
cwsAlarmActiveSiteIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmActiveSiteIdentifier.setStatus(_A)
_CwsAlarmActiveGroupIdentifier_Type=Unsigned32
_CwsAlarmActiveGroupIdentifier_Object=MibTableColumn
cwsAlarmActiveGroupIdentifier=_CwsAlarmActiveGroupIdentifier_Object((1,3,6,1,4,1,1271,3,4,4,3,1,9),_CwsAlarmActiveGroupIdentifier_Type())
cwsAlarmActiveGroupIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmActiveGroupIdentifier.setStatus(_A)
_CwsAlarmActiveMemberIdentifier_Type=Unsigned32
_CwsAlarmActiveMemberIdentifier_Object=MibTableColumn
cwsAlarmActiveMemberIdentifier=_CwsAlarmActiveMemberIdentifier_Object((1,3,6,1,4,1,1271,3,4,4,3,1,10),_CwsAlarmActiveMemberIdentifier_Type())
cwsAlarmActiveMemberIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmActiveMemberIdentifier.setStatus(_A)
_CwsAlarmHistoryTable_Object=MibTable
cwsAlarmHistoryTable=_CwsAlarmHistoryTable_Object((1,3,6,1,4,1,1271,3,4,4,4))
if mibBuilder.loadTexts:cwsAlarmHistoryTable.setStatus(_A)
_CwsAlarmHistoryEntry_Object=MibTableRow
cwsAlarmHistoryEntry=_CwsAlarmHistoryEntry_Object((1,3,6,1,4,1,1271,3,4,4,4,1))
cwsAlarmHistoryEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:cwsAlarmHistoryEntry.setStatus(_A)
class _CwsAlarmHistoryHistoryId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsAlarmHistoryHistoryId_Type.__name__=_D
_CwsAlarmHistoryHistoryId_Object=MibTableColumn
cwsAlarmHistoryHistoryId=_CwsAlarmHistoryHistoryId_Object((1,3,6,1,4,1,1271,3,4,4,4,1,1),_CwsAlarmHistoryHistoryId_Type())
cwsAlarmHistoryHistoryId.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsAlarmHistoryHistoryId.setStatus(_A)
_CwsAlarmHistoryReason_Type=AlarmReason
_CwsAlarmHistoryReason_Object=MibTableColumn
cwsAlarmHistoryReason=_CwsAlarmHistoryReason_Object((1,3,6,1,4,1,1271,3,4,4,4,1,2),_CwsAlarmHistoryReason_Type())
cwsAlarmHistoryReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmHistoryReason.setStatus(_A)
_CwsAlarmHistoryAlarmInstanceId_Type=Unsigned32
_CwsAlarmHistoryAlarmInstanceId_Object=MibTableColumn
cwsAlarmHistoryAlarmInstanceId=_CwsAlarmHistoryAlarmInstanceId_Object((1,3,6,1,4,1,1271,3,4,4,4,1,3),_CwsAlarmHistoryAlarmInstanceId_Type())
cwsAlarmHistoryAlarmInstanceId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmHistoryAlarmInstanceId.setStatus(_A)
_CwsAlarmHistoryAlarmTableId_Type=Unsigned32
_CwsAlarmHistoryAlarmTableId_Object=MibTableColumn
cwsAlarmHistoryAlarmTableId=_CwsAlarmHistoryAlarmTableId_Object((1,3,6,1,4,1,1271,3,4,4,4,1,4),_CwsAlarmHistoryAlarmTableId_Type())
cwsAlarmHistoryAlarmTableId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmHistoryAlarmTableId.setStatus(_A)
_CwsAlarmHistorySeverity_Type=AlarmSeverity
_CwsAlarmHistorySeverity_Object=MibTableColumn
cwsAlarmHistorySeverity=_CwsAlarmHistorySeverity_Object((1,3,6,1,4,1,1271,3,4,4,4,1,5),_CwsAlarmHistorySeverity_Type())
cwsAlarmHistorySeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmHistorySeverity.setStatus(_A)
_CwsAlarmHistoryLocalDateTime_Type=StringMaxl32
_CwsAlarmHistoryLocalDateTime_Object=MibTableColumn
cwsAlarmHistoryLocalDateTime=_CwsAlarmHistoryLocalDateTime_Object((1,3,6,1,4,1,1271,3,4,4,4,1,6),_CwsAlarmHistoryLocalDateTime_Type())
cwsAlarmHistoryLocalDateTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmHistoryLocalDateTime.setStatus(_A)
_CwsAlarmHistoryInstance_Type=StringMaxl32
_CwsAlarmHistoryInstance_Object=MibTableColumn
cwsAlarmHistoryInstance=_CwsAlarmHistoryInstance_Object((1,3,6,1,4,1,1271,3,4,4,4,1,7),_CwsAlarmHistoryInstance_Type())
cwsAlarmHistoryInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmHistoryInstance.setStatus(_A)
_CwsAlarmHistoryDescription_Type=StringMaxl44
_CwsAlarmHistoryDescription_Object=MibTableColumn
cwsAlarmHistoryDescription=_CwsAlarmHistoryDescription_Object((1,3,6,1,4,1,1271,3,4,4,4,1,8),_CwsAlarmHistoryDescription_Type())
cwsAlarmHistoryDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmHistoryDescription.setStatus(_A)
_CwsAlarmHistorySiteIdentifier_Type=Unsigned32
_CwsAlarmHistorySiteIdentifier_Object=MibTableColumn
cwsAlarmHistorySiteIdentifier=_CwsAlarmHistorySiteIdentifier_Object((1,3,6,1,4,1,1271,3,4,4,4,1,9),_CwsAlarmHistorySiteIdentifier_Type())
cwsAlarmHistorySiteIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmHistorySiteIdentifier.setStatus(_A)
_CwsAlarmHistoryGroupIdentifier_Type=Unsigned32
_CwsAlarmHistoryGroupIdentifier_Object=MibTableColumn
cwsAlarmHistoryGroupIdentifier=_CwsAlarmHistoryGroupIdentifier_Object((1,3,6,1,4,1,1271,3,4,4,4,1,10),_CwsAlarmHistoryGroupIdentifier_Type())
cwsAlarmHistoryGroupIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmHistoryGroupIdentifier.setStatus(_A)
_CwsAlarmHistoryMemberIdentifier_Type=Unsigned32
_CwsAlarmHistoryMemberIdentifier_Object=MibTableColumn
cwsAlarmHistoryMemberIdentifier=_CwsAlarmHistoryMemberIdentifier_Object((1,3,6,1,4,1,1271,3,4,4,4,1,11),_CwsAlarmHistoryMemberIdentifier_Type())
cwsAlarmHistoryMemberIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmHistoryMemberIdentifier.setStatus(_A)
_CwsAlarmDefinedTable_Object=MibTable
cwsAlarmDefinedTable=_CwsAlarmDefinedTable_Object((1,3,6,1,4,1,1271,3,4,4,5))
if mibBuilder.loadTexts:cwsAlarmDefinedTable.setStatus(_A)
_CwsAlarmDefinedEntry_Object=MibTableRow
cwsAlarmDefinedEntry=_CwsAlarmDefinedEntry_Object((1,3,6,1,4,1,1271,3,4,4,5,1))
cwsAlarmDefinedEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cwsAlarmDefinedEntry.setStatus(_A)
class _CwsAlarmDefinedAlarmTableId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsAlarmDefinedAlarmTableId_Type.__name__=_D
_CwsAlarmDefinedAlarmTableId_Object=MibTableColumn
cwsAlarmDefinedAlarmTableId=_CwsAlarmDefinedAlarmTableId_Object((1,3,6,1,4,1,1271,3,4,4,5,1,1),_CwsAlarmDefinedAlarmTableId_Type())
cwsAlarmDefinedAlarmTableId.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsAlarmDefinedAlarmTableId.setStatus(_A)
_CwsAlarmDefinedEnabled_Type=TruthValue
_CwsAlarmDefinedEnabled_Object=MibTableColumn
cwsAlarmDefinedEnabled=_CwsAlarmDefinedEnabled_Object((1,3,6,1,4,1,1271,3,4,4,5,1,2),_CwsAlarmDefinedEnabled_Type())
cwsAlarmDefinedEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmDefinedEnabled.setStatus(_A)
_CwsAlarmDefinedActive_Type=TruthValue
_CwsAlarmDefinedActive_Object=MibTableColumn
cwsAlarmDefinedActive=_CwsAlarmDefinedActive_Object((1,3,6,1,4,1,1271,3,4,4,5,1,3),_CwsAlarmDefinedActive_Type())
cwsAlarmDefinedActive.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmDefinedActive.setStatus(_A)
_CwsAlarmDefinedThreshold_Type=Unsigned32
_CwsAlarmDefinedThreshold_Object=MibTableColumn
cwsAlarmDefinedThreshold=_CwsAlarmDefinedThreshold_Object((1,3,6,1,4,1,1271,3,4,4,5,1,4),_CwsAlarmDefinedThreshold_Type())
cwsAlarmDefinedThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmDefinedThreshold.setStatus(_A)
_CwsAlarmDefinedCap_Type=Unsigned32
_CwsAlarmDefinedCap_Object=MibTableColumn
cwsAlarmDefinedCap=_CwsAlarmDefinedCap_Object((1,3,6,1,4,1,1271,3,4,4,5,1,5),_CwsAlarmDefinedCap_Type())
cwsAlarmDefinedCap.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmDefinedCap.setStatus(_A)
_CwsAlarmDefinedSeverity_Type=AlarmSeverity
_CwsAlarmDefinedSeverity_Object=MibTableColumn
cwsAlarmDefinedSeverity=_CwsAlarmDefinedSeverity_Object((1,3,6,1,4,1,1271,3,4,4,5,1,6),_CwsAlarmDefinedSeverity_Type())
cwsAlarmDefinedSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmDefinedSeverity.setStatus(_A)
_CwsAlarmDefinedInstance_Type=StringMaxl16
_CwsAlarmDefinedInstance_Object=MibTableColumn
cwsAlarmDefinedInstance=_CwsAlarmDefinedInstance_Object((1,3,6,1,4,1,1271,3,4,4,5,1,7),_CwsAlarmDefinedInstance_Type())
cwsAlarmDefinedInstance.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmDefinedInstance.setStatus(_A)
_CwsAlarmDefinedDescription_Type=StringMaxl44
_CwsAlarmDefinedDescription_Object=MibTableColumn
cwsAlarmDefinedDescription=_CwsAlarmDefinedDescription_Object((1,3,6,1,4,1,1271,3,4,4,5,1,8),_CwsAlarmDefinedDescription_Type())
cwsAlarmDefinedDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmDefinedDescription.setStatus(_A)
_CwsAlarmStatisticsTable_Object=MibTable
cwsAlarmStatisticsTable=_CwsAlarmStatisticsTable_Object((1,3,6,1,4,1,1271,3,4,4,6))
if mibBuilder.loadTexts:cwsAlarmStatisticsTable.setStatus(_A)
_CwsAlarmStatisticsEntry_Object=MibTableRow
cwsAlarmStatisticsEntry=_CwsAlarmStatisticsEntry_Object((1,3,6,1,4,1,1271,3,4,4,6,1))
cwsAlarmStatisticsEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:cwsAlarmStatisticsEntry.setStatus(_A)
class _CwsAlarmStatisticsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CwsAlarmStatisticsIndex_Type.__name__=_D
_CwsAlarmStatisticsIndex_Object=MibTableColumn
cwsAlarmStatisticsIndex=_CwsAlarmStatisticsIndex_Object((1,3,6,1,4,1,1271,3,4,4,6,1,1),_CwsAlarmStatisticsIndex_Type())
cwsAlarmStatisticsIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cwsAlarmStatisticsIndex.setStatus(_A)
_CwsAlarmStatisticsActive_Type=TruthValue
_CwsAlarmStatisticsActive_Object=MibTableColumn
cwsAlarmStatisticsActive=_CwsAlarmStatisticsActive_Object((1,3,6,1,4,1,1271,3,4,4,6,1,2),_CwsAlarmStatisticsActive_Type())
cwsAlarmStatisticsActive.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmStatisticsActive.setStatus(_A)
_CwsAlarmStatisticsDisabled_Type=TruthValue
_CwsAlarmStatisticsDisabled_Object=MibTableColumn
cwsAlarmStatisticsDisabled=_CwsAlarmStatisticsDisabled_Object((1,3,6,1,4,1,1271,3,4,4,6,1,3),_CwsAlarmStatisticsDisabled_Type())
cwsAlarmStatisticsDisabled.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmStatisticsDisabled.setStatus(_A)
_CwsAlarmStatisticsCount_Type=Unsigned32
_CwsAlarmStatisticsCount_Object=MibTableColumn
cwsAlarmStatisticsCount=_CwsAlarmStatisticsCount_Object((1,3,6,1,4,1,1271,3,4,4,6,1,4),_CwsAlarmStatisticsCount_Type())
cwsAlarmStatisticsCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmStatisticsCount.setStatus(_A)
_CwsAlarmStatisticsCumulative_Type=Unsigned32
_CwsAlarmStatisticsCumulative_Object=MibTableColumn
cwsAlarmStatisticsCumulative=_CwsAlarmStatisticsCumulative_Object((1,3,6,1,4,1,1271,3,4,4,6,1,5),_CwsAlarmStatisticsCumulative_Type())
cwsAlarmStatisticsCumulative.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmStatisticsCumulative.setStatus(_A)
_CwsAlarmStatisticsType_Type=StringMaxl32
_CwsAlarmStatisticsType_Object=MibTableColumn
cwsAlarmStatisticsType=_CwsAlarmStatisticsType_Object((1,3,6,1,4,1,1271,3,4,4,6,1,6),_CwsAlarmStatisticsType_Type())
cwsAlarmStatisticsType.setMaxAccess(_C)
if mibBuilder.loadTexts:cwsAlarmStatisticsType.setStatus(_A)
cienaWsAlarmGroup=ObjectGroup((1,3,6,1,4,1,1271,3,4,4,2,1,1))
cienaWsAlarmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:cienaWsAlarmGroup.setStatus(_A)
cienaWsAlarmCompliance=ModuleCompliance((1,3,6,1,4,1,1271,3,4,4,2,2,1))
cienaWsAlarmCompliance.setObjects((_B,_o))
if mibBuilder.loadTexts:cienaWsAlarmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AlarmReason':AlarmReason,'AlarmSeverity':AlarmSeverity,'cienaWsAlarmMIB':cienaWsAlarmMIB,'cienaWsAlarmObjects':cienaWsAlarmObjects,'cienaWsAlarmConformance':cienaWsAlarmConformance,'cienaWsAlarmGroups':cienaWsAlarmGroups,_o:cienaWsAlarmGroup,'cienaWsAlarmCompliances':cienaWsAlarmCompliances,'cienaWsAlarmCompliance':cienaWsAlarmCompliance,'cwsAlarmActiveTable':cwsAlarmActiveTable,'cwsAlarmActiveEntry':cwsAlarmActiveEntry,_F:cwsAlarmActiveAlarmInstanceId,_J:cwsAlarmActiveAcknowledged,_K:cwsAlarmActiveAlarmTableId,_L:cwsAlarmActiveSeverity,_M:cwsAlarmActiveLocalDateTime,_N:cwsAlarmActiveInstance,_O:cwsAlarmActiveDescription,_P:cwsAlarmActiveSiteIdentifier,_Q:cwsAlarmActiveGroupIdentifier,_R:cwsAlarmActiveMemberIdentifier,'cwsAlarmHistoryTable':cwsAlarmHistoryTable,'cwsAlarmHistoryEntry':cwsAlarmHistoryEntry,_G:cwsAlarmHistoryHistoryId,_S:cwsAlarmHistoryReason,_T:cwsAlarmHistoryAlarmInstanceId,_U:cwsAlarmHistoryAlarmTableId,_V:cwsAlarmHistorySeverity,_W:cwsAlarmHistoryLocalDateTime,_X:cwsAlarmHistoryInstance,_Y:cwsAlarmHistoryDescription,_Z:cwsAlarmHistorySiteIdentifier,_a:cwsAlarmHistoryGroupIdentifier,_b:cwsAlarmHistoryMemberIdentifier,'cwsAlarmDefinedTable':cwsAlarmDefinedTable,'cwsAlarmDefinedEntry':cwsAlarmDefinedEntry,_H:cwsAlarmDefinedAlarmTableId,_c:cwsAlarmDefinedEnabled,_d:cwsAlarmDefinedActive,_e:cwsAlarmDefinedThreshold,_f:cwsAlarmDefinedCap,_g:cwsAlarmDefinedSeverity,_h:cwsAlarmDefinedInstance,_i:cwsAlarmDefinedDescription,'cwsAlarmStatisticsTable':cwsAlarmStatisticsTable,'cwsAlarmStatisticsEntry':cwsAlarmStatisticsEntry,_I:cwsAlarmStatisticsIndex,_j:cwsAlarmStatisticsActive,_k:cwsAlarmStatisticsDisabled,_l:cwsAlarmStatisticsCount,_m:cwsAlarmStatisticsCumulative,_n:cwsAlarmStatisticsType})