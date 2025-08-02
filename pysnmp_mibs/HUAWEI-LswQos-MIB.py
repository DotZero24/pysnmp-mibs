_AS='hwDscpToDscpMapDscpIndex'
_AR='hwDscpToCosMapDscpIndex'
_AQ='hwDscpToDropPreMapDscpIndex'
_AP='hwDscpToLocalPreMapDscpIndex'
_AO='hwCosToDscpMapCosIndex'
_AN='hwRemarkVlanIDDirection'
_AM='hwRemarkVlanIDVlanID'
_AL='hwRemarkVlanIDIfIndex'
_AK='hwRemarkVlanIDAclIndex'
_AJ='hwPortTrustIfIndex'
_AI='hwMirroringGroupMirrorVlanSeq'
_AH='hwMirroringGroupMirrorMacSeq'
_AG='hwPortWredQueueID'
_AF='hwPortWredIfIndex'
_AE='hwLocalPrecedenceMapLocalPrecedenceIndex'
_AD='hwLocalPrecedenceMapConformLevel'
_AC='hwExpMapExpIndex'
_AB='hwExpMapConformLevel'
_AA='hwDscpMapDscpIndex'
_A9='hwDscpMapConformLevel'
_A8='hwCosToDropPrecedenceMapCosIndex'
_A7='hwCosToLocalPrecedenceMapCosIndex'
_A6='hwWredQueueId'
_A5='hwWredIndex'
_A4='hwDropModeIfIndex'
_A3='hwPortQueueQueueID'
_A2='hwPortQueueIfIndex'
_A1='hwTrafficShapeQueueId'
_A0='hwTrafficShapeIfIndex'
_z='hwFlowtempEnableVlanID'
_y='hwFlowtempEnableIfIndex'
_x='user-defined'
_w='hwFlowtempIndex'
_v='hwMirrorGroupID'
_u='hwRedDirection'
_t='hwRedVlanID'
_s='hwRedIfIndex'
_r='hwRedAclIndex'
_q='hwBandwidthDirection'
_p='hwBandwidthVlanID'
_o='hwBandwidthIfIndex'
_n='hwBandwidthAclIndex'
_m='hwLineRateDirection'
_l='hwLineRateIfIndex'
_k='hwPortMirrorIfIndex'
_j='hwMirrorDirection'
_i='hwMirrorVlanID'
_h='hwMirrorIfIndex'
_g='hwMirrorAclIndex'
_f='hwStatisticDirection'
_e='hwStatisticVlanID'
_d='hwStatisticIfIndex'
_c='hwStatisticAclIndex'
_b='hwRedirectDirection'
_a='hwRedirectVlanID'
_Z='hwRedirectIfIndex'
_Y='hwRedirectAclIndex'
_X='hwPriorityDirection'
_W='hwPriorityVlanID'
_V='hwPriorityIfIndex'
_U='hwPriorityAclIndex'
_T='hwRateLimitDirection'
_S='hwRateLimitVlanID'
_R='hwRateLimitIfIndex'
_Q='hwRateLimitAclIndex'
_P='hwQueueIfIndex'
_O='OctetString'
_N='default'
_M='TruthValue'
_L='reset'
_K='input'
_J='hwMirroringGroupID'
_I='output'
_H='invalid'
_G='not-accessible'
_F='read-only'
_E='read-write'
_D='HUAWEI-LswQos-MIB'
_C='read-create'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lswCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','lswCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_M)
hwLswQosAclMib=ModuleIdentity((1,3,6,1,4,1,2011,2,23,1,16))
if mibBuilder.loadTexts:hwLswQosAclMib.setRevisions(('2002-11-19 00:00',))
class HwMirrorOrMonitorType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('port',1),('board',2)))
_HwLswQosMibObject_ObjectIdentity=ObjectIdentity
hwLswQosMibObject=_HwLswQosMibObject_ObjectIdentity((1,3,6,1,4,1,2011,2,23,1,16,2))
class _HwPriorityTrustMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_N,0),('dscp',1),('ipprecedence',2),('cos',3),('localprecedence',4)))
_HwPriorityTrustMode_Type.__name__=_B
_HwPriorityTrustMode_Object=MibScalar
hwPriorityTrustMode=_HwPriorityTrustMode_Object((1,3,6,1,4,1,2011,2,23,1,16,2,1),_HwPriorityTrustMode_Type())
hwPriorityTrustMode.setMaxAccess(_E)
if mibBuilder.loadTexts:hwPriorityTrustMode.setStatus(_A)
class _HwPortMonitorBothIfIndex_Type(Integer32):defaultValue=0
_HwPortMonitorBothIfIndex_Type.__name__=_B
_HwPortMonitorBothIfIndex_Object=MibScalar
hwPortMonitorBothIfIndex=_HwPortMonitorBothIfIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,2),_HwPortMonitorBothIfIndex_Type())
hwPortMonitorBothIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hwPortMonitorBothIfIndex.setStatus(_A)
_HwQueueTable_Object=MibTable
hwQueueTable=_HwQueueTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,3))
if mibBuilder.loadTexts:hwQueueTable.setStatus(_A)
_HwQueueEntry_Object=MibTableRow
hwQueueEntry=_HwQueueEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,3,1))
hwQueueEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:hwQueueEntry.setStatus(_A)
_HwQueueIfIndex_Type=Integer32
_HwQueueIfIndex_Object=MibTableColumn
hwQueueIfIndex=_HwQueueIfIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,3,1,1),_HwQueueIfIndex_Type())
hwQueueIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hwQueueIfIndex.setStatus(_A)
class _HwQueueScheduleMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('sp',1),('wrr',2),('wrr-max-delay',3),('sc-0',4),('sc-1',5),('sc-2',6),('rr',7),('wfq',8),('hq-wrr',9)))
_HwQueueScheduleMode_Type.__name__=_B
_HwQueueScheduleMode_Object=MibTableColumn
hwQueueScheduleMode=_HwQueueScheduleMode_Object((1,3,6,1,4,1,2011,2,23,1,16,2,3,1,2),_HwQueueScheduleMode_Type())
hwQueueScheduleMode.setMaxAccess(_E)
if mibBuilder.loadTexts:hwQueueScheduleMode.setStatus(_A)
_HwQueueWeight1_Type=Integer32
_HwQueueWeight1_Object=MibTableColumn
hwQueueWeight1=_HwQueueWeight1_Object((1,3,6,1,4,1,2011,2,23,1,16,2,3,1,3),_HwQueueWeight1_Type())
hwQueueWeight1.setMaxAccess(_E)
if mibBuilder.loadTexts:hwQueueWeight1.setStatus(_A)
_HwQueueWeight2_Type=Integer32
_HwQueueWeight2_Object=MibTableColumn
hwQueueWeight2=_HwQueueWeight2_Object((1,3,6,1,4,1,2011,2,23,1,16,2,3,1,4),_HwQueueWeight2_Type())
hwQueueWeight2.setMaxAccess(_E)
if mibBuilder.loadTexts:hwQueueWeight2.setStatus(_A)
_HwQueueWeight3_Type=Integer32
_HwQueueWeight3_Object=MibTableColumn
hwQueueWeight3=_HwQueueWeight3_Object((1,3,6,1,4,1,2011,2,23,1,16,2,3,1,5),_HwQueueWeight3_Type())
hwQueueWeight3.setMaxAccess(_E)
if mibBuilder.loadTexts:hwQueueWeight3.setStatus(_A)
_HwQueueWeight4_Type=Integer32
_HwQueueWeight4_Object=MibTableColumn
hwQueueWeight4=_HwQueueWeight4_Object((1,3,6,1,4,1,2011,2,23,1,16,2,3,1,6),_HwQueueWeight4_Type())
hwQueueWeight4.setMaxAccess(_E)
if mibBuilder.loadTexts:hwQueueWeight4.setStatus(_A)
class _HwQueueMaxDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HwQueueMaxDelay_Type.__name__=_B
_HwQueueMaxDelay_Object=MibTableColumn
hwQueueMaxDelay=_HwQueueMaxDelay_Object((1,3,6,1,4,1,2011,2,23,1,16,2,3,1,7),_HwQueueMaxDelay_Type())
hwQueueMaxDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:hwQueueMaxDelay.setStatus(_A)
_HwQueueWeight5_Type=Integer32
_HwQueueWeight5_Object=MibTableColumn
hwQueueWeight5=_HwQueueWeight5_Object((1,3,6,1,4,1,2011,2,23,1,16,2,3,1,8),_HwQueueWeight5_Type())
hwQueueWeight5.setMaxAccess(_E)
if mibBuilder.loadTexts:hwQueueWeight5.setStatus(_A)
_HwQueueWeight6_Type=Integer32
_HwQueueWeight6_Object=MibTableColumn
hwQueueWeight6=_HwQueueWeight6_Object((1,3,6,1,4,1,2011,2,23,1,16,2,3,1,9),_HwQueueWeight6_Type())
hwQueueWeight6.setMaxAccess(_E)
if mibBuilder.loadTexts:hwQueueWeight6.setStatus(_A)
_HwQueueWeight7_Type=Integer32
_HwQueueWeight7_Object=MibTableColumn
hwQueueWeight7=_HwQueueWeight7_Object((1,3,6,1,4,1,2011,2,23,1,16,2,3,1,10),_HwQueueWeight7_Type())
hwQueueWeight7.setMaxAccess(_E)
if mibBuilder.loadTexts:hwQueueWeight7.setStatus(_A)
_HwQueueWeight8_Type=Integer32
_HwQueueWeight8_Object=MibTableColumn
hwQueueWeight8=_HwQueueWeight8_Object((1,3,6,1,4,1,2011,2,23,1,16,2,3,1,11),_HwQueueWeight8_Type())
hwQueueWeight8.setMaxAccess(_E)
if mibBuilder.loadTexts:hwQueueWeight8.setStatus(_A)
_HwRateLimitTable_Object=MibTable
hwRateLimitTable=_HwRateLimitTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4))
if mibBuilder.loadTexts:hwRateLimitTable.setStatus(_A)
_HwRateLimitEntry_Object=MibTableRow
hwRateLimitEntry=_HwRateLimitEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1))
hwRateLimitEntry.setIndexNames((0,_D,_Q),(0,_D,_R),(0,_D,_S),(0,_D,_T))
if mibBuilder.loadTexts:hwRateLimitEntry.setStatus(_A)
class _HwRateLimitAclIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2999))
_HwRateLimitAclIndex_Type.__name__=_B
_HwRateLimitAclIndex_Object=MibTableColumn
hwRateLimitAclIndex=_HwRateLimitAclIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,1),_HwRateLimitAclIndex_Type())
hwRateLimitAclIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitAclIndex.setStatus(_A)
_HwRateLimitIfIndex_Type=Integer32
_HwRateLimitIfIndex_Object=MibTableColumn
hwRateLimitIfIndex=_HwRateLimitIfIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,2),_HwRateLimitIfIndex_Type())
hwRateLimitIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitIfIndex.setStatus(_A)
class _HwRateLimitVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HwRateLimitVlanID_Type.__name__=_B
_HwRateLimitVlanID_Object=MibTableColumn
hwRateLimitVlanID=_HwRateLimitVlanID_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,3),_HwRateLimitVlanID_Type())
hwRateLimitVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitVlanID.setStatus(_A)
class _HwRateLimitDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_K,1),(_I,2)))
_HwRateLimitDirection_Type.__name__=_B
_HwRateLimitDirection_Object=MibTableColumn
hwRateLimitDirection=_HwRateLimitDirection_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,4),_HwRateLimitDirection_Type())
hwRateLimitDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitDirection.setStatus(_A)
class _HwRateLimitUserAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5000,5999),ValueRangeConstraint(10000,12999))
_HwRateLimitUserAclNum_Type.__name__=_B
_HwRateLimitUserAclNum_Object=MibTableColumn
hwRateLimitUserAclNum=_HwRateLimitUserAclNum_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,5),_HwRateLimitUserAclNum_Type())
hwRateLimitUserAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitUserAclNum.setStatus(_A)
class _HwRateLimitUserAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwRateLimitUserAclRule_Type.__name__=_B
_HwRateLimitUserAclRule_Object=MibTableColumn
hwRateLimitUserAclRule=_HwRateLimitUserAclRule_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,6),_HwRateLimitUserAclRule_Type())
hwRateLimitUserAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitUserAclRule.setStatus(_A)
class _HwRateLimitIpAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999),ValueRangeConstraint(10000,12999))
_HwRateLimitIpAclNum_Type.__name__=_B
_HwRateLimitIpAclNum_Object=MibTableColumn
hwRateLimitIpAclNum=_HwRateLimitIpAclNum_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,7),_HwRateLimitIpAclNum_Type())
hwRateLimitIpAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitIpAclNum.setStatus(_A)
class _HwRateLimitIpAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwRateLimitIpAclRule_Type.__name__=_B
_HwRateLimitIpAclRule_Object=MibTableColumn
hwRateLimitIpAclRule=_HwRateLimitIpAclRule_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,8),_HwRateLimitIpAclRule_Type())
hwRateLimitIpAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitIpAclRule.setStatus(_A)
class _HwRateLimitLinkAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4000,4999),ValueRangeConstraint(10000,12999))
_HwRateLimitLinkAclNum_Type.__name__=_B
_HwRateLimitLinkAclNum_Object=MibTableColumn
hwRateLimitLinkAclNum=_HwRateLimitLinkAclNum_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,9),_HwRateLimitLinkAclNum_Type())
hwRateLimitLinkAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitLinkAclNum.setStatus(_A)
class _HwRateLimitLinkAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwRateLimitLinkAclRule_Type.__name__=_B
_HwRateLimitLinkAclRule_Object=MibTableColumn
hwRateLimitLinkAclRule=_HwRateLimitLinkAclRule_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,10),_HwRateLimitLinkAclRule_Type())
hwRateLimitLinkAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitLinkAclRule.setStatus(_A)
_HwRateLimitTargetRateMbps_Type=Integer32
_HwRateLimitTargetRateMbps_Object=MibTableColumn
hwRateLimitTargetRateMbps=_HwRateLimitTargetRateMbps_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,11),_HwRateLimitTargetRateMbps_Type())
hwRateLimitTargetRateMbps.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitTargetRateMbps.setStatus(_A)
_HwRateLimitTargetRateKbps_Type=Integer32
_HwRateLimitTargetRateKbps_Object=MibTableColumn
hwRateLimitTargetRateKbps=_HwRateLimitTargetRateKbps_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,12),_HwRateLimitTargetRateKbps_Type())
hwRateLimitTargetRateKbps.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitTargetRateKbps.setStatus(_A)
class _HwRateLimitPeakRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(64,8388608))
_HwRateLimitPeakRate_Type.__name__=_B
_HwRateLimitPeakRate_Object=MibTableColumn
hwRateLimitPeakRate=_HwRateLimitPeakRate_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,13),_HwRateLimitPeakRate_Type())
hwRateLimitPeakRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitPeakRate.setStatus(_A)
class _HwRateLimitCIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,34120000))
_HwRateLimitCIR_Type.__name__=_B
_HwRateLimitCIR_Object=MibTableColumn
hwRateLimitCIR=_HwRateLimitCIR_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,14),_HwRateLimitCIR_Type())
hwRateLimitCIR.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitCIR.setStatus(_A)
class _HwRateLimitCBS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1048575))
_HwRateLimitCBS_Type.__name__=_B
_HwRateLimitCBS_Object=MibTableColumn
hwRateLimitCBS=_HwRateLimitCBS_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,15),_HwRateLimitCBS_Type())
hwRateLimitCBS.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitCBS.setStatus(_A)
class _HwRateLimitEBS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,268435455))
_HwRateLimitEBS_Type.__name__=_B
_HwRateLimitEBS_Object=MibTableColumn
hwRateLimitEBS=_HwRateLimitEBS_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,16),_HwRateLimitEBS_Type())
hwRateLimitEBS.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitEBS.setStatus(_A)
class _HwRateLimitPIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,34120000))
_HwRateLimitPIR_Type.__name__=_B
_HwRateLimitPIR_Object=MibTableColumn
hwRateLimitPIR=_HwRateLimitPIR_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,17),_HwRateLimitPIR_Type())
hwRateLimitPIR.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitPIR.setStatus(_A)
class _HwRateLimitConformLocalPre_Type(Integer32):defaultValue=1
_HwRateLimitConformLocalPre_Type.__name__=_B
_HwRateLimitConformLocalPre_Object=MibTableColumn
hwRateLimitConformLocalPre=_HwRateLimitConformLocalPre_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,18),_HwRateLimitConformLocalPre_Type())
hwRateLimitConformLocalPre.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitConformLocalPre.setStatus(_A)
class _HwRateLimitConformActionType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_H,0),('remark-cos',1),('remark-drop-priority',2),('remark-cos-drop-priority',3),('remark-policed-service',4),('remark-dscp',5)))
_HwRateLimitConformActionType_Type.__name__=_B
_HwRateLimitConformActionType_Object=MibTableColumn
hwRateLimitConformActionType=_HwRateLimitConformActionType_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,19),_HwRateLimitConformActionType_Type())
hwRateLimitConformActionType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitConformActionType.setStatus(_A)
class _HwRateLimitExceedActionType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_H,0),('forward',1),('drop',2),('remarkdscp',3),('exceed-cos',4)))
_HwRateLimitExceedActionType_Type.__name__=_B
_HwRateLimitExceedActionType_Object=MibTableColumn
hwRateLimitExceedActionType=_HwRateLimitExceedActionType_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,20),_HwRateLimitExceedActionType_Type())
hwRateLimitExceedActionType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitExceedActionType.setStatus(_A)
class _HwRateLimitExceedDscp_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HwRateLimitExceedDscp_Type.__name__=_B
_HwRateLimitExceedDscp_Object=MibTableColumn
hwRateLimitExceedDscp=_HwRateLimitExceedDscp_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,21),_HwRateLimitExceedDscp_Type())
hwRateLimitExceedDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitExceedDscp.setStatus(_A)
_HwRateLimitRuntime_Type=TruthValue
_HwRateLimitRuntime_Object=MibTableColumn
hwRateLimitRuntime=_HwRateLimitRuntime_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,22),_HwRateLimitRuntime_Type())
hwRateLimitRuntime.setMaxAccess(_F)
if mibBuilder.loadTexts:hwRateLimitRuntime.setStatus(_A)
_HwRateLimitRowStatus_Type=RowStatus
_HwRateLimitRowStatus_Object=MibTableColumn
hwRateLimitRowStatus=_HwRateLimitRowStatus_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,23),_HwRateLimitRowStatus_Type())
hwRateLimitRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitRowStatus.setStatus(_A)
class _HwRateLimitExceedCos_Type(Integer32):defaultValue=255
_HwRateLimitExceedCos_Type.__name__=_B
_HwRateLimitExceedCos_Object=MibTableColumn
hwRateLimitExceedCos=_HwRateLimitExceedCos_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,24),_HwRateLimitExceedCos_Type())
hwRateLimitExceedCos.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitExceedCos.setStatus(_A)
class _HwRateLimitConformCos_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HwRateLimitConformCos_Type.__name__=_B
_HwRateLimitConformCos_Object=MibTableColumn
hwRateLimitConformCos=_HwRateLimitConformCos_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,25),_HwRateLimitConformCos_Type())
hwRateLimitConformCos.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitConformCos.setStatus(_A)
class _HwRateLimitConformDscp_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HwRateLimitConformDscp_Type.__name__=_B
_HwRateLimitConformDscp_Object=MibTableColumn
hwRateLimitConformDscp=_HwRateLimitConformDscp_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,26),_HwRateLimitConformDscp_Type())
hwRateLimitConformDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitConformDscp.setStatus(_A)
_HwRateLimitMeterStatByteCount_Type=Counter64
_HwRateLimitMeterStatByteCount_Object=MibTableColumn
hwRateLimitMeterStatByteCount=_HwRateLimitMeterStatByteCount_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,27),_HwRateLimitMeterStatByteCount_Type())
hwRateLimitMeterStatByteCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hwRateLimitMeterStatByteCount.setStatus(_A)
_HwRateLimitMeterStatByteXCount_Type=Counter64
_HwRateLimitMeterStatByteXCount_Object=MibTableColumn
hwRateLimitMeterStatByteXCount=_HwRateLimitMeterStatByteXCount_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,28),_HwRateLimitMeterStatByteXCount_Type())
hwRateLimitMeterStatByteXCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hwRateLimitMeterStatByteXCount.setStatus(_A)
class _HwRateLimitMeterStatState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('set',1),('unDo',2),(_L,3),('running',4),('notRunning',5)))
_HwRateLimitMeterStatState_Type.__name__=_B
_HwRateLimitMeterStatState_Object=MibTableColumn
hwRateLimitMeterStatState=_HwRateLimitMeterStatState_Object((1,3,6,1,4,1,2011,2,23,1,16,2,4,1,29),_HwRateLimitMeterStatState_Type())
hwRateLimitMeterStatState.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRateLimitMeterStatState.setStatus(_A)
_HwPriorityTable_Object=MibTable
hwPriorityTable=_HwPriorityTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5))
if mibBuilder.loadTexts:hwPriorityTable.setStatus(_A)
_HwPriorityEntry_Object=MibTableRow
hwPriorityEntry=_HwPriorityEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5,1))
hwPriorityEntry.setIndexNames((0,_D,_U),(0,_D,_V),(0,_D,_W),(0,_D,_X))
if mibBuilder.loadTexts:hwPriorityEntry.setStatus(_A)
class _HwPriorityAclIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2999))
_HwPriorityAclIndex_Type.__name__=_B
_HwPriorityAclIndex_Object=MibTableColumn
hwPriorityAclIndex=_HwPriorityAclIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5,1,1),_HwPriorityAclIndex_Type())
hwPriorityAclIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPriorityAclIndex.setStatus(_A)
_HwPriorityIfIndex_Type=Integer32
_HwPriorityIfIndex_Object=MibTableColumn
hwPriorityIfIndex=_HwPriorityIfIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5,1,2),_HwPriorityIfIndex_Type())
hwPriorityIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPriorityIfIndex.setStatus(_A)
class _HwPriorityVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HwPriorityVlanID_Type.__name__=_B
_HwPriorityVlanID_Object=MibTableColumn
hwPriorityVlanID=_HwPriorityVlanID_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5,1,3),_HwPriorityVlanID_Type())
hwPriorityVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPriorityVlanID.setStatus(_A)
class _HwPriorityDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_K,1),(_I,2)))
_HwPriorityDirection_Type.__name__=_B
_HwPriorityDirection_Object=MibTableColumn
hwPriorityDirection=_HwPriorityDirection_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5,1,4),_HwPriorityDirection_Type())
hwPriorityDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPriorityDirection.setStatus(_A)
class _HwPriorityUserAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5000,5999),ValueRangeConstraint(10000,12999))
_HwPriorityUserAclNum_Type.__name__=_B
_HwPriorityUserAclNum_Object=MibTableColumn
hwPriorityUserAclNum=_HwPriorityUserAclNum_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5,1,5),_HwPriorityUserAclNum_Type())
hwPriorityUserAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPriorityUserAclNum.setStatus(_A)
class _HwPriorityUserAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwPriorityUserAclRule_Type.__name__=_B
_HwPriorityUserAclRule_Object=MibTableColumn
hwPriorityUserAclRule=_HwPriorityUserAclRule_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5,1,6),_HwPriorityUserAclRule_Type())
hwPriorityUserAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPriorityUserAclRule.setStatus(_A)
class _HwPriorityIpAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999),ValueRangeConstraint(10000,12999))
_HwPriorityIpAclNum_Type.__name__=_B
_HwPriorityIpAclNum_Object=MibTableColumn
hwPriorityIpAclNum=_HwPriorityIpAclNum_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5,1,7),_HwPriorityIpAclNum_Type())
hwPriorityIpAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPriorityIpAclNum.setStatus(_A)
class _HwPriorityIpAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwPriorityIpAclRule_Type.__name__=_B
_HwPriorityIpAclRule_Object=MibTableColumn
hwPriorityIpAclRule=_HwPriorityIpAclRule_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5,1,8),_HwPriorityIpAclRule_Type())
hwPriorityIpAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPriorityIpAclRule.setStatus(_A)
class _HwPriorityLinkAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4000,4999),ValueRangeConstraint(10000,12999))
_HwPriorityLinkAclNum_Type.__name__=_B
_HwPriorityLinkAclNum_Object=MibTableColumn
hwPriorityLinkAclNum=_HwPriorityLinkAclNum_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5,1,9),_HwPriorityLinkAclNum_Type())
hwPriorityLinkAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPriorityLinkAclNum.setStatus(_A)
class _HwPriorityLinkAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwPriorityLinkAclRule_Type.__name__=_B
_HwPriorityLinkAclRule_Object=MibTableColumn
hwPriorityLinkAclRule=_HwPriorityLinkAclRule_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5,1,10),_HwPriorityLinkAclRule_Type())
hwPriorityLinkAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPriorityLinkAclRule.setStatus(_A)
class _HwPriorityDscp_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HwPriorityDscp_Type.__name__=_B
_HwPriorityDscp_Object=MibTableColumn
hwPriorityDscp=_HwPriorityDscp_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5,1,11),_HwPriorityDscp_Type())
hwPriorityDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPriorityDscp.setStatus(_A)
class _HwPriorityIpPre_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HwPriorityIpPre_Type.__name__=_B
_HwPriorityIpPre_Object=MibTableColumn
hwPriorityIpPre=_HwPriorityIpPre_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5,1,12),_HwPriorityIpPre_Type())
hwPriorityIpPre.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPriorityIpPre.setStatus(_A)
class _HwPriorityIpPreFromCos_Type(TruthValue):defaultValue=2
_HwPriorityIpPreFromCos_Type.__name__=_M
_HwPriorityIpPreFromCos_Object=MibTableColumn
hwPriorityIpPreFromCos=_HwPriorityIpPreFromCos_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5,1,13),_HwPriorityIpPreFromCos_Type())
hwPriorityIpPreFromCos.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPriorityIpPreFromCos.setStatus(_A)
class _HwPriorityCos_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HwPriorityCos_Type.__name__=_B
_HwPriorityCos_Object=MibTableColumn
hwPriorityCos=_HwPriorityCos_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5,1,14),_HwPriorityCos_Type())
hwPriorityCos.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPriorityCos.setStatus(_A)
class _HwPriorityCosFromIpPre_Type(TruthValue):defaultValue=2
_HwPriorityCosFromIpPre_Type.__name__=_M
_HwPriorityCosFromIpPre_Object=MibTableColumn
hwPriorityCosFromIpPre=_HwPriorityCosFromIpPre_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5,1,15),_HwPriorityCosFromIpPre_Type())
hwPriorityCosFromIpPre.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPriorityCosFromIpPre.setStatus(_A)
class _HwPriorityLocalPre_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HwPriorityLocalPre_Type.__name__=_B
_HwPriorityLocalPre_Object=MibTableColumn
hwPriorityLocalPre=_HwPriorityLocalPre_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5,1,16),_HwPriorityLocalPre_Type())
hwPriorityLocalPre.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPriorityLocalPre.setStatus(_A)
class _HwPriorityPolicedServiceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_H,0),('auto',1),('trust-dscp',2),('new-dscp',3),('untrusted',4)))
_HwPriorityPolicedServiceType_Type.__name__=_B
_HwPriorityPolicedServiceType_Object=MibTableColumn
hwPriorityPolicedServiceType=_HwPriorityPolicedServiceType_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5,1,17),_HwPriorityPolicedServiceType_Type())
hwPriorityPolicedServiceType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPriorityPolicedServiceType.setStatus(_A)
class _HwPriorityPolicedServiceDscp_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HwPriorityPolicedServiceDscp_Type.__name__=_B
_HwPriorityPolicedServiceDscp_Object=MibTableColumn
hwPriorityPolicedServiceDscp=_HwPriorityPolicedServiceDscp_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5,1,18),_HwPriorityPolicedServiceDscp_Type())
hwPriorityPolicedServiceDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPriorityPolicedServiceDscp.setStatus(_A)
class _HwPriorityPolicedServiceExp_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HwPriorityPolicedServiceExp_Type.__name__=_B
_HwPriorityPolicedServiceExp_Object=MibTableColumn
hwPriorityPolicedServiceExp=_HwPriorityPolicedServiceExp_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5,1,19),_HwPriorityPolicedServiceExp_Type())
hwPriorityPolicedServiceExp.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPriorityPolicedServiceExp.setStatus(_A)
class _HwPriorityPolicedServiceCos_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HwPriorityPolicedServiceCos_Type.__name__=_B
_HwPriorityPolicedServiceCos_Object=MibTableColumn
hwPriorityPolicedServiceCos=_HwPriorityPolicedServiceCos_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5,1,20),_HwPriorityPolicedServiceCos_Type())
hwPriorityPolicedServiceCos.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPriorityPolicedServiceCos.setStatus(_A)
class _HwPriorityPolicedServiceLoaclPre_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HwPriorityPolicedServiceLoaclPre_Type.__name__=_B
_HwPriorityPolicedServiceLoaclPre_Object=MibTableColumn
hwPriorityPolicedServiceLoaclPre=_HwPriorityPolicedServiceLoaclPre_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5,1,21),_HwPriorityPolicedServiceLoaclPre_Type())
hwPriorityPolicedServiceLoaclPre.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPriorityPolicedServiceLoaclPre.setStatus(_A)
class _HwPriorityPolicedServiceDropPriority_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2),ValueRangeConstraint(255,255))
_HwPriorityPolicedServiceDropPriority_Type.__name__=_B
_HwPriorityPolicedServiceDropPriority_Object=MibTableColumn
hwPriorityPolicedServiceDropPriority=_HwPriorityPolicedServiceDropPriority_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5,1,22),_HwPriorityPolicedServiceDropPriority_Type())
hwPriorityPolicedServiceDropPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPriorityPolicedServiceDropPriority.setStatus(_A)
_HwPriorityRuntime_Type=TruthValue
_HwPriorityRuntime_Object=MibTableColumn
hwPriorityRuntime=_HwPriorityRuntime_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5,1,23),_HwPriorityRuntime_Type())
hwPriorityRuntime.setMaxAccess(_F)
if mibBuilder.loadTexts:hwPriorityRuntime.setStatus(_A)
_HwPriorityRowStatus_Type=RowStatus
_HwPriorityRowStatus_Object=MibTableColumn
hwPriorityRowStatus=_HwPriorityRowStatus_Object((1,3,6,1,4,1,2011,2,23,1,16,2,5,1,24),_HwPriorityRowStatus_Type())
hwPriorityRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPriorityRowStatus.setStatus(_A)
_HwRedirectTable_Object=MibTable
hwRedirectTable=_HwRedirectTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6))
if mibBuilder.loadTexts:hwRedirectTable.setStatus(_A)
_HwRedirectEntry_Object=MibTableRow
hwRedirectEntry=_HwRedirectEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1))
hwRedirectEntry.setIndexNames((0,_D,_Y),(0,_D,_Z),(0,_D,_a),(0,_D,_b))
if mibBuilder.loadTexts:hwRedirectEntry.setStatus(_A)
class _HwRedirectAclIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2999))
_HwRedirectAclIndex_Type.__name__=_B
_HwRedirectAclIndex_Object=MibTableColumn
hwRedirectAclIndex=_HwRedirectAclIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1,1),_HwRedirectAclIndex_Type())
hwRedirectAclIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedirectAclIndex.setStatus(_A)
_HwRedirectIfIndex_Type=Integer32
_HwRedirectIfIndex_Object=MibTableColumn
hwRedirectIfIndex=_HwRedirectIfIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1,2),_HwRedirectIfIndex_Type())
hwRedirectIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedirectIfIndex.setStatus(_A)
class _HwRedirectVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HwRedirectVlanID_Type.__name__=_B
_HwRedirectVlanID_Object=MibTableColumn
hwRedirectVlanID=_HwRedirectVlanID_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1,3),_HwRedirectVlanID_Type())
hwRedirectVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedirectVlanID.setStatus(_A)
class _HwRedirectDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_K,1),(_I,2)))
_HwRedirectDirection_Type.__name__=_B
_HwRedirectDirection_Object=MibTableColumn
hwRedirectDirection=_HwRedirectDirection_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1,4),_HwRedirectDirection_Type())
hwRedirectDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedirectDirection.setStatus(_A)
class _HwRedirectUserAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5000,5999),ValueRangeConstraint(10000,12999))
_HwRedirectUserAclNum_Type.__name__=_B
_HwRedirectUserAclNum_Object=MibTableColumn
hwRedirectUserAclNum=_HwRedirectUserAclNum_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1,5),_HwRedirectUserAclNum_Type())
hwRedirectUserAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedirectUserAclNum.setStatus(_A)
class _HwRedirectUserAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwRedirectUserAclRule_Type.__name__=_B
_HwRedirectUserAclRule_Object=MibTableColumn
hwRedirectUserAclRule=_HwRedirectUserAclRule_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1,6),_HwRedirectUserAclRule_Type())
hwRedirectUserAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedirectUserAclRule.setStatus(_A)
class _HwRedirectIpAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999),ValueRangeConstraint(10000,12999))
_HwRedirectIpAclNum_Type.__name__=_B
_HwRedirectIpAclNum_Object=MibTableColumn
hwRedirectIpAclNum=_HwRedirectIpAclNum_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1,7),_HwRedirectIpAclNum_Type())
hwRedirectIpAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedirectIpAclNum.setStatus(_A)
class _HwRedirectIpAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwRedirectIpAclRule_Type.__name__=_B
_HwRedirectIpAclRule_Object=MibTableColumn
hwRedirectIpAclRule=_HwRedirectIpAclRule_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1,8),_HwRedirectIpAclRule_Type())
hwRedirectIpAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedirectIpAclRule.setStatus(_A)
class _HwRedirectLinkAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4000,4999),ValueRangeConstraint(10000,12999))
_HwRedirectLinkAclNum_Type.__name__=_B
_HwRedirectLinkAclNum_Object=MibTableColumn
hwRedirectLinkAclNum=_HwRedirectLinkAclNum_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1,9),_HwRedirectLinkAclNum_Type())
hwRedirectLinkAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedirectLinkAclNum.setStatus(_A)
class _HwRedirectLinkAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwRedirectLinkAclRule_Type.__name__=_B
_HwRedirectLinkAclRule_Object=MibTableColumn
hwRedirectLinkAclRule=_HwRedirectLinkAclRule_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1,10),_HwRedirectLinkAclRule_Type())
hwRedirectLinkAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedirectLinkAclRule.setStatus(_A)
class _HwRedirectToCpu_Type(TruthValue):defaultValue=2
_HwRedirectToCpu_Type.__name__=_M
_HwRedirectToCpu_Object=MibTableColumn
hwRedirectToCpu=_HwRedirectToCpu_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1,11),_HwRedirectToCpu_Type())
hwRedirectToCpu.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedirectToCpu.setStatus(_A)
_HwRedirectToIfIndex_Type=Integer32
_HwRedirectToIfIndex_Object=MibTableColumn
hwRedirectToIfIndex=_HwRedirectToIfIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1,12),_HwRedirectToIfIndex_Type())
hwRedirectToIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedirectToIfIndex.setStatus(_A)
_HwRedirectToNextHop1_Type=IpAddress
_HwRedirectToNextHop1_Object=MibTableColumn
hwRedirectToNextHop1=_HwRedirectToNextHop1_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1,13),_HwRedirectToNextHop1_Type())
hwRedirectToNextHop1.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedirectToNextHop1.setStatus(_A)
_HwRedirectToNextHop2_Type=IpAddress
_HwRedirectToNextHop2_Object=MibTableColumn
hwRedirectToNextHop2=_HwRedirectToNextHop2_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1,14),_HwRedirectToNextHop2_Type())
hwRedirectToNextHop2.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedirectToNextHop2.setStatus(_A)
_HwRedirectRuntime_Type=TruthValue
_HwRedirectRuntime_Object=MibTableColumn
hwRedirectRuntime=_HwRedirectRuntime_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1,15),_HwRedirectRuntime_Type())
hwRedirectRuntime.setMaxAccess(_F)
if mibBuilder.loadTexts:hwRedirectRuntime.setStatus(_A)
_HwRedirectRowStatus_Type=RowStatus
_HwRedirectRowStatus_Object=MibTableColumn
hwRedirectRowStatus=_HwRedirectRowStatus_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1,16),_HwRedirectRowStatus_Type())
hwRedirectRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedirectRowStatus.setStatus(_A)
class _HwRedirectToSlotNo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HwRedirectToSlotNo_Type.__name__=_B
_HwRedirectToSlotNo_Object=MibTableColumn
hwRedirectToSlotNo=_HwRedirectToSlotNo_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1,17),_HwRedirectToSlotNo_Type())
hwRedirectToSlotNo.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedirectToSlotNo.setStatus(_A)
class _HwRedirectRemarkedDSCP_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HwRedirectRemarkedDSCP_Type.__name__=_B
_HwRedirectRemarkedDSCP_Object=MibTableColumn
hwRedirectRemarkedDSCP=_HwRedirectRemarkedDSCP_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1,18),_HwRedirectRemarkedDSCP_Type())
hwRedirectRemarkedDSCP.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedirectRemarkedDSCP.setStatus(_A)
class _HwRedirectRemarkedPri_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HwRedirectRemarkedPri_Type.__name__=_B
_HwRedirectRemarkedPri_Object=MibTableColumn
hwRedirectRemarkedPri=_HwRedirectRemarkedPri_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1,19),_HwRedirectRemarkedPri_Type())
hwRedirectRemarkedPri.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedirectRemarkedPri.setStatus(_A)
class _HwRedirectRemarkedTos_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15),ValueRangeConstraint(255,255))
_HwRedirectRemarkedTos_Type.__name__=_B
_HwRedirectRemarkedTos_Object=MibTableColumn
hwRedirectRemarkedTos=_HwRedirectRemarkedTos_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1,20),_HwRedirectRemarkedTos_Type())
hwRedirectRemarkedTos.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedirectRemarkedTos.setStatus(_A)
_HwRedirectToNextHop3_Type=IpAddress
_HwRedirectToNextHop3_Object=MibTableColumn
hwRedirectToNextHop3=_HwRedirectToNextHop3_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1,21),_HwRedirectToNextHop3_Type())
hwRedirectToNextHop3.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedirectToNextHop3.setStatus(_A)
class _HwRedirectTargetVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HwRedirectTargetVlanID_Type.__name__=_B
_HwRedirectTargetVlanID_Object=MibTableColumn
hwRedirectTargetVlanID=_HwRedirectTargetVlanID_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1,22),_HwRedirectTargetVlanID_Type())
hwRedirectTargetVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedirectTargetVlanID.setStatus(_A)
class _HwRedirectMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('strict-priority',1),('load-balance',2)))
_HwRedirectMode_Type.__name__=_B
_HwRedirectMode_Object=MibTableColumn
hwRedirectMode=_HwRedirectMode_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1,23),_HwRedirectMode_Type())
hwRedirectMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedirectMode.setStatus(_A)
class _HwRedirectToNestedVlanID_Type(Integer32):defaultValue=0
_HwRedirectToNestedVlanID_Type.__name__=_B
_HwRedirectToNestedVlanID_Object=MibTableColumn
hwRedirectToNestedVlanID=_HwRedirectToNestedVlanID_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1,24),_HwRedirectToNestedVlanID_Type())
hwRedirectToNestedVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedirectToNestedVlanID.setStatus(_A)
class _HwRedirectToModifiedVlanID_Type(Integer32):defaultValue=0
_HwRedirectToModifiedVlanID_Type.__name__=_B
_HwRedirectToModifiedVlanID_Object=MibTableColumn
hwRedirectToModifiedVlanID=_HwRedirectToModifiedVlanID_Object((1,3,6,1,4,1,2011,2,23,1,16,2,6,1,25),_HwRedirectToModifiedVlanID_Type())
hwRedirectToModifiedVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedirectToModifiedVlanID.setStatus(_A)
_HwStatisticTable_Object=MibTable
hwStatisticTable=_HwStatisticTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,7))
if mibBuilder.loadTexts:hwStatisticTable.setStatus(_A)
_HwStatisticEntry_Object=MibTableRow
hwStatisticEntry=_HwStatisticEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,7,1))
hwStatisticEntry.setIndexNames((0,_D,_c),(0,_D,_d),(0,_D,_e),(0,_D,_f))
if mibBuilder.loadTexts:hwStatisticEntry.setStatus(_A)
class _HwStatisticAclIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2999))
_HwStatisticAclIndex_Type.__name__=_B
_HwStatisticAclIndex_Object=MibTableColumn
hwStatisticAclIndex=_HwStatisticAclIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,7,1,1),_HwStatisticAclIndex_Type())
hwStatisticAclIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStatisticAclIndex.setStatus(_A)
_HwStatisticIfIndex_Type=Integer32
_HwStatisticIfIndex_Object=MibTableColumn
hwStatisticIfIndex=_HwStatisticIfIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,7,1,2),_HwStatisticIfIndex_Type())
hwStatisticIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStatisticIfIndex.setStatus(_A)
class _HwStatisticVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HwStatisticVlanID_Type.__name__=_B
_HwStatisticVlanID_Object=MibTableColumn
hwStatisticVlanID=_HwStatisticVlanID_Object((1,3,6,1,4,1,2011,2,23,1,16,2,7,1,3),_HwStatisticVlanID_Type())
hwStatisticVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStatisticVlanID.setStatus(_A)
class _HwStatisticDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_K,1),(_I,2)))
_HwStatisticDirection_Type.__name__=_B
_HwStatisticDirection_Object=MibTableColumn
hwStatisticDirection=_HwStatisticDirection_Object((1,3,6,1,4,1,2011,2,23,1,16,2,7,1,4),_HwStatisticDirection_Type())
hwStatisticDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStatisticDirection.setStatus(_A)
class _HwStatisticUserAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5000,5999),ValueRangeConstraint(10000,12999))
_HwStatisticUserAclNum_Type.__name__=_B
_HwStatisticUserAclNum_Object=MibTableColumn
hwStatisticUserAclNum=_HwStatisticUserAclNum_Object((1,3,6,1,4,1,2011,2,23,1,16,2,7,1,5),_HwStatisticUserAclNum_Type())
hwStatisticUserAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStatisticUserAclNum.setStatus(_A)
class _HwStatisticUserAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwStatisticUserAclRule_Type.__name__=_B
_HwStatisticUserAclRule_Object=MibTableColumn
hwStatisticUserAclRule=_HwStatisticUserAclRule_Object((1,3,6,1,4,1,2011,2,23,1,16,2,7,1,6),_HwStatisticUserAclRule_Type())
hwStatisticUserAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStatisticUserAclRule.setStatus(_A)
class _HwStatisticIpAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999),ValueRangeConstraint(10000,12999))
_HwStatisticIpAclNum_Type.__name__=_B
_HwStatisticIpAclNum_Object=MibTableColumn
hwStatisticIpAclNum=_HwStatisticIpAclNum_Object((1,3,6,1,4,1,2011,2,23,1,16,2,7,1,7),_HwStatisticIpAclNum_Type())
hwStatisticIpAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStatisticIpAclNum.setStatus(_A)
class _HwStatisticIpAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwStatisticIpAclRule_Type.__name__=_B
_HwStatisticIpAclRule_Object=MibTableColumn
hwStatisticIpAclRule=_HwStatisticIpAclRule_Object((1,3,6,1,4,1,2011,2,23,1,16,2,7,1,8),_HwStatisticIpAclRule_Type())
hwStatisticIpAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStatisticIpAclRule.setStatus(_A)
class _HwStatisticLinkAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4000,4999),ValueRangeConstraint(10000,12999))
_HwStatisticLinkAclNum_Type.__name__=_B
_HwStatisticLinkAclNum_Object=MibTableColumn
hwStatisticLinkAclNum=_HwStatisticLinkAclNum_Object((1,3,6,1,4,1,2011,2,23,1,16,2,7,1,9),_HwStatisticLinkAclNum_Type())
hwStatisticLinkAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStatisticLinkAclNum.setStatus(_A)
class _HwStatisticLinkAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwStatisticLinkAclRule_Type.__name__=_B
_HwStatisticLinkAclRule_Object=MibTableColumn
hwStatisticLinkAclRule=_HwStatisticLinkAclRule_Object((1,3,6,1,4,1,2011,2,23,1,16,2,7,1,10),_HwStatisticLinkAclRule_Type())
hwStatisticLinkAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStatisticLinkAclRule.setStatus(_A)
_HwStatisticRuntime_Type=TruthValue
_HwStatisticRuntime_Object=MibTableColumn
hwStatisticRuntime=_HwStatisticRuntime_Object((1,3,6,1,4,1,2011,2,23,1,16,2,7,1,11),_HwStatisticRuntime_Type())
hwStatisticRuntime.setMaxAccess(_F)
if mibBuilder.loadTexts:hwStatisticRuntime.setStatus(_A)
_HwStatisticPacketCount_Type=Counter64
_HwStatisticPacketCount_Object=MibTableColumn
hwStatisticPacketCount=_HwStatisticPacketCount_Object((1,3,6,1,4,1,2011,2,23,1,16,2,7,1,12),_HwStatisticPacketCount_Type())
hwStatisticPacketCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hwStatisticPacketCount.setStatus(_A)
_HwStatisticByteCount_Type=Counter64
_HwStatisticByteCount_Object=MibTableColumn
hwStatisticByteCount=_HwStatisticByteCount_Object((1,3,6,1,4,1,2011,2,23,1,16,2,7,1,13),_HwStatisticByteCount_Type())
hwStatisticByteCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hwStatisticByteCount.setStatus(_A)
class _HwStatisticCountClear_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cleared',1),('nouse',2)))
_HwStatisticCountClear_Type.__name__=_B
_HwStatisticCountClear_Object=MibTableColumn
hwStatisticCountClear=_HwStatisticCountClear_Object((1,3,6,1,4,1,2011,2,23,1,16,2,7,1,14),_HwStatisticCountClear_Type())
hwStatisticCountClear.setMaxAccess(_E)
if mibBuilder.loadTexts:hwStatisticCountClear.setStatus(_A)
_HwStatisticRowStatus_Type=RowStatus
_HwStatisticRowStatus_Object=MibTableColumn
hwStatisticRowStatus=_HwStatisticRowStatus_Object((1,3,6,1,4,1,2011,2,23,1,16,2,7,1,15),_HwStatisticRowStatus_Type())
hwStatisticRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwStatisticRowStatus.setStatus(_A)
_HwStatisticPacketXCount_Type=Counter64
_HwStatisticPacketXCount_Object=MibTableColumn
hwStatisticPacketXCount=_HwStatisticPacketXCount_Object((1,3,6,1,4,1,2011,2,23,1,16,2,7,1,16),_HwStatisticPacketXCount_Type())
hwStatisticPacketXCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hwStatisticPacketXCount.setStatus(_A)
_HwStatisticByteXCount_Type=Counter64
_HwStatisticByteXCount_Object=MibTableColumn
hwStatisticByteXCount=_HwStatisticByteXCount_Object((1,3,6,1,4,1,2011,2,23,1,16,2,7,1,17),_HwStatisticByteXCount_Type())
hwStatisticByteXCount.setMaxAccess(_F)
if mibBuilder.loadTexts:hwStatisticByteXCount.setStatus(_A)
_HwMirrorTable_Object=MibTable
hwMirrorTable=_HwMirrorTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,8))
if mibBuilder.loadTexts:hwMirrorTable.setStatus(_A)
_HwMirrorEntry_Object=MibTableRow
hwMirrorEntry=_HwMirrorEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,8,1))
hwMirrorEntry.setIndexNames((0,_D,_g),(0,_D,_h),(0,_D,_i),(0,_D,_j))
if mibBuilder.loadTexts:hwMirrorEntry.setStatus(_A)
class _HwMirrorAclIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2999))
_HwMirrorAclIndex_Type.__name__=_B
_HwMirrorAclIndex_Object=MibTableColumn
hwMirrorAclIndex=_HwMirrorAclIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,8,1,1),_HwMirrorAclIndex_Type())
hwMirrorAclIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirrorAclIndex.setStatus(_A)
_HwMirrorIfIndex_Type=Integer32
_HwMirrorIfIndex_Object=MibTableColumn
hwMirrorIfIndex=_HwMirrorIfIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,8,1,2),_HwMirrorIfIndex_Type())
hwMirrorIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirrorIfIndex.setStatus(_A)
class _HwMirrorVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HwMirrorVlanID_Type.__name__=_B
_HwMirrorVlanID_Object=MibTableColumn
hwMirrorVlanID=_HwMirrorVlanID_Object((1,3,6,1,4,1,2011,2,23,1,16,2,8,1,3),_HwMirrorVlanID_Type())
hwMirrorVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirrorVlanID.setStatus(_A)
class _HwMirrorDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_K,1),(_I,2)))
_HwMirrorDirection_Type.__name__=_B
_HwMirrorDirection_Object=MibTableColumn
hwMirrorDirection=_HwMirrorDirection_Object((1,3,6,1,4,1,2011,2,23,1,16,2,8,1,4),_HwMirrorDirection_Type())
hwMirrorDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirrorDirection.setStatus(_A)
class _HwMirrorUserAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5000,5999),ValueRangeConstraint(10000,12999))
_HwMirrorUserAclNum_Type.__name__=_B
_HwMirrorUserAclNum_Object=MibTableColumn
hwMirrorUserAclNum=_HwMirrorUserAclNum_Object((1,3,6,1,4,1,2011,2,23,1,16,2,8,1,5),_HwMirrorUserAclNum_Type())
hwMirrorUserAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirrorUserAclNum.setStatus(_A)
class _HwMirrorUserAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwMirrorUserAclRule_Type.__name__=_B
_HwMirrorUserAclRule_Object=MibTableColumn
hwMirrorUserAclRule=_HwMirrorUserAclRule_Object((1,3,6,1,4,1,2011,2,23,1,16,2,8,1,6),_HwMirrorUserAclRule_Type())
hwMirrorUserAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirrorUserAclRule.setStatus(_A)
class _HwMirrorIpAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999),ValueRangeConstraint(10000,12999))
_HwMirrorIpAclNum_Type.__name__=_B
_HwMirrorIpAclNum_Object=MibTableColumn
hwMirrorIpAclNum=_HwMirrorIpAclNum_Object((1,3,6,1,4,1,2011,2,23,1,16,2,8,1,7),_HwMirrorIpAclNum_Type())
hwMirrorIpAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirrorIpAclNum.setStatus(_A)
class _HwMirrorIpAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwMirrorIpAclRule_Type.__name__=_B
_HwMirrorIpAclRule_Object=MibTableColumn
hwMirrorIpAclRule=_HwMirrorIpAclRule_Object((1,3,6,1,4,1,2011,2,23,1,16,2,8,1,8),_HwMirrorIpAclRule_Type())
hwMirrorIpAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirrorIpAclRule.setStatus(_A)
class _HwMirrorLinkAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4000,4999),ValueRangeConstraint(10000,12999))
_HwMirrorLinkAclNum_Type.__name__=_B
_HwMirrorLinkAclNum_Object=MibTableColumn
hwMirrorLinkAclNum=_HwMirrorLinkAclNum_Object((1,3,6,1,4,1,2011,2,23,1,16,2,8,1,9),_HwMirrorLinkAclNum_Type())
hwMirrorLinkAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirrorLinkAclNum.setStatus(_A)
class _HwMirrorLinkAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwMirrorLinkAclRule_Type.__name__=_B
_HwMirrorLinkAclRule_Object=MibTableColumn
hwMirrorLinkAclRule=_HwMirrorLinkAclRule_Object((1,3,6,1,4,1,2011,2,23,1,16,2,8,1,10),_HwMirrorLinkAclRule_Type())
hwMirrorLinkAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirrorLinkAclRule.setStatus(_A)
_HwMirrorToIfIndex_Type=Integer32
_HwMirrorToIfIndex_Object=MibTableColumn
hwMirrorToIfIndex=_HwMirrorToIfIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,8,1,11),_HwMirrorToIfIndex_Type())
hwMirrorToIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirrorToIfIndex.setStatus(_A)
_HwMirrorToCpu_Type=TruthValue
_HwMirrorToCpu_Object=MibTableColumn
hwMirrorToCpu=_HwMirrorToCpu_Object((1,3,6,1,4,1,2011,2,23,1,16,2,8,1,12),_HwMirrorToCpu_Type())
hwMirrorToCpu.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirrorToCpu.setStatus(_A)
_HwMirrorRuntime_Type=TruthValue
_HwMirrorRuntime_Object=MibTableColumn
hwMirrorRuntime=_HwMirrorRuntime_Object((1,3,6,1,4,1,2011,2,23,1,16,2,8,1,13),_HwMirrorRuntime_Type())
hwMirrorRuntime.setMaxAccess(_F)
if mibBuilder.loadTexts:hwMirrorRuntime.setStatus(_A)
_HwMirrorRowStatus_Type=RowStatus
_HwMirrorRowStatus_Object=MibTableColumn
hwMirrorRowStatus=_HwMirrorRowStatus_Object((1,3,6,1,4,1,2011,2,23,1,16,2,8,1,14),_HwMirrorRowStatus_Type())
hwMirrorRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirrorRowStatus.setStatus(_A)
_HwMirrorToGroup_Type=Integer32
_HwMirrorToGroup_Object=MibTableColumn
hwMirrorToGroup=_HwMirrorToGroup_Object((1,3,6,1,4,1,2011,2,23,1,16,2,8,1,15),_HwMirrorToGroup_Type())
hwMirrorToGroup.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirrorToGroup.setStatus(_A)
_HwPortMirrorTable_Object=MibTable
hwPortMirrorTable=_HwPortMirrorTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,9))
if mibBuilder.loadTexts:hwPortMirrorTable.setStatus(_A)
_HwPortMirrorEntry_Object=MibTableRow
hwPortMirrorEntry=_HwPortMirrorEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,9,1))
hwPortMirrorEntry.setIndexNames((0,_D,_k))
if mibBuilder.loadTexts:hwPortMirrorEntry.setStatus(_A)
_HwPortMirrorIfIndex_Type=Integer32
_HwPortMirrorIfIndex_Object=MibTableColumn
hwPortMirrorIfIndex=_HwPortMirrorIfIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,9,1,1),_HwPortMirrorIfIndex_Type())
hwPortMirrorIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPortMirrorIfIndex.setStatus(_A)
class _HwPortMirrorDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('in',1),('out',2),('both',3)))
_HwPortMirrorDirection_Type.__name__=_B
_HwPortMirrorDirection_Object=MibTableColumn
hwPortMirrorDirection=_HwPortMirrorDirection_Object((1,3,6,1,4,1,2011,2,23,1,16,2,9,1,2),_HwPortMirrorDirection_Type())
hwPortMirrorDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPortMirrorDirection.setStatus(_A)
_HwPortMirrorRowStatus_Type=RowStatus
_HwPortMirrorRowStatus_Object=MibTableColumn
hwPortMirrorRowStatus=_HwPortMirrorRowStatus_Object((1,3,6,1,4,1,2011,2,23,1,16,2,9,1,3),_HwPortMirrorRowStatus_Type())
hwPortMirrorRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwPortMirrorRowStatus.setStatus(_A)
_HwLineRateTable_Object=MibTable
hwLineRateTable=_HwLineRateTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,10))
if mibBuilder.loadTexts:hwLineRateTable.setStatus(_A)
_HwLineRateEntry_Object=MibTableRow
hwLineRateEntry=_HwLineRateEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,10,1))
hwLineRateEntry.setIndexNames((0,_D,_l),(0,_D,_m))
if mibBuilder.loadTexts:hwLineRateEntry.setStatus(_A)
_HwLineRateIfIndex_Type=Integer32
_HwLineRateIfIndex_Object=MibTableColumn
hwLineRateIfIndex=_HwLineRateIfIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,10,1,1),_HwLineRateIfIndex_Type())
hwLineRateIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwLineRateIfIndex.setStatus(_A)
class _HwLineRateDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('in',1),('out',2)))
_HwLineRateDirection_Type.__name__=_B
_HwLineRateDirection_Object=MibTableColumn
hwLineRateDirection=_HwLineRateDirection_Object((1,3,6,1,4,1,2011,2,23,1,16,2,10,1,2),_HwLineRateDirection_Type())
hwLineRateDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hwLineRateDirection.setStatus(_A)
_HwLineRateValue_Type=Integer32
_HwLineRateValue_Object=MibTableColumn
hwLineRateValue=_HwLineRateValue_Object((1,3,6,1,4,1,2011,2,23,1,16,2,10,1,3),_HwLineRateValue_Type())
hwLineRateValue.setMaxAccess(_C)
if mibBuilder.loadTexts:hwLineRateValue.setStatus(_A)
_HwLineRateRowStatus_Type=RowStatus
_HwLineRateRowStatus_Object=MibTableColumn
hwLineRateRowStatus=_HwLineRateRowStatus_Object((1,3,6,1,4,1,2011,2,23,1,16,2,10,1,4),_HwLineRateRowStatus_Type())
hwLineRateRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwLineRateRowStatus.setStatus(_A)
_HwBandwidthTable_Object=MibTable
hwBandwidthTable=_HwBandwidthTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,11))
if mibBuilder.loadTexts:hwBandwidthTable.setStatus(_A)
_HwBandwidthEntry_Object=MibTableRow
hwBandwidthEntry=_HwBandwidthEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,11,1))
hwBandwidthEntry.setIndexNames((0,_D,_n),(0,_D,_o),(0,_D,_p),(0,_D,_q))
if mibBuilder.loadTexts:hwBandwidthEntry.setStatus(_A)
class _HwBandwidthAclIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2999))
_HwBandwidthAclIndex_Type.__name__=_B
_HwBandwidthAclIndex_Object=MibTableColumn
hwBandwidthAclIndex=_HwBandwidthAclIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,11,1,1),_HwBandwidthAclIndex_Type())
hwBandwidthAclIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwBandwidthAclIndex.setStatus(_A)
_HwBandwidthIfIndex_Type=Integer32
_HwBandwidthIfIndex_Object=MibTableColumn
hwBandwidthIfIndex=_HwBandwidthIfIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,11,1,2),_HwBandwidthIfIndex_Type())
hwBandwidthIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwBandwidthIfIndex.setStatus(_A)
class _HwBandwidthVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HwBandwidthVlanID_Type.__name__=_B
_HwBandwidthVlanID_Object=MibTableColumn
hwBandwidthVlanID=_HwBandwidthVlanID_Object((1,3,6,1,4,1,2011,2,23,1,16,2,11,1,3),_HwBandwidthVlanID_Type())
hwBandwidthVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwBandwidthVlanID.setStatus(_A)
class _HwBandwidthDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*((_H,0),(_I,2)))
_HwBandwidthDirection_Type.__name__=_B
_HwBandwidthDirection_Object=MibTableColumn
hwBandwidthDirection=_HwBandwidthDirection_Object((1,3,6,1,4,1,2011,2,23,1,16,2,11,1,4),_HwBandwidthDirection_Type())
hwBandwidthDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hwBandwidthDirection.setStatus(_A)
class _HwBandwidthIpAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999),ValueRangeConstraint(10000,12999))
_HwBandwidthIpAclNum_Type.__name__=_B
_HwBandwidthIpAclNum_Object=MibTableColumn
hwBandwidthIpAclNum=_HwBandwidthIpAclNum_Object((1,3,6,1,4,1,2011,2,23,1,16,2,11,1,5),_HwBandwidthIpAclNum_Type())
hwBandwidthIpAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwBandwidthIpAclNum.setStatus(_A)
class _HwBandwidthIpAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwBandwidthIpAclRule_Type.__name__=_B
_HwBandwidthIpAclRule_Object=MibTableColumn
hwBandwidthIpAclRule=_HwBandwidthIpAclRule_Object((1,3,6,1,4,1,2011,2,23,1,16,2,11,1,6),_HwBandwidthIpAclRule_Type())
hwBandwidthIpAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hwBandwidthIpAclRule.setStatus(_A)
class _HwBandwidthLinkAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4000,4999),ValueRangeConstraint(10000,12999))
_HwBandwidthLinkAclNum_Type.__name__=_B
_HwBandwidthLinkAclNum_Object=MibTableColumn
hwBandwidthLinkAclNum=_HwBandwidthLinkAclNum_Object((1,3,6,1,4,1,2011,2,23,1,16,2,11,1,7),_HwBandwidthLinkAclNum_Type())
hwBandwidthLinkAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwBandwidthLinkAclNum.setStatus(_A)
class _HwBandwidthLinkAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwBandwidthLinkAclRule_Type.__name__=_B
_HwBandwidthLinkAclRule_Object=MibTableColumn
hwBandwidthLinkAclRule=_HwBandwidthLinkAclRule_Object((1,3,6,1,4,1,2011,2,23,1,16,2,11,1,8),_HwBandwidthLinkAclRule_Type())
hwBandwidthLinkAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hwBandwidthLinkAclRule.setStatus(_A)
class _HwBandwidthMinGuaranteedWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8388608))
_HwBandwidthMinGuaranteedWidth_Type.__name__=_B
_HwBandwidthMinGuaranteedWidth_Object=MibTableColumn
hwBandwidthMinGuaranteedWidth=_HwBandwidthMinGuaranteedWidth_Object((1,3,6,1,4,1,2011,2,23,1,16,2,11,1,9),_HwBandwidthMinGuaranteedWidth_Type())
hwBandwidthMinGuaranteedWidth.setMaxAccess(_E)
if mibBuilder.loadTexts:hwBandwidthMinGuaranteedWidth.setStatus(_A)
class _HwBandwidthMaxGuaranteedWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8388608))
_HwBandwidthMaxGuaranteedWidth_Type.__name__=_B
_HwBandwidthMaxGuaranteedWidth_Object=MibTableColumn
hwBandwidthMaxGuaranteedWidth=_HwBandwidthMaxGuaranteedWidth_Object((1,3,6,1,4,1,2011,2,23,1,16,2,11,1,10),_HwBandwidthMaxGuaranteedWidth_Type())
hwBandwidthMaxGuaranteedWidth.setMaxAccess(_E)
if mibBuilder.loadTexts:hwBandwidthMaxGuaranteedWidth.setStatus(_A)
class _HwBandwidthWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HwBandwidthWeight_Type.__name__=_B
_HwBandwidthWeight_Object=MibTableColumn
hwBandwidthWeight=_HwBandwidthWeight_Object((1,3,6,1,4,1,2011,2,23,1,16,2,11,1,11),_HwBandwidthWeight_Type())
hwBandwidthWeight.setMaxAccess(_E)
if mibBuilder.loadTexts:hwBandwidthWeight.setStatus(_A)
_HwBandwidthRuntime_Type=TruthValue
_HwBandwidthRuntime_Object=MibTableColumn
hwBandwidthRuntime=_HwBandwidthRuntime_Object((1,3,6,1,4,1,2011,2,23,1,16,2,11,1,12),_HwBandwidthRuntime_Type())
hwBandwidthRuntime.setMaxAccess(_F)
if mibBuilder.loadTexts:hwBandwidthRuntime.setStatus(_A)
_HwBandwidthRowStatus_Type=RowStatus
_HwBandwidthRowStatus_Object=MibTableColumn
hwBandwidthRowStatus=_HwBandwidthRowStatus_Object((1,3,6,1,4,1,2011,2,23,1,16,2,11,1,13),_HwBandwidthRowStatus_Type())
hwBandwidthRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hwBandwidthRowStatus.setStatus(_A)
_HwRedTable_Object=MibTable
hwRedTable=_HwRedTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,12))
if mibBuilder.loadTexts:hwRedTable.setStatus(_A)
_HwRedEntry_Object=MibTableRow
hwRedEntry=_HwRedEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,12,1))
hwRedEntry.setIndexNames((0,_D,_r),(0,_D,_s),(0,_D,_t),(0,_D,_u))
if mibBuilder.loadTexts:hwRedEntry.setStatus(_A)
class _HwRedAclIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2999))
_HwRedAclIndex_Type.__name__=_B
_HwRedAclIndex_Object=MibTableColumn
hwRedAclIndex=_HwRedAclIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,12,1,1),_HwRedAclIndex_Type())
hwRedAclIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedAclIndex.setStatus(_A)
_HwRedIfIndex_Type=Integer32
_HwRedIfIndex_Object=MibTableColumn
hwRedIfIndex=_HwRedIfIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,12,1,2),_HwRedIfIndex_Type())
hwRedIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedIfIndex.setStatus(_A)
class _HwRedVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HwRedVlanID_Type.__name__=_B
_HwRedVlanID_Object=MibTableColumn
hwRedVlanID=_HwRedVlanID_Object((1,3,6,1,4,1,2011,2,23,1,16,2,12,1,3),_HwRedVlanID_Type())
hwRedVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedVlanID.setStatus(_A)
class _HwRedDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2)));namedValues=NamedValues(*((_H,0),(_I,2)))
_HwRedDirection_Type.__name__=_B
_HwRedDirection_Object=MibTableColumn
hwRedDirection=_HwRedDirection_Object((1,3,6,1,4,1,2011,2,23,1,16,2,12,1,4),_HwRedDirection_Type())
hwRedDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedDirection.setStatus(_A)
class _HwRedIpAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999),ValueRangeConstraint(10000,12999))
_HwRedIpAclNum_Type.__name__=_B
_HwRedIpAclNum_Object=MibTableColumn
hwRedIpAclNum=_HwRedIpAclNum_Object((1,3,6,1,4,1,2011,2,23,1,16,2,12,1,5),_HwRedIpAclNum_Type())
hwRedIpAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedIpAclNum.setStatus(_A)
class _HwRedIpAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwRedIpAclRule_Type.__name__=_B
_HwRedIpAclRule_Object=MibTableColumn
hwRedIpAclRule=_HwRedIpAclRule_Object((1,3,6,1,4,1,2011,2,23,1,16,2,12,1,6),_HwRedIpAclRule_Type())
hwRedIpAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedIpAclRule.setStatus(_A)
class _HwRedLinkAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4000,4999),ValueRangeConstraint(10000,12999))
_HwRedLinkAclNum_Type.__name__=_B
_HwRedLinkAclNum_Object=MibTableColumn
hwRedLinkAclNum=_HwRedLinkAclNum_Object((1,3,6,1,4,1,2011,2,23,1,16,2,12,1,7),_HwRedLinkAclNum_Type())
hwRedLinkAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedLinkAclNum.setStatus(_A)
class _HwRedLinkAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwRedLinkAclRule_Type.__name__=_B
_HwRedLinkAclRule_Object=MibTableColumn
hwRedLinkAclRule=_HwRedLinkAclRule_Object((1,3,6,1,4,1,2011,2,23,1,16,2,12,1,8),_HwRedLinkAclRule_Type())
hwRedLinkAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRedLinkAclRule.setStatus(_A)
class _HwRedStartQueueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,262128))
_HwRedStartQueueLen_Type.__name__=_B
_HwRedStartQueueLen_Object=MibTableColumn
hwRedStartQueueLen=_HwRedStartQueueLen_Object((1,3,6,1,4,1,2011,2,23,1,16,2,12,1,9),_HwRedStartQueueLen_Type())
hwRedStartQueueLen.setMaxAccess(_E)
if mibBuilder.loadTexts:hwRedStartQueueLen.setStatus(_A)
class _HwRedStopQueueLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,262128))
_HwRedStopQueueLen_Type.__name__=_B
_HwRedStopQueueLen_Object=MibTableColumn
hwRedStopQueueLen=_HwRedStopQueueLen_Object((1,3,6,1,4,1,2011,2,23,1,16,2,12,1,10),_HwRedStopQueueLen_Type())
hwRedStopQueueLen.setMaxAccess(_E)
if mibBuilder.loadTexts:hwRedStopQueueLen.setStatus(_A)
class _HwRedProbability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HwRedProbability_Type.__name__=_B
_HwRedProbability_Object=MibTableColumn
hwRedProbability=_HwRedProbability_Object((1,3,6,1,4,1,2011,2,23,1,16,2,12,1,11),_HwRedProbability_Type())
hwRedProbability.setMaxAccess(_E)
if mibBuilder.loadTexts:hwRedProbability.setStatus(_A)
_HwRedRuntime_Type=TruthValue
_HwRedRuntime_Object=MibTableColumn
hwRedRuntime=_HwRedRuntime_Object((1,3,6,1,4,1,2011,2,23,1,16,2,12,1,12),_HwRedRuntime_Type())
hwRedRuntime.setMaxAccess(_F)
if mibBuilder.loadTexts:hwRedRuntime.setStatus(_A)
_HwRedRowStatus_Type=RowStatus
_HwRedRowStatus_Object=MibTableColumn
hwRedRowStatus=_HwRedRowStatus_Object((1,3,6,1,4,1,2011,2,23,1,16,2,12,1,13),_HwRedRowStatus_Type())
hwRedRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hwRedRowStatus.setStatus(_A)
_HwMirrorGroupTable_Object=MibTable
hwMirrorGroupTable=_HwMirrorGroupTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,13))
if mibBuilder.loadTexts:hwMirrorGroupTable.setStatus(_A)
_HwMirrorGroupEntry_Object=MibTableRow
hwMirrorGroupEntry=_HwMirrorGroupEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,13,1))
hwMirrorGroupEntry.setIndexNames((0,_D,_v))
if mibBuilder.loadTexts:hwMirrorGroupEntry.setStatus(_A)
class _HwMirrorGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_HwMirrorGroupID_Type.__name__=_B
_HwMirrorGroupID_Object=MibTableColumn
hwMirrorGroupID=_HwMirrorGroupID_Object((1,3,6,1,4,1,2011,2,23,1,16,2,13,1,1),_HwMirrorGroupID_Type())
hwMirrorGroupID.setMaxAccess(_F)
if mibBuilder.loadTexts:hwMirrorGroupID.setStatus(_A)
class _HwMirrorGroupDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_I,2)))
_HwMirrorGroupDirection_Type.__name__=_B
_HwMirrorGroupDirection_Object=MibTableColumn
hwMirrorGroupDirection=_HwMirrorGroupDirection_Object((1,3,6,1,4,1,2011,2,23,1,16,2,13,1,2),_HwMirrorGroupDirection_Type())
hwMirrorGroupDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:hwMirrorGroupDirection.setStatus(_A)
class _HwMirrorGroupMirrorIfIndexList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,257))
_HwMirrorGroupMirrorIfIndexList_Type.__name__=_O
_HwMirrorGroupMirrorIfIndexList_Object=MibTableColumn
hwMirrorGroupMirrorIfIndexList=_HwMirrorGroupMirrorIfIndexList_Object((1,3,6,1,4,1,2011,2,23,1,16,2,13,1,3),_HwMirrorGroupMirrorIfIndexList_Type())
hwMirrorGroupMirrorIfIndexList.setMaxAccess(_E)
if mibBuilder.loadTexts:hwMirrorGroupMirrorIfIndexList.setStatus(_A)
_HwMirrorGroupMonitorIfIndex_Type=Integer32
_HwMirrorGroupMonitorIfIndex_Object=MibTableColumn
hwMirrorGroupMonitorIfIndex=_HwMirrorGroupMonitorIfIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,13,1,4),_HwMirrorGroupMonitorIfIndex_Type())
hwMirrorGroupMonitorIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hwMirrorGroupMonitorIfIndex.setStatus(_A)
_HwMirrorGroupRowStatus_Type=RowStatus
_HwMirrorGroupRowStatus_Object=MibTableColumn
hwMirrorGroupRowStatus=_HwMirrorGroupRowStatus_Object((1,3,6,1,4,1,2011,2,23,1,16,2,13,1,5),_HwMirrorGroupRowStatus_Type())
hwMirrorGroupRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hwMirrorGroupRowStatus.setStatus(_A)
_HwFlowtempTable_Object=MibTable
hwFlowtempTable=_HwFlowtempTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14))
if mibBuilder.loadTexts:hwFlowtempTable.setStatus(_A)
_HwFlowtempEntry_Object=MibTableRow
hwFlowtempEntry=_HwFlowtempEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14,1))
hwFlowtempEntry.setIndexNames((0,_D,_w))
if mibBuilder.loadTexts:hwFlowtempEntry.setStatus(_A)
class _HwFlowtempIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_x,2)))
_HwFlowtempIndex_Type.__name__=_B
_HwFlowtempIndex_Object=MibTableColumn
hwFlowtempIndex=_HwFlowtempIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14,1,1),_HwFlowtempIndex_Type())
hwFlowtempIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hwFlowtempIndex.setStatus(_A)
_HwFlowtempIpProtocol_Type=TruthValue
_HwFlowtempIpProtocol_Object=MibTableColumn
hwFlowtempIpProtocol=_HwFlowtempIpProtocol_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14,1,2),_HwFlowtempIpProtocol_Type())
hwFlowtempIpProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:hwFlowtempIpProtocol.setStatus(_A)
_HwFlowtempTcpFlag_Type=TruthValue
_HwFlowtempTcpFlag_Object=MibTableColumn
hwFlowtempTcpFlag=_HwFlowtempTcpFlag_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14,1,3),_HwFlowtempTcpFlag_Type())
hwFlowtempTcpFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:hwFlowtempTcpFlag.setStatus(_A)
_HwFlowtempSPort_Type=TruthValue
_HwFlowtempSPort_Object=MibTableColumn
hwFlowtempSPort=_HwFlowtempSPort_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14,1,4),_HwFlowtempSPort_Type())
hwFlowtempSPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hwFlowtempSPort.setStatus(_A)
_HwFlowtempDPort_Type=TruthValue
_HwFlowtempDPort_Object=MibTableColumn
hwFlowtempDPort=_HwFlowtempDPort_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14,1,5),_HwFlowtempDPort_Type())
hwFlowtempDPort.setMaxAccess(_C)
if mibBuilder.loadTexts:hwFlowtempDPort.setStatus(_A)
_HwFlowtempIcmpType_Type=TruthValue
_HwFlowtempIcmpType_Object=MibTableColumn
hwFlowtempIcmpType=_HwFlowtempIcmpType_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14,1,6),_HwFlowtempIcmpType_Type())
hwFlowtempIcmpType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwFlowtempIcmpType.setStatus(_A)
_HwFlowtempIcmpCode_Type=TruthValue
_HwFlowtempIcmpCode_Object=MibTableColumn
hwFlowtempIcmpCode=_HwFlowtempIcmpCode_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14,1,7),_HwFlowtempIcmpCode_Type())
hwFlowtempIcmpCode.setMaxAccess(_C)
if mibBuilder.loadTexts:hwFlowtempIcmpCode.setStatus(_A)
_HwFlowtempFragment_Type=TruthValue
_HwFlowtempFragment_Object=MibTableColumn
hwFlowtempFragment=_HwFlowtempFragment_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14,1,8),_HwFlowtempFragment_Type())
hwFlowtempFragment.setMaxAccess(_C)
if mibBuilder.loadTexts:hwFlowtempFragment.setStatus(_A)
_HwFlowtempDscp_Type=TruthValue
_HwFlowtempDscp_Object=MibTableColumn
hwFlowtempDscp=_HwFlowtempDscp_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14,1,9),_HwFlowtempDscp_Type())
hwFlowtempDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:hwFlowtempDscp.setStatus(_A)
_HwFlowtempIpPre_Type=TruthValue
_HwFlowtempIpPre_Object=MibTableColumn
hwFlowtempIpPre=_HwFlowtempIpPre_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14,1,10),_HwFlowtempIpPre_Type())
hwFlowtempIpPre.setMaxAccess(_C)
if mibBuilder.loadTexts:hwFlowtempIpPre.setStatus(_A)
_HwFlowtempTos_Type=TruthValue
_HwFlowtempTos_Object=MibTableColumn
hwFlowtempTos=_HwFlowtempTos_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14,1,11),_HwFlowtempTos_Type())
hwFlowtempTos.setMaxAccess(_C)
if mibBuilder.loadTexts:hwFlowtempTos.setStatus(_A)
_HwFlowtempSIp_Type=TruthValue
_HwFlowtempSIp_Object=MibTableColumn
hwFlowtempSIp=_HwFlowtempSIp_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14,1,12),_HwFlowtempSIp_Type())
hwFlowtempSIp.setMaxAccess(_C)
if mibBuilder.loadTexts:hwFlowtempSIp.setStatus(_A)
_HwFlowtempSIpMask_Type=IpAddress
_HwFlowtempSIpMask_Object=MibTableColumn
hwFlowtempSIpMask=_HwFlowtempSIpMask_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14,1,13),_HwFlowtempSIpMask_Type())
hwFlowtempSIpMask.setMaxAccess(_C)
if mibBuilder.loadTexts:hwFlowtempSIpMask.setStatus(_A)
_HwFlowtempDIp_Type=TruthValue
_HwFlowtempDIp_Object=MibTableColumn
hwFlowtempDIp=_HwFlowtempDIp_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14,1,14),_HwFlowtempDIp_Type())
hwFlowtempDIp.setMaxAccess(_C)
if mibBuilder.loadTexts:hwFlowtempDIp.setStatus(_A)
_HwFlowtempDIpMask_Type=IpAddress
_HwFlowtempDIpMask_Object=MibTableColumn
hwFlowtempDIpMask=_HwFlowtempDIpMask_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14,1,15),_HwFlowtempDIpMask_Type())
hwFlowtempDIpMask.setMaxAccess(_C)
if mibBuilder.loadTexts:hwFlowtempDIpMask.setStatus(_A)
_HwFlowtempEthProtocol_Type=TruthValue
_HwFlowtempEthProtocol_Object=MibTableColumn
hwFlowtempEthProtocol=_HwFlowtempEthProtocol_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14,1,16),_HwFlowtempEthProtocol_Type())
hwFlowtempEthProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:hwFlowtempEthProtocol.setStatus(_A)
_HwFlowtempSMac_Type=TruthValue
_HwFlowtempSMac_Object=MibTableColumn
hwFlowtempSMac=_HwFlowtempSMac_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14,1,17),_HwFlowtempSMac_Type())
hwFlowtempSMac.setMaxAccess(_C)
if mibBuilder.loadTexts:hwFlowtempSMac.setStatus(_A)
_HwFlowtempSMacMask_Type=MacAddress
_HwFlowtempSMacMask_Object=MibTableColumn
hwFlowtempSMacMask=_HwFlowtempSMacMask_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14,1,18),_HwFlowtempSMacMask_Type())
hwFlowtempSMacMask.setMaxAccess(_C)
if mibBuilder.loadTexts:hwFlowtempSMacMask.setStatus(_A)
_HwFlowtempDMac_Type=TruthValue
_HwFlowtempDMac_Object=MibTableColumn
hwFlowtempDMac=_HwFlowtempDMac_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14,1,19),_HwFlowtempDMac_Type())
hwFlowtempDMac.setMaxAccess(_C)
if mibBuilder.loadTexts:hwFlowtempDMac.setStatus(_A)
_HwFlowtempDMacMask_Type=MacAddress
_HwFlowtempDMacMask_Object=MibTableColumn
hwFlowtempDMacMask=_HwFlowtempDMacMask_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14,1,20),_HwFlowtempDMacMask_Type())
hwFlowtempDMacMask.setMaxAccess(_C)
if mibBuilder.loadTexts:hwFlowtempDMacMask.setStatus(_A)
_HwFlowtempVpn_Type=TruthValue
_HwFlowtempVpn_Object=MibTableColumn
hwFlowtempVpn=_HwFlowtempVpn_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14,1,21),_HwFlowtempVpn_Type())
hwFlowtempVpn.setMaxAccess(_C)
if mibBuilder.loadTexts:hwFlowtempVpn.setStatus(_A)
_HwFlowtempRowStatus_Type=RowStatus
_HwFlowtempRowStatus_Object=MibTableColumn
hwFlowtempRowStatus=_HwFlowtempRowStatus_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14,1,22),_HwFlowtempRowStatus_Type())
hwFlowtempRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwFlowtempRowStatus.setStatus(_A)
_HwFlowtempVlanId_Type=TruthValue
_HwFlowtempVlanId_Object=MibTableColumn
hwFlowtempVlanId=_HwFlowtempVlanId_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14,1,23),_HwFlowtempVlanId_Type())
hwFlowtempVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:hwFlowtempVlanId.setStatus(_A)
_HwFlowtempCos_Type=TruthValue
_HwFlowtempCos_Object=MibTableColumn
hwFlowtempCos=_HwFlowtempCos_Object((1,3,6,1,4,1,2011,2,23,1,16,2,14,1,24),_HwFlowtempCos_Type())
hwFlowtempCos.setMaxAccess(_C)
if mibBuilder.loadTexts:hwFlowtempCos.setStatus(_A)
_HwFlowtempEnableTable_Object=MibTable
hwFlowtempEnableTable=_HwFlowtempEnableTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,15))
if mibBuilder.loadTexts:hwFlowtempEnableTable.setStatus(_A)
_HwFlowtempEnableEntry_Object=MibTableRow
hwFlowtempEnableEntry=_HwFlowtempEnableEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,15,1))
hwFlowtempEnableEntry.setIndexNames((0,_D,_y),(0,_D,_z))
if mibBuilder.loadTexts:hwFlowtempEnableEntry.setStatus(_A)
_HwFlowtempEnableIfIndex_Type=Integer32
_HwFlowtempEnableIfIndex_Object=MibTableColumn
hwFlowtempEnableIfIndex=_HwFlowtempEnableIfIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,15,1,1),_HwFlowtempEnableIfIndex_Type())
hwFlowtempEnableIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwFlowtempEnableIfIndex.setStatus(_A)
class _HwFlowtempEnableVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HwFlowtempEnableVlanID_Type.__name__=_B
_HwFlowtempEnableVlanID_Object=MibTableColumn
hwFlowtempEnableVlanID=_HwFlowtempEnableVlanID_Object((1,3,6,1,4,1,2011,2,23,1,16,2,15,1,2),_HwFlowtempEnableVlanID_Type())
hwFlowtempEnableVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwFlowtempEnableVlanID.setStatus(_A)
class _HwFlowtempEnableFlowtempIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_x,2)))
_HwFlowtempEnableFlowtempIndex_Type.__name__=_B
_HwFlowtempEnableFlowtempIndex_Object=MibTableColumn
hwFlowtempEnableFlowtempIndex=_HwFlowtempEnableFlowtempIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,15,1,3),_HwFlowtempEnableFlowtempIndex_Type())
hwFlowtempEnableFlowtempIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hwFlowtempEnableFlowtempIndex.setStatus(_A)
_HwTrafficShapeTable_Object=MibTable
hwTrafficShapeTable=_HwTrafficShapeTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,16))
if mibBuilder.loadTexts:hwTrafficShapeTable.setStatus(_A)
_HwTrafficShapeEntry_Object=MibTableRow
hwTrafficShapeEntry=_HwTrafficShapeEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,16,1))
hwTrafficShapeEntry.setIndexNames((0,_D,_A0),(0,_D,_A1))
if mibBuilder.loadTexts:hwTrafficShapeEntry.setStatus(_A)
_HwTrafficShapeIfIndex_Type=Integer32
_HwTrafficShapeIfIndex_Object=MibTableColumn
hwTrafficShapeIfIndex=_HwTrafficShapeIfIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,16,1,1),_HwTrafficShapeIfIndex_Type())
hwTrafficShapeIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwTrafficShapeIfIndex.setStatus(_A)
class _HwTrafficShapeQueueId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HwTrafficShapeQueueId_Type.__name__=_B
_HwTrafficShapeQueueId_Object=MibTableColumn
hwTrafficShapeQueueId=_HwTrafficShapeQueueId_Object((1,3,6,1,4,1,2011,2,23,1,16,2,16,1,2),_HwTrafficShapeQueueId_Type())
hwTrafficShapeQueueId.setMaxAccess(_C)
if mibBuilder.loadTexts:hwTrafficShapeQueueId.setStatus(_A)
_HwTrafficShapeMaxRate_Type=Integer32
_HwTrafficShapeMaxRate_Object=MibTableColumn
hwTrafficShapeMaxRate=_HwTrafficShapeMaxRate_Object((1,3,6,1,4,1,2011,2,23,1,16,2,16,1,3),_HwTrafficShapeMaxRate_Type())
hwTrafficShapeMaxRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hwTrafficShapeMaxRate.setStatus(_A)
_HwTrafficShapeBurstSize_Type=Integer32
_HwTrafficShapeBurstSize_Object=MibTableColumn
hwTrafficShapeBurstSize=_HwTrafficShapeBurstSize_Object((1,3,6,1,4,1,2011,2,23,1,16,2,16,1,4),_HwTrafficShapeBurstSize_Type())
hwTrafficShapeBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hwTrafficShapeBurstSize.setStatus(_A)
class _HwTrafficShapeBufferLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(16,8000))
_HwTrafficShapeBufferLimit_Type.__name__=_B
_HwTrafficShapeBufferLimit_Object=MibTableColumn
hwTrafficShapeBufferLimit=_HwTrafficShapeBufferLimit_Object((1,3,6,1,4,1,2011,2,23,1,16,2,16,1,5),_HwTrafficShapeBufferLimit_Type())
hwTrafficShapeBufferLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:hwTrafficShapeBufferLimit.setStatus(_A)
_HwTrafficShapeRowStatus_Type=RowStatus
_HwTrafficShapeRowStatus_Object=MibTableColumn
hwTrafficShapeRowStatus=_HwTrafficShapeRowStatus_Object((1,3,6,1,4,1,2011,2,23,1,16,2,16,1,6),_HwTrafficShapeRowStatus_Type())
hwTrafficShapeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwTrafficShapeRowStatus.setStatus(_A)
_HwPortQueueTable_Object=MibTable
hwPortQueueTable=_HwPortQueueTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,17))
if mibBuilder.loadTexts:hwPortQueueTable.setStatus(_A)
_HwPortQueueEntry_Object=MibTableRow
hwPortQueueEntry=_HwPortQueueEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,17,1))
hwPortQueueEntry.setIndexNames((0,_D,_A2),(0,_D,_A3))
if mibBuilder.loadTexts:hwPortQueueEntry.setStatus(_A)
_HwPortQueueIfIndex_Type=Integer32
_HwPortQueueIfIndex_Object=MibTableColumn
hwPortQueueIfIndex=_HwPortQueueIfIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,17,1,1),_HwPortQueueIfIndex_Type())
hwPortQueueIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hwPortQueueIfIndex.setStatus(_A)
class _HwPortQueueQueueID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HwPortQueueQueueID_Type.__name__=_B
_HwPortQueueQueueID_Object=MibTableColumn
hwPortQueueQueueID=_HwPortQueueQueueID_Object((1,3,6,1,4,1,2011,2,23,1,16,2,17,1,2),_HwPortQueueQueueID_Type())
hwPortQueueQueueID.setMaxAccess(_F)
if mibBuilder.loadTexts:hwPortQueueQueueID.setStatus(_A)
class _HwPortQueueWrrPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('sp',1),('wrr-high-priority',2),('wrr-low-priority',3)))
_HwPortQueueWrrPriority_Type.__name__=_B
_HwPortQueueWrrPriority_Object=MibTableColumn
hwPortQueueWrrPriority=_HwPortQueueWrrPriority_Object((1,3,6,1,4,1,2011,2,23,1,16,2,17,1,3),_HwPortQueueWrrPriority_Type())
hwPortQueueWrrPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:hwPortQueueWrrPriority.setStatus(_A)
class _HwPortQueueWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,255))
_HwPortQueueWeight_Type.__name__=_B
_HwPortQueueWeight_Object=MibTableColumn
hwPortQueueWeight=_HwPortQueueWeight_Object((1,3,6,1,4,1,2011,2,23,1,16,2,17,1,4),_HwPortQueueWeight_Type())
hwPortQueueWeight.setMaxAccess(_E)
if mibBuilder.loadTexts:hwPortQueueWeight.setStatus(_A)
_HwDropModeTable_Object=MibTable
hwDropModeTable=_HwDropModeTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,18))
if mibBuilder.loadTexts:hwDropModeTable.setStatus(_A)
_HwDropModeEntry_Object=MibTableRow
hwDropModeEntry=_HwDropModeEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,18,1))
hwDropModeEntry.setIndexNames((0,_D,_A4))
if mibBuilder.loadTexts:hwDropModeEntry.setStatus(_A)
_HwDropModeIfIndex_Type=Integer32
_HwDropModeIfIndex_Object=MibTableColumn
hwDropModeIfIndex=_HwDropModeIfIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,18,1,1),_HwDropModeIfIndex_Type())
hwDropModeIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hwDropModeIfIndex.setStatus(_A)
class _HwDropModeMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('random-detect',1),('tail-drop',2)))
_HwDropModeMode_Type.__name__=_B
_HwDropModeMode_Object=MibTableColumn
hwDropModeMode=_HwDropModeMode_Object((1,3,6,1,4,1,2011,2,23,1,16,2,18,1,2),_HwDropModeMode_Type())
hwDropModeMode.setMaxAccess(_E)
if mibBuilder.loadTexts:hwDropModeMode.setStatus(_A)
class _HwDropModeWredIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_HwDropModeWredIndex_Type.__name__=_B
_HwDropModeWredIndex_Object=MibTableColumn
hwDropModeWredIndex=_HwDropModeWredIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,18,1,3),_HwDropModeWredIndex_Type())
hwDropModeWredIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hwDropModeWredIndex.setStatus(_A)
_HwWredTable_Object=MibTable
hwWredTable=_HwWredTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,19))
if mibBuilder.loadTexts:hwWredTable.setStatus(_A)
_HwWredEntry_Object=MibTableRow
hwWredEntry=_HwWredEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,19,1))
hwWredEntry.setIndexNames((0,_D,_A5),(0,_D,_A6))
if mibBuilder.loadTexts:hwWredEntry.setStatus(_A)
class _HwWredIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_HwWredIndex_Type.__name__=_B
_HwWredIndex_Object=MibTableColumn
hwWredIndex=_HwWredIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,19,1,1),_HwWredIndex_Type())
hwWredIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hwWredIndex.setStatus(_A)
class _HwWredQueueId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HwWredQueueId_Type.__name__=_B
_HwWredQueueId_Object=MibTableColumn
hwWredQueueId=_HwWredQueueId_Object((1,3,6,1,4,1,2011,2,23,1,16,2,19,1,2),_HwWredQueueId_Type())
hwWredQueueId.setMaxAccess(_F)
if mibBuilder.loadTexts:hwWredQueueId.setStatus(_A)
class _HwWredGreenMinThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwWredGreenMinThreshold_Type.__name__=_B
_HwWredGreenMinThreshold_Object=MibTableColumn
hwWredGreenMinThreshold=_HwWredGreenMinThreshold_Object((1,3,6,1,4,1,2011,2,23,1,16,2,19,1,3),_HwWredGreenMinThreshold_Type())
hwWredGreenMinThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:hwWredGreenMinThreshold.setStatus(_A)
class _HwWredGreenMaxThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwWredGreenMaxThreshold_Type.__name__=_B
_HwWredGreenMaxThreshold_Object=MibTableColumn
hwWredGreenMaxThreshold=_HwWredGreenMaxThreshold_Object((1,3,6,1,4,1,2011,2,23,1,16,2,19,1,4),_HwWredGreenMaxThreshold_Type())
hwWredGreenMaxThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:hwWredGreenMaxThreshold.setStatus(_A)
class _HwWredGreenMaxProb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_HwWredGreenMaxProb_Type.__name__=_B
_HwWredGreenMaxProb_Object=MibTableColumn
hwWredGreenMaxProb=_HwWredGreenMaxProb_Object((1,3,6,1,4,1,2011,2,23,1,16,2,19,1,5),_HwWredGreenMaxProb_Type())
hwWredGreenMaxProb.setMaxAccess(_E)
if mibBuilder.loadTexts:hwWredGreenMaxProb.setStatus(_A)
class _HwWredYellowMinThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwWredYellowMinThreshold_Type.__name__=_B
_HwWredYellowMinThreshold_Object=MibTableColumn
hwWredYellowMinThreshold=_HwWredYellowMinThreshold_Object((1,3,6,1,4,1,2011,2,23,1,16,2,19,1,6),_HwWredYellowMinThreshold_Type())
hwWredYellowMinThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:hwWredYellowMinThreshold.setStatus(_A)
class _HwWredYellowMaxThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwWredYellowMaxThreshold_Type.__name__=_B
_HwWredYellowMaxThreshold_Object=MibTableColumn
hwWredYellowMaxThreshold=_HwWredYellowMaxThreshold_Object((1,3,6,1,4,1,2011,2,23,1,16,2,19,1,7),_HwWredYellowMaxThreshold_Type())
hwWredYellowMaxThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:hwWredYellowMaxThreshold.setStatus(_A)
class _HwWredYellowMaxProb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_HwWredYellowMaxProb_Type.__name__=_B
_HwWredYellowMaxProb_Object=MibTableColumn
hwWredYellowMaxProb=_HwWredYellowMaxProb_Object((1,3,6,1,4,1,2011,2,23,1,16,2,19,1,8),_HwWredYellowMaxProb_Type())
hwWredYellowMaxProb.setMaxAccess(_E)
if mibBuilder.loadTexts:hwWredYellowMaxProb.setStatus(_A)
class _HwWredRedMinThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwWredRedMinThreshold_Type.__name__=_B
_HwWredRedMinThreshold_Object=MibTableColumn
hwWredRedMinThreshold=_HwWredRedMinThreshold_Object((1,3,6,1,4,1,2011,2,23,1,16,2,19,1,9),_HwWredRedMinThreshold_Type())
hwWredRedMinThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:hwWredRedMinThreshold.setStatus(_A)
class _HwWredRedMaxThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwWredRedMaxThreshold_Type.__name__=_B
_HwWredRedMaxThreshold_Object=MibTableColumn
hwWredRedMaxThreshold=_HwWredRedMaxThreshold_Object((1,3,6,1,4,1,2011,2,23,1,16,2,19,1,10),_HwWredRedMaxThreshold_Type())
hwWredRedMaxThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:hwWredRedMaxThreshold.setStatus(_A)
class _HwWredRedMaxProb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_HwWredRedMaxProb_Type.__name__=_B
_HwWredRedMaxProb_Object=MibTableColumn
hwWredRedMaxProb=_HwWredRedMaxProb_Object((1,3,6,1,4,1,2011,2,23,1,16,2,19,1,11),_HwWredRedMaxProb_Type())
hwWredRedMaxProb.setMaxAccess(_E)
if mibBuilder.loadTexts:hwWredRedMaxProb.setStatus(_A)
class _HwWredExponent_Type(Integer32):defaultValue=9;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_HwWredExponent_Type.__name__=_B
_HwWredExponent_Object=MibTableColumn
hwWredExponent=_HwWredExponent_Object((1,3,6,1,4,1,2011,2,23,1,16,2,19,1,12),_HwWredExponent_Type())
hwWredExponent.setMaxAccess(_E)
if mibBuilder.loadTexts:hwWredExponent.setStatus(_A)
_HwCosToLocalPrecedenceMapTable_Object=MibTable
hwCosToLocalPrecedenceMapTable=_HwCosToLocalPrecedenceMapTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,20))
if mibBuilder.loadTexts:hwCosToLocalPrecedenceMapTable.setStatus(_A)
_HwCosToLocalPrecedenceMapEntry_Object=MibTableRow
hwCosToLocalPrecedenceMapEntry=_HwCosToLocalPrecedenceMapEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,20,1))
hwCosToLocalPrecedenceMapEntry.setIndexNames((0,_D,_A7))
if mibBuilder.loadTexts:hwCosToLocalPrecedenceMapEntry.setStatus(_A)
class _HwCosToLocalPrecedenceMapCosIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HwCosToLocalPrecedenceMapCosIndex_Type.__name__=_B
_HwCosToLocalPrecedenceMapCosIndex_Object=MibTableColumn
hwCosToLocalPrecedenceMapCosIndex=_HwCosToLocalPrecedenceMapCosIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,20,1,1),_HwCosToLocalPrecedenceMapCosIndex_Type())
hwCosToLocalPrecedenceMapCosIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hwCosToLocalPrecedenceMapCosIndex.setStatus(_A)
class _HwCosToLocalPrecedenceMapLocalPrecedenceValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HwCosToLocalPrecedenceMapLocalPrecedenceValue_Type.__name__=_B
_HwCosToLocalPrecedenceMapLocalPrecedenceValue_Object=MibTableColumn
hwCosToLocalPrecedenceMapLocalPrecedenceValue=_HwCosToLocalPrecedenceMapLocalPrecedenceValue_Object((1,3,6,1,4,1,2011,2,23,1,16,2,20,1,2),_HwCosToLocalPrecedenceMapLocalPrecedenceValue_Type())
hwCosToLocalPrecedenceMapLocalPrecedenceValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hwCosToLocalPrecedenceMapLocalPrecedenceValue.setStatus(_A)
_HwCosToDropPrecedenceMapTable_Object=MibTable
hwCosToDropPrecedenceMapTable=_HwCosToDropPrecedenceMapTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,21))
if mibBuilder.loadTexts:hwCosToDropPrecedenceMapTable.setStatus(_A)
_HwCosToDropPrecedenceMapEntry_Object=MibTableRow
hwCosToDropPrecedenceMapEntry=_HwCosToDropPrecedenceMapEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,21,1))
hwCosToDropPrecedenceMapEntry.setIndexNames((0,_D,_A8))
if mibBuilder.loadTexts:hwCosToDropPrecedenceMapEntry.setStatus(_A)
class _HwCosToDropPrecedenceMapCosIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HwCosToDropPrecedenceMapCosIndex_Type.__name__=_B
_HwCosToDropPrecedenceMapCosIndex_Object=MibTableColumn
hwCosToDropPrecedenceMapCosIndex=_HwCosToDropPrecedenceMapCosIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,21,1,1),_HwCosToDropPrecedenceMapCosIndex_Type())
hwCosToDropPrecedenceMapCosIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hwCosToDropPrecedenceMapCosIndex.setStatus(_A)
class _HwCosToDropPrecedenceMapDropPrecedenceValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_HwCosToDropPrecedenceMapDropPrecedenceValue_Type.__name__=_B
_HwCosToDropPrecedenceMapDropPrecedenceValue_Object=MibTableColumn
hwCosToDropPrecedenceMapDropPrecedenceValue=_HwCosToDropPrecedenceMapDropPrecedenceValue_Object((1,3,6,1,4,1,2011,2,23,1,16,2,21,1,2),_HwCosToDropPrecedenceMapDropPrecedenceValue_Type())
hwCosToDropPrecedenceMapDropPrecedenceValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hwCosToDropPrecedenceMapDropPrecedenceValue.setStatus(_A)
_HwDscpMapTable_Object=MibTable
hwDscpMapTable=_HwDscpMapTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,22))
if mibBuilder.loadTexts:hwDscpMapTable.setStatus(_A)
_HwDscpMapEntry_Object=MibTableRow
hwDscpMapEntry=_HwDscpMapEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,22,1))
hwDscpMapEntry.setIndexNames((0,_D,_A9),(0,_D,_AA))
if mibBuilder.loadTexts:hwDscpMapEntry.setStatus(_A)
class _HwDscpMapConformLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_HwDscpMapConformLevel_Type.__name__=_B
_HwDscpMapConformLevel_Object=MibTableColumn
hwDscpMapConformLevel=_HwDscpMapConformLevel_Object((1,3,6,1,4,1,2011,2,23,1,16,2,22,1,1),_HwDscpMapConformLevel_Type())
hwDscpMapConformLevel.setMaxAccess(_F)
if mibBuilder.loadTexts:hwDscpMapConformLevel.setStatus(_A)
class _HwDscpMapDscpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HwDscpMapDscpIndex_Type.__name__=_B
_HwDscpMapDscpIndex_Object=MibTableColumn
hwDscpMapDscpIndex=_HwDscpMapDscpIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,22,1,2),_HwDscpMapDscpIndex_Type())
hwDscpMapDscpIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hwDscpMapDscpIndex.setStatus(_A)
class _HwDscpMapDscpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HwDscpMapDscpValue_Type.__name__=_B
_HwDscpMapDscpValue_Object=MibTableColumn
hwDscpMapDscpValue=_HwDscpMapDscpValue_Object((1,3,6,1,4,1,2011,2,23,1,16,2,22,1,3),_HwDscpMapDscpValue_Type())
hwDscpMapDscpValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hwDscpMapDscpValue.setStatus(_A)
class _HwDscpMapExpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HwDscpMapExpValue_Type.__name__=_B
_HwDscpMapExpValue_Object=MibTableColumn
hwDscpMapExpValue=_HwDscpMapExpValue_Object((1,3,6,1,4,1,2011,2,23,1,16,2,22,1,4),_HwDscpMapExpValue_Type())
hwDscpMapExpValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hwDscpMapExpValue.setStatus(_A)
class _HwDscpMapCosValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HwDscpMapCosValue_Type.__name__=_B
_HwDscpMapCosValue_Object=MibTableColumn
hwDscpMapCosValue=_HwDscpMapCosValue_Object((1,3,6,1,4,1,2011,2,23,1,16,2,22,1,5),_HwDscpMapCosValue_Type())
hwDscpMapCosValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hwDscpMapCosValue.setStatus(_A)
class _HwDscpMapLocalPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HwDscpMapLocalPrecedence_Type.__name__=_B
_HwDscpMapLocalPrecedence_Object=MibTableColumn
hwDscpMapLocalPrecedence=_HwDscpMapLocalPrecedence_Object((1,3,6,1,4,1,2011,2,23,1,16,2,22,1,6),_HwDscpMapLocalPrecedence_Type())
hwDscpMapLocalPrecedence.setMaxAccess(_E)
if mibBuilder.loadTexts:hwDscpMapLocalPrecedence.setStatus(_A)
class _HwDscpMapDropPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_HwDscpMapDropPrecedence_Type.__name__=_B
_HwDscpMapDropPrecedence_Object=MibTableColumn
hwDscpMapDropPrecedence=_HwDscpMapDropPrecedence_Object((1,3,6,1,4,1,2011,2,23,1,16,2,22,1,7),_HwDscpMapDropPrecedence_Type())
hwDscpMapDropPrecedence.setMaxAccess(_E)
if mibBuilder.loadTexts:hwDscpMapDropPrecedence.setStatus(_A)
_HwExpMapTable_Object=MibTable
hwExpMapTable=_HwExpMapTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,23))
if mibBuilder.loadTexts:hwExpMapTable.setStatus(_A)
_HwExpMapEntry_Object=MibTableRow
hwExpMapEntry=_HwExpMapEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,23,1))
hwExpMapEntry.setIndexNames((0,_D,_AB),(0,_D,_AC))
if mibBuilder.loadTexts:hwExpMapEntry.setStatus(_A)
class _HwExpMapConformLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_HwExpMapConformLevel_Type.__name__=_B
_HwExpMapConformLevel_Object=MibTableColumn
hwExpMapConformLevel=_HwExpMapConformLevel_Object((1,3,6,1,4,1,2011,2,23,1,16,2,23,1,1),_HwExpMapConformLevel_Type())
hwExpMapConformLevel.setMaxAccess(_F)
if mibBuilder.loadTexts:hwExpMapConformLevel.setStatus(_A)
class _HwExpMapExpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HwExpMapExpIndex_Type.__name__=_B
_HwExpMapExpIndex_Object=MibTableColumn
hwExpMapExpIndex=_HwExpMapExpIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,23,1,2),_HwExpMapExpIndex_Type())
hwExpMapExpIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hwExpMapExpIndex.setStatus(_A)
class _HwExpMapDscpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HwExpMapDscpValue_Type.__name__=_B
_HwExpMapDscpValue_Object=MibTableColumn
hwExpMapDscpValue=_HwExpMapDscpValue_Object((1,3,6,1,4,1,2011,2,23,1,16,2,23,1,3),_HwExpMapDscpValue_Type())
hwExpMapDscpValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hwExpMapDscpValue.setStatus(_A)
class _HwExpMapExpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HwExpMapExpValue_Type.__name__=_B
_HwExpMapExpValue_Object=MibTableColumn
hwExpMapExpValue=_HwExpMapExpValue_Object((1,3,6,1,4,1,2011,2,23,1,16,2,23,1,4),_HwExpMapExpValue_Type())
hwExpMapExpValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hwExpMapExpValue.setStatus(_A)
class _HwExpMapCosValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HwExpMapCosValue_Type.__name__=_B
_HwExpMapCosValue_Object=MibTableColumn
hwExpMapCosValue=_HwExpMapCosValue_Object((1,3,6,1,4,1,2011,2,23,1,16,2,23,1,5),_HwExpMapCosValue_Type())
hwExpMapCosValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hwExpMapCosValue.setStatus(_A)
class _HwExpMapLocalPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HwExpMapLocalPrecedence_Type.__name__=_B
_HwExpMapLocalPrecedence_Object=MibTableColumn
hwExpMapLocalPrecedence=_HwExpMapLocalPrecedence_Object((1,3,6,1,4,1,2011,2,23,1,16,2,23,1,6),_HwExpMapLocalPrecedence_Type())
hwExpMapLocalPrecedence.setMaxAccess(_E)
if mibBuilder.loadTexts:hwExpMapLocalPrecedence.setStatus(_A)
class _HwExpMapDropPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_HwExpMapDropPrecedence_Type.__name__=_B
_HwExpMapDropPrecedence_Object=MibTableColumn
hwExpMapDropPrecedence=_HwExpMapDropPrecedence_Object((1,3,6,1,4,1,2011,2,23,1,16,2,23,1,7),_HwExpMapDropPrecedence_Type())
hwExpMapDropPrecedence.setMaxAccess(_E)
if mibBuilder.loadTexts:hwExpMapDropPrecedence.setStatus(_A)
_HwLocalPrecedenceMapTable_Object=MibTable
hwLocalPrecedenceMapTable=_HwLocalPrecedenceMapTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,24))
if mibBuilder.loadTexts:hwLocalPrecedenceMapTable.setStatus(_A)
_HwLocalPrecedenceMapEntry_Object=MibTableRow
hwLocalPrecedenceMapEntry=_HwLocalPrecedenceMapEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,24,1))
hwLocalPrecedenceMapEntry.setIndexNames((0,_D,_AD),(0,_D,_AE))
if mibBuilder.loadTexts:hwLocalPrecedenceMapEntry.setStatus(_A)
class _HwLocalPrecedenceMapConformLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_HwLocalPrecedenceMapConformLevel_Type.__name__=_B
_HwLocalPrecedenceMapConformLevel_Object=MibTableColumn
hwLocalPrecedenceMapConformLevel=_HwLocalPrecedenceMapConformLevel_Object((1,3,6,1,4,1,2011,2,23,1,16,2,24,1,1),_HwLocalPrecedenceMapConformLevel_Type())
hwLocalPrecedenceMapConformLevel.setMaxAccess(_F)
if mibBuilder.loadTexts:hwLocalPrecedenceMapConformLevel.setStatus(_A)
class _HwLocalPrecedenceMapLocalPrecedenceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HwLocalPrecedenceMapLocalPrecedenceIndex_Type.__name__=_B
_HwLocalPrecedenceMapLocalPrecedenceIndex_Object=MibTableColumn
hwLocalPrecedenceMapLocalPrecedenceIndex=_HwLocalPrecedenceMapLocalPrecedenceIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,24,1,2),_HwLocalPrecedenceMapLocalPrecedenceIndex_Type())
hwLocalPrecedenceMapLocalPrecedenceIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hwLocalPrecedenceMapLocalPrecedenceIndex.setStatus(_A)
class _HwLocalPrecedenceMapCosValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HwLocalPrecedenceMapCosValue_Type.__name__=_B
_HwLocalPrecedenceMapCosValue_Object=MibTableColumn
hwLocalPrecedenceMapCosValue=_HwLocalPrecedenceMapCosValue_Object((1,3,6,1,4,1,2011,2,23,1,16,2,24,1,3),_HwLocalPrecedenceMapCosValue_Type())
hwLocalPrecedenceMapCosValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hwLocalPrecedenceMapCosValue.setStatus(_A)
_HwPortWredTable_Object=MibTable
hwPortWredTable=_HwPortWredTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,25))
if mibBuilder.loadTexts:hwPortWredTable.setStatus(_A)
_HwPortWredEntry_Object=MibTableRow
hwPortWredEntry=_HwPortWredEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,25,1))
hwPortWredEntry.setIndexNames((0,_D,_AF),(0,_D,_AG))
if mibBuilder.loadTexts:hwPortWredEntry.setStatus(_A)
_HwPortWredIfIndex_Type=Integer32
_HwPortWredIfIndex_Object=MibTableColumn
hwPortWredIfIndex=_HwPortWredIfIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,25,1,1),_HwPortWredIfIndex_Type())
hwPortWredIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hwPortWredIfIndex.setStatus(_A)
class _HwPortWredQueueID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HwPortWredQueueID_Type.__name__=_B
_HwPortWredQueueID_Object=MibTableColumn
hwPortWredQueueID=_HwPortWredQueueID_Object((1,3,6,1,4,1,2011,2,23,1,16,2,25,1,2),_HwPortWredQueueID_Type())
hwPortWredQueueID.setMaxAccess(_F)
if mibBuilder.loadTexts:hwPortWredQueueID.setStatus(_A)
class _HwPortWredQueueStartLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2047))
_HwPortWredQueueStartLength_Type.__name__=_B
_HwPortWredQueueStartLength_Object=MibTableColumn
hwPortWredQueueStartLength=_HwPortWredQueueStartLength_Object((1,3,6,1,4,1,2011,2,23,1,16,2,25,1,3),_HwPortWredQueueStartLength_Type())
hwPortWredQueueStartLength.setMaxAccess(_E)
if mibBuilder.loadTexts:hwPortWredQueueStartLength.setStatus(_A)
class _HwPortWredQueueProbability_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HwPortWredQueueProbability_Type.__name__=_B
_HwPortWredQueueProbability_Object=MibTableColumn
hwPortWredQueueProbability=_HwPortWredQueueProbability_Object((1,3,6,1,4,1,2011,2,23,1,16,2,25,1,4),_HwPortWredQueueProbability_Type())
hwPortWredQueueProbability.setMaxAccess(_E)
if mibBuilder.loadTexts:hwPortWredQueueProbability.setStatus(_A)
_HwMirroringGroupTable_Object=MibTable
hwMirroringGroupTable=_HwMirroringGroupTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,26))
if mibBuilder.loadTexts:hwMirroringGroupTable.setStatus(_A)
_HwMirroringGroupEntry_Object=MibTableRow
hwMirroringGroupEntry=_HwMirroringGroupEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,26,1))
hwMirroringGroupEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:hwMirroringGroupEntry.setStatus(_A)
class _HwMirroringGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_HwMirroringGroupID_Type.__name__=_B
_HwMirroringGroupID_Object=MibTableColumn
hwMirroringGroupID=_HwMirroringGroupID_Object((1,3,6,1,4,1,2011,2,23,1,16,2,26,1,1),_HwMirroringGroupID_Type())
hwMirroringGroupID.setMaxAccess(_G)
if mibBuilder.loadTexts:hwMirroringGroupID.setStatus(_A)
class _HwMirroringGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('local',1),('remote-source',2),('remote-destination',3)))
_HwMirroringGroupType_Type.__name__=_B
_HwMirroringGroupType_Object=MibTableColumn
hwMirroringGroupType=_HwMirroringGroupType_Object((1,3,6,1,4,1,2011,2,23,1,16,2,26,1,2),_HwMirroringGroupType_Type())
hwMirroringGroupType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirroringGroupType.setStatus(_A)
class _HwMirroringGroupStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_HwMirroringGroupStatus_Type.__name__=_B
_HwMirroringGroupStatus_Object=MibTableColumn
hwMirroringGroupStatus=_HwMirroringGroupStatus_Object((1,3,6,1,4,1,2011,2,23,1,16,2,26,1,3),_HwMirroringGroupStatus_Type())
hwMirroringGroupStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hwMirroringGroupStatus.setStatus(_A)
_HwMirroringGroupRowStatus_Type=RowStatus
_HwMirroringGroupRowStatus_Object=MibTableColumn
hwMirroringGroupRowStatus=_HwMirroringGroupRowStatus_Object((1,3,6,1,4,1,2011,2,23,1,16,2,26,1,4),_HwMirroringGroupRowStatus_Type())
hwMirroringGroupRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirroringGroupRowStatus.setStatus(_A)
_HwMirroringGroupMirrorTable_Object=MibTable
hwMirroringGroupMirrorTable=_HwMirroringGroupMirrorTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,27))
if mibBuilder.loadTexts:hwMirroringGroupMirrorTable.setStatus(_A)
_HwMirroringGroupMirrorEntry_Object=MibTableRow
hwMirroringGroupMirrorEntry=_HwMirroringGroupMirrorEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,27,1))
hwMirroringGroupMirrorEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:hwMirroringGroupMirrorEntry.setStatus(_A)
_HwMirroringGroupMirrorInboundIfIndexList_Type=OctetString
_HwMirroringGroupMirrorInboundIfIndexList_Object=MibTableColumn
hwMirroringGroupMirrorInboundIfIndexList=_HwMirroringGroupMirrorInboundIfIndexList_Object((1,3,6,1,4,1,2011,2,23,1,16,2,27,1,1),_HwMirroringGroupMirrorInboundIfIndexList_Type())
hwMirroringGroupMirrorInboundIfIndexList.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirroringGroupMirrorInboundIfIndexList.setStatus(_A)
_HwMirroringGroupMirrorOutboundIfIndexList_Type=OctetString
_HwMirroringGroupMirrorOutboundIfIndexList_Object=MibTableColumn
hwMirroringGroupMirrorOutboundIfIndexList=_HwMirroringGroupMirrorOutboundIfIndexList_Object((1,3,6,1,4,1,2011,2,23,1,16,2,27,1,2),_HwMirroringGroupMirrorOutboundIfIndexList_Type())
hwMirroringGroupMirrorOutboundIfIndexList.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirroringGroupMirrorOutboundIfIndexList.setStatus(_A)
_HwMirroringGroupMirrorRowStatus_Type=RowStatus
_HwMirroringGroupMirrorRowStatus_Object=MibTableColumn
hwMirroringGroupMirrorRowStatus=_HwMirroringGroupMirrorRowStatus_Object((1,3,6,1,4,1,2011,2,23,1,16,2,27,1,3),_HwMirroringGroupMirrorRowStatus_Type())
hwMirroringGroupMirrorRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirroringGroupMirrorRowStatus.setStatus(_A)
_HwMirroringGroupMirrorInTypeList_Type=OctetString
_HwMirroringGroupMirrorInTypeList_Object=MibTableColumn
hwMirroringGroupMirrorInTypeList=_HwMirroringGroupMirrorInTypeList_Object((1,3,6,1,4,1,2011,2,23,1,16,2,27,1,4),_HwMirroringGroupMirrorInTypeList_Type())
hwMirroringGroupMirrorInTypeList.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirroringGroupMirrorInTypeList.setStatus(_A)
_HwMirroringGroupMirrorOutTypeList_Type=OctetString
_HwMirroringGroupMirrorOutTypeList_Object=MibTableColumn
hwMirroringGroupMirrorOutTypeList=_HwMirroringGroupMirrorOutTypeList_Object((1,3,6,1,4,1,2011,2,23,1,16,2,27,1,5),_HwMirroringGroupMirrorOutTypeList_Type())
hwMirroringGroupMirrorOutTypeList.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirroringGroupMirrorOutTypeList.setStatus(_A)
_HwMirroringGroupMonitorTable_Object=MibTable
hwMirroringGroupMonitorTable=_HwMirroringGroupMonitorTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,28))
if mibBuilder.loadTexts:hwMirroringGroupMonitorTable.setStatus(_A)
_HwMirroringGroupMonitorEntry_Object=MibTableRow
hwMirroringGroupMonitorEntry=_HwMirroringGroupMonitorEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,28,1))
hwMirroringGroupMonitorEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:hwMirroringGroupMonitorEntry.setStatus(_A)
_HwMirroringGroupMonitorIfIndex_Type=Integer32
_HwMirroringGroupMonitorIfIndex_Object=MibTableColumn
hwMirroringGroupMonitorIfIndex=_HwMirroringGroupMonitorIfIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,28,1,1),_HwMirroringGroupMonitorIfIndex_Type())
hwMirroringGroupMonitorIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirroringGroupMonitorIfIndex.setStatus(_A)
_HwMirroringGroupMonitorRowStatus_Type=RowStatus
_HwMirroringGroupMonitorRowStatus_Object=MibTableColumn
hwMirroringGroupMonitorRowStatus=_HwMirroringGroupMonitorRowStatus_Object((1,3,6,1,4,1,2011,2,23,1,16,2,28,1,2),_HwMirroringGroupMonitorRowStatus_Type())
hwMirroringGroupMonitorRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirroringGroupMonitorRowStatus.setStatus(_A)
_HwMirroringGroupMonitorType_Type=HwMirrorOrMonitorType
_HwMirroringGroupMonitorType_Object=MibTableColumn
hwMirroringGroupMonitorType=_HwMirroringGroupMonitorType_Object((1,3,6,1,4,1,2011,2,23,1,16,2,28,1,3),_HwMirroringGroupMonitorType_Type())
hwMirroringGroupMonitorType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirroringGroupMonitorType.setStatus(_A)
_HwMirroringGroupReflectorTable_Object=MibTable
hwMirroringGroupReflectorTable=_HwMirroringGroupReflectorTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,29))
if mibBuilder.loadTexts:hwMirroringGroupReflectorTable.setStatus(_A)
_HwMirroringGroupReflectorEntry_Object=MibTableRow
hwMirroringGroupReflectorEntry=_HwMirroringGroupReflectorEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,29,1))
hwMirroringGroupReflectorEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:hwMirroringGroupReflectorEntry.setStatus(_A)
_HwMirroringGroupReflectorIfIndex_Type=Integer32
_HwMirroringGroupReflectorIfIndex_Object=MibTableColumn
hwMirroringGroupReflectorIfIndex=_HwMirroringGroupReflectorIfIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,29,1,1),_HwMirroringGroupReflectorIfIndex_Type())
hwMirroringGroupReflectorIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirroringGroupReflectorIfIndex.setStatus(_A)
_HwMirroringGroupReflectorRowStatus_Type=RowStatus
_HwMirroringGroupReflectorRowStatus_Object=MibTableColumn
hwMirroringGroupReflectorRowStatus=_HwMirroringGroupReflectorRowStatus_Object((1,3,6,1,4,1,2011,2,23,1,16,2,29,1,2),_HwMirroringGroupReflectorRowStatus_Type())
hwMirroringGroupReflectorRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirroringGroupReflectorRowStatus.setStatus(_A)
_HwMirroringGroupRprobeVlanTable_Object=MibTable
hwMirroringGroupRprobeVlanTable=_HwMirroringGroupRprobeVlanTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,30))
if mibBuilder.loadTexts:hwMirroringGroupRprobeVlanTable.setStatus(_A)
_HwMirroringGroupRprobeVlanEntry_Object=MibTableRow
hwMirroringGroupRprobeVlanEntry=_HwMirroringGroupRprobeVlanEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,30,1))
hwMirroringGroupRprobeVlanEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:hwMirroringGroupRprobeVlanEntry.setStatus(_A)
class _HwMirroringGroupRprobeVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HwMirroringGroupRprobeVlanID_Type.__name__=_B
_HwMirroringGroupRprobeVlanID_Object=MibTableColumn
hwMirroringGroupRprobeVlanID=_HwMirroringGroupRprobeVlanID_Object((1,3,6,1,4,1,2011,2,23,1,16,2,30,1,1),_HwMirroringGroupRprobeVlanID_Type())
hwMirroringGroupRprobeVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirroringGroupRprobeVlanID.setStatus(_A)
_HwMirroringGroupRprobeVlanRowStatus_Type=RowStatus
_HwMirroringGroupRprobeVlanRowStatus_Object=MibTableColumn
hwMirroringGroupRprobeVlanRowStatus=_HwMirroringGroupRprobeVlanRowStatus_Object((1,3,6,1,4,1,2011,2,23,1,16,2,30,1,2),_HwMirroringGroupRprobeVlanRowStatus_Type())
hwMirroringGroupRprobeVlanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirroringGroupRprobeVlanRowStatus.setStatus(_A)
_HwMirroringGroupMirrorMacTable_Object=MibTable
hwMirroringGroupMirrorMacTable=_HwMirroringGroupMirrorMacTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,31))
if mibBuilder.loadTexts:hwMirroringGroupMirrorMacTable.setStatus(_A)
_HwMirroringGroupMirrorMacEntry_Object=MibTableRow
hwMirroringGroupMirrorMacEntry=_HwMirroringGroupMirrorMacEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,31,1))
hwMirroringGroupMirrorMacEntry.setIndexNames((0,_D,_J),(0,_D,_AH))
if mibBuilder.loadTexts:hwMirroringGroupMirrorMacEntry.setStatus(_A)
_HwMirroringGroupMirrorMacSeq_Type=Integer32
_HwMirroringGroupMirrorMacSeq_Object=MibTableColumn
hwMirroringGroupMirrorMacSeq=_HwMirroringGroupMirrorMacSeq_Object((1,3,6,1,4,1,2011,2,23,1,16,2,31,1,1),_HwMirroringGroupMirrorMacSeq_Type())
hwMirroringGroupMirrorMacSeq.setMaxAccess(_G)
if mibBuilder.loadTexts:hwMirroringGroupMirrorMacSeq.setStatus(_A)
_HwMirroringGroupMirrorMac_Type=MacAddress
_HwMirroringGroupMirrorMac_Object=MibTableColumn
hwMirroringGroupMirrorMac=_HwMirroringGroupMirrorMac_Object((1,3,6,1,4,1,2011,2,23,1,16,2,31,1,2),_HwMirroringGroupMirrorMac_Type())
hwMirroringGroupMirrorMac.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirroringGroupMirrorMac.setStatus(_A)
class _HwMirrorMacVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HwMirrorMacVlanID_Type.__name__=_B
_HwMirrorMacVlanID_Object=MibTableColumn
hwMirrorMacVlanID=_HwMirrorMacVlanID_Object((1,3,6,1,4,1,2011,2,23,1,16,2,31,1,3),_HwMirrorMacVlanID_Type())
hwMirrorMacVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirrorMacVlanID.setStatus(_A)
_HwMirroringGroupMirroMacStatus_Type=RowStatus
_HwMirroringGroupMirroMacStatus_Object=MibTableColumn
hwMirroringGroupMirroMacStatus=_HwMirroringGroupMirroMacStatus_Object((1,3,6,1,4,1,2011,2,23,1,16,2,31,1,4),_HwMirroringGroupMirroMacStatus_Type())
hwMirroringGroupMirroMacStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirroringGroupMirroMacStatus.setStatus(_A)
_HwMirroringGroupMirrorVlanTable_Object=MibTable
hwMirroringGroupMirrorVlanTable=_HwMirroringGroupMirrorVlanTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,32))
if mibBuilder.loadTexts:hwMirroringGroupMirrorVlanTable.setStatus(_A)
_HwMirroringGroupMirrorVlanEntry_Object=MibTableRow
hwMirroringGroupMirrorVlanEntry=_HwMirroringGroupMirrorVlanEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,32,1))
hwMirroringGroupMirrorVlanEntry.setIndexNames((0,_D,_J),(0,_D,_AI))
if mibBuilder.loadTexts:hwMirroringGroupMirrorVlanEntry.setStatus(_A)
_HwMirroringGroupMirrorVlanSeq_Type=Integer32
_HwMirroringGroupMirrorVlanSeq_Object=MibTableColumn
hwMirroringGroupMirrorVlanSeq=_HwMirroringGroupMirrorVlanSeq_Object((1,3,6,1,4,1,2011,2,23,1,16,2,32,1,1),_HwMirroringGroupMirrorVlanSeq_Type())
hwMirroringGroupMirrorVlanSeq.setMaxAccess(_G)
if mibBuilder.loadTexts:hwMirroringGroupMirrorVlanSeq.setStatus(_A)
class _HwMirroringGroupMirrorVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HwMirroringGroupMirrorVlanID_Type.__name__=_B
_HwMirroringGroupMirrorVlanID_Object=MibTableColumn
hwMirroringGroupMirrorVlanID=_HwMirroringGroupMirrorVlanID_Object((1,3,6,1,4,1,2011,2,23,1,16,2,32,1,2),_HwMirroringGroupMirrorVlanID_Type())
hwMirroringGroupMirrorVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirroringGroupMirrorVlanID.setStatus(_A)
class _HwMirroringGroupMirrorVlanDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inbound',1),('outbound',2),('both',3)))
_HwMirroringGroupMirrorVlanDirection_Type.__name__=_B
_HwMirroringGroupMirrorVlanDirection_Object=MibTableColumn
hwMirroringGroupMirrorVlanDirection=_HwMirroringGroupMirrorVlanDirection_Object((1,3,6,1,4,1,2011,2,23,1,16,2,32,1,3),_HwMirroringGroupMirrorVlanDirection_Type())
hwMirroringGroupMirrorVlanDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirroringGroupMirrorVlanDirection.setStatus(_A)
_HwMirroringGroupMirroVlanStatus_Type=RowStatus
_HwMirroringGroupMirroVlanStatus_Object=MibTableColumn
hwMirroringGroupMirroVlanStatus=_HwMirroringGroupMirroVlanStatus_Object((1,3,6,1,4,1,2011,2,23,1,16,2,32,1,4),_HwMirroringGroupMirroVlanStatus_Type())
hwMirroringGroupMirroVlanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwMirroringGroupMirroVlanStatus.setStatus(_A)
_HwPortTrustTable_Object=MibTable
hwPortTrustTable=_HwPortTrustTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,33))
if mibBuilder.loadTexts:hwPortTrustTable.setStatus(_A)
_HwPortTrustEntry_Object=MibTableRow
hwPortTrustEntry=_HwPortTrustEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,33,1))
hwPortTrustEntry.setIndexNames((0,_D,_AJ))
if mibBuilder.loadTexts:hwPortTrustEntry.setStatus(_A)
_HwPortTrustIfIndex_Type=Integer32
_HwPortTrustIfIndex_Object=MibTableColumn
hwPortTrustIfIndex=_HwPortTrustIfIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,33,1,1),_HwPortTrustIfIndex_Type())
hwPortTrustIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hwPortTrustIfIndex.setStatus(_A)
class _HwPortTrustTrustType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('port',1),('cos',2),('dscp',3)))
_HwPortTrustTrustType_Type.__name__=_B
_HwPortTrustTrustType_Object=MibTableColumn
hwPortTrustTrustType=_HwPortTrustTrustType_Object((1,3,6,1,4,1,2011,2,23,1,16,2,33,1,2),_HwPortTrustTrustType_Type())
hwPortTrustTrustType.setMaxAccess(_E)
if mibBuilder.loadTexts:hwPortTrustTrustType.setStatus(_A)
class _HwPortTrustOvercastType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noOvercast',1),('overcastDSCP',2),('overcastCOS',3)))
_HwPortTrustOvercastType_Type.__name__=_B
_HwPortTrustOvercastType_Object=MibTableColumn
hwPortTrustOvercastType=_HwPortTrustOvercastType_Object((1,3,6,1,4,1,2011,2,23,1,16,2,33,1,3),_HwPortTrustOvercastType_Type())
hwPortTrustOvercastType.setMaxAccess(_E)
if mibBuilder.loadTexts:hwPortTrustOvercastType.setStatus(_A)
class _HwPortTrustReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_L,1))
_HwPortTrustReset_Type.__name__=_B
_HwPortTrustReset_Object=MibTableColumn
hwPortTrustReset=_HwPortTrustReset_Object((1,3,6,1,4,1,2011,2,23,1,16,2,33,1,4),_HwPortTrustReset_Type())
hwPortTrustReset.setMaxAccess(_E)
if mibBuilder.loadTexts:hwPortTrustReset.setStatus(_A)
_HwRemarkVlanIDTable_Object=MibTable
hwRemarkVlanIDTable=_HwRemarkVlanIDTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,34))
if mibBuilder.loadTexts:hwRemarkVlanIDTable.setStatus(_A)
_HwRemarkVlanIDEntry_Object=MibTableRow
hwRemarkVlanIDEntry=_HwRemarkVlanIDEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,34,1))
hwRemarkVlanIDEntry.setIndexNames((0,_D,_AK),(0,_D,_AL),(0,_D,_AM),(0,_D,_AN))
if mibBuilder.loadTexts:hwRemarkVlanIDEntry.setStatus(_A)
class _HwRemarkVlanIDAclIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2999))
_HwRemarkVlanIDAclIndex_Type.__name__=_B
_HwRemarkVlanIDAclIndex_Object=MibTableColumn
hwRemarkVlanIDAclIndex=_HwRemarkVlanIDAclIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,34,1,1),_HwRemarkVlanIDAclIndex_Type())
hwRemarkVlanIDAclIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hwRemarkVlanIDAclIndex.setStatus(_A)
_HwRemarkVlanIDIfIndex_Type=Integer32
_HwRemarkVlanIDIfIndex_Object=MibTableColumn
hwRemarkVlanIDIfIndex=_HwRemarkVlanIDIfIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,34,1,2),_HwRemarkVlanIDIfIndex_Type())
hwRemarkVlanIDIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hwRemarkVlanIDIfIndex.setStatus(_A)
class _HwRemarkVlanIDVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HwRemarkVlanIDVlanID_Type.__name__=_B
_HwRemarkVlanIDVlanID_Object=MibTableColumn
hwRemarkVlanIDVlanID=_HwRemarkVlanIDVlanID_Object((1,3,6,1,4,1,2011,2,23,1,16,2,34,1,3),_HwRemarkVlanIDVlanID_Type())
hwRemarkVlanIDVlanID.setMaxAccess(_G)
if mibBuilder.loadTexts:hwRemarkVlanIDVlanID.setStatus(_A)
class _HwRemarkVlanIDDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_H,0),(_K,1),(_I,2)))
_HwRemarkVlanIDDirection_Type.__name__=_B
_HwRemarkVlanIDDirection_Object=MibTableColumn
hwRemarkVlanIDDirection=_HwRemarkVlanIDDirection_Object((1,3,6,1,4,1,2011,2,23,1,16,2,34,1,4),_HwRemarkVlanIDDirection_Type())
hwRemarkVlanIDDirection.setMaxAccess(_G)
if mibBuilder.loadTexts:hwRemarkVlanIDDirection.setStatus(_A)
class _HwRemarkVlanIDUserAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(5000,5999),ValueRangeConstraint(10000,12999))
_HwRemarkVlanIDUserAclNum_Type.__name__=_B
_HwRemarkVlanIDUserAclNum_Object=MibTableColumn
hwRemarkVlanIDUserAclNum=_HwRemarkVlanIDUserAclNum_Object((1,3,6,1,4,1,2011,2,23,1,16,2,34,1,5),_HwRemarkVlanIDUserAclNum_Type())
hwRemarkVlanIDUserAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRemarkVlanIDUserAclNum.setStatus(_A)
class _HwRemarkVlanIDUserAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwRemarkVlanIDUserAclRule_Type.__name__=_B
_HwRemarkVlanIDUserAclRule_Object=MibTableColumn
hwRemarkVlanIDUserAclRule=_HwRemarkVlanIDUserAclRule_Object((1,3,6,1,4,1,2011,2,23,1,16,2,34,1,6),_HwRemarkVlanIDUserAclRule_Type())
hwRemarkVlanIDUserAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRemarkVlanIDUserAclRule.setStatus(_A)
class _HwRemarkVlanIDIpAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2000,3999),ValueRangeConstraint(10000,12999))
_HwRemarkVlanIDIpAclNum_Type.__name__=_B
_HwRemarkVlanIDIpAclNum_Object=MibTableColumn
hwRemarkVlanIDIpAclNum=_HwRemarkVlanIDIpAclNum_Object((1,3,6,1,4,1,2011,2,23,1,16,2,34,1,7),_HwRemarkVlanIDIpAclNum_Type())
hwRemarkVlanIDIpAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRemarkVlanIDIpAclNum.setStatus(_A)
class _HwRemarkVlanIDIpAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwRemarkVlanIDIpAclRule_Type.__name__=_B
_HwRemarkVlanIDIpAclRule_Object=MibTableColumn
hwRemarkVlanIDIpAclRule=_HwRemarkVlanIDIpAclRule_Object((1,3,6,1,4,1,2011,2,23,1,16,2,34,1,8),_HwRemarkVlanIDIpAclRule_Type())
hwRemarkVlanIDIpAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRemarkVlanIDIpAclRule.setStatus(_A)
class _HwRemarkVlanIDLinkAclNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4000,4999),ValueRangeConstraint(10000,12999))
_HwRemarkVlanIDLinkAclNum_Type.__name__=_B
_HwRemarkVlanIDLinkAclNum_Object=MibTableColumn
hwRemarkVlanIDLinkAclNum=_HwRemarkVlanIDLinkAclNum_Object((1,3,6,1,4,1,2011,2,23,1,16,2,34,1,9),_HwRemarkVlanIDLinkAclNum_Type())
hwRemarkVlanIDLinkAclNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRemarkVlanIDLinkAclNum.setStatus(_A)
class _HwRemarkVlanIDLinkAclRule_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HwRemarkVlanIDLinkAclRule_Type.__name__=_B
_HwRemarkVlanIDLinkAclRule_Object=MibTableColumn
hwRemarkVlanIDLinkAclRule=_HwRemarkVlanIDLinkAclRule_Object((1,3,6,1,4,1,2011,2,23,1,16,2,34,1,10),_HwRemarkVlanIDLinkAclRule_Type())
hwRemarkVlanIDLinkAclRule.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRemarkVlanIDLinkAclRule.setStatus(_A)
class _HwRemarkVlanIDRemarkVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HwRemarkVlanIDRemarkVlanID_Type.__name__=_B
_HwRemarkVlanIDRemarkVlanID_Object=MibTableColumn
hwRemarkVlanIDRemarkVlanID=_HwRemarkVlanIDRemarkVlanID_Object((1,3,6,1,4,1,2011,2,23,1,16,2,34,1,11),_HwRemarkVlanIDRemarkVlanID_Type())
hwRemarkVlanIDRemarkVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRemarkVlanIDRemarkVlanID.setStatus(_A)
class _HwRemarkVlanIDPacketType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('all',1),('tagged',2),('untagged',3)))
_HwRemarkVlanIDPacketType_Type.__name__=_B
_HwRemarkVlanIDPacketType_Object=MibTableColumn
hwRemarkVlanIDPacketType=_HwRemarkVlanIDPacketType_Object((1,3,6,1,4,1,2011,2,23,1,16,2,34,1,12),_HwRemarkVlanIDPacketType_Type())
hwRemarkVlanIDPacketType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRemarkVlanIDPacketType.setStatus(_A)
_HwRemarkVlanIDRowStatus_Type=RowStatus
_HwRemarkVlanIDRowStatus_Object=MibTableColumn
hwRemarkVlanIDRowStatus=_HwRemarkVlanIDRowStatus_Object((1,3,6,1,4,1,2011,2,23,1,16,2,34,1,13),_HwRemarkVlanIDRowStatus_Type())
hwRemarkVlanIDRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwRemarkVlanIDRowStatus.setStatus(_A)
_HwCosToDscpMapTable_Object=MibTable
hwCosToDscpMapTable=_HwCosToDscpMapTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,35))
if mibBuilder.loadTexts:hwCosToDscpMapTable.setStatus(_A)
_HwCosToDscpMapEntry_Object=MibTableRow
hwCosToDscpMapEntry=_HwCosToDscpMapEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,35,1))
hwCosToDscpMapEntry.setIndexNames((0,_D,_AO))
if mibBuilder.loadTexts:hwCosToDscpMapEntry.setStatus(_A)
class _HwCosToDscpMapCosIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HwCosToDscpMapCosIndex_Type.__name__=_B
_HwCosToDscpMapCosIndex_Object=MibTableColumn
hwCosToDscpMapCosIndex=_HwCosToDscpMapCosIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,35,1,1),_HwCosToDscpMapCosIndex_Type())
hwCosToDscpMapCosIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hwCosToDscpMapCosIndex.setStatus(_A)
class _HwCosToDscpMapDscpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HwCosToDscpMapDscpValue_Type.__name__=_B
_HwCosToDscpMapDscpValue_Object=MibTableColumn
hwCosToDscpMapDscpValue=_HwCosToDscpMapDscpValue_Object((1,3,6,1,4,1,2011,2,23,1,16,2,35,1,2),_HwCosToDscpMapDscpValue_Type())
hwCosToDscpMapDscpValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hwCosToDscpMapDscpValue.setStatus(_A)
class _HwCosToDscpMapReSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_L,1))
_HwCosToDscpMapReSet_Type.__name__=_B
_HwCosToDscpMapReSet_Object=MibTableColumn
hwCosToDscpMapReSet=_HwCosToDscpMapReSet_Object((1,3,6,1,4,1,2011,2,23,1,16,2,35,1,3),_HwCosToDscpMapReSet_Type())
hwCosToDscpMapReSet.setMaxAccess(_E)
if mibBuilder.loadTexts:hwCosToDscpMapReSet.setStatus(_A)
_HwDscpToLocalPreMapTable_Object=MibTable
hwDscpToLocalPreMapTable=_HwDscpToLocalPreMapTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,36))
if mibBuilder.loadTexts:hwDscpToLocalPreMapTable.setStatus(_A)
_HwDscpToLocalPreMapEntry_Object=MibTableRow
hwDscpToLocalPreMapEntry=_HwDscpToLocalPreMapEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,36,1))
hwDscpToLocalPreMapEntry.setIndexNames((0,_D,_AP))
if mibBuilder.loadTexts:hwDscpToLocalPreMapEntry.setStatus(_A)
class _HwDscpToLocalPreMapDscpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HwDscpToLocalPreMapDscpIndex_Type.__name__=_B
_HwDscpToLocalPreMapDscpIndex_Object=MibTableColumn
hwDscpToLocalPreMapDscpIndex=_HwDscpToLocalPreMapDscpIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,36,1,1),_HwDscpToLocalPreMapDscpIndex_Type())
hwDscpToLocalPreMapDscpIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hwDscpToLocalPreMapDscpIndex.setStatus(_A)
class _HwDscpToLocalPreMapLocalPreVal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HwDscpToLocalPreMapLocalPreVal_Type.__name__=_B
_HwDscpToLocalPreMapLocalPreVal_Object=MibTableColumn
hwDscpToLocalPreMapLocalPreVal=_HwDscpToLocalPreMapLocalPreVal_Object((1,3,6,1,4,1,2011,2,23,1,16,2,36,1,2),_HwDscpToLocalPreMapLocalPreVal_Type())
hwDscpToLocalPreMapLocalPreVal.setMaxAccess(_E)
if mibBuilder.loadTexts:hwDscpToLocalPreMapLocalPreVal.setStatus(_A)
class _HwDscpToLocalPreMapReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_L,1))
_HwDscpToLocalPreMapReset_Type.__name__=_B
_HwDscpToLocalPreMapReset_Object=MibTableColumn
hwDscpToLocalPreMapReset=_HwDscpToLocalPreMapReset_Object((1,3,6,1,4,1,2011,2,23,1,16,2,36,1,3),_HwDscpToLocalPreMapReset_Type())
hwDscpToLocalPreMapReset.setMaxAccess(_E)
if mibBuilder.loadTexts:hwDscpToLocalPreMapReset.setStatus(_A)
_HwDscpToDropPreMapTable_Object=MibTable
hwDscpToDropPreMapTable=_HwDscpToDropPreMapTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,37))
if mibBuilder.loadTexts:hwDscpToDropPreMapTable.setStatus(_A)
_HwDscpToDropPreMapEntry_Object=MibTableRow
hwDscpToDropPreMapEntry=_HwDscpToDropPreMapEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,37,1))
hwDscpToDropPreMapEntry.setIndexNames((0,_D,_AQ))
if mibBuilder.loadTexts:hwDscpToDropPreMapEntry.setStatus(_A)
class _HwDscpToDropPreMapDscpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HwDscpToDropPreMapDscpIndex_Type.__name__=_B
_HwDscpToDropPreMapDscpIndex_Object=MibTableColumn
hwDscpToDropPreMapDscpIndex=_HwDscpToDropPreMapDscpIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,37,1,1),_HwDscpToDropPreMapDscpIndex_Type())
hwDscpToDropPreMapDscpIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hwDscpToDropPreMapDscpIndex.setStatus(_A)
class _HwDscpToDropPreMapDropPreVal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_HwDscpToDropPreMapDropPreVal_Type.__name__=_B
_HwDscpToDropPreMapDropPreVal_Object=MibTableColumn
hwDscpToDropPreMapDropPreVal=_HwDscpToDropPreMapDropPreVal_Object((1,3,6,1,4,1,2011,2,23,1,16,2,37,1,2),_HwDscpToDropPreMapDropPreVal_Type())
hwDscpToDropPreMapDropPreVal.setMaxAccess(_E)
if mibBuilder.loadTexts:hwDscpToDropPreMapDropPreVal.setStatus(_A)
class _HwDscpToDropPreMapReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_L,1))
_HwDscpToDropPreMapReset_Type.__name__=_B
_HwDscpToDropPreMapReset_Object=MibTableColumn
hwDscpToDropPreMapReset=_HwDscpToDropPreMapReset_Object((1,3,6,1,4,1,2011,2,23,1,16,2,37,1,3),_HwDscpToDropPreMapReset_Type())
hwDscpToDropPreMapReset.setMaxAccess(_E)
if mibBuilder.loadTexts:hwDscpToDropPreMapReset.setStatus(_A)
_HwDscpToCosMapTable_Object=MibTable
hwDscpToCosMapTable=_HwDscpToCosMapTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,38))
if mibBuilder.loadTexts:hwDscpToCosMapTable.setStatus(_A)
_HwDscpToCosMapEntry_Object=MibTableRow
hwDscpToCosMapEntry=_HwDscpToCosMapEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,38,1))
hwDscpToCosMapEntry.setIndexNames((0,_D,_AR))
if mibBuilder.loadTexts:hwDscpToCosMapEntry.setStatus(_A)
class _HwDscpToCosMapDscpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HwDscpToCosMapDscpIndex_Type.__name__=_B
_HwDscpToCosMapDscpIndex_Object=MibTableColumn
hwDscpToCosMapDscpIndex=_HwDscpToCosMapDscpIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,38,1,1),_HwDscpToCosMapDscpIndex_Type())
hwDscpToCosMapDscpIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hwDscpToCosMapDscpIndex.setStatus(_A)
class _HwDscpToCosMapCosValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HwDscpToCosMapCosValue_Type.__name__=_B
_HwDscpToCosMapCosValue_Object=MibTableColumn
hwDscpToCosMapCosValue=_HwDscpToCosMapCosValue_Object((1,3,6,1,4,1,2011,2,23,1,16,2,38,1,2),_HwDscpToCosMapCosValue_Type())
hwDscpToCosMapCosValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hwDscpToCosMapCosValue.setStatus(_A)
class _HwDscpToCosMapReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_L,1))
_HwDscpToCosMapReset_Type.__name__=_B
_HwDscpToCosMapReset_Object=MibTableColumn
hwDscpToCosMapReset=_HwDscpToCosMapReset_Object((1,3,6,1,4,1,2011,2,23,1,16,2,38,1,3),_HwDscpToCosMapReset_Type())
hwDscpToCosMapReset.setMaxAccess(_E)
if mibBuilder.loadTexts:hwDscpToCosMapReset.setStatus(_A)
_HwDscpToDscpMapTable_Object=MibTable
hwDscpToDscpMapTable=_HwDscpToDscpMapTable_Object((1,3,6,1,4,1,2011,2,23,1,16,2,39))
if mibBuilder.loadTexts:hwDscpToDscpMapTable.setStatus(_A)
_HwDscpToDscpMapEntry_Object=MibTableRow
hwDscpToDscpMapEntry=_HwDscpToDscpMapEntry_Object((1,3,6,1,4,1,2011,2,23,1,16,2,39,1))
hwDscpToDscpMapEntry.setIndexNames((0,_D,_AS))
if mibBuilder.loadTexts:hwDscpToDscpMapEntry.setStatus(_A)
class _HwDscpToDscpMapDscpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HwDscpToDscpMapDscpIndex_Type.__name__=_B
_HwDscpToDscpMapDscpIndex_Object=MibTableColumn
hwDscpToDscpMapDscpIndex=_HwDscpToDscpMapDscpIndex_Object((1,3,6,1,4,1,2011,2,23,1,16,2,39,1,1),_HwDscpToDscpMapDscpIndex_Type())
hwDscpToDscpMapDscpIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hwDscpToDscpMapDscpIndex.setStatus(_A)
class _HwDscpToDscpMapDscpValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HwDscpToDscpMapDscpValue_Type.__name__=_B
_HwDscpToDscpMapDscpValue_Object=MibTableColumn
hwDscpToDscpMapDscpValue=_HwDscpToDscpMapDscpValue_Object((1,3,6,1,4,1,2011,2,23,1,16,2,39,1,2),_HwDscpToDscpMapDscpValue_Type())
hwDscpToDscpMapDscpValue.setMaxAccess(_E)
if mibBuilder.loadTexts:hwDscpToDscpMapDscpValue.setStatus(_A)
class _HwDscpToDscpMapReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_L,1))
_HwDscpToDscpMapReset_Type.__name__=_B
_HwDscpToDscpMapReset_Object=MibTableColumn
hwDscpToDscpMapReset=_HwDscpToDscpMapReset_Object((1,3,6,1,4,1,2011,2,23,1,16,2,39,1,3),_HwDscpToDscpMapReset_Type())
hwDscpToDscpMapReset.setMaxAccess(_E)
if mibBuilder.loadTexts:hwDscpToDscpMapReset.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'HwMirrorOrMonitorType':HwMirrorOrMonitorType,'hwLswQosAclMib':hwLswQosAclMib,'hwLswQosMibObject':hwLswQosMibObject,'hwPriorityTrustMode':hwPriorityTrustMode,'hwPortMonitorBothIfIndex':hwPortMonitorBothIfIndex,'hwQueueTable':hwQueueTable,'hwQueueEntry':hwQueueEntry,_P:hwQueueIfIndex,'hwQueueScheduleMode':hwQueueScheduleMode,'hwQueueWeight1':hwQueueWeight1,'hwQueueWeight2':hwQueueWeight2,'hwQueueWeight3':hwQueueWeight3,'hwQueueWeight4':hwQueueWeight4,'hwQueueMaxDelay':hwQueueMaxDelay,'hwQueueWeight5':hwQueueWeight5,'hwQueueWeight6':hwQueueWeight6,'hwQueueWeight7':hwQueueWeight7,'hwQueueWeight8':hwQueueWeight8,'hwRateLimitTable':hwRateLimitTable,'hwRateLimitEntry':hwRateLimitEntry,_Q:hwRateLimitAclIndex,_R:hwRateLimitIfIndex,_S:hwRateLimitVlanID,_T:hwRateLimitDirection,'hwRateLimitUserAclNum':hwRateLimitUserAclNum,'hwRateLimitUserAclRule':hwRateLimitUserAclRule,'hwRateLimitIpAclNum':hwRateLimitIpAclNum,'hwRateLimitIpAclRule':hwRateLimitIpAclRule,'hwRateLimitLinkAclNum':hwRateLimitLinkAclNum,'hwRateLimitLinkAclRule':hwRateLimitLinkAclRule,'hwRateLimitTargetRateMbps':hwRateLimitTargetRateMbps,'hwRateLimitTargetRateKbps':hwRateLimitTargetRateKbps,'hwRateLimitPeakRate':hwRateLimitPeakRate,'hwRateLimitCIR':hwRateLimitCIR,'hwRateLimitCBS':hwRateLimitCBS,'hwRateLimitEBS':hwRateLimitEBS,'hwRateLimitPIR':hwRateLimitPIR,'hwRateLimitConformLocalPre':hwRateLimitConformLocalPre,'hwRateLimitConformActionType':hwRateLimitConformActionType,'hwRateLimitExceedActionType':hwRateLimitExceedActionType,'hwRateLimitExceedDscp':hwRateLimitExceedDscp,'hwRateLimitRuntime':hwRateLimitRuntime,'hwRateLimitRowStatus':hwRateLimitRowStatus,'hwRateLimitExceedCos':hwRateLimitExceedCos,'hwRateLimitConformCos':hwRateLimitConformCos,'hwRateLimitConformDscp':hwRateLimitConformDscp,'hwRateLimitMeterStatByteCount':hwRateLimitMeterStatByteCount,'hwRateLimitMeterStatByteXCount':hwRateLimitMeterStatByteXCount,'hwRateLimitMeterStatState':hwRateLimitMeterStatState,'hwPriorityTable':hwPriorityTable,'hwPriorityEntry':hwPriorityEntry,_U:hwPriorityAclIndex,_V:hwPriorityIfIndex,_W:hwPriorityVlanID,_X:hwPriorityDirection,'hwPriorityUserAclNum':hwPriorityUserAclNum,'hwPriorityUserAclRule':hwPriorityUserAclRule,'hwPriorityIpAclNum':hwPriorityIpAclNum,'hwPriorityIpAclRule':hwPriorityIpAclRule,'hwPriorityLinkAclNum':hwPriorityLinkAclNum,'hwPriorityLinkAclRule':hwPriorityLinkAclRule,'hwPriorityDscp':hwPriorityDscp,'hwPriorityIpPre':hwPriorityIpPre,'hwPriorityIpPreFromCos':hwPriorityIpPreFromCos,'hwPriorityCos':hwPriorityCos,'hwPriorityCosFromIpPre':hwPriorityCosFromIpPre,'hwPriorityLocalPre':hwPriorityLocalPre,'hwPriorityPolicedServiceType':hwPriorityPolicedServiceType,'hwPriorityPolicedServiceDscp':hwPriorityPolicedServiceDscp,'hwPriorityPolicedServiceExp':hwPriorityPolicedServiceExp,'hwPriorityPolicedServiceCos':hwPriorityPolicedServiceCos,'hwPriorityPolicedServiceLoaclPre':hwPriorityPolicedServiceLoaclPre,'hwPriorityPolicedServiceDropPriority':hwPriorityPolicedServiceDropPriority,'hwPriorityRuntime':hwPriorityRuntime,'hwPriorityRowStatus':hwPriorityRowStatus,'hwRedirectTable':hwRedirectTable,'hwRedirectEntry':hwRedirectEntry,_Y:hwRedirectAclIndex,_Z:hwRedirectIfIndex,_a:hwRedirectVlanID,_b:hwRedirectDirection,'hwRedirectUserAclNum':hwRedirectUserAclNum,'hwRedirectUserAclRule':hwRedirectUserAclRule,'hwRedirectIpAclNum':hwRedirectIpAclNum,'hwRedirectIpAclRule':hwRedirectIpAclRule,'hwRedirectLinkAclNum':hwRedirectLinkAclNum,'hwRedirectLinkAclRule':hwRedirectLinkAclRule,'hwRedirectToCpu':hwRedirectToCpu,'hwRedirectToIfIndex':hwRedirectToIfIndex,'hwRedirectToNextHop1':hwRedirectToNextHop1,'hwRedirectToNextHop2':hwRedirectToNextHop2,'hwRedirectRuntime':hwRedirectRuntime,'hwRedirectRowStatus':hwRedirectRowStatus,'hwRedirectToSlotNo':hwRedirectToSlotNo,'hwRedirectRemarkedDSCP':hwRedirectRemarkedDSCP,'hwRedirectRemarkedPri':hwRedirectRemarkedPri,'hwRedirectRemarkedTos':hwRedirectRemarkedTos,'hwRedirectToNextHop3':hwRedirectToNextHop3,'hwRedirectTargetVlanID':hwRedirectTargetVlanID,'hwRedirectMode':hwRedirectMode,'hwRedirectToNestedVlanID':hwRedirectToNestedVlanID,'hwRedirectToModifiedVlanID':hwRedirectToModifiedVlanID,'hwStatisticTable':hwStatisticTable,'hwStatisticEntry':hwStatisticEntry,_c:hwStatisticAclIndex,_d:hwStatisticIfIndex,_e:hwStatisticVlanID,_f:hwStatisticDirection,'hwStatisticUserAclNum':hwStatisticUserAclNum,'hwStatisticUserAclRule':hwStatisticUserAclRule,'hwStatisticIpAclNum':hwStatisticIpAclNum,'hwStatisticIpAclRule':hwStatisticIpAclRule,'hwStatisticLinkAclNum':hwStatisticLinkAclNum,'hwStatisticLinkAclRule':hwStatisticLinkAclRule,'hwStatisticRuntime':hwStatisticRuntime,'hwStatisticPacketCount':hwStatisticPacketCount,'hwStatisticByteCount':hwStatisticByteCount,'hwStatisticCountClear':hwStatisticCountClear,'hwStatisticRowStatus':hwStatisticRowStatus,'hwStatisticPacketXCount':hwStatisticPacketXCount,'hwStatisticByteXCount':hwStatisticByteXCount,'hwMirrorTable':hwMirrorTable,'hwMirrorEntry':hwMirrorEntry,_g:hwMirrorAclIndex,_h:hwMirrorIfIndex,_i:hwMirrorVlanID,_j:hwMirrorDirection,'hwMirrorUserAclNum':hwMirrorUserAclNum,'hwMirrorUserAclRule':hwMirrorUserAclRule,'hwMirrorIpAclNum':hwMirrorIpAclNum,'hwMirrorIpAclRule':hwMirrorIpAclRule,'hwMirrorLinkAclNum':hwMirrorLinkAclNum,'hwMirrorLinkAclRule':hwMirrorLinkAclRule,'hwMirrorToIfIndex':hwMirrorToIfIndex,'hwMirrorToCpu':hwMirrorToCpu,'hwMirrorRuntime':hwMirrorRuntime,'hwMirrorRowStatus':hwMirrorRowStatus,'hwMirrorToGroup':hwMirrorToGroup,'hwPortMirrorTable':hwPortMirrorTable,'hwPortMirrorEntry':hwPortMirrorEntry,_k:hwPortMirrorIfIndex,'hwPortMirrorDirection':hwPortMirrorDirection,'hwPortMirrorRowStatus':hwPortMirrorRowStatus,'hwLineRateTable':hwLineRateTable,'hwLineRateEntry':hwLineRateEntry,_l:hwLineRateIfIndex,_m:hwLineRateDirection,'hwLineRateValue':hwLineRateValue,'hwLineRateRowStatus':hwLineRateRowStatus,'hwBandwidthTable':hwBandwidthTable,'hwBandwidthEntry':hwBandwidthEntry,_n:hwBandwidthAclIndex,_o:hwBandwidthIfIndex,_p:hwBandwidthVlanID,_q:hwBandwidthDirection,'hwBandwidthIpAclNum':hwBandwidthIpAclNum,'hwBandwidthIpAclRule':hwBandwidthIpAclRule,'hwBandwidthLinkAclNum':hwBandwidthLinkAclNum,'hwBandwidthLinkAclRule':hwBandwidthLinkAclRule,'hwBandwidthMinGuaranteedWidth':hwBandwidthMinGuaranteedWidth,'hwBandwidthMaxGuaranteedWidth':hwBandwidthMaxGuaranteedWidth,'hwBandwidthWeight':hwBandwidthWeight,'hwBandwidthRuntime':hwBandwidthRuntime,'hwBandwidthRowStatus':hwBandwidthRowStatus,'hwRedTable':hwRedTable,'hwRedEntry':hwRedEntry,_r:hwRedAclIndex,_s:hwRedIfIndex,_t:hwRedVlanID,_u:hwRedDirection,'hwRedIpAclNum':hwRedIpAclNum,'hwRedIpAclRule':hwRedIpAclRule,'hwRedLinkAclNum':hwRedLinkAclNum,'hwRedLinkAclRule':hwRedLinkAclRule,'hwRedStartQueueLen':hwRedStartQueueLen,'hwRedStopQueueLen':hwRedStopQueueLen,'hwRedProbability':hwRedProbability,'hwRedRuntime':hwRedRuntime,'hwRedRowStatus':hwRedRowStatus,'hwMirrorGroupTable':hwMirrorGroupTable,'hwMirrorGroupEntry':hwMirrorGroupEntry,_v:hwMirrorGroupID,'hwMirrorGroupDirection':hwMirrorGroupDirection,'hwMirrorGroupMirrorIfIndexList':hwMirrorGroupMirrorIfIndexList,'hwMirrorGroupMonitorIfIndex':hwMirrorGroupMonitorIfIndex,'hwMirrorGroupRowStatus':hwMirrorGroupRowStatus,'hwFlowtempTable':hwFlowtempTable,'hwFlowtempEntry':hwFlowtempEntry,_w:hwFlowtempIndex,'hwFlowtempIpProtocol':hwFlowtempIpProtocol,'hwFlowtempTcpFlag':hwFlowtempTcpFlag,'hwFlowtempSPort':hwFlowtempSPort,'hwFlowtempDPort':hwFlowtempDPort,'hwFlowtempIcmpType':hwFlowtempIcmpType,'hwFlowtempIcmpCode':hwFlowtempIcmpCode,'hwFlowtempFragment':hwFlowtempFragment,'hwFlowtempDscp':hwFlowtempDscp,'hwFlowtempIpPre':hwFlowtempIpPre,'hwFlowtempTos':hwFlowtempTos,'hwFlowtempSIp':hwFlowtempSIp,'hwFlowtempSIpMask':hwFlowtempSIpMask,'hwFlowtempDIp':hwFlowtempDIp,'hwFlowtempDIpMask':hwFlowtempDIpMask,'hwFlowtempEthProtocol':hwFlowtempEthProtocol,'hwFlowtempSMac':hwFlowtempSMac,'hwFlowtempSMacMask':hwFlowtempSMacMask,'hwFlowtempDMac':hwFlowtempDMac,'hwFlowtempDMacMask':hwFlowtempDMacMask,'hwFlowtempVpn':hwFlowtempVpn,'hwFlowtempRowStatus':hwFlowtempRowStatus,'hwFlowtempVlanId':hwFlowtempVlanId,'hwFlowtempCos':hwFlowtempCos,'hwFlowtempEnableTable':hwFlowtempEnableTable,'hwFlowtempEnableEntry':hwFlowtempEnableEntry,_y:hwFlowtempEnableIfIndex,_z:hwFlowtempEnableVlanID,'hwFlowtempEnableFlowtempIndex':hwFlowtempEnableFlowtempIndex,'hwTrafficShapeTable':hwTrafficShapeTable,'hwTrafficShapeEntry':hwTrafficShapeEntry,_A0:hwTrafficShapeIfIndex,_A1:hwTrafficShapeQueueId,'hwTrafficShapeMaxRate':hwTrafficShapeMaxRate,'hwTrafficShapeBurstSize':hwTrafficShapeBurstSize,'hwTrafficShapeBufferLimit':hwTrafficShapeBufferLimit,'hwTrafficShapeRowStatus':hwTrafficShapeRowStatus,'hwPortQueueTable':hwPortQueueTable,'hwPortQueueEntry':hwPortQueueEntry,_A2:hwPortQueueIfIndex,_A3:hwPortQueueQueueID,'hwPortQueueWrrPriority':hwPortQueueWrrPriority,'hwPortQueueWeight':hwPortQueueWeight,'hwDropModeTable':hwDropModeTable,'hwDropModeEntry':hwDropModeEntry,_A4:hwDropModeIfIndex,'hwDropModeMode':hwDropModeMode,'hwDropModeWredIndex':hwDropModeWredIndex,'hwWredTable':hwWredTable,'hwWredEntry':hwWredEntry,_A5:hwWredIndex,_A6:hwWredQueueId,'hwWredGreenMinThreshold':hwWredGreenMinThreshold,'hwWredGreenMaxThreshold':hwWredGreenMaxThreshold,'hwWredGreenMaxProb':hwWredGreenMaxProb,'hwWredYellowMinThreshold':hwWredYellowMinThreshold,'hwWredYellowMaxThreshold':hwWredYellowMaxThreshold,'hwWredYellowMaxProb':hwWredYellowMaxProb,'hwWredRedMinThreshold':hwWredRedMinThreshold,'hwWredRedMaxThreshold':hwWredRedMaxThreshold,'hwWredRedMaxProb':hwWredRedMaxProb,'hwWredExponent':hwWredExponent,'hwCosToLocalPrecedenceMapTable':hwCosToLocalPrecedenceMapTable,'hwCosToLocalPrecedenceMapEntry':hwCosToLocalPrecedenceMapEntry,_A7:hwCosToLocalPrecedenceMapCosIndex,'hwCosToLocalPrecedenceMapLocalPrecedenceValue':hwCosToLocalPrecedenceMapLocalPrecedenceValue,'hwCosToDropPrecedenceMapTable':hwCosToDropPrecedenceMapTable,'hwCosToDropPrecedenceMapEntry':hwCosToDropPrecedenceMapEntry,_A8:hwCosToDropPrecedenceMapCosIndex,'hwCosToDropPrecedenceMapDropPrecedenceValue':hwCosToDropPrecedenceMapDropPrecedenceValue,'hwDscpMapTable':hwDscpMapTable,'hwDscpMapEntry':hwDscpMapEntry,_A9:hwDscpMapConformLevel,_AA:hwDscpMapDscpIndex,'hwDscpMapDscpValue':hwDscpMapDscpValue,'hwDscpMapExpValue':hwDscpMapExpValue,'hwDscpMapCosValue':hwDscpMapCosValue,'hwDscpMapLocalPrecedence':hwDscpMapLocalPrecedence,'hwDscpMapDropPrecedence':hwDscpMapDropPrecedence,'hwExpMapTable':hwExpMapTable,'hwExpMapEntry':hwExpMapEntry,_AB:hwExpMapConformLevel,_AC:hwExpMapExpIndex,'hwExpMapDscpValue':hwExpMapDscpValue,'hwExpMapExpValue':hwExpMapExpValue,'hwExpMapCosValue':hwExpMapCosValue,'hwExpMapLocalPrecedence':hwExpMapLocalPrecedence,'hwExpMapDropPrecedence':hwExpMapDropPrecedence,'hwLocalPrecedenceMapTable':hwLocalPrecedenceMapTable,'hwLocalPrecedenceMapEntry':hwLocalPrecedenceMapEntry,_AD:hwLocalPrecedenceMapConformLevel,_AE:hwLocalPrecedenceMapLocalPrecedenceIndex,'hwLocalPrecedenceMapCosValue':hwLocalPrecedenceMapCosValue,'hwPortWredTable':hwPortWredTable,'hwPortWredEntry':hwPortWredEntry,_AF:hwPortWredIfIndex,_AG:hwPortWredQueueID,'hwPortWredQueueStartLength':hwPortWredQueueStartLength,'hwPortWredQueueProbability':hwPortWredQueueProbability,'hwMirroringGroupTable':hwMirroringGroupTable,'hwMirroringGroupEntry':hwMirroringGroupEntry,_J:hwMirroringGroupID,'hwMirroringGroupType':hwMirroringGroupType,'hwMirroringGroupStatus':hwMirroringGroupStatus,'hwMirroringGroupRowStatus':hwMirroringGroupRowStatus,'hwMirroringGroupMirrorTable':hwMirroringGroupMirrorTable,'hwMirroringGroupMirrorEntry':hwMirroringGroupMirrorEntry,'hwMirroringGroupMirrorInboundIfIndexList':hwMirroringGroupMirrorInboundIfIndexList,'hwMirroringGroupMirrorOutboundIfIndexList':hwMirroringGroupMirrorOutboundIfIndexList,'hwMirroringGroupMirrorRowStatus':hwMirroringGroupMirrorRowStatus,'hwMirroringGroupMirrorInTypeList':hwMirroringGroupMirrorInTypeList,'hwMirroringGroupMirrorOutTypeList':hwMirroringGroupMirrorOutTypeList,'hwMirroringGroupMonitorTable':hwMirroringGroupMonitorTable,'hwMirroringGroupMonitorEntry':hwMirroringGroupMonitorEntry,'hwMirroringGroupMonitorIfIndex':hwMirroringGroupMonitorIfIndex,'hwMirroringGroupMonitorRowStatus':hwMirroringGroupMonitorRowStatus,'hwMirroringGroupMonitorType':hwMirroringGroupMonitorType,'hwMirroringGroupReflectorTable':hwMirroringGroupReflectorTable,'hwMirroringGroupReflectorEntry':hwMirroringGroupReflectorEntry,'hwMirroringGroupReflectorIfIndex':hwMirroringGroupReflectorIfIndex,'hwMirroringGroupReflectorRowStatus':hwMirroringGroupReflectorRowStatus,'hwMirroringGroupRprobeVlanTable':hwMirroringGroupRprobeVlanTable,'hwMirroringGroupRprobeVlanEntry':hwMirroringGroupRprobeVlanEntry,'hwMirroringGroupRprobeVlanID':hwMirroringGroupRprobeVlanID,'hwMirroringGroupRprobeVlanRowStatus':hwMirroringGroupRprobeVlanRowStatus,'hwMirroringGroupMirrorMacTable':hwMirroringGroupMirrorMacTable,'hwMirroringGroupMirrorMacEntry':hwMirroringGroupMirrorMacEntry,_AH:hwMirroringGroupMirrorMacSeq,'hwMirroringGroupMirrorMac':hwMirroringGroupMirrorMac,'hwMirrorMacVlanID':hwMirrorMacVlanID,'hwMirroringGroupMirroMacStatus':hwMirroringGroupMirroMacStatus,'hwMirroringGroupMirrorVlanTable':hwMirroringGroupMirrorVlanTable,'hwMirroringGroupMirrorVlanEntry':hwMirroringGroupMirrorVlanEntry,_AI:hwMirroringGroupMirrorVlanSeq,'hwMirroringGroupMirrorVlanID':hwMirroringGroupMirrorVlanID,'hwMirroringGroupMirrorVlanDirection':hwMirroringGroupMirrorVlanDirection,'hwMirroringGroupMirroVlanStatus':hwMirroringGroupMirroVlanStatus,'hwPortTrustTable':hwPortTrustTable,'hwPortTrustEntry':hwPortTrustEntry,_AJ:hwPortTrustIfIndex,'hwPortTrustTrustType':hwPortTrustTrustType,'hwPortTrustOvercastType':hwPortTrustOvercastType,'hwPortTrustReset':hwPortTrustReset,'hwRemarkVlanIDTable':hwRemarkVlanIDTable,'hwRemarkVlanIDEntry':hwRemarkVlanIDEntry,_AK:hwRemarkVlanIDAclIndex,_AL:hwRemarkVlanIDIfIndex,_AM:hwRemarkVlanIDVlanID,_AN:hwRemarkVlanIDDirection,'hwRemarkVlanIDUserAclNum':hwRemarkVlanIDUserAclNum,'hwRemarkVlanIDUserAclRule':hwRemarkVlanIDUserAclRule,'hwRemarkVlanIDIpAclNum':hwRemarkVlanIDIpAclNum,'hwRemarkVlanIDIpAclRule':hwRemarkVlanIDIpAclRule,'hwRemarkVlanIDLinkAclNum':hwRemarkVlanIDLinkAclNum,'hwRemarkVlanIDLinkAclRule':hwRemarkVlanIDLinkAclRule,'hwRemarkVlanIDRemarkVlanID':hwRemarkVlanIDRemarkVlanID,'hwRemarkVlanIDPacketType':hwRemarkVlanIDPacketType,'hwRemarkVlanIDRowStatus':hwRemarkVlanIDRowStatus,'hwCosToDscpMapTable':hwCosToDscpMapTable,'hwCosToDscpMapEntry':hwCosToDscpMapEntry,_AO:hwCosToDscpMapCosIndex,'hwCosToDscpMapDscpValue':hwCosToDscpMapDscpValue,'hwCosToDscpMapReSet':hwCosToDscpMapReSet,'hwDscpToLocalPreMapTable':hwDscpToLocalPreMapTable,'hwDscpToLocalPreMapEntry':hwDscpToLocalPreMapEntry,_AP:hwDscpToLocalPreMapDscpIndex,'hwDscpToLocalPreMapLocalPreVal':hwDscpToLocalPreMapLocalPreVal,'hwDscpToLocalPreMapReset':hwDscpToLocalPreMapReset,'hwDscpToDropPreMapTable':hwDscpToDropPreMapTable,'hwDscpToDropPreMapEntry':hwDscpToDropPreMapEntry,_AQ:hwDscpToDropPreMapDscpIndex,'hwDscpToDropPreMapDropPreVal':hwDscpToDropPreMapDropPreVal,'hwDscpToDropPreMapReset':hwDscpToDropPreMapReset,'hwDscpToCosMapTable':hwDscpToCosMapTable,'hwDscpToCosMapEntry':hwDscpToCosMapEntry,_AR:hwDscpToCosMapDscpIndex,'hwDscpToCosMapCosValue':hwDscpToCosMapCosValue,'hwDscpToCosMapReset':hwDscpToCosMapReset,'hwDscpToDscpMapTable':hwDscpToDscpMapTable,'hwDscpToDscpMapEntry':hwDscpToDscpMapEntry,_AS:hwDscpToDscpMapDscpIndex,'hwDscpToDscpMapDscpValue':hwDscpToDscpMapDscpValue,'hwDscpToDscpMapReset':hwDscpToDscpMapReset})