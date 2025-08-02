_Aa='hpnicfPseProfilesGroup'
_AZ='hpnicfPsePDNotificationGroup'
_AY='hpnicfPseScalarGroup'
_AX='hpnicfMainPseGroup'
_AW='hpnicfPsePortGroup'
_AV='hpnicfPOEDCOutDCVolAlarm'
_AU='hpnicfPOESwitchStateInVolCA'
_AT='hpnicfPOESwitchStateInVolBC'
_AS='hpnicfPOESwitchStateInVolAB'
_AR='hpnicfPOEACSwitchState'
_AQ='hpnicfPOEModuleCurRestricted'
_AP='hpnicfPOEModuleShutdown'
_AO='hpnicfPOEModuleFanError'
_AN='hpnicfPOEModuleOverTemp'
_AM='hpnicfPOEModuleOverVoltage'
_AL='hpnicfPOEModuleOutputError'
_AK='hpnicfPOEModuleInputError'
_AJ='hpnicfPOEModuleDisconnect'
_AI='hpnicfPOEAlarmStateModuleNum'
_AH='hpnicfPOEInCurStateModuleNum'
_AG='hpnicfPOEACSwitchStateModuleNum'
_AF='hpnicfPOEDCOutCurNum'
_AE='hpnicfPOEDCOutStateModuleNum'
_AD='hpnicfPOESMFactorName'
_AC='hpnicfPOESMMinorVersion'
_AB='hpnicfPOESMMajorVersion'
_AA='hpnicfPOESupervisionModuleName'
_A9='hpnicfPOEPowerModuleNum'
_A8='hpnicfPOEPowerType'
_A7='hpnicfPOEThresholdDCMaximum'
_A6='hpnicfPOEThresholdDCMinimum'
_A5='hpnicfPOEThresholdACMaximum'
_A4='hpnicfPOEThresholdACMimimum'
_A3='hpnicfPseProfileRowStatus'
_A2='hpnicfPseProfileApplyNum'
_A1='hpnicfPseProfilePairs'
_A0='hpnicfPseProfilePriority'
_z='hpnicfPseProfilePowerLimit'
_y='hpnicfPseProfilePowerMode'
_x='hpnicfPseProfileName'
_w='hpnicfpsePDChangeNotification'
_v='hpnicfPDPolicyMode'
_u='hpnicfPsePolicyMode'
_t='hpnicfPsePowerMaxValue'
_s='hpnicfPseAutoDetectActive'
_r='hpnicfMainGuaranteedPowerRemaining'
_q='hpnicfMainPsePeakPower'
_p='hpnicfMainPseAveragePower'
_o='hpnicfMainPsePowerLimit'
_n='hpnicfMainPsePriorityMode'
_m='hpnicfPsePortFaultDescription'
_l='hpnicfPsePortPeakPower'
_k='hpnicfPsePortAveragePower'
_j='hpnicfPsePortCurrentPower'
_i='hpnicfPsePortPowerLimit'
_h='hpnicfPsePortProfileIndex'
_g='priority'
_f='hpnicfPOEDCOutInfoIndex'
_e='hpnicfPOEModuleIndex'
_d='hpnicfPseProfileIndex'
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
_R='hpnicfPOEInCurCState'
_Q='hpnicfPOEInCurBState'
_P='hpnicfPOEInCurAState'
_O='hpnicfPOEACSwitchStateIndex'
_N='hpnicfPOEDCOutStateIndex'
_M='disabled'
_L='normal'
_K='hpnicfPOESwitchStateVolExIndex'
_J='POWER-ETHERNET-MIB'
_I='accessible-for-notify'
_H='read-create'
_G='hpnicfPOEAlarmModuleInfoIndex'
_F='OctetString'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='HPN-ICF-POWER-ETH-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
pethMainPseGroupIndex,pethPsePortDetectionStatus,pethPsePortGroupIndex,pethPsePortIndex=mibBuilder.importSymbols(_J,_S,_T,_U,_V)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_W,'PhysAddress','RowStatus','TextualConvention')
hpnicfPowerEthernetExt=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,14))
class ACAlarmState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_L,1),(_X,2),(_Y,3),('lackPhrase',4),(_Z,5),(_a,6),(_b,7)))
class DCAlarmState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_L,1),(_X,2),(_Y,3),(_Z,4),(_a,5),(_b,6)))
class SwitchState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('on',1),('off',2),('highVoltInput',3),('lowVoltInput',4)))
class ModuleAlarmState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_L,1),('alarm',2)))
_HpnicfPsePortTable_Object=MibTable
hpnicfPsePortTable=_HpnicfPsePortTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,1))
if mibBuilder.loadTexts:hpnicfPsePortTable.setStatus(_A)
_HpnicfPsePortEntry_Object=MibTableRow
hpnicfPsePortEntry=_HpnicfPsePortEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,1,1))
hpnicfPsePortEntry.setIndexNames((0,_J,_U),(0,_J,_V))
if mibBuilder.loadTexts:hpnicfPsePortEntry.setStatus(_A)
_HpnicfPsePortFaultDescription_Type=DisplayString
_HpnicfPsePortFaultDescription_Object=MibTableColumn
hpnicfPsePortFaultDescription=_HpnicfPsePortFaultDescription_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,1,1,2),_HpnicfPsePortFaultDescription_Type())
hpnicfPsePortFaultDescription.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPsePortFaultDescription.setStatus(_A)
_HpnicfPsePortPeakPower_Type=Integer32
_HpnicfPsePortPeakPower_Object=MibTableColumn
hpnicfPsePortPeakPower=_HpnicfPsePortPeakPower_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,1,1,3),_HpnicfPsePortPeakPower_Type())
hpnicfPsePortPeakPower.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPsePortPeakPower.setStatus(_A)
_HpnicfPsePortAveragePower_Type=Integer32
_HpnicfPsePortAveragePower_Object=MibTableColumn
hpnicfPsePortAveragePower=_HpnicfPsePortAveragePower_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,1,1,4),_HpnicfPsePortAveragePower_Type())
hpnicfPsePortAveragePower.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPsePortAveragePower.setStatus(_A)
_HpnicfPsePortCurrentPower_Type=Integer32
_HpnicfPsePortCurrentPower_Object=MibTableColumn
hpnicfPsePortCurrentPower=_HpnicfPsePortCurrentPower_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,1,1,5),_HpnicfPsePortCurrentPower_Type())
hpnicfPsePortCurrentPower.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPsePortCurrentPower.setStatus(_A)
_HpnicfPsePortPowerLimit_Type=Integer32
_HpnicfPsePortPowerLimit_Object=MibTableColumn
hpnicfPsePortPowerLimit=_HpnicfPsePortPowerLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,1,1,6),_HpnicfPsePortPowerLimit_Type())
hpnicfPsePortPowerLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPsePortPowerLimit.setStatus(_A)
class _HpnicfPsePortProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfPsePortProfileIndex_Type.__name__=_D
_HpnicfPsePortProfileIndex_Object=MibTableColumn
hpnicfPsePortProfileIndex=_HpnicfPsePortProfileIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,1,1,7),_HpnicfPsePortProfileIndex_Type())
hpnicfPsePortProfileIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPsePortProfileIndex.setStatus(_A)
_HpnicfMainPseTable_Object=MibTable
hpnicfMainPseTable=_HpnicfMainPseTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,2))
if mibBuilder.loadTexts:hpnicfMainPseTable.setStatus(_A)
_HpnicfMainPseEntry_Object=MibTableRow
hpnicfMainPseEntry=_HpnicfMainPseEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,2,1))
hpnicfMainPseEntry.setIndexNames((0,_J,_S))
if mibBuilder.loadTexts:hpnicfMainPseEntry.setStatus(_A)
_HpnicfMainPsePowerLimit_Type=Integer32
_HpnicfMainPsePowerLimit_Object=MibTableColumn
hpnicfMainPsePowerLimit=_HpnicfMainPsePowerLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,2,1,1),_HpnicfMainPsePowerLimit_Type())
hpnicfMainPsePowerLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMainPsePowerLimit.setStatus(_A)
_HpnicfMainPseAveragePower_Type=Integer32
_HpnicfMainPseAveragePower_Object=MibTableColumn
hpnicfMainPseAveragePower=_HpnicfMainPseAveragePower_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,2,1,2),_HpnicfMainPseAveragePower_Type())
hpnicfMainPseAveragePower.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMainPseAveragePower.setStatus(_A)
_HpnicfMainPsePeakPower_Type=Integer32
_HpnicfMainPsePeakPower_Object=MibTableColumn
hpnicfMainPsePeakPower=_HpnicfMainPsePeakPower_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,2,1,3),_HpnicfMainPsePeakPower_Type())
hpnicfMainPsePeakPower.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMainPsePeakPower.setStatus(_A)
_HpnicfMainGuaranteedPowerRemaining_Type=Integer32
_HpnicfMainGuaranteedPowerRemaining_Object=MibTableColumn
hpnicfMainGuaranteedPowerRemaining=_HpnicfMainGuaranteedPowerRemaining_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,2,1,4),_HpnicfMainGuaranteedPowerRemaining_Type())
hpnicfMainGuaranteedPowerRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMainGuaranteedPowerRemaining.setStatus(_A)
class _HpnicfMainPsePriorityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disconnection',0),('non-disconnection',1)))
_HpnicfMainPsePriorityMode_Type.__name__=_D
_HpnicfMainPsePriorityMode_Object=MibTableColumn
hpnicfMainPsePriorityMode=_HpnicfMainPsePriorityMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,2,1,5),_HpnicfMainPsePriorityMode_Type())
hpnicfMainPsePriorityMode.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMainPsePriorityMode.setStatus(_A)
class _HpnicfMainPseLegacy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('enable',0),('disable',1)))
_HpnicfMainPseLegacy_Type.__name__=_D
_HpnicfMainPseLegacy_Object=MibTableColumn
hpnicfMainPseLegacy=_HpnicfMainPseLegacy_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,2,1,6),_HpnicfMainPseLegacy_Type())
hpnicfMainPseLegacy.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMainPseLegacy.setStatus(_A)
class _HpnicfMainPsePowerPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_c,1),('high',2),('low',3)))
_HpnicfMainPsePowerPriority_Type.__name__=_D
_HpnicfMainPsePowerPriority_Object=MibTableColumn
hpnicfMainPsePowerPriority=_HpnicfMainPsePowerPriority_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,2,1,7),_HpnicfMainPsePowerPriority_Type())
hpnicfMainPsePowerPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMainPsePowerPriority.setStatus(_A)
class _HpnicfPseAutoDetectActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notSupported',1),(_M,2),('enabled',3)))
_HpnicfPseAutoDetectActive_Type.__name__=_D
_HpnicfPseAutoDetectActive_Object=MibScalar
hpnicfPseAutoDetectActive=_HpnicfPseAutoDetectActive_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,3),_HpnicfPseAutoDetectActive_Type())
hpnicfPseAutoDetectActive.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPseAutoDetectActive.setStatus(_A)
_HpnicfPseComformance_ObjectIdentity=ObjectIdentity
hpnicfPseComformance=_HpnicfPseComformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,14,4))
_HpnicfPseCompliances_ObjectIdentity=ObjectIdentity
hpnicfPseCompliances=_HpnicfPseCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,14,4,1))
_HpnicfPseGroup_ObjectIdentity=ObjectIdentity
hpnicfPseGroup=_HpnicfPseGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,14,4,2))
_HpnicfPsePowerMaxValue_Type=Integer32
_HpnicfPsePowerMaxValue_Object=MibScalar
hpnicfPsePowerMaxValue=_HpnicfPsePowerMaxValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,5),_HpnicfPsePowerMaxValue_Type())
hpnicfPsePowerMaxValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPsePowerMaxValue.setStatus(_A)
_HpnicfpseportNotification_ObjectIdentity=ObjectIdentity
hpnicfpseportNotification=_HpnicfpseportNotification_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,14,6))
_HpnicfPseProfilesTable_Object=MibTable
hpnicfPseProfilesTable=_HpnicfPseProfilesTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,7))
if mibBuilder.loadTexts:hpnicfPseProfilesTable.setStatus(_A)
_HpnicfPseProfilesEntry_Object=MibTableRow
hpnicfPseProfilesEntry=_HpnicfPseProfilesEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,7,1))
hpnicfPseProfilesEntry.setIndexNames((0,_B,_d))
if mibBuilder.loadTexts:hpnicfPseProfilesEntry.setStatus(_A)
class _HpnicfPseProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpnicfPseProfileIndex_Type.__name__=_D
_HpnicfPseProfileIndex_Object=MibTableColumn
hpnicfPseProfileIndex=_HpnicfPseProfileIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,7,1,1),_HpnicfPseProfileIndex_Type())
hpnicfPseProfileIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpnicfPseProfileIndex.setStatus(_A)
class _HpnicfPseProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_HpnicfPseProfileName_Type.__name__=_W
_HpnicfPseProfileName_Object=MibTableColumn
hpnicfPseProfileName=_HpnicfPseProfileName_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,7,1,2),_HpnicfPseProfileName_Type())
hpnicfPseProfileName.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfPseProfileName.setStatus(_A)
class _HpnicfPseProfilePowerMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('powerDisabled',1),('powerEnabled',2)))
_HpnicfPseProfilePowerMode_Type.__name__=_D
_HpnicfPseProfilePowerMode_Object=MibTableColumn
hpnicfPseProfilePowerMode=_HpnicfPseProfilePowerMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,7,1,3),_HpnicfPseProfilePowerMode_Type())
hpnicfPseProfilePowerMode.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfPseProfilePowerMode.setStatus(_A)
class _HpnicfPseProfilePowerLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15400))
_HpnicfPseProfilePowerLimit_Type.__name__=_D
_HpnicfPseProfilePowerLimit_Object=MibTableColumn
hpnicfPseProfilePowerLimit=_HpnicfPseProfilePowerLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,7,1,4),_HpnicfPseProfilePowerLimit_Type())
hpnicfPseProfilePowerLimit.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfPseProfilePowerLimit.setStatus(_A)
class _HpnicfPseProfilePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_c,1),('high',2),('low',3)))
_HpnicfPseProfilePriority_Type.__name__=_D
_HpnicfPseProfilePriority_Object=MibTableColumn
hpnicfPseProfilePriority=_HpnicfPseProfilePriority_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,7,1,5),_HpnicfPseProfilePriority_Type())
hpnicfPseProfilePriority.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfPseProfilePriority.setStatus(_A)
class _HpnicfPseProfilePairs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('signal',1),('spare',2)))
_HpnicfPseProfilePairs_Type.__name__=_D
_HpnicfPseProfilePairs_Object=MibTableColumn
hpnicfPseProfilePairs=_HpnicfPseProfilePairs_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,7,1,6),_HpnicfPseProfilePairs_Type())
hpnicfPseProfilePairs.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfPseProfilePairs.setStatus(_A)
_HpnicfPseProfileApplyNum_Type=Integer32
_HpnicfPseProfileApplyNum_Object=MibTableColumn
hpnicfPseProfileApplyNum=_HpnicfPseProfileApplyNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,7,1,7),_HpnicfPseProfileApplyNum_Type())
hpnicfPseProfileApplyNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPseProfileApplyNum.setStatus(_A)
_HpnicfPseProfileRowStatus_Type=RowStatus
_HpnicfPseProfileRowStatus_Object=MibTableColumn
hpnicfPseProfileRowStatus=_HpnicfPseProfileRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,7,1,8),_HpnicfPseProfileRowStatus_Type())
hpnicfPseProfileRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfPseProfileRowStatus.setStatus(_A)
_HpnicfPOEPowerObjects_ObjectIdentity=ObjectIdentity
hpnicfPOEPowerObjects=_HpnicfPOEPowerObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,14,8))
_HpnicfPOEThresholdLimitObjs_ObjectIdentity=ObjectIdentity
hpnicfPOEThresholdLimitObjs=_HpnicfPOEThresholdLimitObjs_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,14,8,1))
class _HpnicfPOEThresholdACMimimum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_HpnicfPOEThresholdACMimimum_Type.__name__=_F
_HpnicfPOEThresholdACMimimum_Object=MibScalar
hpnicfPOEThresholdACMimimum=_HpnicfPOEThresholdACMimimum_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,1,1),_HpnicfPOEThresholdACMimimum_Type())
hpnicfPOEThresholdACMimimum.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPOEThresholdACMimimum.setStatus(_A)
class _HpnicfPOEThresholdACMaximum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_HpnicfPOEThresholdACMaximum_Type.__name__=_F
_HpnicfPOEThresholdACMaximum_Object=MibScalar
hpnicfPOEThresholdACMaximum=_HpnicfPOEThresholdACMaximum_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,1,2),_HpnicfPOEThresholdACMaximum_Type())
hpnicfPOEThresholdACMaximum.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPOEThresholdACMaximum.setStatus(_A)
class _HpnicfPOEThresholdDCMinimum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_HpnicfPOEThresholdDCMinimum_Type.__name__=_F
_HpnicfPOEThresholdDCMinimum_Object=MibScalar
hpnicfPOEThresholdDCMinimum=_HpnicfPOEThresholdDCMinimum_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,1,3),_HpnicfPOEThresholdDCMinimum_Type())
hpnicfPOEThresholdDCMinimum.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPOEThresholdDCMinimum.setStatus(_A)
class _HpnicfPOEThresholdDCMaximum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_HpnicfPOEThresholdDCMaximum_Type.__name__=_F
_HpnicfPOEThresholdDCMaximum_Object=MibScalar
hpnicfPOEThresholdDCMaximum=_HpnicfPOEThresholdDCMaximum_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,1,4),_HpnicfPOEThresholdDCMaximum_Type())
hpnicfPOEThresholdDCMaximum.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPOEThresholdDCMaximum.setStatus(_A)
_HpnicfPOESupModuleInfoObjs_ObjectIdentity=ObjectIdentity
hpnicfPOESupModuleInfoObjs=_HpnicfPOESupModuleInfoObjs_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,14,8,2))
class _HpnicfPOEPowerType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,127))
_HpnicfPOEPowerType_Type.__name__=_F
_HpnicfPOEPowerType_Object=MibScalar
hpnicfPOEPowerType=_HpnicfPOEPowerType_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,2,1),_HpnicfPOEPowerType_Type())
hpnicfPOEPowerType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOEPowerType.setStatus(_A)
_HpnicfPOEPowerModuleNum_Type=Integer32
_HpnicfPOEPowerModuleNum_Object=MibScalar
hpnicfPOEPowerModuleNum=_HpnicfPOEPowerModuleNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,2,2),_HpnicfPOEPowerModuleNum_Type())
hpnicfPOEPowerModuleNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOEPowerModuleNum.setStatus(_A)
class _HpnicfPOESupervisionModuleName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,127))
_HpnicfPOESupervisionModuleName_Type.__name__=_F
_HpnicfPOESupervisionModuleName_Object=MibScalar
hpnicfPOESupervisionModuleName=_HpnicfPOESupervisionModuleName_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,2,3),_HpnicfPOESupervisionModuleName_Type())
hpnicfPOESupervisionModuleName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOESupervisionModuleName.setStatus(_A)
_HpnicfPOESMMajorVersion_Type=Integer32
_HpnicfPOESMMajorVersion_Object=MibScalar
hpnicfPOESMMajorVersion=_HpnicfPOESMMajorVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,2,4),_HpnicfPOESMMajorVersion_Type())
hpnicfPOESMMajorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOESMMajorVersion.setStatus(_A)
_HpnicfPOESMMinorVersion_Type=Integer32
_HpnicfPOESMMinorVersion_Object=MibScalar
hpnicfPOESMMinorVersion=_HpnicfPOESMMinorVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,2,5),_HpnicfPOESMMinorVersion_Type())
hpnicfPOESMMinorVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOESMMinorVersion.setStatus(_A)
class _HpnicfPOESMFactorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,127))
_HpnicfPOESMFactorName_Type.__name__=_F
_HpnicfPOESMFactorName_Object=MibScalar
hpnicfPOESMFactorName=_HpnicfPOESMFactorName_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,2,6),_HpnicfPOESMFactorName_Type())
hpnicfPOESMFactorName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOESMFactorName.setStatus(_A)
_HpnicfPOEModuleInfoTable_Object=MibTable
hpnicfPOEModuleInfoTable=_HpnicfPOEModuleInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,2,7))
if mibBuilder.loadTexts:hpnicfPOEModuleInfoTable.setStatus(_A)
_HpnicfPOEModuleInfoEntry_Object=MibTableRow
hpnicfPOEModuleInfoEntry=_HpnicfPOEModuleInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,2,7,1))
hpnicfPOEModuleInfoEntry.setIndexNames((0,_B,_e))
if mibBuilder.loadTexts:hpnicfPOEModuleInfoEntry.setStatus(_A)
class _HpnicfPOEModuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfPOEModuleIndex_Type.__name__=_D
_HpnicfPOEModuleIndex_Object=MibTableColumn
hpnicfPOEModuleIndex=_HpnicfPOEModuleIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,2,7,1,1),_HpnicfPOEModuleIndex_Type())
hpnicfPOEModuleIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfPOEModuleIndex.setStatus(_A)
_HpnicfPOEModuleID_Type=Integer32
_HpnicfPOEModuleID_Object=MibTableColumn
hpnicfPOEModuleID=_HpnicfPOEModuleID_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,2,7,1,2),_HpnicfPOEModuleID_Type())
hpnicfPOEModuleID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOEModuleID.setStatus(_A)
_HpnicfPOEModuleInfoPower_Type=Integer32
_HpnicfPOEModuleInfoPower_Object=MibTableColumn
hpnicfPOEModuleInfoPower=_HpnicfPOEModuleInfoPower_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,2,7,1,3),_HpnicfPOEModuleInfoPower_Type())
hpnicfPOEModuleInfoPower.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOEModuleInfoPower.setStatus(_A)
class _HpnicfPOEModuleHardVerInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,127))
_HpnicfPOEModuleHardVerInfo_Type.__name__=_F
_HpnicfPOEModuleHardVerInfo_Object=MibTableColumn
hpnicfPOEModuleHardVerInfo=_HpnicfPOEModuleHardVerInfo_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,2,7,1,4),_HpnicfPOEModuleHardVerInfo_Type())
hpnicfPOEModuleHardVerInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOEModuleHardVerInfo.setStatus(_A)
_HpnicfPOEDCOutStateObjects_ObjectIdentity=ObjectIdentity
hpnicfPOEDCOutStateObjects=_HpnicfPOEDCOutStateObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,14,8,3))
_HpnicfPOEDCOutStateModuleNum_Type=Integer32
_HpnicfPOEDCOutStateModuleNum_Object=MibScalar
hpnicfPOEDCOutStateModuleNum=_HpnicfPOEDCOutStateModuleNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,3,1),_HpnicfPOEDCOutStateModuleNum_Type())
hpnicfPOEDCOutStateModuleNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOEDCOutStateModuleNum.setStatus(_A)
_HpnicfPOEDCOutStateTable_Object=MibTable
hpnicfPOEDCOutStateTable=_HpnicfPOEDCOutStateTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,3,2))
if mibBuilder.loadTexts:hpnicfPOEDCOutStateTable.setStatus(_A)
_HpnicfPOEDCOutStateEntry_Object=MibTableRow
hpnicfPOEDCOutStateEntry=_HpnicfPOEDCOutStateEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,3,2,1))
hpnicfPOEDCOutStateEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:hpnicfPOEDCOutStateEntry.setStatus(_A)
class _HpnicfPOEDCOutStateIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfPOEDCOutStateIndex_Type.__name__=_D
_HpnicfPOEDCOutStateIndex_Object=MibTableColumn
hpnicfPOEDCOutStateIndex=_HpnicfPOEDCOutStateIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,3,2,1,1),_HpnicfPOEDCOutStateIndex_Type())
hpnicfPOEDCOutStateIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfPOEDCOutStateIndex.setStatus(_A)
_HpnicfPOEDCOutDCVolAlarm_Type=DCAlarmState
_HpnicfPOEDCOutDCVolAlarm_Object=MibTableColumn
hpnicfPOEDCOutDCVolAlarm=_HpnicfPOEDCOutDCVolAlarm_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,3,2,1,2),_HpnicfPOEDCOutDCVolAlarm_Type())
hpnicfPOEDCOutDCVolAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOEDCOutDCVolAlarm.setStatus(_A)
_HpnicfPOEDCOutInfoObjects_ObjectIdentity=ObjectIdentity
hpnicfPOEDCOutInfoObjects=_HpnicfPOEDCOutInfoObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,14,8,4))
_HpnicfPOEDCOutCurNum_Type=Integer32
_HpnicfPOEDCOutCurNum_Object=MibScalar
hpnicfPOEDCOutCurNum=_HpnicfPOEDCOutCurNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,4,1),_HpnicfPOEDCOutCurNum_Type())
hpnicfPOEDCOutCurNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOEDCOutCurNum.setStatus(_A)
_HpnicfPOEDCOutInfoTable_Object=MibTable
hpnicfPOEDCOutInfoTable=_HpnicfPOEDCOutInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,4,2))
if mibBuilder.loadTexts:hpnicfPOEDCOutInfoTable.setStatus(_A)
_HpnicfPOEDCOutInfoEntry_Object=MibTableRow
hpnicfPOEDCOutInfoEntry=_HpnicfPOEDCOutInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,4,2,1))
hpnicfPOEDCOutInfoEntry.setIndexNames((0,_B,_f))
if mibBuilder.loadTexts:hpnicfPOEDCOutInfoEntry.setStatus(_A)
class _HpnicfPOEDCOutInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfPOEDCOutInfoIndex_Type.__name__=_D
_HpnicfPOEDCOutInfoIndex_Object=MibTableColumn
hpnicfPOEDCOutInfoIndex=_HpnicfPOEDCOutInfoIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,4,2,1,1),_HpnicfPOEDCOutInfoIndex_Type())
hpnicfPOEDCOutInfoIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfPOEDCOutInfoIndex.setStatus(_A)
class _HpnicfPOEDCOutVol_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_HpnicfPOEDCOutVol_Type.__name__=_F
_HpnicfPOEDCOutVol_Object=MibTableColumn
hpnicfPOEDCOutVol=_HpnicfPOEDCOutVol_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,4,2,1,2),_HpnicfPOEDCOutVol_Type())
hpnicfPOEDCOutVol.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOEDCOutVol.setStatus(_A)
class _HpnicfPOEDCOutInfoLoadCur_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,10))
_HpnicfPOEDCOutInfoLoadCur_Type.__name__=_F
_HpnicfPOEDCOutInfoLoadCur_Object=MibTableColumn
hpnicfPOEDCOutInfoLoadCur=_HpnicfPOEDCOutInfoLoadCur_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,4,2,1,3),_HpnicfPOEDCOutInfoLoadCur_Type())
hpnicfPOEDCOutInfoLoadCur.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOEDCOutInfoLoadCur.setStatus(_A)
_HpnicfPOEACSwitchStateModuleObjs_ObjectIdentity=ObjectIdentity
hpnicfPOEACSwitchStateModuleObjs=_HpnicfPOEACSwitchStateModuleObjs_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,14,8,5))
_HpnicfPOEACSwitchStateModuleNum_Type=Integer32
_HpnicfPOEACSwitchStateModuleNum_Object=MibScalar
hpnicfPOEACSwitchStateModuleNum=_HpnicfPOEACSwitchStateModuleNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,5,1),_HpnicfPOEACSwitchStateModuleNum_Type())
hpnicfPOEACSwitchStateModuleNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOEACSwitchStateModuleNum.setStatus(_A)
_HpnicfPOEACSwitchStateTable_Object=MibTable
hpnicfPOEACSwitchStateTable=_HpnicfPOEACSwitchStateTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,5,2))
if mibBuilder.loadTexts:hpnicfPOEACSwitchStateTable.setStatus(_A)
_HpnicfPOEACSwitchStateEntry_Object=MibTableRow
hpnicfPOEACSwitchStateEntry=_HpnicfPOEACSwitchStateEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,5,2,1))
hpnicfPOEACSwitchStateEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:hpnicfPOEACSwitchStateEntry.setStatus(_A)
class _HpnicfPOEACSwitchStateIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfPOEACSwitchStateIndex_Type.__name__=_D
_HpnicfPOEACSwitchStateIndex_Object=MibTableColumn
hpnicfPOEACSwitchStateIndex=_HpnicfPOEACSwitchStateIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,5,2,1,1),_HpnicfPOEACSwitchStateIndex_Type())
hpnicfPOEACSwitchStateIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfPOEACSwitchStateIndex.setStatus(_A)
_HpnicfPOEACSwitchState_Type=SwitchState
_HpnicfPOEACSwitchState_Object=MibTableColumn
hpnicfPOEACSwitchState=_HpnicfPOEACSwitchState_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,5,2,1,2),_HpnicfPOEACSwitchState_Type())
hpnicfPOEACSwitchState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOEACSwitchState.setStatus(_A)
_HpnicfPOEInCurStateObjects_ObjectIdentity=ObjectIdentity
hpnicfPOEInCurStateObjects=_HpnicfPOEInCurStateObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,14,8,6))
_HpnicfPOEInCurStateModuleNum_Type=Integer32
_HpnicfPOEInCurStateModuleNum_Object=MibScalar
hpnicfPOEInCurStateModuleNum=_HpnicfPOEInCurStateModuleNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,6,1),_HpnicfPOEInCurStateModuleNum_Type())
hpnicfPOEInCurStateModuleNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOEInCurStateModuleNum.setStatus(_A)
_HpnicfPOEInCurAState_Type=ACAlarmState
_HpnicfPOEInCurAState_Object=MibScalar
hpnicfPOEInCurAState=_HpnicfPOEInCurAState_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,6,2),_HpnicfPOEInCurAState_Type())
hpnicfPOEInCurAState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOEInCurAState.setStatus(_A)
_HpnicfPOEInCurBState_Type=ACAlarmState
_HpnicfPOEInCurBState_Object=MibScalar
hpnicfPOEInCurBState=_HpnicfPOEInCurBState_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,6,3),_HpnicfPOEInCurBState_Type())
hpnicfPOEInCurBState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOEInCurBState.setStatus(_A)
_HpnicfPOEInCurCState_Type=ACAlarmState
_HpnicfPOEInCurCState_Object=MibScalar
hpnicfPOEInCurCState=_HpnicfPOEInCurCState_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,6,4),_HpnicfPOEInCurCState_Type())
hpnicfPOEInCurCState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOEInCurCState.setStatus(_A)
_HpnicfPOESwitchStateVolExTable_Object=MibTable
hpnicfPOESwitchStateVolExTable=_HpnicfPOESwitchStateVolExTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,6,5))
if mibBuilder.loadTexts:hpnicfPOESwitchStateVolExTable.setStatus(_A)
_HpnicfPOESwitchStateVolExEntry_Object=MibTableRow
hpnicfPOESwitchStateVolExEntry=_HpnicfPOESwitchStateVolExEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,6,5,1))
hpnicfPOESwitchStateVolExEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:hpnicfPOESwitchStateVolExEntry.setStatus(_A)
class _HpnicfPOESwitchStateVolExIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfPOESwitchStateVolExIndex_Type.__name__=_D
_HpnicfPOESwitchStateVolExIndex_Object=MibTableColumn
hpnicfPOESwitchStateVolExIndex=_HpnicfPOESwitchStateVolExIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,6,5,1,1),_HpnicfPOESwitchStateVolExIndex_Type())
hpnicfPOESwitchStateVolExIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfPOESwitchStateVolExIndex.setStatus(_A)
_HpnicfPOESwitchStateInVolAB_Type=ACAlarmState
_HpnicfPOESwitchStateInVolAB_Object=MibTableColumn
hpnicfPOESwitchStateInVolAB=_HpnicfPOESwitchStateInVolAB_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,6,5,1,2),_HpnicfPOESwitchStateInVolAB_Type())
hpnicfPOESwitchStateInVolAB.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOESwitchStateInVolAB.setStatus(_A)
_HpnicfPOESwitchStateInVolBC_Type=ACAlarmState
_HpnicfPOESwitchStateInVolBC_Object=MibTableColumn
hpnicfPOESwitchStateInVolBC=_HpnicfPOESwitchStateInVolBC_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,6,5,1,3),_HpnicfPOESwitchStateInVolBC_Type())
hpnicfPOESwitchStateInVolBC.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOESwitchStateInVolBC.setStatus(_A)
_HpnicfPOESwitchStateInVolCA_Type=ACAlarmState
_HpnicfPOESwitchStateInVolCA_Object=MibTableColumn
hpnicfPOESwitchStateInVolCA=_HpnicfPOESwitchStateInVolCA_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,6,5,1,4),_HpnicfPOESwitchStateInVolCA_Type())
hpnicfPOESwitchStateInVolCA.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOESwitchStateInVolCA.setStatus(_A)
_HpnicfPOEAlarmStateObjects_ObjectIdentity=ObjectIdentity
hpnicfPOEAlarmStateObjects=_HpnicfPOEAlarmStateObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,14,8,7))
_HpnicfPOEAlarmStateModuleNum_Type=Integer32
_HpnicfPOEAlarmStateModuleNum_Object=MibScalar
hpnicfPOEAlarmStateModuleNum=_HpnicfPOEAlarmStateModuleNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,7,1),_HpnicfPOEAlarmStateModuleNum_Type())
hpnicfPOEAlarmStateModuleNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOEAlarmStateModuleNum.setStatus(_A)
_HpnicfPOEAlarmStateInfoTable_Object=MibTable
hpnicfPOEAlarmStateInfoTable=_HpnicfPOEAlarmStateInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,7,2))
if mibBuilder.loadTexts:hpnicfPOEAlarmStateInfoTable.setStatus(_A)
_HpnicfPOEAlarmStateInfoEntry_Object=MibTableRow
hpnicfPOEAlarmStateInfoEntry=_HpnicfPOEAlarmStateInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,7,2,1))
hpnicfPOEAlarmStateInfoEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:hpnicfPOEAlarmStateInfoEntry.setStatus(_A)
class _HpnicfPOEAlarmModuleInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfPOEAlarmModuleInfoIndex_Type.__name__=_D
_HpnicfPOEAlarmModuleInfoIndex_Object=MibTableColumn
hpnicfPOEAlarmModuleInfoIndex=_HpnicfPOEAlarmModuleInfoIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,7,2,1,1),_HpnicfPOEAlarmModuleInfoIndex_Type())
hpnicfPOEAlarmModuleInfoIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfPOEAlarmModuleInfoIndex.setStatus(_A)
_HpnicfPOEModuleDisconnect_Type=ModuleAlarmState
_HpnicfPOEModuleDisconnect_Object=MibTableColumn
hpnicfPOEModuleDisconnect=_HpnicfPOEModuleDisconnect_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,7,2,1,2),_HpnicfPOEModuleDisconnect_Type())
hpnicfPOEModuleDisconnect.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOEModuleDisconnect.setStatus(_A)
_HpnicfPOEModuleInputError_Type=ModuleAlarmState
_HpnicfPOEModuleInputError_Object=MibTableColumn
hpnicfPOEModuleInputError=_HpnicfPOEModuleInputError_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,7,2,1,3),_HpnicfPOEModuleInputError_Type())
hpnicfPOEModuleInputError.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOEModuleInputError.setStatus(_A)
_HpnicfPOEModuleOutputError_Type=ModuleAlarmState
_HpnicfPOEModuleOutputError_Object=MibTableColumn
hpnicfPOEModuleOutputError=_HpnicfPOEModuleOutputError_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,7,2,1,4),_HpnicfPOEModuleOutputError_Type())
hpnicfPOEModuleOutputError.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOEModuleOutputError.setStatus(_A)
_HpnicfPOEModuleOverVoltage_Type=ModuleAlarmState
_HpnicfPOEModuleOverVoltage_Object=MibTableColumn
hpnicfPOEModuleOverVoltage=_HpnicfPOEModuleOverVoltage_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,7,2,1,5),_HpnicfPOEModuleOverVoltage_Type())
hpnicfPOEModuleOverVoltage.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOEModuleOverVoltage.setStatus(_A)
_HpnicfPOEModuleOverTemp_Type=ModuleAlarmState
_HpnicfPOEModuleOverTemp_Object=MibTableColumn
hpnicfPOEModuleOverTemp=_HpnicfPOEModuleOverTemp_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,7,2,1,6),_HpnicfPOEModuleOverTemp_Type())
hpnicfPOEModuleOverTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOEModuleOverTemp.setStatus(_A)
_HpnicfPOEModuleFanError_Type=ModuleAlarmState
_HpnicfPOEModuleFanError_Object=MibTableColumn
hpnicfPOEModuleFanError=_HpnicfPOEModuleFanError_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,7,2,1,7),_HpnicfPOEModuleFanError_Type())
hpnicfPOEModuleFanError.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOEModuleFanError.setStatus(_A)
_HpnicfPOEModuleShutdown_Type=ModuleAlarmState
_HpnicfPOEModuleShutdown_Object=MibTableColumn
hpnicfPOEModuleShutdown=_HpnicfPOEModuleShutdown_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,7,2,1,8),_HpnicfPOEModuleShutdown_Type())
hpnicfPOEModuleShutdown.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOEModuleShutdown.setStatus(_A)
_HpnicfPOEModuleCurRestricted_Type=ModuleAlarmState
_HpnicfPOEModuleCurRestricted_Object=MibTableColumn
hpnicfPOEModuleCurRestricted=_HpnicfPOEModuleCurRestricted_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,8,7,2,1,9),_HpnicfPOEModuleCurRestricted_Type())
hpnicfPOEModuleCurRestricted.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPOEModuleCurRestricted.setStatus(_A)
class _HpnicfPsePolicyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_g,2)))
_HpnicfPsePolicyMode_Type.__name__=_D
_HpnicfPsePolicyMode_Object=MibScalar
hpnicfPsePolicyMode=_HpnicfPsePolicyMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,9),_HpnicfPsePolicyMode_Type())
hpnicfPsePolicyMode.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPsePolicyMode.setStatus(_A)
class _HpnicfPDPolicyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_M,1),(_g,2)))
_HpnicfPDPolicyMode_Type.__name__=_D
_HpnicfPDPolicyMode_Object=MibScalar
hpnicfPDPolicyMode=_HpnicfPDPolicyMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,14,10),_HpnicfPDPolicyMode_Type())
hpnicfPDPolicyMode.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPDPolicyMode.setStatus(_A)
hpnicfPsePortGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,14,4,2,1))
hpnicfPsePortGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:hpnicfPsePortGroup.setStatus(_A)
hpnicfMainPseGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,14,4,2,2))
hpnicfMainPseGroup.setObjects(*((_B,_o),(_B,_p),(_B,_q),(_B,_r)))
if mibBuilder.loadTexts:hpnicfMainPseGroup.setStatus(_A)
hpnicfPseScalarGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,14,4,2,3))
hpnicfPseScalarGroup.setObjects(*((_B,_s),(_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:hpnicfPseScalarGroup.setStatus(_A)
hpnicfPsePDNotificationGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,14,4,2,4))
hpnicfPsePDNotificationGroup.setObjects((_B,_w))
if mibBuilder.loadTexts:hpnicfPsePDNotificationGroup.setStatus(_A)
hpnicfPseProfilesGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,14,4,2,5))
hpnicfPseProfilesGroup.setObjects(*((_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3)))
if mibBuilder.loadTexts:hpnicfPseProfilesGroup.setStatus(_A)
hpnicfPOEPowerThresholdLimitGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,14,4,2,6))
hpnicfPOEPowerThresholdLimitGroup.setObjects(*((_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:hpnicfPOEPowerThresholdLimitGroup.setStatus(_A)
hpnicfPOEPowerSupInfoGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,14,4,2,7))
hpnicfPOEPowerSupInfoGroup.setObjects(*((_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:hpnicfPOEPowerSupInfoGroup.setStatus(_A)
hpnicfPOEPowerDCOutStateGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,14,4,2,8))
hpnicfPOEPowerDCOutStateGroup.setObjects((_B,_AE))
if mibBuilder.loadTexts:hpnicfPOEPowerDCOutStateGroup.setStatus(_A)
hpnicfPOEPowerDCOutInfoGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,14,4,2,9))
hpnicfPOEPowerDCOutInfoGroup.setObjects((_B,_AF))
if mibBuilder.loadTexts:hpnicfPOEPowerDCOutInfoGroup.setStatus(_A)
hpnicfPOEPowerACSwitchStateModuleGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,14,4,2,10))
hpnicfPOEPowerACSwitchStateModuleGroup.setObjects((_B,_AG))
if mibBuilder.loadTexts:hpnicfPOEPowerACSwitchStateModuleGroup.setStatus(_A)
hpnicfPOEPowerInCurStateGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,14,4,2,11))
hpnicfPOEPowerInCurStateGroup.setObjects(*((_B,_AH),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:hpnicfPOEPowerInCurStateGroup.setStatus(_A)
hpnicfPOEPowerAlarmStateGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,14,4,2,12))
hpnicfPOEPowerAlarmStateGroup.setObjects((_B,_AI))
if mibBuilder.loadTexts:hpnicfPOEPowerAlarmStateGroup.setStatus(_A)
hpnicfpsePDChangeNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,14,6,1))
hpnicfpsePDChangeNotification.setObjects((_J,_T))
if mibBuilder.loadTexts:hpnicfpsePDChangeNotification.setStatus(_A)
hpnicfPOEDisconnectNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,14,6,2))
hpnicfPOEDisconnectNotification.setObjects(*((_B,_G),(_B,_AJ)))
if mibBuilder.loadTexts:hpnicfPOEDisconnectNotification.setStatus(_A)
hpnicfPOEInputErrorNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,14,6,3))
hpnicfPOEInputErrorNotification.setObjects(*((_B,_G),(_B,_AK)))
if mibBuilder.loadTexts:hpnicfPOEInputErrorNotification.setStatus(_A)
hpnicfPOEOutputErrorNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,14,6,4))
hpnicfPOEOutputErrorNotification.setObjects(*((_B,_G),(_B,_AL)))
if mibBuilder.loadTexts:hpnicfPOEOutputErrorNotification.setStatus(_A)
hpnicfPOEOverVoltageNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,14,6,5))
hpnicfPOEOverVoltageNotification.setObjects(*((_B,_G),(_B,_AM)))
if mibBuilder.loadTexts:hpnicfPOEOverVoltageNotification.setStatus(_A)
hpnicfPOEOverTempNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,14,6,6))
hpnicfPOEOverTempNotification.setObjects(*((_B,_G),(_B,_AN)))
if mibBuilder.loadTexts:hpnicfPOEOverTempNotification.setStatus(_A)
hpnicfPOEFanErrorNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,14,6,7))
hpnicfPOEFanErrorNotification.setObjects(*((_B,_G),(_B,_AO)))
if mibBuilder.loadTexts:hpnicfPOEFanErrorNotification.setStatus(_A)
hpnicfPOEModuleShutdownNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,14,6,8))
hpnicfPOEModuleShutdownNotification.setObjects(*((_B,_G),(_B,_AP)))
if mibBuilder.loadTexts:hpnicfPOEModuleShutdownNotification.setStatus(_A)
hpnicfPOECurRestrictedNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,14,6,9))
hpnicfPOECurRestrictedNotification.setObjects(*((_B,_G),(_B,_AQ)))
if mibBuilder.loadTexts:hpnicfPOECurRestrictedNotification.setStatus(_A)
hpnicfPOEACSwitchNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,14,6,10))
hpnicfPOEACSwitchNotification.setObjects(*((_B,_O),(_B,_AR)))
if mibBuilder.loadTexts:hpnicfPOEACSwitchNotification.setStatus(_A)
hpnicfPOEACInCurANotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,14,6,11))
hpnicfPOEACInCurANotification.setObjects((_B,_P))
if mibBuilder.loadTexts:hpnicfPOEACInCurANotification.setStatus(_A)
hpnicfPOEACInCurBNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,14,6,12))
hpnicfPOEACInCurBNotification.setObjects((_B,_Q))
if mibBuilder.loadTexts:hpnicfPOEACInCurBNotification.setStatus(_A)
hpnicfPOEACInCurCNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,14,6,13))
hpnicfPOEACInCurCNotification.setObjects((_B,_R))
if mibBuilder.loadTexts:hpnicfPOEACInCurCNotification.setStatus(_A)
hpnicfPOEACSwitchVolABNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,14,6,14))
hpnicfPOEACSwitchVolABNotification.setObjects(*((_B,_K),(_B,_AS)))
if mibBuilder.loadTexts:hpnicfPOEACSwitchVolABNotification.setStatus(_A)
hpnicfPOEACSwitchVolBCNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,14,6,15))
hpnicfPOEACSwitchVolBCNotification.setObjects(*((_B,_K),(_B,_AT)))
if mibBuilder.loadTexts:hpnicfPOEACSwitchVolBCNotification.setStatus(_A)
hpnicfPOEACSwitchVolCANotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,14,6,16))
hpnicfPOEACSwitchVolCANotification.setObjects(*((_B,_K),(_B,_AU)))
if mibBuilder.loadTexts:hpnicfPOEACSwitchVolCANotification.setStatus(_A)
hpnicfPOEDCOutVolNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,14,6,17))
hpnicfPOEDCOutVolNotification.setObjects(*((_B,_N),(_B,_AV)))
if mibBuilder.loadTexts:hpnicfPOEDCOutVolNotification.setStatus(_A)
hpnicfPOEShutdownNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,14,6,18))
if mibBuilder.loadTexts:hpnicfPOEShutdownNotification.setStatus(_A)
hpnicfPseCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,2,14,4,1,1))
hpnicfPseCompliance.setObjects(*((_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa)))
if mibBuilder.loadTexts:hpnicfPseCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ACAlarmState':ACAlarmState,'DCAlarmState':DCAlarmState,'SwitchState':SwitchState,'ModuleAlarmState':ModuleAlarmState,'hpnicfPowerEthernetExt':hpnicfPowerEthernetExt,'hpnicfPsePortTable':hpnicfPsePortTable,'hpnicfPsePortEntry':hpnicfPsePortEntry,_m:hpnicfPsePortFaultDescription,_l:hpnicfPsePortPeakPower,_k:hpnicfPsePortAveragePower,_j:hpnicfPsePortCurrentPower,_i:hpnicfPsePortPowerLimit,_h:hpnicfPsePortProfileIndex,'hpnicfMainPseTable':hpnicfMainPseTable,'hpnicfMainPseEntry':hpnicfMainPseEntry,_o:hpnicfMainPsePowerLimit,_p:hpnicfMainPseAveragePower,_q:hpnicfMainPsePeakPower,_r:hpnicfMainGuaranteedPowerRemaining,_n:hpnicfMainPsePriorityMode,'hpnicfMainPseLegacy':hpnicfMainPseLegacy,'hpnicfMainPsePowerPriority':hpnicfMainPsePowerPriority,_s:hpnicfPseAutoDetectActive,'hpnicfPseComformance':hpnicfPseComformance,'hpnicfPseCompliances':hpnicfPseCompliances,'hpnicfPseCompliance':hpnicfPseCompliance,'hpnicfPseGroup':hpnicfPseGroup,_AW:hpnicfPsePortGroup,_AX:hpnicfMainPseGroup,_AY:hpnicfPseScalarGroup,_AZ:hpnicfPsePDNotificationGroup,_Aa:hpnicfPseProfilesGroup,'hpnicfPOEPowerThresholdLimitGroup':hpnicfPOEPowerThresholdLimitGroup,'hpnicfPOEPowerSupInfoGroup':hpnicfPOEPowerSupInfoGroup,'hpnicfPOEPowerDCOutStateGroup':hpnicfPOEPowerDCOutStateGroup,'hpnicfPOEPowerDCOutInfoGroup':hpnicfPOEPowerDCOutInfoGroup,'hpnicfPOEPowerACSwitchStateModuleGroup':hpnicfPOEPowerACSwitchStateModuleGroup,'hpnicfPOEPowerInCurStateGroup':hpnicfPOEPowerInCurStateGroup,'hpnicfPOEPowerAlarmStateGroup':hpnicfPOEPowerAlarmStateGroup,_t:hpnicfPsePowerMaxValue,'hpnicfpseportNotification':hpnicfpseportNotification,_w:hpnicfpsePDChangeNotification,'hpnicfPOEDisconnectNotification':hpnicfPOEDisconnectNotification,'hpnicfPOEInputErrorNotification':hpnicfPOEInputErrorNotification,'hpnicfPOEOutputErrorNotification':hpnicfPOEOutputErrorNotification,'hpnicfPOEOverVoltageNotification':hpnicfPOEOverVoltageNotification,'hpnicfPOEOverTempNotification':hpnicfPOEOverTempNotification,'hpnicfPOEFanErrorNotification':hpnicfPOEFanErrorNotification,'hpnicfPOEModuleShutdownNotification':hpnicfPOEModuleShutdownNotification,'hpnicfPOECurRestrictedNotification':hpnicfPOECurRestrictedNotification,'hpnicfPOEACSwitchNotification':hpnicfPOEACSwitchNotification,'hpnicfPOEACInCurANotification':hpnicfPOEACInCurANotification,'hpnicfPOEACInCurBNotification':hpnicfPOEACInCurBNotification,'hpnicfPOEACInCurCNotification':hpnicfPOEACInCurCNotification,'hpnicfPOEACSwitchVolABNotification':hpnicfPOEACSwitchVolABNotification,'hpnicfPOEACSwitchVolBCNotification':hpnicfPOEACSwitchVolBCNotification,'hpnicfPOEACSwitchVolCANotification':hpnicfPOEACSwitchVolCANotification,'hpnicfPOEDCOutVolNotification':hpnicfPOEDCOutVolNotification,'hpnicfPOEShutdownNotification':hpnicfPOEShutdownNotification,'hpnicfPseProfilesTable':hpnicfPseProfilesTable,'hpnicfPseProfilesEntry':hpnicfPseProfilesEntry,_d:hpnicfPseProfileIndex,_x:hpnicfPseProfileName,_y:hpnicfPseProfilePowerMode,_z:hpnicfPseProfilePowerLimit,_A0:hpnicfPseProfilePriority,_A1:hpnicfPseProfilePairs,_A2:hpnicfPseProfileApplyNum,_A3:hpnicfPseProfileRowStatus,'hpnicfPOEPowerObjects':hpnicfPOEPowerObjects,'hpnicfPOEThresholdLimitObjs':hpnicfPOEThresholdLimitObjs,_A4:hpnicfPOEThresholdACMimimum,_A5:hpnicfPOEThresholdACMaximum,_A6:hpnicfPOEThresholdDCMinimum,_A7:hpnicfPOEThresholdDCMaximum,'hpnicfPOESupModuleInfoObjs':hpnicfPOESupModuleInfoObjs,_A8:hpnicfPOEPowerType,_A9:hpnicfPOEPowerModuleNum,_AA:hpnicfPOESupervisionModuleName,_AB:hpnicfPOESMMajorVersion,_AC:hpnicfPOESMMinorVersion,_AD:hpnicfPOESMFactorName,'hpnicfPOEModuleInfoTable':hpnicfPOEModuleInfoTable,'hpnicfPOEModuleInfoEntry':hpnicfPOEModuleInfoEntry,_e:hpnicfPOEModuleIndex,'hpnicfPOEModuleID':hpnicfPOEModuleID,'hpnicfPOEModuleInfoPower':hpnicfPOEModuleInfoPower,'hpnicfPOEModuleHardVerInfo':hpnicfPOEModuleHardVerInfo,'hpnicfPOEDCOutStateObjects':hpnicfPOEDCOutStateObjects,_AE:hpnicfPOEDCOutStateModuleNum,'hpnicfPOEDCOutStateTable':hpnicfPOEDCOutStateTable,'hpnicfPOEDCOutStateEntry':hpnicfPOEDCOutStateEntry,_N:hpnicfPOEDCOutStateIndex,_AV:hpnicfPOEDCOutDCVolAlarm,'hpnicfPOEDCOutInfoObjects':hpnicfPOEDCOutInfoObjects,_AF:hpnicfPOEDCOutCurNum,'hpnicfPOEDCOutInfoTable':hpnicfPOEDCOutInfoTable,'hpnicfPOEDCOutInfoEntry':hpnicfPOEDCOutInfoEntry,_f:hpnicfPOEDCOutInfoIndex,'hpnicfPOEDCOutVol':hpnicfPOEDCOutVol,'hpnicfPOEDCOutInfoLoadCur':hpnicfPOEDCOutInfoLoadCur,'hpnicfPOEACSwitchStateModuleObjs':hpnicfPOEACSwitchStateModuleObjs,_AG:hpnicfPOEACSwitchStateModuleNum,'hpnicfPOEACSwitchStateTable':hpnicfPOEACSwitchStateTable,'hpnicfPOEACSwitchStateEntry':hpnicfPOEACSwitchStateEntry,_O:hpnicfPOEACSwitchStateIndex,_AR:hpnicfPOEACSwitchState,'hpnicfPOEInCurStateObjects':hpnicfPOEInCurStateObjects,_AH:hpnicfPOEInCurStateModuleNum,_P:hpnicfPOEInCurAState,_Q:hpnicfPOEInCurBState,_R:hpnicfPOEInCurCState,'hpnicfPOESwitchStateVolExTable':hpnicfPOESwitchStateVolExTable,'hpnicfPOESwitchStateVolExEntry':hpnicfPOESwitchStateVolExEntry,_K:hpnicfPOESwitchStateVolExIndex,_AS:hpnicfPOESwitchStateInVolAB,_AT:hpnicfPOESwitchStateInVolBC,_AU:hpnicfPOESwitchStateInVolCA,'hpnicfPOEAlarmStateObjects':hpnicfPOEAlarmStateObjects,_AI:hpnicfPOEAlarmStateModuleNum,'hpnicfPOEAlarmStateInfoTable':hpnicfPOEAlarmStateInfoTable,'hpnicfPOEAlarmStateInfoEntry':hpnicfPOEAlarmStateInfoEntry,_G:hpnicfPOEAlarmModuleInfoIndex,_AJ:hpnicfPOEModuleDisconnect,_AK:hpnicfPOEModuleInputError,_AL:hpnicfPOEModuleOutputError,_AM:hpnicfPOEModuleOverVoltage,_AN:hpnicfPOEModuleOverTemp,_AO:hpnicfPOEModuleFanError,_AP:hpnicfPOEModuleShutdown,_AQ:hpnicfPOEModuleCurRestricted,_u:hpnicfPsePolicyMode,_v:hpnicfPDPolicyMode})