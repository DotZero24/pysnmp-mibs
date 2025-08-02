_b='fs2544TypeOfFailure'
_a='fs2544TrapSlaId'
_Z='fs2544ContextName'
_Y='accessible-for-notify'
_X='notApplicable'
_W='fs2544ReportStatsFrameSize'
_V='fs2544SacId'
_U='fs2544TrafficProfileId'
_T='notInitiated'
_S='disable'
_R='enable'
_Q='IEEE8021PriorityCodePoint'
_P='fail'
_O='pass'
_N='fs2544SlaId'
_M='DisplayString'
_L='seconds'
_K='aborted'
_J='not-accessible'
_I='TruthValue'
_H='fs2544ContextId'
_G='percentage'
_F='Integer32'
_E='ARICENT-RFC2544-MIB'
_D='read-only'
_C='Unsigned32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IEEE8021PriorityCodePoint,=mibBuilder.importSymbols('IEEE8021-TC-MIB',_Q)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_M,'PhysAddress','RowStatus','TextualConvention','TimeStamp',_I)
fs2544=ModuleIdentity((1,3,6,1,4,1,29601,2,105))
if mibBuilder.loadTexts:fs2544.setRevisions(('2015-06-26 00:00',))
_Fs2544Context_ObjectIdentity=ObjectIdentity
fs2544Context=_Fs2544Context_ObjectIdentity((1,3,6,1,4,1,29601,2,105,1))
_Fs2544ContextTable_Object=MibTable
fs2544ContextTable=_Fs2544ContextTable_Object((1,3,6,1,4,1,29601,2,105,1,1))
if mibBuilder.loadTexts:fs2544ContextTable.setStatus(_A)
_Fs2544ContextEntry_Object=MibTableRow
fs2544ContextEntry=_Fs2544ContextEntry_Object((1,3,6,1,4,1,29601,2,105,1,1,1))
fs2544ContextEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:fs2544ContextEntry.setStatus(_A)
_Fs2544ContextId_Type=Unsigned32
_Fs2544ContextId_Object=MibTableColumn
fs2544ContextId=_Fs2544ContextId_Object((1,3,6,1,4,1,29601,2,105,1,1,1,1),_Fs2544ContextId_Type())
fs2544ContextId.setMaxAccess(_J)
if mibBuilder.loadTexts:fs2544ContextId.setStatus(_A)
_Fs2544ContextName_Type=DisplayString
_Fs2544ContextName_Object=MibTableColumn
fs2544ContextName=_Fs2544ContextName_Object((1,3,6,1,4,1,29601,2,105,1,1,1,2),_Fs2544ContextName_Type())
fs2544ContextName.setMaxAccess(_D)
if mibBuilder.loadTexts:fs2544ContextName.setStatus(_A)
class _Fs2544ContextSystemControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_Fs2544ContextSystemControl_Type.__name__=_F
_Fs2544ContextSystemControl_Object=MibTableColumn
fs2544ContextSystemControl=_Fs2544ContextSystemControl_Object((1,3,6,1,4,1,29601,2,105,1,1,1,3),_Fs2544ContextSystemControl_Type())
fs2544ContextSystemControl.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544ContextSystemControl.setStatus(_A)
class _Fs2544ContextModuleStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_Fs2544ContextModuleStatus_Type.__name__=_F
_Fs2544ContextModuleStatus_Object=MibTableColumn
fs2544ContextModuleStatus=_Fs2544ContextModuleStatus_Object((1,3,6,1,4,1,29601,2,105,1,1,1,4),_Fs2544ContextModuleStatus_Type())
fs2544ContextModuleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544ContextModuleStatus.setStatus(_A)
class _Fs2544ContextTraceOption_Type(Unsigned32):defaultValue=32;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_Fs2544ContextTraceOption_Type.__name__=_C
_Fs2544ContextTraceOption_Object=MibTableColumn
fs2544ContextTraceOption=_Fs2544ContextTraceOption_Object((1,3,6,1,4,1,29601,2,105,1,1,1,5),_Fs2544ContextTraceOption_Type())
fs2544ContextTraceOption.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544ContextTraceOption.setStatus(_A)
_Fs2544ContextNumOfTestRunning_Type=Unsigned32
_Fs2544ContextNumOfTestRunning_Object=MibTableColumn
fs2544ContextNumOfTestRunning=_Fs2544ContextNumOfTestRunning_Object((1,3,6,1,4,1,29601,2,105,1,1,1,6),_Fs2544ContextNumOfTestRunning_Type())
fs2544ContextNumOfTestRunning.setMaxAccess(_D)
if mibBuilder.loadTexts:fs2544ContextNumOfTestRunning.setStatus(_A)
class _Fs2544ContextTrapStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_Fs2544ContextTrapStatus_Type.__name__=_F
_Fs2544ContextTrapStatus_Object=MibTableColumn
fs2544ContextTrapStatus=_Fs2544ContextTrapStatus_Object((1,3,6,1,4,1,29601,2,105,1,1,1,7),_Fs2544ContextTrapStatus_Type())
fs2544ContextTrapStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544ContextTrapStatus.setStatus(_A)
_Fs2544Sla_ObjectIdentity=ObjectIdentity
fs2544Sla=_Fs2544Sla_ObjectIdentity((1,3,6,1,4,1,29601,2,105,2))
_Fs2544SlaTable_Object=MibTable
fs2544SlaTable=_Fs2544SlaTable_Object((1,3,6,1,4,1,29601,2,105,2,1))
if mibBuilder.loadTexts:fs2544SlaTable.setStatus(_A)
_Fs2544SlaEntry_Object=MibTableRow
fs2544SlaEntry=_Fs2544SlaEntry_Object((1,3,6,1,4,1,29601,2,105,2,1,1))
fs2544SlaEntry.setIndexNames((0,_E,_H),(0,_E,_N))
if mibBuilder.loadTexts:fs2544SlaEntry.setStatus(_A)
class _Fs2544SlaId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Fs2544SlaId_Type.__name__=_C
_Fs2544SlaId_Object=MibTableColumn
fs2544SlaId=_Fs2544SlaId_Object((1,3,6,1,4,1,29601,2,105,2,1,1,1),_Fs2544SlaId_Type())
fs2544SlaId.setMaxAccess(_J)
if mibBuilder.loadTexts:fs2544SlaId.setStatus(_A)
class _Fs2544SlaMEG_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_Fs2544SlaMEG_Type.__name__=_C
_Fs2544SlaMEG_Object=MibTableColumn
fs2544SlaMEG=_Fs2544SlaMEG_Object((1,3,6,1,4,1,29601,2,105,2,1,1,2),_Fs2544SlaMEG_Type())
fs2544SlaMEG.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544SlaMEG.setStatus(_A)
class _Fs2544SlaME_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_Fs2544SlaME_Type.__name__=_C
_Fs2544SlaME_Object=MibTableColumn
fs2544SlaME=_Fs2544SlaME_Object((1,3,6,1,4,1,29601,2,105,2,1,1,3),_Fs2544SlaME_Type())
fs2544SlaME.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544SlaME.setStatus(_A)
class _Fs2544SlaMEP_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8191))
_Fs2544SlaMEP_Type.__name__=_C
_Fs2544SlaMEP_Object=MibTableColumn
fs2544SlaMEP=_Fs2544SlaMEP_Object((1,3,6,1,4,1,29601,2,105,2,1,1,4),_Fs2544SlaMEP_Type())
fs2544SlaMEP.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544SlaMEP.setStatus(_A)
class _Fs2544SlaTrafficProfileId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_Fs2544SlaTrafficProfileId_Type.__name__=_C
_Fs2544SlaTrafficProfileId_Object=MibTableColumn
fs2544SlaTrafficProfileId=_Fs2544SlaTrafficProfileId_Object((1,3,6,1,4,1,29601,2,105,2,1,1,5),_Fs2544SlaTrafficProfileId_Type())
fs2544SlaTrafficProfileId.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544SlaTrafficProfileId.setStatus(_A)
class _Fs2544SlaSacId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_Fs2544SlaSacId_Type.__name__=_C
_Fs2544SlaSacId_Object=MibTableColumn
fs2544SlaSacId=_Fs2544SlaSacId_Object((1,3,6,1,4,1,29601,2,105,2,1,1,6),_Fs2544SlaSacId_Type())
fs2544SlaSacId.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544SlaSacId.setStatus(_A)
class _Fs2544SlaTestStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('stop',2)))
_Fs2544SlaTestStatus_Type.__name__=_F
_Fs2544SlaTestStatus_Object=MibTableColumn
fs2544SlaTestStatus=_Fs2544SlaTestStatus_Object((1,3,6,1,4,1,29601,2,105,2,1,1,7),_Fs2544SlaTestStatus_Type())
fs2544SlaTestStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544SlaTestStatus.setStatus(_A)
class _Fs2544SlaCurrentTestState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_T,1),('inProgress',2),('completed',3),(_K,4)))
_Fs2544SlaCurrentTestState_Type.__name__=_F
_Fs2544SlaCurrentTestState_Object=MibTableColumn
fs2544SlaCurrentTestState=_Fs2544SlaCurrentTestState_Object((1,3,6,1,4,1,29601,2,105,2,1,1,8),_Fs2544SlaCurrentTestState_Type())
fs2544SlaCurrentTestState.setMaxAccess(_D)
if mibBuilder.loadTexts:fs2544SlaCurrentTestState.setStatus(_A)
_Fs2544SlaTestStartTime_Type=TimeStamp
_Fs2544SlaTestStartTime_Object=MibTableColumn
fs2544SlaTestStartTime=_Fs2544SlaTestStartTime_Object((1,3,6,1,4,1,29601,2,105,2,1,1,9),_Fs2544SlaTestStartTime_Type())
fs2544SlaTestStartTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fs2544SlaTestStartTime.setStatus(_A)
_Fs2544SlaTestEndTime_Type=TimeStamp
_Fs2544SlaTestEndTime_Object=MibTableColumn
fs2544SlaTestEndTime=_Fs2544SlaTestEndTime_Object((1,3,6,1,4,1,29601,2,105,2,1,1,10),_Fs2544SlaTestEndTime_Type())
fs2544SlaTestEndTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fs2544SlaTestEndTime.setStatus(_A)
_Fs2544SlaRowStatus_Type=RowStatus
_Fs2544SlaRowStatus_Object=MibTableColumn
fs2544SlaRowStatus=_Fs2544SlaRowStatus_Object((1,3,6,1,4,1,29601,2,105,2,1,1,11),_Fs2544SlaRowStatus_Type())
fs2544SlaRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544SlaRowStatus.setStatus(_A)
_Fs2544TrafficProfile_ObjectIdentity=ObjectIdentity
fs2544TrafficProfile=_Fs2544TrafficProfile_ObjectIdentity((1,3,6,1,4,1,29601,2,105,3))
_Fs2544TrafficProfileTable_Object=MibTable
fs2544TrafficProfileTable=_Fs2544TrafficProfileTable_Object((1,3,6,1,4,1,29601,2,105,3,1))
if mibBuilder.loadTexts:fs2544TrafficProfileTable.setStatus(_A)
_Fs2544TrafficProfileEntry_Object=MibTableRow
fs2544TrafficProfileEntry=_Fs2544TrafficProfileEntry_Object((1,3,6,1,4,1,29601,2,105,3,1,1))
fs2544TrafficProfileEntry.setIndexNames((0,_E,_H),(0,_E,_U))
if mibBuilder.loadTexts:fs2544TrafficProfileEntry.setStatus(_A)
class _Fs2544TrafficProfileId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_Fs2544TrafficProfileId_Type.__name__=_C
_Fs2544TrafficProfileId_Object=MibTableColumn
fs2544TrafficProfileId=_Fs2544TrafficProfileId_Object((1,3,6,1,4,1,29601,2,105,3,1,1,1),_Fs2544TrafficProfileId_Type())
fs2544TrafficProfileId.setMaxAccess(_J)
if mibBuilder.loadTexts:fs2544TrafficProfileId.setStatus(_A)
class _Fs2544TrafficProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Fs2544TrafficProfileName_Type.__name__=_M
_Fs2544TrafficProfileName_Object=MibTableColumn
fs2544TrafficProfileName=_Fs2544TrafficProfileName_Object((1,3,6,1,4,1,29601,2,105,3,1,1,2),_Fs2544TrafficProfileName_Type())
fs2544TrafficProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544TrafficProfileName.setStatus(_A)
class _Fs2544TrafficProfileSeqNoCheck_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_R,1),(_S,2)))
_Fs2544TrafficProfileSeqNoCheck_Type.__name__=_F
_Fs2544TrafficProfileSeqNoCheck_Object=MibTableColumn
fs2544TrafficProfileSeqNoCheck=_Fs2544TrafficProfileSeqNoCheck_Object((1,3,6,1,4,1,29601,2,105,3,1,1,3),_Fs2544TrafficProfileSeqNoCheck_Type())
fs2544TrafficProfileSeqNoCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544TrafficProfileSeqNoCheck.setStatus(_A)
class _Fs2544TrafficProfileDwellTime_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,60))
_Fs2544TrafficProfileDwellTime_Type.__name__=_F
_Fs2544TrafficProfileDwellTime_Object=MibTableColumn
fs2544TrafficProfileDwellTime=_Fs2544TrafficProfileDwellTime_Object((1,3,6,1,4,1,29601,2,105,3,1,1,4),_Fs2544TrafficProfileDwellTime_Type())
fs2544TrafficProfileDwellTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544TrafficProfileDwellTime.setStatus(_A)
_Fs2544TrafficProfileFrameSize_Type=DisplayString
_Fs2544TrafficProfileFrameSize_Object=MibTableColumn
fs2544TrafficProfileFrameSize=_Fs2544TrafficProfileFrameSize_Object((1,3,6,1,4,1,29601,2,105,3,1,1,5),_Fs2544TrafficProfileFrameSize_Type())
fs2544TrafficProfileFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544TrafficProfileFrameSize.setStatus(_A)
class _Fs2544TrafficProfilePCP_Type(IEEE8021PriorityCodePoint):defaultValue=1
_Fs2544TrafficProfilePCP_Type.__name__=_Q
_Fs2544TrafficProfilePCP_Object=MibTableColumn
fs2544TrafficProfilePCP=_Fs2544TrafficProfilePCP_Object((1,3,6,1,4,1,29601,2,105,3,1,1,6),_Fs2544TrafficProfilePCP_Type())
fs2544TrafficProfilePCP.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544TrafficProfilePCP.setStatus(_A)
class _Fs2544TrafficProfileThTestStatus_Type(TruthValue):defaultValue=1
_Fs2544TrafficProfileThTestStatus_Type.__name__=_I
_Fs2544TrafficProfileThTestStatus_Object=MibTableColumn
fs2544TrafficProfileThTestStatus=_Fs2544TrafficProfileThTestStatus_Object((1,3,6,1,4,1,29601,2,105,3,1,1,7),_Fs2544TrafficProfileThTestStatus_Type())
fs2544TrafficProfileThTestStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544TrafficProfileThTestStatus.setStatus(_A)
class _Fs2544TrafficProfileFlTestStatus_Type(TruthValue):defaultValue=2
_Fs2544TrafficProfileFlTestStatus_Type.__name__=_I
_Fs2544TrafficProfileFlTestStatus_Object=MibTableColumn
fs2544TrafficProfileFlTestStatus=_Fs2544TrafficProfileFlTestStatus_Object((1,3,6,1,4,1,29601,2,105,3,1,1,8),_Fs2544TrafficProfileFlTestStatus_Type())
fs2544TrafficProfileFlTestStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544TrafficProfileFlTestStatus.setStatus(_A)
class _Fs2544TrafficProfileLaTestStatus_Type(TruthValue):defaultValue=1
_Fs2544TrafficProfileLaTestStatus_Type.__name__=_I
_Fs2544TrafficProfileLaTestStatus_Object=MibTableColumn
fs2544TrafficProfileLaTestStatus=_Fs2544TrafficProfileLaTestStatus_Object((1,3,6,1,4,1,29601,2,105,3,1,1,9),_Fs2544TrafficProfileLaTestStatus_Type())
fs2544TrafficProfileLaTestStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544TrafficProfileLaTestStatus.setStatus(_A)
class _Fs2544TrafficProfileBbTestStatus_Type(TruthValue):defaultValue=2
_Fs2544TrafficProfileBbTestStatus_Type.__name__=_I
_Fs2544TrafficProfileBbTestStatus_Object=MibTableColumn
fs2544TrafficProfileBbTestStatus=_Fs2544TrafficProfileBbTestStatus_Object((1,3,6,1,4,1,29601,2,105,3,1,1,10),_Fs2544TrafficProfileBbTestStatus_Type())
fs2544TrafficProfileBbTestStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544TrafficProfileBbTestStatus.setStatus(_A)
class _Fs2544TrafficProfileThTrialDuration_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1800))
_Fs2544TrafficProfileThTrialDuration_Type.__name__=_C
_Fs2544TrafficProfileThTrialDuration_Object=MibTableColumn
fs2544TrafficProfileThTrialDuration=_Fs2544TrafficProfileThTrialDuration_Object((1,3,6,1,4,1,29601,2,105,3,1,1,11),_Fs2544TrafficProfileThTrialDuration_Type())
fs2544TrafficProfileThTrialDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544TrafficProfileThTrialDuration.setStatus(_A)
if mibBuilder.loadTexts:fs2544TrafficProfileThTrialDuration.setUnits(_L)
class _Fs2544TrafficProfileThMaxRate_Type(Unsigned32):defaultValue=100
_Fs2544TrafficProfileThMaxRate_Type.__name__=_C
_Fs2544TrafficProfileThMaxRate_Object=MibTableColumn
fs2544TrafficProfileThMaxRate=_Fs2544TrafficProfileThMaxRate_Object((1,3,6,1,4,1,29601,2,105,3,1,1,12),_Fs2544TrafficProfileThMaxRate_Type())
fs2544TrafficProfileThMaxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544TrafficProfileThMaxRate.setStatus(_A)
if mibBuilder.loadTexts:fs2544TrafficProfileThMaxRate.setUnits(_G)
class _Fs2544TrafficProfileThMinRate_Type(Unsigned32):defaultValue=80
_Fs2544TrafficProfileThMinRate_Type.__name__=_C
_Fs2544TrafficProfileThMinRate_Object=MibTableColumn
fs2544TrafficProfileThMinRate=_Fs2544TrafficProfileThMinRate_Object((1,3,6,1,4,1,29601,2,105,3,1,1,13),_Fs2544TrafficProfileThMinRate_Type())
fs2544TrafficProfileThMinRate.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544TrafficProfileThMinRate.setStatus(_A)
if mibBuilder.loadTexts:fs2544TrafficProfileThMinRate.setUnits(_G)
class _Fs2544TrafficProfileLaTrialDuration_Type(Unsigned32):defaultValue=120;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1800))
_Fs2544TrafficProfileLaTrialDuration_Type.__name__=_C
_Fs2544TrafficProfileLaTrialDuration_Object=MibTableColumn
fs2544TrafficProfileLaTrialDuration=_Fs2544TrafficProfileLaTrialDuration_Object((1,3,6,1,4,1,29601,2,105,3,1,1,14),_Fs2544TrafficProfileLaTrialDuration_Type())
fs2544TrafficProfileLaTrialDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544TrafficProfileLaTrialDuration.setStatus(_A)
if mibBuilder.loadTexts:fs2544TrafficProfileLaTrialDuration.setUnits(_L)
class _Fs2544TrafficProfileLaDelayMeasureInterval_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_Fs2544TrafficProfileLaDelayMeasureInterval_Type.__name__=_C
_Fs2544TrafficProfileLaDelayMeasureInterval_Object=MibTableColumn
fs2544TrafficProfileLaDelayMeasureInterval=_Fs2544TrafficProfileLaDelayMeasureInterval_Object((1,3,6,1,4,1,29601,2,105,3,1,1,15),_Fs2544TrafficProfileLaDelayMeasureInterval_Type())
fs2544TrafficProfileLaDelayMeasureInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544TrafficProfileLaDelayMeasureInterval.setStatus(_A)
if mibBuilder.loadTexts:fs2544TrafficProfileLaDelayMeasureInterval.setUnits(_L)
class _Fs2544TrafficProfileFlTrialDuration_Type(Unsigned32):defaultValue=60;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,1800))
_Fs2544TrafficProfileFlTrialDuration_Type.__name__=_C
_Fs2544TrafficProfileFlTrialDuration_Object=MibTableColumn
fs2544TrafficProfileFlTrialDuration=_Fs2544TrafficProfileFlTrialDuration_Object((1,3,6,1,4,1,29601,2,105,3,1,1,16),_Fs2544TrafficProfileFlTrialDuration_Type())
fs2544TrafficProfileFlTrialDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544TrafficProfileFlTrialDuration.setStatus(_A)
if mibBuilder.loadTexts:fs2544TrafficProfileFlTrialDuration.setUnits(_L)
class _Fs2544TrafficProfileFlMaxRate_Type(Unsigned32):defaultValue=100
_Fs2544TrafficProfileFlMaxRate_Type.__name__=_C
_Fs2544TrafficProfileFlMaxRate_Object=MibTableColumn
fs2544TrafficProfileFlMaxRate=_Fs2544TrafficProfileFlMaxRate_Object((1,3,6,1,4,1,29601,2,105,3,1,1,17),_Fs2544TrafficProfileFlMaxRate_Type())
fs2544TrafficProfileFlMaxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544TrafficProfileFlMaxRate.setStatus(_A)
if mibBuilder.loadTexts:fs2544TrafficProfileFlMaxRate.setUnits(_G)
class _Fs2544TrafficProfileFlMinRate_Type(Unsigned32):defaultValue=80
_Fs2544TrafficProfileFlMinRate_Type.__name__=_C
_Fs2544TrafficProfileFlMinRate_Object=MibTableColumn
fs2544TrafficProfileFlMinRate=_Fs2544TrafficProfileFlMinRate_Object((1,3,6,1,4,1,29601,2,105,3,1,1,18),_Fs2544TrafficProfileFlMinRate_Type())
fs2544TrafficProfileFlMinRate.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544TrafficProfileFlMinRate.setStatus(_A)
if mibBuilder.loadTexts:fs2544TrafficProfileFlMinRate.setUnits(_G)
class _Fs2544TrafficProfileFlRateStep_Type(Unsigned32):defaultValue=10
_Fs2544TrafficProfileFlRateStep_Type.__name__=_C
_Fs2544TrafficProfileFlRateStep_Object=MibTableColumn
fs2544TrafficProfileFlRateStep=_Fs2544TrafficProfileFlRateStep_Object((1,3,6,1,4,1,29601,2,105,3,1,1,19),_Fs2544TrafficProfileFlRateStep_Type())
fs2544TrafficProfileFlRateStep.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544TrafficProfileFlRateStep.setStatus(_A)
if mibBuilder.loadTexts:fs2544TrafficProfileFlRateStep.setUnits(_G)
class _Fs2544TrafficProfileBbTrialDuration_Type(Unsigned32):defaultValue=2000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,10000))
_Fs2544TrafficProfileBbTrialDuration_Type.__name__=_C
_Fs2544TrafficProfileBbTrialDuration_Object=MibTableColumn
fs2544TrafficProfileBbTrialDuration=_Fs2544TrafficProfileBbTrialDuration_Object((1,3,6,1,4,1,29601,2,105,3,1,1,20),_Fs2544TrafficProfileBbTrialDuration_Type())
fs2544TrafficProfileBbTrialDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544TrafficProfileBbTrialDuration.setStatus(_A)
if mibBuilder.loadTexts:fs2544TrafficProfileBbTrialDuration.setUnits('milliseconds')
class _Fs2544TrafficProfileBbTrialCount_Type(Unsigned32):defaultValue=50;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_Fs2544TrafficProfileBbTrialCount_Type.__name__=_C
_Fs2544TrafficProfileBbTrialCount_Object=MibTableColumn
fs2544TrafficProfileBbTrialCount=_Fs2544TrafficProfileBbTrialCount_Object((1,3,6,1,4,1,29601,2,105,3,1,1,21),_Fs2544TrafficProfileBbTrialCount_Type())
fs2544TrafficProfileBbTrialCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544TrafficProfileBbTrialCount.setStatus(_A)
class _Fs2544TrafficProfileThRateStep_Type(Unsigned32):defaultValue=10
_Fs2544TrafficProfileThRateStep_Type.__name__=_C
_Fs2544TrafficProfileThRateStep_Object=MibTableColumn
fs2544TrafficProfileThRateStep=_Fs2544TrafficProfileThRateStep_Object((1,3,6,1,4,1,29601,2,105,3,1,1,22),_Fs2544TrafficProfileThRateStep_Type())
fs2544TrafficProfileThRateStep.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544TrafficProfileThRateStep.setStatus(_A)
if mibBuilder.loadTexts:fs2544TrafficProfileThRateStep.setUnits(_G)
_Fs2544TrafficProfileRowStatus_Type=RowStatus
_Fs2544TrafficProfileRowStatus_Object=MibTableColumn
fs2544TrafficProfileRowStatus=_Fs2544TrafficProfileRowStatus_Object((1,3,6,1,4,1,29601,2,105,3,1,1,23),_Fs2544TrafficProfileRowStatus_Type())
fs2544TrafficProfileRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544TrafficProfileRowStatus.setStatus(_A)
_Fs2544Sac_ObjectIdentity=ObjectIdentity
fs2544Sac=_Fs2544Sac_ObjectIdentity((1,3,6,1,4,1,29601,2,105,4))
_Fs2544SacTable_Object=MibTable
fs2544SacTable=_Fs2544SacTable_Object((1,3,6,1,4,1,29601,2,105,4,1))
if mibBuilder.loadTexts:fs2544SacTable.setStatus(_A)
_Fs2544SacEntry_Object=MibTableRow
fs2544SacEntry=_Fs2544SacEntry_Object((1,3,6,1,4,1,29601,2,105,4,1,1))
fs2544SacEntry.setIndexNames((0,_E,_H),(0,_E,_V))
if mibBuilder.loadTexts:fs2544SacEntry.setStatus(_A)
class _Fs2544SacId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_Fs2544SacId_Type.__name__=_C
_Fs2544SacId_Object=MibTableColumn
fs2544SacId=_Fs2544SacId_Object((1,3,6,1,4,1,29601,2,105,4,1,1,1),_Fs2544SacId_Type())
fs2544SacId.setMaxAccess(_J)
if mibBuilder.loadTexts:fs2544SacId.setStatus(_A)
class _Fs2544SacThAllowedFrameLoss_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Fs2544SacThAllowedFrameLoss_Type.__name__=_C
_Fs2544SacThAllowedFrameLoss_Object=MibTableColumn
fs2544SacThAllowedFrameLoss=_Fs2544SacThAllowedFrameLoss_Object((1,3,6,1,4,1,29601,2,105,4,1,1,2),_Fs2544SacThAllowedFrameLoss_Type())
fs2544SacThAllowedFrameLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544SacThAllowedFrameLoss.setStatus(_A)
if mibBuilder.loadTexts:fs2544SacThAllowedFrameLoss.setUnits(_G)
class _Fs2544SacLaAllowedFrameLoss_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_Fs2544SacLaAllowedFrameLoss_Type.__name__=_C
_Fs2544SacLaAllowedFrameLoss_Object=MibTableColumn
fs2544SacLaAllowedFrameLoss=_Fs2544SacLaAllowedFrameLoss_Object((1,3,6,1,4,1,29601,2,105,4,1,1,3),_Fs2544SacLaAllowedFrameLoss_Type())
fs2544SacLaAllowedFrameLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544SacLaAllowedFrameLoss.setStatus(_A)
if mibBuilder.loadTexts:fs2544SacLaAllowedFrameLoss.setUnits(_G)
class _Fs2544SacFlAllowedFrameLoss_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_Fs2544SacFlAllowedFrameLoss_Type.__name__=_C
_Fs2544SacFlAllowedFrameLoss_Object=MibTableColumn
fs2544SacFlAllowedFrameLoss=_Fs2544SacFlAllowedFrameLoss_Object((1,3,6,1,4,1,29601,2,105,4,1,1,4),_Fs2544SacFlAllowedFrameLoss_Type())
fs2544SacFlAllowedFrameLoss.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544SacFlAllowedFrameLoss.setStatus(_A)
if mibBuilder.loadTexts:fs2544SacFlAllowedFrameLoss.setUnits(_G)
_Fs2544SacRowStatus_Type=RowStatus
_Fs2544SacRowStatus_Object=MibTableColumn
fs2544SacRowStatus=_Fs2544SacRowStatus_Object((1,3,6,1,4,1,29601,2,105,4,1,1,5),_Fs2544SacRowStatus_Type())
fs2544SacRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fs2544SacRowStatus.setStatus(_A)
_Fs2544Statistics_ObjectIdentity=ObjectIdentity
fs2544Statistics=_Fs2544Statistics_ObjectIdentity((1,3,6,1,4,1,29601,2,105,5))
_Fs2544ReportStatsTable_Object=MibTable
fs2544ReportStatsTable=_Fs2544ReportStatsTable_Object((1,3,6,1,4,1,29601,2,105,5,1))
if mibBuilder.loadTexts:fs2544ReportStatsTable.setStatus(_A)
_Fs2544ReportStatsEntry_Object=MibTableRow
fs2544ReportStatsEntry=_Fs2544ReportStatsEntry_Object((1,3,6,1,4,1,29601,2,105,5,1,1))
fs2544ReportStatsEntry.setIndexNames((0,_E,_H),(0,_E,_N),(0,_E,_W))
if mibBuilder.loadTexts:fs2544ReportStatsEntry.setStatus(_A)
class _Fs2544ReportStatsFrameSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,1518))
_Fs2544ReportStatsFrameSize_Type.__name__=_C
_Fs2544ReportStatsFrameSize_Object=MibTableColumn
fs2544ReportStatsFrameSize=_Fs2544ReportStatsFrameSize_Object((1,3,6,1,4,1,29601,2,105,5,1,1,1),_Fs2544ReportStatsFrameSize_Type())
fs2544ReportStatsFrameSize.setMaxAccess(_J)
if mibBuilder.loadTexts:fs2544ReportStatsFrameSize.setStatus(_A)
_Fs2544ReportStatsThVerifiedBps_Type=Unsigned32
_Fs2544ReportStatsThVerifiedBps_Object=MibTableColumn
fs2544ReportStatsThVerifiedBps=_Fs2544ReportStatsThVerifiedBps_Object((1,3,6,1,4,1,29601,2,105,5,1,1,2),_Fs2544ReportStatsThVerifiedBps_Type())
fs2544ReportStatsThVerifiedBps.setMaxAccess(_D)
if mibBuilder.loadTexts:fs2544ReportStatsThVerifiedBps.setStatus(_A)
class _Fs2544ReportStatsThResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_P,2),(_T,3),(_K,4)))
_Fs2544ReportStatsThResult_Type.__name__=_F
_Fs2544ReportStatsThResult_Object=MibTableColumn
fs2544ReportStatsThResult=_Fs2544ReportStatsThResult_Object((1,3,6,1,4,1,29601,2,105,5,1,1,3),_Fs2544ReportStatsThResult_Type())
fs2544ReportStatsThResult.setMaxAccess(_D)
if mibBuilder.loadTexts:fs2544ReportStatsThResult.setStatus(_A)
_Fs2544ReportStatsLatencyMin_Type=Unsigned32
_Fs2544ReportStatsLatencyMin_Object=MibTableColumn
fs2544ReportStatsLatencyMin=_Fs2544ReportStatsLatencyMin_Object((1,3,6,1,4,1,29601,2,105,5,1,1,4),_Fs2544ReportStatsLatencyMin_Type())
fs2544ReportStatsLatencyMin.setMaxAccess(_D)
if mibBuilder.loadTexts:fs2544ReportStatsLatencyMin.setStatus(_A)
_Fs2544ReportStatsLatencyMax_Type=Unsigned32
_Fs2544ReportStatsLatencyMax_Object=MibTableColumn
fs2544ReportStatsLatencyMax=_Fs2544ReportStatsLatencyMax_Object((1,3,6,1,4,1,29601,2,105,5,1,1,5),_Fs2544ReportStatsLatencyMax_Type())
fs2544ReportStatsLatencyMax.setMaxAccess(_D)
if mibBuilder.loadTexts:fs2544ReportStatsLatencyMax.setStatus(_A)
_Fs2544ReportStatsLatencyMean_Type=Unsigned32
_Fs2544ReportStatsLatencyMean_Object=MibTableColumn
fs2544ReportStatsLatencyMean=_Fs2544ReportStatsLatencyMean_Object((1,3,6,1,4,1,29601,2,105,5,1,1,6),_Fs2544ReportStatsLatencyMean_Type())
fs2544ReportStatsLatencyMean.setMaxAccess(_D)
if mibBuilder.loadTexts:fs2544ReportStatsLatencyMean.setStatus(_A)
_Fs2544ReportStatsLatencyFailCount_Type=Integer32
_Fs2544ReportStatsLatencyFailCount_Object=MibTableColumn
fs2544ReportStatsLatencyFailCount=_Fs2544ReportStatsLatencyFailCount_Object((1,3,6,1,4,1,29601,2,105,5,1,1,7),_Fs2544ReportStatsLatencyFailCount_Type())
fs2544ReportStatsLatencyFailCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fs2544ReportStatsLatencyFailCount.setStatus(_A)
_Fs2544ReportStatsLaIterationCalculated_Type=Integer32
_Fs2544ReportStatsLaIterationCalculated_Object=MibTableColumn
fs2544ReportStatsLaIterationCalculated=_Fs2544ReportStatsLaIterationCalculated_Object((1,3,6,1,4,1,29601,2,105,5,1,1,8),_Fs2544ReportStatsLaIterationCalculated_Type())
fs2544ReportStatsLaIterationCalculated.setMaxAccess(_D)
if mibBuilder.loadTexts:fs2544ReportStatsLaIterationCalculated.setStatus(_A)
class _Fs2544ReportStatsLatencyResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_P,2),(_X,3),(_K,4)))
_Fs2544ReportStatsLatencyResult_Type.__name__=_F
_Fs2544ReportStatsLatencyResult_Object=MibTableColumn
fs2544ReportStatsLatencyResult=_Fs2544ReportStatsLatencyResult_Object((1,3,6,1,4,1,29601,2,105,5,1,1,9),_Fs2544ReportStatsLatencyResult_Type())
fs2544ReportStatsLatencyResult.setMaxAccess(_D)
if mibBuilder.loadTexts:fs2544ReportStatsLatencyResult.setStatus(_A)
_Fs2544ReportStatsFLossRate_Type=Integer32
_Fs2544ReportStatsFLossRate_Object=MibTableColumn
fs2544ReportStatsFLossRate=_Fs2544ReportStatsFLossRate_Object((1,3,6,1,4,1,29601,2,105,5,1,1,10),_Fs2544ReportStatsFLossRate_Type())
fs2544ReportStatsFLossRate.setMaxAccess(_D)
if mibBuilder.loadTexts:fs2544ReportStatsFLossRate.setStatus(_A)
class _Fs2544ReportStatsFLResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_O,1),(_P,2),(_X,3),(_K,4)))
_Fs2544ReportStatsFLResult_Type.__name__=_F
_Fs2544ReportStatsFLResult_Object=MibTableColumn
fs2544ReportStatsFLResult=_Fs2544ReportStatsFLResult_Object((1,3,6,1,4,1,29601,2,105,5,1,1,11),_Fs2544ReportStatsFLResult_Type())
fs2544ReportStatsFLResult.setMaxAccess(_D)
if mibBuilder.loadTexts:fs2544ReportStatsFLResult.setStatus(_A)
_Fs2544ReportStatsBacktoBackBurstSize_Type=Integer32
_Fs2544ReportStatsBacktoBackBurstSize_Object=MibTableColumn
fs2544ReportStatsBacktoBackBurstSize=_Fs2544ReportStatsBacktoBackBurstSize_Object((1,3,6,1,4,1,29601,2,105,5,1,1,12),_Fs2544ReportStatsBacktoBackBurstSize_Type())
fs2544ReportStatsBacktoBackBurstSize.setMaxAccess(_D)
if mibBuilder.loadTexts:fs2544ReportStatsBacktoBackBurstSize.setStatus(_A)
_Fs2544Notification_ObjectIdentity=ObjectIdentity
fs2544Notification=_Fs2544Notification_ObjectIdentity((1,3,6,1,4,1,29601,2,105,6))
_Fs2544Traps_ObjectIdentity=ObjectIdentity
fs2544Traps=_Fs2544Traps_ObjectIdentity((1,3,6,1,4,1,29601,2,105,6,0))
_Fs2544TrapObjects_ObjectIdentity=ObjectIdentity
fs2544TrapObjects=_Fs2544TrapObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,105,6,1))
_Fs2544TrapSlaId_Type=TruthValue
_Fs2544TrapSlaId_Object=MibScalar
fs2544TrapSlaId=_Fs2544TrapSlaId_Object((1,3,6,1,4,1,29601,2,105,6,1,2),_Fs2544TrapSlaId_Type())
fs2544TrapSlaId.setMaxAccess(_Y)
if mibBuilder.loadTexts:fs2544TrapSlaId.setStatus(_A)
class _Fs2544TypeOfFailure_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Fs2544TypeOfFailure_Type.__name__=_M
_Fs2544TypeOfFailure_Object=MibScalar
fs2544TypeOfFailure=_Fs2544TypeOfFailure_Object((1,3,6,1,4,1,29601,2,105,6,1,3),_Fs2544TypeOfFailure_Type())
fs2544TypeOfFailure.setMaxAccess(_Y)
if mibBuilder.loadTexts:fs2544TypeOfFailure.setStatus(_A)
fs2544FailureTrap=NotificationType((1,3,6,1,4,1,29601,2,105,6,0,1))
fs2544FailureTrap.setObjects(*((_E,_Z),(_E,_a),(_E,_b)))
if mibBuilder.loadTexts:fs2544FailureTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'fs2544':fs2544,'fs2544Context':fs2544Context,'fs2544ContextTable':fs2544ContextTable,'fs2544ContextEntry':fs2544ContextEntry,_H:fs2544ContextId,_Z:fs2544ContextName,'fs2544ContextSystemControl':fs2544ContextSystemControl,'fs2544ContextModuleStatus':fs2544ContextModuleStatus,'fs2544ContextTraceOption':fs2544ContextTraceOption,'fs2544ContextNumOfTestRunning':fs2544ContextNumOfTestRunning,'fs2544ContextTrapStatus':fs2544ContextTrapStatus,'fs2544Sla':fs2544Sla,'fs2544SlaTable':fs2544SlaTable,'fs2544SlaEntry':fs2544SlaEntry,_N:fs2544SlaId,'fs2544SlaMEG':fs2544SlaMEG,'fs2544SlaME':fs2544SlaME,'fs2544SlaMEP':fs2544SlaMEP,'fs2544SlaTrafficProfileId':fs2544SlaTrafficProfileId,'fs2544SlaSacId':fs2544SlaSacId,'fs2544SlaTestStatus':fs2544SlaTestStatus,'fs2544SlaCurrentTestState':fs2544SlaCurrentTestState,'fs2544SlaTestStartTime':fs2544SlaTestStartTime,'fs2544SlaTestEndTime':fs2544SlaTestEndTime,'fs2544SlaRowStatus':fs2544SlaRowStatus,'fs2544TrafficProfile':fs2544TrafficProfile,'fs2544TrafficProfileTable':fs2544TrafficProfileTable,'fs2544TrafficProfileEntry':fs2544TrafficProfileEntry,_U:fs2544TrafficProfileId,'fs2544TrafficProfileName':fs2544TrafficProfileName,'fs2544TrafficProfileSeqNoCheck':fs2544TrafficProfileSeqNoCheck,'fs2544TrafficProfileDwellTime':fs2544TrafficProfileDwellTime,'fs2544TrafficProfileFrameSize':fs2544TrafficProfileFrameSize,'fs2544TrafficProfilePCP':fs2544TrafficProfilePCP,'fs2544TrafficProfileThTestStatus':fs2544TrafficProfileThTestStatus,'fs2544TrafficProfileFlTestStatus':fs2544TrafficProfileFlTestStatus,'fs2544TrafficProfileLaTestStatus':fs2544TrafficProfileLaTestStatus,'fs2544TrafficProfileBbTestStatus':fs2544TrafficProfileBbTestStatus,'fs2544TrafficProfileThTrialDuration':fs2544TrafficProfileThTrialDuration,'fs2544TrafficProfileThMaxRate':fs2544TrafficProfileThMaxRate,'fs2544TrafficProfileThMinRate':fs2544TrafficProfileThMinRate,'fs2544TrafficProfileLaTrialDuration':fs2544TrafficProfileLaTrialDuration,'fs2544TrafficProfileLaDelayMeasureInterval':fs2544TrafficProfileLaDelayMeasureInterval,'fs2544TrafficProfileFlTrialDuration':fs2544TrafficProfileFlTrialDuration,'fs2544TrafficProfileFlMaxRate':fs2544TrafficProfileFlMaxRate,'fs2544TrafficProfileFlMinRate':fs2544TrafficProfileFlMinRate,'fs2544TrafficProfileFlRateStep':fs2544TrafficProfileFlRateStep,'fs2544TrafficProfileBbTrialDuration':fs2544TrafficProfileBbTrialDuration,'fs2544TrafficProfileBbTrialCount':fs2544TrafficProfileBbTrialCount,'fs2544TrafficProfileThRateStep':fs2544TrafficProfileThRateStep,'fs2544TrafficProfileRowStatus':fs2544TrafficProfileRowStatus,'fs2544Sac':fs2544Sac,'fs2544SacTable':fs2544SacTable,'fs2544SacEntry':fs2544SacEntry,_V:fs2544SacId,'fs2544SacThAllowedFrameLoss':fs2544SacThAllowedFrameLoss,'fs2544SacLaAllowedFrameLoss':fs2544SacLaAllowedFrameLoss,'fs2544SacFlAllowedFrameLoss':fs2544SacFlAllowedFrameLoss,'fs2544SacRowStatus':fs2544SacRowStatus,'fs2544Statistics':fs2544Statistics,'fs2544ReportStatsTable':fs2544ReportStatsTable,'fs2544ReportStatsEntry':fs2544ReportStatsEntry,_W:fs2544ReportStatsFrameSize,'fs2544ReportStatsThVerifiedBps':fs2544ReportStatsThVerifiedBps,'fs2544ReportStatsThResult':fs2544ReportStatsThResult,'fs2544ReportStatsLatencyMin':fs2544ReportStatsLatencyMin,'fs2544ReportStatsLatencyMax':fs2544ReportStatsLatencyMax,'fs2544ReportStatsLatencyMean':fs2544ReportStatsLatencyMean,'fs2544ReportStatsLatencyFailCount':fs2544ReportStatsLatencyFailCount,'fs2544ReportStatsLaIterationCalculated':fs2544ReportStatsLaIterationCalculated,'fs2544ReportStatsLatencyResult':fs2544ReportStatsLatencyResult,'fs2544ReportStatsFLossRate':fs2544ReportStatsFLossRate,'fs2544ReportStatsFLResult':fs2544ReportStatsFLResult,'fs2544ReportStatsBacktoBackBurstSize':fs2544ReportStatsBacktoBackBurstSize,'fs2544Notification':fs2544Notification,'fs2544Traps':fs2544Traps,'fs2544FailureTrap':fs2544FailureTrap,'fs2544TrapObjects':fs2544TrapObjects,_a:fs2544TrapSlaId,_b:fs2544TypeOfFailure})