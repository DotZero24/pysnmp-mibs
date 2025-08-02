_h='ormGroup'
_g='ormFiberType'
_f='ormStaticPostEdfaVoaAttenuation'
_e='ormStaticEdfaGain'
_d='ormStaticRamanGain'
_c='ormPumpRatioPump4'
_b='ormPumpRatioPump3'
_a='ormPumpRatioPump2'
_Z='ormPumpRatioPump1'
_Y='ormPumpPowerBetaCoeffZ'
_X='ormPumpPowerBetaCoeffY'
_W='ormPumpPowerBetaCoeffX'
_V='ormAsePowerBetaCoeffZ'
_U='ormAsePowerBetaCoeffY'
_T='ormAsePowerBetaCoeffX'
_S='ormCBandSoakCapableFW'
_R='ormRowStatus'
_Q='ormEnhPMRept'
_P='ormPointLossOffset'
_O='ormTilt'
_N='ormRxDampSeqNum'
_M='ormLaunchPowerOffset'
_L='ormRxLastAmpDeviceCommitTs'
_K='ormRxAmpDeviceTarget'
_J='ormRxAmpDeviceSetpoint'
_I='ormProvisonedType'
_H='ormMoId'
_G='entPhysicalIndex'
_F='ENTITY-MIB'
_E='read-only'
_D='read-create'
_C='read-write'
_B='INFINERA-ENTITY-ORM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_F,_G)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
FloatHundredths,FloatTenths,InfnEnableDisable,InfnEqptType,InfnFiberType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths','FloatTenths','InfnEnableDisable','InfnEqptType','InfnFiberType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
ormMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,16))
_OrmTable_Object=MibTable
ormTable=_OrmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1))
if mibBuilder.loadTexts:ormTable.setStatus(_A)
_OrmEntry_Object=MibTableRow
ormEntry=_OrmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1))
ormEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:ormEntry.setStatus(_A)
_OrmMoId_Type=DisplayString
_OrmMoId_Object=MibTableColumn
ormMoId=_OrmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,1),_OrmMoId_Type())
ormMoId.setMaxAccess(_D)
if mibBuilder.loadTexts:ormMoId.setStatus(_A)
_OrmProvisonedType_Type=InfnEqptType
_OrmProvisonedType_Object=MibTableColumn
ormProvisonedType=_OrmProvisonedType_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,2),_OrmProvisonedType_Type())
ormProvisonedType.setMaxAccess(_D)
if mibBuilder.loadTexts:ormProvisonedType.setStatus(_A)
_OrmRxAmpDeviceSetpoint_Type=FloatTenths
_OrmRxAmpDeviceSetpoint_Object=MibTableColumn
ormRxAmpDeviceSetpoint=_OrmRxAmpDeviceSetpoint_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,3),_OrmRxAmpDeviceSetpoint_Type())
ormRxAmpDeviceSetpoint.setMaxAccess(_E)
if mibBuilder.loadTexts:ormRxAmpDeviceSetpoint.setStatus(_A)
_OrmRxAmpDeviceTarget_Type=FloatTenths
_OrmRxAmpDeviceTarget_Object=MibTableColumn
ormRxAmpDeviceTarget=_OrmRxAmpDeviceTarget_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,4),_OrmRxAmpDeviceTarget_Type())
ormRxAmpDeviceTarget.setMaxAccess(_E)
if mibBuilder.loadTexts:ormRxAmpDeviceTarget.setStatus(_A)
_OrmRxLastAmpDeviceCommitTs_Type=Integer32
_OrmRxLastAmpDeviceCommitTs_Object=MibTableColumn
ormRxLastAmpDeviceCommitTs=_OrmRxLastAmpDeviceCommitTs_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,5),_OrmRxLastAmpDeviceCommitTs_Type())
ormRxLastAmpDeviceCommitTs.setMaxAccess(_E)
if mibBuilder.loadTexts:ormRxLastAmpDeviceCommitTs.setStatus(_A)
_OrmLaunchPowerOffset_Type=FloatTenths
_OrmLaunchPowerOffset_Object=MibTableColumn
ormLaunchPowerOffset=_OrmLaunchPowerOffset_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,6),_OrmLaunchPowerOffset_Type())
ormLaunchPowerOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:ormLaunchPowerOffset.setStatus(_A)
_OrmRxDampSeqNum_Type=Integer32
_OrmRxDampSeqNum_Object=MibTableColumn
ormRxDampSeqNum=_OrmRxDampSeqNum_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,7),_OrmRxDampSeqNum_Type())
ormRxDampSeqNum.setMaxAccess(_E)
if mibBuilder.loadTexts:ormRxDampSeqNum.setStatus(_A)
_OrmTilt_Type=FloatTenths
_OrmTilt_Object=MibTableColumn
ormTilt=_OrmTilt_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,8),_OrmTilt_Type())
ormTilt.setMaxAccess(_D)
if mibBuilder.loadTexts:ormTilt.setStatus(_A)
_OrmPointLossOffset_Type=FloatTenths
_OrmPointLossOffset_Object=MibTableColumn
ormPointLossOffset=_OrmPointLossOffset_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,9),_OrmPointLossOffset_Type())
ormPointLossOffset.setMaxAccess(_D)
if mibBuilder.loadTexts:ormPointLossOffset.setStatus(_A)
_OrmEnhPMRept_Type=InfnEnableDisable
_OrmEnhPMRept_Object=MibTableColumn
ormEnhPMRept=_OrmEnhPMRept_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,10),_OrmEnhPMRept_Type())
ormEnhPMRept.setMaxAccess(_D)
if mibBuilder.loadTexts:ormEnhPMRept.setStatus(_A)
_OrmRowStatus_Type=RowStatus
_OrmRowStatus_Object=MibTableColumn
ormRowStatus=_OrmRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,11),_OrmRowStatus_Type())
ormRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ormRowStatus.setStatus(_A)
_OrmCBandSoakCapableFW_Type=TruthValue
_OrmCBandSoakCapableFW_Object=MibTableColumn
ormCBandSoakCapableFW=_OrmCBandSoakCapableFW_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,12),_OrmCBandSoakCapableFW_Type())
ormCBandSoakCapableFW.setMaxAccess(_E)
if mibBuilder.loadTexts:ormCBandSoakCapableFW.setStatus(_A)
_OrmAsePowerBetaCoeffX_Type=FloatHundredths
_OrmAsePowerBetaCoeffX_Object=MibTableColumn
ormAsePowerBetaCoeffX=_OrmAsePowerBetaCoeffX_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,13),_OrmAsePowerBetaCoeffX_Type())
ormAsePowerBetaCoeffX.setMaxAccess(_C)
if mibBuilder.loadTexts:ormAsePowerBetaCoeffX.setStatus(_A)
_OrmAsePowerBetaCoeffY_Type=FloatHundredths
_OrmAsePowerBetaCoeffY_Object=MibTableColumn
ormAsePowerBetaCoeffY=_OrmAsePowerBetaCoeffY_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,14),_OrmAsePowerBetaCoeffY_Type())
ormAsePowerBetaCoeffY.setMaxAccess(_C)
if mibBuilder.loadTexts:ormAsePowerBetaCoeffY.setStatus(_A)
_OrmAsePowerBetaCoeffZ_Type=FloatHundredths
_OrmAsePowerBetaCoeffZ_Object=MibTableColumn
ormAsePowerBetaCoeffZ=_OrmAsePowerBetaCoeffZ_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,15),_OrmAsePowerBetaCoeffZ_Type())
ormAsePowerBetaCoeffZ.setMaxAccess(_C)
if mibBuilder.loadTexts:ormAsePowerBetaCoeffZ.setStatus(_A)
_OrmPumpPowerBetaCoeffX_Type=FloatHundredths
_OrmPumpPowerBetaCoeffX_Object=MibTableColumn
ormPumpPowerBetaCoeffX=_OrmPumpPowerBetaCoeffX_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,16),_OrmPumpPowerBetaCoeffX_Type())
ormPumpPowerBetaCoeffX.setMaxAccess(_C)
if mibBuilder.loadTexts:ormPumpPowerBetaCoeffX.setStatus(_A)
_OrmPumpPowerBetaCoeffY_Type=FloatHundredths
_OrmPumpPowerBetaCoeffY_Object=MibTableColumn
ormPumpPowerBetaCoeffY=_OrmPumpPowerBetaCoeffY_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,17),_OrmPumpPowerBetaCoeffY_Type())
ormPumpPowerBetaCoeffY.setMaxAccess(_C)
if mibBuilder.loadTexts:ormPumpPowerBetaCoeffY.setStatus(_A)
_OrmPumpPowerBetaCoeffZ_Type=FloatHundredths
_OrmPumpPowerBetaCoeffZ_Object=MibTableColumn
ormPumpPowerBetaCoeffZ=_OrmPumpPowerBetaCoeffZ_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,18),_OrmPumpPowerBetaCoeffZ_Type())
ormPumpPowerBetaCoeffZ.setMaxAccess(_C)
if mibBuilder.loadTexts:ormPumpPowerBetaCoeffZ.setStatus(_A)
_OrmPumpRatioPump1_Type=FloatHundredths
_OrmPumpRatioPump1_Object=MibTableColumn
ormPumpRatioPump1=_OrmPumpRatioPump1_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,19),_OrmPumpRatioPump1_Type())
ormPumpRatioPump1.setMaxAccess(_C)
if mibBuilder.loadTexts:ormPumpRatioPump1.setStatus(_A)
_OrmPumpRatioPump2_Type=FloatHundredths
_OrmPumpRatioPump2_Object=MibTableColumn
ormPumpRatioPump2=_OrmPumpRatioPump2_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,20),_OrmPumpRatioPump2_Type())
ormPumpRatioPump2.setMaxAccess(_C)
if mibBuilder.loadTexts:ormPumpRatioPump2.setStatus(_A)
_OrmPumpRatioPump3_Type=FloatHundredths
_OrmPumpRatioPump3_Object=MibTableColumn
ormPumpRatioPump3=_OrmPumpRatioPump3_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,21),_OrmPumpRatioPump3_Type())
ormPumpRatioPump3.setMaxAccess(_C)
if mibBuilder.loadTexts:ormPumpRatioPump3.setStatus(_A)
_OrmPumpRatioPump4_Type=FloatHundredths
_OrmPumpRatioPump4_Object=MibTableColumn
ormPumpRatioPump4=_OrmPumpRatioPump4_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,22),_OrmPumpRatioPump4_Type())
ormPumpRatioPump4.setMaxAccess(_C)
if mibBuilder.loadTexts:ormPumpRatioPump4.setStatus(_A)
_OrmStaticRamanGain_Type=FloatHundredths
_OrmStaticRamanGain_Object=MibTableColumn
ormStaticRamanGain=_OrmStaticRamanGain_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,23),_OrmStaticRamanGain_Type())
ormStaticRamanGain.setMaxAccess(_C)
if mibBuilder.loadTexts:ormStaticRamanGain.setStatus(_A)
_OrmStaticEdfaGain_Type=FloatHundredths
_OrmStaticEdfaGain_Object=MibTableColumn
ormStaticEdfaGain=_OrmStaticEdfaGain_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,24),_OrmStaticEdfaGain_Type())
ormStaticEdfaGain.setMaxAccess(_C)
if mibBuilder.loadTexts:ormStaticEdfaGain.setStatus(_A)
_OrmStaticPostEdfaVoaAttenuation_Type=FloatHundredths
_OrmStaticPostEdfaVoaAttenuation_Object=MibTableColumn
ormStaticPostEdfaVoaAttenuation=_OrmStaticPostEdfaVoaAttenuation_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,25),_OrmStaticPostEdfaVoaAttenuation_Type())
ormStaticPostEdfaVoaAttenuation.setMaxAccess(_C)
if mibBuilder.loadTexts:ormStaticPostEdfaVoaAttenuation.setStatus(_A)
_OrmFiberType_Type=InfnFiberType
_OrmFiberType_Object=MibTableColumn
ormFiberType=_OrmFiberType_Object((1,3,6,1,4,1,21296,2,2,2,1,16,1,1,26),_OrmFiberType_Type())
ormFiberType.setMaxAccess(_C)
if mibBuilder.loadTexts:ormFiberType.setStatus(_A)
_OrmConformance_ObjectIdentity=ObjectIdentity
ormConformance=_OrmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,16,3))
_OrmCompliances_ObjectIdentity=ObjectIdentity
ormCompliances=_OrmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,16,3,1))
_OrmGroups_ObjectIdentity=ObjectIdentity
ormGroups=_OrmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,16,3,2))
ormGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,16,3,2,1))
ormGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:ormGroup.setStatus(_A)
ormCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,16,3,1,1))
ormCompliance.setObjects((_B,_h))
if mibBuilder.loadTexts:ormCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ormMIB':ormMIB,'ormTable':ormTable,'ormEntry':ormEntry,_H:ormMoId,_I:ormProvisonedType,_J:ormRxAmpDeviceSetpoint,_K:ormRxAmpDeviceTarget,_L:ormRxLastAmpDeviceCommitTs,_M:ormLaunchPowerOffset,_N:ormRxDampSeqNum,_O:ormTilt,_P:ormPointLossOffset,_Q:ormEnhPMRept,_R:ormRowStatus,_S:ormCBandSoakCapableFW,_T:ormAsePowerBetaCoeffX,_U:ormAsePowerBetaCoeffY,_V:ormAsePowerBetaCoeffZ,_W:ormPumpPowerBetaCoeffX,_X:ormPumpPowerBetaCoeffY,_Y:ormPumpPowerBetaCoeffZ,_Z:ormPumpRatioPump1,_a:ormPumpRatioPump2,_b:ormPumpRatioPump3,_c:ormPumpRatioPump4,_d:ormStaticRamanGain,_e:ormStaticEdfaGain,_f:ormStaticPostEdfaVoaAttenuation,_g:ormFiberType,'ormConformance':ormConformance,'ormCompliances':ormCompliances,'ormCompliance':ormCompliance,'ormGroups':ormGroups,_h:ormGroup})