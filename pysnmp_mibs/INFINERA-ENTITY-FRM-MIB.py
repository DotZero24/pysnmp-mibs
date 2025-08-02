_n='frmGroup'
_m='frmSuccessfulAGCRunTime'
_l='frmTxVOASetPoint'
_k='frmRamanGainSetPoint'
_j='frmTxLastAmpDeviceCommitTs'
_i='frmTxAmpDeviceTarget'
_h='frmTxAmpDeviceSetpoint'
_g='frmMaxLaunchPowerOffset'
_f='frmLaunchPowerOffset'
_e='frmSlotOperatingMode'
_d='frmDeploymentLabel3'
_c='frmDeploymentLabel2'
_b='frmDeploymentLabel1'
_a='frmOperatingMode'
_Z='frmPathLossInvokedPortAid'
_Y='frmIsPathLossCheckInvoked'
_X='frmRxPowerOffset'
_W='frmDampNullSeqReason'
_V='frmDampStatusString'
_U='frmOlosSoakTime'
_T='frmAdPwrTgtFailPortMask'
_S='frmRxDampSeqNum'
_R='frmTxDampSeqNum'
_Q='frmRxLastAmpDeviceCommitTs'
_P='frmRxAmpDeviceTarget'
_O='frmRxAmpDeviceSetpoint'
_N='frmGainControlLoop'
_M='frmEdfaPowerOffset'
_L='frmGainTiltOffset'
_K='frmMaxAddDropPorts'
_J='frmSpectrumTiltOffset'
_I='frmAutomaticTiltControl'
_H='frmProvEqptType'
_G='frmMoId'
_F='entPhysicalIndex'
_E='ENTITY-MIB'
_D='read-only'
_C='read-write'
_B='INFINERA-ENTITY-FRM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_E,_F)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
FloatTenths,InfnAddDropCount,InfnCBandOlosSoakTime,InfnEnableDisable,InfnEqptType,InfnOAOperatingMode,InfnSlotOperatingMode=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatTenths','InfnAddDropCount','InfnCBandOlosSoakTime','InfnEnableDisable','InfnEqptType','InfnOAOperatingMode','InfnSlotOperatingMode')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
frmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,33))
_FrmTable_Object=MibTable
frmTable=_FrmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1))
if mibBuilder.loadTexts:frmTable.setStatus(_A)
_FrmEntry_Object=MibTableRow
frmEntry=_FrmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1))
frmEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:frmEntry.setStatus(_A)
_FrmMoId_Type=DisplayString
_FrmMoId_Object=MibTableColumn
frmMoId=_FrmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,1),_FrmMoId_Type())
frmMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:frmMoId.setStatus(_A)
_FrmProvEqptType_Type=InfnEqptType
_FrmProvEqptType_Object=MibTableColumn
frmProvEqptType=_FrmProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,2),_FrmProvEqptType_Type())
frmProvEqptType.setMaxAccess(_C)
if mibBuilder.loadTexts:frmProvEqptType.setStatus(_A)
_FrmAutomaticTiltControl_Type=InfnEnableDisable
_FrmAutomaticTiltControl_Object=MibTableColumn
frmAutomaticTiltControl=_FrmAutomaticTiltControl_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,3),_FrmAutomaticTiltControl_Type())
frmAutomaticTiltControl.setMaxAccess(_C)
if mibBuilder.loadTexts:frmAutomaticTiltControl.setStatus(_A)
_FrmSpectrumTiltOffset_Type=FloatTenths
_FrmSpectrumTiltOffset_Object=MibTableColumn
frmSpectrumTiltOffset=_FrmSpectrumTiltOffset_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,4),_FrmSpectrumTiltOffset_Type())
frmSpectrumTiltOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:frmSpectrumTiltOffset.setStatus(_A)
_FrmMaxAddDropPorts_Type=InfnAddDropCount
_FrmMaxAddDropPorts_Object=MibTableColumn
frmMaxAddDropPorts=_FrmMaxAddDropPorts_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,5),_FrmMaxAddDropPorts_Type())
frmMaxAddDropPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:frmMaxAddDropPorts.setStatus(_A)
_FrmGainTiltOffset_Type=FloatTenths
_FrmGainTiltOffset_Object=MibTableColumn
frmGainTiltOffset=_FrmGainTiltOffset_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,6),_FrmGainTiltOffset_Type())
frmGainTiltOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:frmGainTiltOffset.setStatus(_A)
_FrmEdfaPowerOffset_Type=FloatTenths
_FrmEdfaPowerOffset_Object=MibTableColumn
frmEdfaPowerOffset=_FrmEdfaPowerOffset_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,7),_FrmEdfaPowerOffset_Type())
frmEdfaPowerOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:frmEdfaPowerOffset.setStatus(_A)
_FrmGainControlLoop_Type=InfnEnableDisable
_FrmGainControlLoop_Object=MibTableColumn
frmGainControlLoop=_FrmGainControlLoop_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,8),_FrmGainControlLoop_Type())
frmGainControlLoop.setMaxAccess(_C)
if mibBuilder.loadTexts:frmGainControlLoop.setStatus(_A)
_FrmRxPowerOffset_Type=FloatTenths
_FrmRxPowerOffset_Object=MibTableColumn
frmRxPowerOffset=_FrmRxPowerOffset_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,9),_FrmRxPowerOffset_Type())
frmRxPowerOffset.setMaxAccess('read-create')
if mibBuilder.loadTexts:frmRxPowerOffset.setStatus(_A)
_FrmRxAmpDeviceSetpoint_Type=FloatTenths
_FrmRxAmpDeviceSetpoint_Object=MibTableColumn
frmRxAmpDeviceSetpoint=_FrmRxAmpDeviceSetpoint_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,12),_FrmRxAmpDeviceSetpoint_Type())
frmRxAmpDeviceSetpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:frmRxAmpDeviceSetpoint.setStatus(_A)
_FrmRxAmpDeviceTarget_Type=FloatTenths
_FrmRxAmpDeviceTarget_Object=MibTableColumn
frmRxAmpDeviceTarget=_FrmRxAmpDeviceTarget_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,13),_FrmRxAmpDeviceTarget_Type())
frmRxAmpDeviceTarget.setMaxAccess(_D)
if mibBuilder.loadTexts:frmRxAmpDeviceTarget.setStatus(_A)
_FrmRxLastAmpDeviceCommitTs_Type=Integer32
_FrmRxLastAmpDeviceCommitTs_Object=MibTableColumn
frmRxLastAmpDeviceCommitTs=_FrmRxLastAmpDeviceCommitTs_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,14),_FrmRxLastAmpDeviceCommitTs_Type())
frmRxLastAmpDeviceCommitTs.setMaxAccess(_D)
if mibBuilder.loadTexts:frmRxLastAmpDeviceCommitTs.setStatus(_A)
_FrmTxDampSeqNum_Type=Integer32
_FrmTxDampSeqNum_Object=MibTableColumn
frmTxDampSeqNum=_FrmTxDampSeqNum_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,15),_FrmTxDampSeqNum_Type())
frmTxDampSeqNum.setMaxAccess(_D)
if mibBuilder.loadTexts:frmTxDampSeqNum.setStatus(_A)
_FrmRxDampSeqNum_Type=Integer32
_FrmRxDampSeqNum_Object=MibTableColumn
frmRxDampSeqNum=_FrmRxDampSeqNum_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,16),_FrmRxDampSeqNum_Type())
frmRxDampSeqNum.setMaxAccess(_D)
if mibBuilder.loadTexts:frmRxDampSeqNum.setStatus(_A)
_FrmAdPwrTgtFailPortMask_Type=Integer32
_FrmAdPwrTgtFailPortMask_Object=MibTableColumn
frmAdPwrTgtFailPortMask=_FrmAdPwrTgtFailPortMask_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,17),_FrmAdPwrTgtFailPortMask_Type())
frmAdPwrTgtFailPortMask.setMaxAccess(_D)
if mibBuilder.loadTexts:frmAdPwrTgtFailPortMask.setStatus(_A)
_FrmOlosSoakTime_Type=InfnCBandOlosSoakTime
_FrmOlosSoakTime_Object=MibTableColumn
frmOlosSoakTime=_FrmOlosSoakTime_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,18),_FrmOlosSoakTime_Type())
frmOlosSoakTime.setMaxAccess(_C)
if mibBuilder.loadTexts:frmOlosSoakTime.setStatus(_A)
_FrmIsPathLossCheckInvoked_Type=TruthValue
_FrmIsPathLossCheckInvoked_Object=MibTableColumn
frmIsPathLossCheckInvoked=_FrmIsPathLossCheckInvoked_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,19),_FrmIsPathLossCheckInvoked_Type())
frmIsPathLossCheckInvoked.setMaxAccess(_D)
if mibBuilder.loadTexts:frmIsPathLossCheckInvoked.setStatus(_A)
_FrmPathLossInvokedPortAid_Type=DisplayString
_FrmPathLossInvokedPortAid_Object=MibTableColumn
frmPathLossInvokedPortAid=_FrmPathLossInvokedPortAid_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,20),_FrmPathLossInvokedPortAid_Type())
frmPathLossInvokedPortAid.setMaxAccess(_D)
if mibBuilder.loadTexts:frmPathLossInvokedPortAid.setStatus(_A)
_FrmDampStatusString_Type=DisplayString
_FrmDampStatusString_Object=MibTableColumn
frmDampStatusString=_FrmDampStatusString_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,21),_FrmDampStatusString_Type())
frmDampStatusString.setMaxAccess(_D)
if mibBuilder.loadTexts:frmDampStatusString.setStatus(_A)
_FrmDampNullSeqReason_Type=DisplayString
_FrmDampNullSeqReason_Object=MibTableColumn
frmDampNullSeqReason=_FrmDampNullSeqReason_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,22),_FrmDampNullSeqReason_Type())
frmDampNullSeqReason.setMaxAccess(_D)
if mibBuilder.loadTexts:frmDampNullSeqReason.setStatus(_A)
_FrmOperatingMode_Type=InfnOAOperatingMode
_FrmOperatingMode_Object=MibTableColumn
frmOperatingMode=_FrmOperatingMode_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,23),_FrmOperatingMode_Type())
frmOperatingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:frmOperatingMode.setStatus(_A)
_FrmDeploymentLabel1_Type=DisplayString
_FrmDeploymentLabel1_Object=MibTableColumn
frmDeploymentLabel1=_FrmDeploymentLabel1_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,24),_FrmDeploymentLabel1_Type())
frmDeploymentLabel1.setMaxAccess(_C)
if mibBuilder.loadTexts:frmDeploymentLabel1.setStatus(_A)
_FrmDeploymentLabel2_Type=DisplayString
_FrmDeploymentLabel2_Object=MibTableColumn
frmDeploymentLabel2=_FrmDeploymentLabel2_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,25),_FrmDeploymentLabel2_Type())
frmDeploymentLabel2.setMaxAccess(_C)
if mibBuilder.loadTexts:frmDeploymentLabel2.setStatus(_A)
_FrmDeploymentLabel3_Type=DisplayString
_FrmDeploymentLabel3_Object=MibTableColumn
frmDeploymentLabel3=_FrmDeploymentLabel3_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,26),_FrmDeploymentLabel3_Type())
frmDeploymentLabel3.setMaxAccess(_C)
if mibBuilder.loadTexts:frmDeploymentLabel3.setStatus(_A)
_FrmSlotOperatingMode_Type=InfnSlotOperatingMode
_FrmSlotOperatingMode_Object=MibTableColumn
frmSlotOperatingMode=_FrmSlotOperatingMode_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,27),_FrmSlotOperatingMode_Type())
frmSlotOperatingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:frmSlotOperatingMode.setStatus(_A)
_FrmLaunchPowerOffset_Type=FloatTenths
_FrmLaunchPowerOffset_Object=MibTableColumn
frmLaunchPowerOffset=_FrmLaunchPowerOffset_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,28),_FrmLaunchPowerOffset_Type())
frmLaunchPowerOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:frmLaunchPowerOffset.setStatus(_A)
_FrmMaxLaunchPowerOffset_Type=FloatTenths
_FrmMaxLaunchPowerOffset_Object=MibTableColumn
frmMaxLaunchPowerOffset=_FrmMaxLaunchPowerOffset_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,29),_FrmMaxLaunchPowerOffset_Type())
frmMaxLaunchPowerOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:frmMaxLaunchPowerOffset.setStatus(_A)
_FrmTxAmpDeviceSetpoint_Type=FloatTenths
_FrmTxAmpDeviceSetpoint_Object=MibTableColumn
frmTxAmpDeviceSetpoint=_FrmTxAmpDeviceSetpoint_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,30),_FrmTxAmpDeviceSetpoint_Type())
frmTxAmpDeviceSetpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:frmTxAmpDeviceSetpoint.setStatus(_A)
_FrmTxAmpDeviceTarget_Type=FloatTenths
_FrmTxAmpDeviceTarget_Object=MibTableColumn
frmTxAmpDeviceTarget=_FrmTxAmpDeviceTarget_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,31),_FrmTxAmpDeviceTarget_Type())
frmTxAmpDeviceTarget.setMaxAccess(_D)
if mibBuilder.loadTexts:frmTxAmpDeviceTarget.setStatus(_A)
_FrmTxLastAmpDeviceCommitTs_Type=Integer32
_FrmTxLastAmpDeviceCommitTs_Object=MibTableColumn
frmTxLastAmpDeviceCommitTs=_FrmTxLastAmpDeviceCommitTs_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,32),_FrmTxLastAmpDeviceCommitTs_Type())
frmTxLastAmpDeviceCommitTs.setMaxAccess(_D)
if mibBuilder.loadTexts:frmTxLastAmpDeviceCommitTs.setStatus(_A)
_FrmRamanGainSetPoint_Type=FloatTenths
_FrmRamanGainSetPoint_Object=MibTableColumn
frmRamanGainSetPoint=_FrmRamanGainSetPoint_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,33),_FrmRamanGainSetPoint_Type())
frmRamanGainSetPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:frmRamanGainSetPoint.setStatus(_A)
_FrmTxVOASetPoint_Type=FloatTenths
_FrmTxVOASetPoint_Object=MibTableColumn
frmTxVOASetPoint=_FrmTxVOASetPoint_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,34),_FrmTxVOASetPoint_Type())
frmTxVOASetPoint.setMaxAccess(_D)
if mibBuilder.loadTexts:frmTxVOASetPoint.setStatus(_A)
_FrmSuccessfulAGCRunTime_Type=Integer32
_FrmSuccessfulAGCRunTime_Object=MibTableColumn
frmSuccessfulAGCRunTime=_FrmSuccessfulAGCRunTime_Object((1,3,6,1,4,1,21296,2,2,2,1,33,1,1,35),_FrmSuccessfulAGCRunTime_Type())
frmSuccessfulAGCRunTime.setMaxAccess(_D)
if mibBuilder.loadTexts:frmSuccessfulAGCRunTime.setStatus(_A)
_FrmConffrmance_ObjectIdentity=ObjectIdentity
frmConffrmance=_FrmConffrmance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,33,3))
_FrmCompliances_ObjectIdentity=ObjectIdentity
frmCompliances=_FrmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,33,3,1))
_FrmGroups_ObjectIdentity=ObjectIdentity
frmGroups=_FrmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,33,3,2))
frmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,33,3,2,1))
frmGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:frmGroup.setStatus(_A)
frmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,33,3,1,1))
frmCompliance.setObjects((_B,_n))
if mibBuilder.loadTexts:frmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'frmMIB':frmMIB,'frmTable':frmTable,'frmEntry':frmEntry,_G:frmMoId,_H:frmProvEqptType,_I:frmAutomaticTiltControl,_J:frmSpectrumTiltOffset,_K:frmMaxAddDropPorts,_L:frmGainTiltOffset,_M:frmEdfaPowerOffset,_N:frmGainControlLoop,_X:frmRxPowerOffset,_O:frmRxAmpDeviceSetpoint,_P:frmRxAmpDeviceTarget,_Q:frmRxLastAmpDeviceCommitTs,_R:frmTxDampSeqNum,_S:frmRxDampSeqNum,_T:frmAdPwrTgtFailPortMask,_U:frmOlosSoakTime,_Y:frmIsPathLossCheckInvoked,_Z:frmPathLossInvokedPortAid,_V:frmDampStatusString,_W:frmDampNullSeqReason,_a:frmOperatingMode,_b:frmDeploymentLabel1,_c:frmDeploymentLabel2,_d:frmDeploymentLabel3,_e:frmSlotOperatingMode,_f:frmLaunchPowerOffset,_g:frmMaxLaunchPowerOffset,_h:frmTxAmpDeviceSetpoint,_i:frmTxAmpDeviceTarget,_j:frmTxLastAmpDeviceCommitTs,_k:frmRamanGainSetPoint,_l:frmTxVOASetPoint,_m:frmSuccessfulAGCRunTime,'frmConffrmance':frmConffrmance,'frmCompliances':frmCompliances,'frmCompliance':frmCompliance,'frmGroups':frmGroups,_n:frmGroup})