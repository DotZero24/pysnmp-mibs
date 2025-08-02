_s='aluSystemSptGroup'
_r='aluTimeRefSelect'
_q='aluTimeRefDisqualified'
_p='aluTimeRefQualified'
_o='aluTimeRefDeleted'
_n='aluTimeRefCreated'
_m='aluSystemSptSecAggRate'
_l='timeRefLeapSecUpdTime'
_k='aluTod1PpsInput'
_j='aluTod1PpsOutput'
_i='aluTod1PpsMessageType'
_h='read-create'
_g='not-accessible'
_f='timeRefId'
_e='timeRefType'
_d='AluTod1PpsMessageType'
_c='accessible-for-notify'
_b='holdover'
_a='TPortSchedulerPIR'
_Z='aluSysTimeNotificationV6v1Group'
_Y='aluSysTimeReferenceGroup'
_X='timeRefLeapSec'
_W='timeRefLeapSecValid'
_V='timeRefLeapSecSched'
_U='timeRefDeltaNs'
_T='timeRefDeltaSec'
_S='timeRefPropertiesUpdate'
_R='timeRefQualifiedChange'
_Q='timeRefQualified'
_P='timeRefRowStatus'
_O='aluActiveTimeSourceChange'
_N='aluActiveTimeSourceId'
_M='aluActiveTimeSourceType'
_L='TmnxAdminState'
_K='aluTod1PpsGroup'
_J='timeRefPriority'
_I='aluNtpMdaTimestamp'
_H='obsolete'
_G='TruthValue'
_F='read-write'
_E='aluSystemNotifyTimeRefType'
_D='aluSystemNotifyTimeRefId'
_C='read-only'
_B='current'
_A='ALU-SYSTEM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
aluHwObjs,=mibBuilder.importSymbols('ALU-CHASSIS-MIB','aluHwObjs')
aluSARConfs,aluSARMIBModules,aluSARNotifyPrefix,aluSARObjs=mibBuilder.importSymbols('ALU-SAR-GLOBAL-MIB','aluSARConfs','aluSARMIBModules','aluSARNotifyPrefix','aluSARObjs')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp',_G)
TPortSchedulerPIR,TmnxAdminState=mibBuilder.importSymbols('TIMETRA-TC-MIB',_a,_L)
aluSystemMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,6,1,1,1,3,13))
if mibBuilder.loadTexts:aluSystemMIBModule.setRevisions(('1911-06-14 00:00','1914-02-10 00:00'))
class AluTod1PpsMessageType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('none',0),('cm',1),('ct',2),('irig-b000-b120',3),('irig-b001-b121',4),('irig-b002-b122',5),('irig-b003-b123',6),('irig-b004-b124',7),('irig-b005-b125',8),('irig-b006-b126',9),('irig-b007-b127',10)))
class AluSysTimePriorityType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*(('none',0),('priority1',1),('priority2',2),('priority3',3),('priority4',4),('priority5',5),('priority6',6),('priority7',7),('priority8',8),('priority9',9),('priority10',10),('priority11',11),('priority12',12),('priority13',13),('priority14',14),('priority15',15),('priority16',16),('priority17',17),(_b,18)))
class AluSysTimeRefLeapSecSchedType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('notScheduled',0),('forwardScheduled',1),('backwardScheduled',2)))
class AluSysTimeReferenceType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('notApplic',0),('gnss',1),('ptp',2),('ntp',3),('sntp',4),(_b,5)))
class AluSysTimeReferenceId(TextualConvention,Unsigned32):status=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_AluSystemMIBConformance_ObjectIdentity=ObjectIdentity
aluSystemMIBConformance=_AluSystemMIBConformance_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,13))
_AluSystemMIBCompliances_ObjectIdentity=ObjectIdentity
aluSystemMIBCompliances=_AluSystemMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,13,1))
_AluSystemMIBGroups_ObjectIdentity=ObjectIdentity
aluSystemMIBGroups=_AluSystemMIBGroups_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,1,13,2))
_AluSystemNotificationObjs_ObjectIdentity=ObjectIdentity
aluSystemNotificationObjs=_AluSystemNotificationObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,2,8))
_AluSystemNotifyTimeRefType_Type=AluSysTimeReferenceType
_AluSystemNotifyTimeRefType_Object=MibScalar
aluSystemNotifyTimeRefType=_AluSystemNotifyTimeRefType_Object((1,3,6,1,4,1,6527,6,1,2,2,2,8,1),_AluSystemNotifyTimeRefType_Type())
aluSystemNotifyTimeRefType.setMaxAccess(_c)
if mibBuilder.loadTexts:aluSystemNotifyTimeRefType.setStatus(_B)
_AluSystemNotifyTimeRefId_Type=AluSysTimeReferenceId
_AluSystemNotifyTimeRefId_Object=MibScalar
aluSystemNotifyTimeRefId=_AluSystemNotifyTimeRefId_Object((1,3,6,1,4,1,6527,6,1,2,2,2,8,2),_AluSystemNotifyTimeRefId_Type())
aluSystemNotifyTimeRefId.setMaxAccess(_c)
if mibBuilder.loadTexts:aluSystemNotifyTimeRefId.setStatus(_B)
_AluSystemObjs_ObjectIdentity=ObjectIdentity
aluSystemObjs=_AluSystemObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,13))
_AluTod1PpsInfo_ObjectIdentity=ObjectIdentity
aluTod1PpsInfo=_AluTod1PpsInfo_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,13,1))
class _AluTod1PpsMessageType_Type(AluTod1PpsMessageType):defaultValue=0
_AluTod1PpsMessageType_Type.__name__=_d
_AluTod1PpsMessageType_Object=MibScalar
aluTod1PpsMessageType=_AluTod1PpsMessageType_Object((1,3,6,1,4,1,6527,6,1,2,2,13,1,1),_AluTod1PpsMessageType_Type())
aluTod1PpsMessageType.setMaxAccess(_F)
if mibBuilder.loadTexts:aluTod1PpsMessageType.setStatus(_B)
class _AluTod1PpsOutput_Type(TmnxAdminState):defaultValue=3
_AluTod1PpsOutput_Type.__name__=_L
_AluTod1PpsOutput_Object=MibScalar
aluTod1PpsOutput=_AluTod1PpsOutput_Object((1,3,6,1,4,1,6527,6,1,2,2,13,1,2),_AluTod1PpsOutput_Type())
aluTod1PpsOutput.setMaxAccess(_F)
if mibBuilder.loadTexts:aluTod1PpsOutput.setStatus(_B)
class _AluTod1PpsInput_Type(TmnxAdminState):defaultValue=3
_AluTod1PpsInput_Type.__name__=_L
_AluTod1PpsInput_Object=MibScalar
aluTod1PpsInput=_AluTod1PpsInput_Object((1,3,6,1,4,1,6527,6,1,2,2,13,1,3),_AluTod1PpsInput_Type())
aluTod1PpsInput.setMaxAccess(_F)
if mibBuilder.loadTexts:aluTod1PpsInput.setStatus(_B)
_AluNtpSystem_ObjectIdentity=ObjectIdentity
aluNtpSystem=_AluNtpSystem_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,13,2))
class _AluNtpMdaTimestamp_Type(TruthValue):defaultValue=2
_AluNtpMdaTimestamp_Type.__name__=_G
_AluNtpMdaTimestamp_Object=MibScalar
aluNtpMdaTimestamp=_AluNtpMdaTimestamp_Object((1,3,6,1,4,1,6527,6,1,2,2,13,2,1),_AluNtpMdaTimestamp_Type())
aluNtpMdaTimestamp.setMaxAccess(_F)
if mibBuilder.loadTexts:aluNtpMdaTimestamp.setStatus(_B)
_AluSysTimeSelector_ObjectIdentity=ObjectIdentity
aluSysTimeSelector=_AluSysTimeSelector_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,13,3))
_AluActiveTimeSourceType_Type=AluSysTimeReferenceType
_AluActiveTimeSourceType_Object=MibScalar
aluActiveTimeSourceType=_AluActiveTimeSourceType_Object((1,3,6,1,4,1,6527,6,1,2,2,13,3,1),_AluActiveTimeSourceType_Type())
aluActiveTimeSourceType.setMaxAccess(_C)
if mibBuilder.loadTexts:aluActiveTimeSourceType.setStatus(_B)
_AluActiveTimeSourceId_Type=AluSysTimeReferenceId
_AluActiveTimeSourceId_Object=MibScalar
aluActiveTimeSourceId=_AluActiveTimeSourceId_Object((1,3,6,1,4,1,6527,6,1,2,2,13,3,2),_AluActiveTimeSourceId_Type())
aluActiveTimeSourceId.setMaxAccess(_C)
if mibBuilder.loadTexts:aluActiveTimeSourceId.setStatus(_B)
_AluActiveTimeSourceChange_Type=TimeStamp
_AluActiveTimeSourceChange_Object=MibScalar
aluActiveTimeSourceChange=_AluActiveTimeSourceChange_Object((1,3,6,1,4,1,6527,6,1,2,2,13,3,3),_AluActiveTimeSourceChange_Type())
aluActiveTimeSourceChange.setMaxAccess(_C)
if mibBuilder.loadTexts:aluActiveTimeSourceChange.setStatus(_B)
_AluTimeSelectorTable_Object=MibTable
aluTimeSelectorTable=_AluTimeSelectorTable_Object((1,3,6,1,4,1,6527,6,1,2,2,13,3,4))
if mibBuilder.loadTexts:aluTimeSelectorTable.setStatus(_B)
_AluTimeReferenceEntry_Object=MibTableRow
aluTimeReferenceEntry=_AluTimeReferenceEntry_Object((1,3,6,1,4,1,6527,6,1,2,2,13,3,4,1))
aluTimeReferenceEntry.setIndexNames((0,_A,_e),(0,_A,_f))
if mibBuilder.loadTexts:aluTimeReferenceEntry.setStatus(_B)
_TimeRefType_Type=AluSysTimeReferenceType
_TimeRefType_Object=MibTableColumn
timeRefType=_TimeRefType_Object((1,3,6,1,4,1,6527,6,1,2,2,13,3,4,1,1),_TimeRefType_Type())
timeRefType.setMaxAccess(_g)
if mibBuilder.loadTexts:timeRefType.setStatus(_B)
_TimeRefId_Type=AluSysTimeReferenceId
_TimeRefId_Object=MibTableColumn
timeRefId=_TimeRefId_Object((1,3,6,1,4,1,6527,6,1,2,2,13,3,4,1,2),_TimeRefId_Type())
timeRefId.setMaxAccess(_g)
if mibBuilder.loadTexts:timeRefId.setStatus(_B)
_TimeRefPriority_Type=AluSysTimePriorityType
_TimeRefPriority_Object=MibTableColumn
timeRefPriority=_TimeRefPriority_Object((1,3,6,1,4,1,6527,6,1,2,2,13,3,4,1,3),_TimeRefPriority_Type())
timeRefPriority.setMaxAccess(_h)
if mibBuilder.loadTexts:timeRefPriority.setStatus(_B)
_TimeRefRowStatus_Type=RowStatus
_TimeRefRowStatus_Object=MibTableColumn
timeRefRowStatus=_TimeRefRowStatus_Object((1,3,6,1,4,1,6527,6,1,2,2,13,3,4,1,4),_TimeRefRowStatus_Type())
timeRefRowStatus.setMaxAccess(_h)
if mibBuilder.loadTexts:timeRefRowStatus.setStatus(_B)
class _TimeRefQualified_Type(TruthValue):defaultValue=2
_TimeRefQualified_Type.__name__=_G
_TimeRefQualified_Object=MibTableColumn
timeRefQualified=_TimeRefQualified_Object((1,3,6,1,4,1,6527,6,1,2,2,13,3,4,1,5),_TimeRefQualified_Type())
timeRefQualified.setMaxAccess(_C)
if mibBuilder.loadTexts:timeRefQualified.setStatus(_B)
_TimeRefQualifiedChange_Type=TimeStamp
_TimeRefQualifiedChange_Object=MibTableColumn
timeRefQualifiedChange=_TimeRefQualifiedChange_Object((1,3,6,1,4,1,6527,6,1,2,2,13,3,4,1,6),_TimeRefQualifiedChange_Type())
timeRefQualifiedChange.setMaxAccess(_C)
if mibBuilder.loadTexts:timeRefQualifiedChange.setStatus(_B)
_TimeRefPropertiesUpdate_Type=TimeStamp
_TimeRefPropertiesUpdate_Object=MibTableColumn
timeRefPropertiesUpdate=_TimeRefPropertiesUpdate_Object((1,3,6,1,4,1,6527,6,1,2,2,13,3,4,1,7),_TimeRefPropertiesUpdate_Type())
timeRefPropertiesUpdate.setMaxAccess(_C)
if mibBuilder.loadTexts:timeRefPropertiesUpdate.setStatus(_B)
_TimeRefDeltaSec_Type=Integer32
_TimeRefDeltaSec_Object=MibTableColumn
timeRefDeltaSec=_TimeRefDeltaSec_Object((1,3,6,1,4,1,6527,6,1,2,2,13,3,4,1,8),_TimeRefDeltaSec_Type())
timeRefDeltaSec.setMaxAccess(_C)
if mibBuilder.loadTexts:timeRefDeltaSec.setStatus(_B)
_TimeRefDeltaNs_Type=Integer32
_TimeRefDeltaNs_Object=MibTableColumn
timeRefDeltaNs=_TimeRefDeltaNs_Object((1,3,6,1,4,1,6527,6,1,2,2,13,3,4,1,9),_TimeRefDeltaNs_Type())
timeRefDeltaNs.setMaxAccess(_C)
if mibBuilder.loadTexts:timeRefDeltaNs.setStatus(_B)
_TimeRefLeapSecSched_Type=AluSysTimeRefLeapSecSchedType
_TimeRefLeapSecSched_Object=MibTableColumn
timeRefLeapSecSched=_TimeRefLeapSecSched_Object((1,3,6,1,4,1,6527,6,1,2,2,13,3,4,1,10),_TimeRefLeapSecSched_Type())
timeRefLeapSecSched.setMaxAccess(_C)
if mibBuilder.loadTexts:timeRefLeapSecSched.setStatus(_B)
class _TimeRefLeapSecValid_Type(TruthValue):defaultValue=2
_TimeRefLeapSecValid_Type.__name__=_G
_TimeRefLeapSecValid_Object=MibTableColumn
timeRefLeapSecValid=_TimeRefLeapSecValid_Object((1,3,6,1,4,1,6527,6,1,2,2,13,3,4,1,11),_TimeRefLeapSecValid_Type())
timeRefLeapSecValid.setMaxAccess(_C)
if mibBuilder.loadTexts:timeRefLeapSecValid.setStatus(_H)
_TimeRefLeapSec_Type=Unsigned32
_TimeRefLeapSec_Object=MibTableColumn
timeRefLeapSec=_TimeRefLeapSec_Object((1,3,6,1,4,1,6527,6,1,2,2,13,3,4,1,12),_TimeRefLeapSec_Type())
timeRefLeapSec.setMaxAccess(_C)
if mibBuilder.loadTexts:timeRefLeapSec.setStatus(_H)
_TimeRefLeapSecUpdTime_Type=TimeStamp
_TimeRefLeapSecUpdTime_Object=MibTableColumn
timeRefLeapSecUpdTime=_TimeRefLeapSecUpdTime_Object((1,3,6,1,4,1,6527,6,1,2,2,13,3,4,1,13),_TimeRefLeapSecUpdTime_Type())
timeRefLeapSecUpdTime.setMaxAccess(_C)
if mibBuilder.loadTexts:timeRefLeapSecUpdTime.setStatus(_B)
_AluSystemSptConfig_ObjectIdentity=ObjectIdentity
aluSystemSptConfig=_AluSystemSptConfig_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,2,13,4))
class _AluSystemSptSecAggRate_Type(TPortSchedulerPIR):defaultValue=50000
_AluSystemSptSecAggRate_Type.__name__=_a
_AluSystemSptSecAggRate_Object=MibScalar
aluSystemSptSecAggRate=_AluSystemSptSecAggRate_Object((1,3,6,1,4,1,6527,6,1,2,2,13,4,1),_AluSystemSptSecAggRate_Type())
aluSystemSptSecAggRate.setMaxAccess(_F)
if mibBuilder.loadTexts:aluSystemSptSecAggRate.setStatus(_B)
_AluSystemNotifyPrefix_ObjectIdentity=ObjectIdentity
aluSystemNotifyPrefix=_AluSystemNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,3,9))
_AluSystemNotification_ObjectIdentity=ObjectIdentity
aluSystemNotification=_AluSystemNotification_ObjectIdentity((1,3,6,1,4,1,6527,6,1,2,3,9,0))
aluTod1PpsGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,13,2,1))
aluTod1PpsGroup.setObjects(*((_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:aluTod1PpsGroup.setStatus(_B)
aluNtpGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,13,2,2))
aluNtpGroup.setObjects((_A,_I))
if mibBuilder.loadTexts:aluNtpGroup.setStatus(_B)
aluSysTimeReferenceGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,13,2,3))
aluSysTimeReferenceGroup.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_J),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:aluSysTimeReferenceGroup.setStatus(_B)
aluSysTimeNotifyObjsV6v1Group=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,13,2,4))
aluSysTimeNotifyObjsV6v1Group.setObjects(*((_A,_D),(_A,_E)))
if mibBuilder.loadTexts:aluSysTimeNotifyObjsV6v1Group.setStatus(_B)
aluSysTimeReferenceV6v1Group=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,13,2,6))
aluSysTimeReferenceV6v1Group.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_J),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_l)))
if mibBuilder.loadTexts:aluSysTimeReferenceV6v1Group.setStatus(_B)
aluSysTimeReferenceObsoleteGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,13,2,7))
aluSysTimeReferenceObsoleteGroup.setObjects(*((_A,_W),(_A,_X)))
if mibBuilder.loadTexts:aluSysTimeReferenceObsoleteGroup.setStatus(_B)
aluSystemSptGroup=ObjectGroup((1,3,6,1,4,1,6527,6,1,2,1,13,2,8))
aluSystemSptGroup.setObjects((_A,_m))
if mibBuilder.loadTexts:aluSystemSptGroup.setStatus(_B)
aluTimeRefCreated=NotificationType((1,3,6,1,4,1,6527,6,1,2,3,9,0,1))
aluTimeRefCreated.setObjects(*((_A,_E),(_A,_D),(_A,_J)))
if mibBuilder.loadTexts:aluTimeRefCreated.setStatus(_B)
aluTimeRefDeleted=NotificationType((1,3,6,1,4,1,6527,6,1,2,3,9,0,2))
aluTimeRefDeleted.setObjects(*((_A,_E),(_A,_D)))
if mibBuilder.loadTexts:aluTimeRefDeleted.setStatus(_B)
aluTimeRefQualified=NotificationType((1,3,6,1,4,1,6527,6,1,2,3,9,0,3))
aluTimeRefQualified.setObjects(*((_A,_E),(_A,_D)))
if mibBuilder.loadTexts:aluTimeRefQualified.setStatus(_B)
aluTimeRefDisqualified=NotificationType((1,3,6,1,4,1,6527,6,1,2,3,9,0,4))
aluTimeRefDisqualified.setObjects(*((_A,_E),(_A,_D)))
if mibBuilder.loadTexts:aluTimeRefDisqualified.setStatus(_B)
aluTimeRefSelect=NotificationType((1,3,6,1,4,1,6527,6,1,2,3,9,0,5))
aluTimeRefSelect.setObjects(*((_A,_E),(_A,_D)))
if mibBuilder.loadTexts:aluTimeRefSelect.setStatus(_B)
aluSysTimeNotificationV6v1Group=NotificationGroup((1,3,6,1,4,1,6527,6,1,2,1,13,2,5))
aluSysTimeNotificationV6v1Group.setObjects(*((_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:aluSysTimeNotificationV6v1Group.setStatus(_B)
aluSystemMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6527,6,1,2,1,13,1,1))
aluSystemMIBCompliance.setObjects((_A,_K))
if mibBuilder.loadTexts:aluSystemMIBCompliance.setStatus(_H)
aluSystemV6v1MIBCompliance=ModuleCompliance((1,3,6,1,4,1,6527,6,1,2,1,13,1,2))
aluSystemV6v1MIBCompliance.setObjects(*((_A,_K),(_A,_I),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:aluSystemV6v1MIBCompliance.setStatus(_H)
aluSystemV7v0MIBCompliance=ModuleCompliance((1,3,6,1,4,1,6527,6,1,2,1,13,1,3))
aluSystemV7v0MIBCompliance.setObjects(*((_A,_K),(_A,_I),(_A,_Y),(_A,_Z),(_A,_s)))
if mibBuilder.loadTexts:aluSystemV7v0MIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_d:AluTod1PpsMessageType,'AluSysTimePriorityType':AluSysTimePriorityType,'AluSysTimeRefLeapSecSchedType':AluSysTimeRefLeapSecSchedType,'AluSysTimeReferenceType':AluSysTimeReferenceType,'AluSysTimeReferenceId':AluSysTimeReferenceId,'aluSystemMIBModule':aluSystemMIBModule,'aluSystemMIBConformance':aluSystemMIBConformance,'aluSystemMIBCompliances':aluSystemMIBCompliances,'aluSystemMIBCompliance':aluSystemMIBCompliance,'aluSystemV6v1MIBCompliance':aluSystemV6v1MIBCompliance,'aluSystemV7v0MIBCompliance':aluSystemV7v0MIBCompliance,'aluSystemMIBGroups':aluSystemMIBGroups,_K:aluTod1PpsGroup,'aluNtpGroup':aluNtpGroup,_Y:aluSysTimeReferenceGroup,'aluSysTimeNotifyObjsV6v1Group':aluSysTimeNotifyObjsV6v1Group,_Z:aluSysTimeNotificationV6v1Group,'aluSysTimeReferenceV6v1Group':aluSysTimeReferenceV6v1Group,'aluSysTimeReferenceObsoleteGroup':aluSysTimeReferenceObsoleteGroup,_s:aluSystemSptGroup,'aluSystemNotificationObjs':aluSystemNotificationObjs,_E:aluSystemNotifyTimeRefType,_D:aluSystemNotifyTimeRefId,'aluSystemObjs':aluSystemObjs,'aluTod1PpsInfo':aluTod1PpsInfo,_i:aluTod1PpsMessageType,_j:aluTod1PpsOutput,_k:aluTod1PpsInput,'aluNtpSystem':aluNtpSystem,_I:aluNtpMdaTimestamp,'aluSysTimeSelector':aluSysTimeSelector,_M:aluActiveTimeSourceType,_N:aluActiveTimeSourceId,_O:aluActiveTimeSourceChange,'aluTimeSelectorTable':aluTimeSelectorTable,'aluTimeReferenceEntry':aluTimeReferenceEntry,_e:timeRefType,_f:timeRefId,_J:timeRefPriority,_P:timeRefRowStatus,_Q:timeRefQualified,_R:timeRefQualifiedChange,_S:timeRefPropertiesUpdate,_T:timeRefDeltaSec,_U:timeRefDeltaNs,_V:timeRefLeapSecSched,_W:timeRefLeapSecValid,_X:timeRefLeapSec,_l:timeRefLeapSecUpdTime,'aluSystemSptConfig':aluSystemSptConfig,_m:aluSystemSptSecAggRate,'aluSystemNotifyPrefix':aluSystemNotifyPrefix,'aluSystemNotification':aluSystemNotification,_n:aluTimeRefCreated,_o:aluTimeRefDeleted,_p:aluTimeRefQualified,_q:aluTimeRefDisqualified,_r:aluTimeRefSelect})