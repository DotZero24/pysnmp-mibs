_b='fbmScgPtpGroup'
_a='fbmScgPtpLastPathLossCheckFailedReason'
_Z='fbmScgPtpLastPathLossCheckAttemptStatus'
_Y='fbmScgPtpLastPathLossCheckAttemptTS'
_X='fbmScgPtpPathLossCheckDetectedPort'
_W='fbmScgPtpPathLoss'
_V='fbmScgPtpLastSuccessfullPathLossCheckTS'
_U='fbmScgPtpPathLossCheckControlStatus'
_T='fbmScgPtpLineOperatingMode'
_S='fbmScgPtpAvailableFreqSlotList'
_R='fbmScgPtpUsedFreqSlotList'
_Q='fbmScgPtpPmHistStatsEnable'
_P='fbmScgPtpProvisionedOpenWaveRemotePtp'
_O='fbmScgPtpProvisionedNeighborAdTpType'
_N='fbmScgPtpProvisionedNeighborTP'
_M='fbmScgPtpInterfaceType'
_L='fbmScgPtpDiscoveredNeighborTP'
_K='fbmScgPtpProvisionedFPMPO'
_J='fbmScgPtpMPOAID'
_I='fbmScgPtpScgSupEqptType'
_H='fbmScgPtpScgNumber'
_G='fbmScgPtpMoId'
_F='ifIndex'
_E='IF-MIB'
_D='read-write'
_C='read-only'
_B='INFINERA-TP-FBMSCGPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatArbitraryPrecision,FloatHundredths,InfnAdTpType,InfnEnableDisableType,InfnEqptType,InfnLastPathLossCheckAttemptStatus,InfnLastPathLossCheckFailedReason,InfnLineOperatingMode,InfnPathLossCheckControlStatus,InfnPmHistStatsControl,InfnWaveInterfaceType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatArbitraryPrecision','FloatHundredths','InfnAdTpType','InfnEnableDisableType','InfnEqptType','InfnLastPathLossCheckAttemptStatus','InfnLastPathLossCheckFailedReason','InfnLineOperatingMode','InfnPathLossCheckControlStatus','InfnPmHistStatsControl','InfnWaveInterfaceType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fbmScgPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,81))
if mibBuilder.loadTexts:fbmScgPtpMIB.setRevisions(('2016-01-23 00:00',))
_FbmScgPtpTable_Object=MibTable
fbmScgPtpTable=_FbmScgPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,81,1))
if mibBuilder.loadTexts:fbmScgPtpTable.setStatus(_A)
_FbmScgPtpEntry_Object=MibTableRow
fbmScgPtpEntry=_FbmScgPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,81,1,1))
fbmScgPtpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:fbmScgPtpEntry.setStatus(_A)
_FbmScgPtpMoId_Type=DisplayString
_FbmScgPtpMoId_Object=MibTableColumn
fbmScgPtpMoId=_FbmScgPtpMoId_Object((1,3,6,1,4,1,21296,2,2,2,2,81,1,1,1),_FbmScgPtpMoId_Type())
fbmScgPtpMoId.setMaxAccess(_D)
if mibBuilder.loadTexts:fbmScgPtpMoId.setStatus(_A)
_FbmScgPtpScgNumber_Type=Integer32
_FbmScgPtpScgNumber_Object=MibTableColumn
fbmScgPtpScgNumber=_FbmScgPtpScgNumber_Object((1,3,6,1,4,1,21296,2,2,2,2,81,1,1,2),_FbmScgPtpScgNumber_Type())
fbmScgPtpScgNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fbmScgPtpScgNumber.setStatus(_A)
_FbmScgPtpScgSupEqptType_Type=InfnEqptType
_FbmScgPtpScgSupEqptType_Object=MibTableColumn
fbmScgPtpScgSupEqptType=_FbmScgPtpScgSupEqptType_Object((1,3,6,1,4,1,21296,2,2,2,2,81,1,1,3),_FbmScgPtpScgSupEqptType_Type())
fbmScgPtpScgSupEqptType.setMaxAccess(_D)
if mibBuilder.loadTexts:fbmScgPtpScgSupEqptType.setStatus(_A)
_FbmScgPtpMPOAID_Type=DisplayString
_FbmScgPtpMPOAID_Object=MibTableColumn
fbmScgPtpMPOAID=_FbmScgPtpMPOAID_Object((1,3,6,1,4,1,21296,2,2,2,2,81,1,1,4),_FbmScgPtpMPOAID_Type())
fbmScgPtpMPOAID.setMaxAccess(_D)
if mibBuilder.loadTexts:fbmScgPtpMPOAID.setStatus(_A)
_FbmScgPtpProvisionedFPMPO_Type=DisplayString
_FbmScgPtpProvisionedFPMPO_Object=MibTableColumn
fbmScgPtpProvisionedFPMPO=_FbmScgPtpProvisionedFPMPO_Object((1,3,6,1,4,1,21296,2,2,2,2,81,1,1,5),_FbmScgPtpProvisionedFPMPO_Type())
fbmScgPtpProvisionedFPMPO.setMaxAccess(_D)
if mibBuilder.loadTexts:fbmScgPtpProvisionedFPMPO.setStatus(_A)
_FbmScgPtpDiscoveredNeighborTP_Type=DisplayString
_FbmScgPtpDiscoveredNeighborTP_Object=MibTableColumn
fbmScgPtpDiscoveredNeighborTP=_FbmScgPtpDiscoveredNeighborTP_Object((1,3,6,1,4,1,21296,2,2,2,2,81,1,1,6),_FbmScgPtpDiscoveredNeighborTP_Type())
fbmScgPtpDiscoveredNeighborTP.setMaxAccess(_C)
if mibBuilder.loadTexts:fbmScgPtpDiscoveredNeighborTP.setStatus(_A)
_FbmScgPtpProvisionedNeighborTP_Type=DisplayString
_FbmScgPtpProvisionedNeighborTP_Object=MibTableColumn
fbmScgPtpProvisionedNeighborTP=_FbmScgPtpProvisionedNeighborTP_Object((1,3,6,1,4,1,21296,2,2,2,2,81,1,1,7),_FbmScgPtpProvisionedNeighborTP_Type())
fbmScgPtpProvisionedNeighborTP.setMaxAccess(_C)
if mibBuilder.loadTexts:fbmScgPtpProvisionedNeighborTP.setStatus(_A)
_FbmScgPtpProvisionedNeighborAdTpType_Type=InfnAdTpType
_FbmScgPtpProvisionedNeighborAdTpType_Object=MibTableColumn
fbmScgPtpProvisionedNeighborAdTpType=_FbmScgPtpProvisionedNeighborAdTpType_Object((1,3,6,1,4,1,21296,2,2,2,2,81,1,1,8),_FbmScgPtpProvisionedNeighborAdTpType_Type())
fbmScgPtpProvisionedNeighborAdTpType.setMaxAccess(_C)
if mibBuilder.loadTexts:fbmScgPtpProvisionedNeighborAdTpType.setStatus(_A)
_FbmScgPtpInterfaceType_Type=InfnWaveInterfaceType
_FbmScgPtpInterfaceType_Object=MibTableColumn
fbmScgPtpInterfaceType=_FbmScgPtpInterfaceType_Object((1,3,6,1,4,1,21296,2,2,2,2,81,1,1,9),_FbmScgPtpInterfaceType_Type())
fbmScgPtpInterfaceType.setMaxAccess(_D)
if mibBuilder.loadTexts:fbmScgPtpInterfaceType.setStatus(_A)
_FbmScgPtpProvisionedOpenWaveRemotePtp_Type=DisplayString
_FbmScgPtpProvisionedOpenWaveRemotePtp_Object=MibTableColumn
fbmScgPtpProvisionedOpenWaveRemotePtp=_FbmScgPtpProvisionedOpenWaveRemotePtp_Object((1,3,6,1,4,1,21296,2,2,2,2,81,1,1,10),_FbmScgPtpProvisionedOpenWaveRemotePtp_Type())
fbmScgPtpProvisionedOpenWaveRemotePtp.setMaxAccess(_D)
if mibBuilder.loadTexts:fbmScgPtpProvisionedOpenWaveRemotePtp.setStatus(_A)
_FbmScgPtpPmHistStatsEnable_Type=InfnPmHistStatsControl
_FbmScgPtpPmHistStatsEnable_Object=MibTableColumn
fbmScgPtpPmHistStatsEnable=_FbmScgPtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,81,1,1,11),_FbmScgPtpPmHistStatsEnable_Type())
fbmScgPtpPmHistStatsEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:fbmScgPtpPmHistStatsEnable.setStatus(_A)
_FbmScgPtpUsedFreqSlotList_Type=DisplayString
_FbmScgPtpUsedFreqSlotList_Object=MibTableColumn
fbmScgPtpUsedFreqSlotList=_FbmScgPtpUsedFreqSlotList_Object((1,3,6,1,4,1,21296,2,2,2,2,81,1,1,12),_FbmScgPtpUsedFreqSlotList_Type())
fbmScgPtpUsedFreqSlotList.setMaxAccess(_C)
if mibBuilder.loadTexts:fbmScgPtpUsedFreqSlotList.setStatus(_A)
_FbmScgPtpAvailableFreqSlotList_Type=DisplayString
_FbmScgPtpAvailableFreqSlotList_Object=MibTableColumn
fbmScgPtpAvailableFreqSlotList=_FbmScgPtpAvailableFreqSlotList_Object((1,3,6,1,4,1,21296,2,2,2,2,81,1,1,13),_FbmScgPtpAvailableFreqSlotList_Type())
fbmScgPtpAvailableFreqSlotList.setMaxAccess(_C)
if mibBuilder.loadTexts:fbmScgPtpAvailableFreqSlotList.setStatus(_A)
_FbmScgPtpLineOperatingMode_Type=InfnLineOperatingMode
_FbmScgPtpLineOperatingMode_Object=MibTableColumn
fbmScgPtpLineOperatingMode=_FbmScgPtpLineOperatingMode_Object((1,3,6,1,4,1,21296,2,2,2,2,81,1,1,14),_FbmScgPtpLineOperatingMode_Type())
fbmScgPtpLineOperatingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:fbmScgPtpLineOperatingMode.setStatus(_A)
_FbmScgPtpPathLossCheckControlStatus_Type=InfnPathLossCheckControlStatus
_FbmScgPtpPathLossCheckControlStatus_Object=MibTableColumn
fbmScgPtpPathLossCheckControlStatus=_FbmScgPtpPathLossCheckControlStatus_Object((1,3,6,1,4,1,21296,2,2,2,2,81,1,1,15),_FbmScgPtpPathLossCheckControlStatus_Type())
fbmScgPtpPathLossCheckControlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fbmScgPtpPathLossCheckControlStatus.setStatus(_A)
_FbmScgPtpLastSuccessfullPathLossCheckTS_Type=Integer32
_FbmScgPtpLastSuccessfullPathLossCheckTS_Object=MibTableColumn
fbmScgPtpLastSuccessfullPathLossCheckTS=_FbmScgPtpLastSuccessfullPathLossCheckTS_Object((1,3,6,1,4,1,21296,2,2,2,2,81,1,1,16),_FbmScgPtpLastSuccessfullPathLossCheckTS_Type())
fbmScgPtpLastSuccessfullPathLossCheckTS.setMaxAccess(_C)
if mibBuilder.loadTexts:fbmScgPtpLastSuccessfullPathLossCheckTS.setStatus(_A)
_FbmScgPtpPathLoss_Type=FloatArbitraryPrecision
_FbmScgPtpPathLoss_Object=MibTableColumn
fbmScgPtpPathLoss=_FbmScgPtpPathLoss_Object((1,3,6,1,4,1,21296,2,2,2,2,81,1,1,17),_FbmScgPtpPathLoss_Type())
fbmScgPtpPathLoss.setMaxAccess(_C)
if mibBuilder.loadTexts:fbmScgPtpPathLoss.setStatus(_A)
_FbmScgPtpPathLossCheckDetectedPort_Type=DisplayString
_FbmScgPtpPathLossCheckDetectedPort_Object=MibTableColumn
fbmScgPtpPathLossCheckDetectedPort=_FbmScgPtpPathLossCheckDetectedPort_Object((1,3,6,1,4,1,21296,2,2,2,2,81,1,1,18),_FbmScgPtpPathLossCheckDetectedPort_Type())
fbmScgPtpPathLossCheckDetectedPort.setMaxAccess(_C)
if mibBuilder.loadTexts:fbmScgPtpPathLossCheckDetectedPort.setStatus(_A)
_FbmScgPtpLastPathLossCheckAttemptTS_Type=Integer32
_FbmScgPtpLastPathLossCheckAttemptTS_Object=MibTableColumn
fbmScgPtpLastPathLossCheckAttemptTS=_FbmScgPtpLastPathLossCheckAttemptTS_Object((1,3,6,1,4,1,21296,2,2,2,2,81,1,1,19),_FbmScgPtpLastPathLossCheckAttemptTS_Type())
fbmScgPtpLastPathLossCheckAttemptTS.setMaxAccess(_C)
if mibBuilder.loadTexts:fbmScgPtpLastPathLossCheckAttemptTS.setStatus(_A)
_FbmScgPtpLastPathLossCheckAttemptStatus_Type=InfnLastPathLossCheckAttemptStatus
_FbmScgPtpLastPathLossCheckAttemptStatus_Object=MibTableColumn
fbmScgPtpLastPathLossCheckAttemptStatus=_FbmScgPtpLastPathLossCheckAttemptStatus_Object((1,3,6,1,4,1,21296,2,2,2,2,81,1,1,20),_FbmScgPtpLastPathLossCheckAttemptStatus_Type())
fbmScgPtpLastPathLossCheckAttemptStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fbmScgPtpLastPathLossCheckAttemptStatus.setStatus(_A)
_FbmScgPtpLastPathLossCheckFailedReason_Type=InfnLastPathLossCheckFailedReason
_FbmScgPtpLastPathLossCheckFailedReason_Object=MibTableColumn
fbmScgPtpLastPathLossCheckFailedReason=_FbmScgPtpLastPathLossCheckFailedReason_Object((1,3,6,1,4,1,21296,2,2,2,2,81,1,1,21),_FbmScgPtpLastPathLossCheckFailedReason_Type())
fbmScgPtpLastPathLossCheckFailedReason.setMaxAccess(_C)
if mibBuilder.loadTexts:fbmScgPtpLastPathLossCheckFailedReason.setStatus(_A)
_FbmScgPtpConformance_ObjectIdentity=ObjectIdentity
fbmScgPtpConformance=_FbmScgPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,81,3))
_FbmScgPtpCompliances_ObjectIdentity=ObjectIdentity
fbmScgPtpCompliances=_FbmScgPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,81,3,1))
_FbmScgPtpGroups_ObjectIdentity=ObjectIdentity
fbmScgPtpGroups=_FbmScgPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,81,3,2))
fbmScgPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,81,3,2,1))
fbmScgPtpGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:fbmScgPtpGroup.setStatus(_A)
fbmScgPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,81,3,1,1))
fbmScgPtpCompliance.setObjects((_B,_b))
if mibBuilder.loadTexts:fbmScgPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fbmScgPtpMIB':fbmScgPtpMIB,'fbmScgPtpTable':fbmScgPtpTable,'fbmScgPtpEntry':fbmScgPtpEntry,_G:fbmScgPtpMoId,_H:fbmScgPtpScgNumber,_I:fbmScgPtpScgSupEqptType,_J:fbmScgPtpMPOAID,_K:fbmScgPtpProvisionedFPMPO,_L:fbmScgPtpDiscoveredNeighborTP,_N:fbmScgPtpProvisionedNeighborTP,_O:fbmScgPtpProvisionedNeighborAdTpType,_M:fbmScgPtpInterfaceType,_P:fbmScgPtpProvisionedOpenWaveRemotePtp,_Q:fbmScgPtpPmHistStatsEnable,_R:fbmScgPtpUsedFreqSlotList,_S:fbmScgPtpAvailableFreqSlotList,_T:fbmScgPtpLineOperatingMode,_U:fbmScgPtpPathLossCheckControlStatus,_V:fbmScgPtpLastSuccessfullPathLossCheckTS,_W:fbmScgPtpPathLoss,_X:fbmScgPtpPathLossCheckDetectedPort,_Y:fbmScgPtpLastPathLossCheckAttemptTS,_Z:fbmScgPtpLastPathLossCheckAttemptStatus,_a:fbmScgPtpLastPathLossCheckFailedReason,'fbmScgPtpConformance':fbmScgPtpConformance,'fbmScgPtpCompliances':fbmScgPtpCompliances,'fbmScgPtpCompliance':fbmScgPtpCompliance,'fbmScgPtpGroups':fbmScgPtpGroups,_b:fbmScgPtpGroup})