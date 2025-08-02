_O='ntcPAMConfGrpV1Standard'
_N='ntcPAMAlNotActive'
_M='ntcPAMAlarmStatsNotActive'
_L='ntcPAMConfigPid'
_K='ntcPAMConfigEnable'
_J='ntcPAMConfigRowStatus'
_I='read-only'
_H='ntcPAMAlarmStatsName'
_G='not-accessible'
_F='ntcPAMConfigName'
_E='Unsigned32'
_D='read-create'
_C='DisplayString'
_B='NEWTEC-PIDACTMON-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcAlarmState,NtcEnable=mibBuilder.importSymbols('NEWTEC-TC-MIB','NtcAlarmState','NtcEnable')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','RowStatus','TextualConvention')
ntcPidActivityMonitor=ModuleIdentity((1,3,6,1,4,1,5835,5,2,9200))
if mibBuilder.loadTexts:ntcPidActivityMonitor.setRevisions(('2015-10-19 11:00',))
_NtcPAMObjects_ObjectIdentity=ObjectIdentity
ntcPAMObjects=_NtcPAMObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9200,1))
if mibBuilder.loadTexts:ntcPAMObjects.setStatus(_A)
_NtcPAMConfiguration_ObjectIdentity=ObjectIdentity
ntcPAMConfiguration=_NtcPAMConfiguration_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9200,1,1))
if mibBuilder.loadTexts:ntcPAMConfiguration.setStatus(_A)
_NtcPAMConfigTable_Object=MibTable
ntcPAMConfigTable=_NtcPAMConfigTable_Object((1,3,6,1,4,1,5835,5,2,9200,1,1,1))
if mibBuilder.loadTexts:ntcPAMConfigTable.setStatus(_A)
_NtcPAMConfigEntry_Object=MibTableRow
ntcPAMConfigEntry=_NtcPAMConfigEntry_Object((1,3,6,1,4,1,5835,5,2,9200,1,1,1,1))
ntcPAMConfigEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:ntcPAMConfigEntry.setStatus(_A)
class _NtcPAMConfigName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_NtcPAMConfigName_Type.__name__=_C
_NtcPAMConfigName_Object=MibTableColumn
ntcPAMConfigName=_NtcPAMConfigName_Object((1,3,6,1,4,1,5835,5,2,9200,1,1,1,1,1),_NtcPAMConfigName_Type())
ntcPAMConfigName.setMaxAccess(_G)
if mibBuilder.loadTexts:ntcPAMConfigName.setStatus(_A)
_NtcPAMConfigRowStatus_Type=RowStatus
_NtcPAMConfigRowStatus_Object=MibTableColumn
ntcPAMConfigRowStatus=_NtcPAMConfigRowStatus_Object((1,3,6,1,4,1,5835,5,2,9200,1,1,1,1,2),_NtcPAMConfigRowStatus_Type())
ntcPAMConfigRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcPAMConfigRowStatus.setStatus(_A)
_NtcPAMConfigEnable_Type=NtcEnable
_NtcPAMConfigEnable_Object=MibTableColumn
ntcPAMConfigEnable=_NtcPAMConfigEnable_Object((1,3,6,1,4,1,5835,5,2,9200,1,1,1,1,3),_NtcPAMConfigEnable_Type())
ntcPAMConfigEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcPAMConfigEnable.setStatus(_A)
class _NtcPAMConfigPid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8190))
_NtcPAMConfigPid_Type.__name__=_E
_NtcPAMConfigPid_Object=MibTableColumn
ntcPAMConfigPid=_NtcPAMConfigPid_Object((1,3,6,1,4,1,5835,5,2,9200,1,1,1,1,4),_NtcPAMConfigPid_Type())
ntcPAMConfigPid.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcPAMConfigPid.setStatus(_A)
_NtcPAMAlarms_ObjectIdentity=ObjectIdentity
ntcPAMAlarms=_NtcPAMAlarms_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9200,1,2))
if mibBuilder.loadTexts:ntcPAMAlarms.setStatus(_A)
_NtcPAMAlarmStatsTable_Object=MibTable
ntcPAMAlarmStatsTable=_NtcPAMAlarmStatsTable_Object((1,3,6,1,4,1,5835,5,2,9200,1,2,1))
if mibBuilder.loadTexts:ntcPAMAlarmStatsTable.setStatus(_A)
_NtcPAMAlarmStatsEntry_Object=MibTableRow
ntcPAMAlarmStatsEntry=_NtcPAMAlarmStatsEntry_Object((1,3,6,1,4,1,5835,5,2,9200,1,2,1,1))
ntcPAMAlarmStatsEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:ntcPAMAlarmStatsEntry.setStatus(_A)
class _NtcPAMAlarmStatsName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_NtcPAMAlarmStatsName_Type.__name__=_C
_NtcPAMAlarmStatsName_Object=MibTableColumn
ntcPAMAlarmStatsName=_NtcPAMAlarmStatsName_Object((1,3,6,1,4,1,5835,5,2,9200,1,2,1,1,1),_NtcPAMAlarmStatsName_Type())
ntcPAMAlarmStatsName.setMaxAccess(_G)
if mibBuilder.loadTexts:ntcPAMAlarmStatsName.setStatus(_A)
_NtcPAMAlarmStatsNotActive_Type=NtcAlarmState
_NtcPAMAlarmStatsNotActive_Object=MibTableColumn
ntcPAMAlarmStatsNotActive=_NtcPAMAlarmStatsNotActive_Object((1,3,6,1,4,1,5835,5,2,9200,1,2,1,1,2),_NtcPAMAlarmStatsNotActive_Type())
ntcPAMAlarmStatsNotActive.setMaxAccess(_I)
if mibBuilder.loadTexts:ntcPAMAlarmStatsNotActive.setStatus(_A)
_NtcPAMAlNotActive_Type=NtcAlarmState
_NtcPAMAlNotActive_Object=MibScalar
ntcPAMAlNotActive=_NtcPAMAlNotActive_Object((1,3,6,1,4,1,5835,5,2,9200,1,2,2),_NtcPAMAlNotActive_Type())
ntcPAMAlNotActive.setMaxAccess(_I)
if mibBuilder.loadTexts:ntcPAMAlNotActive.setStatus(_A)
_NtcPAMConformance_ObjectIdentity=ObjectIdentity
ntcPAMConformance=_NtcPAMConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9200,2))
if mibBuilder.loadTexts:ntcPAMConformance.setStatus(_A)
_NtcPAMConfCompliance_ObjectIdentity=ObjectIdentity
ntcPAMConfCompliance=_NtcPAMConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9200,2,1))
if mibBuilder.loadTexts:ntcPAMConfCompliance.setStatus(_A)
_NtcPAMConfGroup_ObjectIdentity=ObjectIdentity
ntcPAMConfGroup=_NtcPAMConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,9200,2,2))
if mibBuilder.loadTexts:ntcPAMConfGroup.setStatus(_A)
ntcPAMConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,9200,2,2,1))
ntcPAMConfGrpV1Standard.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:ntcPAMConfGrpV1Standard.setStatus(_A)
ntcPAMConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,9200,2,1,1))
ntcPAMConfCompV1Standard.setObjects((_B,_O))
if mibBuilder.loadTexts:ntcPAMConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcPidActivityMonitor':ntcPidActivityMonitor,'ntcPAMObjects':ntcPAMObjects,'ntcPAMConfiguration':ntcPAMConfiguration,'ntcPAMConfigTable':ntcPAMConfigTable,'ntcPAMConfigEntry':ntcPAMConfigEntry,_F:ntcPAMConfigName,_J:ntcPAMConfigRowStatus,_K:ntcPAMConfigEnable,_L:ntcPAMConfigPid,'ntcPAMAlarms':ntcPAMAlarms,'ntcPAMAlarmStatsTable':ntcPAMAlarmStatsTable,'ntcPAMAlarmStatsEntry':ntcPAMAlarmStatsEntry,_H:ntcPAMAlarmStatsName,_M:ntcPAMAlarmStatsNotActive,_N:ntcPAMAlNotActive,'ntcPAMConformance':ntcPAMConformance,'ntcPAMConfCompliance':ntcPAMConfCompliance,'ntcPAMConfCompV1Standard':ntcPAMConfCompV1Standard,'ntcPAMConfGroup':ntcPAMConfGroup,_O:ntcPAMConfGrpV1Standard})