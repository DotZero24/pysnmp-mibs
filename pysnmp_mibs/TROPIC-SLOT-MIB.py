_o='tnSlotResetGroup'
_n='tnSlotGroup'
_m='tnSlotResetTime'
_l='tnSlotResetReason'
_k='tnSlotReset'
_j='tnSlotMigrationSubType'
_i='tnSlotInsertExtract'
_h='tnSlotDueDate'
_g='tnSlotLifeCycleState'
_f='tnSlotProductCodeSup'
_e='tnSlotProgrammedProductCode'
_d='tnSlotPresentGenericType'
_c='tnSlotProgrammedGenericType'
_b='tnSlotPresentSubType'
_a='tnSlotProgrammedSubType'
_Z='tnSlotMigrationType'
_Y='tnSlotAlmProfName'
_X='tnSlotStateQualifier'
_W='tnSlotOperationalCapability'
_V='tnSlotOperationalState'
_U='tnSlotAdminState'
_T='tnSlotPresentType'
_S='tnSlotProgrammedType'
_R='TropicStateQualifierType'
_Q='TropicOperationalStateType'
_P='TropicOperationalCapabilityType'
_O='TropicNewResetType'
_N='TropicAdminStateType'
_M='Unsigned32'
_L='OctetString'
_K='tnSlotIndex'
_J='tnShelfIndex'
_I='TROPIC-SHELF-MIB'
_H='AluWdmSlotSubType'
_G='Integer32'
_F='SnmpAdminString'
_E='ObjectIdentifier'
_D='read-only'
_C='read-create'
_B='TROPIC-SLOT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,_E)
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tnSlotMIB,tnSlotModules,tropicEmptyCard=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSlotMIB','tnSlotModules','tropicEmptyCard')
tnShelfIndex,=mibBuilder.importSymbols(_I,_J)
TropicAdminStateType,TropicNewResetType,TropicOperationalCapabilityType,TropicOperationalStateType,TropicSlotIndexType,TropicStateQualifierType=mibBuilder.importSymbols('TROPIC-TC',_N,_O,_P,_Q,'TropicSlotIndexType',_R)
tnSlotMibModule=ModuleIdentity((1,3,6,1,4,1,7483,1,1,2,2,2,1))
if mibBuilder.loadTexts:tnSlotMibModule.setRevisions(('2020-07-24 12:00','2020-05-15 12:00','2020-05-08 12:00','2020-03-20 12:00','2020-02-28 12:00','2019-12-13 12:00','2019-08-02 12:00','2019-01-18 12:00','2019-01-11 12:00','2018-12-21 12:00','2018-09-28 12:00','2018-06-15 12:00','2018-02-23 12:00','2017-11-24 12:00','2016-11-16 12:00','2016-11-07 12:00','2016-10-20 12:00','2016-07-12 12:00','2014-02-26 12:00','2013-12-06 12:00','2013-05-21 12:00','2010-12-09 12:00','2009-06-25 12:00','2008-10-16 12:00','2008-09-26 12:00','2008-07-25 12:00','2008-03-06 12:00'))
class AluWdmSlotSubType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,9999)));namedValues=NamedValues(*(('empty',1),('mSubType',2),('rSubType',3),('hSubType',4),('eSubType',5),('lSubType',6),('fSubType',7),('qSubType',8),('lPSubType',9),('unassigned',9999)))
_TnSlotConf_ObjectIdentity=ObjectIdentity
tnSlotConf=_TnSlotConf_ObjectIdentity((1,3,6,1,4,1,7483,2,2,2,1,1))
_TnSlotGroups_ObjectIdentity=ObjectIdentity
tnSlotGroups=_TnSlotGroups_ObjectIdentity((1,3,6,1,4,1,7483,2,2,2,1,1,1))
_TnSlotCompliances_ObjectIdentity=ObjectIdentity
tnSlotCompliances=_TnSlotCompliances_ObjectIdentity((1,3,6,1,4,1,7483,2,2,2,1,1,2))
_TnSlotObjs_ObjectIdentity=ObjectIdentity
tnSlotObjs=_TnSlotObjs_ObjectIdentity((1,3,6,1,4,1,7483,2,2,2,1,2))
_TnSlotBasics_ObjectIdentity=ObjectIdentity
tnSlotBasics=_TnSlotBasics_ObjectIdentity((1,3,6,1,4,1,7483,2,2,2,1,2,2))
_TnSlotTable_Object=MibTable
tnSlotTable=_TnSlotTable_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,1))
if mibBuilder.loadTexts:tnSlotTable.setStatus(_A)
_TnSlotEntry_Object=MibTableRow
tnSlotEntry=_TnSlotEntry_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,1,1))
tnSlotEntry.setIndexNames((0,_I,_J),(0,_B,_K))
if mibBuilder.loadTexts:tnSlotEntry.setStatus(_A)
_TnSlotIndex_Type=TropicSlotIndexType
_TnSlotIndex_Object=MibTableColumn
tnSlotIndex=_TnSlotIndex_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,1,1,1),_TnSlotIndex_Type())
tnSlotIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:tnSlotIndex.setStatus(_A)
class _TnSlotProgrammedType_Type(ObjectIdentifier):defaultValue=1,3,6,1,4,1,7483,1,5,1,1
_TnSlotProgrammedType_Type.__name__=_E
_TnSlotProgrammedType_Object=MibTableColumn
tnSlotProgrammedType=_TnSlotProgrammedType_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,1,1,2),_TnSlotProgrammedType_Type())
tnSlotProgrammedType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSlotProgrammedType.setStatus(_A)
class _TnSlotPresentType_Type(ObjectIdentifier):defaultValue=1,3,6,1,4,1,7483,1,5,1,1
_TnSlotPresentType_Type.__name__=_E
_TnSlotPresentType_Object=MibTableColumn
tnSlotPresentType=_TnSlotPresentType_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,1,1,3),_TnSlotPresentType_Type())
tnSlotPresentType.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSlotPresentType.setStatus(_A)
class _TnSlotAdminState_Type(TropicAdminStateType):defaultValue=2
_TnSlotAdminState_Type.__name__=_N
_TnSlotAdminState_Object=MibTableColumn
tnSlotAdminState=_TnSlotAdminState_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,1,1,4),_TnSlotAdminState_Type())
tnSlotAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSlotAdminState.setStatus(_A)
class _TnSlotOperationalState_Type(TropicOperationalStateType):defaultValue=2
_TnSlotOperationalState_Type.__name__=_Q
_TnSlotOperationalState_Object=MibTableColumn
tnSlotOperationalState=_TnSlotOperationalState_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,1,1,5),_TnSlotOperationalState_Type())
tnSlotOperationalState.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSlotOperationalState.setStatus(_A)
class _TnSlotOperationalCapability_Type(TropicOperationalCapabilityType):defaultValue=1
_TnSlotOperationalCapability_Type.__name__=_P
_TnSlotOperationalCapability_Object=MibTableColumn
tnSlotOperationalCapability=_TnSlotOperationalCapability_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,1,1,6),_TnSlotOperationalCapability_Type())
tnSlotOperationalCapability.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSlotOperationalCapability.setStatus(_A)
class _TnSlotStateQualifier_Type(TropicStateQualifierType):defaultBinValue='0000001'
_TnSlotStateQualifier_Type.__name__=_R
_TnSlotStateQualifier_Object=MibTableColumn
tnSlotStateQualifier=_TnSlotStateQualifier_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,1,1,7),_TnSlotStateQualifier_Type())
tnSlotStateQualifier.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSlotStateQualifier.setStatus(_A)
class _TnSlotAlmProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_TnSlotAlmProfName_Type.__name__=_L
_TnSlotAlmProfName_Object=MibTableColumn
tnSlotAlmProfName=_TnSlotAlmProfName_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,1,1,17),_TnSlotAlmProfName_Type())
tnSlotAlmProfName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSlotAlmProfName.setStatus(_A)
class _TnSlotMigrationType_Type(ObjectIdentifier):defaultValue=1,3,6,1,4,1,7483,1,5,1,1
_TnSlotMigrationType_Type.__name__=_E
_TnSlotMigrationType_Object=MibTableColumn
tnSlotMigrationType=_TnSlotMigrationType_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,1,1,18),_TnSlotMigrationType_Type())
tnSlotMigrationType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSlotMigrationType.setStatus(_A)
class _TnSlotProgrammedSubType_Type(AluWdmSlotSubType):defaultValue=2
_TnSlotProgrammedSubType_Type.__name__=_H
_TnSlotProgrammedSubType_Object=MibTableColumn
tnSlotProgrammedSubType=_TnSlotProgrammedSubType_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,1,1,19),_TnSlotProgrammedSubType_Type())
tnSlotProgrammedSubType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSlotProgrammedSubType.setStatus(_A)
class _TnSlotPresentSubType_Type(AluWdmSlotSubType):defaultValue=2
_TnSlotPresentSubType_Type.__name__=_H
_TnSlotPresentSubType_Object=MibTableColumn
tnSlotPresentSubType=_TnSlotPresentSubType_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,1,1,20),_TnSlotPresentSubType_Type())
tnSlotPresentSubType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSlotPresentSubType.setStatus(_A)
_TnSlotProgrammedGenericType_Type=SnmpAdminString
_TnSlotProgrammedGenericType_Object=MibTableColumn
tnSlotProgrammedGenericType=_TnSlotProgrammedGenericType_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,1,1,21),_TnSlotProgrammedGenericType_Type())
tnSlotProgrammedGenericType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSlotProgrammedGenericType.setStatus(_A)
_TnSlotPresentGenericType_Type=SnmpAdminString
_TnSlotPresentGenericType_Object=MibTableColumn
tnSlotPresentGenericType=_TnSlotPresentGenericType_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,1,1,22),_TnSlotPresentGenericType_Type())
tnSlotPresentGenericType.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSlotPresentGenericType.setStatus(_A)
class _TnSlotProgrammedProductCode_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_TnSlotProgrammedProductCode_Type.__name__=_F
_TnSlotProgrammedProductCode_Object=MibTableColumn
tnSlotProgrammedProductCode=_TnSlotProgrammedProductCode_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,1,1,23),_TnSlotProgrammedProductCode_Type())
tnSlotProgrammedProductCode.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSlotProgrammedProductCode.setStatus(_A)
class _TnSlotProductCodeSup_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_TnSlotProductCodeSup_Type.__name__=_G
_TnSlotProductCodeSup_Object=MibTableColumn
tnSlotProductCodeSup=_TnSlotProductCodeSup_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,1,1,24),_TnSlotProductCodeSup_Type())
tnSlotProductCodeSup.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSlotProductCodeSup.setStatus(_A)
class _TnSlotLifeCycleState_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,45))
_TnSlotLifeCycleState_Type.__name__=_F
_TnSlotLifeCycleState_Object=MibTableColumn
tnSlotLifeCycleState=_TnSlotLifeCycleState_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,1,1,25),_TnSlotLifeCycleState_Type())
tnSlotLifeCycleState.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSlotLifeCycleState.setStatus(_A)
class _TnSlotDueDate_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,30))
_TnSlotDueDate_Type.__name__=_F
_TnSlotDueDate_Object=MibTableColumn
tnSlotDueDate=_TnSlotDueDate_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,1,1,26),_TnSlotDueDate_Type())
tnSlotDueDate.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSlotDueDate.setStatus(_A)
class _TnSlotInsertExtract_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('start',1),('stop',2),('remove',3)))
_TnSlotInsertExtract_Type.__name__=_G
_TnSlotInsertExtract_Object=MibTableColumn
tnSlotInsertExtract=_TnSlotInsertExtract_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,1,1,27),_TnSlotInsertExtract_Type())
tnSlotInsertExtract.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSlotInsertExtract.setStatus(_A)
class _TnSlotMigrationSubType_Type(AluWdmSlotSubType):defaultValue=9999
_TnSlotMigrationSubType_Type.__name__=_H
_TnSlotMigrationSubType_Object=MibTableColumn
tnSlotMigrationSubType=_TnSlotMigrationSubType_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,1,1,28),_TnSlotMigrationSubType_Type())
tnSlotMigrationSubType.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSlotMigrationSubType.setStatus(_A)
_TnSlotResetTable_Object=MibTable
tnSlotResetTable=_TnSlotResetTable_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,2))
if mibBuilder.loadTexts:tnSlotResetTable.setStatus(_A)
_TnSlotResetEntry_Object=MibTableRow
tnSlotResetEntry=_TnSlotResetEntry_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,2,1))
tnSlotResetEntry.setIndexNames((0,_I,_J),(0,_B,_K))
if mibBuilder.loadTexts:tnSlotResetEntry.setStatus(_A)
class _TnSlotReset_Type(TropicNewResetType):defaultValue=1
_TnSlotReset_Type.__name__=_O
_TnSlotReset_Object=MibTableColumn
tnSlotReset=_TnSlotReset_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,2,1,1),_TnSlotReset_Type())
tnSlotReset.setMaxAccess(_C)
if mibBuilder.loadTexts:tnSlotReset.setStatus(_A)
class _TnSlotResetReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44)));namedValues=NamedValues(*(('unknown',0),('powerReset',1),('userReset',2),('ccActivitySwitch',3),('softwareTrap',4),('watchdog',5),('alarmPanelStartupError',6),('softwareStartupError',7),('cardCommsError',8),('softwareAssert',9),('subcomponentSoftwareBadCrc',10),('databaseError',11),('seepError',12),('subcomponentReset',13),('warmReset',14),('coldReset',15),('userBootReset',16),('ntpNotResponding',17),('cardTookNewShelfSerialNumber',18),('subcomponentStartupError',19),('inBootJumperSet',20),('inBootSeep',21),('inBootBank0Corrupt',22),('inBootBank1Corrupt',23),('inBootAppLoadCorrupt',24),('inBootCrashCountExceeded',25),('subcomponentWatchdog',26),('criticalDatabaseStartupError',27),('redundancyError',28),('controlNetworkError',29),('shelfSerialNumberChanged',30),('swlDiskTransferFailure',31),('bitSyncCommsFailure',32),('diskReformatted',33),('diskMissing',34),('diskIoError',35),('cpuStarvation',36),('uiStarvation',37),('sonetSdhModeMismatch',38),('universalCardTypeMismatch',39),('boardMgrPowerCycle',40),('boardMgrProcessorReset',41),('ecProcessExit',42),('eventNvramAccessFailure',43),('userCCActivitySwitch',44)))
_TnSlotResetReason_Type.__name__=_G
_TnSlotResetReason_Object=MibTableColumn
tnSlotResetReason=_TnSlotResetReason_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,2,1,2),_TnSlotResetReason_Type())
tnSlotResetReason.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSlotResetReason.setStatus(_A)
class _TnSlotResetTime_Type(Unsigned32):defaultValue=0
_TnSlotResetTime_Type.__name__=_M
_TnSlotResetTime_Object=MibTableColumn
tnSlotResetTime=_TnSlotResetTime_Object((1,3,6,1,4,1,7483,2,2,2,1,2,2,2,1,3),_TnSlotResetTime_Type())
tnSlotResetTime.setMaxAccess(_D)
if mibBuilder.loadTexts:tnSlotResetTime.setStatus(_A)
tnSlotGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,2,1,1,1,1))
tnSlotGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:tnSlotGroup.setStatus(_A)
tnSlotResetGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,2,1,1,1,2))
tnSlotResetGroup.setObjects(*((_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:tnSlotResetGroup.setStatus(_A)
tnSlotCompliance=ModuleCompliance((1,3,6,1,4,1,7483,2,2,2,1,1,2,1))
tnSlotCompliance.setObjects(*((_B,_n),(_B,_o)))
if mibBuilder.loadTexts:tnSlotCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_H:AluWdmSlotSubType,'tnSlotMibModule':tnSlotMibModule,'tnSlotConf':tnSlotConf,'tnSlotGroups':tnSlotGroups,_n:tnSlotGroup,_o:tnSlotResetGroup,'tnSlotCompliances':tnSlotCompliances,'tnSlotCompliance':tnSlotCompliance,'tnSlotObjs':tnSlotObjs,'tnSlotBasics':tnSlotBasics,'tnSlotTable':tnSlotTable,'tnSlotEntry':tnSlotEntry,_K:tnSlotIndex,_S:tnSlotProgrammedType,_T:tnSlotPresentType,_U:tnSlotAdminState,_V:tnSlotOperationalState,_W:tnSlotOperationalCapability,_X:tnSlotStateQualifier,_Y:tnSlotAlmProfName,_Z:tnSlotMigrationType,_a:tnSlotProgrammedSubType,_b:tnSlotPresentSubType,_c:tnSlotProgrammedGenericType,_d:tnSlotPresentGenericType,_e:tnSlotProgrammedProductCode,_f:tnSlotProductCodeSup,_g:tnSlotLifeCycleState,_h:tnSlotDueDate,_i:tnSlotInsertExtract,_j:tnSlotMigrationSubType,'tnSlotResetTable':tnSlotResetTable,'tnSlotResetEntry':tnSlotResetEntry,_k:tnSlotReset,_l:tnSlotResetReason,_m:tnSlotResetTime})