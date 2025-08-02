_o='hwCBQoSFrClassApplyPolicyDirection'
_n='hwCBQoSFrClassApplyPolicyFrClassName'
_m='WredType'
_l='hwCBQoSRemarkType'
_k='hwCBQoSMatchRuleIndex'
_j='remark'
_i='remarkMplsExp'
_h='remarkDscp'
_g='remarkIpPrec'
_f='discard'
_e='typeMplsExp'
_d='typeVlan8021p'
_c='typeDscp'
_b='typeIpPrec'
_a='hwCBQoSIfVlanApplyPolicyDirection'
_Z='hwCBQoSIfVlanApplyPolicyVlanid'
_Y='hwCBQoSIfVlanApplyPolicyIfIndex'
_X='hwCBQoSPolicyIndex'
_W='CarAction'
_V='hwCBQoSClassifierIndex'
_U='hwCBQoSWredClassValue'
_T='read-write'
_S='unavailable'
_R='hwCBQoSFrPvcApplyPolicyDirection'
_Q='hwCBQoSAtmPvcApplyPolicyDirection'
_P='hwCBQoSIfApplyPolicyDirection'
_O='hwCBQoSFrPvcApplyPolicyDlciNum'
_N='hwCBQoSFrPvcApplyPolicyIfIndex'
_M='hwCBQoSAtmPvcApplyPolicyVCI'
_L='hwCBQoSAtmPvcApplyPolicyVPI'
_K='hwCBQoSAtmPvcApplyPolicyIfIndex'
_J='hwCBQoSIfApplyPolicyIfIndex'
_I='hwCBQoSBehaviorIndex'
_H='OctetString'
_G='not-accessible'
_F='hwCBQoSPolicyClassIndex'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='A3COM-HUAWEI-CBQOS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hwQoS,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','hwQoS')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
hwCBQoSMIB=ModuleIdentity((1,3,6,1,4,1,43,45,1,5,25,32,1))
class MatchRuleType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,16,17,25)));namedValues=NamedValues(*(('typeAny',1),('typeAcl',2),('typeRtpPort',3),('typeProtocol',4),(_b,5),(_c,6),(_d,7),(_e,8),('typeSourceMac',9),('typeDestinationMac',10),('typeClassifier',11),('typeInboundInterface',12),('typeMacGroup',13),('typeMatchDe',16),('typeMatchClp',17),('typeOutboundInterface',25)))
class CarAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('pass',1),(_f,2),(_g,3),(_h,4),(_i,5),(_j,6)))
class RemarkType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_b,1),(_c,2),(_e,3),(_d,4),('typeAtmClp',5),('typeFrDe',6)))
class WredType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('typeIpPrecbased',1),('typeDscpbased',2)))
class QueueType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ef',1),('af',2),('wfq',3)))
class QueueBandwidthUnit(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2,3)));namedValues=NamedValues(*(('unitUnavailable',-1),('unitAbsolute',1),('unitPercent',2),('unitRemainPercent',3)))
class LrCirUnit(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('absoluteUnitBps',1),('percentUnit',2)))
class DirectionType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inbound',1),('outbound',2)))
_HwCBQoSObjects_ObjectIdentity=ObjectIdentity
hwCBQoSObjects=_HwCBQoSObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,32,1,1))
_HwCBQoSClassifierObjects_ObjectIdentity=ObjectIdentity
hwCBQoSClassifierObjects=_HwCBQoSClassifierObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,32,1,1,1))
_HwCBQoSClassifierIndexNext_Type=Integer32
_HwCBQoSClassifierIndexNext_Object=MibScalar
hwCBQoSClassifierIndexNext=_HwCBQoSClassifierIndexNext_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,1,1),_HwCBQoSClassifierIndexNext_Type())
hwCBQoSClassifierIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSClassifierIndexNext.setStatus(_A)
_HwCBQoSClassifierCfgInfoTable_Object=MibTable
hwCBQoSClassifierCfgInfoTable=_HwCBQoSClassifierCfgInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,1,2))
if mibBuilder.loadTexts:hwCBQoSClassifierCfgInfoTable.setStatus(_A)
_HwCBQoSClassifierCfgInfoEntry_Object=MibTableRow
hwCBQoSClassifierCfgInfoEntry=_HwCBQoSClassifierCfgInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,1,2,1))
hwCBQoSClassifierCfgInfoEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:hwCBQoSClassifierCfgInfoEntry.setStatus(_A)
_HwCBQoSClassifierIndex_Type=Integer32
_HwCBQoSClassifierIndex_Object=MibTableColumn
hwCBQoSClassifierIndex=_HwCBQoSClassifierIndex_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,1,2,1,1),_HwCBQoSClassifierIndex_Type())
hwCBQoSClassifierIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hwCBQoSClassifierIndex.setStatus(_A)
class _HwCBQoSClassifierName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HwCBQoSClassifierName_Type.__name__=_H
_HwCBQoSClassifierName_Object=MibTableColumn
hwCBQoSClassifierName=_HwCBQoSClassifierName_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,1,2,1,2),_HwCBQoSClassifierName_Type())
hwCBQoSClassifierName.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSClassifierName.setStatus(_A)
_HwCBQoSClassifierRuleCount_Type=Integer32
_HwCBQoSClassifierRuleCount_Object=MibTableColumn
hwCBQoSClassifierRuleCount=_HwCBQoSClassifierRuleCount_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,1,2,1,3),_HwCBQoSClassifierRuleCount_Type())
hwCBQoSClassifierRuleCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSClassifierRuleCount.setStatus(_A)
class _HwCBQoSClassifierOperator_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('and',1),('or',2)))
_HwCBQoSClassifierOperator_Type.__name__=_E
_HwCBQoSClassifierOperator_Object=MibTableColumn
hwCBQoSClassifierOperator=_HwCBQoSClassifierOperator_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,1,2,1,4),_HwCBQoSClassifierOperator_Type())
hwCBQoSClassifierOperator.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSClassifierOperator.setStatus(_A)
class _HwCBQoSClassifierLayer_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2,3)));namedValues=NamedValues(*((_S,-1),('l2',1),('l3',2),('both',3)))
_HwCBQoSClassifierLayer_Type.__name__=_E
_HwCBQoSClassifierLayer_Object=MibTableColumn
hwCBQoSClassifierLayer=_HwCBQoSClassifierLayer_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,1,2,1,5),_HwCBQoSClassifierLayer_Type())
hwCBQoSClassifierLayer.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSClassifierLayer.setStatus(_A)
_HwCBQoSClassifierRowStatus_Type=RowStatus
_HwCBQoSClassifierRowStatus_Object=MibTableColumn
hwCBQoSClassifierRowStatus=_HwCBQoSClassifierRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,1,2,1,6),_HwCBQoSClassifierRowStatus_Type())
hwCBQoSClassifierRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSClassifierRowStatus.setStatus(_A)
_HwCBQoSMatchRuleCfgInfoTable_Object=MibTable
hwCBQoSMatchRuleCfgInfoTable=_HwCBQoSMatchRuleCfgInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,1,3))
if mibBuilder.loadTexts:hwCBQoSMatchRuleCfgInfoTable.setStatus(_A)
_HwCBQoSMatchRuleCfgInfoEntry_Object=MibTableRow
hwCBQoSMatchRuleCfgInfoEntry=_HwCBQoSMatchRuleCfgInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,1,3,1))
hwCBQoSMatchRuleCfgInfoEntry.setIndexNames((0,_B,_V),(0,_B,_k))
if mibBuilder.loadTexts:hwCBQoSMatchRuleCfgInfoEntry.setStatus(_A)
_HwCBQoSMatchRuleIndex_Type=Integer32
_HwCBQoSMatchRuleIndex_Object=MibTableColumn
hwCBQoSMatchRuleIndex=_HwCBQoSMatchRuleIndex_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,1,3,1,1),_HwCBQoSMatchRuleIndex_Type())
hwCBQoSMatchRuleIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hwCBQoSMatchRuleIndex.setStatus(_A)
class _HwCBQoSMatchRuleIfNot_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('match',1),('match-Not',2)))
_HwCBQoSMatchRuleIfNot_Type.__name__=_E
_HwCBQoSMatchRuleIfNot_Object=MibTableColumn
hwCBQoSMatchRuleIfNot=_HwCBQoSMatchRuleIfNot_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,1,3,1,2),_HwCBQoSMatchRuleIfNot_Type())
hwCBQoSMatchRuleIfNot.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSMatchRuleIfNot.setStatus(_A)
_HwCBQoSMatchRuleType_Type=MatchRuleType
_HwCBQoSMatchRuleType_Object=MibTableColumn
hwCBQoSMatchRuleType=_HwCBQoSMatchRuleType_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,1,3,1,3),_HwCBQoSMatchRuleType_Type())
hwCBQoSMatchRuleType.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSMatchRuleType.setStatus(_A)
class _HwCBQoSMatchRuleStringValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HwCBQoSMatchRuleStringValue_Type.__name__=_H
_HwCBQoSMatchRuleStringValue_Object=MibTableColumn
hwCBQoSMatchRuleStringValue=_HwCBQoSMatchRuleStringValue_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,1,3,1,4),_HwCBQoSMatchRuleStringValue_Type())
hwCBQoSMatchRuleStringValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSMatchRuleStringValue.setStatus(_A)
_HwCBQoSMatchRuleIntValue1_Type=Unsigned32
_HwCBQoSMatchRuleIntValue1_Object=MibTableColumn
hwCBQoSMatchRuleIntValue1=_HwCBQoSMatchRuleIntValue1_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,1,3,1,5),_HwCBQoSMatchRuleIntValue1_Type())
hwCBQoSMatchRuleIntValue1.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSMatchRuleIntValue1.setStatus(_A)
_HwCBQoSMatchRuleIntValue2_Type=Unsigned32
_HwCBQoSMatchRuleIntValue2_Object=MibTableColumn
hwCBQoSMatchRuleIntValue2=_HwCBQoSMatchRuleIntValue2_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,1,3,1,6),_HwCBQoSMatchRuleIntValue2_Type())
hwCBQoSMatchRuleIntValue2.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSMatchRuleIntValue2.setStatus(_A)
_HwCBQoSMatchRuleRowStatus_Type=RowStatus
_HwCBQoSMatchRuleRowStatus_Object=MibTableColumn
hwCBQoSMatchRuleRowStatus=_HwCBQoSMatchRuleRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,1,3,1,7),_HwCBQoSMatchRuleRowStatus_Type())
hwCBQoSMatchRuleRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSMatchRuleRowStatus.setStatus(_A)
_HwCBQoSBehaviorObjects_ObjectIdentity=ObjectIdentity
hwCBQoSBehaviorObjects=_HwCBQoSBehaviorObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2))
_HwCBQoSBehaviorIndexNext_Type=Integer32
_HwCBQoSBehaviorIndexNext_Object=MibScalar
hwCBQoSBehaviorIndexNext=_HwCBQoSBehaviorIndexNext_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,1),_HwCBQoSBehaviorIndexNext_Type())
hwCBQoSBehaviorIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSBehaviorIndexNext.setStatus(_A)
_HwCBQoSBehaviorCfgInfoTable_Object=MibTable
hwCBQoSBehaviorCfgInfoTable=_HwCBQoSBehaviorCfgInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,2))
if mibBuilder.loadTexts:hwCBQoSBehaviorCfgInfoTable.setStatus(_A)
_HwCBQoSBehaviorCfgInfoEntry_Object=MibTableRow
hwCBQoSBehaviorCfgInfoEntry=_HwCBQoSBehaviorCfgInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,2,1))
hwCBQoSBehaviorCfgInfoEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:hwCBQoSBehaviorCfgInfoEntry.setStatus(_A)
_HwCBQoSBehaviorIndex_Type=Integer32
_HwCBQoSBehaviorIndex_Object=MibTableColumn
hwCBQoSBehaviorIndex=_HwCBQoSBehaviorIndex_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,2,1,1),_HwCBQoSBehaviorIndex_Type())
hwCBQoSBehaviorIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hwCBQoSBehaviorIndex.setStatus(_A)
class _HwCBQoSBehaviorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HwCBQoSBehaviorName_Type.__name__=_H
_HwCBQoSBehaviorName_Object=MibTableColumn
hwCBQoSBehaviorName=_HwCBQoSBehaviorName_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,2,1,2),_HwCBQoSBehaviorName_Type())
hwCBQoSBehaviorName.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSBehaviorName.setStatus(_A)
_HwCBQoSBehaviorRowStatus_Type=RowStatus
_HwCBQoSBehaviorRowStatus_Object=MibTableColumn
hwCBQoSBehaviorRowStatus=_HwCBQoSBehaviorRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,2,1,3),_HwCBQoSBehaviorRowStatus_Type())
hwCBQoSBehaviorRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSBehaviorRowStatus.setStatus(_A)
_HwCBQoSCarCfgInfoTable_Object=MibTable
hwCBQoSCarCfgInfoTable=_HwCBQoSCarCfgInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,3))
if mibBuilder.loadTexts:hwCBQoSCarCfgInfoTable.setStatus(_A)
_HwCBQoSCarCfgInfoEntry_Object=MibTableRow
hwCBQoSCarCfgInfoEntry=_HwCBQoSCarCfgInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,3,1))
hwCBQoSCarCfgInfoEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:hwCBQoSCarCfgInfoEntry.setStatus(_A)
class _HwCBQoSCarCir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8,10000000))
_HwCBQoSCarCir_Type.__name__=_E
_HwCBQoSCarCir_Object=MibTableColumn
hwCBQoSCarCir=_HwCBQoSCarCir_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,3,1,1),_HwCBQoSCarCir_Type())
hwCBQoSCarCir.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSCarCir.setStatus(_A)
class _HwCBQoSCarCbs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,19375000))
_HwCBQoSCarCbs_Type.__name__=_E
_HwCBQoSCarCbs_Object=MibTableColumn
hwCBQoSCarCbs=_HwCBQoSCarCbs_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,3,1,2),_HwCBQoSCarCbs_Type())
hwCBQoSCarCbs.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSCarCbs.setStatus(_A)
class _HwCBQoSCarEbs_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,19375000))
_HwCBQoSCarEbs_Type.__name__=_E
_HwCBQoSCarEbs_Object=MibTableColumn
hwCBQoSCarEbs=_HwCBQoSCarEbs_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,3,1,3),_HwCBQoSCarEbs_Type())
hwCBQoSCarEbs.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSCarEbs.setStatus(_A)
class _HwCBQoSCarPir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(100,10000000))
_HwCBQoSCarPir_Type.__name__=_E
_HwCBQoSCarPir_Object=MibTableColumn
hwCBQoSCarPir=_HwCBQoSCarPir_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,3,1,4),_HwCBQoSCarPir_Type())
hwCBQoSCarPir.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSCarPir.setStatus(_A)
class _HwCBQoSCarPbs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(64,4000000))
_HwCBQoSCarPbs_Type.__name__=_E
_HwCBQoSCarPbs_Object=MibTableColumn
hwCBQoSCarPbs=_HwCBQoSCarPbs_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,3,1,5),_HwCBQoSCarPbs_Type())
hwCBQoSCarPbs.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSCarPbs.setStatus(_A)
class _HwCBQoSCarGreenAction_Type(CarAction):defaultValue=1
_HwCBQoSCarGreenAction_Type.__name__=_W
_HwCBQoSCarGreenAction_Object=MibTableColumn
hwCBQoSCarGreenAction=_HwCBQoSCarGreenAction_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,3,1,6),_HwCBQoSCarGreenAction_Type())
hwCBQoSCarGreenAction.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSCarGreenAction.setStatus(_A)
class _HwCBQoSCarGreenRemarkValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,63))
_HwCBQoSCarGreenRemarkValue_Type.__name__=_E
_HwCBQoSCarGreenRemarkValue_Object=MibTableColumn
hwCBQoSCarGreenRemarkValue=_HwCBQoSCarGreenRemarkValue_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,3,1,7),_HwCBQoSCarGreenRemarkValue_Type())
hwCBQoSCarGreenRemarkValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSCarGreenRemarkValue.setStatus(_A)
class _HwCBQoSCarYellowAction_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2,3,4,5,6)));namedValues=NamedValues(*((_S,-1),('pass',1),(_f,2),(_g,3),(_h,4),(_i,5),(_j,6)))
_HwCBQoSCarYellowAction_Type.__name__=_E
_HwCBQoSCarYellowAction_Object=MibTableColumn
hwCBQoSCarYellowAction=_HwCBQoSCarYellowAction_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,3,1,8),_HwCBQoSCarYellowAction_Type())
hwCBQoSCarYellowAction.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSCarYellowAction.setStatus(_A)
class _HwCBQoSCarRedAction_Type(CarAction):defaultValue=2
_HwCBQoSCarRedAction_Type.__name__=_W
_HwCBQoSCarRedAction_Object=MibTableColumn
hwCBQoSCarRedAction=_HwCBQoSCarRedAction_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,3,1,9),_HwCBQoSCarRedAction_Type())
hwCBQoSCarRedAction.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSCarRedAction.setStatus(_A)
class _HwCBQoSCarRedRemarkValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,63))
_HwCBQoSCarRedRemarkValue_Type.__name__=_E
_HwCBQoSCarRedRemarkValue_Object=MibTableColumn
hwCBQoSCarRedRemarkValue=_HwCBQoSCarRedRemarkValue_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,3,1,10),_HwCBQoSCarRedRemarkValue_Type())
hwCBQoSCarRedRemarkValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSCarRedRemarkValue.setStatus(_A)
_HwCBQoSCarRowStatus_Type=RowStatus
_HwCBQoSCarRowStatus_Object=MibTableColumn
hwCBQoSCarRowStatus=_HwCBQoSCarRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,3,1,11),_HwCBQoSCarRowStatus_Type())
hwCBQoSCarRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSCarRowStatus.setStatus(_A)
_HwCBQoSGtsCfgInfoTable_Object=MibTable
hwCBQoSGtsCfgInfoTable=_HwCBQoSGtsCfgInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,4))
if mibBuilder.loadTexts:hwCBQoSGtsCfgInfoTable.setStatus(_A)
_HwCBQoSGtsCfgInfoEntry_Object=MibTableRow
hwCBQoSGtsCfgInfoEntry=_HwCBQoSGtsCfgInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,4,1))
hwCBQoSGtsCfgInfoEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:hwCBQoSGtsCfgInfoEntry.setStatus(_A)
class _HwCBQoSGtsCir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8000,155000000))
_HwCBQoSGtsCir_Type.__name__=_E
_HwCBQoSGtsCir_Object=MibTableColumn
hwCBQoSGtsCir=_HwCBQoSGtsCir_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,4,1,1),_HwCBQoSGtsCir_Type())
hwCBQoSGtsCir.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSGtsCir.setStatus(_A)
class _HwCBQoSGtsCbs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(15000,155000000))
_HwCBQoSGtsCbs_Type.__name__=_E
_HwCBQoSGtsCbs_Object=MibTableColumn
hwCBQoSGtsCbs=_HwCBQoSGtsCbs_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,4,1,2),_HwCBQoSGtsCbs_Type())
hwCBQoSGtsCbs.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSGtsCbs.setStatus(_A)
class _HwCBQoSGtsEbs_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,155000000))
_HwCBQoSGtsEbs_Type.__name__=_E
_HwCBQoSGtsEbs_Object=MibTableColumn
hwCBQoSGtsEbs=_HwCBQoSGtsEbs_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,4,1,3),_HwCBQoSGtsEbs_Type())
hwCBQoSGtsEbs.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSGtsEbs.setStatus(_A)
class _HwCBQoSGtsQueueLength_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_HwCBQoSGtsQueueLength_Type.__name__=_E
_HwCBQoSGtsQueueLength_Object=MibTableColumn
hwCBQoSGtsQueueLength=_HwCBQoSGtsQueueLength_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,4,1,4),_HwCBQoSGtsQueueLength_Type())
hwCBQoSGtsQueueLength.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSGtsQueueLength.setStatus(_A)
_HwCBQoSGtsRowStatus_Type=RowStatus
_HwCBQoSGtsRowStatus_Object=MibTableColumn
hwCBQoSGtsRowStatus=_HwCBQoSGtsRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,4,1,5),_HwCBQoSGtsRowStatus_Type())
hwCBQoSGtsRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSGtsRowStatus.setStatus(_A)
_HwCBQoSRemarkCfgInfoTable_Object=MibTable
hwCBQoSRemarkCfgInfoTable=_HwCBQoSRemarkCfgInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,5))
if mibBuilder.loadTexts:hwCBQoSRemarkCfgInfoTable.setStatus(_A)
_HwCBQoSRemarkCfgInfoEntry_Object=MibTableRow
hwCBQoSRemarkCfgInfoEntry=_HwCBQoSRemarkCfgInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,5,1))
hwCBQoSRemarkCfgInfoEntry.setIndexNames((0,_B,_I),(0,_B,_l))
if mibBuilder.loadTexts:hwCBQoSRemarkCfgInfoEntry.setStatus(_A)
_HwCBQoSRemarkType_Type=RemarkType
_HwCBQoSRemarkType_Object=MibTableColumn
hwCBQoSRemarkType=_HwCBQoSRemarkType_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,5,1,1),_HwCBQoSRemarkType_Type())
hwCBQoSRemarkType.setMaxAccess(_G)
if mibBuilder.loadTexts:hwCBQoSRemarkType.setStatus(_A)
class _HwCBQoSRemarkValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HwCBQoSRemarkValue_Type.__name__=_E
_HwCBQoSRemarkValue_Object=MibTableColumn
hwCBQoSRemarkValue=_HwCBQoSRemarkValue_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,5,1,2),_HwCBQoSRemarkValue_Type())
hwCBQoSRemarkValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSRemarkValue.setStatus(_A)
_HwCBQoSRemarkRowStatus_Type=RowStatus
_HwCBQoSRemarkRowStatus_Object=MibTableColumn
hwCBQoSRemarkRowStatus=_HwCBQoSRemarkRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,5,1,3),_HwCBQoSRemarkRowStatus_Type())
hwCBQoSRemarkRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSRemarkRowStatus.setStatus(_A)
_HwCBQoSQueueCfgInfoTable_Object=MibTable
hwCBQoSQueueCfgInfoTable=_HwCBQoSQueueCfgInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,6))
if mibBuilder.loadTexts:hwCBQoSQueueCfgInfoTable.setStatus(_A)
_HwCBQoSQueueCfgInfoEntry_Object=MibTableRow
hwCBQoSQueueCfgInfoEntry=_HwCBQoSQueueCfgInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,6,1))
hwCBQoSQueueCfgInfoEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:hwCBQoSQueueCfgInfoEntry.setStatus(_A)
_HwCBQoSQueueType_Type=QueueType
_HwCBQoSQueueType_Object=MibTableColumn
hwCBQoSQueueType=_HwCBQoSQueueType_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,6,1,1),_HwCBQoSQueueType_Type())
hwCBQoSQueueType.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSQueueType.setStatus(_A)
class _HwCBQoSQueueDropType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*(('typeUnavailable',-1),('typeTailDrop',1),('typeWred',2)))
_HwCBQoSQueueDropType_Type.__name__=_E
_HwCBQoSQueueDropType_Object=MibTableColumn
hwCBQoSQueueDropType=_HwCBQoSQueueDropType_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,6,1,2),_HwCBQoSQueueDropType_Type())
hwCBQoSQueueDropType.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSQueueDropType.setStatus(_A)
class _HwCBQoSQueueLength_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,512))
_HwCBQoSQueueLength_Type.__name__=_E
_HwCBQoSQueueLength_Object=MibTableColumn
hwCBQoSQueueLength=_HwCBQoSQueueLength_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,6,1,3),_HwCBQoSQueueLength_Type())
hwCBQoSQueueLength.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSQueueLength.setStatus(_A)
_HwCBQoSQueueBandwidthUnit_Type=QueueBandwidthUnit
_HwCBQoSQueueBandwidthUnit_Object=MibTableColumn
hwCBQoSQueueBandwidthUnit=_HwCBQoSQueueBandwidthUnit_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,6,1,4),_HwCBQoSQueueBandwidthUnit_Type())
hwCBQoSQueueBandwidthUnit.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSQueueBandwidthUnit.setStatus(_A)
class _HwCBQoSQueueBandwidthValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(1,1000000))
_HwCBQoSQueueBandwidthValue_Type.__name__=_E
_HwCBQoSQueueBandwidthValue_Object=MibTableColumn
hwCBQoSQueueBandwidthValue=_HwCBQoSQueueBandwidthValue_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,6,1,5),_HwCBQoSQueueBandwidthValue_Type())
hwCBQoSQueueBandwidthValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSQueueBandwidthValue.setStatus(_A)
class _HwCBQoSQueueCbs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(32,2000000))
_HwCBQoSQueueCbs_Type.__name__=_E
_HwCBQoSQueueCbs_Object=MibTableColumn
hwCBQoSQueueCbs=_HwCBQoSQueueCbs_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,6,1,6),_HwCBQoSQueueCbs_Type())
hwCBQoSQueueCbs.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSQueueCbs.setStatus(_A)
class _HwCBQoSQueueQueueNumber_Type(Integer32):defaultValue=256;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,16,32,64,128,256,512,1024,2048,4096)));namedValues=NamedValues(*((_S,-1),('a16',16),('a32',32),('a64',64),('a128',128),('a256',256),('a512',512),('a1024',1024),('a2048',2048),('a4096',4096)))
_HwCBQoSQueueQueueNumber_Type.__name__=_E
_HwCBQoSQueueQueueNumber_Object=MibTableColumn
hwCBQoSQueueQueueNumber=_HwCBQoSQueueQueueNumber_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,6,1,7),_HwCBQoSQueueQueueNumber_Type())
hwCBQoSQueueQueueNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSQueueQueueNumber.setStatus(_A)
_HwCBQoSQueueRowStatus_Type=RowStatus
_HwCBQoSQueueRowStatus_Object=MibTableColumn
hwCBQoSQueueRowStatus=_HwCBQoSQueueRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,6,1,8),_HwCBQoSQueueRowStatus_Type())
hwCBQoSQueueRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSQueueRowStatus.setStatus(_A)
class _HwCBQoSQueueCbsRatio_Type(Integer32):defaultValue=25;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(25,500))
_HwCBQoSQueueCbsRatio_Type.__name__=_E
_HwCBQoSQueueCbsRatio_Object=MibTableColumn
hwCBQoSQueueCbsRatio=_HwCBQoSQueueCbsRatio_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,6,1,9),_HwCBQoSQueueCbsRatio_Type())
hwCBQoSQueueCbsRatio.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSQueueCbsRatio.setStatus(_A)
_HwCBQoSWredCfgInfoTable_Object=MibTable
hwCBQoSWredCfgInfoTable=_HwCBQoSWredCfgInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,7))
if mibBuilder.loadTexts:hwCBQoSWredCfgInfoTable.setStatus(_A)
_HwCBQoSWredCfgInfoEntry_Object=MibTableRow
hwCBQoSWredCfgInfoEntry=_HwCBQoSWredCfgInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,7,1))
hwCBQoSWredCfgInfoEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:hwCBQoSWredCfgInfoEntry.setStatus(_A)
class _HwCBQoSWredType_Type(WredType):defaultValue=1
_HwCBQoSWredType_Type.__name__=_m
_HwCBQoSWredType_Object=MibTableColumn
hwCBQoSWredType=_HwCBQoSWredType_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,7,1,1),_HwCBQoSWredType_Type())
hwCBQoSWredType.setMaxAccess(_T)
if mibBuilder.loadTexts:hwCBQoSWredType.setStatus(_A)
class _HwCBQoSWredWeightConst_Type(Integer32):defaultValue=9;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HwCBQoSWredWeightConst_Type.__name__=_E
_HwCBQoSWredWeightConst_Object=MibTableColumn
hwCBQoSWredWeightConst=_HwCBQoSWredWeightConst_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,7,1,2),_HwCBQoSWredWeightConst_Type())
hwCBQoSWredWeightConst.setMaxAccess(_T)
if mibBuilder.loadTexts:hwCBQoSWredWeightConst.setStatus(_A)
_HwCBQoSWredClassCfgInfoTable_Object=MibTable
hwCBQoSWredClassCfgInfoTable=_HwCBQoSWredClassCfgInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,8))
if mibBuilder.loadTexts:hwCBQoSWredClassCfgInfoTable.setStatus(_A)
_HwCBQoSWredClassCfgInfoEntry_Object=MibTableRow
hwCBQoSWredClassCfgInfoEntry=_HwCBQoSWredClassCfgInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,8,1))
hwCBQoSWredClassCfgInfoEntry.setIndexNames((0,_B,_I),(0,_B,_U))
if mibBuilder.loadTexts:hwCBQoSWredClassCfgInfoEntry.setStatus(_A)
class _HwCBQoSWredClassValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HwCBQoSWredClassValue_Type.__name__=_E
_HwCBQoSWredClassValue_Object=MibTableColumn
hwCBQoSWredClassValue=_HwCBQoSWredClassValue_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,8,1,1),_HwCBQoSWredClassValue_Type())
hwCBQoSWredClassValue.setMaxAccess(_G)
if mibBuilder.loadTexts:hwCBQoSWredClassValue.setStatus(_A)
class _HwCBQoSWredClassLowLimit_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_HwCBQoSWredClassLowLimit_Type.__name__=_E
_HwCBQoSWredClassLowLimit_Object=MibTableColumn
hwCBQoSWredClassLowLimit=_HwCBQoSWredClassLowLimit_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,8,1,2),_HwCBQoSWredClassLowLimit_Type())
hwCBQoSWredClassLowLimit.setMaxAccess(_T)
if mibBuilder.loadTexts:hwCBQoSWredClassLowLimit.setStatus(_A)
class _HwCBQoSWredClassHighLimit_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_HwCBQoSWredClassHighLimit_Type.__name__=_E
_HwCBQoSWredClassHighLimit_Object=MibTableColumn
hwCBQoSWredClassHighLimit=_HwCBQoSWredClassHighLimit_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,8,1,3),_HwCBQoSWredClassHighLimit_Type())
hwCBQoSWredClassHighLimit.setMaxAccess(_T)
if mibBuilder.loadTexts:hwCBQoSWredClassHighLimit.setStatus(_A)
class _HwCBQoSWredClassDiscardProb_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HwCBQoSWredClassDiscardProb_Type.__name__=_E
_HwCBQoSWredClassDiscardProb_Object=MibTableColumn
hwCBQoSWredClassDiscardProb=_HwCBQoSWredClassDiscardProb_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,8,1,4),_HwCBQoSWredClassDiscardProb_Type())
hwCBQoSWredClassDiscardProb.setMaxAccess(_T)
if mibBuilder.loadTexts:hwCBQoSWredClassDiscardProb.setStatus(_A)
_HwCBQoSPolicyRouteCfgInfoTable_Object=MibTable
hwCBQoSPolicyRouteCfgInfoTable=_HwCBQoSPolicyRouteCfgInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,9))
if mibBuilder.loadTexts:hwCBQoSPolicyRouteCfgInfoTable.setStatus(_A)
_HwCBQoSPolicyRouteCfgInfoEntry_Object=MibTableRow
hwCBQoSPolicyRouteCfgInfoEntry=_HwCBQoSPolicyRouteCfgInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,9,1))
hwCBQoSPolicyRouteCfgInfoEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:hwCBQoSPolicyRouteCfgInfoEntry.setStatus(_A)
_HwCBQoSPolicyRouteNexthop_Type=IpAddress
_HwCBQoSPolicyRouteNexthop_Object=MibTableColumn
hwCBQoSPolicyRouteNexthop=_HwCBQoSPolicyRouteNexthop_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,9,1,1),_HwCBQoSPolicyRouteNexthop_Type())
hwCBQoSPolicyRouteNexthop.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSPolicyRouteNexthop.setStatus(_A)
class _HwCBQoSPolicyRouteBackup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('backup',1),('notbackup',2)))
_HwCBQoSPolicyRouteBackup_Type.__name__=_E
_HwCBQoSPolicyRouteBackup_Object=MibTableColumn
hwCBQoSPolicyRouteBackup=_HwCBQoSPolicyRouteBackup_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,9,1,2),_HwCBQoSPolicyRouteBackup_Type())
hwCBQoSPolicyRouteBackup.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSPolicyRouteBackup.setStatus(_A)
_HwCBQoSPolicyRouteRowStatus_Type=RowStatus
_HwCBQoSPolicyRouteRowStatus_Object=MibTableColumn
hwCBQoSPolicyRouteRowStatus=_HwCBQoSPolicyRouteRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,9,1,3),_HwCBQoSPolicyRouteRowStatus_Type())
hwCBQoSPolicyRouteRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSPolicyRouteRowStatus.setStatus(_A)
_HwCBQoSNatCfgInfoTable_Object=MibTable
hwCBQoSNatCfgInfoTable=_HwCBQoSNatCfgInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,10))
if mibBuilder.loadTexts:hwCBQoSNatCfgInfoTable.setStatus(_A)
_HwCBQoSNatCfgInfoEntry_Object=MibTableRow
hwCBQoSNatCfgInfoEntry=_HwCBQoSNatCfgInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,10,1))
hwCBQoSNatCfgInfoEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:hwCBQoSNatCfgInfoEntry.setStatus(_A)
class _HwCBQoSNatMainNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HwCBQoSNatMainNumber_Type.__name__=_E
_HwCBQoSNatMainNumber_Object=MibTableColumn
hwCBQoSNatMainNumber=_HwCBQoSNatMainNumber_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,10,1,1),_HwCBQoSNatMainNumber_Type())
hwCBQoSNatMainNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSNatMainNumber.setStatus(_A)
class _HwCBQoSNatBackupNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HwCBQoSNatBackupNumber_Type.__name__=_E
_HwCBQoSNatBackupNumber_Object=MibTableColumn
hwCBQoSNatBackupNumber=_HwCBQoSNatBackupNumber_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,10,1,2),_HwCBQoSNatBackupNumber_Type())
hwCBQoSNatBackupNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSNatBackupNumber.setStatus(_A)
class _HwCBQoSNatServiceClass_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_HwCBQoSNatServiceClass_Type.__name__=_E
_HwCBQoSNatServiceClass_Object=MibTableColumn
hwCBQoSNatServiceClass=_HwCBQoSNatServiceClass_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,10,1,3),_HwCBQoSNatServiceClass_Type())
hwCBQoSNatServiceClass.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSNatServiceClass.setStatus(_A)
_HwCBQoSNatRowStatus_Type=RowStatus
_HwCBQoSNatRowStatus_Object=MibTableColumn
hwCBQoSNatRowStatus=_HwCBQoSNatRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,10,1,4),_HwCBQoSNatRowStatus_Type())
hwCBQoSNatRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSNatRowStatus.setStatus(_A)
_HwCBQoSFirewallCfgInfoTable_Object=MibTable
hwCBQoSFirewallCfgInfoTable=_HwCBQoSFirewallCfgInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,11))
if mibBuilder.loadTexts:hwCBQoSFirewallCfgInfoTable.setStatus(_A)
_HwCBQoSFirewallCfgInfoEntry_Object=MibTableRow
hwCBQoSFirewallCfgInfoEntry=_HwCBQoSFirewallCfgInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,11,1))
hwCBQoSFirewallCfgInfoEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:hwCBQoSFirewallCfgInfoEntry.setStatus(_A)
class _HwCBQoSFirewallAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
_HwCBQoSFirewallAction_Type.__name__=_E
_HwCBQoSFirewallAction_Object=MibTableColumn
hwCBQoSFirewallAction=_HwCBQoSFirewallAction_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,11,1,1),_HwCBQoSFirewallAction_Type())
hwCBQoSFirewallAction.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSFirewallAction.setStatus(_A)
_HwCBQoSFirewallRowStatus_Type=RowStatus
_HwCBQoSFirewallRowStatus_Object=MibTableColumn
hwCBQoSFirewallRowStatus=_HwCBQoSFirewallRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,11,1,2),_HwCBQoSFirewallRowStatus_Type())
hwCBQoSFirewallRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSFirewallRowStatus.setStatus(_A)
_HwCBQoSSamplingCfgInfoTable_Object=MibTable
hwCBQoSSamplingCfgInfoTable=_HwCBQoSSamplingCfgInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,12))
if mibBuilder.loadTexts:hwCBQoSSamplingCfgInfoTable.setStatus(_A)
_HwCBQoSSamplingCfgInfoEntry_Object=MibTableRow
hwCBQoSSamplingCfgInfoEntry=_HwCBQoSSamplingCfgInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,12,1))
hwCBQoSSamplingCfgInfoEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:hwCBQoSSamplingCfgInfoEntry.setStatus(_A)
class _HwCBQoSSamplingNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HwCBQoSSamplingNum_Type.__name__=_E
_HwCBQoSSamplingNum_Object=MibTableColumn
hwCBQoSSamplingNum=_HwCBQoSSamplingNum_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,12,1,1),_HwCBQoSSamplingNum_Type())
hwCBQoSSamplingNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSSamplingNum.setStatus(_A)
_HwCBQoSSamplingRowStatus_Type=RowStatus
_HwCBQoSSamplingRowStatus_Object=MibTableColumn
hwCBQoSSamplingRowStatus=_HwCBQoSSamplingRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,12,1,2),_HwCBQoSSamplingRowStatus_Type())
hwCBQoSSamplingRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSSamplingRowStatus.setStatus(_A)
_HwCBQoSLrCfgInfoTable_Object=MibTable
hwCBQoSLrCfgInfoTable=_HwCBQoSLrCfgInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,13))
if mibBuilder.loadTexts:hwCBQoSLrCfgInfoTable.setStatus(_A)
_HwCBQoSLrCfgInfoEntry_Object=MibTableRow
hwCBQoSLrCfgInfoEntry=_HwCBQoSLrCfgInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,13,1))
hwCBQoSLrCfgInfoEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:hwCBQoSLrCfgInfoEntry.setStatus(_A)
_HwCBQoSLrUnit_Type=LrCirUnit
_HwCBQoSLrUnit_Object=MibTableColumn
hwCBQoSLrUnit=_HwCBQoSLrUnit_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,13,1,1),_HwCBQoSLrUnit_Type())
hwCBQoSLrUnit.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSLrUnit.setStatus(_A)
class _HwCBQoSLrCir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000000000))
_HwCBQoSLrCir_Type.__name__=_E
_HwCBQoSLrCir_Object=MibTableColumn
hwCBQoSLrCir=_HwCBQoSLrCir_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,13,1,2),_HwCBQoSLrCir_Type())
hwCBQoSLrCir.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSLrCir.setStatus(_A)
class _HwCBQoSLrCbs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,1000000000))
_HwCBQoSLrCbs_Type.__name__=_E
_HwCBQoSLrCbs_Object=MibTableColumn
hwCBQoSLrCbs=_HwCBQoSLrCbs_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,13,1,3),_HwCBQoSLrCbs_Type())
hwCBQoSLrCbs.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSLrCbs.setStatus(_A)
class _HwCBQoSLrEbs_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000000))
_HwCBQoSLrEbs_Type.__name__=_E
_HwCBQoSLrEbs_Object=MibTableColumn
hwCBQoSLrEbs=_HwCBQoSLrEbs_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,13,1,4),_HwCBQoSLrEbs_Type())
hwCBQoSLrEbs.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSLrEbs.setStatus(_A)
_HwCBQoSLrRowStatus_Type=RowStatus
_HwCBQoSLrRowStatus_Object=MibTableColumn
hwCBQoSLrRowStatus=_HwCBQoSLrRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,13,1,5),_HwCBQoSLrRowStatus_Type())
hwCBQoSLrRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSLrRowStatus.setStatus(_A)
_HwCBQoSNestPolicyCfgInfoTable_Object=MibTable
hwCBQoSNestPolicyCfgInfoTable=_HwCBQoSNestPolicyCfgInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,14))
if mibBuilder.loadTexts:hwCBQoSNestPolicyCfgInfoTable.setStatus(_A)
_HwCBQoSNestPolicyCfgInfoEntry_Object=MibTableRow
hwCBQoSNestPolicyCfgInfoEntry=_HwCBQoSNestPolicyCfgInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,14,1))
hwCBQoSNestPolicyCfgInfoEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:hwCBQoSNestPolicyCfgInfoEntry.setStatus(_A)
class _HwCBQoSNestPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HwCBQoSNestPolicyName_Type.__name__=_H
_HwCBQoSNestPolicyName_Object=MibTableColumn
hwCBQoSNestPolicyName=_HwCBQoSNestPolicyName_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,14,1,1),_HwCBQoSNestPolicyName_Type())
hwCBQoSNestPolicyName.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSNestPolicyName.setStatus(_A)
_HwCBQoSNestPolicyRowStatus_Type=RowStatus
_HwCBQoSNestPolicyRowStatus_Object=MibTableColumn
hwCBQoSNestPolicyRowStatus=_HwCBQoSNestPolicyRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,2,14,1,2),_HwCBQoSNestPolicyRowStatus_Type())
hwCBQoSNestPolicyRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSNestPolicyRowStatus.setStatus(_A)
_HwCBQoSPolicyObjects_ObjectIdentity=ObjectIdentity
hwCBQoSPolicyObjects=_HwCBQoSPolicyObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,32,1,1,3))
_HwCBQoSPolicyIndexNext_Type=Integer32
_HwCBQoSPolicyIndexNext_Object=MibScalar
hwCBQoSPolicyIndexNext=_HwCBQoSPolicyIndexNext_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,3,1),_HwCBQoSPolicyIndexNext_Type())
hwCBQoSPolicyIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSPolicyIndexNext.setStatus(_A)
_HwCBQoSPolicyCfgInfoTable_Object=MibTable
hwCBQoSPolicyCfgInfoTable=_HwCBQoSPolicyCfgInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,3,2))
if mibBuilder.loadTexts:hwCBQoSPolicyCfgInfoTable.setStatus(_A)
_HwCBQoSPolicyCfgInfoEntry_Object=MibTableRow
hwCBQoSPolicyCfgInfoEntry=_HwCBQoSPolicyCfgInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,3,2,1))
hwCBQoSPolicyCfgInfoEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:hwCBQoSPolicyCfgInfoEntry.setStatus(_A)
_HwCBQoSPolicyIndex_Type=Integer32
_HwCBQoSPolicyIndex_Object=MibTableColumn
hwCBQoSPolicyIndex=_HwCBQoSPolicyIndex_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,3,2,1,1),_HwCBQoSPolicyIndex_Type())
hwCBQoSPolicyIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hwCBQoSPolicyIndex.setStatus(_A)
class _HwCBQoSPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HwCBQoSPolicyName_Type.__name__=_H
_HwCBQoSPolicyName_Object=MibTableColumn
hwCBQoSPolicyName=_HwCBQoSPolicyName_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,3,2,1,2),_HwCBQoSPolicyName_Type())
hwCBQoSPolicyName.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSPolicyName.setStatus(_A)
_HwCBQoSPolicyClassCount_Type=Integer32
_HwCBQoSPolicyClassCount_Object=MibTableColumn
hwCBQoSPolicyClassCount=_HwCBQoSPolicyClassCount_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,3,2,1,3),_HwCBQoSPolicyClassCount_Type())
hwCBQoSPolicyClassCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSPolicyClassCount.setStatus(_A)
class _HwCBQoSPolicyConfigMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_S,-1),('config',1),('auto',2)))
_HwCBQoSPolicyConfigMode_Type.__name__=_E
_HwCBQoSPolicyConfigMode_Object=MibTableColumn
hwCBQoSPolicyConfigMode=_HwCBQoSPolicyConfigMode_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,3,2,1,4),_HwCBQoSPolicyConfigMode_Type())
hwCBQoSPolicyConfigMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSPolicyConfigMode.setStatus(_A)
_HwCBQoSPolicyRowStatus_Type=RowStatus
_HwCBQoSPolicyRowStatus_Object=MibTableColumn
hwCBQoSPolicyRowStatus=_HwCBQoSPolicyRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,3,2,1,5),_HwCBQoSPolicyRowStatus_Type())
hwCBQoSPolicyRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSPolicyRowStatus.setStatus(_A)
_HwCBQoSPolicyClassCfgInfoTable_Object=MibTable
hwCBQoSPolicyClassCfgInfoTable=_HwCBQoSPolicyClassCfgInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,3,3))
if mibBuilder.loadTexts:hwCBQoSPolicyClassCfgInfoTable.setStatus(_A)
_HwCBQoSPolicyClassCfgInfoEntry_Object=MibTableRow
hwCBQoSPolicyClassCfgInfoEntry=_HwCBQoSPolicyClassCfgInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,3,3,1))
hwCBQoSPolicyClassCfgInfoEntry.setIndexNames((0,_B,_X),(0,_B,_F))
if mibBuilder.loadTexts:hwCBQoSPolicyClassCfgInfoEntry.setStatus(_A)
_HwCBQoSPolicyClassIndex_Type=Integer32
_HwCBQoSPolicyClassIndex_Object=MibTableColumn
hwCBQoSPolicyClassIndex=_HwCBQoSPolicyClassIndex_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,3,3,1,1),_HwCBQoSPolicyClassIndex_Type())
hwCBQoSPolicyClassIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hwCBQoSPolicyClassIndex.setStatus(_A)
_HwCBQoSPolicyClassClassifierIndex_Type=Integer32
_HwCBQoSPolicyClassClassifierIndex_Object=MibTableColumn
hwCBQoSPolicyClassClassifierIndex=_HwCBQoSPolicyClassClassifierIndex_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,3,3,1,2),_HwCBQoSPolicyClassClassifierIndex_Type())
hwCBQoSPolicyClassClassifierIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSPolicyClassClassifierIndex.setStatus(_A)
class _HwCBQoSPolicyClassClassifierName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HwCBQoSPolicyClassClassifierName_Type.__name__=_H
_HwCBQoSPolicyClassClassifierName_Object=MibTableColumn
hwCBQoSPolicyClassClassifierName=_HwCBQoSPolicyClassClassifierName_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,3,3,1,3),_HwCBQoSPolicyClassClassifierName_Type())
hwCBQoSPolicyClassClassifierName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSPolicyClassClassifierName.setStatus(_A)
_HwCBQoSPolicyClassBehaviorIndex_Type=Integer32
_HwCBQoSPolicyClassBehaviorIndex_Object=MibTableColumn
hwCBQoSPolicyClassBehaviorIndex=_HwCBQoSPolicyClassBehaviorIndex_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,3,3,1,4),_HwCBQoSPolicyClassBehaviorIndex_Type())
hwCBQoSPolicyClassBehaviorIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSPolicyClassBehaviorIndex.setStatus(_A)
class _HwCBQoSPolicyClassBehaviorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HwCBQoSPolicyClassBehaviorName_Type.__name__=_H
_HwCBQoSPolicyClassBehaviorName_Object=MibTableColumn
hwCBQoSPolicyClassBehaviorName=_HwCBQoSPolicyClassBehaviorName_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,3,3,1,5),_HwCBQoSPolicyClassBehaviorName_Type())
hwCBQoSPolicyClassBehaviorName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSPolicyClassBehaviorName.setStatus(_A)
class _HwCBQoSPolicyClassPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,16383))
_HwCBQoSPolicyClassPrecedence_Type.__name__=_E
_HwCBQoSPolicyClassPrecedence_Object=MibTableColumn
hwCBQoSPolicyClassPrecedence=_HwCBQoSPolicyClassPrecedence_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,3,3,1,6),_HwCBQoSPolicyClassPrecedence_Type())
hwCBQoSPolicyClassPrecedence.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSPolicyClassPrecedence.setStatus(_A)
_HwCBQoSPolicyClassRowStatus_Type=RowStatus
_HwCBQoSPolicyClassRowStatus_Object=MibTableColumn
hwCBQoSPolicyClassRowStatus=_HwCBQoSPolicyClassRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,3,3,1,7),_HwCBQoSPolicyClassRowStatus_Type())
hwCBQoSPolicyClassRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSPolicyClassRowStatus.setStatus(_A)
_HwCBQoSApplyPolicyObjects_ObjectIdentity=ObjectIdentity
hwCBQoSApplyPolicyObjects=_HwCBQoSApplyPolicyObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4))
_HwCBQoSIfApplyPolicyTable_Object=MibTable
hwCBQoSIfApplyPolicyTable=_HwCBQoSIfApplyPolicyTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,1))
if mibBuilder.loadTexts:hwCBQoSIfApplyPolicyTable.setStatus(_A)
_HwCBQoSIfApplyPolicyEntry_Object=MibTableRow
hwCBQoSIfApplyPolicyEntry=_HwCBQoSIfApplyPolicyEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,1,1))
hwCBQoSIfApplyPolicyEntry.setIndexNames((0,_B,_J),(0,_B,_P))
if mibBuilder.loadTexts:hwCBQoSIfApplyPolicyEntry.setStatus(_A)
_HwCBQoSIfApplyPolicyIfIndex_Type=Integer32
_HwCBQoSIfApplyPolicyIfIndex_Object=MibTableColumn
hwCBQoSIfApplyPolicyIfIndex=_HwCBQoSIfApplyPolicyIfIndex_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,1,1,1),_HwCBQoSIfApplyPolicyIfIndex_Type())
hwCBQoSIfApplyPolicyIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hwCBQoSIfApplyPolicyIfIndex.setStatus(_A)
_HwCBQoSIfApplyPolicyDirection_Type=DirectionType
_HwCBQoSIfApplyPolicyDirection_Object=MibTableColumn
hwCBQoSIfApplyPolicyDirection=_HwCBQoSIfApplyPolicyDirection_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,1,1,2),_HwCBQoSIfApplyPolicyDirection_Type())
hwCBQoSIfApplyPolicyDirection.setMaxAccess(_G)
if mibBuilder.loadTexts:hwCBQoSIfApplyPolicyDirection.setStatus(_A)
class _HwCBQoSIfApplyPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HwCBQoSIfApplyPolicyName_Type.__name__=_H
_HwCBQoSIfApplyPolicyName_Object=MibTableColumn
hwCBQoSIfApplyPolicyName=_HwCBQoSIfApplyPolicyName_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,1,1,3),_HwCBQoSIfApplyPolicyName_Type())
hwCBQoSIfApplyPolicyName.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSIfApplyPolicyName.setStatus(_A)
class _HwCBQoSIfApplyPolicyEnableDynamic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(-1,1,2)));namedValues=NamedValues(*((_S,-1),('true',1),('false',2)))
_HwCBQoSIfApplyPolicyEnableDynamic_Type.__name__=_E
_HwCBQoSIfApplyPolicyEnableDynamic_Object=MibTableColumn
hwCBQoSIfApplyPolicyEnableDynamic=_HwCBQoSIfApplyPolicyEnableDynamic_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,1,1,4),_HwCBQoSIfApplyPolicyEnableDynamic_Type())
hwCBQoSIfApplyPolicyEnableDynamic.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSIfApplyPolicyEnableDynamic.setStatus(_A)
_HwCBQoSIfApplyPolicyRowStatus_Type=RowStatus
_HwCBQoSIfApplyPolicyRowStatus_Object=MibTableColumn
hwCBQoSIfApplyPolicyRowStatus=_HwCBQoSIfApplyPolicyRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,1,1,5),_HwCBQoSIfApplyPolicyRowStatus_Type())
hwCBQoSIfApplyPolicyRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSIfApplyPolicyRowStatus.setStatus(_A)
_HwCBQoSAtmPvcApplyPolicyTable_Object=MibTable
hwCBQoSAtmPvcApplyPolicyTable=_HwCBQoSAtmPvcApplyPolicyTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,2))
if mibBuilder.loadTexts:hwCBQoSAtmPvcApplyPolicyTable.setStatus(_A)
_HwCBQoSAtmPvcApplyPolicyEntry_Object=MibTableRow
hwCBQoSAtmPvcApplyPolicyEntry=_HwCBQoSAtmPvcApplyPolicyEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,2,1))
hwCBQoSAtmPvcApplyPolicyEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_Q))
if mibBuilder.loadTexts:hwCBQoSAtmPvcApplyPolicyEntry.setStatus(_A)
_HwCBQoSAtmPvcApplyPolicyIfIndex_Type=Integer32
_HwCBQoSAtmPvcApplyPolicyIfIndex_Object=MibTableColumn
hwCBQoSAtmPvcApplyPolicyIfIndex=_HwCBQoSAtmPvcApplyPolicyIfIndex_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,2,1,1),_HwCBQoSAtmPvcApplyPolicyIfIndex_Type())
hwCBQoSAtmPvcApplyPolicyIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hwCBQoSAtmPvcApplyPolicyIfIndex.setStatus(_A)
_HwCBQoSAtmPvcApplyPolicyVPI_Type=Integer32
_HwCBQoSAtmPvcApplyPolicyVPI_Object=MibTableColumn
hwCBQoSAtmPvcApplyPolicyVPI=_HwCBQoSAtmPvcApplyPolicyVPI_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,2,1,2),_HwCBQoSAtmPvcApplyPolicyVPI_Type())
hwCBQoSAtmPvcApplyPolicyVPI.setMaxAccess(_G)
if mibBuilder.loadTexts:hwCBQoSAtmPvcApplyPolicyVPI.setStatus(_A)
_HwCBQoSAtmPvcApplyPolicyVCI_Type=Integer32
_HwCBQoSAtmPvcApplyPolicyVCI_Object=MibTableColumn
hwCBQoSAtmPvcApplyPolicyVCI=_HwCBQoSAtmPvcApplyPolicyVCI_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,2,1,3),_HwCBQoSAtmPvcApplyPolicyVCI_Type())
hwCBQoSAtmPvcApplyPolicyVCI.setMaxAccess(_G)
if mibBuilder.loadTexts:hwCBQoSAtmPvcApplyPolicyVCI.setStatus(_A)
_HwCBQoSAtmPvcApplyPolicyDirection_Type=DirectionType
_HwCBQoSAtmPvcApplyPolicyDirection_Object=MibTableColumn
hwCBQoSAtmPvcApplyPolicyDirection=_HwCBQoSAtmPvcApplyPolicyDirection_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,2,1,4),_HwCBQoSAtmPvcApplyPolicyDirection_Type())
hwCBQoSAtmPvcApplyPolicyDirection.setMaxAccess(_G)
if mibBuilder.loadTexts:hwCBQoSAtmPvcApplyPolicyDirection.setStatus(_A)
class _HwCBQoSAtmPvcApplyPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HwCBQoSAtmPvcApplyPolicyName_Type.__name__=_H
_HwCBQoSAtmPvcApplyPolicyName_Object=MibTableColumn
hwCBQoSAtmPvcApplyPolicyName=_HwCBQoSAtmPvcApplyPolicyName_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,2,1,5),_HwCBQoSAtmPvcApplyPolicyName_Type())
hwCBQoSAtmPvcApplyPolicyName.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSAtmPvcApplyPolicyName.setStatus(_A)
_HwCBQoSAtmPvcApplyPolicyRowStatus_Type=RowStatus
_HwCBQoSAtmPvcApplyPolicyRowStatus_Object=MibTableColumn
hwCBQoSAtmPvcApplyPolicyRowStatus=_HwCBQoSAtmPvcApplyPolicyRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,2,1,6),_HwCBQoSAtmPvcApplyPolicyRowStatus_Type())
hwCBQoSAtmPvcApplyPolicyRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSAtmPvcApplyPolicyRowStatus.setStatus(_A)
_HwCBQoSIfVlanApplyPolicyTable_Object=MibTable
hwCBQoSIfVlanApplyPolicyTable=_HwCBQoSIfVlanApplyPolicyTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,3))
if mibBuilder.loadTexts:hwCBQoSIfVlanApplyPolicyTable.setStatus(_A)
_HwCBQoSIfVlanApplyPolicyEntry_Object=MibTableRow
hwCBQoSIfVlanApplyPolicyEntry=_HwCBQoSIfVlanApplyPolicyEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,3,1))
hwCBQoSIfVlanApplyPolicyEntry.setIndexNames((0,_B,_Y),(0,_B,_Z),(0,_B,_a))
if mibBuilder.loadTexts:hwCBQoSIfVlanApplyPolicyEntry.setStatus(_A)
_HwCBQoSIfVlanApplyPolicyIfIndex_Type=Integer32
_HwCBQoSIfVlanApplyPolicyIfIndex_Object=MibTableColumn
hwCBQoSIfVlanApplyPolicyIfIndex=_HwCBQoSIfVlanApplyPolicyIfIndex_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,3,1,1),_HwCBQoSIfVlanApplyPolicyIfIndex_Type())
hwCBQoSIfVlanApplyPolicyIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hwCBQoSIfVlanApplyPolicyIfIndex.setStatus(_A)
_HwCBQoSIfVlanApplyPolicyVlanid_Type=Integer32
_HwCBQoSIfVlanApplyPolicyVlanid_Object=MibTableColumn
hwCBQoSIfVlanApplyPolicyVlanid=_HwCBQoSIfVlanApplyPolicyVlanid_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,3,1,2),_HwCBQoSIfVlanApplyPolicyVlanid_Type())
hwCBQoSIfVlanApplyPolicyVlanid.setMaxAccess(_G)
if mibBuilder.loadTexts:hwCBQoSIfVlanApplyPolicyVlanid.setStatus(_A)
_HwCBQoSIfVlanApplyPolicyDirection_Type=DirectionType
_HwCBQoSIfVlanApplyPolicyDirection_Object=MibTableColumn
hwCBQoSIfVlanApplyPolicyDirection=_HwCBQoSIfVlanApplyPolicyDirection_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,3,1,3),_HwCBQoSIfVlanApplyPolicyDirection_Type())
hwCBQoSIfVlanApplyPolicyDirection.setMaxAccess(_G)
if mibBuilder.loadTexts:hwCBQoSIfVlanApplyPolicyDirection.setStatus(_A)
class _HwCBQoSIfVlanApplyPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HwCBQoSIfVlanApplyPolicyName_Type.__name__=_H
_HwCBQoSIfVlanApplyPolicyName_Object=MibTableColumn
hwCBQoSIfVlanApplyPolicyName=_HwCBQoSIfVlanApplyPolicyName_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,3,1,4),_HwCBQoSIfVlanApplyPolicyName_Type())
hwCBQoSIfVlanApplyPolicyName.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSIfVlanApplyPolicyName.setStatus(_A)
_HwCBQoSIfVlanApplyPolicyRowStatus_Type=RowStatus
_HwCBQoSIfVlanApplyPolicyRowStatus_Object=MibTableColumn
hwCBQoSIfVlanApplyPolicyRowStatus=_HwCBQoSIfVlanApplyPolicyRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,3,1,5),_HwCBQoSIfVlanApplyPolicyRowStatus_Type())
hwCBQoSIfVlanApplyPolicyRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSIfVlanApplyPolicyRowStatus.setStatus(_A)
_HwCBQoSFrClassApplyPolicyTable_Object=MibTable
hwCBQoSFrClassApplyPolicyTable=_HwCBQoSFrClassApplyPolicyTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,4))
if mibBuilder.loadTexts:hwCBQoSFrClassApplyPolicyTable.setStatus(_A)
_HwCBQoSFrClassApplyPolicyEntry_Object=MibTableRow
hwCBQoSFrClassApplyPolicyEntry=_HwCBQoSFrClassApplyPolicyEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,4,1))
hwCBQoSFrClassApplyPolicyEntry.setIndexNames((0,_B,_n),(0,_B,_o))
if mibBuilder.loadTexts:hwCBQoSFrClassApplyPolicyEntry.setStatus(_A)
class _HwCBQoSFrClassApplyPolicyFrClassName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HwCBQoSFrClassApplyPolicyFrClassName_Type.__name__=_H
_HwCBQoSFrClassApplyPolicyFrClassName_Object=MibTableColumn
hwCBQoSFrClassApplyPolicyFrClassName=_HwCBQoSFrClassApplyPolicyFrClassName_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,4,1,1),_HwCBQoSFrClassApplyPolicyFrClassName_Type())
hwCBQoSFrClassApplyPolicyFrClassName.setMaxAccess(_G)
if mibBuilder.loadTexts:hwCBQoSFrClassApplyPolicyFrClassName.setStatus(_A)
_HwCBQoSFrClassApplyPolicyDirection_Type=DirectionType
_HwCBQoSFrClassApplyPolicyDirection_Object=MibTableColumn
hwCBQoSFrClassApplyPolicyDirection=_HwCBQoSFrClassApplyPolicyDirection_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,4,1,2),_HwCBQoSFrClassApplyPolicyDirection_Type())
hwCBQoSFrClassApplyPolicyDirection.setMaxAccess(_G)
if mibBuilder.loadTexts:hwCBQoSFrClassApplyPolicyDirection.setStatus(_A)
class _HwCBQoSFrClassApplyPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HwCBQoSFrClassApplyPolicyName_Type.__name__=_H
_HwCBQoSFrClassApplyPolicyName_Object=MibTableColumn
hwCBQoSFrClassApplyPolicyName=_HwCBQoSFrClassApplyPolicyName_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,4,1,3),_HwCBQoSFrClassApplyPolicyName_Type())
hwCBQoSFrClassApplyPolicyName.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSFrClassApplyPolicyName.setStatus(_A)
_HwCBQoSFrClassApplyPolicyRowStatus_Type=RowStatus
_HwCBQoSFrClassApplyPolicyRowStatus_Object=MibTableColumn
hwCBQoSFrClassApplyPolicyRowStatus=_HwCBQoSFrClassApplyPolicyRowStatus_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,4,1,4),_HwCBQoSFrClassApplyPolicyRowStatus_Type())
hwCBQoSFrClassApplyPolicyRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hwCBQoSFrClassApplyPolicyRowStatus.setStatus(_A)
_HwCBQoSFrPvcApplyPolicyTable_Object=MibTable
hwCBQoSFrPvcApplyPolicyTable=_HwCBQoSFrPvcApplyPolicyTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,5))
if mibBuilder.loadTexts:hwCBQoSFrPvcApplyPolicyTable.setStatus(_A)
_HwCBQoSFrPvcApplyPolicyEntry_Object=MibTableRow
hwCBQoSFrPvcApplyPolicyEntry=_HwCBQoSFrPvcApplyPolicyEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,5,1))
hwCBQoSFrPvcApplyPolicyEntry.setIndexNames((0,_B,_N),(0,_B,_O),(0,_B,_R))
if mibBuilder.loadTexts:hwCBQoSFrPvcApplyPolicyEntry.setStatus(_A)
_HwCBQoSFrPvcApplyPolicyIfIndex_Type=Integer32
_HwCBQoSFrPvcApplyPolicyIfIndex_Object=MibTableColumn
hwCBQoSFrPvcApplyPolicyIfIndex=_HwCBQoSFrPvcApplyPolicyIfIndex_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,5,1,1),_HwCBQoSFrPvcApplyPolicyIfIndex_Type())
hwCBQoSFrPvcApplyPolicyIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hwCBQoSFrPvcApplyPolicyIfIndex.setStatus(_A)
class _HwCBQoSFrPvcApplyPolicyDlciNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1007))
_HwCBQoSFrPvcApplyPolicyDlciNum_Type.__name__=_E
_HwCBQoSFrPvcApplyPolicyDlciNum_Object=MibTableColumn
hwCBQoSFrPvcApplyPolicyDlciNum=_HwCBQoSFrPvcApplyPolicyDlciNum_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,5,1,2),_HwCBQoSFrPvcApplyPolicyDlciNum_Type())
hwCBQoSFrPvcApplyPolicyDlciNum.setMaxAccess(_G)
if mibBuilder.loadTexts:hwCBQoSFrPvcApplyPolicyDlciNum.setStatus(_A)
_HwCBQoSFrPvcApplyPolicyDirection_Type=DirectionType
_HwCBQoSFrPvcApplyPolicyDirection_Object=MibTableColumn
hwCBQoSFrPvcApplyPolicyDirection=_HwCBQoSFrPvcApplyPolicyDirection_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,5,1,3),_HwCBQoSFrPvcApplyPolicyDirection_Type())
hwCBQoSFrPvcApplyPolicyDirection.setMaxAccess(_G)
if mibBuilder.loadTexts:hwCBQoSFrPvcApplyPolicyDirection.setStatus(_A)
class _HwCBQoSFrPvcApplyPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HwCBQoSFrPvcApplyPolicyName_Type.__name__=_H
_HwCBQoSFrPvcApplyPolicyName_Object=MibTableColumn
hwCBQoSFrPvcApplyPolicyName=_HwCBQoSFrPvcApplyPolicyName_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,4,5,1,4),_HwCBQoSFrPvcApplyPolicyName_Type())
hwCBQoSFrPvcApplyPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcApplyPolicyName.setStatus(_A)
_HwCBQoSApplyPolicyStaticsObjects_ObjectIdentity=ObjectIdentity
hwCBQoSApplyPolicyStaticsObjects=_HwCBQoSApplyPolicyStaticsObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5))
_HwCBQoSIfStaticsObjects_ObjectIdentity=ObjectIdentity
hwCBQoSIfStaticsObjects=_HwCBQoSIfStaticsObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1))
_HwCBQoSIfCbqRunInfoTable_Object=MibTable
hwCBQoSIfCbqRunInfoTable=_HwCBQoSIfCbqRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,1))
if mibBuilder.loadTexts:hwCBQoSIfCbqRunInfoTable.setStatus(_A)
_HwCBQoSIfCbqRunInfoEntry_Object=MibTableRow
hwCBQoSIfCbqRunInfoEntry=_HwCBQoSIfCbqRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,1,1))
hwCBQoSIfCbqRunInfoEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:hwCBQoSIfCbqRunInfoEntry.setStatus(_A)
_HwCBQoSIfCbqQueueSize_Type=Integer32
_HwCBQoSIfCbqQueueSize_Object=MibTableColumn
hwCBQoSIfCbqQueueSize=_HwCBQoSIfCbqQueueSize_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,1,1,1),_HwCBQoSIfCbqQueueSize_Type())
hwCBQoSIfCbqQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfCbqQueueSize.setStatus(_A)
_HwCBQoSIfCbqDiscard_Type=Counter32
_HwCBQoSIfCbqDiscard_Object=MibTableColumn
hwCBQoSIfCbqDiscard=_HwCBQoSIfCbqDiscard_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,1,1,2),_HwCBQoSIfCbqDiscard_Type())
hwCBQoSIfCbqDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfCbqDiscard.setStatus(_A)
_HwCBQoSIfCbqEfQueueSize_Type=Integer32
_HwCBQoSIfCbqEfQueueSize_Object=MibTableColumn
hwCBQoSIfCbqEfQueueSize=_HwCBQoSIfCbqEfQueueSize_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,1,1,3),_HwCBQoSIfCbqEfQueueSize_Type())
hwCBQoSIfCbqEfQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfCbqEfQueueSize.setStatus(_A)
_HwCBQoSIfCbqAfQueueSize_Type=Integer32
_HwCBQoSIfCbqAfQueueSize_Object=MibTableColumn
hwCBQoSIfCbqAfQueueSize=_HwCBQoSIfCbqAfQueueSize_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,1,1,4),_HwCBQoSIfCbqAfQueueSize_Type())
hwCBQoSIfCbqAfQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfCbqAfQueueSize.setStatus(_A)
_HwCBQoSIfCbqBeQueueSize_Type=Integer32
_HwCBQoSIfCbqBeQueueSize_Object=MibTableColumn
hwCBQoSIfCbqBeQueueSize=_HwCBQoSIfCbqBeQueueSize_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,1,1,5),_HwCBQoSIfCbqBeQueueSize_Type())
hwCBQoSIfCbqBeQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfCbqBeQueueSize.setStatus(_A)
_HwCBQoSIfCbqBeActiveQueueNum_Type=Integer32
_HwCBQoSIfCbqBeActiveQueueNum_Object=MibTableColumn
hwCBQoSIfCbqBeActiveQueueNum=_HwCBQoSIfCbqBeActiveQueueNum_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,1,1,6),_HwCBQoSIfCbqBeActiveQueueNum_Type())
hwCBQoSIfCbqBeActiveQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfCbqBeActiveQueueNum.setStatus(_A)
_HwCBQoSIfCbqBeMaxActiveQueueNum_Type=Integer32
_HwCBQoSIfCbqBeMaxActiveQueueNum_Object=MibTableColumn
hwCBQoSIfCbqBeMaxActiveQueueNum=_HwCBQoSIfCbqBeMaxActiveQueueNum_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,1,1,7),_HwCBQoSIfCbqBeMaxActiveQueueNum_Type())
hwCBQoSIfCbqBeMaxActiveQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfCbqBeMaxActiveQueueNum.setStatus(_A)
_HwCBQoSIfCbqBeTotalQueueNum_Type=Integer32
_HwCBQoSIfCbqBeTotalQueueNum_Object=MibTableColumn
hwCBQoSIfCbqBeTotalQueueNum=_HwCBQoSIfCbqBeTotalQueueNum_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,1,1,8),_HwCBQoSIfCbqBeTotalQueueNum_Type())
hwCBQoSIfCbqBeTotalQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfCbqBeTotalQueueNum.setStatus(_A)
_HwCBQoSIfCbqAfAllocatedQueueNum_Type=Integer32
_HwCBQoSIfCbqAfAllocatedQueueNum_Object=MibTableColumn
hwCBQoSIfCbqAfAllocatedQueueNum=_HwCBQoSIfCbqAfAllocatedQueueNum_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,1,1,9),_HwCBQoSIfCbqAfAllocatedQueueNum_Type())
hwCBQoSIfCbqAfAllocatedQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfCbqAfAllocatedQueueNum.setStatus(_A)
_HwCBQoSIfClassMatchRunInfoTable_Object=MibTable
hwCBQoSIfClassMatchRunInfoTable=_HwCBQoSIfClassMatchRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,2))
if mibBuilder.loadTexts:hwCBQoSIfClassMatchRunInfoTable.setStatus(_A)
_HwCBQoSIfClassMatchRunInfoEntry_Object=MibTableRow
hwCBQoSIfClassMatchRunInfoEntry=_HwCBQoSIfClassMatchRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,2,1))
hwCBQoSIfClassMatchRunInfoEntry.setIndexNames((0,_B,_J),(0,_B,_P),(0,_B,_F))
if mibBuilder.loadTexts:hwCBQoSIfClassMatchRunInfoEntry.setStatus(_A)
_HwCBQoSIfClassMatchedPackets_Type=Counter32
_HwCBQoSIfClassMatchedPackets_Object=MibTableColumn
hwCBQoSIfClassMatchedPackets=_HwCBQoSIfClassMatchedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,2,1,1),_HwCBQoSIfClassMatchedPackets_Type())
hwCBQoSIfClassMatchedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfClassMatchedPackets.setStatus(_A)
_HwCBQoSIfClassMatchedBytes_Type=Counter32
_HwCBQoSIfClassMatchedBytes_Object=MibTableColumn
hwCBQoSIfClassMatchedBytes=_HwCBQoSIfClassMatchedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,2,1,2),_HwCBQoSIfClassMatchedBytes_Type())
hwCBQoSIfClassMatchedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfClassMatchedBytes.setStatus(_A)
_HwCBQoSIfClassAverageRate_Type=Counter64
_HwCBQoSIfClassAverageRate_Object=MibTableColumn
hwCBQoSIfClassAverageRate=_HwCBQoSIfClassAverageRate_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,2,1,3),_HwCBQoSIfClassAverageRate_Type())
hwCBQoSIfClassAverageRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfClassAverageRate.setStatus(_A)
_HwCBQoSIfCarRunInfoTable_Object=MibTable
hwCBQoSIfCarRunInfoTable=_HwCBQoSIfCarRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,3))
if mibBuilder.loadTexts:hwCBQoSIfCarRunInfoTable.setStatus(_A)
_HwCBQoSIfCarRunInfoEntry_Object=MibTableRow
hwCBQoSIfCarRunInfoEntry=_HwCBQoSIfCarRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,3,1))
hwCBQoSIfCarRunInfoEntry.setIndexNames((0,_B,_J),(0,_B,_P),(0,_B,_F))
if mibBuilder.loadTexts:hwCBQoSIfCarRunInfoEntry.setStatus(_A)
_HwCBQoSIfCarGreenPackets_Type=Counter32
_HwCBQoSIfCarGreenPackets_Object=MibTableColumn
hwCBQoSIfCarGreenPackets=_HwCBQoSIfCarGreenPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,3,1,1),_HwCBQoSIfCarGreenPackets_Type())
hwCBQoSIfCarGreenPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfCarGreenPackets.setStatus(_A)
_HwCBQoSIfCarGreenBytes_Type=Counter32
_HwCBQoSIfCarGreenBytes_Object=MibTableColumn
hwCBQoSIfCarGreenBytes=_HwCBQoSIfCarGreenBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,3,1,2),_HwCBQoSIfCarGreenBytes_Type())
hwCBQoSIfCarGreenBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfCarGreenBytes.setStatus(_A)
_HwCBQoSIfCarRedPackets_Type=Counter32
_HwCBQoSIfCarRedPackets_Object=MibTableColumn
hwCBQoSIfCarRedPackets=_HwCBQoSIfCarRedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,3,1,3),_HwCBQoSIfCarRedPackets_Type())
hwCBQoSIfCarRedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfCarRedPackets.setStatus(_A)
_HwCBQoSIfCarRedBytes_Type=Counter32
_HwCBQoSIfCarRedBytes_Object=MibTableColumn
hwCBQoSIfCarRedBytes=_HwCBQoSIfCarRedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,3,1,4),_HwCBQoSIfCarRedBytes_Type())
hwCBQoSIfCarRedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfCarRedBytes.setStatus(_A)
_HwCBQoSIfGtsRunInfoTable_Object=MibTable
hwCBQoSIfGtsRunInfoTable=_HwCBQoSIfGtsRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,4))
if mibBuilder.loadTexts:hwCBQoSIfGtsRunInfoTable.setStatus(_A)
_HwCBQoSIfGtsRunInfoEntry_Object=MibTableRow
hwCBQoSIfGtsRunInfoEntry=_HwCBQoSIfGtsRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,4,1))
hwCBQoSIfGtsRunInfoEntry.setIndexNames((0,_B,_J),(0,_B,_P),(0,_B,_F))
if mibBuilder.loadTexts:hwCBQoSIfGtsRunInfoEntry.setStatus(_A)
_HwCBQoSIfGtsPassedPackets_Type=Counter32
_HwCBQoSIfGtsPassedPackets_Object=MibTableColumn
hwCBQoSIfGtsPassedPackets=_HwCBQoSIfGtsPassedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,4,1,1),_HwCBQoSIfGtsPassedPackets_Type())
hwCBQoSIfGtsPassedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfGtsPassedPackets.setStatus(_A)
_HwCBQoSIfGtsPassedBytes_Type=Counter32
_HwCBQoSIfGtsPassedBytes_Object=MibTableColumn
hwCBQoSIfGtsPassedBytes=_HwCBQoSIfGtsPassedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,4,1,2),_HwCBQoSIfGtsPassedBytes_Type())
hwCBQoSIfGtsPassedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfGtsPassedBytes.setStatus(_A)
_HwCBQoSIfGtsDiscardedPackets_Type=Counter32
_HwCBQoSIfGtsDiscardedPackets_Object=MibTableColumn
hwCBQoSIfGtsDiscardedPackets=_HwCBQoSIfGtsDiscardedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,4,1,3),_HwCBQoSIfGtsDiscardedPackets_Type())
hwCBQoSIfGtsDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfGtsDiscardedPackets.setStatus(_A)
_HwCBQoSIfGtsDiscardedBytes_Type=Counter32
_HwCBQoSIfGtsDiscardedBytes_Object=MibTableColumn
hwCBQoSIfGtsDiscardedBytes=_HwCBQoSIfGtsDiscardedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,4,1,4),_HwCBQoSIfGtsDiscardedBytes_Type())
hwCBQoSIfGtsDiscardedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfGtsDiscardedBytes.setStatus(_A)
_HwCBQoSIfGtsDelayedPackets_Type=Counter32
_HwCBQoSIfGtsDelayedPackets_Object=MibTableColumn
hwCBQoSIfGtsDelayedPackets=_HwCBQoSIfGtsDelayedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,4,1,5),_HwCBQoSIfGtsDelayedPackets_Type())
hwCBQoSIfGtsDelayedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfGtsDelayedPackets.setStatus(_A)
_HwCBQoSIfGtsDelayedBytes_Type=Counter32
_HwCBQoSIfGtsDelayedBytes_Object=MibTableColumn
hwCBQoSIfGtsDelayedBytes=_HwCBQoSIfGtsDelayedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,4,1,6),_HwCBQoSIfGtsDelayedBytes_Type())
hwCBQoSIfGtsDelayedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfGtsDelayedBytes.setStatus(_A)
_HwCBQoSIfGtsQueueSize_Type=Integer32
_HwCBQoSIfGtsQueueSize_Object=MibTableColumn
hwCBQoSIfGtsQueueSize=_HwCBQoSIfGtsQueueSize_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,4,1,7),_HwCBQoSIfGtsQueueSize_Type())
hwCBQoSIfGtsQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfGtsQueueSize.setStatus(_A)
_HwCBQoSIfRemarkRunInfoTable_Object=MibTable
hwCBQoSIfRemarkRunInfoTable=_HwCBQoSIfRemarkRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,5))
if mibBuilder.loadTexts:hwCBQoSIfRemarkRunInfoTable.setStatus(_A)
_HwCBQoSIfRemarkRunInfoEntry_Object=MibTableRow
hwCBQoSIfRemarkRunInfoEntry=_HwCBQoSIfRemarkRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,5,1))
hwCBQoSIfRemarkRunInfoEntry.setIndexNames((0,_B,_J),(0,_B,_P),(0,_B,_F))
if mibBuilder.loadTexts:hwCBQoSIfRemarkRunInfoEntry.setStatus(_A)
_HwCBQoSIfRemarkedPackets_Type=Counter32
_HwCBQoSIfRemarkedPackets_Object=MibTableColumn
hwCBQoSIfRemarkedPackets=_HwCBQoSIfRemarkedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,5,1,1),_HwCBQoSIfRemarkedPackets_Type())
hwCBQoSIfRemarkedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfRemarkedPackets.setStatus(_A)
_HwCBQoSIfQueueRunInfoTable_Object=MibTable
hwCBQoSIfQueueRunInfoTable=_HwCBQoSIfQueueRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,6))
if mibBuilder.loadTexts:hwCBQoSIfQueueRunInfoTable.setStatus(_A)
_HwCBQoSIfQueueRunInfoEntry_Object=MibTableRow
hwCBQoSIfQueueRunInfoEntry=_HwCBQoSIfQueueRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,6,1))
hwCBQoSIfQueueRunInfoEntry.setIndexNames((0,_B,_J),(0,_B,_P),(0,_B,_F))
if mibBuilder.loadTexts:hwCBQoSIfQueueRunInfoEntry.setStatus(_A)
_HwCBQoSIfQueueMatchedPackets_Type=Counter32
_HwCBQoSIfQueueMatchedPackets_Object=MibTableColumn
hwCBQoSIfQueueMatchedPackets=_HwCBQoSIfQueueMatchedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,6,1,1),_HwCBQoSIfQueueMatchedPackets_Type())
hwCBQoSIfQueueMatchedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfQueueMatchedPackets.setStatus(_A)
_HwCBQoSIfQueueMatchedBytes_Type=Counter32
_HwCBQoSIfQueueMatchedBytes_Object=MibTableColumn
hwCBQoSIfQueueMatchedBytes=_HwCBQoSIfQueueMatchedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,6,1,2),_HwCBQoSIfQueueMatchedBytes_Type())
hwCBQoSIfQueueMatchedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfQueueMatchedBytes.setStatus(_A)
_HwCBQoSIfQueueEnqueuedPackets_Type=Counter32
_HwCBQoSIfQueueEnqueuedPackets_Object=MibTableColumn
hwCBQoSIfQueueEnqueuedPackets=_HwCBQoSIfQueueEnqueuedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,6,1,3),_HwCBQoSIfQueueEnqueuedPackets_Type())
hwCBQoSIfQueueEnqueuedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfQueueEnqueuedPackets.setStatus(_A)
_HwCBQoSIfQueueEnqueuedBytes_Type=Counter32
_HwCBQoSIfQueueEnqueuedBytes_Object=MibTableColumn
hwCBQoSIfQueueEnqueuedBytes=_HwCBQoSIfQueueEnqueuedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,6,1,4),_HwCBQoSIfQueueEnqueuedBytes_Type())
hwCBQoSIfQueueEnqueuedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfQueueEnqueuedBytes.setStatus(_A)
_HwCBQoSIfQueueDiscardedPackets_Type=Counter32
_HwCBQoSIfQueueDiscardedPackets_Object=MibTableColumn
hwCBQoSIfQueueDiscardedPackets=_HwCBQoSIfQueueDiscardedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,6,1,5),_HwCBQoSIfQueueDiscardedPackets_Type())
hwCBQoSIfQueueDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfQueueDiscardedPackets.setStatus(_A)
_HwCBQoSIfQueueDiscardedBytes_Type=Counter32
_HwCBQoSIfQueueDiscardedBytes_Object=MibTableColumn
hwCBQoSIfQueueDiscardedBytes=_HwCBQoSIfQueueDiscardedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,6,1,6),_HwCBQoSIfQueueDiscardedBytes_Type())
hwCBQoSIfQueueDiscardedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfQueueDiscardedBytes.setStatus(_A)
_HwCBQoSIfWredRunInfoTable_Object=MibTable
hwCBQoSIfWredRunInfoTable=_HwCBQoSIfWredRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,7))
if mibBuilder.loadTexts:hwCBQoSIfWredRunInfoTable.setStatus(_A)
_HwCBQoSIfWredRunInfoEntry_Object=MibTableRow
hwCBQoSIfWredRunInfoEntry=_HwCBQoSIfWredRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,7,1))
hwCBQoSIfWredRunInfoEntry.setIndexNames((0,_B,_J),(0,_B,_P),(0,_B,_F),(0,_B,_U))
if mibBuilder.loadTexts:hwCBQoSIfWredRunInfoEntry.setStatus(_A)
_HwCBQoSIfWredRandomDiscardedPackets_Type=Counter32
_HwCBQoSIfWredRandomDiscardedPackets_Object=MibTableColumn
hwCBQoSIfWredRandomDiscardedPackets=_HwCBQoSIfWredRandomDiscardedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,7,1,1),_HwCBQoSIfWredRandomDiscardedPackets_Type())
hwCBQoSIfWredRandomDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfWredRandomDiscardedPackets.setStatus(_A)
_HwCBQoSIfWredTailDiscardedPackets_Type=Counter32
_HwCBQoSIfWredTailDiscardedPackets_Object=MibTableColumn
hwCBQoSIfWredTailDiscardedPackets=_HwCBQoSIfWredTailDiscardedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,7,1,2),_HwCBQoSIfWredTailDiscardedPackets_Type())
hwCBQoSIfWredTailDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfWredTailDiscardedPackets.setStatus(_A)
_HwCBQoSIfLrRunInfoTable_Object=MibTable
hwCBQoSIfLrRunInfoTable=_HwCBQoSIfLrRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,8))
if mibBuilder.loadTexts:hwCBQoSIfLrRunInfoTable.setStatus(_A)
_HwCBQoSIfLrRunInfoEntry_Object=MibTableRow
hwCBQoSIfLrRunInfoEntry=_HwCBQoSIfLrRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,8,1))
hwCBQoSIfLrRunInfoEntry.setIndexNames((0,_B,_J),(0,_B,_P),(0,_B,_F))
if mibBuilder.loadTexts:hwCBQoSIfLrRunInfoEntry.setStatus(_A)
_HwCBQoSIfLrPassedPackets_Type=Counter32
_HwCBQoSIfLrPassedPackets_Object=MibTableColumn
hwCBQoSIfLrPassedPackets=_HwCBQoSIfLrPassedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,8,1,1),_HwCBQoSIfLrPassedPackets_Type())
hwCBQoSIfLrPassedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfLrPassedPackets.setStatus(_A)
_HwCBQoSIfLrPassedBytes_Type=Counter32
_HwCBQoSIfLrPassedBytes_Object=MibTableColumn
hwCBQoSIfLrPassedBytes=_HwCBQoSIfLrPassedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,8,1,2),_HwCBQoSIfLrPassedBytes_Type())
hwCBQoSIfLrPassedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfLrPassedBytes.setStatus(_A)
_HwCBQoSIfLrDiscardedPackets_Type=Counter32
_HwCBQoSIfLrDiscardedPackets_Object=MibTableColumn
hwCBQoSIfLrDiscardedPackets=_HwCBQoSIfLrDiscardedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,8,1,3),_HwCBQoSIfLrDiscardedPackets_Type())
hwCBQoSIfLrDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfLrDiscardedPackets.setStatus(_A)
_HwCBQoSIfLrDiscardedBytes_Type=Counter32
_HwCBQoSIfLrDiscardedBytes_Object=MibTableColumn
hwCBQoSIfLrDiscardedBytes=_HwCBQoSIfLrDiscardedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,8,1,4),_HwCBQoSIfLrDiscardedBytes_Type())
hwCBQoSIfLrDiscardedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfLrDiscardedBytes.setStatus(_A)
_HwCBQoSIfLrDelayedPackets_Type=Counter32
_HwCBQoSIfLrDelayedPackets_Object=MibTableColumn
hwCBQoSIfLrDelayedPackets=_HwCBQoSIfLrDelayedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,8,1,5),_HwCBQoSIfLrDelayedPackets_Type())
hwCBQoSIfLrDelayedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfLrDelayedPackets.setStatus(_A)
_HwCBQoSIfLrDelayedBytes_Type=Counter32
_HwCBQoSIfLrDelayedBytes_Object=MibTableColumn
hwCBQoSIfLrDelayedBytes=_HwCBQoSIfLrDelayedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,8,1,6),_HwCBQoSIfLrDelayedBytes_Type())
hwCBQoSIfLrDelayedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfLrDelayedBytes.setStatus(_A)
_HwCBQoSIfLrQueueSize_Type=Integer32
_HwCBQoSIfLrQueueSize_Object=MibTableColumn
hwCBQoSIfLrQueueSize=_HwCBQoSIfLrQueueSize_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,1,8,1,7),_HwCBQoSIfLrQueueSize_Type())
hwCBQoSIfLrQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfLrQueueSize.setStatus(_A)
_HwCBQoSAtmPvcStaticsObjects_ObjectIdentity=ObjectIdentity
hwCBQoSAtmPvcStaticsObjects=_HwCBQoSAtmPvcStaticsObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2))
_HwCBQoSAtmPvcCbqRunInfoTable_Object=MibTable
hwCBQoSAtmPvcCbqRunInfoTable=_HwCBQoSAtmPvcCbqRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,1))
if mibBuilder.loadTexts:hwCBQoSAtmPvcCbqRunInfoTable.setStatus(_A)
_HwCBQoSAtmPvcCbqRunInfoEntry_Object=MibTableRow
hwCBQoSAtmPvcCbqRunInfoEntry=_HwCBQoSAtmPvcCbqRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,1,1))
hwCBQoSAtmPvcCbqRunInfoEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:hwCBQoSAtmPvcCbqRunInfoEntry.setStatus(_A)
_HwCBQoSAtmPvcCbqQueueSize_Type=Integer32
_HwCBQoSAtmPvcCbqQueueSize_Object=MibTableColumn
hwCBQoSAtmPvcCbqQueueSize=_HwCBQoSAtmPvcCbqQueueSize_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,1,1,1),_HwCBQoSAtmPvcCbqQueueSize_Type())
hwCBQoSAtmPvcCbqQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcCbqQueueSize.setStatus(_A)
_HwCBQoSAtmPvcCbqDiscard_Type=Counter32
_HwCBQoSAtmPvcCbqDiscard_Object=MibTableColumn
hwCBQoSAtmPvcCbqDiscard=_HwCBQoSAtmPvcCbqDiscard_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,1,1,2),_HwCBQoSAtmPvcCbqDiscard_Type())
hwCBQoSAtmPvcCbqDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcCbqDiscard.setStatus(_A)
_HwCBQoSAtmPvcCbqEfQueueSize_Type=Integer32
_HwCBQoSAtmPvcCbqEfQueueSize_Object=MibTableColumn
hwCBQoSAtmPvcCbqEfQueueSize=_HwCBQoSAtmPvcCbqEfQueueSize_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,1,1,3),_HwCBQoSAtmPvcCbqEfQueueSize_Type())
hwCBQoSAtmPvcCbqEfQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcCbqEfQueueSize.setStatus(_A)
_HwCBQoSAtmPvcCbqAfQueueSize_Type=Integer32
_HwCBQoSAtmPvcCbqAfQueueSize_Object=MibTableColumn
hwCBQoSAtmPvcCbqAfQueueSize=_HwCBQoSAtmPvcCbqAfQueueSize_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,1,1,4),_HwCBQoSAtmPvcCbqAfQueueSize_Type())
hwCBQoSAtmPvcCbqAfQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcCbqAfQueueSize.setStatus(_A)
_HwCBQoSAtmPvcCbqBeQueueSize_Type=Integer32
_HwCBQoSAtmPvcCbqBeQueueSize_Object=MibTableColumn
hwCBQoSAtmPvcCbqBeQueueSize=_HwCBQoSAtmPvcCbqBeQueueSize_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,1,1,5),_HwCBQoSAtmPvcCbqBeQueueSize_Type())
hwCBQoSAtmPvcCbqBeQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcCbqBeQueueSize.setStatus(_A)
_HwCBQoSAtmPvcCbqBeActiveQueueNum_Type=Integer32
_HwCBQoSAtmPvcCbqBeActiveQueueNum_Object=MibTableColumn
hwCBQoSAtmPvcCbqBeActiveQueueNum=_HwCBQoSAtmPvcCbqBeActiveQueueNum_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,1,1,6),_HwCBQoSAtmPvcCbqBeActiveQueueNum_Type())
hwCBQoSAtmPvcCbqBeActiveQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcCbqBeActiveQueueNum.setStatus(_A)
_HwCBQoSAtmPvcCbqBeMaxActiveQueueNum_Type=Integer32
_HwCBQoSAtmPvcCbqBeMaxActiveQueueNum_Object=MibTableColumn
hwCBQoSAtmPvcCbqBeMaxActiveQueueNum=_HwCBQoSAtmPvcCbqBeMaxActiveQueueNum_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,1,1,7),_HwCBQoSAtmPvcCbqBeMaxActiveQueueNum_Type())
hwCBQoSAtmPvcCbqBeMaxActiveQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcCbqBeMaxActiveQueueNum.setStatus(_A)
_HwCBQoSAtmPvcCbqBeTotalQueueNum_Type=Integer32
_HwCBQoSAtmPvcCbqBeTotalQueueNum_Object=MibTableColumn
hwCBQoSAtmPvcCbqBeTotalQueueNum=_HwCBQoSAtmPvcCbqBeTotalQueueNum_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,1,1,8),_HwCBQoSAtmPvcCbqBeTotalQueueNum_Type())
hwCBQoSAtmPvcCbqBeTotalQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcCbqBeTotalQueueNum.setStatus(_A)
_HwCBQoSAtmPvcCbqAfAllocatedQueueNum_Type=Integer32
_HwCBQoSAtmPvcCbqAfAllocatedQueueNum_Object=MibTableColumn
hwCBQoSAtmPvcCbqAfAllocatedQueueNum=_HwCBQoSAtmPvcCbqAfAllocatedQueueNum_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,1,1,9),_HwCBQoSAtmPvcCbqAfAllocatedQueueNum_Type())
hwCBQoSAtmPvcCbqAfAllocatedQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcCbqAfAllocatedQueueNum.setStatus(_A)
_HwCBQoSAtmPvcClassMatchRunInfoTable_Object=MibTable
hwCBQoSAtmPvcClassMatchRunInfoTable=_HwCBQoSAtmPvcClassMatchRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,2))
if mibBuilder.loadTexts:hwCBQoSAtmPvcClassMatchRunInfoTable.setStatus(_A)
_HwCBQoSAtmPvcClassMatchRunInfoEntry_Object=MibTableRow
hwCBQoSAtmPvcClassMatchRunInfoEntry=_HwCBQoSAtmPvcClassMatchRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,2,1))
hwCBQoSAtmPvcClassMatchRunInfoEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_Q),(0,_B,_F))
if mibBuilder.loadTexts:hwCBQoSAtmPvcClassMatchRunInfoEntry.setStatus(_A)
_HwCBQoSAtmPvcClassMatchPackets_Type=Counter32
_HwCBQoSAtmPvcClassMatchPackets_Object=MibTableColumn
hwCBQoSAtmPvcClassMatchPackets=_HwCBQoSAtmPvcClassMatchPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,2,1,1),_HwCBQoSAtmPvcClassMatchPackets_Type())
hwCBQoSAtmPvcClassMatchPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcClassMatchPackets.setStatus(_A)
_HwCBQoSAtmPvcClassMatchBytes_Type=Counter32
_HwCBQoSAtmPvcClassMatchBytes_Object=MibTableColumn
hwCBQoSAtmPvcClassMatchBytes=_HwCBQoSAtmPvcClassMatchBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,2,1,2),_HwCBQoSAtmPvcClassMatchBytes_Type())
hwCBQoSAtmPvcClassMatchBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcClassMatchBytes.setStatus(_A)
_HwCBQoSAtmPvcClassAverageRate_Type=Counter64
_HwCBQoSAtmPvcClassAverageRate_Object=MibTableColumn
hwCBQoSAtmPvcClassAverageRate=_HwCBQoSAtmPvcClassAverageRate_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,2,1,3),_HwCBQoSAtmPvcClassAverageRate_Type())
hwCBQoSAtmPvcClassAverageRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcClassAverageRate.setStatus(_A)
_HwCBQoSAtmPvcCarRunInfoTable_Object=MibTable
hwCBQoSAtmPvcCarRunInfoTable=_HwCBQoSAtmPvcCarRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,3))
if mibBuilder.loadTexts:hwCBQoSAtmPvcCarRunInfoTable.setStatus(_A)
_HwCBQoSAtmPvcCarRunInfoEntry_Object=MibTableRow
hwCBQoSAtmPvcCarRunInfoEntry=_HwCBQoSAtmPvcCarRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,3,1))
hwCBQoSAtmPvcCarRunInfoEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_Q),(0,_B,_F))
if mibBuilder.loadTexts:hwCBQoSAtmPvcCarRunInfoEntry.setStatus(_A)
_HwCBQoSAtmPvcCarConformPackets_Type=Counter32
_HwCBQoSAtmPvcCarConformPackets_Object=MibTableColumn
hwCBQoSAtmPvcCarConformPackets=_HwCBQoSAtmPvcCarConformPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,3,1,1),_HwCBQoSAtmPvcCarConformPackets_Type())
hwCBQoSAtmPvcCarConformPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcCarConformPackets.setStatus(_A)
_HwCBQoSAtmPvcCarConformBytes_Type=Counter32
_HwCBQoSAtmPvcCarConformBytes_Object=MibTableColumn
hwCBQoSAtmPvcCarConformBytes=_HwCBQoSAtmPvcCarConformBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,3,1,2),_HwCBQoSAtmPvcCarConformBytes_Type())
hwCBQoSAtmPvcCarConformBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcCarConformBytes.setStatus(_A)
_HwCBQoSAtmPvcCarExceedPackets_Type=Counter32
_HwCBQoSAtmPvcCarExceedPackets_Object=MibTableColumn
hwCBQoSAtmPvcCarExceedPackets=_HwCBQoSAtmPvcCarExceedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,3,1,3),_HwCBQoSAtmPvcCarExceedPackets_Type())
hwCBQoSAtmPvcCarExceedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcCarExceedPackets.setStatus(_A)
_HwCBQoSAtmPvcCarExceedBytes_Type=Counter32
_HwCBQoSAtmPvcCarExceedBytes_Object=MibTableColumn
hwCBQoSAtmPvcCarExceedBytes=_HwCBQoSAtmPvcCarExceedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,3,1,4),_HwCBQoSAtmPvcCarExceedBytes_Type())
hwCBQoSAtmPvcCarExceedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcCarExceedBytes.setStatus(_A)
_HwCBQoSAtmPvcGtsRunInfoTable_Object=MibTable
hwCBQoSAtmPvcGtsRunInfoTable=_HwCBQoSAtmPvcGtsRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,4))
if mibBuilder.loadTexts:hwCBQoSAtmPvcGtsRunInfoTable.setStatus(_A)
_HwCBQoSAtmPvcGtsRunInfoEntry_Object=MibTableRow
hwCBQoSAtmPvcGtsRunInfoEntry=_HwCBQoSAtmPvcGtsRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,4,1))
hwCBQoSAtmPvcGtsRunInfoEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_Q),(0,_B,_F))
if mibBuilder.loadTexts:hwCBQoSAtmPvcGtsRunInfoEntry.setStatus(_A)
_HwCBQoSAtmPvcGtsPassedPackets_Type=Counter32
_HwCBQoSAtmPvcGtsPassedPackets_Object=MibTableColumn
hwCBQoSAtmPvcGtsPassedPackets=_HwCBQoSAtmPvcGtsPassedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,4,1,1),_HwCBQoSAtmPvcGtsPassedPackets_Type())
hwCBQoSAtmPvcGtsPassedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcGtsPassedPackets.setStatus(_A)
_HwCBQoSAtmPvcGtsPassedBytes_Type=Counter32
_HwCBQoSAtmPvcGtsPassedBytes_Object=MibTableColumn
hwCBQoSAtmPvcGtsPassedBytes=_HwCBQoSAtmPvcGtsPassedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,4,1,2),_HwCBQoSAtmPvcGtsPassedBytes_Type())
hwCBQoSAtmPvcGtsPassedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcGtsPassedBytes.setStatus(_A)
_HwCBQoSAtmPvcGtsDiscardedPackets_Type=Counter32
_HwCBQoSAtmPvcGtsDiscardedPackets_Object=MibTableColumn
hwCBQoSAtmPvcGtsDiscardedPackets=_HwCBQoSAtmPvcGtsDiscardedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,4,1,3),_HwCBQoSAtmPvcGtsDiscardedPackets_Type())
hwCBQoSAtmPvcGtsDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcGtsDiscardedPackets.setStatus(_A)
_HwCBQoSAtmPvcGtsDiscardedBytes_Type=Counter32
_HwCBQoSAtmPvcGtsDiscardedBytes_Object=MibTableColumn
hwCBQoSAtmPvcGtsDiscardedBytes=_HwCBQoSAtmPvcGtsDiscardedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,4,1,4),_HwCBQoSAtmPvcGtsDiscardedBytes_Type())
hwCBQoSAtmPvcGtsDiscardedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcGtsDiscardedBytes.setStatus(_A)
_HwCBQoSAtmPvcGtsDelayedPackets_Type=Counter32
_HwCBQoSAtmPvcGtsDelayedPackets_Object=MibTableColumn
hwCBQoSAtmPvcGtsDelayedPackets=_HwCBQoSAtmPvcGtsDelayedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,4,1,5),_HwCBQoSAtmPvcGtsDelayedPackets_Type())
hwCBQoSAtmPvcGtsDelayedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcGtsDelayedPackets.setStatus(_A)
_HwCBQoSAtmPvcGtsDelayedBytes_Type=Counter32
_HwCBQoSAtmPvcGtsDelayedBytes_Object=MibTableColumn
hwCBQoSAtmPvcGtsDelayedBytes=_HwCBQoSAtmPvcGtsDelayedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,4,1,6),_HwCBQoSAtmPvcGtsDelayedBytes_Type())
hwCBQoSAtmPvcGtsDelayedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcGtsDelayedBytes.setStatus(_A)
_HwCBQoSAtmPvcGtsQueueSize_Type=Integer32
_HwCBQoSAtmPvcGtsQueueSize_Object=MibTableColumn
hwCBQoSAtmPvcGtsQueueSize=_HwCBQoSAtmPvcGtsQueueSize_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,4,1,7),_HwCBQoSAtmPvcGtsQueueSize_Type())
hwCBQoSAtmPvcGtsQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcGtsQueueSize.setStatus(_A)
_HwCBQoSAtmPvcRemarkRunInfoTable_Object=MibTable
hwCBQoSAtmPvcRemarkRunInfoTable=_HwCBQoSAtmPvcRemarkRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,5))
if mibBuilder.loadTexts:hwCBQoSAtmPvcRemarkRunInfoTable.setStatus(_A)
_HwCBQoSAtmPvcRemarkRunInfoEntry_Object=MibTableRow
hwCBQoSAtmPvcRemarkRunInfoEntry=_HwCBQoSAtmPvcRemarkRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,5,1))
hwCBQoSAtmPvcRemarkRunInfoEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_Q),(0,_B,_F))
if mibBuilder.loadTexts:hwCBQoSAtmPvcRemarkRunInfoEntry.setStatus(_A)
_HwCBQoSAtmPvcRemarkedPackets_Type=Counter32
_HwCBQoSAtmPvcRemarkedPackets_Object=MibTableColumn
hwCBQoSAtmPvcRemarkedPackets=_HwCBQoSAtmPvcRemarkedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,5,1,1),_HwCBQoSAtmPvcRemarkedPackets_Type())
hwCBQoSAtmPvcRemarkedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcRemarkedPackets.setStatus(_A)
_HwCBQoSAtmPvcQueueRunInfoTable_Object=MibTable
hwCBQoSAtmPvcQueueRunInfoTable=_HwCBQoSAtmPvcQueueRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,6))
if mibBuilder.loadTexts:hwCBQoSAtmPvcQueueRunInfoTable.setStatus(_A)
_HwCBQoSAtmPvcQueueRunInfoEntry_Object=MibTableRow
hwCBQoSAtmPvcQueueRunInfoEntry=_HwCBQoSAtmPvcQueueRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,6,1))
hwCBQoSAtmPvcQueueRunInfoEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_Q),(0,_B,_F))
if mibBuilder.loadTexts:hwCBQoSAtmPvcQueueRunInfoEntry.setStatus(_A)
_HwCBQoSAtmPvcQueueMatchedPackets_Type=Counter32
_HwCBQoSAtmPvcQueueMatchedPackets_Object=MibTableColumn
hwCBQoSAtmPvcQueueMatchedPackets=_HwCBQoSAtmPvcQueueMatchedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,6,1,1),_HwCBQoSAtmPvcQueueMatchedPackets_Type())
hwCBQoSAtmPvcQueueMatchedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcQueueMatchedPackets.setStatus(_A)
_HwCBQoSAtmPvcQueueMatchedBytes_Type=Counter32
_HwCBQoSAtmPvcQueueMatchedBytes_Object=MibTableColumn
hwCBQoSAtmPvcQueueMatchedBytes=_HwCBQoSAtmPvcQueueMatchedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,6,1,2),_HwCBQoSAtmPvcQueueMatchedBytes_Type())
hwCBQoSAtmPvcQueueMatchedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcQueueMatchedBytes.setStatus(_A)
_HwCBQoSAtmPvcQueueEnqueuedPackets_Type=Counter32
_HwCBQoSAtmPvcQueueEnqueuedPackets_Object=MibTableColumn
hwCBQoSAtmPvcQueueEnqueuedPackets=_HwCBQoSAtmPvcQueueEnqueuedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,6,1,3),_HwCBQoSAtmPvcQueueEnqueuedPackets_Type())
hwCBQoSAtmPvcQueueEnqueuedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcQueueEnqueuedPackets.setStatus(_A)
_HwCBQoSAtmPvcQueueEnqueuedBytes_Type=Counter32
_HwCBQoSAtmPvcQueueEnqueuedBytes_Object=MibTableColumn
hwCBQoSAtmPvcQueueEnqueuedBytes=_HwCBQoSAtmPvcQueueEnqueuedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,6,1,4),_HwCBQoSAtmPvcQueueEnqueuedBytes_Type())
hwCBQoSAtmPvcQueueEnqueuedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcQueueEnqueuedBytes.setStatus(_A)
_HwCBQoSAtmPvcQueueDiscardedPackets_Type=Counter32
_HwCBQoSAtmPvcQueueDiscardedPackets_Object=MibTableColumn
hwCBQoSAtmPvcQueueDiscardedPackets=_HwCBQoSAtmPvcQueueDiscardedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,6,1,5),_HwCBQoSAtmPvcQueueDiscardedPackets_Type())
hwCBQoSAtmPvcQueueDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcQueueDiscardedPackets.setStatus(_A)
_HwCBQoSAtmPvcQueueDiscardedBytes_Type=Counter32
_HwCBQoSAtmPvcQueueDiscardedBytes_Object=MibTableColumn
hwCBQoSAtmPvcQueueDiscardedBytes=_HwCBQoSAtmPvcQueueDiscardedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,6,1,6),_HwCBQoSAtmPvcQueueDiscardedBytes_Type())
hwCBQoSAtmPvcQueueDiscardedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcQueueDiscardedBytes.setStatus(_A)
_HwCBQoSAtmPvcWredRunInfoTable_Object=MibTable
hwCBQoSAtmPvcWredRunInfoTable=_HwCBQoSAtmPvcWredRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,7))
if mibBuilder.loadTexts:hwCBQoSAtmPvcWredRunInfoTable.setStatus(_A)
_HwCBQoSAtmPvcWredRunInfoEntry_Object=MibTableRow
hwCBQoSAtmPvcWredRunInfoEntry=_HwCBQoSAtmPvcWredRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,7,1))
hwCBQoSAtmPvcWredRunInfoEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_Q),(0,_B,_F),(0,_B,_U))
if mibBuilder.loadTexts:hwCBQoSAtmPvcWredRunInfoEntry.setStatus(_A)
_HwCBQoSAtmPvcWredRandomDiscardedPackets_Type=Counter32
_HwCBQoSAtmPvcWredRandomDiscardedPackets_Object=MibTableColumn
hwCBQoSAtmPvcWredRandomDiscardedPackets=_HwCBQoSAtmPvcWredRandomDiscardedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,7,1,1),_HwCBQoSAtmPvcWredRandomDiscardedPackets_Type())
hwCBQoSAtmPvcWredRandomDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcWredRandomDiscardedPackets.setStatus(_A)
_HwCBQoSAtmPvcWredTailDiscardedPackets_Type=Counter32
_HwCBQoSAtmPvcWredTailDiscardedPackets_Object=MibTableColumn
hwCBQoSAtmPvcWredTailDiscardedPackets=_HwCBQoSAtmPvcWredTailDiscardedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,7,1,2),_HwCBQoSAtmPvcWredTailDiscardedPackets_Type())
hwCBQoSAtmPvcWredTailDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcWredTailDiscardedPackets.setStatus(_A)
_HwCBQoSAtmPvcLrRunInfoTable_Object=MibTable
hwCBQoSAtmPvcLrRunInfoTable=_HwCBQoSAtmPvcLrRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,8))
if mibBuilder.loadTexts:hwCBQoSAtmPvcLrRunInfoTable.setStatus(_A)
_HwCBQoSAtmPvcLrRunInfoEntry_Object=MibTableRow
hwCBQoSAtmPvcLrRunInfoEntry=_HwCBQoSAtmPvcLrRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,8,1))
hwCBQoSAtmPvcLrRunInfoEntry.setIndexNames((0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_Q),(0,_B,_F))
if mibBuilder.loadTexts:hwCBQoSAtmPvcLrRunInfoEntry.setStatus(_A)
_HwCBQoSAtmPvcLrPassedPackets_Type=Counter32
_HwCBQoSAtmPvcLrPassedPackets_Object=MibTableColumn
hwCBQoSAtmPvcLrPassedPackets=_HwCBQoSAtmPvcLrPassedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,8,1,1),_HwCBQoSAtmPvcLrPassedPackets_Type())
hwCBQoSAtmPvcLrPassedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcLrPassedPackets.setStatus(_A)
_HwCBQoSAtmPvcLrPassedBytes_Type=Counter32
_HwCBQoSAtmPvcLrPassedBytes_Object=MibTableColumn
hwCBQoSAtmPvcLrPassedBytes=_HwCBQoSAtmPvcLrPassedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,8,1,2),_HwCBQoSAtmPvcLrPassedBytes_Type())
hwCBQoSAtmPvcLrPassedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcLrPassedBytes.setStatus(_A)
_HwCBQoSAtmPvcLrDiscardedPackets_Type=Counter32
_HwCBQoSAtmPvcLrDiscardedPackets_Object=MibTableColumn
hwCBQoSAtmPvcLrDiscardedPackets=_HwCBQoSAtmPvcLrDiscardedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,8,1,3),_HwCBQoSAtmPvcLrDiscardedPackets_Type())
hwCBQoSAtmPvcLrDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcLrDiscardedPackets.setStatus(_A)
_HwCBQoSAtmPvcLrDiscardedBytes_Type=Counter32
_HwCBQoSAtmPvcLrDiscardedBytes_Object=MibTableColumn
hwCBQoSAtmPvcLrDiscardedBytes=_HwCBQoSAtmPvcLrDiscardedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,8,1,4),_HwCBQoSAtmPvcLrDiscardedBytes_Type())
hwCBQoSAtmPvcLrDiscardedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcLrDiscardedBytes.setStatus(_A)
_HwCBQoSAtmPvcLrDelayedPackets_Type=Counter32
_HwCBQoSAtmPvcLrDelayedPackets_Object=MibTableColumn
hwCBQoSAtmPvcLrDelayedPackets=_HwCBQoSAtmPvcLrDelayedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,8,1,5),_HwCBQoSAtmPvcLrDelayedPackets_Type())
hwCBQoSAtmPvcLrDelayedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcLrDelayedPackets.setStatus(_A)
_HwCBQoSAtmPvcLrDelayedBytes_Type=Counter32
_HwCBQoSAtmPvcLrDelayedBytes_Object=MibTableColumn
hwCBQoSAtmPvcLrDelayedBytes=_HwCBQoSAtmPvcLrDelayedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,8,1,6),_HwCBQoSAtmPvcLrDelayedBytes_Type())
hwCBQoSAtmPvcLrDelayedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcLrDelayedBytes.setStatus(_A)
_HwCBQoSAtmPvcLrQueueSize_Type=Integer32
_HwCBQoSAtmPvcLrQueueSize_Object=MibTableColumn
hwCBQoSAtmPvcLrQueueSize=_HwCBQoSAtmPvcLrQueueSize_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,2,8,1,7),_HwCBQoSAtmPvcLrQueueSize_Type())
hwCBQoSAtmPvcLrQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSAtmPvcLrQueueSize.setStatus(_A)
_HwCBQoSFrPvcStaticsObjects_ObjectIdentity=ObjectIdentity
hwCBQoSFrPvcStaticsObjects=_HwCBQoSFrPvcStaticsObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3))
_HwCBQoSFrPvcCbqRunInfoTable_Object=MibTable
hwCBQoSFrPvcCbqRunInfoTable=_HwCBQoSFrPvcCbqRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,1))
if mibBuilder.loadTexts:hwCBQoSFrPvcCbqRunInfoTable.setStatus(_A)
_HwCBQoSFrPvcCbqRunInfoEntry_Object=MibTableRow
hwCBQoSFrPvcCbqRunInfoEntry=_HwCBQoSFrPvcCbqRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,1,1))
hwCBQoSFrPvcCbqRunInfoEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:hwCBQoSFrPvcCbqRunInfoEntry.setStatus(_A)
_HwCBQoSFrPvcCbqQueueSize_Type=Integer32
_HwCBQoSFrPvcCbqQueueSize_Object=MibTableColumn
hwCBQoSFrPvcCbqQueueSize=_HwCBQoSFrPvcCbqQueueSize_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,1,1,1),_HwCBQoSFrPvcCbqQueueSize_Type())
hwCBQoSFrPvcCbqQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcCbqQueueSize.setStatus(_A)
_HwCBQoSFrPvcCbqDiscard_Type=Counter32
_HwCBQoSFrPvcCbqDiscard_Object=MibTableColumn
hwCBQoSFrPvcCbqDiscard=_HwCBQoSFrPvcCbqDiscard_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,1,1,2),_HwCBQoSFrPvcCbqDiscard_Type())
hwCBQoSFrPvcCbqDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcCbqDiscard.setStatus(_A)
_HwCBQoSFrPvcCbqEfQueueSize_Type=Integer32
_HwCBQoSFrPvcCbqEfQueueSize_Object=MibTableColumn
hwCBQoSFrPvcCbqEfQueueSize=_HwCBQoSFrPvcCbqEfQueueSize_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,1,1,3),_HwCBQoSFrPvcCbqEfQueueSize_Type())
hwCBQoSFrPvcCbqEfQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcCbqEfQueueSize.setStatus(_A)
_HwCBQoSFrPvcCbqAfQueueSize_Type=Integer32
_HwCBQoSFrPvcCbqAfQueueSize_Object=MibTableColumn
hwCBQoSFrPvcCbqAfQueueSize=_HwCBQoSFrPvcCbqAfQueueSize_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,1,1,4),_HwCBQoSFrPvcCbqAfQueueSize_Type())
hwCBQoSFrPvcCbqAfQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcCbqAfQueueSize.setStatus(_A)
_HwCBQoSFrPvcCbqBeQueueSize_Type=Integer32
_HwCBQoSFrPvcCbqBeQueueSize_Object=MibTableColumn
hwCBQoSFrPvcCbqBeQueueSize=_HwCBQoSFrPvcCbqBeQueueSize_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,1,1,5),_HwCBQoSFrPvcCbqBeQueueSize_Type())
hwCBQoSFrPvcCbqBeQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcCbqBeQueueSize.setStatus(_A)
_HwCBQoSFrPvcCbqBeActiveQueueNum_Type=Integer32
_HwCBQoSFrPvcCbqBeActiveQueueNum_Object=MibTableColumn
hwCBQoSFrPvcCbqBeActiveQueueNum=_HwCBQoSFrPvcCbqBeActiveQueueNum_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,1,1,6),_HwCBQoSFrPvcCbqBeActiveQueueNum_Type())
hwCBQoSFrPvcCbqBeActiveQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcCbqBeActiveQueueNum.setStatus(_A)
_HwCBQoSFrPvcCbqBeMaxActiveQueueNum_Type=Integer32
_HwCBQoSFrPvcCbqBeMaxActiveQueueNum_Object=MibTableColumn
hwCBQoSFrPvcCbqBeMaxActiveQueueNum=_HwCBQoSFrPvcCbqBeMaxActiveQueueNum_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,1,1,7),_HwCBQoSFrPvcCbqBeMaxActiveQueueNum_Type())
hwCBQoSFrPvcCbqBeMaxActiveQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcCbqBeMaxActiveQueueNum.setStatus(_A)
_HwCBQoSFrPvcCbqBeTotalQueueNum_Type=Integer32
_HwCBQoSFrPvcCbqBeTotalQueueNum_Object=MibTableColumn
hwCBQoSFrPvcCbqBeTotalQueueNum=_HwCBQoSFrPvcCbqBeTotalQueueNum_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,1,1,8),_HwCBQoSFrPvcCbqBeTotalQueueNum_Type())
hwCBQoSFrPvcCbqBeTotalQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcCbqBeTotalQueueNum.setStatus(_A)
_HwCBQoSFrPvcCbqAfAllocatedQueueNum_Type=Integer32
_HwCBQoSFrPvcCbqAfAllocatedQueueNum_Object=MibTableColumn
hwCBQoSFrPvcCbqAfAllocatedQueueNum=_HwCBQoSFrPvcCbqAfAllocatedQueueNum_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,1,1,9),_HwCBQoSFrPvcCbqAfAllocatedQueueNum_Type())
hwCBQoSFrPvcCbqAfAllocatedQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcCbqAfAllocatedQueueNum.setStatus(_A)
_HwCBQoSFrPvcClassMatchRunInfoTable_Object=MibTable
hwCBQoSFrPvcClassMatchRunInfoTable=_HwCBQoSFrPvcClassMatchRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,2))
if mibBuilder.loadTexts:hwCBQoSFrPvcClassMatchRunInfoTable.setStatus(_A)
_HwCBQoSFrPvcClassMatchRunInfoEntry_Object=MibTableRow
hwCBQoSFrPvcClassMatchRunInfoEntry=_HwCBQoSFrPvcClassMatchRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,2,1))
hwCBQoSFrPvcClassMatchRunInfoEntry.setIndexNames((0,_B,_N),(0,_B,_O),(0,_B,_R),(0,_B,_F))
if mibBuilder.loadTexts:hwCBQoSFrPvcClassMatchRunInfoEntry.setStatus(_A)
_HwCBQoSFrPvcClassMatchedPackets_Type=Counter32
_HwCBQoSFrPvcClassMatchedPackets_Object=MibTableColumn
hwCBQoSFrPvcClassMatchedPackets=_HwCBQoSFrPvcClassMatchedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,2,1,1),_HwCBQoSFrPvcClassMatchedPackets_Type())
hwCBQoSFrPvcClassMatchedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcClassMatchedPackets.setStatus(_A)
_HwCBQoSFrPvcClassMatchedBytes_Type=Counter32
_HwCBQoSFrPvcClassMatchedBytes_Object=MibTableColumn
hwCBQoSFrPvcClassMatchedBytes=_HwCBQoSFrPvcClassMatchedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,2,1,2),_HwCBQoSFrPvcClassMatchedBytes_Type())
hwCBQoSFrPvcClassMatchedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcClassMatchedBytes.setStatus(_A)
_HwCBQoSFrPvcClassAverageRate_Type=Counter64
_HwCBQoSFrPvcClassAverageRate_Object=MibTableColumn
hwCBQoSFrPvcClassAverageRate=_HwCBQoSFrPvcClassAverageRate_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,2,1,3),_HwCBQoSFrPvcClassAverageRate_Type())
hwCBQoSFrPvcClassAverageRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcClassAverageRate.setStatus(_A)
_HwCBQoSFrPvcCarRunInfoTable_Object=MibTable
hwCBQoSFrPvcCarRunInfoTable=_HwCBQoSFrPvcCarRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,3))
if mibBuilder.loadTexts:hwCBQoSFrPvcCarRunInfoTable.setStatus(_A)
_HwCBQoSFrPvcCarRunInfoEntry_Object=MibTableRow
hwCBQoSFrPvcCarRunInfoEntry=_HwCBQoSFrPvcCarRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,3,1))
hwCBQoSFrPvcCarRunInfoEntry.setIndexNames((0,_B,_N),(0,_B,_O),(0,_B,_R),(0,_B,_F))
if mibBuilder.loadTexts:hwCBQoSFrPvcCarRunInfoEntry.setStatus(_A)
_HwCBQoSFrPvcCarConformPackets_Type=Counter32
_HwCBQoSFrPvcCarConformPackets_Object=MibTableColumn
hwCBQoSFrPvcCarConformPackets=_HwCBQoSFrPvcCarConformPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,3,1,1),_HwCBQoSFrPvcCarConformPackets_Type())
hwCBQoSFrPvcCarConformPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcCarConformPackets.setStatus(_A)
_HwCBQoSFrPvcCarConformBytes_Type=Counter32
_HwCBQoSFrPvcCarConformBytes_Object=MibTableColumn
hwCBQoSFrPvcCarConformBytes=_HwCBQoSFrPvcCarConformBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,3,1,2),_HwCBQoSFrPvcCarConformBytes_Type())
hwCBQoSFrPvcCarConformBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcCarConformBytes.setStatus(_A)
_HwCBQoSFrPvcCarExceedPackets_Type=Counter32
_HwCBQoSFrPvcCarExceedPackets_Object=MibTableColumn
hwCBQoSFrPvcCarExceedPackets=_HwCBQoSFrPvcCarExceedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,3,1,3),_HwCBQoSFrPvcCarExceedPackets_Type())
hwCBQoSFrPvcCarExceedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcCarExceedPackets.setStatus(_A)
_HwCBQoSFrPvcCarExceedBytes_Type=Counter32
_HwCBQoSFrPvcCarExceedBytes_Object=MibTableColumn
hwCBQoSFrPvcCarExceedBytes=_HwCBQoSFrPvcCarExceedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,3,1,4),_HwCBQoSFrPvcCarExceedBytes_Type())
hwCBQoSFrPvcCarExceedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcCarExceedBytes.setStatus(_A)
_HwCBQoSFrPvcGtsRunInfoTable_Object=MibTable
hwCBQoSFrPvcGtsRunInfoTable=_HwCBQoSFrPvcGtsRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,4))
if mibBuilder.loadTexts:hwCBQoSFrPvcGtsRunInfoTable.setStatus(_A)
_HwCBQoSFrPvcGtsRunInfoEntry_Object=MibTableRow
hwCBQoSFrPvcGtsRunInfoEntry=_HwCBQoSFrPvcGtsRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,4,1))
hwCBQoSFrPvcGtsRunInfoEntry.setIndexNames((0,_B,_N),(0,_B,_O),(0,_B,_R),(0,_B,_F))
if mibBuilder.loadTexts:hwCBQoSFrPvcGtsRunInfoEntry.setStatus(_A)
_HwCBQoSFrPvcGtsPassedPackets_Type=Counter32
_HwCBQoSFrPvcGtsPassedPackets_Object=MibTableColumn
hwCBQoSFrPvcGtsPassedPackets=_HwCBQoSFrPvcGtsPassedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,4,1,1),_HwCBQoSFrPvcGtsPassedPackets_Type())
hwCBQoSFrPvcGtsPassedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcGtsPassedPackets.setStatus(_A)
_HwCBQoSFrPvcGtsPassedBytes_Type=Counter32
_HwCBQoSFrPvcGtsPassedBytes_Object=MibTableColumn
hwCBQoSFrPvcGtsPassedBytes=_HwCBQoSFrPvcGtsPassedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,4,1,2),_HwCBQoSFrPvcGtsPassedBytes_Type())
hwCBQoSFrPvcGtsPassedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcGtsPassedBytes.setStatus(_A)
_HwCBQoSFrPvcGtsDiscardedPackets_Type=Counter32
_HwCBQoSFrPvcGtsDiscardedPackets_Object=MibTableColumn
hwCBQoSFrPvcGtsDiscardedPackets=_HwCBQoSFrPvcGtsDiscardedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,4,1,3),_HwCBQoSFrPvcGtsDiscardedPackets_Type())
hwCBQoSFrPvcGtsDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcGtsDiscardedPackets.setStatus(_A)
_HwCBQoSFrPvcGtsDiscardedBytes_Type=Counter32
_HwCBQoSFrPvcGtsDiscardedBytes_Object=MibTableColumn
hwCBQoSFrPvcGtsDiscardedBytes=_HwCBQoSFrPvcGtsDiscardedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,4,1,4),_HwCBQoSFrPvcGtsDiscardedBytes_Type())
hwCBQoSFrPvcGtsDiscardedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcGtsDiscardedBytes.setStatus(_A)
_HwCBQoSFrPvcGtsDelayedPackets_Type=Counter32
_HwCBQoSFrPvcGtsDelayedPackets_Object=MibTableColumn
hwCBQoSFrPvcGtsDelayedPackets=_HwCBQoSFrPvcGtsDelayedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,4,1,5),_HwCBQoSFrPvcGtsDelayedPackets_Type())
hwCBQoSFrPvcGtsDelayedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcGtsDelayedPackets.setStatus(_A)
_HwCBQoSFrPvcGtsDelayedBytes_Type=Counter32
_HwCBQoSFrPvcGtsDelayedBytes_Object=MibTableColumn
hwCBQoSFrPvcGtsDelayedBytes=_HwCBQoSFrPvcGtsDelayedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,4,1,6),_HwCBQoSFrPvcGtsDelayedBytes_Type())
hwCBQoSFrPvcGtsDelayedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcGtsDelayedBytes.setStatus(_A)
_HwCBQoSFrPvcGtsQueueSize_Type=Integer32
_HwCBQoSFrPvcGtsQueueSize_Object=MibTableColumn
hwCBQoSFrPvcGtsQueueSize=_HwCBQoSFrPvcGtsQueueSize_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,4,1,7),_HwCBQoSFrPvcGtsQueueSize_Type())
hwCBQoSFrPvcGtsQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcGtsQueueSize.setStatus(_A)
_HwCBQoSFrPvcRemarkRunInfoTable_Object=MibTable
hwCBQoSFrPvcRemarkRunInfoTable=_HwCBQoSFrPvcRemarkRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,5))
if mibBuilder.loadTexts:hwCBQoSFrPvcRemarkRunInfoTable.setStatus(_A)
_HwCBQoSFrPvcRemarkRunInfoEntry_Object=MibTableRow
hwCBQoSFrPvcRemarkRunInfoEntry=_HwCBQoSFrPvcRemarkRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,5,1))
hwCBQoSFrPvcRemarkRunInfoEntry.setIndexNames((0,_B,_N),(0,_B,_O),(0,_B,_R),(0,_B,_F))
if mibBuilder.loadTexts:hwCBQoSFrPvcRemarkRunInfoEntry.setStatus(_A)
_HwCBQoSFrPvcRemarkedPackets_Type=Counter32
_HwCBQoSFrPvcRemarkedPackets_Object=MibTableColumn
hwCBQoSFrPvcRemarkedPackets=_HwCBQoSFrPvcRemarkedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,5,1,1),_HwCBQoSFrPvcRemarkedPackets_Type())
hwCBQoSFrPvcRemarkedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcRemarkedPackets.setStatus(_A)
_HwCBQoSFrPvcQueueRunInfoTable_Object=MibTable
hwCBQoSFrPvcQueueRunInfoTable=_HwCBQoSFrPvcQueueRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,6))
if mibBuilder.loadTexts:hwCBQoSFrPvcQueueRunInfoTable.setStatus(_A)
_HwCBQoSFrPvcQueueRunInfoEntry_Object=MibTableRow
hwCBQoSFrPvcQueueRunInfoEntry=_HwCBQoSFrPvcQueueRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,6,1))
hwCBQoSFrPvcQueueRunInfoEntry.setIndexNames((0,_B,_N),(0,_B,_O),(0,_B,_R),(0,_B,_F))
if mibBuilder.loadTexts:hwCBQoSFrPvcQueueRunInfoEntry.setStatus(_A)
_HwCBQoSFrPvcQueueMatchedPackets_Type=Counter32
_HwCBQoSFrPvcQueueMatchedPackets_Object=MibTableColumn
hwCBQoSFrPvcQueueMatchedPackets=_HwCBQoSFrPvcQueueMatchedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,6,1,1),_HwCBQoSFrPvcQueueMatchedPackets_Type())
hwCBQoSFrPvcQueueMatchedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcQueueMatchedPackets.setStatus(_A)
_HwCBQoSFrPvcQueueMatchedBytes_Type=Counter32
_HwCBQoSFrPvcQueueMatchedBytes_Object=MibTableColumn
hwCBQoSFrPvcQueueMatchedBytes=_HwCBQoSFrPvcQueueMatchedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,6,1,2),_HwCBQoSFrPvcQueueMatchedBytes_Type())
hwCBQoSFrPvcQueueMatchedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcQueueMatchedBytes.setStatus(_A)
_HwCBQoSFrPvcQueueEnqueuedPackets_Type=Counter32
_HwCBQoSFrPvcQueueEnqueuedPackets_Object=MibTableColumn
hwCBQoSFrPvcQueueEnqueuedPackets=_HwCBQoSFrPvcQueueEnqueuedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,6,1,3),_HwCBQoSFrPvcQueueEnqueuedPackets_Type())
hwCBQoSFrPvcQueueEnqueuedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcQueueEnqueuedPackets.setStatus(_A)
_HwCBQoSFrPvcQueueEnqueuedBytes_Type=Counter32
_HwCBQoSFrPvcQueueEnqueuedBytes_Object=MibTableColumn
hwCBQoSFrPvcQueueEnqueuedBytes=_HwCBQoSFrPvcQueueEnqueuedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,6,1,4),_HwCBQoSFrPvcQueueEnqueuedBytes_Type())
hwCBQoSFrPvcQueueEnqueuedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcQueueEnqueuedBytes.setStatus(_A)
_HwCBQoSFrPvcQueueDiscardedPackets_Type=Counter32
_HwCBQoSFrPvcQueueDiscardedPackets_Object=MibTableColumn
hwCBQoSFrPvcQueueDiscardedPackets=_HwCBQoSFrPvcQueueDiscardedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,6,1,5),_HwCBQoSFrPvcQueueDiscardedPackets_Type())
hwCBQoSFrPvcQueueDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcQueueDiscardedPackets.setStatus(_A)
_HwCBQoSFrPvcQueueDiscardedBytes_Type=Counter32
_HwCBQoSFrPvcQueueDiscardedBytes_Object=MibTableColumn
hwCBQoSFrPvcQueueDiscardedBytes=_HwCBQoSFrPvcQueueDiscardedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,6,1,6),_HwCBQoSFrPvcQueueDiscardedBytes_Type())
hwCBQoSFrPvcQueueDiscardedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcQueueDiscardedBytes.setStatus(_A)
_HwCBQoSFrPvcWredRunInfoTable_Object=MibTable
hwCBQoSFrPvcWredRunInfoTable=_HwCBQoSFrPvcWredRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,7))
if mibBuilder.loadTexts:hwCBQoSFrPvcWredRunInfoTable.setStatus(_A)
_HwCBQoSFrPvcWredRunInfoEntry_Object=MibTableRow
hwCBQoSFrPvcWredRunInfoEntry=_HwCBQoSFrPvcWredRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,7,1))
hwCBQoSFrPvcWredRunInfoEntry.setIndexNames((0,_B,_N),(0,_B,_O),(0,_B,_R),(0,_B,_F),(0,_B,_U))
if mibBuilder.loadTexts:hwCBQoSFrPvcWredRunInfoEntry.setStatus(_A)
_HwCBQoSFrPvcWredRandomDiscardedPackets_Type=Counter32
_HwCBQoSFrPvcWredRandomDiscardedPackets_Object=MibTableColumn
hwCBQoSFrPvcWredRandomDiscardedPackets=_HwCBQoSFrPvcWredRandomDiscardedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,7,1,1),_HwCBQoSFrPvcWredRandomDiscardedPackets_Type())
hwCBQoSFrPvcWredRandomDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcWredRandomDiscardedPackets.setStatus(_A)
_HwCBQoSFrPvcWredTailDiscardedPackets_Type=Counter32
_HwCBQoSFrPvcWredTailDiscardedPackets_Object=MibTableColumn
hwCBQoSFrPvcWredTailDiscardedPackets=_HwCBQoSFrPvcWredTailDiscardedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,7,1,2),_HwCBQoSFrPvcWredTailDiscardedPackets_Type())
hwCBQoSFrPvcWredTailDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcWredTailDiscardedPackets.setStatus(_A)
_HwCBQoSFrPvcLrRunInfoTable_Object=MibTable
hwCBQoSFrPvcLrRunInfoTable=_HwCBQoSFrPvcLrRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,8))
if mibBuilder.loadTexts:hwCBQoSFrPvcLrRunInfoTable.setStatus(_A)
_HwCBQoSFrPvcLrRunInfoEntry_Object=MibTableRow
hwCBQoSFrPvcLrRunInfoEntry=_HwCBQoSFrPvcLrRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,8,1))
hwCBQoSFrPvcLrRunInfoEntry.setIndexNames((0,_B,_N),(0,_B,_O),(0,_B,_R),(0,_B,_F))
if mibBuilder.loadTexts:hwCBQoSFrPvcLrRunInfoEntry.setStatus(_A)
_HwCBQoSFrPvcLrPassedPackets_Type=Counter32
_HwCBQoSFrPvcLrPassedPackets_Object=MibTableColumn
hwCBQoSFrPvcLrPassedPackets=_HwCBQoSFrPvcLrPassedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,8,1,1),_HwCBQoSFrPvcLrPassedPackets_Type())
hwCBQoSFrPvcLrPassedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcLrPassedPackets.setStatus(_A)
_HwCBQoSFrPvcLrPassedBytes_Type=Counter32
_HwCBQoSFrPvcLrPassedBytes_Object=MibTableColumn
hwCBQoSFrPvcLrPassedBytes=_HwCBQoSFrPvcLrPassedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,8,1,2),_HwCBQoSFrPvcLrPassedBytes_Type())
hwCBQoSFrPvcLrPassedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcLrPassedBytes.setStatus(_A)
_HwCBQoSFrPvcLrDiscardedPackets_Type=Counter32
_HwCBQoSFrPvcLrDiscardedPackets_Object=MibTableColumn
hwCBQoSFrPvcLrDiscardedPackets=_HwCBQoSFrPvcLrDiscardedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,8,1,3),_HwCBQoSFrPvcLrDiscardedPackets_Type())
hwCBQoSFrPvcLrDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcLrDiscardedPackets.setStatus(_A)
_HwCBQoSFrPvcLrDiscardedBytes_Type=Counter32
_HwCBQoSFrPvcLrDiscardedBytes_Object=MibTableColumn
hwCBQoSFrPvcLrDiscardedBytes=_HwCBQoSFrPvcLrDiscardedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,8,1,4),_HwCBQoSFrPvcLrDiscardedBytes_Type())
hwCBQoSFrPvcLrDiscardedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcLrDiscardedBytes.setStatus(_A)
_HwCBQoSFrPvcLrDelayedPackets_Type=Counter32
_HwCBQoSFrPvcLrDelayedPackets_Object=MibTableColumn
hwCBQoSFrPvcLrDelayedPackets=_HwCBQoSFrPvcLrDelayedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,8,1,5),_HwCBQoSFrPvcLrDelayedPackets_Type())
hwCBQoSFrPvcLrDelayedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcLrDelayedPackets.setStatus(_A)
_HwCBQoSFrPvcLrDelayedBytes_Type=Counter32
_HwCBQoSFrPvcLrDelayedBytes_Object=MibTableColumn
hwCBQoSFrPvcLrDelayedBytes=_HwCBQoSFrPvcLrDelayedBytes_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,8,1,6),_HwCBQoSFrPvcLrDelayedBytes_Type())
hwCBQoSFrPvcLrDelayedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcLrDelayedBytes.setStatus(_A)
_HwCBQoSFrPvcLrQueueSize_Type=Integer32
_HwCBQoSFrPvcLrQueueSize_Object=MibTableColumn
hwCBQoSFrPvcLrQueueSize=_HwCBQoSFrPvcLrQueueSize_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,3,8,1,7),_HwCBQoSFrPvcLrQueueSize_Type())
hwCBQoSFrPvcLrQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSFrPvcLrQueueSize.setStatus(_A)
_HwCBQoSIfVlanStaticsObjects_ObjectIdentity=ObjectIdentity
hwCBQoSIfVlanStaticsObjects=_HwCBQoSIfVlanStaticsObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,4))
_HwCBQoSIfVlanClassMatchRunInfoTable_Object=MibTable
hwCBQoSIfVlanClassMatchRunInfoTable=_HwCBQoSIfVlanClassMatchRunInfoTable_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,4,1))
if mibBuilder.loadTexts:hwCBQoSIfVlanClassMatchRunInfoTable.setStatus(_A)
_HwCBQoSIfVlanClassMatchRunInfoEntry_Object=MibTableRow
hwCBQoSIfVlanClassMatchRunInfoEntry=_HwCBQoSIfVlanClassMatchRunInfoEntry_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,4,1,1))
hwCBQoSIfVlanClassMatchRunInfoEntry.setIndexNames((0,_B,_Y),(0,_B,_Z),(0,_B,_a),(0,_B,_F))
if mibBuilder.loadTexts:hwCBQoSIfVlanClassMatchRunInfoEntry.setStatus(_A)
_HwCBQoSIfVlanClassMatchedPackets_Type=Counter32
_HwCBQoSIfVlanClassMatchedPackets_Object=MibTableColumn
hwCBQoSIfVlanClassMatchedPackets=_HwCBQoSIfVlanClassMatchedPackets_Object((1,3,6,1,4,1,43,45,1,5,25,32,1,1,5,4,1,1,1),_HwCBQoSIfVlanClassMatchedPackets_Type())
hwCBQoSIfVlanClassMatchedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hwCBQoSIfVlanClassMatchedPackets.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'MatchRuleType':MatchRuleType,_W:CarAction,'RemarkType':RemarkType,_m:WredType,'QueueType':QueueType,'QueueBandwidthUnit':QueueBandwidthUnit,'LrCirUnit':LrCirUnit,'DirectionType':DirectionType,'hwCBQoSMIB':hwCBQoSMIB,'hwCBQoSObjects':hwCBQoSObjects,'hwCBQoSClassifierObjects':hwCBQoSClassifierObjects,'hwCBQoSClassifierIndexNext':hwCBQoSClassifierIndexNext,'hwCBQoSClassifierCfgInfoTable':hwCBQoSClassifierCfgInfoTable,'hwCBQoSClassifierCfgInfoEntry':hwCBQoSClassifierCfgInfoEntry,_V:hwCBQoSClassifierIndex,'hwCBQoSClassifierName':hwCBQoSClassifierName,'hwCBQoSClassifierRuleCount':hwCBQoSClassifierRuleCount,'hwCBQoSClassifierOperator':hwCBQoSClassifierOperator,'hwCBQoSClassifierLayer':hwCBQoSClassifierLayer,'hwCBQoSClassifierRowStatus':hwCBQoSClassifierRowStatus,'hwCBQoSMatchRuleCfgInfoTable':hwCBQoSMatchRuleCfgInfoTable,'hwCBQoSMatchRuleCfgInfoEntry':hwCBQoSMatchRuleCfgInfoEntry,_k:hwCBQoSMatchRuleIndex,'hwCBQoSMatchRuleIfNot':hwCBQoSMatchRuleIfNot,'hwCBQoSMatchRuleType':hwCBQoSMatchRuleType,'hwCBQoSMatchRuleStringValue':hwCBQoSMatchRuleStringValue,'hwCBQoSMatchRuleIntValue1':hwCBQoSMatchRuleIntValue1,'hwCBQoSMatchRuleIntValue2':hwCBQoSMatchRuleIntValue2,'hwCBQoSMatchRuleRowStatus':hwCBQoSMatchRuleRowStatus,'hwCBQoSBehaviorObjects':hwCBQoSBehaviorObjects,'hwCBQoSBehaviorIndexNext':hwCBQoSBehaviorIndexNext,'hwCBQoSBehaviorCfgInfoTable':hwCBQoSBehaviorCfgInfoTable,'hwCBQoSBehaviorCfgInfoEntry':hwCBQoSBehaviorCfgInfoEntry,_I:hwCBQoSBehaviorIndex,'hwCBQoSBehaviorName':hwCBQoSBehaviorName,'hwCBQoSBehaviorRowStatus':hwCBQoSBehaviorRowStatus,'hwCBQoSCarCfgInfoTable':hwCBQoSCarCfgInfoTable,'hwCBQoSCarCfgInfoEntry':hwCBQoSCarCfgInfoEntry,'hwCBQoSCarCir':hwCBQoSCarCir,'hwCBQoSCarCbs':hwCBQoSCarCbs,'hwCBQoSCarEbs':hwCBQoSCarEbs,'hwCBQoSCarPir':hwCBQoSCarPir,'hwCBQoSCarPbs':hwCBQoSCarPbs,'hwCBQoSCarGreenAction':hwCBQoSCarGreenAction,'hwCBQoSCarGreenRemarkValue':hwCBQoSCarGreenRemarkValue,'hwCBQoSCarYellowAction':hwCBQoSCarYellowAction,'hwCBQoSCarRedAction':hwCBQoSCarRedAction,'hwCBQoSCarRedRemarkValue':hwCBQoSCarRedRemarkValue,'hwCBQoSCarRowStatus':hwCBQoSCarRowStatus,'hwCBQoSGtsCfgInfoTable':hwCBQoSGtsCfgInfoTable,'hwCBQoSGtsCfgInfoEntry':hwCBQoSGtsCfgInfoEntry,'hwCBQoSGtsCir':hwCBQoSGtsCir,'hwCBQoSGtsCbs':hwCBQoSGtsCbs,'hwCBQoSGtsEbs':hwCBQoSGtsEbs,'hwCBQoSGtsQueueLength':hwCBQoSGtsQueueLength,'hwCBQoSGtsRowStatus':hwCBQoSGtsRowStatus,'hwCBQoSRemarkCfgInfoTable':hwCBQoSRemarkCfgInfoTable,'hwCBQoSRemarkCfgInfoEntry':hwCBQoSRemarkCfgInfoEntry,_l:hwCBQoSRemarkType,'hwCBQoSRemarkValue':hwCBQoSRemarkValue,'hwCBQoSRemarkRowStatus':hwCBQoSRemarkRowStatus,'hwCBQoSQueueCfgInfoTable':hwCBQoSQueueCfgInfoTable,'hwCBQoSQueueCfgInfoEntry':hwCBQoSQueueCfgInfoEntry,'hwCBQoSQueueType':hwCBQoSQueueType,'hwCBQoSQueueDropType':hwCBQoSQueueDropType,'hwCBQoSQueueLength':hwCBQoSQueueLength,'hwCBQoSQueueBandwidthUnit':hwCBQoSQueueBandwidthUnit,'hwCBQoSQueueBandwidthValue':hwCBQoSQueueBandwidthValue,'hwCBQoSQueueCbs':hwCBQoSQueueCbs,'hwCBQoSQueueQueueNumber':hwCBQoSQueueQueueNumber,'hwCBQoSQueueRowStatus':hwCBQoSQueueRowStatus,'hwCBQoSQueueCbsRatio':hwCBQoSQueueCbsRatio,'hwCBQoSWredCfgInfoTable':hwCBQoSWredCfgInfoTable,'hwCBQoSWredCfgInfoEntry':hwCBQoSWredCfgInfoEntry,'hwCBQoSWredType':hwCBQoSWredType,'hwCBQoSWredWeightConst':hwCBQoSWredWeightConst,'hwCBQoSWredClassCfgInfoTable':hwCBQoSWredClassCfgInfoTable,'hwCBQoSWredClassCfgInfoEntry':hwCBQoSWredClassCfgInfoEntry,_U:hwCBQoSWredClassValue,'hwCBQoSWredClassLowLimit':hwCBQoSWredClassLowLimit,'hwCBQoSWredClassHighLimit':hwCBQoSWredClassHighLimit,'hwCBQoSWredClassDiscardProb':hwCBQoSWredClassDiscardProb,'hwCBQoSPolicyRouteCfgInfoTable':hwCBQoSPolicyRouteCfgInfoTable,'hwCBQoSPolicyRouteCfgInfoEntry':hwCBQoSPolicyRouteCfgInfoEntry,'hwCBQoSPolicyRouteNexthop':hwCBQoSPolicyRouteNexthop,'hwCBQoSPolicyRouteBackup':hwCBQoSPolicyRouteBackup,'hwCBQoSPolicyRouteRowStatus':hwCBQoSPolicyRouteRowStatus,'hwCBQoSNatCfgInfoTable':hwCBQoSNatCfgInfoTable,'hwCBQoSNatCfgInfoEntry':hwCBQoSNatCfgInfoEntry,'hwCBQoSNatMainNumber':hwCBQoSNatMainNumber,'hwCBQoSNatBackupNumber':hwCBQoSNatBackupNumber,'hwCBQoSNatServiceClass':hwCBQoSNatServiceClass,'hwCBQoSNatRowStatus':hwCBQoSNatRowStatus,'hwCBQoSFirewallCfgInfoTable':hwCBQoSFirewallCfgInfoTable,'hwCBQoSFirewallCfgInfoEntry':hwCBQoSFirewallCfgInfoEntry,'hwCBQoSFirewallAction':hwCBQoSFirewallAction,'hwCBQoSFirewallRowStatus':hwCBQoSFirewallRowStatus,'hwCBQoSSamplingCfgInfoTable':hwCBQoSSamplingCfgInfoTable,'hwCBQoSSamplingCfgInfoEntry':hwCBQoSSamplingCfgInfoEntry,'hwCBQoSSamplingNum':hwCBQoSSamplingNum,'hwCBQoSSamplingRowStatus':hwCBQoSSamplingRowStatus,'hwCBQoSLrCfgInfoTable':hwCBQoSLrCfgInfoTable,'hwCBQoSLrCfgInfoEntry':hwCBQoSLrCfgInfoEntry,'hwCBQoSLrUnit':hwCBQoSLrUnit,'hwCBQoSLrCir':hwCBQoSLrCir,'hwCBQoSLrCbs':hwCBQoSLrCbs,'hwCBQoSLrEbs':hwCBQoSLrEbs,'hwCBQoSLrRowStatus':hwCBQoSLrRowStatus,'hwCBQoSNestPolicyCfgInfoTable':hwCBQoSNestPolicyCfgInfoTable,'hwCBQoSNestPolicyCfgInfoEntry':hwCBQoSNestPolicyCfgInfoEntry,'hwCBQoSNestPolicyName':hwCBQoSNestPolicyName,'hwCBQoSNestPolicyRowStatus':hwCBQoSNestPolicyRowStatus,'hwCBQoSPolicyObjects':hwCBQoSPolicyObjects,'hwCBQoSPolicyIndexNext':hwCBQoSPolicyIndexNext,'hwCBQoSPolicyCfgInfoTable':hwCBQoSPolicyCfgInfoTable,'hwCBQoSPolicyCfgInfoEntry':hwCBQoSPolicyCfgInfoEntry,_X:hwCBQoSPolicyIndex,'hwCBQoSPolicyName':hwCBQoSPolicyName,'hwCBQoSPolicyClassCount':hwCBQoSPolicyClassCount,'hwCBQoSPolicyConfigMode':hwCBQoSPolicyConfigMode,'hwCBQoSPolicyRowStatus':hwCBQoSPolicyRowStatus,'hwCBQoSPolicyClassCfgInfoTable':hwCBQoSPolicyClassCfgInfoTable,'hwCBQoSPolicyClassCfgInfoEntry':hwCBQoSPolicyClassCfgInfoEntry,_F:hwCBQoSPolicyClassIndex,'hwCBQoSPolicyClassClassifierIndex':hwCBQoSPolicyClassClassifierIndex,'hwCBQoSPolicyClassClassifierName':hwCBQoSPolicyClassClassifierName,'hwCBQoSPolicyClassBehaviorIndex':hwCBQoSPolicyClassBehaviorIndex,'hwCBQoSPolicyClassBehaviorName':hwCBQoSPolicyClassBehaviorName,'hwCBQoSPolicyClassPrecedence':hwCBQoSPolicyClassPrecedence,'hwCBQoSPolicyClassRowStatus':hwCBQoSPolicyClassRowStatus,'hwCBQoSApplyPolicyObjects':hwCBQoSApplyPolicyObjects,'hwCBQoSIfApplyPolicyTable':hwCBQoSIfApplyPolicyTable,'hwCBQoSIfApplyPolicyEntry':hwCBQoSIfApplyPolicyEntry,_J:hwCBQoSIfApplyPolicyIfIndex,_P:hwCBQoSIfApplyPolicyDirection,'hwCBQoSIfApplyPolicyName':hwCBQoSIfApplyPolicyName,'hwCBQoSIfApplyPolicyEnableDynamic':hwCBQoSIfApplyPolicyEnableDynamic,'hwCBQoSIfApplyPolicyRowStatus':hwCBQoSIfApplyPolicyRowStatus,'hwCBQoSAtmPvcApplyPolicyTable':hwCBQoSAtmPvcApplyPolicyTable,'hwCBQoSAtmPvcApplyPolicyEntry':hwCBQoSAtmPvcApplyPolicyEntry,_K:hwCBQoSAtmPvcApplyPolicyIfIndex,_L:hwCBQoSAtmPvcApplyPolicyVPI,_M:hwCBQoSAtmPvcApplyPolicyVCI,_Q:hwCBQoSAtmPvcApplyPolicyDirection,'hwCBQoSAtmPvcApplyPolicyName':hwCBQoSAtmPvcApplyPolicyName,'hwCBQoSAtmPvcApplyPolicyRowStatus':hwCBQoSAtmPvcApplyPolicyRowStatus,'hwCBQoSIfVlanApplyPolicyTable':hwCBQoSIfVlanApplyPolicyTable,'hwCBQoSIfVlanApplyPolicyEntry':hwCBQoSIfVlanApplyPolicyEntry,_Y:hwCBQoSIfVlanApplyPolicyIfIndex,_Z:hwCBQoSIfVlanApplyPolicyVlanid,_a:hwCBQoSIfVlanApplyPolicyDirection,'hwCBQoSIfVlanApplyPolicyName':hwCBQoSIfVlanApplyPolicyName,'hwCBQoSIfVlanApplyPolicyRowStatus':hwCBQoSIfVlanApplyPolicyRowStatus,'hwCBQoSFrClassApplyPolicyTable':hwCBQoSFrClassApplyPolicyTable,'hwCBQoSFrClassApplyPolicyEntry':hwCBQoSFrClassApplyPolicyEntry,_n:hwCBQoSFrClassApplyPolicyFrClassName,_o:hwCBQoSFrClassApplyPolicyDirection,'hwCBQoSFrClassApplyPolicyName':hwCBQoSFrClassApplyPolicyName,'hwCBQoSFrClassApplyPolicyRowStatus':hwCBQoSFrClassApplyPolicyRowStatus,'hwCBQoSFrPvcApplyPolicyTable':hwCBQoSFrPvcApplyPolicyTable,'hwCBQoSFrPvcApplyPolicyEntry':hwCBQoSFrPvcApplyPolicyEntry,_N:hwCBQoSFrPvcApplyPolicyIfIndex,_O:hwCBQoSFrPvcApplyPolicyDlciNum,_R:hwCBQoSFrPvcApplyPolicyDirection,'hwCBQoSFrPvcApplyPolicyName':hwCBQoSFrPvcApplyPolicyName,'hwCBQoSApplyPolicyStaticsObjects':hwCBQoSApplyPolicyStaticsObjects,'hwCBQoSIfStaticsObjects':hwCBQoSIfStaticsObjects,'hwCBQoSIfCbqRunInfoTable':hwCBQoSIfCbqRunInfoTable,'hwCBQoSIfCbqRunInfoEntry':hwCBQoSIfCbqRunInfoEntry,'hwCBQoSIfCbqQueueSize':hwCBQoSIfCbqQueueSize,'hwCBQoSIfCbqDiscard':hwCBQoSIfCbqDiscard,'hwCBQoSIfCbqEfQueueSize':hwCBQoSIfCbqEfQueueSize,'hwCBQoSIfCbqAfQueueSize':hwCBQoSIfCbqAfQueueSize,'hwCBQoSIfCbqBeQueueSize':hwCBQoSIfCbqBeQueueSize,'hwCBQoSIfCbqBeActiveQueueNum':hwCBQoSIfCbqBeActiveQueueNum,'hwCBQoSIfCbqBeMaxActiveQueueNum':hwCBQoSIfCbqBeMaxActiveQueueNum,'hwCBQoSIfCbqBeTotalQueueNum':hwCBQoSIfCbqBeTotalQueueNum,'hwCBQoSIfCbqAfAllocatedQueueNum':hwCBQoSIfCbqAfAllocatedQueueNum,'hwCBQoSIfClassMatchRunInfoTable':hwCBQoSIfClassMatchRunInfoTable,'hwCBQoSIfClassMatchRunInfoEntry':hwCBQoSIfClassMatchRunInfoEntry,'hwCBQoSIfClassMatchedPackets':hwCBQoSIfClassMatchedPackets,'hwCBQoSIfClassMatchedBytes':hwCBQoSIfClassMatchedBytes,'hwCBQoSIfClassAverageRate':hwCBQoSIfClassAverageRate,'hwCBQoSIfCarRunInfoTable':hwCBQoSIfCarRunInfoTable,'hwCBQoSIfCarRunInfoEntry':hwCBQoSIfCarRunInfoEntry,'hwCBQoSIfCarGreenPackets':hwCBQoSIfCarGreenPackets,'hwCBQoSIfCarGreenBytes':hwCBQoSIfCarGreenBytes,'hwCBQoSIfCarRedPackets':hwCBQoSIfCarRedPackets,'hwCBQoSIfCarRedBytes':hwCBQoSIfCarRedBytes,'hwCBQoSIfGtsRunInfoTable':hwCBQoSIfGtsRunInfoTable,'hwCBQoSIfGtsRunInfoEntry':hwCBQoSIfGtsRunInfoEntry,'hwCBQoSIfGtsPassedPackets':hwCBQoSIfGtsPassedPackets,'hwCBQoSIfGtsPassedBytes':hwCBQoSIfGtsPassedBytes,'hwCBQoSIfGtsDiscardedPackets':hwCBQoSIfGtsDiscardedPackets,'hwCBQoSIfGtsDiscardedBytes':hwCBQoSIfGtsDiscardedBytes,'hwCBQoSIfGtsDelayedPackets':hwCBQoSIfGtsDelayedPackets,'hwCBQoSIfGtsDelayedBytes':hwCBQoSIfGtsDelayedBytes,'hwCBQoSIfGtsQueueSize':hwCBQoSIfGtsQueueSize,'hwCBQoSIfRemarkRunInfoTable':hwCBQoSIfRemarkRunInfoTable,'hwCBQoSIfRemarkRunInfoEntry':hwCBQoSIfRemarkRunInfoEntry,'hwCBQoSIfRemarkedPackets':hwCBQoSIfRemarkedPackets,'hwCBQoSIfQueueRunInfoTable':hwCBQoSIfQueueRunInfoTable,'hwCBQoSIfQueueRunInfoEntry':hwCBQoSIfQueueRunInfoEntry,'hwCBQoSIfQueueMatchedPackets':hwCBQoSIfQueueMatchedPackets,'hwCBQoSIfQueueMatchedBytes':hwCBQoSIfQueueMatchedBytes,'hwCBQoSIfQueueEnqueuedPackets':hwCBQoSIfQueueEnqueuedPackets,'hwCBQoSIfQueueEnqueuedBytes':hwCBQoSIfQueueEnqueuedBytes,'hwCBQoSIfQueueDiscardedPackets':hwCBQoSIfQueueDiscardedPackets,'hwCBQoSIfQueueDiscardedBytes':hwCBQoSIfQueueDiscardedBytes,'hwCBQoSIfWredRunInfoTable':hwCBQoSIfWredRunInfoTable,'hwCBQoSIfWredRunInfoEntry':hwCBQoSIfWredRunInfoEntry,'hwCBQoSIfWredRandomDiscardedPackets':hwCBQoSIfWredRandomDiscardedPackets,'hwCBQoSIfWredTailDiscardedPackets':hwCBQoSIfWredTailDiscardedPackets,'hwCBQoSIfLrRunInfoTable':hwCBQoSIfLrRunInfoTable,'hwCBQoSIfLrRunInfoEntry':hwCBQoSIfLrRunInfoEntry,'hwCBQoSIfLrPassedPackets':hwCBQoSIfLrPassedPackets,'hwCBQoSIfLrPassedBytes':hwCBQoSIfLrPassedBytes,'hwCBQoSIfLrDiscardedPackets':hwCBQoSIfLrDiscardedPackets,'hwCBQoSIfLrDiscardedBytes':hwCBQoSIfLrDiscardedBytes,'hwCBQoSIfLrDelayedPackets':hwCBQoSIfLrDelayedPackets,'hwCBQoSIfLrDelayedBytes':hwCBQoSIfLrDelayedBytes,'hwCBQoSIfLrQueueSize':hwCBQoSIfLrQueueSize,'hwCBQoSAtmPvcStaticsObjects':hwCBQoSAtmPvcStaticsObjects,'hwCBQoSAtmPvcCbqRunInfoTable':hwCBQoSAtmPvcCbqRunInfoTable,'hwCBQoSAtmPvcCbqRunInfoEntry':hwCBQoSAtmPvcCbqRunInfoEntry,'hwCBQoSAtmPvcCbqQueueSize':hwCBQoSAtmPvcCbqQueueSize,'hwCBQoSAtmPvcCbqDiscard':hwCBQoSAtmPvcCbqDiscard,'hwCBQoSAtmPvcCbqEfQueueSize':hwCBQoSAtmPvcCbqEfQueueSize,'hwCBQoSAtmPvcCbqAfQueueSize':hwCBQoSAtmPvcCbqAfQueueSize,'hwCBQoSAtmPvcCbqBeQueueSize':hwCBQoSAtmPvcCbqBeQueueSize,'hwCBQoSAtmPvcCbqBeActiveQueueNum':hwCBQoSAtmPvcCbqBeActiveQueueNum,'hwCBQoSAtmPvcCbqBeMaxActiveQueueNum':hwCBQoSAtmPvcCbqBeMaxActiveQueueNum,'hwCBQoSAtmPvcCbqBeTotalQueueNum':hwCBQoSAtmPvcCbqBeTotalQueueNum,'hwCBQoSAtmPvcCbqAfAllocatedQueueNum':hwCBQoSAtmPvcCbqAfAllocatedQueueNum,'hwCBQoSAtmPvcClassMatchRunInfoTable':hwCBQoSAtmPvcClassMatchRunInfoTable,'hwCBQoSAtmPvcClassMatchRunInfoEntry':hwCBQoSAtmPvcClassMatchRunInfoEntry,'hwCBQoSAtmPvcClassMatchPackets':hwCBQoSAtmPvcClassMatchPackets,'hwCBQoSAtmPvcClassMatchBytes':hwCBQoSAtmPvcClassMatchBytes,'hwCBQoSAtmPvcClassAverageRate':hwCBQoSAtmPvcClassAverageRate,'hwCBQoSAtmPvcCarRunInfoTable':hwCBQoSAtmPvcCarRunInfoTable,'hwCBQoSAtmPvcCarRunInfoEntry':hwCBQoSAtmPvcCarRunInfoEntry,'hwCBQoSAtmPvcCarConformPackets':hwCBQoSAtmPvcCarConformPackets,'hwCBQoSAtmPvcCarConformBytes':hwCBQoSAtmPvcCarConformBytes,'hwCBQoSAtmPvcCarExceedPackets':hwCBQoSAtmPvcCarExceedPackets,'hwCBQoSAtmPvcCarExceedBytes':hwCBQoSAtmPvcCarExceedBytes,'hwCBQoSAtmPvcGtsRunInfoTable':hwCBQoSAtmPvcGtsRunInfoTable,'hwCBQoSAtmPvcGtsRunInfoEntry':hwCBQoSAtmPvcGtsRunInfoEntry,'hwCBQoSAtmPvcGtsPassedPackets':hwCBQoSAtmPvcGtsPassedPackets,'hwCBQoSAtmPvcGtsPassedBytes':hwCBQoSAtmPvcGtsPassedBytes,'hwCBQoSAtmPvcGtsDiscardedPackets':hwCBQoSAtmPvcGtsDiscardedPackets,'hwCBQoSAtmPvcGtsDiscardedBytes':hwCBQoSAtmPvcGtsDiscardedBytes,'hwCBQoSAtmPvcGtsDelayedPackets':hwCBQoSAtmPvcGtsDelayedPackets,'hwCBQoSAtmPvcGtsDelayedBytes':hwCBQoSAtmPvcGtsDelayedBytes,'hwCBQoSAtmPvcGtsQueueSize':hwCBQoSAtmPvcGtsQueueSize,'hwCBQoSAtmPvcRemarkRunInfoTable':hwCBQoSAtmPvcRemarkRunInfoTable,'hwCBQoSAtmPvcRemarkRunInfoEntry':hwCBQoSAtmPvcRemarkRunInfoEntry,'hwCBQoSAtmPvcRemarkedPackets':hwCBQoSAtmPvcRemarkedPackets,'hwCBQoSAtmPvcQueueRunInfoTable':hwCBQoSAtmPvcQueueRunInfoTable,'hwCBQoSAtmPvcQueueRunInfoEntry':hwCBQoSAtmPvcQueueRunInfoEntry,'hwCBQoSAtmPvcQueueMatchedPackets':hwCBQoSAtmPvcQueueMatchedPackets,'hwCBQoSAtmPvcQueueMatchedBytes':hwCBQoSAtmPvcQueueMatchedBytes,'hwCBQoSAtmPvcQueueEnqueuedPackets':hwCBQoSAtmPvcQueueEnqueuedPackets,'hwCBQoSAtmPvcQueueEnqueuedBytes':hwCBQoSAtmPvcQueueEnqueuedBytes,'hwCBQoSAtmPvcQueueDiscardedPackets':hwCBQoSAtmPvcQueueDiscardedPackets,'hwCBQoSAtmPvcQueueDiscardedBytes':hwCBQoSAtmPvcQueueDiscardedBytes,'hwCBQoSAtmPvcWredRunInfoTable':hwCBQoSAtmPvcWredRunInfoTable,'hwCBQoSAtmPvcWredRunInfoEntry':hwCBQoSAtmPvcWredRunInfoEntry,'hwCBQoSAtmPvcWredRandomDiscardedPackets':hwCBQoSAtmPvcWredRandomDiscardedPackets,'hwCBQoSAtmPvcWredTailDiscardedPackets':hwCBQoSAtmPvcWredTailDiscardedPackets,'hwCBQoSAtmPvcLrRunInfoTable':hwCBQoSAtmPvcLrRunInfoTable,'hwCBQoSAtmPvcLrRunInfoEntry':hwCBQoSAtmPvcLrRunInfoEntry,'hwCBQoSAtmPvcLrPassedPackets':hwCBQoSAtmPvcLrPassedPackets,'hwCBQoSAtmPvcLrPassedBytes':hwCBQoSAtmPvcLrPassedBytes,'hwCBQoSAtmPvcLrDiscardedPackets':hwCBQoSAtmPvcLrDiscardedPackets,'hwCBQoSAtmPvcLrDiscardedBytes':hwCBQoSAtmPvcLrDiscardedBytes,'hwCBQoSAtmPvcLrDelayedPackets':hwCBQoSAtmPvcLrDelayedPackets,'hwCBQoSAtmPvcLrDelayedBytes':hwCBQoSAtmPvcLrDelayedBytes,'hwCBQoSAtmPvcLrQueueSize':hwCBQoSAtmPvcLrQueueSize,'hwCBQoSFrPvcStaticsObjects':hwCBQoSFrPvcStaticsObjects,'hwCBQoSFrPvcCbqRunInfoTable':hwCBQoSFrPvcCbqRunInfoTable,'hwCBQoSFrPvcCbqRunInfoEntry':hwCBQoSFrPvcCbqRunInfoEntry,'hwCBQoSFrPvcCbqQueueSize':hwCBQoSFrPvcCbqQueueSize,'hwCBQoSFrPvcCbqDiscard':hwCBQoSFrPvcCbqDiscard,'hwCBQoSFrPvcCbqEfQueueSize':hwCBQoSFrPvcCbqEfQueueSize,'hwCBQoSFrPvcCbqAfQueueSize':hwCBQoSFrPvcCbqAfQueueSize,'hwCBQoSFrPvcCbqBeQueueSize':hwCBQoSFrPvcCbqBeQueueSize,'hwCBQoSFrPvcCbqBeActiveQueueNum':hwCBQoSFrPvcCbqBeActiveQueueNum,'hwCBQoSFrPvcCbqBeMaxActiveQueueNum':hwCBQoSFrPvcCbqBeMaxActiveQueueNum,'hwCBQoSFrPvcCbqBeTotalQueueNum':hwCBQoSFrPvcCbqBeTotalQueueNum,'hwCBQoSFrPvcCbqAfAllocatedQueueNum':hwCBQoSFrPvcCbqAfAllocatedQueueNum,'hwCBQoSFrPvcClassMatchRunInfoTable':hwCBQoSFrPvcClassMatchRunInfoTable,'hwCBQoSFrPvcClassMatchRunInfoEntry':hwCBQoSFrPvcClassMatchRunInfoEntry,'hwCBQoSFrPvcClassMatchedPackets':hwCBQoSFrPvcClassMatchedPackets,'hwCBQoSFrPvcClassMatchedBytes':hwCBQoSFrPvcClassMatchedBytes,'hwCBQoSFrPvcClassAverageRate':hwCBQoSFrPvcClassAverageRate,'hwCBQoSFrPvcCarRunInfoTable':hwCBQoSFrPvcCarRunInfoTable,'hwCBQoSFrPvcCarRunInfoEntry':hwCBQoSFrPvcCarRunInfoEntry,'hwCBQoSFrPvcCarConformPackets':hwCBQoSFrPvcCarConformPackets,'hwCBQoSFrPvcCarConformBytes':hwCBQoSFrPvcCarConformBytes,'hwCBQoSFrPvcCarExceedPackets':hwCBQoSFrPvcCarExceedPackets,'hwCBQoSFrPvcCarExceedBytes':hwCBQoSFrPvcCarExceedBytes,'hwCBQoSFrPvcGtsRunInfoTable':hwCBQoSFrPvcGtsRunInfoTable,'hwCBQoSFrPvcGtsRunInfoEntry':hwCBQoSFrPvcGtsRunInfoEntry,'hwCBQoSFrPvcGtsPassedPackets':hwCBQoSFrPvcGtsPassedPackets,'hwCBQoSFrPvcGtsPassedBytes':hwCBQoSFrPvcGtsPassedBytes,'hwCBQoSFrPvcGtsDiscardedPackets':hwCBQoSFrPvcGtsDiscardedPackets,'hwCBQoSFrPvcGtsDiscardedBytes':hwCBQoSFrPvcGtsDiscardedBytes,'hwCBQoSFrPvcGtsDelayedPackets':hwCBQoSFrPvcGtsDelayedPackets,'hwCBQoSFrPvcGtsDelayedBytes':hwCBQoSFrPvcGtsDelayedBytes,'hwCBQoSFrPvcGtsQueueSize':hwCBQoSFrPvcGtsQueueSize,'hwCBQoSFrPvcRemarkRunInfoTable':hwCBQoSFrPvcRemarkRunInfoTable,'hwCBQoSFrPvcRemarkRunInfoEntry':hwCBQoSFrPvcRemarkRunInfoEntry,'hwCBQoSFrPvcRemarkedPackets':hwCBQoSFrPvcRemarkedPackets,'hwCBQoSFrPvcQueueRunInfoTable':hwCBQoSFrPvcQueueRunInfoTable,'hwCBQoSFrPvcQueueRunInfoEntry':hwCBQoSFrPvcQueueRunInfoEntry,'hwCBQoSFrPvcQueueMatchedPackets':hwCBQoSFrPvcQueueMatchedPackets,'hwCBQoSFrPvcQueueMatchedBytes':hwCBQoSFrPvcQueueMatchedBytes,'hwCBQoSFrPvcQueueEnqueuedPackets':hwCBQoSFrPvcQueueEnqueuedPackets,'hwCBQoSFrPvcQueueEnqueuedBytes':hwCBQoSFrPvcQueueEnqueuedBytes,'hwCBQoSFrPvcQueueDiscardedPackets':hwCBQoSFrPvcQueueDiscardedPackets,'hwCBQoSFrPvcQueueDiscardedBytes':hwCBQoSFrPvcQueueDiscardedBytes,'hwCBQoSFrPvcWredRunInfoTable':hwCBQoSFrPvcWredRunInfoTable,'hwCBQoSFrPvcWredRunInfoEntry':hwCBQoSFrPvcWredRunInfoEntry,'hwCBQoSFrPvcWredRandomDiscardedPackets':hwCBQoSFrPvcWredRandomDiscardedPackets,'hwCBQoSFrPvcWredTailDiscardedPackets':hwCBQoSFrPvcWredTailDiscardedPackets,'hwCBQoSFrPvcLrRunInfoTable':hwCBQoSFrPvcLrRunInfoTable,'hwCBQoSFrPvcLrRunInfoEntry':hwCBQoSFrPvcLrRunInfoEntry,'hwCBQoSFrPvcLrPassedPackets':hwCBQoSFrPvcLrPassedPackets,'hwCBQoSFrPvcLrPassedBytes':hwCBQoSFrPvcLrPassedBytes,'hwCBQoSFrPvcLrDiscardedPackets':hwCBQoSFrPvcLrDiscardedPackets,'hwCBQoSFrPvcLrDiscardedBytes':hwCBQoSFrPvcLrDiscardedBytes,'hwCBQoSFrPvcLrDelayedPackets':hwCBQoSFrPvcLrDelayedPackets,'hwCBQoSFrPvcLrDelayedBytes':hwCBQoSFrPvcLrDelayedBytes,'hwCBQoSFrPvcLrQueueSize':hwCBQoSFrPvcLrQueueSize,'hwCBQoSIfVlanStaticsObjects':hwCBQoSIfVlanStaticsObjects,'hwCBQoSIfVlanClassMatchRunInfoTable':hwCBQoSIfVlanClassMatchRunInfoTable,'hwCBQoSIfVlanClassMatchRunInfoEntry':hwCBQoSIfVlanClassMatchRunInfoEntry,'hwCBQoSIfVlanClassMatchedPackets':hwCBQoSIfVlanClassMatchedPackets})