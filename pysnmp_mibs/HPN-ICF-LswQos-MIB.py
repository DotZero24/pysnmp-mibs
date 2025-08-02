_AS='hpnicfDscpToDscpMapDscpIndex'
_AR='hpnicfDscpToCosMapDscpIndex'
_AQ='hpnicfDscpToDropPreMapDscpIndex'
_AP='hpnicfDscpToLocalPreMapDscpIndex'
_AO='hpnicfCosToDscpMapCosIndex'
_AN='hpnicfRemarkVlanIDDirection'
_AM='hpnicfRemarkVlanIDVlanID'
_AL='hpnicfRemarkVlanIDIfIndex'
_AK='hpnicfRemarkVlanIDAclIndex'
_AJ='hpnicfPortTrustIfIndex'
_AI='hpnicfMirroringGroupMirrorVlanSeq'
_AH='hpnicfMirroringGroupMirrorMacSeq'
_AG='hpnicfPortWredQueueID'
_AF='hpnicfPortWredIfIndex'
_AE='hpnicfLocalPrecedenceMapLocalPrecedenceIndex'
_AD='hpnicfLocalPrecedenceMapConformLevel'
_AC='hpnicfExpMapExpIndex'
_AB='hpnicfExpMapConformLevel'
_AA='hpnicfDscpMapDscpIndex'
_A9='hpnicfDscpMapConformLevel'
_A8='hpnicfCosToDropPrecedenceMapCosIndex'
_A7='hpnicfCosToLocalPrecedenceMapCosIndex'
_A6='hpnicfWredQueueId'
_A5='hpnicfWredIndex'
_A4='hpnicfDropModeIfIndex'
_A3='hpnicfPortQueueQueueID'
_A2='hpnicfPortQueueIfIndex'
_A1='hpnicfTrafficShapeQueueId'
_A0='hpnicfTrafficShapeIfIndex'
_z='hpnicfFlowtempEnableVlanID'
_y='hpnicfFlowtempEnableIfIndex'
_x='user-defined'
_w='hpnicfFlowtempIndex'
_v='hpnicfMirrorGroupID'
_u='hpnicfRedDirection'
_t='hpnicfRedVlanID'
_s='hpnicfRedIfIndex'
_r='hpnicfRedAclIndex'
_q='hpnicfBandwidthDirection'
_p='hpnicfBandwidthVlanID'
_o='hpnicfBandwidthIfIndex'
_n='hpnicfBandwidthAclIndex'
_m='hpnicfLineRateDirection'
_l='hpnicfLineRateIfIndex'
_k='hpnicfPortMirrorIfIndex'
_j='hpnicfMirrorDirection'
_i='hpnicfMirrorVlanID'
_h='hpnicfMirrorIfIndex'
_g='hpnicfMirrorAclIndex'
_f='hpnicfStatisticDirection'
_e='hpnicfStatisticVlanID'
_d='hpnicfStatisticIfIndex'
_c='hpnicfStatisticAclIndex'
_b='hpnicfRedirectDirection'
_a='hpnicfRedirectVlanID'
_Z='hpnicfRedirectIfIndex'
_Y='hpnicfRedirectAclIndex'
_X='hpnicfPriorityDirection'
_W='hpnicfPriorityVlanID'
_V='hpnicfPriorityIfIndex'
_U='hpnicfPriorityAclIndex'
_T='hpnicfRateLimitDirection'
_S='hpnicfRateLimitVlanID'
_R='hpnicfRateLimitIfIndex'
_Q='hpnicfRateLimitAclIndex'
_P='hpnicfQueueIfIndex'
_O='OctetString'
_N='default'
_M='TruthValue'
_L='reset'
_K='input'
_J='hpnicfMirroringGroupID'
_I='output'
_H='invalid'
_G='not-accessible'
_F='read-only'
_E='read-write'
_D='HPN-ICF-LswQos-MIB'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicflswCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicflswCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_M)
hpnicfLswQosAclMib=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,16))
if mibBuilder.loadTexts:hpnicfLswQosAclMib.setRevisions(('2002-11-19 00:00',))
class HpnicfMirrorOrMonitorType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('port',1),('board',2)))
_HpnicfLswQosMibObject_ObjectIdentity=ObjectIdentity
hpnicfLswQosMibObject=_HpnicfLswQosMibObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2))
class _HpnicfPriorityTrustMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_N,0),('dscp',1),('ipprecedence',2),('cos',3),('localprecedence',4)))
_HpnicfPriorityTrustMode_Type.__name__=_B
_HpnicfPriorityTrustMode_Object=MibScalar
hpnicfPriorityTrustMode=_HpnicfPriorityTrustMode_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,1),_HpnicfPriorityTrustMode_Type())
hpnicfPriorityTrustMode.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPriorityTrustMode.setStatus(_A)
class _HpnicfPortMonitorBothIfIndex_Type(Integer32):defaultValue=0
_HpnicfPortMonitorBothIfIndex_Type.__name__=_B
_HpnicfPortMonitorBothIfIndex_Object=MibScalar
hpnicfPortMonitorBothIfIndex=_HpnicfPortMonitorBothIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,2),_HpnicfPortMonitorBothIfIndex_Type())
hpnicfPortMonitorBothIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPortMonitorBothIfIndex.setStatus(_A)
_HpnicfQueueTable_Object=MibTable
hpnicfQueueTable=_HpnicfQueueTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,3))
if mibBuilder.loadTexts:hpnicfQueueTable.setStatus(_A)
_HpnicfQueueEntry_Object=MibTableRow
hpnicfQueueEntry=_HpnicfQueueEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,3,1))
hpnicfQueueEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:hpnicfQueueEntry.setStatus(_A)
_HpnicfQueueIfIndex_Type=Integer32
_HpnicfQueueIfIndex_Object=MibTableColumn
hpnicfQueueIfIndex=_HpnicfQueueIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,3,1,1),_HpnicfQueueIfIndex_Type())
hpnicfQueueIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfQueueIfIndex.setStatus(_A)
class _HpnicfQueueScheduleMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('sp',1),('wrr',2),('wrr-max-delay',3),('sc-0',4),('sc-1',5),('sc-2',6),('rr',7),('wfq',8),('hq-wrr',9)))
_HpnicfQueueScheduleMode_Type.__name__=_B
_HpnicfQueueScheduleMode_Object=MibTableColumn
hpnicfQueueScheduleMode=_HpnicfQueueScheduleMode_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,3,1,2),_HpnicfQueueScheduleMode_Type())
hpnicfQueueScheduleMode.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfQueueScheduleMode.setStatus(_A)
_HpnicfQueueWeight1_Type=Integer32
_HpnicfQueueWeight1_Object=MibTableColumn
hpnicfQueueWeight1=_HpnicfQueueWeight1_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,3,1,3),_HpnicfQueueWeight1_Type())
hpnicfQueueWeight1.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfQueueWeight1.setStatus(_A)
_HpnicfQueueWeight2_Type=Integer32
_HpnicfQueueWeight2_Object=MibTableColumn
hpnicfQueueWeight2=_HpnicfQueueWeight2_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,3,1,4),_HpnicfQueueWeight2_Type())
hpnicfQueueWeight2.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfQueueWeight2.setStatus(_A)
_HpnicfQueueWeight3_Type=Integer32
_HpnicfQueueWeight3_Object=MibTableColumn
hpnicfQueueWeight3=_HpnicfQueueWeight3_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,3,1,5),_HpnicfQueueWeight3_Type())
hpnicfQueueWeight3.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfQueueWeight3.setStatus(_A)
_HpnicfQueueWeight4_Type=Integer32
_HpnicfQueueWeight4_Object=MibTableColumn
hpnicfQueueWeight4=_HpnicfQueueWeight4_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,3,1,6),_HpnicfQueueWeight4_Type())
hpnicfQueueWeight4.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfQueueWeight4.setStatus(_A)
class _HpnicfQueueMaxDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfQueueMaxDelay_Type.__name__=_B
_HpnicfQueueMaxDelay_Object=MibTableColumn
hpnicfQueueMaxDelay=_HpnicfQueueMaxDelay_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,3,1,7),_HpnicfQueueMaxDelay_Type())
hpnicfQueueMaxDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfQueueMaxDelay.setStatus(_A)
_HpnicfQueueWeight5_Type=Integer32
_HpnicfQueueWeight5_Object=MibTableColumn
hpnicfQueueWeight5=_HpnicfQueueWeight5_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,3,1,8),_HpnicfQueueWeight5_Type())
hpnicfQueueWeight5.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfQueueWeight5.setStatus(_A)
_HpnicfQueueWeight6_Type=Integer32
_HpnicfQueueWeight6_Object=MibTableColumn
hpnicfQueueWeight6=_HpnicfQueueWeight6_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,3,1,9),_HpnicfQueueWeight6_Type())
hpnicfQueueWeight6.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfQueueWeight6.setStatus(_A)
_HpnicfQueueWeight7_Type=Integer32
_HpnicfQueueWeight7_Object=MibTableColumn
hpnicfQueueWeight7=_HpnicfQueueWeight7_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,3,1,10),_HpnicfQueueWeight7_Type())
hpnicfQueueWeight7.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfQueueWeight7.setStatus(_A)
_HpnicfQueueWeight8_Type=Integer32
_HpnicfQueueWeight8_Object=MibTableColumn
hpnicfQueueWeight8=_HpnicfQueueWeight8_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,3,1,11),_HpnicfQueueWeight8_Type())
hpnicfQueueWeight8.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfQueueWeight8.setStatus(_A)
_HpnicfRateLimitTable_Object=MibTable
hpnicfRateLimitTable=_HpnicfRateLimitTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4))
if mibBuilder.loadTexts:hpnicfRateLimitTable.setStatus(_A)
_HpnicfRateLimitEntry_Object=MibTableRow
hpnicfRateLimitEntry=_HpnicfRateLimitEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1))
hpnicfRateLimitEntry.setIndexNames((0,_D,_Q),(0,_D,_R),(0,_D,_S),(0,_D,_T))
if mibBuilder.loadTexts:hpnicfRateLimitEntry.setStatus(_A)
class _HpnicfRateLimitAclIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2999))
_HpnicfRateLimitAclIndex_Type.__name__=_B
_HpnicfRateLimitAclIndex_Object=MibTableColumn
hpnicfRateLimitAclIndex=_HpnicfRateLimitAclIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,1),_HpnicfRateLimitAclIndex_Type())
hpnicfRateLimitAclIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitAclIndex.setStatus(_A)
_HpnicfRateLimitIfIndex_Type=Integer32
_HpnicfRateLimitIfIndex_Object=MibTableColumn
hpnicfRateLimitIfIndex=_HpnicfRateLimitIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,2),_HpnicfRateLimitIfIndex_Type())
hpnicfRateLimitIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitIfIndex.setStatus(_A)
class _HpnicfRateLimitVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpnicfRateLimitVlanID_Type.__name__=_B
_HpnicfRateLimitVlanID_Object=MibTableColumn
hpnicfRateLimitVlanID=_HpnicfRateLimitVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,3),_HpnicfRateLimitVlanID_Type())
hpnicfRateLimitVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitVlanID.setStatus(_A)
class _HpnicfRateLimitDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_K,1),(_I,2)))
_HpnicfRateLimitDirection_Type.__name__=_B
_HpnicfRateLimitDirection_Object=MibTableColumn
hpnicfRateLimitDirection=_HpnicfRateLimitDirection_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,4),_HpnicfRateLimitDirection_Type())
hpnicfRateLimitDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitDirection.setStatus(_A)
class _HpnicfRateLimitUserAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5000,5999),ValueRangeConstraint(10000,12999))
_HpnicfRateLimitUserAclNum_Type.__name__=_B
_HpnicfRateLimitUserAclNum_Object=MibTableColumn
hpnicfRateLimitUserAclNum=_HpnicfRateLimitUserAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,5),_HpnicfRateLimitUserAclNum_Type())
hpnicfRateLimitUserAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitUserAclNum.setStatus(_A)
class _HpnicfRateLimitUserAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfRateLimitUserAclRule_Type.__name__=_B
_HpnicfRateLimitUserAclRule_Object=MibTableColumn
hpnicfRateLimitUserAclRule=_HpnicfRateLimitUserAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,6),_HpnicfRateLimitUserAclRule_Type())
hpnicfRateLimitUserAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitUserAclRule.setStatus(_A)
class _HpnicfRateLimitIpAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999),ValueRangeConstraint(10000,12999))
_HpnicfRateLimitIpAclNum_Type.__name__=_B
_HpnicfRateLimitIpAclNum_Object=MibTableColumn
hpnicfRateLimitIpAclNum=_HpnicfRateLimitIpAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,7),_HpnicfRateLimitIpAclNum_Type())
hpnicfRateLimitIpAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitIpAclNum.setStatus(_A)
class _HpnicfRateLimitIpAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfRateLimitIpAclRule_Type.__name__=_B
_HpnicfRateLimitIpAclRule_Object=MibTableColumn
hpnicfRateLimitIpAclRule=_HpnicfRateLimitIpAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,8),_HpnicfRateLimitIpAclRule_Type())
hpnicfRateLimitIpAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitIpAclRule.setStatus(_A)
class _HpnicfRateLimitLinkAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4000,4999),ValueRangeConstraint(10000,12999))
_HpnicfRateLimitLinkAclNum_Type.__name__=_B
_HpnicfRateLimitLinkAclNum_Object=MibTableColumn
hpnicfRateLimitLinkAclNum=_HpnicfRateLimitLinkAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,9),_HpnicfRateLimitLinkAclNum_Type())
hpnicfRateLimitLinkAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitLinkAclNum.setStatus(_A)
class _HpnicfRateLimitLinkAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfRateLimitLinkAclRule_Type.__name__=_B
_HpnicfRateLimitLinkAclRule_Object=MibTableColumn
hpnicfRateLimitLinkAclRule=_HpnicfRateLimitLinkAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,10),_HpnicfRateLimitLinkAclRule_Type())
hpnicfRateLimitLinkAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitLinkAclRule.setStatus(_A)
_HpnicfRateLimitTargetRateMbps_Type=Integer32
_HpnicfRateLimitTargetRateMbps_Object=MibTableColumn
hpnicfRateLimitTargetRateMbps=_HpnicfRateLimitTargetRateMbps_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,11),_HpnicfRateLimitTargetRateMbps_Type())
hpnicfRateLimitTargetRateMbps.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitTargetRateMbps.setStatus(_A)
_HpnicfRateLimitTargetRateKbps_Type=Integer32
_HpnicfRateLimitTargetRateKbps_Object=MibTableColumn
hpnicfRateLimitTargetRateKbps=_HpnicfRateLimitTargetRateKbps_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,12),_HpnicfRateLimitTargetRateKbps_Type())
hpnicfRateLimitTargetRateKbps.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitTargetRateKbps.setStatus(_A)
class _HpnicfRateLimitPeakRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(64,8388608))
_HpnicfRateLimitPeakRate_Type.__name__=_B
_HpnicfRateLimitPeakRate_Object=MibTableColumn
hpnicfRateLimitPeakRate=_HpnicfRateLimitPeakRate_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,13),_HpnicfRateLimitPeakRate_Type())
hpnicfRateLimitPeakRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitPeakRate.setStatus(_A)
class _HpnicfRateLimitCIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,34120000))
_HpnicfRateLimitCIR_Type.__name__=_B
_HpnicfRateLimitCIR_Object=MibTableColumn
hpnicfRateLimitCIR=_HpnicfRateLimitCIR_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,14),_HpnicfRateLimitCIR_Type())
hpnicfRateLimitCIR.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitCIR.setStatus(_A)
class _HpnicfRateLimitCBS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048575))
_HpnicfRateLimitCBS_Type.__name__=_B
_HpnicfRateLimitCBS_Object=MibTableColumn
hpnicfRateLimitCBS=_HpnicfRateLimitCBS_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,15),_HpnicfRateLimitCBS_Type())
hpnicfRateLimitCBS.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitCBS.setStatus(_A)
class _HpnicfRateLimitEBS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,268435455))
_HpnicfRateLimitEBS_Type.__name__=_B
_HpnicfRateLimitEBS_Object=MibTableColumn
hpnicfRateLimitEBS=_HpnicfRateLimitEBS_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,16),_HpnicfRateLimitEBS_Type())
hpnicfRateLimitEBS.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitEBS.setStatus(_A)
class _HpnicfRateLimitPIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,34120000))
_HpnicfRateLimitPIR_Type.__name__=_B
_HpnicfRateLimitPIR_Object=MibTableColumn
hpnicfRateLimitPIR=_HpnicfRateLimitPIR_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,17),_HpnicfRateLimitPIR_Type())
hpnicfRateLimitPIR.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitPIR.setStatus(_A)
class _HpnicfRateLimitConformLocalPre_Type(Integer32):defaultValue=1
_HpnicfRateLimitConformLocalPre_Type.__name__=_B
_HpnicfRateLimitConformLocalPre_Object=MibTableColumn
hpnicfRateLimitConformLocalPre=_HpnicfRateLimitConformLocalPre_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,18),_HpnicfRateLimitConformLocalPre_Type())
hpnicfRateLimitConformLocalPre.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitConformLocalPre.setStatus(_A)
class _HpnicfRateLimitConformActionType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_H,0),('remark-cos',1),('remark-drop-priority',2),('remark-cos-drop-priority',3),('remark-policed-service',4),('remark-dscp',5)))
_HpnicfRateLimitConformActionType_Type.__name__=_B
_HpnicfRateLimitConformActionType_Object=MibTableColumn
hpnicfRateLimitConformActionType=_HpnicfRateLimitConformActionType_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,19),_HpnicfRateLimitConformActionType_Type())
hpnicfRateLimitConformActionType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitConformActionType.setStatus(_A)
class _HpnicfRateLimitExceedActionType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_H,0),('forward',1),('drop',2),('remarkdscp',3),('exceed-cos',4)))
_HpnicfRateLimitExceedActionType_Type.__name__=_B
_HpnicfRateLimitExceedActionType_Object=MibTableColumn
hpnicfRateLimitExceedActionType=_HpnicfRateLimitExceedActionType_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,20),_HpnicfRateLimitExceedActionType_Type())
hpnicfRateLimitExceedActionType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitExceedActionType.setStatus(_A)
class _HpnicfRateLimitExceedDscp_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HpnicfRateLimitExceedDscp_Type.__name__=_B
_HpnicfRateLimitExceedDscp_Object=MibTableColumn
hpnicfRateLimitExceedDscp=_HpnicfRateLimitExceedDscp_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,21),_HpnicfRateLimitExceedDscp_Type())
hpnicfRateLimitExceedDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitExceedDscp.setStatus(_A)
_HpnicfRateLimitRuntime_Type=TruthValue
_HpnicfRateLimitRuntime_Object=MibTableColumn
hpnicfRateLimitRuntime=_HpnicfRateLimitRuntime_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,22),_HpnicfRateLimitRuntime_Type())
hpnicfRateLimitRuntime.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRateLimitRuntime.setStatus(_A)
_HpnicfRateLimitRowStatus_Type=RowStatus
_HpnicfRateLimitRowStatus_Object=MibTableColumn
hpnicfRateLimitRowStatus=_HpnicfRateLimitRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,23),_HpnicfRateLimitRowStatus_Type())
hpnicfRateLimitRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitRowStatus.setStatus(_A)
class _HpnicfRateLimitExceedCos_Type(Integer32):defaultValue=255
_HpnicfRateLimitExceedCos_Type.__name__=_B
_HpnicfRateLimitExceedCos_Object=MibTableColumn
hpnicfRateLimitExceedCos=_HpnicfRateLimitExceedCos_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,24),_HpnicfRateLimitExceedCos_Type())
hpnicfRateLimitExceedCos.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitExceedCos.setStatus(_A)
class _HpnicfRateLimitConformCos_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpnicfRateLimitConformCos_Type.__name__=_B
_HpnicfRateLimitConformCos_Object=MibTableColumn
hpnicfRateLimitConformCos=_HpnicfRateLimitConformCos_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,25),_HpnicfRateLimitConformCos_Type())
hpnicfRateLimitConformCos.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitConformCos.setStatus(_A)
class _HpnicfRateLimitConformDscp_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HpnicfRateLimitConformDscp_Type.__name__=_B
_HpnicfRateLimitConformDscp_Object=MibTableColumn
hpnicfRateLimitConformDscp=_HpnicfRateLimitConformDscp_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,26),_HpnicfRateLimitConformDscp_Type())
hpnicfRateLimitConformDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitConformDscp.setStatus(_A)
_HpnicfRateLimitMeterStatByteCount_Type=Counter64
_HpnicfRateLimitMeterStatByteCount_Object=MibTableColumn
hpnicfRateLimitMeterStatByteCount=_HpnicfRateLimitMeterStatByteCount_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,27),_HpnicfRateLimitMeterStatByteCount_Type())
hpnicfRateLimitMeterStatByteCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRateLimitMeterStatByteCount.setStatus(_A)
_HpnicfRateLimitMeterStatByteXCount_Type=Counter64
_HpnicfRateLimitMeterStatByteXCount_Object=MibTableColumn
hpnicfRateLimitMeterStatByteXCount=_HpnicfRateLimitMeterStatByteXCount_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,28),_HpnicfRateLimitMeterStatByteXCount_Type())
hpnicfRateLimitMeterStatByteXCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRateLimitMeterStatByteXCount.setStatus(_A)
class _HpnicfRateLimitMeterStatState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('set',1),('unDo',2),(_L,3),('running',4),('notRunning',5)))
_HpnicfRateLimitMeterStatState_Type.__name__=_B
_HpnicfRateLimitMeterStatState_Object=MibTableColumn
hpnicfRateLimitMeterStatState=_HpnicfRateLimitMeterStatState_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,4,1,29),_HpnicfRateLimitMeterStatState_Type())
hpnicfRateLimitMeterStatState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRateLimitMeterStatState.setStatus(_A)
_HpnicfPriorityTable_Object=MibTable
hpnicfPriorityTable=_HpnicfPriorityTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5))
if mibBuilder.loadTexts:hpnicfPriorityTable.setStatus(_A)
_HpnicfPriorityEntry_Object=MibTableRow
hpnicfPriorityEntry=_HpnicfPriorityEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5,1))
hpnicfPriorityEntry.setIndexNames((0,_D,_U),(0,_D,_V),(0,_D,_W),(0,_D,_X))
if mibBuilder.loadTexts:hpnicfPriorityEntry.setStatus(_A)
class _HpnicfPriorityAclIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2999))
_HpnicfPriorityAclIndex_Type.__name__=_B
_HpnicfPriorityAclIndex_Object=MibTableColumn
hpnicfPriorityAclIndex=_HpnicfPriorityAclIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5,1,1),_HpnicfPriorityAclIndex_Type())
hpnicfPriorityAclIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPriorityAclIndex.setStatus(_A)
_HpnicfPriorityIfIndex_Type=Integer32
_HpnicfPriorityIfIndex_Object=MibTableColumn
hpnicfPriorityIfIndex=_HpnicfPriorityIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5,1,2),_HpnicfPriorityIfIndex_Type())
hpnicfPriorityIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPriorityIfIndex.setStatus(_A)
class _HpnicfPriorityVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpnicfPriorityVlanID_Type.__name__=_B
_HpnicfPriorityVlanID_Object=MibTableColumn
hpnicfPriorityVlanID=_HpnicfPriorityVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5,1,3),_HpnicfPriorityVlanID_Type())
hpnicfPriorityVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPriorityVlanID.setStatus(_A)
class _HpnicfPriorityDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_K,1),(_I,2)))
_HpnicfPriorityDirection_Type.__name__=_B
_HpnicfPriorityDirection_Object=MibTableColumn
hpnicfPriorityDirection=_HpnicfPriorityDirection_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5,1,4),_HpnicfPriorityDirection_Type())
hpnicfPriorityDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPriorityDirection.setStatus(_A)
class _HpnicfPriorityUserAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5000,5999),ValueRangeConstraint(10000,12999))
_HpnicfPriorityUserAclNum_Type.__name__=_B
_HpnicfPriorityUserAclNum_Object=MibTableColumn
hpnicfPriorityUserAclNum=_HpnicfPriorityUserAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5,1,5),_HpnicfPriorityUserAclNum_Type())
hpnicfPriorityUserAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPriorityUserAclNum.setStatus(_A)
class _HpnicfPriorityUserAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfPriorityUserAclRule_Type.__name__=_B
_HpnicfPriorityUserAclRule_Object=MibTableColumn
hpnicfPriorityUserAclRule=_HpnicfPriorityUserAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5,1,6),_HpnicfPriorityUserAclRule_Type())
hpnicfPriorityUserAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPriorityUserAclRule.setStatus(_A)
class _HpnicfPriorityIpAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999),ValueRangeConstraint(10000,12999))
_HpnicfPriorityIpAclNum_Type.__name__=_B
_HpnicfPriorityIpAclNum_Object=MibTableColumn
hpnicfPriorityIpAclNum=_HpnicfPriorityIpAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5,1,7),_HpnicfPriorityIpAclNum_Type())
hpnicfPriorityIpAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPriorityIpAclNum.setStatus(_A)
class _HpnicfPriorityIpAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfPriorityIpAclRule_Type.__name__=_B
_HpnicfPriorityIpAclRule_Object=MibTableColumn
hpnicfPriorityIpAclRule=_HpnicfPriorityIpAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5,1,8),_HpnicfPriorityIpAclRule_Type())
hpnicfPriorityIpAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPriorityIpAclRule.setStatus(_A)
class _HpnicfPriorityLinkAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4000,4999),ValueRangeConstraint(10000,12999))
_HpnicfPriorityLinkAclNum_Type.__name__=_B
_HpnicfPriorityLinkAclNum_Object=MibTableColumn
hpnicfPriorityLinkAclNum=_HpnicfPriorityLinkAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5,1,9),_HpnicfPriorityLinkAclNum_Type())
hpnicfPriorityLinkAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPriorityLinkAclNum.setStatus(_A)
class _HpnicfPriorityLinkAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfPriorityLinkAclRule_Type.__name__=_B
_HpnicfPriorityLinkAclRule_Object=MibTableColumn
hpnicfPriorityLinkAclRule=_HpnicfPriorityLinkAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5,1,10),_HpnicfPriorityLinkAclRule_Type())
hpnicfPriorityLinkAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPriorityLinkAclRule.setStatus(_A)
class _HpnicfPriorityDscp_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HpnicfPriorityDscp_Type.__name__=_B
_HpnicfPriorityDscp_Object=MibTableColumn
hpnicfPriorityDscp=_HpnicfPriorityDscp_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5,1,11),_HpnicfPriorityDscp_Type())
hpnicfPriorityDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPriorityDscp.setStatus(_A)
class _HpnicfPriorityIpPre_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpnicfPriorityIpPre_Type.__name__=_B
_HpnicfPriorityIpPre_Object=MibTableColumn
hpnicfPriorityIpPre=_HpnicfPriorityIpPre_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5,1,12),_HpnicfPriorityIpPre_Type())
hpnicfPriorityIpPre.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPriorityIpPre.setStatus(_A)
class _HpnicfPriorityIpPreFromCos_Type(TruthValue):defaultValue=2
_HpnicfPriorityIpPreFromCos_Type.__name__=_M
_HpnicfPriorityIpPreFromCos_Object=MibTableColumn
hpnicfPriorityIpPreFromCos=_HpnicfPriorityIpPreFromCos_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5,1,13),_HpnicfPriorityIpPreFromCos_Type())
hpnicfPriorityIpPreFromCos.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPriorityIpPreFromCos.setStatus(_A)
class _HpnicfPriorityCos_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpnicfPriorityCos_Type.__name__=_B
_HpnicfPriorityCos_Object=MibTableColumn
hpnicfPriorityCos=_HpnicfPriorityCos_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5,1,14),_HpnicfPriorityCos_Type())
hpnicfPriorityCos.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPriorityCos.setStatus(_A)
class _HpnicfPriorityCosFromIpPre_Type(TruthValue):defaultValue=2
_HpnicfPriorityCosFromIpPre_Type.__name__=_M
_HpnicfPriorityCosFromIpPre_Object=MibTableColumn
hpnicfPriorityCosFromIpPre=_HpnicfPriorityCosFromIpPre_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5,1,15),_HpnicfPriorityCosFromIpPre_Type())
hpnicfPriorityCosFromIpPre.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPriorityCosFromIpPre.setStatus(_A)
class _HpnicfPriorityLocalPre_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpnicfPriorityLocalPre_Type.__name__=_B
_HpnicfPriorityLocalPre_Object=MibTableColumn
hpnicfPriorityLocalPre=_HpnicfPriorityLocalPre_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5,1,16),_HpnicfPriorityLocalPre_Type())
hpnicfPriorityLocalPre.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPriorityLocalPre.setStatus(_A)
class _HpnicfPriorityPolicedServiceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_H,0),('auto',1),('trust-dscp',2),('new-dscp',3),('untrusted',4)))
_HpnicfPriorityPolicedServiceType_Type.__name__=_B
_HpnicfPriorityPolicedServiceType_Object=MibTableColumn
hpnicfPriorityPolicedServiceType=_HpnicfPriorityPolicedServiceType_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5,1,17),_HpnicfPriorityPolicedServiceType_Type())
hpnicfPriorityPolicedServiceType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPriorityPolicedServiceType.setStatus(_A)
class _HpnicfPriorityPolicedServiceDscp_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HpnicfPriorityPolicedServiceDscp_Type.__name__=_B
_HpnicfPriorityPolicedServiceDscp_Object=MibTableColumn
hpnicfPriorityPolicedServiceDscp=_HpnicfPriorityPolicedServiceDscp_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5,1,18),_HpnicfPriorityPolicedServiceDscp_Type())
hpnicfPriorityPolicedServiceDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPriorityPolicedServiceDscp.setStatus(_A)
class _HpnicfPriorityPolicedServiceExp_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpnicfPriorityPolicedServiceExp_Type.__name__=_B
_HpnicfPriorityPolicedServiceExp_Object=MibTableColumn
hpnicfPriorityPolicedServiceExp=_HpnicfPriorityPolicedServiceExp_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5,1,19),_HpnicfPriorityPolicedServiceExp_Type())
hpnicfPriorityPolicedServiceExp.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPriorityPolicedServiceExp.setStatus(_A)
class _HpnicfPriorityPolicedServiceCos_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpnicfPriorityPolicedServiceCos_Type.__name__=_B
_HpnicfPriorityPolicedServiceCos_Object=MibTableColumn
hpnicfPriorityPolicedServiceCos=_HpnicfPriorityPolicedServiceCos_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5,1,20),_HpnicfPriorityPolicedServiceCos_Type())
hpnicfPriorityPolicedServiceCos.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPriorityPolicedServiceCos.setStatus(_A)
class _HpnicfPriorityPolicedServiceLoaclPre_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpnicfPriorityPolicedServiceLoaclPre_Type.__name__=_B
_HpnicfPriorityPolicedServiceLoaclPre_Object=MibTableColumn
hpnicfPriorityPolicedServiceLoaclPre=_HpnicfPriorityPolicedServiceLoaclPre_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5,1,21),_HpnicfPriorityPolicedServiceLoaclPre_Type())
hpnicfPriorityPolicedServiceLoaclPre.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPriorityPolicedServiceLoaclPre.setStatus(_A)
class _HpnicfPriorityPolicedServiceDropPriority_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2),ValueRangeConstraint(255,255))
_HpnicfPriorityPolicedServiceDropPriority_Type.__name__=_B
_HpnicfPriorityPolicedServiceDropPriority_Object=MibTableColumn
hpnicfPriorityPolicedServiceDropPriority=_HpnicfPriorityPolicedServiceDropPriority_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5,1,22),_HpnicfPriorityPolicedServiceDropPriority_Type())
hpnicfPriorityPolicedServiceDropPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPriorityPolicedServiceDropPriority.setStatus(_A)
_HpnicfPriorityRuntime_Type=TruthValue
_HpnicfPriorityRuntime_Object=MibTableColumn
hpnicfPriorityRuntime=_HpnicfPriorityRuntime_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5,1,23),_HpnicfPriorityRuntime_Type())
hpnicfPriorityRuntime.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPriorityRuntime.setStatus(_A)
_HpnicfPriorityRowStatus_Type=RowStatus
_HpnicfPriorityRowStatus_Object=MibTableColumn
hpnicfPriorityRowStatus=_HpnicfPriorityRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,5,1,24),_HpnicfPriorityRowStatus_Type())
hpnicfPriorityRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPriorityRowStatus.setStatus(_A)
_HpnicfRedirectTable_Object=MibTable
hpnicfRedirectTable=_HpnicfRedirectTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6))
if mibBuilder.loadTexts:hpnicfRedirectTable.setStatus(_A)
_HpnicfRedirectEntry_Object=MibTableRow
hpnicfRedirectEntry=_HpnicfRedirectEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1))
hpnicfRedirectEntry.setIndexNames((0,_D,_Y),(0,_D,_Z),(0,_D,_a),(0,_D,_b))
if mibBuilder.loadTexts:hpnicfRedirectEntry.setStatus(_A)
class _HpnicfRedirectAclIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2999))
_HpnicfRedirectAclIndex_Type.__name__=_B
_HpnicfRedirectAclIndex_Object=MibTableColumn
hpnicfRedirectAclIndex=_HpnicfRedirectAclIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1,1),_HpnicfRedirectAclIndex_Type())
hpnicfRedirectAclIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedirectAclIndex.setStatus(_A)
_HpnicfRedirectIfIndex_Type=Integer32
_HpnicfRedirectIfIndex_Object=MibTableColumn
hpnicfRedirectIfIndex=_HpnicfRedirectIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1,2),_HpnicfRedirectIfIndex_Type())
hpnicfRedirectIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedirectIfIndex.setStatus(_A)
class _HpnicfRedirectVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpnicfRedirectVlanID_Type.__name__=_B
_HpnicfRedirectVlanID_Object=MibTableColumn
hpnicfRedirectVlanID=_HpnicfRedirectVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1,3),_HpnicfRedirectVlanID_Type())
hpnicfRedirectVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedirectVlanID.setStatus(_A)
class _HpnicfRedirectDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_K,1),(_I,2)))
_HpnicfRedirectDirection_Type.__name__=_B
_HpnicfRedirectDirection_Object=MibTableColumn
hpnicfRedirectDirection=_HpnicfRedirectDirection_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1,4),_HpnicfRedirectDirection_Type())
hpnicfRedirectDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedirectDirection.setStatus(_A)
class _HpnicfRedirectUserAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5000,5999),ValueRangeConstraint(10000,12999))
_HpnicfRedirectUserAclNum_Type.__name__=_B
_HpnicfRedirectUserAclNum_Object=MibTableColumn
hpnicfRedirectUserAclNum=_HpnicfRedirectUserAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1,5),_HpnicfRedirectUserAclNum_Type())
hpnicfRedirectUserAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedirectUserAclNum.setStatus(_A)
class _HpnicfRedirectUserAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfRedirectUserAclRule_Type.__name__=_B
_HpnicfRedirectUserAclRule_Object=MibTableColumn
hpnicfRedirectUserAclRule=_HpnicfRedirectUserAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1,6),_HpnicfRedirectUserAclRule_Type())
hpnicfRedirectUserAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedirectUserAclRule.setStatus(_A)
class _HpnicfRedirectIpAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999),ValueRangeConstraint(10000,12999))
_HpnicfRedirectIpAclNum_Type.__name__=_B
_HpnicfRedirectIpAclNum_Object=MibTableColumn
hpnicfRedirectIpAclNum=_HpnicfRedirectIpAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1,7),_HpnicfRedirectIpAclNum_Type())
hpnicfRedirectIpAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedirectIpAclNum.setStatus(_A)
class _HpnicfRedirectIpAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfRedirectIpAclRule_Type.__name__=_B
_HpnicfRedirectIpAclRule_Object=MibTableColumn
hpnicfRedirectIpAclRule=_HpnicfRedirectIpAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1,8),_HpnicfRedirectIpAclRule_Type())
hpnicfRedirectIpAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedirectIpAclRule.setStatus(_A)
class _HpnicfRedirectLinkAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4000,4999),ValueRangeConstraint(10000,12999))
_HpnicfRedirectLinkAclNum_Type.__name__=_B
_HpnicfRedirectLinkAclNum_Object=MibTableColumn
hpnicfRedirectLinkAclNum=_HpnicfRedirectLinkAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1,9),_HpnicfRedirectLinkAclNum_Type())
hpnicfRedirectLinkAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedirectLinkAclNum.setStatus(_A)
class _HpnicfRedirectLinkAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfRedirectLinkAclRule_Type.__name__=_B
_HpnicfRedirectLinkAclRule_Object=MibTableColumn
hpnicfRedirectLinkAclRule=_HpnicfRedirectLinkAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1,10),_HpnicfRedirectLinkAclRule_Type())
hpnicfRedirectLinkAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedirectLinkAclRule.setStatus(_A)
class _HpnicfRedirectToCpu_Type(TruthValue):defaultValue=2
_HpnicfRedirectToCpu_Type.__name__=_M
_HpnicfRedirectToCpu_Object=MibTableColumn
hpnicfRedirectToCpu=_HpnicfRedirectToCpu_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1,11),_HpnicfRedirectToCpu_Type())
hpnicfRedirectToCpu.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedirectToCpu.setStatus(_A)
_HpnicfRedirectToIfIndex_Type=Integer32
_HpnicfRedirectToIfIndex_Object=MibTableColumn
hpnicfRedirectToIfIndex=_HpnicfRedirectToIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1,12),_HpnicfRedirectToIfIndex_Type())
hpnicfRedirectToIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedirectToIfIndex.setStatus(_A)
_HpnicfRedirectToNextHop1_Type=IpAddress
_HpnicfRedirectToNextHop1_Object=MibTableColumn
hpnicfRedirectToNextHop1=_HpnicfRedirectToNextHop1_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1,13),_HpnicfRedirectToNextHop1_Type())
hpnicfRedirectToNextHop1.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedirectToNextHop1.setStatus(_A)
_HpnicfRedirectToNextHop2_Type=IpAddress
_HpnicfRedirectToNextHop2_Object=MibTableColumn
hpnicfRedirectToNextHop2=_HpnicfRedirectToNextHop2_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1,14),_HpnicfRedirectToNextHop2_Type())
hpnicfRedirectToNextHop2.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedirectToNextHop2.setStatus(_A)
_HpnicfRedirectRuntime_Type=TruthValue
_HpnicfRedirectRuntime_Object=MibTableColumn
hpnicfRedirectRuntime=_HpnicfRedirectRuntime_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1,15),_HpnicfRedirectRuntime_Type())
hpnicfRedirectRuntime.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRedirectRuntime.setStatus(_A)
_HpnicfRedirectRowStatus_Type=RowStatus
_HpnicfRedirectRowStatus_Object=MibTableColumn
hpnicfRedirectRowStatus=_HpnicfRedirectRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1,16),_HpnicfRedirectRowStatus_Type())
hpnicfRedirectRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedirectRowStatus.setStatus(_A)
class _HpnicfRedirectToSlotNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HpnicfRedirectToSlotNo_Type.__name__=_B
_HpnicfRedirectToSlotNo_Object=MibTableColumn
hpnicfRedirectToSlotNo=_HpnicfRedirectToSlotNo_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1,17),_HpnicfRedirectToSlotNo_Type())
hpnicfRedirectToSlotNo.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedirectToSlotNo.setStatus(_A)
class _HpnicfRedirectRemarkedDSCP_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HpnicfRedirectRemarkedDSCP_Type.__name__=_B
_HpnicfRedirectRemarkedDSCP_Object=MibTableColumn
hpnicfRedirectRemarkedDSCP=_HpnicfRedirectRemarkedDSCP_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1,18),_HpnicfRedirectRemarkedDSCP_Type())
hpnicfRedirectRemarkedDSCP.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedirectRemarkedDSCP.setStatus(_A)
class _HpnicfRedirectRemarkedPri_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpnicfRedirectRemarkedPri_Type.__name__=_B
_HpnicfRedirectRemarkedPri_Object=MibTableColumn
hpnicfRedirectRemarkedPri=_HpnicfRedirectRemarkedPri_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1,19),_HpnicfRedirectRemarkedPri_Type())
hpnicfRedirectRemarkedPri.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedirectRemarkedPri.setStatus(_A)
class _HpnicfRedirectRemarkedTos_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15),ValueRangeConstraint(255,255))
_HpnicfRedirectRemarkedTos_Type.__name__=_B
_HpnicfRedirectRemarkedTos_Object=MibTableColumn
hpnicfRedirectRemarkedTos=_HpnicfRedirectRemarkedTos_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1,20),_HpnicfRedirectRemarkedTos_Type())
hpnicfRedirectRemarkedTos.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedirectRemarkedTos.setStatus(_A)
_HpnicfRedirectToNextHop3_Type=IpAddress
_HpnicfRedirectToNextHop3_Object=MibTableColumn
hpnicfRedirectToNextHop3=_HpnicfRedirectToNextHop3_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1,21),_HpnicfRedirectToNextHop3_Type())
hpnicfRedirectToNextHop3.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedirectToNextHop3.setStatus(_A)
class _HpnicfRedirectTargetVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpnicfRedirectTargetVlanID_Type.__name__=_B
_HpnicfRedirectTargetVlanID_Object=MibTableColumn
hpnicfRedirectTargetVlanID=_HpnicfRedirectTargetVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1,22),_HpnicfRedirectTargetVlanID_Type())
hpnicfRedirectTargetVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedirectTargetVlanID.setStatus(_A)
class _HpnicfRedirectMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('strict-priority',1),('load-balance',2)))
_HpnicfRedirectMode_Type.__name__=_B
_HpnicfRedirectMode_Object=MibTableColumn
hpnicfRedirectMode=_HpnicfRedirectMode_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1,23),_HpnicfRedirectMode_Type())
hpnicfRedirectMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedirectMode.setStatus(_A)
class _HpnicfRedirectToNestedVlanID_Type(Integer32):defaultValue=0
_HpnicfRedirectToNestedVlanID_Type.__name__=_B
_HpnicfRedirectToNestedVlanID_Object=MibTableColumn
hpnicfRedirectToNestedVlanID=_HpnicfRedirectToNestedVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1,24),_HpnicfRedirectToNestedVlanID_Type())
hpnicfRedirectToNestedVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedirectToNestedVlanID.setStatus(_A)
class _HpnicfRedirectToModifiedVlanID_Type(Integer32):defaultValue=0
_HpnicfRedirectToModifiedVlanID_Type.__name__=_B
_HpnicfRedirectToModifiedVlanID_Object=MibTableColumn
hpnicfRedirectToModifiedVlanID=_HpnicfRedirectToModifiedVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,6,1,25),_HpnicfRedirectToModifiedVlanID_Type())
hpnicfRedirectToModifiedVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedirectToModifiedVlanID.setStatus(_A)
_HpnicfStatisticTable_Object=MibTable
hpnicfStatisticTable=_HpnicfStatisticTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,7))
if mibBuilder.loadTexts:hpnicfStatisticTable.setStatus(_A)
_HpnicfStatisticEntry_Object=MibTableRow
hpnicfStatisticEntry=_HpnicfStatisticEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,7,1))
hpnicfStatisticEntry.setIndexNames((0,_D,_c),(0,_D,_d),(0,_D,_e),(0,_D,_f))
if mibBuilder.loadTexts:hpnicfStatisticEntry.setStatus(_A)
class _HpnicfStatisticAclIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2999))
_HpnicfStatisticAclIndex_Type.__name__=_B
_HpnicfStatisticAclIndex_Object=MibTableColumn
hpnicfStatisticAclIndex=_HpnicfStatisticAclIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,7,1,1),_HpnicfStatisticAclIndex_Type())
hpnicfStatisticAclIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfStatisticAclIndex.setStatus(_A)
_HpnicfStatisticIfIndex_Type=Integer32
_HpnicfStatisticIfIndex_Object=MibTableColumn
hpnicfStatisticIfIndex=_HpnicfStatisticIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,7,1,2),_HpnicfStatisticIfIndex_Type())
hpnicfStatisticIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfStatisticIfIndex.setStatus(_A)
class _HpnicfStatisticVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpnicfStatisticVlanID_Type.__name__=_B
_HpnicfStatisticVlanID_Object=MibTableColumn
hpnicfStatisticVlanID=_HpnicfStatisticVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,7,1,3),_HpnicfStatisticVlanID_Type())
hpnicfStatisticVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfStatisticVlanID.setStatus(_A)
class _HpnicfStatisticDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_K,1),(_I,2)))
_HpnicfStatisticDirection_Type.__name__=_B
_HpnicfStatisticDirection_Object=MibTableColumn
hpnicfStatisticDirection=_HpnicfStatisticDirection_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,7,1,4),_HpnicfStatisticDirection_Type())
hpnicfStatisticDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfStatisticDirection.setStatus(_A)
class _HpnicfStatisticUserAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5000,5999),ValueRangeConstraint(10000,12999))
_HpnicfStatisticUserAclNum_Type.__name__=_B
_HpnicfStatisticUserAclNum_Object=MibTableColumn
hpnicfStatisticUserAclNum=_HpnicfStatisticUserAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,7,1,5),_HpnicfStatisticUserAclNum_Type())
hpnicfStatisticUserAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfStatisticUserAclNum.setStatus(_A)
class _HpnicfStatisticUserAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfStatisticUserAclRule_Type.__name__=_B
_HpnicfStatisticUserAclRule_Object=MibTableColumn
hpnicfStatisticUserAclRule=_HpnicfStatisticUserAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,7,1,6),_HpnicfStatisticUserAclRule_Type())
hpnicfStatisticUserAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfStatisticUserAclRule.setStatus(_A)
class _HpnicfStatisticIpAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999),ValueRangeConstraint(10000,12999))
_HpnicfStatisticIpAclNum_Type.__name__=_B
_HpnicfStatisticIpAclNum_Object=MibTableColumn
hpnicfStatisticIpAclNum=_HpnicfStatisticIpAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,7,1,7),_HpnicfStatisticIpAclNum_Type())
hpnicfStatisticIpAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfStatisticIpAclNum.setStatus(_A)
class _HpnicfStatisticIpAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfStatisticIpAclRule_Type.__name__=_B
_HpnicfStatisticIpAclRule_Object=MibTableColumn
hpnicfStatisticIpAclRule=_HpnicfStatisticIpAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,7,1,8),_HpnicfStatisticIpAclRule_Type())
hpnicfStatisticIpAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfStatisticIpAclRule.setStatus(_A)
class _HpnicfStatisticLinkAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4000,4999),ValueRangeConstraint(10000,12999))
_HpnicfStatisticLinkAclNum_Type.__name__=_B
_HpnicfStatisticLinkAclNum_Object=MibTableColumn
hpnicfStatisticLinkAclNum=_HpnicfStatisticLinkAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,7,1,9),_HpnicfStatisticLinkAclNum_Type())
hpnicfStatisticLinkAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfStatisticLinkAclNum.setStatus(_A)
class _HpnicfStatisticLinkAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfStatisticLinkAclRule_Type.__name__=_B
_HpnicfStatisticLinkAclRule_Object=MibTableColumn
hpnicfStatisticLinkAclRule=_HpnicfStatisticLinkAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,7,1,10),_HpnicfStatisticLinkAclRule_Type())
hpnicfStatisticLinkAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfStatisticLinkAclRule.setStatus(_A)
_HpnicfStatisticRuntime_Type=TruthValue
_HpnicfStatisticRuntime_Object=MibTableColumn
hpnicfStatisticRuntime=_HpnicfStatisticRuntime_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,7,1,11),_HpnicfStatisticRuntime_Type())
hpnicfStatisticRuntime.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfStatisticRuntime.setStatus(_A)
_HpnicfStatisticPacketCount_Type=Counter64
_HpnicfStatisticPacketCount_Object=MibTableColumn
hpnicfStatisticPacketCount=_HpnicfStatisticPacketCount_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,7,1,12),_HpnicfStatisticPacketCount_Type())
hpnicfStatisticPacketCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfStatisticPacketCount.setStatus(_A)
_HpnicfStatisticByteCount_Type=Counter64
_HpnicfStatisticByteCount_Object=MibTableColumn
hpnicfStatisticByteCount=_HpnicfStatisticByteCount_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,7,1,13),_HpnicfStatisticByteCount_Type())
hpnicfStatisticByteCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfStatisticByteCount.setStatus(_A)
class _HpnicfStatisticCountClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cleared',1),('nouse',2)))
_HpnicfStatisticCountClear_Type.__name__=_B
_HpnicfStatisticCountClear_Object=MibTableColumn
hpnicfStatisticCountClear=_HpnicfStatisticCountClear_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,7,1,14),_HpnicfStatisticCountClear_Type())
hpnicfStatisticCountClear.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfStatisticCountClear.setStatus(_A)
_HpnicfStatisticRowStatus_Type=RowStatus
_HpnicfStatisticRowStatus_Object=MibTableColumn
hpnicfStatisticRowStatus=_HpnicfStatisticRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,7,1,15),_HpnicfStatisticRowStatus_Type())
hpnicfStatisticRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfStatisticRowStatus.setStatus(_A)
_HpnicfStatisticPacketXCount_Type=Counter64
_HpnicfStatisticPacketXCount_Object=MibTableColumn
hpnicfStatisticPacketXCount=_HpnicfStatisticPacketXCount_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,7,1,16),_HpnicfStatisticPacketXCount_Type())
hpnicfStatisticPacketXCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfStatisticPacketXCount.setStatus(_A)
_HpnicfStatisticByteXCount_Type=Counter64
_HpnicfStatisticByteXCount_Object=MibTableColumn
hpnicfStatisticByteXCount=_HpnicfStatisticByteXCount_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,7,1,17),_HpnicfStatisticByteXCount_Type())
hpnicfStatisticByteXCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfStatisticByteXCount.setStatus(_A)
_HpnicfMirrorTable_Object=MibTable
hpnicfMirrorTable=_HpnicfMirrorTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,8))
if mibBuilder.loadTexts:hpnicfMirrorTable.setStatus(_A)
_HpnicfMirrorEntry_Object=MibTableRow
hpnicfMirrorEntry=_HpnicfMirrorEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,8,1))
hpnicfMirrorEntry.setIndexNames((0,_D,_g),(0,_D,_h),(0,_D,_i),(0,_D,_j))
if mibBuilder.loadTexts:hpnicfMirrorEntry.setStatus(_A)
class _HpnicfMirrorAclIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2999))
_HpnicfMirrorAclIndex_Type.__name__=_B
_HpnicfMirrorAclIndex_Object=MibTableColumn
hpnicfMirrorAclIndex=_HpnicfMirrorAclIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,8,1,1),_HpnicfMirrorAclIndex_Type())
hpnicfMirrorAclIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirrorAclIndex.setStatus(_A)
_HpnicfMirrorIfIndex_Type=Integer32
_HpnicfMirrorIfIndex_Object=MibTableColumn
hpnicfMirrorIfIndex=_HpnicfMirrorIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,8,1,2),_HpnicfMirrorIfIndex_Type())
hpnicfMirrorIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirrorIfIndex.setStatus(_A)
class _HpnicfMirrorVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpnicfMirrorVlanID_Type.__name__=_B
_HpnicfMirrorVlanID_Object=MibTableColumn
hpnicfMirrorVlanID=_HpnicfMirrorVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,8,1,3),_HpnicfMirrorVlanID_Type())
hpnicfMirrorVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirrorVlanID.setStatus(_A)
class _HpnicfMirrorDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_K,1),(_I,2)))
_HpnicfMirrorDirection_Type.__name__=_B
_HpnicfMirrorDirection_Object=MibTableColumn
hpnicfMirrorDirection=_HpnicfMirrorDirection_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,8,1,4),_HpnicfMirrorDirection_Type())
hpnicfMirrorDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirrorDirection.setStatus(_A)
class _HpnicfMirrorUserAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5000,5999),ValueRangeConstraint(10000,12999))
_HpnicfMirrorUserAclNum_Type.__name__=_B
_HpnicfMirrorUserAclNum_Object=MibTableColumn
hpnicfMirrorUserAclNum=_HpnicfMirrorUserAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,8,1,5),_HpnicfMirrorUserAclNum_Type())
hpnicfMirrorUserAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirrorUserAclNum.setStatus(_A)
class _HpnicfMirrorUserAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfMirrorUserAclRule_Type.__name__=_B
_HpnicfMirrorUserAclRule_Object=MibTableColumn
hpnicfMirrorUserAclRule=_HpnicfMirrorUserAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,8,1,6),_HpnicfMirrorUserAclRule_Type())
hpnicfMirrorUserAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirrorUserAclRule.setStatus(_A)
class _HpnicfMirrorIpAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999),ValueRangeConstraint(10000,12999))
_HpnicfMirrorIpAclNum_Type.__name__=_B
_HpnicfMirrorIpAclNum_Object=MibTableColumn
hpnicfMirrorIpAclNum=_HpnicfMirrorIpAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,8,1,7),_HpnicfMirrorIpAclNum_Type())
hpnicfMirrorIpAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirrorIpAclNum.setStatus(_A)
class _HpnicfMirrorIpAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfMirrorIpAclRule_Type.__name__=_B
_HpnicfMirrorIpAclRule_Object=MibTableColumn
hpnicfMirrorIpAclRule=_HpnicfMirrorIpAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,8,1,8),_HpnicfMirrorIpAclRule_Type())
hpnicfMirrorIpAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirrorIpAclRule.setStatus(_A)
class _HpnicfMirrorLinkAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4000,4999),ValueRangeConstraint(10000,12999))
_HpnicfMirrorLinkAclNum_Type.__name__=_B
_HpnicfMirrorLinkAclNum_Object=MibTableColumn
hpnicfMirrorLinkAclNum=_HpnicfMirrorLinkAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,8,1,9),_HpnicfMirrorLinkAclNum_Type())
hpnicfMirrorLinkAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirrorLinkAclNum.setStatus(_A)
class _HpnicfMirrorLinkAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfMirrorLinkAclRule_Type.__name__=_B
_HpnicfMirrorLinkAclRule_Object=MibTableColumn
hpnicfMirrorLinkAclRule=_HpnicfMirrorLinkAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,8,1,10),_HpnicfMirrorLinkAclRule_Type())
hpnicfMirrorLinkAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirrorLinkAclRule.setStatus(_A)
_HpnicfMirrorToIfIndex_Type=Integer32
_HpnicfMirrorToIfIndex_Object=MibTableColumn
hpnicfMirrorToIfIndex=_HpnicfMirrorToIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,8,1,11),_HpnicfMirrorToIfIndex_Type())
hpnicfMirrorToIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirrorToIfIndex.setStatus(_A)
_HpnicfMirrorToCpu_Type=TruthValue
_HpnicfMirrorToCpu_Object=MibTableColumn
hpnicfMirrorToCpu=_HpnicfMirrorToCpu_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,8,1,12),_HpnicfMirrorToCpu_Type())
hpnicfMirrorToCpu.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirrorToCpu.setStatus(_A)
_HpnicfMirrorRuntime_Type=TruthValue
_HpnicfMirrorRuntime_Object=MibTableColumn
hpnicfMirrorRuntime=_HpnicfMirrorRuntime_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,8,1,13),_HpnicfMirrorRuntime_Type())
hpnicfMirrorRuntime.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMirrorRuntime.setStatus(_A)
_HpnicfMirrorRowStatus_Type=RowStatus
_HpnicfMirrorRowStatus_Object=MibTableColumn
hpnicfMirrorRowStatus=_HpnicfMirrorRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,8,1,14),_HpnicfMirrorRowStatus_Type())
hpnicfMirrorRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirrorRowStatus.setStatus(_A)
_HpnicfMirrorToGroup_Type=Integer32
_HpnicfMirrorToGroup_Object=MibTableColumn
hpnicfMirrorToGroup=_HpnicfMirrorToGroup_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,8,1,15),_HpnicfMirrorToGroup_Type())
hpnicfMirrorToGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirrorToGroup.setStatus(_A)
_HpnicfPortMirrorTable_Object=MibTable
hpnicfPortMirrorTable=_HpnicfPortMirrorTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,9))
if mibBuilder.loadTexts:hpnicfPortMirrorTable.setStatus(_A)
_HpnicfPortMirrorEntry_Object=MibTableRow
hpnicfPortMirrorEntry=_HpnicfPortMirrorEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,9,1))
hpnicfPortMirrorEntry.setIndexNames((0,_D,_k))
if mibBuilder.loadTexts:hpnicfPortMirrorEntry.setStatus(_A)
_HpnicfPortMirrorIfIndex_Type=Integer32
_HpnicfPortMirrorIfIndex_Object=MibTableColumn
hpnicfPortMirrorIfIndex=_HpnicfPortMirrorIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,9,1,1),_HpnicfPortMirrorIfIndex_Type())
hpnicfPortMirrorIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortMirrorIfIndex.setStatus(_A)
class _HpnicfPortMirrorDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('in',1),('out',2),('both',3)))
_HpnicfPortMirrorDirection_Type.__name__=_B
_HpnicfPortMirrorDirection_Object=MibTableColumn
hpnicfPortMirrorDirection=_HpnicfPortMirrorDirection_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,9,1,2),_HpnicfPortMirrorDirection_Type())
hpnicfPortMirrorDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortMirrorDirection.setStatus(_A)
_HpnicfPortMirrorRowStatus_Type=RowStatus
_HpnicfPortMirrorRowStatus_Object=MibTableColumn
hpnicfPortMirrorRowStatus=_HpnicfPortMirrorRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,9,1,3),_HpnicfPortMirrorRowStatus_Type())
hpnicfPortMirrorRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfPortMirrorRowStatus.setStatus(_A)
_HpnicfLineRateTable_Object=MibTable
hpnicfLineRateTable=_HpnicfLineRateTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,10))
if mibBuilder.loadTexts:hpnicfLineRateTable.setStatus(_A)
_HpnicfLineRateEntry_Object=MibTableRow
hpnicfLineRateEntry=_HpnicfLineRateEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,10,1))
hpnicfLineRateEntry.setIndexNames((0,_D,_l),(0,_D,_m))
if mibBuilder.loadTexts:hpnicfLineRateEntry.setStatus(_A)
_HpnicfLineRateIfIndex_Type=Integer32
_HpnicfLineRateIfIndex_Object=MibTableColumn
hpnicfLineRateIfIndex=_HpnicfLineRateIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,10,1,1),_HpnicfLineRateIfIndex_Type())
hpnicfLineRateIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfLineRateIfIndex.setStatus(_A)
class _HpnicfLineRateDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),('out',2)))
_HpnicfLineRateDirection_Type.__name__=_B
_HpnicfLineRateDirection_Object=MibTableColumn
hpnicfLineRateDirection=_HpnicfLineRateDirection_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,10,1,2),_HpnicfLineRateDirection_Type())
hpnicfLineRateDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfLineRateDirection.setStatus(_A)
_HpnicfLineRateValue_Type=Integer32
_HpnicfLineRateValue_Object=MibTableColumn
hpnicfLineRateValue=_HpnicfLineRateValue_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,10,1,3),_HpnicfLineRateValue_Type())
hpnicfLineRateValue.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfLineRateValue.setStatus(_A)
_HpnicfLineRateRowStatus_Type=RowStatus
_HpnicfLineRateRowStatus_Object=MibTableColumn
hpnicfLineRateRowStatus=_HpnicfLineRateRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,10,1,4),_HpnicfLineRateRowStatus_Type())
hpnicfLineRateRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfLineRateRowStatus.setStatus(_A)
_HpnicfBandwidthTable_Object=MibTable
hpnicfBandwidthTable=_HpnicfBandwidthTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,11))
if mibBuilder.loadTexts:hpnicfBandwidthTable.setStatus(_A)
_HpnicfBandwidthEntry_Object=MibTableRow
hpnicfBandwidthEntry=_HpnicfBandwidthEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,11,1))
hpnicfBandwidthEntry.setIndexNames((0,_D,_n),(0,_D,_o),(0,_D,_p),(0,_D,_q))
if mibBuilder.loadTexts:hpnicfBandwidthEntry.setStatus(_A)
class _HpnicfBandwidthAclIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2999))
_HpnicfBandwidthAclIndex_Type.__name__=_B
_HpnicfBandwidthAclIndex_Object=MibTableColumn
hpnicfBandwidthAclIndex=_HpnicfBandwidthAclIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,11,1,1),_HpnicfBandwidthAclIndex_Type())
hpnicfBandwidthAclIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfBandwidthAclIndex.setStatus(_A)
_HpnicfBandwidthIfIndex_Type=Integer32
_HpnicfBandwidthIfIndex_Object=MibTableColumn
hpnicfBandwidthIfIndex=_HpnicfBandwidthIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,11,1,2),_HpnicfBandwidthIfIndex_Type())
hpnicfBandwidthIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfBandwidthIfIndex.setStatus(_A)
class _HpnicfBandwidthVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpnicfBandwidthVlanID_Type.__name__=_B
_HpnicfBandwidthVlanID_Object=MibTableColumn
hpnicfBandwidthVlanID=_HpnicfBandwidthVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,11,1,3),_HpnicfBandwidthVlanID_Type())
hpnicfBandwidthVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfBandwidthVlanID.setStatus(_A)
class _HpnicfBandwidthDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*((_H,0),(_I,2)))
_HpnicfBandwidthDirection_Type.__name__=_B
_HpnicfBandwidthDirection_Object=MibTableColumn
hpnicfBandwidthDirection=_HpnicfBandwidthDirection_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,11,1,4),_HpnicfBandwidthDirection_Type())
hpnicfBandwidthDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfBandwidthDirection.setStatus(_A)
class _HpnicfBandwidthIpAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999),ValueRangeConstraint(10000,12999))
_HpnicfBandwidthIpAclNum_Type.__name__=_B
_HpnicfBandwidthIpAclNum_Object=MibTableColumn
hpnicfBandwidthIpAclNum=_HpnicfBandwidthIpAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,11,1,5),_HpnicfBandwidthIpAclNum_Type())
hpnicfBandwidthIpAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfBandwidthIpAclNum.setStatus(_A)
class _HpnicfBandwidthIpAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfBandwidthIpAclRule_Type.__name__=_B
_HpnicfBandwidthIpAclRule_Object=MibTableColumn
hpnicfBandwidthIpAclRule=_HpnicfBandwidthIpAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,11,1,6),_HpnicfBandwidthIpAclRule_Type())
hpnicfBandwidthIpAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfBandwidthIpAclRule.setStatus(_A)
class _HpnicfBandwidthLinkAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4000,4999),ValueRangeConstraint(10000,12999))
_HpnicfBandwidthLinkAclNum_Type.__name__=_B
_HpnicfBandwidthLinkAclNum_Object=MibTableColumn
hpnicfBandwidthLinkAclNum=_HpnicfBandwidthLinkAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,11,1,7),_HpnicfBandwidthLinkAclNum_Type())
hpnicfBandwidthLinkAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfBandwidthLinkAclNum.setStatus(_A)
class _HpnicfBandwidthLinkAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfBandwidthLinkAclRule_Type.__name__=_B
_HpnicfBandwidthLinkAclRule_Object=MibTableColumn
hpnicfBandwidthLinkAclRule=_HpnicfBandwidthLinkAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,11,1,8),_HpnicfBandwidthLinkAclRule_Type())
hpnicfBandwidthLinkAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfBandwidthLinkAclRule.setStatus(_A)
class _HpnicfBandwidthMinGuaranteedWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8388608))
_HpnicfBandwidthMinGuaranteedWidth_Type.__name__=_B
_HpnicfBandwidthMinGuaranteedWidth_Object=MibTableColumn
hpnicfBandwidthMinGuaranteedWidth=_HpnicfBandwidthMinGuaranteedWidth_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,11,1,9),_HpnicfBandwidthMinGuaranteedWidth_Type())
hpnicfBandwidthMinGuaranteedWidth.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfBandwidthMinGuaranteedWidth.setStatus(_A)
class _HpnicfBandwidthMaxGuaranteedWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8388608))
_HpnicfBandwidthMaxGuaranteedWidth_Type.__name__=_B
_HpnicfBandwidthMaxGuaranteedWidth_Object=MibTableColumn
hpnicfBandwidthMaxGuaranteedWidth=_HpnicfBandwidthMaxGuaranteedWidth_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,11,1,10),_HpnicfBandwidthMaxGuaranteedWidth_Type())
hpnicfBandwidthMaxGuaranteedWidth.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfBandwidthMaxGuaranteedWidth.setStatus(_A)
class _HpnicfBandwidthWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfBandwidthWeight_Type.__name__=_B
_HpnicfBandwidthWeight_Object=MibTableColumn
hpnicfBandwidthWeight=_HpnicfBandwidthWeight_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,11,1,11),_HpnicfBandwidthWeight_Type())
hpnicfBandwidthWeight.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfBandwidthWeight.setStatus(_A)
_HpnicfBandwidthRuntime_Type=TruthValue
_HpnicfBandwidthRuntime_Object=MibTableColumn
hpnicfBandwidthRuntime=_HpnicfBandwidthRuntime_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,11,1,12),_HpnicfBandwidthRuntime_Type())
hpnicfBandwidthRuntime.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfBandwidthRuntime.setStatus(_A)
_HpnicfBandwidthRowStatus_Type=RowStatus
_HpnicfBandwidthRowStatus_Object=MibTableColumn
hpnicfBandwidthRowStatus=_HpnicfBandwidthRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,11,1,13),_HpnicfBandwidthRowStatus_Type())
hpnicfBandwidthRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfBandwidthRowStatus.setStatus(_A)
_HpnicfRedTable_Object=MibTable
hpnicfRedTable=_HpnicfRedTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,12))
if mibBuilder.loadTexts:hpnicfRedTable.setStatus(_A)
_HpnicfRedEntry_Object=MibTableRow
hpnicfRedEntry=_HpnicfRedEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,12,1))
hpnicfRedEntry.setIndexNames((0,_D,_r),(0,_D,_s),(0,_D,_t),(0,_D,_u))
if mibBuilder.loadTexts:hpnicfRedEntry.setStatus(_A)
class _HpnicfRedAclIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2999))
_HpnicfRedAclIndex_Type.__name__=_B
_HpnicfRedAclIndex_Object=MibTableColumn
hpnicfRedAclIndex=_HpnicfRedAclIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,12,1,1),_HpnicfRedAclIndex_Type())
hpnicfRedAclIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedAclIndex.setStatus(_A)
_HpnicfRedIfIndex_Type=Integer32
_HpnicfRedIfIndex_Object=MibTableColumn
hpnicfRedIfIndex=_HpnicfRedIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,12,1,2),_HpnicfRedIfIndex_Type())
hpnicfRedIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedIfIndex.setStatus(_A)
class _HpnicfRedVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpnicfRedVlanID_Type.__name__=_B
_HpnicfRedVlanID_Object=MibTableColumn
hpnicfRedVlanID=_HpnicfRedVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,12,1,3),_HpnicfRedVlanID_Type())
hpnicfRedVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedVlanID.setStatus(_A)
class _HpnicfRedDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*((_H,0),(_I,2)))
_HpnicfRedDirection_Type.__name__=_B
_HpnicfRedDirection_Object=MibTableColumn
hpnicfRedDirection=_HpnicfRedDirection_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,12,1,4),_HpnicfRedDirection_Type())
hpnicfRedDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedDirection.setStatus(_A)
class _HpnicfRedIpAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999),ValueRangeConstraint(10000,12999))
_HpnicfRedIpAclNum_Type.__name__=_B
_HpnicfRedIpAclNum_Object=MibTableColumn
hpnicfRedIpAclNum=_HpnicfRedIpAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,12,1,5),_HpnicfRedIpAclNum_Type())
hpnicfRedIpAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedIpAclNum.setStatus(_A)
class _HpnicfRedIpAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfRedIpAclRule_Type.__name__=_B
_HpnicfRedIpAclRule_Object=MibTableColumn
hpnicfRedIpAclRule=_HpnicfRedIpAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,12,1,6),_HpnicfRedIpAclRule_Type())
hpnicfRedIpAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedIpAclRule.setStatus(_A)
class _HpnicfRedLinkAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4000,4999),ValueRangeConstraint(10000,12999))
_HpnicfRedLinkAclNum_Type.__name__=_B
_HpnicfRedLinkAclNum_Object=MibTableColumn
hpnicfRedLinkAclNum=_HpnicfRedLinkAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,12,1,7),_HpnicfRedLinkAclNum_Type())
hpnicfRedLinkAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedLinkAclNum.setStatus(_A)
class _HpnicfRedLinkAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfRedLinkAclRule_Type.__name__=_B
_HpnicfRedLinkAclRule_Object=MibTableColumn
hpnicfRedLinkAclRule=_HpnicfRedLinkAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,12,1,8),_HpnicfRedLinkAclRule_Type())
hpnicfRedLinkAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRedLinkAclRule.setStatus(_A)
class _HpnicfRedStartQueueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,262128))
_HpnicfRedStartQueueLen_Type.__name__=_B
_HpnicfRedStartQueueLen_Object=MibTableColumn
hpnicfRedStartQueueLen=_HpnicfRedStartQueueLen_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,12,1,9),_HpnicfRedStartQueueLen_Type())
hpnicfRedStartQueueLen.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRedStartQueueLen.setStatus(_A)
class _HpnicfRedStopQueueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,262128))
_HpnicfRedStopQueueLen_Type.__name__=_B
_HpnicfRedStopQueueLen_Object=MibTableColumn
hpnicfRedStopQueueLen=_HpnicfRedStopQueueLen_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,12,1,10),_HpnicfRedStopQueueLen_Type())
hpnicfRedStopQueueLen.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRedStopQueueLen.setStatus(_A)
class _HpnicfRedProbability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfRedProbability_Type.__name__=_B
_HpnicfRedProbability_Object=MibTableColumn
hpnicfRedProbability=_HpnicfRedProbability_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,12,1,11),_HpnicfRedProbability_Type())
hpnicfRedProbability.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRedProbability.setStatus(_A)
_HpnicfRedRuntime_Type=TruthValue
_HpnicfRedRuntime_Object=MibTableColumn
hpnicfRedRuntime=_HpnicfRedRuntime_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,12,1,12),_HpnicfRedRuntime_Type())
hpnicfRedRuntime.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRedRuntime.setStatus(_A)
_HpnicfRedRowStatus_Type=RowStatus
_HpnicfRedRowStatus_Object=MibTableColumn
hpnicfRedRowStatus=_HpnicfRedRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,12,1,13),_HpnicfRedRowStatus_Type())
hpnicfRedRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRedRowStatus.setStatus(_A)
_HpnicfMirrorGroupTable_Object=MibTable
hpnicfMirrorGroupTable=_HpnicfMirrorGroupTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,13))
if mibBuilder.loadTexts:hpnicfMirrorGroupTable.setStatus(_A)
_HpnicfMirrorGroupEntry_Object=MibTableRow
hpnicfMirrorGroupEntry=_HpnicfMirrorGroupEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,13,1))
hpnicfMirrorGroupEntry.setIndexNames((0,_D,_v))
if mibBuilder.loadTexts:hpnicfMirrorGroupEntry.setStatus(_A)
class _HpnicfMirrorGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_HpnicfMirrorGroupID_Type.__name__=_B
_HpnicfMirrorGroupID_Object=MibTableColumn
hpnicfMirrorGroupID=_HpnicfMirrorGroupID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,13,1,1),_HpnicfMirrorGroupID_Type())
hpnicfMirrorGroupID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMirrorGroupID.setStatus(_A)
class _HpnicfMirrorGroupDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_I,2)))
_HpnicfMirrorGroupDirection_Type.__name__=_B
_HpnicfMirrorGroupDirection_Object=MibTableColumn
hpnicfMirrorGroupDirection=_HpnicfMirrorGroupDirection_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,13,1,2),_HpnicfMirrorGroupDirection_Type())
hpnicfMirrorGroupDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMirrorGroupDirection.setStatus(_A)
class _HpnicfMirrorGroupMirrorIfIndexList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,257))
_HpnicfMirrorGroupMirrorIfIndexList_Type.__name__=_O
_HpnicfMirrorGroupMirrorIfIndexList_Object=MibTableColumn
hpnicfMirrorGroupMirrorIfIndexList=_HpnicfMirrorGroupMirrorIfIndexList_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,13,1,3),_HpnicfMirrorGroupMirrorIfIndexList_Type())
hpnicfMirrorGroupMirrorIfIndexList.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMirrorGroupMirrorIfIndexList.setStatus(_A)
_HpnicfMirrorGroupMonitorIfIndex_Type=Integer32
_HpnicfMirrorGroupMonitorIfIndex_Object=MibTableColumn
hpnicfMirrorGroupMonitorIfIndex=_HpnicfMirrorGroupMonitorIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,13,1,4),_HpnicfMirrorGroupMonitorIfIndex_Type())
hpnicfMirrorGroupMonitorIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMirrorGroupMonitorIfIndex.setStatus(_A)
_HpnicfMirrorGroupRowStatus_Type=RowStatus
_HpnicfMirrorGroupRowStatus_Object=MibTableColumn
hpnicfMirrorGroupRowStatus=_HpnicfMirrorGroupRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,13,1,5),_HpnicfMirrorGroupRowStatus_Type())
hpnicfMirrorGroupRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMirrorGroupRowStatus.setStatus(_A)
_HpnicfFlowtempTable_Object=MibTable
hpnicfFlowtempTable=_HpnicfFlowtempTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14))
if mibBuilder.loadTexts:hpnicfFlowtempTable.setStatus(_A)
_HpnicfFlowtempEntry_Object=MibTableRow
hpnicfFlowtempEntry=_HpnicfFlowtempEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14,1))
hpnicfFlowtempEntry.setIndexNames((0,_D,_w))
if mibBuilder.loadTexts:hpnicfFlowtempEntry.setStatus(_A)
class _HpnicfFlowtempIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_x,2)))
_HpnicfFlowtempIndex_Type.__name__=_B
_HpnicfFlowtempIndex_Object=MibTableColumn
hpnicfFlowtempIndex=_HpnicfFlowtempIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14,1,1),_HpnicfFlowtempIndex_Type())
hpnicfFlowtempIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfFlowtempIndex.setStatus(_A)
_HpnicfFlowtempIpProtocol_Type=TruthValue
_HpnicfFlowtempIpProtocol_Object=MibTableColumn
hpnicfFlowtempIpProtocol=_HpnicfFlowtempIpProtocol_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14,1,2),_HpnicfFlowtempIpProtocol_Type())
hpnicfFlowtempIpProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlowtempIpProtocol.setStatus(_A)
_HpnicfFlowtempTcpFlag_Type=TruthValue
_HpnicfFlowtempTcpFlag_Object=MibTableColumn
hpnicfFlowtempTcpFlag=_HpnicfFlowtempTcpFlag_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14,1,3),_HpnicfFlowtempTcpFlag_Type())
hpnicfFlowtempTcpFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlowtempTcpFlag.setStatus(_A)
_HpnicfFlowtempSPort_Type=TruthValue
_HpnicfFlowtempSPort_Object=MibTableColumn
hpnicfFlowtempSPort=_HpnicfFlowtempSPort_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14,1,4),_HpnicfFlowtempSPort_Type())
hpnicfFlowtempSPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlowtempSPort.setStatus(_A)
_HpnicfFlowtempDPort_Type=TruthValue
_HpnicfFlowtempDPort_Object=MibTableColumn
hpnicfFlowtempDPort=_HpnicfFlowtempDPort_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14,1,5),_HpnicfFlowtempDPort_Type())
hpnicfFlowtempDPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlowtempDPort.setStatus(_A)
_HpnicfFlowtempIcmpType_Type=TruthValue
_HpnicfFlowtempIcmpType_Object=MibTableColumn
hpnicfFlowtempIcmpType=_HpnicfFlowtempIcmpType_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14,1,6),_HpnicfFlowtempIcmpType_Type())
hpnicfFlowtempIcmpType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlowtempIcmpType.setStatus(_A)
_HpnicfFlowtempIcmpCode_Type=TruthValue
_HpnicfFlowtempIcmpCode_Object=MibTableColumn
hpnicfFlowtempIcmpCode=_HpnicfFlowtempIcmpCode_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14,1,7),_HpnicfFlowtempIcmpCode_Type())
hpnicfFlowtempIcmpCode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlowtempIcmpCode.setStatus(_A)
_HpnicfFlowtempFragment_Type=TruthValue
_HpnicfFlowtempFragment_Object=MibTableColumn
hpnicfFlowtempFragment=_HpnicfFlowtempFragment_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14,1,8),_HpnicfFlowtempFragment_Type())
hpnicfFlowtempFragment.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlowtempFragment.setStatus(_A)
_HpnicfFlowtempDscp_Type=TruthValue
_HpnicfFlowtempDscp_Object=MibTableColumn
hpnicfFlowtempDscp=_HpnicfFlowtempDscp_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14,1,9),_HpnicfFlowtempDscp_Type())
hpnicfFlowtempDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlowtempDscp.setStatus(_A)
_HpnicfFlowtempIpPre_Type=TruthValue
_HpnicfFlowtempIpPre_Object=MibTableColumn
hpnicfFlowtempIpPre=_HpnicfFlowtempIpPre_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14,1,10),_HpnicfFlowtempIpPre_Type())
hpnicfFlowtempIpPre.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlowtempIpPre.setStatus(_A)
_HpnicfFlowtempTos_Type=TruthValue
_HpnicfFlowtempTos_Object=MibTableColumn
hpnicfFlowtempTos=_HpnicfFlowtempTos_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14,1,11),_HpnicfFlowtempTos_Type())
hpnicfFlowtempTos.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlowtempTos.setStatus(_A)
_HpnicfFlowtempSIp_Type=TruthValue
_HpnicfFlowtempSIp_Object=MibTableColumn
hpnicfFlowtempSIp=_HpnicfFlowtempSIp_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14,1,12),_HpnicfFlowtempSIp_Type())
hpnicfFlowtempSIp.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlowtempSIp.setStatus(_A)
_HpnicfFlowtempSIpMask_Type=IpAddress
_HpnicfFlowtempSIpMask_Object=MibTableColumn
hpnicfFlowtempSIpMask=_HpnicfFlowtempSIpMask_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14,1,13),_HpnicfFlowtempSIpMask_Type())
hpnicfFlowtempSIpMask.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlowtempSIpMask.setStatus(_A)
_HpnicfFlowtempDIp_Type=TruthValue
_HpnicfFlowtempDIp_Object=MibTableColumn
hpnicfFlowtempDIp=_HpnicfFlowtempDIp_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14,1,14),_HpnicfFlowtempDIp_Type())
hpnicfFlowtempDIp.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlowtempDIp.setStatus(_A)
_HpnicfFlowtempDIpMask_Type=IpAddress
_HpnicfFlowtempDIpMask_Object=MibTableColumn
hpnicfFlowtempDIpMask=_HpnicfFlowtempDIpMask_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14,1,15),_HpnicfFlowtempDIpMask_Type())
hpnicfFlowtempDIpMask.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlowtempDIpMask.setStatus(_A)
_HpnicfFlowtempEthProtocol_Type=TruthValue
_HpnicfFlowtempEthProtocol_Object=MibTableColumn
hpnicfFlowtempEthProtocol=_HpnicfFlowtempEthProtocol_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14,1,16),_HpnicfFlowtempEthProtocol_Type())
hpnicfFlowtempEthProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlowtempEthProtocol.setStatus(_A)
_HpnicfFlowtempSMac_Type=TruthValue
_HpnicfFlowtempSMac_Object=MibTableColumn
hpnicfFlowtempSMac=_HpnicfFlowtempSMac_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14,1,17),_HpnicfFlowtempSMac_Type())
hpnicfFlowtempSMac.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlowtempSMac.setStatus(_A)
_HpnicfFlowtempSMacMask_Type=MacAddress
_HpnicfFlowtempSMacMask_Object=MibTableColumn
hpnicfFlowtempSMacMask=_HpnicfFlowtempSMacMask_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14,1,18),_HpnicfFlowtempSMacMask_Type())
hpnicfFlowtempSMacMask.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlowtempSMacMask.setStatus(_A)
_HpnicfFlowtempDMac_Type=TruthValue
_HpnicfFlowtempDMac_Object=MibTableColumn
hpnicfFlowtempDMac=_HpnicfFlowtempDMac_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14,1,19),_HpnicfFlowtempDMac_Type())
hpnicfFlowtempDMac.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlowtempDMac.setStatus(_A)
_HpnicfFlowtempDMacMask_Type=MacAddress
_HpnicfFlowtempDMacMask_Object=MibTableColumn
hpnicfFlowtempDMacMask=_HpnicfFlowtempDMacMask_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14,1,20),_HpnicfFlowtempDMacMask_Type())
hpnicfFlowtempDMacMask.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlowtempDMacMask.setStatus(_A)
_HpnicfFlowtempVpn_Type=TruthValue
_HpnicfFlowtempVpn_Object=MibTableColumn
hpnicfFlowtempVpn=_HpnicfFlowtempVpn_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14,1,21),_HpnicfFlowtempVpn_Type())
hpnicfFlowtempVpn.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlowtempVpn.setStatus(_A)
_HpnicfFlowtempRowStatus_Type=RowStatus
_HpnicfFlowtempRowStatus_Object=MibTableColumn
hpnicfFlowtempRowStatus=_HpnicfFlowtempRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14,1,22),_HpnicfFlowtempRowStatus_Type())
hpnicfFlowtempRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlowtempRowStatus.setStatus(_A)
_HpnicfFlowtempVlanId_Type=TruthValue
_HpnicfFlowtempVlanId_Object=MibTableColumn
hpnicfFlowtempVlanId=_HpnicfFlowtempVlanId_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14,1,23),_HpnicfFlowtempVlanId_Type())
hpnicfFlowtempVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlowtempVlanId.setStatus(_A)
_HpnicfFlowtempCos_Type=TruthValue
_HpnicfFlowtempCos_Object=MibTableColumn
hpnicfFlowtempCos=_HpnicfFlowtempCos_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,14,1,24),_HpnicfFlowtempCos_Type())
hpnicfFlowtempCos.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlowtempCos.setStatus(_A)
_HpnicfFlowtempEnableTable_Object=MibTable
hpnicfFlowtempEnableTable=_HpnicfFlowtempEnableTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,15))
if mibBuilder.loadTexts:hpnicfFlowtempEnableTable.setStatus(_A)
_HpnicfFlowtempEnableEntry_Object=MibTableRow
hpnicfFlowtempEnableEntry=_HpnicfFlowtempEnableEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,15,1))
hpnicfFlowtempEnableEntry.setIndexNames((0,_D,_y),(0,_D,_z))
if mibBuilder.loadTexts:hpnicfFlowtempEnableEntry.setStatus(_A)
_HpnicfFlowtempEnableIfIndex_Type=Integer32
_HpnicfFlowtempEnableIfIndex_Object=MibTableColumn
hpnicfFlowtempEnableIfIndex=_HpnicfFlowtempEnableIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,15,1,1),_HpnicfFlowtempEnableIfIndex_Type())
hpnicfFlowtempEnableIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlowtempEnableIfIndex.setStatus(_A)
class _HpnicfFlowtempEnableVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpnicfFlowtempEnableVlanID_Type.__name__=_B
_HpnicfFlowtempEnableVlanID_Object=MibTableColumn
hpnicfFlowtempEnableVlanID=_HpnicfFlowtempEnableVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,15,1,2),_HpnicfFlowtempEnableVlanID_Type())
hpnicfFlowtempEnableVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfFlowtempEnableVlanID.setStatus(_A)
class _HpnicfFlowtempEnableFlowtempIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_x,2)))
_HpnicfFlowtempEnableFlowtempIndex_Type.__name__=_B
_HpnicfFlowtempEnableFlowtempIndex_Object=MibTableColumn
hpnicfFlowtempEnableFlowtempIndex=_HpnicfFlowtempEnableFlowtempIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,15,1,3),_HpnicfFlowtempEnableFlowtempIndex_Type())
hpnicfFlowtempEnableFlowtempIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfFlowtempEnableFlowtempIndex.setStatus(_A)
_HpnicfTrafficShapeTable_Object=MibTable
hpnicfTrafficShapeTable=_HpnicfTrafficShapeTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,16))
if mibBuilder.loadTexts:hpnicfTrafficShapeTable.setStatus(_A)
_HpnicfTrafficShapeEntry_Object=MibTableRow
hpnicfTrafficShapeEntry=_HpnicfTrafficShapeEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,16,1))
hpnicfTrafficShapeEntry.setIndexNames((0,_D,_A0),(0,_D,_A1))
if mibBuilder.loadTexts:hpnicfTrafficShapeEntry.setStatus(_A)
_HpnicfTrafficShapeIfIndex_Type=Integer32
_HpnicfTrafficShapeIfIndex_Object=MibTableColumn
hpnicfTrafficShapeIfIndex=_HpnicfTrafficShapeIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,16,1,1),_HpnicfTrafficShapeIfIndex_Type())
hpnicfTrafficShapeIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTrafficShapeIfIndex.setStatus(_A)
class _HpnicfTrafficShapeQueueId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpnicfTrafficShapeQueueId_Type.__name__=_B
_HpnicfTrafficShapeQueueId_Object=MibTableColumn
hpnicfTrafficShapeQueueId=_HpnicfTrafficShapeQueueId_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,16,1,2),_HpnicfTrafficShapeQueueId_Type())
hpnicfTrafficShapeQueueId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTrafficShapeQueueId.setStatus(_A)
_HpnicfTrafficShapeMaxRate_Type=Integer32
_HpnicfTrafficShapeMaxRate_Object=MibTableColumn
hpnicfTrafficShapeMaxRate=_HpnicfTrafficShapeMaxRate_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,16,1,3),_HpnicfTrafficShapeMaxRate_Type())
hpnicfTrafficShapeMaxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTrafficShapeMaxRate.setStatus(_A)
_HpnicfTrafficShapeBurstSize_Type=Integer32
_HpnicfTrafficShapeBurstSize_Object=MibTableColumn
hpnicfTrafficShapeBurstSize=_HpnicfTrafficShapeBurstSize_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,16,1,4),_HpnicfTrafficShapeBurstSize_Type())
hpnicfTrafficShapeBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTrafficShapeBurstSize.setStatus(_A)
class _HpnicfTrafficShapeBufferLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(16,8000))
_HpnicfTrafficShapeBufferLimit_Type.__name__=_B
_HpnicfTrafficShapeBufferLimit_Object=MibTableColumn
hpnicfTrafficShapeBufferLimit=_HpnicfTrafficShapeBufferLimit_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,16,1,5),_HpnicfTrafficShapeBufferLimit_Type())
hpnicfTrafficShapeBufferLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTrafficShapeBufferLimit.setStatus(_A)
_HpnicfTrafficShapeRowStatus_Type=RowStatus
_HpnicfTrafficShapeRowStatus_Object=MibTableColumn
hpnicfTrafficShapeRowStatus=_HpnicfTrafficShapeRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,16,1,6),_HpnicfTrafficShapeRowStatus_Type())
hpnicfTrafficShapeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfTrafficShapeRowStatus.setStatus(_A)
_HpnicfPortQueueTable_Object=MibTable
hpnicfPortQueueTable=_HpnicfPortQueueTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,17))
if mibBuilder.loadTexts:hpnicfPortQueueTable.setStatus(_A)
_HpnicfPortQueueEntry_Object=MibTableRow
hpnicfPortQueueEntry=_HpnicfPortQueueEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,17,1))
hpnicfPortQueueEntry.setIndexNames((0,_D,_A2),(0,_D,_A3))
if mibBuilder.loadTexts:hpnicfPortQueueEntry.setStatus(_A)
_HpnicfPortQueueIfIndex_Type=Integer32
_HpnicfPortQueueIfIndex_Object=MibTableColumn
hpnicfPortQueueIfIndex=_HpnicfPortQueueIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,17,1,1),_HpnicfPortQueueIfIndex_Type())
hpnicfPortQueueIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPortQueueIfIndex.setStatus(_A)
class _HpnicfPortQueueQueueID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfPortQueueQueueID_Type.__name__=_B
_HpnicfPortQueueQueueID_Object=MibTableColumn
hpnicfPortQueueQueueID=_HpnicfPortQueueQueueID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,17,1,2),_HpnicfPortQueueQueueID_Type())
hpnicfPortQueueQueueID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPortQueueQueueID.setStatus(_A)
class _HpnicfPortQueueWrrPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sp',1),('wrr-high-priority',2),('wrr-low-priority',3)))
_HpnicfPortQueueWrrPriority_Type.__name__=_B
_HpnicfPortQueueWrrPriority_Object=MibTableColumn
hpnicfPortQueueWrrPriority=_HpnicfPortQueueWrrPriority_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,17,1,3),_HpnicfPortQueueWrrPriority_Type())
hpnicfPortQueueWrrPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPortQueueWrrPriority.setStatus(_A)
class _HpnicfPortQueueWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,255))
_HpnicfPortQueueWeight_Type.__name__=_B
_HpnicfPortQueueWeight_Object=MibTableColumn
hpnicfPortQueueWeight=_HpnicfPortQueueWeight_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,17,1,4),_HpnicfPortQueueWeight_Type())
hpnicfPortQueueWeight.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPortQueueWeight.setStatus(_A)
_HpnicfDropModeTable_Object=MibTable
hpnicfDropModeTable=_HpnicfDropModeTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,18))
if mibBuilder.loadTexts:hpnicfDropModeTable.setStatus(_A)
_HpnicfDropModeEntry_Object=MibTableRow
hpnicfDropModeEntry=_HpnicfDropModeEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,18,1))
hpnicfDropModeEntry.setIndexNames((0,_D,_A4))
if mibBuilder.loadTexts:hpnicfDropModeEntry.setStatus(_A)
_HpnicfDropModeIfIndex_Type=Integer32
_HpnicfDropModeIfIndex_Object=MibTableColumn
hpnicfDropModeIfIndex=_HpnicfDropModeIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,18,1,1),_HpnicfDropModeIfIndex_Type())
hpnicfDropModeIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDropModeIfIndex.setStatus(_A)
class _HpnicfDropModeMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('random-detect',1),('tail-drop',2)))
_HpnicfDropModeMode_Type.__name__=_B
_HpnicfDropModeMode_Object=MibTableColumn
hpnicfDropModeMode=_HpnicfDropModeMode_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,18,1,2),_HpnicfDropModeMode_Type())
hpnicfDropModeMode.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDropModeMode.setStatus(_A)
class _HpnicfDropModeWredIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_HpnicfDropModeWredIndex_Type.__name__=_B
_HpnicfDropModeWredIndex_Object=MibTableColumn
hpnicfDropModeWredIndex=_HpnicfDropModeWredIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,18,1,3),_HpnicfDropModeWredIndex_Type())
hpnicfDropModeWredIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDropModeWredIndex.setStatus(_A)
_HpnicfWredTable_Object=MibTable
hpnicfWredTable=_HpnicfWredTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,19))
if mibBuilder.loadTexts:hpnicfWredTable.setStatus(_A)
_HpnicfWredEntry_Object=MibTableRow
hpnicfWredEntry=_HpnicfWredEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,19,1))
hpnicfWredEntry.setIndexNames((0,_D,_A5),(0,_D,_A6))
if mibBuilder.loadTexts:hpnicfWredEntry.setStatus(_A)
class _HpnicfWredIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_HpnicfWredIndex_Type.__name__=_B
_HpnicfWredIndex_Object=MibTableColumn
hpnicfWredIndex=_HpnicfWredIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,19,1,1),_HpnicfWredIndex_Type())
hpnicfWredIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfWredIndex.setStatus(_A)
class _HpnicfWredQueueId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfWredQueueId_Type.__name__=_B
_HpnicfWredQueueId_Object=MibTableColumn
hpnicfWredQueueId=_HpnicfWredQueueId_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,19,1,2),_HpnicfWredQueueId_Type())
hpnicfWredQueueId.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfWredQueueId.setStatus(_A)
class _HpnicfWredGreenMinThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfWredGreenMinThreshold_Type.__name__=_B
_HpnicfWredGreenMinThreshold_Object=MibTableColumn
hpnicfWredGreenMinThreshold=_HpnicfWredGreenMinThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,19,1,3),_HpnicfWredGreenMinThreshold_Type())
hpnicfWredGreenMinThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfWredGreenMinThreshold.setStatus(_A)
class _HpnicfWredGreenMaxThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfWredGreenMaxThreshold_Type.__name__=_B
_HpnicfWredGreenMaxThreshold_Object=MibTableColumn
hpnicfWredGreenMaxThreshold=_HpnicfWredGreenMaxThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,19,1,4),_HpnicfWredGreenMaxThreshold_Type())
hpnicfWredGreenMaxThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfWredGreenMaxThreshold.setStatus(_A)
class _HpnicfWredGreenMaxProb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_HpnicfWredGreenMaxProb_Type.__name__=_B
_HpnicfWredGreenMaxProb_Object=MibTableColumn
hpnicfWredGreenMaxProb=_HpnicfWredGreenMaxProb_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,19,1,5),_HpnicfWredGreenMaxProb_Type())
hpnicfWredGreenMaxProb.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfWredGreenMaxProb.setStatus(_A)
class _HpnicfWredYellowMinThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfWredYellowMinThreshold_Type.__name__=_B
_HpnicfWredYellowMinThreshold_Object=MibTableColumn
hpnicfWredYellowMinThreshold=_HpnicfWredYellowMinThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,19,1,6),_HpnicfWredYellowMinThreshold_Type())
hpnicfWredYellowMinThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfWredYellowMinThreshold.setStatus(_A)
class _HpnicfWredYellowMaxThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfWredYellowMaxThreshold_Type.__name__=_B
_HpnicfWredYellowMaxThreshold_Object=MibTableColumn
hpnicfWredYellowMaxThreshold=_HpnicfWredYellowMaxThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,19,1,7),_HpnicfWredYellowMaxThreshold_Type())
hpnicfWredYellowMaxThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfWredYellowMaxThreshold.setStatus(_A)
class _HpnicfWredYellowMaxProb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_HpnicfWredYellowMaxProb_Type.__name__=_B
_HpnicfWredYellowMaxProb_Object=MibTableColumn
hpnicfWredYellowMaxProb=_HpnicfWredYellowMaxProb_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,19,1,8),_HpnicfWredYellowMaxProb_Type())
hpnicfWredYellowMaxProb.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfWredYellowMaxProb.setStatus(_A)
class _HpnicfWredRedMinThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfWredRedMinThreshold_Type.__name__=_B
_HpnicfWredRedMinThreshold_Object=MibTableColumn
hpnicfWredRedMinThreshold=_HpnicfWredRedMinThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,19,1,9),_HpnicfWredRedMinThreshold_Type())
hpnicfWredRedMinThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfWredRedMinThreshold.setStatus(_A)
class _HpnicfWredRedMaxThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfWredRedMaxThreshold_Type.__name__=_B
_HpnicfWredRedMaxThreshold_Object=MibTableColumn
hpnicfWredRedMaxThreshold=_HpnicfWredRedMaxThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,19,1,10),_HpnicfWredRedMaxThreshold_Type())
hpnicfWredRedMaxThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfWredRedMaxThreshold.setStatus(_A)
class _HpnicfWredRedMaxProb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_HpnicfWredRedMaxProb_Type.__name__=_B
_HpnicfWredRedMaxProb_Object=MibTableColumn
hpnicfWredRedMaxProb=_HpnicfWredRedMaxProb_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,19,1,11),_HpnicfWredRedMaxProb_Type())
hpnicfWredRedMaxProb.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfWredRedMaxProb.setStatus(_A)
class _HpnicfWredExponent_Type(Integer32):defaultValue=9;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_HpnicfWredExponent_Type.__name__=_B
_HpnicfWredExponent_Object=MibTableColumn
hpnicfWredExponent=_HpnicfWredExponent_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,19,1,12),_HpnicfWredExponent_Type())
hpnicfWredExponent.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfWredExponent.setStatus(_A)
_HpnicfCosToLocalPrecedenceMapTable_Object=MibTable
hpnicfCosToLocalPrecedenceMapTable=_HpnicfCosToLocalPrecedenceMapTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,20))
if mibBuilder.loadTexts:hpnicfCosToLocalPrecedenceMapTable.setStatus(_A)
_HpnicfCosToLocalPrecedenceMapEntry_Object=MibTableRow
hpnicfCosToLocalPrecedenceMapEntry=_HpnicfCosToLocalPrecedenceMapEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,20,1))
hpnicfCosToLocalPrecedenceMapEntry.setIndexNames((0,_D,_A7))
if mibBuilder.loadTexts:hpnicfCosToLocalPrecedenceMapEntry.setStatus(_A)
class _HpnicfCosToLocalPrecedenceMapCosIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfCosToLocalPrecedenceMapCosIndex_Type.__name__=_B
_HpnicfCosToLocalPrecedenceMapCosIndex_Object=MibTableColumn
hpnicfCosToLocalPrecedenceMapCosIndex=_HpnicfCosToLocalPrecedenceMapCosIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,20,1,1),_HpnicfCosToLocalPrecedenceMapCosIndex_Type())
hpnicfCosToLocalPrecedenceMapCosIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCosToLocalPrecedenceMapCosIndex.setStatus(_A)
class _HpnicfCosToLocalPrecedenceMapLocalPrecedenceValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfCosToLocalPrecedenceMapLocalPrecedenceValue_Type.__name__=_B
_HpnicfCosToLocalPrecedenceMapLocalPrecedenceValue_Object=MibTableColumn
hpnicfCosToLocalPrecedenceMapLocalPrecedenceValue=_HpnicfCosToLocalPrecedenceMapLocalPrecedenceValue_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,20,1,2),_HpnicfCosToLocalPrecedenceMapLocalPrecedenceValue_Type())
hpnicfCosToLocalPrecedenceMapLocalPrecedenceValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfCosToLocalPrecedenceMapLocalPrecedenceValue.setStatus(_A)
_HpnicfCosToDropPrecedenceMapTable_Object=MibTable
hpnicfCosToDropPrecedenceMapTable=_HpnicfCosToDropPrecedenceMapTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,21))
if mibBuilder.loadTexts:hpnicfCosToDropPrecedenceMapTable.setStatus(_A)
_HpnicfCosToDropPrecedenceMapEntry_Object=MibTableRow
hpnicfCosToDropPrecedenceMapEntry=_HpnicfCosToDropPrecedenceMapEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,21,1))
hpnicfCosToDropPrecedenceMapEntry.setIndexNames((0,_D,_A8))
if mibBuilder.loadTexts:hpnicfCosToDropPrecedenceMapEntry.setStatus(_A)
class _HpnicfCosToDropPrecedenceMapCosIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfCosToDropPrecedenceMapCosIndex_Type.__name__=_B
_HpnicfCosToDropPrecedenceMapCosIndex_Object=MibTableColumn
hpnicfCosToDropPrecedenceMapCosIndex=_HpnicfCosToDropPrecedenceMapCosIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,21,1,1),_HpnicfCosToDropPrecedenceMapCosIndex_Type())
hpnicfCosToDropPrecedenceMapCosIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfCosToDropPrecedenceMapCosIndex.setStatus(_A)
class _HpnicfCosToDropPrecedenceMapDropPrecedenceValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_HpnicfCosToDropPrecedenceMapDropPrecedenceValue_Type.__name__=_B
_HpnicfCosToDropPrecedenceMapDropPrecedenceValue_Object=MibTableColumn
hpnicfCosToDropPrecedenceMapDropPrecedenceValue=_HpnicfCosToDropPrecedenceMapDropPrecedenceValue_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,21,1,2),_HpnicfCosToDropPrecedenceMapDropPrecedenceValue_Type())
hpnicfCosToDropPrecedenceMapDropPrecedenceValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfCosToDropPrecedenceMapDropPrecedenceValue.setStatus(_A)
_HpnicfDscpMapTable_Object=MibTable
hpnicfDscpMapTable=_HpnicfDscpMapTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,22))
if mibBuilder.loadTexts:hpnicfDscpMapTable.setStatus(_A)
_HpnicfDscpMapEntry_Object=MibTableRow
hpnicfDscpMapEntry=_HpnicfDscpMapEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,22,1))
hpnicfDscpMapEntry.setIndexNames((0,_D,_A9),(0,_D,_AA))
if mibBuilder.loadTexts:hpnicfDscpMapEntry.setStatus(_A)
class _HpnicfDscpMapConformLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_HpnicfDscpMapConformLevel_Type.__name__=_B
_HpnicfDscpMapConformLevel_Object=MibTableColumn
hpnicfDscpMapConformLevel=_HpnicfDscpMapConformLevel_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,22,1,1),_HpnicfDscpMapConformLevel_Type())
hpnicfDscpMapConformLevel.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDscpMapConformLevel.setStatus(_A)
class _HpnicfDscpMapDscpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HpnicfDscpMapDscpIndex_Type.__name__=_B
_HpnicfDscpMapDscpIndex_Object=MibTableColumn
hpnicfDscpMapDscpIndex=_HpnicfDscpMapDscpIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,22,1,2),_HpnicfDscpMapDscpIndex_Type())
hpnicfDscpMapDscpIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfDscpMapDscpIndex.setStatus(_A)
class _HpnicfDscpMapDscpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HpnicfDscpMapDscpValue_Type.__name__=_B
_HpnicfDscpMapDscpValue_Object=MibTableColumn
hpnicfDscpMapDscpValue=_HpnicfDscpMapDscpValue_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,22,1,3),_HpnicfDscpMapDscpValue_Type())
hpnicfDscpMapDscpValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDscpMapDscpValue.setStatus(_A)
class _HpnicfDscpMapExpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfDscpMapExpValue_Type.__name__=_B
_HpnicfDscpMapExpValue_Object=MibTableColumn
hpnicfDscpMapExpValue=_HpnicfDscpMapExpValue_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,22,1,4),_HpnicfDscpMapExpValue_Type())
hpnicfDscpMapExpValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDscpMapExpValue.setStatus(_A)
class _HpnicfDscpMapCosValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfDscpMapCosValue_Type.__name__=_B
_HpnicfDscpMapCosValue_Object=MibTableColumn
hpnicfDscpMapCosValue=_HpnicfDscpMapCosValue_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,22,1,5),_HpnicfDscpMapCosValue_Type())
hpnicfDscpMapCosValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDscpMapCosValue.setStatus(_A)
class _HpnicfDscpMapLocalPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfDscpMapLocalPrecedence_Type.__name__=_B
_HpnicfDscpMapLocalPrecedence_Object=MibTableColumn
hpnicfDscpMapLocalPrecedence=_HpnicfDscpMapLocalPrecedence_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,22,1,6),_HpnicfDscpMapLocalPrecedence_Type())
hpnicfDscpMapLocalPrecedence.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDscpMapLocalPrecedence.setStatus(_A)
class _HpnicfDscpMapDropPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_HpnicfDscpMapDropPrecedence_Type.__name__=_B
_HpnicfDscpMapDropPrecedence_Object=MibTableColumn
hpnicfDscpMapDropPrecedence=_HpnicfDscpMapDropPrecedence_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,22,1,7),_HpnicfDscpMapDropPrecedence_Type())
hpnicfDscpMapDropPrecedence.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDscpMapDropPrecedence.setStatus(_A)
_HpnicfExpMapTable_Object=MibTable
hpnicfExpMapTable=_HpnicfExpMapTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,23))
if mibBuilder.loadTexts:hpnicfExpMapTable.setStatus(_A)
_HpnicfExpMapEntry_Object=MibTableRow
hpnicfExpMapEntry=_HpnicfExpMapEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,23,1))
hpnicfExpMapEntry.setIndexNames((0,_D,_AB),(0,_D,_AC))
if mibBuilder.loadTexts:hpnicfExpMapEntry.setStatus(_A)
class _HpnicfExpMapConformLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_HpnicfExpMapConformLevel_Type.__name__=_B
_HpnicfExpMapConformLevel_Object=MibTableColumn
hpnicfExpMapConformLevel=_HpnicfExpMapConformLevel_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,23,1,1),_HpnicfExpMapConformLevel_Type())
hpnicfExpMapConformLevel.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfExpMapConformLevel.setStatus(_A)
class _HpnicfExpMapExpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfExpMapExpIndex_Type.__name__=_B
_HpnicfExpMapExpIndex_Object=MibTableColumn
hpnicfExpMapExpIndex=_HpnicfExpMapExpIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,23,1,2),_HpnicfExpMapExpIndex_Type())
hpnicfExpMapExpIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfExpMapExpIndex.setStatus(_A)
class _HpnicfExpMapDscpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HpnicfExpMapDscpValue_Type.__name__=_B
_HpnicfExpMapDscpValue_Object=MibTableColumn
hpnicfExpMapDscpValue=_HpnicfExpMapDscpValue_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,23,1,3),_HpnicfExpMapDscpValue_Type())
hpnicfExpMapDscpValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfExpMapDscpValue.setStatus(_A)
class _HpnicfExpMapExpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfExpMapExpValue_Type.__name__=_B
_HpnicfExpMapExpValue_Object=MibTableColumn
hpnicfExpMapExpValue=_HpnicfExpMapExpValue_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,23,1,4),_HpnicfExpMapExpValue_Type())
hpnicfExpMapExpValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfExpMapExpValue.setStatus(_A)
class _HpnicfExpMapCosValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfExpMapCosValue_Type.__name__=_B
_HpnicfExpMapCosValue_Object=MibTableColumn
hpnicfExpMapCosValue=_HpnicfExpMapCosValue_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,23,1,5),_HpnicfExpMapCosValue_Type())
hpnicfExpMapCosValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfExpMapCosValue.setStatus(_A)
class _HpnicfExpMapLocalPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfExpMapLocalPrecedence_Type.__name__=_B
_HpnicfExpMapLocalPrecedence_Object=MibTableColumn
hpnicfExpMapLocalPrecedence=_HpnicfExpMapLocalPrecedence_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,23,1,6),_HpnicfExpMapLocalPrecedence_Type())
hpnicfExpMapLocalPrecedence.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfExpMapLocalPrecedence.setStatus(_A)
class _HpnicfExpMapDropPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_HpnicfExpMapDropPrecedence_Type.__name__=_B
_HpnicfExpMapDropPrecedence_Object=MibTableColumn
hpnicfExpMapDropPrecedence=_HpnicfExpMapDropPrecedence_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,23,1,7),_HpnicfExpMapDropPrecedence_Type())
hpnicfExpMapDropPrecedence.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfExpMapDropPrecedence.setStatus(_A)
_HpnicfLocalPrecedenceMapTable_Object=MibTable
hpnicfLocalPrecedenceMapTable=_HpnicfLocalPrecedenceMapTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,24))
if mibBuilder.loadTexts:hpnicfLocalPrecedenceMapTable.setStatus(_A)
_HpnicfLocalPrecedenceMapEntry_Object=MibTableRow
hpnicfLocalPrecedenceMapEntry=_HpnicfLocalPrecedenceMapEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,24,1))
hpnicfLocalPrecedenceMapEntry.setIndexNames((0,_D,_AD),(0,_D,_AE))
if mibBuilder.loadTexts:hpnicfLocalPrecedenceMapEntry.setStatus(_A)
class _HpnicfLocalPrecedenceMapConformLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_HpnicfLocalPrecedenceMapConformLevel_Type.__name__=_B
_HpnicfLocalPrecedenceMapConformLevel_Object=MibTableColumn
hpnicfLocalPrecedenceMapConformLevel=_HpnicfLocalPrecedenceMapConformLevel_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,24,1,1),_HpnicfLocalPrecedenceMapConformLevel_Type())
hpnicfLocalPrecedenceMapConformLevel.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfLocalPrecedenceMapConformLevel.setStatus(_A)
class _HpnicfLocalPrecedenceMapLocalPrecedenceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfLocalPrecedenceMapLocalPrecedenceIndex_Type.__name__=_B
_HpnicfLocalPrecedenceMapLocalPrecedenceIndex_Object=MibTableColumn
hpnicfLocalPrecedenceMapLocalPrecedenceIndex=_HpnicfLocalPrecedenceMapLocalPrecedenceIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,24,1,2),_HpnicfLocalPrecedenceMapLocalPrecedenceIndex_Type())
hpnicfLocalPrecedenceMapLocalPrecedenceIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfLocalPrecedenceMapLocalPrecedenceIndex.setStatus(_A)
class _HpnicfLocalPrecedenceMapCosValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfLocalPrecedenceMapCosValue_Type.__name__=_B
_HpnicfLocalPrecedenceMapCosValue_Object=MibTableColumn
hpnicfLocalPrecedenceMapCosValue=_HpnicfLocalPrecedenceMapCosValue_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,24,1,3),_HpnicfLocalPrecedenceMapCosValue_Type())
hpnicfLocalPrecedenceMapCosValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfLocalPrecedenceMapCosValue.setStatus(_A)
_HpnicfPortWredTable_Object=MibTable
hpnicfPortWredTable=_HpnicfPortWredTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,25))
if mibBuilder.loadTexts:hpnicfPortWredTable.setStatus(_A)
_HpnicfPortWredEntry_Object=MibTableRow
hpnicfPortWredEntry=_HpnicfPortWredEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,25,1))
hpnicfPortWredEntry.setIndexNames((0,_D,_AF),(0,_D,_AG))
if mibBuilder.loadTexts:hpnicfPortWredEntry.setStatus(_A)
_HpnicfPortWredIfIndex_Type=Integer32
_HpnicfPortWredIfIndex_Object=MibTableColumn
hpnicfPortWredIfIndex=_HpnicfPortWredIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,25,1,1),_HpnicfPortWredIfIndex_Type())
hpnicfPortWredIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPortWredIfIndex.setStatus(_A)
class _HpnicfPortWredQueueID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfPortWredQueueID_Type.__name__=_B
_HpnicfPortWredQueueID_Object=MibTableColumn
hpnicfPortWredQueueID=_HpnicfPortWredQueueID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,25,1,2),_HpnicfPortWredQueueID_Type())
hpnicfPortWredQueueID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfPortWredQueueID.setStatus(_A)
class _HpnicfPortWredQueueStartLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2047))
_HpnicfPortWredQueueStartLength_Type.__name__=_B
_HpnicfPortWredQueueStartLength_Object=MibTableColumn
hpnicfPortWredQueueStartLength=_HpnicfPortWredQueueStartLength_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,25,1,3),_HpnicfPortWredQueueStartLength_Type())
hpnicfPortWredQueueStartLength.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPortWredQueueStartLength.setStatus(_A)
class _HpnicfPortWredQueueProbability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfPortWredQueueProbability_Type.__name__=_B
_HpnicfPortWredQueueProbability_Object=MibTableColumn
hpnicfPortWredQueueProbability=_HpnicfPortWredQueueProbability_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,25,1,4),_HpnicfPortWredQueueProbability_Type())
hpnicfPortWredQueueProbability.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPortWredQueueProbability.setStatus(_A)
_HpnicfMirroringGroupTable_Object=MibTable
hpnicfMirroringGroupTable=_HpnicfMirroringGroupTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,26))
if mibBuilder.loadTexts:hpnicfMirroringGroupTable.setStatus(_A)
_HpnicfMirroringGroupEntry_Object=MibTableRow
hpnicfMirroringGroupEntry=_HpnicfMirroringGroupEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,26,1))
hpnicfMirroringGroupEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:hpnicfMirroringGroupEntry.setStatus(_A)
class _HpnicfMirroringGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_HpnicfMirroringGroupID_Type.__name__=_B
_HpnicfMirroringGroupID_Object=MibTableColumn
hpnicfMirroringGroupID=_HpnicfMirroringGroupID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,26,1,1),_HpnicfMirroringGroupID_Type())
hpnicfMirroringGroupID.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMirroringGroupID.setStatus(_A)
class _HpnicfMirroringGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('local',1),('remote-source',2),('remote-destination',3)))
_HpnicfMirroringGroupType_Type.__name__=_B
_HpnicfMirroringGroupType_Object=MibTableColumn
hpnicfMirroringGroupType=_HpnicfMirroringGroupType_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,26,1,2),_HpnicfMirroringGroupType_Type())
hpnicfMirroringGroupType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirroringGroupType.setStatus(_A)
class _HpnicfMirroringGroupStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_HpnicfMirroringGroupStatus_Type.__name__=_B
_HpnicfMirroringGroupStatus_Object=MibTableColumn
hpnicfMirroringGroupStatus=_HpnicfMirroringGroupStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,26,1,3),_HpnicfMirroringGroupStatus_Type())
hpnicfMirroringGroupStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfMirroringGroupStatus.setStatus(_A)
_HpnicfMirroringGroupRowStatus_Type=RowStatus
_HpnicfMirroringGroupRowStatus_Object=MibTableColumn
hpnicfMirroringGroupRowStatus=_HpnicfMirroringGroupRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,26,1,4),_HpnicfMirroringGroupRowStatus_Type())
hpnicfMirroringGroupRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirroringGroupRowStatus.setStatus(_A)
_HpnicfMirroringGroupMirrorTable_Object=MibTable
hpnicfMirroringGroupMirrorTable=_HpnicfMirroringGroupMirrorTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,27))
if mibBuilder.loadTexts:hpnicfMirroringGroupMirrorTable.setStatus(_A)
_HpnicfMirroringGroupMirrorEntry_Object=MibTableRow
hpnicfMirroringGroupMirrorEntry=_HpnicfMirroringGroupMirrorEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,27,1))
hpnicfMirroringGroupMirrorEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:hpnicfMirroringGroupMirrorEntry.setStatus(_A)
_HpnicfMirroringGroupMirrorInboundIfIndexList_Type=OctetString
_HpnicfMirroringGroupMirrorInboundIfIndexList_Object=MibTableColumn
hpnicfMirroringGroupMirrorInboundIfIndexList=_HpnicfMirroringGroupMirrorInboundIfIndexList_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,27,1,1),_HpnicfMirroringGroupMirrorInboundIfIndexList_Type())
hpnicfMirroringGroupMirrorInboundIfIndexList.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirroringGroupMirrorInboundIfIndexList.setStatus(_A)
_HpnicfMirroringGroupMirrorOutboundIfIndexList_Type=OctetString
_HpnicfMirroringGroupMirrorOutboundIfIndexList_Object=MibTableColumn
hpnicfMirroringGroupMirrorOutboundIfIndexList=_HpnicfMirroringGroupMirrorOutboundIfIndexList_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,27,1,2),_HpnicfMirroringGroupMirrorOutboundIfIndexList_Type())
hpnicfMirroringGroupMirrorOutboundIfIndexList.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirroringGroupMirrorOutboundIfIndexList.setStatus(_A)
_HpnicfMirroringGroupMirrorRowStatus_Type=RowStatus
_HpnicfMirroringGroupMirrorRowStatus_Object=MibTableColumn
hpnicfMirroringGroupMirrorRowStatus=_HpnicfMirroringGroupMirrorRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,27,1,3),_HpnicfMirroringGroupMirrorRowStatus_Type())
hpnicfMirroringGroupMirrorRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirroringGroupMirrorRowStatus.setStatus(_A)
_HpnicfMirroringGroupMirrorInTypeList_Type=OctetString
_HpnicfMirroringGroupMirrorInTypeList_Object=MibTableColumn
hpnicfMirroringGroupMirrorInTypeList=_HpnicfMirroringGroupMirrorInTypeList_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,27,1,4),_HpnicfMirroringGroupMirrorInTypeList_Type())
hpnicfMirroringGroupMirrorInTypeList.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirroringGroupMirrorInTypeList.setStatus(_A)
_HpnicfMirroringGroupMirrorOutTypeList_Type=OctetString
_HpnicfMirroringGroupMirrorOutTypeList_Object=MibTableColumn
hpnicfMirroringGroupMirrorOutTypeList=_HpnicfMirroringGroupMirrorOutTypeList_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,27,1,5),_HpnicfMirroringGroupMirrorOutTypeList_Type())
hpnicfMirroringGroupMirrorOutTypeList.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirroringGroupMirrorOutTypeList.setStatus(_A)
_HpnicfMirroringGroupMonitorTable_Object=MibTable
hpnicfMirroringGroupMonitorTable=_HpnicfMirroringGroupMonitorTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,28))
if mibBuilder.loadTexts:hpnicfMirroringGroupMonitorTable.setStatus(_A)
_HpnicfMirroringGroupMonitorEntry_Object=MibTableRow
hpnicfMirroringGroupMonitorEntry=_HpnicfMirroringGroupMonitorEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,28,1))
hpnicfMirroringGroupMonitorEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:hpnicfMirroringGroupMonitorEntry.setStatus(_A)
_HpnicfMirroringGroupMonitorIfIndex_Type=Integer32
_HpnicfMirroringGroupMonitorIfIndex_Object=MibTableColumn
hpnicfMirroringGroupMonitorIfIndex=_HpnicfMirroringGroupMonitorIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,28,1,1),_HpnicfMirroringGroupMonitorIfIndex_Type())
hpnicfMirroringGroupMonitorIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirroringGroupMonitorIfIndex.setStatus(_A)
_HpnicfMirroringGroupMonitorRowStatus_Type=RowStatus
_HpnicfMirroringGroupMonitorRowStatus_Object=MibTableColumn
hpnicfMirroringGroupMonitorRowStatus=_HpnicfMirroringGroupMonitorRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,28,1,2),_HpnicfMirroringGroupMonitorRowStatus_Type())
hpnicfMirroringGroupMonitorRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirroringGroupMonitorRowStatus.setStatus(_A)
_HpnicfMirroringGroupMonitorType_Type=HpnicfMirrorOrMonitorType
_HpnicfMirroringGroupMonitorType_Object=MibTableColumn
hpnicfMirroringGroupMonitorType=_HpnicfMirroringGroupMonitorType_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,28,1,3),_HpnicfMirroringGroupMonitorType_Type())
hpnicfMirroringGroupMonitorType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirroringGroupMonitorType.setStatus(_A)
_HpnicfMirroringGroupReflectorTable_Object=MibTable
hpnicfMirroringGroupReflectorTable=_HpnicfMirroringGroupReflectorTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,29))
if mibBuilder.loadTexts:hpnicfMirroringGroupReflectorTable.setStatus(_A)
_HpnicfMirroringGroupReflectorEntry_Object=MibTableRow
hpnicfMirroringGroupReflectorEntry=_HpnicfMirroringGroupReflectorEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,29,1))
hpnicfMirroringGroupReflectorEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:hpnicfMirroringGroupReflectorEntry.setStatus(_A)
_HpnicfMirroringGroupReflectorIfIndex_Type=Integer32
_HpnicfMirroringGroupReflectorIfIndex_Object=MibTableColumn
hpnicfMirroringGroupReflectorIfIndex=_HpnicfMirroringGroupReflectorIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,29,1,1),_HpnicfMirroringGroupReflectorIfIndex_Type())
hpnicfMirroringGroupReflectorIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirroringGroupReflectorIfIndex.setStatus(_A)
_HpnicfMirroringGroupReflectorRowStatus_Type=RowStatus
_HpnicfMirroringGroupReflectorRowStatus_Object=MibTableColumn
hpnicfMirroringGroupReflectorRowStatus=_HpnicfMirroringGroupReflectorRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,29,1,2),_HpnicfMirroringGroupReflectorRowStatus_Type())
hpnicfMirroringGroupReflectorRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirroringGroupReflectorRowStatus.setStatus(_A)
_HpnicfMirroringGroupRprobeVlanTable_Object=MibTable
hpnicfMirroringGroupRprobeVlanTable=_HpnicfMirroringGroupRprobeVlanTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,30))
if mibBuilder.loadTexts:hpnicfMirroringGroupRprobeVlanTable.setStatus(_A)
_HpnicfMirroringGroupRprobeVlanEntry_Object=MibTableRow
hpnicfMirroringGroupRprobeVlanEntry=_HpnicfMirroringGroupRprobeVlanEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,30,1))
hpnicfMirroringGroupRprobeVlanEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:hpnicfMirroringGroupRprobeVlanEntry.setStatus(_A)
class _HpnicfMirroringGroupRprobeVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpnicfMirroringGroupRprobeVlanID_Type.__name__=_B
_HpnicfMirroringGroupRprobeVlanID_Object=MibTableColumn
hpnicfMirroringGroupRprobeVlanID=_HpnicfMirroringGroupRprobeVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,30,1,1),_HpnicfMirroringGroupRprobeVlanID_Type())
hpnicfMirroringGroupRprobeVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirroringGroupRprobeVlanID.setStatus(_A)
_HpnicfMirroringGroupRprobeVlanRowStatus_Type=RowStatus
_HpnicfMirroringGroupRprobeVlanRowStatus_Object=MibTableColumn
hpnicfMirroringGroupRprobeVlanRowStatus=_HpnicfMirroringGroupRprobeVlanRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,30,1,2),_HpnicfMirroringGroupRprobeVlanRowStatus_Type())
hpnicfMirroringGroupRprobeVlanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirroringGroupRprobeVlanRowStatus.setStatus(_A)
_HpnicfMirroringGroupMirrorMacTable_Object=MibTable
hpnicfMirroringGroupMirrorMacTable=_HpnicfMirroringGroupMirrorMacTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,31))
if mibBuilder.loadTexts:hpnicfMirroringGroupMirrorMacTable.setStatus(_A)
_HpnicfMirroringGroupMirrorMacEntry_Object=MibTableRow
hpnicfMirroringGroupMirrorMacEntry=_HpnicfMirroringGroupMirrorMacEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,31,1))
hpnicfMirroringGroupMirrorMacEntry.setIndexNames((0,_D,_J),(0,_D,_AH))
if mibBuilder.loadTexts:hpnicfMirroringGroupMirrorMacEntry.setStatus(_A)
_HpnicfMirroringGroupMirrorMacSeq_Type=Integer32
_HpnicfMirroringGroupMirrorMacSeq_Object=MibTableColumn
hpnicfMirroringGroupMirrorMacSeq=_HpnicfMirroringGroupMirrorMacSeq_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,31,1,1),_HpnicfMirroringGroupMirrorMacSeq_Type())
hpnicfMirroringGroupMirrorMacSeq.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMirroringGroupMirrorMacSeq.setStatus(_A)
_HpnicfMirroringGroupMirrorMac_Type=MacAddress
_HpnicfMirroringGroupMirrorMac_Object=MibTableColumn
hpnicfMirroringGroupMirrorMac=_HpnicfMirroringGroupMirrorMac_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,31,1,2),_HpnicfMirroringGroupMirrorMac_Type())
hpnicfMirroringGroupMirrorMac.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirroringGroupMirrorMac.setStatus(_A)
class _HpnicfMirrorMacVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpnicfMirrorMacVlanID_Type.__name__=_B
_HpnicfMirrorMacVlanID_Object=MibTableColumn
hpnicfMirrorMacVlanID=_HpnicfMirrorMacVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,31,1,3),_HpnicfMirrorMacVlanID_Type())
hpnicfMirrorMacVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirrorMacVlanID.setStatus(_A)
_HpnicfMirroringGroupMirroMacStatus_Type=RowStatus
_HpnicfMirroringGroupMirroMacStatus_Object=MibTableColumn
hpnicfMirroringGroupMirroMacStatus=_HpnicfMirroringGroupMirroMacStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,31,1,4),_HpnicfMirroringGroupMirroMacStatus_Type())
hpnicfMirroringGroupMirroMacStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirroringGroupMirroMacStatus.setStatus(_A)
_HpnicfMirroringGroupMirrorVlanTable_Object=MibTable
hpnicfMirroringGroupMirrorVlanTable=_HpnicfMirroringGroupMirrorVlanTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,32))
if mibBuilder.loadTexts:hpnicfMirroringGroupMirrorVlanTable.setStatus(_A)
_HpnicfMirroringGroupMirrorVlanEntry_Object=MibTableRow
hpnicfMirroringGroupMirrorVlanEntry=_HpnicfMirroringGroupMirrorVlanEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,32,1))
hpnicfMirroringGroupMirrorVlanEntry.setIndexNames((0,_D,_J),(0,_D,_AI))
if mibBuilder.loadTexts:hpnicfMirroringGroupMirrorVlanEntry.setStatus(_A)
_HpnicfMirroringGroupMirrorVlanSeq_Type=Integer32
_HpnicfMirroringGroupMirrorVlanSeq_Object=MibTableColumn
hpnicfMirroringGroupMirrorVlanSeq=_HpnicfMirroringGroupMirrorVlanSeq_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,32,1,1),_HpnicfMirroringGroupMirrorVlanSeq_Type())
hpnicfMirroringGroupMirrorVlanSeq.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMirroringGroupMirrorVlanSeq.setStatus(_A)
class _HpnicfMirroringGroupMirrorVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpnicfMirroringGroupMirrorVlanID_Type.__name__=_B
_HpnicfMirroringGroupMirrorVlanID_Object=MibTableColumn
hpnicfMirroringGroupMirrorVlanID=_HpnicfMirroringGroupMirrorVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,32,1,2),_HpnicfMirroringGroupMirrorVlanID_Type())
hpnicfMirroringGroupMirrorVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirroringGroupMirrorVlanID.setStatus(_A)
class _HpnicfMirroringGroupMirrorVlanDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inbound',1),('outbound',2),('both',3)))
_HpnicfMirroringGroupMirrorVlanDirection_Type.__name__=_B
_HpnicfMirroringGroupMirrorVlanDirection_Object=MibTableColumn
hpnicfMirroringGroupMirrorVlanDirection=_HpnicfMirroringGroupMirrorVlanDirection_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,32,1,3),_HpnicfMirroringGroupMirrorVlanDirection_Type())
hpnicfMirroringGroupMirrorVlanDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirroringGroupMirrorVlanDirection.setStatus(_A)
_HpnicfMirroringGroupMirroVlanStatus_Type=RowStatus
_HpnicfMirroringGroupMirroVlanStatus_Object=MibTableColumn
hpnicfMirroringGroupMirroVlanStatus=_HpnicfMirroringGroupMirroVlanStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,32,1,4),_HpnicfMirroringGroupMirroVlanStatus_Type())
hpnicfMirroringGroupMirroVlanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMirroringGroupMirroVlanStatus.setStatus(_A)
_HpnicfPortTrustTable_Object=MibTable
hpnicfPortTrustTable=_HpnicfPortTrustTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,33))
if mibBuilder.loadTexts:hpnicfPortTrustTable.setStatus(_A)
_HpnicfPortTrustEntry_Object=MibTableRow
hpnicfPortTrustEntry=_HpnicfPortTrustEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,33,1))
hpnicfPortTrustEntry.setIndexNames((0,_D,_AJ))
if mibBuilder.loadTexts:hpnicfPortTrustEntry.setStatus(_A)
_HpnicfPortTrustIfIndex_Type=Integer32
_HpnicfPortTrustIfIndex_Object=MibTableColumn
hpnicfPortTrustIfIndex=_HpnicfPortTrustIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,33,1,1),_HpnicfPortTrustIfIndex_Type())
hpnicfPortTrustIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfPortTrustIfIndex.setStatus(_A)
class _HpnicfPortTrustTrustType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('port',1),('cos',2),('dscp',3)))
_HpnicfPortTrustTrustType_Type.__name__=_B
_HpnicfPortTrustTrustType_Object=MibTableColumn
hpnicfPortTrustTrustType=_HpnicfPortTrustTrustType_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,33,1,2),_HpnicfPortTrustTrustType_Type())
hpnicfPortTrustTrustType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPortTrustTrustType.setStatus(_A)
class _HpnicfPortTrustOvercastType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noOvercast',1),('overcastDSCP',2),('overcastCOS',3)))
_HpnicfPortTrustOvercastType_Type.__name__=_B
_HpnicfPortTrustOvercastType_Object=MibTableColumn
hpnicfPortTrustOvercastType=_HpnicfPortTrustOvercastType_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,33,1,3),_HpnicfPortTrustOvercastType_Type())
hpnicfPortTrustOvercastType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPortTrustOvercastType.setStatus(_A)
class _HpnicfPortTrustReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_L,1))
_HpnicfPortTrustReset_Type.__name__=_B
_HpnicfPortTrustReset_Object=MibTableColumn
hpnicfPortTrustReset=_HpnicfPortTrustReset_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,33,1,4),_HpnicfPortTrustReset_Type())
hpnicfPortTrustReset.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfPortTrustReset.setStatus(_A)
_HpnicfRemarkVlanIDTable_Object=MibTable
hpnicfRemarkVlanIDTable=_HpnicfRemarkVlanIDTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,34))
if mibBuilder.loadTexts:hpnicfRemarkVlanIDTable.setStatus(_A)
_HpnicfRemarkVlanIDEntry_Object=MibTableRow
hpnicfRemarkVlanIDEntry=_HpnicfRemarkVlanIDEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,34,1))
hpnicfRemarkVlanIDEntry.setIndexNames((0,_D,_AK),(0,_D,_AL),(0,_D,_AM),(0,_D,_AN))
if mibBuilder.loadTexts:hpnicfRemarkVlanIDEntry.setStatus(_A)
class _HpnicfRemarkVlanIDAclIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2999))
_HpnicfRemarkVlanIDAclIndex_Type.__name__=_B
_HpnicfRemarkVlanIDAclIndex_Object=MibTableColumn
hpnicfRemarkVlanIDAclIndex=_HpnicfRemarkVlanIDAclIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,34,1,1),_HpnicfRemarkVlanIDAclIndex_Type())
hpnicfRemarkVlanIDAclIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfRemarkVlanIDAclIndex.setStatus(_A)
_HpnicfRemarkVlanIDIfIndex_Type=Integer32
_HpnicfRemarkVlanIDIfIndex_Object=MibTableColumn
hpnicfRemarkVlanIDIfIndex=_HpnicfRemarkVlanIDIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,34,1,2),_HpnicfRemarkVlanIDIfIndex_Type())
hpnicfRemarkVlanIDIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfRemarkVlanIDIfIndex.setStatus(_A)
class _HpnicfRemarkVlanIDVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpnicfRemarkVlanIDVlanID_Type.__name__=_B
_HpnicfRemarkVlanIDVlanID_Object=MibTableColumn
hpnicfRemarkVlanIDVlanID=_HpnicfRemarkVlanIDVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,34,1,3),_HpnicfRemarkVlanIDVlanID_Type())
hpnicfRemarkVlanIDVlanID.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfRemarkVlanIDVlanID.setStatus(_A)
class _HpnicfRemarkVlanIDDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_K,1),(_I,2)))
_HpnicfRemarkVlanIDDirection_Type.__name__=_B
_HpnicfRemarkVlanIDDirection_Object=MibTableColumn
hpnicfRemarkVlanIDDirection=_HpnicfRemarkVlanIDDirection_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,34,1,4),_HpnicfRemarkVlanIDDirection_Type())
hpnicfRemarkVlanIDDirection.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfRemarkVlanIDDirection.setStatus(_A)
class _HpnicfRemarkVlanIDUserAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5000,5999),ValueRangeConstraint(10000,12999))
_HpnicfRemarkVlanIDUserAclNum_Type.__name__=_B
_HpnicfRemarkVlanIDUserAclNum_Object=MibTableColumn
hpnicfRemarkVlanIDUserAclNum=_HpnicfRemarkVlanIDUserAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,34,1,5),_HpnicfRemarkVlanIDUserAclNum_Type())
hpnicfRemarkVlanIDUserAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRemarkVlanIDUserAclNum.setStatus(_A)
class _HpnicfRemarkVlanIDUserAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfRemarkVlanIDUserAclRule_Type.__name__=_B
_HpnicfRemarkVlanIDUserAclRule_Object=MibTableColumn
hpnicfRemarkVlanIDUserAclRule=_HpnicfRemarkVlanIDUserAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,34,1,6),_HpnicfRemarkVlanIDUserAclRule_Type())
hpnicfRemarkVlanIDUserAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRemarkVlanIDUserAclRule.setStatus(_A)
class _HpnicfRemarkVlanIDIpAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999),ValueRangeConstraint(10000,12999))
_HpnicfRemarkVlanIDIpAclNum_Type.__name__=_B
_HpnicfRemarkVlanIDIpAclNum_Object=MibTableColumn
hpnicfRemarkVlanIDIpAclNum=_HpnicfRemarkVlanIDIpAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,34,1,7),_HpnicfRemarkVlanIDIpAclNum_Type())
hpnicfRemarkVlanIDIpAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRemarkVlanIDIpAclNum.setStatus(_A)
class _HpnicfRemarkVlanIDIpAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfRemarkVlanIDIpAclRule_Type.__name__=_B
_HpnicfRemarkVlanIDIpAclRule_Object=MibTableColumn
hpnicfRemarkVlanIDIpAclRule=_HpnicfRemarkVlanIDIpAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,34,1,8),_HpnicfRemarkVlanIDIpAclRule_Type())
hpnicfRemarkVlanIDIpAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRemarkVlanIDIpAclRule.setStatus(_A)
class _HpnicfRemarkVlanIDLinkAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4000,4999),ValueRangeConstraint(10000,12999))
_HpnicfRemarkVlanIDLinkAclNum_Type.__name__=_B
_HpnicfRemarkVlanIDLinkAclNum_Object=MibTableColumn
hpnicfRemarkVlanIDLinkAclNum=_HpnicfRemarkVlanIDLinkAclNum_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,34,1,9),_HpnicfRemarkVlanIDLinkAclNum_Type())
hpnicfRemarkVlanIDLinkAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRemarkVlanIDLinkAclNum.setStatus(_A)
class _HpnicfRemarkVlanIDLinkAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfRemarkVlanIDLinkAclRule_Type.__name__=_B
_HpnicfRemarkVlanIDLinkAclRule_Object=MibTableColumn
hpnicfRemarkVlanIDLinkAclRule=_HpnicfRemarkVlanIDLinkAclRule_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,34,1,10),_HpnicfRemarkVlanIDLinkAclRule_Type())
hpnicfRemarkVlanIDLinkAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRemarkVlanIDLinkAclRule.setStatus(_A)
class _HpnicfRemarkVlanIDRemarkVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpnicfRemarkVlanIDRemarkVlanID_Type.__name__=_B
_HpnicfRemarkVlanIDRemarkVlanID_Object=MibTableColumn
hpnicfRemarkVlanIDRemarkVlanID=_HpnicfRemarkVlanIDRemarkVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,34,1,11),_HpnicfRemarkVlanIDRemarkVlanID_Type())
hpnicfRemarkVlanIDRemarkVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRemarkVlanIDRemarkVlanID.setStatus(_A)
class _HpnicfRemarkVlanIDPacketType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('all',1),('tagged',2),('untagged',3)))
_HpnicfRemarkVlanIDPacketType_Type.__name__=_B
_HpnicfRemarkVlanIDPacketType_Object=MibTableColumn
hpnicfRemarkVlanIDPacketType=_HpnicfRemarkVlanIDPacketType_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,34,1,12),_HpnicfRemarkVlanIDPacketType_Type())
hpnicfRemarkVlanIDPacketType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRemarkVlanIDPacketType.setStatus(_A)
_HpnicfRemarkVlanIDRowStatus_Type=RowStatus
_HpnicfRemarkVlanIDRowStatus_Object=MibTableColumn
hpnicfRemarkVlanIDRowStatus=_HpnicfRemarkVlanIDRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,34,1,13),_HpnicfRemarkVlanIDRowStatus_Type())
hpnicfRemarkVlanIDRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRemarkVlanIDRowStatus.setStatus(_A)
_HpnicfCosToDscpMapTable_Object=MibTable
hpnicfCosToDscpMapTable=_HpnicfCosToDscpMapTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,35))
if mibBuilder.loadTexts:hpnicfCosToDscpMapTable.setStatus(_A)
_HpnicfCosToDscpMapEntry_Object=MibTableRow
hpnicfCosToDscpMapEntry=_HpnicfCosToDscpMapEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,35,1))
hpnicfCosToDscpMapEntry.setIndexNames((0,_D,_AO))
if mibBuilder.loadTexts:hpnicfCosToDscpMapEntry.setStatus(_A)
class _HpnicfCosToDscpMapCosIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfCosToDscpMapCosIndex_Type.__name__=_B
_HpnicfCosToDscpMapCosIndex_Object=MibTableColumn
hpnicfCosToDscpMapCosIndex=_HpnicfCosToDscpMapCosIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,35,1,1),_HpnicfCosToDscpMapCosIndex_Type())
hpnicfCosToDscpMapCosIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfCosToDscpMapCosIndex.setStatus(_A)
class _HpnicfCosToDscpMapDscpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HpnicfCosToDscpMapDscpValue_Type.__name__=_B
_HpnicfCosToDscpMapDscpValue_Object=MibTableColumn
hpnicfCosToDscpMapDscpValue=_HpnicfCosToDscpMapDscpValue_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,35,1,2),_HpnicfCosToDscpMapDscpValue_Type())
hpnicfCosToDscpMapDscpValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfCosToDscpMapDscpValue.setStatus(_A)
class _HpnicfCosToDscpMapReSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_L,1))
_HpnicfCosToDscpMapReSet_Type.__name__=_B
_HpnicfCosToDscpMapReSet_Object=MibTableColumn
hpnicfCosToDscpMapReSet=_HpnicfCosToDscpMapReSet_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,35,1,3),_HpnicfCosToDscpMapReSet_Type())
hpnicfCosToDscpMapReSet.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfCosToDscpMapReSet.setStatus(_A)
_HpnicfDscpToLocalPreMapTable_Object=MibTable
hpnicfDscpToLocalPreMapTable=_HpnicfDscpToLocalPreMapTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,36))
if mibBuilder.loadTexts:hpnicfDscpToLocalPreMapTable.setStatus(_A)
_HpnicfDscpToLocalPreMapEntry_Object=MibTableRow
hpnicfDscpToLocalPreMapEntry=_HpnicfDscpToLocalPreMapEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,36,1))
hpnicfDscpToLocalPreMapEntry.setIndexNames((0,_D,_AP))
if mibBuilder.loadTexts:hpnicfDscpToLocalPreMapEntry.setStatus(_A)
class _HpnicfDscpToLocalPreMapDscpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HpnicfDscpToLocalPreMapDscpIndex_Type.__name__=_B
_HpnicfDscpToLocalPreMapDscpIndex_Object=MibTableColumn
hpnicfDscpToLocalPreMapDscpIndex=_HpnicfDscpToLocalPreMapDscpIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,36,1,1),_HpnicfDscpToLocalPreMapDscpIndex_Type())
hpnicfDscpToLocalPreMapDscpIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDscpToLocalPreMapDscpIndex.setStatus(_A)
class _HpnicfDscpToLocalPreMapLocalPreVal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfDscpToLocalPreMapLocalPreVal_Type.__name__=_B
_HpnicfDscpToLocalPreMapLocalPreVal_Object=MibTableColumn
hpnicfDscpToLocalPreMapLocalPreVal=_HpnicfDscpToLocalPreMapLocalPreVal_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,36,1,2),_HpnicfDscpToLocalPreMapLocalPreVal_Type())
hpnicfDscpToLocalPreMapLocalPreVal.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDscpToLocalPreMapLocalPreVal.setStatus(_A)
class _HpnicfDscpToLocalPreMapReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_L,1))
_HpnicfDscpToLocalPreMapReset_Type.__name__=_B
_HpnicfDscpToLocalPreMapReset_Object=MibTableColumn
hpnicfDscpToLocalPreMapReset=_HpnicfDscpToLocalPreMapReset_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,36,1,3),_HpnicfDscpToLocalPreMapReset_Type())
hpnicfDscpToLocalPreMapReset.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDscpToLocalPreMapReset.setStatus(_A)
_HpnicfDscpToDropPreMapTable_Object=MibTable
hpnicfDscpToDropPreMapTable=_HpnicfDscpToDropPreMapTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,37))
if mibBuilder.loadTexts:hpnicfDscpToDropPreMapTable.setStatus(_A)
_HpnicfDscpToDropPreMapEntry_Object=MibTableRow
hpnicfDscpToDropPreMapEntry=_HpnicfDscpToDropPreMapEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,37,1))
hpnicfDscpToDropPreMapEntry.setIndexNames((0,_D,_AQ))
if mibBuilder.loadTexts:hpnicfDscpToDropPreMapEntry.setStatus(_A)
class _HpnicfDscpToDropPreMapDscpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HpnicfDscpToDropPreMapDscpIndex_Type.__name__=_B
_HpnicfDscpToDropPreMapDscpIndex_Object=MibTableColumn
hpnicfDscpToDropPreMapDscpIndex=_HpnicfDscpToDropPreMapDscpIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,37,1,1),_HpnicfDscpToDropPreMapDscpIndex_Type())
hpnicfDscpToDropPreMapDscpIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDscpToDropPreMapDscpIndex.setStatus(_A)
class _HpnicfDscpToDropPreMapDropPreVal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_HpnicfDscpToDropPreMapDropPreVal_Type.__name__=_B
_HpnicfDscpToDropPreMapDropPreVal_Object=MibTableColumn
hpnicfDscpToDropPreMapDropPreVal=_HpnicfDscpToDropPreMapDropPreVal_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,37,1,2),_HpnicfDscpToDropPreMapDropPreVal_Type())
hpnicfDscpToDropPreMapDropPreVal.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDscpToDropPreMapDropPreVal.setStatus(_A)
class _HpnicfDscpToDropPreMapReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_L,1))
_HpnicfDscpToDropPreMapReset_Type.__name__=_B
_HpnicfDscpToDropPreMapReset_Object=MibTableColumn
hpnicfDscpToDropPreMapReset=_HpnicfDscpToDropPreMapReset_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,37,1,3),_HpnicfDscpToDropPreMapReset_Type())
hpnicfDscpToDropPreMapReset.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDscpToDropPreMapReset.setStatus(_A)
_HpnicfDscpToCosMapTable_Object=MibTable
hpnicfDscpToCosMapTable=_HpnicfDscpToCosMapTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,38))
if mibBuilder.loadTexts:hpnicfDscpToCosMapTable.setStatus(_A)
_HpnicfDscpToCosMapEntry_Object=MibTableRow
hpnicfDscpToCosMapEntry=_HpnicfDscpToCosMapEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,38,1))
hpnicfDscpToCosMapEntry.setIndexNames((0,_D,_AR))
if mibBuilder.loadTexts:hpnicfDscpToCosMapEntry.setStatus(_A)
class _HpnicfDscpToCosMapDscpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HpnicfDscpToCosMapDscpIndex_Type.__name__=_B
_HpnicfDscpToCosMapDscpIndex_Object=MibTableColumn
hpnicfDscpToCosMapDscpIndex=_HpnicfDscpToCosMapDscpIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,38,1,1),_HpnicfDscpToCosMapDscpIndex_Type())
hpnicfDscpToCosMapDscpIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDscpToCosMapDscpIndex.setStatus(_A)
class _HpnicfDscpToCosMapCosValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfDscpToCosMapCosValue_Type.__name__=_B
_HpnicfDscpToCosMapCosValue_Object=MibTableColumn
hpnicfDscpToCosMapCosValue=_HpnicfDscpToCosMapCosValue_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,38,1,2),_HpnicfDscpToCosMapCosValue_Type())
hpnicfDscpToCosMapCosValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDscpToCosMapCosValue.setStatus(_A)
class _HpnicfDscpToCosMapReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_L,1))
_HpnicfDscpToCosMapReset_Type.__name__=_B
_HpnicfDscpToCosMapReset_Object=MibTableColumn
hpnicfDscpToCosMapReset=_HpnicfDscpToCosMapReset_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,38,1,3),_HpnicfDscpToCosMapReset_Type())
hpnicfDscpToCosMapReset.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDscpToCosMapReset.setStatus(_A)
_HpnicfDscpToDscpMapTable_Object=MibTable
hpnicfDscpToDscpMapTable=_HpnicfDscpToDscpMapTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,39))
if mibBuilder.loadTexts:hpnicfDscpToDscpMapTable.setStatus(_A)
_HpnicfDscpToDscpMapEntry_Object=MibTableRow
hpnicfDscpToDscpMapEntry=_HpnicfDscpToDscpMapEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,39,1))
hpnicfDscpToDscpMapEntry.setIndexNames((0,_D,_AS))
if mibBuilder.loadTexts:hpnicfDscpToDscpMapEntry.setStatus(_A)
class _HpnicfDscpToDscpMapDscpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HpnicfDscpToDscpMapDscpIndex_Type.__name__=_B
_HpnicfDscpToDscpMapDscpIndex_Object=MibTableColumn
hpnicfDscpToDscpMapDscpIndex=_HpnicfDscpToDscpMapDscpIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,39,1,1),_HpnicfDscpToDscpMapDscpIndex_Type())
hpnicfDscpToDscpMapDscpIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDscpToDscpMapDscpIndex.setStatus(_A)
class _HpnicfDscpToDscpMapDscpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HpnicfDscpToDscpMapDscpValue_Type.__name__=_B
_HpnicfDscpToDscpMapDscpValue_Object=MibTableColumn
hpnicfDscpToDscpMapDscpValue=_HpnicfDscpToDscpMapDscpValue_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,39,1,2),_HpnicfDscpToDscpMapDscpValue_Type())
hpnicfDscpToDscpMapDscpValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDscpToDscpMapDscpValue.setStatus(_A)
class _HpnicfDscpToDscpMapReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_L,1))
_HpnicfDscpToDscpMapReset_Type.__name__=_B
_HpnicfDscpToDscpMapReset_Object=MibTableColumn
hpnicfDscpToDscpMapReset=_HpnicfDscpToDscpMapReset_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,16,2,39,1,3),_HpnicfDscpToDscpMapReset_Type())
hpnicfDscpToDscpMapReset.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDscpToDscpMapReset.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'HpnicfMirrorOrMonitorType':HpnicfMirrorOrMonitorType,'hpnicfLswQosAclMib':hpnicfLswQosAclMib,'hpnicfLswQosMibObject':hpnicfLswQosMibObject,'hpnicfPriorityTrustMode':hpnicfPriorityTrustMode,'hpnicfPortMonitorBothIfIndex':hpnicfPortMonitorBothIfIndex,'hpnicfQueueTable':hpnicfQueueTable,'hpnicfQueueEntry':hpnicfQueueEntry,_P:hpnicfQueueIfIndex,'hpnicfQueueScheduleMode':hpnicfQueueScheduleMode,'hpnicfQueueWeight1':hpnicfQueueWeight1,'hpnicfQueueWeight2':hpnicfQueueWeight2,'hpnicfQueueWeight3':hpnicfQueueWeight3,'hpnicfQueueWeight4':hpnicfQueueWeight4,'hpnicfQueueMaxDelay':hpnicfQueueMaxDelay,'hpnicfQueueWeight5':hpnicfQueueWeight5,'hpnicfQueueWeight6':hpnicfQueueWeight6,'hpnicfQueueWeight7':hpnicfQueueWeight7,'hpnicfQueueWeight8':hpnicfQueueWeight8,'hpnicfRateLimitTable':hpnicfRateLimitTable,'hpnicfRateLimitEntry':hpnicfRateLimitEntry,_Q:hpnicfRateLimitAclIndex,_R:hpnicfRateLimitIfIndex,_S:hpnicfRateLimitVlanID,_T:hpnicfRateLimitDirection,'hpnicfRateLimitUserAclNum':hpnicfRateLimitUserAclNum,'hpnicfRateLimitUserAclRule':hpnicfRateLimitUserAclRule,'hpnicfRateLimitIpAclNum':hpnicfRateLimitIpAclNum,'hpnicfRateLimitIpAclRule':hpnicfRateLimitIpAclRule,'hpnicfRateLimitLinkAclNum':hpnicfRateLimitLinkAclNum,'hpnicfRateLimitLinkAclRule':hpnicfRateLimitLinkAclRule,'hpnicfRateLimitTargetRateMbps':hpnicfRateLimitTargetRateMbps,'hpnicfRateLimitTargetRateKbps':hpnicfRateLimitTargetRateKbps,'hpnicfRateLimitPeakRate':hpnicfRateLimitPeakRate,'hpnicfRateLimitCIR':hpnicfRateLimitCIR,'hpnicfRateLimitCBS':hpnicfRateLimitCBS,'hpnicfRateLimitEBS':hpnicfRateLimitEBS,'hpnicfRateLimitPIR':hpnicfRateLimitPIR,'hpnicfRateLimitConformLocalPre':hpnicfRateLimitConformLocalPre,'hpnicfRateLimitConformActionType':hpnicfRateLimitConformActionType,'hpnicfRateLimitExceedActionType':hpnicfRateLimitExceedActionType,'hpnicfRateLimitExceedDscp':hpnicfRateLimitExceedDscp,'hpnicfRateLimitRuntime':hpnicfRateLimitRuntime,'hpnicfRateLimitRowStatus':hpnicfRateLimitRowStatus,'hpnicfRateLimitExceedCos':hpnicfRateLimitExceedCos,'hpnicfRateLimitConformCos':hpnicfRateLimitConformCos,'hpnicfRateLimitConformDscp':hpnicfRateLimitConformDscp,'hpnicfRateLimitMeterStatByteCount':hpnicfRateLimitMeterStatByteCount,'hpnicfRateLimitMeterStatByteXCount':hpnicfRateLimitMeterStatByteXCount,'hpnicfRateLimitMeterStatState':hpnicfRateLimitMeterStatState,'hpnicfPriorityTable':hpnicfPriorityTable,'hpnicfPriorityEntry':hpnicfPriorityEntry,_U:hpnicfPriorityAclIndex,_V:hpnicfPriorityIfIndex,_W:hpnicfPriorityVlanID,_X:hpnicfPriorityDirection,'hpnicfPriorityUserAclNum':hpnicfPriorityUserAclNum,'hpnicfPriorityUserAclRule':hpnicfPriorityUserAclRule,'hpnicfPriorityIpAclNum':hpnicfPriorityIpAclNum,'hpnicfPriorityIpAclRule':hpnicfPriorityIpAclRule,'hpnicfPriorityLinkAclNum':hpnicfPriorityLinkAclNum,'hpnicfPriorityLinkAclRule':hpnicfPriorityLinkAclRule,'hpnicfPriorityDscp':hpnicfPriorityDscp,'hpnicfPriorityIpPre':hpnicfPriorityIpPre,'hpnicfPriorityIpPreFromCos':hpnicfPriorityIpPreFromCos,'hpnicfPriorityCos':hpnicfPriorityCos,'hpnicfPriorityCosFromIpPre':hpnicfPriorityCosFromIpPre,'hpnicfPriorityLocalPre':hpnicfPriorityLocalPre,'hpnicfPriorityPolicedServiceType':hpnicfPriorityPolicedServiceType,'hpnicfPriorityPolicedServiceDscp':hpnicfPriorityPolicedServiceDscp,'hpnicfPriorityPolicedServiceExp':hpnicfPriorityPolicedServiceExp,'hpnicfPriorityPolicedServiceCos':hpnicfPriorityPolicedServiceCos,'hpnicfPriorityPolicedServiceLoaclPre':hpnicfPriorityPolicedServiceLoaclPre,'hpnicfPriorityPolicedServiceDropPriority':hpnicfPriorityPolicedServiceDropPriority,'hpnicfPriorityRuntime':hpnicfPriorityRuntime,'hpnicfPriorityRowStatus':hpnicfPriorityRowStatus,'hpnicfRedirectTable':hpnicfRedirectTable,'hpnicfRedirectEntry':hpnicfRedirectEntry,_Y:hpnicfRedirectAclIndex,_Z:hpnicfRedirectIfIndex,_a:hpnicfRedirectVlanID,_b:hpnicfRedirectDirection,'hpnicfRedirectUserAclNum':hpnicfRedirectUserAclNum,'hpnicfRedirectUserAclRule':hpnicfRedirectUserAclRule,'hpnicfRedirectIpAclNum':hpnicfRedirectIpAclNum,'hpnicfRedirectIpAclRule':hpnicfRedirectIpAclRule,'hpnicfRedirectLinkAclNum':hpnicfRedirectLinkAclNum,'hpnicfRedirectLinkAclRule':hpnicfRedirectLinkAclRule,'hpnicfRedirectToCpu':hpnicfRedirectToCpu,'hpnicfRedirectToIfIndex':hpnicfRedirectToIfIndex,'hpnicfRedirectToNextHop1':hpnicfRedirectToNextHop1,'hpnicfRedirectToNextHop2':hpnicfRedirectToNextHop2,'hpnicfRedirectRuntime':hpnicfRedirectRuntime,'hpnicfRedirectRowStatus':hpnicfRedirectRowStatus,'hpnicfRedirectToSlotNo':hpnicfRedirectToSlotNo,'hpnicfRedirectRemarkedDSCP':hpnicfRedirectRemarkedDSCP,'hpnicfRedirectRemarkedPri':hpnicfRedirectRemarkedPri,'hpnicfRedirectRemarkedTos':hpnicfRedirectRemarkedTos,'hpnicfRedirectToNextHop3':hpnicfRedirectToNextHop3,'hpnicfRedirectTargetVlanID':hpnicfRedirectTargetVlanID,'hpnicfRedirectMode':hpnicfRedirectMode,'hpnicfRedirectToNestedVlanID':hpnicfRedirectToNestedVlanID,'hpnicfRedirectToModifiedVlanID':hpnicfRedirectToModifiedVlanID,'hpnicfStatisticTable':hpnicfStatisticTable,'hpnicfStatisticEntry':hpnicfStatisticEntry,_c:hpnicfStatisticAclIndex,_d:hpnicfStatisticIfIndex,_e:hpnicfStatisticVlanID,_f:hpnicfStatisticDirection,'hpnicfStatisticUserAclNum':hpnicfStatisticUserAclNum,'hpnicfStatisticUserAclRule':hpnicfStatisticUserAclRule,'hpnicfStatisticIpAclNum':hpnicfStatisticIpAclNum,'hpnicfStatisticIpAclRule':hpnicfStatisticIpAclRule,'hpnicfStatisticLinkAclNum':hpnicfStatisticLinkAclNum,'hpnicfStatisticLinkAclRule':hpnicfStatisticLinkAclRule,'hpnicfStatisticRuntime':hpnicfStatisticRuntime,'hpnicfStatisticPacketCount':hpnicfStatisticPacketCount,'hpnicfStatisticByteCount':hpnicfStatisticByteCount,'hpnicfStatisticCountClear':hpnicfStatisticCountClear,'hpnicfStatisticRowStatus':hpnicfStatisticRowStatus,'hpnicfStatisticPacketXCount':hpnicfStatisticPacketXCount,'hpnicfStatisticByteXCount':hpnicfStatisticByteXCount,'hpnicfMirrorTable':hpnicfMirrorTable,'hpnicfMirrorEntry':hpnicfMirrorEntry,_g:hpnicfMirrorAclIndex,_h:hpnicfMirrorIfIndex,_i:hpnicfMirrorVlanID,_j:hpnicfMirrorDirection,'hpnicfMirrorUserAclNum':hpnicfMirrorUserAclNum,'hpnicfMirrorUserAclRule':hpnicfMirrorUserAclRule,'hpnicfMirrorIpAclNum':hpnicfMirrorIpAclNum,'hpnicfMirrorIpAclRule':hpnicfMirrorIpAclRule,'hpnicfMirrorLinkAclNum':hpnicfMirrorLinkAclNum,'hpnicfMirrorLinkAclRule':hpnicfMirrorLinkAclRule,'hpnicfMirrorToIfIndex':hpnicfMirrorToIfIndex,'hpnicfMirrorToCpu':hpnicfMirrorToCpu,'hpnicfMirrorRuntime':hpnicfMirrorRuntime,'hpnicfMirrorRowStatus':hpnicfMirrorRowStatus,'hpnicfMirrorToGroup':hpnicfMirrorToGroup,'hpnicfPortMirrorTable':hpnicfPortMirrorTable,'hpnicfPortMirrorEntry':hpnicfPortMirrorEntry,_k:hpnicfPortMirrorIfIndex,'hpnicfPortMirrorDirection':hpnicfPortMirrorDirection,'hpnicfPortMirrorRowStatus':hpnicfPortMirrorRowStatus,'hpnicfLineRateTable':hpnicfLineRateTable,'hpnicfLineRateEntry':hpnicfLineRateEntry,_l:hpnicfLineRateIfIndex,_m:hpnicfLineRateDirection,'hpnicfLineRateValue':hpnicfLineRateValue,'hpnicfLineRateRowStatus':hpnicfLineRateRowStatus,'hpnicfBandwidthTable':hpnicfBandwidthTable,'hpnicfBandwidthEntry':hpnicfBandwidthEntry,_n:hpnicfBandwidthAclIndex,_o:hpnicfBandwidthIfIndex,_p:hpnicfBandwidthVlanID,_q:hpnicfBandwidthDirection,'hpnicfBandwidthIpAclNum':hpnicfBandwidthIpAclNum,'hpnicfBandwidthIpAclRule':hpnicfBandwidthIpAclRule,'hpnicfBandwidthLinkAclNum':hpnicfBandwidthLinkAclNum,'hpnicfBandwidthLinkAclRule':hpnicfBandwidthLinkAclRule,'hpnicfBandwidthMinGuaranteedWidth':hpnicfBandwidthMinGuaranteedWidth,'hpnicfBandwidthMaxGuaranteedWidth':hpnicfBandwidthMaxGuaranteedWidth,'hpnicfBandwidthWeight':hpnicfBandwidthWeight,'hpnicfBandwidthRuntime':hpnicfBandwidthRuntime,'hpnicfBandwidthRowStatus':hpnicfBandwidthRowStatus,'hpnicfRedTable':hpnicfRedTable,'hpnicfRedEntry':hpnicfRedEntry,_r:hpnicfRedAclIndex,_s:hpnicfRedIfIndex,_t:hpnicfRedVlanID,_u:hpnicfRedDirection,'hpnicfRedIpAclNum':hpnicfRedIpAclNum,'hpnicfRedIpAclRule':hpnicfRedIpAclRule,'hpnicfRedLinkAclNum':hpnicfRedLinkAclNum,'hpnicfRedLinkAclRule':hpnicfRedLinkAclRule,'hpnicfRedStartQueueLen':hpnicfRedStartQueueLen,'hpnicfRedStopQueueLen':hpnicfRedStopQueueLen,'hpnicfRedProbability':hpnicfRedProbability,'hpnicfRedRuntime':hpnicfRedRuntime,'hpnicfRedRowStatus':hpnicfRedRowStatus,'hpnicfMirrorGroupTable':hpnicfMirrorGroupTable,'hpnicfMirrorGroupEntry':hpnicfMirrorGroupEntry,_v:hpnicfMirrorGroupID,'hpnicfMirrorGroupDirection':hpnicfMirrorGroupDirection,'hpnicfMirrorGroupMirrorIfIndexList':hpnicfMirrorGroupMirrorIfIndexList,'hpnicfMirrorGroupMonitorIfIndex':hpnicfMirrorGroupMonitorIfIndex,'hpnicfMirrorGroupRowStatus':hpnicfMirrorGroupRowStatus,'hpnicfFlowtempTable':hpnicfFlowtempTable,'hpnicfFlowtempEntry':hpnicfFlowtempEntry,_w:hpnicfFlowtempIndex,'hpnicfFlowtempIpProtocol':hpnicfFlowtempIpProtocol,'hpnicfFlowtempTcpFlag':hpnicfFlowtempTcpFlag,'hpnicfFlowtempSPort':hpnicfFlowtempSPort,'hpnicfFlowtempDPort':hpnicfFlowtempDPort,'hpnicfFlowtempIcmpType':hpnicfFlowtempIcmpType,'hpnicfFlowtempIcmpCode':hpnicfFlowtempIcmpCode,'hpnicfFlowtempFragment':hpnicfFlowtempFragment,'hpnicfFlowtempDscp':hpnicfFlowtempDscp,'hpnicfFlowtempIpPre':hpnicfFlowtempIpPre,'hpnicfFlowtempTos':hpnicfFlowtempTos,'hpnicfFlowtempSIp':hpnicfFlowtempSIp,'hpnicfFlowtempSIpMask':hpnicfFlowtempSIpMask,'hpnicfFlowtempDIp':hpnicfFlowtempDIp,'hpnicfFlowtempDIpMask':hpnicfFlowtempDIpMask,'hpnicfFlowtempEthProtocol':hpnicfFlowtempEthProtocol,'hpnicfFlowtempSMac':hpnicfFlowtempSMac,'hpnicfFlowtempSMacMask':hpnicfFlowtempSMacMask,'hpnicfFlowtempDMac':hpnicfFlowtempDMac,'hpnicfFlowtempDMacMask':hpnicfFlowtempDMacMask,'hpnicfFlowtempVpn':hpnicfFlowtempVpn,'hpnicfFlowtempRowStatus':hpnicfFlowtempRowStatus,'hpnicfFlowtempVlanId':hpnicfFlowtempVlanId,'hpnicfFlowtempCos':hpnicfFlowtempCos,'hpnicfFlowtempEnableTable':hpnicfFlowtempEnableTable,'hpnicfFlowtempEnableEntry':hpnicfFlowtempEnableEntry,_y:hpnicfFlowtempEnableIfIndex,_z:hpnicfFlowtempEnableVlanID,'hpnicfFlowtempEnableFlowtempIndex':hpnicfFlowtempEnableFlowtempIndex,'hpnicfTrafficShapeTable':hpnicfTrafficShapeTable,'hpnicfTrafficShapeEntry':hpnicfTrafficShapeEntry,_A0:hpnicfTrafficShapeIfIndex,_A1:hpnicfTrafficShapeQueueId,'hpnicfTrafficShapeMaxRate':hpnicfTrafficShapeMaxRate,'hpnicfTrafficShapeBurstSize':hpnicfTrafficShapeBurstSize,'hpnicfTrafficShapeBufferLimit':hpnicfTrafficShapeBufferLimit,'hpnicfTrafficShapeRowStatus':hpnicfTrafficShapeRowStatus,'hpnicfPortQueueTable':hpnicfPortQueueTable,'hpnicfPortQueueEntry':hpnicfPortQueueEntry,_A2:hpnicfPortQueueIfIndex,_A3:hpnicfPortQueueQueueID,'hpnicfPortQueueWrrPriority':hpnicfPortQueueWrrPriority,'hpnicfPortQueueWeight':hpnicfPortQueueWeight,'hpnicfDropModeTable':hpnicfDropModeTable,'hpnicfDropModeEntry':hpnicfDropModeEntry,_A4:hpnicfDropModeIfIndex,'hpnicfDropModeMode':hpnicfDropModeMode,'hpnicfDropModeWredIndex':hpnicfDropModeWredIndex,'hpnicfWredTable':hpnicfWredTable,'hpnicfWredEntry':hpnicfWredEntry,_A5:hpnicfWredIndex,_A6:hpnicfWredQueueId,'hpnicfWredGreenMinThreshold':hpnicfWredGreenMinThreshold,'hpnicfWredGreenMaxThreshold':hpnicfWredGreenMaxThreshold,'hpnicfWredGreenMaxProb':hpnicfWredGreenMaxProb,'hpnicfWredYellowMinThreshold':hpnicfWredYellowMinThreshold,'hpnicfWredYellowMaxThreshold':hpnicfWredYellowMaxThreshold,'hpnicfWredYellowMaxProb':hpnicfWredYellowMaxProb,'hpnicfWredRedMinThreshold':hpnicfWredRedMinThreshold,'hpnicfWredRedMaxThreshold':hpnicfWredRedMaxThreshold,'hpnicfWredRedMaxProb':hpnicfWredRedMaxProb,'hpnicfWredExponent':hpnicfWredExponent,'hpnicfCosToLocalPrecedenceMapTable':hpnicfCosToLocalPrecedenceMapTable,'hpnicfCosToLocalPrecedenceMapEntry':hpnicfCosToLocalPrecedenceMapEntry,_A7:hpnicfCosToLocalPrecedenceMapCosIndex,'hpnicfCosToLocalPrecedenceMapLocalPrecedenceValue':hpnicfCosToLocalPrecedenceMapLocalPrecedenceValue,'hpnicfCosToDropPrecedenceMapTable':hpnicfCosToDropPrecedenceMapTable,'hpnicfCosToDropPrecedenceMapEntry':hpnicfCosToDropPrecedenceMapEntry,_A8:hpnicfCosToDropPrecedenceMapCosIndex,'hpnicfCosToDropPrecedenceMapDropPrecedenceValue':hpnicfCosToDropPrecedenceMapDropPrecedenceValue,'hpnicfDscpMapTable':hpnicfDscpMapTable,'hpnicfDscpMapEntry':hpnicfDscpMapEntry,_A9:hpnicfDscpMapConformLevel,_AA:hpnicfDscpMapDscpIndex,'hpnicfDscpMapDscpValue':hpnicfDscpMapDscpValue,'hpnicfDscpMapExpValue':hpnicfDscpMapExpValue,'hpnicfDscpMapCosValue':hpnicfDscpMapCosValue,'hpnicfDscpMapLocalPrecedence':hpnicfDscpMapLocalPrecedence,'hpnicfDscpMapDropPrecedence':hpnicfDscpMapDropPrecedence,'hpnicfExpMapTable':hpnicfExpMapTable,'hpnicfExpMapEntry':hpnicfExpMapEntry,_AB:hpnicfExpMapConformLevel,_AC:hpnicfExpMapExpIndex,'hpnicfExpMapDscpValue':hpnicfExpMapDscpValue,'hpnicfExpMapExpValue':hpnicfExpMapExpValue,'hpnicfExpMapCosValue':hpnicfExpMapCosValue,'hpnicfExpMapLocalPrecedence':hpnicfExpMapLocalPrecedence,'hpnicfExpMapDropPrecedence':hpnicfExpMapDropPrecedence,'hpnicfLocalPrecedenceMapTable':hpnicfLocalPrecedenceMapTable,'hpnicfLocalPrecedenceMapEntry':hpnicfLocalPrecedenceMapEntry,_AD:hpnicfLocalPrecedenceMapConformLevel,_AE:hpnicfLocalPrecedenceMapLocalPrecedenceIndex,'hpnicfLocalPrecedenceMapCosValue':hpnicfLocalPrecedenceMapCosValue,'hpnicfPortWredTable':hpnicfPortWredTable,'hpnicfPortWredEntry':hpnicfPortWredEntry,_AF:hpnicfPortWredIfIndex,_AG:hpnicfPortWredQueueID,'hpnicfPortWredQueueStartLength':hpnicfPortWredQueueStartLength,'hpnicfPortWredQueueProbability':hpnicfPortWredQueueProbability,'hpnicfMirroringGroupTable':hpnicfMirroringGroupTable,'hpnicfMirroringGroupEntry':hpnicfMirroringGroupEntry,_J:hpnicfMirroringGroupID,'hpnicfMirroringGroupType':hpnicfMirroringGroupType,'hpnicfMirroringGroupStatus':hpnicfMirroringGroupStatus,'hpnicfMirroringGroupRowStatus':hpnicfMirroringGroupRowStatus,'hpnicfMirroringGroupMirrorTable':hpnicfMirroringGroupMirrorTable,'hpnicfMirroringGroupMirrorEntry':hpnicfMirroringGroupMirrorEntry,'hpnicfMirroringGroupMirrorInboundIfIndexList':hpnicfMirroringGroupMirrorInboundIfIndexList,'hpnicfMirroringGroupMirrorOutboundIfIndexList':hpnicfMirroringGroupMirrorOutboundIfIndexList,'hpnicfMirroringGroupMirrorRowStatus':hpnicfMirroringGroupMirrorRowStatus,'hpnicfMirroringGroupMirrorInTypeList':hpnicfMirroringGroupMirrorInTypeList,'hpnicfMirroringGroupMirrorOutTypeList':hpnicfMirroringGroupMirrorOutTypeList,'hpnicfMirroringGroupMonitorTable':hpnicfMirroringGroupMonitorTable,'hpnicfMirroringGroupMonitorEntry':hpnicfMirroringGroupMonitorEntry,'hpnicfMirroringGroupMonitorIfIndex':hpnicfMirroringGroupMonitorIfIndex,'hpnicfMirroringGroupMonitorRowStatus':hpnicfMirroringGroupMonitorRowStatus,'hpnicfMirroringGroupMonitorType':hpnicfMirroringGroupMonitorType,'hpnicfMirroringGroupReflectorTable':hpnicfMirroringGroupReflectorTable,'hpnicfMirroringGroupReflectorEntry':hpnicfMirroringGroupReflectorEntry,'hpnicfMirroringGroupReflectorIfIndex':hpnicfMirroringGroupReflectorIfIndex,'hpnicfMirroringGroupReflectorRowStatus':hpnicfMirroringGroupReflectorRowStatus,'hpnicfMirroringGroupRprobeVlanTable':hpnicfMirroringGroupRprobeVlanTable,'hpnicfMirroringGroupRprobeVlanEntry':hpnicfMirroringGroupRprobeVlanEntry,'hpnicfMirroringGroupRprobeVlanID':hpnicfMirroringGroupRprobeVlanID,'hpnicfMirroringGroupRprobeVlanRowStatus':hpnicfMirroringGroupRprobeVlanRowStatus,'hpnicfMirroringGroupMirrorMacTable':hpnicfMirroringGroupMirrorMacTable,'hpnicfMirroringGroupMirrorMacEntry':hpnicfMirroringGroupMirrorMacEntry,_AH:hpnicfMirroringGroupMirrorMacSeq,'hpnicfMirroringGroupMirrorMac':hpnicfMirroringGroupMirrorMac,'hpnicfMirrorMacVlanID':hpnicfMirrorMacVlanID,'hpnicfMirroringGroupMirroMacStatus':hpnicfMirroringGroupMirroMacStatus,'hpnicfMirroringGroupMirrorVlanTable':hpnicfMirroringGroupMirrorVlanTable,'hpnicfMirroringGroupMirrorVlanEntry':hpnicfMirroringGroupMirrorVlanEntry,_AI:hpnicfMirroringGroupMirrorVlanSeq,'hpnicfMirroringGroupMirrorVlanID':hpnicfMirroringGroupMirrorVlanID,'hpnicfMirroringGroupMirrorVlanDirection':hpnicfMirroringGroupMirrorVlanDirection,'hpnicfMirroringGroupMirroVlanStatus':hpnicfMirroringGroupMirroVlanStatus,'hpnicfPortTrustTable':hpnicfPortTrustTable,'hpnicfPortTrustEntry':hpnicfPortTrustEntry,_AJ:hpnicfPortTrustIfIndex,'hpnicfPortTrustTrustType':hpnicfPortTrustTrustType,'hpnicfPortTrustOvercastType':hpnicfPortTrustOvercastType,'hpnicfPortTrustReset':hpnicfPortTrustReset,'hpnicfRemarkVlanIDTable':hpnicfRemarkVlanIDTable,'hpnicfRemarkVlanIDEntry':hpnicfRemarkVlanIDEntry,_AK:hpnicfRemarkVlanIDAclIndex,_AL:hpnicfRemarkVlanIDIfIndex,_AM:hpnicfRemarkVlanIDVlanID,_AN:hpnicfRemarkVlanIDDirection,'hpnicfRemarkVlanIDUserAclNum':hpnicfRemarkVlanIDUserAclNum,'hpnicfRemarkVlanIDUserAclRule':hpnicfRemarkVlanIDUserAclRule,'hpnicfRemarkVlanIDIpAclNum':hpnicfRemarkVlanIDIpAclNum,'hpnicfRemarkVlanIDIpAclRule':hpnicfRemarkVlanIDIpAclRule,'hpnicfRemarkVlanIDLinkAclNum':hpnicfRemarkVlanIDLinkAclNum,'hpnicfRemarkVlanIDLinkAclRule':hpnicfRemarkVlanIDLinkAclRule,'hpnicfRemarkVlanIDRemarkVlanID':hpnicfRemarkVlanIDRemarkVlanID,'hpnicfRemarkVlanIDPacketType':hpnicfRemarkVlanIDPacketType,'hpnicfRemarkVlanIDRowStatus':hpnicfRemarkVlanIDRowStatus,'hpnicfCosToDscpMapTable':hpnicfCosToDscpMapTable,'hpnicfCosToDscpMapEntry':hpnicfCosToDscpMapEntry,_AO:hpnicfCosToDscpMapCosIndex,'hpnicfCosToDscpMapDscpValue':hpnicfCosToDscpMapDscpValue,'hpnicfCosToDscpMapReSet':hpnicfCosToDscpMapReSet,'hpnicfDscpToLocalPreMapTable':hpnicfDscpToLocalPreMapTable,'hpnicfDscpToLocalPreMapEntry':hpnicfDscpToLocalPreMapEntry,_AP:hpnicfDscpToLocalPreMapDscpIndex,'hpnicfDscpToLocalPreMapLocalPreVal':hpnicfDscpToLocalPreMapLocalPreVal,'hpnicfDscpToLocalPreMapReset':hpnicfDscpToLocalPreMapReset,'hpnicfDscpToDropPreMapTable':hpnicfDscpToDropPreMapTable,'hpnicfDscpToDropPreMapEntry':hpnicfDscpToDropPreMapEntry,_AQ:hpnicfDscpToDropPreMapDscpIndex,'hpnicfDscpToDropPreMapDropPreVal':hpnicfDscpToDropPreMapDropPreVal,'hpnicfDscpToDropPreMapReset':hpnicfDscpToDropPreMapReset,'hpnicfDscpToCosMapTable':hpnicfDscpToCosMapTable,'hpnicfDscpToCosMapEntry':hpnicfDscpToCosMapEntry,_AR:hpnicfDscpToCosMapDscpIndex,'hpnicfDscpToCosMapCosValue':hpnicfDscpToCosMapCosValue,'hpnicfDscpToCosMapReset':hpnicfDscpToCosMapReset,'hpnicfDscpToDscpMapTable':hpnicfDscpToDscpMapTable,'hpnicfDscpToDscpMapEntry':hpnicfDscpToDscpMapEntry,_AS:hpnicfDscpToDscpMapDscpIndex,'hpnicfDscpToDscpMapDscpValue':hpnicfDscpToDscpMapDscpValue,'hpnicfDscpToDscpMapReset':hpnicfDscpToDscpMapReset})