_X='fmmFScgPtpGroup'
_W='fmmFScgPtpTargetRxPower'
_V='fmmFScgPtpAutoDiscSoakTime'
_U='fmmFScgPtpProvisionedSuperChannelNumber'
_T='fmmFScgPtpProvisionedSpectrumType'
_S='fmmFScgPtpUsedFreqSlotList'
_R='fmmFScgPtpPowerControlLoop'
_Q='fmmFScgPtpProvisionedOpenWaveRemotePtp'
_P='fmmFScgPtpPmHistStatsEnable'
_O='fmmFScgPtpProvisionedNeighborAdTpType'
_N='fmmFScgPtpProvisionedNeighborTP'
_M='fmmFScgPtpInterfaceType'
_L='fmmFScgPtpDiscoveredNeighborTP'
_K='fmmFScgPtpAutoDiscoveryState'
_J='fmmFScgPtpProvisionedFPMPO'
_I='fmmFScgPtpMPOAID'
_H='fmmFScgPtpScgSupEqptType'
_G='fmmFScgPtpScgNumber'
_F='ifIndex'
_E='IF-MIB'
_D='read-write'
_C='read-only'
_B='INFINERA-TP-FMMFSCGPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatHundredths,InfnAdTpType,InfnAutoDiscoveryState,InfnEnableDisable,InfnEqptType,InfnInterfaceType,InfnPmHistStatsControl,InfnSpectrumType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths','InfnAdTpType','InfnAutoDiscoveryState','InfnEnableDisable','InfnEqptType','InfnInterfaceType','InfnPmHistStatsControl','InfnSpectrumType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fmmFScgPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,60))
if mibBuilder.loadTexts:fmmFScgPtpMIB.setRevisions(('2015-05-20 00:00',))
_FmmFScgPtpTable_Object=MibTable
fmmFScgPtpTable=_FmmFScgPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,60,1))
if mibBuilder.loadTexts:fmmFScgPtpTable.setStatus(_A)
_FmmFScgPtpEntry_Object=MibTableRow
fmmFScgPtpEntry=_FmmFScgPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,60,1,1))
fmmFScgPtpEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:fmmFScgPtpEntry.setStatus(_A)
_FmmFScgPtpScgNumber_Type=Integer32
_FmmFScgPtpScgNumber_Object=MibTableColumn
fmmFScgPtpScgNumber=_FmmFScgPtpScgNumber_Object((1,3,6,1,4,1,21296,2,2,2,2,60,1,1,1),_FmmFScgPtpScgNumber_Type())
fmmFScgPtpScgNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmFScgPtpScgNumber.setStatus(_A)
_FmmFScgPtpScgSupEqptType_Type=InfnEqptType
_FmmFScgPtpScgSupEqptType_Object=MibTableColumn
fmmFScgPtpScgSupEqptType=_FmmFScgPtpScgSupEqptType_Object((1,3,6,1,4,1,21296,2,2,2,2,60,1,1,2),_FmmFScgPtpScgSupEqptType_Type())
fmmFScgPtpScgSupEqptType.setMaxAccess(_D)
if mibBuilder.loadTexts:fmmFScgPtpScgSupEqptType.setStatus(_A)
_FmmFScgPtpMPOAID_Type=DisplayString
_FmmFScgPtpMPOAID_Object=MibTableColumn
fmmFScgPtpMPOAID=_FmmFScgPtpMPOAID_Object((1,3,6,1,4,1,21296,2,2,2,2,60,1,1,3),_FmmFScgPtpMPOAID_Type())
fmmFScgPtpMPOAID.setMaxAccess(_D)
if mibBuilder.loadTexts:fmmFScgPtpMPOAID.setStatus(_A)
_FmmFScgPtpProvisionedFPMPO_Type=DisplayString
_FmmFScgPtpProvisionedFPMPO_Object=MibTableColumn
fmmFScgPtpProvisionedFPMPO=_FmmFScgPtpProvisionedFPMPO_Object((1,3,6,1,4,1,21296,2,2,2,2,60,1,1,4),_FmmFScgPtpProvisionedFPMPO_Type())
fmmFScgPtpProvisionedFPMPO.setMaxAccess(_D)
if mibBuilder.loadTexts:fmmFScgPtpProvisionedFPMPO.setStatus(_A)
_FmmFScgPtpAutoDiscoveryState_Type=InfnAutoDiscoveryState
_FmmFScgPtpAutoDiscoveryState_Object=MibTableColumn
fmmFScgPtpAutoDiscoveryState=_FmmFScgPtpAutoDiscoveryState_Object((1,3,6,1,4,1,21296,2,2,2,2,60,1,1,5),_FmmFScgPtpAutoDiscoveryState_Type())
fmmFScgPtpAutoDiscoveryState.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmFScgPtpAutoDiscoveryState.setStatus(_A)
_FmmFScgPtpDiscoveredNeighborTP_Type=DisplayString
_FmmFScgPtpDiscoveredNeighborTP_Object=MibTableColumn
fmmFScgPtpDiscoveredNeighborTP=_FmmFScgPtpDiscoveredNeighborTP_Object((1,3,6,1,4,1,21296,2,2,2,2,60,1,1,6),_FmmFScgPtpDiscoveredNeighborTP_Type())
fmmFScgPtpDiscoveredNeighborTP.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmFScgPtpDiscoveredNeighborTP.setStatus(_A)
_FmmFScgPtpProvisionedNeighborTP_Type=DisplayString
_FmmFScgPtpProvisionedNeighborTP_Object=MibTableColumn
fmmFScgPtpProvisionedNeighborTP=_FmmFScgPtpProvisionedNeighborTP_Object((1,3,6,1,4,1,21296,2,2,2,2,60,1,1,7),_FmmFScgPtpProvisionedNeighborTP_Type())
fmmFScgPtpProvisionedNeighborTP.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmFScgPtpProvisionedNeighborTP.setStatus(_A)
_FmmFScgPtpProvisionedNeighborAdTpType_Type=InfnAdTpType
_FmmFScgPtpProvisionedNeighborAdTpType_Object=MibTableColumn
fmmFScgPtpProvisionedNeighborAdTpType=_FmmFScgPtpProvisionedNeighborAdTpType_Object((1,3,6,1,4,1,21296,2,2,2,2,60,1,1,8),_FmmFScgPtpProvisionedNeighborAdTpType_Type())
fmmFScgPtpProvisionedNeighborAdTpType.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmFScgPtpProvisionedNeighborAdTpType.setStatus(_A)
_FmmFScgPtpInterfaceType_Type=InfnInterfaceType
_FmmFScgPtpInterfaceType_Object=MibTableColumn
fmmFScgPtpInterfaceType=_FmmFScgPtpInterfaceType_Object((1,3,6,1,4,1,21296,2,2,2,2,60,1,1,9),_FmmFScgPtpInterfaceType_Type())
fmmFScgPtpInterfaceType.setMaxAccess(_D)
if mibBuilder.loadTexts:fmmFScgPtpInterfaceType.setStatus(_A)
_FmmFScgPtpProvisionedOpenWaveRemotePtp_Type=DisplayString
_FmmFScgPtpProvisionedOpenWaveRemotePtp_Object=MibTableColumn
fmmFScgPtpProvisionedOpenWaveRemotePtp=_FmmFScgPtpProvisionedOpenWaveRemotePtp_Object((1,3,6,1,4,1,21296,2,2,2,2,60,1,1,10),_FmmFScgPtpProvisionedOpenWaveRemotePtp_Type())
fmmFScgPtpProvisionedOpenWaveRemotePtp.setMaxAccess(_D)
if mibBuilder.loadTexts:fmmFScgPtpProvisionedOpenWaveRemotePtp.setStatus(_A)
_FmmFScgPtpPmHistStatsEnable_Type=InfnPmHistStatsControl
_FmmFScgPtpPmHistStatsEnable_Object=MibTableColumn
fmmFScgPtpPmHistStatsEnable=_FmmFScgPtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,60,1,1,11),_FmmFScgPtpPmHistStatsEnable_Type())
fmmFScgPtpPmHistStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmFScgPtpPmHistStatsEnable.setStatus(_A)
_FmmFScgPtpPowerControlLoop_Type=InfnEnableDisable
_FmmFScgPtpPowerControlLoop_Object=MibTableColumn
fmmFScgPtpPowerControlLoop=_FmmFScgPtpPowerControlLoop_Object((1,3,6,1,4,1,21296,2,2,2,2,60,1,1,12),_FmmFScgPtpPowerControlLoop_Type())
fmmFScgPtpPowerControlLoop.setMaxAccess(_D)
if mibBuilder.loadTexts:fmmFScgPtpPowerControlLoop.setStatus(_A)
_FmmFScgPtpUsedFreqSlotList_Type=DisplayString
_FmmFScgPtpUsedFreqSlotList_Object=MibTableColumn
fmmFScgPtpUsedFreqSlotList=_FmmFScgPtpUsedFreqSlotList_Object((1,3,6,1,4,1,21296,2,2,2,2,60,1,1,13),_FmmFScgPtpUsedFreqSlotList_Type())
fmmFScgPtpUsedFreqSlotList.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmFScgPtpUsedFreqSlotList.setStatus(_A)
_FmmFScgPtpProvisionedSpectrumType_Type=InfnSpectrumType
_FmmFScgPtpProvisionedSpectrumType_Object=MibTableColumn
fmmFScgPtpProvisionedSpectrumType=_FmmFScgPtpProvisionedSpectrumType_Object((1,3,6,1,4,1,21296,2,2,2,2,60,1,1,14),_FmmFScgPtpProvisionedSpectrumType_Type())
fmmFScgPtpProvisionedSpectrumType.setMaxAccess(_D)
if mibBuilder.loadTexts:fmmFScgPtpProvisionedSpectrumType.setStatus(_A)
_FmmFScgPtpProvisionedSuperChannelNumber_Type=DisplayString
_FmmFScgPtpProvisionedSuperChannelNumber_Object=MibTableColumn
fmmFScgPtpProvisionedSuperChannelNumber=_FmmFScgPtpProvisionedSuperChannelNumber_Object((1,3,6,1,4,1,21296,2,2,2,2,60,1,1,15),_FmmFScgPtpProvisionedSuperChannelNumber_Type())
fmmFScgPtpProvisionedSuperChannelNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmFScgPtpProvisionedSuperChannelNumber.setStatus(_A)
_FmmFScgPtpAutoDiscSoakTime_Type=Integer32
_FmmFScgPtpAutoDiscSoakTime_Object=MibTableColumn
fmmFScgPtpAutoDiscSoakTime=_FmmFScgPtpAutoDiscSoakTime_Object((1,3,6,1,4,1,21296,2,2,2,2,60,1,1,16),_FmmFScgPtpAutoDiscSoakTime_Type())
fmmFScgPtpAutoDiscSoakTime.setMaxAccess(_D)
if mibBuilder.loadTexts:fmmFScgPtpAutoDiscSoakTime.setStatus(_A)
_FmmFScgPtpTargetRxPower_Type=FloatHundredths
_FmmFScgPtpTargetRxPower_Object=MibTableColumn
fmmFScgPtpTargetRxPower=_FmmFScgPtpTargetRxPower_Object((1,3,6,1,4,1,21296,2,2,2,2,60,1,1,17),_FmmFScgPtpTargetRxPower_Type())
fmmFScgPtpTargetRxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:fmmFScgPtpTargetRxPower.setStatus(_A)
_FmmFScgPtpConformance_ObjectIdentity=ObjectIdentity
fmmFScgPtpConformance=_FmmFScgPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,60,3))
_FmmFScgPtpCompliances_ObjectIdentity=ObjectIdentity
fmmFScgPtpCompliances=_FmmFScgPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,60,3,1))
_FmmFScgPtpGroups_ObjectIdentity=ObjectIdentity
fmmFScgPtpGroups=_FmmFScgPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,60,3,2))
fmmFScgPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,60,3,2,1))
fmmFScgPtpGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:fmmFScgPtpGroup.setStatus(_A)
fmmFScgPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,60,3,1,1))
fmmFScgPtpCompliance.setObjects((_B,_X))
if mibBuilder.loadTexts:fmmFScgPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fmmFScgPtpMIB':fmmFScgPtpMIB,'fmmFScgPtpTable':fmmFScgPtpTable,'fmmFScgPtpEntry':fmmFScgPtpEntry,_G:fmmFScgPtpScgNumber,_H:fmmFScgPtpScgSupEqptType,_I:fmmFScgPtpMPOAID,_J:fmmFScgPtpProvisionedFPMPO,_K:fmmFScgPtpAutoDiscoveryState,_L:fmmFScgPtpDiscoveredNeighborTP,_N:fmmFScgPtpProvisionedNeighborTP,_O:fmmFScgPtpProvisionedNeighborAdTpType,_M:fmmFScgPtpInterfaceType,_Q:fmmFScgPtpProvisionedOpenWaveRemotePtp,_P:fmmFScgPtpPmHistStatsEnable,_R:fmmFScgPtpPowerControlLoop,_S:fmmFScgPtpUsedFreqSlotList,_T:fmmFScgPtpProvisionedSpectrumType,_U:fmmFScgPtpProvisionedSuperChannelNumber,_V:fmmFScgPtpAutoDiscSoakTime,_W:fmmFScgPtpTargetRxPower,'fmmFScgPtpConformance':fmmFScgPtpConformance,'fmmFScgPtpCompliances':fmmFScgPtpCompliances,'fmmFScgPtpCompliance':fmmFScgPtpCompliance,'fmmFScgPtpGroups':fmmFScgPtpGroups,_X:fmmFScgPtpGroup})