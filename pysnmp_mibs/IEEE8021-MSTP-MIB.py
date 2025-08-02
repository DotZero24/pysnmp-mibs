_Ao='ieee8021MstpVlanV2Group'
_An='ieee8021MstpFidToMstiV2Group'
_Am='ieee8021MstpVlanGroup'
_Al='ieee8021MstpFidToMstiGroup'
_Ak='ieee8021MstpVlanV2MstId'
_Aj='ieee8021MstpFidToMstiV2MstId'
_Ai='ieee8021MstpCistPortAutoIsolatePort'
_Ah='ieee8021MstpCistPortAutoEdgePort'
_Ag='ieee8021MstpConfigurationDigest'
_Af='ieee8021MstpRevisionLevel'
_Ae='ieee8021MstpConfigurationName'
_Ad='ieee8021MstpConfigIdFormatSelector'
_Ac='ieee8021MstpVlanMstId'
_Ab='ieee8021MstpFidToMstiMstId'
_Aa='ieee8021MstpPortAdminPathCost'
_AZ='ieee8021MstpPortDisputed'
_AY='ieee8021MstpPortRole'
_AX='ieee8021MstpPortDesignatedPort'
_AW='ieee8021MstpPortDesignatedBridge'
_AV='ieee8021MstpPortDesignatedCost'
_AU='ieee8021MstpPortDesignatedRoot'
_AT='ieee8021MstpPortPathCost'
_AS='ieee8021MstpPortPriority'
_AR='ieee8021MstpPortState'
_AQ='ieee8021MstpPortUptime'
_AP='ieee8021MstpCistPortIsL2Gp'
_AO='ieee8021MstpCistPortPseudoRootId'
_AN='ieee8021MstpCistPortEnableBPDUTx'
_AM='ieee8021MstpCistPortEnableBPDURx'
_AL='ieee8021MstpCistPortProtocolMigration'
_AK='ieee8021MstpCistPortCistPathCost'
_AJ='ieee8021MstpCistPortCistRegionalRootId'
_AI='ieee8021MstpCistPortDisputed'
_AH='ieee8021MstpCistPortRole'
_AG='ieee8021MstpCistPortRestrictedTcn'
_AF='ieee8021MstpCistPortRestrictedRole'
_AE='ieee8021MstpCistPortMacOperational'
_AD='ieee8021MstpCistPortMacEnabled'
_AC='ieee8021MstpCistPortOperEdgePort'
_AB='ieee8021MstpCistPortAdminEdgePort'
_AA='ieee8021MstpCistPortHelloTime'
_A9='ieee8021MstpCistPortTopologyChangeAck'
_A8='ieee8021MstpCistPortDesignatedRoot'
_A7='ieee8021MstpCistPortAdminPathCost'
_A6='ieee8021MstpCistPortUptime'
_A5='ieee8021MstpRowStatus'
_A4='ieee8021MstpVids3'
_A3='ieee8021MstpVids2'
_A2='ieee8021MstpVids1'
_A1='ieee8021MstpVids0'
_A0='ieee8021MstpBridgePriority'
_z='ieee8021MstpRootPort'
_y='ieee8021MstpRootPathCost'
_x='ieee8021MstpDesignatedRoot'
_w='ieee8021MstpTopologyChange'
_v='ieee8021MstpTopologyChanges'
_u='ieee8021MstpTimeSinceTopologyChange'
_t='ieee8021MstpBridgeId'
_s='ieee8021MstpCistMaxHops'
_r='ieee8021MstpCistPathCost'
_q='ieee8021MstpCistRegionalRootIdentifier'
_p='ieee8021MstpCistTopologyChange'
_o='ieee8021MstpCistBridgeIdentifier'
_n='ieee8021MstpCistPortExtensionEntry'
_m='ieee8021MstpVlanV2Id'
_l='ieee8021MstpVlanV2ComponentId'
_k='ieee8021MstpFidToMstiV2Fid'
_j='ieee8021MstpFidToMstiV2ComponentId'
_i='ieee8021MstpConfigIdComponentId'
_h='ieee8021MstpVlanId'
_g='ieee8021MstpVlanComponentId'
_f='ieee8021MstpFidToMstiFid'
_e='ieee8021MstpFidToMstiComponentId'
_d='ieee8021MstpPortNum'
_c='ieee8021MstpPortMstId'
_b='ieee8021MstpPortComponentId'
_a='backup'
_Z='designated'
_Y='alternate'
_X='ieee8021MstpCistPortNum'
_W='ieee8021MstpCistPortComponentId'
_V='read-create'
_U='ieee8021MstpId'
_T='ieee8021MstpComponentId'
_S='ieee8021MstpCistComponentId'
_R='SnmpAdminString'
_Q='ieee8021MstpCistPortExtensionGroup'
_P='ieee8021MstpConfigIdGroup'
_O='ieee8021MstpPortGroup'
_N='ieee8021MstpCistPortGroup'
_M='ieee8021MstpGroup'
_L='ieee8021MstpCistGroup'
_K='centi-seconds'
_J='TruthValue'
_I='OctetString'
_H='Unsigned32'
_G='Integer32'
_F='deprecated'
_E='not-accessible'
_D='read-write'
_C='read-only'
_B='IEEE8021-MSTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,=mibBuilder.importSymbols('BRIDGE-MIB','BridgeId')
IEEE8021BridgePortNumber,IEEE8021MstIdentifier,IEEE8021PbbComponentIdentifier,IEEE8021VlanIndex,ieee802dot1mibs=mibBuilder.importSymbols('IEEE8021-TC-MIB','IEEE8021BridgePortNumber','IEEE8021MstIdentifier','IEEE8021PbbComponentIdentifier','IEEE8021VlanIndex','ieee802dot1mibs')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_R)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_J)
ieee8021MstpMib=ModuleIdentity((1,3,111,2,802,1,1,6))
if mibBuilder.loadTexts:ieee8021MstpMib.setRevisions(('2018-06-28 00:00','2014-12-15 00:00','2012-08-10 00:00','2011-12-12 00:00','2011-03-23 00:00','2008-10-15 00:00'))
_Ieee8021MstpNotifications_ObjectIdentity=ObjectIdentity
ieee8021MstpNotifications=_Ieee8021MstpNotifications_ObjectIdentity((1,3,111,2,802,1,1,6,0))
_Ieee8021MstpObjects_ObjectIdentity=ObjectIdentity
ieee8021MstpObjects=_Ieee8021MstpObjects_ObjectIdentity((1,3,111,2,802,1,1,6,1))
_Ieee8021MstpCistTable_Object=MibTable
ieee8021MstpCistTable=_Ieee8021MstpCistTable_Object((1,3,111,2,802,1,1,6,1,1))
if mibBuilder.loadTexts:ieee8021MstpCistTable.setStatus(_A)
_Ieee8021MstpCistEntry_Object=MibTableRow
ieee8021MstpCistEntry=_Ieee8021MstpCistEntry_Object((1,3,111,2,802,1,1,6,1,1,1))
ieee8021MstpCistEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:ieee8021MstpCistEntry.setStatus(_A)
_Ieee8021MstpCistComponentId_Type=IEEE8021PbbComponentIdentifier
_Ieee8021MstpCistComponentId_Object=MibTableColumn
ieee8021MstpCistComponentId=_Ieee8021MstpCistComponentId_Object((1,3,111,2,802,1,1,6,1,1,1,1),_Ieee8021MstpCistComponentId_Type())
ieee8021MstpCistComponentId.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021MstpCistComponentId.setStatus(_A)
_Ieee8021MstpCistBridgeIdentifier_Type=BridgeId
_Ieee8021MstpCistBridgeIdentifier_Object=MibTableColumn
ieee8021MstpCistBridgeIdentifier=_Ieee8021MstpCistBridgeIdentifier_Object((1,3,111,2,802,1,1,6,1,1,1,2),_Ieee8021MstpCistBridgeIdentifier_Type())
ieee8021MstpCistBridgeIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpCistBridgeIdentifier.setStatus(_A)
_Ieee8021MstpCistTopologyChange_Type=TruthValue
_Ieee8021MstpCistTopologyChange_Object=MibTableColumn
ieee8021MstpCistTopologyChange=_Ieee8021MstpCistTopologyChange_Object((1,3,111,2,802,1,1,6,1,1,1,3),_Ieee8021MstpCistTopologyChange_Type())
ieee8021MstpCistTopologyChange.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpCistTopologyChange.setStatus(_A)
_Ieee8021MstpCistRegionalRootIdentifier_Type=BridgeId
_Ieee8021MstpCistRegionalRootIdentifier_Object=MibTableColumn
ieee8021MstpCistRegionalRootIdentifier=_Ieee8021MstpCistRegionalRootIdentifier_Object((1,3,111,2,802,1,1,6,1,1,1,4),_Ieee8021MstpCistRegionalRootIdentifier_Type())
ieee8021MstpCistRegionalRootIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpCistRegionalRootIdentifier.setStatus(_A)
class _Ieee8021MstpCistPathCost_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Ieee8021MstpCistPathCost_Type.__name__=_H
_Ieee8021MstpCistPathCost_Object=MibTableColumn
ieee8021MstpCistPathCost=_Ieee8021MstpCistPathCost_Object((1,3,111,2,802,1,1,6,1,1,1,5),_Ieee8021MstpCistPathCost_Type())
ieee8021MstpCistPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpCistPathCost.setStatus(_A)
class _Ieee8021MstpCistMaxHops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(6,40))
_Ieee8021MstpCistMaxHops_Type.__name__=_G
_Ieee8021MstpCistMaxHops_Object=MibTableColumn
ieee8021MstpCistMaxHops=_Ieee8021MstpCistMaxHops_Object((1,3,111,2,802,1,1,6,1,1,1,6),_Ieee8021MstpCistMaxHops_Type())
ieee8021MstpCistMaxHops.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021MstpCistMaxHops.setStatus(_A)
_Ieee8021MstpTable_Object=MibTable
ieee8021MstpTable=_Ieee8021MstpTable_Object((1,3,111,2,802,1,1,6,1,2))
if mibBuilder.loadTexts:ieee8021MstpTable.setStatus(_A)
_Ieee8021MstpEntry_Object=MibTableRow
ieee8021MstpEntry=_Ieee8021MstpEntry_Object((1,3,111,2,802,1,1,6,1,2,1))
ieee8021MstpEntry.setIndexNames((0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:ieee8021MstpEntry.setStatus(_A)
_Ieee8021MstpComponentId_Type=IEEE8021PbbComponentIdentifier
_Ieee8021MstpComponentId_Object=MibTableColumn
ieee8021MstpComponentId=_Ieee8021MstpComponentId_Object((1,3,111,2,802,1,1,6,1,2,1,1),_Ieee8021MstpComponentId_Type())
ieee8021MstpComponentId.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021MstpComponentId.setStatus(_A)
_Ieee8021MstpId_Type=IEEE8021MstIdentifier
_Ieee8021MstpId_Object=MibTableColumn
ieee8021MstpId=_Ieee8021MstpId_Object((1,3,111,2,802,1,1,6,1,2,1,2),_Ieee8021MstpId_Type())
ieee8021MstpId.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021MstpId.setStatus(_A)
_Ieee8021MstpBridgeId_Type=BridgeId
_Ieee8021MstpBridgeId_Object=MibTableColumn
ieee8021MstpBridgeId=_Ieee8021MstpBridgeId_Object((1,3,111,2,802,1,1,6,1,2,1,3),_Ieee8021MstpBridgeId_Type())
ieee8021MstpBridgeId.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpBridgeId.setStatus(_A)
_Ieee8021MstpTimeSinceTopologyChange_Type=TimeTicks
_Ieee8021MstpTimeSinceTopologyChange_Object=MibTableColumn
ieee8021MstpTimeSinceTopologyChange=_Ieee8021MstpTimeSinceTopologyChange_Object((1,3,111,2,802,1,1,6,1,2,1,4),_Ieee8021MstpTimeSinceTopologyChange_Type())
ieee8021MstpTimeSinceTopologyChange.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpTimeSinceTopologyChange.setStatus(_A)
if mibBuilder.loadTexts:ieee8021MstpTimeSinceTopologyChange.setUnits(_K)
_Ieee8021MstpTopologyChanges_Type=Counter64
_Ieee8021MstpTopologyChanges_Object=MibTableColumn
ieee8021MstpTopologyChanges=_Ieee8021MstpTopologyChanges_Object((1,3,111,2,802,1,1,6,1,2,1,5),_Ieee8021MstpTopologyChanges_Type())
ieee8021MstpTopologyChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpTopologyChanges.setStatus(_A)
if mibBuilder.loadTexts:ieee8021MstpTopologyChanges.setUnits('topology changes')
_Ieee8021MstpTopologyChange_Type=TruthValue
_Ieee8021MstpTopologyChange_Object=MibTableColumn
ieee8021MstpTopologyChange=_Ieee8021MstpTopologyChange_Object((1,3,111,2,802,1,1,6,1,2,1,6),_Ieee8021MstpTopologyChange_Type())
ieee8021MstpTopologyChange.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpTopologyChange.setStatus(_A)
_Ieee8021MstpDesignatedRoot_Type=BridgeId
_Ieee8021MstpDesignatedRoot_Object=MibTableColumn
ieee8021MstpDesignatedRoot=_Ieee8021MstpDesignatedRoot_Object((1,3,111,2,802,1,1,6,1,2,1,7),_Ieee8021MstpDesignatedRoot_Type())
ieee8021MstpDesignatedRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpDesignatedRoot.setStatus(_A)
_Ieee8021MstpRootPathCost_Type=Integer32
_Ieee8021MstpRootPathCost_Object=MibTableColumn
ieee8021MstpRootPathCost=_Ieee8021MstpRootPathCost_Object((1,3,111,2,802,1,1,6,1,2,1,8),_Ieee8021MstpRootPathCost_Type())
ieee8021MstpRootPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpRootPathCost.setStatus(_A)
_Ieee8021MstpRootPort_Type=IEEE8021BridgePortNumber
_Ieee8021MstpRootPort_Object=MibTableColumn
ieee8021MstpRootPort=_Ieee8021MstpRootPort_Object((1,3,111,2,802,1,1,6,1,2,1,9),_Ieee8021MstpRootPort_Type())
ieee8021MstpRootPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpRootPort.setStatus(_A)
class _Ieee8021MstpBridgePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_Ieee8021MstpBridgePriority_Type.__name__=_G
_Ieee8021MstpBridgePriority_Object=MibTableColumn
ieee8021MstpBridgePriority=_Ieee8021MstpBridgePriority_Object((1,3,111,2,802,1,1,6,1,2,1,10),_Ieee8021MstpBridgePriority_Type())
ieee8021MstpBridgePriority.setMaxAccess(_V)
if mibBuilder.loadTexts:ieee8021MstpBridgePriority.setStatus(_A)
class _Ieee8021MstpVids0_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_Ieee8021MstpVids0_Type.__name__=_I
_Ieee8021MstpVids0_Object=MibTableColumn
ieee8021MstpVids0=_Ieee8021MstpVids0_Object((1,3,111,2,802,1,1,6,1,2,1,11),_Ieee8021MstpVids0_Type())
ieee8021MstpVids0.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpVids0.setStatus(_A)
class _Ieee8021MstpVids1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_Ieee8021MstpVids1_Type.__name__=_I
_Ieee8021MstpVids1_Object=MibTableColumn
ieee8021MstpVids1=_Ieee8021MstpVids1_Object((1,3,111,2,802,1,1,6,1,2,1,12),_Ieee8021MstpVids1_Type())
ieee8021MstpVids1.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpVids1.setStatus(_A)
class _Ieee8021MstpVids2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_Ieee8021MstpVids2_Type.__name__=_I
_Ieee8021MstpVids2_Object=MibTableColumn
ieee8021MstpVids2=_Ieee8021MstpVids2_Object((1,3,111,2,802,1,1,6,1,2,1,13),_Ieee8021MstpVids2_Type())
ieee8021MstpVids2.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpVids2.setStatus(_A)
class _Ieee8021MstpVids3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(128,128));fixedLength=128
_Ieee8021MstpVids3_Type.__name__=_I
_Ieee8021MstpVids3_Object=MibTableColumn
ieee8021MstpVids3=_Ieee8021MstpVids3_Object((1,3,111,2,802,1,1,6,1,2,1,14),_Ieee8021MstpVids3_Type())
ieee8021MstpVids3.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpVids3.setStatus(_A)
_Ieee8021MstpRowStatus_Type=RowStatus
_Ieee8021MstpRowStatus_Object=MibTableColumn
ieee8021MstpRowStatus=_Ieee8021MstpRowStatus_Object((1,3,111,2,802,1,1,6,1,2,1,15),_Ieee8021MstpRowStatus_Type())
ieee8021MstpRowStatus.setMaxAccess(_V)
if mibBuilder.loadTexts:ieee8021MstpRowStatus.setStatus(_A)
_Ieee8021MstpCistPortTable_Object=MibTable
ieee8021MstpCistPortTable=_Ieee8021MstpCistPortTable_Object((1,3,111,2,802,1,1,6,1,3))
if mibBuilder.loadTexts:ieee8021MstpCistPortTable.setStatus(_A)
_Ieee8021MstpCistPortEntry_Object=MibTableRow
ieee8021MstpCistPortEntry=_Ieee8021MstpCistPortEntry_Object((1,3,111,2,802,1,1,6,1,3,1))
ieee8021MstpCistPortEntry.setIndexNames((0,_B,_W),(0,_B,_X))
if mibBuilder.loadTexts:ieee8021MstpCistPortEntry.setStatus(_A)
_Ieee8021MstpCistPortComponentId_Type=IEEE8021PbbComponentIdentifier
_Ieee8021MstpCistPortComponentId_Object=MibTableColumn
ieee8021MstpCistPortComponentId=_Ieee8021MstpCistPortComponentId_Object((1,3,111,2,802,1,1,6,1,3,1,1),_Ieee8021MstpCistPortComponentId_Type())
ieee8021MstpCistPortComponentId.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021MstpCistPortComponentId.setStatus(_A)
_Ieee8021MstpCistPortNum_Type=IEEE8021BridgePortNumber
_Ieee8021MstpCistPortNum_Object=MibTableColumn
ieee8021MstpCistPortNum=_Ieee8021MstpCistPortNum_Object((1,3,111,2,802,1,1,6,1,3,1,2),_Ieee8021MstpCistPortNum_Type())
ieee8021MstpCistPortNum.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021MstpCistPortNum.setStatus(_A)
_Ieee8021MstpCistPortUptime_Type=TimeTicks
_Ieee8021MstpCistPortUptime_Object=MibTableColumn
ieee8021MstpCistPortUptime=_Ieee8021MstpCistPortUptime_Object((1,3,111,2,802,1,1,6,1,3,1,3),_Ieee8021MstpCistPortUptime_Type())
ieee8021MstpCistPortUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpCistPortUptime.setStatus(_A)
if mibBuilder.loadTexts:ieee8021MstpCistPortUptime.setUnits(_K)
class _Ieee8021MstpCistPortAdminPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_Ieee8021MstpCistPortAdminPathCost_Type.__name__=_G
_Ieee8021MstpCistPortAdminPathCost_Object=MibTableColumn
ieee8021MstpCistPortAdminPathCost=_Ieee8021MstpCistPortAdminPathCost_Object((1,3,111,2,802,1,1,6,1,3,1,4),_Ieee8021MstpCistPortAdminPathCost_Type())
ieee8021MstpCistPortAdminPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021MstpCistPortAdminPathCost.setStatus(_A)
_Ieee8021MstpCistPortDesignatedRoot_Type=BridgeId
_Ieee8021MstpCistPortDesignatedRoot_Object=MibTableColumn
ieee8021MstpCistPortDesignatedRoot=_Ieee8021MstpCistPortDesignatedRoot_Object((1,3,111,2,802,1,1,6,1,3,1,5),_Ieee8021MstpCistPortDesignatedRoot_Type())
ieee8021MstpCistPortDesignatedRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpCistPortDesignatedRoot.setStatus(_A)
_Ieee8021MstpCistPortTopologyChangeAck_Type=TruthValue
_Ieee8021MstpCistPortTopologyChangeAck_Object=MibTableColumn
ieee8021MstpCistPortTopologyChangeAck=_Ieee8021MstpCistPortTopologyChangeAck_Object((1,3,111,2,802,1,1,6,1,3,1,6),_Ieee8021MstpCistPortTopologyChangeAck_Type())
ieee8021MstpCistPortTopologyChangeAck.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpCistPortTopologyChangeAck.setStatus(_A)
class _Ieee8021MstpCistPortHelloTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_Ieee8021MstpCistPortHelloTime_Type.__name__=_G
_Ieee8021MstpCistPortHelloTime_Object=MibTableColumn
ieee8021MstpCistPortHelloTime=_Ieee8021MstpCistPortHelloTime_Object((1,3,111,2,802,1,1,6,1,3,1,7),_Ieee8021MstpCistPortHelloTime_Type())
ieee8021MstpCistPortHelloTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpCistPortHelloTime.setStatus(_A)
if mibBuilder.loadTexts:ieee8021MstpCistPortHelloTime.setUnits(_K)
class _Ieee8021MstpCistPortAdminEdgePort_Type(TruthValue):defaultValue=2
_Ieee8021MstpCistPortAdminEdgePort_Type.__name__=_J
_Ieee8021MstpCistPortAdminEdgePort_Object=MibTableColumn
ieee8021MstpCistPortAdminEdgePort=_Ieee8021MstpCistPortAdminEdgePort_Object((1,3,111,2,802,1,1,6,1,3,1,8),_Ieee8021MstpCistPortAdminEdgePort_Type())
ieee8021MstpCistPortAdminEdgePort.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021MstpCistPortAdminEdgePort.setStatus(_A)
_Ieee8021MstpCistPortOperEdgePort_Type=TruthValue
_Ieee8021MstpCistPortOperEdgePort_Object=MibTableColumn
ieee8021MstpCistPortOperEdgePort=_Ieee8021MstpCistPortOperEdgePort_Object((1,3,111,2,802,1,1,6,1,3,1,9),_Ieee8021MstpCistPortOperEdgePort_Type())
ieee8021MstpCistPortOperEdgePort.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpCistPortOperEdgePort.setStatus(_A)
_Ieee8021MstpCistPortMacEnabled_Type=TruthValue
_Ieee8021MstpCistPortMacEnabled_Object=MibTableColumn
ieee8021MstpCistPortMacEnabled=_Ieee8021MstpCistPortMacEnabled_Object((1,3,111,2,802,1,1,6,1,3,1,10),_Ieee8021MstpCistPortMacEnabled_Type())
ieee8021MstpCistPortMacEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021MstpCistPortMacEnabled.setStatus(_A)
_Ieee8021MstpCistPortMacOperational_Type=TruthValue
_Ieee8021MstpCistPortMacOperational_Object=MibTableColumn
ieee8021MstpCistPortMacOperational=_Ieee8021MstpCistPortMacOperational_Object((1,3,111,2,802,1,1,6,1,3,1,11),_Ieee8021MstpCistPortMacOperational_Type())
ieee8021MstpCistPortMacOperational.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpCistPortMacOperational.setStatus(_A)
_Ieee8021MstpCistPortRestrictedRole_Type=TruthValue
_Ieee8021MstpCistPortRestrictedRole_Object=MibTableColumn
ieee8021MstpCistPortRestrictedRole=_Ieee8021MstpCistPortRestrictedRole_Object((1,3,111,2,802,1,1,6,1,3,1,12),_Ieee8021MstpCistPortRestrictedRole_Type())
ieee8021MstpCistPortRestrictedRole.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021MstpCistPortRestrictedRole.setStatus(_A)
_Ieee8021MstpCistPortRestrictedTcn_Type=TruthValue
_Ieee8021MstpCistPortRestrictedTcn_Object=MibTableColumn
ieee8021MstpCistPortRestrictedTcn=_Ieee8021MstpCistPortRestrictedTcn_Object((1,3,111,2,802,1,1,6,1,3,1,13),_Ieee8021MstpCistPortRestrictedTcn_Type())
ieee8021MstpCistPortRestrictedTcn.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021MstpCistPortRestrictedTcn.setStatus(_A)
class _Ieee8021MstpCistPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('root',1),(_Y,2),(_Z,3),(_a,4)))
_Ieee8021MstpCistPortRole_Type.__name__=_G
_Ieee8021MstpCistPortRole_Object=MibTableColumn
ieee8021MstpCistPortRole=_Ieee8021MstpCistPortRole_Object((1,3,111,2,802,1,1,6,1,3,1,14),_Ieee8021MstpCistPortRole_Type())
ieee8021MstpCistPortRole.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpCistPortRole.setStatus(_A)
_Ieee8021MstpCistPortDisputed_Type=TruthValue
_Ieee8021MstpCistPortDisputed_Object=MibTableColumn
ieee8021MstpCistPortDisputed=_Ieee8021MstpCistPortDisputed_Object((1,3,111,2,802,1,1,6,1,3,1,15),_Ieee8021MstpCistPortDisputed_Type())
ieee8021MstpCistPortDisputed.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpCistPortDisputed.setStatus(_A)
_Ieee8021MstpCistPortCistRegionalRootId_Type=BridgeId
_Ieee8021MstpCistPortCistRegionalRootId_Object=MibTableColumn
ieee8021MstpCistPortCistRegionalRootId=_Ieee8021MstpCistPortCistRegionalRootId_Object((1,3,111,2,802,1,1,6,1,3,1,16),_Ieee8021MstpCistPortCistRegionalRootId_Type())
ieee8021MstpCistPortCistRegionalRootId.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpCistPortCistRegionalRootId.setStatus(_A)
class _Ieee8021MstpCistPortCistPathCost_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Ieee8021MstpCistPortCistPathCost_Type.__name__=_H
_Ieee8021MstpCistPortCistPathCost_Object=MibTableColumn
ieee8021MstpCistPortCistPathCost=_Ieee8021MstpCistPortCistPathCost_Object((1,3,111,2,802,1,1,6,1,3,1,17),_Ieee8021MstpCistPortCistPathCost_Type())
ieee8021MstpCistPortCistPathCost.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpCistPortCistPathCost.setStatus(_A)
_Ieee8021MstpCistPortProtocolMigration_Type=TruthValue
_Ieee8021MstpCistPortProtocolMigration_Object=MibTableColumn
ieee8021MstpCistPortProtocolMigration=_Ieee8021MstpCistPortProtocolMigration_Object((1,3,111,2,802,1,1,6,1,3,1,18),_Ieee8021MstpCistPortProtocolMigration_Type())
ieee8021MstpCistPortProtocolMigration.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021MstpCistPortProtocolMigration.setStatus(_A)
class _Ieee8021MstpCistPortEnableBPDURx_Type(TruthValue):defaultValue=1
_Ieee8021MstpCistPortEnableBPDURx_Type.__name__=_J
_Ieee8021MstpCistPortEnableBPDURx_Object=MibTableColumn
ieee8021MstpCistPortEnableBPDURx=_Ieee8021MstpCistPortEnableBPDURx_Object((1,3,111,2,802,1,1,6,1,3,1,19),_Ieee8021MstpCistPortEnableBPDURx_Type())
ieee8021MstpCistPortEnableBPDURx.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021MstpCistPortEnableBPDURx.setStatus(_A)
class _Ieee8021MstpCistPortEnableBPDUTx_Type(TruthValue):defaultValue=1
_Ieee8021MstpCistPortEnableBPDUTx_Type.__name__=_J
_Ieee8021MstpCistPortEnableBPDUTx_Object=MibTableColumn
ieee8021MstpCistPortEnableBPDUTx=_Ieee8021MstpCistPortEnableBPDUTx_Object((1,3,111,2,802,1,1,6,1,3,1,20),_Ieee8021MstpCistPortEnableBPDUTx_Type())
ieee8021MstpCistPortEnableBPDUTx.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021MstpCistPortEnableBPDUTx.setStatus(_A)
_Ieee8021MstpCistPortPseudoRootId_Type=BridgeId
_Ieee8021MstpCistPortPseudoRootId_Object=MibTableColumn
ieee8021MstpCistPortPseudoRootId=_Ieee8021MstpCistPortPseudoRootId_Object((1,3,111,2,802,1,1,6,1,3,1,21),_Ieee8021MstpCistPortPseudoRootId_Type())
ieee8021MstpCistPortPseudoRootId.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021MstpCistPortPseudoRootId.setStatus(_A)
class _Ieee8021MstpCistPortIsL2Gp_Type(TruthValue):defaultValue=2
_Ieee8021MstpCistPortIsL2Gp_Type.__name__=_J
_Ieee8021MstpCistPortIsL2Gp_Object=MibTableColumn
ieee8021MstpCistPortIsL2Gp=_Ieee8021MstpCistPortIsL2Gp_Object((1,3,111,2,802,1,1,6,1,3,1,22),_Ieee8021MstpCistPortIsL2Gp_Type())
ieee8021MstpCistPortIsL2Gp.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021MstpCistPortIsL2Gp.setStatus(_A)
_Ieee8021MstpPortTable_Object=MibTable
ieee8021MstpPortTable=_Ieee8021MstpPortTable_Object((1,3,111,2,802,1,1,6,1,4))
if mibBuilder.loadTexts:ieee8021MstpPortTable.setStatus(_A)
_Ieee8021MstpPortEntry_Object=MibTableRow
ieee8021MstpPortEntry=_Ieee8021MstpPortEntry_Object((1,3,111,2,802,1,1,6,1,4,1))
ieee8021MstpPortEntry.setIndexNames((0,_B,_b),(0,_B,_c),(0,_B,_d))
if mibBuilder.loadTexts:ieee8021MstpPortEntry.setStatus(_A)
_Ieee8021MstpPortComponentId_Type=IEEE8021PbbComponentIdentifier
_Ieee8021MstpPortComponentId_Object=MibTableColumn
ieee8021MstpPortComponentId=_Ieee8021MstpPortComponentId_Object((1,3,111,2,802,1,1,6,1,4,1,1),_Ieee8021MstpPortComponentId_Type())
ieee8021MstpPortComponentId.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021MstpPortComponentId.setStatus(_A)
_Ieee8021MstpPortMstId_Type=IEEE8021MstIdentifier
_Ieee8021MstpPortMstId_Object=MibTableColumn
ieee8021MstpPortMstId=_Ieee8021MstpPortMstId_Object((1,3,111,2,802,1,1,6,1,4,1,2),_Ieee8021MstpPortMstId_Type())
ieee8021MstpPortMstId.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021MstpPortMstId.setStatus(_A)
_Ieee8021MstpPortNum_Type=IEEE8021BridgePortNumber
_Ieee8021MstpPortNum_Object=MibTableColumn
ieee8021MstpPortNum=_Ieee8021MstpPortNum_Object((1,3,111,2,802,1,1,6,1,4,1,3),_Ieee8021MstpPortNum_Type())
ieee8021MstpPortNum.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021MstpPortNum.setStatus(_A)
_Ieee8021MstpPortUptime_Type=TimeTicks
_Ieee8021MstpPortUptime_Object=MibTableColumn
ieee8021MstpPortUptime=_Ieee8021MstpPortUptime_Object((1,3,111,2,802,1,1,6,1,4,1,4),_Ieee8021MstpPortUptime_Type())
ieee8021MstpPortUptime.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpPortUptime.setStatus(_A)
if mibBuilder.loadTexts:ieee8021MstpPortUptime.setUnits(_K)
class _Ieee8021MstpPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('disabled',1),('listening',2),('learning',3),('forwarding',4),('blocking',5)))
_Ieee8021MstpPortState_Type.__name__=_G
_Ieee8021MstpPortState_Object=MibTableColumn
ieee8021MstpPortState=_Ieee8021MstpPortState_Object((1,3,111,2,802,1,1,6,1,4,1,5),_Ieee8021MstpPortState_Type())
ieee8021MstpPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpPortState.setStatus(_A)
class _Ieee8021MstpPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_Ieee8021MstpPortPriority_Type.__name__=_G
_Ieee8021MstpPortPriority_Object=MibTableColumn
ieee8021MstpPortPriority=_Ieee8021MstpPortPriority_Object((1,3,111,2,802,1,1,6,1,4,1,6),_Ieee8021MstpPortPriority_Type())
ieee8021MstpPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021MstpPortPriority.setStatus(_A)
class _Ieee8021MstpPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_Ieee8021MstpPortPathCost_Type.__name__=_G
_Ieee8021MstpPortPathCost_Object=MibTableColumn
ieee8021MstpPortPathCost=_Ieee8021MstpPortPathCost_Object((1,3,111,2,802,1,1,6,1,4,1,7),_Ieee8021MstpPortPathCost_Type())
ieee8021MstpPortPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021MstpPortPathCost.setStatus(_A)
_Ieee8021MstpPortDesignatedRoot_Type=BridgeId
_Ieee8021MstpPortDesignatedRoot_Object=MibTableColumn
ieee8021MstpPortDesignatedRoot=_Ieee8021MstpPortDesignatedRoot_Object((1,3,111,2,802,1,1,6,1,4,1,8),_Ieee8021MstpPortDesignatedRoot_Type())
ieee8021MstpPortDesignatedRoot.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpPortDesignatedRoot.setStatus(_A)
_Ieee8021MstpPortDesignatedCost_Type=Integer32
_Ieee8021MstpPortDesignatedCost_Object=MibTableColumn
ieee8021MstpPortDesignatedCost=_Ieee8021MstpPortDesignatedCost_Object((1,3,111,2,802,1,1,6,1,4,1,9),_Ieee8021MstpPortDesignatedCost_Type())
ieee8021MstpPortDesignatedCost.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpPortDesignatedCost.setStatus(_A)
_Ieee8021MstpPortDesignatedBridge_Type=BridgeId
_Ieee8021MstpPortDesignatedBridge_Object=MibTableColumn
ieee8021MstpPortDesignatedBridge=_Ieee8021MstpPortDesignatedBridge_Object((1,3,111,2,802,1,1,6,1,4,1,10),_Ieee8021MstpPortDesignatedBridge_Type())
ieee8021MstpPortDesignatedBridge.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpPortDesignatedBridge.setStatus(_A)
_Ieee8021MstpPortDesignatedPort_Type=IEEE8021BridgePortNumber
_Ieee8021MstpPortDesignatedPort_Object=MibTableColumn
ieee8021MstpPortDesignatedPort=_Ieee8021MstpPortDesignatedPort_Object((1,3,111,2,802,1,1,6,1,4,1,11),_Ieee8021MstpPortDesignatedPort_Type())
ieee8021MstpPortDesignatedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpPortDesignatedPort.setStatus(_A)
class _Ieee8021MstpPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('root',1),(_Y,2),(_Z,3),(_a,4)))
_Ieee8021MstpPortRole_Type.__name__=_G
_Ieee8021MstpPortRole_Object=MibTableColumn
ieee8021MstpPortRole=_Ieee8021MstpPortRole_Object((1,3,111,2,802,1,1,6,1,4,1,12),_Ieee8021MstpPortRole_Type())
ieee8021MstpPortRole.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpPortRole.setStatus(_A)
_Ieee8021MstpPortDisputed_Type=TruthValue
_Ieee8021MstpPortDisputed_Object=MibTableColumn
ieee8021MstpPortDisputed=_Ieee8021MstpPortDisputed_Object((1,3,111,2,802,1,1,6,1,4,1,13),_Ieee8021MstpPortDisputed_Type())
ieee8021MstpPortDisputed.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpPortDisputed.setStatus(_A)
class _Ieee8021MstpPortAdminPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_Ieee8021MstpPortAdminPathCost_Type.__name__=_G
_Ieee8021MstpPortAdminPathCost_Object=MibTableColumn
ieee8021MstpPortAdminPathCost=_Ieee8021MstpPortAdminPathCost_Object((1,3,111,2,802,1,1,6,1,4,1,14),_Ieee8021MstpPortAdminPathCost_Type())
ieee8021MstpPortAdminPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021MstpPortAdminPathCost.setStatus(_A)
_Ieee8021MstpFidToMstiTable_Object=MibTable
ieee8021MstpFidToMstiTable=_Ieee8021MstpFidToMstiTable_Object((1,3,111,2,802,1,1,6,1,5))
if mibBuilder.loadTexts:ieee8021MstpFidToMstiTable.setStatus(_F)
_Ieee8021MstpFidToMstiEntry_Object=MibTableRow
ieee8021MstpFidToMstiEntry=_Ieee8021MstpFidToMstiEntry_Object((1,3,111,2,802,1,1,6,1,5,1))
ieee8021MstpFidToMstiEntry.setIndexNames((0,_B,_e),(0,_B,_f))
if mibBuilder.loadTexts:ieee8021MstpFidToMstiEntry.setStatus(_F)
_Ieee8021MstpFidToMstiComponentId_Type=IEEE8021PbbComponentIdentifier
_Ieee8021MstpFidToMstiComponentId_Object=MibTableColumn
ieee8021MstpFidToMstiComponentId=_Ieee8021MstpFidToMstiComponentId_Object((1,3,111,2,802,1,1,6,1,5,1,1),_Ieee8021MstpFidToMstiComponentId_Type())
ieee8021MstpFidToMstiComponentId.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021MstpFidToMstiComponentId.setStatus(_F)
class _Ieee8021MstpFidToMstiFid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_Ieee8021MstpFidToMstiFid_Type.__name__=_H
_Ieee8021MstpFidToMstiFid_Object=MibTableColumn
ieee8021MstpFidToMstiFid=_Ieee8021MstpFidToMstiFid_Object((1,3,111,2,802,1,1,6,1,5,1,2),_Ieee8021MstpFidToMstiFid_Type())
ieee8021MstpFidToMstiFid.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021MstpFidToMstiFid.setStatus(_F)
_Ieee8021MstpFidToMstiMstId_Type=IEEE8021MstIdentifier
_Ieee8021MstpFidToMstiMstId_Object=MibTableColumn
ieee8021MstpFidToMstiMstId=_Ieee8021MstpFidToMstiMstId_Object((1,3,111,2,802,1,1,6,1,5,1,3),_Ieee8021MstpFidToMstiMstId_Type())
ieee8021MstpFidToMstiMstId.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021MstpFidToMstiMstId.setStatus(_F)
_Ieee8021MstpVlanTable_Object=MibTable
ieee8021MstpVlanTable=_Ieee8021MstpVlanTable_Object((1,3,111,2,802,1,1,6,1,6))
if mibBuilder.loadTexts:ieee8021MstpVlanTable.setStatus(_F)
_Ieee8021MstpVlanEntry_Object=MibTableRow
ieee8021MstpVlanEntry=_Ieee8021MstpVlanEntry_Object((1,3,111,2,802,1,1,6,1,6,1))
ieee8021MstpVlanEntry.setIndexNames((0,_B,_g),(0,_B,_h))
if mibBuilder.loadTexts:ieee8021MstpVlanEntry.setStatus(_F)
_Ieee8021MstpVlanComponentId_Type=IEEE8021PbbComponentIdentifier
_Ieee8021MstpVlanComponentId_Object=MibTableColumn
ieee8021MstpVlanComponentId=_Ieee8021MstpVlanComponentId_Object((1,3,111,2,802,1,1,6,1,6,1,1),_Ieee8021MstpVlanComponentId_Type())
ieee8021MstpVlanComponentId.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021MstpVlanComponentId.setStatus(_F)
_Ieee8021MstpVlanId_Type=IEEE8021VlanIndex
_Ieee8021MstpVlanId_Object=MibTableColumn
ieee8021MstpVlanId=_Ieee8021MstpVlanId_Object((1,3,111,2,802,1,1,6,1,6,1,2),_Ieee8021MstpVlanId_Type())
ieee8021MstpVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021MstpVlanId.setStatus(_F)
_Ieee8021MstpVlanMstId_Type=IEEE8021MstIdentifier
_Ieee8021MstpVlanMstId_Object=MibTableColumn
ieee8021MstpVlanMstId=_Ieee8021MstpVlanMstId_Object((1,3,111,2,802,1,1,6,1,6,1,3),_Ieee8021MstpVlanMstId_Type())
ieee8021MstpVlanMstId.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpVlanMstId.setStatus(_F)
_Ieee8021MstpConfigIdTable_Object=MibTable
ieee8021MstpConfigIdTable=_Ieee8021MstpConfigIdTable_Object((1,3,111,2,802,1,1,6,1,7))
if mibBuilder.loadTexts:ieee8021MstpConfigIdTable.setStatus(_A)
_Ieee8021MstpConfigIdEntry_Object=MibTableRow
ieee8021MstpConfigIdEntry=_Ieee8021MstpConfigIdEntry_Object((1,3,111,2,802,1,1,6,1,7,1))
ieee8021MstpConfigIdEntry.setIndexNames((0,_B,_i))
if mibBuilder.loadTexts:ieee8021MstpConfigIdEntry.setStatus(_A)
_Ieee8021MstpConfigIdComponentId_Type=IEEE8021PbbComponentIdentifier
_Ieee8021MstpConfigIdComponentId_Object=MibTableColumn
ieee8021MstpConfigIdComponentId=_Ieee8021MstpConfigIdComponentId_Object((1,3,111,2,802,1,1,6,1,7,1,1),_Ieee8021MstpConfigIdComponentId_Type())
ieee8021MstpConfigIdComponentId.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021MstpConfigIdComponentId.setStatus(_A)
class _Ieee8021MstpConfigIdFormatSelector_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_Ieee8021MstpConfigIdFormatSelector_Type.__name__=_G
_Ieee8021MstpConfigIdFormatSelector_Object=MibTableColumn
ieee8021MstpConfigIdFormatSelector=_Ieee8021MstpConfigIdFormatSelector_Object((1,3,111,2,802,1,1,6,1,7,1,2),_Ieee8021MstpConfigIdFormatSelector_Type())
ieee8021MstpConfigIdFormatSelector.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021MstpConfigIdFormatSelector.setStatus(_A)
class _Ieee8021MstpConfigurationName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_Ieee8021MstpConfigurationName_Type.__name__=_R
_Ieee8021MstpConfigurationName_Object=MibTableColumn
ieee8021MstpConfigurationName=_Ieee8021MstpConfigurationName_Object((1,3,111,2,802,1,1,6,1,7,1,3),_Ieee8021MstpConfigurationName_Type())
ieee8021MstpConfigurationName.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021MstpConfigurationName.setStatus(_A)
class _Ieee8021MstpRevisionLevel_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Ieee8021MstpRevisionLevel_Type.__name__=_H
_Ieee8021MstpRevisionLevel_Object=MibTableColumn
ieee8021MstpRevisionLevel=_Ieee8021MstpRevisionLevel_Object((1,3,111,2,802,1,1,6,1,7,1,4),_Ieee8021MstpRevisionLevel_Type())
ieee8021MstpRevisionLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021MstpRevisionLevel.setStatus(_A)
class _Ieee8021MstpConfigurationDigest_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_Ieee8021MstpConfigurationDigest_Type.__name__=_I
_Ieee8021MstpConfigurationDigest_Object=MibTableColumn
ieee8021MstpConfigurationDigest=_Ieee8021MstpConfigurationDigest_Object((1,3,111,2,802,1,1,6,1,7,1,5),_Ieee8021MstpConfigurationDigest_Type())
ieee8021MstpConfigurationDigest.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpConfigurationDigest.setStatus(_A)
_Ieee8021MstpCistPortExtensionTable_Object=MibTable
ieee8021MstpCistPortExtensionTable=_Ieee8021MstpCistPortExtensionTable_Object((1,3,111,2,802,1,1,6,1,8))
if mibBuilder.loadTexts:ieee8021MstpCistPortExtensionTable.setStatus(_A)
_Ieee8021MstpCistPortExtensionEntry_Object=MibTableRow
ieee8021MstpCistPortExtensionEntry=_Ieee8021MstpCistPortExtensionEntry_Object((1,3,111,2,802,1,1,6,1,8,1))
if mibBuilder.loadTexts:ieee8021MstpCistPortExtensionEntry.setStatus(_A)
_Ieee8021MstpCistPortAutoEdgePort_Type=TruthValue
_Ieee8021MstpCistPortAutoEdgePort_Object=MibTableColumn
ieee8021MstpCistPortAutoEdgePort=_Ieee8021MstpCistPortAutoEdgePort_Object((1,3,111,2,802,1,1,6,1,8,1,1),_Ieee8021MstpCistPortAutoEdgePort_Type())
ieee8021MstpCistPortAutoEdgePort.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021MstpCistPortAutoEdgePort.setStatus(_A)
_Ieee8021MstpCistPortAutoIsolatePort_Type=TruthValue
_Ieee8021MstpCistPortAutoIsolatePort_Object=MibTableColumn
ieee8021MstpCistPortAutoIsolatePort=_Ieee8021MstpCistPortAutoIsolatePort_Object((1,3,111,2,802,1,1,6,1,8,1,2),_Ieee8021MstpCistPortAutoIsolatePort_Type())
ieee8021MstpCistPortAutoIsolatePort.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpCistPortAutoIsolatePort.setStatus(_A)
_Ieee8021MstpFidToMstiV2Table_Object=MibTable
ieee8021MstpFidToMstiV2Table=_Ieee8021MstpFidToMstiV2Table_Object((1,3,111,2,802,1,1,6,1,9))
if mibBuilder.loadTexts:ieee8021MstpFidToMstiV2Table.setStatus(_A)
_Ieee8021MstpFidToMstiV2Entry_Object=MibTableRow
ieee8021MstpFidToMstiV2Entry=_Ieee8021MstpFidToMstiV2Entry_Object((1,3,111,2,802,1,1,6,1,9,1))
ieee8021MstpFidToMstiV2Entry.setIndexNames((0,_B,_j),(0,_B,_k))
if mibBuilder.loadTexts:ieee8021MstpFidToMstiV2Entry.setStatus(_A)
_Ieee8021MstpFidToMstiV2ComponentId_Type=IEEE8021PbbComponentIdentifier
_Ieee8021MstpFidToMstiV2ComponentId_Object=MibTableColumn
ieee8021MstpFidToMstiV2ComponentId=_Ieee8021MstpFidToMstiV2ComponentId_Object((1,3,111,2,802,1,1,6,1,9,1,1),_Ieee8021MstpFidToMstiV2ComponentId_Type())
ieee8021MstpFidToMstiV2ComponentId.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021MstpFidToMstiV2ComponentId.setStatus(_A)
class _Ieee8021MstpFidToMstiV2Fid_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_Ieee8021MstpFidToMstiV2Fid_Type.__name__=_H
_Ieee8021MstpFidToMstiV2Fid_Object=MibTableColumn
ieee8021MstpFidToMstiV2Fid=_Ieee8021MstpFidToMstiV2Fid_Object((1,3,111,2,802,1,1,6,1,9,1,2),_Ieee8021MstpFidToMstiV2Fid_Type())
ieee8021MstpFidToMstiV2Fid.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021MstpFidToMstiV2Fid.setStatus(_A)
class _Ieee8021MstpFidToMstiV2MstId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_Ieee8021MstpFidToMstiV2MstId_Type.__name__=_H
_Ieee8021MstpFidToMstiV2MstId_Object=MibTableColumn
ieee8021MstpFidToMstiV2MstId=_Ieee8021MstpFidToMstiV2MstId_Object((1,3,111,2,802,1,1,6,1,9,1,3),_Ieee8021MstpFidToMstiV2MstId_Type())
ieee8021MstpFidToMstiV2MstId.setMaxAccess(_D)
if mibBuilder.loadTexts:ieee8021MstpFidToMstiV2MstId.setStatus(_A)
_Ieee8021MstpVlanV2Table_Object=MibTable
ieee8021MstpVlanV2Table=_Ieee8021MstpVlanV2Table_Object((1,3,111,2,802,1,1,6,1,10))
if mibBuilder.loadTexts:ieee8021MstpVlanV2Table.setStatus(_A)
_Ieee8021MstpVlanV2Entry_Object=MibTableRow
ieee8021MstpVlanV2Entry=_Ieee8021MstpVlanV2Entry_Object((1,3,111,2,802,1,1,6,1,10,1))
ieee8021MstpVlanV2Entry.setIndexNames((0,_B,_l),(0,_B,_m))
if mibBuilder.loadTexts:ieee8021MstpVlanV2Entry.setStatus(_A)
_Ieee8021MstpVlanV2ComponentId_Type=IEEE8021PbbComponentIdentifier
_Ieee8021MstpVlanV2ComponentId_Object=MibTableColumn
ieee8021MstpVlanV2ComponentId=_Ieee8021MstpVlanV2ComponentId_Object((1,3,111,2,802,1,1,6,1,10,1,1),_Ieee8021MstpVlanV2ComponentId_Type())
ieee8021MstpVlanV2ComponentId.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021MstpVlanV2ComponentId.setStatus(_A)
_Ieee8021MstpVlanV2Id_Type=IEEE8021VlanIndex
_Ieee8021MstpVlanV2Id_Object=MibTableColumn
ieee8021MstpVlanV2Id=_Ieee8021MstpVlanV2Id_Object((1,3,111,2,802,1,1,6,1,10,1,2),_Ieee8021MstpVlanV2Id_Type())
ieee8021MstpVlanV2Id.setMaxAccess(_E)
if mibBuilder.loadTexts:ieee8021MstpVlanV2Id.setStatus(_A)
class _Ieee8021MstpVlanV2MstId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_Ieee8021MstpVlanV2MstId_Type.__name__=_H
_Ieee8021MstpVlanV2MstId_Object=MibTableColumn
ieee8021MstpVlanV2MstId=_Ieee8021MstpVlanV2MstId_Object((1,3,111,2,802,1,1,6,1,10,1,3),_Ieee8021MstpVlanV2MstId_Type())
ieee8021MstpVlanV2MstId.setMaxAccess(_C)
if mibBuilder.loadTexts:ieee8021MstpVlanV2MstId.setStatus(_A)
_Ieee8021MstpConformance_ObjectIdentity=ObjectIdentity
ieee8021MstpConformance=_Ieee8021MstpConformance_ObjectIdentity((1,3,111,2,802,1,1,6,2))
_Ieee8021MstpGroups_ObjectIdentity=ObjectIdentity
ieee8021MstpGroups=_Ieee8021MstpGroups_ObjectIdentity((1,3,111,2,802,1,1,6,2,1))
_Ieee8021MstpCompliances_ObjectIdentity=ObjectIdentity
ieee8021MstpCompliances=_Ieee8021MstpCompliances_ObjectIdentity((1,3,111,2,802,1,1,6,2,2))
ieee8021MstpCistPortEntry.registerAugmentions((_B,_n))
ieee8021MstpCistPortExtensionEntry.setIndexNames(*ieee8021MstpCistPortEntry.getIndexNames())
ieee8021MstpCistGroup=ObjectGroup((1,3,111,2,802,1,1,6,2,1,1))
ieee8021MstpCistGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:ieee8021MstpCistGroup.setStatus(_A)
ieee8021MstpGroup=ObjectGroup((1,3,111,2,802,1,1,6,2,1,2))
ieee8021MstpGroup.setObjects(*((_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:ieee8021MstpGroup.setStatus(_A)
ieee8021MstpCistPortGroup=ObjectGroup((1,3,111,2,802,1,1,6,2,1,3))
ieee8021MstpCistPortGroup.setObjects(*((_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP)))
if mibBuilder.loadTexts:ieee8021MstpCistPortGroup.setStatus(_A)
ieee8021MstpPortGroup=ObjectGroup((1,3,111,2,802,1,1,6,2,1,4))
ieee8021MstpPortGroup.setObjects(*((_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa)))
if mibBuilder.loadTexts:ieee8021MstpPortGroup.setStatus(_A)
ieee8021MstpFidToMstiGroup=ObjectGroup((1,3,111,2,802,1,1,6,2,1,5))
ieee8021MstpFidToMstiGroup.setObjects((_B,_Ab))
if mibBuilder.loadTexts:ieee8021MstpFidToMstiGroup.setStatus(_F)
ieee8021MstpVlanGroup=ObjectGroup((1,3,111,2,802,1,1,6,2,1,6))
ieee8021MstpVlanGroup.setObjects((_B,_Ac))
if mibBuilder.loadTexts:ieee8021MstpVlanGroup.setStatus(_F)
ieee8021MstpConfigIdGroup=ObjectGroup((1,3,111,2,802,1,1,6,2,1,7))
ieee8021MstpConfigIdGroup.setObjects(*((_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag)))
if mibBuilder.loadTexts:ieee8021MstpConfigIdGroup.setStatus(_A)
ieee8021MstpCistPortExtensionGroup=ObjectGroup((1,3,111,2,802,1,1,6,2,1,8))
ieee8021MstpCistPortExtensionGroup.setObjects(*((_B,_Ah),(_B,_Ai)))
if mibBuilder.loadTexts:ieee8021MstpCistPortExtensionGroup.setStatus(_A)
ieee8021MstpFidToMstiV2Group=ObjectGroup((1,3,111,2,802,1,1,6,2,1,9))
ieee8021MstpFidToMstiV2Group.setObjects((_B,_Aj))
if mibBuilder.loadTexts:ieee8021MstpFidToMstiV2Group.setStatus(_A)
ieee8021MstpVlanV2Group=ObjectGroup((1,3,111,2,802,1,1,6,2,1,10))
ieee8021MstpVlanV2Group.setObjects((_B,_Ak))
if mibBuilder.loadTexts:ieee8021MstpVlanV2Group.setStatus(_A)
ieee8021MstpCompliance=ModuleCompliance((1,3,111,2,802,1,1,6,2,2,1))
ieee8021MstpCompliance.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_Al),(_B,_Am),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:ieee8021MstpCompliance.setStatus(_F)
ieee8021MstpComplianceV2=ModuleCompliance((1,3,111,2,802,1,1,6,2,2,2))
ieee8021MstpComplianceV2.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_An),(_B,_Ao),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:ieee8021MstpComplianceV2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ieee8021MstpMib':ieee8021MstpMib,'ieee8021MstpNotifications':ieee8021MstpNotifications,'ieee8021MstpObjects':ieee8021MstpObjects,'ieee8021MstpCistTable':ieee8021MstpCistTable,'ieee8021MstpCistEntry':ieee8021MstpCistEntry,_S:ieee8021MstpCistComponentId,_o:ieee8021MstpCistBridgeIdentifier,_p:ieee8021MstpCistTopologyChange,_q:ieee8021MstpCistRegionalRootIdentifier,_r:ieee8021MstpCistPathCost,_s:ieee8021MstpCistMaxHops,'ieee8021MstpTable':ieee8021MstpTable,'ieee8021MstpEntry':ieee8021MstpEntry,_T:ieee8021MstpComponentId,_U:ieee8021MstpId,_t:ieee8021MstpBridgeId,_u:ieee8021MstpTimeSinceTopologyChange,_v:ieee8021MstpTopologyChanges,_w:ieee8021MstpTopologyChange,_x:ieee8021MstpDesignatedRoot,_y:ieee8021MstpRootPathCost,_z:ieee8021MstpRootPort,_A0:ieee8021MstpBridgePriority,_A1:ieee8021MstpVids0,_A2:ieee8021MstpVids1,_A3:ieee8021MstpVids2,_A4:ieee8021MstpVids3,_A5:ieee8021MstpRowStatus,'ieee8021MstpCistPortTable':ieee8021MstpCistPortTable,'ieee8021MstpCistPortEntry':ieee8021MstpCistPortEntry,_W:ieee8021MstpCistPortComponentId,_X:ieee8021MstpCistPortNum,_A6:ieee8021MstpCistPortUptime,_A7:ieee8021MstpCistPortAdminPathCost,_A8:ieee8021MstpCistPortDesignatedRoot,_A9:ieee8021MstpCistPortTopologyChangeAck,_AA:ieee8021MstpCistPortHelloTime,_AB:ieee8021MstpCistPortAdminEdgePort,_AC:ieee8021MstpCistPortOperEdgePort,_AD:ieee8021MstpCistPortMacEnabled,_AE:ieee8021MstpCistPortMacOperational,_AF:ieee8021MstpCistPortRestrictedRole,_AG:ieee8021MstpCistPortRestrictedTcn,_AH:ieee8021MstpCistPortRole,_AI:ieee8021MstpCistPortDisputed,_AJ:ieee8021MstpCistPortCistRegionalRootId,_AK:ieee8021MstpCistPortCistPathCost,_AL:ieee8021MstpCistPortProtocolMigration,_AM:ieee8021MstpCistPortEnableBPDURx,_AN:ieee8021MstpCistPortEnableBPDUTx,_AO:ieee8021MstpCistPortPseudoRootId,_AP:ieee8021MstpCistPortIsL2Gp,'ieee8021MstpPortTable':ieee8021MstpPortTable,'ieee8021MstpPortEntry':ieee8021MstpPortEntry,_b:ieee8021MstpPortComponentId,_c:ieee8021MstpPortMstId,_d:ieee8021MstpPortNum,_AQ:ieee8021MstpPortUptime,_AR:ieee8021MstpPortState,_AS:ieee8021MstpPortPriority,_AT:ieee8021MstpPortPathCost,_AU:ieee8021MstpPortDesignatedRoot,_AV:ieee8021MstpPortDesignatedCost,_AW:ieee8021MstpPortDesignatedBridge,_AX:ieee8021MstpPortDesignatedPort,_AY:ieee8021MstpPortRole,_AZ:ieee8021MstpPortDisputed,_Aa:ieee8021MstpPortAdminPathCost,'ieee8021MstpFidToMstiTable':ieee8021MstpFidToMstiTable,'ieee8021MstpFidToMstiEntry':ieee8021MstpFidToMstiEntry,_e:ieee8021MstpFidToMstiComponentId,_f:ieee8021MstpFidToMstiFid,_Ab:ieee8021MstpFidToMstiMstId,'ieee8021MstpVlanTable':ieee8021MstpVlanTable,'ieee8021MstpVlanEntry':ieee8021MstpVlanEntry,_g:ieee8021MstpVlanComponentId,_h:ieee8021MstpVlanId,_Ac:ieee8021MstpVlanMstId,'ieee8021MstpConfigIdTable':ieee8021MstpConfigIdTable,'ieee8021MstpConfigIdEntry':ieee8021MstpConfigIdEntry,_i:ieee8021MstpConfigIdComponentId,_Ad:ieee8021MstpConfigIdFormatSelector,_Ae:ieee8021MstpConfigurationName,_Af:ieee8021MstpRevisionLevel,_Ag:ieee8021MstpConfigurationDigest,'ieee8021MstpCistPortExtensionTable':ieee8021MstpCistPortExtensionTable,_n:ieee8021MstpCistPortExtensionEntry,_Ah:ieee8021MstpCistPortAutoEdgePort,_Ai:ieee8021MstpCistPortAutoIsolatePort,'ieee8021MstpFidToMstiV2Table':ieee8021MstpFidToMstiV2Table,'ieee8021MstpFidToMstiV2Entry':ieee8021MstpFidToMstiV2Entry,_j:ieee8021MstpFidToMstiV2ComponentId,_k:ieee8021MstpFidToMstiV2Fid,_Aj:ieee8021MstpFidToMstiV2MstId,'ieee8021MstpVlanV2Table':ieee8021MstpVlanV2Table,'ieee8021MstpVlanV2Entry':ieee8021MstpVlanV2Entry,_l:ieee8021MstpVlanV2ComponentId,_m:ieee8021MstpVlanV2Id,_Ak:ieee8021MstpVlanV2MstId,'ieee8021MstpConformance':ieee8021MstpConformance,'ieee8021MstpGroups':ieee8021MstpGroups,_L:ieee8021MstpCistGroup,_M:ieee8021MstpGroup,_N:ieee8021MstpCistPortGroup,_O:ieee8021MstpPortGroup,_Al:ieee8021MstpFidToMstiGroup,_Am:ieee8021MstpVlanGroup,_P:ieee8021MstpConfigIdGroup,_Q:ieee8021MstpCistPortExtensionGroup,_An:ieee8021MstpFidToMstiV2Group,_Ao:ieee8021MstpVlanV2Group,'ieee8021MstpCompliances':ieee8021MstpCompliances,'ieee8021MstpCompliance':ieee8021MstpCompliance,'ieee8021MstpComplianceV2':ieee8021MstpComplianceV2})