_b='mstpBridgeStatusIndex'
_a='mstpStatusTableIndex'
_Z='master'
_Y='backup'
_X='alternate'
_W='designated'
_V='broken'
_U='listening'
_T='blocking'
_S='forwarding'
_R='learning'
_Q='discarding'
_P='portStatusPortIndex'
_O='bridgeStatusIndex'
_N='mstpGroupIndex'
_M='portConfigPortIndex'
_L='bridgeConfigIndex'
_K='true'
_J='false'
_I='unknown'
_H='enabled'
_G='not-accessible'
_F='G6-STP-MIB'
_E='disabled'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
protocol=ModuleIdentity((1,3,6,1,4,1,3181,10,6,2))
if mibBuilder.loadTexts:protocol.setRevisions(('2018-02-12 16:19',))
_Stp_ObjectIdentity=ObjectIdentity
stp=_Stp_ObjectIdentity((1,3,6,1,4,1,3181,10,6,2,42))
_BridgeConfigTable_Object=MibTable
bridgeConfigTable=_BridgeConfigTable_Object((1,3,6,1,4,1,3181,10,6,2,42,1))
if mibBuilder.loadTexts:bridgeConfigTable.setStatus(_A)
_BridgeConfigEntry_Object=MibTableRow
bridgeConfigEntry=_BridgeConfigEntry_Object((1,3,6,1,4,1,3181,10,6,2,42,1,1))
bridgeConfigEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:bridgeConfigEntry.setStatus(_A)
class _BridgeConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_BridgeConfigIndex_Type.__name__=_B
_BridgeConfigIndex_Object=MibTableColumn
bridgeConfigIndex=_BridgeConfigIndex_Object((1,3,6,1,4,1,3181,10,6,2,42,1,1,1),_BridgeConfigIndex_Type())
bridgeConfigIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:bridgeConfigIndex.setStatus(_A)
class _BridgeConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_E,0),('stp',1),('rstp',2),('mstp',3)))
_BridgeConfigMode_Type.__name__=_B
_BridgeConfigMode_Object=MibTableColumn
bridgeConfigMode=_BridgeConfigMode_Object((1,3,6,1,4,1,3181,10,6,2,42,1,1,2),_BridgeConfigMode_Type())
bridgeConfigMode.setMaxAccess(_D)
if mibBuilder.loadTexts:bridgeConfigMode.setStatus(_A)
class _BridgeConfigPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BridgeConfigPriority_Type.__name__=_B
_BridgeConfigPriority_Object=MibTableColumn
bridgeConfigPriority=_BridgeConfigPriority_Object((1,3,6,1,4,1,3181,10,6,2,42,1,1,3),_BridgeConfigPriority_Type())
bridgeConfigPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:bridgeConfigPriority.setStatus(_A)
class _BridgeConfigHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BridgeConfigHelloTime_Type.__name__=_B
_BridgeConfigHelloTime_Object=MibTableColumn
bridgeConfigHelloTime=_BridgeConfigHelloTime_Object((1,3,6,1,4,1,3181,10,6,2,42,1,1,4),_BridgeConfigHelloTime_Type())
bridgeConfigHelloTime.setMaxAccess(_D)
if mibBuilder.loadTexts:bridgeConfigHelloTime.setStatus(_A)
class _BridgeConfigMaxAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BridgeConfigMaxAge_Type.__name__=_B
_BridgeConfigMaxAge_Object=MibTableColumn
bridgeConfigMaxAge=_BridgeConfigMaxAge_Object((1,3,6,1,4,1,3181,10,6,2,42,1,1,5),_BridgeConfigMaxAge_Type())
bridgeConfigMaxAge.setMaxAccess(_D)
if mibBuilder.loadTexts:bridgeConfigMaxAge.setStatus(_A)
class _BridgeConfigForwardDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BridgeConfigForwardDelay_Type.__name__=_B
_BridgeConfigForwardDelay_Object=MibTableColumn
bridgeConfigForwardDelay=_BridgeConfigForwardDelay_Object((1,3,6,1,4,1,3181,10,6,2,42,1,1,6),_BridgeConfigForwardDelay_Type())
bridgeConfigForwardDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:bridgeConfigForwardDelay.setStatus(_A)
class _BridgeConfigTxHoldCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BridgeConfigTxHoldCount_Type.__name__=_B
_BridgeConfigTxHoldCount_Object=MibTableColumn
bridgeConfigTxHoldCount=_BridgeConfigTxHoldCount_Object((1,3,6,1,4,1,3181,10,6,2,42,1,1,7),_BridgeConfigTxHoldCount_Type())
bridgeConfigTxHoldCount.setMaxAccess(_D)
if mibBuilder.loadTexts:bridgeConfigTxHoldCount.setStatus(_A)
class _BridgeConfigIeeePathCostModel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ms1998Compliant',0),('ms2004Compliant',1)))
_BridgeConfigIeeePathCostModel_Type.__name__=_B
_BridgeConfigIeeePathCostModel_Object=MibTableColumn
bridgeConfigIeeePathCostModel=_BridgeConfigIeeePathCostModel_Object((1,3,6,1,4,1,3181,10,6,2,42,1,1,8),_BridgeConfigIeeePathCostModel_Type())
bridgeConfigIeeePathCostModel.setMaxAccess(_D)
if mibBuilder.loadTexts:bridgeConfigIeeePathCostModel.setStatus(_A)
_BridgeConfigMstpRegionName_Type=DisplayString
_BridgeConfigMstpRegionName_Object=MibTableColumn
bridgeConfigMstpRegionName=_BridgeConfigMstpRegionName_Object((1,3,6,1,4,1,3181,10,6,2,42,1,1,9),_BridgeConfigMstpRegionName_Type())
bridgeConfigMstpRegionName.setMaxAccess(_D)
if mibBuilder.loadTexts:bridgeConfigMstpRegionName.setStatus(_A)
class _BridgeConfigMstpRevisionLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BridgeConfigMstpRevisionLevel_Type.__name__=_B
_BridgeConfigMstpRevisionLevel_Object=MibTableColumn
bridgeConfigMstpRevisionLevel=_BridgeConfigMstpRevisionLevel_Object((1,3,6,1,4,1,3181,10,6,2,42,1,1,10),_BridgeConfigMstpRevisionLevel_Type())
bridgeConfigMstpRevisionLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:bridgeConfigMstpRevisionLevel.setStatus(_A)
class _BridgeConfigMstpMaxHops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BridgeConfigMstpMaxHops_Type.__name__=_B
_BridgeConfigMstpMaxHops_Object=MibTableColumn
bridgeConfigMstpMaxHops=_BridgeConfigMstpMaxHops_Object((1,3,6,1,4,1,3181,10,6,2,42,1,1,11),_BridgeConfigMstpMaxHops_Type())
bridgeConfigMstpMaxHops.setMaxAccess(_D)
if mibBuilder.loadTexts:bridgeConfigMstpMaxHops.setStatus(_A)
_BridgeConfigMstpStpAgingTime_Type=Unsigned32
_BridgeConfigMstpStpAgingTime_Object=MibTableColumn
bridgeConfigMstpStpAgingTime=_BridgeConfigMstpStpAgingTime_Object((1,3,6,1,4,1,3181,10,6,2,42,1,1,12),_BridgeConfigMstpStpAgingTime_Type())
bridgeConfigMstpStpAgingTime.setMaxAccess(_D)
if mibBuilder.loadTexts:bridgeConfigMstpStpAgingTime.setStatus(_A)
_PortConfigTable_Object=MibTable
portConfigTable=_PortConfigTable_Object((1,3,6,1,4,1,3181,10,6,2,42,2))
if mibBuilder.loadTexts:portConfigTable.setStatus(_A)
_PortConfigEntry_Object=MibTableRow
portConfigEntry=_PortConfigEntry_Object((1,3,6,1,4,1,3181,10,6,2,42,2,1))
portConfigEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:portConfigEntry.setStatus(_A)
class _PortConfigPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_PortConfigPortIndex_Type.__name__=_B
_PortConfigPortIndex_Object=MibTableColumn
portConfigPortIndex=_PortConfigPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,42,2,1,1),_PortConfigPortIndex_Type())
portConfigPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:portConfigPortIndex.setStatus(_A)
class _PortConfigEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_H,1)))
_PortConfigEnable_Type.__name__=_B
_PortConfigEnable_Object=MibTableColumn
portConfigEnable=_PortConfigEnable_Object((1,3,6,1,4,1,3181,10,6,2,42,2,1,2),_PortConfigEnable_Type())
portConfigEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:portConfigEnable.setStatus(_A)
class _PortConfigPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PortConfigPriority_Type.__name__=_B
_PortConfigPriority_Object=MibTableColumn
portConfigPriority=_PortConfigPriority_Object((1,3,6,1,4,1,3181,10,6,2,42,2,1,3),_PortConfigPriority_Type())
portConfigPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:portConfigPriority.setStatus(_A)
class _PortConfigAdminP2pPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('auto',0),('forceFalse',1),('forceTrue',2)))
_PortConfigAdminP2pPort_Type.__name__=_B
_PortConfigAdminP2pPort_Object=MibTableColumn
portConfigAdminP2pPort=_PortConfigAdminP2pPort_Object((1,3,6,1,4,1,3181,10,6,2,42,2,1,4),_PortConfigAdminP2pPort_Type())
portConfigAdminP2pPort.setMaxAccess(_D)
if mibBuilder.loadTexts:portConfigAdminP2pPort.setStatus(_A)
class _PortConfigAdminEdgePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_H,1)))
_PortConfigAdminEdgePort_Type.__name__=_B
_PortConfigAdminEdgePort_Object=MibTableColumn
portConfigAdminEdgePort=_PortConfigAdminEdgePort_Object((1,3,6,1,4,1,3181,10,6,2,42,2,1,5),_PortConfigAdminEdgePort_Type())
portConfigAdminEdgePort.setMaxAccess(_D)
if mibBuilder.loadTexts:portConfigAdminEdgePort.setStatus(_A)
_PortConfigAdminPathCost_Type=Unsigned32
_PortConfigAdminPathCost_Object=MibTableColumn
portConfigAdminPathCost=_PortConfigAdminPathCost_Object((1,3,6,1,4,1,3181,10,6,2,42,2,1,6),_PortConfigAdminPathCost_Type())
portConfigAdminPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:portConfigAdminPathCost.setStatus(_A)
_PortConfigProtocolMigration_Type=DisplayString
_PortConfigProtocolMigration_Object=MibTableColumn
portConfigProtocolMigration=_PortConfigProtocolMigration_Object((1,3,6,1,4,1,3181,10,6,2,42,2,1,7),_PortConfigProtocolMigration_Type())
portConfigProtocolMigration.setMaxAccess(_D)
if mibBuilder.loadTexts:portConfigProtocolMigration.setStatus(_A)
class _PortConfigBridgeAssurance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_H,1)))
_PortConfigBridgeAssurance_Type.__name__=_B
_PortConfigBridgeAssurance_Object=MibTableColumn
portConfigBridgeAssurance=_PortConfigBridgeAssurance_Object((1,3,6,1,4,1,3181,10,6,2,42,2,1,8),_PortConfigBridgeAssurance_Type())
portConfigBridgeAssurance.setMaxAccess(_D)
if mibBuilder.loadTexts:portConfigBridgeAssurance.setStatus(_A)
class _PortConfigMstpDefaultPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PortConfigMstpDefaultPriority_Type.__name__=_B
_PortConfigMstpDefaultPriority_Object=MibTableColumn
portConfigMstpDefaultPriority=_PortConfigMstpDefaultPriority_Object((1,3,6,1,4,1,3181,10,6,2,42,2,1,9),_PortConfigMstpDefaultPriority_Type())
portConfigMstpDefaultPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:portConfigMstpDefaultPriority.setStatus(_A)
_PortConfigMstpPortPriority_Type=DisplayString
_PortConfigMstpPortPriority_Object=MibTableColumn
portConfigMstpPortPriority=_PortConfigMstpPortPriority_Object((1,3,6,1,4,1,3181,10,6,2,42,2,1,10),_PortConfigMstpPortPriority_Type())
portConfigMstpPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:portConfigMstpPortPriority.setStatus(_A)
_PortConfigMstpDefaultAdminPathCost_Type=Unsigned32
_PortConfigMstpDefaultAdminPathCost_Object=MibTableColumn
portConfigMstpDefaultAdminPathCost=_PortConfigMstpDefaultAdminPathCost_Object((1,3,6,1,4,1,3181,10,6,2,42,2,1,11),_PortConfigMstpDefaultAdminPathCost_Type())
portConfigMstpDefaultAdminPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:portConfigMstpDefaultAdminPathCost.setStatus(_A)
_PortConfigMstpPortAdminPathCost_Type=DisplayString
_PortConfigMstpPortAdminPathCost_Object=MibTableColumn
portConfigMstpPortAdminPathCost=_PortConfigMstpPortAdminPathCost_Object((1,3,6,1,4,1,3181,10,6,2,42,2,1,12),_PortConfigMstpPortAdminPathCost_Type())
portConfigMstpPortAdminPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:portConfigMstpPortAdminPathCost.setStatus(_A)
class _PortConfigBpduGuard_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('dropAndEvent',1),('blockPort',2)))
_PortConfigBpduGuard_Type.__name__=_B
_PortConfigBpduGuard_Object=MibTableColumn
portConfigBpduGuard=_PortConfigBpduGuard_Object((1,3,6,1,4,1,3181,10,6,2,42,2,1,13),_PortConfigBpduGuard_Type())
portConfigBpduGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:portConfigBpduGuard.setStatus(_A)
class _PortConfigBpduReceiveOnly_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_H,1)))
_PortConfigBpduReceiveOnly_Type.__name__=_B
_PortConfigBpduReceiveOnly_Object=MibTableColumn
portConfigBpduReceiveOnly=_PortConfigBpduReceiveOnly_Object((1,3,6,1,4,1,3181,10,6,2,42,2,1,14),_PortConfigBpduReceiveOnly_Type())
portConfigBpduReceiveOnly.setMaxAccess(_D)
if mibBuilder.loadTexts:portConfigBpduReceiveOnly.setStatus(_A)
class _PortConfigRestrictTcn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_H,1)))
_PortConfigRestrictTcn_Type.__name__=_B
_PortConfigRestrictTcn_Object=MibTableColumn
portConfigRestrictTcn=_PortConfigRestrictTcn_Object((1,3,6,1,4,1,3181,10,6,2,42,2,1,15),_PortConfigRestrictTcn_Type())
portConfigRestrictTcn.setMaxAccess(_D)
if mibBuilder.loadTexts:portConfigRestrictTcn.setStatus(_A)
class _PortConfigRestrictRoot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_H,1)))
_PortConfigRestrictRoot_Type.__name__=_B
_PortConfigRestrictRoot_Object=MibTableColumn
portConfigRestrictRoot=_PortConfigRestrictRoot_Object((1,3,6,1,4,1,3181,10,6,2,42,2,1,16),_PortConfigRestrictRoot_Type())
portConfigRestrictRoot.setMaxAccess(_D)
if mibBuilder.loadTexts:portConfigRestrictRoot.setStatus(_A)
_MstpGroupTable_Object=MibTable
mstpGroupTable=_MstpGroupTable_Object((1,3,6,1,4,1,3181,10,6,2,42,3))
if mibBuilder.loadTexts:mstpGroupTable.setStatus(_A)
_MstpGroupEntry_Object=MibTableRow
mstpGroupEntry=_MstpGroupEntry_Object((1,3,6,1,4,1,3181,10,6,2,42,3,1))
mstpGroupEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:mstpGroupEntry.setStatus(_A)
class _MstpGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,62))
_MstpGroupIndex_Type.__name__=_B
_MstpGroupIndex_Object=MibTableColumn
mstpGroupIndex=_MstpGroupIndex_Object((1,3,6,1,4,1,3181,10,6,2,42,3,1,1),_MstpGroupIndex_Type())
mstpGroupIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mstpGroupIndex.setStatus(_A)
_MstpGroupMstpId_Type=DisplayString
_MstpGroupMstpId_Object=MibTableColumn
mstpGroupMstpId=_MstpGroupMstpId_Object((1,3,6,1,4,1,3181,10,6,2,42,3,1,2),_MstpGroupMstpId_Type())
mstpGroupMstpId.setMaxAccess(_D)
if mibBuilder.loadTexts:mstpGroupMstpId.setStatus(_A)
class _MstpGroupBridgePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MstpGroupBridgePriority_Type.__name__=_B
_MstpGroupBridgePriority_Object=MibTableColumn
mstpGroupBridgePriority=_MstpGroupBridgePriority_Object((1,3,6,1,4,1,3181,10,6,2,42,3,1,3),_MstpGroupBridgePriority_Type())
mstpGroupBridgePriority.setMaxAccess(_D)
if mibBuilder.loadTexts:mstpGroupBridgePriority.setStatus(_A)
_BridgeStatusTable_Object=MibTable
bridgeStatusTable=_BridgeStatusTable_Object((1,3,6,1,4,1,3181,10,6,2,42,100))
if mibBuilder.loadTexts:bridgeStatusTable.setStatus(_A)
_BridgeStatusEntry_Object=MibTableRow
bridgeStatusEntry=_BridgeStatusEntry_Object((1,3,6,1,4,1,3181,10,6,2,42,100,1))
bridgeStatusEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:bridgeStatusEntry.setStatus(_A)
class _BridgeStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_BridgeStatusIndex_Type.__name__=_B
_BridgeStatusIndex_Object=MibTableColumn
bridgeStatusIndex=_BridgeStatusIndex_Object((1,3,6,1,4,1,3181,10,6,2,42,100,1,1),_BridgeStatusIndex_Type())
bridgeStatusIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:bridgeStatusIndex.setStatus(_A)
class _BridgeStatusStpProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_BridgeStatusStpProtocol_Type.__name__=_B
_BridgeStatusStpProtocol_Object=MibTableColumn
bridgeStatusStpProtocol=_BridgeStatusStpProtocol_Object((1,3,6,1,4,1,3181,10,6,2,42,100,1,2),_BridgeStatusStpProtocol_Type())
bridgeStatusStpProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeStatusStpProtocol.setStatus(_A)
class _BridgeStatusHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BridgeStatusHelloTime_Type.__name__=_B
_BridgeStatusHelloTime_Object=MibTableColumn
bridgeStatusHelloTime=_BridgeStatusHelloTime_Object((1,3,6,1,4,1,3181,10,6,2,42,100,1,3),_BridgeStatusHelloTime_Type())
bridgeStatusHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeStatusHelloTime.setStatus(_A)
class _BridgeStatusMaxAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BridgeStatusMaxAge_Type.__name__=_B
_BridgeStatusMaxAge_Object=MibTableColumn
bridgeStatusMaxAge=_BridgeStatusMaxAge_Object((1,3,6,1,4,1,3181,10,6,2,42,100,1,4),_BridgeStatusMaxAge_Type())
bridgeStatusMaxAge.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeStatusMaxAge.setStatus(_A)
class _BridgeStatusHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BridgeStatusHoldTime_Type.__name__=_B
_BridgeStatusHoldTime_Object=MibTableColumn
bridgeStatusHoldTime=_BridgeStatusHoldTime_Object((1,3,6,1,4,1,3181,10,6,2,42,100,1,5),_BridgeStatusHoldTime_Type())
bridgeStatusHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeStatusHoldTime.setStatus(_A)
class _BridgeStatusForwardDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BridgeStatusForwardDelay_Type.__name__=_B
_BridgeStatusForwardDelay_Object=MibTableColumn
bridgeStatusForwardDelay=_BridgeStatusForwardDelay_Object((1,3,6,1,4,1,3181,10,6,2,42,100,1,6),_BridgeStatusForwardDelay_Type())
bridgeStatusForwardDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeStatusForwardDelay.setStatus(_A)
class _BridgeStatusRootPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BridgeStatusRootPort_Type.__name__=_B
_BridgeStatusRootPort_Object=MibTableColumn
bridgeStatusRootPort=_BridgeStatusRootPort_Object((1,3,6,1,4,1,3181,10,6,2,42,100,1,7),_BridgeStatusRootPort_Type())
bridgeStatusRootPort.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeStatusRootPort.setStatus(_A)
_BridgeStatusRootCost_Type=Unsigned32
_BridgeStatusRootCost_Object=MibTableColumn
bridgeStatusRootCost=_BridgeStatusRootCost_Object((1,3,6,1,4,1,3181,10,6,2,42,100,1,8),_BridgeStatusRootCost_Type())
bridgeStatusRootCost.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeStatusRootCost.setStatus(_A)
class _BridgeStatusTopologyChanges_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BridgeStatusTopologyChanges_Type.__name__=_B
_BridgeStatusTopologyChanges_Object=MibTableColumn
bridgeStatusTopologyChanges=_BridgeStatusTopologyChanges_Object((1,3,6,1,4,1,3181,10,6,2,42,100,1,9),_BridgeStatusTopologyChanges_Type())
bridgeStatusTopologyChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeStatusTopologyChanges.setStatus(_A)
_BridgeStatusLastTopologyChange_Type=Counter32
_BridgeStatusLastTopologyChange_Object=MibTableColumn
bridgeStatusLastTopologyChange=_BridgeStatusLastTopologyChange_Object((1,3,6,1,4,1,3181,10,6,2,42,100,1,10),_BridgeStatusLastTopologyChange_Type())
bridgeStatusLastTopologyChange.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeStatusLastTopologyChange.setStatus(_A)
_BridgeStatusMstpRegionName_Type=DisplayString
_BridgeStatusMstpRegionName_Object=MibTableColumn
bridgeStatusMstpRegionName=_BridgeStatusMstpRegionName_Object((1,3,6,1,4,1,3181,10,6,2,42,100,1,11),_BridgeStatusMstpRegionName_Type())
bridgeStatusMstpRegionName.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeStatusMstpRegionName.setStatus(_A)
class _BridgeStatusMstiRevisionLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BridgeStatusMstiRevisionLevel_Type.__name__=_B
_BridgeStatusMstiRevisionLevel_Object=MibTableColumn
bridgeStatusMstiRevisionLevel=_BridgeStatusMstiRevisionLevel_Object((1,3,6,1,4,1,3181,10,6,2,42,100,1,12),_BridgeStatusMstiRevisionLevel_Type())
bridgeStatusMstiRevisionLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeStatusMstiRevisionLevel.setStatus(_A)
_BridgeStatusCistInternalRootPathCost_Type=Unsigned32
_BridgeStatusCistInternalRootPathCost_Object=MibTableColumn
bridgeStatusCistInternalRootPathCost=_BridgeStatusCistInternalRootPathCost_Object((1,3,6,1,4,1,3181,10,6,2,42,100,1,13),_BridgeStatusCistInternalRootPathCost_Type())
bridgeStatusCistInternalRootPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeStatusCistInternalRootPathCost.setStatus(_A)
_BridgeStatusCistRegionalRootId_Type=DisplayString
_BridgeStatusCistRegionalRootId_Object=MibTableColumn
bridgeStatusCistRegionalRootId=_BridgeStatusCistRegionalRootId_Object((1,3,6,1,4,1,3181,10,6,2,42,100,1,14),_BridgeStatusCistRegionalRootId_Type())
bridgeStatusCistRegionalRootId.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeStatusCistRegionalRootId.setStatus(_A)
_BridgeStatusCistRegionalRootPriority_Type=Unsigned32
_BridgeStatusCistRegionalRootPriority_Object=MibTableColumn
bridgeStatusCistRegionalRootPriority=_BridgeStatusCistRegionalRootPriority_Object((1,3,6,1,4,1,3181,10,6,2,42,100,1,15),_BridgeStatusCistRegionalRootPriority_Type())
bridgeStatusCistRegionalRootPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeStatusCistRegionalRootPriority.setStatus(_A)
_BridgeStatusCistRegionalRootMac_Type=MacAddress
_BridgeStatusCistRegionalRootMac_Object=MibTableColumn
bridgeStatusCistRegionalRootMac=_BridgeStatusCistRegionalRootMac_Object((1,3,6,1,4,1,3181,10,6,2,42,100,1,16),_BridgeStatusCistRegionalRootMac_Type())
bridgeStatusCistRegionalRootMac.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeStatusCistRegionalRootMac.setStatus(_A)
class _BridgeStatusMaxHops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BridgeStatusMaxHops_Type.__name__=_B
_BridgeStatusMaxHops_Object=MibTableColumn
bridgeStatusMaxHops=_BridgeStatusMaxHops_Object((1,3,6,1,4,1,3181,10,6,2,42,100,1,17),_BridgeStatusMaxHops_Type())
bridgeStatusMaxHops.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeStatusMaxHops.setStatus(_A)
_BridgeStatusMstpStpAgingTime_Type=Unsigned32
_BridgeStatusMstpStpAgingTime_Object=MibTableColumn
bridgeStatusMstpStpAgingTime=_BridgeStatusMstpStpAgingTime_Object((1,3,6,1,4,1,3181,10,6,2,42,100,1,18),_BridgeStatusMstpStpAgingTime_Type())
bridgeStatusMstpStpAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bridgeStatusMstpStpAgingTime.setStatus(_A)
_PortStatusTable_Object=MibTable
portStatusTable=_PortStatusTable_Object((1,3,6,1,4,1,3181,10,6,2,42,101))
if mibBuilder.loadTexts:portStatusTable.setStatus(_A)
_PortStatusEntry_Object=MibTableRow
portStatusEntry=_PortStatusEntry_Object((1,3,6,1,4,1,3181,10,6,2,42,101,1))
portStatusEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:portStatusEntry.setStatus(_A)
class _PortStatusPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_PortStatusPortIndex_Type.__name__=_B
_PortStatusPortIndex_Object=MibTableColumn
portStatusPortIndex=_PortStatusPortIndex_Object((1,3,6,1,4,1,3181,10,6,2,42,101,1,1),_PortStatusPortIndex_Type())
portStatusPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:portStatusPortIndex.setStatus(_A)
class _PortStatusPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PortStatusPort_Type.__name__=_B
_PortStatusPort_Object=MibTableColumn
portStatusPort=_PortStatusPort_Object((1,3,6,1,4,1,3181,10,6,2,42,101,1,2),_PortStatusPort_Type())
portStatusPort.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusPort.setStatus(_A)
class _PortStatusState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_I,0),(_Q,1),(_R,2),(_S,3),(_T,4),(_U,5),(_V,6)))
_PortStatusState_Type.__name__=_B
_PortStatusState_Object=MibTableColumn
portStatusState=_PortStatusState_Object((1,3,6,1,4,1,3181,10,6,2,42,101,1,3),_PortStatusState_Type())
portStatusState.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusState.setStatus(_A)
_PortStatusLocalPortCost_Type=Unsigned32
_PortStatusLocalPortCost_Object=MibTableColumn
portStatusLocalPortCost=_PortStatusLocalPortCost_Object((1,3,6,1,4,1,3181,10,6,2,42,101,1,4),_PortStatusLocalPortCost_Type())
portStatusLocalPortCost.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusLocalPortCost.setStatus(_A)
_PortStatusDesignatedPortId_Type=DisplayString
_PortStatusDesignatedPortId_Object=MibTableColumn
portStatusDesignatedPortId=_PortStatusDesignatedPortId_Object((1,3,6,1,4,1,3181,10,6,2,42,101,1,5),_PortStatusDesignatedPortId_Type())
portStatusDesignatedPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusDesignatedPortId.setStatus(_A)
_PortStatusDesignatedPort_Type=Unsigned32
_PortStatusDesignatedPort_Object=MibTableColumn
portStatusDesignatedPort=_PortStatusDesignatedPort_Object((1,3,6,1,4,1,3181,10,6,2,42,101,1,6),_PortStatusDesignatedPort_Type())
portStatusDesignatedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusDesignatedPort.setStatus(_A)
_PortStatusDesignatedPortPriority_Type=Unsigned32
_PortStatusDesignatedPortPriority_Object=MibTableColumn
portStatusDesignatedPortPriority=_PortStatusDesignatedPortPriority_Object((1,3,6,1,4,1,3181,10,6,2,42,101,1,7),_PortStatusDesignatedPortPriority_Type())
portStatusDesignatedPortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusDesignatedPortPriority.setStatus(_A)
_PortStatusDesignatedCost_Type=Unsigned32
_PortStatusDesignatedCost_Object=MibTableColumn
portStatusDesignatedCost=_PortStatusDesignatedCost_Object((1,3,6,1,4,1,3181,10,6,2,42,101,1,8),_PortStatusDesignatedCost_Type())
portStatusDesignatedCost.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusDesignatedCost.setStatus(_A)
_PortStatusDesignatedRootId_Type=DisplayString
_PortStatusDesignatedRootId_Object=MibTableColumn
portStatusDesignatedRootId=_PortStatusDesignatedRootId_Object((1,3,6,1,4,1,3181,10,6,2,42,101,1,9),_PortStatusDesignatedRootId_Type())
portStatusDesignatedRootId.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusDesignatedRootId.setStatus(_A)
_PortStatusDesignatedRootMac_Type=MacAddress
_PortStatusDesignatedRootMac_Object=MibTableColumn
portStatusDesignatedRootMac=_PortStatusDesignatedRootMac_Object((1,3,6,1,4,1,3181,10,6,2,42,101,1,10),_PortStatusDesignatedRootMac_Type())
portStatusDesignatedRootMac.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusDesignatedRootMac.setStatus(_A)
class _PortStatusDesignatedRootPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PortStatusDesignatedRootPriority_Type.__name__=_B
_PortStatusDesignatedRootPriority_Object=MibTableColumn
portStatusDesignatedRootPriority=_PortStatusDesignatedRootPriority_Object((1,3,6,1,4,1,3181,10,6,2,42,101,1,11),_PortStatusDesignatedRootPriority_Type())
portStatusDesignatedRootPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusDesignatedRootPriority.setStatus(_A)
_PortStatusDesignatedBridgeId_Type=DisplayString
_PortStatusDesignatedBridgeId_Object=MibTableColumn
portStatusDesignatedBridgeId=_PortStatusDesignatedBridgeId_Object((1,3,6,1,4,1,3181,10,6,2,42,101,1,12),_PortStatusDesignatedBridgeId_Type())
portStatusDesignatedBridgeId.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusDesignatedBridgeId.setStatus(_A)
_PortStatusDesignatedBridgeMac_Type=MacAddress
_PortStatusDesignatedBridgeMac_Object=MibTableColumn
portStatusDesignatedBridgeMac=_PortStatusDesignatedBridgeMac_Object((1,3,6,1,4,1,3181,10,6,2,42,101,1,13),_PortStatusDesignatedBridgeMac_Type())
portStatusDesignatedBridgeMac.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusDesignatedBridgeMac.setStatus(_A)
class _PortStatusDesignatedBridgePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PortStatusDesignatedBridgePriority_Type.__name__=_B
_PortStatusDesignatedBridgePriority_Object=MibTableColumn
portStatusDesignatedBridgePriority=_PortStatusDesignatedBridgePriority_Object((1,3,6,1,4,1,3181,10,6,2,42,101,1,14),_PortStatusDesignatedBridgePriority_Type())
portStatusDesignatedBridgePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusDesignatedBridgePriority.setStatus(_A)
_PortStatusForwardTransition_Type=Unsigned32
_PortStatusForwardTransition_Object=MibTableColumn
portStatusForwardTransition=_PortStatusForwardTransition_Object((1,3,6,1,4,1,3181,10,6,2,42,101,1,15),_PortStatusForwardTransition_Type())
portStatusForwardTransition.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusForwardTransition.setStatus(_A)
class _PortStatusOperEdgePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_PortStatusOperEdgePort_Type.__name__=_B
_PortStatusOperEdgePort_Object=MibTableColumn
portStatusOperEdgePort=_PortStatusOperEdgePort_Object((1,3,6,1,4,1,3181,10,6,2,42,101,1,16),_PortStatusOperEdgePort_Type())
portStatusOperEdgePort.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusOperEdgePort.setStatus(_A)
class _PortStatusOperP2pPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_PortStatusOperP2pPort_Type.__name__=_B
_PortStatusOperP2pPort_Object=MibTableColumn
portStatusOperP2pPort=_PortStatusOperP2pPort_Object((1,3,6,1,4,1,3181,10,6,2,42,101,1,17),_PortStatusOperP2pPort_Type())
portStatusOperP2pPort.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusOperP2pPort.setStatus(_A)
class _PortStatusRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_I,0),('root',1),(_W,2),(_X,3),(_Y,4),(_Z,5),(_E,6)))
_PortStatusRole_Type.__name__=_B
_PortStatusRole_Object=MibTableColumn
portStatusRole=_PortStatusRole_Object((1,3,6,1,4,1,3181,10,6,2,42,101,1,18),_PortStatusRole_Type())
portStatusRole.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusRole.setStatus(_A)
class _PortStatusInconsistentBridge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_PortStatusInconsistentBridge_Type.__name__=_B
_PortStatusInconsistentBridge_Object=MibTableColumn
portStatusInconsistentBridge=_PortStatusInconsistentBridge_Object((1,3,6,1,4,1,3181,10,6,2,42,101,1,19),_PortStatusInconsistentBridge_Type())
portStatusInconsistentBridge.setMaxAccess(_C)
if mibBuilder.loadTexts:portStatusInconsistentBridge.setStatus(_A)
_MstpStatusTableTable_Object=MibTable
mstpStatusTableTable=_MstpStatusTableTable_Object((1,3,6,1,4,1,3181,10,6,2,42,102))
if mibBuilder.loadTexts:mstpStatusTableTable.setStatus(_A)
_MstpStatusTableEntry_Object=MibTableRow
mstpStatusTableEntry=_MstpStatusTableEntry_Object((1,3,6,1,4,1,3181,10,6,2,42,102,1))
mstpStatusTableEntry.setIndexNames((0,_F,_a))
if mibBuilder.loadTexts:mstpStatusTableEntry.setStatus(_A)
class _MstpStatusTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2047))
_MstpStatusTableIndex_Type.__name__=_B
_MstpStatusTableIndex_Object=MibTableColumn
mstpStatusTableIndex=_MstpStatusTableIndex_Object((1,3,6,1,4,1,3181,10,6,2,42,102,1,1),_MstpStatusTableIndex_Type())
mstpStatusTableIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mstpStatusTableIndex.setStatus(_A)
class _MstpStatusTableMstpId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MstpStatusTableMstpId_Type.__name__=_B
_MstpStatusTableMstpId_Object=MibTableColumn
mstpStatusTableMstpId=_MstpStatusTableMstpId_Object((1,3,6,1,4,1,3181,10,6,2,42,102,1,2),_MstpStatusTableMstpId_Type())
mstpStatusTableMstpId.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpStatusTableMstpId.setStatus(_A)
class _MstpStatusTablePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MstpStatusTablePort_Type.__name__=_B
_MstpStatusTablePort_Object=MibTableColumn
mstpStatusTablePort=_MstpStatusTablePort_Object((1,3,6,1,4,1,3181,10,6,2,42,102,1,3),_MstpStatusTablePort_Type())
mstpStatusTablePort.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpStatusTablePort.setStatus(_A)
class _MstpStatusTableState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_I,0),(_Q,1),(_R,2),(_S,3),(_T,4),(_U,5),(_V,6)))
_MstpStatusTableState_Type.__name__=_B
_MstpStatusTableState_Object=MibTableColumn
mstpStatusTableState=_MstpStatusTableState_Object((1,3,6,1,4,1,3181,10,6,2,42,102,1,4),_MstpStatusTableState_Type())
mstpStatusTableState.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpStatusTableState.setStatus(_A)
class _MstpStatusTablePortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MstpStatusTablePortPriority_Type.__name__=_B
_MstpStatusTablePortPriority_Object=MibTableColumn
mstpStatusTablePortPriority=_MstpStatusTablePortPriority_Object((1,3,6,1,4,1,3181,10,6,2,42,102,1,5),_MstpStatusTablePortPriority_Type())
mstpStatusTablePortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpStatusTablePortPriority.setStatus(_A)
_MstpStatusTableInternalAdminPathCost_Type=Unsigned32
_MstpStatusTableInternalAdminPathCost_Object=MibTableColumn
mstpStatusTableInternalAdminPathCost=_MstpStatusTableInternalAdminPathCost_Object((1,3,6,1,4,1,3181,10,6,2,42,102,1,6),_MstpStatusTableInternalAdminPathCost_Type())
mstpStatusTableInternalAdminPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpStatusTableInternalAdminPathCost.setStatus(_A)
_MstpStatusTableForwardTransition_Type=Unsigned32
_MstpStatusTableForwardTransition_Object=MibTableColumn
mstpStatusTableForwardTransition=_MstpStatusTableForwardTransition_Object((1,3,6,1,4,1,3181,10,6,2,42,102,1,7),_MstpStatusTableForwardTransition_Type())
mstpStatusTableForwardTransition.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpStatusTableForwardTransition.setStatus(_A)
class _MstpStatusTableRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_I,0),('root',1),(_W,2),(_X,3),(_Y,4),(_Z,5),(_E,6)))
_MstpStatusTableRole_Type.__name__=_B
_MstpStatusTableRole_Object=MibTableColumn
mstpStatusTableRole=_MstpStatusTableRole_Object((1,3,6,1,4,1,3181,10,6,2,42,102,1,8),_MstpStatusTableRole_Type())
mstpStatusTableRole.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpStatusTableRole.setStatus(_A)
_MstpBridgeStatusTable_Object=MibTable
mstpBridgeStatusTable=_MstpBridgeStatusTable_Object((1,3,6,1,4,1,3181,10,6,2,42,103))
if mibBuilder.loadTexts:mstpBridgeStatusTable.setStatus(_A)
_MstpBridgeStatusEntry_Object=MibTableRow
mstpBridgeStatusEntry=_MstpBridgeStatusEntry_Object((1,3,6,1,4,1,3181,10,6,2,42,103,1))
mstpBridgeStatusEntry.setIndexNames((0,_F,_b))
if mibBuilder.loadTexts:mstpBridgeStatusEntry.setStatus(_A)
class _MstpBridgeStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,62))
_MstpBridgeStatusIndex_Type.__name__=_B
_MstpBridgeStatusIndex_Object=MibTableColumn
mstpBridgeStatusIndex=_MstpBridgeStatusIndex_Object((1,3,6,1,4,1,3181,10,6,2,42,103,1,1),_MstpBridgeStatusIndex_Type())
mstpBridgeStatusIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:mstpBridgeStatusIndex.setStatus(_A)
class _MstpBridgeStatusMstpId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MstpBridgeStatusMstpId_Type.__name__=_B
_MstpBridgeStatusMstpId_Object=MibTableColumn
mstpBridgeStatusMstpId=_MstpBridgeStatusMstpId_Object((1,3,6,1,4,1,3181,10,6,2,42,103,1,2),_MstpBridgeStatusMstpId_Type())
mstpBridgeStatusMstpId.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpBridgeStatusMstpId.setStatus(_A)
_MstpBridgeStatusBridgePriority_Type=Unsigned32
_MstpBridgeStatusBridgePriority_Object=MibTableColumn
mstpBridgeStatusBridgePriority=_MstpBridgeStatusBridgePriority_Object((1,3,6,1,4,1,3181,10,6,2,42,103,1,3),_MstpBridgeStatusBridgePriority_Type())
mstpBridgeStatusBridgePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpBridgeStatusBridgePriority.setStatus(_A)
class _MstpBridgeStatusRootPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MstpBridgeStatusRootPort_Type.__name__=_B
_MstpBridgeStatusRootPort_Object=MibTableColumn
mstpBridgeStatusRootPort=_MstpBridgeStatusRootPort_Object((1,3,6,1,4,1,3181,10,6,2,42,103,1,4),_MstpBridgeStatusRootPort_Type())
mstpBridgeStatusRootPort.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpBridgeStatusRootPort.setStatus(_A)
_MstpBridgeStatusRootCost_Type=Unsigned32
_MstpBridgeStatusRootCost_Object=MibTableColumn
mstpBridgeStatusRootCost=_MstpBridgeStatusRootCost_Object((1,3,6,1,4,1,3181,10,6,2,42,103,1,5),_MstpBridgeStatusRootCost_Type())
mstpBridgeStatusRootCost.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpBridgeStatusRootCost.setStatus(_A)
class _MstpBridgeStatusMaxHops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MstpBridgeStatusMaxHops_Type.__name__=_B
_MstpBridgeStatusMaxHops_Object=MibTableColumn
mstpBridgeStatusMaxHops=_MstpBridgeStatusMaxHops_Object((1,3,6,1,4,1,3181,10,6,2,42,103,1,6),_MstpBridgeStatusMaxHops_Type())
mstpBridgeStatusMaxHops.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpBridgeStatusMaxHops.setStatus(_A)
_MstpBridgeStatusRegionalRootId_Type=DisplayString
_MstpBridgeStatusRegionalRootId_Object=MibTableColumn
mstpBridgeStatusRegionalRootId=_MstpBridgeStatusRegionalRootId_Object((1,3,6,1,4,1,3181,10,6,2,42,103,1,7),_MstpBridgeStatusRegionalRootId_Type())
mstpBridgeStatusRegionalRootId.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpBridgeStatusRegionalRootId.setStatus(_A)
_MstpBridgeStatusRegionalRootPriority_Type=Unsigned32
_MstpBridgeStatusRegionalRootPriority_Object=MibTableColumn
mstpBridgeStatusRegionalRootPriority=_MstpBridgeStatusRegionalRootPriority_Object((1,3,6,1,4,1,3181,10,6,2,42,103,1,8),_MstpBridgeStatusRegionalRootPriority_Type())
mstpBridgeStatusRegionalRootPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpBridgeStatusRegionalRootPriority.setStatus(_A)
_MstpBridgeStatusRegionalRootMac_Type=MacAddress
_MstpBridgeStatusRegionalRootMac_Object=MibTableColumn
mstpBridgeStatusRegionalRootMac=_MstpBridgeStatusRegionalRootMac_Object((1,3,6,1,4,1,3181,10,6,2,42,103,1,9),_MstpBridgeStatusRegionalRootMac_Type())
mstpBridgeStatusRegionalRootMac.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpBridgeStatusRegionalRootMac.setStatus(_A)
class _MstpBridgeStatusTopologyChanges_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MstpBridgeStatusTopologyChanges_Type.__name__=_B
_MstpBridgeStatusTopologyChanges_Object=MibTableColumn
mstpBridgeStatusTopologyChanges=_MstpBridgeStatusTopologyChanges_Object((1,3,6,1,4,1,3181,10,6,2,42,103,1,10),_MstpBridgeStatusTopologyChanges_Type())
mstpBridgeStatusTopologyChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpBridgeStatusTopologyChanges.setStatus(_A)
_MstpBridgeStatusLastTopologyChange_Type=Counter32
_MstpBridgeStatusLastTopologyChange_Object=MibTableColumn
mstpBridgeStatusLastTopologyChange=_MstpBridgeStatusLastTopologyChange_Object((1,3,6,1,4,1,3181,10,6,2,42,103,1,11),_MstpBridgeStatusLastTopologyChange_Type())
mstpBridgeStatusLastTopologyChange.setMaxAccess(_C)
if mibBuilder.loadTexts:mstpBridgeStatusLastTopologyChange.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'protocol':protocol,'stp':stp,'bridgeConfigTable':bridgeConfigTable,'bridgeConfigEntry':bridgeConfigEntry,_L:bridgeConfigIndex,'bridgeConfigMode':bridgeConfigMode,'bridgeConfigPriority':bridgeConfigPriority,'bridgeConfigHelloTime':bridgeConfigHelloTime,'bridgeConfigMaxAge':bridgeConfigMaxAge,'bridgeConfigForwardDelay':bridgeConfigForwardDelay,'bridgeConfigTxHoldCount':bridgeConfigTxHoldCount,'bridgeConfigIeeePathCostModel':bridgeConfigIeeePathCostModel,'bridgeConfigMstpRegionName':bridgeConfigMstpRegionName,'bridgeConfigMstpRevisionLevel':bridgeConfigMstpRevisionLevel,'bridgeConfigMstpMaxHops':bridgeConfigMstpMaxHops,'bridgeConfigMstpStpAgingTime':bridgeConfigMstpStpAgingTime,'portConfigTable':portConfigTable,'portConfigEntry':portConfigEntry,_M:portConfigPortIndex,'portConfigEnable':portConfigEnable,'portConfigPriority':portConfigPriority,'portConfigAdminP2pPort':portConfigAdminP2pPort,'portConfigAdminEdgePort':portConfigAdminEdgePort,'portConfigAdminPathCost':portConfigAdminPathCost,'portConfigProtocolMigration':portConfigProtocolMigration,'portConfigBridgeAssurance':portConfigBridgeAssurance,'portConfigMstpDefaultPriority':portConfigMstpDefaultPriority,'portConfigMstpPortPriority':portConfigMstpPortPriority,'portConfigMstpDefaultAdminPathCost':portConfigMstpDefaultAdminPathCost,'portConfigMstpPortAdminPathCost':portConfigMstpPortAdminPathCost,'portConfigBpduGuard':portConfigBpduGuard,'portConfigBpduReceiveOnly':portConfigBpduReceiveOnly,'portConfigRestrictTcn':portConfigRestrictTcn,'portConfigRestrictRoot':portConfigRestrictRoot,'mstpGroupTable':mstpGroupTable,'mstpGroupEntry':mstpGroupEntry,_N:mstpGroupIndex,'mstpGroupMstpId':mstpGroupMstpId,'mstpGroupBridgePriority':mstpGroupBridgePriority,'bridgeStatusTable':bridgeStatusTable,'bridgeStatusEntry':bridgeStatusEntry,_O:bridgeStatusIndex,'bridgeStatusStpProtocol':bridgeStatusStpProtocol,'bridgeStatusHelloTime':bridgeStatusHelloTime,'bridgeStatusMaxAge':bridgeStatusMaxAge,'bridgeStatusHoldTime':bridgeStatusHoldTime,'bridgeStatusForwardDelay':bridgeStatusForwardDelay,'bridgeStatusRootPort':bridgeStatusRootPort,'bridgeStatusRootCost':bridgeStatusRootCost,'bridgeStatusTopologyChanges':bridgeStatusTopologyChanges,'bridgeStatusLastTopologyChange':bridgeStatusLastTopologyChange,'bridgeStatusMstpRegionName':bridgeStatusMstpRegionName,'bridgeStatusMstiRevisionLevel':bridgeStatusMstiRevisionLevel,'bridgeStatusCistInternalRootPathCost':bridgeStatusCistInternalRootPathCost,'bridgeStatusCistRegionalRootId':bridgeStatusCistRegionalRootId,'bridgeStatusCistRegionalRootPriority':bridgeStatusCistRegionalRootPriority,'bridgeStatusCistRegionalRootMac':bridgeStatusCistRegionalRootMac,'bridgeStatusMaxHops':bridgeStatusMaxHops,'bridgeStatusMstpStpAgingTime':bridgeStatusMstpStpAgingTime,'portStatusTable':portStatusTable,'portStatusEntry':portStatusEntry,_P:portStatusPortIndex,'portStatusPort':portStatusPort,'portStatusState':portStatusState,'portStatusLocalPortCost':portStatusLocalPortCost,'portStatusDesignatedPortId':portStatusDesignatedPortId,'portStatusDesignatedPort':portStatusDesignatedPort,'portStatusDesignatedPortPriority':portStatusDesignatedPortPriority,'portStatusDesignatedCost':portStatusDesignatedCost,'portStatusDesignatedRootId':portStatusDesignatedRootId,'portStatusDesignatedRootMac':portStatusDesignatedRootMac,'portStatusDesignatedRootPriority':portStatusDesignatedRootPriority,'portStatusDesignatedBridgeId':portStatusDesignatedBridgeId,'portStatusDesignatedBridgeMac':portStatusDesignatedBridgeMac,'portStatusDesignatedBridgePriority':portStatusDesignatedBridgePriority,'portStatusForwardTransition':portStatusForwardTransition,'portStatusOperEdgePort':portStatusOperEdgePort,'portStatusOperP2pPort':portStatusOperP2pPort,'portStatusRole':portStatusRole,'portStatusInconsistentBridge':portStatusInconsistentBridge,'mstpStatusTableTable':mstpStatusTableTable,'mstpStatusTableEntry':mstpStatusTableEntry,_a:mstpStatusTableIndex,'mstpStatusTableMstpId':mstpStatusTableMstpId,'mstpStatusTablePort':mstpStatusTablePort,'mstpStatusTableState':mstpStatusTableState,'mstpStatusTablePortPriority':mstpStatusTablePortPriority,'mstpStatusTableInternalAdminPathCost':mstpStatusTableInternalAdminPathCost,'mstpStatusTableForwardTransition':mstpStatusTableForwardTransition,'mstpStatusTableRole':mstpStatusTableRole,'mstpBridgeStatusTable':mstpBridgeStatusTable,'mstpBridgeStatusEntry':mstpBridgeStatusEntry,_b:mstpBridgeStatusIndex,'mstpBridgeStatusMstpId':mstpBridgeStatusMstpId,'mstpBridgeStatusBridgePriority':mstpBridgeStatusBridgePriority,'mstpBridgeStatusRootPort':mstpBridgeStatusRootPort,'mstpBridgeStatusRootCost':mstpBridgeStatusRootCost,'mstpBridgeStatusMaxHops':mstpBridgeStatusMaxHops,'mstpBridgeStatusRegionalRootId':mstpBridgeStatusRegionalRootId,'mstpBridgeStatusRegionalRootPriority':mstpBridgeStatusRegionalRootPriority,'mstpBridgeStatusRegionalRootMac':mstpBridgeStatusRegionalRootMac,'mstpBridgeStatusTopologyChanges':mstpBridgeStatusTopologyChanges,'mstpBridgeStatusLastTopologyChange':mstpBridgeStatusLastTopologyChange})