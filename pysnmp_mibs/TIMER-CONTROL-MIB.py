_Q='timerCtrlSchdlRowStatus'
_P='timerCtrlSchdlDateStop'
_O='timerCtrlSchdlDateStart'
_N='timerCtrlSchdlTimeStop'
_M='timerCtrlSchdlTimeStart'
_L='timerCtrlSchdlMonthDayAcc'
_K='timerCtrlSchdlWeekDay'
_J='timerCtrlSchdlMonthFreq'
_I='timerCtrlSchdlRecurring'
_H='timerCtrlSchdlName'
_G='timerCtrlGlobalMode'
_F='timerCtrlSchdlIndex'
_E='SnmpAdminString'
_D='Integer32'
_C='read-create'
_B='TIMER-CONTROL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ng700smartswitch,=mibBuilder.importSymbols('NETGEAR-REF-MIB','ng700smartswitch')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
timerControl=ModuleIdentity((1,3,6,1,4,1,4526,11,1025))
if mibBuilder.loadTexts:timerControl.setRevisions(('2009-12-02 00:00',))
class TimeHoursMinutes(TextualConvention,OctetString):status=_A;displayHint='1d:1d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
class DateYearMonthDay(TextualConvention,OctetString):status=_A;displayHint='2d-1d-1d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_TimerCtrlObjects_ObjectIdentity=ObjectIdentity
timerCtrlObjects=_TimerCtrlObjects_ObjectIdentity((1,3,6,1,4,1,4526,11,1025,1))
_TimerCtrlModeGroup_ObjectIdentity=ObjectIdentity
timerCtrlModeGroup=_TimerCtrlModeGroup_ObjectIdentity((1,3,6,1,4,1,4526,11,1025,1,1))
class _TimerCtrlGlobalMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_TimerCtrlGlobalMode_Type.__name__=_D
_TimerCtrlGlobalMode_Object=MibScalar
timerCtrlGlobalMode=_TimerCtrlGlobalMode_Object((1,3,6,1,4,1,4526,11,1025,1,1,1),_TimerCtrlGlobalMode_Type())
timerCtrlGlobalMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:timerCtrlGlobalMode.setStatus(_A)
_TimerCtrlSchdlTable_Object=MibTable
timerCtrlSchdlTable=_TimerCtrlSchdlTable_Object((1,3,6,1,4,1,4526,11,1025,1,2))
if mibBuilder.loadTexts:timerCtrlSchdlTable.setStatus(_A)
_TimerCtrlSchdlEntry_Object=MibTableRow
timerCtrlSchdlEntry=_TimerCtrlSchdlEntry_Object((1,3,6,1,4,1,4526,11,1025,1,2,1))
timerCtrlSchdlEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:timerCtrlSchdlEntry.setStatus(_A)
class _TimerCtrlSchdlIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_TimerCtrlSchdlIndex_Type.__name__=_D
_TimerCtrlSchdlIndex_Object=MibTableColumn
timerCtrlSchdlIndex=_TimerCtrlSchdlIndex_Object((1,3,6,1,4,1,4526,11,1025,1,2,1,1),_TimerCtrlSchdlIndex_Type())
timerCtrlSchdlIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:timerCtrlSchdlIndex.setStatus(_A)
class _TimerCtrlSchdlName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_TimerCtrlSchdlName_Type.__name__=_E
_TimerCtrlSchdlName_Object=MibTableColumn
timerCtrlSchdlName=_TimerCtrlSchdlName_Object((1,3,6,1,4,1,4526,11,1025,1,2,1,2),_TimerCtrlSchdlName_Type())
timerCtrlSchdlName.setMaxAccess(_C)
if mibBuilder.loadTexts:timerCtrlSchdlName.setStatus(_A)
class _TimerCtrlSchdlRecurring_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('invalid',0),('daily',1),('weekly',2),('monthly',3),('yearly',4)))
_TimerCtrlSchdlRecurring_Type.__name__=_D
_TimerCtrlSchdlRecurring_Object=MibTableColumn
timerCtrlSchdlRecurring=_TimerCtrlSchdlRecurring_Object((1,3,6,1,4,1,4526,11,1025,1,2,1,3),_TimerCtrlSchdlRecurring_Type())
timerCtrlSchdlRecurring.setMaxAccess(_C)
if mibBuilder.loadTexts:timerCtrlSchdlRecurring.setStatus(_A)
class _TimerCtrlSchdlMonthFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('january',0),('february',1),('march',2),('april',3),('may',4),('june',5),('july',6),('august',7),('september',8),('october',9),('november',10),('december',11)))
_TimerCtrlSchdlMonthFreq_Type.__name__=_D
_TimerCtrlSchdlMonthFreq_Object=MibTableColumn
timerCtrlSchdlMonthFreq=_TimerCtrlSchdlMonthFreq_Object((1,3,6,1,4,1,4526,11,1025,1,2,1,4),_TimerCtrlSchdlMonthFreq_Type())
timerCtrlSchdlMonthFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:timerCtrlSchdlMonthFreq.setStatus(_A)
class _TimerCtrlSchdlWeekDay_Type(Bits):namedValues=NamedValues(*(('sunday',0),('monday',1),('tuesday',2),('wednesday',3),('thursday',4),('friday',5),('saturday',6)))
_TimerCtrlSchdlWeekDay_Type.__name__='Bits'
_TimerCtrlSchdlWeekDay_Object=MibTableColumn
timerCtrlSchdlWeekDay=_TimerCtrlSchdlWeekDay_Object((1,3,6,1,4,1,4526,11,1025,1,2,1,5),_TimerCtrlSchdlWeekDay_Type())
timerCtrlSchdlWeekDay.setMaxAccess(_C)
if mibBuilder.loadTexts:timerCtrlSchdlWeekDay.setStatus(_A)
class _TimerCtrlSchdlMonthDayAcc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,37))
_TimerCtrlSchdlMonthDayAcc_Type.__name__=_D
_TimerCtrlSchdlMonthDayAcc_Object=MibTableColumn
timerCtrlSchdlMonthDayAcc=_TimerCtrlSchdlMonthDayAcc_Object((1,3,6,1,4,1,4526,11,1025,1,2,1,6),_TimerCtrlSchdlMonthDayAcc_Type())
timerCtrlSchdlMonthDayAcc.setMaxAccess(_C)
if mibBuilder.loadTexts:timerCtrlSchdlMonthDayAcc.setStatus(_A)
_TimerCtrlSchdlTimeStart_Type=TimeHoursMinutes
_TimerCtrlSchdlTimeStart_Object=MibTableColumn
timerCtrlSchdlTimeStart=_TimerCtrlSchdlTimeStart_Object((1,3,6,1,4,1,4526,11,1025,1,2,1,7),_TimerCtrlSchdlTimeStart_Type())
timerCtrlSchdlTimeStart.setMaxAccess(_C)
if mibBuilder.loadTexts:timerCtrlSchdlTimeStart.setStatus(_A)
_TimerCtrlSchdlTimeStop_Type=TimeHoursMinutes
_TimerCtrlSchdlTimeStop_Object=MibTableColumn
timerCtrlSchdlTimeStop=_TimerCtrlSchdlTimeStop_Object((1,3,6,1,4,1,4526,11,1025,1,2,1,8),_TimerCtrlSchdlTimeStop_Type())
timerCtrlSchdlTimeStop.setMaxAccess(_C)
if mibBuilder.loadTexts:timerCtrlSchdlTimeStop.setStatus(_A)
_TimerCtrlSchdlDateStart_Type=DateYearMonthDay
_TimerCtrlSchdlDateStart_Object=MibTableColumn
timerCtrlSchdlDateStart=_TimerCtrlSchdlDateStart_Object((1,3,6,1,4,1,4526,11,1025,1,2,1,9),_TimerCtrlSchdlDateStart_Type())
timerCtrlSchdlDateStart.setMaxAccess(_C)
if mibBuilder.loadTexts:timerCtrlSchdlDateStart.setStatus(_A)
_TimerCtrlSchdlDateStop_Type=DateYearMonthDay
_TimerCtrlSchdlDateStop_Object=MibTableColumn
timerCtrlSchdlDateStop=_TimerCtrlSchdlDateStop_Object((1,3,6,1,4,1,4526,11,1025,1,2,1,10),_TimerCtrlSchdlDateStop_Type())
timerCtrlSchdlDateStop.setMaxAccess(_C)
if mibBuilder.loadTexts:timerCtrlSchdlDateStop.setStatus(_A)
_TimerCtrlSchdlRowStatus_Type=RowStatus
_TimerCtrlSchdlRowStatus_Object=MibTableColumn
timerCtrlSchdlRowStatus=_TimerCtrlSchdlRowStatus_Object((1,3,6,1,4,1,4526,11,1025,1,2,1,11),_TimerCtrlSchdlRowStatus_Type())
timerCtrlSchdlRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:timerCtrlSchdlRowStatus.setStatus(_A)
timerCtrlGroup=ObjectGroup((1,3,6,1,4,1,4526,11,1025,1,3))
timerCtrlGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:timerCtrlGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'TimeHoursMinutes':TimeHoursMinutes,'DateYearMonthDay':DateYearMonthDay,'timerControl':timerControl,'timerCtrlObjects':timerCtrlObjects,'timerCtrlModeGroup':timerCtrlModeGroup,_G:timerCtrlGlobalMode,'timerCtrlSchdlTable':timerCtrlSchdlTable,'timerCtrlSchdlEntry':timerCtrlSchdlEntry,_F:timerCtrlSchdlIndex,_H:timerCtrlSchdlName,_I:timerCtrlSchdlRecurring,_J:timerCtrlSchdlMonthFreq,_K:timerCtrlSchdlWeekDay,_L:timerCtrlSchdlMonthDayAcc,_M:timerCtrlSchdlTimeStart,_N:timerCtrlSchdlTimeStop,_O:timerCtrlSchdlDateStart,_P:timerCtrlSchdlDateStop,_Q:timerCtrlSchdlRowStatus,'timerCtrlGroup':timerCtrlGroup})