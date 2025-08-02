_a='bmmGroup'
_Z='bmmSuccessfulACGRunTime'
_Y='bmmCBandSoakCapableFW'
_X='bmmMaxChanRatePlan'
_W='bmmRowStatus'
_V='bmmGain'
_U='bmmOperatingMode'
_T='bmmTilt'
_S='bmmRxDampSeqNum'
_R='bmmTxDampSeqNum'
_Q='bmmNumberOfChannel'
_P='bmmLaunchPowerOffset'
_O='bmmDisableGainControlLoop'
_N='bmmRxLastAmpDeviceCommitTs'
_M='bmmRxAmpDeviceTarget'
_L='bmmRxAmpDeviceSetpoint'
_K='bmmProvisonedType'
_J='bmmMoId'
_I='TruthValue'
_H='Integer32'
_G='InfnEqptType'
_F='entPhysicalIndex'
_E='ENTITY-MIB'
_D='read-only'
_C='read-create'
_B='INFINERA-ENTITY-BMM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_E,_F)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
FloatTenths,InfnEqptType,InfnMaxChRatePlan=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatTenths',_G,'InfnMaxChRatePlan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_I)
bmmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,3))
_BmmTable_Object=MibTable
bmmTable=_BmmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,3,1))
if mibBuilder.loadTexts:bmmTable.setStatus(_A)
_BmmEntry_Object=MibTableRow
bmmEntry=_BmmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,3,1,1))
bmmEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:bmmEntry.setStatus(_A)
_BmmMoId_Type=DisplayString
_BmmMoId_Object=MibTableColumn
bmmMoId=_BmmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,3,1,1,1),_BmmMoId_Type())
bmmMoId.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmMoId.setStatus(_A)
class _BmmProvisonedType_Type(InfnEqptType):defaultValue=47
_BmmProvisonedType_Type.__name__=_G
_BmmProvisonedType_Object=MibTableColumn
bmmProvisonedType=_BmmProvisonedType_Object((1,3,6,1,4,1,21296,2,2,2,1,3,1,1,2),_BmmProvisonedType_Type())
bmmProvisonedType.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmProvisonedType.setStatus(_A)
_BmmRxAmpDeviceSetpoint_Type=FloatTenths
_BmmRxAmpDeviceSetpoint_Object=MibTableColumn
bmmRxAmpDeviceSetpoint=_BmmRxAmpDeviceSetpoint_Object((1,3,6,1,4,1,21296,2,2,2,1,3,1,1,3),_BmmRxAmpDeviceSetpoint_Type())
bmmRxAmpDeviceSetpoint.setMaxAccess(_D)
if mibBuilder.loadTexts:bmmRxAmpDeviceSetpoint.setStatus(_A)
_BmmRxAmpDeviceTarget_Type=FloatTenths
_BmmRxAmpDeviceTarget_Object=MibTableColumn
bmmRxAmpDeviceTarget=_BmmRxAmpDeviceTarget_Object((1,3,6,1,4,1,21296,2,2,2,1,3,1,1,4),_BmmRxAmpDeviceTarget_Type())
bmmRxAmpDeviceTarget.setMaxAccess(_D)
if mibBuilder.loadTexts:bmmRxAmpDeviceTarget.setStatus(_A)
_BmmRxLastAmpDeviceCommitTs_Type=Integer32
_BmmRxLastAmpDeviceCommitTs_Object=MibTableColumn
bmmRxLastAmpDeviceCommitTs=_BmmRxLastAmpDeviceCommitTs_Object((1,3,6,1,4,1,21296,2,2,2,1,3,1,1,5),_BmmRxLastAmpDeviceCommitTs_Type())
bmmRxLastAmpDeviceCommitTs.setMaxAccess(_D)
if mibBuilder.loadTexts:bmmRxLastAmpDeviceCommitTs.setStatus(_A)
class _BmmDisableGainControlLoop_Type(TruthValue):defaultValue=2
_BmmDisableGainControlLoop_Type.__name__=_I
_BmmDisableGainControlLoop_Object=MibTableColumn
bmmDisableGainControlLoop=_BmmDisableGainControlLoop_Object((1,3,6,1,4,1,21296,2,2,2,1,3,1,1,6),_BmmDisableGainControlLoop_Type())
bmmDisableGainControlLoop.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmDisableGainControlLoop.setStatus(_A)
_BmmLaunchPowerOffset_Type=FloatTenths
_BmmLaunchPowerOffset_Object=MibTableColumn
bmmLaunchPowerOffset=_BmmLaunchPowerOffset_Object((1,3,6,1,4,1,21296,2,2,2,1,3,1,1,7),_BmmLaunchPowerOffset_Type())
bmmLaunchPowerOffset.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmLaunchPowerOffset.setStatus(_A)
_BmmNumberOfChannel_Type=Integer32
_BmmNumberOfChannel_Object=MibTableColumn
bmmNumberOfChannel=_BmmNumberOfChannel_Object((1,3,6,1,4,1,21296,2,2,2,1,3,1,1,8),_BmmNumberOfChannel_Type())
bmmNumberOfChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmNumberOfChannel.setStatus(_A)
_BmmTxDampSeqNum_Type=Integer32
_BmmTxDampSeqNum_Object=MibTableColumn
bmmTxDampSeqNum=_BmmTxDampSeqNum_Object((1,3,6,1,4,1,21296,2,2,2,1,3,1,1,9),_BmmTxDampSeqNum_Type())
bmmTxDampSeqNum.setMaxAccess(_D)
if mibBuilder.loadTexts:bmmTxDampSeqNum.setStatus(_A)
_BmmRxDampSeqNum_Type=Integer32
_BmmRxDampSeqNum_Object=MibTableColumn
bmmRxDampSeqNum=_BmmRxDampSeqNum_Object((1,3,6,1,4,1,21296,2,2,2,1,3,1,1,10),_BmmRxDampSeqNum_Type())
bmmRxDampSeqNum.setMaxAccess(_D)
if mibBuilder.loadTexts:bmmRxDampSeqNum.setStatus(_A)
_BmmTilt_Type=FloatTenths
_BmmTilt_Object=MibTableColumn
bmmTilt=_BmmTilt_Object((1,3,6,1,4,1,21296,2,2,2,1,3,1,1,11),_BmmTilt_Type())
bmmTilt.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmTilt.setStatus(_A)
class _BmmOperatingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('nativeAutomated',1),('slteMode1',2),('thirdPartyAmp',3),('static',4)))
_BmmOperatingMode_Type.__name__=_H
_BmmOperatingMode_Object=MibTableColumn
bmmOperatingMode=_BmmOperatingMode_Object((1,3,6,1,4,1,21296,2,2,2,1,3,1,1,12),_BmmOperatingMode_Type())
bmmOperatingMode.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmOperatingMode.setStatus(_A)
_BmmGain_Type=FloatTenths
_BmmGain_Object=MibTableColumn
bmmGain=_BmmGain_Object((1,3,6,1,4,1,21296,2,2,2,1,3,1,1,13),_BmmGain_Type())
bmmGain.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmGain.setStatus(_A)
_BmmRowStatus_Type=RowStatus
_BmmRowStatus_Object=MibTableColumn
bmmRowStatus=_BmmRowStatus_Object((1,3,6,1,4,1,21296,2,2,2,1,3,1,1,14),_BmmRowStatus_Type())
bmmRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmRowStatus.setStatus(_A)
_BmmMaxChanRatePlan_Type=InfnMaxChRatePlan
_BmmMaxChanRatePlan_Object=MibTableColumn
bmmMaxChanRatePlan=_BmmMaxChanRatePlan_Object((1,3,6,1,4,1,21296,2,2,2,1,3,1,1,15),_BmmMaxChanRatePlan_Type())
bmmMaxChanRatePlan.setMaxAccess(_C)
if mibBuilder.loadTexts:bmmMaxChanRatePlan.setStatus(_A)
_BmmCBandSoakCapableFW_Type=TruthValue
_BmmCBandSoakCapableFW_Object=MibTableColumn
bmmCBandSoakCapableFW=_BmmCBandSoakCapableFW_Object((1,3,6,1,4,1,21296,2,2,2,1,3,1,1,16),_BmmCBandSoakCapableFW_Type())
bmmCBandSoakCapableFW.setMaxAccess(_D)
if mibBuilder.loadTexts:bmmCBandSoakCapableFW.setStatus(_A)
_BmmSuccessfulACGRunTime_Type=Integer32
_BmmSuccessfulACGRunTime_Object=MibTableColumn
bmmSuccessfulACGRunTime=_BmmSuccessfulACGRunTime_Object((1,3,6,1,4,1,21296,2,2,2,1,3,1,1,17),_BmmSuccessfulACGRunTime_Type())
bmmSuccessfulACGRunTime.setMaxAccess(_D)
if mibBuilder.loadTexts:bmmSuccessfulACGRunTime.setStatus(_A)
_BmmConformance_ObjectIdentity=ObjectIdentity
bmmConformance=_BmmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,3,3))
_BmmCompliances_ObjectIdentity=ObjectIdentity
bmmCompliances=_BmmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,3,3,1))
_BmmGroups_ObjectIdentity=ObjectIdentity
bmmGroups=_BmmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,3,3,2))
bmmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,3,3,2,1))
bmmGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:bmmGroup.setStatus(_A)
bmmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,3,3,1,1))
bmmCompliance.setObjects((_B,_a))
if mibBuilder.loadTexts:bmmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'bmmMIB':bmmMIB,'bmmTable':bmmTable,'bmmEntry':bmmEntry,_J:bmmMoId,_K:bmmProvisonedType,_L:bmmRxAmpDeviceSetpoint,_M:bmmRxAmpDeviceTarget,_N:bmmRxLastAmpDeviceCommitTs,_O:bmmDisableGainControlLoop,_P:bmmLaunchPowerOffset,_Q:bmmNumberOfChannel,_R:bmmTxDampSeqNum,_S:bmmRxDampSeqNum,_T:bmmTilt,_U:bmmOperatingMode,_V:bmmGain,_W:bmmRowStatus,_X:bmmMaxChanRatePlan,_Y:bmmCBandSoakCapableFW,_Z:bmmSuccessfulACGRunTime,'bmmConformance':bmmConformance,'bmmCompliances':bmmCompliances,'bmmCompliance':bmmCompliance,'bmmGroups':bmmGroups,_a:bmmGroup})