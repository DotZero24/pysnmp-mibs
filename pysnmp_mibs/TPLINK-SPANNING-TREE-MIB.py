_U='tpMstpInstancePortConfigId'
_T='tpMstpInstanceId'
_S='forwarding'
_R='learning'
_Q='blocking'
_P='master'
_O='designated'
_N='backup'
_M='alternate'
_L='TPLINK-SPANNING-TREE-MIB'
_K='disabled'
_J='ifIndex'
_I='IF-MIB'
_H='na'
_G='disable'
_F='enable'
_E='OctetString'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_I,_J)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkSpanningTreeMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,21))
if mibBuilder.loadTexts:tplinkSpanningTreeMIB.setRevisions(('2012-11-21 09:30',))
_TplinkSpanningTreeMIBObjects_ObjectIdentity=ObjectIdentity
tplinkSpanningTreeMIBObjects=_TplinkSpanningTreeMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,21,1))
_TpStpBasicCfg_ObjectIdentity=ObjectIdentity
tpStpBasicCfg=_TpStpBasicCfg_ObjectIdentity((1,3,6,1,4,1,11863,6,21,1,1))
_TpStpBasicGlobalConfig_ObjectIdentity=ObjectIdentity
tpStpBasicGlobalConfig=_TpStpBasicGlobalConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,21,1,1,1))
class _TpStpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_F,1)))
_TpStpEnable_Type.__name__=_B
_TpStpEnable_Object=MibScalar
tpStpEnable=_TpStpEnable_Object((1,3,6,1,4,1,11863,6,21,1,1,1,1),_TpStpEnable_Type())
tpStpEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStpEnable.setStatus(_A)
class _TpRstpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_F,1)))
_TpRstpEnable_Type.__name__=_B
_TpRstpEnable_Object=MibScalar
tpRstpEnable=_TpRstpEnable_Object((1,3,6,1,4,1,11863,6,21,1,1,1,2),_TpRstpEnable_Type())
tpRstpEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpRstpEnable.setStatus(_A)
class _TpMstpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_F,1)))
_TpMstpEnable_Type.__name__=_B
_TpMstpEnable_Object=MibScalar
tpMstpEnable=_TpMstpEnable_Object((1,3,6,1,4,1,11863,6,21,1,1,1,3),_TpMstpEnable_Type())
tpMstpEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMstpEnable.setStatus(_A)
_TpStpBasicParamConfig_ObjectIdentity=ObjectIdentity
tpStpBasicParamConfig=_TpStpBasicParamConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,21,1,1,2))
class _TpStpCistPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_TpStpCistPriority_Type.__name__=_B
_TpStpCistPriority_Object=MibScalar
tpStpCistPriority=_TpStpCistPriority_Object((1,3,6,1,4,1,11863,6,21,1,1,2,1),_TpStpCistPriority_Type())
tpStpCistPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStpCistPriority.setStatus(_A)
class _TpStpHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_TpStpHelloTime_Type.__name__=_B
_TpStpHelloTime_Object=MibScalar
tpStpHelloTime=_TpStpHelloTime_Object((1,3,6,1,4,1,11863,6,21,1,1,2,2),_TpStpHelloTime_Type())
tpStpHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStpHelloTime.setStatus(_A)
class _TpStpAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_TpStpAgingTime_Type.__name__=_B
_TpStpAgingTime_Object=MibScalar
tpStpAgingTime=_TpStpAgingTime_Object((1,3,6,1,4,1,11863,6,21,1,1,2,3),_TpStpAgingTime_Type())
tpStpAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStpAgingTime.setStatus(_A)
class _TpStpForwardDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_TpStpForwardDelay_Type.__name__=_B
_TpStpForwardDelay_Object=MibScalar
tpStpForwardDelay=_TpStpForwardDelay_Object((1,3,6,1,4,1,11863,6,21,1,1,2,4),_TpStpForwardDelay_Type())
tpStpForwardDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStpForwardDelay.setStatus(_A)
class _TpStpHoldCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_TpStpHoldCount_Type.__name__=_B
_TpStpHoldCount_Object=MibScalar
tpStpHoldCount=_TpStpHoldCount_Object((1,3,6,1,4,1,11863,6,21,1,1,2,5),_TpStpHoldCount_Type())
tpStpHoldCount.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStpHoldCount.setStatus(_A)
class _TpStpMaxHops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,40))
_TpStpMaxHops_Type.__name__=_B
_TpStpMaxHops_Object=MibScalar
tpStpMaxHops=_TpStpMaxHops_Object((1,3,6,1,4,1,11863,6,21,1,1,2,6),_TpStpMaxHops_Type())
tpStpMaxHops.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStpMaxHops.setStatus(_A)
_TpStpInfo_ObjectIdentity=ObjectIdentity
tpStpInfo=_TpStpInfo_ObjectIdentity((1,3,6,1,4,1,11863,6,21,1,1,3))
class _TpStpEnableStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_F,1)))
_TpStpEnableStatus_Type.__name__=_B
_TpStpEnableStatus_Object=MibScalar
tpStpEnableStatus=_TpStpEnableStatus_Object((1,3,6,1,4,1,11863,6,21,1,1,3,1),_TpStpEnableStatus_Type())
tpStpEnableStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tpStpEnableStatus.setStatus(_A)
class _TpStpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('stp',1),('rstp',2),('mstp',3)))
_TpStpMode_Type.__name__=_B
_TpStpMode_Object=MibScalar
tpStpMode=_TpStpMode_Object((1,3,6,1,4,1,11863,6,21,1,1,3,2),_TpStpMode_Type())
tpStpMode.setMaxAccess(_D)
if mibBuilder.loadTexts:tpStpMode.setStatus(_A)
class _TpStpLocalBridge_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpStpLocalBridge_Type.__name__=_E
_TpStpLocalBridge_Object=MibScalar
tpStpLocalBridge=_TpStpLocalBridge_Object((1,3,6,1,4,1,11863,6,21,1,1,3,3),_TpStpLocalBridge_Type())
tpStpLocalBridge.setMaxAccess(_D)
if mibBuilder.loadTexts:tpStpLocalBridge.setStatus(_A)
class _TpStpCISTRoot_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpStpCISTRoot_Type.__name__=_E
_TpStpCISTRoot_Object=MibScalar
tpStpCISTRoot=_TpStpCISTRoot_Object((1,3,6,1,4,1,11863,6,21,1,1,3,4),_TpStpCISTRoot_Type())
tpStpCISTRoot.setMaxAccess(_D)
if mibBuilder.loadTexts:tpStpCISTRoot.setStatus(_A)
class _TpStpExPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000000))
_TpStpExPathCost_Type.__name__=_B
_TpStpExPathCost_Object=MibScalar
tpStpExPathCost=_TpStpExPathCost_Object((1,3,6,1,4,1,11863,6,21,1,1,3,5),_TpStpExPathCost_Type())
tpStpExPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:tpStpExPathCost.setStatus(_A)
class _TpStpRegionRoot_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpStpRegionRoot_Type.__name__=_E
_TpStpRegionRoot_Object=MibScalar
tpStpRegionRoot=_TpStpRegionRoot_Object((1,3,6,1,4,1,11863,6,21,1,1,3,6),_TpStpRegionRoot_Type())
tpStpRegionRoot.setMaxAccess(_D)
if mibBuilder.loadTexts:tpStpRegionRoot.setStatus(_A)
class _TpStpInPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000000))
_TpStpInPathCost_Type.__name__=_B
_TpStpInPathCost_Object=MibScalar
tpStpInPathCost=_TpStpInPathCost_Object((1,3,6,1,4,1,11863,6,21,1,1,3,7),_TpStpInPathCost_Type())
tpStpInPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:tpStpInPathCost.setStatus(_A)
class _TpStpDesignatedBridge_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpStpDesignatedBridge_Type.__name__=_E
_TpStpDesignatedBridge_Object=MibScalar
tpStpDesignatedBridge=_TpStpDesignatedBridge_Object((1,3,6,1,4,1,11863,6,21,1,1,3,8),_TpStpDesignatedBridge_Type())
tpStpDesignatedBridge.setMaxAccess(_D)
if mibBuilder.loadTexts:tpStpDesignatedBridge.setStatus(_A)
_TpStpRootPort_Type=Integer32
_TpStpRootPort_Object=MibScalar
tpStpRootPort=_TpStpRootPort_Object((1,3,6,1,4,1,11863,6,21,1,1,3,9),_TpStpRootPort_Type())
tpStpRootPort.setMaxAccess(_D)
if mibBuilder.loadTexts:tpStpRootPort.setStatus(_A)
class _TpStpLastTopologyChangeTime_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpStpLastTopologyChangeTime_Type.__name__=_E
_TpStpLastTopologyChangeTime_Object=MibScalar
tpStpLastTopologyChangeTime=_TpStpLastTopologyChangeTime_Object((1,3,6,1,4,1,11863,6,21,1,1,3,10),_TpStpLastTopologyChangeTime_Type())
tpStpLastTopologyChangeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:tpStpLastTopologyChangeTime.setStatus(_A)
_TpStpTopologyChangeCounter_Type=Integer32
_TpStpTopologyChangeCounter_Object=MibScalar
tpStpTopologyChangeCounter=_TpStpTopologyChangeCounter_Object((1,3,6,1,4,1,11863,6,21,1,1,3,11),_TpStpTopologyChangeCounter_Type())
tpStpTopologyChangeCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:tpStpTopologyChangeCounter.setStatus(_A)
_TpStpPortCfg_ObjectIdentity=ObjectIdentity
tpStpPortCfg=_TpStpPortCfg_ObjectIdentity((1,3,6,1,4,1,11863,6,21,1,2))
_TpStpPortConfigTable_Object=MibTable
tpStpPortConfigTable=_TpStpPortConfigTable_Object((1,3,6,1,4,1,11863,6,21,1,2,1))
if mibBuilder.loadTexts:tpStpPortConfigTable.setStatus(_A)
_TpStpPortConfigEntry_Object=MibTableRow
tpStpPortConfigEntry=_TpStpPortConfigEntry_Object((1,3,6,1,4,1,11863,6,21,1,2,1,1))
tpStpPortConfigEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:tpStpPortConfigEntry.setStatus(_A)
class _TpStpPortNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpStpPortNumber_Type.__name__=_E
_TpStpPortNumber_Object=MibTableColumn
tpStpPortNumber=_TpStpPortNumber_Object((1,3,6,1,4,1,11863,6,21,1,2,1,1,1),_TpStpPortNumber_Type())
tpStpPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:tpStpPortNumber.setStatus(_A)
class _TpStpPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),(_F,1),('errPort',2)))
_TpStpPortEnable_Type.__name__=_B
_TpStpPortEnable_Object=MibTableColumn
tpStpPortEnable=_TpStpPortEnable_Object((1,3,6,1,4,1,11863,6,21,1,2,1,1,2),_TpStpPortEnable_Type())
tpStpPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStpPortEnable.setStatus(_A)
class _TpStpPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_TpStpPortPriority_Type.__name__=_B
_TpStpPortPriority_Object=MibTableColumn
tpStpPortPriority=_TpStpPortPriority_Object((1,3,6,1,4,1,11863,6,21,1,2,1,1,3),_TpStpPortPriority_Type())
tpStpPortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStpPortPriority.setStatus(_A)
class _TpStpPortExPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000000))
_TpStpPortExPathCost_Type.__name__=_B
_TpStpPortExPathCost_Object=MibTableColumn
tpStpPortExPathCost=_TpStpPortExPathCost_Object((1,3,6,1,4,1,11863,6,21,1,2,1,1,4),_TpStpPortExPathCost_Type())
tpStpPortExPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStpPortExPathCost.setStatus(_A)
class _TpStpPortInPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000000))
_TpStpPortInPathCost_Type.__name__=_B
_TpStpPortInPathCost_Object=MibTableColumn
tpStpPortInPathCost=_TpStpPortInPathCost_Object((1,3,6,1,4,1,11863,6,21,1,2,1,1,5),_TpStpPortInPathCost_Type())
tpStpPortInPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStpPortInPathCost.setStatus(_A)
class _TpStpEdgePortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_F,1)))
_TpStpEdgePortStatus_Type.__name__=_B
_TpStpEdgePortStatus_Object=MibTableColumn
tpStpEdgePortStatus=_TpStpEdgePortStatus_Object((1,3,6,1,4,1,11863,6,21,1,2,1,1,6),_TpStpEdgePortStatus_Type())
tpStpEdgePortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStpEdgePortStatus.setStatus(_A)
class _TpStpPointToPointStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('auto',0),('force-enable',1),('force-disable',2)))
_TpStpPointToPointStatus_Type.__name__=_B
_TpStpPointToPointStatus_Object=MibTableColumn
tpStpPointToPointStatus=_TpStpPointToPointStatus_Object((1,3,6,1,4,1,11863,6,21,1,2,1,1,7),_TpStpPointToPointStatus_Type())
tpStpPointToPointStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStpPointToPointStatus.setStatus(_A)
class _TpStpPortMCheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unChange',0),(_F,1)))
_TpStpPortMCheck_Type.__name__=_B
_TpStpPortMCheck_Object=MibTableColumn
tpStpPortMCheck=_TpStpPortMCheck_Object((1,3,6,1,4,1,11863,6,21,1,2,1,1,8),_TpStpPortMCheck_Type())
tpStpPortMCheck.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStpPortMCheck.setStatus(_A)
class _TpStpPortStpVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_H,0),('stp',1),('rstp',2),('mstp',3)))
_TpStpPortStpVersion_Type.__name__=_B
_TpStpPortStpVersion_Object=MibTableColumn
tpStpPortStpVersion=_TpStpPortStpVersion_Object((1,3,6,1,4,1,11863,6,21,1,2,1,1,9),_TpStpPortStpVersion_Type())
tpStpPortStpVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:tpStpPortStpVersion.setStatus(_A)
class _TpStpPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_H,0),(_K,1),(_M,2),(_N,3),(_O,4),('root',5),(_P,6)))
_TpStpPortRole_Type.__name__=_B
_TpStpPortRole_Object=MibTableColumn
tpStpPortRole=_TpStpPortRole_Object((1,3,6,1,4,1,11863,6,21,1,2,1,1,10),_TpStpPortRole_Type())
tpStpPortRole.setMaxAccess(_D)
if mibBuilder.loadTexts:tpStpPortRole.setStatus(_A)
class _TpStpPortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_H,0),('disconnected',1),(_Q,2),(_R,3),(_S,4)))
_TpStpPortStatus_Type.__name__=_B
_TpStpPortStatus_Object=MibTableColumn
tpStpPortStatus=_TpStpPortStatus_Object((1,3,6,1,4,1,11863,6,21,1,2,1,1,11),_TpStpPortStatus_Type())
tpStpPortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tpStpPortStatus.setStatus(_A)
class _TpStpPortLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpStpPortLag_Type.__name__=_E
_TpStpPortLag_Object=MibTableColumn
tpStpPortLag=_TpStpPortLag_Object((1,3,6,1,4,1,11863,6,21,1,2,1,1,12),_TpStpPortLag_Type())
tpStpPortLag.setMaxAccess(_D)
if mibBuilder.loadTexts:tpStpPortLag.setStatus(_A)
_TpStpInstanceCfg_ObjectIdentity=ObjectIdentity
tpStpInstanceCfg=_TpStpInstanceCfg_ObjectIdentity((1,3,6,1,4,1,11863,6,21,1,3))
_TpMstpRegionConfig_ObjectIdentity=ObjectIdentity
tpMstpRegionConfig=_TpMstpRegionConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,21,1,3,1))
class _TpMstpRegionName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TpMstpRegionName_Type.__name__=_E
_TpMstpRegionName_Object=MibScalar
tpMstpRegionName=_TpMstpRegionName_Object((1,3,6,1,4,1,11863,6,21,1,3,1,1),_TpMstpRegionName_Type())
tpMstpRegionName.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMstpRegionName.setStatus(_A)
class _TpMstpRevision_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TpMstpRevision_Type.__name__=_B
_TpMstpRevision_Object=MibScalar
tpMstpRevision=_TpMstpRevision_Object((1,3,6,1,4,1,11863,6,21,1,3,1,2),_TpMstpRevision_Type())
tpMstpRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMstpRevision.setStatus(_A)
_TpMstpInstanceConfigTable_Object=MibTable
tpMstpInstanceConfigTable=_TpMstpInstanceConfigTable_Object((1,3,6,1,4,1,11863,6,21,1,3,2))
if mibBuilder.loadTexts:tpMstpInstanceConfigTable.setStatus(_A)
_TpMstpInstanceConfigEntry_Object=MibTableRow
tpMstpInstanceConfigEntry=_TpMstpInstanceConfigEntry_Object((1,3,6,1,4,1,11863,6,21,1,3,2,1))
tpMstpInstanceConfigEntry.setIndexNames((0,_L,_T))
if mibBuilder.loadTexts:tpMstpInstanceConfigEntry.setStatus(_A)
_TpMstpInstanceId_Type=Integer32
_TpMstpInstanceId_Object=MibTableColumn
tpMstpInstanceId=_TpMstpInstanceId_Object((1,3,6,1,4,1,11863,6,21,1,3,2,1,1),_TpMstpInstanceId_Type())
tpMstpInstanceId.setMaxAccess(_D)
if mibBuilder.loadTexts:tpMstpInstanceId.setStatus(_A)
class _TpMstpInstanceEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_F,1)))
_TpMstpInstanceEnable_Type.__name__=_B
_TpMstpInstanceEnable_Object=MibTableColumn
tpMstpInstanceEnable=_TpMstpInstanceEnable_Object((1,3,6,1,4,1,11863,6,21,1,3,2,1,2),_TpMstpInstanceEnable_Type())
tpMstpInstanceEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:tpMstpInstanceEnable.setStatus(_A)
class _TpMstpInstancePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_TpMstpInstancePriority_Type.__name__=_B
_TpMstpInstancePriority_Object=MibTableColumn
tpMstpInstancePriority=_TpMstpInstancePriority_Object((1,3,6,1,4,1,11863,6,21,1,3,2,1,3),_TpMstpInstancePriority_Type())
tpMstpInstancePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMstpInstancePriority.setStatus(_A)
class _TpMstpInstanceVlanId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_TpMstpInstanceVlanId_Type.__name__=_E
_TpMstpInstanceVlanId_Object=MibTableColumn
tpMstpInstanceVlanId=_TpMstpInstanceVlanId_Object((1,3,6,1,4,1,11863,6,21,1,3,2,1,4),_TpMstpInstanceVlanId_Type())
tpMstpInstanceVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMstpInstanceVlanId.setStatus(_A)
class _TpMstpClearInstanceVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('clear',1))
_TpMstpClearInstanceVlanId_Type.__name__=_B
_TpMstpClearInstanceVlanId_Object=MibTableColumn
tpMstpClearInstanceVlanId=_TpMstpClearInstanceVlanId_Object((1,3,6,1,4,1,11863,6,21,1,3,2,1,5),_TpMstpClearInstanceVlanId_Type())
tpMstpClearInstanceVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMstpClearInstanceVlanId.setStatus(_A)
_TpMstpInstancePortConfigTable_Object=MibTable
tpMstpInstancePortConfigTable=_TpMstpInstancePortConfigTable_Object((1,3,6,1,4,1,11863,6,21,1,3,3))
if mibBuilder.loadTexts:tpMstpInstancePortConfigTable.setStatus(_A)
_TpMstpInstancePortConfigEntry_Object=MibTableRow
tpMstpInstancePortConfigEntry=_TpMstpInstancePortConfigEntry_Object((1,3,6,1,4,1,11863,6,21,1,3,3,1))
tpMstpInstancePortConfigEntry.setIndexNames((0,_L,_U),(0,_I,_J))
if mibBuilder.loadTexts:tpMstpInstancePortConfigEntry.setStatus(_A)
_TpMstpInstancePortConfigId_Type=Integer32
_TpMstpInstancePortConfigId_Object=MibTableColumn
tpMstpInstancePortConfigId=_TpMstpInstancePortConfigId_Object((1,3,6,1,4,1,11863,6,21,1,3,3,1,1),_TpMstpInstancePortConfigId_Type())
tpMstpInstancePortConfigId.setMaxAccess(_D)
if mibBuilder.loadTexts:tpMstpInstancePortConfigId.setStatus(_A)
class _TpMstpInstancePortNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpMstpInstancePortNumber_Type.__name__=_E
_TpMstpInstancePortNumber_Object=MibTableColumn
tpMstpInstancePortNumber=_TpMstpInstancePortNumber_Object((1,3,6,1,4,1,11863,6,21,1,3,3,1,2),_TpMstpInstancePortNumber_Type())
tpMstpInstancePortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:tpMstpInstancePortNumber.setStatus(_A)
class _TpMstpInstancePortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_TpMstpInstancePortPriority_Type.__name__=_B
_TpMstpInstancePortPriority_Object=MibTableColumn
tpMstpInstancePortPriority=_TpMstpInstancePortPriority_Object((1,3,6,1,4,1,11863,6,21,1,3,3,1,3),_TpMstpInstancePortPriority_Type())
tpMstpInstancePortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMstpInstancePortPriority.setStatus(_A)
class _TpMstpInstancePortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2000000))
_TpMstpInstancePortPathCost_Type.__name__=_B
_TpMstpInstancePortPathCost_Object=MibTableColumn
tpMstpInstancePortPathCost=_TpMstpInstancePortPathCost_Object((1,3,6,1,4,1,11863,6,21,1,3,3,1,4),_TpMstpInstancePortPathCost_Type())
tpMstpInstancePortPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:tpMstpInstancePortPathCost.setStatus(_A)
class _TpMstpInstancePortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_H,0),(_K,1),(_M,2),(_N,3),(_O,4),('root',5),(_P,6)))
_TpMstpInstancePortRole_Type.__name__=_B
_TpMstpInstancePortRole_Object=MibTableColumn
tpMstpInstancePortRole=_TpMstpInstancePortRole_Object((1,3,6,1,4,1,11863,6,21,1,3,3,1,5),_TpMstpInstancePortRole_Type())
tpMstpInstancePortRole.setMaxAccess(_D)
if mibBuilder.loadTexts:tpMstpInstancePortRole.setStatus(_A)
class _TpMstpInstancePortStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_H,0),(_K,1),(_Q,2),(_R,3),(_S,4)))
_TpMstpInstancePortStatus_Type.__name__=_B
_TpMstpInstancePortStatus_Object=MibTableColumn
tpMstpInstancePortStatus=_TpMstpInstancePortStatus_Object((1,3,6,1,4,1,11863,6,21,1,3,3,1,6),_TpMstpInstancePortStatus_Type())
tpMstpInstancePortStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tpMstpInstancePortStatus.setStatus(_A)
class _TpMstpInstancePortLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpMstpInstancePortLag_Type.__name__=_E
_TpMstpInstancePortLag_Object=MibTableColumn
tpMstpInstancePortLag=_TpMstpInstancePortLag_Object((1,3,6,1,4,1,11863,6,21,1,3,3,1,7),_TpMstpInstancePortLag_Type())
tpMstpInstancePortLag.setMaxAccess(_D)
if mibBuilder.loadTexts:tpMstpInstancePortLag.setStatus(_A)
_TpStpSecurityCfg_ObjectIdentity=ObjectIdentity
tpStpSecurityCfg=_TpStpSecurityCfg_ObjectIdentity((1,3,6,1,4,1,11863,6,21,1,4))
_TpStpPortDefendTable_Object=MibTable
tpStpPortDefendTable=_TpStpPortDefendTable_Object((1,3,6,1,4,1,11863,6,21,1,4,1))
if mibBuilder.loadTexts:tpStpPortDefendTable.setStatus(_A)
_TpStpPortDefendEntry_Object=MibTableRow
tpStpPortDefendEntry=_TpStpPortDefendEntry_Object((1,3,6,1,4,1,11863,6,21,1,4,1,1))
tpStpPortDefendEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:tpStpPortDefendEntry.setStatus(_A)
class _TpStpDefendPortNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpStpDefendPortNumber_Type.__name__=_E
_TpStpDefendPortNumber_Object=MibTableColumn
tpStpDefendPortNumber=_TpStpDefendPortNumber_Object((1,3,6,1,4,1,11863,6,21,1,4,1,1,1),_TpStpDefendPortNumber_Type())
tpStpDefendPortNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:tpStpDefendPortNumber.setStatus(_A)
class _TpStpLoopDefendEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_F,1)))
_TpStpLoopDefendEnable_Type.__name__=_B
_TpStpLoopDefendEnable_Object=MibTableColumn
tpStpLoopDefendEnable=_TpStpLoopDefendEnable_Object((1,3,6,1,4,1,11863,6,21,1,4,1,1,2),_TpStpLoopDefendEnable_Type())
tpStpLoopDefendEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStpLoopDefendEnable.setStatus(_A)
class _TpStpRootBridgeDefendEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_F,1)))
_TpStpRootBridgeDefendEnable_Type.__name__=_B
_TpStpRootBridgeDefendEnable_Object=MibTableColumn
tpStpRootBridgeDefendEnable=_TpStpRootBridgeDefendEnable_Object((1,3,6,1,4,1,11863,6,21,1,4,1,1,3),_TpStpRootBridgeDefendEnable_Type())
tpStpRootBridgeDefendEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStpRootBridgeDefendEnable.setStatus(_A)
class _TpStpTcDefendEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_F,1)))
_TpStpTcDefendEnable_Type.__name__=_B
_TpStpTcDefendEnable_Object=MibTableColumn
tpStpTcDefendEnable=_TpStpTcDefendEnable_Object((1,3,6,1,4,1,11863,6,21,1,4,1,1,4),_TpStpTcDefendEnable_Type())
tpStpTcDefendEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStpTcDefendEnable.setStatus(_A)
class _TpStpBPDUDefendEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_F,1)))
_TpStpBPDUDefendEnable_Type.__name__=_B
_TpStpBPDUDefendEnable_Object=MibTableColumn
tpStpBPDUDefendEnable=_TpStpBPDUDefendEnable_Object((1,3,6,1,4,1,11863,6,21,1,4,1,1,5),_TpStpBPDUDefendEnable_Type())
tpStpBPDUDefendEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStpBPDUDefendEnable.setStatus(_A)
class _TpStpBPDUHoldEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_F,1)))
_TpStpBPDUHoldEnable_Type.__name__=_B
_TpStpBPDUHoldEnable_Object=MibTableColumn
tpStpBPDUHoldEnable=_TpStpBPDUHoldEnable_Object((1,3,6,1,4,1,11863,6,21,1,4,1,1,6),_TpStpBPDUHoldEnable_Type())
tpStpBPDUHoldEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStpBPDUHoldEnable.setStatus(_A)
class _TpStpBPDUFloodEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_F,1)))
_TpStpBPDUFloodEnable_Type.__name__=_B
_TpStpBPDUFloodEnable_Object=MibTableColumn
tpStpBPDUFloodEnable=_TpStpBPDUFloodEnable_Object((1,3,6,1,4,1,11863,6,21,1,4,1,1,7),_TpStpBPDUFloodEnable_Type())
tpStpBPDUFloodEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpStpBPDUFloodEnable.setStatus(_A)
class _TpStpDefendPortLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TpStpDefendPortLag_Type.__name__=_E
_TpStpDefendPortLag_Object=MibTableColumn
tpStpDefendPortLag=_TpStpDefendPortLag_Object((1,3,6,1,4,1,11863,6,21,1,4,1,1,8),_TpStpDefendPortLag_Type())
tpStpDefendPortLag.setMaxAccess(_D)
if mibBuilder.loadTexts:tpStpDefendPortLag.setStatus(_A)
_TplinkSpanningTreeNotifications_ObjectIdentity=ObjectIdentity
tplinkSpanningTreeNotifications=_TplinkSpanningTreeNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,21,2))
tpMstpTopologyChange=NotificationType((1,3,6,1,4,1,11863,6,21,2,1))
if mibBuilder.loadTexts:tpMstpTopologyChange.setStatus(_A)
mibBuilder.exportSymbols(_L,**{'tplinkSpanningTreeMIB':tplinkSpanningTreeMIB,'tplinkSpanningTreeMIBObjects':tplinkSpanningTreeMIBObjects,'tpStpBasicCfg':tpStpBasicCfg,'tpStpBasicGlobalConfig':tpStpBasicGlobalConfig,'tpStpEnable':tpStpEnable,'tpRstpEnable':tpRstpEnable,'tpMstpEnable':tpMstpEnable,'tpStpBasicParamConfig':tpStpBasicParamConfig,'tpStpCistPriority':tpStpCistPriority,'tpStpHelloTime':tpStpHelloTime,'tpStpAgingTime':tpStpAgingTime,'tpStpForwardDelay':tpStpForwardDelay,'tpStpHoldCount':tpStpHoldCount,'tpStpMaxHops':tpStpMaxHops,'tpStpInfo':tpStpInfo,'tpStpEnableStatus':tpStpEnableStatus,'tpStpMode':tpStpMode,'tpStpLocalBridge':tpStpLocalBridge,'tpStpCISTRoot':tpStpCISTRoot,'tpStpExPathCost':tpStpExPathCost,'tpStpRegionRoot':tpStpRegionRoot,'tpStpInPathCost':tpStpInPathCost,'tpStpDesignatedBridge':tpStpDesignatedBridge,'tpStpRootPort':tpStpRootPort,'tpStpLastTopologyChangeTime':tpStpLastTopologyChangeTime,'tpStpTopologyChangeCounter':tpStpTopologyChangeCounter,'tpStpPortCfg':tpStpPortCfg,'tpStpPortConfigTable':tpStpPortConfigTable,'tpStpPortConfigEntry':tpStpPortConfigEntry,'tpStpPortNumber':tpStpPortNumber,'tpStpPortEnable':tpStpPortEnable,'tpStpPortPriority':tpStpPortPriority,'tpStpPortExPathCost':tpStpPortExPathCost,'tpStpPortInPathCost':tpStpPortInPathCost,'tpStpEdgePortStatus':tpStpEdgePortStatus,'tpStpPointToPointStatus':tpStpPointToPointStatus,'tpStpPortMCheck':tpStpPortMCheck,'tpStpPortStpVersion':tpStpPortStpVersion,'tpStpPortRole':tpStpPortRole,'tpStpPortStatus':tpStpPortStatus,'tpStpPortLag':tpStpPortLag,'tpStpInstanceCfg':tpStpInstanceCfg,'tpMstpRegionConfig':tpMstpRegionConfig,'tpMstpRegionName':tpMstpRegionName,'tpMstpRevision':tpMstpRevision,'tpMstpInstanceConfigTable':tpMstpInstanceConfigTable,'tpMstpInstanceConfigEntry':tpMstpInstanceConfigEntry,_T:tpMstpInstanceId,'tpMstpInstanceEnable':tpMstpInstanceEnable,'tpMstpInstancePriority':tpMstpInstancePriority,'tpMstpInstanceVlanId':tpMstpInstanceVlanId,'tpMstpClearInstanceVlanId':tpMstpClearInstanceVlanId,'tpMstpInstancePortConfigTable':tpMstpInstancePortConfigTable,'tpMstpInstancePortConfigEntry':tpMstpInstancePortConfigEntry,_U:tpMstpInstancePortConfigId,'tpMstpInstancePortNumber':tpMstpInstancePortNumber,'tpMstpInstancePortPriority':tpMstpInstancePortPriority,'tpMstpInstancePortPathCost':tpMstpInstancePortPathCost,'tpMstpInstancePortRole':tpMstpInstancePortRole,'tpMstpInstancePortStatus':tpMstpInstancePortStatus,'tpMstpInstancePortLag':tpMstpInstancePortLag,'tpStpSecurityCfg':tpStpSecurityCfg,'tpStpPortDefendTable':tpStpPortDefendTable,'tpStpPortDefendEntry':tpStpPortDefendEntry,'tpStpDefendPortNumber':tpStpDefendPortNumber,'tpStpLoopDefendEnable':tpStpLoopDefendEnable,'tpStpRootBridgeDefendEnable':tpStpRootBridgeDefendEnable,'tpStpTcDefendEnable':tpStpTcDefendEnable,'tpStpBPDUDefendEnable':tpStpBPDUDefendEnable,'tpStpBPDUHoldEnable':tpStpBPDUHoldEnable,'tpStpBPDUFloodEnable':tpStpBPDUFloodEnable,'tpStpDefendPortLag':tpStpDefendPortLag,'tplinkSpanningTreeNotifications':tplinkSpanningTreeNotifications,'tpMstpTopologyChange':tpMstpTopologyChange})