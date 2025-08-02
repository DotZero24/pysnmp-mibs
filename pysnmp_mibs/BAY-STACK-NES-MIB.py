_R='bsnesEEEPortStatsPort'
_Q='bsnesSavingsUnitIndex'
_P='disabled'
_O='enabled'
_N='bsnesInterfaceIndex'
_M='read-create'
_L='bsnesScheduleMinute'
_K='bsnesScheduleHour'
_J='bsnesScheduleDay'
_I='2018-06-01 00:00'
_H='Unsigned32'
_G='TruthValue'
_F='not-accessible'
_E='BAY-STACK-NES-MIB'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_G)
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackNesMib=ModuleIdentity((1,3,6,1,4,1,45,5,34))
if mibBuilder.loadTexts:bayStackNesMib.setRevisions(('2018-12-04 00:00',_I,_I,'2014-08-22 00:00','2009-05-19 00:00'))
_BayStackNesNotifications_ObjectIdentity=ObjectIdentity
bayStackNesNotifications=_BayStackNesNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,34,0))
_BayStackNesObjects_ObjectIdentity=ObjectIdentity
bayStackNesObjects=_BayStackNesObjects_ObjectIdentity((1,3,6,1,4,1,45,5,34,1))
_BsnesScalars_ObjectIdentity=ObjectIdentity
bsnesScalars=_BsnesScalars_ObjectIdentity((1,3,6,1,4,1,45,5,34,1,1))
_BsnesEnergySaverEnabled_Type=TruthValue
_BsnesEnergySaverEnabled_Object=MibScalar
bsnesEnergySaverEnabled=_BsnesEnergySaverEnabled_Object((1,3,6,1,4,1,45,5,34,1,1,1),_BsnesEnergySaverEnabled_Type())
bsnesEnergySaverEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:bsnesEnergySaverEnabled.setStatus(_A)
_BsnesPoePowerSavingEnabled_Type=TruthValue
_BsnesPoePowerSavingEnabled_Object=MibScalar
bsnesPoePowerSavingEnabled=_BsnesPoePowerSavingEnabled_Object((1,3,6,1,4,1,45,5,34,1,1,2),_BsnesPoePowerSavingEnabled_Type())
bsnesPoePowerSavingEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:bsnesPoePowerSavingEnabled.setStatus(_A)
_BsnesEfficiencyModeEnabled_Type=TruthValue
_BsnesEfficiencyModeEnabled_Object=MibScalar
bsnesEfficiencyModeEnabled=_BsnesEfficiencyModeEnabled_Object((1,3,6,1,4,1,45,5,34,1,1,3),_BsnesEfficiencyModeEnabled_Type())
bsnesEfficiencyModeEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:bsnesEfficiencyModeEnabled.setStatus(_A)
_BsnesEnergySaverActive_Type=TruthValue
_BsnesEnergySaverActive_Object=MibScalar
bsnesEnergySaverActive=_BsnesEnergySaverActive_Object((1,3,6,1,4,1,45,5,34,1,1,4),_BsnesEnergySaverActive_Type())
bsnesEnergySaverActive.setMaxAccess(_B)
if mibBuilder.loadTexts:bsnesEnergySaverActive.setStatus(_A)
class _BsnesEnergySaverClearEEEStats_Type(TruthValue):defaultValue=2
_BsnesEnergySaverClearEEEStats_Type.__name__=_G
_BsnesEnergySaverClearEEEStats_Object=MibScalar
bsnesEnergySaverClearEEEStats=_BsnesEnergySaverClearEEEStats_Object((1,3,6,1,4,1,45,5,34,1,1,5),_BsnesEnergySaverClearEEEStats_Type())
bsnesEnergySaverClearEEEStats.setMaxAccess(_B)
if mibBuilder.loadTexts:bsnesEnergySaverClearEEEStats.setStatus(_A)
_BsnesScheduleTable_Object=MibTable
bsnesScheduleTable=_BsnesScheduleTable_Object((1,3,6,1,4,1,45,5,34,1,2))
if mibBuilder.loadTexts:bsnesScheduleTable.setStatus(_A)
_BsnesScheduleEntry_Object=MibTableRow
bsnesScheduleEntry=_BsnesScheduleEntry_Object((1,3,6,1,4,1,45,5,34,1,2,1))
bsnesScheduleEntry.setIndexNames((0,_E,_J),(0,_E,_K),(0,_E,_L))
if mibBuilder.loadTexts:bsnesScheduleEntry.setStatus(_A)
class _BsnesScheduleDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('monday',1),('tuesday',2),('wednesday',3),('thursday',4),('friday',5),('saturday',6),('sunday',7)))
_BsnesScheduleDay_Type.__name__=_D
_BsnesScheduleDay_Object=MibTableColumn
bsnesScheduleDay=_BsnesScheduleDay_Object((1,3,6,1,4,1,45,5,34,1,2,1,1),_BsnesScheduleDay_Type())
bsnesScheduleDay.setMaxAccess(_F)
if mibBuilder.loadTexts:bsnesScheduleDay.setStatus(_A)
class _BsnesScheduleHour_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23))
_BsnesScheduleHour_Type.__name__=_D
_BsnesScheduleHour_Object=MibTableColumn
bsnesScheduleHour=_BsnesScheduleHour_Object((1,3,6,1,4,1,45,5,34,1,2,1,2),_BsnesScheduleHour_Type())
bsnesScheduleHour.setMaxAccess(_F)
if mibBuilder.loadTexts:bsnesScheduleHour.setStatus(_A)
class _BsnesScheduleMinute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59))
_BsnesScheduleMinute_Type.__name__=_D
_BsnesScheduleMinute_Object=MibTableColumn
bsnesScheduleMinute=_BsnesScheduleMinute_Object((1,3,6,1,4,1,45,5,34,1,2,1,3),_BsnesScheduleMinute_Type())
bsnesScheduleMinute.setMaxAccess(_F)
if mibBuilder.loadTexts:bsnesScheduleMinute.setStatus(_A)
class _BsnesScheduleAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('activate',1),('deactivate',2)))
_BsnesScheduleAction_Type.__name__=_D
_BsnesScheduleAction_Object=MibTableColumn
bsnesScheduleAction=_BsnesScheduleAction_Object((1,3,6,1,4,1,45,5,34,1,2,1,4),_BsnesScheduleAction_Type())
bsnesScheduleAction.setMaxAccess(_M)
if mibBuilder.loadTexts:bsnesScheduleAction.setStatus(_A)
_BsnesScheduleRowStatus_Type=RowStatus
_BsnesScheduleRowStatus_Object=MibTableColumn
bsnesScheduleRowStatus=_BsnesScheduleRowStatus_Object((1,3,6,1,4,1,45,5,34,1,2,1,5),_BsnesScheduleRowStatus_Type())
bsnesScheduleRowStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:bsnesScheduleRowStatus.setStatus(_A)
_BsnesInterfaceTable_Object=MibTable
bsnesInterfaceTable=_BsnesInterfaceTable_Object((1,3,6,1,4,1,45,5,34,1,3))
if mibBuilder.loadTexts:bsnesInterfaceTable.setStatus(_A)
_BsnesInterfaceEntry_Object=MibTableRow
bsnesInterfaceEntry=_BsnesInterfaceEntry_Object((1,3,6,1,4,1,45,5,34,1,3,1))
bsnesInterfaceEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:bsnesInterfaceEntry.setStatus(_A)
_BsnesInterfaceIndex_Type=InterfaceIndex
_BsnesInterfaceIndex_Object=MibTableColumn
bsnesInterfaceIndex=_BsnesInterfaceIndex_Object((1,3,6,1,4,1,45,5,34,1,3,1,1),_BsnesInterfaceIndex_Type())
bsnesInterfaceIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:bsnesInterfaceIndex.setStatus(_A)
_BsnesInterfaceEnergySaverEnabled_Type=TruthValue
_BsnesInterfaceEnergySaverEnabled_Object=MibTableColumn
bsnesInterfaceEnergySaverEnabled=_BsnesInterfaceEnergySaverEnabled_Object((1,3,6,1,4,1,45,5,34,1,3,1,2),_BsnesInterfaceEnergySaverEnabled_Type())
bsnesInterfaceEnergySaverEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:bsnesInterfaceEnergySaverEnabled.setStatus(_A)
class _BsnesInterfaceEnergySaverPoeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_P,2),('notApplicable',3)))
_BsnesInterfaceEnergySaverPoeStatus_Type.__name__=_D
_BsnesInterfaceEnergySaverPoeStatus_Object=MibTableColumn
bsnesInterfaceEnergySaverPoeStatus=_BsnesInterfaceEnergySaverPoeStatus_Object((1,3,6,1,4,1,45,5,34,1,3,1,3),_BsnesInterfaceEnergySaverPoeStatus_Type())
bsnesInterfaceEnergySaverPoeStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bsnesInterfaceEnergySaverPoeStatus.setStatus(_A)
class _BsnesInterfaceEnergySaverEEEEnable_Type(TruthValue):defaultValue=2
_BsnesInterfaceEnergySaverEEEEnable_Type.__name__=_G
_BsnesInterfaceEnergySaverEEEEnable_Object=MibTableColumn
bsnesInterfaceEnergySaverEEEEnable=_BsnesInterfaceEnergySaverEEEEnable_Object((1,3,6,1,4,1,45,5,34,1,3,1,4),_BsnesInterfaceEnergySaverEEEEnable_Type())
bsnesInterfaceEnergySaverEEEEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:bsnesInterfaceEnergySaverEEEEnable.setStatus(_A)
class _BsnesInterfaceClearEEEStats_Type(TruthValue):defaultValue=2
_BsnesInterfaceClearEEEStats_Type.__name__=_G
_BsnesInterfaceClearEEEStats_Object=MibTableColumn
bsnesInterfaceClearEEEStats=_BsnesInterfaceClearEEEStats_Object((1,3,6,1,4,1,45,5,34,1,3,1,5),_BsnesInterfaceClearEEEStats_Type())
bsnesInterfaceClearEEEStats.setMaxAccess(_B)
if mibBuilder.loadTexts:bsnesInterfaceClearEEEStats.setStatus(_A)
_BsnesSavingsTable_Object=MibTable
bsnesSavingsTable=_BsnesSavingsTable_Object((1,3,6,1,4,1,45,5,34,1,4))
if mibBuilder.loadTexts:bsnesSavingsTable.setStatus(_A)
_BsnesSavingsEntry_Object=MibTableRow
bsnesSavingsEntry=_BsnesSavingsEntry_Object((1,3,6,1,4,1,45,5,34,1,4,1))
bsnesSavingsEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:bsnesSavingsEntry.setStatus(_A)
class _BsnesSavingsUnitIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_BsnesSavingsUnitIndex_Type.__name__=_H
_BsnesSavingsUnitIndex_Object=MibTableColumn
bsnesSavingsUnitIndex=_BsnesSavingsUnitIndex_Object((1,3,6,1,4,1,45,5,34,1,4,1,1),_BsnesSavingsUnitIndex_Type())
bsnesSavingsUnitIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:bsnesSavingsUnitIndex.setStatus(_A)
_BsnesSavingsUnitSavings_Type=Unsigned32
_BsnesSavingsUnitSavings_Object=MibTableColumn
bsnesSavingsUnitSavings=_BsnesSavingsUnitSavings_Object((1,3,6,1,4,1,45,5,34,1,4,1,2),_BsnesSavingsUnitSavings_Type())
bsnesSavingsUnitSavings.setMaxAccess(_C)
if mibBuilder.loadTexts:bsnesSavingsUnitSavings.setStatus(_A)
_BsnesSavingsPoeSavings_Type=Unsigned32
_BsnesSavingsPoeSavings_Object=MibTableColumn
bsnesSavingsPoeSavings=_BsnesSavingsPoeSavings_Object((1,3,6,1,4,1,45,5,34,1,4,1,3),_BsnesSavingsPoeSavings_Type())
bsnesSavingsPoeSavings.setMaxAccess(_C)
if mibBuilder.loadTexts:bsnesSavingsPoeSavings.setStatus(_A)
_BsnesEEEPortStatsTable_Object=MibTable
bsnesEEEPortStatsTable=_BsnesEEEPortStatsTable_Object((1,3,6,1,4,1,45,5,34,1,5))
if mibBuilder.loadTexts:bsnesEEEPortStatsTable.setStatus(_A)
_BsnesEEEPortStatsEntry_Object=MibTableRow
bsnesEEEPortStatsEntry=_BsnesEEEPortStatsEntry_Object((1,3,6,1,4,1,45,5,34,1,5,1))
bsnesEEEPortStatsEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:bsnesEEEPortStatsEntry.setStatus(_A)
_BsnesEEEPortStatsPort_Type=InterfaceIndex
_BsnesEEEPortStatsPort_Object=MibTableColumn
bsnesEEEPortStatsPort=_BsnesEEEPortStatsPort_Object((1,3,6,1,4,1,45,5,34,1,5,1,1),_BsnesEEEPortStatsPort_Type())
bsnesEEEPortStatsPort.setMaxAccess(_F)
if mibBuilder.loadTexts:bsnesEEEPortStatsPort.setStatus(_A)
class _BsnesEEEPortStatsState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_O,1),(_P,2),('unsupported',3)))
_BsnesEEEPortStatsState_Type.__name__=_D
_BsnesEEEPortStatsState_Object=MibTableColumn
bsnesEEEPortStatsState=_BsnesEEEPortStatsState_Object((1,3,6,1,4,1,45,5,34,1,5,1,2),_BsnesEEEPortStatsState_Type())
bsnesEEEPortStatsState.setMaxAccess(_C)
if mibBuilder.loadTexts:bsnesEEEPortStatsState.setStatus(_A)
_BsnesEEEPortStatsTxEvents_Type=Integer32
_BsnesEEEPortStatsTxEvents_Object=MibTableColumn
bsnesEEEPortStatsTxEvents=_BsnesEEEPortStatsTxEvents_Object((1,3,6,1,4,1,45,5,34,1,5,1,3),_BsnesEEEPortStatsTxEvents_Type())
bsnesEEEPortStatsTxEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:bsnesEEEPortStatsTxEvents.setStatus(_A)
_BsnesEEEPortStatsTxDuration_Type=Integer32
_BsnesEEEPortStatsTxDuration_Object=MibTableColumn
bsnesEEEPortStatsTxDuration=_BsnesEEEPortStatsTxDuration_Object((1,3,6,1,4,1,45,5,34,1,5,1,4),_BsnesEEEPortStatsTxDuration_Type())
bsnesEEEPortStatsTxDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:bsnesEEEPortStatsTxDuration.setStatus(_A)
_BsnesEEEPortStatsRxEvents_Type=Integer32
_BsnesEEEPortStatsRxEvents_Object=MibTableColumn
bsnesEEEPortStatsRxEvents=_BsnesEEEPortStatsRxEvents_Object((1,3,6,1,4,1,45,5,34,1,5,1,5),_BsnesEEEPortStatsRxEvents_Type())
bsnesEEEPortStatsRxEvents.setMaxAccess(_C)
if mibBuilder.loadTexts:bsnesEEEPortStatsRxEvents.setStatus(_A)
_BsnesEEEPortStatsRxDuration_Type=Integer32
_BsnesEEEPortStatsRxDuration_Object=MibTableColumn
bsnesEEEPortStatsRxDuration=_BsnesEEEPortStatsRxDuration_Object((1,3,6,1,4,1,45,5,34,1,5,1,6),_BsnesEEEPortStatsRxDuration_Type())
bsnesEEEPortStatsRxDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:bsnesEEEPortStatsRxDuration.setStatus(_A)
_BayStackNesNotificationObjects_ObjectIdentity=ObjectIdentity
bayStackNesNotificationObjects=_BayStackNesNotificationObjects_ObjectIdentity((1,3,6,1,4,1,45,5,34,2))
bsnesGloballyEnabled=NotificationType((1,3,6,1,4,1,45,5,34,0,1))
if mibBuilder.loadTexts:bsnesGloballyEnabled.setStatus(_A)
bsnesGloballyDisabled=NotificationType((1,3,6,1,4,1,45,5,34,0,2))
if mibBuilder.loadTexts:bsnesGloballyDisabled.setStatus(_A)
bsnesManuallyActivated=NotificationType((1,3,6,1,4,1,45,5,34,0,3))
if mibBuilder.loadTexts:bsnesManuallyActivated.setStatus(_A)
bsnesManuallyDeactivated=NotificationType((1,3,6,1,4,1,45,5,34,0,4))
if mibBuilder.loadTexts:bsnesManuallyDeactivated.setStatus(_A)
bsnesScheduleNotApplied=NotificationType((1,3,6,1,4,1,45,5,34,0,5))
if mibBuilder.loadTexts:bsnesScheduleNotApplied.setStatus(_A)
bsnesScheduleApplied=NotificationType((1,3,6,1,4,1,45,5,34,0,6))
if mibBuilder.loadTexts:bsnesScheduleApplied.setStatus(_A)
bsnesActivated=NotificationType((1,3,6,1,4,1,45,5,34,0,7))
if mibBuilder.loadTexts:bsnesActivated.setStatus(_A)
bsnesDeactivated=NotificationType((1,3,6,1,4,1,45,5,34,0,8))
if mibBuilder.loadTexts:bsnesDeactivated.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'bayStackNesMib':bayStackNesMib,'bayStackNesNotifications':bayStackNesNotifications,'bsnesGloballyEnabled':bsnesGloballyEnabled,'bsnesGloballyDisabled':bsnesGloballyDisabled,'bsnesManuallyActivated':bsnesManuallyActivated,'bsnesManuallyDeactivated':bsnesManuallyDeactivated,'bsnesScheduleNotApplied':bsnesScheduleNotApplied,'bsnesScheduleApplied':bsnesScheduleApplied,'bsnesActivated':bsnesActivated,'bsnesDeactivated':bsnesDeactivated,'bayStackNesObjects':bayStackNesObjects,'bsnesScalars':bsnesScalars,'bsnesEnergySaverEnabled':bsnesEnergySaverEnabled,'bsnesPoePowerSavingEnabled':bsnesPoePowerSavingEnabled,'bsnesEfficiencyModeEnabled':bsnesEfficiencyModeEnabled,'bsnesEnergySaverActive':bsnesEnergySaverActive,'bsnesEnergySaverClearEEEStats':bsnesEnergySaverClearEEEStats,'bsnesScheduleTable':bsnesScheduleTable,'bsnesScheduleEntry':bsnesScheduleEntry,_J:bsnesScheduleDay,_K:bsnesScheduleHour,_L:bsnesScheduleMinute,'bsnesScheduleAction':bsnesScheduleAction,'bsnesScheduleRowStatus':bsnesScheduleRowStatus,'bsnesInterfaceTable':bsnesInterfaceTable,'bsnesInterfaceEntry':bsnesInterfaceEntry,_N:bsnesInterfaceIndex,'bsnesInterfaceEnergySaverEnabled':bsnesInterfaceEnergySaverEnabled,'bsnesInterfaceEnergySaverPoeStatus':bsnesInterfaceEnergySaverPoeStatus,'bsnesInterfaceEnergySaverEEEEnable':bsnesInterfaceEnergySaverEEEEnable,'bsnesInterfaceClearEEEStats':bsnesInterfaceClearEEEStats,'bsnesSavingsTable':bsnesSavingsTable,'bsnesSavingsEntry':bsnesSavingsEntry,_Q:bsnesSavingsUnitIndex,'bsnesSavingsUnitSavings':bsnesSavingsUnitSavings,'bsnesSavingsPoeSavings':bsnesSavingsPoeSavings,'bsnesEEEPortStatsTable':bsnesEEEPortStatsTable,'bsnesEEEPortStatsEntry':bsnesEEEPortStatsEntry,_R:bsnesEEEPortStatsPort,'bsnesEEEPortStatsState':bsnesEEEPortStatsState,'bsnesEEEPortStatsTxEvents':bsnesEEEPortStatsTxEvents,'bsnesEEEPortStatsTxDuration':bsnesEEEPortStatsTxDuration,'bsnesEEEPortStatsRxEvents':bsnesEEEPortStatsRxEvents,'bsnesEEEPortStatsRxDuration':bsnesEEEPortStatsRxDuration,'bayStackNesNotificationObjects':bayStackNesNotificationObjects})