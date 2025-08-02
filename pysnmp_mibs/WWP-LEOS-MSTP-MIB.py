_U='wwpLeosMstpPortOperEdgePort'
_T='wwpLeosMstpPortStatsIndex'
_S='wwpLeosMstpXstPortCfgXstIndex'
_R='wwpLeosMstpXstPortCfgPortIndex'
_Q='read-create'
_P='wwpLeosMstpMstCfgXstMappingIndex'
_O='MstiOrCistInstanceIndex'
_N='wwpLeosMstpMstCfgVlanIndex'
_M='accessible-for-notify'
_L='DisplayString'
_K='seconds'
_J='wwpLeosMstpXstCfgIndex'
_I='not-accessible'
_H='OctetString'
_G='wwpLeosMstpPortInfoIndex'
_F='TruthValue'
_E='read-only'
_D='WWP-LEOS-MSTP-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_L,'PhysAddress','RowStatus','TextualConvention',_F)
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosMstp=ModuleIdentity((1,3,6,1,4,1,6141,2,60,37))
if mibBuilder.loadTexts:wwpLeosMstp.setRevisions(('2011-08-02 00:00','2006-09-29 17:00'))
class MstiInstanceIndex(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
class MstiOrCistInstanceIndex(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
class BpduCounter(TextualConvention,Counter32):status=_A;displayHint='d'
_WwpLeosMstpNotifications_ObjectIdentity=ObjectIdentity
wwpLeosMstpNotifications=_WwpLeosMstpNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,37,0))
_WwpLeosMstpObjects_ObjectIdentity=ObjectIdentity
wwpLeosMstpObjects=_WwpLeosMstpObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,37,1))
_WwpLeosMstpCfg_ObjectIdentity=ObjectIdentity
wwpLeosMstpCfg=_WwpLeosMstpCfg_ObjectIdentity((1,3,6,1,4,1,6141,2,60,37,1,1))
class _WwpLeosMstpBridgeEnable_Type(TruthValue):defaultValue=1
_WwpLeosMstpBridgeEnable_Type.__name__=_F
_WwpLeosMstpBridgeEnable_Object=MibScalar
wwpLeosMstpBridgeEnable=_WwpLeosMstpBridgeEnable_Object((1,3,6,1,4,1,6141,2,60,37,1,1,1),_WwpLeosMstpBridgeEnable_Type())
wwpLeosMstpBridgeEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpBridgeEnable.setStatus(_A)
class _WwpLeosMstpForceVersion_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3)));namedValues=NamedValues(*(('stp',0),('rstp',2),('mstp',3)))
_WwpLeosMstpForceVersion_Type.__name__=_C
_WwpLeosMstpForceVersion_Object=MibScalar
wwpLeosMstpForceVersion=_WwpLeosMstpForceVersion_Object((1,3,6,1,4,1,6141,2,60,37,1,1,2),_WwpLeosMstpForceVersion_Type())
wwpLeosMstpForceVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosMstpForceVersion.setStatus(_A)
class _WwpLeosMstpForwardDelay_Type(Integer32):defaultValue=15;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_WwpLeosMstpForwardDelay_Type.__name__=_C
_WwpLeosMstpForwardDelay_Object=MibScalar
wwpLeosMstpForwardDelay=_WwpLeosMstpForwardDelay_Object((1,3,6,1,4,1,6141,2,60,37,1,1,3),_WwpLeosMstpForwardDelay_Type())
wwpLeosMstpForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpForwardDelay.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosMstpForwardDelay.setUnits(_K)
class _WwpLeosMstpTxHoldCount_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_WwpLeosMstpTxHoldCount_Type.__name__=_C
_WwpLeosMstpTxHoldCount_Object=MibScalar
wwpLeosMstpTxHoldCount=_WwpLeosMstpTxHoldCount_Object((1,3,6,1,4,1,6141,2,60,37,1,1,4),_WwpLeosMstpTxHoldCount_Type())
wwpLeosMstpTxHoldCount.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpTxHoldCount.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosMstpTxHoldCount.setUnits(_K)
class _WwpLeosMstpHelloTime_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_WwpLeosMstpHelloTime_Type.__name__=_C
_WwpLeosMstpHelloTime_Object=MibScalar
wwpLeosMstpHelloTime=_WwpLeosMstpHelloTime_Object((1,3,6,1,4,1,6141,2,60,37,1,1,5),_WwpLeosMstpHelloTime_Type())
wwpLeosMstpHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpHelloTime.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosMstpHelloTime.setUnits(_K)
class _WwpLeosMstpMaxAge_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_WwpLeosMstpMaxAge_Type.__name__=_C
_WwpLeosMstpMaxAge_Object=MibScalar
wwpLeosMstpMaxAge=_WwpLeosMstpMaxAge_Object((1,3,6,1,4,1,6141,2,60,37,1,1,6),_WwpLeosMstpMaxAge_Type())
wwpLeosMstpMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpMaxAge.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosMstpMaxAge.setUnits(_K)
class _WwpLeosMstpMaxHops_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_WwpLeosMstpMaxHops_Type.__name__=_C
_WwpLeosMstpMaxHops_Object=MibScalar
wwpLeosMstpMaxHops=_WwpLeosMstpMaxHops_Object((1,3,6,1,4,1,6141,2,60,37,1,1,7),_WwpLeosMstpMaxHops_Type())
wwpLeosMstpMaxHops.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpMaxHops.setStatus(_A)
class _WwpLeosMstpLoopbackBlock_Type(TruthValue):defaultValue=2
_WwpLeosMstpLoopbackBlock_Type.__name__=_F
_WwpLeosMstpLoopbackBlock_Object=MibScalar
wwpLeosMstpLoopbackBlock=_WwpLeosMstpLoopbackBlock_Object((1,3,6,1,4,1,6141,2,60,37,1,1,8),_WwpLeosMstpLoopbackBlock_Type())
wwpLeosMstpLoopbackBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpLoopbackBlock.setStatus(_A)
class _WwpLeosMstpPathCostDefault_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stp8021d1998',1),('stp8021t2001',2)))
_WwpLeosMstpPathCostDefault_Type.__name__=_C
_WwpLeosMstpPathCostDefault_Object=MibScalar
wwpLeosMstpPathCostDefault=_WwpLeosMstpPathCostDefault_Object((1,3,6,1,4,1,6141,2,60,37,1,1,9),_WwpLeosMstpPathCostDefault_Type())
wwpLeosMstpPathCostDefault.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpPathCostDefault.setStatus(_A)
class _WwpLeosMstpGlobalStpMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rstp',1),('mstp',2)))
_WwpLeosMstpGlobalStpMode_Type.__name__=_C
_WwpLeosMstpGlobalStpMode_Object=MibScalar
wwpLeosMstpGlobalStpMode=_WwpLeosMstpGlobalStpMode_Object((1,3,6,1,4,1,6141,2,60,37,1,1,10),_WwpLeosMstpGlobalStpMode_Type())
wwpLeosMstpGlobalStpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpGlobalStpMode.setStatus(_A)
_WwpLeosMstpPortCfgTable_Object=MibTable
wwpLeosMstpPortCfgTable=_WwpLeosMstpPortCfgTable_Object((1,3,6,1,4,1,6141,2,60,37,1,1,11))
if mibBuilder.loadTexts:wwpLeosMstpPortCfgTable.setStatus(_A)
_WwpLeosMstpPortCfgEntry_Object=MibTableRow
wwpLeosMstpPortCfgEntry=_WwpLeosMstpPortCfgEntry_Object((1,3,6,1,4,1,6141,2,60,37,1,1,11,1))
wwpLeosMstpPortCfgEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:wwpLeosMstpPortCfgEntry.setStatus(_A)
class _WwpLeosMstpPortInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosMstpPortInfoIndex_Type.__name__=_C
_WwpLeosMstpPortInfoIndex_Object=MibTableColumn
wwpLeosMstpPortInfoIndex=_WwpLeosMstpPortInfoIndex_Object((1,3,6,1,4,1,6141,2,60,37,1,1,11,1,1),_WwpLeosMstpPortInfoIndex_Type())
wwpLeosMstpPortInfoIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:wwpLeosMstpPortInfoIndex.setStatus(_A)
class _WwpLeosMstpPortEnable_Type(TruthValue):defaultValue=1
_WwpLeosMstpPortEnable_Type.__name__=_F
_WwpLeosMstpPortEnable_Object=MibTableColumn
wwpLeosMstpPortEnable=_WwpLeosMstpPortEnable_Object((1,3,6,1,4,1,6141,2,60,37,1,1,11,1,2),_WwpLeosMstpPortEnable_Type())
wwpLeosMstpPortEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpPortEnable.setStatus(_A)
class _WwpLeosMstpPortAdminExtPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_WwpLeosMstpPortAdminExtPathCost_Type.__name__=_C
_WwpLeosMstpPortAdminExtPathCost_Object=MibTableColumn
wwpLeosMstpPortAdminExtPathCost=_WwpLeosMstpPortAdminExtPathCost_Object((1,3,6,1,4,1,6141,2,60,37,1,1,11,1,3),_WwpLeosMstpPortAdminExtPathCost_Type())
wwpLeosMstpPortAdminExtPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpPortAdminExtPathCost.setStatus(_A)
_WwpLeosMstpPortOperExtPathCost_Type=Integer32
_WwpLeosMstpPortOperExtPathCost_Object=MibTableColumn
wwpLeosMstpPortOperExtPathCost=_WwpLeosMstpPortOperExtPathCost_Object((1,3,6,1,4,1,6141,2,60,37,1,1,11,1,4),_WwpLeosMstpPortOperExtPathCost_Type())
wwpLeosMstpPortOperExtPathCost.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosMstpPortOperExtPathCost.setStatus(_A)
class _WwpLeosMstpPortDynamicExtPathCost_Type(TruthValue):defaultValue=1
_WwpLeosMstpPortDynamicExtPathCost_Type.__name__=_F
_WwpLeosMstpPortDynamicExtPathCost_Object=MibTableColumn
wwpLeosMstpPortDynamicExtPathCost=_WwpLeosMstpPortDynamicExtPathCost_Object((1,3,6,1,4,1,6141,2,60,37,1,1,11,1,5),_WwpLeosMstpPortDynamicExtPathCost_Type())
wwpLeosMstpPortDynamicExtPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpPortDynamicExtPathCost.setStatus(_A)
_WwpLeosMstpPortAdminEdgePort_Type=TruthValue
_WwpLeosMstpPortAdminEdgePort_Object=MibTableColumn
wwpLeosMstpPortAdminEdgePort=_WwpLeosMstpPortAdminEdgePort_Object((1,3,6,1,4,1,6141,2,60,37,1,1,11,1,6),_WwpLeosMstpPortAdminEdgePort_Type())
wwpLeosMstpPortAdminEdgePort.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpPortAdminEdgePort.setStatus(_A)
_WwpLeosMstpPortOperEdgePort_Type=TruthValue
_WwpLeosMstpPortOperEdgePort_Object=MibTableColumn
wwpLeosMstpPortOperEdgePort=_WwpLeosMstpPortOperEdgePort_Object((1,3,6,1,4,1,6141,2,60,37,1,1,11,1,7),_WwpLeosMstpPortOperEdgePort_Type())
wwpLeosMstpPortOperEdgePort.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosMstpPortOperEdgePort.setStatus(_A)
_WwpLeosMstpPortProtocolMigration_Type=TruthValue
_WwpLeosMstpPortProtocolMigration_Object=MibTableColumn
wwpLeosMstpPortProtocolMigration=_WwpLeosMstpPortProtocolMigration_Object((1,3,6,1,4,1,6141,2,60,37,1,1,11,1,8),_WwpLeosMstpPortProtocolMigration_Type())
wwpLeosMstpPortProtocolMigration.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpPortProtocolMigration.setStatus(_A)
class _WwpLeosMstpPortAdminPointToPoint_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('forceTrue',0),('forceFalse',1),('auto',2)))
_WwpLeosMstpPortAdminPointToPoint_Type.__name__=_C
_WwpLeosMstpPortAdminPointToPoint_Object=MibTableColumn
wwpLeosMstpPortAdminPointToPoint=_WwpLeosMstpPortAdminPointToPoint_Object((1,3,6,1,4,1,6141,2,60,37,1,1,11,1,9),_WwpLeosMstpPortAdminPointToPoint_Type())
wwpLeosMstpPortAdminPointToPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpPortAdminPointToPoint.setStatus(_A)
_WwpLeosMstpPortOperPointToPoint_Type=TruthValue
_WwpLeosMstpPortOperPointToPoint_Object=MibTableColumn
wwpLeosMstpPortOperPointToPoint=_WwpLeosMstpPortOperPointToPoint_Object((1,3,6,1,4,1,6141,2,60,37,1,1,11,1,10),_WwpLeosMstpPortOperPointToPoint_Type())
wwpLeosMstpPortOperPointToPoint.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosMstpPortOperPointToPoint.setStatus(_A)
class _WwpLeosMstpPortAutoEdge_Type(TruthValue):defaultValue=1
_WwpLeosMstpPortAutoEdge_Type.__name__=_F
_WwpLeosMstpPortAutoEdge_Object=MibTableColumn
wwpLeosMstpPortAutoEdge=_WwpLeosMstpPortAutoEdge_Object((1,3,6,1,4,1,6141,2,60,37,1,1,11,1,11),_WwpLeosMstpPortAutoEdge_Type())
wwpLeosMstpPortAutoEdge.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpPortAutoEdge.setStatus(_A)
class _WwpLeosMstpPortRestrictedRole_Type(TruthValue):defaultValue=2
_WwpLeosMstpPortRestrictedRole_Type.__name__=_F
_WwpLeosMstpPortRestrictedRole_Object=MibTableColumn
wwpLeosMstpPortRestrictedRole=_WwpLeosMstpPortRestrictedRole_Object((1,3,6,1,4,1,6141,2,60,37,1,1,11,1,12),_WwpLeosMstpPortRestrictedRole_Type())
wwpLeosMstpPortRestrictedRole.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpPortRestrictedRole.setStatus(_A)
class _WwpLeosMstpPortRestrictedTcn_Type(TruthValue):defaultValue=2
_WwpLeosMstpPortRestrictedTcn_Type.__name__=_F
_WwpLeosMstpPortRestrictedTcn_Object=MibTableColumn
wwpLeosMstpPortRestrictedTcn=_WwpLeosMstpPortRestrictedTcn_Object((1,3,6,1,4,1,6141,2,60,37,1,1,11,1,13),_WwpLeosMstpPortRestrictedTcn_Type())
wwpLeosMstpPortRestrictedTcn.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpPortRestrictedTcn.setStatus(_A)
_WwpLeosMstpMstCfg_ObjectIdentity=ObjectIdentity
wwpLeosMstpMstCfg=_WwpLeosMstpMstCfg_ObjectIdentity((1,3,6,1,4,1,6141,2,60,37,1,2))
class _WwpLeosMstpMstCfgName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_WwpLeosMstpMstCfgName_Type.__name__=_L
_WwpLeosMstpMstCfgName_Object=MibScalar
wwpLeosMstpMstCfgName=_WwpLeosMstpMstCfgName_Object((1,3,6,1,4,1,6141,2,60,37,1,2,1),_WwpLeosMstpMstCfgName_Type())
wwpLeosMstpMstCfgName.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpMstCfgName.setStatus(_A)
class _WwpLeosMstpMstCfgRevLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosMstpMstCfgRevLevel_Type.__name__=_C
_WwpLeosMstpMstCfgRevLevel_Object=MibScalar
wwpLeosMstpMstCfgRevLevel=_WwpLeosMstpMstCfgRevLevel_Object((1,3,6,1,4,1,6141,2,60,37,1,2,2),_WwpLeosMstpMstCfgRevLevel_Type())
wwpLeosMstpMstCfgRevLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpMstCfgRevLevel.setStatus(_A)
_WwpLeosMstpMstCfgVlanTable_Object=MibTable
wwpLeosMstpMstCfgVlanTable=_WwpLeosMstpMstCfgVlanTable_Object((1,3,6,1,4,1,6141,2,60,37,1,2,3))
if mibBuilder.loadTexts:wwpLeosMstpMstCfgVlanTable.setStatus(_A)
_WwpLeosMstpMstCfgVlanEntry_Object=MibTableRow
wwpLeosMstpMstCfgVlanEntry=_WwpLeosMstpMstCfgVlanEntry_Object((1,3,6,1,4,1,6141,2,60,37,1,2,3,1))
wwpLeosMstpMstCfgVlanEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:wwpLeosMstpMstCfgVlanEntry.setStatus(_A)
class _WwpLeosMstpMstCfgVlanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_WwpLeosMstpMstCfgVlanIndex_Type.__name__=_C
_WwpLeosMstpMstCfgVlanIndex_Object=MibTableColumn
wwpLeosMstpMstCfgVlanIndex=_WwpLeosMstpMstCfgVlanIndex_Object((1,3,6,1,4,1,6141,2,60,37,1,2,3,1,1),_WwpLeosMstpMstCfgVlanIndex_Type())
wwpLeosMstpMstCfgVlanIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:wwpLeosMstpMstCfgVlanIndex.setStatus(_A)
class _WwpLeosMstpMstCfgMstiIndex_Type(MstiOrCistInstanceIndex):defaultValue=0
_WwpLeosMstpMstCfgMstiIndex_Type.__name__=_O
_WwpLeosMstpMstCfgMstiIndex_Object=MibTableColumn
wwpLeosMstpMstCfgMstiIndex=_WwpLeosMstpMstCfgMstiIndex_Object((1,3,6,1,4,1,6141,2,60,37,1,2,3,1,2),_WwpLeosMstpMstCfgMstiIndex_Type())
wwpLeosMstpMstCfgMstiIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpMstCfgMstiIndex.setStatus(_A)
_WwpLeosMstpMstCfgXstMappingTable_Object=MibTable
wwpLeosMstpMstCfgXstMappingTable=_WwpLeosMstpMstCfgXstMappingTable_Object((1,3,6,1,4,1,6141,2,60,37,1,2,4))
if mibBuilder.loadTexts:wwpLeosMstpMstCfgXstMappingTable.setStatus(_A)
_WwpLeosMstpMstCfgXstMappingEntry_Object=MibTableRow
wwpLeosMstpMstCfgXstMappingEntry=_WwpLeosMstpMstCfgXstMappingEntry_Object((1,3,6,1,4,1,6141,2,60,37,1,2,4,1))
wwpLeosMstpMstCfgXstMappingEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:wwpLeosMstpMstCfgXstMappingEntry.setStatus(_A)
_WwpLeosMstpMstCfgXstMappingIndex_Type=MstiOrCistInstanceIndex
_WwpLeosMstpMstCfgXstMappingIndex_Object=MibTableColumn
wwpLeosMstpMstCfgXstMappingIndex=_WwpLeosMstpMstCfgXstMappingIndex_Object((1,3,6,1,4,1,6141,2,60,37,1,2,4,1,1),_WwpLeosMstpMstCfgXstMappingIndex_Type())
wwpLeosMstpMstCfgXstMappingIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:wwpLeosMstpMstCfgXstMappingIndex.setStatus(_A)
class _WwpLeosMstpMstCfgXstMapping1k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_WwpLeosMstpMstCfgXstMapping1k_Type.__name__=_H
_WwpLeosMstpMstCfgXstMapping1k_Object=MibTableColumn
wwpLeosMstpMstCfgXstMapping1k=_WwpLeosMstpMstCfgXstMapping1k_Object((1,3,6,1,4,1,6141,2,60,37,1,2,4,1,2),_WwpLeosMstpMstCfgXstMapping1k_Type())
wwpLeosMstpMstCfgXstMapping1k.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosMstpMstCfgXstMapping1k.setStatus(_A)
class _WwpLeosMstpMstCfgXstMapping2k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_WwpLeosMstpMstCfgXstMapping2k_Type.__name__=_H
_WwpLeosMstpMstCfgXstMapping2k_Object=MibTableColumn
wwpLeosMstpMstCfgXstMapping2k=_WwpLeosMstpMstCfgXstMapping2k_Object((1,3,6,1,4,1,6141,2,60,37,1,2,4,1,3),_WwpLeosMstpMstCfgXstMapping2k_Type())
wwpLeosMstpMstCfgXstMapping2k.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosMstpMstCfgXstMapping2k.setStatus(_A)
class _WwpLeosMstpMstCfgXstMapping3k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_WwpLeosMstpMstCfgXstMapping3k_Type.__name__=_H
_WwpLeosMstpMstCfgXstMapping3k_Object=MibTableColumn
wwpLeosMstpMstCfgXstMapping3k=_WwpLeosMstpMstCfgXstMapping3k_Object((1,3,6,1,4,1,6141,2,60,37,1,2,4,1,4),_WwpLeosMstpMstCfgXstMapping3k_Type())
wwpLeosMstpMstCfgXstMapping3k.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosMstpMstCfgXstMapping3k.setStatus(_A)
class _WwpLeosMstpMstCfgXstMapping4k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_WwpLeosMstpMstCfgXstMapping4k_Type.__name__=_H
_WwpLeosMstpMstCfgXstMapping4k_Object=MibTableColumn
wwpLeosMstpMstCfgXstMapping4k=_WwpLeosMstpMstCfgXstMapping4k_Object((1,3,6,1,4,1,6141,2,60,37,1,2,4,1,5),_WwpLeosMstpMstCfgXstMapping4k_Type())
wwpLeosMstpMstCfgXstMapping4k.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosMstpMstCfgXstMapping4k.setStatus(_A)
class _WwpLeosMstpMstCfgIdDigest_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_WwpLeosMstpMstCfgIdDigest_Type.__name__=_H
_WwpLeosMstpMstCfgIdDigest_Object=MibScalar
wwpLeosMstpMstCfgIdDigest=_WwpLeosMstpMstCfgIdDigest_Object((1,3,6,1,4,1,6141,2,60,37,1,2,5),_WwpLeosMstpMstCfgIdDigest_Type())
wwpLeosMstpMstCfgIdDigest.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosMstpMstCfgIdDigest.setStatus(_A)
_WwpLeosMstpXstCfg_ObjectIdentity=ObjectIdentity
wwpLeosMstpXstCfg=_WwpLeosMstpXstCfg_ObjectIdentity((1,3,6,1,4,1,6141,2,60,37,1,3))
_WwpLeosMstpXstCfgTable_Object=MibTable
wwpLeosMstpXstCfgTable=_WwpLeosMstpXstCfgTable_Object((1,3,6,1,4,1,6141,2,60,37,1,3,1))
if mibBuilder.loadTexts:wwpLeosMstpXstCfgTable.setStatus(_A)
_WwpLeosMstpXstCfgEntry_Object=MibTableRow
wwpLeosMstpXstCfgEntry=_WwpLeosMstpXstCfgEntry_Object((1,3,6,1,4,1,6141,2,60,37,1,3,1,1))
wwpLeosMstpXstCfgEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:wwpLeosMstpXstCfgEntry.setStatus(_A)
_WwpLeosMstpXstCfgIndex_Type=MstiOrCistInstanceIndex
_WwpLeosMstpXstCfgIndex_Object=MibTableColumn
wwpLeosMstpXstCfgIndex=_WwpLeosMstpXstCfgIndex_Object((1,3,6,1,4,1,6141,2,60,37,1,3,1,1,1),_WwpLeosMstpXstCfgIndex_Type())
wwpLeosMstpXstCfgIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:wwpLeosMstpXstCfgIndex.setStatus(_A)
class _WwpLeosMstpXstCfgBridgePriority_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_WwpLeosMstpXstCfgBridgePriority_Type.__name__=_C
_WwpLeosMstpXstCfgBridgePriority_Object=MibTableColumn
wwpLeosMstpXstCfgBridgePriority=_WwpLeosMstpXstCfgBridgePriority_Object((1,3,6,1,4,1,6141,2,60,37,1,3,1,1,2),_WwpLeosMstpXstCfgBridgePriority_Type())
wwpLeosMstpXstCfgBridgePriority.setMaxAccess(_Q)
if mibBuilder.loadTexts:wwpLeosMstpXstCfgBridgePriority.setStatus(_A)
_WwpLeosMstpXstCfgStatus_Type=RowStatus
_WwpLeosMstpXstCfgStatus_Object=MibTableColumn
wwpLeosMstpXstCfgStatus=_WwpLeosMstpXstCfgStatus_Object((1,3,6,1,4,1,6141,2,60,37,1,3,1,1,3),_WwpLeosMstpXstCfgStatus_Type())
wwpLeosMstpXstCfgStatus.setMaxAccess(_Q)
if mibBuilder.loadTexts:wwpLeosMstpXstCfgStatus.setStatus(_A)
_WwpLeosMstpXstPortCfgTable_Object=MibTable
wwpLeosMstpXstPortCfgTable=_WwpLeosMstpXstPortCfgTable_Object((1,3,6,1,4,1,6141,2,60,37,1,3,2))
if mibBuilder.loadTexts:wwpLeosMstpXstPortCfgTable.setStatus(_A)
_WwpLeosMstpXstPortCfgEntry_Object=MibTableRow
wwpLeosMstpXstPortCfgEntry=_WwpLeosMstpXstPortCfgEntry_Object((1,3,6,1,4,1,6141,2,60,37,1,3,2,1))
wwpLeosMstpXstPortCfgEntry.setIndexNames((0,_D,_R),(0,_D,_S))
if mibBuilder.loadTexts:wwpLeosMstpXstPortCfgEntry.setStatus(_A)
class _WwpLeosMstpXstPortCfgPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosMstpXstPortCfgPortIndex_Type.__name__=_C
_WwpLeosMstpXstPortCfgPortIndex_Object=MibTableColumn
wwpLeosMstpXstPortCfgPortIndex=_WwpLeosMstpXstPortCfgPortIndex_Object((1,3,6,1,4,1,6141,2,60,37,1,3,2,1,1),_WwpLeosMstpXstPortCfgPortIndex_Type())
wwpLeosMstpXstPortCfgPortIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:wwpLeosMstpXstPortCfgPortIndex.setStatus(_A)
_WwpLeosMstpXstPortCfgXstIndex_Type=MstiOrCistInstanceIndex
_WwpLeosMstpXstPortCfgXstIndex_Object=MibTableColumn
wwpLeosMstpXstPortCfgXstIndex=_WwpLeosMstpXstPortCfgXstIndex_Object((1,3,6,1,4,1,6141,2,60,37,1,3,2,1,2),_WwpLeosMstpXstPortCfgXstIndex_Type())
wwpLeosMstpXstPortCfgXstIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:wwpLeosMstpXstPortCfgXstIndex.setStatus(_A)
class _WwpLeosMstpXstPortCfgPortPriority_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_WwpLeosMstpXstPortCfgPortPriority_Type.__name__=_C
_WwpLeosMstpXstPortCfgPortPriority_Object=MibTableColumn
wwpLeosMstpXstPortCfgPortPriority=_WwpLeosMstpXstPortCfgPortPriority_Object((1,3,6,1,4,1,6141,2,60,37,1,3,2,1,3),_WwpLeosMstpXstPortCfgPortPriority_Type())
wwpLeosMstpXstPortCfgPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpXstPortCfgPortPriority.setStatus(_A)
class _WwpLeosMstpXstPortCfgAdminIntPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_WwpLeosMstpXstPortCfgAdminIntPathCost_Type.__name__=_C
_WwpLeosMstpXstPortCfgAdminIntPathCost_Object=MibTableColumn
wwpLeosMstpXstPortCfgAdminIntPathCost=_WwpLeosMstpXstPortCfgAdminIntPathCost_Object((1,3,6,1,4,1,6141,2,60,37,1,3,2,1,4),_WwpLeosMstpXstPortCfgAdminIntPathCost_Type())
wwpLeosMstpXstPortCfgAdminIntPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpXstPortCfgAdminIntPathCost.setStatus(_A)
_WwpLeosMstpXstPortCfgOperIntPathCost_Type=Integer32
_WwpLeosMstpXstPortCfgOperIntPathCost_Object=MibTableColumn
wwpLeosMstpXstPortCfgOperIntPathCost=_WwpLeosMstpXstPortCfgOperIntPathCost_Object((1,3,6,1,4,1,6141,2,60,37,1,3,2,1,5),_WwpLeosMstpXstPortCfgOperIntPathCost_Type())
wwpLeosMstpXstPortCfgOperIntPathCost.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosMstpXstPortCfgOperIntPathCost.setStatus(_A)
class _WwpLeosMstpXstPortCfgDynamicIntPathCost_Type(TruthValue):defaultValue=1
_WwpLeosMstpXstPortCfgDynamicIntPathCost_Type.__name__=_F
_WwpLeosMstpXstPortCfgDynamicIntPathCost_Object=MibTableColumn
wwpLeosMstpXstPortCfgDynamicIntPathCost=_WwpLeosMstpXstPortCfgDynamicIntPathCost_Object((1,3,6,1,4,1,6141,2,60,37,1,3,2,1,6),_WwpLeosMstpXstPortCfgDynamicIntPathCost_Type())
wwpLeosMstpXstPortCfgDynamicIntPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpXstPortCfgDynamicIntPathCost.setStatus(_A)
_WwpLeosMstpStats_ObjectIdentity=ObjectIdentity
wwpLeosMstpStats=_WwpLeosMstpStats_ObjectIdentity((1,3,6,1,4,1,6141,2,60,37,1,4))
_WwpLeosMstpBridgeStatsClear_Type=TruthValue
_WwpLeosMstpBridgeStatsClear_Object=MibScalar
wwpLeosMstpBridgeStatsClear=_WwpLeosMstpBridgeStatsClear_Object((1,3,6,1,4,1,6141,2,60,37,1,4,1),_WwpLeosMstpBridgeStatsClear_Type())
wwpLeosMstpBridgeStatsClear.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpBridgeStatsClear.setStatus(_A)
_WwpLeosMstpPortStatsTable_Object=MibTable
wwpLeosMstpPortStatsTable=_WwpLeosMstpPortStatsTable_Object((1,3,6,1,4,1,6141,2,60,37,1,4,2))
if mibBuilder.loadTexts:wwpLeosMstpPortStatsTable.setStatus(_A)
_WwpLeosMstpPortStatsEntry_Object=MibTableRow
wwpLeosMstpPortStatsEntry=_WwpLeosMstpPortStatsEntry_Object((1,3,6,1,4,1,6141,2,60,37,1,4,2,1))
wwpLeosMstpPortStatsEntry.setIndexNames((0,_D,_T))
if mibBuilder.loadTexts:wwpLeosMstpPortStatsEntry.setStatus(_A)
class _WwpLeosMstpPortStatsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosMstpPortStatsIndex_Type.__name__=_C
_WwpLeosMstpPortStatsIndex_Object=MibTableColumn
wwpLeosMstpPortStatsIndex=_WwpLeosMstpPortStatsIndex_Object((1,3,6,1,4,1,6141,2,60,37,1,4,2,1,1),_WwpLeosMstpPortStatsIndex_Type())
wwpLeosMstpPortStatsIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:wwpLeosMstpPortStatsIndex.setStatus(_A)
_WwpLeosMstpPortStatsClear_Type=TruthValue
_WwpLeosMstpPortStatsClear_Object=MibTableColumn
wwpLeosMstpPortStatsClear=_WwpLeosMstpPortStatsClear_Object((1,3,6,1,4,1,6141,2,60,37,1,4,2,1,2),_WwpLeosMstpPortStatsClear_Type())
wwpLeosMstpPortStatsClear.setMaxAccess(_B)
if mibBuilder.loadTexts:wwpLeosMstpPortStatsClear.setStatus(_A)
_WwpLeosMstpPortStatsRxTcnBpdu_Type=BpduCounter
_WwpLeosMstpPortStatsRxTcnBpdu_Object=MibTableColumn
wwpLeosMstpPortStatsRxTcnBpdu=_WwpLeosMstpPortStatsRxTcnBpdu_Object((1,3,6,1,4,1,6141,2,60,37,1,4,2,1,3),_WwpLeosMstpPortStatsRxTcnBpdu_Type())
wwpLeosMstpPortStatsRxTcnBpdu.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosMstpPortStatsRxTcnBpdu.setStatus(_A)
_WwpLeosMstpPortStatsRxCfgBpdu_Type=BpduCounter
_WwpLeosMstpPortStatsRxCfgBpdu_Object=MibTableColumn
wwpLeosMstpPortStatsRxCfgBpdu=_WwpLeosMstpPortStatsRxCfgBpdu_Object((1,3,6,1,4,1,6141,2,60,37,1,4,2,1,4),_WwpLeosMstpPortStatsRxCfgBpdu_Type())
wwpLeosMstpPortStatsRxCfgBpdu.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosMstpPortStatsRxCfgBpdu.setStatus(_A)
_WwpLeosMstpPortStatsRxRstBpdu_Type=BpduCounter
_WwpLeosMstpPortStatsRxRstBpdu_Object=MibTableColumn
wwpLeosMstpPortStatsRxRstBpdu=_WwpLeosMstpPortStatsRxRstBpdu_Object((1,3,6,1,4,1,6141,2,60,37,1,4,2,1,5),_WwpLeosMstpPortStatsRxRstBpdu_Type())
wwpLeosMstpPortStatsRxRstBpdu.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosMstpPortStatsRxRstBpdu.setStatus(_A)
_WwpLeosMstpPortStatsRxMstBpdu_Type=BpduCounter
_WwpLeosMstpPortStatsRxMstBpdu_Object=MibTableColumn
wwpLeosMstpPortStatsRxMstBpdu=_WwpLeosMstpPortStatsRxMstBpdu_Object((1,3,6,1,4,1,6141,2,60,37,1,4,2,1,6),_WwpLeosMstpPortStatsRxMstBpdu_Type())
wwpLeosMstpPortStatsRxMstBpdu.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosMstpPortStatsRxMstBpdu.setStatus(_A)
_WwpLeosMstpPortStatsTxTcnBpdu_Type=BpduCounter
_WwpLeosMstpPortStatsTxTcnBpdu_Object=MibTableColumn
wwpLeosMstpPortStatsTxTcnBpdu=_WwpLeosMstpPortStatsTxTcnBpdu_Object((1,3,6,1,4,1,6141,2,60,37,1,4,2,1,7),_WwpLeosMstpPortStatsTxTcnBpdu_Type())
wwpLeosMstpPortStatsTxTcnBpdu.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosMstpPortStatsTxTcnBpdu.setStatus(_A)
_WwpLeosMstpPortStatsTxCfgBpdu_Type=BpduCounter
_WwpLeosMstpPortStatsTxCfgBpdu_Object=MibTableColumn
wwpLeosMstpPortStatsTxCfgBpdu=_WwpLeosMstpPortStatsTxCfgBpdu_Object((1,3,6,1,4,1,6141,2,60,37,1,4,2,1,8),_WwpLeosMstpPortStatsTxCfgBpdu_Type())
wwpLeosMstpPortStatsTxCfgBpdu.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosMstpPortStatsTxCfgBpdu.setStatus(_A)
_WwpLeosMstpPortStatsTxRstBpdu_Type=BpduCounter
_WwpLeosMstpPortStatsTxRstBpdu_Object=MibTableColumn
wwpLeosMstpPortStatsTxRstBpdu=_WwpLeosMstpPortStatsTxRstBpdu_Object((1,3,6,1,4,1,6141,2,60,37,1,4,2,1,9),_WwpLeosMstpPortStatsTxRstBpdu_Type())
wwpLeosMstpPortStatsTxRstBpdu.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosMstpPortStatsTxRstBpdu.setStatus(_A)
_WwpLeosMstpPortStatsTxMstBpdu_Type=BpduCounter
_WwpLeosMstpPortStatsTxMstBpdu_Object=MibTableColumn
wwpLeosMstpPortStatsTxMstBpdu=_WwpLeosMstpPortStatsTxMstBpdu_Object((1,3,6,1,4,1,6141,2,60,37,1,4,2,1,10),_WwpLeosMstpPortStatsTxMstBpdu_Type())
wwpLeosMstpPortStatsTxMstBpdu.setMaxAccess(_E)
if mibBuilder.loadTexts:wwpLeosMstpPortStatsTxMstBpdu.setStatus(_A)
_WwpLeosMstpConformance_ObjectIdentity=ObjectIdentity
wwpLeosMstpConformance=_WwpLeosMstpConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,37,2))
wwpLeosMstpNewRootNotification=NotificationType((1,3,6,1,4,1,6141,2,60,37,0,1))
wwpLeosMstpNewRootNotification.setObjects((_D,_J))
if mibBuilder.loadTexts:wwpLeosMstpNewRootNotification.setStatus(_A)
wwpLeosMstpTopologyChangeNotification=NotificationType((1,3,6,1,4,1,6141,2,60,37,0,2))
wwpLeosMstpTopologyChangeNotification.setObjects(*((_D,_G),(_D,_J)))
if mibBuilder.loadTexts:wwpLeosMstpTopologyChangeNotification.setStatus(_A)
wwpLeosMstpPortBackupNotification=NotificationType((1,3,6,1,4,1,6141,2,60,37,0,3))
wwpLeosMstpPortBackupNotification.setObjects((_D,_G))
if mibBuilder.loadTexts:wwpLeosMstpPortBackupNotification.setStatus(_A)
wwpLeosMstpPvstBpduReceivedNotification=NotificationType((1,3,6,1,4,1,6141,2,60,37,0,4))
wwpLeosMstpPvstBpduReceivedNotification.setObjects((_D,_G))
if mibBuilder.loadTexts:wwpLeosMstpPvstBpduReceivedNotification.setStatus('deprecated')
wwpLeosMstpSelfLoopNotification=NotificationType((1,3,6,1,4,1,6141,2,60,37,0,5))
wwpLeosMstpSelfLoopNotification.setObjects((_D,_G))
if mibBuilder.loadTexts:wwpLeosMstpSelfLoopNotification.setStatus(_A)
wwpLeosMstpPortOperEdgeNotification=NotificationType((1,3,6,1,4,1,6141,2,60,37,0,6))
wwpLeosMstpPortOperEdgeNotification.setObjects(*((_D,_G),(_D,_U)))
if mibBuilder.loadTexts:wwpLeosMstpPortOperEdgeNotification.setStatus(_A)
wwpLeosMstpPortFlapNotification=NotificationType((1,3,6,1,4,1,6141,2,60,37,0,7))
wwpLeosMstpPortFlapNotification.setObjects((_D,_G))
if mibBuilder.loadTexts:wwpLeosMstpPortFlapNotification.setStatus(_A)
wwpLeosMstpBridgeRootPortLostNotification=NotificationType((1,3,6,1,4,1,6141,2,60,37,0,8))
wwpLeosMstpBridgeRootPortLostNotification.setObjects(*((_D,_G),(_D,_J)))
if mibBuilder.loadTexts:wwpLeosMstpBridgeRootPortLostNotification.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'MstiInstanceIndex':MstiInstanceIndex,_O:MstiOrCistInstanceIndex,'BpduCounter':BpduCounter,'wwpLeosMstp':wwpLeosMstp,'wwpLeosMstpNotifications':wwpLeosMstpNotifications,'wwpLeosMstpNewRootNotification':wwpLeosMstpNewRootNotification,'wwpLeosMstpTopologyChangeNotification':wwpLeosMstpTopologyChangeNotification,'wwpLeosMstpPortBackupNotification':wwpLeosMstpPortBackupNotification,'wwpLeosMstpPvstBpduReceivedNotification':wwpLeosMstpPvstBpduReceivedNotification,'wwpLeosMstpSelfLoopNotification':wwpLeosMstpSelfLoopNotification,'wwpLeosMstpPortOperEdgeNotification':wwpLeosMstpPortOperEdgeNotification,'wwpLeosMstpPortFlapNotification':wwpLeosMstpPortFlapNotification,'wwpLeosMstpBridgeRootPortLostNotification':wwpLeosMstpBridgeRootPortLostNotification,'wwpLeosMstpObjects':wwpLeosMstpObjects,'wwpLeosMstpCfg':wwpLeosMstpCfg,'wwpLeosMstpBridgeEnable':wwpLeosMstpBridgeEnable,'wwpLeosMstpForceVersion':wwpLeosMstpForceVersion,'wwpLeosMstpForwardDelay':wwpLeosMstpForwardDelay,'wwpLeosMstpTxHoldCount':wwpLeosMstpTxHoldCount,'wwpLeosMstpHelloTime':wwpLeosMstpHelloTime,'wwpLeosMstpMaxAge':wwpLeosMstpMaxAge,'wwpLeosMstpMaxHops':wwpLeosMstpMaxHops,'wwpLeosMstpLoopbackBlock':wwpLeosMstpLoopbackBlock,'wwpLeosMstpPathCostDefault':wwpLeosMstpPathCostDefault,'wwpLeosMstpGlobalStpMode':wwpLeosMstpGlobalStpMode,'wwpLeosMstpPortCfgTable':wwpLeosMstpPortCfgTable,'wwpLeosMstpPortCfgEntry':wwpLeosMstpPortCfgEntry,_G:wwpLeosMstpPortInfoIndex,'wwpLeosMstpPortEnable':wwpLeosMstpPortEnable,'wwpLeosMstpPortAdminExtPathCost':wwpLeosMstpPortAdminExtPathCost,'wwpLeosMstpPortOperExtPathCost':wwpLeosMstpPortOperExtPathCost,'wwpLeosMstpPortDynamicExtPathCost':wwpLeosMstpPortDynamicExtPathCost,'wwpLeosMstpPortAdminEdgePort':wwpLeosMstpPortAdminEdgePort,_U:wwpLeosMstpPortOperEdgePort,'wwpLeosMstpPortProtocolMigration':wwpLeosMstpPortProtocolMigration,'wwpLeosMstpPortAdminPointToPoint':wwpLeosMstpPortAdminPointToPoint,'wwpLeosMstpPortOperPointToPoint':wwpLeosMstpPortOperPointToPoint,'wwpLeosMstpPortAutoEdge':wwpLeosMstpPortAutoEdge,'wwpLeosMstpPortRestrictedRole':wwpLeosMstpPortRestrictedRole,'wwpLeosMstpPortRestrictedTcn':wwpLeosMstpPortRestrictedTcn,'wwpLeosMstpMstCfg':wwpLeosMstpMstCfg,'wwpLeosMstpMstCfgName':wwpLeosMstpMstCfgName,'wwpLeosMstpMstCfgRevLevel':wwpLeosMstpMstCfgRevLevel,'wwpLeosMstpMstCfgVlanTable':wwpLeosMstpMstCfgVlanTable,'wwpLeosMstpMstCfgVlanEntry':wwpLeosMstpMstCfgVlanEntry,_N:wwpLeosMstpMstCfgVlanIndex,'wwpLeosMstpMstCfgMstiIndex':wwpLeosMstpMstCfgMstiIndex,'wwpLeosMstpMstCfgXstMappingTable':wwpLeosMstpMstCfgXstMappingTable,'wwpLeosMstpMstCfgXstMappingEntry':wwpLeosMstpMstCfgXstMappingEntry,_P:wwpLeosMstpMstCfgXstMappingIndex,'wwpLeosMstpMstCfgXstMapping1k':wwpLeosMstpMstCfgXstMapping1k,'wwpLeosMstpMstCfgXstMapping2k':wwpLeosMstpMstCfgXstMapping2k,'wwpLeosMstpMstCfgXstMapping3k':wwpLeosMstpMstCfgXstMapping3k,'wwpLeosMstpMstCfgXstMapping4k':wwpLeosMstpMstCfgXstMapping4k,'wwpLeosMstpMstCfgIdDigest':wwpLeosMstpMstCfgIdDigest,'wwpLeosMstpXstCfg':wwpLeosMstpXstCfg,'wwpLeosMstpXstCfgTable':wwpLeosMstpXstCfgTable,'wwpLeosMstpXstCfgEntry':wwpLeosMstpXstCfgEntry,_J:wwpLeosMstpXstCfgIndex,'wwpLeosMstpXstCfgBridgePriority':wwpLeosMstpXstCfgBridgePriority,'wwpLeosMstpXstCfgStatus':wwpLeosMstpXstCfgStatus,'wwpLeosMstpXstPortCfgTable':wwpLeosMstpXstPortCfgTable,'wwpLeosMstpXstPortCfgEntry':wwpLeosMstpXstPortCfgEntry,_R:wwpLeosMstpXstPortCfgPortIndex,_S:wwpLeosMstpXstPortCfgXstIndex,'wwpLeosMstpXstPortCfgPortPriority':wwpLeosMstpXstPortCfgPortPriority,'wwpLeosMstpXstPortCfgAdminIntPathCost':wwpLeosMstpXstPortCfgAdminIntPathCost,'wwpLeosMstpXstPortCfgOperIntPathCost':wwpLeosMstpXstPortCfgOperIntPathCost,'wwpLeosMstpXstPortCfgDynamicIntPathCost':wwpLeosMstpXstPortCfgDynamicIntPathCost,'wwpLeosMstpStats':wwpLeosMstpStats,'wwpLeosMstpBridgeStatsClear':wwpLeosMstpBridgeStatsClear,'wwpLeosMstpPortStatsTable':wwpLeosMstpPortStatsTable,'wwpLeosMstpPortStatsEntry':wwpLeosMstpPortStatsEntry,_T:wwpLeosMstpPortStatsIndex,'wwpLeosMstpPortStatsClear':wwpLeosMstpPortStatsClear,'wwpLeosMstpPortStatsRxTcnBpdu':wwpLeosMstpPortStatsRxTcnBpdu,'wwpLeosMstpPortStatsRxCfgBpdu':wwpLeosMstpPortStatsRxCfgBpdu,'wwpLeosMstpPortStatsRxRstBpdu':wwpLeosMstpPortStatsRxRstBpdu,'wwpLeosMstpPortStatsRxMstBpdu':wwpLeosMstpPortStatsRxMstBpdu,'wwpLeosMstpPortStatsTxTcnBpdu':wwpLeosMstpPortStatsTxTcnBpdu,'wwpLeosMstpPortStatsTxCfgBpdu':wwpLeosMstpPortStatsTxCfgBpdu,'wwpLeosMstpPortStatsTxRstBpdu':wwpLeosMstpPortStatsTxRstBpdu,'wwpLeosMstpPortStatsTxMstBpdu':wwpLeosMstpPortStatsTxMstBpdu,'wwpLeosMstpConformance':wwpLeosMstpConformance})