_AV='arubaWiredRpvstNotificationGroup'
_AU='arubaWiredRpvstNotificationObjectGrp'
_AT='arubaWiredRpvstPvst1'
_AS='arubaWiredRpvstPortGroup'
_AR='arubaWiredRpvstPortVlanGroup'
_AQ='arubaWiredRpvstVlanGroup'
_AP='arubaWiredRpvstGroup'
_AO='arubaWiredRpvstTopologyChange'
_AN='arubaWiredRpvstLoopGuardInconsistency'
_AM='arubaWiredRpvstRootGuardInconsistency'
_AL='arubaWiredRpvstNewRoot'
_AK='arubaWiredRpvstErrantBpduReceived'
_AJ='arubaWiredRpvstPortVlanInconsistencyReason'
_AI='arubaWiredRpvstVlanLogPortStateTransitions'
_AH='arubaWiredRpvstVlanSendTopoChangeCtrl'
_AG='arubaWiredRpvstPathCostMode'
_AF='arubaWiredRpvstPortBpduProtection'
_AE='arubaWiredRpvstPortLoopGuard'
_AD='arubaWiredRpvstPortRootGuard'
_AC='arubaWiredRpvstPortRestrictedTcn'
_AB='arubaWiredRpvstPortBpduFiltering'
_AA='arubaWiredRpvstPortAutoEdge'
_A9='arubaWiredRpvstPortAdminPointToPoint'
_A8='arubaWiredRpvstPortAdminEdge'
_A7='arubaWiredRpvstPortVlanOperEdge'
_A6='arubaWiredRpvstPortVlanOperPointToPoint'
_A5='arubaWiredRpvstPortVlanRole'
_A4='arubaWiredRpvstPortVlanResetCounters'
_A3='arubaWiredRpvstPortVlanPriority'
_A2='arubaWiredRpvstPortVlanPathCost'
_A1='arubaWiredRpvstVlanTopoChangeCount'
_A0='arubaWiredRpvstVlanTimeSinceLastTopoChange'
_z='arubaWiredRpvstVlanRootChangeCounter'
_y='arubaWiredRpvstVlanRootMacAddress'
_x='arubaWiredRpvstVlanRootPathCost'
_w='arubaWiredRpvstVlanRootPort'
_v='arubaWiredRpvstVlanRootPriority'
_u='arubaWiredRpvstVlanOperHelloTime'
_t='arubaWiredRpvstVlanResetCounters'
_s='arubaWiredRpvstVlanRpvstAdminStatus'
_r='arubaWiredRpvstVlanRoot'
_q='arubaWiredRpvstVlanPriority'
_p='arubaWiredRpvstVlanMaxAge'
_o='arubaWiredRpvstVlanForwardDelay'
_n='arubaWiredRpvstVlanHelloTime'
_m='arubaWiredRpvstCurrentVportCount'
_l='arubaWiredRpvstMstpInterconnectVlan'
_k='arubaWiredRpvstBpduGuardTimeout'
_j='arubaWiredRpvstIgnorePVIDInconsistency'
_i='arubaWiredRpvstExtendedSystemID'
_h='arubaWiredRpvstResetCounters'
_g='arubaWiredRpvstId'
_f='arubaWiredRpvstPortVlanIndex'
_e='arubaWiredRpvstPortVlanId'
_d='PointToPoint'
_c='arubaWiredRpvstPortIndex'
_b='arubaWiredRpvstVlanId'
_a='arubaWiredRpvstRootBridgeChangeTimeStamp'
_Z='arubaWiredRpvstNewRootBridgeID'
_Y='arubaWiredRpvstPreviousRootBridgeID'
_X='arubaWiredRpvstTopoChangeTime'
_W='arubaWiredRpvstNewPortRole'
_V='arubaWiredRpvstOldPortRole'
_U='arubaWiredRpvstDesignatedPort'
_T='arubaWiredRpvstErrantBpduDetector'
_S='arubaWiredRpvstSuperiorBpduSrcMac'
_R='arubaWiredRpvstSuperiorBpduSrcPort'
_Q='arubaWiredRpvstErrantBpduSrcMac'
_P='arubaWiredRpvstPortVlanErrantBpduRxCount'
_O='arubaWiredRpvstPortVlanState'
_N='disabled'
_M='arubaWiredRpvstPortVlanDesigBridge'
_L='seconds'
_K='not-accessible'
_J='arubaWiredRpvstPortName'
_I='arubaWiredRpvstVlanIndex'
_H='DisplayString'
_G='accessible-for-notify'
_F='read-only'
_E='TruthValue'
_D='Integer32'
_C='read-write'
_B='current'
_A='ARUBAWIRED-RPVST-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wndFeatures,=mibBuilder.importSymbols('ARUBAWIRED-NETWORKING-OID','wndFeatures')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_H,'MacAddress','PhysAddress','TextualConvention',_E)
arubaWiredRpvstMIB=ModuleIdentity((1,3,6,1,4,1,47196,4,1,1,3,5))
if mibBuilder.loadTexts:arubaWiredRpvstMIB.setRevisions(('2020-11-25 00:00','2020-10-22 00:00','2020-06-12 00:00','2018-05-29 00:00','2018-01-18 00:00'))
class PointToPoint(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('forceTrue',1),('forceFalse',2),('auto',3)))
_ArubaWiredRpvstNotifications_ObjectIdentity=ObjectIdentity
arubaWiredRpvstNotifications=_ArubaWiredRpvstNotifications_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,5,0))
_ArubaWiredRpvstObjects_ObjectIdentity=ObjectIdentity
arubaWiredRpvstObjects=_ArubaWiredRpvstObjects_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,5,1))
_ArubaWiredRpvstGeneralGroup_ObjectIdentity=ObjectIdentity
arubaWiredRpvstGeneralGroup=_ArubaWiredRpvstGeneralGroup_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,5,1,1))
class _ArubaWiredRpvstResetCounters_Type(TruthValue):defaultValue=2
_ArubaWiredRpvstResetCounters_Type.__name__=_E
_ArubaWiredRpvstResetCounters_Object=MibScalar
arubaWiredRpvstResetCounters=_ArubaWiredRpvstResetCounters_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,1,1),_ArubaWiredRpvstResetCounters_Type())
arubaWiredRpvstResetCounters.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstResetCounters.setStatus(_B)
class _ArubaWiredRpvstExtendedSystemID_Type(TruthValue):defaultValue=1
_ArubaWiredRpvstExtendedSystemID_Type.__name__=_E
_ArubaWiredRpvstExtendedSystemID_Object=MibScalar
arubaWiredRpvstExtendedSystemID=_ArubaWiredRpvstExtendedSystemID_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,1,2),_ArubaWiredRpvstExtendedSystemID_Type())
arubaWiredRpvstExtendedSystemID.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstExtendedSystemID.setStatus(_B)
class _ArubaWiredRpvstIgnorePVIDInconsistency_Type(TruthValue):defaultValue=2
_ArubaWiredRpvstIgnorePVIDInconsistency_Type.__name__=_E
_ArubaWiredRpvstIgnorePVIDInconsistency_Object=MibScalar
arubaWiredRpvstIgnorePVIDInconsistency=_ArubaWiredRpvstIgnorePVIDInconsistency_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,1,3),_ArubaWiredRpvstIgnorePVIDInconsistency_Type())
arubaWiredRpvstIgnorePVIDInconsistency.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstIgnorePVIDInconsistency.setStatus(_B)
class _ArubaWiredRpvstPathCostMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('pathCost8021d',1),('pathCost8021t',2),('proprietary',3)))
_ArubaWiredRpvstPathCostMode_Type.__name__=_D
_ArubaWiredRpvstPathCostMode_Object=MibScalar
arubaWiredRpvstPathCostMode=_ArubaWiredRpvstPathCostMode_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,1,4),_ArubaWiredRpvstPathCostMode_Type())
arubaWiredRpvstPathCostMode.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstPathCostMode.setStatus(_B)
_ArubaWiredRpvstBpduGuardTimeout_Type=Integer32
_ArubaWiredRpvstBpduGuardTimeout_Object=MibScalar
arubaWiredRpvstBpduGuardTimeout=_ArubaWiredRpvstBpduGuardTimeout_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,1,5),_ArubaWiredRpvstBpduGuardTimeout_Type())
arubaWiredRpvstBpduGuardTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstBpduGuardTimeout.setStatus(_B)
_ArubaWiredRpvstMstpInterconnectVlan_Type=Integer32
_ArubaWiredRpvstMstpInterconnectVlan_Object=MibScalar
arubaWiredRpvstMstpInterconnectVlan=_ArubaWiredRpvstMstpInterconnectVlan_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,1,6),_ArubaWiredRpvstMstpInterconnectVlan_Type())
arubaWiredRpvstMstpInterconnectVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstMstpInterconnectVlan.setStatus(_B)
_ArubaWiredRpvstCurrentVportCount_Type=Integer32
_ArubaWiredRpvstCurrentVportCount_Object=MibScalar
arubaWiredRpvstCurrentVportCount=_ArubaWiredRpvstCurrentVportCount_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,1,7),_ArubaWiredRpvstCurrentVportCount_Type())
arubaWiredRpvstCurrentVportCount.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstCurrentVportCount.setStatus(_B)
_ArubaWiredRpvstVlanTable_Object=MibTable
arubaWiredRpvstVlanTable=_ArubaWiredRpvstVlanTable_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,2))
if mibBuilder.loadTexts:arubaWiredRpvstVlanTable.setStatus(_B)
_ArubaWiredRpvstVlanEntry_Object=MibTableRow
arubaWiredRpvstVlanEntry=_ArubaWiredRpvstVlanEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,2,1))
arubaWiredRpvstVlanEntry.setIndexNames((0,_A,_b))
if mibBuilder.loadTexts:arubaWiredRpvstVlanEntry.setStatus(_B)
_ArubaWiredRpvstVlanId_Type=VlanIndex
_ArubaWiredRpvstVlanId_Object=MibTableColumn
arubaWiredRpvstVlanId=_ArubaWiredRpvstVlanId_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,2,1,1),_ArubaWiredRpvstVlanId_Type())
arubaWiredRpvstVlanId.setMaxAccess(_K)
if mibBuilder.loadTexts:arubaWiredRpvstVlanId.setStatus(_B)
class _ArubaWiredRpvstVlanHelloTime_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,10))
_ArubaWiredRpvstVlanHelloTime_Type.__name__=_D
_ArubaWiredRpvstVlanHelloTime_Object=MibTableColumn
arubaWiredRpvstVlanHelloTime=_ArubaWiredRpvstVlanHelloTime_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,2,1,2),_ArubaWiredRpvstVlanHelloTime_Type())
arubaWiredRpvstVlanHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstVlanHelloTime.setStatus(_B)
if mibBuilder.loadTexts:arubaWiredRpvstVlanHelloTime.setUnits(_L)
class _ArubaWiredRpvstVlanForwardDelay_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_ArubaWiredRpvstVlanForwardDelay_Type.__name__=_D
_ArubaWiredRpvstVlanForwardDelay_Object=MibTableColumn
arubaWiredRpvstVlanForwardDelay=_ArubaWiredRpvstVlanForwardDelay_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,2,1,3),_ArubaWiredRpvstVlanForwardDelay_Type())
arubaWiredRpvstVlanForwardDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstVlanForwardDelay.setStatus(_B)
if mibBuilder.loadTexts:arubaWiredRpvstVlanForwardDelay.setUnits(_L)
class _ArubaWiredRpvstVlanMaxAge_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_ArubaWiredRpvstVlanMaxAge_Type.__name__=_D
_ArubaWiredRpvstVlanMaxAge_Object=MibTableColumn
arubaWiredRpvstVlanMaxAge=_ArubaWiredRpvstVlanMaxAge_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,2,1,4),_ArubaWiredRpvstVlanMaxAge_Type())
arubaWiredRpvstVlanMaxAge.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstVlanMaxAge.setStatus(_B)
if mibBuilder.loadTexts:arubaWiredRpvstVlanMaxAge.setUnits(_L)
class _ArubaWiredRpvstVlanPriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ArubaWiredRpvstVlanPriority_Type.__name__=_D
_ArubaWiredRpvstVlanPriority_Object=MibTableColumn
arubaWiredRpvstVlanPriority=_ArubaWiredRpvstVlanPriority_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,2,1,5),_ArubaWiredRpvstVlanPriority_Type())
arubaWiredRpvstVlanPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstVlanPriority.setStatus(_B)
class _ArubaWiredRpvstVlanRoot_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('none',0),('primary',1),('secondary',2)))
_ArubaWiredRpvstVlanRoot_Type.__name__=_D
_ArubaWiredRpvstVlanRoot_Object=MibTableColumn
arubaWiredRpvstVlanRoot=_ArubaWiredRpvstVlanRoot_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,2,1,6),_ArubaWiredRpvstVlanRoot_Type())
arubaWiredRpvstVlanRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstVlanRoot.setStatus(_B)
class _ArubaWiredRpvstVlanRpvstAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_N,2)))
_ArubaWiredRpvstVlanRpvstAdminStatus_Type.__name__=_D
_ArubaWiredRpvstVlanRpvstAdminStatus_Object=MibTableColumn
arubaWiredRpvstVlanRpvstAdminStatus=_ArubaWiredRpvstVlanRpvstAdminStatus_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,2,1,7),_ArubaWiredRpvstVlanRpvstAdminStatus_Type())
arubaWiredRpvstVlanRpvstAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstVlanRpvstAdminStatus.setStatus(_B)
class _ArubaWiredRpvstVlanResetCounters_Type(TruthValue):defaultValue=2
_ArubaWiredRpvstVlanResetCounters_Type.__name__=_E
_ArubaWiredRpvstVlanResetCounters_Object=MibTableColumn
arubaWiredRpvstVlanResetCounters=_ArubaWiredRpvstVlanResetCounters_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,2,1,8),_ArubaWiredRpvstVlanResetCounters_Type())
arubaWiredRpvstVlanResetCounters.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstVlanResetCounters.setStatus(_B)
class _ArubaWiredRpvstVlanOperHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_ArubaWiredRpvstVlanOperHelloTime_Type.__name__=_D
_ArubaWiredRpvstVlanOperHelloTime_Object=MibTableColumn
arubaWiredRpvstVlanOperHelloTime=_ArubaWiredRpvstVlanOperHelloTime_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,2,1,9),_ArubaWiredRpvstVlanOperHelloTime_Type())
arubaWiredRpvstVlanOperHelloTime.setMaxAccess(_F)
if mibBuilder.loadTexts:arubaWiredRpvstVlanOperHelloTime.setStatus(_B)
if mibBuilder.loadTexts:arubaWiredRpvstVlanOperHelloTime.setUnits(_L)
class _ArubaWiredRpvstVlanRootPriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ArubaWiredRpvstVlanRootPriority_Type.__name__=_D
_ArubaWiredRpvstVlanRootPriority_Object=MibTableColumn
arubaWiredRpvstVlanRootPriority=_ArubaWiredRpvstVlanRootPriority_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,2,1,10),_ArubaWiredRpvstVlanRootPriority_Type())
arubaWiredRpvstVlanRootPriority.setMaxAccess(_F)
if mibBuilder.loadTexts:arubaWiredRpvstVlanRootPriority.setStatus(_B)
_ArubaWiredRpvstVlanRootPort_Type=InterfaceIndex
_ArubaWiredRpvstVlanRootPort_Object=MibTableColumn
arubaWiredRpvstVlanRootPort=_ArubaWiredRpvstVlanRootPort_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,2,1,11),_ArubaWiredRpvstVlanRootPort_Type())
arubaWiredRpvstVlanRootPort.setMaxAccess(_F)
if mibBuilder.loadTexts:arubaWiredRpvstVlanRootPort.setStatus(_B)
class _ArubaWiredRpvstVlanRootPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_ArubaWiredRpvstVlanRootPathCost_Type.__name__=_D
_ArubaWiredRpvstVlanRootPathCost_Object=MibTableColumn
arubaWiredRpvstVlanRootPathCost=_ArubaWiredRpvstVlanRootPathCost_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,2,1,12),_ArubaWiredRpvstVlanRootPathCost_Type())
arubaWiredRpvstVlanRootPathCost.setMaxAccess(_F)
if mibBuilder.loadTexts:arubaWiredRpvstVlanRootPathCost.setStatus(_B)
_ArubaWiredRpvstVlanRootMacAddress_Type=MacAddress
_ArubaWiredRpvstVlanRootMacAddress_Object=MibTableColumn
arubaWiredRpvstVlanRootMacAddress=_ArubaWiredRpvstVlanRootMacAddress_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,2,1,13),_ArubaWiredRpvstVlanRootMacAddress_Type())
arubaWiredRpvstVlanRootMacAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:arubaWiredRpvstVlanRootMacAddress.setStatus(_B)
_ArubaWiredRpvstVlanRootChangeCounter_Type=Counter32
_ArubaWiredRpvstVlanRootChangeCounter_Object=MibTableColumn
arubaWiredRpvstVlanRootChangeCounter=_ArubaWiredRpvstVlanRootChangeCounter_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,2,1,14),_ArubaWiredRpvstVlanRootChangeCounter_Type())
arubaWiredRpvstVlanRootChangeCounter.setMaxAccess(_F)
if mibBuilder.loadTexts:arubaWiredRpvstVlanRootChangeCounter.setStatus(_B)
_ArubaWiredRpvstVlanTimeSinceLastTopoChange_Type=TimeTicks
_ArubaWiredRpvstVlanTimeSinceLastTopoChange_Object=MibTableColumn
arubaWiredRpvstVlanTimeSinceLastTopoChange=_ArubaWiredRpvstVlanTimeSinceLastTopoChange_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,2,1,15),_ArubaWiredRpvstVlanTimeSinceLastTopoChange_Type())
arubaWiredRpvstVlanTimeSinceLastTopoChange.setMaxAccess(_F)
if mibBuilder.loadTexts:arubaWiredRpvstVlanTimeSinceLastTopoChange.setStatus(_B)
_ArubaWiredRpvstVlanTopoChangeCount_Type=Counter32
_ArubaWiredRpvstVlanTopoChangeCount_Object=MibTableColumn
arubaWiredRpvstVlanTopoChangeCount=_ArubaWiredRpvstVlanTopoChangeCount_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,2,1,16),_ArubaWiredRpvstVlanTopoChangeCount_Type())
arubaWiredRpvstVlanTopoChangeCount.setMaxAccess(_F)
if mibBuilder.loadTexts:arubaWiredRpvstVlanTopoChangeCount.setStatus(_B)
class _ArubaWiredRpvstVlanSendTopoChangeCtrl_Type(TruthValue):defaultValue=2
_ArubaWiredRpvstVlanSendTopoChangeCtrl_Type.__name__=_E
_ArubaWiredRpvstVlanSendTopoChangeCtrl_Object=MibTableColumn
arubaWiredRpvstVlanSendTopoChangeCtrl=_ArubaWiredRpvstVlanSendTopoChangeCtrl_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,2,1,17),_ArubaWiredRpvstVlanSendTopoChangeCtrl_Type())
arubaWiredRpvstVlanSendTopoChangeCtrl.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstVlanSendTopoChangeCtrl.setStatus(_B)
class _ArubaWiredRpvstVlanLogPortStateTransitions_Type(TruthValue):defaultValue=2
_ArubaWiredRpvstVlanLogPortStateTransitions_Type.__name__=_E
_ArubaWiredRpvstVlanLogPortStateTransitions_Object=MibTableColumn
arubaWiredRpvstVlanLogPortStateTransitions=_ArubaWiredRpvstVlanLogPortStateTransitions_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,2,1,18),_ArubaWiredRpvstVlanLogPortStateTransitions_Type())
arubaWiredRpvstVlanLogPortStateTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstVlanLogPortStateTransitions.setStatus(_B)
_ArubaWiredRpvstPortTable_Object=MibTable
arubaWiredRpvstPortTable=_ArubaWiredRpvstPortTable_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,3))
if mibBuilder.loadTexts:arubaWiredRpvstPortTable.setStatus(_B)
_ArubaWiredRpvstPortEntry_Object=MibTableRow
arubaWiredRpvstPortEntry=_ArubaWiredRpvstPortEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,3,1))
arubaWiredRpvstPortEntry.setIndexNames((0,_A,_c))
if mibBuilder.loadTexts:arubaWiredRpvstPortEntry.setStatus(_B)
_ArubaWiredRpvstPortIndex_Type=InterfaceIndex
_ArubaWiredRpvstPortIndex_Object=MibTableColumn
arubaWiredRpvstPortIndex=_ArubaWiredRpvstPortIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,3,1,1),_ArubaWiredRpvstPortIndex_Type())
arubaWiredRpvstPortIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:arubaWiredRpvstPortIndex.setStatus(_B)
class _ArubaWiredRpvstPortAdminEdge_Type(TruthValue):defaultValue=2
_ArubaWiredRpvstPortAdminEdge_Type.__name__=_E
_ArubaWiredRpvstPortAdminEdge_Object=MibTableColumn
arubaWiredRpvstPortAdminEdge=_ArubaWiredRpvstPortAdminEdge_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,3,1,2),_ArubaWiredRpvstPortAdminEdge_Type())
arubaWiredRpvstPortAdminEdge.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstPortAdminEdge.setStatus(_B)
class _ArubaWiredRpvstPortAdminPointToPoint_Type(PointToPoint):defaultValue=3
_ArubaWiredRpvstPortAdminPointToPoint_Type.__name__=_d
_ArubaWiredRpvstPortAdminPointToPoint_Object=MibTableColumn
arubaWiredRpvstPortAdminPointToPoint=_ArubaWiredRpvstPortAdminPointToPoint_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,3,1,3),_ArubaWiredRpvstPortAdminPointToPoint_Type())
arubaWiredRpvstPortAdminPointToPoint.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstPortAdminPointToPoint.setStatus(_B)
class _ArubaWiredRpvstPortAutoEdge_Type(TruthValue):defaultValue=1
_ArubaWiredRpvstPortAutoEdge_Type.__name__=_E
_ArubaWiredRpvstPortAutoEdge_Object=MibTableColumn
arubaWiredRpvstPortAutoEdge=_ArubaWiredRpvstPortAutoEdge_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,3,1,4),_ArubaWiredRpvstPortAutoEdge_Type())
arubaWiredRpvstPortAutoEdge.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstPortAutoEdge.setStatus(_B)
class _ArubaWiredRpvstPortBpduFiltering_Type(TruthValue):defaultValue=2
_ArubaWiredRpvstPortBpduFiltering_Type.__name__=_E
_ArubaWiredRpvstPortBpduFiltering_Object=MibTableColumn
arubaWiredRpvstPortBpduFiltering=_ArubaWiredRpvstPortBpduFiltering_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,3,1,5),_ArubaWiredRpvstPortBpduFiltering_Type())
arubaWiredRpvstPortBpduFiltering.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstPortBpduFiltering.setStatus(_B)
class _ArubaWiredRpvstPortRestrictedTcn_Type(TruthValue):defaultValue=2
_ArubaWiredRpvstPortRestrictedTcn_Type.__name__=_E
_ArubaWiredRpvstPortRestrictedTcn_Object=MibTableColumn
arubaWiredRpvstPortRestrictedTcn=_ArubaWiredRpvstPortRestrictedTcn_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,3,1,6),_ArubaWiredRpvstPortRestrictedTcn_Type())
arubaWiredRpvstPortRestrictedTcn.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstPortRestrictedTcn.setStatus(_B)
class _ArubaWiredRpvstPortRootGuard_Type(TruthValue):defaultValue=2
_ArubaWiredRpvstPortRootGuard_Type.__name__=_E
_ArubaWiredRpvstPortRootGuard_Object=MibTableColumn
arubaWiredRpvstPortRootGuard=_ArubaWiredRpvstPortRootGuard_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,3,1,7),_ArubaWiredRpvstPortRootGuard_Type())
arubaWiredRpvstPortRootGuard.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstPortRootGuard.setStatus(_B)
class _ArubaWiredRpvstPortLoopGuard_Type(TruthValue):defaultValue=2
_ArubaWiredRpvstPortLoopGuard_Type.__name__=_E
_ArubaWiredRpvstPortLoopGuard_Object=MibTableColumn
arubaWiredRpvstPortLoopGuard=_ArubaWiredRpvstPortLoopGuard_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,3,1,8),_ArubaWiredRpvstPortLoopGuard_Type())
arubaWiredRpvstPortLoopGuard.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstPortLoopGuard.setStatus(_B)
class _ArubaWiredRpvstPortBpduProtection_Type(TruthValue):defaultValue=2
_ArubaWiredRpvstPortBpduProtection_Type.__name__=_E
_ArubaWiredRpvstPortBpduProtection_Object=MibTableColumn
arubaWiredRpvstPortBpduProtection=_ArubaWiredRpvstPortBpduProtection_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,3,1,9),_ArubaWiredRpvstPortBpduProtection_Type())
arubaWiredRpvstPortBpduProtection.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstPortBpduProtection.setStatus(_B)
_ArubaWiredRpvstPortVlanTable_Object=MibTable
arubaWiredRpvstPortVlanTable=_ArubaWiredRpvstPortVlanTable_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,4))
if mibBuilder.loadTexts:arubaWiredRpvstPortVlanTable.setStatus(_B)
_ArubaWiredRpvstPortVlanEntry_Object=MibTableRow
arubaWiredRpvstPortVlanEntry=_ArubaWiredRpvstPortVlanEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,4,1))
arubaWiredRpvstPortVlanEntry.setIndexNames((0,_A,_e),(0,_A,_f))
if mibBuilder.loadTexts:arubaWiredRpvstPortVlanEntry.setStatus(_B)
_ArubaWiredRpvstPortVlanId_Type=VlanIndex
_ArubaWiredRpvstPortVlanId_Object=MibTableColumn
arubaWiredRpvstPortVlanId=_ArubaWiredRpvstPortVlanId_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,4,1,1),_ArubaWiredRpvstPortVlanId_Type())
arubaWiredRpvstPortVlanId.setMaxAccess(_K)
if mibBuilder.loadTexts:arubaWiredRpvstPortVlanId.setStatus(_B)
_ArubaWiredRpvstPortVlanIndex_Type=InterfaceIndex
_ArubaWiredRpvstPortVlanIndex_Object=MibTableColumn
arubaWiredRpvstPortVlanIndex=_ArubaWiredRpvstPortVlanIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,4,1,2),_ArubaWiredRpvstPortVlanIndex_Type())
arubaWiredRpvstPortVlanIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:arubaWiredRpvstPortVlanIndex.setStatus(_B)
class _ArubaWiredRpvstPortVlanPathCost_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_ArubaWiredRpvstPortVlanPathCost_Type.__name__=_D
_ArubaWiredRpvstPortVlanPathCost_Object=MibTableColumn
arubaWiredRpvstPortVlanPathCost=_ArubaWiredRpvstPortVlanPathCost_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,4,1,3),_ArubaWiredRpvstPortVlanPathCost_Type())
arubaWiredRpvstPortVlanPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstPortVlanPathCost.setStatus(_B)
class _ArubaWiredRpvstPortVlanPriority_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ArubaWiredRpvstPortVlanPriority_Type.__name__=_D
_ArubaWiredRpvstPortVlanPriority_Object=MibTableColumn
arubaWiredRpvstPortVlanPriority=_ArubaWiredRpvstPortVlanPriority_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,4,1,4),_ArubaWiredRpvstPortVlanPriority_Type())
arubaWiredRpvstPortVlanPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstPortVlanPriority.setStatus(_B)
class _ArubaWiredRpvstPortVlanResetCounters_Type(TruthValue):defaultValue=2
_ArubaWiredRpvstPortVlanResetCounters_Type.__name__=_E
_ArubaWiredRpvstPortVlanResetCounters_Object=MibTableColumn
arubaWiredRpvstPortVlanResetCounters=_ArubaWiredRpvstPortVlanResetCounters_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,4,1,5),_ArubaWiredRpvstPortVlanResetCounters_Type())
arubaWiredRpvstPortVlanResetCounters.setMaxAccess(_C)
if mibBuilder.loadTexts:arubaWiredRpvstPortVlanResetCounters.setStatus(_B)
class _ArubaWiredRpvstPortVlanRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('root',1),('alternate',2),('designated',3),('backup',4),('master',5),(_N,6)))
_ArubaWiredRpvstPortVlanRole_Type.__name__=_D
_ArubaWiredRpvstPortVlanRole_Object=MibTableColumn
arubaWiredRpvstPortVlanRole=_ArubaWiredRpvstPortVlanRole_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,4,1,6),_ArubaWiredRpvstPortVlanRole_Type())
arubaWiredRpvstPortVlanRole.setMaxAccess(_F)
if mibBuilder.loadTexts:arubaWiredRpvstPortVlanRole.setStatus(_B)
class _ArubaWiredRpvstPortVlanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_N,1),('blocking',2),('listening',3),('learning',4),('forwarding',5),('broken',6),('bpduError',7),('loopInconsistent',8),('pvidInconsistent',9),('rootGuard',10)))
_ArubaWiredRpvstPortVlanState_Type.__name__=_D
_ArubaWiredRpvstPortVlanState_Object=MibTableColumn
arubaWiredRpvstPortVlanState=_ArubaWiredRpvstPortVlanState_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,4,1,7),_ArubaWiredRpvstPortVlanState_Type())
arubaWiredRpvstPortVlanState.setMaxAccess(_F)
if mibBuilder.loadTexts:arubaWiredRpvstPortVlanState.setStatus(_B)
_ArubaWiredRpvstPortVlanDesigBridge_Type=MacAddress
_ArubaWiredRpvstPortVlanDesigBridge_Object=MibTableColumn
arubaWiredRpvstPortVlanDesigBridge=_ArubaWiredRpvstPortVlanDesigBridge_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,4,1,8),_ArubaWiredRpvstPortVlanDesigBridge_Type())
arubaWiredRpvstPortVlanDesigBridge.setMaxAccess(_F)
if mibBuilder.loadTexts:arubaWiredRpvstPortVlanDesigBridge.setStatus(_B)
_ArubaWiredRpvstPortVlanOperPointToPoint_Type=TruthValue
_ArubaWiredRpvstPortVlanOperPointToPoint_Object=MibTableColumn
arubaWiredRpvstPortVlanOperPointToPoint=_ArubaWiredRpvstPortVlanOperPointToPoint_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,4,1,9),_ArubaWiredRpvstPortVlanOperPointToPoint_Type())
arubaWiredRpvstPortVlanOperPointToPoint.setMaxAccess(_F)
if mibBuilder.loadTexts:arubaWiredRpvstPortVlanOperPointToPoint.setStatus(_B)
_ArubaWiredRpvstPortVlanOperEdge_Type=TruthValue
_ArubaWiredRpvstPortVlanOperEdge_Object=MibTableColumn
arubaWiredRpvstPortVlanOperEdge=_ArubaWiredRpvstPortVlanOperEdge_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,4,1,10),_ArubaWiredRpvstPortVlanOperEdge_Type())
arubaWiredRpvstPortVlanOperEdge.setMaxAccess(_F)
if mibBuilder.loadTexts:arubaWiredRpvstPortVlanOperEdge.setStatus(_B)
class _ArubaWiredRpvstPortVlanInconsistencyReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('invalid',0),('rootProtected',1),('loopProtected',2),('inconsistentPvidProtected',3)))
_ArubaWiredRpvstPortVlanInconsistencyReason_Type.__name__=_D
_ArubaWiredRpvstPortVlanInconsistencyReason_Object=MibTableColumn
arubaWiredRpvstPortVlanInconsistencyReason=_ArubaWiredRpvstPortVlanInconsistencyReason_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,4,1,11),_ArubaWiredRpvstPortVlanInconsistencyReason_Type())
arubaWiredRpvstPortVlanInconsistencyReason.setMaxAccess(_F)
if mibBuilder.loadTexts:arubaWiredRpvstPortVlanInconsistencyReason.setStatus(_B)
_ArubaWiredRpvstNotificationTable_Object=MibTable
arubaWiredRpvstNotificationTable=_ArubaWiredRpvstNotificationTable_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,5))
if mibBuilder.loadTexts:arubaWiredRpvstNotificationTable.setStatus(_B)
_ArubaWiredRpvstNotificationEntry_Object=MibTableRow
arubaWiredRpvstNotificationEntry=_ArubaWiredRpvstNotificationEntry_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,5,1))
arubaWiredRpvstNotificationEntry.setIndexNames((0,_A,_g))
if mibBuilder.loadTexts:arubaWiredRpvstNotificationEntry.setStatus(_B)
class _ArubaWiredRpvstPortName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredRpvstPortName_Type.__name__=_H
_ArubaWiredRpvstPortName_Object=MibTableColumn
arubaWiredRpvstPortName=_ArubaWiredRpvstPortName_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,5,1,1),_ArubaWiredRpvstPortName_Type())
arubaWiredRpvstPortName.setMaxAccess(_G)
if mibBuilder.loadTexts:arubaWiredRpvstPortName.setStatus(_B)
class _ArubaWiredRpvstVlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4097))
_ArubaWiredRpvstVlanIndex_Type.__name__=_D
_ArubaWiredRpvstVlanIndex_Object=MibTableColumn
arubaWiredRpvstVlanIndex=_ArubaWiredRpvstVlanIndex_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,5,1,2),_ArubaWiredRpvstVlanIndex_Type())
arubaWiredRpvstVlanIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:arubaWiredRpvstVlanIndex.setStatus(_B)
class _ArubaWiredRpvstPortVlanErrantBpduRxCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ArubaWiredRpvstPortVlanErrantBpduRxCount_Type.__name__=_D
_ArubaWiredRpvstPortVlanErrantBpduRxCount_Object=MibTableColumn
arubaWiredRpvstPortVlanErrantBpduRxCount=_ArubaWiredRpvstPortVlanErrantBpduRxCount_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,5,1,3),_ArubaWiredRpvstPortVlanErrantBpduRxCount_Type())
arubaWiredRpvstPortVlanErrantBpduRxCount.setMaxAccess(_G)
if mibBuilder.loadTexts:arubaWiredRpvstPortVlanErrantBpduRxCount.setStatus(_B)
_ArubaWiredRpvstErrantBpduSrcMac_Type=MacAddress
_ArubaWiredRpvstErrantBpduSrcMac_Object=MibTableColumn
arubaWiredRpvstErrantBpduSrcMac=_ArubaWiredRpvstErrantBpduSrcMac_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,5,1,4),_ArubaWiredRpvstErrantBpduSrcMac_Type())
arubaWiredRpvstErrantBpduSrcMac.setMaxAccess(_G)
if mibBuilder.loadTexts:arubaWiredRpvstErrantBpduSrcMac.setStatus(_B)
class _ArubaWiredRpvstSuperiorBpduSrcPort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredRpvstSuperiorBpduSrcPort_Type.__name__=_H
_ArubaWiredRpvstSuperiorBpduSrcPort_Object=MibTableColumn
arubaWiredRpvstSuperiorBpduSrcPort=_ArubaWiredRpvstSuperiorBpduSrcPort_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,5,1,5),_ArubaWiredRpvstSuperiorBpduSrcPort_Type())
arubaWiredRpvstSuperiorBpduSrcPort.setMaxAccess(_G)
if mibBuilder.loadTexts:arubaWiredRpvstSuperiorBpduSrcPort.setStatus(_B)
_ArubaWiredRpvstSuperiorBpduSrcMac_Type=MacAddress
_ArubaWiredRpvstSuperiorBpduSrcMac_Object=MibTableColumn
arubaWiredRpvstSuperiorBpduSrcMac=_ArubaWiredRpvstSuperiorBpduSrcMac_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,5,1,6),_ArubaWiredRpvstSuperiorBpduSrcMac_Type())
arubaWiredRpvstSuperiorBpduSrcMac.setMaxAccess(_G)
if mibBuilder.loadTexts:arubaWiredRpvstSuperiorBpduSrcMac.setStatus(_B)
class _ArubaWiredRpvstErrantBpduDetector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bpduFilter',1),('bpduProtection',2)))
_ArubaWiredRpvstErrantBpduDetector_Type.__name__=_D
_ArubaWiredRpvstErrantBpduDetector_Object=MibTableColumn
arubaWiredRpvstErrantBpduDetector=_ArubaWiredRpvstErrantBpduDetector_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,5,1,7),_ArubaWiredRpvstErrantBpduDetector_Type())
arubaWiredRpvstErrantBpduDetector.setMaxAccess(_G)
if mibBuilder.loadTexts:arubaWiredRpvstErrantBpduDetector.setStatus(_B)
class _ArubaWiredRpvstDesignatedPort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredRpvstDesignatedPort_Type.__name__=_H
_ArubaWiredRpvstDesignatedPort_Object=MibTableColumn
arubaWiredRpvstDesignatedPort=_ArubaWiredRpvstDesignatedPort_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,5,1,8),_ArubaWiredRpvstDesignatedPort_Type())
arubaWiredRpvstDesignatedPort.setMaxAccess(_G)
if mibBuilder.loadTexts:arubaWiredRpvstDesignatedPort.setStatus(_B)
class _ArubaWiredRpvstOldPortRole_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredRpvstOldPortRole_Type.__name__=_H
_ArubaWiredRpvstOldPortRole_Object=MibTableColumn
arubaWiredRpvstOldPortRole=_ArubaWiredRpvstOldPortRole_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,5,1,9),_ArubaWiredRpvstOldPortRole_Type())
arubaWiredRpvstOldPortRole.setMaxAccess(_G)
if mibBuilder.loadTexts:arubaWiredRpvstOldPortRole.setStatus(_B)
class _ArubaWiredRpvstNewPortRole_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredRpvstNewPortRole_Type.__name__=_H
_ArubaWiredRpvstNewPortRole_Object=MibTableColumn
arubaWiredRpvstNewPortRole=_ArubaWiredRpvstNewPortRole_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,5,1,10),_ArubaWiredRpvstNewPortRole_Type())
arubaWiredRpvstNewPortRole.setMaxAccess(_G)
if mibBuilder.loadTexts:arubaWiredRpvstNewPortRole.setStatus(_B)
_ArubaWiredRpvstTopoChangeTime_Type=DateAndTime
_ArubaWiredRpvstTopoChangeTime_Object=MibTableColumn
arubaWiredRpvstTopoChangeTime=_ArubaWiredRpvstTopoChangeTime_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,5,1,11),_ArubaWiredRpvstTopoChangeTime_Type())
arubaWiredRpvstTopoChangeTime.setMaxAccess(_G)
if mibBuilder.loadTexts:arubaWiredRpvstTopoChangeTime.setStatus(_B)
class _ArubaWiredRpvstPreviousRootBridgeID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredRpvstPreviousRootBridgeID_Type.__name__=_H
_ArubaWiredRpvstPreviousRootBridgeID_Object=MibTableColumn
arubaWiredRpvstPreviousRootBridgeID=_ArubaWiredRpvstPreviousRootBridgeID_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,5,1,12),_ArubaWiredRpvstPreviousRootBridgeID_Type())
arubaWiredRpvstPreviousRootBridgeID.setMaxAccess(_G)
if mibBuilder.loadTexts:arubaWiredRpvstPreviousRootBridgeID.setStatus(_B)
class _ArubaWiredRpvstNewRootBridgeID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_ArubaWiredRpvstNewRootBridgeID_Type.__name__=_H
_ArubaWiredRpvstNewRootBridgeID_Object=MibTableColumn
arubaWiredRpvstNewRootBridgeID=_ArubaWiredRpvstNewRootBridgeID_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,5,1,13),_ArubaWiredRpvstNewRootBridgeID_Type())
arubaWiredRpvstNewRootBridgeID.setMaxAccess(_G)
if mibBuilder.loadTexts:arubaWiredRpvstNewRootBridgeID.setStatus(_B)
_ArubaWiredRpvstRootBridgeChangeTimeStamp_Type=DateAndTime
_ArubaWiredRpvstRootBridgeChangeTimeStamp_Object=MibTableColumn
arubaWiredRpvstRootBridgeChangeTimeStamp=_ArubaWiredRpvstRootBridgeChangeTimeStamp_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,5,1,14),_ArubaWiredRpvstRootBridgeChangeTimeStamp_Type())
arubaWiredRpvstRootBridgeChangeTimeStamp.setMaxAccess(_G)
if mibBuilder.loadTexts:arubaWiredRpvstRootBridgeChangeTimeStamp.setStatus(_B)
class _ArubaWiredRpvstId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4097))
_ArubaWiredRpvstId_Type.__name__=_D
_ArubaWiredRpvstId_Object=MibTableColumn
arubaWiredRpvstId=_ArubaWiredRpvstId_Object((1,3,6,1,4,1,47196,4,1,1,3,5,1,5,1,15),_ArubaWiredRpvstId_Type())
arubaWiredRpvstId.setMaxAccess(_K)
if mibBuilder.loadTexts:arubaWiredRpvstId.setStatus(_B)
_ArubaWiredRpvstConformance_ObjectIdentity=ObjectIdentity
arubaWiredRpvstConformance=_ArubaWiredRpvstConformance_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,5,2))
_ArubaWiredRpvstGroups_ObjectIdentity=ObjectIdentity
arubaWiredRpvstGroups=_ArubaWiredRpvstGroups_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,5,2,1))
_ArubaWiredRpvstCompliances_ObjectIdentity=ObjectIdentity
arubaWiredRpvstCompliances=_ArubaWiredRpvstCompliances_ObjectIdentity((1,3,6,1,4,1,47196,4,1,1,3,5,2,2))
arubaWiredRpvstGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,5,2,1,1))
arubaWiredRpvstGroup.setObjects(*((_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:arubaWiredRpvstGroup.setStatus(_B)
arubaWiredRpvstVlanGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,5,2,1,2))
arubaWiredRpvstVlanGroup.setObjects(*((_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:arubaWiredRpvstVlanGroup.setStatus(_B)
arubaWiredRpvstPortVlanGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,5,2,1,3))
arubaWiredRpvstPortVlanGroup.setObjects(*((_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_O),(_A,_M),(_A,_A6),(_A,_A7)))
if mibBuilder.loadTexts:arubaWiredRpvstPortVlanGroup.setStatus(_B)
arubaWiredRpvstPortGroup=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,5,2,1,4))
arubaWiredRpvstPortGroup.setObjects(*((_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF)))
if mibBuilder.loadTexts:arubaWiredRpvstPortGroup.setStatus(_B)
arubaWiredRpvstPvst1=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,5,2,1,5))
arubaWiredRpvstPvst1.setObjects(*((_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ)))
if mibBuilder.loadTexts:arubaWiredRpvstPvst1.setStatus(_B)
arubaWiredRpvstNotificationObjectGrp=ObjectGroup((1,3,6,1,4,1,47196,4,1,1,3,5,2,1,6))
arubaWiredRpvstNotificationObjectGrp.setObjects(*((_A,_J),(_A,_I),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:arubaWiredRpvstNotificationObjectGrp.setStatus(_B)
arubaWiredRpvstErrantBpduReceived=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,5,0,1))
arubaWiredRpvstErrantBpduReceived.setObjects(*((_A,_I),(_A,_J),(_A,_P),(_A,_O),(_A,_M),(_A,_U),(_A,_Q),(_A,_T)))
if mibBuilder.loadTexts:arubaWiredRpvstErrantBpduReceived.setStatus(_B)
arubaWiredRpvstNewRoot=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,5,0,2))
arubaWiredRpvstNewRoot.setObjects(*((_A,_I),(_A,_Z),(_A,_Y),(_A,_a)))
if mibBuilder.loadTexts:arubaWiredRpvstNewRoot.setStatus(_B)
arubaWiredRpvstRootGuardInconsistency=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,5,0,3))
arubaWiredRpvstRootGuardInconsistency.setObjects(*((_A,_I),(_A,_J),(_A,_S),(_A,_R)))
if mibBuilder.loadTexts:arubaWiredRpvstRootGuardInconsistency.setStatus(_B)
arubaWiredRpvstLoopGuardInconsistency=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,5,0,4))
arubaWiredRpvstLoopGuardInconsistency.setObjects(*((_A,_I),(_A,_J),(_A,_M)))
if mibBuilder.loadTexts:arubaWiredRpvstLoopGuardInconsistency.setStatus(_B)
arubaWiredRpvstTopologyChange=NotificationType((1,3,6,1,4,1,47196,4,1,1,3,5,0,5))
arubaWiredRpvstTopologyChange.setObjects(*((_A,_I),(_A,_J),(_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:arubaWiredRpvstTopologyChange.setStatus(_B)
arubaWiredRpvstNotificationGroup=NotificationGroup((1,3,6,1,4,1,47196,4,1,1,3,5,2,1,7))
arubaWiredRpvstNotificationGroup.setObjects(*((_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:arubaWiredRpvstNotificationGroup.setStatus(_B)
arubaWiredRpvstCompliance1=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,5,2,2,1))
arubaWiredRpvstCompliance1.setObjects(*((_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS)))
if mibBuilder.loadTexts:arubaWiredRpvstCompliance1.setStatus(_B)
arubaWiredRpvstCompliance2=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,5,2,2,2))
arubaWiredRpvstCompliance2.setObjects((_A,_AT))
if mibBuilder.loadTexts:arubaWiredRpvstCompliance2.setStatus(_B)
arubaWiredRpvstNotificationCompliance=ModuleCompliance((1,3,6,1,4,1,47196,4,1,1,3,5,2,2,3))
arubaWiredRpvstNotificationCompliance.setObjects(*((_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:arubaWiredRpvstNotificationCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_d:PointToPoint,'arubaWiredRpvstMIB':arubaWiredRpvstMIB,'arubaWiredRpvstNotifications':arubaWiredRpvstNotifications,_AK:arubaWiredRpvstErrantBpduReceived,_AL:arubaWiredRpvstNewRoot,_AM:arubaWiredRpvstRootGuardInconsistency,_AN:arubaWiredRpvstLoopGuardInconsistency,_AO:arubaWiredRpvstTopologyChange,'arubaWiredRpvstObjects':arubaWiredRpvstObjects,'arubaWiredRpvstGeneralGroup':arubaWiredRpvstGeneralGroup,_h:arubaWiredRpvstResetCounters,_i:arubaWiredRpvstExtendedSystemID,_j:arubaWiredRpvstIgnorePVIDInconsistency,_AG:arubaWiredRpvstPathCostMode,_k:arubaWiredRpvstBpduGuardTimeout,_l:arubaWiredRpvstMstpInterconnectVlan,_m:arubaWiredRpvstCurrentVportCount,'arubaWiredRpvstVlanTable':arubaWiredRpvstVlanTable,'arubaWiredRpvstVlanEntry':arubaWiredRpvstVlanEntry,_b:arubaWiredRpvstVlanId,_n:arubaWiredRpvstVlanHelloTime,_o:arubaWiredRpvstVlanForwardDelay,_p:arubaWiredRpvstVlanMaxAge,_q:arubaWiredRpvstVlanPriority,_r:arubaWiredRpvstVlanRoot,_s:arubaWiredRpvstVlanRpvstAdminStatus,_t:arubaWiredRpvstVlanResetCounters,_u:arubaWiredRpvstVlanOperHelloTime,_v:arubaWiredRpvstVlanRootPriority,_w:arubaWiredRpvstVlanRootPort,_x:arubaWiredRpvstVlanRootPathCost,_y:arubaWiredRpvstVlanRootMacAddress,_z:arubaWiredRpvstVlanRootChangeCounter,_A0:arubaWiredRpvstVlanTimeSinceLastTopoChange,_A1:arubaWiredRpvstVlanTopoChangeCount,_AH:arubaWiredRpvstVlanSendTopoChangeCtrl,_AI:arubaWiredRpvstVlanLogPortStateTransitions,'arubaWiredRpvstPortTable':arubaWiredRpvstPortTable,'arubaWiredRpvstPortEntry':arubaWiredRpvstPortEntry,_c:arubaWiredRpvstPortIndex,_A8:arubaWiredRpvstPortAdminEdge,_A9:arubaWiredRpvstPortAdminPointToPoint,_AA:arubaWiredRpvstPortAutoEdge,_AB:arubaWiredRpvstPortBpduFiltering,_AC:arubaWiredRpvstPortRestrictedTcn,_AD:arubaWiredRpvstPortRootGuard,_AE:arubaWiredRpvstPortLoopGuard,_AF:arubaWiredRpvstPortBpduProtection,'arubaWiredRpvstPortVlanTable':arubaWiredRpvstPortVlanTable,'arubaWiredRpvstPortVlanEntry':arubaWiredRpvstPortVlanEntry,_e:arubaWiredRpvstPortVlanId,_f:arubaWiredRpvstPortVlanIndex,_A2:arubaWiredRpvstPortVlanPathCost,_A3:arubaWiredRpvstPortVlanPriority,_A4:arubaWiredRpvstPortVlanResetCounters,_A5:arubaWiredRpvstPortVlanRole,_O:arubaWiredRpvstPortVlanState,_M:arubaWiredRpvstPortVlanDesigBridge,_A6:arubaWiredRpvstPortVlanOperPointToPoint,_A7:arubaWiredRpvstPortVlanOperEdge,_AJ:arubaWiredRpvstPortVlanInconsistencyReason,'arubaWiredRpvstNotificationTable':arubaWiredRpvstNotificationTable,'arubaWiredRpvstNotificationEntry':arubaWiredRpvstNotificationEntry,_J:arubaWiredRpvstPortName,_I:arubaWiredRpvstVlanIndex,_P:arubaWiredRpvstPortVlanErrantBpduRxCount,_Q:arubaWiredRpvstErrantBpduSrcMac,_R:arubaWiredRpvstSuperiorBpduSrcPort,_S:arubaWiredRpvstSuperiorBpduSrcMac,_T:arubaWiredRpvstErrantBpduDetector,_U:arubaWiredRpvstDesignatedPort,_V:arubaWiredRpvstOldPortRole,_W:arubaWiredRpvstNewPortRole,_X:arubaWiredRpvstTopoChangeTime,_Y:arubaWiredRpvstPreviousRootBridgeID,_Z:arubaWiredRpvstNewRootBridgeID,_a:arubaWiredRpvstRootBridgeChangeTimeStamp,_g:arubaWiredRpvstId,'arubaWiredRpvstConformance':arubaWiredRpvstConformance,'arubaWiredRpvstGroups':arubaWiredRpvstGroups,_AP:arubaWiredRpvstGroup,_AQ:arubaWiredRpvstVlanGroup,_AR:arubaWiredRpvstPortVlanGroup,_AS:arubaWiredRpvstPortGroup,_AT:arubaWiredRpvstPvst1,_AU:arubaWiredRpvstNotificationObjectGrp,_AV:arubaWiredRpvstNotificationGroup,'arubaWiredRpvstCompliances':arubaWiredRpvstCompliances,'arubaWiredRpvstCompliance1':arubaWiredRpvstCompliance1,'arubaWiredRpvstCompliance2':arubaWiredRpvstCompliance2,'arubaWiredRpvstNotificationCompliance':arubaWiredRpvstNotificationCompliance})