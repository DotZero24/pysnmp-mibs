_AF='etsysMstpLoopProtectNotificationGroup'
_AE='etsysMstpLoopProtectGroup'
_AD='etsysMstpNonForwardingReasonGroup'
_AC='etsysMstpMaxInstancesGroup'
_AB='etsysMstpBackupRootGroup'
_AA='etsysMstpBridgeHelloTimeGroup'
_A9='etsysMstpAutoEdgeDetectGroup'
_A8='etsysMstpPortGroup'
_A7='etsysMstpBridgeGroup'
_A6='etsysMstpConfigGroup'
_A5='etsysMstpLoopProtectEvent'
_A4='etsysMstpPortExtnLoopProtectEnable'
_A3='etsysMstpPortExtnNonForwardingReason'
_A2='etsysMstpMaxConfigurableMsts'
_A1='etsysMstpMstiExtnBackupRootEnable'
_A0='etsysMstpBridgeHelloTimeMode'
_z='etsysMstpAutoEdgeDetection'
_y='etsysMstpBoundaryPort'
_x='etsysMstpPortHelloTime'
_w='etsysMstpHelloTime'
_v='etsysMstpPortRoleValue'
_u='etsysMstpPortDesignatedPort'
_t='etsysMstpPortDesignatedBridge'
_s='etsysMstpPortDesignatedCost'
_r='etsysMstpPortDesignatedRoot'
_q='etsysMstpPortOperPathCost'
_p='etsysMstpPortAdminPathCost'
_o='etsysMstpPortState'
_n='etsysMstpPortPriority'
_m='etsysMstpRootPort'
_l='etsysMstpRootPathCost'
_k='etsysMstpDesignatedRoot'
_j='etsysMstpTopologyChangeInProgress'
_i='etsysMstpTopologyChangeCount'
_h='etsysMstpTimeSinceTopologyChange'
_g='etsysMstpBridgePriority'
_f='etsysMstpMaxHopCount'
_e='etsysMstpCistPathCost'
_d='etsysMstpCistRegionalRootIdentifier'
_c='etsysMstpConfigDigest'
_b='etsysMstpRevisionLevel'
_a='etsysMstpConfigName'
_Z='etsysMstpFormatSelector'
_Y='etsysMstpMstIdOfVlan'
_X='etsysMstpMstIdOfFdb'
_W='etsysMstpMstiStatus'
_V='etsysMstpNumMsts'
_U='etsysMstpMaxSupportedMsts'
_T='etsysMstpMaxMstId'
_S='etsysMstpPortExtnEntry'
_R='etsysMstpMstiExtnEntry'
_Q='disabled'
_P='HexString'
_O='etsysMstpVlanId'
_N='etsysMstpFdbId'
_M='TruthValue'
_L='SnmpAdminString'
_K='etsysMstpPortExtnLoopProtectBlocking'
_J='etsysMstpPortNumber'
_I='not-accessible'
_H='Integer32'
_G='etsysMstpMstId'
_F='EnabledStatus'
_E='Unsigned32'
_D='read-write'
_C='read-only'
_B='ENTERASYS-MSTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,=mibBuilder.importSymbols('BRIDGE-MIB','BridgeId')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_F)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_L)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_M)
etsysMstpMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,28))
if mibBuilder.loadTexts:etsysMstpMIB.setRevisions(('2006-11-09 16:40','2006-10-04 19:54','2004-07-14 16:25','2004-04-08 19:59','2004-02-12 21:38','2003-01-21 14:27','2002-10-11 17:05'))
class HexString(TextualConvention,OctetString):status=_A;displayHint='1x:';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,1024))
_EtsysMstpObjects_ObjectIdentity=ObjectIdentity
etsysMstpObjects=_EtsysMstpObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,28,1))
_EtsysMstpNotifications_ObjectIdentity=ObjectIdentity
etsysMstpNotifications=_EtsysMstpNotifications_ObjectIdentity((1,3,6,1,4,1,5624,1,2,28,1,0))
_EtsysMstpConfig_ObjectIdentity=ObjectIdentity
etsysMstpConfig=_EtsysMstpConfig_ObjectIdentity((1,3,6,1,4,1,5624,1,2,28,1,1))
class _EtsysMstpMaxMstId_Type(Unsigned32):defaultValue=4094
_EtsysMstpMaxMstId_Type.__name__=_E
_EtsysMstpMaxMstId_Object=MibScalar
etsysMstpMaxMstId=_EtsysMstpMaxMstId_Object((1,3,6,1,4,1,5624,1,2,28,1,1,1),_EtsysMstpMaxMstId_Type())
etsysMstpMaxMstId.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMstpMaxMstId.setStatus(_A)
class _EtsysMstpMaxSupportedMsts_Type(Unsigned32):defaultValue=64
_EtsysMstpMaxSupportedMsts_Type.__name__=_E
_EtsysMstpMaxSupportedMsts_Object=MibScalar
etsysMstpMaxSupportedMsts=_EtsysMstpMaxSupportedMsts_Object((1,3,6,1,4,1,5624,1,2,28,1,1,2),_EtsysMstpMaxSupportedMsts_Type())
etsysMstpMaxSupportedMsts.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMstpMaxSupportedMsts.setStatus(_A)
_EtsysMstpNumMsts_Type=Unsigned32
_EtsysMstpNumMsts_Object=MibScalar
etsysMstpNumMsts=_EtsysMstpNumMsts_Object((1,3,6,1,4,1,5624,1,2,28,1,1,3),_EtsysMstpNumMsts_Type())
etsysMstpNumMsts.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMstpNumMsts.setStatus(_A)
_EtsysMstpMstiTable_Object=MibTable
etsysMstpMstiTable=_EtsysMstpMstiTable_Object((1,3,6,1,4,1,5624,1,2,28,1,1,4))
if mibBuilder.loadTexts:etsysMstpMstiTable.setStatus(_A)
_EtsysMstpMstiEntry_Object=MibTableRow
etsysMstpMstiEntry=_EtsysMstpMstiEntry_Object((1,3,6,1,4,1,5624,1,2,28,1,1,4,1))
etsysMstpMstiEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:etsysMstpMstiEntry.setStatus(_A)
_EtsysMstpMstId_Type=Unsigned32
_EtsysMstpMstId_Object=MibTableColumn
etsysMstpMstId=_EtsysMstpMstId_Object((1,3,6,1,4,1,5624,1,2,28,1,1,4,1,1),_EtsysMstpMstId_Type())
etsysMstpMstId.setMaxAccess(_I)
if mibBuilder.loadTexts:etsysMstpMstId.setStatus(_A)
_EtsysMstpMstiStatus_Type=RowStatus
_EtsysMstpMstiStatus_Object=MibTableColumn
etsysMstpMstiStatus=_EtsysMstpMstiStatus_Object((1,3,6,1,4,1,5624,1,2,28,1,1,4,1,2),_EtsysMstpMstiStatus_Type())
etsysMstpMstiStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:etsysMstpMstiStatus.setStatus(_A)
_EtsysMstpAllocTable_Object=MibTable
etsysMstpAllocTable=_EtsysMstpAllocTable_Object((1,3,6,1,4,1,5624,1,2,28,1,1,5))
if mibBuilder.loadTexts:etsysMstpAllocTable.setStatus(_A)
_EtsysMstpAllocEntry_Object=MibTableRow
etsysMstpAllocEntry=_EtsysMstpAllocEntry_Object((1,3,6,1,4,1,5624,1,2,28,1,1,5,1))
etsysMstpAllocEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:etsysMstpAllocEntry.setStatus(_A)
_EtsysMstpFdbId_Type=Unsigned32
_EtsysMstpFdbId_Object=MibTableColumn
etsysMstpFdbId=_EtsysMstpFdbId_Object((1,3,6,1,4,1,5624,1,2,28,1,1,5,1,1),_EtsysMstpFdbId_Type())
etsysMstpFdbId.setMaxAccess(_I)
if mibBuilder.loadTexts:etsysMstpFdbId.setStatus(_A)
class _EtsysMstpMstIdOfFdb_Type(Unsigned32):defaultValue=0
_EtsysMstpMstIdOfFdb_Type.__name__=_E
_EtsysMstpMstIdOfFdb_Object=MibTableColumn
etsysMstpMstIdOfFdb=_EtsysMstpMstIdOfFdb_Object((1,3,6,1,4,1,5624,1,2,28,1,1,5,1,2),_EtsysMstpMstIdOfFdb_Type())
etsysMstpMstIdOfFdb.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMstpMstIdOfFdb.setStatus(_A)
_EtsysMstpConfigTable_Object=MibTable
etsysMstpConfigTable=_EtsysMstpConfigTable_Object((1,3,6,1,4,1,5624,1,2,28,1,1,6))
if mibBuilder.loadTexts:etsysMstpConfigTable.setStatus(_A)
_EtsysMstpConfigEntry_Object=MibTableRow
etsysMstpConfigEntry=_EtsysMstpConfigEntry_Object((1,3,6,1,4,1,5624,1,2,28,1,1,6,1))
etsysMstpConfigEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:etsysMstpConfigEntry.setStatus(_A)
_EtsysMstpVlanId_Type=Unsigned32
_EtsysMstpVlanId_Object=MibTableColumn
etsysMstpVlanId=_EtsysMstpVlanId_Object((1,3,6,1,4,1,5624,1,2,28,1,1,6,1,1),_EtsysMstpVlanId_Type())
etsysMstpVlanId.setMaxAccess(_I)
if mibBuilder.loadTexts:etsysMstpVlanId.setStatus(_A)
_EtsysMstpMstIdOfVlan_Type=Unsigned32
_EtsysMstpMstIdOfVlan_Object=MibTableColumn
etsysMstpMstIdOfVlan=_EtsysMstpMstIdOfVlan_Object((1,3,6,1,4,1,5624,1,2,28,1,1,6,1,2),_EtsysMstpMstIdOfVlan_Type())
etsysMstpMstIdOfVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMstpMstIdOfVlan.setStatus(_A)
_EtsysMstpFormatSelector_Type=Unsigned32
_EtsysMstpFormatSelector_Object=MibScalar
etsysMstpFormatSelector=_EtsysMstpFormatSelector_Object((1,3,6,1,4,1,5624,1,2,28,1,1,7),_EtsysMstpFormatSelector_Type())
etsysMstpFormatSelector.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMstpFormatSelector.setStatus(_A)
class _EtsysMstpConfigName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EtsysMstpConfigName_Type.__name__=_L
_EtsysMstpConfigName_Object=MibScalar
etsysMstpConfigName=_EtsysMstpConfigName_Object((1,3,6,1,4,1,5624,1,2,28,1,1,8),_EtsysMstpConfigName_Type())
etsysMstpConfigName.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMstpConfigName.setStatus(_A)
class _EtsysMstpRevisionLevel_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EtsysMstpRevisionLevel_Type.__name__=_E
_EtsysMstpRevisionLevel_Object=MibScalar
etsysMstpRevisionLevel=_EtsysMstpRevisionLevel_Object((1,3,6,1,4,1,5624,1,2,28,1,1,9),_EtsysMstpRevisionLevel_Type())
etsysMstpRevisionLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMstpRevisionLevel.setStatus(_A)
class _EtsysMstpConfigDigest_Type(HexString):subtypeSpec=HexString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_EtsysMstpConfigDigest_Type.__name__=_P
_EtsysMstpConfigDigest_Object=MibScalar
etsysMstpConfigDigest=_EtsysMstpConfigDigest_Object((1,3,6,1,4,1,5624,1,2,28,1,1,10),_EtsysMstpConfigDigest_Type())
etsysMstpConfigDigest.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMstpConfigDigest.setStatus(_A)
class _EtsysMstpMaxConfigurableMsts_Type(Unsigned32):defaultValue=64
_EtsysMstpMaxConfigurableMsts_Type.__name__=_E
_EtsysMstpMaxConfigurableMsts_Object=MibScalar
etsysMstpMaxConfigurableMsts=_EtsysMstpMaxConfigurableMsts_Object((1,3,6,1,4,1,5624,1,2,28,1,1,11),_EtsysMstpMaxConfigurableMsts_Type())
etsysMstpMaxConfigurableMsts.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMstpMaxConfigurableMsts.setStatus(_A)
_EtsysMstpBridge_ObjectIdentity=ObjectIdentity
etsysMstpBridge=_EtsysMstpBridge_ObjectIdentity((1,3,6,1,4,1,5624,1,2,28,1,2))
_EtsysMstpCistRegionalRootIdentifier_Type=BridgeId
_EtsysMstpCistRegionalRootIdentifier_Object=MibScalar
etsysMstpCistRegionalRootIdentifier=_EtsysMstpCistRegionalRootIdentifier_Object((1,3,6,1,4,1,5624,1,2,28,1,2,1),_EtsysMstpCistRegionalRootIdentifier_Type())
etsysMstpCistRegionalRootIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMstpCistRegionalRootIdentifier.setStatus(_A)
_EtsysMstpCistPathCost_Type=Unsigned32
_EtsysMstpCistPathCost_Object=MibScalar
etsysMstpCistPathCost=_EtsysMstpCistPathCost_Object((1,3,6,1,4,1,5624,1,2,28,1,2,2),_EtsysMstpCistPathCost_Type())
etsysMstpCistPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMstpCistPathCost.setStatus(_A)
class _EtsysMstpMaxHopCount_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_EtsysMstpMaxHopCount_Type.__name__=_E
_EtsysMstpMaxHopCount_Object=MibScalar
etsysMstpMaxHopCount=_EtsysMstpMaxHopCount_Object((1,3,6,1,4,1,5624,1,2,28,1,2,3),_EtsysMstpMaxHopCount_Type())
etsysMstpMaxHopCount.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMstpMaxHopCount.setStatus(_A)
_EtsysMstpBridgeTable_Object=MibTable
etsysMstpBridgeTable=_EtsysMstpBridgeTable_Object((1,3,6,1,4,1,5624,1,2,28,1,2,4))
if mibBuilder.loadTexts:etsysMstpBridgeTable.setStatus(_A)
_EtsysMstpBridgeEntry_Object=MibTableRow
etsysMstpBridgeEntry=_EtsysMstpBridgeEntry_Object((1,3,6,1,4,1,5624,1,2,28,1,2,4,1))
etsysMstpBridgeEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:etsysMstpBridgeEntry.setStatus(_A)
class _EtsysMstpBridgePriority_Type(Unsigned32):defaultValue=32768;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_EtsysMstpBridgePriority_Type.__name__=_E
_EtsysMstpBridgePriority_Object=MibTableColumn
etsysMstpBridgePriority=_EtsysMstpBridgePriority_Object((1,3,6,1,4,1,5624,1,2,28,1,2,4,1,1),_EtsysMstpBridgePriority_Type())
etsysMstpBridgePriority.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMstpBridgePriority.setStatus(_A)
_EtsysMstpTimeSinceTopologyChange_Type=TimeTicks
_EtsysMstpTimeSinceTopologyChange_Object=MibTableColumn
etsysMstpTimeSinceTopologyChange=_EtsysMstpTimeSinceTopologyChange_Object((1,3,6,1,4,1,5624,1,2,28,1,2,4,1,2),_EtsysMstpTimeSinceTopologyChange_Type())
etsysMstpTimeSinceTopologyChange.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMstpTimeSinceTopologyChange.setStatus(_A)
_EtsysMstpTopologyChangeCount_Type=Counter32
_EtsysMstpTopologyChangeCount_Object=MibTableColumn
etsysMstpTopologyChangeCount=_EtsysMstpTopologyChangeCount_Object((1,3,6,1,4,1,5624,1,2,28,1,2,4,1,3),_EtsysMstpTopologyChangeCount_Type())
etsysMstpTopologyChangeCount.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMstpTopologyChangeCount.setStatus(_A)
_EtsysMstpTopologyChangeInProgress_Type=TruthValue
_EtsysMstpTopologyChangeInProgress_Object=MibTableColumn
etsysMstpTopologyChangeInProgress=_EtsysMstpTopologyChangeInProgress_Object((1,3,6,1,4,1,5624,1,2,28,1,2,4,1,4),_EtsysMstpTopologyChangeInProgress_Type())
etsysMstpTopologyChangeInProgress.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMstpTopologyChangeInProgress.setStatus(_A)
_EtsysMstpDesignatedRoot_Type=BridgeId
_EtsysMstpDesignatedRoot_Object=MibTableColumn
etsysMstpDesignatedRoot=_EtsysMstpDesignatedRoot_Object((1,3,6,1,4,1,5624,1,2,28,1,2,4,1,5),_EtsysMstpDesignatedRoot_Type())
etsysMstpDesignatedRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMstpDesignatedRoot.setStatus(_A)
_EtsysMstpRootPathCost_Type=Unsigned32
_EtsysMstpRootPathCost_Object=MibTableColumn
etsysMstpRootPathCost=_EtsysMstpRootPathCost_Object((1,3,6,1,4,1,5624,1,2,28,1,2,4,1,6),_EtsysMstpRootPathCost_Type())
etsysMstpRootPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMstpRootPathCost.setStatus(_A)
_EtsysMstpRootPort_Type=Unsigned32
_EtsysMstpRootPort_Object=MibTableColumn
etsysMstpRootPort=_EtsysMstpRootPort_Object((1,3,6,1,4,1,5624,1,2,28,1,2,4,1,7),_EtsysMstpRootPort_Type())
etsysMstpRootPort.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMstpRootPort.setStatus(_A)
_EtsysMstpPort_ObjectIdentity=ObjectIdentity
etsysMstpPort=_EtsysMstpPort_ObjectIdentity((1,3,6,1,4,1,5624,1,2,28,1,3))
_EtsysMstpPortTable_Object=MibTable
etsysMstpPortTable=_EtsysMstpPortTable_Object((1,3,6,1,4,1,5624,1,2,28,1,3,1))
if mibBuilder.loadTexts:etsysMstpPortTable.setStatus(_A)
_EtsysMstpPortEntry_Object=MibTableRow
etsysMstpPortEntry=_EtsysMstpPortEntry_Object((1,3,6,1,4,1,5624,1,2,28,1,3,1,1))
etsysMstpPortEntry.setIndexNames((0,_B,_G),(0,_B,_J))
if mibBuilder.loadTexts:etsysMstpPortEntry.setStatus(_A)
_EtsysMstpPortNumber_Type=InterfaceIndex
_EtsysMstpPortNumber_Object=MibTableColumn
etsysMstpPortNumber=_EtsysMstpPortNumber_Object((1,3,6,1,4,1,5624,1,2,28,1,3,1,1,1),_EtsysMstpPortNumber_Type())
etsysMstpPortNumber.setMaxAccess(_I)
if mibBuilder.loadTexts:etsysMstpPortNumber.setStatus(_A)
class _EtsysMstpPortPriority_Type(Unsigned32):defaultValue=128;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_EtsysMstpPortPriority_Type.__name__=_E
_EtsysMstpPortPriority_Object=MibTableColumn
etsysMstpPortPriority=_EtsysMstpPortPriority_Object((1,3,6,1,4,1,5624,1,2,28,1,3,1,1,2),_EtsysMstpPortPriority_Type())
etsysMstpPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMstpPortPriority.setStatus(_A)
class _EtsysMstpPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_Q,1),('blocking',2),('listening',3),('learning',4),('forwarding',5),('broken',6)))
_EtsysMstpPortState_Type.__name__=_H
_EtsysMstpPortState_Object=MibTableColumn
etsysMstpPortState=_EtsysMstpPortState_Object((1,3,6,1,4,1,5624,1,2,28,1,3,1,1,3),_EtsysMstpPortState_Type())
etsysMstpPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMstpPortState.setStatus(_A)
class _EtsysMstpPortAdminPathCost_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_EtsysMstpPortAdminPathCost_Type.__name__=_E
_EtsysMstpPortAdminPathCost_Object=MibTableColumn
etsysMstpPortAdminPathCost=_EtsysMstpPortAdminPathCost_Object((1,3,6,1,4,1,5624,1,2,28,1,3,1,1,4),_EtsysMstpPortAdminPathCost_Type())
etsysMstpPortAdminPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMstpPortAdminPathCost.setStatus(_A)
_EtsysMstpPortOperPathCost_Type=Unsigned32
_EtsysMstpPortOperPathCost_Object=MibTableColumn
etsysMstpPortOperPathCost=_EtsysMstpPortOperPathCost_Object((1,3,6,1,4,1,5624,1,2,28,1,3,1,1,5),_EtsysMstpPortOperPathCost_Type())
etsysMstpPortOperPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMstpPortOperPathCost.setStatus(_A)
_EtsysMstpPortDesignatedRoot_Type=BridgeId
_EtsysMstpPortDesignatedRoot_Object=MibTableColumn
etsysMstpPortDesignatedRoot=_EtsysMstpPortDesignatedRoot_Object((1,3,6,1,4,1,5624,1,2,28,1,3,1,1,6),_EtsysMstpPortDesignatedRoot_Type())
etsysMstpPortDesignatedRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMstpPortDesignatedRoot.setStatus(_A)
_EtsysMstpPortDesignatedCost_Type=Unsigned32
_EtsysMstpPortDesignatedCost_Object=MibTableColumn
etsysMstpPortDesignatedCost=_EtsysMstpPortDesignatedCost_Object((1,3,6,1,4,1,5624,1,2,28,1,3,1,1,7),_EtsysMstpPortDesignatedCost_Type())
etsysMstpPortDesignatedCost.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMstpPortDesignatedCost.setStatus(_A)
_EtsysMstpPortDesignatedBridge_Type=BridgeId
_EtsysMstpPortDesignatedBridge_Object=MibTableColumn
etsysMstpPortDesignatedBridge=_EtsysMstpPortDesignatedBridge_Object((1,3,6,1,4,1,5624,1,2,28,1,3,1,1,8),_EtsysMstpPortDesignatedBridge_Type())
etsysMstpPortDesignatedBridge.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMstpPortDesignatedBridge.setStatus(_A)
_EtsysMstpPortDesignatedPort_Type=OctetString
_EtsysMstpPortDesignatedPort_Object=MibTableColumn
etsysMstpPortDesignatedPort=_EtsysMstpPortDesignatedPort_Object((1,3,6,1,4,1,5624,1,2,28,1,3,1,1,9),_EtsysMstpPortDesignatedPort_Type())
etsysMstpPortDesignatedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMstpPortDesignatedPort.setStatus(_A)
class _EtsysMstpPortRoleValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_Q,1),('root',2),('designated',3),('alternate',4),('backUp',5),('master',6)))
_EtsysMstpPortRoleValue_Type.__name__=_H
_EtsysMstpPortRoleValue_Object=MibTableColumn
etsysMstpPortRoleValue=_EtsysMstpPortRoleValue_Object((1,3,6,1,4,1,5624,1,2,28,1,3,1,1,10),_EtsysMstpPortRoleValue_Type())
etsysMstpPortRoleValue.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMstpPortRoleValue.setStatus(_A)
_EtsysMstpGlobalPortTable_Object=MibTable
etsysMstpGlobalPortTable=_EtsysMstpGlobalPortTable_Object((1,3,6,1,4,1,5624,1,2,28,1,3,2))
if mibBuilder.loadTexts:etsysMstpGlobalPortTable.setStatus(_A)
_EtsysMstpGlobalPortEntry_Object=MibTableRow
etsysMstpGlobalPortEntry=_EtsysMstpGlobalPortEntry_Object((1,3,6,1,4,1,5624,1,2,28,1,3,2,1))
etsysMstpGlobalPortEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:etsysMstpGlobalPortEntry.setStatus(_A)
_EtsysMstpHelloTime_Type=Unsigned32
_EtsysMstpHelloTime_Object=MibTableColumn
etsysMstpHelloTime=_EtsysMstpHelloTime_Object((1,3,6,1,4,1,5624,1,2,28,1,3,2,1,1),_EtsysMstpHelloTime_Type())
etsysMstpHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMstpHelloTime.setStatus(_A)
class _EtsysMstpPortHelloTime_Type(Unsigned32):defaultValue=200;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_EtsysMstpPortHelloTime_Type.__name__=_E
_EtsysMstpPortHelloTime_Object=MibTableColumn
etsysMstpPortHelloTime=_EtsysMstpPortHelloTime_Object((1,3,6,1,4,1,5624,1,2,28,1,3,2,1,2),_EtsysMstpPortHelloTime_Type())
etsysMstpPortHelloTime.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMstpPortHelloTime.setStatus(_A)
_EtsysMstpBoundaryPort_Type=TruthValue
_EtsysMstpBoundaryPort_Object=MibTableColumn
etsysMstpBoundaryPort=_EtsysMstpBoundaryPort_Object((1,3,6,1,4,1,5624,1,2,28,1,3,2,1,3),_EtsysMstpBoundaryPort_Type())
etsysMstpBoundaryPort.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMstpBoundaryPort.setStatus(_A)
_EtsysMstpExtn_ObjectIdentity=ObjectIdentity
etsysMstpExtn=_EtsysMstpExtn_ObjectIdentity((1,3,6,1,4,1,5624,1,2,28,1,4))
class _EtsysMstpAutoEdgeDetection_Type(EnabledStatus):defaultValue=1
_EtsysMstpAutoEdgeDetection_Type.__name__=_F
_EtsysMstpAutoEdgeDetection_Object=MibScalar
etsysMstpAutoEdgeDetection=_EtsysMstpAutoEdgeDetection_Object((1,3,6,1,4,1,5624,1,2,28,1,4,1),_EtsysMstpAutoEdgeDetection_Type())
etsysMstpAutoEdgeDetection.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMstpAutoEdgeDetection.setStatus(_A)
class _EtsysMstpBridgeHelloTimeMode_Type(EnabledStatus):defaultValue=1
_EtsysMstpBridgeHelloTimeMode_Type.__name__=_F
_EtsysMstpBridgeHelloTimeMode_Object=MibScalar
etsysMstpBridgeHelloTimeMode=_EtsysMstpBridgeHelloTimeMode_Object((1,3,6,1,4,1,5624,1,2,28,1,4,2),_EtsysMstpBridgeHelloTimeMode_Type())
etsysMstpBridgeHelloTimeMode.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMstpBridgeHelloTimeMode.setStatus(_A)
_EtsysMstpMstiExtnTable_Object=MibTable
etsysMstpMstiExtnTable=_EtsysMstpMstiExtnTable_Object((1,3,6,1,4,1,5624,1,2,28,1,4,3))
if mibBuilder.loadTexts:etsysMstpMstiExtnTable.setStatus(_A)
_EtsysMstpMstiExtnEntry_Object=MibTableRow
etsysMstpMstiExtnEntry=_EtsysMstpMstiExtnEntry_Object((1,3,6,1,4,1,5624,1,2,28,1,4,3,1))
if mibBuilder.loadTexts:etsysMstpMstiExtnEntry.setStatus(_A)
class _EtsysMstpMstiExtnBackupRootEnable_Type(EnabledStatus):defaultValue=2
_EtsysMstpMstiExtnBackupRootEnable_Type.__name__=_F
_EtsysMstpMstiExtnBackupRootEnable_Object=MibTableColumn
etsysMstpMstiExtnBackupRootEnable=_EtsysMstpMstiExtnBackupRootEnable_Object((1,3,6,1,4,1,5624,1,2,28,1,4,3,1,1),_EtsysMstpMstiExtnBackupRootEnable_Type())
etsysMstpMstiExtnBackupRootEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMstpMstiExtnBackupRootEnable.setStatus(_A)
_EtsysMstpPortExtnTable_Object=MibTable
etsysMstpPortExtnTable=_EtsysMstpPortExtnTable_Object((1,3,6,1,4,1,5624,1,2,28,1,4,4))
if mibBuilder.loadTexts:etsysMstpPortExtnTable.setStatus(_A)
_EtsysMstpPortExtnEntry_Object=MibTableRow
etsysMstpPortExtnEntry=_EtsysMstpPortExtnEntry_Object((1,3,6,1,4,1,5624,1,2,28,1,4,4,1))
if mibBuilder.loadTexts:etsysMstpPortExtnEntry.setStatus(_A)
class _EtsysMstpPortExtnNonForwardingReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('none',1),('disputed',2),('spanGuardLocked',3),('loopProtectEvent',4),('loopProtectAdvisory',5),('loopbackDetected',6)))
_EtsysMstpPortExtnNonForwardingReason_Type.__name__=_H
_EtsysMstpPortExtnNonForwardingReason_Object=MibTableColumn
etsysMstpPortExtnNonForwardingReason=_EtsysMstpPortExtnNonForwardingReason_Object((1,3,6,1,4,1,5624,1,2,28,1,4,4,1,1),_EtsysMstpPortExtnNonForwardingReason_Type())
etsysMstpPortExtnNonForwardingReason.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysMstpPortExtnNonForwardingReason.setStatus(_A)
class _EtsysMstpPortExtnLoopProtectEnable_Type(EnabledStatus):defaultValue=2
_EtsysMstpPortExtnLoopProtectEnable_Type.__name__=_F
_EtsysMstpPortExtnLoopProtectEnable_Object=MibTableColumn
etsysMstpPortExtnLoopProtectEnable=_EtsysMstpPortExtnLoopProtectEnable_Object((1,3,6,1,4,1,5624,1,2,28,1,4,4,1,2),_EtsysMstpPortExtnLoopProtectEnable_Type())
etsysMstpPortExtnLoopProtectEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMstpPortExtnLoopProtectEnable.setStatus(_A)
class _EtsysMstpPortExtnLoopProtectBlocking_Type(TruthValue):defaultValue=2
_EtsysMstpPortExtnLoopProtectBlocking_Type.__name__=_M
_EtsysMstpPortExtnLoopProtectBlocking_Object=MibTableColumn
etsysMstpPortExtnLoopProtectBlocking=_EtsysMstpPortExtnLoopProtectBlocking_Object((1,3,6,1,4,1,5624,1,2,28,1,4,4,1,3),_EtsysMstpPortExtnLoopProtectBlocking_Type())
etsysMstpPortExtnLoopProtectBlocking.setMaxAccess(_D)
if mibBuilder.loadTexts:etsysMstpPortExtnLoopProtectBlocking.setStatus(_A)
_EtsysMstpConformance_ObjectIdentity=ObjectIdentity
etsysMstpConformance=_EtsysMstpConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,28,2))
_EtsysMstpGroups_ObjectIdentity=ObjectIdentity
etsysMstpGroups=_EtsysMstpGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,28,2,1))
_EtsysMstpCompliances_ObjectIdentity=ObjectIdentity
etsysMstpCompliances=_EtsysMstpCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,28,2,2))
etsysMstpMstiEntry.registerAugmentions((_B,_R))
etsysMstpMstiExtnEntry.setIndexNames(*etsysMstpMstiEntry.getIndexNames())
etsysMstpPortEntry.registerAugmentions((_B,_S))
etsysMstpPortExtnEntry.setIndexNames(*etsysMstpPortEntry.getIndexNames())
etsysMstpConfigGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,28,2,1,1))
etsysMstpConfigGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:etsysMstpConfigGroup.setStatus(_A)
etsysMstpBridgeGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,28,2,1,2))
etsysMstpBridgeGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:etsysMstpBridgeGroup.setStatus(_A)
etsysMstpPortGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,28,2,1,3))
etsysMstpPortGroup.setObjects(*((_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:etsysMstpPortGroup.setStatus(_A)
etsysMstpAutoEdgeDetectGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,28,2,1,4))
etsysMstpAutoEdgeDetectGroup.setObjects((_B,_z))
if mibBuilder.loadTexts:etsysMstpAutoEdgeDetectGroup.setStatus(_A)
etsysMstpBridgeHelloTimeGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,28,2,1,5))
etsysMstpBridgeHelloTimeGroup.setObjects((_B,_A0))
if mibBuilder.loadTexts:etsysMstpBridgeHelloTimeGroup.setStatus(_A)
etsysMstpBackupRootGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,28,2,1,6))
etsysMstpBackupRootGroup.setObjects((_B,_A1))
if mibBuilder.loadTexts:etsysMstpBackupRootGroup.setStatus(_A)
etsysMstpMaxInstancesGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,28,2,1,7))
etsysMstpMaxInstancesGroup.setObjects((_B,_A2))
if mibBuilder.loadTexts:etsysMstpMaxInstancesGroup.setStatus(_A)
etsysMstpNonForwardingReasonGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,28,2,1,8))
etsysMstpNonForwardingReasonGroup.setObjects((_B,_A3))
if mibBuilder.loadTexts:etsysMstpNonForwardingReasonGroup.setStatus(_A)
etsysMstpLoopProtectGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,28,2,1,9))
etsysMstpLoopProtectGroup.setObjects(*((_B,_A4),(_B,_K)))
if mibBuilder.loadTexts:etsysMstpLoopProtectGroup.setStatus(_A)
etsysMstpLoopProtectEvent=NotificationType((1,3,6,1,4,1,5624,1,2,28,1,0,1))
etsysMstpLoopProtectEvent.setObjects(*((_B,_G),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:etsysMstpLoopProtectEvent.setStatus(_A)
etsysMstpLoopProtectNotificationGroup=NotificationGroup((1,3,6,1,4,1,5624,1,2,28,2,1,10))
etsysMstpLoopProtectNotificationGroup.setObjects((_B,_A5))
if mibBuilder.loadTexts:etsysMstpLoopProtectNotificationGroup.setStatus(_A)
etsysMstpCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,28,2,2,1))
etsysMstpCompliance.setObjects(*((_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF)))
if mibBuilder.loadTexts:etsysMstpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_P:HexString,'etsysMstpMIB':etsysMstpMIB,'etsysMstpObjects':etsysMstpObjects,'etsysMstpNotifications':etsysMstpNotifications,_A5:etsysMstpLoopProtectEvent,'etsysMstpConfig':etsysMstpConfig,_T:etsysMstpMaxMstId,_U:etsysMstpMaxSupportedMsts,_V:etsysMstpNumMsts,'etsysMstpMstiTable':etsysMstpMstiTable,'etsysMstpMstiEntry':etsysMstpMstiEntry,_G:etsysMstpMstId,_W:etsysMstpMstiStatus,'etsysMstpAllocTable':etsysMstpAllocTable,'etsysMstpAllocEntry':etsysMstpAllocEntry,_N:etsysMstpFdbId,_X:etsysMstpMstIdOfFdb,'etsysMstpConfigTable':etsysMstpConfigTable,'etsysMstpConfigEntry':etsysMstpConfigEntry,_O:etsysMstpVlanId,_Y:etsysMstpMstIdOfVlan,_Z:etsysMstpFormatSelector,_a:etsysMstpConfigName,_b:etsysMstpRevisionLevel,_c:etsysMstpConfigDigest,_A2:etsysMstpMaxConfigurableMsts,'etsysMstpBridge':etsysMstpBridge,_d:etsysMstpCistRegionalRootIdentifier,_e:etsysMstpCistPathCost,_f:etsysMstpMaxHopCount,'etsysMstpBridgeTable':etsysMstpBridgeTable,'etsysMstpBridgeEntry':etsysMstpBridgeEntry,_g:etsysMstpBridgePriority,_h:etsysMstpTimeSinceTopologyChange,_i:etsysMstpTopologyChangeCount,_j:etsysMstpTopologyChangeInProgress,_k:etsysMstpDesignatedRoot,_l:etsysMstpRootPathCost,_m:etsysMstpRootPort,'etsysMstpPort':etsysMstpPort,'etsysMstpPortTable':etsysMstpPortTable,'etsysMstpPortEntry':etsysMstpPortEntry,_J:etsysMstpPortNumber,_n:etsysMstpPortPriority,_o:etsysMstpPortState,_p:etsysMstpPortAdminPathCost,_q:etsysMstpPortOperPathCost,_r:etsysMstpPortDesignatedRoot,_s:etsysMstpPortDesignatedCost,_t:etsysMstpPortDesignatedBridge,_u:etsysMstpPortDesignatedPort,_v:etsysMstpPortRoleValue,'etsysMstpGlobalPortTable':etsysMstpGlobalPortTable,'etsysMstpGlobalPortEntry':etsysMstpGlobalPortEntry,_w:etsysMstpHelloTime,_x:etsysMstpPortHelloTime,_y:etsysMstpBoundaryPort,'etsysMstpExtn':etsysMstpExtn,_z:etsysMstpAutoEdgeDetection,_A0:etsysMstpBridgeHelloTimeMode,'etsysMstpMstiExtnTable':etsysMstpMstiExtnTable,_R:etsysMstpMstiExtnEntry,_A1:etsysMstpMstiExtnBackupRootEnable,'etsysMstpPortExtnTable':etsysMstpPortExtnTable,_S:etsysMstpPortExtnEntry,_A3:etsysMstpPortExtnNonForwardingReason,_A4:etsysMstpPortExtnLoopProtectEnable,_K:etsysMstpPortExtnLoopProtectBlocking,'etsysMstpConformance':etsysMstpConformance,'etsysMstpGroups':etsysMstpGroups,_A6:etsysMstpConfigGroup,_A7:etsysMstpBridgeGroup,_A8:etsysMstpPortGroup,_A9:etsysMstpAutoEdgeDetectGroup,_AA:etsysMstpBridgeHelloTimeGroup,_AB:etsysMstpBackupRootGroup,_AC:etsysMstpMaxInstancesGroup,_AD:etsysMstpNonForwardingReasonGroup,_AE:etsysMstpLoopProtectGroup,_AF:etsysMstpLoopProtectNotificationGroup,'etsysMstpCompliances':etsysMstpCompliances,'etsysMstpCompliance':etsysMstpCompliance})