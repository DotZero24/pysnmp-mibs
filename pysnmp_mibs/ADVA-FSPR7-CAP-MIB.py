_Bc='objectGroupCap'
_Bb='externalPortCapMinChromDisperRcv'
_Ba='externalPortCapMaxPmdRcv'
_BZ='externalPortCapMaxOptPowerRcv'
_BY='externalPortCapMinOptPowerRcv'
_BX='externalPortCapMinOsnrRcv'
_BW='externalPortCapChromDisperTx'
_BV='externalPortCapPmdTransmit'
_BU='externalPortCapOsnrTransmit'
_BT='externalPortCapOpticalPowerTx'
_BS='externalPortCapFrameFormat'
_BR='externalPortCapLineCoding'
_BQ='externalPortCapFecType'
_BP='externalPortCapSourceProfile'
_BO='externalPortCapMaxBitErrorRate'
_BN='externalPortCapMaxChromDisperRcv'
_BM='externalPortCapBitrate'
_BL='externalPortCapFarEndLocation'
_BK='externalPortCapAlias'
_BJ='externalPortCapChannelBandwith'
_BI='externalPortCapTransmitChannel'
_BH='externalPortCapType'
_BG='externalPortCapRowStatus'
_BF='connectionCapType'
_BE='connectionCapRowStatus'
_BD='terminationPointCapAlias'
_BC='terminationPointCapFiberDetect'
_BB='terminationPointCapAdmin'
_BA='terminationPointCapRowStatus'
_B9='oprThresholdConfigCapHighConfig'
_B8='oprThresholdConfigCapLowConfig'
_B7='optThresholdConfigCapHighConfig'
_B6='optThresholdConfigCapLowConfig'
_B5='virtualPortCapInitEqlz'
_B4='virtualPortCapEqlzAdmin'
_B3='virtualPortCapAdmin'
_B2='virtualPortCapAlias'
_B1='virtualPortCapType'
_B0='virtualPortCapChannelBand'
_A_='virtualPortCapRowStatus'
_Az='physicalPortCapAdmin'
_Ay='physicalPortCapType'
_Ax='physicalPortCapRowStatus'
_Aw='crossConnectionCapType'
_Av='crossOpticalLineCapTunnelAid'
_Au='crossOpticalLineCapAlias'
_At='crossOpticalLineCapCrsType'
_As='crossOpticalLineCapConn'
_Ar='crossOpticalLineCapRedLineState'
_Aq='crossOpticalLineCapRowStatus'
_Ap='crossConnectionCapTunnelAid'
_Ao='crossConnectionCapPathNode'
_An='crossConnectionCapAlias'
_Am='crossConnectionCapConn'
_Al='crossConnectionCapRedLineState'
_Ak='crossConnectionCapAdmin'
_Aj='crossConnectionCapRowStatus'
_Ai='0.001 GHz'
_Ah='0.1 dB/min'
_Ag='entityShelfConnSlotNo'
_Af='entityShelfConnShelfNo'
_Ae='entityShelfConnPortNo'
_Ad='entityShelfConnExtNo'
_Ac='entityShelfConnClassName'
_Ab='entityProtectionCableIndex4'
_Aa='entityProtectionCableIndex3'
_AZ='entityProtectionCableIndex2'
_AY='entityProtectionCableIndex1'
_AX='entityProtectionCableClassName'
_AW='entityOptLineClassName'
_AV='entityFilterCableIndex4'
_AU='entityFilterCableIndex3'
_AT='entityFilterCableIndex2'
_AS='entityFilterCableIndex1'
_AR='entityFilterCableClassName'
_AQ='entityFfpSlotNo'
_AP='entityFfpShelfNo'
_AO='entityFfpPortNo'
_AN='entityFfpExtNo'
_AM='entityFfpClassName'
_AL='entityExternalPortSlotNo'
_AK='entityExternalPortShelfNo'
_AJ='entityExternalPortPortNo'
_AI='entityExternalPortExtNo'
_AH='entityExternalPortClassName'
_AG='entityCrsOptLineToIndexNo4'
_AF='entityCrsOptLineToIndexNo3'
_AE='entityCrsOptLineToIndexNo2'
_AD='entityCrsOptLineToIndexNo1'
_AC='entityCrsOptLineToClassName'
_AB='entityCrsOptLineFromIndexNo4'
_AA='entityCrsOptLineFromIndexNo3'
_A9='entityCrsOptLineFromIndexNo2'
_A8='entityCrsOptLineFromIndexNo1'
_A7='entityCrsOptLineFromClassName'
_A6='entityCrsOptLineClassName'
_A5='entityCrossDcnSlotNo'
_A4='entityCrossDcnShelfNo'
_A3='entityCrossDcnPortNo'
_A2='entityCrossDcnExtNo'
_A1='entityCrossDcnClassName'
_A0='entityCrossConnToSlotNo'
_z='entityCrossConnToShelfNo'
_y='entityCrossConnToPortNo'
_x='entityCrossConnToExtNo'
_w='entityCrossConnToClassName'
_v='entityCrossConnFromSlotNo'
_u='entityCrossConnFromShelfNo'
_t='entityCrossConnFromPortNo'
_s='entityCrossConnFromExtNo'
_r='entityCrossConnFromClassName'
_q='entityCrossConnClassName'
_p='entityContainerSlotNo'
_o='entityContainerShelfNo'
_n='entityContainerPortNo'
_m='entityContainerExtNo'
_l='entityContainerClassName'
_k='entityConnectionClassName'
_j='entityOpticalMuxSlotNo'
_i='entityOpticalMuxShelfNo'
_h='entityOpticalMuxPortNo'
_g='entityOpticalMuxExtNo'
_f='entityOpticalMuxClassName'
_e='entityTerminPointIndexNo4'
_d='entityTerminPointIndexNo3'
_c='entityTerminPointIndexNo2'
_b='entityTerminPointIndexNo1'
_a='entityTerminPointClassName'
_Z='entityOptLineIndexNo1'
_Y='entityEqptSlotNo'
_X='entityEqptShelfNo'
_W='entityEqptPortNo'
_V='entityEqptExtNo'
_U='entityEqptClassName'
_T='entityDcnSlotNo'
_S='entityDcnShelfNo'
_R='entityDcnPortNo'
_Q='entityDcnExtNo'
_P='entityDcnClassName'
_O='ms'
_N='ps/nm'
_M='entityFacilitySlotNo'
_L='entityFacilityShelfNo'
_K='entityFacilityPortNo'
_J='entityFacilityExtNo'
_I='entityFacilityClassName'
_H='s'
_G='%'
_F='0.1 dB'
_E='0.1 dBm'
_D='ADVA-FSPR7-CAP-MIB'
_C='ADVA-FSPR7-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entityConnectionClassName,entityContainerClassName,entityContainerExtNo,entityContainerPortNo,entityContainerShelfNo,entityContainerSlotNo,entityCrossConnClassName,entityCrossConnFromClassName,entityCrossConnFromExtNo,entityCrossConnFromPortNo,entityCrossConnFromShelfNo,entityCrossConnFromSlotNo,entityCrossConnToClassName,entityCrossConnToExtNo,entityCrossConnToPortNo,entityCrossConnToShelfNo,entityCrossConnToSlotNo,entityCrossDcnClassName,entityCrossDcnExtNo,entityCrossDcnPortNo,entityCrossDcnShelfNo,entityCrossDcnSlotNo,entityCrsOptLineClassName,entityCrsOptLineFromClassName,entityCrsOptLineFromIndexNo1,entityCrsOptLineFromIndexNo2,entityCrsOptLineFromIndexNo3,entityCrsOptLineFromIndexNo4,entityCrsOptLineToClassName,entityCrsOptLineToIndexNo1,entityCrsOptLineToIndexNo2,entityCrsOptLineToIndexNo3,entityCrsOptLineToIndexNo4,entityDcnClassName,entityDcnExtNo,entityDcnPortNo,entityDcnShelfNo,entityDcnSlotNo,entityEqptClassName,entityEqptExtNo,entityEqptPortNo,entityEqptShelfNo,entityEqptSlotNo,entityExternalPortClassName,entityExternalPortExtNo,entityExternalPortPortNo,entityExternalPortShelfNo,entityExternalPortSlotNo,entityFacilityClassName,entityFacilityExtNo,entityFacilityPortNo,entityFacilityShelfNo,entityFacilitySlotNo,entityFfpClassName,entityFfpExtNo,entityFfpPortNo,entityFfpShelfNo,entityFfpSlotNo,entityFilterCableClassName,entityFilterCableIndex1,entityFilterCableIndex2,entityFilterCableIndex3,entityFilterCableIndex4,entityOptLineClassName,entityOptLineIndexNo1,entityOpticalMuxClassName,entityOpticalMuxExtNo,entityOpticalMuxPortNo,entityOpticalMuxShelfNo,entityOpticalMuxSlotNo,entityProtectionCableClassName,entityProtectionCableIndex1,entityProtectionCableIndex2,entityProtectionCableIndex3,entityProtectionCableIndex4,entityShelfConnClassName,entityShelfConnExtNo,entityShelfConnPortNo,entityShelfConnShelfNo,entityShelfConnSlotNo,entityTerminPointClassName,entityTerminPointIndexNo1,entityTerminPointIndexNo2,entityTerminPointIndexNo3,entityTerminPointIndexNo4=mibBuilder.importSymbols(_C,_k,_l,_m,_n,_o,_p,_q,_r,_s,_t,_u,_v,_w,_x,_y,_z,_A0,_A1,_A2,_A3,_A4,_A5,_A6,_A7,_A8,_A9,_AA,_AB,_AC,_AD,_AE,_AF,_AG,_P,_Q,_R,_S,_T,_U,_V,_W,_X,_Y,_AH,_AI,_AJ,_AK,_AL,_I,_J,_K,_L,_M,_AM,_AN,_AO,_AP,_AQ,_AR,_AS,_AT,_AU,_AV,_AW,_Z,_f,_g,_h,_i,_j,_AX,_AY,_AZ,_Aa,_Ab,_Ac,_Ad,_Ae,_Af,_Ag,_a,_b,_c,_d,_e)
ApsRevertModeCaps,ApsTypeCaps,Counter64StringCaps,FfpTypeCaps,FspR7APSCommandCaps,FspR7AdminStateCaps,FspR7AlsModeCaps,FspR7AseTabOprCaps,FspR7AutoThresResetCaps,FspR7BERThresholdCaps,FspR7BERThresholdSectionCaps,FspR7BaundCaps,FspR7BidirectionalChannelCaps,FspR7BitrateCaps,FspR7CapInventoryCaps,FspR7ChannelBandwidthCaps,FspR7ChannelIdentifierCaps,FspR7ChannelSpacingCaps,FspR7CodeGainCaps,FspR7ConnCaps,FspR7ConnectorTypeCaps,FspR7CpAuthTypeCaps,FspR7DCFiberTypeCaps,FspR7DeploymentScenarioCaps,FspR7DisableEnableCaps,FspR7DispersionCompensationCaps,FspR7DispersionConfigCaps,FspR7DispersionModesCaps,FspR7EdfaOutputPowerRatingCaps,FspR7EnableDisableCaps,FspR7EqlzAdminStateCaps,FspR7ErrorFwdModeCaps,FspR7FecTypeCaps,FspR7FiberBrandCaps,FspR7FiberDetectCaps,FspR7FlowControlModeCaps,FspR7FltrCableTypeCaps,FspR7ForceConfigCaps,FspR7ForcedStatusCaps,FspR7FrameFormatCaps,FspR7FunctionCrsCaps,FspR7GainCaps,FspR7GainRangeCaps,FspR7IPv6TypeCaps,FspR7InitEqualizationCaps,FspR7Integer32Caps,FspR7InterfaceTypeCaps,FspR7InvertTelemetryInputLogicCaps,FspR7IpModeCaps,FspR7IpTypeCaps,FspR7LacpModeCaps,FspR7LacpTimeoutCaps,FspR7LagPortTypeCaps,FspR7LaneGroupInventoryCaps,FspR7LaserDelayTimerCaps,FspR7LaserForcedOperationCaps,FspR7LineCodingCaps,FspR7LossAttenuationCaps,FspR7ManualAutoCaps,FspR7MappingCaps,FspR7MaxBitErrorRateCaps,FspR7MuxMethodCaps,FspR7NdpCleanupCaps,FspR7NoYesCaps,FspR7NumberOfChannelsCaps,FspR7NumberOfChannelsProvCaps,FspR7OptUpdateCaps,FspR7OpticalBandCaps,FspR7OpticalFiberTypeCaps,FspR7OpticalGroupCaps,FspR7OpticalInterfaceReachCaps,FspR7OpticalSubBandCaps,FspR7OpuPayloadTypeCaps,FspR7OscUsageCaps,FspR7OspfModeCaps,FspR7OtdrPeriodCaps,FspR7PRBSTestCaps,FspR7PathNodeCaps,FspR7PlugDataRateCaps,FspR7PmResetCaps,FspR7PortBehaviourCaps,FspR7PortModeCaps,FspR7PortRoleCaps,FspR7PrbsPmResetCaps,FspR7PsuOutputPowerCaps,FspR7RedLinedStateCaps,FspR7RlsManCaps,FspR7RoadmNumberCaps,FspR7RowStatusCaps,FspR7ScramblingCaps,FspR7SingleFiberLocationCaps,FspR7SnmpLongString,FspR7StuffCaps,FspR7SupplyTypeCaps,FspR7TelemetryOutputCaps,FspR7TifOutputResetCaps,FspR7TiltSetCaps,FspR7TopologyCaps,FspR7TrafficDirectionCaps,FspR7TransmissionModeCaps,FspR7TurnupConfigCaps,FspR7TxOffOnTmCaps,FspR7TypeConnectionCaps,FspR7TypeCrsCaps,FspR7Unsigned32Caps,FspR7UntaggedFramesCaps,FspR7VoaModeCaps,FspR7XfpDecisionThresCaps,FspR7YcableTypeCaps,FspR7YesNo,FspR7YesNoCaps=mibBuilder.importSymbols('ADVA-FSPR7-TC-MIB','ApsRevertModeCaps','ApsTypeCaps','Counter64StringCaps','FfpTypeCaps','FspR7APSCommandCaps','FspR7AdminStateCaps','FspR7AlsModeCaps','FspR7AseTabOprCaps','FspR7AutoThresResetCaps','FspR7BERThresholdCaps','FspR7BERThresholdSectionCaps','FspR7BaundCaps','FspR7BidirectionalChannelCaps','FspR7BitrateCaps','FspR7CapInventoryCaps','FspR7ChannelBandwidthCaps','FspR7ChannelIdentifierCaps','FspR7ChannelSpacingCaps','FspR7CodeGainCaps','FspR7ConnCaps','FspR7ConnectorTypeCaps','FspR7CpAuthTypeCaps','FspR7DCFiberTypeCaps','FspR7DeploymentScenarioCaps','FspR7DisableEnableCaps','FspR7DispersionCompensationCaps','FspR7DispersionConfigCaps','FspR7DispersionModesCaps','FspR7EdfaOutputPowerRatingCaps','FspR7EnableDisableCaps','FspR7EqlzAdminStateCaps','FspR7ErrorFwdModeCaps','FspR7FecTypeCaps','FspR7FiberBrandCaps','FspR7FiberDetectCaps','FspR7FlowControlModeCaps','FspR7FltrCableTypeCaps','FspR7ForceConfigCaps','FspR7ForcedStatusCaps','FspR7FrameFormatCaps','FspR7FunctionCrsCaps','FspR7GainCaps','FspR7GainRangeCaps','FspR7IPv6TypeCaps','FspR7InitEqualizationCaps','FspR7Integer32Caps','FspR7InterfaceTypeCaps','FspR7InvertTelemetryInputLogicCaps','FspR7IpModeCaps','FspR7IpTypeCaps','FspR7LacpModeCaps','FspR7LacpTimeoutCaps','FspR7LagPortTypeCaps','FspR7LaneGroupInventoryCaps','FspR7LaserDelayTimerCaps','FspR7LaserForcedOperationCaps','FspR7LineCodingCaps','FspR7LossAttenuationCaps','FspR7ManualAutoCaps','FspR7MappingCaps','FspR7MaxBitErrorRateCaps','FspR7MuxMethodCaps','FspR7NdpCleanupCaps','FspR7NoYesCaps','FspR7NumberOfChannelsCaps','FspR7NumberOfChannelsProvCaps','FspR7OptUpdateCaps','FspR7OpticalBandCaps','FspR7OpticalFiberTypeCaps','FspR7OpticalGroupCaps','FspR7OpticalInterfaceReachCaps','FspR7OpticalSubBandCaps','FspR7OpuPayloadTypeCaps','FspR7OscUsageCaps','FspR7OspfModeCaps','FspR7OtdrPeriodCaps','FspR7PRBSTestCaps','FspR7PathNodeCaps','FspR7PlugDataRateCaps','FspR7PmResetCaps','FspR7PortBehaviourCaps','FspR7PortModeCaps','FspR7PortRoleCaps','FspR7PrbsPmResetCaps','FspR7PsuOutputPowerCaps','FspR7RedLinedStateCaps','FspR7RlsManCaps','FspR7RoadmNumberCaps','FspR7RowStatusCaps','FspR7ScramblingCaps','FspR7SingleFiberLocationCaps','FspR7SnmpLongString','FspR7StuffCaps','FspR7SupplyTypeCaps','FspR7TelemetryOutputCaps','FspR7TifOutputResetCaps','FspR7TiltSetCaps','FspR7TopologyCaps','FspR7TrafficDirectionCaps','FspR7TransmissionModeCaps','FspR7TurnupConfigCaps','FspR7TxOffOnTmCaps','FspR7TypeConnectionCaps','FspR7TypeCrsCaps','FspR7Unsigned32Caps','FspR7UntaggedFramesCaps','FspR7VoaModeCaps','FspR7XfpDecisionThresCaps','FspR7YcableTypeCaps','FspR7YesNo','FspR7YesNoCaps')
ApsDirectionCaps,ApsHoldoffTimeCaps,EnableStateCaps,EthDuplexModeCaps,FspR7EquipmentTypeCaps,LoopConfigCaps,OhTerminationLevelCaps,OtnPayloadTypeCaps,OtnTcmLevelCaps,ProtectionMechCaps,SonetTimingSourceCaps,SonetTraceFormCaps,TimModeCaps,VirtualContainerTypeCaps,fspR7=mibBuilder.importSymbols('ADVA-MIB','ApsDirectionCaps','ApsHoldoffTimeCaps','EnableStateCaps','EthDuplexModeCaps','FspR7EquipmentTypeCaps','LoopConfigCaps','OhTerminationLevelCaps','OtnPayloadTypeCaps','OtnTcmLevelCaps','ProtectionMechCaps','SonetTimingSourceCaps','SonetTraceFormCaps','TimModeCaps','VirtualContainerTypeCaps','fspR7')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
advaFspR7Cap=ModuleIdentity((1,3,6,1,4,1,2544,1,11,9))
if mibBuilder.loadTexts:advaFspR7Cap.setRevisions(('2014-10-15 00:00','2014-09-29 00:00','2013-12-04 00:00','2013-08-20 00:00','2011-05-22 00:00'))
_ManagementCap_ObjectIdentity=ObjectIdentity
managementCap=_ManagementCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,3))
_SpecificMgmtCap_ObjectIdentity=ObjectIdentity
specificMgmtCap=_SpecificMgmtCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,3,2))
_CrossConnectionCapTable_Object=MibTable
crossConnectionCapTable=_CrossConnectionCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,2,6))
if mibBuilder.loadTexts:crossConnectionCapTable.setStatus(_A)
_CrossConnectionCapEntry_Object=MibTableRow
crossConnectionCapEntry=_CrossConnectionCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,3,2,6,1))
crossConnectionCapEntry.setIndexNames((0,_C,_u),(0,_C,_v),(0,_C,_t),(0,_C,_s),(0,_C,_r),(0,_C,_z),(0,_C,_A0),(0,_C,_y),(0,_C,_x),(0,_C,_w),(0,_C,_q))
if mibBuilder.loadTexts:crossConnectionCapEntry.setStatus(_A)
_CrossConnectionCapRowStatus_Type=FspR7RowStatusCaps
_CrossConnectionCapRowStatus_Object=MibTableColumn
crossConnectionCapRowStatus=_CrossConnectionCapRowStatus_Object((1,3,6,1,4,1,2544,1,11,9,3,2,6,1,1),_CrossConnectionCapRowStatus_Type())
crossConnectionCapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:crossConnectionCapRowStatus.setStatus(_A)
_CrossConnectionCapAdmin_Type=FspR7AdminStateCaps
_CrossConnectionCapAdmin_Object=MibTableColumn
crossConnectionCapAdmin=_CrossConnectionCapAdmin_Object((1,3,6,1,4,1,2544,1,11,9,3,2,6,1,2),_CrossConnectionCapAdmin_Type())
crossConnectionCapAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:crossConnectionCapAdmin.setStatus(_A)
_CrossConnectionCapRedLineState_Type=FspR7RedLinedStateCaps
_CrossConnectionCapRedLineState_Object=MibTableColumn
crossConnectionCapRedLineState=_CrossConnectionCapRedLineState_Object((1,3,6,1,4,1,2544,1,11,9,3,2,6,1,3),_CrossConnectionCapRedLineState_Type())
crossConnectionCapRedLineState.setMaxAccess(_B)
if mibBuilder.loadTexts:crossConnectionCapRedLineState.setStatus(_A)
_CrossConnectionCapConn_Type=FspR7ConnCaps
_CrossConnectionCapConn_Object=MibTableColumn
crossConnectionCapConn=_CrossConnectionCapConn_Object((1,3,6,1,4,1,2544,1,11,9,3,2,6,1,4),_CrossConnectionCapConn_Type())
crossConnectionCapConn.setMaxAccess(_B)
if mibBuilder.loadTexts:crossConnectionCapConn.setStatus(_A)
_CrossConnectionCapAlias_Type=Integer32
_CrossConnectionCapAlias_Object=MibTableColumn
crossConnectionCapAlias=_CrossConnectionCapAlias_Object((1,3,6,1,4,1,2544,1,11,9,3,2,6,1,5),_CrossConnectionCapAlias_Type())
crossConnectionCapAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:crossConnectionCapAlias.setStatus(_A)
_CrossConnectionCapPathNode_Type=FspR7PathNodeCaps
_CrossConnectionCapPathNode_Object=MibTableColumn
crossConnectionCapPathNode=_CrossConnectionCapPathNode_Object((1,3,6,1,4,1,2544,1,11,9,3,2,6,1,6),_CrossConnectionCapPathNode_Type())
crossConnectionCapPathNode.setMaxAccess(_B)
if mibBuilder.loadTexts:crossConnectionCapPathNode.setStatus(_A)
_CrossConnectionCapTunnelAid_Type=Integer32
_CrossConnectionCapTunnelAid_Object=MibTableColumn
crossConnectionCapTunnelAid=_CrossConnectionCapTunnelAid_Object((1,3,6,1,4,1,2544,1,11,9,3,2,6,1,7),_CrossConnectionCapTunnelAid_Type())
crossConnectionCapTunnelAid.setMaxAccess(_B)
if mibBuilder.loadTexts:crossConnectionCapTunnelAid.setStatus(_A)
_CrossConnectionCapType_Type=FspR7InterfaceTypeCaps
_CrossConnectionCapType_Object=MibTableColumn
crossConnectionCapType=_CrossConnectionCapType_Object((1,3,6,1,4,1,2544,1,11,9,3,2,6,1,8),_CrossConnectionCapType_Type())
crossConnectionCapType.setMaxAccess(_B)
if mibBuilder.loadTexts:crossConnectionCapType.setStatus(_A)
_CrossConnectionCapCrsFunction_Type=FspR7FunctionCrsCaps
_CrossConnectionCapCrsFunction_Object=MibTableColumn
crossConnectionCapCrsFunction=_CrossConnectionCapCrsFunction_Object((1,3,6,1,4,1,2544,1,11,9,3,2,6,1,9),_CrossConnectionCapCrsFunction_Type())
crossConnectionCapCrsFunction.setMaxAccess(_B)
if mibBuilder.loadTexts:crossConnectionCapCrsFunction.setStatus(_A)
_CrossConnectionCapCrsFromAidTwo_Type=FspR7SnmpLongString
_CrossConnectionCapCrsFromAidTwo_Object=MibTableColumn
crossConnectionCapCrsFromAidTwo=_CrossConnectionCapCrsFromAidTwo_Object((1,3,6,1,4,1,2544,1,11,9,3,2,6,1,10),_CrossConnectionCapCrsFromAidTwo_Type())
crossConnectionCapCrsFromAidTwo.setMaxAccess(_B)
if mibBuilder.loadTexts:crossConnectionCapCrsFromAidTwo.setStatus(_A)
_CrossConnectionCapCrsToAidTwo_Type=FspR7SnmpLongString
_CrossConnectionCapCrsToAidTwo_Object=MibTableColumn
crossConnectionCapCrsToAidTwo=_CrossConnectionCapCrsToAidTwo_Object((1,3,6,1,4,1,2544,1,11,9,3,2,6,1,11),_CrossConnectionCapCrsToAidTwo_Type())
crossConnectionCapCrsToAidTwo.setMaxAccess(_B)
if mibBuilder.loadTexts:crossConnectionCapCrsToAidTwo.setStatus(_A)
_CrossConnectionCapCrsMcAidList_Type=FspR7SnmpLongString
_CrossConnectionCapCrsMcAidList_Object=MibTableColumn
crossConnectionCapCrsMcAidList=_CrossConnectionCapCrsMcAidList_Object((1,3,6,1,4,1,2544,1,11,9,3,2,6,1,12),_CrossConnectionCapCrsMcAidList_Type())
crossConnectionCapCrsMcAidList.setMaxAccess(_B)
if mibBuilder.loadTexts:crossConnectionCapCrsMcAidList.setStatus(_A)
_CrossConnectionCapCrsContAidList_Type=FspR7SnmpLongString
_CrossConnectionCapCrsContAidList_Object=MibTableColumn
crossConnectionCapCrsContAidList=_CrossConnectionCapCrsContAidList_Object((1,3,6,1,4,1,2544,1,11,9,3,2,6,1,13),_CrossConnectionCapCrsContAidList_Type())
crossConnectionCapCrsContAidList.setMaxAccess(_B)
if mibBuilder.loadTexts:crossConnectionCapCrsContAidList.setStatus(_A)
_CrossConnectionCapCrsContAidListTwo_Type=FspR7SnmpLongString
_CrossConnectionCapCrsContAidListTwo_Object=MibTableColumn
crossConnectionCapCrsContAidListTwo=_CrossConnectionCapCrsContAidListTwo_Object((1,3,6,1,4,1,2544,1,11,9,3,2,6,1,14),_CrossConnectionCapCrsContAidListTwo_Type())
crossConnectionCapCrsContAidListTwo.setMaxAccess(_B)
if mibBuilder.loadTexts:crossConnectionCapCrsContAidListTwo.setStatus(_A)
_CrossOpticalLineCapTable_Object=MibTable
crossOpticalLineCapTable=_CrossOpticalLineCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,2,7))
if mibBuilder.loadTexts:crossOpticalLineCapTable.setStatus(_A)
_CrossOpticalLineCapEntry_Object=MibTableRow
crossOpticalLineCapEntry=_CrossOpticalLineCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,3,2,7,1))
crossOpticalLineCapEntry.setIndexNames((0,_C,_A8),(0,_C,_A9),(0,_C,_AA),(0,_C,_AB),(0,_C,_A7),(0,_C,_AD),(0,_C,_AE),(0,_C,_AF),(0,_C,_AG),(0,_C,_AC),(0,_C,_A6))
if mibBuilder.loadTexts:crossOpticalLineCapEntry.setStatus(_A)
_CrossOpticalLineCapRowStatus_Type=FspR7RowStatusCaps
_CrossOpticalLineCapRowStatus_Object=MibTableColumn
crossOpticalLineCapRowStatus=_CrossOpticalLineCapRowStatus_Object((1,3,6,1,4,1,2544,1,11,9,3,2,7,1,1),_CrossOpticalLineCapRowStatus_Type())
crossOpticalLineCapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:crossOpticalLineCapRowStatus.setStatus(_A)
_CrossOpticalLineCapRedLineState_Type=FspR7RedLinedStateCaps
_CrossOpticalLineCapRedLineState_Object=MibTableColumn
crossOpticalLineCapRedLineState=_CrossOpticalLineCapRedLineState_Object((1,3,6,1,4,1,2544,1,11,9,3,2,7,1,2),_CrossOpticalLineCapRedLineState_Type())
crossOpticalLineCapRedLineState.setMaxAccess(_B)
if mibBuilder.loadTexts:crossOpticalLineCapRedLineState.setStatus(_A)
_CrossOpticalLineCapConn_Type=FspR7ConnCaps
_CrossOpticalLineCapConn_Object=MibTableColumn
crossOpticalLineCapConn=_CrossOpticalLineCapConn_Object((1,3,6,1,4,1,2544,1,11,9,3,2,7,1,3),_CrossOpticalLineCapConn_Type())
crossOpticalLineCapConn.setMaxAccess(_B)
if mibBuilder.loadTexts:crossOpticalLineCapConn.setStatus(_A)
_CrossOpticalLineCapCrsType_Type=FspR7TypeCrsCaps
_CrossOpticalLineCapCrsType_Object=MibTableColumn
crossOpticalLineCapCrsType=_CrossOpticalLineCapCrsType_Object((1,3,6,1,4,1,2544,1,11,9,3,2,7,1,4),_CrossOpticalLineCapCrsType_Type())
crossOpticalLineCapCrsType.setMaxAccess(_B)
if mibBuilder.loadTexts:crossOpticalLineCapCrsType.setStatus(_A)
_CrossOpticalLineCapAlias_Type=Integer32
_CrossOpticalLineCapAlias_Object=MibTableColumn
crossOpticalLineCapAlias=_CrossOpticalLineCapAlias_Object((1,3,6,1,4,1,2544,1,11,9,3,2,7,1,5),_CrossOpticalLineCapAlias_Type())
crossOpticalLineCapAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:crossOpticalLineCapAlias.setStatus(_A)
_CrossOpticalLineCapTunnelAid_Type=Integer32
_CrossOpticalLineCapTunnelAid_Object=MibTableColumn
crossOpticalLineCapTunnelAid=_CrossOpticalLineCapTunnelAid_Object((1,3,6,1,4,1,2544,1,11,9,3,2,7,1,6),_CrossOpticalLineCapTunnelAid_Type())
crossOpticalLineCapTunnelAid.setMaxAccess(_B)
if mibBuilder.loadTexts:crossOpticalLineCapTunnelAid.setStatus(_A)
_EndOfCrossOpticalLineCapTable_Type=Integer32
_EndOfCrossOpticalLineCapTable_Object=MibScalar
endOfCrossOpticalLineCapTable=_EndOfCrossOpticalLineCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,2,8),_EndOfCrossOpticalLineCapTable_Type())
endOfCrossOpticalLineCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfCrossOpticalLineCapTable.setStatus(_A)
_CrossDcnCapTable_Object=MibTable
crossDcnCapTable=_CrossDcnCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,2,9))
if mibBuilder.loadTexts:crossDcnCapTable.setStatus(_A)
_CrossDcnCapEntry_Object=MibTableRow
crossDcnCapEntry=_CrossDcnCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,3,2,9,1))
crossDcnCapEntry.setIndexNames((0,_C,_A4),(0,_C,_A5),(0,_C,_A3),(0,_C,_A2),(0,_C,_A1))
if mibBuilder.loadTexts:crossDcnCapEntry.setStatus(_A)
_CrossDcnCapRowStatus_Type=FspR7RowStatusCaps
_CrossDcnCapRowStatus_Object=MibTableColumn
crossDcnCapRowStatus=_CrossDcnCapRowStatus_Object((1,3,6,1,4,1,2544,1,11,9,3,2,9,1,1),_CrossDcnCapRowStatus_Type())
crossDcnCapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:crossDcnCapRowStatus.setStatus(_A)
_CrossDcnCapType_Type=FspR7TypeConnectionCaps
_CrossDcnCapType_Object=MibTableColumn
crossDcnCapType=_CrossDcnCapType_Object((1,3,6,1,4,1,2544,1,11,9,3,2,9,1,2),_CrossDcnCapType_Type())
crossDcnCapType.setMaxAccess(_B)
if mibBuilder.loadTexts:crossDcnCapType.setStatus(_A)
_CrossDcnCapLink_Type=SnmpAdminString
_CrossDcnCapLink_Object=MibTableColumn
crossDcnCapLink=_CrossDcnCapLink_Object((1,3,6,1,4,1,2544,1,11,9,3,2,9,1,3),_CrossDcnCapLink_Type())
crossDcnCapLink.setMaxAccess(_B)
if mibBuilder.loadTexts:crossDcnCapLink.setStatus(_A)
_CrossDcnCapEcc_Type=SnmpAdminString
_CrossDcnCapEcc_Object=MibTableColumn
crossDcnCapEcc=_CrossDcnCapEcc_Object((1,3,6,1,4,1,2544,1,11,9,3,2,9,1,4),_CrossDcnCapEcc_Type())
crossDcnCapEcc.setMaxAccess(_B)
if mibBuilder.loadTexts:crossDcnCapEcc.setStatus(_A)
_EndOfCrossDcnCapTable_Type=Integer32
_EndOfCrossDcnCapTable_Object=MibScalar
endOfCrossDcnCapTable=_EndOfCrossDcnCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,2,10),_EndOfCrossDcnCapTable_Type())
endOfCrossDcnCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfCrossDcnCapTable.setStatus(_A)
_EndOfSpecificMgmtCap_Type=Integer32
_EndOfSpecificMgmtCap_Object=MibScalar
endOfSpecificMgmtCap=_EndOfSpecificMgmtCap_Object((1,3,6,1,4,1,2544,1,11,9,3,2,10000),_EndOfSpecificMgmtCap_Type())
endOfSpecificMgmtCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfSpecificMgmtCap.setStatus(_A)
_EqptMgmtCap_ObjectIdentity=ObjectIdentity
eqptMgmtCap=_EqptMgmtCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,3,3))
_ShelfCapTable_Object=MibTable
shelfCapTable=_ShelfCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,3,1))
if mibBuilder.loadTexts:shelfCapTable.setStatus(_A)
_ShelfCapEntry_Object=MibTableRow
shelfCapEntry=_ShelfCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,3,3,1,1))
shelfCapEntry.setIndexNames((0,_C,_X),(0,_C,_Y),(0,_C,_W),(0,_C,_V),(0,_C,_U))
if mibBuilder.loadTexts:shelfCapEntry.setStatus(_A)
_ShelfCapRowStatus_Type=FspR7RowStatusCaps
_ShelfCapRowStatus_Object=MibTableColumn
shelfCapRowStatus=_ShelfCapRowStatus_Object((1,3,6,1,4,1,2544,1,11,9,3,3,1,1,1),_ShelfCapRowStatus_Type())
shelfCapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfCapRowStatus.setStatus(_A)
_ShelfCapPsuOutputPower_Type=FspR7PsuOutputPowerCaps
_ShelfCapPsuOutputPower_Object=MibTableColumn
shelfCapPsuOutputPower=_ShelfCapPsuOutputPower_Object((1,3,6,1,4,1,2544,1,11,9,3,3,1,1,2),_ShelfCapPsuOutputPower_Type())
shelfCapPsuOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfCapPsuOutputPower.setStatus(_A)
_ShelfCapType_Type=FspR7EquipmentTypeCaps
_ShelfCapType_Object=MibTableColumn
shelfCapType=_ShelfCapType_Object((1,3,6,1,4,1,2544,1,11,9,3,3,1,1,3),_ShelfCapType_Type())
shelfCapType.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfCapType.setStatus(_A)
_ShelfCapRack_Type=Integer32
_ShelfCapRack_Object=MibTableColumn
shelfCapRack=_ShelfCapRack_Object((1,3,6,1,4,1,2544,1,11,9,3,3,1,1,4),_ShelfCapRack_Type())
shelfCapRack.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfCapRack.setStatus(_A)
_ShelfCapSupply_Type=FspR7SupplyTypeCaps
_ShelfCapSupply_Object=MibTableColumn
shelfCapSupply=_ShelfCapSupply_Object((1,3,6,1,4,1,2544,1,11,9,3,3,1,1,5),_ShelfCapSupply_Type())
shelfCapSupply.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfCapSupply.setStatus(_A)
_ShelfCapBandProvision_Type=FspR7OpticalBandCaps
_ShelfCapBandProvision_Object=MibTableColumn
shelfCapBandProvision=_ShelfCapBandProvision_Object((1,3,6,1,4,1,2544,1,11,9,3,3,1,1,6),_ShelfCapBandProvision_Type())
shelfCapBandProvision.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfCapBandProvision.setStatus(_A)
_ShelfCapAdmin_Type=FspR7AdminStateCaps
_ShelfCapAdmin_Object=MibTableColumn
shelfCapAdmin=_ShelfCapAdmin_Object((1,3,6,1,4,1,2544,1,11,9,3,3,1,1,7),_ShelfCapAdmin_Type())
shelfCapAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfCapAdmin.setStatus(_A)
_ShelfCapRackNumber_Type=FspR7Unsigned32Caps
_ShelfCapRackNumber_Object=MibTableColumn
shelfCapRackNumber=_ShelfCapRackNumber_Object((1,3,6,1,4,1,2544,1,11,9,3,3,1,1,8),_ShelfCapRackNumber_Type())
shelfCapRackNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfCapRackNumber.setStatus(_A)
_ShelfCapRackOrder_Type=FspR7Unsigned32Caps
_ShelfCapRackOrder_Object=MibTableColumn
shelfCapRackOrder=_ShelfCapRackOrder_Object((1,3,6,1,4,1,2544,1,11,9,3,3,1,1,9),_ShelfCapRackOrder_Type())
shelfCapRackOrder.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfCapRackOrder.setStatus(_A)
_ShelfCapAlias_Type=Integer32
_ShelfCapAlias_Object=MibTableColumn
shelfCapAlias=_ShelfCapAlias_Object((1,3,6,1,4,1,2544,1,11,9,3,3,1,1,10),_ShelfCapAlias_Type())
shelfCapAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfCapAlias.setStatus(_A)
_ShelfCapSlot_Type=FspR7Unsigned32Caps
_ShelfCapSlot_Object=MibTableColumn
shelfCapSlot=_ShelfCapSlot_Object((1,3,6,1,4,1,2544,1,11,9,3,3,1,1,11),_ShelfCapSlot_Type())
shelfCapSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfCapSlot.setStatus(_A)
_EndOfShelfCapTable_Type=Integer32
_EndOfShelfCapTable_Object=MibScalar
endOfShelfCapTable=_EndOfShelfCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,3,2),_EndOfShelfCapTable_Type())
endOfShelfCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfShelfCapTable.setStatus(_A)
_FanCapTable_Object=MibTable
fanCapTable=_FanCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,3,3))
if mibBuilder.loadTexts:fanCapTable.setStatus(_A)
_FanCapEntry_Object=MibTableRow
fanCapEntry=_FanCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,3,3,3,1))
fanCapEntry.setIndexNames((0,_C,_X),(0,_C,_Y),(0,_C,_W),(0,_C,_V),(0,_C,_U))
if mibBuilder.loadTexts:fanCapEntry.setStatus(_A)
_FanCapRowStatus_Type=FspR7RowStatusCaps
_FanCapRowStatus_Object=MibTableColumn
fanCapRowStatus=_FanCapRowStatus_Object((1,3,6,1,4,1,2544,1,11,9,3,3,3,1,1),_FanCapRowStatus_Type())
fanCapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fanCapRowStatus.setStatus(_A)
_FanCapForceDestroy_Type=FspR7ForcedStatusCaps
_FanCapForceDestroy_Object=MibTableColumn
fanCapForceDestroy=_FanCapForceDestroy_Object((1,3,6,1,4,1,2544,1,11,9,3,3,3,1,2),_FanCapForceDestroy_Type())
fanCapForceDestroy.setMaxAccess(_B)
if mibBuilder.loadTexts:fanCapForceDestroy.setStatus(_A)
_FanCapAdmin_Type=FspR7AdminStateCaps
_FanCapAdmin_Object=MibTableColumn
fanCapAdmin=_FanCapAdmin_Object((1,3,6,1,4,1,2544,1,11,9,3,3,3,1,3),_FanCapAdmin_Type())
fanCapAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:fanCapAdmin.setStatus(_A)
_FanCapType_Type=FspR7EquipmentTypeCaps
_FanCapType_Object=MibTableColumn
fanCapType=_FanCapType_Object((1,3,6,1,4,1,2544,1,11,9,3,3,3,1,4),_FanCapType_Type())
fanCapType.setMaxAccess(_B)
if mibBuilder.loadTexts:fanCapType.setStatus(_A)
_FanCapAlias_Type=Integer32
_FanCapAlias_Object=MibTableColumn
fanCapAlias=_FanCapAlias_Object((1,3,6,1,4,1,2544,1,11,9,3,3,3,1,5),_FanCapAlias_Type())
fanCapAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:fanCapAlias.setStatus(_A)
_FanCapOutputReset_Type=FspR7TifOutputResetCaps
_FanCapOutputReset_Object=MibTableColumn
fanCapOutputReset=_FanCapOutputReset_Object((1,3,6,1,4,1,2544,1,11,9,3,3,3,1,6),_FanCapOutputReset_Type())
fanCapOutputReset.setMaxAccess(_B)
if mibBuilder.loadTexts:fanCapOutputReset.setStatus(_A)
_EndOfFanCapTable_Type=Integer32
_EndOfFanCapTable_Object=MibScalar
endOfFanCapTable=_EndOfFanCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,3,4),_EndOfFanCapTable_Type())
endOfFanCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfFanCapTable.setStatus(_A)
_PlugCapTable_Object=MibTable
plugCapTable=_PlugCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,3,5))
if mibBuilder.loadTexts:plugCapTable.setStatus(_A)
_PlugCapEntry_Object=MibTableRow
plugCapEntry=_PlugCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,3,3,5,1))
plugCapEntry.setIndexNames((0,_C,_X),(0,_C,_Y),(0,_C,_W),(0,_C,_V),(0,_C,_U))
if mibBuilder.loadTexts:plugCapEntry.setStatus(_A)
_PlugCapRowStatus_Type=FspR7RowStatusCaps
_PlugCapRowStatus_Object=MibTableColumn
plugCapRowStatus=_PlugCapRowStatus_Object((1,3,6,1,4,1,2544,1,11,9,3,3,5,1,1),_PlugCapRowStatus_Type())
plugCapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:plugCapRowStatus.setStatus(_A)
_PlugCapConnector_Type=FspR7ConnectorTypeCaps
_PlugCapConnector_Object=MibTableColumn
plugCapConnector=_PlugCapConnector_Object((1,3,6,1,4,1,2544,1,11,9,3,3,5,1,2),_PlugCapConnector_Type())
plugCapConnector.setMaxAccess(_B)
if mibBuilder.loadTexts:plugCapConnector.setStatus(_A)
_PlugCapType_Type=FspR7EquipmentTypeCaps
_PlugCapType_Object=MibTableColumn
plugCapType=_PlugCapType_Object((1,3,6,1,4,1,2544,1,11,9,3,3,5,1,3),_PlugCapType_Type())
plugCapType.setMaxAccess(_B)
if mibBuilder.loadTexts:plugCapType.setStatus(_A)
_PlugCapReach_Type=FspR7OpticalInterfaceReachCaps
_PlugCapReach_Object=MibTableColumn
plugCapReach=_PlugCapReach_Object((1,3,6,1,4,1,2544,1,11,9,3,3,5,1,4),_PlugCapReach_Type())
plugCapReach.setMaxAccess(_B)
if mibBuilder.loadTexts:plugCapReach.setStatus(_A)
_PlugCapLoopbackAttenuation_Type=FspR7Unsigned32Caps
_PlugCapLoopbackAttenuation_Object=MibTableColumn
plugCapLoopbackAttenuation=_PlugCapLoopbackAttenuation_Object((1,3,6,1,4,1,2544,1,11,9,3,3,5,1,5),_PlugCapLoopbackAttenuation_Type())
plugCapLoopbackAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:plugCapLoopbackAttenuation.setStatus(_A)
if mibBuilder.loadTexts:plugCapLoopbackAttenuation.setUnits(_F)
_PlugCapTransmitChannel_Type=FspR7ChannelIdentifierCaps
_PlugCapTransmitChannel_Object=MibTableColumn
plugCapTransmitChannel=_PlugCapTransmitChannel_Object((1,3,6,1,4,1,2544,1,11,9,3,3,5,1,6),_PlugCapTransmitChannel_Type())
plugCapTransmitChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:plugCapTransmitChannel.setStatus(_A)
_PlugCapAlias_Type=Integer32
_PlugCapAlias_Object=MibTableColumn
plugCapAlias=_PlugCapAlias_Object((1,3,6,1,4,1,2544,1,11,9,3,3,5,1,7),_PlugCapAlias_Type())
plugCapAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:plugCapAlias.setStatus(_A)
_PlugCapLaneGroup_Type=FspR7LaneGroupInventoryCaps
_PlugCapLaneGroup_Object=MibTableColumn
plugCapLaneGroup=_PlugCapLaneGroup_Object((1,3,6,1,4,1,2544,1,11,9,3,3,5,1,8),_PlugCapLaneGroup_Type())
plugCapLaneGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:plugCapLaneGroup.setStatus(_A)
_PlugCapMaxDataRate_Type=FspR7PlugDataRateCaps
_PlugCapMaxDataRate_Object=MibTableColumn
plugCapMaxDataRate=_PlugCapMaxDataRate_Object((1,3,6,1,4,1,2544,1,11,9,3,3,5,1,9),_PlugCapMaxDataRate_Type())
plugCapMaxDataRate.setMaxAccess(_B)
if mibBuilder.loadTexts:plugCapMaxDataRate.setStatus(_A)
_PlugCapThirdPartyUsage_Type=EnableStateCaps
_PlugCapThirdPartyUsage_Object=MibTableColumn
plugCapThirdPartyUsage=_PlugCapThirdPartyUsage_Object((1,3,6,1,4,1,2544,1,11,9,3,3,5,1,10),_PlugCapThirdPartyUsage_Type())
plugCapThirdPartyUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:plugCapThirdPartyUsage.setStatus(_A)
_PlugCapAdmin_Type=FspR7AdminStateCaps
_PlugCapAdmin_Object=MibTableColumn
plugCapAdmin=_PlugCapAdmin_Object((1,3,6,1,4,1,2544,1,11,9,3,3,5,1,11),_PlugCapAdmin_Type())
plugCapAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:plugCapAdmin.setStatus(_A)
_PlugCapBidirectionalChannel_Type=FspR7BidirectionalChannelCaps
_PlugCapBidirectionalChannel_Object=MibTableColumn
plugCapBidirectionalChannel=_PlugCapBidirectionalChannel_Object((1,3,6,1,4,1,2544,1,11,9,3,3,5,1,12),_PlugCapBidirectionalChannel_Type())
plugCapBidirectionalChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:plugCapBidirectionalChannel.setStatus(_A)
_PlugCapChannelSpacingProvision_Type=FspR7ChannelSpacingCaps
_PlugCapChannelSpacingProvision_Object=MibTableColumn
plugCapChannelSpacingProvision=_PlugCapChannelSpacingProvision_Object((1,3,6,1,4,1,2544,1,11,9,3,3,5,1,13),_PlugCapChannelSpacingProvision_Type())
plugCapChannelSpacingProvision.setMaxAccess(_B)
if mibBuilder.loadTexts:plugCapChannelSpacingProvision.setStatus(_A)
_EndOfPlugCapTable_Type=Integer32
_EndOfPlugCapTable_Object=MibScalar
endOfPlugCapTable=_EndOfPlugCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,3,6),_EndOfPlugCapTable_Type())
endOfPlugCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfPlugCapTable.setStatus(_A)
_ModuleCapTable_Object=MibTable
moduleCapTable=_ModuleCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7))
if mibBuilder.loadTexts:moduleCapTable.setStatus(_A)
_ModuleCapEntry_Object=MibTableRow
moduleCapEntry=_ModuleCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1))
moduleCapEntry.setIndexNames((0,_C,_X),(0,_C,_Y),(0,_C,_W),(0,_C,_V),(0,_C,_U))
if mibBuilder.loadTexts:moduleCapEntry.setStatus(_A)
_ModuleCapRowStatus_Type=FspR7RowStatusCaps
_ModuleCapRowStatus_Object=MibTableColumn
moduleCapRowStatus=_ModuleCapRowStatus_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,1),_ModuleCapRowStatus_Type())
moduleCapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapRowStatus.setStatus(_A)
_ModuleCapForceDestroy_Type=FspR7ForcedStatusCaps
_ModuleCapForceDestroy_Object=MibTableColumn
moduleCapForceDestroy=_ModuleCapForceDestroy_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,2),_ModuleCapForceDestroy_Type())
moduleCapForceDestroy.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapForceDestroy.setStatus(_A)
_ModuleCapPsuOutputPower_Type=FspR7PsuOutputPowerCaps
_ModuleCapPsuOutputPower_Object=MibTableColumn
moduleCapPsuOutputPower=_ModuleCapPsuOutputPower_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,3),_ModuleCapPsuOutputPower_Type())
moduleCapPsuOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapPsuOutputPower.setStatus(_A)
_ModuleCapPower_Type=FspR7EdfaOutputPowerRatingCaps
_ModuleCapPower_Object=MibTableColumn
moduleCapPower=_ModuleCapPower_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,4),_ModuleCapPower_Type())
moduleCapPower.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapPower.setStatus(_A)
_ModuleCapReach_Type=FspR7OpticalInterfaceReachCaps
_ModuleCapReach_Object=MibTableColumn
moduleCapReach=_ModuleCapReach_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,5),_ModuleCapReach_Type())
moduleCapReach.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapReach.setStatus(_A)
_ModuleCapInitEqlz_Type=FspR7InitEqualizationCaps
_ModuleCapInitEqlz_Object=MibTableColumn
moduleCapInitEqlz=_ModuleCapInitEqlz_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,6),_ModuleCapInitEqlz_Type())
moduleCapInitEqlz.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapInitEqlz.setStatus(_A)
_ModuleCapLanAid_Type=SnmpAdminString
_ModuleCapLanAid_Object=MibTableColumn
moduleCapLanAid=_ModuleCapLanAid_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,7),_ModuleCapLanAid_Type())
moduleCapLanAid.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapLanAid.setStatus(_A)
_ModuleCapType_Type=FspR7EquipmentTypeCaps
_ModuleCapType_Object=MibTableColumn
moduleCapType=_ModuleCapType_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,8),_ModuleCapType_Type())
moduleCapType.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapType.setStatus(_A)
_ModuleCapMapping_Type=FspR7MappingCaps
_ModuleCapMapping_Object=MibTableColumn
moduleCapMapping=_ModuleCapMapping_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,9),_ModuleCapMapping_Type())
moduleCapMapping.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapMapping.setStatus(_A)
_ModuleCapGainRange_Type=FspR7GainRangeCaps
_ModuleCapGainRange_Object=MibTableColumn
moduleCapGainRange=_ModuleCapGainRange_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,10),_ModuleCapGainRange_Type())
moduleCapGainRange.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapGainRange.setStatus(_A)
_ModuleCapSfProvision_Type=FspR7SingleFiberLocationCaps
_ModuleCapSfProvision_Object=MibTableColumn
moduleCapSfProvision=_ModuleCapSfProvision_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,11),_ModuleCapSfProvision_Type())
moduleCapSfProvision.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapSfProvision.setStatus(_A)
_ModuleCapCapabilityLevelProvision_Type=FspR7CapInventoryCaps
_ModuleCapCapabilityLevelProvision_Object=MibTableColumn
moduleCapCapabilityLevelProvision=_ModuleCapCapabilityLevelProvision_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,12),_ModuleCapCapabilityLevelProvision_Type())
moduleCapCapabilityLevelProvision.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapCapabilityLevelProvision.setStatus(_A)
_ModuleCapDCFiberType_Type=FspR7DCFiberTypeCaps
_ModuleCapDCFiberType_Object=MibTableColumn
moduleCapDCFiberType=_ModuleCapDCFiberType_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,13),_ModuleCapDCFiberType_Type())
moduleCapDCFiberType.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapDCFiberType.setStatus(_A)
_ModuleCapChannelsProvision_Type=FspR7NumberOfChannelsProvCaps
_ModuleCapChannelsProvision_Object=MibTableColumn
moduleCapChannelsProvision=_ModuleCapChannelsProvision_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,14),_ModuleCapChannelsProvision_Type())
moduleCapChannelsProvision.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapChannelsProvision.setStatus(_A)
_ModuleCapFiberDetect_Type=FspR7FiberDetectCaps
_ModuleCapFiberDetect_Object=MibTableColumn
moduleCapFiberDetect=_ModuleCapFiberDetect_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,15),_ModuleCapFiberDetect_Type())
moduleCapFiberDetect.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapFiberDetect.setStatus(_A)
_ModuleCapSupply_Type=FspR7SupplyTypeCaps
_ModuleCapSupply_Object=MibTableColumn
moduleCapSupply=_ModuleCapSupply_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,16),_ModuleCapSupply_Type())
moduleCapSupply.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapSupply.setStatus(_A)
_ModuleCapGroup_Type=FspR7OpticalGroupCaps
_ModuleCapGroup_Object=MibTableColumn
moduleCapGroup=_ModuleCapGroup_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,17),_ModuleCapGroup_Type())
moduleCapGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapGroup.setStatus(_A)
_ModuleCapDeploy_Type=FspR7DeploymentScenarioCaps
_ModuleCapDeploy_Object=MibTableColumn
moduleCapDeploy=_ModuleCapDeploy_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,18),_ModuleCapDeploy_Type())
moduleCapDeploy.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapDeploy.setStatus(_A)
_ModuleCapLagSysPrio_Type=FspR7Unsigned32Caps
_ModuleCapLagSysPrio_Object=MibTableColumn
moduleCapLagSysPrio=_ModuleCapLagSysPrio_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,19),_ModuleCapLagSysPrio_Type())
moduleCapLagSysPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapLagSysPrio.setStatus(_A)
_ModuleCapTransmitChannel_Type=FspR7ChannelIdentifierCaps
_ModuleCapTransmitChannel_Object=MibTableColumn
moduleCapTransmitChannel=_ModuleCapTransmitChannel_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,20),_ModuleCapTransmitChannel_Type())
moduleCapTransmitChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapTransmitChannel.setStatus(_A)
_ModuleCapBand_Type=FspR7OpticalBandCaps
_ModuleCapBand_Object=MibTableColumn
moduleCapBand=_ModuleCapBand_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,21),_ModuleCapBand_Type())
moduleCapBand.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapBand.setStatus(_A)
_ModuleCapTrafficDirection_Type=FspR7TrafficDirectionCaps
_ModuleCapTrafficDirection_Object=MibTableColumn
moduleCapTrafficDirection=_ModuleCapTrafficDirection_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,22),_ModuleCapTrafficDirection_Type())
moduleCapTrafficDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapTrafficDirection.setStatus(_A)
_ModuleCapIpAddr_Type=FspR7YesNo
_ModuleCapIpAddr_Object=MibTableColumn
moduleCapIpAddr=_ModuleCapIpAddr_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,23),_ModuleCapIpAddr_Type())
moduleCapIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapIpAddr.setStatus(_A)
_ModuleCapDispersionCompensation_Type=FspR7DispersionCompensationCaps
_ModuleCapDispersionCompensation_Object=MibTableColumn
moduleCapDispersionCompensation=_ModuleCapDispersionCompensation_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,24),_ModuleCapDispersionCompensation_Type())
moduleCapDispersionCompensation.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapDispersionCompensation.setStatus(_A)
_ModuleCapActivateDetect_Type=FspR7YesNoCaps
_ModuleCapActivateDetect_Object=MibTableColumn
moduleCapActivateDetect=_ModuleCapActivateDetect_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,25),_ModuleCapActivateDetect_Type())
moduleCapActivateDetect.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapActivateDetect.setStatus(_A)
_ModuleCapOscUsage_Type=FspR7OscUsageCaps
_ModuleCapOscUsage_Object=MibTableColumn
moduleCapOscUsage=_ModuleCapOscUsage_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,26),_ModuleCapOscUsage_Type())
moduleCapOscUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapOscUsage.setStatus(_A)
_ModuleCapAdmin_Type=FspR7AdminStateCaps
_ModuleCapAdmin_Object=MibTableColumn
moduleCapAdmin=_ModuleCapAdmin_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,27),_ModuleCapAdmin_Type())
moduleCapAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapAdmin.setStatus(_A)
_ModuleCapScrambling_Type=FspR7ScramblingCaps
_ModuleCapScrambling_Object=MibTableColumn
moduleCapScrambling=_ModuleCapScrambling_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,28),_ModuleCapScrambling_Type())
moduleCapScrambling.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapScrambling.setStatus(_A)
_ModuleCapChannelsNumber_Type=FspR7NumberOfChannelsCaps
_ModuleCapChannelsNumber_Object=MibTableColumn
moduleCapChannelsNumber=_ModuleCapChannelsNumber_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,29),_ModuleCapChannelsNumber_Type())
moduleCapChannelsNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapChannelsNumber.setStatus(_A)
_ModuleCapChannelSpacingProvision_Type=FspR7ChannelSpacingCaps
_ModuleCapChannelSpacingProvision_Object=MibTableColumn
moduleCapChannelSpacingProvision=_ModuleCapChannelSpacingProvision_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,30),_ModuleCapChannelSpacingProvision_Type())
moduleCapChannelSpacingProvision.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapChannelSpacingProvision.setStatus(_A)
_ModuleCapMode_Type=FspR7TransmissionModeCaps
_ModuleCapMode_Object=MibTableColumn
moduleCapMode=_ModuleCapMode_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,31),_ModuleCapMode_Type())
moduleCapMode.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapMode.setStatus(_A)
_ModuleCapSubBandProvision_Type=FspR7OpticalSubBandCaps
_ModuleCapSubBandProvision_Object=MibTableColumn
moduleCapSubBandProvision=_ModuleCapSubBandProvision_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,32),_ModuleCapSubBandProvision_Type())
moduleCapSubBandProvision.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapSubBandProvision.setStatus(_A)
_ModuleCapAlias_Type=Integer32
_ModuleCapAlias_Object=MibTableColumn
moduleCapAlias=_ModuleCapAlias_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,33),_ModuleCapAlias_Type())
moduleCapAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapAlias.setStatus(_A)
_ModuleCapFiberType_Type=FspR7OpticalFiberTypeCaps
_ModuleCapFiberType_Object=MibTableColumn
moduleCapFiberType=_ModuleCapFiberType_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,34),_ModuleCapFiberType_Type())
moduleCapFiberType.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapFiberType.setStatus(_A)
_ModuleCapChannelSpacing_Type=FspR7ChannelSpacingCaps
_ModuleCapChannelSpacing_Object=MibTableColumn
moduleCapChannelSpacing=_ModuleCapChannelSpacing_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,35),_ModuleCapChannelSpacing_Type())
moduleCapChannelSpacing.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapChannelSpacing.setStatus(_A)
_ModuleCapOutputReset_Type=FspR7TifOutputResetCaps
_ModuleCapOutputReset_Object=MibTableColumn
moduleCapOutputReset=_ModuleCapOutputReset_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,36),_ModuleCapOutputReset_Type())
moduleCapOutputReset.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapOutputReset.setStatus(_A)
_ModuleCapRoadmNumber_Type=FspR7RoadmNumberCaps
_ModuleCapRoadmNumber_Object=MibTableColumn
moduleCapRoadmNumber=_ModuleCapRoadmNumber_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,37),_ModuleCapRoadmNumber_Type())
moduleCapRoadmNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapRoadmNumber.setStatus(_A)
_ModuleCapTopology_Type=FspR7TopologyCaps
_ModuleCapTopology_Object=MibTableColumn
moduleCapTopology=_ModuleCapTopology_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,38),_ModuleCapTopology_Type())
moduleCapTopology.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapTopology.setStatus(_A)
_ModuleCapForceConfig_Type=FspR7ForceConfigCaps
_ModuleCapForceConfig_Object=MibTableColumn
moduleCapForceConfig=_ModuleCapForceConfig_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,39),_ModuleCapForceConfig_Type())
moduleCapForceConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapForceConfig.setStatus(_A)
_ModuleCapMuxMethod_Type=FspR7MuxMethodCaps
_ModuleCapMuxMethod_Object=MibTableColumn
moduleCapMuxMethod=_ModuleCapMuxMethod_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,40),_ModuleCapMuxMethod_Type())
moduleCapMuxMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapMuxMethod.setStatus(_A)
_ModuleCapNdpCleanup_Type=FspR7NdpCleanupCaps
_ModuleCapNdpCleanup_Object=MibTableColumn
moduleCapNdpCleanup=_ModuleCapNdpCleanup_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,41),_ModuleCapNdpCleanup_Type())
moduleCapNdpCleanup.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapNdpCleanup.setStatus(_A)
_ModuleCapRstp_Type=FspR7EnableDisableCaps
_ModuleCapRstp_Object=MibTableColumn
moduleCapRstp=_ModuleCapRstp_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,42),_ModuleCapRstp_Type())
moduleCapRstp.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapRstp.setStatus(_A)
_ModuleCapRemoteReset_Type=FspR7RlsManCaps
_ModuleCapRemoteReset_Object=MibTableColumn
moduleCapRemoteReset=_ModuleCapRemoteReset_Object((1,3,6,1,4,1,2544,1,11,9,3,3,7,1,43),_ModuleCapRemoteReset_Type())
moduleCapRemoteReset.setMaxAccess(_B)
if mibBuilder.loadTexts:moduleCapRemoteReset.setStatus(_A)
_EndOfModuleCap_Type=Integer32
_EndOfModuleCap_Object=MibScalar
endOfModuleCap=_EndOfModuleCap_Object((1,3,6,1,4,1,2544,1,11,9,3,3,8),_EndOfModuleCap_Type())
endOfModuleCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfModuleCap.setStatus(_A)
_ProtectionCableCapTable_Object=MibTable
protectionCableCapTable=_ProtectionCableCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,3,9))
if mibBuilder.loadTexts:protectionCableCapTable.setStatus(_A)
_ProtectionCableCapEntry_Object=MibTableRow
protectionCableCapEntry=_ProtectionCableCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,3,3,9,1))
protectionCableCapEntry.setIndexNames((0,_C,_AY),(0,_C,_AZ),(0,_C,_Aa),(0,_C,_Ab),(0,_C,_AX))
if mibBuilder.loadTexts:protectionCableCapEntry.setStatus(_A)
_ProtectionCableCapRowStatus_Type=FspR7RowStatusCaps
_ProtectionCableCapRowStatus_Object=MibTableColumn
protectionCableCapRowStatus=_ProtectionCableCapRowStatus_Object((1,3,6,1,4,1,2544,1,11,9,3,3,9,1,1),_ProtectionCableCapRowStatus_Type())
protectionCableCapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:protectionCableCapRowStatus.setStatus(_A)
_ProtectionCableCapType_Type=FspR7YcableTypeCaps
_ProtectionCableCapType_Object=MibTableColumn
protectionCableCapType=_ProtectionCableCapType_Object((1,3,6,1,4,1,2544,1,11,9,3,3,9,1,2),_ProtectionCableCapType_Type())
protectionCableCapType.setMaxAccess(_B)
if mibBuilder.loadTexts:protectionCableCapType.setStatus(_A)
_EndOfProtectionCableCap_Type=Integer32
_EndOfProtectionCableCap_Object=MibScalar
endOfProtectionCableCap=_EndOfProtectionCableCap_Object((1,3,6,1,4,1,2544,1,11,9,3,3,10),_EndOfProtectionCableCap_Type())
endOfProtectionCableCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfProtectionCableCap.setStatus(_A)
_FilterCableCapTable_Object=MibTable
filterCableCapTable=_FilterCableCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,3,11))
if mibBuilder.loadTexts:filterCableCapTable.setStatus(_A)
_FilterCableCapEntry_Object=MibTableRow
filterCableCapEntry=_FilterCableCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,3,3,11,1))
filterCableCapEntry.setIndexNames((0,_C,_AS),(0,_C,_AT),(0,_C,_AU),(0,_C,_AV),(0,_C,_AR))
if mibBuilder.loadTexts:filterCableCapEntry.setStatus(_A)
_FilterCableCapRowStatus_Type=FspR7RowStatusCaps
_FilterCableCapRowStatus_Object=MibTableColumn
filterCableCapRowStatus=_FilterCableCapRowStatus_Object((1,3,6,1,4,1,2544,1,11,9,3,3,11,1,1),_FilterCableCapRowStatus_Type())
filterCableCapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:filterCableCapRowStatus.setStatus(_A)
_FilterCableCapType_Type=FspR7FltrCableTypeCaps
_FilterCableCapType_Object=MibTableColumn
filterCableCapType=_FilterCableCapType_Object((1,3,6,1,4,1,2544,1,11,9,3,3,11,1,2),_FilterCableCapType_Type())
filterCableCapType.setMaxAccess(_B)
if mibBuilder.loadTexts:filterCableCapType.setStatus(_A)
_EndOfFilterCableCap_Type=Integer32
_EndOfFilterCableCap_Object=MibScalar
endOfFilterCableCap=_EndOfFilterCableCap_Object((1,3,6,1,4,1,2544,1,11,9,3,3,12),_EndOfFilterCableCap_Type())
endOfFilterCableCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfFilterCableCap.setStatus(_A)
_EndOfEqptMgmCap_Type=Integer32
_EndOfEqptMgmCap_Object=MibScalar
endOfEqptMgmCap=_EndOfEqptMgmCap_Object((1,3,6,1,4,1,2544,1,11,9,3,3,10000),_EndOfEqptMgmCap_Type())
endOfEqptMgmCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfEqptMgmCap.setStatus(_A)
_FacilityMgmtCap_ObjectIdentity=ObjectIdentity
facilityMgmtCap=_FacilityMgmtCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,3,4))
_PhysicalPortCapTable_Object=MibTable
physicalPortCapTable=_PhysicalPortCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1))
if mibBuilder.loadTexts:physicalPortCapTable.setStatus(_A)
_PhysicalPortCapEntry_Object=MibTableRow
physicalPortCapEntry=_PhysicalPortCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1))
physicalPortCapEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_K),(0,_C,_J),(0,_C,_I))
if mibBuilder.loadTexts:physicalPortCapEntry.setStatus(_A)
_PhysicalPortCapRowStatus_Type=FspR7RowStatusCaps
_PhysicalPortCapRowStatus_Object=MibTableColumn
physicalPortCapRowStatus=_PhysicalPortCapRowStatus_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,1),_PhysicalPortCapRowStatus_Type())
physicalPortCapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapRowStatus.setStatus(_A)
_PhysicalPortCapType_Type=FspR7InterfaceTypeCaps
_PhysicalPortCapType_Object=MibTableColumn
physicalPortCapType=_PhysicalPortCapType_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,2),_PhysicalPortCapType_Type())
physicalPortCapType.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapType.setStatus(_A)
_PhysicalPortCapAdmin_Type=FspR7AdminStateCaps
_PhysicalPortCapAdmin_Object=MibTableColumn
physicalPortCapAdmin=_PhysicalPortCapAdmin_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,3),_PhysicalPortCapAdmin_Type())
physicalPortCapAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapAdmin.setStatus(_A)
_PhysicalPortCapAlias_Type=Integer32
_PhysicalPortCapAlias_Object=MibTableColumn
physicalPortCapAlias=_PhysicalPortCapAlias_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,4),_PhysicalPortCapAlias_Type())
physicalPortCapAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapAlias.setStatus(_A)
_PhysicalPortCapAlsMode_Type=FspR7AlsModeCaps
_PhysicalPortCapAlsMode_Object=MibTableColumn
physicalPortCapAlsMode=_PhysicalPortCapAlsMode_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,5),_PhysicalPortCapAlsMode_Type())
physicalPortCapAlsMode.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapAlsMode.setStatus(_A)
_PhysicalPortCapAutoThresReset_Type=FspR7AutoThresResetCaps
_PhysicalPortCapAutoThresReset_Object=MibTableColumn
physicalPortCapAutoThresReset=_PhysicalPortCapAutoThresReset_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,6),_PhysicalPortCapAutoThresReset_Type())
physicalPortCapAutoThresReset.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapAutoThresReset.setStatus(_A)
_PhysicalPortCapAutonegotiation_Type=EnableStateCaps
_PhysicalPortCapAutonegotiation_Object=MibTableColumn
physicalPortCapAutonegotiation=_PhysicalPortCapAutonegotiation_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,7),_PhysicalPortCapAutonegotiation_Type())
physicalPortCapAutonegotiation.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapAutonegotiation.setStatus(_A)
_PhysicalPortCapBehaviour_Type=FspR7PortBehaviourCaps
_PhysicalPortCapBehaviour_Object=MibTableColumn
physicalPortCapBehaviour=_PhysicalPortCapBehaviour_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,8),_PhysicalPortCapBehaviour_Type())
physicalPortCapBehaviour.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapBehaviour.setStatus(_A)
_PhysicalPortCapDispertionConfig_Type=FspR7DispersionConfigCaps
_PhysicalPortCapDispertionConfig_Object=MibTableColumn
physicalPortCapDispertionConfig=_PhysicalPortCapDispertionConfig_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,9),_PhysicalPortCapDispertionConfig_Type())
physicalPortCapDispertionConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapDispertionConfig.setStatus(_A)
_PhysicalPortCapDispersionSetting_Type=FspR7Integer32Caps
_PhysicalPortCapDispersionSetting_Object=MibTableColumn
physicalPortCapDispersionSetting=_PhysicalPortCapDispersionSetting_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,10),_PhysicalPortCapDispersionSetting_Type())
physicalPortCapDispersionSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapDispersionSetting.setStatus(_A)
if mibBuilder.loadTexts:physicalPortCapDispersionSetting.setUnits(_N)
_PhysicalPortCapDispersionMode_Type=FspR7DispersionModesCaps
_PhysicalPortCapDispersionMode_Object=MibTableColumn
physicalPortCapDispersionMode=_PhysicalPortCapDispersionMode_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,11),_PhysicalPortCapDispersionMode_Type())
physicalPortCapDispersionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapDispersionMode.setStatus(_A)
_PhysicalPortCapChannelProv_Type=FspR7ChannelIdentifierCaps
_PhysicalPortCapChannelProv_Object=MibTableColumn
physicalPortCapChannelProv=_PhysicalPortCapChannelProv_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,12),_PhysicalPortCapChannelProv_Type())
physicalPortCapChannelProv.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapChannelProv.setStatus(_A)
_PhysicalPortCapWdmRxChannel_Type=FspR7ChannelIdentifierCaps
_PhysicalPortCapWdmRxChannel_Object=MibTableColumn
physicalPortCapWdmRxChannel=_PhysicalPortCapWdmRxChannel_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,13),_PhysicalPortCapWdmRxChannel_Type())
physicalPortCapWdmRxChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapWdmRxChannel.setStatus(_A)
_PhysicalPortCapCodeGain_Type=FspR7CodeGainCaps
_PhysicalPortCapCodeGain_Object=MibTableColumn
physicalPortCapCodeGain=_PhysicalPortCapCodeGain_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,14),_PhysicalPortCapCodeGain_Type())
physicalPortCapCodeGain.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapCodeGain.setStatus(_A)
_PhysicalPortCapXfpDecisionThres_Type=FspR7XfpDecisionThresCaps
_PhysicalPortCapXfpDecisionThres_Object=MibTableColumn
physicalPortCapXfpDecisionThres=_PhysicalPortCapXfpDecisionThres_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,15),_PhysicalPortCapXfpDecisionThres_Type())
physicalPortCapXfpDecisionThres.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapXfpDecisionThres.setStatus(_A)
_PhysicalPortCapDisparityCorrection_Type=EnableStateCaps
_PhysicalPortCapDisparityCorrection_Object=MibTableColumn
physicalPortCapDisparityCorrection=_PhysicalPortCapDisparityCorrection_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,16),_PhysicalPortCapDisparityCorrection_Type())
physicalPortCapDisparityCorrection.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapDisparityCorrection.setStatus(_A)
_PhysicalPortCapEqlzAdmin_Type=FspR7EqlzAdminStateCaps
_PhysicalPortCapEqlzAdmin_Object=MibTableColumn
physicalPortCapEqlzAdmin=_PhysicalPortCapEqlzAdmin_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,17),_PhysicalPortCapEqlzAdmin_Type())
physicalPortCapEqlzAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapEqlzAdmin.setStatus(_A)
_PhysicalPortCapErrorForwarding_Type=FspR7ErrorFwdModeCaps
_PhysicalPortCapErrorForwarding_Object=MibTableColumn
physicalPortCapErrorForwarding=_PhysicalPortCapErrorForwarding_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,18),_PhysicalPortCapErrorForwarding_Type())
physicalPortCapErrorForwarding.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapErrorForwarding.setStatus(_A)
_PhysicalPortCapFecType_Type=FspR7FecTypeCaps
_PhysicalPortCapFecType_Object=MibTableColumn
physicalPortCapFecType=_PhysicalPortCapFecType_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,19),_PhysicalPortCapFecType_Type())
physicalPortCapFecType.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapFecType.setStatus(_A)
_PhysicalPortCapFarEndCommunication_Type=FspR7YesNoCaps
_PhysicalPortCapFarEndCommunication_Object=MibTableColumn
physicalPortCapFarEndCommunication=_PhysicalPortCapFarEndCommunication_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,20),_PhysicalPortCapFarEndCommunication_Type())
physicalPortCapFarEndCommunication.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapFarEndCommunication.setStatus(_A)
_PhysicalPortCapFlowControl_Type=FspR7FlowControlModeCaps
_PhysicalPortCapFlowControl_Object=MibTableColumn
physicalPortCapFlowControl=_PhysicalPortCapFlowControl_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,21),_PhysicalPortCapFlowControl_Type())
physicalPortCapFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapFlowControl.setStatus(_A)
_PhysicalPortCapForceLaserOn_Type=FspR7LaserForcedOperationCaps
_PhysicalPortCapForceLaserOn_Object=MibTableColumn
physicalPortCapForceLaserOn=_PhysicalPortCapForceLaserOn_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,22),_PhysicalPortCapForceLaserOn_Type())
physicalPortCapForceLaserOn.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapForceLaserOn.setStatus(_A)
_PhysicalPortCapInhibitSwitchToProt_Type=FspR7YesNoCaps
_PhysicalPortCapInhibitSwitchToProt_Object=MibTableColumn
physicalPortCapInhibitSwitchToProt=_PhysicalPortCapInhibitSwitchToProt_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,23),_PhysicalPortCapInhibitSwitchToProt_Type())
physicalPortCapInhibitSwitchToProt.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapInhibitSwitchToProt.setStatus(_A)
_PhysicalPortCapInhibitSwitchToWork_Type=FspR7YesNoCaps
_PhysicalPortCapInhibitSwitchToWork_Object=MibTableColumn
physicalPortCapInhibitSwitchToWork=_PhysicalPortCapInhibitSwitchToWork_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,24),_PhysicalPortCapInhibitSwitchToWork_Type())
physicalPortCapInhibitSwitchToWork.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapInhibitSwitchToWork.setStatus(_A)
_PhysicalPortCapLaneChannelSetting_Type=FspR7ChannelIdentifierCaps
_PhysicalPortCapLaneChannelSetting_Object=MibTableColumn
physicalPortCapLaneChannelSetting=_PhysicalPortCapLaneChannelSetting_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,25),_PhysicalPortCapLaneChannelSetting_Type())
physicalPortCapLaneChannelSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapLaneChannelSetting.setStatus(_A)
_PhysicalPortCapLoopConfig_Type=LoopConfigCaps
_PhysicalPortCapLoopConfig_Object=MibTableColumn
physicalPortCapLoopConfig=_PhysicalPortCapLoopConfig_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,26),_PhysicalPortCapLoopConfig_Type())
physicalPortCapLoopConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapLoopConfig.setStatus(_A)
_PhysicalPortCapLaserDelayTimer_Type=FspR7LaserDelayTimerCaps
_PhysicalPortCapLaserDelayTimer_Object=MibTableColumn
physicalPortCapLaserDelayTimer=_PhysicalPortCapLaserDelayTimer_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,27),_PhysicalPortCapLaserDelayTimer_Type())
physicalPortCapLaserDelayTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapLaserDelayTimer.setStatus(_A)
_PhysicalPortCapLaserOffTimer_Type=FspR7Unsigned32Caps
_PhysicalPortCapLaserOffTimer_Object=MibTableColumn
physicalPortCapLaserOffTimer=_PhysicalPortCapLaserOffTimer_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,28),_PhysicalPortCapLaserOffTimer_Type())
physicalPortCapLaserOffTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapLaserOffTimer.setStatus(_A)
if mibBuilder.loadTexts:physicalPortCapLaserOffTimer.setUnits(_O)
_PhysicalPortCapLaserOnTimer_Type=FspR7Unsigned32Caps
_PhysicalPortCapLaserOnTimer_Object=MibTableColumn
physicalPortCapLaserOnTimer=_PhysicalPortCapLaserOnTimer_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,29),_PhysicalPortCapLaserOnTimer_Type())
physicalPortCapLaserOnTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapLaserOnTimer.setStatus(_A)
if mibBuilder.loadTexts:physicalPortCapLaserOnTimer.setUnits(_O)
_PhysicalPortCapLaserOffDelayFunction_Type=EnableStateCaps
_PhysicalPortCapLaserOffDelayFunction_Object=MibTableColumn
physicalPortCapLaserOffDelayFunction=_PhysicalPortCapLaserOffDelayFunction_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,30),_PhysicalPortCapLaserOffDelayFunction_Type())
physicalPortCapLaserOffDelayFunction.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapLaserOffDelayFunction.setStatus(_A)
_PhysicalPortCapAutoPTassignment_Type=FspR7ManualAutoCaps
_PhysicalPortCapAutoPTassignment_Object=MibTableColumn
physicalPortCapAutoPTassignment=_PhysicalPortCapAutoPTassignment_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,31),_PhysicalPortCapAutoPTassignment_Type())
physicalPortCapAutoPTassignment.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapAutoPTassignment.setStatus(_A)
_PhysicalPortCapTributarySlotMethod_Type=FspR7ManualAutoCaps
_PhysicalPortCapTributarySlotMethod_Object=MibTableColumn
physicalPortCapTributarySlotMethod=_PhysicalPortCapTributarySlotMethod_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,32),_PhysicalPortCapTributarySlotMethod_Type())
physicalPortCapTributarySlotMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTributarySlotMethod.setStatus(_A)
_PhysicalPortCapInitiateEqualization_Type=FspR7InitEqualizationCaps
_PhysicalPortCapInitiateEqualization_Object=MibTableColumn
physicalPortCapInitiateEqualization=_PhysicalPortCapInitiateEqualization_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,33),_PhysicalPortCapInitiateEqualization_Type())
physicalPortCapInitiateEqualization.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapInitiateEqualization.setStatus(_A)
_PhysicalPortCapLossAttenuation_Type=FspR7LossAttenuationCaps
_PhysicalPortCapLossAttenuation_Object=MibTableColumn
physicalPortCapLossAttenuation=_PhysicalPortCapLossAttenuation_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,34),_PhysicalPortCapLossAttenuation_Type())
physicalPortCapLossAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapLossAttenuation.setStatus(_A)
_PhysicalPortCapOpticalSetPoint_Type=FspR7Integer32Caps
_PhysicalPortCapOpticalSetPoint_Object=MibTableColumn
physicalPortCapOpticalSetPoint=_PhysicalPortCapOpticalSetPoint_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,35),_PhysicalPortCapOpticalSetPoint_Type())
physicalPortCapOpticalSetPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapOpticalSetPoint.setStatus(_A)
if mibBuilder.loadTexts:physicalPortCapOpticalSetPoint.setUnits(_E)
_PhysicalPortCapDataLayerPmReset_Type=FspR7PmResetCaps
_PhysicalPortCapDataLayerPmReset_Object=MibTableColumn
physicalPortCapDataLayerPmReset=_PhysicalPortCapDataLayerPmReset_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,36),_PhysicalPortCapDataLayerPmReset_Type())
physicalPortCapDataLayerPmReset.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapDataLayerPmReset.setStatus(_A)
_PhysicalPortCapPrbsPmReset_Type=FspR7PrbsPmResetCaps
_PhysicalPortCapPrbsPmReset_Object=MibTableColumn
physicalPortCapPrbsPmReset=_PhysicalPortCapPrbsPmReset_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,37),_PhysicalPortCapPrbsPmReset_Type())
physicalPortCapPrbsPmReset.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapPrbsPmReset.setStatus(_A)
_PhysicalPortCapTestPrbsRcvMode_Type=FspR7PRBSTestCaps
_PhysicalPortCapTestPrbsRcvMode_Object=MibTableColumn
physicalPortCapTestPrbsRcvMode=_PhysicalPortCapTestPrbsRcvMode_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,38),_PhysicalPortCapTestPrbsRcvMode_Type())
physicalPortCapTestPrbsRcvMode.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTestPrbsRcvMode.setStatus(_A)
_PhysicalPortCapTestPrbsTrmtMode_Type=FspR7PRBSTestCaps
_PhysicalPortCapTestPrbsTrmtMode_Object=MibTableColumn
physicalPortCapTestPrbsTrmtMode=_PhysicalPortCapTestPrbsTrmtMode_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,39),_PhysicalPortCapTestPrbsTrmtMode_Type())
physicalPortCapTestPrbsTrmtMode.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTestPrbsTrmtMode.setStatus(_A)
_PhysicalPortCapSwitchCommand_Type=FspR7APSCommandCaps
_PhysicalPortCapSwitchCommand_Object=MibTableColumn
physicalPortCapSwitchCommand=_PhysicalPortCapSwitchCommand_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,40),_PhysicalPortCapSwitchCommand_Type())
physicalPortCapSwitchCommand.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapSwitchCommand.setStatus(_A)
_PhysicalPortCapOpuPayloadType_Type=FspR7OpuPayloadTypeCaps
_PhysicalPortCapOpuPayloadType_Object=MibTableColumn
physicalPortCapOpuPayloadType=_PhysicalPortCapOpuPayloadType_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,41),_PhysicalPortCapOpuPayloadType_Type())
physicalPortCapOpuPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapOpuPayloadType.setStatus(_A)
_PhysicalPortCapSigDegThresSonetLine_Type=FspR7BERThresholdCaps
_PhysicalPortCapSigDegThresSonetLine_Object=MibTableColumn
physicalPortCapSigDegThresSonetLine=_PhysicalPortCapSigDegThresSonetLine_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,42),_PhysicalPortCapSigDegThresSonetLine_Type())
physicalPortCapSigDegThresSonetLine.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapSigDegThresSonetLine.setStatus(_A)
_PhysicalPortCapSigDegThresSdhMs_Type=FspR7Unsigned32Caps
_PhysicalPortCapSigDegThresSdhMs_Object=MibTableColumn
physicalPortCapSigDegThresSdhMs=_PhysicalPortCapSigDegThresSdhMs_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,43),_PhysicalPortCapSigDegThresSdhMs_Type())
physicalPortCapSigDegThresSdhMs.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapSigDegThresSdhMs.setStatus(_A)
if mibBuilder.loadTexts:physicalPortCapSigDegThresSdhMs.setUnits(_G)
_PhysicalPortCapSigDegThresOtu_Type=FspR7Integer32Caps
_PhysicalPortCapSigDegThresOtu_Object=MibTableColumn
physicalPortCapSigDegThresOtu=_PhysicalPortCapSigDegThresOtu_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,44),_PhysicalPortCapSigDegThresOtu_Type())
physicalPortCapSigDegThresOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapSigDegThresOtu.setStatus(_A)
if mibBuilder.loadTexts:physicalPortCapSigDegThresOtu.setUnits(_G)
_PhysicalPortCapSigDegThresOdu_Type=FspR7Integer32Caps
_PhysicalPortCapSigDegThresOdu_Object=MibTableColumn
physicalPortCapSigDegThresOdu=_PhysicalPortCapSigDegThresOdu_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,45),_PhysicalPortCapSigDegThresOdu_Type())
physicalPortCapSigDegThresOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapSigDegThresOdu.setStatus(_A)
if mibBuilder.loadTexts:physicalPortCapSigDegThresOdu.setUnits(_G)
_PhysicalPortCapSigDegThreshold_Type=FspR7Unsigned32Caps
_PhysicalPortCapSigDegThreshold_Object=MibTableColumn
physicalPortCapSigDegThreshold=_PhysicalPortCapSigDegThreshold_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,46),_PhysicalPortCapSigDegThreshold_Type())
physicalPortCapSigDegThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapSigDegThreshold.setStatus(_A)
_PhysicalPortCapSigDegPcslThreshold_Type=FspR7Unsigned32Caps
_PhysicalPortCapSigDegPcslThreshold_Object=MibTableColumn
physicalPortCapSigDegPcslThreshold=_PhysicalPortCapSigDegPcslThreshold_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,47),_PhysicalPortCapSigDegPcslThreshold_Type())
physicalPortCapSigDegPcslThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapSigDegPcslThreshold.setStatus(_A)
if mibBuilder.loadTexts:physicalPortCapSigDegPcslThreshold.setUnits(_G)
_PhysicalPortCapSigDegThresSonetSection_Type=FspR7BERThresholdSectionCaps
_PhysicalPortCapSigDegThresSonetSection_Object=MibTableColumn
physicalPortCapSigDegThresSonetSection=_PhysicalPortCapSigDegThresSonetSection_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,48),_PhysicalPortCapSigDegThresSonetSection_Type())
physicalPortCapSigDegThresSonetSection.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapSigDegThresSonetSection.setStatus(_A)
_PhysicalPortCapSigDegThresSdhSection_Type=FspR7Unsigned32Caps
_PhysicalPortCapSigDegThresSdhSection_Object=MibTableColumn
physicalPortCapSigDegThresSdhSection=_PhysicalPortCapSigDegThresSdhSection_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,49),_PhysicalPortCapSigDegThresSdhSection_Type())
physicalPortCapSigDegThresSdhSection.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapSigDegThresSdhSection.setStatus(_A)
if mibBuilder.loadTexts:physicalPortCapSigDegThresSdhSection.setUnits(_G)
_PhysicalPortCapSigDegThresOduTcmA_Type=FspR7Integer32Caps
_PhysicalPortCapSigDegThresOduTcmA_Object=MibTableColumn
physicalPortCapSigDegThresOduTcmA=_PhysicalPortCapSigDegThresOduTcmA_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,50),_PhysicalPortCapSigDegThresOduTcmA_Type())
physicalPortCapSigDegThresOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapSigDegThresOduTcmA.setStatus(_A)
if mibBuilder.loadTexts:physicalPortCapSigDegThresOduTcmA.setUnits(_G)
_PhysicalPortCapSigDegThresOduTcmB_Type=FspR7Integer32Caps
_PhysicalPortCapSigDegThresOduTcmB_Object=MibTableColumn
physicalPortCapSigDegThresOduTcmB=_PhysicalPortCapSigDegThresOduTcmB_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,51),_PhysicalPortCapSigDegThresOduTcmB_Type())
physicalPortCapSigDegThresOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapSigDegThresOduTcmB.setStatus(_A)
if mibBuilder.loadTexts:physicalPortCapSigDegThresOduTcmB.setUnits(_G)
_PhysicalPortCapSigDegThresOduTcmC_Type=FspR7Integer32Caps
_PhysicalPortCapSigDegThresOduTcmC_Object=MibTableColumn
physicalPortCapSigDegThresOduTcmC=_PhysicalPortCapSigDegThresOduTcmC_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,52),_PhysicalPortCapSigDegThresOduTcmC_Type())
physicalPortCapSigDegThresOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapSigDegThresOduTcmC.setStatus(_A)
if mibBuilder.loadTexts:physicalPortCapSigDegThresOduTcmC.setUnits(_G)
_PhysicalPortCapSignalDegradePeriod_Type=FspR7Unsigned32Caps
_PhysicalPortCapSignalDegradePeriod_Object=MibTableColumn
physicalPortCapSignalDegradePeriod=_PhysicalPortCapSignalDegradePeriod_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,53),_PhysicalPortCapSignalDegradePeriod_Type())
physicalPortCapSignalDegradePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapSignalDegradePeriod.setStatus(_A)
if mibBuilder.loadTexts:physicalPortCapSignalDegradePeriod.setUnits(_H)
_PhysicalPortCapSigDegPeriodOdu_Type=FspR7Unsigned32Caps
_PhysicalPortCapSigDegPeriodOdu_Object=MibTableColumn
physicalPortCapSigDegPeriodOdu=_PhysicalPortCapSigDegPeriodOdu_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,54),_PhysicalPortCapSigDegPeriodOdu_Type())
physicalPortCapSigDegPeriodOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapSigDegPeriodOdu.setStatus(_A)
if mibBuilder.loadTexts:physicalPortCapSigDegPeriodOdu.setUnits(_H)
_PhysicalPortCapSigDegPeriodOtu_Type=FspR7Unsigned32Caps
_PhysicalPortCapSigDegPeriodOtu_Object=MibTableColumn
physicalPortCapSigDegPeriodOtu=_PhysicalPortCapSigDegPeriodOtu_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,55),_PhysicalPortCapSigDegPeriodOtu_Type())
physicalPortCapSigDegPeriodOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapSigDegPeriodOtu.setStatus(_A)
if mibBuilder.loadTexts:physicalPortCapSigDegPeriodOtu.setUnits(_H)
_PhysicalPortCapSigDegPeriodIntegration_Type=FspR7Unsigned32Caps
_PhysicalPortCapSigDegPeriodIntegration_Object=MibTableColumn
physicalPortCapSigDegPeriodIntegration=_PhysicalPortCapSigDegPeriodIntegration_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,56),_PhysicalPortCapSigDegPeriodIntegration_Type())
physicalPortCapSigDegPeriodIntegration.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapSigDegPeriodIntegration.setStatus(_A)
if mibBuilder.loadTexts:physicalPortCapSigDegPeriodIntegration.setUnits(_H)
_PhysicalPortCapSigDegPeriodSdhSection_Type=FspR7Unsigned32Caps
_PhysicalPortCapSigDegPeriodSdhSection_Object=MibTableColumn
physicalPortCapSigDegPeriodSdhSection=_PhysicalPortCapSigDegPeriodSdhSection_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,57),_PhysicalPortCapSigDegPeriodSdhSection_Type())
physicalPortCapSigDegPeriodSdhSection.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapSigDegPeriodSdhSection.setStatus(_A)
if mibBuilder.loadTexts:physicalPortCapSigDegPeriodSdhSection.setUnits(_H)
_PhysicalPortCapSigDegPeriodOduTcmA_Type=FspR7Unsigned32Caps
_PhysicalPortCapSigDegPeriodOduTcmA_Object=MibTableColumn
physicalPortCapSigDegPeriodOduTcmA=_PhysicalPortCapSigDegPeriodOduTcmA_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,58),_PhysicalPortCapSigDegPeriodOduTcmA_Type())
physicalPortCapSigDegPeriodOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapSigDegPeriodOduTcmA.setStatus(_A)
if mibBuilder.loadTexts:physicalPortCapSigDegPeriodOduTcmA.setUnits(_H)
_PhysicalPortCapSigDegPeriodOduTcmB_Type=FspR7Unsigned32Caps
_PhysicalPortCapSigDegPeriodOduTcmB_Object=MibTableColumn
physicalPortCapSigDegPeriodOduTcmB=_PhysicalPortCapSigDegPeriodOduTcmB_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,59),_PhysicalPortCapSigDegPeriodOduTcmB_Type())
physicalPortCapSigDegPeriodOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapSigDegPeriodOduTcmB.setStatus(_A)
if mibBuilder.loadTexts:physicalPortCapSigDegPeriodOduTcmB.setUnits(_H)
_PhysicalPortCapSigDegPeriodOduTcmC_Type=FspR7Unsigned32Caps
_PhysicalPortCapSigDegPeriodOduTcmC_Object=MibTableColumn
physicalPortCapSigDegPeriodOduTcmC=_PhysicalPortCapSigDegPeriodOduTcmC_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,60),_PhysicalPortCapSigDegPeriodOduTcmC_Type())
physicalPortCapSigDegPeriodOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapSigDegPeriodOduTcmC.setStatus(_A)
if mibBuilder.loadTexts:physicalPortCapSigDegPeriodOduTcmC.setUnits(_H)
_PhysicalPortCapOtnStuffing_Type=FspR7StuffCaps
_PhysicalPortCapOtnStuffing_Object=MibTableColumn
physicalPortCapOtnStuffing=_PhysicalPortCapOtnStuffing_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,61),_PhysicalPortCapOtnStuffing_Type())
physicalPortCapOtnStuffing.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapOtnStuffing.setStatus(_A)
_PhysicalPortCapTcmALevel_Type=OtnTcmLevelCaps
_PhysicalPortCapTcmALevel_Object=MibTableColumn
physicalPortCapTcmALevel=_PhysicalPortCapTcmALevel_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,62),_PhysicalPortCapTcmALevel_Type())
physicalPortCapTcmALevel.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTcmALevel.setStatus(_A)
_PhysicalPortCapTcmBLevel_Type=OtnTcmLevelCaps
_PhysicalPortCapTcmBLevel_Object=MibTableColumn
physicalPortCapTcmBLevel=_PhysicalPortCapTcmBLevel_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,63),_PhysicalPortCapTcmBLevel_Type())
physicalPortCapTcmBLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTcmBLevel.setStatus(_A)
_PhysicalPortCapTcmCLevel_Type=OtnTcmLevelCaps
_PhysicalPortCapTcmCLevel_Object=MibTableColumn
physicalPortCapTcmCLevel=_PhysicalPortCapTcmCLevel_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,64),_PhysicalPortCapTcmCLevel_Type())
physicalPortCapTcmCLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTcmCLevel.setStatus(_A)
_PhysicalPortCapTerminationLevel_Type=OhTerminationLevelCaps
_PhysicalPortCapTerminationLevel_Object=MibTableColumn
physicalPortCapTerminationLevel=_PhysicalPortCapTerminationLevel_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,65),_PhysicalPortCapTerminationLevel_Type())
physicalPortCapTerminationLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTerminationLevel.setStatus(_A)
_PhysicalPortCapTimingSource_Type=SonetTimingSourceCaps
_PhysicalPortCapTimingSource_Object=MibTableColumn
physicalPortCapTimingSource=_PhysicalPortCapTimingSource_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,66),_PhysicalPortCapTimingSource_Type())
physicalPortCapTimingSource.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTimingSource.setStatus(_A)
_PhysicalPortCapTimModeOdu_Type=TimModeCaps
_PhysicalPortCapTimModeOdu_Object=MibTableColumn
physicalPortCapTimModeOdu=_PhysicalPortCapTimModeOdu_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,67),_PhysicalPortCapTimModeOdu_Type())
physicalPortCapTimModeOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTimModeOdu.setStatus(_A)
_PhysicalPortCapTimModeOtu_Type=TimModeCaps
_PhysicalPortCapTimModeOtu_Object=MibTableColumn
physicalPortCapTimModeOtu=_PhysicalPortCapTimModeOtu_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,68),_PhysicalPortCapTimModeOtu_Type())
physicalPortCapTimModeOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTimModeOtu.setStatus(_A)
_PhysicalPortCapTimModeSonetSection_Type=TimModeCaps
_PhysicalPortCapTimModeSonetSection_Object=MibTableColumn
physicalPortCapTimModeSonetSection=_PhysicalPortCapTimModeSonetSection_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,69),_PhysicalPortCapTimModeSonetSection_Type())
physicalPortCapTimModeSonetSection.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTimModeSonetSection.setStatus(_A)
_PhysicalPortCapTimModeOduTcmA_Type=TimModeCaps
_PhysicalPortCapTimModeOduTcmA_Object=MibTableColumn
physicalPortCapTimModeOduTcmA=_PhysicalPortCapTimModeOduTcmA_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,70),_PhysicalPortCapTimModeOduTcmA_Type())
physicalPortCapTimModeOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTimModeOduTcmA.setStatus(_A)
_PhysicalPortCapTimModeOduTcmB_Type=TimModeCaps
_PhysicalPortCapTimModeOduTcmB_Object=MibTableColumn
physicalPortCapTimModeOduTcmB=_PhysicalPortCapTimModeOduTcmB_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,71),_PhysicalPortCapTimModeOduTcmB_Type())
physicalPortCapTimModeOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTimModeOduTcmB.setStatus(_A)
_PhysicalPortCapTimModeOduTcmC_Type=TimModeCaps
_PhysicalPortCapTimModeOduTcmC_Object=MibTableColumn
physicalPortCapTimModeOduTcmC=_PhysicalPortCapTimModeOduTcmC_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,72),_PhysicalPortCapTimModeOduTcmC_Type())
physicalPortCapTimModeOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTimModeOduTcmC.setStatus(_A)
_PhysicalPortCapTraceFormSonetSection_Type=SonetTraceFormCaps
_PhysicalPortCapTraceFormSonetSection_Object=MibTableColumn
physicalPortCapTraceFormSonetSection=_PhysicalPortCapTraceFormSonetSection_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,73),_PhysicalPortCapTraceFormSonetSection_Type())
physicalPortCapTraceFormSonetSection.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTraceFormSonetSection.setStatus(_A)
_PhysicalPortCapTraceExpectedSonetSection_Type=Integer32
_PhysicalPortCapTraceExpectedSonetSection_Object=MibTableColumn
physicalPortCapTraceExpectedSonetSection=_PhysicalPortCapTraceExpectedSonetSection_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,74),_PhysicalPortCapTraceExpectedSonetSection_Type())
physicalPortCapTraceExpectedSonetSection.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTraceExpectedSonetSection.setStatus(_A)
_PhysicalPortCapTraceTransmitSonetSection_Type=Integer32
_PhysicalPortCapTraceTransmitSonetSection_Object=MibTableColumn
physicalPortCapTraceTransmitSonetSection=_PhysicalPortCapTraceTransmitSonetSection_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,75),_PhysicalPortCapTraceTransmitSonetSection_Type())
physicalPortCapTraceTransmitSonetSection.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTraceTransmitSonetSection.setStatus(_A)
_PhysicalPortCapTraceExpectedOtu_Type=Integer32
_PhysicalPortCapTraceExpectedOtu_Object=MibTableColumn
physicalPortCapTraceExpectedOtu=_PhysicalPortCapTraceExpectedOtu_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,76),_PhysicalPortCapTraceExpectedOtu_Type())
physicalPortCapTraceExpectedOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTraceExpectedOtu.setStatus(_A)
_PhysicalPortCapTraceTransmitSapiOtu_Type=Integer32
_PhysicalPortCapTraceTransmitSapiOtu_Object=MibTableColumn
physicalPortCapTraceTransmitSapiOtu=_PhysicalPortCapTraceTransmitSapiOtu_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,77),_PhysicalPortCapTraceTransmitSapiOtu_Type())
physicalPortCapTraceTransmitSapiOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTraceTransmitSapiOtu.setStatus(_A)
_PhysicalPortCapTraceTransmitDapiOtu_Type=Integer32
_PhysicalPortCapTraceTransmitDapiOtu_Object=MibTableColumn
physicalPortCapTraceTransmitDapiOtu=_PhysicalPortCapTraceTransmitDapiOtu_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,78),_PhysicalPortCapTraceTransmitDapiOtu_Type())
physicalPortCapTraceTransmitDapiOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTraceTransmitDapiOtu.setStatus(_A)
_PhysicalPortCapTraceTransmitOpspOtu_Type=Integer32
_PhysicalPortCapTraceTransmitOpspOtu_Object=MibTableColumn
physicalPortCapTraceTransmitOpspOtu=_PhysicalPortCapTraceTransmitOpspOtu_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,79),_PhysicalPortCapTraceTransmitOpspOtu_Type())
physicalPortCapTraceTransmitOpspOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTraceTransmitOpspOtu.setStatus(_A)
_PhysicalPortCapTraceExpectedOdu_Type=Integer32
_PhysicalPortCapTraceExpectedOdu_Object=MibTableColumn
physicalPortCapTraceExpectedOdu=_PhysicalPortCapTraceExpectedOdu_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,80),_PhysicalPortCapTraceExpectedOdu_Type())
physicalPortCapTraceExpectedOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTraceExpectedOdu.setStatus(_A)
_PhysicalPortCapTraceTransmitSapiOdu_Type=Integer32
_PhysicalPortCapTraceTransmitSapiOdu_Object=MibTableColumn
physicalPortCapTraceTransmitSapiOdu=_PhysicalPortCapTraceTransmitSapiOdu_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,81),_PhysicalPortCapTraceTransmitSapiOdu_Type())
physicalPortCapTraceTransmitSapiOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTraceTransmitSapiOdu.setStatus(_A)
_PhysicalPortCapTraceTransmitDapiOdu_Type=Integer32
_PhysicalPortCapTraceTransmitDapiOdu_Object=MibTableColumn
physicalPortCapTraceTransmitDapiOdu=_PhysicalPortCapTraceTransmitDapiOdu_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,82),_PhysicalPortCapTraceTransmitDapiOdu_Type())
physicalPortCapTraceTransmitDapiOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTraceTransmitDapiOdu.setStatus(_A)
_PhysicalPortCapTraceTransmitOpspOdu_Type=Integer32
_PhysicalPortCapTraceTransmitOpspOdu_Object=MibTableColumn
physicalPortCapTraceTransmitOpspOdu=_PhysicalPortCapTraceTransmitOpspOdu_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,83),_PhysicalPortCapTraceTransmitOpspOdu_Type())
physicalPortCapTraceTransmitOpspOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTraceTransmitOpspOdu.setStatus(_A)
_PhysicalPortCapTraceExpectedOduTcmA_Type=Integer32
_PhysicalPortCapTraceExpectedOduTcmA_Object=MibTableColumn
physicalPortCapTraceExpectedOduTcmA=_PhysicalPortCapTraceExpectedOduTcmA_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,84),_PhysicalPortCapTraceExpectedOduTcmA_Type())
physicalPortCapTraceExpectedOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTraceExpectedOduTcmA.setStatus(_A)
_PhysicalPortCapTraceTransmitSapiOduTcmA_Type=Integer32
_PhysicalPortCapTraceTransmitSapiOduTcmA_Object=MibTableColumn
physicalPortCapTraceTransmitSapiOduTcmA=_PhysicalPortCapTraceTransmitSapiOduTcmA_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,85),_PhysicalPortCapTraceTransmitSapiOduTcmA_Type())
physicalPortCapTraceTransmitSapiOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTraceTransmitSapiOduTcmA.setStatus(_A)
_PhysicalPortCapTraceTransmitDapiOduTcmA_Type=Integer32
_PhysicalPortCapTraceTransmitDapiOduTcmA_Object=MibTableColumn
physicalPortCapTraceTransmitDapiOduTcmA=_PhysicalPortCapTraceTransmitDapiOduTcmA_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,86),_PhysicalPortCapTraceTransmitDapiOduTcmA_Type())
physicalPortCapTraceTransmitDapiOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTraceTransmitDapiOduTcmA.setStatus(_A)
_PhysicalPortCapTraceTransmitOpspOduTcmA_Type=Integer32
_PhysicalPortCapTraceTransmitOpspOduTcmA_Object=MibTableColumn
physicalPortCapTraceTransmitOpspOduTcmA=_PhysicalPortCapTraceTransmitOpspOduTcmA_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,87),_PhysicalPortCapTraceTransmitOpspOduTcmA_Type())
physicalPortCapTraceTransmitOpspOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTraceTransmitOpspOduTcmA.setStatus(_A)
_PhysicalPortCapTraceExpectedOduTcmB_Type=Integer32
_PhysicalPortCapTraceExpectedOduTcmB_Object=MibTableColumn
physicalPortCapTraceExpectedOduTcmB=_PhysicalPortCapTraceExpectedOduTcmB_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,88),_PhysicalPortCapTraceExpectedOduTcmB_Type())
physicalPortCapTraceExpectedOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTraceExpectedOduTcmB.setStatus(_A)
_PhysicalPortCapTraceTransmitSapiOduTcmB_Type=Integer32
_PhysicalPortCapTraceTransmitSapiOduTcmB_Object=MibTableColumn
physicalPortCapTraceTransmitSapiOduTcmB=_PhysicalPortCapTraceTransmitSapiOduTcmB_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,89),_PhysicalPortCapTraceTransmitSapiOduTcmB_Type())
physicalPortCapTraceTransmitSapiOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTraceTransmitSapiOduTcmB.setStatus(_A)
_PhysicalPortCapTraceTransmitDapiOduTcmB_Type=Integer32
_PhysicalPortCapTraceTransmitDapiOduTcmB_Object=MibTableColumn
physicalPortCapTraceTransmitDapiOduTcmB=_PhysicalPortCapTraceTransmitDapiOduTcmB_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,90),_PhysicalPortCapTraceTransmitDapiOduTcmB_Type())
physicalPortCapTraceTransmitDapiOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTraceTransmitDapiOduTcmB.setStatus(_A)
_PhysicalPortCapTraceTransmitOpspOduTcmB_Type=Integer32
_PhysicalPortCapTraceTransmitOpspOduTcmB_Object=MibTableColumn
physicalPortCapTraceTransmitOpspOduTcmB=_PhysicalPortCapTraceTransmitOpspOduTcmB_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,91),_PhysicalPortCapTraceTransmitOpspOduTcmB_Type())
physicalPortCapTraceTransmitOpspOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTraceTransmitOpspOduTcmB.setStatus(_A)
_PhysicalPortCapTraceExpectedOduTcmC_Type=Integer32
_PhysicalPortCapTraceExpectedOduTcmC_Object=MibTableColumn
physicalPortCapTraceExpectedOduTcmC=_PhysicalPortCapTraceExpectedOduTcmC_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,92),_PhysicalPortCapTraceExpectedOduTcmC_Type())
physicalPortCapTraceExpectedOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTraceExpectedOduTcmC.setStatus(_A)
_PhysicalPortCapTraceTransmitSapiOduTcmC_Type=Integer32
_PhysicalPortCapTraceTransmitSapiOduTcmC_Object=MibTableColumn
physicalPortCapTraceTransmitSapiOduTcmC=_PhysicalPortCapTraceTransmitSapiOduTcmC_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,93),_PhysicalPortCapTraceTransmitSapiOduTcmC_Type())
physicalPortCapTraceTransmitSapiOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTraceTransmitSapiOduTcmC.setStatus(_A)
_PhysicalPortCapTraceTransmitDapiOduTcmC_Type=Integer32
_PhysicalPortCapTraceTransmitDapiOduTcmC_Object=MibTableColumn
physicalPortCapTraceTransmitDapiOduTcmC=_PhysicalPortCapTraceTransmitDapiOduTcmC_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,94),_PhysicalPortCapTraceTransmitDapiOduTcmC_Type())
physicalPortCapTraceTransmitDapiOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTraceTransmitDapiOduTcmC.setStatus(_A)
_PhysicalPortCapTraceTransmitOpspOduTcmC_Type=Integer32
_PhysicalPortCapTraceTransmitOpspOduTcmC_Object=MibTableColumn
physicalPortCapTraceTransmitOpspOduTcmC=_PhysicalPortCapTraceTransmitOpspOduTcmC_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,95),_PhysicalPortCapTraceTransmitOpspOduTcmC_Type())
physicalPortCapTraceTransmitOpspOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTraceTransmitOpspOduTcmC.setStatus(_A)
_PhysicalPortCapTurnupConfig_Type=FspR7TurnupConfigCaps
_PhysicalPortCapTurnupConfig_Object=MibTableColumn
physicalPortCapTurnupConfig=_PhysicalPortCapTurnupConfig_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,96),_PhysicalPortCapTurnupConfig_Type())
physicalPortCapTurnupConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTurnupConfig.setStatus(_A)
_PhysicalPortCapTxOffDelay_Type=FspR7EnableDisableCaps
_PhysicalPortCapTxOffDelay_Object=MibTableColumn
physicalPortCapTxOffDelay=_PhysicalPortCapTxOffDelay_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,97),_PhysicalPortCapTxOffDelay_Type())
physicalPortCapTxOffDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTxOffDelay.setStatus(_A)
_PhysicalPortCapVoaMode_Type=FspR7VoaModeCaps
_PhysicalPortCapVoaMode_Object=MibTableColumn
physicalPortCapVoaMode=_PhysicalPortCapVoaMode_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,98),_PhysicalPortCapVoaMode_Type())
physicalPortCapVoaMode.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapVoaMode.setStatus(_A)
_PhysicalPortCapVoaSetpoint_Type=FspR7Unsigned32Caps
_PhysicalPortCapVoaSetpoint_Object=MibTableColumn
physicalPortCapVoaSetpoint=_PhysicalPortCapVoaSetpoint_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,99),_PhysicalPortCapVoaSetpoint_Type())
physicalPortCapVoaSetpoint.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapVoaSetpoint.setStatus(_A)
if mibBuilder.loadTexts:physicalPortCapVoaSetpoint.setUnits(_F)
_PhysicalPortCapLagPrio_Type=FspR7Unsigned32Caps
_PhysicalPortCapLagPrio_Object=MibTableColumn
physicalPortCapLagPrio=_PhysicalPortCapLagPrio_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,100),_PhysicalPortCapLagPrio_Type())
physicalPortCapLagPrio.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapLagPrio.setStatus(_A)
_PhysicalPortCapMaxFrameSize_Type=FspR7Unsigned32Caps
_PhysicalPortCapMaxFrameSize_Object=MibTableColumn
physicalPortCapMaxFrameSize=_PhysicalPortCapMaxFrameSize_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,101),_PhysicalPortCapMaxFrameSize_Type())
physicalPortCapMaxFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapMaxFrameSize.setStatus(_A)
_PhysicalPortCapPayload_Type=OtnPayloadTypeCaps
_PhysicalPortCapPayload_Object=MibTableColumn
physicalPortCapPayload=_PhysicalPortCapPayload_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,102),_PhysicalPortCapPayload_Type())
physicalPortCapPayload.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapPayload.setStatus(_A)
_PhysicalPortCapPortMode_Type=FspR7PortModeCaps
_PhysicalPortCapPortMode_Object=MibTableColumn
physicalPortCapPortMode=_PhysicalPortCapPortMode_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,103),_PhysicalPortCapPortMode_Type())
physicalPortCapPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapPortMode.setStatus(_A)
_PhysicalPortCapPortRole_Type=FspR7PortRoleCaps
_PhysicalPortCapPortRole_Object=MibTableColumn
physicalPortCapPortRole=_PhysicalPortCapPortRole_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,104),_PhysicalPortCapPortRole_Type())
physicalPortCapPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapPortRole.setStatus(_A)
_PhysicalPortCapPriority_Type=FspR7Unsigned32Caps
_PhysicalPortCapPriority_Object=MibTableColumn
physicalPortCapPriority=_PhysicalPortCapPriority_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,105),_PhysicalPortCapPriority_Type())
physicalPortCapPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapPriority.setStatus(_A)
_PhysicalPortCapPvid_Type=FspR7Unsigned32Caps
_PhysicalPortCapPvid_Object=MibTableColumn
physicalPortCapPvid=_PhysicalPortCapPvid_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,106),_PhysicalPortCapPvid_Type())
physicalPortCapPvid.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapPvid.setStatus(_A)
_PhysicalPortCapStagType_Type=Integer32
_PhysicalPortCapStagType_Object=MibTableColumn
physicalPortCapStagType=_PhysicalPortCapStagType_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,107),_PhysicalPortCapStagType_Type())
physicalPortCapStagType.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapStagType.setStatus(_A)
_PhysicalPortCapUtag_Type=FspR7UntaggedFramesCaps
_PhysicalPortCapUtag_Object=MibTableColumn
physicalPortCapUtag=_PhysicalPortCapUtag_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,108),_PhysicalPortCapUtag_Type())
physicalPortCapUtag.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapUtag.setStatus(_A)
_PhysicalPortCapVethAid_Type=SnmpAdminString
_PhysicalPortCapVethAid_Object=MibTableColumn
physicalPortCapVethAid=_PhysicalPortCapVethAid_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,109),_PhysicalPortCapVethAid_Type())
physicalPortCapVethAid.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapVethAid.setStatus(_A)
_PhysicalPortCapRedLineState_Type=FspR7RedLinedStateCaps
_PhysicalPortCapRedLineState_Object=MibTableColumn
physicalPortCapRedLineState=_PhysicalPortCapRedLineState_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,110),_PhysicalPortCapRedLineState_Type())
physicalPortCapRedLineState.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapRedLineState.setStatus(_A)
_PhysicalPortCapTunnelAid_Type=Integer32
_PhysicalPortCapTunnelAid_Object=MibTableColumn
physicalPortCapTunnelAid=_PhysicalPortCapTunnelAid_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,111),_PhysicalPortCapTunnelAid_Type())
physicalPortCapTunnelAid.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTunnelAid.setStatus(_A)
_PhysicalPortCapRateLimit_Type=FspR7DisableEnableCaps
_PhysicalPortCapRateLimit_Object=MibTableColumn
physicalPortCapRateLimit=_PhysicalPortCapRateLimit_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,112),_PhysicalPortCapRateLimit_Type())
physicalPortCapRateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapRateLimit.setStatus(_A)
_PhysicalPortCapTxOffOnTm_Type=FspR7TxOffOnTmCaps
_PhysicalPortCapTxOffOnTm_Object=MibTableColumn
physicalPortCapTxOffOnTm=_PhysicalPortCapTxOffOnTm_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,113),_PhysicalPortCapTxOffOnTm_Type())
physicalPortCapTxOffOnTm.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTxOffOnTm.setStatus(_A)
_PhysicalPortCapTxOffTimer_Type=FspR7Unsigned32Caps
_PhysicalPortCapTxOffTimer_Object=MibTableColumn
physicalPortCapTxOffTimer=_PhysicalPortCapTxOffTimer_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,114),_PhysicalPortCapTxOffTimer_Type())
physicalPortCapTxOffTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTxOffTimer.setStatus(_A)
if mibBuilder.loadTexts:physicalPortCapTxOffTimer.setUnits(_O)
_PhysicalPortCapTxOnTimer_Type=FspR7Unsigned32Caps
_PhysicalPortCapTxOnTimer_Object=MibTableColumn
physicalPortCapTxOnTimer=_PhysicalPortCapTxOnTimer_Object((1,3,6,1,4,1,2544,1,11,9,3,4,1,1,115),_PhysicalPortCapTxOnTimer_Type())
physicalPortCapTxOnTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:physicalPortCapTxOnTimer.setStatus(_A)
if mibBuilder.loadTexts:physicalPortCapTxOnTimer.setUnits(_O)
_VirtualPortCapTable_Object=MibTable
virtualPortCapTable=_VirtualPortCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2))
if mibBuilder.loadTexts:virtualPortCapTable.setStatus(_A)
_VirtualPortCapEntry_Object=MibTableRow
virtualPortCapEntry=_VirtualPortCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1))
virtualPortCapEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_K),(0,_C,_J),(0,_C,_I))
if mibBuilder.loadTexts:virtualPortCapEntry.setStatus(_A)
_VirtualPortCapRowStatus_Type=FspR7RowStatusCaps
_VirtualPortCapRowStatus_Object=MibTableColumn
virtualPortCapRowStatus=_VirtualPortCapRowStatus_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,1),_VirtualPortCapRowStatus_Type())
virtualPortCapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapRowStatus.setStatus(_A)
_VirtualPortCapChannelBand_Type=FspR7ChannelBandwidthCaps
_VirtualPortCapChannelBand_Object=MibTableColumn
virtualPortCapChannelBand=_VirtualPortCapChannelBand_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,2),_VirtualPortCapChannelBand_Type())
virtualPortCapChannelBand.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapChannelBand.setStatus(_A)
_VirtualPortCapType_Type=FspR7InterfaceTypeCaps
_VirtualPortCapType_Object=MibTableColumn
virtualPortCapType=_VirtualPortCapType_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,3),_VirtualPortCapType_Type())
virtualPortCapType.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapType.setStatus(_A)
_VirtualPortCapAlias_Type=Integer32
_VirtualPortCapAlias_Object=MibTableColumn
virtualPortCapAlias=_VirtualPortCapAlias_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,4),_VirtualPortCapAlias_Type())
virtualPortCapAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapAlias.setStatus(_A)
_VirtualPortCapAdmin_Type=FspR7AdminStateCaps
_VirtualPortCapAdmin_Object=MibTableColumn
virtualPortCapAdmin=_VirtualPortCapAdmin_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,5),_VirtualPortCapAdmin_Type())
virtualPortCapAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapAdmin.setStatus(_A)
_VirtualPortCapEqlzAdmin_Type=FspR7EqlzAdminStateCaps
_VirtualPortCapEqlzAdmin_Object=MibTableColumn
virtualPortCapEqlzAdmin=_VirtualPortCapEqlzAdmin_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,6),_VirtualPortCapEqlzAdmin_Type())
virtualPortCapEqlzAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapEqlzAdmin.setStatus(_A)
_VirtualPortCapInitEqlz_Type=FspR7InitEqualizationCaps
_VirtualPortCapInitEqlz_Object=MibTableColumn
virtualPortCapInitEqlz=_VirtualPortCapInitEqlz_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,7),_VirtualPortCapInitEqlz_Type())
virtualPortCapInitEqlz.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapInitEqlz.setStatus(_A)
_VirtualPortCapLacpMode_Type=FspR7LacpModeCaps
_VirtualPortCapLacpMode_Object=MibTableColumn
virtualPortCapLacpMode=_VirtualPortCapLacpMode_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,8),_VirtualPortCapLacpMode_Type())
virtualPortCapLacpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapLacpMode.setStatus(_A)
_VirtualPortCapLacpTimeout_Type=FspR7LacpTimeoutCaps
_VirtualPortCapLacpTimeout_Object=MibTableColumn
virtualPortCapLacpTimeout=_VirtualPortCapLacpTimeout_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,9),_VirtualPortCapLacpTimeout_Type())
virtualPortCapLacpTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapLacpTimeout.setStatus(_A)
_VirtualPortCapLagActivePorts_Type=FspR7Unsigned32Caps
_VirtualPortCapLagActivePorts_Object=MibTableColumn
virtualPortCapLagActivePorts=_VirtualPortCapLagActivePorts_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,10),_VirtualPortCapLagActivePorts_Type())
virtualPortCapLagActivePorts.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapLagActivePorts.setStatus(_A)
_VirtualPortCapMaxFrameSize_Type=FspR7Unsigned32Caps
_VirtualPortCapMaxFrameSize_Object=MibTableColumn
virtualPortCapMaxFrameSize=_VirtualPortCapMaxFrameSize_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,11),_VirtualPortCapMaxFrameSize_Type())
virtualPortCapMaxFrameSize.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapMaxFrameSize.setStatus(_A)
_VirtualPortCapPortMode_Type=FspR7PortModeCaps
_VirtualPortCapPortMode_Object=MibTableColumn
virtualPortCapPortMode=_VirtualPortCapPortMode_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,12),_VirtualPortCapPortMode_Type())
virtualPortCapPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapPortMode.setStatus(_A)
_VirtualPortCapDataLayerPmReset_Type=FspR7PmResetCaps
_VirtualPortCapDataLayerPmReset_Object=MibTableColumn
virtualPortCapDataLayerPmReset=_VirtualPortCapDataLayerPmReset_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,13),_VirtualPortCapDataLayerPmReset_Type())
virtualPortCapDataLayerPmReset.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapDataLayerPmReset.setStatus(_A)
_VirtualPortCapPortRole_Type=FspR7PortRoleCaps
_VirtualPortCapPortRole_Object=MibTableColumn
virtualPortCapPortRole=_VirtualPortCapPortRole_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,14),_VirtualPortCapPortRole_Type())
virtualPortCapPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapPortRole.setStatus(_A)
_VirtualPortCapLagPortType_Type=FspR7LagPortTypeCaps
_VirtualPortCapLagPortType_Object=MibTableColumn
virtualPortCapLagPortType=_VirtualPortCapLagPortType_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,15),_VirtualPortCapLagPortType_Type())
virtualPortCapLagPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapLagPortType.setStatus(_A)
_VirtualPortCapPriority_Type=FspR7Unsigned32Caps
_VirtualPortCapPriority_Object=MibTableColumn
virtualPortCapPriority=_VirtualPortCapPriority_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,16),_VirtualPortCapPriority_Type())
virtualPortCapPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapPriority.setStatus(_A)
_VirtualPortCapPvid_Type=FspR7Unsigned32Caps
_VirtualPortCapPvid_Object=MibTableColumn
virtualPortCapPvid=_VirtualPortCapPvid_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,17),_VirtualPortCapPvid_Type())
virtualPortCapPvid.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapPvid.setStatus(_A)
_VirtualPortCapRevertiveMode_Type=ApsRevertModeCaps
_VirtualPortCapRevertiveMode_Object=MibTableColumn
virtualPortCapRevertiveMode=_VirtualPortCapRevertiveMode_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,18),_VirtualPortCapRevertiveMode_Type())
virtualPortCapRevertiveMode.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapRevertiveMode.setStatus(_A)
_VirtualPortCapStagType_Type=Integer32
_VirtualPortCapStagType_Object=MibTableColumn
virtualPortCapStagType=_VirtualPortCapStagType_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,19),_VirtualPortCapStagType_Type())
virtualPortCapStagType.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapStagType.setStatus(_A)
_VirtualPortCapUtag_Type=FspR7UntaggedFramesCaps
_VirtualPortCapUtag_Object=MibTableColumn
virtualPortCapUtag=_VirtualPortCapUtag_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,20),_VirtualPortCapUtag_Type())
virtualPortCapUtag.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapUtag.setStatus(_A)
_VirtualPortCapBundle_Type=FspR7SnmpLongString
_VirtualPortCapBundle_Object=MibTableColumn
virtualPortCapBundle=_VirtualPortCapBundle_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,21),_VirtualPortCapBundle_Type())
virtualPortCapBundle.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapBundle.setStatus(_A)
_VirtualPortCapSwitchCommand_Type=FspR7APSCommandCaps
_VirtualPortCapSwitchCommand_Object=MibTableColumn
virtualPortCapSwitchCommand=_VirtualPortCapSwitchCommand_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,22),_VirtualPortCapSwitchCommand_Type())
virtualPortCapSwitchCommand.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapSwitchCommand.setStatus(_A)
_VirtualPortCapInhibitSwitchToWork_Type=FspR7YesNoCaps
_VirtualPortCapInhibitSwitchToWork_Object=MibTableColumn
virtualPortCapInhibitSwitchToWork=_VirtualPortCapInhibitSwitchToWork_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,23),_VirtualPortCapInhibitSwitchToWork_Type())
virtualPortCapInhibitSwitchToWork.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapInhibitSwitchToWork.setStatus(_A)
_VirtualPortCapInhibitSwitchToProt_Type=FspR7YesNoCaps
_VirtualPortCapInhibitSwitchToProt_Object=MibTableColumn
virtualPortCapInhibitSwitchToProt=_VirtualPortCapInhibitSwitchToProt_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,24),_VirtualPortCapInhibitSwitchToProt_Type())
virtualPortCapInhibitSwitchToProt.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapInhibitSwitchToProt.setStatus(_A)
_VirtualPortCapOduTribPortNo_Type=SnmpAdminString
_VirtualPortCapOduTribPortNo_Object=MibTableColumn
virtualPortCapOduTribPortNo=_VirtualPortCapOduTribPortNo_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,25),_VirtualPortCapOduTribPortNo_Type())
virtualPortCapOduTribPortNo.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapOduTribPortNo.setStatus(_A)
_VirtualPortCapOduTribTimeSlottNo_Type=SnmpAdminString
_VirtualPortCapOduTribTimeSlottNo_Object=MibTableColumn
virtualPortCapOduTribTimeSlottNo=_VirtualPortCapOduTribTimeSlottNo_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,26),_VirtualPortCapOduTribTimeSlottNo_Type())
virtualPortCapOduTribTimeSlottNo.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapOduTribTimeSlottNo.setStatus(_A)
_VirtualPortCapSigDegThresOdu_Type=FspR7Integer32Caps
_VirtualPortCapSigDegThresOdu_Object=MibTableColumn
virtualPortCapSigDegThresOdu=_VirtualPortCapSigDegThresOdu_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,27),_VirtualPortCapSigDegThresOdu_Type())
virtualPortCapSigDegThresOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapSigDegThresOdu.setStatus(_A)
if mibBuilder.loadTexts:virtualPortCapSigDegThresOdu.setUnits(_G)
_VirtualPortCapSigDegPeriodOdu_Type=FspR7Unsigned32Caps
_VirtualPortCapSigDegPeriodOdu_Object=MibTableColumn
virtualPortCapSigDegPeriodOdu=_VirtualPortCapSigDegPeriodOdu_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,28),_VirtualPortCapSigDegPeriodOdu_Type())
virtualPortCapSigDegPeriodOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapSigDegPeriodOdu.setStatus(_A)
if mibBuilder.loadTexts:virtualPortCapSigDegPeriodOdu.setUnits(_H)
_VirtualPortCapTraceExpectedOdu_Type=Integer32
_VirtualPortCapTraceExpectedOdu_Object=MibTableColumn
virtualPortCapTraceExpectedOdu=_VirtualPortCapTraceExpectedOdu_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,29),_VirtualPortCapTraceExpectedOdu_Type())
virtualPortCapTraceExpectedOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTraceExpectedOdu.setStatus(_A)
_VirtualPortCapTraceTransmitSapiOdu_Type=Integer32
_VirtualPortCapTraceTransmitSapiOdu_Object=MibTableColumn
virtualPortCapTraceTransmitSapiOdu=_VirtualPortCapTraceTransmitSapiOdu_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,30),_VirtualPortCapTraceTransmitSapiOdu_Type())
virtualPortCapTraceTransmitSapiOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTraceTransmitSapiOdu.setStatus(_A)
_VirtualPortCapTraceTransmitDapiOdu_Type=Integer32
_VirtualPortCapTraceTransmitDapiOdu_Object=MibTableColumn
virtualPortCapTraceTransmitDapiOdu=_VirtualPortCapTraceTransmitDapiOdu_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,31),_VirtualPortCapTraceTransmitDapiOdu_Type())
virtualPortCapTraceTransmitDapiOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTraceTransmitDapiOdu.setStatus(_A)
_VirtualPortCapTraceTransmitOpspOdu_Type=Integer32
_VirtualPortCapTraceTransmitOpspOdu_Object=MibTableColumn
virtualPortCapTraceTransmitOpspOdu=_VirtualPortCapTraceTransmitOpspOdu_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,32),_VirtualPortCapTraceTransmitOpspOdu_Type())
virtualPortCapTraceTransmitOpspOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTraceTransmitOpspOdu.setStatus(_A)
_VirtualPortCapTimModeOdu_Type=TimModeCaps
_VirtualPortCapTimModeOdu_Object=MibTableColumn
virtualPortCapTimModeOdu=_VirtualPortCapTimModeOdu_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,33),_VirtualPortCapTimModeOdu_Type())
virtualPortCapTimModeOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTimModeOdu.setStatus(_A)
_VirtualPortCapSigDegThresOduTcmA_Type=FspR7Integer32Caps
_VirtualPortCapSigDegThresOduTcmA_Object=MibTableColumn
virtualPortCapSigDegThresOduTcmA=_VirtualPortCapSigDegThresOduTcmA_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,34),_VirtualPortCapSigDegThresOduTcmA_Type())
virtualPortCapSigDegThresOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapSigDegThresOduTcmA.setStatus(_A)
if mibBuilder.loadTexts:virtualPortCapSigDegThresOduTcmA.setUnits(_G)
_VirtualPortCapSigDegPeriodOduTcmA_Type=FspR7Unsigned32Caps
_VirtualPortCapSigDegPeriodOduTcmA_Object=MibTableColumn
virtualPortCapSigDegPeriodOduTcmA=_VirtualPortCapSigDegPeriodOduTcmA_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,35),_VirtualPortCapSigDegPeriodOduTcmA_Type())
virtualPortCapSigDegPeriodOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapSigDegPeriodOduTcmA.setStatus(_A)
if mibBuilder.loadTexts:virtualPortCapSigDegPeriodOduTcmA.setUnits(_H)
_VirtualPortCapSigDegThresOduTcmB_Type=FspR7Integer32Caps
_VirtualPortCapSigDegThresOduTcmB_Object=MibTableColumn
virtualPortCapSigDegThresOduTcmB=_VirtualPortCapSigDegThresOduTcmB_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,36),_VirtualPortCapSigDegThresOduTcmB_Type())
virtualPortCapSigDegThresOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapSigDegThresOduTcmB.setStatus(_A)
if mibBuilder.loadTexts:virtualPortCapSigDegThresOduTcmB.setUnits(_G)
_VirtualPortCapSigDegPeriodOduTcmB_Type=FspR7Unsigned32Caps
_VirtualPortCapSigDegPeriodOduTcmB_Object=MibTableColumn
virtualPortCapSigDegPeriodOduTcmB=_VirtualPortCapSigDegPeriodOduTcmB_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,37),_VirtualPortCapSigDegPeriodOduTcmB_Type())
virtualPortCapSigDegPeriodOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapSigDegPeriodOduTcmB.setStatus(_A)
if mibBuilder.loadTexts:virtualPortCapSigDegPeriodOduTcmB.setUnits(_H)
_VirtualPortCapSigDegThresOduTcmC_Type=FspR7Integer32Caps
_VirtualPortCapSigDegThresOduTcmC_Object=MibTableColumn
virtualPortCapSigDegThresOduTcmC=_VirtualPortCapSigDegThresOduTcmC_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,38),_VirtualPortCapSigDegThresOduTcmC_Type())
virtualPortCapSigDegThresOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapSigDegThresOduTcmC.setStatus(_A)
if mibBuilder.loadTexts:virtualPortCapSigDegThresOduTcmC.setUnits(_G)
_VirtualPortCapSigDegPeriodOduTcmC_Type=FspR7Unsigned32Caps
_VirtualPortCapSigDegPeriodOduTcmC_Object=MibTableColumn
virtualPortCapSigDegPeriodOduTcmC=_VirtualPortCapSigDegPeriodOduTcmC_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,39),_VirtualPortCapSigDegPeriodOduTcmC_Type())
virtualPortCapSigDegPeriodOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapSigDegPeriodOduTcmC.setStatus(_A)
if mibBuilder.loadTexts:virtualPortCapSigDegPeriodOduTcmC.setUnits(_H)
_VirtualPortCapTcmALevel_Type=OtnTcmLevelCaps
_VirtualPortCapTcmALevel_Object=MibTableColumn
virtualPortCapTcmALevel=_VirtualPortCapTcmALevel_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,40),_VirtualPortCapTcmALevel_Type())
virtualPortCapTcmALevel.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTcmALevel.setStatus(_A)
_VirtualPortCapTcmBLevel_Type=OtnTcmLevelCaps
_VirtualPortCapTcmBLevel_Object=MibTableColumn
virtualPortCapTcmBLevel=_VirtualPortCapTcmBLevel_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,41),_VirtualPortCapTcmBLevel_Type())
virtualPortCapTcmBLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTcmBLevel.setStatus(_A)
_VirtualPortCapTcmCLevel_Type=OtnTcmLevelCaps
_VirtualPortCapTcmCLevel_Object=MibTableColumn
virtualPortCapTcmCLevel=_VirtualPortCapTcmCLevel_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,42),_VirtualPortCapTcmCLevel_Type())
virtualPortCapTcmCLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTcmCLevel.setStatus(_A)
_VirtualPortCapTraceTransmitSapiOduTcmA_Type=Integer32
_VirtualPortCapTraceTransmitSapiOduTcmA_Object=MibTableColumn
virtualPortCapTraceTransmitSapiOduTcmA=_VirtualPortCapTraceTransmitSapiOduTcmA_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,43),_VirtualPortCapTraceTransmitSapiOduTcmA_Type())
virtualPortCapTraceTransmitSapiOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTraceTransmitSapiOduTcmA.setStatus(_A)
_VirtualPortCapTraceTransmitDapiOduTcmA_Type=Integer32
_VirtualPortCapTraceTransmitDapiOduTcmA_Object=MibTableColumn
virtualPortCapTraceTransmitDapiOduTcmA=_VirtualPortCapTraceTransmitDapiOduTcmA_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,44),_VirtualPortCapTraceTransmitDapiOduTcmA_Type())
virtualPortCapTraceTransmitDapiOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTraceTransmitDapiOduTcmA.setStatus(_A)
_VirtualPortCapTraceTransmitOpspOduTcmA_Type=Integer32
_VirtualPortCapTraceTransmitOpspOduTcmA_Object=MibTableColumn
virtualPortCapTraceTransmitOpspOduTcmA=_VirtualPortCapTraceTransmitOpspOduTcmA_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,45),_VirtualPortCapTraceTransmitOpspOduTcmA_Type())
virtualPortCapTraceTransmitOpspOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTraceTransmitOpspOduTcmA.setStatus(_A)
_VirtualPortCapTraceExpectedOduTcmA_Type=Integer32
_VirtualPortCapTraceExpectedOduTcmA_Object=MibTableColumn
virtualPortCapTraceExpectedOduTcmA=_VirtualPortCapTraceExpectedOduTcmA_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,46),_VirtualPortCapTraceExpectedOduTcmA_Type())
virtualPortCapTraceExpectedOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTraceExpectedOduTcmA.setStatus(_A)
_VirtualPortCapTimModeOduTcmA_Type=TimModeCaps
_VirtualPortCapTimModeOduTcmA_Object=MibTableColumn
virtualPortCapTimModeOduTcmA=_VirtualPortCapTimModeOduTcmA_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,47),_VirtualPortCapTimModeOduTcmA_Type())
virtualPortCapTimModeOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTimModeOduTcmA.setStatus(_A)
_VirtualPortCapTraceExpectedOduTcmB_Type=Integer32
_VirtualPortCapTraceExpectedOduTcmB_Object=MibTableColumn
virtualPortCapTraceExpectedOduTcmB=_VirtualPortCapTraceExpectedOduTcmB_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,48),_VirtualPortCapTraceExpectedOduTcmB_Type())
virtualPortCapTraceExpectedOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTraceExpectedOduTcmB.setStatus(_A)
_VirtualPortCapTraceTransmitSapiOduTcmB_Type=Integer32
_VirtualPortCapTraceTransmitSapiOduTcmB_Object=MibTableColumn
virtualPortCapTraceTransmitSapiOduTcmB=_VirtualPortCapTraceTransmitSapiOduTcmB_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,49),_VirtualPortCapTraceTransmitSapiOduTcmB_Type())
virtualPortCapTraceTransmitSapiOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTraceTransmitSapiOduTcmB.setStatus(_A)
_VirtualPortCapTraceTransmitDapiOduTcmB_Type=Integer32
_VirtualPortCapTraceTransmitDapiOduTcmB_Object=MibTableColumn
virtualPortCapTraceTransmitDapiOduTcmB=_VirtualPortCapTraceTransmitDapiOduTcmB_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,50),_VirtualPortCapTraceTransmitDapiOduTcmB_Type())
virtualPortCapTraceTransmitDapiOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTraceTransmitDapiOduTcmB.setStatus(_A)
_VirtualPortCapTraceTransmitOpspOduTcmB_Type=Integer32
_VirtualPortCapTraceTransmitOpspOduTcmB_Object=MibTableColumn
virtualPortCapTraceTransmitOpspOduTcmB=_VirtualPortCapTraceTransmitOpspOduTcmB_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,51),_VirtualPortCapTraceTransmitOpspOduTcmB_Type())
virtualPortCapTraceTransmitOpspOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTraceTransmitOpspOduTcmB.setStatus(_A)
_VirtualPortCapTimModeOduTcmB_Type=TimModeCaps
_VirtualPortCapTimModeOduTcmB_Object=MibTableColumn
virtualPortCapTimModeOduTcmB=_VirtualPortCapTimModeOduTcmB_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,52),_VirtualPortCapTimModeOduTcmB_Type())
virtualPortCapTimModeOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTimModeOduTcmB.setStatus(_A)
_VirtualPortCapTraceExpectedOduTcmC_Type=Integer32
_VirtualPortCapTraceExpectedOduTcmC_Object=MibTableColumn
virtualPortCapTraceExpectedOduTcmC=_VirtualPortCapTraceExpectedOduTcmC_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,53),_VirtualPortCapTraceExpectedOduTcmC_Type())
virtualPortCapTraceExpectedOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTraceExpectedOduTcmC.setStatus(_A)
_VirtualPortCapTraceTransmitSapiOduTcmC_Type=Integer32
_VirtualPortCapTraceTransmitSapiOduTcmC_Object=MibTableColumn
virtualPortCapTraceTransmitSapiOduTcmC=_VirtualPortCapTraceTransmitSapiOduTcmC_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,54),_VirtualPortCapTraceTransmitSapiOduTcmC_Type())
virtualPortCapTraceTransmitSapiOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTraceTransmitSapiOduTcmC.setStatus(_A)
_VirtualPortCapTraceTransmitDapiOduTcmC_Type=Integer32
_VirtualPortCapTraceTransmitDapiOduTcmC_Object=MibTableColumn
virtualPortCapTraceTransmitDapiOduTcmC=_VirtualPortCapTraceTransmitDapiOduTcmC_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,55),_VirtualPortCapTraceTransmitDapiOduTcmC_Type())
virtualPortCapTraceTransmitDapiOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTraceTransmitDapiOduTcmC.setStatus(_A)
_VirtualPortCapTraceTransmitOpspOduTcmC_Type=Integer32
_VirtualPortCapTraceTransmitOpspOduTcmC_Object=MibTableColumn
virtualPortCapTraceTransmitOpspOduTcmC=_VirtualPortCapTraceTransmitOpspOduTcmC_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,56),_VirtualPortCapTraceTransmitOpspOduTcmC_Type())
virtualPortCapTraceTransmitOpspOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTraceTransmitOpspOduTcmC.setStatus(_A)
_VirtualPortCapTimModeOduTcmC_Type=TimModeCaps
_VirtualPortCapTimModeOduTcmC_Object=MibTableColumn
virtualPortCapTimModeOduTcmC=_VirtualPortCapTimModeOduTcmC_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,57),_VirtualPortCapTimModeOduTcmC_Type())
virtualPortCapTimModeOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTimModeOduTcmC.setStatus(_A)
_VirtualPortCapTerminationLevel_Type=OhTerminationLevelCaps
_VirtualPortCapTerminationLevel_Object=MibTableColumn
virtualPortCapTerminationLevel=_VirtualPortCapTerminationLevel_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,58),_VirtualPortCapTerminationLevel_Type())
virtualPortCapTerminationLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTerminationLevel.setStatus(_A)
_VirtualPortCapLoopConfig_Type=LoopConfigCaps
_VirtualPortCapLoopConfig_Object=MibTableColumn
virtualPortCapLoopConfig=_VirtualPortCapLoopConfig_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,59),_VirtualPortCapLoopConfig_Type())
virtualPortCapLoopConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapLoopConfig.setStatus(_A)
_VirtualPortCapVcType_Type=VirtualContainerTypeCaps
_VirtualPortCapVcType_Object=MibTableColumn
virtualPortCapVcType=_VirtualPortCapVcType_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,60),_VirtualPortCapVcType_Type())
virtualPortCapVcType.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapVcType.setStatus(_A)
_VirtualPortCapCir_Type=FspR7Unsigned32Caps
_VirtualPortCapCir_Object=MibTableColumn
virtualPortCapCir=_VirtualPortCapCir_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,61),_VirtualPortCapCir_Type())
virtualPortCapCir.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapCir.setStatus(_A)
if mibBuilder.loadTexts:virtualPortCapCir.setUnits('Mbps')
_VirtualPortCapOpuPayloadType_Type=FspR7OpuPayloadTypeCaps
_VirtualPortCapOpuPayloadType_Object=MibTableColumn
virtualPortCapOpuPayloadType=_VirtualPortCapOpuPayloadType_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,62),_VirtualPortCapOpuPayloadType_Type())
virtualPortCapOpuPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapOpuPayloadType.setStatus(_A)
_VirtualPortCapOtnStuffing_Type=FspR7StuffCaps
_VirtualPortCapOtnStuffing_Object=MibTableColumn
virtualPortCapOtnStuffing=_VirtualPortCapOtnStuffing_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,63),_VirtualPortCapOtnStuffing_Type())
virtualPortCapOtnStuffing.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapOtnStuffing.setStatus(_A)
_VirtualPortCapRedLineState_Type=FspR7RedLinedStateCaps
_VirtualPortCapRedLineState_Object=MibTableColumn
virtualPortCapRedLineState=_VirtualPortCapRedLineState_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,64),_VirtualPortCapRedLineState_Type())
virtualPortCapRedLineState.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapRedLineState.setStatus(_A)
_VirtualPortCapTunnelAid_Type=Integer32
_VirtualPortCapTunnelAid_Object=MibTableColumn
virtualPortCapTunnelAid=_VirtualPortCapTunnelAid_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,65),_VirtualPortCapTunnelAid_Type())
virtualPortCapTunnelAid.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTunnelAid.setStatus(_A)
_VirtualPortCapTrafficDirection_Type=FspR7TrafficDirectionCaps
_VirtualPortCapTrafficDirection_Object=MibTableColumn
virtualPortCapTrafficDirection=_VirtualPortCapTrafficDirection_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,66),_VirtualPortCapTrafficDirection_Type())
virtualPortCapTrafficDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapTrafficDirection.setStatus(_A)
_VirtualPortCapChannelId_Type=FspR7SnmpLongString
_VirtualPortCapChannelId_Object=MibTableColumn
virtualPortCapChannelId=_VirtualPortCapChannelId_Object((1,3,6,1,4,1,2544,1,11,9,3,4,2,1,67),_VirtualPortCapChannelId_Type())
virtualPortCapChannelId.setMaxAccess(_B)
if mibBuilder.loadTexts:virtualPortCapChannelId.setStatus(_A)
_EndOfVirtualPortCapTable_Type=Integer32
_EndOfVirtualPortCapTable_Object=MibScalar
endOfVirtualPortCapTable=_EndOfVirtualPortCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,4,3),_EndOfVirtualPortCapTable_Type())
endOfVirtualPortCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfVirtualPortCapTable.setStatus(_A)
_EndOfFacilityMgmtCap_Type=Integer32
_EndOfFacilityMgmtCap_Object=MibScalar
endOfFacilityMgmtCap=_EndOfFacilityMgmtCap_Object((1,3,6,1,4,1,2544,1,11,9,3,4,10000),_EndOfFacilityMgmtCap_Type())
endOfFacilityMgmtCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfFacilityMgmtCap.setStatus(_A)
_DcnMgmtCap_ObjectIdentity=ObjectIdentity
dcnMgmtCap=_DcnMgmtCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,3,5))
_LinkCapTable_Object=MibTable
linkCapTable=_LinkCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,5,1))
if mibBuilder.loadTexts:linkCapTable.setStatus(_A)
_LinkCapEntry_Object=MibTableRow
linkCapEntry=_LinkCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,3,5,1,1))
linkCapEntry.setIndexNames((0,_C,_S),(0,_C,_T),(0,_C,_R),(0,_C,_Q),(0,_C,_P))
if mibBuilder.loadTexts:linkCapEntry.setStatus(_A)
_LinkCapRowStatus_Type=FspR7RowStatusCaps
_LinkCapRowStatus_Object=MibTableColumn
linkCapRowStatus=_LinkCapRowStatus_Object((1,3,6,1,4,1,2544,1,11,9,3,5,1,1,1),_LinkCapRowStatus_Type())
linkCapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:linkCapRowStatus.setStatus(_A)
_LinkCapType_Type=FspR7InterfaceTypeCaps
_LinkCapType_Object=MibTableColumn
linkCapType=_LinkCapType_Object((1,3,6,1,4,1,2544,1,11,9,3,5,1,1,2),_LinkCapType_Type())
linkCapType.setMaxAccess(_B)
if mibBuilder.loadTexts:linkCapType.setStatus(_A)
_LinkCapAdmin_Type=FspR7AdminStateCaps
_LinkCapAdmin_Object=MibTableColumn
linkCapAdmin=_LinkCapAdmin_Object((1,3,6,1,4,1,2544,1,11,9,3,5,1,1,3),_LinkCapAdmin_Type())
linkCapAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:linkCapAdmin.setStatus(_A)
_LinkCapAlias_Type=Integer32
_LinkCapAlias_Object=MibTableColumn
linkCapAlias=_LinkCapAlias_Object((1,3,6,1,4,1,2544,1,11,9,3,5,1,1,4),_LinkCapAlias_Type())
linkCapAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:linkCapAlias.setStatus(_A)
_LinkCapAuthString_Type=Integer32
_LinkCapAuthString_Object=MibTableColumn
linkCapAuthString=_LinkCapAuthString_Object((1,3,6,1,4,1,2544,1,11,9,3,5,1,1,5),_LinkCapAuthString_Type())
linkCapAuthString.setMaxAccess(_B)
if mibBuilder.loadTexts:linkCapAuthString.setStatus(_A)
_LinkCapProxyArp_Type=FspR7NoYesCaps
_LinkCapProxyArp_Object=MibTableColumn
linkCapProxyArp=_LinkCapProxyArp_Object((1,3,6,1,4,1,2544,1,11,9,3,5,1,1,6),_LinkCapProxyArp_Type())
linkCapProxyArp.setMaxAccess(_B)
if mibBuilder.loadTexts:linkCapProxyArp.setStatus(_A)
_LinkCapOspf_Type=FspR7OspfModeCaps
_LinkCapOspf_Object=MibTableColumn
linkCapOspf=_LinkCapOspf_Object((1,3,6,1,4,1,2544,1,11,9,3,5,1,1,7),_LinkCapOspf_Type())
linkCapOspf.setMaxAccess(_B)
if mibBuilder.loadTexts:linkCapOspf.setStatus(_A)
_LinkCapBaud_Type=FspR7BaundCaps
_LinkCapBaud_Object=MibTableColumn
linkCapBaud=_LinkCapBaud_Object((1,3,6,1,4,1,2544,1,11,9,3,5,1,1,8),_LinkCapBaud_Type())
linkCapBaud.setMaxAccess(_B)
if mibBuilder.loadTexts:linkCapBaud.setStatus(_A)
_LinkCapAuthType_Type=FspR7CpAuthTypeCaps
_LinkCapAuthType_Object=MibTableColumn
linkCapAuthType=_LinkCapAuthType_Object((1,3,6,1,4,1,2544,1,11,9,3,5,1,1,9),_LinkCapAuthType_Type())
linkCapAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:linkCapAuthType.setStatus(_A)
_LinkCapIpType_Type=FspR7IpTypeCaps
_LinkCapIpType_Object=MibTableColumn
linkCapIpType=_LinkCapIpType_Object((1,3,6,1,4,1,2544,1,11,9,3,5,1,1,10),_LinkCapIpType_Type())
linkCapIpType.setMaxAccess(_B)
if mibBuilder.loadTexts:linkCapIpType.setStatus(_A)
_LinkCapMetric_Type=FspR7Unsigned32Caps
_LinkCapMetric_Object=MibTableColumn
linkCapMetric=_LinkCapMetric_Object((1,3,6,1,4,1,2544,1,11,9,3,5,1,1,11),_LinkCapMetric_Type())
linkCapMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:linkCapMetric.setStatus(_A)
_LinkCapAreaAid_Type=SnmpAdminString
_LinkCapAreaAid_Object=MibTableColumn
linkCapAreaAid=_LinkCapAreaAid_Object((1,3,6,1,4,1,2544,1,11,9,3,5,1,1,12),_LinkCapAreaAid_Type())
linkCapAreaAid.setMaxAccess(_B)
if mibBuilder.loadTexts:linkCapAreaAid.setStatus(_A)
_LinkCapNearEndIp_Type=FspR7YesNo
_LinkCapNearEndIp_Object=MibTableColumn
linkCapNearEndIp=_LinkCapNearEndIp_Object((1,3,6,1,4,1,2544,1,11,9,3,5,1,1,13),_LinkCapNearEndIp_Type())
linkCapNearEndIp.setMaxAccess(_B)
if mibBuilder.loadTexts:linkCapNearEndIp.setStatus(_A)
_LinkCapBitrate_Type=FspR7Unsigned32Caps
_LinkCapBitrate_Object=MibTableColumn
linkCapBitrate=_LinkCapBitrate_Object((1,3,6,1,4,1,2544,1,11,9,3,5,1,1,14),_LinkCapBitrate_Type())
linkCapBitrate.setMaxAccess(_B)
if mibBuilder.loadTexts:linkCapBitrate.setStatus(_A)
if mibBuilder.loadTexts:linkCapBitrate.setUnits('kbps')
_LinkCapIPv6Type_Type=FspR7IPv6TypeCaps
_LinkCapIPv6Type_Object=MibTableColumn
linkCapIPv6Type=_LinkCapIPv6Type_Object((1,3,6,1,4,1,2544,1,11,9,3,5,1,1,15),_LinkCapIPv6Type_Type())
linkCapIPv6Type.setMaxAccess(_B)
if mibBuilder.loadTexts:linkCapIPv6Type.setStatus(_A)
_LinkCapNendIPv6_Type=FspR7YesNo
_LinkCapNendIPv6_Object=MibTableColumn
linkCapNendIPv6=_LinkCapNendIPv6_Object((1,3,6,1,4,1,2544,1,11,9,3,5,1,1,16),_LinkCapNendIPv6_Type())
linkCapNendIPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:linkCapNendIPv6.setStatus(_A)
_EndOfLinkCapTable_Type=Integer32
_EndOfLinkCapTable_Object=MibScalar
endOfLinkCapTable=_EndOfLinkCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,5,2),_EndOfLinkCapTable_Type())
endOfLinkCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfLinkCapTable.setStatus(_A)
_ScCapTable_Object=MibTable
scCapTable=_ScCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3))
if mibBuilder.loadTexts:scCapTable.setStatus(_A)
_ScCapEntry_Object=MibTableRow
scCapEntry=_ScCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1))
scCapEntry.setIndexNames((0,_C,_S),(0,_C,_T),(0,_C,_R),(0,_C,_Q),(0,_C,_P))
if mibBuilder.loadTexts:scCapEntry.setStatus(_A)
_ScCapRowStatus_Type=FspR7RowStatusCaps
_ScCapRowStatus_Object=MibTableColumn
scCapRowStatus=_ScCapRowStatus_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1,1),_ScCapRowStatus_Type())
scCapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:scCapRowStatus.setStatus(_A)
_ScCapType_Type=FspR7InterfaceTypeCaps
_ScCapType_Object=MibTableColumn
scCapType=_ScCapType_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1,2),_ScCapType_Type())
scCapType.setMaxAccess(_B)
if mibBuilder.loadTexts:scCapType.setStatus(_A)
_ScCapAdmin_Type=FspR7AdminStateCaps
_ScCapAdmin_Object=MibTableColumn
scCapAdmin=_ScCapAdmin_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1,3),_ScCapAdmin_Type())
scCapAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:scCapAdmin.setStatus(_A)
_ScCapAlias_Type=Integer32
_ScCapAlias_Object=MibTableColumn
scCapAlias=_ScCapAlias_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1,4),_ScCapAlias_Type())
scCapAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:scCapAlias.setStatus(_A)
_ScCapAuthString_Type=Integer32
_ScCapAuthString_Object=MibTableColumn
scCapAuthString=_ScCapAuthString_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1,5),_ScCapAuthString_Type())
scCapAuthString.setMaxAccess(_B)
if mibBuilder.loadTexts:scCapAuthString.setStatus(_A)
_ScCapOspf_Type=FspR7OspfModeCaps
_ScCapOspf_Object=MibTableColumn
scCapOspf=_ScCapOspf_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1,6),_ScCapOspf_Type())
scCapOspf.setMaxAccess(_B)
if mibBuilder.loadTexts:scCapOspf.setStatus(_A)
_ScCapAuthType_Type=FspR7CpAuthTypeCaps
_ScCapAuthType_Object=MibTableColumn
scCapAuthType=_ScCapAuthType_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1,7),_ScCapAuthType_Type())
scCapAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:scCapAuthType.setStatus(_A)
_ScCapIpType_Type=FspR7IpTypeCaps
_ScCapIpType_Object=MibTableColumn
scCapIpType=_ScCapIpType_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1,8),_ScCapIpType_Type())
scCapIpType.setMaxAccess(_B)
if mibBuilder.loadTexts:scCapIpType.setStatus(_A)
_ScCapMetric_Type=FspR7Unsigned32Caps
_ScCapMetric_Object=MibTableColumn
scCapMetric=_ScCapMetric_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1,9),_ScCapMetric_Type())
scCapMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:scCapMetric.setStatus(_A)
_ScCapAreaAid_Type=SnmpAdminString
_ScCapAreaAid_Object=MibTableColumn
scCapAreaAid=_ScCapAreaAid_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1,10),_ScCapAreaAid_Type())
scCapAreaAid.setMaxAccess(_B)
if mibBuilder.loadTexts:scCapAreaAid.setStatus(_A)
_ScCapAlsMode_Type=FspR7AlsModeCaps
_ScCapAlsMode_Object=MibTableColumn
scCapAlsMode=_ScCapAlsMode_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1,11),_ScCapAlsMode_Type())
scCapAlsMode.setMaxAccess(_B)
if mibBuilder.loadTexts:scCapAlsMode.setStatus(_A)
_ScCapSigDegThresReceiver_Type=FspR7Unsigned32Caps
_ScCapSigDegThresReceiver_Object=MibTableColumn
scCapSigDegThresReceiver=_ScCapSigDegThresReceiver_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1,12),_ScCapSigDegThresReceiver_Type())
scCapSigDegThresReceiver.setMaxAccess(_B)
if mibBuilder.loadTexts:scCapSigDegThresReceiver.setStatus(_A)
if mibBuilder.loadTexts:scCapSigDegThresReceiver.setUnits(_F)
_ScCapAutonegotiation_Type=EnableStateCaps
_ScCapAutonegotiation_Object=MibTableColumn
scCapAutonegotiation=_ScCapAutonegotiation_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1,13),_ScCapAutonegotiation_Type())
scCapAutonegotiation.setMaxAccess(_B)
if mibBuilder.loadTexts:scCapAutonegotiation.setStatus(_A)
_ScCapBitrate_Type=FspR7BitrateCaps
_ScCapBitrate_Object=MibTableColumn
scCapBitrate=_ScCapBitrate_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1,14),_ScCapBitrate_Type())
scCapBitrate.setMaxAccess(_B)
if mibBuilder.loadTexts:scCapBitrate.setStatus(_A)
_ScCapDuplex_Type=EthDuplexModeCaps
_ScCapDuplex_Object=MibTableColumn
scCapDuplex=_ScCapDuplex_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1,15),_ScCapDuplex_Type())
scCapDuplex.setMaxAccess(_B)
if mibBuilder.loadTexts:scCapDuplex.setStatus(_A)
_ScCapAttGradientTh_Type=FspR7Unsigned32Caps
_ScCapAttGradientTh_Object=MibTableColumn
scCapAttGradientTh=_ScCapAttGradientTh_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1,16),_ScCapAttGradientTh_Type())
scCapAttGradientTh.setMaxAccess(_B)
if mibBuilder.loadTexts:scCapAttGradientTh.setStatus(_A)
if mibBuilder.loadTexts:scCapAttGradientTh.setUnits(_Ah)
_ScCapIpAddr_Type=FspR7YesNo
_ScCapIpAddr_Object=MibTableColumn
scCapIpAddr=_ScCapIpAddr_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1,17),_ScCapIpAddr_Type())
scCapIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:scCapIpAddr.setStatus(_A)
_ScCapLanAid_Type=SnmpAdminString
_ScCapLanAid_Object=MibTableColumn
scCapLanAid=_ScCapLanAid_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1,18),_ScCapLanAid_Type())
scCapLanAid.setMaxAccess(_B)
if mibBuilder.loadTexts:scCapLanAid.setStatus(_A)
_ScCapIpMask_Type=FspR7YesNo
_ScCapIpMask_Object=MibTableColumn
scCapIpMask=_ScCapIpMask_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1,19),_ScCapIpMask_Type())
scCapIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:scCapIpMask.setStatus(_A)
_ScCapDataLayerPmReset_Type=FspR7PmResetCaps
_ScCapDataLayerPmReset_Object=MibTableColumn
scCapDataLayerPmReset=_ScCapDataLayerPmReset_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1,20),_ScCapDataLayerPmReset_Type())
scCapDataLayerPmReset.setMaxAccess(_B)
if mibBuilder.loadTexts:scCapDataLayerPmReset.setStatus(_A)
_ScCapPriority_Type=FspR7Unsigned32Caps
_ScCapPriority_Object=MibTableColumn
scCapPriority=_ScCapPriority_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1,21),_ScCapPriority_Type())
scCapPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:scCapPriority.setStatus(_A)
_ScCapIPv6_Type=FspR7YesNo
_ScCapIPv6_Object=MibTableColumn
scCapIPv6=_ScCapIPv6_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1,22),_ScCapIPv6_Type())
scCapIPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:scCapIPv6.setStatus(_A)
_ScCapIPv6PrefixLen_Type=FspR7Unsigned32Caps
_ScCapIPv6PrefixLen_Object=MibTableColumn
scCapIPv6PrefixLen=_ScCapIPv6PrefixLen_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1,23),_ScCapIPv6PrefixLen_Type())
scCapIPv6PrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:scCapIPv6PrefixLen.setStatus(_A)
_ScCapIpMode_Type=FspR7IpModeCaps
_ScCapIpMode_Object=MibTableColumn
scCapIpMode=_ScCapIpMode_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1,24),_ScCapIpMode_Type())
scCapIpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:scCapIpMode.setStatus(_A)
_ScCapGatewayProxyArp_Type=FspR7EnableDisableCaps
_ScCapGatewayProxyArp_Object=MibTableColumn
scCapGatewayProxyArp=_ScCapGatewayProxyArp_Object((1,3,6,1,4,1,2544,1,11,9,3,5,3,1,25),_ScCapGatewayProxyArp_Type())
scCapGatewayProxyArp.setMaxAccess(_B)
if mibBuilder.loadTexts:scCapGatewayProxyArp.setStatus(_A)
_EndOfScCapTable_Type=Integer32
_EndOfScCapTable_Object=MibScalar
endOfScCapTable=_EndOfScCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,5,4),_EndOfScCapTable_Type())
endOfScCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfScCapTable.setStatus(_A)
_LanCapTable_Object=MibTable
lanCapTable=_LanCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,5,5))
if mibBuilder.loadTexts:lanCapTable.setStatus(_A)
_LanCapEntry_Object=MibTableRow
lanCapEntry=_LanCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,3,5,5,1))
lanCapEntry.setIndexNames((0,_C,_S),(0,_C,_T),(0,_C,_R),(0,_C,_Q),(0,_C,_P))
if mibBuilder.loadTexts:lanCapEntry.setStatus(_A)
_LanCapRowStatus_Type=FspR7RowStatusCaps
_LanCapRowStatus_Object=MibTableColumn
lanCapRowStatus=_LanCapRowStatus_Object((1,3,6,1,4,1,2544,1,11,9,3,5,5,1,1),_LanCapRowStatus_Type())
lanCapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:lanCapRowStatus.setStatus(_A)
_LanCapType_Type=FspR7InterfaceTypeCaps
_LanCapType_Object=MibTableColumn
lanCapType=_LanCapType_Object((1,3,6,1,4,1,2544,1,11,9,3,5,5,1,2),_LanCapType_Type())
lanCapType.setMaxAccess(_B)
if mibBuilder.loadTexts:lanCapType.setStatus(_A)
_LanCapAdmin_Type=FspR7AdminStateCaps
_LanCapAdmin_Object=MibTableColumn
lanCapAdmin=_LanCapAdmin_Object((1,3,6,1,4,1,2544,1,11,9,3,5,5,1,3),_LanCapAdmin_Type())
lanCapAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:lanCapAdmin.setStatus(_A)
_LanCapAlias_Type=Integer32
_LanCapAlias_Object=MibTableColumn
lanCapAlias=_LanCapAlias_Object((1,3,6,1,4,1,2544,1,11,9,3,5,5,1,4),_LanCapAlias_Type())
lanCapAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:lanCapAlias.setStatus(_A)
_LanCapAuthString_Type=Integer32
_LanCapAuthString_Object=MibTableColumn
lanCapAuthString=_LanCapAuthString_Object((1,3,6,1,4,1,2544,1,11,9,3,5,5,1,5),_LanCapAuthString_Type())
lanCapAuthString.setMaxAccess(_B)
if mibBuilder.loadTexts:lanCapAuthString.setStatus(_A)
_LanCapOspf_Type=FspR7OspfModeCaps
_LanCapOspf_Object=MibTableColumn
lanCapOspf=_LanCapOspf_Object((1,3,6,1,4,1,2544,1,11,9,3,5,5,1,6),_LanCapOspf_Type())
lanCapOspf.setMaxAccess(_B)
if mibBuilder.loadTexts:lanCapOspf.setStatus(_A)
_LanCapAuthType_Type=FspR7CpAuthTypeCaps
_LanCapAuthType_Object=MibTableColumn
lanCapAuthType=_LanCapAuthType_Object((1,3,6,1,4,1,2544,1,11,9,3,5,5,1,7),_LanCapAuthType_Type())
lanCapAuthType.setMaxAccess(_B)
if mibBuilder.loadTexts:lanCapAuthType.setStatus(_A)
_LanCapIpType_Type=FspR7IpTypeCaps
_LanCapIpType_Object=MibTableColumn
lanCapIpType=_LanCapIpType_Object((1,3,6,1,4,1,2544,1,11,9,3,5,5,1,8),_LanCapIpType_Type())
lanCapIpType.setMaxAccess(_B)
if mibBuilder.loadTexts:lanCapIpType.setStatus(_A)
_LanCapMetric_Type=FspR7Unsigned32Caps
_LanCapMetric_Object=MibTableColumn
lanCapMetric=_LanCapMetric_Object((1,3,6,1,4,1,2544,1,11,9,3,5,5,1,9),_LanCapMetric_Type())
lanCapMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:lanCapMetric.setStatus(_A)
_LanCapAreaAid_Type=SnmpAdminString
_LanCapAreaAid_Object=MibTableColumn
lanCapAreaAid=_LanCapAreaAid_Object((1,3,6,1,4,1,2544,1,11,9,3,5,5,1,10),_LanCapAreaAid_Type())
lanCapAreaAid.setMaxAccess(_B)
if mibBuilder.loadTexts:lanCapAreaAid.setStatus(_A)
_LanCapIpAddr_Type=FspR7YesNo
_LanCapIpAddr_Object=MibTableColumn
lanCapIpAddr=_LanCapIpAddr_Object((1,3,6,1,4,1,2544,1,11,9,3,5,5,1,11),_LanCapIpAddr_Type())
lanCapIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:lanCapIpAddr.setStatus(_A)
_LanCapIpMask_Type=FspR7YesNo
_LanCapIpMask_Object=MibTableColumn
lanCapIpMask=_LanCapIpMask_Object((1,3,6,1,4,1,2544,1,11,9,3,5,5,1,12),_LanCapIpMask_Type())
lanCapIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:lanCapIpMask.setStatus(_A)
_LanCapPriority_Type=FspR7Unsigned32Caps
_LanCapPriority_Object=MibTableColumn
lanCapPriority=_LanCapPriority_Object((1,3,6,1,4,1,2544,1,11,9,3,5,5,1,13),_LanCapPriority_Type())
lanCapPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:lanCapPriority.setStatus(_A)
_LanCapIPv6_Type=FspR7YesNo
_LanCapIPv6_Object=MibTableColumn
lanCapIPv6=_LanCapIPv6_Object((1,3,6,1,4,1,2544,1,11,9,3,5,5,1,14),_LanCapIPv6_Type())
lanCapIPv6.setMaxAccess(_B)
if mibBuilder.loadTexts:lanCapIPv6.setStatus(_A)
_LanCapIPv6PrefixLen_Type=FspR7Unsigned32Caps
_LanCapIPv6PrefixLen_Object=MibTableColumn
lanCapIPv6PrefixLen=_LanCapIPv6PrefixLen_Object((1,3,6,1,4,1,2544,1,11,9,3,5,5,1,15),_LanCapIPv6PrefixLen_Type())
lanCapIPv6PrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:lanCapIPv6PrefixLen.setStatus(_A)
_LanCapIpMode_Type=FspR7IpModeCaps
_LanCapIpMode_Object=MibTableColumn
lanCapIpMode=_LanCapIpMode_Object((1,3,6,1,4,1,2544,1,11,9,3,5,5,1,16),_LanCapIpMode_Type())
lanCapIpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:lanCapIpMode.setStatus(_A)
_EndOfLanCapTable_Type=Integer32
_EndOfLanCapTable_Object=MibScalar
endOfLanCapTable=_EndOfLanCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,5,6),_EndOfLanCapTable_Type())
endOfLanCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfLanCapTable.setStatus(_A)
_EccCapTable_Object=MibTable
eccCapTable=_EccCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,5,7))
if mibBuilder.loadTexts:eccCapTable.setStatus(_A)
_EccCapEntry_Object=MibTableRow
eccCapEntry=_EccCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,3,5,7,1))
eccCapEntry.setIndexNames((0,_C,_S),(0,_C,_T),(0,_C,_R),(0,_C,_Q),(0,_C,_P))
if mibBuilder.loadTexts:eccCapEntry.setStatus(_A)
_EccCapRowStatus_Type=FspR7RowStatusCaps
_EccCapRowStatus_Object=MibTableColumn
eccCapRowStatus=_EccCapRowStatus_Object((1,3,6,1,4,1,2544,1,11,9,3,5,7,1,1),_EccCapRowStatus_Type())
eccCapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:eccCapRowStatus.setStatus(_A)
_EccCapType_Type=FspR7InterfaceTypeCaps
_EccCapType_Object=MibTableColumn
eccCapType=_EccCapType_Object((1,3,6,1,4,1,2544,1,11,9,3,5,7,1,2),_EccCapType_Type())
eccCapType.setMaxAccess(_B)
if mibBuilder.loadTexts:eccCapType.setStatus(_A)
_EccCapAdmin_Type=FspR7AdminStateCaps
_EccCapAdmin_Object=MibTableColumn
eccCapAdmin=_EccCapAdmin_Object((1,3,6,1,4,1,2544,1,11,9,3,5,7,1,3),_EccCapAdmin_Type())
eccCapAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:eccCapAdmin.setStatus(_A)
_EccCapAlias_Type=Integer32
_EccCapAlias_Object=MibTableColumn
eccCapAlias=_EccCapAlias_Object((1,3,6,1,4,1,2544,1,11,9,3,5,7,1,4),_EccCapAlias_Type())
eccCapAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:eccCapAlias.setStatus(_A)
_EccCapLanAid_Type=SnmpAdminString
_EccCapLanAid_Object=MibTableColumn
eccCapLanAid=_EccCapLanAid_Object((1,3,6,1,4,1,2544,1,11,9,3,5,7,1,5),_EccCapLanAid_Type())
eccCapLanAid.setMaxAccess(_B)
if mibBuilder.loadTexts:eccCapLanAid.setStatus(_A)
_EccCapExternalVid_Type=Unsigned32
_EccCapExternalVid_Object=MibTableColumn
eccCapExternalVid=_EccCapExternalVid_Object((1,3,6,1,4,1,2544,1,11,9,3,5,7,1,6),_EccCapExternalVid_Type())
eccCapExternalVid.setMaxAccess(_B)
if mibBuilder.loadTexts:eccCapExternalVid.setStatus(_A)
_EndOfEccCapTable_Type=Integer32
_EndOfEccCapTable_Object=MibScalar
endOfEccCapTable=_EndOfEccCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,5,8),_EndOfEccCapTable_Type())
endOfEccCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfEccCapTable.setStatus(_A)
_EndOfDcnMgmtCap_Type=Integer32
_EndOfDcnMgmtCap_Object=MibScalar
endOfDcnMgmtCap=_EndOfDcnMgmtCap_Object((1,3,6,1,4,1,2544,1,11,9,3,5,10000),_EndOfDcnMgmtCap_Type())
endOfDcnMgmtCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfDcnMgmtCap.setStatus(_A)
_OpticalMuxMgmtCap_ObjectIdentity=ObjectIdentity
opticalMuxMgmtCap=_OpticalMuxMgmtCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,3,6))
_OpticalMuxCapTable_Object=MibTable
opticalMuxCapTable=_OpticalMuxCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1))
if mibBuilder.loadTexts:opticalMuxCapTable.setStatus(_A)
_OpticalMuxCapEntry_Object=MibTableRow
opticalMuxCapEntry=_OpticalMuxCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1))
opticalMuxCapEntry.setIndexNames((0,_C,_i),(0,_C,_j),(0,_C,_h),(0,_C,_g),(0,_C,_f))
if mibBuilder.loadTexts:opticalMuxCapEntry.setStatus(_A)
_OpticalMuxCapRowStatus_Type=FspR7RowStatusCaps
_OpticalMuxCapRowStatus_Object=MibTableColumn
opticalMuxCapRowStatus=_OpticalMuxCapRowStatus_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,1),_OpticalMuxCapRowStatus_Type())
opticalMuxCapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapRowStatus.setStatus(_A)
_OpticalMuxCapPumpPower_Type=FspR7Integer32Caps
_OpticalMuxCapPumpPower_Object=MibTableColumn
opticalMuxCapPumpPower=_OpticalMuxCapPumpPower_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,2),_OpticalMuxCapPumpPower_Type())
opticalMuxCapPumpPower.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapPumpPower.setStatus(_A)
if mibBuilder.loadTexts:opticalMuxCapPumpPower.setUnits('0.2 dBm')
_OpticalMuxCapInhibitSwitchToWork_Type=FspR7YesNoCaps
_OpticalMuxCapInhibitSwitchToWork_Object=MibTableColumn
opticalMuxCapInhibitSwitchToWork=_OpticalMuxCapInhibitSwitchToWork_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,3),_OpticalMuxCapInhibitSwitchToWork_Type())
opticalMuxCapInhibitSwitchToWork.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapInhibitSwitchToWork.setStatus(_A)
_OpticalMuxCapForceLaserOn_Type=FspR7LaserForcedOperationCaps
_OpticalMuxCapForceLaserOn_Object=MibTableColumn
opticalMuxCapForceLaserOn=_OpticalMuxCapForceLaserOn_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,4),_OpticalMuxCapForceLaserOn_Type())
opticalMuxCapForceLaserOn.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapForceLaserOn.setStatus(_A)
_OpticalMuxCapAseTabCreation_Type=FspR7AseTabOprCaps
_OpticalMuxCapAseTabCreation_Object=MibTableColumn
opticalMuxCapAseTabCreation=_OpticalMuxCapAseTabCreation_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,5),_OpticalMuxCapAseTabCreation_Type())
opticalMuxCapAseTabCreation.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapAseTabCreation.setStatus(_A)
_OpticalMuxCapOpticalSetPoint_Type=FspR7Integer32Caps
_OpticalMuxCapOpticalSetPoint_Object=MibTableColumn
opticalMuxCapOpticalSetPoint=_OpticalMuxCapOpticalSetPoint_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,6),_OpticalMuxCapOpticalSetPoint_Type())
opticalMuxCapOpticalSetPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapOpticalSetPoint.setStatus(_A)
if mibBuilder.loadTexts:opticalMuxCapOpticalSetPoint.setUnits(_E)
_OpticalMuxCapInitiateEqualization_Type=FspR7InitEqualizationCaps
_OpticalMuxCapInitiateEqualization_Object=MibTableColumn
opticalMuxCapInitiateEqualization=_OpticalMuxCapInitiateEqualization_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,7),_OpticalMuxCapInitiateEqualization_Type())
opticalMuxCapInitiateEqualization.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapInitiateEqualization.setStatus(_A)
_OpticalMuxCapTilt_Type=FspR7Integer32Caps
_OpticalMuxCapTilt_Object=MibTableColumn
opticalMuxCapTilt=_OpticalMuxCapTilt_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,8),_OpticalMuxCapTilt_Type())
opticalMuxCapTilt.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapTilt.setStatus(_A)
if mibBuilder.loadTexts:opticalMuxCapTilt.setUnits(_F)
_OpticalMuxCapOscOpticalSetpoint_Type=FspR7Integer32Caps
_OpticalMuxCapOscOpticalSetpoint_Object=MibTableColumn
opticalMuxCapOscOpticalSetpoint=_OpticalMuxCapOscOpticalSetpoint_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,9),_OpticalMuxCapOscOpticalSetpoint_Type())
opticalMuxCapOscOpticalSetpoint.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapOscOpticalSetpoint.setStatus(_A)
if mibBuilder.loadTexts:opticalMuxCapOscOpticalSetpoint.setUnits(_E)
_OpticalMuxCapOffset_Type=FspR7Integer32Caps
_OpticalMuxCapOffset_Object=MibTableColumn
opticalMuxCapOffset=_OpticalMuxCapOffset_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,10),_OpticalMuxCapOffset_Type())
opticalMuxCapOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapOffset.setStatus(_A)
if mibBuilder.loadTexts:opticalMuxCapOffset.setUnits(_F)
_OpticalMuxCapSwitchCommand_Type=FspR7APSCommandCaps
_OpticalMuxCapSwitchCommand_Object=MibTableColumn
opticalMuxCapSwitchCommand=_OpticalMuxCapSwitchCommand_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,11),_OpticalMuxCapSwitchCommand_Type())
opticalMuxCapSwitchCommand.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapSwitchCommand.setStatus(_A)
_OpticalMuxCapAlsMode_Type=FspR7AlsModeCaps
_OpticalMuxCapAlsMode_Object=MibTableColumn
opticalMuxCapAlsMode=_OpticalMuxCapAlsMode_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,12),_OpticalMuxCapAlsMode_Type())
opticalMuxCapAlsMode.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapAlsMode.setStatus(_A)
_OpticalMuxCapType_Type=FspR7InterfaceTypeCaps
_OpticalMuxCapType_Object=MibTableColumn
opticalMuxCapType=_OpticalMuxCapType_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,13),_OpticalMuxCapType_Type())
opticalMuxCapType.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapType.setStatus(_A)
_OpticalMuxCapAttenuationGradient_Type=FspR7Unsigned32Caps
_OpticalMuxCapAttenuationGradient_Object=MibTableColumn
opticalMuxCapAttenuationGradient=_OpticalMuxCapAttenuationGradient_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,14),_OpticalMuxCapAttenuationGradient_Type())
opticalMuxCapAttenuationGradient.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapAttenuationGradient.setStatus(_A)
if mibBuilder.loadTexts:opticalMuxCapAttenuationGradient.setUnits(_Ah)
_OpticalMuxCapInhibitSwitchToProt_Type=FspR7YesNoCaps
_OpticalMuxCapInhibitSwitchToProt_Object=MibTableColumn
opticalMuxCapInhibitSwitchToProt=_OpticalMuxCapInhibitSwitchToProt_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,15),_OpticalMuxCapInhibitSwitchToProt_Type())
opticalMuxCapInhibitSwitchToProt.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapInhibitSwitchToProt.setStatus(_A)
_OpticalMuxCapVariableGain_Type=FspR7Unsigned32Caps
_OpticalMuxCapVariableGain_Object=MibTableColumn
opticalMuxCapVariableGain=_OpticalMuxCapVariableGain_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,16),_OpticalMuxCapVariableGain_Type())
opticalMuxCapVariableGain.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapVariableGain.setStatus(_A)
if mibBuilder.loadTexts:opticalMuxCapVariableGain.setUnits(_F)
_OpticalMuxCapAdmin_Type=FspR7AdminStateCaps
_OpticalMuxCapAdmin_Object=MibTableColumn
opticalMuxCapAdmin=_OpticalMuxCapAdmin_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,17),_OpticalMuxCapAdmin_Type())
opticalMuxCapAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapAdmin.setStatus(_A)
_OpticalMuxCapTimePeriod_Type=FspR7OtdrPeriodCaps
_OpticalMuxCapTimePeriod_Object=MibTableColumn
opticalMuxCapTimePeriod=_OpticalMuxCapTimePeriod_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,18),_OpticalMuxCapTimePeriod_Type())
opticalMuxCapTimePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapTimePeriod.setStatus(_A)
_OpticalMuxCapSigDegThresReceiver_Type=FspR7Unsigned32Caps
_OpticalMuxCapSigDegThresReceiver_Object=MibTableColumn
opticalMuxCapSigDegThresReceiver=_OpticalMuxCapSigDegThresReceiver_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,19),_OpticalMuxCapSigDegThresReceiver_Type())
opticalMuxCapSigDegThresReceiver.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapSigDegThresReceiver.setStatus(_A)
if mibBuilder.loadTexts:opticalMuxCapSigDegThresReceiver.setUnits(_F)
_OpticalMuxCapAlias_Type=Integer32
_OpticalMuxCapAlias_Object=MibTableColumn
opticalMuxCapAlias=_OpticalMuxCapAlias_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,20),_OpticalMuxCapAlias_Type())
opticalMuxCapAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapAlias.setStatus(_A)
_OpticalMuxCapDataLayerPmReset_Type=FspR7PmResetCaps
_OpticalMuxCapDataLayerPmReset_Object=MibTableColumn
opticalMuxCapDataLayerPmReset=_OpticalMuxCapDataLayerPmReset_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,21),_OpticalMuxCapDataLayerPmReset_Type())
opticalMuxCapDataLayerPmReset.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapDataLayerPmReset.setStatus(_A)
_OpticalMuxCapGain_Type=FspR7GainCaps
_OpticalMuxCapGain_Object=MibTableColumn
opticalMuxCapGain=_OpticalMuxCapGain_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,22),_OpticalMuxCapGain_Type())
opticalMuxCapGain.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapGain.setStatus(_A)
_OpticalMuxCapEdfaPwrOut_Type=FspR7EdfaOutputPowerRatingCaps
_OpticalMuxCapEdfaPwrOut_Object=MibTableColumn
opticalMuxCapEdfaPwrOut=_OpticalMuxCapEdfaPwrOut_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,23),_OpticalMuxCapEdfaPwrOut_Type())
opticalMuxCapEdfaPwrOut.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapEdfaPwrOut.setStatus(_A)
_OpticalMuxCapVoaSetpoint_Type=FspR7Unsigned32Caps
_OpticalMuxCapVoaSetpoint_Object=MibTableColumn
opticalMuxCapVoaSetpoint=_OpticalMuxCapVoaSetpoint_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,24),_OpticalMuxCapVoaSetpoint_Type())
opticalMuxCapVoaSetpoint.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapVoaSetpoint.setStatus(_A)
if mibBuilder.loadTexts:opticalMuxCapVoaSetpoint.setUnits(_F)
_OpticalMuxCapFiberBrand_Type=FspR7FiberBrandCaps
_OpticalMuxCapFiberBrand_Object=MibTableColumn
opticalMuxCapFiberBrand=_OpticalMuxCapFiberBrand_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,25),_OpticalMuxCapFiberBrand_Type())
opticalMuxCapFiberBrand.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapFiberBrand.setStatus(_A)
_OpticalMuxCapTiltSet_Type=FspR7TiltSetCaps
_OpticalMuxCapTiltSet_Object=MibTableColumn
opticalMuxCapTiltSet=_OpticalMuxCapTiltSet_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,26),_OpticalMuxCapTiltSet_Type())
opticalMuxCapTiltSet.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapTiltSet.setStatus(_A)
_OpticalMuxCapForceFwdAsePilotOn_Type=FspR7LaserForcedOperationCaps
_OpticalMuxCapForceFwdAsePilotOn_Object=MibTableColumn
opticalMuxCapForceFwdAsePilotOn=_OpticalMuxCapForceFwdAsePilotOn_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,27),_OpticalMuxCapForceFwdAsePilotOn_Type())
opticalMuxCapForceFwdAsePilotOn.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapForceFwdAsePilotOn.setStatus(_A)
_OpticalMuxCapBandProvision_Type=FspR7OpticalBandCaps
_OpticalMuxCapBandProvision_Object=MibTableColumn
opticalMuxCapBandProvision=_OpticalMuxCapBandProvision_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,28),_OpticalMuxCapBandProvision_Type())
opticalMuxCapBandProvision.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapBandProvision.setStatus(_A)
_OpticalMuxCapOffsetHigh_Type=FspR7Integer32Caps
_OpticalMuxCapOffsetHigh_Object=MibTableColumn
opticalMuxCapOffsetHigh=_OpticalMuxCapOffsetHigh_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,29),_OpticalMuxCapOffsetHigh_Type())
opticalMuxCapOffsetHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapOffsetHigh.setStatus(_A)
if mibBuilder.loadTexts:opticalMuxCapOffsetHigh.setUnits(_E)
_OpticalMuxCapOffsetLow_Type=FspR7Integer32Caps
_OpticalMuxCapOffsetLow_Object=MibTableColumn
opticalMuxCapOffsetLow=_OpticalMuxCapOffsetLow_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,30),_OpticalMuxCapOffsetLow_Type())
opticalMuxCapOffsetLow.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapOffsetLow.setStatus(_A)
if mibBuilder.loadTexts:opticalMuxCapOffsetLow.setUnits(_E)
_OpticalMuxCapOptUpdate_Type=FspR7OptUpdateCaps
_OpticalMuxCapOptUpdate_Object=MibTableColumn
opticalMuxCapOptUpdate=_OpticalMuxCapOptUpdate_Object((1,3,6,1,4,1,2544,1,11,9,3,6,1,1,31),_OpticalMuxCapOptUpdate_Type())
opticalMuxCapOptUpdate.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalMuxCapOptUpdate.setStatus(_A)
_EndOfOpticalMuxCapTable_Type=Integer32
_EndOfOpticalMuxCapTable_Object=MibScalar
endOfOpticalMuxCapTable=_EndOfOpticalMuxCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,6,2),_EndOfOpticalMuxCapTable_Type())
endOfOpticalMuxCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfOpticalMuxCapTable.setStatus(_A)
_EndOfOpticalMuxMgmtCap_Type=Integer32
_EndOfOpticalMuxMgmtCap_Object=MibScalar
endOfOpticalMuxMgmtCap=_EndOfOpticalMuxMgmtCap_Object((1,3,6,1,4,1,2544,1,11,9,3,6,10000),_EndOfOpticalMuxMgmtCap_Type())
endOfOpticalMuxMgmtCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfOpticalMuxMgmtCap.setStatus(_A)
_ShelfConnMgmtCap_ObjectIdentity=ObjectIdentity
shelfConnMgmtCap=_ShelfConnMgmtCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,3,7))
_ShelfConnCapTable_Object=MibTable
shelfConnCapTable=_ShelfConnCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,7,1))
if mibBuilder.loadTexts:shelfConnCapTable.setStatus(_A)
_ShelfConnCapEntry_Object=MibTableRow
shelfConnCapEntry=_ShelfConnCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,3,7,1,1))
shelfConnCapEntry.setIndexNames((0,_C,_Af),(0,_C,_Ag),(0,_C,_Ae),(0,_C,_Ad),(0,_C,_Ac))
if mibBuilder.loadTexts:shelfConnCapEntry.setStatus(_A)
_ShelfConnCapRowStatus_Type=FspR7RowStatusCaps
_ShelfConnCapRowStatus_Object=MibTableColumn
shelfConnCapRowStatus=_ShelfConnCapRowStatus_Object((1,3,6,1,4,1,2544,1,11,9,3,7,1,1,1),_ShelfConnCapRowStatus_Type())
shelfConnCapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfConnCapRowStatus.setStatus(_A)
_ShelfConnCapAdmin_Type=FspR7AdminStateCaps
_ShelfConnCapAdmin_Object=MibTableColumn
shelfConnCapAdmin=_ShelfConnCapAdmin_Object((1,3,6,1,4,1,2544,1,11,9,3,7,1,1,2),_ShelfConnCapAdmin_Type())
shelfConnCapAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfConnCapAdmin.setStatus(_A)
_ShelfConnCapAlias_Type=Integer32
_ShelfConnCapAlias_Object=MibTableColumn
shelfConnCapAlias=_ShelfConnCapAlias_Object((1,3,6,1,4,1,2544,1,11,9,3,7,1,1,3),_ShelfConnCapAlias_Type())
shelfConnCapAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfConnCapAlias.setStatus(_A)
_ShelfConnCapFacilityType_Type=FspR7InterfaceTypeCaps
_ShelfConnCapFacilityType_Object=MibTableColumn
shelfConnCapFacilityType=_ShelfConnCapFacilityType_Object((1,3,6,1,4,1,2544,1,11,9,3,7,1,1,4),_ShelfConnCapFacilityType_Type())
shelfConnCapFacilityType.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfConnCapFacilityType.setStatus(_A)
_EndOfShelfConnCapTable_Type=Integer32
_EndOfShelfConnCapTable_Object=MibScalar
endOfShelfConnCapTable=_EndOfShelfConnCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,7,2),_EndOfShelfConnCapTable_Type())
endOfShelfConnCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfShelfConnCapTable.setStatus(_A)
_EndOfShelfConnMgmtCap_Type=Integer32
_EndOfShelfConnMgmtCap_Object=MibScalar
endOfShelfConnMgmtCap=_EndOfShelfConnMgmtCap_Object((1,3,6,1,4,1,2544,1,11,9,3,7,10000),_EndOfShelfConnMgmtCap_Type())
endOfShelfConnMgmtCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfShelfConnMgmtCap.setStatus(_A)
_EnvMgmtCap_ObjectIdentity=ObjectIdentity
envMgmtCap=_EnvMgmtCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,3,8))
_EnvPortCapTable_Object=MibTable
envPortCapTable=_EnvPortCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,8,1))
if mibBuilder.loadTexts:envPortCapTable.setStatus(_A)
_EnvPortCapEntry_Object=MibTableRow
envPortCapEntry=_EnvPortCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,3,8,1,1))
envPortCapEntry.setIndexNames((0,_C,_X),(0,_C,_Y),(0,_C,_W),(0,_C,_V),(0,_C,_U))
if mibBuilder.loadTexts:envPortCapEntry.setStatus(_A)
_EnvPortCapRowStatus_Type=FspR7RowStatusCaps
_EnvPortCapRowStatus_Object=MibTableColumn
envPortCapRowStatus=_EnvPortCapRowStatus_Object((1,3,6,1,4,1,2544,1,11,9,3,8,1,1,1),_EnvPortCapRowStatus_Type())
envPortCapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:envPortCapRowStatus.setStatus(_A)
_EnvPortCapTelemetry_Type=FspR7TelemetryOutputCaps
_EnvPortCapTelemetry_Object=MibTableColumn
envPortCapTelemetry=_EnvPortCapTelemetry_Object((1,3,6,1,4,1,2544,1,11,9,3,8,1,1,2),_EnvPortCapTelemetry_Type())
envPortCapTelemetry.setMaxAccess(_B)
if mibBuilder.loadTexts:envPortCapTelemetry.setStatus(_A)
_EnvPortCapFacilityType_Type=FspR7InterfaceTypeCaps
_EnvPortCapFacilityType_Object=MibTableColumn
envPortCapFacilityType=_EnvPortCapFacilityType_Object((1,3,6,1,4,1,2544,1,11,9,3,8,1,1,3),_EnvPortCapFacilityType_Type())
envPortCapFacilityType.setMaxAccess(_B)
if mibBuilder.loadTexts:envPortCapFacilityType.setStatus(_A)
_EnvPortCapTifAlarmType_Type=Integer32
_EnvPortCapTifAlarmType_Object=MibTableColumn
envPortCapTifAlarmType=_EnvPortCapTifAlarmType_Object((1,3,6,1,4,1,2544,1,11,9,3,8,1,1,4),_EnvPortCapTifAlarmType_Type())
envPortCapTifAlarmType.setMaxAccess(_B)
if mibBuilder.loadTexts:envPortCapTifAlarmType.setStatus(_A)
_EnvPortCapTifAlarmMessage_Type=Integer32
_EnvPortCapTifAlarmMessage_Object=MibTableColumn
envPortCapTifAlarmMessage=_EnvPortCapTifAlarmMessage_Object((1,3,6,1,4,1,2544,1,11,9,3,8,1,1,5),_EnvPortCapTifAlarmMessage_Type())
envPortCapTifAlarmMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:envPortCapTifAlarmMessage.setStatus(_A)
_EnvPortCapInvertTifInputLogic_Type=FspR7InvertTelemetryInputLogicCaps
_EnvPortCapInvertTifInputLogic_Object=MibTableColumn
envPortCapInvertTifInputLogic=_EnvPortCapInvertTifInputLogic_Object((1,3,6,1,4,1,2544,1,11,9,3,8,1,1,6),_EnvPortCapInvertTifInputLogic_Type())
envPortCapInvertTifInputLogic.setMaxAccess(_B)
if mibBuilder.loadTexts:envPortCapInvertTifInputLogic.setStatus(_A)
_EndOfEnvPortCapTable_Type=Integer32
_EndOfEnvPortCapTable_Object=MibScalar
endOfEnvPortCapTable=_EndOfEnvPortCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,8,2),_EndOfEnvPortCapTable_Type())
endOfEnvPortCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfEnvPortCapTable.setStatus(_A)
_EndOfEnvMgmtCap_Type=Integer32
_EndOfEnvMgmtCap_Object=MibScalar
endOfEnvMgmtCap=_EndOfEnvMgmtCap_Object((1,3,6,1,4,1,2544,1,11,9,3,8,10000),_EndOfEnvMgmtCap_Type())
endOfEnvMgmtCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfEnvMgmtCap.setStatus(_A)
_ContainerMgmtCap_ObjectIdentity=ObjectIdentity
containerMgmtCap=_ContainerMgmtCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,3,9))
_ContainerCapTable_Object=MibTable
containerCapTable=_ContainerCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,9,1))
if mibBuilder.loadTexts:containerCapTable.setStatus(_A)
_ContainerCapEntry_Object=MibTableRow
containerCapEntry=_ContainerCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,3,9,1,1))
containerCapEntry.setIndexNames((0,_C,_o),(0,_C,_p),(0,_C,_n),(0,_C,_m),(0,_C,_l))
if mibBuilder.loadTexts:containerCapEntry.setStatus(_A)
_ContainerCapRowStatus_Type=FspR7RowStatusCaps
_ContainerCapRowStatus_Object=MibTableColumn
containerCapRowStatus=_ContainerCapRowStatus_Object((1,3,6,1,4,1,2544,1,11,9,3,9,1,1,1),_ContainerCapRowStatus_Type())
containerCapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:containerCapRowStatus.setStatus(_A)
_ContainerCapFacilityType_Type=FspR7InterfaceTypeCaps
_ContainerCapFacilityType_Object=MibTableColumn
containerCapFacilityType=_ContainerCapFacilityType_Object((1,3,6,1,4,1,2544,1,11,9,3,9,1,1,2),_ContainerCapFacilityType_Type())
containerCapFacilityType.setMaxAccess(_B)
if mibBuilder.loadTexts:containerCapFacilityType.setStatus(_A)
_EndOfContainerCapTable_Type=Integer32
_EndOfContainerCapTable_Object=MibScalar
endOfContainerCapTable=_EndOfContainerCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,9,2),_EndOfContainerCapTable_Type())
endOfContainerCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfContainerCapTable.setStatus(_A)
_EndOfContainerMgmtCap_Type=Integer32
_EndOfContainerMgmtCap_Object=MibScalar
endOfContainerMgmtCap=_EndOfContainerMgmtCap_Object((1,3,6,1,4,1,2544,1,11,9,3,9,10000),_EndOfContainerMgmtCap_Type())
endOfContainerMgmtCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfContainerMgmtCap.setStatus(_A)
_OpticalLineMgmtCap_ObjectIdentity=ObjectIdentity
opticalLineMgmtCap=_OpticalLineMgmtCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,3,10))
_OpticalLineCapTable_Object=MibTable
opticalLineCapTable=_OpticalLineCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,10,1))
if mibBuilder.loadTexts:opticalLineCapTable.setStatus(_A)
_OpticalLineCapEntry_Object=MibTableRow
opticalLineCapEntry=_OpticalLineCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,3,10,1,1))
opticalLineCapEntry.setIndexNames((0,_C,_Z),(0,_C,_Z),(0,_C,_Z),(0,_C,_Z),(0,_C,_AW))
if mibBuilder.loadTexts:opticalLineCapEntry.setStatus(_A)
_OpticalLineCapRowStatus_Type=FspR7RowStatusCaps
_OpticalLineCapRowStatus_Object=MibTableColumn
opticalLineCapRowStatus=_OpticalLineCapRowStatus_Object((1,3,6,1,4,1,2544,1,11,9,3,10,1,1,1),_OpticalLineCapRowStatus_Type())
opticalLineCapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalLineCapRowStatus.setStatus(_A)
_OpticalLineCapTxLineAttenuation_Type=FspR7Integer32Caps
_OpticalLineCapTxLineAttenuation_Object=MibTableColumn
opticalLineCapTxLineAttenuation=_OpticalLineCapTxLineAttenuation_Object((1,3,6,1,4,1,2544,1,11,9,3,10,1,1,2),_OpticalLineCapTxLineAttenuation_Type())
opticalLineCapTxLineAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalLineCapTxLineAttenuation.setStatus(_A)
if mibBuilder.loadTexts:opticalLineCapTxLineAttenuation.setUnits(_F)
_OpticalLineCapRxLineAttenuation_Type=FspR7Integer32Caps
_OpticalLineCapRxLineAttenuation_Object=MibTableColumn
opticalLineCapRxLineAttenuation=_OpticalLineCapRxLineAttenuation_Object((1,3,6,1,4,1,2544,1,11,9,3,10,1,1,3),_OpticalLineCapRxLineAttenuation_Type())
opticalLineCapRxLineAttenuation.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalLineCapRxLineAttenuation.setStatus(_A)
if mibBuilder.loadTexts:opticalLineCapRxLineAttenuation.setUnits(_F)
_OpticalLineCapAlias_Type=Integer32
_OpticalLineCapAlias_Object=MibTableColumn
opticalLineCapAlias=_OpticalLineCapAlias_Object((1,3,6,1,4,1,2544,1,11,9,3,10,1,1,4),_OpticalLineCapAlias_Type())
opticalLineCapAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalLineCapAlias.setStatus(_A)
_OpticalLineCapFarEndLocation_Type=Integer32
_OpticalLineCapFarEndLocation_Object=MibTableColumn
opticalLineCapFarEndLocation=_OpticalLineCapFarEndLocation_Object((1,3,6,1,4,1,2544,1,11,9,3,10,1,1,5),_OpticalLineCapFarEndLocation_Type())
opticalLineCapFarEndLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:opticalLineCapFarEndLocation.setStatus(_A)
_EndOfOpticalLineCapTable_Type=Integer32
_EndOfOpticalLineCapTable_Object=MibScalar
endOfOpticalLineCapTable=_EndOfOpticalLineCapTable_Object((1,3,6,1,4,1,2544,1,11,9,3,10,2),_EndOfOpticalLineCapTable_Type())
endOfOpticalLineCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfOpticalLineCapTable.setStatus(_A)
_EndOfOpticalLineMgmtCap_Type=Integer32
_EndOfOpticalLineMgmtCap_Object=MibScalar
endOfOpticalLineMgmtCap=_EndOfOpticalLineMgmtCap_Object((1,3,6,1,4,1,2544,1,11,9,3,10,10000),_EndOfOpticalLineMgmtCap_Type())
endOfOpticalLineMgmtCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfOpticalLineMgmtCap.setStatus(_A)
_EndOfManagementCap_Type=Integer32
_EndOfManagementCap_Object=MibScalar
endOfManagementCap=_EndOfManagementCap_Object((1,3,6,1,4,1,2544,1,11,9,3,10000),_EndOfManagementCap_Type())
endOfManagementCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfManagementCap.setStatus(_A)
_PerformanceCap_ObjectIdentity=ObjectIdentity
performanceCap=_PerformanceCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,6))
_PerformanceFacilityCap_ObjectIdentity=ObjectIdentity
performanceFacilityCap=_PerformanceFacilityCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,6,4))
_PerformanceFacilityThresholdCap_ObjectIdentity=ObjectIdentity
performanceFacilityThresholdCap=_PerformanceFacilityThresholdCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,6,4,1))
_OptThresholdConfigCapTable_Object=MibTable
optThresholdConfigCapTable=_OptThresholdConfigCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,4,1,1))
if mibBuilder.loadTexts:optThresholdConfigCapTable.setStatus(_A)
_OptThresholdConfigCapEntry_Object=MibTableRow
optThresholdConfigCapEntry=_OptThresholdConfigCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,6,4,1,1,1))
optThresholdConfigCapEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_K),(0,_C,_J),(0,_C,_I))
if mibBuilder.loadTexts:optThresholdConfigCapEntry.setStatus(_A)
_OptThresholdConfigCapLowConfig_Type=FspR7Integer32Caps
_OptThresholdConfigCapLowConfig_Object=MibTableColumn
optThresholdConfigCapLowConfig=_OptThresholdConfigCapLowConfig_Object((1,3,6,1,4,1,2544,1,11,9,6,4,1,1,1,1),_OptThresholdConfigCapLowConfig_Type())
optThresholdConfigCapLowConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:optThresholdConfigCapLowConfig.setStatus(_A)
if mibBuilder.loadTexts:optThresholdConfigCapLowConfig.setUnits(_E)
_OptThresholdConfigCapHighConfig_Type=FspR7Integer32Caps
_OptThresholdConfigCapHighConfig_Object=MibTableColumn
optThresholdConfigCapHighConfig=_OptThresholdConfigCapHighConfig_Object((1,3,6,1,4,1,2544,1,11,9,6,4,1,1,1,2),_OptThresholdConfigCapHighConfig_Type())
optThresholdConfigCapHighConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:optThresholdConfigCapHighConfig.setStatus(_A)
if mibBuilder.loadTexts:optThresholdConfigCapHighConfig.setUnits(_E)
_OprThresholdConfigCapTable_Object=MibTable
oprThresholdConfigCapTable=_OprThresholdConfigCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,4,1,2))
if mibBuilder.loadTexts:oprThresholdConfigCapTable.setStatus(_A)
_OprThresholdConfigCapEntry_Object=MibTableRow
oprThresholdConfigCapEntry=_OprThresholdConfigCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,6,4,1,2,1))
oprThresholdConfigCapEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_K),(0,_C,_J),(0,_C,_I))
if mibBuilder.loadTexts:oprThresholdConfigCapEntry.setStatus(_A)
_OprThresholdConfigCapLowConfig_Type=FspR7Integer32Caps
_OprThresholdConfigCapLowConfig_Object=MibTableColumn
oprThresholdConfigCapLowConfig=_OprThresholdConfigCapLowConfig_Object((1,3,6,1,4,1,2544,1,11,9,6,4,1,2,1,1),_OprThresholdConfigCapLowConfig_Type())
oprThresholdConfigCapLowConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:oprThresholdConfigCapLowConfig.setStatus(_A)
if mibBuilder.loadTexts:oprThresholdConfigCapLowConfig.setUnits(_E)
_OprThresholdConfigCapHighConfig_Type=FspR7Integer32Caps
_OprThresholdConfigCapHighConfig_Object=MibTableColumn
oprThresholdConfigCapHighConfig=_OprThresholdConfigCapHighConfig_Object((1,3,6,1,4,1,2544,1,11,9,6,4,1,2,1,2),_OprThresholdConfigCapHighConfig_Type())
oprThresholdConfigCapHighConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:oprThresholdConfigCapHighConfig.setStatus(_A)
if mibBuilder.loadTexts:oprThresholdConfigCapHighConfig.setUnits(_E)
_EndOfOprThresholdConfigCapTable_Type=Integer32
_EndOfOprThresholdConfigCapTable_Object=MibScalar
endOfOprThresholdConfigCapTable=_EndOfOprThresholdConfigCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,4,1,3),_EndOfOprThresholdConfigCapTable_Type())
endOfOprThresholdConfigCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfOprThresholdConfigCapTable.setStatus(_A)
_EndOfPerformanceFacilityThresholdCap_Type=Integer32
_EndOfPerformanceFacilityThresholdCap_Object=MibScalar
endOfPerformanceFacilityThresholdCap=_EndOfPerformanceFacilityThresholdCap_Object((1,3,6,1,4,1,2544,1,11,9,6,4,1,10000),_EndOfPerformanceFacilityThresholdCap_Type())
endOfPerformanceFacilityThresholdCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfPerformanceFacilityThresholdCap.setStatus(_A)
_EndOfPerformanceFacilityCap_Type=Integer32
_EndOfPerformanceFacilityCap_Object=MibScalar
endOfPerformanceFacilityCap=_EndOfPerformanceFacilityCap_Object((1,3,6,1,4,1,2544,1,11,9,6,4,10000),_EndOfPerformanceFacilityCap_Type())
endOfPerformanceFacilityCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfPerformanceFacilityCap.setStatus(_A)
_PmEqptCap_ObjectIdentity=ObjectIdentity
pmEqptCap=_PmEqptCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,6,10))
_PmDcnCap_ObjectIdentity=ObjectIdentity
pmDcnCap=_PmDcnCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,6,11))
_PmDcnDataCap_ObjectIdentity=ObjectIdentity
pmDcnDataCap=_PmDcnDataCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,6,11,1))
_PmDcnPhysicalCap_ObjectIdentity=ObjectIdentity
pmDcnPhysicalCap=_PmDcnPhysicalCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,6,11,2))
_PmDcnPhysThresholdCap_ObjectIdentity=ObjectIdentity
pmDcnPhysThresholdCap=_PmDcnPhysThresholdCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,6,11,2,2))
_DcnPhysThresholdCapTable_Object=MibTable
dcnPhysThresholdCapTable=_DcnPhysThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,11,2,2,1))
if mibBuilder.loadTexts:dcnPhysThresholdCapTable.setStatus(_A)
_DcnPhysThresholdCapEntry_Object=MibTableRow
dcnPhysThresholdCapEntry=_DcnPhysThresholdCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,6,11,2,2,1,1))
dcnPhysThresholdCapEntry.setIndexNames((0,_C,_S),(0,_C,_T),(0,_C,_R),(0,_C,_Q),(0,_C,_P))
if mibBuilder.loadTexts:dcnPhysThresholdCapEntry.setStatus(_A)
_DcnPhysThresholdCapOprLow_Type=FspR7Integer32Caps
_DcnPhysThresholdCapOprLow_Object=MibTableColumn
dcnPhysThresholdCapOprLow=_DcnPhysThresholdCapOprLow_Object((1,3,6,1,4,1,2544,1,11,9,6,11,2,2,1,1,1),_DcnPhysThresholdCapOprLow_Type())
dcnPhysThresholdCapOprLow.setMaxAccess(_B)
if mibBuilder.loadTexts:dcnPhysThresholdCapOprLow.setStatus(_A)
if mibBuilder.loadTexts:dcnPhysThresholdCapOprLow.setUnits(_E)
_DcnPhysThresholdCapOprHigh_Type=FspR7Integer32Caps
_DcnPhysThresholdCapOprHigh_Object=MibTableColumn
dcnPhysThresholdCapOprHigh=_DcnPhysThresholdCapOprHigh_Object((1,3,6,1,4,1,2544,1,11,9,6,11,2,2,1,1,2),_DcnPhysThresholdCapOprHigh_Type())
dcnPhysThresholdCapOprHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:dcnPhysThresholdCapOprHigh.setStatus(_A)
if mibBuilder.loadTexts:dcnPhysThresholdCapOprHigh.setUnits(_E)
_DcnPhysThresholdCapAttRcvLow_Type=FspR7Integer32Caps
_DcnPhysThresholdCapAttRcvLow_Object=MibTableColumn
dcnPhysThresholdCapAttRcvLow=_DcnPhysThresholdCapAttRcvLow_Object((1,3,6,1,4,1,2544,1,11,9,6,11,2,2,1,1,3),_DcnPhysThresholdCapAttRcvLow_Type())
dcnPhysThresholdCapAttRcvLow.setMaxAccess(_B)
if mibBuilder.loadTexts:dcnPhysThresholdCapAttRcvLow.setStatus(_A)
if mibBuilder.loadTexts:dcnPhysThresholdCapAttRcvLow.setUnits(_F)
_DcnPhysThresholdCapAttRcvHigh_Type=FspR7Integer32Caps
_DcnPhysThresholdCapAttRcvHigh_Object=MibTableColumn
dcnPhysThresholdCapAttRcvHigh=_DcnPhysThresholdCapAttRcvHigh_Object((1,3,6,1,4,1,2544,1,11,9,6,11,2,2,1,1,4),_DcnPhysThresholdCapAttRcvHigh_Type())
dcnPhysThresholdCapAttRcvHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:dcnPhysThresholdCapAttRcvHigh.setStatus(_A)
if mibBuilder.loadTexts:dcnPhysThresholdCapAttRcvHigh.setUnits(_F)
_EndOfDcnPhysThresholdCapTable_Type=Integer32
_EndOfDcnPhysThresholdCapTable_Object=MibScalar
endOfDcnPhysThresholdCapTable=_EndOfDcnPhysThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,11,2,2,2),_EndOfDcnPhysThresholdCapTable_Type())
endOfDcnPhysThresholdCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfDcnPhysThresholdCapTable.setStatus(_A)
_EndOfPmDcnPhysThresholdCap_Type=Integer32
_EndOfPmDcnPhysThresholdCap_Object=MibScalar
endOfPmDcnPhysThresholdCap=_EndOfPmDcnPhysThresholdCap_Object((1,3,6,1,4,1,2544,1,11,9,6,11,2,2,10000),_EndOfPmDcnPhysThresholdCap_Type())
endOfPmDcnPhysThresholdCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfPmDcnPhysThresholdCap.setStatus(_A)
_EndOfPmDcnPhysicalCap_Type=Integer32
_EndOfPmDcnPhysicalCap_Object=MibScalar
endOfPmDcnPhysicalCap=_EndOfPmDcnPhysicalCap_Object((1,3,6,1,4,1,2544,1,11,9,6,11,2,10000),_EndOfPmDcnPhysicalCap_Type())
endOfPmDcnPhysicalCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfPmDcnPhysicalCap.setStatus(_A)
_EndOfPmDcnCap_Type=Integer32
_EndOfPmDcnCap_Object=MibScalar
endOfPmDcnCap=_EndOfPmDcnCap_Object((1,3,6,1,4,1,2544,1,11,9,6,11,10000),_EndOfPmDcnCap_Type())
endOfPmDcnCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfPmDcnCap.setStatus(_A)
_PmFacilityCap_ObjectIdentity=ObjectIdentity
pmFacilityCap=_PmFacilityCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,6,12))
_PmFacilityDataCap_ObjectIdentity=ObjectIdentity
pmFacilityDataCap=_PmFacilityDataCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,6,12,1))
_PmFacilityDataThresholdCap_ObjectIdentity=ObjectIdentity
pmFacilityDataThresholdCap=_PmFacilityDataThresholdCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,6,12,1,1))
_OduFacilityDataThresholdCapTable_Object=MibTable
oduFacilityDataThresholdCapTable=_OduFacilityDataThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,1))
if mibBuilder.loadTexts:oduFacilityDataThresholdCapTable.setStatus(_A)
_OduFacilityDataThresholdCapEntry_Object=MibTableRow
oduFacilityDataThresholdCapEntry=_OduFacilityDataThresholdCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,1,1))
oduFacilityDataThresholdCapEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_K),(0,_C,_J),(0,_C,_I))
if mibBuilder.loadTexts:oduFacilityDataThresholdCapEntry.setStatus(_A)
_OduFacilityDataThresholdCapESHighThres15min_Type=FspR7Unsigned32Caps
_OduFacilityDataThresholdCapESHighThres15min_Object=MibTableColumn
oduFacilityDataThresholdCapESHighThres15min=_OduFacilityDataThresholdCapESHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,1,1,1),_OduFacilityDataThresholdCapESHighThres15min_Type())
oduFacilityDataThresholdCapESHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:oduFacilityDataThresholdCapESHighThres15min.setStatus(_A)
_OduFacilityDataThresholdCapESHighThres1day_Type=FspR7Unsigned32Caps
_OduFacilityDataThresholdCapESHighThres1day_Object=MibTableColumn
oduFacilityDataThresholdCapESHighThres1day=_OduFacilityDataThresholdCapESHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,1,1,2),_OduFacilityDataThresholdCapESHighThres1day_Type())
oduFacilityDataThresholdCapESHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:oduFacilityDataThresholdCapESHighThres1day.setStatus(_A)
_OduFacilityDataThresholdCapSESHighThres15min_Type=FspR7Unsigned32Caps
_OduFacilityDataThresholdCapSESHighThres15min_Object=MibTableColumn
oduFacilityDataThresholdCapSESHighThres15min=_OduFacilityDataThresholdCapSESHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,1,1,3),_OduFacilityDataThresholdCapSESHighThres15min_Type())
oduFacilityDataThresholdCapSESHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:oduFacilityDataThresholdCapSESHighThres15min.setStatus(_A)
_OduFacilityDataThresholdCapSESHighThres1day_Type=FspR7Unsigned32Caps
_OduFacilityDataThresholdCapSESHighThres1day_Object=MibTableColumn
oduFacilityDataThresholdCapSESHighThres1day=_OduFacilityDataThresholdCapSESHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,1,1,4),_OduFacilityDataThresholdCapSESHighThres1day_Type())
oduFacilityDataThresholdCapSESHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:oduFacilityDataThresholdCapSESHighThres1day.setStatus(_A)
_OduFacilityDataThresholdCapBbeHighThres15min_Type=Counter64StringCaps
_OduFacilityDataThresholdCapBbeHighThres15min_Object=MibTableColumn
oduFacilityDataThresholdCapBbeHighThres15min=_OduFacilityDataThresholdCapBbeHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,1,1,5),_OduFacilityDataThresholdCapBbeHighThres15min_Type())
oduFacilityDataThresholdCapBbeHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:oduFacilityDataThresholdCapBbeHighThres15min.setStatus(_A)
_OduFacilityDataThresholdCapBbeHighThres1day_Type=Counter64StringCaps
_OduFacilityDataThresholdCapBbeHighThres1day_Object=MibTableColumn
oduFacilityDataThresholdCapBbeHighThres1day=_OduFacilityDataThresholdCapBbeHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,1,1,6),_OduFacilityDataThresholdCapBbeHighThres1day_Type())
oduFacilityDataThresholdCapBbeHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:oduFacilityDataThresholdCapBbeHighThres1day.setStatus(_A)
_OduFacilityDataThresholdCapUASHighThres15min_Type=FspR7Unsigned32Caps
_OduFacilityDataThresholdCapUASHighThres15min_Object=MibTableColumn
oduFacilityDataThresholdCapUASHighThres15min=_OduFacilityDataThresholdCapUASHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,1,1,7),_OduFacilityDataThresholdCapUASHighThres15min_Type())
oduFacilityDataThresholdCapUASHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:oduFacilityDataThresholdCapUASHighThres15min.setStatus(_A)
_OduFacilityDataThresholdCapUASHighThres1day_Type=FspR7Unsigned32Caps
_OduFacilityDataThresholdCapUASHighThres1day_Object=MibTableColumn
oduFacilityDataThresholdCapUASHighThres1day=_OduFacilityDataThresholdCapUASHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,1,1,8),_OduFacilityDataThresholdCapUASHighThres1day_Type())
oduFacilityDataThresholdCapUASHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:oduFacilityDataThresholdCapUASHighThres1day.setStatus(_A)
_EndOfOduFacilityDataThresholdCapTable_Type=Integer32
_EndOfOduFacilityDataThresholdCapTable_Object=MibScalar
endOfOduFacilityDataThresholdCapTable=_EndOfOduFacilityDataThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,2),_EndOfOduFacilityDataThresholdCapTable_Type())
endOfOduFacilityDataThresholdCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfOduFacilityDataThresholdCapTable.setStatus(_A)
_TcmAFacilityDataThresholdCapTable_Object=MibTable
tcmAFacilityDataThresholdCapTable=_TcmAFacilityDataThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,3))
if mibBuilder.loadTexts:tcmAFacilityDataThresholdCapTable.setStatus(_A)
_TcmAFacilityDataThresholdCapEntry_Object=MibTableRow
tcmAFacilityDataThresholdCapEntry=_TcmAFacilityDataThresholdCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,3,1))
tcmAFacilityDataThresholdCapEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_K),(0,_C,_J),(0,_C,_I))
if mibBuilder.loadTexts:tcmAFacilityDataThresholdCapEntry.setStatus(_A)
_TcmAFacilityDataThresholdCapESHighThres15min_Type=FspR7Unsigned32Caps
_TcmAFacilityDataThresholdCapESHighThres15min_Object=MibTableColumn
tcmAFacilityDataThresholdCapESHighThres15min=_TcmAFacilityDataThresholdCapESHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,3,1,1),_TcmAFacilityDataThresholdCapESHighThres15min_Type())
tcmAFacilityDataThresholdCapESHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:tcmAFacilityDataThresholdCapESHighThres15min.setStatus(_A)
_TcmAFacilityDataThresholdCapESHighThres1day_Type=FspR7Unsigned32Caps
_TcmAFacilityDataThresholdCapESHighThres1day_Object=MibTableColumn
tcmAFacilityDataThresholdCapESHighThres1day=_TcmAFacilityDataThresholdCapESHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,3,1,2),_TcmAFacilityDataThresholdCapESHighThres1day_Type())
tcmAFacilityDataThresholdCapESHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:tcmAFacilityDataThresholdCapESHighThres1day.setStatus(_A)
_TcmAFacilityDataThresholdCapSESHighThres15min_Type=FspR7Unsigned32Caps
_TcmAFacilityDataThresholdCapSESHighThres15min_Object=MibTableColumn
tcmAFacilityDataThresholdCapSESHighThres15min=_TcmAFacilityDataThresholdCapSESHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,3,1,3),_TcmAFacilityDataThresholdCapSESHighThres15min_Type())
tcmAFacilityDataThresholdCapSESHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:tcmAFacilityDataThresholdCapSESHighThres15min.setStatus(_A)
_TcmAFacilityDataThresholdCapSESHighThres1day_Type=FspR7Unsigned32Caps
_TcmAFacilityDataThresholdCapSESHighThres1day_Object=MibTableColumn
tcmAFacilityDataThresholdCapSESHighThres1day=_TcmAFacilityDataThresholdCapSESHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,3,1,4),_TcmAFacilityDataThresholdCapSESHighThres1day_Type())
tcmAFacilityDataThresholdCapSESHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:tcmAFacilityDataThresholdCapSESHighThres1day.setStatus(_A)
_TcmAFacilityDataThresholdCapBbeHighThres15min_Type=Counter64StringCaps
_TcmAFacilityDataThresholdCapBbeHighThres15min_Object=MibTableColumn
tcmAFacilityDataThresholdCapBbeHighThres15min=_TcmAFacilityDataThresholdCapBbeHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,3,1,5),_TcmAFacilityDataThresholdCapBbeHighThres15min_Type())
tcmAFacilityDataThresholdCapBbeHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:tcmAFacilityDataThresholdCapBbeHighThres15min.setStatus(_A)
_TcmAFacilityDataThresholdCapBbeHighThres1day_Type=Counter64StringCaps
_TcmAFacilityDataThresholdCapBbeHighThres1day_Object=MibTableColumn
tcmAFacilityDataThresholdCapBbeHighThres1day=_TcmAFacilityDataThresholdCapBbeHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,3,1,6),_TcmAFacilityDataThresholdCapBbeHighThres1day_Type())
tcmAFacilityDataThresholdCapBbeHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:tcmAFacilityDataThresholdCapBbeHighThres1day.setStatus(_A)
_TcmAFacilityDataThresholdCapUASHighThres15min_Type=FspR7Unsigned32Caps
_TcmAFacilityDataThresholdCapUASHighThres15min_Object=MibTableColumn
tcmAFacilityDataThresholdCapUASHighThres15min=_TcmAFacilityDataThresholdCapUASHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,3,1,7),_TcmAFacilityDataThresholdCapUASHighThres15min_Type())
tcmAFacilityDataThresholdCapUASHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:tcmAFacilityDataThresholdCapUASHighThres15min.setStatus(_A)
_TcmAFacilityDataThresholdCapUASHighThres1day_Type=FspR7Unsigned32Caps
_TcmAFacilityDataThresholdCapUASHighThres1day_Object=MibTableColumn
tcmAFacilityDataThresholdCapUASHighThres1day=_TcmAFacilityDataThresholdCapUASHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,3,1,8),_TcmAFacilityDataThresholdCapUASHighThres1day_Type())
tcmAFacilityDataThresholdCapUASHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:tcmAFacilityDataThresholdCapUASHighThres1day.setStatus(_A)
_EndOfTcmAFacilityDataThresholdCapTable_Type=Integer32
_EndOfTcmAFacilityDataThresholdCapTable_Object=MibScalar
endOfTcmAFacilityDataThresholdCapTable=_EndOfTcmAFacilityDataThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,4),_EndOfTcmAFacilityDataThresholdCapTable_Type())
endOfTcmAFacilityDataThresholdCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfTcmAFacilityDataThresholdCapTable.setStatus(_A)
_TcmBFacilityDataThresholdCapTable_Object=MibTable
tcmBFacilityDataThresholdCapTable=_TcmBFacilityDataThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,5))
if mibBuilder.loadTexts:tcmBFacilityDataThresholdCapTable.setStatus(_A)
_TcmBFacilityDataThresholdCapEntry_Object=MibTableRow
tcmBFacilityDataThresholdCapEntry=_TcmBFacilityDataThresholdCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,5,1))
tcmBFacilityDataThresholdCapEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_K),(0,_C,_J),(0,_C,_I))
if mibBuilder.loadTexts:tcmBFacilityDataThresholdCapEntry.setStatus(_A)
_TcmBFacilityDataThresholdCapBESHighThres15min_Type=FspR7Unsigned32Caps
_TcmBFacilityDataThresholdCapBESHighThres15min_Object=MibTableColumn
tcmBFacilityDataThresholdCapBESHighThres15min=_TcmBFacilityDataThresholdCapBESHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,5,1,1),_TcmBFacilityDataThresholdCapBESHighThres15min_Type())
tcmBFacilityDataThresholdCapBESHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:tcmBFacilityDataThresholdCapBESHighThres15min.setStatus(_A)
_TcmBFacilityDataThresholdCapESHighThres1day_Type=FspR7Unsigned32Caps
_TcmBFacilityDataThresholdCapESHighThres1day_Object=MibTableColumn
tcmBFacilityDataThresholdCapESHighThres1day=_TcmBFacilityDataThresholdCapESHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,5,1,2),_TcmBFacilityDataThresholdCapESHighThres1day_Type())
tcmBFacilityDataThresholdCapESHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:tcmBFacilityDataThresholdCapESHighThres1day.setStatus(_A)
_TcmBFacilityDataThresholdCapSESHighThres15min_Type=FspR7Unsigned32Caps
_TcmBFacilityDataThresholdCapSESHighThres15min_Object=MibTableColumn
tcmBFacilityDataThresholdCapSESHighThres15min=_TcmBFacilityDataThresholdCapSESHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,5,1,3),_TcmBFacilityDataThresholdCapSESHighThres15min_Type())
tcmBFacilityDataThresholdCapSESHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:tcmBFacilityDataThresholdCapSESHighThres15min.setStatus(_A)
_TcmBFacilityDataThresholdCapSESHighThres1day_Type=FspR7Unsigned32Caps
_TcmBFacilityDataThresholdCapSESHighThres1day_Object=MibTableColumn
tcmBFacilityDataThresholdCapSESHighThres1day=_TcmBFacilityDataThresholdCapSESHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,5,1,4),_TcmBFacilityDataThresholdCapSESHighThres1day_Type())
tcmBFacilityDataThresholdCapSESHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:tcmBFacilityDataThresholdCapSESHighThres1day.setStatus(_A)
_TcmBFacilityDataThresholdCapOduTcmBBbeHighThres15min_Type=Counter64StringCaps
_TcmBFacilityDataThresholdCapOduTcmBBbeHighThres15min_Object=MibTableColumn
tcmBFacilityDataThresholdCapOduTcmBBbeHighThres15min=_TcmBFacilityDataThresholdCapOduTcmBBbeHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,5,1,5),_TcmBFacilityDataThresholdCapOduTcmBBbeHighThres15min_Type())
tcmBFacilityDataThresholdCapOduTcmBBbeHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:tcmBFacilityDataThresholdCapOduTcmBBbeHighThres15min.setStatus(_A)
_TcmBFacilityDataThresholdCapOduTcmBBbeHighThres1day_Type=Counter64StringCaps
_TcmBFacilityDataThresholdCapOduTcmBBbeHighThres1day_Object=MibTableColumn
tcmBFacilityDataThresholdCapOduTcmBBbeHighThres1day=_TcmBFacilityDataThresholdCapOduTcmBBbeHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,5,1,6),_TcmBFacilityDataThresholdCapOduTcmBBbeHighThres1day_Type())
tcmBFacilityDataThresholdCapOduTcmBBbeHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:tcmBFacilityDataThresholdCapOduTcmBBbeHighThres1day.setStatus(_A)
_TcmBFacilityDataThresholdCapUASHighThres15min_Type=FspR7Unsigned32Caps
_TcmBFacilityDataThresholdCapUASHighThres15min_Object=MibTableColumn
tcmBFacilityDataThresholdCapUASHighThres15min=_TcmBFacilityDataThresholdCapUASHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,5,1,7),_TcmBFacilityDataThresholdCapUASHighThres15min_Type())
tcmBFacilityDataThresholdCapUASHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:tcmBFacilityDataThresholdCapUASHighThres15min.setStatus(_A)
_TcmBFacilityDataThresholdCapUASHighThres1day_Type=FspR7Unsigned32Caps
_TcmBFacilityDataThresholdCapUASHighThres1day_Object=MibTableColumn
tcmBFacilityDataThresholdCapUASHighThres1day=_TcmBFacilityDataThresholdCapUASHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,5,1,8),_TcmBFacilityDataThresholdCapUASHighThres1day_Type())
tcmBFacilityDataThresholdCapUASHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:tcmBFacilityDataThresholdCapUASHighThres1day.setStatus(_A)
_EndOfTcmBFacilityDataThresholdCapTable_Type=Integer32
_EndOfTcmBFacilityDataThresholdCapTable_Object=MibScalar
endOfTcmBFacilityDataThresholdCapTable=_EndOfTcmBFacilityDataThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,6),_EndOfTcmBFacilityDataThresholdCapTable_Type())
endOfTcmBFacilityDataThresholdCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfTcmBFacilityDataThresholdCapTable.setStatus(_A)
_TcmCFacilityDataThresholdCapTable_Object=MibTable
tcmCFacilityDataThresholdCapTable=_TcmCFacilityDataThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,7))
if mibBuilder.loadTexts:tcmCFacilityDataThresholdCapTable.setStatus(_A)
_TcmCFacilityDataThresholdCapEntry_Object=MibTableRow
tcmCFacilityDataThresholdCapEntry=_TcmCFacilityDataThresholdCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,7,1))
tcmCFacilityDataThresholdCapEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_K),(0,_C,_J),(0,_C,_I))
if mibBuilder.loadTexts:tcmCFacilityDataThresholdCapEntry.setStatus(_A)
_TcmCFacilityDataThresholdCapBESHighThres15min_Type=FspR7Unsigned32Caps
_TcmCFacilityDataThresholdCapBESHighThres15min_Object=MibTableColumn
tcmCFacilityDataThresholdCapBESHighThres15min=_TcmCFacilityDataThresholdCapBESHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,7,1,1),_TcmCFacilityDataThresholdCapBESHighThres15min_Type())
tcmCFacilityDataThresholdCapBESHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:tcmCFacilityDataThresholdCapBESHighThres15min.setStatus(_A)
_TcmCFacilityDataThresholdCapESHighThres1day_Type=FspR7Unsigned32Caps
_TcmCFacilityDataThresholdCapESHighThres1day_Object=MibTableColumn
tcmCFacilityDataThresholdCapESHighThres1day=_TcmCFacilityDataThresholdCapESHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,7,1,2),_TcmCFacilityDataThresholdCapESHighThres1day_Type())
tcmCFacilityDataThresholdCapESHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:tcmCFacilityDataThresholdCapESHighThres1day.setStatus(_A)
_TcmCFacilityDataThresholdCapSESHighThres15min_Type=FspR7Unsigned32Caps
_TcmCFacilityDataThresholdCapSESHighThres15min_Object=MibTableColumn
tcmCFacilityDataThresholdCapSESHighThres15min=_TcmCFacilityDataThresholdCapSESHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,7,1,3),_TcmCFacilityDataThresholdCapSESHighThres15min_Type())
tcmCFacilityDataThresholdCapSESHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:tcmCFacilityDataThresholdCapSESHighThres15min.setStatus(_A)
_TcmCFacilityDataThresholdCapSESHighThres1day_Type=FspR7Unsigned32Caps
_TcmCFacilityDataThresholdCapSESHighThres1day_Object=MibTableColumn
tcmCFacilityDataThresholdCapSESHighThres1day=_TcmCFacilityDataThresholdCapSESHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,7,1,4),_TcmCFacilityDataThresholdCapSESHighThres1day_Type())
tcmCFacilityDataThresholdCapSESHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:tcmCFacilityDataThresholdCapSESHighThres1day.setStatus(_A)
_TcmCFacilityDataThresholdCapOduTcmCBbeHighThres15min_Type=Counter64StringCaps
_TcmCFacilityDataThresholdCapOduTcmCBbeHighThres15min_Object=MibTableColumn
tcmCFacilityDataThresholdCapOduTcmCBbeHighThres15min=_TcmCFacilityDataThresholdCapOduTcmCBbeHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,7,1,5),_TcmCFacilityDataThresholdCapOduTcmCBbeHighThres15min_Type())
tcmCFacilityDataThresholdCapOduTcmCBbeHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:tcmCFacilityDataThresholdCapOduTcmCBbeHighThres15min.setStatus(_A)
_TcmCFacilityDataThresholdCapOduTcmCBbeHighThres1day_Type=Counter64StringCaps
_TcmCFacilityDataThresholdCapOduTcmCBbeHighThres1day_Object=MibTableColumn
tcmCFacilityDataThresholdCapOduTcmCBbeHighThres1day=_TcmCFacilityDataThresholdCapOduTcmCBbeHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,7,1,6),_TcmCFacilityDataThresholdCapOduTcmCBbeHighThres1day_Type())
tcmCFacilityDataThresholdCapOduTcmCBbeHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:tcmCFacilityDataThresholdCapOduTcmCBbeHighThres1day.setStatus(_A)
_TcmCFacilityDataThresholdCapUASHighThres15min_Type=FspR7Unsigned32Caps
_TcmCFacilityDataThresholdCapUASHighThres15min_Object=MibTableColumn
tcmCFacilityDataThresholdCapUASHighThres15min=_TcmCFacilityDataThresholdCapUASHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,7,1,7),_TcmCFacilityDataThresholdCapUASHighThres15min_Type())
tcmCFacilityDataThresholdCapUASHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:tcmCFacilityDataThresholdCapUASHighThres15min.setStatus(_A)
_TcmCFacilityDataThresholdCapUASHighThres1day_Type=FspR7Unsigned32Caps
_TcmCFacilityDataThresholdCapUASHighThres1day_Object=MibTableColumn
tcmCFacilityDataThresholdCapUASHighThres1day=_TcmCFacilityDataThresholdCapUASHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,7,1,8),_TcmCFacilityDataThresholdCapUASHighThres1day_Type())
tcmCFacilityDataThresholdCapUASHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:tcmCFacilityDataThresholdCapUASHighThres1day.setStatus(_A)
_EndOfTcmCFacilityDataThresholdCapTable_Type=Integer32
_EndOfTcmCFacilityDataThresholdCapTable_Object=MibScalar
endOfTcmCFacilityDataThresholdCapTable=_EndOfTcmCFacilityDataThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,8),_EndOfTcmCFacilityDataThresholdCapTable_Type())
endOfTcmCFacilityDataThresholdCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfTcmCFacilityDataThresholdCapTable.setStatus(_A)
_OtuFacilityDataThresholdCapTable_Object=MibTable
otuFacilityDataThresholdCapTable=_OtuFacilityDataThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,9))
if mibBuilder.loadTexts:otuFacilityDataThresholdCapTable.setStatus(_A)
_OtuFacilityDataThresholdCapEntry_Object=MibTableRow
otuFacilityDataThresholdCapEntry=_OtuFacilityDataThresholdCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,9,1))
otuFacilityDataThresholdCapEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_K),(0,_C,_J),(0,_C,_I))
if mibBuilder.loadTexts:otuFacilityDataThresholdCapEntry.setStatus(_A)
_OtuFacilityDataThresholdCapESHighThres15min_Type=FspR7Unsigned32Caps
_OtuFacilityDataThresholdCapESHighThres15min_Object=MibTableColumn
otuFacilityDataThresholdCapESHighThres15min=_OtuFacilityDataThresholdCapESHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,9,1,1),_OtuFacilityDataThresholdCapESHighThres15min_Type())
otuFacilityDataThresholdCapESHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:otuFacilityDataThresholdCapESHighThres15min.setStatus(_A)
_OtuFacilityDataThresholdCapESHighThres1day_Type=FspR7Unsigned32Caps
_OtuFacilityDataThresholdCapESHighThres1day_Object=MibTableColumn
otuFacilityDataThresholdCapESHighThres1day=_OtuFacilityDataThresholdCapESHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,9,1,2),_OtuFacilityDataThresholdCapESHighThres1day_Type())
otuFacilityDataThresholdCapESHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:otuFacilityDataThresholdCapESHighThres1day.setStatus(_A)
_OtuFacilityDataThresholdCapSESHighThres15min_Type=FspR7Unsigned32Caps
_OtuFacilityDataThresholdCapSESHighThres15min_Object=MibTableColumn
otuFacilityDataThresholdCapSESHighThres15min=_OtuFacilityDataThresholdCapSESHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,9,1,3),_OtuFacilityDataThresholdCapSESHighThres15min_Type())
otuFacilityDataThresholdCapSESHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:otuFacilityDataThresholdCapSESHighThres15min.setStatus(_A)
_OtuFacilityDataThresholdCapSESHighThres1day_Type=FspR7Unsigned32Caps
_OtuFacilityDataThresholdCapSESHighThres1day_Object=MibTableColumn
otuFacilityDataThresholdCapSESHighThres1day=_OtuFacilityDataThresholdCapSESHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,9,1,4),_OtuFacilityDataThresholdCapSESHighThres1day_Type())
otuFacilityDataThresholdCapSESHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:otuFacilityDataThresholdCapSESHighThres1day.setStatus(_A)
_OtuFacilityDataThresholdCapBbeHighThres15min_Type=Counter64StringCaps
_OtuFacilityDataThresholdCapBbeHighThres15min_Object=MibTableColumn
otuFacilityDataThresholdCapBbeHighThres15min=_OtuFacilityDataThresholdCapBbeHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,9,1,5),_OtuFacilityDataThresholdCapBbeHighThres15min_Type())
otuFacilityDataThresholdCapBbeHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:otuFacilityDataThresholdCapBbeHighThres15min.setStatus(_A)
_OtuFacilityDataThresholdCapBbeHighThres1day_Type=Counter64StringCaps
_OtuFacilityDataThresholdCapBbeHighThres1day_Object=MibTableColumn
otuFacilityDataThresholdCapBbeHighThres1day=_OtuFacilityDataThresholdCapBbeHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,9,1,6),_OtuFacilityDataThresholdCapBbeHighThres1day_Type())
otuFacilityDataThresholdCapBbeHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:otuFacilityDataThresholdCapBbeHighThres1day.setStatus(_A)
_OtuFacilityDataThresholdCapUASHighThres15min_Type=FspR7Unsigned32Caps
_OtuFacilityDataThresholdCapUASHighThres15min_Object=MibTableColumn
otuFacilityDataThresholdCapUASHighThres15min=_OtuFacilityDataThresholdCapUASHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,9,1,7),_OtuFacilityDataThresholdCapUASHighThres15min_Type())
otuFacilityDataThresholdCapUASHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:otuFacilityDataThresholdCapUASHighThres15min.setStatus(_A)
_OtuFacilityDataThresholdCapUASHighThres1day_Type=FspR7Unsigned32Caps
_OtuFacilityDataThresholdCapUASHighThres1day_Object=MibTableColumn
otuFacilityDataThresholdCapUASHighThres1day=_OtuFacilityDataThresholdCapUASHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,9,1,8),_OtuFacilityDataThresholdCapUASHighThres1day_Type())
otuFacilityDataThresholdCapUASHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:otuFacilityDataThresholdCapUASHighThres1day.setStatus(_A)
_EndOfOtuFacilityDataThresholdCapTable_Type=Integer32
_EndOfOtuFacilityDataThresholdCapTable_Object=MibScalar
endOfOtuFacilityDataThresholdCapTable=_EndOfOtuFacilityDataThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,10),_EndOfOtuFacilityDataThresholdCapTable_Type())
endOfOtuFacilityDataThresholdCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfOtuFacilityDataThresholdCapTable.setStatus(_A)
_OtuFecFacilityDataThresholdCapTable_Object=MibTable
otuFecFacilityDataThresholdCapTable=_OtuFecFacilityDataThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,11))
if mibBuilder.loadTexts:otuFecFacilityDataThresholdCapTable.setStatus(_A)
_OtuFecFacilityDataThresholdCapEntry_Object=MibTableRow
otuFecFacilityDataThresholdCapEntry=_OtuFecFacilityDataThresholdCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,11,1))
otuFecFacilityDataThresholdCapEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_K),(0,_C,_J),(0,_C,_I))
if mibBuilder.loadTexts:otuFecFacilityDataThresholdCapEntry.setStatus(_A)
_OtuFecFacilityDataThresholdCapESHighThres15min_Type=FspR7Unsigned32Caps
_OtuFecFacilityDataThresholdCapESHighThres15min_Object=MibTableColumn
otuFecFacilityDataThresholdCapESHighThres15min=_OtuFecFacilityDataThresholdCapESHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,11,1,1),_OtuFecFacilityDataThresholdCapESHighThres15min_Type())
otuFecFacilityDataThresholdCapESHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:otuFecFacilityDataThresholdCapESHighThres15min.setStatus(_A)
_OtuFecFacilityDataThresholdCapESHighThres1day_Type=FspR7Unsigned32Caps
_OtuFecFacilityDataThresholdCapESHighThres1day_Object=MibTableColumn
otuFecFacilityDataThresholdCapESHighThres1day=_OtuFecFacilityDataThresholdCapESHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,11,1,2),_OtuFecFacilityDataThresholdCapESHighThres1day_Type())
otuFecFacilityDataThresholdCapESHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:otuFecFacilityDataThresholdCapESHighThres1day.setStatus(_A)
_OtuFecFacilityDataThresholdCapSESHighThres15min_Type=FspR7Unsigned32Caps
_OtuFecFacilityDataThresholdCapSESHighThres15min_Object=MibTableColumn
otuFecFacilityDataThresholdCapSESHighThres15min=_OtuFecFacilityDataThresholdCapSESHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,11,1,3),_OtuFecFacilityDataThresholdCapSESHighThres15min_Type())
otuFecFacilityDataThresholdCapSESHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:otuFecFacilityDataThresholdCapSESHighThres15min.setStatus(_A)
_OtuFecFacilityDataThresholdCapSESHighThres1day_Type=FspR7Unsigned32Caps
_OtuFecFacilityDataThresholdCapSESHighThres1day_Object=MibTableColumn
otuFecFacilityDataThresholdCapSESHighThres1day=_OtuFecFacilityDataThresholdCapSESHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,11,1,4),_OtuFecFacilityDataThresholdCapSESHighThres1day_Type())
otuFecFacilityDataThresholdCapSESHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:otuFecFacilityDataThresholdCapSESHighThres1day.setStatus(_A)
_OtuFecFacilityDataThresholdCapUBEHighThres15min_Type=Counter64StringCaps
_OtuFecFacilityDataThresholdCapUBEHighThres15min_Object=MibTableColumn
otuFecFacilityDataThresholdCapUBEHighThres15min=_OtuFecFacilityDataThresholdCapUBEHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,11,1,5),_OtuFecFacilityDataThresholdCapUBEHighThres15min_Type())
otuFecFacilityDataThresholdCapUBEHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:otuFecFacilityDataThresholdCapUBEHighThres15min.setStatus(_A)
_OtuFecFacilityDataThresholdCapUBEHighThres1day_Type=Counter64StringCaps
_OtuFecFacilityDataThresholdCapUBEHighThres1day_Object=MibTableColumn
otuFecFacilityDataThresholdCapUBEHighThres1day=_OtuFecFacilityDataThresholdCapUBEHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,11,1,6),_OtuFecFacilityDataThresholdCapUBEHighThres1day_Type())
otuFecFacilityDataThresholdCapUBEHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:otuFecFacilityDataThresholdCapUBEHighThres1day.setStatus(_A)
_OtuFecFacilityDataThresholdCapCErrHighThres15min_Type=Counter64StringCaps
_OtuFecFacilityDataThresholdCapCErrHighThres15min_Object=MibTableColumn
otuFecFacilityDataThresholdCapCErrHighThres15min=_OtuFecFacilityDataThresholdCapCErrHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,11,1,7),_OtuFecFacilityDataThresholdCapCErrHighThres15min_Type())
otuFecFacilityDataThresholdCapCErrHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:otuFecFacilityDataThresholdCapCErrHighThres15min.setStatus(_A)
_OtuFecFacilityDataThresholdCapCErrHighThres1day_Type=Counter64StringCaps
_OtuFecFacilityDataThresholdCapCErrHighThres1day_Object=MibTableColumn
otuFecFacilityDataThresholdCapCErrHighThres1day=_OtuFecFacilityDataThresholdCapCErrHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,11,1,8),_OtuFecFacilityDataThresholdCapCErrHighThres1day_Type())
otuFecFacilityDataThresholdCapCErrHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:otuFecFacilityDataThresholdCapCErrHighThres1day.setStatus(_A)
_OtuFecFacilityDataThresholdCapBERCErrHighThres15min_Type=Counter64StringCaps
_OtuFecFacilityDataThresholdCapBERCErrHighThres15min_Object=MibTableColumn
otuFecFacilityDataThresholdCapBERCErrHighThres15min=_OtuFecFacilityDataThresholdCapBERCErrHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,11,1,9),_OtuFecFacilityDataThresholdCapBERCErrHighThres15min_Type())
otuFecFacilityDataThresholdCapBERCErrHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:otuFecFacilityDataThresholdCapBERCErrHighThres15min.setStatus(_A)
_OtuFecFacilityDataThresholdCapBERCErrHighThres1day_Type=Counter64StringCaps
_OtuFecFacilityDataThresholdCapBERCErrHighThres1day_Object=MibTableColumn
otuFecFacilityDataThresholdCapBERCErrHighThres1day=_OtuFecFacilityDataThresholdCapBERCErrHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,11,1,10),_OtuFecFacilityDataThresholdCapBERCErrHighThres1day_Type())
otuFecFacilityDataThresholdCapBERCErrHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:otuFecFacilityDataThresholdCapBERCErrHighThres1day.setStatus(_A)
_EndOfOtuFecFacilityDataThresholdCapTable_Type=Integer32
_EndOfOtuFecFacilityDataThresholdCapTable_Object=MibScalar
endOfOtuFecFacilityDataThresholdCapTable=_EndOfOtuFecFacilityDataThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,12),_EndOfOtuFecFacilityDataThresholdCapTable_Type())
endOfOtuFecFacilityDataThresholdCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfOtuFecFacilityDataThresholdCapTable.setStatus(_A)
_FecFacilityDataThresholdCapTable_Object=MibTable
fecFacilityDataThresholdCapTable=_FecFacilityDataThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,13))
if mibBuilder.loadTexts:fecFacilityDataThresholdCapTable.setStatus(_A)
_FecFacilityDataThresholdCapEntry_Object=MibTableRow
fecFacilityDataThresholdCapEntry=_FecFacilityDataThresholdCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,13,1))
fecFacilityDataThresholdCapEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_K),(0,_C,_J),(0,_C,_I))
if mibBuilder.loadTexts:fecFacilityDataThresholdCapEntry.setStatus(_A)
_FecFacilityDataThresholdCapCEHighThres15min_Type=Counter64StringCaps
_FecFacilityDataThresholdCapCEHighThres15min_Object=MibTableColumn
fecFacilityDataThresholdCapCEHighThres15min=_FecFacilityDataThresholdCapCEHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,13,1,1),_FecFacilityDataThresholdCapCEHighThres15min_Type())
fecFacilityDataThresholdCapCEHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:fecFacilityDataThresholdCapCEHighThres15min.setStatus(_A)
_FecFacilityDataThresholdCapCEHighThres1day_Type=Counter64StringCaps
_FecFacilityDataThresholdCapCEHighThres1day_Object=MibTableColumn
fecFacilityDataThresholdCapCEHighThres1day=_FecFacilityDataThresholdCapCEHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,13,1,2),_FecFacilityDataThresholdCapCEHighThres1day_Type())
fecFacilityDataThresholdCapCEHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:fecFacilityDataThresholdCapCEHighThres1day.setStatus(_A)
_FecFacilityDataThresholdCapUBEHighThres15min_Type=Counter64StringCaps
_FecFacilityDataThresholdCapUBEHighThres15min_Object=MibTableColumn
fecFacilityDataThresholdCapUBEHighThres15min=_FecFacilityDataThresholdCapUBEHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,13,1,3),_FecFacilityDataThresholdCapUBEHighThres15min_Type())
fecFacilityDataThresholdCapUBEHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:fecFacilityDataThresholdCapUBEHighThres15min.setStatus(_A)
_FecFacilityDataThresholdCapUBEHighThres1day_Type=Counter64StringCaps
_FecFacilityDataThresholdCapUBEHighThres1day_Object=MibTableColumn
fecFacilityDataThresholdCapUBEHighThres1day=_FecFacilityDataThresholdCapUBEHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,13,1,4),_FecFacilityDataThresholdCapUBEHighThres1day_Type())
fecFacilityDataThresholdCapUBEHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:fecFacilityDataThresholdCapUBEHighThres1day.setStatus(_A)
_EndOfFecFacilityDataThresholdCapTable_Type=Integer32
_EndOfFecFacilityDataThresholdCapTable_Object=MibScalar
endOfFecFacilityDataThresholdCapTable=_EndOfFecFacilityDataThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,14),_EndOfFecFacilityDataThresholdCapTable_Type())
endOfFecFacilityDataThresholdCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfFecFacilityDataThresholdCapTable.setStatus(_A)
_Pcs2FacilityDataThresholdCapTable_Object=MibTable
pcs2FacilityDataThresholdCapTable=_Pcs2FacilityDataThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,15))
if mibBuilder.loadTexts:pcs2FacilityDataThresholdCapTable.setStatus(_A)
_Pcs2FacilityDataThresholdCapEntry_Object=MibTableRow
pcs2FacilityDataThresholdCapEntry=_Pcs2FacilityDataThresholdCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,15,1))
pcs2FacilityDataThresholdCapEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_K),(0,_C,_J),(0,_C,_I))
if mibBuilder.loadTexts:pcs2FacilityDataThresholdCapEntry.setStatus(_A)
_Pcs2FacilityDataThresholdCapESHighThres15min_Type=FspR7Unsigned32Caps
_Pcs2FacilityDataThresholdCapESHighThres15min_Object=MibTableColumn
pcs2FacilityDataThresholdCapESHighThres15min=_Pcs2FacilityDataThresholdCapESHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,15,1,1),_Pcs2FacilityDataThresholdCapESHighThres15min_Type())
pcs2FacilityDataThresholdCapESHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:pcs2FacilityDataThresholdCapESHighThres15min.setStatus(_A)
_Pcs2FacilityDataThresholdCapESHighThres1day_Type=FspR7Unsigned32Caps
_Pcs2FacilityDataThresholdCapESHighThres1day_Object=MibTableColumn
pcs2FacilityDataThresholdCapESHighThres1day=_Pcs2FacilityDataThresholdCapESHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,15,1,2),_Pcs2FacilityDataThresholdCapESHighThres1day_Type())
pcs2FacilityDataThresholdCapESHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:pcs2FacilityDataThresholdCapESHighThres1day.setStatus(_A)
_Pcs2FacilityDataThresholdCapDEHighThres15min_Type=FspR7Unsigned32Caps
_Pcs2FacilityDataThresholdCapDEHighThres15min_Object=MibTableColumn
pcs2FacilityDataThresholdCapDEHighThres15min=_Pcs2FacilityDataThresholdCapDEHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,15,1,3),_Pcs2FacilityDataThresholdCapDEHighThres15min_Type())
pcs2FacilityDataThresholdCapDEHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:pcs2FacilityDataThresholdCapDEHighThres15min.setStatus(_A)
_Pcs2FacilityDataThresholdCapDEHighThres1day_Type=FspR7Unsigned32Caps
_Pcs2FacilityDataThresholdCapDEHighThres1day_Object=MibTableColumn
pcs2FacilityDataThresholdCapDEHighThres1day=_Pcs2FacilityDataThresholdCapDEHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,15,1,4),_Pcs2FacilityDataThresholdCapDEHighThres1day_Type())
pcs2FacilityDataThresholdCapDEHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:pcs2FacilityDataThresholdCapDEHighThres1day.setStatus(_A)
_Pcs2FacilityDataThresholdCapCVHighThres15min_Type=Counter64StringCaps
_Pcs2FacilityDataThresholdCapCVHighThres15min_Object=MibTableColumn
pcs2FacilityDataThresholdCapCVHighThres15min=_Pcs2FacilityDataThresholdCapCVHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,15,1,5),_Pcs2FacilityDataThresholdCapCVHighThres15min_Type())
pcs2FacilityDataThresholdCapCVHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:pcs2FacilityDataThresholdCapCVHighThres15min.setStatus(_A)
_Pcs2FacilityDataThresholdCapCVHighThres1day_Type=Counter64StringCaps
_Pcs2FacilityDataThresholdCapCVHighThres1day_Object=MibTableColumn
pcs2FacilityDataThresholdCapCVHighThres1day=_Pcs2FacilityDataThresholdCapCVHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,15,1,6),_Pcs2FacilityDataThresholdCapCVHighThres1day_Type())
pcs2FacilityDataThresholdCapCVHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:pcs2FacilityDataThresholdCapCVHighThres1day.setStatus(_A)
_EndOfPcs2FacilityDataThresholdCapTable_Type=Integer32
_EndOfPcs2FacilityDataThresholdCapTable_Object=MibScalar
endOfPcs2FacilityDataThresholdCapTable=_EndOfPcs2FacilityDataThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,16),_EndOfPcs2FacilityDataThresholdCapTable_Type())
endOfPcs2FacilityDataThresholdCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfPcs2FacilityDataThresholdCapTable.setStatus(_A)
_LFacilityDataThresholdCapTable_Object=MibTable
lFacilityDataThresholdCapTable=_LFacilityDataThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,17))
if mibBuilder.loadTexts:lFacilityDataThresholdCapTable.setStatus(_A)
_LFacilityDataThresholdCapEntry_Object=MibTableRow
lFacilityDataThresholdCapEntry=_LFacilityDataThresholdCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,17,1))
lFacilityDataThresholdCapEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_K),(0,_C,_J),(0,_C,_I))
if mibBuilder.loadTexts:lFacilityDataThresholdCapEntry.setStatus(_A)
_LFacilityDataThresholdCapESHighThres15min_Type=FspR7Unsigned32Caps
_LFacilityDataThresholdCapESHighThres15min_Object=MibTableColumn
lFacilityDataThresholdCapESHighThres15min=_LFacilityDataThresholdCapESHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,17,1,1),_LFacilityDataThresholdCapESHighThres15min_Type())
lFacilityDataThresholdCapESHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:lFacilityDataThresholdCapESHighThres15min.setStatus(_A)
_LFacilityDataThresholdCapESHighThres1day_Type=FspR7Unsigned32Caps
_LFacilityDataThresholdCapESHighThres1day_Object=MibTableColumn
lFacilityDataThresholdCapESHighThres1day=_LFacilityDataThresholdCapESHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,17,1,2),_LFacilityDataThresholdCapESHighThres1day_Type())
lFacilityDataThresholdCapESHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:lFacilityDataThresholdCapESHighThres1day.setStatus(_A)
_LFacilityDataThresholdCapSESHighThres15min_Type=FspR7Unsigned32Caps
_LFacilityDataThresholdCapSESHighThres15min_Object=MibTableColumn
lFacilityDataThresholdCapSESHighThres15min=_LFacilityDataThresholdCapSESHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,17,1,3),_LFacilityDataThresholdCapSESHighThres15min_Type())
lFacilityDataThresholdCapSESHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:lFacilityDataThresholdCapSESHighThres15min.setStatus(_A)
_LFacilityDataThresholdCapSESHighThres1day_Type=FspR7Unsigned32Caps
_LFacilityDataThresholdCapSESHighThres1day_Object=MibTableColumn
lFacilityDataThresholdCapSESHighThres1day=_LFacilityDataThresholdCapSESHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,17,1,4),_LFacilityDataThresholdCapSESHighThres1day_Type())
lFacilityDataThresholdCapSESHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:lFacilityDataThresholdCapSESHighThres1day.setStatus(_A)
_LFacilityDataThresholdCapUASHighThres15min_Type=FspR7Unsigned32Caps
_LFacilityDataThresholdCapUASHighThres15min_Object=MibTableColumn
lFacilityDataThresholdCapUASHighThres15min=_LFacilityDataThresholdCapUASHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,17,1,5),_LFacilityDataThresholdCapUASHighThres15min_Type())
lFacilityDataThresholdCapUASHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:lFacilityDataThresholdCapUASHighThres15min.setStatus(_A)
_LFacilityDataThresholdCapUASSHighThres1day_Type=FspR7Unsigned32Caps
_LFacilityDataThresholdCapUASSHighThres1day_Object=MibTableColumn
lFacilityDataThresholdCapUASSHighThres1day=_LFacilityDataThresholdCapUASSHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,17,1,6),_LFacilityDataThresholdCapUASSHighThres1day_Type())
lFacilityDataThresholdCapUASSHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:lFacilityDataThresholdCapUASSHighThres1day.setStatus(_A)
_LFacilityDataThresholdCapCVHighThres15min_Type=Counter64StringCaps
_LFacilityDataThresholdCapCVHighThres15min_Object=MibTableColumn
lFacilityDataThresholdCapCVHighThres15min=_LFacilityDataThresholdCapCVHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,17,1,7),_LFacilityDataThresholdCapCVHighThres15min_Type())
lFacilityDataThresholdCapCVHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:lFacilityDataThresholdCapCVHighThres15min.setStatus(_A)
_LFacilityDataThresholdCapCVSHighThres1day_Type=Counter64StringCaps
_LFacilityDataThresholdCapCVSHighThres1day_Object=MibTableColumn
lFacilityDataThresholdCapCVSHighThres1day=_LFacilityDataThresholdCapCVSHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,17,1,8),_LFacilityDataThresholdCapCVSHighThres1day_Type())
lFacilityDataThresholdCapCVSHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:lFacilityDataThresholdCapCVSHighThres1day.setStatus(_A)
_EndOfLFacilityDataThresholdCapTable_Type=Integer32
_EndOfLFacilityDataThresholdCapTable_Object=MibScalar
endOfLFacilityDataThresholdCapTable=_EndOfLFacilityDataThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,18),_EndOfLFacilityDataThresholdCapTable_Type())
endOfLFacilityDataThresholdCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfLFacilityDataThresholdCapTable.setStatus(_A)
_SFacilityDataThresholdCapTable_Object=MibTable
sFacilityDataThresholdCapTable=_SFacilityDataThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,19))
if mibBuilder.loadTexts:sFacilityDataThresholdCapTable.setStatus(_A)
_SFacilityDataThresholdCapEntry_Object=MibTableRow
sFacilityDataThresholdCapEntry=_SFacilityDataThresholdCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,19,1))
sFacilityDataThresholdCapEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_K),(0,_C,_J),(0,_C,_I))
if mibBuilder.loadTexts:sFacilityDataThresholdCapEntry.setStatus(_A)
_SFacilityDataThresholdCapESHighThres15min_Type=FspR7Unsigned32Caps
_SFacilityDataThresholdCapESHighThres15min_Object=MibTableColumn
sFacilityDataThresholdCapESHighThres15min=_SFacilityDataThresholdCapESHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,19,1,1),_SFacilityDataThresholdCapESHighThres15min_Type())
sFacilityDataThresholdCapESHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:sFacilityDataThresholdCapESHighThres15min.setStatus(_A)
_SFacilityDataThresholdCapESHighThres1day_Type=FspR7Unsigned32Caps
_SFacilityDataThresholdCapESHighThres1day_Object=MibTableColumn
sFacilityDataThresholdCapESHighThres1day=_SFacilityDataThresholdCapESHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,19,1,2),_SFacilityDataThresholdCapESHighThres1day_Type())
sFacilityDataThresholdCapESHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:sFacilityDataThresholdCapESHighThres1day.setStatus(_A)
_SFacilityDataThresholdCapSESHighThres15min_Type=FspR7Unsigned32Caps
_SFacilityDataThresholdCapSESHighThres15min_Object=MibTableColumn
sFacilityDataThresholdCapSESHighThres15min=_SFacilityDataThresholdCapSESHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,19,1,3),_SFacilityDataThresholdCapSESHighThres15min_Type())
sFacilityDataThresholdCapSESHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:sFacilityDataThresholdCapSESHighThres15min.setStatus(_A)
_SFacilityDataThresholdCapSESHighThres1day_Type=FspR7Unsigned32Caps
_SFacilityDataThresholdCapSESHighThres1day_Object=MibTableColumn
sFacilityDataThresholdCapSESHighThres1day=_SFacilityDataThresholdCapSESHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,19,1,4),_SFacilityDataThresholdCapSESHighThres1day_Type())
sFacilityDataThresholdCapSESHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:sFacilityDataThresholdCapSESHighThres1day.setStatus(_A)
_SFacilityDataThresholdCapSEFSHighThres15min_Type=FspR7Unsigned32Caps
_SFacilityDataThresholdCapSEFSHighThres15min_Object=MibTableColumn
sFacilityDataThresholdCapSEFSHighThres15min=_SFacilityDataThresholdCapSEFSHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,19,1,5),_SFacilityDataThresholdCapSEFSHighThres15min_Type())
sFacilityDataThresholdCapSEFSHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:sFacilityDataThresholdCapSEFSHighThres15min.setStatus(_A)
_SFacilityDataThresholdCapSEFSHighThres1day_Type=FspR7Unsigned32Caps
_SFacilityDataThresholdCapSEFSHighThres1day_Object=MibTableColumn
sFacilityDataThresholdCapSEFSHighThres1day=_SFacilityDataThresholdCapSEFSHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,19,1,6),_SFacilityDataThresholdCapSEFSHighThres1day_Type())
sFacilityDataThresholdCapSEFSHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:sFacilityDataThresholdCapSEFSHighThres1day.setStatus(_A)
_SFacilityDataThresholdCapCVHighThres15min_Type=Counter64StringCaps
_SFacilityDataThresholdCapCVHighThres15min_Object=MibTableColumn
sFacilityDataThresholdCapCVHighThres15min=_SFacilityDataThresholdCapCVHighThres15min_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,19,1,7),_SFacilityDataThresholdCapCVHighThres15min_Type())
sFacilityDataThresholdCapCVHighThres15min.setMaxAccess(_B)
if mibBuilder.loadTexts:sFacilityDataThresholdCapCVHighThres15min.setStatus(_A)
_SFacilityDataThresholdCapCVHighThres1day_Type=Counter64StringCaps
_SFacilityDataThresholdCapCVHighThres1day_Object=MibTableColumn
sFacilityDataThresholdCapCVHighThres1day=_SFacilityDataThresholdCapCVHighThres1day_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,19,1,8),_SFacilityDataThresholdCapCVHighThres1day_Type())
sFacilityDataThresholdCapCVHighThres1day.setMaxAccess(_B)
if mibBuilder.loadTexts:sFacilityDataThresholdCapCVHighThres1day.setStatus(_A)
_EndOfSFacilityDataThresholdCapTable_Type=Integer32
_EndOfSFacilityDataThresholdCapTable_Object=MibScalar
endOfSFacilityDataThresholdCapTable=_EndOfSFacilityDataThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,20),_EndOfSFacilityDataThresholdCapTable_Type())
endOfSFacilityDataThresholdCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfSFacilityDataThresholdCapTable.setStatus(_A)
_EndOfPmFacilityDataThresholdCap_Type=Integer32
_EndOfPmFacilityDataThresholdCap_Object=MibScalar
endOfPmFacilityDataThresholdCap=_EndOfPmFacilityDataThresholdCap_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,1,10000),_EndOfPmFacilityDataThresholdCap_Type())
endOfPmFacilityDataThresholdCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfPmFacilityDataThresholdCap.setStatus(_A)
_EndOfPmFacilityDataCap_Type=Integer32
_EndOfPmFacilityDataCap_Object=MibScalar
endOfPmFacilityDataCap=_EndOfPmFacilityDataCap_Object((1,3,6,1,4,1,2544,1,11,9,6,12,1,10000),_EndOfPmFacilityDataCap_Type())
endOfPmFacilityDataCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfPmFacilityDataCap.setStatus(_A)
_PmFacilityPhysicalCap_ObjectIdentity=ObjectIdentity
pmFacilityPhysicalCap=_PmFacilityPhysicalCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,6,12,2))
_PmFacilityPhysValueCap_ObjectIdentity=ObjectIdentity
pmFacilityPhysValueCap=_PmFacilityPhysValueCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,6,12,2,1))
_PmFacilityPhysThresholdCap_ObjectIdentity=ObjectIdentity
pmFacilityPhysThresholdCap=_PmFacilityPhysThresholdCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,6,12,2,2))
_FacilityPhysThresholdCapTable_Object=MibTable
facilityPhysThresholdCapTable=_FacilityPhysThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,12,2,2,1))
if mibBuilder.loadTexts:facilityPhysThresholdCapTable.setStatus(_A)
_FacilityPhysThresholdCapEntry_Object=MibTableRow
facilityPhysThresholdCapEntry=_FacilityPhysThresholdCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,6,12,2,2,1,1))
facilityPhysThresholdCapEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_K),(0,_C,_J),(0,_C,_I))
if mibBuilder.loadTexts:facilityPhysThresholdCapEntry.setStatus(_A)
_FacilityPhysThresholdCapOpticalInputPwrLow_Type=FspR7Integer32Caps
_FacilityPhysThresholdCapOpticalInputPwrLow_Object=MibTableColumn
facilityPhysThresholdCapOpticalInputPwrLow=_FacilityPhysThresholdCapOpticalInputPwrLow_Object((1,3,6,1,4,1,2544,1,11,9,6,12,2,2,1,1,1),_FacilityPhysThresholdCapOpticalInputPwrLow_Type())
facilityPhysThresholdCapOpticalInputPwrLow.setMaxAccess(_B)
if mibBuilder.loadTexts:facilityPhysThresholdCapOpticalInputPwrLow.setStatus(_A)
if mibBuilder.loadTexts:facilityPhysThresholdCapOpticalInputPwrLow.setUnits(_E)
_FacilityPhysThresholdCapOpticalInputPwrHigh_Type=FspR7Integer32Caps
_FacilityPhysThresholdCapOpticalInputPwrHigh_Object=MibTableColumn
facilityPhysThresholdCapOpticalInputPwrHigh=_FacilityPhysThresholdCapOpticalInputPwrHigh_Object((1,3,6,1,4,1,2544,1,11,9,6,12,2,2,1,1,2),_FacilityPhysThresholdCapOpticalInputPwrHigh_Type())
facilityPhysThresholdCapOpticalInputPwrHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:facilityPhysThresholdCapOpticalInputPwrHigh.setStatus(_A)
if mibBuilder.loadTexts:facilityPhysThresholdCapOpticalInputPwrHigh.setUnits(_E)
_FacilityPhysThresholdCapConfigurableOpticalOutputPwrLow_Type=FspR7Integer32Caps
_FacilityPhysThresholdCapConfigurableOpticalOutputPwrLow_Object=MibTableColumn
facilityPhysThresholdCapConfigurableOpticalOutputPwrLow=_FacilityPhysThresholdCapConfigurableOpticalOutputPwrLow_Object((1,3,6,1,4,1,2544,1,11,9,6,12,2,2,1,1,3),_FacilityPhysThresholdCapConfigurableOpticalOutputPwrLow_Type())
facilityPhysThresholdCapConfigurableOpticalOutputPwrLow.setMaxAccess(_B)
if mibBuilder.loadTexts:facilityPhysThresholdCapConfigurableOpticalOutputPwrLow.setStatus(_A)
if mibBuilder.loadTexts:facilityPhysThresholdCapConfigurableOpticalOutputPwrLow.setUnits(_E)
_FacilityPhysThresholdCapConfigurableOpticalOutputPwrHigh_Type=FspR7Integer32Caps
_FacilityPhysThresholdCapConfigurableOpticalOutputPwrHigh_Object=MibTableColumn
facilityPhysThresholdCapConfigurableOpticalOutputPwrHigh=_FacilityPhysThresholdCapConfigurableOpticalOutputPwrHigh_Object((1,3,6,1,4,1,2544,1,11,9,6,12,2,2,1,1,4),_FacilityPhysThresholdCapConfigurableOpticalOutputPwrHigh_Type())
facilityPhysThresholdCapConfigurableOpticalOutputPwrHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:facilityPhysThresholdCapConfigurableOpticalOutputPwrHigh.setStatus(_A)
if mibBuilder.loadTexts:facilityPhysThresholdCapConfigurableOpticalOutputPwrHigh.setUnits(_E)
_FacilityPhysThresholdCapRoundTripDelayLowThres_Type=FspR7Integer32Caps
_FacilityPhysThresholdCapRoundTripDelayLowThres_Object=MibTableColumn
facilityPhysThresholdCapRoundTripDelayLowThres=_FacilityPhysThresholdCapRoundTripDelayLowThres_Object((1,3,6,1,4,1,2544,1,11,9,6,12,2,2,1,1,5),_FacilityPhysThresholdCapRoundTripDelayLowThres_Type())
facilityPhysThresholdCapRoundTripDelayLowThres.setMaxAccess(_B)
if mibBuilder.loadTexts:facilityPhysThresholdCapRoundTripDelayLowThres.setStatus(_A)
if mibBuilder.loadTexts:facilityPhysThresholdCapRoundTripDelayLowThres.setUnits('ns')
_FacilityPhysThresholdCapRoundTripDelayHighThres_Type=FspR7Integer32Caps
_FacilityPhysThresholdCapRoundTripDelayHighThres_Object=MibTableColumn
facilityPhysThresholdCapRoundTripDelayHighThres=_FacilityPhysThresholdCapRoundTripDelayHighThres_Object((1,3,6,1,4,1,2544,1,11,9,6,12,2,2,1,1,6),_FacilityPhysThresholdCapRoundTripDelayHighThres_Type())
facilityPhysThresholdCapRoundTripDelayHighThres.setMaxAccess(_B)
if mibBuilder.loadTexts:facilityPhysThresholdCapRoundTripDelayHighThres.setStatus(_A)
if mibBuilder.loadTexts:facilityPhysThresholdCapRoundTripDelayHighThres.setUnits('ns')
_FacilityPhysThresholdCapLatencyLowThres_Type=FspR7Integer32Caps
_FacilityPhysThresholdCapLatencyLowThres_Object=MibTableColumn
facilityPhysThresholdCapLatencyLowThres=_FacilityPhysThresholdCapLatencyLowThres_Object((1,3,6,1,4,1,2544,1,11,9,6,12,2,2,1,1,7),_FacilityPhysThresholdCapLatencyLowThres_Type())
facilityPhysThresholdCapLatencyLowThres.setMaxAccess(_B)
if mibBuilder.loadTexts:facilityPhysThresholdCapLatencyLowThres.setStatus(_A)
if mibBuilder.loadTexts:facilityPhysThresholdCapLatencyLowThres.setUnits('0.1 us')
_FacilityPhysThresholdCapLatencyHighThres_Type=FspR7Integer32Caps
_FacilityPhysThresholdCapLatencyHighThres_Object=MibTableColumn
facilityPhysThresholdCapLatencyHighThres=_FacilityPhysThresholdCapLatencyHighThres_Object((1,3,6,1,4,1,2544,1,11,9,6,12,2,2,1,1,8),_FacilityPhysThresholdCapLatencyHighThres_Type())
facilityPhysThresholdCapLatencyHighThres.setMaxAccess(_B)
if mibBuilder.loadTexts:facilityPhysThresholdCapLatencyHighThres.setStatus(_A)
if mibBuilder.loadTexts:facilityPhysThresholdCapLatencyHighThres.setUnits('0.1 us')
_FacilityPhysThresholdCapChromaticDispersionHigh_Type=FspR7Integer32Caps
_FacilityPhysThresholdCapChromaticDispersionHigh_Object=MibTableColumn
facilityPhysThresholdCapChromaticDispersionHigh=_FacilityPhysThresholdCapChromaticDispersionHigh_Object((1,3,6,1,4,1,2544,1,11,9,6,12,2,2,1,1,9),_FacilityPhysThresholdCapChromaticDispersionHigh_Type())
facilityPhysThresholdCapChromaticDispersionHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:facilityPhysThresholdCapChromaticDispersionHigh.setStatus(_A)
if mibBuilder.loadTexts:facilityPhysThresholdCapChromaticDispersionHigh.setUnits(_N)
_FacilityPhysThresholdCapChromaticDispersionLow_Type=FspR7Integer32Caps
_FacilityPhysThresholdCapChromaticDispersionLow_Object=MibTableColumn
facilityPhysThresholdCapChromaticDispersionLow=_FacilityPhysThresholdCapChromaticDispersionLow_Object((1,3,6,1,4,1,2544,1,11,9,6,12,2,2,1,1,10),_FacilityPhysThresholdCapChromaticDispersionLow_Type())
facilityPhysThresholdCapChromaticDispersionLow.setMaxAccess(_B)
if mibBuilder.loadTexts:facilityPhysThresholdCapChromaticDispersionLow.setStatus(_A)
if mibBuilder.loadTexts:facilityPhysThresholdCapChromaticDispersionLow.setUnits(_N)
_FacilityPhysThresholdCapCarrierFreqOffsetLow_Type=FspR7Integer32Caps
_FacilityPhysThresholdCapCarrierFreqOffsetLow_Object=MibTableColumn
facilityPhysThresholdCapCarrierFreqOffsetLow=_FacilityPhysThresholdCapCarrierFreqOffsetLow_Object((1,3,6,1,4,1,2544,1,11,9,6,12,2,2,1,1,11),_FacilityPhysThresholdCapCarrierFreqOffsetLow_Type())
facilityPhysThresholdCapCarrierFreqOffsetLow.setMaxAccess(_B)
if mibBuilder.loadTexts:facilityPhysThresholdCapCarrierFreqOffsetLow.setStatus(_A)
if mibBuilder.loadTexts:facilityPhysThresholdCapCarrierFreqOffsetLow.setUnits(_Ai)
_FacilityPhysThresholdCapCarrierFreqOffsetHigh_Type=FspR7Integer32Caps
_FacilityPhysThresholdCapCarrierFreqOffsetHigh_Object=MibTableColumn
facilityPhysThresholdCapCarrierFreqOffsetHigh=_FacilityPhysThresholdCapCarrierFreqOffsetHigh_Object((1,3,6,1,4,1,2544,1,11,9,6,12,2,2,1,1,12),_FacilityPhysThresholdCapCarrierFreqOffsetHigh_Type())
facilityPhysThresholdCapCarrierFreqOffsetHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:facilityPhysThresholdCapCarrierFreqOffsetHigh.setStatus(_A)
if mibBuilder.loadTexts:facilityPhysThresholdCapCarrierFreqOffsetHigh.setUnits(_Ai)
_FacilityPhysThresholdCapLogicalLanesSkewHigh_Type=FspR7Integer32Caps
_FacilityPhysThresholdCapLogicalLanesSkewHigh_Object=MibTableColumn
facilityPhysThresholdCapLogicalLanesSkewHigh=_FacilityPhysThresholdCapLogicalLanesSkewHigh_Object((1,3,6,1,4,1,2544,1,11,9,6,12,2,2,1,1,13),_FacilityPhysThresholdCapLogicalLanesSkewHigh_Type())
facilityPhysThresholdCapLogicalLanesSkewHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:facilityPhysThresholdCapLogicalLanesSkewHigh.setStatus(_A)
if mibBuilder.loadTexts:facilityPhysThresholdCapLogicalLanesSkewHigh.setUnits('ns')
_FacilityPhysThresholdCapDispersionCompensationLowThres_Type=FspR7Integer32Caps
_FacilityPhysThresholdCapDispersionCompensationLowThres_Object=MibTableColumn
facilityPhysThresholdCapDispersionCompensationLowThres=_FacilityPhysThresholdCapDispersionCompensationLowThres_Object((1,3,6,1,4,1,2544,1,11,9,6,12,2,2,1,1,14),_FacilityPhysThresholdCapDispersionCompensationLowThres_Type())
facilityPhysThresholdCapDispersionCompensationLowThres.setMaxAccess(_B)
if mibBuilder.loadTexts:facilityPhysThresholdCapDispersionCompensationLowThres.setStatus(_A)
if mibBuilder.loadTexts:facilityPhysThresholdCapDispersionCompensationLowThres.setUnits(_N)
_FacilityPhysThresholdCapDispersionCompensationHighThres_Type=FspR7Integer32Caps
_FacilityPhysThresholdCapDispersionCompensationHighThres_Object=MibTableColumn
facilityPhysThresholdCapDispersionCompensationHighThres=_FacilityPhysThresholdCapDispersionCompensationHighThres_Object((1,3,6,1,4,1,2544,1,11,9,6,12,2,2,1,1,15),_FacilityPhysThresholdCapDispersionCompensationHighThres_Type())
facilityPhysThresholdCapDispersionCompensationHighThres.setMaxAccess(_B)
if mibBuilder.loadTexts:facilityPhysThresholdCapDispersionCompensationHighThres.setStatus(_A)
if mibBuilder.loadTexts:facilityPhysThresholdCapDispersionCompensationHighThres.setUnits(_N)
_FacilityPhysThresholdCapSignalToNoiseRatioLow_Type=FspR7Integer32Caps
_FacilityPhysThresholdCapSignalToNoiseRatioLow_Object=MibTableColumn
facilityPhysThresholdCapSignalToNoiseRatioLow=_FacilityPhysThresholdCapSignalToNoiseRatioLow_Object((1,3,6,1,4,1,2544,1,11,9,6,12,2,2,1,1,16),_FacilityPhysThresholdCapSignalToNoiseRatioLow_Type())
facilityPhysThresholdCapSignalToNoiseRatioLow.setMaxAccess(_B)
if mibBuilder.loadTexts:facilityPhysThresholdCapSignalToNoiseRatioLow.setStatus(_A)
if mibBuilder.loadTexts:facilityPhysThresholdCapSignalToNoiseRatioLow.setUnits(_F)
_FacilityPhysThresholdCapDifferentialGroupDelayHigh_Type=FspR7Integer32Caps
_FacilityPhysThresholdCapDifferentialGroupDelayHigh_Object=MibTableColumn
facilityPhysThresholdCapDifferentialGroupDelayHigh=_FacilityPhysThresholdCapDifferentialGroupDelayHigh_Object((1,3,6,1,4,1,2544,1,11,9,6,12,2,2,1,1,17),_FacilityPhysThresholdCapDifferentialGroupDelayHigh_Type())
facilityPhysThresholdCapDifferentialGroupDelayHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:facilityPhysThresholdCapDifferentialGroupDelayHigh.setStatus(_A)
if mibBuilder.loadTexts:facilityPhysThresholdCapDifferentialGroupDelayHigh.setUnits('ps')
_EndOfFacilityPhysThresholdCapTable_Type=Integer32
_EndOfFacilityPhysThresholdCapTable_Object=MibScalar
endOfFacilityPhysThresholdCapTable=_EndOfFacilityPhysThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,12,2,2,2),_EndOfFacilityPhysThresholdCapTable_Type())
endOfFacilityPhysThresholdCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfFacilityPhysThresholdCapTable.setStatus(_A)
_EndOfPmFacilityPhysThresholdCap_Type=Integer32
_EndOfPmFacilityPhysThresholdCap_Object=MibScalar
endOfPmFacilityPhysThresholdCap=_EndOfPmFacilityPhysThresholdCap_Object((1,3,6,1,4,1,2544,1,11,9,6,12,2,2,10000),_EndOfPmFacilityPhysThresholdCap_Type())
endOfPmFacilityPhysThresholdCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfPmFacilityPhysThresholdCap.setStatus(_A)
_EndOfPmFacilityPhysicalCap_Type=Integer32
_EndOfPmFacilityPhysicalCap_Object=MibScalar
endOfPmFacilityPhysicalCap=_EndOfPmFacilityPhysicalCap_Object((1,3,6,1,4,1,2544,1,11,9,6,12,2,10000),_EndOfPmFacilityPhysicalCap_Type())
endOfPmFacilityPhysicalCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfPmFacilityPhysicalCap.setStatus(_A)
_EndOfPmFacilityCap_Type=Integer32
_EndOfPmFacilityCap_Object=MibScalar
endOfPmFacilityCap=_EndOfPmFacilityCap_Object((1,3,6,1,4,1,2544,1,11,9,6,12,10000),_EndOfPmFacilityCap_Type())
endOfPmFacilityCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfPmFacilityCap.setStatus(_A)
_PmTerminPointCap_ObjectIdentity=ObjectIdentity
pmTerminPointCap=_PmTerminPointCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,6,13))
_PmOptMuxCap_ObjectIdentity=ObjectIdentity
pmOptMuxCap=_PmOptMuxCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,6,14))
_PmOptMuxDataCap_ObjectIdentity=ObjectIdentity
pmOptMuxDataCap=_PmOptMuxDataCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,6,14,1))
_PmOptMuxPhysicalCap_ObjectIdentity=ObjectIdentity
pmOptMuxPhysicalCap=_PmOptMuxPhysicalCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,6,14,2))
_PmOptMuxPhysValueCap_ObjectIdentity=ObjectIdentity
pmOptMuxPhysValueCap=_PmOptMuxPhysValueCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,6,14,2,1))
_PmOptMuxPhysThresholdCap_ObjectIdentity=ObjectIdentity
pmOptMuxPhysThresholdCap=_PmOptMuxPhysThresholdCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,6,14,2,2))
_OptMuxPhysThresholdCapTable_Object=MibTable
optMuxPhysThresholdCapTable=_OptMuxPhysThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,14,2,2,2))
if mibBuilder.loadTexts:optMuxPhysThresholdCapTable.setStatus(_A)
_OptMuxPhysThresholdCapEntry_Object=MibTableRow
optMuxPhysThresholdCapEntry=_OptMuxPhysThresholdCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,6,14,2,2,2,1))
optMuxPhysThresholdCapEntry.setIndexNames((0,_C,_i),(0,_C,_j),(0,_C,_h),(0,_C,_g),(0,_C,_f))
if mibBuilder.loadTexts:optMuxPhysThresholdCapEntry.setStatus(_A)
_OptMuxPhysThresholdCapBrtxHighConfig_Type=FspR7Integer32Caps
_OptMuxPhysThresholdCapBrtxHighConfig_Object=MibTableColumn
optMuxPhysThresholdCapBrtxHighConfig=_OptMuxPhysThresholdCapBrtxHighConfig_Object((1,3,6,1,4,1,2544,1,11,9,6,14,2,2,2,1,1),_OptMuxPhysThresholdCapBrtxHighConfig_Type())
optMuxPhysThresholdCapBrtxHighConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:optMuxPhysThresholdCapBrtxHighConfig.setStatus(_A)
if mibBuilder.loadTexts:optMuxPhysThresholdCapBrtxHighConfig.setUnits(_F)
_OptMuxPhysThresholdCapBrPwrReceivedHighThres_Type=FspR7Integer32Caps
_OptMuxPhysThresholdCapBrPwrReceivedHighThres_Object=MibTableColumn
optMuxPhysThresholdCapBrPwrReceivedHighThres=_OptMuxPhysThresholdCapBrPwrReceivedHighThres_Object((1,3,6,1,4,1,2544,1,11,9,6,14,2,2,2,1,2),_OptMuxPhysThresholdCapBrPwrReceivedHighThres_Type())
optMuxPhysThresholdCapBrPwrReceivedHighThres.setMaxAccess(_B)
if mibBuilder.loadTexts:optMuxPhysThresholdCapBrPwrReceivedHighThres.setStatus(_A)
if mibBuilder.loadTexts:optMuxPhysThresholdCapBrPwrReceivedHighThres.setUnits(_F)
_OptMuxPhysThresholdCapConfigurableOpticalOutputPwrHigh_Type=FspR7Integer32Caps
_OptMuxPhysThresholdCapConfigurableOpticalOutputPwrHigh_Object=MibTableColumn
optMuxPhysThresholdCapConfigurableOpticalOutputPwrHigh=_OptMuxPhysThresholdCapConfigurableOpticalOutputPwrHigh_Object((1,3,6,1,4,1,2544,1,11,9,6,14,2,2,2,1,3),_OptMuxPhysThresholdCapConfigurableOpticalOutputPwrHigh_Type())
optMuxPhysThresholdCapConfigurableOpticalOutputPwrHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:optMuxPhysThresholdCapConfigurableOpticalOutputPwrHigh.setStatus(_A)
if mibBuilder.loadTexts:optMuxPhysThresholdCapConfigurableOpticalOutputPwrHigh.setUnits(_E)
_OptMuxPhysThresholdCapConfigurableOpticalOutputPwrLow_Type=FspR7Integer32Caps
_OptMuxPhysThresholdCapConfigurableOpticalOutputPwrLow_Object=MibTableColumn
optMuxPhysThresholdCapConfigurableOpticalOutputPwrLow=_OptMuxPhysThresholdCapConfigurableOpticalOutputPwrLow_Object((1,3,6,1,4,1,2544,1,11,9,6,14,2,2,2,1,4),_OptMuxPhysThresholdCapConfigurableOpticalOutputPwrLow_Type())
optMuxPhysThresholdCapConfigurableOpticalOutputPwrLow.setMaxAccess(_B)
if mibBuilder.loadTexts:optMuxPhysThresholdCapConfigurableOpticalOutputPwrLow.setStatus(_A)
if mibBuilder.loadTexts:optMuxPhysThresholdCapConfigurableOpticalOutputPwrLow.setUnits(_E)
_OptMuxPhysThresholdCapOscPwrRcvHighThres_Type=FspR7Integer32Caps
_OptMuxPhysThresholdCapOscPwrRcvHighThres_Object=MibTableColumn
optMuxPhysThresholdCapOscPwrRcvHighThres=_OptMuxPhysThresholdCapOscPwrRcvHighThres_Object((1,3,6,1,4,1,2544,1,11,9,6,14,2,2,2,1,5),_OptMuxPhysThresholdCapOscPwrRcvHighThres_Type())
optMuxPhysThresholdCapOscPwrRcvHighThres.setMaxAccess(_B)
if mibBuilder.loadTexts:optMuxPhysThresholdCapOscPwrRcvHighThres.setStatus(_A)
if mibBuilder.loadTexts:optMuxPhysThresholdCapOscPwrRcvHighThres.setUnits(_E)
_OptMuxPhysThresholdCapOscPwrRcvLowThres_Type=FspR7Integer32Caps
_OptMuxPhysThresholdCapOscPwrRcvLowThres_Object=MibTableColumn
optMuxPhysThresholdCapOscPwrRcvLowThres=_OptMuxPhysThresholdCapOscPwrRcvLowThres_Object((1,3,6,1,4,1,2544,1,11,9,6,14,2,2,2,1,6),_OptMuxPhysThresholdCapOscPwrRcvLowThres_Type())
optMuxPhysThresholdCapOscPwrRcvLowThres.setMaxAccess(_B)
if mibBuilder.loadTexts:optMuxPhysThresholdCapOscPwrRcvLowThres.setStatus(_A)
if mibBuilder.loadTexts:optMuxPhysThresholdCapOscPwrRcvLowThres.setUnits(_E)
_OptMuxPhysThresholdCapOpticalInputPwrHigh_Type=FspR7Integer32Caps
_OptMuxPhysThresholdCapOpticalInputPwrHigh_Object=MibTableColumn
optMuxPhysThresholdCapOpticalInputPwrHigh=_OptMuxPhysThresholdCapOpticalInputPwrHigh_Object((1,3,6,1,4,1,2544,1,11,9,6,14,2,2,2,1,7),_OptMuxPhysThresholdCapOpticalInputPwrHigh_Type())
optMuxPhysThresholdCapOpticalInputPwrHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:optMuxPhysThresholdCapOpticalInputPwrHigh.setStatus(_A)
if mibBuilder.loadTexts:optMuxPhysThresholdCapOpticalInputPwrHigh.setUnits(_E)
_OptMuxPhysThresholdCapOpticalInputPwrLow_Type=FspR7Integer32Caps
_OptMuxPhysThresholdCapOpticalInputPwrLow_Object=MibTableColumn
optMuxPhysThresholdCapOpticalInputPwrLow=_OptMuxPhysThresholdCapOpticalInputPwrLow_Object((1,3,6,1,4,1,2544,1,11,9,6,14,2,2,2,1,8),_OptMuxPhysThresholdCapOpticalInputPwrLow_Type())
optMuxPhysThresholdCapOpticalInputPwrLow.setMaxAccess(_B)
if mibBuilder.loadTexts:optMuxPhysThresholdCapOpticalInputPwrLow.setStatus(_A)
if mibBuilder.loadTexts:optMuxPhysThresholdCapOpticalInputPwrLow.setUnits(_E)
_OptMuxPhysThresholdCapAttRxHigh_Type=FspR7Integer32Caps
_OptMuxPhysThresholdCapAttRxHigh_Object=MibTableColumn
optMuxPhysThresholdCapAttRxHigh=_OptMuxPhysThresholdCapAttRxHigh_Object((1,3,6,1,4,1,2544,1,11,9,6,14,2,2,2,1,9),_OptMuxPhysThresholdCapAttRxHigh_Type())
optMuxPhysThresholdCapAttRxHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:optMuxPhysThresholdCapAttRxHigh.setStatus(_A)
if mibBuilder.loadTexts:optMuxPhysThresholdCapAttRxHigh.setUnits(_F)
_OptMuxPhysThresholdCapAttRxLow_Type=FspR7Integer32Caps
_OptMuxPhysThresholdCapAttRxLow_Object=MibTableColumn
optMuxPhysThresholdCapAttRxLow=_OptMuxPhysThresholdCapAttRxLow_Object((1,3,6,1,4,1,2544,1,11,9,6,14,2,2,2,1,10),_OptMuxPhysThresholdCapAttRxLow_Type())
optMuxPhysThresholdCapAttRxLow.setMaxAccess(_B)
if mibBuilder.loadTexts:optMuxPhysThresholdCapAttRxLow.setStatus(_A)
if mibBuilder.loadTexts:optMuxPhysThresholdCapAttRxLow.setUnits(_F)
_OptMuxPhysThresholdCapAttTxHigh_Type=FspR7Integer32Caps
_OptMuxPhysThresholdCapAttTxHigh_Object=MibTableColumn
optMuxPhysThresholdCapAttTxHigh=_OptMuxPhysThresholdCapAttTxHigh_Object((1,3,6,1,4,1,2544,1,11,9,6,14,2,2,2,1,11),_OptMuxPhysThresholdCapAttTxHigh_Type())
optMuxPhysThresholdCapAttTxHigh.setMaxAccess(_B)
if mibBuilder.loadTexts:optMuxPhysThresholdCapAttTxHigh.setStatus(_A)
if mibBuilder.loadTexts:optMuxPhysThresholdCapAttTxHigh.setUnits(_F)
_OptMuxPhysThresholdCapAttTxLow_Type=FspR7Integer32Caps
_OptMuxPhysThresholdCapAttTxLow_Object=MibTableColumn
optMuxPhysThresholdCapAttTxLow=_OptMuxPhysThresholdCapAttTxLow_Object((1,3,6,1,4,1,2544,1,11,9,6,14,2,2,2,1,12),_OptMuxPhysThresholdCapAttTxLow_Type())
optMuxPhysThresholdCapAttTxLow.setMaxAccess(_B)
if mibBuilder.loadTexts:optMuxPhysThresholdCapAttTxLow.setStatus(_A)
if mibBuilder.loadTexts:optMuxPhysThresholdCapAttTxLow.setUnits(_F)
_EndOfOptMuxPhysThresholdCapTable_Type=Integer32
_EndOfOptMuxPhysThresholdCapTable_Object=MibScalar
endOfOptMuxPhysThresholdCapTable=_EndOfOptMuxPhysThresholdCapTable_Object((1,3,6,1,4,1,2544,1,11,9,6,14,2,2,3),_EndOfOptMuxPhysThresholdCapTable_Type())
endOfOptMuxPhysThresholdCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfOptMuxPhysThresholdCapTable.setStatus(_A)
_EndOfPmOptMuxPhysThresholdCap_Type=Integer32
_EndOfPmOptMuxPhysThresholdCap_Object=MibScalar
endOfPmOptMuxPhysThresholdCap=_EndOfPmOptMuxPhysThresholdCap_Object((1,3,6,1,4,1,2544,1,11,9,6,14,2,2,10000),_EndOfPmOptMuxPhysThresholdCap_Type())
endOfPmOptMuxPhysThresholdCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfPmOptMuxPhysThresholdCap.setStatus(_A)
_FeatureSpecificCap_ObjectIdentity=ObjectIdentity
featureSpecificCap=_FeatureSpecificCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,7))
_FiberMapCap_ObjectIdentity=ObjectIdentity
fiberMapCap=_FiberMapCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,7,1))
_TerminationPointCapTable_Object=MibTable
terminationPointCapTable=_TerminationPointCapTable_Object((1,3,6,1,4,1,2544,1,11,9,7,1,1))
if mibBuilder.loadTexts:terminationPointCapTable.setStatus(_A)
_TerminationPointCapEntry_Object=MibTableRow
terminationPointCapEntry=_TerminationPointCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,7,1,1,1))
terminationPointCapEntry.setIndexNames((0,_C,_b),(0,_C,_c),(0,_C,_d),(0,_C,_e),(0,_C,_a))
if mibBuilder.loadTexts:terminationPointCapEntry.setStatus(_A)
_TerminationPointCapRowStatus_Type=FspR7RowStatusCaps
_TerminationPointCapRowStatus_Object=MibTableColumn
terminationPointCapRowStatus=_TerminationPointCapRowStatus_Object((1,3,6,1,4,1,2544,1,11,9,7,1,1,1,1),_TerminationPointCapRowStatus_Type())
terminationPointCapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:terminationPointCapRowStatus.setStatus(_A)
_TerminationPointCapAdmin_Type=FspR7AdminStateCaps
_TerminationPointCapAdmin_Object=MibTableColumn
terminationPointCapAdmin=_TerminationPointCapAdmin_Object((1,3,6,1,4,1,2544,1,11,9,7,1,1,1,2),_TerminationPointCapAdmin_Type())
terminationPointCapAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:terminationPointCapAdmin.setStatus(_A)
_TerminationPointCapFiberDetect_Type=FspR7FiberDetectCaps
_TerminationPointCapFiberDetect_Object=MibTableColumn
terminationPointCapFiberDetect=_TerminationPointCapFiberDetect_Object((1,3,6,1,4,1,2544,1,11,9,7,1,1,1,3),_TerminationPointCapFiberDetect_Type())
terminationPointCapFiberDetect.setMaxAccess(_B)
if mibBuilder.loadTexts:terminationPointCapFiberDetect.setStatus(_A)
_TerminationPointCapAlias_Type=Integer32
_TerminationPointCapAlias_Object=MibTableColumn
terminationPointCapAlias=_TerminationPointCapAlias_Object((1,3,6,1,4,1,2544,1,11,9,7,1,1,1,4),_TerminationPointCapAlias_Type())
terminationPointCapAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:terminationPointCapAlias.setStatus(_A)
_ConnectionCapTable_Object=MibTable
connectionCapTable=_ConnectionCapTable_Object((1,3,6,1,4,1,2544,1,11,9,7,1,2))
if mibBuilder.loadTexts:connectionCapTable.setStatus(_A)
_ConnectionCapEntry_Object=MibTableRow
connectionCapEntry=_ConnectionCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,7,1,2,1))
connectionCapEntry.setIndexNames((0,_C,_b),(0,_C,_c),(0,_C,_d),(0,_C,_e),(0,_C,_a),(0,_C,_b),(0,_C,_c),(0,_C,_d),(0,_C,_e),(0,_C,_a),(0,_C,_k))
if mibBuilder.loadTexts:connectionCapEntry.setStatus(_A)
_ConnectionCapRowStatus_Type=FspR7RowStatusCaps
_ConnectionCapRowStatus_Object=MibTableColumn
connectionCapRowStatus=_ConnectionCapRowStatus_Object((1,3,6,1,4,1,2544,1,11,9,7,1,2,1,1),_ConnectionCapRowStatus_Type())
connectionCapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:connectionCapRowStatus.setStatus(_A)
_ConnectionCapType_Type=FspR7TypeConnectionCaps
_ConnectionCapType_Object=MibTableColumn
connectionCapType=_ConnectionCapType_Object((1,3,6,1,4,1,2544,1,11,9,7,1,2,1,2),_ConnectionCapType_Type())
connectionCapType.setMaxAccess(_B)
if mibBuilder.loadTexts:connectionCapType.setStatus(_A)
_EndOfConnectionCapTable_Type=Integer32
_EndOfConnectionCapTable_Object=MibScalar
endOfConnectionCapTable=_EndOfConnectionCapTable_Object((1,3,6,1,4,1,2544,1,11,9,7,1,3),_EndOfConnectionCapTable_Type())
endOfConnectionCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfConnectionCapTable.setStatus(_A)
_EndOfFiberMapCap_Type=Integer32
_EndOfFiberMapCap_Object=MibScalar
endOfFiberMapCap=_EndOfFiberMapCap_Object((1,3,6,1,4,1,2544,1,11,9,7,1,10000),_EndOfFiberMapCap_Type())
endOfFiberMapCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfFiberMapCap.setStatus(_A)
_EciCap_ObjectIdentity=ObjectIdentity
eciCap=_EciCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,7,3))
_ExternalPortCapTable_Object=MibTable
externalPortCapTable=_ExternalPortCapTable_Object((1,3,6,1,4,1,2544,1,11,9,7,3,1))
if mibBuilder.loadTexts:externalPortCapTable.setStatus(_A)
_ExternalPortCapEntry_Object=MibTableRow
externalPortCapEntry=_ExternalPortCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,7,3,1,1))
externalPortCapEntry.setIndexNames((0,_C,_AK),(0,_C,_AL),(0,_C,_AJ),(0,_C,_AI),(0,_C,_AH))
if mibBuilder.loadTexts:externalPortCapEntry.setStatus(_A)
_ExternalPortCapRowStatus_Type=FspR7RowStatusCaps
_ExternalPortCapRowStatus_Object=MibTableColumn
externalPortCapRowStatus=_ExternalPortCapRowStatus_Object((1,3,6,1,4,1,2544,1,11,9,7,3,1,1,1),_ExternalPortCapRowStatus_Type())
externalPortCapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortCapRowStatus.setStatus(_A)
_ExternalPortCapType_Type=FspR7InterfaceTypeCaps
_ExternalPortCapType_Object=MibTableColumn
externalPortCapType=_ExternalPortCapType_Object((1,3,6,1,4,1,2544,1,11,9,7,3,1,1,2),_ExternalPortCapType_Type())
externalPortCapType.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortCapType.setStatus(_A)
_ExternalPortCapTransmitChannel_Type=FspR7ChannelIdentifierCaps
_ExternalPortCapTransmitChannel_Object=MibTableColumn
externalPortCapTransmitChannel=_ExternalPortCapTransmitChannel_Object((1,3,6,1,4,1,2544,1,11,9,7,3,1,1,3),_ExternalPortCapTransmitChannel_Type())
externalPortCapTransmitChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortCapTransmitChannel.setStatus(_A)
_ExternalPortCapChannelBandwith_Type=FspR7ChannelBandwidthCaps
_ExternalPortCapChannelBandwith_Object=MibTableColumn
externalPortCapChannelBandwith=_ExternalPortCapChannelBandwith_Object((1,3,6,1,4,1,2544,1,11,9,7,3,1,1,4),_ExternalPortCapChannelBandwith_Type())
externalPortCapChannelBandwith.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortCapChannelBandwith.setStatus(_A)
_ExternalPortCapAlias_Type=Integer32
_ExternalPortCapAlias_Object=MibTableColumn
externalPortCapAlias=_ExternalPortCapAlias_Object((1,3,6,1,4,1,2544,1,11,9,7,3,1,1,5),_ExternalPortCapAlias_Type())
externalPortCapAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortCapAlias.setStatus(_A)
_ExternalPortCapFarEndLocation_Type=Integer32
_ExternalPortCapFarEndLocation_Object=MibTableColumn
externalPortCapFarEndLocation=_ExternalPortCapFarEndLocation_Object((1,3,6,1,4,1,2544,1,11,9,7,3,1,1,6),_ExternalPortCapFarEndLocation_Type())
externalPortCapFarEndLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortCapFarEndLocation.setStatus(_A)
_ExternalPortCapBitrate_Type=FspR7Unsigned32Caps
_ExternalPortCapBitrate_Object=MibTableColumn
externalPortCapBitrate=_ExternalPortCapBitrate_Object((1,3,6,1,4,1,2544,1,11,9,7,3,1,1,7),_ExternalPortCapBitrate_Type())
externalPortCapBitrate.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortCapBitrate.setStatus(_A)
if mibBuilder.loadTexts:externalPortCapBitrate.setUnits('Mbps')
_ExternalPortCapFecType_Type=FspR7FecTypeCaps
_ExternalPortCapFecType_Object=MibTableColumn
externalPortCapFecType=_ExternalPortCapFecType_Object((1,3,6,1,4,1,2544,1,11,9,7,3,1,1,8),_ExternalPortCapFecType_Type())
externalPortCapFecType.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortCapFecType.setStatus(_A)
_ExternalPortCapLineCoding_Type=FspR7LineCodingCaps
_ExternalPortCapLineCoding_Object=MibTableColumn
externalPortCapLineCoding=_ExternalPortCapLineCoding_Object((1,3,6,1,4,1,2544,1,11,9,7,3,1,1,9),_ExternalPortCapLineCoding_Type())
externalPortCapLineCoding.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortCapLineCoding.setStatus(_A)
_ExternalPortCapFrameFormat_Type=FspR7FrameFormatCaps
_ExternalPortCapFrameFormat_Object=MibTableColumn
externalPortCapFrameFormat=_ExternalPortCapFrameFormat_Object((1,3,6,1,4,1,2544,1,11,9,7,3,1,1,10),_ExternalPortCapFrameFormat_Type())
externalPortCapFrameFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortCapFrameFormat.setStatus(_A)
_ExternalPortCapOpticalPowerTx_Type=FspR7Integer32Caps
_ExternalPortCapOpticalPowerTx_Object=MibTableColumn
externalPortCapOpticalPowerTx=_ExternalPortCapOpticalPowerTx_Object((1,3,6,1,4,1,2544,1,11,9,7,3,1,1,11),_ExternalPortCapOpticalPowerTx_Type())
externalPortCapOpticalPowerTx.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortCapOpticalPowerTx.setStatus(_A)
if mibBuilder.loadTexts:externalPortCapOpticalPowerTx.setUnits(_E)
_ExternalPortCapOsnrTransmit_Type=FspR7Unsigned32Caps
_ExternalPortCapOsnrTransmit_Object=MibTableColumn
externalPortCapOsnrTransmit=_ExternalPortCapOsnrTransmit_Object((1,3,6,1,4,1,2544,1,11,9,7,3,1,1,12),_ExternalPortCapOsnrTransmit_Type())
externalPortCapOsnrTransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortCapOsnrTransmit.setStatus(_A)
if mibBuilder.loadTexts:externalPortCapOsnrTransmit.setUnits('dB')
_ExternalPortCapPmdTransmit_Type=FspR7Unsigned32Caps
_ExternalPortCapPmdTransmit_Object=MibTableColumn
externalPortCapPmdTransmit=_ExternalPortCapPmdTransmit_Object((1,3,6,1,4,1,2544,1,11,9,7,3,1,1,13),_ExternalPortCapPmdTransmit_Type())
externalPortCapPmdTransmit.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortCapPmdTransmit.setStatus(_A)
if mibBuilder.loadTexts:externalPortCapPmdTransmit.setUnits('ps')
_ExternalPortCapChromDisperTx_Type=FspR7Integer32Caps
_ExternalPortCapChromDisperTx_Object=MibTableColumn
externalPortCapChromDisperTx=_ExternalPortCapChromDisperTx_Object((1,3,6,1,4,1,2544,1,11,9,7,3,1,1,14),_ExternalPortCapChromDisperTx_Type())
externalPortCapChromDisperTx.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortCapChromDisperTx.setStatus(_A)
if mibBuilder.loadTexts:externalPortCapChromDisperTx.setUnits(_N)
_ExternalPortCapMinOsnrRcv_Type=FspR7Unsigned32Caps
_ExternalPortCapMinOsnrRcv_Object=MibTableColumn
externalPortCapMinOsnrRcv=_ExternalPortCapMinOsnrRcv_Object((1,3,6,1,4,1,2544,1,11,9,7,3,1,1,15),_ExternalPortCapMinOsnrRcv_Type())
externalPortCapMinOsnrRcv.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortCapMinOsnrRcv.setStatus(_A)
if mibBuilder.loadTexts:externalPortCapMinOsnrRcv.setUnits('dB')
_ExternalPortCapMinOptPowerRcv_Type=FspR7Integer32Caps
_ExternalPortCapMinOptPowerRcv_Object=MibTableColumn
externalPortCapMinOptPowerRcv=_ExternalPortCapMinOptPowerRcv_Object((1,3,6,1,4,1,2544,1,11,9,7,3,1,1,16),_ExternalPortCapMinOptPowerRcv_Type())
externalPortCapMinOptPowerRcv.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortCapMinOptPowerRcv.setStatus(_A)
if mibBuilder.loadTexts:externalPortCapMinOptPowerRcv.setUnits(_E)
_ExternalPortCapMaxOptPowerRcv_Type=FspR7Integer32Caps
_ExternalPortCapMaxOptPowerRcv_Object=MibTableColumn
externalPortCapMaxOptPowerRcv=_ExternalPortCapMaxOptPowerRcv_Object((1,3,6,1,4,1,2544,1,11,9,7,3,1,1,17),_ExternalPortCapMaxOptPowerRcv_Type())
externalPortCapMaxOptPowerRcv.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortCapMaxOptPowerRcv.setStatus(_A)
if mibBuilder.loadTexts:externalPortCapMaxOptPowerRcv.setUnits(_E)
_ExternalPortCapMaxPmdRcv_Type=FspR7Unsigned32Caps
_ExternalPortCapMaxPmdRcv_Object=MibTableColumn
externalPortCapMaxPmdRcv=_ExternalPortCapMaxPmdRcv_Object((1,3,6,1,4,1,2544,1,11,9,7,3,1,1,18),_ExternalPortCapMaxPmdRcv_Type())
externalPortCapMaxPmdRcv.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortCapMaxPmdRcv.setStatus(_A)
if mibBuilder.loadTexts:externalPortCapMaxPmdRcv.setUnits('ps')
_ExternalPortCapMinChromDisperRcv_Type=FspR7Integer32Caps
_ExternalPortCapMinChromDisperRcv_Object=MibTableColumn
externalPortCapMinChromDisperRcv=_ExternalPortCapMinChromDisperRcv_Object((1,3,6,1,4,1,2544,1,11,9,7,3,1,1,19),_ExternalPortCapMinChromDisperRcv_Type())
externalPortCapMinChromDisperRcv.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortCapMinChromDisperRcv.setStatus(_A)
if mibBuilder.loadTexts:externalPortCapMinChromDisperRcv.setUnits(_N)
_ExternalPortCapMaxChromDisperRcv_Type=FspR7Integer32Caps
_ExternalPortCapMaxChromDisperRcv_Object=MibTableColumn
externalPortCapMaxChromDisperRcv=_ExternalPortCapMaxChromDisperRcv_Object((1,3,6,1,4,1,2544,1,11,9,7,3,1,1,20),_ExternalPortCapMaxChromDisperRcv_Type())
externalPortCapMaxChromDisperRcv.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortCapMaxChromDisperRcv.setStatus(_A)
if mibBuilder.loadTexts:externalPortCapMaxChromDisperRcv.setUnits(_N)
_ExternalPortCapMaxBitErrorRate_Type=FspR7MaxBitErrorRateCaps
_ExternalPortCapMaxBitErrorRate_Object=MibTableColumn
externalPortCapMaxBitErrorRate=_ExternalPortCapMaxBitErrorRate_Object((1,3,6,1,4,1,2544,1,11,9,7,3,1,1,21),_ExternalPortCapMaxBitErrorRate_Type())
externalPortCapMaxBitErrorRate.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortCapMaxBitErrorRate.setStatus(_A)
_ExternalPortCapSourceProfile_Type=Integer32
_ExternalPortCapSourceProfile_Object=MibTableColumn
externalPortCapSourceProfile=_ExternalPortCapSourceProfile_Object((1,3,6,1,4,1,2544,1,11,9,7,3,1,1,22),_ExternalPortCapSourceProfile_Type())
externalPortCapSourceProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:externalPortCapSourceProfile.setStatus(_A)
_EndOfExternalPortCapTable_Type=Integer32
_EndOfExternalPortCapTable_Object=MibScalar
endOfExternalPortCapTable=_EndOfExternalPortCapTable_Object((1,3,6,1,4,1,2544,1,11,9,7,3,2),_EndOfExternalPortCapTable_Type())
endOfExternalPortCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfExternalPortCapTable.setStatus(_A)
_EndOfEciCap_Type=Integer32
_EndOfEciCap_Object=MibScalar
endOfEciCap=_EndOfEciCap_Object((1,3,6,1,4,1,2544,1,11,9,7,3,10000),_EndOfEciCap_Type())
endOfEciCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfEciCap.setStatus(_A)
_ChangeServiceCap_ObjectIdentity=ObjectIdentity
changeServiceCap=_ChangeServiceCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,7,5))
_ChangePhysicalPortServiceCapTable_Object=MibTable
changePhysicalPortServiceCapTable=_ChangePhysicalPortServiceCapTable_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1))
if mibBuilder.loadTexts:changePhysicalPortServiceCapTable.setStatus(_A)
_ChangePhysicalPortServiceCapEntry_Object=MibTableRow
changePhysicalPortServiceCapEntry=_ChangePhysicalPortServiceCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1))
changePhysicalPortServiceCapEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_K),(0,_C,_J),(0,_C,_I))
if mibBuilder.loadTexts:changePhysicalPortServiceCapEntry.setStatus(_A)
_ChangePhysicalPortServiceCapRowStatus_Type=FspR7RowStatusCaps
_ChangePhysicalPortServiceCapRowStatus_Object=MibTableColumn
changePhysicalPortServiceCapRowStatus=_ChangePhysicalPortServiceCapRowStatus_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,1),_ChangePhysicalPortServiceCapRowStatus_Type())
changePhysicalPortServiceCapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapRowStatus.setStatus(_A)
_ChangePhysicalPortServiceCapType_Type=FspR7InterfaceTypeCaps
_ChangePhysicalPortServiceCapType_Object=MibTableColumn
changePhysicalPortServiceCapType=_ChangePhysicalPortServiceCapType_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,2),_ChangePhysicalPortServiceCapType_Type())
changePhysicalPortServiceCapType.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapType.setStatus(_A)
_ChangePhysicalPortServiceCapAdmin_Type=FspR7AdminStateCaps
_ChangePhysicalPortServiceCapAdmin_Object=MibTableColumn
changePhysicalPortServiceCapAdmin=_ChangePhysicalPortServiceCapAdmin_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,3),_ChangePhysicalPortServiceCapAdmin_Type())
changePhysicalPortServiceCapAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapAdmin.setStatus(_A)
_ChangePhysicalPortServiceCapAlias_Type=Integer32
_ChangePhysicalPortServiceCapAlias_Object=MibTableColumn
changePhysicalPortServiceCapAlias=_ChangePhysicalPortServiceCapAlias_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,4),_ChangePhysicalPortServiceCapAlias_Type())
changePhysicalPortServiceCapAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapAlias.setStatus(_A)
_ChangePhysicalPortServiceCapAlsMode_Type=FspR7AlsModeCaps
_ChangePhysicalPortServiceCapAlsMode_Object=MibTableColumn
changePhysicalPortServiceCapAlsMode=_ChangePhysicalPortServiceCapAlsMode_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,5),_ChangePhysicalPortServiceCapAlsMode_Type())
changePhysicalPortServiceCapAlsMode.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapAlsMode.setStatus(_A)
_ChangePhysicalPortServiceCapBehaviour_Type=FspR7PortBehaviourCaps
_ChangePhysicalPortServiceCapBehaviour_Object=MibTableColumn
changePhysicalPortServiceCapBehaviour=_ChangePhysicalPortServiceCapBehaviour_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,6),_ChangePhysicalPortServiceCapBehaviour_Type())
changePhysicalPortServiceCapBehaviour.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapBehaviour.setStatus(_A)
_ChangePhysicalPortServiceCapDispersionSetting_Type=FspR7Integer32Caps
_ChangePhysicalPortServiceCapDispersionSetting_Object=MibTableColumn
changePhysicalPortServiceCapDispersionSetting=_ChangePhysicalPortServiceCapDispersionSetting_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,7),_ChangePhysicalPortServiceCapDispersionSetting_Type())
changePhysicalPortServiceCapDispersionSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapDispersionSetting.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceCapDispersionSetting.setUnits(_N)
_ChangePhysicalPortServiceCapDispersionMode_Type=FspR7DispersionModesCaps
_ChangePhysicalPortServiceCapDispersionMode_Object=MibTableColumn
changePhysicalPortServiceCapDispersionMode=_ChangePhysicalPortServiceCapDispersionMode_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,8),_ChangePhysicalPortServiceCapDispersionMode_Type())
changePhysicalPortServiceCapDispersionMode.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapDispersionMode.setStatus(_A)
_ChangePhysicalPortServiceCapChannelProv_Type=FspR7ChannelIdentifierCaps
_ChangePhysicalPortServiceCapChannelProv_Object=MibTableColumn
changePhysicalPortServiceCapChannelProv=_ChangePhysicalPortServiceCapChannelProv_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,9),_ChangePhysicalPortServiceCapChannelProv_Type())
changePhysicalPortServiceCapChannelProv.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapChannelProv.setStatus(_A)
_ChangePhysicalPortServiceCapWdmRxChannel_Type=FspR7ChannelIdentifierCaps
_ChangePhysicalPortServiceCapWdmRxChannel_Object=MibTableColumn
changePhysicalPortServiceCapWdmRxChannel=_ChangePhysicalPortServiceCapWdmRxChannel_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,10),_ChangePhysicalPortServiceCapWdmRxChannel_Type())
changePhysicalPortServiceCapWdmRxChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapWdmRxChannel.setStatus(_A)
_ChangePhysicalPortServiceCapCodeGain_Type=FspR7CodeGainCaps
_ChangePhysicalPortServiceCapCodeGain_Object=MibTableColumn
changePhysicalPortServiceCapCodeGain=_ChangePhysicalPortServiceCapCodeGain_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,11),_ChangePhysicalPortServiceCapCodeGain_Type())
changePhysicalPortServiceCapCodeGain.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapCodeGain.setStatus(_A)
_ChangePhysicalPortServiceCapXfpDecisionThres_Type=FspR7XfpDecisionThresCaps
_ChangePhysicalPortServiceCapXfpDecisionThres_Object=MibTableColumn
changePhysicalPortServiceCapXfpDecisionThres=_ChangePhysicalPortServiceCapXfpDecisionThres_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,12),_ChangePhysicalPortServiceCapXfpDecisionThres_Type())
changePhysicalPortServiceCapXfpDecisionThres.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapXfpDecisionThres.setStatus(_A)
_ChangePhysicalPortServiceCapDisparityCorrection_Type=EnableStateCaps
_ChangePhysicalPortServiceCapDisparityCorrection_Object=MibTableColumn
changePhysicalPortServiceCapDisparityCorrection=_ChangePhysicalPortServiceCapDisparityCorrection_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,13),_ChangePhysicalPortServiceCapDisparityCorrection_Type())
changePhysicalPortServiceCapDisparityCorrection.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapDisparityCorrection.setStatus(_A)
_ChangePhysicalPortServiceCapEqlzAdmin_Type=FspR7EqlzAdminStateCaps
_ChangePhysicalPortServiceCapEqlzAdmin_Object=MibTableColumn
changePhysicalPortServiceCapEqlzAdmin=_ChangePhysicalPortServiceCapEqlzAdmin_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,14),_ChangePhysicalPortServiceCapEqlzAdmin_Type())
changePhysicalPortServiceCapEqlzAdmin.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapEqlzAdmin.setStatus(_A)
_ChangePhysicalPortServiceCapErrorForwarding_Type=FspR7ErrorFwdModeCaps
_ChangePhysicalPortServiceCapErrorForwarding_Object=MibTableColumn
changePhysicalPortServiceCapErrorForwarding=_ChangePhysicalPortServiceCapErrorForwarding_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,15),_ChangePhysicalPortServiceCapErrorForwarding_Type())
changePhysicalPortServiceCapErrorForwarding.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapErrorForwarding.setStatus(_A)
_ChangePhysicalPortServiceCapFecType_Type=FspR7FecTypeCaps
_ChangePhysicalPortServiceCapFecType_Object=MibTableColumn
changePhysicalPortServiceCapFecType=_ChangePhysicalPortServiceCapFecType_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,16),_ChangePhysicalPortServiceCapFecType_Type())
changePhysicalPortServiceCapFecType.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapFecType.setStatus(_A)
_ChangePhysicalPortServiceCapFarEndCommunication_Type=FspR7YesNoCaps
_ChangePhysicalPortServiceCapFarEndCommunication_Object=MibTableColumn
changePhysicalPortServiceCapFarEndCommunication=_ChangePhysicalPortServiceCapFarEndCommunication_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,17),_ChangePhysicalPortServiceCapFarEndCommunication_Type())
changePhysicalPortServiceCapFarEndCommunication.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapFarEndCommunication.setStatus(_A)
_ChangePhysicalPortServiceCapFlowControl_Type=FspR7FlowControlModeCaps
_ChangePhysicalPortServiceCapFlowControl_Object=MibTableColumn
changePhysicalPortServiceCapFlowControl=_ChangePhysicalPortServiceCapFlowControl_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,18),_ChangePhysicalPortServiceCapFlowControl_Type())
changePhysicalPortServiceCapFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapFlowControl.setStatus(_A)
_ChangePhysicalPortServiceCapLaneChannelSetting_Type=FspR7ChannelIdentifierCaps
_ChangePhysicalPortServiceCapLaneChannelSetting_Object=MibTableColumn
changePhysicalPortServiceCapLaneChannelSetting=_ChangePhysicalPortServiceCapLaneChannelSetting_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,19),_ChangePhysicalPortServiceCapLaneChannelSetting_Type())
changePhysicalPortServiceCapLaneChannelSetting.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapLaneChannelSetting.setStatus(_A)
_ChangePhysicalPortServiceCapLaserDelayTimer_Type=FspR7LaserDelayTimerCaps
_ChangePhysicalPortServiceCapLaserDelayTimer_Object=MibTableColumn
changePhysicalPortServiceCapLaserDelayTimer=_ChangePhysicalPortServiceCapLaserDelayTimer_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,20),_ChangePhysicalPortServiceCapLaserDelayTimer_Type())
changePhysicalPortServiceCapLaserDelayTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapLaserDelayTimer.setStatus(_A)
_ChangePhysicalPortServiceCapLaserOffTimer_Type=FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapLaserOffTimer_Object=MibTableColumn
changePhysicalPortServiceCapLaserOffTimer=_ChangePhysicalPortServiceCapLaserOffTimer_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,21),_ChangePhysicalPortServiceCapLaserOffTimer_Type())
changePhysicalPortServiceCapLaserOffTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapLaserOffTimer.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceCapLaserOffTimer.setUnits(_O)
_ChangePhysicalPortServiceCapLaserOnTimer_Type=FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapLaserOnTimer_Object=MibTableColumn
changePhysicalPortServiceCapLaserOnTimer=_ChangePhysicalPortServiceCapLaserOnTimer_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,22),_ChangePhysicalPortServiceCapLaserOnTimer_Type())
changePhysicalPortServiceCapLaserOnTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapLaserOnTimer.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceCapLaserOnTimer.setUnits(_O)
_ChangePhysicalPortServiceCapLaserOffDelayFunction_Type=EnableStateCaps
_ChangePhysicalPortServiceCapLaserOffDelayFunction_Object=MibTableColumn
changePhysicalPortServiceCapLaserOffDelayFunction=_ChangePhysicalPortServiceCapLaserOffDelayFunction_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,23),_ChangePhysicalPortServiceCapLaserOffDelayFunction_Type())
changePhysicalPortServiceCapLaserOffDelayFunction.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapLaserOffDelayFunction.setStatus(_A)
_ChangePhysicalPortServiceCapAutoPTassignment_Type=FspR7ManualAutoCaps
_ChangePhysicalPortServiceCapAutoPTassignment_Object=MibTableColumn
changePhysicalPortServiceCapAutoPTassignment=_ChangePhysicalPortServiceCapAutoPTassignment_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,24),_ChangePhysicalPortServiceCapAutoPTassignment_Type())
changePhysicalPortServiceCapAutoPTassignment.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapAutoPTassignment.setStatus(_A)
_ChangePhysicalPortServiceCapTributarySlotMethod_Type=FspR7ManualAutoCaps
_ChangePhysicalPortServiceCapTributarySlotMethod_Object=MibTableColumn
changePhysicalPortServiceCapTributarySlotMethod=_ChangePhysicalPortServiceCapTributarySlotMethod_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,25),_ChangePhysicalPortServiceCapTributarySlotMethod_Type())
changePhysicalPortServiceCapTributarySlotMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTributarySlotMethod.setStatus(_A)
_ChangePhysicalPortServiceCapOpticalSetPoint_Type=FspR7Integer32Caps
_ChangePhysicalPortServiceCapOpticalSetPoint_Object=MibTableColumn
changePhysicalPortServiceCapOpticalSetPoint=_ChangePhysicalPortServiceCapOpticalSetPoint_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,26),_ChangePhysicalPortServiceCapOpticalSetPoint_Type())
changePhysicalPortServiceCapOpticalSetPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapOpticalSetPoint.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceCapOpticalSetPoint.setUnits(_E)
_ChangePhysicalPortServiceCapOpuPayloadType_Type=FspR7OpuPayloadTypeCaps
_ChangePhysicalPortServiceCapOpuPayloadType_Object=MibTableColumn
changePhysicalPortServiceCapOpuPayloadType=_ChangePhysicalPortServiceCapOpuPayloadType_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,27),_ChangePhysicalPortServiceCapOpuPayloadType_Type())
changePhysicalPortServiceCapOpuPayloadType.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapOpuPayloadType.setStatus(_A)
_ChangePhysicalPortServiceCapSigDegThresSonetLine_Type=FspR7BERThresholdCaps
_ChangePhysicalPortServiceCapSigDegThresSonetLine_Object=MibTableColumn
changePhysicalPortServiceCapSigDegThresSonetLine=_ChangePhysicalPortServiceCapSigDegThresSonetLine_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,28),_ChangePhysicalPortServiceCapSigDegThresSonetLine_Type())
changePhysicalPortServiceCapSigDegThresSonetLine.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegThresSonetLine.setStatus(_A)
_ChangePhysicalPortServiceCapSigDegThresSdhMs_Type=FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapSigDegThresSdhMs_Object=MibTableColumn
changePhysicalPortServiceCapSigDegThresSdhMs=_ChangePhysicalPortServiceCapSigDegThresSdhMs_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,29),_ChangePhysicalPortServiceCapSigDegThresSdhMs_Type())
changePhysicalPortServiceCapSigDegThresSdhMs.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegThresSdhMs.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegThresSdhMs.setUnits(_G)
_ChangePhysicalPortServiceCapSigDegThresOtu_Type=FspR7Integer32Caps
_ChangePhysicalPortServiceCapSigDegThresOtu_Object=MibTableColumn
changePhysicalPortServiceCapSigDegThresOtu=_ChangePhysicalPortServiceCapSigDegThresOtu_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,30),_ChangePhysicalPortServiceCapSigDegThresOtu_Type())
changePhysicalPortServiceCapSigDegThresOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegThresOtu.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegThresOtu.setUnits(_G)
_ChangePhysicalPortServiceCapSigDegThresOdu_Type=FspR7Integer32Caps
_ChangePhysicalPortServiceCapSigDegThresOdu_Object=MibTableColumn
changePhysicalPortServiceCapSigDegThresOdu=_ChangePhysicalPortServiceCapSigDegThresOdu_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,31),_ChangePhysicalPortServiceCapSigDegThresOdu_Type())
changePhysicalPortServiceCapSigDegThresOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegThresOdu.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegThresOdu.setUnits(_G)
_ChangePhysicalPortServiceCapSigDegThreshold_Type=FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapSigDegThreshold_Object=MibTableColumn
changePhysicalPortServiceCapSigDegThreshold=_ChangePhysicalPortServiceCapSigDegThreshold_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,32),_ChangePhysicalPortServiceCapSigDegThreshold_Type())
changePhysicalPortServiceCapSigDegThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegThreshold.setStatus(_A)
_ChangePhysicalPortServiceCapSigDegPcslThreshold_Type=FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapSigDegPcslThreshold_Object=MibTableColumn
changePhysicalPortServiceCapSigDegPcslThreshold=_ChangePhysicalPortServiceCapSigDegPcslThreshold_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,33),_ChangePhysicalPortServiceCapSigDegPcslThreshold_Type())
changePhysicalPortServiceCapSigDegPcslThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegPcslThreshold.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegPcslThreshold.setUnits(_G)
_ChangePhysicalPortServiceCapSigDegThresSonetSection_Type=FspR7BERThresholdSectionCaps
_ChangePhysicalPortServiceCapSigDegThresSonetSection_Object=MibTableColumn
changePhysicalPortServiceCapSigDegThresSonetSection=_ChangePhysicalPortServiceCapSigDegThresSonetSection_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,34),_ChangePhysicalPortServiceCapSigDegThresSonetSection_Type())
changePhysicalPortServiceCapSigDegThresSonetSection.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegThresSonetSection.setStatus(_A)
_ChangePhysicalPortServiceCapSigDegThresSdhSection_Type=FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapSigDegThresSdhSection_Object=MibTableColumn
changePhysicalPortServiceCapSigDegThresSdhSection=_ChangePhysicalPortServiceCapSigDegThresSdhSection_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,35),_ChangePhysicalPortServiceCapSigDegThresSdhSection_Type())
changePhysicalPortServiceCapSigDegThresSdhSection.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegThresSdhSection.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegThresSdhSection.setUnits(_G)
_ChangePhysicalPortServiceCapSigDegThresOduTcmA_Type=FspR7Integer32Caps
_ChangePhysicalPortServiceCapSigDegThresOduTcmA_Object=MibTableColumn
changePhysicalPortServiceCapSigDegThresOduTcmA=_ChangePhysicalPortServiceCapSigDegThresOduTcmA_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,36),_ChangePhysicalPortServiceCapSigDegThresOduTcmA_Type())
changePhysicalPortServiceCapSigDegThresOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegThresOduTcmA.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegThresOduTcmA.setUnits(_G)
_ChangePhysicalPortServiceCapSigDegThresOduTcmB_Type=FspR7Integer32Caps
_ChangePhysicalPortServiceCapSigDegThresOduTcmB_Object=MibTableColumn
changePhysicalPortServiceCapSigDegThresOduTcmB=_ChangePhysicalPortServiceCapSigDegThresOduTcmB_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,37),_ChangePhysicalPortServiceCapSigDegThresOduTcmB_Type())
changePhysicalPortServiceCapSigDegThresOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegThresOduTcmB.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegThresOduTcmB.setUnits(_G)
_ChangePhysicalPortServiceCapSigDegThresOduTcmC_Type=FspR7Integer32Caps
_ChangePhysicalPortServiceCapSigDegThresOduTcmC_Object=MibTableColumn
changePhysicalPortServiceCapSigDegThresOduTcmC=_ChangePhysicalPortServiceCapSigDegThresOduTcmC_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,38),_ChangePhysicalPortServiceCapSigDegThresOduTcmC_Type())
changePhysicalPortServiceCapSigDegThresOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegThresOduTcmC.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegThresOduTcmC.setUnits(_G)
_ChangePhysicalPortServiceCapSignalDegradePeriod_Type=FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapSignalDegradePeriod_Object=MibTableColumn
changePhysicalPortServiceCapSignalDegradePeriod=_ChangePhysicalPortServiceCapSignalDegradePeriod_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,39),_ChangePhysicalPortServiceCapSignalDegradePeriod_Type())
changePhysicalPortServiceCapSignalDegradePeriod.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSignalDegradePeriod.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSignalDegradePeriod.setUnits(_H)
_ChangePhysicalPortServiceCapSigDegPeriodOdu_Type=FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapSigDegPeriodOdu_Object=MibTableColumn
changePhysicalPortServiceCapSigDegPeriodOdu=_ChangePhysicalPortServiceCapSigDegPeriodOdu_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,40),_ChangePhysicalPortServiceCapSigDegPeriodOdu_Type())
changePhysicalPortServiceCapSigDegPeriodOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegPeriodOdu.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegPeriodOdu.setUnits(_H)
_ChangePhysicalPortServiceCapSigDegPeriodOtu_Type=FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapSigDegPeriodOtu_Object=MibTableColumn
changePhysicalPortServiceCapSigDegPeriodOtu=_ChangePhysicalPortServiceCapSigDegPeriodOtu_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,41),_ChangePhysicalPortServiceCapSigDegPeriodOtu_Type())
changePhysicalPortServiceCapSigDegPeriodOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegPeriodOtu.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegPeriodOtu.setUnits(_H)
_ChangePhysicalPortServiceCapSigDegPeriodIntegration_Type=FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapSigDegPeriodIntegration_Object=MibTableColumn
changePhysicalPortServiceCapSigDegPeriodIntegration=_ChangePhysicalPortServiceCapSigDegPeriodIntegration_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,42),_ChangePhysicalPortServiceCapSigDegPeriodIntegration_Type())
changePhysicalPortServiceCapSigDegPeriodIntegration.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegPeriodIntegration.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegPeriodIntegration.setUnits(_H)
_ChangePhysicalPortServiceCapSigDegPeriodSdhSection_Type=FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapSigDegPeriodSdhSection_Object=MibTableColumn
changePhysicalPortServiceCapSigDegPeriodSdhSection=_ChangePhysicalPortServiceCapSigDegPeriodSdhSection_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,43),_ChangePhysicalPortServiceCapSigDegPeriodSdhSection_Type())
changePhysicalPortServiceCapSigDegPeriodSdhSection.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegPeriodSdhSection.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegPeriodSdhSection.setUnits(_H)
_ChangePhysicalPortServiceCapSigDegPeriodOduTcmA_Type=FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapSigDegPeriodOduTcmA_Object=MibTableColumn
changePhysicalPortServiceCapSigDegPeriodOduTcmA=_ChangePhysicalPortServiceCapSigDegPeriodOduTcmA_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,44),_ChangePhysicalPortServiceCapSigDegPeriodOduTcmA_Type())
changePhysicalPortServiceCapSigDegPeriodOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegPeriodOduTcmA.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegPeriodOduTcmA.setUnits(_H)
_ChangePhysicalPortServiceCapSigDegPeriodOduTcmB_Type=FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapSigDegPeriodOduTcmB_Object=MibTableColumn
changePhysicalPortServiceCapSigDegPeriodOduTcmB=_ChangePhysicalPortServiceCapSigDegPeriodOduTcmB_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,45),_ChangePhysicalPortServiceCapSigDegPeriodOduTcmB_Type())
changePhysicalPortServiceCapSigDegPeriodOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegPeriodOduTcmB.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegPeriodOduTcmB.setUnits(_H)
_ChangePhysicalPortServiceCapSigDegPeriodOduTcmC_Type=FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapSigDegPeriodOduTcmC_Object=MibTableColumn
changePhysicalPortServiceCapSigDegPeriodOduTcmC=_ChangePhysicalPortServiceCapSigDegPeriodOduTcmC_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,46),_ChangePhysicalPortServiceCapSigDegPeriodOduTcmC_Type())
changePhysicalPortServiceCapSigDegPeriodOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegPeriodOduTcmC.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceCapSigDegPeriodOduTcmC.setUnits(_H)
_ChangePhysicalPortServiceCapOtnStuffing_Type=FspR7StuffCaps
_ChangePhysicalPortServiceCapOtnStuffing_Object=MibTableColumn
changePhysicalPortServiceCapOtnStuffing=_ChangePhysicalPortServiceCapOtnStuffing_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,47),_ChangePhysicalPortServiceCapOtnStuffing_Type())
changePhysicalPortServiceCapOtnStuffing.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapOtnStuffing.setStatus(_A)
_ChangePhysicalPortServiceCapTcmALevel_Type=OtnTcmLevelCaps
_ChangePhysicalPortServiceCapTcmALevel_Object=MibTableColumn
changePhysicalPortServiceCapTcmALevel=_ChangePhysicalPortServiceCapTcmALevel_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,48),_ChangePhysicalPortServiceCapTcmALevel_Type())
changePhysicalPortServiceCapTcmALevel.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTcmALevel.setStatus(_A)
_ChangePhysicalPortServiceCapTcmBLevel_Type=OtnTcmLevelCaps
_ChangePhysicalPortServiceCapTcmBLevel_Object=MibTableColumn
changePhysicalPortServiceCapTcmBLevel=_ChangePhysicalPortServiceCapTcmBLevel_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,49),_ChangePhysicalPortServiceCapTcmBLevel_Type())
changePhysicalPortServiceCapTcmBLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTcmBLevel.setStatus(_A)
_ChangePhysicalPortServiceCapTcmCLevel_Type=OtnTcmLevelCaps
_ChangePhysicalPortServiceCapTcmCLevel_Object=MibTableColumn
changePhysicalPortServiceCapTcmCLevel=_ChangePhysicalPortServiceCapTcmCLevel_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,50),_ChangePhysicalPortServiceCapTcmCLevel_Type())
changePhysicalPortServiceCapTcmCLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTcmCLevel.setStatus(_A)
_ChangePhysicalPortServiceCapTerminationLevel_Type=OhTerminationLevelCaps
_ChangePhysicalPortServiceCapTerminationLevel_Object=MibTableColumn
changePhysicalPortServiceCapTerminationLevel=_ChangePhysicalPortServiceCapTerminationLevel_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,51),_ChangePhysicalPortServiceCapTerminationLevel_Type())
changePhysicalPortServiceCapTerminationLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTerminationLevel.setStatus(_A)
_ChangePhysicalPortServiceCapTimingSource_Type=SonetTimingSourceCaps
_ChangePhysicalPortServiceCapTimingSource_Object=MibTableColumn
changePhysicalPortServiceCapTimingSource=_ChangePhysicalPortServiceCapTimingSource_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,52),_ChangePhysicalPortServiceCapTimingSource_Type())
changePhysicalPortServiceCapTimingSource.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTimingSource.setStatus(_A)
_ChangePhysicalPortServiceCapTimModeOdu_Type=TimModeCaps
_ChangePhysicalPortServiceCapTimModeOdu_Object=MibTableColumn
changePhysicalPortServiceCapTimModeOdu=_ChangePhysicalPortServiceCapTimModeOdu_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,53),_ChangePhysicalPortServiceCapTimModeOdu_Type())
changePhysicalPortServiceCapTimModeOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTimModeOdu.setStatus(_A)
_ChangePhysicalPortServiceCapTimModeOtu_Type=TimModeCaps
_ChangePhysicalPortServiceCapTimModeOtu_Object=MibTableColumn
changePhysicalPortServiceCapTimModeOtu=_ChangePhysicalPortServiceCapTimModeOtu_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,54),_ChangePhysicalPortServiceCapTimModeOtu_Type())
changePhysicalPortServiceCapTimModeOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTimModeOtu.setStatus(_A)
_ChangePhysicalPortServiceCapTimModeSonetSection_Type=TimModeCaps
_ChangePhysicalPortServiceCapTimModeSonetSection_Object=MibTableColumn
changePhysicalPortServiceCapTimModeSonetSection=_ChangePhysicalPortServiceCapTimModeSonetSection_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,55),_ChangePhysicalPortServiceCapTimModeSonetSection_Type())
changePhysicalPortServiceCapTimModeSonetSection.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTimModeSonetSection.setStatus(_A)
_ChangePhysicalPortServiceCapTimModeOduTcmA_Type=TimModeCaps
_ChangePhysicalPortServiceCapTimModeOduTcmA_Object=MibTableColumn
changePhysicalPortServiceCapTimModeOduTcmA=_ChangePhysicalPortServiceCapTimModeOduTcmA_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,56),_ChangePhysicalPortServiceCapTimModeOduTcmA_Type())
changePhysicalPortServiceCapTimModeOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTimModeOduTcmA.setStatus(_A)
_ChangePhysicalPortServiceCapTimModeOduTcmB_Type=TimModeCaps
_ChangePhysicalPortServiceCapTimModeOduTcmB_Object=MibTableColumn
changePhysicalPortServiceCapTimModeOduTcmB=_ChangePhysicalPortServiceCapTimModeOduTcmB_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,57),_ChangePhysicalPortServiceCapTimModeOduTcmB_Type())
changePhysicalPortServiceCapTimModeOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTimModeOduTcmB.setStatus(_A)
_ChangePhysicalPortServiceCapTimModeOduTcmC_Type=TimModeCaps
_ChangePhysicalPortServiceCapTimModeOduTcmC_Object=MibTableColumn
changePhysicalPortServiceCapTimModeOduTcmC=_ChangePhysicalPortServiceCapTimModeOduTcmC_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,58),_ChangePhysicalPortServiceCapTimModeOduTcmC_Type())
changePhysicalPortServiceCapTimModeOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTimModeOduTcmC.setStatus(_A)
_ChangePhysicalPortServiceCapTraceFormSonetSection_Type=SonetTraceFormCaps
_ChangePhysicalPortServiceCapTraceFormSonetSection_Object=MibTableColumn
changePhysicalPortServiceCapTraceFormSonetSection=_ChangePhysicalPortServiceCapTraceFormSonetSection_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,59),_ChangePhysicalPortServiceCapTraceFormSonetSection_Type())
changePhysicalPortServiceCapTraceFormSonetSection.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTraceFormSonetSection.setStatus(_A)
_ChangePhysicalPortServiceCapTraceExpectedSonetSection_Type=Integer32
_ChangePhysicalPortServiceCapTraceExpectedSonetSection_Object=MibTableColumn
changePhysicalPortServiceCapTraceExpectedSonetSection=_ChangePhysicalPortServiceCapTraceExpectedSonetSection_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,60),_ChangePhysicalPortServiceCapTraceExpectedSonetSection_Type())
changePhysicalPortServiceCapTraceExpectedSonetSection.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTraceExpectedSonetSection.setStatus(_A)
_ChangePhysicalPortServiceCapTraceTransmitSonetSection_Type=Integer32
_ChangePhysicalPortServiceCapTraceTransmitSonetSection_Object=MibTableColumn
changePhysicalPortServiceCapTraceTransmitSonetSection=_ChangePhysicalPortServiceCapTraceTransmitSonetSection_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,61),_ChangePhysicalPortServiceCapTraceTransmitSonetSection_Type())
changePhysicalPortServiceCapTraceTransmitSonetSection.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTraceTransmitSonetSection.setStatus(_A)
_ChangePhysicalPortServiceCapTraceExpectedOtu_Type=Integer32
_ChangePhysicalPortServiceCapTraceExpectedOtu_Object=MibTableColumn
changePhysicalPortServiceCapTraceExpectedOtu=_ChangePhysicalPortServiceCapTraceExpectedOtu_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,62),_ChangePhysicalPortServiceCapTraceExpectedOtu_Type())
changePhysicalPortServiceCapTraceExpectedOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTraceExpectedOtu.setStatus(_A)
_ChangePhysicalPortServiceCapTraceTransmitSapiOtu_Type=Integer32
_ChangePhysicalPortServiceCapTraceTransmitSapiOtu_Object=MibTableColumn
changePhysicalPortServiceCapTraceTransmitSapiOtu=_ChangePhysicalPortServiceCapTraceTransmitSapiOtu_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,63),_ChangePhysicalPortServiceCapTraceTransmitSapiOtu_Type())
changePhysicalPortServiceCapTraceTransmitSapiOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTraceTransmitSapiOtu.setStatus(_A)
_ChangePhysicalPortServiceCapTraceTransmitDapiOtu_Type=Integer32
_ChangePhysicalPortServiceCapTraceTransmitDapiOtu_Object=MibTableColumn
changePhysicalPortServiceCapTraceTransmitDapiOtu=_ChangePhysicalPortServiceCapTraceTransmitDapiOtu_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,64),_ChangePhysicalPortServiceCapTraceTransmitDapiOtu_Type())
changePhysicalPortServiceCapTraceTransmitDapiOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTraceTransmitDapiOtu.setStatus(_A)
_ChangePhysicalPortServiceCapTraceTransmitOpspOtu_Type=Integer32
_ChangePhysicalPortServiceCapTraceTransmitOpspOtu_Object=MibTableColumn
changePhysicalPortServiceCapTraceTransmitOpspOtu=_ChangePhysicalPortServiceCapTraceTransmitOpspOtu_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,65),_ChangePhysicalPortServiceCapTraceTransmitOpspOtu_Type())
changePhysicalPortServiceCapTraceTransmitOpspOtu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTraceTransmitOpspOtu.setStatus(_A)
_ChangePhysicalPortServiceCapTraceExpectedOdu_Type=Integer32
_ChangePhysicalPortServiceCapTraceExpectedOdu_Object=MibTableColumn
changePhysicalPortServiceCapTraceExpectedOdu=_ChangePhysicalPortServiceCapTraceExpectedOdu_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,66),_ChangePhysicalPortServiceCapTraceExpectedOdu_Type())
changePhysicalPortServiceCapTraceExpectedOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTraceExpectedOdu.setStatus(_A)
_ChangePhysicalPortServiceCapTraceTransmitSapiOdu_Type=Integer32
_ChangePhysicalPortServiceCapTraceTransmitSapiOdu_Object=MibTableColumn
changePhysicalPortServiceCapTraceTransmitSapiOdu=_ChangePhysicalPortServiceCapTraceTransmitSapiOdu_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,67),_ChangePhysicalPortServiceCapTraceTransmitSapiOdu_Type())
changePhysicalPortServiceCapTraceTransmitSapiOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTraceTransmitSapiOdu.setStatus(_A)
_ChangePhysicalPortServiceCapTraceTransmitDapiOdu_Type=Integer32
_ChangePhysicalPortServiceCapTraceTransmitDapiOdu_Object=MibTableColumn
changePhysicalPortServiceCapTraceTransmitDapiOdu=_ChangePhysicalPortServiceCapTraceTransmitDapiOdu_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,68),_ChangePhysicalPortServiceCapTraceTransmitDapiOdu_Type())
changePhysicalPortServiceCapTraceTransmitDapiOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTraceTransmitDapiOdu.setStatus(_A)
_ChangePhysicalPortServiceCapTraceTransmitOpspOdu_Type=Integer32
_ChangePhysicalPortServiceCapTraceTransmitOpspOdu_Object=MibTableColumn
changePhysicalPortServiceCapTraceTransmitOpspOdu=_ChangePhysicalPortServiceCapTraceTransmitOpspOdu_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,69),_ChangePhysicalPortServiceCapTraceTransmitOpspOdu_Type())
changePhysicalPortServiceCapTraceTransmitOpspOdu.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTraceTransmitOpspOdu.setStatus(_A)
_ChangePhysicalPortServiceCapTraceExpectedOduTcmA_Type=Integer32
_ChangePhysicalPortServiceCapTraceExpectedOduTcmA_Object=MibTableColumn
changePhysicalPortServiceCapTraceExpectedOduTcmA=_ChangePhysicalPortServiceCapTraceExpectedOduTcmA_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,70),_ChangePhysicalPortServiceCapTraceExpectedOduTcmA_Type())
changePhysicalPortServiceCapTraceExpectedOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTraceExpectedOduTcmA.setStatus(_A)
_ChangePhysicalPortServiceCapTraceTransmitSapiOduTcmA_Type=Integer32
_ChangePhysicalPortServiceCapTraceTransmitSapiOduTcmA_Object=MibTableColumn
changePhysicalPortServiceCapTraceTransmitSapiOduTcmA=_ChangePhysicalPortServiceCapTraceTransmitSapiOduTcmA_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,71),_ChangePhysicalPortServiceCapTraceTransmitSapiOduTcmA_Type())
changePhysicalPortServiceCapTraceTransmitSapiOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTraceTransmitSapiOduTcmA.setStatus(_A)
_ChangePhysicalPortServiceCapTraceTransmitDapiOduTcmA_Type=Integer32
_ChangePhysicalPortServiceCapTraceTransmitDapiOduTcmA_Object=MibTableColumn
changePhysicalPortServiceCapTraceTransmitDapiOduTcmA=_ChangePhysicalPortServiceCapTraceTransmitDapiOduTcmA_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,72),_ChangePhysicalPortServiceCapTraceTransmitDapiOduTcmA_Type())
changePhysicalPortServiceCapTraceTransmitDapiOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTraceTransmitDapiOduTcmA.setStatus(_A)
_ChangePhysicalPortServiceCapTraceTransmitOpspOduTcmA_Type=Integer32
_ChangePhysicalPortServiceCapTraceTransmitOpspOduTcmA_Object=MibTableColumn
changePhysicalPortServiceCapTraceTransmitOpspOduTcmA=_ChangePhysicalPortServiceCapTraceTransmitOpspOduTcmA_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,73),_ChangePhysicalPortServiceCapTraceTransmitOpspOduTcmA_Type())
changePhysicalPortServiceCapTraceTransmitOpspOduTcmA.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTraceTransmitOpspOduTcmA.setStatus(_A)
_ChangePhysicalPortServiceCapTraceExpectedOduTcmB_Type=Integer32
_ChangePhysicalPortServiceCapTraceExpectedOduTcmB_Object=MibTableColumn
changePhysicalPortServiceCapTraceExpectedOduTcmB=_ChangePhysicalPortServiceCapTraceExpectedOduTcmB_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,74),_ChangePhysicalPortServiceCapTraceExpectedOduTcmB_Type())
changePhysicalPortServiceCapTraceExpectedOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTraceExpectedOduTcmB.setStatus(_A)
_ChangePhysicalPortServiceCapTraceTransmitSapiOduTcmB_Type=Integer32
_ChangePhysicalPortServiceCapTraceTransmitSapiOduTcmB_Object=MibTableColumn
changePhysicalPortServiceCapTraceTransmitSapiOduTcmB=_ChangePhysicalPortServiceCapTraceTransmitSapiOduTcmB_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,75),_ChangePhysicalPortServiceCapTraceTransmitSapiOduTcmB_Type())
changePhysicalPortServiceCapTraceTransmitSapiOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTraceTransmitSapiOduTcmB.setStatus(_A)
_ChangePhysicalPortServiceCapTraceTransmitDapiOduTcmB_Type=Integer32
_ChangePhysicalPortServiceCapTraceTransmitDapiOduTcmB_Object=MibTableColumn
changePhysicalPortServiceCapTraceTransmitDapiOduTcmB=_ChangePhysicalPortServiceCapTraceTransmitDapiOduTcmB_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,76),_ChangePhysicalPortServiceCapTraceTransmitDapiOduTcmB_Type())
changePhysicalPortServiceCapTraceTransmitDapiOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTraceTransmitDapiOduTcmB.setStatus(_A)
_ChangePhysicalPortServiceCapTraceTransmitOpspOduTcmB_Type=Integer32
_ChangePhysicalPortServiceCapTraceTransmitOpspOduTcmB_Object=MibTableColumn
changePhysicalPortServiceCapTraceTransmitOpspOduTcmB=_ChangePhysicalPortServiceCapTraceTransmitOpspOduTcmB_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,77),_ChangePhysicalPortServiceCapTraceTransmitOpspOduTcmB_Type())
changePhysicalPortServiceCapTraceTransmitOpspOduTcmB.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTraceTransmitOpspOduTcmB.setStatus(_A)
_ChangePhysicalPortServiceCapTraceExpectedOduTcmC_Type=Integer32
_ChangePhysicalPortServiceCapTraceExpectedOduTcmC_Object=MibTableColumn
changePhysicalPortServiceCapTraceExpectedOduTcmC=_ChangePhysicalPortServiceCapTraceExpectedOduTcmC_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,78),_ChangePhysicalPortServiceCapTraceExpectedOduTcmC_Type())
changePhysicalPortServiceCapTraceExpectedOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTraceExpectedOduTcmC.setStatus(_A)
_ChangePhysicalPortServiceCapTraceTransmitSapiOduTcmC_Type=Integer32
_ChangePhysicalPortServiceCapTraceTransmitSapiOduTcmC_Object=MibTableColumn
changePhysicalPortServiceCapTraceTransmitSapiOduTcmC=_ChangePhysicalPortServiceCapTraceTransmitSapiOduTcmC_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,79),_ChangePhysicalPortServiceCapTraceTransmitSapiOduTcmC_Type())
changePhysicalPortServiceCapTraceTransmitSapiOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTraceTransmitSapiOduTcmC.setStatus(_A)
_ChangePhysicalPortServiceCapTraceTransmitDapiOduTcmC_Type=Integer32
_ChangePhysicalPortServiceCapTraceTransmitDapiOduTcmC_Object=MibTableColumn
changePhysicalPortServiceCapTraceTransmitDapiOduTcmC=_ChangePhysicalPortServiceCapTraceTransmitDapiOduTcmC_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,80),_ChangePhysicalPortServiceCapTraceTransmitDapiOduTcmC_Type())
changePhysicalPortServiceCapTraceTransmitDapiOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTraceTransmitDapiOduTcmC.setStatus(_A)
_ChangePhysicalPortServiceCapTraceTransmitOpspOduTcmC_Type=Integer32
_ChangePhysicalPortServiceCapTraceTransmitOpspOduTcmC_Object=MibTableColumn
changePhysicalPortServiceCapTraceTransmitOpspOduTcmC=_ChangePhysicalPortServiceCapTraceTransmitOpspOduTcmC_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,81),_ChangePhysicalPortServiceCapTraceTransmitOpspOduTcmC_Type())
changePhysicalPortServiceCapTraceTransmitOpspOduTcmC.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTraceTransmitOpspOduTcmC.setStatus(_A)
_ChangePhysicalPortServiceCapTxOffDelay_Type=FspR7EnableDisableCaps
_ChangePhysicalPortServiceCapTxOffDelay_Object=MibTableColumn
changePhysicalPortServiceCapTxOffDelay=_ChangePhysicalPortServiceCapTxOffDelay_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,82),_ChangePhysicalPortServiceCapTxOffDelay_Type())
changePhysicalPortServiceCapTxOffDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTxOffDelay.setStatus(_A)
_ChangePhysicalPortServiceCapVoaMode_Type=FspR7VoaModeCaps
_ChangePhysicalPortServiceCapVoaMode_Object=MibTableColumn
changePhysicalPortServiceCapVoaMode=_ChangePhysicalPortServiceCapVoaMode_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,83),_ChangePhysicalPortServiceCapVoaMode_Type())
changePhysicalPortServiceCapVoaMode.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapVoaMode.setStatus(_A)
_ChangePhysicalPortServiceCapVoaSetpoint_Type=FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapVoaSetpoint_Object=MibTableColumn
changePhysicalPortServiceCapVoaSetpoint=_ChangePhysicalPortServiceCapVoaSetpoint_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,84),_ChangePhysicalPortServiceCapVoaSetpoint_Type())
changePhysicalPortServiceCapVoaSetpoint.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapVoaSetpoint.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceCapVoaSetpoint.setUnits(_F)
_ChangePhysicalPortServiceCapTxOffOnTm_Type=FspR7TxOffOnTmCaps
_ChangePhysicalPortServiceCapTxOffOnTm_Object=MibTableColumn
changePhysicalPortServiceCapTxOffOnTm=_ChangePhysicalPortServiceCapTxOffOnTm_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,85),_ChangePhysicalPortServiceCapTxOffOnTm_Type())
changePhysicalPortServiceCapTxOffOnTm.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTxOffOnTm.setStatus(_A)
_ChangePhysicalPortServiceCapTxOffTimer_Type=FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapTxOffTimer_Object=MibTableColumn
changePhysicalPortServiceCapTxOffTimer=_ChangePhysicalPortServiceCapTxOffTimer_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,86),_ChangePhysicalPortServiceCapTxOffTimer_Type())
changePhysicalPortServiceCapTxOffTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTxOffTimer.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTxOffTimer.setUnits(_O)
_ChangePhysicalPortServiceCapTxOnTimer_Type=FspR7Unsigned32Caps
_ChangePhysicalPortServiceCapTxOnTimer_Object=MibTableColumn
changePhysicalPortServiceCapTxOnTimer=_ChangePhysicalPortServiceCapTxOnTimer_Object((1,3,6,1,4,1,2544,1,11,9,7,5,1,1,87),_ChangePhysicalPortServiceCapTxOnTimer_Type())
changePhysicalPortServiceCapTxOnTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTxOnTimer.setStatus(_A)
if mibBuilder.loadTexts:changePhysicalPortServiceCapTxOnTimer.setUnits(_O)
_EndOfChangePhysicalPortServiceCapTable_Type=Integer32
_EndOfChangePhysicalPortServiceCapTable_Object=MibScalar
endOfChangePhysicalPortServiceCapTable=_EndOfChangePhysicalPortServiceCapTable_Object((1,3,6,1,4,1,2544,1,11,9,7,5,2),_EndOfChangePhysicalPortServiceCapTable_Type())
endOfChangePhysicalPortServiceCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfChangePhysicalPortServiceCapTable.setStatus(_A)
_EndOfChangeServiceCap_Type=Integer32
_EndOfChangeServiceCap_Object=MibScalar
endOfChangeServiceCap=_EndOfChangeServiceCap_Object((1,3,6,1,4,1,2544,1,11,9,7,5,10000),_EndOfChangeServiceCap_Type())
endOfChangeServiceCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfChangeServiceCap.setStatus(_A)
_ProtectionCap_ObjectIdentity=ObjectIdentity
protectionCap=_ProtectionCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,7,6))
_FfpCapTable_Object=MibTable
ffpCapTable=_FfpCapTable_Object((1,3,6,1,4,1,2544,1,11,9,7,6,2))
if mibBuilder.loadTexts:ffpCapTable.setStatus(_A)
_FfpCapEntry_Object=MibTableRow
ffpCapEntry=_FfpCapEntry_Object((1,3,6,1,4,1,2544,1,11,9,7,6,2,1))
ffpCapEntry.setIndexNames((0,_C,_AP),(0,_C,_AQ),(0,_C,_AO),(0,_C,_AN),(0,_C,_AM))
if mibBuilder.loadTexts:ffpCapEntry.setStatus(_A)
_FfpCapRowStatus_Type=FspR7RowStatusCaps
_FfpCapRowStatus_Object=MibTableColumn
ffpCapRowStatus=_FfpCapRowStatus_Object((1,3,6,1,4,1,2544,1,11,9,7,6,2,1,1),_FfpCapRowStatus_Type())
ffpCapRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpCapRowStatus.setStatus(_A)
_FfpCapCreationMethod_Type=FfpTypeCaps
_FfpCapCreationMethod_Object=MibTableColumn
ffpCapCreationMethod=_FfpCapCreationMethod_Object((1,3,6,1,4,1,2544,1,11,9,7,6,2,1,2),_FfpCapCreationMethod_Type())
ffpCapCreationMethod.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpCapCreationMethod.setStatus(_A)
_FfpCapSDswitching_Type=EnableStateCaps
_FfpCapSDswitching_Object=MibTableColumn
ffpCapSDswitching=_FfpCapSDswitching_Object((1,3,6,1,4,1,2544,1,11,9,7,6,2,1,3),_FfpCapSDswitching_Type())
ffpCapSDswitching.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpCapSDswitching.setStatus(_A)
_FfpCapHoldOffTime_Type=ApsHoldoffTimeCaps
_FfpCapHoldOffTime_Object=MibTableColumn
ffpCapHoldOffTime=_FfpCapHoldOffTime_Object((1,3,6,1,4,1,2544,1,11,9,7,6,2,1,4),_FfpCapHoldOffTime_Type())
ffpCapHoldOffTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpCapHoldOffTime.setStatus(_A)
_FfpCapProtectionMech_Type=ProtectionMechCaps
_FfpCapProtectionMech_Object=MibTableColumn
ffpCapProtectionMech=_FfpCapProtectionMech_Object((1,3,6,1,4,1,2544,1,11,9,7,6,2,1,5),_FfpCapProtectionMech_Type())
ffpCapProtectionMech.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpCapProtectionMech.setStatus(_A)
_FfpCapWorkingAid_Type=SnmpAdminString
_FfpCapWorkingAid_Object=MibTableColumn
ffpCapWorkingAid=_FfpCapWorkingAid_Object((1,3,6,1,4,1,2544,1,11,9,7,6,2,1,6),_FfpCapWorkingAid_Type())
ffpCapWorkingAid.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpCapWorkingAid.setStatus(_A)
_FfpCapProtectionAid_Type=SnmpAdminString
_FfpCapProtectionAid_Object=MibTableColumn
ffpCapProtectionAid=_FfpCapProtectionAid_Object((1,3,6,1,4,1,2544,1,11,9,7,6,2,1,7),_FfpCapProtectionAid_Type())
ffpCapProtectionAid.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpCapProtectionAid.setStatus(_A)
_FfpCapSignalDegradeSwitching_Type=EnableStateCaps
_FfpCapSignalDegradeSwitching_Object=MibTableColumn
ffpCapSignalDegradeSwitching=_FfpCapSignalDegradeSwitching_Object((1,3,6,1,4,1,2544,1,11,9,7,6,2,1,8),_FfpCapSignalDegradeSwitching_Type())
ffpCapSignalDegradeSwitching.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpCapSignalDegradeSwitching.setStatus(_A)
_FfpCapFarEndIp_Type=FspR7YesNo
_FfpCapFarEndIp_Object=MibTableColumn
ffpCapFarEndIp=_FfpCapFarEndIp_Object((1,3,6,1,4,1,2544,1,11,9,7,6,2,1,9),_FfpCapFarEndIp_Type())
ffpCapFarEndIp.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpCapFarEndIp.setStatus(_A)
_FfpCapPeerAid_Type=SnmpAdminString
_FfpCapPeerAid_Object=MibTableColumn
ffpCapPeerAid=_FfpCapPeerAid_Object((1,3,6,1,4,1,2544,1,11,9,7,6,2,1,10),_FfpCapPeerAid_Type())
ffpCapPeerAid.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpCapPeerAid.setStatus(_A)
_FfpCapApsType_Type=ApsTypeCaps
_FfpCapApsType_Object=MibTableColumn
ffpCapApsType=_FfpCapApsType_Object((1,3,6,1,4,1,2544,1,11,9,7,6,2,1,11),_FfpCapApsType_Type())
ffpCapApsType.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpCapApsType.setStatus(_A)
_FfpCapRevertMode_Type=ApsRevertModeCaps
_FfpCapRevertMode_Object=MibTableColumn
ffpCapRevertMode=_FfpCapRevertMode_Object((1,3,6,1,4,1,2544,1,11,9,7,6,2,1,12),_FfpCapRevertMode_Type())
ffpCapRevertMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpCapRevertMode.setStatus(_A)
_FfpCapWaitToRestore_Type=FspR7Unsigned32Caps
_FfpCapWaitToRestore_Object=MibTableColumn
ffpCapWaitToRestore=_FfpCapWaitToRestore_Object((1,3,6,1,4,1,2544,1,11,9,7,6,2,1,13),_FfpCapWaitToRestore_Type())
ffpCapWaitToRestore.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpCapWaitToRestore.setStatus(_A)
if mibBuilder.loadTexts:ffpCapWaitToRestore.setUnits('min')
_FfpCapDirection_Type=ApsDirectionCaps
_FfpCapDirection_Object=MibTableColumn
ffpCapDirection=_FfpCapDirection_Object((1,3,6,1,4,1,2544,1,11,9,7,6,2,1,14),_FfpCapDirection_Type())
ffpCapDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:ffpCapDirection.setStatus(_A)
_EndOfFfpCapTable_Type=Integer32
_EndOfFfpCapTable_Object=MibScalar
endOfFfpCapTable=_EndOfFfpCapTable_Object((1,3,6,1,4,1,2544,1,11,9,7,6,3),_EndOfFfpCapTable_Type())
endOfFfpCapTable.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfFfpCapTable.setStatus(_A)
_EndOfProtectionCap_Type=Integer32
_EndOfProtectionCap_Object=MibScalar
endOfProtectionCap=_EndOfProtectionCap_Object((1,3,6,1,4,1,2544,1,11,9,7,6,10000),_EndOfProtectionCap_Type())
endOfProtectionCap.setMaxAccess(_B)
if mibBuilder.loadTexts:endOfProtectionCap.setStatus(_A)
_ConformanceCap_ObjectIdentity=ObjectIdentity
conformanceCap=_ConformanceCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,10))
_CompliancesCap_ObjectIdentity=ObjectIdentity
compliancesCap=_CompliancesCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,10,1))
_GroupsCap_ObjectIdentity=ObjectIdentity
groupsCap=_GroupsCap_ObjectIdentity((1,3,6,1,4,1,2544,1,11,9,10,2))
objectGroupCap=ObjectGroup((1,3,6,1,4,1,2544,1,11,9,10,2,1))
objectGroupCap.setObjects(*((_D,_Aj),(_D,_Ak),(_D,_Al),(_D,_Am),(_D,_An),(_D,_Ao),(_D,_Ap),(_D,_Aq),(_D,_Ar),(_D,_As),(_D,_At),(_D,_Au),(_D,_Av),(_D,_Aw),(_D,_Ax),(_D,_Ay),(_D,_Az),(_D,_A_),(_D,_B0),(_D,_B1),(_D,_B2),(_D,_B3),(_D,_B4),(_D,_B5),(_D,_B6),(_D,_B7),(_D,_B8),(_D,_B9),(_D,_BA),(_D,_BB),(_D,_BC),(_D,_BD),(_D,_BE),(_D,_BF),(_D,_BG),(_D,_BH),(_D,_BI),(_D,_BJ),(_D,_BK),(_D,_BL),(_D,_BM),(_D,_BN),(_D,_BO),(_D,_BP),(_D,_BQ),(_D,_BR),(_D,_BS),(_D,_BT),(_D,_BU),(_D,_BV),(_D,_BW),(_D,_BX),(_D,_BY),(_D,_BZ),(_D,_Ba),(_D,_Bb)))
if mibBuilder.loadTexts:objectGroupCap.setStatus(_A)
complianceCap=ModuleCompliance((1,3,6,1,4,1,2544,1,11,9,10,1,1))
complianceCap.setObjects((_D,_Bc))
if mibBuilder.loadTexts:complianceCap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'advaFspR7Cap':advaFspR7Cap,'managementCap':managementCap,'specificMgmtCap':specificMgmtCap,'crossConnectionCapTable':crossConnectionCapTable,'crossConnectionCapEntry':crossConnectionCapEntry,_Aj:crossConnectionCapRowStatus,_Ak:crossConnectionCapAdmin,_Al:crossConnectionCapRedLineState,_Am:crossConnectionCapConn,_An:crossConnectionCapAlias,_Ao:crossConnectionCapPathNode,_Ap:crossConnectionCapTunnelAid,_Aw:crossConnectionCapType,'crossConnectionCapCrsFunction':crossConnectionCapCrsFunction,'crossConnectionCapCrsFromAidTwo':crossConnectionCapCrsFromAidTwo,'crossConnectionCapCrsToAidTwo':crossConnectionCapCrsToAidTwo,'crossConnectionCapCrsMcAidList':crossConnectionCapCrsMcAidList,'crossConnectionCapCrsContAidList':crossConnectionCapCrsContAidList,'crossConnectionCapCrsContAidListTwo':crossConnectionCapCrsContAidListTwo,'crossOpticalLineCapTable':crossOpticalLineCapTable,'crossOpticalLineCapEntry':crossOpticalLineCapEntry,_Aq:crossOpticalLineCapRowStatus,_Ar:crossOpticalLineCapRedLineState,_As:crossOpticalLineCapConn,_At:crossOpticalLineCapCrsType,_Au:crossOpticalLineCapAlias,_Av:crossOpticalLineCapTunnelAid,'endOfCrossOpticalLineCapTable':endOfCrossOpticalLineCapTable,'crossDcnCapTable':crossDcnCapTable,'crossDcnCapEntry':crossDcnCapEntry,'crossDcnCapRowStatus':crossDcnCapRowStatus,'crossDcnCapType':crossDcnCapType,'crossDcnCapLink':crossDcnCapLink,'crossDcnCapEcc':crossDcnCapEcc,'endOfCrossDcnCapTable':endOfCrossDcnCapTable,'endOfSpecificMgmtCap':endOfSpecificMgmtCap,'eqptMgmtCap':eqptMgmtCap,'shelfCapTable':shelfCapTable,'shelfCapEntry':shelfCapEntry,'shelfCapRowStatus':shelfCapRowStatus,'shelfCapPsuOutputPower':shelfCapPsuOutputPower,'shelfCapType':shelfCapType,'shelfCapRack':shelfCapRack,'shelfCapSupply':shelfCapSupply,'shelfCapBandProvision':shelfCapBandProvision,'shelfCapAdmin':shelfCapAdmin,'shelfCapRackNumber':shelfCapRackNumber,'shelfCapRackOrder':shelfCapRackOrder,'shelfCapAlias':shelfCapAlias,'shelfCapSlot':shelfCapSlot,'endOfShelfCapTable':endOfShelfCapTable,'fanCapTable':fanCapTable,'fanCapEntry':fanCapEntry,'fanCapRowStatus':fanCapRowStatus,'fanCapForceDestroy':fanCapForceDestroy,'fanCapAdmin':fanCapAdmin,'fanCapType':fanCapType,'fanCapAlias':fanCapAlias,'fanCapOutputReset':fanCapOutputReset,'endOfFanCapTable':endOfFanCapTable,'plugCapTable':plugCapTable,'plugCapEntry':plugCapEntry,'plugCapRowStatus':plugCapRowStatus,'plugCapConnector':plugCapConnector,'plugCapType':plugCapType,'plugCapReach':plugCapReach,'plugCapLoopbackAttenuation':plugCapLoopbackAttenuation,'plugCapTransmitChannel':plugCapTransmitChannel,'plugCapAlias':plugCapAlias,'plugCapLaneGroup':plugCapLaneGroup,'plugCapMaxDataRate':plugCapMaxDataRate,'plugCapThirdPartyUsage':plugCapThirdPartyUsage,'plugCapAdmin':plugCapAdmin,'plugCapBidirectionalChannel':plugCapBidirectionalChannel,'plugCapChannelSpacingProvision':plugCapChannelSpacingProvision,'endOfPlugCapTable':endOfPlugCapTable,'moduleCapTable':moduleCapTable,'moduleCapEntry':moduleCapEntry,'moduleCapRowStatus':moduleCapRowStatus,'moduleCapForceDestroy':moduleCapForceDestroy,'moduleCapPsuOutputPower':moduleCapPsuOutputPower,'moduleCapPower':moduleCapPower,'moduleCapReach':moduleCapReach,'moduleCapInitEqlz':moduleCapInitEqlz,'moduleCapLanAid':moduleCapLanAid,'moduleCapType':moduleCapType,'moduleCapMapping':moduleCapMapping,'moduleCapGainRange':moduleCapGainRange,'moduleCapSfProvision':moduleCapSfProvision,'moduleCapCapabilityLevelProvision':moduleCapCapabilityLevelProvision,'moduleCapDCFiberType':moduleCapDCFiberType,'moduleCapChannelsProvision':moduleCapChannelsProvision,'moduleCapFiberDetect':moduleCapFiberDetect,'moduleCapSupply':moduleCapSupply,'moduleCapGroup':moduleCapGroup,'moduleCapDeploy':moduleCapDeploy,'moduleCapLagSysPrio':moduleCapLagSysPrio,'moduleCapTransmitChannel':moduleCapTransmitChannel,'moduleCapBand':moduleCapBand,'moduleCapTrafficDirection':moduleCapTrafficDirection,'moduleCapIpAddr':moduleCapIpAddr,'moduleCapDispersionCompensation':moduleCapDispersionCompensation,'moduleCapActivateDetect':moduleCapActivateDetect,'moduleCapOscUsage':moduleCapOscUsage,'moduleCapAdmin':moduleCapAdmin,'moduleCapScrambling':moduleCapScrambling,'moduleCapChannelsNumber':moduleCapChannelsNumber,'moduleCapChannelSpacingProvision':moduleCapChannelSpacingProvision,'moduleCapMode':moduleCapMode,'moduleCapSubBandProvision':moduleCapSubBandProvision,'moduleCapAlias':moduleCapAlias,'moduleCapFiberType':moduleCapFiberType,'moduleCapChannelSpacing':moduleCapChannelSpacing,'moduleCapOutputReset':moduleCapOutputReset,'moduleCapRoadmNumber':moduleCapRoadmNumber,'moduleCapTopology':moduleCapTopology,'moduleCapForceConfig':moduleCapForceConfig,'moduleCapMuxMethod':moduleCapMuxMethod,'moduleCapNdpCleanup':moduleCapNdpCleanup,'moduleCapRstp':moduleCapRstp,'moduleCapRemoteReset':moduleCapRemoteReset,'endOfModuleCap':endOfModuleCap,'protectionCableCapTable':protectionCableCapTable,'protectionCableCapEntry':protectionCableCapEntry,'protectionCableCapRowStatus':protectionCableCapRowStatus,'protectionCableCapType':protectionCableCapType,'endOfProtectionCableCap':endOfProtectionCableCap,'filterCableCapTable':filterCableCapTable,'filterCableCapEntry':filterCableCapEntry,'filterCableCapRowStatus':filterCableCapRowStatus,'filterCableCapType':filterCableCapType,'endOfFilterCableCap':endOfFilterCableCap,'endOfEqptMgmCap':endOfEqptMgmCap,'facilityMgmtCap':facilityMgmtCap,'physicalPortCapTable':physicalPortCapTable,'physicalPortCapEntry':physicalPortCapEntry,_Ax:physicalPortCapRowStatus,_Ay:physicalPortCapType,_Az:physicalPortCapAdmin,'physicalPortCapAlias':physicalPortCapAlias,'physicalPortCapAlsMode':physicalPortCapAlsMode,'physicalPortCapAutoThresReset':physicalPortCapAutoThresReset,'physicalPortCapAutonegotiation':physicalPortCapAutonegotiation,'physicalPortCapBehaviour':physicalPortCapBehaviour,'physicalPortCapDispertionConfig':physicalPortCapDispertionConfig,'physicalPortCapDispersionSetting':physicalPortCapDispersionSetting,'physicalPortCapDispersionMode':physicalPortCapDispersionMode,'physicalPortCapChannelProv':physicalPortCapChannelProv,'physicalPortCapWdmRxChannel':physicalPortCapWdmRxChannel,'physicalPortCapCodeGain':physicalPortCapCodeGain,'physicalPortCapXfpDecisionThres':physicalPortCapXfpDecisionThres,'physicalPortCapDisparityCorrection':physicalPortCapDisparityCorrection,'physicalPortCapEqlzAdmin':physicalPortCapEqlzAdmin,'physicalPortCapErrorForwarding':physicalPortCapErrorForwarding,'physicalPortCapFecType':physicalPortCapFecType,'physicalPortCapFarEndCommunication':physicalPortCapFarEndCommunication,'physicalPortCapFlowControl':physicalPortCapFlowControl,'physicalPortCapForceLaserOn':physicalPortCapForceLaserOn,'physicalPortCapInhibitSwitchToProt':physicalPortCapInhibitSwitchToProt,'physicalPortCapInhibitSwitchToWork':physicalPortCapInhibitSwitchToWork,'physicalPortCapLaneChannelSetting':physicalPortCapLaneChannelSetting,'physicalPortCapLoopConfig':physicalPortCapLoopConfig,'physicalPortCapLaserDelayTimer':physicalPortCapLaserDelayTimer,'physicalPortCapLaserOffTimer':physicalPortCapLaserOffTimer,'physicalPortCapLaserOnTimer':physicalPortCapLaserOnTimer,'physicalPortCapLaserOffDelayFunction':physicalPortCapLaserOffDelayFunction,'physicalPortCapAutoPTassignment':physicalPortCapAutoPTassignment,'physicalPortCapTributarySlotMethod':physicalPortCapTributarySlotMethod,'physicalPortCapInitiateEqualization':physicalPortCapInitiateEqualization,'physicalPortCapLossAttenuation':physicalPortCapLossAttenuation,'physicalPortCapOpticalSetPoint':physicalPortCapOpticalSetPoint,'physicalPortCapDataLayerPmReset':physicalPortCapDataLayerPmReset,'physicalPortCapPrbsPmReset':physicalPortCapPrbsPmReset,'physicalPortCapTestPrbsRcvMode':physicalPortCapTestPrbsRcvMode,'physicalPortCapTestPrbsTrmtMode':physicalPortCapTestPrbsTrmtMode,'physicalPortCapSwitchCommand':physicalPortCapSwitchCommand,'physicalPortCapOpuPayloadType':physicalPortCapOpuPayloadType,'physicalPortCapSigDegThresSonetLine':physicalPortCapSigDegThresSonetLine,'physicalPortCapSigDegThresSdhMs':physicalPortCapSigDegThresSdhMs,'physicalPortCapSigDegThresOtu':physicalPortCapSigDegThresOtu,'physicalPortCapSigDegThresOdu':physicalPortCapSigDegThresOdu,'physicalPortCapSigDegThreshold':physicalPortCapSigDegThreshold,'physicalPortCapSigDegPcslThreshold':physicalPortCapSigDegPcslThreshold,'physicalPortCapSigDegThresSonetSection':physicalPortCapSigDegThresSonetSection,'physicalPortCapSigDegThresSdhSection':physicalPortCapSigDegThresSdhSection,'physicalPortCapSigDegThresOduTcmA':physicalPortCapSigDegThresOduTcmA,'physicalPortCapSigDegThresOduTcmB':physicalPortCapSigDegThresOduTcmB,'physicalPortCapSigDegThresOduTcmC':physicalPortCapSigDegThresOduTcmC,'physicalPortCapSignalDegradePeriod':physicalPortCapSignalDegradePeriod,'physicalPortCapSigDegPeriodOdu':physicalPortCapSigDegPeriodOdu,'physicalPortCapSigDegPeriodOtu':physicalPortCapSigDegPeriodOtu,'physicalPortCapSigDegPeriodIntegration':physicalPortCapSigDegPeriodIntegration,'physicalPortCapSigDegPeriodSdhSection':physicalPortCapSigDegPeriodSdhSection,'physicalPortCapSigDegPeriodOduTcmA':physicalPortCapSigDegPeriodOduTcmA,'physicalPortCapSigDegPeriodOduTcmB':physicalPortCapSigDegPeriodOduTcmB,'physicalPortCapSigDegPeriodOduTcmC':physicalPortCapSigDegPeriodOduTcmC,'physicalPortCapOtnStuffing':physicalPortCapOtnStuffing,'physicalPortCapTcmALevel':physicalPortCapTcmALevel,'physicalPortCapTcmBLevel':physicalPortCapTcmBLevel,'physicalPortCapTcmCLevel':physicalPortCapTcmCLevel,'physicalPortCapTerminationLevel':physicalPortCapTerminationLevel,'physicalPortCapTimingSource':physicalPortCapTimingSource,'physicalPortCapTimModeOdu':physicalPortCapTimModeOdu,'physicalPortCapTimModeOtu':physicalPortCapTimModeOtu,'physicalPortCapTimModeSonetSection':physicalPortCapTimModeSonetSection,'physicalPortCapTimModeOduTcmA':physicalPortCapTimModeOduTcmA,'physicalPortCapTimModeOduTcmB':physicalPortCapTimModeOduTcmB,'physicalPortCapTimModeOduTcmC':physicalPortCapTimModeOduTcmC,'physicalPortCapTraceFormSonetSection':physicalPortCapTraceFormSonetSection,'physicalPortCapTraceExpectedSonetSection':physicalPortCapTraceExpectedSonetSection,'physicalPortCapTraceTransmitSonetSection':physicalPortCapTraceTransmitSonetSection,'physicalPortCapTraceExpectedOtu':physicalPortCapTraceExpectedOtu,'physicalPortCapTraceTransmitSapiOtu':physicalPortCapTraceTransmitSapiOtu,'physicalPortCapTraceTransmitDapiOtu':physicalPortCapTraceTransmitDapiOtu,'physicalPortCapTraceTransmitOpspOtu':physicalPortCapTraceTransmitOpspOtu,'physicalPortCapTraceExpectedOdu':physicalPortCapTraceExpectedOdu,'physicalPortCapTraceTransmitSapiOdu':physicalPortCapTraceTransmitSapiOdu,'physicalPortCapTraceTransmitDapiOdu':physicalPortCapTraceTransmitDapiOdu,'physicalPortCapTraceTransmitOpspOdu':physicalPortCapTraceTransmitOpspOdu,'physicalPortCapTraceExpectedOduTcmA':physicalPortCapTraceExpectedOduTcmA,'physicalPortCapTraceTransmitSapiOduTcmA':physicalPortCapTraceTransmitSapiOduTcmA,'physicalPortCapTraceTransmitDapiOduTcmA':physicalPortCapTraceTransmitDapiOduTcmA,'physicalPortCapTraceTransmitOpspOduTcmA':physicalPortCapTraceTransmitOpspOduTcmA,'physicalPortCapTraceExpectedOduTcmB':physicalPortCapTraceExpectedOduTcmB,'physicalPortCapTraceTransmitSapiOduTcmB':physicalPortCapTraceTransmitSapiOduTcmB,'physicalPortCapTraceTransmitDapiOduTcmB':physicalPortCapTraceTransmitDapiOduTcmB,'physicalPortCapTraceTransmitOpspOduTcmB':physicalPortCapTraceTransmitOpspOduTcmB,'physicalPortCapTraceExpectedOduTcmC':physicalPortCapTraceExpectedOduTcmC,'physicalPortCapTraceTransmitSapiOduTcmC':physicalPortCapTraceTransmitSapiOduTcmC,'physicalPortCapTraceTransmitDapiOduTcmC':physicalPortCapTraceTransmitDapiOduTcmC,'physicalPortCapTraceTransmitOpspOduTcmC':physicalPortCapTraceTransmitOpspOduTcmC,'physicalPortCapTurnupConfig':physicalPortCapTurnupConfig,'physicalPortCapTxOffDelay':physicalPortCapTxOffDelay,'physicalPortCapVoaMode':physicalPortCapVoaMode,'physicalPortCapVoaSetpoint':physicalPortCapVoaSetpoint,'physicalPortCapLagPrio':physicalPortCapLagPrio,'physicalPortCapMaxFrameSize':physicalPortCapMaxFrameSize,'physicalPortCapPayload':physicalPortCapPayload,'physicalPortCapPortMode':physicalPortCapPortMode,'physicalPortCapPortRole':physicalPortCapPortRole,'physicalPortCapPriority':physicalPortCapPriority,'physicalPortCapPvid':physicalPortCapPvid,'physicalPortCapStagType':physicalPortCapStagType,'physicalPortCapUtag':physicalPortCapUtag,'physicalPortCapVethAid':physicalPortCapVethAid,'physicalPortCapRedLineState':physicalPortCapRedLineState,'physicalPortCapTunnelAid':physicalPortCapTunnelAid,'physicalPortCapRateLimit':physicalPortCapRateLimit,'physicalPortCapTxOffOnTm':physicalPortCapTxOffOnTm,'physicalPortCapTxOffTimer':physicalPortCapTxOffTimer,'physicalPortCapTxOnTimer':physicalPortCapTxOnTimer,'virtualPortCapTable':virtualPortCapTable,'virtualPortCapEntry':virtualPortCapEntry,_A_:virtualPortCapRowStatus,_B0:virtualPortCapChannelBand,_B1:virtualPortCapType,_B2:virtualPortCapAlias,_B3:virtualPortCapAdmin,_B4:virtualPortCapEqlzAdmin,_B5:virtualPortCapInitEqlz,'virtualPortCapLacpMode':virtualPortCapLacpMode,'virtualPortCapLacpTimeout':virtualPortCapLacpTimeout,'virtualPortCapLagActivePorts':virtualPortCapLagActivePorts,'virtualPortCapMaxFrameSize':virtualPortCapMaxFrameSize,'virtualPortCapPortMode':virtualPortCapPortMode,'virtualPortCapDataLayerPmReset':virtualPortCapDataLayerPmReset,'virtualPortCapPortRole':virtualPortCapPortRole,'virtualPortCapLagPortType':virtualPortCapLagPortType,'virtualPortCapPriority':virtualPortCapPriority,'virtualPortCapPvid':virtualPortCapPvid,'virtualPortCapRevertiveMode':virtualPortCapRevertiveMode,'virtualPortCapStagType':virtualPortCapStagType,'virtualPortCapUtag':virtualPortCapUtag,'virtualPortCapBundle':virtualPortCapBundle,'virtualPortCapSwitchCommand':virtualPortCapSwitchCommand,'virtualPortCapInhibitSwitchToWork':virtualPortCapInhibitSwitchToWork,'virtualPortCapInhibitSwitchToProt':virtualPortCapInhibitSwitchToProt,'virtualPortCapOduTribPortNo':virtualPortCapOduTribPortNo,'virtualPortCapOduTribTimeSlottNo':virtualPortCapOduTribTimeSlottNo,'virtualPortCapSigDegThresOdu':virtualPortCapSigDegThresOdu,'virtualPortCapSigDegPeriodOdu':virtualPortCapSigDegPeriodOdu,'virtualPortCapTraceExpectedOdu':virtualPortCapTraceExpectedOdu,'virtualPortCapTraceTransmitSapiOdu':virtualPortCapTraceTransmitSapiOdu,'virtualPortCapTraceTransmitDapiOdu':virtualPortCapTraceTransmitDapiOdu,'virtualPortCapTraceTransmitOpspOdu':virtualPortCapTraceTransmitOpspOdu,'virtualPortCapTimModeOdu':virtualPortCapTimModeOdu,'virtualPortCapSigDegThresOduTcmA':virtualPortCapSigDegThresOduTcmA,'virtualPortCapSigDegPeriodOduTcmA':virtualPortCapSigDegPeriodOduTcmA,'virtualPortCapSigDegThresOduTcmB':virtualPortCapSigDegThresOduTcmB,'virtualPortCapSigDegPeriodOduTcmB':virtualPortCapSigDegPeriodOduTcmB,'virtualPortCapSigDegThresOduTcmC':virtualPortCapSigDegThresOduTcmC,'virtualPortCapSigDegPeriodOduTcmC':virtualPortCapSigDegPeriodOduTcmC,'virtualPortCapTcmALevel':virtualPortCapTcmALevel,'virtualPortCapTcmBLevel':virtualPortCapTcmBLevel,'virtualPortCapTcmCLevel':virtualPortCapTcmCLevel,'virtualPortCapTraceTransmitSapiOduTcmA':virtualPortCapTraceTransmitSapiOduTcmA,'virtualPortCapTraceTransmitDapiOduTcmA':virtualPortCapTraceTransmitDapiOduTcmA,'virtualPortCapTraceTransmitOpspOduTcmA':virtualPortCapTraceTransmitOpspOduTcmA,'virtualPortCapTraceExpectedOduTcmA':virtualPortCapTraceExpectedOduTcmA,'virtualPortCapTimModeOduTcmA':virtualPortCapTimModeOduTcmA,'virtualPortCapTraceExpectedOduTcmB':virtualPortCapTraceExpectedOduTcmB,'virtualPortCapTraceTransmitSapiOduTcmB':virtualPortCapTraceTransmitSapiOduTcmB,'virtualPortCapTraceTransmitDapiOduTcmB':virtualPortCapTraceTransmitDapiOduTcmB,'virtualPortCapTraceTransmitOpspOduTcmB':virtualPortCapTraceTransmitOpspOduTcmB,'virtualPortCapTimModeOduTcmB':virtualPortCapTimModeOduTcmB,'virtualPortCapTraceExpectedOduTcmC':virtualPortCapTraceExpectedOduTcmC,'virtualPortCapTraceTransmitSapiOduTcmC':virtualPortCapTraceTransmitSapiOduTcmC,'virtualPortCapTraceTransmitDapiOduTcmC':virtualPortCapTraceTransmitDapiOduTcmC,'virtualPortCapTraceTransmitOpspOduTcmC':virtualPortCapTraceTransmitOpspOduTcmC,'virtualPortCapTimModeOduTcmC':virtualPortCapTimModeOduTcmC,'virtualPortCapTerminationLevel':virtualPortCapTerminationLevel,'virtualPortCapLoopConfig':virtualPortCapLoopConfig,'virtualPortCapVcType':virtualPortCapVcType,'virtualPortCapCir':virtualPortCapCir,'virtualPortCapOpuPayloadType':virtualPortCapOpuPayloadType,'virtualPortCapOtnStuffing':virtualPortCapOtnStuffing,'virtualPortCapRedLineState':virtualPortCapRedLineState,'virtualPortCapTunnelAid':virtualPortCapTunnelAid,'virtualPortCapTrafficDirection':virtualPortCapTrafficDirection,'virtualPortCapChannelId':virtualPortCapChannelId,'endOfVirtualPortCapTable':endOfVirtualPortCapTable,'endOfFacilityMgmtCap':endOfFacilityMgmtCap,'dcnMgmtCap':dcnMgmtCap,'linkCapTable':linkCapTable,'linkCapEntry':linkCapEntry,'linkCapRowStatus':linkCapRowStatus,'linkCapType':linkCapType,'linkCapAdmin':linkCapAdmin,'linkCapAlias':linkCapAlias,'linkCapAuthString':linkCapAuthString,'linkCapProxyArp':linkCapProxyArp,'linkCapOspf':linkCapOspf,'linkCapBaud':linkCapBaud,'linkCapAuthType':linkCapAuthType,'linkCapIpType':linkCapIpType,'linkCapMetric':linkCapMetric,'linkCapAreaAid':linkCapAreaAid,'linkCapNearEndIp':linkCapNearEndIp,'linkCapBitrate':linkCapBitrate,'linkCapIPv6Type':linkCapIPv6Type,'linkCapNendIPv6':linkCapNendIPv6,'endOfLinkCapTable':endOfLinkCapTable,'scCapTable':scCapTable,'scCapEntry':scCapEntry,'scCapRowStatus':scCapRowStatus,'scCapType':scCapType,'scCapAdmin':scCapAdmin,'scCapAlias':scCapAlias,'scCapAuthString':scCapAuthString,'scCapOspf':scCapOspf,'scCapAuthType':scCapAuthType,'scCapIpType':scCapIpType,'scCapMetric':scCapMetric,'scCapAreaAid':scCapAreaAid,'scCapAlsMode':scCapAlsMode,'scCapSigDegThresReceiver':scCapSigDegThresReceiver,'scCapAutonegotiation':scCapAutonegotiation,'scCapBitrate':scCapBitrate,'scCapDuplex':scCapDuplex,'scCapAttGradientTh':scCapAttGradientTh,'scCapIpAddr':scCapIpAddr,'scCapLanAid':scCapLanAid,'scCapIpMask':scCapIpMask,'scCapDataLayerPmReset':scCapDataLayerPmReset,'scCapPriority':scCapPriority,'scCapIPv6':scCapIPv6,'scCapIPv6PrefixLen':scCapIPv6PrefixLen,'scCapIpMode':scCapIpMode,'scCapGatewayProxyArp':scCapGatewayProxyArp,'endOfScCapTable':endOfScCapTable,'lanCapTable':lanCapTable,'lanCapEntry':lanCapEntry,'lanCapRowStatus':lanCapRowStatus,'lanCapType':lanCapType,'lanCapAdmin':lanCapAdmin,'lanCapAlias':lanCapAlias,'lanCapAuthString':lanCapAuthString,'lanCapOspf':lanCapOspf,'lanCapAuthType':lanCapAuthType,'lanCapIpType':lanCapIpType,'lanCapMetric':lanCapMetric,'lanCapAreaAid':lanCapAreaAid,'lanCapIpAddr':lanCapIpAddr,'lanCapIpMask':lanCapIpMask,'lanCapPriority':lanCapPriority,'lanCapIPv6':lanCapIPv6,'lanCapIPv6PrefixLen':lanCapIPv6PrefixLen,'lanCapIpMode':lanCapIpMode,'endOfLanCapTable':endOfLanCapTable,'eccCapTable':eccCapTable,'eccCapEntry':eccCapEntry,'eccCapRowStatus':eccCapRowStatus,'eccCapType':eccCapType,'eccCapAdmin':eccCapAdmin,'eccCapAlias':eccCapAlias,'eccCapLanAid':eccCapLanAid,'eccCapExternalVid':eccCapExternalVid,'endOfEccCapTable':endOfEccCapTable,'endOfDcnMgmtCap':endOfDcnMgmtCap,'opticalMuxMgmtCap':opticalMuxMgmtCap,'opticalMuxCapTable':opticalMuxCapTable,'opticalMuxCapEntry':opticalMuxCapEntry,'opticalMuxCapRowStatus':opticalMuxCapRowStatus,'opticalMuxCapPumpPower':opticalMuxCapPumpPower,'opticalMuxCapInhibitSwitchToWork':opticalMuxCapInhibitSwitchToWork,'opticalMuxCapForceLaserOn':opticalMuxCapForceLaserOn,'opticalMuxCapAseTabCreation':opticalMuxCapAseTabCreation,'opticalMuxCapOpticalSetPoint':opticalMuxCapOpticalSetPoint,'opticalMuxCapInitiateEqualization':opticalMuxCapInitiateEqualization,'opticalMuxCapTilt':opticalMuxCapTilt,'opticalMuxCapOscOpticalSetpoint':opticalMuxCapOscOpticalSetpoint,'opticalMuxCapOffset':opticalMuxCapOffset,'opticalMuxCapSwitchCommand':opticalMuxCapSwitchCommand,'opticalMuxCapAlsMode':opticalMuxCapAlsMode,'opticalMuxCapType':opticalMuxCapType,'opticalMuxCapAttenuationGradient':opticalMuxCapAttenuationGradient,'opticalMuxCapInhibitSwitchToProt':opticalMuxCapInhibitSwitchToProt,'opticalMuxCapVariableGain':opticalMuxCapVariableGain,'opticalMuxCapAdmin':opticalMuxCapAdmin,'opticalMuxCapTimePeriod':opticalMuxCapTimePeriod,'opticalMuxCapSigDegThresReceiver':opticalMuxCapSigDegThresReceiver,'opticalMuxCapAlias':opticalMuxCapAlias,'opticalMuxCapDataLayerPmReset':opticalMuxCapDataLayerPmReset,'opticalMuxCapGain':opticalMuxCapGain,'opticalMuxCapEdfaPwrOut':opticalMuxCapEdfaPwrOut,'opticalMuxCapVoaSetpoint':opticalMuxCapVoaSetpoint,'opticalMuxCapFiberBrand':opticalMuxCapFiberBrand,'opticalMuxCapTiltSet':opticalMuxCapTiltSet,'opticalMuxCapForceFwdAsePilotOn':opticalMuxCapForceFwdAsePilotOn,'opticalMuxCapBandProvision':opticalMuxCapBandProvision,'opticalMuxCapOffsetHigh':opticalMuxCapOffsetHigh,'opticalMuxCapOffsetLow':opticalMuxCapOffsetLow,'opticalMuxCapOptUpdate':opticalMuxCapOptUpdate,'endOfOpticalMuxCapTable':endOfOpticalMuxCapTable,'endOfOpticalMuxMgmtCap':endOfOpticalMuxMgmtCap,'shelfConnMgmtCap':shelfConnMgmtCap,'shelfConnCapTable':shelfConnCapTable,'shelfConnCapEntry':shelfConnCapEntry,'shelfConnCapRowStatus':shelfConnCapRowStatus,'shelfConnCapAdmin':shelfConnCapAdmin,'shelfConnCapAlias':shelfConnCapAlias,'shelfConnCapFacilityType':shelfConnCapFacilityType,'endOfShelfConnCapTable':endOfShelfConnCapTable,'endOfShelfConnMgmtCap':endOfShelfConnMgmtCap,'envMgmtCap':envMgmtCap,'envPortCapTable':envPortCapTable,'envPortCapEntry':envPortCapEntry,'envPortCapRowStatus':envPortCapRowStatus,'envPortCapTelemetry':envPortCapTelemetry,'envPortCapFacilityType':envPortCapFacilityType,'envPortCapTifAlarmType':envPortCapTifAlarmType,'envPortCapTifAlarmMessage':envPortCapTifAlarmMessage,'envPortCapInvertTifInputLogic':envPortCapInvertTifInputLogic,'endOfEnvPortCapTable':endOfEnvPortCapTable,'endOfEnvMgmtCap':endOfEnvMgmtCap,'containerMgmtCap':containerMgmtCap,'containerCapTable':containerCapTable,'containerCapEntry':containerCapEntry,'containerCapRowStatus':containerCapRowStatus,'containerCapFacilityType':containerCapFacilityType,'endOfContainerCapTable':endOfContainerCapTable,'endOfContainerMgmtCap':endOfContainerMgmtCap,'opticalLineMgmtCap':opticalLineMgmtCap,'opticalLineCapTable':opticalLineCapTable,'opticalLineCapEntry':opticalLineCapEntry,'opticalLineCapRowStatus':opticalLineCapRowStatus,'opticalLineCapTxLineAttenuation':opticalLineCapTxLineAttenuation,'opticalLineCapRxLineAttenuation':opticalLineCapRxLineAttenuation,'opticalLineCapAlias':opticalLineCapAlias,'opticalLineCapFarEndLocation':opticalLineCapFarEndLocation,'endOfOpticalLineCapTable':endOfOpticalLineCapTable,'endOfOpticalLineMgmtCap':endOfOpticalLineMgmtCap,'endOfManagementCap':endOfManagementCap,'performanceCap':performanceCap,'performanceFacilityCap':performanceFacilityCap,'performanceFacilityThresholdCap':performanceFacilityThresholdCap,'optThresholdConfigCapTable':optThresholdConfigCapTable,'optThresholdConfigCapEntry':optThresholdConfigCapEntry,_B6:optThresholdConfigCapLowConfig,_B7:optThresholdConfigCapHighConfig,'oprThresholdConfigCapTable':oprThresholdConfigCapTable,'oprThresholdConfigCapEntry':oprThresholdConfigCapEntry,_B8:oprThresholdConfigCapLowConfig,_B9:oprThresholdConfigCapHighConfig,'endOfOprThresholdConfigCapTable':endOfOprThresholdConfigCapTable,'endOfPerformanceFacilityThresholdCap':endOfPerformanceFacilityThresholdCap,'endOfPerformanceFacilityCap':endOfPerformanceFacilityCap,'pmEqptCap':pmEqptCap,'pmDcnCap':pmDcnCap,'pmDcnDataCap':pmDcnDataCap,'pmDcnPhysicalCap':pmDcnPhysicalCap,'pmDcnPhysThresholdCap':pmDcnPhysThresholdCap,'dcnPhysThresholdCapTable':dcnPhysThresholdCapTable,'dcnPhysThresholdCapEntry':dcnPhysThresholdCapEntry,'dcnPhysThresholdCapOprLow':dcnPhysThresholdCapOprLow,'dcnPhysThresholdCapOprHigh':dcnPhysThresholdCapOprHigh,'dcnPhysThresholdCapAttRcvLow':dcnPhysThresholdCapAttRcvLow,'dcnPhysThresholdCapAttRcvHigh':dcnPhysThresholdCapAttRcvHigh,'endOfDcnPhysThresholdCapTable':endOfDcnPhysThresholdCapTable,'endOfPmDcnPhysThresholdCap':endOfPmDcnPhysThresholdCap,'endOfPmDcnPhysicalCap':endOfPmDcnPhysicalCap,'endOfPmDcnCap':endOfPmDcnCap,'pmFacilityCap':pmFacilityCap,'pmFacilityDataCap':pmFacilityDataCap,'pmFacilityDataThresholdCap':pmFacilityDataThresholdCap,'oduFacilityDataThresholdCapTable':oduFacilityDataThresholdCapTable,'oduFacilityDataThresholdCapEntry':oduFacilityDataThresholdCapEntry,'oduFacilityDataThresholdCapESHighThres15min':oduFacilityDataThresholdCapESHighThres15min,'oduFacilityDataThresholdCapESHighThres1day':oduFacilityDataThresholdCapESHighThres1day,'oduFacilityDataThresholdCapSESHighThres15min':oduFacilityDataThresholdCapSESHighThres15min,'oduFacilityDataThresholdCapSESHighThres1day':oduFacilityDataThresholdCapSESHighThres1day,'oduFacilityDataThresholdCapBbeHighThres15min':oduFacilityDataThresholdCapBbeHighThres15min,'oduFacilityDataThresholdCapBbeHighThres1day':oduFacilityDataThresholdCapBbeHighThres1day,'oduFacilityDataThresholdCapUASHighThres15min':oduFacilityDataThresholdCapUASHighThres15min,'oduFacilityDataThresholdCapUASHighThres1day':oduFacilityDataThresholdCapUASHighThres1day,'endOfOduFacilityDataThresholdCapTable':endOfOduFacilityDataThresholdCapTable,'tcmAFacilityDataThresholdCapTable':tcmAFacilityDataThresholdCapTable,'tcmAFacilityDataThresholdCapEntry':tcmAFacilityDataThresholdCapEntry,'tcmAFacilityDataThresholdCapESHighThres15min':tcmAFacilityDataThresholdCapESHighThres15min,'tcmAFacilityDataThresholdCapESHighThres1day':tcmAFacilityDataThresholdCapESHighThres1day,'tcmAFacilityDataThresholdCapSESHighThres15min':tcmAFacilityDataThresholdCapSESHighThres15min,'tcmAFacilityDataThresholdCapSESHighThres1day':tcmAFacilityDataThresholdCapSESHighThres1day,'tcmAFacilityDataThresholdCapBbeHighThres15min':tcmAFacilityDataThresholdCapBbeHighThres15min,'tcmAFacilityDataThresholdCapBbeHighThres1day':tcmAFacilityDataThresholdCapBbeHighThres1day,'tcmAFacilityDataThresholdCapUASHighThres15min':tcmAFacilityDataThresholdCapUASHighThres15min,'tcmAFacilityDataThresholdCapUASHighThres1day':tcmAFacilityDataThresholdCapUASHighThres1day,'endOfTcmAFacilityDataThresholdCapTable':endOfTcmAFacilityDataThresholdCapTable,'tcmBFacilityDataThresholdCapTable':tcmBFacilityDataThresholdCapTable,'tcmBFacilityDataThresholdCapEntry':tcmBFacilityDataThresholdCapEntry,'tcmBFacilityDataThresholdCapBESHighThres15min':tcmBFacilityDataThresholdCapBESHighThres15min,'tcmBFacilityDataThresholdCapESHighThres1day':tcmBFacilityDataThresholdCapESHighThres1day,'tcmBFacilityDataThresholdCapSESHighThres15min':tcmBFacilityDataThresholdCapSESHighThres15min,'tcmBFacilityDataThresholdCapSESHighThres1day':tcmBFacilityDataThresholdCapSESHighThres1day,'tcmBFacilityDataThresholdCapOduTcmBBbeHighThres15min':tcmBFacilityDataThresholdCapOduTcmBBbeHighThres15min,'tcmBFacilityDataThresholdCapOduTcmBBbeHighThres1day':tcmBFacilityDataThresholdCapOduTcmBBbeHighThres1day,'tcmBFacilityDataThresholdCapUASHighThres15min':tcmBFacilityDataThresholdCapUASHighThres15min,'tcmBFacilityDataThresholdCapUASHighThres1day':tcmBFacilityDataThresholdCapUASHighThres1day,'endOfTcmBFacilityDataThresholdCapTable':endOfTcmBFacilityDataThresholdCapTable,'tcmCFacilityDataThresholdCapTable':tcmCFacilityDataThresholdCapTable,'tcmCFacilityDataThresholdCapEntry':tcmCFacilityDataThresholdCapEntry,'tcmCFacilityDataThresholdCapBESHighThres15min':tcmCFacilityDataThresholdCapBESHighThres15min,'tcmCFacilityDataThresholdCapESHighThres1day':tcmCFacilityDataThresholdCapESHighThres1day,'tcmCFacilityDataThresholdCapSESHighThres15min':tcmCFacilityDataThresholdCapSESHighThres15min,'tcmCFacilityDataThresholdCapSESHighThres1day':tcmCFacilityDataThresholdCapSESHighThres1day,'tcmCFacilityDataThresholdCapOduTcmCBbeHighThres15min':tcmCFacilityDataThresholdCapOduTcmCBbeHighThres15min,'tcmCFacilityDataThresholdCapOduTcmCBbeHighThres1day':tcmCFacilityDataThresholdCapOduTcmCBbeHighThres1day,'tcmCFacilityDataThresholdCapUASHighThres15min':tcmCFacilityDataThresholdCapUASHighThres15min,'tcmCFacilityDataThresholdCapUASHighThres1day':tcmCFacilityDataThresholdCapUASHighThres1day,'endOfTcmCFacilityDataThresholdCapTable':endOfTcmCFacilityDataThresholdCapTable,'otuFacilityDataThresholdCapTable':otuFacilityDataThresholdCapTable,'otuFacilityDataThresholdCapEntry':otuFacilityDataThresholdCapEntry,'otuFacilityDataThresholdCapESHighThres15min':otuFacilityDataThresholdCapESHighThres15min,'otuFacilityDataThresholdCapESHighThres1day':otuFacilityDataThresholdCapESHighThres1day,'otuFacilityDataThresholdCapSESHighThres15min':otuFacilityDataThresholdCapSESHighThres15min,'otuFacilityDataThresholdCapSESHighThres1day':otuFacilityDataThresholdCapSESHighThres1day,'otuFacilityDataThresholdCapBbeHighThres15min':otuFacilityDataThresholdCapBbeHighThres15min,'otuFacilityDataThresholdCapBbeHighThres1day':otuFacilityDataThresholdCapBbeHighThres1day,'otuFacilityDataThresholdCapUASHighThres15min':otuFacilityDataThresholdCapUASHighThres15min,'otuFacilityDataThresholdCapUASHighThres1day':otuFacilityDataThresholdCapUASHighThres1day,'endOfOtuFacilityDataThresholdCapTable':endOfOtuFacilityDataThresholdCapTable,'otuFecFacilityDataThresholdCapTable':otuFecFacilityDataThresholdCapTable,'otuFecFacilityDataThresholdCapEntry':otuFecFacilityDataThresholdCapEntry,'otuFecFacilityDataThresholdCapESHighThres15min':otuFecFacilityDataThresholdCapESHighThres15min,'otuFecFacilityDataThresholdCapESHighThres1day':otuFecFacilityDataThresholdCapESHighThres1day,'otuFecFacilityDataThresholdCapSESHighThres15min':otuFecFacilityDataThresholdCapSESHighThres15min,'otuFecFacilityDataThresholdCapSESHighThres1day':otuFecFacilityDataThresholdCapSESHighThres1day,'otuFecFacilityDataThresholdCapUBEHighThres15min':otuFecFacilityDataThresholdCapUBEHighThres15min,'otuFecFacilityDataThresholdCapUBEHighThres1day':otuFecFacilityDataThresholdCapUBEHighThres1day,'otuFecFacilityDataThresholdCapCErrHighThres15min':otuFecFacilityDataThresholdCapCErrHighThres15min,'otuFecFacilityDataThresholdCapCErrHighThres1day':otuFecFacilityDataThresholdCapCErrHighThres1day,'otuFecFacilityDataThresholdCapBERCErrHighThres15min':otuFecFacilityDataThresholdCapBERCErrHighThres15min,'otuFecFacilityDataThresholdCapBERCErrHighThres1day':otuFecFacilityDataThresholdCapBERCErrHighThres1day,'endOfOtuFecFacilityDataThresholdCapTable':endOfOtuFecFacilityDataThresholdCapTable,'fecFacilityDataThresholdCapTable':fecFacilityDataThresholdCapTable,'fecFacilityDataThresholdCapEntry':fecFacilityDataThresholdCapEntry,'fecFacilityDataThresholdCapCEHighThres15min':fecFacilityDataThresholdCapCEHighThres15min,'fecFacilityDataThresholdCapCEHighThres1day':fecFacilityDataThresholdCapCEHighThres1day,'fecFacilityDataThresholdCapUBEHighThres15min':fecFacilityDataThresholdCapUBEHighThres15min,'fecFacilityDataThresholdCapUBEHighThres1day':fecFacilityDataThresholdCapUBEHighThres1day,'endOfFecFacilityDataThresholdCapTable':endOfFecFacilityDataThresholdCapTable,'pcs2FacilityDataThresholdCapTable':pcs2FacilityDataThresholdCapTable,'pcs2FacilityDataThresholdCapEntry':pcs2FacilityDataThresholdCapEntry,'pcs2FacilityDataThresholdCapESHighThres15min':pcs2FacilityDataThresholdCapESHighThres15min,'pcs2FacilityDataThresholdCapESHighThres1day':pcs2FacilityDataThresholdCapESHighThres1day,'pcs2FacilityDataThresholdCapDEHighThres15min':pcs2FacilityDataThresholdCapDEHighThres15min,'pcs2FacilityDataThresholdCapDEHighThres1day':pcs2FacilityDataThresholdCapDEHighThres1day,'pcs2FacilityDataThresholdCapCVHighThres15min':pcs2FacilityDataThresholdCapCVHighThres15min,'pcs2FacilityDataThresholdCapCVHighThres1day':pcs2FacilityDataThresholdCapCVHighThres1day,'endOfPcs2FacilityDataThresholdCapTable':endOfPcs2FacilityDataThresholdCapTable,'lFacilityDataThresholdCapTable':lFacilityDataThresholdCapTable,'lFacilityDataThresholdCapEntry':lFacilityDataThresholdCapEntry,'lFacilityDataThresholdCapESHighThres15min':lFacilityDataThresholdCapESHighThres15min,'lFacilityDataThresholdCapESHighThres1day':lFacilityDataThresholdCapESHighThres1day,'lFacilityDataThresholdCapSESHighThres15min':lFacilityDataThresholdCapSESHighThres15min,'lFacilityDataThresholdCapSESHighThres1day':lFacilityDataThresholdCapSESHighThres1day,'lFacilityDataThresholdCapUASHighThres15min':lFacilityDataThresholdCapUASHighThres15min,'lFacilityDataThresholdCapUASSHighThres1day':lFacilityDataThresholdCapUASSHighThres1day,'lFacilityDataThresholdCapCVHighThres15min':lFacilityDataThresholdCapCVHighThres15min,'lFacilityDataThresholdCapCVSHighThres1day':lFacilityDataThresholdCapCVSHighThres1day,'endOfLFacilityDataThresholdCapTable':endOfLFacilityDataThresholdCapTable,'sFacilityDataThresholdCapTable':sFacilityDataThresholdCapTable,'sFacilityDataThresholdCapEntry':sFacilityDataThresholdCapEntry,'sFacilityDataThresholdCapESHighThres15min':sFacilityDataThresholdCapESHighThres15min,'sFacilityDataThresholdCapESHighThres1day':sFacilityDataThresholdCapESHighThres1day,'sFacilityDataThresholdCapSESHighThres15min':sFacilityDataThresholdCapSESHighThres15min,'sFacilityDataThresholdCapSESHighThres1day':sFacilityDataThresholdCapSESHighThres1day,'sFacilityDataThresholdCapSEFSHighThres15min':sFacilityDataThresholdCapSEFSHighThres15min,'sFacilityDataThresholdCapSEFSHighThres1day':sFacilityDataThresholdCapSEFSHighThres1day,'sFacilityDataThresholdCapCVHighThres15min':sFacilityDataThresholdCapCVHighThres15min,'sFacilityDataThresholdCapCVHighThres1day':sFacilityDataThresholdCapCVHighThres1day,'endOfSFacilityDataThresholdCapTable':endOfSFacilityDataThresholdCapTable,'endOfPmFacilityDataThresholdCap':endOfPmFacilityDataThresholdCap,'endOfPmFacilityDataCap':endOfPmFacilityDataCap,'pmFacilityPhysicalCap':pmFacilityPhysicalCap,'pmFacilityPhysValueCap':pmFacilityPhysValueCap,'pmFacilityPhysThresholdCap':pmFacilityPhysThresholdCap,'facilityPhysThresholdCapTable':facilityPhysThresholdCapTable,'facilityPhysThresholdCapEntry':facilityPhysThresholdCapEntry,'facilityPhysThresholdCapOpticalInputPwrLow':facilityPhysThresholdCapOpticalInputPwrLow,'facilityPhysThresholdCapOpticalInputPwrHigh':facilityPhysThresholdCapOpticalInputPwrHigh,'facilityPhysThresholdCapConfigurableOpticalOutputPwrLow':facilityPhysThresholdCapConfigurableOpticalOutputPwrLow,'facilityPhysThresholdCapConfigurableOpticalOutputPwrHigh':facilityPhysThresholdCapConfigurableOpticalOutputPwrHigh,'facilityPhysThresholdCapRoundTripDelayLowThres':facilityPhysThresholdCapRoundTripDelayLowThres,'facilityPhysThresholdCapRoundTripDelayHighThres':facilityPhysThresholdCapRoundTripDelayHighThres,'facilityPhysThresholdCapLatencyLowThres':facilityPhysThresholdCapLatencyLowThres,'facilityPhysThresholdCapLatencyHighThres':facilityPhysThresholdCapLatencyHighThres,'facilityPhysThresholdCapChromaticDispersionHigh':facilityPhysThresholdCapChromaticDispersionHigh,'facilityPhysThresholdCapChromaticDispersionLow':facilityPhysThresholdCapChromaticDispersionLow,'facilityPhysThresholdCapCarrierFreqOffsetLow':facilityPhysThresholdCapCarrierFreqOffsetLow,'facilityPhysThresholdCapCarrierFreqOffsetHigh':facilityPhysThresholdCapCarrierFreqOffsetHigh,'facilityPhysThresholdCapLogicalLanesSkewHigh':facilityPhysThresholdCapLogicalLanesSkewHigh,'facilityPhysThresholdCapDispersionCompensationLowThres':facilityPhysThresholdCapDispersionCompensationLowThres,'facilityPhysThresholdCapDispersionCompensationHighThres':facilityPhysThresholdCapDispersionCompensationHighThres,'facilityPhysThresholdCapSignalToNoiseRatioLow':facilityPhysThresholdCapSignalToNoiseRatioLow,'facilityPhysThresholdCapDifferentialGroupDelayHigh':facilityPhysThresholdCapDifferentialGroupDelayHigh,'endOfFacilityPhysThresholdCapTable':endOfFacilityPhysThresholdCapTable,'endOfPmFacilityPhysThresholdCap':endOfPmFacilityPhysThresholdCap,'endOfPmFacilityPhysicalCap':endOfPmFacilityPhysicalCap,'endOfPmFacilityCap':endOfPmFacilityCap,'pmTerminPointCap':pmTerminPointCap,'pmOptMuxCap':pmOptMuxCap,'pmOptMuxDataCap':pmOptMuxDataCap,'pmOptMuxPhysicalCap':pmOptMuxPhysicalCap,'pmOptMuxPhysValueCap':pmOptMuxPhysValueCap,'pmOptMuxPhysThresholdCap':pmOptMuxPhysThresholdCap,'optMuxPhysThresholdCapTable':optMuxPhysThresholdCapTable,'optMuxPhysThresholdCapEntry':optMuxPhysThresholdCapEntry,'optMuxPhysThresholdCapBrtxHighConfig':optMuxPhysThresholdCapBrtxHighConfig,'optMuxPhysThresholdCapBrPwrReceivedHighThres':optMuxPhysThresholdCapBrPwrReceivedHighThres,'optMuxPhysThresholdCapConfigurableOpticalOutputPwrHigh':optMuxPhysThresholdCapConfigurableOpticalOutputPwrHigh,'optMuxPhysThresholdCapConfigurableOpticalOutputPwrLow':optMuxPhysThresholdCapConfigurableOpticalOutputPwrLow,'optMuxPhysThresholdCapOscPwrRcvHighThres':optMuxPhysThresholdCapOscPwrRcvHighThres,'optMuxPhysThresholdCapOscPwrRcvLowThres':optMuxPhysThresholdCapOscPwrRcvLowThres,'optMuxPhysThresholdCapOpticalInputPwrHigh':optMuxPhysThresholdCapOpticalInputPwrHigh,'optMuxPhysThresholdCapOpticalInputPwrLow':optMuxPhysThresholdCapOpticalInputPwrLow,'optMuxPhysThresholdCapAttRxHigh':optMuxPhysThresholdCapAttRxHigh,'optMuxPhysThresholdCapAttRxLow':optMuxPhysThresholdCapAttRxLow,'optMuxPhysThresholdCapAttTxHigh':optMuxPhysThresholdCapAttTxHigh,'optMuxPhysThresholdCapAttTxLow':optMuxPhysThresholdCapAttTxLow,'endOfOptMuxPhysThresholdCapTable':endOfOptMuxPhysThresholdCapTable,'endOfPmOptMuxPhysThresholdCap':endOfPmOptMuxPhysThresholdCap,'featureSpecificCap':featureSpecificCap,'fiberMapCap':fiberMapCap,'terminationPointCapTable':terminationPointCapTable,'terminationPointCapEntry':terminationPointCapEntry,_BA:terminationPointCapRowStatus,_BB:terminationPointCapAdmin,_BC:terminationPointCapFiberDetect,_BD:terminationPointCapAlias,'connectionCapTable':connectionCapTable,'connectionCapEntry':connectionCapEntry,_BE:connectionCapRowStatus,_BF:connectionCapType,'endOfConnectionCapTable':endOfConnectionCapTable,'endOfFiberMapCap':endOfFiberMapCap,'eciCap':eciCap,'externalPortCapTable':externalPortCapTable,'externalPortCapEntry':externalPortCapEntry,_BG:externalPortCapRowStatus,_BH:externalPortCapType,_BI:externalPortCapTransmitChannel,_BJ:externalPortCapChannelBandwith,_BK:externalPortCapAlias,_BL:externalPortCapFarEndLocation,_BM:externalPortCapBitrate,_BQ:externalPortCapFecType,_BR:externalPortCapLineCoding,_BS:externalPortCapFrameFormat,_BT:externalPortCapOpticalPowerTx,_BU:externalPortCapOsnrTransmit,_BV:externalPortCapPmdTransmit,_BW:externalPortCapChromDisperTx,_BX:externalPortCapMinOsnrRcv,_BY:externalPortCapMinOptPowerRcv,_BZ:externalPortCapMaxOptPowerRcv,_Ba:externalPortCapMaxPmdRcv,_Bb:externalPortCapMinChromDisperRcv,_BN:externalPortCapMaxChromDisperRcv,_BO:externalPortCapMaxBitErrorRate,_BP:externalPortCapSourceProfile,'endOfExternalPortCapTable':endOfExternalPortCapTable,'endOfEciCap':endOfEciCap,'changeServiceCap':changeServiceCap,'changePhysicalPortServiceCapTable':changePhysicalPortServiceCapTable,'changePhysicalPortServiceCapEntry':changePhysicalPortServiceCapEntry,'changePhysicalPortServiceCapRowStatus':changePhysicalPortServiceCapRowStatus,'changePhysicalPortServiceCapType':changePhysicalPortServiceCapType,'changePhysicalPortServiceCapAdmin':changePhysicalPortServiceCapAdmin,'changePhysicalPortServiceCapAlias':changePhysicalPortServiceCapAlias,'changePhysicalPortServiceCapAlsMode':changePhysicalPortServiceCapAlsMode,'changePhysicalPortServiceCapBehaviour':changePhysicalPortServiceCapBehaviour,'changePhysicalPortServiceCapDispersionSetting':changePhysicalPortServiceCapDispersionSetting,'changePhysicalPortServiceCapDispersionMode':changePhysicalPortServiceCapDispersionMode,'changePhysicalPortServiceCapChannelProv':changePhysicalPortServiceCapChannelProv,'changePhysicalPortServiceCapWdmRxChannel':changePhysicalPortServiceCapWdmRxChannel,'changePhysicalPortServiceCapCodeGain':changePhysicalPortServiceCapCodeGain,'changePhysicalPortServiceCapXfpDecisionThres':changePhysicalPortServiceCapXfpDecisionThres,'changePhysicalPortServiceCapDisparityCorrection':changePhysicalPortServiceCapDisparityCorrection,'changePhysicalPortServiceCapEqlzAdmin':changePhysicalPortServiceCapEqlzAdmin,'changePhysicalPortServiceCapErrorForwarding':changePhysicalPortServiceCapErrorForwarding,'changePhysicalPortServiceCapFecType':changePhysicalPortServiceCapFecType,'changePhysicalPortServiceCapFarEndCommunication':changePhysicalPortServiceCapFarEndCommunication,'changePhysicalPortServiceCapFlowControl':changePhysicalPortServiceCapFlowControl,'changePhysicalPortServiceCapLaneChannelSetting':changePhysicalPortServiceCapLaneChannelSetting,'changePhysicalPortServiceCapLaserDelayTimer':changePhysicalPortServiceCapLaserDelayTimer,'changePhysicalPortServiceCapLaserOffTimer':changePhysicalPortServiceCapLaserOffTimer,'changePhysicalPortServiceCapLaserOnTimer':changePhysicalPortServiceCapLaserOnTimer,'changePhysicalPortServiceCapLaserOffDelayFunction':changePhysicalPortServiceCapLaserOffDelayFunction,'changePhysicalPortServiceCapAutoPTassignment':changePhysicalPortServiceCapAutoPTassignment,'changePhysicalPortServiceCapTributarySlotMethod':changePhysicalPortServiceCapTributarySlotMethod,'changePhysicalPortServiceCapOpticalSetPoint':changePhysicalPortServiceCapOpticalSetPoint,'changePhysicalPortServiceCapOpuPayloadType':changePhysicalPortServiceCapOpuPayloadType,'changePhysicalPortServiceCapSigDegThresSonetLine':changePhysicalPortServiceCapSigDegThresSonetLine,'changePhysicalPortServiceCapSigDegThresSdhMs':changePhysicalPortServiceCapSigDegThresSdhMs,'changePhysicalPortServiceCapSigDegThresOtu':changePhysicalPortServiceCapSigDegThresOtu,'changePhysicalPortServiceCapSigDegThresOdu':changePhysicalPortServiceCapSigDegThresOdu,'changePhysicalPortServiceCapSigDegThreshold':changePhysicalPortServiceCapSigDegThreshold,'changePhysicalPortServiceCapSigDegPcslThreshold':changePhysicalPortServiceCapSigDegPcslThreshold,'changePhysicalPortServiceCapSigDegThresSonetSection':changePhysicalPortServiceCapSigDegThresSonetSection,'changePhysicalPortServiceCapSigDegThresSdhSection':changePhysicalPortServiceCapSigDegThresSdhSection,'changePhysicalPortServiceCapSigDegThresOduTcmA':changePhysicalPortServiceCapSigDegThresOduTcmA,'changePhysicalPortServiceCapSigDegThresOduTcmB':changePhysicalPortServiceCapSigDegThresOduTcmB,'changePhysicalPortServiceCapSigDegThresOduTcmC':changePhysicalPortServiceCapSigDegThresOduTcmC,'changePhysicalPortServiceCapSignalDegradePeriod':changePhysicalPortServiceCapSignalDegradePeriod,'changePhysicalPortServiceCapSigDegPeriodOdu':changePhysicalPortServiceCapSigDegPeriodOdu,'changePhysicalPortServiceCapSigDegPeriodOtu':changePhysicalPortServiceCapSigDegPeriodOtu,'changePhysicalPortServiceCapSigDegPeriodIntegration':changePhysicalPortServiceCapSigDegPeriodIntegration,'changePhysicalPortServiceCapSigDegPeriodSdhSection':changePhysicalPortServiceCapSigDegPeriodSdhSection,'changePhysicalPortServiceCapSigDegPeriodOduTcmA':changePhysicalPortServiceCapSigDegPeriodOduTcmA,'changePhysicalPortServiceCapSigDegPeriodOduTcmB':changePhysicalPortServiceCapSigDegPeriodOduTcmB,'changePhysicalPortServiceCapSigDegPeriodOduTcmC':changePhysicalPortServiceCapSigDegPeriodOduTcmC,'changePhysicalPortServiceCapOtnStuffing':changePhysicalPortServiceCapOtnStuffing,'changePhysicalPortServiceCapTcmALevel':changePhysicalPortServiceCapTcmALevel,'changePhysicalPortServiceCapTcmBLevel':changePhysicalPortServiceCapTcmBLevel,'changePhysicalPortServiceCapTcmCLevel':changePhysicalPortServiceCapTcmCLevel,'changePhysicalPortServiceCapTerminationLevel':changePhysicalPortServiceCapTerminationLevel,'changePhysicalPortServiceCapTimingSource':changePhysicalPortServiceCapTimingSource,'changePhysicalPortServiceCapTimModeOdu':changePhysicalPortServiceCapTimModeOdu,'changePhysicalPortServiceCapTimModeOtu':changePhysicalPortServiceCapTimModeOtu,'changePhysicalPortServiceCapTimModeSonetSection':changePhysicalPortServiceCapTimModeSonetSection,'changePhysicalPortServiceCapTimModeOduTcmA':changePhysicalPortServiceCapTimModeOduTcmA,'changePhysicalPortServiceCapTimModeOduTcmB':changePhysicalPortServiceCapTimModeOduTcmB,'changePhysicalPortServiceCapTimModeOduTcmC':changePhysicalPortServiceCapTimModeOduTcmC,'changePhysicalPortServiceCapTraceFormSonetSection':changePhysicalPortServiceCapTraceFormSonetSection,'changePhysicalPortServiceCapTraceExpectedSonetSection':changePhysicalPortServiceCapTraceExpectedSonetSection,'changePhysicalPortServiceCapTraceTransmitSonetSection':changePhysicalPortServiceCapTraceTransmitSonetSection,'changePhysicalPortServiceCapTraceExpectedOtu':changePhysicalPortServiceCapTraceExpectedOtu,'changePhysicalPortServiceCapTraceTransmitSapiOtu':changePhysicalPortServiceCapTraceTransmitSapiOtu,'changePhysicalPortServiceCapTraceTransmitDapiOtu':changePhysicalPortServiceCapTraceTransmitDapiOtu,'changePhysicalPortServiceCapTraceTransmitOpspOtu':changePhysicalPortServiceCapTraceTransmitOpspOtu,'changePhysicalPortServiceCapTraceExpectedOdu':changePhysicalPortServiceCapTraceExpectedOdu,'changePhysicalPortServiceCapTraceTransmitSapiOdu':changePhysicalPortServiceCapTraceTransmitSapiOdu,'changePhysicalPortServiceCapTraceTransmitDapiOdu':changePhysicalPortServiceCapTraceTransmitDapiOdu,'changePhysicalPortServiceCapTraceTransmitOpspOdu':changePhysicalPortServiceCapTraceTransmitOpspOdu,'changePhysicalPortServiceCapTraceExpectedOduTcmA':changePhysicalPortServiceCapTraceExpectedOduTcmA,'changePhysicalPortServiceCapTraceTransmitSapiOduTcmA':changePhysicalPortServiceCapTraceTransmitSapiOduTcmA,'changePhysicalPortServiceCapTraceTransmitDapiOduTcmA':changePhysicalPortServiceCapTraceTransmitDapiOduTcmA,'changePhysicalPortServiceCapTraceTransmitOpspOduTcmA':changePhysicalPortServiceCapTraceTransmitOpspOduTcmA,'changePhysicalPortServiceCapTraceExpectedOduTcmB':changePhysicalPortServiceCapTraceExpectedOduTcmB,'changePhysicalPortServiceCapTraceTransmitSapiOduTcmB':changePhysicalPortServiceCapTraceTransmitSapiOduTcmB,'changePhysicalPortServiceCapTraceTransmitDapiOduTcmB':changePhysicalPortServiceCapTraceTransmitDapiOduTcmB,'changePhysicalPortServiceCapTraceTransmitOpspOduTcmB':changePhysicalPortServiceCapTraceTransmitOpspOduTcmB,'changePhysicalPortServiceCapTraceExpectedOduTcmC':changePhysicalPortServiceCapTraceExpectedOduTcmC,'changePhysicalPortServiceCapTraceTransmitSapiOduTcmC':changePhysicalPortServiceCapTraceTransmitSapiOduTcmC,'changePhysicalPortServiceCapTraceTransmitDapiOduTcmC':changePhysicalPortServiceCapTraceTransmitDapiOduTcmC,'changePhysicalPortServiceCapTraceTransmitOpspOduTcmC':changePhysicalPortServiceCapTraceTransmitOpspOduTcmC,'changePhysicalPortServiceCapTxOffDelay':changePhysicalPortServiceCapTxOffDelay,'changePhysicalPortServiceCapVoaMode':changePhysicalPortServiceCapVoaMode,'changePhysicalPortServiceCapVoaSetpoint':changePhysicalPortServiceCapVoaSetpoint,'changePhysicalPortServiceCapTxOffOnTm':changePhysicalPortServiceCapTxOffOnTm,'changePhysicalPortServiceCapTxOffTimer':changePhysicalPortServiceCapTxOffTimer,'changePhysicalPortServiceCapTxOnTimer':changePhysicalPortServiceCapTxOnTimer,'endOfChangePhysicalPortServiceCapTable':endOfChangePhysicalPortServiceCapTable,'endOfChangeServiceCap':endOfChangeServiceCap,'protectionCap':protectionCap,'ffpCapTable':ffpCapTable,'ffpCapEntry':ffpCapEntry,'ffpCapRowStatus':ffpCapRowStatus,'ffpCapCreationMethod':ffpCapCreationMethod,'ffpCapSDswitching':ffpCapSDswitching,'ffpCapHoldOffTime':ffpCapHoldOffTime,'ffpCapProtectionMech':ffpCapProtectionMech,'ffpCapWorkingAid':ffpCapWorkingAid,'ffpCapProtectionAid':ffpCapProtectionAid,'ffpCapSignalDegradeSwitching':ffpCapSignalDegradeSwitching,'ffpCapFarEndIp':ffpCapFarEndIp,'ffpCapPeerAid':ffpCapPeerAid,'ffpCapApsType':ffpCapApsType,'ffpCapRevertMode':ffpCapRevertMode,'ffpCapWaitToRestore':ffpCapWaitToRestore,'ffpCapDirection':ffpCapDirection,'endOfFfpCapTable':endOfFfpCapTable,'endOfProtectionCap':endOfProtectionCap,'conformanceCap':conformanceCap,'compliancesCap':compliancesCap,'complianceCap':complianceCap,'groupsCap':groupsCap,_Bc:objectGroupCap})