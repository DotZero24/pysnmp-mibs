_g='hpicfJobSchedulerGroup3'
_f='hpicfJobSchedulerGroup2'
_e='hpicfJobSchedulerGroup1'
_d='hpicfJobSchedulerGroup'
_c='hpicfJobSchedulerSkipCount'
_b='hpicfJobSchedulerName'
_a='DisplayString'
_Z='Integer32'
_Y='hpicfJobSchedulerLastRunTime'
_X='hpicfJobSchedulerRunningStatus'
_W='OctetString'
_V='hpicfJobSchedulerStatus'
_U='hpicfJobSchedulerCount'
_T='hpicfJobSchedulerDelay'
_S='Unsigned32'
_R='hpicfJobSchedulerCalendarMinute'
_Q='hpicfJobSchedulerCalendarHour'
_P='hpicfJobSchedulerCalendarDayOfWeek'
_O='hpicfJobSchedulerCalendarDayOfMonth'
_N='hpicfJobSchedulerCalendarMonth'
_M='hpicfJobSchedulerEvent'
_L='hpicfJobSchedulerLastOutput'
_K='hpicfJobSchedulerErrorCount'
_J='hpicfJobSchedulerRunCount'
_I='hpicfJobSchedulerConfigSave'
_H='hpicfJobSchedulerCommand'
_G='hpicfJobSchedulerRowStatus'
_F='deprecated'
_E='read-only'
_D='Bits'
_C='read-write'
_B='current'
_A='HP-ICF-JOB-SCHEDULER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_W,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_D,'Counter32','Counter64','Gauge32',_Z,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_S,'iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_a,'PhysAddress','RowStatus','TextualConvention','TruthValue')
hpicfJobSchedulerMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,105))
if mibBuilder.loadTexts:hpicfJobSchedulerMIB.setRevisions(('2016-05-04 00:00','2016-04-19 00:00','2015-08-27 00:00','2015-05-13 00:00','2013-10-05 00:00'))
_HpicfJobSchedulerObjects_ObjectIdentity=ObjectIdentity
hpicfJobSchedulerObjects=_HpicfJobSchedulerObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,105,1))
_HpicfJobSchedulerTable_Object=MibTable
hpicfJobSchedulerTable=_HpicfJobSchedulerTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,105,1,1))
if mibBuilder.loadTexts:hpicfJobSchedulerTable.setStatus(_B)
_HpicfJobSchedulerEntry_Object=MibTableRow
hpicfJobSchedulerEntry=_HpicfJobSchedulerEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,105,1,1,1))
hpicfJobSchedulerEntry.setIndexNames((0,_A,_b))
if mibBuilder.loadTexts:hpicfJobSchedulerEntry.setStatus(_B)
class _HpicfJobSchedulerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_HpicfJobSchedulerName_Type.__name__=_a
_HpicfJobSchedulerName_Object=MibTableColumn
hpicfJobSchedulerName=_HpicfJobSchedulerName_Object((1,3,6,1,4,1,11,2,14,11,5,1,105,1,1,1,1),_HpicfJobSchedulerName_Type())
hpicfJobSchedulerName.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpicfJobSchedulerName.setStatus(_B)
_HpicfJobSchedulerRowStatus_Type=RowStatus
_HpicfJobSchedulerRowStatus_Object=MibTableColumn
hpicfJobSchedulerRowStatus=_HpicfJobSchedulerRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,105,1,1,1,2),_HpicfJobSchedulerRowStatus_Type())
hpicfJobSchedulerRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:hpicfJobSchedulerRowStatus.setStatus(_B)
class _HpicfJobSchedulerCommand_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpicfJobSchedulerCommand_Type.__name__=_W
_HpicfJobSchedulerCommand_Object=MibTableColumn
hpicfJobSchedulerCommand=_HpicfJobSchedulerCommand_Object((1,3,6,1,4,1,11,2,14,11,5,1,105,1,1,1,3),_HpicfJobSchedulerCommand_Type())
hpicfJobSchedulerCommand.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfJobSchedulerCommand.setStatus(_B)
_HpicfJobSchedulerConfigSave_Type=TruthValue
_HpicfJobSchedulerConfigSave_Object=MibTableColumn
hpicfJobSchedulerConfigSave=_HpicfJobSchedulerConfigSave_Object((1,3,6,1,4,1,11,2,14,11,5,1,105,1,1,1,4),_HpicfJobSchedulerConfigSave_Type())
hpicfJobSchedulerConfigSave.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfJobSchedulerConfigSave.setStatus(_B)
_HpicfJobSchedulerRunCount_Type=Unsigned32
_HpicfJobSchedulerRunCount_Object=MibTableColumn
hpicfJobSchedulerRunCount=_HpicfJobSchedulerRunCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,105,1,1,1,5),_HpicfJobSchedulerRunCount_Type())
hpicfJobSchedulerRunCount.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfJobSchedulerRunCount.setStatus(_B)
_HpicfJobSchedulerErrorCount_Type=Unsigned32
_HpicfJobSchedulerErrorCount_Object=MibTableColumn
hpicfJobSchedulerErrorCount=_HpicfJobSchedulerErrorCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,105,1,1,1,6),_HpicfJobSchedulerErrorCount_Type())
hpicfJobSchedulerErrorCount.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfJobSchedulerErrorCount.setStatus(_B)
class _HpicfJobSchedulerLastOutput_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpicfJobSchedulerLastOutput_Type.__name__=_W
_HpicfJobSchedulerLastOutput_Object=MibTableColumn
hpicfJobSchedulerLastOutput=_HpicfJobSchedulerLastOutput_Object((1,3,6,1,4,1,11,2,14,11,5,1,105,1,1,1,7),_HpicfJobSchedulerLastOutput_Type())
hpicfJobSchedulerLastOutput.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfJobSchedulerLastOutput.setStatus(_B)
class _HpicfJobSchedulerEvent_Type(Bits):namedValues=NamedValues(*(('reboot',0),('failover',1)))
_HpicfJobSchedulerEvent_Type.__name__=_D
_HpicfJobSchedulerEvent_Object=MibTableColumn
hpicfJobSchedulerEvent=_HpicfJobSchedulerEvent_Object((1,3,6,1,4,1,11,2,14,11,5,1,105,1,1,1,8),_HpicfJobSchedulerEvent_Type())
hpicfJobSchedulerEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfJobSchedulerEvent.setStatus(_B)
class _HpicfJobSchedulerCalendarMonth_Type(Bits):namedValues=NamedValues(*(('january',0),('february',1),('march',2),('april',3),('may',4),('june',5),('july',6),('august',7),('september',8),('october',9),('november',10),('december',11)))
_HpicfJobSchedulerCalendarMonth_Type.__name__=_D
_HpicfJobSchedulerCalendarMonth_Object=MibTableColumn
hpicfJobSchedulerCalendarMonth=_HpicfJobSchedulerCalendarMonth_Object((1,3,6,1,4,1,11,2,14,11,5,1,105,1,1,1,9),_HpicfJobSchedulerCalendarMonth_Type())
hpicfJobSchedulerCalendarMonth.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfJobSchedulerCalendarMonth.setStatus(_B)
class _HpicfJobSchedulerCalendarDayOfMonth_Type(Bits):namedValues=NamedValues(*(('d1',0),('d2',1),('d3',2),('d4',3),('d5',4),('d6',5),('d7',6),('d8',7),('d9',8),('d10',9),('d11',10),('d12',11),('d13',12),('d14',13),('d15',14),('d16',15),('d17',16),('d18',17),('d19',18),('d20',19),('d21',20),('d22',21),('d23',22),('d24',23),('d25',24),('d26',25),('d27',26),('d28',27),('d29',28),('d30',29),('d31',30),('r1',31),('r2',32),('r3',33),('r4',34),('r5',35),('r6',36),('r7',37),('r8',38),('r9',39),('r10',40),('r11',41),('r12',42),('r13',43),('r14',44),('r15',45),('r16',46),('r17',47),('r18',48),('r19',49),('r20',50),('r21',51),('r22',52),('r23',53),('r24',54),('r25',55),('r26',56),('r27',57),('r28',58),('r29',59),('r30',60),('r31',61)))
_HpicfJobSchedulerCalendarDayOfMonth_Type.__name__=_D
_HpicfJobSchedulerCalendarDayOfMonth_Object=MibTableColumn
hpicfJobSchedulerCalendarDayOfMonth=_HpicfJobSchedulerCalendarDayOfMonth_Object((1,3,6,1,4,1,11,2,14,11,5,1,105,1,1,1,10),_HpicfJobSchedulerCalendarDayOfMonth_Type())
hpicfJobSchedulerCalendarDayOfMonth.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfJobSchedulerCalendarDayOfMonth.setStatus(_B)
class _HpicfJobSchedulerCalendarDayOfWeek_Type(Bits):namedValues=NamedValues(*(('sunday',0),('monday',1),('tuesday',2),('wednesday',3),('thursday',4),('friday',5),('saturday',6)))
_HpicfJobSchedulerCalendarDayOfWeek_Type.__name__=_D
_HpicfJobSchedulerCalendarDayOfWeek_Object=MibTableColumn
hpicfJobSchedulerCalendarDayOfWeek=_HpicfJobSchedulerCalendarDayOfWeek_Object((1,3,6,1,4,1,11,2,14,11,5,1,105,1,1,1,11),_HpicfJobSchedulerCalendarDayOfWeek_Type())
hpicfJobSchedulerCalendarDayOfWeek.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfJobSchedulerCalendarDayOfWeek.setStatus(_B)
class _HpicfJobSchedulerCalendarHour_Type(Bits):namedValues=NamedValues(*(('h0',0),('h1',1),('h2',2),('h3',3),('h4',4),('h5',5),('h6',6),('h7',7),('h8',8),('h9',9),('h10',10),('h11',11),('h12',12),('h13',13),('h14',14),('h15',15),('h16',16),('h17',17),('h18',18),('h19',19),('h20',20),('h21',21),('h22',22),('h23',23)))
_HpicfJobSchedulerCalendarHour_Type.__name__=_D
_HpicfJobSchedulerCalendarHour_Object=MibTableColumn
hpicfJobSchedulerCalendarHour=_HpicfJobSchedulerCalendarHour_Object((1,3,6,1,4,1,11,2,14,11,5,1,105,1,1,1,12),_HpicfJobSchedulerCalendarHour_Type())
hpicfJobSchedulerCalendarHour.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfJobSchedulerCalendarHour.setStatus(_B)
class _HpicfJobSchedulerCalendarMinute_Type(Bits):namedValues=NamedValues(*(('m0',0),('m1',1),('m2',2),('m3',3),('m4',4),('m5',5),('m6',6),('m7',7),('m8',8),('m9',9),('m10',10),('m11',11),('m12',12),('m13',13),('m14',14),('m15',15),('m16',16),('m17',17),('m18',18),('m19',19),('m20',20),('m21',21),('m22',22),('m23',23),('m24',24),('m25',25),('m26',26),('m27',27),('m28',28),('m29',29),('m30',30),('m31',31),('m32',32),('m33',33),('m34',34),('m35',35),('m36',36),('m37',37),('m38',38),('m39',39),('m40',40),('m41',41),('m42',42),('m43',43),('m44',44),('m45',45),('m46',46),('m47',47),('m48',48),('m49',49),('m50',50),('m51',51),('m52',52),('m53',53),('m54',54),('m55',55),('m56',56),('m57',57),('m58',58),('m59',59)))
_HpicfJobSchedulerCalendarMinute_Type.__name__=_D
_HpicfJobSchedulerCalendarMinute_Object=MibTableColumn
hpicfJobSchedulerCalendarMinute=_HpicfJobSchedulerCalendarMinute_Object((1,3,6,1,4,1,11,2,14,11,5,1,105,1,1,1,13),_HpicfJobSchedulerCalendarMinute_Type())
hpicfJobSchedulerCalendarMinute.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfJobSchedulerCalendarMinute.setStatus(_B)
class _HpicfJobSchedulerDelay_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,527039))
_HpicfJobSchedulerDelay_Type.__name__=_S
_HpicfJobSchedulerDelay_Object=MibTableColumn
hpicfJobSchedulerDelay=_HpicfJobSchedulerDelay_Object((1,3,6,1,4,1,11,2,14,11,5,1,105,1,1,1,14),_HpicfJobSchedulerDelay_Type())
hpicfJobSchedulerDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfJobSchedulerDelay.setStatus(_B)
if mibBuilder.loadTexts:hpicfJobSchedulerDelay.setUnits('minutes')
class _HpicfJobSchedulerCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_HpicfJobSchedulerCount_Type.__name__=_S
_HpicfJobSchedulerCount_Object=MibTableColumn
hpicfJobSchedulerCount=_HpicfJobSchedulerCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,105,1,1,1,15),_HpicfJobSchedulerCount_Type())
hpicfJobSchedulerCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfJobSchedulerCount.setStatus(_B)
_HpicfJobSchedulerStatus_Type=TruthValue
_HpicfJobSchedulerStatus_Object=MibTableColumn
hpicfJobSchedulerStatus=_HpicfJobSchedulerStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,105,1,1,1,16),_HpicfJobSchedulerStatus_Type())
hpicfJobSchedulerStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfJobSchedulerStatus.setStatus(_B)
class _HpicfJobSchedulerRunningStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('active',1),('inactive',2),('expired',3)))
_HpicfJobSchedulerRunningStatus_Type.__name__=_Z
_HpicfJobSchedulerRunningStatus_Object=MibTableColumn
hpicfJobSchedulerRunningStatus=_HpicfJobSchedulerRunningStatus_Object((1,3,6,1,4,1,11,2,14,11,5,1,105,1,1,1,17),_HpicfJobSchedulerRunningStatus_Type())
hpicfJobSchedulerRunningStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfJobSchedulerRunningStatus.setStatus(_B)
_HpicfJobSchedulerLastRunTime_Type=DateAndTime
_HpicfJobSchedulerLastRunTime_Object=MibTableColumn
hpicfJobSchedulerLastRunTime=_HpicfJobSchedulerLastRunTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,105,1,1,1,18),_HpicfJobSchedulerLastRunTime_Type())
hpicfJobSchedulerLastRunTime.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfJobSchedulerLastRunTime.setStatus(_B)
class _HpicfJobSchedulerSkipCount_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_HpicfJobSchedulerSkipCount_Type.__name__=_S
_HpicfJobSchedulerSkipCount_Object=MibTableColumn
hpicfJobSchedulerSkipCount=_HpicfJobSchedulerSkipCount_Object((1,3,6,1,4,1,11,2,14,11,5,1,105,1,1,1,19),_HpicfJobSchedulerSkipCount_Type())
hpicfJobSchedulerSkipCount.setMaxAccess(_E)
if mibBuilder.loadTexts:hpicfJobSchedulerSkipCount.setStatus(_B)
_HpicfJobSchedulerConformance_ObjectIdentity=ObjectIdentity
hpicfJobSchedulerConformance=_HpicfJobSchedulerConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,105,2))
_HpicfJobSchedulerMIBCompliances_ObjectIdentity=ObjectIdentity
hpicfJobSchedulerMIBCompliances=_HpicfJobSchedulerMIBCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,105,2,1))
_HpicfJobSchedulerMIBGroups_ObjectIdentity=ObjectIdentity
hpicfJobSchedulerMIBGroups=_HpicfJobSchedulerMIBGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,105,2,2))
hpicfJobSchedulerGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,105,2,2,1))
hpicfJobSchedulerGroup.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:hpicfJobSchedulerGroup.setStatus(_F)
hpicfJobSchedulerGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,105,2,2,2))
hpicfJobSchedulerGroup1.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_T),(_A,_U),(_A,_V)))
if mibBuilder.loadTexts:hpicfJobSchedulerGroup1.setStatus(_F)
hpicfJobSchedulerGroup2=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,105,2,2,3))
hpicfJobSchedulerGroup2.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_T),(_A,_U),(_A,_V),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:hpicfJobSchedulerGroup2.setStatus(_F)
hpicfJobSchedulerGroup3=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,105,2,2,4))
hpicfJobSchedulerGroup3.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_T),(_A,_U),(_A,_V),(_A,_X),(_A,_Y),(_A,_c)))
if mibBuilder.loadTexts:hpicfJobSchedulerGroup3.setStatus(_B)
hpicfJobSchedulerMIBCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,105,2,1,1))
hpicfJobSchedulerMIBCompliance.setObjects((_A,_d))
if mibBuilder.loadTexts:hpicfJobSchedulerMIBCompliance.setStatus(_F)
hpicfJobSchedulerMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,105,2,1,2))
hpicfJobSchedulerMIBCompliance1.setObjects((_A,_e))
if mibBuilder.loadTexts:hpicfJobSchedulerMIBCompliance1.setStatus(_F)
hpicfJobSchedulerMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,105,2,1,3))
hpicfJobSchedulerMIBCompliance2.setObjects((_A,_f))
if mibBuilder.loadTexts:hpicfJobSchedulerMIBCompliance2.setStatus(_F)
hpicfJobSchedulerMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,105,2,1,4))
hpicfJobSchedulerMIBCompliance3.setObjects((_A,_g))
if mibBuilder.loadTexts:hpicfJobSchedulerMIBCompliance3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfJobSchedulerMIB':hpicfJobSchedulerMIB,'hpicfJobSchedulerObjects':hpicfJobSchedulerObjects,'hpicfJobSchedulerTable':hpicfJobSchedulerTable,'hpicfJobSchedulerEntry':hpicfJobSchedulerEntry,_b:hpicfJobSchedulerName,_G:hpicfJobSchedulerRowStatus,_H:hpicfJobSchedulerCommand,_I:hpicfJobSchedulerConfigSave,_J:hpicfJobSchedulerRunCount,_K:hpicfJobSchedulerErrorCount,_L:hpicfJobSchedulerLastOutput,_M:hpicfJobSchedulerEvent,_N:hpicfJobSchedulerCalendarMonth,_O:hpicfJobSchedulerCalendarDayOfMonth,_P:hpicfJobSchedulerCalendarDayOfWeek,_Q:hpicfJobSchedulerCalendarHour,_R:hpicfJobSchedulerCalendarMinute,_T:hpicfJobSchedulerDelay,_U:hpicfJobSchedulerCount,_V:hpicfJobSchedulerStatus,_X:hpicfJobSchedulerRunningStatus,_Y:hpicfJobSchedulerLastRunTime,_c:hpicfJobSchedulerSkipCount,'hpicfJobSchedulerConformance':hpicfJobSchedulerConformance,'hpicfJobSchedulerMIBCompliances':hpicfJobSchedulerMIBCompliances,'hpicfJobSchedulerMIBCompliance':hpicfJobSchedulerMIBCompliance,'hpicfJobSchedulerMIBCompliance1':hpicfJobSchedulerMIBCompliance1,'hpicfJobSchedulerMIBCompliance2':hpicfJobSchedulerMIBCompliance2,'hpicfJobSchedulerMIBCompliance3':hpicfJobSchedulerMIBCompliance3,'hpicfJobSchedulerMIBGroups':hpicfJobSchedulerMIBGroups,_d:hpicfJobSchedulerGroup,_e:hpicfJobSchedulerGroup1,_f:hpicfJobSchedulerGroup2,_g:hpicfJobSchedulerGroup3})