_g='fsmScgPtpGroup'
_f='fsmScgPtpPathLossHigh'
_e='fsmScgPtpPmHistStatsEnable'
_d='fsmScgPtpProvisionedOpenWaveRemotePtp'
_c='fsmScgPtpProvisionedNeighborTP'
_b='fsmScgPtpInterfaceType'
_a='fsmScgPtpDiscoveredNeighborTP'
_Z='fsmScgPtpAutoDiscoveryState'
_Y='fsmScgPtpProvisionedFPMPO'
_X='fsmScgPtpMPOAID'
_W='fsmScgPtpScgSupEqptType'
_V='fsmScgPtpScgNumber'
_U='fsmScgPtpTrafficMode'
_T='fsmScgPtpRxEdfaPowerOffset'
_S='fsmScgPtpTxEdfaPowerOffset'
_R='fsmScgPtpLastPathLossCheckFailedReason'
_Q='fsmScgPtpLastPathLossCheckAttemptStatus'
_P='fsmScgPtpLastPathLossCheckAttemptTS'
_O='fsmScgPtpPathLossCheckDetectPort'
_N='fsmScgPtpPathLoss'
_M='fsmScgPtpLastSuccessfullPathLossCheckTS'
_L='fsmScgPtpPathLossCheckControlStatus'
_K='fsmScgPtpUsedFreqSlotList'
_J='fsmScgPtpAvailableFreqSlotList'
_I='fsmScgPtpPowerControlLoop'
_H='inProgress'
_G='ifIndex'
_F='IF-MIB'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='INFINERA-TP-FSMSCGPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatHundredths,InfnEnableDisable,InfnEqptType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths','InfnEnableDisable','InfnEqptType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsmScgPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,44))
if mibBuilder.loadTexts:fsmScgPtpMIB.setRevisions(('2013-10-20 00:00',))
_FsmScgPtpTable_Object=MibTable
fsmScgPtpTable=_FsmScgPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1))
if mibBuilder.loadTexts:fsmScgPtpTable.setStatus(_A)
_FsmScgPtpEntry_Object=MibTableRow
fsmScgPtpEntry=_FsmScgPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1,1))
fsmScgPtpEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:fsmScgPtpEntry.setStatus(_A)
_FsmScgPtpPowerControlLoop_Type=InfnEnableDisable
_FsmScgPtpPowerControlLoop_Object=MibTableColumn
fsmScgPtpPowerControlLoop=_FsmScgPtpPowerControlLoop_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1,1,1),_FsmScgPtpPowerControlLoop_Type())
fsmScgPtpPowerControlLoop.setMaxAccess(_E)
if mibBuilder.loadTexts:fsmScgPtpPowerControlLoop.setStatus(_A)
_FsmScgPtpAvailableFreqSlotList_Type=DisplayString
_FsmScgPtpAvailableFreqSlotList_Object=MibTableColumn
fsmScgPtpAvailableFreqSlotList=_FsmScgPtpAvailableFreqSlotList_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1,1,2),_FsmScgPtpAvailableFreqSlotList_Type())
fsmScgPtpAvailableFreqSlotList.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmScgPtpAvailableFreqSlotList.setStatus(_A)
_FsmScgPtpUsedFreqSlotList_Type=DisplayString
_FsmScgPtpUsedFreqSlotList_Object=MibTableColumn
fsmScgPtpUsedFreqSlotList=_FsmScgPtpUsedFreqSlotList_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1,1,3),_FsmScgPtpUsedFreqSlotList_Type())
fsmScgPtpUsedFreqSlotList.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmScgPtpUsedFreqSlotList.setStatus(_A)
class _FsmScgPtpPathLossCheckControlStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('idle',2)))
_FsmScgPtpPathLossCheckControlStatus_Type.__name__=_D
_FsmScgPtpPathLossCheckControlStatus_Object=MibTableColumn
fsmScgPtpPathLossCheckControlStatus=_FsmScgPtpPathLossCheckControlStatus_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1,1,4),_FsmScgPtpPathLossCheckControlStatus_Type())
fsmScgPtpPathLossCheckControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmScgPtpPathLossCheckControlStatus.setStatus(_A)
_FsmScgPtpLastSuccessfullPathLossCheckTS_Type=Integer32
_FsmScgPtpLastSuccessfullPathLossCheckTS_Object=MibTableColumn
fsmScgPtpLastSuccessfullPathLossCheckTS=_FsmScgPtpLastSuccessfullPathLossCheckTS_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1,1,5),_FsmScgPtpLastSuccessfullPathLossCheckTS_Type())
fsmScgPtpLastSuccessfullPathLossCheckTS.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmScgPtpLastSuccessfullPathLossCheckTS.setStatus(_A)
_FsmScgPtpPathLoss_Type=FloatHundredths
_FsmScgPtpPathLoss_Object=MibTableColumn
fsmScgPtpPathLoss=_FsmScgPtpPathLoss_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1,1,6),_FsmScgPtpPathLoss_Type())
fsmScgPtpPathLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmScgPtpPathLoss.setStatus(_A)
_FsmScgPtpPathLossCheckDetectPort_Type=DisplayString
_FsmScgPtpPathLossCheckDetectPort_Object=MibTableColumn
fsmScgPtpPathLossCheckDetectPort=_FsmScgPtpPathLossCheckDetectPort_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1,1,7),_FsmScgPtpPathLossCheckDetectPort_Type())
fsmScgPtpPathLossCheckDetectPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmScgPtpPathLossCheckDetectPort.setStatus(_A)
_FsmScgPtpLastPathLossCheckAttemptTS_Type=Integer32
_FsmScgPtpLastPathLossCheckAttemptTS_Object=MibTableColumn
fsmScgPtpLastPathLossCheckAttemptTS=_FsmScgPtpLastPathLossCheckAttemptTS_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1,1,8),_FsmScgPtpLastPathLossCheckAttemptTS_Type())
fsmScgPtpLastPathLossCheckAttemptTS.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmScgPtpLastPathLossCheckAttemptTS.setStatus(_A)
class _FsmScgPtpLastPathLossCheckAttemptStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('successfull',1),('unsuccessfull',2),('notAttempted',3)))
_FsmScgPtpLastPathLossCheckAttemptStatus_Type.__name__=_D
_FsmScgPtpLastPathLossCheckAttemptStatus_Object=MibTableColumn
fsmScgPtpLastPathLossCheckAttemptStatus=_FsmScgPtpLastPathLossCheckAttemptStatus_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1,1,9),_FsmScgPtpLastPathLossCheckAttemptStatus_Type())
fsmScgPtpLastPathLossCheckAttemptStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmScgPtpLastPathLossCheckAttemptStatus.setStatus(_A)
class _FsmScgPtpLastPathLossCheckFailedReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('notAvailable',1),('timedOut',2),('interruptedByAD',3),('interruptedByReset',4),('portInService',5)))
_FsmScgPtpLastPathLossCheckFailedReason_Type.__name__=_D
_FsmScgPtpLastPathLossCheckFailedReason_Object=MibTableColumn
fsmScgPtpLastPathLossCheckFailedReason=_FsmScgPtpLastPathLossCheckFailedReason_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1,1,10),_FsmScgPtpLastPathLossCheckFailedReason_Type())
fsmScgPtpLastPathLossCheckFailedReason.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmScgPtpLastPathLossCheckFailedReason.setStatus(_A)
_FsmScgPtpTxEdfaPowerOffset_Type=FloatHundredths
_FsmScgPtpTxEdfaPowerOffset_Object=MibTableColumn
fsmScgPtpTxEdfaPowerOffset=_FsmScgPtpTxEdfaPowerOffset_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1,1,11),_FsmScgPtpTxEdfaPowerOffset_Type())
fsmScgPtpTxEdfaPowerOffset.setMaxAccess(_E)
if mibBuilder.loadTexts:fsmScgPtpTxEdfaPowerOffset.setStatus(_A)
_FsmScgPtpRxEdfaPowerOffset_Type=FloatHundredths
_FsmScgPtpRxEdfaPowerOffset_Object=MibTableColumn
fsmScgPtpRxEdfaPowerOffset=_FsmScgPtpRxEdfaPowerOffset_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1,1,12),_FsmScgPtpRxEdfaPowerOffset_Type())
fsmScgPtpRxEdfaPowerOffset.setMaxAccess(_E)
if mibBuilder.loadTexts:fsmScgPtpRxEdfaPowerOffset.setStatus(_A)
class _FsmScgPtpTrafficMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('addDrop',2),('pathLossCheckSource',3)))
_FsmScgPtpTrafficMode_Type.__name__=_D
_FsmScgPtpTrafficMode_Object=MibTableColumn
fsmScgPtpTrafficMode=_FsmScgPtpTrafficMode_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1,1,13),_FsmScgPtpTrafficMode_Type())
fsmScgPtpTrafficMode.setMaxAccess(_E)
if mibBuilder.loadTexts:fsmScgPtpTrafficMode.setStatus(_A)
_FsmScgPtpScgNumber_Type=Integer32
_FsmScgPtpScgNumber_Object=MibTableColumn
fsmScgPtpScgNumber=_FsmScgPtpScgNumber_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1,1,14),_FsmScgPtpScgNumber_Type())
fsmScgPtpScgNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmScgPtpScgNumber.setStatus(_A)
_FsmScgPtpScgSupEqptType_Type=InfnEqptType
_FsmScgPtpScgSupEqptType_Object=MibTableColumn
fsmScgPtpScgSupEqptType=_FsmScgPtpScgSupEqptType_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1,1,15),_FsmScgPtpScgSupEqptType_Type())
fsmScgPtpScgSupEqptType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsmScgPtpScgSupEqptType.setStatus(_A)
_FsmScgPtpMPOAID_Type=DisplayString
_FsmScgPtpMPOAID_Object=MibTableColumn
fsmScgPtpMPOAID=_FsmScgPtpMPOAID_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1,1,16),_FsmScgPtpMPOAID_Type())
fsmScgPtpMPOAID.setMaxAccess(_E)
if mibBuilder.loadTexts:fsmScgPtpMPOAID.setStatus(_A)
_FsmScgPtpProvisionedFPMPO_Type=DisplayString
_FsmScgPtpProvisionedFPMPO_Object=MibTableColumn
fsmScgPtpProvisionedFPMPO=_FsmScgPtpProvisionedFPMPO_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1,1,17),_FsmScgPtpProvisionedFPMPO_Type())
fsmScgPtpProvisionedFPMPO.setMaxAccess(_E)
if mibBuilder.loadTexts:fsmScgPtpProvisionedFPMPO.setStatus(_A)
class _FsmScgPtpAutoDiscoveryState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_H,1),('completed',2),('unknown',3),('notValid',4),('failed',5),('waitToStart',6),('associated',7)))
_FsmScgPtpAutoDiscoveryState_Type.__name__=_D
_FsmScgPtpAutoDiscoveryState_Object=MibTableColumn
fsmScgPtpAutoDiscoveryState=_FsmScgPtpAutoDiscoveryState_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1,1,18),_FsmScgPtpAutoDiscoveryState_Type())
fsmScgPtpAutoDiscoveryState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmScgPtpAutoDiscoveryState.setStatus(_A)
_FsmScgPtpDiscoveredNeighborTP_Type=DisplayString
_FsmScgPtpDiscoveredNeighborTP_Object=MibTableColumn
fsmScgPtpDiscoveredNeighborTP=_FsmScgPtpDiscoveredNeighborTP_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1,1,19),_FsmScgPtpDiscoveredNeighborTP_Type())
fsmScgPtpDiscoveredNeighborTP.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmScgPtpDiscoveredNeighborTP.setStatus(_A)
class _FsmScgPtpInterfaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('optical',1),('electrical',2)))
_FsmScgPtpInterfaceType_Type.__name__=_D
_FsmScgPtpInterfaceType_Object=MibTableColumn
fsmScgPtpInterfaceType=_FsmScgPtpInterfaceType_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1,1,20),_FsmScgPtpInterfaceType_Type())
fsmScgPtpInterfaceType.setMaxAccess(_E)
if mibBuilder.loadTexts:fsmScgPtpInterfaceType.setStatus(_A)
_FsmScgPtpProvisionedOpenWaveRemotePtp_Type=DisplayString
_FsmScgPtpProvisionedOpenWaveRemotePtp_Object=MibTableColumn
fsmScgPtpProvisionedOpenWaveRemotePtp=_FsmScgPtpProvisionedOpenWaveRemotePtp_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1,1,21),_FsmScgPtpProvisionedOpenWaveRemotePtp_Type())
fsmScgPtpProvisionedOpenWaveRemotePtp.setMaxAccess(_E)
if mibBuilder.loadTexts:fsmScgPtpProvisionedOpenWaveRemotePtp.setStatus(_A)
class _FsmScgPtpPmHistStatsEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_FsmScgPtpPmHistStatsEnable_Type.__name__=_D
_FsmScgPtpPmHistStatsEnable_Object=MibTableColumn
fsmScgPtpPmHistStatsEnable=_FsmScgPtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1,1,22),_FsmScgPtpPmHistStatsEnable_Type())
fsmScgPtpPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmScgPtpPmHistStatsEnable.setStatus(_A)
_FsmScgPtpProvisionedNeighborTP_Type=DisplayString
_FsmScgPtpProvisionedNeighborTP_Object=MibTableColumn
fsmScgPtpProvisionedNeighborTP=_FsmScgPtpProvisionedNeighborTP_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1,1,23),_FsmScgPtpProvisionedNeighborTP_Type())
fsmScgPtpProvisionedNeighborTP.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmScgPtpProvisionedNeighborTP.setStatus(_A)
class _FsmScgPtpPathLossHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_FsmScgPtpPathLossHigh_Type.__name__=_D
_FsmScgPtpPathLossHigh_Object=MibTableColumn
fsmScgPtpPathLossHigh=_FsmScgPtpPathLossHigh_Object((1,3,6,1,4,1,21296,2,2,2,2,44,1,1,24),_FsmScgPtpPathLossHigh_Type())
fsmScgPtpPathLossHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:fsmScgPtpPathLossHigh.setStatus(_A)
_FsmScgPtpConformance_ObjectIdentity=ObjectIdentity
fsmScgPtpConformance=_FsmScgPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,44,3))
_FsmScgPtpCompliances_ObjectIdentity=ObjectIdentity
fsmScgPtpCompliances=_FsmScgPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,44,3,1))
_FsmScgPtpGroups_ObjectIdentity=ObjectIdentity
fsmScgPtpGroups=_FsmScgPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,44,3,2))
fsmScgPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,44,3,2,1))
fsmScgPtpGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:fsmScgPtpGroup.setStatus(_A)
fsmScgPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,44,3,1,1))
fsmScgPtpCompliance.setObjects((_B,_g))
if mibBuilder.loadTexts:fsmScgPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsmScgPtpMIB':fsmScgPtpMIB,'fsmScgPtpTable':fsmScgPtpTable,'fsmScgPtpEntry':fsmScgPtpEntry,_I:fsmScgPtpPowerControlLoop,_J:fsmScgPtpAvailableFreqSlotList,_K:fsmScgPtpUsedFreqSlotList,_L:fsmScgPtpPathLossCheckControlStatus,_M:fsmScgPtpLastSuccessfullPathLossCheckTS,_N:fsmScgPtpPathLoss,_O:fsmScgPtpPathLossCheckDetectPort,_P:fsmScgPtpLastPathLossCheckAttemptTS,_Q:fsmScgPtpLastPathLossCheckAttemptStatus,_R:fsmScgPtpLastPathLossCheckFailedReason,_S:fsmScgPtpTxEdfaPowerOffset,_T:fsmScgPtpRxEdfaPowerOffset,_U:fsmScgPtpTrafficMode,_V:fsmScgPtpScgNumber,_W:fsmScgPtpScgSupEqptType,_X:fsmScgPtpMPOAID,_Y:fsmScgPtpProvisionedFPMPO,_Z:fsmScgPtpAutoDiscoveryState,_a:fsmScgPtpDiscoveredNeighborTP,_b:fsmScgPtpInterfaceType,_d:fsmScgPtpProvisionedOpenWaveRemotePtp,_e:fsmScgPtpPmHistStatsEnable,_c:fsmScgPtpProvisionedNeighborTP,_f:fsmScgPtpPathLossHigh,'fsmScgPtpConformance':fsmScgPtpConformance,'fsmScgPtpCompliances':fsmScgPtpCompliances,'fsmScgPtpCompliance':fsmScgPtpCompliance,'fsmScgPtpGroups':fsmScgPtpGroups,_g:fsmScgPtpGroup})