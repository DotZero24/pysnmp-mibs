_AR='cvaIfEMGroupRev2'
_AQ='cvaIfEMGroupRev1'
_AP='cvaIfFXOGroup'
_AO='cvaIfEMGroup'
_AN='cvaIfEMTimingDelayVoice'
_AM='cvaIfEMTimeoutPttRcv'
_AL='cvaIfEMTimeoutPttXmt'
_AK='cvaIfEMCfgAutoGainControl'
_AJ='cvaIfFXOCfgSupDisconnect2'
_AI='cvaIfFXSTimingInterDigitDuration'
_AH='cvaIfFXSTimingDigitDuration'
_AG='cvaIfFXSRingFrequency'
_AF='cvaIfFXSCfgSignalType'
_AE='cvaIfFXSTipGround'
_AD='cvaIfFXSRingGround'
_AC='cvaIfFXSRingActive'
_AB='cvaIfFXSHookStatus'
_AA='cvaIfFXOCfgSupDisconnect'
_A9='cvaIfStatusSignalErrors'
_A8='cvaIfMaintenanceMode'
_A7='cvaIfStatusInfoType'
_A6='cvaIfCfgImpedance'
_A5='cvaIfCfgIntegratedDSP'
_A4='cvaIfFXSTimingEntry'
_A3='cvaIfFXSStatusEntry'
_A2='cvaIfFXOTimingEntry'
_A1='cvaIfFXOStatusEntry'
_A0='cvaIfEMTimingEntry'
_z='cvaIfEMStatusEntry'
_y='cvaIfStatusEntry'
_x='trunked'
_w='offHook'
_v='onHook'
_u='minutes'
_t='pulses per second'
_s='cvaIfFXOGroup2'
_r='cvaIfEMTimeoutLmrTeardown'
_q='cvaIfEMTimingVoiceHangover'
_p='cvaIfEMCfgLmrECap'
_o='cvaIfEMCfgLmrMCap'
_n='cvaIfFXOTimingPulseInterDigitDuration'
_m='cvaIfFXOTimingPulseRate'
_l='cvaIfFXOTimingInterDigitDuration'
_k='cvaIfFXOTimingDigitDuration'
_j='cvaIfFXOCfgDialType'
_i='cvaIfFXOCfgNumberRings'
_h='cvaIfFXOCfgSignalType'
_g='cvaIfFXOTipGround'
_f='cvaIfFXORingGround'
_e='cvaIfFXORingDetect'
_d='cvaIfFXOHookStatus'
_c='InterfaceDialType'
_b='TruthValue'
_a='cvaIfFXSGroup'
_Z='cvaIfGeneralGroup'
_Y='cvaIfEMTimingMinDelayPulseWidth'
_X='cvaIfEMTimingMaxDelayDuration'
_W='cvaIfEMTimingDelayStart'
_V='cvaIfEMTimingMaxWinkDuration'
_U='cvaIfEMTimingMaxWinkWaitDuration'
_T='cvaIfEMTimingClearWaitDuration'
_S='cvaIfEMTimingPulseInterDigitDuration'
_R='cvaIfEMTimingPulseRate'
_Q='cvaIfEMTimingInterDigitDuration'
_P='cvaIfEMTimingDigitDuration'
_O='cvaIfEMCfgDialType'
_N='cvaIfEMCfgType'
_M='cvaIfEMCfgOperation'
_L='cvaIfEMCfgSignalType'
_K='cvaIfEMOutSeizureActive'
_J='cvaIfEMInSeizureActive'
_I='ifIndex'
_H='IF-MIB'
_G='deprecated'
_F='read-only'
_E='milliseconds'
_D='read-write'
_C='Integer32'
_B='current'
_A='CISCO-VOICE-ANALOG-IF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_b)
ciscoVoiceAnalogIfMIB=ModuleIdentity((1,3,6,1,4,1,9,9,62))
if mibBuilder.loadTexts:ciscoVoiceAnalogIfMIB.setRevisions(('2005-10-03 00:00','2004-10-14 00:00','2004-01-15 00:00','2002-08-03 00:00','2002-07-29 00:00','2002-01-21 00:00'))
class InterfaceDialType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('dtmf',1),('pulse',2),('mf',3)))
_CvaIfObjects_ObjectIdentity=ObjectIdentity
cvaIfObjects=_CvaIfObjects_ObjectIdentity((1,3,6,1,4,1,9,9,62,1))
_CvaIfGeneralObjects_ObjectIdentity=ObjectIdentity
cvaIfGeneralObjects=_CvaIfGeneralObjects_ObjectIdentity((1,3,6,1,4,1,9,9,62,1,1))
_CvaIfCfgTable_Object=MibTable
cvaIfCfgTable=_CvaIfCfgTable_Object((1,3,6,1,4,1,9,9,62,1,1,1))
if mibBuilder.loadTexts:cvaIfCfgTable.setStatus(_B)
_CvaIfCfgEntry_Object=MibTableRow
cvaIfCfgEntry=_CvaIfCfgEntry_Object((1,3,6,1,4,1,9,9,62,1,1,1,1))
cvaIfCfgEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cvaIfCfgEntry.setStatus(_B)
class _CvaIfCfgImpedance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('other',1),('ohms600Real',2),('ohms600Complex',3),('ohms900Complex',4),('ohmsComplex1',5),('ohmsComplex2',6)))
_CvaIfCfgImpedance_Type.__name__=_C
_CvaIfCfgImpedance_Object=MibTableColumn
cvaIfCfgImpedance=_CvaIfCfgImpedance_Object((1,3,6,1,4,1,9,9,62,1,1,1,1,1),_CvaIfCfgImpedance_Type())
cvaIfCfgImpedance.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfCfgImpedance.setStatus(_B)
_CvaIfCfgIntegratedDSP_Type=TruthValue
_CvaIfCfgIntegratedDSP_Object=MibTableColumn
cvaIfCfgIntegratedDSP=_CvaIfCfgIntegratedDSP_Object((1,3,6,1,4,1,9,9,62,1,1,1,1,2),_CvaIfCfgIntegratedDSP_Type())
cvaIfCfgIntegratedDSP.setMaxAccess(_F)
if mibBuilder.loadTexts:cvaIfCfgIntegratedDSP.setStatus(_B)
_CvaIfStatusTable_Object=MibTable
cvaIfStatusTable=_CvaIfStatusTable_Object((1,3,6,1,4,1,9,9,62,1,1,2))
if mibBuilder.loadTexts:cvaIfStatusTable.setStatus(_B)
_CvaIfStatusEntry_Object=MibTableRow
cvaIfStatusEntry=_CvaIfStatusEntry_Object((1,3,6,1,4,1,9,9,62,1,1,2,1))
if mibBuilder.loadTexts:cvaIfStatusEntry.setStatus(_B)
class _CvaIfStatusInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('voice',2),('g3Fax',3)))
_CvaIfStatusInfoType_Type.__name__=_C
_CvaIfStatusInfoType_Object=MibTableColumn
cvaIfStatusInfoType=_CvaIfStatusInfoType_Object((1,3,6,1,4,1,9,9,62,1,1,2,1,1),_CvaIfStatusInfoType_Type())
cvaIfStatusInfoType.setMaxAccess(_F)
if mibBuilder.loadTexts:cvaIfStatusInfoType.setStatus(_B)
class _CvaIfMaintenanceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('hostCompressedLoopback',2),('hostUncompressedLoopback',3),('ifCompressedLoopback',4),('ifUncompressedLoopback',5)))
_CvaIfMaintenanceMode_Type.__name__=_C
_CvaIfMaintenanceMode_Object=MibTableColumn
cvaIfMaintenanceMode=_CvaIfMaintenanceMode_Object((1,3,6,1,4,1,9,9,62,1,1,2,1,2),_CvaIfMaintenanceMode_Type())
cvaIfMaintenanceMode.setMaxAccess(_F)
if mibBuilder.loadTexts:cvaIfMaintenanceMode.setStatus(_B)
_CvaIfStatusSignalErrors_Type=Counter32
_CvaIfStatusSignalErrors_Object=MibTableColumn
cvaIfStatusSignalErrors=_CvaIfStatusSignalErrors_Object((1,3,6,1,4,1,9,9,62,1,1,2,1,3),_CvaIfStatusSignalErrors_Type())
cvaIfStatusSignalErrors.setMaxAccess(_F)
if mibBuilder.loadTexts:cvaIfStatusSignalErrors.setStatus(_B)
_CvaIfEMObjects_ObjectIdentity=ObjectIdentity
cvaIfEMObjects=_CvaIfEMObjects_ObjectIdentity((1,3,6,1,4,1,9,9,62,1,2))
_CvaIfEMCfgTable_Object=MibTable
cvaIfEMCfgTable=_CvaIfEMCfgTable_Object((1,3,6,1,4,1,9,9,62,1,2,1))
if mibBuilder.loadTexts:cvaIfEMCfgTable.setStatus(_B)
_CvaIfEMCfgEntry_Object=MibTableRow
cvaIfEMCfgEntry=_CvaIfEMCfgEntry_Object((1,3,6,1,4,1,9,9,62,1,2,1,1))
cvaIfEMCfgEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cvaIfEMCfgEntry.setStatus(_B)
class _CvaIfEMCfgSignalType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('winkStart',1),('immediateDial',2),('delayDial',3),('lmr',4),('fgd',5),('fgd-eana',6)))
_CvaIfEMCfgSignalType_Type.__name__=_C
_CvaIfEMCfgSignalType_Object=MibTableColumn
cvaIfEMCfgSignalType=_CvaIfEMCfgSignalType_Object((1,3,6,1,4,1,9,9,62,1,2,1,1,1),_CvaIfEMCfgSignalType_Type())
cvaIfEMCfgSignalType.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfEMCfgSignalType.setStatus(_B)
class _CvaIfEMCfgOperation_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('twoWires',1),('fourWires',2)))
_CvaIfEMCfgOperation_Type.__name__=_C
_CvaIfEMCfgOperation_Object=MibTableColumn
cvaIfEMCfgOperation=_CvaIfEMCfgOperation_Object((1,3,6,1,4,1,9,9,62,1,2,1,1,2),_CvaIfEMCfgOperation_Type())
cvaIfEMCfgOperation.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfEMCfgOperation.setStatus(_B)
class _CvaIfEMCfgType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('typeI',1),('typeII',2),('typeIII',3),('typeIV',4),('typeV',5)))
_CvaIfEMCfgType_Type.__name__=_C
_CvaIfEMCfgType_Object=MibTableColumn
cvaIfEMCfgType=_CvaIfEMCfgType_Object((1,3,6,1,4,1,9,9,62,1,2,1,1,3),_CvaIfEMCfgType_Type())
cvaIfEMCfgType.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfEMCfgType.setStatus(_B)
class _CvaIfEMCfgDialType_Type(InterfaceDialType):defaultValue=1
_CvaIfEMCfgDialType_Type.__name__=_c
_CvaIfEMCfgDialType_Object=MibTableColumn
cvaIfEMCfgDialType=_CvaIfEMCfgDialType_Object((1,3,6,1,4,1,9,9,62,1,2,1,1,4),_CvaIfEMCfgDialType_Type())
cvaIfEMCfgDialType.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfEMCfgDialType.setStatus(_B)
class _CvaIfEMCfgLmrMCap_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inact',1),('audio',2),('dial',3)))
_CvaIfEMCfgLmrMCap_Type.__name__=_C
_CvaIfEMCfgLmrMCap_Object=MibTableColumn
cvaIfEMCfgLmrMCap=_CvaIfEMCfgLmrMCap_Object((1,3,6,1,4,1,9,9,62,1,2,1,1,5),_CvaIfEMCfgLmrMCap_Type())
cvaIfEMCfgLmrMCap.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfEMCfgLmrMCap.setStatus(_B)
class _CvaIfEMCfgLmrECap_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4,5,6)));namedValues=NamedValues(*(('seize',4),('voice',5),('inactive',6)))
_CvaIfEMCfgLmrECap_Type.__name__=_C
_CvaIfEMCfgLmrECap_Object=MibTableColumn
cvaIfEMCfgLmrECap=_CvaIfEMCfgLmrECap_Object((1,3,6,1,4,1,9,9,62,1,2,1,1,6),_CvaIfEMCfgLmrECap_Type())
cvaIfEMCfgLmrECap.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfEMCfgLmrECap.setStatus(_B)
class _CvaIfEMCfgAutoGainControl_Type(TruthValue):defaultValue=2
_CvaIfEMCfgAutoGainControl_Type.__name__=_b
_CvaIfEMCfgAutoGainControl_Object=MibTableColumn
cvaIfEMCfgAutoGainControl=_CvaIfEMCfgAutoGainControl_Object((1,3,6,1,4,1,9,9,62,1,2,1,1,7),_CvaIfEMCfgAutoGainControl_Type())
cvaIfEMCfgAutoGainControl.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfEMCfgAutoGainControl.setStatus(_B)
_CvaIfEMStatusTable_Object=MibTable
cvaIfEMStatusTable=_CvaIfEMStatusTable_Object((1,3,6,1,4,1,9,9,62,1,2,2))
if mibBuilder.loadTexts:cvaIfEMStatusTable.setStatus(_B)
_CvaIfEMStatusEntry_Object=MibTableRow
cvaIfEMStatusEntry=_CvaIfEMStatusEntry_Object((1,3,6,1,4,1,9,9,62,1,2,2,1))
if mibBuilder.loadTexts:cvaIfEMStatusEntry.setStatus(_B)
_CvaIfEMInSeizureActive_Type=TruthValue
_CvaIfEMInSeizureActive_Object=MibTableColumn
cvaIfEMInSeizureActive=_CvaIfEMInSeizureActive_Object((1,3,6,1,4,1,9,9,62,1,2,2,1,1),_CvaIfEMInSeizureActive_Type())
cvaIfEMInSeizureActive.setMaxAccess(_F)
if mibBuilder.loadTexts:cvaIfEMInSeizureActive.setStatus(_B)
_CvaIfEMOutSeizureActive_Type=TruthValue
_CvaIfEMOutSeizureActive_Object=MibTableColumn
cvaIfEMOutSeizureActive=_CvaIfEMOutSeizureActive_Object((1,3,6,1,4,1,9,9,62,1,2,2,1,2),_CvaIfEMOutSeizureActive_Type())
cvaIfEMOutSeizureActive.setMaxAccess(_F)
if mibBuilder.loadTexts:cvaIfEMOutSeizureActive.setStatus(_B)
_CvaIfEMTimingTable_Object=MibTable
cvaIfEMTimingTable=_CvaIfEMTimingTable_Object((1,3,6,1,4,1,9,9,62,1,2,3))
if mibBuilder.loadTexts:cvaIfEMTimingTable.setStatus(_B)
_CvaIfEMTimingEntry_Object=MibTableRow
cvaIfEMTimingEntry=_CvaIfEMTimingEntry_Object((1,3,6,1,4,1,9,9,62,1,2,3,1))
if mibBuilder.loadTexts:cvaIfEMTimingEntry.setStatus(_B)
class _CvaIfEMTimingDigitDuration_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_CvaIfEMTimingDigitDuration_Type.__name__=_C
_CvaIfEMTimingDigitDuration_Object=MibTableColumn
cvaIfEMTimingDigitDuration=_CvaIfEMTimingDigitDuration_Object((1,3,6,1,4,1,9,9,62,1,2,3,1,1),_CvaIfEMTimingDigitDuration_Type())
cvaIfEMTimingDigitDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfEMTimingDigitDuration.setStatus(_B)
if mibBuilder.loadTexts:cvaIfEMTimingDigitDuration.setUnits(_E)
class _CvaIfEMTimingInterDigitDuration_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_CvaIfEMTimingInterDigitDuration_Type.__name__=_C
_CvaIfEMTimingInterDigitDuration_Object=MibTableColumn
cvaIfEMTimingInterDigitDuration=_CvaIfEMTimingInterDigitDuration_Object((1,3,6,1,4,1,9,9,62,1,2,3,1,2),_CvaIfEMTimingInterDigitDuration_Type())
cvaIfEMTimingInterDigitDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfEMTimingInterDigitDuration.setStatus(_B)
if mibBuilder.loadTexts:cvaIfEMTimingInterDigitDuration.setUnits(_E)
class _CvaIfEMTimingPulseRate_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,20))
_CvaIfEMTimingPulseRate_Type.__name__=_C
_CvaIfEMTimingPulseRate_Object=MibTableColumn
cvaIfEMTimingPulseRate=_CvaIfEMTimingPulseRate_Object((1,3,6,1,4,1,9,9,62,1,2,3,1,3),_CvaIfEMTimingPulseRate_Type())
cvaIfEMTimingPulseRate.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfEMTimingPulseRate.setStatus(_B)
if mibBuilder.loadTexts:cvaIfEMTimingPulseRate.setUnits(_t)
class _CvaIfEMTimingPulseInterDigitDuration_Type(Integer32):defaultValue=750;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_CvaIfEMTimingPulseInterDigitDuration_Type.__name__=_C
_CvaIfEMTimingPulseInterDigitDuration_Object=MibTableColumn
cvaIfEMTimingPulseInterDigitDuration=_CvaIfEMTimingPulseInterDigitDuration_Object((1,3,6,1,4,1,9,9,62,1,2,3,1,4),_CvaIfEMTimingPulseInterDigitDuration_Type())
cvaIfEMTimingPulseInterDigitDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfEMTimingPulseInterDigitDuration.setStatus(_B)
if mibBuilder.loadTexts:cvaIfEMTimingPulseInterDigitDuration.setUnits(_E)
class _CvaIfEMTimingClearWaitDuration_Type(Integer32):defaultValue=400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,2000))
_CvaIfEMTimingClearWaitDuration_Type.__name__=_C
_CvaIfEMTimingClearWaitDuration_Object=MibTableColumn
cvaIfEMTimingClearWaitDuration=_CvaIfEMTimingClearWaitDuration_Object((1,3,6,1,4,1,9,9,62,1,2,3,1,5),_CvaIfEMTimingClearWaitDuration_Type())
cvaIfEMTimingClearWaitDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfEMTimingClearWaitDuration.setStatus(_B)
if mibBuilder.loadTexts:cvaIfEMTimingClearWaitDuration.setUnits(_E)
class _CvaIfEMTimingMaxWinkWaitDuration_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,5000))
_CvaIfEMTimingMaxWinkWaitDuration_Type.__name__=_C
_CvaIfEMTimingMaxWinkWaitDuration_Object=MibTableColumn
cvaIfEMTimingMaxWinkWaitDuration=_CvaIfEMTimingMaxWinkWaitDuration_Object((1,3,6,1,4,1,9,9,62,1,2,3,1,6),_CvaIfEMTimingMaxWinkWaitDuration_Type())
cvaIfEMTimingMaxWinkWaitDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfEMTimingMaxWinkWaitDuration.setStatus(_B)
if mibBuilder.loadTexts:cvaIfEMTimingMaxWinkWaitDuration.setUnits(_E)
class _CvaIfEMTimingMaxWinkDuration_Type(Integer32):defaultValue=200;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,3000))
_CvaIfEMTimingMaxWinkDuration_Type.__name__=_C
_CvaIfEMTimingMaxWinkDuration_Object=MibTableColumn
cvaIfEMTimingMaxWinkDuration=_CvaIfEMTimingMaxWinkDuration_Object((1,3,6,1,4,1,9,9,62,1,2,3,1,7),_CvaIfEMTimingMaxWinkDuration_Type())
cvaIfEMTimingMaxWinkDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfEMTimingMaxWinkDuration.setStatus(_B)
if mibBuilder.loadTexts:cvaIfEMTimingMaxWinkDuration.setUnits(_E)
class _CvaIfEMTimingDelayStart_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(20,2000))
_CvaIfEMTimingDelayStart_Type.__name__=_C
_CvaIfEMTimingDelayStart_Object=MibTableColumn
cvaIfEMTimingDelayStart=_CvaIfEMTimingDelayStart_Object((1,3,6,1,4,1,9,9,62,1,2,3,1,8),_CvaIfEMTimingDelayStart_Type())
cvaIfEMTimingDelayStart.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfEMTimingDelayStart.setStatus(_B)
if mibBuilder.loadTexts:cvaIfEMTimingDelayStart.setUnits(_E)
class _CvaIfEMTimingMaxDelayDuration_Type(Integer32):defaultValue=2000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,5000))
_CvaIfEMTimingMaxDelayDuration_Type.__name__=_C
_CvaIfEMTimingMaxDelayDuration_Object=MibTableColumn
cvaIfEMTimingMaxDelayDuration=_CvaIfEMTimingMaxDelayDuration_Object((1,3,6,1,4,1,9,9,62,1,2,3,1,9),_CvaIfEMTimingMaxDelayDuration_Type())
cvaIfEMTimingMaxDelayDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfEMTimingMaxDelayDuration.setStatus(_B)
if mibBuilder.loadTexts:cvaIfEMTimingMaxDelayDuration.setUnits(_E)
class _CvaIfEMTimingMinDelayPulseWidth_Type(Integer32):defaultValue=140;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(140,5000))
_CvaIfEMTimingMinDelayPulseWidth_Type.__name__=_C
_CvaIfEMTimingMinDelayPulseWidth_Object=MibTableColumn
cvaIfEMTimingMinDelayPulseWidth=_CvaIfEMTimingMinDelayPulseWidth_Object((1,3,6,1,4,1,9,9,62,1,2,3,1,10),_CvaIfEMTimingMinDelayPulseWidth_Type())
cvaIfEMTimingMinDelayPulseWidth.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfEMTimingMinDelayPulseWidth.setStatus(_B)
if mibBuilder.loadTexts:cvaIfEMTimingMinDelayPulseWidth.setUnits(_E)
class _CvaIfEMTimingVoiceHangover_Type(Integer32):defaultValue=250;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000))
_CvaIfEMTimingVoiceHangover_Type.__name__=_C
_CvaIfEMTimingVoiceHangover_Object=MibTableColumn
cvaIfEMTimingVoiceHangover=_CvaIfEMTimingVoiceHangover_Object((1,3,6,1,4,1,9,9,62,1,2,3,1,11),_CvaIfEMTimingVoiceHangover_Type())
cvaIfEMTimingVoiceHangover.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfEMTimingVoiceHangover.setStatus(_B)
if mibBuilder.loadTexts:cvaIfEMTimingVoiceHangover.setUnits(_E)
class _CvaIfEMTimeoutLmrTeardown_Type(Integer32):defaultValue=1800;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(5,60000))
_CvaIfEMTimeoutLmrTeardown_Type.__name__=_C
_CvaIfEMTimeoutLmrTeardown_Object=MibTableColumn
cvaIfEMTimeoutLmrTeardown=_CvaIfEMTimeoutLmrTeardown_Object((1,3,6,1,4,1,9,9,62,1,2,3,1,12),_CvaIfEMTimeoutLmrTeardown_Type())
cvaIfEMTimeoutLmrTeardown.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfEMTimeoutLmrTeardown.setStatus(_B)
if mibBuilder.loadTexts:cvaIfEMTimeoutLmrTeardown.setUnits('seconds')
class _CvaIfEMTimeoutPttXmt_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_CvaIfEMTimeoutPttXmt_Type.__name__=_C
_CvaIfEMTimeoutPttXmt_Object=MibTableColumn
cvaIfEMTimeoutPttXmt=_CvaIfEMTimeoutPttXmt_Object((1,3,6,1,4,1,9,9,62,1,2,3,1,13),_CvaIfEMTimeoutPttXmt_Type())
cvaIfEMTimeoutPttXmt.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfEMTimeoutPttXmt.setStatus(_B)
if mibBuilder.loadTexts:cvaIfEMTimeoutPttXmt.setUnits(_u)
class _CvaIfEMTimeoutPttRcv_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30))
_CvaIfEMTimeoutPttRcv_Type.__name__=_C
_CvaIfEMTimeoutPttRcv_Object=MibTableColumn
cvaIfEMTimeoutPttRcv=_CvaIfEMTimeoutPttRcv_Object((1,3,6,1,4,1,9,9,62,1,2,3,1,14),_CvaIfEMTimeoutPttRcv_Type())
cvaIfEMTimeoutPttRcv.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfEMTimeoutPttRcv.setStatus(_B)
if mibBuilder.loadTexts:cvaIfEMTimeoutPttRcv.setUnits(_u)
class _CvaIfEMTimingDelayVoice_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1500))
_CvaIfEMTimingDelayVoice_Type.__name__=_C
_CvaIfEMTimingDelayVoice_Object=MibTableColumn
cvaIfEMTimingDelayVoice=_CvaIfEMTimingDelayVoice_Object((1,3,6,1,4,1,9,9,62,1,2,3,1,15),_CvaIfEMTimingDelayVoice_Type())
cvaIfEMTimingDelayVoice.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfEMTimingDelayVoice.setStatus(_B)
if mibBuilder.loadTexts:cvaIfEMTimingDelayVoice.setUnits(_E)
_CvaIfFXOObjects_ObjectIdentity=ObjectIdentity
cvaIfFXOObjects=_CvaIfFXOObjects_ObjectIdentity((1,3,6,1,4,1,9,9,62,1,3))
_CvaIfFXOCfgTable_Object=MibTable
cvaIfFXOCfgTable=_CvaIfFXOCfgTable_Object((1,3,6,1,4,1,9,9,62,1,3,1))
if mibBuilder.loadTexts:cvaIfFXOCfgTable.setStatus(_B)
_CvaIfFXOCfgEntry_Object=MibTableRow
cvaIfFXOCfgEntry=_CvaIfFXOCfgEntry_Object((1,3,6,1,4,1,9,9,62,1,3,1,1))
cvaIfFXOCfgEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cvaIfFXOCfgEntry.setStatus(_B)
class _CvaIfFXOCfgSignalType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fxoLoopStart',1),('fxoGroundStart',2),('fxoCama',3)))
_CvaIfFXOCfgSignalType_Type.__name__=_C
_CvaIfFXOCfgSignalType_Object=MibTableColumn
cvaIfFXOCfgSignalType=_CvaIfFXOCfgSignalType_Object((1,3,6,1,4,1,9,9,62,1,3,1,1,1),_CvaIfFXOCfgSignalType_Type())
cvaIfFXOCfgSignalType.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfFXOCfgSignalType.setStatus(_B)
class _CvaIfFXOCfgNumberRings_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CvaIfFXOCfgNumberRings_Type.__name__=_C
_CvaIfFXOCfgNumberRings_Object=MibTableColumn
cvaIfFXOCfgNumberRings=_CvaIfFXOCfgNumberRings_Object((1,3,6,1,4,1,9,9,62,1,3,1,1,2),_CvaIfFXOCfgNumberRings_Type())
cvaIfFXOCfgNumberRings.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfFXOCfgNumberRings.setStatus(_B)
if mibBuilder.loadTexts:cvaIfFXOCfgNumberRings.setUnits('rings')
class _CvaIfFXOCfgSupDisconnect_Type(TruthValue):defaultValue=1
_CvaIfFXOCfgSupDisconnect_Type.__name__=_b
_CvaIfFXOCfgSupDisconnect_Object=MibTableColumn
cvaIfFXOCfgSupDisconnect=_CvaIfFXOCfgSupDisconnect_Object((1,3,6,1,4,1,9,9,62,1,3,1,1,3),_CvaIfFXOCfgSupDisconnect_Type())
cvaIfFXOCfgSupDisconnect.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfFXOCfgSupDisconnect.setStatus(_G)
class _CvaIfFXOCfgDialType_Type(InterfaceDialType):defaultValue=1
_CvaIfFXOCfgDialType_Type.__name__=_c
_CvaIfFXOCfgDialType_Object=MibTableColumn
cvaIfFXOCfgDialType=_CvaIfFXOCfgDialType_Object((1,3,6,1,4,1,9,9,62,1,3,1,1,4),_CvaIfFXOCfgDialType_Type())
cvaIfFXOCfgDialType.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfFXOCfgDialType.setStatus(_B)
class _CvaIfFXOCfgSupDisconnect2_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('signal',0),('anytone',1),('dualtoneMidcall',2),('dualtonePreconnect',3)))
_CvaIfFXOCfgSupDisconnect2_Type.__name__=_C
_CvaIfFXOCfgSupDisconnect2_Object=MibTableColumn
cvaIfFXOCfgSupDisconnect2=_CvaIfFXOCfgSupDisconnect2_Object((1,3,6,1,4,1,9,9,62,1,3,1,1,5),_CvaIfFXOCfgSupDisconnect2_Type())
cvaIfFXOCfgSupDisconnect2.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfFXOCfgSupDisconnect2.setStatus(_B)
_CvaIfFXOStatusTable_Object=MibTable
cvaIfFXOStatusTable=_CvaIfFXOStatusTable_Object((1,3,6,1,4,1,9,9,62,1,3,2))
if mibBuilder.loadTexts:cvaIfFXOStatusTable.setStatus(_B)
_CvaIfFXOStatusEntry_Object=MibTableRow
cvaIfFXOStatusEntry=_CvaIfFXOStatusEntry_Object((1,3,6,1,4,1,9,9,62,1,3,2,1))
if mibBuilder.loadTexts:cvaIfFXOStatusEntry.setStatus(_B)
class _CvaIfFXOHookStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_v,1),(_w,2),(_x,3)))
_CvaIfFXOHookStatus_Type.__name__=_C
_CvaIfFXOHookStatus_Object=MibTableColumn
cvaIfFXOHookStatus=_CvaIfFXOHookStatus_Object((1,3,6,1,4,1,9,9,62,1,3,2,1,1),_CvaIfFXOHookStatus_Type())
cvaIfFXOHookStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cvaIfFXOHookStatus.setStatus(_B)
_CvaIfFXORingDetect_Type=TruthValue
_CvaIfFXORingDetect_Object=MibTableColumn
cvaIfFXORingDetect=_CvaIfFXORingDetect_Object((1,3,6,1,4,1,9,9,62,1,3,2,1,2),_CvaIfFXORingDetect_Type())
cvaIfFXORingDetect.setMaxAccess(_F)
if mibBuilder.loadTexts:cvaIfFXORingDetect.setStatus(_B)
_CvaIfFXORingGround_Type=TruthValue
_CvaIfFXORingGround_Object=MibTableColumn
cvaIfFXORingGround=_CvaIfFXORingGround_Object((1,3,6,1,4,1,9,9,62,1,3,2,1,3),_CvaIfFXORingGround_Type())
cvaIfFXORingGround.setMaxAccess(_F)
if mibBuilder.loadTexts:cvaIfFXORingGround.setStatus(_B)
_CvaIfFXOTipGround_Type=TruthValue
_CvaIfFXOTipGround_Object=MibTableColumn
cvaIfFXOTipGround=_CvaIfFXOTipGround_Object((1,3,6,1,4,1,9,9,62,1,3,2,1,4),_CvaIfFXOTipGround_Type())
cvaIfFXOTipGround.setMaxAccess(_F)
if mibBuilder.loadTexts:cvaIfFXOTipGround.setStatus(_B)
_CvaIfFXOTimingTable_Object=MibTable
cvaIfFXOTimingTable=_CvaIfFXOTimingTable_Object((1,3,6,1,4,1,9,9,62,1,3,3))
if mibBuilder.loadTexts:cvaIfFXOTimingTable.setStatus(_B)
_CvaIfFXOTimingEntry_Object=MibTableRow
cvaIfFXOTimingEntry=_CvaIfFXOTimingEntry_Object((1,3,6,1,4,1,9,9,62,1,3,3,1))
if mibBuilder.loadTexts:cvaIfFXOTimingEntry.setStatus(_B)
class _CvaIfFXOTimingDigitDuration_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_CvaIfFXOTimingDigitDuration_Type.__name__=_C
_CvaIfFXOTimingDigitDuration_Object=MibTableColumn
cvaIfFXOTimingDigitDuration=_CvaIfFXOTimingDigitDuration_Object((1,3,6,1,4,1,9,9,62,1,3,3,1,1),_CvaIfFXOTimingDigitDuration_Type())
cvaIfFXOTimingDigitDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfFXOTimingDigitDuration.setStatus(_B)
if mibBuilder.loadTexts:cvaIfFXOTimingDigitDuration.setUnits(_E)
class _CvaIfFXOTimingInterDigitDuration_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_CvaIfFXOTimingInterDigitDuration_Type.__name__=_C
_CvaIfFXOTimingInterDigitDuration_Object=MibTableColumn
cvaIfFXOTimingInterDigitDuration=_CvaIfFXOTimingInterDigitDuration_Object((1,3,6,1,4,1,9,9,62,1,3,3,1,2),_CvaIfFXOTimingInterDigitDuration_Type())
cvaIfFXOTimingInterDigitDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfFXOTimingInterDigitDuration.setStatus(_B)
if mibBuilder.loadTexts:cvaIfFXOTimingInterDigitDuration.setUnits(_E)
class _CvaIfFXOTimingPulseRate_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,20))
_CvaIfFXOTimingPulseRate_Type.__name__=_C
_CvaIfFXOTimingPulseRate_Object=MibTableColumn
cvaIfFXOTimingPulseRate=_CvaIfFXOTimingPulseRate_Object((1,3,6,1,4,1,9,9,62,1,3,3,1,3),_CvaIfFXOTimingPulseRate_Type())
cvaIfFXOTimingPulseRate.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfFXOTimingPulseRate.setStatus(_B)
if mibBuilder.loadTexts:cvaIfFXOTimingPulseRate.setUnits(_t)
class _CvaIfFXOTimingPulseInterDigitDuration_Type(Integer32):defaultValue=500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,1000))
_CvaIfFXOTimingPulseInterDigitDuration_Type.__name__=_C
_CvaIfFXOTimingPulseInterDigitDuration_Object=MibTableColumn
cvaIfFXOTimingPulseInterDigitDuration=_CvaIfFXOTimingPulseInterDigitDuration_Object((1,3,6,1,4,1,9,9,62,1,3,3,1,4),_CvaIfFXOTimingPulseInterDigitDuration_Type())
cvaIfFXOTimingPulseInterDigitDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfFXOTimingPulseInterDigitDuration.setStatus(_B)
if mibBuilder.loadTexts:cvaIfFXOTimingPulseInterDigitDuration.setUnits(_E)
_CvaIfFXSObjects_ObjectIdentity=ObjectIdentity
cvaIfFXSObjects=_CvaIfFXSObjects_ObjectIdentity((1,3,6,1,4,1,9,9,62,1,4))
_CvaIfFXSCfgTable_Object=MibTable
cvaIfFXSCfgTable=_CvaIfFXSCfgTable_Object((1,3,6,1,4,1,9,9,62,1,4,1))
if mibBuilder.loadTexts:cvaIfFXSCfgTable.setStatus(_B)
_CvaIfFXSCfgEntry_Object=MibTableRow
cvaIfFXSCfgEntry=_CvaIfFXSCfgEntry_Object((1,3,6,1,4,1,9,9,62,1,4,1,1))
cvaIfFXSCfgEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:cvaIfFXSCfgEntry.setStatus(_B)
class _CvaIfFXSCfgSignalType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fxsLoopStart',1),('fxsGroundStart',2)))
_CvaIfFXSCfgSignalType_Type.__name__=_C
_CvaIfFXSCfgSignalType_Object=MibTableColumn
cvaIfFXSCfgSignalType=_CvaIfFXSCfgSignalType_Object((1,3,6,1,4,1,9,9,62,1,4,1,1,1),_CvaIfFXSCfgSignalType_Type())
cvaIfFXSCfgSignalType.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfFXSCfgSignalType.setStatus(_B)
class _CvaIfFXSRingFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('ringFrequency25',1),('ringFrequency50',2),('ringFrequency20',3),('ringFrequency30',4)))
_CvaIfFXSRingFrequency_Type.__name__=_C
_CvaIfFXSRingFrequency_Object=MibTableColumn
cvaIfFXSRingFrequency=_CvaIfFXSRingFrequency_Object((1,3,6,1,4,1,9,9,62,1,4,1,1,2),_CvaIfFXSRingFrequency_Type())
cvaIfFXSRingFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfFXSRingFrequency.setStatus(_B)
_CvaIfFXSStatusTable_Object=MibTable
cvaIfFXSStatusTable=_CvaIfFXSStatusTable_Object((1,3,6,1,4,1,9,9,62,1,4,2))
if mibBuilder.loadTexts:cvaIfFXSStatusTable.setStatus(_B)
_CvaIfFXSStatusEntry_Object=MibTableRow
cvaIfFXSStatusEntry=_CvaIfFXSStatusEntry_Object((1,3,6,1,4,1,9,9,62,1,4,2,1))
if mibBuilder.loadTexts:cvaIfFXSStatusEntry.setStatus(_B)
class _CvaIfFXSHookStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_v,1),(_w,2),(_x,3)))
_CvaIfFXSHookStatus_Type.__name__=_C
_CvaIfFXSHookStatus_Object=MibTableColumn
cvaIfFXSHookStatus=_CvaIfFXSHookStatus_Object((1,3,6,1,4,1,9,9,62,1,4,2,1,1),_CvaIfFXSHookStatus_Type())
cvaIfFXSHookStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cvaIfFXSHookStatus.setStatus(_B)
_CvaIfFXSRingActive_Type=TruthValue
_CvaIfFXSRingActive_Object=MibTableColumn
cvaIfFXSRingActive=_CvaIfFXSRingActive_Object((1,3,6,1,4,1,9,9,62,1,4,2,1,2),_CvaIfFXSRingActive_Type())
cvaIfFXSRingActive.setMaxAccess(_F)
if mibBuilder.loadTexts:cvaIfFXSRingActive.setStatus(_B)
_CvaIfFXSRingGround_Type=TruthValue
_CvaIfFXSRingGround_Object=MibTableColumn
cvaIfFXSRingGround=_CvaIfFXSRingGround_Object((1,3,6,1,4,1,9,9,62,1,4,2,1,3),_CvaIfFXSRingGround_Type())
cvaIfFXSRingGround.setMaxAccess(_F)
if mibBuilder.loadTexts:cvaIfFXSRingGround.setStatus(_B)
_CvaIfFXSTipGround_Type=TruthValue
_CvaIfFXSTipGround_Object=MibTableColumn
cvaIfFXSTipGround=_CvaIfFXSTipGround_Object((1,3,6,1,4,1,9,9,62,1,4,2,1,4),_CvaIfFXSTipGround_Type())
cvaIfFXSTipGround.setMaxAccess(_F)
if mibBuilder.loadTexts:cvaIfFXSTipGround.setStatus(_B)
_CvaIfFXSTimingTable_Object=MibTable
cvaIfFXSTimingTable=_CvaIfFXSTimingTable_Object((1,3,6,1,4,1,9,9,62,1,4,3))
if mibBuilder.loadTexts:cvaIfFXSTimingTable.setStatus(_B)
_CvaIfFXSTimingEntry_Object=MibTableRow
cvaIfFXSTimingEntry=_CvaIfFXSTimingEntry_Object((1,3,6,1,4,1,9,9,62,1,4,3,1))
if mibBuilder.loadTexts:cvaIfFXSTimingEntry.setStatus(_B)
class _CvaIfFXSTimingDigitDuration_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_CvaIfFXSTimingDigitDuration_Type.__name__=_C
_CvaIfFXSTimingDigitDuration_Object=MibTableColumn
cvaIfFXSTimingDigitDuration=_CvaIfFXSTimingDigitDuration_Object((1,3,6,1,4,1,9,9,62,1,4,3,1,1),_CvaIfFXSTimingDigitDuration_Type())
cvaIfFXSTimingDigitDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfFXSTimingDigitDuration.setStatus(_B)
if mibBuilder.loadTexts:cvaIfFXSTimingDigitDuration.setUnits(_E)
class _CvaIfFXSTimingInterDigitDuration_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,500))
_CvaIfFXSTimingInterDigitDuration_Type.__name__=_C
_CvaIfFXSTimingInterDigitDuration_Object=MibTableColumn
cvaIfFXSTimingInterDigitDuration=_CvaIfFXSTimingInterDigitDuration_Object((1,3,6,1,4,1,9,9,62,1,4,3,1,2),_CvaIfFXSTimingInterDigitDuration_Type())
cvaIfFXSTimingInterDigitDuration.setMaxAccess(_D)
if mibBuilder.loadTexts:cvaIfFXSTimingInterDigitDuration.setStatus(_B)
if mibBuilder.loadTexts:cvaIfFXSTimingInterDigitDuration.setUnits(_E)
_CvaIfMIBConformance_ObjectIdentity=ObjectIdentity
cvaIfMIBConformance=_CvaIfMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,62,3))
_CvaIfMIBCompliances_ObjectIdentity=ObjectIdentity
cvaIfMIBCompliances=_CvaIfMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,62,3,1))
_CvaIfMIBGroups_ObjectIdentity=ObjectIdentity
cvaIfMIBGroups=_CvaIfMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,62,3,2))
cvaIfCfgEntry.registerAugmentions((_A,_y))
cvaIfStatusEntry.setIndexNames(*cvaIfCfgEntry.getIndexNames())
cvaIfEMCfgEntry.registerAugmentions((_A,_z))
cvaIfEMStatusEntry.setIndexNames(*cvaIfEMCfgEntry.getIndexNames())
cvaIfEMCfgEntry.registerAugmentions((_A,_A0))
cvaIfEMTimingEntry.setIndexNames(*cvaIfEMCfgEntry.getIndexNames())
cvaIfFXOCfgEntry.registerAugmentions((_A,_A1))
cvaIfFXOStatusEntry.setIndexNames(*cvaIfFXOCfgEntry.getIndexNames())
cvaIfFXOCfgEntry.registerAugmentions((_A,_A2))
cvaIfFXOTimingEntry.setIndexNames(*cvaIfFXOCfgEntry.getIndexNames())
cvaIfFXSCfgEntry.registerAugmentions((_A,_A3))
cvaIfFXSStatusEntry.setIndexNames(*cvaIfFXSCfgEntry.getIndexNames())
cvaIfFXSCfgEntry.registerAugmentions((_A,_A4))
cvaIfFXSTimingEntry.setIndexNames(*cvaIfFXSCfgEntry.getIndexNames())
cvaIfGeneralGroup=ObjectGroup((1,3,6,1,4,1,9,9,62,3,2,1))
cvaIfGeneralGroup.setObjects(*((_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:cvaIfGeneralGroup.setStatus(_B)
cvaIfEMGroup=ObjectGroup((1,3,6,1,4,1,9,9,62,3,2,2))
cvaIfEMGroup.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:cvaIfEMGroup.setStatus(_G)
cvaIfFXOGroup=ObjectGroup((1,3,6,1,4,1,9,9,62,3,2,3))
cvaIfFXOGroup.setObjects(*((_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_AA),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:cvaIfFXOGroup.setStatus(_G)
cvaIfFXSGroup=ObjectGroup((1,3,6,1,4,1,9,9,62,3,2,4))
cvaIfFXSGroup.setObjects(*((_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI)))
if mibBuilder.loadTexts:cvaIfFXSGroup.setStatus(_B)
cvaIfFXOGroup2=ObjectGroup((1,3,6,1,4,1,9,9,62,3,2,5))
cvaIfFXOGroup2.setObjects(*((_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_AJ),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:cvaIfFXOGroup2.setStatus(_B)
cvaIfEMGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,62,3,2,6))
cvaIfEMGroupRev1.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_o),(_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:cvaIfEMGroupRev1.setStatus(_G)
cvaIfEMGroupRev2=ObjectGroup((1,3,6,1,4,1,9,9,62,3,2,7))
cvaIfEMGroupRev2.setObjects(*((_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN)))
if mibBuilder.loadTexts:cvaIfEMGroupRev2.setStatus(_B)
cvaIfMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,62,3,1,1))
cvaIfMIBCompliance.setObjects(*((_A,_Z),(_A,_AO),(_A,_AP),(_A,_a)))
if mibBuilder.loadTexts:cvaIfMIBCompliance.setStatus(_G)
cvaIfMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,62,3,1,2))
cvaIfMIBCompliance2.setObjects(*((_A,_Z),(_A,_AQ),(_A,_s),(_A,_a)))
if mibBuilder.loadTexts:cvaIfMIBCompliance2.setStatus(_G)
cvaIfMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,62,3,1,3))
cvaIfMIBCompliance3.setObjects(*((_A,_Z),(_A,_AR),(_A,_s),(_A,_a)))
if mibBuilder.loadTexts:cvaIfMIBCompliance3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_c:InterfaceDialType,'ciscoVoiceAnalogIfMIB':ciscoVoiceAnalogIfMIB,'cvaIfObjects':cvaIfObjects,'cvaIfGeneralObjects':cvaIfGeneralObjects,'cvaIfCfgTable':cvaIfCfgTable,'cvaIfCfgEntry':cvaIfCfgEntry,_A6:cvaIfCfgImpedance,_A5:cvaIfCfgIntegratedDSP,'cvaIfStatusTable':cvaIfStatusTable,_y:cvaIfStatusEntry,_A7:cvaIfStatusInfoType,_A8:cvaIfMaintenanceMode,_A9:cvaIfStatusSignalErrors,'cvaIfEMObjects':cvaIfEMObjects,'cvaIfEMCfgTable':cvaIfEMCfgTable,'cvaIfEMCfgEntry':cvaIfEMCfgEntry,_L:cvaIfEMCfgSignalType,_M:cvaIfEMCfgOperation,_N:cvaIfEMCfgType,_O:cvaIfEMCfgDialType,_o:cvaIfEMCfgLmrMCap,_p:cvaIfEMCfgLmrECap,_AK:cvaIfEMCfgAutoGainControl,'cvaIfEMStatusTable':cvaIfEMStatusTable,_z:cvaIfEMStatusEntry,_J:cvaIfEMInSeizureActive,_K:cvaIfEMOutSeizureActive,'cvaIfEMTimingTable':cvaIfEMTimingTable,_A0:cvaIfEMTimingEntry,_P:cvaIfEMTimingDigitDuration,_Q:cvaIfEMTimingInterDigitDuration,_R:cvaIfEMTimingPulseRate,_S:cvaIfEMTimingPulseInterDigitDuration,_T:cvaIfEMTimingClearWaitDuration,_U:cvaIfEMTimingMaxWinkWaitDuration,_V:cvaIfEMTimingMaxWinkDuration,_W:cvaIfEMTimingDelayStart,_X:cvaIfEMTimingMaxDelayDuration,_Y:cvaIfEMTimingMinDelayPulseWidth,_q:cvaIfEMTimingVoiceHangover,_r:cvaIfEMTimeoutLmrTeardown,_AL:cvaIfEMTimeoutPttXmt,_AM:cvaIfEMTimeoutPttRcv,_AN:cvaIfEMTimingDelayVoice,'cvaIfFXOObjects':cvaIfFXOObjects,'cvaIfFXOCfgTable':cvaIfFXOCfgTable,'cvaIfFXOCfgEntry':cvaIfFXOCfgEntry,_h:cvaIfFXOCfgSignalType,_i:cvaIfFXOCfgNumberRings,_AA:cvaIfFXOCfgSupDisconnect,_j:cvaIfFXOCfgDialType,_AJ:cvaIfFXOCfgSupDisconnect2,'cvaIfFXOStatusTable':cvaIfFXOStatusTable,_A1:cvaIfFXOStatusEntry,_d:cvaIfFXOHookStatus,_e:cvaIfFXORingDetect,_f:cvaIfFXORingGround,_g:cvaIfFXOTipGround,'cvaIfFXOTimingTable':cvaIfFXOTimingTable,_A2:cvaIfFXOTimingEntry,_k:cvaIfFXOTimingDigitDuration,_l:cvaIfFXOTimingInterDigitDuration,_m:cvaIfFXOTimingPulseRate,_n:cvaIfFXOTimingPulseInterDigitDuration,'cvaIfFXSObjects':cvaIfFXSObjects,'cvaIfFXSCfgTable':cvaIfFXSCfgTable,'cvaIfFXSCfgEntry':cvaIfFXSCfgEntry,_AF:cvaIfFXSCfgSignalType,_AG:cvaIfFXSRingFrequency,'cvaIfFXSStatusTable':cvaIfFXSStatusTable,_A3:cvaIfFXSStatusEntry,_AB:cvaIfFXSHookStatus,_AC:cvaIfFXSRingActive,_AD:cvaIfFXSRingGround,_AE:cvaIfFXSTipGround,'cvaIfFXSTimingTable':cvaIfFXSTimingTable,_A4:cvaIfFXSTimingEntry,_AH:cvaIfFXSTimingDigitDuration,_AI:cvaIfFXSTimingInterDigitDuration,'cvaIfMIBConformance':cvaIfMIBConformance,'cvaIfMIBCompliances':cvaIfMIBCompliances,'cvaIfMIBCompliance':cvaIfMIBCompliance,'cvaIfMIBCompliance2':cvaIfMIBCompliance2,'cvaIfMIBCompliance3':cvaIfMIBCompliance3,'cvaIfMIBGroups':cvaIfMIBGroups,_Z:cvaIfGeneralGroup,_AO:cvaIfEMGroup,_AP:cvaIfFXOGroup,_a:cvaIfFXSGroup,_s:cvaIfFXOGroup2,_AQ:cvaIfEMGroupRev1,_AR:cvaIfEMGroupRev2})