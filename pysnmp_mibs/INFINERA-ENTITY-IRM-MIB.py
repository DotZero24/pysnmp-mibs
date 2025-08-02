_q='irmGroup'
_p='irmRxEDFAGain'
_o='irmALSDisableMode'
_n='irmSingleSlotMode'
_m='irmLimitPower'
_l='irmTxVOA'
_k='irmRamanTiltOffset'
_j='irmRamanGain'
_i='irmDeploymentConfig'
_h='irmOperatingMode'
_g='irmOlosSoakTime'
_f='irmGainTiltOffset'
_e='irmPilotLaserDisable'
_d='irmALSDetectionMode'
_c='irmTxDampSeqNum'
_b='irmStaticPostEdfaVoaAttenuation'
_a='irmStaticEdfaGain'
_Z='irmStaticRamanGain'
_Y='irmPumpRatioPump4'
_X='irmPumpRatioPump3'
_W='irmPumpRatioPump2'
_V='irmPumpRatioPump1'
_U='irmPumpPowerBetaCoeffZ'
_T='irmPumpPowerBetaCoeffY'
_S='irmPumpPowerBetaCoeffX'
_R='irmAsePowerBetaCoeffZ'
_Q='irmAsePowerBetaCoeffY'
_P='irmAsePowerBetaCoeffX'
_O='irmFiberType'
_N='irmAutomaticPLOAdjustmen'
_M='irmEnhPMRept'
_L='irmRxDampSeqNum'
_K='irmLaunchPowerOffset'
_J='irmPointLossOffset'
_I='irmProvEqptType'
_H='irmMoId'
_G='read-only'
_F='entLPPhysicalIndex'
_E='ENTITY-MIB'
_D='read-write'
_C='read-create'
_B='INFINERA-ENTITY-IRM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entLPPhysicalIndex,=mibBuilder.importSymbols(_E,_F)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
FloatArbitraryPrecision,FloatHundredths,InfnALSDetectionMode,InfnALSDisableMode,InfnDeploymentConfig,InfnEnableDisable,InfnEqptType,InfnFiberType,InfnOAOperatingMode,InfnOlosSoakTime=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatArbitraryPrecision','FloatHundredths','InfnALSDetectionMode','InfnALSDisableMode','InfnDeploymentConfig','InfnEnableDisable','InfnEqptType','InfnFiberType','InfnOAOperatingMode','InfnOlosSoakTime')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
irmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,29))
_IrmTable_Object=MibTable
irmTable=_IrmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1))
if mibBuilder.loadTexts:irmTable.setStatus(_A)
_IrmEntry_Object=MibTableRow
irmEntry=_IrmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1))
irmEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:irmEntry.setStatus(_A)
_IrmMoId_Type=DisplayString
_IrmMoId_Object=MibTableColumn
irmMoId=_IrmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,1),_IrmMoId_Type())
irmMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:irmMoId.setStatus(_A)
_IrmProvEqptType_Type=InfnEqptType
_IrmProvEqptType_Object=MibTableColumn
irmProvEqptType=_IrmProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,2),_IrmProvEqptType_Type())
irmProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:irmProvEqptType.setStatus(_A)
_IrmPointLossOffset_Type=FloatHundredths
_IrmPointLossOffset_Object=MibTableColumn
irmPointLossOffset=_IrmPointLossOffset_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,3),_IrmPointLossOffset_Type())
irmPointLossOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:irmPointLossOffset.setStatus(_A)
_IrmLaunchPowerOffset_Type=FloatHundredths
_IrmLaunchPowerOffset_Object=MibTableColumn
irmLaunchPowerOffset=_IrmLaunchPowerOffset_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,4),_IrmLaunchPowerOffset_Type())
irmLaunchPowerOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:irmLaunchPowerOffset.setStatus(_A)
_IrmRxDampSeqNum_Type=Integer32
_IrmRxDampSeqNum_Object=MibTableColumn
irmRxDampSeqNum=_IrmRxDampSeqNum_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,5),_IrmRxDampSeqNum_Type())
irmRxDampSeqNum.setMaxAccess(_G)
if mibBuilder.loadTexts:irmRxDampSeqNum.setStatus(_A)
_IrmTxDampSeqNum_Type=Integer32
_IrmTxDampSeqNum_Object=MibTableColumn
irmTxDampSeqNum=_IrmTxDampSeqNum_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,6),_IrmTxDampSeqNum_Type())
irmTxDampSeqNum.setMaxAccess(_G)
if mibBuilder.loadTexts:irmTxDampSeqNum.setStatus(_A)
_IrmPilotLaserDisable_Type=TruthValue
_IrmPilotLaserDisable_Object=MibTableColumn
irmPilotLaserDisable=_IrmPilotLaserDisable_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,7),_IrmPilotLaserDisable_Type())
irmPilotLaserDisable.setMaxAccess(_D)
if mibBuilder.loadTexts:irmPilotLaserDisable.setStatus(_A)
_IrmEnhPMRept_Type=InfnEnableDisable
_IrmEnhPMRept_Object=MibTableColumn
irmEnhPMRept=_IrmEnhPMRept_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,8),_IrmEnhPMRept_Type())
irmEnhPMRept.setMaxAccess(_C)
if mibBuilder.loadTexts:irmEnhPMRept.setStatus(_A)
_IrmALSDetectionMode_Type=InfnALSDetectionMode
_IrmALSDetectionMode_Object=MibTableColumn
irmALSDetectionMode=_IrmALSDetectionMode_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,9),_IrmALSDetectionMode_Type())
irmALSDetectionMode.setMaxAccess(_D)
if mibBuilder.loadTexts:irmALSDetectionMode.setStatus(_A)
_IrmAutomaticPLOAdjustmen_Type=InfnEnableDisable
_IrmAutomaticPLOAdjustmen_Object=MibTableColumn
irmAutomaticPLOAdjustmen=_IrmAutomaticPLOAdjustmen_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,10),_IrmAutomaticPLOAdjustmen_Type())
irmAutomaticPLOAdjustmen.setMaxAccess(_C)
if mibBuilder.loadTexts:irmAutomaticPLOAdjustmen.setStatus(_A)
_IrmAsePowerBetaCoeffX_Type=FloatHundredths
_IrmAsePowerBetaCoeffX_Object=MibTableColumn
irmAsePowerBetaCoeffX=_IrmAsePowerBetaCoeffX_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,11),_IrmAsePowerBetaCoeffX_Type())
irmAsePowerBetaCoeffX.setMaxAccess(_C)
if mibBuilder.loadTexts:irmAsePowerBetaCoeffX.setStatus(_A)
_IrmAsePowerBetaCoeffY_Type=FloatHundredths
_IrmAsePowerBetaCoeffY_Object=MibTableColumn
irmAsePowerBetaCoeffY=_IrmAsePowerBetaCoeffY_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,12),_IrmAsePowerBetaCoeffY_Type())
irmAsePowerBetaCoeffY.setMaxAccess(_C)
if mibBuilder.loadTexts:irmAsePowerBetaCoeffY.setStatus(_A)
_IrmAsePowerBetaCoeffZ_Type=FloatHundredths
_IrmAsePowerBetaCoeffZ_Object=MibTableColumn
irmAsePowerBetaCoeffZ=_IrmAsePowerBetaCoeffZ_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,13),_IrmAsePowerBetaCoeffZ_Type())
irmAsePowerBetaCoeffZ.setMaxAccess(_C)
if mibBuilder.loadTexts:irmAsePowerBetaCoeffZ.setStatus(_A)
_IrmPumpPowerBetaCoeffX_Type=FloatHundredths
_IrmPumpPowerBetaCoeffX_Object=MibTableColumn
irmPumpPowerBetaCoeffX=_IrmPumpPowerBetaCoeffX_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,14),_IrmPumpPowerBetaCoeffX_Type())
irmPumpPowerBetaCoeffX.setMaxAccess(_C)
if mibBuilder.loadTexts:irmPumpPowerBetaCoeffX.setStatus(_A)
_IrmPumpPowerBetaCoeffY_Type=FloatHundredths
_IrmPumpPowerBetaCoeffY_Object=MibTableColumn
irmPumpPowerBetaCoeffY=_IrmPumpPowerBetaCoeffY_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,15),_IrmPumpPowerBetaCoeffY_Type())
irmPumpPowerBetaCoeffY.setMaxAccess(_C)
if mibBuilder.loadTexts:irmPumpPowerBetaCoeffY.setStatus(_A)
_IrmPumpPowerBetaCoeffZ_Type=FloatHundredths
_IrmPumpPowerBetaCoeffZ_Object=MibTableColumn
irmPumpPowerBetaCoeffZ=_IrmPumpPowerBetaCoeffZ_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,16),_IrmPumpPowerBetaCoeffZ_Type())
irmPumpPowerBetaCoeffZ.setMaxAccess(_C)
if mibBuilder.loadTexts:irmPumpPowerBetaCoeffZ.setStatus(_A)
_IrmPumpRatioPump1_Type=FloatHundredths
_IrmPumpRatioPump1_Object=MibTableColumn
irmPumpRatioPump1=_IrmPumpRatioPump1_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,17),_IrmPumpRatioPump1_Type())
irmPumpRatioPump1.setMaxAccess(_C)
if mibBuilder.loadTexts:irmPumpRatioPump1.setStatus(_A)
_IrmPumpRatioPump2_Type=FloatHundredths
_IrmPumpRatioPump2_Object=MibTableColumn
irmPumpRatioPump2=_IrmPumpRatioPump2_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,18),_IrmPumpRatioPump2_Type())
irmPumpRatioPump2.setMaxAccess(_C)
if mibBuilder.loadTexts:irmPumpRatioPump2.setStatus(_A)
_IrmPumpRatioPump3_Type=FloatHundredths
_IrmPumpRatioPump3_Object=MibTableColumn
irmPumpRatioPump3=_IrmPumpRatioPump3_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,19),_IrmPumpRatioPump3_Type())
irmPumpRatioPump3.setMaxAccess(_C)
if mibBuilder.loadTexts:irmPumpRatioPump3.setStatus(_A)
_IrmPumpRatioPump4_Type=FloatHundredths
_IrmPumpRatioPump4_Object=MibTableColumn
irmPumpRatioPump4=_IrmPumpRatioPump4_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,20),_IrmPumpRatioPump4_Type())
irmPumpRatioPump4.setMaxAccess(_C)
if mibBuilder.loadTexts:irmPumpRatioPump4.setStatus(_A)
_IrmStaticRamanGain_Type=FloatHundredths
_IrmStaticRamanGain_Object=MibTableColumn
irmStaticRamanGain=_IrmStaticRamanGain_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,21),_IrmStaticRamanGain_Type())
irmStaticRamanGain.setMaxAccess(_C)
if mibBuilder.loadTexts:irmStaticRamanGain.setStatus(_A)
_IrmStaticEdfaGain_Type=FloatHundredths
_IrmStaticEdfaGain_Object=MibTableColumn
irmStaticEdfaGain=_IrmStaticEdfaGain_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,22),_IrmStaticEdfaGain_Type())
irmStaticEdfaGain.setMaxAccess(_C)
if mibBuilder.loadTexts:irmStaticEdfaGain.setStatus(_A)
_IrmStaticPostEdfaVoaAttenuation_Type=FloatHundredths
_IrmStaticPostEdfaVoaAttenuation_Object=MibTableColumn
irmStaticPostEdfaVoaAttenuation=_IrmStaticPostEdfaVoaAttenuation_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,23),_IrmStaticPostEdfaVoaAttenuation_Type())
irmStaticPostEdfaVoaAttenuation.setMaxAccess(_C)
if mibBuilder.loadTexts:irmStaticPostEdfaVoaAttenuation.setStatus(_A)
_IrmFiberType_Type=InfnFiberType
_IrmFiberType_Object=MibTableColumn
irmFiberType=_IrmFiberType_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,24),_IrmFiberType_Type())
irmFiberType.setMaxAccess(_C)
if mibBuilder.loadTexts:irmFiberType.setStatus(_A)
_IrmGainTiltOffset_Type=FloatHundredths
_IrmGainTiltOffset_Object=MibTableColumn
irmGainTiltOffset=_IrmGainTiltOffset_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,25),_IrmGainTiltOffset_Type())
irmGainTiltOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:irmGainTiltOffset.setStatus(_A)
_IrmOlosSoakTime_Type=InfnOlosSoakTime
_IrmOlosSoakTime_Object=MibTableColumn
irmOlosSoakTime=_IrmOlosSoakTime_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,26),_IrmOlosSoakTime_Type())
irmOlosSoakTime.setMaxAccess(_D)
if mibBuilder.loadTexts:irmOlosSoakTime.setStatus(_A)
_IrmOperatingMode_Type=InfnOAOperatingMode
_IrmOperatingMode_Object=MibTableColumn
irmOperatingMode=_IrmOperatingMode_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,27),_IrmOperatingMode_Type())
irmOperatingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:irmOperatingMode.setStatus(_A)
_IrmDeploymentConfig_Type=InfnDeploymentConfig
_IrmDeploymentConfig_Object=MibTableColumn
irmDeploymentConfig=_IrmDeploymentConfig_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,28),_IrmDeploymentConfig_Type())
irmDeploymentConfig.setMaxAccess(_D)
if mibBuilder.loadTexts:irmDeploymentConfig.setStatus(_A)
_IrmRamanGain_Type=FloatArbitraryPrecision
_IrmRamanGain_Object=MibTableColumn
irmRamanGain=_IrmRamanGain_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,29),_IrmRamanGain_Type())
irmRamanGain.setMaxAccess(_D)
if mibBuilder.loadTexts:irmRamanGain.setStatus(_A)
_IrmRamanTiltOffset_Type=FloatArbitraryPrecision
_IrmRamanTiltOffset_Object=MibTableColumn
irmRamanTiltOffset=_IrmRamanTiltOffset_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,30),_IrmRamanTiltOffset_Type())
irmRamanTiltOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:irmRamanTiltOffset.setStatus(_A)
_IrmTxVOA_Type=FloatArbitraryPrecision
_IrmTxVOA_Object=MibTableColumn
irmTxVOA=_IrmTxVOA_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,31),_IrmTxVOA_Type())
irmTxVOA.setMaxAccess(_D)
if mibBuilder.loadTexts:irmTxVOA.setStatus(_A)
_IrmLimitPower_Type=InfnEnableDisable
_IrmLimitPower_Object=MibTableColumn
irmLimitPower=_IrmLimitPower_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,32),_IrmLimitPower_Type())
irmLimitPower.setMaxAccess(_D)
if mibBuilder.loadTexts:irmLimitPower.setStatus(_A)
_IrmSingleSlotMode_Type=InfnEnableDisable
_IrmSingleSlotMode_Object=MibTableColumn
irmSingleSlotMode=_IrmSingleSlotMode_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,33),_IrmSingleSlotMode_Type())
irmSingleSlotMode.setMaxAccess(_D)
if mibBuilder.loadTexts:irmSingleSlotMode.setStatus(_A)
_IrmALSDisableMode_Type=InfnALSDisableMode
_IrmALSDisableMode_Object=MibTableColumn
irmALSDisableMode=_IrmALSDisableMode_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,34),_IrmALSDisableMode_Type())
irmALSDisableMode.setMaxAccess(_D)
if mibBuilder.loadTexts:irmALSDisableMode.setStatus(_A)
_IrmRxEDFAGain_Type=FloatArbitraryPrecision
_IrmRxEDFAGain_Object=MibTableColumn
irmRxEDFAGain=_IrmRxEDFAGain_Object((1,3,6,1,4,1,21296,2,2,2,1,29,1,1,35),_IrmRxEDFAGain_Type())
irmRxEDFAGain.setMaxAccess(_D)
if mibBuilder.loadTexts:irmRxEDFAGain.setStatus(_A)
_IrmConformance_ObjectIdentity=ObjectIdentity
irmConformance=_IrmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,29,3))
_IrmCompliances_ObjectIdentity=ObjectIdentity
irmCompliances=_IrmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,29,3,1))
_IrmGroups_ObjectIdentity=ObjectIdentity
irmGroups=_IrmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,29,3,2))
irmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,29,3,2,1))
irmGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:irmGroup.setStatus(_A)
irmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,29,3,1,1))
irmCompliance.setObjects((_B,_q))
if mibBuilder.loadTexts:irmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'irmMIB':irmMIB,'irmTable':irmTable,'irmEntry':irmEntry,_H:irmMoId,_I:irmProvEqptType,_J:irmPointLossOffset,_K:irmLaunchPowerOffset,_L:irmRxDampSeqNum,_c:irmTxDampSeqNum,_e:irmPilotLaserDisable,_M:irmEnhPMRept,_d:irmALSDetectionMode,_N:irmAutomaticPLOAdjustmen,_P:irmAsePowerBetaCoeffX,_Q:irmAsePowerBetaCoeffY,_R:irmAsePowerBetaCoeffZ,_S:irmPumpPowerBetaCoeffX,_T:irmPumpPowerBetaCoeffY,_U:irmPumpPowerBetaCoeffZ,_V:irmPumpRatioPump1,_W:irmPumpRatioPump2,_X:irmPumpRatioPump3,_Y:irmPumpRatioPump4,_Z:irmStaticRamanGain,_a:irmStaticEdfaGain,_b:irmStaticPostEdfaVoaAttenuation,_O:irmFiberType,_f:irmGainTiltOffset,_g:irmOlosSoakTime,_h:irmOperatingMode,_i:irmDeploymentConfig,_j:irmRamanGain,_k:irmRamanTiltOffset,_l:irmTxVOA,_m:irmLimitPower,_n:irmSingleSlotMode,_o:irmALSDisableMode,_p:irmRxEDFAGain,'irmConformance':irmConformance,'irmCompliances':irmCompliances,'irmCompliance':irmCompliance,'irmGroups':irmGroups,_q:irmGroup})