_AQ='fsMstMstiPortState'
_AP='fsMstCistPortState'
_AO='fsMstOldRoleType'
_AN='fsMstPortRoleType'
_AM='fsMstMstiConfigDigest'
_AL='fsMstMstiRegionVersion'
_AK='fsMstMstiRegionName'
_AJ='fsMstMstiConfigIdSel'
_AI='fsMstPktErrVal'
_AH='fsMstPktErrType'
_AG='fsMstPortMigrationType'
_AF='fsMstForceProtocolVersion'
_AE='fsMstMstiTopChanges'
_AD='fsMstMstiBridgeRegionalRoot'
_AC='fsMstOldDesignatedRoot'
_AB='fsMstErrTrapType'
_AA='fsMstInstanceDownCount'
_A9='fsMstInstanceUpCount'
_A8='fsMstGenTrapType'
_A7='designatedPort'
_A6='backupPort'
_A5='alternatePort'
_A4='disabledPort'
_A3='fsMstPort'
_A2='fsMstMstiPort'
_A1='timerExpiryEvent'
_A0='bpduEvent'
_z='configurationEvent'
_y='acknowledged'
_x='propagating'
_w='notifiedtc'
_v='notifiedtcn'
_u='active'
_t='detected'
_s='inactive'
_r='alternateport'
_q='designatedport'
_p='rootport'
_o='disabledport'
_n='disableport'
_m='present'
_l='notdesg'
_k='inferiordesg'
_j='repeatdesg'
_i='superiordesg'
_h='update'
_g='sendstp'
_f='sendrstp'
_e='fsMstCistPort'
_d='roleselection'
_c='initbridge'
_b='stpCompatible'
_a='fsMstPortTrapIndex'
_Z='none'
_Y='init'
_X='receive'
_W='fsMstInstanceIndex'
_V='fsMstMstiInstanceIndex'
_U='enabled'
_T='masterport'
_S='designated'
_R='root'
_Q='backup'
_P='alternate'
_O='forwarding'
_N='discarding'
_M='Timeout'
_L='learning'
_K='not-accessible'
_J='TruthValue'
_I='centi-seconds'
_H='fsMstBrgAddress'
_G='disabled'
_F='OctetString'
_E='SUPERMICRO-MST-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_J)
futureMstMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,1,80))
if mibBuilder.loadTexts:futureMstMIB.setRevisions(('2012-09-05 00:00',))
class VlanId(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
class BridgeId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class Timeout(TextualConvention,Integer32):status=_A;displayHint='d4'
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_G,2)))
_Dot1sFutureMst_ObjectIdentity=ObjectIdentity
dot1sFutureMst=_Dot1sFutureMst_ObjectIdentity((1,3,6,1,4,1,10876,101,1,80,1))
class _FsMstSystemControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsMstSystemControl_Type.__name__=_C
_FsMstSystemControl_Object=MibScalar
fsMstSystemControl=_FsMstSystemControl_Object((1,3,6,1,4,1,10876,101,1,80,1,1),_FsMstSystemControl_Type())
fsMstSystemControl.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstSystemControl.setStatus(_A)
_FsMstModuleStatus_Type=EnabledStatus
_FsMstModuleStatus_Object=MibScalar
fsMstModuleStatus=_FsMstModuleStatus_Object((1,3,6,1,4,1,10876,101,1,80,1,2),_FsMstModuleStatus_Type())
fsMstModuleStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstModuleStatus.setStatus(_A)
class _FsMstMaxMstInstanceNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_FsMstMaxMstInstanceNumber_Type.__name__=_C
_FsMstMaxMstInstanceNumber_Object=MibScalar
fsMstMaxMstInstanceNumber=_FsMstMaxMstInstanceNumber_Object((1,3,6,1,4,1,10876,101,1,80,1,3),_FsMstMaxMstInstanceNumber_Type())
fsMstMaxMstInstanceNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstMaxMstInstanceNumber.setStatus(_A)
_FsMstNoOfMstiSupported_Type=Integer32
_FsMstNoOfMstiSupported_Object=MibScalar
fsMstNoOfMstiSupported=_FsMstNoOfMstiSupported_Object((1,3,6,1,4,1,10876,101,1,80,1,4),_FsMstNoOfMstiSupported_Type())
fsMstNoOfMstiSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstNoOfMstiSupported.setStatus(_A)
class _FsMstMaxHopCount_Type(Integer32):defaultValue=2000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(600,4000))
_FsMstMaxHopCount_Type.__name__=_C
_FsMstMaxHopCount_Object=MibScalar
fsMstMaxHopCount=_FsMstMaxHopCount_Object((1,3,6,1,4,1,10876,101,1,80,1,5),_FsMstMaxHopCount_Type())
fsMstMaxHopCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstMaxHopCount.setStatus(_A)
_FsMstBrgAddress_Type=MacAddress
_FsMstBrgAddress_Object=MibScalar
fsMstBrgAddress=_FsMstBrgAddress_Object((1,3,6,1,4,1,10876,101,1,80,1,6),_FsMstBrgAddress_Type())
fsMstBrgAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstBrgAddress.setStatus(_A)
_FsMstCistRoot_Type=BridgeId
_FsMstCistRoot_Object=MibScalar
fsMstCistRoot=_FsMstCistRoot_Object((1,3,6,1,4,1,10876,101,1,80,1,7),_FsMstCistRoot_Type())
fsMstCistRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistRoot.setStatus(_A)
_FsMstCistRegionalRoot_Type=BridgeId
_FsMstCistRegionalRoot_Object=MibScalar
fsMstCistRegionalRoot=_FsMstCistRegionalRoot_Object((1,3,6,1,4,1,10876,101,1,80,1,8),_FsMstCistRegionalRoot_Type())
fsMstCistRegionalRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistRegionalRoot.setStatus(_A)
_FsMstCistRootCost_Type=Integer32
_FsMstCistRootCost_Object=MibScalar
fsMstCistRootCost=_FsMstCistRootCost_Object((1,3,6,1,4,1,10876,101,1,80,1,9),_FsMstCistRootCost_Type())
fsMstCistRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistRootCost.setStatus(_A)
_FsMstCistRegionalRootCost_Type=Integer32
_FsMstCistRegionalRootCost_Object=MibScalar
fsMstCistRegionalRootCost=_FsMstCistRegionalRootCost_Object((1,3,6,1,4,1,10876,101,1,80,1,10),_FsMstCistRegionalRootCost_Type())
fsMstCistRegionalRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistRegionalRootCost.setStatus(_A)
_FsMstCistRootPort_Type=Integer32
_FsMstCistRootPort_Object=MibScalar
fsMstCistRootPort=_FsMstCistRootPort_Object((1,3,6,1,4,1,10876,101,1,80,1,11),_FsMstCistRootPort_Type())
fsMstCistRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistRootPort.setStatus(_A)
class _FsMstCistBridgePriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_FsMstCistBridgePriority_Type.__name__=_C
_FsMstCistBridgePriority_Object=MibScalar
fsMstCistBridgePriority=_FsMstCistBridgePriority_Object((1,3,6,1,4,1,10876,101,1,80,1,12),_FsMstCistBridgePriority_Type())
fsMstCistBridgePriority.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstCistBridgePriority.setStatus(_A)
class _FsMstCistBridgeMaxAge_Type(Timeout):defaultValue=2000;subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(600,4000))
_FsMstCistBridgeMaxAge_Type.__name__=_M
_FsMstCistBridgeMaxAge_Object=MibScalar
fsMstCistBridgeMaxAge=_FsMstCistBridgeMaxAge_Object((1,3,6,1,4,1,10876,101,1,80,1,13),_FsMstCistBridgeMaxAge_Type())
fsMstCistBridgeMaxAge.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstCistBridgeMaxAge.setStatus(_A)
if mibBuilder.loadTexts:fsMstCistBridgeMaxAge.setUnits(_I)
class _FsMstCistBridgeForwardDelay_Type(Timeout):defaultValue=1500;subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(400,3000))
_FsMstCistBridgeForwardDelay_Type.__name__=_M
_FsMstCistBridgeForwardDelay_Object=MibScalar
fsMstCistBridgeForwardDelay=_FsMstCistBridgeForwardDelay_Object((1,3,6,1,4,1,10876,101,1,80,1,14),_FsMstCistBridgeForwardDelay_Type())
fsMstCistBridgeForwardDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstCistBridgeForwardDelay.setStatus(_A)
if mibBuilder.loadTexts:fsMstCistBridgeForwardDelay.setUnits(_I)
_FsMstCistHoldTime_Type=Integer32
_FsMstCistHoldTime_Object=MibScalar
fsMstCistHoldTime=_FsMstCistHoldTime_Object((1,3,6,1,4,1,10876,101,1,80,1,15),_FsMstCistHoldTime_Type())
fsMstCistHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistHoldTime.setStatus(_A)
if mibBuilder.loadTexts:fsMstCistHoldTime.setUnits(_I)
_FsMstCistMaxAge_Type=Timeout
_FsMstCistMaxAge_Object=MibScalar
fsMstCistMaxAge=_FsMstCistMaxAge_Object((1,3,6,1,4,1,10876,101,1,80,1,16),_FsMstCistMaxAge_Type())
fsMstCistMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistMaxAge.setStatus(_A)
if mibBuilder.loadTexts:fsMstCistMaxAge.setUnits(_I)
_FsMstCistForwardDelay_Type=Timeout
_FsMstCistForwardDelay_Object=MibScalar
fsMstCistForwardDelay=_FsMstCistForwardDelay_Object((1,3,6,1,4,1,10876,101,1,80,1,17),_FsMstCistForwardDelay_Type())
fsMstCistForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistForwardDelay.setStatus(_A)
if mibBuilder.loadTexts:fsMstCistForwardDelay.setUnits(_I)
_FsMstMstpUpCount_Type=Counter32
_FsMstMstpUpCount_Object=MibScalar
fsMstMstpUpCount=_FsMstMstpUpCount_Object((1,3,6,1,4,1,10876,101,1,80,1,18),_FsMstMstpUpCount_Type())
fsMstMstpUpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstpUpCount.setStatus(_A)
_FsMstMstpDownCount_Type=Counter32
_FsMstMstpDownCount_Object=MibScalar
fsMstMstpDownCount=_FsMstMstpDownCount_Object((1,3,6,1,4,1,10876,101,1,80,1,19),_FsMstMstpDownCount_Type())
fsMstMstpDownCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstpDownCount.setStatus(_A)
class _FsMstPathCostDefaultType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stp8021d1998',1),('stp8021t2001',2)))
_FsMstPathCostDefaultType_Type.__name__=_C
_FsMstPathCostDefaultType_Object=MibScalar
fsMstPathCostDefaultType=_FsMstPathCostDefaultType_Object((1,3,6,1,4,1,10876,101,1,80,1,20),_FsMstPathCostDefaultType_Type())
fsMstPathCostDefaultType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstPathCostDefaultType.setStatus('obsolete')
class _FsMstTrace_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMstTrace_Type.__name__=_C
_FsMstTrace_Object=MibScalar
fsMstTrace=_FsMstTrace_Object((1,3,6,1,4,1,10876,101,1,80,1,21),_FsMstTrace_Type())
fsMstTrace.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstTrace.setStatus(_A)
class _FsMstDebug_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,524287))
_FsMstDebug_Type.__name__=_C
_FsMstDebug_Object=MibScalar
fsMstDebug=_FsMstDebug_Object((1,3,6,1,4,1,10876,101,1,80,1,22),_FsMstDebug_Type())
fsMstDebug.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstDebug.setStatus(_A)
class _FsMstForceProtocolVersion_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3)));namedValues=NamedValues(*((_b,0),('rstp',2),('mstp',3)))
_FsMstForceProtocolVersion_Type.__name__=_C
_FsMstForceProtocolVersion_Object=MibScalar
fsMstForceProtocolVersion=_FsMstForceProtocolVersion_Object((1,3,6,1,4,1,10876,101,1,80,1,23),_FsMstForceProtocolVersion_Type())
fsMstForceProtocolVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstForceProtocolVersion.setStatus(_A)
class _FsMstTxHoldCount_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FsMstTxHoldCount_Type.__name__=_C
_FsMstTxHoldCount_Object=MibScalar
fsMstTxHoldCount=_FsMstTxHoldCount_Object((1,3,6,1,4,1,10876,101,1,80,1,24),_FsMstTxHoldCount_Type())
fsMstTxHoldCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstTxHoldCount.setStatus(_A)
class _FsMstMstiConfigIdSel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMstMstiConfigIdSel_Type.__name__=_C
_FsMstMstiConfigIdSel_Object=MibScalar
fsMstMstiConfigIdSel=_FsMstMstiConfigIdSel_Object((1,3,6,1,4,1,10876,101,1,80,1,25),_FsMstMstiConfigIdSel_Type())
fsMstMstiConfigIdSel.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstMstiConfigIdSel.setStatus(_A)
class _FsMstMstiRegionName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsMstMstiRegionName_Type.__name__=_F
_FsMstMstiRegionName_Object=MibScalar
fsMstMstiRegionName=_FsMstMstiRegionName_Object((1,3,6,1,4,1,10876,101,1,80,1,26),_FsMstMstiRegionName_Type())
fsMstMstiRegionName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstMstiRegionName.setStatus(_A)
class _FsMstMstiRegionVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMstMstiRegionVersion_Type.__name__=_C
_FsMstMstiRegionVersion_Object=MibScalar
fsMstMstiRegionVersion=_FsMstMstiRegionVersion_Object((1,3,6,1,4,1,10876,101,1,80,1,27),_FsMstMstiRegionVersion_Type())
fsMstMstiRegionVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstMstiRegionVersion.setStatus(_A)
class _FsMstMstiConfigDigest_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsMstMstiConfigDigest_Type.__name__=_F
_FsMstMstiConfigDigest_Object=MibScalar
fsMstMstiConfigDigest=_FsMstMstiConfigDigest_Object((1,3,6,1,4,1,10876,101,1,80,1,28),_FsMstMstiConfigDigest_Type())
fsMstMstiConfigDigest.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstiConfigDigest.setStatus(_A)
_FsMstBufferOverFlowCount_Type=Counter32
_FsMstBufferOverFlowCount_Object=MibScalar
fsMstBufferOverFlowCount=_FsMstBufferOverFlowCount_Object((1,3,6,1,4,1,10876,101,1,80,1,29),_FsMstBufferOverFlowCount_Type())
fsMstBufferOverFlowCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstBufferOverFlowCount.setStatus(_A)
_FsMstMemAllocFailureCount_Type=Counter32
_FsMstMemAllocFailureCount_Object=MibScalar
fsMstMemAllocFailureCount=_FsMstMemAllocFailureCount_Object((1,3,6,1,4,1,10876,101,1,80,1,30),_FsMstMemAllocFailureCount_Type())
fsMstMemAllocFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMemAllocFailureCount.setStatus(_A)
_FsMstRegionConfigChangeCount_Type=Counter32
_FsMstRegionConfigChangeCount_Object=MibScalar
fsMstRegionConfigChangeCount=_FsMstRegionConfigChangeCount_Object((1,3,6,1,4,1,10876,101,1,80,1,31),_FsMstRegionConfigChangeCount_Type())
fsMstRegionConfigChangeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstRegionConfigChangeCount.setStatus(_A)
class _FsMstCistBridgeRoleSelectionSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_c,0),(_d,1)))
_FsMstCistBridgeRoleSelectionSemState_Type.__name__=_C
_FsMstCistBridgeRoleSelectionSemState_Object=MibScalar
fsMstCistBridgeRoleSelectionSemState=_FsMstCistBridgeRoleSelectionSemState_Object((1,3,6,1,4,1,10876,101,1,80,1,32),_FsMstCistBridgeRoleSelectionSemState_Type())
fsMstCistBridgeRoleSelectionSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistBridgeRoleSelectionSemState.setStatus(_A)
_FsMstCistTimeSinceTopologyChange_Type=TimeTicks
_FsMstCistTimeSinceTopologyChange_Object=MibScalar
fsMstCistTimeSinceTopologyChange=_FsMstCistTimeSinceTopologyChange_Object((1,3,6,1,4,1,10876,101,1,80,1,33),_FsMstCistTimeSinceTopologyChange_Type())
fsMstCistTimeSinceTopologyChange.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistTimeSinceTopologyChange.setStatus(_A)
if mibBuilder.loadTexts:fsMstCistTimeSinceTopologyChange.setUnits(_I)
_FsMstCistTopChanges_Type=Counter32
_FsMstCistTopChanges_Object=MibScalar
fsMstCistTopChanges=_FsMstCistTopChanges_Object((1,3,6,1,4,1,10876,101,1,80,1,34),_FsMstCistTopChanges_Type())
fsMstCistTopChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistTopChanges.setStatus(_A)
_FsMstCistNewRootBridgeCount_Type=Counter32
_FsMstCistNewRootBridgeCount_Object=MibScalar
fsMstCistNewRootBridgeCount=_FsMstCistNewRootBridgeCount_Object((1,3,6,1,4,1,10876,101,1,80,1,35),_FsMstCistNewRootBridgeCount_Type())
fsMstCistNewRootBridgeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistNewRootBridgeCount.setStatus(_A)
_FsMstCistHelloTime_Type=Timeout
_FsMstCistHelloTime_Object=MibScalar
fsMstCistHelloTime=_FsMstCistHelloTime_Object((1,3,6,1,4,1,10876,101,1,80,1,36),_FsMstCistHelloTime_Type())
fsMstCistHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistHelloTime.setStatus(_A)
if mibBuilder.loadTexts:fsMstCistHelloTime.setUnits(_I)
class _FsMstCistBridgeHelloTime_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,100),ValueRangeConstraint(200,200))
_FsMstCistBridgeHelloTime_Type.__name__=_M
_FsMstCistBridgeHelloTime_Object=MibScalar
fsMstCistBridgeHelloTime=_FsMstCistBridgeHelloTime_Object((1,3,6,1,4,1,10876,101,1,80,1,37),_FsMstCistBridgeHelloTime_Type())
fsMstCistBridgeHelloTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstCistBridgeHelloTime.setStatus(_A)
if mibBuilder.loadTexts:fsMstCistBridgeHelloTime.setUnits(_I)
_FsMstMstiBridgeTable_Object=MibTable
fsMstMstiBridgeTable=_FsMstMstiBridgeTable_Object((1,3,6,1,4,1,10876,101,1,80,1,38))
if mibBuilder.loadTexts:fsMstMstiBridgeTable.setStatus(_A)
_FsMstMstiBridgeEntry_Object=MibTableRow
fsMstMstiBridgeEntry=_FsMstMstiBridgeEntry_Object((1,3,6,1,4,1,10876,101,1,80,1,38,1))
fsMstMstiBridgeEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:fsMstMstiBridgeEntry.setStatus(_A)
class _FsMstMstiInstanceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64),ValueRangeConstraint(4094,4094))
_FsMstMstiInstanceIndex_Type.__name__=_C
_FsMstMstiInstanceIndex_Object=MibTableColumn
fsMstMstiInstanceIndex=_FsMstMstiInstanceIndex_Object((1,3,6,1,4,1,10876,101,1,80,1,38,1,1),_FsMstMstiInstanceIndex_Type())
fsMstMstiInstanceIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:fsMstMstiInstanceIndex.setStatus(_A)
_FsMstMstiBridgeRegionalRoot_Type=BridgeId
_FsMstMstiBridgeRegionalRoot_Object=MibTableColumn
fsMstMstiBridgeRegionalRoot=_FsMstMstiBridgeRegionalRoot_Object((1,3,6,1,4,1,10876,101,1,80,1,38,1,2),_FsMstMstiBridgeRegionalRoot_Type())
fsMstMstiBridgeRegionalRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstiBridgeRegionalRoot.setStatus(_A)
class _FsMstMstiBridgePriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_FsMstMstiBridgePriority_Type.__name__=_C
_FsMstMstiBridgePriority_Object=MibTableColumn
fsMstMstiBridgePriority=_FsMstMstiBridgePriority_Object((1,3,6,1,4,1,10876,101,1,80,1,38,1,3),_FsMstMstiBridgePriority_Type())
fsMstMstiBridgePriority.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstMstiBridgePriority.setStatus(_A)
_FsMstMstiRootCost_Type=Integer32
_FsMstMstiRootCost_Object=MibTableColumn
fsMstMstiRootCost=_FsMstMstiRootCost_Object((1,3,6,1,4,1,10876,101,1,80,1,38,1,4),_FsMstMstiRootCost_Type())
fsMstMstiRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstiRootCost.setStatus(_A)
_FsMstMstiRootPort_Type=Integer32
_FsMstMstiRootPort_Object=MibTableColumn
fsMstMstiRootPort=_FsMstMstiRootPort_Object((1,3,6,1,4,1,10876,101,1,80,1,38,1,5),_FsMstMstiRootPort_Type())
fsMstMstiRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstiRootPort.setStatus(_A)
_FsMstMstiTimeSinceTopologyChange_Type=TimeTicks
_FsMstMstiTimeSinceTopologyChange_Object=MibTableColumn
fsMstMstiTimeSinceTopologyChange=_FsMstMstiTimeSinceTopologyChange_Object((1,3,6,1,4,1,10876,101,1,80,1,38,1,6),_FsMstMstiTimeSinceTopologyChange_Type())
fsMstMstiTimeSinceTopologyChange.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstiTimeSinceTopologyChange.setStatus(_A)
if mibBuilder.loadTexts:fsMstMstiTimeSinceTopologyChange.setUnits(_I)
_FsMstMstiTopChanges_Type=Counter32
_FsMstMstiTopChanges_Object=MibTableColumn
fsMstMstiTopChanges=_FsMstMstiTopChanges_Object((1,3,6,1,4,1,10876,101,1,80,1,38,1,7),_FsMstMstiTopChanges_Type())
fsMstMstiTopChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstiTopChanges.setStatus(_A)
_FsMstMstiNewRootBridgeCount_Type=Counter32
_FsMstMstiNewRootBridgeCount_Object=MibTableColumn
fsMstMstiNewRootBridgeCount=_FsMstMstiNewRootBridgeCount_Object((1,3,6,1,4,1,10876,101,1,80,1,38,1,8),_FsMstMstiNewRootBridgeCount_Type())
fsMstMstiNewRootBridgeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstiNewRootBridgeCount.setStatus(_A)
class _FsMstMstiBridgeRoleSelectionSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_c,0),(_d,1)))
_FsMstMstiBridgeRoleSelectionSemState_Type.__name__=_C
_FsMstMstiBridgeRoleSelectionSemState_Object=MibTableColumn
fsMstMstiBridgeRoleSelectionSemState=_FsMstMstiBridgeRoleSelectionSemState_Object((1,3,6,1,4,1,10876,101,1,80,1,38,1,9),_FsMstMstiBridgeRoleSelectionSemState_Type())
fsMstMstiBridgeRoleSelectionSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstiBridgeRoleSelectionSemState.setStatus(_A)
_FsMstInstanceUpCount_Type=Counter32
_FsMstInstanceUpCount_Object=MibTableColumn
fsMstInstanceUpCount=_FsMstInstanceUpCount_Object((1,3,6,1,4,1,10876,101,1,80,1,38,1,10),_FsMstInstanceUpCount_Type())
fsMstInstanceUpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstInstanceUpCount.setStatus(_A)
_FsMstInstanceDownCount_Type=Counter32
_FsMstInstanceDownCount_Object=MibTableColumn
fsMstInstanceDownCount=_FsMstInstanceDownCount_Object((1,3,6,1,4,1,10876,101,1,80,1,38,1,11),_FsMstInstanceDownCount_Type())
fsMstInstanceDownCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstInstanceDownCount.setStatus(_A)
_FsMstOldDesignatedRoot_Type=BridgeId
_FsMstOldDesignatedRoot_Object=MibTableColumn
fsMstOldDesignatedRoot=_FsMstOldDesignatedRoot_Object((1,3,6,1,4,1,10876,101,1,80,1,38,1,12),_FsMstOldDesignatedRoot_Type())
fsMstOldDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstOldDesignatedRoot.setStatus(_A)
_FsMstVlanInstanceMappingTable_Object=MibTable
fsMstVlanInstanceMappingTable=_FsMstVlanInstanceMappingTable_Object((1,3,6,1,4,1,10876,101,1,80,1,39))
if mibBuilder.loadTexts:fsMstVlanInstanceMappingTable.setStatus(_A)
_FsMstVlanInstanceMappingEntry_Object=MibTableRow
fsMstVlanInstanceMappingEntry=_FsMstVlanInstanceMappingEntry_Object((1,3,6,1,4,1,10876,101,1,80,1,39,1))
fsMstVlanInstanceMappingEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:fsMstVlanInstanceMappingEntry.setStatus(_A)
class _FsMstInstanceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64),ValueRangeConstraint(4094,4094))
_FsMstInstanceIndex_Type.__name__=_C
_FsMstInstanceIndex_Object=MibTableColumn
fsMstInstanceIndex=_FsMstInstanceIndex_Object((1,3,6,1,4,1,10876,101,1,80,1,39,1,1),_FsMstInstanceIndex_Type())
fsMstInstanceIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:fsMstInstanceIndex.setStatus(_A)
_FsMstMapVlanIndex_Type=VlanId
_FsMstMapVlanIndex_Object=MibTableColumn
fsMstMapVlanIndex=_FsMstMapVlanIndex_Object((1,3,6,1,4,1,10876,101,1,80,1,39,1,2),_FsMstMapVlanIndex_Type())
fsMstMapVlanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstMapVlanIndex.setStatus(_A)
_FsMstUnMapVlanIndex_Type=VlanId
_FsMstUnMapVlanIndex_Object=MibTableColumn
fsMstUnMapVlanIndex=_FsMstUnMapVlanIndex_Object((1,3,6,1,4,1,10876,101,1,80,1,39,1,3),_FsMstUnMapVlanIndex_Type())
fsMstUnMapVlanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstUnMapVlanIndex.setStatus(_A)
class _FsMstSetVlanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_FsMstSetVlanList_Type.__name__=_F
_FsMstSetVlanList_Object=MibTableColumn
fsMstSetVlanList=_FsMstSetVlanList_Object((1,3,6,1,4,1,10876,101,1,80,1,39,1,4),_FsMstSetVlanList_Type())
fsMstSetVlanList.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstSetVlanList.setStatus(_A)
class _FsMstResetVlanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_FsMstResetVlanList_Type.__name__=_F
_FsMstResetVlanList_Object=MibTableColumn
fsMstResetVlanList=_FsMstResetVlanList_Object((1,3,6,1,4,1,10876,101,1,80,1,39,1,5),_FsMstResetVlanList_Type())
fsMstResetVlanList.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstResetVlanList.setStatus(_A)
class _FsMstInstanceVlanMapped_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FsMstInstanceVlanMapped_Type.__name__=_F
_FsMstInstanceVlanMapped_Object=MibTableColumn
fsMstInstanceVlanMapped=_FsMstInstanceVlanMapped_Object((1,3,6,1,4,1,10876,101,1,80,1,39,1,6),_FsMstInstanceVlanMapped_Type())
fsMstInstanceVlanMapped.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstInstanceVlanMapped.setStatus(_A)
class _FsMstInstanceVlanMapped2k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FsMstInstanceVlanMapped2k_Type.__name__=_F
_FsMstInstanceVlanMapped2k_Object=MibTableColumn
fsMstInstanceVlanMapped2k=_FsMstInstanceVlanMapped2k_Object((1,3,6,1,4,1,10876,101,1,80,1,39,1,7),_FsMstInstanceVlanMapped2k_Type())
fsMstInstanceVlanMapped2k.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstInstanceVlanMapped2k.setStatus(_A)
class _FsMstInstanceVlanMapped3k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FsMstInstanceVlanMapped3k_Type.__name__=_F
_FsMstInstanceVlanMapped3k_Object=MibTableColumn
fsMstInstanceVlanMapped3k=_FsMstInstanceVlanMapped3k_Object((1,3,6,1,4,1,10876,101,1,80,1,39,1,8),_FsMstInstanceVlanMapped3k_Type())
fsMstInstanceVlanMapped3k.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstInstanceVlanMapped3k.setStatus(_A)
class _FsMstInstanceVlanMapped4k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FsMstInstanceVlanMapped4k_Type.__name__=_F
_FsMstInstanceVlanMapped4k_Object=MibTableColumn
fsMstInstanceVlanMapped4k=_FsMstInstanceVlanMapped4k_Object((1,3,6,1,4,1,10876,101,1,80,1,39,1,9),_FsMstInstanceVlanMapped4k_Type())
fsMstInstanceVlanMapped4k.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstInstanceVlanMapped4k.setStatus(_A)
_FsMstCistPortTable_Object=MibTable
fsMstCistPortTable=_FsMstCistPortTable_Object((1,3,6,1,4,1,10876,101,1,80,1,40))
if mibBuilder.loadTexts:fsMstCistPortTable.setStatus(_A)
_FsMstCistPortEntry_Object=MibTableRow
fsMstCistPortEntry=_FsMstCistPortEntry_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1))
fsMstCistPortEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:fsMstCistPortEntry.setStatus(_A)
class _FsMstCistPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsMstCistPort_Type.__name__=_C
_FsMstCistPort_Object=MibTableColumn
fsMstCistPort=_FsMstCistPort_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,1),_FsMstCistPort_Type())
fsMstCistPort.setMaxAccess(_K)
if mibBuilder.loadTexts:fsMstCistPort.setStatus(_A)
class _FsMstCistPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_FsMstCistPortPathCost_Type.__name__=_C
_FsMstCistPortPathCost_Object=MibTableColumn
fsMstCistPortPathCost=_FsMstCistPortPathCost_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,2),_FsMstCistPortPathCost_Type())
fsMstCistPortPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstCistPortPathCost.setStatus(_A)
class _FsMstCistPortPriority_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_FsMstCistPortPriority_Type.__name__=_C
_FsMstCistPortPriority_Object=MibTableColumn
fsMstCistPortPriority=_FsMstCistPortPriority_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,3),_FsMstCistPortPriority_Type())
fsMstCistPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstCistPortPriority.setStatus(_A)
_FsMstCistPortDesignatedRoot_Type=BridgeId
_FsMstCistPortDesignatedRoot_Object=MibTableColumn
fsMstCistPortDesignatedRoot=_FsMstCistPortDesignatedRoot_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,4),_FsMstCistPortDesignatedRoot_Type())
fsMstCistPortDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortDesignatedRoot.setStatus(_A)
_FsMstCistPortDesignatedBridge_Type=BridgeId
_FsMstCistPortDesignatedBridge_Object=MibTableColumn
fsMstCistPortDesignatedBridge=_FsMstCistPortDesignatedBridge_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,5),_FsMstCistPortDesignatedBridge_Type())
fsMstCistPortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortDesignatedBridge.setStatus(_A)
class _FsMstCistPortDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_FsMstCistPortDesignatedPort_Type.__name__=_F
_FsMstCistPortDesignatedPort_Object=MibTableColumn
fsMstCistPortDesignatedPort=_FsMstCistPortDesignatedPort_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,6),_FsMstCistPortDesignatedPort_Type())
fsMstCistPortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortDesignatedPort.setStatus(_A)
class _FsMstCistPortAdminP2P_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('forceTrue',0),('forceFalse',1),('auto',2)))
_FsMstCistPortAdminP2P_Type.__name__=_C
_FsMstCistPortAdminP2P_Object=MibTableColumn
fsMstCistPortAdminP2P=_FsMstCistPortAdminP2P_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,7),_FsMstCistPortAdminP2P_Type())
fsMstCistPortAdminP2P.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstCistPortAdminP2P.setStatus(_A)
_FsMstCistPortOperP2P_Type=TruthValue
_FsMstCistPortOperP2P_Object=MibTableColumn
fsMstCistPortOperP2P=_FsMstCistPortOperP2P_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,8),_FsMstCistPortOperP2P_Type())
fsMstCistPortOperP2P.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortOperP2P.setStatus(_A)
_FsMstCistPortAdminEdgeStatus_Type=TruthValue
_FsMstCistPortAdminEdgeStatus_Object=MibTableColumn
fsMstCistPortAdminEdgeStatus=_FsMstCistPortAdminEdgeStatus_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,9),_FsMstCistPortAdminEdgeStatus_Type())
fsMstCistPortAdminEdgeStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstCistPortAdminEdgeStatus.setStatus(_A)
_FsMstCistPortOperEdgeStatus_Type=TruthValue
_FsMstCistPortOperEdgeStatus_Object=MibTableColumn
fsMstCistPortOperEdgeStatus=_FsMstCistPortOperEdgeStatus_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,10),_FsMstCistPortOperEdgeStatus_Type())
fsMstCistPortOperEdgeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortOperEdgeStatus.setStatus(_A)
_FsMstCistPortProtocolMigration_Type=TruthValue
_FsMstCistPortProtocolMigration_Object=MibTableColumn
fsMstCistPortProtocolMigration=_FsMstCistPortProtocolMigration_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,11),_FsMstCistPortProtocolMigration_Type())
fsMstCistPortProtocolMigration.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstCistPortProtocolMigration.setStatus(_A)
class _FsMstCistPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5)));namedValues=NamedValues(*((_G,1),(_N,2),(_L,4),(_O,5)))
_FsMstCistPortState_Type.__name__=_C
_FsMstCistPortState_Object=MibTableColumn
fsMstCistPortState=_FsMstCistPortState_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,12),_FsMstCistPortState_Type())
fsMstCistPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortState.setStatus(_A)
class _FsMstCistForcePortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_U,1)))
_FsMstCistForcePortState_Type.__name__=_C
_FsMstCistForcePortState_Object=MibTableColumn
fsMstCistForcePortState=_FsMstCistForcePortState_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,13),_FsMstCistForcePortState_Type())
fsMstCistForcePortState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstCistForcePortState.setStatus(_A)
_FsMstCistPortForwardTransitions_Type=Counter32
_FsMstCistPortForwardTransitions_Object=MibTableColumn
fsMstCistPortForwardTransitions=_FsMstCistPortForwardTransitions_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,14),_FsMstCistPortForwardTransitions_Type())
fsMstCistPortForwardTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortForwardTransitions.setStatus(_A)
_FsMstCistPortRxMstBpduCount_Type=Counter32
_FsMstCistPortRxMstBpduCount_Object=MibTableColumn
fsMstCistPortRxMstBpduCount=_FsMstCistPortRxMstBpduCount_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,15),_FsMstCistPortRxMstBpduCount_Type())
fsMstCistPortRxMstBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortRxMstBpduCount.setStatus(_A)
_FsMstCistPortRxRstBpduCount_Type=Counter32
_FsMstCistPortRxRstBpduCount_Object=MibTableColumn
fsMstCistPortRxRstBpduCount=_FsMstCistPortRxRstBpduCount_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,16),_FsMstCistPortRxRstBpduCount_Type())
fsMstCistPortRxRstBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortRxRstBpduCount.setStatus(_A)
_FsMstCistPortRxConfigBpduCount_Type=Counter32
_FsMstCistPortRxConfigBpduCount_Object=MibTableColumn
fsMstCistPortRxConfigBpduCount=_FsMstCistPortRxConfigBpduCount_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,17),_FsMstCistPortRxConfigBpduCount_Type())
fsMstCistPortRxConfigBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortRxConfigBpduCount.setStatus(_A)
_FsMstCistPortRxTcnBpduCount_Type=Counter32
_FsMstCistPortRxTcnBpduCount_Object=MibTableColumn
fsMstCistPortRxTcnBpduCount=_FsMstCistPortRxTcnBpduCount_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,18),_FsMstCistPortRxTcnBpduCount_Type())
fsMstCistPortRxTcnBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortRxTcnBpduCount.setStatus(_A)
_FsMstCistPortTxMstBpduCount_Type=Counter32
_FsMstCistPortTxMstBpduCount_Object=MibTableColumn
fsMstCistPortTxMstBpduCount=_FsMstCistPortTxMstBpduCount_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,19),_FsMstCistPortTxMstBpduCount_Type())
fsMstCistPortTxMstBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortTxMstBpduCount.setStatus(_A)
_FsMstCistPortTxRstBpduCount_Type=Counter32
_FsMstCistPortTxRstBpduCount_Object=MibTableColumn
fsMstCistPortTxRstBpduCount=_FsMstCistPortTxRstBpduCount_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,20),_FsMstCistPortTxRstBpduCount_Type())
fsMstCistPortTxRstBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortTxRstBpduCount.setStatus(_A)
_FsMstCistPortTxConfigBpduCount_Type=Counter32
_FsMstCistPortTxConfigBpduCount_Object=MibTableColumn
fsMstCistPortTxConfigBpduCount=_FsMstCistPortTxConfigBpduCount_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,21),_FsMstCistPortTxConfigBpduCount_Type())
fsMstCistPortTxConfigBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortTxConfigBpduCount.setStatus(_A)
_FsMstCistPortTxTcnBpduCount_Type=Counter32
_FsMstCistPortTxTcnBpduCount_Object=MibTableColumn
fsMstCistPortTxTcnBpduCount=_FsMstCistPortTxTcnBpduCount_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,22),_FsMstCistPortTxTcnBpduCount_Type())
fsMstCistPortTxTcnBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortTxTcnBpduCount.setStatus(_A)
_FsMstCistPortInvalidMstBpduRxCount_Type=Counter32
_FsMstCistPortInvalidMstBpduRxCount_Object=MibTableColumn
fsMstCistPortInvalidMstBpduRxCount=_FsMstCistPortInvalidMstBpduRxCount_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,23),_FsMstCistPortInvalidMstBpduRxCount_Type())
fsMstCistPortInvalidMstBpduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortInvalidMstBpduRxCount.setStatus(_A)
_FsMstCistPortInvalidRstBpduRxCount_Type=Counter32
_FsMstCistPortInvalidRstBpduRxCount_Object=MibTableColumn
fsMstCistPortInvalidRstBpduRxCount=_FsMstCistPortInvalidRstBpduRxCount_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,24),_FsMstCistPortInvalidRstBpduRxCount_Type())
fsMstCistPortInvalidRstBpduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortInvalidRstBpduRxCount.setStatus(_A)
_FsMstCistPortInvalidConfigBpduRxCount_Type=Counter32
_FsMstCistPortInvalidConfigBpduRxCount_Object=MibTableColumn
fsMstCistPortInvalidConfigBpduRxCount=_FsMstCistPortInvalidConfigBpduRxCount_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,25),_FsMstCistPortInvalidConfigBpduRxCount_Type())
fsMstCistPortInvalidConfigBpduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortInvalidConfigBpduRxCount.setStatus(_A)
_FsMstCistPortInvalidTcnBpduRxCount_Type=Counter32
_FsMstCistPortInvalidTcnBpduRxCount_Object=MibTableColumn
fsMstCistPortInvalidTcnBpduRxCount=_FsMstCistPortInvalidTcnBpduRxCount_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,26),_FsMstCistPortInvalidTcnBpduRxCount_Type())
fsMstCistPortInvalidTcnBpduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortInvalidTcnBpduRxCount.setStatus(_A)
class _FsMstCistPortTransmitSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('transmitinit',0),('transmitperiodic',1),('transmitconfig',2),('transmittcn',3),('transmitrstp',4),('idle',5)))
_FsMstCistPortTransmitSemState_Type.__name__=_C
_FsMstCistPortTransmitSemState_Object=MibTableColumn
fsMstCistPortTransmitSemState=_FsMstCistPortTransmitSemState_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,27),_FsMstCistPortTransmitSemState_Type())
fsMstCistPortTransmitSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortTransmitSemState.setStatus(_A)
class _FsMstCistPortReceiveSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('discard',0),(_X,1)))
_FsMstCistPortReceiveSemState_Type.__name__=_C
_FsMstCistPortReceiveSemState_Object=MibTableColumn
fsMstCistPortReceiveSemState=_FsMstCistPortReceiveSemState_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,28),_FsMstCistPortReceiveSemState_Type())
fsMstCistPortReceiveSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortReceiveSemState.setStatus(_A)
class _FsMstCistPortProtMigrationSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_Y,0),(_f,1),('sendingrstp',2),(_g,3),('sendingstp',4)))
_FsMstCistPortProtMigrationSemState_Type.__name__=_C
_FsMstCistPortProtMigrationSemState_Object=MibTableColumn
fsMstCistPortProtMigrationSemState=_FsMstCistPortProtMigrationSemState_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,29),_FsMstCistPortProtMigrationSemState_Type())
fsMstCistPortProtMigrationSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortProtMigrationSemState.setStatus(_A)
_FsMstCistProtocolMigrationCount_Type=Counter32
_FsMstCistProtocolMigrationCount_Object=MibTableColumn
fsMstCistProtocolMigrationCount=_FsMstCistProtocolMigrationCount_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,30),_FsMstCistProtocolMigrationCount_Type())
fsMstCistProtocolMigrationCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistProtocolMigrationCount.setStatus(_A)
_FsMstCistPortDesignatedCost_Type=Integer32
_FsMstCistPortDesignatedCost_Object=MibTableColumn
fsMstCistPortDesignatedCost=_FsMstCistPortDesignatedCost_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,31),_FsMstCistPortDesignatedCost_Type())
fsMstCistPortDesignatedCost.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortDesignatedCost.setStatus(_A)
_FsMstCistPortRegionalRoot_Type=BridgeId
_FsMstCistPortRegionalRoot_Object=MibTableColumn
fsMstCistPortRegionalRoot=_FsMstCistPortRegionalRoot_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,32),_FsMstCistPortRegionalRoot_Type())
fsMstCistPortRegionalRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortRegionalRoot.setStatus(_A)
_FsMstCistPortRegionalPathCost_Type=Integer32
_FsMstCistPortRegionalPathCost_Object=MibTableColumn
fsMstCistPortRegionalPathCost=_FsMstCistPortRegionalPathCost_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,33),_FsMstCistPortRegionalPathCost_Type())
fsMstCistPortRegionalPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortRegionalPathCost.setStatus(_A)
class _FsMstCistSelectedPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_G,0),(_P,1),(_Q,2),(_R,3),(_S,4)))
_FsMstCistSelectedPortRole_Type.__name__=_C
_FsMstCistSelectedPortRole_Object=MibTableColumn
fsMstCistSelectedPortRole=_FsMstCistSelectedPortRole_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,34),_FsMstCistSelectedPortRole_Type())
fsMstCistSelectedPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistSelectedPortRole.setStatus(_A)
class _FsMstCistCurrentPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_G,0),(_P,1),(_Q,2),(_R,3),(_S,4)))
_FsMstCistCurrentPortRole_Type.__name__=_C
_FsMstCistCurrentPortRole_Object=MibTableColumn
fsMstCistCurrentPortRole=_FsMstCistCurrentPortRole_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,35),_FsMstCistCurrentPortRole_Type())
fsMstCistCurrentPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistCurrentPortRole.setStatus(_A)
class _FsMstCistPortInfoSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_G,0),('aged',1),(_h,2),(_i,3),(_j,4),(_k,5),(_l,6),(_m,7),(_X,8),('other',9)))
_FsMstCistPortInfoSemState_Type.__name__=_C
_FsMstCistPortInfoSemState_Object=MibTableColumn
fsMstCistPortInfoSemState=_FsMstCistPortInfoSemState_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,36),_FsMstCistPortInfoSemState_Type())
fsMstCistPortInfoSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortInfoSemState.setStatus(_A)
class _FsMstCistPortRoleTransitionSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_Y,0),(_n,1),(_o,2),(_p,3),(_q,4),(_r,5),(_T,6)))
_FsMstCistPortRoleTransitionSemState_Type.__name__=_C
_FsMstCistPortRoleTransitionSemState_Object=MibTableColumn
fsMstCistPortRoleTransitionSemState=_FsMstCistPortRoleTransitionSemState_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,37),_FsMstCistPortRoleTransitionSemState_Type())
fsMstCistPortRoleTransitionSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortRoleTransitionSemState.setStatus(_A)
class _FsMstCistPortStateTransitionSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_L,1),(_O,2)))
_FsMstCistPortStateTransitionSemState_Type.__name__=_C
_FsMstCistPortStateTransitionSemState_Object=MibTableColumn
fsMstCistPortStateTransitionSemState=_FsMstCistPortStateTransitionSemState_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,38),_FsMstCistPortStateTransitionSemState_Type())
fsMstCistPortStateTransitionSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortStateTransitionSemState.setStatus(_A)
class _FsMstCistPortTopologyChangeSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_s,0),(_L,1),(_t,2),(_u,3),(_v,4),(_w,5),(_x,6),(_y,7)))
_FsMstCistPortTopologyChangeSemState_Type.__name__=_C
_FsMstCistPortTopologyChangeSemState_Object=MibTableColumn
fsMstCistPortTopologyChangeSemState=_FsMstCistPortTopologyChangeSemState_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,39),_FsMstCistPortTopologyChangeSemState_Type())
fsMstCistPortTopologyChangeSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortTopologyChangeSemState.setStatus(_A)
class _FsMstCistPortHelloTime_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,100),ValueRangeConstraint(200,200))
_FsMstCistPortHelloTime_Type.__name__=_M
_FsMstCistPortHelloTime_Object=MibTableColumn
fsMstCistPortHelloTime=_FsMstCistPortHelloTime_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,40),_FsMstCistPortHelloTime_Type())
fsMstCistPortHelloTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstCistPortHelloTime.setStatus(_A)
if mibBuilder.loadTexts:fsMstCistPortHelloTime.setUnits(_I)
class _FsMstCistPortOperVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3)));namedValues=NamedValues(*((_b,0),('rstp',2),('mstp',3)))
_FsMstCistPortOperVersion_Type.__name__=_C
_FsMstCistPortOperVersion_Object=MibTableColumn
fsMstCistPortOperVersion=_FsMstCistPortOperVersion_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,41),_FsMstCistPortOperVersion_Type())
fsMstCistPortOperVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortOperVersion.setStatus(_A)
_FsMstCistPortEffectivePortState_Type=TruthValue
_FsMstCistPortEffectivePortState_Object=MibTableColumn
fsMstCistPortEffectivePortState=_FsMstCistPortEffectivePortState_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,42),_FsMstCistPortEffectivePortState_Type())
fsMstCistPortEffectivePortState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortEffectivePortState.setStatus(_A)
_FsMstCistPortAutoEdgeStatus_Type=TruthValue
_FsMstCistPortAutoEdgeStatus_Object=MibTableColumn
fsMstCistPortAutoEdgeStatus=_FsMstCistPortAutoEdgeStatus_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,43),_FsMstCistPortAutoEdgeStatus_Type())
fsMstCistPortAutoEdgeStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstCistPortAutoEdgeStatus.setStatus(_A)
_FsMstCistPortRestrictedRole_Type=TruthValue
_FsMstCistPortRestrictedRole_Object=MibTableColumn
fsMstCistPortRestrictedRole=_FsMstCistPortRestrictedRole_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,44),_FsMstCistPortRestrictedRole_Type())
fsMstCistPortRestrictedRole.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstCistPortRestrictedRole.setStatus(_A)
_FsMstCistPortRestrictedTCN_Type=TruthValue
_FsMstCistPortRestrictedTCN_Object=MibTableColumn
fsMstCistPortRestrictedTCN=_FsMstCistPortRestrictedTCN_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,45),_FsMstCistPortRestrictedTCN_Type())
fsMstCistPortRestrictedTCN.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstCistPortRestrictedTCN.setStatus(_A)
class _FsMstCistPortAdminPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_FsMstCistPortAdminPathCost_Type.__name__=_C
_FsMstCistPortAdminPathCost_Object=MibTableColumn
fsMstCistPortAdminPathCost=_FsMstCistPortAdminPathCost_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,46),_FsMstCistPortAdminPathCost_Type())
fsMstCistPortAdminPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstCistPortAdminPathCost.setStatus(_A)
class _FsMstCistPortEnableBPDURx_Type(TruthValue):defaultValue=1
_FsMstCistPortEnableBPDURx_Type.__name__=_J
_FsMstCistPortEnableBPDURx_Object=MibTableColumn
fsMstCistPortEnableBPDURx=_FsMstCistPortEnableBPDURx_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,47),_FsMstCistPortEnableBPDURx_Type())
fsMstCistPortEnableBPDURx.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstCistPortEnableBPDURx.setStatus(_A)
class _FsMstCistPortEnableBPDUTx_Type(TruthValue):defaultValue=1
_FsMstCistPortEnableBPDUTx_Type.__name__=_J
_FsMstCistPortEnableBPDUTx_Object=MibTableColumn
fsMstCistPortEnableBPDUTx=_FsMstCistPortEnableBPDUTx_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,48),_FsMstCistPortEnableBPDUTx_Type())
fsMstCistPortEnableBPDUTx.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstCistPortEnableBPDUTx.setStatus(_A)
_FsMstCistPortPseudoRootId_Type=BridgeId
_FsMstCistPortPseudoRootId_Object=MibTableColumn
fsMstCistPortPseudoRootId=_FsMstCistPortPseudoRootId_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,49),_FsMstCistPortPseudoRootId_Type())
fsMstCistPortPseudoRootId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstCistPortPseudoRootId.setStatus(_A)
class _FsMstCistPortIsL2Gp_Type(TruthValue):defaultValue=2
_FsMstCistPortIsL2Gp_Type.__name__=_J
_FsMstCistPortIsL2Gp_Object=MibTableColumn
fsMstCistPortIsL2Gp=_FsMstCistPortIsL2Gp_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,50),_FsMstCistPortIsL2Gp_Type())
fsMstCistPortIsL2Gp.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstCistPortIsL2Gp.setStatus(_A)
class _FsMstCistPortLoopGuard_Type(TruthValue):defaultValue=2
_FsMstCistPortLoopGuard_Type.__name__=_J
_FsMstCistPortLoopGuard_Object=MibTableColumn
fsMstCistPortLoopGuard=_FsMstCistPortLoopGuard_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,51),_FsMstCistPortLoopGuard_Type())
fsMstCistPortLoopGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstCistPortLoopGuard.setStatus(_A)
class _FsMstCistPortRcvdEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_z,1),(_A0,2),(_A1,3)))
_FsMstCistPortRcvdEvent_Type.__name__=_C
_FsMstCistPortRcvdEvent_Object=MibTableColumn
fsMstCistPortRcvdEvent=_FsMstCistPortRcvdEvent_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,52),_FsMstCistPortRcvdEvent_Type())
fsMstCistPortRcvdEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortRcvdEvent.setStatus(_A)
_FsMstCistPortRcvdEventSubType_Type=Integer32
_FsMstCistPortRcvdEventSubType_Object=MibTableColumn
fsMstCistPortRcvdEventSubType=_FsMstCistPortRcvdEventSubType_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,53),_FsMstCistPortRcvdEventSubType_Type())
fsMstCistPortRcvdEventSubType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortRcvdEventSubType.setStatus(_A)
_FsMstCistPortRcvdEventTimeStamp_Type=Unsigned32
_FsMstCistPortRcvdEventTimeStamp_Object=MibTableColumn
fsMstCistPortRcvdEventTimeStamp=_FsMstCistPortRcvdEventTimeStamp_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,54),_FsMstCistPortRcvdEventTimeStamp_Type())
fsMstCistPortRcvdEventTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstCistPortRcvdEventTimeStamp.setStatus(_A)
class _FsMstCistPortBpduGuard_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Z,0),('enable',1),('disable',2)))
_FsMstCistPortBpduGuard_Type.__name__=_C
_FsMstCistPortBpduGuard_Object=MibTableColumn
fsMstCistPortBpduGuard=_FsMstCistPortBpduGuard_Object((1,3,6,1,4,1,10876,101,1,80,1,40,1,55),_FsMstCistPortBpduGuard_Type())
fsMstCistPortBpduGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstCistPortBpduGuard.setStatus(_A)
_FsMstMstiPortTable_Object=MibTable
fsMstMstiPortTable=_FsMstMstiPortTable_Object((1,3,6,1,4,1,10876,101,1,80,1,41))
if mibBuilder.loadTexts:fsMstMstiPortTable.setStatus(_A)
_FsMstMstiPortEntry_Object=MibTableRow
fsMstMstiPortEntry=_FsMstMstiPortEntry_Object((1,3,6,1,4,1,10876,101,1,80,1,41,1))
fsMstMstiPortEntry.setIndexNames((0,_E,_A2),(0,_E,_W))
if mibBuilder.loadTexts:fsMstMstiPortEntry.setStatus(_A)
class _FsMstMstiPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsMstMstiPort_Type.__name__=_C
_FsMstMstiPort_Object=MibTableColumn
fsMstMstiPort=_FsMstMstiPort_Object((1,3,6,1,4,1,10876,101,1,80,1,41,1,1),_FsMstMstiPort_Type())
fsMstMstiPort.setMaxAccess(_K)
if mibBuilder.loadTexts:fsMstMstiPort.setStatus(_A)
class _FsMstMstiPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_FsMstMstiPortPathCost_Type.__name__=_C
_FsMstMstiPortPathCost_Object=MibTableColumn
fsMstMstiPortPathCost=_FsMstMstiPortPathCost_Object((1,3,6,1,4,1,10876,101,1,80,1,41,1,2),_FsMstMstiPortPathCost_Type())
fsMstMstiPortPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstMstiPortPathCost.setStatus(_A)
class _FsMstMstiPortPriority_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_FsMstMstiPortPriority_Type.__name__=_C
_FsMstMstiPortPriority_Object=MibTableColumn
fsMstMstiPortPriority=_FsMstMstiPortPriority_Object((1,3,6,1,4,1,10876,101,1,80,1,41,1,3),_FsMstMstiPortPriority_Type())
fsMstMstiPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstMstiPortPriority.setStatus(_A)
_FsMstMstiPortDesignatedRoot_Type=BridgeId
_FsMstMstiPortDesignatedRoot_Object=MibTableColumn
fsMstMstiPortDesignatedRoot=_FsMstMstiPortDesignatedRoot_Object((1,3,6,1,4,1,10876,101,1,80,1,41,1,4),_FsMstMstiPortDesignatedRoot_Type())
fsMstMstiPortDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstiPortDesignatedRoot.setStatus(_A)
_FsMstMstiPortDesignatedBridge_Type=BridgeId
_FsMstMstiPortDesignatedBridge_Object=MibTableColumn
fsMstMstiPortDesignatedBridge=_FsMstMstiPortDesignatedBridge_Object((1,3,6,1,4,1,10876,101,1,80,1,41,1,5),_FsMstMstiPortDesignatedBridge_Type())
fsMstMstiPortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstiPortDesignatedBridge.setStatus(_A)
class _FsMstMstiPortDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_FsMstMstiPortDesignatedPort_Type.__name__=_F
_FsMstMstiPortDesignatedPort_Object=MibTableColumn
fsMstMstiPortDesignatedPort=_FsMstMstiPortDesignatedPort_Object((1,3,6,1,4,1,10876,101,1,80,1,41,1,6),_FsMstMstiPortDesignatedPort_Type())
fsMstMstiPortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstiPortDesignatedPort.setStatus(_A)
class _FsMstMstiPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5)));namedValues=NamedValues(*((_G,1),(_N,2),(_L,4),(_O,5)))
_FsMstMstiPortState_Type.__name__=_C
_FsMstMstiPortState_Object=MibTableColumn
fsMstMstiPortState=_FsMstMstiPortState_Object((1,3,6,1,4,1,10876,101,1,80,1,41,1,7),_FsMstMstiPortState_Type())
fsMstMstiPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstiPortState.setStatus(_A)
class _FsMstMstiForcePortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_U,1)))
_FsMstMstiForcePortState_Type.__name__=_C
_FsMstMstiForcePortState_Object=MibTableColumn
fsMstMstiForcePortState=_FsMstMstiForcePortState_Object((1,3,6,1,4,1,10876,101,1,80,1,41,1,8),_FsMstMstiForcePortState_Type())
fsMstMstiForcePortState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstMstiForcePortState.setStatus(_A)
_FsMstMstiPortForwardTransitions_Type=Counter32
_FsMstMstiPortForwardTransitions_Object=MibTableColumn
fsMstMstiPortForwardTransitions=_FsMstMstiPortForwardTransitions_Object((1,3,6,1,4,1,10876,101,1,80,1,41,1,9),_FsMstMstiPortForwardTransitions_Type())
fsMstMstiPortForwardTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstiPortForwardTransitions.setStatus(_A)
_FsMstMstiPortReceivedBPDUs_Type=Counter32
_FsMstMstiPortReceivedBPDUs_Object=MibTableColumn
fsMstMstiPortReceivedBPDUs=_FsMstMstiPortReceivedBPDUs_Object((1,3,6,1,4,1,10876,101,1,80,1,41,1,10),_FsMstMstiPortReceivedBPDUs_Type())
fsMstMstiPortReceivedBPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstiPortReceivedBPDUs.setStatus(_A)
_FsMstMstiPortTransmittedBPDUs_Type=Counter32
_FsMstMstiPortTransmittedBPDUs_Object=MibTableColumn
fsMstMstiPortTransmittedBPDUs=_FsMstMstiPortTransmittedBPDUs_Object((1,3,6,1,4,1,10876,101,1,80,1,41,1,11),_FsMstMstiPortTransmittedBPDUs_Type())
fsMstMstiPortTransmittedBPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstiPortTransmittedBPDUs.setStatus(_A)
_FsMstMstiPortInvalidBPDUsRcvd_Type=Counter32
_FsMstMstiPortInvalidBPDUsRcvd_Object=MibTableColumn
fsMstMstiPortInvalidBPDUsRcvd=_FsMstMstiPortInvalidBPDUsRcvd_Object((1,3,6,1,4,1,10876,101,1,80,1,41,1,12),_FsMstMstiPortInvalidBPDUsRcvd_Type())
fsMstMstiPortInvalidBPDUsRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstiPortInvalidBPDUsRcvd.setStatus(_A)
_FsMstMstiPortDesignatedCost_Type=Integer32
_FsMstMstiPortDesignatedCost_Object=MibTableColumn
fsMstMstiPortDesignatedCost=_FsMstMstiPortDesignatedCost_Object((1,3,6,1,4,1,10876,101,1,80,1,41,1,13),_FsMstMstiPortDesignatedCost_Type())
fsMstMstiPortDesignatedCost.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstiPortDesignatedCost.setStatus(_A)
class _FsMstMstiSelectedPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_G,0),(_P,1),(_Q,2),(_R,3),(_S,4),('master',5)))
_FsMstMstiSelectedPortRole_Type.__name__=_C
_FsMstMstiSelectedPortRole_Object=MibTableColumn
fsMstMstiSelectedPortRole=_FsMstMstiSelectedPortRole_Object((1,3,6,1,4,1,10876,101,1,80,1,41,1,14),_FsMstMstiSelectedPortRole_Type())
fsMstMstiSelectedPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstiSelectedPortRole.setStatus(_A)
class _FsMstMstiCurrentPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_G,0),(_P,1),(_Q,2),(_R,3),(_S,4),('master',5)))
_FsMstMstiCurrentPortRole_Type.__name__=_C
_FsMstMstiCurrentPortRole_Object=MibTableColumn
fsMstMstiCurrentPortRole=_FsMstMstiCurrentPortRole_Object((1,3,6,1,4,1,10876,101,1,80,1,41,1,15),_FsMstMstiCurrentPortRole_Type())
fsMstMstiCurrentPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstiCurrentPortRole.setStatus(_A)
class _FsMstMstiPortInfoSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_G,0),('aged',1),(_h,2),(_i,3),(_j,4),(_k,5),(_l,6),(_m,7),(_X,8),('other',9)))
_FsMstMstiPortInfoSemState_Type.__name__=_C
_FsMstMstiPortInfoSemState_Object=MibTableColumn
fsMstMstiPortInfoSemState=_FsMstMstiPortInfoSemState_Object((1,3,6,1,4,1,10876,101,1,80,1,41,1,16),_FsMstMstiPortInfoSemState_Type())
fsMstMstiPortInfoSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstiPortInfoSemState.setStatus(_A)
class _FsMstMstiPortRoleTransitionSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_Y,0),(_n,1),(_o,2),(_p,3),(_q,4),(_r,5),(_T,6)))
_FsMstMstiPortRoleTransitionSemState_Type.__name__=_C
_FsMstMstiPortRoleTransitionSemState_Object=MibTableColumn
fsMstMstiPortRoleTransitionSemState=_FsMstMstiPortRoleTransitionSemState_Object((1,3,6,1,4,1,10876,101,1,80,1,41,1,17),_FsMstMstiPortRoleTransitionSemState_Type())
fsMstMstiPortRoleTransitionSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstiPortRoleTransitionSemState.setStatus(_A)
class _FsMstMstiPortStateTransitionSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),(_L,1),(_O,2)))
_FsMstMstiPortStateTransitionSemState_Type.__name__=_C
_FsMstMstiPortStateTransitionSemState_Object=MibTableColumn
fsMstMstiPortStateTransitionSemState=_FsMstMstiPortStateTransitionSemState_Object((1,3,6,1,4,1,10876,101,1,80,1,41,1,18),_FsMstMstiPortStateTransitionSemState_Type())
fsMstMstiPortStateTransitionSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstiPortStateTransitionSemState.setStatus(_A)
class _FsMstMstiPortTopologyChangeSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_s,0),(_L,1),(_t,2),(_u,3),(_v,4),(_w,5),(_x,6),(_y,7)))
_FsMstMstiPortTopologyChangeSemState_Type.__name__=_C
_FsMstMstiPortTopologyChangeSemState_Object=MibTableColumn
fsMstMstiPortTopologyChangeSemState=_FsMstMstiPortTopologyChangeSemState_Object((1,3,6,1,4,1,10876,101,1,80,1,41,1,19),_FsMstMstiPortTopologyChangeSemState_Type())
fsMstMstiPortTopologyChangeSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstiPortTopologyChangeSemState.setStatus(_A)
_FsMstMstiPortEffectivePortState_Type=TruthValue
_FsMstMstiPortEffectivePortState_Object=MibTableColumn
fsMstMstiPortEffectivePortState=_FsMstMstiPortEffectivePortState_Object((1,3,6,1,4,1,10876,101,1,80,1,41,1,20),_FsMstMstiPortEffectivePortState_Type())
fsMstMstiPortEffectivePortState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstiPortEffectivePortState.setStatus(_A)
class _FsMstMstiPortAdminPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_FsMstMstiPortAdminPathCost_Type.__name__=_C
_FsMstMstiPortAdminPathCost_Object=MibTableColumn
fsMstMstiPortAdminPathCost=_FsMstMstiPortAdminPathCost_Object((1,3,6,1,4,1,10876,101,1,80,1,41,1,21),_FsMstMstiPortAdminPathCost_Type())
fsMstMstiPortAdminPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstMstiPortAdminPathCost.setStatus(_A)
_FsMstMstiPortPseudoRootId_Type=BridgeId
_FsMstMstiPortPseudoRootId_Object=MibTableColumn
fsMstMstiPortPseudoRootId=_FsMstMstiPortPseudoRootId_Object((1,3,6,1,4,1,10876,101,1,80,1,41,1,22),_FsMstMstiPortPseudoRootId_Type())
fsMstMstiPortPseudoRootId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstMstiPortPseudoRootId.setStatus(_A)
_FsMstMstiPortStateChangeTimeStamp_Type=Unsigned32
_FsMstMstiPortStateChangeTimeStamp_Object=MibTableColumn
fsMstMstiPortStateChangeTimeStamp=_FsMstMstiPortStateChangeTimeStamp_Object((1,3,6,1,4,1,10876,101,1,80,1,41,1,23),_FsMstMstiPortStateChangeTimeStamp_Type())
fsMstMstiPortStateChangeTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstMstiPortStateChangeTimeStamp.setStatus(_A)
class _FsMstCistDynamicPathcostCalculation_Type(TruthValue):defaultValue=2
_FsMstCistDynamicPathcostCalculation_Type.__name__=_J
_FsMstCistDynamicPathcostCalculation_Object=MibScalar
fsMstCistDynamicPathcostCalculation=_FsMstCistDynamicPathcostCalculation_Object((1,3,6,1,4,1,10876,101,1,80,1,42),_FsMstCistDynamicPathcostCalculation_Type())
fsMstCistDynamicPathcostCalculation.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstCistDynamicPathcostCalculation.setStatus(_A)
class _FsMstCalcPortPathCostOnSpeedChg_Type(TruthValue):defaultValue=2
_FsMstCalcPortPathCostOnSpeedChg_Type.__name__=_J
_FsMstCalcPortPathCostOnSpeedChg_Object=MibScalar
fsMstCalcPortPathCostOnSpeedChg=_FsMstCalcPortPathCostOnSpeedChg_Object((1,3,6,1,4,1,10876,101,1,80,1,43),_FsMstCalcPortPathCostOnSpeedChg_Type())
fsMstCalcPortPathCostOnSpeedChg.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstCalcPortPathCostOnSpeedChg.setStatus(_A)
class _FsMstRcvdEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_z,1),(_A0,2),(_A1,3)))
_FsMstRcvdEvent_Type.__name__=_C
_FsMstRcvdEvent_Object=MibScalar
fsMstRcvdEvent=_FsMstRcvdEvent_Object((1,3,6,1,4,1,10876,101,1,80,1,44),_FsMstRcvdEvent_Type())
fsMstRcvdEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstRcvdEvent.setStatus(_A)
_FsMstRcvdEventSubType_Type=Integer32
_FsMstRcvdEventSubType_Object=MibScalar
fsMstRcvdEventSubType=_FsMstRcvdEventSubType_Object((1,3,6,1,4,1,10876,101,1,80,1,45),_FsMstRcvdEventSubType_Type())
fsMstRcvdEventSubType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstRcvdEventSubType.setStatus(_A)
_FsMstRcvdEventTimeStamp_Type=Unsigned32
_FsMstRcvdEventTimeStamp_Object=MibScalar
fsMstRcvdEventTimeStamp=_FsMstRcvdEventTimeStamp_Object((1,3,6,1,4,1,10876,101,1,80,1,46),_FsMstRcvdEventTimeStamp_Type())
fsMstRcvdEventTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstRcvdEventTimeStamp.setStatus(_A)
_FsMstPortStateChangeTimeStamp_Type=Unsigned32
_FsMstPortStateChangeTimeStamp_Object=MibScalar
fsMstPortStateChangeTimeStamp=_FsMstPortStateChangeTimeStamp_Object((1,3,6,1,4,1,10876,101,1,80,1,47),_FsMstPortStateChangeTimeStamp_Type())
fsMstPortStateChangeTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstPortStateChangeTimeStamp.setStatus(_A)
_FsMstPortExtTable_Object=MibTable
fsMstPortExtTable=_FsMstPortExtTable_Object((1,3,6,1,4,1,10876,101,1,80,1,48))
if mibBuilder.loadTexts:fsMstPortExtTable.setStatus(_A)
_FsMstPortExtEntry_Object=MibTableRow
fsMstPortExtEntry=_FsMstPortExtEntry_Object((1,3,6,1,4,1,10876,101,1,80,1,48,1))
fsMstPortExtEntry.setIndexNames((0,_E,_A3))
if mibBuilder.loadTexts:fsMstPortExtEntry.setStatus(_A)
class _FsMstPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_FsMstPort_Type.__name__=_C
_FsMstPort_Object=MibTableColumn
fsMstPort=_FsMstPort_Object((1,3,6,1,4,1,10876,101,1,80,1,48,1,1),_FsMstPort_Type())
fsMstPort.setMaxAccess(_K)
if mibBuilder.loadTexts:fsMstPort.setStatus(_A)
_FsMstPortRowStatus_Type=RowStatus
_FsMstPortRowStatus_Object=MibTableColumn
fsMstPortRowStatus=_FsMstPortRowStatus_Object((1,3,6,1,4,1,10876,101,1,80,1,48,1,2),_FsMstPortRowStatus_Type())
fsMstPortRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:fsMstPortRowStatus.setStatus(_A)
class _FsMstBpduGuard_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_FsMstBpduGuard_Type.__name__=_C
_FsMstBpduGuard_Object=MibScalar
fsMstBpduGuard=_FsMstBpduGuard_Object((1,3,6,1,4,1,10876,101,1,80,1,49),_FsMstBpduGuard_Type())
fsMstBpduGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstBpduGuard.setStatus(_A)
_Dot1sFsMstTrapsControl_ObjectIdentity=ObjectIdentity
dot1sFsMstTrapsControl=_Dot1sFsMstTrapsControl_ObjectIdentity((1,3,6,1,4,1,10876,101,1,80,2))
class _FsMstSetTraps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMstSetTraps_Type.__name__=_C
_FsMstSetTraps_Object=MibScalar
fsMstSetTraps=_FsMstSetTraps_Object((1,3,6,1,4,1,10876,101,1,80,2,1),_FsMstSetTraps_Type())
fsMstSetTraps.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMstSetTraps.setStatus(_A)
class _FsMstGenTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Z,0),('up',1),('down',2)))
_FsMstGenTrapType_Type.__name__=_C
_FsMstGenTrapType_Object=MibScalar
fsMstGenTrapType=_FsMstGenTrapType_Object((1,3,6,1,4,1,10876,101,1,80,2,2),_FsMstGenTrapType_Type())
fsMstGenTrapType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstGenTrapType.setStatus(_A)
class _FsMstErrTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Z,0),('memfail',1),('bufffail',2)))
_FsMstErrTrapType_Type.__name__=_C
_FsMstErrTrapType_Object=MibScalar
fsMstErrTrapType=_FsMstErrTrapType_Object((1,3,6,1,4,1,10876,101,1,80,2,3),_FsMstErrTrapType_Type())
fsMstErrTrapType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstErrTrapType.setStatus(_A)
_FsMstPortTrapNotificationTable_Object=MibTable
fsMstPortTrapNotificationTable=_FsMstPortTrapNotificationTable_Object((1,3,6,1,4,1,10876,101,1,80,2,4))
if mibBuilder.loadTexts:fsMstPortTrapNotificationTable.setStatus(_A)
_FsMstPortTrapNotificationEntry_Object=MibTableRow
fsMstPortTrapNotificationEntry=_FsMstPortTrapNotificationEntry_Object((1,3,6,1,4,1,10876,101,1,80,2,4,1))
fsMstPortTrapNotificationEntry.setIndexNames((0,_E,_a))
if mibBuilder.loadTexts:fsMstPortTrapNotificationEntry.setStatus(_A)
class _FsMstPortTrapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_FsMstPortTrapIndex_Type.__name__=_C
_FsMstPortTrapIndex_Object=MibTableColumn
fsMstPortTrapIndex=_FsMstPortTrapIndex_Object((1,3,6,1,4,1,10876,101,1,80,2,4,1,1),_FsMstPortTrapIndex_Type())
fsMstPortTrapIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:fsMstPortTrapIndex.setStatus(_A)
class _FsMstPortMigrationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_g,0),(_f,1)))
_FsMstPortMigrationType_Type.__name__=_C
_FsMstPortMigrationType_Object=MibTableColumn
fsMstPortMigrationType=_FsMstPortMigrationType_Object((1,3,6,1,4,1,10876,101,1,80,2,4,1,2),_FsMstPortMigrationType_Type())
fsMstPortMigrationType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstPortMigrationType.setStatus(_A)
class _FsMstPktErrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('protocolIdErr',0),('invalidBpdu',1),('configLengthErr',2),('tcnLengthErr',3),('rstpLengthErr',4),('maxAgeErr',5),('fwdDelayErr',6),('helloTimeErr',7),('mstpLengthErr',8)))
_FsMstPktErrType_Type.__name__=_C
_FsMstPktErrType_Object=MibTableColumn
fsMstPktErrType=_FsMstPktErrType_Object((1,3,6,1,4,1,10876,101,1,80,2,4,1,3),_FsMstPktErrType_Type())
fsMstPktErrType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstPktErrType.setStatus(_A)
_FsMstPktErrVal_Type=Integer32
_FsMstPktErrVal_Object=MibTableColumn
fsMstPktErrVal=_FsMstPktErrVal_Object((1,3,6,1,4,1,10876,101,1,80,2,4,1,4),_FsMstPktErrVal_Type())
fsMstPktErrVal.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstPktErrVal.setStatus(_A)
_FsMstPortRoleTrapNotificationTable_Object=MibTable
fsMstPortRoleTrapNotificationTable=_FsMstPortRoleTrapNotificationTable_Object((1,3,6,1,4,1,10876,101,1,80,2,5))
if mibBuilder.loadTexts:fsMstPortRoleTrapNotificationTable.setStatus(_A)
_FsMstPortRoleTrapNotificationEntry_Object=MibTableRow
fsMstPortRoleTrapNotificationEntry=_FsMstPortRoleTrapNotificationEntry_Object((1,3,6,1,4,1,10876,101,1,80,2,5,1))
fsMstPortRoleTrapNotificationEntry.setIndexNames((0,_E,_a),(0,_E,_V))
if mibBuilder.loadTexts:fsMstPortRoleTrapNotificationEntry.setStatus(_A)
class _FsMstPortRoleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_A4,0),(_A5,1),(_A6,2),('rootPort',3),(_A7,4),(_T,5)))
_FsMstPortRoleType_Type.__name__=_C
_FsMstPortRoleType_Object=MibTableColumn
fsMstPortRoleType=_FsMstPortRoleType_Object((1,3,6,1,4,1,10876,101,1,80,2,5,1,1),_FsMstPortRoleType_Type())
fsMstPortRoleType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstPortRoleType.setStatus(_A)
class _FsMstOldRoleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_A4,0),(_A5,1),(_A6,2),('rootPort',3),(_A7,4),(_T,5)))
_FsMstOldRoleType_Type.__name__=_C
_FsMstOldRoleType_Object=MibTableColumn
fsMstOldRoleType=_FsMstOldRoleType_Object((1,3,6,1,4,1,10876,101,1,80,2,5,1,2),_FsMstOldRoleType_Type())
fsMstOldRoleType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMstOldRoleType.setStatus(_A)
_Dot1sFutureMstTraps_ObjectIdentity=ObjectIdentity
dot1sFutureMstTraps=_Dot1sFutureMstTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,80,3))
_FsMstTraps_ObjectIdentity=ObjectIdentity
fsMstTraps=_FsMstTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,80,3,0))
fsMstGenTrap=NotificationType((1,3,6,1,4,1,10876,101,1,80,3,0,1))
fsMstGenTrap.setObjects(*((_E,_H),(_E,_A8),(_E,_A9),(_E,_AA)))
if mibBuilder.loadTexts:fsMstGenTrap.setStatus(_A)
fsMstErrTrap=NotificationType((1,3,6,1,4,1,10876,101,1,80,3,0,2))
fsMstErrTrap.setObjects(*((_E,_H),(_E,_AB)))
if mibBuilder.loadTexts:fsMstErrTrap.setStatus(_A)
fsMstNewRootTrap=NotificationType((1,3,6,1,4,1,10876,101,1,80,3,0,3))
fsMstNewRootTrap.setObjects(*((_E,_H),(_E,_AC),(_E,_AD)))
if mibBuilder.loadTexts:fsMstNewRootTrap.setStatus(_A)
fsMstTopologyChgTrap=NotificationType((1,3,6,1,4,1,10876,101,1,80,3,0,4))
fsMstTopologyChgTrap.setObjects(*((_E,_H),(_E,_AE)))
if mibBuilder.loadTexts:fsMstTopologyChgTrap.setStatus(_A)
fsMstProtocolMigrationTrap=NotificationType((1,3,6,1,4,1,10876,101,1,80,3,0,5))
fsMstProtocolMigrationTrap.setObjects(*((_E,_H),(_E,_AF),(_E,_AG)))
if mibBuilder.loadTexts:fsMstProtocolMigrationTrap.setStatus(_A)
fsMstInvalidBpduRxdTrap=NotificationType((1,3,6,1,4,1,10876,101,1,80,3,0,6))
fsMstInvalidBpduRxdTrap.setObjects(*((_E,_H),(_E,_AH),(_E,_AI)))
if mibBuilder.loadTexts:fsMstInvalidBpduRxdTrap.setStatus(_A)
fsMstRegionConfigChangeTrap=NotificationType((1,3,6,1,4,1,10876,101,1,80,3,0,7))
fsMstRegionConfigChangeTrap.setObjects(*((_E,_H),(_E,_AJ),(_E,_AK),(_E,_AL),(_E,_AM)))
if mibBuilder.loadTexts:fsMstRegionConfigChangeTrap.setStatus(_A)
fsMstNewPortRoleTrap=NotificationType((1,3,6,1,4,1,10876,101,1,80,3,0,8))
fsMstNewPortRoleTrap.setObjects(*((_E,_H),(_E,_AN),(_E,_AO)))
if mibBuilder.loadTexts:fsMstNewPortRoleTrap.setStatus(_A)
fsMstCistHwFailureTrap=NotificationType((1,3,6,1,4,1,10876,101,1,80,3,0,9))
fsMstCistHwFailureTrap.setObjects(*((_E,_H),(_E,_AP)))
if mibBuilder.loadTexts:fsMstCistHwFailureTrap.setStatus(_A)
fsMstMstiHwFailureTrap=NotificationType((1,3,6,1,4,1,10876,101,1,80,3,0,10))
fsMstMstiHwFailureTrap.setObjects(*((_E,_H),(_E,_AQ)))
if mibBuilder.loadTexts:fsMstMstiHwFailureTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'VlanId':VlanId,'BridgeId':BridgeId,_M:Timeout,'EnabledStatus':EnabledStatus,'futureMstMIB':futureMstMIB,'dot1sFutureMst':dot1sFutureMst,'fsMstSystemControl':fsMstSystemControl,'fsMstModuleStatus':fsMstModuleStatus,'fsMstMaxMstInstanceNumber':fsMstMaxMstInstanceNumber,'fsMstNoOfMstiSupported':fsMstNoOfMstiSupported,'fsMstMaxHopCount':fsMstMaxHopCount,_H:fsMstBrgAddress,'fsMstCistRoot':fsMstCistRoot,'fsMstCistRegionalRoot':fsMstCistRegionalRoot,'fsMstCistRootCost':fsMstCistRootCost,'fsMstCistRegionalRootCost':fsMstCistRegionalRootCost,'fsMstCistRootPort':fsMstCistRootPort,'fsMstCistBridgePriority':fsMstCistBridgePriority,'fsMstCistBridgeMaxAge':fsMstCistBridgeMaxAge,'fsMstCistBridgeForwardDelay':fsMstCistBridgeForwardDelay,'fsMstCistHoldTime':fsMstCistHoldTime,'fsMstCistMaxAge':fsMstCistMaxAge,'fsMstCistForwardDelay':fsMstCistForwardDelay,'fsMstMstpUpCount':fsMstMstpUpCount,'fsMstMstpDownCount':fsMstMstpDownCount,'fsMstPathCostDefaultType':fsMstPathCostDefaultType,'fsMstTrace':fsMstTrace,'fsMstDebug':fsMstDebug,_AF:fsMstForceProtocolVersion,'fsMstTxHoldCount':fsMstTxHoldCount,_AJ:fsMstMstiConfigIdSel,_AK:fsMstMstiRegionName,_AL:fsMstMstiRegionVersion,_AM:fsMstMstiConfigDigest,'fsMstBufferOverFlowCount':fsMstBufferOverFlowCount,'fsMstMemAllocFailureCount':fsMstMemAllocFailureCount,'fsMstRegionConfigChangeCount':fsMstRegionConfigChangeCount,'fsMstCistBridgeRoleSelectionSemState':fsMstCistBridgeRoleSelectionSemState,'fsMstCistTimeSinceTopologyChange':fsMstCistTimeSinceTopologyChange,'fsMstCistTopChanges':fsMstCistTopChanges,'fsMstCistNewRootBridgeCount':fsMstCistNewRootBridgeCount,'fsMstCistHelloTime':fsMstCistHelloTime,'fsMstCistBridgeHelloTime':fsMstCistBridgeHelloTime,'fsMstMstiBridgeTable':fsMstMstiBridgeTable,'fsMstMstiBridgeEntry':fsMstMstiBridgeEntry,_V:fsMstMstiInstanceIndex,_AD:fsMstMstiBridgeRegionalRoot,'fsMstMstiBridgePriority':fsMstMstiBridgePriority,'fsMstMstiRootCost':fsMstMstiRootCost,'fsMstMstiRootPort':fsMstMstiRootPort,'fsMstMstiTimeSinceTopologyChange':fsMstMstiTimeSinceTopologyChange,_AE:fsMstMstiTopChanges,'fsMstMstiNewRootBridgeCount':fsMstMstiNewRootBridgeCount,'fsMstMstiBridgeRoleSelectionSemState':fsMstMstiBridgeRoleSelectionSemState,_A9:fsMstInstanceUpCount,_AA:fsMstInstanceDownCount,_AC:fsMstOldDesignatedRoot,'fsMstVlanInstanceMappingTable':fsMstVlanInstanceMappingTable,'fsMstVlanInstanceMappingEntry':fsMstVlanInstanceMappingEntry,_W:fsMstInstanceIndex,'fsMstMapVlanIndex':fsMstMapVlanIndex,'fsMstUnMapVlanIndex':fsMstUnMapVlanIndex,'fsMstSetVlanList':fsMstSetVlanList,'fsMstResetVlanList':fsMstResetVlanList,'fsMstInstanceVlanMapped':fsMstInstanceVlanMapped,'fsMstInstanceVlanMapped2k':fsMstInstanceVlanMapped2k,'fsMstInstanceVlanMapped3k':fsMstInstanceVlanMapped3k,'fsMstInstanceVlanMapped4k':fsMstInstanceVlanMapped4k,'fsMstCistPortTable':fsMstCistPortTable,'fsMstCistPortEntry':fsMstCistPortEntry,_e:fsMstCistPort,'fsMstCistPortPathCost':fsMstCistPortPathCost,'fsMstCistPortPriority':fsMstCistPortPriority,'fsMstCistPortDesignatedRoot':fsMstCistPortDesignatedRoot,'fsMstCistPortDesignatedBridge':fsMstCistPortDesignatedBridge,'fsMstCistPortDesignatedPort':fsMstCistPortDesignatedPort,'fsMstCistPortAdminP2P':fsMstCistPortAdminP2P,'fsMstCistPortOperP2P':fsMstCistPortOperP2P,'fsMstCistPortAdminEdgeStatus':fsMstCistPortAdminEdgeStatus,'fsMstCistPortOperEdgeStatus':fsMstCistPortOperEdgeStatus,'fsMstCistPortProtocolMigration':fsMstCistPortProtocolMigration,_AP:fsMstCistPortState,'fsMstCistForcePortState':fsMstCistForcePortState,'fsMstCistPortForwardTransitions':fsMstCistPortForwardTransitions,'fsMstCistPortRxMstBpduCount':fsMstCistPortRxMstBpduCount,'fsMstCistPortRxRstBpduCount':fsMstCistPortRxRstBpduCount,'fsMstCistPortRxConfigBpduCount':fsMstCistPortRxConfigBpduCount,'fsMstCistPortRxTcnBpduCount':fsMstCistPortRxTcnBpduCount,'fsMstCistPortTxMstBpduCount':fsMstCistPortTxMstBpduCount,'fsMstCistPortTxRstBpduCount':fsMstCistPortTxRstBpduCount,'fsMstCistPortTxConfigBpduCount':fsMstCistPortTxConfigBpduCount,'fsMstCistPortTxTcnBpduCount':fsMstCistPortTxTcnBpduCount,'fsMstCistPortInvalidMstBpduRxCount':fsMstCistPortInvalidMstBpduRxCount,'fsMstCistPortInvalidRstBpduRxCount':fsMstCistPortInvalidRstBpduRxCount,'fsMstCistPortInvalidConfigBpduRxCount':fsMstCistPortInvalidConfigBpduRxCount,'fsMstCistPortInvalidTcnBpduRxCount':fsMstCistPortInvalidTcnBpduRxCount,'fsMstCistPortTransmitSemState':fsMstCistPortTransmitSemState,'fsMstCistPortReceiveSemState':fsMstCistPortReceiveSemState,'fsMstCistPortProtMigrationSemState':fsMstCistPortProtMigrationSemState,'fsMstCistProtocolMigrationCount':fsMstCistProtocolMigrationCount,'fsMstCistPortDesignatedCost':fsMstCistPortDesignatedCost,'fsMstCistPortRegionalRoot':fsMstCistPortRegionalRoot,'fsMstCistPortRegionalPathCost':fsMstCistPortRegionalPathCost,'fsMstCistSelectedPortRole':fsMstCistSelectedPortRole,'fsMstCistCurrentPortRole':fsMstCistCurrentPortRole,'fsMstCistPortInfoSemState':fsMstCistPortInfoSemState,'fsMstCistPortRoleTransitionSemState':fsMstCistPortRoleTransitionSemState,'fsMstCistPortStateTransitionSemState':fsMstCistPortStateTransitionSemState,'fsMstCistPortTopologyChangeSemState':fsMstCistPortTopologyChangeSemState,'fsMstCistPortHelloTime':fsMstCistPortHelloTime,'fsMstCistPortOperVersion':fsMstCistPortOperVersion,'fsMstCistPortEffectivePortState':fsMstCistPortEffectivePortState,'fsMstCistPortAutoEdgeStatus':fsMstCistPortAutoEdgeStatus,'fsMstCistPortRestrictedRole':fsMstCistPortRestrictedRole,'fsMstCistPortRestrictedTCN':fsMstCistPortRestrictedTCN,'fsMstCistPortAdminPathCost':fsMstCistPortAdminPathCost,'fsMstCistPortEnableBPDURx':fsMstCistPortEnableBPDURx,'fsMstCistPortEnableBPDUTx':fsMstCistPortEnableBPDUTx,'fsMstCistPortPseudoRootId':fsMstCistPortPseudoRootId,'fsMstCistPortIsL2Gp':fsMstCistPortIsL2Gp,'fsMstCistPortLoopGuard':fsMstCistPortLoopGuard,'fsMstCistPortRcvdEvent':fsMstCistPortRcvdEvent,'fsMstCistPortRcvdEventSubType':fsMstCistPortRcvdEventSubType,'fsMstCistPortRcvdEventTimeStamp':fsMstCistPortRcvdEventTimeStamp,'fsMstCistPortBpduGuard':fsMstCistPortBpduGuard,'fsMstMstiPortTable':fsMstMstiPortTable,'fsMstMstiPortEntry':fsMstMstiPortEntry,_A2:fsMstMstiPort,'fsMstMstiPortPathCost':fsMstMstiPortPathCost,'fsMstMstiPortPriority':fsMstMstiPortPriority,'fsMstMstiPortDesignatedRoot':fsMstMstiPortDesignatedRoot,'fsMstMstiPortDesignatedBridge':fsMstMstiPortDesignatedBridge,'fsMstMstiPortDesignatedPort':fsMstMstiPortDesignatedPort,_AQ:fsMstMstiPortState,'fsMstMstiForcePortState':fsMstMstiForcePortState,'fsMstMstiPortForwardTransitions':fsMstMstiPortForwardTransitions,'fsMstMstiPortReceivedBPDUs':fsMstMstiPortReceivedBPDUs,'fsMstMstiPortTransmittedBPDUs':fsMstMstiPortTransmittedBPDUs,'fsMstMstiPortInvalidBPDUsRcvd':fsMstMstiPortInvalidBPDUsRcvd,'fsMstMstiPortDesignatedCost':fsMstMstiPortDesignatedCost,'fsMstMstiSelectedPortRole':fsMstMstiSelectedPortRole,'fsMstMstiCurrentPortRole':fsMstMstiCurrentPortRole,'fsMstMstiPortInfoSemState':fsMstMstiPortInfoSemState,'fsMstMstiPortRoleTransitionSemState':fsMstMstiPortRoleTransitionSemState,'fsMstMstiPortStateTransitionSemState':fsMstMstiPortStateTransitionSemState,'fsMstMstiPortTopologyChangeSemState':fsMstMstiPortTopologyChangeSemState,'fsMstMstiPortEffectivePortState':fsMstMstiPortEffectivePortState,'fsMstMstiPortAdminPathCost':fsMstMstiPortAdminPathCost,'fsMstMstiPortPseudoRootId':fsMstMstiPortPseudoRootId,'fsMstMstiPortStateChangeTimeStamp':fsMstMstiPortStateChangeTimeStamp,'fsMstCistDynamicPathcostCalculation':fsMstCistDynamicPathcostCalculation,'fsMstCalcPortPathCostOnSpeedChg':fsMstCalcPortPathCostOnSpeedChg,'fsMstRcvdEvent':fsMstRcvdEvent,'fsMstRcvdEventSubType':fsMstRcvdEventSubType,'fsMstRcvdEventTimeStamp':fsMstRcvdEventTimeStamp,'fsMstPortStateChangeTimeStamp':fsMstPortStateChangeTimeStamp,'fsMstPortExtTable':fsMstPortExtTable,'fsMstPortExtEntry':fsMstPortExtEntry,_A3:fsMstPort,'fsMstPortRowStatus':fsMstPortRowStatus,'fsMstBpduGuard':fsMstBpduGuard,'dot1sFsMstTrapsControl':dot1sFsMstTrapsControl,'fsMstSetTraps':fsMstSetTraps,_A8:fsMstGenTrapType,_AB:fsMstErrTrapType,'fsMstPortTrapNotificationTable':fsMstPortTrapNotificationTable,'fsMstPortTrapNotificationEntry':fsMstPortTrapNotificationEntry,_a:fsMstPortTrapIndex,_AG:fsMstPortMigrationType,_AH:fsMstPktErrType,_AI:fsMstPktErrVal,'fsMstPortRoleTrapNotificationTable':fsMstPortRoleTrapNotificationTable,'fsMstPortRoleTrapNotificationEntry':fsMstPortRoleTrapNotificationEntry,_AN:fsMstPortRoleType,_AO:fsMstOldRoleType,'dot1sFutureMstTraps':dot1sFutureMstTraps,'fsMstTraps':fsMstTraps,'fsMstGenTrap':fsMstGenTrap,'fsMstErrTrap':fsMstErrTrap,'fsMstNewRootTrap':fsMstNewRootTrap,'fsMstTopologyChgTrap':fsMstTopologyChgTrap,'fsMstProtocolMigrationTrap':fsMstProtocolMigrationTrap,'fsMstInvalidBpduRxdTrap':fsMstInvalidBpduRxdTrap,'fsMstRegionConfigChangeTrap':fsMstRegionConfigChangeTrap,'fsMstNewPortRoleTrap':fsMstNewPortRoleTrap,'fsMstCistHwFailureTrap':fsMstCistHwFailureTrap,'fsMstMstiHwFailureTrap':fsMstMstiHwFailureTrap})