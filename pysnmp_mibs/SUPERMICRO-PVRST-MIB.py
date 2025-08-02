_q='fsPvrstInstPortState'
_p='fsPvrstOldRoleType'
_o='fsPvrstPortRoleType'
_n='fsPvrstPktErrVal'
_m='fsPvrstPktErrType'
_l='fsPvrstPortMigrationType'
_k='fsPvrstInstTopChanges'
_j='fsPvrstInstDesignatedRoot'
_i='fsPvrstErrTrapType'
_h='fsPvrstInstInstanceDownCount'
_g='fsPvrstInstInstanceUpCount'
_f='fsPvrstGenTrapType'
_e='designatedPort'
_d='rootPort'
_c='backupPort'
_b='alternatePort'
_a='disabledPort'
_Z='designated'
_Y='backup'
_X='alternate'
_W='sendstp'
_V='sendrstp'
_U='forwarding'
_T='learning'
_S='discarding'
_R='fsPvrstInstPortIndex'
_Q='fsPvrstPort'
_P='OctetString'
_O='fsPvrstPortTrapIndex'
_N='init'
_M='disable'
_L='enable'
_K='none'
_J='TruthValue'
_I='fsPvrstInstVlanId'
_H='not-accessible'
_G='disabled'
_F='fsPvrstBrgAddress'
_E='read-write'
_D='SUPERMICRO-PVRST-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_P,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_J)
futurePvrstMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,1,161))
if mibBuilder.loadTexts:futurePvrstMIB.setRevisions(('2012-09-05 00:00',))
class BridgeId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class Timeout(TextualConvention,Integer32):status=_A;displayHint='d4'
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_G,2)))
_FsFuturePvrst_ObjectIdentity=ObjectIdentity
fsFuturePvrst=_FsFuturePvrst_ObjectIdentity((1,3,6,1,4,1,10876,101,1,161,1))
class _FsPvrstSystemControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsPvrstSystemControl_Type.__name__=_C
_FsPvrstSystemControl_Object=MibScalar
fsPvrstSystemControl=_FsPvrstSystemControl_Object((1,3,6,1,4,1,10876,101,1,161,1,1),_FsPvrstSystemControl_Type())
fsPvrstSystemControl.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPvrstSystemControl.setStatus(_A)
_FsPvrstModuleStatus_Type=EnabledStatus
_FsPvrstModuleStatus_Object=MibScalar
fsPvrstModuleStatus=_FsPvrstModuleStatus_Object((1,3,6,1,4,1,10876,101,1,161,1,2),_FsPvrstModuleStatus_Type())
fsPvrstModuleStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPvrstModuleStatus.setStatus(_A)
_FsPvrstNoOfActiveInstances_Type=Integer32
_FsPvrstNoOfActiveInstances_Object=MibScalar
fsPvrstNoOfActiveInstances=_FsPvrstNoOfActiveInstances_Object((1,3,6,1,4,1,10876,101,1,161,1,3),_FsPvrstNoOfActiveInstances_Type())
fsPvrstNoOfActiveInstances.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstNoOfActiveInstances.setStatus(_A)
_FsPvrstBrgAddress_Type=MacAddress
_FsPvrstBrgAddress_Object=MibScalar
fsPvrstBrgAddress=_FsPvrstBrgAddress_Object((1,3,6,1,4,1,10876,101,1,161,1,4),_FsPvrstBrgAddress_Type())
fsPvrstBrgAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstBrgAddress.setStatus(_A)
_FsPvrstUpCount_Type=Counter32
_FsPvrstUpCount_Object=MibScalar
fsPvrstUpCount=_FsPvrstUpCount_Object((1,3,6,1,4,1,10876,101,1,161,1,5),_FsPvrstUpCount_Type())
fsPvrstUpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstUpCount.setStatus(_A)
_FsPvrstDownCount_Type=Counter32
_FsPvrstDownCount_Object=MibScalar
fsPvrstDownCount=_FsPvrstDownCount_Object((1,3,6,1,4,1,10876,101,1,161,1,6),_FsPvrstDownCount_Type())
fsPvrstDownCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstDownCount.setStatus(_A)
class _FsPvrstPathCostDefaultType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stp8021d1998',1),('stp8021t2001',2)))
_FsPvrstPathCostDefaultType_Type.__name__=_C
_FsPvrstPathCostDefaultType_Object=MibScalar
fsPvrstPathCostDefaultType=_FsPvrstPathCostDefaultType_Object((1,3,6,1,4,1,10876,101,1,161,1,7),_FsPvrstPathCostDefaultType_Type())
fsPvrstPathCostDefaultType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPvrstPathCostDefaultType.setStatus('obsolete')
class _FsPvrstDynamicPathCostCalculation_Type(TruthValue):defaultValue=2
_FsPvrstDynamicPathCostCalculation_Type.__name__=_J
_FsPvrstDynamicPathCostCalculation_Object=MibScalar
fsPvrstDynamicPathCostCalculation=_FsPvrstDynamicPathCostCalculation_Object((1,3,6,1,4,1,10876,101,1,161,1,8),_FsPvrstDynamicPathCostCalculation_Type())
fsPvrstDynamicPathCostCalculation.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPvrstDynamicPathCostCalculation.setStatus(_A)
class _FsPvrstTrace_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsPvrstTrace_Type.__name__=_C
_FsPvrstTrace_Object=MibScalar
fsPvrstTrace=_FsPvrstTrace_Object((1,3,6,1,4,1,10876,101,1,161,1,9),_FsPvrstTrace_Type())
fsPvrstTrace.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPvrstTrace.setStatus(_A)
class _FsPvrstDebug_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,524287))
_FsPvrstDebug_Type.__name__=_C
_FsPvrstDebug_Object=MibScalar
fsPvrstDebug=_FsPvrstDebug_Object((1,3,6,1,4,1,10876,101,1,161,1,10),_FsPvrstDebug_Type())
fsPvrstDebug.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPvrstDebug.setStatus(_A)
_FsPvrstBufferOverFlowCount_Type=Counter32
_FsPvrstBufferOverFlowCount_Object=MibScalar
fsPvrstBufferOverFlowCount=_FsPvrstBufferOverFlowCount_Object((1,3,6,1,4,1,10876,101,1,161,1,11),_FsPvrstBufferOverFlowCount_Type())
fsPvrstBufferOverFlowCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstBufferOverFlowCount.setStatus(_A)
_FsPvrstMemAllocFailureCount_Type=Counter32
_FsPvrstMemAllocFailureCount_Object=MibScalar
fsPvrstMemAllocFailureCount=_FsPvrstMemAllocFailureCount_Object((1,3,6,1,4,1,10876,101,1,161,1,12),_FsPvrstMemAllocFailureCount_Type())
fsPvrstMemAllocFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstMemAllocFailureCount.setStatus(_A)
_FsFuturePvrstPortTable_Object=MibTable
fsFuturePvrstPortTable=_FsFuturePvrstPortTable_Object((1,3,6,1,4,1,10876,101,1,161,1,13))
if mibBuilder.loadTexts:fsFuturePvrstPortTable.setStatus(_A)
_FsFuturePvrstPortEntry_Object=MibTableRow
fsFuturePvrstPortEntry=_FsFuturePvrstPortEntry_Object((1,3,6,1,4,1,10876,101,1,161,1,13,1))
fsFuturePvrstPortEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:fsFuturePvrstPortEntry.setStatus(_A)
class _FsPvrstPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsPvrstPort_Type.__name__=_C
_FsPvrstPort_Object=MibTableColumn
fsPvrstPort=_FsPvrstPort_Object((1,3,6,1,4,1,10876,101,1,161,1,13,1,1),_FsPvrstPort_Type())
fsPvrstPort.setMaxAccess(_H)
if mibBuilder.loadTexts:fsPvrstPort.setStatus(_A)
_FsPvrstPortAdminEdgeStatus_Type=TruthValue
_FsPvrstPortAdminEdgeStatus_Object=MibTableColumn
fsPvrstPortAdminEdgeStatus=_FsPvrstPortAdminEdgeStatus_Object((1,3,6,1,4,1,10876,101,1,161,1,13,1,2),_FsPvrstPortAdminEdgeStatus_Type())
fsPvrstPortAdminEdgeStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPvrstPortAdminEdgeStatus.setStatus(_A)
_FsPvrstPortOperEdgePortStatus_Type=TruthValue
_FsPvrstPortOperEdgePortStatus_Object=MibTableColumn
fsPvrstPortOperEdgePortStatus=_FsPvrstPortOperEdgePortStatus_Object((1,3,6,1,4,1,10876,101,1,161,1,13,1,3),_FsPvrstPortOperEdgePortStatus_Type())
fsPvrstPortOperEdgePortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstPortOperEdgePortStatus.setStatus(_A)
class _FsPvrstBridgeDetectionSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('edge',0),('notedge',1)))
_FsPvrstBridgeDetectionSemState_Type.__name__=_C
_FsPvrstBridgeDetectionSemState_Object=MibTableColumn
fsPvrstBridgeDetectionSemState=_FsPvrstBridgeDetectionSemState_Object((1,3,6,1,4,1,10876,101,1,161,1,13,1,4),_FsPvrstBridgeDetectionSemState_Type())
fsPvrstBridgeDetectionSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstBridgeDetectionSemState.setStatus(_A)
_FsPvrstPortEnabledStatus_Type=TruthValue
_FsPvrstPortEnabledStatus_Object=MibTableColumn
fsPvrstPortEnabledStatus=_FsPvrstPortEnabledStatus_Object((1,3,6,1,4,1,10876,101,1,161,1,13,1,5),_FsPvrstPortEnabledStatus_Type())
fsPvrstPortEnabledStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPvrstPortEnabledStatus.setStatus(_A)
_FsPvrstRootGuard_Type=TruthValue
_FsPvrstRootGuard_Object=MibTableColumn
fsPvrstRootGuard=_FsPvrstRootGuard_Object((1,3,6,1,4,1,10876,101,1,161,1,13,1,6),_FsPvrstRootGuard_Type())
fsPvrstRootGuard.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPvrstRootGuard.setStatus(_A)
class _FsPvrstBpduGuard_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),(_L,1),(_M,2)))
_FsPvrstBpduGuard_Type.__name__=_C
_FsPvrstBpduGuard_Object=MibTableColumn
fsPvrstBpduGuard=_FsPvrstBpduGuard_Object((1,3,6,1,4,1,10876,101,1,161,1,13,1,7),_FsPvrstBpduGuard_Type())
fsPvrstBpduGuard.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPvrstBpduGuard.setStatus(_A)
class _FsPvrstEncapType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('dot1Q',0),('isl',1)))
_FsPvrstEncapType_Type.__name__=_C
_FsPvrstEncapType_Object=MibTableColumn
fsPvrstEncapType=_FsPvrstEncapType_Object((1,3,6,1,4,1,10876,101,1,161,1,13,1,8),_FsPvrstEncapType_Type())
fsPvrstEncapType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPvrstEncapType.setStatus(_A)
class _FsPvrstPortAdminPointToPoint_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('forceTrue',0),('forceFalse',1),('auto',2)))
_FsPvrstPortAdminPointToPoint_Type.__name__=_C
_FsPvrstPortAdminPointToPoint_Object=MibTableColumn
fsPvrstPortAdminPointToPoint=_FsPvrstPortAdminPointToPoint_Object((1,3,6,1,4,1,10876,101,1,161,1,13,1,9),_FsPvrstPortAdminPointToPoint_Type())
fsPvrstPortAdminPointToPoint.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPvrstPortAdminPointToPoint.setStatus(_A)
_FsPvrstPortOperPointToPoint_Type=TruthValue
_FsPvrstPortOperPointToPoint_Object=MibTableColumn
fsPvrstPortOperPointToPoint=_FsPvrstPortOperPointToPoint_Object((1,3,6,1,4,1,10876,101,1,161,1,13,1,10),_FsPvrstPortOperPointToPoint_Type())
fsPvrstPortOperPointToPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstPortOperPointToPoint.setStatus(_A)
_FsPvrstPortInvalidBpdusRcvd_Type=Counter32
_FsPvrstPortInvalidBpdusRcvd_Object=MibTableColumn
fsPvrstPortInvalidBpdusRcvd=_FsPvrstPortInvalidBpdusRcvd_Object((1,3,6,1,4,1,10876,101,1,161,1,13,1,11),_FsPvrstPortInvalidBpdusRcvd_Type())
fsPvrstPortInvalidBpdusRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstPortInvalidBpdusRcvd.setStatus(_A)
_FsPvrstPortInvalidConfigBpduRxCount_Type=Counter32
_FsPvrstPortInvalidConfigBpduRxCount_Object=MibTableColumn
fsPvrstPortInvalidConfigBpduRxCount=_FsPvrstPortInvalidConfigBpduRxCount_Object((1,3,6,1,4,1,10876,101,1,161,1,13,1,12),_FsPvrstPortInvalidConfigBpduRxCount_Type())
fsPvrstPortInvalidConfigBpduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstPortInvalidConfigBpduRxCount.setStatus(_A)
_FsPvrstPortInvalidTcnBpduRxCount_Type=Counter32
_FsPvrstPortInvalidTcnBpduRxCount_Object=MibTableColumn
fsPvrstPortInvalidTcnBpduRxCount=_FsPvrstPortInvalidTcnBpduRxCount_Object((1,3,6,1,4,1,10876,101,1,161,1,13,1,13),_FsPvrstPortInvalidTcnBpduRxCount_Type())
fsPvrstPortInvalidTcnBpduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstPortInvalidTcnBpduRxCount.setStatus(_A)
_FsPvrstPortRowStatus_Type=RowStatus
_FsPvrstPortRowStatus_Object=MibTableColumn
fsPvrstPortRowStatus=_FsPvrstPortRowStatus_Object((1,3,6,1,4,1,10876,101,1,161,1,13,1,14),_FsPvrstPortRowStatus_Type())
fsPvrstPortRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:fsPvrstPortRowStatus.setStatus(_A)
_FsPvrstInstBridgeTable_Object=MibTable
fsPvrstInstBridgeTable=_FsPvrstInstBridgeTable_Object((1,3,6,1,4,1,10876,101,1,161,1,14))
if mibBuilder.loadTexts:fsPvrstInstBridgeTable.setStatus(_A)
_FsPvrstInstBridgeEntry_Object=MibTableRow
fsPvrstInstBridgeEntry=_FsPvrstInstBridgeEntry_Object((1,3,6,1,4,1,10876,101,1,161,1,14,1))
fsPvrstInstBridgeEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:fsPvrstInstBridgeEntry.setStatus(_A)
class _FsPvrstInstVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsPvrstInstVlanId_Type.__name__=_C
_FsPvrstInstVlanId_Object=MibTableColumn
fsPvrstInstVlanId=_FsPvrstInstVlanId_Object((1,3,6,1,4,1,10876,101,1,161,1,14,1,1),_FsPvrstInstVlanId_Type())
fsPvrstInstVlanId.setMaxAccess(_H)
if mibBuilder.loadTexts:fsPvrstInstVlanId.setStatus(_A)
class _FsPvrstInstBridgePriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_FsPvrstInstBridgePriority_Type.__name__=_C
_FsPvrstInstBridgePriority_Object=MibTableColumn
fsPvrstInstBridgePriority=_FsPvrstInstBridgePriority_Object((1,3,6,1,4,1,10876,101,1,161,1,14,1,2),_FsPvrstInstBridgePriority_Type())
fsPvrstInstBridgePriority.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPvrstInstBridgePriority.setStatus(_A)
_FsPvrstInstRootCost_Type=Integer32
_FsPvrstInstRootCost_Object=MibTableColumn
fsPvrstInstRootCost=_FsPvrstInstRootCost_Object((1,3,6,1,4,1,10876,101,1,161,1,14,1,3),_FsPvrstInstRootCost_Type())
fsPvrstInstRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstRootCost.setStatus(_A)
_FsPvrstInstRootPort_Type=Integer32
_FsPvrstInstRootPort_Object=MibTableColumn
fsPvrstInstRootPort=_FsPvrstInstRootPort_Object((1,3,6,1,4,1,10876,101,1,161,1,14,1,4),_FsPvrstInstRootPort_Type())
fsPvrstInstRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstRootPort.setStatus(_A)
_FsPvrstInstBridgeMaxAge_Type=Timeout
_FsPvrstInstBridgeMaxAge_Object=MibTableColumn
fsPvrstInstBridgeMaxAge=_FsPvrstInstBridgeMaxAge_Object((1,3,6,1,4,1,10876,101,1,161,1,14,1,5),_FsPvrstInstBridgeMaxAge_Type())
fsPvrstInstBridgeMaxAge.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPvrstInstBridgeMaxAge.setStatus(_A)
_FsPvrstInstBridgeHelloTime_Type=Timeout
_FsPvrstInstBridgeHelloTime_Object=MibTableColumn
fsPvrstInstBridgeHelloTime=_FsPvrstInstBridgeHelloTime_Object((1,3,6,1,4,1,10876,101,1,161,1,14,1,6),_FsPvrstInstBridgeHelloTime_Type())
fsPvrstInstBridgeHelloTime.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPvrstInstBridgeHelloTime.setStatus(_A)
_FsPvrstInstBridgeForwardDelay_Type=Timeout
_FsPvrstInstBridgeForwardDelay_Object=MibTableColumn
fsPvrstInstBridgeForwardDelay=_FsPvrstInstBridgeForwardDelay_Object((1,3,6,1,4,1,10876,101,1,161,1,14,1,7),_FsPvrstInstBridgeForwardDelay_Type())
fsPvrstInstBridgeForwardDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPvrstInstBridgeForwardDelay.setStatus(_A)
_FsPvrstInstHoldTime_Type=Integer32
_FsPvrstInstHoldTime_Object=MibTableColumn
fsPvrstInstHoldTime=_FsPvrstInstHoldTime_Object((1,3,6,1,4,1,10876,101,1,161,1,14,1,8),_FsPvrstInstHoldTime_Type())
fsPvrstInstHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstHoldTime.setStatus(_A)
class _FsPvrstInstTxHoldCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FsPvrstInstTxHoldCount_Type.__name__=_C
_FsPvrstInstTxHoldCount_Object=MibTableColumn
fsPvrstInstTxHoldCount=_FsPvrstInstTxHoldCount_Object((1,3,6,1,4,1,10876,101,1,161,1,14,1,9),_FsPvrstInstTxHoldCount_Type())
fsPvrstInstTxHoldCount.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPvrstInstTxHoldCount.setStatus(_A)
_FsPvrstInstTimeSinceTopologyChange_Type=TimeTicks
_FsPvrstInstTimeSinceTopologyChange_Object=MibTableColumn
fsPvrstInstTimeSinceTopologyChange=_FsPvrstInstTimeSinceTopologyChange_Object((1,3,6,1,4,1,10876,101,1,161,1,14,1,10),_FsPvrstInstTimeSinceTopologyChange_Type())
fsPvrstInstTimeSinceTopologyChange.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstTimeSinceTopologyChange.setStatus(_A)
_FsPvrstInstTopChanges_Type=Counter32
_FsPvrstInstTopChanges_Object=MibTableColumn
fsPvrstInstTopChanges=_FsPvrstInstTopChanges_Object((1,3,6,1,4,1,10876,101,1,161,1,14,1,11),_FsPvrstInstTopChanges_Type())
fsPvrstInstTopChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstTopChanges.setStatus(_A)
_FsPvrstInstNewRootCount_Type=Counter32
_FsPvrstInstNewRootCount_Object=MibTableColumn
fsPvrstInstNewRootCount=_FsPvrstInstNewRootCount_Object((1,3,6,1,4,1,10876,101,1,161,1,14,1,12),_FsPvrstInstNewRootCount_Type())
fsPvrstInstNewRootCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstNewRootCount.setStatus(_A)
_FsPvrstInstInstanceUpCount_Type=Counter32
_FsPvrstInstInstanceUpCount_Object=MibTableColumn
fsPvrstInstInstanceUpCount=_FsPvrstInstInstanceUpCount_Object((1,3,6,1,4,1,10876,101,1,161,1,14,1,13),_FsPvrstInstInstanceUpCount_Type())
fsPvrstInstInstanceUpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstInstanceUpCount.setStatus(_A)
_FsPvrstInstInstanceDownCount_Type=Counter32
_FsPvrstInstInstanceDownCount_Object=MibTableColumn
fsPvrstInstInstanceDownCount=_FsPvrstInstInstanceDownCount_Object((1,3,6,1,4,1,10876,101,1,161,1,14,1,14),_FsPvrstInstInstanceDownCount_Type())
fsPvrstInstInstanceDownCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstInstanceDownCount.setStatus(_A)
class _FsPvrstInstPortRoleSelSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('initbridge',0),('roleselection',1)))
_FsPvrstInstPortRoleSelSemState_Type.__name__=_C
_FsPvrstInstPortRoleSelSemState_Object=MibTableColumn
fsPvrstInstPortRoleSelSemState=_FsPvrstInstPortRoleSelSemState_Object((1,3,6,1,4,1,10876,101,1,161,1,14,1,15),_FsPvrstInstPortRoleSelSemState_Type())
fsPvrstInstPortRoleSelSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortRoleSelSemState.setStatus(_A)
_FsPvrstInstDesignatedRoot_Type=BridgeId
_FsPvrstInstDesignatedRoot_Object=MibTableColumn
fsPvrstInstDesignatedRoot=_FsPvrstInstDesignatedRoot_Object((1,3,6,1,4,1,10876,101,1,161,1,14,1,16),_FsPvrstInstDesignatedRoot_Type())
fsPvrstInstDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstDesignatedRoot.setStatus(_A)
_FsPvrstInstRootMaxAge_Type=Timeout
_FsPvrstInstRootMaxAge_Object=MibTableColumn
fsPvrstInstRootMaxAge=_FsPvrstInstRootMaxAge_Object((1,3,6,1,4,1,10876,101,1,161,1,14,1,17),_FsPvrstInstRootMaxAge_Type())
fsPvrstInstRootMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstRootMaxAge.setStatus(_A)
_FsPvrstInstRootHelloTime_Type=Timeout
_FsPvrstInstRootHelloTime_Object=MibTableColumn
fsPvrstInstRootHelloTime=_FsPvrstInstRootHelloTime_Object((1,3,6,1,4,1,10876,101,1,161,1,14,1,18),_FsPvrstInstRootHelloTime_Type())
fsPvrstInstRootHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstRootHelloTime.setStatus(_A)
_FsPvrstInstRootForwardDelay_Type=Timeout
_FsPvrstInstRootForwardDelay_Object=MibTableColumn
fsPvrstInstRootForwardDelay=_FsPvrstInstRootForwardDelay_Object((1,3,6,1,4,1,10876,101,1,161,1,14,1,19),_FsPvrstInstRootForwardDelay_Type())
fsPvrstInstRootForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstRootForwardDelay.setStatus(_A)
_FsPvrstInstPortTable_Object=MibTable
fsPvrstInstPortTable=_FsPvrstInstPortTable_Object((1,3,6,1,4,1,10876,101,1,161,1,15))
if mibBuilder.loadTexts:fsPvrstInstPortTable.setStatus(_A)
_FsPvrstInstPortEntry_Object=MibTableRow
fsPvrstInstPortEntry=_FsPvrstInstPortEntry_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1))
fsPvrstInstPortEntry.setIndexNames((0,_D,_I),(0,_D,_R))
if mibBuilder.loadTexts:fsPvrstInstPortEntry.setStatus(_A)
class _FsPvrstInstPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsPvrstInstPortIndex_Type.__name__=_C
_FsPvrstInstPortIndex_Object=MibTableColumn
fsPvrstInstPortIndex=_FsPvrstInstPortIndex_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,1),_FsPvrstInstPortIndex_Type())
fsPvrstInstPortIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:fsPvrstInstPortIndex.setStatus(_A)
class _FsPvrstInstPortEnableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_FsPvrstInstPortEnableStatus_Type.__name__=_C
_FsPvrstInstPortEnableStatus_Object=MibTableColumn
fsPvrstInstPortEnableStatus=_FsPvrstInstPortEnableStatus_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,2),_FsPvrstInstPortEnableStatus_Type())
fsPvrstInstPortEnableStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPvrstInstPortEnableStatus.setStatus(_A)
class _FsPvrstInstPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_FsPvrstInstPortPathCost_Type.__name__=_C
_FsPvrstInstPortPathCost_Object=MibTableColumn
fsPvrstInstPortPathCost=_FsPvrstInstPortPathCost_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,3),_FsPvrstInstPortPathCost_Type())
fsPvrstInstPortPathCost.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPvrstInstPortPathCost.setStatus(_A)
class _FsPvrstInstPortPriority_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_FsPvrstInstPortPriority_Type.__name__=_C
_FsPvrstInstPortPriority_Object=MibTableColumn
fsPvrstInstPortPriority=_FsPvrstInstPortPriority_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,4),_FsPvrstInstPortPriority_Type())
fsPvrstInstPortPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPvrstInstPortPriority.setStatus(_A)
_FsPvrstInstPortDesignatedRoot_Type=BridgeId
_FsPvrstInstPortDesignatedRoot_Object=MibTableColumn
fsPvrstInstPortDesignatedRoot=_FsPvrstInstPortDesignatedRoot_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,5),_FsPvrstInstPortDesignatedRoot_Type())
fsPvrstInstPortDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortDesignatedRoot.setStatus(_A)
_FsPvrstInstPortDesignatedBridge_Type=BridgeId
_FsPvrstInstPortDesignatedBridge_Object=MibTableColumn
fsPvrstInstPortDesignatedBridge=_FsPvrstInstPortDesignatedBridge_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,6),_FsPvrstInstPortDesignatedBridge_Type())
fsPvrstInstPortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortDesignatedBridge.setStatus(_A)
class _FsPvrstInstPortDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_FsPvrstInstPortDesignatedPort_Type.__name__=_P
_FsPvrstInstPortDesignatedPort_Object=MibTableColumn
fsPvrstInstPortDesignatedPort=_FsPvrstInstPortDesignatedPort_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,7),_FsPvrstInstPortDesignatedPort_Type())
fsPvrstInstPortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortDesignatedPort.setStatus(_A)
class _FsPvrstInstPortOperVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*(('stpCompatible',0),('rstp',2)))
_FsPvrstInstPortOperVersion_Type.__name__=_C
_FsPvrstInstPortOperVersion_Object=MibTableColumn
fsPvrstInstPortOperVersion=_FsPvrstInstPortOperVersion_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,8),_FsPvrstInstPortOperVersion_Type())
fsPvrstInstPortOperVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortOperVersion.setStatus(_A)
_FsPvrstInstPortProtocolMigration_Type=TruthValue
_FsPvrstInstPortProtocolMigration_Object=MibTableColumn
fsPvrstInstPortProtocolMigration=_FsPvrstInstPortProtocolMigration_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,9),_FsPvrstInstPortProtocolMigration_Type())
fsPvrstInstPortProtocolMigration.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortProtocolMigration.setStatus(_A)
class _FsPvrstInstPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5)));namedValues=NamedValues(*((_G,1),(_S,2),(_T,4),(_U,5)))
_FsPvrstInstPortState_Type.__name__=_C
_FsPvrstInstPortState_Object=MibTableColumn
fsPvrstInstPortState=_FsPvrstInstPortState_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,10),_FsPvrstInstPortState_Type())
fsPvrstInstPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortState.setStatus(_A)
_FsPvrstInstPortForwardTransitions_Type=Counter32
_FsPvrstInstPortForwardTransitions_Object=MibTableColumn
fsPvrstInstPortForwardTransitions=_FsPvrstInstPortForwardTransitions_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,11),_FsPvrstInstPortForwardTransitions_Type())
fsPvrstInstPortForwardTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortForwardTransitions.setStatus(_A)
_FsPvrstInstPortReceivedBpdus_Type=Counter32
_FsPvrstInstPortReceivedBpdus_Object=MibTableColumn
fsPvrstInstPortReceivedBpdus=_FsPvrstInstPortReceivedBpdus_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,12),_FsPvrstInstPortReceivedBpdus_Type())
fsPvrstInstPortReceivedBpdus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortReceivedBpdus.setStatus(_A)
_FsPvrstInstPortRxConfigBpduCount_Type=Counter32
_FsPvrstInstPortRxConfigBpduCount_Object=MibTableColumn
fsPvrstInstPortRxConfigBpduCount=_FsPvrstInstPortRxConfigBpduCount_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,13),_FsPvrstInstPortRxConfigBpduCount_Type())
fsPvrstInstPortRxConfigBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortRxConfigBpduCount.setStatus(_A)
_FsPvrstInstPortRxTcnBpduCount_Type=Counter32
_FsPvrstInstPortRxTcnBpduCount_Object=MibTableColumn
fsPvrstInstPortRxTcnBpduCount=_FsPvrstInstPortRxTcnBpduCount_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,14),_FsPvrstInstPortRxTcnBpduCount_Type())
fsPvrstInstPortRxTcnBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortRxTcnBpduCount.setStatus(_A)
_FsPvrstInstPortTransmittedBpdus_Type=Counter32
_FsPvrstInstPortTransmittedBpdus_Object=MibTableColumn
fsPvrstInstPortTransmittedBpdus=_FsPvrstInstPortTransmittedBpdus_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,15),_FsPvrstInstPortTransmittedBpdus_Type())
fsPvrstInstPortTransmittedBpdus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortTransmittedBpdus.setStatus(_A)
_FsPvrstInstPortTxConfigBpduCount_Type=Counter32
_FsPvrstInstPortTxConfigBpduCount_Object=MibTableColumn
fsPvrstInstPortTxConfigBpduCount=_FsPvrstInstPortTxConfigBpduCount_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,16),_FsPvrstInstPortTxConfigBpduCount_Type())
fsPvrstInstPortTxConfigBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortTxConfigBpduCount.setStatus(_A)
_FsPvrstInstPortTxTcnBpduCount_Type=Counter32
_FsPvrstInstPortTxTcnBpduCount_Object=MibTableColumn
fsPvrstInstPortTxTcnBpduCount=_FsPvrstInstPortTxTcnBpduCount_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,17),_FsPvrstInstPortTxTcnBpduCount_Type())
fsPvrstInstPortTxTcnBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortTxTcnBpduCount.setStatus(_A)
class _FsPvrstInstPortTxSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('transmitinit',0),('transmitperiodic',1),('transmitconfig',2),('transmittcn',3),('transmitrstp',4),('idle',5)))
_FsPvrstInstPortTxSemState_Type.__name__=_C
_FsPvrstInstPortTxSemState_Object=MibTableColumn
fsPvrstInstPortTxSemState=_FsPvrstInstPortTxSemState_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,18),_FsPvrstInstPortTxSemState_Type())
fsPvrstInstPortTxSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortTxSemState.setStatus(_A)
class _FsPvrstInstPortProtMigrationSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_N,0),(_V,1),('sendingrstp',2),(_W,3),('sendingstp',4)))
_FsPvrstInstPortProtMigrationSemState_Type.__name__=_C
_FsPvrstInstPortProtMigrationSemState_Object=MibTableColumn
fsPvrstInstPortProtMigrationSemState=_FsPvrstInstPortProtMigrationSemState_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,19),_FsPvrstInstPortProtMigrationSemState_Type())
fsPvrstInstPortProtMigrationSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortProtMigrationSemState.setStatus(_A)
_FsPvrstInstProtocolMigrationCount_Type=Counter32
_FsPvrstInstProtocolMigrationCount_Object=MibTableColumn
fsPvrstInstProtocolMigrationCount=_FsPvrstInstProtocolMigrationCount_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,20),_FsPvrstInstProtocolMigrationCount_Type())
fsPvrstInstProtocolMigrationCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstProtocolMigrationCount.setStatus(_A)
class _FsPvrstInstPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_G,0),(_X,1),(_Y,2),('root',3),(_Z,4)))
_FsPvrstInstPortRole_Type.__name__=_C
_FsPvrstInstPortRole_Object=MibTableColumn
fsPvrstInstPortRole=_FsPvrstInstPortRole_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,21),_FsPvrstInstPortRole_Type())
fsPvrstInstPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortRole.setStatus(_A)
class _FsPvrstInstCurrentPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_G,0),(_X,1),(_Y,2),('root',3),(_Z,4)))
_FsPvrstInstCurrentPortRole_Type.__name__=_C
_FsPvrstInstCurrentPortRole_Object=MibTableColumn
fsPvrstInstCurrentPortRole=_FsPvrstInstCurrentPortRole_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,22),_FsPvrstInstCurrentPortRole_Type())
fsPvrstInstCurrentPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstCurrentPortRole.setStatus(_A)
class _FsPvrstInstPortInfoSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,0),('aged',1),('update',2),('superior',3),('repeat',4),('agreement',5),('present',6),('receive',7)))
_FsPvrstInstPortInfoSemState_Type.__name__=_C
_FsPvrstInstPortInfoSemState_Object=MibTableColumn
fsPvrstInstPortInfoSemState=_FsPvrstInstPortInfoSemState_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,23),_FsPvrstInstPortInfoSemState_Type())
fsPvrstInstPortInfoSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortInfoSemState.setStatus(_A)
class _FsPvrstInstPortRoleTransitionSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_N,0),('blockport',1),('blockedport',2),('rootport',3),('designatedport',4)))
_FsPvrstInstPortRoleTransitionSemState_Type.__name__=_C
_FsPvrstInstPortRoleTransitionSemState_Object=MibTableColumn
fsPvrstInstPortRoleTransitionSemState=_FsPvrstInstPortRoleTransitionSemState_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,24),_FsPvrstInstPortRoleTransitionSemState_Type())
fsPvrstInstPortRoleTransitionSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortRoleTransitionSemState.setStatus(_A)
class _FsPvrstInstPortStateTransitionSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_S,0),(_T,1),(_U,2)))
_FsPvrstInstPortStateTransitionSemState_Type.__name__=_C
_FsPvrstInstPortStateTransitionSemState_Object=MibTableColumn
fsPvrstInstPortStateTransitionSemState=_FsPvrstInstPortStateTransitionSemState_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,25),_FsPvrstInstPortStateTransitionSemState_Type())
fsPvrstInstPortStateTransitionSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortStateTransitionSemState.setStatus(_A)
class _FsPvrstInstPortTopologyChangeSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_N,0),('inactive',1),('active',2),('detected',3),('notifiedtcn',4),('notifiedtc',5),('propagating',6),('acknowledged',7)))
_FsPvrstInstPortTopologyChangeSemState_Type.__name__=_C
_FsPvrstInstPortTopologyChangeSemState_Object=MibTableColumn
fsPvrstInstPortTopologyChangeSemState=_FsPvrstInstPortTopologyChangeSemState_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,26),_FsPvrstInstPortTopologyChangeSemState_Type())
fsPvrstInstPortTopologyChangeSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortTopologyChangeSemState.setStatus(_A)
_FsPvrstInstPortEffectivePortState_Type=TruthValue
_FsPvrstInstPortEffectivePortState_Object=MibTableColumn
fsPvrstInstPortEffectivePortState=_FsPvrstInstPortEffectivePortState_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,27),_FsPvrstInstPortEffectivePortState_Type())
fsPvrstInstPortEffectivePortState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortEffectivePortState.setStatus(_A)
_FsPvrstInstPortHelloTime_Type=Timeout
_FsPvrstInstPortHelloTime_Object=MibTableColumn
fsPvrstInstPortHelloTime=_FsPvrstInstPortHelloTime_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,28),_FsPvrstInstPortHelloTime_Type())
fsPvrstInstPortHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortHelloTime.setStatus(_A)
_FsPvrstInstPortMaxAge_Type=Timeout
_FsPvrstInstPortMaxAge_Object=MibTableColumn
fsPvrstInstPortMaxAge=_FsPvrstInstPortMaxAge_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,29),_FsPvrstInstPortMaxAge_Type())
fsPvrstInstPortMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortMaxAge.setStatus(_A)
_FsPvrstInstPortForwardDelay_Type=Timeout
_FsPvrstInstPortForwardDelay_Object=MibTableColumn
fsPvrstInstPortForwardDelay=_FsPvrstInstPortForwardDelay_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,30),_FsPvrstInstPortForwardDelay_Type())
fsPvrstInstPortForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortForwardDelay.setStatus(_A)
_FsPvrstInstPortHoldTime_Type=Timeout
_FsPvrstInstPortHoldTime_Object=MibTableColumn
fsPvrstInstPortHoldTime=_FsPvrstInstPortHoldTime_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,31),_FsPvrstInstPortHoldTime_Type())
fsPvrstInstPortHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstInstPortHoldTime.setStatus(_A)
class _FsPvrstInstPortAdminPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_FsPvrstInstPortAdminPathCost_Type.__name__=_C
_FsPvrstInstPortAdminPathCost_Object=MibTableColumn
fsPvrstInstPortAdminPathCost=_FsPvrstInstPortAdminPathCost_Object((1,3,6,1,4,1,10876,101,1,161,1,15,1,32),_FsPvrstInstPortAdminPathCost_Type())
fsPvrstInstPortAdminPathCost.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPvrstInstPortAdminPathCost.setStatus(_A)
class _FsPvrstCalcPortPathCostOnSpeedChg_Type(TruthValue):defaultValue=2
_FsPvrstCalcPortPathCostOnSpeedChg_Type.__name__=_J
_FsPvrstCalcPortPathCostOnSpeedChg_Object=MibScalar
fsPvrstCalcPortPathCostOnSpeedChg=_FsPvrstCalcPortPathCostOnSpeedChg_Object((1,3,6,1,4,1,10876,101,1,161,1,16),_FsPvrstCalcPortPathCostOnSpeedChg_Type())
fsPvrstCalcPortPathCostOnSpeedChg.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPvrstCalcPortPathCostOnSpeedChg.setStatus(_A)
class _FsPvrstGlobalBpduGuard_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),(_M,2)))
_FsPvrstGlobalBpduGuard_Type.__name__=_C
_FsPvrstGlobalBpduGuard_Object=MibScalar
fsPvrstGlobalBpduGuard=_FsPvrstGlobalBpduGuard_Object((1,3,6,1,4,1,10876,101,1,161,1,17),_FsPvrstGlobalBpduGuard_Type())
fsPvrstGlobalBpduGuard.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPvrstGlobalBpduGuard.setStatus(_A)
_FsPvrstTrapsControl_ObjectIdentity=ObjectIdentity
fsPvrstTrapsControl=_FsPvrstTrapsControl_ObjectIdentity((1,3,6,1,4,1,10876,101,1,161,2))
class _FsPvrstSetTraps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_FsPvrstSetTraps_Type.__name__=_C
_FsPvrstSetTraps_Object=MibScalar
fsPvrstSetTraps=_FsPvrstSetTraps_Object((1,3,6,1,4,1,10876,101,1,161,2,1),_FsPvrstSetTraps_Type())
fsPvrstSetTraps.setMaxAccess(_E)
if mibBuilder.loadTexts:fsPvrstSetTraps.setStatus(_A)
class _FsPvrstGenTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),('up',1),('down',2)))
_FsPvrstGenTrapType_Type.__name__=_C
_FsPvrstGenTrapType_Object=MibScalar
fsPvrstGenTrapType=_FsPvrstGenTrapType_Object((1,3,6,1,4,1,10876,101,1,161,2,2),_FsPvrstGenTrapType_Type())
fsPvrstGenTrapType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstGenTrapType.setStatus(_A)
class _FsPvrstErrTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),('memfail',1),('bufffail',2)))
_FsPvrstErrTrapType_Type.__name__=_C
_FsPvrstErrTrapType_Object=MibScalar
fsPvrstErrTrapType=_FsPvrstErrTrapType_Object((1,3,6,1,4,1,10876,101,1,161,2,3),_FsPvrstErrTrapType_Type())
fsPvrstErrTrapType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstErrTrapType.setStatus(_A)
_FsPvrstPortTrapNotificationTable_Object=MibTable
fsPvrstPortTrapNotificationTable=_FsPvrstPortTrapNotificationTable_Object((1,3,6,1,4,1,10876,101,1,161,2,4))
if mibBuilder.loadTexts:fsPvrstPortTrapNotificationTable.setStatus(_A)
_FsPvrstPortTrapNotificationEntry_Object=MibTableRow
fsPvrstPortTrapNotificationEntry=_FsPvrstPortTrapNotificationEntry_Object((1,3,6,1,4,1,10876,101,1,161,2,4,1))
fsPvrstPortTrapNotificationEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:fsPvrstPortTrapNotificationEntry.setStatus(_A)
class _FsPvrstPortTrapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_FsPvrstPortTrapIndex_Type.__name__=_C
_FsPvrstPortTrapIndex_Object=MibTableColumn
fsPvrstPortTrapIndex=_FsPvrstPortTrapIndex_Object((1,3,6,1,4,1,10876,101,1,161,2,4,1,1),_FsPvrstPortTrapIndex_Type())
fsPvrstPortTrapIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:fsPvrstPortTrapIndex.setStatus(_A)
class _FsPvrstPortMigrationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_W,0),(_V,1)))
_FsPvrstPortMigrationType_Type.__name__=_C
_FsPvrstPortMigrationType_Object=MibTableColumn
fsPvrstPortMigrationType=_FsPvrstPortMigrationType_Object((1,3,6,1,4,1,10876,101,1,161,2,4,1,2),_FsPvrstPortMigrationType_Type())
fsPvrstPortMigrationType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstPortMigrationType.setStatus(_A)
class _FsPvrstPktErrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('protocolIdErr',0),('invalidBpdu',1),('configLengthErr',2),('tcnLengthErr',3),('rstpLengthErr',4),('maxAgeErr',5),('fwdDelayErr',6),('helloTimeErr',7),('pvrstLengthErr',8)))
_FsPvrstPktErrType_Type.__name__=_C
_FsPvrstPktErrType_Object=MibTableColumn
fsPvrstPktErrType=_FsPvrstPktErrType_Object((1,3,6,1,4,1,10876,101,1,161,2,4,1,3),_FsPvrstPktErrType_Type())
fsPvrstPktErrType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstPktErrType.setStatus(_A)
_FsPvrstPktErrVal_Type=Integer32
_FsPvrstPktErrVal_Object=MibTableColumn
fsPvrstPktErrVal=_FsPvrstPktErrVal_Object((1,3,6,1,4,1,10876,101,1,161,2,4,1,4),_FsPvrstPktErrVal_Type())
fsPvrstPktErrVal.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstPktErrVal.setStatus(_A)
_FsPvrstPortRoleTrapNotificationTable_Object=MibTable
fsPvrstPortRoleTrapNotificationTable=_FsPvrstPortRoleTrapNotificationTable_Object((1,3,6,1,4,1,10876,101,1,161,2,5))
if mibBuilder.loadTexts:fsPvrstPortRoleTrapNotificationTable.setStatus(_A)
_FsPvrstPortRoleTrapNotificationEntry_Object=MibTableRow
fsPvrstPortRoleTrapNotificationEntry=_FsPvrstPortRoleTrapNotificationEntry_Object((1,3,6,1,4,1,10876,101,1,161,2,5,1))
fsPvrstPortRoleTrapNotificationEntry.setIndexNames((0,_D,_O),(0,_D,_I))
if mibBuilder.loadTexts:fsPvrstPortRoleTrapNotificationEntry.setStatus(_A)
class _FsPvrstPortRoleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_a,0),(_b,1),(_c,2),(_d,3),(_e,4)))
_FsPvrstPortRoleType_Type.__name__=_C
_FsPvrstPortRoleType_Object=MibTableColumn
fsPvrstPortRoleType=_FsPvrstPortRoleType_Object((1,3,6,1,4,1,10876,101,1,161,2,5,1,1),_FsPvrstPortRoleType_Type())
fsPvrstPortRoleType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstPortRoleType.setStatus(_A)
class _FsPvrstOldRoleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_a,0),(_b,1),(_c,2),(_d,3),(_e,4)))
_FsPvrstOldRoleType_Type.__name__=_C
_FsPvrstOldRoleType_Object=MibTableColumn
fsPvrstOldRoleType=_FsPvrstOldRoleType_Object((1,3,6,1,4,1,10876,101,1,161,2,5,1,2),_FsPvrstOldRoleType_Type())
fsPvrstOldRoleType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsPvrstOldRoleType.setStatus(_A)
_FsFuturePvrstTraps_ObjectIdentity=ObjectIdentity
fsFuturePvrstTraps=_FsFuturePvrstTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,161,3))
_FsPvrstTraps_ObjectIdentity=ObjectIdentity
fsPvrstTraps=_FsPvrstTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,161,3,0))
fsPvrstGenTrap=NotificationType((1,3,6,1,4,1,10876,101,1,161,3,0,1))
fsPvrstGenTrap.setObjects(*((_D,_F),(_D,_f),(_D,_g),(_D,_h)))
if mibBuilder.loadTexts:fsPvrstGenTrap.setStatus(_A)
fsPvrstErrTrap=NotificationType((1,3,6,1,4,1,10876,101,1,161,3,0,2))
fsPvrstErrTrap.setObjects(*((_D,_F),(_D,_i)))
if mibBuilder.loadTexts:fsPvrstErrTrap.setStatus(_A)
fsPvrstNewRootTrap=NotificationType((1,3,6,1,4,1,10876,101,1,161,3,0,3))
fsPvrstNewRootTrap.setObjects(*((_D,_F),(_D,_j)))
if mibBuilder.loadTexts:fsPvrstNewRootTrap.setStatus(_A)
fsPvrstTopologyChgTrap=NotificationType((1,3,6,1,4,1,10876,101,1,161,3,0,4))
fsPvrstTopologyChgTrap.setObjects(*((_D,_F),(_D,_k)))
if mibBuilder.loadTexts:fsPvrstTopologyChgTrap.setStatus(_A)
fsPvrstProtocolMigrationTrap=NotificationType((1,3,6,1,4,1,10876,101,1,161,3,0,5))
fsPvrstProtocolMigrationTrap.setObjects(*((_D,_F),(_D,_l)))
if mibBuilder.loadTexts:fsPvrstProtocolMigrationTrap.setStatus(_A)
fsPvrstInvalidBpduRxdTrap=NotificationType((1,3,6,1,4,1,10876,101,1,161,3,0,6))
fsPvrstInvalidBpduRxdTrap.setObjects(*((_D,_F),(_D,_m),(_D,_n)))
if mibBuilder.loadTexts:fsPvrstInvalidBpduRxdTrap.setStatus(_A)
fsPvrstNewPortRoleTrap=NotificationType((1,3,6,1,4,1,10876,101,1,161,3,0,7))
fsPvrstNewPortRoleTrap.setObjects(*((_D,_F),(_D,_o),(_D,_p)))
if mibBuilder.loadTexts:fsPvrstNewPortRoleTrap.setStatus(_A)
fsPvrstHwFailureTrap=NotificationType((1,3,6,1,4,1,10876,101,1,161,3,0,8))
fsPvrstHwFailureTrap.setObjects(*((_D,_F),(_D,_q)))
if mibBuilder.loadTexts:fsPvrstHwFailureTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'BridgeId':BridgeId,'Timeout':Timeout,'EnabledStatus':EnabledStatus,'futurePvrstMIB':futurePvrstMIB,'fsFuturePvrst':fsFuturePvrst,'fsPvrstSystemControl':fsPvrstSystemControl,'fsPvrstModuleStatus':fsPvrstModuleStatus,'fsPvrstNoOfActiveInstances':fsPvrstNoOfActiveInstances,_F:fsPvrstBrgAddress,'fsPvrstUpCount':fsPvrstUpCount,'fsPvrstDownCount':fsPvrstDownCount,'fsPvrstPathCostDefaultType':fsPvrstPathCostDefaultType,'fsPvrstDynamicPathCostCalculation':fsPvrstDynamicPathCostCalculation,'fsPvrstTrace':fsPvrstTrace,'fsPvrstDebug':fsPvrstDebug,'fsPvrstBufferOverFlowCount':fsPvrstBufferOverFlowCount,'fsPvrstMemAllocFailureCount':fsPvrstMemAllocFailureCount,'fsFuturePvrstPortTable':fsFuturePvrstPortTable,'fsFuturePvrstPortEntry':fsFuturePvrstPortEntry,_Q:fsPvrstPort,'fsPvrstPortAdminEdgeStatus':fsPvrstPortAdminEdgeStatus,'fsPvrstPortOperEdgePortStatus':fsPvrstPortOperEdgePortStatus,'fsPvrstBridgeDetectionSemState':fsPvrstBridgeDetectionSemState,'fsPvrstPortEnabledStatus':fsPvrstPortEnabledStatus,'fsPvrstRootGuard':fsPvrstRootGuard,'fsPvrstBpduGuard':fsPvrstBpduGuard,'fsPvrstEncapType':fsPvrstEncapType,'fsPvrstPortAdminPointToPoint':fsPvrstPortAdminPointToPoint,'fsPvrstPortOperPointToPoint':fsPvrstPortOperPointToPoint,'fsPvrstPortInvalidBpdusRcvd':fsPvrstPortInvalidBpdusRcvd,'fsPvrstPortInvalidConfigBpduRxCount':fsPvrstPortInvalidConfigBpduRxCount,'fsPvrstPortInvalidTcnBpduRxCount':fsPvrstPortInvalidTcnBpduRxCount,'fsPvrstPortRowStatus':fsPvrstPortRowStatus,'fsPvrstInstBridgeTable':fsPvrstInstBridgeTable,'fsPvrstInstBridgeEntry':fsPvrstInstBridgeEntry,_I:fsPvrstInstVlanId,'fsPvrstInstBridgePriority':fsPvrstInstBridgePriority,'fsPvrstInstRootCost':fsPvrstInstRootCost,'fsPvrstInstRootPort':fsPvrstInstRootPort,'fsPvrstInstBridgeMaxAge':fsPvrstInstBridgeMaxAge,'fsPvrstInstBridgeHelloTime':fsPvrstInstBridgeHelloTime,'fsPvrstInstBridgeForwardDelay':fsPvrstInstBridgeForwardDelay,'fsPvrstInstHoldTime':fsPvrstInstHoldTime,'fsPvrstInstTxHoldCount':fsPvrstInstTxHoldCount,'fsPvrstInstTimeSinceTopologyChange':fsPvrstInstTimeSinceTopologyChange,_k:fsPvrstInstTopChanges,'fsPvrstInstNewRootCount':fsPvrstInstNewRootCount,_g:fsPvrstInstInstanceUpCount,_h:fsPvrstInstInstanceDownCount,'fsPvrstInstPortRoleSelSemState':fsPvrstInstPortRoleSelSemState,_j:fsPvrstInstDesignatedRoot,'fsPvrstInstRootMaxAge':fsPvrstInstRootMaxAge,'fsPvrstInstRootHelloTime':fsPvrstInstRootHelloTime,'fsPvrstInstRootForwardDelay':fsPvrstInstRootForwardDelay,'fsPvrstInstPortTable':fsPvrstInstPortTable,'fsPvrstInstPortEntry':fsPvrstInstPortEntry,_R:fsPvrstInstPortIndex,'fsPvrstInstPortEnableStatus':fsPvrstInstPortEnableStatus,'fsPvrstInstPortPathCost':fsPvrstInstPortPathCost,'fsPvrstInstPortPriority':fsPvrstInstPortPriority,'fsPvrstInstPortDesignatedRoot':fsPvrstInstPortDesignatedRoot,'fsPvrstInstPortDesignatedBridge':fsPvrstInstPortDesignatedBridge,'fsPvrstInstPortDesignatedPort':fsPvrstInstPortDesignatedPort,'fsPvrstInstPortOperVersion':fsPvrstInstPortOperVersion,'fsPvrstInstPortProtocolMigration':fsPvrstInstPortProtocolMigration,_q:fsPvrstInstPortState,'fsPvrstInstPortForwardTransitions':fsPvrstInstPortForwardTransitions,'fsPvrstInstPortReceivedBpdus':fsPvrstInstPortReceivedBpdus,'fsPvrstInstPortRxConfigBpduCount':fsPvrstInstPortRxConfigBpduCount,'fsPvrstInstPortRxTcnBpduCount':fsPvrstInstPortRxTcnBpduCount,'fsPvrstInstPortTransmittedBpdus':fsPvrstInstPortTransmittedBpdus,'fsPvrstInstPortTxConfigBpduCount':fsPvrstInstPortTxConfigBpduCount,'fsPvrstInstPortTxTcnBpduCount':fsPvrstInstPortTxTcnBpduCount,'fsPvrstInstPortTxSemState':fsPvrstInstPortTxSemState,'fsPvrstInstPortProtMigrationSemState':fsPvrstInstPortProtMigrationSemState,'fsPvrstInstProtocolMigrationCount':fsPvrstInstProtocolMigrationCount,'fsPvrstInstPortRole':fsPvrstInstPortRole,'fsPvrstInstCurrentPortRole':fsPvrstInstCurrentPortRole,'fsPvrstInstPortInfoSemState':fsPvrstInstPortInfoSemState,'fsPvrstInstPortRoleTransitionSemState':fsPvrstInstPortRoleTransitionSemState,'fsPvrstInstPortStateTransitionSemState':fsPvrstInstPortStateTransitionSemState,'fsPvrstInstPortTopologyChangeSemState':fsPvrstInstPortTopologyChangeSemState,'fsPvrstInstPortEffectivePortState':fsPvrstInstPortEffectivePortState,'fsPvrstInstPortHelloTime':fsPvrstInstPortHelloTime,'fsPvrstInstPortMaxAge':fsPvrstInstPortMaxAge,'fsPvrstInstPortForwardDelay':fsPvrstInstPortForwardDelay,'fsPvrstInstPortHoldTime':fsPvrstInstPortHoldTime,'fsPvrstInstPortAdminPathCost':fsPvrstInstPortAdminPathCost,'fsPvrstCalcPortPathCostOnSpeedChg':fsPvrstCalcPortPathCostOnSpeedChg,'fsPvrstGlobalBpduGuard':fsPvrstGlobalBpduGuard,'fsPvrstTrapsControl':fsPvrstTrapsControl,'fsPvrstSetTraps':fsPvrstSetTraps,_f:fsPvrstGenTrapType,_i:fsPvrstErrTrapType,'fsPvrstPortTrapNotificationTable':fsPvrstPortTrapNotificationTable,'fsPvrstPortTrapNotificationEntry':fsPvrstPortTrapNotificationEntry,_O:fsPvrstPortTrapIndex,_l:fsPvrstPortMigrationType,_m:fsPvrstPktErrType,_n:fsPvrstPktErrVal,'fsPvrstPortRoleTrapNotificationTable':fsPvrstPortRoleTrapNotificationTable,'fsPvrstPortRoleTrapNotificationEntry':fsPvrstPortRoleTrapNotificationEntry,_o:fsPvrstPortRoleType,_p:fsPvrstOldRoleType,'fsFuturePvrstTraps':fsFuturePvrstTraps,'fsPvrstTraps':fsPvrstTraps,'fsPvrstGenTrap':fsPvrstGenTrap,'fsPvrstErrTrap':fsPvrstErrTrap,'fsPvrstNewRootTrap':fsPvrstNewRootTrap,'fsPvrstTopologyChgTrap':fsPvrstTopologyChgTrap,'fsPvrstProtocolMigrationTrap':fsPvrstProtocolMigrationTrap,'fsPvrstInvalidBpduRxdTrap':fsPvrstInvalidBpduRxdTrap,'fsPvrstNewPortRoleTrap':fsPvrstNewPortRoleTrap,'fsPvrstHwFailureTrap':fsPvrstHwFailureTrap})