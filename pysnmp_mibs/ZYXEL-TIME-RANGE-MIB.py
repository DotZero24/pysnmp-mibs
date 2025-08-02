_N='not-accessible'
_M='zyTimeRangeType'
_L='zyTimeRangeName'
_K='sunday'
_J='saturday'
_I='friday'
_H='thursday'
_G='wednesday'
_F='tuesday'
_E='monday'
_D='Integer32'
_C='ZYXEL-TIME-RANGE-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols('BRIDGE-MIB','dot1dBasePort')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','StorageType','TextualConvention','TruthValue')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelTimeRange=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,98))
class ZyTimeRangeWeekDayList(TextualConvention,Bits):status=_A;namedValues=NamedValues(*((_E,0),(_F,1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6)))
_ZyxelTimeRangeSetup_ObjectIdentity=ObjectIdentity
zyxelTimeRangeSetup=_ZyxelTimeRangeSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,98,1))
_ZyTimeRangeMaxNumberOfProfiles_Type=Integer32
_ZyTimeRangeMaxNumberOfProfiles_Object=MibScalar
zyTimeRangeMaxNumberOfProfiles=_ZyTimeRangeMaxNumberOfProfiles_Object((1,3,6,1,4,1,890,1,15,3,98,1,1),_ZyTimeRangeMaxNumberOfProfiles_Type())
zyTimeRangeMaxNumberOfProfiles.setMaxAccess('read-only')
if mibBuilder.loadTexts:zyTimeRangeMaxNumberOfProfiles.setStatus(_A)
_ZyxelTimeRangeTable_Object=MibTable
zyxelTimeRangeTable=_ZyxelTimeRangeTable_Object((1,3,6,1,4,1,890,1,15,3,98,1,2))
if mibBuilder.loadTexts:zyxelTimeRangeTable.setStatus(_A)
_ZyxelTimeRangeEntry_Object=MibTableRow
zyxelTimeRangeEntry=_ZyxelTimeRangeEntry_Object((1,3,6,1,4,1,890,1,15,3,98,1,2,1))
zyxelTimeRangeEntry.setIndexNames((0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:zyxelTimeRangeEntry.setStatus(_A)
_ZyTimeRangeName_Type=DisplayString
_ZyTimeRangeName_Object=MibTableColumn
zyTimeRangeName=_ZyTimeRangeName_Object((1,3,6,1,4,1,890,1,15,3,98,1,2,1,1),_ZyTimeRangeName_Type())
zyTimeRangeName.setMaxAccess(_N)
if mibBuilder.loadTexts:zyTimeRangeName.setStatus(_A)
class _ZyTimeRangeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('absolute',1),('periodic',2)))
_ZyTimeRangeType_Type.__name__=_D
_ZyTimeRangeType_Object=MibTableColumn
zyTimeRangeType=_ZyTimeRangeType_Object((1,3,6,1,4,1,890,1,15,3,98,1,2,1,2),_ZyTimeRangeType_Type())
zyTimeRangeType.setMaxAccess(_N)
if mibBuilder.loadTexts:zyTimeRangeType.setStatus(_A)
_ZyTimeRangeRowStatus_Type=RowStatus
_ZyTimeRangeRowStatus_Object=MibTableColumn
zyTimeRangeRowStatus=_ZyTimeRangeRowStatus_Object((1,3,6,1,4,1,890,1,15,3,98,1,2,1,3),_ZyTimeRangeRowStatus_Type())
zyTimeRangeRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyTimeRangeRowStatus.setStatus(_A)
_ZyxelTimeRangeAbsoluteTable_Object=MibTable
zyxelTimeRangeAbsoluteTable=_ZyxelTimeRangeAbsoluteTable_Object((1,3,6,1,4,1,890,1,15,3,98,1,3))
if mibBuilder.loadTexts:zyxelTimeRangeAbsoluteTable.setStatus(_A)
_ZyxelTimeRangeAbsoluteEntry_Object=MibTableRow
zyxelTimeRangeAbsoluteEntry=_ZyxelTimeRangeAbsoluteEntry_Object((1,3,6,1,4,1,890,1,15,3,98,1,3,1))
zyxelTimeRangeAbsoluteEntry.setIndexNames((0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:zyxelTimeRangeAbsoluteEntry.setStatus(_A)
_ZyTimeRangeAbsoluteStartYear_Type=Integer32
_ZyTimeRangeAbsoluteStartYear_Object=MibTableColumn
zyTimeRangeAbsoluteStartYear=_ZyTimeRangeAbsoluteStartYear_Object((1,3,6,1,4,1,890,1,15,3,98,1,3,1,1),_ZyTimeRangeAbsoluteStartYear_Type())
zyTimeRangeAbsoluteStartYear.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTimeRangeAbsoluteStartYear.setStatus(_A)
_ZyTimeRangeAbsoluteStartMonth_Type=Integer32
_ZyTimeRangeAbsoluteStartMonth_Object=MibTableColumn
zyTimeRangeAbsoluteStartMonth=_ZyTimeRangeAbsoluteStartMonth_Object((1,3,6,1,4,1,890,1,15,3,98,1,3,1,2),_ZyTimeRangeAbsoluteStartMonth_Type())
zyTimeRangeAbsoluteStartMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTimeRangeAbsoluteStartMonth.setStatus(_A)
_ZyTimeRangeAbsoluteStartDate_Type=Integer32
_ZyTimeRangeAbsoluteStartDate_Object=MibTableColumn
zyTimeRangeAbsoluteStartDate=_ZyTimeRangeAbsoluteStartDate_Object((1,3,6,1,4,1,890,1,15,3,98,1,3,1,3),_ZyTimeRangeAbsoluteStartDate_Type())
zyTimeRangeAbsoluteStartDate.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTimeRangeAbsoluteStartDate.setStatus(_A)
_ZyTimeRangeAbsoluteStartHour_Type=Integer32
_ZyTimeRangeAbsoluteStartHour_Object=MibTableColumn
zyTimeRangeAbsoluteStartHour=_ZyTimeRangeAbsoluteStartHour_Object((1,3,6,1,4,1,890,1,15,3,98,1,3,1,4),_ZyTimeRangeAbsoluteStartHour_Type())
zyTimeRangeAbsoluteStartHour.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTimeRangeAbsoluteStartHour.setStatus(_A)
_ZyTimeRangeAbsoluteStartMinute_Type=Integer32
_ZyTimeRangeAbsoluteStartMinute_Object=MibTableColumn
zyTimeRangeAbsoluteStartMinute=_ZyTimeRangeAbsoluteStartMinute_Object((1,3,6,1,4,1,890,1,15,3,98,1,3,1,5),_ZyTimeRangeAbsoluteStartMinute_Type())
zyTimeRangeAbsoluteStartMinute.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTimeRangeAbsoluteStartMinute.setStatus(_A)
_ZyTimeRangeAbsoluteEndYear_Type=Integer32
_ZyTimeRangeAbsoluteEndYear_Object=MibTableColumn
zyTimeRangeAbsoluteEndYear=_ZyTimeRangeAbsoluteEndYear_Object((1,3,6,1,4,1,890,1,15,3,98,1,3,1,6),_ZyTimeRangeAbsoluteEndYear_Type())
zyTimeRangeAbsoluteEndYear.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTimeRangeAbsoluteEndYear.setStatus(_A)
_ZyTimeRangeAbsoluteEndMonth_Type=Integer32
_ZyTimeRangeAbsoluteEndMonth_Object=MibTableColumn
zyTimeRangeAbsoluteEndMonth=_ZyTimeRangeAbsoluteEndMonth_Object((1,3,6,1,4,1,890,1,15,3,98,1,3,1,7),_ZyTimeRangeAbsoluteEndMonth_Type())
zyTimeRangeAbsoluteEndMonth.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTimeRangeAbsoluteEndMonth.setStatus(_A)
_ZyTimeRangeAbsoluteEndDate_Type=Integer32
_ZyTimeRangeAbsoluteEndDate_Object=MibTableColumn
zyTimeRangeAbsoluteEndDate=_ZyTimeRangeAbsoluteEndDate_Object((1,3,6,1,4,1,890,1,15,3,98,1,3,1,8),_ZyTimeRangeAbsoluteEndDate_Type())
zyTimeRangeAbsoluteEndDate.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTimeRangeAbsoluteEndDate.setStatus(_A)
_ZyTimeRangeAbsoluteEndHour_Type=Integer32
_ZyTimeRangeAbsoluteEndHour_Object=MibTableColumn
zyTimeRangeAbsoluteEndHour=_ZyTimeRangeAbsoluteEndHour_Object((1,3,6,1,4,1,890,1,15,3,98,1,3,1,9),_ZyTimeRangeAbsoluteEndHour_Type())
zyTimeRangeAbsoluteEndHour.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTimeRangeAbsoluteEndHour.setStatus(_A)
_ZyTimeRangeAbsoluteEndMinute_Type=Integer32
_ZyTimeRangeAbsoluteEndMinute_Object=MibTableColumn
zyTimeRangeAbsoluteEndMinute=_ZyTimeRangeAbsoluteEndMinute_Object((1,3,6,1,4,1,890,1,15,3,98,1,3,1,10),_ZyTimeRangeAbsoluteEndMinute_Type())
zyTimeRangeAbsoluteEndMinute.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTimeRangeAbsoluteEndMinute.setStatus(_A)
_ZyxelTimeRangePeriodicTable_Object=MibTable
zyxelTimeRangePeriodicTable=_ZyxelTimeRangePeriodicTable_Object((1,3,6,1,4,1,890,1,15,3,98,1,4))
if mibBuilder.loadTexts:zyxelTimeRangePeriodicTable.setStatus(_A)
_ZyxelTimeRangePeriodicEntry_Object=MibTableRow
zyxelTimeRangePeriodicEntry=_ZyxelTimeRangePeriodicEntry_Object((1,3,6,1,4,1,890,1,15,3,98,1,4,1))
zyxelTimeRangePeriodicEntry.setIndexNames((0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:zyxelTimeRangePeriodicEntry.setStatus(_A)
class _ZyTimeRangePeriodicWeekDayList_Type(Bits):namedValues=NamedValues(*((_E,0),(_F,1),(_G,2),(_H,3),(_I,4),(_J,5),(_K,6)))
_ZyTimeRangePeriodicWeekDayList_Type.__name__='Bits'
_ZyTimeRangePeriodicWeekDayList_Object=MibTableColumn
zyTimeRangePeriodicWeekDayList=_ZyTimeRangePeriodicWeekDayList_Object((1,3,6,1,4,1,890,1,15,3,98,1,4,1,1),_ZyTimeRangePeriodicWeekDayList_Type())
zyTimeRangePeriodicWeekDayList.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTimeRangePeriodicWeekDayList.setStatus(_A)
class _ZyTimeRangePeriodicStartWeekDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',0),(_E,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6),(_K,7)))
_ZyTimeRangePeriodicStartWeekDay_Type.__name__=_D
_ZyTimeRangePeriodicStartWeekDay_Object=MibTableColumn
zyTimeRangePeriodicStartWeekDay=_ZyTimeRangePeriodicStartWeekDay_Object((1,3,6,1,4,1,890,1,15,3,98,1,4,1,2),_ZyTimeRangePeriodicStartWeekDay_Type())
zyTimeRangePeriodicStartWeekDay.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTimeRangePeriodicStartWeekDay.setStatus(_A)
_ZyTimeRangePeriodicStartHour_Type=Integer32
_ZyTimeRangePeriodicStartHour_Object=MibTableColumn
zyTimeRangePeriodicStartHour=_ZyTimeRangePeriodicStartHour_Object((1,3,6,1,4,1,890,1,15,3,98,1,4,1,3),_ZyTimeRangePeriodicStartHour_Type())
zyTimeRangePeriodicStartHour.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTimeRangePeriodicStartHour.setStatus(_A)
_ZyTimeRangePeriodicStartMinute_Type=Integer32
_ZyTimeRangePeriodicStartMinute_Object=MibTableColumn
zyTimeRangePeriodicStartMinute=_ZyTimeRangePeriodicStartMinute_Object((1,3,6,1,4,1,890,1,15,3,98,1,4,1,4),_ZyTimeRangePeriodicStartMinute_Type())
zyTimeRangePeriodicStartMinute.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTimeRangePeriodicStartMinute.setStatus(_A)
class _ZyTimeRangePeriodicEndWeekDay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('none',0),(_E,1),(_F,2),(_G,3),(_H,4),(_I,5),(_J,6),(_K,7)))
_ZyTimeRangePeriodicEndWeekDay_Type.__name__=_D
_ZyTimeRangePeriodicEndWeekDay_Object=MibTableColumn
zyTimeRangePeriodicEndWeekDay=_ZyTimeRangePeriodicEndWeekDay_Object((1,3,6,1,4,1,890,1,15,3,98,1,4,1,5),_ZyTimeRangePeriodicEndWeekDay_Type())
zyTimeRangePeriodicEndWeekDay.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTimeRangePeriodicEndWeekDay.setStatus(_A)
_ZyTimeRangePeriodicEndHour_Type=Integer32
_ZyTimeRangePeriodicEndHour_Object=MibTableColumn
zyTimeRangePeriodicEndHour=_ZyTimeRangePeriodicEndHour_Object((1,3,6,1,4,1,890,1,15,3,98,1,4,1,6),_ZyTimeRangePeriodicEndHour_Type())
zyTimeRangePeriodicEndHour.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTimeRangePeriodicEndHour.setStatus(_A)
_ZyTimeRangePeriodicEndMinute_Type=Integer32
_ZyTimeRangePeriodicEndMinute_Object=MibTableColumn
zyTimeRangePeriodicEndMinute=_ZyTimeRangePeriodicEndMinute_Object((1,3,6,1,4,1,890,1,15,3,98,1,4,1,7),_ZyTimeRangePeriodicEndMinute_Type())
zyTimeRangePeriodicEndMinute.setMaxAccess(_B)
if mibBuilder.loadTexts:zyTimeRangePeriodicEndMinute.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ZyTimeRangeWeekDayList':ZyTimeRangeWeekDayList,'zyxelTimeRange':zyxelTimeRange,'zyxelTimeRangeSetup':zyxelTimeRangeSetup,'zyTimeRangeMaxNumberOfProfiles':zyTimeRangeMaxNumberOfProfiles,'zyxelTimeRangeTable':zyxelTimeRangeTable,'zyxelTimeRangeEntry':zyxelTimeRangeEntry,_L:zyTimeRangeName,_M:zyTimeRangeType,'zyTimeRangeRowStatus':zyTimeRangeRowStatus,'zyxelTimeRangeAbsoluteTable':zyxelTimeRangeAbsoluteTable,'zyxelTimeRangeAbsoluteEntry':zyxelTimeRangeAbsoluteEntry,'zyTimeRangeAbsoluteStartYear':zyTimeRangeAbsoluteStartYear,'zyTimeRangeAbsoluteStartMonth':zyTimeRangeAbsoluteStartMonth,'zyTimeRangeAbsoluteStartDate':zyTimeRangeAbsoluteStartDate,'zyTimeRangeAbsoluteStartHour':zyTimeRangeAbsoluteStartHour,'zyTimeRangeAbsoluteStartMinute':zyTimeRangeAbsoluteStartMinute,'zyTimeRangeAbsoluteEndYear':zyTimeRangeAbsoluteEndYear,'zyTimeRangeAbsoluteEndMonth':zyTimeRangeAbsoluteEndMonth,'zyTimeRangeAbsoluteEndDate':zyTimeRangeAbsoluteEndDate,'zyTimeRangeAbsoluteEndHour':zyTimeRangeAbsoluteEndHour,'zyTimeRangeAbsoluteEndMinute':zyTimeRangeAbsoluteEndMinute,'zyxelTimeRangePeriodicTable':zyxelTimeRangePeriodicTable,'zyxelTimeRangePeriodicEntry':zyxelTimeRangePeriodicEntry,'zyTimeRangePeriodicWeekDayList':zyTimeRangePeriodicWeekDayList,'zyTimeRangePeriodicStartWeekDay':zyTimeRangePeriodicStartWeekDay,'zyTimeRangePeriodicStartHour':zyTimeRangePeriodicStartHour,'zyTimeRangePeriodicStartMinute':zyTimeRangePeriodicStartMinute,'zyTimeRangePeriodicEndWeekDay':zyTimeRangePeriodicEndWeekDay,'zyTimeRangePeriodicEndHour':zyTimeRangePeriodicEndHour,'zyTimeRangePeriodicEndMinute':zyTimeRangePeriodicEndMinute})