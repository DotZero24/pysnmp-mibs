_f='ituAlarmStatisticsGroup'
_e='ituAlarmSecurityGroup'
_d='ituAlarmServiceUserGroup'
_c='ituAlarmGroup'
_b='ituAlarmActiveStatsWarnings'
_a='ituAlarmActiveStatsMinors'
_Z='ituAlarmActiveStatsMajors'
_Y='ituAlarmActiveStatsCriticals'
_X='ituAlarmActiveStatsIndeterminates'
_W='ituAlarmActiveStatsWarningCurrent'
_V='ituAlarmActiveStatsMinorCurrent'
_U='ituAlarmActiveStatsMajorCurrent'
_T='ituAlarmActiveStatsCriticalCurrent'
_S='ituAlarmActiveStatsIndeterminateCurrent'
_R='ituAlarmActiveServiceUser'
_Q='ituAlarmActiveServiceProvider'
_P='ituAlarmActiveDetector'
_O='ituAlarmActiveTrendIndication'
_N='ituAlarmAdditionalText'
_M='ituAlarmGenericModel'
_L='ituAlarmProbableCause'
_K='ituAlarmEventType'
_J='ituAlarmPerceivedSeverity'
_I='alarmModelIndex'
_H='alarmActiveIndex'
_G='alarmActiveDateAndTime'
_F='read-write'
_E='alarmListName'
_D='ALARM-MIB'
_C='read-only'
_B='ITU-ALARM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
alarmActiveDateAndTime,alarmActiveIndex,alarmListName,alarmModelIndex=mibBuilder.importSymbols(_D,_G,_H,_E,_I)
IANAItuEventType,IANAItuProbableCause=mibBuilder.importSymbols('IANA-ITU-ALARM-TC-MIB','IANAItuEventType','IANAItuProbableCause')
ItuPerceivedSeverity,ItuTrendIndication=mibBuilder.importSymbols('ITU-ALARM-TC-MIB','ItuPerceivedSeverity','ItuTrendIndication')
ZeroBasedCounter32,=mibBuilder.importSymbols('RMON2-MIB','ZeroBasedCounter32')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
AutonomousType,DisplayString,PhysAddress,RowPointer,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','RowPointer','TextualConvention')
ituAlarmMIB=ModuleIdentity((1,3,6,1,2,1,121))
if mibBuilder.loadTexts:ituAlarmMIB.setRevisions(('2004-09-09 00:00',))
_ItuAlarmObjects_ObjectIdentity=ObjectIdentity
ituAlarmObjects=_ItuAlarmObjects_ObjectIdentity((1,3,6,1,2,1,121,1))
_ItuAlarmModel_ObjectIdentity=ObjectIdentity
ituAlarmModel=_ItuAlarmModel_ObjectIdentity((1,3,6,1,2,1,121,1,1))
_ItuAlarmTable_Object=MibTable
ituAlarmTable=_ItuAlarmTable_Object((1,3,6,1,2,1,121,1,1,1))
if mibBuilder.loadTexts:ituAlarmTable.setStatus(_A)
_ItuAlarmEntry_Object=MibTableRow
ituAlarmEntry=_ItuAlarmEntry_Object((1,3,6,1,2,1,121,1,1,1,1))
ituAlarmEntry.setIndexNames((0,_D,_E),(0,_D,_I),(0,_B,_J))
if mibBuilder.loadTexts:ituAlarmEntry.setStatus(_A)
_ItuAlarmPerceivedSeverity_Type=ItuPerceivedSeverity
_ItuAlarmPerceivedSeverity_Object=MibTableColumn
ituAlarmPerceivedSeverity=_ItuAlarmPerceivedSeverity_Object((1,3,6,1,2,1,121,1,1,1,1,1),_ItuAlarmPerceivedSeverity_Type())
ituAlarmPerceivedSeverity.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:ituAlarmPerceivedSeverity.setStatus(_A)
_ItuAlarmEventType_Type=IANAItuEventType
_ItuAlarmEventType_Object=MibTableColumn
ituAlarmEventType=_ItuAlarmEventType_Object((1,3,6,1,2,1,121,1,1,1,1,2),_ItuAlarmEventType_Type())
ituAlarmEventType.setMaxAccess(_F)
if mibBuilder.loadTexts:ituAlarmEventType.setStatus(_A)
_ItuAlarmProbableCause_Type=IANAItuProbableCause
_ItuAlarmProbableCause_Object=MibTableColumn
ituAlarmProbableCause=_ItuAlarmProbableCause_Object((1,3,6,1,2,1,121,1,1,1,1,3),_ItuAlarmProbableCause_Type())
ituAlarmProbableCause.setMaxAccess(_F)
if mibBuilder.loadTexts:ituAlarmProbableCause.setStatus(_A)
_ItuAlarmAdditionalText_Type=SnmpAdminString
_ItuAlarmAdditionalText_Object=MibTableColumn
ituAlarmAdditionalText=_ItuAlarmAdditionalText_Object((1,3,6,1,2,1,121,1,1,1,1,4),_ItuAlarmAdditionalText_Type())
ituAlarmAdditionalText.setMaxAccess(_F)
if mibBuilder.loadTexts:ituAlarmAdditionalText.setStatus(_A)
_ItuAlarmGenericModel_Type=RowPointer
_ItuAlarmGenericModel_Object=MibTableColumn
ituAlarmGenericModel=_ItuAlarmGenericModel_Object((1,3,6,1,2,1,121,1,1,1,1,5),_ItuAlarmGenericModel_Type())
ituAlarmGenericModel.setMaxAccess(_F)
if mibBuilder.loadTexts:ituAlarmGenericModel.setStatus(_A)
_ItuAlarmActive_ObjectIdentity=ObjectIdentity
ituAlarmActive=_ItuAlarmActive_ObjectIdentity((1,3,6,1,2,1,121,1,2))
_ItuAlarmActiveTable_Object=MibTable
ituAlarmActiveTable=_ItuAlarmActiveTable_Object((1,3,6,1,2,1,121,1,2,1))
if mibBuilder.loadTexts:ituAlarmActiveTable.setStatus(_A)
_ItuAlarmActiveEntry_Object=MibTableRow
ituAlarmActiveEntry=_ItuAlarmActiveEntry_Object((1,3,6,1,2,1,121,1,2,1,1))
ituAlarmActiveEntry.setIndexNames((0,_D,_E),(0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:ituAlarmActiveEntry.setStatus(_A)
_ItuAlarmActiveTrendIndication_Type=ItuTrendIndication
_ItuAlarmActiveTrendIndication_Object=MibTableColumn
ituAlarmActiveTrendIndication=_ItuAlarmActiveTrendIndication_Object((1,3,6,1,2,1,121,1,2,1,1,1),_ItuAlarmActiveTrendIndication_Type())
ituAlarmActiveTrendIndication.setMaxAccess(_C)
if mibBuilder.loadTexts:ituAlarmActiveTrendIndication.setStatus(_A)
_ItuAlarmActiveDetector_Type=AutonomousType
_ItuAlarmActiveDetector_Object=MibTableColumn
ituAlarmActiveDetector=_ItuAlarmActiveDetector_Object((1,3,6,1,2,1,121,1,2,1,1,2),_ItuAlarmActiveDetector_Type())
ituAlarmActiveDetector.setMaxAccess(_C)
if mibBuilder.loadTexts:ituAlarmActiveDetector.setStatus(_A)
_ItuAlarmActiveServiceProvider_Type=AutonomousType
_ItuAlarmActiveServiceProvider_Object=MibTableColumn
ituAlarmActiveServiceProvider=_ItuAlarmActiveServiceProvider_Object((1,3,6,1,2,1,121,1,2,1,1,3),_ItuAlarmActiveServiceProvider_Type())
ituAlarmActiveServiceProvider.setMaxAccess(_C)
if mibBuilder.loadTexts:ituAlarmActiveServiceProvider.setStatus(_A)
_ItuAlarmActiveServiceUser_Type=AutonomousType
_ItuAlarmActiveServiceUser_Object=MibTableColumn
ituAlarmActiveServiceUser=_ItuAlarmActiveServiceUser_Object((1,3,6,1,2,1,121,1,2,1,1,4),_ItuAlarmActiveServiceUser_Type())
ituAlarmActiveServiceUser.setMaxAccess(_C)
if mibBuilder.loadTexts:ituAlarmActiveServiceUser.setStatus(_A)
_ItuAlarmActiveStatsTable_Object=MibTable
ituAlarmActiveStatsTable=_ItuAlarmActiveStatsTable_Object((1,3,6,1,2,1,121,1,2,2))
if mibBuilder.loadTexts:ituAlarmActiveStatsTable.setStatus(_A)
_ItuAlarmActiveStatsEntry_Object=MibTableRow
ituAlarmActiveStatsEntry=_ItuAlarmActiveStatsEntry_Object((1,3,6,1,2,1,121,1,2,2,1))
ituAlarmActiveStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ituAlarmActiveStatsEntry.setStatus(_A)
_ItuAlarmActiveStatsIndeterminateCurrent_Type=Gauge32
_ItuAlarmActiveStatsIndeterminateCurrent_Object=MibTableColumn
ituAlarmActiveStatsIndeterminateCurrent=_ItuAlarmActiveStatsIndeterminateCurrent_Object((1,3,6,1,2,1,121,1,2,2,1,1),_ItuAlarmActiveStatsIndeterminateCurrent_Type())
ituAlarmActiveStatsIndeterminateCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:ituAlarmActiveStatsIndeterminateCurrent.setStatus(_A)
_ItuAlarmActiveStatsCriticalCurrent_Type=Gauge32
_ItuAlarmActiveStatsCriticalCurrent_Object=MibTableColumn
ituAlarmActiveStatsCriticalCurrent=_ItuAlarmActiveStatsCriticalCurrent_Object((1,3,6,1,2,1,121,1,2,2,1,2),_ItuAlarmActiveStatsCriticalCurrent_Type())
ituAlarmActiveStatsCriticalCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:ituAlarmActiveStatsCriticalCurrent.setStatus(_A)
_ItuAlarmActiveStatsMajorCurrent_Type=Gauge32
_ItuAlarmActiveStatsMajorCurrent_Object=MibTableColumn
ituAlarmActiveStatsMajorCurrent=_ItuAlarmActiveStatsMajorCurrent_Object((1,3,6,1,2,1,121,1,2,2,1,3),_ItuAlarmActiveStatsMajorCurrent_Type())
ituAlarmActiveStatsMajorCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:ituAlarmActiveStatsMajorCurrent.setStatus(_A)
_ItuAlarmActiveStatsMinorCurrent_Type=Gauge32
_ItuAlarmActiveStatsMinorCurrent_Object=MibTableColumn
ituAlarmActiveStatsMinorCurrent=_ItuAlarmActiveStatsMinorCurrent_Object((1,3,6,1,2,1,121,1,2,2,1,4),_ItuAlarmActiveStatsMinorCurrent_Type())
ituAlarmActiveStatsMinorCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:ituAlarmActiveStatsMinorCurrent.setStatus(_A)
_ItuAlarmActiveStatsWarningCurrent_Type=Gauge32
_ItuAlarmActiveStatsWarningCurrent_Object=MibTableColumn
ituAlarmActiveStatsWarningCurrent=_ItuAlarmActiveStatsWarningCurrent_Object((1,3,6,1,2,1,121,1,2,2,1,5),_ItuAlarmActiveStatsWarningCurrent_Type())
ituAlarmActiveStatsWarningCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:ituAlarmActiveStatsWarningCurrent.setStatus(_A)
_ItuAlarmActiveStatsIndeterminates_Type=ZeroBasedCounter32
_ItuAlarmActiveStatsIndeterminates_Object=MibTableColumn
ituAlarmActiveStatsIndeterminates=_ItuAlarmActiveStatsIndeterminates_Object((1,3,6,1,2,1,121,1,2,2,1,6),_ItuAlarmActiveStatsIndeterminates_Type())
ituAlarmActiveStatsIndeterminates.setMaxAccess(_C)
if mibBuilder.loadTexts:ituAlarmActiveStatsIndeterminates.setStatus(_A)
_ItuAlarmActiveStatsCriticals_Type=ZeroBasedCounter32
_ItuAlarmActiveStatsCriticals_Object=MibTableColumn
ituAlarmActiveStatsCriticals=_ItuAlarmActiveStatsCriticals_Object((1,3,6,1,2,1,121,1,2,2,1,7),_ItuAlarmActiveStatsCriticals_Type())
ituAlarmActiveStatsCriticals.setMaxAccess(_C)
if mibBuilder.loadTexts:ituAlarmActiveStatsCriticals.setStatus(_A)
_ItuAlarmActiveStatsMajors_Type=ZeroBasedCounter32
_ItuAlarmActiveStatsMajors_Object=MibTableColumn
ituAlarmActiveStatsMajors=_ItuAlarmActiveStatsMajors_Object((1,3,6,1,2,1,121,1,2,2,1,8),_ItuAlarmActiveStatsMajors_Type())
ituAlarmActiveStatsMajors.setMaxAccess(_C)
if mibBuilder.loadTexts:ituAlarmActiveStatsMajors.setStatus(_A)
_ItuAlarmActiveStatsMinors_Type=ZeroBasedCounter32
_ItuAlarmActiveStatsMinors_Object=MibTableColumn
ituAlarmActiveStatsMinors=_ItuAlarmActiveStatsMinors_Object((1,3,6,1,2,1,121,1,2,2,1,9),_ItuAlarmActiveStatsMinors_Type())
ituAlarmActiveStatsMinors.setMaxAccess(_C)
if mibBuilder.loadTexts:ituAlarmActiveStatsMinors.setStatus(_A)
_ItuAlarmActiveStatsWarnings_Type=ZeroBasedCounter32
_ItuAlarmActiveStatsWarnings_Object=MibTableColumn
ituAlarmActiveStatsWarnings=_ItuAlarmActiveStatsWarnings_Object((1,3,6,1,2,1,121,1,2,2,1,10),_ItuAlarmActiveStatsWarnings_Type())
ituAlarmActiveStatsWarnings.setMaxAccess(_C)
if mibBuilder.loadTexts:ituAlarmActiveStatsWarnings.setStatus(_A)
_ItuAlarmConformance_ObjectIdentity=ObjectIdentity
ituAlarmConformance=_ItuAlarmConformance_ObjectIdentity((1,3,6,1,2,1,121,2))
_ItuAlarmCompliances_ObjectIdentity=ObjectIdentity
ituAlarmCompliances=_ItuAlarmCompliances_ObjectIdentity((1,3,6,1,2,1,121,2,1))
_ItuAlarmGroups_ObjectIdentity=ObjectIdentity
ituAlarmGroups=_ItuAlarmGroups_ObjectIdentity((1,3,6,1,2,1,121,2,2))
ituAlarmGroup=ObjectGroup((1,3,6,1,2,1,121,2,2,1))
ituAlarmGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:ituAlarmGroup.setStatus(_A)
ituAlarmServiceUserGroup=ObjectGroup((1,3,6,1,2,1,121,2,2,2))
ituAlarmServiceUserGroup.setObjects(*((_B,_N),(_B,_O)))
if mibBuilder.loadTexts:ituAlarmServiceUserGroup.setStatus(_A)
ituAlarmSecurityGroup=ObjectGroup((1,3,6,1,2,1,121,2,2,3))
ituAlarmSecurityGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ituAlarmSecurityGroup.setStatus(_A)
ituAlarmStatisticsGroup=ObjectGroup((1,3,6,1,2,1,121,2,2,4))
ituAlarmStatisticsGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:ituAlarmStatisticsGroup.setStatus(_A)
ituAlarmCompliance=ModuleCompliance((1,3,6,1,2,1,121,2,1,1))
ituAlarmCompliance.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:ituAlarmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ituAlarmMIB':ituAlarmMIB,'ituAlarmObjects':ituAlarmObjects,'ituAlarmModel':ituAlarmModel,'ituAlarmTable':ituAlarmTable,'ituAlarmEntry':ituAlarmEntry,_J:ituAlarmPerceivedSeverity,_K:ituAlarmEventType,_L:ituAlarmProbableCause,_N:ituAlarmAdditionalText,_M:ituAlarmGenericModel,'ituAlarmActive':ituAlarmActive,'ituAlarmActiveTable':ituAlarmActiveTable,'ituAlarmActiveEntry':ituAlarmActiveEntry,_O:ituAlarmActiveTrendIndication,_P:ituAlarmActiveDetector,_Q:ituAlarmActiveServiceProvider,_R:ituAlarmActiveServiceUser,'ituAlarmActiveStatsTable':ituAlarmActiveStatsTable,'ituAlarmActiveStatsEntry':ituAlarmActiveStatsEntry,_S:ituAlarmActiveStatsIndeterminateCurrent,_T:ituAlarmActiveStatsCriticalCurrent,_U:ituAlarmActiveStatsMajorCurrent,_V:ituAlarmActiveStatsMinorCurrent,_W:ituAlarmActiveStatsWarningCurrent,_X:ituAlarmActiveStatsIndeterminates,_Y:ituAlarmActiveStatsCriticals,_Z:ituAlarmActiveStatsMajors,_a:ituAlarmActiveStatsMinors,_b:ituAlarmActiveStatsWarnings,'ituAlarmConformance':ituAlarmConformance,'ituAlarmCompliances':ituAlarmCompliances,'ituAlarmCompliance':ituAlarmCompliance,'ituAlarmGroups':ituAlarmGroups,_c:ituAlarmGroup,_d:ituAlarmServiceUserGroup,_e:ituAlarmSecurityGroup,_f:ituAlarmStatisticsGroup})