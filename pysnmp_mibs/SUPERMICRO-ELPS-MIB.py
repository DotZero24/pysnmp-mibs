_p='fsElpsTrapMismatchType'
_o='fsElpsTypeOfFailure'
_n='fsElpsTrapSwitchingMechanism'
_m='fsElpsPgServiceListId'
_l='fsElpsPgShareProtectionPort'
_k='fsElpsPgServiceListValue'
_j='PgExtCmd'
_i='PgMonitorMechanismType'
_h='PgServiceType'
_g='PgType'
_f='noRequestOnProtection'
_e='noRequestOnWorking'
_d='reverseRequestOnProtection'
_c='reverseRequestOnWorking'
_b='exerciseOnProtection'
_a='exerciseOnWorking'
_Z='waitToRestore'
_Y='rejected'
_X='notApplicable'
_W='overruled'
_V='accepted'
_U='doNotRevert'
_T='signalFailOnProtection'
_S='signalFailOnWorking'
_R='manualSwitchToWorking'
_Q='manualSwitchToProtection'
_P='forceSwitchToProtection'
_O='lockOutProtection'
_N='TruthValue'
_M='fsElpsPgCmdPgStatus'
_L='fsElpsTrapContextName'
_K='accessible-for-notify'
_J='not-accessible'
_I='DisplayString'
_H='fsElpsPgConfigPgId'
_G='fsElpsContextId'
_F='Unsigned32'
_E='Integer32'
_D='read-only'
_C='SUPERMICRO-ELPS-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Dot1agCfmMepId,=mibBuilder.importSymbols('IEEE8021-CFM-MIB','Dot1agCfmMepId')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'enterprises','iso')
DisplayString,PhysAddress,RowPointer,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','RowPointer','RowStatus','TextualConvention',_N)
fselps=ModuleIdentity((1,3,6,1,4,1,10876,101,2,25))
if mibBuilder.loadTexts:fselps.setRevisions(('2012-09-05 00:00',))
class PgId(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class PgType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('individual',1),('list',2),('all',3)))
class PgServiceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('vlan',1),('mplsLSP',2),('mplsPW',3)))
class PgServiceValue(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
class PgServiceValueOrNone(TextualConvention,Unsigned32):status=_A;displayHint='d';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,4294967295))
class PgMonitorMechanismType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('cfm',1),('mplsOam',2),('none',3)))
class PgExtCmd(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),('exercise',4),('clear',5),('freeze',6),('clearFreeze',7),(_R,8)))
class PgLocalCondition(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_S,1),('recoverSignalFailOnWorking',2),(_T,3),('recoverSignalFailOnProtection',4),('waitToRestoreExpiry',5)))
class PgFarEndRequest(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_O,1),(_T,2),(_P,3),(_S,4),(_Q,5),(_Z,6),(_a,7),(_b,8),(_c,9),(_d,10),(_e,11),(_f,12),(_U,13),(_R,14)))
class PgActiveRequest(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)));namedValues=NamedValues(*(('localLockOutProtection',0),('localForcedSwitchToProtection',1),('localSignalFailOnWorking',2),('localRecoverSignalFailOnWorking',3),('localSignalFailOnProtection',4),('localRecoverSignalFailOnProtection',5),('localManualSwitchToProtection',6),('localManualSwitchToWorking',7),('localClear',8),('localExercise',9),('localWaitToRestoreExpiry',10),('farLockOutProtection',11),('farSignalFailOnProtection',12),('farForceSwitchToProtection',13),('farSignalFailOnWorking',14),('farManualSwitchToProtection',15),('farManualSwitchToWorking',16),('farWaitToRestore',17),('farExerciseOnWorking',18),('farExerciseOnProtection',19),('farReverseRequestOnWorking',20),('farReverseRequestOnProtection',21),('farNoRequestOnWorking',22),('farNoRequestOnProtection',23),('farDoNotRevert',24)))
class PgSemState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*((_e,0),(_f,1),(_O,2),(_P,3),(_S,4),(_T,5),(_Q,6),(_R,7),(_Z,8),(_U,9),(_a,10),(_b,11),(_c,12),(_d,13)))
class PgStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('protectionDisabled',0),('workingPathActive',1),('protectionPathActive',2),('waitToRestoreState',3),('holdOffState',4),('switchingFailed',5),('unavailable',6),(_U,7)))
_FsElpsSystem_ObjectIdentity=ObjectIdentity
fsElpsSystem=_FsElpsSystem_ObjectIdentity((1,3,6,1,4,1,10876,101,2,25,1))
class _FsElpsGlobalTraceOption_Type(TruthValue):defaultValue=2
_FsElpsGlobalTraceOption_Type.__name__=_N
_FsElpsGlobalTraceOption_Object=MibScalar
fsElpsGlobalTraceOption=_FsElpsGlobalTraceOption_Object((1,3,6,1,4,1,10876,101,2,25,1,1),_FsElpsGlobalTraceOption_Type())
fsElpsGlobalTraceOption.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsGlobalTraceOption.setStatus(_A)
class _FsElpsPSCChannelCode_Type(Unsigned32):defaultValue=9;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(9,32))
_FsElpsPSCChannelCode_Type.__name__=_F
_FsElpsPSCChannelCode_Object=MibScalar
fsElpsPSCChannelCode=_FsElpsPSCChannelCode_Object((1,3,6,1,4,1,10876,101,2,25,1,2),_FsElpsPSCChannelCode_Type())
fsElpsPSCChannelCode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPSCChannelCode.setStatus('obsolete')
class _FsElpsRapidTxTime_Type(Unsigned32):defaultValue=3300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,3300))
_FsElpsRapidTxTime_Type.__name__=_F
_FsElpsRapidTxTime_Object=MibScalar
fsElpsRapidTxTime=_FsElpsRapidTxTime_Object((1,3,6,1,4,1,10876,101,2,25,1,3),_FsElpsRapidTxTime_Type())
fsElpsRapidTxTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsRapidTxTime.setStatus(_A)
if mibBuilder.loadTexts:fsElpsRapidTxTime.setUnits('microseconds')
_FsElpsContext_ObjectIdentity=ObjectIdentity
fsElpsContext=_FsElpsContext_ObjectIdentity((1,3,6,1,4,1,10876,101,2,25,2))
_FsElpsContextTable_Object=MibTable
fsElpsContextTable=_FsElpsContextTable_Object((1,3,6,1,4,1,10876,101,2,25,2,1))
if mibBuilder.loadTexts:fsElpsContextTable.setStatus(_A)
_FsElpsContextEntry_Object=MibTableRow
fsElpsContextEntry=_FsElpsContextEntry_Object((1,3,6,1,4,1,10876,101,2,25,2,1,1))
fsElpsContextEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:fsElpsContextEntry.setStatus(_A)
_FsElpsContextId_Type=Unsigned32
_FsElpsContextId_Object=MibTableColumn
fsElpsContextId=_FsElpsContextId_Object((1,3,6,1,4,1,10876,101,2,25,2,1,1,1),_FsElpsContextId_Type())
fsElpsContextId.setMaxAccess(_J)
if mibBuilder.loadTexts:fsElpsContextId.setStatus(_A)
class _FsElpsContextSystemControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsElpsContextSystemControl_Type.__name__=_E
_FsElpsContextSystemControl_Object=MibTableColumn
fsElpsContextSystemControl=_FsElpsContextSystemControl_Object((1,3,6,1,4,1,10876,101,2,25,2,1,1,2),_FsElpsContextSystemControl_Type())
fsElpsContextSystemControl.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsContextSystemControl.setStatus(_A)
class _FsElpsContextModuleStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_FsElpsContextModuleStatus_Type.__name__=_E
_FsElpsContextModuleStatus_Object=MibTableColumn
fsElpsContextModuleStatus=_FsElpsContextModuleStatus_Object((1,3,6,1,4,1,10876,101,2,25,2,1,1,3),_FsElpsContextModuleStatus_Type())
fsElpsContextModuleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsContextModuleStatus.setStatus(_A)
class _FsElpsContextTraceInputString_Type(DisplayString):defaultValue=OctetString('critical');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_FsElpsContextTraceInputString_Type.__name__=_I
_FsElpsContextTraceInputString_Object=MibTableColumn
fsElpsContextTraceInputString=_FsElpsContextTraceInputString_Object((1,3,6,1,4,1,10876,101,2,25,2,1,1,4),_FsElpsContextTraceInputString_Type())
fsElpsContextTraceInputString.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsContextTraceInputString.setStatus(_A)
class _FsElpsContextEnableTrap_Type(TruthValue):defaultValue=1
_FsElpsContextEnableTrap_Type.__name__=_N
_FsElpsContextEnableTrap_Object=MibTableColumn
fsElpsContextEnableTrap=_FsElpsContextEnableTrap_Object((1,3,6,1,4,1,10876,101,2,25,2,1,1,5),_FsElpsContextEnableTrap_Type())
fsElpsContextEnableTrap.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsContextEnableTrap.setStatus(_A)
class _FsElpsContextVlanGroupManager_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('mstp',1),('elps',2)))
_FsElpsContextVlanGroupManager_Type.__name__=_E
_FsElpsContextVlanGroupManager_Object=MibTableColumn
fsElpsContextVlanGroupManager=_FsElpsContextVlanGroupManager_Object((1,3,6,1,4,1,10876,101,2,25,2,1,1,6),_FsElpsContextVlanGroupManager_Type())
fsElpsContextVlanGroupManager.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsContextVlanGroupManager.setStatus(_A)
_FsElpsPg_ObjectIdentity=ObjectIdentity
fsElpsPg=_FsElpsPg_ObjectIdentity((1,3,6,1,4,1,10876,101,2,25,3))
_FsElpsPgConfigTable_Object=MibTable
fsElpsPgConfigTable=_FsElpsPgConfigTable_Object((1,3,6,1,4,1,10876,101,2,25,3,1))
if mibBuilder.loadTexts:fsElpsPgConfigTable.setStatus(_A)
_FsElpsPgConfigEntry_Object=MibTableRow
fsElpsPgConfigEntry=_FsElpsPgConfigEntry_Object((1,3,6,1,4,1,10876,101,2,25,3,1,1))
fsElpsPgConfigEntry.setIndexNames((0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:fsElpsPgConfigEntry.setStatus(_A)
_FsElpsPgConfigPgId_Type=PgId
_FsElpsPgConfigPgId_Object=MibTableColumn
fsElpsPgConfigPgId=_FsElpsPgConfigPgId_Object((1,3,6,1,4,1,10876,101,2,25,3,1,1,1),_FsElpsPgConfigPgId_Type())
fsElpsPgConfigPgId.setMaxAccess(_J)
if mibBuilder.loadTexts:fsElpsPgConfigPgId.setStatus(_A)
class _FsElpsPgConfigType_Type(PgType):defaultValue=1
_FsElpsPgConfigType_Type.__name__=_g
_FsElpsPgConfigType_Object=MibTableColumn
fsElpsPgConfigType=_FsElpsPgConfigType_Object((1,3,6,1,4,1,10876,101,2,25,3,1,1,2),_FsElpsPgConfigType_Type())
fsElpsPgConfigType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgConfigType.setStatus(_A)
class _FsElpsPgConfigServiceType_Type(PgServiceType):defaultValue=1
_FsElpsPgConfigServiceType_Type.__name__=_h
_FsElpsPgConfigServiceType_Object=MibTableColumn
fsElpsPgConfigServiceType=_FsElpsPgConfigServiceType_Object((1,3,6,1,4,1,10876,101,2,25,3,1,1,3),_FsElpsPgConfigServiceType_Type())
fsElpsPgConfigServiceType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgConfigServiceType.setStatus(_A)
class _FsElpsPgConfigMonitorMechanism_Type(PgMonitorMechanismType):defaultValue=1
_FsElpsPgConfigMonitorMechanism_Type.__name__=_i
_FsElpsPgConfigMonitorMechanism_Object=MibTableColumn
fsElpsPgConfigMonitorMechanism=_FsElpsPgConfigMonitorMechanism_Object((1,3,6,1,4,1,10876,101,2,25,3,1,1,4),_FsElpsPgConfigMonitorMechanism_Type())
fsElpsPgConfigMonitorMechanism.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgConfigMonitorMechanism.setStatus(_A)
_FsElpsPgConfigIngressPort_Type=InterfaceIndexOrZero
_FsElpsPgConfigIngressPort_Object=MibTableColumn
fsElpsPgConfigIngressPort=_FsElpsPgConfigIngressPort_Object((1,3,6,1,4,1,10876,101,2,25,3,1,1,5),_FsElpsPgConfigIngressPort_Type())
fsElpsPgConfigIngressPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgConfigIngressPort.setStatus(_A)
_FsElpsPgConfigWorkingPort_Type=InterfaceIndexOrZero
_FsElpsPgConfigWorkingPort_Object=MibTableColumn
fsElpsPgConfigWorkingPort=_FsElpsPgConfigWorkingPort_Object((1,3,6,1,4,1,10876,101,2,25,3,1,1,6),_FsElpsPgConfigWorkingPort_Type())
fsElpsPgConfigWorkingPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgConfigWorkingPort.setStatus(_A)
_FsElpsPgConfigProtectionPort_Type=InterfaceIndexOrZero
_FsElpsPgConfigProtectionPort_Object=MibTableColumn
fsElpsPgConfigProtectionPort=_FsElpsPgConfigProtectionPort_Object((1,3,6,1,4,1,10876,101,2,25,3,1,1,7),_FsElpsPgConfigProtectionPort_Type())
fsElpsPgConfigProtectionPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgConfigProtectionPort.setStatus(_A)
_FsElpsPgConfigWorkingServiceValue_Type=PgServiceValueOrNone
_FsElpsPgConfigWorkingServiceValue_Object=MibTableColumn
fsElpsPgConfigWorkingServiceValue=_FsElpsPgConfigWorkingServiceValue_Object((1,3,6,1,4,1,10876,101,2,25,3,1,1,8),_FsElpsPgConfigWorkingServiceValue_Type())
fsElpsPgConfigWorkingServiceValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgConfigWorkingServiceValue.setStatus(_A)
_FsElpsPgConfigProtectionServiceValue_Type=PgServiceValueOrNone
_FsElpsPgConfigProtectionServiceValue_Object=MibTableColumn
fsElpsPgConfigProtectionServiceValue=_FsElpsPgConfigProtectionServiceValue_Object((1,3,6,1,4,1,10876,101,2,25,3,1,1,9),_FsElpsPgConfigProtectionServiceValue_Type())
fsElpsPgConfigProtectionServiceValue.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgConfigProtectionServiceValue.setStatus(_A)
class _FsElpsPgConfigOperType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('revertive',1),('nonRevertive',2)))
_FsElpsPgConfigOperType_Type.__name__=_E
_FsElpsPgConfigOperType_Object=MibTableColumn
fsElpsPgConfigOperType=_FsElpsPgConfigOperType_Object((1,3,6,1,4,1,10876,101,2,25,3,1,1,10),_FsElpsPgConfigOperType_Type())
fsElpsPgConfigOperType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgConfigOperType.setStatus(_A)
class _FsElpsPgConfigProtType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('oneIsToOneBidirectionalWithAps',1),('onePlusOneBidirectionalWithAps',2),('onePlusOneUnidirectionalWithAps',3),('onePlusOneUnidirectionalWithOutAps',4)))
_FsElpsPgConfigProtType_Type.__name__=_E
_FsElpsPgConfigProtType_Object=MibTableColumn
fsElpsPgConfigProtType=_FsElpsPgConfigProtType_Object((1,3,6,1,4,1,10876,101,2,25,3,1,1,11),_FsElpsPgConfigProtType_Type())
fsElpsPgConfigProtType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgConfigProtType.setStatus(_A)
class _FsElpsPgConfigName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsElpsPgConfigName_Type.__name__=_I
_FsElpsPgConfigName_Object=MibTableColumn
fsElpsPgConfigName=_FsElpsPgConfigName_Object((1,3,6,1,4,1,10876,101,2,25,3,1,1,12),_FsElpsPgConfigName_Type())
fsElpsPgConfigName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgConfigName.setStatus(_A)
_FsElpsPgConfigRowStatus_Type=RowStatus
_FsElpsPgConfigRowStatus_Object=MibTableColumn
fsElpsPgConfigRowStatus=_FsElpsPgConfigRowStatus_Object((1,3,6,1,4,1,10876,101,2,25,3,1,1,13),_FsElpsPgConfigRowStatus_Type())
fsElpsPgConfigRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgConfigRowStatus.setStatus(_A)
_FsElpsPgConfigWorkingServicePointer_Type=RowPointer
_FsElpsPgConfigWorkingServicePointer_Object=MibTableColumn
fsElpsPgConfigWorkingServicePointer=_FsElpsPgConfigWorkingServicePointer_Object((1,3,6,1,4,1,10876,101,2,25,3,1,1,14),_FsElpsPgConfigWorkingServicePointer_Type())
fsElpsPgConfigWorkingServicePointer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgConfigWorkingServicePointer.setStatus(_A)
_FsElpsPgConfigWorkingReverseServicePointer_Type=RowPointer
_FsElpsPgConfigWorkingReverseServicePointer_Object=MibTableColumn
fsElpsPgConfigWorkingReverseServicePointer=_FsElpsPgConfigWorkingReverseServicePointer_Object((1,3,6,1,4,1,10876,101,2,25,3,1,1,15),_FsElpsPgConfigWorkingReverseServicePointer_Type())
fsElpsPgConfigWorkingReverseServicePointer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgConfigWorkingReverseServicePointer.setStatus(_A)
_FsElpsPgConfigProtectionServicePointer_Type=RowPointer
_FsElpsPgConfigProtectionServicePointer_Object=MibTableColumn
fsElpsPgConfigProtectionServicePointer=_FsElpsPgConfigProtectionServicePointer_Object((1,3,6,1,4,1,10876,101,2,25,3,1,1,16),_FsElpsPgConfigProtectionServicePointer_Type())
fsElpsPgConfigProtectionServicePointer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgConfigProtectionServicePointer.setStatus(_A)
_FsElpsPgConfigProtectionReverseServicePointer_Type=RowPointer
_FsElpsPgConfigProtectionReverseServicePointer_Object=MibTableColumn
fsElpsPgConfigProtectionReverseServicePointer=_FsElpsPgConfigProtectionReverseServicePointer_Object((1,3,6,1,4,1,10876,101,2,25,3,1,1,17),_FsElpsPgConfigProtectionReverseServicePointer_Type())
fsElpsPgConfigProtectionReverseServicePointer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgConfigProtectionReverseServicePointer.setStatus(_A)
class _FsElpsPgConfigWorkingInstanceId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_FsElpsPgConfigWorkingInstanceId_Type.__name__=_F
_FsElpsPgConfigWorkingInstanceId_Object=MibTableColumn
fsElpsPgConfigWorkingInstanceId=_FsElpsPgConfigWorkingInstanceId_Object((1,3,6,1,4,1,10876,101,2,25,3,1,1,18),_FsElpsPgConfigWorkingInstanceId_Type())
fsElpsPgConfigWorkingInstanceId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgConfigWorkingInstanceId.setStatus(_A)
class _FsElpsPgConfigProtectionInstanceId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_FsElpsPgConfigProtectionInstanceId_Type.__name__=_F
_FsElpsPgConfigProtectionInstanceId_Object=MibTableColumn
fsElpsPgConfigProtectionInstanceId=_FsElpsPgConfigProtectionInstanceId_Object((1,3,6,1,4,1,10876,101,2,25,3,1,1,19),_FsElpsPgConfigProtectionInstanceId_Type())
fsElpsPgConfigProtectionInstanceId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgConfigProtectionInstanceId.setStatus(_A)
class _FsElpsPgPscVersion_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsElpsPgPscVersion_Type.__name__=_F
_FsElpsPgPscVersion_Object=MibTableColumn
fsElpsPgPscVersion=_FsElpsPgPscVersion_Object((1,3,6,1,4,1,10876,101,2,25,3,1,1,20),_FsElpsPgPscVersion_Type())
fsElpsPgPscVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgPscVersion.setStatus(_A)
_FsElpsPgCmdTable_Object=MibTable
fsElpsPgCmdTable=_FsElpsPgCmdTable_Object((1,3,6,1,4,1,10876,101,2,25,3,2))
if mibBuilder.loadTexts:fsElpsPgCmdTable.setStatus(_A)
_FsElpsPgCmdEntry_Object=MibTableRow
fsElpsPgCmdEntry=_FsElpsPgCmdEntry_Object((1,3,6,1,4,1,10876,101,2,25,3,2,1))
fsElpsPgCmdEntry.setIndexNames((0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:fsElpsPgCmdEntry.setStatus(_A)
class _FsElpsPgCmdHoTime_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_FsElpsPgCmdHoTime_Type.__name__=_F
_FsElpsPgCmdHoTime_Object=MibTableColumn
fsElpsPgCmdHoTime=_FsElpsPgCmdHoTime_Object((1,3,6,1,4,1,10876,101,2,25,3,2,1,1),_FsElpsPgCmdHoTime_Type())
fsElpsPgCmdHoTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgCmdHoTime.setStatus(_A)
class _FsElpsPgCmdWTR_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_FsElpsPgCmdWTR_Type.__name__=_F
_FsElpsPgCmdWTR_Object=MibTableColumn
fsElpsPgCmdWTR=_FsElpsPgCmdWTR_Object((1,3,6,1,4,1,10876,101,2,25,3,2,1,2),_FsElpsPgCmdWTR_Type())
fsElpsPgCmdWTR.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgCmdWTR.setStatus(_A)
class _FsElpsPgCmdExtCmd_Type(PgExtCmd):defaultValue=5
_FsElpsPgCmdExtCmd_Type.__name__=_j
_FsElpsPgCmdExtCmd_Object=MibTableColumn
fsElpsPgCmdExtCmd=_FsElpsPgCmdExtCmd_Object((1,3,6,1,4,1,10876,101,2,25,3,2,1,3),_FsElpsPgCmdExtCmd_Type())
fsElpsPgCmdExtCmd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgCmdExtCmd.setStatus(_A)
class _FsElpsPgCmdExtCmdStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3),(_Y,4)))
_FsElpsPgCmdExtCmdStatus_Type.__name__=_E
_FsElpsPgCmdExtCmdStatus_Object=MibTableColumn
fsElpsPgCmdExtCmdStatus=_FsElpsPgCmdExtCmdStatus_Object((1,3,6,1,4,1,10876,101,2,25,3,2,1,4),_FsElpsPgCmdExtCmdStatus_Type())
fsElpsPgCmdExtCmdStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsElpsPgCmdExtCmdStatus.setStatus(_A)
_FsElpsPgCmdLocalCondition_Type=PgLocalCondition
_FsElpsPgCmdLocalCondition_Object=MibTableColumn
fsElpsPgCmdLocalCondition=_FsElpsPgCmdLocalCondition_Object((1,3,6,1,4,1,10876,101,2,25,3,2,1,5),_FsElpsPgCmdLocalCondition_Type())
fsElpsPgCmdLocalCondition.setMaxAccess(_D)
if mibBuilder.loadTexts:fsElpsPgCmdLocalCondition.setStatus(_A)
class _FsElpsPgCmdLocalConditionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3),(_Y,4)))
_FsElpsPgCmdLocalConditionStatus_Type.__name__=_E
_FsElpsPgCmdLocalConditionStatus_Object=MibTableColumn
fsElpsPgCmdLocalConditionStatus=_FsElpsPgCmdLocalConditionStatus_Object((1,3,6,1,4,1,10876,101,2,25,3,2,1,6),_FsElpsPgCmdLocalConditionStatus_Type())
fsElpsPgCmdLocalConditionStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsElpsPgCmdLocalConditionStatus.setStatus(_A)
_FsElpsPgCmdFarEndRequest_Type=PgFarEndRequest
_FsElpsPgCmdFarEndRequest_Object=MibTableColumn
fsElpsPgCmdFarEndRequest=_FsElpsPgCmdFarEndRequest_Object((1,3,6,1,4,1,10876,101,2,25,3,2,1,7),_FsElpsPgCmdFarEndRequest_Type())
fsElpsPgCmdFarEndRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:fsElpsPgCmdFarEndRequest.setStatus(_A)
class _FsElpsPgCmdFarEndRequestStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3),(_Y,4)))
_FsElpsPgCmdFarEndRequestStatus_Type.__name__=_E
_FsElpsPgCmdFarEndRequestStatus_Object=MibTableColumn
fsElpsPgCmdFarEndRequestStatus=_FsElpsPgCmdFarEndRequestStatus_Object((1,3,6,1,4,1,10876,101,2,25,3,2,1,8),_FsElpsPgCmdFarEndRequestStatus_Type())
fsElpsPgCmdFarEndRequestStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsElpsPgCmdFarEndRequestStatus.setStatus(_A)
_FsElpsPgCmdActiveRequest_Type=PgActiveRequest
_FsElpsPgCmdActiveRequest_Object=MibTableColumn
fsElpsPgCmdActiveRequest=_FsElpsPgCmdActiveRequest_Object((1,3,6,1,4,1,10876,101,2,25,3,2,1,9),_FsElpsPgCmdActiveRequest_Type())
fsElpsPgCmdActiveRequest.setMaxAccess(_D)
if mibBuilder.loadTexts:fsElpsPgCmdActiveRequest.setStatus(_A)
_FsElpsPgCmdSemState_Type=PgSemState
_FsElpsPgCmdSemState_Object=MibTableColumn
fsElpsPgCmdSemState=_FsElpsPgCmdSemState_Object((1,3,6,1,4,1,10876,101,2,25,3,2,1,10),_FsElpsPgCmdSemState_Type())
fsElpsPgCmdSemState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsElpsPgCmdSemState.setStatus(_A)
_FsElpsPgCmdPgStatus_Type=PgStatus
_FsElpsPgCmdPgStatus_Object=MibTableColumn
fsElpsPgCmdPgStatus=_FsElpsPgCmdPgStatus_Object((1,3,6,1,4,1,10876,101,2,25,3,2,1,11),_FsElpsPgCmdPgStatus_Type())
fsElpsPgCmdPgStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsElpsPgCmdPgStatus.setStatus(_A)
class _FsElpsPgCmdApsPeriodicTime_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_FsElpsPgCmdApsPeriodicTime_Type.__name__=_F
_FsElpsPgCmdApsPeriodicTime_Object=MibTableColumn
fsElpsPgCmdApsPeriodicTime=_FsElpsPgCmdApsPeriodicTime_Object((1,3,6,1,4,1,10876,101,2,25,3,2,1,12),_FsElpsPgCmdApsPeriodicTime_Type())
fsElpsPgCmdApsPeriodicTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgCmdApsPeriodicTime.setStatus(_A)
if mibBuilder.loadTexts:fsElpsPgCmdApsPeriodicTime.setUnits('seconds')
_FsElpsPgCfmTable_Object=MibTable
fsElpsPgCfmTable=_FsElpsPgCfmTable_Object((1,3,6,1,4,1,10876,101,2,25,3,3))
if mibBuilder.loadTexts:fsElpsPgCfmTable.setStatus(_A)
_FsElpsPgCfmEntry_Object=MibTableRow
fsElpsPgCfmEntry=_FsElpsPgCfmEntry_Object((1,3,6,1,4,1,10876,101,2,25,3,3,1))
fsElpsPgCfmEntry.setIndexNames((0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:fsElpsPgCfmEntry.setStatus(_A)
_FsElpsPgCfmWorkingMEG_Type=Unsigned32
_FsElpsPgCfmWorkingMEG_Object=MibTableColumn
fsElpsPgCfmWorkingMEG=_FsElpsPgCfmWorkingMEG_Object((1,3,6,1,4,1,10876,101,2,25,3,3,1,1),_FsElpsPgCfmWorkingMEG_Type())
fsElpsPgCfmWorkingMEG.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgCfmWorkingMEG.setStatus(_A)
_FsElpsPgCfmWorkingME_Type=Unsigned32
_FsElpsPgCfmWorkingME_Object=MibTableColumn
fsElpsPgCfmWorkingME=_FsElpsPgCfmWorkingME_Object((1,3,6,1,4,1,10876,101,2,25,3,3,1,2),_FsElpsPgCfmWorkingME_Type())
fsElpsPgCfmWorkingME.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgCfmWorkingME.setStatus(_A)
_FsElpsPgCfmWorkingMEP_Type=Dot1agCfmMepId
_FsElpsPgCfmWorkingMEP_Object=MibTableColumn
fsElpsPgCfmWorkingMEP=_FsElpsPgCfmWorkingMEP_Object((1,3,6,1,4,1,10876,101,2,25,3,3,1,3),_FsElpsPgCfmWorkingMEP_Type())
fsElpsPgCfmWorkingMEP.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgCfmWorkingMEP.setStatus(_A)
_FsElpsPgCfmProtectionMEG_Type=Unsigned32
_FsElpsPgCfmProtectionMEG_Object=MibTableColumn
fsElpsPgCfmProtectionMEG=_FsElpsPgCfmProtectionMEG_Object((1,3,6,1,4,1,10876,101,2,25,3,3,1,4),_FsElpsPgCfmProtectionMEG_Type())
fsElpsPgCfmProtectionMEG.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgCfmProtectionMEG.setStatus(_A)
_FsElpsPgCfmProtectionME_Type=Unsigned32
_FsElpsPgCfmProtectionME_Object=MibTableColumn
fsElpsPgCfmProtectionME=_FsElpsPgCfmProtectionME_Object((1,3,6,1,4,1,10876,101,2,25,3,3,1,5),_FsElpsPgCfmProtectionME_Type())
fsElpsPgCfmProtectionME.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgCfmProtectionME.setStatus(_A)
_FsElpsPgCfmProtectionMEP_Type=Dot1agCfmMepId
_FsElpsPgCfmProtectionMEP_Object=MibTableColumn
fsElpsPgCfmProtectionMEP=_FsElpsPgCfmProtectionMEP_Object((1,3,6,1,4,1,10876,101,2,25,3,3,1,6),_FsElpsPgCfmProtectionMEP_Type())
fsElpsPgCfmProtectionMEP.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgCfmProtectionMEP.setStatus(_A)
_FsElpsPgCfmRowStatus_Type=RowStatus
_FsElpsPgCfmRowStatus_Object=MibTableColumn
fsElpsPgCfmRowStatus=_FsElpsPgCfmRowStatus_Object((1,3,6,1,4,1,10876,101,2,25,3,3,1,7),_FsElpsPgCfmRowStatus_Type())
fsElpsPgCfmRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgCfmRowStatus.setStatus(_A)
_FsElpsPgCfmWorkingReverseMEG_Type=Unsigned32
_FsElpsPgCfmWorkingReverseMEG_Object=MibTableColumn
fsElpsPgCfmWorkingReverseMEG=_FsElpsPgCfmWorkingReverseMEG_Object((1,3,6,1,4,1,10876,101,2,25,3,3,1,8),_FsElpsPgCfmWorkingReverseMEG_Type())
fsElpsPgCfmWorkingReverseMEG.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgCfmWorkingReverseMEG.setStatus(_A)
_FsElpsPgCfmWorkingReverseME_Type=Unsigned32
_FsElpsPgCfmWorkingReverseME_Object=MibTableColumn
fsElpsPgCfmWorkingReverseME=_FsElpsPgCfmWorkingReverseME_Object((1,3,6,1,4,1,10876,101,2,25,3,3,1,9),_FsElpsPgCfmWorkingReverseME_Type())
fsElpsPgCfmWorkingReverseME.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgCfmWorkingReverseME.setStatus(_A)
_FsElpsPgCfmWorkingReverseMEP_Type=Dot1agCfmMepId
_FsElpsPgCfmWorkingReverseMEP_Object=MibTableColumn
fsElpsPgCfmWorkingReverseMEP=_FsElpsPgCfmWorkingReverseMEP_Object((1,3,6,1,4,1,10876,101,2,25,3,3,1,10),_FsElpsPgCfmWorkingReverseMEP_Type())
fsElpsPgCfmWorkingReverseMEP.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgCfmWorkingReverseMEP.setStatus(_A)
_FsElpsPgCfmProtectionReverseMEG_Type=Unsigned32
_FsElpsPgCfmProtectionReverseMEG_Object=MibTableColumn
fsElpsPgCfmProtectionReverseMEG=_FsElpsPgCfmProtectionReverseMEG_Object((1,3,6,1,4,1,10876,101,2,25,3,3,1,11),_FsElpsPgCfmProtectionReverseMEG_Type())
fsElpsPgCfmProtectionReverseMEG.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgCfmProtectionReverseMEG.setStatus(_A)
_FsElpsPgCfmProtectionReverseME_Type=Unsigned32
_FsElpsPgCfmProtectionReverseME_Object=MibTableColumn
fsElpsPgCfmProtectionReverseME=_FsElpsPgCfmProtectionReverseME_Object((1,3,6,1,4,1,10876,101,2,25,3,3,1,12),_FsElpsPgCfmProtectionReverseME_Type())
fsElpsPgCfmProtectionReverseME.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgCfmProtectionReverseME.setStatus(_A)
_FsElpsPgCfmProtectionReverseMEP_Type=Dot1agCfmMepId
_FsElpsPgCfmProtectionReverseMEP_Object=MibTableColumn
fsElpsPgCfmProtectionReverseMEP=_FsElpsPgCfmProtectionReverseMEP_Object((1,3,6,1,4,1,10876,101,2,25,3,3,1,13),_FsElpsPgCfmProtectionReverseMEP_Type())
fsElpsPgCfmProtectionReverseMEP.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgCfmProtectionReverseMEP.setStatus(_A)
_FsElpsPgServiceListTable_Object=MibTable
fsElpsPgServiceListTable=_FsElpsPgServiceListTable_Object((1,3,6,1,4,1,10876,101,2,25,3,4))
if mibBuilder.loadTexts:fsElpsPgServiceListTable.setStatus(_A)
_FsElpsPgServiceListEntry_Object=MibTableRow
fsElpsPgServiceListEntry=_FsElpsPgServiceListEntry_Object((1,3,6,1,4,1,10876,101,2,25,3,4,1))
fsElpsPgServiceListEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_k))
if mibBuilder.loadTexts:fsElpsPgServiceListEntry.setStatus(_A)
_FsElpsPgServiceListValue_Type=PgServiceValue
_FsElpsPgServiceListValue_Object=MibTableColumn
fsElpsPgServiceListValue=_FsElpsPgServiceListValue_Object((1,3,6,1,4,1,10876,101,2,25,3,4,1,1),_FsElpsPgServiceListValue_Type())
fsElpsPgServiceListValue.setMaxAccess(_J)
if mibBuilder.loadTexts:fsElpsPgServiceListValue.setStatus(_A)
_FsElpsPgServiceListRowStatus_Type=RowStatus
_FsElpsPgServiceListRowStatus_Object=MibTableColumn
fsElpsPgServiceListRowStatus=_FsElpsPgServiceListRowStatus_Object((1,3,6,1,4,1,10876,101,2,25,3,4,1,2),_FsElpsPgServiceListRowStatus_Type())
fsElpsPgServiceListRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgServiceListRowStatus.setStatus(_A)
_FsElpsPgShareTable_Object=MibTable
fsElpsPgShareTable=_FsElpsPgShareTable_Object((1,3,6,1,4,1,10876,101,2,25,3,5))
if mibBuilder.loadTexts:fsElpsPgShareTable.setStatus(_A)
_FsElpsPgShareEntry_Object=MibTableRow
fsElpsPgShareEntry=_FsElpsPgShareEntry_Object((1,3,6,1,4,1,10876,101,2,25,3,5,1))
fsElpsPgShareEntry.setIndexNames((0,_C,_G),(0,_C,_l),(0,_C,_H))
if mibBuilder.loadTexts:fsElpsPgShareEntry.setStatus(_A)
_FsElpsPgShareProtectionPort_Type=InterfaceIndex
_FsElpsPgShareProtectionPort_Object=MibTableColumn
fsElpsPgShareProtectionPort=_FsElpsPgShareProtectionPort_Object((1,3,6,1,4,1,10876,101,2,25,3,5,1,1),_FsElpsPgShareProtectionPort_Type())
fsElpsPgShareProtectionPort.setMaxAccess(_J)
if mibBuilder.loadTexts:fsElpsPgShareProtectionPort.setStatus(_A)
_FsElpsPgSharePgStatus_Type=PgStatus
_FsElpsPgSharePgStatus_Object=MibTableColumn
fsElpsPgSharePgStatus=_FsElpsPgSharePgStatus_Object((1,3,6,1,4,1,10876,101,2,25,3,5,1,2),_FsElpsPgSharePgStatus_Type())
fsElpsPgSharePgStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsElpsPgSharePgStatus.setStatus(_A)
_FsElpsPgStatsTable_Object=MibTable
fsElpsPgStatsTable=_FsElpsPgStatsTable_Object((1,3,6,1,4,1,10876,101,2,25,3,6))
if mibBuilder.loadTexts:fsElpsPgStatsTable.setStatus(_A)
_FsElpsPgStatsEntry_Object=MibTableRow
fsElpsPgStatsEntry=_FsElpsPgStatsEntry_Object((1,3,6,1,4,1,10876,101,2,25,3,6,1))
fsElpsPgStatsEntry.setIndexNames((0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:fsElpsPgStatsEntry.setStatus(_A)
_FsElpsPgStatsAutoProtectionSwitchCount_Type=Counter32
_FsElpsPgStatsAutoProtectionSwitchCount_Object=MibTableColumn
fsElpsPgStatsAutoProtectionSwitchCount=_FsElpsPgStatsAutoProtectionSwitchCount_Object((1,3,6,1,4,1,10876,101,2,25,3,6,1,1),_FsElpsPgStatsAutoProtectionSwitchCount_Type())
fsElpsPgStatsAutoProtectionSwitchCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsElpsPgStatsAutoProtectionSwitchCount.setStatus(_A)
_FsElpsPgStatsForcedSwitchCount_Type=Counter32
_FsElpsPgStatsForcedSwitchCount_Object=MibTableColumn
fsElpsPgStatsForcedSwitchCount=_FsElpsPgStatsForcedSwitchCount_Object((1,3,6,1,4,1,10876,101,2,25,3,6,1,2),_FsElpsPgStatsForcedSwitchCount_Type())
fsElpsPgStatsForcedSwitchCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsElpsPgStatsForcedSwitchCount.setStatus(_A)
_FsElpsPgStatsManualSwitchCount_Type=Counter32
_FsElpsPgStatsManualSwitchCount_Object=MibTableColumn
fsElpsPgStatsManualSwitchCount=_FsElpsPgStatsManualSwitchCount_Object((1,3,6,1,4,1,10876,101,2,25,3,6,1,3),_FsElpsPgStatsManualSwitchCount_Type())
fsElpsPgStatsManualSwitchCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsElpsPgStatsManualSwitchCount.setStatus(_A)
_FsElpsPgStatsClearStatistics_Type=TruthValue
_FsElpsPgStatsClearStatistics_Object=MibTableColumn
fsElpsPgStatsClearStatistics=_FsElpsPgStatsClearStatistics_Object((1,3,6,1,4,1,10876,101,2,25,3,6,1,4),_FsElpsPgStatsClearStatistics_Type())
fsElpsPgStatsClearStatistics.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgStatsClearStatistics.setStatus(_A)
_FsElpsPgStatsApsPktTxCount_Type=Counter32
_FsElpsPgStatsApsPktTxCount_Object=MibTableColumn
fsElpsPgStatsApsPktTxCount=_FsElpsPgStatsApsPktTxCount_Object((1,3,6,1,4,1,10876,101,2,25,3,6,1,5),_FsElpsPgStatsApsPktTxCount_Type())
fsElpsPgStatsApsPktTxCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsElpsPgStatsApsPktTxCount.setStatus(_A)
_FsElpsPgStatsApsPktRxCount_Type=Counter32
_FsElpsPgStatsApsPktRxCount_Object=MibTableColumn
fsElpsPgStatsApsPktRxCount=_FsElpsPgStatsApsPktRxCount_Object((1,3,6,1,4,1,10876,101,2,25,3,6,1,6),_FsElpsPgStatsApsPktRxCount_Type())
fsElpsPgStatsApsPktRxCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsElpsPgStatsApsPktRxCount.setStatus(_A)
_FsElpsPgStatsApsPktDiscardCount_Type=Counter32
_FsElpsPgStatsApsPktDiscardCount_Object=MibTableColumn
fsElpsPgStatsApsPktDiscardCount=_FsElpsPgStatsApsPktDiscardCount_Object((1,3,6,1,4,1,10876,101,2,25,3,6,1,7),_FsElpsPgStatsApsPktDiscardCount_Type())
fsElpsPgStatsApsPktDiscardCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsElpsPgStatsApsPktDiscardCount.setStatus(_A)
_FsElpsPgLRSFRxTime_Type=Unsigned32
_FsElpsPgLRSFRxTime_Object=MibTableColumn
fsElpsPgLRSFRxTime=_FsElpsPgLRSFRxTime_Object((1,3,6,1,4,1,10876,101,2,25,3,6,1,8),_FsElpsPgLRSFRxTime_Type())
fsElpsPgLRSFRxTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsElpsPgLRSFRxTime.setStatus(_A)
_FsElpsPgLRSFTxTime_Type=Unsigned32
_FsElpsPgLRSFTxTime_Object=MibTableColumn
fsElpsPgLRSFTxTime=_FsElpsPgLRSFTxTime_Object((1,3,6,1,4,1,10876,101,2,25,3,6,1,9),_FsElpsPgLRSFTxTime_Type())
fsElpsPgLRSFTxTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsElpsPgLRSFTxTime.setStatus(_A)
_FsElpsPgFRSFRxTime_Type=Unsigned32
_FsElpsPgFRSFRxTime_Object=MibTableColumn
fsElpsPgFRSFRxTime=_FsElpsPgFRSFRxTime_Object((1,3,6,1,4,1,10876,101,2,25,3,6,1,10),_FsElpsPgFRSFRxTime_Type())
fsElpsPgFRSFRxTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsElpsPgFRSFRxTime.setStatus(_A)
_FsElpsPgStateChgTime_Type=Unsigned32
_FsElpsPgStateChgTime_Object=MibTableColumn
fsElpsPgStateChgTime=_FsElpsPgStateChgTime_Object((1,3,6,1,4,1,10876,101,2,25,3,6,1,11),_FsElpsPgStateChgTime_Type())
fsElpsPgStateChgTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsElpsPgStateChgTime.setStatus(_A)
_FsElpsPgServiceListPointerTable_Object=MibTable
fsElpsPgServiceListPointerTable=_FsElpsPgServiceListPointerTable_Object((1,3,6,1,4,1,10876,101,2,25,3,7))
if mibBuilder.loadTexts:fsElpsPgServiceListPointerTable.setStatus(_A)
_FsElpsPgServiceListPointerEntry_Object=MibTableRow
fsElpsPgServiceListPointerEntry=_FsElpsPgServiceListPointerEntry_Object((1,3,6,1,4,1,10876,101,2,25,3,7,1))
fsElpsPgServiceListPointerEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_m))
if mibBuilder.loadTexts:fsElpsPgServiceListPointerEntry.setStatus(_A)
_FsElpsPgServiceListId_Type=Unsigned32
_FsElpsPgServiceListId_Object=MibTableColumn
fsElpsPgServiceListId=_FsElpsPgServiceListId_Object((1,3,6,1,4,1,10876,101,2,25,3,7,1,1),_FsElpsPgServiceListId_Type())
fsElpsPgServiceListId.setMaxAccess(_J)
if mibBuilder.loadTexts:fsElpsPgServiceListId.setStatus(_A)
_FsElpsPgWorkingServiceListPointer_Type=RowPointer
_FsElpsPgWorkingServiceListPointer_Object=MibTableColumn
fsElpsPgWorkingServiceListPointer=_FsElpsPgWorkingServiceListPointer_Object((1,3,6,1,4,1,10876,101,2,25,3,7,1,2),_FsElpsPgWorkingServiceListPointer_Type())
fsElpsPgWorkingServiceListPointer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgWorkingServiceListPointer.setStatus(_A)
_FsElpsPgWorkingReverseServiceListPointer_Type=RowPointer
_FsElpsPgWorkingReverseServiceListPointer_Object=MibTableColumn
fsElpsPgWorkingReverseServiceListPointer=_FsElpsPgWorkingReverseServiceListPointer_Object((1,3,6,1,4,1,10876,101,2,25,3,7,1,3),_FsElpsPgWorkingReverseServiceListPointer_Type())
fsElpsPgWorkingReverseServiceListPointer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgWorkingReverseServiceListPointer.setStatus(_A)
_FsElpsPgProtectionServiceListPointer_Type=RowPointer
_FsElpsPgProtectionServiceListPointer_Object=MibTableColumn
fsElpsPgProtectionServiceListPointer=_FsElpsPgProtectionServiceListPointer_Object((1,3,6,1,4,1,10876,101,2,25,3,7,1,4),_FsElpsPgProtectionServiceListPointer_Type())
fsElpsPgProtectionServiceListPointer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgProtectionServiceListPointer.setStatus(_A)
_FsElpsPgProtectionReverseServiceListPointer_Type=RowPointer
_FsElpsPgProtectionReverseServiceListPointer_Object=MibTableColumn
fsElpsPgProtectionReverseServiceListPointer=_FsElpsPgProtectionReverseServiceListPointer_Object((1,3,6,1,4,1,10876,101,2,25,3,7,1,5),_FsElpsPgProtectionReverseServiceListPointer_Type())
fsElpsPgProtectionReverseServiceListPointer.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgProtectionReverseServiceListPointer.setStatus(_A)
_FsElpsPgServiceListPointerRowStatus_Type=RowStatus
_FsElpsPgServiceListPointerRowStatus_Object=MibTableColumn
fsElpsPgServiceListPointerRowStatus=_FsElpsPgServiceListPointerRowStatus_Object((1,3,6,1,4,1,10876,101,2,25,3,7,1,6),_FsElpsPgServiceListPointerRowStatus_Type())
fsElpsPgServiceListPointerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsElpsPgServiceListPointerRowStatus.setStatus(_A)
_FsElpsPgNotifications_ObjectIdentity=ObjectIdentity
fsElpsPgNotifications=_FsElpsPgNotifications_ObjectIdentity((1,3,6,1,4,1,10876,101,2,25,4))
_FsElpsTraps_ObjectIdentity=ObjectIdentity
fsElpsTraps=_FsElpsTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,2,25,4,0))
class _FsElpsTrapContextName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsElpsTrapContextName_Type.__name__=_I
_FsElpsTrapContextName_Object=MibScalar
fsElpsTrapContextName=_FsElpsTrapContextName_Object((1,3,6,1,4,1,10876,101,2,25,4,1),_FsElpsTrapContextName_Type())
fsElpsTrapContextName.setMaxAccess(_K)
if mibBuilder.loadTexts:fsElpsTrapContextName.setStatus(_A)
class _FsElpsTrapSwitchingMechanism_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsElpsTrapSwitchingMechanism_Type.__name__=_I
_FsElpsTrapSwitchingMechanism_Object=MibScalar
fsElpsTrapSwitchingMechanism=_FsElpsTrapSwitchingMechanism_Object((1,3,6,1,4,1,10876,101,2,25,4,2),_FsElpsTrapSwitchingMechanism_Type())
fsElpsTrapSwitchingMechanism.setMaxAccess(_K)
if mibBuilder.loadTexts:fsElpsTrapSwitchingMechanism.setStatus(_A)
class _FsElpsTrapMismatchType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsElpsTrapMismatchType_Type.__name__=_I
_FsElpsTrapMismatchType_Object=MibScalar
fsElpsTrapMismatchType=_FsElpsTrapMismatchType_Object((1,3,6,1,4,1,10876,101,2,25,4,3),_FsElpsTrapMismatchType_Type())
fsElpsTrapMismatchType.setMaxAccess(_K)
if mibBuilder.loadTexts:fsElpsTrapMismatchType.setStatus(_A)
class _FsElpsTypeOfFailure_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsElpsTypeOfFailure_Type.__name__=_I
_FsElpsTypeOfFailure_Object=MibScalar
fsElpsTypeOfFailure=_FsElpsTypeOfFailure_Object((1,3,6,1,4,1,10876,101,2,25,4,4),_FsElpsTypeOfFailure_Type())
fsElpsTypeOfFailure.setMaxAccess(_K)
if mibBuilder.loadTexts:fsElpsTypeOfFailure.setStatus(_A)
_FsElpsScalars_ObjectIdentity=ObjectIdentity
fsElpsScalars=_FsElpsScalars_ObjectIdentity((1,3,6,1,4,1,10876,101,2,25,5))
_FsElpsStatsOneIsToOneApsPktTxCount_Type=Counter32
_FsElpsStatsOneIsToOneApsPktTxCount_Object=MibScalar
fsElpsStatsOneIsToOneApsPktTxCount=_FsElpsStatsOneIsToOneApsPktTxCount_Object((1,3,6,1,4,1,10876,101,2,25,5,1),_FsElpsStatsOneIsToOneApsPktTxCount_Type())
fsElpsStatsOneIsToOneApsPktTxCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsElpsStatsOneIsToOneApsPktTxCount.setStatus(_A)
_FsElpsStatsOneIsToOneApsPktRxCount_Type=Counter32
_FsElpsStatsOneIsToOneApsPktRxCount_Object=MibScalar
fsElpsStatsOneIsToOneApsPktRxCount=_FsElpsStatsOneIsToOneApsPktRxCount_Object((1,3,6,1,4,1,10876,101,2,25,5,2),_FsElpsStatsOneIsToOneApsPktRxCount_Type())
fsElpsStatsOneIsToOneApsPktRxCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsElpsStatsOneIsToOneApsPktRxCount.setStatus(_A)
_FsElpsStatsOneIsToOneApsPktDiscardCount_Type=Counter32
_FsElpsStatsOneIsToOneApsPktDiscardCount_Object=MibScalar
fsElpsStatsOneIsToOneApsPktDiscardCount=_FsElpsStatsOneIsToOneApsPktDiscardCount_Object((1,3,6,1,4,1,10876,101,2,25,5,3),_FsElpsStatsOneIsToOneApsPktDiscardCount_Type())
fsElpsStatsOneIsToOneApsPktDiscardCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsElpsStatsOneIsToOneApsPktDiscardCount.setStatus(_A)
_FsElpsStatsOnePlusOneApsPktTxCount_Type=Counter32
_FsElpsStatsOnePlusOneApsPktTxCount_Object=MibScalar
fsElpsStatsOnePlusOneApsPktTxCount=_FsElpsStatsOnePlusOneApsPktTxCount_Object((1,3,6,1,4,1,10876,101,2,25,5,4),_FsElpsStatsOnePlusOneApsPktTxCount_Type())
fsElpsStatsOnePlusOneApsPktTxCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsElpsStatsOnePlusOneApsPktTxCount.setStatus(_A)
_FsElpsStatsOnePlusOneApsPktRxCount_Type=Counter32
_FsElpsStatsOnePlusOneApsPktRxCount_Object=MibScalar
fsElpsStatsOnePlusOneApsPktRxCount=_FsElpsStatsOnePlusOneApsPktRxCount_Object((1,3,6,1,4,1,10876,101,2,25,5,5),_FsElpsStatsOnePlusOneApsPktRxCount_Type())
fsElpsStatsOnePlusOneApsPktRxCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsElpsStatsOnePlusOneApsPktRxCount.setStatus(_A)
_FsElpsStatsOnePlusOneApsPktDiscardCount_Type=Counter32
_FsElpsStatsOnePlusOneApsPktDiscardCount_Object=MibScalar
fsElpsStatsOnePlusOneApsPktDiscardCount=_FsElpsStatsOnePlusOneApsPktDiscardCount_Object((1,3,6,1,4,1,10876,101,2,25,5,6),_FsElpsStatsOnePlusOneApsPktDiscardCount_Type())
fsElpsStatsOnePlusOneApsPktDiscardCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsElpsStatsOnePlusOneApsPktDiscardCount.setStatus(_A)
fsElpsProtectionSwitchTrap=NotificationType((1,3,6,1,4,1,10876,101,2,25,4,0,1))
fsElpsProtectionSwitchTrap.setObjects(*((_C,_L),(_C,_M),(_C,_n)))
if mibBuilder.loadTexts:fsElpsProtectionSwitchTrap.setStatus(_A)
fsElpsProtectionSwitchFailureTrap=NotificationType((1,3,6,1,4,1,10876,101,2,25,4,0,2))
fsElpsProtectionSwitchFailureTrap.setObjects(*((_C,_L),(_C,_M),(_C,_o)))
if mibBuilder.loadTexts:fsElpsProtectionSwitchFailureTrap.setStatus(_A)
fsElpsProtectionTypeMismatchTrap=NotificationType((1,3,6,1,4,1,10876,101,2,25,4,0,3))
fsElpsProtectionTypeMismatchTrap.setObjects(*((_C,_L),(_C,_M),(_C,_p)))
if mibBuilder.loadTexts:fsElpsProtectionTypeMismatchTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'PgId':PgId,_g:PgType,_h:PgServiceType,'PgServiceValue':PgServiceValue,'PgServiceValueOrNone':PgServiceValueOrNone,_i:PgMonitorMechanismType,_j:PgExtCmd,'PgLocalCondition':PgLocalCondition,'PgFarEndRequest':PgFarEndRequest,'PgActiveRequest':PgActiveRequest,'PgSemState':PgSemState,'PgStatus':PgStatus,'fselps':fselps,'fsElpsSystem':fsElpsSystem,'fsElpsGlobalTraceOption':fsElpsGlobalTraceOption,'fsElpsPSCChannelCode':fsElpsPSCChannelCode,'fsElpsRapidTxTime':fsElpsRapidTxTime,'fsElpsContext':fsElpsContext,'fsElpsContextTable':fsElpsContextTable,'fsElpsContextEntry':fsElpsContextEntry,_G:fsElpsContextId,'fsElpsContextSystemControl':fsElpsContextSystemControl,'fsElpsContextModuleStatus':fsElpsContextModuleStatus,'fsElpsContextTraceInputString':fsElpsContextTraceInputString,'fsElpsContextEnableTrap':fsElpsContextEnableTrap,'fsElpsContextVlanGroupManager':fsElpsContextVlanGroupManager,'fsElpsPg':fsElpsPg,'fsElpsPgConfigTable':fsElpsPgConfigTable,'fsElpsPgConfigEntry':fsElpsPgConfigEntry,_H:fsElpsPgConfigPgId,'fsElpsPgConfigType':fsElpsPgConfigType,'fsElpsPgConfigServiceType':fsElpsPgConfigServiceType,'fsElpsPgConfigMonitorMechanism':fsElpsPgConfigMonitorMechanism,'fsElpsPgConfigIngressPort':fsElpsPgConfigIngressPort,'fsElpsPgConfigWorkingPort':fsElpsPgConfigWorkingPort,'fsElpsPgConfigProtectionPort':fsElpsPgConfigProtectionPort,'fsElpsPgConfigWorkingServiceValue':fsElpsPgConfigWorkingServiceValue,'fsElpsPgConfigProtectionServiceValue':fsElpsPgConfigProtectionServiceValue,'fsElpsPgConfigOperType':fsElpsPgConfigOperType,'fsElpsPgConfigProtType':fsElpsPgConfigProtType,'fsElpsPgConfigName':fsElpsPgConfigName,'fsElpsPgConfigRowStatus':fsElpsPgConfigRowStatus,'fsElpsPgConfigWorkingServicePointer':fsElpsPgConfigWorkingServicePointer,'fsElpsPgConfigWorkingReverseServicePointer':fsElpsPgConfigWorkingReverseServicePointer,'fsElpsPgConfigProtectionServicePointer':fsElpsPgConfigProtectionServicePointer,'fsElpsPgConfigProtectionReverseServicePointer':fsElpsPgConfigProtectionReverseServicePointer,'fsElpsPgConfigWorkingInstanceId':fsElpsPgConfigWorkingInstanceId,'fsElpsPgConfigProtectionInstanceId':fsElpsPgConfigProtectionInstanceId,'fsElpsPgPscVersion':fsElpsPgPscVersion,'fsElpsPgCmdTable':fsElpsPgCmdTable,'fsElpsPgCmdEntry':fsElpsPgCmdEntry,'fsElpsPgCmdHoTime':fsElpsPgCmdHoTime,'fsElpsPgCmdWTR':fsElpsPgCmdWTR,'fsElpsPgCmdExtCmd':fsElpsPgCmdExtCmd,'fsElpsPgCmdExtCmdStatus':fsElpsPgCmdExtCmdStatus,'fsElpsPgCmdLocalCondition':fsElpsPgCmdLocalCondition,'fsElpsPgCmdLocalConditionStatus':fsElpsPgCmdLocalConditionStatus,'fsElpsPgCmdFarEndRequest':fsElpsPgCmdFarEndRequest,'fsElpsPgCmdFarEndRequestStatus':fsElpsPgCmdFarEndRequestStatus,'fsElpsPgCmdActiveRequest':fsElpsPgCmdActiveRequest,'fsElpsPgCmdSemState':fsElpsPgCmdSemState,_M:fsElpsPgCmdPgStatus,'fsElpsPgCmdApsPeriodicTime':fsElpsPgCmdApsPeriodicTime,'fsElpsPgCfmTable':fsElpsPgCfmTable,'fsElpsPgCfmEntry':fsElpsPgCfmEntry,'fsElpsPgCfmWorkingMEG':fsElpsPgCfmWorkingMEG,'fsElpsPgCfmWorkingME':fsElpsPgCfmWorkingME,'fsElpsPgCfmWorkingMEP':fsElpsPgCfmWorkingMEP,'fsElpsPgCfmProtectionMEG':fsElpsPgCfmProtectionMEG,'fsElpsPgCfmProtectionME':fsElpsPgCfmProtectionME,'fsElpsPgCfmProtectionMEP':fsElpsPgCfmProtectionMEP,'fsElpsPgCfmRowStatus':fsElpsPgCfmRowStatus,'fsElpsPgCfmWorkingReverseMEG':fsElpsPgCfmWorkingReverseMEG,'fsElpsPgCfmWorkingReverseME':fsElpsPgCfmWorkingReverseME,'fsElpsPgCfmWorkingReverseMEP':fsElpsPgCfmWorkingReverseMEP,'fsElpsPgCfmProtectionReverseMEG':fsElpsPgCfmProtectionReverseMEG,'fsElpsPgCfmProtectionReverseME':fsElpsPgCfmProtectionReverseME,'fsElpsPgCfmProtectionReverseMEP':fsElpsPgCfmProtectionReverseMEP,'fsElpsPgServiceListTable':fsElpsPgServiceListTable,'fsElpsPgServiceListEntry':fsElpsPgServiceListEntry,_k:fsElpsPgServiceListValue,'fsElpsPgServiceListRowStatus':fsElpsPgServiceListRowStatus,'fsElpsPgShareTable':fsElpsPgShareTable,'fsElpsPgShareEntry':fsElpsPgShareEntry,_l:fsElpsPgShareProtectionPort,'fsElpsPgSharePgStatus':fsElpsPgSharePgStatus,'fsElpsPgStatsTable':fsElpsPgStatsTable,'fsElpsPgStatsEntry':fsElpsPgStatsEntry,'fsElpsPgStatsAutoProtectionSwitchCount':fsElpsPgStatsAutoProtectionSwitchCount,'fsElpsPgStatsForcedSwitchCount':fsElpsPgStatsForcedSwitchCount,'fsElpsPgStatsManualSwitchCount':fsElpsPgStatsManualSwitchCount,'fsElpsPgStatsClearStatistics':fsElpsPgStatsClearStatistics,'fsElpsPgStatsApsPktTxCount':fsElpsPgStatsApsPktTxCount,'fsElpsPgStatsApsPktRxCount':fsElpsPgStatsApsPktRxCount,'fsElpsPgStatsApsPktDiscardCount':fsElpsPgStatsApsPktDiscardCount,'fsElpsPgLRSFRxTime':fsElpsPgLRSFRxTime,'fsElpsPgLRSFTxTime':fsElpsPgLRSFTxTime,'fsElpsPgFRSFRxTime':fsElpsPgFRSFRxTime,'fsElpsPgStateChgTime':fsElpsPgStateChgTime,'fsElpsPgServiceListPointerTable':fsElpsPgServiceListPointerTable,'fsElpsPgServiceListPointerEntry':fsElpsPgServiceListPointerEntry,_m:fsElpsPgServiceListId,'fsElpsPgWorkingServiceListPointer':fsElpsPgWorkingServiceListPointer,'fsElpsPgWorkingReverseServiceListPointer':fsElpsPgWorkingReverseServiceListPointer,'fsElpsPgProtectionServiceListPointer':fsElpsPgProtectionServiceListPointer,'fsElpsPgProtectionReverseServiceListPointer':fsElpsPgProtectionReverseServiceListPointer,'fsElpsPgServiceListPointerRowStatus':fsElpsPgServiceListPointerRowStatus,'fsElpsPgNotifications':fsElpsPgNotifications,'fsElpsTraps':fsElpsTraps,'fsElpsProtectionSwitchTrap':fsElpsProtectionSwitchTrap,'fsElpsProtectionSwitchFailureTrap':fsElpsProtectionSwitchFailureTrap,'fsElpsProtectionTypeMismatchTrap':fsElpsProtectionTypeMismatchTrap,_L:fsElpsTrapContextName,_n:fsElpsTrapSwitchingMechanism,_p:fsElpsTrapMismatchType,_o:fsElpsTypeOfFailure,'fsElpsScalars':fsElpsScalars,'fsElpsStatsOneIsToOneApsPktTxCount':fsElpsStatsOneIsToOneApsPktTxCount,'fsElpsStatsOneIsToOneApsPktRxCount':fsElpsStatsOneIsToOneApsPktRxCount,'fsElpsStatsOneIsToOneApsPktDiscardCount':fsElpsStatsOneIsToOneApsPktDiscardCount,'fsElpsStatsOnePlusOneApsPktTxCount':fsElpsStatsOnePlusOneApsPktTxCount,'fsElpsStatsOnePlusOneApsPktRxCount':fsElpsStatsOnePlusOneApsPktRxCount,'fsElpsStatsOnePlusOneApsPktDiscardCount':fsElpsStatsOnePlusOneApsPktDiscardCount})