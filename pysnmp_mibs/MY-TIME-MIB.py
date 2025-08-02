_W='myTimeRangeMIBGroup'
_V='myTimeMIBGroup'
_U='myTimeRangePeriodicRowStatus'
_T='myTimeRangePeriodicTimeOfDayEnd'
_S='myTimeRangePeriodicTimeOfDayMy'
_R='myTimeRangePeriodicEndWeekDay'
_Q='myTimeRangePeriodicMyWeekDay'
_P='myTimeRangePeriodicType'
_O='myTimeRangePeriodicIndex'
_N='myClockWeek'
_M='myClockDateAndTime'
_L='read-create'
_K='not-accessible'
_J='myTimeRangeName'
_I='read-only'
_H='OctetString'
_G='myTimeRangePeriodicTRName'
_F='DisplayString'
_E='DateAndTime'
_D='Integer32'
_C='read-write'
_B='MY-TIME-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('MY-SMI','myMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,_F,'PhysAddress','RowStatus','TextualConvention','TruthValue')
myTimeMIB=ModuleIdentity((1,3,6,1,4,1,4881,1,1,10,2,15))
if mibBuilder.loadTexts:myTimeMIB.setRevisions(('2002-03-20 00:00',))
_MyTimeMIBObjects_ObjectIdentity=ObjectIdentity
myTimeMIBObjects=_MyTimeMIBObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,15,1))
_MyClockDateAndTime_Type=DateAndTime
_MyClockDateAndTime_Object=MibScalar
myClockDateAndTime=_MyClockDateAndTime_Object((1,3,6,1,4,1,4881,1,1,10,2,15,1,1),_MyClockDateAndTime_Type())
myClockDateAndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:myClockDateAndTime.setStatus(_A)
class _MyClockWeek_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,7))
_MyClockWeek_Type.__name__=_D
_MyClockWeek_Object=MibScalar
myClockWeek=_MyClockWeek_Object((1,3,6,1,4,1,4881,1,1,10,2,15,1,2),_MyClockWeek_Type())
myClockWeek.setMaxAccess(_I)
if mibBuilder.loadTexts:myClockWeek.setStatus(_A)
_MyTimeRangeMIBObjects_ObjectIdentity=ObjectIdentity
myTimeRangeMIBObjects=_MyTimeRangeMIBObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,15,2))
_MyTimeRangeTable_Object=MibTable
myTimeRangeTable=_MyTimeRangeTable_Object((1,3,6,1,4,1,4881,1,1,10,2,15,2,1))
if mibBuilder.loadTexts:myTimeRangeTable.setStatus(_A)
_MyTimeRangeEntry_Object=MibTableRow
myTimeRangeEntry=_MyTimeRangeEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,15,2,1,1))
myTimeRangeEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:myTimeRangeEntry.setStatus(_A)
class _MyTimeRangeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MyTimeRangeName_Type.__name__=_F
_MyTimeRangeName_Object=MibTableColumn
myTimeRangeName=_MyTimeRangeName_Object((1,3,6,1,4,1,4881,1,1,10,2,15,2,1,1,1),_MyTimeRangeName_Type())
myTimeRangeName.setMaxAccess(_K)
if mibBuilder.loadTexts:myTimeRangeName.setStatus(_A)
class _MyTimeRangePeriodMy_Type(DateAndTime):defaultHexValue='0000010100000000'
_MyTimeRangePeriodMy_Type.__name__=_E
_MyTimeRangePeriodMy_Object=MibTableColumn
myTimeRangePeriodMy=_MyTimeRangePeriodMy_Object((1,3,6,1,4,1,4881,1,1,10,2,15,2,1,1,2),_MyTimeRangePeriodMy_Type())
myTimeRangePeriodMy.setMaxAccess(_C)
if mibBuilder.loadTexts:myTimeRangePeriodMy.setStatus(_A)
class _MyTimeRangePeriodEnd_Type(DateAndTime):defaultHexValue='9999123123595909'
_MyTimeRangePeriodEnd_Type.__name__=_E
_MyTimeRangePeriodEnd_Object=MibTableColumn
myTimeRangePeriodEnd=_MyTimeRangePeriodEnd_Object((1,3,6,1,4,1,4881,1,1,10,2,15,2,1,1,3),_MyTimeRangePeriodEnd_Type())
myTimeRangePeriodEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:myTimeRangePeriodEnd.setStatus(_A)
_MyTimeRangeRowStatus_Type=RowStatus
_MyTimeRangeRowStatus_Object=MibTableColumn
myTimeRangeRowStatus=_MyTimeRangeRowStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,15,2,1,1,4),_MyTimeRangeRowStatus_Type())
myTimeRangeRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:myTimeRangeRowStatus.setStatus(_A)
_MyTimeRangePeriodicTable_Object=MibTable
myTimeRangePeriodicTable=_MyTimeRangePeriodicTable_Object((1,3,6,1,4,1,4881,1,1,10,2,15,2,2))
if mibBuilder.loadTexts:myTimeRangePeriodicTable.setStatus(_A)
_MyTimeRangePeriodicEntry_Object=MibTableRow
myTimeRangePeriodicEntry=_MyTimeRangePeriodicEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,15,2,2,1))
myTimeRangePeriodicEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:myTimeRangePeriodicEntry.setStatus(_A)
class _MyTimeRangePeriodicTRName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MyTimeRangePeriodicTRName_Type.__name__=_F
_MyTimeRangePeriodicTRName_Object=MibTableColumn
myTimeRangePeriodicTRName=_MyTimeRangePeriodicTRName_Object((1,3,6,1,4,1,4881,1,1,10,2,15,2,2,1,1),_MyTimeRangePeriodicTRName_Type())
myTimeRangePeriodicTRName.setMaxAccess(_K)
if mibBuilder.loadTexts:myTimeRangePeriodicTRName.setStatus(_A)
class _MyTimeRangePeriodicIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_MyTimeRangePeriodicIndex_Type.__name__=_D
_MyTimeRangePeriodicIndex_Object=MibTableColumn
myTimeRangePeriodicIndex=_MyTimeRangePeriodicIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,15,2,2,1,2),_MyTimeRangePeriodicIndex_Type())
myTimeRangePeriodicIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:myTimeRangePeriodicIndex.setStatus(_A)
class _MyTimeRangePeriodicType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fixed-segment',1),('unfixed-segment',2)))
_MyTimeRangePeriodicType_Type.__name__=_D
_MyTimeRangePeriodicType_Object=MibTableColumn
myTimeRangePeriodicType=_MyTimeRangePeriodicType_Object((1,3,6,1,4,1,4881,1,1,10,2,15,2,2,1,3),_MyTimeRangePeriodicType_Type())
myTimeRangePeriodicType.setMaxAccess(_C)
if mibBuilder.loadTexts:myTimeRangePeriodicType.setStatus(_A)
class _MyTimeRangePeriodicMyWeekDay_Type(OctetString):defaultHexValue='fe';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_MyTimeRangePeriodicMyWeekDay_Type.__name__=_H
_MyTimeRangePeriodicMyWeekDay_Object=MibTableColumn
myTimeRangePeriodicMyWeekDay=_MyTimeRangePeriodicMyWeekDay_Object((1,3,6,1,4,1,4881,1,1,10,2,15,2,2,1,4),_MyTimeRangePeriodicMyWeekDay_Type())
myTimeRangePeriodicMyWeekDay.setMaxAccess(_C)
if mibBuilder.loadTexts:myTimeRangePeriodicMyWeekDay.setStatus(_A)
class _MyTimeRangePeriodicEndWeekDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('monday',1),('tuesday',2),('wednesday',3),('thursday',4),('friday',5),('saturday',6),('sunday',7)))
_MyTimeRangePeriodicEndWeekDay_Type.__name__=_D
_MyTimeRangePeriodicEndWeekDay_Object=MibTableColumn
myTimeRangePeriodicEndWeekDay=_MyTimeRangePeriodicEndWeekDay_Object((1,3,6,1,4,1,4881,1,1,10,2,15,2,2,1,5),_MyTimeRangePeriodicEndWeekDay_Type())
myTimeRangePeriodicEndWeekDay.setMaxAccess(_C)
if mibBuilder.loadTexts:myTimeRangePeriodicEndWeekDay.setStatus(_A)
_MyTimeRangePeriodicTimeOfDayMy_Type=DateAndTime
_MyTimeRangePeriodicTimeOfDayMy_Object=MibTableColumn
myTimeRangePeriodicTimeOfDayMy=_MyTimeRangePeriodicTimeOfDayMy_Object((1,3,6,1,4,1,4881,1,1,10,2,15,2,2,1,6),_MyTimeRangePeriodicTimeOfDayMy_Type())
myTimeRangePeriodicTimeOfDayMy.setMaxAccess(_C)
if mibBuilder.loadTexts:myTimeRangePeriodicTimeOfDayMy.setStatus(_A)
_MyTimeRangePeriodicTimeOfDayEnd_Type=DateAndTime
_MyTimeRangePeriodicTimeOfDayEnd_Object=MibTableColumn
myTimeRangePeriodicTimeOfDayEnd=_MyTimeRangePeriodicTimeOfDayEnd_Object((1,3,6,1,4,1,4881,1,1,10,2,15,2,2,1,7),_MyTimeRangePeriodicTimeOfDayEnd_Type())
myTimeRangePeriodicTimeOfDayEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:myTimeRangePeriodicTimeOfDayEnd.setStatus(_A)
_MyTimeRangePeriodicRowStatus_Type=RowStatus
_MyTimeRangePeriodicRowStatus_Object=MibTableColumn
myTimeRangePeriodicRowStatus=_MyTimeRangePeriodicRowStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,15,2,2,1,8),_MyTimeRangePeriodicRowStatus_Type())
myTimeRangePeriodicRowStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:myTimeRangePeriodicRowStatus.setStatus(_A)
_MyTimeMIBConformance_ObjectIdentity=ObjectIdentity
myTimeMIBConformance=_MyTimeMIBConformance_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,15,3))
_MyTimeMIBCompliances_ObjectIdentity=ObjectIdentity
myTimeMIBCompliances=_MyTimeMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,15,3,1))
_MyTimeMIBGroups_ObjectIdentity=ObjectIdentity
myTimeMIBGroups=_MyTimeMIBGroups_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,15,3,2))
myTimeMIBGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,15,3,2,1))
myTimeMIBGroup.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:myTimeMIBGroup.setStatus(_A)
myTimeRangeMIBGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,15,3,2,2))
myTimeRangeMIBGroup.setObjects(*((_B,_G),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:myTimeRangeMIBGroup.setStatus(_A)
myTimeMIBCompliance=ModuleCompliance((1,3,6,1,4,1,4881,1,1,10,2,15,3,1,1))
myTimeMIBCompliance.setObjects(*((_B,_V),(_B,_W)))
if mibBuilder.loadTexts:myTimeMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'myTimeMIB':myTimeMIB,'myTimeMIBObjects':myTimeMIBObjects,_M:myClockDateAndTime,_N:myClockWeek,'myTimeRangeMIBObjects':myTimeRangeMIBObjects,'myTimeRangeTable':myTimeRangeTable,'myTimeRangeEntry':myTimeRangeEntry,_J:myTimeRangeName,'myTimeRangePeriodMy':myTimeRangePeriodMy,'myTimeRangePeriodEnd':myTimeRangePeriodEnd,'myTimeRangeRowStatus':myTimeRangeRowStatus,'myTimeRangePeriodicTable':myTimeRangePeriodicTable,'myTimeRangePeriodicEntry':myTimeRangePeriodicEntry,_G:myTimeRangePeriodicTRName,_O:myTimeRangePeriodicIndex,_P:myTimeRangePeriodicType,_Q:myTimeRangePeriodicMyWeekDay,_R:myTimeRangePeriodicEndWeekDay,_S:myTimeRangePeriodicTimeOfDayMy,_T:myTimeRangePeriodicTimeOfDayEnd,_U:myTimeRangePeriodicRowStatus,'myTimeMIBConformance':myTimeMIBConformance,'myTimeMIBCompliances':myTimeMIBCompliances,'myTimeMIBCompliance':myTimeMIBCompliance,'myTimeMIBGroups':myTimeMIBGroups,_V:myTimeMIBGroup,_W:myTimeRangeMIBGroup})