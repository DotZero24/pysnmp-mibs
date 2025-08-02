_A4='nnMstConfigDigest'
_A3='nnMstRegionVersion'
_A2='nnMstRegionName'
_A1='nnMstConfigIdSel'
_A0='nnMstPortNotificationMigrationType'
_z='nnMstForceProtocolVersion'
_y='nnMstBridgeRegionalRoot'
_x='nnMstBridgeOldDesignatedRoot'
_w='nnMstErrNotificationType'
_v='nnMstGenNotificationType'
_u='nnMstBridgeInstId'
_t='nnMstPortNotificationIndex'
_s='master'
_r='nnMstPort'
_q='acknowledged'
_p='propagating'
_o='notifiedtc'
_n='notifiedtcn'
_m='detected'
_l='active'
_k='inactive'
_j='activeport'
_i='blockedport'
_h='blockport'
_g='present'
_f='repeatdesg'
_e='superiordesg'
_d='update'
_c='sendstp'
_b='sendrstp'
_a='nnMstCistPort'
_Z='roleselection'
_Y='initbridge'
_X='stpCompatible'
_W='receive'
_V='none'
_U='read-create'
_T='nnMstBridgeInstance'
_S='designated'
_R='backup'
_Q='alternate'
_P='enabled'
_O='forwarding'
_N='learning'
_M='discarding'
_L='Timeout'
_K='init'
_J='not-accessible'
_I='root'
_H='nnMstBrgAddress'
_G='OctetString'
_F='disabled'
_E='NORTEL-NETWORKS-MULTIPLE-SPANNING-TREE-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
BridgeId,Timeout=mibBuilder.importSymbols('BRIDGE-MIB','BridgeId',_L)
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
nnMultipleSpanningTreeMib=ModuleIdentity((1,3,6,1,4,1,45,5,5))
if mibBuilder.loadTexts:nnMultipleSpanningTreeMib.setRevisions(('2016-03-24 00:00','2015-09-24 00:00','2014-06-24 00:00','2009-03-25 00:00','2008-11-05 00:00','2006-04-10 00:00','2004-02-24 00:00'))
_NnMstNotifications_ObjectIdentity=ObjectIdentity
nnMstNotifications=_NnMstNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,5,0))
_NnMstObjects_ObjectIdentity=ObjectIdentity
nnMstObjects=_NnMstObjects_ObjectIdentity((1,3,6,1,4,1,45,5,5,1))
_NnMstScalars_ObjectIdentity=ObjectIdentity
nnMstScalars=_NnMstScalars_ObjectIdentity((1,3,6,1,4,1,45,5,5,1,1))
_NnMstNoOfInstancesSupported_Type=Integer32
_NnMstNoOfInstancesSupported_Object=MibScalar
nnMstNoOfInstancesSupported=_NnMstNoOfInstancesSupported_Object((1,3,6,1,4,1,45,5,5,1,1,1),_NnMstNoOfInstancesSupported_Type())
nnMstNoOfInstancesSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstNoOfInstancesSupported.setStatus(_A)
class _NnMstMaxHopCount_Type(Integer32):defaultValue=2000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,4000))
_NnMstMaxHopCount_Type.__name__=_C
_NnMstMaxHopCount_Object=MibScalar
nnMstMaxHopCount=_NnMstMaxHopCount_Object((1,3,6,1,4,1,45,5,5,1,1,2),_NnMstMaxHopCount_Type())
nnMstMaxHopCount.setMaxAccess(_D)
if mibBuilder.loadTexts:nnMstMaxHopCount.setStatus(_A)
_NnMstBrgAddress_Type=MacAddress
_NnMstBrgAddress_Object=MibScalar
nnMstBrgAddress=_NnMstBrgAddress_Object((1,3,6,1,4,1,45,5,5,1,1,3),_NnMstBrgAddress_Type())
nnMstBrgAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstBrgAddress.setStatus(_A)
_NnMstCistRoot_Type=BridgeId
_NnMstCistRoot_Object=MibScalar
nnMstCistRoot=_NnMstCistRoot_Object((1,3,6,1,4,1,45,5,5,1,1,4),_NnMstCistRoot_Type())
nnMstCistRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistRoot.setStatus(_A)
_NnMstCistRegionalRoot_Type=BridgeId
_NnMstCistRegionalRoot_Object=MibScalar
nnMstCistRegionalRoot=_NnMstCistRegionalRoot_Object((1,3,6,1,4,1,45,5,5,1,1,5),_NnMstCistRegionalRoot_Type())
nnMstCistRegionalRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistRegionalRoot.setStatus(_A)
_NnMstCistRootCost_Type=Integer32
_NnMstCistRootCost_Object=MibScalar
nnMstCistRootCost=_NnMstCistRootCost_Object((1,3,6,1,4,1,45,5,5,1,1,6),_NnMstCistRootCost_Type())
nnMstCistRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistRootCost.setStatus(_A)
_NnMstCistRegionalRootCost_Type=Integer32
_NnMstCistRegionalRootCost_Object=MibScalar
nnMstCistRegionalRootCost=_NnMstCistRegionalRootCost_Object((1,3,6,1,4,1,45,5,5,1,1,7),_NnMstCistRegionalRootCost_Type())
nnMstCistRegionalRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistRegionalRootCost.setStatus(_A)
_NnMstCistRootPort_Type=Integer32
_NnMstCistRootPort_Object=MibScalar
nnMstCistRootPort=_NnMstCistRootPort_Object((1,3,6,1,4,1,45,5,5,1,1,8),_NnMstCistRootPort_Type())
nnMstCistRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistRootPort.setStatus(_A)
class _NnMstCistBridgePriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_NnMstCistBridgePriority_Type.__name__=_C
_NnMstCistBridgePriority_Object=MibScalar
nnMstCistBridgePriority=_NnMstCistBridgePriority_Object((1,3,6,1,4,1,45,5,5,1,1,9),_NnMstCistBridgePriority_Type())
nnMstCistBridgePriority.setMaxAccess(_D)
if mibBuilder.loadTexts:nnMstCistBridgePriority.setStatus(_A)
class _NnMstCistBridgeMaxAge_Type(Timeout):defaultValue=2000;subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(600,4000))
_NnMstCistBridgeMaxAge_Type.__name__=_L
_NnMstCistBridgeMaxAge_Object=MibScalar
nnMstCistBridgeMaxAge=_NnMstCistBridgeMaxAge_Object((1,3,6,1,4,1,45,5,5,1,1,10),_NnMstCistBridgeMaxAge_Type())
nnMstCistBridgeMaxAge.setMaxAccess(_D)
if mibBuilder.loadTexts:nnMstCistBridgeMaxAge.setStatus(_A)
class _NnMstCistBridgeForwardDelay_Type(Timeout):defaultValue=1500;subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(400,3000))
_NnMstCistBridgeForwardDelay_Type.__name__=_L
_NnMstCistBridgeForwardDelay_Object=MibScalar
nnMstCistBridgeForwardDelay=_NnMstCistBridgeForwardDelay_Object((1,3,6,1,4,1,45,5,5,1,1,11),_NnMstCistBridgeForwardDelay_Type())
nnMstCistBridgeForwardDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:nnMstCistBridgeForwardDelay.setStatus(_A)
_NnMstCistHoldTime_Type=Integer32
_NnMstCistHoldTime_Object=MibScalar
nnMstCistHoldTime=_NnMstCistHoldTime_Object((1,3,6,1,4,1,45,5,5,1,1,12),_NnMstCistHoldTime_Type())
nnMstCistHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistHoldTime.setStatus(_A)
_NnMstCistMaxAge_Type=Timeout
_NnMstCistMaxAge_Object=MibScalar
nnMstCistMaxAge=_NnMstCistMaxAge_Object((1,3,6,1,4,1,45,5,5,1,1,13),_NnMstCistMaxAge_Type())
nnMstCistMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistMaxAge.setStatus(_A)
_NnMstCistForwardDelay_Type=Timeout
_NnMstCistForwardDelay_Object=MibScalar
nnMstCistForwardDelay=_NnMstCistForwardDelay_Object((1,3,6,1,4,1,45,5,5,1,1,14),_NnMstCistForwardDelay_Type())
nnMstCistForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistForwardDelay.setStatus(_A)
_NnMstMstpUpCount_Type=Counter32
_NnMstMstpUpCount_Object=MibScalar
nnMstMstpUpCount=_NnMstMstpUpCount_Object((1,3,6,1,4,1,45,5,5,1,1,15),_NnMstMstpUpCount_Type())
nnMstMstpUpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstMstpUpCount.setStatus(_A)
_NnMstMstpDownCount_Type=Counter32
_NnMstMstpDownCount_Object=MibScalar
nnMstMstpDownCount=_NnMstMstpDownCount_Object((1,3,6,1,4,1,45,5,5,1,1,16),_NnMstMstpDownCount_Type())
nnMstMstpDownCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstMstpDownCount.setStatus(_A)
class _NnMstPathCostDefaultType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stp8021d1998',1),('stp8021t2001',2)))
_NnMstPathCostDefaultType_Type.__name__=_C
_NnMstPathCostDefaultType_Object=MibScalar
nnMstPathCostDefaultType=_NnMstPathCostDefaultType_Object((1,3,6,1,4,1,45,5,5,1,1,17),_NnMstPathCostDefaultType_Type())
nnMstPathCostDefaultType.setMaxAccess(_D)
if mibBuilder.loadTexts:nnMstPathCostDefaultType.setStatus(_A)
class _NnMstForceProtocolVersion_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3)));namedValues=NamedValues(*((_X,0),('rstp',2),('mstp',3)))
_NnMstForceProtocolVersion_Type.__name__=_C
_NnMstForceProtocolVersion_Object=MibScalar
nnMstForceProtocolVersion=_NnMstForceProtocolVersion_Object((1,3,6,1,4,1,45,5,5,1,1,18),_NnMstForceProtocolVersion_Type())
nnMstForceProtocolVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:nnMstForceProtocolVersion.setStatus(_A)
class _NnMstTxHoldCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_NnMstTxHoldCount_Type.__name__=_C
_NnMstTxHoldCount_Object=MibScalar
nnMstTxHoldCount=_NnMstTxHoldCount_Object((1,3,6,1,4,1,45,5,5,1,1,19),_NnMstTxHoldCount_Type())
nnMstTxHoldCount.setMaxAccess(_D)
if mibBuilder.loadTexts:nnMstTxHoldCount.setStatus(_A)
class _NnMstConfigIdSel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NnMstConfigIdSel_Type.__name__=_C
_NnMstConfigIdSel_Object=MibScalar
nnMstConfigIdSel=_NnMstConfigIdSel_Object((1,3,6,1,4,1,45,5,5,1,1,20),_NnMstConfigIdSel_Type())
nnMstConfigIdSel.setMaxAccess(_D)
if mibBuilder.loadTexts:nnMstConfigIdSel.setStatus(_A)
class _NnMstRegionName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_NnMstRegionName_Type.__name__=_G
_NnMstRegionName_Object=MibScalar
nnMstRegionName=_NnMstRegionName_Object((1,3,6,1,4,1,45,5,5,1,1,21),_NnMstRegionName_Type())
nnMstRegionName.setMaxAccess(_D)
if mibBuilder.loadTexts:nnMstRegionName.setStatus(_A)
class _NnMstRegionVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NnMstRegionVersion_Type.__name__=_C
_NnMstRegionVersion_Object=MibScalar
nnMstRegionVersion=_NnMstRegionVersion_Object((1,3,6,1,4,1,45,5,5,1,1,22),_NnMstRegionVersion_Type())
nnMstRegionVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:nnMstRegionVersion.setStatus(_A)
class _NnMstConfigDigest_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
_NnMstConfigDigest_Type.__name__=_G
_NnMstConfigDigest_Object=MibScalar
nnMstConfigDigest=_NnMstConfigDigest_Object((1,3,6,1,4,1,45,5,5,1,1,23),_NnMstConfigDigest_Type())
nnMstConfigDigest.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstConfigDigest.setStatus(_A)
_NnMstRegionConfigChangeCount_Type=Counter32
_NnMstRegionConfigChangeCount_Object=MibScalar
nnMstRegionConfigChangeCount=_NnMstRegionConfigChangeCount_Object((1,3,6,1,4,1,45,5,5,1,1,24),_NnMstRegionConfigChangeCount_Type())
nnMstRegionConfigChangeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstRegionConfigChangeCount.setStatus(_A)
class _NnMstCistBridgeRoleSelectionSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Y,0),(_Z,1)))
_NnMstCistBridgeRoleSelectionSemState_Type.__name__=_C
_NnMstCistBridgeRoleSelectionSemState_Object=MibScalar
nnMstCistBridgeRoleSelectionSemState=_NnMstCistBridgeRoleSelectionSemState_Object((1,3,6,1,4,1,45,5,5,1,1,25),_NnMstCistBridgeRoleSelectionSemState_Type())
nnMstCistBridgeRoleSelectionSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistBridgeRoleSelectionSemState.setStatus(_A)
_NnMstCistTimeSinceTopologyChange_Type=TimeTicks
_NnMstCistTimeSinceTopologyChange_Object=MibScalar
nnMstCistTimeSinceTopologyChange=_NnMstCistTimeSinceTopologyChange_Object((1,3,6,1,4,1,45,5,5,1,1,26),_NnMstCistTimeSinceTopologyChange_Type())
nnMstCistTimeSinceTopologyChange.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistTimeSinceTopologyChange.setStatus(_A)
_NnMstCistTopChanges_Type=Counter32
_NnMstCistTopChanges_Object=MibScalar
nnMstCistTopChanges=_NnMstCistTopChanges_Object((1,3,6,1,4,1,45,5,5,1,1,27),_NnMstCistTopChanges_Type())
nnMstCistTopChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistTopChanges.setStatus(_A)
_NnMstCistNewRootBridgeCount_Type=Counter32
_NnMstCistNewRootBridgeCount_Object=MibScalar
nnMstCistNewRootBridgeCount=_NnMstCistNewRootBridgeCount_Object((1,3,6,1,4,1,45,5,5,1,1,28),_NnMstCistNewRootBridgeCount_Type())
nnMstCistNewRootBridgeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistNewRootBridgeCount.setStatus(_A)
_NnMstBridgeTable_Object=MibTable
nnMstBridgeTable=_NnMstBridgeTable_Object((1,3,6,1,4,1,45,5,5,1,2))
if mibBuilder.loadTexts:nnMstBridgeTable.setStatus(_A)
_NnMstBridgeEntry_Object=MibTableRow
nnMstBridgeEntry=_NnMstBridgeEntry_Object((1,3,6,1,4,1,45,5,5,1,2,1))
nnMstBridgeEntry.setIndexNames((0,_E,_T))
if mibBuilder.loadTexts:nnMstBridgeEntry.setStatus(_A)
class _NnMstBridgeInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_NnMstBridgeInstance_Type.__name__=_C
_NnMstBridgeInstance_Object=MibTableColumn
nnMstBridgeInstance=_NnMstBridgeInstance_Object((1,3,6,1,4,1,45,5,5,1,2,1,1),_NnMstBridgeInstance_Type())
nnMstBridgeInstance.setMaxAccess(_J)
if mibBuilder.loadTexts:nnMstBridgeInstance.setStatus(_A)
_NnMstBridgeRegionalRoot_Type=BridgeId
_NnMstBridgeRegionalRoot_Object=MibTableColumn
nnMstBridgeRegionalRoot=_NnMstBridgeRegionalRoot_Object((1,3,6,1,4,1,45,5,5,1,2,1,2),_NnMstBridgeRegionalRoot_Type())
nnMstBridgeRegionalRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstBridgeRegionalRoot.setStatus(_A)
class _NnMstBridgePriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_NnMstBridgePriority_Type.__name__=_C
_NnMstBridgePriority_Object=MibTableColumn
nnMstBridgePriority=_NnMstBridgePriority_Object((1,3,6,1,4,1,45,5,5,1,2,1,3),_NnMstBridgePriority_Type())
nnMstBridgePriority.setMaxAccess(_U)
if mibBuilder.loadTexts:nnMstBridgePriority.setStatus(_A)
_NnMstBridgeRootCost_Type=Integer32
_NnMstBridgeRootCost_Object=MibTableColumn
nnMstBridgeRootCost=_NnMstBridgeRootCost_Object((1,3,6,1,4,1,45,5,5,1,2,1,4),_NnMstBridgeRootCost_Type())
nnMstBridgeRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstBridgeRootCost.setStatus(_A)
_NnMstBridgeRootPort_Type=Integer32
_NnMstBridgeRootPort_Object=MibTableColumn
nnMstBridgeRootPort=_NnMstBridgeRootPort_Object((1,3,6,1,4,1,45,5,5,1,2,1,5),_NnMstBridgeRootPort_Type())
nnMstBridgeRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstBridgeRootPort.setStatus(_A)
_NnMstBridgeTimeSinceTopologyChange_Type=TimeTicks
_NnMstBridgeTimeSinceTopologyChange_Object=MibTableColumn
nnMstBridgeTimeSinceTopologyChange=_NnMstBridgeTimeSinceTopologyChange_Object((1,3,6,1,4,1,45,5,5,1,2,1,6),_NnMstBridgeTimeSinceTopologyChange_Type())
nnMstBridgeTimeSinceTopologyChange.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstBridgeTimeSinceTopologyChange.setStatus(_A)
_NnMstBridgeTopChanges_Type=Counter32
_NnMstBridgeTopChanges_Object=MibTableColumn
nnMstBridgeTopChanges=_NnMstBridgeTopChanges_Object((1,3,6,1,4,1,45,5,5,1,2,1,7),_NnMstBridgeTopChanges_Type())
nnMstBridgeTopChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstBridgeTopChanges.setStatus(_A)
_NnMstBridgeNewRootCount_Type=Counter32
_NnMstBridgeNewRootCount_Object=MibTableColumn
nnMstBridgeNewRootCount=_NnMstBridgeNewRootCount_Object((1,3,6,1,4,1,45,5,5,1,2,1,8),_NnMstBridgeNewRootCount_Type())
nnMstBridgeNewRootCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstBridgeNewRootCount.setStatus(_A)
class _NnMstBridgeRoleSelectionSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Y,0),(_Z,1)))
_NnMstBridgeRoleSelectionSemState_Type.__name__=_C
_NnMstBridgeRoleSelectionSemState_Object=MibTableColumn
nnMstBridgeRoleSelectionSemState=_NnMstBridgeRoleSelectionSemState_Object((1,3,6,1,4,1,45,5,5,1,2,1,9),_NnMstBridgeRoleSelectionSemState_Type())
nnMstBridgeRoleSelectionSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstBridgeRoleSelectionSemState.setStatus(_A)
_NnMstBridgeInstanceUpCount_Type=Counter32
_NnMstBridgeInstanceUpCount_Object=MibTableColumn
nnMstBridgeInstanceUpCount=_NnMstBridgeInstanceUpCount_Object((1,3,6,1,4,1,45,5,5,1,2,1,10),_NnMstBridgeInstanceUpCount_Type())
nnMstBridgeInstanceUpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstBridgeInstanceUpCount.setStatus(_A)
_NnMstBridgeInstanceDownCount_Type=Counter32
_NnMstBridgeInstanceDownCount_Object=MibTableColumn
nnMstBridgeInstanceDownCount=_NnMstBridgeInstanceDownCount_Object((1,3,6,1,4,1,45,5,5,1,2,1,11),_NnMstBridgeInstanceDownCount_Type())
nnMstBridgeInstanceDownCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstBridgeInstanceDownCount.setStatus(_A)
_NnMstBridgeOldDesignatedRoot_Type=BridgeId
_NnMstBridgeOldDesignatedRoot_Object=MibTableColumn
nnMstBridgeOldDesignatedRoot=_NnMstBridgeOldDesignatedRoot_Object((1,3,6,1,4,1,45,5,5,1,2,1,12),_NnMstBridgeOldDesignatedRoot_Type())
nnMstBridgeOldDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstBridgeOldDesignatedRoot.setStatus(_A)
_NnMstBridgeEnabled_Type=TruthValue
_NnMstBridgeEnabled_Object=MibTableColumn
nnMstBridgeEnabled=_NnMstBridgeEnabled_Object((1,3,6,1,4,1,45,5,5,1,2,1,13),_NnMstBridgeEnabled_Type())
nnMstBridgeEnabled.setMaxAccess(_U)
if mibBuilder.loadTexts:nnMstBridgeEnabled.setStatus(_A)
_NnMstBridgeRowStatus_Type=RowStatus
_NnMstBridgeRowStatus_Object=MibTableColumn
nnMstBridgeRowStatus=_NnMstBridgeRowStatus_Object((1,3,6,1,4,1,45,5,5,1,2,1,14),_NnMstBridgeRowStatus_Type())
nnMstBridgeRowStatus.setMaxAccess(_U)
if mibBuilder.loadTexts:nnMstBridgeRowStatus.setStatus(_A)
class _NnMstBridgeMappedVlans_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_NnMstBridgeMappedVlans_Type.__name__=_G
_NnMstBridgeMappedVlans_Object=MibTableColumn
nnMstBridgeMappedVlans=_NnMstBridgeMappedVlans_Object((1,3,6,1,4,1,45,5,5,1,2,1,15),_NnMstBridgeMappedVlans_Type())
nnMstBridgeMappedVlans.setMaxAccess(_D)
if mibBuilder.loadTexts:nnMstBridgeMappedVlans.setStatus(_A)
class _NnMstBridgeMappedVlansAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('add',1),('remove',2),(_V,3)))
_NnMstBridgeMappedVlansAction_Type.__name__=_C
_NnMstBridgeMappedVlansAction_Object=MibTableColumn
nnMstBridgeMappedVlansAction=_NnMstBridgeMappedVlansAction_Object((1,3,6,1,4,1,45,5,5,1,2,1,16),_NnMstBridgeMappedVlansAction_Type())
nnMstBridgeMappedVlansAction.setMaxAccess(_D)
if mibBuilder.loadTexts:nnMstBridgeMappedVlansAction.setStatus(_A)
_NnMstCistPortTable_Object=MibTable
nnMstCistPortTable=_NnMstCistPortTable_Object((1,3,6,1,4,1,45,5,5,1,3))
if mibBuilder.loadTexts:nnMstCistPortTable.setStatus(_A)
_NnMstCistPortEntry_Object=MibTableRow
nnMstCistPortEntry=_NnMstCistPortEntry_Object((1,3,6,1,4,1,45,5,5,1,3,1))
nnMstCistPortEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:nnMstCistPortEntry.setStatus(_A)
class _NnMstCistPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NnMstCistPort_Type.__name__=_C
_NnMstCistPort_Object=MibTableColumn
nnMstCistPort=_NnMstCistPort_Object((1,3,6,1,4,1,45,5,5,1,3,1,1),_NnMstCistPort_Type())
nnMstCistPort.setMaxAccess(_J)
if mibBuilder.loadTexts:nnMstCistPort.setStatus(_A)
class _NnMstCistPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_NnMstCistPortPathCost_Type.__name__=_C
_NnMstCistPortPathCost_Object=MibTableColumn
nnMstCistPortPathCost=_NnMstCistPortPathCost_Object((1,3,6,1,4,1,45,5,5,1,3,1,2),_NnMstCistPortPathCost_Type())
nnMstCistPortPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:nnMstCistPortPathCost.setStatus(_A)
class _NnMstCistPortPriority_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_NnMstCistPortPriority_Type.__name__=_C
_NnMstCistPortPriority_Object=MibTableColumn
nnMstCistPortPriority=_NnMstCistPortPriority_Object((1,3,6,1,4,1,45,5,5,1,3,1,3),_NnMstCistPortPriority_Type())
nnMstCistPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:nnMstCistPortPriority.setStatus(_A)
_NnMstCistPortDesignatedRoot_Type=BridgeId
_NnMstCistPortDesignatedRoot_Object=MibTableColumn
nnMstCistPortDesignatedRoot=_NnMstCistPortDesignatedRoot_Object((1,3,6,1,4,1,45,5,5,1,3,1,4),_NnMstCistPortDesignatedRoot_Type())
nnMstCistPortDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortDesignatedRoot.setStatus(_A)
_NnMstCistPortDesignatedBridge_Type=BridgeId
_NnMstCistPortDesignatedBridge_Object=MibTableColumn
nnMstCistPortDesignatedBridge=_NnMstCistPortDesignatedBridge_Object((1,3,6,1,4,1,45,5,5,1,3,1,5),_NnMstCistPortDesignatedBridge_Type())
nnMstCistPortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortDesignatedBridge.setStatus(_A)
class _NnMstCistPortDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_NnMstCistPortDesignatedPort_Type.__name__=_G
_NnMstCistPortDesignatedPort_Object=MibTableColumn
nnMstCistPortDesignatedPort=_NnMstCistPortDesignatedPort_Object((1,3,6,1,4,1,45,5,5,1,3,1,6),_NnMstCistPortDesignatedPort_Type())
nnMstCistPortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortDesignatedPort.setStatus(_A)
class _NnMstCistPortAdminP2P_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('forceTrue',0),('forceFalse',1),('auto',2)))
_NnMstCistPortAdminP2P_Type.__name__=_C
_NnMstCistPortAdminP2P_Object=MibTableColumn
nnMstCistPortAdminP2P=_NnMstCistPortAdminP2P_Object((1,3,6,1,4,1,45,5,5,1,3,1,7),_NnMstCistPortAdminP2P_Type())
nnMstCistPortAdminP2P.setMaxAccess(_D)
if mibBuilder.loadTexts:nnMstCistPortAdminP2P.setStatus(_A)
_NnMstCistPortOperP2P_Type=TruthValue
_NnMstCistPortOperP2P_Object=MibTableColumn
nnMstCistPortOperP2P=_NnMstCistPortOperP2P_Object((1,3,6,1,4,1,45,5,5,1,3,1,8),_NnMstCistPortOperP2P_Type())
nnMstCistPortOperP2P.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortOperP2P.setStatus(_A)
_NnMstCistPortAdminEdgeStatus_Type=TruthValue
_NnMstCistPortAdminEdgeStatus_Object=MibTableColumn
nnMstCistPortAdminEdgeStatus=_NnMstCistPortAdminEdgeStatus_Object((1,3,6,1,4,1,45,5,5,1,3,1,9),_NnMstCistPortAdminEdgeStatus_Type())
nnMstCistPortAdminEdgeStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:nnMstCistPortAdminEdgeStatus.setStatus(_A)
_NnMstCistPortOperEdgeStatus_Type=TruthValue
_NnMstCistPortOperEdgeStatus_Object=MibTableColumn
nnMstCistPortOperEdgeStatus=_NnMstCistPortOperEdgeStatus_Object((1,3,6,1,4,1,45,5,5,1,3,1,10),_NnMstCistPortOperEdgeStatus_Type())
nnMstCistPortOperEdgeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortOperEdgeStatus.setStatus(_A)
_NnMstCistPortProtocolMigration_Type=TruthValue
_NnMstCistPortProtocolMigration_Object=MibTableColumn
nnMstCistPortProtocolMigration=_NnMstCistPortProtocolMigration_Object((1,3,6,1,4,1,45,5,5,1,3,1,11),_NnMstCistPortProtocolMigration_Type())
nnMstCistPortProtocolMigration.setMaxAccess(_D)
if mibBuilder.loadTexts:nnMstCistPortProtocolMigration.setStatus(_A)
class _NnMstCistPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5)));namedValues=NamedValues(*((_F,1),(_M,2),(_N,4),(_O,5)))
_NnMstCistPortState_Type.__name__=_C
_NnMstCistPortState_Object=MibTableColumn
nnMstCistPortState=_NnMstCistPortState_Object((1,3,6,1,4,1,45,5,5,1,3,1,12),_NnMstCistPortState_Type())
nnMstCistPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortState.setStatus(_A)
class _NnMstCistForcePortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_P,1)))
_NnMstCistForcePortState_Type.__name__=_C
_NnMstCistForcePortState_Object=MibTableColumn
nnMstCistForcePortState=_NnMstCistForcePortState_Object((1,3,6,1,4,1,45,5,5,1,3,1,13),_NnMstCistForcePortState_Type())
nnMstCistForcePortState.setMaxAccess(_D)
if mibBuilder.loadTexts:nnMstCistForcePortState.setStatus(_A)
_NnMstCistPortForwardTransitions_Type=Counter32
_NnMstCistPortForwardTransitions_Object=MibTableColumn
nnMstCistPortForwardTransitions=_NnMstCistPortForwardTransitions_Object((1,3,6,1,4,1,45,5,5,1,3,1,14),_NnMstCistPortForwardTransitions_Type())
nnMstCistPortForwardTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortForwardTransitions.setStatus(_A)
_NnMstCistPortRxMstBpduCount_Type=Counter32
_NnMstCistPortRxMstBpduCount_Object=MibTableColumn
nnMstCistPortRxMstBpduCount=_NnMstCistPortRxMstBpduCount_Object((1,3,6,1,4,1,45,5,5,1,3,1,15),_NnMstCistPortRxMstBpduCount_Type())
nnMstCistPortRxMstBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortRxMstBpduCount.setStatus(_A)
_NnMstCistPortRxRstBpduCount_Type=Counter32
_NnMstCistPortRxRstBpduCount_Object=MibTableColumn
nnMstCistPortRxRstBpduCount=_NnMstCistPortRxRstBpduCount_Object((1,3,6,1,4,1,45,5,5,1,3,1,16),_NnMstCistPortRxRstBpduCount_Type())
nnMstCistPortRxRstBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortRxRstBpduCount.setStatus(_A)
_NnMstCistPortRxConfigBpduCount_Type=Counter32
_NnMstCistPortRxConfigBpduCount_Object=MibTableColumn
nnMstCistPortRxConfigBpduCount=_NnMstCistPortRxConfigBpduCount_Object((1,3,6,1,4,1,45,5,5,1,3,1,17),_NnMstCistPortRxConfigBpduCount_Type())
nnMstCistPortRxConfigBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortRxConfigBpduCount.setStatus(_A)
_NnMstCistPortRxTcnBpduCount_Type=Counter32
_NnMstCistPortRxTcnBpduCount_Object=MibTableColumn
nnMstCistPortRxTcnBpduCount=_NnMstCistPortRxTcnBpduCount_Object((1,3,6,1,4,1,45,5,5,1,3,1,18),_NnMstCistPortRxTcnBpduCount_Type())
nnMstCistPortRxTcnBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortRxTcnBpduCount.setStatus(_A)
_NnMstCistPortTxMstBpduCount_Type=Counter32
_NnMstCistPortTxMstBpduCount_Object=MibTableColumn
nnMstCistPortTxMstBpduCount=_NnMstCistPortTxMstBpduCount_Object((1,3,6,1,4,1,45,5,5,1,3,1,19),_NnMstCistPortTxMstBpduCount_Type())
nnMstCistPortTxMstBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortTxMstBpduCount.setStatus(_A)
_NnMstCistPortTxRstBpduCount_Type=Counter32
_NnMstCistPortTxRstBpduCount_Object=MibTableColumn
nnMstCistPortTxRstBpduCount=_NnMstCistPortTxRstBpduCount_Object((1,3,6,1,4,1,45,5,5,1,3,1,20),_NnMstCistPortTxRstBpduCount_Type())
nnMstCistPortTxRstBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortTxRstBpduCount.setStatus(_A)
_NnMstCistPortTxConfigBpduCount_Type=Counter32
_NnMstCistPortTxConfigBpduCount_Object=MibTableColumn
nnMstCistPortTxConfigBpduCount=_NnMstCistPortTxConfigBpduCount_Object((1,3,6,1,4,1,45,5,5,1,3,1,21),_NnMstCistPortTxConfigBpduCount_Type())
nnMstCistPortTxConfigBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortTxConfigBpduCount.setStatus(_A)
_NnMstCistPortTxTcnBpduCount_Type=Counter32
_NnMstCistPortTxTcnBpduCount_Object=MibTableColumn
nnMstCistPortTxTcnBpduCount=_NnMstCistPortTxTcnBpduCount_Object((1,3,6,1,4,1,45,5,5,1,3,1,22),_NnMstCistPortTxTcnBpduCount_Type())
nnMstCistPortTxTcnBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortTxTcnBpduCount.setStatus(_A)
_NnMstCistPortInvalidMstBpduRxCount_Type=Counter32
_NnMstCistPortInvalidMstBpduRxCount_Object=MibTableColumn
nnMstCistPortInvalidMstBpduRxCount=_NnMstCistPortInvalidMstBpduRxCount_Object((1,3,6,1,4,1,45,5,5,1,3,1,23),_NnMstCistPortInvalidMstBpduRxCount_Type())
nnMstCistPortInvalidMstBpduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortInvalidMstBpduRxCount.setStatus(_A)
_NnMstCistPortInvalidRstBpduRxCount_Type=Counter32
_NnMstCistPortInvalidRstBpduRxCount_Object=MibTableColumn
nnMstCistPortInvalidRstBpduRxCount=_NnMstCistPortInvalidRstBpduRxCount_Object((1,3,6,1,4,1,45,5,5,1,3,1,24),_NnMstCistPortInvalidRstBpduRxCount_Type())
nnMstCistPortInvalidRstBpduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortInvalidRstBpduRxCount.setStatus(_A)
_NnMstCistPortInvalidConfigBpduRxCount_Type=Counter32
_NnMstCistPortInvalidConfigBpduRxCount_Object=MibTableColumn
nnMstCistPortInvalidConfigBpduRxCount=_NnMstCistPortInvalidConfigBpduRxCount_Object((1,3,6,1,4,1,45,5,5,1,3,1,25),_NnMstCistPortInvalidConfigBpduRxCount_Type())
nnMstCistPortInvalidConfigBpduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortInvalidConfigBpduRxCount.setStatus(_A)
_NnMstCistPortInvalidTcnBpduRxCount_Type=Counter32
_NnMstCistPortInvalidTcnBpduRxCount_Object=MibTableColumn
nnMstCistPortInvalidTcnBpduRxCount=_NnMstCistPortInvalidTcnBpduRxCount_Object((1,3,6,1,4,1,45,5,5,1,3,1,26),_NnMstCistPortInvalidTcnBpduRxCount_Type())
nnMstCistPortInvalidTcnBpduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortInvalidTcnBpduRxCount.setStatus(_A)
class _NnMstCistPortTransmitSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('transmitinit',0),('transmitperiodic',1),('transmitconfig',2),('transmittcn',3),('transmitrstp',4),('idle',5)))
_NnMstCistPortTransmitSemState_Type.__name__=_C
_NnMstCistPortTransmitSemState_Object=MibTableColumn
nnMstCistPortTransmitSemState=_NnMstCistPortTransmitSemState_Object((1,3,6,1,4,1,45,5,5,1,3,1,27),_NnMstCistPortTransmitSemState_Type())
nnMstCistPortTransmitSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortTransmitSemState.setStatus(_A)
class _NnMstCistPortReceiveSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('discard',0),(_W,1)))
_NnMstCistPortReceiveSemState_Type.__name__=_C
_NnMstCistPortReceiveSemState_Object=MibTableColumn
nnMstCistPortReceiveSemState=_NnMstCistPortReceiveSemState_Object((1,3,6,1,4,1,45,5,5,1,3,1,28),_NnMstCistPortReceiveSemState_Type())
nnMstCistPortReceiveSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortReceiveSemState.setStatus(_A)
class _NnMstCistPortProtMigrationSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_K,0),(_b,1),('sendingrstp',2),(_c,3),('sendingstp',4)))
_NnMstCistPortProtMigrationSemState_Type.__name__=_C
_NnMstCistPortProtMigrationSemState_Object=MibTableColumn
nnMstCistPortProtMigrationSemState=_NnMstCistPortProtMigrationSemState_Object((1,3,6,1,4,1,45,5,5,1,3,1,29),_NnMstCistPortProtMigrationSemState_Type())
nnMstCistPortProtMigrationSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortProtMigrationSemState.setStatus(_A)
_NnMstCistProtocolMigrationCount_Type=Counter32
_NnMstCistProtocolMigrationCount_Object=MibTableColumn
nnMstCistProtocolMigrationCount=_NnMstCistProtocolMigrationCount_Object((1,3,6,1,4,1,45,5,5,1,3,1,30),_NnMstCistProtocolMigrationCount_Type())
nnMstCistProtocolMigrationCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistProtocolMigrationCount.setStatus(_A)
_NnMstCistPortDesignatedCost_Type=Integer32
_NnMstCistPortDesignatedCost_Object=MibTableColumn
nnMstCistPortDesignatedCost=_NnMstCistPortDesignatedCost_Object((1,3,6,1,4,1,45,5,5,1,3,1,31),_NnMstCistPortDesignatedCost_Type())
nnMstCistPortDesignatedCost.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortDesignatedCost.setStatus(_A)
_NnMstCistPortRegionalRoot_Type=BridgeId
_NnMstCistPortRegionalRoot_Object=MibTableColumn
nnMstCistPortRegionalRoot=_NnMstCistPortRegionalRoot_Object((1,3,6,1,4,1,45,5,5,1,3,1,32),_NnMstCistPortRegionalRoot_Type())
nnMstCistPortRegionalRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortRegionalRoot.setStatus(_A)
_NnMstCistPortRegionalPathCost_Type=Integer32
_NnMstCistPortRegionalPathCost_Object=MibTableColumn
nnMstCistPortRegionalPathCost=_NnMstCistPortRegionalPathCost_Object((1,3,6,1,4,1,45,5,5,1,3,1,33),_NnMstCistPortRegionalPathCost_Type())
nnMstCistPortRegionalPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortRegionalPathCost.setStatus(_A)
class _NnMstCistSelectedPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_F,0),(_Q,1),(_R,2),(_I,3),(_S,4)))
_NnMstCistSelectedPortRole_Type.__name__=_C
_NnMstCistSelectedPortRole_Object=MibTableColumn
nnMstCistSelectedPortRole=_NnMstCistSelectedPortRole_Object((1,3,6,1,4,1,45,5,5,1,3,1,34),_NnMstCistSelectedPortRole_Type())
nnMstCistSelectedPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistSelectedPortRole.setStatus(_A)
class _NnMstCistCurrentPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_F,0),(_Q,1),(_R,2),(_I,3),(_S,4)))
_NnMstCistCurrentPortRole_Type.__name__=_C
_NnMstCistCurrentPortRole_Object=MibTableColumn
nnMstCistCurrentPortRole=_NnMstCistCurrentPortRole_Object((1,3,6,1,4,1,45,5,5,1,3,1,35),_NnMstCistCurrentPortRole_Type())
nnMstCistCurrentPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistCurrentPortRole.setStatus(_A)
class _NnMstCistPortInfoSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_F,0),(_P,1),('aged',2),(_d,3),(_e,4),(_f,5),(_I,6),('other',7),(_g,8),(_W,9)))
_NnMstCistPortInfoSemState_Type.__name__=_C
_NnMstCistPortInfoSemState_Object=MibTableColumn
nnMstCistPortInfoSemState=_NnMstCistPortInfoSemState_Object((1,3,6,1,4,1,45,5,5,1,3,1,36),_NnMstCistPortInfoSemState_Type())
nnMstCistPortInfoSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortInfoSemState.setStatus(_A)
class _NnMstCistPortRoleTransitionSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_K,0),(_h,1),(_i,2),(_j,3)))
_NnMstCistPortRoleTransitionSemState_Type.__name__=_C
_NnMstCistPortRoleTransitionSemState_Object=MibTableColumn
nnMstCistPortRoleTransitionSemState=_NnMstCistPortRoleTransitionSemState_Object((1,3,6,1,4,1,45,5,5,1,3,1,37),_NnMstCistPortRoleTransitionSemState_Type())
nnMstCistPortRoleTransitionSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortRoleTransitionSemState.setStatus(_A)
class _NnMstCistPortStateTransitionSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2)))
_NnMstCistPortStateTransitionSemState_Type.__name__=_C
_NnMstCistPortStateTransitionSemState_Object=MibTableColumn
nnMstCistPortStateTransitionSemState=_NnMstCistPortStateTransitionSemState_Object((1,3,6,1,4,1,45,5,5,1,3,1,38),_NnMstCistPortStateTransitionSemState_Type())
nnMstCistPortStateTransitionSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortStateTransitionSemState.setStatus(_A)
class _NnMstCistPortTopologyChangeSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_K,0),(_k,1),(_l,2),(_m,3),(_n,4),(_o,5),(_p,6),(_q,7)))
_NnMstCistPortTopologyChangeSemState_Type.__name__=_C
_NnMstCistPortTopologyChangeSemState_Object=MibTableColumn
nnMstCistPortTopologyChangeSemState=_NnMstCistPortTopologyChangeSemState_Object((1,3,6,1,4,1,45,5,5,1,3,1,39),_NnMstCistPortTopologyChangeSemState_Type())
nnMstCistPortTopologyChangeSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortTopologyChangeSemState.setStatus(_A)
class _NnMstCistPortHelloTime_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_NnMstCistPortHelloTime_Type.__name__=_L
_NnMstCistPortHelloTime_Object=MibTableColumn
nnMstCistPortHelloTime=_NnMstCistPortHelloTime_Object((1,3,6,1,4,1,45,5,5,1,3,1,40),_NnMstCistPortHelloTime_Type())
nnMstCistPortHelloTime.setMaxAccess(_D)
if mibBuilder.loadTexts:nnMstCistPortHelloTime.setStatus(_A)
class _NnMstCistPortOperVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3)));namedValues=NamedValues(*((_X,0),('rstp',2),('mstp',3)))
_NnMstCistPortOperVersion_Type.__name__=_C
_NnMstCistPortOperVersion_Object=MibTableColumn
nnMstCistPortOperVersion=_NnMstCistPortOperVersion_Object((1,3,6,1,4,1,45,5,5,1,3,1,41),_NnMstCistPortOperVersion_Type())
nnMstCistPortOperVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortOperVersion.setStatus(_A)
_NnMstCistPortEffectivePortState_Type=TruthValue
_NnMstCistPortEffectivePortState_Object=MibTableColumn
nnMstCistPortEffectivePortState=_NnMstCistPortEffectivePortState_Object((1,3,6,1,4,1,45,5,5,1,3,1,42),_NnMstCistPortEffectivePortState_Type())
nnMstCistPortEffectivePortState.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortEffectivePortState.setStatus(_A)
_NnMstCistPortRxTcBpduCount_Type=Counter32
_NnMstCistPortRxTcBpduCount_Object=MibTableColumn
nnMstCistPortRxTcBpduCount=_NnMstCistPortRxTcBpduCount_Object((1,3,6,1,4,1,45,5,5,1,3,1,43),_NnMstCistPortRxTcBpduCount_Type())
nnMstCistPortRxTcBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstCistPortRxTcBpduCount.setStatus(_A)
_NnMstPortTable_Object=MibTable
nnMstPortTable=_NnMstPortTable_Object((1,3,6,1,4,1,45,5,5,1,4))
if mibBuilder.loadTexts:nnMstPortTable.setStatus(_A)
_NnMstPortEntry_Object=MibTableRow
nnMstPortEntry=_NnMstPortEntry_Object((1,3,6,1,4,1,45,5,5,1,4,1))
nnMstPortEntry.setIndexNames((0,_E,_r),(0,_E,_T))
if mibBuilder.loadTexts:nnMstPortEntry.setStatus(_A)
class _NnMstPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NnMstPort_Type.__name__=_C
_NnMstPort_Object=MibTableColumn
nnMstPort=_NnMstPort_Object((1,3,6,1,4,1,45,5,5,1,4,1,1),_NnMstPort_Type())
nnMstPort.setMaxAccess(_J)
if mibBuilder.loadTexts:nnMstPort.setStatus(_A)
class _NnMstPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_NnMstPortPathCost_Type.__name__=_C
_NnMstPortPathCost_Object=MibTableColumn
nnMstPortPathCost=_NnMstPortPathCost_Object((1,3,6,1,4,1,45,5,5,1,4,1,2),_NnMstPortPathCost_Type())
nnMstPortPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:nnMstPortPathCost.setStatus(_A)
class _NnMstPortPriority_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_NnMstPortPriority_Type.__name__=_C
_NnMstPortPriority_Object=MibTableColumn
nnMstPortPriority=_NnMstPortPriority_Object((1,3,6,1,4,1,45,5,5,1,4,1,3),_NnMstPortPriority_Type())
nnMstPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:nnMstPortPriority.setStatus(_A)
_NnMstPortDesignatedRoot_Type=BridgeId
_NnMstPortDesignatedRoot_Object=MibTableColumn
nnMstPortDesignatedRoot=_NnMstPortDesignatedRoot_Object((1,3,6,1,4,1,45,5,5,1,4,1,4),_NnMstPortDesignatedRoot_Type())
nnMstPortDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstPortDesignatedRoot.setStatus(_A)
_NnMstPortDesignatedBridge_Type=BridgeId
_NnMstPortDesignatedBridge_Object=MibTableColumn
nnMstPortDesignatedBridge=_NnMstPortDesignatedBridge_Object((1,3,6,1,4,1,45,5,5,1,4,1,5),_NnMstPortDesignatedBridge_Type())
nnMstPortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstPortDesignatedBridge.setStatus(_A)
class _NnMstPortDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_NnMstPortDesignatedPort_Type.__name__=_G
_NnMstPortDesignatedPort_Object=MibTableColumn
nnMstPortDesignatedPort=_NnMstPortDesignatedPort_Object((1,3,6,1,4,1,45,5,5,1,4,1,6),_NnMstPortDesignatedPort_Type())
nnMstPortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstPortDesignatedPort.setStatus(_A)
class _NnMstPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5)));namedValues=NamedValues(*((_F,1),(_M,2),(_N,4),(_O,5)))
_NnMstPortState_Type.__name__=_C
_NnMstPortState_Object=MibTableColumn
nnMstPortState=_NnMstPortState_Object((1,3,6,1,4,1,45,5,5,1,4,1,7),_NnMstPortState_Type())
nnMstPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstPortState.setStatus(_A)
class _NnMstPortForcePortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_P,1)))
_NnMstPortForcePortState_Type.__name__=_C
_NnMstPortForcePortState_Object=MibTableColumn
nnMstPortForcePortState=_NnMstPortForcePortState_Object((1,3,6,1,4,1,45,5,5,1,4,1,8),_NnMstPortForcePortState_Type())
nnMstPortForcePortState.setMaxAccess(_D)
if mibBuilder.loadTexts:nnMstPortForcePortState.setStatus(_A)
_NnMstPortForwardTransitions_Type=Counter32
_NnMstPortForwardTransitions_Object=MibTableColumn
nnMstPortForwardTransitions=_NnMstPortForwardTransitions_Object((1,3,6,1,4,1,45,5,5,1,4,1,9),_NnMstPortForwardTransitions_Type())
nnMstPortForwardTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstPortForwardTransitions.setStatus(_A)
_NnMstPortReceivedBPDUs_Type=Counter32
_NnMstPortReceivedBPDUs_Object=MibTableColumn
nnMstPortReceivedBPDUs=_NnMstPortReceivedBPDUs_Object((1,3,6,1,4,1,45,5,5,1,4,1,10),_NnMstPortReceivedBPDUs_Type())
nnMstPortReceivedBPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstPortReceivedBPDUs.setStatus(_A)
_NnMstPortTransmittedBPDUs_Type=Counter32
_NnMstPortTransmittedBPDUs_Object=MibTableColumn
nnMstPortTransmittedBPDUs=_NnMstPortTransmittedBPDUs_Object((1,3,6,1,4,1,45,5,5,1,4,1,11),_NnMstPortTransmittedBPDUs_Type())
nnMstPortTransmittedBPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstPortTransmittedBPDUs.setStatus(_A)
_NnMstPortInvalidBPDUsRcvd_Type=Counter32
_NnMstPortInvalidBPDUsRcvd_Object=MibTableColumn
nnMstPortInvalidBPDUsRcvd=_NnMstPortInvalidBPDUsRcvd_Object((1,3,6,1,4,1,45,5,5,1,4,1,12),_NnMstPortInvalidBPDUsRcvd_Type())
nnMstPortInvalidBPDUsRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstPortInvalidBPDUsRcvd.setStatus(_A)
_NnMstPortDesignatedCost_Type=Integer32
_NnMstPortDesignatedCost_Object=MibTableColumn
nnMstPortDesignatedCost=_NnMstPortDesignatedCost_Object((1,3,6,1,4,1,45,5,5,1,4,1,13),_NnMstPortDesignatedCost_Type())
nnMstPortDesignatedCost.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstPortDesignatedCost.setStatus(_A)
class _NnMstPortSelectedPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_F,0),(_Q,1),(_R,2),(_I,3),(_S,4),(_s,5)))
_NnMstPortSelectedPortRole_Type.__name__=_C
_NnMstPortSelectedPortRole_Object=MibTableColumn
nnMstPortSelectedPortRole=_NnMstPortSelectedPortRole_Object((1,3,6,1,4,1,45,5,5,1,4,1,14),_NnMstPortSelectedPortRole_Type())
nnMstPortSelectedPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstPortSelectedPortRole.setStatus(_A)
class _NnMstPortCurrentPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_F,0),(_Q,1),(_R,2),(_I,3),(_S,4),(_s,5)))
_NnMstPortCurrentPortRole_Type.__name__=_C
_NnMstPortCurrentPortRole_Object=MibTableColumn
nnMstPortCurrentPortRole=_NnMstPortCurrentPortRole_Object((1,3,6,1,4,1,45,5,5,1,4,1,15),_NnMstPortCurrentPortRole_Type())
nnMstPortCurrentPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstPortCurrentPortRole.setStatus(_A)
class _NnMstPortInfoSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_F,0),(_P,1),('aged',2),(_d,3),(_e,4),(_f,5),(_I,6),('other',7),(_g,8),(_W,9)))
_NnMstPortInfoSemState_Type.__name__=_C
_NnMstPortInfoSemState_Object=MibTableColumn
nnMstPortInfoSemState=_NnMstPortInfoSemState_Object((1,3,6,1,4,1,45,5,5,1,4,1,16),_NnMstPortInfoSemState_Type())
nnMstPortInfoSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstPortInfoSemState.setStatus(_A)
class _NnMstPortRoleTransitionSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_K,0),(_h,1),(_i,2),(_j,3)))
_NnMstPortRoleTransitionSemState_Type.__name__=_C
_NnMstPortRoleTransitionSemState_Object=MibTableColumn
nnMstPortRoleTransitionSemState=_NnMstPortRoleTransitionSemState_Object((1,3,6,1,4,1,45,5,5,1,4,1,17),_NnMstPortRoleTransitionSemState_Type())
nnMstPortRoleTransitionSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstPortRoleTransitionSemState.setStatus(_A)
class _NnMstPortStateTransitionSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),(_N,1),(_O,2)))
_NnMstPortStateTransitionSemState_Type.__name__=_C
_NnMstPortStateTransitionSemState_Object=MibTableColumn
nnMstPortStateTransitionSemState=_NnMstPortStateTransitionSemState_Object((1,3,6,1,4,1,45,5,5,1,4,1,18),_NnMstPortStateTransitionSemState_Type())
nnMstPortStateTransitionSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstPortStateTransitionSemState.setStatus(_A)
class _NnMstPortTopologyChangeSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_K,0),(_k,1),(_l,2),(_m,3),(_n,4),(_o,5),(_p,6),(_q,7)))
_NnMstPortTopologyChangeSemState_Type.__name__=_C
_NnMstPortTopologyChangeSemState_Object=MibTableColumn
nnMstPortTopologyChangeSemState=_NnMstPortTopologyChangeSemState_Object((1,3,6,1,4,1,45,5,5,1,4,1,19),_NnMstPortTopologyChangeSemState_Type())
nnMstPortTopologyChangeSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstPortTopologyChangeSemState.setStatus(_A)
_NnMstPortEffectivePortState_Type=TruthValue
_NnMstPortEffectivePortState_Object=MibTableColumn
nnMstPortEffectivePortState=_NnMstPortEffectivePortState_Object((1,3,6,1,4,1,45,5,5,1,4,1,20),_NnMstPortEffectivePortState_Type())
nnMstPortEffectivePortState.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstPortEffectivePortState.setStatus(_A)
_NnMstNotificationControl_ObjectIdentity=ObjectIdentity
nnMstNotificationControl=_NnMstNotificationControl_ObjectIdentity((1,3,6,1,4,1,45,5,5,1,5))
_NnMstNotificationControlScalars_ObjectIdentity=ObjectIdentity
nnMstNotificationControlScalars=_NnMstNotificationControlScalars_ObjectIdentity((1,3,6,1,4,1,45,5,5,1,5,1))
class _NnMstSetNotifications_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_NnMstSetNotifications_Type.__name__=_C
_NnMstSetNotifications_Object=MibScalar
nnMstSetNotifications=_NnMstSetNotifications_Object((1,3,6,1,4,1,45,5,5,1,5,1,1),_NnMstSetNotifications_Type())
nnMstSetNotifications.setMaxAccess(_D)
if mibBuilder.loadTexts:nnMstSetNotifications.setStatus(_A)
class _NnMstGenNotificationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_V,0),('up',1),('down',2),('instanceUp',3),('instanceDown',4)))
_NnMstGenNotificationType_Type.__name__=_C
_NnMstGenNotificationType_Object=MibScalar
nnMstGenNotificationType=_NnMstGenNotificationType_Object((1,3,6,1,4,1,45,5,5,1,5,1,2),_NnMstGenNotificationType_Type())
nnMstGenNotificationType.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstGenNotificationType.setStatus(_A)
class _NnMstErrNotificationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_V,0),('memfail',1),('bufffail',2)))
_NnMstErrNotificationType_Type.__name__=_C
_NnMstErrNotificationType_Object=MibScalar
nnMstErrNotificationType=_NnMstErrNotificationType_Object((1,3,6,1,4,1,45,5,5,1,5,1,3),_NnMstErrNotificationType_Type())
nnMstErrNotificationType.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstErrNotificationType.setStatus(_A)
_NnMstPortNotificationTable_Object=MibTable
nnMstPortNotificationTable=_NnMstPortNotificationTable_Object((1,3,6,1,4,1,45,5,5,1,5,2))
if mibBuilder.loadTexts:nnMstPortNotificationTable.setStatus(_A)
_NnMstPortNotificationEntry_Object=MibTableRow
nnMstPortNotificationEntry=_NnMstPortNotificationEntry_Object((1,3,6,1,4,1,45,5,5,1,5,2,1))
nnMstPortNotificationEntry.setIndexNames((0,_E,_t))
if mibBuilder.loadTexts:nnMstPortNotificationEntry.setStatus(_A)
class _NnMstPortNotificationIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_NnMstPortNotificationIndex_Type.__name__=_C
_NnMstPortNotificationIndex_Object=MibTableColumn
nnMstPortNotificationIndex=_NnMstPortNotificationIndex_Object((1,3,6,1,4,1,45,5,5,1,5,2,1,1),_NnMstPortNotificationIndex_Type())
nnMstPortNotificationIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:nnMstPortNotificationIndex.setStatus(_A)
class _NnMstPortNotificationMigrationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_c,0),(_b,1)))
_NnMstPortNotificationMigrationType_Type.__name__=_C
_NnMstPortNotificationMigrationType_Object=MibTableColumn
nnMstPortNotificationMigrationType=_NnMstPortNotificationMigrationType_Object((1,3,6,1,4,1,45,5,5,1,5,2,1,2),_NnMstPortNotificationMigrationType_Type())
nnMstPortNotificationMigrationType.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstPortNotificationMigrationType.setStatus(_A)
class _NnMstPortNotificationPktErrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('protocolIdErr',0),('invalidBpdu',1),('configLengthErr',2),('tcnLengthErr',3),('rstpLengthErr',4),('maxAgeErr',5),('fwdDelayErr',6),('helloTimeErr',7),('mstpLengthErr',8)))
_NnMstPortNotificationPktErrType_Type.__name__=_C
_NnMstPortNotificationPktErrType_Object=MibTableColumn
nnMstPortNotificationPktErrType=_NnMstPortNotificationPktErrType_Object((1,3,6,1,4,1,45,5,5,1,5,2,1,3),_NnMstPortNotificationPktErrType_Type())
nnMstPortNotificationPktErrType.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstPortNotificationPktErrType.setStatus(_A)
_NnMstPortNotificationPktErrVal_Type=Integer32
_NnMstPortNotificationPktErrVal_Object=MibTableColumn
nnMstPortNotificationPktErrVal=_NnMstPortNotificationPktErrVal_Object((1,3,6,1,4,1,45,5,5,1,5,2,1,4),_NnMstPortNotificationPktErrVal_Type())
nnMstPortNotificationPktErrVal.setMaxAccess(_B)
if mibBuilder.loadTexts:nnMstPortNotificationPktErrVal.setStatus(_A)
_NnMstBridgeVlanMapTable_Object=MibTable
nnMstBridgeVlanMapTable=_NnMstBridgeVlanMapTable_Object((1,3,6,1,4,1,45,5,5,1,6))
if mibBuilder.loadTexts:nnMstBridgeVlanMapTable.setStatus(_A)
_NnMstBridgeVlanMapEntry_Object=MibTableRow
nnMstBridgeVlanMapEntry=_NnMstBridgeVlanMapEntry_Object((1,3,6,1,4,1,45,5,5,1,6,1))
nnMstBridgeVlanMapEntry.setIndexNames((0,_E,_u))
if mibBuilder.loadTexts:nnMstBridgeVlanMapEntry.setStatus(_A)
class _NnMstBridgeInstId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_NnMstBridgeInstId_Type.__name__=_C
_NnMstBridgeInstId_Object=MibTableColumn
nnMstBridgeInstId=_NnMstBridgeInstId_Object((1,3,6,1,4,1,45,5,5,1,6,1,1),_NnMstBridgeInstId_Type())
nnMstBridgeInstId.setMaxAccess(_J)
if mibBuilder.loadTexts:nnMstBridgeInstId.setStatus(_A)
class _NnMstBridgeVlanMap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_NnMstBridgeVlanMap_Type.__name__=_G
_NnMstBridgeVlanMap_Object=MibTableColumn
nnMstBridgeVlanMap=_NnMstBridgeVlanMap_Object((1,3,6,1,4,1,45,5,5,1,6,1,2),_NnMstBridgeVlanMap_Type())
nnMstBridgeVlanMap.setMaxAccess(_D)
if mibBuilder.loadTexts:nnMstBridgeVlanMap.setStatus(_A)
nnMstGeneralEvent=NotificationType((1,3,6,1,4,1,45,5,5,0,1))
nnMstGeneralEvent.setObjects(*((_E,_H),(_E,_v)))
if mibBuilder.loadTexts:nnMstGeneralEvent.setStatus(_A)
nnMstErrorEvent=NotificationType((1,3,6,1,4,1,45,5,5,0,2))
nnMstErrorEvent.setObjects(*((_E,_H),(_E,_w)))
if mibBuilder.loadTexts:nnMstErrorEvent.setStatus(_A)
nnMstNewRoot=NotificationType((1,3,6,1,4,1,45,5,5,0,3))
nnMstNewRoot.setObjects(*((_E,_H),(_E,_x),(_E,_y)))
if mibBuilder.loadTexts:nnMstNewRoot.setStatus(_A)
nnMstTopologyChange=NotificationType((1,3,6,1,4,1,45,5,5,0,4))
nnMstTopologyChange.setObjects((_E,_H))
if mibBuilder.loadTexts:nnMstTopologyChange.setStatus(_A)
nnMstProtocolMigration=NotificationType((1,3,6,1,4,1,45,5,5,0,5))
nnMstProtocolMigration.setObjects(*((_E,_H),(_E,_z),(_E,_A0)))
if mibBuilder.loadTexts:nnMstProtocolMigration.setStatus(_A)
nnMstRegionConfigChange=NotificationType((1,3,6,1,4,1,45,5,5,0,6))
nnMstRegionConfigChange.setObjects(*((_E,_H),(_E,_A1),(_E,_A2),(_E,_A3),(_E,_A4)))
if mibBuilder.loadTexts:nnMstRegionConfigChange.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'nnMultipleSpanningTreeMib':nnMultipleSpanningTreeMib,'nnMstNotifications':nnMstNotifications,'nnMstGeneralEvent':nnMstGeneralEvent,'nnMstErrorEvent':nnMstErrorEvent,'nnMstNewRoot':nnMstNewRoot,'nnMstTopologyChange':nnMstTopologyChange,'nnMstProtocolMigration':nnMstProtocolMigration,'nnMstRegionConfigChange':nnMstRegionConfigChange,'nnMstObjects':nnMstObjects,'nnMstScalars':nnMstScalars,'nnMstNoOfInstancesSupported':nnMstNoOfInstancesSupported,'nnMstMaxHopCount':nnMstMaxHopCount,_H:nnMstBrgAddress,'nnMstCistRoot':nnMstCistRoot,'nnMstCistRegionalRoot':nnMstCistRegionalRoot,'nnMstCistRootCost':nnMstCistRootCost,'nnMstCistRegionalRootCost':nnMstCistRegionalRootCost,'nnMstCistRootPort':nnMstCistRootPort,'nnMstCistBridgePriority':nnMstCistBridgePriority,'nnMstCistBridgeMaxAge':nnMstCistBridgeMaxAge,'nnMstCistBridgeForwardDelay':nnMstCistBridgeForwardDelay,'nnMstCistHoldTime':nnMstCistHoldTime,'nnMstCistMaxAge':nnMstCistMaxAge,'nnMstCistForwardDelay':nnMstCistForwardDelay,'nnMstMstpUpCount':nnMstMstpUpCount,'nnMstMstpDownCount':nnMstMstpDownCount,'nnMstPathCostDefaultType':nnMstPathCostDefaultType,_z:nnMstForceProtocolVersion,'nnMstTxHoldCount':nnMstTxHoldCount,_A1:nnMstConfigIdSel,_A2:nnMstRegionName,_A3:nnMstRegionVersion,_A4:nnMstConfigDigest,'nnMstRegionConfigChangeCount':nnMstRegionConfigChangeCount,'nnMstCistBridgeRoleSelectionSemState':nnMstCistBridgeRoleSelectionSemState,'nnMstCistTimeSinceTopologyChange':nnMstCistTimeSinceTopologyChange,'nnMstCistTopChanges':nnMstCistTopChanges,'nnMstCistNewRootBridgeCount':nnMstCistNewRootBridgeCount,'nnMstBridgeTable':nnMstBridgeTable,'nnMstBridgeEntry':nnMstBridgeEntry,_T:nnMstBridgeInstance,_y:nnMstBridgeRegionalRoot,'nnMstBridgePriority':nnMstBridgePriority,'nnMstBridgeRootCost':nnMstBridgeRootCost,'nnMstBridgeRootPort':nnMstBridgeRootPort,'nnMstBridgeTimeSinceTopologyChange':nnMstBridgeTimeSinceTopologyChange,'nnMstBridgeTopChanges':nnMstBridgeTopChanges,'nnMstBridgeNewRootCount':nnMstBridgeNewRootCount,'nnMstBridgeRoleSelectionSemState':nnMstBridgeRoleSelectionSemState,'nnMstBridgeInstanceUpCount':nnMstBridgeInstanceUpCount,'nnMstBridgeInstanceDownCount':nnMstBridgeInstanceDownCount,_x:nnMstBridgeOldDesignatedRoot,'nnMstBridgeEnabled':nnMstBridgeEnabled,'nnMstBridgeRowStatus':nnMstBridgeRowStatus,'nnMstBridgeMappedVlans':nnMstBridgeMappedVlans,'nnMstBridgeMappedVlansAction':nnMstBridgeMappedVlansAction,'nnMstCistPortTable':nnMstCistPortTable,'nnMstCistPortEntry':nnMstCistPortEntry,_a:nnMstCistPort,'nnMstCistPortPathCost':nnMstCistPortPathCost,'nnMstCistPortPriority':nnMstCistPortPriority,'nnMstCistPortDesignatedRoot':nnMstCistPortDesignatedRoot,'nnMstCistPortDesignatedBridge':nnMstCistPortDesignatedBridge,'nnMstCistPortDesignatedPort':nnMstCistPortDesignatedPort,'nnMstCistPortAdminP2P':nnMstCistPortAdminP2P,'nnMstCistPortOperP2P':nnMstCistPortOperP2P,'nnMstCistPortAdminEdgeStatus':nnMstCistPortAdminEdgeStatus,'nnMstCistPortOperEdgeStatus':nnMstCistPortOperEdgeStatus,'nnMstCistPortProtocolMigration':nnMstCistPortProtocolMigration,'nnMstCistPortState':nnMstCistPortState,'nnMstCistForcePortState':nnMstCistForcePortState,'nnMstCistPortForwardTransitions':nnMstCistPortForwardTransitions,'nnMstCistPortRxMstBpduCount':nnMstCistPortRxMstBpduCount,'nnMstCistPortRxRstBpduCount':nnMstCistPortRxRstBpduCount,'nnMstCistPortRxConfigBpduCount':nnMstCistPortRxConfigBpduCount,'nnMstCistPortRxTcnBpduCount':nnMstCistPortRxTcnBpduCount,'nnMstCistPortTxMstBpduCount':nnMstCistPortTxMstBpduCount,'nnMstCistPortTxRstBpduCount':nnMstCistPortTxRstBpduCount,'nnMstCistPortTxConfigBpduCount':nnMstCistPortTxConfigBpduCount,'nnMstCistPortTxTcnBpduCount':nnMstCistPortTxTcnBpduCount,'nnMstCistPortInvalidMstBpduRxCount':nnMstCistPortInvalidMstBpduRxCount,'nnMstCistPortInvalidRstBpduRxCount':nnMstCistPortInvalidRstBpduRxCount,'nnMstCistPortInvalidConfigBpduRxCount':nnMstCistPortInvalidConfigBpduRxCount,'nnMstCistPortInvalidTcnBpduRxCount':nnMstCistPortInvalidTcnBpduRxCount,'nnMstCistPortTransmitSemState':nnMstCistPortTransmitSemState,'nnMstCistPortReceiveSemState':nnMstCistPortReceiveSemState,'nnMstCistPortProtMigrationSemState':nnMstCistPortProtMigrationSemState,'nnMstCistProtocolMigrationCount':nnMstCistProtocolMigrationCount,'nnMstCistPortDesignatedCost':nnMstCistPortDesignatedCost,'nnMstCistPortRegionalRoot':nnMstCistPortRegionalRoot,'nnMstCistPortRegionalPathCost':nnMstCistPortRegionalPathCost,'nnMstCistSelectedPortRole':nnMstCistSelectedPortRole,'nnMstCistCurrentPortRole':nnMstCistCurrentPortRole,'nnMstCistPortInfoSemState':nnMstCistPortInfoSemState,'nnMstCistPortRoleTransitionSemState':nnMstCistPortRoleTransitionSemState,'nnMstCistPortStateTransitionSemState':nnMstCistPortStateTransitionSemState,'nnMstCistPortTopologyChangeSemState':nnMstCistPortTopologyChangeSemState,'nnMstCistPortHelloTime':nnMstCistPortHelloTime,'nnMstCistPortOperVersion':nnMstCistPortOperVersion,'nnMstCistPortEffectivePortState':nnMstCistPortEffectivePortState,'nnMstCistPortRxTcBpduCount':nnMstCistPortRxTcBpduCount,'nnMstPortTable':nnMstPortTable,'nnMstPortEntry':nnMstPortEntry,_r:nnMstPort,'nnMstPortPathCost':nnMstPortPathCost,'nnMstPortPriority':nnMstPortPriority,'nnMstPortDesignatedRoot':nnMstPortDesignatedRoot,'nnMstPortDesignatedBridge':nnMstPortDesignatedBridge,'nnMstPortDesignatedPort':nnMstPortDesignatedPort,'nnMstPortState':nnMstPortState,'nnMstPortForcePortState':nnMstPortForcePortState,'nnMstPortForwardTransitions':nnMstPortForwardTransitions,'nnMstPortReceivedBPDUs':nnMstPortReceivedBPDUs,'nnMstPortTransmittedBPDUs':nnMstPortTransmittedBPDUs,'nnMstPortInvalidBPDUsRcvd':nnMstPortInvalidBPDUsRcvd,'nnMstPortDesignatedCost':nnMstPortDesignatedCost,'nnMstPortSelectedPortRole':nnMstPortSelectedPortRole,'nnMstPortCurrentPortRole':nnMstPortCurrentPortRole,'nnMstPortInfoSemState':nnMstPortInfoSemState,'nnMstPortRoleTransitionSemState':nnMstPortRoleTransitionSemState,'nnMstPortStateTransitionSemState':nnMstPortStateTransitionSemState,'nnMstPortTopologyChangeSemState':nnMstPortTopologyChangeSemState,'nnMstPortEffectivePortState':nnMstPortEffectivePortState,'nnMstNotificationControl':nnMstNotificationControl,'nnMstNotificationControlScalars':nnMstNotificationControlScalars,'nnMstSetNotifications':nnMstSetNotifications,_v:nnMstGenNotificationType,_w:nnMstErrNotificationType,'nnMstPortNotificationTable':nnMstPortNotificationTable,'nnMstPortNotificationEntry':nnMstPortNotificationEntry,_t:nnMstPortNotificationIndex,_A0:nnMstPortNotificationMigrationType,'nnMstPortNotificationPktErrType':nnMstPortNotificationPktErrType,'nnMstPortNotificationPktErrVal':nnMstPortNotificationPktErrVal,'nnMstBridgeVlanMapTable':nnMstBridgeVlanMapTable,'nnMstBridgeVlanMapEntry':nnMstBridgeVlanMapEntry,_u:nnMstBridgeInstId,'nnMstBridgeVlanMap':nnMstBridgeVlanMap})