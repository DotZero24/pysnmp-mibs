_Z='nbSchedMandatoryGroup'
_Y='nbSchedRowStatus'
_X='nbSchedIsCompleted'
_W='nbSchedRemark'
_V='nbSchedCommand'
_U='nbSchedCmdType'
_T='nbSchedNotify'
_S='nbSchedIsNow'
_R='nbSchedInterval'
_Q='nbSchedNumberOfTimes'
_P='nbSchedEndWeekday'
_O='nbSchedEndMonth'
_N='nbSchedEndDay'
_M='nbSchedEndHour'
_L='nbSchedEndMinute'
_K='nbSchedStartWeekday'
_J='nbSchedStartMonth'
_I='nbSchedStartDay'
_H='nbSchedStartHour'
_G='nbSchedStartMinute'
_F='nbSchedIndex'
_E='DisplayString'
_D='Unsigned32'
_C='read-write'
_B='OA-SCHED-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nbSwitchG1Il,=mibBuilder.importSymbols('OS-COMMON-TC-MIB','nbSwitchG1Il')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention','TruthValue')
nbSched=ModuleIdentity((1,3,6,1,4,1,629,1,50,18))
if mibBuilder.loadTexts:nbSched.setRevisions(('2008-01-07 00:00',))
class SchedCommandType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cli',1),('shell',2)))
_NbSchedTable_Object=MibTable
nbSchedTable=_NbSchedTable_Object((1,3,6,1,4,1,629,1,50,18,1))
if mibBuilder.loadTexts:nbSchedTable.setStatus(_A)
_NbSchedEntry_Object=MibTableRow
nbSchedEntry=_NbSchedEntry_Object((1,3,6,1,4,1,629,1,50,18,1,1))
nbSchedEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:nbSchedEntry.setStatus(_A)
class _NbSchedIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535),ValueRangeConstraint(65536,65536))
_NbSchedIndex_Type.__name__=_D
_NbSchedIndex_Object=MibTableColumn
nbSchedIndex=_NbSchedIndex_Object((1,3,6,1,4,1,629,1,50,18,1,1,1),_NbSchedIndex_Type())
nbSchedIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:nbSchedIndex.setStatus(_A)
class _NbSchedStartMinute_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59),ValueRangeConstraint(99,99))
_NbSchedStartMinute_Type.__name__=_D
_NbSchedStartMinute_Object=MibTableColumn
nbSchedStartMinute=_NbSchedStartMinute_Object((1,3,6,1,4,1,629,1,50,18,1,1,4),_NbSchedStartMinute_Type())
nbSchedStartMinute.setMaxAccess(_C)
if mibBuilder.loadTexts:nbSchedStartMinute.setStatus(_A)
class _NbSchedStartHour_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23),ValueRangeConstraint(99,99))
_NbSchedStartHour_Type.__name__=_D
_NbSchedStartHour_Object=MibTableColumn
nbSchedStartHour=_NbSchedStartHour_Object((1,3,6,1,4,1,629,1,50,18,1,1,5),_NbSchedStartHour_Type())
nbSchedStartHour.setMaxAccess(_C)
if mibBuilder.loadTexts:nbSchedStartHour.setStatus(_A)
class _NbSchedStartDay_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31),ValueRangeConstraint(99,99))
_NbSchedStartDay_Type.__name__=_D
_NbSchedStartDay_Object=MibTableColumn
nbSchedStartDay=_NbSchedStartDay_Object((1,3,6,1,4,1,629,1,50,18,1,1,6),_NbSchedStartDay_Type())
nbSchedStartDay.setMaxAccess(_C)
if mibBuilder.loadTexts:nbSchedStartDay.setStatus(_A)
class _NbSchedStartMonth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12),ValueRangeConstraint(99,99))
_NbSchedStartMonth_Type.__name__=_D
_NbSchedStartMonth_Object=MibTableColumn
nbSchedStartMonth=_NbSchedStartMonth_Object((1,3,6,1,4,1,629,1,50,18,1,1,7),_NbSchedStartMonth_Type())
nbSchedStartMonth.setMaxAccess(_C)
if mibBuilder.loadTexts:nbSchedStartMonth.setStatus(_A)
class _NbSchedStartWeekday_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6),ValueRangeConstraint(99,99))
_NbSchedStartWeekday_Type.__name__=_D
_NbSchedStartWeekday_Object=MibTableColumn
nbSchedStartWeekday=_NbSchedStartWeekday_Object((1,3,6,1,4,1,629,1,50,18,1,1,8),_NbSchedStartWeekday_Type())
nbSchedStartWeekday.setMaxAccess(_C)
if mibBuilder.loadTexts:nbSchedStartWeekday.setStatus(_A)
class _NbSchedEndMinute_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,59),ValueRangeConstraint(99,99))
_NbSchedEndMinute_Type.__name__=_D
_NbSchedEndMinute_Object=MibTableColumn
nbSchedEndMinute=_NbSchedEndMinute_Object((1,3,6,1,4,1,629,1,50,18,1,1,10),_NbSchedEndMinute_Type())
nbSchedEndMinute.setMaxAccess(_C)
if mibBuilder.loadTexts:nbSchedEndMinute.setStatus(_A)
class _NbSchedEndHour_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,23),ValueRangeConstraint(99,99))
_NbSchedEndHour_Type.__name__=_D
_NbSchedEndHour_Object=MibTableColumn
nbSchedEndHour=_NbSchedEndHour_Object((1,3,6,1,4,1,629,1,50,18,1,1,11),_NbSchedEndHour_Type())
nbSchedEndHour.setMaxAccess(_C)
if mibBuilder.loadTexts:nbSchedEndHour.setStatus(_A)
class _NbSchedEndDay_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31),ValueRangeConstraint(99,99))
_NbSchedEndDay_Type.__name__=_D
_NbSchedEndDay_Object=MibTableColumn
nbSchedEndDay=_NbSchedEndDay_Object((1,3,6,1,4,1,629,1,50,18,1,1,12),_NbSchedEndDay_Type())
nbSchedEndDay.setMaxAccess(_C)
if mibBuilder.loadTexts:nbSchedEndDay.setStatus(_A)
class _NbSchedEndMonth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12),ValueRangeConstraint(99,99))
_NbSchedEndMonth_Type.__name__=_D
_NbSchedEndMonth_Object=MibTableColumn
nbSchedEndMonth=_NbSchedEndMonth_Object((1,3,6,1,4,1,629,1,50,18,1,1,13),_NbSchedEndMonth_Type())
nbSchedEndMonth.setMaxAccess(_C)
if mibBuilder.loadTexts:nbSchedEndMonth.setStatus(_A)
class _NbSchedEndWeekday_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,6),ValueRangeConstraint(99,99))
_NbSchedEndWeekday_Type.__name__=_D
_NbSchedEndWeekday_Object=MibTableColumn
nbSchedEndWeekday=_NbSchedEndWeekday_Object((1,3,6,1,4,1,629,1,50,18,1,1,14),_NbSchedEndWeekday_Type())
nbSchedEndWeekday.setMaxAccess(_C)
if mibBuilder.loadTexts:nbSchedEndWeekday.setStatus(_A)
class _NbSchedNumberOfTimes_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,527040))
_NbSchedNumberOfTimes_Type.__name__=_D
_NbSchedNumberOfTimes_Object=MibTableColumn
nbSchedNumberOfTimes=_NbSchedNumberOfTimes_Object((1,3,6,1,4,1,629,1,50,18,1,1,20),_NbSchedNumberOfTimes_Type())
nbSchedNumberOfTimes.setMaxAccess(_C)
if mibBuilder.loadTexts:nbSchedNumberOfTimes.setStatus(_A)
class _NbSchedInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,527040))
_NbSchedInterval_Type.__name__=_D
_NbSchedInterval_Object=MibTableColumn
nbSchedInterval=_NbSchedInterval_Object((1,3,6,1,4,1,629,1,50,18,1,1,21),_NbSchedInterval_Type())
nbSchedInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:nbSchedInterval.setStatus(_A)
_NbSchedIsNow_Type=TruthValue
_NbSchedIsNow_Object=MibTableColumn
nbSchedIsNow=_NbSchedIsNow_Object((1,3,6,1,4,1,629,1,50,18,1,1,22),_NbSchedIsNow_Type())
nbSchedIsNow.setMaxAccess(_C)
if mibBuilder.loadTexts:nbSchedIsNow.setStatus(_A)
_NbSchedNotify_Type=TruthValue
_NbSchedNotify_Object=MibTableColumn
nbSchedNotify=_NbSchedNotify_Object((1,3,6,1,4,1,629,1,50,18,1,1,23),_NbSchedNotify_Type())
nbSchedNotify.setMaxAccess(_C)
if mibBuilder.loadTexts:nbSchedNotify.setStatus(_A)
_NbSchedCmdType_Type=SchedCommandType
_NbSchedCmdType_Object=MibTableColumn
nbSchedCmdType=_NbSchedCmdType_Object((1,3,6,1,4,1,629,1,50,18,1,1,24),_NbSchedCmdType_Type())
nbSchedCmdType.setMaxAccess(_C)
if mibBuilder.loadTexts:nbSchedCmdType.setStatus(_A)
class _NbSchedCommand_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,132))
_NbSchedCommand_Type.__name__=_E
_NbSchedCommand_Object=MibTableColumn
nbSchedCommand=_NbSchedCommand_Object((1,3,6,1,4,1,629,1,50,18,1,1,25),_NbSchedCommand_Type())
nbSchedCommand.setMaxAccess(_C)
if mibBuilder.loadTexts:nbSchedCommand.setStatus(_A)
class _NbSchedRemark_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,132))
_NbSchedRemark_Type.__name__=_E
_NbSchedRemark_Object=MibTableColumn
nbSchedRemark=_NbSchedRemark_Object((1,3,6,1,4,1,629,1,50,18,1,1,26),_NbSchedRemark_Type())
nbSchedRemark.setMaxAccess(_C)
if mibBuilder.loadTexts:nbSchedRemark.setStatus(_A)
_NbSchedIsCompleted_Type=TruthValue
_NbSchedIsCompleted_Object=MibTableColumn
nbSchedIsCompleted=_NbSchedIsCompleted_Object((1,3,6,1,4,1,629,1,50,18,1,1,27),_NbSchedIsCompleted_Type())
nbSchedIsCompleted.setMaxAccess('read-only')
if mibBuilder.loadTexts:nbSchedIsCompleted.setStatus(_A)
_NbSchedRowStatus_Type=RowStatus
_NbSchedRowStatus_Object=MibTableColumn
nbSchedRowStatus=_NbSchedRowStatus_Object((1,3,6,1,4,1,629,1,50,18,1,1,28),_NbSchedRowStatus_Type())
nbSchedRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:nbSchedRowStatus.setStatus(_A)
_NbSchedConformance_ObjectIdentity=ObjectIdentity
nbSchedConformance=_NbSchedConformance_ObjectIdentity((1,3,6,1,4,1,629,1,50,18,100))
_NbSchedMIBCompliances_ObjectIdentity=ObjectIdentity
nbSchedMIBCompliances=_NbSchedMIBCompliances_ObjectIdentity((1,3,6,1,4,1,629,1,50,18,100,1))
_NbSchedMIBGroups_ObjectIdentity=ObjectIdentity
nbSchedMIBGroups=_NbSchedMIBGroups_ObjectIdentity((1,3,6,1,4,1,629,1,50,18,100,2))
nbSchedMandatoryGroup=ObjectGroup((1,3,6,1,4,1,629,1,50,18,100,2,1))
nbSchedMandatoryGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:nbSchedMandatoryGroup.setStatus(_A)
nbSchedMIBCompliance=ModuleCompliance((1,3,6,1,4,1,629,1,50,18,100,1,1))
nbSchedMIBCompliance.setObjects((_B,_Z))
if mibBuilder.loadTexts:nbSchedMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SchedCommandType':SchedCommandType,'nbSched':nbSched,'nbSchedTable':nbSchedTable,'nbSchedEntry':nbSchedEntry,_F:nbSchedIndex,_G:nbSchedStartMinute,_H:nbSchedStartHour,_I:nbSchedStartDay,_J:nbSchedStartMonth,_K:nbSchedStartWeekday,_L:nbSchedEndMinute,_M:nbSchedEndHour,_N:nbSchedEndDay,_O:nbSchedEndMonth,_P:nbSchedEndWeekday,_Q:nbSchedNumberOfTimes,_R:nbSchedInterval,_S:nbSchedIsNow,_T:nbSchedNotify,_U:nbSchedCmdType,_V:nbSchedCommand,_W:nbSchedRemark,_X:nbSchedIsCompleted,_Y:nbSchedRowStatus,'nbSchedConformance':nbSchedConformance,'nbSchedMIBCompliances':nbSchedMIBCompliances,'nbSchedMIBCompliance':nbSchedMIBCompliance,'nbSchedMIBGroups':nbSchedMIBGroups,_Z:nbSchedMandatoryGroup})