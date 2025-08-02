_AE='hpnicfCBQoSCpApplyObjectSlot'
_AD='hpnicfCBQoSCpApplyObjectChassis'
_AC='hpnicfCBQoSNestPolicyClassIndex'
_AB='hpnicfCBQoSPvcApplyObjectPvcID'
_AA='hpnicfCBQoSPvcApplyObjectIfIndex'
_A9='hpnicfCBQoSVlanApplyObjectVlanID'
_A8='hpnicfCBQoSIntApplyObjectIfIndex'
_A7='hpnicfCBQoSCpApplyPolicyDirection'
_A6='hpnicfCBQoSCpApplyPolicySlot'
_A5='hpnicfCBQoSCpApplyPolicyChassis'
_A4='hpnicfCBQoSGlobalApplyDirection'
_A3='hpnicfCBQoSFrClassApplyPolicyDirection'
_A2='hpnicfCBQoSFrClassApplyPolicyFrClassName'
_A1='hpnicfCBQoSPrePriMapTableType'
_A0='hpnicfCBQoSPrimapColorType'
_z='hpnicfCBQoSColoredRemarkColor'
_y='hpnicfCBQoSColoredRemarkType'
_x='active'
_w='inactive'
_v='hpnicfCBQoSMirrorIfMainIfIndex'
_u='dropPrecedence'
_t='localPrecedence'
_s='ipPrecedence'
_r='WredType'
_q='hpnicfCBQoSRemarkType'
_p='hpnicfCBQoSCarAggregativeCarIndex'
_o='InetAddressType'
_n='hpnicfCBQoSPolicyIndex'
_m='matchNot'
_l='match'
_k='userDefined'
_j='systemDefined'
_i='interface'
_h='Unsigned32'
_g='partialItemFailed'
_f='proccessing'
_e='accessible-for-notify'
_d='CarAction'
_c='hpnicfCBQoSMatchRuleIndex'
_b='unavailable'
_a='invalid'
_Z='hpnicfCBQoSApplyObjectDirection'
_Y='hpnicfCBQoSVlanApplyPolicyDirection'
_X='hpnicfCBQoSVlanApplyPolicyVlanid'
_W='success'
_V='read-write'
_U='hpnicfCBQoSClassifierIndex'
_T='hpnicfCBQoSWredClassValue'
_S='hpnicfCBQoSFrPvcApplyPolicyDirection'
_R='hpnicfCBQoSAtmPvcApplyPolicyDirection'
_Q='hpnicfCBQoSFrPvcApplyPolicyDlciNum'
_P='hpnicfCBQoSFrPvcApplyPolicyIfIndex'
_O='hpnicfCBQoSAtmPvcApplyPolicyVCI'
_N='hpnicfCBQoSAtmPvcApplyPolicyVPI'
_M='hpnicfCBQoSAtmPvcApplyPolicyIfIndex'
_L='hpnicfCBQoSIfApplyPolicyDirection'
_K='hpnicfCBQoSApplyObjectIndex'
_J='hpnicfCBQoSIfApplyPolicyIfIndex'
_I='OctetString'
_H='hpnicfCBQoSBehaviorIndex'
_G='hpnicfCBQoSPolicyClassIndex'
_F='not-accessible'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='HPN-ICF-CBQOS2-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_o)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_h,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
hpnicfCBQos2=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,2))
if mibBuilder.loadTexts:hpnicfCBQos2.setRevisions(('2012-07-02 00:00','2005-07-30 00:00'))
class MatchRuleType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33)));namedValues=NamedValues(*(('matchRuleAny',1),('matchRuleIpv4Acl',2),('matchRuleIPv6Acl',3),('matchRuleIPv4Protocol',4),('matchRuleIPv6Protocol',5),('matchRuleIPXProtocol',6),('matchRuleDscp',7),('matchRuleIpPre',8),('matchRuleVlan8021p',9),('matchRuleMplsExp',10),('matchRuleAtmClp',11),('matchRuleFrDe',12),('matchRuleSourceMac',13),('matchRuleDestinationMac',14),('matchRuleQosLocalID',15),('matchRuleClassifier',16),('matchRuleInboundInterface',17),('matchRuleRtpPort',18),('matchRuleSourceIp',19),('matchRuleVlanID',20),('matchRuleTopMostVlanID',21),('matchRuleLocalPrecedence',22),('matchRuleDropPriority',23),('matchRuleBittorrent',24),('matchRuleServiceDot1p',25),('matchRuleMplsLabel',26),('matchRuleSecondMplsLabel',27),('matchRuleSecondMplsExp',28),('matchRulePacketLength',29),('matchRuleArpProtocol',30),('matchRuleForwardingLayer',31),('matchRuleMacAcl',32),('matchRuleUserAcl',33)))
class CarAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18)));namedValues=NamedValues(*((_a,0),('pass',1),('continue',2),('discard',3),('remark',4),('remark-ip-continue',5),('remark-ip-pass',6),('remark-mplsexp-continue',7),('remark-mplsexp-pass',8),('remark-dscp-continue',9),('remark-dscp-pass',10),('remark-dot1p-continue',11),('remark-dot1p-pass',12),('remark-atm-clp-continue',13),('remark-atm-clp-pass',14),('remark-fr-de-continue',15),('remark-fr-de-pass',16),('remark-local-pre-pass',17),('remark-drop-pre-pass',18)))
class RemarkType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('typeIpPrecedence',1),('typeDscp',2),('typeMplsExp',3),('typeVlan8021p',4),('typeAtmClp',5),('typeFrDe',6),('typeVlanID',7),('typeQosLocalID',8),('typeDropPrecedence',9),('typeLocalPrecedence',10),('typeTopMostVlanID',11),('typeSecondMplsExp',12)))
class WredType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('typeIpPrecBased',1),('typeDscpBased',2),('typeDropLevelBased',3),('typeAtmClpBased',4),('typeVlan8021pBased',5),('typeMplsExpBased',6)))
class QueueType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ef',1),('af',2),('wfq',3)))
class QueueBandwidthUnit(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('unitUnavailable',0),('unitAbsolute',1),('unitPercent',2),('unitRemainPercent',3)))
class DirectionType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inbound',1),('outbound',2)))
class ApplyObjectType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_i,1),('vlan',2),('atmPvc',3),('frDlci',4),('controlPlane',5)))
_HpnicfQos2_ObjectIdentity=ObjectIdentity
hpnicfQos2=_HpnicfQos2_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65))
_HpnicfCBQoSObjects_ObjectIdentity=ObjectIdentity
hpnicfCBQoSObjects=_HpnicfCBQoSObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1))
_HpnicfCBQoSClassifierObjects_ObjectIdentity=ObjectIdentity
hpnicfCBQoSClassifierObjects=_HpnicfCBQoSClassifierObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1))
_HpnicfCBQoSClassifierIndexNext_Type=Integer32
_HpnicfCBQoSClassifierIndexNext_Object=MibScalar
hpnicfCBQoSClassifierIndexNext=_HpnicfCBQoSClassifierIndexNext_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,1),_HpnicfCBQoSClassifierIndexNext_Type())
hpnicfCBQoSClassifierIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSClassifierIndexNext.setStatus(_A)
_HpnicfCBQoSClassifierCfgInfoTable_Object=MibTable
hpnicfCBQoSClassifierCfgInfoTable=_HpnicfCBQoSClassifierCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,2))
if mibBuilder.loadTexts:hpnicfCBQoSClassifierCfgInfoTable.setStatus(_A)
_HpnicfCBQoSClassifierCfgInfoEntry_Object=MibTableRow
hpnicfCBQoSClassifierCfgInfoEntry=_HpnicfCBQoSClassifierCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,2,1))
hpnicfCBQoSClassifierCfgInfoEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:hpnicfCBQoSClassifierCfgInfoEntry.setStatus(_A)
_HpnicfCBQoSClassifierIndex_Type=Integer32
_HpnicfCBQoSClassifierIndex_Object=MibTableColumn
hpnicfCBQoSClassifierIndex=_HpnicfCBQoSClassifierIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,2,1,1),_HpnicfCBQoSClassifierIndex_Type())
hpnicfCBQoSClassifierIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSClassifierIndex.setStatus(_A)
class _HpnicfCBQoSClassifierName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HpnicfCBQoSClassifierName_Type.__name__=_I
_HpnicfCBQoSClassifierName_Object=MibTableColumn
hpnicfCBQoSClassifierName=_HpnicfCBQoSClassifierName_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,2,1,2),_HpnicfCBQoSClassifierName_Type())
hpnicfCBQoSClassifierName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSClassifierName.setStatus(_A)
_HpnicfCBQoSClassifierRuleCount_Type=Integer32
_HpnicfCBQoSClassifierRuleCount_Object=MibTableColumn
hpnicfCBQoSClassifierRuleCount=_HpnicfCBQoSClassifierRuleCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,2,1,3),_HpnicfCBQoSClassifierRuleCount_Type())
hpnicfCBQoSClassifierRuleCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSClassifierRuleCount.setStatus(_A)
class _HpnicfCBQoSClassifierOperator_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('and',1),('or',2)))
_HpnicfCBQoSClassifierOperator_Type.__name__=_E
_HpnicfCBQoSClassifierOperator_Object=MibTableColumn
hpnicfCBQoSClassifierOperator=_HpnicfCBQoSClassifierOperator_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,2,1,4),_HpnicfCBQoSClassifierOperator_Type())
hpnicfCBQoSClassifierOperator.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSClassifierOperator.setStatus(_A)
class _HpnicfCBQoSClassifierLayer_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_b,1),('l2',2),('l3',3),('both',4)))
_HpnicfCBQoSClassifierLayer_Type.__name__=_E
_HpnicfCBQoSClassifierLayer_Object=MibTableColumn
hpnicfCBQoSClassifierLayer=_HpnicfCBQoSClassifierLayer_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,2,1,5),_HpnicfCBQoSClassifierLayer_Type())
hpnicfCBQoSClassifierLayer.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSClassifierLayer.setStatus(_A)
class _HpnicfCBQoSClassifierType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_j,1),(_k,2)))
_HpnicfCBQoSClassifierType_Type.__name__=_E
_HpnicfCBQoSClassifierType_Object=MibTableColumn
hpnicfCBQoSClassifierType=_HpnicfCBQoSClassifierType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,2,1,6),_HpnicfCBQoSClassifierType_Type())
hpnicfCBQoSClassifierType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSClassifierType.setStatus(_A)
_HpnicfCBQosClassifierMatchRuleNextIndex_Type=Integer32
_HpnicfCBQosClassifierMatchRuleNextIndex_Object=MibTableColumn
hpnicfCBQosClassifierMatchRuleNextIndex=_HpnicfCBQosClassifierMatchRuleNextIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,2,1,7),_HpnicfCBQosClassifierMatchRuleNextIndex_Type())
hpnicfCBQosClassifierMatchRuleNextIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQosClassifierMatchRuleNextIndex.setStatus(_A)
_HpnicfCBQoSClassifierRowStatus_Type=RowStatus
_HpnicfCBQoSClassifierRowStatus_Object=MibTableColumn
hpnicfCBQoSClassifierRowStatus=_HpnicfCBQoSClassifierRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,2,1,8),_HpnicfCBQoSClassifierRowStatus_Type())
hpnicfCBQoSClassifierRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSClassifierRowStatus.setStatus(_A)
_HpnicfCBQoSMatchRuleCfgInfoTable_Object=MibTable
hpnicfCBQoSMatchRuleCfgInfoTable=_HpnicfCBQoSMatchRuleCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,3))
if mibBuilder.loadTexts:hpnicfCBQoSMatchRuleCfgInfoTable.setStatus(_A)
_HpnicfCBQoSMatchRuleCfgInfoEntry_Object=MibTableRow
hpnicfCBQoSMatchRuleCfgInfoEntry=_HpnicfCBQoSMatchRuleCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,3,1))
hpnicfCBQoSMatchRuleCfgInfoEntry.setIndexNames((0,_B,_U),(0,_B,_c))
if mibBuilder.loadTexts:hpnicfCBQoSMatchRuleCfgInfoEntry.setStatus(_A)
_HpnicfCBQoSMatchRuleIndex_Type=Integer32
_HpnicfCBQoSMatchRuleIndex_Object=MibTableColumn
hpnicfCBQoSMatchRuleIndex=_HpnicfCBQoSMatchRuleIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,3,1,1),_HpnicfCBQoSMatchRuleIndex_Type())
hpnicfCBQoSMatchRuleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSMatchRuleIndex.setStatus(_A)
class _HpnicfCBQoSMatchRuleIfNot_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_m,2)))
_HpnicfCBQoSMatchRuleIfNot_Type.__name__=_E
_HpnicfCBQoSMatchRuleIfNot_Object=MibTableColumn
hpnicfCBQoSMatchRuleIfNot=_HpnicfCBQoSMatchRuleIfNot_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,3,1,2),_HpnicfCBQoSMatchRuleIfNot_Type())
hpnicfCBQoSMatchRuleIfNot.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSMatchRuleIfNot.setStatus(_A)
_HpnicfCBQoSMatchRuleType_Type=MatchRuleType
_HpnicfCBQoSMatchRuleType_Object=MibTableColumn
hpnicfCBQoSMatchRuleType=_HpnicfCBQoSMatchRuleType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,3,1,3),_HpnicfCBQoSMatchRuleType_Type())
hpnicfCBQoSMatchRuleType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSMatchRuleType.setStatus(_A)
class _HpnicfCBQoSMatchRuleStringValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfCBQoSMatchRuleStringValue_Type.__name__=_I
_HpnicfCBQoSMatchRuleStringValue_Object=MibTableColumn
hpnicfCBQoSMatchRuleStringValue=_HpnicfCBQoSMatchRuleStringValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,3,1,4),_HpnicfCBQoSMatchRuleStringValue_Type())
hpnicfCBQoSMatchRuleStringValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSMatchRuleStringValue.setStatus(_A)
_HpnicfCBQoSMatchRuleIntValue1_Type=Unsigned32
_HpnicfCBQoSMatchRuleIntValue1_Object=MibTableColumn
hpnicfCBQoSMatchRuleIntValue1=_HpnicfCBQoSMatchRuleIntValue1_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,3,1,5),_HpnicfCBQoSMatchRuleIntValue1_Type())
hpnicfCBQoSMatchRuleIntValue1.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSMatchRuleIntValue1.setStatus(_A)
_HpnicfCBQoSMatchRuleIntValue2_Type=Unsigned32
_HpnicfCBQoSMatchRuleIntValue2_Object=MibTableColumn
hpnicfCBQoSMatchRuleIntValue2=_HpnicfCBQoSMatchRuleIntValue2_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,3,1,6),_HpnicfCBQoSMatchRuleIntValue2_Type())
hpnicfCBQoSMatchRuleIntValue2.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSMatchRuleIntValue2.setStatus(_A)
_HpnicfCBQoSMatchIpAddressType_Type=InetAddressType
_HpnicfCBQoSMatchIpAddressType_Object=MibTableColumn
hpnicfCBQoSMatchIpAddressType=_HpnicfCBQoSMatchIpAddressType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,3,1,7),_HpnicfCBQoSMatchIpAddressType_Type())
hpnicfCBQoSMatchIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSMatchIpAddressType.setStatus(_A)
_HpnicfCBQoSMatchIpAddress_Type=InetAddress
_HpnicfCBQoSMatchIpAddress_Object=MibTableColumn
hpnicfCBQoSMatchIpAddress=_HpnicfCBQoSMatchIpAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,3,1,8),_HpnicfCBQoSMatchIpAddress_Type())
hpnicfCBQoSMatchIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSMatchIpAddress.setStatus(_A)
_HpnicfCBQoSMatchRuleRowStatus_Type=RowStatus
_HpnicfCBQoSMatchRuleRowStatus_Object=MibTableColumn
hpnicfCBQoSMatchRuleRowStatus=_HpnicfCBQoSMatchRuleRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,3,1,9),_HpnicfCBQoSMatchRuleRowStatus_Type())
hpnicfCBQoSMatchRuleRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSMatchRuleRowStatus.setStatus(_A)
_HpnicfCBQoSMatchCpProtoCfgTable_Object=MibTable
hpnicfCBQoSMatchCpProtoCfgTable=_HpnicfCBQoSMatchCpProtoCfgTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,4))
if mibBuilder.loadTexts:hpnicfCBQoSMatchCpProtoCfgTable.setStatus(_A)
_HpnicfCBQoSMatchCpProtoCfgEntry_Object=MibTableRow
hpnicfCBQoSMatchCpProtoCfgEntry=_HpnicfCBQoSMatchCpProtoCfgEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,4,1))
hpnicfCBQoSMatchCpProtoCfgEntry.setIndexNames((0,_B,_U),(0,_B,_c))
if mibBuilder.loadTexts:hpnicfCBQoSMatchCpProtoCfgEntry.setStatus(_A)
class _HpnicfCBQoSMatchCpProtoIfNot_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_m,2)))
_HpnicfCBQoSMatchCpProtoIfNot_Type.__name__=_E
_HpnicfCBQoSMatchCpProtoIfNot_Object=MibTableColumn
hpnicfCBQoSMatchCpProtoIfNot=_HpnicfCBQoSMatchCpProtoIfNot_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,4,1,1),_HpnicfCBQoSMatchCpProtoIfNot_Type())
hpnicfCBQoSMatchCpProtoIfNot.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSMatchCpProtoIfNot.setStatus(_A)
class _HpnicfCBQoSMatchCpProtoValue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfCBQoSMatchCpProtoValue_Type.__name__=_I
_HpnicfCBQoSMatchCpProtoValue_Object=MibTableColumn
hpnicfCBQoSMatchCpProtoValue=_HpnicfCBQoSMatchCpProtoValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,4,1,2),_HpnicfCBQoSMatchCpProtoValue_Type())
hpnicfCBQoSMatchCpProtoValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSMatchCpProtoValue.setStatus(_A)
_HpnicfCBQoSMatchCpProtoRowStatus_Type=RowStatus
_HpnicfCBQoSMatchCpProtoRowStatus_Object=MibTableColumn
hpnicfCBQoSMatchCpProtoRowStatus=_HpnicfCBQoSMatchCpProtoRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,4,1,3),_HpnicfCBQoSMatchCpProtoRowStatus_Type())
hpnicfCBQoSMatchCpProtoRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSMatchCpProtoRowStatus.setStatus(_A)
_HpnicfCBQoSMatchCpGroupCfgTable_Object=MibTable
hpnicfCBQoSMatchCpGroupCfgTable=_HpnicfCBQoSMatchCpGroupCfgTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,5))
if mibBuilder.loadTexts:hpnicfCBQoSMatchCpGroupCfgTable.setStatus(_A)
_HpnicfCBQoSMatchCpGroupCfgEntry_Object=MibTableRow
hpnicfCBQoSMatchCpGroupCfgEntry=_HpnicfCBQoSMatchCpGroupCfgEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,5,1))
hpnicfCBQoSMatchCpGroupCfgEntry.setIndexNames((0,_B,_U),(0,_B,_c))
if mibBuilder.loadTexts:hpnicfCBQoSMatchCpGroupCfgEntry.setStatus(_A)
class _HpnicfCBQoSMatchCpGroupIfNot_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_m,2)))
_HpnicfCBQoSMatchCpGroupIfNot_Type.__name__=_E
_HpnicfCBQoSMatchCpGroupIfNot_Object=MibTableColumn
hpnicfCBQoSMatchCpGroupIfNot=_HpnicfCBQoSMatchCpGroupIfNot_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,5,1,1),_HpnicfCBQoSMatchCpGroupIfNot_Type())
hpnicfCBQoSMatchCpGroupIfNot.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSMatchCpGroupIfNot.setStatus(_A)
class _HpnicfCBQoSMatchCpGroupValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('critical',1),('important',2),('management',3),('normal',4),('redirect',5),('monitor',6),('exception',7)))
_HpnicfCBQoSMatchCpGroupValue_Type.__name__=_E
_HpnicfCBQoSMatchCpGroupValue_Object=MibTableColumn
hpnicfCBQoSMatchCpGroupValue=_HpnicfCBQoSMatchCpGroupValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,5,1,2),_HpnicfCBQoSMatchCpGroupValue_Type())
hpnicfCBQoSMatchCpGroupValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSMatchCpGroupValue.setStatus(_A)
_HpnicfCBQoSMatchCpGroupRowStatus_Type=RowStatus
_HpnicfCBQoSMatchCpGroupRowStatus_Object=MibTableColumn
hpnicfCBQoSMatchCpGroupRowStatus=_HpnicfCBQoSMatchCpGroupRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,1,5,1,3),_HpnicfCBQoSMatchCpGroupRowStatus_Type())
hpnicfCBQoSMatchCpGroupRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSMatchCpGroupRowStatus.setStatus(_A)
_HpnicfCBQoSBehaviorObjects_ObjectIdentity=ObjectIdentity
hpnicfCBQoSBehaviorObjects=_HpnicfCBQoSBehaviorObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2))
_HpnicfCBQoSBehaviorIndexNext_Type=Integer32
_HpnicfCBQoSBehaviorIndexNext_Object=MibScalar
hpnicfCBQoSBehaviorIndexNext=_HpnicfCBQoSBehaviorIndexNext_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,1),_HpnicfCBQoSBehaviorIndexNext_Type())
hpnicfCBQoSBehaviorIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSBehaviorIndexNext.setStatus(_A)
_HpnicfCBQoSBehaviorCfgInfoTable_Object=MibTable
hpnicfCBQoSBehaviorCfgInfoTable=_HpnicfCBQoSBehaviorCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,2))
if mibBuilder.loadTexts:hpnicfCBQoSBehaviorCfgInfoTable.setStatus(_A)
_HpnicfCBQoSBehaviorCfgInfoEntry_Object=MibTableRow
hpnicfCBQoSBehaviorCfgInfoEntry=_HpnicfCBQoSBehaviorCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,2,1))
hpnicfCBQoSBehaviorCfgInfoEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hpnicfCBQoSBehaviorCfgInfoEntry.setStatus(_A)
_HpnicfCBQoSBehaviorIndex_Type=Integer32
_HpnicfCBQoSBehaviorIndex_Object=MibTableColumn
hpnicfCBQoSBehaviorIndex=_HpnicfCBQoSBehaviorIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,2,1,1),_HpnicfCBQoSBehaviorIndex_Type())
hpnicfCBQoSBehaviorIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSBehaviorIndex.setStatus(_A)
class _HpnicfCBQoSBehaviorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HpnicfCBQoSBehaviorName_Type.__name__=_I
_HpnicfCBQoSBehaviorName_Object=MibTableColumn
hpnicfCBQoSBehaviorName=_HpnicfCBQoSBehaviorName_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,2,1,2),_HpnicfCBQoSBehaviorName_Type())
hpnicfCBQoSBehaviorName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSBehaviorName.setStatus(_A)
class _HpnicfCBQoSBehaviorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_j,1),(_k,2)))
_HpnicfCBQoSBehaviorType_Type.__name__=_E
_HpnicfCBQoSBehaviorType_Object=MibTableColumn
hpnicfCBQoSBehaviorType=_HpnicfCBQoSBehaviorType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,2,1,3),_HpnicfCBQoSBehaviorType_Type())
hpnicfCBQoSBehaviorType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSBehaviorType.setStatus(_A)
_HpnicfCBQoSBehaviorRowStatus_Type=RowStatus
_HpnicfCBQoSBehaviorRowStatus_Object=MibTableColumn
hpnicfCBQoSBehaviorRowStatus=_HpnicfCBQoSBehaviorRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,2,1,4),_HpnicfCBQoSBehaviorRowStatus_Type())
hpnicfCBQoSBehaviorRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSBehaviorRowStatus.setStatus(_A)
_HpnicfCBQoSCarCfgInfoTable_Object=MibTable
hpnicfCBQoSCarCfgInfoTable=_HpnicfCBQoSCarCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,3))
if mibBuilder.loadTexts:hpnicfCBQoSCarCfgInfoTable.setStatus(_A)
_HpnicfCBQoSCarCfgInfoEntry_Object=MibTableRow
hpnicfCBQoSCarCfgInfoEntry=_HpnicfCBQoSCarCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,3,1))
hpnicfCBQoSCarCfgInfoEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hpnicfCBQoSCarCfgInfoEntry.setStatus(_A)
_HpnicfCBQoSCarCir_Type=Unsigned32
_HpnicfCBQoSCarCir_Object=MibTableColumn
hpnicfCBQoSCarCir=_HpnicfCBQoSCarCir_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,3,1,1),_HpnicfCBQoSCarCir_Type())
hpnicfCBQoSCarCir.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSCarCir.setStatus(_A)
_HpnicfCBQoSCarCbs_Type=Unsigned32
_HpnicfCBQoSCarCbs_Object=MibTableColumn
hpnicfCBQoSCarCbs=_HpnicfCBQoSCarCbs_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,3,1,2),_HpnicfCBQoSCarCbs_Type())
hpnicfCBQoSCarCbs.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSCarCbs.setStatus(_A)
class _HpnicfCBQoSCarEbs_Type(Unsigned32):defaultValue=0
_HpnicfCBQoSCarEbs_Type.__name__=_h
_HpnicfCBQoSCarEbs_Object=MibTableColumn
hpnicfCBQoSCarEbs=_HpnicfCBQoSCarEbs_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,3,1,3),_HpnicfCBQoSCarEbs_Type())
hpnicfCBQoSCarEbs.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSCarEbs.setStatus(_A)
_HpnicfCBQoSCarPir_Type=Unsigned32
_HpnicfCBQoSCarPir_Object=MibTableColumn
hpnicfCBQoSCarPir=_HpnicfCBQoSCarPir_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,3,1,4),_HpnicfCBQoSCarPir_Type())
hpnicfCBQoSCarPir.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSCarPir.setStatus(_A)
_HpnicfCBQoSCarPbs_Type=Unsigned32
_HpnicfCBQoSCarPbs_Object=MibTableColumn
hpnicfCBQoSCarPbs=_HpnicfCBQoSCarPbs_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,3,1,5),_HpnicfCBQoSCarPbs_Type())
hpnicfCBQoSCarPbs.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSCarPbs.setStatus(_A)
class _HpnicfCBQoSCarGreenAction_Type(CarAction):defaultValue=1
_HpnicfCBQoSCarGreenAction_Type.__name__=_d
_HpnicfCBQoSCarGreenAction_Object=MibTableColumn
hpnicfCBQoSCarGreenAction=_HpnicfCBQoSCarGreenAction_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,3,1,6),_HpnicfCBQoSCarGreenAction_Type())
hpnicfCBQoSCarGreenAction.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSCarGreenAction.setStatus(_A)
class _HpnicfCBQoSCarGreenRemarkValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HpnicfCBQoSCarGreenRemarkValue_Type.__name__=_E
_HpnicfCBQoSCarGreenRemarkValue_Object=MibTableColumn
hpnicfCBQoSCarGreenRemarkValue=_HpnicfCBQoSCarGreenRemarkValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,3,1,7),_HpnicfCBQoSCarGreenRemarkValue_Type())
hpnicfCBQoSCarGreenRemarkValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSCarGreenRemarkValue.setStatus(_A)
class _HpnicfCBQoSCarYellowAction_Type(CarAction):defaultValue=4
_HpnicfCBQoSCarYellowAction_Type.__name__=_d
_HpnicfCBQoSCarYellowAction_Object=MibTableColumn
hpnicfCBQoSCarYellowAction=_HpnicfCBQoSCarYellowAction_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,3,1,8),_HpnicfCBQoSCarYellowAction_Type())
hpnicfCBQoSCarYellowAction.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSCarYellowAction.setStatus(_A)
class _HpnicfCBQoSCarYellowRemarkValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HpnicfCBQoSCarYellowRemarkValue_Type.__name__=_E
_HpnicfCBQoSCarYellowRemarkValue_Object=MibTableColumn
hpnicfCBQoSCarYellowRemarkValue=_HpnicfCBQoSCarYellowRemarkValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,3,1,9),_HpnicfCBQoSCarYellowRemarkValue_Type())
hpnicfCBQoSCarYellowRemarkValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSCarYellowRemarkValue.setStatus(_A)
class _HpnicfCBQoSCarRedAction_Type(CarAction):defaultValue=3
_HpnicfCBQoSCarRedAction_Type.__name__=_d
_HpnicfCBQoSCarRedAction_Object=MibTableColumn
hpnicfCBQoSCarRedAction=_HpnicfCBQoSCarRedAction_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,3,1,10),_HpnicfCBQoSCarRedAction_Type())
hpnicfCBQoSCarRedAction.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSCarRedAction.setStatus(_A)
class _HpnicfCBQoSCarRedRemarkValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HpnicfCBQoSCarRedRemarkValue_Type.__name__=_E
_HpnicfCBQoSCarRedRemarkValue_Object=MibTableColumn
hpnicfCBQoSCarRedRemarkValue=_HpnicfCBQoSCarRedRemarkValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,3,1,11),_HpnicfCBQoSCarRedRemarkValue_Type())
hpnicfCBQoSCarRedRemarkValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSCarRedRemarkValue.setStatus(_A)
class _HpnicfCBQoSCarPolicedPriorityMapType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('policed-service-map',1),('local-precedence-dot1p-map',2),('drop-precedence-map',3)))
_HpnicfCBQoSCarPolicedPriorityMapType_Type.__name__=_E
_HpnicfCBQoSCarPolicedPriorityMapType_Object=MibTableColumn
hpnicfCBQoSCarPolicedPriorityMapType=_HpnicfCBQoSCarPolicedPriorityMapType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,3,1,12),_HpnicfCBQoSCarPolicedPriorityMapType_Type())
hpnicfCBQoSCarPolicedPriorityMapType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSCarPolicedPriorityMapType.setStatus(_A)
_HpnicfCBQoSCarRowStatus_Type=RowStatus
_HpnicfCBQoSCarRowStatus_Object=MibTableColumn
hpnicfCBQoSCarRowStatus=_HpnicfCBQoSCarRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,3,1,13),_HpnicfCBQoSCarRowStatus_Type())
hpnicfCBQoSCarRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSCarRowStatus.setStatus(_A)
_HpnicfCBQoSAggregativeCarCfgInfoTable_Object=MibTable
hpnicfCBQoSAggregativeCarCfgInfoTable=_HpnicfCBQoSAggregativeCarCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,4))
if mibBuilder.loadTexts:hpnicfCBQoSAggregativeCarCfgInfoTable.setStatus(_A)
_HpnicfCBQoSAggregativeCarCfgInfoEntry_Object=MibTableRow
hpnicfCBQoSAggregativeCarCfgInfoEntry=_HpnicfCBQoSAggregativeCarCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,4,1))
hpnicfCBQoSAggregativeCarCfgInfoEntry.setIndexNames((0,_B,_H),(0,_B,_p))
if mibBuilder.loadTexts:hpnicfCBQoSAggregativeCarCfgInfoEntry.setStatus(_A)
_HpnicfCBQoSCarAggregativeCarIndex_Type=Integer32
_HpnicfCBQoSCarAggregativeCarIndex_Object=MibTableColumn
hpnicfCBQoSCarAggregativeCarIndex=_HpnicfCBQoSCarAggregativeCarIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,4,1,1),_HpnicfCBQoSCarAggregativeCarIndex_Type())
hpnicfCBQoSCarAggregativeCarIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSCarAggregativeCarIndex.setStatus(_A)
class _HpnicfCBQoSCarAggregativeCarName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HpnicfCBQoSCarAggregativeCarName_Type.__name__=_I
_HpnicfCBQoSCarAggregativeCarName_Object=MibTableColumn
hpnicfCBQoSCarAggregativeCarName=_HpnicfCBQoSCarAggregativeCarName_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,4,1,2),_HpnicfCBQoSCarAggregativeCarName_Type())
hpnicfCBQoSCarAggregativeCarName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSCarAggregativeCarName.setStatus(_A)
_HpnicfCBQoSAggregativeCarRowStatus_Type=RowStatus
_HpnicfCBQoSAggregativeCarRowStatus_Object=MibTableColumn
hpnicfCBQoSAggregativeCarRowStatus=_HpnicfCBQoSAggregativeCarRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,4,1,3),_HpnicfCBQoSAggregativeCarRowStatus_Type())
hpnicfCBQoSAggregativeCarRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSAggregativeCarRowStatus.setStatus(_A)
_HpnicfCBQoSGtsCfgInfoTable_Object=MibTable
hpnicfCBQoSGtsCfgInfoTable=_HpnicfCBQoSGtsCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,5))
if mibBuilder.loadTexts:hpnicfCBQoSGtsCfgInfoTable.setStatus(_A)
_HpnicfCBQoSGtsCfgInfoEntry_Object=MibTableRow
hpnicfCBQoSGtsCfgInfoEntry=_HpnicfCBQoSGtsCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,5,1))
hpnicfCBQoSGtsCfgInfoEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hpnicfCBQoSGtsCfgInfoEntry.setStatus(_A)
_HpnicfCBQoSGtsCir_Type=Unsigned32
_HpnicfCBQoSGtsCir_Object=MibTableColumn
hpnicfCBQoSGtsCir=_HpnicfCBQoSGtsCir_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,5,1,1),_HpnicfCBQoSGtsCir_Type())
hpnicfCBQoSGtsCir.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSGtsCir.setStatus(_A)
_HpnicfCBQoSGtsCbs_Type=Unsigned32
_HpnicfCBQoSGtsCbs_Object=MibTableColumn
hpnicfCBQoSGtsCbs=_HpnicfCBQoSGtsCbs_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,5,1,2),_HpnicfCBQoSGtsCbs_Type())
hpnicfCBQoSGtsCbs.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSGtsCbs.setStatus(_A)
_HpnicfCBQoSGtsEbs_Type=Unsigned32
_HpnicfCBQoSGtsEbs_Object=MibTableColumn
hpnicfCBQoSGtsEbs=_HpnicfCBQoSGtsEbs_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,5,1,3),_HpnicfCBQoSGtsEbs_Type())
hpnicfCBQoSGtsEbs.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSGtsEbs.setStatus(_A)
class _HpnicfCBQoSGtsQueueLength_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_HpnicfCBQoSGtsQueueLength_Type.__name__=_E
_HpnicfCBQoSGtsQueueLength_Object=MibTableColumn
hpnicfCBQoSGtsQueueLength=_HpnicfCBQoSGtsQueueLength_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,5,1,4),_HpnicfCBQoSGtsQueueLength_Type())
hpnicfCBQoSGtsQueueLength.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSGtsQueueLength.setStatus(_A)
_HpnicfCBQoSGtsRowStatus_Type=RowStatus
_HpnicfCBQoSGtsRowStatus_Object=MibTableColumn
hpnicfCBQoSGtsRowStatus=_HpnicfCBQoSGtsRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,5,1,5),_HpnicfCBQoSGtsRowStatus_Type())
hpnicfCBQoSGtsRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSGtsRowStatus.setStatus(_A)
_HpnicfCBQoSGtsPir_Type=Unsigned32
_HpnicfCBQoSGtsPir_Object=MibTableColumn
hpnicfCBQoSGtsPir=_HpnicfCBQoSGtsPir_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,5,1,6),_HpnicfCBQoSGtsPir_Type())
hpnicfCBQoSGtsPir.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSGtsPir.setStatus(_A)
if mibBuilder.loadTexts:hpnicfCBQoSGtsPir.setUnits('kbps')
_HpnicfCBQoSRemarkCfgInfoTable_Object=MibTable
hpnicfCBQoSRemarkCfgInfoTable=_HpnicfCBQoSRemarkCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,6))
if mibBuilder.loadTexts:hpnicfCBQoSRemarkCfgInfoTable.setStatus(_A)
_HpnicfCBQoSRemarkCfgInfoEntry_Object=MibTableRow
hpnicfCBQoSRemarkCfgInfoEntry=_HpnicfCBQoSRemarkCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,6,1))
hpnicfCBQoSRemarkCfgInfoEntry.setIndexNames((0,_B,_H),(0,_B,_q))
if mibBuilder.loadTexts:hpnicfCBQoSRemarkCfgInfoEntry.setStatus(_A)
_HpnicfCBQoSRemarkType_Type=RemarkType
_HpnicfCBQoSRemarkType_Object=MibTableColumn
hpnicfCBQoSRemarkType=_HpnicfCBQoSRemarkType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,6,1,1),_HpnicfCBQoSRemarkType_Type())
hpnicfCBQoSRemarkType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSRemarkType.setStatus(_A)
class _HpnicfCBQoSRemarkValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_HpnicfCBQoSRemarkValue_Type.__name__=_E
_HpnicfCBQoSRemarkValue_Object=MibTableColumn
hpnicfCBQoSRemarkValue=_HpnicfCBQoSRemarkValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,6,1,2),_HpnicfCBQoSRemarkValue_Type())
hpnicfCBQoSRemarkValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSRemarkValue.setStatus(_A)
_HpnicfCBQoSRemarkRowStatus_Type=RowStatus
_HpnicfCBQoSRemarkRowStatus_Object=MibTableColumn
hpnicfCBQoSRemarkRowStatus=_HpnicfCBQoSRemarkRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,6,1,3),_HpnicfCBQoSRemarkRowStatus_Type())
hpnicfCBQoSRemarkRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSRemarkRowStatus.setStatus(_A)
_HpnicfCBQoSQueueCfgInfoTable_Object=MibTable
hpnicfCBQoSQueueCfgInfoTable=_HpnicfCBQoSQueueCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,7))
if mibBuilder.loadTexts:hpnicfCBQoSQueueCfgInfoTable.setStatus(_A)
_HpnicfCBQoSQueueCfgInfoEntry_Object=MibTableRow
hpnicfCBQoSQueueCfgInfoEntry=_HpnicfCBQoSQueueCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,7,1))
hpnicfCBQoSQueueCfgInfoEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hpnicfCBQoSQueueCfgInfoEntry.setStatus(_A)
_HpnicfCBQoSQueueType_Type=QueueType
_HpnicfCBQoSQueueType_Object=MibTableColumn
hpnicfCBQoSQueueType=_HpnicfCBQoSQueueType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,7,1,1),_HpnicfCBQoSQueueType_Type())
hpnicfCBQoSQueueType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSQueueType.setStatus(_A)
class _HpnicfCBQoSQueueDropType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('typeUnavailable',0),('typeTailDrop',1),('typeWred',2)))
_HpnicfCBQoSQueueDropType_Type.__name__=_E
_HpnicfCBQoSQueueDropType_Object=MibTableColumn
hpnicfCBQoSQueueDropType=_HpnicfCBQoSQueueDropType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,7,1,2),_HpnicfCBQoSQueueDropType_Type())
hpnicfCBQoSQueueDropType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSQueueDropType.setStatus(_A)
class _HpnicfCBQoSQueueLength_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfCBQoSQueueLength_Type.__name__=_E
_HpnicfCBQoSQueueLength_Object=MibTableColumn
hpnicfCBQoSQueueLength=_HpnicfCBQoSQueueLength_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,7,1,3),_HpnicfCBQoSQueueLength_Type())
hpnicfCBQoSQueueLength.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSQueueLength.setStatus(_A)
_HpnicfCBQoSQueueBandwidthUnit_Type=QueueBandwidthUnit
_HpnicfCBQoSQueueBandwidthUnit_Object=MibTableColumn
hpnicfCBQoSQueueBandwidthUnit=_HpnicfCBQoSQueueBandwidthUnit_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,7,1,4),_HpnicfCBQoSQueueBandwidthUnit_Type())
hpnicfCBQoSQueueBandwidthUnit.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSQueueBandwidthUnit.setStatus(_A)
class _HpnicfCBQoSQueueBandwidthValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000000),ValueRangeConstraint(2147483647,2147483647))
_HpnicfCBQoSQueueBandwidthValue_Type.__name__=_E
_HpnicfCBQoSQueueBandwidthValue_Object=MibTableColumn
hpnicfCBQoSQueueBandwidthValue=_HpnicfCBQoSQueueBandwidthValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,7,1,5),_HpnicfCBQoSQueueBandwidthValue_Type())
hpnicfCBQoSQueueBandwidthValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSQueueBandwidthValue.setStatus(_A)
class _HpnicfCBQoSQueueCbs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(32,1000000000),ValueRangeConstraint(2147483647,2147483647))
_HpnicfCBQoSQueueCbs_Type.__name__=_E
_HpnicfCBQoSQueueCbs_Object=MibTableColumn
hpnicfCBQoSQueueCbs=_HpnicfCBQoSQueueCbs_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,7,1,6),_HpnicfCBQoSQueueCbs_Type())
hpnicfCBQoSQueueCbs.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSQueueCbs.setStatus(_A)
class _HpnicfCBQoSQueueQueueNumber_Type(Integer32):defaultValue=256;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,16,32,64,128,256,512,1024,2048,4096)));namedValues=NamedValues(*((_b,0),('a16',16),('a32',32),('a64',64),('a128',128),('a256',256),('a512',512),('a1024',1024),('a2048',2048),('a4096',4096)))
_HpnicfCBQoSQueueQueueNumber_Type.__name__=_E
_HpnicfCBQoSQueueQueueNumber_Object=MibTableColumn
hpnicfCBQoSQueueQueueNumber=_HpnicfCBQoSQueueQueueNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,7,1,7),_HpnicfCBQoSQueueQueueNumber_Type())
hpnicfCBQoSQueueQueueNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSQueueQueueNumber.setStatus(_A)
class _HpnicfCBQoSQueueCbsRatio_Type(Integer32):defaultValue=25;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(25,500),ValueRangeConstraint(2147483647,2147483647))
_HpnicfCBQoSQueueCbsRatio_Type.__name__=_E
_HpnicfCBQoSQueueCbsRatio_Object=MibTableColumn
hpnicfCBQoSQueueCbsRatio=_HpnicfCBQoSQueueCbsRatio_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,7,1,8),_HpnicfCBQoSQueueCbsRatio_Type())
hpnicfCBQoSQueueCbsRatio.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSQueueCbsRatio.setStatus(_A)
_HpnicfCBQoSQueueRowStatus_Type=RowStatus
_HpnicfCBQoSQueueRowStatus_Object=MibTableColumn
hpnicfCBQoSQueueRowStatus=_HpnicfCBQoSQueueRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,7,1,9),_HpnicfCBQoSQueueRowStatus_Type())
hpnicfCBQoSQueueRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSQueueRowStatus.setStatus(_A)
_HpnicfCBQoSWredCfgInfoTable_Object=MibTable
hpnicfCBQoSWredCfgInfoTable=_HpnicfCBQoSWredCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,8))
if mibBuilder.loadTexts:hpnicfCBQoSWredCfgInfoTable.setStatus(_A)
_HpnicfCBQoSWredCfgInfoEntry_Object=MibTableRow
hpnicfCBQoSWredCfgInfoEntry=_HpnicfCBQoSWredCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,8,1))
hpnicfCBQoSWredCfgInfoEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hpnicfCBQoSWredCfgInfoEntry.setStatus(_A)
class _HpnicfCBQoSWredType_Type(WredType):defaultValue=1
_HpnicfCBQoSWredType_Type.__name__=_r
_HpnicfCBQoSWredType_Object=MibTableColumn
hpnicfCBQoSWredType=_HpnicfCBQoSWredType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,8,1,1),_HpnicfCBQoSWredType_Type())
hpnicfCBQoSWredType.setMaxAccess(_V)
if mibBuilder.loadTexts:hpnicfCBQoSWredType.setStatus(_A)
class _HpnicfCBQoSWredWeightConst_Type(Integer32):defaultValue=9;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HpnicfCBQoSWredWeightConst_Type.__name__=_E
_HpnicfCBQoSWredWeightConst_Object=MibTableColumn
hpnicfCBQoSWredWeightConst=_HpnicfCBQoSWredWeightConst_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,8,1,2),_HpnicfCBQoSWredWeightConst_Type())
hpnicfCBQoSWredWeightConst.setMaxAccess(_V)
if mibBuilder.loadTexts:hpnicfCBQoSWredWeightConst.setStatus(_A)
_HpnicfCBQoSWredClassCfgInfoTable_Object=MibTable
hpnicfCBQoSWredClassCfgInfoTable=_HpnicfCBQoSWredClassCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,9))
if mibBuilder.loadTexts:hpnicfCBQoSWredClassCfgInfoTable.setStatus(_A)
_HpnicfCBQoSWredClassCfgInfoEntry_Object=MibTableRow
hpnicfCBQoSWredClassCfgInfoEntry=_HpnicfCBQoSWredClassCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,9,1))
hpnicfCBQoSWredClassCfgInfoEntry.setIndexNames((0,_B,_H),(0,_B,_T))
if mibBuilder.loadTexts:hpnicfCBQoSWredClassCfgInfoEntry.setStatus(_A)
class _HpnicfCBQoSWredClassValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HpnicfCBQoSWredClassValue_Type.__name__=_E
_HpnicfCBQoSWredClassValue_Object=MibTableColumn
hpnicfCBQoSWredClassValue=_HpnicfCBQoSWredClassValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,9,1,1),_HpnicfCBQoSWredClassValue_Type())
hpnicfCBQoSWredClassValue.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSWredClassValue.setStatus(_A)
class _HpnicfCBQoSWredClassLowLimit_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_HpnicfCBQoSWredClassLowLimit_Type.__name__=_E
_HpnicfCBQoSWredClassLowLimit_Object=MibTableColumn
hpnicfCBQoSWredClassLowLimit=_HpnicfCBQoSWredClassLowLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,9,1,2),_HpnicfCBQoSWredClassLowLimit_Type())
hpnicfCBQoSWredClassLowLimit.setMaxAccess(_V)
if mibBuilder.loadTexts:hpnicfCBQoSWredClassLowLimit.setStatus(_A)
class _HpnicfCBQoSWredClassHighLimit_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_HpnicfCBQoSWredClassHighLimit_Type.__name__=_E
_HpnicfCBQoSWredClassHighLimit_Object=MibTableColumn
hpnicfCBQoSWredClassHighLimit=_HpnicfCBQoSWredClassHighLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,9,1,3),_HpnicfCBQoSWredClassHighLimit_Type())
hpnicfCBQoSWredClassHighLimit.setMaxAccess(_V)
if mibBuilder.loadTexts:hpnicfCBQoSWredClassHighLimit.setStatus(_A)
class _HpnicfCBQoSWredClassDiscardProb_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpnicfCBQoSWredClassDiscardProb_Type.__name__=_E
_HpnicfCBQoSWredClassDiscardProb_Object=MibTableColumn
hpnicfCBQoSWredClassDiscardProb=_HpnicfCBQoSWredClassDiscardProb_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,9,1,4),_HpnicfCBQoSWredClassDiscardProb_Type())
hpnicfCBQoSWredClassDiscardProb.setMaxAccess(_V)
if mibBuilder.loadTexts:hpnicfCBQoSWredClassDiscardProb.setStatus(_A)
_HpnicfCBQoSPolicyRouteCfgInfoTable_Object=MibTable
hpnicfCBQoSPolicyRouteCfgInfoTable=_HpnicfCBQoSPolicyRouteCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,10))
if mibBuilder.loadTexts:hpnicfCBQoSPolicyRouteCfgInfoTable.setStatus(_A)
_HpnicfCBQoSPolicyRouteCfgInfoEntry_Object=MibTableRow
hpnicfCBQoSPolicyRouteCfgInfoEntry=_HpnicfCBQoSPolicyRouteCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,10,1))
hpnicfCBQoSPolicyRouteCfgInfoEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hpnicfCBQoSPolicyRouteCfgInfoEntry.setStatus(_A)
_HpnicfCBQoSPolicyRouteIpAddrType_Type=InetAddressType
_HpnicfCBQoSPolicyRouteIpAddrType_Object=MibTableColumn
hpnicfCBQoSPolicyRouteIpAddrType=_HpnicfCBQoSPolicyRouteIpAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,10,1,1),_HpnicfCBQoSPolicyRouteIpAddrType_Type())
hpnicfCBQoSPolicyRouteIpAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSPolicyRouteIpAddrType.setStatus(_A)
_HpnicfCBQoSPolicyRouteNexthop_Type=InetAddress
_HpnicfCBQoSPolicyRouteNexthop_Object=MibTableColumn
hpnicfCBQoSPolicyRouteNexthop=_HpnicfCBQoSPolicyRouteNexthop_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,10,1,2),_HpnicfCBQoSPolicyRouteNexthop_Type())
hpnicfCBQoSPolicyRouteNexthop.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSPolicyRouteNexthop.setStatus(_A)
class _HpnicfCBQoSPolicyRouteBackup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('backup',1),('notbackup',2)))
_HpnicfCBQoSPolicyRouteBackup_Type.__name__=_E
_HpnicfCBQoSPolicyRouteBackup_Object=MibTableColumn
hpnicfCBQoSPolicyRouteBackup=_HpnicfCBQoSPolicyRouteBackup_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,10,1,3),_HpnicfCBQoSPolicyRouteBackup_Type())
hpnicfCBQoSPolicyRouteBackup.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSPolicyRouteBackup.setStatus(_A)
_HpnicfCBQoSPolicyRouteRowStatus_Type=RowStatus
_HpnicfCBQoSPolicyRouteRowStatus_Object=MibTableColumn
hpnicfCBQoSPolicyRouteRowStatus=_HpnicfCBQoSPolicyRouteRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,10,1,4),_HpnicfCBQoSPolicyRouteRowStatus_Type())
hpnicfCBQoSPolicyRouteRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSPolicyRouteRowStatus.setStatus(_A)
_HpnicfCBQoSNatCfgInfoTable_Object=MibTable
hpnicfCBQoSNatCfgInfoTable=_HpnicfCBQoSNatCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,11))
if mibBuilder.loadTexts:hpnicfCBQoSNatCfgInfoTable.setStatus(_A)
_HpnicfCBQoSNatCfgInfoEntry_Object=MibTableRow
hpnicfCBQoSNatCfgInfoEntry=_HpnicfCBQoSNatCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,11,1))
hpnicfCBQoSNatCfgInfoEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hpnicfCBQoSNatCfgInfoEntry.setStatus(_A)
class _HpnicfCBQoSNatMainNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpnicfCBQoSNatMainNumber_Type.__name__=_E
_HpnicfCBQoSNatMainNumber_Object=MibTableColumn
hpnicfCBQoSNatMainNumber=_HpnicfCBQoSNatMainNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,11,1,1),_HpnicfCBQoSNatMainNumber_Type())
hpnicfCBQoSNatMainNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSNatMainNumber.setStatus(_A)
class _HpnicfCBQoSNatBackupNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_HpnicfCBQoSNatBackupNumber_Type.__name__=_E
_HpnicfCBQoSNatBackupNumber_Object=MibTableColumn
hpnicfCBQoSNatBackupNumber=_HpnicfCBQoSNatBackupNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,11,1,2),_HpnicfCBQoSNatBackupNumber_Type())
hpnicfCBQoSNatBackupNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSNatBackupNumber.setStatus(_A)
class _HpnicfCBQoSNatServiceClass_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_HpnicfCBQoSNatServiceClass_Type.__name__=_E
_HpnicfCBQoSNatServiceClass_Object=MibTableColumn
hpnicfCBQoSNatServiceClass=_HpnicfCBQoSNatServiceClass_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,11,1,3),_HpnicfCBQoSNatServiceClass_Type())
hpnicfCBQoSNatServiceClass.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSNatServiceClass.setStatus(_A)
_HpnicfCBQoSNatRowStatus_Type=RowStatus
_HpnicfCBQoSNatRowStatus_Object=MibTableColumn
hpnicfCBQoSNatRowStatus=_HpnicfCBQoSNatRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,11,1,4),_HpnicfCBQoSNatRowStatus_Type())
hpnicfCBQoSNatRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSNatRowStatus.setStatus(_A)
_HpnicfCBQoSFirewallCfgInfoTable_Object=MibTable
hpnicfCBQoSFirewallCfgInfoTable=_HpnicfCBQoSFirewallCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,12))
if mibBuilder.loadTexts:hpnicfCBQoSFirewallCfgInfoTable.setStatus(_A)
_HpnicfCBQoSFirewallCfgInfoEntry_Object=MibTableRow
hpnicfCBQoSFirewallCfgInfoEntry=_HpnicfCBQoSFirewallCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,12,1))
hpnicfCBQoSFirewallCfgInfoEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hpnicfCBQoSFirewallCfgInfoEntry.setStatus(_A)
class _HpnicfCBQoSFirewallAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('permit',1),('deny',2)))
_HpnicfCBQoSFirewallAction_Type.__name__=_E
_HpnicfCBQoSFirewallAction_Object=MibTableColumn
hpnicfCBQoSFirewallAction=_HpnicfCBQoSFirewallAction_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,12,1,1),_HpnicfCBQoSFirewallAction_Type())
hpnicfCBQoSFirewallAction.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSFirewallAction.setStatus(_A)
_HpnicfCBQoSFirewallRowStatus_Type=RowStatus
_HpnicfCBQoSFirewallRowStatus_Object=MibTableColumn
hpnicfCBQoSFirewallRowStatus=_HpnicfCBQoSFirewallRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,12,1,2),_HpnicfCBQoSFirewallRowStatus_Type())
hpnicfCBQoSFirewallRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSFirewallRowStatus.setStatus(_A)
_HpnicfCBQoSSamplingCfgInfoTable_Object=MibTable
hpnicfCBQoSSamplingCfgInfoTable=_HpnicfCBQoSSamplingCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,13))
if mibBuilder.loadTexts:hpnicfCBQoSSamplingCfgInfoTable.setStatus(_A)
_HpnicfCBQoSSamplingCfgInfoEntry_Object=MibTableRow
hpnicfCBQoSSamplingCfgInfoEntry=_HpnicfCBQoSSamplingCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,13,1))
hpnicfCBQoSSamplingCfgInfoEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hpnicfCBQoSSamplingCfgInfoEntry.setStatus(_A)
class _HpnicfCBQoSSamplingNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HpnicfCBQoSSamplingNum_Type.__name__=_E
_HpnicfCBQoSSamplingNum_Object=MibTableColumn
hpnicfCBQoSSamplingNum=_HpnicfCBQoSSamplingNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,13,1,1),_HpnicfCBQoSSamplingNum_Type())
hpnicfCBQoSSamplingNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSSamplingNum.setStatus(_A)
_HpnicfCBQoSSamplingRowStatus_Type=RowStatus
_HpnicfCBQoSSamplingRowStatus_Object=MibTableColumn
hpnicfCBQoSSamplingRowStatus=_HpnicfCBQoSSamplingRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,13,1,2),_HpnicfCBQoSSamplingRowStatus_Type())
hpnicfCBQoSSamplingRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSSamplingRowStatus.setStatus(_A)
_HpnicfCBQoSAccountCfgInfoTable_Object=MibTable
hpnicfCBQoSAccountCfgInfoTable=_HpnicfCBQoSAccountCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,14))
if mibBuilder.loadTexts:hpnicfCBQoSAccountCfgInfoTable.setStatus(_A)
_HpnicfCBQoSAccountCfgInfoEntry_Object=MibTableRow
hpnicfCBQoSAccountCfgInfoEntry=_HpnicfCBQoSAccountCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,14,1))
hpnicfCBQoSAccountCfgInfoEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hpnicfCBQoSAccountCfgInfoEntry.setStatus(_A)
_HpnicfCBQoSAccounting_Type=TruthValue
_HpnicfCBQoSAccounting_Object=MibTableColumn
hpnicfCBQoSAccounting=_HpnicfCBQoSAccounting_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,14,1,1),_HpnicfCBQoSAccounting_Type())
hpnicfCBQoSAccounting.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSAccounting.setStatus(_A)
_HpnicfCBQoSAccountRowStatus_Type=RowStatus
_HpnicfCBQoSAccountRowStatus_Object=MibTableColumn
hpnicfCBQoSAccountRowStatus=_HpnicfCBQoSAccountRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,14,1,2),_HpnicfCBQoSAccountRowStatus_Type())
hpnicfCBQoSAccountRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSAccountRowStatus.setStatus(_A)
class _HpnicfCBQoSAccountingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('auto',1),('packet',2),('byte',3),('both',4)))
_HpnicfCBQoSAccountingMode_Type.__name__=_E
_HpnicfCBQoSAccountingMode_Object=MibTableColumn
hpnicfCBQoSAccountingMode=_HpnicfCBQoSAccountingMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,14,1,3),_HpnicfCBQoSAccountingMode_Type())
hpnicfCBQoSAccountingMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSAccountingMode.setStatus(_A)
_HpnicfCBQoSRedirectCfgInfoTable_Object=MibTable
hpnicfCBQoSRedirectCfgInfoTable=_HpnicfCBQoSRedirectCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,15))
if mibBuilder.loadTexts:hpnicfCBQoSRedirectCfgInfoTable.setStatus(_A)
_HpnicfCBQoSRedirectCfgInfoEntry_Object=MibTableRow
hpnicfCBQoSRedirectCfgInfoEntry=_HpnicfCBQoSRedirectCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,15,1))
hpnicfCBQoSRedirectCfgInfoEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hpnicfCBQoSRedirectCfgInfoEntry.setStatus(_A)
class _HpnicfCBQoSRedirectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('cpu',1),(_i,2),('nextHop',3)))
_HpnicfCBQoSRedirectType_Type.__name__=_E
_HpnicfCBQoSRedirectType_Object=MibTableColumn
hpnicfCBQoSRedirectType=_HpnicfCBQoSRedirectType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,15,1,1),_HpnicfCBQoSRedirectType_Type())
hpnicfCBQoSRedirectType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSRedirectType.setStatus(_A)
class _HpnicfCBQoSRedirectIfIndex_Type(Integer32):defaultValue=0
_HpnicfCBQoSRedirectIfIndex_Type.__name__=_E
_HpnicfCBQoSRedirectIfIndex_Object=MibTableColumn
hpnicfCBQoSRedirectIfIndex=_HpnicfCBQoSRedirectIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,15,1,2),_HpnicfCBQoSRedirectIfIndex_Type())
hpnicfCBQoSRedirectIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSRedirectIfIndex.setStatus(_A)
class _HpnicfCBQoSRedirectIpAddressType_Type(InetAddressType):defaultValue=0
_HpnicfCBQoSRedirectIpAddressType_Type.__name__=_o
_HpnicfCBQoSRedirectIpAddressType_Object=MibTableColumn
hpnicfCBQoSRedirectIpAddressType=_HpnicfCBQoSRedirectIpAddressType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,15,1,3),_HpnicfCBQoSRedirectIpAddressType_Type())
hpnicfCBQoSRedirectIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSRedirectIpAddressType.setStatus(_A)
_HpnicfCBQoSRedirectIpAddress1_Type=InetAddress
_HpnicfCBQoSRedirectIpAddress1_Object=MibTableColumn
hpnicfCBQoSRedirectIpAddress1=_HpnicfCBQoSRedirectIpAddress1_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,15,1,4),_HpnicfCBQoSRedirectIpAddress1_Type())
hpnicfCBQoSRedirectIpAddress1.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSRedirectIpAddress1.setStatus(_A)
_HpnicfCBQoSRedirectIpAddress2_Type=InetAddress
_HpnicfCBQoSRedirectIpAddress2_Object=MibTableColumn
hpnicfCBQoSRedirectIpAddress2=_HpnicfCBQoSRedirectIpAddress2_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,15,1,5),_HpnicfCBQoSRedirectIpAddress2_Type())
hpnicfCBQoSRedirectIpAddress2.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSRedirectIpAddress2.setStatus(_A)
_HpnicfCBQoSRedirectRowStatus_Type=RowStatus
_HpnicfCBQoSRedirectRowStatus_Object=MibTableColumn
hpnicfCBQoSRedirectRowStatus=_HpnicfCBQoSRedirectRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,15,1,6),_HpnicfCBQoSRedirectRowStatus_Type())
hpnicfCBQoSRedirectRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSRedirectRowStatus.setStatus(_A)
class _HpnicfCBQoSRedirectIpv6Interface1_Type(Integer32):defaultValue=0
_HpnicfCBQoSRedirectIpv6Interface1_Type.__name__=_E
_HpnicfCBQoSRedirectIpv6Interface1_Object=MibTableColumn
hpnicfCBQoSRedirectIpv6Interface1=_HpnicfCBQoSRedirectIpv6Interface1_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,15,1,7),_HpnicfCBQoSRedirectIpv6Interface1_Type())
hpnicfCBQoSRedirectIpv6Interface1.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSRedirectIpv6Interface1.setStatus(_A)
class _HpnicfCBQoSRedirectIpv6Interface2_Type(Integer32):defaultValue=0
_HpnicfCBQoSRedirectIpv6Interface2_Type.__name__=_E
_HpnicfCBQoSRedirectIpv6Interface2_Object=MibTableColumn
hpnicfCBQoSRedirectIpv6Interface2=_HpnicfCBQoSRedirectIpv6Interface2_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,15,1,8),_HpnicfCBQoSRedirectIpv6Interface2_Type())
hpnicfCBQoSRedirectIpv6Interface2.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSRedirectIpv6Interface2.setStatus(_A)
class _HpnicfCBQoSRedirectIfVlanID_Type(Integer32):defaultValue=65535;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094),ValueRangeConstraint(65535,65535))
_HpnicfCBQoSRedirectIfVlanID_Type.__name__=_E
_HpnicfCBQoSRedirectIfVlanID_Object=MibTableColumn
hpnicfCBQoSRedirectIfVlanID=_HpnicfCBQoSRedirectIfVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,15,1,9),_HpnicfCBQoSRedirectIfVlanID_Type())
hpnicfCBQoSRedirectIfVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSRedirectIfVlanID.setStatus(_A)
_HpnicfCBQoSPriorityMapCfgInfoTable_Object=MibTable
hpnicfCBQoSPriorityMapCfgInfoTable=_HpnicfCBQoSPriorityMapCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,16))
if mibBuilder.loadTexts:hpnicfCBQoSPriorityMapCfgInfoTable.setStatus(_A)
_HpnicfCBQoSPriorityMapCfgInfoEntry_Object=MibTableRow
hpnicfCBQoSPriorityMapCfgInfoEntry=_HpnicfCBQoSPriorityMapCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,16,1))
hpnicfCBQoSPriorityMapCfgInfoEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hpnicfCBQoSPriorityMapCfgInfoEntry.setStatus(_A)
class _HpnicfCBQoSPriorityMapImportType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_a,1),('dscp',2),('dot1p',3),('exp',4),(_s,5),(_t,6),(_u,7)))
_HpnicfCBQoSPriorityMapImportType_Type.__name__=_E
_HpnicfCBQoSPriorityMapImportType_Object=MibTableColumn
hpnicfCBQoSPriorityMapImportType=_HpnicfCBQoSPriorityMapImportType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,16,1,1),_HpnicfCBQoSPriorityMapImportType_Type())
hpnicfCBQoSPriorityMapImportType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSPriorityMapImportType.setStatus(_A)
class _HpnicfCBQoSPriorityMapExportType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_a,1),('dscp',2),('dot1p',3),('exp',4),(_s,5),(_t,6),(_u,7)))
_HpnicfCBQoSPriorityMapExportType_Type.__name__=_E
_HpnicfCBQoSPriorityMapExportType_Object=MibTableColumn
hpnicfCBQoSPriorityMapExportType=_HpnicfCBQoSPriorityMapExportType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,16,1,2),_HpnicfCBQoSPriorityMapExportType_Type())
hpnicfCBQoSPriorityMapExportType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSPriorityMapExportType.setStatus(_A)
_HpnicfCBQoSPriorityMapGroupIndex_Type=Integer32
_HpnicfCBQoSPriorityMapGroupIndex_Object=MibTableColumn
hpnicfCBQoSPriorityMapGroupIndex=_HpnicfCBQoSPriorityMapGroupIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,16,1,3),_HpnicfCBQoSPriorityMapGroupIndex_Type())
hpnicfCBQoSPriorityMapGroupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSPriorityMapGroupIndex.setStatus(_A)
class _HpnicfCBQoSPriorityMapGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HpnicfCBQoSPriorityMapGroupName_Type.__name__=_I
_HpnicfCBQoSPriorityMapGroupName_Object=MibTableColumn
hpnicfCBQoSPriorityMapGroupName=_HpnicfCBQoSPriorityMapGroupName_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,16,1,4),_HpnicfCBQoSPriorityMapGroupName_Type())
hpnicfCBQoSPriorityMapGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSPriorityMapGroupName.setStatus(_A)
class _HpnicfCBQoSPriorityMapAuto_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_a,1),('autoDscp',2),('autoDot1p',3),('autoMplsExp',4),('autoIp',5)))
_HpnicfCBQoSPriorityMapAuto_Type.__name__=_E
_HpnicfCBQoSPriorityMapAuto_Object=MibTableColumn
hpnicfCBQoSPriorityMapAuto=_HpnicfCBQoSPriorityMapAuto_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,16,1,5),_HpnicfCBQoSPriorityMapAuto_Type())
hpnicfCBQoSPriorityMapAuto.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSPriorityMapAuto.setStatus(_A)
_HpnicfCBQoSPriorityMapRowStatus_Type=RowStatus
_HpnicfCBQoSPriorityMapRowStatus_Object=MibTableColumn
hpnicfCBQoSPriorityMapRowStatus=_HpnicfCBQoSPriorityMapRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,16,1,6),_HpnicfCBQoSPriorityMapRowStatus_Type())
hpnicfCBQoSPriorityMapRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSPriorityMapRowStatus.setStatus(_A)
_HpnicfCBQoSMirrorCfgInfoTable_Object=MibTable
hpnicfCBQoSMirrorCfgInfoTable=_HpnicfCBQoSMirrorCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,17))
if mibBuilder.loadTexts:hpnicfCBQoSMirrorCfgInfoTable.setStatus(_A)
_HpnicfCBQoSMirrorCfgInfoEntry_Object=MibTableRow
hpnicfCBQoSMirrorCfgInfoEntry=_HpnicfCBQoSMirrorCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,17,1))
hpnicfCBQoSMirrorCfgInfoEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hpnicfCBQoSMirrorCfgInfoEntry.setStatus(_A)
class _HpnicfCBQoSMirrorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_i,1),('cpu',2),('vlan',3)))
_HpnicfCBQoSMirrorType_Type.__name__=_E
_HpnicfCBQoSMirrorType_Object=MibTableColumn
hpnicfCBQoSMirrorType=_HpnicfCBQoSMirrorType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,17,1,1),_HpnicfCBQoSMirrorType_Type())
hpnicfCBQoSMirrorType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSMirrorType.setStatus(_A)
class _HpnicfCBQoSMirrorIfIndex_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfCBQoSMirrorIfIndex_Type.__name__=_I
_HpnicfCBQoSMirrorIfIndex_Object=MibTableColumn
hpnicfCBQoSMirrorIfIndex=_HpnicfCBQoSMirrorIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,17,1,2),_HpnicfCBQoSMirrorIfIndex_Type())
hpnicfCBQoSMirrorIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSMirrorIfIndex.setStatus(_A)
class _HpnicfCBQoSMirrorVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpnicfCBQoSMirrorVlanID_Type.__name__=_E
_HpnicfCBQoSMirrorVlanID_Object=MibTableColumn
hpnicfCBQoSMirrorVlanID=_HpnicfCBQoSMirrorVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,17,1,3),_HpnicfCBQoSMirrorVlanID_Type())
hpnicfCBQoSMirrorVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSMirrorVlanID.setStatus(_A)
_HpnicfCBQoSMirrorRowStatus_Type=RowStatus
_HpnicfCBQoSMirrorRowStatus_Object=MibTableColumn
hpnicfCBQoSMirrorRowStatus=_HpnicfCBQoSMirrorRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,17,1,4),_HpnicfCBQoSMirrorRowStatus_Type())
hpnicfCBQoSMirrorRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSMirrorRowStatus.setStatus(_A)
_HpnicfCBQoSNestCfgInfoTable_Object=MibTable
hpnicfCBQoSNestCfgInfoTable=_HpnicfCBQoSNestCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,18))
if mibBuilder.loadTexts:hpnicfCBQoSNestCfgInfoTable.setStatus(_A)
_HpnicfCBQoSNestCfgInfoEntry_Object=MibTableRow
hpnicfCBQoSNestCfgInfoEntry=_HpnicfCBQoSNestCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,18,1))
hpnicfCBQoSNestCfgInfoEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hpnicfCBQoSNestCfgInfoEntry.setStatus(_A)
class _HpnicfCBQoSNestServiceVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094),ValueRangeConstraint(65535,65535))
_HpnicfCBQoSNestServiceVlanID_Type.__name__=_E
_HpnicfCBQoSNestServiceVlanID_Object=MibTableColumn
hpnicfCBQoSNestServiceVlanID=_HpnicfCBQoSNestServiceVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,18,1,1),_HpnicfCBQoSNestServiceVlanID_Type())
hpnicfCBQoSNestServiceVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSNestServiceVlanID.setStatus(_A)
class _HpnicfCBQoSNestServiceDot1pValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(65535,65535))
_HpnicfCBQoSNestServiceDot1pValue_Type.__name__=_E
_HpnicfCBQoSNestServiceDot1pValue_Object=MibTableColumn
hpnicfCBQoSNestServiceDot1pValue=_HpnicfCBQoSNestServiceDot1pValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,18,1,2),_HpnicfCBQoSNestServiceDot1pValue_Type())
hpnicfCBQoSNestServiceDot1pValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSNestServiceDot1pValue.setStatus(_A)
class _HpnicfCBQoSNestCustomerVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094),ValueRangeConstraint(65535,65535))
_HpnicfCBQoSNestCustomerVlanID_Type.__name__=_E
_HpnicfCBQoSNestCustomerVlanID_Object=MibTableColumn
hpnicfCBQoSNestCustomerVlanID=_HpnicfCBQoSNestCustomerVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,18,1,3),_HpnicfCBQoSNestCustomerVlanID_Type())
hpnicfCBQoSNestCustomerVlanID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSNestCustomerVlanID.setStatus(_A)
class _HpnicfCBQoSNestCustomerDot1pValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(65535,65535))
_HpnicfCBQoSNestCustomerDot1pValue_Type.__name__=_E
_HpnicfCBQoSNestCustomerDot1pValue_Object=MibTableColumn
hpnicfCBQoSNestCustomerDot1pValue=_HpnicfCBQoSNestCustomerDot1pValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,18,1,4),_HpnicfCBQoSNestCustomerDot1pValue_Type())
hpnicfCBQoSNestCustomerDot1pValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSNestCustomerDot1pValue.setStatus(_A)
_HpnicfCBQoSNestRowStatus_Type=RowStatus
_HpnicfCBQoSNestRowStatus_Object=MibTableColumn
hpnicfCBQoSNestRowStatus=_HpnicfCBQoSNestRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,18,1,5),_HpnicfCBQoSNestRowStatus_Type())
hpnicfCBQoSNestRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSNestRowStatus.setStatus(_A)
_HpnicfCBQoSNestPolicyCfgInfoTable_Object=MibTable
hpnicfCBQoSNestPolicyCfgInfoTable=_HpnicfCBQoSNestPolicyCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,19))
if mibBuilder.loadTexts:hpnicfCBQoSNestPolicyCfgInfoTable.setStatus(_A)
_HpnicfCBQoSNestPolicyCfgInfoEntry_Object=MibTableRow
hpnicfCBQoSNestPolicyCfgInfoEntry=_HpnicfCBQoSNestPolicyCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,19,1))
hpnicfCBQoSNestPolicyCfgInfoEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hpnicfCBQoSNestPolicyCfgInfoEntry.setStatus(_A)
class _HpnicfCBQoSNestPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HpnicfCBQoSNestPolicyName_Type.__name__=_I
_HpnicfCBQoSNestPolicyName_Object=MibTableColumn
hpnicfCBQoSNestPolicyName=_HpnicfCBQoSNestPolicyName_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,19,1,1),_HpnicfCBQoSNestPolicyName_Type())
hpnicfCBQoSNestPolicyName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSNestPolicyName.setStatus(_A)
_HpnicfCBQoSNestPolicyRowStatus_Type=RowStatus
_HpnicfCBQoSNestPolicyRowStatus_Object=MibTableColumn
hpnicfCBQoSNestPolicyRowStatus=_HpnicfCBQoSNestPolicyRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,19,1,2),_HpnicfCBQoSNestPolicyRowStatus_Type())
hpnicfCBQoSNestPolicyRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSNestPolicyRowStatus.setStatus(_A)
_HpnicfCBQoSMirrorIfCfgInfoTable_Object=MibTable
hpnicfCBQoSMirrorIfCfgInfoTable=_HpnicfCBQoSMirrorIfCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,20))
if mibBuilder.loadTexts:hpnicfCBQoSMirrorIfCfgInfoTable.setStatus(_A)
_HpnicfCBQoSMirrorIfCfgInfoEntry_Object=MibTableRow
hpnicfCBQoSMirrorIfCfgInfoEntry=_HpnicfCBQoSMirrorIfCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,20,1))
hpnicfCBQoSMirrorIfCfgInfoEntry.setIndexNames((0,_B,_H),(0,_B,_v))
if mibBuilder.loadTexts:hpnicfCBQoSMirrorIfCfgInfoEntry.setStatus(_A)
_HpnicfCBQoSMirrorIfMainIfIndex_Type=Integer32
_HpnicfCBQoSMirrorIfMainIfIndex_Object=MibTableColumn
hpnicfCBQoSMirrorIfMainIfIndex=_HpnicfCBQoSMirrorIfMainIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,20,1,1),_HpnicfCBQoSMirrorIfMainIfIndex_Type())
hpnicfCBQoSMirrorIfMainIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSMirrorIfMainIfIndex.setStatus(_A)
class _HpnicfCBQoSMirrorIfMainIfStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_w,1),(_x,2)))
_HpnicfCBQoSMirrorIfMainIfStatus_Type.__name__=_E
_HpnicfCBQoSMirrorIfMainIfStatus_Object=MibTableColumn
hpnicfCBQoSMirrorIfMainIfStatus=_HpnicfCBQoSMirrorIfMainIfStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,20,1,2),_HpnicfCBQoSMirrorIfMainIfStatus_Type())
hpnicfCBQoSMirrorIfMainIfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSMirrorIfMainIfStatus.setStatus(_A)
_HpnicfCBQoSMirrorIfBackupIfIndex_Type=Integer32
_HpnicfCBQoSMirrorIfBackupIfIndex_Object=MibTableColumn
hpnicfCBQoSMirrorIfBackupIfIndex=_HpnicfCBQoSMirrorIfBackupIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,20,1,3),_HpnicfCBQoSMirrorIfBackupIfIndex_Type())
hpnicfCBQoSMirrorIfBackupIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSMirrorIfBackupIfIndex.setStatus(_A)
class _HpnicfCBQoSMirrorIfBackupIfStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_w,1),(_x,2)))
_HpnicfCBQoSMirrorIfBackupIfStatus_Type.__name__=_E
_HpnicfCBQoSMirrorIfBackupIfStatus_Object=MibTableColumn
hpnicfCBQoSMirrorIfBackupIfStatus=_HpnicfCBQoSMirrorIfBackupIfStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,20,1,4),_HpnicfCBQoSMirrorIfBackupIfStatus_Type())
hpnicfCBQoSMirrorIfBackupIfStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSMirrorIfBackupIfStatus.setStatus(_A)
_HpnicfCBQoSMirrorIfRowStatus_Type=RowStatus
_HpnicfCBQoSMirrorIfRowStatus_Object=MibTableColumn
hpnicfCBQoSMirrorIfRowStatus=_HpnicfCBQoSMirrorIfRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,20,1,5),_HpnicfCBQoSMirrorIfRowStatus_Type())
hpnicfCBQoSMirrorIfRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSMirrorIfRowStatus.setStatus(_A)
_HpnicfCBQoSColoredRemarkCfgTable_Object=MibTable
hpnicfCBQoSColoredRemarkCfgTable=_HpnicfCBQoSColoredRemarkCfgTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,21))
if mibBuilder.loadTexts:hpnicfCBQoSColoredRemarkCfgTable.setStatus(_A)
_HpnicfCBQoSColoredRemarkCfgEntry_Object=MibTableRow
hpnicfCBQoSColoredRemarkCfgEntry=_HpnicfCBQoSColoredRemarkCfgEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,21,1))
hpnicfCBQoSColoredRemarkCfgEntry.setIndexNames((0,_B,_H),(0,_B,_y),(0,_B,_z))
if mibBuilder.loadTexts:hpnicfCBQoSColoredRemarkCfgEntry.setStatus(_A)
_HpnicfCBQoSColoredRemarkType_Type=RemarkType
_HpnicfCBQoSColoredRemarkType_Object=MibTableColumn
hpnicfCBQoSColoredRemarkType=_HpnicfCBQoSColoredRemarkType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,21,1,1),_HpnicfCBQoSColoredRemarkType_Type())
hpnicfCBQoSColoredRemarkType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSColoredRemarkType.setStatus(_A)
class _HpnicfCBQoSColoredRemarkColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('green',1),('yellow',2),('red',3)))
_HpnicfCBQoSColoredRemarkColor_Type.__name__=_E
_HpnicfCBQoSColoredRemarkColor_Object=MibTableColumn
hpnicfCBQoSColoredRemarkColor=_HpnicfCBQoSColoredRemarkColor_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,21,1,2),_HpnicfCBQoSColoredRemarkColor_Type())
hpnicfCBQoSColoredRemarkColor.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSColoredRemarkColor.setStatus(_A)
class _HpnicfCBQoSColoredRemarkValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_HpnicfCBQoSColoredRemarkValue_Type.__name__=_E
_HpnicfCBQoSColoredRemarkValue_Object=MibTableColumn
hpnicfCBQoSColoredRemarkValue=_HpnicfCBQoSColoredRemarkValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,21,1,3),_HpnicfCBQoSColoredRemarkValue_Type())
hpnicfCBQoSColoredRemarkValue.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSColoredRemarkValue.setStatus(_A)
_HpnicfCBQoSColoredRemarkRowStatus_Type=RowStatus
_HpnicfCBQoSColoredRemarkRowStatus_Object=MibTableColumn
hpnicfCBQoSColoredRemarkRowStatus=_HpnicfCBQoSColoredRemarkRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,21,1,4),_HpnicfCBQoSColoredRemarkRowStatus_Type())
hpnicfCBQoSColoredRemarkRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSColoredRemarkRowStatus.setStatus(_A)
_HpnicfCBQoSPrimapCfgInfoTable_Object=MibTable
hpnicfCBQoSPrimapCfgInfoTable=_HpnicfCBQoSPrimapCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,22))
if mibBuilder.loadTexts:hpnicfCBQoSPrimapCfgInfoTable.setStatus(_A)
_HpnicfCBQoSPrimapCfgInfoEntry_Object=MibTableRow
hpnicfCBQoSPrimapCfgInfoEntry=_HpnicfCBQoSPrimapCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,22,1))
hpnicfCBQoSPrimapCfgInfoEntry.setIndexNames((0,_B,_H),(0,_B,_A0),(0,_B,_A1))
if mibBuilder.loadTexts:hpnicfCBQoSPrimapCfgInfoEntry.setStatus(_A)
class _HpnicfCBQoSPrimapColorType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noColorMap',1),('colorMap',2)))
_HpnicfCBQoSPrimapColorType_Type.__name__=_E
_HpnicfCBQoSPrimapColorType_Object=MibTableColumn
hpnicfCBQoSPrimapColorType=_HpnicfCBQoSPrimapColorType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,22,1,1),_HpnicfCBQoSPrimapColorType_Type())
hpnicfCBQoSPrimapColorType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSPrimapColorType.setStatus(_A)
class _HpnicfCBQoSPrePriMapTableType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34)));namedValues=NamedValues(*(('dot1pToLp',1),('dot1pToDp',2),('expToLp',3),('dscpToLp',4),('expToDp',5),('dscpToDp',6),('dscpToDot1p',7),('dot1pToDscp',8),('dscpToDscp',9),('dscpToExp',10),('expToDscp',11),('expToDot1p',12),('expToExp',13),('lpToDot1p',14),('dot1pToRpr',15),('dscpToRpr',16),('expToRpr',17),('ippreToRpr',18),('upToDot1p',19),('upToDscp',20),('upToExp',21),('upToDp',22),('upToLp',23),('upToRpr',24),('upToFc',25),('lpTodscp',26),('dot11eToLp',27),('lpToDot11e',28),('lpToLp',29),('dot1pToExp',30),('lpToExp',31),('lpToDp',32),('upToUp',33),('dot1pToDot1p',34)))
_HpnicfCBQoSPrePriMapTableType_Type.__name__=_E
_HpnicfCBQoSPrePriMapTableType_Object=MibTableColumn
hpnicfCBQoSPrePriMapTableType=_HpnicfCBQoSPrePriMapTableType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,22,1,2),_HpnicfCBQoSPrePriMapTableType_Type())
hpnicfCBQoSPrePriMapTableType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSPrePriMapTableType.setStatus(_A)
_HpnicfCBQoSPrimapRowStatus_Type=RowStatus
_HpnicfCBQoSPrimapRowStatus_Object=MibTableColumn
hpnicfCBQoSPrimapRowStatus=_HpnicfCBQoSPrimapRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,22,1,3),_HpnicfCBQoSPrimapRowStatus_Type())
hpnicfCBQoSPrimapRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSPrimapRowStatus.setStatus(_A)
_HpnicfCBQoSColorMapDpCfgInfoTable_Object=MibTable
hpnicfCBQoSColorMapDpCfgInfoTable=_HpnicfCBQoSColorMapDpCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,23))
if mibBuilder.loadTexts:hpnicfCBQoSColorMapDpCfgInfoTable.setStatus(_A)
_HpnicfCBQoSColorMapDpCfgInfoEntry_Object=MibTableRow
hpnicfCBQoSColorMapDpCfgInfoEntry=_HpnicfCBQoSColorMapDpCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,23,1))
hpnicfCBQoSColorMapDpCfgInfoEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:hpnicfCBQoSColorMapDpCfgInfoEntry.setStatus(_A)
_HpnicfCBQoSColorMapDpEnable_Type=TruthValue
_HpnicfCBQoSColorMapDpEnable_Object=MibTableColumn
hpnicfCBQoSColorMapDpEnable=_HpnicfCBQoSColorMapDpEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,23,1,1),_HpnicfCBQoSColorMapDpEnable_Type())
hpnicfCBQoSColorMapDpEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSColorMapDpEnable.setStatus(_A)
_HpnicfCBQoSColorMapDpRowStatus_Type=RowStatus
_HpnicfCBQoSColorMapDpRowStatus_Object=MibTableColumn
hpnicfCBQoSColorMapDpRowStatus=_HpnicfCBQoSColorMapDpRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,2,23,1,2),_HpnicfCBQoSColorMapDpRowStatus_Type())
hpnicfCBQoSColorMapDpRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSColorMapDpRowStatus.setStatus(_A)
_HpnicfCBQoSPolicyObjects_ObjectIdentity=ObjectIdentity
hpnicfCBQoSPolicyObjects=_HpnicfCBQoSPolicyObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,3))
_HpnicfCBQoSPolicyIndexNext_Type=Integer32
_HpnicfCBQoSPolicyIndexNext_Object=MibScalar
hpnicfCBQoSPolicyIndexNext=_HpnicfCBQoSPolicyIndexNext_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,3,1),_HpnicfCBQoSPolicyIndexNext_Type())
hpnicfCBQoSPolicyIndexNext.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSPolicyIndexNext.setStatus(_A)
_HpnicfCBQoSPolicyCfgInfoTable_Object=MibTable
hpnicfCBQoSPolicyCfgInfoTable=_HpnicfCBQoSPolicyCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,3,2))
if mibBuilder.loadTexts:hpnicfCBQoSPolicyCfgInfoTable.setStatus(_A)
_HpnicfCBQoSPolicyCfgInfoEntry_Object=MibTableRow
hpnicfCBQoSPolicyCfgInfoEntry=_HpnicfCBQoSPolicyCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,3,2,1))
hpnicfCBQoSPolicyCfgInfoEntry.setIndexNames((0,_B,_n))
if mibBuilder.loadTexts:hpnicfCBQoSPolicyCfgInfoEntry.setStatus(_A)
_HpnicfCBQoSPolicyIndex_Type=Integer32
_HpnicfCBQoSPolicyIndex_Object=MibTableColumn
hpnicfCBQoSPolicyIndex=_HpnicfCBQoSPolicyIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,3,2,1,1),_HpnicfCBQoSPolicyIndex_Type())
hpnicfCBQoSPolicyIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSPolicyIndex.setStatus(_A)
class _HpnicfCBQoSPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HpnicfCBQoSPolicyName_Type.__name__=_I
_HpnicfCBQoSPolicyName_Object=MibTableColumn
hpnicfCBQoSPolicyName=_HpnicfCBQoSPolicyName_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,3,2,1,2),_HpnicfCBQoSPolicyName_Type())
hpnicfCBQoSPolicyName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSPolicyName.setStatus(_A)
_HpnicfCBQoSPolicyClassCount_Type=Integer32
_HpnicfCBQoSPolicyClassCount_Object=MibTableColumn
hpnicfCBQoSPolicyClassCount=_HpnicfCBQoSPolicyClassCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,3,2,1,3),_HpnicfCBQoSPolicyClassCount_Type())
hpnicfCBQoSPolicyClassCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSPolicyClassCount.setStatus(_A)
class _HpnicfCBQoSPolicyConfigMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_b,0),('config',1),('auto',2)))
_HpnicfCBQoSPolicyConfigMode_Type.__name__=_E
_HpnicfCBQoSPolicyConfigMode_Object=MibTableColumn
hpnicfCBQoSPolicyConfigMode=_HpnicfCBQoSPolicyConfigMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,3,2,1,4),_HpnicfCBQoSPolicyConfigMode_Type())
hpnicfCBQoSPolicyConfigMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSPolicyConfigMode.setStatus(_A)
class _HpnicfCBQoSPolicyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_j,1),(_k,2)))
_HpnicfCBQoSPolicyType_Type.__name__=_E
_HpnicfCBQoSPolicyType_Object=MibTableColumn
hpnicfCBQoSPolicyType=_HpnicfCBQoSPolicyType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,3,2,1,5),_HpnicfCBQoSPolicyType_Type())
hpnicfCBQoSPolicyType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSPolicyType.setStatus(_A)
_HpnicfCBQoSPolicyClassNextIndex_Type=Integer32
_HpnicfCBQoSPolicyClassNextIndex_Object=MibTableColumn
hpnicfCBQoSPolicyClassNextIndex=_HpnicfCBQoSPolicyClassNextIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,3,2,1,6),_HpnicfCBQoSPolicyClassNextIndex_Type())
hpnicfCBQoSPolicyClassNextIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSPolicyClassNextIndex.setStatus(_A)
_HpnicfCBQoSPolicyRowStatus_Type=RowStatus
_HpnicfCBQoSPolicyRowStatus_Object=MibTableColumn
hpnicfCBQoSPolicyRowStatus=_HpnicfCBQoSPolicyRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,3,2,1,7),_HpnicfCBQoSPolicyRowStatus_Type())
hpnicfCBQoSPolicyRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSPolicyRowStatus.setStatus(_A)
_HpnicfCBQoSPolicyClassCfgInfoTable_Object=MibTable
hpnicfCBQoSPolicyClassCfgInfoTable=_HpnicfCBQoSPolicyClassCfgInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,3,3))
if mibBuilder.loadTexts:hpnicfCBQoSPolicyClassCfgInfoTable.setStatus(_A)
_HpnicfCBQoSPolicyClassCfgInfoEntry_Object=MibTableRow
hpnicfCBQoSPolicyClassCfgInfoEntry=_HpnicfCBQoSPolicyClassCfgInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,3,3,1))
hpnicfCBQoSPolicyClassCfgInfoEntry.setIndexNames((0,_B,_n),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfCBQoSPolicyClassCfgInfoEntry.setStatus(_A)
_HpnicfCBQoSPolicyClassIndex_Type=Integer32
_HpnicfCBQoSPolicyClassIndex_Object=MibTableColumn
hpnicfCBQoSPolicyClassIndex=_HpnicfCBQoSPolicyClassIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,3,3,1,1),_HpnicfCBQoSPolicyClassIndex_Type())
hpnicfCBQoSPolicyClassIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSPolicyClassIndex.setStatus(_A)
_HpnicfCBQoSPolicyClassClassifierIndex_Type=Integer32
_HpnicfCBQoSPolicyClassClassifierIndex_Object=MibTableColumn
hpnicfCBQoSPolicyClassClassifierIndex=_HpnicfCBQoSPolicyClassClassifierIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,3,3,1,2),_HpnicfCBQoSPolicyClassClassifierIndex_Type())
hpnicfCBQoSPolicyClassClassifierIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSPolicyClassClassifierIndex.setStatus(_A)
class _HpnicfCBQoSPolicyClassClassifierName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HpnicfCBQoSPolicyClassClassifierName_Type.__name__=_I
_HpnicfCBQoSPolicyClassClassifierName_Object=MibTableColumn
hpnicfCBQoSPolicyClassClassifierName=_HpnicfCBQoSPolicyClassClassifierName_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,3,3,1,3),_HpnicfCBQoSPolicyClassClassifierName_Type())
hpnicfCBQoSPolicyClassClassifierName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSPolicyClassClassifierName.setStatus(_A)
_HpnicfCBQoSPolicyClassBehaviorIndex_Type=Integer32
_HpnicfCBQoSPolicyClassBehaviorIndex_Object=MibTableColumn
hpnicfCBQoSPolicyClassBehaviorIndex=_HpnicfCBQoSPolicyClassBehaviorIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,3,3,1,4),_HpnicfCBQoSPolicyClassBehaviorIndex_Type())
hpnicfCBQoSPolicyClassBehaviorIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSPolicyClassBehaviorIndex.setStatus(_A)
class _HpnicfCBQoSPolicyClassBehaviorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HpnicfCBQoSPolicyClassBehaviorName_Type.__name__=_I
_HpnicfCBQoSPolicyClassBehaviorName_Object=MibTableColumn
hpnicfCBQoSPolicyClassBehaviorName=_HpnicfCBQoSPolicyClassBehaviorName_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,3,3,1,5),_HpnicfCBQoSPolicyClassBehaviorName_Type())
hpnicfCBQoSPolicyClassBehaviorName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSPolicyClassBehaviorName.setStatus(_A)
class _HpnicfCBQoSPolicyClassPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16383),ValueRangeConstraint(2147483647,2147483647))
_HpnicfCBQoSPolicyClassPrecedence_Type.__name__=_E
_HpnicfCBQoSPolicyClassPrecedence_Object=MibTableColumn
hpnicfCBQoSPolicyClassPrecedence=_HpnicfCBQoSPolicyClassPrecedence_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,3,3,1,6),_HpnicfCBQoSPolicyClassPrecedence_Type())
hpnicfCBQoSPolicyClassPrecedence.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSPolicyClassPrecedence.setStatus(_A)
_HpnicfCBQoSPolicyClassRowStatus_Type=RowStatus
_HpnicfCBQoSPolicyClassRowStatus_Object=MibTableColumn
hpnicfCBQoSPolicyClassRowStatus=_HpnicfCBQoSPolicyClassRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,3,3,1,7),_HpnicfCBQoSPolicyClassRowStatus_Type())
hpnicfCBQoSPolicyClassRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSPolicyClassRowStatus.setStatus(_A)
class _HpnicfCBQoSPolicyClassMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('modeNo',1),('modeDot1q',2),('modeQppb',3),('modeIpSourceGuard',4),('modeVoiceVlan',5),('modeDCBX',6)))
_HpnicfCBQoSPolicyClassMode_Type.__name__=_E
_HpnicfCBQoSPolicyClassMode_Object=MibTableColumn
hpnicfCBQoSPolicyClassMode=_HpnicfCBQoSPolicyClassMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,3,3,1,8),_HpnicfCBQoSPolicyClassMode_Type())
hpnicfCBQoSPolicyClassMode.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSPolicyClassMode.setStatus(_A)
_HpnicfCBQoSPolicyClassCfgOrder_Type=Integer32
_HpnicfCBQoSPolicyClassCfgOrder_Object=MibTableColumn
hpnicfCBQoSPolicyClassCfgOrder=_HpnicfCBQoSPolicyClassCfgOrder_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,3,3,1,9),_HpnicfCBQoSPolicyClassCfgOrder_Type())
hpnicfCBQoSPolicyClassCfgOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSPolicyClassCfgOrder.setStatus(_A)
_HpnicfCBQoSApplyPolicyObjects_ObjectIdentity=ObjectIdentity
hpnicfCBQoSApplyPolicyObjects=_HpnicfCBQoSApplyPolicyObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4))
_HpnicfCBQoSIfApplyPolicyTable_Object=MibTable
hpnicfCBQoSIfApplyPolicyTable=_HpnicfCBQoSIfApplyPolicyTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,1))
if mibBuilder.loadTexts:hpnicfCBQoSIfApplyPolicyTable.setStatus(_A)
_HpnicfCBQoSIfApplyPolicyEntry_Object=MibTableRow
hpnicfCBQoSIfApplyPolicyEntry=_HpnicfCBQoSIfApplyPolicyEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,1,1))
hpnicfCBQoSIfApplyPolicyEntry.setIndexNames((0,_B,_J),(0,_B,_L))
if mibBuilder.loadTexts:hpnicfCBQoSIfApplyPolicyEntry.setStatus(_A)
_HpnicfCBQoSIfApplyPolicyIfIndex_Type=Integer32
_HpnicfCBQoSIfApplyPolicyIfIndex_Object=MibTableColumn
hpnicfCBQoSIfApplyPolicyIfIndex=_HpnicfCBQoSIfApplyPolicyIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,1,1,1),_HpnicfCBQoSIfApplyPolicyIfIndex_Type())
hpnicfCBQoSIfApplyPolicyIfIndex.setMaxAccess(_e)
if mibBuilder.loadTexts:hpnicfCBQoSIfApplyPolicyIfIndex.setStatus(_A)
_HpnicfCBQoSIfApplyPolicyDirection_Type=DirectionType
_HpnicfCBQoSIfApplyPolicyDirection_Object=MibTableColumn
hpnicfCBQoSIfApplyPolicyDirection=_HpnicfCBQoSIfApplyPolicyDirection_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,1,1,2),_HpnicfCBQoSIfApplyPolicyDirection_Type())
hpnicfCBQoSIfApplyPolicyDirection.setMaxAccess(_e)
if mibBuilder.loadTexts:hpnicfCBQoSIfApplyPolicyDirection.setStatus(_A)
class _HpnicfCBQoSIfApplyPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HpnicfCBQoSIfApplyPolicyName_Type.__name__=_I
_HpnicfCBQoSIfApplyPolicyName_Object=MibTableColumn
hpnicfCBQoSIfApplyPolicyName=_HpnicfCBQoSIfApplyPolicyName_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,1,1,3),_HpnicfCBQoSIfApplyPolicyName_Type())
hpnicfCBQoSIfApplyPolicyName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSIfApplyPolicyName.setStatus(_A)
class _HpnicfCBQoSIfApplyPolicyEnableDynamic_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_b,1),('true',2),('false',3)))
_HpnicfCBQoSIfApplyPolicyEnableDynamic_Type.__name__=_E
_HpnicfCBQoSIfApplyPolicyEnableDynamic_Object=MibTableColumn
hpnicfCBQoSIfApplyPolicyEnableDynamic=_HpnicfCBQoSIfApplyPolicyEnableDynamic_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,1,1,4),_HpnicfCBQoSIfApplyPolicyEnableDynamic_Type())
hpnicfCBQoSIfApplyPolicyEnableDynamic.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSIfApplyPolicyEnableDynamic.setStatus(_A)
_HpnicfCBQoSIfApplyPolicyRowStatus_Type=RowStatus
_HpnicfCBQoSIfApplyPolicyRowStatus_Object=MibTableColumn
hpnicfCBQoSIfApplyPolicyRowStatus=_HpnicfCBQoSIfApplyPolicyRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,1,1,5),_HpnicfCBQoSIfApplyPolicyRowStatus_Type())
hpnicfCBQoSIfApplyPolicyRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSIfApplyPolicyRowStatus.setStatus(_A)
class _HpnicfCBQoSIfApplyPolicyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_f,1),(_W,2),(_g,3)))
_HpnicfCBQoSIfApplyPolicyStatus_Type.__name__=_E
_HpnicfCBQoSIfApplyPolicyStatus_Object=MibTableColumn
hpnicfCBQoSIfApplyPolicyStatus=_HpnicfCBQoSIfApplyPolicyStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,1,1,6),_HpnicfCBQoSIfApplyPolicyStatus_Type())
hpnicfCBQoSIfApplyPolicyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfApplyPolicyStatus.setStatus(_A)
_HpnicfCBQoSAtmPvcApplyPolicyTable_Object=MibTable
hpnicfCBQoSAtmPvcApplyPolicyTable=_HpnicfCBQoSAtmPvcApplyPolicyTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,2))
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcApplyPolicyTable.setStatus(_A)
_HpnicfCBQoSAtmPvcApplyPolicyEntry_Object=MibTableRow
hpnicfCBQoSAtmPvcApplyPolicyEntry=_HpnicfCBQoSAtmPvcApplyPolicyEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,2,1))
hpnicfCBQoSAtmPvcApplyPolicyEntry.setIndexNames((0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_R))
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcApplyPolicyEntry.setStatus(_A)
_HpnicfCBQoSAtmPvcApplyPolicyIfIndex_Type=Integer32
_HpnicfCBQoSAtmPvcApplyPolicyIfIndex_Object=MibTableColumn
hpnicfCBQoSAtmPvcApplyPolicyIfIndex=_HpnicfCBQoSAtmPvcApplyPolicyIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,2,1,1),_HpnicfCBQoSAtmPvcApplyPolicyIfIndex_Type())
hpnicfCBQoSAtmPvcApplyPolicyIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcApplyPolicyIfIndex.setStatus(_A)
_HpnicfCBQoSAtmPvcApplyPolicyVPI_Type=Integer32
_HpnicfCBQoSAtmPvcApplyPolicyVPI_Object=MibTableColumn
hpnicfCBQoSAtmPvcApplyPolicyVPI=_HpnicfCBQoSAtmPvcApplyPolicyVPI_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,2,1,2),_HpnicfCBQoSAtmPvcApplyPolicyVPI_Type())
hpnicfCBQoSAtmPvcApplyPolicyVPI.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcApplyPolicyVPI.setStatus(_A)
_HpnicfCBQoSAtmPvcApplyPolicyVCI_Type=Integer32
_HpnicfCBQoSAtmPvcApplyPolicyVCI_Object=MibTableColumn
hpnicfCBQoSAtmPvcApplyPolicyVCI=_HpnicfCBQoSAtmPvcApplyPolicyVCI_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,2,1,3),_HpnicfCBQoSAtmPvcApplyPolicyVCI_Type())
hpnicfCBQoSAtmPvcApplyPolicyVCI.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcApplyPolicyVCI.setStatus(_A)
_HpnicfCBQoSAtmPvcApplyPolicyDirection_Type=DirectionType
_HpnicfCBQoSAtmPvcApplyPolicyDirection_Object=MibTableColumn
hpnicfCBQoSAtmPvcApplyPolicyDirection=_HpnicfCBQoSAtmPvcApplyPolicyDirection_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,2,1,4),_HpnicfCBQoSAtmPvcApplyPolicyDirection_Type())
hpnicfCBQoSAtmPvcApplyPolicyDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcApplyPolicyDirection.setStatus(_A)
class _HpnicfCBQoSAtmPvcApplyPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HpnicfCBQoSAtmPvcApplyPolicyName_Type.__name__=_I
_HpnicfCBQoSAtmPvcApplyPolicyName_Object=MibTableColumn
hpnicfCBQoSAtmPvcApplyPolicyName=_HpnicfCBQoSAtmPvcApplyPolicyName_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,2,1,5),_HpnicfCBQoSAtmPvcApplyPolicyName_Type())
hpnicfCBQoSAtmPvcApplyPolicyName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcApplyPolicyName.setStatus(_A)
_HpnicfCBQoSAtmPvcApplyPolicyRowStatus_Type=RowStatus
_HpnicfCBQoSAtmPvcApplyPolicyRowStatus_Object=MibTableColumn
hpnicfCBQoSAtmPvcApplyPolicyRowStatus=_HpnicfCBQoSAtmPvcApplyPolicyRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,2,1,6),_HpnicfCBQoSAtmPvcApplyPolicyRowStatus_Type())
hpnicfCBQoSAtmPvcApplyPolicyRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcApplyPolicyRowStatus.setStatus(_A)
_HpnicfCBQoSVlanApplyPolicyTable_Object=MibTable
hpnicfCBQoSVlanApplyPolicyTable=_HpnicfCBQoSVlanApplyPolicyTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,3))
if mibBuilder.loadTexts:hpnicfCBQoSVlanApplyPolicyTable.setStatus(_A)
_HpnicfCBQoSVlanApplyPolicyEntry_Object=MibTableRow
hpnicfCBQoSVlanApplyPolicyEntry=_HpnicfCBQoSVlanApplyPolicyEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,3,1))
hpnicfCBQoSVlanApplyPolicyEntry.setIndexNames((0,_B,_X),(0,_B,_Y))
if mibBuilder.loadTexts:hpnicfCBQoSVlanApplyPolicyEntry.setStatus(_A)
_HpnicfCBQoSVlanApplyPolicyVlanid_Type=Integer32
_HpnicfCBQoSVlanApplyPolicyVlanid_Object=MibTableColumn
hpnicfCBQoSVlanApplyPolicyVlanid=_HpnicfCBQoSVlanApplyPolicyVlanid_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,3,1,1),_HpnicfCBQoSVlanApplyPolicyVlanid_Type())
hpnicfCBQoSVlanApplyPolicyVlanid.setMaxAccess(_e)
if mibBuilder.loadTexts:hpnicfCBQoSVlanApplyPolicyVlanid.setStatus(_A)
_HpnicfCBQoSVlanApplyPolicyDirection_Type=DirectionType
_HpnicfCBQoSVlanApplyPolicyDirection_Object=MibTableColumn
hpnicfCBQoSVlanApplyPolicyDirection=_HpnicfCBQoSVlanApplyPolicyDirection_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,3,1,2),_HpnicfCBQoSVlanApplyPolicyDirection_Type())
hpnicfCBQoSVlanApplyPolicyDirection.setMaxAccess(_e)
if mibBuilder.loadTexts:hpnicfCBQoSVlanApplyPolicyDirection.setStatus(_A)
class _HpnicfCBQoSVlanApplyPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_HpnicfCBQoSVlanApplyPolicyName_Type.__name__=_I
_HpnicfCBQoSVlanApplyPolicyName_Object=MibTableColumn
hpnicfCBQoSVlanApplyPolicyName=_HpnicfCBQoSVlanApplyPolicyName_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,3,1,3),_HpnicfCBQoSVlanApplyPolicyName_Type())
hpnicfCBQoSVlanApplyPolicyName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSVlanApplyPolicyName.setStatus(_A)
class _HpnicfCBQoSVlanApplyPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_HpnicfCBQoSVlanApplyPriority_Type.__name__=_E
_HpnicfCBQoSVlanApplyPriority_Object=MibTableColumn
hpnicfCBQoSVlanApplyPriority=_HpnicfCBQoSVlanApplyPriority_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,3,1,4),_HpnicfCBQoSVlanApplyPriority_Type())
hpnicfCBQoSVlanApplyPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSVlanApplyPriority.setStatus(_A)
_HpnicfCBQoSVlanApplyPolicyRowStatus_Type=RowStatus
_HpnicfCBQoSVlanApplyPolicyRowStatus_Object=MibTableColumn
hpnicfCBQoSVlanApplyPolicyRowStatus=_HpnicfCBQoSVlanApplyPolicyRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,3,1,5),_HpnicfCBQoSVlanApplyPolicyRowStatus_Type())
hpnicfCBQoSVlanApplyPolicyRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSVlanApplyPolicyRowStatus.setStatus(_A)
class _HpnicfCBQoSVlanApplyPolicyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_f,1),(_W,2),(_g,3)))
_HpnicfCBQoSVlanApplyPolicyStatus_Type.__name__=_E
_HpnicfCBQoSVlanApplyPolicyStatus_Object=MibTableColumn
hpnicfCBQoSVlanApplyPolicyStatus=_HpnicfCBQoSVlanApplyPolicyStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,3,1,6),_HpnicfCBQoSVlanApplyPolicyStatus_Type())
hpnicfCBQoSVlanApplyPolicyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSVlanApplyPolicyStatus.setStatus(_A)
_HpnicfCBQoSFrClassApplyPolicyTable_Object=MibTable
hpnicfCBQoSFrClassApplyPolicyTable=_HpnicfCBQoSFrClassApplyPolicyTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,4))
if mibBuilder.loadTexts:hpnicfCBQoSFrClassApplyPolicyTable.setStatus(_A)
_HpnicfCBQoSFrClassApplyPolicyEntry_Object=MibTableRow
hpnicfCBQoSFrClassApplyPolicyEntry=_HpnicfCBQoSFrClassApplyPolicyEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,4,1))
hpnicfCBQoSFrClassApplyPolicyEntry.setIndexNames((0,_B,_A2),(0,_B,_A3))
if mibBuilder.loadTexts:hpnicfCBQoSFrClassApplyPolicyEntry.setStatus(_A)
class _HpnicfCBQoSFrClassApplyPolicyFrClassName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HpnicfCBQoSFrClassApplyPolicyFrClassName_Type.__name__=_I
_HpnicfCBQoSFrClassApplyPolicyFrClassName_Object=MibTableColumn
hpnicfCBQoSFrClassApplyPolicyFrClassName=_HpnicfCBQoSFrClassApplyPolicyFrClassName_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,4,1,1),_HpnicfCBQoSFrClassApplyPolicyFrClassName_Type())
hpnicfCBQoSFrClassApplyPolicyFrClassName.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSFrClassApplyPolicyFrClassName.setStatus(_A)
_HpnicfCBQoSFrClassApplyPolicyDirection_Type=DirectionType
_HpnicfCBQoSFrClassApplyPolicyDirection_Object=MibTableColumn
hpnicfCBQoSFrClassApplyPolicyDirection=_HpnicfCBQoSFrClassApplyPolicyDirection_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,4,1,2),_HpnicfCBQoSFrClassApplyPolicyDirection_Type())
hpnicfCBQoSFrClassApplyPolicyDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSFrClassApplyPolicyDirection.setStatus(_A)
class _HpnicfCBQoSFrClassApplyPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HpnicfCBQoSFrClassApplyPolicyName_Type.__name__=_I
_HpnicfCBQoSFrClassApplyPolicyName_Object=MibTableColumn
hpnicfCBQoSFrClassApplyPolicyName=_HpnicfCBQoSFrClassApplyPolicyName_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,4,1,3),_HpnicfCBQoSFrClassApplyPolicyName_Type())
hpnicfCBQoSFrClassApplyPolicyName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSFrClassApplyPolicyName.setStatus(_A)
_HpnicfCBQoSFrClassApplyPolicyRowStatus_Type=RowStatus
_HpnicfCBQoSFrClassApplyPolicyRowStatus_Object=MibTableColumn
hpnicfCBQoSFrClassApplyPolicyRowStatus=_HpnicfCBQoSFrClassApplyPolicyRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,4,1,4),_HpnicfCBQoSFrClassApplyPolicyRowStatus_Type())
hpnicfCBQoSFrClassApplyPolicyRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSFrClassApplyPolicyRowStatus.setStatus(_A)
_HpnicfCBQoSFrPvcApplyPolicyTable_Object=MibTable
hpnicfCBQoSFrPvcApplyPolicyTable=_HpnicfCBQoSFrPvcApplyPolicyTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,5))
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcApplyPolicyTable.setStatus(_A)
_HpnicfCBQoSFrPvcApplyPolicyEntry_Object=MibTableRow
hpnicfCBQoSFrPvcApplyPolicyEntry=_HpnicfCBQoSFrPvcApplyPolicyEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,5,1))
hpnicfCBQoSFrPvcApplyPolicyEntry.setIndexNames((0,_B,_P),(0,_B,_Q),(0,_B,_S))
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcApplyPolicyEntry.setStatus(_A)
_HpnicfCBQoSFrPvcApplyPolicyIfIndex_Type=Integer32
_HpnicfCBQoSFrPvcApplyPolicyIfIndex_Object=MibTableColumn
hpnicfCBQoSFrPvcApplyPolicyIfIndex=_HpnicfCBQoSFrPvcApplyPolicyIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,5,1,1),_HpnicfCBQoSFrPvcApplyPolicyIfIndex_Type())
hpnicfCBQoSFrPvcApplyPolicyIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcApplyPolicyIfIndex.setStatus(_A)
class _HpnicfCBQoSFrPvcApplyPolicyDlciNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,1007))
_HpnicfCBQoSFrPvcApplyPolicyDlciNum_Type.__name__=_E
_HpnicfCBQoSFrPvcApplyPolicyDlciNum_Object=MibTableColumn
hpnicfCBQoSFrPvcApplyPolicyDlciNum=_HpnicfCBQoSFrPvcApplyPolicyDlciNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,5,1,2),_HpnicfCBQoSFrPvcApplyPolicyDlciNum_Type())
hpnicfCBQoSFrPvcApplyPolicyDlciNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcApplyPolicyDlciNum.setStatus(_A)
_HpnicfCBQoSFrPvcApplyPolicyDirection_Type=DirectionType
_HpnicfCBQoSFrPvcApplyPolicyDirection_Object=MibTableColumn
hpnicfCBQoSFrPvcApplyPolicyDirection=_HpnicfCBQoSFrPvcApplyPolicyDirection_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,5,1,3),_HpnicfCBQoSFrPvcApplyPolicyDirection_Type())
hpnicfCBQoSFrPvcApplyPolicyDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcApplyPolicyDirection.setStatus(_A)
class _HpnicfCBQoSFrPvcApplyPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HpnicfCBQoSFrPvcApplyPolicyName_Type.__name__=_I
_HpnicfCBQoSFrPvcApplyPolicyName_Object=MibTableColumn
hpnicfCBQoSFrPvcApplyPolicyName=_HpnicfCBQoSFrPvcApplyPolicyName_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,5,1,4),_HpnicfCBQoSFrPvcApplyPolicyName_Type())
hpnicfCBQoSFrPvcApplyPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcApplyPolicyName.setStatus(_A)
_HpnicfCBQoSFrPvcApplyPolicyRowStatus_Type=RowStatus
_HpnicfCBQoSFrPvcApplyPolicyRowStatus_Object=MibTableColumn
hpnicfCBQoSFrPvcApplyPolicyRowStatus=_HpnicfCBQoSFrPvcApplyPolicyRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,5,1,5),_HpnicfCBQoSFrPvcApplyPolicyRowStatus_Type())
hpnicfCBQoSFrPvcApplyPolicyRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcApplyPolicyRowStatus.setStatus(_A)
_HpnicfCBQoSGlobalApplyTable_Object=MibTable
hpnicfCBQoSGlobalApplyTable=_HpnicfCBQoSGlobalApplyTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,6))
if mibBuilder.loadTexts:hpnicfCBQoSGlobalApplyTable.setStatus(_A)
_HpnicfCBQoSGlobalApplyEntry_Object=MibTableRow
hpnicfCBQoSGlobalApplyEntry=_HpnicfCBQoSGlobalApplyEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,6,1))
hpnicfCBQoSGlobalApplyEntry.setIndexNames((0,_B,_A4))
if mibBuilder.loadTexts:hpnicfCBQoSGlobalApplyEntry.setStatus(_A)
_HpnicfCBQoSGlobalApplyDirection_Type=DirectionType
_HpnicfCBQoSGlobalApplyDirection_Object=MibTableColumn
hpnicfCBQoSGlobalApplyDirection=_HpnicfCBQoSGlobalApplyDirection_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,6,1,1),_HpnicfCBQoSGlobalApplyDirection_Type())
hpnicfCBQoSGlobalApplyDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSGlobalApplyDirection.setStatus(_A)
class _HpnicfCBQoSGlobalApplyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HpnicfCBQoSGlobalApplyName_Type.__name__=_I
_HpnicfCBQoSGlobalApplyName_Object=MibTableColumn
hpnicfCBQoSGlobalApplyName=_HpnicfCBQoSGlobalApplyName_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,6,1,2),_HpnicfCBQoSGlobalApplyName_Type())
hpnicfCBQoSGlobalApplyName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSGlobalApplyName.setStatus(_A)
_HpnicfCBQoSGlobalApplyRowStatus_Type=RowStatus
_HpnicfCBQoSGlobalApplyRowStatus_Object=MibTableColumn
hpnicfCBQoSGlobalApplyRowStatus=_HpnicfCBQoSGlobalApplyRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,6,1,3),_HpnicfCBQoSGlobalApplyRowStatus_Type())
hpnicfCBQoSGlobalApplyRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSGlobalApplyRowStatus.setStatus(_A)
class _HpnicfCBQoSGlobalApplyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_f,1),(_W,2),(_g,3)))
_HpnicfCBQoSGlobalApplyStatus_Type.__name__=_E
_HpnicfCBQoSGlobalApplyStatus_Object=MibTableColumn
hpnicfCBQoSGlobalApplyStatus=_HpnicfCBQoSGlobalApplyStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,6,1,4),_HpnicfCBQoSGlobalApplyStatus_Type())
hpnicfCBQoSGlobalApplyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSGlobalApplyStatus.setStatus(_A)
_HpnicfCBQoSCpApplyPolicyTable_Object=MibTable
hpnicfCBQoSCpApplyPolicyTable=_HpnicfCBQoSCpApplyPolicyTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,7))
if mibBuilder.loadTexts:hpnicfCBQoSCpApplyPolicyTable.setStatus(_A)
_HpnicfCBQoSCpApplyPolicyEntry_Object=MibTableRow
hpnicfCBQoSCpApplyPolicyEntry=_HpnicfCBQoSCpApplyPolicyEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,7,1))
hpnicfCBQoSCpApplyPolicyEntry.setIndexNames((0,_B,_A5),(0,_B,_A6),(0,_B,_A7))
if mibBuilder.loadTexts:hpnicfCBQoSCpApplyPolicyEntry.setStatus(_A)
_HpnicfCBQoSCpApplyPolicyChassis_Type=Unsigned32
_HpnicfCBQoSCpApplyPolicyChassis_Object=MibTableColumn
hpnicfCBQoSCpApplyPolicyChassis=_HpnicfCBQoSCpApplyPolicyChassis_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,7,1,1),_HpnicfCBQoSCpApplyPolicyChassis_Type())
hpnicfCBQoSCpApplyPolicyChassis.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSCpApplyPolicyChassis.setStatus(_A)
_HpnicfCBQoSCpApplyPolicySlot_Type=Unsigned32
_HpnicfCBQoSCpApplyPolicySlot_Object=MibTableColumn
hpnicfCBQoSCpApplyPolicySlot=_HpnicfCBQoSCpApplyPolicySlot_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,7,1,2),_HpnicfCBQoSCpApplyPolicySlot_Type())
hpnicfCBQoSCpApplyPolicySlot.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSCpApplyPolicySlot.setStatus(_A)
_HpnicfCBQoSCpApplyPolicyDirection_Type=DirectionType
_HpnicfCBQoSCpApplyPolicyDirection_Object=MibTableColumn
hpnicfCBQoSCpApplyPolicyDirection=_HpnicfCBQoSCpApplyPolicyDirection_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,7,1,3),_HpnicfCBQoSCpApplyPolicyDirection_Type())
hpnicfCBQoSCpApplyPolicyDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSCpApplyPolicyDirection.setStatus(_A)
class _HpnicfCBQoSCpApplyPolicyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HpnicfCBQoSCpApplyPolicyName_Type.__name__=_I
_HpnicfCBQoSCpApplyPolicyName_Object=MibTableColumn
hpnicfCBQoSCpApplyPolicyName=_HpnicfCBQoSCpApplyPolicyName_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,7,1,4),_HpnicfCBQoSCpApplyPolicyName_Type())
hpnicfCBQoSCpApplyPolicyName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSCpApplyPolicyName.setStatus(_A)
class _HpnicfCBQoSCpApplyPolicyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_f,1),(_W,2),(_g,3)))
_HpnicfCBQoSCpApplyPolicyStatus_Type.__name__=_E
_HpnicfCBQoSCpApplyPolicyStatus_Object=MibTableColumn
hpnicfCBQoSCpApplyPolicyStatus=_HpnicfCBQoSCpApplyPolicyStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,7,1,5),_HpnicfCBQoSCpApplyPolicyStatus_Type())
hpnicfCBQoSCpApplyPolicyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSCpApplyPolicyStatus.setStatus(_A)
_HpnicfCBQoSCpApplyRowStatus_Type=RowStatus
_HpnicfCBQoSCpApplyRowStatus_Object=MibTableColumn
hpnicfCBQoSCpApplyRowStatus=_HpnicfCBQoSCpApplyRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,4,7,1,6),_HpnicfCBQoSCpApplyRowStatus_Type())
hpnicfCBQoSCpApplyRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfCBQoSCpApplyRowStatus.setStatus(_A)
_HpnicfCBQoSApplyPolicyStaticsObjects_ObjectIdentity=ObjectIdentity
hpnicfCBQoSApplyPolicyStaticsObjects=_HpnicfCBQoSApplyPolicyStaticsObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5))
_HpnicfCBQoSIfStaticsObjects_ObjectIdentity=ObjectIdentity
hpnicfCBQoSIfStaticsObjects=_HpnicfCBQoSIfStaticsObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1))
_HpnicfCBQoSIfCbqRunInfoTable_Object=MibTable
hpnicfCBQoSIfCbqRunInfoTable=_HpnicfCBQoSIfCbqRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,1))
if mibBuilder.loadTexts:hpnicfCBQoSIfCbqRunInfoTable.setStatus(_A)
_HpnicfCBQoSIfCbqRunInfoEntry_Object=MibTableRow
hpnicfCBQoSIfCbqRunInfoEntry=_HpnicfCBQoSIfCbqRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,1,1))
hpnicfCBQoSIfCbqRunInfoEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:hpnicfCBQoSIfCbqRunInfoEntry.setStatus(_A)
_HpnicfCBQoSIfCbqQueueSize_Type=Integer32
_HpnicfCBQoSIfCbqQueueSize_Object=MibTableColumn
hpnicfCBQoSIfCbqQueueSize=_HpnicfCBQoSIfCbqQueueSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,1,1,1),_HpnicfCBQoSIfCbqQueueSize_Type())
hpnicfCBQoSIfCbqQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfCbqQueueSize.setStatus(_A)
_HpnicfCBQoSIfCbqDiscard_Type=Counter64
_HpnicfCBQoSIfCbqDiscard_Object=MibTableColumn
hpnicfCBQoSIfCbqDiscard=_HpnicfCBQoSIfCbqDiscard_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,1,1,2),_HpnicfCBQoSIfCbqDiscard_Type())
hpnicfCBQoSIfCbqDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfCbqDiscard.setStatus(_A)
_HpnicfCBQoSIfCbqEfQueueSize_Type=Integer32
_HpnicfCBQoSIfCbqEfQueueSize_Object=MibTableColumn
hpnicfCBQoSIfCbqEfQueueSize=_HpnicfCBQoSIfCbqEfQueueSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,1,1,3),_HpnicfCBQoSIfCbqEfQueueSize_Type())
hpnicfCBQoSIfCbqEfQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfCbqEfQueueSize.setStatus(_A)
_HpnicfCBQoSIfCbqAfQueueSize_Type=Integer32
_HpnicfCBQoSIfCbqAfQueueSize_Object=MibTableColumn
hpnicfCBQoSIfCbqAfQueueSize=_HpnicfCBQoSIfCbqAfQueueSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,1,1,4),_HpnicfCBQoSIfCbqAfQueueSize_Type())
hpnicfCBQoSIfCbqAfQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfCbqAfQueueSize.setStatus(_A)
_HpnicfCBQoSIfCbqBeQueueSize_Type=Integer32
_HpnicfCBQoSIfCbqBeQueueSize_Object=MibTableColumn
hpnicfCBQoSIfCbqBeQueueSize=_HpnicfCBQoSIfCbqBeQueueSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,1,1,5),_HpnicfCBQoSIfCbqBeQueueSize_Type())
hpnicfCBQoSIfCbqBeQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfCbqBeQueueSize.setStatus(_A)
_HpnicfCBQoSIfCbqBeActiveQueueNum_Type=Integer32
_HpnicfCBQoSIfCbqBeActiveQueueNum_Object=MibTableColumn
hpnicfCBQoSIfCbqBeActiveQueueNum=_HpnicfCBQoSIfCbqBeActiveQueueNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,1,1,6),_HpnicfCBQoSIfCbqBeActiveQueueNum_Type())
hpnicfCBQoSIfCbqBeActiveQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfCbqBeActiveQueueNum.setStatus(_A)
_HpnicfCBQoSIfCbqBeMaxActiveQueueNum_Type=Integer32
_HpnicfCBQoSIfCbqBeMaxActiveQueueNum_Object=MibTableColumn
hpnicfCBQoSIfCbqBeMaxActiveQueueNum=_HpnicfCBQoSIfCbqBeMaxActiveQueueNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,1,1,7),_HpnicfCBQoSIfCbqBeMaxActiveQueueNum_Type())
hpnicfCBQoSIfCbqBeMaxActiveQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfCbqBeMaxActiveQueueNum.setStatus(_A)
_HpnicfCBQoSIfCbqBeTotalQueueNum_Type=Integer32
_HpnicfCBQoSIfCbqBeTotalQueueNum_Object=MibTableColumn
hpnicfCBQoSIfCbqBeTotalQueueNum=_HpnicfCBQoSIfCbqBeTotalQueueNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,1,1,8),_HpnicfCBQoSIfCbqBeTotalQueueNum_Type())
hpnicfCBQoSIfCbqBeTotalQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfCbqBeTotalQueueNum.setStatus(_A)
_HpnicfCBQoSIfCbqAfAllocatedQueueNum_Type=Integer32
_HpnicfCBQoSIfCbqAfAllocatedQueueNum_Object=MibTableColumn
hpnicfCBQoSIfCbqAfAllocatedQueueNum=_HpnicfCBQoSIfCbqAfAllocatedQueueNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,1,1,9),_HpnicfCBQoSIfCbqAfAllocatedQueueNum_Type())
hpnicfCBQoSIfCbqAfAllocatedQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfCbqAfAllocatedQueueNum.setStatus(_A)
_HpnicfCBQoSIfClassMatchRunInfoTable_Object=MibTable
hpnicfCBQoSIfClassMatchRunInfoTable=_HpnicfCBQoSIfClassMatchRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,2))
if mibBuilder.loadTexts:hpnicfCBQoSIfClassMatchRunInfoTable.setStatus(_A)
_HpnicfCBQoSIfClassMatchRunInfoEntry_Object=MibTableRow
hpnicfCBQoSIfClassMatchRunInfoEntry=_HpnicfCBQoSIfClassMatchRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,2,1))
hpnicfCBQoSIfClassMatchRunInfoEntry.setIndexNames((0,_B,_J),(0,_B,_L),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfCBQoSIfClassMatchRunInfoEntry.setStatus(_A)
_HpnicfCBQoSIfClassMatchedPackets_Type=Counter64
_HpnicfCBQoSIfClassMatchedPackets_Object=MibTableColumn
hpnicfCBQoSIfClassMatchedPackets=_HpnicfCBQoSIfClassMatchedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,2,1,1),_HpnicfCBQoSIfClassMatchedPackets_Type())
hpnicfCBQoSIfClassMatchedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfClassMatchedPackets.setStatus(_A)
_HpnicfCBQoSIfClassMatchedBytes_Type=Counter64
_HpnicfCBQoSIfClassMatchedBytes_Object=MibTableColumn
hpnicfCBQoSIfClassMatchedBytes=_HpnicfCBQoSIfClassMatchedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,2,1,2),_HpnicfCBQoSIfClassMatchedBytes_Type())
hpnicfCBQoSIfClassMatchedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfClassMatchedBytes.setStatus(_A)
_HpnicfCBQoSIfClassAverageRate_Type=Counter64
_HpnicfCBQoSIfClassAverageRate_Object=MibTableColumn
hpnicfCBQoSIfClassAverageRate=_HpnicfCBQoSIfClassAverageRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,2,1,3),_HpnicfCBQoSIfClassAverageRate_Type())
hpnicfCBQoSIfClassAverageRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfClassAverageRate.setStatus(_A)
_HpnicfCBQoSIfCarRunInfoTable_Object=MibTable
hpnicfCBQoSIfCarRunInfoTable=_HpnicfCBQoSIfCarRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,3))
if mibBuilder.loadTexts:hpnicfCBQoSIfCarRunInfoTable.setStatus(_A)
_HpnicfCBQoSIfCarRunInfoEntry_Object=MibTableRow
hpnicfCBQoSIfCarRunInfoEntry=_HpnicfCBQoSIfCarRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,3,1))
hpnicfCBQoSIfCarRunInfoEntry.setIndexNames((0,_B,_J),(0,_B,_L),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfCBQoSIfCarRunInfoEntry.setStatus(_A)
_HpnicfCBQoSIfCarGreenPackets_Type=Counter64
_HpnicfCBQoSIfCarGreenPackets_Object=MibTableColumn
hpnicfCBQoSIfCarGreenPackets=_HpnicfCBQoSIfCarGreenPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,3,1,1),_HpnicfCBQoSIfCarGreenPackets_Type())
hpnicfCBQoSIfCarGreenPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfCarGreenPackets.setStatus(_A)
_HpnicfCBQoSIfCarGreenBytes_Type=Counter64
_HpnicfCBQoSIfCarGreenBytes_Object=MibTableColumn
hpnicfCBQoSIfCarGreenBytes=_HpnicfCBQoSIfCarGreenBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,3,1,2),_HpnicfCBQoSIfCarGreenBytes_Type())
hpnicfCBQoSIfCarGreenBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfCarGreenBytes.setStatus(_A)
_HpnicfCBQoSIfCarRedPackets_Type=Counter64
_HpnicfCBQoSIfCarRedPackets_Object=MibTableColumn
hpnicfCBQoSIfCarRedPackets=_HpnicfCBQoSIfCarRedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,3,1,3),_HpnicfCBQoSIfCarRedPackets_Type())
hpnicfCBQoSIfCarRedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfCarRedPackets.setStatus(_A)
_HpnicfCBQoSIfCarRedBytes_Type=Counter64
_HpnicfCBQoSIfCarRedBytes_Object=MibTableColumn
hpnicfCBQoSIfCarRedBytes=_HpnicfCBQoSIfCarRedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,3,1,4),_HpnicfCBQoSIfCarRedBytes_Type())
hpnicfCBQoSIfCarRedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfCarRedBytes.setStatus(_A)
_HpnicfCBQoSIfCarYellowPackets_Type=Counter64
_HpnicfCBQoSIfCarYellowPackets_Object=MibTableColumn
hpnicfCBQoSIfCarYellowPackets=_HpnicfCBQoSIfCarYellowPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,3,1,5),_HpnicfCBQoSIfCarYellowPackets_Type())
hpnicfCBQoSIfCarYellowPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfCarYellowPackets.setStatus(_A)
_HpnicfCBQoSIfCarYellowBytes_Type=Counter64
_HpnicfCBQoSIfCarYellowBytes_Object=MibTableColumn
hpnicfCBQoSIfCarYellowBytes=_HpnicfCBQoSIfCarYellowBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,3,1,6),_HpnicfCBQoSIfCarYellowBytes_Type())
hpnicfCBQoSIfCarYellowBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfCarYellowBytes.setStatus(_A)
_HpnicfCBQoSIfGtsRunInfoTable_Object=MibTable
hpnicfCBQoSIfGtsRunInfoTable=_HpnicfCBQoSIfGtsRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,4))
if mibBuilder.loadTexts:hpnicfCBQoSIfGtsRunInfoTable.setStatus(_A)
_HpnicfCBQoSIfGtsRunInfoEntry_Object=MibTableRow
hpnicfCBQoSIfGtsRunInfoEntry=_HpnicfCBQoSIfGtsRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,4,1))
hpnicfCBQoSIfGtsRunInfoEntry.setIndexNames((0,_B,_J),(0,_B,_L),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfCBQoSIfGtsRunInfoEntry.setStatus(_A)
_HpnicfCBQoSIfGtsPassedPackets_Type=Counter64
_HpnicfCBQoSIfGtsPassedPackets_Object=MibTableColumn
hpnicfCBQoSIfGtsPassedPackets=_HpnicfCBQoSIfGtsPassedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,4,1,1),_HpnicfCBQoSIfGtsPassedPackets_Type())
hpnicfCBQoSIfGtsPassedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfGtsPassedPackets.setStatus(_A)
_HpnicfCBQoSIfGtsPassedBytes_Type=Counter64
_HpnicfCBQoSIfGtsPassedBytes_Object=MibTableColumn
hpnicfCBQoSIfGtsPassedBytes=_HpnicfCBQoSIfGtsPassedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,4,1,2),_HpnicfCBQoSIfGtsPassedBytes_Type())
hpnicfCBQoSIfGtsPassedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfGtsPassedBytes.setStatus(_A)
_HpnicfCBQoSIfGtsDiscardedPackets_Type=Counter64
_HpnicfCBQoSIfGtsDiscardedPackets_Object=MibTableColumn
hpnicfCBQoSIfGtsDiscardedPackets=_HpnicfCBQoSIfGtsDiscardedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,4,1,3),_HpnicfCBQoSIfGtsDiscardedPackets_Type())
hpnicfCBQoSIfGtsDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfGtsDiscardedPackets.setStatus(_A)
_HpnicfCBQoSIfGtsDiscardedBytes_Type=Counter64
_HpnicfCBQoSIfGtsDiscardedBytes_Object=MibTableColumn
hpnicfCBQoSIfGtsDiscardedBytes=_HpnicfCBQoSIfGtsDiscardedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,4,1,4),_HpnicfCBQoSIfGtsDiscardedBytes_Type())
hpnicfCBQoSIfGtsDiscardedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfGtsDiscardedBytes.setStatus(_A)
_HpnicfCBQoSIfGtsDelayedPackets_Type=Counter64
_HpnicfCBQoSIfGtsDelayedPackets_Object=MibTableColumn
hpnicfCBQoSIfGtsDelayedPackets=_HpnicfCBQoSIfGtsDelayedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,4,1,5),_HpnicfCBQoSIfGtsDelayedPackets_Type())
hpnicfCBQoSIfGtsDelayedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfGtsDelayedPackets.setStatus(_A)
_HpnicfCBQoSIfGtsDelayedBytes_Type=Counter64
_HpnicfCBQoSIfGtsDelayedBytes_Object=MibTableColumn
hpnicfCBQoSIfGtsDelayedBytes=_HpnicfCBQoSIfGtsDelayedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,4,1,6),_HpnicfCBQoSIfGtsDelayedBytes_Type())
hpnicfCBQoSIfGtsDelayedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfGtsDelayedBytes.setStatus(_A)
_HpnicfCBQoSIfGtsQueueSize_Type=Integer32
_HpnicfCBQoSIfGtsQueueSize_Object=MibTableColumn
hpnicfCBQoSIfGtsQueueSize=_HpnicfCBQoSIfGtsQueueSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,4,1,7),_HpnicfCBQoSIfGtsQueueSize_Type())
hpnicfCBQoSIfGtsQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfGtsQueueSize.setStatus(_A)
_HpnicfCBQoSIfRemarkRunInfoTable_Object=MibTable
hpnicfCBQoSIfRemarkRunInfoTable=_HpnicfCBQoSIfRemarkRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,5))
if mibBuilder.loadTexts:hpnicfCBQoSIfRemarkRunInfoTable.setStatus(_A)
_HpnicfCBQoSIfRemarkRunInfoEntry_Object=MibTableRow
hpnicfCBQoSIfRemarkRunInfoEntry=_HpnicfCBQoSIfRemarkRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,5,1))
hpnicfCBQoSIfRemarkRunInfoEntry.setIndexNames((0,_B,_J),(0,_B,_L),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfCBQoSIfRemarkRunInfoEntry.setStatus(_A)
_HpnicfCBQoSIfRemarkedPackets_Type=Counter64
_HpnicfCBQoSIfRemarkedPackets_Object=MibTableColumn
hpnicfCBQoSIfRemarkedPackets=_HpnicfCBQoSIfRemarkedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,5,1,1),_HpnicfCBQoSIfRemarkedPackets_Type())
hpnicfCBQoSIfRemarkedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfRemarkedPackets.setStatus(_A)
_HpnicfCBQoSIfQueueRunInfoTable_Object=MibTable
hpnicfCBQoSIfQueueRunInfoTable=_HpnicfCBQoSIfQueueRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,6))
if mibBuilder.loadTexts:hpnicfCBQoSIfQueueRunInfoTable.setStatus(_A)
_HpnicfCBQoSIfQueueRunInfoEntry_Object=MibTableRow
hpnicfCBQoSIfQueueRunInfoEntry=_HpnicfCBQoSIfQueueRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,6,1))
hpnicfCBQoSIfQueueRunInfoEntry.setIndexNames((0,_B,_J),(0,_B,_L),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfCBQoSIfQueueRunInfoEntry.setStatus(_A)
_HpnicfCBQoSIfQueueMatchedPackets_Type=Counter64
_HpnicfCBQoSIfQueueMatchedPackets_Object=MibTableColumn
hpnicfCBQoSIfQueueMatchedPackets=_HpnicfCBQoSIfQueueMatchedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,6,1,1),_HpnicfCBQoSIfQueueMatchedPackets_Type())
hpnicfCBQoSIfQueueMatchedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfQueueMatchedPackets.setStatus(_A)
_HpnicfCBQoSIfQueueMatchedBytes_Type=Counter64
_HpnicfCBQoSIfQueueMatchedBytes_Object=MibTableColumn
hpnicfCBQoSIfQueueMatchedBytes=_HpnicfCBQoSIfQueueMatchedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,6,1,2),_HpnicfCBQoSIfQueueMatchedBytes_Type())
hpnicfCBQoSIfQueueMatchedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfQueueMatchedBytes.setStatus(_A)
_HpnicfCBQoSIfQueueEnqueuedPackets_Type=Counter64
_HpnicfCBQoSIfQueueEnqueuedPackets_Object=MibTableColumn
hpnicfCBQoSIfQueueEnqueuedPackets=_HpnicfCBQoSIfQueueEnqueuedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,6,1,3),_HpnicfCBQoSIfQueueEnqueuedPackets_Type())
hpnicfCBQoSIfQueueEnqueuedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfQueueEnqueuedPackets.setStatus(_A)
_HpnicfCBQoSIfQueueEnqueuedBytes_Type=Counter64
_HpnicfCBQoSIfQueueEnqueuedBytes_Object=MibTableColumn
hpnicfCBQoSIfQueueEnqueuedBytes=_HpnicfCBQoSIfQueueEnqueuedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,6,1,4),_HpnicfCBQoSIfQueueEnqueuedBytes_Type())
hpnicfCBQoSIfQueueEnqueuedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfQueueEnqueuedBytes.setStatus(_A)
_HpnicfCBQoSIfQueueDiscardedPackets_Type=Counter64
_HpnicfCBQoSIfQueueDiscardedPackets_Object=MibTableColumn
hpnicfCBQoSIfQueueDiscardedPackets=_HpnicfCBQoSIfQueueDiscardedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,6,1,5),_HpnicfCBQoSIfQueueDiscardedPackets_Type())
hpnicfCBQoSIfQueueDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfQueueDiscardedPackets.setStatus(_A)
_HpnicfCBQoSIfQueueDiscardedBytes_Type=Counter64
_HpnicfCBQoSIfQueueDiscardedBytes_Object=MibTableColumn
hpnicfCBQoSIfQueueDiscardedBytes=_HpnicfCBQoSIfQueueDiscardedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,6,1,6),_HpnicfCBQoSIfQueueDiscardedBytes_Type())
hpnicfCBQoSIfQueueDiscardedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfQueueDiscardedBytes.setStatus(_A)
_HpnicfCBQoSIfWredRunInfoTable_Object=MibTable
hpnicfCBQoSIfWredRunInfoTable=_HpnicfCBQoSIfWredRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,7))
if mibBuilder.loadTexts:hpnicfCBQoSIfWredRunInfoTable.setStatus(_A)
_HpnicfCBQoSIfWredRunInfoEntry_Object=MibTableRow
hpnicfCBQoSIfWredRunInfoEntry=_HpnicfCBQoSIfWredRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,7,1))
hpnicfCBQoSIfWredRunInfoEntry.setIndexNames((0,_B,_J),(0,_B,_L),(0,_B,_G),(0,_B,_T))
if mibBuilder.loadTexts:hpnicfCBQoSIfWredRunInfoEntry.setStatus(_A)
_HpnicfCBQoSIfWredRandomDiscardedPackets_Type=Counter64
_HpnicfCBQoSIfWredRandomDiscardedPackets_Object=MibTableColumn
hpnicfCBQoSIfWredRandomDiscardedPackets=_HpnicfCBQoSIfWredRandomDiscardedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,7,1,1),_HpnicfCBQoSIfWredRandomDiscardedPackets_Type())
hpnicfCBQoSIfWredRandomDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfWredRandomDiscardedPackets.setStatus(_A)
_HpnicfCBQoSIfWredTailDiscardedPackets_Type=Counter64
_HpnicfCBQoSIfWredTailDiscardedPackets_Object=MibTableColumn
hpnicfCBQoSIfWredTailDiscardedPackets=_HpnicfCBQoSIfWredTailDiscardedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,7,1,2),_HpnicfCBQoSIfWredTailDiscardedPackets_Type())
hpnicfCBQoSIfWredTailDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfWredTailDiscardedPackets.setStatus(_A)
_HpnicfCBQoSIfAccountingRunInfoTable_Object=MibTable
hpnicfCBQoSIfAccountingRunInfoTable=_HpnicfCBQoSIfAccountingRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,8))
if mibBuilder.loadTexts:hpnicfCBQoSIfAccountingRunInfoTable.setStatus(_A)
_HpnicfCBQoSIfAccountingRunInfoEntry_Object=MibTableRow
hpnicfCBQoSIfAccountingRunInfoEntry=_HpnicfCBQoSIfAccountingRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,8,1))
hpnicfCBQoSIfAccountingRunInfoEntry.setIndexNames((0,_B,_J),(0,_B,_L),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfCBQoSIfAccountingRunInfoEntry.setStatus(_A)
_HpnicfCBQoSIfAccountingPackets_Type=Counter64
_HpnicfCBQoSIfAccountingPackets_Object=MibTableColumn
hpnicfCBQoSIfAccountingPackets=_HpnicfCBQoSIfAccountingPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,8,1,1),_HpnicfCBQoSIfAccountingPackets_Type())
hpnicfCBQoSIfAccountingPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfAccountingPackets.setStatus(_A)
_HpnicfCBQoSIfAccountingBytes_Type=Counter64
_HpnicfCBQoSIfAccountingBytes_Object=MibTableColumn
hpnicfCBQoSIfAccountingBytes=_HpnicfCBQoSIfAccountingBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,1,8,1,2),_HpnicfCBQoSIfAccountingBytes_Type())
hpnicfCBQoSIfAccountingBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIfAccountingBytes.setStatus(_A)
_HpnicfCBQoSAtmPvcStaticsObjects_ObjectIdentity=ObjectIdentity
hpnicfCBQoSAtmPvcStaticsObjects=_HpnicfCBQoSAtmPvcStaticsObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2))
_HpnicfCBQoSAtmPvcCbqRunInfoTable_Object=MibTable
hpnicfCBQoSAtmPvcCbqRunInfoTable=_HpnicfCBQoSAtmPvcCbqRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,1))
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcCbqRunInfoTable.setStatus(_A)
_HpnicfCBQoSAtmPvcCbqRunInfoEntry_Object=MibTableRow
hpnicfCBQoSAtmPvcCbqRunInfoEntry=_HpnicfCBQoSAtmPvcCbqRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,1,1))
hpnicfCBQoSAtmPvcCbqRunInfoEntry.setIndexNames((0,_B,_M),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcCbqRunInfoEntry.setStatus(_A)
_HpnicfCBQoSAtmPvcCbqQueueSize_Type=Integer32
_HpnicfCBQoSAtmPvcCbqQueueSize_Object=MibTableColumn
hpnicfCBQoSAtmPvcCbqQueueSize=_HpnicfCBQoSAtmPvcCbqQueueSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,1,1,1),_HpnicfCBQoSAtmPvcCbqQueueSize_Type())
hpnicfCBQoSAtmPvcCbqQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcCbqQueueSize.setStatus(_A)
_HpnicfCBQoSAtmPvcCbqDiscard_Type=Counter64
_HpnicfCBQoSAtmPvcCbqDiscard_Object=MibTableColumn
hpnicfCBQoSAtmPvcCbqDiscard=_HpnicfCBQoSAtmPvcCbqDiscard_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,1,1,2),_HpnicfCBQoSAtmPvcCbqDiscard_Type())
hpnicfCBQoSAtmPvcCbqDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcCbqDiscard.setStatus(_A)
_HpnicfCBQoSAtmPvcCbqEfQueueSize_Type=Integer32
_HpnicfCBQoSAtmPvcCbqEfQueueSize_Object=MibTableColumn
hpnicfCBQoSAtmPvcCbqEfQueueSize=_HpnicfCBQoSAtmPvcCbqEfQueueSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,1,1,3),_HpnicfCBQoSAtmPvcCbqEfQueueSize_Type())
hpnicfCBQoSAtmPvcCbqEfQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcCbqEfQueueSize.setStatus(_A)
_HpnicfCBQoSAtmPvcCbqAfQueueSize_Type=Integer32
_HpnicfCBQoSAtmPvcCbqAfQueueSize_Object=MibTableColumn
hpnicfCBQoSAtmPvcCbqAfQueueSize=_HpnicfCBQoSAtmPvcCbqAfQueueSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,1,1,4),_HpnicfCBQoSAtmPvcCbqAfQueueSize_Type())
hpnicfCBQoSAtmPvcCbqAfQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcCbqAfQueueSize.setStatus(_A)
_HpnicfCBQoSAtmPvcCbqBeQueueSize_Type=Integer32
_HpnicfCBQoSAtmPvcCbqBeQueueSize_Object=MibTableColumn
hpnicfCBQoSAtmPvcCbqBeQueueSize=_HpnicfCBQoSAtmPvcCbqBeQueueSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,1,1,5),_HpnicfCBQoSAtmPvcCbqBeQueueSize_Type())
hpnicfCBQoSAtmPvcCbqBeQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcCbqBeQueueSize.setStatus(_A)
_HpnicfCBQoSAtmPvcCbqBeActiveQueueNum_Type=Integer32
_HpnicfCBQoSAtmPvcCbqBeActiveQueueNum_Object=MibTableColumn
hpnicfCBQoSAtmPvcCbqBeActiveQueueNum=_HpnicfCBQoSAtmPvcCbqBeActiveQueueNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,1,1,6),_HpnicfCBQoSAtmPvcCbqBeActiveQueueNum_Type())
hpnicfCBQoSAtmPvcCbqBeActiveQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcCbqBeActiveQueueNum.setStatus(_A)
_HpnicfCBQoSAtmPvcCbqBeMaxActiveQueueNum_Type=Integer32
_HpnicfCBQoSAtmPvcCbqBeMaxActiveQueueNum_Object=MibTableColumn
hpnicfCBQoSAtmPvcCbqBeMaxActiveQueueNum=_HpnicfCBQoSAtmPvcCbqBeMaxActiveQueueNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,1,1,7),_HpnicfCBQoSAtmPvcCbqBeMaxActiveQueueNum_Type())
hpnicfCBQoSAtmPvcCbqBeMaxActiveQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcCbqBeMaxActiveQueueNum.setStatus(_A)
_HpnicfCBQoSAtmPvcCbqBeTotalQueueNum_Type=Integer32
_HpnicfCBQoSAtmPvcCbqBeTotalQueueNum_Object=MibTableColumn
hpnicfCBQoSAtmPvcCbqBeTotalQueueNum=_HpnicfCBQoSAtmPvcCbqBeTotalQueueNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,1,1,8),_HpnicfCBQoSAtmPvcCbqBeTotalQueueNum_Type())
hpnicfCBQoSAtmPvcCbqBeTotalQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcCbqBeTotalQueueNum.setStatus(_A)
_HpnicfCBQoSAtmPvcCbqAfAllocatedQueueNum_Type=Integer32
_HpnicfCBQoSAtmPvcCbqAfAllocatedQueueNum_Object=MibTableColumn
hpnicfCBQoSAtmPvcCbqAfAllocatedQueueNum=_HpnicfCBQoSAtmPvcCbqAfAllocatedQueueNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,1,1,9),_HpnicfCBQoSAtmPvcCbqAfAllocatedQueueNum_Type())
hpnicfCBQoSAtmPvcCbqAfAllocatedQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcCbqAfAllocatedQueueNum.setStatus(_A)
_HpnicfCBQoSAtmPvcClassMatchRunInfoTable_Object=MibTable
hpnicfCBQoSAtmPvcClassMatchRunInfoTable=_HpnicfCBQoSAtmPvcClassMatchRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,2))
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcClassMatchRunInfoTable.setStatus(_A)
_HpnicfCBQoSAtmPvcClassMatchRunInfoEntry_Object=MibTableRow
hpnicfCBQoSAtmPvcClassMatchRunInfoEntry=_HpnicfCBQoSAtmPvcClassMatchRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,2,1))
hpnicfCBQoSAtmPvcClassMatchRunInfoEntry.setIndexNames((0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_R),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcClassMatchRunInfoEntry.setStatus(_A)
_HpnicfCBQoSAtmPvcClassMatchPackets_Type=Counter64
_HpnicfCBQoSAtmPvcClassMatchPackets_Object=MibTableColumn
hpnicfCBQoSAtmPvcClassMatchPackets=_HpnicfCBQoSAtmPvcClassMatchPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,2,1,1),_HpnicfCBQoSAtmPvcClassMatchPackets_Type())
hpnicfCBQoSAtmPvcClassMatchPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcClassMatchPackets.setStatus(_A)
_HpnicfCBQoSAtmPvcClassMatchBytes_Type=Counter64
_HpnicfCBQoSAtmPvcClassMatchBytes_Object=MibTableColumn
hpnicfCBQoSAtmPvcClassMatchBytes=_HpnicfCBQoSAtmPvcClassMatchBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,2,1,2),_HpnicfCBQoSAtmPvcClassMatchBytes_Type())
hpnicfCBQoSAtmPvcClassMatchBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcClassMatchBytes.setStatus(_A)
_HpnicfCBQoSAtmPvcClassAverageRate_Type=Integer32
_HpnicfCBQoSAtmPvcClassAverageRate_Object=MibTableColumn
hpnicfCBQoSAtmPvcClassAverageRate=_HpnicfCBQoSAtmPvcClassAverageRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,2,1,3),_HpnicfCBQoSAtmPvcClassAverageRate_Type())
hpnicfCBQoSAtmPvcClassAverageRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcClassAverageRate.setStatus(_A)
_HpnicfCBQoSAtmPvcCarRunInfoTable_Object=MibTable
hpnicfCBQoSAtmPvcCarRunInfoTable=_HpnicfCBQoSAtmPvcCarRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,3))
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcCarRunInfoTable.setStatus(_A)
_HpnicfCBQoSAtmPvcCarRunInfoEntry_Object=MibTableRow
hpnicfCBQoSAtmPvcCarRunInfoEntry=_HpnicfCBQoSAtmPvcCarRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,3,1))
hpnicfCBQoSAtmPvcCarRunInfoEntry.setIndexNames((0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_R),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcCarRunInfoEntry.setStatus(_A)
_HpnicfCBQoSAtmPvcCarConformPackets_Type=Counter64
_HpnicfCBQoSAtmPvcCarConformPackets_Object=MibTableColumn
hpnicfCBQoSAtmPvcCarConformPackets=_HpnicfCBQoSAtmPvcCarConformPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,3,1,1),_HpnicfCBQoSAtmPvcCarConformPackets_Type())
hpnicfCBQoSAtmPvcCarConformPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcCarConformPackets.setStatus(_A)
_HpnicfCBQoSAtmPvcCarConformBytes_Type=Counter64
_HpnicfCBQoSAtmPvcCarConformBytes_Object=MibTableColumn
hpnicfCBQoSAtmPvcCarConformBytes=_HpnicfCBQoSAtmPvcCarConformBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,3,1,2),_HpnicfCBQoSAtmPvcCarConformBytes_Type())
hpnicfCBQoSAtmPvcCarConformBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcCarConformBytes.setStatus(_A)
_HpnicfCBQoSAtmPvcCarExceedPackets_Type=Counter64
_HpnicfCBQoSAtmPvcCarExceedPackets_Object=MibTableColumn
hpnicfCBQoSAtmPvcCarExceedPackets=_HpnicfCBQoSAtmPvcCarExceedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,3,1,3),_HpnicfCBQoSAtmPvcCarExceedPackets_Type())
hpnicfCBQoSAtmPvcCarExceedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcCarExceedPackets.setStatus(_A)
_HpnicfCBQoSAtmPvcCarExceedBytes_Type=Counter64
_HpnicfCBQoSAtmPvcCarExceedBytes_Object=MibTableColumn
hpnicfCBQoSAtmPvcCarExceedBytes=_HpnicfCBQoSAtmPvcCarExceedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,3,1,4),_HpnicfCBQoSAtmPvcCarExceedBytes_Type())
hpnicfCBQoSAtmPvcCarExceedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcCarExceedBytes.setStatus(_A)
_HpnicfCBQoSAtmPvcGtsRunInfoTable_Object=MibTable
hpnicfCBQoSAtmPvcGtsRunInfoTable=_HpnicfCBQoSAtmPvcGtsRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,4))
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcGtsRunInfoTable.setStatus(_A)
_HpnicfCBQoSAtmPvcGtsRunInfoEntry_Object=MibTableRow
hpnicfCBQoSAtmPvcGtsRunInfoEntry=_HpnicfCBQoSAtmPvcGtsRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,4,1))
hpnicfCBQoSAtmPvcGtsRunInfoEntry.setIndexNames((0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_R),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcGtsRunInfoEntry.setStatus(_A)
_HpnicfCBQoSAtmPvcGtsPassedPackets_Type=Counter64
_HpnicfCBQoSAtmPvcGtsPassedPackets_Object=MibTableColumn
hpnicfCBQoSAtmPvcGtsPassedPackets=_HpnicfCBQoSAtmPvcGtsPassedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,4,1,1),_HpnicfCBQoSAtmPvcGtsPassedPackets_Type())
hpnicfCBQoSAtmPvcGtsPassedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcGtsPassedPackets.setStatus(_A)
_HpnicfCBQoSAtmPvcGtsPassedBytes_Type=Counter64
_HpnicfCBQoSAtmPvcGtsPassedBytes_Object=MibTableColumn
hpnicfCBQoSAtmPvcGtsPassedBytes=_HpnicfCBQoSAtmPvcGtsPassedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,4,1,2),_HpnicfCBQoSAtmPvcGtsPassedBytes_Type())
hpnicfCBQoSAtmPvcGtsPassedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcGtsPassedBytes.setStatus(_A)
_HpnicfCBQoSAtmPvcGtsDiscardedPackets_Type=Counter64
_HpnicfCBQoSAtmPvcGtsDiscardedPackets_Object=MibTableColumn
hpnicfCBQoSAtmPvcGtsDiscardedPackets=_HpnicfCBQoSAtmPvcGtsDiscardedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,4,1,3),_HpnicfCBQoSAtmPvcGtsDiscardedPackets_Type())
hpnicfCBQoSAtmPvcGtsDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcGtsDiscardedPackets.setStatus(_A)
_HpnicfCBQoSAtmPvcGtsDiscardedBytes_Type=Counter64
_HpnicfCBQoSAtmPvcGtsDiscardedBytes_Object=MibTableColumn
hpnicfCBQoSAtmPvcGtsDiscardedBytes=_HpnicfCBQoSAtmPvcGtsDiscardedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,4,1,4),_HpnicfCBQoSAtmPvcGtsDiscardedBytes_Type())
hpnicfCBQoSAtmPvcGtsDiscardedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcGtsDiscardedBytes.setStatus(_A)
_HpnicfCBQoSAtmPvcGtsDelayedPackets_Type=Counter64
_HpnicfCBQoSAtmPvcGtsDelayedPackets_Object=MibTableColumn
hpnicfCBQoSAtmPvcGtsDelayedPackets=_HpnicfCBQoSAtmPvcGtsDelayedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,4,1,5),_HpnicfCBQoSAtmPvcGtsDelayedPackets_Type())
hpnicfCBQoSAtmPvcGtsDelayedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcGtsDelayedPackets.setStatus(_A)
_HpnicfCBQoSAtmPvcGtsDelayedBytes_Type=Counter64
_HpnicfCBQoSAtmPvcGtsDelayedBytes_Object=MibTableColumn
hpnicfCBQoSAtmPvcGtsDelayedBytes=_HpnicfCBQoSAtmPvcGtsDelayedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,4,1,6),_HpnicfCBQoSAtmPvcGtsDelayedBytes_Type())
hpnicfCBQoSAtmPvcGtsDelayedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcGtsDelayedBytes.setStatus(_A)
_HpnicfCBQoSAtmPvcGtsQueueSize_Type=Integer32
_HpnicfCBQoSAtmPvcGtsQueueSize_Object=MibTableColumn
hpnicfCBQoSAtmPvcGtsQueueSize=_HpnicfCBQoSAtmPvcGtsQueueSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,4,1,7),_HpnicfCBQoSAtmPvcGtsQueueSize_Type())
hpnicfCBQoSAtmPvcGtsQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcGtsQueueSize.setStatus(_A)
_HpnicfCBQoSAtmPvcRemarkRunInfoTable_Object=MibTable
hpnicfCBQoSAtmPvcRemarkRunInfoTable=_HpnicfCBQoSAtmPvcRemarkRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,5))
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcRemarkRunInfoTable.setStatus(_A)
_HpnicfCBQoSAtmPvcRemarkRunInfoEntry_Object=MibTableRow
hpnicfCBQoSAtmPvcRemarkRunInfoEntry=_HpnicfCBQoSAtmPvcRemarkRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,5,1))
hpnicfCBQoSAtmPvcRemarkRunInfoEntry.setIndexNames((0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_R),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcRemarkRunInfoEntry.setStatus(_A)
_HpnicfCBQoSAtmPvcRemarkedPackets_Type=Counter64
_HpnicfCBQoSAtmPvcRemarkedPackets_Object=MibTableColumn
hpnicfCBQoSAtmPvcRemarkedPackets=_HpnicfCBQoSAtmPvcRemarkedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,5,1,1),_HpnicfCBQoSAtmPvcRemarkedPackets_Type())
hpnicfCBQoSAtmPvcRemarkedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcRemarkedPackets.setStatus(_A)
_HpnicfCBQoSAtmPvcQueueRunInfoTable_Object=MibTable
hpnicfCBQoSAtmPvcQueueRunInfoTable=_HpnicfCBQoSAtmPvcQueueRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,6))
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcQueueRunInfoTable.setStatus(_A)
_HpnicfCBQoSAtmPvcQueueRunInfoEntry_Object=MibTableRow
hpnicfCBQoSAtmPvcQueueRunInfoEntry=_HpnicfCBQoSAtmPvcQueueRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,6,1))
hpnicfCBQoSAtmPvcQueueRunInfoEntry.setIndexNames((0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_R),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcQueueRunInfoEntry.setStatus(_A)
_HpnicfCBQoSAtmPvcQueueMatchedPackets_Type=Counter64
_HpnicfCBQoSAtmPvcQueueMatchedPackets_Object=MibTableColumn
hpnicfCBQoSAtmPvcQueueMatchedPackets=_HpnicfCBQoSAtmPvcQueueMatchedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,6,1,1),_HpnicfCBQoSAtmPvcQueueMatchedPackets_Type())
hpnicfCBQoSAtmPvcQueueMatchedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcQueueMatchedPackets.setStatus(_A)
_HpnicfCBQoSAtmPvcQueueMatchedBytes_Type=Counter64
_HpnicfCBQoSAtmPvcQueueMatchedBytes_Object=MibTableColumn
hpnicfCBQoSAtmPvcQueueMatchedBytes=_HpnicfCBQoSAtmPvcQueueMatchedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,6,1,2),_HpnicfCBQoSAtmPvcQueueMatchedBytes_Type())
hpnicfCBQoSAtmPvcQueueMatchedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcQueueMatchedBytes.setStatus(_A)
_HpnicfCBQoSAtmPvcQueueEnqueuedPackets_Type=Counter64
_HpnicfCBQoSAtmPvcQueueEnqueuedPackets_Object=MibTableColumn
hpnicfCBQoSAtmPvcQueueEnqueuedPackets=_HpnicfCBQoSAtmPvcQueueEnqueuedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,6,1,3),_HpnicfCBQoSAtmPvcQueueEnqueuedPackets_Type())
hpnicfCBQoSAtmPvcQueueEnqueuedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcQueueEnqueuedPackets.setStatus(_A)
_HpnicfCBQoSAtmPvcQueueEnqueuedBytes_Type=Counter64
_HpnicfCBQoSAtmPvcQueueEnqueuedBytes_Object=MibTableColumn
hpnicfCBQoSAtmPvcQueueEnqueuedBytes=_HpnicfCBQoSAtmPvcQueueEnqueuedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,6,1,4),_HpnicfCBQoSAtmPvcQueueEnqueuedBytes_Type())
hpnicfCBQoSAtmPvcQueueEnqueuedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcQueueEnqueuedBytes.setStatus(_A)
_HpnicfCBQoSAtmPvcQueueDiscardedPackets_Type=Counter64
_HpnicfCBQoSAtmPvcQueueDiscardedPackets_Object=MibTableColumn
hpnicfCBQoSAtmPvcQueueDiscardedPackets=_HpnicfCBQoSAtmPvcQueueDiscardedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,6,1,5),_HpnicfCBQoSAtmPvcQueueDiscardedPackets_Type())
hpnicfCBQoSAtmPvcQueueDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcQueueDiscardedPackets.setStatus(_A)
_HpnicfCBQoSAtmPvcQueueDiscardedBytes_Type=Counter64
_HpnicfCBQoSAtmPvcQueueDiscardedBytes_Object=MibTableColumn
hpnicfCBQoSAtmPvcQueueDiscardedBytes=_HpnicfCBQoSAtmPvcQueueDiscardedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,6,1,6),_HpnicfCBQoSAtmPvcQueueDiscardedBytes_Type())
hpnicfCBQoSAtmPvcQueueDiscardedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcQueueDiscardedBytes.setStatus(_A)
_HpnicfCBQoSAtmPvcWredRunInfoTable_Object=MibTable
hpnicfCBQoSAtmPvcWredRunInfoTable=_HpnicfCBQoSAtmPvcWredRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,7))
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcWredRunInfoTable.setStatus(_A)
_HpnicfCBQoSAtmPvcWredRunInfoEntry_Object=MibTableRow
hpnicfCBQoSAtmPvcWredRunInfoEntry=_HpnicfCBQoSAtmPvcWredRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,7,1))
hpnicfCBQoSAtmPvcWredRunInfoEntry.setIndexNames((0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_R),(0,_B,_G),(0,_B,_T))
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcWredRunInfoEntry.setStatus(_A)
_HpnicfCBQoSAtmPvcWredRandomDiscardedPackets_Type=Counter64
_HpnicfCBQoSAtmPvcWredRandomDiscardedPackets_Object=MibTableColumn
hpnicfCBQoSAtmPvcWredRandomDiscardedPackets=_HpnicfCBQoSAtmPvcWredRandomDiscardedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,7,1,1),_HpnicfCBQoSAtmPvcWredRandomDiscardedPackets_Type())
hpnicfCBQoSAtmPvcWredRandomDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcWredRandomDiscardedPackets.setStatus(_A)
_HpnicfCBQoSAtmPvcWredTailDiscardedPackets_Type=Counter64
_HpnicfCBQoSAtmPvcWredTailDiscardedPackets_Object=MibTableColumn
hpnicfCBQoSAtmPvcWredTailDiscardedPackets=_HpnicfCBQoSAtmPvcWredTailDiscardedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,7,1,2),_HpnicfCBQoSAtmPvcWredTailDiscardedPackets_Type())
hpnicfCBQoSAtmPvcWredTailDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcWredTailDiscardedPackets.setStatus(_A)
_HpnicfCBQoSAtmPvcAccountingRunInfoTable_Object=MibTable
hpnicfCBQoSAtmPvcAccountingRunInfoTable=_HpnicfCBQoSAtmPvcAccountingRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,8))
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcAccountingRunInfoTable.setStatus(_A)
_HpnicfCBQoSAtmPvcAccountingRunInfoEntry_Object=MibTableRow
hpnicfCBQoSAtmPvcAccountingRunInfoEntry=_HpnicfCBQoSAtmPvcAccountingRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,8,1))
hpnicfCBQoSAtmPvcAccountingRunInfoEntry.setIndexNames((0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_R),(0,_B,_G),(0,_B,_T))
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcAccountingRunInfoEntry.setStatus(_A)
_HpnicfCBQoSAtmPvcAccountingPackets_Type=Counter64
_HpnicfCBQoSAtmPvcAccountingPackets_Object=MibTableColumn
hpnicfCBQoSAtmPvcAccountingPackets=_HpnicfCBQoSAtmPvcAccountingPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,8,1,1),_HpnicfCBQoSAtmPvcAccountingPackets_Type())
hpnicfCBQoSAtmPvcAccountingPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcAccountingPackets.setStatus(_A)
_HpnicfCBQoSAtmPvcAccountingBytes_Type=Counter64
_HpnicfCBQoSAtmPvcAccountingBytes_Object=MibTableColumn
hpnicfCBQoSAtmPvcAccountingBytes=_HpnicfCBQoSAtmPvcAccountingBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,2,8,1,2),_HpnicfCBQoSAtmPvcAccountingBytes_Type())
hpnicfCBQoSAtmPvcAccountingBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAtmPvcAccountingBytes.setStatus(_A)
_HpnicfCBQoSFrPvcStaticsObjects_ObjectIdentity=ObjectIdentity
hpnicfCBQoSFrPvcStaticsObjects=_HpnicfCBQoSFrPvcStaticsObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3))
_HpnicfCBQoSFrPvcCbqRunInfoTable_Object=MibTable
hpnicfCBQoSFrPvcCbqRunInfoTable=_HpnicfCBQoSFrPvcCbqRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,1))
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcCbqRunInfoTable.setStatus(_A)
_HpnicfCBQoSFrPvcCbqRunInfoEntry_Object=MibTableRow
hpnicfCBQoSFrPvcCbqRunInfoEntry=_HpnicfCBQoSFrPvcCbqRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,1,1))
hpnicfCBQoSFrPvcCbqRunInfoEntry.setIndexNames((0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcCbqRunInfoEntry.setStatus(_A)
_HpnicfCBQoSFrPvcCbqQueueSize_Type=Integer32
_HpnicfCBQoSFrPvcCbqQueueSize_Object=MibTableColumn
hpnicfCBQoSFrPvcCbqQueueSize=_HpnicfCBQoSFrPvcCbqQueueSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,1,1,1),_HpnicfCBQoSFrPvcCbqQueueSize_Type())
hpnicfCBQoSFrPvcCbqQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcCbqQueueSize.setStatus(_A)
_HpnicfCBQoSFrPvcCbqDiscard_Type=Counter64
_HpnicfCBQoSFrPvcCbqDiscard_Object=MibTableColumn
hpnicfCBQoSFrPvcCbqDiscard=_HpnicfCBQoSFrPvcCbqDiscard_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,1,1,2),_HpnicfCBQoSFrPvcCbqDiscard_Type())
hpnicfCBQoSFrPvcCbqDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcCbqDiscard.setStatus(_A)
_HpnicfCBQoSFrPvcCbqEfQueueSize_Type=Integer32
_HpnicfCBQoSFrPvcCbqEfQueueSize_Object=MibTableColumn
hpnicfCBQoSFrPvcCbqEfQueueSize=_HpnicfCBQoSFrPvcCbqEfQueueSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,1,1,3),_HpnicfCBQoSFrPvcCbqEfQueueSize_Type())
hpnicfCBQoSFrPvcCbqEfQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcCbqEfQueueSize.setStatus(_A)
_HpnicfCBQoSFrPvcCbqAfQueueSize_Type=Integer32
_HpnicfCBQoSFrPvcCbqAfQueueSize_Object=MibTableColumn
hpnicfCBQoSFrPvcCbqAfQueueSize=_HpnicfCBQoSFrPvcCbqAfQueueSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,1,1,4),_HpnicfCBQoSFrPvcCbqAfQueueSize_Type())
hpnicfCBQoSFrPvcCbqAfQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcCbqAfQueueSize.setStatus(_A)
_HpnicfCBQoSFrPvcCbqBeQueueSize_Type=Integer32
_HpnicfCBQoSFrPvcCbqBeQueueSize_Object=MibTableColumn
hpnicfCBQoSFrPvcCbqBeQueueSize=_HpnicfCBQoSFrPvcCbqBeQueueSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,1,1,5),_HpnicfCBQoSFrPvcCbqBeQueueSize_Type())
hpnicfCBQoSFrPvcCbqBeQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcCbqBeQueueSize.setStatus(_A)
_HpnicfCBQoSFrPvcCbqBeActiveQueueNum_Type=Integer32
_HpnicfCBQoSFrPvcCbqBeActiveQueueNum_Object=MibTableColumn
hpnicfCBQoSFrPvcCbqBeActiveQueueNum=_HpnicfCBQoSFrPvcCbqBeActiveQueueNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,1,1,6),_HpnicfCBQoSFrPvcCbqBeActiveQueueNum_Type())
hpnicfCBQoSFrPvcCbqBeActiveQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcCbqBeActiveQueueNum.setStatus(_A)
_HpnicfCBQoSFrPvcCbqBeMaxActiveQueueNum_Type=Integer32
_HpnicfCBQoSFrPvcCbqBeMaxActiveQueueNum_Object=MibTableColumn
hpnicfCBQoSFrPvcCbqBeMaxActiveQueueNum=_HpnicfCBQoSFrPvcCbqBeMaxActiveQueueNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,1,1,7),_HpnicfCBQoSFrPvcCbqBeMaxActiveQueueNum_Type())
hpnicfCBQoSFrPvcCbqBeMaxActiveQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcCbqBeMaxActiveQueueNum.setStatus(_A)
_HpnicfCBQoSFrPvcCbqBeTotalQueueNum_Type=Integer32
_HpnicfCBQoSFrPvcCbqBeTotalQueueNum_Object=MibTableColumn
hpnicfCBQoSFrPvcCbqBeTotalQueueNum=_HpnicfCBQoSFrPvcCbqBeTotalQueueNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,1,1,8),_HpnicfCBQoSFrPvcCbqBeTotalQueueNum_Type())
hpnicfCBQoSFrPvcCbqBeTotalQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcCbqBeTotalQueueNum.setStatus(_A)
_HpnicfCBQoSFrPvcCbqAfAllocatedQueueNum_Type=Integer32
_HpnicfCBQoSFrPvcCbqAfAllocatedQueueNum_Object=MibTableColumn
hpnicfCBQoSFrPvcCbqAfAllocatedQueueNum=_HpnicfCBQoSFrPvcCbqAfAllocatedQueueNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,1,1,9),_HpnicfCBQoSFrPvcCbqAfAllocatedQueueNum_Type())
hpnicfCBQoSFrPvcCbqAfAllocatedQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcCbqAfAllocatedQueueNum.setStatus(_A)
_HpnicfCBQoSFrPvcClassMatchRunInfoTable_Object=MibTable
hpnicfCBQoSFrPvcClassMatchRunInfoTable=_HpnicfCBQoSFrPvcClassMatchRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,2))
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcClassMatchRunInfoTable.setStatus(_A)
_HpnicfCBQoSFrPvcClassMatchRunInfoEntry_Object=MibTableRow
hpnicfCBQoSFrPvcClassMatchRunInfoEntry=_HpnicfCBQoSFrPvcClassMatchRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,2,1))
hpnicfCBQoSFrPvcClassMatchRunInfoEntry.setIndexNames((0,_B,_P),(0,_B,_Q),(0,_B,_S),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcClassMatchRunInfoEntry.setStatus(_A)
_HpnicfCBQoSFrPvcClassMatchedPackets_Type=Counter64
_HpnicfCBQoSFrPvcClassMatchedPackets_Object=MibTableColumn
hpnicfCBQoSFrPvcClassMatchedPackets=_HpnicfCBQoSFrPvcClassMatchedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,2,1,1),_HpnicfCBQoSFrPvcClassMatchedPackets_Type())
hpnicfCBQoSFrPvcClassMatchedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcClassMatchedPackets.setStatus(_A)
_HpnicfCBQoSFrPvcClassMatchedBytes_Type=Counter64
_HpnicfCBQoSFrPvcClassMatchedBytes_Object=MibTableColumn
hpnicfCBQoSFrPvcClassMatchedBytes=_HpnicfCBQoSFrPvcClassMatchedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,2,1,2),_HpnicfCBQoSFrPvcClassMatchedBytes_Type())
hpnicfCBQoSFrPvcClassMatchedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcClassMatchedBytes.setStatus(_A)
_HpnicfCBQoSFrPvcClassAverageRate_Type=Counter64
_HpnicfCBQoSFrPvcClassAverageRate_Object=MibTableColumn
hpnicfCBQoSFrPvcClassAverageRate=_HpnicfCBQoSFrPvcClassAverageRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,2,1,3),_HpnicfCBQoSFrPvcClassAverageRate_Type())
hpnicfCBQoSFrPvcClassAverageRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcClassAverageRate.setStatus(_A)
_HpnicfCBQoSFrPvcCarRunInfoTable_Object=MibTable
hpnicfCBQoSFrPvcCarRunInfoTable=_HpnicfCBQoSFrPvcCarRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,3))
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcCarRunInfoTable.setStatus(_A)
_HpnicfCBQoSFrPvcCarRunInfoEntry_Object=MibTableRow
hpnicfCBQoSFrPvcCarRunInfoEntry=_HpnicfCBQoSFrPvcCarRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,3,1))
hpnicfCBQoSFrPvcCarRunInfoEntry.setIndexNames((0,_B,_P),(0,_B,_Q),(0,_B,_S),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcCarRunInfoEntry.setStatus(_A)
_HpnicfCBQoSFrPvcCarConformPackets_Type=Counter64
_HpnicfCBQoSFrPvcCarConformPackets_Object=MibTableColumn
hpnicfCBQoSFrPvcCarConformPackets=_HpnicfCBQoSFrPvcCarConformPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,3,1,1),_HpnicfCBQoSFrPvcCarConformPackets_Type())
hpnicfCBQoSFrPvcCarConformPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcCarConformPackets.setStatus(_A)
_HpnicfCBQoSFrPvcCarConformBytes_Type=Counter64
_HpnicfCBQoSFrPvcCarConformBytes_Object=MibTableColumn
hpnicfCBQoSFrPvcCarConformBytes=_HpnicfCBQoSFrPvcCarConformBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,3,1,2),_HpnicfCBQoSFrPvcCarConformBytes_Type())
hpnicfCBQoSFrPvcCarConformBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcCarConformBytes.setStatus(_A)
_HpnicfCBQoSFrPvcCarExceedPackets_Type=Counter64
_HpnicfCBQoSFrPvcCarExceedPackets_Object=MibTableColumn
hpnicfCBQoSFrPvcCarExceedPackets=_HpnicfCBQoSFrPvcCarExceedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,3,1,3),_HpnicfCBQoSFrPvcCarExceedPackets_Type())
hpnicfCBQoSFrPvcCarExceedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcCarExceedPackets.setStatus(_A)
_HpnicfCBQoSFrPvcCarExceedBytes_Type=Counter64
_HpnicfCBQoSFrPvcCarExceedBytes_Object=MibTableColumn
hpnicfCBQoSFrPvcCarExceedBytes=_HpnicfCBQoSFrPvcCarExceedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,3,1,4),_HpnicfCBQoSFrPvcCarExceedBytes_Type())
hpnicfCBQoSFrPvcCarExceedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcCarExceedBytes.setStatus(_A)
_HpnicfCBQoSFrPvcGtsRunInfoTable_Object=MibTable
hpnicfCBQoSFrPvcGtsRunInfoTable=_HpnicfCBQoSFrPvcGtsRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,4))
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcGtsRunInfoTable.setStatus(_A)
_HpnicfCBQoSFrPvcGtsRunInfoEntry_Object=MibTableRow
hpnicfCBQoSFrPvcGtsRunInfoEntry=_HpnicfCBQoSFrPvcGtsRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,4,1))
hpnicfCBQoSFrPvcGtsRunInfoEntry.setIndexNames((0,_B,_P),(0,_B,_Q),(0,_B,_S),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcGtsRunInfoEntry.setStatus(_A)
_HpnicfCBQoSFrPvcGtsPassedPackets_Type=Counter64
_HpnicfCBQoSFrPvcGtsPassedPackets_Object=MibTableColumn
hpnicfCBQoSFrPvcGtsPassedPackets=_HpnicfCBQoSFrPvcGtsPassedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,4,1,1),_HpnicfCBQoSFrPvcGtsPassedPackets_Type())
hpnicfCBQoSFrPvcGtsPassedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcGtsPassedPackets.setStatus(_A)
_HpnicfCBQoSFrPvcGtsPassedBytes_Type=Counter64
_HpnicfCBQoSFrPvcGtsPassedBytes_Object=MibTableColumn
hpnicfCBQoSFrPvcGtsPassedBytes=_HpnicfCBQoSFrPvcGtsPassedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,4,1,2),_HpnicfCBQoSFrPvcGtsPassedBytes_Type())
hpnicfCBQoSFrPvcGtsPassedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcGtsPassedBytes.setStatus(_A)
_HpnicfCBQoSFrPvcGtsDiscardedPackets_Type=Counter64
_HpnicfCBQoSFrPvcGtsDiscardedPackets_Object=MibTableColumn
hpnicfCBQoSFrPvcGtsDiscardedPackets=_HpnicfCBQoSFrPvcGtsDiscardedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,4,1,3),_HpnicfCBQoSFrPvcGtsDiscardedPackets_Type())
hpnicfCBQoSFrPvcGtsDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcGtsDiscardedPackets.setStatus(_A)
_HpnicfCBQoSFrPvcGtsDiscardedBytes_Type=Counter64
_HpnicfCBQoSFrPvcGtsDiscardedBytes_Object=MibTableColumn
hpnicfCBQoSFrPvcGtsDiscardedBytes=_HpnicfCBQoSFrPvcGtsDiscardedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,4,1,4),_HpnicfCBQoSFrPvcGtsDiscardedBytes_Type())
hpnicfCBQoSFrPvcGtsDiscardedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcGtsDiscardedBytes.setStatus(_A)
_HpnicfCBQoSFrPvcGtsDelayedPackets_Type=Counter64
_HpnicfCBQoSFrPvcGtsDelayedPackets_Object=MibTableColumn
hpnicfCBQoSFrPvcGtsDelayedPackets=_HpnicfCBQoSFrPvcGtsDelayedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,4,1,5),_HpnicfCBQoSFrPvcGtsDelayedPackets_Type())
hpnicfCBQoSFrPvcGtsDelayedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcGtsDelayedPackets.setStatus(_A)
_HpnicfCBQoSFrPvcGtsDelayedBytes_Type=Counter64
_HpnicfCBQoSFrPvcGtsDelayedBytes_Object=MibTableColumn
hpnicfCBQoSFrPvcGtsDelayedBytes=_HpnicfCBQoSFrPvcGtsDelayedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,4,1,6),_HpnicfCBQoSFrPvcGtsDelayedBytes_Type())
hpnicfCBQoSFrPvcGtsDelayedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcGtsDelayedBytes.setStatus(_A)
_HpnicfCBQoSFrPvcGtsQueueSize_Type=Integer32
_HpnicfCBQoSFrPvcGtsQueueSize_Object=MibTableColumn
hpnicfCBQoSFrPvcGtsQueueSize=_HpnicfCBQoSFrPvcGtsQueueSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,4,1,7),_HpnicfCBQoSFrPvcGtsQueueSize_Type())
hpnicfCBQoSFrPvcGtsQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcGtsQueueSize.setStatus(_A)
_HpnicfCBQoSFrPvcRemarkRunInfoTable_Object=MibTable
hpnicfCBQoSFrPvcRemarkRunInfoTable=_HpnicfCBQoSFrPvcRemarkRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,5))
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcRemarkRunInfoTable.setStatus(_A)
_HpnicfCBQoSFrPvcRemarkRunInfoEntry_Object=MibTableRow
hpnicfCBQoSFrPvcRemarkRunInfoEntry=_HpnicfCBQoSFrPvcRemarkRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,5,1))
hpnicfCBQoSFrPvcRemarkRunInfoEntry.setIndexNames((0,_B,_P),(0,_B,_Q),(0,_B,_S),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcRemarkRunInfoEntry.setStatus(_A)
_HpnicfCBQoSFrPvcRemarkedPackets_Type=Counter64
_HpnicfCBQoSFrPvcRemarkedPackets_Object=MibTableColumn
hpnicfCBQoSFrPvcRemarkedPackets=_HpnicfCBQoSFrPvcRemarkedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,5,1,1),_HpnicfCBQoSFrPvcRemarkedPackets_Type())
hpnicfCBQoSFrPvcRemarkedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcRemarkedPackets.setStatus(_A)
_HpnicfCBQoSFrPvcQueueRunInfoTable_Object=MibTable
hpnicfCBQoSFrPvcQueueRunInfoTable=_HpnicfCBQoSFrPvcQueueRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,6))
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcQueueRunInfoTable.setStatus(_A)
_HpnicfCBQoSFrPvcQueueRunInfoEntry_Object=MibTableRow
hpnicfCBQoSFrPvcQueueRunInfoEntry=_HpnicfCBQoSFrPvcQueueRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,6,1))
hpnicfCBQoSFrPvcQueueRunInfoEntry.setIndexNames((0,_B,_P),(0,_B,_Q),(0,_B,_S),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcQueueRunInfoEntry.setStatus(_A)
_HpnicfCBQoSFrPvcQueueMatchedPackets_Type=Counter64
_HpnicfCBQoSFrPvcQueueMatchedPackets_Object=MibTableColumn
hpnicfCBQoSFrPvcQueueMatchedPackets=_HpnicfCBQoSFrPvcQueueMatchedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,6,1,1),_HpnicfCBQoSFrPvcQueueMatchedPackets_Type())
hpnicfCBQoSFrPvcQueueMatchedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcQueueMatchedPackets.setStatus(_A)
_HpnicfCBQoSFrPvcQueueMatchedBytes_Type=Counter64
_HpnicfCBQoSFrPvcQueueMatchedBytes_Object=MibTableColumn
hpnicfCBQoSFrPvcQueueMatchedBytes=_HpnicfCBQoSFrPvcQueueMatchedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,6,1,2),_HpnicfCBQoSFrPvcQueueMatchedBytes_Type())
hpnicfCBQoSFrPvcQueueMatchedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcQueueMatchedBytes.setStatus(_A)
_HpnicfCBQoSFrPvcQueueEnqueuedPackets_Type=Counter64
_HpnicfCBQoSFrPvcQueueEnqueuedPackets_Object=MibTableColumn
hpnicfCBQoSFrPvcQueueEnqueuedPackets=_HpnicfCBQoSFrPvcQueueEnqueuedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,6,1,3),_HpnicfCBQoSFrPvcQueueEnqueuedPackets_Type())
hpnicfCBQoSFrPvcQueueEnqueuedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcQueueEnqueuedPackets.setStatus(_A)
_HpnicfCBQoSFrPvcQueueEnqueuedBytes_Type=Counter64
_HpnicfCBQoSFrPvcQueueEnqueuedBytes_Object=MibTableColumn
hpnicfCBQoSFrPvcQueueEnqueuedBytes=_HpnicfCBQoSFrPvcQueueEnqueuedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,6,1,4),_HpnicfCBQoSFrPvcQueueEnqueuedBytes_Type())
hpnicfCBQoSFrPvcQueueEnqueuedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcQueueEnqueuedBytes.setStatus(_A)
_HpnicfCBQoSFrPvcQueueDiscardedPackets_Type=Counter64
_HpnicfCBQoSFrPvcQueueDiscardedPackets_Object=MibTableColumn
hpnicfCBQoSFrPvcQueueDiscardedPackets=_HpnicfCBQoSFrPvcQueueDiscardedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,6,1,5),_HpnicfCBQoSFrPvcQueueDiscardedPackets_Type())
hpnicfCBQoSFrPvcQueueDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcQueueDiscardedPackets.setStatus(_A)
_HpnicfCBQoSFrPvcQueueDiscardedBytes_Type=Counter64
_HpnicfCBQoSFrPvcQueueDiscardedBytes_Object=MibTableColumn
hpnicfCBQoSFrPvcQueueDiscardedBytes=_HpnicfCBQoSFrPvcQueueDiscardedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,6,1,6),_HpnicfCBQoSFrPvcQueueDiscardedBytes_Type())
hpnicfCBQoSFrPvcQueueDiscardedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcQueueDiscardedBytes.setStatus(_A)
_HpnicfCBQoSFrPvcWredRunInfoTable_Object=MibTable
hpnicfCBQoSFrPvcWredRunInfoTable=_HpnicfCBQoSFrPvcWredRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,7))
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcWredRunInfoTable.setStatus(_A)
_HpnicfCBQoSFrPvcWredRunInfoEntry_Object=MibTableRow
hpnicfCBQoSFrPvcWredRunInfoEntry=_HpnicfCBQoSFrPvcWredRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,7,1))
hpnicfCBQoSFrPvcWredRunInfoEntry.setIndexNames((0,_B,_P),(0,_B,_Q),(0,_B,_S),(0,_B,_G),(0,_B,_T))
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcWredRunInfoEntry.setStatus(_A)
_HpnicfCBQoSFrPvcWredRandomDiscardedPackets_Type=Counter64
_HpnicfCBQoSFrPvcWredRandomDiscardedPackets_Object=MibTableColumn
hpnicfCBQoSFrPvcWredRandomDiscardedPackets=_HpnicfCBQoSFrPvcWredRandomDiscardedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,7,1,1),_HpnicfCBQoSFrPvcWredRandomDiscardedPackets_Type())
hpnicfCBQoSFrPvcWredRandomDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcWredRandomDiscardedPackets.setStatus(_A)
_HpnicfCBQoSFrPvcWredTailDiscardedPackets_Type=Counter64
_HpnicfCBQoSFrPvcWredTailDiscardedPackets_Object=MibTableColumn
hpnicfCBQoSFrPvcWredTailDiscardedPackets=_HpnicfCBQoSFrPvcWredTailDiscardedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,7,1,2),_HpnicfCBQoSFrPvcWredTailDiscardedPackets_Type())
hpnicfCBQoSFrPvcWredTailDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcWredTailDiscardedPackets.setStatus(_A)
_HpnicfCBQoSFrPvcAccountingRunInfoTable_Object=MibTable
hpnicfCBQoSFrPvcAccountingRunInfoTable=_HpnicfCBQoSFrPvcAccountingRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,8))
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcAccountingRunInfoTable.setStatus(_A)
_HpnicfCBQoSFrPvcAccountingRunInfoEntry_Object=MibTableRow
hpnicfCBQoSFrPvcAccountingRunInfoEntry=_HpnicfCBQoSFrPvcAccountingRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,8,1))
hpnicfCBQoSFrPvcAccountingRunInfoEntry.setIndexNames((0,_B,_P),(0,_B,_Q),(0,_B,_S),(0,_B,_G),(0,_B,_T))
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcAccountingRunInfoEntry.setStatus(_A)
_HpnicfCBQoSFrPvcAccountingPackets_Type=Counter64
_HpnicfCBQoSFrPvcAccountingPackets_Object=MibTableColumn
hpnicfCBQoSFrPvcAccountingPackets=_HpnicfCBQoSFrPvcAccountingPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,8,1,1),_HpnicfCBQoSFrPvcAccountingPackets_Type())
hpnicfCBQoSFrPvcAccountingPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcAccountingPackets.setStatus(_A)
_HpnicfCBQoSFrPvcAccountingBytes_Type=Counter64
_HpnicfCBQoSFrPvcAccountingBytes_Object=MibTableColumn
hpnicfCBQoSFrPvcAccountingBytes=_HpnicfCBQoSFrPvcAccountingBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,3,8,1,2),_HpnicfCBQoSFrPvcAccountingBytes_Type())
hpnicfCBQoSFrPvcAccountingBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSFrPvcAccountingBytes.setStatus(_A)
_HpnicfCBQoSVlanStaticsObjects_ObjectIdentity=ObjectIdentity
hpnicfCBQoSVlanStaticsObjects=_HpnicfCBQoSVlanStaticsObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,4))
_HpnicfCBQoSVlanClassMatchRunInfoTable_Object=MibTable
hpnicfCBQoSVlanClassMatchRunInfoTable=_HpnicfCBQoSVlanClassMatchRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,4,1))
if mibBuilder.loadTexts:hpnicfCBQoSVlanClassMatchRunInfoTable.setStatus(_A)
_HpnicfCBQoSVlanClassMatchRunInfoEntry_Object=MibTableRow
hpnicfCBQoSVlanClassMatchRunInfoEntry=_HpnicfCBQoSVlanClassMatchRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,4,1,1))
hpnicfCBQoSVlanClassMatchRunInfoEntry.setIndexNames((0,_B,_X),(0,_B,_Y),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfCBQoSVlanClassMatchRunInfoEntry.setStatus(_A)
_HpnicfCBQoSVlanClassMatchedPackets_Type=Counter64
_HpnicfCBQoSVlanClassMatchedPackets_Object=MibTableColumn
hpnicfCBQoSVlanClassMatchedPackets=_HpnicfCBQoSVlanClassMatchedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,4,1,1,1),_HpnicfCBQoSVlanClassMatchedPackets_Type())
hpnicfCBQoSVlanClassMatchedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSVlanClassMatchedPackets.setStatus(_A)
_HpnicfCBQoSVlanAccountingRunInfoTable_Object=MibTable
hpnicfCBQoSVlanAccountingRunInfoTable=_HpnicfCBQoSVlanAccountingRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,4,2))
if mibBuilder.loadTexts:hpnicfCBQoSVlanAccountingRunInfoTable.setStatus(_A)
_HpnicfCBQoSVlanAccountingRunInfoEntry_Object=MibTableRow
hpnicfCBQoSVlanAccountingRunInfoEntry=_HpnicfCBQoSVlanAccountingRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,4,2,1))
hpnicfCBQoSVlanAccountingRunInfoEntry.setIndexNames((0,_B,_X),(0,_B,_Y),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfCBQoSVlanAccountingRunInfoEntry.setStatus(_A)
_HpnicfCBQoSVlanAccountingPackets_Type=Counter64
_HpnicfCBQoSVlanAccountingPackets_Object=MibTableColumn
hpnicfCBQoSVlanAccountingPackets=_HpnicfCBQoSVlanAccountingPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,4,2,1,1),_HpnicfCBQoSVlanAccountingPackets_Type())
hpnicfCBQoSVlanAccountingPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSVlanAccountingPackets.setStatus(_A)
_HpnicfCBQoSVlanAccountingBytes_Type=Counter64
_HpnicfCBQoSVlanAccountingBytes_Object=MibTableColumn
hpnicfCBQoSVlanAccountingBytes=_HpnicfCBQoSVlanAccountingBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,4,2,1,2),_HpnicfCBQoSVlanAccountingBytes_Type())
hpnicfCBQoSVlanAccountingBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSVlanAccountingBytes.setStatus(_A)
_HpnicfCBQoSApplyPolicyIndexObjects_ObjectIdentity=ObjectIdentity
hpnicfCBQoSApplyPolicyIndexObjects=_HpnicfCBQoSApplyPolicyIndexObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5))
_HpnicfCBQoSApplyObjectTable_Object=MibTable
hpnicfCBQoSApplyObjectTable=_HpnicfCBQoSApplyObjectTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,1))
if mibBuilder.loadTexts:hpnicfCBQoSApplyObjectTable.setStatus(_A)
_HpnicfCBQoSApplyObjectEntry_Object=MibTableRow
hpnicfCBQoSApplyObjectEntry=_HpnicfCBQoSApplyObjectEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,1,1))
hpnicfCBQoSApplyObjectEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:hpnicfCBQoSApplyObjectEntry.setStatus(_A)
_HpnicfCBQoSApplyObjectIndex_Type=Unsigned32
_HpnicfCBQoSApplyObjectIndex_Object=MibTableColumn
hpnicfCBQoSApplyObjectIndex=_HpnicfCBQoSApplyObjectIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,1,1,1),_HpnicfCBQoSApplyObjectIndex_Type())
hpnicfCBQoSApplyObjectIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSApplyObjectIndex.setStatus(_A)
_HpnicfCBQoSApplyObjectType_Type=ApplyObjectType
_HpnicfCBQoSApplyObjectType_Object=MibTableColumn
hpnicfCBQoSApplyObjectType=_HpnicfCBQoSApplyObjectType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,1,1,2),_HpnicfCBQoSApplyObjectType_Type())
hpnicfCBQoSApplyObjectType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSApplyObjectType.setStatus(_A)
_HpnicfCBQoSApplyObjectDirection_Type=DirectionType
_HpnicfCBQoSApplyObjectDirection_Object=MibTableColumn
hpnicfCBQoSApplyObjectDirection=_HpnicfCBQoSApplyObjectDirection_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,1,1,3),_HpnicfCBQoSApplyObjectDirection_Type())
hpnicfCBQoSApplyObjectDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSApplyObjectDirection.setStatus(_A)
_HpnicfCBQoSApplyObjectMainSite_Type=Unsigned32
_HpnicfCBQoSApplyObjectMainSite_Object=MibTableColumn
hpnicfCBQoSApplyObjectMainSite=_HpnicfCBQoSApplyObjectMainSite_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,1,1,4),_HpnicfCBQoSApplyObjectMainSite_Type())
hpnicfCBQoSApplyObjectMainSite.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSApplyObjectMainSite.setStatus(_A)
_HpnicfCBQoSApplyObjectSubChannel_Type=Unsigned32
_HpnicfCBQoSApplyObjectSubChannel_Object=MibTableColumn
hpnicfCBQoSApplyObjectSubChannel=_HpnicfCBQoSApplyObjectSubChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,1,1,5),_HpnicfCBQoSApplyObjectSubChannel_Type())
hpnicfCBQoSApplyObjectSubChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSApplyObjectSubChannel.setStatus(_A)
_HpnicfCBQoSApplyObjectSubClass_Type=Unsigned32
_HpnicfCBQoSApplyObjectSubClass_Object=MibTableColumn
hpnicfCBQoSApplyObjectSubClass=_HpnicfCBQoSApplyObjectSubClass_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,1,1,6),_HpnicfCBQoSApplyObjectSubClass_Type())
hpnicfCBQoSApplyObjectSubClass.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSApplyObjectSubClass.setStatus(_A)
_HpnicfCBQoSApplyObjectSubClassSec_Type=Unsigned32
_HpnicfCBQoSApplyObjectSubClassSec_Object=MibTableColumn
hpnicfCBQoSApplyObjectSubClassSec=_HpnicfCBQoSApplyObjectSubClassSec_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,1,1,7),_HpnicfCBQoSApplyObjectSubClassSec_Type())
hpnicfCBQoSApplyObjectSubClassSec.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSApplyObjectSubClassSec.setStatus(_A)
_HpnicfCBQoSIntApplyObjectTable_Object=MibTable
hpnicfCBQoSIntApplyObjectTable=_HpnicfCBQoSIntApplyObjectTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,2))
if mibBuilder.loadTexts:hpnicfCBQoSIntApplyObjectTable.setStatus(_A)
_HpnicfCBQoSIntApplyObjectEntry_Object=MibTableRow
hpnicfCBQoSIntApplyObjectEntry=_HpnicfCBQoSIntApplyObjectEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,2,1))
hpnicfCBQoSIntApplyObjectEntry.setIndexNames((0,_B,_A8),(0,_B,_Z))
if mibBuilder.loadTexts:hpnicfCBQoSIntApplyObjectEntry.setStatus(_A)
_HpnicfCBQoSIntApplyObjectIfIndex_Type=Unsigned32
_HpnicfCBQoSIntApplyObjectIfIndex_Object=MibTableColumn
hpnicfCBQoSIntApplyObjectIfIndex=_HpnicfCBQoSIntApplyObjectIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,2,1,1),_HpnicfCBQoSIntApplyObjectIfIndex_Type())
hpnicfCBQoSIntApplyObjectIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSIntApplyObjectIfIndex.setStatus(_A)
_HpnicfCBQoSIntApplyObjectIndex_Type=Unsigned32
_HpnicfCBQoSIntApplyObjectIndex_Object=MibTableColumn
hpnicfCBQoSIntApplyObjectIndex=_HpnicfCBQoSIntApplyObjectIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,2,1,2),_HpnicfCBQoSIntApplyObjectIndex_Type())
hpnicfCBQoSIntApplyObjectIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSIntApplyObjectIndex.setStatus(_A)
_HpnicfCBQoSVlanApplyObjectTable_Object=MibTable
hpnicfCBQoSVlanApplyObjectTable=_HpnicfCBQoSVlanApplyObjectTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,3))
if mibBuilder.loadTexts:hpnicfCBQoSVlanApplyObjectTable.setStatus(_A)
_HpnicfCBQoSVlanApplyObjectEntry_Object=MibTableRow
hpnicfCBQoSVlanApplyObjectEntry=_HpnicfCBQoSVlanApplyObjectEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,3,1))
hpnicfCBQoSVlanApplyObjectEntry.setIndexNames((0,_B,_A9),(0,_B,_Z))
if mibBuilder.loadTexts:hpnicfCBQoSVlanApplyObjectEntry.setStatus(_A)
class _HpnicfCBQoSVlanApplyObjectVlanID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpnicfCBQoSVlanApplyObjectVlanID_Type.__name__=_h
_HpnicfCBQoSVlanApplyObjectVlanID_Object=MibTableColumn
hpnicfCBQoSVlanApplyObjectVlanID=_HpnicfCBQoSVlanApplyObjectVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,3,1,1),_HpnicfCBQoSVlanApplyObjectVlanID_Type())
hpnicfCBQoSVlanApplyObjectVlanID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSVlanApplyObjectVlanID.setStatus(_A)
_HpnicfCBQoSVlanApplyObjectIndex_Type=Unsigned32
_HpnicfCBQoSVlanApplyObjectIndex_Object=MibTableColumn
hpnicfCBQoSVlanApplyObjectIndex=_HpnicfCBQoSVlanApplyObjectIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,3,1,2),_HpnicfCBQoSVlanApplyObjectIndex_Type())
hpnicfCBQoSVlanApplyObjectIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSVlanApplyObjectIndex.setStatus(_A)
_HpnicfCBQoSPvcApplyObjectTable_Object=MibTable
hpnicfCBQoSPvcApplyObjectTable=_HpnicfCBQoSPvcApplyObjectTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,4))
if mibBuilder.loadTexts:hpnicfCBQoSPvcApplyObjectTable.setStatus(_A)
_HpnicfCBQoSPvcApplyObjectEntry_Object=MibTableRow
hpnicfCBQoSPvcApplyObjectEntry=_HpnicfCBQoSPvcApplyObjectEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,4,1))
hpnicfCBQoSPvcApplyObjectEntry.setIndexNames((0,_B,_AA),(0,_B,_AB),(0,_B,_Z))
if mibBuilder.loadTexts:hpnicfCBQoSPvcApplyObjectEntry.setStatus(_A)
_HpnicfCBQoSPvcApplyObjectIfIndex_Type=Unsigned32
_HpnicfCBQoSPvcApplyObjectIfIndex_Object=MibTableColumn
hpnicfCBQoSPvcApplyObjectIfIndex=_HpnicfCBQoSPvcApplyObjectIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,4,1,1),_HpnicfCBQoSPvcApplyObjectIfIndex_Type())
hpnicfCBQoSPvcApplyObjectIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSPvcApplyObjectIfIndex.setStatus(_A)
_HpnicfCBQoSPvcApplyObjectPvcID_Type=Unsigned32
_HpnicfCBQoSPvcApplyObjectPvcID_Object=MibTableColumn
hpnicfCBQoSPvcApplyObjectPvcID=_HpnicfCBQoSPvcApplyObjectPvcID_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,4,1,2),_HpnicfCBQoSPvcApplyObjectPvcID_Type())
hpnicfCBQoSPvcApplyObjectPvcID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSPvcApplyObjectPvcID.setStatus(_A)
_HpnicfCBQoSPvcApplyObjectIndex_Type=Unsigned32
_HpnicfCBQoSPvcApplyObjectIndex_Object=MibTableColumn
hpnicfCBQoSPvcApplyObjectIndex=_HpnicfCBQoSPvcApplyObjectIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,4,1,3),_HpnicfCBQoSPvcApplyObjectIndex_Type())
hpnicfCBQoSPvcApplyObjectIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSPvcApplyObjectIndex.setStatus(_A)
_HpnicfCBQoSNestPolicyApplyObjectTable_Object=MibTable
hpnicfCBQoSNestPolicyApplyObjectTable=_HpnicfCBQoSNestPolicyApplyObjectTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,5))
if mibBuilder.loadTexts:hpnicfCBQoSNestPolicyApplyObjectTable.setStatus(_A)
_HpnicfCBQoSNestPolicyApplyObjectEntry_Object=MibTableRow
hpnicfCBQoSNestPolicyApplyObjectEntry=_HpnicfCBQoSNestPolicyApplyObjectEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,5,1))
hpnicfCBQoSNestPolicyApplyObjectEntry.setIndexNames((0,_B,_K),(0,_B,_AC))
if mibBuilder.loadTexts:hpnicfCBQoSNestPolicyApplyObjectEntry.setStatus(_A)
_HpnicfCBQoSNestPolicyClassIndex_Type=Unsigned32
_HpnicfCBQoSNestPolicyClassIndex_Object=MibTableColumn
hpnicfCBQoSNestPolicyClassIndex=_HpnicfCBQoSNestPolicyClassIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,5,1,1),_HpnicfCBQoSNestPolicyClassIndex_Type())
hpnicfCBQoSNestPolicyClassIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSNestPolicyClassIndex.setStatus(_A)
_HpnicfCBQoSNestPolicyApplyObjectIndex_Type=Unsigned32
_HpnicfCBQoSNestPolicyApplyObjectIndex_Object=MibTableColumn
hpnicfCBQoSNestPolicyApplyObjectIndex=_HpnicfCBQoSNestPolicyApplyObjectIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,5,1,2),_HpnicfCBQoSNestPolicyApplyObjectIndex_Type())
hpnicfCBQoSNestPolicyApplyObjectIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSNestPolicyApplyObjectIndex.setStatus(_A)
_HpnicfCBQoSCpApplyObjectTable_Object=MibTable
hpnicfCBQoSCpApplyObjectTable=_HpnicfCBQoSCpApplyObjectTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,6))
if mibBuilder.loadTexts:hpnicfCBQoSCpApplyObjectTable.setStatus(_A)
_HpnicfCBQoSCpApplyObjectEntry_Object=MibTableRow
hpnicfCBQoSCpApplyObjectEntry=_HpnicfCBQoSCpApplyObjectEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,6,1))
hpnicfCBQoSCpApplyObjectEntry.setIndexNames((0,_B,_AD),(0,_B,_AE),(0,_B,_Z))
if mibBuilder.loadTexts:hpnicfCBQoSCpApplyObjectEntry.setStatus(_A)
_HpnicfCBQoSCpApplyObjectChassis_Type=Unsigned32
_HpnicfCBQoSCpApplyObjectChassis_Object=MibTableColumn
hpnicfCBQoSCpApplyObjectChassis=_HpnicfCBQoSCpApplyObjectChassis_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,6,1,1),_HpnicfCBQoSCpApplyObjectChassis_Type())
hpnicfCBQoSCpApplyObjectChassis.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSCpApplyObjectChassis.setStatus(_A)
_HpnicfCBQoSCpApplyObjectSlot_Type=Unsigned32
_HpnicfCBQoSCpApplyObjectSlot_Object=MibTableColumn
hpnicfCBQoSCpApplyObjectSlot=_HpnicfCBQoSCpApplyObjectSlot_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,6,1,2),_HpnicfCBQoSCpApplyObjectSlot_Type())
hpnicfCBQoSCpApplyObjectSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCBQoSCpApplyObjectSlot.setStatus(_A)
_HpnicfCBQoSCpApplyObjectIndex_Type=Unsigned32
_HpnicfCBQoSCpApplyObjectIndex_Object=MibTableColumn
hpnicfCBQoSCpApplyObjectIndex=_HpnicfCBQoSCpApplyObjectIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,5,6,1,3),_HpnicfCBQoSCpApplyObjectIndex_Type())
hpnicfCBQoSCpApplyObjectIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSCpApplyObjectIndex.setStatus(_A)
_HpnicfCBQoSStaticsObjects_ObjectIdentity=ObjectIdentity
hpnicfCBQoSStaticsObjects=_HpnicfCBQoSStaticsObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6))
_HpnicfCBQoSCbqRunInfoTable_Object=MibTable
hpnicfCBQoSCbqRunInfoTable=_HpnicfCBQoSCbqRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,1))
if mibBuilder.loadTexts:hpnicfCBQoSCbqRunInfoTable.setStatus(_A)
_HpnicfCBQoSCbqRunInfoEntry_Object=MibTableRow
hpnicfCBQoSCbqRunInfoEntry=_HpnicfCBQoSCbqRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,1,1))
hpnicfCBQoSCbqRunInfoEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:hpnicfCBQoSCbqRunInfoEntry.setStatus(_A)
_HpnicfCBQoSCbqQueueSize_Type=Integer32
_HpnicfCBQoSCbqQueueSize_Object=MibTableColumn
hpnicfCBQoSCbqQueueSize=_HpnicfCBQoSCbqQueueSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,1,1,1),_HpnicfCBQoSCbqQueueSize_Type())
hpnicfCBQoSCbqQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSCbqQueueSize.setStatus(_A)
_HpnicfCBQoSCbqDiscard_Type=Counter64
_HpnicfCBQoSCbqDiscard_Object=MibTableColumn
hpnicfCBQoSCbqDiscard=_HpnicfCBQoSCbqDiscard_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,1,1,2),_HpnicfCBQoSCbqDiscard_Type())
hpnicfCBQoSCbqDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSCbqDiscard.setStatus(_A)
_HpnicfCBQoSCbqEfQueueSize_Type=Integer32
_HpnicfCBQoSCbqEfQueueSize_Object=MibTableColumn
hpnicfCBQoSCbqEfQueueSize=_HpnicfCBQoSCbqEfQueueSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,1,1,3),_HpnicfCBQoSCbqEfQueueSize_Type())
hpnicfCBQoSCbqEfQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSCbqEfQueueSize.setStatus(_A)
_HpnicfCBQoSCbqAfQueueSize_Type=Integer32
_HpnicfCBQoSCbqAfQueueSize_Object=MibTableColumn
hpnicfCBQoSCbqAfQueueSize=_HpnicfCBQoSCbqAfQueueSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,1,1,4),_HpnicfCBQoSCbqAfQueueSize_Type())
hpnicfCBQoSCbqAfQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSCbqAfQueueSize.setStatus(_A)
_HpnicfCBQoSCbqBeQueueSize_Type=Integer32
_HpnicfCBQoSCbqBeQueueSize_Object=MibTableColumn
hpnicfCBQoSCbqBeQueueSize=_HpnicfCBQoSCbqBeQueueSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,1,1,5),_HpnicfCBQoSCbqBeQueueSize_Type())
hpnicfCBQoSCbqBeQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSCbqBeQueueSize.setStatus(_A)
_HpnicfCBQoSCbqBeActiveQueueNum_Type=Integer32
_HpnicfCBQoSCbqBeActiveQueueNum_Object=MibTableColumn
hpnicfCBQoSCbqBeActiveQueueNum=_HpnicfCBQoSCbqBeActiveQueueNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,1,1,6),_HpnicfCBQoSCbqBeActiveQueueNum_Type())
hpnicfCBQoSCbqBeActiveQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSCbqBeActiveQueueNum.setStatus(_A)
_HpnicfCBQoSCbqBeMaxActiveQueueNum_Type=Integer32
_HpnicfCBQoSCbqBeMaxActiveQueueNum_Object=MibTableColumn
hpnicfCBQoSCbqBeMaxActiveQueueNum=_HpnicfCBQoSCbqBeMaxActiveQueueNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,1,1,7),_HpnicfCBQoSCbqBeMaxActiveQueueNum_Type())
hpnicfCBQoSCbqBeMaxActiveQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSCbqBeMaxActiveQueueNum.setStatus(_A)
_HpnicfCBQoSCbqBeTotalQueueNum_Type=Integer32
_HpnicfCBQoSCbqBeTotalQueueNum_Object=MibTableColumn
hpnicfCBQoSCbqBeTotalQueueNum=_HpnicfCBQoSCbqBeTotalQueueNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,1,1,8),_HpnicfCBQoSCbqBeTotalQueueNum_Type())
hpnicfCBQoSCbqBeTotalQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSCbqBeTotalQueueNum.setStatus(_A)
_HpnicfCBQoSCbqAfAllocatedQueueNum_Type=Integer32
_HpnicfCBQoSCbqAfAllocatedQueueNum_Object=MibTableColumn
hpnicfCBQoSCbqAfAllocatedQueueNum=_HpnicfCBQoSCbqAfAllocatedQueueNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,1,1,9),_HpnicfCBQoSCbqAfAllocatedQueueNum_Type())
hpnicfCBQoSCbqAfAllocatedQueueNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSCbqAfAllocatedQueueNum.setStatus(_A)
_HpnicfCBQoSClassMatchRunInfoTable_Object=MibTable
hpnicfCBQoSClassMatchRunInfoTable=_HpnicfCBQoSClassMatchRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,2))
if mibBuilder.loadTexts:hpnicfCBQoSClassMatchRunInfoTable.setStatus(_A)
_HpnicfCBQoSClassMatchRunInfoEntry_Object=MibTableRow
hpnicfCBQoSClassMatchRunInfoEntry=_HpnicfCBQoSClassMatchRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,2,1))
hpnicfCBQoSClassMatchRunInfoEntry.setIndexNames((0,_B,_K),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfCBQoSClassMatchRunInfoEntry.setStatus(_A)
_HpnicfCBQoSClassMatchedPackets_Type=Counter64
_HpnicfCBQoSClassMatchedPackets_Object=MibTableColumn
hpnicfCBQoSClassMatchedPackets=_HpnicfCBQoSClassMatchedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,2,1,1),_HpnicfCBQoSClassMatchedPackets_Type())
hpnicfCBQoSClassMatchedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSClassMatchedPackets.setStatus(_A)
_HpnicfCBQoSClassMatchedBytes_Type=Counter64
_HpnicfCBQoSClassMatchedBytes_Object=MibTableColumn
hpnicfCBQoSClassMatchedBytes=_HpnicfCBQoSClassMatchedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,2,1,2),_HpnicfCBQoSClassMatchedBytes_Type())
hpnicfCBQoSClassMatchedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSClassMatchedBytes.setStatus(_A)
_HpnicfCBQoSClassFwdPktpps_Type=Unsigned32
_HpnicfCBQoSClassFwdPktpps_Object=MibTableColumn
hpnicfCBQoSClassFwdPktpps=_HpnicfCBQoSClassFwdPktpps_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,2,1,3),_HpnicfCBQoSClassFwdPktpps_Type())
hpnicfCBQoSClassFwdPktpps.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSClassFwdPktpps.setStatus(_A)
_HpnicfCBQoSClassFwdPktbps_Type=Unsigned32
_HpnicfCBQoSClassFwdPktbps_Object=MibTableColumn
hpnicfCBQoSClassFwdPktbps=_HpnicfCBQoSClassFwdPktbps_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,2,1,4),_HpnicfCBQoSClassFwdPktbps_Type())
hpnicfCBQoSClassFwdPktbps.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSClassFwdPktbps.setStatus(_A)
_HpnicfCBQoSClassDropPktpps_Type=Unsigned32
_HpnicfCBQoSClassDropPktpps_Object=MibTableColumn
hpnicfCBQoSClassDropPktpps=_HpnicfCBQoSClassDropPktpps_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,2,1,5),_HpnicfCBQoSClassDropPktpps_Type())
hpnicfCBQoSClassDropPktpps.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSClassDropPktpps.setStatus(_A)
_HpnicfCBQoSClassDropPktbps_Type=Unsigned32
_HpnicfCBQoSClassDropPktbps_Object=MibTableColumn
hpnicfCBQoSClassDropPktbps=_HpnicfCBQoSClassDropPktbps_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,2,1,6),_HpnicfCBQoSClassDropPktbps_Type())
hpnicfCBQoSClassDropPktbps.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSClassDropPktbps.setStatus(_A)
_HpnicfCBQoSClassFlowStatInterval_Type=Unsigned32
_HpnicfCBQoSClassFlowStatInterval_Object=MibTableColumn
hpnicfCBQoSClassFlowStatInterval=_HpnicfCBQoSClassFlowStatInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,2,1,7),_HpnicfCBQoSClassFlowStatInterval_Type())
hpnicfCBQoSClassFlowStatInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSClassFlowStatInterval.setStatus(_A)
class _HpnicfCBQoSClassBehaviorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_W,1),('failure',2),('partialSuccess',3)))
_HpnicfCBQoSClassBehaviorStatus_Type.__name__=_E
_HpnicfCBQoSClassBehaviorStatus_Object=MibTableColumn
hpnicfCBQoSClassBehaviorStatus=_HpnicfCBQoSClassBehaviorStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,2,1,8),_HpnicfCBQoSClassBehaviorStatus_Type())
hpnicfCBQoSClassBehaviorStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSClassBehaviorStatus.setStatus(_A)
_HpnicfCBQoSCarRunInfoTable_Object=MibTable
hpnicfCBQoSCarRunInfoTable=_HpnicfCBQoSCarRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,3))
if mibBuilder.loadTexts:hpnicfCBQoSCarRunInfoTable.setStatus(_A)
_HpnicfCBQoSCarRunInfoEntry_Object=MibTableRow
hpnicfCBQoSCarRunInfoEntry=_HpnicfCBQoSCarRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,3,1))
hpnicfCBQoSCarRunInfoEntry.setIndexNames((0,_B,_K),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfCBQoSCarRunInfoEntry.setStatus(_A)
_HpnicfCBQoSCarGreenPackets_Type=Counter64
_HpnicfCBQoSCarGreenPackets_Object=MibTableColumn
hpnicfCBQoSCarGreenPackets=_HpnicfCBQoSCarGreenPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,3,1,1),_HpnicfCBQoSCarGreenPackets_Type())
hpnicfCBQoSCarGreenPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSCarGreenPackets.setStatus(_A)
_HpnicfCBQoSCarGreenBytes_Type=Counter64
_HpnicfCBQoSCarGreenBytes_Object=MibTableColumn
hpnicfCBQoSCarGreenBytes=_HpnicfCBQoSCarGreenBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,3,1,2),_HpnicfCBQoSCarGreenBytes_Type())
hpnicfCBQoSCarGreenBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSCarGreenBytes.setStatus(_A)
_HpnicfCBQoSCarRedPackets_Type=Counter64
_HpnicfCBQoSCarRedPackets_Object=MibTableColumn
hpnicfCBQoSCarRedPackets=_HpnicfCBQoSCarRedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,3,1,3),_HpnicfCBQoSCarRedPackets_Type())
hpnicfCBQoSCarRedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSCarRedPackets.setStatus(_A)
_HpnicfCBQoSCarRedBytes_Type=Counter64
_HpnicfCBQoSCarRedBytes_Object=MibTableColumn
hpnicfCBQoSCarRedBytes=_HpnicfCBQoSCarRedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,3,1,4),_HpnicfCBQoSCarRedBytes_Type())
hpnicfCBQoSCarRedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSCarRedBytes.setStatus(_A)
_HpnicfCBQoSCarYellowPackets_Type=Counter64
_HpnicfCBQoSCarYellowPackets_Object=MibTableColumn
hpnicfCBQoSCarYellowPackets=_HpnicfCBQoSCarYellowPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,3,1,5),_HpnicfCBQoSCarYellowPackets_Type())
hpnicfCBQoSCarYellowPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSCarYellowPackets.setStatus(_A)
_HpnicfCBQoSCarYellowBytes_Type=Counter64
_HpnicfCBQoSCarYellowBytes_Object=MibTableColumn
hpnicfCBQoSCarYellowBytes=_HpnicfCBQoSCarYellowBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,3,1,6),_HpnicfCBQoSCarYellowBytes_Type())
hpnicfCBQoSCarYellowBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSCarYellowBytes.setStatus(_A)
_HpnicfCBQoSGtsRunInfoTable_Object=MibTable
hpnicfCBQoSGtsRunInfoTable=_HpnicfCBQoSGtsRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,4))
if mibBuilder.loadTexts:hpnicfCBQoSGtsRunInfoTable.setStatus(_A)
_HpnicfCBQoSGtsRunInfoEntry_Object=MibTableRow
hpnicfCBQoSGtsRunInfoEntry=_HpnicfCBQoSGtsRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,4,1))
hpnicfCBQoSGtsRunInfoEntry.setIndexNames((0,_B,_K),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfCBQoSGtsRunInfoEntry.setStatus(_A)
_HpnicfCBQoSGtsPassedPackets_Type=Counter64
_HpnicfCBQoSGtsPassedPackets_Object=MibTableColumn
hpnicfCBQoSGtsPassedPackets=_HpnicfCBQoSGtsPassedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,4,1,1),_HpnicfCBQoSGtsPassedPackets_Type())
hpnicfCBQoSGtsPassedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSGtsPassedPackets.setStatus(_A)
_HpnicfCBQoSGtsPassedBytes_Type=Counter64
_HpnicfCBQoSGtsPassedBytes_Object=MibTableColumn
hpnicfCBQoSGtsPassedBytes=_HpnicfCBQoSGtsPassedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,4,1,2),_HpnicfCBQoSGtsPassedBytes_Type())
hpnicfCBQoSGtsPassedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSGtsPassedBytes.setStatus(_A)
_HpnicfCBQoSGtsDiscardedPackets_Type=Counter64
_HpnicfCBQoSGtsDiscardedPackets_Object=MibTableColumn
hpnicfCBQoSGtsDiscardedPackets=_HpnicfCBQoSGtsDiscardedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,4,1,3),_HpnicfCBQoSGtsDiscardedPackets_Type())
hpnicfCBQoSGtsDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSGtsDiscardedPackets.setStatus(_A)
_HpnicfCBQoSGtsDiscardedBytes_Type=Counter64
_HpnicfCBQoSGtsDiscardedBytes_Object=MibTableColumn
hpnicfCBQoSGtsDiscardedBytes=_HpnicfCBQoSGtsDiscardedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,4,1,4),_HpnicfCBQoSGtsDiscardedBytes_Type())
hpnicfCBQoSGtsDiscardedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSGtsDiscardedBytes.setStatus(_A)
_HpnicfCBQoSGtsDelayedPackets_Type=Counter64
_HpnicfCBQoSGtsDelayedPackets_Object=MibTableColumn
hpnicfCBQoSGtsDelayedPackets=_HpnicfCBQoSGtsDelayedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,4,1,5),_HpnicfCBQoSGtsDelayedPackets_Type())
hpnicfCBQoSGtsDelayedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSGtsDelayedPackets.setStatus(_A)
_HpnicfCBQoSGtsDelayedBytes_Type=Counter64
_HpnicfCBQoSGtsDelayedBytes_Object=MibTableColumn
hpnicfCBQoSGtsDelayedBytes=_HpnicfCBQoSGtsDelayedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,4,1,6),_HpnicfCBQoSGtsDelayedBytes_Type())
hpnicfCBQoSGtsDelayedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSGtsDelayedBytes.setStatus(_A)
_HpnicfCBQoSGtsQueueSize_Type=Integer32
_HpnicfCBQoSGtsQueueSize_Object=MibTableColumn
hpnicfCBQoSGtsQueueSize=_HpnicfCBQoSGtsQueueSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,4,1,7),_HpnicfCBQoSGtsQueueSize_Type())
hpnicfCBQoSGtsQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSGtsQueueSize.setStatus(_A)
_HpnicfCBQoSRemarkRunInfoTable_Object=MibTable
hpnicfCBQoSRemarkRunInfoTable=_HpnicfCBQoSRemarkRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,5))
if mibBuilder.loadTexts:hpnicfCBQoSRemarkRunInfoTable.setStatus(_A)
_HpnicfCBQoSRemarkRunInfoEntry_Object=MibTableRow
hpnicfCBQoSRemarkRunInfoEntry=_HpnicfCBQoSRemarkRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,5,1))
hpnicfCBQoSRemarkRunInfoEntry.setIndexNames((0,_B,_K),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfCBQoSRemarkRunInfoEntry.setStatus(_A)
_HpnicfCBQoSRemarkedPackets_Type=Counter64
_HpnicfCBQoSRemarkedPackets_Object=MibTableColumn
hpnicfCBQoSRemarkedPackets=_HpnicfCBQoSRemarkedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,5,1,1),_HpnicfCBQoSRemarkedPackets_Type())
hpnicfCBQoSRemarkedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSRemarkedPackets.setStatus(_A)
_HpnicfCBQoSQueueRunInfoTable_Object=MibTable
hpnicfCBQoSQueueRunInfoTable=_HpnicfCBQoSQueueRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,6))
if mibBuilder.loadTexts:hpnicfCBQoSQueueRunInfoTable.setStatus(_A)
_HpnicfCBQoSQueueRunInfoEntry_Object=MibTableRow
hpnicfCBQoSQueueRunInfoEntry=_HpnicfCBQoSQueueRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,6,1))
hpnicfCBQoSQueueRunInfoEntry.setIndexNames((0,_B,_K),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfCBQoSQueueRunInfoEntry.setStatus(_A)
_HpnicfCBQoSQueueMatchedPackets_Type=Counter64
_HpnicfCBQoSQueueMatchedPackets_Object=MibTableColumn
hpnicfCBQoSQueueMatchedPackets=_HpnicfCBQoSQueueMatchedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,6,1,1),_HpnicfCBQoSQueueMatchedPackets_Type())
hpnicfCBQoSQueueMatchedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSQueueMatchedPackets.setStatus(_A)
_HpnicfCBQoSQueueMatchedBytes_Type=Counter64
_HpnicfCBQoSQueueMatchedBytes_Object=MibTableColumn
hpnicfCBQoSQueueMatchedBytes=_HpnicfCBQoSQueueMatchedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,6,1,2),_HpnicfCBQoSQueueMatchedBytes_Type())
hpnicfCBQoSQueueMatchedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSQueueMatchedBytes.setStatus(_A)
_HpnicfCBQoSQueueEnqueuedPackets_Type=Counter64
_HpnicfCBQoSQueueEnqueuedPackets_Object=MibTableColumn
hpnicfCBQoSQueueEnqueuedPackets=_HpnicfCBQoSQueueEnqueuedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,6,1,3),_HpnicfCBQoSQueueEnqueuedPackets_Type())
hpnicfCBQoSQueueEnqueuedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSQueueEnqueuedPackets.setStatus(_A)
_HpnicfCBQoSQueueEnqueuedBytes_Type=Counter64
_HpnicfCBQoSQueueEnqueuedBytes_Object=MibTableColumn
hpnicfCBQoSQueueEnqueuedBytes=_HpnicfCBQoSQueueEnqueuedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,6,1,4),_HpnicfCBQoSQueueEnqueuedBytes_Type())
hpnicfCBQoSQueueEnqueuedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSQueueEnqueuedBytes.setStatus(_A)
_HpnicfCBQoSQueueDiscardedPackets_Type=Counter64
_HpnicfCBQoSQueueDiscardedPackets_Object=MibTableColumn
hpnicfCBQoSQueueDiscardedPackets=_HpnicfCBQoSQueueDiscardedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,6,1,5),_HpnicfCBQoSQueueDiscardedPackets_Type())
hpnicfCBQoSQueueDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSQueueDiscardedPackets.setStatus(_A)
_HpnicfCBQoSQueueDiscardedBytes_Type=Counter64
_HpnicfCBQoSQueueDiscardedBytes_Object=MibTableColumn
hpnicfCBQoSQueueDiscardedBytes=_HpnicfCBQoSQueueDiscardedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,6,1,6),_HpnicfCBQoSQueueDiscardedBytes_Type())
hpnicfCBQoSQueueDiscardedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSQueueDiscardedBytes.setStatus(_A)
_HpnicfCBQoSWredRunInfoTable_Object=MibTable
hpnicfCBQoSWredRunInfoTable=_HpnicfCBQoSWredRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,7))
if mibBuilder.loadTexts:hpnicfCBQoSWredRunInfoTable.setStatus(_A)
_HpnicfCBQoSWredRunInfoEntry_Object=MibTableRow
hpnicfCBQoSWredRunInfoEntry=_HpnicfCBQoSWredRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,7,1))
hpnicfCBQoSWredRunInfoEntry.setIndexNames((0,_B,_K),(0,_B,_G),(0,_B,_T))
if mibBuilder.loadTexts:hpnicfCBQoSWredRunInfoEntry.setStatus(_A)
_HpnicfCBQoSWredRandomDiscardedPackets_Type=Counter64
_HpnicfCBQoSWredRandomDiscardedPackets_Object=MibTableColumn
hpnicfCBQoSWredRandomDiscardedPackets=_HpnicfCBQoSWredRandomDiscardedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,7,1,1),_HpnicfCBQoSWredRandomDiscardedPackets_Type())
hpnicfCBQoSWredRandomDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSWredRandomDiscardedPackets.setStatus(_A)
_HpnicfCBQoSWredTailDiscardedPackets_Type=Counter64
_HpnicfCBQoSWredTailDiscardedPackets_Object=MibTableColumn
hpnicfCBQoSWredTailDiscardedPackets=_HpnicfCBQoSWredTailDiscardedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,7,1,2),_HpnicfCBQoSWredTailDiscardedPackets_Type())
hpnicfCBQoSWredTailDiscardedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSWredTailDiscardedPackets.setStatus(_A)
_HpnicfCBQoSAccountingRunInfoTable_Object=MibTable
hpnicfCBQoSAccountingRunInfoTable=_HpnicfCBQoSAccountingRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,8))
if mibBuilder.loadTexts:hpnicfCBQoSAccountingRunInfoTable.setStatus(_A)
_HpnicfCBQoSAccountingRunInfoEntry_Object=MibTableRow
hpnicfCBQoSAccountingRunInfoEntry=_HpnicfCBQoSAccountingRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,8,1))
hpnicfCBQoSAccountingRunInfoEntry.setIndexNames((0,_B,_K),(0,_B,_G))
if mibBuilder.loadTexts:hpnicfCBQoSAccountingRunInfoEntry.setStatus(_A)
_HpnicfCBQoSAccountingPackets_Type=Counter64
_HpnicfCBQoSAccountingPackets_Object=MibTableColumn
hpnicfCBQoSAccountingPackets=_HpnicfCBQoSAccountingPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,8,1,1),_HpnicfCBQoSAccountingPackets_Type())
hpnicfCBQoSAccountingPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAccountingPackets.setStatus(_A)
_HpnicfCBQoSAccountingBytes_Type=Counter64
_HpnicfCBQoSAccountingBytes_Object=MibTableColumn
hpnicfCBQoSAccountingBytes=_HpnicfCBQoSAccountingBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,5,6,8,1,2),_HpnicfCBQoSAccountingBytes_Type())
hpnicfCBQoSAccountingBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSAccountingBytes.setStatus(_A)
_HpnicfCBQoSApplyingStatusObjects_ObjectIdentity=ObjectIdentity
hpnicfCBQoSApplyingStatusObjects=_HpnicfCBQoSApplyingStatusObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,6))
class _HpnicfCBQoSApplyingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('idle',1),('busy',2)))
_HpnicfCBQoSApplyingStatus_Type.__name__=_E
_HpnicfCBQoSApplyingStatus_Object=MibScalar
hpnicfCBQoSApplyingStatus=_HpnicfCBQoSApplyingStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,6,1),_HpnicfCBQoSApplyingStatus_Type())
hpnicfCBQoSApplyingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfCBQoSApplyingStatus.setStatus(_A)
_HpnicfCBQoSNotifications_ObjectIdentity=ObjectIdentity
hpnicfCBQoSNotifications=_HpnicfCBQoSNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,7))
_HpnicfCBQoSNotificationsPrefix_ObjectIdentity=ObjectIdentity
hpnicfCBQoSNotificationsPrefix=_HpnicfCBQoSNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,7,0))
hpnicfCBQoSIfPolicyChanged=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,7,0,1))
hpnicfCBQoSIfPolicyChanged.setObjects(*((_B,_J),(_B,_L)))
if mibBuilder.loadTexts:hpnicfCBQoSIfPolicyChanged.setStatus(_A)
hpnicfCBQoSVlanPolicyChanged=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,65,2,1,7,0,2))
hpnicfCBQoSVlanPolicyChanged.setObjects(*((_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:hpnicfCBQoSVlanPolicyChanged.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'MatchRuleType':MatchRuleType,_d:CarAction,'RemarkType':RemarkType,_r:WredType,'QueueType':QueueType,'QueueBandwidthUnit':QueueBandwidthUnit,'DirectionType':DirectionType,'ApplyObjectType':ApplyObjectType,'hpnicfQos2':hpnicfQos2,'hpnicfCBQos2':hpnicfCBQos2,'hpnicfCBQoSObjects':hpnicfCBQoSObjects,'hpnicfCBQoSClassifierObjects':hpnicfCBQoSClassifierObjects,'hpnicfCBQoSClassifierIndexNext':hpnicfCBQoSClassifierIndexNext,'hpnicfCBQoSClassifierCfgInfoTable':hpnicfCBQoSClassifierCfgInfoTable,'hpnicfCBQoSClassifierCfgInfoEntry':hpnicfCBQoSClassifierCfgInfoEntry,_U:hpnicfCBQoSClassifierIndex,'hpnicfCBQoSClassifierName':hpnicfCBQoSClassifierName,'hpnicfCBQoSClassifierRuleCount':hpnicfCBQoSClassifierRuleCount,'hpnicfCBQoSClassifierOperator':hpnicfCBQoSClassifierOperator,'hpnicfCBQoSClassifierLayer':hpnicfCBQoSClassifierLayer,'hpnicfCBQoSClassifierType':hpnicfCBQoSClassifierType,'hpnicfCBQosClassifierMatchRuleNextIndex':hpnicfCBQosClassifierMatchRuleNextIndex,'hpnicfCBQoSClassifierRowStatus':hpnicfCBQoSClassifierRowStatus,'hpnicfCBQoSMatchRuleCfgInfoTable':hpnicfCBQoSMatchRuleCfgInfoTable,'hpnicfCBQoSMatchRuleCfgInfoEntry':hpnicfCBQoSMatchRuleCfgInfoEntry,_c:hpnicfCBQoSMatchRuleIndex,'hpnicfCBQoSMatchRuleIfNot':hpnicfCBQoSMatchRuleIfNot,'hpnicfCBQoSMatchRuleType':hpnicfCBQoSMatchRuleType,'hpnicfCBQoSMatchRuleStringValue':hpnicfCBQoSMatchRuleStringValue,'hpnicfCBQoSMatchRuleIntValue1':hpnicfCBQoSMatchRuleIntValue1,'hpnicfCBQoSMatchRuleIntValue2':hpnicfCBQoSMatchRuleIntValue2,'hpnicfCBQoSMatchIpAddressType':hpnicfCBQoSMatchIpAddressType,'hpnicfCBQoSMatchIpAddress':hpnicfCBQoSMatchIpAddress,'hpnicfCBQoSMatchRuleRowStatus':hpnicfCBQoSMatchRuleRowStatus,'hpnicfCBQoSMatchCpProtoCfgTable':hpnicfCBQoSMatchCpProtoCfgTable,'hpnicfCBQoSMatchCpProtoCfgEntry':hpnicfCBQoSMatchCpProtoCfgEntry,'hpnicfCBQoSMatchCpProtoIfNot':hpnicfCBQoSMatchCpProtoIfNot,'hpnicfCBQoSMatchCpProtoValue':hpnicfCBQoSMatchCpProtoValue,'hpnicfCBQoSMatchCpProtoRowStatus':hpnicfCBQoSMatchCpProtoRowStatus,'hpnicfCBQoSMatchCpGroupCfgTable':hpnicfCBQoSMatchCpGroupCfgTable,'hpnicfCBQoSMatchCpGroupCfgEntry':hpnicfCBQoSMatchCpGroupCfgEntry,'hpnicfCBQoSMatchCpGroupIfNot':hpnicfCBQoSMatchCpGroupIfNot,'hpnicfCBQoSMatchCpGroupValue':hpnicfCBQoSMatchCpGroupValue,'hpnicfCBQoSMatchCpGroupRowStatus':hpnicfCBQoSMatchCpGroupRowStatus,'hpnicfCBQoSBehaviorObjects':hpnicfCBQoSBehaviorObjects,'hpnicfCBQoSBehaviorIndexNext':hpnicfCBQoSBehaviorIndexNext,'hpnicfCBQoSBehaviorCfgInfoTable':hpnicfCBQoSBehaviorCfgInfoTable,'hpnicfCBQoSBehaviorCfgInfoEntry':hpnicfCBQoSBehaviorCfgInfoEntry,_H:hpnicfCBQoSBehaviorIndex,'hpnicfCBQoSBehaviorName':hpnicfCBQoSBehaviorName,'hpnicfCBQoSBehaviorType':hpnicfCBQoSBehaviorType,'hpnicfCBQoSBehaviorRowStatus':hpnicfCBQoSBehaviorRowStatus,'hpnicfCBQoSCarCfgInfoTable':hpnicfCBQoSCarCfgInfoTable,'hpnicfCBQoSCarCfgInfoEntry':hpnicfCBQoSCarCfgInfoEntry,'hpnicfCBQoSCarCir':hpnicfCBQoSCarCir,'hpnicfCBQoSCarCbs':hpnicfCBQoSCarCbs,'hpnicfCBQoSCarEbs':hpnicfCBQoSCarEbs,'hpnicfCBQoSCarPir':hpnicfCBQoSCarPir,'hpnicfCBQoSCarPbs':hpnicfCBQoSCarPbs,'hpnicfCBQoSCarGreenAction':hpnicfCBQoSCarGreenAction,'hpnicfCBQoSCarGreenRemarkValue':hpnicfCBQoSCarGreenRemarkValue,'hpnicfCBQoSCarYellowAction':hpnicfCBQoSCarYellowAction,'hpnicfCBQoSCarYellowRemarkValue':hpnicfCBQoSCarYellowRemarkValue,'hpnicfCBQoSCarRedAction':hpnicfCBQoSCarRedAction,'hpnicfCBQoSCarRedRemarkValue':hpnicfCBQoSCarRedRemarkValue,'hpnicfCBQoSCarPolicedPriorityMapType':hpnicfCBQoSCarPolicedPriorityMapType,'hpnicfCBQoSCarRowStatus':hpnicfCBQoSCarRowStatus,'hpnicfCBQoSAggregativeCarCfgInfoTable':hpnicfCBQoSAggregativeCarCfgInfoTable,'hpnicfCBQoSAggregativeCarCfgInfoEntry':hpnicfCBQoSAggregativeCarCfgInfoEntry,_p:hpnicfCBQoSCarAggregativeCarIndex,'hpnicfCBQoSCarAggregativeCarName':hpnicfCBQoSCarAggregativeCarName,'hpnicfCBQoSAggregativeCarRowStatus':hpnicfCBQoSAggregativeCarRowStatus,'hpnicfCBQoSGtsCfgInfoTable':hpnicfCBQoSGtsCfgInfoTable,'hpnicfCBQoSGtsCfgInfoEntry':hpnicfCBQoSGtsCfgInfoEntry,'hpnicfCBQoSGtsCir':hpnicfCBQoSGtsCir,'hpnicfCBQoSGtsCbs':hpnicfCBQoSGtsCbs,'hpnicfCBQoSGtsEbs':hpnicfCBQoSGtsEbs,'hpnicfCBQoSGtsQueueLength':hpnicfCBQoSGtsQueueLength,'hpnicfCBQoSGtsRowStatus':hpnicfCBQoSGtsRowStatus,'hpnicfCBQoSGtsPir':hpnicfCBQoSGtsPir,'hpnicfCBQoSRemarkCfgInfoTable':hpnicfCBQoSRemarkCfgInfoTable,'hpnicfCBQoSRemarkCfgInfoEntry':hpnicfCBQoSRemarkCfgInfoEntry,_q:hpnicfCBQoSRemarkType,'hpnicfCBQoSRemarkValue':hpnicfCBQoSRemarkValue,'hpnicfCBQoSRemarkRowStatus':hpnicfCBQoSRemarkRowStatus,'hpnicfCBQoSQueueCfgInfoTable':hpnicfCBQoSQueueCfgInfoTable,'hpnicfCBQoSQueueCfgInfoEntry':hpnicfCBQoSQueueCfgInfoEntry,'hpnicfCBQoSQueueType':hpnicfCBQoSQueueType,'hpnicfCBQoSQueueDropType':hpnicfCBQoSQueueDropType,'hpnicfCBQoSQueueLength':hpnicfCBQoSQueueLength,'hpnicfCBQoSQueueBandwidthUnit':hpnicfCBQoSQueueBandwidthUnit,'hpnicfCBQoSQueueBandwidthValue':hpnicfCBQoSQueueBandwidthValue,'hpnicfCBQoSQueueCbs':hpnicfCBQoSQueueCbs,'hpnicfCBQoSQueueQueueNumber':hpnicfCBQoSQueueQueueNumber,'hpnicfCBQoSQueueCbsRatio':hpnicfCBQoSQueueCbsRatio,'hpnicfCBQoSQueueRowStatus':hpnicfCBQoSQueueRowStatus,'hpnicfCBQoSWredCfgInfoTable':hpnicfCBQoSWredCfgInfoTable,'hpnicfCBQoSWredCfgInfoEntry':hpnicfCBQoSWredCfgInfoEntry,'hpnicfCBQoSWredType':hpnicfCBQoSWredType,'hpnicfCBQoSWredWeightConst':hpnicfCBQoSWredWeightConst,'hpnicfCBQoSWredClassCfgInfoTable':hpnicfCBQoSWredClassCfgInfoTable,'hpnicfCBQoSWredClassCfgInfoEntry':hpnicfCBQoSWredClassCfgInfoEntry,_T:hpnicfCBQoSWredClassValue,'hpnicfCBQoSWredClassLowLimit':hpnicfCBQoSWredClassLowLimit,'hpnicfCBQoSWredClassHighLimit':hpnicfCBQoSWredClassHighLimit,'hpnicfCBQoSWredClassDiscardProb':hpnicfCBQoSWredClassDiscardProb,'hpnicfCBQoSPolicyRouteCfgInfoTable':hpnicfCBQoSPolicyRouteCfgInfoTable,'hpnicfCBQoSPolicyRouteCfgInfoEntry':hpnicfCBQoSPolicyRouteCfgInfoEntry,'hpnicfCBQoSPolicyRouteIpAddrType':hpnicfCBQoSPolicyRouteIpAddrType,'hpnicfCBQoSPolicyRouteNexthop':hpnicfCBQoSPolicyRouteNexthop,'hpnicfCBQoSPolicyRouteBackup':hpnicfCBQoSPolicyRouteBackup,'hpnicfCBQoSPolicyRouteRowStatus':hpnicfCBQoSPolicyRouteRowStatus,'hpnicfCBQoSNatCfgInfoTable':hpnicfCBQoSNatCfgInfoTable,'hpnicfCBQoSNatCfgInfoEntry':hpnicfCBQoSNatCfgInfoEntry,'hpnicfCBQoSNatMainNumber':hpnicfCBQoSNatMainNumber,'hpnicfCBQoSNatBackupNumber':hpnicfCBQoSNatBackupNumber,'hpnicfCBQoSNatServiceClass':hpnicfCBQoSNatServiceClass,'hpnicfCBQoSNatRowStatus':hpnicfCBQoSNatRowStatus,'hpnicfCBQoSFirewallCfgInfoTable':hpnicfCBQoSFirewallCfgInfoTable,'hpnicfCBQoSFirewallCfgInfoEntry':hpnicfCBQoSFirewallCfgInfoEntry,'hpnicfCBQoSFirewallAction':hpnicfCBQoSFirewallAction,'hpnicfCBQoSFirewallRowStatus':hpnicfCBQoSFirewallRowStatus,'hpnicfCBQoSSamplingCfgInfoTable':hpnicfCBQoSSamplingCfgInfoTable,'hpnicfCBQoSSamplingCfgInfoEntry':hpnicfCBQoSSamplingCfgInfoEntry,'hpnicfCBQoSSamplingNum':hpnicfCBQoSSamplingNum,'hpnicfCBQoSSamplingRowStatus':hpnicfCBQoSSamplingRowStatus,'hpnicfCBQoSAccountCfgInfoTable':hpnicfCBQoSAccountCfgInfoTable,'hpnicfCBQoSAccountCfgInfoEntry':hpnicfCBQoSAccountCfgInfoEntry,'hpnicfCBQoSAccounting':hpnicfCBQoSAccounting,'hpnicfCBQoSAccountRowStatus':hpnicfCBQoSAccountRowStatus,'hpnicfCBQoSAccountingMode':hpnicfCBQoSAccountingMode,'hpnicfCBQoSRedirectCfgInfoTable':hpnicfCBQoSRedirectCfgInfoTable,'hpnicfCBQoSRedirectCfgInfoEntry':hpnicfCBQoSRedirectCfgInfoEntry,'hpnicfCBQoSRedirectType':hpnicfCBQoSRedirectType,'hpnicfCBQoSRedirectIfIndex':hpnicfCBQoSRedirectIfIndex,'hpnicfCBQoSRedirectIpAddressType':hpnicfCBQoSRedirectIpAddressType,'hpnicfCBQoSRedirectIpAddress1':hpnicfCBQoSRedirectIpAddress1,'hpnicfCBQoSRedirectIpAddress2':hpnicfCBQoSRedirectIpAddress2,'hpnicfCBQoSRedirectRowStatus':hpnicfCBQoSRedirectRowStatus,'hpnicfCBQoSRedirectIpv6Interface1':hpnicfCBQoSRedirectIpv6Interface1,'hpnicfCBQoSRedirectIpv6Interface2':hpnicfCBQoSRedirectIpv6Interface2,'hpnicfCBQoSRedirectIfVlanID':hpnicfCBQoSRedirectIfVlanID,'hpnicfCBQoSPriorityMapCfgInfoTable':hpnicfCBQoSPriorityMapCfgInfoTable,'hpnicfCBQoSPriorityMapCfgInfoEntry':hpnicfCBQoSPriorityMapCfgInfoEntry,'hpnicfCBQoSPriorityMapImportType':hpnicfCBQoSPriorityMapImportType,'hpnicfCBQoSPriorityMapExportType':hpnicfCBQoSPriorityMapExportType,'hpnicfCBQoSPriorityMapGroupIndex':hpnicfCBQoSPriorityMapGroupIndex,'hpnicfCBQoSPriorityMapGroupName':hpnicfCBQoSPriorityMapGroupName,'hpnicfCBQoSPriorityMapAuto':hpnicfCBQoSPriorityMapAuto,'hpnicfCBQoSPriorityMapRowStatus':hpnicfCBQoSPriorityMapRowStatus,'hpnicfCBQoSMirrorCfgInfoTable':hpnicfCBQoSMirrorCfgInfoTable,'hpnicfCBQoSMirrorCfgInfoEntry':hpnicfCBQoSMirrorCfgInfoEntry,'hpnicfCBQoSMirrorType':hpnicfCBQoSMirrorType,'hpnicfCBQoSMirrorIfIndex':hpnicfCBQoSMirrorIfIndex,'hpnicfCBQoSMirrorVlanID':hpnicfCBQoSMirrorVlanID,'hpnicfCBQoSMirrorRowStatus':hpnicfCBQoSMirrorRowStatus,'hpnicfCBQoSNestCfgInfoTable':hpnicfCBQoSNestCfgInfoTable,'hpnicfCBQoSNestCfgInfoEntry':hpnicfCBQoSNestCfgInfoEntry,'hpnicfCBQoSNestServiceVlanID':hpnicfCBQoSNestServiceVlanID,'hpnicfCBQoSNestServiceDot1pValue':hpnicfCBQoSNestServiceDot1pValue,'hpnicfCBQoSNestCustomerVlanID':hpnicfCBQoSNestCustomerVlanID,'hpnicfCBQoSNestCustomerDot1pValue':hpnicfCBQoSNestCustomerDot1pValue,'hpnicfCBQoSNestRowStatus':hpnicfCBQoSNestRowStatus,'hpnicfCBQoSNestPolicyCfgInfoTable':hpnicfCBQoSNestPolicyCfgInfoTable,'hpnicfCBQoSNestPolicyCfgInfoEntry':hpnicfCBQoSNestPolicyCfgInfoEntry,'hpnicfCBQoSNestPolicyName':hpnicfCBQoSNestPolicyName,'hpnicfCBQoSNestPolicyRowStatus':hpnicfCBQoSNestPolicyRowStatus,'hpnicfCBQoSMirrorIfCfgInfoTable':hpnicfCBQoSMirrorIfCfgInfoTable,'hpnicfCBQoSMirrorIfCfgInfoEntry':hpnicfCBQoSMirrorIfCfgInfoEntry,_v:hpnicfCBQoSMirrorIfMainIfIndex,'hpnicfCBQoSMirrorIfMainIfStatus':hpnicfCBQoSMirrorIfMainIfStatus,'hpnicfCBQoSMirrorIfBackupIfIndex':hpnicfCBQoSMirrorIfBackupIfIndex,'hpnicfCBQoSMirrorIfBackupIfStatus':hpnicfCBQoSMirrorIfBackupIfStatus,'hpnicfCBQoSMirrorIfRowStatus':hpnicfCBQoSMirrorIfRowStatus,'hpnicfCBQoSColoredRemarkCfgTable':hpnicfCBQoSColoredRemarkCfgTable,'hpnicfCBQoSColoredRemarkCfgEntry':hpnicfCBQoSColoredRemarkCfgEntry,_y:hpnicfCBQoSColoredRemarkType,_z:hpnicfCBQoSColoredRemarkColor,'hpnicfCBQoSColoredRemarkValue':hpnicfCBQoSColoredRemarkValue,'hpnicfCBQoSColoredRemarkRowStatus':hpnicfCBQoSColoredRemarkRowStatus,'hpnicfCBQoSPrimapCfgInfoTable':hpnicfCBQoSPrimapCfgInfoTable,'hpnicfCBQoSPrimapCfgInfoEntry':hpnicfCBQoSPrimapCfgInfoEntry,_A0:hpnicfCBQoSPrimapColorType,_A1:hpnicfCBQoSPrePriMapTableType,'hpnicfCBQoSPrimapRowStatus':hpnicfCBQoSPrimapRowStatus,'hpnicfCBQoSColorMapDpCfgInfoTable':hpnicfCBQoSColorMapDpCfgInfoTable,'hpnicfCBQoSColorMapDpCfgInfoEntry':hpnicfCBQoSColorMapDpCfgInfoEntry,'hpnicfCBQoSColorMapDpEnable':hpnicfCBQoSColorMapDpEnable,'hpnicfCBQoSColorMapDpRowStatus':hpnicfCBQoSColorMapDpRowStatus,'hpnicfCBQoSPolicyObjects':hpnicfCBQoSPolicyObjects,'hpnicfCBQoSPolicyIndexNext':hpnicfCBQoSPolicyIndexNext,'hpnicfCBQoSPolicyCfgInfoTable':hpnicfCBQoSPolicyCfgInfoTable,'hpnicfCBQoSPolicyCfgInfoEntry':hpnicfCBQoSPolicyCfgInfoEntry,_n:hpnicfCBQoSPolicyIndex,'hpnicfCBQoSPolicyName':hpnicfCBQoSPolicyName,'hpnicfCBQoSPolicyClassCount':hpnicfCBQoSPolicyClassCount,'hpnicfCBQoSPolicyConfigMode':hpnicfCBQoSPolicyConfigMode,'hpnicfCBQoSPolicyType':hpnicfCBQoSPolicyType,'hpnicfCBQoSPolicyClassNextIndex':hpnicfCBQoSPolicyClassNextIndex,'hpnicfCBQoSPolicyRowStatus':hpnicfCBQoSPolicyRowStatus,'hpnicfCBQoSPolicyClassCfgInfoTable':hpnicfCBQoSPolicyClassCfgInfoTable,'hpnicfCBQoSPolicyClassCfgInfoEntry':hpnicfCBQoSPolicyClassCfgInfoEntry,_G:hpnicfCBQoSPolicyClassIndex,'hpnicfCBQoSPolicyClassClassifierIndex':hpnicfCBQoSPolicyClassClassifierIndex,'hpnicfCBQoSPolicyClassClassifierName':hpnicfCBQoSPolicyClassClassifierName,'hpnicfCBQoSPolicyClassBehaviorIndex':hpnicfCBQoSPolicyClassBehaviorIndex,'hpnicfCBQoSPolicyClassBehaviorName':hpnicfCBQoSPolicyClassBehaviorName,'hpnicfCBQoSPolicyClassPrecedence':hpnicfCBQoSPolicyClassPrecedence,'hpnicfCBQoSPolicyClassRowStatus':hpnicfCBQoSPolicyClassRowStatus,'hpnicfCBQoSPolicyClassMode':hpnicfCBQoSPolicyClassMode,'hpnicfCBQoSPolicyClassCfgOrder':hpnicfCBQoSPolicyClassCfgOrder,'hpnicfCBQoSApplyPolicyObjects':hpnicfCBQoSApplyPolicyObjects,'hpnicfCBQoSIfApplyPolicyTable':hpnicfCBQoSIfApplyPolicyTable,'hpnicfCBQoSIfApplyPolicyEntry':hpnicfCBQoSIfApplyPolicyEntry,_J:hpnicfCBQoSIfApplyPolicyIfIndex,_L:hpnicfCBQoSIfApplyPolicyDirection,'hpnicfCBQoSIfApplyPolicyName':hpnicfCBQoSIfApplyPolicyName,'hpnicfCBQoSIfApplyPolicyEnableDynamic':hpnicfCBQoSIfApplyPolicyEnableDynamic,'hpnicfCBQoSIfApplyPolicyRowStatus':hpnicfCBQoSIfApplyPolicyRowStatus,'hpnicfCBQoSIfApplyPolicyStatus':hpnicfCBQoSIfApplyPolicyStatus,'hpnicfCBQoSAtmPvcApplyPolicyTable':hpnicfCBQoSAtmPvcApplyPolicyTable,'hpnicfCBQoSAtmPvcApplyPolicyEntry':hpnicfCBQoSAtmPvcApplyPolicyEntry,_M:hpnicfCBQoSAtmPvcApplyPolicyIfIndex,_N:hpnicfCBQoSAtmPvcApplyPolicyVPI,_O:hpnicfCBQoSAtmPvcApplyPolicyVCI,_R:hpnicfCBQoSAtmPvcApplyPolicyDirection,'hpnicfCBQoSAtmPvcApplyPolicyName':hpnicfCBQoSAtmPvcApplyPolicyName,'hpnicfCBQoSAtmPvcApplyPolicyRowStatus':hpnicfCBQoSAtmPvcApplyPolicyRowStatus,'hpnicfCBQoSVlanApplyPolicyTable':hpnicfCBQoSVlanApplyPolicyTable,'hpnicfCBQoSVlanApplyPolicyEntry':hpnicfCBQoSVlanApplyPolicyEntry,_X:hpnicfCBQoSVlanApplyPolicyVlanid,_Y:hpnicfCBQoSVlanApplyPolicyDirection,'hpnicfCBQoSVlanApplyPolicyName':hpnicfCBQoSVlanApplyPolicyName,'hpnicfCBQoSVlanApplyPriority':hpnicfCBQoSVlanApplyPriority,'hpnicfCBQoSVlanApplyPolicyRowStatus':hpnicfCBQoSVlanApplyPolicyRowStatus,'hpnicfCBQoSVlanApplyPolicyStatus':hpnicfCBQoSVlanApplyPolicyStatus,'hpnicfCBQoSFrClassApplyPolicyTable':hpnicfCBQoSFrClassApplyPolicyTable,'hpnicfCBQoSFrClassApplyPolicyEntry':hpnicfCBQoSFrClassApplyPolicyEntry,_A2:hpnicfCBQoSFrClassApplyPolicyFrClassName,_A3:hpnicfCBQoSFrClassApplyPolicyDirection,'hpnicfCBQoSFrClassApplyPolicyName':hpnicfCBQoSFrClassApplyPolicyName,'hpnicfCBQoSFrClassApplyPolicyRowStatus':hpnicfCBQoSFrClassApplyPolicyRowStatus,'hpnicfCBQoSFrPvcApplyPolicyTable':hpnicfCBQoSFrPvcApplyPolicyTable,'hpnicfCBQoSFrPvcApplyPolicyEntry':hpnicfCBQoSFrPvcApplyPolicyEntry,_P:hpnicfCBQoSFrPvcApplyPolicyIfIndex,_Q:hpnicfCBQoSFrPvcApplyPolicyDlciNum,_S:hpnicfCBQoSFrPvcApplyPolicyDirection,'hpnicfCBQoSFrPvcApplyPolicyName':hpnicfCBQoSFrPvcApplyPolicyName,'hpnicfCBQoSFrPvcApplyPolicyRowStatus':hpnicfCBQoSFrPvcApplyPolicyRowStatus,'hpnicfCBQoSGlobalApplyTable':hpnicfCBQoSGlobalApplyTable,'hpnicfCBQoSGlobalApplyEntry':hpnicfCBQoSGlobalApplyEntry,_A4:hpnicfCBQoSGlobalApplyDirection,'hpnicfCBQoSGlobalApplyName':hpnicfCBQoSGlobalApplyName,'hpnicfCBQoSGlobalApplyRowStatus':hpnicfCBQoSGlobalApplyRowStatus,'hpnicfCBQoSGlobalApplyStatus':hpnicfCBQoSGlobalApplyStatus,'hpnicfCBQoSCpApplyPolicyTable':hpnicfCBQoSCpApplyPolicyTable,'hpnicfCBQoSCpApplyPolicyEntry':hpnicfCBQoSCpApplyPolicyEntry,_A5:hpnicfCBQoSCpApplyPolicyChassis,_A6:hpnicfCBQoSCpApplyPolicySlot,_A7:hpnicfCBQoSCpApplyPolicyDirection,'hpnicfCBQoSCpApplyPolicyName':hpnicfCBQoSCpApplyPolicyName,'hpnicfCBQoSCpApplyPolicyStatus':hpnicfCBQoSCpApplyPolicyStatus,'hpnicfCBQoSCpApplyRowStatus':hpnicfCBQoSCpApplyRowStatus,'hpnicfCBQoSApplyPolicyStaticsObjects':hpnicfCBQoSApplyPolicyStaticsObjects,'hpnicfCBQoSIfStaticsObjects':hpnicfCBQoSIfStaticsObjects,'hpnicfCBQoSIfCbqRunInfoTable':hpnicfCBQoSIfCbqRunInfoTable,'hpnicfCBQoSIfCbqRunInfoEntry':hpnicfCBQoSIfCbqRunInfoEntry,'hpnicfCBQoSIfCbqQueueSize':hpnicfCBQoSIfCbqQueueSize,'hpnicfCBQoSIfCbqDiscard':hpnicfCBQoSIfCbqDiscard,'hpnicfCBQoSIfCbqEfQueueSize':hpnicfCBQoSIfCbqEfQueueSize,'hpnicfCBQoSIfCbqAfQueueSize':hpnicfCBQoSIfCbqAfQueueSize,'hpnicfCBQoSIfCbqBeQueueSize':hpnicfCBQoSIfCbqBeQueueSize,'hpnicfCBQoSIfCbqBeActiveQueueNum':hpnicfCBQoSIfCbqBeActiveQueueNum,'hpnicfCBQoSIfCbqBeMaxActiveQueueNum':hpnicfCBQoSIfCbqBeMaxActiveQueueNum,'hpnicfCBQoSIfCbqBeTotalQueueNum':hpnicfCBQoSIfCbqBeTotalQueueNum,'hpnicfCBQoSIfCbqAfAllocatedQueueNum':hpnicfCBQoSIfCbqAfAllocatedQueueNum,'hpnicfCBQoSIfClassMatchRunInfoTable':hpnicfCBQoSIfClassMatchRunInfoTable,'hpnicfCBQoSIfClassMatchRunInfoEntry':hpnicfCBQoSIfClassMatchRunInfoEntry,'hpnicfCBQoSIfClassMatchedPackets':hpnicfCBQoSIfClassMatchedPackets,'hpnicfCBQoSIfClassMatchedBytes':hpnicfCBQoSIfClassMatchedBytes,'hpnicfCBQoSIfClassAverageRate':hpnicfCBQoSIfClassAverageRate,'hpnicfCBQoSIfCarRunInfoTable':hpnicfCBQoSIfCarRunInfoTable,'hpnicfCBQoSIfCarRunInfoEntry':hpnicfCBQoSIfCarRunInfoEntry,'hpnicfCBQoSIfCarGreenPackets':hpnicfCBQoSIfCarGreenPackets,'hpnicfCBQoSIfCarGreenBytes':hpnicfCBQoSIfCarGreenBytes,'hpnicfCBQoSIfCarRedPackets':hpnicfCBQoSIfCarRedPackets,'hpnicfCBQoSIfCarRedBytes':hpnicfCBQoSIfCarRedBytes,'hpnicfCBQoSIfCarYellowPackets':hpnicfCBQoSIfCarYellowPackets,'hpnicfCBQoSIfCarYellowBytes':hpnicfCBQoSIfCarYellowBytes,'hpnicfCBQoSIfGtsRunInfoTable':hpnicfCBQoSIfGtsRunInfoTable,'hpnicfCBQoSIfGtsRunInfoEntry':hpnicfCBQoSIfGtsRunInfoEntry,'hpnicfCBQoSIfGtsPassedPackets':hpnicfCBQoSIfGtsPassedPackets,'hpnicfCBQoSIfGtsPassedBytes':hpnicfCBQoSIfGtsPassedBytes,'hpnicfCBQoSIfGtsDiscardedPackets':hpnicfCBQoSIfGtsDiscardedPackets,'hpnicfCBQoSIfGtsDiscardedBytes':hpnicfCBQoSIfGtsDiscardedBytes,'hpnicfCBQoSIfGtsDelayedPackets':hpnicfCBQoSIfGtsDelayedPackets,'hpnicfCBQoSIfGtsDelayedBytes':hpnicfCBQoSIfGtsDelayedBytes,'hpnicfCBQoSIfGtsQueueSize':hpnicfCBQoSIfGtsQueueSize,'hpnicfCBQoSIfRemarkRunInfoTable':hpnicfCBQoSIfRemarkRunInfoTable,'hpnicfCBQoSIfRemarkRunInfoEntry':hpnicfCBQoSIfRemarkRunInfoEntry,'hpnicfCBQoSIfRemarkedPackets':hpnicfCBQoSIfRemarkedPackets,'hpnicfCBQoSIfQueueRunInfoTable':hpnicfCBQoSIfQueueRunInfoTable,'hpnicfCBQoSIfQueueRunInfoEntry':hpnicfCBQoSIfQueueRunInfoEntry,'hpnicfCBQoSIfQueueMatchedPackets':hpnicfCBQoSIfQueueMatchedPackets,'hpnicfCBQoSIfQueueMatchedBytes':hpnicfCBQoSIfQueueMatchedBytes,'hpnicfCBQoSIfQueueEnqueuedPackets':hpnicfCBQoSIfQueueEnqueuedPackets,'hpnicfCBQoSIfQueueEnqueuedBytes':hpnicfCBQoSIfQueueEnqueuedBytes,'hpnicfCBQoSIfQueueDiscardedPackets':hpnicfCBQoSIfQueueDiscardedPackets,'hpnicfCBQoSIfQueueDiscardedBytes':hpnicfCBQoSIfQueueDiscardedBytes,'hpnicfCBQoSIfWredRunInfoTable':hpnicfCBQoSIfWredRunInfoTable,'hpnicfCBQoSIfWredRunInfoEntry':hpnicfCBQoSIfWredRunInfoEntry,'hpnicfCBQoSIfWredRandomDiscardedPackets':hpnicfCBQoSIfWredRandomDiscardedPackets,'hpnicfCBQoSIfWredTailDiscardedPackets':hpnicfCBQoSIfWredTailDiscardedPackets,'hpnicfCBQoSIfAccountingRunInfoTable':hpnicfCBQoSIfAccountingRunInfoTable,'hpnicfCBQoSIfAccountingRunInfoEntry':hpnicfCBQoSIfAccountingRunInfoEntry,'hpnicfCBQoSIfAccountingPackets':hpnicfCBQoSIfAccountingPackets,'hpnicfCBQoSIfAccountingBytes':hpnicfCBQoSIfAccountingBytes,'hpnicfCBQoSAtmPvcStaticsObjects':hpnicfCBQoSAtmPvcStaticsObjects,'hpnicfCBQoSAtmPvcCbqRunInfoTable':hpnicfCBQoSAtmPvcCbqRunInfoTable,'hpnicfCBQoSAtmPvcCbqRunInfoEntry':hpnicfCBQoSAtmPvcCbqRunInfoEntry,'hpnicfCBQoSAtmPvcCbqQueueSize':hpnicfCBQoSAtmPvcCbqQueueSize,'hpnicfCBQoSAtmPvcCbqDiscard':hpnicfCBQoSAtmPvcCbqDiscard,'hpnicfCBQoSAtmPvcCbqEfQueueSize':hpnicfCBQoSAtmPvcCbqEfQueueSize,'hpnicfCBQoSAtmPvcCbqAfQueueSize':hpnicfCBQoSAtmPvcCbqAfQueueSize,'hpnicfCBQoSAtmPvcCbqBeQueueSize':hpnicfCBQoSAtmPvcCbqBeQueueSize,'hpnicfCBQoSAtmPvcCbqBeActiveQueueNum':hpnicfCBQoSAtmPvcCbqBeActiveQueueNum,'hpnicfCBQoSAtmPvcCbqBeMaxActiveQueueNum':hpnicfCBQoSAtmPvcCbqBeMaxActiveQueueNum,'hpnicfCBQoSAtmPvcCbqBeTotalQueueNum':hpnicfCBQoSAtmPvcCbqBeTotalQueueNum,'hpnicfCBQoSAtmPvcCbqAfAllocatedQueueNum':hpnicfCBQoSAtmPvcCbqAfAllocatedQueueNum,'hpnicfCBQoSAtmPvcClassMatchRunInfoTable':hpnicfCBQoSAtmPvcClassMatchRunInfoTable,'hpnicfCBQoSAtmPvcClassMatchRunInfoEntry':hpnicfCBQoSAtmPvcClassMatchRunInfoEntry,'hpnicfCBQoSAtmPvcClassMatchPackets':hpnicfCBQoSAtmPvcClassMatchPackets,'hpnicfCBQoSAtmPvcClassMatchBytes':hpnicfCBQoSAtmPvcClassMatchBytes,'hpnicfCBQoSAtmPvcClassAverageRate':hpnicfCBQoSAtmPvcClassAverageRate,'hpnicfCBQoSAtmPvcCarRunInfoTable':hpnicfCBQoSAtmPvcCarRunInfoTable,'hpnicfCBQoSAtmPvcCarRunInfoEntry':hpnicfCBQoSAtmPvcCarRunInfoEntry,'hpnicfCBQoSAtmPvcCarConformPackets':hpnicfCBQoSAtmPvcCarConformPackets,'hpnicfCBQoSAtmPvcCarConformBytes':hpnicfCBQoSAtmPvcCarConformBytes,'hpnicfCBQoSAtmPvcCarExceedPackets':hpnicfCBQoSAtmPvcCarExceedPackets,'hpnicfCBQoSAtmPvcCarExceedBytes':hpnicfCBQoSAtmPvcCarExceedBytes,'hpnicfCBQoSAtmPvcGtsRunInfoTable':hpnicfCBQoSAtmPvcGtsRunInfoTable,'hpnicfCBQoSAtmPvcGtsRunInfoEntry':hpnicfCBQoSAtmPvcGtsRunInfoEntry,'hpnicfCBQoSAtmPvcGtsPassedPackets':hpnicfCBQoSAtmPvcGtsPassedPackets,'hpnicfCBQoSAtmPvcGtsPassedBytes':hpnicfCBQoSAtmPvcGtsPassedBytes,'hpnicfCBQoSAtmPvcGtsDiscardedPackets':hpnicfCBQoSAtmPvcGtsDiscardedPackets,'hpnicfCBQoSAtmPvcGtsDiscardedBytes':hpnicfCBQoSAtmPvcGtsDiscardedBytes,'hpnicfCBQoSAtmPvcGtsDelayedPackets':hpnicfCBQoSAtmPvcGtsDelayedPackets,'hpnicfCBQoSAtmPvcGtsDelayedBytes':hpnicfCBQoSAtmPvcGtsDelayedBytes,'hpnicfCBQoSAtmPvcGtsQueueSize':hpnicfCBQoSAtmPvcGtsQueueSize,'hpnicfCBQoSAtmPvcRemarkRunInfoTable':hpnicfCBQoSAtmPvcRemarkRunInfoTable,'hpnicfCBQoSAtmPvcRemarkRunInfoEntry':hpnicfCBQoSAtmPvcRemarkRunInfoEntry,'hpnicfCBQoSAtmPvcRemarkedPackets':hpnicfCBQoSAtmPvcRemarkedPackets,'hpnicfCBQoSAtmPvcQueueRunInfoTable':hpnicfCBQoSAtmPvcQueueRunInfoTable,'hpnicfCBQoSAtmPvcQueueRunInfoEntry':hpnicfCBQoSAtmPvcQueueRunInfoEntry,'hpnicfCBQoSAtmPvcQueueMatchedPackets':hpnicfCBQoSAtmPvcQueueMatchedPackets,'hpnicfCBQoSAtmPvcQueueMatchedBytes':hpnicfCBQoSAtmPvcQueueMatchedBytes,'hpnicfCBQoSAtmPvcQueueEnqueuedPackets':hpnicfCBQoSAtmPvcQueueEnqueuedPackets,'hpnicfCBQoSAtmPvcQueueEnqueuedBytes':hpnicfCBQoSAtmPvcQueueEnqueuedBytes,'hpnicfCBQoSAtmPvcQueueDiscardedPackets':hpnicfCBQoSAtmPvcQueueDiscardedPackets,'hpnicfCBQoSAtmPvcQueueDiscardedBytes':hpnicfCBQoSAtmPvcQueueDiscardedBytes,'hpnicfCBQoSAtmPvcWredRunInfoTable':hpnicfCBQoSAtmPvcWredRunInfoTable,'hpnicfCBQoSAtmPvcWredRunInfoEntry':hpnicfCBQoSAtmPvcWredRunInfoEntry,'hpnicfCBQoSAtmPvcWredRandomDiscardedPackets':hpnicfCBQoSAtmPvcWredRandomDiscardedPackets,'hpnicfCBQoSAtmPvcWredTailDiscardedPackets':hpnicfCBQoSAtmPvcWredTailDiscardedPackets,'hpnicfCBQoSAtmPvcAccountingRunInfoTable':hpnicfCBQoSAtmPvcAccountingRunInfoTable,'hpnicfCBQoSAtmPvcAccountingRunInfoEntry':hpnicfCBQoSAtmPvcAccountingRunInfoEntry,'hpnicfCBQoSAtmPvcAccountingPackets':hpnicfCBQoSAtmPvcAccountingPackets,'hpnicfCBQoSAtmPvcAccountingBytes':hpnicfCBQoSAtmPvcAccountingBytes,'hpnicfCBQoSFrPvcStaticsObjects':hpnicfCBQoSFrPvcStaticsObjects,'hpnicfCBQoSFrPvcCbqRunInfoTable':hpnicfCBQoSFrPvcCbqRunInfoTable,'hpnicfCBQoSFrPvcCbqRunInfoEntry':hpnicfCBQoSFrPvcCbqRunInfoEntry,'hpnicfCBQoSFrPvcCbqQueueSize':hpnicfCBQoSFrPvcCbqQueueSize,'hpnicfCBQoSFrPvcCbqDiscard':hpnicfCBQoSFrPvcCbqDiscard,'hpnicfCBQoSFrPvcCbqEfQueueSize':hpnicfCBQoSFrPvcCbqEfQueueSize,'hpnicfCBQoSFrPvcCbqAfQueueSize':hpnicfCBQoSFrPvcCbqAfQueueSize,'hpnicfCBQoSFrPvcCbqBeQueueSize':hpnicfCBQoSFrPvcCbqBeQueueSize,'hpnicfCBQoSFrPvcCbqBeActiveQueueNum':hpnicfCBQoSFrPvcCbqBeActiveQueueNum,'hpnicfCBQoSFrPvcCbqBeMaxActiveQueueNum':hpnicfCBQoSFrPvcCbqBeMaxActiveQueueNum,'hpnicfCBQoSFrPvcCbqBeTotalQueueNum':hpnicfCBQoSFrPvcCbqBeTotalQueueNum,'hpnicfCBQoSFrPvcCbqAfAllocatedQueueNum':hpnicfCBQoSFrPvcCbqAfAllocatedQueueNum,'hpnicfCBQoSFrPvcClassMatchRunInfoTable':hpnicfCBQoSFrPvcClassMatchRunInfoTable,'hpnicfCBQoSFrPvcClassMatchRunInfoEntry':hpnicfCBQoSFrPvcClassMatchRunInfoEntry,'hpnicfCBQoSFrPvcClassMatchedPackets':hpnicfCBQoSFrPvcClassMatchedPackets,'hpnicfCBQoSFrPvcClassMatchedBytes':hpnicfCBQoSFrPvcClassMatchedBytes,'hpnicfCBQoSFrPvcClassAverageRate':hpnicfCBQoSFrPvcClassAverageRate,'hpnicfCBQoSFrPvcCarRunInfoTable':hpnicfCBQoSFrPvcCarRunInfoTable,'hpnicfCBQoSFrPvcCarRunInfoEntry':hpnicfCBQoSFrPvcCarRunInfoEntry,'hpnicfCBQoSFrPvcCarConformPackets':hpnicfCBQoSFrPvcCarConformPackets,'hpnicfCBQoSFrPvcCarConformBytes':hpnicfCBQoSFrPvcCarConformBytes,'hpnicfCBQoSFrPvcCarExceedPackets':hpnicfCBQoSFrPvcCarExceedPackets,'hpnicfCBQoSFrPvcCarExceedBytes':hpnicfCBQoSFrPvcCarExceedBytes,'hpnicfCBQoSFrPvcGtsRunInfoTable':hpnicfCBQoSFrPvcGtsRunInfoTable,'hpnicfCBQoSFrPvcGtsRunInfoEntry':hpnicfCBQoSFrPvcGtsRunInfoEntry,'hpnicfCBQoSFrPvcGtsPassedPackets':hpnicfCBQoSFrPvcGtsPassedPackets,'hpnicfCBQoSFrPvcGtsPassedBytes':hpnicfCBQoSFrPvcGtsPassedBytes,'hpnicfCBQoSFrPvcGtsDiscardedPackets':hpnicfCBQoSFrPvcGtsDiscardedPackets,'hpnicfCBQoSFrPvcGtsDiscardedBytes':hpnicfCBQoSFrPvcGtsDiscardedBytes,'hpnicfCBQoSFrPvcGtsDelayedPackets':hpnicfCBQoSFrPvcGtsDelayedPackets,'hpnicfCBQoSFrPvcGtsDelayedBytes':hpnicfCBQoSFrPvcGtsDelayedBytes,'hpnicfCBQoSFrPvcGtsQueueSize':hpnicfCBQoSFrPvcGtsQueueSize,'hpnicfCBQoSFrPvcRemarkRunInfoTable':hpnicfCBQoSFrPvcRemarkRunInfoTable,'hpnicfCBQoSFrPvcRemarkRunInfoEntry':hpnicfCBQoSFrPvcRemarkRunInfoEntry,'hpnicfCBQoSFrPvcRemarkedPackets':hpnicfCBQoSFrPvcRemarkedPackets,'hpnicfCBQoSFrPvcQueueRunInfoTable':hpnicfCBQoSFrPvcQueueRunInfoTable,'hpnicfCBQoSFrPvcQueueRunInfoEntry':hpnicfCBQoSFrPvcQueueRunInfoEntry,'hpnicfCBQoSFrPvcQueueMatchedPackets':hpnicfCBQoSFrPvcQueueMatchedPackets,'hpnicfCBQoSFrPvcQueueMatchedBytes':hpnicfCBQoSFrPvcQueueMatchedBytes,'hpnicfCBQoSFrPvcQueueEnqueuedPackets':hpnicfCBQoSFrPvcQueueEnqueuedPackets,'hpnicfCBQoSFrPvcQueueEnqueuedBytes':hpnicfCBQoSFrPvcQueueEnqueuedBytes,'hpnicfCBQoSFrPvcQueueDiscardedPackets':hpnicfCBQoSFrPvcQueueDiscardedPackets,'hpnicfCBQoSFrPvcQueueDiscardedBytes':hpnicfCBQoSFrPvcQueueDiscardedBytes,'hpnicfCBQoSFrPvcWredRunInfoTable':hpnicfCBQoSFrPvcWredRunInfoTable,'hpnicfCBQoSFrPvcWredRunInfoEntry':hpnicfCBQoSFrPvcWredRunInfoEntry,'hpnicfCBQoSFrPvcWredRandomDiscardedPackets':hpnicfCBQoSFrPvcWredRandomDiscardedPackets,'hpnicfCBQoSFrPvcWredTailDiscardedPackets':hpnicfCBQoSFrPvcWredTailDiscardedPackets,'hpnicfCBQoSFrPvcAccountingRunInfoTable':hpnicfCBQoSFrPvcAccountingRunInfoTable,'hpnicfCBQoSFrPvcAccountingRunInfoEntry':hpnicfCBQoSFrPvcAccountingRunInfoEntry,'hpnicfCBQoSFrPvcAccountingPackets':hpnicfCBQoSFrPvcAccountingPackets,'hpnicfCBQoSFrPvcAccountingBytes':hpnicfCBQoSFrPvcAccountingBytes,'hpnicfCBQoSVlanStaticsObjects':hpnicfCBQoSVlanStaticsObjects,'hpnicfCBQoSVlanClassMatchRunInfoTable':hpnicfCBQoSVlanClassMatchRunInfoTable,'hpnicfCBQoSVlanClassMatchRunInfoEntry':hpnicfCBQoSVlanClassMatchRunInfoEntry,'hpnicfCBQoSVlanClassMatchedPackets':hpnicfCBQoSVlanClassMatchedPackets,'hpnicfCBQoSVlanAccountingRunInfoTable':hpnicfCBQoSVlanAccountingRunInfoTable,'hpnicfCBQoSVlanAccountingRunInfoEntry':hpnicfCBQoSVlanAccountingRunInfoEntry,'hpnicfCBQoSVlanAccountingPackets':hpnicfCBQoSVlanAccountingPackets,'hpnicfCBQoSVlanAccountingBytes':hpnicfCBQoSVlanAccountingBytes,'hpnicfCBQoSApplyPolicyIndexObjects':hpnicfCBQoSApplyPolicyIndexObjects,'hpnicfCBQoSApplyObjectTable':hpnicfCBQoSApplyObjectTable,'hpnicfCBQoSApplyObjectEntry':hpnicfCBQoSApplyObjectEntry,_K:hpnicfCBQoSApplyObjectIndex,'hpnicfCBQoSApplyObjectType':hpnicfCBQoSApplyObjectType,_Z:hpnicfCBQoSApplyObjectDirection,'hpnicfCBQoSApplyObjectMainSite':hpnicfCBQoSApplyObjectMainSite,'hpnicfCBQoSApplyObjectSubChannel':hpnicfCBQoSApplyObjectSubChannel,'hpnicfCBQoSApplyObjectSubClass':hpnicfCBQoSApplyObjectSubClass,'hpnicfCBQoSApplyObjectSubClassSec':hpnicfCBQoSApplyObjectSubClassSec,'hpnicfCBQoSIntApplyObjectTable':hpnicfCBQoSIntApplyObjectTable,'hpnicfCBQoSIntApplyObjectEntry':hpnicfCBQoSIntApplyObjectEntry,_A8:hpnicfCBQoSIntApplyObjectIfIndex,'hpnicfCBQoSIntApplyObjectIndex':hpnicfCBQoSIntApplyObjectIndex,'hpnicfCBQoSVlanApplyObjectTable':hpnicfCBQoSVlanApplyObjectTable,'hpnicfCBQoSVlanApplyObjectEntry':hpnicfCBQoSVlanApplyObjectEntry,_A9:hpnicfCBQoSVlanApplyObjectVlanID,'hpnicfCBQoSVlanApplyObjectIndex':hpnicfCBQoSVlanApplyObjectIndex,'hpnicfCBQoSPvcApplyObjectTable':hpnicfCBQoSPvcApplyObjectTable,'hpnicfCBQoSPvcApplyObjectEntry':hpnicfCBQoSPvcApplyObjectEntry,_AA:hpnicfCBQoSPvcApplyObjectIfIndex,_AB:hpnicfCBQoSPvcApplyObjectPvcID,'hpnicfCBQoSPvcApplyObjectIndex':hpnicfCBQoSPvcApplyObjectIndex,'hpnicfCBQoSNestPolicyApplyObjectTable':hpnicfCBQoSNestPolicyApplyObjectTable,'hpnicfCBQoSNestPolicyApplyObjectEntry':hpnicfCBQoSNestPolicyApplyObjectEntry,_AC:hpnicfCBQoSNestPolicyClassIndex,'hpnicfCBQoSNestPolicyApplyObjectIndex':hpnicfCBQoSNestPolicyApplyObjectIndex,'hpnicfCBQoSCpApplyObjectTable':hpnicfCBQoSCpApplyObjectTable,'hpnicfCBQoSCpApplyObjectEntry':hpnicfCBQoSCpApplyObjectEntry,_AD:hpnicfCBQoSCpApplyObjectChassis,_AE:hpnicfCBQoSCpApplyObjectSlot,'hpnicfCBQoSCpApplyObjectIndex':hpnicfCBQoSCpApplyObjectIndex,'hpnicfCBQoSStaticsObjects':hpnicfCBQoSStaticsObjects,'hpnicfCBQoSCbqRunInfoTable':hpnicfCBQoSCbqRunInfoTable,'hpnicfCBQoSCbqRunInfoEntry':hpnicfCBQoSCbqRunInfoEntry,'hpnicfCBQoSCbqQueueSize':hpnicfCBQoSCbqQueueSize,'hpnicfCBQoSCbqDiscard':hpnicfCBQoSCbqDiscard,'hpnicfCBQoSCbqEfQueueSize':hpnicfCBQoSCbqEfQueueSize,'hpnicfCBQoSCbqAfQueueSize':hpnicfCBQoSCbqAfQueueSize,'hpnicfCBQoSCbqBeQueueSize':hpnicfCBQoSCbqBeQueueSize,'hpnicfCBQoSCbqBeActiveQueueNum':hpnicfCBQoSCbqBeActiveQueueNum,'hpnicfCBQoSCbqBeMaxActiveQueueNum':hpnicfCBQoSCbqBeMaxActiveQueueNum,'hpnicfCBQoSCbqBeTotalQueueNum':hpnicfCBQoSCbqBeTotalQueueNum,'hpnicfCBQoSCbqAfAllocatedQueueNum':hpnicfCBQoSCbqAfAllocatedQueueNum,'hpnicfCBQoSClassMatchRunInfoTable':hpnicfCBQoSClassMatchRunInfoTable,'hpnicfCBQoSClassMatchRunInfoEntry':hpnicfCBQoSClassMatchRunInfoEntry,'hpnicfCBQoSClassMatchedPackets':hpnicfCBQoSClassMatchedPackets,'hpnicfCBQoSClassMatchedBytes':hpnicfCBQoSClassMatchedBytes,'hpnicfCBQoSClassFwdPktpps':hpnicfCBQoSClassFwdPktpps,'hpnicfCBQoSClassFwdPktbps':hpnicfCBQoSClassFwdPktbps,'hpnicfCBQoSClassDropPktpps':hpnicfCBQoSClassDropPktpps,'hpnicfCBQoSClassDropPktbps':hpnicfCBQoSClassDropPktbps,'hpnicfCBQoSClassFlowStatInterval':hpnicfCBQoSClassFlowStatInterval,'hpnicfCBQoSClassBehaviorStatus':hpnicfCBQoSClassBehaviorStatus,'hpnicfCBQoSCarRunInfoTable':hpnicfCBQoSCarRunInfoTable,'hpnicfCBQoSCarRunInfoEntry':hpnicfCBQoSCarRunInfoEntry,'hpnicfCBQoSCarGreenPackets':hpnicfCBQoSCarGreenPackets,'hpnicfCBQoSCarGreenBytes':hpnicfCBQoSCarGreenBytes,'hpnicfCBQoSCarRedPackets':hpnicfCBQoSCarRedPackets,'hpnicfCBQoSCarRedBytes':hpnicfCBQoSCarRedBytes,'hpnicfCBQoSCarYellowPackets':hpnicfCBQoSCarYellowPackets,'hpnicfCBQoSCarYellowBytes':hpnicfCBQoSCarYellowBytes,'hpnicfCBQoSGtsRunInfoTable':hpnicfCBQoSGtsRunInfoTable,'hpnicfCBQoSGtsRunInfoEntry':hpnicfCBQoSGtsRunInfoEntry,'hpnicfCBQoSGtsPassedPackets':hpnicfCBQoSGtsPassedPackets,'hpnicfCBQoSGtsPassedBytes':hpnicfCBQoSGtsPassedBytes,'hpnicfCBQoSGtsDiscardedPackets':hpnicfCBQoSGtsDiscardedPackets,'hpnicfCBQoSGtsDiscardedBytes':hpnicfCBQoSGtsDiscardedBytes,'hpnicfCBQoSGtsDelayedPackets':hpnicfCBQoSGtsDelayedPackets,'hpnicfCBQoSGtsDelayedBytes':hpnicfCBQoSGtsDelayedBytes,'hpnicfCBQoSGtsQueueSize':hpnicfCBQoSGtsQueueSize,'hpnicfCBQoSRemarkRunInfoTable':hpnicfCBQoSRemarkRunInfoTable,'hpnicfCBQoSRemarkRunInfoEntry':hpnicfCBQoSRemarkRunInfoEntry,'hpnicfCBQoSRemarkedPackets':hpnicfCBQoSRemarkedPackets,'hpnicfCBQoSQueueRunInfoTable':hpnicfCBQoSQueueRunInfoTable,'hpnicfCBQoSQueueRunInfoEntry':hpnicfCBQoSQueueRunInfoEntry,'hpnicfCBQoSQueueMatchedPackets':hpnicfCBQoSQueueMatchedPackets,'hpnicfCBQoSQueueMatchedBytes':hpnicfCBQoSQueueMatchedBytes,'hpnicfCBQoSQueueEnqueuedPackets':hpnicfCBQoSQueueEnqueuedPackets,'hpnicfCBQoSQueueEnqueuedBytes':hpnicfCBQoSQueueEnqueuedBytes,'hpnicfCBQoSQueueDiscardedPackets':hpnicfCBQoSQueueDiscardedPackets,'hpnicfCBQoSQueueDiscardedBytes':hpnicfCBQoSQueueDiscardedBytes,'hpnicfCBQoSWredRunInfoTable':hpnicfCBQoSWredRunInfoTable,'hpnicfCBQoSWredRunInfoEntry':hpnicfCBQoSWredRunInfoEntry,'hpnicfCBQoSWredRandomDiscardedPackets':hpnicfCBQoSWredRandomDiscardedPackets,'hpnicfCBQoSWredTailDiscardedPackets':hpnicfCBQoSWredTailDiscardedPackets,'hpnicfCBQoSAccountingRunInfoTable':hpnicfCBQoSAccountingRunInfoTable,'hpnicfCBQoSAccountingRunInfoEntry':hpnicfCBQoSAccountingRunInfoEntry,'hpnicfCBQoSAccountingPackets':hpnicfCBQoSAccountingPackets,'hpnicfCBQoSAccountingBytes':hpnicfCBQoSAccountingBytes,'hpnicfCBQoSApplyingStatusObjects':hpnicfCBQoSApplyingStatusObjects,'hpnicfCBQoSApplyingStatus':hpnicfCBQoSApplyingStatus,'hpnicfCBQoSNotifications':hpnicfCBQoSNotifications,'hpnicfCBQoSNotificationsPrefix':hpnicfCBQoSNotificationsPrefix,'hpnicfCBQoSIfPolicyChanged':hpnicfCBQoSIfPolicyChanged,'hpnicfCBQoSVlanPolicyChanged':hpnicfCBQoSVlanPolicyChanged})