_o='fsMIRstOldRoleType'
_n='fsMIRstPortRoleType'
_m='fsMIRstPktErrVal'
_l='fsMIRstPktErrType'
_k='fsMIRstPortMigrationType'
_j='fsMIRstOldDesignatedRoot'
_i='fsMIRstGenTrapType'
_h='fsMIRstGlobalErrTrapType'
_g='fsMIRstPortTrapIndex'
_f='learning'
_e='fsMIRstPort'
_d='disable'
_c='enable'
_b='EnabledStatus'
_a='timerExpiryEvent'
_Z='bpduEvent'
_Y='configurationEvent'
_X='disabled'
_W='fsDot1dStpVersion'
_V='SUPERMICRO-MIStdRSTP-MIB'
_U='fsDot1dStpPortState'
_T='fsDot1dStpDesignatedRoot'
_S='Timeout'
_R='DisplayString'
_Q='none'
_P='designatedPort'
_O='rootPort'
_N='backupPort'
_M='alternatePort'
_L='disabledPort'
_K='not-accessible'
_J='fsMIDot1wFutureRstContextId'
_I='fsMIRstContextName'
_H='TruthValue'
_G='fsDot1dBaseBridgeAddress'
_F='SUPERMICRO-MIStdBRIDGE-MIB'
_E='SUPERMICRO-MIRSTP-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_R,'PhysAddress','RowStatus','TextualConvention',_H)
BridgeId,Timeout,fsDot1dBaseBridgeAddress,fsDot1dStpDesignatedRoot,fsDot1dStpPortState=mibBuilder.importSymbols(_F,'BridgeId',_S,_G,_T,_U)
fsDot1dStpVersion,=mibBuilder.importSymbols(_V,_W)
futureMIRstMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,1,119))
if mibBuilder.loadTexts:futureMIRstMIB.setRevisions(('2012-09-05 00:00',))
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_X,2)))
_FsMIDot1wFutureRst_ObjectIdentity=ObjectIdentity
fsMIDot1wFutureRst=_FsMIDot1wFutureRst_ObjectIdentity((1,3,6,1,4,1,10876,101,1,119,1))
_FsMIRstGlobalTrace_Type=TruthValue
_FsMIRstGlobalTrace_Object=MibScalar
fsMIRstGlobalTrace=_FsMIRstGlobalTrace_Object((1,3,6,1,4,1,10876,101,1,119,1,1),_FsMIRstGlobalTrace_Type())
fsMIRstGlobalTrace.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIRstGlobalTrace.setStatus(_A)
_FsMIRstGlobalDebug_Type=TruthValue
_FsMIRstGlobalDebug_Object=MibScalar
fsMIRstGlobalDebug=_FsMIRstGlobalDebug_Object((1,3,6,1,4,1,10876,101,1,119,1,2),_FsMIRstGlobalDebug_Type())
fsMIRstGlobalDebug.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIRstGlobalDebug.setStatus(_A)
_FsMIDot1wFutureRstTable_Object=MibTable
fsMIDot1wFutureRstTable=_FsMIDot1wFutureRstTable_Object((1,3,6,1,4,1,10876,101,1,119,1,3))
if mibBuilder.loadTexts:fsMIDot1wFutureRstTable.setStatus(_A)
_FsMIDot1wFutureRstEntry_Object=MibTableRow
fsMIDot1wFutureRstEntry=_FsMIDot1wFutureRstEntry_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1))
fsMIDot1wFutureRstEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:fsMIDot1wFutureRstEntry.setStatus(_A)
class _FsMIDot1wFutureRstContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIDot1wFutureRstContextId_Type.__name__=_C
_FsMIDot1wFutureRstContextId_Object=MibTableColumn
fsMIDot1wFutureRstContextId=_FsMIDot1wFutureRstContextId_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1,1),_FsMIDot1wFutureRstContextId_Type())
fsMIDot1wFutureRstContextId.setMaxAccess(_K)
if mibBuilder.loadTexts:fsMIDot1wFutureRstContextId.setStatus(_A)
class _FsMIRstSystemControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsMIRstSystemControl_Type.__name__=_C
_FsMIRstSystemControl_Object=MibTableColumn
fsMIRstSystemControl=_FsMIRstSystemControl_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1,2),_FsMIRstSystemControl_Type())
fsMIRstSystemControl.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIRstSystemControl.setStatus(_A)
_FsMIRstModuleStatus_Type=EnabledStatus
_FsMIRstModuleStatus_Object=MibTableColumn
fsMIRstModuleStatus=_FsMIRstModuleStatus_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1,3),_FsMIRstModuleStatus_Type())
fsMIRstModuleStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIRstModuleStatus.setStatus(_A)
class _FsMIRstTraceOption_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIRstTraceOption_Type.__name__=_C
_FsMIRstTraceOption_Object=MibTableColumn
fsMIRstTraceOption=_FsMIRstTraceOption_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1,4),_FsMIRstTraceOption_Type())
fsMIRstTraceOption.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIRstTraceOption.setStatus(_A)
class _FsMIRstDebugOption_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,524287))
_FsMIRstDebugOption_Type.__name__=_C
_FsMIRstDebugOption_Object=MibTableColumn
fsMIRstDebugOption=_FsMIRstDebugOption_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1,5),_FsMIRstDebugOption_Type())
fsMIRstDebugOption.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIRstDebugOption.setStatus(_A)
_FsMIRstRstpUpCount_Type=Counter32
_FsMIRstRstpUpCount_Object=MibTableColumn
fsMIRstRstpUpCount=_FsMIRstRstpUpCount_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1,6),_FsMIRstRstpUpCount_Type())
fsMIRstRstpUpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstRstpUpCount.setStatus(_A)
_FsMIRstRstpDownCount_Type=Counter32
_FsMIRstRstpDownCount_Object=MibTableColumn
fsMIRstRstpDownCount=_FsMIRstRstpDownCount_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1,7),_FsMIRstRstpDownCount_Type())
fsMIRstRstpDownCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstRstpDownCount.setStatus(_A)
_FsMIRstBufferFailureCount_Type=Counter32
_FsMIRstBufferFailureCount_Object=MibTableColumn
fsMIRstBufferFailureCount=_FsMIRstBufferFailureCount_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1,8),_FsMIRstBufferFailureCount_Type())
fsMIRstBufferFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstBufferFailureCount.setStatus(_A)
_FsMIRstMemAllocFailureCount_Type=Counter32
_FsMIRstMemAllocFailureCount_Object=MibTableColumn
fsMIRstMemAllocFailureCount=_FsMIRstMemAllocFailureCount_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1,9),_FsMIRstMemAllocFailureCount_Type())
fsMIRstMemAllocFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstMemAllocFailureCount.setStatus(_A)
_FsMIRstNewRootIdCount_Type=Counter32
_FsMIRstNewRootIdCount_Object=MibTableColumn
fsMIRstNewRootIdCount=_FsMIRstNewRootIdCount_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1,10),_FsMIRstNewRootIdCount_Type())
fsMIRstNewRootIdCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstNewRootIdCount.setStatus(_A)
class _FsMIRstPortRoleSelSmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('initbridge',0),('roleselection',1)))
_FsMIRstPortRoleSelSmState_Type.__name__=_C
_FsMIRstPortRoleSelSmState_Object=MibTableColumn
fsMIRstPortRoleSelSmState=_FsMIRstPortRoleSelSmState_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1,11),_FsMIRstPortRoleSelSmState_Type())
fsMIRstPortRoleSelSmState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortRoleSelSmState.setStatus(_A)
_FsMIRstOldDesignatedRoot_Type=BridgeId
_FsMIRstOldDesignatedRoot_Object=MibTableColumn
fsMIRstOldDesignatedRoot=_FsMIRstOldDesignatedRoot_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1,12),_FsMIRstOldDesignatedRoot_Type())
fsMIRstOldDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstOldDesignatedRoot.setStatus(_A)
class _FsMIRstDynamicPathcostCalculation_Type(TruthValue):defaultValue=2
_FsMIRstDynamicPathcostCalculation_Type.__name__=_H
_FsMIRstDynamicPathcostCalculation_Object=MibTableColumn
fsMIRstDynamicPathcostCalculation=_FsMIRstDynamicPathcostCalculation_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1,13),_FsMIRstDynamicPathcostCalculation_Type())
fsMIRstDynamicPathcostCalculation.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIRstDynamicPathcostCalculation.setStatus(_A)
class _FsMIRstContextName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsMIRstContextName_Type.__name__=_R
_FsMIRstContextName_Object=MibTableColumn
fsMIRstContextName=_FsMIRstContextName_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1,14),_FsMIRstContextName_Type())
fsMIRstContextName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstContextName.setStatus(_A)
class _FsMIRstCalcPortPathCostOnSpeedChg_Type(TruthValue):defaultValue=2
_FsMIRstCalcPortPathCostOnSpeedChg_Type.__name__=_H
_FsMIRstCalcPortPathCostOnSpeedChg_Object=MibTableColumn
fsMIRstCalcPortPathCostOnSpeedChg=_FsMIRstCalcPortPathCostOnSpeedChg_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1,15),_FsMIRstCalcPortPathCostOnSpeedChg_Type())
fsMIRstCalcPortPathCostOnSpeedChg.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIRstCalcPortPathCostOnSpeedChg.setStatus(_A)
_FsMIRstClearBridgeStats_Type=TruthValue
_FsMIRstClearBridgeStats_Object=MibTableColumn
fsMIRstClearBridgeStats=_FsMIRstClearBridgeStats_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1,16),_FsMIRstClearBridgeStats_Type())
fsMIRstClearBridgeStats.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIRstClearBridgeStats.setStatus(_A)
class _FsMIRstRcvdEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Y,1),(_Z,2),(_a,3)))
_FsMIRstRcvdEvent_Type.__name__=_C
_FsMIRstRcvdEvent_Object=MibTableColumn
fsMIRstRcvdEvent=_FsMIRstRcvdEvent_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1,17),_FsMIRstRcvdEvent_Type())
fsMIRstRcvdEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstRcvdEvent.setStatus(_A)
_FsMIRstRcvdEventSubType_Type=Integer32
_FsMIRstRcvdEventSubType_Object=MibTableColumn
fsMIRstRcvdEventSubType=_FsMIRstRcvdEventSubType_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1,18),_FsMIRstRcvdEventSubType_Type())
fsMIRstRcvdEventSubType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstRcvdEventSubType.setStatus(_A)
_FsMIRstRcvdEventTimeStamp_Type=Unsigned32
_FsMIRstRcvdEventTimeStamp_Object=MibTableColumn
fsMIRstRcvdEventTimeStamp=_FsMIRstRcvdEventTimeStamp_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1,19),_FsMIRstRcvdEventTimeStamp_Type())
fsMIRstRcvdEventTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstRcvdEventTimeStamp.setStatus(_A)
_FsMIRstRcvdPortStateChangeTimeStamp_Type=Unsigned32
_FsMIRstRcvdPortStateChangeTimeStamp_Object=MibTableColumn
fsMIRstRcvdPortStateChangeTimeStamp=_FsMIRstRcvdPortStateChangeTimeStamp_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1,20),_FsMIRstRcvdPortStateChangeTimeStamp_Type())
fsMIRstRcvdPortStateChangeTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstRcvdPortStateChangeTimeStamp.setStatus(_A)
class _FsMIRstFlushInterval_Type(Timeout):defaultValue=0;subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_FsMIRstFlushInterval_Type.__name__=_S
_FsMIRstFlushInterval_Object=MibTableColumn
fsMIRstFlushInterval=_FsMIRstFlushInterval_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1,21),_FsMIRstFlushInterval_Type())
fsMIRstFlushInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIRstFlushInterval.setStatus(_A)
if mibBuilder.loadTexts:fsMIRstFlushInterval.setUnits('centi-seconds')
class _FsMIRstFlushIndicationThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIRstFlushIndicationThreshold_Type.__name__=_C
_FsMIRstFlushIndicationThreshold_Object=MibTableColumn
fsMIRstFlushIndicationThreshold=_FsMIRstFlushIndicationThreshold_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1,22),_FsMIRstFlushIndicationThreshold_Type())
fsMIRstFlushIndicationThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIRstFlushIndicationThreshold.setStatus(_A)
_FsMIRstTotalFlushCount_Type=Counter32
_FsMIRstTotalFlushCount_Object=MibTableColumn
fsMIRstTotalFlushCount=_FsMIRstTotalFlushCount_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1,23),_FsMIRstTotalFlushCount_Type())
fsMIRstTotalFlushCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstTotalFlushCount.setStatus(_A)
class _FsMIRstFwdDelayAltPortRoleTrOptimization_Type(EnabledStatus):defaultValue=1
_FsMIRstFwdDelayAltPortRoleTrOptimization_Type.__name__=_b
_FsMIRstFwdDelayAltPortRoleTrOptimization_Object=MibTableColumn
fsMIRstFwdDelayAltPortRoleTrOptimization=_FsMIRstFwdDelayAltPortRoleTrOptimization_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1,24),_FsMIRstFwdDelayAltPortRoleTrOptimization_Type())
fsMIRstFwdDelayAltPortRoleTrOptimization.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIRstFwdDelayAltPortRoleTrOptimization.setStatus(_A)
class _FsMIRstBpduGuard_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_c,1),(_d,2)))
_FsMIRstBpduGuard_Type.__name__=_C
_FsMIRstBpduGuard_Object=MibTableColumn
fsMIRstBpduGuard=_FsMIRstBpduGuard_Object((1,3,6,1,4,1,10876,101,1,119,1,3,1,25),_FsMIRstBpduGuard_Type())
fsMIRstBpduGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIRstBpduGuard.setStatus(_A)
_FsMIRstPortExtTable_Object=MibTable
fsMIRstPortExtTable=_FsMIRstPortExtTable_Object((1,3,6,1,4,1,10876,101,1,119,1,4))
if mibBuilder.loadTexts:fsMIRstPortExtTable.setStatus(_A)
_FsMIRstPortExtEntry_Object=MibTableRow
fsMIRstPortExtEntry=_FsMIRstPortExtEntry_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1))
fsMIRstPortExtEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:fsMIRstPortExtEntry.setStatus(_A)
class _FsMIRstPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_FsMIRstPort_Type.__name__=_C
_FsMIRstPort_Object=MibTableColumn
fsMIRstPort=_FsMIRstPort_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,1),_FsMIRstPort_Type())
fsMIRstPort.setMaxAccess(_K)
if mibBuilder.loadTexts:fsMIRstPort.setStatus(_A)
class _FsMIRstPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_L,0),(_M,1),(_N,2),(_O,3),(_P,4)))
_FsMIRstPortRole_Type.__name__=_C
_FsMIRstPortRole_Object=MibTableColumn
fsMIRstPortRole=_FsMIRstPortRole_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,2),_FsMIRstPortRole_Type())
fsMIRstPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortRole.setStatus(_A)
class _FsMIRstPortOperVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*(('stpCompatible',0),('rstp',2)))
_FsMIRstPortOperVersion_Type.__name__=_C
_FsMIRstPortOperVersion_Object=MibTableColumn
fsMIRstPortOperVersion=_FsMIRstPortOperVersion_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,3),_FsMIRstPortOperVersion_Type())
fsMIRstPortOperVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortOperVersion.setStatus(_A)
class _FsMIRstPortInfoSmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_X,0),('aged',1),('update',2),('superior',3),('repeat',4),('notdesignated',5),('present',6),('receive',7),('inferiordesignated',8)))
_FsMIRstPortInfoSmState_Type.__name__=_C
_FsMIRstPortInfoSmState_Object=MibTableColumn
fsMIRstPortInfoSmState=_FsMIRstPortInfoSmState_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,4),_FsMIRstPortInfoSmState_Type())
fsMIRstPortInfoSmState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortInfoSmState.setStatus(_A)
class _FsMIRstPortMigSmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('checkingrstp',0),('selectingstp',1),('sensing',2)))
_FsMIRstPortMigSmState_Type.__name__=_C
_FsMIRstPortMigSmState_Object=MibTableColumn
fsMIRstPortMigSmState=_FsMIRstPortMigSmState_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,5),_FsMIRstPortMigSmState_Type())
fsMIRstPortMigSmState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortMigSmState.setStatus(_A)
class _FsMIRstPortRoleTransSmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('init',0),('disableport',1),('disabledport',2),('rootport',3),('designatedport',4),('backupport',5),('rootproposed',6),('rootagreed',7),('reroot',8),('rootforward',9),('rootlearn',10),('rerooted',11),('designatedpropose',12),('designatedsynced',13),('designatedretired',14),('designatedforward',15),('designatedlearn',16),('designatedlisten',17)))
_FsMIRstPortRoleTransSmState_Type.__name__=_C
_FsMIRstPortRoleTransSmState_Object=MibTableColumn
fsMIRstPortRoleTransSmState=_FsMIRstPortRoleTransSmState_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,6),_FsMIRstPortRoleTransSmState_Type())
fsMIRstPortRoleTransSmState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortRoleTransSmState.setStatus(_A)
class _FsMIRstPortStateTransSmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('discarding',0),(_f,1),('forwarding',2)))
_FsMIRstPortStateTransSmState_Type.__name__=_C
_FsMIRstPortStateTransSmState_Object=MibTableColumn
fsMIRstPortStateTransSmState=_FsMIRstPortStateTransSmState_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,7),_FsMIRstPortStateTransSmState_Type())
fsMIRstPortStateTransSmState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortStateTransSmState.setStatus(_A)
class _FsMIRstPortTopoChSmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('inactive',0),(_f,1),('detected',2),('active',3),('notifiedtcn',4),('notifiedtc',5),('propagating',6),('acknowledged',7)))
_FsMIRstPortTopoChSmState_Type.__name__=_C
_FsMIRstPortTopoChSmState_Object=MibTableColumn
fsMIRstPortTopoChSmState=_FsMIRstPortTopoChSmState_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,8),_FsMIRstPortTopoChSmState_Type())
fsMIRstPortTopoChSmState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortTopoChSmState.setStatus(_A)
class _FsMIRstPortTxSmState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('transmitinit',0),('transmitperiodic',1),('transmitconfig',2),('transmittcn',3),('transmitrstp',4),('idle',5)))
_FsMIRstPortTxSmState_Type.__name__=_C
_FsMIRstPortTxSmState_Object=MibTableColumn
fsMIRstPortTxSmState=_FsMIRstPortTxSmState_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,9),_FsMIRstPortTxSmState_Type())
fsMIRstPortTxSmState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortTxSmState.setStatus(_A)
_FsMIRstPortRxRstBpduCount_Type=Counter32
_FsMIRstPortRxRstBpduCount_Object=MibTableColumn
fsMIRstPortRxRstBpduCount=_FsMIRstPortRxRstBpduCount_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,10),_FsMIRstPortRxRstBpduCount_Type())
fsMIRstPortRxRstBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortRxRstBpduCount.setStatus(_A)
_FsMIRstPortRxConfigBpduCount_Type=Counter32
_FsMIRstPortRxConfigBpduCount_Object=MibTableColumn
fsMIRstPortRxConfigBpduCount=_FsMIRstPortRxConfigBpduCount_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,11),_FsMIRstPortRxConfigBpduCount_Type())
fsMIRstPortRxConfigBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortRxConfigBpduCount.setStatus(_A)
_FsMIRstPortRxTcnBpduCount_Type=Counter32
_FsMIRstPortRxTcnBpduCount_Object=MibTableColumn
fsMIRstPortRxTcnBpduCount=_FsMIRstPortRxTcnBpduCount_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,12),_FsMIRstPortRxTcnBpduCount_Type())
fsMIRstPortRxTcnBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortRxTcnBpduCount.setStatus(_A)
_FsMIRstPortTxRstBpduCount_Type=Counter32
_FsMIRstPortTxRstBpduCount_Object=MibTableColumn
fsMIRstPortTxRstBpduCount=_FsMIRstPortTxRstBpduCount_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,13),_FsMIRstPortTxRstBpduCount_Type())
fsMIRstPortTxRstBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortTxRstBpduCount.setStatus(_A)
_FsMIRstPortTxConfigBpduCount_Type=Counter32
_FsMIRstPortTxConfigBpduCount_Object=MibTableColumn
fsMIRstPortTxConfigBpduCount=_FsMIRstPortTxConfigBpduCount_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,14),_FsMIRstPortTxConfigBpduCount_Type())
fsMIRstPortTxConfigBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortTxConfigBpduCount.setStatus(_A)
_FsMIRstPortTxTcnBpduCount_Type=Counter32
_FsMIRstPortTxTcnBpduCount_Object=MibTableColumn
fsMIRstPortTxTcnBpduCount=_FsMIRstPortTxTcnBpduCount_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,15),_FsMIRstPortTxTcnBpduCount_Type())
fsMIRstPortTxTcnBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortTxTcnBpduCount.setStatus(_A)
_FsMIRstPortInvalidRstBpduRxCount_Type=Counter32
_FsMIRstPortInvalidRstBpduRxCount_Object=MibTableColumn
fsMIRstPortInvalidRstBpduRxCount=_FsMIRstPortInvalidRstBpduRxCount_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,16),_FsMIRstPortInvalidRstBpduRxCount_Type())
fsMIRstPortInvalidRstBpduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortInvalidRstBpduRxCount.setStatus(_A)
_FsMIRstPortInvalidConfigBpduRxCount_Type=Counter32
_FsMIRstPortInvalidConfigBpduRxCount_Object=MibTableColumn
fsMIRstPortInvalidConfigBpduRxCount=_FsMIRstPortInvalidConfigBpduRxCount_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,17),_FsMIRstPortInvalidConfigBpduRxCount_Type())
fsMIRstPortInvalidConfigBpduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortInvalidConfigBpduRxCount.setStatus(_A)
_FsMIRstPortInvalidTcnBpduRxCount_Type=Counter32
_FsMIRstPortInvalidTcnBpduRxCount_Object=MibTableColumn
fsMIRstPortInvalidTcnBpduRxCount=_FsMIRstPortInvalidTcnBpduRxCount_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,18),_FsMIRstPortInvalidTcnBpduRxCount_Type())
fsMIRstPortInvalidTcnBpduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortInvalidTcnBpduRxCount.setStatus(_A)
_FsMIRstPortProtocolMigrationCount_Type=Counter32
_FsMIRstPortProtocolMigrationCount_Object=MibTableColumn
fsMIRstPortProtocolMigrationCount=_FsMIRstPortProtocolMigrationCount_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,19),_FsMIRstPortProtocolMigrationCount_Type())
fsMIRstPortProtocolMigrationCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortProtocolMigrationCount.setStatus(_A)
_FsMIRstPortEffectivePortState_Type=TruthValue
_FsMIRstPortEffectivePortState_Object=MibTableColumn
fsMIRstPortEffectivePortState=_FsMIRstPortEffectivePortState_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,20),_FsMIRstPortEffectivePortState_Type())
fsMIRstPortEffectivePortState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortEffectivePortState.setStatus(_A)
_FsMIRstPortAutoEdge_Type=TruthValue
_FsMIRstPortAutoEdge_Object=MibTableColumn
fsMIRstPortAutoEdge=_FsMIRstPortAutoEdge_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,21),_FsMIRstPortAutoEdge_Type())
fsMIRstPortAutoEdge.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIRstPortAutoEdge.setStatus(_A)
_FsMIRstPortRestrictedRole_Type=TruthValue
_FsMIRstPortRestrictedRole_Object=MibTableColumn
fsMIRstPortRestrictedRole=_FsMIRstPortRestrictedRole_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,22),_FsMIRstPortRestrictedRole_Type())
fsMIRstPortRestrictedRole.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIRstPortRestrictedRole.setStatus(_A)
_FsMIRstPortRestrictedTCN_Type=TruthValue
_FsMIRstPortRestrictedTCN_Object=MibTableColumn
fsMIRstPortRestrictedTCN=_FsMIRstPortRestrictedTCN_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,23),_FsMIRstPortRestrictedTCN_Type())
fsMIRstPortRestrictedTCN.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIRstPortRestrictedTCN.setStatus(_A)
class _FsMIRstPortEnableBPDURx_Type(TruthValue):defaultValue=1
_FsMIRstPortEnableBPDURx_Type.__name__=_H
_FsMIRstPortEnableBPDURx_Object=MibTableColumn
fsMIRstPortEnableBPDURx=_FsMIRstPortEnableBPDURx_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,24),_FsMIRstPortEnableBPDURx_Type())
fsMIRstPortEnableBPDURx.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIRstPortEnableBPDURx.setStatus(_A)
class _FsMIRstPortEnableBPDUTx_Type(TruthValue):defaultValue=1
_FsMIRstPortEnableBPDUTx_Type.__name__=_H
_FsMIRstPortEnableBPDUTx_Object=MibTableColumn
fsMIRstPortEnableBPDUTx=_FsMIRstPortEnableBPDUTx_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,25),_FsMIRstPortEnableBPDUTx_Type())
fsMIRstPortEnableBPDUTx.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIRstPortEnableBPDUTx.setStatus(_A)
_FsMIRstPortPseudoRootId_Type=BridgeId
_FsMIRstPortPseudoRootId_Object=MibTableColumn
fsMIRstPortPseudoRootId=_FsMIRstPortPseudoRootId_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,26),_FsMIRstPortPseudoRootId_Type())
fsMIRstPortPseudoRootId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIRstPortPseudoRootId.setStatus(_A)
class _FsMIRstPortIsL2Gp_Type(TruthValue):defaultValue=2
_FsMIRstPortIsL2Gp_Type.__name__=_H
_FsMIRstPortIsL2Gp_Object=MibTableColumn
fsMIRstPortIsL2Gp=_FsMIRstPortIsL2Gp_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,27),_FsMIRstPortIsL2Gp_Type())
fsMIRstPortIsL2Gp.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIRstPortIsL2Gp.setStatus(_A)
class _FsMIRstPortLoopGuard_Type(TruthValue):defaultValue=2
_FsMIRstPortLoopGuard_Type.__name__=_H
_FsMIRstPortLoopGuard_Object=MibTableColumn
fsMIRstPortLoopGuard=_FsMIRstPortLoopGuard_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,28),_FsMIRstPortLoopGuard_Type())
fsMIRstPortLoopGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIRstPortLoopGuard.setStatus(_A)
_FsMIRstPortClearStats_Type=TruthValue
_FsMIRstPortClearStats_Object=MibTableColumn
fsMIRstPortClearStats=_FsMIRstPortClearStats_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,29),_FsMIRstPortClearStats_Type())
fsMIRstPortClearStats.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIRstPortClearStats.setStatus(_A)
class _FsMIRstPortRcvdEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Y,1),(_Z,2),(_a,3)))
_FsMIRstPortRcvdEvent_Type.__name__=_C
_FsMIRstPortRcvdEvent_Object=MibTableColumn
fsMIRstPortRcvdEvent=_FsMIRstPortRcvdEvent_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,30),_FsMIRstPortRcvdEvent_Type())
fsMIRstPortRcvdEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortRcvdEvent.setStatus(_A)
_FsMIRstPortRcvdEventSubType_Type=Integer32
_FsMIRstPortRcvdEventSubType_Object=MibTableColumn
fsMIRstPortRcvdEventSubType=_FsMIRstPortRcvdEventSubType_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,31),_FsMIRstPortRcvdEventSubType_Type())
fsMIRstPortRcvdEventSubType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortRcvdEventSubType.setStatus(_A)
_FsMIRstPortRcvdEventTimeStamp_Type=Unsigned32
_FsMIRstPortRcvdEventTimeStamp_Object=MibTableColumn
fsMIRstPortRcvdEventTimeStamp=_FsMIRstPortRcvdEventTimeStamp_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,32),_FsMIRstPortRcvdEventTimeStamp_Type())
fsMIRstPortRcvdEventTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortRcvdEventTimeStamp.setStatus(_A)
_FsMIRstPortStateChangeTimeStamp_Type=Unsigned32
_FsMIRstPortStateChangeTimeStamp_Object=MibTableColumn
fsMIRstPortStateChangeTimeStamp=_FsMIRstPortStateChangeTimeStamp_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,33),_FsMIRstPortStateChangeTimeStamp_Type())
fsMIRstPortStateChangeTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortStateChangeTimeStamp.setStatus(_A)
_FsMIRstPortRowStatus_Type=RowStatus
_FsMIRstPortRowStatus_Object=MibTableColumn
fsMIRstPortRowStatus=_FsMIRstPortRowStatus_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,34),_FsMIRstPortRowStatus_Type())
fsMIRstPortRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:fsMIRstPortRowStatus.setStatus(_A)
class _FsMIRstLoopInconsistentState_Type(TruthValue):defaultValue=2
_FsMIRstLoopInconsistentState_Type.__name__=_H
_FsMIRstLoopInconsistentState_Object=MibTableColumn
fsMIRstLoopInconsistentState=_FsMIRstLoopInconsistentState_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,35),_FsMIRstLoopInconsistentState_Type())
fsMIRstLoopInconsistentState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstLoopInconsistentState.setStatus(_A)
class _FsMIRstPortBpduGuard_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Q,0),(_c,1),(_d,2)))
_FsMIRstPortBpduGuard_Type.__name__=_C
_FsMIRstPortBpduGuard_Object=MibTableColumn
fsMIRstPortBpduGuard=_FsMIRstPortBpduGuard_Object((1,3,6,1,4,1,10876,101,1,119,1,4,1,36),_FsMIRstPortBpduGuard_Type())
fsMIRstPortBpduGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIRstPortBpduGuard.setStatus(_A)
_FsMIDot1wFsRstTrapsControl_ObjectIdentity=ObjectIdentity
fsMIDot1wFsRstTrapsControl=_FsMIDot1wFsRstTrapsControl_ObjectIdentity((1,3,6,1,4,1,10876,101,1,119,2))
class _FsMIRstSetGlobalTraps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsMIRstSetGlobalTraps_Type.__name__=_C
_FsMIRstSetGlobalTraps_Object=MibScalar
fsMIRstSetGlobalTraps=_FsMIRstSetGlobalTraps_Object((1,3,6,1,4,1,10876,101,1,119,2,1),_FsMIRstSetGlobalTraps_Type())
fsMIRstSetGlobalTraps.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIRstSetGlobalTraps.setStatus(_A)
class _FsMIRstGlobalErrTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Q,0),('memfail',1),('bufffail',2)))
_FsMIRstGlobalErrTrapType_Type.__name__=_C
_FsMIRstGlobalErrTrapType_Object=MibScalar
fsMIRstGlobalErrTrapType=_FsMIRstGlobalErrTrapType_Object((1,3,6,1,4,1,10876,101,1,119,2,2),_FsMIRstGlobalErrTrapType_Type())
fsMIRstGlobalErrTrapType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstGlobalErrTrapType.setStatus(_A)
_FsMIDot1wFsRstTrapsControlTable_Object=MibTable
fsMIDot1wFsRstTrapsControlTable=_FsMIDot1wFsRstTrapsControlTable_Object((1,3,6,1,4,1,10876,101,1,119,2,3))
if mibBuilder.loadTexts:fsMIDot1wFsRstTrapsControlTable.setStatus(_A)
_FsMIDot1wFsRstTrapsControlEntry_Object=MibTableRow
fsMIDot1wFsRstTrapsControlEntry=_FsMIDot1wFsRstTrapsControlEntry_Object((1,3,6,1,4,1,10876,101,1,119,2,3,1))
fsMIDot1wFsRstTrapsControlEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:fsMIDot1wFsRstTrapsControlEntry.setStatus(_A)
class _FsMIRstSetTraps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_FsMIRstSetTraps_Type.__name__=_C
_FsMIRstSetTraps_Object=MibTableColumn
fsMIRstSetTraps=_FsMIRstSetTraps_Object((1,3,6,1,4,1,10876,101,1,119,2,3,1,1),_FsMIRstSetTraps_Type())
fsMIRstSetTraps.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIRstSetTraps.setStatus(_A)
class _FsMIRstGenTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Q,0),('up',1),('down',2)))
_FsMIRstGenTrapType_Type.__name__=_C
_FsMIRstGenTrapType_Object=MibTableColumn
fsMIRstGenTrapType=_FsMIRstGenTrapType_Object((1,3,6,1,4,1,10876,101,1,119,2,3,1,2),_FsMIRstGenTrapType_Type())
fsMIRstGenTrapType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstGenTrapType.setStatus(_A)
_FsMIRstPortTrapNotificationTable_Object=MibTable
fsMIRstPortTrapNotificationTable=_FsMIRstPortTrapNotificationTable_Object((1,3,6,1,4,1,10876,101,1,119,2,4))
if mibBuilder.loadTexts:fsMIRstPortTrapNotificationTable.setStatus(_A)
_FsMIRstPortTrapNotificationEntry_Object=MibTableRow
fsMIRstPortTrapNotificationEntry=_FsMIRstPortTrapNotificationEntry_Object((1,3,6,1,4,1,10876,101,1,119,2,4,1))
fsMIRstPortTrapNotificationEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:fsMIRstPortTrapNotificationEntry.setStatus(_A)
class _FsMIRstPortTrapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_FsMIRstPortTrapIndex_Type.__name__=_C
_FsMIRstPortTrapIndex_Object=MibTableColumn
fsMIRstPortTrapIndex=_FsMIRstPortTrapIndex_Object((1,3,6,1,4,1,10876,101,1,119,2,4,1,1),_FsMIRstPortTrapIndex_Type())
fsMIRstPortTrapIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:fsMIRstPortTrapIndex.setStatus(_A)
class _FsMIRstPortMigrationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('sendstp',0),('sendrstp',1)))
_FsMIRstPortMigrationType_Type.__name__=_C
_FsMIRstPortMigrationType_Object=MibTableColumn
fsMIRstPortMigrationType=_FsMIRstPortMigrationType_Object((1,3,6,1,4,1,10876,101,1,119,2,4,1,2),_FsMIRstPortMigrationType_Type())
fsMIRstPortMigrationType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortMigrationType.setStatus(_A)
class _FsMIRstPktErrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('protocolIdErr',0),('invalidBpdu',1),('configLengthErr',2),('tcnLengthErr',3),('rstpLengthErr',4),('maxAgeErr',5),('fwdDelayErr',6),('helloTimeErr',7)))
_FsMIRstPktErrType_Type.__name__=_C
_FsMIRstPktErrType_Object=MibTableColumn
fsMIRstPktErrType=_FsMIRstPktErrType_Object((1,3,6,1,4,1,10876,101,1,119,2,4,1,3),_FsMIRstPktErrType_Type())
fsMIRstPktErrType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPktErrType.setStatus(_A)
_FsMIRstPktErrVal_Type=Integer32
_FsMIRstPktErrVal_Object=MibTableColumn
fsMIRstPktErrVal=_FsMIRstPktErrVal_Object((1,3,6,1,4,1,10876,101,1,119,2,4,1,4),_FsMIRstPktErrVal_Type())
fsMIRstPktErrVal.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPktErrVal.setStatus(_A)
class _FsMIRstPortRoleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_L,0),(_M,1),(_N,2),(_O,3),(_P,4)))
_FsMIRstPortRoleType_Type.__name__=_C
_FsMIRstPortRoleType_Object=MibTableColumn
fsMIRstPortRoleType=_FsMIRstPortRoleType_Object((1,3,6,1,4,1,10876,101,1,119,2,4,1,5),_FsMIRstPortRoleType_Type())
fsMIRstPortRoleType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstPortRoleType.setStatus(_A)
class _FsMIRstOldRoleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_L,0),(_M,1),(_N,2),(_O,3),(_P,4)))
_FsMIRstOldRoleType_Type.__name__=_C
_FsMIRstOldRoleType_Object=MibTableColumn
fsMIRstOldRoleType=_FsMIRstOldRoleType_Object((1,3,6,1,4,1,10876,101,1,119,2,4,1,6),_FsMIRstOldRoleType_Type())
fsMIRstOldRoleType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIRstOldRoleType.setStatus(_A)
_FsMIDot1wFutureRstTraps_ObjectIdentity=ObjectIdentity
fsMIDot1wFutureRstTraps=_FsMIDot1wFutureRstTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,119,3))
_FsMIRstTraps_ObjectIdentity=ObjectIdentity
fsMIRstTraps=_FsMIRstTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,119,3,0))
fsMIRstGlobalErrTrap=NotificationType((1,3,6,1,4,1,10876,101,1,119,3,0,1))
fsMIRstGlobalErrTrap.setObjects(*((_F,_G),(_E,_h)))
if mibBuilder.loadTexts:fsMIRstGlobalErrTrap.setStatus(_A)
fsMIRstGenTrap=NotificationType((1,3,6,1,4,1,10876,101,1,119,3,0,2))
fsMIRstGenTrap.setObjects(*((_F,_G),(_E,_I),(_E,_i)))
if mibBuilder.loadTexts:fsMIRstGenTrap.setStatus(_A)
fsMIRstNewRootTrap=NotificationType((1,3,6,1,4,1,10876,101,1,119,3,0,3))
fsMIRstNewRootTrap.setObjects(*((_F,_G),(_E,_I),(_E,_j),(_F,_T)))
if mibBuilder.loadTexts:fsMIRstNewRootTrap.setStatus(_A)
fsMIRstTopologyChgTrap=NotificationType((1,3,6,1,4,1,10876,101,1,119,3,0,4))
fsMIRstTopologyChgTrap.setObjects(*((_F,_G),(_E,_I)))
if mibBuilder.loadTexts:fsMIRstTopologyChgTrap.setStatus(_A)
fsMIRstProtocolMigrationTrap=NotificationType((1,3,6,1,4,1,10876,101,1,119,3,0,5))
fsMIRstProtocolMigrationTrap.setObjects(*((_F,_G),(_E,_I),(_V,_W),(_E,_k)))
if mibBuilder.loadTexts:fsMIRstProtocolMigrationTrap.setStatus(_A)
fsMIRstInvalidBpduRxdTrap=NotificationType((1,3,6,1,4,1,10876,101,1,119,3,0,6))
fsMIRstInvalidBpduRxdTrap.setObjects(*((_F,_G),(_E,_I),(_E,_l),(_E,_m)))
if mibBuilder.loadTexts:fsMIRstInvalidBpduRxdTrap.setStatus(_A)
fsMIRstNewPortRoleTrap=NotificationType((1,3,6,1,4,1,10876,101,1,119,3,0,7))
fsMIRstNewPortRoleTrap.setObjects(*((_F,_G),(_E,_n),(_E,_o)))
if mibBuilder.loadTexts:fsMIRstNewPortRoleTrap.setStatus(_A)
fsMIRstHwFailureTrap=NotificationType((1,3,6,1,4,1,10876,101,1,119,3,0,8))
fsMIRstHwFailureTrap.setObjects(*((_F,_G),(_E,_I),(_F,_U)))
if mibBuilder.loadTexts:fsMIRstHwFailureTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_b:EnabledStatus,'futureMIRstMIB':futureMIRstMIB,'fsMIDot1wFutureRst':fsMIDot1wFutureRst,'fsMIRstGlobalTrace':fsMIRstGlobalTrace,'fsMIRstGlobalDebug':fsMIRstGlobalDebug,'fsMIDot1wFutureRstTable':fsMIDot1wFutureRstTable,'fsMIDot1wFutureRstEntry':fsMIDot1wFutureRstEntry,_J:fsMIDot1wFutureRstContextId,'fsMIRstSystemControl':fsMIRstSystemControl,'fsMIRstModuleStatus':fsMIRstModuleStatus,'fsMIRstTraceOption':fsMIRstTraceOption,'fsMIRstDebugOption':fsMIRstDebugOption,'fsMIRstRstpUpCount':fsMIRstRstpUpCount,'fsMIRstRstpDownCount':fsMIRstRstpDownCount,'fsMIRstBufferFailureCount':fsMIRstBufferFailureCount,'fsMIRstMemAllocFailureCount':fsMIRstMemAllocFailureCount,'fsMIRstNewRootIdCount':fsMIRstNewRootIdCount,'fsMIRstPortRoleSelSmState':fsMIRstPortRoleSelSmState,_j:fsMIRstOldDesignatedRoot,'fsMIRstDynamicPathcostCalculation':fsMIRstDynamicPathcostCalculation,_I:fsMIRstContextName,'fsMIRstCalcPortPathCostOnSpeedChg':fsMIRstCalcPortPathCostOnSpeedChg,'fsMIRstClearBridgeStats':fsMIRstClearBridgeStats,'fsMIRstRcvdEvent':fsMIRstRcvdEvent,'fsMIRstRcvdEventSubType':fsMIRstRcvdEventSubType,'fsMIRstRcvdEventTimeStamp':fsMIRstRcvdEventTimeStamp,'fsMIRstRcvdPortStateChangeTimeStamp':fsMIRstRcvdPortStateChangeTimeStamp,'fsMIRstFlushInterval':fsMIRstFlushInterval,'fsMIRstFlushIndicationThreshold':fsMIRstFlushIndicationThreshold,'fsMIRstTotalFlushCount':fsMIRstTotalFlushCount,'fsMIRstFwdDelayAltPortRoleTrOptimization':fsMIRstFwdDelayAltPortRoleTrOptimization,'fsMIRstBpduGuard':fsMIRstBpduGuard,'fsMIRstPortExtTable':fsMIRstPortExtTable,'fsMIRstPortExtEntry':fsMIRstPortExtEntry,_e:fsMIRstPort,'fsMIRstPortRole':fsMIRstPortRole,'fsMIRstPortOperVersion':fsMIRstPortOperVersion,'fsMIRstPortInfoSmState':fsMIRstPortInfoSmState,'fsMIRstPortMigSmState':fsMIRstPortMigSmState,'fsMIRstPortRoleTransSmState':fsMIRstPortRoleTransSmState,'fsMIRstPortStateTransSmState':fsMIRstPortStateTransSmState,'fsMIRstPortTopoChSmState':fsMIRstPortTopoChSmState,'fsMIRstPortTxSmState':fsMIRstPortTxSmState,'fsMIRstPortRxRstBpduCount':fsMIRstPortRxRstBpduCount,'fsMIRstPortRxConfigBpduCount':fsMIRstPortRxConfigBpduCount,'fsMIRstPortRxTcnBpduCount':fsMIRstPortRxTcnBpduCount,'fsMIRstPortTxRstBpduCount':fsMIRstPortTxRstBpduCount,'fsMIRstPortTxConfigBpduCount':fsMIRstPortTxConfigBpduCount,'fsMIRstPortTxTcnBpduCount':fsMIRstPortTxTcnBpduCount,'fsMIRstPortInvalidRstBpduRxCount':fsMIRstPortInvalidRstBpduRxCount,'fsMIRstPortInvalidConfigBpduRxCount':fsMIRstPortInvalidConfigBpduRxCount,'fsMIRstPortInvalidTcnBpduRxCount':fsMIRstPortInvalidTcnBpduRxCount,'fsMIRstPortProtocolMigrationCount':fsMIRstPortProtocolMigrationCount,'fsMIRstPortEffectivePortState':fsMIRstPortEffectivePortState,'fsMIRstPortAutoEdge':fsMIRstPortAutoEdge,'fsMIRstPortRestrictedRole':fsMIRstPortRestrictedRole,'fsMIRstPortRestrictedTCN':fsMIRstPortRestrictedTCN,'fsMIRstPortEnableBPDURx':fsMIRstPortEnableBPDURx,'fsMIRstPortEnableBPDUTx':fsMIRstPortEnableBPDUTx,'fsMIRstPortPseudoRootId':fsMIRstPortPseudoRootId,'fsMIRstPortIsL2Gp':fsMIRstPortIsL2Gp,'fsMIRstPortLoopGuard':fsMIRstPortLoopGuard,'fsMIRstPortClearStats':fsMIRstPortClearStats,'fsMIRstPortRcvdEvent':fsMIRstPortRcvdEvent,'fsMIRstPortRcvdEventSubType':fsMIRstPortRcvdEventSubType,'fsMIRstPortRcvdEventTimeStamp':fsMIRstPortRcvdEventTimeStamp,'fsMIRstPortStateChangeTimeStamp':fsMIRstPortStateChangeTimeStamp,'fsMIRstPortRowStatus':fsMIRstPortRowStatus,'fsMIRstLoopInconsistentState':fsMIRstLoopInconsistentState,'fsMIRstPortBpduGuard':fsMIRstPortBpduGuard,'fsMIDot1wFsRstTrapsControl':fsMIDot1wFsRstTrapsControl,'fsMIRstSetGlobalTraps':fsMIRstSetGlobalTraps,_h:fsMIRstGlobalErrTrapType,'fsMIDot1wFsRstTrapsControlTable':fsMIDot1wFsRstTrapsControlTable,'fsMIDot1wFsRstTrapsControlEntry':fsMIDot1wFsRstTrapsControlEntry,'fsMIRstSetTraps':fsMIRstSetTraps,_i:fsMIRstGenTrapType,'fsMIRstPortTrapNotificationTable':fsMIRstPortTrapNotificationTable,'fsMIRstPortTrapNotificationEntry':fsMIRstPortTrapNotificationEntry,_g:fsMIRstPortTrapIndex,_k:fsMIRstPortMigrationType,_l:fsMIRstPktErrType,_m:fsMIRstPktErrVal,_n:fsMIRstPortRoleType,_o:fsMIRstOldRoleType,'fsMIDot1wFutureRstTraps':fsMIDot1wFutureRstTraps,'fsMIRstTraps':fsMIRstTraps,'fsMIRstGlobalErrTrap':fsMIRstGlobalErrTrap,'fsMIRstGenTrap':fsMIRstGenTrap,'fsMIRstNewRootTrap':fsMIRstNewRootTrap,'fsMIRstTopologyChgTrap':fsMIRstTopologyChgTrap,'fsMIRstProtocolMigrationTrap':fsMIRstProtocolMigrationTrap,'fsMIRstInvalidBpduRxdTrap':fsMIRstInvalidBpduRxdTrap,'fsMIRstNewPortRoleTrap':fsMIRstNewPortRoleTrap,'fsMIRstHwFailureTrap':fsMIRstHwFailureTrap})