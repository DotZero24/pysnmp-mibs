_M='stpPortIndex'
_L='stpPortCardIndex'
_K='stpPortStpIndex'
_J='stpGlobalSetIndex'
_I='OctetString'
_H='not-accessible'
_G='Timeout'
_F='NSCRTV-EPON-STP-MGM-MIB'
_E='centi-seconds'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,Timeout=mibBuilder.importSymbols('BRIDGE-MIB','BridgeId',_G)
AutoNegotiationTechAbility,EponAlarmCode,EponAlarmInstance,EponCardIndex,EponDeviceIndex,EponPortIndex,EponSeverityType,EponStats15MinRecordType,EponStats24HourRecordType,EponStatsThresholdType,TAddress,stpManagementObjects=mibBuilder.importSymbols('NSCRTV-EPONEOC-EPON-MIB','AutoNegotiationTechAbility','EponAlarmCode','EponAlarmInstance','EponCardIndex','EponDeviceIndex','EponPortIndex','EponSeverityType','EponStats15MinRecordType','EponStats24HourRecordType','EponStatsThresholdType','TAddress','stpManagementObjects')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
_StpGlobalSetTable_Object=MibTable
stpGlobalSetTable=_StpGlobalSetTable_Object((1,3,6,1,4,1,17409,2,3,9,1))
if mibBuilder.loadTexts:stpGlobalSetTable.setStatus(_A)
_StpGlobalSetEntry_Object=MibTableRow
stpGlobalSetEntry=_StpGlobalSetEntry_Object((1,3,6,1,4,1,17409,2,3,9,1,1))
stpGlobalSetEntry.setIndexNames((0,_F,_J))
if mibBuilder.loadTexts:stpGlobalSetEntry.setStatus(_A)
_StpGlobalSetIndex_Type=EponDeviceIndex
_StpGlobalSetIndex_Object=MibTableColumn
stpGlobalSetIndex=_StpGlobalSetIndex_Object((1,3,6,1,4,1,17409,2,3,9,1,1,1),_StpGlobalSetIndex_Type())
stpGlobalSetIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:stpGlobalSetIndex.setStatus(_A)
class _StpGlobalSetVersion_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rstp',1),('stp',2)))
_StpGlobalSetVersion_Type.__name__=_D
_StpGlobalSetVersion_Object=MibTableColumn
stpGlobalSetVersion=_StpGlobalSetVersion_Object((1,3,6,1,4,1,17409,2,3,9,1,1,2),_StpGlobalSetVersion_Type())
stpGlobalSetVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:stpGlobalSetVersion.setStatus(_A)
class _StpGlobalSetPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_StpGlobalSetPriority_Type.__name__=_D
_StpGlobalSetPriority_Object=MibTableColumn
stpGlobalSetPriority=_StpGlobalSetPriority_Object((1,3,6,1,4,1,17409,2,3,9,1,1,3),_StpGlobalSetPriority_Type())
stpGlobalSetPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:stpGlobalSetPriority.setStatus(_A)
_StpGlobalSetTimeSinceTopologyChange_Type=TimeTicks
_StpGlobalSetTimeSinceTopologyChange_Object=MibTableColumn
stpGlobalSetTimeSinceTopologyChange=_StpGlobalSetTimeSinceTopologyChange_Object((1,3,6,1,4,1,17409,2,3,9,1,1,4),_StpGlobalSetTimeSinceTopologyChange_Type())
stpGlobalSetTimeSinceTopologyChange.setMaxAccess(_B)
if mibBuilder.loadTexts:stpGlobalSetTimeSinceTopologyChange.setStatus(_A)
_StpGlobalSetTopChanges_Type=Counter32
_StpGlobalSetTopChanges_Object=MibTableColumn
stpGlobalSetTopChanges=_StpGlobalSetTopChanges_Object((1,3,6,1,4,1,17409,2,3,9,1,1,5),_StpGlobalSetTopChanges_Type())
stpGlobalSetTopChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:stpGlobalSetTopChanges.setStatus(_A)
if mibBuilder.loadTexts:stpGlobalSetTopChanges.setUnits('topology changes')
_StpGlobalSetDesignatedRoot_Type=BridgeId
_StpGlobalSetDesignatedRoot_Object=MibTableColumn
stpGlobalSetDesignatedRoot=_StpGlobalSetDesignatedRoot_Object((1,3,6,1,4,1,17409,2,3,9,1,1,6),_StpGlobalSetDesignatedRoot_Type())
stpGlobalSetDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:stpGlobalSetDesignatedRoot.setStatus(_A)
_StpGlobalSetRootCost_Type=Integer32
_StpGlobalSetRootCost_Object=MibTableColumn
stpGlobalSetRootCost=_StpGlobalSetRootCost_Object((1,3,6,1,4,1,17409,2,3,9,1,1,7),_StpGlobalSetRootCost_Type())
stpGlobalSetRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:stpGlobalSetRootCost.setStatus(_A)
class _StpGlobalSetRootPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,3));fixedLength=3
_StpGlobalSetRootPort_Type.__name__=_I
_StpGlobalSetRootPort_Object=MibTableColumn
stpGlobalSetRootPort=_StpGlobalSetRootPort_Object((1,3,6,1,4,1,17409,2,3,9,1,1,8),_StpGlobalSetRootPort_Type())
stpGlobalSetRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:stpGlobalSetRootPort.setStatus(_A)
_StpGlobalSetMaxAge_Type=Timeout
_StpGlobalSetMaxAge_Object=MibTableColumn
stpGlobalSetMaxAge=_StpGlobalSetMaxAge_Object((1,3,6,1,4,1,17409,2,3,9,1,1,9),_StpGlobalSetMaxAge_Type())
stpGlobalSetMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:stpGlobalSetMaxAge.setStatus(_A)
if mibBuilder.loadTexts:stpGlobalSetMaxAge.setUnits(_E)
_StpGlobalSetHelloTime_Type=Timeout
_StpGlobalSetHelloTime_Object=MibTableColumn
stpGlobalSetHelloTime=_StpGlobalSetHelloTime_Object((1,3,6,1,4,1,17409,2,3,9,1,1,10),_StpGlobalSetHelloTime_Type())
stpGlobalSetHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:stpGlobalSetHelloTime.setStatus(_A)
if mibBuilder.loadTexts:stpGlobalSetHelloTime.setUnits(_E)
_StpGlobalSetHoldTime_Type=Integer32
_StpGlobalSetHoldTime_Object=MibTableColumn
stpGlobalSetHoldTime=_StpGlobalSetHoldTime_Object((1,3,6,1,4,1,17409,2,3,9,1,1,11),_StpGlobalSetHoldTime_Type())
stpGlobalSetHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:stpGlobalSetHoldTime.setStatus(_A)
if mibBuilder.loadTexts:stpGlobalSetHoldTime.setUnits(_E)
_StpGlobalSetForwardDelay_Type=Timeout
_StpGlobalSetForwardDelay_Object=MibTableColumn
stpGlobalSetForwardDelay=_StpGlobalSetForwardDelay_Object((1,3,6,1,4,1,17409,2,3,9,1,1,12),_StpGlobalSetForwardDelay_Type())
stpGlobalSetForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:stpGlobalSetForwardDelay.setStatus(_A)
if mibBuilder.loadTexts:stpGlobalSetForwardDelay.setUnits(_E)
class _StpGlobalSetBridgeMaxAge_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(600,4000))
_StpGlobalSetBridgeMaxAge_Type.__name__=_G
_StpGlobalSetBridgeMaxAge_Object=MibTableColumn
stpGlobalSetBridgeMaxAge=_StpGlobalSetBridgeMaxAge_Object((1,3,6,1,4,1,17409,2,3,9,1,1,13),_StpGlobalSetBridgeMaxAge_Type())
stpGlobalSetBridgeMaxAge.setMaxAccess(_C)
if mibBuilder.loadTexts:stpGlobalSetBridgeMaxAge.setStatus(_A)
if mibBuilder.loadTexts:stpGlobalSetBridgeMaxAge.setUnits(_E)
class _StpGlobalSetBridgeHelloTime_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_StpGlobalSetBridgeHelloTime_Type.__name__=_G
_StpGlobalSetBridgeHelloTime_Object=MibTableColumn
stpGlobalSetBridgeHelloTime=_StpGlobalSetBridgeHelloTime_Object((1,3,6,1,4,1,17409,2,3,9,1,1,14),_StpGlobalSetBridgeHelloTime_Type())
stpGlobalSetBridgeHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:stpGlobalSetBridgeHelloTime.setStatus(_A)
if mibBuilder.loadTexts:stpGlobalSetBridgeHelloTime.setUnits(_E)
class _StpGlobalSetBridgeForwardDelay_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(400,3000))
_StpGlobalSetBridgeForwardDelay_Type.__name__=_G
_StpGlobalSetBridgeForwardDelay_Object=MibTableColumn
stpGlobalSetBridgeForwardDelay=_StpGlobalSetBridgeForwardDelay_Object((1,3,6,1,4,1,17409,2,3,9,1,1,15),_StpGlobalSetBridgeForwardDelay_Type())
stpGlobalSetBridgeForwardDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:stpGlobalSetBridgeForwardDelay.setStatus(_A)
if mibBuilder.loadTexts:stpGlobalSetBridgeForwardDelay.setUnits(_E)
class _StpGlobalSetRstpTxHoldCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_StpGlobalSetRstpTxHoldCount_Type.__name__=_D
_StpGlobalSetRstpTxHoldCount_Object=MibTableColumn
stpGlobalSetRstpTxHoldCount=_StpGlobalSetRstpTxHoldCount_Object((1,3,6,1,4,1,17409,2,3,9,1,1,16),_StpGlobalSetRstpTxHoldCount_Type())
stpGlobalSetRstpTxHoldCount.setMaxAccess(_C)
if mibBuilder.loadTexts:stpGlobalSetRstpTxHoldCount.setStatus(_A)
_StpGlobalSetEnable_Type=TruthValue
_StpGlobalSetEnable_Object=MibTableColumn
stpGlobalSetEnable=_StpGlobalSetEnable_Object((1,3,6,1,4,1,17409,2,3,9,1,1,17),_StpGlobalSetEnable_Type())
stpGlobalSetEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:stpGlobalSetEnable.setStatus(_A)
_StpPortTable_Object=MibTable
stpPortTable=_StpPortTable_Object((1,3,6,1,4,1,17409,2,3,9,2))
if mibBuilder.loadTexts:stpPortTable.setStatus(_A)
_StpPortEntry_Object=MibTableRow
stpPortEntry=_StpPortEntry_Object((1,3,6,1,4,1,17409,2,3,9,2,1))
stpPortEntry.setIndexNames((0,_F,_K),(0,_F,_L),(0,_F,_M))
if mibBuilder.loadTexts:stpPortEntry.setStatus(_A)
_StpPortStpIndex_Type=EponDeviceIndex
_StpPortStpIndex_Object=MibTableColumn
stpPortStpIndex=_StpPortStpIndex_Object((1,3,6,1,4,1,17409,2,3,9,2,1,1),_StpPortStpIndex_Type())
stpPortStpIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:stpPortStpIndex.setStatus(_A)
_StpPortCardIndex_Type=EponCardIndex
_StpPortCardIndex_Object=MibTableColumn
stpPortCardIndex=_StpPortCardIndex_Object((1,3,6,1,4,1,17409,2,3,9,2,1,2),_StpPortCardIndex_Type())
stpPortCardIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:stpPortCardIndex.setStatus(_A)
_StpPortIndex_Type=EponPortIndex
_StpPortIndex_Object=MibTableColumn
stpPortIndex=_StpPortIndex_Object((1,3,6,1,4,1,17409,2,3,9,2,1,3),_StpPortIndex_Type())
stpPortIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:stpPortIndex.setStatus(_A)
class _StpPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('disabled',1),('blocking',2),('listening',3),('learning',4),('forwarding',5),('broken',6)))
_StpPortStatus_Type.__name__=_D
_StpPortStatus_Object=MibTableColumn
stpPortStatus=_StpPortStatus_Object((1,3,6,1,4,1,17409,2,3,9,2,1,4),_StpPortStatus_Type())
stpPortStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:stpPortStatus.setStatus(_A)
class _StpPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_StpPortPriority_Type.__name__=_D
_StpPortPriority_Object=MibTableColumn
stpPortPriority=_StpPortPriority_Object((1,3,6,1,4,1,17409,2,3,9,2,1,5),_StpPortPriority_Type())
stpPortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:stpPortPriority.setStatus(_A)
class _StpPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_StpPortPathCost_Type.__name__=_D
_StpPortPathCost_Object=MibTableColumn
stpPortPathCost=_StpPortPathCost_Object((1,3,6,1,4,1,17409,2,3,9,2,1,6),_StpPortPathCost_Type())
stpPortPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:stpPortPathCost.setStatus(_A)
_StpPortDesignatedRoot_Type=BridgeId
_StpPortDesignatedRoot_Object=MibTableColumn
stpPortDesignatedRoot=_StpPortDesignatedRoot_Object((1,3,6,1,4,1,17409,2,3,9,2,1,7),_StpPortDesignatedRoot_Type())
stpPortDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:stpPortDesignatedRoot.setStatus(_A)
_StpPortDesignatedCost_Type=Integer32
_StpPortDesignatedCost_Object=MibTableColumn
stpPortDesignatedCost=_StpPortDesignatedCost_Object((1,3,6,1,4,1,17409,2,3,9,2,1,8),_StpPortDesignatedCost_Type())
stpPortDesignatedCost.setMaxAccess(_B)
if mibBuilder.loadTexts:stpPortDesignatedCost.setStatus(_A)
_StpPortDesignatedBridge_Type=BridgeId
_StpPortDesignatedBridge_Object=MibTableColumn
stpPortDesignatedBridge=_StpPortDesignatedBridge_Object((1,3,6,1,4,1,17409,2,3,9,2,1,9),_StpPortDesignatedBridge_Type())
stpPortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:stpPortDesignatedBridge.setStatus(_A)
_StpPortDesignatedPort_Type=Gauge32
_StpPortDesignatedPort_Object=MibTableColumn
stpPortDesignatedPort=_StpPortDesignatedPort_Object((1,3,6,1,4,1,17409,2,3,9,2,1,10),_StpPortDesignatedPort_Type())
stpPortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:stpPortDesignatedPort.setStatus(_A)
_StpPortForwardTransitions_Type=Unsigned32
_StpPortForwardTransitions_Object=MibTableColumn
stpPortForwardTransitions=_StpPortForwardTransitions_Object((1,3,6,1,4,1,17409,2,3,9,2,1,11),_StpPortForwardTransitions_Type())
stpPortForwardTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:stpPortForwardTransitions.setStatus(_A)
if mibBuilder.loadTexts:stpPortForwardTransitions.setUnits('seconds')
_StpPortRstpProtocolMigration_Type=TruthValue
_StpPortRstpProtocolMigration_Object=MibTableColumn
stpPortRstpProtocolMigration=_StpPortRstpProtocolMigration_Object((1,3,6,1,4,1,17409,2,3,9,2,1,12),_StpPortRstpProtocolMigration_Type())
stpPortRstpProtocolMigration.setMaxAccess(_C)
if mibBuilder.loadTexts:stpPortRstpProtocolMigration.setStatus(_A)
_StpPortRstpAdminEdgePort_Type=TruthValue
_StpPortRstpAdminEdgePort_Object=MibTableColumn
stpPortRstpAdminEdgePort=_StpPortRstpAdminEdgePort_Object((1,3,6,1,4,1,17409,2,3,9,2,1,13),_StpPortRstpAdminEdgePort_Type())
stpPortRstpAdminEdgePort.setMaxAccess(_C)
if mibBuilder.loadTexts:stpPortRstpAdminEdgePort.setStatus(_A)
_StpPortRstpOperEdgePort_Type=TruthValue
_StpPortRstpOperEdgePort_Object=MibTableColumn
stpPortRstpOperEdgePort=_StpPortRstpOperEdgePort_Object((1,3,6,1,4,1,17409,2,3,9,2,1,14),_StpPortRstpOperEdgePort_Type())
stpPortRstpOperEdgePort.setMaxAccess(_B)
if mibBuilder.loadTexts:stpPortRstpOperEdgePort.setStatus(_A)
class _StpPortPointToPointAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('forceFalse',0),('forceTrue',1),('auto',2)))
_StpPortPointToPointAdminStatus_Type.__name__=_D
_StpPortPointToPointAdminStatus_Object=MibTableColumn
stpPortPointToPointAdminStatus=_StpPortPointToPointAdminStatus_Object((1,3,6,1,4,1,17409,2,3,9,2,1,15),_StpPortPointToPointAdminStatus_Type())
stpPortPointToPointAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:stpPortPointToPointAdminStatus.setStatus(_A)
_StpPortPointToPointOperStatus_Type=TruthValue
_StpPortPointToPointOperStatus_Object=MibTableColumn
stpPortPointToPointOperStatus=_StpPortPointToPointOperStatus_Object((1,3,6,1,4,1,17409,2,3,9,2,1,16),_StpPortPointToPointOperStatus_Type())
stpPortPointToPointOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:stpPortPointToPointOperStatus.setStatus(_A)
_StpPortEnabled_Type=TruthValue
_StpPortEnabled_Object=MibTableColumn
stpPortEnabled=_StpPortEnabled_Object((1,3,6,1,4,1,17409,2,3,9,2,1,17),_StpPortEnabled_Type())
stpPortEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:stpPortEnabled.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'stpGlobalSetTable':stpGlobalSetTable,'stpGlobalSetEntry':stpGlobalSetEntry,_J:stpGlobalSetIndex,'stpGlobalSetVersion':stpGlobalSetVersion,'stpGlobalSetPriority':stpGlobalSetPriority,'stpGlobalSetTimeSinceTopologyChange':stpGlobalSetTimeSinceTopologyChange,'stpGlobalSetTopChanges':stpGlobalSetTopChanges,'stpGlobalSetDesignatedRoot':stpGlobalSetDesignatedRoot,'stpGlobalSetRootCost':stpGlobalSetRootCost,'stpGlobalSetRootPort':stpGlobalSetRootPort,'stpGlobalSetMaxAge':stpGlobalSetMaxAge,'stpGlobalSetHelloTime':stpGlobalSetHelloTime,'stpGlobalSetHoldTime':stpGlobalSetHoldTime,'stpGlobalSetForwardDelay':stpGlobalSetForwardDelay,'stpGlobalSetBridgeMaxAge':stpGlobalSetBridgeMaxAge,'stpGlobalSetBridgeHelloTime':stpGlobalSetBridgeHelloTime,'stpGlobalSetBridgeForwardDelay':stpGlobalSetBridgeForwardDelay,'stpGlobalSetRstpTxHoldCount':stpGlobalSetRstpTxHoldCount,'stpGlobalSetEnable':stpGlobalSetEnable,'stpPortTable':stpPortTable,'stpPortEntry':stpPortEntry,_K:stpPortStpIndex,_L:stpPortCardIndex,_M:stpPortIndex,'stpPortStatus':stpPortStatus,'stpPortPriority':stpPortPriority,'stpPortPathCost':stpPortPathCost,'stpPortDesignatedRoot':stpPortDesignatedRoot,'stpPortDesignatedCost':stpPortDesignatedCost,'stpPortDesignatedBridge':stpPortDesignatedBridge,'stpPortDesignatedPort':stpPortDesignatedPort,'stpPortForwardTransitions':stpPortForwardTransitions,'stpPortRstpProtocolMigration':stpPortRstpProtocolMigration,'stpPortRstpAdminEdgePort':stpPortRstpAdminEdgePort,'stpPortRstpOperEdgePort':stpPortRstpOperEdgePort,'stpPortPointToPointAdminStatus':stpPortPointToPointAdminStatus,'stpPortPointToPointOperStatus':stpPortPointToPointOperStatus,'stpPortEnabled':stpPortEnabled})