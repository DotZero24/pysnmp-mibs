_P='zyMstpInfoInstancePortInstanceId'
_O='zyMstpInfoInstanceId'
_N='zyMstpInfoVlanMapVid'
_M='zyMstpInstancePortInstanceId'
_L='zyMstpVlanMapInstance'
_K='zyMstpInstanceId'
_J='dot1dBasePort'
_I='BRIDGE-MIB'
_H='not-accessible'
_G='Timeout'
_F='OctetString'
_E='ZYXEL-MSTP-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,Timeout,dot1dBasePort=mibBuilder.importSymbols(_I,'BridgeId',_G,_J)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelMstp=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,53))
class MstiOrCistInstanceIndex(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_ZyxelMstpSetup_ObjectIdentity=ObjectIdentity
zyxelMstpSetup=_ZyxelMstpSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,53,1))
_ZyxelMstpGeneral_ObjectIdentity=ObjectIdentity
zyxelMstpGeneral=_ZyxelMstpGeneral_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,53,1,1))
_ZyMstpGeneralState_Type=EnabledStatus
_ZyMstpGeneralState_Object=MibScalar
zyMstpGeneralState=_ZyMstpGeneralState_Object((1,3,6,1,4,1,890,1,15,3,53,1,1,1),_ZyMstpGeneralState_Type())
zyMstpGeneralState.setMaxAccess(_C)
if mibBuilder.loadTexts:zyMstpGeneralState.setStatus(_A)
_ZyMstpGeneralConfigIdName_Type=DisplayString
_ZyMstpGeneralConfigIdName_Object=MibScalar
zyMstpGeneralConfigIdName=_ZyMstpGeneralConfigIdName_Object((1,3,6,1,4,1,890,1,15,3,53,1,1,2),_ZyMstpGeneralConfigIdName_Type())
zyMstpGeneralConfigIdName.setMaxAccess(_C)
if mibBuilder.loadTexts:zyMstpGeneralConfigIdName.setStatus(_A)
_ZyMstpGeneralConfigIdRevisionLevel_Type=Integer32
_ZyMstpGeneralConfigIdRevisionLevel_Object=MibScalar
zyMstpGeneralConfigIdRevisionLevel=_ZyMstpGeneralConfigIdRevisionLevel_Object((1,3,6,1,4,1,890,1,15,3,53,1,1,3),_ZyMstpGeneralConfigIdRevisionLevel_Type())
zyMstpGeneralConfigIdRevisionLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:zyMstpGeneralConfigIdRevisionLevel.setStatus(_A)
class _ZyMstpGeneralHelloTime_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_ZyMstpGeneralHelloTime_Type.__name__=_G
_ZyMstpGeneralHelloTime_Object=MibScalar
zyMstpGeneralHelloTime=_ZyMstpGeneralHelloTime_Object((1,3,6,1,4,1,890,1,15,3,53,1,1,4),_ZyMstpGeneralHelloTime_Type())
zyMstpGeneralHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:zyMstpGeneralHelloTime.setStatus(_A)
class _ZyMstpGeneralMaxAge_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_ZyMstpGeneralMaxAge_Type.__name__=_G
_ZyMstpGeneralMaxAge_Object=MibScalar
zyMstpGeneralMaxAge=_ZyMstpGeneralMaxAge_Object((1,3,6,1,4,1,890,1,15,3,53,1,1,5),_ZyMstpGeneralMaxAge_Type())
zyMstpGeneralMaxAge.setMaxAccess(_C)
if mibBuilder.loadTexts:zyMstpGeneralMaxAge.setStatus(_A)
class _ZyMstpGeneralForwardDelay_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_ZyMstpGeneralForwardDelay_Type.__name__=_G
_ZyMstpGeneralForwardDelay_Object=MibScalar
zyMstpGeneralForwardDelay=_ZyMstpGeneralForwardDelay_Object((1,3,6,1,4,1,890,1,15,3,53,1,1,6),_ZyMstpGeneralForwardDelay_Type())
zyMstpGeneralForwardDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:zyMstpGeneralForwardDelay.setStatus(_A)
class _ZyMstpGeneralMaxHops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ZyMstpGeneralMaxHops_Type.__name__=_D
_ZyMstpGeneralMaxHops_Object=MibScalar
zyMstpGeneralMaxHops=_ZyMstpGeneralMaxHops_Object((1,3,6,1,4,1,890,1,15,3,53,1,1,7),_ZyMstpGeneralMaxHops_Type())
zyMstpGeneralMaxHops.setMaxAccess(_C)
if mibBuilder.loadTexts:zyMstpGeneralMaxHops.setStatus(_A)
_ZyMstpVlanMapMaxNumberOfInstances_Type=Integer32
_ZyMstpVlanMapMaxNumberOfInstances_Object=MibScalar
zyMstpVlanMapMaxNumberOfInstances=_ZyMstpVlanMapMaxNumberOfInstances_Object((1,3,6,1,4,1,890,1,15,3,53,1,2),_ZyMstpVlanMapMaxNumberOfInstances_Type())
zyMstpVlanMapMaxNumberOfInstances.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMstpVlanMapMaxNumberOfInstances.setStatus(_A)
_ZyxelMstpVlanMapTable_Object=MibTable
zyxelMstpVlanMapTable=_ZyxelMstpVlanMapTable_Object((1,3,6,1,4,1,890,1,15,3,53,1,3))
if mibBuilder.loadTexts:zyxelMstpVlanMapTable.setStatus(_A)
_ZyxelMstpVlanMapEntry_Object=MibTableRow
zyxelMstpVlanMapEntry=_ZyxelMstpVlanMapEntry_Object((1,3,6,1,4,1,890,1,15,3,53,1,3,1))
zyxelMstpVlanMapEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:zyxelMstpVlanMapEntry.setStatus(_A)
_ZyMstpVlanMapInstance_Type=MstiOrCistInstanceIndex
_ZyMstpVlanMapInstance_Object=MibTableColumn
zyMstpVlanMapInstance=_ZyMstpVlanMapInstance_Object((1,3,6,1,4,1,890,1,15,3,53,1,3,1,1),_ZyMstpVlanMapInstance_Type())
zyMstpVlanMapInstance.setMaxAccess(_H)
if mibBuilder.loadTexts:zyMstpVlanMapInstance.setStatus(_A)
class _ZyMstpVlanMapVlans1k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ZyMstpVlanMapVlans1k_Type.__name__=_F
_ZyMstpVlanMapVlans1k_Object=MibTableColumn
zyMstpVlanMapVlans1k=_ZyMstpVlanMapVlans1k_Object((1,3,6,1,4,1,890,1,15,3,53,1,3,1,2),_ZyMstpVlanMapVlans1k_Type())
zyMstpVlanMapVlans1k.setMaxAccess(_C)
if mibBuilder.loadTexts:zyMstpVlanMapVlans1k.setStatus(_A)
class _ZyMstpVlanMapVlans2k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ZyMstpVlanMapVlans2k_Type.__name__=_F
_ZyMstpVlanMapVlans2k_Object=MibTableColumn
zyMstpVlanMapVlans2k=_ZyMstpVlanMapVlans2k_Object((1,3,6,1,4,1,890,1,15,3,53,1,3,1,3),_ZyMstpVlanMapVlans2k_Type())
zyMstpVlanMapVlans2k.setMaxAccess(_C)
if mibBuilder.loadTexts:zyMstpVlanMapVlans2k.setStatus(_A)
class _ZyMstpVlanMapVlans3k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ZyMstpVlanMapVlans3k_Type.__name__=_F
_ZyMstpVlanMapVlans3k_Object=MibTableColumn
zyMstpVlanMapVlans3k=_ZyMstpVlanMapVlans3k_Object((1,3,6,1,4,1,890,1,15,3,53,1,3,1,4),_ZyMstpVlanMapVlans3k_Type())
zyMstpVlanMapVlans3k.setMaxAccess(_C)
if mibBuilder.loadTexts:zyMstpVlanMapVlans3k.setStatus(_A)
class _ZyMstpVlanMapVlans4k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_ZyMstpVlanMapVlans4k_Type.__name__=_F
_ZyMstpVlanMapVlans4k_Object=MibTableColumn
zyMstpVlanMapVlans4k=_ZyMstpVlanMapVlans4k_Object((1,3,6,1,4,1,890,1,15,3,53,1,3,1,5),_ZyMstpVlanMapVlans4k_Type())
zyMstpVlanMapVlans4k.setMaxAccess(_C)
if mibBuilder.loadTexts:zyMstpVlanMapVlans4k.setStatus(_A)
_ZyMstpVlanMapRowStatus_Type=RowStatus
_ZyMstpVlanMapRowStatus_Object=MibTableColumn
zyMstpVlanMapRowStatus=_ZyMstpVlanMapRowStatus_Object((1,3,6,1,4,1,890,1,15,3,53,1,3,1,6),_ZyMstpVlanMapRowStatus_Type())
zyMstpVlanMapRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyMstpVlanMapRowStatus.setStatus(_A)
_ZyxelMstpPortTable_Object=MibTable
zyxelMstpPortTable=_ZyxelMstpPortTable_Object((1,3,6,1,4,1,890,1,15,3,53,1,4))
if mibBuilder.loadTexts:zyxelMstpPortTable.setStatus(_A)
_ZyxelMstpPortEntry_Object=MibTableRow
zyxelMstpPortEntry=_ZyxelMstpPortEntry_Object((1,3,6,1,4,1,890,1,15,3,53,1,4,1))
zyxelMstpPortEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:zyxelMstpPortEntry.setStatus(_A)
class _ZyMstpPortAdminEdgePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_ZyMstpPortAdminEdgePort_Type.__name__=_D
_ZyMstpPortAdminEdgePort_Object=MibTableColumn
zyMstpPortAdminEdgePort=_ZyMstpPortAdminEdgePort_Object((1,3,6,1,4,1,890,1,15,3,53,1,4,1,1),_ZyMstpPortAdminEdgePort_Type())
zyMstpPortAdminEdgePort.setMaxAccess(_C)
if mibBuilder.loadTexts:zyMstpPortAdminEdgePort.setStatus(_A)
_ZyxelMstpInstanceTable_Object=MibTable
zyxelMstpInstanceTable=_ZyxelMstpInstanceTable_Object((1,3,6,1,4,1,890,1,15,3,53,1,5))
if mibBuilder.loadTexts:zyxelMstpInstanceTable.setStatus(_A)
_ZyxelMstpInstanceEntry_Object=MibTableRow
zyxelMstpInstanceEntry=_ZyxelMstpInstanceEntry_Object((1,3,6,1,4,1,890,1,15,3,53,1,5,1))
zyxelMstpInstanceEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:zyxelMstpInstanceEntry.setStatus(_A)
_ZyMstpInstanceId_Type=MstiOrCistInstanceIndex
_ZyMstpInstanceId_Object=MibTableColumn
zyMstpInstanceId=_ZyMstpInstanceId_Object((1,3,6,1,4,1,890,1,15,3,53,1,5,1,1),_ZyMstpInstanceId_Type())
zyMstpInstanceId.setMaxAccess(_H)
if mibBuilder.loadTexts:zyMstpInstanceId.setStatus(_A)
class _ZyMstpInstanceBridgePriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_ZyMstpInstanceBridgePriority_Type.__name__=_D
_ZyMstpInstanceBridgePriority_Object=MibTableColumn
zyMstpInstanceBridgePriority=_ZyMstpInstanceBridgePriority_Object((1,3,6,1,4,1,890,1,15,3,53,1,5,1,2),_ZyMstpInstanceBridgePriority_Type())
zyMstpInstanceBridgePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:zyMstpInstanceBridgePriority.setStatus(_A)
_ZyxelMstpInstancePortTable_Object=MibTable
zyxelMstpInstancePortTable=_ZyxelMstpInstancePortTable_Object((1,3,6,1,4,1,890,1,15,3,53,1,6))
if mibBuilder.loadTexts:zyxelMstpInstancePortTable.setStatus(_A)
_ZyxelMstpInstancePortEntry_Object=MibTableRow
zyxelMstpInstancePortEntry=_ZyxelMstpInstancePortEntry_Object((1,3,6,1,4,1,890,1,15,3,53,1,6,1))
zyxelMstpInstancePortEntry.setIndexNames((0,_E,_M),(0,_I,_J))
if mibBuilder.loadTexts:zyxelMstpInstancePortEntry.setStatus(_A)
_ZyMstpInstancePortInstanceId_Type=MstiOrCistInstanceIndex
_ZyMstpInstancePortInstanceId_Object=MibTableColumn
zyMstpInstancePortInstanceId=_ZyMstpInstancePortInstanceId_Object((1,3,6,1,4,1,890,1,15,3,53,1,6,1,1),_ZyMstpInstancePortInstanceId_Type())
zyMstpInstancePortInstanceId.setMaxAccess(_H)
if mibBuilder.loadTexts:zyMstpInstancePortInstanceId.setStatus(_A)
_ZyMstpInstancePortState_Type=EnabledStatus
_ZyMstpInstancePortState_Object=MibTableColumn
zyMstpInstancePortState=_ZyMstpInstancePortState_Object((1,3,6,1,4,1,890,1,15,3,53,1,6,1,2),_ZyMstpInstancePortState_Type())
zyMstpInstancePortState.setMaxAccess(_C)
if mibBuilder.loadTexts:zyMstpInstancePortState.setStatus(_A)
class _ZyMstpInstancePortPriority_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ZyMstpInstancePortPriority_Type.__name__=_D
_ZyMstpInstancePortPriority_Object=MibTableColumn
zyMstpInstancePortPriority=_ZyMstpInstancePortPriority_Object((1,3,6,1,4,1,890,1,15,3,53,1,6,1,3),_ZyMstpInstancePortPriority_Type())
zyMstpInstancePortPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:zyMstpInstancePortPriority.setStatus(_A)
class _ZyMstpInstancePortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_ZyMstpInstancePortPathCost_Type.__name__=_D
_ZyMstpInstancePortPathCost_Object=MibTableColumn
zyMstpInstancePortPathCost=_ZyMstpInstancePortPathCost_Object((1,3,6,1,4,1,890,1,15,3,53,1,6,1,4),_ZyMstpInstancePortPathCost_Type())
zyMstpInstancePortPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:zyMstpInstancePortPathCost.setStatus(_A)
_ZyxelMstpStatus_ObjectIdentity=ObjectIdentity
zyxelMstpStatus=_ZyxelMstpStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,53,2))
_ZyxelMstpInfoGeneral_ObjectIdentity=ObjectIdentity
zyxelMstpInfoGeneral=_ZyxelMstpInfoGeneral_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,53,2,1))
_ZyMstpInfoGeneralConfigIdName_Type=DisplayString
_ZyMstpInfoGeneralConfigIdName_Object=MibScalar
zyMstpInfoGeneralConfigIdName=_ZyMstpInfoGeneralConfigIdName_Object((1,3,6,1,4,1,890,1,15,3,53,2,1,1),_ZyMstpInfoGeneralConfigIdName_Type())
zyMstpInfoGeneralConfigIdName.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMstpInfoGeneralConfigIdName.setStatus(_A)
_ZyMstpInfoGeneralConfigIdRevisionLevel_Type=Integer32
_ZyMstpInfoGeneralConfigIdRevisionLevel_Object=MibScalar
zyMstpInfoGeneralConfigIdRevisionLevel=_ZyMstpInfoGeneralConfigIdRevisionLevel_Object((1,3,6,1,4,1,890,1,15,3,53,2,1,2),_ZyMstpInfoGeneralConfigIdRevisionLevel_Type())
zyMstpInfoGeneralConfigIdRevisionLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMstpInfoGeneralConfigIdRevisionLevel.setStatus(_A)
class _ZyMstpInfoGeneralConfigIdConfigDigest_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_ZyMstpInfoGeneralConfigIdConfigDigest_Type.__name__=_F
_ZyMstpInfoGeneralConfigIdConfigDigest_Object=MibScalar
zyMstpInfoGeneralConfigIdConfigDigest=_ZyMstpInfoGeneralConfigIdConfigDigest_Object((1,3,6,1,4,1,890,1,15,3,53,2,1,3),_ZyMstpInfoGeneralConfigIdConfigDigest_Type())
zyMstpInfoGeneralConfigIdConfigDigest.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMstpInfoGeneralConfigIdConfigDigest.setStatus(_A)
class _ZyMstpInfoGeneralHelloTime_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_ZyMstpInfoGeneralHelloTime_Type.__name__=_G
_ZyMstpInfoGeneralHelloTime_Object=MibScalar
zyMstpInfoGeneralHelloTime=_ZyMstpInfoGeneralHelloTime_Object((1,3,6,1,4,1,890,1,15,3,53,2,1,4),_ZyMstpInfoGeneralHelloTime_Type())
zyMstpInfoGeneralHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMstpInfoGeneralHelloTime.setStatus(_A)
class _ZyMstpInfoGeneralMaxAge_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_ZyMstpInfoGeneralMaxAge_Type.__name__=_G
_ZyMstpInfoGeneralMaxAge_Object=MibScalar
zyMstpInfoGeneralMaxAge=_ZyMstpInfoGeneralMaxAge_Object((1,3,6,1,4,1,890,1,15,3,53,2,1,5),_ZyMstpInfoGeneralMaxAge_Type())
zyMstpInfoGeneralMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMstpInfoGeneralMaxAge.setStatus(_A)
class _ZyMstpInfoGeneralForwardDelay_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,30))
_ZyMstpInfoGeneralForwardDelay_Type.__name__=_G
_ZyMstpInfoGeneralForwardDelay_Object=MibScalar
zyMstpInfoGeneralForwardDelay=_ZyMstpInfoGeneralForwardDelay_Object((1,3,6,1,4,1,890,1,15,3,53,2,1,6),_ZyMstpInfoGeneralForwardDelay_Type())
zyMstpInfoGeneralForwardDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:zyMstpInfoGeneralForwardDelay.setStatus(_A)
_ZyMstpInfoGeneralCistRootPathCost_Type=Integer32
_ZyMstpInfoGeneralCistRootPathCost_Object=MibScalar
zyMstpInfoGeneralCistRootPathCost=_ZyMstpInfoGeneralCistRootPathCost_Object((1,3,6,1,4,1,890,1,15,3,53,2,1,7),_ZyMstpInfoGeneralCistRootPathCost_Type())
zyMstpInfoGeneralCistRootPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMstpInfoGeneralCistRootPathCost.setStatus(_A)
class _ZyMstpInfoGeneralCistRootBridgeId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ZyMstpInfoGeneralCistRootBridgeId_Type.__name__=_F
_ZyMstpInfoGeneralCistRootBridgeId_Object=MibScalar
zyMstpInfoGeneralCistRootBridgeId=_ZyMstpInfoGeneralCistRootBridgeId_Object((1,3,6,1,4,1,890,1,15,3,53,2,1,8),_ZyMstpInfoGeneralCistRootBridgeId_Type())
zyMstpInfoGeneralCistRootBridgeId.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMstpInfoGeneralCistRootBridgeId.setStatus(_A)
_ZyxelMstpInfoVlanMapTable_Object=MibTable
zyxelMstpInfoVlanMapTable=_ZyxelMstpInfoVlanMapTable_Object((1,3,6,1,4,1,890,1,15,3,53,2,2))
if mibBuilder.loadTexts:zyxelMstpInfoVlanMapTable.setStatus(_A)
_ZyxelMstpInfoVlanMapEntry_Object=MibTableRow
zyxelMstpInfoVlanMapEntry=_ZyxelMstpInfoVlanMapEntry_Object((1,3,6,1,4,1,890,1,15,3,53,2,2,1))
zyxelMstpInfoVlanMapEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:zyxelMstpInfoVlanMapEntry.setStatus(_A)
class _ZyMstpInfoVlanMapVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZyMstpInfoVlanMapVid_Type.__name__=_D
_ZyMstpInfoVlanMapVid_Object=MibTableColumn
zyMstpInfoVlanMapVid=_ZyMstpInfoVlanMapVid_Object((1,3,6,1,4,1,890,1,15,3,53,2,2,1,1),_ZyMstpInfoVlanMapVid_Type())
zyMstpInfoVlanMapVid.setMaxAccess(_H)
if mibBuilder.loadTexts:zyMstpInfoVlanMapVid.setStatus(_A)
_ZyMstpInfoVlanMapInstance_Type=MstiOrCistInstanceIndex
_ZyMstpInfoVlanMapInstance_Object=MibTableColumn
zyMstpInfoVlanMapInstance=_ZyMstpInfoVlanMapInstance_Object((1,3,6,1,4,1,890,1,15,3,53,2,2,1,2),_ZyMstpInfoVlanMapInstance_Type())
zyMstpInfoVlanMapInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMstpInfoVlanMapInstance.setStatus(_A)
_ZyxelMstpInfoPortTable_Object=MibTable
zyxelMstpInfoPortTable=_ZyxelMstpInfoPortTable_Object((1,3,6,1,4,1,890,1,15,3,53,2,3))
if mibBuilder.loadTexts:zyxelMstpInfoPortTable.setStatus(_A)
_ZyxelMstpInfoPortEntry_Object=MibTableRow
zyxelMstpInfoPortEntry=_ZyxelMstpInfoPortEntry_Object((1,3,6,1,4,1,890,1,15,3,53,2,3,1))
zyxelMstpInfoPortEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:zyxelMstpInfoPortEntry.setStatus(_A)
_ZyMstpInfoPortOperEdgePort_Type=TruthValue
_ZyMstpInfoPortOperEdgePort_Object=MibTableColumn
zyMstpInfoPortOperEdgePort=_ZyMstpInfoPortOperEdgePort_Object((1,3,6,1,4,1,890,1,15,3,53,2,3,1,1),_ZyMstpInfoPortOperEdgePort_Type())
zyMstpInfoPortOperEdgePort.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMstpInfoPortOperEdgePort.setStatus(_A)
_ZyMstpInfoPortOperPointToPointMAC_Type=TruthValue
_ZyMstpInfoPortOperPointToPointMAC_Object=MibTableColumn
zyMstpInfoPortOperPointToPointMAC=_ZyMstpInfoPortOperPointToPointMAC_Object((1,3,6,1,4,1,890,1,15,3,53,2,3,1,2),_ZyMstpInfoPortOperPointToPointMAC_Type())
zyMstpInfoPortOperPointToPointMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMstpInfoPortOperPointToPointMAC.setStatus(_A)
_ZyxelMstpInfoInstanceTable_Object=MibTable
zyxelMstpInfoInstanceTable=_ZyxelMstpInfoInstanceTable_Object((1,3,6,1,4,1,890,1,15,3,53,2,4))
if mibBuilder.loadTexts:zyxelMstpInfoInstanceTable.setStatus(_A)
_ZyxelMstpInfoInstanceEntry_Object=MibTableRow
zyxelMstpInfoInstanceEntry=_ZyxelMstpInfoInstanceEntry_Object((1,3,6,1,4,1,890,1,15,3,53,2,4,1))
zyxelMstpInfoInstanceEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:zyxelMstpInfoInstanceEntry.setStatus(_A)
_ZyMstpInfoInstanceId_Type=MstiOrCistInstanceIndex
_ZyMstpInfoInstanceId_Object=MibTableColumn
zyMstpInfoInstanceId=_ZyMstpInfoInstanceId_Object((1,3,6,1,4,1,890,1,15,3,53,2,4,1,1),_ZyMstpInfoInstanceId_Type())
zyMstpInfoInstanceId.setMaxAccess(_H)
if mibBuilder.loadTexts:zyMstpInfoInstanceId.setStatus(_A)
_ZyMstpInfoInstanceBridgeId_Type=BridgeId
_ZyMstpInfoInstanceBridgeId_Object=MibTableColumn
zyMstpInfoInstanceBridgeId=_ZyMstpInfoInstanceBridgeId_Object((1,3,6,1,4,1,890,1,15,3,53,2,4,1,2),_ZyMstpInfoInstanceBridgeId_Type())
zyMstpInfoInstanceBridgeId.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMstpInfoInstanceBridgeId.setStatus(_A)
_ZyMstpInfoInstanceInternalRootCost_Type=Integer32
_ZyMstpInfoInstanceInternalRootCost_Object=MibTableColumn
zyMstpInfoInstanceInternalRootCost=_ZyMstpInfoInstanceInternalRootCost_Object((1,3,6,1,4,1,890,1,15,3,53,2,4,1,3),_ZyMstpInfoInstanceInternalRootCost_Type())
zyMstpInfoInstanceInternalRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMstpInfoInstanceInternalRootCost.setStatus(_A)
_ZyMstpInfoInstanceRootPort_Type=Integer32
_ZyMstpInfoInstanceRootPort_Object=MibTableColumn
zyMstpInfoInstanceRootPort=_ZyMstpInfoInstanceRootPort_Object((1,3,6,1,4,1,890,1,15,3,53,2,4,1,4),_ZyMstpInfoInstanceRootPort_Type())
zyMstpInfoInstanceRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMstpInfoInstanceRootPort.setStatus(_A)
_ZyMstpInfoInstanceTimeSinceTopologyChange_Type=TimeTicks
_ZyMstpInfoInstanceTimeSinceTopologyChange_Object=MibTableColumn
zyMstpInfoInstanceTimeSinceTopologyChange=_ZyMstpInfoInstanceTimeSinceTopologyChange_Object((1,3,6,1,4,1,890,1,15,3,53,2,4,1,5),_ZyMstpInfoInstanceTimeSinceTopologyChange_Type())
zyMstpInfoInstanceTimeSinceTopologyChange.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMstpInfoInstanceTimeSinceTopologyChange.setStatus(_A)
_ZyMstpInfoInstanceTopologyChangesCount_Type=Counter32
_ZyMstpInfoInstanceTopologyChangesCount_Object=MibTableColumn
zyMstpInfoInstanceTopologyChangesCount=_ZyMstpInfoInstanceTopologyChangesCount_Object((1,3,6,1,4,1,890,1,15,3,53,2,4,1,6),_ZyMstpInfoInstanceTopologyChangesCount_Type())
zyMstpInfoInstanceTopologyChangesCount.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMstpInfoInstanceTopologyChangesCount.setStatus(_A)
_ZyxelMstpInfoInstancePortTable_Object=MibTable
zyxelMstpInfoInstancePortTable=_ZyxelMstpInfoInstancePortTable_Object((1,3,6,1,4,1,890,1,15,3,53,2,5))
if mibBuilder.loadTexts:zyxelMstpInfoInstancePortTable.setStatus(_A)
_ZyxelMstpInfoInstancePortEntry_Object=MibTableRow
zyxelMstpInfoInstancePortEntry=_ZyxelMstpInfoInstancePortEntry_Object((1,3,6,1,4,1,890,1,15,3,53,2,5,1))
zyxelMstpInfoInstancePortEntry.setIndexNames((0,_E,_P),(0,_I,_J))
if mibBuilder.loadTexts:zyxelMstpInfoInstancePortEntry.setStatus(_A)
_ZyMstpInfoInstancePortInstanceId_Type=MstiOrCistInstanceIndex
_ZyMstpInfoInstancePortInstanceId_Object=MibTableColumn
zyMstpInfoInstancePortInstanceId=_ZyMstpInfoInstancePortInstanceId_Object((1,3,6,1,4,1,890,1,15,3,53,2,5,1,1),_ZyMstpInfoInstancePortInstanceId_Type())
zyMstpInfoInstancePortInstanceId.setMaxAccess(_H)
if mibBuilder.loadTexts:zyMstpInfoInstancePortInstanceId.setStatus(_A)
class _ZyMstpInfoInstancePortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_ZyMstpInfoInstancePortPathCost_Type.__name__=_D
_ZyMstpInfoInstancePortPathCost_Object=MibTableColumn
zyMstpInfoInstancePortPathCost=_ZyMstpInfoInstancePortPathCost_Object((1,3,6,1,4,1,890,1,15,3,53,2,5,1,2),_ZyMstpInfoInstancePortPathCost_Type())
zyMstpInfoInstancePortPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMstpInfoInstancePortPathCost.setStatus(_A)
class _ZyMstpInfoInstancePortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('disabled',0),('discarding',1),('learning',2),('forwarding',3),('unknown',4)))
_ZyMstpInfoInstancePortState_Type.__name__=_D
_ZyMstpInfoInstancePortState_Object=MibTableColumn
zyMstpInfoInstancePortState=_ZyMstpInfoInstancePortState_Object((1,3,6,1,4,1,890,1,15,3,53,2,5,1,3),_ZyMstpInfoInstancePortState_Type())
zyMstpInfoInstancePortState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMstpInfoInstancePortState.setStatus(_A)
_ZyMstpInfoInstancePortDesignatedRoot_Type=BridgeId
_ZyMstpInfoInstancePortDesignatedRoot_Object=MibTableColumn
zyMstpInfoInstancePortDesignatedRoot=_ZyMstpInfoInstancePortDesignatedRoot_Object((1,3,6,1,4,1,890,1,15,3,53,2,5,1,4),_ZyMstpInfoInstancePortDesignatedRoot_Type())
zyMstpInfoInstancePortDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMstpInfoInstancePortDesignatedRoot.setStatus(_A)
_ZyMstpInfoInstancePortDesignatedCost_Type=Integer32
_ZyMstpInfoInstancePortDesignatedCost_Object=MibTableColumn
zyMstpInfoInstancePortDesignatedCost=_ZyMstpInfoInstancePortDesignatedCost_Object((1,3,6,1,4,1,890,1,15,3,53,2,5,1,5),_ZyMstpInfoInstancePortDesignatedCost_Type())
zyMstpInfoInstancePortDesignatedCost.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMstpInfoInstancePortDesignatedCost.setStatus(_A)
_ZyMstpInfoInstancePortDesignatedBridge_Type=BridgeId
_ZyMstpInfoInstancePortDesignatedBridge_Object=MibTableColumn
zyMstpInfoInstancePortDesignatedBridge=_ZyMstpInfoInstancePortDesignatedBridge_Object((1,3,6,1,4,1,890,1,15,3,53,2,5,1,6),_ZyMstpInfoInstancePortDesignatedBridge_Type())
zyMstpInfoInstancePortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMstpInfoInstancePortDesignatedBridge.setStatus(_A)
_ZyMstpInfoInstancePortDesignatedPort_Type=Integer32
_ZyMstpInfoInstancePortDesignatedPort_Object=MibTableColumn
zyMstpInfoInstancePortDesignatedPort=_ZyMstpInfoInstancePortDesignatedPort_Object((1,3,6,1,4,1,890,1,15,3,53,2,5,1,7),_ZyMstpInfoInstancePortDesignatedPort_Type())
zyMstpInfoInstancePortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMstpInfoInstancePortDesignatedPort.setStatus(_A)
_ZyxelMstpNotifications_ObjectIdentity=ObjectIdentity
zyxelMstpNotifications=_ZyxelMstpNotifications_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,53,3))
zyMstpNewRoot=NotificationType((1,3,6,1,4,1,890,1,15,3,53,3,1))
zyMstpNewRoot.setObjects((_E,_K))
if mibBuilder.loadTexts:zyMstpNewRoot.setStatus(_A)
zyMstpTopologyChange=NotificationType((1,3,6,1,4,1,890,1,15,3,53,3,2))
zyMstpTopologyChange.setObjects((_E,_K))
if mibBuilder.loadTexts:zyMstpTopologyChange.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'MstiOrCistInstanceIndex':MstiOrCistInstanceIndex,'zyxelMstp':zyxelMstp,'zyxelMstpSetup':zyxelMstpSetup,'zyxelMstpGeneral':zyxelMstpGeneral,'zyMstpGeneralState':zyMstpGeneralState,'zyMstpGeneralConfigIdName':zyMstpGeneralConfigIdName,'zyMstpGeneralConfigIdRevisionLevel':zyMstpGeneralConfigIdRevisionLevel,'zyMstpGeneralHelloTime':zyMstpGeneralHelloTime,'zyMstpGeneralMaxAge':zyMstpGeneralMaxAge,'zyMstpGeneralForwardDelay':zyMstpGeneralForwardDelay,'zyMstpGeneralMaxHops':zyMstpGeneralMaxHops,'zyMstpVlanMapMaxNumberOfInstances':zyMstpVlanMapMaxNumberOfInstances,'zyxelMstpVlanMapTable':zyxelMstpVlanMapTable,'zyxelMstpVlanMapEntry':zyxelMstpVlanMapEntry,_L:zyMstpVlanMapInstance,'zyMstpVlanMapVlans1k':zyMstpVlanMapVlans1k,'zyMstpVlanMapVlans2k':zyMstpVlanMapVlans2k,'zyMstpVlanMapVlans3k':zyMstpVlanMapVlans3k,'zyMstpVlanMapVlans4k':zyMstpVlanMapVlans4k,'zyMstpVlanMapRowStatus':zyMstpVlanMapRowStatus,'zyxelMstpPortTable':zyxelMstpPortTable,'zyxelMstpPortEntry':zyxelMstpPortEntry,'zyMstpPortAdminEdgePort':zyMstpPortAdminEdgePort,'zyxelMstpInstanceTable':zyxelMstpInstanceTable,'zyxelMstpInstanceEntry':zyxelMstpInstanceEntry,_K:zyMstpInstanceId,'zyMstpInstanceBridgePriority':zyMstpInstanceBridgePriority,'zyxelMstpInstancePortTable':zyxelMstpInstancePortTable,'zyxelMstpInstancePortEntry':zyxelMstpInstancePortEntry,_M:zyMstpInstancePortInstanceId,'zyMstpInstancePortState':zyMstpInstancePortState,'zyMstpInstancePortPriority':zyMstpInstancePortPriority,'zyMstpInstancePortPathCost':zyMstpInstancePortPathCost,'zyxelMstpStatus':zyxelMstpStatus,'zyxelMstpInfoGeneral':zyxelMstpInfoGeneral,'zyMstpInfoGeneralConfigIdName':zyMstpInfoGeneralConfigIdName,'zyMstpInfoGeneralConfigIdRevisionLevel':zyMstpInfoGeneralConfigIdRevisionLevel,'zyMstpInfoGeneralConfigIdConfigDigest':zyMstpInfoGeneralConfigIdConfigDigest,'zyMstpInfoGeneralHelloTime':zyMstpInfoGeneralHelloTime,'zyMstpInfoGeneralMaxAge':zyMstpInfoGeneralMaxAge,'zyMstpInfoGeneralForwardDelay':zyMstpInfoGeneralForwardDelay,'zyMstpInfoGeneralCistRootPathCost':zyMstpInfoGeneralCistRootPathCost,'zyMstpInfoGeneralCistRootBridgeId':zyMstpInfoGeneralCistRootBridgeId,'zyxelMstpInfoVlanMapTable':zyxelMstpInfoVlanMapTable,'zyxelMstpInfoVlanMapEntry':zyxelMstpInfoVlanMapEntry,_N:zyMstpInfoVlanMapVid,'zyMstpInfoVlanMapInstance':zyMstpInfoVlanMapInstance,'zyxelMstpInfoPortTable':zyxelMstpInfoPortTable,'zyxelMstpInfoPortEntry':zyxelMstpInfoPortEntry,'zyMstpInfoPortOperEdgePort':zyMstpInfoPortOperEdgePort,'zyMstpInfoPortOperPointToPointMAC':zyMstpInfoPortOperPointToPointMAC,'zyxelMstpInfoInstanceTable':zyxelMstpInfoInstanceTable,'zyxelMstpInfoInstanceEntry':zyxelMstpInfoInstanceEntry,_O:zyMstpInfoInstanceId,'zyMstpInfoInstanceBridgeId':zyMstpInfoInstanceBridgeId,'zyMstpInfoInstanceInternalRootCost':zyMstpInfoInstanceInternalRootCost,'zyMstpInfoInstanceRootPort':zyMstpInfoInstanceRootPort,'zyMstpInfoInstanceTimeSinceTopologyChange':zyMstpInfoInstanceTimeSinceTopologyChange,'zyMstpInfoInstanceTopologyChangesCount':zyMstpInfoInstanceTopologyChangesCount,'zyxelMstpInfoInstancePortTable':zyxelMstpInfoInstancePortTable,'zyxelMstpInfoInstancePortEntry':zyxelMstpInfoInstancePortEntry,_P:zyMstpInfoInstancePortInstanceId,'zyMstpInfoInstancePortPathCost':zyMstpInfoInstancePortPathCost,'zyMstpInfoInstancePortState':zyMstpInfoInstancePortState,'zyMstpInfoInstancePortDesignatedRoot':zyMstpInfoInstancePortDesignatedRoot,'zyMstpInfoInstancePortDesignatedCost':zyMstpInfoInstancePortDesignatedCost,'zyMstpInfoInstancePortDesignatedBridge':zyMstpInfoInstancePortDesignatedBridge,'zyMstpInfoInstancePortDesignatedPort':zyMstpInfoInstancePortDesignatedPort,'zyxelMstpNotifications':zyxelMstpNotifications,'zyMstpNewRoot':zyMstpNewRoot,'zyMstpTopologyChange':zyMstpTopologyChange})