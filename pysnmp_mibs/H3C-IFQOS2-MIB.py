_AK='h3cIfQoSCoppFlowStatProType'
_AJ='h3cIfQoSCoppFlowStatSlot'
_AI='h3cIfQoSCoppFlowStatChassis'
_AH='h3cQoSRemarkVlanStart'
_AG='h3cQoSRemarkProtocolValue'
_AF='h3cQoSRemarkIPv6AddrValue'
_AE='h3cQoSRemarkIPv4AddrValue'
_AD='h3cQoSRemarkUdpPortStart'
_AC='h3cQoSRemarkTcpPortStart'
_AB='h3cQoSIfTraStaRunDirection'
_AA='h3cQoSIfTraStaRunObjectValue'
_A9='h3cQoSIfTraStaRunObjectType'
_A8='h3cQoSIfTraStaConfigDirection'
_A7='h3cIfQoSPrePriMapTableImportValue'
_A6='h3cIfQoSPrePriMapTableDirection'
_A5='h3cIfQoSPrePriMapTableColor'
_A4='h3cIfQoSPrePriMapTableType'
_A3='h3cIfQoSPriMapGroupImportValue'
_A2='ipPrecedence'
_A1='userdefined'
_A0='h3cIfQoSAggregativeCarApplyRuleValue'
_z='h3cIfQoSAggregativeCarApplyRuleType'
_y='h3cIfQoSAggregativeCarApplyDirection'
_x='h3cIfQoSCarlListNum'
_w='h3cIfQoSCQClassRuleValue'
_v='h3cIfQoSCQClassRuleType'
_u='h3cIfQoSPQType'
_t='less-than'
_s='greater-than'
_r='fragments'
_q='interface'
_p='h3cIfQoSPQClassRuleValue'
_o='h3cIfQoSPQClassRuleType'
_n='h3cIfQoSPQQueueLengthType'
_m='outbound'
_l='inbound'
_k='InetAddressPrefixLength'
_j='h3cIfQoSPriMapGroupIndex'
_i='h3cIfQoSPortWredPreID'
_h='h3cIfQoSWredGroupContentSubIndex'
_g='h3cIfQoSWredGroupContentIndex'
_f='dot1p'
_e='queue'
_d='h3cIfQoSGTSClassRuleValue'
_c='h3cIfQoSGTSClassRuleType'
_b='h3cIfQoSTricolorCarValue'
_a='h3cIfQoSTricolorCarType'
_Z='h3cIfQoSTricolorCarDirection'
_Y='any'
_X='h3cIfQoSAggregativeCarIndex'
_W='unitPercent'
_V='unitAbsolute'
_U='h3cIfQoSLRDirection'
_T='h3cIfQoSCQQueueID'
_S='h3cIfQoSWredGroupIndex'
_R='h3cIfQoSCQListNumber'
_Q='h3cIfQoSPQListNumber'
_P='h3cIfQoSQueueID'
_O='H3cIfCarAction'
_N='dscp'
_M='ipv6acl'
_L='ipv4acl'
_K='OctetString'
_J='read-write'
_I='Unsigned32'
_H='ifIndex'
_G='IF-MIB'
_F='not-accessible'
_E='H3C-IFQOS2-MIB'
_D='Integer32'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_G,_H)
InetAddressIPv6,InetAddressPrefixLength=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv6',_k)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
h3cIfQos2=ModuleIdentity((1,3,6,1,4,1,2011,10,2,65,1))
if mibBuilder.loadTexts:h3cIfQos2.setRevisions(('2018-02-28 00:00','2017-05-20 00:00','2016-10-25 00:00','2014-11-25 00:00','2013-11-28 00:00'))
class H3cIfCarAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*(('invalid',0),('pass',1),('continue',2),('discard',3),('remark',4),('remark-ip-continue',5),('remark-ip-pass',6),('remark-mplsexp-continue',7),('remark-mplsexp-pass',8),('remark-dscp-continue',9),('remark-dscp-pass',10),('remark-dot1p-continue',11),('remark-dot1p-pass',12),('remark-atm-clp-continue',13),('remark-atm-clp-pass',14),('remark-fr-de-continue',15),('remark-fr-de-pass',16),('remarkLocalPreContinue',17),('remarkLocalPrePass',18),('remarkDropPreContinue',19),('remarkDropPrePass',20)))
class PriorityQueue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('top',1),('middle',2),('normal',3),('bottom',4)))
class Direction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_l,1),(_m,2)))
_H3cQos2_ObjectIdentity=ObjectIdentity
h3cQos2=_H3cQos2_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65))
_H3cIfQoSHardwareQueueObjects_ObjectIdentity=ObjectIdentity
h3cIfQoSHardwareQueueObjects=_H3cIfQoSHardwareQueueObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,1))
_H3cIfQoSHardwareQueueConfigGroup_ObjectIdentity=ObjectIdentity
h3cIfQoSHardwareQueueConfigGroup=_H3cIfQoSHardwareQueueConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,1,1))
_H3cIfQoSQSModeTable_Object=MibTable
h3cIfQoSQSModeTable=_H3cIfQoSQSModeTable_Object((1,3,6,1,4,1,2011,10,2,65,1,1,1,1))
if mibBuilder.loadTexts:h3cIfQoSQSModeTable.setStatus(_A)
_H3cIfQoSQSModeEntry_Object=MibTableRow
h3cIfQoSQSModeEntry=_H3cIfQoSQSModeEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,1,1,1,1))
h3cIfQoSQSModeEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:h3cIfQoSQSModeEntry.setStatus(_A)
class _H3cIfQoSQSMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('sp',1),('sp0',2),('sp1',3),('sp2',4),('wrr',5),('hwfq',6),('wrr-sp',7),('byteCountWrr',8),('byteCountWfq',9),('gmb',10)))
_H3cIfQoSQSMode_Type.__name__=_D
_H3cIfQoSQSMode_Object=MibTableColumn
h3cIfQoSQSMode=_H3cIfQoSQSMode_Object((1,3,6,1,4,1,2011,10,2,65,1,1,1,1,1,1),_H3cIfQoSQSMode_Type())
h3cIfQoSQSMode.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cIfQoSQSMode.setStatus(_A)
_H3cIfQoSQSWeightTable_Object=MibTable
h3cIfQoSQSWeightTable=_H3cIfQoSQSWeightTable_Object((1,3,6,1,4,1,2011,10,2,65,1,1,1,2))
if mibBuilder.loadTexts:h3cIfQoSQSWeightTable.setStatus(_A)
_H3cIfQoSQSWeightEntry_Object=MibTableRow
h3cIfQoSQSWeightEntry=_H3cIfQoSQSWeightEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,1,1,2,1))
h3cIfQoSQSWeightEntry.setIndexNames((0,_G,_H),(0,_E,_P))
if mibBuilder.loadTexts:h3cIfQoSQSWeightEntry.setStatus(_A)
_H3cIfQoSQueueID_Type=Integer32
_H3cIfQoSQueueID_Object=MibTableColumn
h3cIfQoSQueueID=_H3cIfQoSQueueID_Object((1,3,6,1,4,1,2011,10,2,65,1,1,1,2,1,1),_H3cIfQoSQueueID_Type())
h3cIfQoSQueueID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSQueueID.setStatus(_A)
class _H3cIfQoSQueueGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('group0',1),('group1',2),('group2',3),('group3',4),('group4',5)))
_H3cIfQoSQueueGroupType_Type.__name__=_D
_H3cIfQoSQueueGroupType_Object=MibTableColumn
h3cIfQoSQueueGroupType=_H3cIfQoSQueueGroupType_Object((1,3,6,1,4,1,2011,10,2,65,1,1,1,2,1,2),_H3cIfQoSQueueGroupType_Type())
h3cIfQoSQueueGroupType.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cIfQoSQueueGroupType.setStatus(_A)
class _H3cIfQoSQSType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('weight',1),('byte-count',2)))
_H3cIfQoSQSType_Type.__name__=_D
_H3cIfQoSQSType_Object=MibTableColumn
h3cIfQoSQSType=_H3cIfQoSQSType_Object((1,3,6,1,4,1,2011,10,2,65,1,1,1,2,1,3),_H3cIfQoSQSType_Type())
h3cIfQoSQSType.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cIfQoSQSType.setStatus(_A)
_H3cIfQoSQSValue_Type=Integer32
_H3cIfQoSQSValue_Object=MibTableColumn
h3cIfQoSQSValue=_H3cIfQoSQSValue_Object((1,3,6,1,4,1,2011,10,2,65,1,1,1,2,1,4),_H3cIfQoSQSValue_Type())
h3cIfQoSQSValue.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cIfQoSQSValue.setStatus(_A)
class _H3cIfQoSQSMaxDelay_Type(Integer32):defaultValue=9
_H3cIfQoSQSMaxDelay_Type.__name__=_D
_H3cIfQoSQSMaxDelay_Object=MibTableColumn
h3cIfQoSQSMaxDelay=_H3cIfQoSQSMaxDelay_Object((1,3,6,1,4,1,2011,10,2,65,1,1,1,2,1,5),_H3cIfQoSQSMaxDelay_Type())
h3cIfQoSQSMaxDelay.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cIfQoSQSMaxDelay.setStatus(_A)
_H3cIfQoSQSMinBandwidth_Type=Integer32
_H3cIfQoSQSMinBandwidth_Object=MibTableColumn
h3cIfQoSQSMinBandwidth=_H3cIfQoSQSMinBandwidth_Object((1,3,6,1,4,1,2011,10,2,65,1,1,1,2,1,6),_H3cIfQoSQSMinBandwidth_Type())
h3cIfQoSQSMinBandwidth.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cIfQoSQSMinBandwidth.setStatus(_A)
class _H3cIfQoSQSMinBandwidthPercent_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100),ValueRangeConstraint(255,255))
_H3cIfQoSQSMinBandwidthPercent_Type.__name__=_I
_H3cIfQoSQSMinBandwidthPercent_Object=MibTableColumn
h3cIfQoSQSMinBandwidthPercent=_H3cIfQoSQSMinBandwidthPercent_Object((1,3,6,1,4,1,2011,10,2,65,1,1,1,2,1,7),_H3cIfQoSQSMinBandwidthPercent_Type())
h3cIfQoSQSMinBandwidthPercent.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cIfQoSQSMinBandwidthPercent.setStatus(_A)
_H3cIfQoSHardwareQueueRunInfoGroup_ObjectIdentity=ObjectIdentity
h3cIfQoSHardwareQueueRunInfoGroup=_H3cIfQoSHardwareQueueRunInfoGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,1,2))
_H3cIfQoSHardwareQueueRunInfoTable_Object=MibTable
h3cIfQoSHardwareQueueRunInfoTable=_H3cIfQoSHardwareQueueRunInfoTable_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,1))
if mibBuilder.loadTexts:h3cIfQoSHardwareQueueRunInfoTable.setStatus(_A)
_H3cIfQoSHardwareQueueRunInfoEntry_Object=MibTableRow
h3cIfQoSHardwareQueueRunInfoEntry=_H3cIfQoSHardwareQueueRunInfoEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,1,1))
h3cIfQoSHardwareQueueRunInfoEntry.setIndexNames((0,_G,_H),(0,_E,_P))
if mibBuilder.loadTexts:h3cIfQoSHardwareQueueRunInfoEntry.setStatus(_A)
_H3cIfQoSPassPackets_Type=Counter64
_H3cIfQoSPassPackets_Object=MibTableColumn
h3cIfQoSPassPackets=_H3cIfQoSPassPackets_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,1,1,1),_H3cIfQoSPassPackets_Type())
h3cIfQoSPassPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSPassPackets.setStatus(_A)
_H3cIfQoSDropPackets_Type=Counter64
_H3cIfQoSDropPackets_Object=MibTableColumn
h3cIfQoSDropPackets=_H3cIfQoSDropPackets_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,1,1,2),_H3cIfQoSDropPackets_Type())
h3cIfQoSDropPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSDropPackets.setStatus(_A)
_H3cIfQoSPassBytes_Type=Counter64
_H3cIfQoSPassBytes_Object=MibTableColumn
h3cIfQoSPassBytes=_H3cIfQoSPassBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,1,1,3),_H3cIfQoSPassBytes_Type())
h3cIfQoSPassBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSPassBytes.setStatus(_A)
_H3cIfQoSPassPPS_Type=Unsigned32
_H3cIfQoSPassPPS_Object=MibTableColumn
h3cIfQoSPassPPS=_H3cIfQoSPassPPS_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,1,1,4),_H3cIfQoSPassPPS_Type())
h3cIfQoSPassPPS.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSPassPPS.setStatus(_A)
_H3cIfQoSPassBPS_Type=Unsigned32
_H3cIfQoSPassBPS_Object=MibTableColumn
h3cIfQoSPassBPS=_H3cIfQoSPassBPS_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,1,1,5),_H3cIfQoSPassBPS_Type())
h3cIfQoSPassBPS.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSPassBPS.setStatus(_A)
_H3cIfQoSDropBytes_Type=Counter64
_H3cIfQoSDropBytes_Object=MibTableColumn
h3cIfQoSDropBytes=_H3cIfQoSDropBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,1,1,6),_H3cIfQoSDropBytes_Type())
h3cIfQoSDropBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSDropBytes.setStatus(_A)
_H3cIfQoSQueueLengthInPkts_Type=Unsigned32
_H3cIfQoSQueueLengthInPkts_Object=MibTableColumn
h3cIfQoSQueueLengthInPkts=_H3cIfQoSQueueLengthInPkts_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,1,1,7),_H3cIfQoSQueueLengthInPkts_Type())
h3cIfQoSQueueLengthInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSQueueLengthInPkts.setStatus(_A)
_H3cIfQoSQueueLengthInBytes_Type=Unsigned32
_H3cIfQoSQueueLengthInBytes_Object=MibTableColumn
h3cIfQoSQueueLengthInBytes=_H3cIfQoSQueueLengthInBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,1,1,8),_H3cIfQoSQueueLengthInBytes_Type())
h3cIfQoSQueueLengthInBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSQueueLengthInBytes.setStatus(_A)
_H3cIfQoSCurQueuePkts_Type=Unsigned32
_H3cIfQoSCurQueuePkts_Object=MibTableColumn
h3cIfQoSCurQueuePkts=_H3cIfQoSCurQueuePkts_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,1,1,9),_H3cIfQoSCurQueuePkts_Type())
h3cIfQoSCurQueuePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSCurQueuePkts.setStatus(_A)
_H3cIfQoSCurQueueBytes_Type=Unsigned32
_H3cIfQoSCurQueueBytes_Object=MibTableColumn
h3cIfQoSCurQueueBytes=_H3cIfQoSCurQueueBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,1,1,10),_H3cIfQoSCurQueueBytes_Type())
h3cIfQoSCurQueueBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSCurQueueBytes.setStatus(_A)
_H3cIfQoSCurQueuePPS_Type=Unsigned32
_H3cIfQoSCurQueuePPS_Object=MibTableColumn
h3cIfQoSCurQueuePPS=_H3cIfQoSCurQueuePPS_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,1,1,11),_H3cIfQoSCurQueuePPS_Type())
h3cIfQoSCurQueuePPS.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSCurQueuePPS.setStatus(_A)
_H3cIfQoSCurQueueBPS_Type=Unsigned32
_H3cIfQoSCurQueueBPS_Object=MibTableColumn
h3cIfQoSCurQueueBPS=_H3cIfQoSCurQueueBPS_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,1,1,12),_H3cIfQoSCurQueueBPS_Type())
h3cIfQoSCurQueueBPS.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSCurQueueBPS.setStatus(_A)
_H3cIfQoSTailDropPkts_Type=Counter64
_H3cIfQoSTailDropPkts_Object=MibTableColumn
h3cIfQoSTailDropPkts=_H3cIfQoSTailDropPkts_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,1,1,13),_H3cIfQoSTailDropPkts_Type())
h3cIfQoSTailDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSTailDropPkts.setStatus(_A)
_H3cIfQoSTailDropBytes_Type=Counter64
_H3cIfQoSTailDropBytes_Object=MibTableColumn
h3cIfQoSTailDropBytes=_H3cIfQoSTailDropBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,1,1,14),_H3cIfQoSTailDropBytes_Type())
h3cIfQoSTailDropBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSTailDropBytes.setStatus(_A)
_H3cIfQoSTailDropPPS_Type=Unsigned32
_H3cIfQoSTailDropPPS_Object=MibTableColumn
h3cIfQoSTailDropPPS=_H3cIfQoSTailDropPPS_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,1,1,15),_H3cIfQoSTailDropPPS_Type())
h3cIfQoSTailDropPPS.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSTailDropPPS.setStatus(_A)
_H3cIfQoSTailDropBPS_Type=Unsigned32
_H3cIfQoSTailDropBPS_Object=MibTableColumn
h3cIfQoSTailDropBPS=_H3cIfQoSTailDropBPS_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,1,1,16),_H3cIfQoSTailDropBPS_Type())
h3cIfQoSTailDropBPS.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSTailDropBPS.setStatus(_A)
_H3cIfQoSWredDropPkts_Type=Counter64
_H3cIfQoSWredDropPkts_Object=MibTableColumn
h3cIfQoSWredDropPkts=_H3cIfQoSWredDropPkts_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,1,1,17),_H3cIfQoSWredDropPkts_Type())
h3cIfQoSWredDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWredDropPkts.setStatus(_A)
_H3cIfQoSWredDropBytes_Type=Counter64
_H3cIfQoSWredDropBytes_Object=MibTableColumn
h3cIfQoSWredDropBytes=_H3cIfQoSWredDropBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,1,1,18),_H3cIfQoSWredDropBytes_Type())
h3cIfQoSWredDropBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWredDropBytes.setStatus(_A)
_H3cIfQoSWredDropPPS_Type=Unsigned32
_H3cIfQoSWredDropPPS_Object=MibTableColumn
h3cIfQoSWredDropPPS=_H3cIfQoSWredDropPPS_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,1,1,19),_H3cIfQoSWredDropPPS_Type())
h3cIfQoSWredDropPPS.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWredDropPPS.setStatus(_A)
_H3cIfQoSWredDropBPS_Type=Unsigned32
_H3cIfQoSWredDropBPS_Object=MibTableColumn
h3cIfQoSWredDropBPS=_H3cIfQoSWredDropBPS_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,1,1,20),_H3cIfQoSWredDropBPS_Type())
h3cIfQoSWredDropBPS.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWredDropBPS.setStatus(_A)
class _H3cIfQoSQueueName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,3))
_H3cIfQoSQueueName_Type.__name__=_K
_H3cIfQoSQueueName_Object=MibTableColumn
h3cIfQoSQueueName=_H3cIfQoSQueueName_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,1,1,21),_H3cIfQoSQueueName_Type())
h3cIfQoSQueueName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSQueueName.setStatus(_A)
_H3cIfQoSHQueueTcpRunInfoTable_Object=MibTable
h3cIfQoSHQueueTcpRunInfoTable=_H3cIfQoSHQueueTcpRunInfoTable_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,2))
if mibBuilder.loadTexts:h3cIfQoSHQueueTcpRunInfoTable.setStatus(_A)
_H3cIfQoSHQueueTcpRunInfoEntry_Object=MibTableRow
h3cIfQoSHQueueTcpRunInfoEntry=_H3cIfQoSHQueueTcpRunInfoEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,2,1))
h3cIfQoSHQueueTcpRunInfoEntry.setIndexNames((0,_G,_H),(0,_E,_P))
if mibBuilder.loadTexts:h3cIfQoSHQueueTcpRunInfoEntry.setStatus(_A)
_H3cIfQoSWredDropLPreNTcpPkts_Type=Counter64
_H3cIfQoSWredDropLPreNTcpPkts_Object=MibTableColumn
h3cIfQoSWredDropLPreNTcpPkts=_H3cIfQoSWredDropLPreNTcpPkts_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,2,1,1),_H3cIfQoSWredDropLPreNTcpPkts_Type())
h3cIfQoSWredDropLPreNTcpPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWredDropLPreNTcpPkts.setStatus(_A)
_H3cIfQoSWredDropLPreNTcpBytes_Type=Counter64
_H3cIfQoSWredDropLPreNTcpBytes_Object=MibTableColumn
h3cIfQoSWredDropLPreNTcpBytes=_H3cIfQoSWredDropLPreNTcpBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,2,1,2),_H3cIfQoSWredDropLPreNTcpBytes_Type())
h3cIfQoSWredDropLPreNTcpBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWredDropLPreNTcpBytes.setStatus(_A)
_H3cIfQoSWredDropLPreNTcpPPS_Type=Unsigned32
_H3cIfQoSWredDropLPreNTcpPPS_Object=MibTableColumn
h3cIfQoSWredDropLPreNTcpPPS=_H3cIfQoSWredDropLPreNTcpPPS_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,2,1,3),_H3cIfQoSWredDropLPreNTcpPPS_Type())
h3cIfQoSWredDropLPreNTcpPPS.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWredDropLPreNTcpPPS.setStatus(_A)
_H3cIfQoSWredDropLPreNTcpBPS_Type=Unsigned32
_H3cIfQoSWredDropLPreNTcpBPS_Object=MibTableColumn
h3cIfQoSWredDropLPreNTcpBPS=_H3cIfQoSWredDropLPreNTcpBPS_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,2,1,4),_H3cIfQoSWredDropLPreNTcpBPS_Type())
h3cIfQoSWredDropLPreNTcpBPS.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWredDropLPreNTcpBPS.setStatus(_A)
_H3cIfQoSWredDropLPreTcpPkts_Type=Counter64
_H3cIfQoSWredDropLPreTcpPkts_Object=MibTableColumn
h3cIfQoSWredDropLPreTcpPkts=_H3cIfQoSWredDropLPreTcpPkts_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,2,1,5),_H3cIfQoSWredDropLPreTcpPkts_Type())
h3cIfQoSWredDropLPreTcpPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWredDropLPreTcpPkts.setStatus(_A)
_H3cIfQoSWredDropLPreTcpBytes_Type=Counter64
_H3cIfQoSWredDropLPreTcpBytes_Object=MibTableColumn
h3cIfQoSWredDropLPreTcpBytes=_H3cIfQoSWredDropLPreTcpBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,2,1,6),_H3cIfQoSWredDropLPreTcpBytes_Type())
h3cIfQoSWredDropLPreTcpBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWredDropLPreTcpBytes.setStatus(_A)
_H3cIfQoSWredDropLPreTcpPPS_Type=Unsigned32
_H3cIfQoSWredDropLPreTcpPPS_Object=MibTableColumn
h3cIfQoSWredDropLPreTcpPPS=_H3cIfQoSWredDropLPreTcpPPS_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,2,1,7),_H3cIfQoSWredDropLPreTcpPPS_Type())
h3cIfQoSWredDropLPreTcpPPS.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWredDropLPreTcpPPS.setStatus(_A)
_H3cIfQoSWredDropLPreTcpBPS_Type=Unsigned32
_H3cIfQoSWredDropLPreTcpBPS_Object=MibTableColumn
h3cIfQoSWredDropLPreTcpBPS=_H3cIfQoSWredDropLPreTcpBPS_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,2,1,8),_H3cIfQoSWredDropLPreTcpBPS_Type())
h3cIfQoSWredDropLPreTcpBPS.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWredDropLPreTcpBPS.setStatus(_A)
_H3cIfQoSWredDropHPreNTcpPkts_Type=Counter64
_H3cIfQoSWredDropHPreNTcpPkts_Object=MibTableColumn
h3cIfQoSWredDropHPreNTcpPkts=_H3cIfQoSWredDropHPreNTcpPkts_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,2,1,9),_H3cIfQoSWredDropHPreNTcpPkts_Type())
h3cIfQoSWredDropHPreNTcpPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWredDropHPreNTcpPkts.setStatus(_A)
_H3cIfQoSWredDropHPreNTcpBytes_Type=Counter64
_H3cIfQoSWredDropHPreNTcpBytes_Object=MibTableColumn
h3cIfQoSWredDropHPreNTcpBytes=_H3cIfQoSWredDropHPreNTcpBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,2,1,10),_H3cIfQoSWredDropHPreNTcpBytes_Type())
h3cIfQoSWredDropHPreNTcpBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWredDropHPreNTcpBytes.setStatus(_A)
_H3cIfQoSWredDropHPreNTcpPPS_Type=Unsigned32
_H3cIfQoSWredDropHPreNTcpPPS_Object=MibTableColumn
h3cIfQoSWredDropHPreNTcpPPS=_H3cIfQoSWredDropHPreNTcpPPS_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,2,1,11),_H3cIfQoSWredDropHPreNTcpPPS_Type())
h3cIfQoSWredDropHPreNTcpPPS.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWredDropHPreNTcpPPS.setStatus(_A)
_H3cIfQoSWredDropHPreNTcpBPS_Type=Unsigned32
_H3cIfQoSWredDropHPreNTcpBPS_Object=MibTableColumn
h3cIfQoSWredDropHPreNTcpBPS=_H3cIfQoSWredDropHPreNTcpBPS_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,2,1,12),_H3cIfQoSWredDropHPreNTcpBPS_Type())
h3cIfQoSWredDropHPreNTcpBPS.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWredDropHPreNTcpBPS.setStatus(_A)
_H3cIfQoSWredDropHPreTcpPkts_Type=Counter64
_H3cIfQoSWredDropHPreTcpPkts_Object=MibTableColumn
h3cIfQoSWredDropHPreTcpPkts=_H3cIfQoSWredDropHPreTcpPkts_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,2,1,13),_H3cIfQoSWredDropHPreTcpPkts_Type())
h3cIfQoSWredDropHPreTcpPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWredDropHPreTcpPkts.setStatus(_A)
_H3cIfQoSWredDropHPreTcpBytes_Type=Counter64
_H3cIfQoSWredDropHPreTcpBytes_Object=MibTableColumn
h3cIfQoSWredDropHPreTcpBytes=_H3cIfQoSWredDropHPreTcpBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,2,1,14),_H3cIfQoSWredDropHPreTcpBytes_Type())
h3cIfQoSWredDropHPreTcpBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWredDropHPreTcpBytes.setStatus(_A)
_H3cIfQoSWredDropHPreTcpPPS_Type=Unsigned32
_H3cIfQoSWredDropHPreTcpPPS_Object=MibTableColumn
h3cIfQoSWredDropHPreTcpPPS=_H3cIfQoSWredDropHPreTcpPPS_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,2,1,15),_H3cIfQoSWredDropHPreTcpPPS_Type())
h3cIfQoSWredDropHPreTcpPPS.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWredDropHPreTcpPPS.setStatus(_A)
_H3cIfQoSWredDropHPreTcpBPS_Type=Unsigned32
_H3cIfQoSWredDropHPreTcpBPS_Object=MibTableColumn
h3cIfQoSWredDropHPreTcpBPS=_H3cIfQoSWredDropHPreTcpBPS_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,2,1,16),_H3cIfQoSWredDropHPreTcpBPS_Type())
h3cIfQoSWredDropHPreTcpBPS.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWredDropHPreTcpBPS.setStatus(_A)
_H3cIfQoSHardwareQueueTotalRunInfoTable_Object=MibTable
h3cIfQoSHardwareQueueTotalRunInfoTable=_H3cIfQoSHardwareQueueTotalRunInfoTable_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,3))
if mibBuilder.loadTexts:h3cIfQoSHardwareQueueTotalRunInfoTable.setStatus(_A)
_H3cIfQoSHardwareQueueTotalRunInfoEntry_Object=MibTableRow
h3cIfQoSHardwareQueueTotalRunInfoEntry=_H3cIfQoSHardwareQueueTotalRunInfoEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,3,1))
h3cIfQoSHardwareQueueTotalRunInfoEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:h3cIfQoSHardwareQueueTotalRunInfoEntry.setStatus(_A)
_H3cIfQoSQueueLength_Type=Unsigned32
_H3cIfQoSQueueLength_Object=MibTableColumn
h3cIfQoSQueueLength=_H3cIfQoSQueueLength_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,3,1,1),_H3cIfQoSQueueLength_Type())
h3cIfQoSQueueLength.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSQueueLength.setStatus(_A)
_H3cIfQoSPeakQueueBytes_Type=Unsigned32
_H3cIfQoSPeakQueueBytes_Object=MibTableColumn
h3cIfQoSPeakQueueBytes=_H3cIfQoSPeakQueueBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,1,2,3,1,2),_H3cIfQoSPeakQueueBytes_Type())
h3cIfQoSPeakQueueBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSPeakQueueBytes.setStatus(_A)
_H3cIfQoSSoftwareQueueObjects_ObjectIdentity=ObjectIdentity
h3cIfQoSSoftwareQueueObjects=_H3cIfQoSSoftwareQueueObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,2))
_H3cIfQoSFIFOObject_ObjectIdentity=ObjectIdentity
h3cIfQoSFIFOObject=_H3cIfQoSFIFOObject_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,2,1))
_H3cIfQoSFIFOConfigTable_Object=MibTable
h3cIfQoSFIFOConfigTable=_H3cIfQoSFIFOConfigTable_Object((1,3,6,1,4,1,2011,10,2,65,1,2,1,1))
if mibBuilder.loadTexts:h3cIfQoSFIFOConfigTable.setStatus(_A)
_H3cIfQoSFIFOConfigEntry_Object=MibTableRow
h3cIfQoSFIFOConfigEntry=_H3cIfQoSFIFOConfigEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,2,1,1,1))
h3cIfQoSFIFOConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:h3cIfQoSFIFOConfigEntry.setStatus(_A)
_H3cIfQoSFIFOMaxQueueLen_Type=Integer32
_H3cIfQoSFIFOMaxQueueLen_Object=MibTableColumn
h3cIfQoSFIFOMaxQueueLen=_H3cIfQoSFIFOMaxQueueLen_Object((1,3,6,1,4,1,2011,10,2,65,1,2,1,1,1,1),_H3cIfQoSFIFOMaxQueueLen_Type())
h3cIfQoSFIFOMaxQueueLen.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cIfQoSFIFOMaxQueueLen.setStatus(_A)
_H3cIfQoSFIFORunInfoTable_Object=MibTable
h3cIfQoSFIFORunInfoTable=_H3cIfQoSFIFORunInfoTable_Object((1,3,6,1,4,1,2011,10,2,65,1,2,1,2))
if mibBuilder.loadTexts:h3cIfQoSFIFORunInfoTable.setStatus(_A)
_H3cIfQoSFIFORunInfoEntry_Object=MibTableRow
h3cIfQoSFIFORunInfoEntry=_H3cIfQoSFIFORunInfoEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,2,1,2,1))
h3cIfQoSFIFORunInfoEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:h3cIfQoSFIFORunInfoEntry.setStatus(_A)
_H3cIfQoSFIFOSize_Type=Integer32
_H3cIfQoSFIFOSize_Object=MibTableColumn
h3cIfQoSFIFOSize=_H3cIfQoSFIFOSize_Object((1,3,6,1,4,1,2011,10,2,65,1,2,1,2,1,1),_H3cIfQoSFIFOSize_Type())
h3cIfQoSFIFOSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSFIFOSize.setStatus(_A)
_H3cIfQoSFIFODiscardPackets_Type=Counter64
_H3cIfQoSFIFODiscardPackets_Object=MibTableColumn
h3cIfQoSFIFODiscardPackets=_H3cIfQoSFIFODiscardPackets_Object((1,3,6,1,4,1,2011,10,2,65,1,2,1,2,1,2),_H3cIfQoSFIFODiscardPackets_Type())
h3cIfQoSFIFODiscardPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSFIFODiscardPackets.setStatus(_A)
_H3cIfQoSPQObject_ObjectIdentity=ObjectIdentity
h3cIfQoSPQObject=_H3cIfQoSPQObject_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,2,2))
_H3cIfQoSPQConfigGroup_ObjectIdentity=ObjectIdentity
h3cIfQoSPQConfigGroup=_H3cIfQoSPQConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,2,2,1))
_H3cIfQoSPQDefaultTable_Object=MibTable
h3cIfQoSPQDefaultTable=_H3cIfQoSPQDefaultTable_Object((1,3,6,1,4,1,2011,10,2,65,1,2,2,1,1))
if mibBuilder.loadTexts:h3cIfQoSPQDefaultTable.setStatus(_A)
_H3cIfQoSPQDefaultEntry_Object=MibTableRow
h3cIfQoSPQDefaultEntry=_H3cIfQoSPQDefaultEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,2,2,1,1,1))
h3cIfQoSPQDefaultEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:h3cIfQoSPQDefaultEntry.setStatus(_A)
class _H3cIfQoSPQListNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_H3cIfQoSPQListNumber_Type.__name__=_D
_H3cIfQoSPQListNumber_Object=MibTableColumn
h3cIfQoSPQListNumber=_H3cIfQoSPQListNumber_Object((1,3,6,1,4,1,2011,10,2,65,1,2,2,1,1,1,1),_H3cIfQoSPQListNumber_Type())
h3cIfQoSPQListNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSPQListNumber.setStatus(_A)
_H3cIfQoSPQDefaultQueueType_Type=PriorityQueue
_H3cIfQoSPQDefaultQueueType_Object=MibTableColumn
h3cIfQoSPQDefaultQueueType=_H3cIfQoSPQDefaultQueueType_Object((1,3,6,1,4,1,2011,10,2,65,1,2,2,1,1,1,2),_H3cIfQoSPQDefaultQueueType_Type())
h3cIfQoSPQDefaultQueueType.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cIfQoSPQDefaultQueueType.setStatus(_A)
_H3cIfQoSPQQueueLengthTable_Object=MibTable
h3cIfQoSPQQueueLengthTable=_H3cIfQoSPQQueueLengthTable_Object((1,3,6,1,4,1,2011,10,2,65,1,2,2,1,2))
if mibBuilder.loadTexts:h3cIfQoSPQQueueLengthTable.setStatus(_A)
_H3cIfQoSPQQueueLengthEntry_Object=MibTableRow
h3cIfQoSPQQueueLengthEntry=_H3cIfQoSPQQueueLengthEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,2,2,1,2,1))
h3cIfQoSPQQueueLengthEntry.setIndexNames((0,_E,_Q),(0,_E,_n))
if mibBuilder.loadTexts:h3cIfQoSPQQueueLengthEntry.setStatus(_A)
_H3cIfQoSPQQueueLengthType_Type=PriorityQueue
_H3cIfQoSPQQueueLengthType_Object=MibTableColumn
h3cIfQoSPQQueueLengthType=_H3cIfQoSPQQueueLengthType_Object((1,3,6,1,4,1,2011,10,2,65,1,2,2,1,2,1,1),_H3cIfQoSPQQueueLengthType_Type())
h3cIfQoSPQQueueLengthType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSPQQueueLengthType.setStatus(_A)
class _H3cIfQoSPQQueueLengthValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_H3cIfQoSPQQueueLengthValue_Type.__name__=_D
_H3cIfQoSPQQueueLengthValue_Object=MibTableColumn
h3cIfQoSPQQueueLengthValue=_H3cIfQoSPQQueueLengthValue_Object((1,3,6,1,4,1,2011,10,2,65,1,2,2,1,2,1,2),_H3cIfQoSPQQueueLengthValue_Type())
h3cIfQoSPQQueueLengthValue.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cIfQoSPQQueueLengthValue.setStatus(_A)
_H3cIfQoSPQClassRuleTable_Object=MibTable
h3cIfQoSPQClassRuleTable=_H3cIfQoSPQClassRuleTable_Object((1,3,6,1,4,1,2011,10,2,65,1,2,2,1,3))
if mibBuilder.loadTexts:h3cIfQoSPQClassRuleTable.setStatus(_A)
_H3cIfQoSPQClassRuleEntry_Object=MibTableRow
h3cIfQoSPQClassRuleEntry=_H3cIfQoSPQClassRuleEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,2,2,1,3,1))
h3cIfQoSPQClassRuleEntry.setIndexNames((0,_E,_Q),(0,_E,_o),(0,_E,_p))
if mibBuilder.loadTexts:h3cIfQoSPQClassRuleEntry.setStatus(_A)
class _H3cIfQoSPQClassRuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_q,1),(_L,2),(_M,3),(_r,4),(_s,5),(_t,6),('tcp',7),('udp',8),('ipall',9),('mpls',10)))
_H3cIfQoSPQClassRuleType_Type.__name__=_D
_H3cIfQoSPQClassRuleType_Object=MibTableColumn
h3cIfQoSPQClassRuleType=_H3cIfQoSPQClassRuleType_Object((1,3,6,1,4,1,2011,10,2,65,1,2,2,1,3,1,1),_H3cIfQoSPQClassRuleType_Type())
h3cIfQoSPQClassRuleType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSPQClassRuleType.setStatus(_A)
_H3cIfQoSPQClassRuleValue_Type=Integer32
_H3cIfQoSPQClassRuleValue_Object=MibTableColumn
h3cIfQoSPQClassRuleValue=_H3cIfQoSPQClassRuleValue_Object((1,3,6,1,4,1,2011,10,2,65,1,2,2,1,3,1,2),_H3cIfQoSPQClassRuleValue_Type())
h3cIfQoSPQClassRuleValue.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSPQClassRuleValue.setStatus(_A)
_H3cIfQoSPQClassRuleQueueType_Type=PriorityQueue
_H3cIfQoSPQClassRuleQueueType_Object=MibTableColumn
h3cIfQoSPQClassRuleQueueType=_H3cIfQoSPQClassRuleQueueType_Object((1,3,6,1,4,1,2011,10,2,65,1,2,2,1,3,1,3),_H3cIfQoSPQClassRuleQueueType_Type())
h3cIfQoSPQClassRuleQueueType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSPQClassRuleQueueType.setStatus(_A)
_H3cIfQoSPQClassRowStatus_Type=RowStatus
_H3cIfQoSPQClassRowStatus_Object=MibTableColumn
h3cIfQoSPQClassRowStatus=_H3cIfQoSPQClassRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,2,2,1,3,1,4),_H3cIfQoSPQClassRowStatus_Type())
h3cIfQoSPQClassRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSPQClassRowStatus.setStatus(_A)
_H3cIfQoSPQApplyTable_Object=MibTable
h3cIfQoSPQApplyTable=_H3cIfQoSPQApplyTable_Object((1,3,6,1,4,1,2011,10,2,65,1,2,2,1,4))
if mibBuilder.loadTexts:h3cIfQoSPQApplyTable.setStatus(_A)
_H3cIfQoSPQApplyEntry_Object=MibTableRow
h3cIfQoSPQApplyEntry=_H3cIfQoSPQApplyEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,2,2,1,4,1))
h3cIfQoSPQApplyEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:h3cIfQoSPQApplyEntry.setStatus(_A)
class _H3cIfQoSPQApplyListNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_H3cIfQoSPQApplyListNumber_Type.__name__=_D
_H3cIfQoSPQApplyListNumber_Object=MibTableColumn
h3cIfQoSPQApplyListNumber=_H3cIfQoSPQApplyListNumber_Object((1,3,6,1,4,1,2011,10,2,65,1,2,2,1,4,1,1),_H3cIfQoSPQApplyListNumber_Type())
h3cIfQoSPQApplyListNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSPQApplyListNumber.setStatus(_A)
_H3cIfQoSPQApplyRowStatus_Type=RowStatus
_H3cIfQoSPQApplyRowStatus_Object=MibTableColumn
h3cIfQoSPQApplyRowStatus=_H3cIfQoSPQApplyRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,2,2,1,4,1,2),_H3cIfQoSPQApplyRowStatus_Type())
h3cIfQoSPQApplyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSPQApplyRowStatus.setStatus(_A)
_H3cIfQoSPQRunInfoGroup_ObjectIdentity=ObjectIdentity
h3cIfQoSPQRunInfoGroup=_H3cIfQoSPQRunInfoGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,2,2,2))
_H3cIfQoSPQRunInfoTable_Object=MibTable
h3cIfQoSPQRunInfoTable=_H3cIfQoSPQRunInfoTable_Object((1,3,6,1,4,1,2011,10,2,65,1,2,2,2,1))
if mibBuilder.loadTexts:h3cIfQoSPQRunInfoTable.setStatus(_A)
_H3cIfQoSPQRunInfoEntry_Object=MibTableRow
h3cIfQoSPQRunInfoEntry=_H3cIfQoSPQRunInfoEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,2,2,2,1,1))
h3cIfQoSPQRunInfoEntry.setIndexNames((0,_G,_H),(0,_E,_u))
if mibBuilder.loadTexts:h3cIfQoSPQRunInfoEntry.setStatus(_A)
_H3cIfQoSPQType_Type=PriorityQueue
_H3cIfQoSPQType_Object=MibTableColumn
h3cIfQoSPQType=_H3cIfQoSPQType_Object((1,3,6,1,4,1,2011,10,2,65,1,2,2,2,1,1,1),_H3cIfQoSPQType_Type())
h3cIfQoSPQType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSPQType.setStatus(_A)
_H3cIfQoSPQSize_Type=Integer32
_H3cIfQoSPQSize_Object=MibTableColumn
h3cIfQoSPQSize=_H3cIfQoSPQSize_Object((1,3,6,1,4,1,2011,10,2,65,1,2,2,2,1,1,2),_H3cIfQoSPQSize_Type())
h3cIfQoSPQSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSPQSize.setStatus(_A)
_H3cIfQoSPQLength_Type=Integer32
_H3cIfQoSPQLength_Object=MibTableColumn
h3cIfQoSPQLength=_H3cIfQoSPQLength_Object((1,3,6,1,4,1,2011,10,2,65,1,2,2,2,1,1,3),_H3cIfQoSPQLength_Type())
h3cIfQoSPQLength.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSPQLength.setStatus(_A)
_H3cIfQoSPQDiscardPackets_Type=Counter64
_H3cIfQoSPQDiscardPackets_Object=MibTableColumn
h3cIfQoSPQDiscardPackets=_H3cIfQoSPQDiscardPackets_Object((1,3,6,1,4,1,2011,10,2,65,1,2,2,2,1,1,4),_H3cIfQoSPQDiscardPackets_Type())
h3cIfQoSPQDiscardPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSPQDiscardPackets.setStatus(_A)
_H3cIfQoSCQObject_ObjectIdentity=ObjectIdentity
h3cIfQoSCQObject=_H3cIfQoSCQObject_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,2,3))
_H3cIfQoSCQConfigGroup_ObjectIdentity=ObjectIdentity
h3cIfQoSCQConfigGroup=_H3cIfQoSCQConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,2,3,1))
_H3cIfQoSCQDefaultTable_Object=MibTable
h3cIfQoSCQDefaultTable=_H3cIfQoSCQDefaultTable_Object((1,3,6,1,4,1,2011,10,2,65,1,2,3,1,1))
if mibBuilder.loadTexts:h3cIfQoSCQDefaultTable.setStatus(_A)
_H3cIfQoSCQDefaultEntry_Object=MibTableRow
h3cIfQoSCQDefaultEntry=_H3cIfQoSCQDefaultEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,2,3,1,1,1))
h3cIfQoSCQDefaultEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:h3cIfQoSCQDefaultEntry.setStatus(_A)
class _H3cIfQoSCQListNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_H3cIfQoSCQListNumber_Type.__name__=_D
_H3cIfQoSCQListNumber_Object=MibTableColumn
h3cIfQoSCQListNumber=_H3cIfQoSCQListNumber_Object((1,3,6,1,4,1,2011,10,2,65,1,2,3,1,1,1,1),_H3cIfQoSCQListNumber_Type())
h3cIfQoSCQListNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSCQListNumber.setStatus(_A)
class _H3cIfQoSCQDefaultQueueID_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_H3cIfQoSCQDefaultQueueID_Type.__name__=_D
_H3cIfQoSCQDefaultQueueID_Object=MibTableColumn
h3cIfQoSCQDefaultQueueID=_H3cIfQoSCQDefaultQueueID_Object((1,3,6,1,4,1,2011,10,2,65,1,2,3,1,1,1,2),_H3cIfQoSCQDefaultQueueID_Type())
h3cIfQoSCQDefaultQueueID.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cIfQoSCQDefaultQueueID.setStatus(_A)
_H3cIfQoSCQQueueLengthTable_Object=MibTable
h3cIfQoSCQQueueLengthTable=_H3cIfQoSCQQueueLengthTable_Object((1,3,6,1,4,1,2011,10,2,65,1,2,3,1,2))
if mibBuilder.loadTexts:h3cIfQoSCQQueueLengthTable.setStatus(_A)
_H3cIfQoSCQQueueLengthEntry_Object=MibTableRow
h3cIfQoSCQQueueLengthEntry=_H3cIfQoSCQQueueLengthEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,2,3,1,2,1))
h3cIfQoSCQQueueLengthEntry.setIndexNames((0,_E,_R),(0,_E,_T))
if mibBuilder.loadTexts:h3cIfQoSCQQueueLengthEntry.setStatus(_A)
class _H3cIfQoSCQQueueID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_H3cIfQoSCQQueueID_Type.__name__=_D
_H3cIfQoSCQQueueID_Object=MibTableColumn
h3cIfQoSCQQueueID=_H3cIfQoSCQQueueID_Object((1,3,6,1,4,1,2011,10,2,65,1,2,3,1,2,1,1),_H3cIfQoSCQQueueID_Type())
h3cIfQoSCQQueueID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSCQQueueID.setStatus(_A)
class _H3cIfQoSCQQueueLength_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_H3cIfQoSCQQueueLength_Type.__name__=_D
_H3cIfQoSCQQueueLength_Object=MibTableColumn
h3cIfQoSCQQueueLength=_H3cIfQoSCQQueueLength_Object((1,3,6,1,4,1,2011,10,2,65,1,2,3,1,2,1,2),_H3cIfQoSCQQueueLength_Type())
h3cIfQoSCQQueueLength.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cIfQoSCQQueueLength.setStatus(_A)
class _H3cIfQoSCQQueueServing_Type(Integer32):defaultValue=1500
_H3cIfQoSCQQueueServing_Type.__name__=_D
_H3cIfQoSCQQueueServing_Object=MibTableColumn
h3cIfQoSCQQueueServing=_H3cIfQoSCQQueueServing_Object((1,3,6,1,4,1,2011,10,2,65,1,2,3,1,2,1,3),_H3cIfQoSCQQueueServing_Type())
h3cIfQoSCQQueueServing.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cIfQoSCQQueueServing.setStatus(_A)
_H3cIfQoSCQClassRuleTable_Object=MibTable
h3cIfQoSCQClassRuleTable=_H3cIfQoSCQClassRuleTable_Object((1,3,6,1,4,1,2011,10,2,65,1,2,3,1,3))
if mibBuilder.loadTexts:h3cIfQoSCQClassRuleTable.setStatus(_A)
_H3cIfQoSCQClassRuleEntry_Object=MibTableRow
h3cIfQoSCQClassRuleEntry=_H3cIfQoSCQClassRuleEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,2,3,1,3,1))
h3cIfQoSCQClassRuleEntry.setIndexNames((0,_E,_R),(0,_E,_v),(0,_E,_w))
if mibBuilder.loadTexts:h3cIfQoSCQClassRuleEntry.setStatus(_A)
class _H3cIfQoSCQClassRuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_q,1),(_L,2),(_M,3),(_r,4),(_s,5),(_t,6),('tcp',7),('udp',8),('ipall',9),('mpls',10)))
_H3cIfQoSCQClassRuleType_Type.__name__=_D
_H3cIfQoSCQClassRuleType_Object=MibTableColumn
h3cIfQoSCQClassRuleType=_H3cIfQoSCQClassRuleType_Object((1,3,6,1,4,1,2011,10,2,65,1,2,3,1,3,1,1),_H3cIfQoSCQClassRuleType_Type())
h3cIfQoSCQClassRuleType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSCQClassRuleType.setStatus(_A)
_H3cIfQoSCQClassRuleValue_Type=Integer32
_H3cIfQoSCQClassRuleValue_Object=MibTableColumn
h3cIfQoSCQClassRuleValue=_H3cIfQoSCQClassRuleValue_Object((1,3,6,1,4,1,2011,10,2,65,1,2,3,1,3,1,2),_H3cIfQoSCQClassRuleValue_Type())
h3cIfQoSCQClassRuleValue.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSCQClassRuleValue.setStatus(_A)
class _H3cIfQoSCQClassRuleQueueID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_H3cIfQoSCQClassRuleQueueID_Type.__name__=_D
_H3cIfQoSCQClassRuleQueueID_Object=MibTableColumn
h3cIfQoSCQClassRuleQueueID=_H3cIfQoSCQClassRuleQueueID_Object((1,3,6,1,4,1,2011,10,2,65,1,2,3,1,3,1,3),_H3cIfQoSCQClassRuleQueueID_Type())
h3cIfQoSCQClassRuleQueueID.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSCQClassRuleQueueID.setStatus(_A)
_H3cIfQoSCQClassRowStatus_Type=RowStatus
_H3cIfQoSCQClassRowStatus_Object=MibTableColumn
h3cIfQoSCQClassRowStatus=_H3cIfQoSCQClassRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,2,3,1,3,1,4),_H3cIfQoSCQClassRowStatus_Type())
h3cIfQoSCQClassRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSCQClassRowStatus.setStatus(_A)
_H3cIfQoSCQApplyTable_Object=MibTable
h3cIfQoSCQApplyTable=_H3cIfQoSCQApplyTable_Object((1,3,6,1,4,1,2011,10,2,65,1,2,3,1,4))
if mibBuilder.loadTexts:h3cIfQoSCQApplyTable.setStatus(_A)
_H3cIfQoSCQApplyEntry_Object=MibTableRow
h3cIfQoSCQApplyEntry=_H3cIfQoSCQApplyEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,2,3,1,4,1))
h3cIfQoSCQApplyEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:h3cIfQoSCQApplyEntry.setStatus(_A)
class _H3cIfQoSCQApplyListNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_H3cIfQoSCQApplyListNumber_Type.__name__=_D
_H3cIfQoSCQApplyListNumber_Object=MibTableColumn
h3cIfQoSCQApplyListNumber=_H3cIfQoSCQApplyListNumber_Object((1,3,6,1,4,1,2011,10,2,65,1,2,3,1,4,1,1),_H3cIfQoSCQApplyListNumber_Type())
h3cIfQoSCQApplyListNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSCQApplyListNumber.setStatus(_A)
_H3cIfQoSCQApplyRowStatus_Type=RowStatus
_H3cIfQoSCQApplyRowStatus_Object=MibTableColumn
h3cIfQoSCQApplyRowStatus=_H3cIfQoSCQApplyRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,2,3,1,4,1,2),_H3cIfQoSCQApplyRowStatus_Type())
h3cIfQoSCQApplyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSCQApplyRowStatus.setStatus(_A)
_H3cIfQoSCQRunInfoGroup_ObjectIdentity=ObjectIdentity
h3cIfQoSCQRunInfoGroup=_H3cIfQoSCQRunInfoGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,2,3,2))
_H3cIfQoSCQRunInfoTable_Object=MibTable
h3cIfQoSCQRunInfoTable=_H3cIfQoSCQRunInfoTable_Object((1,3,6,1,4,1,2011,10,2,65,1,2,3,2,1))
if mibBuilder.loadTexts:h3cIfQoSCQRunInfoTable.setStatus(_A)
_H3cIfQoSCQRunInfoEntry_Object=MibTableRow
h3cIfQoSCQRunInfoEntry=_H3cIfQoSCQRunInfoEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,2,3,2,1,1))
h3cIfQoSCQRunInfoEntry.setIndexNames((0,_G,_H),(0,_E,_T))
if mibBuilder.loadTexts:h3cIfQoSCQRunInfoEntry.setStatus(_A)
_H3cIfQoSCQRunInfoSize_Type=Integer32
_H3cIfQoSCQRunInfoSize_Object=MibTableColumn
h3cIfQoSCQRunInfoSize=_H3cIfQoSCQRunInfoSize_Object((1,3,6,1,4,1,2011,10,2,65,1,2,3,2,1,1,1),_H3cIfQoSCQRunInfoSize_Type())
h3cIfQoSCQRunInfoSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSCQRunInfoSize.setStatus(_A)
_H3cIfQoSCQRunInfoLength_Type=Integer32
_H3cIfQoSCQRunInfoLength_Object=MibTableColumn
h3cIfQoSCQRunInfoLength=_H3cIfQoSCQRunInfoLength_Object((1,3,6,1,4,1,2011,10,2,65,1,2,3,2,1,1,2),_H3cIfQoSCQRunInfoLength_Type())
h3cIfQoSCQRunInfoLength.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSCQRunInfoLength.setStatus(_A)
_H3cIfQoSCQRunInfoDiscardPackets_Type=Counter64
_H3cIfQoSCQRunInfoDiscardPackets_Object=MibTableColumn
h3cIfQoSCQRunInfoDiscardPackets=_H3cIfQoSCQRunInfoDiscardPackets_Object((1,3,6,1,4,1,2011,10,2,65,1,2,3,2,1,1,3),_H3cIfQoSCQRunInfoDiscardPackets_Type())
h3cIfQoSCQRunInfoDiscardPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSCQRunInfoDiscardPackets.setStatus(_A)
_H3cIfQoSWFQObject_ObjectIdentity=ObjectIdentity
h3cIfQoSWFQObject=_H3cIfQoSWFQObject_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,2,4))
_H3cIfQoSWFQConfigGroup_ObjectIdentity=ObjectIdentity
h3cIfQoSWFQConfigGroup=_H3cIfQoSWFQConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,2,4,1))
_H3cIfQoSWFQTable_Object=MibTable
h3cIfQoSWFQTable=_H3cIfQoSWFQTable_Object((1,3,6,1,4,1,2011,10,2,65,1,2,4,1,1))
if mibBuilder.loadTexts:h3cIfQoSWFQTable.setStatus(_A)
_H3cIfQoSWFQEntry_Object=MibTableRow
h3cIfQoSWFQEntry=_H3cIfQoSWFQEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,2,4,1,1,1))
h3cIfQoSWFQEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:h3cIfQoSWFQEntry.setStatus(_A)
class _H3cIfQoSWFQQueueLength_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_H3cIfQoSWFQQueueLength_Type.__name__=_D
_H3cIfQoSWFQQueueLength_Object=MibTableColumn
h3cIfQoSWFQQueueLength=_H3cIfQoSWFQQueueLength_Object((1,3,6,1,4,1,2011,10,2,65,1,2,4,1,1,1,1),_H3cIfQoSWFQQueueLength_Type())
h3cIfQoSWFQQueueLength.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSWFQQueueLength.setStatus(_A)
class _H3cIfQoSWFQQueueNumber_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('size16',1),('size32',2),('size64',3),('size128',4),('size256',5),('size512',6),('size1024',7),('size2048',8),('size4096',9)))
_H3cIfQoSWFQQueueNumber_Type.__name__=_D
_H3cIfQoSWFQQueueNumber_Object=MibTableColumn
h3cIfQoSWFQQueueNumber=_H3cIfQoSWFQQueueNumber_Object((1,3,6,1,4,1,2011,10,2,65,1,2,4,1,1,1,2),_H3cIfQoSWFQQueueNumber_Type())
h3cIfQoSWFQQueueNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSWFQQueueNumber.setStatus(_A)
_H3cIfQoSWFQRowStatus_Type=RowStatus
_H3cIfQoSWFQRowStatus_Object=MibTableColumn
h3cIfQoSWFQRowStatus=_H3cIfQoSWFQRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,2,4,1,1,1,3),_H3cIfQoSWFQRowStatus_Type())
h3cIfQoSWFQRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSWFQRowStatus.setStatus(_A)
class _H3cIfQoSWFQType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ip-precedence',1),(_N,2)))
_H3cIfQoSWFQType_Type.__name__=_D
_H3cIfQoSWFQType_Object=MibTableColumn
h3cIfQoSWFQType=_H3cIfQoSWFQType_Object((1,3,6,1,4,1,2011,10,2,65,1,2,4,1,1,1,4),_H3cIfQoSWFQType_Type())
h3cIfQoSWFQType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSWFQType.setStatus(_A)
_H3cIfQoSWFQRunInfoGroup_ObjectIdentity=ObjectIdentity
h3cIfQoSWFQRunInfoGroup=_H3cIfQoSWFQRunInfoGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,2,4,2))
_H3cIfQoSWFQRunInfoTable_Object=MibTable
h3cIfQoSWFQRunInfoTable=_H3cIfQoSWFQRunInfoTable_Object((1,3,6,1,4,1,2011,10,2,65,1,2,4,2,1))
if mibBuilder.loadTexts:h3cIfQoSWFQRunInfoTable.setStatus(_A)
_H3cIfQoSWFQRunInfoEntry_Object=MibTableRow
h3cIfQoSWFQRunInfoEntry=_H3cIfQoSWFQRunInfoEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,2,4,2,1,1))
h3cIfQoSWFQRunInfoEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:h3cIfQoSWFQRunInfoEntry.setStatus(_A)
_H3cIfQoSWFQSize_Type=Integer32
_H3cIfQoSWFQSize_Object=MibTableColumn
h3cIfQoSWFQSize=_H3cIfQoSWFQSize_Object((1,3,6,1,4,1,2011,10,2,65,1,2,4,2,1,1,1),_H3cIfQoSWFQSize_Type())
h3cIfQoSWFQSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWFQSize.setStatus(_A)
_H3cIfQoSWFQLength_Type=Integer32
_H3cIfQoSWFQLength_Object=MibTableColumn
h3cIfQoSWFQLength=_H3cIfQoSWFQLength_Object((1,3,6,1,4,1,2011,10,2,65,1,2,4,2,1,1,2),_H3cIfQoSWFQLength_Type())
h3cIfQoSWFQLength.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWFQLength.setStatus(_A)
_H3cIfQoSWFQDiscardPackets_Type=Counter64
_H3cIfQoSWFQDiscardPackets_Object=MibTableColumn
h3cIfQoSWFQDiscardPackets=_H3cIfQoSWFQDiscardPackets_Object((1,3,6,1,4,1,2011,10,2,65,1,2,4,2,1,1,3),_H3cIfQoSWFQDiscardPackets_Type())
h3cIfQoSWFQDiscardPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWFQDiscardPackets.setStatus(_A)
_H3cIfQoSWFQHashedActiveQueues_Type=Integer32
_H3cIfQoSWFQHashedActiveQueues_Object=MibTableColumn
h3cIfQoSWFQHashedActiveQueues=_H3cIfQoSWFQHashedActiveQueues_Object((1,3,6,1,4,1,2011,10,2,65,1,2,4,2,1,1,4),_H3cIfQoSWFQHashedActiveQueues_Type())
h3cIfQoSWFQHashedActiveQueues.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWFQHashedActiveQueues.setStatus(_A)
_H3cIfQoSWFQHashedMaxActiveQueues_Type=Integer32
_H3cIfQoSWFQHashedMaxActiveQueues_Object=MibTableColumn
h3cIfQoSWFQHashedMaxActiveQueues=_H3cIfQoSWFQHashedMaxActiveQueues_Object((1,3,6,1,4,1,2011,10,2,65,1,2,4,2,1,1,5),_H3cIfQoSWFQHashedMaxActiveQueues_Type())
h3cIfQoSWFQHashedMaxActiveQueues.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWFQHashedMaxActiveQueues.setStatus(_A)
_H3fIfQosWFQhashedTotalQueues_Type=Integer32
_H3fIfQosWFQhashedTotalQueues_Object=MibTableColumn
h3fIfQosWFQhashedTotalQueues=_H3fIfQosWFQhashedTotalQueues_Object((1,3,6,1,4,1,2011,10,2,65,1,2,4,2,1,1,6),_H3fIfQosWFQhashedTotalQueues_Type())
h3fIfQosWFQhashedTotalQueues.setMaxAccess(_C)
if mibBuilder.loadTexts:h3fIfQosWFQhashedTotalQueues.setStatus(_A)
_H3cIfQoSBandwidthGroup_ObjectIdentity=ObjectIdentity
h3cIfQoSBandwidthGroup=_H3cIfQoSBandwidthGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,2,5))
_H3cIfQoSBandwidthTable_Object=MibTable
h3cIfQoSBandwidthTable=_H3cIfQoSBandwidthTable_Object((1,3,6,1,4,1,2011,10,2,65,1,2,5,1))
if mibBuilder.loadTexts:h3cIfQoSBandwidthTable.setStatus(_A)
_H3cIfQoSBandwidthEntry_Object=MibTableRow
h3cIfQoSBandwidthEntry=_H3cIfQoSBandwidthEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,2,5,1,1))
h3cIfQoSBandwidthEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:h3cIfQoSBandwidthEntry.setStatus(_A)
_H3cIfQoSMaxBandwidth_Type=Integer32
_H3cIfQoSMaxBandwidth_Object=MibTableColumn
h3cIfQoSMaxBandwidth=_H3cIfQoSMaxBandwidth_Object((1,3,6,1,4,1,2011,10,2,65,1,2,5,1,1,1),_H3cIfQoSMaxBandwidth_Type())
h3cIfQoSMaxBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSMaxBandwidth.setStatus(_A)
class _H3cIfQoSReservedBandwidthPct_Type(Integer32):defaultValue=75;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_H3cIfQoSReservedBandwidthPct_Type.__name__=_D
_H3cIfQoSReservedBandwidthPct_Object=MibTableColumn
h3cIfQoSReservedBandwidthPct=_H3cIfQoSReservedBandwidthPct_Object((1,3,6,1,4,1,2011,10,2,65,1,2,5,1,1,2),_H3cIfQoSReservedBandwidthPct_Type())
h3cIfQoSReservedBandwidthPct.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSReservedBandwidthPct.setStatus(_A)
_H3cIfQoSBandwidthRowStatus_Type=RowStatus
_H3cIfQoSBandwidthRowStatus_Object=MibTableColumn
h3cIfQoSBandwidthRowStatus=_H3cIfQoSBandwidthRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,2,5,1,1,3),_H3cIfQoSBandwidthRowStatus_Type())
h3cIfQoSBandwidthRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSBandwidthRowStatus.setStatus(_A)
_H3cIfQoSQmtokenGroup_ObjectIdentity=ObjectIdentity
h3cIfQoSQmtokenGroup=_H3cIfQoSQmtokenGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,2,6))
_H3cIfQoSQmtokenTable_Object=MibTable
h3cIfQoSQmtokenTable=_H3cIfQoSQmtokenTable_Object((1,3,6,1,4,1,2011,10,2,65,1,2,6,1))
if mibBuilder.loadTexts:h3cIfQoSQmtokenTable.setStatus(_A)
_H3cIfQoSQmtokenEntry_Object=MibTableRow
h3cIfQoSQmtokenEntry=_H3cIfQoSQmtokenEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,2,6,1,1))
h3cIfQoSQmtokenEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:h3cIfQoSQmtokenEntry.setStatus(_A)
class _H3cIfQoSQmtokenNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_H3cIfQoSQmtokenNumber_Type.__name__=_D
_H3cIfQoSQmtokenNumber_Object=MibTableColumn
h3cIfQoSQmtokenNumber=_H3cIfQoSQmtokenNumber_Object((1,3,6,1,4,1,2011,10,2,65,1,2,6,1,1,1),_H3cIfQoSQmtokenNumber_Type())
h3cIfQoSQmtokenNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSQmtokenNumber.setStatus(_A)
_H3cIfQoSQmtokenRosStatus_Type=RowStatus
_H3cIfQoSQmtokenRosStatus_Object=MibTableColumn
h3cIfQoSQmtokenRosStatus=_H3cIfQoSQmtokenRosStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,2,6,1,1,2),_H3cIfQoSQmtokenRosStatus_Type())
h3cIfQoSQmtokenRosStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSQmtokenRosStatus.setStatus(_A)
_H3cIfQoSRTPQObject_ObjectIdentity=ObjectIdentity
h3cIfQoSRTPQObject=_H3cIfQoSRTPQObject_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,2,7))
_H3cIfQoSRTPQConfigGroup_ObjectIdentity=ObjectIdentity
h3cIfQoSRTPQConfigGroup=_H3cIfQoSRTPQConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,2,7,1))
_H3cIfQoSRTPQConfigTable_Object=MibTable
h3cIfQoSRTPQConfigTable=_H3cIfQoSRTPQConfigTable_Object((1,3,6,1,4,1,2011,10,2,65,1,2,7,1,1))
if mibBuilder.loadTexts:h3cIfQoSRTPQConfigTable.setStatus(_A)
_H3cIfQoSRTPQConfigEntry_Object=MibTableRow
h3cIfQoSRTPQConfigEntry=_H3cIfQoSRTPQConfigEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,2,7,1,1,1))
h3cIfQoSRTPQConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:h3cIfQoSRTPQConfigEntry.setStatus(_A)
class _H3cIfQoSRTPQStartPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2000,65535))
_H3cIfQoSRTPQStartPort_Type.__name__=_D
_H3cIfQoSRTPQStartPort_Object=MibTableColumn
h3cIfQoSRTPQStartPort=_H3cIfQoSRTPQStartPort_Object((1,3,6,1,4,1,2011,10,2,65,1,2,7,1,1,1,1),_H3cIfQoSRTPQStartPort_Type())
h3cIfQoSRTPQStartPort.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSRTPQStartPort.setStatus(_A)
class _H3cIfQoSRTPQEndPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2000,65535))
_H3cIfQoSRTPQEndPort_Type.__name__=_D
_H3cIfQoSRTPQEndPort_Object=MibTableColumn
h3cIfQoSRTPQEndPort=_H3cIfQoSRTPQEndPort_Object((1,3,6,1,4,1,2011,10,2,65,1,2,7,1,1,1,2),_H3cIfQoSRTPQEndPort_Type())
h3cIfQoSRTPQEndPort.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSRTPQEndPort.setStatus(_A)
_H3cIfQoSRTPQReservedBandwidth_Type=Integer32
_H3cIfQoSRTPQReservedBandwidth_Object=MibTableColumn
h3cIfQoSRTPQReservedBandwidth=_H3cIfQoSRTPQReservedBandwidth_Object((1,3,6,1,4,1,2011,10,2,65,1,2,7,1,1,1,3),_H3cIfQoSRTPQReservedBandwidth_Type())
h3cIfQoSRTPQReservedBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSRTPQReservedBandwidth.setStatus(_A)
_H3cIfQoSRTPQCbs_Type=Unsigned32
_H3cIfQoSRTPQCbs_Object=MibTableColumn
h3cIfQoSRTPQCbs=_H3cIfQoSRTPQCbs_Object((1,3,6,1,4,1,2011,10,2,65,1,2,7,1,1,1,4),_H3cIfQoSRTPQCbs_Type())
h3cIfQoSRTPQCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSRTPQCbs.setStatus(_A)
_H3cIfQoSRTPQRowStatus_Type=RowStatus
_H3cIfQoSRTPQRowStatus_Object=MibTableColumn
h3cIfQoSRTPQRowStatus=_H3cIfQoSRTPQRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,2,7,1,1,1,5),_H3cIfQoSRTPQRowStatus_Type())
h3cIfQoSRTPQRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSRTPQRowStatus.setStatus(_A)
_H3cIfQoSRTPQRunInfoGroup_ObjectIdentity=ObjectIdentity
h3cIfQoSRTPQRunInfoGroup=_H3cIfQoSRTPQRunInfoGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,2,7,2))
_H3cIfQoSRTPQRunInfoTable_Object=MibTable
h3cIfQoSRTPQRunInfoTable=_H3cIfQoSRTPQRunInfoTable_Object((1,3,6,1,4,1,2011,10,2,65,1,2,7,2,1))
if mibBuilder.loadTexts:h3cIfQoSRTPQRunInfoTable.setStatus(_A)
_H3cIfQoSRTPQRunInfoEntry_Object=MibTableRow
h3cIfQoSRTPQRunInfoEntry=_H3cIfQoSRTPQRunInfoEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,2,7,2,1,1))
h3cIfQoSRTPQRunInfoEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:h3cIfQoSRTPQRunInfoEntry.setStatus(_A)
_H3cIfQoSRTPQPacketNumber_Type=Integer32
_H3cIfQoSRTPQPacketNumber_Object=MibTableColumn
h3cIfQoSRTPQPacketNumber=_H3cIfQoSRTPQPacketNumber_Object((1,3,6,1,4,1,2011,10,2,65,1,2,7,2,1,1,1),_H3cIfQoSRTPQPacketNumber_Type())
h3cIfQoSRTPQPacketNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSRTPQPacketNumber.setStatus(_A)
_H3cIfQoSRTPQPacketSize_Type=Integer32
_H3cIfQoSRTPQPacketSize_Object=MibTableColumn
h3cIfQoSRTPQPacketSize=_H3cIfQoSRTPQPacketSize_Object((1,3,6,1,4,1,2011,10,2,65,1,2,7,2,1,1,2),_H3cIfQoSRTPQPacketSize_Type())
h3cIfQoSRTPQPacketSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSRTPQPacketSize.setStatus(_A)
_H3cIfQoSRTPQOutputPackets_Type=Counter64
_H3cIfQoSRTPQOutputPackets_Object=MibTableColumn
h3cIfQoSRTPQOutputPackets=_H3cIfQoSRTPQOutputPackets_Object((1,3,6,1,4,1,2011,10,2,65,1,2,7,2,1,1,3),_H3cIfQoSRTPQOutputPackets_Type())
h3cIfQoSRTPQOutputPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSRTPQOutputPackets.setStatus(_A)
_H3cIfQoSRTPQDiscardPackets_Type=Counter64
_H3cIfQoSRTPQDiscardPackets_Object=MibTableColumn
h3cIfQoSRTPQDiscardPackets=_H3cIfQoSRTPQDiscardPackets_Object((1,3,6,1,4,1,2011,10,2,65,1,2,7,2,1,1,4),_H3cIfQoSRTPQDiscardPackets_Type())
h3cIfQoSRTPQDiscardPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSRTPQDiscardPackets.setStatus(_A)
_H3cIfQoSCarListObject_ObjectIdentity=ObjectIdentity
h3cIfQoSCarListObject=_H3cIfQoSCarListObject_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,2,8))
_H3cIfQoCarListGroup_ObjectIdentity=ObjectIdentity
h3cIfQoCarListGroup=_H3cIfQoCarListGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,2,8,1))
_H3cIfQoSCarlTable_Object=MibTable
h3cIfQoSCarlTable=_H3cIfQoSCarlTable_Object((1,3,6,1,4,1,2011,10,2,65,1,2,8,1,1))
if mibBuilder.loadTexts:h3cIfQoSCarlTable.setStatus(_A)
_H3cIfQoSCarlEntry_Object=MibTableRow
h3cIfQoSCarlEntry=_H3cIfQoSCarlEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,2,8,1,1,1))
h3cIfQoSCarlEntry.setIndexNames((0,_E,_x))
if mibBuilder.loadTexts:h3cIfQoSCarlEntry.setStatus(_A)
_H3cIfQoSCarlListNum_Type=Integer32
_H3cIfQoSCarlListNum_Object=MibTableColumn
h3cIfQoSCarlListNum=_H3cIfQoSCarlListNum_Object((1,3,6,1,4,1,2011,10,2,65,1,2,8,1,1,1,1),_H3cIfQoSCarlListNum_Type())
h3cIfQoSCarlListNum.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSCarlListNum.setStatus(_A)
class _H3cIfQoSCarlParaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('macAddress',1),('precMask',2),('dscpMask',3)))
_H3cIfQoSCarlParaType_Type.__name__=_D
_H3cIfQoSCarlParaType_Object=MibTableColumn
h3cIfQoSCarlParaType=_H3cIfQoSCarlParaType_Object((1,3,6,1,4,1,2011,10,2,65,1,2,8,1,1,1,2),_H3cIfQoSCarlParaType_Type())
h3cIfQoSCarlParaType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSCarlParaType.setStatus(_A)
_H3cIfQoSCarlParaValue_Type=OctetString
_H3cIfQoSCarlParaValue_Object=MibTableColumn
h3cIfQoSCarlParaValue=_H3cIfQoSCarlParaValue_Object((1,3,6,1,4,1,2011,10,2,65,1,2,8,1,1,1,3),_H3cIfQoSCarlParaValue_Type())
h3cIfQoSCarlParaValue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSCarlParaValue.setStatus(_A)
_H3cIfQoSCarlRowStatus_Type=RowStatus
_H3cIfQoSCarlRowStatus_Object=MibTableColumn
h3cIfQoSCarlRowStatus=_H3cIfQoSCarlRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,2,8,1,1,1,4),_H3cIfQoSCarlRowStatus_Type())
h3cIfQoSCarlRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSCarlRowStatus.setStatus(_A)
_H3cIfQoSLineRateObjects_ObjectIdentity=ObjectIdentity
h3cIfQoSLineRateObjects=_H3cIfQoSLineRateObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,3))
_H3cIfQoSLRConfigTable_Object=MibTable
h3cIfQoSLRConfigTable=_H3cIfQoSLRConfigTable_Object((1,3,6,1,4,1,2011,10,2,65,1,3,1))
if mibBuilder.loadTexts:h3cIfQoSLRConfigTable.setStatus(_A)
_H3cIfQoSLRConfigEntry_Object=MibTableRow
h3cIfQoSLRConfigEntry=_H3cIfQoSLRConfigEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,3,1,1))
h3cIfQoSLRConfigEntry.setIndexNames((0,_G,_H),(0,_E,_U))
if mibBuilder.loadTexts:h3cIfQoSLRConfigEntry.setStatus(_A)
_H3cIfQoSLRDirection_Type=Direction
_H3cIfQoSLRDirection_Object=MibTableColumn
h3cIfQoSLRDirection=_H3cIfQoSLRDirection_Object((1,3,6,1,4,1,2011,10,2,65,1,3,1,1,1),_H3cIfQoSLRDirection_Type())
h3cIfQoSLRDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSLRDirection.setStatus(_A)
_H3cIfQoSLRCir_Type=Unsigned32
_H3cIfQoSLRCir_Object=MibTableColumn
h3cIfQoSLRCir=_H3cIfQoSLRCir_Object((1,3,6,1,4,1,2011,10,2,65,1,3,1,1,2),_H3cIfQoSLRCir_Type())
h3cIfQoSLRCir.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSLRCir.setStatus(_A)
_H3cIfQoSLRCbs_Type=Unsigned32
_H3cIfQoSLRCbs_Object=MibTableColumn
h3cIfQoSLRCbs=_H3cIfQoSLRCbs_Object((1,3,6,1,4,1,2011,10,2,65,1,3,1,1,3),_H3cIfQoSLRCbs_Type())
h3cIfQoSLRCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSLRCbs.setStatus(_A)
_H3cIfQoSLREbs_Type=Unsigned32
_H3cIfQoSLREbs_Object=MibTableColumn
h3cIfQoSLREbs=_H3cIfQoSLREbs_Object((1,3,6,1,4,1,2011,10,2,65,1,3,1,1,4),_H3cIfQoSLREbs_Type())
h3cIfQoSLREbs.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSLREbs.setStatus(_A)
_H3cIfQoSRowStatus_Type=RowStatus
_H3cIfQoSRowStatus_Object=MibTableColumn
h3cIfQoSRowStatus=_H3cIfQoSRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,3,1,1,5),_H3cIfQoSRowStatus_Type())
h3cIfQoSRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSRowStatus.setStatus(_A)
_H3cIfQoSLRPir_Type=Unsigned32
_H3cIfQoSLRPir_Object=MibTableColumn
h3cIfQoSLRPir=_H3cIfQoSLRPir_Object((1,3,6,1,4,1,2011,10,2,65,1,3,1,1,6),_H3cIfQoSLRPir_Type())
h3cIfQoSLRPir.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSLRPir.setStatus(_A)
class _H3cIfQoSLRUnit_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_W,2)))
_H3cIfQoSLRUnit_Type.__name__=_D
_H3cIfQoSLRUnit_Object=MibTableColumn
h3cIfQoSLRUnit=_H3cIfQoSLRUnit_Object((1,3,6,1,4,1,2011,10,2,65,1,3,1,1,7),_H3cIfQoSLRUnit_Type())
h3cIfQoSLRUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSLRUnit.setStatus(_A)
_H3cIfQoSLRRunInfoTable_Object=MibTable
h3cIfQoSLRRunInfoTable=_H3cIfQoSLRRunInfoTable_Object((1,3,6,1,4,1,2011,10,2,65,1,3,2))
if mibBuilder.loadTexts:h3cIfQoSLRRunInfoTable.setStatus(_A)
_H3cIfQoSLRRunInfoEntry_Object=MibTableRow
h3cIfQoSLRRunInfoEntry=_H3cIfQoSLRRunInfoEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,3,2,1))
h3cIfQoSLRRunInfoEntry.setIndexNames((0,_G,_H),(0,_E,_U))
if mibBuilder.loadTexts:h3cIfQoSLRRunInfoEntry.setStatus(_A)
_H3cIfQoSLRRunInfoPassedPackets_Type=Counter64
_H3cIfQoSLRRunInfoPassedPackets_Object=MibTableColumn
h3cIfQoSLRRunInfoPassedPackets=_H3cIfQoSLRRunInfoPassedPackets_Object((1,3,6,1,4,1,2011,10,2,65,1,3,2,1,1),_H3cIfQoSLRRunInfoPassedPackets_Type())
h3cIfQoSLRRunInfoPassedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSLRRunInfoPassedPackets.setStatus(_A)
_H3cIfQoSLRRunInfoPassedBytes_Type=Counter64
_H3cIfQoSLRRunInfoPassedBytes_Object=MibTableColumn
h3cIfQoSLRRunInfoPassedBytes=_H3cIfQoSLRRunInfoPassedBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,3,2,1,2),_H3cIfQoSLRRunInfoPassedBytes_Type())
h3cIfQoSLRRunInfoPassedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSLRRunInfoPassedBytes.setStatus(_A)
_H3cIfQoSLRRunInfoDelayedPackets_Type=Counter64
_H3cIfQoSLRRunInfoDelayedPackets_Object=MibTableColumn
h3cIfQoSLRRunInfoDelayedPackets=_H3cIfQoSLRRunInfoDelayedPackets_Object((1,3,6,1,4,1,2011,10,2,65,1,3,2,1,3),_H3cIfQoSLRRunInfoDelayedPackets_Type())
h3cIfQoSLRRunInfoDelayedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSLRRunInfoDelayedPackets.setStatus(_A)
_H3cIfQoSLRRunInfoDelayedBytes_Type=Counter64
_H3cIfQoSLRRunInfoDelayedBytes_Object=MibTableColumn
h3cIfQoSLRRunInfoDelayedBytes=_H3cIfQoSLRRunInfoDelayedBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,3,2,1,4),_H3cIfQoSLRRunInfoDelayedBytes_Type())
h3cIfQoSLRRunInfoDelayedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSLRRunInfoDelayedBytes.setStatus(_A)
class _H3cIfQoSLRRunInfoActiveShaping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_H3cIfQoSLRRunInfoActiveShaping_Type.__name__=_D
_H3cIfQoSLRRunInfoActiveShaping_Object=MibTableColumn
h3cIfQoSLRRunInfoActiveShaping=_H3cIfQoSLRRunInfoActiveShaping_Object((1,3,6,1,4,1,2011,10,2,65,1,3,2,1,5),_H3cIfQoSLRRunInfoActiveShaping_Type())
h3cIfQoSLRRunInfoActiveShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSLRRunInfoActiveShaping.setStatus(_A)
_H3cIfQoSCARObjects_ObjectIdentity=ObjectIdentity
h3cIfQoSCARObjects=_H3cIfQoSCARObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,4))
_H3cIfQoSAggregativeCarGroup_ObjectIdentity=ObjectIdentity
h3cIfQoSAggregativeCarGroup=_H3cIfQoSAggregativeCarGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,4,1))
_H3cIfQoSAggregativeCarNextIndex_Type=Integer32
_H3cIfQoSAggregativeCarNextIndex_Object=MibScalar
h3cIfQoSAggregativeCarNextIndex=_H3cIfQoSAggregativeCarNextIndex_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,1),_H3cIfQoSAggregativeCarNextIndex_Type())
h3cIfQoSAggregativeCarNextIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarNextIndex.setStatus(_A)
_H3cIfQoSAggregativeCarConfigTable_Object=MibTable
h3cIfQoSAggregativeCarConfigTable=_H3cIfQoSAggregativeCarConfigTable_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,2))
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarConfigTable.setStatus(_A)
_H3cIfQoSAggregativeCarConfigEntry_Object=MibTableRow
h3cIfQoSAggregativeCarConfigEntry=_H3cIfQoSAggregativeCarConfigEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,2,1))
h3cIfQoSAggregativeCarConfigEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarConfigEntry.setStatus(_A)
class _H3cIfQoSAggregativeCarIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65534))
_H3cIfQoSAggregativeCarIndex_Type.__name__=_D
_H3cIfQoSAggregativeCarIndex_Object=MibTableColumn
h3cIfQoSAggregativeCarIndex=_H3cIfQoSAggregativeCarIndex_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,2,1,1),_H3cIfQoSAggregativeCarIndex_Type())
h3cIfQoSAggregativeCarIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarIndex.setStatus(_A)
class _H3cIfQoSAggregativeCarName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_H3cIfQoSAggregativeCarName_Type.__name__=_K
_H3cIfQoSAggregativeCarName_Object=MibTableColumn
h3cIfQoSAggregativeCarName=_H3cIfQoSAggregativeCarName_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,2,1,2),_H3cIfQoSAggregativeCarName_Type())
h3cIfQoSAggregativeCarName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarName.setStatus(_A)
_H3cIfQoSAggregativeCarCir_Type=Unsigned32
_H3cIfQoSAggregativeCarCir_Object=MibTableColumn
h3cIfQoSAggregativeCarCir=_H3cIfQoSAggregativeCarCir_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,2,1,3),_H3cIfQoSAggregativeCarCir_Type())
h3cIfQoSAggregativeCarCir.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarCir.setStatus(_A)
_H3cIfQoSAggregativeCarCbs_Type=Unsigned32
_H3cIfQoSAggregativeCarCbs_Object=MibTableColumn
h3cIfQoSAggregativeCarCbs=_H3cIfQoSAggregativeCarCbs_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,2,1,4),_H3cIfQoSAggregativeCarCbs_Type())
h3cIfQoSAggregativeCarCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarCbs.setStatus(_A)
_H3cIfQoSAggregativeCarEbs_Type=Unsigned32
_H3cIfQoSAggregativeCarEbs_Object=MibTableColumn
h3cIfQoSAggregativeCarEbs=_H3cIfQoSAggregativeCarEbs_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,2,1,5),_H3cIfQoSAggregativeCarEbs_Type())
h3cIfQoSAggregativeCarEbs.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarEbs.setStatus(_A)
class _H3cIfQoSAggregativeCarPir_Type(Unsigned32):defaultValue=4294967295
_H3cIfQoSAggregativeCarPir_Type.__name__=_I
_H3cIfQoSAggregativeCarPir_Object=MibTableColumn
h3cIfQoSAggregativeCarPir=_H3cIfQoSAggregativeCarPir_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,2,1,6),_H3cIfQoSAggregativeCarPir_Type())
h3cIfQoSAggregativeCarPir.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarPir.setStatus(_A)
class _H3cIfQoSAggregativeCarGreenActionType_Type(H3cIfCarAction):defaultValue=1
_H3cIfQoSAggregativeCarGreenActionType_Type.__name__=_O
_H3cIfQoSAggregativeCarGreenActionType_Object=MibTableColumn
h3cIfQoSAggregativeCarGreenActionType=_H3cIfQoSAggregativeCarGreenActionType_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,2,1,7),_H3cIfQoSAggregativeCarGreenActionType_Type())
h3cIfQoSAggregativeCarGreenActionType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarGreenActionType.setStatus(_A)
class _H3cIfQoSAggregativeCarGreenActionValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_H3cIfQoSAggregativeCarGreenActionValue_Type.__name__=_D
_H3cIfQoSAggregativeCarGreenActionValue_Object=MibTableColumn
h3cIfQoSAggregativeCarGreenActionValue=_H3cIfQoSAggregativeCarGreenActionValue_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,2,1,8),_H3cIfQoSAggregativeCarGreenActionValue_Type())
h3cIfQoSAggregativeCarGreenActionValue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarGreenActionValue.setStatus(_A)
_H3cIfQoSAggregativeCarYellowActionType_Type=H3cIfCarAction
_H3cIfQoSAggregativeCarYellowActionType_Object=MibTableColumn
h3cIfQoSAggregativeCarYellowActionType=_H3cIfQoSAggregativeCarYellowActionType_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,2,1,9),_H3cIfQoSAggregativeCarYellowActionType_Type())
h3cIfQoSAggregativeCarYellowActionType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarYellowActionType.setStatus(_A)
class _H3cIfQoSAggregativeCarYellowActionValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_H3cIfQoSAggregativeCarYellowActionValue_Type.__name__=_D
_H3cIfQoSAggregativeCarYellowActionValue_Object=MibTableColumn
h3cIfQoSAggregativeCarYellowActionValue=_H3cIfQoSAggregativeCarYellowActionValue_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,2,1,10),_H3cIfQoSAggregativeCarYellowActionValue_Type())
h3cIfQoSAggregativeCarYellowActionValue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarYellowActionValue.setStatus(_A)
_H3cIfQoSAggregativeCarRedActionType_Type=H3cIfCarAction
_H3cIfQoSAggregativeCarRedActionType_Object=MibTableColumn
h3cIfQoSAggregativeCarRedActionType=_H3cIfQoSAggregativeCarRedActionType_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,2,1,11),_H3cIfQoSAggregativeCarRedActionType_Type())
h3cIfQoSAggregativeCarRedActionType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarRedActionType.setStatus(_A)
class _H3cIfQoSAggregativeCarRedActionValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_H3cIfQoSAggregativeCarRedActionValue_Type.__name__=_D
_H3cIfQoSAggregativeCarRedActionValue_Object=MibTableColumn
h3cIfQoSAggregativeCarRedActionValue=_H3cIfQoSAggregativeCarRedActionValue_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,2,1,12),_H3cIfQoSAggregativeCarRedActionValue_Type())
h3cIfQoSAggregativeCarRedActionValue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarRedActionValue.setStatus(_A)
class _H3cIfQoSAggregativeCarType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('aggregative',1),('notAggregative',2),('hierarchy',3)))
_H3cIfQoSAggregativeCarType_Type.__name__=_D
_H3cIfQoSAggregativeCarType_Object=MibTableColumn
h3cIfQoSAggregativeCarType=_H3cIfQoSAggregativeCarType_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,2,1,13),_H3cIfQoSAggregativeCarType_Type())
h3cIfQoSAggregativeCarType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarType.setStatus(_A)
_H3cIfQoSAggregativeCarRowStatus_Type=RowStatus
_H3cIfQoSAggregativeCarRowStatus_Object=MibTableColumn
h3cIfQoSAggregativeCarRowStatus=_H3cIfQoSAggregativeCarRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,2,1,14),_H3cIfQoSAggregativeCarRowStatus_Type())
h3cIfQoSAggregativeCarRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarRowStatus.setStatus(_A)
_H3cIfQoSAggregativeCarApplyTable_Object=MibTable
h3cIfQoSAggregativeCarApplyTable=_H3cIfQoSAggregativeCarApplyTable_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,3))
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarApplyTable.setStatus(_A)
_H3cIfQoSAggregativeCarApplyEntry_Object=MibTableRow
h3cIfQoSAggregativeCarApplyEntry=_H3cIfQoSAggregativeCarApplyEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,3,1))
h3cIfQoSAggregativeCarApplyEntry.setIndexNames((0,_G,_H),(0,_E,_y),(0,_E,_z),(0,_E,_A0))
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarApplyEntry.setStatus(_A)
_H3cIfQoSAggregativeCarApplyDirection_Type=Direction
_H3cIfQoSAggregativeCarApplyDirection_Object=MibTableColumn
h3cIfQoSAggregativeCarApplyDirection=_H3cIfQoSAggregativeCarApplyDirection_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,3,1,1),_H3cIfQoSAggregativeCarApplyDirection_Type())
h3cIfQoSAggregativeCarApplyDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarApplyDirection.setStatus(_A)
class _H3cIfQoSAggregativeCarApplyRuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_M,2),('carl',3),(_Y,4)))
_H3cIfQoSAggregativeCarApplyRuleType_Type.__name__=_D
_H3cIfQoSAggregativeCarApplyRuleType_Object=MibTableColumn
h3cIfQoSAggregativeCarApplyRuleType=_H3cIfQoSAggregativeCarApplyRuleType_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,3,1,2),_H3cIfQoSAggregativeCarApplyRuleType_Type())
h3cIfQoSAggregativeCarApplyRuleType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarApplyRuleType.setStatus(_A)
class _H3cIfQoSAggregativeCarApplyRuleValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cIfQoSAggregativeCarApplyRuleValue_Type.__name__=_D
_H3cIfQoSAggregativeCarApplyRuleValue_Object=MibTableColumn
h3cIfQoSAggregativeCarApplyRuleValue=_H3cIfQoSAggregativeCarApplyRuleValue_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,3,1,3),_H3cIfQoSAggregativeCarApplyRuleValue_Type())
h3cIfQoSAggregativeCarApplyRuleValue.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarApplyRuleValue.setStatus(_A)
class _H3cIfQoSAggregativeCarApplyCarIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65534))
_H3cIfQoSAggregativeCarApplyCarIndex_Type.__name__=_D
_H3cIfQoSAggregativeCarApplyCarIndex_Object=MibTableColumn
h3cIfQoSAggregativeCarApplyCarIndex=_H3cIfQoSAggregativeCarApplyCarIndex_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,3,1,4),_H3cIfQoSAggregativeCarApplyCarIndex_Type())
h3cIfQoSAggregativeCarApplyCarIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarApplyCarIndex.setStatus(_A)
_H3cIfQoSAggregativeCarApplyRowStatus_Type=RowStatus
_H3cIfQoSAggregativeCarApplyRowStatus_Object=MibTableColumn
h3cIfQoSAggregativeCarApplyRowStatus=_H3cIfQoSAggregativeCarApplyRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,3,1,5),_H3cIfQoSAggregativeCarApplyRowStatus_Type())
h3cIfQoSAggregativeCarApplyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarApplyRowStatus.setStatus(_A)
_H3cIfQoSAggregativeCarRunInfoTable_Object=MibTable
h3cIfQoSAggregativeCarRunInfoTable=_H3cIfQoSAggregativeCarRunInfoTable_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,4))
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarRunInfoTable.setStatus(_A)
_H3cIfQoSAggregativeCarRunInfoEntry_Object=MibTableRow
h3cIfQoSAggregativeCarRunInfoEntry=_H3cIfQoSAggregativeCarRunInfoEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,4,1))
h3cIfQoSAggregativeCarRunInfoEntry.setIndexNames((0,_E,_X))
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarRunInfoEntry.setStatus(_A)
_H3cIfQoSAggregativeCarGreenPackets_Type=Counter64
_H3cIfQoSAggregativeCarGreenPackets_Object=MibTableColumn
h3cIfQoSAggregativeCarGreenPackets=_H3cIfQoSAggregativeCarGreenPackets_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,4,1,1),_H3cIfQoSAggregativeCarGreenPackets_Type())
h3cIfQoSAggregativeCarGreenPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarGreenPackets.setStatus(_A)
_H3cIfQoSAggregativeCarGreenBytes_Type=Counter64
_H3cIfQoSAggregativeCarGreenBytes_Object=MibTableColumn
h3cIfQoSAggregativeCarGreenBytes=_H3cIfQoSAggregativeCarGreenBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,4,1,2),_H3cIfQoSAggregativeCarGreenBytes_Type())
h3cIfQoSAggregativeCarGreenBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarGreenBytes.setStatus(_A)
_H3cIfQoSAggregativeCarYellowPackets_Type=Counter64
_H3cIfQoSAggregativeCarYellowPackets_Object=MibTableColumn
h3cIfQoSAggregativeCarYellowPackets=_H3cIfQoSAggregativeCarYellowPackets_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,4,1,3),_H3cIfQoSAggregativeCarYellowPackets_Type())
h3cIfQoSAggregativeCarYellowPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarYellowPackets.setStatus(_A)
_H3cIfQoSAggregativeCarYellowBytes_Type=Counter64
_H3cIfQoSAggregativeCarYellowBytes_Object=MibTableColumn
h3cIfQoSAggregativeCarYellowBytes=_H3cIfQoSAggregativeCarYellowBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,4,1,4),_H3cIfQoSAggregativeCarYellowBytes_Type())
h3cIfQoSAggregativeCarYellowBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarYellowBytes.setStatus(_A)
_H3cIfQoSAggregativeCarRedPackets_Type=Counter64
_H3cIfQoSAggregativeCarRedPackets_Object=MibTableColumn
h3cIfQoSAggregativeCarRedPackets=_H3cIfQoSAggregativeCarRedPackets_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,4,1,5),_H3cIfQoSAggregativeCarRedPackets_Type())
h3cIfQoSAggregativeCarRedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarRedPackets.setStatus(_A)
_H3cIfQoSAggregativeCarRedBytes_Type=Counter64
_H3cIfQoSAggregativeCarRedBytes_Object=MibTableColumn
h3cIfQoSAggregativeCarRedBytes=_H3cIfQoSAggregativeCarRedBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,4,1,4,1,6),_H3cIfQoSAggregativeCarRedBytes_Type())
h3cIfQoSAggregativeCarRedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSAggregativeCarRedBytes.setStatus(_A)
_H3cIfQoSTricolorCarGroup_ObjectIdentity=ObjectIdentity
h3cIfQoSTricolorCarGroup=_H3cIfQoSTricolorCarGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,4,2))
_H3cIfQoSTricolorCarConfigTable_Object=MibTable
h3cIfQoSTricolorCarConfigTable=_H3cIfQoSTricolorCarConfigTable_Object((1,3,6,1,4,1,2011,10,2,65,1,4,2,1))
if mibBuilder.loadTexts:h3cIfQoSTricolorCarConfigTable.setStatus(_A)
_H3cIfQoSTricolorCarConfigEntry_Object=MibTableRow
h3cIfQoSTricolorCarConfigEntry=_H3cIfQoSTricolorCarConfigEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,4,2,1,1))
h3cIfQoSTricolorCarConfigEntry.setIndexNames((0,_G,_H),(0,_E,_Z),(0,_E,_a),(0,_E,_b))
if mibBuilder.loadTexts:h3cIfQoSTricolorCarConfigEntry.setStatus(_A)
_H3cIfQoSTricolorCarDirection_Type=Direction
_H3cIfQoSTricolorCarDirection_Object=MibTableColumn
h3cIfQoSTricolorCarDirection=_H3cIfQoSTricolorCarDirection_Object((1,3,6,1,4,1,2011,10,2,65,1,4,2,1,1,1),_H3cIfQoSTricolorCarDirection_Type())
h3cIfQoSTricolorCarDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSTricolorCarDirection.setStatus(_A)
class _H3cIfQoSTricolorCarType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_M,2),('carl',3),(_Y,4)))
_H3cIfQoSTricolorCarType_Type.__name__=_D
_H3cIfQoSTricolorCarType_Object=MibTableColumn
h3cIfQoSTricolorCarType=_H3cIfQoSTricolorCarType_Object((1,3,6,1,4,1,2011,10,2,65,1,4,2,1,1,2),_H3cIfQoSTricolorCarType_Type())
h3cIfQoSTricolorCarType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSTricolorCarType.setStatus(_A)
class _H3cIfQoSTricolorCarValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cIfQoSTricolorCarValue_Type.__name__=_D
_H3cIfQoSTricolorCarValue_Object=MibTableColumn
h3cIfQoSTricolorCarValue=_H3cIfQoSTricolorCarValue_Object((1,3,6,1,4,1,2011,10,2,65,1,4,2,1,1,3),_H3cIfQoSTricolorCarValue_Type())
h3cIfQoSTricolorCarValue.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSTricolorCarValue.setStatus(_A)
_H3cIfQoSTricolorCarCir_Type=Unsigned32
_H3cIfQoSTricolorCarCir_Object=MibTableColumn
h3cIfQoSTricolorCarCir=_H3cIfQoSTricolorCarCir_Object((1,3,6,1,4,1,2011,10,2,65,1,4,2,1,1,4),_H3cIfQoSTricolorCarCir_Type())
h3cIfQoSTricolorCarCir.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSTricolorCarCir.setStatus(_A)
_H3cIfQoSTricolorCarCbs_Type=Unsigned32
_H3cIfQoSTricolorCarCbs_Object=MibTableColumn
h3cIfQoSTricolorCarCbs=_H3cIfQoSTricolorCarCbs_Object((1,3,6,1,4,1,2011,10,2,65,1,4,2,1,1,5),_H3cIfQoSTricolorCarCbs_Type())
h3cIfQoSTricolorCarCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSTricolorCarCbs.setStatus(_A)
_H3cIfQoSTricolorCarEbs_Type=Unsigned32
_H3cIfQoSTricolorCarEbs_Object=MibTableColumn
h3cIfQoSTricolorCarEbs=_H3cIfQoSTricolorCarEbs_Object((1,3,6,1,4,1,2011,10,2,65,1,4,2,1,1,6),_H3cIfQoSTricolorCarEbs_Type())
h3cIfQoSTricolorCarEbs.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSTricolorCarEbs.setStatus(_A)
class _H3cIfQoSTricolorCarPir_Type(Unsigned32):defaultValue=4294967295
_H3cIfQoSTricolorCarPir_Type.__name__=_I
_H3cIfQoSTricolorCarPir_Object=MibTableColumn
h3cIfQoSTricolorCarPir=_H3cIfQoSTricolorCarPir_Object((1,3,6,1,4,1,2011,10,2,65,1,4,2,1,1,7),_H3cIfQoSTricolorCarPir_Type())
h3cIfQoSTricolorCarPir.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSTricolorCarPir.setStatus(_A)
class _H3cIfQoSTricolorCarGreenActionType_Type(H3cIfCarAction):defaultValue=1
_H3cIfQoSTricolorCarGreenActionType_Type.__name__=_O
_H3cIfQoSTricolorCarGreenActionType_Object=MibTableColumn
h3cIfQoSTricolorCarGreenActionType=_H3cIfQoSTricolorCarGreenActionType_Object((1,3,6,1,4,1,2011,10,2,65,1,4,2,1,1,8),_H3cIfQoSTricolorCarGreenActionType_Type())
h3cIfQoSTricolorCarGreenActionType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSTricolorCarGreenActionType.setStatus(_A)
class _H3cIfQoSTricolorCarGreenActionValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_H3cIfQoSTricolorCarGreenActionValue_Type.__name__=_D
_H3cIfQoSTricolorCarGreenActionValue_Object=MibTableColumn
h3cIfQoSTricolorCarGreenActionValue=_H3cIfQoSTricolorCarGreenActionValue_Object((1,3,6,1,4,1,2011,10,2,65,1,4,2,1,1,9),_H3cIfQoSTricolorCarGreenActionValue_Type())
h3cIfQoSTricolorCarGreenActionValue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSTricolorCarGreenActionValue.setStatus(_A)
class _H3cIfQoSTricolorCarYellowActionType_Type(H3cIfCarAction):defaultValue=1
_H3cIfQoSTricolorCarYellowActionType_Type.__name__=_O
_H3cIfQoSTricolorCarYellowActionType_Object=MibTableColumn
h3cIfQoSTricolorCarYellowActionType=_H3cIfQoSTricolorCarYellowActionType_Object((1,3,6,1,4,1,2011,10,2,65,1,4,2,1,1,10),_H3cIfQoSTricolorCarYellowActionType_Type())
h3cIfQoSTricolorCarYellowActionType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSTricolorCarYellowActionType.setStatus(_A)
class _H3cIfQoSTricolorCarYellowActionValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_H3cIfQoSTricolorCarYellowActionValue_Type.__name__=_D
_H3cIfQoSTricolorCarYellowActionValue_Object=MibTableColumn
h3cIfQoSTricolorCarYellowActionValue=_H3cIfQoSTricolorCarYellowActionValue_Object((1,3,6,1,4,1,2011,10,2,65,1,4,2,1,1,11),_H3cIfQoSTricolorCarYellowActionValue_Type())
h3cIfQoSTricolorCarYellowActionValue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSTricolorCarYellowActionValue.setStatus(_A)
class _H3cIfQoSTricolorCarRedActionType_Type(H3cIfCarAction):defaultValue=3
_H3cIfQoSTricolorCarRedActionType_Type.__name__=_O
_H3cIfQoSTricolorCarRedActionType_Object=MibTableColumn
h3cIfQoSTricolorCarRedActionType=_H3cIfQoSTricolorCarRedActionType_Object((1,3,6,1,4,1,2011,10,2,65,1,4,2,1,1,12),_H3cIfQoSTricolorCarRedActionType_Type())
h3cIfQoSTricolorCarRedActionType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSTricolorCarRedActionType.setStatus(_A)
class _H3cIfQoSTricolorCarRedActionValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_H3cIfQoSTricolorCarRedActionValue_Type.__name__=_D
_H3cIfQoSTricolorCarRedActionValue_Object=MibTableColumn
h3cIfQoSTricolorCarRedActionValue=_H3cIfQoSTricolorCarRedActionValue_Object((1,3,6,1,4,1,2011,10,2,65,1,4,2,1,1,13),_H3cIfQoSTricolorCarRedActionValue_Type())
h3cIfQoSTricolorCarRedActionValue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSTricolorCarRedActionValue.setStatus(_A)
_H3cIfQoSTricolorCarRowStatus_Type=RowStatus
_H3cIfQoSTricolorCarRowStatus_Object=MibTableColumn
h3cIfQoSTricolorCarRowStatus=_H3cIfQoSTricolorCarRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,4,2,1,1,14),_H3cIfQoSTricolorCarRowStatus_Type())
h3cIfQoSTricolorCarRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSTricolorCarRowStatus.setStatus(_A)
class _H3cIfQoSTricolorCarUnitType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_W,2)))
_H3cIfQoSTricolorCarUnitType_Type.__name__=_D
_H3cIfQoSTricolorCarUnitType_Object=MibTableColumn
h3cIfQoSTricolorCarUnitType=_H3cIfQoSTricolorCarUnitType_Object((1,3,6,1,4,1,2011,10,2,65,1,4,2,1,1,15),_H3cIfQoSTricolorCarUnitType_Type())
h3cIfQoSTricolorCarUnitType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSTricolorCarUnitType.setStatus(_A)
_H3cIfQoSTricolorCarRunInfoTable_Object=MibTable
h3cIfQoSTricolorCarRunInfoTable=_H3cIfQoSTricolorCarRunInfoTable_Object((1,3,6,1,4,1,2011,10,2,65,1,4,2,2))
if mibBuilder.loadTexts:h3cIfQoSTricolorCarRunInfoTable.setStatus(_A)
_H3cIfQoSTricolorCarRunInfoEntry_Object=MibTableRow
h3cIfQoSTricolorCarRunInfoEntry=_H3cIfQoSTricolorCarRunInfoEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,4,2,2,1))
h3cIfQoSTricolorCarRunInfoEntry.setIndexNames((0,_G,_H),(0,_E,_Z),(0,_E,_a),(0,_E,_b))
if mibBuilder.loadTexts:h3cIfQoSTricolorCarRunInfoEntry.setStatus(_A)
_H3cIfQoSTricolorCarGreenPackets_Type=Counter64
_H3cIfQoSTricolorCarGreenPackets_Object=MibTableColumn
h3cIfQoSTricolorCarGreenPackets=_H3cIfQoSTricolorCarGreenPackets_Object((1,3,6,1,4,1,2011,10,2,65,1,4,2,2,1,1),_H3cIfQoSTricolorCarGreenPackets_Type())
h3cIfQoSTricolorCarGreenPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSTricolorCarGreenPackets.setStatus(_A)
_H3cIfQoSTricolorCarGreenBytes_Type=Counter64
_H3cIfQoSTricolorCarGreenBytes_Object=MibTableColumn
h3cIfQoSTricolorCarGreenBytes=_H3cIfQoSTricolorCarGreenBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,4,2,2,1,2),_H3cIfQoSTricolorCarGreenBytes_Type())
h3cIfQoSTricolorCarGreenBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSTricolorCarGreenBytes.setStatus(_A)
_H3cIfQoSTricolorCarYellowPackets_Type=Counter64
_H3cIfQoSTricolorCarYellowPackets_Object=MibTableColumn
h3cIfQoSTricolorCarYellowPackets=_H3cIfQoSTricolorCarYellowPackets_Object((1,3,6,1,4,1,2011,10,2,65,1,4,2,2,1,3),_H3cIfQoSTricolorCarYellowPackets_Type())
h3cIfQoSTricolorCarYellowPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSTricolorCarYellowPackets.setStatus(_A)
_H3cIfQoSTricolorCarYellowBytes_Type=Counter64
_H3cIfQoSTricolorCarYellowBytes_Object=MibTableColumn
h3cIfQoSTricolorCarYellowBytes=_H3cIfQoSTricolorCarYellowBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,4,2,2,1,4),_H3cIfQoSTricolorCarYellowBytes_Type())
h3cIfQoSTricolorCarYellowBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSTricolorCarYellowBytes.setStatus(_A)
_H3cIfQoSTricolorCarRedPackets_Type=Counter64
_H3cIfQoSTricolorCarRedPackets_Object=MibTableColumn
h3cIfQoSTricolorCarRedPackets=_H3cIfQoSTricolorCarRedPackets_Object((1,3,6,1,4,1,2011,10,2,65,1,4,2,2,1,5),_H3cIfQoSTricolorCarRedPackets_Type())
h3cIfQoSTricolorCarRedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSTricolorCarRedPackets.setStatus(_A)
_H3cIfQoSTricolorCarRedBytes_Type=Counter64
_H3cIfQoSTricolorCarRedBytes_Object=MibTableColumn
h3cIfQoSTricolorCarRedBytes=_H3cIfQoSTricolorCarRedBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,4,2,2,1,6),_H3cIfQoSTricolorCarRedBytes_Type())
h3cIfQoSTricolorCarRedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSTricolorCarRedBytes.setStatus(_A)
_H3cIfQoSGTSObjects_ObjectIdentity=ObjectIdentity
h3cIfQoSGTSObjects=_H3cIfQoSGTSObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,5))
_H3cIfQoSGTSConfigTable_Object=MibTable
h3cIfQoSGTSConfigTable=_H3cIfQoSGTSConfigTable_Object((1,3,6,1,4,1,2011,10,2,65,1,5,1))
if mibBuilder.loadTexts:h3cIfQoSGTSConfigTable.setStatus(_A)
_H3cIfQoSGTSConfigEntry_Object=MibTableRow
h3cIfQoSGTSConfigEntry=_H3cIfQoSGTSConfigEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,5,1,1))
h3cIfQoSGTSConfigEntry.setIndexNames((0,_G,_H),(0,_E,_c),(0,_E,_d))
if mibBuilder.loadTexts:h3cIfQoSGTSConfigEntry.setStatus(_A)
class _H3cIfQoSGTSClassRuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Y,1),(_L,2),(_M,3),(_e,4)))
_H3cIfQoSGTSClassRuleType_Type.__name__=_D
_H3cIfQoSGTSClassRuleType_Object=MibTableColumn
h3cIfQoSGTSClassRuleType=_H3cIfQoSGTSClassRuleType_Object((1,3,6,1,4,1,2011,10,2,65,1,5,1,1,1),_H3cIfQoSGTSClassRuleType_Type())
h3cIfQoSGTSClassRuleType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSGTSClassRuleType.setStatus(_A)
class _H3cIfQoSGTSClassRuleValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cIfQoSGTSClassRuleValue_Type.__name__=_D
_H3cIfQoSGTSClassRuleValue_Object=MibTableColumn
h3cIfQoSGTSClassRuleValue=_H3cIfQoSGTSClassRuleValue_Object((1,3,6,1,4,1,2011,10,2,65,1,5,1,1,2),_H3cIfQoSGTSClassRuleValue_Type())
h3cIfQoSGTSClassRuleValue.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSGTSClassRuleValue.setStatus(_A)
_H3cIfQoSGTSCir_Type=Unsigned32
_H3cIfQoSGTSCir_Object=MibTableColumn
h3cIfQoSGTSCir=_H3cIfQoSGTSCir_Object((1,3,6,1,4,1,2011,10,2,65,1,5,1,1,3),_H3cIfQoSGTSCir_Type())
h3cIfQoSGTSCir.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSGTSCir.setStatus(_A)
_H3cIfQoSGTSCbs_Type=Unsigned32
_H3cIfQoSGTSCbs_Object=MibTableColumn
h3cIfQoSGTSCbs=_H3cIfQoSGTSCbs_Object((1,3,6,1,4,1,2011,10,2,65,1,5,1,1,4),_H3cIfQoSGTSCbs_Type())
h3cIfQoSGTSCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSGTSCbs.setStatus(_A)
_H3cIfQoSGTSEbs_Type=Unsigned32
_H3cIfQoSGTSEbs_Object=MibTableColumn
h3cIfQoSGTSEbs=_H3cIfQoSGTSEbs_Object((1,3,6,1,4,1,2011,10,2,65,1,5,1,1,5),_H3cIfQoSGTSEbs_Type())
h3cIfQoSGTSEbs.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSGTSEbs.setStatus(_A)
_H3cIfQoSGTSQueueLength_Type=Integer32
_H3cIfQoSGTSQueueLength_Object=MibTableColumn
h3cIfQoSGTSQueueLength=_H3cIfQoSGTSQueueLength_Object((1,3,6,1,4,1,2011,10,2,65,1,5,1,1,6),_H3cIfQoSGTSQueueLength_Type())
h3cIfQoSGTSQueueLength.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSGTSQueueLength.setStatus(_A)
_H3cIfQoSGTSConfigRowStatus_Type=RowStatus
_H3cIfQoSGTSConfigRowStatus_Object=MibTableColumn
h3cIfQoSGTSConfigRowStatus=_H3cIfQoSGTSConfigRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,5,1,1,7),_H3cIfQoSGTSConfigRowStatus_Type())
h3cIfQoSGTSConfigRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSGTSConfigRowStatus.setStatus(_A)
class _H3cIfQoSGTSPir_Type(Unsigned32):defaultValue=4294967295
_H3cIfQoSGTSPir_Type.__name__=_I
_H3cIfQoSGTSPir_Object=MibTableColumn
h3cIfQoSGTSPir=_H3cIfQoSGTSPir_Object((1,3,6,1,4,1,2011,10,2,65,1,5,1,1,8),_H3cIfQoSGTSPir_Type())
h3cIfQoSGTSPir.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSGTSPir.setStatus(_A)
class _H3cIfQoSGTSUnitType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_W,2)))
_H3cIfQoSGTSUnitType_Type.__name__=_D
_H3cIfQoSGTSUnitType_Object=MibTableColumn
h3cIfQoSGTSUnitType=_H3cIfQoSGTSUnitType_Object((1,3,6,1,4,1,2011,10,2,65,1,5,1,1,9),_H3cIfQoSGTSUnitType_Type())
h3cIfQoSGTSUnitType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSGTSUnitType.setStatus(_A)
_H3cIfQoSGTSRunInfoTable_Object=MibTable
h3cIfQoSGTSRunInfoTable=_H3cIfQoSGTSRunInfoTable_Object((1,3,6,1,4,1,2011,10,2,65,1,5,2))
if mibBuilder.loadTexts:h3cIfQoSGTSRunInfoTable.setStatus(_A)
_H3cIfQoSGTSRunInfoEntry_Object=MibTableRow
h3cIfQoSGTSRunInfoEntry=_H3cIfQoSGTSRunInfoEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,5,2,1))
h3cIfQoSGTSRunInfoEntry.setIndexNames((0,_G,_H),(0,_E,_c),(0,_E,_d))
if mibBuilder.loadTexts:h3cIfQoSGTSRunInfoEntry.setStatus(_A)
_H3cIfQoSGTSQueueSize_Type=Integer32
_H3cIfQoSGTSQueueSize_Object=MibTableColumn
h3cIfQoSGTSQueueSize=_H3cIfQoSGTSQueueSize_Object((1,3,6,1,4,1,2011,10,2,65,1,5,2,1,1),_H3cIfQoSGTSQueueSize_Type())
h3cIfQoSGTSQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSGTSQueueSize.setStatus(_A)
_H3cIfQoSGTSPassedPackets_Type=Counter64
_H3cIfQoSGTSPassedPackets_Object=MibTableColumn
h3cIfQoSGTSPassedPackets=_H3cIfQoSGTSPassedPackets_Object((1,3,6,1,4,1,2011,10,2,65,1,5,2,1,2),_H3cIfQoSGTSPassedPackets_Type())
h3cIfQoSGTSPassedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSGTSPassedPackets.setStatus(_A)
_H3cIfQoSGTSPassedBytes_Type=Counter64
_H3cIfQoSGTSPassedBytes_Object=MibTableColumn
h3cIfQoSGTSPassedBytes=_H3cIfQoSGTSPassedBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,5,2,1,3),_H3cIfQoSGTSPassedBytes_Type())
h3cIfQoSGTSPassedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSGTSPassedBytes.setStatus(_A)
_H3cIfQoSGTSDiscardPackets_Type=Counter64
_H3cIfQoSGTSDiscardPackets_Object=MibTableColumn
h3cIfQoSGTSDiscardPackets=_H3cIfQoSGTSDiscardPackets_Object((1,3,6,1,4,1,2011,10,2,65,1,5,2,1,4),_H3cIfQoSGTSDiscardPackets_Type())
h3cIfQoSGTSDiscardPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSGTSDiscardPackets.setStatus(_A)
_H3cIfQoSGTSDiscardBytes_Type=Counter64
_H3cIfQoSGTSDiscardBytes_Object=MibTableColumn
h3cIfQoSGTSDiscardBytes=_H3cIfQoSGTSDiscardBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,5,2,1,5),_H3cIfQoSGTSDiscardBytes_Type())
h3cIfQoSGTSDiscardBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSGTSDiscardBytes.setStatus(_A)
_H3cIfQoSGTSDelayedPackets_Type=Counter64
_H3cIfQoSGTSDelayedPackets_Object=MibTableColumn
h3cIfQoSGTSDelayedPackets=_H3cIfQoSGTSDelayedPackets_Object((1,3,6,1,4,1,2011,10,2,65,1,5,2,1,6),_H3cIfQoSGTSDelayedPackets_Type())
h3cIfQoSGTSDelayedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSGTSDelayedPackets.setStatus(_A)
_H3cIfQoSGTSDelayedBytes_Type=Counter64
_H3cIfQoSGTSDelayedBytes_Object=MibTableColumn
h3cIfQoSGTSDelayedBytes=_H3cIfQoSGTSDelayedBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,5,2,1,7),_H3cIfQoSGTSDelayedBytes_Type())
h3cIfQoSGTSDelayedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSGTSDelayedBytes.setStatus(_A)
_H3cIfQoSWREDObjects_ObjectIdentity=ObjectIdentity
h3cIfQoSWREDObjects=_H3cIfQoSWREDObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,6))
_H3cIfQoSWredGroupGroup_ObjectIdentity=ObjectIdentity
h3cIfQoSWredGroupGroup=_H3cIfQoSWredGroupGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,6,1))
_H3cIfQoSWredGroupNextIndex_Type=Integer32
_H3cIfQoSWredGroupNextIndex_Object=MibScalar
h3cIfQoSWredGroupNextIndex=_H3cIfQoSWredGroupNextIndex_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,1),_H3cIfQoSWredGroupNextIndex_Type())
h3cIfQoSWredGroupNextIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWredGroupNextIndex.setStatus(_A)
_H3cIfQoSWredGroupTable_Object=MibTable
h3cIfQoSWredGroupTable=_H3cIfQoSWredGroupTable_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,2))
if mibBuilder.loadTexts:h3cIfQoSWredGroupTable.setStatus(_A)
_H3cIfQoSWredGroupEntry_Object=MibTableRow
h3cIfQoSWredGroupEntry=_H3cIfQoSWredGroupEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,2,1))
h3cIfQoSWredGroupEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:h3cIfQoSWredGroupEntry.setStatus(_A)
class _H3cIfQoSWredGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_H3cIfQoSWredGroupIndex_Type.__name__=_D
_H3cIfQoSWredGroupIndex_Object=MibTableColumn
h3cIfQoSWredGroupIndex=_H3cIfQoSWredGroupIndex_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,2,1,1),_H3cIfQoSWredGroupIndex_Type())
h3cIfQoSWredGroupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSWredGroupIndex.setStatus(_A)
class _H3cIfQoSWredGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cIfQoSWredGroupName_Type.__name__=_K
_H3cIfQoSWredGroupName_Object=MibTableColumn
h3cIfQoSWredGroupName=_H3cIfQoSWredGroupName_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,2,1,2),_H3cIfQoSWredGroupName_Type())
h3cIfQoSWredGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSWredGroupName.setStatus(_A)
class _H3cIfQoSWredGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_A1,0),(_f,1),('ippre',2),(_N,3),('localpre',4),('atmclp',5),('frde',6),('exp',7),(_e,8),('dropLevel',9)))
_H3cIfQoSWredGroupType_Type.__name__=_D
_H3cIfQoSWredGroupType_Object=MibTableColumn
h3cIfQoSWredGroupType=_H3cIfQoSWredGroupType_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,2,1,3),_H3cIfQoSWredGroupType_Type())
h3cIfQoSWredGroupType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSWredGroupType.setStatus(_A)
class _H3cIfQoSWredGroupWeightingConstant_Type(Integer32):defaultValue=9;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_H3cIfQoSWredGroupWeightingConstant_Type.__name__=_D
_H3cIfQoSWredGroupWeightingConstant_Object=MibTableColumn
h3cIfQoSWredGroupWeightingConstant=_H3cIfQoSWredGroupWeightingConstant_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,2,1,4),_H3cIfQoSWredGroupWeightingConstant_Type())
h3cIfQoSWredGroupWeightingConstant.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSWredGroupWeightingConstant.setStatus(_A)
_H3cIfQoSWredGroupRowStatus_Type=RowStatus
_H3cIfQoSWredGroupRowStatus_Object=MibTableColumn
h3cIfQoSWredGroupRowStatus=_H3cIfQoSWredGroupRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,2,1,6),_H3cIfQoSWredGroupRowStatus_Type())
h3cIfQoSWredGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSWredGroupRowStatus.setStatus(_A)
_H3cIfQoSWredGroupContentTable_Object=MibTable
h3cIfQoSWredGroupContentTable=_H3cIfQoSWredGroupContentTable_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,3))
if mibBuilder.loadTexts:h3cIfQoSWredGroupContentTable.setStatus(_A)
_H3cIfQoSWredGroupContentEntry_Object=MibTableRow
h3cIfQoSWredGroupContentEntry=_H3cIfQoSWredGroupContentEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,3,1))
h3cIfQoSWredGroupContentEntry.setIndexNames((0,_E,_S),(0,_E,_g),(0,_E,_h))
if mibBuilder.loadTexts:h3cIfQoSWredGroupContentEntry.setStatus(_A)
class _H3cIfQoSWredGroupContentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_H3cIfQoSWredGroupContentIndex_Type.__name__=_D
_H3cIfQoSWredGroupContentIndex_Object=MibTableColumn
h3cIfQoSWredGroupContentIndex=_H3cIfQoSWredGroupContentIndex_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,3,1,1),_H3cIfQoSWredGroupContentIndex_Type())
h3cIfQoSWredGroupContentIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSWredGroupContentIndex.setStatus(_A)
class _H3cIfQoSWredGroupContentSubIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_H3cIfQoSWredGroupContentSubIndex_Type.__name__=_D
_H3cIfQoSWredGroupContentSubIndex_Object=MibTableColumn
h3cIfQoSWredGroupContentSubIndex=_H3cIfQoSWredGroupContentSubIndex_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,3,1,2),_H3cIfQoSWredGroupContentSubIndex_Type())
h3cIfQoSWredGroupContentSubIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSWredGroupContentSubIndex.setStatus(_A)
_H3cIfQoSWredLowLimit_Type=Integer32
_H3cIfQoSWredLowLimit_Object=MibTableColumn
h3cIfQoSWredLowLimit=_H3cIfQoSWredLowLimit_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,3,1,3),_H3cIfQoSWredLowLimit_Type())
h3cIfQoSWredLowLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSWredLowLimit.setStatus(_A)
_H3cIfQoSWredHighLimit_Type=Integer32
_H3cIfQoSWredHighLimit_Object=MibTableColumn
h3cIfQoSWredHighLimit=_H3cIfQoSWredHighLimit_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,3,1,4),_H3cIfQoSWredHighLimit_Type())
h3cIfQoSWredHighLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSWredHighLimit.setStatus(_A)
_H3cIfQoSWredDiscardProb_Type=Integer32
_H3cIfQoSWredDiscardProb_Object=MibTableColumn
h3cIfQoSWredDiscardProb=_H3cIfQoSWredDiscardProb_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,3,1,5),_H3cIfQoSWredDiscardProb_Type())
h3cIfQoSWredDiscardProb.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSWredDiscardProb.setStatus(_A)
class _H3cIfQoSWredGroupExponent_Type(Integer32):defaultValue=9;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_H3cIfQoSWredGroupExponent_Type.__name__=_D
_H3cIfQoSWredGroupExponent_Object=MibTableColumn
h3cIfQoSWredGroupExponent=_H3cIfQoSWredGroupExponent_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,3,1,6),_H3cIfQoSWredGroupExponent_Type())
h3cIfQoSWredGroupExponent.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSWredGroupExponent.setStatus(_A)
_H3cIfQoSWredRowStatus_Type=RowStatus
_H3cIfQoSWredRowStatus_Object=MibTableColumn
h3cIfQoSWredRowStatus=_H3cIfQoSWredRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,3,1,7),_H3cIfQoSWredRowStatus_Type())
h3cIfQoSWredRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSWredRowStatus.setStatus(_A)
_H3cIfQoSWredGroupApplyIfTable_Object=MibTable
h3cIfQoSWredGroupApplyIfTable=_H3cIfQoSWredGroupApplyIfTable_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,4))
if mibBuilder.loadTexts:h3cIfQoSWredGroupApplyIfTable.setStatus(_A)
_H3cIfQoSWredGroupApplyIfEntry_Object=MibTableRow
h3cIfQoSWredGroupApplyIfEntry=_H3cIfQoSWredGroupApplyIfEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,4,1))
h3cIfQoSWredGroupApplyIfEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:h3cIfQoSWredGroupApplyIfEntry.setStatus(_A)
class _H3cIfQoSWredGroupApplyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_H3cIfQoSWredGroupApplyIndex_Type.__name__=_D
_H3cIfQoSWredGroupApplyIndex_Object=MibTableColumn
h3cIfQoSWredGroupApplyIndex=_H3cIfQoSWredGroupApplyIndex_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,4,1,1),_H3cIfQoSWredGroupApplyIndex_Type())
h3cIfQoSWredGroupApplyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSWredGroupApplyIndex.setStatus(_A)
class _H3cIfQoSWredGroupApplyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cIfQoSWredGroupApplyName_Type.__name__=_K
_H3cIfQoSWredGroupApplyName_Object=MibTableColumn
h3cIfQoSWredGroupApplyName=_H3cIfQoSWredGroupApplyName_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,4,1,2),_H3cIfQoSWredGroupApplyName_Type())
h3cIfQoSWredGroupApplyName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWredGroupApplyName.setStatus(_A)
_H3cIfQoSWredGroupIfRowStatus_Type=RowStatus
_H3cIfQoSWredGroupIfRowStatus_Object=MibTableColumn
h3cIfQoSWredGroupIfRowStatus=_H3cIfQoSWredGroupIfRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,4,1,3),_H3cIfQoSWredGroupIfRowStatus_Type())
h3cIfQoSWredGroupIfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSWredGroupIfRowStatus.setStatus(_A)
_H3cIfQoSWredApplyIfRunInfoTable_Object=MibTable
h3cIfQoSWredApplyIfRunInfoTable=_H3cIfQoSWredApplyIfRunInfoTable_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,5))
if mibBuilder.loadTexts:h3cIfQoSWredApplyIfRunInfoTable.setStatus(_A)
_H3cIfQoSWredApplyIfRunInfoEntry_Object=MibTableRow
h3cIfQoSWredApplyIfRunInfoEntry=_H3cIfQoSWredApplyIfRunInfoEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,5,1))
h3cIfQoSWredApplyIfRunInfoEntry.setIndexNames((0,_G,_H),(0,_E,_S),(0,_E,_g),(0,_E,_h))
if mibBuilder.loadTexts:h3cIfQoSWredApplyIfRunInfoEntry.setStatus(_A)
_H3cIfQoSWredPreRandomDropNum_Type=Counter64
_H3cIfQoSWredPreRandomDropNum_Object=MibTableColumn
h3cIfQoSWredPreRandomDropNum=_H3cIfQoSWredPreRandomDropNum_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,5,1,1),_H3cIfQoSWredPreRandomDropNum_Type())
h3cIfQoSWredPreRandomDropNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWredPreRandomDropNum.setStatus(_A)
_H3cIfQoSWredPreTailDropNum_Type=Counter64
_H3cIfQoSWredPreTailDropNum_Object=MibTableColumn
h3cIfQoSWredPreTailDropNum=_H3cIfQoSWredPreTailDropNum_Object((1,3,6,1,4,1,2011,10,2,65,1,6,1,5,1,2),_H3cIfQoSWredPreTailDropNum_Type())
h3cIfQoSWredPreTailDropNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWredPreTailDropNum.setStatus(_A)
_H3cIfQoSPortWredGroup_ObjectIdentity=ObjectIdentity
h3cIfQoSPortWredGroup=_H3cIfQoSPortWredGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,6,2))
_H3cIfQoSPortWredWeightConstantTable_Object=MibTable
h3cIfQoSPortWredWeightConstantTable=_H3cIfQoSPortWredWeightConstantTable_Object((1,3,6,1,4,1,2011,10,2,65,1,6,2,1))
if mibBuilder.loadTexts:h3cIfQoSPortWredWeightConstantTable.setStatus(_A)
_H3cIfQoSPortWredWeightConstantEntry_Object=MibTableRow
h3cIfQoSPortWredWeightConstantEntry=_H3cIfQoSPortWredWeightConstantEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,6,2,1,1))
h3cIfQoSPortWredWeightConstantEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:h3cIfQoSPortWredWeightConstantEntry.setStatus(_A)
_H3cIfQoSPortWredEnable_Type=TruthValue
_H3cIfQoSPortWredEnable_Object=MibTableColumn
h3cIfQoSPortWredEnable=_H3cIfQoSPortWredEnable_Object((1,3,6,1,4,1,2011,10,2,65,1,6,2,1,1,1),_H3cIfQoSPortWredEnable_Type())
h3cIfQoSPortWredEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSPortWredEnable.setStatus(_A)
class _H3cIfQoSPortWredWeightConstant_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_H3cIfQoSPortWredWeightConstant_Type.__name__=_D
_H3cIfQoSPortWredWeightConstant_Object=MibTableColumn
h3cIfQoSPortWredWeightConstant=_H3cIfQoSPortWredWeightConstant_Object((1,3,6,1,4,1,2011,10,2,65,1,6,2,1,1,2),_H3cIfQoSPortWredWeightConstant_Type())
h3cIfQoSPortWredWeightConstant.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSPortWredWeightConstant.setStatus(_A)
_H3cIfQoSPortWredWeightConstantRowStatus_Type=RowStatus
_H3cIfQoSPortWredWeightConstantRowStatus_Object=MibTableColumn
h3cIfQoSPortWredWeightConstantRowStatus=_H3cIfQoSPortWredWeightConstantRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,6,2,1,1,3),_H3cIfQoSPortWredWeightConstantRowStatus_Type())
h3cIfQoSPortWredWeightConstantRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSPortWredWeightConstantRowStatus.setStatus(_A)
_H3cIfQoSPortWredPreConfigTable_Object=MibTable
h3cIfQoSPortWredPreConfigTable=_H3cIfQoSPortWredPreConfigTable_Object((1,3,6,1,4,1,2011,10,2,65,1,6,2,2))
if mibBuilder.loadTexts:h3cIfQoSPortWredPreConfigTable.setStatus(_A)
_H3cIfQoSPortWredPreConfigEntry_Object=MibTableRow
h3cIfQoSPortWredPreConfigEntry=_H3cIfQoSPortWredPreConfigEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,6,2,2,1))
h3cIfQoSPortWredPreConfigEntry.setIndexNames((0,_G,_H),(0,_E,_i))
if mibBuilder.loadTexts:h3cIfQoSPortWredPreConfigEntry.setStatus(_A)
_H3cIfQoSPortWredPreID_Type=Integer32
_H3cIfQoSPortWredPreID_Object=MibTableColumn
h3cIfQoSPortWredPreID=_H3cIfQoSPortWredPreID_Object((1,3,6,1,4,1,2011,10,2,65,1,6,2,2,1,1),_H3cIfQoSPortWredPreID_Type())
h3cIfQoSPortWredPreID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSPortWredPreID.setStatus(_A)
_H3cIfQoSPortWredPreLowLimit_Type=Integer32
_H3cIfQoSPortWredPreLowLimit_Object=MibTableColumn
h3cIfQoSPortWredPreLowLimit=_H3cIfQoSPortWredPreLowLimit_Object((1,3,6,1,4,1,2011,10,2,65,1,6,2,2,1,2),_H3cIfQoSPortWredPreLowLimit_Type())
h3cIfQoSPortWredPreLowLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSPortWredPreLowLimit.setStatus(_A)
_H3cIfQoSPortWredPreHighLimit_Type=Integer32
_H3cIfQoSPortWredPreHighLimit_Object=MibTableColumn
h3cIfQoSPortWredPreHighLimit=_H3cIfQoSPortWredPreHighLimit_Object((1,3,6,1,4,1,2011,10,2,65,1,6,2,2,1,3),_H3cIfQoSPortWredPreHighLimit_Type())
h3cIfQoSPortWredPreHighLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSPortWredPreHighLimit.setStatus(_A)
_H3cIfQoSPortWredPreDiscardProbability_Type=Integer32
_H3cIfQoSPortWredPreDiscardProbability_Object=MibTableColumn
h3cIfQoSPortWredPreDiscardProbability=_H3cIfQoSPortWredPreDiscardProbability_Object((1,3,6,1,4,1,2011,10,2,65,1,6,2,2,1,4),_H3cIfQoSPortWredPreDiscardProbability_Type())
h3cIfQoSPortWredPreDiscardProbability.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSPortWredPreDiscardProbability.setStatus(_A)
_H3cIfQoSPortWredPreRowStatus_Type=RowStatus
_H3cIfQoSPortWredPreRowStatus_Object=MibTableColumn
h3cIfQoSPortWredPreRowStatus=_H3cIfQoSPortWredPreRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,6,2,2,1,5),_H3cIfQoSPortWredPreRowStatus_Type())
h3cIfQoSPortWredPreRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSPortWredPreRowStatus.setStatus(_A)
_H3cIfQoSPortWredRunInfoTable_Object=MibTable
h3cIfQoSPortWredRunInfoTable=_H3cIfQoSPortWredRunInfoTable_Object((1,3,6,1,4,1,2011,10,2,65,1,6,2,3))
if mibBuilder.loadTexts:h3cIfQoSPortWredRunInfoTable.setStatus(_A)
_H3cIfQoSPortWredRunInfoEntry_Object=MibTableRow
h3cIfQoSPortWredRunInfoEntry=_H3cIfQoSPortWredRunInfoEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,6,2,3,1))
h3cIfQoSPortWredRunInfoEntry.setIndexNames((0,_G,_H),(0,_E,_i))
if mibBuilder.loadTexts:h3cIfQoSPortWredRunInfoEntry.setStatus(_A)
_H3cIfQoSWREDTailDropNum_Type=Counter64
_H3cIfQoSWREDTailDropNum_Object=MibTableColumn
h3cIfQoSWREDTailDropNum=_H3cIfQoSWREDTailDropNum_Object((1,3,6,1,4,1,2011,10,2,65,1,6,2,3,1,1),_H3cIfQoSWREDTailDropNum_Type())
h3cIfQoSWREDTailDropNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWREDTailDropNum.setStatus(_A)
_H3cIfQoSWREDRandomDropNum_Type=Counter64
_H3cIfQoSWREDRandomDropNum_Object=MibTableColumn
h3cIfQoSWREDRandomDropNum=_H3cIfQoSWREDRandomDropNum_Object((1,3,6,1,4,1,2011,10,2,65,1,6,2,3,1,2),_H3cIfQoSWREDRandomDropNum_Type())
h3cIfQoSWREDRandomDropNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSWREDRandomDropNum.setStatus(_A)
_H3cIfQoSPortPriorityObjects_ObjectIdentity=ObjectIdentity
h3cIfQoSPortPriorityObjects=_H3cIfQoSPortPriorityObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,7))
_H3cIfQoSPortPriorityConfigGroup_ObjectIdentity=ObjectIdentity
h3cIfQoSPortPriorityConfigGroup=_H3cIfQoSPortPriorityConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,7,1))
_H3cIfQoSPortPriorityTable_Object=MibTable
h3cIfQoSPortPriorityTable=_H3cIfQoSPortPriorityTable_Object((1,3,6,1,4,1,2011,10,2,65,1,7,1,1))
if mibBuilder.loadTexts:h3cIfQoSPortPriorityTable.setStatus(_A)
_H3cIfQoSPortPriorityEntry_Object=MibTableRow
h3cIfQoSPortPriorityEntry=_H3cIfQoSPortPriorityEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,7,1,1,1))
h3cIfQoSPortPriorityEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:h3cIfQoSPortPriorityEntry.setStatus(_A)
class _H3cIfQoSPortPriorityValue_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_H3cIfQoSPortPriorityValue_Type.__name__=_D
_H3cIfQoSPortPriorityValue_Object=MibTableColumn
h3cIfQoSPortPriorityValue=_H3cIfQoSPortPriorityValue_Object((1,3,6,1,4,1,2011,10,2,65,1,7,1,1,1,1),_H3cIfQoSPortPriorityValue_Type())
h3cIfQoSPortPriorityValue.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cIfQoSPortPriorityValue.setStatus(_A)
_H3cIfQoSPortPirorityTrustTable_Object=MibTable
h3cIfQoSPortPirorityTrustTable=_H3cIfQoSPortPirorityTrustTable_Object((1,3,6,1,4,1,2011,10,2,65,1,7,1,2))
if mibBuilder.loadTexts:h3cIfQoSPortPirorityTrustTable.setStatus(_A)
_H3cIfQoSPortPirorityTrustEntry_Object=MibTableRow
h3cIfQoSPortPirorityTrustEntry=_H3cIfQoSPortPirorityTrustEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,7,1,2,1))
h3cIfQoSPortPirorityTrustEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:h3cIfQoSPortPirorityTrustEntry.setStatus(_A)
class _H3cIfQoSPortPriorityTrustTrustType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('untrust',1),(_f,2),(_N,3),('exp',4),(_A2,5),('dot11e',6),('auto',7)))
_H3cIfQoSPortPriorityTrustTrustType_Type.__name__=_D
_H3cIfQoSPortPriorityTrustTrustType_Object=MibTableColumn
h3cIfQoSPortPriorityTrustTrustType=_H3cIfQoSPortPriorityTrustTrustType_Object((1,3,6,1,4,1,2011,10,2,65,1,7,1,2,1,1),_H3cIfQoSPortPriorityTrustTrustType_Type())
h3cIfQoSPortPriorityTrustTrustType.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cIfQoSPortPriorityTrustTrustType.setStatus(_A)
class _H3cIfQoSPortPriorityTrustOvercastType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noOvercast',1),('overcastDSCP',2),('overcastCOS',3),('overcast',4)))
_H3cIfQoSPortPriorityTrustOvercastType_Type.__name__=_D
_H3cIfQoSPortPriorityTrustOvercastType_Object=MibTableColumn
h3cIfQoSPortPriorityTrustOvercastType=_H3cIfQoSPortPriorityTrustOvercastType_Object((1,3,6,1,4,1,2011,10,2,65,1,7,1,2,1,2),_H3cIfQoSPortPriorityTrustOvercastType_Type())
h3cIfQoSPortPriorityTrustOvercastType.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cIfQoSPortPriorityTrustOvercastType.setStatus(_A)
_H3cIfQoSMapObjects_ObjectIdentity=ObjectIdentity
h3cIfQoSMapObjects=_H3cIfQoSMapObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,9))
_H3cIfQoSPriMapConfigGroup_ObjectIdentity=ObjectIdentity
h3cIfQoSPriMapConfigGroup=_H3cIfQoSPriMapConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,9,1))
_H3cIfQoSPriMapGroupNextIndex_Type=Integer32
_H3cIfQoSPriMapGroupNextIndex_Object=MibScalar
h3cIfQoSPriMapGroupNextIndex=_H3cIfQoSPriMapGroupNextIndex_Object((1,3,6,1,4,1,2011,10,2,65,1,9,1,1),_H3cIfQoSPriMapGroupNextIndex_Type())
h3cIfQoSPriMapGroupNextIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSPriMapGroupNextIndex.setStatus(_A)
_H3cIfQoSPriMapGroupTable_Object=MibTable
h3cIfQoSPriMapGroupTable=_H3cIfQoSPriMapGroupTable_Object((1,3,6,1,4,1,2011,10,2,65,1,9,1,2))
if mibBuilder.loadTexts:h3cIfQoSPriMapGroupTable.setStatus(_A)
_H3cIfQoSPriMapGroupEntry_Object=MibTableRow
h3cIfQoSPriMapGroupEntry=_H3cIfQoSPriMapGroupEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,9,1,2,1))
h3cIfQoSPriMapGroupEntry.setIndexNames((0,_E,_j))
if mibBuilder.loadTexts:h3cIfQoSPriMapGroupEntry.setStatus(_A)
_H3cIfQoSPriMapGroupIndex_Type=Integer32
_H3cIfQoSPriMapGroupIndex_Object=MibTableColumn
h3cIfQoSPriMapGroupIndex=_H3cIfQoSPriMapGroupIndex_Object((1,3,6,1,4,1,2011,10,2,65,1,9,1,2,1,1),_H3cIfQoSPriMapGroupIndex_Type())
h3cIfQoSPriMapGroupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSPriMapGroupIndex.setStatus(_A)
class _H3cIfQoSPriMapGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_A1,1),('dot1p-dp',2),('dot1p-dscp',3),('dot1p-lp',4),('dscp-dot1p',5),('dscp-dp',6),('dscp-dscp',7),('dscp-lp',8),('exp-dp',9),('exp-lp',10)))
_H3cIfQoSPriMapGroupType_Type.__name__=_D
_H3cIfQoSPriMapGroupType_Object=MibTableColumn
h3cIfQoSPriMapGroupType=_H3cIfQoSPriMapGroupType_Object((1,3,6,1,4,1,2011,10,2,65,1,9,1,2,1,2),_H3cIfQoSPriMapGroupType_Type())
h3cIfQoSPriMapGroupType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSPriMapGroupType.setStatus(_A)
class _H3cIfQoSPriMapGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cIfQoSPriMapGroupName_Type.__name__=_K
_H3cIfQoSPriMapGroupName_Object=MibTableColumn
h3cIfQoSPriMapGroupName=_H3cIfQoSPriMapGroupName_Object((1,3,6,1,4,1,2011,10,2,65,1,9,1,2,1,3),_H3cIfQoSPriMapGroupName_Type())
h3cIfQoSPriMapGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSPriMapGroupName.setStatus(_A)
_H3cIfQoSPriMapGroupRowStatus_Type=RowStatus
_H3cIfQoSPriMapGroupRowStatus_Object=MibTableColumn
h3cIfQoSPriMapGroupRowStatus=_H3cIfQoSPriMapGroupRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,9,1,2,1,4),_H3cIfQoSPriMapGroupRowStatus_Type())
h3cIfQoSPriMapGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSPriMapGroupRowStatus.setStatus(_A)
_H3cIfQoSPriMapContentTable_Object=MibTable
h3cIfQoSPriMapContentTable=_H3cIfQoSPriMapContentTable_Object((1,3,6,1,4,1,2011,10,2,65,1,9,1,3))
if mibBuilder.loadTexts:h3cIfQoSPriMapContentTable.setStatus(_A)
_H3cIfQoSPriMapContentEntry_Object=MibTableRow
h3cIfQoSPriMapContentEntry=_H3cIfQoSPriMapContentEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,9,1,3,1))
h3cIfQoSPriMapContentEntry.setIndexNames((0,_E,_j),(0,_E,_A3))
if mibBuilder.loadTexts:h3cIfQoSPriMapContentEntry.setStatus(_A)
class _H3cIfQoSPriMapGroupImportValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_H3cIfQoSPriMapGroupImportValue_Type.__name__=_D
_H3cIfQoSPriMapGroupImportValue_Object=MibTableColumn
h3cIfQoSPriMapGroupImportValue=_H3cIfQoSPriMapGroupImportValue_Object((1,3,6,1,4,1,2011,10,2,65,1,9,1,3,1,1),_H3cIfQoSPriMapGroupImportValue_Type())
h3cIfQoSPriMapGroupImportValue.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSPriMapGroupImportValue.setStatus(_A)
class _H3cIfQoSPriMapGroupExportValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_H3cIfQoSPriMapGroupExportValue_Type.__name__=_D
_H3cIfQoSPriMapGroupExportValue_Object=MibTableColumn
h3cIfQoSPriMapGroupExportValue=_H3cIfQoSPriMapGroupExportValue_Object((1,3,6,1,4,1,2011,10,2,65,1,9,1,3,1,2),_H3cIfQoSPriMapGroupExportValue_Type())
h3cIfQoSPriMapGroupExportValue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSPriMapGroupExportValue.setStatus(_A)
_H3cIfQoSPriMapContentRowStatus_Type=RowStatus
_H3cIfQoSPriMapContentRowStatus_Object=MibTableColumn
h3cIfQoSPriMapContentRowStatus=_H3cIfQoSPriMapContentRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,9,1,3,1,3),_H3cIfQoSPriMapContentRowStatus_Type())
h3cIfQoSPriMapContentRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSPriMapContentRowStatus.setStatus(_A)
_H3cIfQoSPrePriMapTable_Object=MibTable
h3cIfQoSPrePriMapTable=_H3cIfQoSPrePriMapTable_Object((1,3,6,1,4,1,2011,10,2,65,1,9,1,4))
if mibBuilder.loadTexts:h3cIfQoSPrePriMapTable.setStatus(_A)
_H3cIfQoSPrePriMapEntry_Object=MibTableRow
h3cIfQoSPrePriMapEntry=_H3cIfQoSPrePriMapEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,9,1,4,1))
h3cIfQoSPrePriMapEntry.setIndexNames((0,_E,_A4),(0,_E,_A5),(0,_E,_A6),(0,_E,_A7))
if mibBuilder.loadTexts:h3cIfQoSPrePriMapEntry.setStatus(_A)
class _H3cIfQoSPrePriMapTableType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34)));namedValues=NamedValues(*(('dot1pToLp',1),('dot1pToDp',2),('expToLp',3),('dscpToLp',4),('expToDp',5),('dscpToDp',6),('dscpToDot1p',7),('dot1pToDscp',8),('dscpToDscp',9),('dscpToExp',10),('expToDscp',11),('expToDot1p',12),('expToExp',13),('lpToDot1p',14),('dot1pToRpr',15),('dscpToRpr',16),('expToRpr',17),('ippreToRpr',18),('upToDot1p',19),('upToDscp',20),('upToExp',21),('upToDp',22),('upToLp',23),('upToRpr',24),('upToFc',25),('lpTodscp',26),('dot11eToLp',27),('lpToDot11e',28),('lpToLp',29),('dot1pToExp',30),('lpToExp',31),('lpToDp',32),('upToUp',33),('dot1pToDot1p',34)))
_H3cIfQoSPrePriMapTableType_Type.__name__=_D
_H3cIfQoSPrePriMapTableType_Object=MibTableColumn
h3cIfQoSPrePriMapTableType=_H3cIfQoSPrePriMapTableType_Object((1,3,6,1,4,1,2011,10,2,65,1,9,1,4,1,1),_H3cIfQoSPrePriMapTableType_Type())
h3cIfQoSPrePriMapTableType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSPrePriMapTableType.setStatus(_A)
class _H3cIfQoSPrePriMapTableColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noColor',1),('green',2),('yellow',3),('red',4)))
_H3cIfQoSPrePriMapTableColor_Type.__name__=_D
_H3cIfQoSPrePriMapTableColor_Object=MibTableColumn
h3cIfQoSPrePriMapTableColor=_H3cIfQoSPrePriMapTableColor_Object((1,3,6,1,4,1,2011,10,2,65,1,9,1,4,1,2),_H3cIfQoSPrePriMapTableColor_Type())
h3cIfQoSPrePriMapTableColor.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSPrePriMapTableColor.setStatus(_A)
class _H3cIfQoSPrePriMapTableDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noDirection',1),(_l,2),(_m,3)))
_H3cIfQoSPrePriMapTableDirection_Type.__name__=_D
_H3cIfQoSPrePriMapTableDirection_Object=MibTableColumn
h3cIfQoSPrePriMapTableDirection=_H3cIfQoSPrePriMapTableDirection_Object((1,3,6,1,4,1,2011,10,2,65,1,9,1,4,1,3),_H3cIfQoSPrePriMapTableDirection_Type())
h3cIfQoSPrePriMapTableDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSPrePriMapTableDirection.setStatus(_A)
class _H3cIfQoSPrePriMapTableImportValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_H3cIfQoSPrePriMapTableImportValue_Type.__name__=_D
_H3cIfQoSPrePriMapTableImportValue_Object=MibTableColumn
h3cIfQoSPrePriMapTableImportValue=_H3cIfQoSPrePriMapTableImportValue_Object((1,3,6,1,4,1,2011,10,2,65,1,9,1,4,1,4),_H3cIfQoSPrePriMapTableImportValue_Type())
h3cIfQoSPrePriMapTableImportValue.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSPrePriMapTableImportValue.setStatus(_A)
class _H3cIfQoSPrePriMapTableExportValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_H3cIfQoSPrePriMapTableExportValue_Type.__name__=_D
_H3cIfQoSPrePriMapTableExportValue_Object=MibTableColumn
h3cIfQoSPrePriMapTableExportValue=_H3cIfQoSPrePriMapTableExportValue_Object((1,3,6,1,4,1,2011,10,2,65,1,9,1,4,1,5),_H3cIfQoSPrePriMapTableExportValue_Type())
h3cIfQoSPrePriMapTableExportValue.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cIfQoSPrePriMapTableExportValue.setStatus(_A)
_H3cIfQoSL3PlusObjects_ObjectIdentity=ObjectIdentity
h3cIfQoSL3PlusObjects=_H3cIfQoSL3PlusObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,10))
_H3cIfQoSPortBindingGroup_ObjectIdentity=ObjectIdentity
h3cIfQoSPortBindingGroup=_H3cIfQoSPortBindingGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,10,1))
_H3cIfQoSPortBindingTable_Object=MibTable
h3cIfQoSPortBindingTable=_H3cIfQoSPortBindingTable_Object((1,3,6,1,4,1,2011,10,2,65,1,10,1,1))
if mibBuilder.loadTexts:h3cIfQoSPortBindingTable.setStatus(_A)
_H3cIfQoSPortBindingEntry_Object=MibTableRow
h3cIfQoSPortBindingEntry=_H3cIfQoSPortBindingEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,10,1,1,1))
h3cIfQoSPortBindingEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:h3cIfQoSPortBindingEntry.setStatus(_A)
_H3cIfQoSBindingIf_Type=Integer32
_H3cIfQoSBindingIf_Object=MibTableColumn
h3cIfQoSBindingIf=_H3cIfQoSBindingIf_Object((1,3,6,1,4,1,2011,10,2,65,1,10,1,1,1,1),_H3cIfQoSBindingIf_Type())
h3cIfQoSBindingIf.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSBindingIf.setStatus(_A)
_H3cIfQoSBindingRowStatus_Type=RowStatus
_H3cIfQoSBindingRowStatus_Object=MibTableColumn
h3cIfQoSBindingRowStatus=_H3cIfQoSBindingRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,10,1,1,1,2),_H3cIfQoSBindingRowStatus_Type())
h3cIfQoSBindingRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIfQoSBindingRowStatus.setStatus(_A)
_H3cQoSTraStaObjects_ObjectIdentity=ObjectIdentity
h3cQoSTraStaObjects=_H3cQoSTraStaObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,11))
_H3cQoSTraStaConfigGroup_ObjectIdentity=ObjectIdentity
h3cQoSTraStaConfigGroup=_H3cQoSTraStaConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,11,1))
_H3cQoSIfTraStaConfigInfoTable_Object=MibTable
h3cQoSIfTraStaConfigInfoTable=_H3cQoSIfTraStaConfigInfoTable_Object((1,3,6,1,4,1,2011,10,2,65,1,11,1,1))
if mibBuilder.loadTexts:h3cQoSIfTraStaConfigInfoTable.setStatus(_A)
_H3cQoSIfTraStaConfigInfoEntry_Object=MibTableRow
h3cQoSIfTraStaConfigInfoEntry=_H3cQoSIfTraStaConfigInfoEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,11,1,1,1))
h3cQoSIfTraStaConfigInfoEntry.setIndexNames((0,_G,_H),(0,_E,_A8))
if mibBuilder.loadTexts:h3cQoSIfTraStaConfigInfoEntry.setStatus(_A)
_H3cQoSIfTraStaConfigDirection_Type=Direction
_H3cQoSIfTraStaConfigDirection_Object=MibTableColumn
h3cQoSIfTraStaConfigDirection=_H3cQoSIfTraStaConfigDirection_Object((1,3,6,1,4,1,2011,10,2,65,1,11,1,1,1,1),_H3cQoSIfTraStaConfigDirection_Type())
h3cQoSIfTraStaConfigDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cQoSIfTraStaConfigDirection.setStatus(_A)
class _H3cQoSIfTraStaConfigQueue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_H3cQoSIfTraStaConfigQueue_Type.__name__=_K
_H3cQoSIfTraStaConfigQueue_Object=MibTableColumn
h3cQoSIfTraStaConfigQueue=_H3cQoSIfTraStaConfigQueue_Object((1,3,6,1,4,1,2011,10,2,65,1,11,1,1,1,2),_H3cQoSIfTraStaConfigQueue_Type())
h3cQoSIfTraStaConfigQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSIfTraStaConfigQueue.setStatus(_A)
class _H3cQoSIfTraStaConfigDot1p_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_H3cQoSIfTraStaConfigDot1p_Type.__name__=_K
_H3cQoSIfTraStaConfigDot1p_Object=MibTableColumn
h3cQoSIfTraStaConfigDot1p=_H3cQoSIfTraStaConfigDot1p_Object((1,3,6,1,4,1,2011,10,2,65,1,11,1,1,1,3),_H3cQoSIfTraStaConfigDot1p_Type())
h3cQoSIfTraStaConfigDot1p.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSIfTraStaConfigDot1p.setStatus(_A)
class _H3cQoSIfTraStaConfigDscp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_H3cQoSIfTraStaConfigDscp_Type.__name__=_K
_H3cQoSIfTraStaConfigDscp_Object=MibTableColumn
h3cQoSIfTraStaConfigDscp=_H3cQoSIfTraStaConfigDscp_Object((1,3,6,1,4,1,2011,10,2,65,1,11,1,1,1,4),_H3cQoSIfTraStaConfigDscp_Type())
h3cQoSIfTraStaConfigDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSIfTraStaConfigDscp.setStatus(_A)
class _H3cQoSIfTraStaConfigVlan_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_H3cQoSIfTraStaConfigVlan_Type.__name__=_K
_H3cQoSIfTraStaConfigVlan_Object=MibTableColumn
h3cQoSIfTraStaConfigVlan=_H3cQoSIfTraStaConfigVlan_Object((1,3,6,1,4,1,2011,10,2,65,1,11,1,1,1,5),_H3cQoSIfTraStaConfigVlan_Type())
h3cQoSIfTraStaConfigVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSIfTraStaConfigVlan.setStatus(_A)
_H3cQoSIfTraStaConfigStatus_Type=RowStatus
_H3cQoSIfTraStaConfigStatus_Object=MibTableColumn
h3cQoSIfTraStaConfigStatus=_H3cQoSIfTraStaConfigStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,11,1,1,1,6),_H3cQoSIfTraStaConfigStatus_Type())
h3cQoSIfTraStaConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSIfTraStaConfigStatus.setStatus(_A)
_H3cQoSTraStaRunGroup_ObjectIdentity=ObjectIdentity
h3cQoSTraStaRunGroup=_H3cQoSTraStaRunGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,11,2))
_H3cQoSIfTraStaRunInfoTable_Object=MibTable
h3cQoSIfTraStaRunInfoTable=_H3cQoSIfTraStaRunInfoTable_Object((1,3,6,1,4,1,2011,10,2,65,1,11,2,1))
if mibBuilder.loadTexts:h3cQoSIfTraStaRunInfoTable.setStatus(_A)
_H3cQoSIfTraStaRunInfoEntry_Object=MibTableRow
h3cQoSIfTraStaRunInfoEntry=_H3cQoSIfTraStaRunInfoEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,11,2,1,1))
h3cQoSIfTraStaRunInfoEntry.setIndexNames((0,_G,_H),(0,_E,_A9),(0,_E,_AA),(0,_E,_AB))
if mibBuilder.loadTexts:h3cQoSIfTraStaRunInfoEntry.setStatus(_A)
class _H3cQoSIfTraStaRunObjectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_e,1),(_f,2),(_N,3),('vlanID',4)))
_H3cQoSIfTraStaRunObjectType_Type.__name__=_D
_H3cQoSIfTraStaRunObjectType_Object=MibTableColumn
h3cQoSIfTraStaRunObjectType=_H3cQoSIfTraStaRunObjectType_Object((1,3,6,1,4,1,2011,10,2,65,1,11,2,1,1,1),_H3cQoSIfTraStaRunObjectType_Type())
h3cQoSIfTraStaRunObjectType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cQoSIfTraStaRunObjectType.setStatus(_A)
_H3cQoSIfTraStaRunObjectValue_Type=Integer32
_H3cQoSIfTraStaRunObjectValue_Object=MibTableColumn
h3cQoSIfTraStaRunObjectValue=_H3cQoSIfTraStaRunObjectValue_Object((1,3,6,1,4,1,2011,10,2,65,1,11,2,1,1,2),_H3cQoSIfTraStaRunObjectValue_Type())
h3cQoSIfTraStaRunObjectValue.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cQoSIfTraStaRunObjectValue.setStatus(_A)
_H3cQoSIfTraStaRunDirection_Type=Direction
_H3cQoSIfTraStaRunDirection_Object=MibTableColumn
h3cQoSIfTraStaRunDirection=_H3cQoSIfTraStaRunDirection_Object((1,3,6,1,4,1,2011,10,2,65,1,11,2,1,1,3),_H3cQoSIfTraStaRunDirection_Type())
h3cQoSIfTraStaRunDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cQoSIfTraStaRunDirection.setStatus(_A)
_H3cQoSIfTraStaRunPassPackets_Type=Counter64
_H3cQoSIfTraStaRunPassPackets_Object=MibTableColumn
h3cQoSIfTraStaRunPassPackets=_H3cQoSIfTraStaRunPassPackets_Object((1,3,6,1,4,1,2011,10,2,65,1,11,2,1,1,4),_H3cQoSIfTraStaRunPassPackets_Type())
h3cQoSIfTraStaRunPassPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cQoSIfTraStaRunPassPackets.setStatus(_A)
_H3cQoSIfTraStaRunDropPackets_Type=Counter64
_H3cQoSIfTraStaRunDropPackets_Object=MibTableColumn
h3cQoSIfTraStaRunDropPackets=_H3cQoSIfTraStaRunDropPackets_Object((1,3,6,1,4,1,2011,10,2,65,1,11,2,1,1,5),_H3cQoSIfTraStaRunDropPackets_Type())
h3cQoSIfTraStaRunDropPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cQoSIfTraStaRunDropPackets.setStatus(_A)
_H3cQoSIfTraStaRunPassBytes_Type=Counter64
_H3cQoSIfTraStaRunPassBytes_Object=MibTableColumn
h3cQoSIfTraStaRunPassBytes=_H3cQoSIfTraStaRunPassBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,11,2,1,1,6),_H3cQoSIfTraStaRunPassBytes_Type())
h3cQoSIfTraStaRunPassBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cQoSIfTraStaRunPassBytes.setStatus(_A)
_H3cQoSIfTraStaRunDropBytes_Type=Counter64
_H3cQoSIfTraStaRunDropBytes_Object=MibTableColumn
h3cQoSIfTraStaRunDropBytes=_H3cQoSIfTraStaRunDropBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,11,2,1,1,7),_H3cQoSIfTraStaRunDropBytes_Type())
h3cQoSIfTraStaRunDropBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cQoSIfTraStaRunDropBytes.setStatus(_A)
_H3cQoSIfTraStaRunPassPPS_Type=Counter64
_H3cQoSIfTraStaRunPassPPS_Object=MibTableColumn
h3cQoSIfTraStaRunPassPPS=_H3cQoSIfTraStaRunPassPPS_Object((1,3,6,1,4,1,2011,10,2,65,1,11,2,1,1,8),_H3cQoSIfTraStaRunPassPPS_Type())
h3cQoSIfTraStaRunPassPPS.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cQoSIfTraStaRunPassPPS.setStatus(_A)
_H3cQoSIfTraStaRunPassBPS_Type=Counter64
_H3cQoSIfTraStaRunPassBPS_Object=MibTableColumn
h3cQoSIfTraStaRunPassBPS=_H3cQoSIfTraStaRunPassBPS_Object((1,3,6,1,4,1,2011,10,2,65,1,11,2,1,1,9),_H3cQoSIfTraStaRunPassBPS_Type())
h3cQoSIfTraStaRunPassBPS.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cQoSIfTraStaRunPassBPS.setStatus(_A)
_H3cQoSGlobalPriorityObject_ObjectIdentity=ObjectIdentity
h3cQoSGlobalPriorityObject=_H3cQoSGlobalPriorityObject_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,12))
_H3cQoSRemarkTcpPortPriTable_Object=MibTable
h3cQoSRemarkTcpPortPriTable=_H3cQoSRemarkTcpPortPriTable_Object((1,3,6,1,4,1,2011,10,2,65,1,12,1))
if mibBuilder.loadTexts:h3cQoSRemarkTcpPortPriTable.setStatus(_A)
_H3cQoSRemarkTcpPortPriEntry_Object=MibTableRow
h3cQoSRemarkTcpPortPriEntry=_H3cQoSRemarkTcpPortPriEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,12,1,1))
h3cQoSRemarkTcpPortPriEntry.setIndexNames((0,_E,_AC))
if mibBuilder.loadTexts:h3cQoSRemarkTcpPortPriEntry.setStatus(_A)
class _H3cQoSRemarkTcpPortStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cQoSRemarkTcpPortStart_Type.__name__=_D
_H3cQoSRemarkTcpPortStart_Object=MibTableColumn
h3cQoSRemarkTcpPortStart=_H3cQoSRemarkTcpPortStart_Object((1,3,6,1,4,1,2011,10,2,65,1,12,1,1,1),_H3cQoSRemarkTcpPortStart_Type())
h3cQoSRemarkTcpPortStart.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cQoSRemarkTcpPortStart.setStatus(_A)
class _H3cQoSRemarkTcpPortEnd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cQoSRemarkTcpPortEnd_Type.__name__=_D
_H3cQoSRemarkTcpPortEnd_Object=MibTableColumn
h3cQoSRemarkTcpPortEnd=_H3cQoSRemarkTcpPortEnd_Object((1,3,6,1,4,1,2011,10,2,65,1,12,1,1,2),_H3cQoSRemarkTcpPortEnd_Type())
h3cQoSRemarkTcpPortEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSRemarkTcpPortEnd.setStatus(_A)
class _H3cQoSRemarkTcpPortType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ipAll',1),('ipv4',2),('ipv6',3)))
_H3cQoSRemarkTcpPortType_Type.__name__=_D
_H3cQoSRemarkTcpPortType_Object=MibTableColumn
h3cQoSRemarkTcpPortType=_H3cQoSRemarkTcpPortType_Object((1,3,6,1,4,1,2011,10,2,65,1,12,1,1,3),_H3cQoSRemarkTcpPortType_Type())
h3cQoSRemarkTcpPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSRemarkTcpPortType.setStatus(_A)
class _H3cQoSRemarkTcpPortDot1p_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_H3cQoSRemarkTcpPortDot1p_Type.__name__=_I
_H3cQoSRemarkTcpPortDot1p_Object=MibTableColumn
h3cQoSRemarkTcpPortDot1p=_H3cQoSRemarkTcpPortDot1p_Object((1,3,6,1,4,1,2011,10,2,65,1,12,1,1,4),_H3cQoSRemarkTcpPortDot1p_Type())
h3cQoSRemarkTcpPortDot1p.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSRemarkTcpPortDot1p.setStatus(_A)
class _H3cQoSRemarkTcpPortDscp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_H3cQoSRemarkTcpPortDscp_Type.__name__=_I
_H3cQoSRemarkTcpPortDscp_Object=MibTableColumn
h3cQoSRemarkTcpPortDscp=_H3cQoSRemarkTcpPortDscp_Object((1,3,6,1,4,1,2011,10,2,65,1,12,1,1,5),_H3cQoSRemarkTcpPortDscp_Type())
h3cQoSRemarkTcpPortDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSRemarkTcpPortDscp.setStatus(_A)
_H3cQoSRemarkTcpPortRowStatus_Type=RowStatus
_H3cQoSRemarkTcpPortRowStatus_Object=MibTableColumn
h3cQoSRemarkTcpPortRowStatus=_H3cQoSRemarkTcpPortRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,12,1,1,6),_H3cQoSRemarkTcpPortRowStatus_Type())
h3cQoSRemarkTcpPortRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSRemarkTcpPortRowStatus.setStatus(_A)
_H3cQoSRemarkUdpPortPriTable_Object=MibTable
h3cQoSRemarkUdpPortPriTable=_H3cQoSRemarkUdpPortPriTable_Object((1,3,6,1,4,1,2011,10,2,65,1,12,2))
if mibBuilder.loadTexts:h3cQoSRemarkUdpPortPriTable.setStatus(_A)
_H3cQoSRemarkUdpPortPriEntry_Object=MibTableRow
h3cQoSRemarkUdpPortPriEntry=_H3cQoSRemarkUdpPortPriEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,12,2,1))
h3cQoSRemarkUdpPortPriEntry.setIndexNames((0,_E,_AD))
if mibBuilder.loadTexts:h3cQoSRemarkUdpPortPriEntry.setStatus(_A)
class _H3cQoSRemarkUdpPortStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cQoSRemarkUdpPortStart_Type.__name__=_D
_H3cQoSRemarkUdpPortStart_Object=MibTableColumn
h3cQoSRemarkUdpPortStart=_H3cQoSRemarkUdpPortStart_Object((1,3,6,1,4,1,2011,10,2,65,1,12,2,1,1),_H3cQoSRemarkUdpPortStart_Type())
h3cQoSRemarkUdpPortStart.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cQoSRemarkUdpPortStart.setStatus(_A)
class _H3cQoSRemarkUdpPortEnd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cQoSRemarkUdpPortEnd_Type.__name__=_D
_H3cQoSRemarkUdpPortEnd_Object=MibTableColumn
h3cQoSRemarkUdpPortEnd=_H3cQoSRemarkUdpPortEnd_Object((1,3,6,1,4,1,2011,10,2,65,1,12,2,1,2),_H3cQoSRemarkUdpPortEnd_Type())
h3cQoSRemarkUdpPortEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSRemarkUdpPortEnd.setStatus(_A)
class _H3cQoSRemarkUdpPortType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ipAll',1),('ipv4',2),('ipv6',3)))
_H3cQoSRemarkUdpPortType_Type.__name__=_D
_H3cQoSRemarkUdpPortType_Object=MibTableColumn
h3cQoSRemarkUdpPortType=_H3cQoSRemarkUdpPortType_Object((1,3,6,1,4,1,2011,10,2,65,1,12,2,1,3),_H3cQoSRemarkUdpPortType_Type())
h3cQoSRemarkUdpPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSRemarkUdpPortType.setStatus(_A)
class _H3cQoSRemarkUdpPortDot1p_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_H3cQoSRemarkUdpPortDot1p_Type.__name__=_I
_H3cQoSRemarkUdpPortDot1p_Object=MibTableColumn
h3cQoSRemarkUdpPortDot1p=_H3cQoSRemarkUdpPortDot1p_Object((1,3,6,1,4,1,2011,10,2,65,1,12,2,1,4),_H3cQoSRemarkUdpPortDot1p_Type())
h3cQoSRemarkUdpPortDot1p.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSRemarkUdpPortDot1p.setStatus(_A)
class _H3cQoSRemarkUdpPortDscp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_H3cQoSRemarkUdpPortDscp_Type.__name__=_I
_H3cQoSRemarkUdpPortDscp_Object=MibTableColumn
h3cQoSRemarkUdpPortDscp=_H3cQoSRemarkUdpPortDscp_Object((1,3,6,1,4,1,2011,10,2,65,1,12,2,1,5),_H3cQoSRemarkUdpPortDscp_Type())
h3cQoSRemarkUdpPortDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSRemarkUdpPortDscp.setStatus(_A)
_H3cQoSRemarkUdpPortRowStatus_Type=RowStatus
_H3cQoSRemarkUdpPortRowStatus_Object=MibTableColumn
h3cQoSRemarkUdpPortRowStatus=_H3cQoSRemarkUdpPortRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,12,2,1,6),_H3cQoSRemarkUdpPortRowStatus_Type())
h3cQoSRemarkUdpPortRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSRemarkUdpPortRowStatus.setStatus(_A)
_H3cQoSRemarkIPv4AddrPriTable_Object=MibTable
h3cQoSRemarkIPv4AddrPriTable=_H3cQoSRemarkIPv4AddrPriTable_Object((1,3,6,1,4,1,2011,10,2,65,1,12,3))
if mibBuilder.loadTexts:h3cQoSRemarkIPv4AddrPriTable.setStatus(_A)
_H3cQoSRemarkIPv4AddrPriEntry_Object=MibTableRow
h3cQoSRemarkIPv4AddrPriEntry=_H3cQoSRemarkIPv4AddrPriEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,12,3,1))
h3cQoSRemarkIPv4AddrPriEntry.setIndexNames((0,_E,_AE))
if mibBuilder.loadTexts:h3cQoSRemarkIPv4AddrPriEntry.setStatus(_A)
_H3cQoSRemarkIPv4AddrValue_Type=IpAddress
_H3cQoSRemarkIPv4AddrValue_Object=MibTableColumn
h3cQoSRemarkIPv4AddrValue=_H3cQoSRemarkIPv4AddrValue_Object((1,3,6,1,4,1,2011,10,2,65,1,12,3,1,1),_H3cQoSRemarkIPv4AddrValue_Type())
h3cQoSRemarkIPv4AddrValue.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cQoSRemarkIPv4AddrValue.setStatus(_A)
_H3cQoSRemarkIPv4AddrMask_Type=IpAddress
_H3cQoSRemarkIPv4AddrMask_Object=MibTableColumn
h3cQoSRemarkIPv4AddrMask=_H3cQoSRemarkIPv4AddrMask_Object((1,3,6,1,4,1,2011,10,2,65,1,12,3,1,2),_H3cQoSRemarkIPv4AddrMask_Type())
h3cQoSRemarkIPv4AddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSRemarkIPv4AddrMask.setStatus(_A)
class _H3cQoSRemarkIPv4AddrMaskLength_Type(Unsigned32):defaultValue=32;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32),ValueRangeConstraint(4294967295,4294967295))
_H3cQoSRemarkIPv4AddrMaskLength_Type.__name__=_I
_H3cQoSRemarkIPv4AddrMaskLength_Object=MibTableColumn
h3cQoSRemarkIPv4AddrMaskLength=_H3cQoSRemarkIPv4AddrMaskLength_Object((1,3,6,1,4,1,2011,10,2,65,1,12,3,1,3),_H3cQoSRemarkIPv4AddrMaskLength_Type())
h3cQoSRemarkIPv4AddrMaskLength.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSRemarkIPv4AddrMaskLength.setStatus(_A)
class _H3cQoSRemarkIPv4AddrDot1p_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_H3cQoSRemarkIPv4AddrDot1p_Type.__name__=_I
_H3cQoSRemarkIPv4AddrDot1p_Object=MibTableColumn
h3cQoSRemarkIPv4AddrDot1p=_H3cQoSRemarkIPv4AddrDot1p_Object((1,3,6,1,4,1,2011,10,2,65,1,12,3,1,4),_H3cQoSRemarkIPv4AddrDot1p_Type())
h3cQoSRemarkIPv4AddrDot1p.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSRemarkIPv4AddrDot1p.setStatus(_A)
class _H3cQoSRemarkIPv4AddrDscp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_H3cQoSRemarkIPv4AddrDscp_Type.__name__=_I
_H3cQoSRemarkIPv4AddrDscp_Object=MibTableColumn
h3cQoSRemarkIPv4AddrDscp=_H3cQoSRemarkIPv4AddrDscp_Object((1,3,6,1,4,1,2011,10,2,65,1,12,3,1,5),_H3cQoSRemarkIPv4AddrDscp_Type())
h3cQoSRemarkIPv4AddrDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSRemarkIPv4AddrDscp.setStatus(_A)
_H3cQoSRemarkIPv4AddrRowStatus_Type=RowStatus
_H3cQoSRemarkIPv4AddrRowStatus_Object=MibTableColumn
h3cQoSRemarkIPv4AddrRowStatus=_H3cQoSRemarkIPv4AddrRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,12,3,1,6),_H3cQoSRemarkIPv4AddrRowStatus_Type())
h3cQoSRemarkIPv4AddrRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSRemarkIPv4AddrRowStatus.setStatus(_A)
_H3cQoSRemarkIPv6AddrPriTable_Object=MibTable
h3cQoSRemarkIPv6AddrPriTable=_H3cQoSRemarkIPv6AddrPriTable_Object((1,3,6,1,4,1,2011,10,2,65,1,12,4))
if mibBuilder.loadTexts:h3cQoSRemarkIPv6AddrPriTable.setStatus(_A)
_H3cQoSRemarkIPv6AddrPriEntry_Object=MibTableRow
h3cQoSRemarkIPv6AddrPriEntry=_H3cQoSRemarkIPv6AddrPriEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,12,4,1))
h3cQoSRemarkIPv6AddrPriEntry.setIndexNames((0,_E,_AF))
if mibBuilder.loadTexts:h3cQoSRemarkIPv6AddrPriEntry.setStatus(_A)
_H3cQoSRemarkIPv6AddrValue_Type=InetAddressIPv6
_H3cQoSRemarkIPv6AddrValue_Object=MibTableColumn
h3cQoSRemarkIPv6AddrValue=_H3cQoSRemarkIPv6AddrValue_Object((1,3,6,1,4,1,2011,10,2,65,1,12,4,1,1),_H3cQoSRemarkIPv6AddrValue_Type())
h3cQoSRemarkIPv6AddrValue.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cQoSRemarkIPv6AddrValue.setStatus(_A)
class _H3cQoSRemarkIPv6AddrPrefixLength_Type(InetAddressPrefixLength):defaultValue=128
_H3cQoSRemarkIPv6AddrPrefixLength_Type.__name__=_k
_H3cQoSRemarkIPv6AddrPrefixLength_Object=MibTableColumn
h3cQoSRemarkIPv6AddrPrefixLength=_H3cQoSRemarkIPv6AddrPrefixLength_Object((1,3,6,1,4,1,2011,10,2,65,1,12,4,1,2),_H3cQoSRemarkIPv6AddrPrefixLength_Type())
h3cQoSRemarkIPv6AddrPrefixLength.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSRemarkIPv6AddrPrefixLength.setStatus(_A)
class _H3cQoSRemarkIPv6AddrDot1p_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_H3cQoSRemarkIPv6AddrDot1p_Type.__name__=_I
_H3cQoSRemarkIPv6AddrDot1p_Object=MibTableColumn
h3cQoSRemarkIPv6AddrDot1p=_H3cQoSRemarkIPv6AddrDot1p_Object((1,3,6,1,4,1,2011,10,2,65,1,12,4,1,3),_H3cQoSRemarkIPv6AddrDot1p_Type())
h3cQoSRemarkIPv6AddrDot1p.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSRemarkIPv6AddrDot1p.setStatus(_A)
class _H3cQoSRemarkIPv6AddrDscp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_H3cQoSRemarkIPv6AddrDscp_Type.__name__=_I
_H3cQoSRemarkIPv6AddrDscp_Object=MibTableColumn
h3cQoSRemarkIPv6AddrDscp=_H3cQoSRemarkIPv6AddrDscp_Object((1,3,6,1,4,1,2011,10,2,65,1,12,4,1,4),_H3cQoSRemarkIPv6AddrDscp_Type())
h3cQoSRemarkIPv6AddrDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSRemarkIPv6AddrDscp.setStatus(_A)
_H3cQoSRemarkIPv6AddrRowStatus_Type=RowStatus
_H3cQoSRemarkIPv6AddrRowStatus_Object=MibTableColumn
h3cQoSRemarkIPv6AddrRowStatus=_H3cQoSRemarkIPv6AddrRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,12,4,1,5),_H3cQoSRemarkIPv6AddrRowStatus_Type())
h3cQoSRemarkIPv6AddrRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSRemarkIPv6AddrRowStatus.setStatus(_A)
_H3cQoSRemarkProtocolPriTable_Object=MibTable
h3cQoSRemarkProtocolPriTable=_H3cQoSRemarkProtocolPriTable_Object((1,3,6,1,4,1,2011,10,2,65,1,12,5))
if mibBuilder.loadTexts:h3cQoSRemarkProtocolPriTable.setStatus(_A)
_H3cQoSRemarkProtocolPriEntry_Object=MibTableRow
h3cQoSRemarkProtocolPriEntry=_H3cQoSRemarkProtocolPriEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,12,5,1))
h3cQoSRemarkProtocolPriEntry.setIndexNames((0,_E,_AG))
if mibBuilder.loadTexts:h3cQoSRemarkProtocolPriEntry.setStatus(_A)
class _H3cQoSRemarkProtocolValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ip',1),('ipx',2),('arp',3),('appletalk',4),('sna',5),('netbeui',6)))
_H3cQoSRemarkProtocolValue_Type.__name__=_D
_H3cQoSRemarkProtocolValue_Object=MibTableColumn
h3cQoSRemarkProtocolValue=_H3cQoSRemarkProtocolValue_Object((1,3,6,1,4,1,2011,10,2,65,1,12,5,1,1),_H3cQoSRemarkProtocolValue_Type())
h3cQoSRemarkProtocolValue.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cQoSRemarkProtocolValue.setStatus(_A)
class _H3cQoSRemarkProtocolDot1p_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_H3cQoSRemarkProtocolDot1p_Type.__name__=_I
_H3cQoSRemarkProtocolDot1p_Object=MibTableColumn
h3cQoSRemarkProtocolDot1p=_H3cQoSRemarkProtocolDot1p_Object((1,3,6,1,4,1,2011,10,2,65,1,12,5,1,2),_H3cQoSRemarkProtocolDot1p_Type())
h3cQoSRemarkProtocolDot1p.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSRemarkProtocolDot1p.setStatus(_A)
_H3cQoSRemarkProtocolRowStatus_Type=RowStatus
_H3cQoSRemarkProtocolRowStatus_Object=MibTableColumn
h3cQoSRemarkProtocolRowStatus=_H3cQoSRemarkProtocolRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,12,5,1,3),_H3cQoSRemarkProtocolRowStatus_Type())
h3cQoSRemarkProtocolRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSRemarkProtocolRowStatus.setStatus(_A)
_H3cQoSRemarkVlanPriTable_Object=MibTable
h3cQoSRemarkVlanPriTable=_H3cQoSRemarkVlanPriTable_Object((1,3,6,1,4,1,2011,10,2,65,1,12,6))
if mibBuilder.loadTexts:h3cQoSRemarkVlanPriTable.setStatus(_A)
_H3cQoSRemarkVlanPriEntry_Object=MibTableRow
h3cQoSRemarkVlanPriEntry=_H3cQoSRemarkVlanPriEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,12,6,1))
h3cQoSRemarkVlanPriEntry.setIndexNames((0,_E,_AH))
if mibBuilder.loadTexts:h3cQoSRemarkVlanPriEntry.setStatus(_A)
class _H3cQoSRemarkVlanStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_H3cQoSRemarkVlanStart_Type.__name__=_D
_H3cQoSRemarkVlanStart_Object=MibTableColumn
h3cQoSRemarkVlanStart=_H3cQoSRemarkVlanStart_Object((1,3,6,1,4,1,2011,10,2,65,1,12,6,1,1),_H3cQoSRemarkVlanStart_Type())
h3cQoSRemarkVlanStart.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cQoSRemarkVlanStart.setStatus(_A)
class _H3cQoSRemarkVlanEnd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_H3cQoSRemarkVlanEnd_Type.__name__=_D
_H3cQoSRemarkVlanEnd_Object=MibTableColumn
h3cQoSRemarkVlanEnd=_H3cQoSRemarkVlanEnd_Object((1,3,6,1,4,1,2011,10,2,65,1,12,6,1,2),_H3cQoSRemarkVlanEnd_Type())
h3cQoSRemarkVlanEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSRemarkVlanEnd.setStatus(_A)
class _H3cQoSRemarkVlanDot1p_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_H3cQoSRemarkVlanDot1p_Type.__name__=_I
_H3cQoSRemarkVlanDot1p_Object=MibTableColumn
h3cQoSRemarkVlanDot1p=_H3cQoSRemarkVlanDot1p_Object((1,3,6,1,4,1,2011,10,2,65,1,12,6,1,3),_H3cQoSRemarkVlanDot1p_Type())
h3cQoSRemarkVlanDot1p.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSRemarkVlanDot1p.setStatus(_A)
class _H3cQoSRemarkVlanDscp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_H3cQoSRemarkVlanDscp_Type.__name__=_I
_H3cQoSRemarkVlanDscp_Object=MibTableColumn
h3cQoSRemarkVlanDscp=_H3cQoSRemarkVlanDscp_Object((1,3,6,1,4,1,2011,10,2,65,1,12,6,1,4),_H3cQoSRemarkVlanDscp_Type())
h3cQoSRemarkVlanDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSRemarkVlanDscp.setStatus(_A)
_H3cQoSRemarkVlanRowStatus_Type=RowStatus
_H3cQoSRemarkVlanRowStatus_Object=MibTableColumn
h3cQoSRemarkVlanRowStatus=_H3cQoSRemarkVlanRowStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,12,6,1,5),_H3cQoSRemarkVlanRowStatus_Type())
h3cQoSRemarkVlanRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cQoSRemarkVlanRowStatus.setStatus(_A)
_H3cQoSTypeOfServiceObjects_ObjectIdentity=ObjectIdentity
h3cQoSTypeOfServiceObjects=_H3cQoSTypeOfServiceObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,12,7))
class _H3cQoSTypeOfServiceMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),(_A2,2),(_N,3)))
_H3cQoSTypeOfServiceMode_Type.__name__=_D
_H3cQoSTypeOfServiceMode_Object=MibScalar
h3cQoSTypeOfServiceMode=_H3cQoSTypeOfServiceMode_Object((1,3,6,1,4,1,2011,10,2,65,1,12,7,1),_H3cQoSTypeOfServiceMode_Type())
h3cQoSTypeOfServiceMode.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cQoSTypeOfServiceMode.setStatus(_A)
_H3cIfQoSProcessingStatusObjects_ObjectIdentity=ObjectIdentity
h3cIfQoSProcessingStatusObjects=_H3cIfQoSProcessingStatusObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,13))
class _H3cIfQoSProcessingStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('idle',1),('busy',2)))
_H3cIfQoSProcessingStatus_Type.__name__=_D
_H3cIfQoSProcessingStatus_Object=MibScalar
h3cIfQoSProcessingStatus=_H3cIfQoSProcessingStatus_Object((1,3,6,1,4,1,2011,10,2,65,1,13,1),_H3cIfQoSProcessingStatus_Type())
h3cIfQoSProcessingStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSProcessingStatus.setStatus(_A)
_H3cIfQoSCoppObjects_ObjectIdentity=ObjectIdentity
h3cIfQoSCoppObjects=_H3cIfQoSCoppObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,65,1,14))
_H3cIfQoSCoppFlowStatTable_Object=MibTable
h3cIfQoSCoppFlowStatTable=_H3cIfQoSCoppFlowStatTable_Object((1,3,6,1,4,1,2011,10,2,65,1,14,1))
if mibBuilder.loadTexts:h3cIfQoSCoppFlowStatTable.setStatus(_A)
_H3cIfQoSCoppFlowStatEntry_Object=MibTableRow
h3cIfQoSCoppFlowStatEntry=_H3cIfQoSCoppFlowStatEntry_Object((1,3,6,1,4,1,2011,10,2,65,1,14,1,1))
h3cIfQoSCoppFlowStatEntry.setIndexNames((0,_E,_AI),(0,_E,_AJ),(0,_E,_AK))
if mibBuilder.loadTexts:h3cIfQoSCoppFlowStatEntry.setStatus(_A)
_H3cIfQoSCoppFlowStatChassis_Type=Unsigned32
_H3cIfQoSCoppFlowStatChassis_Object=MibTableColumn
h3cIfQoSCoppFlowStatChassis=_H3cIfQoSCoppFlowStatChassis_Object((1,3,6,1,4,1,2011,10,2,65,1,14,1,1,1),_H3cIfQoSCoppFlowStatChassis_Type())
h3cIfQoSCoppFlowStatChassis.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSCoppFlowStatChassis.setStatus(_A)
_H3cIfQoSCoppFlowStatSlot_Type=Unsigned32
_H3cIfQoSCoppFlowStatSlot_Object=MibTableColumn
h3cIfQoSCoppFlowStatSlot=_H3cIfQoSCoppFlowStatSlot_Object((1,3,6,1,4,1,2011,10,2,65,1,14,1,1,2),_H3cIfQoSCoppFlowStatSlot_Type())
h3cIfQoSCoppFlowStatSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSCoppFlowStatSlot.setStatus(_A)
class _H3cIfQoSCoppFlowStatProType_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65))
_H3cIfQoSCoppFlowStatProType_Type.__name__=_I
_H3cIfQoSCoppFlowStatProType_Object=MibTableColumn
h3cIfQoSCoppFlowStatProType=_H3cIfQoSCoppFlowStatProType_Object((1,3,6,1,4,1,2011,10,2,65,1,14,1,1,3),_H3cIfQoSCoppFlowStatProType_Type())
h3cIfQoSCoppFlowStatProType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIfQoSCoppFlowStatProType.setStatus(_A)
_H3cIfQoSCoppFlowPassPackets_Type=Counter64
_H3cIfQoSCoppFlowPassPackets_Object=MibTableColumn
h3cIfQoSCoppFlowPassPackets=_H3cIfQoSCoppFlowPassPackets_Object((1,3,6,1,4,1,2011,10,2,65,1,14,1,1,4),_H3cIfQoSCoppFlowPassPackets_Type())
h3cIfQoSCoppFlowPassPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSCoppFlowPassPackets.setStatus(_A)
_H3cIfQoSCoppFlowPassBytes_Type=Counter64
_H3cIfQoSCoppFlowPassBytes_Object=MibTableColumn
h3cIfQoSCoppFlowPassBytes=_H3cIfQoSCoppFlowPassBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,14,1,1,5),_H3cIfQoSCoppFlowPassBytes_Type())
h3cIfQoSCoppFlowPassBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSCoppFlowPassBytes.setStatus(_A)
_H3cIfQoSCoppFlowDropPackets_Type=Counter64
_H3cIfQoSCoppFlowDropPackets_Object=MibTableColumn
h3cIfQoSCoppFlowDropPackets=_H3cIfQoSCoppFlowDropPackets_Object((1,3,6,1,4,1,2011,10,2,65,1,14,1,1,6),_H3cIfQoSCoppFlowDropPackets_Type())
h3cIfQoSCoppFlowDropPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSCoppFlowDropPackets.setStatus(_A)
_H3cIfQoSCoppFlowDropBytes_Type=Counter64
_H3cIfQoSCoppFlowDropBytes_Object=MibTableColumn
h3cIfQoSCoppFlowDropBytes=_H3cIfQoSCoppFlowDropBytes_Object((1,3,6,1,4,1,2011,10,2,65,1,14,1,1,7),_H3cIfQoSCoppFlowDropBytes_Type())
h3cIfQoSCoppFlowDropBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cIfQoSCoppFlowDropBytes.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_O:H3cIfCarAction,'PriorityQueue':PriorityQueue,'Direction':Direction,'h3cQos2':h3cQos2,'h3cIfQos2':h3cIfQos2,'h3cIfQoSHardwareQueueObjects':h3cIfQoSHardwareQueueObjects,'h3cIfQoSHardwareQueueConfigGroup':h3cIfQoSHardwareQueueConfigGroup,'h3cIfQoSQSModeTable':h3cIfQoSQSModeTable,'h3cIfQoSQSModeEntry':h3cIfQoSQSModeEntry,'h3cIfQoSQSMode':h3cIfQoSQSMode,'h3cIfQoSQSWeightTable':h3cIfQoSQSWeightTable,'h3cIfQoSQSWeightEntry':h3cIfQoSQSWeightEntry,_P:h3cIfQoSQueueID,'h3cIfQoSQueueGroupType':h3cIfQoSQueueGroupType,'h3cIfQoSQSType':h3cIfQoSQSType,'h3cIfQoSQSValue':h3cIfQoSQSValue,'h3cIfQoSQSMaxDelay':h3cIfQoSQSMaxDelay,'h3cIfQoSQSMinBandwidth':h3cIfQoSQSMinBandwidth,'h3cIfQoSQSMinBandwidthPercent':h3cIfQoSQSMinBandwidthPercent,'h3cIfQoSHardwareQueueRunInfoGroup':h3cIfQoSHardwareQueueRunInfoGroup,'h3cIfQoSHardwareQueueRunInfoTable':h3cIfQoSHardwareQueueRunInfoTable,'h3cIfQoSHardwareQueueRunInfoEntry':h3cIfQoSHardwareQueueRunInfoEntry,'h3cIfQoSPassPackets':h3cIfQoSPassPackets,'h3cIfQoSDropPackets':h3cIfQoSDropPackets,'h3cIfQoSPassBytes':h3cIfQoSPassBytes,'h3cIfQoSPassPPS':h3cIfQoSPassPPS,'h3cIfQoSPassBPS':h3cIfQoSPassBPS,'h3cIfQoSDropBytes':h3cIfQoSDropBytes,'h3cIfQoSQueueLengthInPkts':h3cIfQoSQueueLengthInPkts,'h3cIfQoSQueueLengthInBytes':h3cIfQoSQueueLengthInBytes,'h3cIfQoSCurQueuePkts':h3cIfQoSCurQueuePkts,'h3cIfQoSCurQueueBytes':h3cIfQoSCurQueueBytes,'h3cIfQoSCurQueuePPS':h3cIfQoSCurQueuePPS,'h3cIfQoSCurQueueBPS':h3cIfQoSCurQueueBPS,'h3cIfQoSTailDropPkts':h3cIfQoSTailDropPkts,'h3cIfQoSTailDropBytes':h3cIfQoSTailDropBytes,'h3cIfQoSTailDropPPS':h3cIfQoSTailDropPPS,'h3cIfQoSTailDropBPS':h3cIfQoSTailDropBPS,'h3cIfQoSWredDropPkts':h3cIfQoSWredDropPkts,'h3cIfQoSWredDropBytes':h3cIfQoSWredDropBytes,'h3cIfQoSWredDropPPS':h3cIfQoSWredDropPPS,'h3cIfQoSWredDropBPS':h3cIfQoSWredDropBPS,'h3cIfQoSQueueName':h3cIfQoSQueueName,'h3cIfQoSHQueueTcpRunInfoTable':h3cIfQoSHQueueTcpRunInfoTable,'h3cIfQoSHQueueTcpRunInfoEntry':h3cIfQoSHQueueTcpRunInfoEntry,'h3cIfQoSWredDropLPreNTcpPkts':h3cIfQoSWredDropLPreNTcpPkts,'h3cIfQoSWredDropLPreNTcpBytes':h3cIfQoSWredDropLPreNTcpBytes,'h3cIfQoSWredDropLPreNTcpPPS':h3cIfQoSWredDropLPreNTcpPPS,'h3cIfQoSWredDropLPreNTcpBPS':h3cIfQoSWredDropLPreNTcpBPS,'h3cIfQoSWredDropLPreTcpPkts':h3cIfQoSWredDropLPreTcpPkts,'h3cIfQoSWredDropLPreTcpBytes':h3cIfQoSWredDropLPreTcpBytes,'h3cIfQoSWredDropLPreTcpPPS':h3cIfQoSWredDropLPreTcpPPS,'h3cIfQoSWredDropLPreTcpBPS':h3cIfQoSWredDropLPreTcpBPS,'h3cIfQoSWredDropHPreNTcpPkts':h3cIfQoSWredDropHPreNTcpPkts,'h3cIfQoSWredDropHPreNTcpBytes':h3cIfQoSWredDropHPreNTcpBytes,'h3cIfQoSWredDropHPreNTcpPPS':h3cIfQoSWredDropHPreNTcpPPS,'h3cIfQoSWredDropHPreNTcpBPS':h3cIfQoSWredDropHPreNTcpBPS,'h3cIfQoSWredDropHPreTcpPkts':h3cIfQoSWredDropHPreTcpPkts,'h3cIfQoSWredDropHPreTcpBytes':h3cIfQoSWredDropHPreTcpBytes,'h3cIfQoSWredDropHPreTcpPPS':h3cIfQoSWredDropHPreTcpPPS,'h3cIfQoSWredDropHPreTcpBPS':h3cIfQoSWredDropHPreTcpBPS,'h3cIfQoSHardwareQueueTotalRunInfoTable':h3cIfQoSHardwareQueueTotalRunInfoTable,'h3cIfQoSHardwareQueueTotalRunInfoEntry':h3cIfQoSHardwareQueueTotalRunInfoEntry,'h3cIfQoSQueueLength':h3cIfQoSQueueLength,'h3cIfQoSPeakQueueBytes':h3cIfQoSPeakQueueBytes,'h3cIfQoSSoftwareQueueObjects':h3cIfQoSSoftwareQueueObjects,'h3cIfQoSFIFOObject':h3cIfQoSFIFOObject,'h3cIfQoSFIFOConfigTable':h3cIfQoSFIFOConfigTable,'h3cIfQoSFIFOConfigEntry':h3cIfQoSFIFOConfigEntry,'h3cIfQoSFIFOMaxQueueLen':h3cIfQoSFIFOMaxQueueLen,'h3cIfQoSFIFORunInfoTable':h3cIfQoSFIFORunInfoTable,'h3cIfQoSFIFORunInfoEntry':h3cIfQoSFIFORunInfoEntry,'h3cIfQoSFIFOSize':h3cIfQoSFIFOSize,'h3cIfQoSFIFODiscardPackets':h3cIfQoSFIFODiscardPackets,'h3cIfQoSPQObject':h3cIfQoSPQObject,'h3cIfQoSPQConfigGroup':h3cIfQoSPQConfigGroup,'h3cIfQoSPQDefaultTable':h3cIfQoSPQDefaultTable,'h3cIfQoSPQDefaultEntry':h3cIfQoSPQDefaultEntry,_Q:h3cIfQoSPQListNumber,'h3cIfQoSPQDefaultQueueType':h3cIfQoSPQDefaultQueueType,'h3cIfQoSPQQueueLengthTable':h3cIfQoSPQQueueLengthTable,'h3cIfQoSPQQueueLengthEntry':h3cIfQoSPQQueueLengthEntry,_n:h3cIfQoSPQQueueLengthType,'h3cIfQoSPQQueueLengthValue':h3cIfQoSPQQueueLengthValue,'h3cIfQoSPQClassRuleTable':h3cIfQoSPQClassRuleTable,'h3cIfQoSPQClassRuleEntry':h3cIfQoSPQClassRuleEntry,_o:h3cIfQoSPQClassRuleType,_p:h3cIfQoSPQClassRuleValue,'h3cIfQoSPQClassRuleQueueType':h3cIfQoSPQClassRuleQueueType,'h3cIfQoSPQClassRowStatus':h3cIfQoSPQClassRowStatus,'h3cIfQoSPQApplyTable':h3cIfQoSPQApplyTable,'h3cIfQoSPQApplyEntry':h3cIfQoSPQApplyEntry,'h3cIfQoSPQApplyListNumber':h3cIfQoSPQApplyListNumber,'h3cIfQoSPQApplyRowStatus':h3cIfQoSPQApplyRowStatus,'h3cIfQoSPQRunInfoGroup':h3cIfQoSPQRunInfoGroup,'h3cIfQoSPQRunInfoTable':h3cIfQoSPQRunInfoTable,'h3cIfQoSPQRunInfoEntry':h3cIfQoSPQRunInfoEntry,_u:h3cIfQoSPQType,'h3cIfQoSPQSize':h3cIfQoSPQSize,'h3cIfQoSPQLength':h3cIfQoSPQLength,'h3cIfQoSPQDiscardPackets':h3cIfQoSPQDiscardPackets,'h3cIfQoSCQObject':h3cIfQoSCQObject,'h3cIfQoSCQConfigGroup':h3cIfQoSCQConfigGroup,'h3cIfQoSCQDefaultTable':h3cIfQoSCQDefaultTable,'h3cIfQoSCQDefaultEntry':h3cIfQoSCQDefaultEntry,_R:h3cIfQoSCQListNumber,'h3cIfQoSCQDefaultQueueID':h3cIfQoSCQDefaultQueueID,'h3cIfQoSCQQueueLengthTable':h3cIfQoSCQQueueLengthTable,'h3cIfQoSCQQueueLengthEntry':h3cIfQoSCQQueueLengthEntry,_T:h3cIfQoSCQQueueID,'h3cIfQoSCQQueueLength':h3cIfQoSCQQueueLength,'h3cIfQoSCQQueueServing':h3cIfQoSCQQueueServing,'h3cIfQoSCQClassRuleTable':h3cIfQoSCQClassRuleTable,'h3cIfQoSCQClassRuleEntry':h3cIfQoSCQClassRuleEntry,_v:h3cIfQoSCQClassRuleType,_w:h3cIfQoSCQClassRuleValue,'h3cIfQoSCQClassRuleQueueID':h3cIfQoSCQClassRuleQueueID,'h3cIfQoSCQClassRowStatus':h3cIfQoSCQClassRowStatus,'h3cIfQoSCQApplyTable':h3cIfQoSCQApplyTable,'h3cIfQoSCQApplyEntry':h3cIfQoSCQApplyEntry,'h3cIfQoSCQApplyListNumber':h3cIfQoSCQApplyListNumber,'h3cIfQoSCQApplyRowStatus':h3cIfQoSCQApplyRowStatus,'h3cIfQoSCQRunInfoGroup':h3cIfQoSCQRunInfoGroup,'h3cIfQoSCQRunInfoTable':h3cIfQoSCQRunInfoTable,'h3cIfQoSCQRunInfoEntry':h3cIfQoSCQRunInfoEntry,'h3cIfQoSCQRunInfoSize':h3cIfQoSCQRunInfoSize,'h3cIfQoSCQRunInfoLength':h3cIfQoSCQRunInfoLength,'h3cIfQoSCQRunInfoDiscardPackets':h3cIfQoSCQRunInfoDiscardPackets,'h3cIfQoSWFQObject':h3cIfQoSWFQObject,'h3cIfQoSWFQConfigGroup':h3cIfQoSWFQConfigGroup,'h3cIfQoSWFQTable':h3cIfQoSWFQTable,'h3cIfQoSWFQEntry':h3cIfQoSWFQEntry,'h3cIfQoSWFQQueueLength':h3cIfQoSWFQQueueLength,'h3cIfQoSWFQQueueNumber':h3cIfQoSWFQQueueNumber,'h3cIfQoSWFQRowStatus':h3cIfQoSWFQRowStatus,'h3cIfQoSWFQType':h3cIfQoSWFQType,'h3cIfQoSWFQRunInfoGroup':h3cIfQoSWFQRunInfoGroup,'h3cIfQoSWFQRunInfoTable':h3cIfQoSWFQRunInfoTable,'h3cIfQoSWFQRunInfoEntry':h3cIfQoSWFQRunInfoEntry,'h3cIfQoSWFQSize':h3cIfQoSWFQSize,'h3cIfQoSWFQLength':h3cIfQoSWFQLength,'h3cIfQoSWFQDiscardPackets':h3cIfQoSWFQDiscardPackets,'h3cIfQoSWFQHashedActiveQueues':h3cIfQoSWFQHashedActiveQueues,'h3cIfQoSWFQHashedMaxActiveQueues':h3cIfQoSWFQHashedMaxActiveQueues,'h3fIfQosWFQhashedTotalQueues':h3fIfQosWFQhashedTotalQueues,'h3cIfQoSBandwidthGroup':h3cIfQoSBandwidthGroup,'h3cIfQoSBandwidthTable':h3cIfQoSBandwidthTable,'h3cIfQoSBandwidthEntry':h3cIfQoSBandwidthEntry,'h3cIfQoSMaxBandwidth':h3cIfQoSMaxBandwidth,'h3cIfQoSReservedBandwidthPct':h3cIfQoSReservedBandwidthPct,'h3cIfQoSBandwidthRowStatus':h3cIfQoSBandwidthRowStatus,'h3cIfQoSQmtokenGroup':h3cIfQoSQmtokenGroup,'h3cIfQoSQmtokenTable':h3cIfQoSQmtokenTable,'h3cIfQoSQmtokenEntry':h3cIfQoSQmtokenEntry,'h3cIfQoSQmtokenNumber':h3cIfQoSQmtokenNumber,'h3cIfQoSQmtokenRosStatus':h3cIfQoSQmtokenRosStatus,'h3cIfQoSRTPQObject':h3cIfQoSRTPQObject,'h3cIfQoSRTPQConfigGroup':h3cIfQoSRTPQConfigGroup,'h3cIfQoSRTPQConfigTable':h3cIfQoSRTPQConfigTable,'h3cIfQoSRTPQConfigEntry':h3cIfQoSRTPQConfigEntry,'h3cIfQoSRTPQStartPort':h3cIfQoSRTPQStartPort,'h3cIfQoSRTPQEndPort':h3cIfQoSRTPQEndPort,'h3cIfQoSRTPQReservedBandwidth':h3cIfQoSRTPQReservedBandwidth,'h3cIfQoSRTPQCbs':h3cIfQoSRTPQCbs,'h3cIfQoSRTPQRowStatus':h3cIfQoSRTPQRowStatus,'h3cIfQoSRTPQRunInfoGroup':h3cIfQoSRTPQRunInfoGroup,'h3cIfQoSRTPQRunInfoTable':h3cIfQoSRTPQRunInfoTable,'h3cIfQoSRTPQRunInfoEntry':h3cIfQoSRTPQRunInfoEntry,'h3cIfQoSRTPQPacketNumber':h3cIfQoSRTPQPacketNumber,'h3cIfQoSRTPQPacketSize':h3cIfQoSRTPQPacketSize,'h3cIfQoSRTPQOutputPackets':h3cIfQoSRTPQOutputPackets,'h3cIfQoSRTPQDiscardPackets':h3cIfQoSRTPQDiscardPackets,'h3cIfQoSCarListObject':h3cIfQoSCarListObject,'h3cIfQoCarListGroup':h3cIfQoCarListGroup,'h3cIfQoSCarlTable':h3cIfQoSCarlTable,'h3cIfQoSCarlEntry':h3cIfQoSCarlEntry,_x:h3cIfQoSCarlListNum,'h3cIfQoSCarlParaType':h3cIfQoSCarlParaType,'h3cIfQoSCarlParaValue':h3cIfQoSCarlParaValue,'h3cIfQoSCarlRowStatus':h3cIfQoSCarlRowStatus,'h3cIfQoSLineRateObjects':h3cIfQoSLineRateObjects,'h3cIfQoSLRConfigTable':h3cIfQoSLRConfigTable,'h3cIfQoSLRConfigEntry':h3cIfQoSLRConfigEntry,_U:h3cIfQoSLRDirection,'h3cIfQoSLRCir':h3cIfQoSLRCir,'h3cIfQoSLRCbs':h3cIfQoSLRCbs,'h3cIfQoSLREbs':h3cIfQoSLREbs,'h3cIfQoSRowStatus':h3cIfQoSRowStatus,'h3cIfQoSLRPir':h3cIfQoSLRPir,'h3cIfQoSLRUnit':h3cIfQoSLRUnit,'h3cIfQoSLRRunInfoTable':h3cIfQoSLRRunInfoTable,'h3cIfQoSLRRunInfoEntry':h3cIfQoSLRRunInfoEntry,'h3cIfQoSLRRunInfoPassedPackets':h3cIfQoSLRRunInfoPassedPackets,'h3cIfQoSLRRunInfoPassedBytes':h3cIfQoSLRRunInfoPassedBytes,'h3cIfQoSLRRunInfoDelayedPackets':h3cIfQoSLRRunInfoDelayedPackets,'h3cIfQoSLRRunInfoDelayedBytes':h3cIfQoSLRRunInfoDelayedBytes,'h3cIfQoSLRRunInfoActiveShaping':h3cIfQoSLRRunInfoActiveShaping,'h3cIfQoSCARObjects':h3cIfQoSCARObjects,'h3cIfQoSAggregativeCarGroup':h3cIfQoSAggregativeCarGroup,'h3cIfQoSAggregativeCarNextIndex':h3cIfQoSAggregativeCarNextIndex,'h3cIfQoSAggregativeCarConfigTable':h3cIfQoSAggregativeCarConfigTable,'h3cIfQoSAggregativeCarConfigEntry':h3cIfQoSAggregativeCarConfigEntry,_X:h3cIfQoSAggregativeCarIndex,'h3cIfQoSAggregativeCarName':h3cIfQoSAggregativeCarName,'h3cIfQoSAggregativeCarCir':h3cIfQoSAggregativeCarCir,'h3cIfQoSAggregativeCarCbs':h3cIfQoSAggregativeCarCbs,'h3cIfQoSAggregativeCarEbs':h3cIfQoSAggregativeCarEbs,'h3cIfQoSAggregativeCarPir':h3cIfQoSAggregativeCarPir,'h3cIfQoSAggregativeCarGreenActionType':h3cIfQoSAggregativeCarGreenActionType,'h3cIfQoSAggregativeCarGreenActionValue':h3cIfQoSAggregativeCarGreenActionValue,'h3cIfQoSAggregativeCarYellowActionType':h3cIfQoSAggregativeCarYellowActionType,'h3cIfQoSAggregativeCarYellowActionValue':h3cIfQoSAggregativeCarYellowActionValue,'h3cIfQoSAggregativeCarRedActionType':h3cIfQoSAggregativeCarRedActionType,'h3cIfQoSAggregativeCarRedActionValue':h3cIfQoSAggregativeCarRedActionValue,'h3cIfQoSAggregativeCarType':h3cIfQoSAggregativeCarType,'h3cIfQoSAggregativeCarRowStatus':h3cIfQoSAggregativeCarRowStatus,'h3cIfQoSAggregativeCarApplyTable':h3cIfQoSAggregativeCarApplyTable,'h3cIfQoSAggregativeCarApplyEntry':h3cIfQoSAggregativeCarApplyEntry,_y:h3cIfQoSAggregativeCarApplyDirection,_z:h3cIfQoSAggregativeCarApplyRuleType,_A0:h3cIfQoSAggregativeCarApplyRuleValue,'h3cIfQoSAggregativeCarApplyCarIndex':h3cIfQoSAggregativeCarApplyCarIndex,'h3cIfQoSAggregativeCarApplyRowStatus':h3cIfQoSAggregativeCarApplyRowStatus,'h3cIfQoSAggregativeCarRunInfoTable':h3cIfQoSAggregativeCarRunInfoTable,'h3cIfQoSAggregativeCarRunInfoEntry':h3cIfQoSAggregativeCarRunInfoEntry,'h3cIfQoSAggregativeCarGreenPackets':h3cIfQoSAggregativeCarGreenPackets,'h3cIfQoSAggregativeCarGreenBytes':h3cIfQoSAggregativeCarGreenBytes,'h3cIfQoSAggregativeCarYellowPackets':h3cIfQoSAggregativeCarYellowPackets,'h3cIfQoSAggregativeCarYellowBytes':h3cIfQoSAggregativeCarYellowBytes,'h3cIfQoSAggregativeCarRedPackets':h3cIfQoSAggregativeCarRedPackets,'h3cIfQoSAggregativeCarRedBytes':h3cIfQoSAggregativeCarRedBytes,'h3cIfQoSTricolorCarGroup':h3cIfQoSTricolorCarGroup,'h3cIfQoSTricolorCarConfigTable':h3cIfQoSTricolorCarConfigTable,'h3cIfQoSTricolorCarConfigEntry':h3cIfQoSTricolorCarConfigEntry,_Z:h3cIfQoSTricolorCarDirection,_a:h3cIfQoSTricolorCarType,_b:h3cIfQoSTricolorCarValue,'h3cIfQoSTricolorCarCir':h3cIfQoSTricolorCarCir,'h3cIfQoSTricolorCarCbs':h3cIfQoSTricolorCarCbs,'h3cIfQoSTricolorCarEbs':h3cIfQoSTricolorCarEbs,'h3cIfQoSTricolorCarPir':h3cIfQoSTricolorCarPir,'h3cIfQoSTricolorCarGreenActionType':h3cIfQoSTricolorCarGreenActionType,'h3cIfQoSTricolorCarGreenActionValue':h3cIfQoSTricolorCarGreenActionValue,'h3cIfQoSTricolorCarYellowActionType':h3cIfQoSTricolorCarYellowActionType,'h3cIfQoSTricolorCarYellowActionValue':h3cIfQoSTricolorCarYellowActionValue,'h3cIfQoSTricolorCarRedActionType':h3cIfQoSTricolorCarRedActionType,'h3cIfQoSTricolorCarRedActionValue':h3cIfQoSTricolorCarRedActionValue,'h3cIfQoSTricolorCarRowStatus':h3cIfQoSTricolorCarRowStatus,'h3cIfQoSTricolorCarUnitType':h3cIfQoSTricolorCarUnitType,'h3cIfQoSTricolorCarRunInfoTable':h3cIfQoSTricolorCarRunInfoTable,'h3cIfQoSTricolorCarRunInfoEntry':h3cIfQoSTricolorCarRunInfoEntry,'h3cIfQoSTricolorCarGreenPackets':h3cIfQoSTricolorCarGreenPackets,'h3cIfQoSTricolorCarGreenBytes':h3cIfQoSTricolorCarGreenBytes,'h3cIfQoSTricolorCarYellowPackets':h3cIfQoSTricolorCarYellowPackets,'h3cIfQoSTricolorCarYellowBytes':h3cIfQoSTricolorCarYellowBytes,'h3cIfQoSTricolorCarRedPackets':h3cIfQoSTricolorCarRedPackets,'h3cIfQoSTricolorCarRedBytes':h3cIfQoSTricolorCarRedBytes,'h3cIfQoSGTSObjects':h3cIfQoSGTSObjects,'h3cIfQoSGTSConfigTable':h3cIfQoSGTSConfigTable,'h3cIfQoSGTSConfigEntry':h3cIfQoSGTSConfigEntry,_c:h3cIfQoSGTSClassRuleType,_d:h3cIfQoSGTSClassRuleValue,'h3cIfQoSGTSCir':h3cIfQoSGTSCir,'h3cIfQoSGTSCbs':h3cIfQoSGTSCbs,'h3cIfQoSGTSEbs':h3cIfQoSGTSEbs,'h3cIfQoSGTSQueueLength':h3cIfQoSGTSQueueLength,'h3cIfQoSGTSConfigRowStatus':h3cIfQoSGTSConfigRowStatus,'h3cIfQoSGTSPir':h3cIfQoSGTSPir,'h3cIfQoSGTSUnitType':h3cIfQoSGTSUnitType,'h3cIfQoSGTSRunInfoTable':h3cIfQoSGTSRunInfoTable,'h3cIfQoSGTSRunInfoEntry':h3cIfQoSGTSRunInfoEntry,'h3cIfQoSGTSQueueSize':h3cIfQoSGTSQueueSize,'h3cIfQoSGTSPassedPackets':h3cIfQoSGTSPassedPackets,'h3cIfQoSGTSPassedBytes':h3cIfQoSGTSPassedBytes,'h3cIfQoSGTSDiscardPackets':h3cIfQoSGTSDiscardPackets,'h3cIfQoSGTSDiscardBytes':h3cIfQoSGTSDiscardBytes,'h3cIfQoSGTSDelayedPackets':h3cIfQoSGTSDelayedPackets,'h3cIfQoSGTSDelayedBytes':h3cIfQoSGTSDelayedBytes,'h3cIfQoSWREDObjects':h3cIfQoSWREDObjects,'h3cIfQoSWredGroupGroup':h3cIfQoSWredGroupGroup,'h3cIfQoSWredGroupNextIndex':h3cIfQoSWredGroupNextIndex,'h3cIfQoSWredGroupTable':h3cIfQoSWredGroupTable,'h3cIfQoSWredGroupEntry':h3cIfQoSWredGroupEntry,_S:h3cIfQoSWredGroupIndex,'h3cIfQoSWredGroupName':h3cIfQoSWredGroupName,'h3cIfQoSWredGroupType':h3cIfQoSWredGroupType,'h3cIfQoSWredGroupWeightingConstant':h3cIfQoSWredGroupWeightingConstant,'h3cIfQoSWredGroupRowStatus':h3cIfQoSWredGroupRowStatus,'h3cIfQoSWredGroupContentTable':h3cIfQoSWredGroupContentTable,'h3cIfQoSWredGroupContentEntry':h3cIfQoSWredGroupContentEntry,_g:h3cIfQoSWredGroupContentIndex,_h:h3cIfQoSWredGroupContentSubIndex,'h3cIfQoSWredLowLimit':h3cIfQoSWredLowLimit,'h3cIfQoSWredHighLimit':h3cIfQoSWredHighLimit,'h3cIfQoSWredDiscardProb':h3cIfQoSWredDiscardProb,'h3cIfQoSWredGroupExponent':h3cIfQoSWredGroupExponent,'h3cIfQoSWredRowStatus':h3cIfQoSWredRowStatus,'h3cIfQoSWredGroupApplyIfTable':h3cIfQoSWredGroupApplyIfTable,'h3cIfQoSWredGroupApplyIfEntry':h3cIfQoSWredGroupApplyIfEntry,'h3cIfQoSWredGroupApplyIndex':h3cIfQoSWredGroupApplyIndex,'h3cIfQoSWredGroupApplyName':h3cIfQoSWredGroupApplyName,'h3cIfQoSWredGroupIfRowStatus':h3cIfQoSWredGroupIfRowStatus,'h3cIfQoSWredApplyIfRunInfoTable':h3cIfQoSWredApplyIfRunInfoTable,'h3cIfQoSWredApplyIfRunInfoEntry':h3cIfQoSWredApplyIfRunInfoEntry,'h3cIfQoSWredPreRandomDropNum':h3cIfQoSWredPreRandomDropNum,'h3cIfQoSWredPreTailDropNum':h3cIfQoSWredPreTailDropNum,'h3cIfQoSPortWredGroup':h3cIfQoSPortWredGroup,'h3cIfQoSPortWredWeightConstantTable':h3cIfQoSPortWredWeightConstantTable,'h3cIfQoSPortWredWeightConstantEntry':h3cIfQoSPortWredWeightConstantEntry,'h3cIfQoSPortWredEnable':h3cIfQoSPortWredEnable,'h3cIfQoSPortWredWeightConstant':h3cIfQoSPortWredWeightConstant,'h3cIfQoSPortWredWeightConstantRowStatus':h3cIfQoSPortWredWeightConstantRowStatus,'h3cIfQoSPortWredPreConfigTable':h3cIfQoSPortWredPreConfigTable,'h3cIfQoSPortWredPreConfigEntry':h3cIfQoSPortWredPreConfigEntry,_i:h3cIfQoSPortWredPreID,'h3cIfQoSPortWredPreLowLimit':h3cIfQoSPortWredPreLowLimit,'h3cIfQoSPortWredPreHighLimit':h3cIfQoSPortWredPreHighLimit,'h3cIfQoSPortWredPreDiscardProbability':h3cIfQoSPortWredPreDiscardProbability,'h3cIfQoSPortWredPreRowStatus':h3cIfQoSPortWredPreRowStatus,'h3cIfQoSPortWredRunInfoTable':h3cIfQoSPortWredRunInfoTable,'h3cIfQoSPortWredRunInfoEntry':h3cIfQoSPortWredRunInfoEntry,'h3cIfQoSWREDTailDropNum':h3cIfQoSWREDTailDropNum,'h3cIfQoSWREDRandomDropNum':h3cIfQoSWREDRandomDropNum,'h3cIfQoSPortPriorityObjects':h3cIfQoSPortPriorityObjects,'h3cIfQoSPortPriorityConfigGroup':h3cIfQoSPortPriorityConfigGroup,'h3cIfQoSPortPriorityTable':h3cIfQoSPortPriorityTable,'h3cIfQoSPortPriorityEntry':h3cIfQoSPortPriorityEntry,'h3cIfQoSPortPriorityValue':h3cIfQoSPortPriorityValue,'h3cIfQoSPortPirorityTrustTable':h3cIfQoSPortPirorityTrustTable,'h3cIfQoSPortPirorityTrustEntry':h3cIfQoSPortPirorityTrustEntry,'h3cIfQoSPortPriorityTrustTrustType':h3cIfQoSPortPriorityTrustTrustType,'h3cIfQoSPortPriorityTrustOvercastType':h3cIfQoSPortPriorityTrustOvercastType,'h3cIfQoSMapObjects':h3cIfQoSMapObjects,'h3cIfQoSPriMapConfigGroup':h3cIfQoSPriMapConfigGroup,'h3cIfQoSPriMapGroupNextIndex':h3cIfQoSPriMapGroupNextIndex,'h3cIfQoSPriMapGroupTable':h3cIfQoSPriMapGroupTable,'h3cIfQoSPriMapGroupEntry':h3cIfQoSPriMapGroupEntry,_j:h3cIfQoSPriMapGroupIndex,'h3cIfQoSPriMapGroupType':h3cIfQoSPriMapGroupType,'h3cIfQoSPriMapGroupName':h3cIfQoSPriMapGroupName,'h3cIfQoSPriMapGroupRowStatus':h3cIfQoSPriMapGroupRowStatus,'h3cIfQoSPriMapContentTable':h3cIfQoSPriMapContentTable,'h3cIfQoSPriMapContentEntry':h3cIfQoSPriMapContentEntry,_A3:h3cIfQoSPriMapGroupImportValue,'h3cIfQoSPriMapGroupExportValue':h3cIfQoSPriMapGroupExportValue,'h3cIfQoSPriMapContentRowStatus':h3cIfQoSPriMapContentRowStatus,'h3cIfQoSPrePriMapTable':h3cIfQoSPrePriMapTable,'h3cIfQoSPrePriMapEntry':h3cIfQoSPrePriMapEntry,_A4:h3cIfQoSPrePriMapTableType,_A5:h3cIfQoSPrePriMapTableColor,_A6:h3cIfQoSPrePriMapTableDirection,_A7:h3cIfQoSPrePriMapTableImportValue,'h3cIfQoSPrePriMapTableExportValue':h3cIfQoSPrePriMapTableExportValue,'h3cIfQoSL3PlusObjects':h3cIfQoSL3PlusObjects,'h3cIfQoSPortBindingGroup':h3cIfQoSPortBindingGroup,'h3cIfQoSPortBindingTable':h3cIfQoSPortBindingTable,'h3cIfQoSPortBindingEntry':h3cIfQoSPortBindingEntry,'h3cIfQoSBindingIf':h3cIfQoSBindingIf,'h3cIfQoSBindingRowStatus':h3cIfQoSBindingRowStatus,'h3cQoSTraStaObjects':h3cQoSTraStaObjects,'h3cQoSTraStaConfigGroup':h3cQoSTraStaConfigGroup,'h3cQoSIfTraStaConfigInfoTable':h3cQoSIfTraStaConfigInfoTable,'h3cQoSIfTraStaConfigInfoEntry':h3cQoSIfTraStaConfigInfoEntry,_A8:h3cQoSIfTraStaConfigDirection,'h3cQoSIfTraStaConfigQueue':h3cQoSIfTraStaConfigQueue,'h3cQoSIfTraStaConfigDot1p':h3cQoSIfTraStaConfigDot1p,'h3cQoSIfTraStaConfigDscp':h3cQoSIfTraStaConfigDscp,'h3cQoSIfTraStaConfigVlan':h3cQoSIfTraStaConfigVlan,'h3cQoSIfTraStaConfigStatus':h3cQoSIfTraStaConfigStatus,'h3cQoSTraStaRunGroup':h3cQoSTraStaRunGroup,'h3cQoSIfTraStaRunInfoTable':h3cQoSIfTraStaRunInfoTable,'h3cQoSIfTraStaRunInfoEntry':h3cQoSIfTraStaRunInfoEntry,_A9:h3cQoSIfTraStaRunObjectType,_AA:h3cQoSIfTraStaRunObjectValue,_AB:h3cQoSIfTraStaRunDirection,'h3cQoSIfTraStaRunPassPackets':h3cQoSIfTraStaRunPassPackets,'h3cQoSIfTraStaRunDropPackets':h3cQoSIfTraStaRunDropPackets,'h3cQoSIfTraStaRunPassBytes':h3cQoSIfTraStaRunPassBytes,'h3cQoSIfTraStaRunDropBytes':h3cQoSIfTraStaRunDropBytes,'h3cQoSIfTraStaRunPassPPS':h3cQoSIfTraStaRunPassPPS,'h3cQoSIfTraStaRunPassBPS':h3cQoSIfTraStaRunPassBPS,'h3cQoSGlobalPriorityObject':h3cQoSGlobalPriorityObject,'h3cQoSRemarkTcpPortPriTable':h3cQoSRemarkTcpPortPriTable,'h3cQoSRemarkTcpPortPriEntry':h3cQoSRemarkTcpPortPriEntry,_AC:h3cQoSRemarkTcpPortStart,'h3cQoSRemarkTcpPortEnd':h3cQoSRemarkTcpPortEnd,'h3cQoSRemarkTcpPortType':h3cQoSRemarkTcpPortType,'h3cQoSRemarkTcpPortDot1p':h3cQoSRemarkTcpPortDot1p,'h3cQoSRemarkTcpPortDscp':h3cQoSRemarkTcpPortDscp,'h3cQoSRemarkTcpPortRowStatus':h3cQoSRemarkTcpPortRowStatus,'h3cQoSRemarkUdpPortPriTable':h3cQoSRemarkUdpPortPriTable,'h3cQoSRemarkUdpPortPriEntry':h3cQoSRemarkUdpPortPriEntry,_AD:h3cQoSRemarkUdpPortStart,'h3cQoSRemarkUdpPortEnd':h3cQoSRemarkUdpPortEnd,'h3cQoSRemarkUdpPortType':h3cQoSRemarkUdpPortType,'h3cQoSRemarkUdpPortDot1p':h3cQoSRemarkUdpPortDot1p,'h3cQoSRemarkUdpPortDscp':h3cQoSRemarkUdpPortDscp,'h3cQoSRemarkUdpPortRowStatus':h3cQoSRemarkUdpPortRowStatus,'h3cQoSRemarkIPv4AddrPriTable':h3cQoSRemarkIPv4AddrPriTable,'h3cQoSRemarkIPv4AddrPriEntry':h3cQoSRemarkIPv4AddrPriEntry,_AE:h3cQoSRemarkIPv4AddrValue,'h3cQoSRemarkIPv4AddrMask':h3cQoSRemarkIPv4AddrMask,'h3cQoSRemarkIPv4AddrMaskLength':h3cQoSRemarkIPv4AddrMaskLength,'h3cQoSRemarkIPv4AddrDot1p':h3cQoSRemarkIPv4AddrDot1p,'h3cQoSRemarkIPv4AddrDscp':h3cQoSRemarkIPv4AddrDscp,'h3cQoSRemarkIPv4AddrRowStatus':h3cQoSRemarkIPv4AddrRowStatus,'h3cQoSRemarkIPv6AddrPriTable':h3cQoSRemarkIPv6AddrPriTable,'h3cQoSRemarkIPv6AddrPriEntry':h3cQoSRemarkIPv6AddrPriEntry,_AF:h3cQoSRemarkIPv6AddrValue,'h3cQoSRemarkIPv6AddrPrefixLength':h3cQoSRemarkIPv6AddrPrefixLength,'h3cQoSRemarkIPv6AddrDot1p':h3cQoSRemarkIPv6AddrDot1p,'h3cQoSRemarkIPv6AddrDscp':h3cQoSRemarkIPv6AddrDscp,'h3cQoSRemarkIPv6AddrRowStatus':h3cQoSRemarkIPv6AddrRowStatus,'h3cQoSRemarkProtocolPriTable':h3cQoSRemarkProtocolPriTable,'h3cQoSRemarkProtocolPriEntry':h3cQoSRemarkProtocolPriEntry,_AG:h3cQoSRemarkProtocolValue,'h3cQoSRemarkProtocolDot1p':h3cQoSRemarkProtocolDot1p,'h3cQoSRemarkProtocolRowStatus':h3cQoSRemarkProtocolRowStatus,'h3cQoSRemarkVlanPriTable':h3cQoSRemarkVlanPriTable,'h3cQoSRemarkVlanPriEntry':h3cQoSRemarkVlanPriEntry,_AH:h3cQoSRemarkVlanStart,'h3cQoSRemarkVlanEnd':h3cQoSRemarkVlanEnd,'h3cQoSRemarkVlanDot1p':h3cQoSRemarkVlanDot1p,'h3cQoSRemarkVlanDscp':h3cQoSRemarkVlanDscp,'h3cQoSRemarkVlanRowStatus':h3cQoSRemarkVlanRowStatus,'h3cQoSTypeOfServiceObjects':h3cQoSTypeOfServiceObjects,'h3cQoSTypeOfServiceMode':h3cQoSTypeOfServiceMode,'h3cIfQoSProcessingStatusObjects':h3cIfQoSProcessingStatusObjects,'h3cIfQoSProcessingStatus':h3cIfQoSProcessingStatus,'h3cIfQoSCoppObjects':h3cIfQoSCoppObjects,'h3cIfQoSCoppFlowStatTable':h3cIfQoSCoppFlowStatTable,'h3cIfQoSCoppFlowStatEntry':h3cIfQoSCoppFlowStatEntry,_AI:h3cIfQoSCoppFlowStatChassis,_AJ:h3cIfQoSCoppFlowStatSlot,_AK:h3cIfQoSCoppFlowStatProType,'h3cIfQoSCoppFlowPassPackets':h3cIfQoSCoppFlowPassPackets,'h3cIfQoSCoppFlowPassBytes':h3cIfQoSCoppFlowPassBytes,'h3cIfQoSCoppFlowDropPackets':h3cIfQoSCoppFlowDropPackets,'h3cIfQoSCoppFlowDropBytes':h3cIfQoSCoppFlowDropBytes})