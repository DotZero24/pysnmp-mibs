_J='mitelCs2000AlmNbrCategories'
_I='mitelCs2000AlmDetectDate'
_H='mitelCs2000AlmLevel'
_G='mitelCs2000SysName'
_F='mitelCs2000CatTblIndex'
_E='NotificationType'
_D='Integer32'
_C='MITEL-SX2000-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mitelAppCallServer,mitelConfAgents,mitelConfCompliances,mitelGrpCs2000,mitelIdCs2000Light=mibBuilder.importSymbols('MITEL-MIB','mitelAppCallServer','mitelConfAgents','mitelConfCompliances','mitelGrpCs2000','mitelIdCs2000Light')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_E,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_E,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class Integer32(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
class DateAndTime(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8),ValueSizeConstraint(11,11))
class MitelCs2000AlarmLevelType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('almClear',1),('almMinor',2),('almMajor',3),('almCritical',4)))
_MitelAppCs2000_ObjectIdentity=ObjectIdentity
mitelAppCs2000=_MitelAppCs2000_ObjectIdentity((1,3,6,1,4,1,1027,4,1,1,1))
_MitelCs2000System_ObjectIdentity=ObjectIdentity
mitelCs2000System=_MitelCs2000System_ObjectIdentity((1,3,6,1,4,1,1027,4,1,1,1,1))
_MitelCs2000SysName_Type=DisplayString
_MitelCs2000SysName_Object=MibScalar
mitelCs2000SysName=_MitelCs2000SysName_Object((1,3,6,1,4,1,1027,4,1,1,1,1,1),_MitelCs2000SysName_Type())
mitelCs2000SysName.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelCs2000SysName.setStatus(_A)
_MitelCs2000Alarms_ObjectIdentity=ObjectIdentity
mitelCs2000Alarms=_MitelCs2000Alarms_ObjectIdentity((1,3,6,1,4,1,1027,4,1,1,1,2))
_MitelCs2000AlmLevel_Type=MitelCs2000AlarmLevelType
_MitelCs2000AlmLevel_Object=MibScalar
mitelCs2000AlmLevel=_MitelCs2000AlmLevel_Object((1,3,6,1,4,1,1027,4,1,1,1,2,1),_MitelCs2000AlmLevel_Type())
mitelCs2000AlmLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelCs2000AlmLevel.setStatus(_A)
_MitelCs2000AlmDetectDate_Type=DateAndTime
_MitelCs2000AlmDetectDate_Object=MibScalar
mitelCs2000AlmDetectDate=_MitelCs2000AlmDetectDate_Object((1,3,6,1,4,1,1027,4,1,1,1,2,2),_MitelCs2000AlmDetectDate_Type())
mitelCs2000AlmDetectDate.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelCs2000AlmDetectDate.setStatus(_A)
_MitelCs2000AlmNbrCategories_Type=Integer32
_MitelCs2000AlmNbrCategories_Object=MibScalar
mitelCs2000AlmNbrCategories=_MitelCs2000AlmNbrCategories_Object((1,3,6,1,4,1,1027,4,1,1,1,2,3),_MitelCs2000AlmNbrCategories_Type())
mitelCs2000AlmNbrCategories.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelCs2000AlmNbrCategories.setStatus(_A)
_MitelCs2000CategoryTable_Object=MibTable
mitelCs2000CategoryTable=_MitelCs2000CategoryTable_Object((1,3,6,1,4,1,1027,4,1,1,1,2,4))
if mibBuilder.loadTexts:mitelCs2000CategoryTable.setStatus(_A)
_MitelCs2000CategoryTableEntry_Object=MibTableRow
mitelCs2000CategoryTableEntry=_MitelCs2000CategoryTableEntry_Object((1,3,6,1,4,1,1027,4,1,1,1,2,4,1))
mitelCs2000CategoryTableEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:mitelCs2000CategoryTableEntry.setStatus(_A)
_MitelCs2000CatTblIndex_Type=Integer32
_MitelCs2000CatTblIndex_Object=MibTableColumn
mitelCs2000CatTblIndex=_MitelCs2000CatTblIndex_Object((1,3,6,1,4,1,1027,4,1,1,1,2,4,1,1),_MitelCs2000CatTblIndex_Type())
mitelCs2000CatTblIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelCs2000CatTblIndex.setStatus(_A)
_MitelCs2000CatTblAvailable_Type=Integer32
_MitelCs2000CatTblAvailable_Object=MibTableColumn
mitelCs2000CatTblAvailable=_MitelCs2000CatTblAvailable_Object((1,3,6,1,4,1,1027,4,1,1,1,2,4,1,2),_MitelCs2000CatTblAvailable_Type())
mitelCs2000CatTblAvailable.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelCs2000CatTblAvailable.setStatus(_A)
_MitelCs2000CatTblUnavailable_Type=Integer32
_MitelCs2000CatTblUnavailable_Object=MibTableColumn
mitelCs2000CatTblUnavailable=_MitelCs2000CatTblUnavailable_Object((1,3,6,1,4,1,1027,4,1,1,1,2,4,1,3),_MitelCs2000CatTblUnavailable_Type())
mitelCs2000CatTblUnavailable.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelCs2000CatTblUnavailable.setStatus(_A)
_MitelCs2000CatTblLevel_Type=MitelCs2000AlarmLevelType
_MitelCs2000CatTblLevel_Object=MibTableColumn
mitelCs2000CatTblLevel=_MitelCs2000CatTblLevel_Object((1,3,6,1,4,1,1027,4,1,1,1,2,4,1,4),_MitelCs2000CatTblLevel_Type())
mitelCs2000CatTblLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelCs2000CatTblLevel.setStatus(_A)
_MitelCs2000CatTblMinorThresh_Type=Integer32
_MitelCs2000CatTblMinorThresh_Object=MibTableColumn
mitelCs2000CatTblMinorThresh=_MitelCs2000CatTblMinorThresh_Object((1,3,6,1,4,1,1027,4,1,1,1,2,4,1,5),_MitelCs2000CatTblMinorThresh_Type())
mitelCs2000CatTblMinorThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelCs2000CatTblMinorThresh.setStatus(_A)
_MitelCs2000CatTblMajorThresh_Type=Integer32
_MitelCs2000CatTblMajorThresh_Object=MibTableColumn
mitelCs2000CatTblMajorThresh=_MitelCs2000CatTblMajorThresh_Object((1,3,6,1,4,1,1027,4,1,1,1,2,4,1,6),_MitelCs2000CatTblMajorThresh_Type())
mitelCs2000CatTblMajorThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelCs2000CatTblMajorThresh.setStatus(_A)
_MitelCs2000CatTblCriticalThresh_Type=Integer32
_MitelCs2000CatTblCriticalThresh_Object=MibTableColumn
mitelCs2000CatTblCriticalThresh=_MitelCs2000CatTblCriticalThresh_Object((1,3,6,1,4,1,1027,4,1,1,1,2,4,1,7),_MitelCs2000CatTblCriticalThresh_Type())
mitelCs2000CatTblCriticalThresh.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelCs2000CatTblCriticalThresh.setStatus(_A)
_MitelCs2000CatTblName_Type=DisplayString
_MitelCs2000CatTblName_Object=MibTableColumn
mitelCs2000CatTblName=_MitelCs2000CatTblName_Object((1,3,6,1,4,1,1027,4,1,1,1,2,4,1,8),_MitelCs2000CatTblName_Type())
mitelCs2000CatTblName.setMaxAccess(_B)
if mibBuilder.loadTexts:mitelCs2000CatTblName.setStatus(_A)
_MitelCs2000Notifications_ObjectIdentity=ObjectIdentity
mitelCs2000Notifications=_MitelCs2000Notifications_ObjectIdentity((1,3,6,1,4,1,1027,4,1,1,1,3))
_MitelComplCs2000_ObjectIdentity=ObjectIdentity
mitelComplCs2000=_MitelComplCs2000_ObjectIdentity((1,3,6,1,4,1,1027,5,1,4))
_MitelGrpCs2000System_ObjectIdentity=ObjectIdentity
mitelGrpCs2000System=_MitelGrpCs2000System_ObjectIdentity((1,3,6,1,4,1,1027,5,2,3,1))
_MitelGrpCs2000Alarms_ObjectIdentity=ObjectIdentity
mitelGrpCs2000Alarms=_MitelGrpCs2000Alarms_ObjectIdentity((1,3,6,1,4,1,1027,5,2,3,2))
_MitelAgentCs2000_ObjectIdentity=ObjectIdentity
mitelAgentCs2000=_MitelAgentCs2000_ObjectIdentity((1,3,6,1,4,1,1027,5,3,2))
mitelCs2000NotifAlarm=NotificationType((1,3,6,1,4,1,1027,1,2,2,0,201))
mitelCs2000NotifAlarm.setObjects(*((_C,_G),(_C,_H),(_C,_I),(_C,_J)))
if mibBuilder.loadTexts:mitelCs2000NotifAlarm.setStatus('')
mibBuilder.exportSymbols(_C,**{_D:Integer32,'DateAndTime':DateAndTime,'MitelCs2000AlarmLevelType':MitelCs2000AlarmLevelType,'mitelCs2000NotifAlarm':mitelCs2000NotifAlarm,'mitelAppCs2000':mitelAppCs2000,'mitelCs2000System':mitelCs2000System,_G:mitelCs2000SysName,'mitelCs2000Alarms':mitelCs2000Alarms,_H:mitelCs2000AlmLevel,_I:mitelCs2000AlmDetectDate,_J:mitelCs2000AlmNbrCategories,'mitelCs2000CategoryTable':mitelCs2000CategoryTable,'mitelCs2000CategoryTableEntry':mitelCs2000CategoryTableEntry,_F:mitelCs2000CatTblIndex,'mitelCs2000CatTblAvailable':mitelCs2000CatTblAvailable,'mitelCs2000CatTblUnavailable':mitelCs2000CatTblUnavailable,'mitelCs2000CatTblLevel':mitelCs2000CatTblLevel,'mitelCs2000CatTblMinorThresh':mitelCs2000CatTblMinorThresh,'mitelCs2000CatTblMajorThresh':mitelCs2000CatTblMajorThresh,'mitelCs2000CatTblCriticalThresh':mitelCs2000CatTblCriticalThresh,'mitelCs2000CatTblName':mitelCs2000CatTblName,'mitelCs2000Notifications':mitelCs2000Notifications,'mitelComplCs2000':mitelComplCs2000,'mitelGrpCs2000System':mitelGrpCs2000System,'mitelGrpCs2000Alarms':mitelGrpCs2000Alarms,'mitelAgentCs2000':mitelAgentCs2000})