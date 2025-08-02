_AD='xScgPtpGroup'
_AC='xScgPtpExpTotalTxPower'
_AB='xScgPtpPerCarrierTargetTxPower'
_AA='xScgPtpInstalledRxPCLOprMode'
_A9='xScgPtpOpticalSignalStatus'
_A8='xScgPtpOpticalSignal'
_A7='xScgPtpCarrierCount17Gbaud'
_A6='xScgPtpCarrierCount22Gbaud'
_A5='xScgPtpCarrierCount33Gbaud'
_A4='xScgPtpRxPCLOprMode'
_A3='xScgPtpInstalledFECOHRatio'
_A2='xScgPtpUnAssignedCarrierList'
_A1='xScgPtpBwBlicensed'
_A0='xScgPtpBwBused'
_z='xScgPtpBwBmax'
_y='xScgPtpBw3Qlicensed'
_x='xScgPtpBw3Qused'
_w='xScgPtpBw3Qmax'
_v='xScgPtpBw8Qlicensed'
_u='xScgPtpBw8Qused'
_t='xScgPtpBw8Qmax'
_s='xScgPtpBw16Qlicensed'
_r='xScgPtpBw16Qused'
_q='xScgPtpBw16Qmax'
_p='xScgPtpFECOverheadRatio'
_o='xScgPtpBwUsgWaterMarkGranularity'
_n='xScgPtpDefFlexLicModFormat'
_m='xScgPtpLoopback'
_l='xScgPtpCarrierCount'
_k='xScgPtpRxPicState'
_j='xScgPtpTxPicState'
_i='xScgPtpBwQlicensed'
_h='xScgPtpBwQused'
_g='xScgPtpBwQmax'
_f='xScgPtpProvisionedPeerTp'
_e='xScgPtpRxPowerOffset'
_d='xScgPtpTargetTxPower'
_c='xScgPtpTargetTxPowerOffset'
_b='xScgPtpLineSystemMode'
_a='xScgPtpInstalledEncodingMode'
_Z='xScgPtpProvisionedEncodingMode'
_Y='xScgPtpPowerControlLoop'
_X='xScgPtpAvailableTunableSchNumbers'
_W='xScgPtpGain'
_V='xScgPtpRxEdfaOutputPowerTarget'
_U='xScgPtpRecommendedGain'
_T='xScgPtpMaxFruGain'
_S='xScgPtpPmHistStatsEnable'
_R='xScgPtpProvisionedOpenWaveRemotePtp'
_Q='xScgPtpInterfaceType'
_P='xScgPtpProvisionedNeighborAdTpType'
_O='xScgPtpProvisionedNeighborTP'
_N='xScgPtpDiscoveredNeighborTP'
_M='xScgPtpAutoDiscoveryState'
_L='xScgPtpProvisionedFPMPO'
_K='xScgPtpMPOAID'
_J='xScgPtpOpenwaveTargetTxScgPower'
_I='InfnPowerControlLoop'
_H='InfnLineSystemMode'
_G='ifIndex'
_F='IF-MIB'
_E='InfnEncoding'
_D='read-write'
_C='read-only'
_B='INFINERA-TP-XSCGPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatArbitraryPrecision,FloatHundredths,FloatTenths,InfnAdTpType,InfnAutoDiscoveryState,InfnEnableDisable,InfnEncoding,InfnEqptType,InfnFECOverHeadPercent,InfnLicenseModulationType,InfnLineSystemMode,InfnOpticalSignal,InfnOpticalSignalStatus,InfnPCLOperatingMode,InfnPicStatus,InfnPmHistStatsControl,InfnPowerControlLoop,InfnWaveInterfaceType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatArbitraryPrecision','FloatHundredths','FloatTenths','InfnAdTpType','InfnAutoDiscoveryState','InfnEnableDisable',_E,'InfnEqptType','InfnFECOverHeadPercent','InfnLicenseModulationType',_H,'InfnOpticalSignal','InfnOpticalSignalStatus','InfnPCLOperatingMode','InfnPicStatus','InfnPmHistStatsControl',_I,'InfnWaveInterfaceType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
xScgPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,57))
if mibBuilder.loadTexts:xScgPtpMIB.setRevisions(('2008-10-20 00:00',))
_XScgPtpTable_Object=MibTable
xScgPtpTable=_XScgPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1))
if mibBuilder.loadTexts:xScgPtpTable.setStatus(_A)
_XScgPtpEntry_Object=MibTableRow
xScgPtpEntry=_XScgPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1))
xScgPtpEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:xScgPtpEntry.setStatus(_A)
_XScgPtpOpenwaveTargetTxScgPower_Type=FloatTenths
_XScgPtpOpenwaveTargetTxScgPower_Object=MibTableColumn
xScgPtpOpenwaveTargetTxScgPower=_XScgPtpOpenwaveTargetTxScgPower_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,1),_XScgPtpOpenwaveTargetTxScgPower_Type())
xScgPtpOpenwaveTargetTxScgPower.setMaxAccess(_D)
if mibBuilder.loadTexts:xScgPtpOpenwaveTargetTxScgPower.setStatus(_A)
_XScgPtpMPOAID_Type=DisplayString
_XScgPtpMPOAID_Object=MibTableColumn
xScgPtpMPOAID=_XScgPtpMPOAID_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,2),_XScgPtpMPOAID_Type())
xScgPtpMPOAID.setMaxAccess(_D)
if mibBuilder.loadTexts:xScgPtpMPOAID.setStatus(_A)
_XScgPtpProvisionedFPMPO_Type=DisplayString
_XScgPtpProvisionedFPMPO_Object=MibTableColumn
xScgPtpProvisionedFPMPO=_XScgPtpProvisionedFPMPO_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,3),_XScgPtpProvisionedFPMPO_Type())
xScgPtpProvisionedFPMPO.setMaxAccess(_D)
if mibBuilder.loadTexts:xScgPtpProvisionedFPMPO.setStatus(_A)
_XScgPtpAutoDiscoveryState_Type=InfnAutoDiscoveryState
_XScgPtpAutoDiscoveryState_Object=MibTableColumn
xScgPtpAutoDiscoveryState=_XScgPtpAutoDiscoveryState_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,4),_XScgPtpAutoDiscoveryState_Type())
xScgPtpAutoDiscoveryState.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpAutoDiscoveryState.setStatus(_A)
_XScgPtpDiscoveredNeighborTP_Type=DisplayString
_XScgPtpDiscoveredNeighborTP_Object=MibTableColumn
xScgPtpDiscoveredNeighborTP=_XScgPtpDiscoveredNeighborTP_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,5),_XScgPtpDiscoveredNeighborTP_Type())
xScgPtpDiscoveredNeighborTP.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpDiscoveredNeighborTP.setStatus(_A)
_XScgPtpProvisionedNeighborTP_Type=DisplayString
_XScgPtpProvisionedNeighborTP_Object=MibTableColumn
xScgPtpProvisionedNeighborTP=_XScgPtpProvisionedNeighborTP_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,6),_XScgPtpProvisionedNeighborTP_Type())
xScgPtpProvisionedNeighborTP.setMaxAccess(_D)
if mibBuilder.loadTexts:xScgPtpProvisionedNeighborTP.setStatus(_A)
_XScgPtpProvisionedNeighborAdTpType_Type=InfnAdTpType
_XScgPtpProvisionedNeighborAdTpType_Object=MibTableColumn
xScgPtpProvisionedNeighborAdTpType=_XScgPtpProvisionedNeighborAdTpType_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,7),_XScgPtpProvisionedNeighborAdTpType_Type())
xScgPtpProvisionedNeighborAdTpType.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpProvisionedNeighborAdTpType.setStatus(_A)
_XScgPtpInterfaceType_Type=InfnWaveInterfaceType
_XScgPtpInterfaceType_Object=MibTableColumn
xScgPtpInterfaceType=_XScgPtpInterfaceType_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,8),_XScgPtpInterfaceType_Type())
xScgPtpInterfaceType.setMaxAccess(_D)
if mibBuilder.loadTexts:xScgPtpInterfaceType.setStatus(_A)
_XScgPtpProvisionedOpenWaveRemotePtp_Type=DisplayString
_XScgPtpProvisionedOpenWaveRemotePtp_Object=MibTableColumn
xScgPtpProvisionedOpenWaveRemotePtp=_XScgPtpProvisionedOpenWaveRemotePtp_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,9),_XScgPtpProvisionedOpenWaveRemotePtp_Type())
xScgPtpProvisionedOpenWaveRemotePtp.setMaxAccess(_D)
if mibBuilder.loadTexts:xScgPtpProvisionedOpenWaveRemotePtp.setStatus(_A)
_XScgPtpPmHistStatsEnable_Type=InfnPmHistStatsControl
_XScgPtpPmHistStatsEnable_Object=MibTableColumn
xScgPtpPmHistStatsEnable=_XScgPtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,10),_XScgPtpPmHistStatsEnable_Type())
xScgPtpPmHistStatsEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:xScgPtpPmHistStatsEnable.setStatus(_A)
_XScgPtpMaxFruGain_Type=FloatHundredths
_XScgPtpMaxFruGain_Object=MibTableColumn
xScgPtpMaxFruGain=_XScgPtpMaxFruGain_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,11),_XScgPtpMaxFruGain_Type())
xScgPtpMaxFruGain.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpMaxFruGain.setStatus(_A)
_XScgPtpRecommendedGain_Type=FloatTenths
_XScgPtpRecommendedGain_Object=MibTableColumn
xScgPtpRecommendedGain=_XScgPtpRecommendedGain_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,12),_XScgPtpRecommendedGain_Type())
xScgPtpRecommendedGain.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpRecommendedGain.setStatus(_A)
_XScgPtpRxEdfaOutputPowerTarget_Type=FloatTenths
_XScgPtpRxEdfaOutputPowerTarget_Object=MibTableColumn
xScgPtpRxEdfaOutputPowerTarget=_XScgPtpRxEdfaOutputPowerTarget_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,13),_XScgPtpRxEdfaOutputPowerTarget_Type())
xScgPtpRxEdfaOutputPowerTarget.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpRxEdfaOutputPowerTarget.setStatus(_A)
_XScgPtpGain_Type=FloatTenths
_XScgPtpGain_Object=MibTableColumn
xScgPtpGain=_XScgPtpGain_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,14),_XScgPtpGain_Type())
xScgPtpGain.setMaxAccess(_D)
if mibBuilder.loadTexts:xScgPtpGain.setStatus(_A)
_XScgPtpAvailableTunableSchNumbers_Type=DisplayString
_XScgPtpAvailableTunableSchNumbers_Object=MibTableColumn
xScgPtpAvailableTunableSchNumbers=_XScgPtpAvailableTunableSchNumbers_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,15),_XScgPtpAvailableTunableSchNumbers_Type())
xScgPtpAvailableTunableSchNumbers.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpAvailableTunableSchNumbers.setStatus(_A)
class _XScgPtpPowerControlLoop_Type(InfnPowerControlLoop):defaultValue=1
_XScgPtpPowerControlLoop_Type.__name__=_I
_XScgPtpPowerControlLoop_Object=MibTableColumn
xScgPtpPowerControlLoop=_XScgPtpPowerControlLoop_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,16),_XScgPtpPowerControlLoop_Type())
xScgPtpPowerControlLoop.setMaxAccess(_D)
if mibBuilder.loadTexts:xScgPtpPowerControlLoop.setStatus(_A)
class _XScgPtpProvisionedEncodingMode_Type(InfnEncoding):defaultValue=1
_XScgPtpProvisionedEncodingMode_Type.__name__=_E
_XScgPtpProvisionedEncodingMode_Object=MibTableColumn
xScgPtpProvisionedEncodingMode=_XScgPtpProvisionedEncodingMode_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,17),_XScgPtpProvisionedEncodingMode_Type())
xScgPtpProvisionedEncodingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:xScgPtpProvisionedEncodingMode.setStatus(_A)
class _XScgPtpInstalledEncodingMode_Type(InfnEncoding):defaultValue=1
_XScgPtpInstalledEncodingMode_Type.__name__=_E
_XScgPtpInstalledEncodingMode_Object=MibTableColumn
xScgPtpInstalledEncodingMode=_XScgPtpInstalledEncodingMode_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,18),_XScgPtpInstalledEncodingMode_Type())
xScgPtpInstalledEncodingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:xScgPtpInstalledEncodingMode.setStatus(_A)
class _XScgPtpLineSystemMode_Type(InfnLineSystemMode):defaultValue=2
_XScgPtpLineSystemMode_Type.__name__=_H
_XScgPtpLineSystemMode_Object=MibTableColumn
xScgPtpLineSystemMode=_XScgPtpLineSystemMode_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,19),_XScgPtpLineSystemMode_Type())
xScgPtpLineSystemMode.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpLineSystemMode.setStatus(_A)
_XScgPtpTargetTxPowerOffset_Type=FloatTenths
_XScgPtpTargetTxPowerOffset_Object=MibTableColumn
xScgPtpTargetTxPowerOffset=_XScgPtpTargetTxPowerOffset_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,20),_XScgPtpTargetTxPowerOffset_Type())
xScgPtpTargetTxPowerOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:xScgPtpTargetTxPowerOffset.setStatus(_A)
_XScgPtpTargetTxPower_Type=FloatTenths
_XScgPtpTargetTxPower_Object=MibTableColumn
xScgPtpTargetTxPower=_XScgPtpTargetTxPower_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,21),_XScgPtpTargetTxPower_Type())
xScgPtpTargetTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpTargetTxPower.setStatus(_A)
_XScgPtpRxPowerOffset_Type=FloatTenths
_XScgPtpRxPowerOffset_Object=MibTableColumn
xScgPtpRxPowerOffset=_XScgPtpRxPowerOffset_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,22),_XScgPtpRxPowerOffset_Type())
xScgPtpRxPowerOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:xScgPtpRxPowerOffset.setStatus(_A)
_XScgPtpProvisionedPeerTp_Type=DisplayString
_XScgPtpProvisionedPeerTp_Object=MibTableColumn
xScgPtpProvisionedPeerTp=_XScgPtpProvisionedPeerTp_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,23),_XScgPtpProvisionedPeerTp_Type())
xScgPtpProvisionedPeerTp.setMaxAccess(_D)
if mibBuilder.loadTexts:xScgPtpProvisionedPeerTp.setStatus(_A)
_XScgPtpBwQmax_Type=FloatTenths
_XScgPtpBwQmax_Object=MibTableColumn
xScgPtpBwQmax=_XScgPtpBwQmax_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,24),_XScgPtpBwQmax_Type())
xScgPtpBwQmax.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpBwQmax.setStatus(_A)
_XScgPtpBwQused_Type=FloatTenths
_XScgPtpBwQused_Object=MibTableColumn
xScgPtpBwQused=_XScgPtpBwQused_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,25),_XScgPtpBwQused_Type())
xScgPtpBwQused.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpBwQused.setStatus(_A)
_XScgPtpBwQlicensed_Type=FloatTenths
_XScgPtpBwQlicensed_Object=MibTableColumn
xScgPtpBwQlicensed=_XScgPtpBwQlicensed_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,26),_XScgPtpBwQlicensed_Type())
xScgPtpBwQlicensed.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpBwQlicensed.setStatus(_A)
_XScgPtpTxPicState_Type=InfnPicStatus
_XScgPtpTxPicState_Object=MibTableColumn
xScgPtpTxPicState=_XScgPtpTxPicState_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,27),_XScgPtpTxPicState_Type())
xScgPtpTxPicState.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpTxPicState.setStatus(_A)
_XScgPtpRxPicState_Type=InfnPicStatus
_XScgPtpRxPicState_Object=MibTableColumn
xScgPtpRxPicState=_XScgPtpRxPicState_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,28),_XScgPtpRxPicState_Type())
xScgPtpRxPicState.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpRxPicState.setStatus(_A)
_XScgPtpCarrierCount_Type=FloatTenths
_XScgPtpCarrierCount_Object=MibTableColumn
xScgPtpCarrierCount=_XScgPtpCarrierCount_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,29),_XScgPtpCarrierCount_Type())
xScgPtpCarrierCount.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpCarrierCount.setStatus(_A)
_XScgPtpLoopback_Type=TruthValue
_XScgPtpLoopback_Object=MibTableColumn
xScgPtpLoopback=_XScgPtpLoopback_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,30),_XScgPtpLoopback_Type())
xScgPtpLoopback.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpLoopback.setStatus(_A)
_XScgPtpDefFlexLicModFormat_Type=InfnLicenseModulationType
_XScgPtpDefFlexLicModFormat_Object=MibTableColumn
xScgPtpDefFlexLicModFormat=_XScgPtpDefFlexLicModFormat_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,31),_XScgPtpDefFlexLicModFormat_Type())
xScgPtpDefFlexLicModFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpDefFlexLicModFormat.setStatus(_A)
_XScgPtpBwUsgWaterMarkGranularity_Type=FloatTenths
_XScgPtpBwUsgWaterMarkGranularity_Object=MibTableColumn
xScgPtpBwUsgWaterMarkGranularity=_XScgPtpBwUsgWaterMarkGranularity_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,32),_XScgPtpBwUsgWaterMarkGranularity_Type())
xScgPtpBwUsgWaterMarkGranularity.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpBwUsgWaterMarkGranularity.setStatus(_A)
_XScgPtpFECOverheadRatio_Type=InfnFECOverHeadPercent
_XScgPtpFECOverheadRatio_Object=MibTableColumn
xScgPtpFECOverheadRatio=_XScgPtpFECOverheadRatio_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,33),_XScgPtpFECOverheadRatio_Type())
xScgPtpFECOverheadRatio.setMaxAccess(_D)
if mibBuilder.loadTexts:xScgPtpFECOverheadRatio.setStatus(_A)
_XScgPtpBw16Qmax_Type=FloatTenths
_XScgPtpBw16Qmax_Object=MibTableColumn
xScgPtpBw16Qmax=_XScgPtpBw16Qmax_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,34),_XScgPtpBw16Qmax_Type())
xScgPtpBw16Qmax.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpBw16Qmax.setStatus(_A)
_XScgPtpBw16Qused_Type=FloatTenths
_XScgPtpBw16Qused_Object=MibTableColumn
xScgPtpBw16Qused=_XScgPtpBw16Qused_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,35),_XScgPtpBw16Qused_Type())
xScgPtpBw16Qused.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpBw16Qused.setStatus(_A)
_XScgPtpBw16Qlicensed_Type=FloatTenths
_XScgPtpBw16Qlicensed_Object=MibTableColumn
xScgPtpBw16Qlicensed=_XScgPtpBw16Qlicensed_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,36),_XScgPtpBw16Qlicensed_Type())
xScgPtpBw16Qlicensed.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpBw16Qlicensed.setStatus(_A)
_XScgPtpBw8Qmax_Type=FloatTenths
_XScgPtpBw8Qmax_Object=MibTableColumn
xScgPtpBw8Qmax=_XScgPtpBw8Qmax_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,37),_XScgPtpBw8Qmax_Type())
xScgPtpBw8Qmax.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpBw8Qmax.setStatus(_A)
_XScgPtpBw8Qused_Type=FloatTenths
_XScgPtpBw8Qused_Object=MibTableColumn
xScgPtpBw8Qused=_XScgPtpBw8Qused_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,38),_XScgPtpBw8Qused_Type())
xScgPtpBw8Qused.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpBw8Qused.setStatus(_A)
_XScgPtpBw8Qlicensed_Type=FloatTenths
_XScgPtpBw8Qlicensed_Object=MibTableColumn
xScgPtpBw8Qlicensed=_XScgPtpBw8Qlicensed_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,39),_XScgPtpBw8Qlicensed_Type())
xScgPtpBw8Qlicensed.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpBw8Qlicensed.setStatus(_A)
_XScgPtpBw3Qmax_Type=FloatTenths
_XScgPtpBw3Qmax_Object=MibTableColumn
xScgPtpBw3Qmax=_XScgPtpBw3Qmax_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,40),_XScgPtpBw3Qmax_Type())
xScgPtpBw3Qmax.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpBw3Qmax.setStatus(_A)
_XScgPtpBw3Qused_Type=FloatTenths
_XScgPtpBw3Qused_Object=MibTableColumn
xScgPtpBw3Qused=_XScgPtpBw3Qused_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,41),_XScgPtpBw3Qused_Type())
xScgPtpBw3Qused.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpBw3Qused.setStatus(_A)
_XScgPtpBw3Qlicensed_Type=FloatTenths
_XScgPtpBw3Qlicensed_Object=MibTableColumn
xScgPtpBw3Qlicensed=_XScgPtpBw3Qlicensed_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,42),_XScgPtpBw3Qlicensed_Type())
xScgPtpBw3Qlicensed.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpBw3Qlicensed.setStatus(_A)
_XScgPtpBwBmax_Type=FloatTenths
_XScgPtpBwBmax_Object=MibTableColumn
xScgPtpBwBmax=_XScgPtpBwBmax_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,43),_XScgPtpBwBmax_Type())
xScgPtpBwBmax.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpBwBmax.setStatus(_A)
_XScgPtpBwBused_Type=FloatTenths
_XScgPtpBwBused_Object=MibTableColumn
xScgPtpBwBused=_XScgPtpBwBused_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,44),_XScgPtpBwBused_Type())
xScgPtpBwBused.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpBwBused.setStatus(_A)
_XScgPtpBwBlicensed_Type=FloatTenths
_XScgPtpBwBlicensed_Object=MibTableColumn
xScgPtpBwBlicensed=_XScgPtpBwBlicensed_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,45),_XScgPtpBwBlicensed_Type())
xScgPtpBwBlicensed.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpBwBlicensed.setStatus(_A)
_XScgPtpUnAssignedCarrierList_Type=DisplayString
_XScgPtpUnAssignedCarrierList_Object=MibTableColumn
xScgPtpUnAssignedCarrierList=_XScgPtpUnAssignedCarrierList_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,46),_XScgPtpUnAssignedCarrierList_Type())
xScgPtpUnAssignedCarrierList.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpUnAssignedCarrierList.setStatus(_A)
_XScgPtpInstalledFECOHRatio_Type=InfnFECOverHeadPercent
_XScgPtpInstalledFECOHRatio_Object=MibTableColumn
xScgPtpInstalledFECOHRatio=_XScgPtpInstalledFECOHRatio_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,47),_XScgPtpInstalledFECOHRatio_Type())
xScgPtpInstalledFECOHRatio.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpInstalledFECOHRatio.setStatus(_A)
_XScgPtpRxPCLOprMode_Type=InfnPCLOperatingMode
_XScgPtpRxPCLOprMode_Object=MibTableColumn
xScgPtpRxPCLOprMode=_XScgPtpRxPCLOprMode_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,48),_XScgPtpRxPCLOprMode_Type())
xScgPtpRxPCLOprMode.setMaxAccess(_D)
if mibBuilder.loadTexts:xScgPtpRxPCLOprMode.setStatus(_A)
_XScgPtpInstalledRxPCLOprMode_Type=InfnPCLOperatingMode
_XScgPtpInstalledRxPCLOprMode_Object=MibTableColumn
xScgPtpInstalledRxPCLOprMode=_XScgPtpInstalledRxPCLOprMode_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,49),_XScgPtpInstalledRxPCLOprMode_Type())
xScgPtpInstalledRxPCLOprMode.setMaxAccess(_D)
if mibBuilder.loadTexts:xScgPtpInstalledRxPCLOprMode.setStatus(_A)
_XScgPtpCarrierCount33Gbaud_Type=FloatArbitraryPrecision
_XScgPtpCarrierCount33Gbaud_Object=MibTableColumn
xScgPtpCarrierCount33Gbaud=_XScgPtpCarrierCount33Gbaud_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,50),_XScgPtpCarrierCount33Gbaud_Type())
xScgPtpCarrierCount33Gbaud.setMaxAccess(_D)
if mibBuilder.loadTexts:xScgPtpCarrierCount33Gbaud.setStatus(_A)
_XScgPtpCarrierCount22Gbaud_Type=FloatArbitraryPrecision
_XScgPtpCarrierCount22Gbaud_Object=MibTableColumn
xScgPtpCarrierCount22Gbaud=_XScgPtpCarrierCount22Gbaud_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,51),_XScgPtpCarrierCount22Gbaud_Type())
xScgPtpCarrierCount22Gbaud.setMaxAccess(_D)
if mibBuilder.loadTexts:xScgPtpCarrierCount22Gbaud.setStatus(_A)
_XScgPtpCarrierCount17Gbaud_Type=FloatArbitraryPrecision
_XScgPtpCarrierCount17Gbaud_Object=MibTableColumn
xScgPtpCarrierCount17Gbaud=_XScgPtpCarrierCount17Gbaud_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,52),_XScgPtpCarrierCount17Gbaud_Type())
xScgPtpCarrierCount17Gbaud.setMaxAccess(_D)
if mibBuilder.loadTexts:xScgPtpCarrierCount17Gbaud.setStatus(_A)
_XScgPtpOpticalSignal_Type=InfnOpticalSignal
_XScgPtpOpticalSignal_Object=MibTableColumn
xScgPtpOpticalSignal=_XScgPtpOpticalSignal_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,53),_XScgPtpOpticalSignal_Type())
xScgPtpOpticalSignal.setMaxAccess(_D)
if mibBuilder.loadTexts:xScgPtpOpticalSignal.setStatus(_A)
_XScgPtpOpticalSignalStatus_Type=InfnOpticalSignalStatus
_XScgPtpOpticalSignalStatus_Object=MibTableColumn
xScgPtpOpticalSignalStatus=_XScgPtpOpticalSignalStatus_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,54),_XScgPtpOpticalSignalStatus_Type())
xScgPtpOpticalSignalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpOpticalSignalStatus.setStatus(_A)
_XScgPtpPerCarrierTargetTxPower_Type=FloatArbitraryPrecision
_XScgPtpPerCarrierTargetTxPower_Object=MibTableColumn
xScgPtpPerCarrierTargetTxPower=_XScgPtpPerCarrierTargetTxPower_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,55),_XScgPtpPerCarrierTargetTxPower_Type())
xScgPtpPerCarrierTargetTxPower.setMaxAccess(_D)
if mibBuilder.loadTexts:xScgPtpPerCarrierTargetTxPower.setStatus(_A)
_XScgPtpExpTotalTxPower_Type=FloatArbitraryPrecision
_XScgPtpExpTotalTxPower_Object=MibTableColumn
xScgPtpExpTotalTxPower=_XScgPtpExpTotalTxPower_Object((1,3,6,1,4,1,21296,2,2,2,2,57,1,1,56),_XScgPtpExpTotalTxPower_Type())
xScgPtpExpTotalTxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:xScgPtpExpTotalTxPower.setStatus(_A)
_XScgPtpConformance_ObjectIdentity=ObjectIdentity
xScgPtpConformance=_XScgPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,57,3))
_XScgPtpCompliances_ObjectIdentity=ObjectIdentity
xScgPtpCompliances=_XScgPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,57,3,1))
_XScgPtpGroups_ObjectIdentity=ObjectIdentity
xScgPtpGroups=_XScgPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,57,3,2))
xScgPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,57,3,2,1))
xScgPtpGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:xScgPtpGroup.setStatus(_A)
xScgPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,57,3,1,1))
xScgPtpCompliance.setObjects((_B,_AD))
if mibBuilder.loadTexts:xScgPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'xScgPtpMIB':xScgPtpMIB,'xScgPtpTable':xScgPtpTable,'xScgPtpEntry':xScgPtpEntry,_J:xScgPtpOpenwaveTargetTxScgPower,_K:xScgPtpMPOAID,_L:xScgPtpProvisionedFPMPO,_M:xScgPtpAutoDiscoveryState,_N:xScgPtpDiscoveredNeighborTP,_O:xScgPtpProvisionedNeighborTP,_P:xScgPtpProvisionedNeighborAdTpType,_Q:xScgPtpInterfaceType,_R:xScgPtpProvisionedOpenWaveRemotePtp,_S:xScgPtpPmHistStatsEnable,_T:xScgPtpMaxFruGain,_U:xScgPtpRecommendedGain,_V:xScgPtpRxEdfaOutputPowerTarget,_W:xScgPtpGain,_X:xScgPtpAvailableTunableSchNumbers,_Y:xScgPtpPowerControlLoop,_Z:xScgPtpProvisionedEncodingMode,_a:xScgPtpInstalledEncodingMode,_b:xScgPtpLineSystemMode,_c:xScgPtpTargetTxPowerOffset,_d:xScgPtpTargetTxPower,_e:xScgPtpRxPowerOffset,_f:xScgPtpProvisionedPeerTp,_g:xScgPtpBwQmax,_h:xScgPtpBwQused,_i:xScgPtpBwQlicensed,_j:xScgPtpTxPicState,_k:xScgPtpRxPicState,_l:xScgPtpCarrierCount,_m:xScgPtpLoopback,_n:xScgPtpDefFlexLicModFormat,_o:xScgPtpBwUsgWaterMarkGranularity,_p:xScgPtpFECOverheadRatio,_q:xScgPtpBw16Qmax,_r:xScgPtpBw16Qused,_s:xScgPtpBw16Qlicensed,_t:xScgPtpBw8Qmax,_u:xScgPtpBw8Qused,_v:xScgPtpBw8Qlicensed,_w:xScgPtpBw3Qmax,_x:xScgPtpBw3Qused,_y:xScgPtpBw3Qlicensed,_z:xScgPtpBwBmax,_A0:xScgPtpBwBused,_A1:xScgPtpBwBlicensed,_A2:xScgPtpUnAssignedCarrierList,_A3:xScgPtpInstalledFECOHRatio,_A4:xScgPtpRxPCLOprMode,_AA:xScgPtpInstalledRxPCLOprMode,_A5:xScgPtpCarrierCount33Gbaud,_A6:xScgPtpCarrierCount22Gbaud,_A7:xScgPtpCarrierCount17Gbaud,_A8:xScgPtpOpticalSignal,_A9:xScgPtpOpticalSignalStatus,_AB:xScgPtpPerCarrierTargetTxPower,_AC:xScgPtpExpTotalTxPower,'xScgPtpConformance':xScgPtpConformance,'xScgPtpCompliances':xScgPtpCompliances,'xScgPtpCompliance':xScgPtpCompliance,'xScgPtpGroups':xScgPtpGroups,_AD:xScgPtpGroup})