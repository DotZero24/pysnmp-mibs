_Aa='h3cPseProfilesGroup'
_AZ='h3cPsePDNotificationGroup'
_AY='h3cPseScalarGroup'
_AX='h3cMainPseGroup'
_AW='h3cPsePortGroup'
_AV='h3cPOEDCOutDCVolAlarm'
_AU='h3cPOESwitchStateInVolCA'
_AT='h3cPOESwitchStateInVolBC'
_AS='h3cPOESwitchStateInVolAB'
_AR='h3cPOEACSwitchState'
_AQ='h3cPOEModuleCurRestricted'
_AP='h3cPOEModuleShutdown'
_AO='h3cPOEModuleFanError'
_AN='h3cPOEModuleOverTemp'
_AM='h3cPOEModuleOverVoltage'
_AL='h3cPOEModuleOutputError'
_AK='h3cPOEModuleInputError'
_AJ='h3cPOEModuleDisconnect'
_AI='h3cPOEAlarmStateModuleNum'
_AH='h3cPOEInCurStateModuleNum'
_AG='h3cPOEACSwitchStateModuleNum'
_AF='h3cPOEDCOutCurNum'
_AE='h3cPOEDCOutStateModuleNum'
_AD='h3cPOESMFactorName'
_AC='h3cPOESMMinorVersion'
_AB='h3cPOESMMajorVersion'
_AA='h3cPOESupervisionModuleName'
_A9='h3cPOEPowerModuleNum'
_A8='h3cPOEPowerType'
_A7='h3cPOEThresholdDCMaximum'
_A6='h3cPOEThresholdDCMinimum'
_A5='h3cPOEThresholdACMaximum'
_A4='h3cPOEThresholdACMimimum'
_A3='h3cPseProfileRowStatus'
_A2='h3cPseProfileApplyNum'
_A1='h3cPseProfilePairs'
_A0='h3cPseProfilePriority'
_z='h3cPseProfilePowerLimit'
_y='h3cPseProfilePowerMode'
_x='h3cPseProfileName'
_w='h3cpsePDChangeNotification'
_v='h3cPDPolicyMode'
_u='h3cPsePolicyMode'
_t='h3cPsePowerMaxValue'
_s='h3cPseAutoDetectActive'
_r='h3cMainGuaranteedPowerRemaining'
_q='h3cMainPsePeakPower'
_p='h3cMainPseAveragePower'
_o='h3cMainPsePowerLimit'
_n='h3cMainPsePriorityMode'
_m='h3cPsePortFaultDescription'
_l='h3cPsePortPeakPower'
_k='h3cPsePortAveragePower'
_j='h3cPsePortCurrentPower'
_i='h3cPsePortPowerLimit'
_h='h3cPsePortProfileIndex'
_g='priority'
_f='h3cPOEDCOutInfoIndex'
_e='h3cPOEModuleIndex'
_d='h3cPseProfileIndex'
_c='critical'
_b='otherError'
_a='switchOff'
_Z='fuseBroken'
_Y='aboveLimit'
_X='underLimit'
_W='DisplayString'
_V='pethPsePortIndex'
_U='pethPsePortGroupIndex'
_T='pethPsePortDetectionStatus'
_S='pethMainPseGroupIndex'
_R='h3cPOEInCurCState'
_Q='h3cPOEInCurBState'
_P='h3cPOEInCurAState'
_O='h3cPOEACSwitchStateIndex'
_N='h3cPOEDCOutStateIndex'
_M='disabled'
_L='normal'
_K='h3cPOESwitchStateVolExIndex'
_J='POWER-ETHERNET-MIB'
_I='accessible-for-notify'
_H='read-create'
_G='h3cPOEAlarmModuleInfoIndex'
_F='OctetString'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='A3COM-HUAWEI-POWER-ETH-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
pethMainPseGroupIndex,pethPsePortDetectionStatus,pethPsePortGroupIndex,pethPsePortIndex=mibBuilder.importSymbols(_J,_S,_T,_U,_V)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_W,'PhysAddress','RowStatus','TextualConvention')
h3cPowerEthernetExt=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,14))
class ACAlarmState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_L,1),(_X,2),(_Y,3),('lackPhrase',4),(_Z,5),(_a,6),(_b,7)))
class DCAlarmState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_L,1),(_X,2),(_Y,3),(_Z,4),(_a,5),(_b,6)))
class SwitchState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('on',1),('off',2),('highVoltInput',3),('lowVoltInput',4)))
class ModuleAlarmState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('alarm',2)))
_H3cPsePortTable_Object=MibTable
h3cPsePortTable=_H3cPsePortTable_Object((1,3,6,1,4,1,43,45,1,10,2,14,1))
if mibBuilder.loadTexts:h3cPsePortTable.setStatus(_A)
_H3cPsePortEntry_Object=MibTableRow
h3cPsePortEntry=_H3cPsePortEntry_Object((1,3,6,1,4,1,43,45,1,10,2,14,1,1))
h3cPsePortEntry.setIndexNames((0,_J,_U),(0,_J,_V))
if mibBuilder.loadTexts:h3cPsePortEntry.setStatus(_A)
_H3cPsePortFaultDescription_Type=DisplayString
_H3cPsePortFaultDescription_Object=MibTableColumn
h3cPsePortFaultDescription=_H3cPsePortFaultDescription_Object((1,3,6,1,4,1,43,45,1,10,2,14,1,1,2),_H3cPsePortFaultDescription_Type())
h3cPsePortFaultDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPsePortFaultDescription.setStatus(_A)
_H3cPsePortPeakPower_Type=Integer32
_H3cPsePortPeakPower_Object=MibTableColumn
h3cPsePortPeakPower=_H3cPsePortPeakPower_Object((1,3,6,1,4,1,43,45,1,10,2,14,1,1,3),_H3cPsePortPeakPower_Type())
h3cPsePortPeakPower.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPsePortPeakPower.setStatus(_A)
_H3cPsePortAveragePower_Type=Integer32
_H3cPsePortAveragePower_Object=MibTableColumn
h3cPsePortAveragePower=_H3cPsePortAveragePower_Object((1,3,6,1,4,1,43,45,1,10,2,14,1,1,4),_H3cPsePortAveragePower_Type())
h3cPsePortAveragePower.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPsePortAveragePower.setStatus(_A)
_H3cPsePortCurrentPower_Type=Integer32
_H3cPsePortCurrentPower_Object=MibTableColumn
h3cPsePortCurrentPower=_H3cPsePortCurrentPower_Object((1,3,6,1,4,1,43,45,1,10,2,14,1,1,5),_H3cPsePortCurrentPower_Type())
h3cPsePortCurrentPower.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPsePortCurrentPower.setStatus(_A)
_H3cPsePortPowerLimit_Type=Integer32
_H3cPsePortPowerLimit_Object=MibTableColumn
h3cPsePortPowerLimit=_H3cPsePortPowerLimit_Object((1,3,6,1,4,1,43,45,1,10,2,14,1,1,6),_H3cPsePortPowerLimit_Type())
h3cPsePortPowerLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPsePortPowerLimit.setStatus(_A)
class _H3cPsePortProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cPsePortProfileIndex_Type.__name__=_D
_H3cPsePortProfileIndex_Object=MibTableColumn
h3cPsePortProfileIndex=_H3cPsePortProfileIndex_Object((1,3,6,1,4,1,43,45,1,10,2,14,1,1,7),_H3cPsePortProfileIndex_Type())
h3cPsePortProfileIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPsePortProfileIndex.setStatus(_A)
_H3cMainPseTable_Object=MibTable
h3cMainPseTable=_H3cMainPseTable_Object((1,3,6,1,4,1,43,45,1,10,2,14,2))
if mibBuilder.loadTexts:h3cMainPseTable.setStatus(_A)
_H3cMainPseEntry_Object=MibTableRow
h3cMainPseEntry=_H3cMainPseEntry_Object((1,3,6,1,4,1,43,45,1,10,2,14,2,1))
h3cMainPseEntry.setIndexNames((0,_J,_S))
if mibBuilder.loadTexts:h3cMainPseEntry.setStatus(_A)
_H3cMainPsePowerLimit_Type=Integer32
_H3cMainPsePowerLimit_Object=MibTableColumn
h3cMainPsePowerLimit=_H3cMainPsePowerLimit_Object((1,3,6,1,4,1,43,45,1,10,2,14,2,1,1),_H3cMainPsePowerLimit_Type())
h3cMainPsePowerLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMainPsePowerLimit.setStatus(_A)
_H3cMainPseAveragePower_Type=Integer32
_H3cMainPseAveragePower_Object=MibTableColumn
h3cMainPseAveragePower=_H3cMainPseAveragePower_Object((1,3,6,1,4,1,43,45,1,10,2,14,2,1,2),_H3cMainPseAveragePower_Type())
h3cMainPseAveragePower.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMainPseAveragePower.setStatus(_A)
_H3cMainPsePeakPower_Type=Integer32
_H3cMainPsePeakPower_Object=MibTableColumn
h3cMainPsePeakPower=_H3cMainPsePeakPower_Object((1,3,6,1,4,1,43,45,1,10,2,14,2,1,3),_H3cMainPsePeakPower_Type())
h3cMainPsePeakPower.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMainPsePeakPower.setStatus(_A)
_H3cMainGuaranteedPowerRemaining_Type=Integer32
_H3cMainGuaranteedPowerRemaining_Object=MibTableColumn
h3cMainGuaranteedPowerRemaining=_H3cMainGuaranteedPowerRemaining_Object((1,3,6,1,4,1,43,45,1,10,2,14,2,1,4),_H3cMainGuaranteedPowerRemaining_Type())
h3cMainGuaranteedPowerRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMainGuaranteedPowerRemaining.setStatus(_A)
class _H3cMainPsePriorityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disconnection',0),('non-disconnection',1)))
_H3cMainPsePriorityMode_Type.__name__=_D
_H3cMainPsePriorityMode_Object=MibTableColumn
h3cMainPsePriorityMode=_H3cMainPsePriorityMode_Object((1,3,6,1,4,1,43,45,1,10,2,14,2,1,5),_H3cMainPsePriorityMode_Type())
h3cMainPsePriorityMode.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMainPsePriorityMode.setStatus(_A)
class _H3cMainPseLegacy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('enable',0),('disable',1)))
_H3cMainPseLegacy_Type.__name__=_D
_H3cMainPseLegacy_Object=MibTableColumn
h3cMainPseLegacy=_H3cMainPseLegacy_Object((1,3,6,1,4,1,43,45,1,10,2,14,2,1,6),_H3cMainPseLegacy_Type())
h3cMainPseLegacy.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMainPseLegacy.setStatus(_A)
class _H3cMainPsePowerPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_c,1),('high',2),('low',3)))
_H3cMainPsePowerPriority_Type.__name__=_D
_H3cMainPsePowerPriority_Object=MibTableColumn
h3cMainPsePowerPriority=_H3cMainPsePowerPriority_Object((1,3,6,1,4,1,43,45,1,10,2,14,2,1,7),_H3cMainPsePowerPriority_Type())
h3cMainPsePowerPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMainPsePowerPriority.setStatus(_A)
class _H3cPseAutoDetectActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notSupported',1),(_M,2),('enabled',3)))
_H3cPseAutoDetectActive_Type.__name__=_D
_H3cPseAutoDetectActive_Object=MibScalar
h3cPseAutoDetectActive=_H3cPseAutoDetectActive_Object((1,3,6,1,4,1,43,45,1,10,2,14,3),_H3cPseAutoDetectActive_Type())
h3cPseAutoDetectActive.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPseAutoDetectActive.setStatus(_A)
_H3cPseComformance_ObjectIdentity=ObjectIdentity
h3cPseComformance=_H3cPseComformance_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,14,4))
_H3cPseCompliances_ObjectIdentity=ObjectIdentity
h3cPseCompliances=_H3cPseCompliances_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,14,4,1))
_H3cPseGroup_ObjectIdentity=ObjectIdentity
h3cPseGroup=_H3cPseGroup_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,14,4,2))
_H3cPsePowerMaxValue_Type=Integer32
_H3cPsePowerMaxValue_Object=MibScalar
h3cPsePowerMaxValue=_H3cPsePowerMaxValue_Object((1,3,6,1,4,1,43,45,1,10,2,14,5),_H3cPsePowerMaxValue_Type())
h3cPsePowerMaxValue.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPsePowerMaxValue.setStatus(_A)
_H3cpseportNotification_ObjectIdentity=ObjectIdentity
h3cpseportNotification=_H3cpseportNotification_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,14,6))
_H3cPseProfilesTable_Object=MibTable
h3cPseProfilesTable=_H3cPseProfilesTable_Object((1,3,6,1,4,1,43,45,1,10,2,14,7))
if mibBuilder.loadTexts:h3cPseProfilesTable.setStatus(_A)
_H3cPseProfilesEntry_Object=MibTableRow
h3cPseProfilesEntry=_H3cPseProfilesEntry_Object((1,3,6,1,4,1,43,45,1,10,2,14,7,1))
h3cPseProfilesEntry.setIndexNames((0,_B,_d))
if mibBuilder.loadTexts:h3cPseProfilesEntry.setStatus(_A)
class _H3cPseProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_H3cPseProfileIndex_Type.__name__=_D
_H3cPseProfileIndex_Object=MibTableColumn
h3cPseProfileIndex=_H3cPseProfileIndex_Object((1,3,6,1,4,1,43,45,1,10,2,14,7,1,1),_H3cPseProfileIndex_Type())
h3cPseProfileIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cPseProfileIndex.setStatus(_A)
class _H3cPseProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_H3cPseProfileName_Type.__name__=_W
_H3cPseProfileName_Object=MibTableColumn
h3cPseProfileName=_H3cPseProfileName_Object((1,3,6,1,4,1,43,45,1,10,2,14,7,1,2),_H3cPseProfileName_Type())
h3cPseProfileName.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cPseProfileName.setStatus(_A)
class _H3cPseProfilePowerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('powerDisabled',1),('powerEnabled',2)))
_H3cPseProfilePowerMode_Type.__name__=_D
_H3cPseProfilePowerMode_Object=MibTableColumn
h3cPseProfilePowerMode=_H3cPseProfilePowerMode_Object((1,3,6,1,4,1,43,45,1,10,2,14,7,1,3),_H3cPseProfilePowerMode_Type())
h3cPseProfilePowerMode.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cPseProfilePowerMode.setStatus(_A)
class _H3cPseProfilePowerLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15400))
_H3cPseProfilePowerLimit_Type.__name__=_D
_H3cPseProfilePowerLimit_Object=MibTableColumn
h3cPseProfilePowerLimit=_H3cPseProfilePowerLimit_Object((1,3,6,1,4,1,43,45,1,10,2,14,7,1,4),_H3cPseProfilePowerLimit_Type())
h3cPseProfilePowerLimit.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cPseProfilePowerLimit.setStatus(_A)
class _H3cPseProfilePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_c,1),('high',2),('low',3)))
_H3cPseProfilePriority_Type.__name__=_D
_H3cPseProfilePriority_Object=MibTableColumn
h3cPseProfilePriority=_H3cPseProfilePriority_Object((1,3,6,1,4,1,43,45,1,10,2,14,7,1,5),_H3cPseProfilePriority_Type())
h3cPseProfilePriority.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cPseProfilePriority.setStatus(_A)
class _H3cPseProfilePairs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('signal',1),('spare',2)))
_H3cPseProfilePairs_Type.__name__=_D
_H3cPseProfilePairs_Object=MibTableColumn
h3cPseProfilePairs=_H3cPseProfilePairs_Object((1,3,6,1,4,1,43,45,1,10,2,14,7,1,6),_H3cPseProfilePairs_Type())
h3cPseProfilePairs.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cPseProfilePairs.setStatus(_A)
_H3cPseProfileApplyNum_Type=Integer32
_H3cPseProfileApplyNum_Object=MibTableColumn
h3cPseProfileApplyNum=_H3cPseProfileApplyNum_Object((1,3,6,1,4,1,43,45,1,10,2,14,7,1,7),_H3cPseProfileApplyNum_Type())
h3cPseProfileApplyNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPseProfileApplyNum.setStatus(_A)
_H3cPseProfileRowStatus_Type=RowStatus
_H3cPseProfileRowStatus_Object=MibTableColumn
h3cPseProfileRowStatus=_H3cPseProfileRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,14,7,1,8),_H3cPseProfileRowStatus_Type())
h3cPseProfileRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cPseProfileRowStatus.setStatus(_A)
_H3cPOEPowerObjects_ObjectIdentity=ObjectIdentity
h3cPOEPowerObjects=_H3cPOEPowerObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,14,8))
_H3cPOEThresholdLimitObjs_ObjectIdentity=ObjectIdentity
h3cPOEThresholdLimitObjs=_H3cPOEThresholdLimitObjs_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,14,8,1))
class _H3cPOEThresholdACMimimum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_H3cPOEThresholdACMimimum_Type.__name__=_F
_H3cPOEThresholdACMimimum_Object=MibScalar
h3cPOEThresholdACMimimum=_H3cPOEThresholdACMimimum_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,1,1),_H3cPOEThresholdACMimimum_Type())
h3cPOEThresholdACMimimum.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPOEThresholdACMimimum.setStatus(_A)
class _H3cPOEThresholdACMaximum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_H3cPOEThresholdACMaximum_Type.__name__=_F
_H3cPOEThresholdACMaximum_Object=MibScalar
h3cPOEThresholdACMaximum=_H3cPOEThresholdACMaximum_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,1,2),_H3cPOEThresholdACMaximum_Type())
h3cPOEThresholdACMaximum.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPOEThresholdACMaximum.setStatus(_A)
class _H3cPOEThresholdDCMinimum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_H3cPOEThresholdDCMinimum_Type.__name__=_F
_H3cPOEThresholdDCMinimum_Object=MibScalar
h3cPOEThresholdDCMinimum=_H3cPOEThresholdDCMinimum_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,1,3),_H3cPOEThresholdDCMinimum_Type())
h3cPOEThresholdDCMinimum.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPOEThresholdDCMinimum.setStatus(_A)
class _H3cPOEThresholdDCMaximum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_H3cPOEThresholdDCMaximum_Type.__name__=_F
_H3cPOEThresholdDCMaximum_Object=MibScalar
h3cPOEThresholdDCMaximum=_H3cPOEThresholdDCMaximum_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,1,4),_H3cPOEThresholdDCMaximum_Type())
h3cPOEThresholdDCMaximum.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPOEThresholdDCMaximum.setStatus(_A)
_H3cPOESupModuleInfoObjs_ObjectIdentity=ObjectIdentity
h3cPOESupModuleInfoObjs=_H3cPOESupModuleInfoObjs_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,14,8,2))
class _H3cPOEPowerType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,127))
_H3cPOEPowerType_Type.__name__=_F
_H3cPOEPowerType_Object=MibScalar
h3cPOEPowerType=_H3cPOEPowerType_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,2,1),_H3cPOEPowerType_Type())
h3cPOEPowerType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOEPowerType.setStatus(_A)
_H3cPOEPowerModuleNum_Type=Integer32
_H3cPOEPowerModuleNum_Object=MibScalar
h3cPOEPowerModuleNum=_H3cPOEPowerModuleNum_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,2,2),_H3cPOEPowerModuleNum_Type())
h3cPOEPowerModuleNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOEPowerModuleNum.setStatus(_A)
class _H3cPOESupervisionModuleName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,127))
_H3cPOESupervisionModuleName_Type.__name__=_F
_H3cPOESupervisionModuleName_Object=MibScalar
h3cPOESupervisionModuleName=_H3cPOESupervisionModuleName_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,2,3),_H3cPOESupervisionModuleName_Type())
h3cPOESupervisionModuleName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOESupervisionModuleName.setStatus(_A)
_H3cPOESMMajorVersion_Type=Integer32
_H3cPOESMMajorVersion_Object=MibScalar
h3cPOESMMajorVersion=_H3cPOESMMajorVersion_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,2,4),_H3cPOESMMajorVersion_Type())
h3cPOESMMajorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOESMMajorVersion.setStatus(_A)
_H3cPOESMMinorVersion_Type=Integer32
_H3cPOESMMinorVersion_Object=MibScalar
h3cPOESMMinorVersion=_H3cPOESMMinorVersion_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,2,5),_H3cPOESMMinorVersion_Type())
h3cPOESMMinorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOESMMinorVersion.setStatus(_A)
class _H3cPOESMFactorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,127))
_H3cPOESMFactorName_Type.__name__=_F
_H3cPOESMFactorName_Object=MibScalar
h3cPOESMFactorName=_H3cPOESMFactorName_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,2,6),_H3cPOESMFactorName_Type())
h3cPOESMFactorName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOESMFactorName.setStatus(_A)
_H3cPOEModuleInfoTable_Object=MibTable
h3cPOEModuleInfoTable=_H3cPOEModuleInfoTable_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,2,7))
if mibBuilder.loadTexts:h3cPOEModuleInfoTable.setStatus(_A)
_H3cPOEModuleInfoEntry_Object=MibTableRow
h3cPOEModuleInfoEntry=_H3cPOEModuleInfoEntry_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,2,7,1))
h3cPOEModuleInfoEntry.setIndexNames((0,_B,_e))
if mibBuilder.loadTexts:h3cPOEModuleInfoEntry.setStatus(_A)
class _H3cPOEModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cPOEModuleIndex_Type.__name__=_D
_H3cPOEModuleIndex_Object=MibTableColumn
h3cPOEModuleIndex=_H3cPOEModuleIndex_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,2,7,1,1),_H3cPOEModuleIndex_Type())
h3cPOEModuleIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cPOEModuleIndex.setStatus(_A)
_H3cPOEModuleID_Type=Integer32
_H3cPOEModuleID_Object=MibTableColumn
h3cPOEModuleID=_H3cPOEModuleID_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,2,7,1,2),_H3cPOEModuleID_Type())
h3cPOEModuleID.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOEModuleID.setStatus(_A)
_H3cPOEModuleInfoPower_Type=Integer32
_H3cPOEModuleInfoPower_Object=MibTableColumn
h3cPOEModuleInfoPower=_H3cPOEModuleInfoPower_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,2,7,1,3),_H3cPOEModuleInfoPower_Type())
h3cPOEModuleInfoPower.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOEModuleInfoPower.setStatus(_A)
class _H3cPOEModuleHardVerInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,127))
_H3cPOEModuleHardVerInfo_Type.__name__=_F
_H3cPOEModuleHardVerInfo_Object=MibTableColumn
h3cPOEModuleHardVerInfo=_H3cPOEModuleHardVerInfo_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,2,7,1,4),_H3cPOEModuleHardVerInfo_Type())
h3cPOEModuleHardVerInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOEModuleHardVerInfo.setStatus(_A)
_H3cPOEDCOutStateObjects_ObjectIdentity=ObjectIdentity
h3cPOEDCOutStateObjects=_H3cPOEDCOutStateObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,14,8,3))
_H3cPOEDCOutStateModuleNum_Type=Integer32
_H3cPOEDCOutStateModuleNum_Object=MibScalar
h3cPOEDCOutStateModuleNum=_H3cPOEDCOutStateModuleNum_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,3,1),_H3cPOEDCOutStateModuleNum_Type())
h3cPOEDCOutStateModuleNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOEDCOutStateModuleNum.setStatus(_A)
_H3cPOEDCOutStateTable_Object=MibTable
h3cPOEDCOutStateTable=_H3cPOEDCOutStateTable_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,3,2))
if mibBuilder.loadTexts:h3cPOEDCOutStateTable.setStatus(_A)
_H3cPOEDCOutStateEntry_Object=MibTableRow
h3cPOEDCOutStateEntry=_H3cPOEDCOutStateEntry_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,3,2,1))
h3cPOEDCOutStateEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:h3cPOEDCOutStateEntry.setStatus(_A)
class _H3cPOEDCOutStateIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cPOEDCOutStateIndex_Type.__name__=_D
_H3cPOEDCOutStateIndex_Object=MibTableColumn
h3cPOEDCOutStateIndex=_H3cPOEDCOutStateIndex_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,3,2,1,1),_H3cPOEDCOutStateIndex_Type())
h3cPOEDCOutStateIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cPOEDCOutStateIndex.setStatus(_A)
_H3cPOEDCOutDCVolAlarm_Type=DCAlarmState
_H3cPOEDCOutDCVolAlarm_Object=MibTableColumn
h3cPOEDCOutDCVolAlarm=_H3cPOEDCOutDCVolAlarm_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,3,2,1,2),_H3cPOEDCOutDCVolAlarm_Type())
h3cPOEDCOutDCVolAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOEDCOutDCVolAlarm.setStatus(_A)
_H3cPOEDCOutInfoObjects_ObjectIdentity=ObjectIdentity
h3cPOEDCOutInfoObjects=_H3cPOEDCOutInfoObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,14,8,4))
_H3cPOEDCOutCurNum_Type=Integer32
_H3cPOEDCOutCurNum_Object=MibScalar
h3cPOEDCOutCurNum=_H3cPOEDCOutCurNum_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,4,1),_H3cPOEDCOutCurNum_Type())
h3cPOEDCOutCurNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOEDCOutCurNum.setStatus(_A)
_H3cPOEDCOutInfoTable_Object=MibTable
h3cPOEDCOutInfoTable=_H3cPOEDCOutInfoTable_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,4,2))
if mibBuilder.loadTexts:h3cPOEDCOutInfoTable.setStatus(_A)
_H3cPOEDCOutInfoEntry_Object=MibTableRow
h3cPOEDCOutInfoEntry=_H3cPOEDCOutInfoEntry_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,4,2,1))
h3cPOEDCOutInfoEntry.setIndexNames((0,_B,_f))
if mibBuilder.loadTexts:h3cPOEDCOutInfoEntry.setStatus(_A)
class _H3cPOEDCOutInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cPOEDCOutInfoIndex_Type.__name__=_D
_H3cPOEDCOutInfoIndex_Object=MibTableColumn
h3cPOEDCOutInfoIndex=_H3cPOEDCOutInfoIndex_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,4,2,1,1),_H3cPOEDCOutInfoIndex_Type())
h3cPOEDCOutInfoIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cPOEDCOutInfoIndex.setStatus(_A)
class _H3cPOEDCOutVol_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_H3cPOEDCOutVol_Type.__name__=_F
_H3cPOEDCOutVol_Object=MibTableColumn
h3cPOEDCOutVol=_H3cPOEDCOutVol_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,4,2,1,2),_H3cPOEDCOutVol_Type())
h3cPOEDCOutVol.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOEDCOutVol.setStatus(_A)
class _H3cPOEDCOutInfoLoadCur_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_H3cPOEDCOutInfoLoadCur_Type.__name__=_F
_H3cPOEDCOutInfoLoadCur_Object=MibTableColumn
h3cPOEDCOutInfoLoadCur=_H3cPOEDCOutInfoLoadCur_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,4,2,1,3),_H3cPOEDCOutInfoLoadCur_Type())
h3cPOEDCOutInfoLoadCur.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOEDCOutInfoLoadCur.setStatus(_A)
_H3cPOEACSwitchStateModuleObjs_ObjectIdentity=ObjectIdentity
h3cPOEACSwitchStateModuleObjs=_H3cPOEACSwitchStateModuleObjs_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,14,8,5))
_H3cPOEACSwitchStateModuleNum_Type=Integer32
_H3cPOEACSwitchStateModuleNum_Object=MibScalar
h3cPOEACSwitchStateModuleNum=_H3cPOEACSwitchStateModuleNum_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,5,1),_H3cPOEACSwitchStateModuleNum_Type())
h3cPOEACSwitchStateModuleNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOEACSwitchStateModuleNum.setStatus(_A)
_H3cPOEACSwitchStateTable_Object=MibTable
h3cPOEACSwitchStateTable=_H3cPOEACSwitchStateTable_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,5,2))
if mibBuilder.loadTexts:h3cPOEACSwitchStateTable.setStatus(_A)
_H3cPOEACSwitchStateEntry_Object=MibTableRow
h3cPOEACSwitchStateEntry=_H3cPOEACSwitchStateEntry_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,5,2,1))
h3cPOEACSwitchStateEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:h3cPOEACSwitchStateEntry.setStatus(_A)
class _H3cPOEACSwitchStateIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cPOEACSwitchStateIndex_Type.__name__=_D
_H3cPOEACSwitchStateIndex_Object=MibTableColumn
h3cPOEACSwitchStateIndex=_H3cPOEACSwitchStateIndex_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,5,2,1,1),_H3cPOEACSwitchStateIndex_Type())
h3cPOEACSwitchStateIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cPOEACSwitchStateIndex.setStatus(_A)
_H3cPOEACSwitchState_Type=SwitchState
_H3cPOEACSwitchState_Object=MibTableColumn
h3cPOEACSwitchState=_H3cPOEACSwitchState_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,5,2,1,2),_H3cPOEACSwitchState_Type())
h3cPOEACSwitchState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOEACSwitchState.setStatus(_A)
_H3cPOEInCurStateObjects_ObjectIdentity=ObjectIdentity
h3cPOEInCurStateObjects=_H3cPOEInCurStateObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,14,8,6))
_H3cPOEInCurStateModuleNum_Type=Integer32
_H3cPOEInCurStateModuleNum_Object=MibScalar
h3cPOEInCurStateModuleNum=_H3cPOEInCurStateModuleNum_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,6,1),_H3cPOEInCurStateModuleNum_Type())
h3cPOEInCurStateModuleNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOEInCurStateModuleNum.setStatus(_A)
_H3cPOEInCurAState_Type=ACAlarmState
_H3cPOEInCurAState_Object=MibScalar
h3cPOEInCurAState=_H3cPOEInCurAState_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,6,2),_H3cPOEInCurAState_Type())
h3cPOEInCurAState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOEInCurAState.setStatus(_A)
_H3cPOEInCurBState_Type=ACAlarmState
_H3cPOEInCurBState_Object=MibScalar
h3cPOEInCurBState=_H3cPOEInCurBState_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,6,3),_H3cPOEInCurBState_Type())
h3cPOEInCurBState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOEInCurBState.setStatus(_A)
_H3cPOEInCurCState_Type=ACAlarmState
_H3cPOEInCurCState_Object=MibScalar
h3cPOEInCurCState=_H3cPOEInCurCState_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,6,4),_H3cPOEInCurCState_Type())
h3cPOEInCurCState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOEInCurCState.setStatus(_A)
_H3cPOESwitchStateVolExTable_Object=MibTable
h3cPOESwitchStateVolExTable=_H3cPOESwitchStateVolExTable_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,6,5))
if mibBuilder.loadTexts:h3cPOESwitchStateVolExTable.setStatus(_A)
_H3cPOESwitchStateVolExEntry_Object=MibTableRow
h3cPOESwitchStateVolExEntry=_H3cPOESwitchStateVolExEntry_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,6,5,1))
h3cPOESwitchStateVolExEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:h3cPOESwitchStateVolExEntry.setStatus(_A)
class _H3cPOESwitchStateVolExIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cPOESwitchStateVolExIndex_Type.__name__=_D
_H3cPOESwitchStateVolExIndex_Object=MibTableColumn
h3cPOESwitchStateVolExIndex=_H3cPOESwitchStateVolExIndex_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,6,5,1,1),_H3cPOESwitchStateVolExIndex_Type())
h3cPOESwitchStateVolExIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cPOESwitchStateVolExIndex.setStatus(_A)
_H3cPOESwitchStateInVolAB_Type=ACAlarmState
_H3cPOESwitchStateInVolAB_Object=MibTableColumn
h3cPOESwitchStateInVolAB=_H3cPOESwitchStateInVolAB_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,6,5,1,2),_H3cPOESwitchStateInVolAB_Type())
h3cPOESwitchStateInVolAB.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOESwitchStateInVolAB.setStatus(_A)
_H3cPOESwitchStateInVolBC_Type=ACAlarmState
_H3cPOESwitchStateInVolBC_Object=MibTableColumn
h3cPOESwitchStateInVolBC=_H3cPOESwitchStateInVolBC_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,6,5,1,3),_H3cPOESwitchStateInVolBC_Type())
h3cPOESwitchStateInVolBC.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOESwitchStateInVolBC.setStatus(_A)
_H3cPOESwitchStateInVolCA_Type=ACAlarmState
_H3cPOESwitchStateInVolCA_Object=MibTableColumn
h3cPOESwitchStateInVolCA=_H3cPOESwitchStateInVolCA_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,6,5,1,4),_H3cPOESwitchStateInVolCA_Type())
h3cPOESwitchStateInVolCA.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOESwitchStateInVolCA.setStatus(_A)
_H3cPOEAlarmStateObjects_ObjectIdentity=ObjectIdentity
h3cPOEAlarmStateObjects=_H3cPOEAlarmStateObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,14,8,7))
_H3cPOEAlarmStateModuleNum_Type=Integer32
_H3cPOEAlarmStateModuleNum_Object=MibScalar
h3cPOEAlarmStateModuleNum=_H3cPOEAlarmStateModuleNum_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,7,1),_H3cPOEAlarmStateModuleNum_Type())
h3cPOEAlarmStateModuleNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOEAlarmStateModuleNum.setStatus(_A)
_H3cPOEAlarmStateInfoTable_Object=MibTable
h3cPOEAlarmStateInfoTable=_H3cPOEAlarmStateInfoTable_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,7,2))
if mibBuilder.loadTexts:h3cPOEAlarmStateInfoTable.setStatus(_A)
_H3cPOEAlarmStateInfoEntry_Object=MibTableRow
h3cPOEAlarmStateInfoEntry=_H3cPOEAlarmStateInfoEntry_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,7,2,1))
h3cPOEAlarmStateInfoEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:h3cPOEAlarmStateInfoEntry.setStatus(_A)
class _H3cPOEAlarmModuleInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cPOEAlarmModuleInfoIndex_Type.__name__=_D
_H3cPOEAlarmModuleInfoIndex_Object=MibTableColumn
h3cPOEAlarmModuleInfoIndex=_H3cPOEAlarmModuleInfoIndex_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,7,2,1,1),_H3cPOEAlarmModuleInfoIndex_Type())
h3cPOEAlarmModuleInfoIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cPOEAlarmModuleInfoIndex.setStatus(_A)
_H3cPOEModuleDisconnect_Type=ModuleAlarmState
_H3cPOEModuleDisconnect_Object=MibTableColumn
h3cPOEModuleDisconnect=_H3cPOEModuleDisconnect_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,7,2,1,2),_H3cPOEModuleDisconnect_Type())
h3cPOEModuleDisconnect.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOEModuleDisconnect.setStatus(_A)
_H3cPOEModuleInputError_Type=ModuleAlarmState
_H3cPOEModuleInputError_Object=MibTableColumn
h3cPOEModuleInputError=_H3cPOEModuleInputError_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,7,2,1,3),_H3cPOEModuleInputError_Type())
h3cPOEModuleInputError.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOEModuleInputError.setStatus(_A)
_H3cPOEModuleOutputError_Type=ModuleAlarmState
_H3cPOEModuleOutputError_Object=MibTableColumn
h3cPOEModuleOutputError=_H3cPOEModuleOutputError_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,7,2,1,4),_H3cPOEModuleOutputError_Type())
h3cPOEModuleOutputError.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOEModuleOutputError.setStatus(_A)
_H3cPOEModuleOverVoltage_Type=ModuleAlarmState
_H3cPOEModuleOverVoltage_Object=MibTableColumn
h3cPOEModuleOverVoltage=_H3cPOEModuleOverVoltage_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,7,2,1,5),_H3cPOEModuleOverVoltage_Type())
h3cPOEModuleOverVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOEModuleOverVoltage.setStatus(_A)
_H3cPOEModuleOverTemp_Type=ModuleAlarmState
_H3cPOEModuleOverTemp_Object=MibTableColumn
h3cPOEModuleOverTemp=_H3cPOEModuleOverTemp_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,7,2,1,6),_H3cPOEModuleOverTemp_Type())
h3cPOEModuleOverTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOEModuleOverTemp.setStatus(_A)
_H3cPOEModuleFanError_Type=ModuleAlarmState
_H3cPOEModuleFanError_Object=MibTableColumn
h3cPOEModuleFanError=_H3cPOEModuleFanError_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,7,2,1,7),_H3cPOEModuleFanError_Type())
h3cPOEModuleFanError.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOEModuleFanError.setStatus(_A)
_H3cPOEModuleShutdown_Type=ModuleAlarmState
_H3cPOEModuleShutdown_Object=MibTableColumn
h3cPOEModuleShutdown=_H3cPOEModuleShutdown_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,7,2,1,8),_H3cPOEModuleShutdown_Type())
h3cPOEModuleShutdown.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOEModuleShutdown.setStatus(_A)
_H3cPOEModuleCurRestricted_Type=ModuleAlarmState
_H3cPOEModuleCurRestricted_Object=MibTableColumn
h3cPOEModuleCurRestricted=_H3cPOEModuleCurRestricted_Object((1,3,6,1,4,1,43,45,1,10,2,14,8,7,2,1,9),_H3cPOEModuleCurRestricted_Type())
h3cPOEModuleCurRestricted.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cPOEModuleCurRestricted.setStatus(_A)
class _H3cPsePolicyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_g,2)))
_H3cPsePolicyMode_Type.__name__=_D
_H3cPsePolicyMode_Object=MibScalar
h3cPsePolicyMode=_H3cPsePolicyMode_Object((1,3,6,1,4,1,43,45,1,10,2,14,9),_H3cPsePolicyMode_Type())
h3cPsePolicyMode.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPsePolicyMode.setStatus(_A)
class _H3cPDPolicyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_g,2)))
_H3cPDPolicyMode_Type.__name__=_D
_H3cPDPolicyMode_Object=MibScalar
h3cPDPolicyMode=_H3cPDPolicyMode_Object((1,3,6,1,4,1,43,45,1,10,2,14,10),_H3cPDPolicyMode_Type())
h3cPDPolicyMode.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cPDPolicyMode.setStatus(_A)
h3cPsePortGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,10,2,14,4,2,1))
h3cPsePortGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:h3cPsePortGroup.setStatus(_A)
h3cMainPseGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,10,2,14,4,2,2))
h3cMainPseGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:h3cMainPseGroup.setStatus(_A)
h3cPseScalarGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,10,2,14,4,2,3))
h3cPseScalarGroup.setObjects(*((_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:h3cPseScalarGroup.setStatus(_A)
h3cPsePDNotificationGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,10,2,14,4,2,4))
h3cPsePDNotificationGroup.setObjects((_B,_w))
if mibBuilder.loadTexts:h3cPsePDNotificationGroup.setStatus(_A)
h3cPseProfilesGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,10,2,14,4,2,5))
h3cPseProfilesGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:h3cPseProfilesGroup.setStatus(_A)
h3cPOEPowerThresholdLimitGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,10,2,14,4,2,6))
h3cPOEPowerThresholdLimitGroup.setObjects(*((_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:h3cPOEPowerThresholdLimitGroup.setStatus(_A)
h3cPOEPowerSupInfoGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,10,2,14,4,2,7))
h3cPOEPowerSupInfoGroup.setObjects(*((_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:h3cPOEPowerSupInfoGroup.setStatus(_A)
h3cPOEPowerDCOutStateGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,10,2,14,4,2,8))
h3cPOEPowerDCOutStateGroup.setObjects((_B,_AE))
if mibBuilder.loadTexts:h3cPOEPowerDCOutStateGroup.setStatus(_A)
h3cPOEPowerDCOutInfoGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,10,2,14,4,2,9))
h3cPOEPowerDCOutInfoGroup.setObjects((_B,_AF))
if mibBuilder.loadTexts:h3cPOEPowerDCOutInfoGroup.setStatus(_A)
h3cPOEPowerACSwitchStateModuleGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,10,2,14,4,2,10))
h3cPOEPowerACSwitchStateModuleGroup.setObjects((_B,_AG))
if mibBuilder.loadTexts:h3cPOEPowerACSwitchStateModuleGroup.setStatus(_A)
h3cPOEPowerInCurStateGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,10,2,14,4,2,11))
h3cPOEPowerInCurStateGroup.setObjects(*((_B,_AH),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:h3cPOEPowerInCurStateGroup.setStatus(_A)
h3cPOEPowerAlarmStateGroup=ObjectGroup((1,3,6,1,4,1,43,45,1,10,2,14,4,2,12))
h3cPOEPowerAlarmStateGroup.setObjects((_B,_AI))
if mibBuilder.loadTexts:h3cPOEPowerAlarmStateGroup.setStatus(_A)
h3cpsePDChangeNotification=NotificationType((1,3,6,1,4,1,43,45,1,10,2,14,6,1))
h3cpsePDChangeNotification.setObjects((_J,_T))
if mibBuilder.loadTexts:h3cpsePDChangeNotification.setStatus(_A)
h3cPOEDisconnectNotification=NotificationType((1,3,6,1,4,1,43,45,1,10,2,14,6,2))
h3cPOEDisconnectNotification.setObjects(*((_B,_G),(_B,_AJ)))
if mibBuilder.loadTexts:h3cPOEDisconnectNotification.setStatus(_A)
h3cPOEInputErrorNotification=NotificationType((1,3,6,1,4,1,43,45,1,10,2,14,6,3))
h3cPOEInputErrorNotification.setObjects(*((_B,_G),(_B,_AK)))
if mibBuilder.loadTexts:h3cPOEInputErrorNotification.setStatus(_A)
h3cPOEOutputErrorNotification=NotificationType((1,3,6,1,4,1,43,45,1,10,2,14,6,4))
h3cPOEOutputErrorNotification.setObjects(*((_B,_G),(_B,_AL)))
if mibBuilder.loadTexts:h3cPOEOutputErrorNotification.setStatus(_A)
h3cPOEOverVoltageNotification=NotificationType((1,3,6,1,4,1,43,45,1,10,2,14,6,5))
h3cPOEOverVoltageNotification.setObjects(*((_B,_G),(_B,_AM)))
if mibBuilder.loadTexts:h3cPOEOverVoltageNotification.setStatus(_A)
h3cPOEOverTempNotification=NotificationType((1,3,6,1,4,1,43,45,1,10,2,14,6,6))
h3cPOEOverTempNotification.setObjects(*((_B,_G),(_B,_AN)))
if mibBuilder.loadTexts:h3cPOEOverTempNotification.setStatus(_A)
h3cPOEFanErrorNotification=NotificationType((1,3,6,1,4,1,43,45,1,10,2,14,6,7))
h3cPOEFanErrorNotification.setObjects(*((_B,_G),(_B,_AO)))
if mibBuilder.loadTexts:h3cPOEFanErrorNotification.setStatus(_A)
h3cPOEModuleShutdownNotification=NotificationType((1,3,6,1,4,1,43,45,1,10,2,14,6,8))
h3cPOEModuleShutdownNotification.setObjects(*((_B,_G),(_B,_AP)))
if mibBuilder.loadTexts:h3cPOEModuleShutdownNotification.setStatus(_A)
h3cPOECurRestrictedNotification=NotificationType((1,3,6,1,4,1,43,45,1,10,2,14,6,9))
h3cPOECurRestrictedNotification.setObjects(*((_B,_G),(_B,_AQ)))
if mibBuilder.loadTexts:h3cPOECurRestrictedNotification.setStatus(_A)
h3cPOEACSwitchNotification=NotificationType((1,3,6,1,4,1,43,45,1,10,2,14,6,10))
h3cPOEACSwitchNotification.setObjects(*((_B,_O),(_B,_AR)))
if mibBuilder.loadTexts:h3cPOEACSwitchNotification.setStatus(_A)
h3cPOEACInCurANotification=NotificationType((1,3,6,1,4,1,43,45,1,10,2,14,6,11))
h3cPOEACInCurANotification.setObjects((_B,_P))
if mibBuilder.loadTexts:h3cPOEACInCurANotification.setStatus(_A)
h3cPOEACInCurBNotification=NotificationType((1,3,6,1,4,1,43,45,1,10,2,14,6,12))
h3cPOEACInCurBNotification.setObjects((_B,_Q))
if mibBuilder.loadTexts:h3cPOEACInCurBNotification.setStatus(_A)
h3cPOEACInCurCNotification=NotificationType((1,3,6,1,4,1,43,45,1,10,2,14,6,13))
h3cPOEACInCurCNotification.setObjects((_B,_R))
if mibBuilder.loadTexts:h3cPOEACInCurCNotification.setStatus(_A)
h3cPOEACSwitchVolABNotification=NotificationType((1,3,6,1,4,1,43,45,1,10,2,14,6,14))
h3cPOEACSwitchVolABNotification.setObjects(*((_B,_K),(_B,_AS)))
if mibBuilder.loadTexts:h3cPOEACSwitchVolABNotification.setStatus(_A)
h3cPOEACSwitchVolBCNotification=NotificationType((1,3,6,1,4,1,43,45,1,10,2,14,6,15))
h3cPOEACSwitchVolBCNotification.setObjects(*((_B,_K),(_B,_AT)))
if mibBuilder.loadTexts:h3cPOEACSwitchVolBCNotification.setStatus(_A)
h3cPOEACSwitchVolCANotification=NotificationType((1,3,6,1,4,1,43,45,1,10,2,14,6,16))
h3cPOEACSwitchVolCANotification.setObjects(*((_B,_K),(_B,_AU)))
if mibBuilder.loadTexts:h3cPOEACSwitchVolCANotification.setStatus(_A)
h3cPOEDCOutVolNotification=NotificationType((1,3,6,1,4,1,43,45,1,10,2,14,6,17))
h3cPOEDCOutVolNotification.setObjects(*((_B,_N),(_B,_AV)))
if mibBuilder.loadTexts:h3cPOEDCOutVolNotification.setStatus(_A)
h3cPOEShutdownNotification=NotificationType((1,3,6,1,4,1,43,45,1,10,2,14,6,18))
if mibBuilder.loadTexts:h3cPOEShutdownNotification.setStatus(_A)
h3cPseCompliance=ModuleCompliance((1,3,6,1,4,1,43,45,1,10,2,14,4,1,1))
h3cPseCompliance.setObjects(*((_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa)))
if mibBuilder.loadTexts:h3cPseCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ACAlarmState':ACAlarmState,'DCAlarmState':DCAlarmState,'SwitchState':SwitchState,'ModuleAlarmState':ModuleAlarmState,'h3cPowerEthernetExt':h3cPowerEthernetExt,'h3cPsePortTable':h3cPsePortTable,'h3cPsePortEntry':h3cPsePortEntry,_m:h3cPsePortFaultDescription,_l:h3cPsePortPeakPower,_k:h3cPsePortAveragePower,_j:h3cPsePortCurrentPower,_i:h3cPsePortPowerLimit,_h:h3cPsePortProfileIndex,'h3cMainPseTable':h3cMainPseTable,'h3cMainPseEntry':h3cMainPseEntry,_o:h3cMainPsePowerLimit,_p:h3cMainPseAveragePower,_q:h3cMainPsePeakPower,_r:h3cMainGuaranteedPowerRemaining,_n:h3cMainPsePriorityMode,'h3cMainPseLegacy':h3cMainPseLegacy,'h3cMainPsePowerPriority':h3cMainPsePowerPriority,_s:h3cPseAutoDetectActive,'h3cPseComformance':h3cPseComformance,'h3cPseCompliances':h3cPseCompliances,'h3cPseCompliance':h3cPseCompliance,'h3cPseGroup':h3cPseGroup,_AW:h3cPsePortGroup,_AX:h3cMainPseGroup,_AY:h3cPseScalarGroup,_AZ:h3cPsePDNotificationGroup,_Aa:h3cPseProfilesGroup,'h3cPOEPowerThresholdLimitGroup':h3cPOEPowerThresholdLimitGroup,'h3cPOEPowerSupInfoGroup':h3cPOEPowerSupInfoGroup,'h3cPOEPowerDCOutStateGroup':h3cPOEPowerDCOutStateGroup,'h3cPOEPowerDCOutInfoGroup':h3cPOEPowerDCOutInfoGroup,'h3cPOEPowerACSwitchStateModuleGroup':h3cPOEPowerACSwitchStateModuleGroup,'h3cPOEPowerInCurStateGroup':h3cPOEPowerInCurStateGroup,'h3cPOEPowerAlarmStateGroup':h3cPOEPowerAlarmStateGroup,_t:h3cPsePowerMaxValue,'h3cpseportNotification':h3cpseportNotification,_w:h3cpsePDChangeNotification,'h3cPOEDisconnectNotification':h3cPOEDisconnectNotification,'h3cPOEInputErrorNotification':h3cPOEInputErrorNotification,'h3cPOEOutputErrorNotification':h3cPOEOutputErrorNotification,'h3cPOEOverVoltageNotification':h3cPOEOverVoltageNotification,'h3cPOEOverTempNotification':h3cPOEOverTempNotification,'h3cPOEFanErrorNotification':h3cPOEFanErrorNotification,'h3cPOEModuleShutdownNotification':h3cPOEModuleShutdownNotification,'h3cPOECurRestrictedNotification':h3cPOECurRestrictedNotification,'h3cPOEACSwitchNotification':h3cPOEACSwitchNotification,'h3cPOEACInCurANotification':h3cPOEACInCurANotification,'h3cPOEACInCurBNotification':h3cPOEACInCurBNotification,'h3cPOEACInCurCNotification':h3cPOEACInCurCNotification,'h3cPOEACSwitchVolABNotification':h3cPOEACSwitchVolABNotification,'h3cPOEACSwitchVolBCNotification':h3cPOEACSwitchVolBCNotification,'h3cPOEACSwitchVolCANotification':h3cPOEACSwitchVolCANotification,'h3cPOEDCOutVolNotification':h3cPOEDCOutVolNotification,'h3cPOEShutdownNotification':h3cPOEShutdownNotification,'h3cPseProfilesTable':h3cPseProfilesTable,'h3cPseProfilesEntry':h3cPseProfilesEntry,_d:h3cPseProfileIndex,_x:h3cPseProfileName,_y:h3cPseProfilePowerMode,_z:h3cPseProfilePowerLimit,_A0:h3cPseProfilePriority,_A1:h3cPseProfilePairs,_A2:h3cPseProfileApplyNum,_A3:h3cPseProfileRowStatus,'h3cPOEPowerObjects':h3cPOEPowerObjects,'h3cPOEThresholdLimitObjs':h3cPOEThresholdLimitObjs,_A4:h3cPOEThresholdACMimimum,_A5:h3cPOEThresholdACMaximum,_A6:h3cPOEThresholdDCMinimum,_A7:h3cPOEThresholdDCMaximum,'h3cPOESupModuleInfoObjs':h3cPOESupModuleInfoObjs,_A8:h3cPOEPowerType,_A9:h3cPOEPowerModuleNum,_AA:h3cPOESupervisionModuleName,_AB:h3cPOESMMajorVersion,_AC:h3cPOESMMinorVersion,_AD:h3cPOESMFactorName,'h3cPOEModuleInfoTable':h3cPOEModuleInfoTable,'h3cPOEModuleInfoEntry':h3cPOEModuleInfoEntry,_e:h3cPOEModuleIndex,'h3cPOEModuleID':h3cPOEModuleID,'h3cPOEModuleInfoPower':h3cPOEModuleInfoPower,'h3cPOEModuleHardVerInfo':h3cPOEModuleHardVerInfo,'h3cPOEDCOutStateObjects':h3cPOEDCOutStateObjects,_AE:h3cPOEDCOutStateModuleNum,'h3cPOEDCOutStateTable':h3cPOEDCOutStateTable,'h3cPOEDCOutStateEntry':h3cPOEDCOutStateEntry,_N:h3cPOEDCOutStateIndex,_AV:h3cPOEDCOutDCVolAlarm,'h3cPOEDCOutInfoObjects':h3cPOEDCOutInfoObjects,_AF:h3cPOEDCOutCurNum,'h3cPOEDCOutInfoTable':h3cPOEDCOutInfoTable,'h3cPOEDCOutInfoEntry':h3cPOEDCOutInfoEntry,_f:h3cPOEDCOutInfoIndex,'h3cPOEDCOutVol':h3cPOEDCOutVol,'h3cPOEDCOutInfoLoadCur':h3cPOEDCOutInfoLoadCur,'h3cPOEACSwitchStateModuleObjs':h3cPOEACSwitchStateModuleObjs,_AG:h3cPOEACSwitchStateModuleNum,'h3cPOEACSwitchStateTable':h3cPOEACSwitchStateTable,'h3cPOEACSwitchStateEntry':h3cPOEACSwitchStateEntry,_O:h3cPOEACSwitchStateIndex,_AR:h3cPOEACSwitchState,'h3cPOEInCurStateObjects':h3cPOEInCurStateObjects,_AH:h3cPOEInCurStateModuleNum,_P:h3cPOEInCurAState,_Q:h3cPOEInCurBState,_R:h3cPOEInCurCState,'h3cPOESwitchStateVolExTable':h3cPOESwitchStateVolExTable,'h3cPOESwitchStateVolExEntry':h3cPOESwitchStateVolExEntry,_K:h3cPOESwitchStateVolExIndex,_AS:h3cPOESwitchStateInVolAB,_AT:h3cPOESwitchStateInVolBC,_AU:h3cPOESwitchStateInVolCA,'h3cPOEAlarmStateObjects':h3cPOEAlarmStateObjects,_AI:h3cPOEAlarmStateModuleNum,'h3cPOEAlarmStateInfoTable':h3cPOEAlarmStateInfoTable,'h3cPOEAlarmStateInfoEntry':h3cPOEAlarmStateInfoEntry,_G:h3cPOEAlarmModuleInfoIndex,_AJ:h3cPOEModuleDisconnect,_AK:h3cPOEModuleInputError,_AL:h3cPOEModuleOutputError,_AM:h3cPOEModuleOverVoltage,_AN:h3cPOEModuleOverTemp,_AO:h3cPOEModuleFanError,_AP:h3cPOEModuleShutdown,_AQ:h3cPOEModuleCurRestricted,_u:h3cPsePolicyMode,_v:h3cPDPolicyMode})