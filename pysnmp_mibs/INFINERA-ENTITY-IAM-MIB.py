_j='iamGroup'
_i='iamOSCState'
_h='iamDeploymentConfig'
_g='iamCBandSoakCapableFW'
_f='iamGainTiltOffset'
_e='iamIlRxLineInToEdfa'
_d='iamRxLastAmpDeviceCommitTs'
_c='iamRxAmpDeviceTarget'
_b='iamRxAmpDeviceSetpoint'
_a='iamSlotOperatingMode'
_Z='iamisEqptMisMatchStateIsSet'
_Y='iamGainRangeHigh'
_X='iamGainRangeLow'
_W='iamMidStageAccess'
_V='iamGainType'
_U='iamGain'
_T='iamAssociatedDegree'
_S='iamTxVOA'
_R='iamTargetLineOutputPower'
_Q='iamRxEDFATargetOpt'
_P='iamALSDisableMode'
_O='iamOlosSoakTime'
_N='iamTxDampSeqNum'
_M='iamStaticVoaAttenuation'
_L='iamRxDampSeqNum'
_K='iamLaunchPowerOffset'
_J='iamProvEqptType'
_I='iamMoId'
_H='entLPPhysicalIndex'
_G='ENTITY-MIB'
_F='iamOperatingMode'
_E='read-create'
_D='read-only'
_C='read-write'
_B='INFINERA-ENTITY-IAM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_G,_H)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
FloatTenths,InfnALSDisableMode,InfnDeploymentConfig,InfnEnableDisable,InfnEqptType,InfnMidStageAccess,InfnOAOperatingMode,InfnOASlotOperatingMode,InfnOTSGainType,InfnOlosSoakTime=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatTenths','InfnALSDisableMode','InfnDeploymentConfig','InfnEnableDisable','InfnEqptType','InfnMidStageAccess','InfnOAOperatingMode','InfnOASlotOperatingMode','InfnOTSGainType','InfnOlosSoakTime')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
iamMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,28))
_IamTable_Object=MibTable
iamTable=_IamTable_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1))
if mibBuilder.loadTexts:iamTable.setStatus(_A)
_IamEntry_Object=MibTableRow
iamEntry=_IamEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1))
iamEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:iamEntry.setStatus(_A)
_IamMoId_Type=DisplayString
_IamMoId_Object=MibTableColumn
iamMoId=_IamMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,1),_IamMoId_Type())
iamMoId.setMaxAccess(_E)
if mibBuilder.loadTexts:iamMoId.setStatus(_A)
_IamProvEqptType_Type=InfnEqptType
_IamProvEqptType_Object=MibTableColumn
iamProvEqptType=_IamProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,2),_IamProvEqptType_Type())
iamProvEqptType.setMaxAccess(_E)
if mibBuilder.loadTexts:iamProvEqptType.setStatus(_A)
_IamRxDampSeqNum_Type=Integer32
_IamRxDampSeqNum_Object=MibTableColumn
iamRxDampSeqNum=_IamRxDampSeqNum_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,3),_IamRxDampSeqNum_Type())
iamRxDampSeqNum.setMaxAccess(_D)
if mibBuilder.loadTexts:iamRxDampSeqNum.setStatus(_A)
_IamTxDampSeqNum_Type=Integer32
_IamTxDampSeqNum_Object=MibTableColumn
iamTxDampSeqNum=_IamTxDampSeqNum_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,4),_IamTxDampSeqNum_Type())
iamTxDampSeqNum.setMaxAccess(_D)
if mibBuilder.loadTexts:iamTxDampSeqNum.setStatus(_A)
_IamStaticVoaAttenuation_Type=FloatTenths
_IamStaticVoaAttenuation_Object=MibTableColumn
iamStaticVoaAttenuation=_IamStaticVoaAttenuation_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,5),_IamStaticVoaAttenuation_Type())
iamStaticVoaAttenuation.setMaxAccess(_E)
if mibBuilder.loadTexts:iamStaticVoaAttenuation.setStatus(_A)
_IamOlosSoakTime_Type=InfnOlosSoakTime
_IamOlosSoakTime_Object=MibTableColumn
iamOlosSoakTime=_IamOlosSoakTime_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,6),_IamOlosSoakTime_Type())
iamOlosSoakTime.setMaxAccess(_C)
if mibBuilder.loadTexts:iamOlosSoakTime.setStatus(_A)
_IamALSDisableMode_Type=InfnALSDisableMode
_IamALSDisableMode_Object=MibTableColumn
iamALSDisableMode=_IamALSDisableMode_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,7),_IamALSDisableMode_Type())
iamALSDisableMode.setMaxAccess(_C)
if mibBuilder.loadTexts:iamALSDisableMode.setStatus(_A)
_IamRxEDFATargetOpt_Type=FloatTenths
_IamRxEDFATargetOpt_Object=MibTableColumn
iamRxEDFATargetOpt=_IamRxEDFATargetOpt_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,8),_IamRxEDFATargetOpt_Type())
iamRxEDFATargetOpt.setMaxAccess(_C)
if mibBuilder.loadTexts:iamRxEDFATargetOpt.setStatus(_A)
_IamTargetLineOutputPower_Type=FloatTenths
_IamTargetLineOutputPower_Object=MibTableColumn
iamTargetLineOutputPower=_IamTargetLineOutputPower_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,9),_IamTargetLineOutputPower_Type())
iamTargetLineOutputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:iamTargetLineOutputPower.setStatus(_A)
_IamTxVOA_Type=FloatTenths
_IamTxVOA_Object=MibTableColumn
iamTxVOA=_IamTxVOA_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,10),_IamTxVOA_Type())
iamTxVOA.setMaxAccess(_C)
if mibBuilder.loadTexts:iamTxVOA.setStatus(_A)
_IamAssociatedDegree_Type=DisplayString
_IamAssociatedDegree_Object=MibTableColumn
iamAssociatedDegree=_IamAssociatedDegree_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,11),_IamAssociatedDegree_Type())
iamAssociatedDegree.setMaxAccess(_C)
if mibBuilder.loadTexts:iamAssociatedDegree.setStatus(_A)
_IamLaunchPowerOffset_Type=FloatTenths
_IamLaunchPowerOffset_Object=MibTableColumn
iamLaunchPowerOffset=_IamLaunchPowerOffset_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,12),_IamLaunchPowerOffset_Type())
iamLaunchPowerOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:iamLaunchPowerOffset.setStatus(_A)
_IamGain_Type=FloatTenths
_IamGain_Object=MibTableColumn
iamGain=_IamGain_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,13),_IamGain_Type())
iamGain.setMaxAccess(_C)
if mibBuilder.loadTexts:iamGain.setStatus(_A)
_IamOperatingMode_Type=InfnOAOperatingMode
_IamOperatingMode_Object=MibTableColumn
iamOperatingMode=_IamOperatingMode_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,14),_IamOperatingMode_Type())
iamOperatingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:iamOperatingMode.setStatus(_A)
_IamGainType_Type=InfnOTSGainType
_IamGainType_Object=MibTableColumn
iamGainType=_IamGainType_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,15),_IamGainType_Type())
iamGainType.setMaxAccess(_D)
if mibBuilder.loadTexts:iamGainType.setStatus(_A)
_IamMidStageAccess_Type=InfnMidStageAccess
_IamMidStageAccess_Object=MibTableColumn
iamMidStageAccess=_IamMidStageAccess_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,16),_IamMidStageAccess_Type())
iamMidStageAccess.setMaxAccess(_D)
if mibBuilder.loadTexts:iamMidStageAccess.setStatus(_A)
_IamGainRangeLow_Type=FloatTenths
_IamGainRangeLow_Object=MibTableColumn
iamGainRangeLow=_IamGainRangeLow_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,17),_IamGainRangeLow_Type())
iamGainRangeLow.setMaxAccess(_D)
if mibBuilder.loadTexts:iamGainRangeLow.setStatus(_A)
_IamGainRangeHigh_Type=FloatTenths
_IamGainRangeHigh_Object=MibTableColumn
iamGainRangeHigh=_IamGainRangeHigh_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,18),_IamGainRangeHigh_Type())
iamGainRangeHigh.setMaxAccess(_D)
if mibBuilder.loadTexts:iamGainRangeHigh.setStatus(_A)
_IamisEqptMisMatchStateIsSet_Type=TruthValue
_IamisEqptMisMatchStateIsSet_Object=MibTableColumn
iamisEqptMisMatchStateIsSet=_IamisEqptMisMatchStateIsSet_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,19),_IamisEqptMisMatchStateIsSet_Type())
iamisEqptMisMatchStateIsSet.setMaxAccess(_D)
if mibBuilder.loadTexts:iamisEqptMisMatchStateIsSet.setStatus(_A)
_IamSlotOperatingMode_Type=InfnOASlotOperatingMode
_IamSlotOperatingMode_Object=MibTableColumn
iamSlotOperatingMode=_IamSlotOperatingMode_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,20),_IamSlotOperatingMode_Type())
iamSlotOperatingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:iamSlotOperatingMode.setStatus(_A)
_IamRxAmpDeviceSetpoint_Type=FloatTenths
_IamRxAmpDeviceSetpoint_Object=MibTableColumn
iamRxAmpDeviceSetpoint=_IamRxAmpDeviceSetpoint_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,21),_IamRxAmpDeviceSetpoint_Type())
iamRxAmpDeviceSetpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:iamRxAmpDeviceSetpoint.setStatus(_A)
_IamRxAmpDeviceTarget_Type=FloatTenths
_IamRxAmpDeviceTarget_Object=MibTableColumn
iamRxAmpDeviceTarget=_IamRxAmpDeviceTarget_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,22),_IamRxAmpDeviceTarget_Type())
iamRxAmpDeviceTarget.setMaxAccess(_D)
if mibBuilder.loadTexts:iamRxAmpDeviceTarget.setStatus(_A)
_IamRxLastAmpDeviceCommitTs_Type=FloatTenths
_IamRxLastAmpDeviceCommitTs_Object=MibTableColumn
iamRxLastAmpDeviceCommitTs=_IamRxLastAmpDeviceCommitTs_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,23),_IamRxLastAmpDeviceCommitTs_Type())
iamRxLastAmpDeviceCommitTs.setMaxAccess(_D)
if mibBuilder.loadTexts:iamRxLastAmpDeviceCommitTs.setStatus(_A)
_IamIlRxLineInToEdfa_Type=FloatTenths
_IamIlRxLineInToEdfa_Object=MibTableColumn
iamIlRxLineInToEdfa=_IamIlRxLineInToEdfa_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,24),_IamIlRxLineInToEdfa_Type())
iamIlRxLineInToEdfa.setMaxAccess(_D)
if mibBuilder.loadTexts:iamIlRxLineInToEdfa.setStatus(_A)
_IamGainTiltOffset_Type=FloatTenths
_IamGainTiltOffset_Object=MibTableColumn
iamGainTiltOffset=_IamGainTiltOffset_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,25),_IamGainTiltOffset_Type())
iamGainTiltOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:iamGainTiltOffset.setStatus(_A)
_IamCBandSoakCapableFW_Type=TruthValue
_IamCBandSoakCapableFW_Object=MibTableColumn
iamCBandSoakCapableFW=_IamCBandSoakCapableFW_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,26),_IamCBandSoakCapableFW_Type())
iamCBandSoakCapableFW.setMaxAccess(_D)
if mibBuilder.loadTexts:iamCBandSoakCapableFW.setStatus(_A)
_IamDeploymentConfig_Type=InfnDeploymentConfig
_IamDeploymentConfig_Object=MibTableColumn
iamDeploymentConfig=_IamDeploymentConfig_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,27),_IamDeploymentConfig_Type())
iamDeploymentConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:iamDeploymentConfig.setStatus(_A)
_IamOSCState_Type=InfnEnableDisable
_IamOSCState_Object=MibTableColumn
iamOSCState=_IamOSCState_Object((1,3,6,1,4,1,21296,2,2,2,1,28,1,1,28),_IamOSCState_Type())
iamOSCState.setMaxAccess(_C)
if mibBuilder.loadTexts:iamOSCState.setStatus(_A)
_IamConformance_ObjectIdentity=ObjectIdentity
iamConformance=_IamConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,28,3))
_IamCompliances_ObjectIdentity=ObjectIdentity
iamCompliances=_IamCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,28,3,1))
_IamGroups_ObjectIdentity=ObjectIdentity
iamGroups=_IamGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,28,3,2))
iamGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,28,3,2,1))
iamGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_F),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_F),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:iamGroup.setStatus(_A)
iamCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,28,3,1,1))
iamCompliance.setObjects((_B,_j))
if mibBuilder.loadTexts:iamCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'iamMIB':iamMIB,'iamTable':iamTable,'iamEntry':iamEntry,_I:iamMoId,_J:iamProvEqptType,_L:iamRxDampSeqNum,_N:iamTxDampSeqNum,_M:iamStaticVoaAttenuation,_O:iamOlosSoakTime,_P:iamALSDisableMode,_Q:iamRxEDFATargetOpt,_R:iamTargetLineOutputPower,_S:iamTxVOA,_T:iamAssociatedDegree,_K:iamLaunchPowerOffset,_U:iamGain,_F:iamOperatingMode,_V:iamGainType,_W:iamMidStageAccess,_X:iamGainRangeLow,_Y:iamGainRangeHigh,_Z:iamisEqptMisMatchStateIsSet,_a:iamSlotOperatingMode,_b:iamRxAmpDeviceSetpoint,_c:iamRxAmpDeviceTarget,_d:iamRxLastAmpDeviceCommitTs,_e:iamIlRxLineInToEdfa,_f:iamGainTiltOffset,_g:iamCBandSoakCapableFW,_h:iamDeploymentConfig,_i:iamOSCState,'iamConformance':iamConformance,'iamCompliances':iamCompliances,'iamCompliance':iamCompliance,'iamGroups':iamGroups,_j:iamGroup})