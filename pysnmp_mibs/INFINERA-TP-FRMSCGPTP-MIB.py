_j='frmScgPtpGroup'
_i='frmScgPtpRxProvEqptType'
_h='frmScgPtpTxProvEqptType'
_g='frmScgPtpRxProvNbrTP'
_f='frmScgPtpTxProvNbrTP'
_e='frmScgPtpMuxedProvisionedNeighborMotList'
_d='frmScgPtpPassiveProvisionedNeighborTP'
_c='frmScgPtpProvisionedNeighborAdTpType'
_b='frmScgPtpPathLossHigh'
_a='frmScgPtpPmHistStatsEnable'
_Z='frmScgPtpProvisionedOpenWaveRemotePtp'
_Y='frmScgPtpMuxedProvisionedNeighborTPList'
_X='frmScgPtpAutoDiscSoakTime'
_W='frmScgPtpProvisionedNeighborTP'
_V='frmScgPtpInterfaceType'
_U='frmScgPtpDiscoveredNeighborTP'
_T='frmScgPtpAutoDiscoveryState'
_S='frmScgPtpProvisionedFPMPO'
_R='frmScgPtpMPOAID'
_Q='frmScgPtpScgSupEqptType'
_P='frmScgPtpScgNumber'
_O='frmScgPtpPowerContolLoop'
_N='frmScgPtpLastPathLossCheckFailedReason'
_M='frmScgPtpLastPathLossCheckAttemptStatus'
_L='frmScgPtpLastPathLossCheckAttemptTS'
_K='frmScgPtpPathLossCheckDetectPort'
_J='frmScgPtpPathLoss'
_I='frmScgPtpLastSuccessfullPathLossCheckTS'
_H='frmScgPtpPathLossCheckControlStatus'
_G='frmScgPtpTrafficMode'
_F='ifIndex'
_E='IF-MIB'
_D='read-write'
_C='read-only'
_B='INFINERA-TP-FRMSCGPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatHundredths,InfnAdTpType,InfnAutoDiscoveryState,InfnEnableDisable,InfnEqptType,InfnLastPathLossCheckAttemptStatus,InfnLastPathLossCheckFailedReason,InfnPathLossCheckControlStatus,InfnPmHistStatsControl,InfnTrafficMode,InfnWaveInterfaceType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths','InfnAdTpType','InfnAutoDiscoveryState','InfnEnableDisable','InfnEqptType','InfnLastPathLossCheckAttemptStatus','InfnLastPathLossCheckFailedReason','InfnPathLossCheckControlStatus','InfnPmHistStatsControl','InfnTrafficMode','InfnWaveInterfaceType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
frmScgPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,45))
if mibBuilder.loadTexts:frmScgPtpMIB.setRevisions(('2013-10-20 00:00',))
_FrmScgPtpTable_Object=MibTable
frmScgPtpTable=_FrmScgPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1))
if mibBuilder.loadTexts:frmScgPtpTable.setStatus(_A)
_FrmScgPtpEntry_Object=MibTableRow
frmScgPtpEntry=_FrmScgPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1))
frmScgPtpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:frmScgPtpEntry.setStatus(_A)
_FrmScgPtpScgNumber_Type=Integer32
_FrmScgPtpScgNumber_Object=MibTableColumn
frmScgPtpScgNumber=_FrmScgPtpScgNumber_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,1),_FrmScgPtpScgNumber_Type())
frmScgPtpScgNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpScgNumber.setStatus(_A)
_FrmScgPtpScgSupEqptType_Type=InfnEqptType
_FrmScgPtpScgSupEqptType_Object=MibTableColumn
frmScgPtpScgSupEqptType=_FrmScgPtpScgSupEqptType_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,2),_FrmScgPtpScgSupEqptType_Type())
frmScgPtpScgSupEqptType.setMaxAccess(_D)
if mibBuilder.loadTexts:frmScgPtpScgSupEqptType.setStatus(_A)
_FrmScgPtpMPOAID_Type=DisplayString
_FrmScgPtpMPOAID_Object=MibTableColumn
frmScgPtpMPOAID=_FrmScgPtpMPOAID_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,3),_FrmScgPtpMPOAID_Type())
frmScgPtpMPOAID.setMaxAccess(_D)
if mibBuilder.loadTexts:frmScgPtpMPOAID.setStatus(_A)
_FrmScgPtpProvisionedFPMPO_Type=DisplayString
_FrmScgPtpProvisionedFPMPO_Object=MibTableColumn
frmScgPtpProvisionedFPMPO=_FrmScgPtpProvisionedFPMPO_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,4),_FrmScgPtpProvisionedFPMPO_Type())
frmScgPtpProvisionedFPMPO.setMaxAccess(_D)
if mibBuilder.loadTexts:frmScgPtpProvisionedFPMPO.setStatus(_A)
_FrmScgPtpAutoDiscoveryState_Type=InfnAutoDiscoveryState
_FrmScgPtpAutoDiscoveryState_Object=MibTableColumn
frmScgPtpAutoDiscoveryState=_FrmScgPtpAutoDiscoveryState_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,5),_FrmScgPtpAutoDiscoveryState_Type())
frmScgPtpAutoDiscoveryState.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpAutoDiscoveryState.setStatus(_A)
_FrmScgPtpDiscoveredNeighborTP_Type=DisplayString
_FrmScgPtpDiscoveredNeighborTP_Object=MibTableColumn
frmScgPtpDiscoveredNeighborTP=_FrmScgPtpDiscoveredNeighborTP_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,6),_FrmScgPtpDiscoveredNeighborTP_Type())
frmScgPtpDiscoveredNeighborTP.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpDiscoveredNeighborTP.setStatus(_A)
_FrmScgPtpProvisionedNeighborTP_Type=DisplayString
_FrmScgPtpProvisionedNeighborTP_Object=MibTableColumn
frmScgPtpProvisionedNeighborTP=_FrmScgPtpProvisionedNeighborTP_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,7),_FrmScgPtpProvisionedNeighborTP_Type())
frmScgPtpProvisionedNeighborTP.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpProvisionedNeighborTP.setStatus(_A)
_FrmScgPtpProvisionedNeighborAdTpType_Type=InfnAdTpType
_FrmScgPtpProvisionedNeighborAdTpType_Object=MibTableColumn
frmScgPtpProvisionedNeighborAdTpType=_FrmScgPtpProvisionedNeighborAdTpType_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,8),_FrmScgPtpProvisionedNeighborAdTpType_Type())
frmScgPtpProvisionedNeighborAdTpType.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpProvisionedNeighborAdTpType.setStatus(_A)
_FrmScgPtpInterfaceType_Type=InfnWaveInterfaceType
_FrmScgPtpInterfaceType_Object=MibTableColumn
frmScgPtpInterfaceType=_FrmScgPtpInterfaceType_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,9),_FrmScgPtpInterfaceType_Type())
frmScgPtpInterfaceType.setMaxAccess(_D)
if mibBuilder.loadTexts:frmScgPtpInterfaceType.setStatus(_A)
_FrmScgPtpProvisionedOpenWaveRemotePtp_Type=DisplayString
_FrmScgPtpProvisionedOpenWaveRemotePtp_Object=MibTableColumn
frmScgPtpProvisionedOpenWaveRemotePtp=_FrmScgPtpProvisionedOpenWaveRemotePtp_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,10),_FrmScgPtpProvisionedOpenWaveRemotePtp_Type())
frmScgPtpProvisionedOpenWaveRemotePtp.setMaxAccess(_D)
if mibBuilder.loadTexts:frmScgPtpProvisionedOpenWaveRemotePtp.setStatus(_A)
_FrmScgPtpPmHistStatsEnable_Type=InfnPmHistStatsControl
_FrmScgPtpPmHistStatsEnable_Object=MibTableColumn
frmScgPtpPmHistStatsEnable=_FrmScgPtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,11),_FrmScgPtpPmHistStatsEnable_Type())
frmScgPtpPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpPmHistStatsEnable.setStatus(_A)
_FrmScgPtpTrafficMode_Type=InfnTrafficMode
_FrmScgPtpTrafficMode_Object=MibTableColumn
frmScgPtpTrafficMode=_FrmScgPtpTrafficMode_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,12),_FrmScgPtpTrafficMode_Type())
frmScgPtpTrafficMode.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpTrafficMode.setStatus(_A)
_FrmScgPtpPathLossCheckControlStatus_Type=InfnPathLossCheckControlStatus
_FrmScgPtpPathLossCheckControlStatus_Object=MibTableColumn
frmScgPtpPathLossCheckControlStatus=_FrmScgPtpPathLossCheckControlStatus_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,13),_FrmScgPtpPathLossCheckControlStatus_Type())
frmScgPtpPathLossCheckControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpPathLossCheckControlStatus.setStatus(_A)
_FrmScgPtpLastSuccessfullPathLossCheckTS_Type=Integer32
_FrmScgPtpLastSuccessfullPathLossCheckTS_Object=MibTableColumn
frmScgPtpLastSuccessfullPathLossCheckTS=_FrmScgPtpLastSuccessfullPathLossCheckTS_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,14),_FrmScgPtpLastSuccessfullPathLossCheckTS_Type())
frmScgPtpLastSuccessfullPathLossCheckTS.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpLastSuccessfullPathLossCheckTS.setStatus(_A)
_FrmScgPtpPathLoss_Type=FloatHundredths
_FrmScgPtpPathLoss_Object=MibTableColumn
frmScgPtpPathLoss=_FrmScgPtpPathLoss_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,15),_FrmScgPtpPathLoss_Type())
frmScgPtpPathLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpPathLoss.setStatus(_A)
_FrmScgPtpLastPathLossCheckAttemptTS_Type=Integer32
_FrmScgPtpLastPathLossCheckAttemptTS_Object=MibTableColumn
frmScgPtpLastPathLossCheckAttemptTS=_FrmScgPtpLastPathLossCheckAttemptTS_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,16),_FrmScgPtpLastPathLossCheckAttemptTS_Type())
frmScgPtpLastPathLossCheckAttemptTS.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpLastPathLossCheckAttemptTS.setStatus(_A)
_FrmScgPtpLastPathLossCheckAttemptStatus_Type=InfnLastPathLossCheckAttemptStatus
_FrmScgPtpLastPathLossCheckAttemptStatus_Object=MibTableColumn
frmScgPtpLastPathLossCheckAttemptStatus=_FrmScgPtpLastPathLossCheckAttemptStatus_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,17),_FrmScgPtpLastPathLossCheckAttemptStatus_Type())
frmScgPtpLastPathLossCheckAttemptStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpLastPathLossCheckAttemptStatus.setStatus(_A)
_FrmScgPtpLastPathLossCheckFailedReason_Type=InfnLastPathLossCheckFailedReason
_FrmScgPtpLastPathLossCheckFailedReason_Object=MibTableColumn
frmScgPtpLastPathLossCheckFailedReason=_FrmScgPtpLastPathLossCheckFailedReason_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,18),_FrmScgPtpLastPathLossCheckFailedReason_Type())
frmScgPtpLastPathLossCheckFailedReason.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpLastPathLossCheckFailedReason.setStatus(_A)
_FrmScgPtpPathLossHigh_Type=TruthValue
_FrmScgPtpPathLossHigh_Object=MibTableColumn
frmScgPtpPathLossHigh=_FrmScgPtpPathLossHigh_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,19),_FrmScgPtpPathLossHigh_Type())
frmScgPtpPathLossHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpPathLossHigh.setStatus(_A)
_FrmScgPtpPowerContolLoop_Type=InfnEnableDisable
_FrmScgPtpPowerContolLoop_Object=MibTableColumn
frmScgPtpPowerContolLoop=_FrmScgPtpPowerContolLoop_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,20),_FrmScgPtpPowerContolLoop_Type())
frmScgPtpPowerContolLoop.setMaxAccess(_D)
if mibBuilder.loadTexts:frmScgPtpPowerContolLoop.setStatus(_A)
_FrmScgPtpAutoDiscSoakTime_Type=Integer32
_FrmScgPtpAutoDiscSoakTime_Object=MibTableColumn
frmScgPtpAutoDiscSoakTime=_FrmScgPtpAutoDiscSoakTime_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,21),_FrmScgPtpAutoDiscSoakTime_Type())
frmScgPtpAutoDiscSoakTime.setMaxAccess(_D)
if mibBuilder.loadTexts:frmScgPtpAutoDiscSoakTime.setStatus(_A)
_FrmScgPtpPathLossCheckDetectPort_Type=DisplayString
_FrmScgPtpPathLossCheckDetectPort_Object=MibTableColumn
frmScgPtpPathLossCheckDetectPort=_FrmScgPtpPathLossCheckDetectPort_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,22),_FrmScgPtpPathLossCheckDetectPort_Type())
frmScgPtpPathLossCheckDetectPort.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpPathLossCheckDetectPort.setStatus(_A)
_FrmScgPtpMuxedProvisionedNeighborTPList_Type=DisplayString
_FrmScgPtpMuxedProvisionedNeighborTPList_Object=MibTableColumn
frmScgPtpMuxedProvisionedNeighborTPList=_FrmScgPtpMuxedProvisionedNeighborTPList_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,23),_FrmScgPtpMuxedProvisionedNeighborTPList_Type())
frmScgPtpMuxedProvisionedNeighborTPList.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpMuxedProvisionedNeighborTPList.setStatus(_A)
_FrmScgPtpPassiveProvisionedNeighborTP_Type=DisplayString
_FrmScgPtpPassiveProvisionedNeighborTP_Object=MibTableColumn
frmScgPtpPassiveProvisionedNeighborTP=_FrmScgPtpPassiveProvisionedNeighborTP_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,24),_FrmScgPtpPassiveProvisionedNeighborTP_Type())
frmScgPtpPassiveProvisionedNeighborTP.setMaxAccess(_D)
if mibBuilder.loadTexts:frmScgPtpPassiveProvisionedNeighborTP.setStatus(_A)
_FrmScgPtpMuxedProvisionedNeighborMotList_Type=DisplayString
_FrmScgPtpMuxedProvisionedNeighborMotList_Object=MibTableColumn
frmScgPtpMuxedProvisionedNeighborMotList=_FrmScgPtpMuxedProvisionedNeighborMotList_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,25),_FrmScgPtpMuxedProvisionedNeighborMotList_Type())
frmScgPtpMuxedProvisionedNeighborMotList.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpMuxedProvisionedNeighborMotList.setStatus(_A)
_FrmScgPtpTxProvNbrTP_Type=DisplayString
_FrmScgPtpTxProvNbrTP_Object=MibTableColumn
frmScgPtpTxProvNbrTP=_FrmScgPtpTxProvNbrTP_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,26),_FrmScgPtpTxProvNbrTP_Type())
frmScgPtpTxProvNbrTP.setMaxAccess(_D)
if mibBuilder.loadTexts:frmScgPtpTxProvNbrTP.setStatus(_A)
_FrmScgPtpRxProvNbrTP_Type=DisplayString
_FrmScgPtpRxProvNbrTP_Object=MibTableColumn
frmScgPtpRxProvNbrTP=_FrmScgPtpRxProvNbrTP_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,27),_FrmScgPtpRxProvNbrTP_Type())
frmScgPtpRxProvNbrTP.setMaxAccess(_D)
if mibBuilder.loadTexts:frmScgPtpRxProvNbrTP.setStatus(_A)
_FrmScgPtpTxProvEqptType_Type=InfnEqptType
_FrmScgPtpTxProvEqptType_Object=MibTableColumn
frmScgPtpTxProvEqptType=_FrmScgPtpTxProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,28),_FrmScgPtpTxProvEqptType_Type())
frmScgPtpTxProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpTxProvEqptType.setStatus(_A)
_FrmScgPtpRxProvEqptType_Type=InfnEqptType
_FrmScgPtpRxProvEqptType_Object=MibTableColumn
frmScgPtpRxProvEqptType=_FrmScgPtpRxProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,2,45,1,1,29),_FrmScgPtpRxProvEqptType_Type())
frmScgPtpRxProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:frmScgPtpRxProvEqptType.setStatus(_A)
_FrmScgPtpConformance_ObjectIdentity=ObjectIdentity
frmScgPtpConformance=_FrmScgPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,45,3))
_FrmScgPtpCompliances_ObjectIdentity=ObjectIdentity
frmScgPtpCompliances=_FrmScgPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,45,3,1))
_FrmScgPtpGroups_ObjectIdentity=ObjectIdentity
frmScgPtpGroups=_FrmScgPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,45,3,2))
frmScgPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,45,3,2,1))
frmScgPtpGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:frmScgPtpGroup.setStatus(_A)
frmScgPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,45,3,1,1))
frmScgPtpCompliance.setObjects((_B,_j))
if mibBuilder.loadTexts:frmScgPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'frmScgPtpMIB':frmScgPtpMIB,'frmScgPtpTable':frmScgPtpTable,'frmScgPtpEntry':frmScgPtpEntry,_P:frmScgPtpScgNumber,_Q:frmScgPtpScgSupEqptType,_R:frmScgPtpMPOAID,_S:frmScgPtpProvisionedFPMPO,_T:frmScgPtpAutoDiscoveryState,_U:frmScgPtpDiscoveredNeighborTP,_W:frmScgPtpProvisionedNeighborTP,_c:frmScgPtpProvisionedNeighborAdTpType,_V:frmScgPtpInterfaceType,_Z:frmScgPtpProvisionedOpenWaveRemotePtp,_a:frmScgPtpPmHistStatsEnable,_G:frmScgPtpTrafficMode,_H:frmScgPtpPathLossCheckControlStatus,_I:frmScgPtpLastSuccessfullPathLossCheckTS,_J:frmScgPtpPathLoss,_L:frmScgPtpLastPathLossCheckAttemptTS,_M:frmScgPtpLastPathLossCheckAttemptStatus,_N:frmScgPtpLastPathLossCheckFailedReason,_b:frmScgPtpPathLossHigh,_O:frmScgPtpPowerContolLoop,_X:frmScgPtpAutoDiscSoakTime,_K:frmScgPtpPathLossCheckDetectPort,_Y:frmScgPtpMuxedProvisionedNeighborTPList,_d:frmScgPtpPassiveProvisionedNeighborTP,_e:frmScgPtpMuxedProvisionedNeighborMotList,_f:frmScgPtpTxProvNbrTP,_g:frmScgPtpRxProvNbrTP,_h:frmScgPtpTxProvEqptType,_i:frmScgPtpRxProvEqptType,'frmScgPtpConformance':frmScgPtpConformance,'frmScgPtpCompliances':frmScgPtpCompliances,'frmScgPtpCompliance':frmScgPtpCompliance,'frmScgPtpGroups':frmScgPtpGroups,_j:frmScgPtpGroup})