_s='fsMIPvrstInstPortState'
_r='fsMIPvrstOldRoleType'
_q='fsMIPvrstPortRoleType'
_p='fsMIPvrstPktErrVal'
_o='fsMIPvrstPktErrType'
_n='fsMIPvrstPortMigrationType'
_m='fsMIPvrstInstTopChanges'
_l='fsMIPvrstInstDesignatedRoot'
_k='fsMIPvrstInstInstanceDownCount'
_j='fsMIPvrstInstInstanceUpCount'
_i='designatedPort'
_h='rootPort'
_g='backupPort'
_f='alternatePort'
_e='disabledPort'
_d='designated'
_c='backup'
_b='alternate'
_a='sendstp'
_Z='sendrstp'
_Y='forwarding'
_X='learning'
_W='discarding'
_V='fsMIPvrstInstPortIndex'
_U='fsMIPvrstPort'
_T='DisplayString'
_S='OctetString'
_R='fsMIPvrstGenTrapType'
_Q='fsMIPvrstPortTrapIndex'
_P='init'
_O='none'
_N='disable'
_M='enable'
_L='fsMIPvrstInstVlanId'
_K='fsMIFuturePvrstContextId'
_J='TruthValue'
_I='not-accessible'
_H='disabled'
_G='fsMIPvrstContextName'
_F='fsMIPvrstBrgAddress'
_E='read-write'
_D='SUPERMICRO-MIPVRST-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_S,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_T,'MacAddress','PhysAddress','RowStatus','TextualConvention',_J)
futureMIPvrstMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,1,154))
if mibBuilder.loadTexts:futureMIPvrstMIB.setRevisions(('2012-09-05 00:00',))
class BridgeId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class Timeout(TextualConvention,Integer32):status=_A;displayHint='d4'
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_H,2)))
_FsMIFuturePvrst_ObjectIdentity=ObjectIdentity
fsMIFuturePvrst=_FsMIFuturePvrst_ObjectIdentity((1,3,6,1,4,1,10876,101,1,154,1))
_FsMIPvrstGlobalTrace_Type=TruthValue
_FsMIPvrstGlobalTrace_Object=MibScalar
fsMIPvrstGlobalTrace=_FsMIPvrstGlobalTrace_Object((1,3,6,1,4,1,10876,101,1,154,1,1),_FsMIPvrstGlobalTrace_Type())
fsMIPvrstGlobalTrace.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstGlobalTrace.setStatus(_A)
_FsMIPvrstGlobalDebug_Type=TruthValue
_FsMIPvrstGlobalDebug_Object=MibScalar
fsMIPvrstGlobalDebug=_FsMIPvrstGlobalDebug_Object((1,3,6,1,4,1,10876,101,1,154,1,2),_FsMIPvrstGlobalDebug_Type())
fsMIPvrstGlobalDebug.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstGlobalDebug.setStatus(_A)
_FsMIFuturePvrstTable_Object=MibTable
fsMIFuturePvrstTable=_FsMIFuturePvrstTable_Object((1,3,6,1,4,1,10876,101,1,154,1,3))
if mibBuilder.loadTexts:fsMIFuturePvrstTable.setStatus(_A)
_FsMIFuturePvrstEntry_Object=MibTableRow
fsMIFuturePvrstEntry=_FsMIFuturePvrstEntry_Object((1,3,6,1,4,1,10876,101,1,154,1,3,1))
fsMIFuturePvrstEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:fsMIFuturePvrstEntry.setStatus(_A)
class _FsMIFuturePvrstContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIFuturePvrstContextId_Type.__name__=_C
_FsMIFuturePvrstContextId_Object=MibTableColumn
fsMIFuturePvrstContextId=_FsMIFuturePvrstContextId_Object((1,3,6,1,4,1,10876,101,1,154,1,3,1,1),_FsMIFuturePvrstContextId_Type())
fsMIFuturePvrstContextId.setMaxAccess(_I)
if mibBuilder.loadTexts:fsMIFuturePvrstContextId.setStatus(_A)
class _FsMIPvrstSystemControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsMIPvrstSystemControl_Type.__name__=_C
_FsMIPvrstSystemControl_Object=MibTableColumn
fsMIPvrstSystemControl=_FsMIPvrstSystemControl_Object((1,3,6,1,4,1,10876,101,1,154,1,3,1,2),_FsMIPvrstSystemControl_Type())
fsMIPvrstSystemControl.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstSystemControl.setStatus(_A)
_FsMIPvrstModuleStatus_Type=EnabledStatus
_FsMIPvrstModuleStatus_Object=MibTableColumn
fsMIPvrstModuleStatus=_FsMIPvrstModuleStatus_Object((1,3,6,1,4,1,10876,101,1,154,1,3,1,3),_FsMIPvrstModuleStatus_Type())
fsMIPvrstModuleStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstModuleStatus.setStatus(_A)
_FsMIPvrstNoOfActiveInstances_Type=Integer32
_FsMIPvrstNoOfActiveInstances_Object=MibTableColumn
fsMIPvrstNoOfActiveInstances=_FsMIPvrstNoOfActiveInstances_Object((1,3,6,1,4,1,10876,101,1,154,1,3,1,4),_FsMIPvrstNoOfActiveInstances_Type())
fsMIPvrstNoOfActiveInstances.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstNoOfActiveInstances.setStatus(_A)
_FsMIPvrstBrgAddress_Type=MacAddress
_FsMIPvrstBrgAddress_Object=MibTableColumn
fsMIPvrstBrgAddress=_FsMIPvrstBrgAddress_Object((1,3,6,1,4,1,10876,101,1,154,1,3,1,5),_FsMIPvrstBrgAddress_Type())
fsMIPvrstBrgAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstBrgAddress.setStatus(_A)
_FsMIPvrstUpCount_Type=Counter32
_FsMIPvrstUpCount_Object=MibTableColumn
fsMIPvrstUpCount=_FsMIPvrstUpCount_Object((1,3,6,1,4,1,10876,101,1,154,1,3,1,6),_FsMIPvrstUpCount_Type())
fsMIPvrstUpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstUpCount.setStatus(_A)
_FsMIPvrstDownCount_Type=Counter32
_FsMIPvrstDownCount_Object=MibTableColumn
fsMIPvrstDownCount=_FsMIPvrstDownCount_Object((1,3,6,1,4,1,10876,101,1,154,1,3,1,7),_FsMIPvrstDownCount_Type())
fsMIPvrstDownCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstDownCount.setStatus(_A)
class _FsMIPvrstPathCostDefaultType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stp8021d1998',1),('stp8021t2001',2)))
_FsMIPvrstPathCostDefaultType_Type.__name__=_C
_FsMIPvrstPathCostDefaultType_Object=MibTableColumn
fsMIPvrstPathCostDefaultType=_FsMIPvrstPathCostDefaultType_Object((1,3,6,1,4,1,10876,101,1,154,1,3,1,8),_FsMIPvrstPathCostDefaultType_Type())
fsMIPvrstPathCostDefaultType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstPathCostDefaultType.setStatus('obsolete')
class _FsMIPvrstDynamicPathCostCalculation_Type(TruthValue):defaultValue=2
_FsMIPvrstDynamicPathCostCalculation_Type.__name__=_J
_FsMIPvrstDynamicPathCostCalculation_Object=MibTableColumn
fsMIPvrstDynamicPathCostCalculation=_FsMIPvrstDynamicPathCostCalculation_Object((1,3,6,1,4,1,10876,101,1,154,1,3,1,9),_FsMIPvrstDynamicPathCostCalculation_Type())
fsMIPvrstDynamicPathCostCalculation.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstDynamicPathCostCalculation.setStatus(_A)
class _FsMIPvrstTrace_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIPvrstTrace_Type.__name__=_C
_FsMIPvrstTrace_Object=MibTableColumn
fsMIPvrstTrace=_FsMIPvrstTrace_Object((1,3,6,1,4,1,10876,101,1,154,1,3,1,10),_FsMIPvrstTrace_Type())
fsMIPvrstTrace.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstTrace.setStatus(_A)
class _FsMIPvrstDebug_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,131071))
_FsMIPvrstDebug_Type.__name__=_C
_FsMIPvrstDebug_Object=MibTableColumn
fsMIPvrstDebug=_FsMIPvrstDebug_Object((1,3,6,1,4,1,10876,101,1,154,1,3,1,11),_FsMIPvrstDebug_Type())
fsMIPvrstDebug.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstDebug.setStatus(_A)
_FsMIPvrstBufferOverFlowCount_Type=Counter32
_FsMIPvrstBufferOverFlowCount_Object=MibTableColumn
fsMIPvrstBufferOverFlowCount=_FsMIPvrstBufferOverFlowCount_Object((1,3,6,1,4,1,10876,101,1,154,1,3,1,12),_FsMIPvrstBufferOverFlowCount_Type())
fsMIPvrstBufferOverFlowCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstBufferOverFlowCount.setStatus(_A)
_FsMIPvrstMemAllocFailureCount_Type=Counter32
_FsMIPvrstMemAllocFailureCount_Object=MibTableColumn
fsMIPvrstMemAllocFailureCount=_FsMIPvrstMemAllocFailureCount_Object((1,3,6,1,4,1,10876,101,1,154,1,3,1,13),_FsMIPvrstMemAllocFailureCount_Type())
fsMIPvrstMemAllocFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstMemAllocFailureCount.setStatus(_A)
class _FsMIPvrstContextName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsMIPvrstContextName_Type.__name__=_T
_FsMIPvrstContextName_Object=MibTableColumn
fsMIPvrstContextName=_FsMIPvrstContextName_Object((1,3,6,1,4,1,10876,101,1,154,1,3,1,14),_FsMIPvrstContextName_Type())
fsMIPvrstContextName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstContextName.setStatus(_A)
class _FsMIPvrstCalcPortPathCostOnSpeedChg_Type(TruthValue):defaultValue=2
_FsMIPvrstCalcPortPathCostOnSpeedChg_Type.__name__=_J
_FsMIPvrstCalcPortPathCostOnSpeedChg_Object=MibTableColumn
fsMIPvrstCalcPortPathCostOnSpeedChg=_FsMIPvrstCalcPortPathCostOnSpeedChg_Object((1,3,6,1,4,1,10876,101,1,154,1,3,1,15),_FsMIPvrstCalcPortPathCostOnSpeedChg_Type())
fsMIPvrstCalcPortPathCostOnSpeedChg.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstCalcPortPathCostOnSpeedChg.setStatus(_A)
class _FsMIPvrstGlobalBpduGuard_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_FsMIPvrstGlobalBpduGuard_Type.__name__=_C
_FsMIPvrstGlobalBpduGuard_Object=MibTableColumn
fsMIPvrstGlobalBpduGuard=_FsMIPvrstGlobalBpduGuard_Object((1,3,6,1,4,1,10876,101,1,154,1,3,1,16),_FsMIPvrstGlobalBpduGuard_Type())
fsMIPvrstGlobalBpduGuard.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstGlobalBpduGuard.setStatus(_A)
_FsMIFuturePvrstPortTable_Object=MibTable
fsMIFuturePvrstPortTable=_FsMIFuturePvrstPortTable_Object((1,3,6,1,4,1,10876,101,1,154,1,4))
if mibBuilder.loadTexts:fsMIFuturePvrstPortTable.setStatus(_A)
_FsMIFuturePvrstPortEntry_Object=MibTableRow
fsMIFuturePvrstPortEntry=_FsMIFuturePvrstPortEntry_Object((1,3,6,1,4,1,10876,101,1,154,1,4,1))
fsMIFuturePvrstPortEntry.setIndexNames((0,_D,_U))
if mibBuilder.loadTexts:fsMIFuturePvrstPortEntry.setStatus(_A)
class _FsMIPvrstPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsMIPvrstPort_Type.__name__=_C
_FsMIPvrstPort_Object=MibTableColumn
fsMIPvrstPort=_FsMIPvrstPort_Object((1,3,6,1,4,1,10876,101,1,154,1,4,1,1),_FsMIPvrstPort_Type())
fsMIPvrstPort.setMaxAccess(_I)
if mibBuilder.loadTexts:fsMIPvrstPort.setStatus(_A)
_FsMIPvrstPortAdminEdgeStatus_Type=TruthValue
_FsMIPvrstPortAdminEdgeStatus_Object=MibTableColumn
fsMIPvrstPortAdminEdgeStatus=_FsMIPvrstPortAdminEdgeStatus_Object((1,3,6,1,4,1,10876,101,1,154,1,4,1,2),_FsMIPvrstPortAdminEdgeStatus_Type())
fsMIPvrstPortAdminEdgeStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstPortAdminEdgeStatus.setStatus(_A)
_FsMIPvrstPortOperEdgePortStatus_Type=TruthValue
_FsMIPvrstPortOperEdgePortStatus_Object=MibTableColumn
fsMIPvrstPortOperEdgePortStatus=_FsMIPvrstPortOperEdgePortStatus_Object((1,3,6,1,4,1,10876,101,1,154,1,4,1,3),_FsMIPvrstPortOperEdgePortStatus_Type())
fsMIPvrstPortOperEdgePortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstPortOperEdgePortStatus.setStatus(_A)
class _FsMIPvrstBridgeDetectionSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('edge',0),('notedge',1)))
_FsMIPvrstBridgeDetectionSemState_Type.__name__=_C
_FsMIPvrstBridgeDetectionSemState_Object=MibTableColumn
fsMIPvrstBridgeDetectionSemState=_FsMIPvrstBridgeDetectionSemState_Object((1,3,6,1,4,1,10876,101,1,154,1,4,1,4),_FsMIPvrstBridgeDetectionSemState_Type())
fsMIPvrstBridgeDetectionSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstBridgeDetectionSemState.setStatus(_A)
_FsMIPvrstPortEnabledStatus_Type=TruthValue
_FsMIPvrstPortEnabledStatus_Object=MibTableColumn
fsMIPvrstPortEnabledStatus=_FsMIPvrstPortEnabledStatus_Object((1,3,6,1,4,1,10876,101,1,154,1,4,1,5),_FsMIPvrstPortEnabledStatus_Type())
fsMIPvrstPortEnabledStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstPortEnabledStatus.setStatus(_A)
_FsMIPvrstRootGuard_Type=TruthValue
_FsMIPvrstRootGuard_Object=MibTableColumn
fsMIPvrstRootGuard=_FsMIPvrstRootGuard_Object((1,3,6,1,4,1,10876,101,1,154,1,4,1,6),_FsMIPvrstRootGuard_Type())
fsMIPvrstRootGuard.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstRootGuard.setStatus(_A)
class _FsMIPvrstBpduGuard_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_O,0),(_M,1),(_N,2)))
_FsMIPvrstBpduGuard_Type.__name__=_C
_FsMIPvrstBpduGuard_Object=MibTableColumn
fsMIPvrstBpduGuard=_FsMIPvrstBpduGuard_Object((1,3,6,1,4,1,10876,101,1,154,1,4,1,7),_FsMIPvrstBpduGuard_Type())
fsMIPvrstBpduGuard.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstBpduGuard.setStatus(_A)
class _FsMIPvrstEncapType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('dot1Q',0),('isl',1)))
_FsMIPvrstEncapType_Type.__name__=_C
_FsMIPvrstEncapType_Object=MibTableColumn
fsMIPvrstEncapType=_FsMIPvrstEncapType_Object((1,3,6,1,4,1,10876,101,1,154,1,4,1,8),_FsMIPvrstEncapType_Type())
fsMIPvrstEncapType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstEncapType.setStatus(_A)
class _FsMIPvrstPortAdminPointToPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('forceTrue',0),('forceFalse',1),('auto',2)))
_FsMIPvrstPortAdminPointToPoint_Type.__name__=_C
_FsMIPvrstPortAdminPointToPoint_Object=MibTableColumn
fsMIPvrstPortAdminPointToPoint=_FsMIPvrstPortAdminPointToPoint_Object((1,3,6,1,4,1,10876,101,1,154,1,4,1,9),_FsMIPvrstPortAdminPointToPoint_Type())
fsMIPvrstPortAdminPointToPoint.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstPortAdminPointToPoint.setStatus(_A)
_FsMIPvrstPortOperPointToPoint_Type=TruthValue
_FsMIPvrstPortOperPointToPoint_Object=MibTableColumn
fsMIPvrstPortOperPointToPoint=_FsMIPvrstPortOperPointToPoint_Object((1,3,6,1,4,1,10876,101,1,154,1,4,1,10),_FsMIPvrstPortOperPointToPoint_Type())
fsMIPvrstPortOperPointToPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstPortOperPointToPoint.setStatus(_A)
_FsMIPvrstPortInvalidBpdusRcvd_Type=Counter32
_FsMIPvrstPortInvalidBpdusRcvd_Object=MibTableColumn
fsMIPvrstPortInvalidBpdusRcvd=_FsMIPvrstPortInvalidBpdusRcvd_Object((1,3,6,1,4,1,10876,101,1,154,1,4,1,11),_FsMIPvrstPortInvalidBpdusRcvd_Type())
fsMIPvrstPortInvalidBpdusRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstPortInvalidBpdusRcvd.setStatus(_A)
_FsMIPvrstPortInvalidConfigBpduRxCount_Type=Counter32
_FsMIPvrstPortInvalidConfigBpduRxCount_Object=MibTableColumn
fsMIPvrstPortInvalidConfigBpduRxCount=_FsMIPvrstPortInvalidConfigBpduRxCount_Object((1,3,6,1,4,1,10876,101,1,154,1,4,1,12),_FsMIPvrstPortInvalidConfigBpduRxCount_Type())
fsMIPvrstPortInvalidConfigBpduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstPortInvalidConfigBpduRxCount.setStatus(_A)
_FsMIPvrstPortInvalidTcnBpduRxCount_Type=Counter32
_FsMIPvrstPortInvalidTcnBpduRxCount_Object=MibTableColumn
fsMIPvrstPortInvalidTcnBpduRxCount=_FsMIPvrstPortInvalidTcnBpduRxCount_Object((1,3,6,1,4,1,10876,101,1,154,1,4,1,13),_FsMIPvrstPortInvalidTcnBpduRxCount_Type())
fsMIPvrstPortInvalidTcnBpduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstPortInvalidTcnBpduRxCount.setStatus(_A)
_FsMIPvrstPortRowStatus_Type=RowStatus
_FsMIPvrstPortRowStatus_Object=MibTableColumn
fsMIPvrstPortRowStatus=_FsMIPvrstPortRowStatus_Object((1,3,6,1,4,1,10876,101,1,154,1,4,1,14),_FsMIPvrstPortRowStatus_Type())
fsMIPvrstPortRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:fsMIPvrstPortRowStatus.setStatus(_A)
class _FsMIPvrstRootInconsistentState_Type(TruthValue):defaultValue=2
_FsMIPvrstRootInconsistentState_Type.__name__=_J
_FsMIPvrstRootInconsistentState_Object=MibTableColumn
fsMIPvrstRootInconsistentState=_FsMIPvrstRootInconsistentState_Object((1,3,6,1,4,1,10876,101,1,154,1,4,1,15),_FsMIPvrstRootInconsistentState_Type())
fsMIPvrstRootInconsistentState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstRootInconsistentState.setStatus(_A)
_FsMIPvrstInstBridgeTable_Object=MibTable
fsMIPvrstInstBridgeTable=_FsMIPvrstInstBridgeTable_Object((1,3,6,1,4,1,10876,101,1,154,1,5))
if mibBuilder.loadTexts:fsMIPvrstInstBridgeTable.setStatus(_A)
_FsMIPvrstInstBridgeEntry_Object=MibTableRow
fsMIPvrstInstBridgeEntry=_FsMIPvrstInstBridgeEntry_Object((1,3,6,1,4,1,10876,101,1,154,1,5,1))
fsMIPvrstInstBridgeEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:fsMIPvrstInstBridgeEntry.setStatus(_A)
class _FsMIPvrstInstVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsMIPvrstInstVlanId_Type.__name__=_C
_FsMIPvrstInstVlanId_Object=MibTableColumn
fsMIPvrstInstVlanId=_FsMIPvrstInstVlanId_Object((1,3,6,1,4,1,10876,101,1,154,1,5,1,1),_FsMIPvrstInstVlanId_Type())
fsMIPvrstInstVlanId.setMaxAccess(_I)
if mibBuilder.loadTexts:fsMIPvrstInstVlanId.setStatus(_A)
class _FsMIPvrstInstBridgePriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_FsMIPvrstInstBridgePriority_Type.__name__=_C
_FsMIPvrstInstBridgePriority_Object=MibTableColumn
fsMIPvrstInstBridgePriority=_FsMIPvrstInstBridgePriority_Object((1,3,6,1,4,1,10876,101,1,154,1,5,1,2),_FsMIPvrstInstBridgePriority_Type())
fsMIPvrstInstBridgePriority.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstInstBridgePriority.setStatus(_A)
_FsMIPvrstInstRootCost_Type=Integer32
_FsMIPvrstInstRootCost_Object=MibTableColumn
fsMIPvrstInstRootCost=_FsMIPvrstInstRootCost_Object((1,3,6,1,4,1,10876,101,1,154,1,5,1,3),_FsMIPvrstInstRootCost_Type())
fsMIPvrstInstRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstRootCost.setStatus(_A)
_FsMIPvrstInstRootPort_Type=Integer32
_FsMIPvrstInstRootPort_Object=MibTableColumn
fsMIPvrstInstRootPort=_FsMIPvrstInstRootPort_Object((1,3,6,1,4,1,10876,101,1,154,1,5,1,4),_FsMIPvrstInstRootPort_Type())
fsMIPvrstInstRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstRootPort.setStatus(_A)
_FsMIPvrstInstBridgeMaxAge_Type=Timeout
_FsMIPvrstInstBridgeMaxAge_Object=MibTableColumn
fsMIPvrstInstBridgeMaxAge=_FsMIPvrstInstBridgeMaxAge_Object((1,3,6,1,4,1,10876,101,1,154,1,5,1,5),_FsMIPvrstInstBridgeMaxAge_Type())
fsMIPvrstInstBridgeMaxAge.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstInstBridgeMaxAge.setStatus(_A)
_FsMIPvrstInstBridgeHelloTime_Type=Timeout
_FsMIPvrstInstBridgeHelloTime_Object=MibTableColumn
fsMIPvrstInstBridgeHelloTime=_FsMIPvrstInstBridgeHelloTime_Object((1,3,6,1,4,1,10876,101,1,154,1,5,1,6),_FsMIPvrstInstBridgeHelloTime_Type())
fsMIPvrstInstBridgeHelloTime.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstInstBridgeHelloTime.setStatus(_A)
_FsMIPvrstInstBridgeForwardDelay_Type=Timeout
_FsMIPvrstInstBridgeForwardDelay_Object=MibTableColumn
fsMIPvrstInstBridgeForwardDelay=_FsMIPvrstInstBridgeForwardDelay_Object((1,3,6,1,4,1,10876,101,1,154,1,5,1,7),_FsMIPvrstInstBridgeForwardDelay_Type())
fsMIPvrstInstBridgeForwardDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstInstBridgeForwardDelay.setStatus(_A)
_FsMIPvrstInstHoldTime_Type=Integer32
_FsMIPvrstInstHoldTime_Object=MibTableColumn
fsMIPvrstInstHoldTime=_FsMIPvrstInstHoldTime_Object((1,3,6,1,4,1,10876,101,1,154,1,5,1,8),_FsMIPvrstInstHoldTime_Type())
fsMIPvrstInstHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstHoldTime.setStatus(_A)
class _FsMIPvrstInstTxHoldCount_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FsMIPvrstInstTxHoldCount_Type.__name__=_C
_FsMIPvrstInstTxHoldCount_Object=MibTableColumn
fsMIPvrstInstTxHoldCount=_FsMIPvrstInstTxHoldCount_Object((1,3,6,1,4,1,10876,101,1,154,1,5,1,9),_FsMIPvrstInstTxHoldCount_Type())
fsMIPvrstInstTxHoldCount.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstInstTxHoldCount.setStatus(_A)
_FsMIPvrstInstTimeSinceTopologyChange_Type=TimeTicks
_FsMIPvrstInstTimeSinceTopologyChange_Object=MibTableColumn
fsMIPvrstInstTimeSinceTopologyChange=_FsMIPvrstInstTimeSinceTopologyChange_Object((1,3,6,1,4,1,10876,101,1,154,1,5,1,10),_FsMIPvrstInstTimeSinceTopologyChange_Type())
fsMIPvrstInstTimeSinceTopologyChange.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstTimeSinceTopologyChange.setStatus(_A)
_FsMIPvrstInstTopChanges_Type=Counter32
_FsMIPvrstInstTopChanges_Object=MibTableColumn
fsMIPvrstInstTopChanges=_FsMIPvrstInstTopChanges_Object((1,3,6,1,4,1,10876,101,1,154,1,5,1,11),_FsMIPvrstInstTopChanges_Type())
fsMIPvrstInstTopChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstTopChanges.setStatus(_A)
_FsMIPvrstInstNewRootCount_Type=Counter32
_FsMIPvrstInstNewRootCount_Object=MibTableColumn
fsMIPvrstInstNewRootCount=_FsMIPvrstInstNewRootCount_Object((1,3,6,1,4,1,10876,101,1,154,1,5,1,12),_FsMIPvrstInstNewRootCount_Type())
fsMIPvrstInstNewRootCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstNewRootCount.setStatus(_A)
_FsMIPvrstInstInstanceUpCount_Type=Counter32
_FsMIPvrstInstInstanceUpCount_Object=MibTableColumn
fsMIPvrstInstInstanceUpCount=_FsMIPvrstInstInstanceUpCount_Object((1,3,6,1,4,1,10876,101,1,154,1,5,1,13),_FsMIPvrstInstInstanceUpCount_Type())
fsMIPvrstInstInstanceUpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstInstanceUpCount.setStatus(_A)
_FsMIPvrstInstInstanceDownCount_Type=Counter32
_FsMIPvrstInstInstanceDownCount_Object=MibTableColumn
fsMIPvrstInstInstanceDownCount=_FsMIPvrstInstInstanceDownCount_Object((1,3,6,1,4,1,10876,101,1,154,1,5,1,14),_FsMIPvrstInstInstanceDownCount_Type())
fsMIPvrstInstInstanceDownCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstInstanceDownCount.setStatus(_A)
class _FsMIPvrstInstPortRoleSelSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('initbridge',0),('roleselection',1)))
_FsMIPvrstInstPortRoleSelSemState_Type.__name__=_C
_FsMIPvrstInstPortRoleSelSemState_Object=MibTableColumn
fsMIPvrstInstPortRoleSelSemState=_FsMIPvrstInstPortRoleSelSemState_Object((1,3,6,1,4,1,10876,101,1,154,1,5,1,15),_FsMIPvrstInstPortRoleSelSemState_Type())
fsMIPvrstInstPortRoleSelSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortRoleSelSemState.setStatus(_A)
_FsMIPvrstInstDesignatedRoot_Type=BridgeId
_FsMIPvrstInstDesignatedRoot_Object=MibTableColumn
fsMIPvrstInstDesignatedRoot=_FsMIPvrstInstDesignatedRoot_Object((1,3,6,1,4,1,10876,101,1,154,1,5,1,16),_FsMIPvrstInstDesignatedRoot_Type())
fsMIPvrstInstDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstDesignatedRoot.setStatus(_A)
_FsMIPvrstInstRootMaxAge_Type=Timeout
_FsMIPvrstInstRootMaxAge_Object=MibTableColumn
fsMIPvrstInstRootMaxAge=_FsMIPvrstInstRootMaxAge_Object((1,3,6,1,4,1,10876,101,1,154,1,5,1,17),_FsMIPvrstInstRootMaxAge_Type())
fsMIPvrstInstRootMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstRootMaxAge.setStatus(_A)
_FsMIPvrstInstRootHelloTime_Type=Timeout
_FsMIPvrstInstRootHelloTime_Object=MibTableColumn
fsMIPvrstInstRootHelloTime=_FsMIPvrstInstRootHelloTime_Object((1,3,6,1,4,1,10876,101,1,154,1,5,1,18),_FsMIPvrstInstRootHelloTime_Type())
fsMIPvrstInstRootHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstRootHelloTime.setStatus(_A)
_FsMIPvrstInstRootForwardDelay_Type=Timeout
_FsMIPvrstInstRootForwardDelay_Object=MibTableColumn
fsMIPvrstInstRootForwardDelay=_FsMIPvrstInstRootForwardDelay_Object((1,3,6,1,4,1,10876,101,1,154,1,5,1,19),_FsMIPvrstInstRootForwardDelay_Type())
fsMIPvrstInstRootForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstRootForwardDelay.setStatus(_A)
_FsMIPvrstInstPortTable_Object=MibTable
fsMIPvrstInstPortTable=_FsMIPvrstInstPortTable_Object((1,3,6,1,4,1,10876,101,1,154,1,6))
if mibBuilder.loadTexts:fsMIPvrstInstPortTable.setStatus(_A)
_FsMIPvrstInstPortEntry_Object=MibTableRow
fsMIPvrstInstPortEntry=_FsMIPvrstInstPortEntry_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1))
fsMIPvrstInstPortEntry.setIndexNames((0,_D,_L),(0,_D,_V))
if mibBuilder.loadTexts:fsMIPvrstInstPortEntry.setStatus(_A)
class _FsMIPvrstInstPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsMIPvrstInstPortIndex_Type.__name__=_C
_FsMIPvrstInstPortIndex_Object=MibTableColumn
fsMIPvrstInstPortIndex=_FsMIPvrstInstPortIndex_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,1),_FsMIPvrstInstPortIndex_Type())
fsMIPvrstInstPortIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:fsMIPvrstInstPortIndex.setStatus(_A)
class _FsMIPvrstInstPortEnableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_N,2)))
_FsMIPvrstInstPortEnableStatus_Type.__name__=_C
_FsMIPvrstInstPortEnableStatus_Object=MibTableColumn
fsMIPvrstInstPortEnableStatus=_FsMIPvrstInstPortEnableStatus_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,2),_FsMIPvrstInstPortEnableStatus_Type())
fsMIPvrstInstPortEnableStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstInstPortEnableStatus.setStatus(_A)
class _FsMIPvrstInstPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_FsMIPvrstInstPortPathCost_Type.__name__=_C
_FsMIPvrstInstPortPathCost_Object=MibTableColumn
fsMIPvrstInstPortPathCost=_FsMIPvrstInstPortPathCost_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,3),_FsMIPvrstInstPortPathCost_Type())
fsMIPvrstInstPortPathCost.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstInstPortPathCost.setStatus(_A)
class _FsMIPvrstInstPortPriority_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_FsMIPvrstInstPortPriority_Type.__name__=_C
_FsMIPvrstInstPortPriority_Object=MibTableColumn
fsMIPvrstInstPortPriority=_FsMIPvrstInstPortPriority_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,4),_FsMIPvrstInstPortPriority_Type())
fsMIPvrstInstPortPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstInstPortPriority.setStatus(_A)
_FsMIPvrstInstPortDesignatedRoot_Type=BridgeId
_FsMIPvrstInstPortDesignatedRoot_Object=MibTableColumn
fsMIPvrstInstPortDesignatedRoot=_FsMIPvrstInstPortDesignatedRoot_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,5),_FsMIPvrstInstPortDesignatedRoot_Type())
fsMIPvrstInstPortDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortDesignatedRoot.setStatus(_A)
_FsMIPvrstInstPortDesignatedBridge_Type=BridgeId
_FsMIPvrstInstPortDesignatedBridge_Object=MibTableColumn
fsMIPvrstInstPortDesignatedBridge=_FsMIPvrstInstPortDesignatedBridge_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,6),_FsMIPvrstInstPortDesignatedBridge_Type())
fsMIPvrstInstPortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortDesignatedBridge.setStatus(_A)
class _FsMIPvrstInstPortDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_FsMIPvrstInstPortDesignatedPort_Type.__name__=_S
_FsMIPvrstInstPortDesignatedPort_Object=MibTableColumn
fsMIPvrstInstPortDesignatedPort=_FsMIPvrstInstPortDesignatedPort_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,7),_FsMIPvrstInstPortDesignatedPort_Type())
fsMIPvrstInstPortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortDesignatedPort.setStatus(_A)
class _FsMIPvrstInstPortOperVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*(('stpCompatible',0),('rstp',2)))
_FsMIPvrstInstPortOperVersion_Type.__name__=_C
_FsMIPvrstInstPortOperVersion_Object=MibTableColumn
fsMIPvrstInstPortOperVersion=_FsMIPvrstInstPortOperVersion_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,8),_FsMIPvrstInstPortOperVersion_Type())
fsMIPvrstInstPortOperVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortOperVersion.setStatus(_A)
_FsMIPvrstInstPortProtocolMigration_Type=TruthValue
_FsMIPvrstInstPortProtocolMigration_Object=MibTableColumn
fsMIPvrstInstPortProtocolMigration=_FsMIPvrstInstPortProtocolMigration_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,9),_FsMIPvrstInstPortProtocolMigration_Type())
fsMIPvrstInstPortProtocolMigration.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortProtocolMigration.setStatus(_A)
class _FsMIPvrstInstPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5)));namedValues=NamedValues(*((_H,1),(_W,2),(_X,4),(_Y,5)))
_FsMIPvrstInstPortState_Type.__name__=_C
_FsMIPvrstInstPortState_Object=MibTableColumn
fsMIPvrstInstPortState=_FsMIPvrstInstPortState_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,10),_FsMIPvrstInstPortState_Type())
fsMIPvrstInstPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortState.setStatus(_A)
_FsMIPvrstInstPortForwardTransitions_Type=Counter32
_FsMIPvrstInstPortForwardTransitions_Object=MibTableColumn
fsMIPvrstInstPortForwardTransitions=_FsMIPvrstInstPortForwardTransitions_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,11),_FsMIPvrstInstPortForwardTransitions_Type())
fsMIPvrstInstPortForwardTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortForwardTransitions.setStatus(_A)
_FsMIPvrstInstPortReceivedBpdus_Type=Counter32
_FsMIPvrstInstPortReceivedBpdus_Object=MibTableColumn
fsMIPvrstInstPortReceivedBpdus=_FsMIPvrstInstPortReceivedBpdus_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,12),_FsMIPvrstInstPortReceivedBpdus_Type())
fsMIPvrstInstPortReceivedBpdus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortReceivedBpdus.setStatus(_A)
_FsMIPvrstInstPortRxConfigBpduCount_Type=Counter32
_FsMIPvrstInstPortRxConfigBpduCount_Object=MibTableColumn
fsMIPvrstInstPortRxConfigBpduCount=_FsMIPvrstInstPortRxConfigBpduCount_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,13),_FsMIPvrstInstPortRxConfigBpduCount_Type())
fsMIPvrstInstPortRxConfigBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortRxConfigBpduCount.setStatus(_A)
_FsMIPvrstInstPortRxTcnBpduCount_Type=Counter32
_FsMIPvrstInstPortRxTcnBpduCount_Object=MibTableColumn
fsMIPvrstInstPortRxTcnBpduCount=_FsMIPvrstInstPortRxTcnBpduCount_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,14),_FsMIPvrstInstPortRxTcnBpduCount_Type())
fsMIPvrstInstPortRxTcnBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortRxTcnBpduCount.setStatus(_A)
_FsMIPvrstInstPortTransmittedBpdus_Type=Counter32
_FsMIPvrstInstPortTransmittedBpdus_Object=MibTableColumn
fsMIPvrstInstPortTransmittedBpdus=_FsMIPvrstInstPortTransmittedBpdus_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,15),_FsMIPvrstInstPortTransmittedBpdus_Type())
fsMIPvrstInstPortTransmittedBpdus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortTransmittedBpdus.setStatus(_A)
_FsMIPvrstInstPortTxConfigBpduCount_Type=Counter32
_FsMIPvrstInstPortTxConfigBpduCount_Object=MibTableColumn
fsMIPvrstInstPortTxConfigBpduCount=_FsMIPvrstInstPortTxConfigBpduCount_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,16),_FsMIPvrstInstPortTxConfigBpduCount_Type())
fsMIPvrstInstPortTxConfigBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortTxConfigBpduCount.setStatus(_A)
_FsMIPvrstInstPortTxTcnBpduCount_Type=Counter32
_FsMIPvrstInstPortTxTcnBpduCount_Object=MibTableColumn
fsMIPvrstInstPortTxTcnBpduCount=_FsMIPvrstInstPortTxTcnBpduCount_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,17),_FsMIPvrstInstPortTxTcnBpduCount_Type())
fsMIPvrstInstPortTxTcnBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortTxTcnBpduCount.setStatus(_A)
class _FsMIPvrstInstPortTxSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('transmitinit',0),('transmitperiodic',1),('transmitconfig',2),('transmittcn',3),('transmitrstp',4),('idle',5)))
_FsMIPvrstInstPortTxSemState_Type.__name__=_C
_FsMIPvrstInstPortTxSemState_Object=MibTableColumn
fsMIPvrstInstPortTxSemState=_FsMIPvrstInstPortTxSemState_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,18),_FsMIPvrstInstPortTxSemState_Type())
fsMIPvrstInstPortTxSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortTxSemState.setStatus(_A)
class _FsMIPvrstInstPortProtMigrationSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_P,0),(_Z,1),('sendingrstp',2),(_a,3),('sendingstp',4)))
_FsMIPvrstInstPortProtMigrationSemState_Type.__name__=_C
_FsMIPvrstInstPortProtMigrationSemState_Object=MibTableColumn
fsMIPvrstInstPortProtMigrationSemState=_FsMIPvrstInstPortProtMigrationSemState_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,19),_FsMIPvrstInstPortProtMigrationSemState_Type())
fsMIPvrstInstPortProtMigrationSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortProtMigrationSemState.setStatus(_A)
_FsMIPvrstInstProtocolMigrationCount_Type=Counter32
_FsMIPvrstInstProtocolMigrationCount_Object=MibTableColumn
fsMIPvrstInstProtocolMigrationCount=_FsMIPvrstInstProtocolMigrationCount_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,20),_FsMIPvrstInstProtocolMigrationCount_Type())
fsMIPvrstInstProtocolMigrationCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstProtocolMigrationCount.setStatus(_A)
class _FsMIPvrstInstPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_H,0),(_b,1),(_c,2),('root',3),(_d,4)))
_FsMIPvrstInstPortRole_Type.__name__=_C
_FsMIPvrstInstPortRole_Object=MibTableColumn
fsMIPvrstInstPortRole=_FsMIPvrstInstPortRole_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,21),_FsMIPvrstInstPortRole_Type())
fsMIPvrstInstPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortRole.setStatus(_A)
class _FsMIPvrstInstCurrentPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_H,0),(_b,1),(_c,2),('root',3),(_d,4)))
_FsMIPvrstInstCurrentPortRole_Type.__name__=_C
_FsMIPvrstInstCurrentPortRole_Object=MibTableColumn
fsMIPvrstInstCurrentPortRole=_FsMIPvrstInstCurrentPortRole_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,22),_FsMIPvrstInstCurrentPortRole_Type())
fsMIPvrstInstCurrentPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstCurrentPortRole.setStatus(_A)
class _FsMIPvrstInstPortInfoSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_H,0),('aged',1),('update',2),('superior',3),('repeat',4),('agreement',5),('present',6),('receive',7)))
_FsMIPvrstInstPortInfoSemState_Type.__name__=_C
_FsMIPvrstInstPortInfoSemState_Object=MibTableColumn
fsMIPvrstInstPortInfoSemState=_FsMIPvrstInstPortInfoSemState_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,23),_FsMIPvrstInstPortInfoSemState_Type())
fsMIPvrstInstPortInfoSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortInfoSemState.setStatus(_A)
class _FsMIPvrstInstPortRoleTransitionSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_P,0),('blockport',1),('blockedport',2),('rootport',3),('designatedport',4)))
_FsMIPvrstInstPortRoleTransitionSemState_Type.__name__=_C
_FsMIPvrstInstPortRoleTransitionSemState_Object=MibTableColumn
fsMIPvrstInstPortRoleTransitionSemState=_FsMIPvrstInstPortRoleTransitionSemState_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,24),_FsMIPvrstInstPortRoleTransitionSemState_Type())
fsMIPvrstInstPortRoleTransitionSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortRoleTransitionSemState.setStatus(_A)
class _FsMIPvrstInstPortStateTransitionSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_W,0),(_X,1),(_Y,2)))
_FsMIPvrstInstPortStateTransitionSemState_Type.__name__=_C
_FsMIPvrstInstPortStateTransitionSemState_Object=MibTableColumn
fsMIPvrstInstPortStateTransitionSemState=_FsMIPvrstInstPortStateTransitionSemState_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,25),_FsMIPvrstInstPortStateTransitionSemState_Type())
fsMIPvrstInstPortStateTransitionSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortStateTransitionSemState.setStatus(_A)
class _FsMIPvrstInstPortTopologyChangeSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_P,0),('inactive',1),('active',2),('detected',3),('notifiedtcn',4),('notifiedtc',5),('propagating',6),('acknowledged',7)))
_FsMIPvrstInstPortTopologyChangeSemState_Type.__name__=_C
_FsMIPvrstInstPortTopologyChangeSemState_Object=MibTableColumn
fsMIPvrstInstPortTopologyChangeSemState=_FsMIPvrstInstPortTopologyChangeSemState_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,26),_FsMIPvrstInstPortTopologyChangeSemState_Type())
fsMIPvrstInstPortTopologyChangeSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortTopologyChangeSemState.setStatus(_A)
_FsMIPvrstInstPortEffectivePortState_Type=TruthValue
_FsMIPvrstInstPortEffectivePortState_Object=MibTableColumn
fsMIPvrstInstPortEffectivePortState=_FsMIPvrstInstPortEffectivePortState_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,27),_FsMIPvrstInstPortEffectivePortState_Type())
fsMIPvrstInstPortEffectivePortState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortEffectivePortState.setStatus(_A)
_FsMIPvrstInstPortHelloTime_Type=Timeout
_FsMIPvrstInstPortHelloTime_Object=MibTableColumn
fsMIPvrstInstPortHelloTime=_FsMIPvrstInstPortHelloTime_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,28),_FsMIPvrstInstPortHelloTime_Type())
fsMIPvrstInstPortHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortHelloTime.setStatus(_A)
_FsMIPvrstInstPortMaxAge_Type=Timeout
_FsMIPvrstInstPortMaxAge_Object=MibTableColumn
fsMIPvrstInstPortMaxAge=_FsMIPvrstInstPortMaxAge_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,29),_FsMIPvrstInstPortMaxAge_Type())
fsMIPvrstInstPortMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortMaxAge.setStatus(_A)
_FsMIPvrstInstPortForwardDelay_Type=Timeout
_FsMIPvrstInstPortForwardDelay_Object=MibTableColumn
fsMIPvrstInstPortForwardDelay=_FsMIPvrstInstPortForwardDelay_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,30),_FsMIPvrstInstPortForwardDelay_Type())
fsMIPvrstInstPortForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortForwardDelay.setStatus(_A)
_FsMIPvrstInstPortHoldTime_Type=Timeout
_FsMIPvrstInstPortHoldTime_Object=MibTableColumn
fsMIPvrstInstPortHoldTime=_FsMIPvrstInstPortHoldTime_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,31),_FsMIPvrstInstPortHoldTime_Type())
fsMIPvrstInstPortHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstInstPortHoldTime.setStatus(_A)
class _FsMIPvrstInstPortAdminPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_FsMIPvrstInstPortAdminPathCost_Type.__name__=_C
_FsMIPvrstInstPortAdminPathCost_Object=MibTableColumn
fsMIPvrstInstPortAdminPathCost=_FsMIPvrstInstPortAdminPathCost_Object((1,3,6,1,4,1,10876,101,1,154,1,6,1,32),_FsMIPvrstInstPortAdminPathCost_Type())
fsMIPvrstInstPortAdminPathCost.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstInstPortAdminPathCost.setStatus(_A)
_FsMIFsPvrstTrapsControl_ObjectIdentity=ObjectIdentity
fsMIFsPvrstTrapsControl=_FsMIFsPvrstTrapsControl_ObjectIdentity((1,3,6,1,4,1,10876,101,1,154,2))
class _FsMIFsPvrstSetGlobalTrapOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsMIFsPvrstSetGlobalTrapOption_Type.__name__=_C
_FsMIFsPvrstSetGlobalTrapOption_Object=MibScalar
fsMIFsPvrstSetGlobalTrapOption=_FsMIFsPvrstSetGlobalTrapOption_Object((1,3,6,1,4,1,10876,101,1,154,2,1),_FsMIFsPvrstSetGlobalTrapOption_Type())
fsMIFsPvrstSetGlobalTrapOption.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIFsPvrstSetGlobalTrapOption.setStatus(_A)
class _FsMIPvrstGlobalErrTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_O,0),('memfail',1),('bufffail',2)))
_FsMIPvrstGlobalErrTrapType_Type.__name__=_C
_FsMIPvrstGlobalErrTrapType_Object=MibScalar
fsMIPvrstGlobalErrTrapType=_FsMIPvrstGlobalErrTrapType_Object((1,3,6,1,4,1,10876,101,1,154,2,2),_FsMIPvrstGlobalErrTrapType_Type())
fsMIPvrstGlobalErrTrapType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstGlobalErrTrapType.setStatus(_A)
_FsMIFsPvrstTrapsControlTable_Object=MibTable
fsMIFsPvrstTrapsControlTable=_FsMIFsPvrstTrapsControlTable_Object((1,3,6,1,4,1,10876,101,1,154,2,3))
if mibBuilder.loadTexts:fsMIFsPvrstTrapsControlTable.setStatus(_A)
_FsMIFsPvrstTrapsControlEntry_Object=MibTableRow
fsMIFsPvrstTrapsControlEntry=_FsMIFsPvrstTrapsControlEntry_Object((1,3,6,1,4,1,10876,101,1,154,2,3,1))
fsMIFsPvrstTrapsControlEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:fsMIFsPvrstTrapsControlEntry.setStatus(_A)
class _FsMIPvrstSetTraps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_FsMIPvrstSetTraps_Type.__name__=_C
_FsMIPvrstSetTraps_Object=MibTableColumn
fsMIPvrstSetTraps=_FsMIPvrstSetTraps_Object((1,3,6,1,4,1,10876,101,1,154,2,3,1,1),_FsMIPvrstSetTraps_Type())
fsMIPvrstSetTraps.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIPvrstSetTraps.setStatus(_A)
class _FsMIPvrstGenTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_O,0),('up',1),('down',2)))
_FsMIPvrstGenTrapType_Type.__name__=_C
_FsMIPvrstGenTrapType_Object=MibTableColumn
fsMIPvrstGenTrapType=_FsMIPvrstGenTrapType_Object((1,3,6,1,4,1,10876,101,1,154,2,3,1,2),_FsMIPvrstGenTrapType_Type())
fsMIPvrstGenTrapType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstGenTrapType.setStatus(_A)
_FsMIPvrstPortTrapNotificationTable_Object=MibTable
fsMIPvrstPortTrapNotificationTable=_FsMIPvrstPortTrapNotificationTable_Object((1,3,6,1,4,1,10876,101,1,154,2,4))
if mibBuilder.loadTexts:fsMIPvrstPortTrapNotificationTable.setStatus(_A)
_FsMIPvrstPortTrapNotificationEntry_Object=MibTableRow
fsMIPvrstPortTrapNotificationEntry=_FsMIPvrstPortTrapNotificationEntry_Object((1,3,6,1,4,1,10876,101,1,154,2,4,1))
fsMIPvrstPortTrapNotificationEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:fsMIPvrstPortTrapNotificationEntry.setStatus(_A)
class _FsMIPvrstPortTrapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_FsMIPvrstPortTrapIndex_Type.__name__=_C
_FsMIPvrstPortTrapIndex_Object=MibTableColumn
fsMIPvrstPortTrapIndex=_FsMIPvrstPortTrapIndex_Object((1,3,6,1,4,1,10876,101,1,154,2,4,1,1),_FsMIPvrstPortTrapIndex_Type())
fsMIPvrstPortTrapIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:fsMIPvrstPortTrapIndex.setStatus(_A)
class _FsMIPvrstPortMigrationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_a,0),(_Z,1)))
_FsMIPvrstPortMigrationType_Type.__name__=_C
_FsMIPvrstPortMigrationType_Object=MibTableColumn
fsMIPvrstPortMigrationType=_FsMIPvrstPortMigrationType_Object((1,3,6,1,4,1,10876,101,1,154,2,4,1,2),_FsMIPvrstPortMigrationType_Type())
fsMIPvrstPortMigrationType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstPortMigrationType.setStatus(_A)
class _FsMIPvrstPktErrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('protocolIdErr',0),('invalidBpdu',1),('configLengthErr',2),('tcnLengthErr',3),('rstpLengthErr',4),('maxAgeErr',5),('fwdDelayErr',6),('helloTimeErr',7),('pvrstLengthErr',8)))
_FsMIPvrstPktErrType_Type.__name__=_C
_FsMIPvrstPktErrType_Object=MibTableColumn
fsMIPvrstPktErrType=_FsMIPvrstPktErrType_Object((1,3,6,1,4,1,10876,101,1,154,2,4,1,3),_FsMIPvrstPktErrType_Type())
fsMIPvrstPktErrType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstPktErrType.setStatus(_A)
_FsMIPvrstPktErrVal_Type=Integer32
_FsMIPvrstPktErrVal_Object=MibTableColumn
fsMIPvrstPktErrVal=_FsMIPvrstPktErrVal_Object((1,3,6,1,4,1,10876,101,1,154,2,4,1,4),_FsMIPvrstPktErrVal_Type())
fsMIPvrstPktErrVal.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstPktErrVal.setStatus(_A)
_FsMIPvrstPortRoleTrapNotificationTable_Object=MibTable
fsMIPvrstPortRoleTrapNotificationTable=_FsMIPvrstPortRoleTrapNotificationTable_Object((1,3,6,1,4,1,10876,101,1,154,2,5))
if mibBuilder.loadTexts:fsMIPvrstPortRoleTrapNotificationTable.setStatus(_A)
_FsMIPvrstPortRoleTrapNotificationEntry_Object=MibTableRow
fsMIPvrstPortRoleTrapNotificationEntry=_FsMIPvrstPortRoleTrapNotificationEntry_Object((1,3,6,1,4,1,10876,101,1,154,2,5,1))
fsMIPvrstPortRoleTrapNotificationEntry.setIndexNames((0,_D,_Q),(0,_D,_L))
if mibBuilder.loadTexts:fsMIPvrstPortRoleTrapNotificationEntry.setStatus(_A)
class _FsMIPvrstPortRoleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_e,0),(_f,1),(_g,2),(_h,3),(_i,4)))
_FsMIPvrstPortRoleType_Type.__name__=_C
_FsMIPvrstPortRoleType_Object=MibTableColumn
fsMIPvrstPortRoleType=_FsMIPvrstPortRoleType_Object((1,3,6,1,4,1,10876,101,1,154,2,5,1,1),_FsMIPvrstPortRoleType_Type())
fsMIPvrstPortRoleType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstPortRoleType.setStatus(_A)
class _FsMIPvrstOldRoleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_e,0),(_f,1),(_g,2),(_h,3),(_i,4)))
_FsMIPvrstOldRoleType_Type.__name__=_C
_FsMIPvrstOldRoleType_Object=MibTableColumn
fsMIPvrstOldRoleType=_FsMIPvrstOldRoleType_Object((1,3,6,1,4,1,10876,101,1,154,2,5,1,2),_FsMIPvrstOldRoleType_Type())
fsMIPvrstOldRoleType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIPvrstOldRoleType.setStatus(_A)
_FsMIFuturePvrstTraps_ObjectIdentity=ObjectIdentity
fsMIFuturePvrstTraps=_FsMIFuturePvrstTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,154,3))
_FsMIPvrstTraps_ObjectIdentity=ObjectIdentity
fsMIPvrstTraps=_FsMIPvrstTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,154,3,0))
fsMIPvrstGlobalErrTrap=NotificationType((1,3,6,1,4,1,10876,101,1,154,3,0,1))
fsMIPvrstGlobalErrTrap.setObjects(*((_D,_F),(_D,_R),(_D,_j),(_D,_k)))
if mibBuilder.loadTexts:fsMIPvrstGlobalErrTrap.setStatus(_A)
fsMIPvrstGenTrap=NotificationType((1,3,6,1,4,1,10876,101,1,154,3,0,2))
fsMIPvrstGenTrap.setObjects(*((_D,_F),(_D,_G),(_D,_R)))
if mibBuilder.loadTexts:fsMIPvrstGenTrap.setStatus(_A)
fsMIPvrstNewRootTrap=NotificationType((1,3,6,1,4,1,10876,101,1,154,3,0,3))
fsMIPvrstNewRootTrap.setObjects(*((_D,_F),(_D,_G),(_D,_l)))
if mibBuilder.loadTexts:fsMIPvrstNewRootTrap.setStatus(_A)
fsMIPvrstTopologyChgTrap=NotificationType((1,3,6,1,4,1,10876,101,1,154,3,0,4))
fsMIPvrstTopologyChgTrap.setObjects(*((_D,_F),(_D,_G),(_D,_m)))
if mibBuilder.loadTexts:fsMIPvrstTopologyChgTrap.setStatus(_A)
fsMIPvrstProtocolMigrationTrap=NotificationType((1,3,6,1,4,1,10876,101,1,154,3,0,5))
fsMIPvrstProtocolMigrationTrap.setObjects(*((_D,_F),(_D,_G),(_D,_n)))
if mibBuilder.loadTexts:fsMIPvrstProtocolMigrationTrap.setStatus(_A)
fsMIPvrstInvalidBpduRxdTrap=NotificationType((1,3,6,1,4,1,10876,101,1,154,3,0,6))
fsMIPvrstInvalidBpduRxdTrap.setObjects(*((_D,_F),(_D,_G),(_D,_o),(_D,_p)))
if mibBuilder.loadTexts:fsMIPvrstInvalidBpduRxdTrap.setStatus(_A)
fsMIPvrstNewPortRoleTrap=NotificationType((1,3,6,1,4,1,10876,101,1,154,3,0,7))
fsMIPvrstNewPortRoleTrap.setObjects(*((_D,_F),(_D,_q),(_D,_r)))
if mibBuilder.loadTexts:fsMIPvrstNewPortRoleTrap.setStatus(_A)
fsMIPvrstHwFailureTrap=NotificationType((1,3,6,1,4,1,10876,101,1,154,3,0,8))
fsMIPvrstHwFailureTrap.setObjects(*((_D,_F),(_D,_G),(_D,_s)))
if mibBuilder.loadTexts:fsMIPvrstHwFailureTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'BridgeId':BridgeId,'Timeout':Timeout,'EnabledStatus':EnabledStatus,'futureMIPvrstMIB':futureMIPvrstMIB,'fsMIFuturePvrst':fsMIFuturePvrst,'fsMIPvrstGlobalTrace':fsMIPvrstGlobalTrace,'fsMIPvrstGlobalDebug':fsMIPvrstGlobalDebug,'fsMIFuturePvrstTable':fsMIFuturePvrstTable,'fsMIFuturePvrstEntry':fsMIFuturePvrstEntry,_K:fsMIFuturePvrstContextId,'fsMIPvrstSystemControl':fsMIPvrstSystemControl,'fsMIPvrstModuleStatus':fsMIPvrstModuleStatus,'fsMIPvrstNoOfActiveInstances':fsMIPvrstNoOfActiveInstances,_F:fsMIPvrstBrgAddress,'fsMIPvrstUpCount':fsMIPvrstUpCount,'fsMIPvrstDownCount':fsMIPvrstDownCount,'fsMIPvrstPathCostDefaultType':fsMIPvrstPathCostDefaultType,'fsMIPvrstDynamicPathCostCalculation':fsMIPvrstDynamicPathCostCalculation,'fsMIPvrstTrace':fsMIPvrstTrace,'fsMIPvrstDebug':fsMIPvrstDebug,'fsMIPvrstBufferOverFlowCount':fsMIPvrstBufferOverFlowCount,'fsMIPvrstMemAllocFailureCount':fsMIPvrstMemAllocFailureCount,_G:fsMIPvrstContextName,'fsMIPvrstCalcPortPathCostOnSpeedChg':fsMIPvrstCalcPortPathCostOnSpeedChg,'fsMIPvrstGlobalBpduGuard':fsMIPvrstGlobalBpduGuard,'fsMIFuturePvrstPortTable':fsMIFuturePvrstPortTable,'fsMIFuturePvrstPortEntry':fsMIFuturePvrstPortEntry,_U:fsMIPvrstPort,'fsMIPvrstPortAdminEdgeStatus':fsMIPvrstPortAdminEdgeStatus,'fsMIPvrstPortOperEdgePortStatus':fsMIPvrstPortOperEdgePortStatus,'fsMIPvrstBridgeDetectionSemState':fsMIPvrstBridgeDetectionSemState,'fsMIPvrstPortEnabledStatus':fsMIPvrstPortEnabledStatus,'fsMIPvrstRootGuard':fsMIPvrstRootGuard,'fsMIPvrstBpduGuard':fsMIPvrstBpduGuard,'fsMIPvrstEncapType':fsMIPvrstEncapType,'fsMIPvrstPortAdminPointToPoint':fsMIPvrstPortAdminPointToPoint,'fsMIPvrstPortOperPointToPoint':fsMIPvrstPortOperPointToPoint,'fsMIPvrstPortInvalidBpdusRcvd':fsMIPvrstPortInvalidBpdusRcvd,'fsMIPvrstPortInvalidConfigBpduRxCount':fsMIPvrstPortInvalidConfigBpduRxCount,'fsMIPvrstPortInvalidTcnBpduRxCount':fsMIPvrstPortInvalidTcnBpduRxCount,'fsMIPvrstPortRowStatus':fsMIPvrstPortRowStatus,'fsMIPvrstRootInconsistentState':fsMIPvrstRootInconsistentState,'fsMIPvrstInstBridgeTable':fsMIPvrstInstBridgeTable,'fsMIPvrstInstBridgeEntry':fsMIPvrstInstBridgeEntry,_L:fsMIPvrstInstVlanId,'fsMIPvrstInstBridgePriority':fsMIPvrstInstBridgePriority,'fsMIPvrstInstRootCost':fsMIPvrstInstRootCost,'fsMIPvrstInstRootPort':fsMIPvrstInstRootPort,'fsMIPvrstInstBridgeMaxAge':fsMIPvrstInstBridgeMaxAge,'fsMIPvrstInstBridgeHelloTime':fsMIPvrstInstBridgeHelloTime,'fsMIPvrstInstBridgeForwardDelay':fsMIPvrstInstBridgeForwardDelay,'fsMIPvrstInstHoldTime':fsMIPvrstInstHoldTime,'fsMIPvrstInstTxHoldCount':fsMIPvrstInstTxHoldCount,'fsMIPvrstInstTimeSinceTopologyChange':fsMIPvrstInstTimeSinceTopologyChange,_m:fsMIPvrstInstTopChanges,'fsMIPvrstInstNewRootCount':fsMIPvrstInstNewRootCount,_j:fsMIPvrstInstInstanceUpCount,_k:fsMIPvrstInstInstanceDownCount,'fsMIPvrstInstPortRoleSelSemState':fsMIPvrstInstPortRoleSelSemState,_l:fsMIPvrstInstDesignatedRoot,'fsMIPvrstInstRootMaxAge':fsMIPvrstInstRootMaxAge,'fsMIPvrstInstRootHelloTime':fsMIPvrstInstRootHelloTime,'fsMIPvrstInstRootForwardDelay':fsMIPvrstInstRootForwardDelay,'fsMIPvrstInstPortTable':fsMIPvrstInstPortTable,'fsMIPvrstInstPortEntry':fsMIPvrstInstPortEntry,_V:fsMIPvrstInstPortIndex,'fsMIPvrstInstPortEnableStatus':fsMIPvrstInstPortEnableStatus,'fsMIPvrstInstPortPathCost':fsMIPvrstInstPortPathCost,'fsMIPvrstInstPortPriority':fsMIPvrstInstPortPriority,'fsMIPvrstInstPortDesignatedRoot':fsMIPvrstInstPortDesignatedRoot,'fsMIPvrstInstPortDesignatedBridge':fsMIPvrstInstPortDesignatedBridge,'fsMIPvrstInstPortDesignatedPort':fsMIPvrstInstPortDesignatedPort,'fsMIPvrstInstPortOperVersion':fsMIPvrstInstPortOperVersion,'fsMIPvrstInstPortProtocolMigration':fsMIPvrstInstPortProtocolMigration,_s:fsMIPvrstInstPortState,'fsMIPvrstInstPortForwardTransitions':fsMIPvrstInstPortForwardTransitions,'fsMIPvrstInstPortReceivedBpdus':fsMIPvrstInstPortReceivedBpdus,'fsMIPvrstInstPortRxConfigBpduCount':fsMIPvrstInstPortRxConfigBpduCount,'fsMIPvrstInstPortRxTcnBpduCount':fsMIPvrstInstPortRxTcnBpduCount,'fsMIPvrstInstPortTransmittedBpdus':fsMIPvrstInstPortTransmittedBpdus,'fsMIPvrstInstPortTxConfigBpduCount':fsMIPvrstInstPortTxConfigBpduCount,'fsMIPvrstInstPortTxTcnBpduCount':fsMIPvrstInstPortTxTcnBpduCount,'fsMIPvrstInstPortTxSemState':fsMIPvrstInstPortTxSemState,'fsMIPvrstInstPortProtMigrationSemState':fsMIPvrstInstPortProtMigrationSemState,'fsMIPvrstInstProtocolMigrationCount':fsMIPvrstInstProtocolMigrationCount,'fsMIPvrstInstPortRole':fsMIPvrstInstPortRole,'fsMIPvrstInstCurrentPortRole':fsMIPvrstInstCurrentPortRole,'fsMIPvrstInstPortInfoSemState':fsMIPvrstInstPortInfoSemState,'fsMIPvrstInstPortRoleTransitionSemState':fsMIPvrstInstPortRoleTransitionSemState,'fsMIPvrstInstPortStateTransitionSemState':fsMIPvrstInstPortStateTransitionSemState,'fsMIPvrstInstPortTopologyChangeSemState':fsMIPvrstInstPortTopologyChangeSemState,'fsMIPvrstInstPortEffectivePortState':fsMIPvrstInstPortEffectivePortState,'fsMIPvrstInstPortHelloTime':fsMIPvrstInstPortHelloTime,'fsMIPvrstInstPortMaxAge':fsMIPvrstInstPortMaxAge,'fsMIPvrstInstPortForwardDelay':fsMIPvrstInstPortForwardDelay,'fsMIPvrstInstPortHoldTime':fsMIPvrstInstPortHoldTime,'fsMIPvrstInstPortAdminPathCost':fsMIPvrstInstPortAdminPathCost,'fsMIFsPvrstTrapsControl':fsMIFsPvrstTrapsControl,'fsMIFsPvrstSetGlobalTrapOption':fsMIFsPvrstSetGlobalTrapOption,'fsMIPvrstGlobalErrTrapType':fsMIPvrstGlobalErrTrapType,'fsMIFsPvrstTrapsControlTable':fsMIFsPvrstTrapsControlTable,'fsMIFsPvrstTrapsControlEntry':fsMIFsPvrstTrapsControlEntry,'fsMIPvrstSetTraps':fsMIPvrstSetTraps,_R:fsMIPvrstGenTrapType,'fsMIPvrstPortTrapNotificationTable':fsMIPvrstPortTrapNotificationTable,'fsMIPvrstPortTrapNotificationEntry':fsMIPvrstPortTrapNotificationEntry,_Q:fsMIPvrstPortTrapIndex,_n:fsMIPvrstPortMigrationType,_o:fsMIPvrstPktErrType,_p:fsMIPvrstPktErrVal,'fsMIPvrstPortRoleTrapNotificationTable':fsMIPvrstPortRoleTrapNotificationTable,'fsMIPvrstPortRoleTrapNotificationEntry':fsMIPvrstPortRoleTrapNotificationEntry,_q:fsMIPvrstPortRoleType,_r:fsMIPvrstOldRoleType,'fsMIFuturePvrstTraps':fsMIFuturePvrstTraps,'fsMIPvrstTraps':fsMIPvrstTraps,'fsMIPvrstGlobalErrTrap':fsMIPvrstGlobalErrTrap,'fsMIPvrstGenTrap':fsMIPvrstGenTrap,'fsMIPvrstNewRootTrap':fsMIPvrstNewRootTrap,'fsMIPvrstTopologyChgTrap':fsMIPvrstTopologyChgTrap,'fsMIPvrstProtocolMigrationTrap':fsMIPvrstProtocolMigrationTrap,'fsMIPvrstInvalidBpduRxdTrap':fsMIPvrstInvalidBpduRxdTrap,'fsMIPvrstNewPortRoleTrap':fsMIPvrstNewPortRoleTrap,'fsMIPvrstHwFailureTrap':fsMIPvrstHwFailureTrap})