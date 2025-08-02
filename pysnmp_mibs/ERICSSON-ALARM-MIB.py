_AN='eriAlarmSNMPResourceGroup'
_AM='eriAlarmAddAddInfoGroup'
_AL='eriAlarmChangeAlarmGroup'
_AK='eriAlarmAlertNotifGroup'
_AJ='eriAlarmAlertsGroup'
_AI='eriAlarmHeartBeatNotifGroup'
_AH='eriAlarmSimpleAlarmGroup'
_AG='eriAlarmHeartBeatGroup'
_AF='eriAlarmActiveAlarmsGroup'
_AE='eriAlarmSummaryGroup'
_AD='eriAlarmHeartBeatNotif'
_AC='eriAlarmCriticalAlert'
_AB='eriAlarmMajorAlert'
_AA='eriAlarmMinorAlert'
_A9='eriAlarmWarnAlert'
_A8='eriAlarmIndAlert'
_A7='eriAlarmAppendAlertInfo'
_A6='eriAlarmAppendInfo'
_A5='eriAlarmAlarmListRebuilt'
_A4='eriAlarmCleared'
_A3='eriAlarmCritical'
_A2='eriAlarmMajor'
_A1='eriAlarmMinor'
_A0='eriAlarmWarning'
_z='eriAlarmIndeterminate'
_y='eriAlarmActiveOrigAdditionalText'
_x='eriAlarmActiveOriginalSeverity'
_w='eriAlarmActiveOriginalEventTime'
_v='eriAlarmHbInterval'
_u='eriAlarmAlertAdditionalText'
_t='eriAlarmAlertSeverity'
_s='eriAlarmAlertTableURL'
_r='eriAlarmAlertNumber'
_q='eriAlarmActiveAdditionalText'
_p='eriAlarmActiveSeverity'
_o='eriAlarmActiveNumber'
_n='eriAlarmSumWarning'
_m='eriAlarmSumMinor'
_l='eriAlarmSumMajor'
_k='eriAlarmSumCritical'
_j='eriAlarmSumIndeterminate'
_i='eriAlarmAlertIndex'
_h='not-accessible'
_g='eriAlarmActiveIndex'
_f='snmpTargetBasicGroup'
_e='SNMP-TARGET-MIB'
_d='snmpNotifyGroup'
_c='SNMP-NOTIFICATION-MIB'
_b='eriAlarmAlertResourceId'
_a='eriAlarmActiveResourceId'
_Z='eriAlarmAlertLastChanged'
_Y='eriAlarmActiveTableURL'
_X='eriAlarmActiveLastChanged'
_W='accessible-for-notify'
_V='eriAlarmAlertProbableCause'
_U='eriAlarmAlertEventTime'
_T='eriAlarmAlertEventType'
_S='eriAlarmAlertSpecificProblem'
_R='eriAlarmAlertManagedObject'
_Q='eriAlarmAlertMinorType'
_P='eriAlarmAlertMajorType'
_O='eriAlarmAlertLastSequenceNo'
_N='eriAlarmActiveProbableCause'
_M='eriAlarmActiveEventTime'
_L='eriAlarmActiveEventType'
_K='eriAlarmActiveSpecificProblem'
_J='eriAlarmActiveManagedObject'
_I='eriAlarmActiveMinorType'
_H='eriAlarmActiveMajorType'
_G='eriAlarmActiveLastSequenceNo'
_F='eriAlarmNObjMoreAdditionalText'
_E='eriAlarmNObjResourceId'
_D='eriAlarmNObjAdditionalText'
_C='read-only'
_B='current'
_A='ERICSSON-ALARM-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ResourceId,=mibBuilder.importSymbols('ALARM-MIB','ResourceId')
EriProbableCause,=mibBuilder.importSymbols('ERICSSON-ALARM-PC-MIB','EriProbableCause')
EriAdditionalText,EriAlarmIndex,EriAlarmSequenceNumber,EriAlarmSpecificProblem,EriAlarmType,EriLargeAdditionalText=mibBuilder.importSymbols('ERICSSON-ALARM-TC-MIB','EriAdditionalText','EriAlarmIndex','EriAlarmSequenceNumber','EriAlarmSpecificProblem','EriAlarmType','EriLargeAdditionalText')
EriMO,=mibBuilder.importSymbols('ERICSSON-TC-MIB','EriMO')
ericssonModules,=mibBuilder.importSymbols('ERICSSON-TOP-MIB','ericssonModules')
IANAItuEventType,=mibBuilder.importSymbols('IANA-ITU-ALARM-TC-MIB','IANAItuEventType')
ItuPerceivedSeverity,=mibBuilder.importSymbols('ITU-ALARM-TC-MIB','ItuPerceivedSeverity')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
snmpNotifyGroup,=mibBuilder.importSymbols(_c,_d)
snmpTargetBasicGroup,=mibBuilder.importSymbols(_e,_f)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention','TruthValue')
ericssonAlarmMIB=ModuleIdentity((1,3,6,1,4,1,193,183,4))
if mibBuilder.loadTexts:ericssonAlarmMIB.setRevisions(('2008-10-17 00:00',))
_EriAlarmObjects_ObjectIdentity=ObjectIdentity
eriAlarmObjects=_EriAlarmObjects_ObjectIdentity((1,3,6,1,4,1,193,183,4,1))
_EriAlarmSummary_ObjectIdentity=ObjectIdentity
eriAlarmSummary=_EriAlarmSummary_ObjectIdentity((1,3,6,1,4,1,193,183,4,1,1))
_EriAlarmSumIndeterminate_Type=Gauge32
_EriAlarmSumIndeterminate_Object=MibScalar
eriAlarmSumIndeterminate=_EriAlarmSumIndeterminate_Object((1,3,6,1,4,1,193,183,4,1,1,1),_EriAlarmSumIndeterminate_Type())
eriAlarmSumIndeterminate.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmSumIndeterminate.setStatus(_B)
_EriAlarmSumCritical_Type=Gauge32
_EriAlarmSumCritical_Object=MibScalar
eriAlarmSumCritical=_EriAlarmSumCritical_Object((1,3,6,1,4,1,193,183,4,1,1,2),_EriAlarmSumCritical_Type())
eriAlarmSumCritical.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmSumCritical.setStatus(_B)
_EriAlarmSumMajor_Type=Gauge32
_EriAlarmSumMajor_Object=MibScalar
eriAlarmSumMajor=_EriAlarmSumMajor_Object((1,3,6,1,4,1,193,183,4,1,1,3),_EriAlarmSumMajor_Type())
eriAlarmSumMajor.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmSumMajor.setStatus(_B)
_EriAlarmSumMinor_Type=Gauge32
_EriAlarmSumMinor_Object=MibScalar
eriAlarmSumMinor=_EriAlarmSumMinor_Object((1,3,6,1,4,1,193,183,4,1,1,4),_EriAlarmSumMinor_Type())
eriAlarmSumMinor.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmSumMinor.setStatus(_B)
_EriAlarmSumWarning_Type=Gauge32
_EriAlarmSumWarning_Object=MibScalar
eriAlarmSumWarning=_EriAlarmSumWarning_Object((1,3,6,1,4,1,193,183,4,1,1,5),_EriAlarmSumWarning_Type())
eriAlarmSumWarning.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmSumWarning.setStatus(_B)
_EriAlarmNotifObjects_ObjectIdentity=ObjectIdentity
eriAlarmNotifObjects=_EriAlarmNotifObjects_ObjectIdentity((1,3,6,1,4,1,193,183,4,1,2))
_EriAlarmNObjAdditionalText_Type=EriAdditionalText
_EriAlarmNObjAdditionalText_Object=MibScalar
eriAlarmNObjAdditionalText=_EriAlarmNObjAdditionalText_Object((1,3,6,1,4,1,193,183,4,1,2,1),_EriAlarmNObjAdditionalText_Type())
eriAlarmNObjAdditionalText.setMaxAccess(_W)
if mibBuilder.loadTexts:eriAlarmNObjAdditionalText.setStatus(_B)
_EriAlarmNObjMoreAdditionalText_Type=TruthValue
_EriAlarmNObjMoreAdditionalText_Object=MibScalar
eriAlarmNObjMoreAdditionalText=_EriAlarmNObjMoreAdditionalText_Object((1,3,6,1,4,1,193,183,4,1,2,2),_EriAlarmNObjMoreAdditionalText_Type())
eriAlarmNObjMoreAdditionalText.setMaxAccess(_W)
if mibBuilder.loadTexts:eriAlarmNObjMoreAdditionalText.setStatus(_B)
_EriAlarmNObjResourceId_Type=TruthValue
_EriAlarmNObjResourceId_Object=MibScalar
eriAlarmNObjResourceId=_EriAlarmNObjResourceId_Object((1,3,6,1,4,1,193,183,4,1,2,3),_EriAlarmNObjResourceId_Type())
eriAlarmNObjResourceId.setMaxAccess(_W)
if mibBuilder.loadTexts:eriAlarmNObjResourceId.setStatus(_B)
_EriAlarmActiveAlarms_ObjectIdentity=ObjectIdentity
eriAlarmActiveAlarms=_EriAlarmActiveAlarms_ObjectIdentity((1,3,6,1,4,1,193,183,4,1,3))
_EriAlarmActiveNumber_Type=Unsigned32
_EriAlarmActiveNumber_Object=MibScalar
eriAlarmActiveNumber=_EriAlarmActiveNumber_Object((1,3,6,1,4,1,193,183,4,1,3,1),_EriAlarmActiveNumber_Type())
eriAlarmActiveNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmActiveNumber.setStatus(_B)
_EriAlarmActiveLastChanged_Type=DateAndTime
_EriAlarmActiveLastChanged_Object=MibScalar
eriAlarmActiveLastChanged=_EriAlarmActiveLastChanged_Object((1,3,6,1,4,1,193,183,4,1,3,2),_EriAlarmActiveLastChanged_Type())
eriAlarmActiveLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmActiveLastChanged.setStatus(_B)
_EriAlarmActiveLastSequenceNo_Type=EriAlarmSequenceNumber
_EriAlarmActiveLastSequenceNo_Object=MibScalar
eriAlarmActiveLastSequenceNo=_EriAlarmActiveLastSequenceNo_Object((1,3,6,1,4,1,193,183,4,1,3,3),_EriAlarmActiveLastSequenceNo_Type())
eriAlarmActiveLastSequenceNo.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmActiveLastSequenceNo.setStatus(_B)
_EriAlarmActiveTableURL_Type=SnmpAdminString
_EriAlarmActiveTableURL_Object=MibScalar
eriAlarmActiveTableURL=_EriAlarmActiveTableURL_Object((1,3,6,1,4,1,193,183,4,1,3,4),_EriAlarmActiveTableURL_Type())
eriAlarmActiveTableURL.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmActiveTableURL.setStatus(_B)
_EriAlarmActiveAlarmTable_Object=MibTable
eriAlarmActiveAlarmTable=_EriAlarmActiveAlarmTable_Object((1,3,6,1,4,1,193,183,4,1,3,5))
if mibBuilder.loadTexts:eriAlarmActiveAlarmTable.setStatus(_B)
_EriAlarmActiveAlarmEntry_Object=MibTableRow
eriAlarmActiveAlarmEntry=_EriAlarmActiveAlarmEntry_Object((1,3,6,1,4,1,193,183,4,1,3,5,1))
eriAlarmActiveAlarmEntry.setIndexNames((0,_A,_g))
if mibBuilder.loadTexts:eriAlarmActiveAlarmEntry.setStatus(_B)
_EriAlarmActiveIndex_Type=EriAlarmIndex
_EriAlarmActiveIndex_Object=MibTableColumn
eriAlarmActiveIndex=_EriAlarmActiveIndex_Object((1,3,6,1,4,1,193,183,4,1,3,5,1,1),_EriAlarmActiveIndex_Type())
eriAlarmActiveIndex.setMaxAccess(_h)
if mibBuilder.loadTexts:eriAlarmActiveIndex.setStatus(_B)
_EriAlarmActiveMajorType_Type=EriAlarmType
_EriAlarmActiveMajorType_Object=MibTableColumn
eriAlarmActiveMajorType=_EriAlarmActiveMajorType_Object((1,3,6,1,4,1,193,183,4,1,3,5,1,2),_EriAlarmActiveMajorType_Type())
eriAlarmActiveMajorType.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmActiveMajorType.setStatus(_B)
_EriAlarmActiveMinorType_Type=EriAlarmType
_EriAlarmActiveMinorType_Object=MibTableColumn
eriAlarmActiveMinorType=_EriAlarmActiveMinorType_Object((1,3,6,1,4,1,193,183,4,1,3,5,1,3),_EriAlarmActiveMinorType_Type())
eriAlarmActiveMinorType.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmActiveMinorType.setStatus(_B)
_EriAlarmActiveSpecificProblem_Type=EriAlarmSpecificProblem
_EriAlarmActiveSpecificProblem_Object=MibTableColumn
eriAlarmActiveSpecificProblem=_EriAlarmActiveSpecificProblem_Object((1,3,6,1,4,1,193,183,4,1,3,5,1,4),_EriAlarmActiveSpecificProblem_Type())
eriAlarmActiveSpecificProblem.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmActiveSpecificProblem.setStatus(_B)
_EriAlarmActiveManagedObject_Type=EriMO
_EriAlarmActiveManagedObject_Object=MibTableColumn
eriAlarmActiveManagedObject=_EriAlarmActiveManagedObject_Object((1,3,6,1,4,1,193,183,4,1,3,5,1,5),_EriAlarmActiveManagedObject_Type())
eriAlarmActiveManagedObject.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmActiveManagedObject.setStatus(_B)
_EriAlarmActiveEventType_Type=IANAItuEventType
_EriAlarmActiveEventType_Object=MibTableColumn
eriAlarmActiveEventType=_EriAlarmActiveEventType_Object((1,3,6,1,4,1,193,183,4,1,3,5,1,6),_EriAlarmActiveEventType_Type())
eriAlarmActiveEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmActiveEventType.setStatus(_B)
_EriAlarmActiveEventTime_Type=DateAndTime
_EriAlarmActiveEventTime_Object=MibTableColumn
eriAlarmActiveEventTime=_EriAlarmActiveEventTime_Object((1,3,6,1,4,1,193,183,4,1,3,5,1,7),_EriAlarmActiveEventTime_Type())
eriAlarmActiveEventTime.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmActiveEventTime.setStatus(_B)
_EriAlarmActiveOriginalEventTime_Type=DateAndTime
_EriAlarmActiveOriginalEventTime_Object=MibTableColumn
eriAlarmActiveOriginalEventTime=_EriAlarmActiveOriginalEventTime_Object((1,3,6,1,4,1,193,183,4,1,3,5,1,8),_EriAlarmActiveOriginalEventTime_Type())
eriAlarmActiveOriginalEventTime.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmActiveOriginalEventTime.setStatus(_B)
_EriAlarmActiveProbableCause_Type=EriProbableCause
_EriAlarmActiveProbableCause_Object=MibTableColumn
eriAlarmActiveProbableCause=_EriAlarmActiveProbableCause_Object((1,3,6,1,4,1,193,183,4,1,3,5,1,9),_EriAlarmActiveProbableCause_Type())
eriAlarmActiveProbableCause.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmActiveProbableCause.setStatus(_B)
_EriAlarmActiveSeverity_Type=ItuPerceivedSeverity
_EriAlarmActiveSeverity_Object=MibTableColumn
eriAlarmActiveSeverity=_EriAlarmActiveSeverity_Object((1,3,6,1,4,1,193,183,4,1,3,5,1,10),_EriAlarmActiveSeverity_Type())
eriAlarmActiveSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmActiveSeverity.setStatus(_B)
_EriAlarmActiveOriginalSeverity_Type=ItuPerceivedSeverity
_EriAlarmActiveOriginalSeverity_Object=MibTableColumn
eriAlarmActiveOriginalSeverity=_EriAlarmActiveOriginalSeverity_Object((1,3,6,1,4,1,193,183,4,1,3,5,1,11),_EriAlarmActiveOriginalSeverity_Type())
eriAlarmActiveOriginalSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmActiveOriginalSeverity.setStatus(_B)
_EriAlarmActiveAdditionalText_Type=EriLargeAdditionalText
_EriAlarmActiveAdditionalText_Object=MibTableColumn
eriAlarmActiveAdditionalText=_EriAlarmActiveAdditionalText_Object((1,3,6,1,4,1,193,183,4,1,3,5,1,12),_EriAlarmActiveAdditionalText_Type())
eriAlarmActiveAdditionalText.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmActiveAdditionalText.setStatus(_B)
_EriAlarmActiveOrigAdditionalText_Type=EriLargeAdditionalText
_EriAlarmActiveOrigAdditionalText_Object=MibTableColumn
eriAlarmActiveOrigAdditionalText=_EriAlarmActiveOrigAdditionalText_Object((1,3,6,1,4,1,193,183,4,1,3,5,1,13),_EriAlarmActiveOrigAdditionalText_Type())
eriAlarmActiveOrigAdditionalText.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmActiveOrigAdditionalText.setStatus(_B)
_EriAlarmActiveResourceId_Type=ResourceId
_EriAlarmActiveResourceId_Object=MibTableColumn
eriAlarmActiveResourceId=_EriAlarmActiveResourceId_Object((1,3,6,1,4,1,193,183,4,1,3,5,1,14),_EriAlarmActiveResourceId_Type())
eriAlarmActiveResourceId.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmActiveResourceId.setStatus(_B)
_EriAlarmAlerts_ObjectIdentity=ObjectIdentity
eriAlarmAlerts=_EriAlarmAlerts_ObjectIdentity((1,3,6,1,4,1,193,183,4,1,4))
_EriAlarmAlertNumber_Type=Unsigned32
_EriAlarmAlertNumber_Object=MibScalar
eriAlarmAlertNumber=_EriAlarmAlertNumber_Object((1,3,6,1,4,1,193,183,4,1,4,1),_EriAlarmAlertNumber_Type())
eriAlarmAlertNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmAlertNumber.setStatus(_B)
_EriAlarmAlertLastChanged_Type=DateAndTime
_EriAlarmAlertLastChanged_Object=MibScalar
eriAlarmAlertLastChanged=_EriAlarmAlertLastChanged_Object((1,3,6,1,4,1,193,183,4,1,4,2),_EriAlarmAlertLastChanged_Type())
eriAlarmAlertLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmAlertLastChanged.setStatus(_B)
_EriAlarmAlertLastSequenceNo_Type=EriAlarmSequenceNumber
_EriAlarmAlertLastSequenceNo_Object=MibScalar
eriAlarmAlertLastSequenceNo=_EriAlarmAlertLastSequenceNo_Object((1,3,6,1,4,1,193,183,4,1,4,3),_EriAlarmAlertLastSequenceNo_Type())
eriAlarmAlertLastSequenceNo.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmAlertLastSequenceNo.setStatus(_B)
_EriAlarmAlertTableURL_Type=SnmpAdminString
_EriAlarmAlertTableURL_Object=MibScalar
eriAlarmAlertTableURL=_EriAlarmAlertTableURL_Object((1,3,6,1,4,1,193,183,4,1,4,4),_EriAlarmAlertTableURL_Type())
eriAlarmAlertTableURL.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmAlertTableURL.setStatus(_B)
_EriAlarmAlertTable_Object=MibTable
eriAlarmAlertTable=_EriAlarmAlertTable_Object((1,3,6,1,4,1,193,183,4,1,4,5))
if mibBuilder.loadTexts:eriAlarmAlertTable.setStatus(_B)
_EriAlarmAlertEntry_Object=MibTableRow
eriAlarmAlertEntry=_EriAlarmAlertEntry_Object((1,3,6,1,4,1,193,183,4,1,4,5,1))
eriAlarmAlertEntry.setIndexNames((0,_A,_i))
if mibBuilder.loadTexts:eriAlarmAlertEntry.setStatus(_B)
_EriAlarmAlertIndex_Type=EriAlarmIndex
_EriAlarmAlertIndex_Object=MibTableColumn
eriAlarmAlertIndex=_EriAlarmAlertIndex_Object((1,3,6,1,4,1,193,183,4,1,4,5,1,1),_EriAlarmAlertIndex_Type())
eriAlarmAlertIndex.setMaxAccess(_h)
if mibBuilder.loadTexts:eriAlarmAlertIndex.setStatus(_B)
_EriAlarmAlertMajorType_Type=EriAlarmType
_EriAlarmAlertMajorType_Object=MibTableColumn
eriAlarmAlertMajorType=_EriAlarmAlertMajorType_Object((1,3,6,1,4,1,193,183,4,1,4,5,1,2),_EriAlarmAlertMajorType_Type())
eriAlarmAlertMajorType.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmAlertMajorType.setStatus(_B)
_EriAlarmAlertMinorType_Type=EriAlarmType
_EriAlarmAlertMinorType_Object=MibTableColumn
eriAlarmAlertMinorType=_EriAlarmAlertMinorType_Object((1,3,6,1,4,1,193,183,4,1,4,5,1,3),_EriAlarmAlertMinorType_Type())
eriAlarmAlertMinorType.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmAlertMinorType.setStatus(_B)
_EriAlarmAlertSpecificProblem_Type=EriAlarmSpecificProblem
_EriAlarmAlertSpecificProblem_Object=MibTableColumn
eriAlarmAlertSpecificProblem=_EriAlarmAlertSpecificProblem_Object((1,3,6,1,4,1,193,183,4,1,4,5,1,4),_EriAlarmAlertSpecificProblem_Type())
eriAlarmAlertSpecificProblem.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmAlertSpecificProblem.setStatus(_B)
_EriAlarmAlertManagedObject_Type=EriMO
_EriAlarmAlertManagedObject_Object=MibTableColumn
eriAlarmAlertManagedObject=_EriAlarmAlertManagedObject_Object((1,3,6,1,4,1,193,183,4,1,4,5,1,5),_EriAlarmAlertManagedObject_Type())
eriAlarmAlertManagedObject.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmAlertManagedObject.setStatus(_B)
_EriAlarmAlertEventType_Type=IANAItuEventType
_EriAlarmAlertEventType_Object=MibTableColumn
eriAlarmAlertEventType=_EriAlarmAlertEventType_Object((1,3,6,1,4,1,193,183,4,1,4,5,1,6),_EriAlarmAlertEventType_Type())
eriAlarmAlertEventType.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmAlertEventType.setStatus(_B)
_EriAlarmAlertEventTime_Type=DateAndTime
_EriAlarmAlertEventTime_Object=MibTableColumn
eriAlarmAlertEventTime=_EriAlarmAlertEventTime_Object((1,3,6,1,4,1,193,183,4,1,4,5,1,7),_EriAlarmAlertEventTime_Type())
eriAlarmAlertEventTime.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmAlertEventTime.setStatus(_B)
_EriAlarmAlertProbableCause_Type=EriProbableCause
_EriAlarmAlertProbableCause_Object=MibTableColumn
eriAlarmAlertProbableCause=_EriAlarmAlertProbableCause_Object((1,3,6,1,4,1,193,183,4,1,4,5,1,8),_EriAlarmAlertProbableCause_Type())
eriAlarmAlertProbableCause.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmAlertProbableCause.setStatus(_B)
_EriAlarmAlertSeverity_Type=ItuPerceivedSeverity
_EriAlarmAlertSeverity_Object=MibTableColumn
eriAlarmAlertSeverity=_EriAlarmAlertSeverity_Object((1,3,6,1,4,1,193,183,4,1,4,5,1,9),_EriAlarmAlertSeverity_Type())
eriAlarmAlertSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmAlertSeverity.setStatus(_B)
_EriAlarmAlertAdditionalText_Type=EriLargeAdditionalText
_EriAlarmAlertAdditionalText_Object=MibTableColumn
eriAlarmAlertAdditionalText=_EriAlarmAlertAdditionalText_Object((1,3,6,1,4,1,193,183,4,1,4,5,1,10),_EriAlarmAlertAdditionalText_Type())
eriAlarmAlertAdditionalText.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmAlertAdditionalText.setStatus(_B)
_EriAlarmAlertResourceId_Type=ResourceId
_EriAlarmAlertResourceId_Object=MibTableColumn
eriAlarmAlertResourceId=_EriAlarmAlertResourceId_Object((1,3,6,1,4,1,193,183,4,1,4,5,1,11),_EriAlarmAlertResourceId_Type())
eriAlarmAlertResourceId.setMaxAccess(_C)
if mibBuilder.loadTexts:eriAlarmAlertResourceId.setStatus(_B)
_EriAlarmHeartBeat_ObjectIdentity=ObjectIdentity
eriAlarmHeartBeat=_EriAlarmHeartBeat_ObjectIdentity((1,3,6,1,4,1,193,183,4,1,5))
_EriAlarmHbInterval_Type=Unsigned32
_EriAlarmHbInterval_Object=MibScalar
eriAlarmHbInterval=_EriAlarmHbInterval_Object((1,3,6,1,4,1,193,183,4,1,5,1),_EriAlarmHbInterval_Type())
eriAlarmHbInterval.setMaxAccess('read-write')
if mibBuilder.loadTexts:eriAlarmHbInterval.setStatus(_B)
_EriAlarmNotifications_ObjectIdentity=ObjectIdentity
eriAlarmNotifications=_EriAlarmNotifications_ObjectIdentity((1,3,6,1,4,1,193,183,4,2))
_EriAlarmNotifsPrefix_ObjectIdentity=ObjectIdentity
eriAlarmNotifsPrefix=_EriAlarmNotifsPrefix_ObjectIdentity((1,3,6,1,4,1,193,183,4,2,0))
_EriAlarmConformance_ObjectIdentity=ObjectIdentity
eriAlarmConformance=_EriAlarmConformance_ObjectIdentity((1,3,6,1,4,1,193,183,4,4))
_EriAlarmCompliances_ObjectIdentity=ObjectIdentity
eriAlarmCompliances=_EriAlarmCompliances_ObjectIdentity((1,3,6,1,4,1,193,183,4,4,1))
_EriAlarmGroups_ObjectIdentity=ObjectIdentity
eriAlarmGroups=_EriAlarmGroups_ObjectIdentity((1,3,6,1,4,1,193,183,4,4,2))
eriAlarmSummaryGroup=ObjectGroup((1,3,6,1,4,1,193,183,4,4,2,1))
eriAlarmSummaryGroup.setObjects(*((_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:eriAlarmSummaryGroup.setStatus(_B)
eriAlarmActiveAlarmsGroup=ObjectGroup((1,3,6,1,4,1,193,183,4,4,2,2))
eriAlarmActiveAlarmsGroup.setObjects(*((_A,_o),(_A,_X),(_A,_G),(_A,_Y),(_A,_H),(_A,_I),(_A,_K),(_A,_J),(_A,_L),(_A,_M),(_A,_N),(_A,_p),(_A,_q),(_A,_D),(_A,_E)))
if mibBuilder.loadTexts:eriAlarmActiveAlarmsGroup.setStatus(_B)
eriAlarmAlertsGroup=ObjectGroup((1,3,6,1,4,1,193,183,4,4,2,3))
eriAlarmAlertsGroup.setObjects(*((_A,_r),(_A,_Z),(_A,_O),(_A,_s),(_A,_P),(_A,_Q),(_A,_S),(_A,_R),(_A,_T),(_A,_U),(_A,_V),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:eriAlarmAlertsGroup.setStatus(_B)
eriAlarmHeartBeatGroup=ObjectGroup((1,3,6,1,4,1,193,183,4,4,2,4))
eriAlarmHeartBeatGroup.setObjects((_A,_v))
if mibBuilder.loadTexts:eriAlarmHeartBeatGroup.setStatus(_B)
eriAlarmSNMPResourceGroup=ObjectGroup((1,3,6,1,4,1,193,183,4,4,2,5))
eriAlarmSNMPResourceGroup.setObjects(*((_A,_a),(_A,_b)))
if mibBuilder.loadTexts:eriAlarmSNMPResourceGroup.setStatus(_B)
eriAlarmChangeAlarmGroup=ObjectGroup((1,3,6,1,4,1,193,183,4,4,2,6))
eriAlarmChangeAlarmGroup.setObjects(*((_A,_w),(_A,_x),(_A,_y),(_A,_F)))
if mibBuilder.loadTexts:eriAlarmChangeAlarmGroup.setStatus(_B)
eriAlarmIndeterminate=NotificationType((1,3,6,1,4,1,193,183,4,2,0,1))
eriAlarmIndeterminate.setObjects(*((_A,_J),(_A,_H),(_A,_I),(_A,_K),(_A,_G),(_A,_L),(_A,_M),(_A,_N),(_A,_D),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:eriAlarmIndeterminate.setStatus(_B)
eriAlarmWarning=NotificationType((1,3,6,1,4,1,193,183,4,2,0,2))
eriAlarmWarning.setObjects(*((_A,_J),(_A,_H),(_A,_I),(_A,_K),(_A,_G),(_A,_L),(_A,_M),(_A,_N),(_A,_D),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:eriAlarmWarning.setStatus(_B)
eriAlarmMinor=NotificationType((1,3,6,1,4,1,193,183,4,2,0,3))
eriAlarmMinor.setObjects(*((_A,_J),(_A,_H),(_A,_I),(_A,_K),(_A,_G),(_A,_L),(_A,_M),(_A,_N),(_A,_D),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:eriAlarmMinor.setStatus(_B)
eriAlarmMajor=NotificationType((1,3,6,1,4,1,193,183,4,2,0,4))
eriAlarmMajor.setObjects(*((_A,_J),(_A,_H),(_A,_I),(_A,_K),(_A,_G),(_A,_L),(_A,_M),(_A,_N),(_A,_D),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:eriAlarmMajor.setStatus(_B)
eriAlarmCritical=NotificationType((1,3,6,1,4,1,193,183,4,2,0,5))
eriAlarmCritical.setObjects(*((_A,_J),(_A,_H),(_A,_I),(_A,_K),(_A,_G),(_A,_L),(_A,_M),(_A,_N),(_A,_D),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:eriAlarmCritical.setStatus(_B)
eriAlarmCleared=NotificationType((1,3,6,1,4,1,193,183,4,2,0,7))
eriAlarmCleared.setObjects(*((_A,_J),(_A,_H),(_A,_I),(_A,_K),(_A,_G),(_A,_L),(_A,_M),(_A,_N),(_A,_D),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:eriAlarmCleared.setStatus(_B)
eriAlarmAppendInfo=NotificationType((1,3,6,1,4,1,193,183,4,2,0,8))
eriAlarmAppendInfo.setObjects(*((_A,_J),(_A,_H),(_A,_I),(_A,_D),(_A,_a)))
if mibBuilder.loadTexts:eriAlarmAppendInfo.setStatus(_B)
eriAlarmIndAlert=NotificationType((1,3,6,1,4,1,193,183,4,2,0,10))
eriAlarmIndAlert.setObjects(*((_A,_R),(_A,_P),(_A,_Q),(_A,_S),(_A,_O),(_A,_T),(_A,_U),(_A,_V),(_A,_D),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:eriAlarmIndAlert.setStatus(_B)
eriAlarmWarnAlert=NotificationType((1,3,6,1,4,1,193,183,4,2,0,11))
eriAlarmWarnAlert.setObjects(*((_A,_R),(_A,_P),(_A,_Q),(_A,_S),(_A,_O),(_A,_T),(_A,_U),(_A,_V),(_A,_D),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:eriAlarmWarnAlert.setStatus(_B)
eriAlarmMinorAlert=NotificationType((1,3,6,1,4,1,193,183,4,2,0,12))
eriAlarmMinorAlert.setObjects(*((_A,_R),(_A,_P),(_A,_Q),(_A,_S),(_A,_O),(_A,_T),(_A,_U),(_A,_V),(_A,_D),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:eriAlarmMinorAlert.setStatus(_B)
eriAlarmMajorAlert=NotificationType((1,3,6,1,4,1,193,183,4,2,0,13))
eriAlarmMajorAlert.setObjects(*((_A,_R),(_A,_P),(_A,_Q),(_A,_S),(_A,_O),(_A,_T),(_A,_U),(_A,_V),(_A,_D),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:eriAlarmMajorAlert.setStatus(_B)
eriAlarmCriticalAlert=NotificationType((1,3,6,1,4,1,193,183,4,2,0,14))
eriAlarmCriticalAlert.setObjects(*((_A,_R),(_A,_P),(_A,_Q),(_A,_S),(_A,_O),(_A,_T),(_A,_U),(_A,_V),(_A,_D),(_A,_F),(_A,_E)))
if mibBuilder.loadTexts:eriAlarmCriticalAlert.setStatus(_B)
eriAlarmAppendAlertInfo=NotificationType((1,3,6,1,4,1,193,183,4,2,0,15))
eriAlarmAppendAlertInfo.setObjects(*((_A,_R),(_A,_P),(_A,_Q),(_A,_D),(_A,_b)))
if mibBuilder.loadTexts:eriAlarmAppendAlertInfo.setStatus(_B)
eriAlarmHeartBeatNotif=NotificationType((1,3,6,1,4,1,193,183,4,2,0,20))
eriAlarmHeartBeatNotif.setObjects(*((_A,_G),(_A,_O),(_A,_X),(_A,_Z)))
if mibBuilder.loadTexts:eriAlarmHeartBeatNotif.setStatus(_B)
eriAlarmAlarmListRebuilt=NotificationType((1,3,6,1,4,1,193,183,4,2,0,30))
eriAlarmAlarmListRebuilt.setObjects((_A,_Y))
if mibBuilder.loadTexts:eriAlarmAlarmListRebuilt.setStatus(_B)
eriAlarmSimpleAlarmGroup=NotificationGroup((1,3,6,1,4,1,193,183,4,4,2,10))
eriAlarmSimpleAlarmGroup.setObjects(*((_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:eriAlarmSimpleAlarmGroup.setStatus(_B)
eriAlarmAddAddInfoGroup=NotificationGroup((1,3,6,1,4,1,193,183,4,4,2,12))
eriAlarmAddAddInfoGroup.setObjects(*((_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:eriAlarmAddAddInfoGroup.setStatus(_B)
eriAlarmAlertNotifGroup=NotificationGroup((1,3,6,1,4,1,193,183,4,4,2,13))
eriAlarmAlertNotifGroup.setObjects(*((_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:eriAlarmAlertNotifGroup.setStatus(_B)
eriAlarmHeartBeatNotifGroup=NotificationGroup((1,3,6,1,4,1,193,183,4,4,2,14))
eriAlarmHeartBeatNotifGroup.setObjects((_A,_AD))
if mibBuilder.loadTexts:eriAlarmHeartBeatNotifGroup.setStatus(_B)
eriAlarmBasicAlarmsCompliance=ModuleCompliance((1,3,6,1,4,1,193,183,4,4,1,1))
eriAlarmBasicAlarmsCompliance.setObjects(*((_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_e,_f),(_c,_d)))
if mibBuilder.loadTexts:eriAlarmBasicAlarmsCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'ericssonAlarmMIB':ericssonAlarmMIB,'eriAlarmObjects':eriAlarmObjects,'eriAlarmSummary':eriAlarmSummary,_j:eriAlarmSumIndeterminate,_k:eriAlarmSumCritical,_l:eriAlarmSumMajor,_m:eriAlarmSumMinor,_n:eriAlarmSumWarning,'eriAlarmNotifObjects':eriAlarmNotifObjects,_D:eriAlarmNObjAdditionalText,_F:eriAlarmNObjMoreAdditionalText,_E:eriAlarmNObjResourceId,'eriAlarmActiveAlarms':eriAlarmActiveAlarms,_o:eriAlarmActiveNumber,_X:eriAlarmActiveLastChanged,_G:eriAlarmActiveLastSequenceNo,_Y:eriAlarmActiveTableURL,'eriAlarmActiveAlarmTable':eriAlarmActiveAlarmTable,'eriAlarmActiveAlarmEntry':eriAlarmActiveAlarmEntry,_g:eriAlarmActiveIndex,_H:eriAlarmActiveMajorType,_I:eriAlarmActiveMinorType,_K:eriAlarmActiveSpecificProblem,_J:eriAlarmActiveManagedObject,_L:eriAlarmActiveEventType,_M:eriAlarmActiveEventTime,_w:eriAlarmActiveOriginalEventTime,_N:eriAlarmActiveProbableCause,_p:eriAlarmActiveSeverity,_x:eriAlarmActiveOriginalSeverity,_q:eriAlarmActiveAdditionalText,_y:eriAlarmActiveOrigAdditionalText,_a:eriAlarmActiveResourceId,'eriAlarmAlerts':eriAlarmAlerts,_r:eriAlarmAlertNumber,_Z:eriAlarmAlertLastChanged,_O:eriAlarmAlertLastSequenceNo,_s:eriAlarmAlertTableURL,'eriAlarmAlertTable':eriAlarmAlertTable,'eriAlarmAlertEntry':eriAlarmAlertEntry,_i:eriAlarmAlertIndex,_P:eriAlarmAlertMajorType,_Q:eriAlarmAlertMinorType,_S:eriAlarmAlertSpecificProblem,_R:eriAlarmAlertManagedObject,_T:eriAlarmAlertEventType,_U:eriAlarmAlertEventTime,_V:eriAlarmAlertProbableCause,_t:eriAlarmAlertSeverity,_u:eriAlarmAlertAdditionalText,_b:eriAlarmAlertResourceId,'eriAlarmHeartBeat':eriAlarmHeartBeat,_v:eriAlarmHbInterval,'eriAlarmNotifications':eriAlarmNotifications,'eriAlarmNotifsPrefix':eriAlarmNotifsPrefix,_z:eriAlarmIndeterminate,_A0:eriAlarmWarning,_A1:eriAlarmMinor,_A2:eriAlarmMajor,_A3:eriAlarmCritical,_A4:eriAlarmCleared,_A6:eriAlarmAppendInfo,_A8:eriAlarmIndAlert,_A9:eriAlarmWarnAlert,_AA:eriAlarmMinorAlert,_AB:eriAlarmMajorAlert,_AC:eriAlarmCriticalAlert,_A7:eriAlarmAppendAlertInfo,_AD:eriAlarmHeartBeatNotif,_A5:eriAlarmAlarmListRebuilt,'eriAlarmConformance':eriAlarmConformance,'eriAlarmCompliances':eriAlarmCompliances,'eriAlarmBasicAlarmsCompliance':eriAlarmBasicAlarmsCompliance,'eriAlarmGroups':eriAlarmGroups,_AE:eriAlarmSummaryGroup,_AF:eriAlarmActiveAlarmsGroup,_AJ:eriAlarmAlertsGroup,_AG:eriAlarmHeartBeatGroup,_AN:eriAlarmSNMPResourceGroup,_AL:eriAlarmChangeAlarmGroup,_AH:eriAlarmSimpleAlarmGroup,_AM:eriAlarmAddAddInfoGroup,_AK:eriAlarmAlertNotifGroup,_AI:eriAlarmHeartBeatNotifGroup})