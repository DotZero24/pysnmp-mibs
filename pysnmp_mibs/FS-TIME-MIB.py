_V='fsTimeRangeMIBGroup'
_U='fsTimeMIBGroup'
_T='fsTimeRangePeriodicRowStatus'
_S='fsTimeRangePeriodicTimeOfDayEnd'
_R='fsTimeRangePeriodicTimeOfDayFS'
_Q='fsTimeRangePeriodicEndWeekDay'
_P='fsTimeRangePeriodicFSWeekDay'
_O='fsTimeRangePeriodicType'
_N='fsTimeRangePeriodicIndex'
_M='fsClockWeek'
_L='fsClockDateAndTime'
_K='fsTimeRangePeriodicTRName'
_J='not-accessible'
_I='fsTimeRangeName'
_H='read-only'
_G='OctetString'
_F='DisplayString'
_E='DateAndTime'
_D='Integer32'
_C='read-create'
_B='FS-TIME-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,_F,'PhysAddress','RowStatus','TextualConvention')
fsTimeMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,15))
if mibBuilder.loadTexts:fsTimeMIB.setRevisions(('2002-03-20 00:00',))
_FsTimeMIBObjects_ObjectIdentity=ObjectIdentity
fsTimeMIBObjects=_FsTimeMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,15,1))
_FsClockDateAndTime_Type=DateAndTime
_FsClockDateAndTime_Object=MibScalar
fsClockDateAndTime=_FsClockDateAndTime_Object((1,3,6,1,4,1,52642,1,1,10,2,15,1,1),_FsClockDateAndTime_Type())
fsClockDateAndTime.setMaxAccess('read-write')
if mibBuilder.loadTexts:fsClockDateAndTime.setStatus(_A)
class _FsClockWeek_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_FsClockWeek_Type.__name__=_D
_FsClockWeek_Object=MibScalar
fsClockWeek=_FsClockWeek_Object((1,3,6,1,4,1,52642,1,1,10,2,15,1,2),_FsClockWeek_Type())
fsClockWeek.setMaxAccess(_H)
if mibBuilder.loadTexts:fsClockWeek.setStatus(_A)
_FsTimeRangeMIBObjects_ObjectIdentity=ObjectIdentity
fsTimeRangeMIBObjects=_FsTimeRangeMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,15,2))
_FsTimeRangeTable_Object=MibTable
fsTimeRangeTable=_FsTimeRangeTable_Object((1,3,6,1,4,1,52642,1,1,10,2,15,2,1))
if mibBuilder.loadTexts:fsTimeRangeTable.setStatus(_A)
_FsTimeRangeEntry_Object=MibTableRow
fsTimeRangeEntry=_FsTimeRangeEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,15,2,1,1))
fsTimeRangeEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:fsTimeRangeEntry.setStatus(_A)
class _FsTimeRangeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsTimeRangeName_Type.__name__=_F
_FsTimeRangeName_Object=MibTableColumn
fsTimeRangeName=_FsTimeRangeName_Object((1,3,6,1,4,1,52642,1,1,10,2,15,2,1,1,1),_FsTimeRangeName_Type())
fsTimeRangeName.setMaxAccess(_J)
if mibBuilder.loadTexts:fsTimeRangeName.setStatus(_A)
class _FsTimeRangePeriodFS_Type(DateAndTime):defaultHexValue='0000010100000000'
_FsTimeRangePeriodFS_Type.__name__=_E
_FsTimeRangePeriodFS_Object=MibTableColumn
fsTimeRangePeriodFS=_FsTimeRangePeriodFS_Object((1,3,6,1,4,1,52642,1,1,10,2,15,2,1,1,2),_FsTimeRangePeriodFS_Type())
fsTimeRangePeriodFS.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTimeRangePeriodFS.setStatus(_A)
class _FsTimeRangePeriodEnd_Type(DateAndTime):defaultHexValue='9999123123595909'
_FsTimeRangePeriodEnd_Type.__name__=_E
_FsTimeRangePeriodEnd_Object=MibTableColumn
fsTimeRangePeriodEnd=_FsTimeRangePeriodEnd_Object((1,3,6,1,4,1,52642,1,1,10,2,15,2,1,1,3),_FsTimeRangePeriodEnd_Type())
fsTimeRangePeriodEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTimeRangePeriodEnd.setStatus(_A)
_FsTimeRangeRowStatus_Type=RowStatus
_FsTimeRangeRowStatus_Object=MibTableColumn
fsTimeRangeRowStatus=_FsTimeRangeRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,15,2,1,1,4),_FsTimeRangeRowStatus_Type())
fsTimeRangeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTimeRangeRowStatus.setStatus(_A)
_FsTimeRangePeriodicTable_Object=MibTable
fsTimeRangePeriodicTable=_FsTimeRangePeriodicTable_Object((1,3,6,1,4,1,52642,1,1,10,2,15,2,2))
if mibBuilder.loadTexts:fsTimeRangePeriodicTable.setStatus(_A)
_FsTimeRangePeriodicEntry_Object=MibTableRow
fsTimeRangePeriodicEntry=_FsTimeRangePeriodicEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,15,2,2,1))
fsTimeRangePeriodicEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:fsTimeRangePeriodicEntry.setStatus(_A)
class _FsTimeRangePeriodicTRName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsTimeRangePeriodicTRName_Type.__name__=_F
_FsTimeRangePeriodicTRName_Object=MibTableColumn
fsTimeRangePeriodicTRName=_FsTimeRangePeriodicTRName_Object((1,3,6,1,4,1,52642,1,1,10,2,15,2,2,1,1),_FsTimeRangePeriodicTRName_Type())
fsTimeRangePeriodicTRName.setMaxAccess(_J)
if mibBuilder.loadTexts:fsTimeRangePeriodicTRName.setStatus(_A)
class _FsTimeRangePeriodicIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsTimeRangePeriodicIndex_Type.__name__=_D
_FsTimeRangePeriodicIndex_Object=MibTableColumn
fsTimeRangePeriodicIndex=_FsTimeRangePeriodicIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,15,2,2,1,2),_FsTimeRangePeriodicIndex_Type())
fsTimeRangePeriodicIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:fsTimeRangePeriodicIndex.setStatus(_A)
class _FsTimeRangePeriodicType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fixed-segment',1),('unfixed-segment',2)))
_FsTimeRangePeriodicType_Type.__name__=_D
_FsTimeRangePeriodicType_Object=MibTableColumn
fsTimeRangePeriodicType=_FsTimeRangePeriodicType_Object((1,3,6,1,4,1,52642,1,1,10,2,15,2,2,1,3),_FsTimeRangePeriodicType_Type())
fsTimeRangePeriodicType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTimeRangePeriodicType.setStatus(_A)
class _FsTimeRangePeriodicFSWeekDay_Type(OctetString):defaultHexValue='fe';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_FsTimeRangePeriodicFSWeekDay_Type.__name__=_G
_FsTimeRangePeriodicFSWeekDay_Object=MibTableColumn
fsTimeRangePeriodicFSWeekDay=_FsTimeRangePeriodicFSWeekDay_Object((1,3,6,1,4,1,52642,1,1,10,2,15,2,2,1,4),_FsTimeRangePeriodicFSWeekDay_Type())
fsTimeRangePeriodicFSWeekDay.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTimeRangePeriodicFSWeekDay.setStatus(_A)
class _FsTimeRangePeriodicEndWeekDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('monday',1),('tuesday',2),('wednesday',3),('thursday',4),('friday',5),('saturday',6),('sunday',7)))
_FsTimeRangePeriodicEndWeekDay_Type.__name__=_D
_FsTimeRangePeriodicEndWeekDay_Object=MibTableColumn
fsTimeRangePeriodicEndWeekDay=_FsTimeRangePeriodicEndWeekDay_Object((1,3,6,1,4,1,52642,1,1,10,2,15,2,2,1,5),_FsTimeRangePeriodicEndWeekDay_Type())
fsTimeRangePeriodicEndWeekDay.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTimeRangePeriodicEndWeekDay.setStatus(_A)
_FsTimeRangePeriodicTimeOfDayFS_Type=DateAndTime
_FsTimeRangePeriodicTimeOfDayFS_Object=MibTableColumn
fsTimeRangePeriodicTimeOfDayFS=_FsTimeRangePeriodicTimeOfDayFS_Object((1,3,6,1,4,1,52642,1,1,10,2,15,2,2,1,6),_FsTimeRangePeriodicTimeOfDayFS_Type())
fsTimeRangePeriodicTimeOfDayFS.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTimeRangePeriodicTimeOfDayFS.setStatus(_A)
_FsTimeRangePeriodicTimeOfDayEnd_Type=DateAndTime
_FsTimeRangePeriodicTimeOfDayEnd_Object=MibTableColumn
fsTimeRangePeriodicTimeOfDayEnd=_FsTimeRangePeriodicTimeOfDayEnd_Object((1,3,6,1,4,1,52642,1,1,10,2,15,2,2,1,7),_FsTimeRangePeriodicTimeOfDayEnd_Type())
fsTimeRangePeriodicTimeOfDayEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTimeRangePeriodicTimeOfDayEnd.setStatus(_A)
_FsTimeRangePeriodicRowStatus_Type=RowStatus
_FsTimeRangePeriodicRowStatus_Object=MibTableColumn
fsTimeRangePeriodicRowStatus=_FsTimeRangePeriodicRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,15,2,2,1,8),_FsTimeRangePeriodicRowStatus_Type())
fsTimeRangePeriodicRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsTimeRangePeriodicRowStatus.setStatus(_A)
_FsTimeMIBConformance_ObjectIdentity=ObjectIdentity
fsTimeMIBConformance=_FsTimeMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,15,3))
_FsTimeMIBCompliances_ObjectIdentity=ObjectIdentity
fsTimeMIBCompliances=_FsTimeMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,15,3,1))
_FsTimeMIBGroups_ObjectIdentity=ObjectIdentity
fsTimeMIBGroups=_FsTimeMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,15,3,2))
fsTimeMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,15,3,2,1))
fsTimeMIBGroup.setObjects(*((_B,_L),(_B,_M)))
if mibBuilder.loadTexts:fsTimeMIBGroup.setStatus(_A)
fsTimeRangeMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,15,3,2,2))
fsTimeRangeMIBGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:fsTimeRangeMIBGroup.setStatus(_A)
fsTimeMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,15,3,1,1))
fsTimeMIBCompliance.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:fsTimeMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsTimeMIB':fsTimeMIB,'fsTimeMIBObjects':fsTimeMIBObjects,_L:fsClockDateAndTime,_M:fsClockWeek,'fsTimeRangeMIBObjects':fsTimeRangeMIBObjects,'fsTimeRangeTable':fsTimeRangeTable,'fsTimeRangeEntry':fsTimeRangeEntry,_I:fsTimeRangeName,'fsTimeRangePeriodFS':fsTimeRangePeriodFS,'fsTimeRangePeriodEnd':fsTimeRangePeriodEnd,'fsTimeRangeRowStatus':fsTimeRangeRowStatus,'fsTimeRangePeriodicTable':fsTimeRangePeriodicTable,'fsTimeRangePeriodicEntry':fsTimeRangePeriodicEntry,_K:fsTimeRangePeriodicTRName,_N:fsTimeRangePeriodicIndex,_O:fsTimeRangePeriodicType,_P:fsTimeRangePeriodicFSWeekDay,_Q:fsTimeRangePeriodicEndWeekDay,_R:fsTimeRangePeriodicTimeOfDayFS,_S:fsTimeRangePeriodicTimeOfDayEnd,_T:fsTimeRangePeriodicRowStatus,'fsTimeMIBConformance':fsTimeMIBConformance,'fsTimeMIBCompliances':fsTimeMIBCompliances,'fsTimeMIBCompliance':fsTimeMIBCompliance,'fsTimeMIBGroups':fsTimeMIBGroups,_U:fsTimeMIBGroup,_V:fsTimeRangeMIBGroup})