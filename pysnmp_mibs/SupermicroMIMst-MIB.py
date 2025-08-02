_AQ='fsMIMstMstiPortState'
_AP='fsMIMstCistPortState'
_AO='fsMIMstOldRoleType'
_AN='fsMIMstPortRoleType'
_AM='fsMIMstMstiConfigDigest'
_AL='fsMIMstMstiRegionVersion'
_AK='fsMIMstMstiRegionName'
_AJ='fsMIMstMstiConfigIdSel'
_AI='fsMIMstPktErrVal'
_AH='fsMIMstPktErrType'
_AG='fsMIMstPortMigrationType'
_AF='fsMIMstForceProtocolVersion'
_AE='fsMIMstMstiTopChanges'
_AD='fsMIMstMstiBridgeRegionalRoot'
_AC='fsMIMstOldDesignatedRoot'
_AB='fsMIMstGenTrapType'
_AA='fsMIMstGlobalErrTrapType'
_A9='designatedPort'
_A8='backupPort'
_A7='alternatePort'
_A6='disabledPort'
_A5='fsMIMstPort'
_A4='fsMIMstMstiPort'
_A3='acknowledged'
_A2='propagating'
_A1='notifiedtc'
_A0='notifiedtcn'
_z='alternateport'
_y='designatedport'
_x='rootport'
_w='disabledport'
_v='disableport'
_u='present'
_t='notdesg'
_s='inferiordesg'
_r='repeatdesg'
_q='superiordesg'
_p='update'
_o='sendstp'
_n='sendrstp'
_m='fsMIMstCistPort'
_l='disable'
_k='enable'
_j='timerExpiryEvent'
_i='bpduEvent'
_h='configurationEvent'
_g='roleselection'
_f='initbridge'
_e='stpCompatible'
_d='DisplayString'
_c='fsMIMstPortTrapIndex'
_b='none'
_a='init'
_Z='receive'
_Y='fsMIMstInstanceIndex'
_X='fsMIMstMstiInstanceIndex'
_W='enabled'
_V='masterport'
_U='designated'
_T='root'
_S='backup'
_R='alternate'
_Q='forwarding'
_P='discarding'
_O='fsMIDot1sFutureMstContextId'
_N='learning'
_M='Timeout'
_L='not-accessible'
_K='TruthValue'
_J='fsMIMstContextName'
_I='fsMIMstBrgAddress'
_H='centi-seconds'
_G='disabled'
_F='OctetString'
_E='SupermicroMIMst-MIB'
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
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_d,'MacAddress','PhysAddress','RowStatus','TextualConvention',_K)
futureMIMstMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,1,118))
if mibBuilder.loadTexts:futureMIMstMIB.setRevisions(('2012-09-05 00:00',))
class VlanId(TextualConvention,Integer32):status=_A;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
class BridgeId(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
class Timeout(TextualConvention,Integer32):status=_A;displayHint='d4'
class EnabledStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_W,1),(_G,2)))
_FsMIDot1sFutureMst_ObjectIdentity=ObjectIdentity
fsMIDot1sFutureMst=_FsMIDot1sFutureMst_ObjectIdentity((1,3,6,1,4,1,10876,101,1,118,1))
_FsMIMstGlobalTrace_Type=TruthValue
_FsMIMstGlobalTrace_Object=MibScalar
fsMIMstGlobalTrace=_FsMIMstGlobalTrace_Object((1,3,6,1,4,1,10876,101,1,118,1,1),_FsMIMstGlobalTrace_Type())
fsMIMstGlobalTrace.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstGlobalTrace.setStatus(_A)
_FsMIMstGlobalDebug_Type=TruthValue
_FsMIMstGlobalDebug_Object=MibScalar
fsMIMstGlobalDebug=_FsMIMstGlobalDebug_Object((1,3,6,1,4,1,10876,101,1,118,1,2),_FsMIMstGlobalDebug_Type())
fsMIMstGlobalDebug.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstGlobalDebug.setStatus(_A)
_FsMIDot1sFutureMstTable_Object=MibTable
fsMIDot1sFutureMstTable=_FsMIDot1sFutureMstTable_Object((1,3,6,1,4,1,10876,101,1,118,1,3))
if mibBuilder.loadTexts:fsMIDot1sFutureMstTable.setStatus(_A)
_FsMIDot1sFutureMstEntry_Object=MibTableRow
fsMIDot1sFutureMstEntry=_FsMIDot1sFutureMstEntry_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1))
fsMIDot1sFutureMstEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:fsMIDot1sFutureMstEntry.setStatus(_A)
class _FsMIDot1sFutureMstContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIDot1sFutureMstContextId_Type.__name__=_C
_FsMIDot1sFutureMstContextId_Object=MibTableColumn
fsMIDot1sFutureMstContextId=_FsMIDot1sFutureMstContextId_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,1),_FsMIDot1sFutureMstContextId_Type())
fsMIDot1sFutureMstContextId.setMaxAccess(_L)
if mibBuilder.loadTexts:fsMIDot1sFutureMstContextId.setStatus(_A)
class _FsMIMstSystemControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsMIMstSystemControl_Type.__name__=_C
_FsMIMstSystemControl_Object=MibTableColumn
fsMIMstSystemControl=_FsMIMstSystemControl_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,2),_FsMIMstSystemControl_Type())
fsMIMstSystemControl.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstSystemControl.setStatus(_A)
_FsMIMstModuleStatus_Type=EnabledStatus
_FsMIMstModuleStatus_Object=MibTableColumn
fsMIMstModuleStatus=_FsMIMstModuleStatus_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,3),_FsMIMstModuleStatus_Type())
fsMIMstModuleStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstModuleStatus.setStatus(_A)
class _FsMIMstMaxMstInstanceNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_FsMIMstMaxMstInstanceNumber_Type.__name__=_C
_FsMIMstMaxMstInstanceNumber_Object=MibTableColumn
fsMIMstMaxMstInstanceNumber=_FsMIMstMaxMstInstanceNumber_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,4),_FsMIMstMaxMstInstanceNumber_Type())
fsMIMstMaxMstInstanceNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstMaxMstInstanceNumber.setStatus(_A)
_FsMIMstNoOfMstiSupported_Type=Integer32
_FsMIMstNoOfMstiSupported_Object=MibTableColumn
fsMIMstNoOfMstiSupported=_FsMIMstNoOfMstiSupported_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,5),_FsMIMstNoOfMstiSupported_Type())
fsMIMstNoOfMstiSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstNoOfMstiSupported.setStatus(_A)
class _FsMIMstMaxHopCount_Type(Integer32):defaultValue=2000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(600,4000))
_FsMIMstMaxHopCount_Type.__name__=_C
_FsMIMstMaxHopCount_Object=MibTableColumn
fsMIMstMaxHopCount=_FsMIMstMaxHopCount_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,6),_FsMIMstMaxHopCount_Type())
fsMIMstMaxHopCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstMaxHopCount.setStatus(_A)
_FsMIMstBrgAddress_Type=MacAddress
_FsMIMstBrgAddress_Object=MibTableColumn
fsMIMstBrgAddress=_FsMIMstBrgAddress_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,7),_FsMIMstBrgAddress_Type())
fsMIMstBrgAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstBrgAddress.setStatus(_A)
_FsMIMstCistRoot_Type=BridgeId
_FsMIMstCistRoot_Object=MibTableColumn
fsMIMstCistRoot=_FsMIMstCistRoot_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,8),_FsMIMstCistRoot_Type())
fsMIMstCistRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistRoot.setStatus(_A)
_FsMIMstCistRegionalRoot_Type=BridgeId
_FsMIMstCistRegionalRoot_Object=MibTableColumn
fsMIMstCistRegionalRoot=_FsMIMstCistRegionalRoot_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,9),_FsMIMstCistRegionalRoot_Type())
fsMIMstCistRegionalRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistRegionalRoot.setStatus(_A)
_FsMIMstCistRootCost_Type=Integer32
_FsMIMstCistRootCost_Object=MibTableColumn
fsMIMstCistRootCost=_FsMIMstCistRootCost_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,10),_FsMIMstCistRootCost_Type())
fsMIMstCistRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistRootCost.setStatus(_A)
_FsMIMstCistRegionalRootCost_Type=Integer32
_FsMIMstCistRegionalRootCost_Object=MibTableColumn
fsMIMstCistRegionalRootCost=_FsMIMstCistRegionalRootCost_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,11),_FsMIMstCistRegionalRootCost_Type())
fsMIMstCistRegionalRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistRegionalRootCost.setStatus(_A)
_FsMIMstCistRootPort_Type=Integer32
_FsMIMstCistRootPort_Object=MibTableColumn
fsMIMstCistRootPort=_FsMIMstCistRootPort_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,12),_FsMIMstCistRootPort_Type())
fsMIMstCistRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistRootPort.setStatus(_A)
class _FsMIMstCistBridgePriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_FsMIMstCistBridgePriority_Type.__name__=_C
_FsMIMstCistBridgePriority_Object=MibTableColumn
fsMIMstCistBridgePriority=_FsMIMstCistBridgePriority_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,13),_FsMIMstCistBridgePriority_Type())
fsMIMstCistBridgePriority.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstCistBridgePriority.setStatus(_A)
class _FsMIMstCistBridgeMaxAge_Type(Timeout):defaultValue=2000;subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(600,4000))
_FsMIMstCistBridgeMaxAge_Type.__name__=_M
_FsMIMstCistBridgeMaxAge_Object=MibTableColumn
fsMIMstCistBridgeMaxAge=_FsMIMstCistBridgeMaxAge_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,14),_FsMIMstCistBridgeMaxAge_Type())
fsMIMstCistBridgeMaxAge.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstCistBridgeMaxAge.setStatus(_A)
if mibBuilder.loadTexts:fsMIMstCistBridgeMaxAge.setUnits(_H)
class _FsMIMstCistBridgeForwardDelay_Type(Timeout):defaultValue=1500;subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(400,3000))
_FsMIMstCistBridgeForwardDelay_Type.__name__=_M
_FsMIMstCistBridgeForwardDelay_Object=MibTableColumn
fsMIMstCistBridgeForwardDelay=_FsMIMstCistBridgeForwardDelay_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,15),_FsMIMstCistBridgeForwardDelay_Type())
fsMIMstCistBridgeForwardDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstCistBridgeForwardDelay.setStatus(_A)
if mibBuilder.loadTexts:fsMIMstCistBridgeForwardDelay.setUnits(_H)
_FsMIMstCistHoldTime_Type=Integer32
_FsMIMstCistHoldTime_Object=MibTableColumn
fsMIMstCistHoldTime=_FsMIMstCistHoldTime_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,16),_FsMIMstCistHoldTime_Type())
fsMIMstCistHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistHoldTime.setStatus(_A)
if mibBuilder.loadTexts:fsMIMstCistHoldTime.setUnits(_H)
_FsMIMstCistMaxAge_Type=Timeout
_FsMIMstCistMaxAge_Object=MibTableColumn
fsMIMstCistMaxAge=_FsMIMstCistMaxAge_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,17),_FsMIMstCistMaxAge_Type())
fsMIMstCistMaxAge.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistMaxAge.setStatus(_A)
if mibBuilder.loadTexts:fsMIMstCistMaxAge.setUnits(_H)
_FsMIMstCistForwardDelay_Type=Timeout
_FsMIMstCistForwardDelay_Object=MibTableColumn
fsMIMstCistForwardDelay=_FsMIMstCistForwardDelay_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,18),_FsMIMstCistForwardDelay_Type())
fsMIMstCistForwardDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistForwardDelay.setStatus(_A)
if mibBuilder.loadTexts:fsMIMstCistForwardDelay.setUnits(_H)
_FsMIMstMstpUpCount_Type=Counter32
_FsMIMstMstpUpCount_Object=MibTableColumn
fsMIMstMstpUpCount=_FsMIMstMstpUpCount_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,19),_FsMIMstMstpUpCount_Type())
fsMIMstMstpUpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstpUpCount.setStatus(_A)
_FsMIMstMstpDownCount_Type=Counter32
_FsMIMstMstpDownCount_Object=MibTableColumn
fsMIMstMstpDownCount=_FsMIMstMstpDownCount_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,20),_FsMIMstMstpDownCount_Type())
fsMIMstMstpDownCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstpDownCount.setStatus(_A)
class _FsMIMstPathCostDefaultType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stp8021d1998',1),('stp8021t2001',2)))
_FsMIMstPathCostDefaultType_Type.__name__=_C
_FsMIMstPathCostDefaultType_Object=MibTableColumn
fsMIMstPathCostDefaultType=_FsMIMstPathCostDefaultType_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,21),_FsMIMstPathCostDefaultType_Type())
fsMIMstPathCostDefaultType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstPathCostDefaultType.setStatus('obsolete')
class _FsMIMstTrace_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIMstTrace_Type.__name__=_C
_FsMIMstTrace_Object=MibTableColumn
fsMIMstTrace=_FsMIMstTrace_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,22),_FsMIMstTrace_Type())
fsMIMstTrace.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstTrace.setStatus(_A)
class _FsMIMstDebug_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,524287))
_FsMIMstDebug_Type.__name__=_C
_FsMIMstDebug_Object=MibTableColumn
fsMIMstDebug=_FsMIMstDebug_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,23),_FsMIMstDebug_Type())
fsMIMstDebug.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstDebug.setStatus(_A)
class _FsMIMstForceProtocolVersion_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3)));namedValues=NamedValues(*((_e,0),('rstp',2),('mstp',3)))
_FsMIMstForceProtocolVersion_Type.__name__=_C
_FsMIMstForceProtocolVersion_Object=MibTableColumn
fsMIMstForceProtocolVersion=_FsMIMstForceProtocolVersion_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,24),_FsMIMstForceProtocolVersion_Type())
fsMIMstForceProtocolVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstForceProtocolVersion.setStatus(_A)
class _FsMIMstTxHoldCount_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FsMIMstTxHoldCount_Type.__name__=_C
_FsMIMstTxHoldCount_Object=MibTableColumn
fsMIMstTxHoldCount=_FsMIMstTxHoldCount_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,25),_FsMIMstTxHoldCount_Type())
fsMIMstTxHoldCount.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstTxHoldCount.setStatus(_A)
class _FsMIMstMstiConfigIdSel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsMIMstMstiConfigIdSel_Type.__name__=_C
_FsMIMstMstiConfigIdSel_Object=MibTableColumn
fsMIMstMstiConfigIdSel=_FsMIMstMstiConfigIdSel_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,26),_FsMIMstMstiConfigIdSel_Type())
fsMIMstMstiConfigIdSel.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstMstiConfigIdSel.setStatus(_A)
class _FsMIMstMstiRegionName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsMIMstMstiRegionName_Type.__name__=_F
_FsMIMstMstiRegionName_Object=MibTableColumn
fsMIMstMstiRegionName=_FsMIMstMstiRegionName_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,27),_FsMIMstMstiRegionName_Type())
fsMIMstMstiRegionName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstMstiRegionName.setStatus(_A)
class _FsMIMstMstiRegionVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIMstMstiRegionVersion_Type.__name__=_C
_FsMIMstMstiRegionVersion_Object=MibTableColumn
fsMIMstMstiRegionVersion=_FsMIMstMstiRegionVersion_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,28),_FsMIMstMstiRegionVersion_Type())
fsMIMstMstiRegionVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstMstiRegionVersion.setStatus(_A)
class _FsMIMstMstiConfigDigest_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsMIMstMstiConfigDigest_Type.__name__=_F
_FsMIMstMstiConfigDigest_Object=MibTableColumn
fsMIMstMstiConfigDigest=_FsMIMstMstiConfigDigest_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,29),_FsMIMstMstiConfigDigest_Type())
fsMIMstMstiConfigDigest.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiConfigDigest.setStatus(_A)
_FsMIMstBufferOverFlowCount_Type=Counter32
_FsMIMstBufferOverFlowCount_Object=MibTableColumn
fsMIMstBufferOverFlowCount=_FsMIMstBufferOverFlowCount_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,30),_FsMIMstBufferOverFlowCount_Type())
fsMIMstBufferOverFlowCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstBufferOverFlowCount.setStatus(_A)
_FsMIMstMemAllocFailureCount_Type=Counter32
_FsMIMstMemAllocFailureCount_Object=MibTableColumn
fsMIMstMemAllocFailureCount=_FsMIMstMemAllocFailureCount_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,31),_FsMIMstMemAllocFailureCount_Type())
fsMIMstMemAllocFailureCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMemAllocFailureCount.setStatus(_A)
_FsMIMstRegionConfigChangeCount_Type=Counter32
_FsMIMstRegionConfigChangeCount_Object=MibTableColumn
fsMIMstRegionConfigChangeCount=_FsMIMstRegionConfigChangeCount_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,32),_FsMIMstRegionConfigChangeCount_Type())
fsMIMstRegionConfigChangeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstRegionConfigChangeCount.setStatus(_A)
class _FsMIMstCistBridgeRoleSelectionSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_f,0),(_g,1)))
_FsMIMstCistBridgeRoleSelectionSemState_Type.__name__=_C
_FsMIMstCistBridgeRoleSelectionSemState_Object=MibTableColumn
fsMIMstCistBridgeRoleSelectionSemState=_FsMIMstCistBridgeRoleSelectionSemState_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,33),_FsMIMstCistBridgeRoleSelectionSemState_Type())
fsMIMstCistBridgeRoleSelectionSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistBridgeRoleSelectionSemState.setStatus(_A)
_FsMIMstCistTimeSinceTopologyChange_Type=TimeTicks
_FsMIMstCistTimeSinceTopologyChange_Object=MibTableColumn
fsMIMstCistTimeSinceTopologyChange=_FsMIMstCistTimeSinceTopologyChange_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,34),_FsMIMstCistTimeSinceTopologyChange_Type())
fsMIMstCistTimeSinceTopologyChange.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistTimeSinceTopologyChange.setStatus(_A)
if mibBuilder.loadTexts:fsMIMstCistTimeSinceTopologyChange.setUnits(_H)
_FsMIMstCistTopChanges_Type=Counter32
_FsMIMstCistTopChanges_Object=MibTableColumn
fsMIMstCistTopChanges=_FsMIMstCistTopChanges_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,35),_FsMIMstCistTopChanges_Type())
fsMIMstCistTopChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistTopChanges.setStatus(_A)
_FsMIMstCistNewRootBridgeCount_Type=Counter32
_FsMIMstCistNewRootBridgeCount_Object=MibTableColumn
fsMIMstCistNewRootBridgeCount=_FsMIMstCistNewRootBridgeCount_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,36),_FsMIMstCistNewRootBridgeCount_Type())
fsMIMstCistNewRootBridgeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistNewRootBridgeCount.setStatus(_A)
_FsMIMstCistHelloTime_Type=Timeout
_FsMIMstCistHelloTime_Object=MibTableColumn
fsMIMstCistHelloTime=_FsMIMstCistHelloTime_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,37),_FsMIMstCistHelloTime_Type())
fsMIMstCistHelloTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistHelloTime.setStatus(_A)
if mibBuilder.loadTexts:fsMIMstCistHelloTime.setUnits(_H)
class _FsMIMstCistBridgeHelloTime_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,100),ValueRangeConstraint(200,200))
_FsMIMstCistBridgeHelloTime_Type.__name__=_M
_FsMIMstCistBridgeHelloTime_Object=MibTableColumn
fsMIMstCistBridgeHelloTime=_FsMIMstCistBridgeHelloTime_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,38),_FsMIMstCistBridgeHelloTime_Type())
fsMIMstCistBridgeHelloTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstCistBridgeHelloTime.setStatus(_A)
if mibBuilder.loadTexts:fsMIMstCistBridgeHelloTime.setUnits(_H)
class _FsMIMstCistDynamicPathcostCalculation_Type(TruthValue):defaultValue=2
_FsMIMstCistDynamicPathcostCalculation_Type.__name__=_K
_FsMIMstCistDynamicPathcostCalculation_Object=MibTableColumn
fsMIMstCistDynamicPathcostCalculation=_FsMIMstCistDynamicPathcostCalculation_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,39),_FsMIMstCistDynamicPathcostCalculation_Type())
fsMIMstCistDynamicPathcostCalculation.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstCistDynamicPathcostCalculation.setStatus(_A)
class _FsMIMstContextName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsMIMstContextName_Type.__name__=_d
_FsMIMstContextName_Object=MibTableColumn
fsMIMstContextName=_FsMIMstContextName_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,40),_FsMIMstContextName_Type())
fsMIMstContextName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstContextName.setStatus(_A)
class _FsMIMstCalcPortPathCostOnSpeedChg_Type(TruthValue):defaultValue=2
_FsMIMstCalcPortPathCostOnSpeedChg_Type.__name__=_K
_FsMIMstCalcPortPathCostOnSpeedChg_Object=MibTableColumn
fsMIMstCalcPortPathCostOnSpeedChg=_FsMIMstCalcPortPathCostOnSpeedChg_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,41),_FsMIMstCalcPortPathCostOnSpeedChg_Type())
fsMIMstCalcPortPathCostOnSpeedChg.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstCalcPortPathCostOnSpeedChg.setStatus(_A)
_FsMIMstClearBridgeStats_Type=TruthValue
_FsMIMstClearBridgeStats_Object=MibTableColumn
fsMIMstClearBridgeStats=_FsMIMstClearBridgeStats_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,42),_FsMIMstClearBridgeStats_Type())
fsMIMstClearBridgeStats.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstClearBridgeStats.setStatus(_A)
class _FsMIMstRcvdEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_h,1),(_i,2),(_j,3)))
_FsMIMstRcvdEvent_Type.__name__=_C
_FsMIMstRcvdEvent_Object=MibTableColumn
fsMIMstRcvdEvent=_FsMIMstRcvdEvent_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,43),_FsMIMstRcvdEvent_Type())
fsMIMstRcvdEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstRcvdEvent.setStatus(_A)
_FsMIMstRcvdEventSubType_Type=Integer32
_FsMIMstRcvdEventSubType_Object=MibTableColumn
fsMIMstRcvdEventSubType=_FsMIMstRcvdEventSubType_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,44),_FsMIMstRcvdEventSubType_Type())
fsMIMstRcvdEventSubType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstRcvdEventSubType.setStatus(_A)
_FsMIMstRcvdEventTimeStamp_Type=Unsigned32
_FsMIMstRcvdEventTimeStamp_Object=MibTableColumn
fsMIMstRcvdEventTimeStamp=_FsMIMstRcvdEventTimeStamp_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,45),_FsMIMstRcvdEventTimeStamp_Type())
fsMIMstRcvdEventTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstRcvdEventTimeStamp.setStatus(_A)
_FsMIMstPortStateChangeTimeStamp_Type=Unsigned32
_FsMIMstPortStateChangeTimeStamp_Object=MibTableColumn
fsMIMstPortStateChangeTimeStamp=_FsMIMstPortStateChangeTimeStamp_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,46),_FsMIMstPortStateChangeTimeStamp_Type())
fsMIMstPortStateChangeTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstPortStateChangeTimeStamp.setStatus(_A)
class _FsMIMstFlushInterval_Type(Timeout):defaultValue=0;subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_FsMIMstFlushInterval_Type.__name__=_M
_FsMIMstFlushInterval_Object=MibTableColumn
fsMIMstFlushInterval=_FsMIMstFlushInterval_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,47),_FsMIMstFlushInterval_Type())
fsMIMstFlushInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstFlushInterval.setStatus(_A)
if mibBuilder.loadTexts:fsMIMstFlushInterval.setUnits(_H)
class _FsMIMstCistFlushIndicationThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIMstCistFlushIndicationThreshold_Type.__name__=_C
_FsMIMstCistFlushIndicationThreshold_Object=MibTableColumn
fsMIMstCistFlushIndicationThreshold=_FsMIMstCistFlushIndicationThreshold_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,48),_FsMIMstCistFlushIndicationThreshold_Type())
fsMIMstCistFlushIndicationThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstCistFlushIndicationThreshold.setStatus(_A)
_FsMIMstCistTotalFlushCount_Type=Counter32
_FsMIMstCistTotalFlushCount_Object=MibTableColumn
fsMIMstCistTotalFlushCount=_FsMIMstCistTotalFlushCount_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,49),_FsMIMstCistTotalFlushCount_Type())
fsMIMstCistTotalFlushCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistTotalFlushCount.setStatus(_A)
class _FsMIMstBpduGuard_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_k,1),(_l,2)))
_FsMIMstBpduGuard_Type.__name__=_C
_FsMIMstBpduGuard_Object=MibTableColumn
fsMIMstBpduGuard=_FsMIMstBpduGuard_Object((1,3,6,1,4,1,10876,101,1,118,1,3,1,50),_FsMIMstBpduGuard_Type())
fsMIMstBpduGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstBpduGuard.setStatus(_A)
_FsMIMstMstiBridgeTable_Object=MibTable
fsMIMstMstiBridgeTable=_FsMIMstMstiBridgeTable_Object((1,3,6,1,4,1,10876,101,1,118,1,4))
if mibBuilder.loadTexts:fsMIMstMstiBridgeTable.setStatus(_A)
_FsMIMstMstiBridgeEntry_Object=MibTableRow
fsMIMstMstiBridgeEntry=_FsMIMstMstiBridgeEntry_Object((1,3,6,1,4,1,10876,101,1,118,1,4,1))
fsMIMstMstiBridgeEntry.setIndexNames((0,_E,_O),(0,_E,_X))
if mibBuilder.loadTexts:fsMIMstMstiBridgeEntry.setStatus(_A)
class _FsMIMstMstiInstanceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64),ValueRangeConstraint(4094,4094))
_FsMIMstMstiInstanceIndex_Type.__name__=_C
_FsMIMstMstiInstanceIndex_Object=MibTableColumn
fsMIMstMstiInstanceIndex=_FsMIMstMstiInstanceIndex_Object((1,3,6,1,4,1,10876,101,1,118,1,4,1,1),_FsMIMstMstiInstanceIndex_Type())
fsMIMstMstiInstanceIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:fsMIMstMstiInstanceIndex.setStatus(_A)
_FsMIMstMstiBridgeRegionalRoot_Type=BridgeId
_FsMIMstMstiBridgeRegionalRoot_Object=MibTableColumn
fsMIMstMstiBridgeRegionalRoot=_FsMIMstMstiBridgeRegionalRoot_Object((1,3,6,1,4,1,10876,101,1,118,1,4,1,2),_FsMIMstMstiBridgeRegionalRoot_Type())
fsMIMstMstiBridgeRegionalRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiBridgeRegionalRoot.setStatus(_A)
class _FsMIMstMstiBridgePriority_Type(Integer32):defaultValue=32768;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,61440))
_FsMIMstMstiBridgePriority_Type.__name__=_C
_FsMIMstMstiBridgePriority_Object=MibTableColumn
fsMIMstMstiBridgePriority=_FsMIMstMstiBridgePriority_Object((1,3,6,1,4,1,10876,101,1,118,1,4,1,3),_FsMIMstMstiBridgePriority_Type())
fsMIMstMstiBridgePriority.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstMstiBridgePriority.setStatus(_A)
_FsMIMstMstiRootCost_Type=Integer32
_FsMIMstMstiRootCost_Object=MibTableColumn
fsMIMstMstiRootCost=_FsMIMstMstiRootCost_Object((1,3,6,1,4,1,10876,101,1,118,1,4,1,4),_FsMIMstMstiRootCost_Type())
fsMIMstMstiRootCost.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiRootCost.setStatus(_A)
_FsMIMstMstiRootPort_Type=Integer32
_FsMIMstMstiRootPort_Object=MibTableColumn
fsMIMstMstiRootPort=_FsMIMstMstiRootPort_Object((1,3,6,1,4,1,10876,101,1,118,1,4,1,5),_FsMIMstMstiRootPort_Type())
fsMIMstMstiRootPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiRootPort.setStatus(_A)
_FsMIMstMstiTimeSinceTopologyChange_Type=TimeTicks
_FsMIMstMstiTimeSinceTopologyChange_Object=MibTableColumn
fsMIMstMstiTimeSinceTopologyChange=_FsMIMstMstiTimeSinceTopologyChange_Object((1,3,6,1,4,1,10876,101,1,118,1,4,1,6),_FsMIMstMstiTimeSinceTopologyChange_Type())
fsMIMstMstiTimeSinceTopologyChange.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiTimeSinceTopologyChange.setStatus(_A)
if mibBuilder.loadTexts:fsMIMstMstiTimeSinceTopologyChange.setUnits(_H)
_FsMIMstMstiTopChanges_Type=Counter32
_FsMIMstMstiTopChanges_Object=MibTableColumn
fsMIMstMstiTopChanges=_FsMIMstMstiTopChanges_Object((1,3,6,1,4,1,10876,101,1,118,1,4,1,7),_FsMIMstMstiTopChanges_Type())
fsMIMstMstiTopChanges.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiTopChanges.setStatus(_A)
_FsMIMstMstiNewRootBridgeCount_Type=Counter32
_FsMIMstMstiNewRootBridgeCount_Object=MibTableColumn
fsMIMstMstiNewRootBridgeCount=_FsMIMstMstiNewRootBridgeCount_Object((1,3,6,1,4,1,10876,101,1,118,1,4,1,8),_FsMIMstMstiNewRootBridgeCount_Type())
fsMIMstMstiNewRootBridgeCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiNewRootBridgeCount.setStatus(_A)
class _FsMIMstMstiBridgeRoleSelectionSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_f,0),(_g,1)))
_FsMIMstMstiBridgeRoleSelectionSemState_Type.__name__=_C
_FsMIMstMstiBridgeRoleSelectionSemState_Object=MibTableColumn
fsMIMstMstiBridgeRoleSelectionSemState=_FsMIMstMstiBridgeRoleSelectionSemState_Object((1,3,6,1,4,1,10876,101,1,118,1,4,1,9),_FsMIMstMstiBridgeRoleSelectionSemState_Type())
fsMIMstMstiBridgeRoleSelectionSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiBridgeRoleSelectionSemState.setStatus(_A)
_FsMIMstInstanceUpCount_Type=Counter32
_FsMIMstInstanceUpCount_Object=MibTableColumn
fsMIMstInstanceUpCount=_FsMIMstInstanceUpCount_Object((1,3,6,1,4,1,10876,101,1,118,1,4,1,10),_FsMIMstInstanceUpCount_Type())
fsMIMstInstanceUpCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstInstanceUpCount.setStatus(_A)
_FsMIMstInstanceDownCount_Type=Counter32
_FsMIMstInstanceDownCount_Object=MibTableColumn
fsMIMstInstanceDownCount=_FsMIMstInstanceDownCount_Object((1,3,6,1,4,1,10876,101,1,118,1,4,1,11),_FsMIMstInstanceDownCount_Type())
fsMIMstInstanceDownCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstInstanceDownCount.setStatus(_A)
_FsMIMstOldDesignatedRoot_Type=BridgeId
_FsMIMstOldDesignatedRoot_Object=MibTableColumn
fsMIMstOldDesignatedRoot=_FsMIMstOldDesignatedRoot_Object((1,3,6,1,4,1,10876,101,1,118,1,4,1,12),_FsMIMstOldDesignatedRoot_Type())
fsMIMstOldDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstOldDesignatedRoot.setStatus(_A)
_FsMIMstMstiClearBridgeStats_Type=TruthValue
_FsMIMstMstiClearBridgeStats_Object=MibTableColumn
fsMIMstMstiClearBridgeStats=_FsMIMstMstiClearBridgeStats_Object((1,3,6,1,4,1,10876,101,1,118,1,4,1,13),_FsMIMstMstiClearBridgeStats_Type())
fsMIMstMstiClearBridgeStats.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstMstiClearBridgeStats.setStatus(_A)
class _FsMIMstMstiFlushIndicationThreshold_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIMstMstiFlushIndicationThreshold_Type.__name__=_C
_FsMIMstMstiFlushIndicationThreshold_Object=MibTableColumn
fsMIMstMstiFlushIndicationThreshold=_FsMIMstMstiFlushIndicationThreshold_Object((1,3,6,1,4,1,10876,101,1,118,1,4,1,14),_FsMIMstMstiFlushIndicationThreshold_Type())
fsMIMstMstiFlushIndicationThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstMstiFlushIndicationThreshold.setStatus(_A)
_FsMIMstMstiTotalFlushCount_Type=Counter32
_FsMIMstMstiTotalFlushCount_Object=MibTableColumn
fsMIMstMstiTotalFlushCount=_FsMIMstMstiTotalFlushCount_Object((1,3,6,1,4,1,10876,101,1,118,1,4,1,15),_FsMIMstMstiTotalFlushCount_Type())
fsMIMstMstiTotalFlushCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiTotalFlushCount.setStatus(_A)
_FsMIMstVlanInstanceMappingTable_Object=MibTable
fsMIMstVlanInstanceMappingTable=_FsMIMstVlanInstanceMappingTable_Object((1,3,6,1,4,1,10876,101,1,118,1,5))
if mibBuilder.loadTexts:fsMIMstVlanInstanceMappingTable.setStatus(_A)
_FsMIMstVlanInstanceMappingEntry_Object=MibTableRow
fsMIMstVlanInstanceMappingEntry=_FsMIMstVlanInstanceMappingEntry_Object((1,3,6,1,4,1,10876,101,1,118,1,5,1))
fsMIMstVlanInstanceMappingEntry.setIndexNames((0,_E,_O),(0,_E,_Y))
if mibBuilder.loadTexts:fsMIMstVlanInstanceMappingEntry.setStatus(_A)
class _FsMIMstInstanceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64),ValueRangeConstraint(4094,4094))
_FsMIMstInstanceIndex_Type.__name__=_C
_FsMIMstInstanceIndex_Object=MibTableColumn
fsMIMstInstanceIndex=_FsMIMstInstanceIndex_Object((1,3,6,1,4,1,10876,101,1,118,1,5,1,1),_FsMIMstInstanceIndex_Type())
fsMIMstInstanceIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:fsMIMstInstanceIndex.setStatus(_A)
_FsMIMstMapVlanIndex_Type=VlanId
_FsMIMstMapVlanIndex_Object=MibTableColumn
fsMIMstMapVlanIndex=_FsMIMstMapVlanIndex_Object((1,3,6,1,4,1,10876,101,1,118,1,5,1,2),_FsMIMstMapVlanIndex_Type())
fsMIMstMapVlanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstMapVlanIndex.setStatus(_A)
_FsMIMstUnMapVlanIndex_Type=VlanId
_FsMIMstUnMapVlanIndex_Object=MibTableColumn
fsMIMstUnMapVlanIndex=_FsMIMstUnMapVlanIndex_Object((1,3,6,1,4,1,10876,101,1,118,1,5,1,3),_FsMIMstUnMapVlanIndex_Type())
fsMIMstUnMapVlanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstUnMapVlanIndex.setStatus(_A)
class _FsMIMstSetVlanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_FsMIMstSetVlanList_Type.__name__=_F
_FsMIMstSetVlanList_Object=MibTableColumn
fsMIMstSetVlanList=_FsMIMstSetVlanList_Object((1,3,6,1,4,1,10876,101,1,118,1,5,1,4),_FsMIMstSetVlanList_Type())
fsMIMstSetVlanList.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstSetVlanList.setStatus(_A)
class _FsMIMstResetVlanList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_FsMIMstResetVlanList_Type.__name__=_F
_FsMIMstResetVlanList_Object=MibTableColumn
fsMIMstResetVlanList=_FsMIMstResetVlanList_Object((1,3,6,1,4,1,10876,101,1,118,1,5,1,5),_FsMIMstResetVlanList_Type())
fsMIMstResetVlanList.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstResetVlanList.setStatus(_A)
class _FsMIMstInstanceVlanMapped_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FsMIMstInstanceVlanMapped_Type.__name__=_F
_FsMIMstInstanceVlanMapped_Object=MibTableColumn
fsMIMstInstanceVlanMapped=_FsMIMstInstanceVlanMapped_Object((1,3,6,1,4,1,10876,101,1,118,1,5,1,6),_FsMIMstInstanceVlanMapped_Type())
fsMIMstInstanceVlanMapped.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstInstanceVlanMapped.setStatus(_A)
class _FsMIMstInstanceVlanMapped2k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FsMIMstInstanceVlanMapped2k_Type.__name__=_F
_FsMIMstInstanceVlanMapped2k_Object=MibTableColumn
fsMIMstInstanceVlanMapped2k=_FsMIMstInstanceVlanMapped2k_Object((1,3,6,1,4,1,10876,101,1,118,1,5,1,7),_FsMIMstInstanceVlanMapped2k_Type())
fsMIMstInstanceVlanMapped2k.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstInstanceVlanMapped2k.setStatus(_A)
class _FsMIMstInstanceVlanMapped3k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FsMIMstInstanceVlanMapped3k_Type.__name__=_F
_FsMIMstInstanceVlanMapped3k_Object=MibTableColumn
fsMIMstInstanceVlanMapped3k=_FsMIMstInstanceVlanMapped3k_Object((1,3,6,1,4,1,10876,101,1,118,1,5,1,8),_FsMIMstInstanceVlanMapped3k_Type())
fsMIMstInstanceVlanMapped3k.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstInstanceVlanMapped3k.setStatus(_A)
class _FsMIMstInstanceVlanMapped4k_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_FsMIMstInstanceVlanMapped4k_Type.__name__=_F
_FsMIMstInstanceVlanMapped4k_Object=MibTableColumn
fsMIMstInstanceVlanMapped4k=_FsMIMstInstanceVlanMapped4k_Object((1,3,6,1,4,1,10876,101,1,118,1,5,1,9),_FsMIMstInstanceVlanMapped4k_Type())
fsMIMstInstanceVlanMapped4k.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstInstanceVlanMapped4k.setStatus(_A)
_FsMIMstCistPortTable_Object=MibTable
fsMIMstCistPortTable=_FsMIMstCistPortTable_Object((1,3,6,1,4,1,10876,101,1,118,1,6))
if mibBuilder.loadTexts:fsMIMstCistPortTable.setStatus(_A)
_FsMIMstCistPortEntry_Object=MibTableRow
fsMIMstCistPortEntry=_FsMIMstCistPortEntry_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1))
fsMIMstCistPortEntry.setIndexNames((0,_E,_m))
if mibBuilder.loadTexts:fsMIMstCistPortEntry.setStatus(_A)
class _FsMIMstCistPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsMIMstCistPort_Type.__name__=_C
_FsMIMstCistPort_Object=MibTableColumn
fsMIMstCistPort=_FsMIMstCistPort_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,1),_FsMIMstCistPort_Type())
fsMIMstCistPort.setMaxAccess(_L)
if mibBuilder.loadTexts:fsMIMstCistPort.setStatus(_A)
class _FsMIMstCistPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_FsMIMstCistPortPathCost_Type.__name__=_C
_FsMIMstCistPortPathCost_Object=MibTableColumn
fsMIMstCistPortPathCost=_FsMIMstCistPortPathCost_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,2),_FsMIMstCistPortPathCost_Type())
fsMIMstCistPortPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstCistPortPathCost.setStatus(_A)
class _FsMIMstCistPortPriority_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_FsMIMstCistPortPriority_Type.__name__=_C
_FsMIMstCistPortPriority_Object=MibTableColumn
fsMIMstCistPortPriority=_FsMIMstCistPortPriority_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,3),_FsMIMstCistPortPriority_Type())
fsMIMstCistPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstCistPortPriority.setStatus(_A)
_FsMIMstCistPortDesignatedRoot_Type=BridgeId
_FsMIMstCistPortDesignatedRoot_Object=MibTableColumn
fsMIMstCistPortDesignatedRoot=_FsMIMstCistPortDesignatedRoot_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,4),_FsMIMstCistPortDesignatedRoot_Type())
fsMIMstCistPortDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortDesignatedRoot.setStatus(_A)
_FsMIMstCistPortDesignatedBridge_Type=BridgeId
_FsMIMstCistPortDesignatedBridge_Object=MibTableColumn
fsMIMstCistPortDesignatedBridge=_FsMIMstCistPortDesignatedBridge_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,5),_FsMIMstCistPortDesignatedBridge_Type())
fsMIMstCistPortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortDesignatedBridge.setStatus(_A)
class _FsMIMstCistPortDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_FsMIMstCistPortDesignatedPort_Type.__name__=_F
_FsMIMstCistPortDesignatedPort_Object=MibTableColumn
fsMIMstCistPortDesignatedPort=_FsMIMstCistPortDesignatedPort_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,6),_FsMIMstCistPortDesignatedPort_Type())
fsMIMstCistPortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortDesignatedPort.setStatus(_A)
class _FsMIMstCistPortAdminP2P_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('forceTrue',0),('forceFalse',1),('auto',2)))
_FsMIMstCistPortAdminP2P_Type.__name__=_C
_FsMIMstCistPortAdminP2P_Object=MibTableColumn
fsMIMstCistPortAdminP2P=_FsMIMstCistPortAdminP2P_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,7),_FsMIMstCistPortAdminP2P_Type())
fsMIMstCistPortAdminP2P.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstCistPortAdminP2P.setStatus(_A)
_FsMIMstCistPortOperP2P_Type=TruthValue
_FsMIMstCistPortOperP2P_Object=MibTableColumn
fsMIMstCistPortOperP2P=_FsMIMstCistPortOperP2P_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,8),_FsMIMstCistPortOperP2P_Type())
fsMIMstCistPortOperP2P.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortOperP2P.setStatus(_A)
_FsMIMstCistPortAdminEdgeStatus_Type=TruthValue
_FsMIMstCistPortAdminEdgeStatus_Object=MibTableColumn
fsMIMstCistPortAdminEdgeStatus=_FsMIMstCistPortAdminEdgeStatus_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,9),_FsMIMstCistPortAdminEdgeStatus_Type())
fsMIMstCistPortAdminEdgeStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstCistPortAdminEdgeStatus.setStatus(_A)
_FsMIMstCistPortOperEdgeStatus_Type=TruthValue
_FsMIMstCistPortOperEdgeStatus_Object=MibTableColumn
fsMIMstCistPortOperEdgeStatus=_FsMIMstCistPortOperEdgeStatus_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,10),_FsMIMstCistPortOperEdgeStatus_Type())
fsMIMstCistPortOperEdgeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortOperEdgeStatus.setStatus(_A)
_FsMIMstCistPortProtocolMigration_Type=TruthValue
_FsMIMstCistPortProtocolMigration_Object=MibTableColumn
fsMIMstCistPortProtocolMigration=_FsMIMstCistPortProtocolMigration_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,11),_FsMIMstCistPortProtocolMigration_Type())
fsMIMstCistPortProtocolMigration.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstCistPortProtocolMigration.setStatus(_A)
class _FsMIMstCistPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5)));namedValues=NamedValues(*((_G,1),(_P,2),(_N,4),(_Q,5)))
_FsMIMstCistPortState_Type.__name__=_C
_FsMIMstCistPortState_Object=MibTableColumn
fsMIMstCistPortState=_FsMIMstCistPortState_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,12),_FsMIMstCistPortState_Type())
fsMIMstCistPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortState.setStatus(_A)
class _FsMIMstCistForcePortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_W,1)))
_FsMIMstCistForcePortState_Type.__name__=_C
_FsMIMstCistForcePortState_Object=MibTableColumn
fsMIMstCistForcePortState=_FsMIMstCistForcePortState_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,13),_FsMIMstCistForcePortState_Type())
fsMIMstCistForcePortState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstCistForcePortState.setStatus(_A)
_FsMIMstCistPortForwardTransitions_Type=Counter32
_FsMIMstCistPortForwardTransitions_Object=MibTableColumn
fsMIMstCistPortForwardTransitions=_FsMIMstCistPortForwardTransitions_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,14),_FsMIMstCistPortForwardTransitions_Type())
fsMIMstCistPortForwardTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortForwardTransitions.setStatus(_A)
_FsMIMstCistPortRxMstBpduCount_Type=Counter32
_FsMIMstCistPortRxMstBpduCount_Object=MibTableColumn
fsMIMstCistPortRxMstBpduCount=_FsMIMstCistPortRxMstBpduCount_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,15),_FsMIMstCistPortRxMstBpduCount_Type())
fsMIMstCistPortRxMstBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortRxMstBpduCount.setStatus(_A)
_FsMIMstCistPortRxRstBpduCount_Type=Counter32
_FsMIMstCistPortRxRstBpduCount_Object=MibTableColumn
fsMIMstCistPortRxRstBpduCount=_FsMIMstCistPortRxRstBpduCount_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,16),_FsMIMstCistPortRxRstBpduCount_Type())
fsMIMstCistPortRxRstBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortRxRstBpduCount.setStatus(_A)
_FsMIMstCistPortRxConfigBpduCount_Type=Counter32
_FsMIMstCistPortRxConfigBpduCount_Object=MibTableColumn
fsMIMstCistPortRxConfigBpduCount=_FsMIMstCistPortRxConfigBpduCount_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,17),_FsMIMstCistPortRxConfigBpduCount_Type())
fsMIMstCistPortRxConfigBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortRxConfigBpduCount.setStatus(_A)
_FsMIMstCistPortRxTcnBpduCount_Type=Counter32
_FsMIMstCistPortRxTcnBpduCount_Object=MibTableColumn
fsMIMstCistPortRxTcnBpduCount=_FsMIMstCistPortRxTcnBpduCount_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,18),_FsMIMstCistPortRxTcnBpduCount_Type())
fsMIMstCistPortRxTcnBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortRxTcnBpduCount.setStatus(_A)
_FsMIMstCistPortTxMstBpduCount_Type=Counter32
_FsMIMstCistPortTxMstBpduCount_Object=MibTableColumn
fsMIMstCistPortTxMstBpduCount=_FsMIMstCistPortTxMstBpduCount_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,19),_FsMIMstCistPortTxMstBpduCount_Type())
fsMIMstCistPortTxMstBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortTxMstBpduCount.setStatus(_A)
_FsMIMstCistPortTxRstBpduCount_Type=Counter32
_FsMIMstCistPortTxRstBpduCount_Object=MibTableColumn
fsMIMstCistPortTxRstBpduCount=_FsMIMstCistPortTxRstBpduCount_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,20),_FsMIMstCistPortTxRstBpduCount_Type())
fsMIMstCistPortTxRstBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortTxRstBpduCount.setStatus(_A)
_FsMIMstCistPortTxConfigBpduCount_Type=Counter32
_FsMIMstCistPortTxConfigBpduCount_Object=MibTableColumn
fsMIMstCistPortTxConfigBpduCount=_FsMIMstCistPortTxConfigBpduCount_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,21),_FsMIMstCistPortTxConfigBpduCount_Type())
fsMIMstCistPortTxConfigBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortTxConfigBpduCount.setStatus(_A)
_FsMIMstCistPortTxTcnBpduCount_Type=Counter32
_FsMIMstCistPortTxTcnBpduCount_Object=MibTableColumn
fsMIMstCistPortTxTcnBpduCount=_FsMIMstCistPortTxTcnBpduCount_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,22),_FsMIMstCistPortTxTcnBpduCount_Type())
fsMIMstCistPortTxTcnBpduCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortTxTcnBpduCount.setStatus(_A)
_FsMIMstCistPortInvalidMstBpduRxCount_Type=Counter32
_FsMIMstCistPortInvalidMstBpduRxCount_Object=MibTableColumn
fsMIMstCistPortInvalidMstBpduRxCount=_FsMIMstCistPortInvalidMstBpduRxCount_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,23),_FsMIMstCistPortInvalidMstBpduRxCount_Type())
fsMIMstCistPortInvalidMstBpduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortInvalidMstBpduRxCount.setStatus(_A)
_FsMIMstCistPortInvalidRstBpduRxCount_Type=Counter32
_FsMIMstCistPortInvalidRstBpduRxCount_Object=MibTableColumn
fsMIMstCistPortInvalidRstBpduRxCount=_FsMIMstCistPortInvalidRstBpduRxCount_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,24),_FsMIMstCistPortInvalidRstBpduRxCount_Type())
fsMIMstCistPortInvalidRstBpduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortInvalidRstBpduRxCount.setStatus(_A)
_FsMIMstCistPortInvalidConfigBpduRxCount_Type=Counter32
_FsMIMstCistPortInvalidConfigBpduRxCount_Object=MibTableColumn
fsMIMstCistPortInvalidConfigBpduRxCount=_FsMIMstCistPortInvalidConfigBpduRxCount_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,25),_FsMIMstCistPortInvalidConfigBpduRxCount_Type())
fsMIMstCistPortInvalidConfigBpduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortInvalidConfigBpduRxCount.setStatus(_A)
_FsMIMstCistPortInvalidTcnBpduRxCount_Type=Counter32
_FsMIMstCistPortInvalidTcnBpduRxCount_Object=MibTableColumn
fsMIMstCistPortInvalidTcnBpduRxCount=_FsMIMstCistPortInvalidTcnBpduRxCount_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,26),_FsMIMstCistPortInvalidTcnBpduRxCount_Type())
fsMIMstCistPortInvalidTcnBpduRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortInvalidTcnBpduRxCount.setStatus(_A)
class _FsMIMstCistPortTransmitSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('transmitinit',0),('transmitperiodic',1),('transmitconfig',2),('transmittcn',3),('transmitrstp',4),('idle',5)))
_FsMIMstCistPortTransmitSemState_Type.__name__=_C
_FsMIMstCistPortTransmitSemState_Object=MibTableColumn
fsMIMstCistPortTransmitSemState=_FsMIMstCistPortTransmitSemState_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,27),_FsMIMstCistPortTransmitSemState_Type())
fsMIMstCistPortTransmitSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortTransmitSemState.setStatus(_A)
class _FsMIMstCistPortReceiveSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('discard',0),(_Z,1)))
_FsMIMstCistPortReceiveSemState_Type.__name__=_C
_FsMIMstCistPortReceiveSemState_Object=MibTableColumn
fsMIMstCistPortReceiveSemState=_FsMIMstCistPortReceiveSemState_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,28),_FsMIMstCistPortReceiveSemState_Type())
fsMIMstCistPortReceiveSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortReceiveSemState.setStatus(_A)
class _FsMIMstCistPortProtMigrationSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_a,0),(_n,1),('sendingrstp',2),(_o,3),('sendingstp',4)))
_FsMIMstCistPortProtMigrationSemState_Type.__name__=_C
_FsMIMstCistPortProtMigrationSemState_Object=MibTableColumn
fsMIMstCistPortProtMigrationSemState=_FsMIMstCistPortProtMigrationSemState_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,29),_FsMIMstCistPortProtMigrationSemState_Type())
fsMIMstCistPortProtMigrationSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortProtMigrationSemState.setStatus(_A)
_FsMIMstCistProtocolMigrationCount_Type=Counter32
_FsMIMstCistProtocolMigrationCount_Object=MibTableColumn
fsMIMstCistProtocolMigrationCount=_FsMIMstCistProtocolMigrationCount_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,30),_FsMIMstCistProtocolMigrationCount_Type())
fsMIMstCistProtocolMigrationCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistProtocolMigrationCount.setStatus(_A)
_FsMIMstCistPortDesignatedCost_Type=Integer32
_FsMIMstCistPortDesignatedCost_Object=MibTableColumn
fsMIMstCistPortDesignatedCost=_FsMIMstCistPortDesignatedCost_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,31),_FsMIMstCistPortDesignatedCost_Type())
fsMIMstCistPortDesignatedCost.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortDesignatedCost.setStatus(_A)
_FsMIMstCistPortRegionalRoot_Type=BridgeId
_FsMIMstCistPortRegionalRoot_Object=MibTableColumn
fsMIMstCistPortRegionalRoot=_FsMIMstCistPortRegionalRoot_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,32),_FsMIMstCistPortRegionalRoot_Type())
fsMIMstCistPortRegionalRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortRegionalRoot.setStatus(_A)
_FsMIMstCistPortRegionalPathCost_Type=Integer32
_FsMIMstCistPortRegionalPathCost_Object=MibTableColumn
fsMIMstCistPortRegionalPathCost=_FsMIMstCistPortRegionalPathCost_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,33),_FsMIMstCistPortRegionalPathCost_Type())
fsMIMstCistPortRegionalPathCost.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortRegionalPathCost.setStatus(_A)
class _FsMIMstCistSelectedPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_G,0),(_R,1),(_S,2),(_T,3),(_U,4)))
_FsMIMstCistSelectedPortRole_Type.__name__=_C
_FsMIMstCistSelectedPortRole_Object=MibTableColumn
fsMIMstCistSelectedPortRole=_FsMIMstCistSelectedPortRole_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,34),_FsMIMstCistSelectedPortRole_Type())
fsMIMstCistSelectedPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistSelectedPortRole.setStatus(_A)
class _FsMIMstCistCurrentPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_G,0),(_R,1),(_S,2),(_T,3),(_U,4)))
_FsMIMstCistCurrentPortRole_Type.__name__=_C
_FsMIMstCistCurrentPortRole_Object=MibTableColumn
fsMIMstCistCurrentPortRole=_FsMIMstCistCurrentPortRole_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,35),_FsMIMstCistCurrentPortRole_Type())
fsMIMstCistCurrentPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistCurrentPortRole.setStatus(_A)
class _FsMIMstCistPortInfoSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_G,0),('aged',1),(_p,2),(_q,3),(_r,4),(_s,5),(_t,6),(_u,7),(_Z,8),('other',9)))
_FsMIMstCistPortInfoSemState_Type.__name__=_C
_FsMIMstCistPortInfoSemState_Object=MibTableColumn
fsMIMstCistPortInfoSemState=_FsMIMstCistPortInfoSemState_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,36),_FsMIMstCistPortInfoSemState_Type())
fsMIMstCistPortInfoSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortInfoSemState.setStatus(_A)
class _FsMIMstCistPortRoleTransitionSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_a,0),(_v,1),(_w,2),(_x,3),(_y,4),(_z,5),(_V,6)))
_FsMIMstCistPortRoleTransitionSemState_Type.__name__=_C
_FsMIMstCistPortRoleTransitionSemState_Object=MibTableColumn
fsMIMstCistPortRoleTransitionSemState=_FsMIMstCistPortRoleTransitionSemState_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,37),_FsMIMstCistPortRoleTransitionSemState_Type())
fsMIMstCistPortRoleTransitionSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortRoleTransitionSemState.setStatus(_A)
class _FsMIMstCistPortStateTransitionSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_P,0),(_N,1),(_Q,2)))
_FsMIMstCistPortStateTransitionSemState_Type.__name__=_C
_FsMIMstCistPortStateTransitionSemState_Object=MibTableColumn
fsMIMstCistPortStateTransitionSemState=_FsMIMstCistPortStateTransitionSemState_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,38),_FsMIMstCistPortStateTransitionSemState_Type())
fsMIMstCistPortStateTransitionSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortStateTransitionSemState.setStatus(_A)
class _FsMIMstCistPortTopologyChangeSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('inactive',0),(_N,1),('detected',2),('active',3),(_A0,4),(_A1,5),(_A2,6),(_A3,7)))
_FsMIMstCistPortTopologyChangeSemState_Type.__name__=_C
_FsMIMstCistPortTopologyChangeSemState_Object=MibTableColumn
fsMIMstCistPortTopologyChangeSemState=_FsMIMstCistPortTopologyChangeSemState_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,39),_FsMIMstCistPortTopologyChangeSemState_Type())
fsMIMstCistPortTopologyChangeSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortTopologyChangeSemState.setStatus(_A)
class _FsMIMstCistPortHelloTime_Type(Timeout):subtypeSpec=Timeout.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,100),ValueRangeConstraint(200,200))
_FsMIMstCistPortHelloTime_Type.__name__=_M
_FsMIMstCistPortHelloTime_Object=MibTableColumn
fsMIMstCistPortHelloTime=_FsMIMstCistPortHelloTime_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,40),_FsMIMstCistPortHelloTime_Type())
fsMIMstCistPortHelloTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstCistPortHelloTime.setStatus(_A)
if mibBuilder.loadTexts:fsMIMstCistPortHelloTime.setUnits(_H)
class _FsMIMstCistPortOperVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3)));namedValues=NamedValues(*((_e,0),('rstp',2),('mstp',3)))
_FsMIMstCistPortOperVersion_Type.__name__=_C
_FsMIMstCistPortOperVersion_Object=MibTableColumn
fsMIMstCistPortOperVersion=_FsMIMstCistPortOperVersion_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,41),_FsMIMstCistPortOperVersion_Type())
fsMIMstCistPortOperVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortOperVersion.setStatus(_A)
_FsMIMstCistPortEffectivePortState_Type=TruthValue
_FsMIMstCistPortEffectivePortState_Object=MibTableColumn
fsMIMstCistPortEffectivePortState=_FsMIMstCistPortEffectivePortState_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,42),_FsMIMstCistPortEffectivePortState_Type())
fsMIMstCistPortEffectivePortState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortEffectivePortState.setStatus(_A)
_FsMIMstCistPortAutoEdgeStatus_Type=TruthValue
_FsMIMstCistPortAutoEdgeStatus_Object=MibTableColumn
fsMIMstCistPortAutoEdgeStatus=_FsMIMstCistPortAutoEdgeStatus_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,43),_FsMIMstCistPortAutoEdgeStatus_Type())
fsMIMstCistPortAutoEdgeStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstCistPortAutoEdgeStatus.setStatus(_A)
_FsMIMstCistPortRestrictedRole_Type=TruthValue
_FsMIMstCistPortRestrictedRole_Object=MibTableColumn
fsMIMstCistPortRestrictedRole=_FsMIMstCistPortRestrictedRole_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,44),_FsMIMstCistPortRestrictedRole_Type())
fsMIMstCistPortRestrictedRole.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstCistPortRestrictedRole.setStatus(_A)
_FsMIMstCistPortRestrictedTCN_Type=TruthValue
_FsMIMstCistPortRestrictedTCN_Object=MibTableColumn
fsMIMstCistPortRestrictedTCN=_FsMIMstCistPortRestrictedTCN_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,45),_FsMIMstCistPortRestrictedTCN_Type())
fsMIMstCistPortRestrictedTCN.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstCistPortRestrictedTCN.setStatus(_A)
class _FsMIMstCistPortAdminPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_FsMIMstCistPortAdminPathCost_Type.__name__=_C
_FsMIMstCistPortAdminPathCost_Object=MibTableColumn
fsMIMstCistPortAdminPathCost=_FsMIMstCistPortAdminPathCost_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,46),_FsMIMstCistPortAdminPathCost_Type())
fsMIMstCistPortAdminPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstCistPortAdminPathCost.setStatus(_A)
class _FsMIMstCistPortEnableBPDURx_Type(TruthValue):defaultValue=1
_FsMIMstCistPortEnableBPDURx_Type.__name__=_K
_FsMIMstCistPortEnableBPDURx_Object=MibTableColumn
fsMIMstCistPortEnableBPDURx=_FsMIMstCistPortEnableBPDURx_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,47),_FsMIMstCistPortEnableBPDURx_Type())
fsMIMstCistPortEnableBPDURx.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstCistPortEnableBPDURx.setStatus(_A)
class _FsMIMstCistPortEnableBPDUTx_Type(TruthValue):defaultValue=1
_FsMIMstCistPortEnableBPDUTx_Type.__name__=_K
_FsMIMstCistPortEnableBPDUTx_Object=MibTableColumn
fsMIMstCistPortEnableBPDUTx=_FsMIMstCistPortEnableBPDUTx_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,48),_FsMIMstCistPortEnableBPDUTx_Type())
fsMIMstCistPortEnableBPDUTx.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstCistPortEnableBPDUTx.setStatus(_A)
_FsMIMstCistPortPseudoRootId_Type=BridgeId
_FsMIMstCistPortPseudoRootId_Object=MibTableColumn
fsMIMstCistPortPseudoRootId=_FsMIMstCistPortPseudoRootId_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,49),_FsMIMstCistPortPseudoRootId_Type())
fsMIMstCistPortPseudoRootId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstCistPortPseudoRootId.setStatus(_A)
class _FsMIMstCistPortIsL2Gp_Type(TruthValue):defaultValue=2
_FsMIMstCistPortIsL2Gp_Type.__name__=_K
_FsMIMstCistPortIsL2Gp_Object=MibTableColumn
fsMIMstCistPortIsL2Gp=_FsMIMstCistPortIsL2Gp_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,50),_FsMIMstCistPortIsL2Gp_Type())
fsMIMstCistPortIsL2Gp.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstCistPortIsL2Gp.setStatus(_A)
class _FsMIMstCistPortLoopGuard_Type(TruthValue):defaultValue=2
_FsMIMstCistPortLoopGuard_Type.__name__=_K
_FsMIMstCistPortLoopGuard_Object=MibTableColumn
fsMIMstCistPortLoopGuard=_FsMIMstCistPortLoopGuard_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,51),_FsMIMstCistPortLoopGuard_Type())
fsMIMstCistPortLoopGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstCistPortLoopGuard.setStatus(_A)
_FsMIMstCistPortClearStats_Type=TruthValue
_FsMIMstCistPortClearStats_Object=MibTableColumn
fsMIMstCistPortClearStats=_FsMIMstCistPortClearStats_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,52),_FsMIMstCistPortClearStats_Type())
fsMIMstCistPortClearStats.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstCistPortClearStats.setStatus(_A)
class _FsMIMstCistPortRcvdEvent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_h,1),(_i,2),(_j,3)))
_FsMIMstCistPortRcvdEvent_Type.__name__=_C
_FsMIMstCistPortRcvdEvent_Object=MibTableColumn
fsMIMstCistPortRcvdEvent=_FsMIMstCistPortRcvdEvent_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,53),_FsMIMstCistPortRcvdEvent_Type())
fsMIMstCistPortRcvdEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortRcvdEvent.setStatus(_A)
_FsMIMstCistPortRcvdEventSubType_Type=Integer32
_FsMIMstCistPortRcvdEventSubType_Object=MibTableColumn
fsMIMstCistPortRcvdEventSubType=_FsMIMstCistPortRcvdEventSubType_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,54),_FsMIMstCistPortRcvdEventSubType_Type())
fsMIMstCistPortRcvdEventSubType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortRcvdEventSubType.setStatus(_A)
_FsMIMstCistPortRcvdEventTimeStamp_Type=Unsigned32
_FsMIMstCistPortRcvdEventTimeStamp_Object=MibTableColumn
fsMIMstCistPortRcvdEventTimeStamp=_FsMIMstCistPortRcvdEventTimeStamp_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,55),_FsMIMstCistPortRcvdEventTimeStamp_Type())
fsMIMstCistPortRcvdEventTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistPortRcvdEventTimeStamp.setStatus(_A)
class _FsMIMstCistLoopInconsistentState_Type(TruthValue):defaultValue=2
_FsMIMstCistLoopInconsistentState_Type.__name__=_K
_FsMIMstCistLoopInconsistentState_Object=MibTableColumn
fsMIMstCistLoopInconsistentState=_FsMIMstCistLoopInconsistentState_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,56),_FsMIMstCistLoopInconsistentState_Type())
fsMIMstCistLoopInconsistentState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstCistLoopInconsistentState.setStatus(_A)
class _FsMIMstCistPortBpduGuard_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_b,0),(_k,1),(_l,2)))
_FsMIMstCistPortBpduGuard_Type.__name__=_C
_FsMIMstCistPortBpduGuard_Object=MibTableColumn
fsMIMstCistPortBpduGuard=_FsMIMstCistPortBpduGuard_Object((1,3,6,1,4,1,10876,101,1,118,1,6,1,57),_FsMIMstCistPortBpduGuard_Type())
fsMIMstCistPortBpduGuard.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstCistPortBpduGuard.setStatus(_A)
_FsMIMstMstiPortTable_Object=MibTable
fsMIMstMstiPortTable=_FsMIMstMstiPortTable_Object((1,3,6,1,4,1,10876,101,1,118,1,7))
if mibBuilder.loadTexts:fsMIMstMstiPortTable.setStatus(_A)
_FsMIMstMstiPortEntry_Object=MibTableRow
fsMIMstMstiPortEntry=_FsMIMstMstiPortEntry_Object((1,3,6,1,4,1,10876,101,1,118,1,7,1))
fsMIMstMstiPortEntry.setIndexNames((0,_E,_A4),(0,_E,_Y))
if mibBuilder.loadTexts:fsMIMstMstiPortEntry.setStatus(_A)
class _FsMIMstMstiPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsMIMstMstiPort_Type.__name__=_C
_FsMIMstMstiPort_Object=MibTableColumn
fsMIMstMstiPort=_FsMIMstMstiPort_Object((1,3,6,1,4,1,10876,101,1,118,1,7,1,1),_FsMIMstMstiPort_Type())
fsMIMstMstiPort.setMaxAccess(_L)
if mibBuilder.loadTexts:fsMIMstMstiPort.setStatus(_A)
class _FsMIMstMstiPortPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,200000000))
_FsMIMstMstiPortPathCost_Type.__name__=_C
_FsMIMstMstiPortPathCost_Object=MibTableColumn
fsMIMstMstiPortPathCost=_FsMIMstMstiPortPathCost_Object((1,3,6,1,4,1,10876,101,1,118,1,7,1,2),_FsMIMstMstiPortPathCost_Type())
fsMIMstMstiPortPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstMstiPortPathCost.setStatus(_A)
class _FsMIMstMstiPortPriority_Type(Integer32):defaultValue=128;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,240))
_FsMIMstMstiPortPriority_Type.__name__=_C
_FsMIMstMstiPortPriority_Object=MibTableColumn
fsMIMstMstiPortPriority=_FsMIMstMstiPortPriority_Object((1,3,6,1,4,1,10876,101,1,118,1,7,1,3),_FsMIMstMstiPortPriority_Type())
fsMIMstMstiPortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstMstiPortPriority.setStatus(_A)
_FsMIMstMstiPortDesignatedRoot_Type=BridgeId
_FsMIMstMstiPortDesignatedRoot_Object=MibTableColumn
fsMIMstMstiPortDesignatedRoot=_FsMIMstMstiPortDesignatedRoot_Object((1,3,6,1,4,1,10876,101,1,118,1,7,1,4),_FsMIMstMstiPortDesignatedRoot_Type())
fsMIMstMstiPortDesignatedRoot.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiPortDesignatedRoot.setStatus(_A)
_FsMIMstMstiPortDesignatedBridge_Type=BridgeId
_FsMIMstMstiPortDesignatedBridge_Object=MibTableColumn
fsMIMstMstiPortDesignatedBridge=_FsMIMstMstiPortDesignatedBridge_Object((1,3,6,1,4,1,10876,101,1,118,1,7,1,5),_FsMIMstMstiPortDesignatedBridge_Type())
fsMIMstMstiPortDesignatedBridge.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiPortDesignatedBridge.setStatus(_A)
class _FsMIMstMstiPortDesignatedPort_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_FsMIMstMstiPortDesignatedPort_Type.__name__=_F
_FsMIMstMstiPortDesignatedPort_Object=MibTableColumn
fsMIMstMstiPortDesignatedPort=_FsMIMstMstiPortDesignatedPort_Object((1,3,6,1,4,1,10876,101,1,118,1,7,1,6),_FsMIMstMstiPortDesignatedPort_Type())
fsMIMstMstiPortDesignatedPort.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiPortDesignatedPort.setStatus(_A)
class _FsMIMstMstiPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5)));namedValues=NamedValues(*((_G,1),(_P,2),(_N,4),(_Q,5)))
_FsMIMstMstiPortState_Type.__name__=_C
_FsMIMstMstiPortState_Object=MibTableColumn
fsMIMstMstiPortState=_FsMIMstMstiPortState_Object((1,3,6,1,4,1,10876,101,1,118,1,7,1,7),_FsMIMstMstiPortState_Type())
fsMIMstMstiPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiPortState.setStatus(_A)
class _FsMIMstMstiForcePortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_W,1)))
_FsMIMstMstiForcePortState_Type.__name__=_C
_FsMIMstMstiForcePortState_Object=MibTableColumn
fsMIMstMstiForcePortState=_FsMIMstMstiForcePortState_Object((1,3,6,1,4,1,10876,101,1,118,1,7,1,8),_FsMIMstMstiForcePortState_Type())
fsMIMstMstiForcePortState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstMstiForcePortState.setStatus(_A)
_FsMIMstMstiPortForwardTransitions_Type=Counter32
_FsMIMstMstiPortForwardTransitions_Object=MibTableColumn
fsMIMstMstiPortForwardTransitions=_FsMIMstMstiPortForwardTransitions_Object((1,3,6,1,4,1,10876,101,1,118,1,7,1,9),_FsMIMstMstiPortForwardTransitions_Type())
fsMIMstMstiPortForwardTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiPortForwardTransitions.setStatus(_A)
_FsMIMstMstiPortReceivedBPDUs_Type=Counter32
_FsMIMstMstiPortReceivedBPDUs_Object=MibTableColumn
fsMIMstMstiPortReceivedBPDUs=_FsMIMstMstiPortReceivedBPDUs_Object((1,3,6,1,4,1,10876,101,1,118,1,7,1,10),_FsMIMstMstiPortReceivedBPDUs_Type())
fsMIMstMstiPortReceivedBPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiPortReceivedBPDUs.setStatus(_A)
_FsMIMstMstiPortTransmittedBPDUs_Type=Counter32
_FsMIMstMstiPortTransmittedBPDUs_Object=MibTableColumn
fsMIMstMstiPortTransmittedBPDUs=_FsMIMstMstiPortTransmittedBPDUs_Object((1,3,6,1,4,1,10876,101,1,118,1,7,1,11),_FsMIMstMstiPortTransmittedBPDUs_Type())
fsMIMstMstiPortTransmittedBPDUs.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiPortTransmittedBPDUs.setStatus(_A)
_FsMIMstMstiPortInvalidBPDUsRcvd_Type=Counter32
_FsMIMstMstiPortInvalidBPDUsRcvd_Object=MibTableColumn
fsMIMstMstiPortInvalidBPDUsRcvd=_FsMIMstMstiPortInvalidBPDUsRcvd_Object((1,3,6,1,4,1,10876,101,1,118,1,7,1,12),_FsMIMstMstiPortInvalidBPDUsRcvd_Type())
fsMIMstMstiPortInvalidBPDUsRcvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiPortInvalidBPDUsRcvd.setStatus(_A)
_FsMIMstMstiPortDesignatedCost_Type=Integer32
_FsMIMstMstiPortDesignatedCost_Object=MibTableColumn
fsMIMstMstiPortDesignatedCost=_FsMIMstMstiPortDesignatedCost_Object((1,3,6,1,4,1,10876,101,1,118,1,7,1,13),_FsMIMstMstiPortDesignatedCost_Type())
fsMIMstMstiPortDesignatedCost.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiPortDesignatedCost.setStatus(_A)
class _FsMIMstMstiSelectedPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_G,0),(_R,1),(_S,2),(_T,3),(_U,4),('master',5)))
_FsMIMstMstiSelectedPortRole_Type.__name__=_C
_FsMIMstMstiSelectedPortRole_Object=MibTableColumn
fsMIMstMstiSelectedPortRole=_FsMIMstMstiSelectedPortRole_Object((1,3,6,1,4,1,10876,101,1,118,1,7,1,14),_FsMIMstMstiSelectedPortRole_Type())
fsMIMstMstiSelectedPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiSelectedPortRole.setStatus(_A)
class _FsMIMstMstiCurrentPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_G,0),(_R,1),(_S,2),(_T,3),(_U,4),('master',5)))
_FsMIMstMstiCurrentPortRole_Type.__name__=_C
_FsMIMstMstiCurrentPortRole_Object=MibTableColumn
fsMIMstMstiCurrentPortRole=_FsMIMstMstiCurrentPortRole_Object((1,3,6,1,4,1,10876,101,1,118,1,7,1,15),_FsMIMstMstiCurrentPortRole_Type())
fsMIMstMstiCurrentPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiCurrentPortRole.setStatus(_A)
class _FsMIMstMstiPortInfoSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_G,0),('aged',1),(_p,2),(_q,3),(_r,4),(_s,5),(_t,6),(_u,7),(_Z,8),('other',9)))
_FsMIMstMstiPortInfoSemState_Type.__name__=_C
_FsMIMstMstiPortInfoSemState_Object=MibTableColumn
fsMIMstMstiPortInfoSemState=_FsMIMstMstiPortInfoSemState_Object((1,3,6,1,4,1,10876,101,1,118,1,7,1,16),_FsMIMstMstiPortInfoSemState_Type())
fsMIMstMstiPortInfoSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiPortInfoSemState.setStatus(_A)
class _FsMIMstMstiPortRoleTransitionSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_a,0),(_v,1),(_w,2),(_x,3),(_y,4),(_z,5),(_V,6)))
_FsMIMstMstiPortRoleTransitionSemState_Type.__name__=_C
_FsMIMstMstiPortRoleTransitionSemState_Object=MibTableColumn
fsMIMstMstiPortRoleTransitionSemState=_FsMIMstMstiPortRoleTransitionSemState_Object((1,3,6,1,4,1,10876,101,1,118,1,7,1,17),_FsMIMstMstiPortRoleTransitionSemState_Type())
fsMIMstMstiPortRoleTransitionSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiPortRoleTransitionSemState.setStatus(_A)
class _FsMIMstMstiPortStateTransitionSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_P,0),(_N,1),(_Q,2)))
_FsMIMstMstiPortStateTransitionSemState_Type.__name__=_C
_FsMIMstMstiPortStateTransitionSemState_Object=MibTableColumn
fsMIMstMstiPortStateTransitionSemState=_FsMIMstMstiPortStateTransitionSemState_Object((1,3,6,1,4,1,10876,101,1,118,1,7,1,18),_FsMIMstMstiPortStateTransitionSemState_Type())
fsMIMstMstiPortStateTransitionSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiPortStateTransitionSemState.setStatus(_A)
class _FsMIMstMstiPortTopologyChangeSemState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('inactive',0),(_N,1),('detected',2),('active',3),(_A0,4),(_A1,5),(_A2,6),(_A3,7)))
_FsMIMstMstiPortTopologyChangeSemState_Type.__name__=_C
_FsMIMstMstiPortTopologyChangeSemState_Object=MibTableColumn
fsMIMstMstiPortTopologyChangeSemState=_FsMIMstMstiPortTopologyChangeSemState_Object((1,3,6,1,4,1,10876,101,1,118,1,7,1,19),_FsMIMstMstiPortTopologyChangeSemState_Type())
fsMIMstMstiPortTopologyChangeSemState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiPortTopologyChangeSemState.setStatus(_A)
_FsMIMstMstiPortEffectivePortState_Type=TruthValue
_FsMIMstMstiPortEffectivePortState_Object=MibTableColumn
fsMIMstMstiPortEffectivePortState=_FsMIMstMstiPortEffectivePortState_Object((1,3,6,1,4,1,10876,101,1,118,1,7,1,20),_FsMIMstMstiPortEffectivePortState_Type())
fsMIMstMstiPortEffectivePortState.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiPortEffectivePortState.setStatus(_A)
class _FsMIMstMstiPortAdminPathCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,200000000))
_FsMIMstMstiPortAdminPathCost_Type.__name__=_C
_FsMIMstMstiPortAdminPathCost_Object=MibTableColumn
fsMIMstMstiPortAdminPathCost=_FsMIMstMstiPortAdminPathCost_Object((1,3,6,1,4,1,10876,101,1,118,1,7,1,21),_FsMIMstMstiPortAdminPathCost_Type())
fsMIMstMstiPortAdminPathCost.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstMstiPortAdminPathCost.setStatus(_A)
_FsMIMstMstiPortPseudoRootId_Type=BridgeId
_FsMIMstMstiPortPseudoRootId_Object=MibTableColumn
fsMIMstMstiPortPseudoRootId=_FsMIMstMstiPortPseudoRootId_Object((1,3,6,1,4,1,10876,101,1,118,1,7,1,22),_FsMIMstMstiPortPseudoRootId_Type())
fsMIMstMstiPortPseudoRootId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstMstiPortPseudoRootId.setStatus(_A)
_FsMIMstMstiPortClearStats_Type=TruthValue
_FsMIMstMstiPortClearStats_Object=MibTableColumn
fsMIMstMstiPortClearStats=_FsMIMstMstiPortClearStats_Object((1,3,6,1,4,1,10876,101,1,118,1,7,1,23),_FsMIMstMstiPortClearStats_Type())
fsMIMstMstiPortClearStats.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstMstiPortClearStats.setStatus(_A)
_FsMIMstMstiPortStateChangeTimeStamp_Type=Unsigned32
_FsMIMstMstiPortStateChangeTimeStamp_Object=MibTableColumn
fsMIMstMstiPortStateChangeTimeStamp=_FsMIMstMstiPortStateChangeTimeStamp_Object((1,3,6,1,4,1,10876,101,1,118,1,7,1,24),_FsMIMstMstiPortStateChangeTimeStamp_Type())
fsMIMstMstiPortStateChangeTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstMstiPortStateChangeTimeStamp.setStatus(_A)
_FsMIMstPortExtTable_Object=MibTable
fsMIMstPortExtTable=_FsMIMstPortExtTable_Object((1,3,6,1,4,1,10876,101,1,118,1,8))
if mibBuilder.loadTexts:fsMIMstPortExtTable.setStatus(_A)
_FsMIMstPortExtEntry_Object=MibTableRow
fsMIMstPortExtEntry=_FsMIMstPortExtEntry_Object((1,3,6,1,4,1,10876,101,1,118,1,8,1))
fsMIMstPortExtEntry.setIndexNames((0,_E,_A5))
if mibBuilder.loadTexts:fsMIMstPortExtEntry.setStatus(_A)
class _FsMIMstPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_FsMIMstPort_Type.__name__=_C
_FsMIMstPort_Object=MibTableColumn
fsMIMstPort=_FsMIMstPort_Object((1,3,6,1,4,1,10876,101,1,118,1,8,1,1),_FsMIMstPort_Type())
fsMIMstPort.setMaxAccess(_L)
if mibBuilder.loadTexts:fsMIMstPort.setStatus(_A)
_FsMIMstPortRowStatus_Type=RowStatus
_FsMIMstPortRowStatus_Object=MibTableColumn
fsMIMstPortRowStatus=_FsMIMstPortRowStatus_Object((1,3,6,1,4,1,10876,101,1,118,1,8,1,2),_FsMIMstPortRowStatus_Type())
fsMIMstPortRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:fsMIMstPortRowStatus.setStatus(_A)
_FsMIDot1sFsMstTrapsControl_ObjectIdentity=ObjectIdentity
fsMIDot1sFsMstTrapsControl=_FsMIDot1sFsMstTrapsControl_ObjectIdentity((1,3,6,1,4,1,10876,101,1,118,2))
class _FsMIDot1sFsMstSetGlobalTrapOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1))
_FsMIDot1sFsMstSetGlobalTrapOption_Type.__name__=_C
_FsMIDot1sFsMstSetGlobalTrapOption_Object=MibScalar
fsMIDot1sFsMstSetGlobalTrapOption=_FsMIDot1sFsMstSetGlobalTrapOption_Object((1,3,6,1,4,1,10876,101,1,118,2,1),_FsMIDot1sFsMstSetGlobalTrapOption_Type())
fsMIDot1sFsMstSetGlobalTrapOption.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIDot1sFsMstSetGlobalTrapOption.setStatus(_A)
class _FsMIMstGlobalErrTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_b,0),('memfail',1),('bufffail',2)))
_FsMIMstGlobalErrTrapType_Type.__name__=_C
_FsMIMstGlobalErrTrapType_Object=MibScalar
fsMIMstGlobalErrTrapType=_FsMIMstGlobalErrTrapType_Object((1,3,6,1,4,1,10876,101,1,118,2,2),_FsMIMstGlobalErrTrapType_Type())
fsMIMstGlobalErrTrapType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstGlobalErrTrapType.setStatus(_A)
_FsMIDot1sFsMstTrapsControlTable_Object=MibTable
fsMIDot1sFsMstTrapsControlTable=_FsMIDot1sFsMstTrapsControlTable_Object((1,3,6,1,4,1,10876,101,1,118,2,3))
if mibBuilder.loadTexts:fsMIDot1sFsMstTrapsControlTable.setStatus(_A)
_FsMIDot1sFsMstTrapsControlEntry_Object=MibTableRow
fsMIDot1sFsMstTrapsControlEntry=_FsMIDot1sFsMstTrapsControlEntry_Object((1,3,6,1,4,1,10876,101,1,118,2,3,1))
fsMIDot1sFsMstTrapsControlEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:fsMIDot1sFsMstTrapsControlEntry.setStatus(_A)
class _FsMIMstSetTraps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_FsMIMstSetTraps_Type.__name__=_C
_FsMIMstSetTraps_Object=MibTableColumn
fsMIMstSetTraps=_FsMIMstSetTraps_Object((1,3,6,1,4,1,10876,101,1,118,2,3,1,1),_FsMIMstSetTraps_Type())
fsMIMstSetTraps.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIMstSetTraps.setStatus(_A)
class _FsMIMstGenTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_b,0),('up',1),('down',2)))
_FsMIMstGenTrapType_Type.__name__=_C
_FsMIMstGenTrapType_Object=MibTableColumn
fsMIMstGenTrapType=_FsMIMstGenTrapType_Object((1,3,6,1,4,1,10876,101,1,118,2,3,1,2),_FsMIMstGenTrapType_Type())
fsMIMstGenTrapType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstGenTrapType.setStatus(_A)
_FsMIMstPortTrapNotificationTable_Object=MibTable
fsMIMstPortTrapNotificationTable=_FsMIMstPortTrapNotificationTable_Object((1,3,6,1,4,1,10876,101,1,118,2,4))
if mibBuilder.loadTexts:fsMIMstPortTrapNotificationTable.setStatus(_A)
_FsMIMstPortTrapNotificationEntry_Object=MibTableRow
fsMIMstPortTrapNotificationEntry=_FsMIMstPortTrapNotificationEntry_Object((1,3,6,1,4,1,10876,101,1,118,2,4,1))
fsMIMstPortTrapNotificationEntry.setIndexNames((0,_E,_c))
if mibBuilder.loadTexts:fsMIMstPortTrapNotificationEntry.setStatus(_A)
class _FsMIMstPortTrapIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_FsMIMstPortTrapIndex_Type.__name__=_C
_FsMIMstPortTrapIndex_Object=MibTableColumn
fsMIMstPortTrapIndex=_FsMIMstPortTrapIndex_Object((1,3,6,1,4,1,10876,101,1,118,2,4,1,1),_FsMIMstPortTrapIndex_Type())
fsMIMstPortTrapIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:fsMIMstPortTrapIndex.setStatus(_A)
class _FsMIMstPortMigrationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_o,0),(_n,1)))
_FsMIMstPortMigrationType_Type.__name__=_C
_FsMIMstPortMigrationType_Object=MibTableColumn
fsMIMstPortMigrationType=_FsMIMstPortMigrationType_Object((1,3,6,1,4,1,10876,101,1,118,2,4,1,2),_FsMIMstPortMigrationType_Type())
fsMIMstPortMigrationType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstPortMigrationType.setStatus(_A)
class _FsMIMstPktErrType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('protocolIdErr',0),('invalidBpdu',1),('configLengthErr',2),('tcnLengthErr',3),('rstpLengthErr',4),('maxAgeErr',5),('fwdDelayErr',6),('helloTimeErr',7),('mstpLengthErr',8)))
_FsMIMstPktErrType_Type.__name__=_C
_FsMIMstPktErrType_Object=MibTableColumn
fsMIMstPktErrType=_FsMIMstPktErrType_Object((1,3,6,1,4,1,10876,101,1,118,2,4,1,3),_FsMIMstPktErrType_Type())
fsMIMstPktErrType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstPktErrType.setStatus(_A)
_FsMIMstPktErrVal_Type=Integer32
_FsMIMstPktErrVal_Object=MibTableColumn
fsMIMstPktErrVal=_FsMIMstPktErrVal_Object((1,3,6,1,4,1,10876,101,1,118,2,4,1,4),_FsMIMstPktErrVal_Type())
fsMIMstPktErrVal.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstPktErrVal.setStatus(_A)
_FsMIMstPortRoleTrapNotificationTable_Object=MibTable
fsMIMstPortRoleTrapNotificationTable=_FsMIMstPortRoleTrapNotificationTable_Object((1,3,6,1,4,1,10876,101,1,118,2,5))
if mibBuilder.loadTexts:fsMIMstPortRoleTrapNotificationTable.setStatus(_A)
_FsMIMstPortRoleTrapNotificationEntry_Object=MibTableRow
fsMIMstPortRoleTrapNotificationEntry=_FsMIMstPortRoleTrapNotificationEntry_Object((1,3,6,1,4,1,10876,101,1,118,2,5,1))
fsMIMstPortRoleTrapNotificationEntry.setIndexNames((0,_E,_c),(0,_E,_X))
if mibBuilder.loadTexts:fsMIMstPortRoleTrapNotificationEntry.setStatus(_A)
class _FsMIMstPortRoleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_A6,0),(_A7,1),(_A8,2),('rootPort',3),(_A9,4),(_V,5)))
_FsMIMstPortRoleType_Type.__name__=_C
_FsMIMstPortRoleType_Object=MibTableColumn
fsMIMstPortRoleType=_FsMIMstPortRoleType_Object((1,3,6,1,4,1,10876,101,1,118,2,5,1,1),_FsMIMstPortRoleType_Type())
fsMIMstPortRoleType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstPortRoleType.setStatus(_A)
class _FsMIMstOldRoleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_A6,0),(_A7,1),(_A8,2),('rootPort',3),(_A9,4),(_V,5)))
_FsMIMstOldRoleType_Type.__name__=_C
_FsMIMstOldRoleType_Object=MibTableColumn
fsMIMstOldRoleType=_FsMIMstOldRoleType_Object((1,3,6,1,4,1,10876,101,1,118,2,5,1,2),_FsMIMstOldRoleType_Type())
fsMIMstOldRoleType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIMstOldRoleType.setStatus(_A)
_FsMIDot1sFutureMstTraps_ObjectIdentity=ObjectIdentity
fsMIDot1sFutureMstTraps=_FsMIDot1sFutureMstTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,118,3))
_FsMIMstTraps_ObjectIdentity=ObjectIdentity
fsMIMstTraps=_FsMIMstTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,118,3,0))
fsMIMstGlobalErrTrap=NotificationType((1,3,6,1,4,1,10876,101,1,118,3,0,1))
fsMIMstGlobalErrTrap.setObjects(*((_E,_I),(_E,_AA)))
if mibBuilder.loadTexts:fsMIMstGlobalErrTrap.setStatus(_A)
fsMIMstGenTrap=NotificationType((1,3,6,1,4,1,10876,101,1,118,3,0,2))
fsMIMstGenTrap.setObjects(*((_E,_I),(_E,_J),(_E,_AB)))
if mibBuilder.loadTexts:fsMIMstGenTrap.setStatus(_A)
fsMIMstNewRootTrap=NotificationType((1,3,6,1,4,1,10876,101,1,118,3,0,3))
fsMIMstNewRootTrap.setObjects(*((_E,_I),(_E,_J),(_E,_AC),(_E,_AD)))
if mibBuilder.loadTexts:fsMIMstNewRootTrap.setStatus(_A)
fsMIMstTopologyChgTrap=NotificationType((1,3,6,1,4,1,10876,101,1,118,3,0,4))
fsMIMstTopologyChgTrap.setObjects(*((_E,_I),(_E,_J),(_E,_AE)))
if mibBuilder.loadTexts:fsMIMstTopologyChgTrap.setStatus(_A)
fsMIMstProtocolMigrationTrap=NotificationType((1,3,6,1,4,1,10876,101,1,118,3,0,5))
fsMIMstProtocolMigrationTrap.setObjects(*((_E,_I),(_E,_J),(_E,_AF),(_E,_AG)))
if mibBuilder.loadTexts:fsMIMstProtocolMigrationTrap.setStatus(_A)
fsMIMstInvalidBpduRxdTrap=NotificationType((1,3,6,1,4,1,10876,101,1,118,3,0,6))
fsMIMstInvalidBpduRxdTrap.setObjects(*((_E,_I),(_E,_J),(_E,_AH),(_E,_AI)))
if mibBuilder.loadTexts:fsMIMstInvalidBpduRxdTrap.setStatus(_A)
fsMIMstRegionConfigChangeTrap=NotificationType((1,3,6,1,4,1,10876,101,1,118,3,0,7))
fsMIMstRegionConfigChangeTrap.setObjects(*((_E,_I),(_E,_J),(_E,_AJ),(_E,_AK),(_E,_AL),(_E,_AM)))
if mibBuilder.loadTexts:fsMIMstRegionConfigChangeTrap.setStatus(_A)
fsMIMstNewPortRoleTrap=NotificationType((1,3,6,1,4,1,10876,101,1,118,3,0,8))
fsMIMstNewPortRoleTrap.setObjects(*((_E,_I),(_E,_AN),(_E,_AO)))
if mibBuilder.loadTexts:fsMIMstNewPortRoleTrap.setStatus(_A)
fsMIMstCistHwFailureTrap=NotificationType((1,3,6,1,4,1,10876,101,1,118,3,0,9))
fsMIMstCistHwFailureTrap.setObjects(*((_E,_I),(_E,_J),(_E,_AP)))
if mibBuilder.loadTexts:fsMIMstCistHwFailureTrap.setStatus(_A)
fsMIMstMstiHwFailureTrap=NotificationType((1,3,6,1,4,1,10876,101,1,118,3,0,10))
fsMIMstMstiHwFailureTrap.setObjects(*((_E,_I),(_E,_J),(_E,_AQ)))
if mibBuilder.loadTexts:fsMIMstMstiHwFailureTrap.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'VlanId':VlanId,'BridgeId':BridgeId,_M:Timeout,'EnabledStatus':EnabledStatus,'futureMIMstMIB':futureMIMstMIB,'fsMIDot1sFutureMst':fsMIDot1sFutureMst,'fsMIMstGlobalTrace':fsMIMstGlobalTrace,'fsMIMstGlobalDebug':fsMIMstGlobalDebug,'fsMIDot1sFutureMstTable':fsMIDot1sFutureMstTable,'fsMIDot1sFutureMstEntry':fsMIDot1sFutureMstEntry,_O:fsMIDot1sFutureMstContextId,'fsMIMstSystemControl':fsMIMstSystemControl,'fsMIMstModuleStatus':fsMIMstModuleStatus,'fsMIMstMaxMstInstanceNumber':fsMIMstMaxMstInstanceNumber,'fsMIMstNoOfMstiSupported':fsMIMstNoOfMstiSupported,'fsMIMstMaxHopCount':fsMIMstMaxHopCount,_I:fsMIMstBrgAddress,'fsMIMstCistRoot':fsMIMstCistRoot,'fsMIMstCistRegionalRoot':fsMIMstCistRegionalRoot,'fsMIMstCistRootCost':fsMIMstCistRootCost,'fsMIMstCistRegionalRootCost':fsMIMstCistRegionalRootCost,'fsMIMstCistRootPort':fsMIMstCistRootPort,'fsMIMstCistBridgePriority':fsMIMstCistBridgePriority,'fsMIMstCistBridgeMaxAge':fsMIMstCistBridgeMaxAge,'fsMIMstCistBridgeForwardDelay':fsMIMstCistBridgeForwardDelay,'fsMIMstCistHoldTime':fsMIMstCistHoldTime,'fsMIMstCistMaxAge':fsMIMstCistMaxAge,'fsMIMstCistForwardDelay':fsMIMstCistForwardDelay,'fsMIMstMstpUpCount':fsMIMstMstpUpCount,'fsMIMstMstpDownCount':fsMIMstMstpDownCount,'fsMIMstPathCostDefaultType':fsMIMstPathCostDefaultType,'fsMIMstTrace':fsMIMstTrace,'fsMIMstDebug':fsMIMstDebug,_AF:fsMIMstForceProtocolVersion,'fsMIMstTxHoldCount':fsMIMstTxHoldCount,_AJ:fsMIMstMstiConfigIdSel,_AK:fsMIMstMstiRegionName,_AL:fsMIMstMstiRegionVersion,_AM:fsMIMstMstiConfigDigest,'fsMIMstBufferOverFlowCount':fsMIMstBufferOverFlowCount,'fsMIMstMemAllocFailureCount':fsMIMstMemAllocFailureCount,'fsMIMstRegionConfigChangeCount':fsMIMstRegionConfigChangeCount,'fsMIMstCistBridgeRoleSelectionSemState':fsMIMstCistBridgeRoleSelectionSemState,'fsMIMstCistTimeSinceTopologyChange':fsMIMstCistTimeSinceTopologyChange,'fsMIMstCistTopChanges':fsMIMstCistTopChanges,'fsMIMstCistNewRootBridgeCount':fsMIMstCistNewRootBridgeCount,'fsMIMstCistHelloTime':fsMIMstCistHelloTime,'fsMIMstCistBridgeHelloTime':fsMIMstCistBridgeHelloTime,'fsMIMstCistDynamicPathcostCalculation':fsMIMstCistDynamicPathcostCalculation,_J:fsMIMstContextName,'fsMIMstCalcPortPathCostOnSpeedChg':fsMIMstCalcPortPathCostOnSpeedChg,'fsMIMstClearBridgeStats':fsMIMstClearBridgeStats,'fsMIMstRcvdEvent':fsMIMstRcvdEvent,'fsMIMstRcvdEventSubType':fsMIMstRcvdEventSubType,'fsMIMstRcvdEventTimeStamp':fsMIMstRcvdEventTimeStamp,'fsMIMstPortStateChangeTimeStamp':fsMIMstPortStateChangeTimeStamp,'fsMIMstFlushInterval':fsMIMstFlushInterval,'fsMIMstCistFlushIndicationThreshold':fsMIMstCistFlushIndicationThreshold,'fsMIMstCistTotalFlushCount':fsMIMstCistTotalFlushCount,'fsMIMstBpduGuard':fsMIMstBpduGuard,'fsMIMstMstiBridgeTable':fsMIMstMstiBridgeTable,'fsMIMstMstiBridgeEntry':fsMIMstMstiBridgeEntry,_X:fsMIMstMstiInstanceIndex,_AD:fsMIMstMstiBridgeRegionalRoot,'fsMIMstMstiBridgePriority':fsMIMstMstiBridgePriority,'fsMIMstMstiRootCost':fsMIMstMstiRootCost,'fsMIMstMstiRootPort':fsMIMstMstiRootPort,'fsMIMstMstiTimeSinceTopologyChange':fsMIMstMstiTimeSinceTopologyChange,_AE:fsMIMstMstiTopChanges,'fsMIMstMstiNewRootBridgeCount':fsMIMstMstiNewRootBridgeCount,'fsMIMstMstiBridgeRoleSelectionSemState':fsMIMstMstiBridgeRoleSelectionSemState,'fsMIMstInstanceUpCount':fsMIMstInstanceUpCount,'fsMIMstInstanceDownCount':fsMIMstInstanceDownCount,_AC:fsMIMstOldDesignatedRoot,'fsMIMstMstiClearBridgeStats':fsMIMstMstiClearBridgeStats,'fsMIMstMstiFlushIndicationThreshold':fsMIMstMstiFlushIndicationThreshold,'fsMIMstMstiTotalFlushCount':fsMIMstMstiTotalFlushCount,'fsMIMstVlanInstanceMappingTable':fsMIMstVlanInstanceMappingTable,'fsMIMstVlanInstanceMappingEntry':fsMIMstVlanInstanceMappingEntry,_Y:fsMIMstInstanceIndex,'fsMIMstMapVlanIndex':fsMIMstMapVlanIndex,'fsMIMstUnMapVlanIndex':fsMIMstUnMapVlanIndex,'fsMIMstSetVlanList':fsMIMstSetVlanList,'fsMIMstResetVlanList':fsMIMstResetVlanList,'fsMIMstInstanceVlanMapped':fsMIMstInstanceVlanMapped,'fsMIMstInstanceVlanMapped2k':fsMIMstInstanceVlanMapped2k,'fsMIMstInstanceVlanMapped3k':fsMIMstInstanceVlanMapped3k,'fsMIMstInstanceVlanMapped4k':fsMIMstInstanceVlanMapped4k,'fsMIMstCistPortTable':fsMIMstCistPortTable,'fsMIMstCistPortEntry':fsMIMstCistPortEntry,_m:fsMIMstCistPort,'fsMIMstCistPortPathCost':fsMIMstCistPortPathCost,'fsMIMstCistPortPriority':fsMIMstCistPortPriority,'fsMIMstCistPortDesignatedRoot':fsMIMstCistPortDesignatedRoot,'fsMIMstCistPortDesignatedBridge':fsMIMstCistPortDesignatedBridge,'fsMIMstCistPortDesignatedPort':fsMIMstCistPortDesignatedPort,'fsMIMstCistPortAdminP2P':fsMIMstCistPortAdminP2P,'fsMIMstCistPortOperP2P':fsMIMstCistPortOperP2P,'fsMIMstCistPortAdminEdgeStatus':fsMIMstCistPortAdminEdgeStatus,'fsMIMstCistPortOperEdgeStatus':fsMIMstCistPortOperEdgeStatus,'fsMIMstCistPortProtocolMigration':fsMIMstCistPortProtocolMigration,_AP:fsMIMstCistPortState,'fsMIMstCistForcePortState':fsMIMstCistForcePortState,'fsMIMstCistPortForwardTransitions':fsMIMstCistPortForwardTransitions,'fsMIMstCistPortRxMstBpduCount':fsMIMstCistPortRxMstBpduCount,'fsMIMstCistPortRxRstBpduCount':fsMIMstCistPortRxRstBpduCount,'fsMIMstCistPortRxConfigBpduCount':fsMIMstCistPortRxConfigBpduCount,'fsMIMstCistPortRxTcnBpduCount':fsMIMstCistPortRxTcnBpduCount,'fsMIMstCistPortTxMstBpduCount':fsMIMstCistPortTxMstBpduCount,'fsMIMstCistPortTxRstBpduCount':fsMIMstCistPortTxRstBpduCount,'fsMIMstCistPortTxConfigBpduCount':fsMIMstCistPortTxConfigBpduCount,'fsMIMstCistPortTxTcnBpduCount':fsMIMstCistPortTxTcnBpduCount,'fsMIMstCistPortInvalidMstBpduRxCount':fsMIMstCistPortInvalidMstBpduRxCount,'fsMIMstCistPortInvalidRstBpduRxCount':fsMIMstCistPortInvalidRstBpduRxCount,'fsMIMstCistPortInvalidConfigBpduRxCount':fsMIMstCistPortInvalidConfigBpduRxCount,'fsMIMstCistPortInvalidTcnBpduRxCount':fsMIMstCistPortInvalidTcnBpduRxCount,'fsMIMstCistPortTransmitSemState':fsMIMstCistPortTransmitSemState,'fsMIMstCistPortReceiveSemState':fsMIMstCistPortReceiveSemState,'fsMIMstCistPortProtMigrationSemState':fsMIMstCistPortProtMigrationSemState,'fsMIMstCistProtocolMigrationCount':fsMIMstCistProtocolMigrationCount,'fsMIMstCistPortDesignatedCost':fsMIMstCistPortDesignatedCost,'fsMIMstCistPortRegionalRoot':fsMIMstCistPortRegionalRoot,'fsMIMstCistPortRegionalPathCost':fsMIMstCistPortRegionalPathCost,'fsMIMstCistSelectedPortRole':fsMIMstCistSelectedPortRole,'fsMIMstCistCurrentPortRole':fsMIMstCistCurrentPortRole,'fsMIMstCistPortInfoSemState':fsMIMstCistPortInfoSemState,'fsMIMstCistPortRoleTransitionSemState':fsMIMstCistPortRoleTransitionSemState,'fsMIMstCistPortStateTransitionSemState':fsMIMstCistPortStateTransitionSemState,'fsMIMstCistPortTopologyChangeSemState':fsMIMstCistPortTopologyChangeSemState,'fsMIMstCistPortHelloTime':fsMIMstCistPortHelloTime,'fsMIMstCistPortOperVersion':fsMIMstCistPortOperVersion,'fsMIMstCistPortEffectivePortState':fsMIMstCistPortEffectivePortState,'fsMIMstCistPortAutoEdgeStatus':fsMIMstCistPortAutoEdgeStatus,'fsMIMstCistPortRestrictedRole':fsMIMstCistPortRestrictedRole,'fsMIMstCistPortRestrictedTCN':fsMIMstCistPortRestrictedTCN,'fsMIMstCistPortAdminPathCost':fsMIMstCistPortAdminPathCost,'fsMIMstCistPortEnableBPDURx':fsMIMstCistPortEnableBPDURx,'fsMIMstCistPortEnableBPDUTx':fsMIMstCistPortEnableBPDUTx,'fsMIMstCistPortPseudoRootId':fsMIMstCistPortPseudoRootId,'fsMIMstCistPortIsL2Gp':fsMIMstCistPortIsL2Gp,'fsMIMstCistPortLoopGuard':fsMIMstCistPortLoopGuard,'fsMIMstCistPortClearStats':fsMIMstCistPortClearStats,'fsMIMstCistPortRcvdEvent':fsMIMstCistPortRcvdEvent,'fsMIMstCistPortRcvdEventSubType':fsMIMstCistPortRcvdEventSubType,'fsMIMstCistPortRcvdEventTimeStamp':fsMIMstCistPortRcvdEventTimeStamp,'fsMIMstCistLoopInconsistentState':fsMIMstCistLoopInconsistentState,'fsMIMstCistPortBpduGuard':fsMIMstCistPortBpduGuard,'fsMIMstMstiPortTable':fsMIMstMstiPortTable,'fsMIMstMstiPortEntry':fsMIMstMstiPortEntry,_A4:fsMIMstMstiPort,'fsMIMstMstiPortPathCost':fsMIMstMstiPortPathCost,'fsMIMstMstiPortPriority':fsMIMstMstiPortPriority,'fsMIMstMstiPortDesignatedRoot':fsMIMstMstiPortDesignatedRoot,'fsMIMstMstiPortDesignatedBridge':fsMIMstMstiPortDesignatedBridge,'fsMIMstMstiPortDesignatedPort':fsMIMstMstiPortDesignatedPort,_AQ:fsMIMstMstiPortState,'fsMIMstMstiForcePortState':fsMIMstMstiForcePortState,'fsMIMstMstiPortForwardTransitions':fsMIMstMstiPortForwardTransitions,'fsMIMstMstiPortReceivedBPDUs':fsMIMstMstiPortReceivedBPDUs,'fsMIMstMstiPortTransmittedBPDUs':fsMIMstMstiPortTransmittedBPDUs,'fsMIMstMstiPortInvalidBPDUsRcvd':fsMIMstMstiPortInvalidBPDUsRcvd,'fsMIMstMstiPortDesignatedCost':fsMIMstMstiPortDesignatedCost,'fsMIMstMstiSelectedPortRole':fsMIMstMstiSelectedPortRole,'fsMIMstMstiCurrentPortRole':fsMIMstMstiCurrentPortRole,'fsMIMstMstiPortInfoSemState':fsMIMstMstiPortInfoSemState,'fsMIMstMstiPortRoleTransitionSemState':fsMIMstMstiPortRoleTransitionSemState,'fsMIMstMstiPortStateTransitionSemState':fsMIMstMstiPortStateTransitionSemState,'fsMIMstMstiPortTopologyChangeSemState':fsMIMstMstiPortTopologyChangeSemState,'fsMIMstMstiPortEffectivePortState':fsMIMstMstiPortEffectivePortState,'fsMIMstMstiPortAdminPathCost':fsMIMstMstiPortAdminPathCost,'fsMIMstMstiPortPseudoRootId':fsMIMstMstiPortPseudoRootId,'fsMIMstMstiPortClearStats':fsMIMstMstiPortClearStats,'fsMIMstMstiPortStateChangeTimeStamp':fsMIMstMstiPortStateChangeTimeStamp,'fsMIMstPortExtTable':fsMIMstPortExtTable,'fsMIMstPortExtEntry':fsMIMstPortExtEntry,_A5:fsMIMstPort,'fsMIMstPortRowStatus':fsMIMstPortRowStatus,'fsMIDot1sFsMstTrapsControl':fsMIDot1sFsMstTrapsControl,'fsMIDot1sFsMstSetGlobalTrapOption':fsMIDot1sFsMstSetGlobalTrapOption,_AA:fsMIMstGlobalErrTrapType,'fsMIDot1sFsMstTrapsControlTable':fsMIDot1sFsMstTrapsControlTable,'fsMIDot1sFsMstTrapsControlEntry':fsMIDot1sFsMstTrapsControlEntry,'fsMIMstSetTraps':fsMIMstSetTraps,_AB:fsMIMstGenTrapType,'fsMIMstPortTrapNotificationTable':fsMIMstPortTrapNotificationTable,'fsMIMstPortTrapNotificationEntry':fsMIMstPortTrapNotificationEntry,_c:fsMIMstPortTrapIndex,_AG:fsMIMstPortMigrationType,_AH:fsMIMstPktErrType,_AI:fsMIMstPktErrVal,'fsMIMstPortRoleTrapNotificationTable':fsMIMstPortRoleTrapNotificationTable,'fsMIMstPortRoleTrapNotificationEntry':fsMIMstPortRoleTrapNotificationEntry,_AN:fsMIMstPortRoleType,_AO:fsMIMstOldRoleType,'fsMIDot1sFutureMstTraps':fsMIDot1sFutureMstTraps,'fsMIMstTraps':fsMIMstTraps,'fsMIMstGlobalErrTrap':fsMIMstGlobalErrTrap,'fsMIMstGenTrap':fsMIMstGenTrap,'fsMIMstNewRootTrap':fsMIMstNewRootTrap,'fsMIMstTopologyChgTrap':fsMIMstTopologyChgTrap,'fsMIMstProtocolMigrationTrap':fsMIMstProtocolMigrationTrap,'fsMIMstInvalidBpduRxdTrap':fsMIMstInvalidBpduRxdTrap,'fsMIMstRegionConfigChangeTrap':fsMIMstRegionConfigChangeTrap,'fsMIMstNewPortRoleTrap':fsMIMstNewPortRoleTrap,'fsMIMstCistHwFailureTrap':fsMIMstCistHwFailureTrap,'fsMIMstMstiHwFailureTrap':fsMIMstMstiHwFailureTrap})