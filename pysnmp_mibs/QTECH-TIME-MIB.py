_V='qtechTimeRangeMIBGroup'
_U='qtechTimeMIBGroup'
_T='qtechTimeRangePeriodicRowStatus'
_S='qtechTimeRangePeriodicTimeOfDayEnd'
_R='qtechTimeRangePeriodicTimeOfDayQtech'
_Q='qtechTimeRangePeriodicEndWeekDay'
_P='qtechTimeRangePeriodicQtechWeekDay'
_O='qtechTimeRangePeriodicType'
_N='qtechTimeRangePeriodicIndex'
_M='qtechClockWeek'
_L='qtechClockDateAndTime'
_K='qtechTimeRangePeriodicTRName'
_J='not-accessible'
_I='qtechTimeRangeName'
_H='read-only'
_G='OctetString'
_F='DisplayString'
_E='DateAndTime'
_D='Integer32'
_C='read-create'
_B='QTECH-TIME-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,_F,'PhysAddress','RowStatus','TextualConvention')
qtechTimeMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,15))
if mibBuilder.loadTexts:qtechTimeMIB.setRevisions(('2002-03-20 00:00',))
_QtechTimeMIBObjects_ObjectIdentity=ObjectIdentity
qtechTimeMIBObjects=_QtechTimeMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,15,1))
_QtechClockDateAndTime_Type=DateAndTime
_QtechClockDateAndTime_Object=MibScalar
qtechClockDateAndTime=_QtechClockDateAndTime_Object((1,3,6,1,4,1,27514,1,1,10,2,15,1,1),_QtechClockDateAndTime_Type())
qtechClockDateAndTime.setMaxAccess('read-write')
if mibBuilder.loadTexts:qtechClockDateAndTime.setStatus(_A)
class _QtechClockWeek_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_QtechClockWeek_Type.__name__=_D
_QtechClockWeek_Object=MibScalar
qtechClockWeek=_QtechClockWeek_Object((1,3,6,1,4,1,27514,1,1,10,2,15,1,2),_QtechClockWeek_Type())
qtechClockWeek.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechClockWeek.setStatus(_A)
_QtechTimeRangeMIBObjects_ObjectIdentity=ObjectIdentity
qtechTimeRangeMIBObjects=_QtechTimeRangeMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,15,2))
_QtechTimeRangeTable_Object=MibTable
qtechTimeRangeTable=_QtechTimeRangeTable_Object((1,3,6,1,4,1,27514,1,1,10,2,15,2,1))
if mibBuilder.loadTexts:qtechTimeRangeTable.setStatus(_A)
_QtechTimeRangeEntry_Object=MibTableRow
qtechTimeRangeEntry=_QtechTimeRangeEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,15,2,1,1))
qtechTimeRangeEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:qtechTimeRangeEntry.setStatus(_A)
class _QtechTimeRangeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechTimeRangeName_Type.__name__=_F
_QtechTimeRangeName_Object=MibTableColumn
qtechTimeRangeName=_QtechTimeRangeName_Object((1,3,6,1,4,1,27514,1,1,10,2,15,2,1,1,1),_QtechTimeRangeName_Type())
qtechTimeRangeName.setMaxAccess(_J)
if mibBuilder.loadTexts:qtechTimeRangeName.setStatus(_A)
class _QtechTimeRangePeriodQtech_Type(DateAndTime):defaultHexValue='0000010100000000'
_QtechTimeRangePeriodQtech_Type.__name__=_E
_QtechTimeRangePeriodQtech_Object=MibTableColumn
qtechTimeRangePeriodQtech=_QtechTimeRangePeriodQtech_Object((1,3,6,1,4,1,27514,1,1,10,2,15,2,1,1,2),_QtechTimeRangePeriodQtech_Type())
qtechTimeRangePeriodQtech.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTimeRangePeriodQtech.setStatus(_A)
class _QtechTimeRangePeriodEnd_Type(DateAndTime):defaultHexValue='9999123123595909'
_QtechTimeRangePeriodEnd_Type.__name__=_E
_QtechTimeRangePeriodEnd_Object=MibTableColumn
qtechTimeRangePeriodEnd=_QtechTimeRangePeriodEnd_Object((1,3,6,1,4,1,27514,1,1,10,2,15,2,1,1,3),_QtechTimeRangePeriodEnd_Type())
qtechTimeRangePeriodEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTimeRangePeriodEnd.setStatus(_A)
_QtechTimeRangeRowStatus_Type=RowStatus
_QtechTimeRangeRowStatus_Object=MibTableColumn
qtechTimeRangeRowStatus=_QtechTimeRangeRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,15,2,1,1,4),_QtechTimeRangeRowStatus_Type())
qtechTimeRangeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTimeRangeRowStatus.setStatus(_A)
_QtechTimeRangePeriodicTable_Object=MibTable
qtechTimeRangePeriodicTable=_QtechTimeRangePeriodicTable_Object((1,3,6,1,4,1,27514,1,1,10,2,15,2,2))
if mibBuilder.loadTexts:qtechTimeRangePeriodicTable.setStatus(_A)
_QtechTimeRangePeriodicEntry_Object=MibTableRow
qtechTimeRangePeriodicEntry=_QtechTimeRangePeriodicEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,15,2,2,1))
qtechTimeRangePeriodicEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:qtechTimeRangePeriodicEntry.setStatus(_A)
class _QtechTimeRangePeriodicTRName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechTimeRangePeriodicTRName_Type.__name__=_F
_QtechTimeRangePeriodicTRName_Object=MibTableColumn
qtechTimeRangePeriodicTRName=_QtechTimeRangePeriodicTRName_Object((1,3,6,1,4,1,27514,1,1,10,2,15,2,2,1,1),_QtechTimeRangePeriodicTRName_Type())
qtechTimeRangePeriodicTRName.setMaxAccess(_J)
if mibBuilder.loadTexts:qtechTimeRangePeriodicTRName.setStatus(_A)
class _QtechTimeRangePeriodicIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_QtechTimeRangePeriodicIndex_Type.__name__=_D
_QtechTimeRangePeriodicIndex_Object=MibTableColumn
qtechTimeRangePeriodicIndex=_QtechTimeRangePeriodicIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,15,2,2,1,2),_QtechTimeRangePeriodicIndex_Type())
qtechTimeRangePeriodicIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechTimeRangePeriodicIndex.setStatus(_A)
class _QtechTimeRangePeriodicType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fixed-segment',1),('unfixed-segment',2)))
_QtechTimeRangePeriodicType_Type.__name__=_D
_QtechTimeRangePeriodicType_Object=MibTableColumn
qtechTimeRangePeriodicType=_QtechTimeRangePeriodicType_Object((1,3,6,1,4,1,27514,1,1,10,2,15,2,2,1,3),_QtechTimeRangePeriodicType_Type())
qtechTimeRangePeriodicType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTimeRangePeriodicType.setStatus(_A)
class _QtechTimeRangePeriodicQtechWeekDay_Type(OctetString):defaultHexValue='fe';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_QtechTimeRangePeriodicQtechWeekDay_Type.__name__=_G
_QtechTimeRangePeriodicQtechWeekDay_Object=MibTableColumn
qtechTimeRangePeriodicQtechWeekDay=_QtechTimeRangePeriodicQtechWeekDay_Object((1,3,6,1,4,1,27514,1,1,10,2,15,2,2,1,4),_QtechTimeRangePeriodicQtechWeekDay_Type())
qtechTimeRangePeriodicQtechWeekDay.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTimeRangePeriodicQtechWeekDay.setStatus(_A)
class _QtechTimeRangePeriodicEndWeekDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('monday',1),('tuesday',2),('wednesday',3),('thursday',4),('friday',5),('saturday',6),('sunday',7)))
_QtechTimeRangePeriodicEndWeekDay_Type.__name__=_D
_QtechTimeRangePeriodicEndWeekDay_Object=MibTableColumn
qtechTimeRangePeriodicEndWeekDay=_QtechTimeRangePeriodicEndWeekDay_Object((1,3,6,1,4,1,27514,1,1,10,2,15,2,2,1,5),_QtechTimeRangePeriodicEndWeekDay_Type())
qtechTimeRangePeriodicEndWeekDay.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTimeRangePeriodicEndWeekDay.setStatus(_A)
_QtechTimeRangePeriodicTimeOfDayQtech_Type=DateAndTime
_QtechTimeRangePeriodicTimeOfDayQtech_Object=MibTableColumn
qtechTimeRangePeriodicTimeOfDayQtech=_QtechTimeRangePeriodicTimeOfDayQtech_Object((1,3,6,1,4,1,27514,1,1,10,2,15,2,2,1,6),_QtechTimeRangePeriodicTimeOfDayQtech_Type())
qtechTimeRangePeriodicTimeOfDayQtech.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTimeRangePeriodicTimeOfDayQtech.setStatus(_A)
_QtechTimeRangePeriodicTimeOfDayEnd_Type=DateAndTime
_QtechTimeRangePeriodicTimeOfDayEnd_Object=MibTableColumn
qtechTimeRangePeriodicTimeOfDayEnd=_QtechTimeRangePeriodicTimeOfDayEnd_Object((1,3,6,1,4,1,27514,1,1,10,2,15,2,2,1,7),_QtechTimeRangePeriodicTimeOfDayEnd_Type())
qtechTimeRangePeriodicTimeOfDayEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTimeRangePeriodicTimeOfDayEnd.setStatus(_A)
_QtechTimeRangePeriodicRowStatus_Type=RowStatus
_QtechTimeRangePeriodicRowStatus_Object=MibTableColumn
qtechTimeRangePeriodicRowStatus=_QtechTimeRangePeriodicRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,15,2,2,1,8),_QtechTimeRangePeriodicRowStatus_Type())
qtechTimeRangePeriodicRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechTimeRangePeriodicRowStatus.setStatus(_A)
_QtechTimeMIBConformance_ObjectIdentity=ObjectIdentity
qtechTimeMIBConformance=_QtechTimeMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,15,3))
_QtechTimeMIBCompliances_ObjectIdentity=ObjectIdentity
qtechTimeMIBCompliances=_QtechTimeMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,15,3,1))
_QtechTimeMIBGroups_ObjectIdentity=ObjectIdentity
qtechTimeMIBGroups=_QtechTimeMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,15,3,2))
qtechTimeMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,15,3,2,1))
qtechTimeMIBGroup.setObjects(*((_B,_L),(_B,_M)))
if mibBuilder.loadTexts:qtechTimeMIBGroup.setStatus(_A)
qtechTimeRangeMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,15,3,2,2))
qtechTimeRangeMIBGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:qtechTimeRangeMIBGroup.setStatus(_A)
qtechTimeMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,15,3,1,1))
qtechTimeMIBCompliance.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:qtechTimeMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechTimeMIB':qtechTimeMIB,'qtechTimeMIBObjects':qtechTimeMIBObjects,_L:qtechClockDateAndTime,_M:qtechClockWeek,'qtechTimeRangeMIBObjects':qtechTimeRangeMIBObjects,'qtechTimeRangeTable':qtechTimeRangeTable,'qtechTimeRangeEntry':qtechTimeRangeEntry,_I:qtechTimeRangeName,'qtechTimeRangePeriodQtech':qtechTimeRangePeriodQtech,'qtechTimeRangePeriodEnd':qtechTimeRangePeriodEnd,'qtechTimeRangeRowStatus':qtechTimeRangeRowStatus,'qtechTimeRangePeriodicTable':qtechTimeRangePeriodicTable,'qtechTimeRangePeriodicEntry':qtechTimeRangePeriodicEntry,_K:qtechTimeRangePeriodicTRName,_N:qtechTimeRangePeriodicIndex,_O:qtechTimeRangePeriodicType,_P:qtechTimeRangePeriodicQtechWeekDay,_Q:qtechTimeRangePeriodicEndWeekDay,_R:qtechTimeRangePeriodicTimeOfDayQtech,_S:qtechTimeRangePeriodicTimeOfDayEnd,_T:qtechTimeRangePeriodicRowStatus,'qtechTimeMIBConformance':qtechTimeMIBConformance,'qtechTimeMIBCompliances':qtechTimeMIBCompliances,'qtechTimeMIBCompliance':qtechTimeMIBCompliance,'qtechTimeMIBGroups':qtechTimeMIBGroups,_U:qtechTimeMIBGroup,_V:qtechTimeRangeMIBGroup})