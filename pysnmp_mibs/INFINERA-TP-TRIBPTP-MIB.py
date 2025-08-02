_A1='tribPtpGroup'
_A0='tribPtpAppliedFecEncodingMode'
_z='tribPtpProvisionedFecEncodingMode'
_y='tribPtpForwardDefectTDATrigger'
_x='tribPtpProvisionedRemoteTP'
_w='tribPtpDiscoveredRemoteTP'
_v='tribPtpAutoDiscovery'
_u='tribPtpInterfaceType'
_t='tribPtpDirectionality'
_s='tribPtpAutoCableEqualization'
_r='tribPtpDisableActionOnBERSF'
_q='tribPtpEnetPswLaserCtrl'
_p='tribPtpDtpAISOnClientSF'
_o='tribPtpAssocMoInteropCPTEInterface'
_n='tribPtpRemoteInterfaceIndex'
_m='tribPtpLocalInterfaceIndex'
_l='tribPtpCurrNumOfDrops'
_k='tribPtpMaxAllowedDrops'
_j='tribPtpPmHistStatsEnable'
_i='tribPtpSupportedServiceTypes'
_h='tribPtpRemValidSignalTimer'
_g='tribPtpValidSignalTimeInterval'
_f='tribPtpAINS'
_e='tribPtpOprSensitivityThreshold'
_d='tribPtpOprOverloadThreshold'
_c='tribPtpOprOorAlarmReporting'
_b='tribPtpOprOorLowThresholdOffset'
_a='tribPtpOprOorHighThresholdOffset'
_Z='tribPtpProvisionedServiceType'
_Y='tribPtpTribDisableAction'
_X='tribPtpMaxPerChannelCapacity'
_W='tribPtpSwRqState'
_V='tribPtpSwReason'
_U='tribPtpPsDirn'
_T='tribPtpCurProtSt'
_S='tribPtpCfgProtSt'
_R='tribPtpProtMod'
_Q='tribPtpPgMoId'
_P='InfnTribAction'
_O='InfnReporting'
_N='InfnPmHistStatsControl'
_M='InfnEnetPswLaserCtrlState'
_L='InfnDirectionality'
_K='InfnAutoCableEqualization'
_J='ifIndex'
_I='IF-MIB'
_H='Integer32'
_G='InfnOperationalState'
_F='FloatTenths'
_E='InfnEnableDisable'
_D='read-write'
_C='read-only'
_B='INFINERA-TP-TRIBPTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_I,_J)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatTenths,InfnAutoCableEqualization,InfnCfgProtState,InfnCurrProtState,InfnDirectionality,InfnEnableDisable,InfnEnetPswLaserCtrlState,InfnFecEncodingMode,InfnInterfaceType,InfnOperationalState,InfnPmHistStatsControl,InfnProtectionMode,InfnPsDirn,InfnReporting,InfnServiceType,InfnServiceTypeList,InfnSwitchReason,InfnSwitchRequestState,InfnTribAction=mibBuilder.importSymbols('INFINERA-TC-MIB',_F,_K,'InfnCfgProtState','InfnCurrProtState',_L,_E,_M,'InfnFecEncodingMode','InfnInterfaceType',_G,_N,'InfnProtectionMode','InfnPsDirn',_O,'InfnServiceType','InfnServiceTypeList','InfnSwitchReason','InfnSwitchRequestState',_P)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tribPtpMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,17))
if mibBuilder.loadTexts:tribPtpMIB.setRevisions(('2008-10-20 00:00',))
_TribPtpTable_Object=MibTable
tribPtpTable=_TribPtpTable_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1))
if mibBuilder.loadTexts:tribPtpTable.setStatus(_A)
_TribPtpEntry_Object=MibTableRow
tribPtpEntry=_TribPtpEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1))
tribPtpEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:tribPtpEntry.setStatus(_A)
_TribPtpPgMoId_Type=DisplayString
_TribPtpPgMoId_Object=MibTableColumn
tribPtpPgMoId=_TribPtpPgMoId_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,1),_TribPtpPgMoId_Type())
tribPtpPgMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPgMoId.setStatus(_A)
_TribPtpProtMod_Type=InfnProtectionMode
_TribPtpProtMod_Object=MibTableColumn
tribPtpProtMod=_TribPtpProtMod_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,2),_TribPtpProtMod_Type())
tribPtpProtMod.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpProtMod.setStatus(_A)
_TribPtpCfgProtSt_Type=InfnProtectionMode
_TribPtpCfgProtSt_Object=MibTableColumn
tribPtpCfgProtSt=_TribPtpCfgProtSt_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,3),_TribPtpCfgProtSt_Type())
tribPtpCfgProtSt.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpCfgProtSt.setStatus(_A)
_TribPtpCurProtSt_Type=InfnCurrProtState
_TribPtpCurProtSt_Object=MibTableColumn
tribPtpCurProtSt=_TribPtpCurProtSt_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,4),_TribPtpCurProtSt_Type())
tribPtpCurProtSt.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpCurProtSt.setStatus(_A)
_TribPtpPsDirn_Type=InfnPsDirn
_TribPtpPsDirn_Object=MibTableColumn
tribPtpPsDirn=_TribPtpPsDirn_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,5),_TribPtpPsDirn_Type())
tribPtpPsDirn.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpPsDirn.setStatus(_A)
_TribPtpSwReason_Type=InfnSwitchReason
_TribPtpSwReason_Object=MibTableColumn
tribPtpSwReason=_TribPtpSwReason_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,6),_TribPtpSwReason_Type())
tribPtpSwReason.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpSwReason.setStatus(_A)
_TribPtpSwRqState_Type=InfnSwitchRequestState
_TribPtpSwRqState_Object=MibTableColumn
tribPtpSwRqState=_TribPtpSwRqState_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,7),_TribPtpSwRqState_Type())
tribPtpSwRqState.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpSwRqState.setStatus(_A)
_TribPtpMaxPerChannelCapacity_Type=InfnServiceType
_TribPtpMaxPerChannelCapacity_Object=MibTableColumn
tribPtpMaxPerChannelCapacity=_TribPtpMaxPerChannelCapacity_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,8),_TribPtpMaxPerChannelCapacity_Type())
tribPtpMaxPerChannelCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpMaxPerChannelCapacity.setStatus(_A)
class _TribPtpTribDisableAction_Type(InfnTribAction):defaultValue=3
_TribPtpTribDisableAction_Type.__name__=_P
_TribPtpTribDisableAction_Object=MibTableColumn
tribPtpTribDisableAction=_TribPtpTribDisableAction_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,9),_TribPtpTribDisableAction_Type())
tribPtpTribDisableAction.setMaxAccess(_D)
if mibBuilder.loadTexts:tribPtpTribDisableAction.setStatus(_A)
_TribPtpProvisionedServiceType_Type=InfnServiceType
_TribPtpProvisionedServiceType_Object=MibTableColumn
tribPtpProvisionedServiceType=_TribPtpProvisionedServiceType_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,10),_TribPtpProvisionedServiceType_Type())
tribPtpProvisionedServiceType.setMaxAccess(_D)
if mibBuilder.loadTexts:tribPtpProvisionedServiceType.setStatus(_A)
class _TribPtpOprOorHighThresholdOffset_Type(FloatTenths):defaultValue=0
_TribPtpOprOorHighThresholdOffset_Type.__name__=_F
_TribPtpOprOorHighThresholdOffset_Object=MibTableColumn
tribPtpOprOorHighThresholdOffset=_TribPtpOprOorHighThresholdOffset_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,11),_TribPtpOprOorHighThresholdOffset_Type())
tribPtpOprOorHighThresholdOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:tribPtpOprOorHighThresholdOffset.setStatus(_A)
class _TribPtpOprOorLowThresholdOffset_Type(FloatTenths):defaultValue=0
_TribPtpOprOorLowThresholdOffset_Type.__name__=_F
_TribPtpOprOorLowThresholdOffset_Object=MibTableColumn
tribPtpOprOorLowThresholdOffset=_TribPtpOprOorLowThresholdOffset_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,12),_TribPtpOprOorLowThresholdOffset_Type())
tribPtpOprOorLowThresholdOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:tribPtpOprOorLowThresholdOffset.setStatus(_A)
class _TribPtpOprOorAlarmReporting_Type(InfnReporting):defaultValue=1
_TribPtpOprOorAlarmReporting_Type.__name__=_O
_TribPtpOprOorAlarmReporting_Object=MibTableColumn
tribPtpOprOorAlarmReporting=_TribPtpOprOorAlarmReporting_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,13),_TribPtpOprOorAlarmReporting_Type())
tribPtpOprOorAlarmReporting.setMaxAccess(_D)
if mibBuilder.loadTexts:tribPtpOprOorAlarmReporting.setStatus(_A)
_TribPtpOprOverloadThreshold_Type=FloatTenths
_TribPtpOprOverloadThreshold_Object=MibTableColumn
tribPtpOprOverloadThreshold=_TribPtpOprOverloadThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,14),_TribPtpOprOverloadThreshold_Type())
tribPtpOprOverloadThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpOprOverloadThreshold.setStatus(_A)
_TribPtpOprSensitivityThreshold_Type=FloatTenths
_TribPtpOprSensitivityThreshold_Object=MibTableColumn
tribPtpOprSensitivityThreshold=_TribPtpOprSensitivityThreshold_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,15),_TribPtpOprSensitivityThreshold_Type())
tribPtpOprSensitivityThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpOprSensitivityThreshold.setStatus(_A)
class _TribPtpAINS_Type(InfnOperationalState):defaultValue=1
_TribPtpAINS_Type.__name__=_G
_TribPtpAINS_Object=MibTableColumn
tribPtpAINS=_TribPtpAINS_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,16),_TribPtpAINS_Type())
tribPtpAINS.setMaxAccess(_D)
if mibBuilder.loadTexts:tribPtpAINS.setStatus(_A)
class _TribPtpValidSignalTimeInterval_Type(Integer32):defaultValue=480
_TribPtpValidSignalTimeInterval_Type.__name__=_H
_TribPtpValidSignalTimeInterval_Object=MibTableColumn
tribPtpValidSignalTimeInterval=_TribPtpValidSignalTimeInterval_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,17),_TribPtpValidSignalTimeInterval_Type())
tribPtpValidSignalTimeInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:tribPtpValidSignalTimeInterval.setStatus(_A)
_TribPtpRemValidSignalTimer_Type=Integer32
_TribPtpRemValidSignalTimer_Object=MibTableColumn
tribPtpRemValidSignalTimer=_TribPtpRemValidSignalTimer_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,18),_TribPtpRemValidSignalTimer_Type())
tribPtpRemValidSignalTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpRemValidSignalTimer.setStatus(_A)
_TribPtpSupportedServiceTypes_Type=InfnServiceTypeList
_TribPtpSupportedServiceTypes_Object=MibTableColumn
tribPtpSupportedServiceTypes=_TribPtpSupportedServiceTypes_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,19),_TribPtpSupportedServiceTypes_Type())
tribPtpSupportedServiceTypes.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpSupportedServiceTypes.setStatus(_A)
class _TribPtpPmHistStatsEnable_Type(InfnPmHistStatsControl):defaultValue=1
_TribPtpPmHistStatsEnable_Type.__name__=_N
_TribPtpPmHistStatsEnable_Object=MibTableColumn
tribPtpPmHistStatsEnable=_TribPtpPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,20),_TribPtpPmHistStatsEnable_Type())
tribPtpPmHistStatsEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:tribPtpPmHistStatsEnable.setStatus(_A)
_TribPtpMaxAllowedDrops_Type=Integer32
_TribPtpMaxAllowedDrops_Object=MibTableColumn
tribPtpMaxAllowedDrops=_TribPtpMaxAllowedDrops_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,21),_TribPtpMaxAllowedDrops_Type())
tribPtpMaxAllowedDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpMaxAllowedDrops.setStatus(_A)
_TribPtpCurrNumOfDrops_Type=Integer32
_TribPtpCurrNumOfDrops_Object=MibTableColumn
tribPtpCurrNumOfDrops=_TribPtpCurrNumOfDrops_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,22),_TribPtpCurrNumOfDrops_Type())
tribPtpCurrNumOfDrops.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpCurrNumOfDrops.setStatus(_A)
_TribPtpLocalInterfaceIndex_Type=Integer32
_TribPtpLocalInterfaceIndex_Object=MibTableColumn
tribPtpLocalInterfaceIndex=_TribPtpLocalInterfaceIndex_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,23),_TribPtpLocalInterfaceIndex_Type())
tribPtpLocalInterfaceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpLocalInterfaceIndex.setStatus(_A)
class _TribPtpRemoteInterfaceIndex_Type(Integer32):defaultValue=0
_TribPtpRemoteInterfaceIndex_Type.__name__=_H
_TribPtpRemoteInterfaceIndex_Object=MibTableColumn
tribPtpRemoteInterfaceIndex=_TribPtpRemoteInterfaceIndex_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,24),_TribPtpRemoteInterfaceIndex_Type())
tribPtpRemoteInterfaceIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:tribPtpRemoteInterfaceIndex.setStatus(_A)
_TribPtpAssocMoInteropCPTEInterface_Type=DisplayString
_TribPtpAssocMoInteropCPTEInterface_Object=MibTableColumn
tribPtpAssocMoInteropCPTEInterface=_TribPtpAssocMoInteropCPTEInterface_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,25),_TribPtpAssocMoInteropCPTEInterface_Type())
tribPtpAssocMoInteropCPTEInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpAssocMoInteropCPTEInterface.setStatus(_A)
class _TribPtpDtpAISOnClientSF_Type(InfnOperationalState):defaultValue=1
_TribPtpDtpAISOnClientSF_Type.__name__=_G
_TribPtpDtpAISOnClientSF_Object=MibTableColumn
tribPtpDtpAISOnClientSF=_TribPtpDtpAISOnClientSF_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,26),_TribPtpDtpAISOnClientSF_Type())
tribPtpDtpAISOnClientSF.setMaxAccess(_D)
if mibBuilder.loadTexts:tribPtpDtpAISOnClientSF.setStatus(_A)
class _TribPtpEnetPswLaserCtrl_Type(InfnEnetPswLaserCtrlState):defaultValue=1
_TribPtpEnetPswLaserCtrl_Type.__name__=_M
_TribPtpEnetPswLaserCtrl_Object=MibTableColumn
tribPtpEnetPswLaserCtrl=_TribPtpEnetPswLaserCtrl_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,27),_TribPtpEnetPswLaserCtrl_Type())
tribPtpEnetPswLaserCtrl.setMaxAccess(_D)
if mibBuilder.loadTexts:tribPtpEnetPswLaserCtrl.setStatus(_A)
class _TribPtpDisableActionOnBERSF_Type(InfnEnableDisable):defaultValue=1
_TribPtpDisableActionOnBERSF_Type.__name__=_E
_TribPtpDisableActionOnBERSF_Object=MibTableColumn
tribPtpDisableActionOnBERSF=_TribPtpDisableActionOnBERSF_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,28),_TribPtpDisableActionOnBERSF_Type())
tribPtpDisableActionOnBERSF.setMaxAccess(_D)
if mibBuilder.loadTexts:tribPtpDisableActionOnBERSF.setStatus(_A)
class _TribPtpAutoCableEqualization_Type(InfnAutoCableEqualization):defaultValue=1
_TribPtpAutoCableEqualization_Type.__name__=_K
_TribPtpAutoCableEqualization_Object=MibTableColumn
tribPtpAutoCableEqualization=_TribPtpAutoCableEqualization_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,29),_TribPtpAutoCableEqualization_Type())
tribPtpAutoCableEqualization.setMaxAccess(_D)
if mibBuilder.loadTexts:tribPtpAutoCableEqualization.setStatus(_A)
class _TribPtpDirectionality_Type(InfnDirectionality):defaultValue=3
_TribPtpDirectionality_Type.__name__=_L
_TribPtpDirectionality_Object=MibTableColumn
tribPtpDirectionality=_TribPtpDirectionality_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,30),_TribPtpDirectionality_Type())
tribPtpDirectionality.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpDirectionality.setStatus(_A)
_TribPtpInterfaceType_Type=InfnInterfaceType
_TribPtpInterfaceType_Object=MibTableColumn
tribPtpInterfaceType=_TribPtpInterfaceType_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,31),_TribPtpInterfaceType_Type())
tribPtpInterfaceType.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpInterfaceType.setStatus(_A)
class _TribPtpAutoDiscovery_Type(InfnEnableDisable):defaultValue=2
_TribPtpAutoDiscovery_Type.__name__=_E
_TribPtpAutoDiscovery_Object=MibTableColumn
tribPtpAutoDiscovery=_TribPtpAutoDiscovery_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,32),_TribPtpAutoDiscovery_Type())
tribPtpAutoDiscovery.setMaxAccess(_D)
if mibBuilder.loadTexts:tribPtpAutoDiscovery.setStatus(_A)
_TribPtpDiscoveredRemoteTP_Type=DisplayString
_TribPtpDiscoveredRemoteTP_Object=MibTableColumn
tribPtpDiscoveredRemoteTP=_TribPtpDiscoveredRemoteTP_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,33),_TribPtpDiscoveredRemoteTP_Type())
tribPtpDiscoveredRemoteTP.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpDiscoveredRemoteTP.setStatus(_A)
_TribPtpProvisionedRemoteTP_Type=DisplayString
_TribPtpProvisionedRemoteTP_Object=MibTableColumn
tribPtpProvisionedRemoteTP=_TribPtpProvisionedRemoteTP_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,34),_TribPtpProvisionedRemoteTP_Type())
tribPtpProvisionedRemoteTP.setMaxAccess(_D)
if mibBuilder.loadTexts:tribPtpProvisionedRemoteTP.setStatus(_A)
class _TribPtpForwardDefectTDATrigger_Type(InfnEnableDisable):defaultValue=1
_TribPtpForwardDefectTDATrigger_Type.__name__=_E
_TribPtpForwardDefectTDATrigger_Object=MibTableColumn
tribPtpForwardDefectTDATrigger=_TribPtpForwardDefectTDATrigger_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,35),_TribPtpForwardDefectTDATrigger_Type())
tribPtpForwardDefectTDATrigger.setMaxAccess(_D)
if mibBuilder.loadTexts:tribPtpForwardDefectTDATrigger.setStatus(_A)
_TribPtpProvisionedFecEncodingMode_Type=InfnFecEncodingMode
_TribPtpProvisionedFecEncodingMode_Object=MibTableColumn
tribPtpProvisionedFecEncodingMode=_TribPtpProvisionedFecEncodingMode_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,36),_TribPtpProvisionedFecEncodingMode_Type())
tribPtpProvisionedFecEncodingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:tribPtpProvisionedFecEncodingMode.setStatus(_A)
_TribPtpAppliedFecEncodingMode_Type=InfnFecEncodingMode
_TribPtpAppliedFecEncodingMode_Object=MibTableColumn
tribPtpAppliedFecEncodingMode=_TribPtpAppliedFecEncodingMode_Object((1,3,6,1,4,1,21296,2,2,2,2,17,1,1,37),_TribPtpAppliedFecEncodingMode_Type())
tribPtpAppliedFecEncodingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tribPtpAppliedFecEncodingMode.setStatus(_A)
_TribPtpConformance_ObjectIdentity=ObjectIdentity
tribPtpConformance=_TribPtpConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,17,3))
_TribPtpCompliances_ObjectIdentity=ObjectIdentity
tribPtpCompliances=_TribPtpCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,17,3,1))
_TribPtpGroups_ObjectIdentity=ObjectIdentity
tribPtpGroups=_TribPtpGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,17,3,2))
tribPtpGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,17,3,2,1))
tribPtpGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:tribPtpGroup.setStatus(_A)
tribPtpCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,17,3,1,1))
tribPtpCompliance.setObjects((_B,_A1))
if mibBuilder.loadTexts:tribPtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'tribPtpMIB':tribPtpMIB,'tribPtpTable':tribPtpTable,'tribPtpEntry':tribPtpEntry,_Q:tribPtpPgMoId,_R:tribPtpProtMod,_S:tribPtpCfgProtSt,_T:tribPtpCurProtSt,_U:tribPtpPsDirn,_V:tribPtpSwReason,_W:tribPtpSwRqState,_X:tribPtpMaxPerChannelCapacity,_Y:tribPtpTribDisableAction,_Z:tribPtpProvisionedServiceType,_a:tribPtpOprOorHighThresholdOffset,_b:tribPtpOprOorLowThresholdOffset,_c:tribPtpOprOorAlarmReporting,_d:tribPtpOprOverloadThreshold,_e:tribPtpOprSensitivityThreshold,_f:tribPtpAINS,_g:tribPtpValidSignalTimeInterval,_h:tribPtpRemValidSignalTimer,_i:tribPtpSupportedServiceTypes,_j:tribPtpPmHistStatsEnable,_k:tribPtpMaxAllowedDrops,_l:tribPtpCurrNumOfDrops,_m:tribPtpLocalInterfaceIndex,_n:tribPtpRemoteInterfaceIndex,_o:tribPtpAssocMoInteropCPTEInterface,_p:tribPtpDtpAISOnClientSF,_q:tribPtpEnetPswLaserCtrl,_r:tribPtpDisableActionOnBERSF,_s:tribPtpAutoCableEqualization,_t:tribPtpDirectionality,_u:tribPtpInterfaceType,_v:tribPtpAutoDiscovery,_w:tribPtpDiscoveredRemoteTP,_x:tribPtpProvisionedRemoteTP,_y:tribPtpForwardDefectTDATrigger,_z:tribPtpProvisionedFecEncodingMode,_A0:tribPtpAppliedFecEncodingMode,'tribPtpConformance':tribPtpConformance,'tribPtpCompliances':tribPtpCompliances,'tribPtpCompliance':tribPtpCompliance,'tribPtpGroups':tribPtpGroups,_A1:tribPtpGroup})