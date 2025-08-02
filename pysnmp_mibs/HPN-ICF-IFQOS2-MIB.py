_AF='hpnicfQoSRemarkVlanStart'
_AE='hpnicfQoSRemarkProtocolValue'
_AD='hpnicfQoSRemarkIPv6AddrValue'
_AC='hpnicfQoSRemarkIPv4AddrValue'
_AB='hpnicfQoSRemarkUdpPortStart'
_AA='hpnicfQoSRemarkTcpPortStart'
_A9='hpnicfQoSIfTraStaRunDirection'
_A8='hpnicfQoSIfTraStaRunObjectValue'
_A7='hpnicfQoSIfTraStaRunObjectType'
_A6='hpnicfQoSIfTraStaConfigDirection'
_A5='hpnicfIfQoSPrePriMapTableImportValue'
_A4='hpnicfIfQoSPrePriMapTableDirection'
_A3='hpnicfIfQoSPrePriMapTableColor'
_A2='hpnicfIfQoSPrePriMapTableType'
_A1='hpnicfIfQoSPriMapGroupImportValue'
_A0='ipPrecedence'
_z='userdefined'
_y='hpnicfIfQoSAggregativeCarApplyRuleValue'
_x='hpnicfIfQoSAggregativeCarApplyRuleType'
_w='hpnicfIfQoSAggregativeCarApplyDirection'
_v='hpnicfIfQoSCarlListNum'
_u='hpnicfIfQoSCQClassRuleValue'
_t='hpnicfIfQoSCQClassRuleType'
_s='hpnicfIfQoSPQType'
_r='less-than'
_q='greater-than'
_p='fragments'
_o='interface'
_n='hpnicfIfQoSPQClassRuleValue'
_m='hpnicfIfQoSPQClassRuleType'
_l='hpnicfIfQoSPQQueueLengthType'
_k='outbound'
_j='inbound'
_i='InetAddressPrefixLength'
_h='hpnicfIfQoSPriMapGroupIndex'
_g='hpnicfIfQoSPortWredPreID'
_f='hpnicfIfQoSWredGroupContentSubIndex'
_e='hpnicfIfQoSWredGroupContentIndex'
_d='dot1p'
_c='queue'
_b='hpnicfIfQoSGTSClassRuleValue'
_a='hpnicfIfQoSGTSClassRuleType'
_Z='hpnicfIfQoSTricolorCarValue'
_Y='hpnicfIfQoSTricolorCarType'
_X='hpnicfIfQoSTricolorCarDirection'
_W='any'
_V='hpnicfIfQoSAggregativeCarIndex'
_U='hpnicfIfQoSLRDirection'
_T='hpnicfIfQoSCQQueueID'
_S='hpnicfIfQoSWredGroupIndex'
_R='hpnicfIfQoSCQListNumber'
_Q='hpnicfIfQoSPQListNumber'
_P='hpnicfIfQoSQueueID'
_O='CarAction'
_N='dscp'
_M='ipv6acl'
_L='ipv4acl'
_K='OctetString'
_J='Unsigned32'
_I='read-write'
_H='ifIndex'
_G='IF-MIB'
_F='not-accessible'
_E='HPN-ICF-IFQOS2-MIB'
_D='Integer32'
_C='read-only'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_G,_H)
InetAddressIPv6,InetAddressPrefixLength=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv6',_i)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_J,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
hpnicfIfQos2=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1))
if mibBuilder.loadTexts:hpnicfIfQos2.setRevisions(('2013-11-28 00:00',))
class CarAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('invalid',0),('pass',1),('continue',2),('discard',3),('remark',4),('remark-ip-continue',5),('remark-ip-pass',6),('remark-mplsexp-continue',7),('remark-mplsexp-pass',8),('remark-dscp-continue',9),('remark-dscp-pass',10),('remark-dot1p-continue',11),('remark-dot1p-pass',12),('remark-atm-clp-continue',13),('remark-atm-clp-pass',14),('remark-fr-de-continue',15),('remark-fr-de-pass',16)))
class PriorityQueue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('top',1),('middle',2),('normal',3),('bottom',4)))
class Direction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_j,1),(_k,2)))
_HpnicfQos2_ObjectIdentity=ObjectIdentity
hpnicfQos2=_HpnicfQos2_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65))
_HpnicfIfQoSHardwareQueueObjects_ObjectIdentity=ObjectIdentity
hpnicfIfQoSHardwareQueueObjects=_HpnicfIfQoSHardwareQueueObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1))
_HpnicfIfQoSHardwareQueueConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfIfQoSHardwareQueueConfigGroup=_HpnicfIfQoSHardwareQueueConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,1))
_HpnicfIfQoSQSModeTable_Object=MibTable
hpnicfIfQoSQSModeTable=_HpnicfIfQoSQSModeTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,1,1))
if mibBuilder.loadTexts:hpnicfIfQoSQSModeTable.setStatus(_A)
_HpnicfIfQoSQSModeEntry_Object=MibTableRow
hpnicfIfQoSQSModeEntry=_HpnicfIfQoSQSModeEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,1,1,1))
hpnicfIfQoSQSModeEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hpnicfIfQoSQSModeEntry.setStatus(_A)
class _HpnicfIfQoSQSMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('sp',1),('sp0',2),('sp1',3),('sp2',4),('wrr',5),('hpnicffq',6),('wrr-sp',7),('byteCountWrr',8),('byteCountWfq',9),('gmb',10)))
_HpnicfIfQoSQSMode_Type.__name__=_D
_HpnicfIfQoSQSMode_Object=MibTableColumn
hpnicfIfQoSQSMode=_HpnicfIfQoSQSMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,1,1,1,1),_HpnicfIfQoSQSMode_Type())
hpnicfIfQoSQSMode.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfIfQoSQSMode.setStatus(_A)
_HpnicfIfQoSQSWeightTable_Object=MibTable
hpnicfIfQoSQSWeightTable=_HpnicfIfQoSQSWeightTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,1,2))
if mibBuilder.loadTexts:hpnicfIfQoSQSWeightTable.setStatus(_A)
_HpnicfIfQoSQSWeightEntry_Object=MibTableRow
hpnicfIfQoSQSWeightEntry=_HpnicfIfQoSQSWeightEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,1,2,1))
hpnicfIfQoSQSWeightEntry.setIndexNames((0,_G,_H),(0,_E,_P))
if mibBuilder.loadTexts:hpnicfIfQoSQSWeightEntry.setStatus(_A)
_HpnicfIfQoSQueueID_Type=Integer32
_HpnicfIfQoSQueueID_Object=MibTableColumn
hpnicfIfQoSQueueID=_HpnicfIfQoSQueueID_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,1,2,1,1),_HpnicfIfQoSQueueID_Type())
hpnicfIfQoSQueueID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSQueueID.setStatus(_A)
class _HpnicfIfQoSQueueGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('group0',1),('group1',2),('group2',3)))
_HpnicfIfQoSQueueGroupType_Type.__name__=_D
_HpnicfIfQoSQueueGroupType_Object=MibTableColumn
hpnicfIfQoSQueueGroupType=_HpnicfIfQoSQueueGroupType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,1,2,1,2),_HpnicfIfQoSQueueGroupType_Type())
hpnicfIfQoSQueueGroupType.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfIfQoSQueueGroupType.setStatus(_A)
class _HpnicfIfQoSQSType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('weight',1),('byte-count',2)))
_HpnicfIfQoSQSType_Type.__name__=_D
_HpnicfIfQoSQSType_Object=MibTableColumn
hpnicfIfQoSQSType=_HpnicfIfQoSQSType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,1,2,1,3),_HpnicfIfQoSQSType_Type())
hpnicfIfQoSQSType.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfIfQoSQSType.setStatus(_A)
_HpnicfIfQoSQSValue_Type=Integer32
_HpnicfIfQoSQSValue_Object=MibTableColumn
hpnicfIfQoSQSValue=_HpnicfIfQoSQSValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,1,2,1,4),_HpnicfIfQoSQSValue_Type())
hpnicfIfQoSQSValue.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfIfQoSQSValue.setStatus(_A)
class _HpnicfIfQoSQSMaxDelay_Type(Integer32):defaultValue=9
_HpnicfIfQoSQSMaxDelay_Type.__name__=_D
_HpnicfIfQoSQSMaxDelay_Object=MibTableColumn
hpnicfIfQoSQSMaxDelay=_HpnicfIfQoSQSMaxDelay_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,1,2,1,5),_HpnicfIfQoSQSMaxDelay_Type())
hpnicfIfQoSQSMaxDelay.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfIfQoSQSMaxDelay.setStatus(_A)
_HpnicfIfQoSQSMinBandwidth_Type=Integer32
_HpnicfIfQoSQSMinBandwidth_Object=MibTableColumn
hpnicfIfQoSQSMinBandwidth=_HpnicfIfQoSQSMinBandwidth_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,1,2,1,6),_HpnicfIfQoSQSMinBandwidth_Type())
hpnicfIfQoSQSMinBandwidth.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfIfQoSQSMinBandwidth.setStatus(_A)
class _HpnicfIfQoSQSMinBandwidthPercent_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100),ValueRangeConstraint(255,255))
_HpnicfIfQoSQSMinBandwidthPercent_Type.__name__=_J
_HpnicfIfQoSQSMinBandwidthPercent_Object=MibTableColumn
hpnicfIfQoSQSMinBandwidthPercent=_HpnicfIfQoSQSMinBandwidthPercent_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,1,2,1,7),_HpnicfIfQoSQSMinBandwidthPercent_Type())
hpnicfIfQoSQSMinBandwidthPercent.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfIfQoSQSMinBandwidthPercent.setStatus(_A)
_HpnicfIfQoSHardwareQueueRunInfoGroup_ObjectIdentity=ObjectIdentity
hpnicfIfQoSHardwareQueueRunInfoGroup=_HpnicfIfQoSHardwareQueueRunInfoGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2))
_HpnicfIfQoSHardwareQueueRunInfoTable_Object=MibTable
hpnicfIfQoSHardwareQueueRunInfoTable=_HpnicfIfQoSHardwareQueueRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,1))
if mibBuilder.loadTexts:hpnicfIfQoSHardwareQueueRunInfoTable.setStatus(_A)
_HpnicfIfQoSHardwareQueueRunInfoEntry_Object=MibTableRow
hpnicfIfQoSHardwareQueueRunInfoEntry=_HpnicfIfQoSHardwareQueueRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,1,1))
hpnicfIfQoSHardwareQueueRunInfoEntry.setIndexNames((0,_G,_H),(0,_E,_P))
if mibBuilder.loadTexts:hpnicfIfQoSHardwareQueueRunInfoEntry.setStatus(_A)
_HpnicfIfQoSPassPackets_Type=Counter64
_HpnicfIfQoSPassPackets_Object=MibTableColumn
hpnicfIfQoSPassPackets=_HpnicfIfQoSPassPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,1,1,1),_HpnicfIfQoSPassPackets_Type())
hpnicfIfQoSPassPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSPassPackets.setStatus(_A)
_HpnicfIfQoSDropPackets_Type=Counter64
_HpnicfIfQoSDropPackets_Object=MibTableColumn
hpnicfIfQoSDropPackets=_HpnicfIfQoSDropPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,1,1,2),_HpnicfIfQoSDropPackets_Type())
hpnicfIfQoSDropPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSDropPackets.setStatus(_A)
_HpnicfIfQoSPassBytes_Type=Counter64
_HpnicfIfQoSPassBytes_Object=MibTableColumn
hpnicfIfQoSPassBytes=_HpnicfIfQoSPassBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,1,1,3),_HpnicfIfQoSPassBytes_Type())
hpnicfIfQoSPassBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSPassBytes.setStatus(_A)
_HpnicfIfQoSPassPPS_Type=Unsigned32
_HpnicfIfQoSPassPPS_Object=MibTableColumn
hpnicfIfQoSPassPPS=_HpnicfIfQoSPassPPS_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,1,1,4),_HpnicfIfQoSPassPPS_Type())
hpnicfIfQoSPassPPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSPassPPS.setStatus(_A)
_HpnicfIfQoSPassBPS_Type=Unsigned32
_HpnicfIfQoSPassBPS_Object=MibTableColumn
hpnicfIfQoSPassBPS=_HpnicfIfQoSPassBPS_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,1,1,5),_HpnicfIfQoSPassBPS_Type())
hpnicfIfQoSPassBPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSPassBPS.setStatus(_A)
_HpnicfIfQoSDropBytes_Type=Counter64
_HpnicfIfQoSDropBytes_Object=MibTableColumn
hpnicfIfQoSDropBytes=_HpnicfIfQoSDropBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,1,1,6),_HpnicfIfQoSDropBytes_Type())
hpnicfIfQoSDropBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSDropBytes.setStatus(_A)
_HpnicfIfQoSQueueLengthInPkts_Type=Unsigned32
_HpnicfIfQoSQueueLengthInPkts_Object=MibTableColumn
hpnicfIfQoSQueueLengthInPkts=_HpnicfIfQoSQueueLengthInPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,1,1,7),_HpnicfIfQoSQueueLengthInPkts_Type())
hpnicfIfQoSQueueLengthInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSQueueLengthInPkts.setStatus(_A)
_HpnicfIfQoSQueueLengthInBytes_Type=Unsigned32
_HpnicfIfQoSQueueLengthInBytes_Object=MibTableColumn
hpnicfIfQoSQueueLengthInBytes=_HpnicfIfQoSQueueLengthInBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,1,1,8),_HpnicfIfQoSQueueLengthInBytes_Type())
hpnicfIfQoSQueueLengthInBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSQueueLengthInBytes.setStatus(_A)
_HpnicfIfQoSCurQueuePkts_Type=Unsigned32
_HpnicfIfQoSCurQueuePkts_Object=MibTableColumn
hpnicfIfQoSCurQueuePkts=_HpnicfIfQoSCurQueuePkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,1,1,9),_HpnicfIfQoSCurQueuePkts_Type())
hpnicfIfQoSCurQueuePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSCurQueuePkts.setStatus(_A)
_HpnicfIfQoSCurQueueBytes_Type=Unsigned32
_HpnicfIfQoSCurQueueBytes_Object=MibTableColumn
hpnicfIfQoSCurQueueBytes=_HpnicfIfQoSCurQueueBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,1,1,10),_HpnicfIfQoSCurQueueBytes_Type())
hpnicfIfQoSCurQueueBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSCurQueueBytes.setStatus(_A)
_HpnicfIfQoSCurQueuePPS_Type=Unsigned32
_HpnicfIfQoSCurQueuePPS_Object=MibTableColumn
hpnicfIfQoSCurQueuePPS=_HpnicfIfQoSCurQueuePPS_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,1,1,11),_HpnicfIfQoSCurQueuePPS_Type())
hpnicfIfQoSCurQueuePPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSCurQueuePPS.setStatus(_A)
_HpnicfIfQoSCurQueueBPS_Type=Unsigned32
_HpnicfIfQoSCurQueueBPS_Object=MibTableColumn
hpnicfIfQoSCurQueueBPS=_HpnicfIfQoSCurQueueBPS_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,1,1,12),_HpnicfIfQoSCurQueueBPS_Type())
hpnicfIfQoSCurQueueBPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSCurQueueBPS.setStatus(_A)
_HpnicfIfQoSTailDropPkts_Type=Counter64
_HpnicfIfQoSTailDropPkts_Object=MibTableColumn
hpnicfIfQoSTailDropPkts=_HpnicfIfQoSTailDropPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,1,1,13),_HpnicfIfQoSTailDropPkts_Type())
hpnicfIfQoSTailDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSTailDropPkts.setStatus(_A)
_HpnicfIfQoSTailDropBytes_Type=Counter64
_HpnicfIfQoSTailDropBytes_Object=MibTableColumn
hpnicfIfQoSTailDropBytes=_HpnicfIfQoSTailDropBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,1,1,14),_HpnicfIfQoSTailDropBytes_Type())
hpnicfIfQoSTailDropBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSTailDropBytes.setStatus(_A)
_HpnicfIfQoSTailDropPPS_Type=Unsigned32
_HpnicfIfQoSTailDropPPS_Object=MibTableColumn
hpnicfIfQoSTailDropPPS=_HpnicfIfQoSTailDropPPS_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,1,1,15),_HpnicfIfQoSTailDropPPS_Type())
hpnicfIfQoSTailDropPPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSTailDropPPS.setStatus(_A)
_HpnicfIfQoSTailDropBPS_Type=Unsigned32
_HpnicfIfQoSTailDropBPS_Object=MibTableColumn
hpnicfIfQoSTailDropBPS=_HpnicfIfQoSTailDropBPS_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,1,1,16),_HpnicfIfQoSTailDropBPS_Type())
hpnicfIfQoSTailDropBPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSTailDropBPS.setStatus(_A)
_HpnicfIfQoSWredDropPkts_Type=Counter64
_HpnicfIfQoSWredDropPkts_Object=MibTableColumn
hpnicfIfQoSWredDropPkts=_HpnicfIfQoSWredDropPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,1,1,17),_HpnicfIfQoSWredDropPkts_Type())
hpnicfIfQoSWredDropPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWredDropPkts.setStatus(_A)
_HpnicfIfQoSWredDropBytes_Type=Counter64
_HpnicfIfQoSWredDropBytes_Object=MibTableColumn
hpnicfIfQoSWredDropBytes=_HpnicfIfQoSWredDropBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,1,1,18),_HpnicfIfQoSWredDropBytes_Type())
hpnicfIfQoSWredDropBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWredDropBytes.setStatus(_A)
_HpnicfIfQoSWredDropPPS_Type=Unsigned32
_HpnicfIfQoSWredDropPPS_Object=MibTableColumn
hpnicfIfQoSWredDropPPS=_HpnicfIfQoSWredDropPPS_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,1,1,19),_HpnicfIfQoSWredDropPPS_Type())
hpnicfIfQoSWredDropPPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWredDropPPS.setStatus(_A)
_HpnicfIfQoSWredDropBPS_Type=Unsigned32
_HpnicfIfQoSWredDropBPS_Object=MibTableColumn
hpnicfIfQoSWredDropBPS=_HpnicfIfQoSWredDropBPS_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,1,1,20),_HpnicfIfQoSWredDropBPS_Type())
hpnicfIfQoSWredDropBPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWredDropBPS.setStatus(_A)
_HpnicfIfQoSHQueueTcpRunInfoTable_Object=MibTable
hpnicfIfQoSHQueueTcpRunInfoTable=_HpnicfIfQoSHQueueTcpRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,2))
if mibBuilder.loadTexts:hpnicfIfQoSHQueueTcpRunInfoTable.setStatus(_A)
_HpnicfIfQoSHQueueTcpRunInfoEntry_Object=MibTableRow
hpnicfIfQoSHQueueTcpRunInfoEntry=_HpnicfIfQoSHQueueTcpRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,2,1))
hpnicfIfQoSHQueueTcpRunInfoEntry.setIndexNames((0,_G,_H),(0,_E,_P))
if mibBuilder.loadTexts:hpnicfIfQoSHQueueTcpRunInfoEntry.setStatus(_A)
_HpnicfIfQoSWredDropLPreNTcpPkts_Type=Counter64
_HpnicfIfQoSWredDropLPreNTcpPkts_Object=MibTableColumn
hpnicfIfQoSWredDropLPreNTcpPkts=_HpnicfIfQoSWredDropLPreNTcpPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,2,1,1),_HpnicfIfQoSWredDropLPreNTcpPkts_Type())
hpnicfIfQoSWredDropLPreNTcpPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWredDropLPreNTcpPkts.setStatus(_A)
_HpnicfIfQoSWredDropLPreNTcpBytes_Type=Counter64
_HpnicfIfQoSWredDropLPreNTcpBytes_Object=MibTableColumn
hpnicfIfQoSWredDropLPreNTcpBytes=_HpnicfIfQoSWredDropLPreNTcpBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,2,1,2),_HpnicfIfQoSWredDropLPreNTcpBytes_Type())
hpnicfIfQoSWredDropLPreNTcpBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWredDropLPreNTcpBytes.setStatus(_A)
_HpnicfIfQoSWredDropLPreNTcpPPS_Type=Unsigned32
_HpnicfIfQoSWredDropLPreNTcpPPS_Object=MibTableColumn
hpnicfIfQoSWredDropLPreNTcpPPS=_HpnicfIfQoSWredDropLPreNTcpPPS_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,2,1,3),_HpnicfIfQoSWredDropLPreNTcpPPS_Type())
hpnicfIfQoSWredDropLPreNTcpPPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWredDropLPreNTcpPPS.setStatus(_A)
_HpnicfIfQoSWredDropLPreNTcpBPS_Type=Unsigned32
_HpnicfIfQoSWredDropLPreNTcpBPS_Object=MibTableColumn
hpnicfIfQoSWredDropLPreNTcpBPS=_HpnicfIfQoSWredDropLPreNTcpBPS_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,2,1,4),_HpnicfIfQoSWredDropLPreNTcpBPS_Type())
hpnicfIfQoSWredDropLPreNTcpBPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWredDropLPreNTcpBPS.setStatus(_A)
_HpnicfIfQoSWredDropLPreTcpPkts_Type=Counter64
_HpnicfIfQoSWredDropLPreTcpPkts_Object=MibTableColumn
hpnicfIfQoSWredDropLPreTcpPkts=_HpnicfIfQoSWredDropLPreTcpPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,2,1,5),_HpnicfIfQoSWredDropLPreTcpPkts_Type())
hpnicfIfQoSWredDropLPreTcpPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWredDropLPreTcpPkts.setStatus(_A)
_HpnicfIfQoSWredDropLPreTcpBytes_Type=Counter64
_HpnicfIfQoSWredDropLPreTcpBytes_Object=MibTableColumn
hpnicfIfQoSWredDropLPreTcpBytes=_HpnicfIfQoSWredDropLPreTcpBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,2,1,6),_HpnicfIfQoSWredDropLPreTcpBytes_Type())
hpnicfIfQoSWredDropLPreTcpBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWredDropLPreTcpBytes.setStatus(_A)
_HpnicfIfQoSWredDropLPreTcpPPS_Type=Unsigned32
_HpnicfIfQoSWredDropLPreTcpPPS_Object=MibTableColumn
hpnicfIfQoSWredDropLPreTcpPPS=_HpnicfIfQoSWredDropLPreTcpPPS_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,2,1,7),_HpnicfIfQoSWredDropLPreTcpPPS_Type())
hpnicfIfQoSWredDropLPreTcpPPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWredDropLPreTcpPPS.setStatus(_A)
_HpnicfIfQoSWredDropLPreTcpBPS_Type=Unsigned32
_HpnicfIfQoSWredDropLPreTcpBPS_Object=MibTableColumn
hpnicfIfQoSWredDropLPreTcpBPS=_HpnicfIfQoSWredDropLPreTcpBPS_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,2,1,8),_HpnicfIfQoSWredDropLPreTcpBPS_Type())
hpnicfIfQoSWredDropLPreTcpBPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWredDropLPreTcpBPS.setStatus(_A)
_HpnicfIfQoSWredDropHPreNTcpPkts_Type=Counter64
_HpnicfIfQoSWredDropHPreNTcpPkts_Object=MibTableColumn
hpnicfIfQoSWredDropHPreNTcpPkts=_HpnicfIfQoSWredDropHPreNTcpPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,2,1,9),_HpnicfIfQoSWredDropHPreNTcpPkts_Type())
hpnicfIfQoSWredDropHPreNTcpPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWredDropHPreNTcpPkts.setStatus(_A)
_HpnicfIfQoSWredDropHPreNTcpBytes_Type=Counter64
_HpnicfIfQoSWredDropHPreNTcpBytes_Object=MibTableColumn
hpnicfIfQoSWredDropHPreNTcpBytes=_HpnicfIfQoSWredDropHPreNTcpBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,2,1,10),_HpnicfIfQoSWredDropHPreNTcpBytes_Type())
hpnicfIfQoSWredDropHPreNTcpBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWredDropHPreNTcpBytes.setStatus(_A)
_HpnicfIfQoSWredDropHPreNTcpPPS_Type=Unsigned32
_HpnicfIfQoSWredDropHPreNTcpPPS_Object=MibTableColumn
hpnicfIfQoSWredDropHPreNTcpPPS=_HpnicfIfQoSWredDropHPreNTcpPPS_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,2,1,11),_HpnicfIfQoSWredDropHPreNTcpPPS_Type())
hpnicfIfQoSWredDropHPreNTcpPPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWredDropHPreNTcpPPS.setStatus(_A)
_HpnicfIfQoSWredDropHPreNTcpBPS_Type=Unsigned32
_HpnicfIfQoSWredDropHPreNTcpBPS_Object=MibTableColumn
hpnicfIfQoSWredDropHPreNTcpBPS=_HpnicfIfQoSWredDropHPreNTcpBPS_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,2,1,12),_HpnicfIfQoSWredDropHPreNTcpBPS_Type())
hpnicfIfQoSWredDropHPreNTcpBPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWredDropHPreNTcpBPS.setStatus(_A)
_HpnicfIfQoSWredDropHPreTcpPkts_Type=Counter64
_HpnicfIfQoSWredDropHPreTcpPkts_Object=MibTableColumn
hpnicfIfQoSWredDropHPreTcpPkts=_HpnicfIfQoSWredDropHPreTcpPkts_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,2,1,13),_HpnicfIfQoSWredDropHPreTcpPkts_Type())
hpnicfIfQoSWredDropHPreTcpPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWredDropHPreTcpPkts.setStatus(_A)
_HpnicfIfQoSWredDropHPreTcpBytes_Type=Counter64
_HpnicfIfQoSWredDropHPreTcpBytes_Object=MibTableColumn
hpnicfIfQoSWredDropHPreTcpBytes=_HpnicfIfQoSWredDropHPreTcpBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,2,1,14),_HpnicfIfQoSWredDropHPreTcpBytes_Type())
hpnicfIfQoSWredDropHPreTcpBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWredDropHPreTcpBytes.setStatus(_A)
_HpnicfIfQoSWredDropHPreTcpPPS_Type=Unsigned32
_HpnicfIfQoSWredDropHPreTcpPPS_Object=MibTableColumn
hpnicfIfQoSWredDropHPreTcpPPS=_HpnicfIfQoSWredDropHPreTcpPPS_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,2,1,15),_HpnicfIfQoSWredDropHPreTcpPPS_Type())
hpnicfIfQoSWredDropHPreTcpPPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWredDropHPreTcpPPS.setStatus(_A)
_HpnicfIfQoSWredDropHPreTcpBPS_Type=Unsigned32
_HpnicfIfQoSWredDropHPreTcpBPS_Object=MibTableColumn
hpnicfIfQoSWredDropHPreTcpBPS=_HpnicfIfQoSWredDropHPreTcpBPS_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,1,2,2,1,16),_HpnicfIfQoSWredDropHPreTcpBPS_Type())
hpnicfIfQoSWredDropHPreTcpBPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWredDropHPreTcpBPS.setStatus(_A)
_HpnicfIfQoSSoftwareQueueObjects_ObjectIdentity=ObjectIdentity
hpnicfIfQoSSoftwareQueueObjects=_HpnicfIfQoSSoftwareQueueObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2))
_HpnicfIfQoSFIFOObject_ObjectIdentity=ObjectIdentity
hpnicfIfQoSFIFOObject=_HpnicfIfQoSFIFOObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,1))
_HpnicfIfQoSFIFOConfigTable_Object=MibTable
hpnicfIfQoSFIFOConfigTable=_HpnicfIfQoSFIFOConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,1,1))
if mibBuilder.loadTexts:hpnicfIfQoSFIFOConfigTable.setStatus(_A)
_HpnicfIfQoSFIFOConfigEntry_Object=MibTableRow
hpnicfIfQoSFIFOConfigEntry=_HpnicfIfQoSFIFOConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,1,1,1))
hpnicfIfQoSFIFOConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hpnicfIfQoSFIFOConfigEntry.setStatus(_A)
_HpnicfIfQoSFIFOMaxQueueLen_Type=Integer32
_HpnicfIfQoSFIFOMaxQueueLen_Object=MibTableColumn
hpnicfIfQoSFIFOMaxQueueLen=_HpnicfIfQoSFIFOMaxQueueLen_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,1,1,1,1),_HpnicfIfQoSFIFOMaxQueueLen_Type())
hpnicfIfQoSFIFOMaxQueueLen.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfIfQoSFIFOMaxQueueLen.setStatus(_A)
_HpnicfIfQoSFIFORunInfoTable_Object=MibTable
hpnicfIfQoSFIFORunInfoTable=_HpnicfIfQoSFIFORunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,1,2))
if mibBuilder.loadTexts:hpnicfIfQoSFIFORunInfoTable.setStatus(_A)
_HpnicfIfQoSFIFORunInfoEntry_Object=MibTableRow
hpnicfIfQoSFIFORunInfoEntry=_HpnicfIfQoSFIFORunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,1,2,1))
hpnicfIfQoSFIFORunInfoEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hpnicfIfQoSFIFORunInfoEntry.setStatus(_A)
_HpnicfIfQoSFIFOSize_Type=Integer32
_HpnicfIfQoSFIFOSize_Object=MibTableColumn
hpnicfIfQoSFIFOSize=_HpnicfIfQoSFIFOSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,1,2,1,1),_HpnicfIfQoSFIFOSize_Type())
hpnicfIfQoSFIFOSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSFIFOSize.setStatus(_A)
_HpnicfIfQoSFIFODiscardPackets_Type=Counter64
_HpnicfIfQoSFIFODiscardPackets_Object=MibTableColumn
hpnicfIfQoSFIFODiscardPackets=_HpnicfIfQoSFIFODiscardPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,1,2,1,2),_HpnicfIfQoSFIFODiscardPackets_Type())
hpnicfIfQoSFIFODiscardPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSFIFODiscardPackets.setStatus(_A)
_HpnicfIfQoSPQObject_ObjectIdentity=ObjectIdentity
hpnicfIfQoSPQObject=_HpnicfIfQoSPQObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2))
_HpnicfIfQoSPQConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfIfQoSPQConfigGroup=_HpnicfIfQoSPQConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,1))
_HpnicfIfQoSPQDefaultTable_Object=MibTable
hpnicfIfQoSPQDefaultTable=_HpnicfIfQoSPQDefaultTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,1,1))
if mibBuilder.loadTexts:hpnicfIfQoSPQDefaultTable.setStatus(_A)
_HpnicfIfQoSPQDefaultEntry_Object=MibTableRow
hpnicfIfQoSPQDefaultEntry=_HpnicfIfQoSPQDefaultEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,1,1,1))
hpnicfIfQoSPQDefaultEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:hpnicfIfQoSPQDefaultEntry.setStatus(_A)
class _HpnicfIfQoSPQListNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HpnicfIfQoSPQListNumber_Type.__name__=_D
_HpnicfIfQoSPQListNumber_Object=MibTableColumn
hpnicfIfQoSPQListNumber=_HpnicfIfQoSPQListNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,1,1,1,1),_HpnicfIfQoSPQListNumber_Type())
hpnicfIfQoSPQListNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSPQListNumber.setStatus(_A)
_HpnicfIfQoSPQDefaultQueueType_Type=PriorityQueue
_HpnicfIfQoSPQDefaultQueueType_Object=MibTableColumn
hpnicfIfQoSPQDefaultQueueType=_HpnicfIfQoSPQDefaultQueueType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,1,1,1,2),_HpnicfIfQoSPQDefaultQueueType_Type())
hpnicfIfQoSPQDefaultQueueType.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfIfQoSPQDefaultQueueType.setStatus(_A)
_HpnicfIfQoSPQQueueLengthTable_Object=MibTable
hpnicfIfQoSPQQueueLengthTable=_HpnicfIfQoSPQQueueLengthTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,1,2))
if mibBuilder.loadTexts:hpnicfIfQoSPQQueueLengthTable.setStatus(_A)
_HpnicfIfQoSPQQueueLengthEntry_Object=MibTableRow
hpnicfIfQoSPQQueueLengthEntry=_HpnicfIfQoSPQQueueLengthEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,1,2,1))
hpnicfIfQoSPQQueueLengthEntry.setIndexNames((0,_E,_Q),(0,_E,_l))
if mibBuilder.loadTexts:hpnicfIfQoSPQQueueLengthEntry.setStatus(_A)
_HpnicfIfQoSPQQueueLengthType_Type=PriorityQueue
_HpnicfIfQoSPQQueueLengthType_Object=MibTableColumn
hpnicfIfQoSPQQueueLengthType=_HpnicfIfQoSPQQueueLengthType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,1,2,1,1),_HpnicfIfQoSPQQueueLengthType_Type())
hpnicfIfQoSPQQueueLengthType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSPQQueueLengthType.setStatus(_A)
class _HpnicfIfQoSPQQueueLengthValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_HpnicfIfQoSPQQueueLengthValue_Type.__name__=_D
_HpnicfIfQoSPQQueueLengthValue_Object=MibTableColumn
hpnicfIfQoSPQQueueLengthValue=_HpnicfIfQoSPQQueueLengthValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,1,2,1,2),_HpnicfIfQoSPQQueueLengthValue_Type())
hpnicfIfQoSPQQueueLengthValue.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfIfQoSPQQueueLengthValue.setStatus(_A)
_HpnicfIfQoSPQClassRuleTable_Object=MibTable
hpnicfIfQoSPQClassRuleTable=_HpnicfIfQoSPQClassRuleTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,1,3))
if mibBuilder.loadTexts:hpnicfIfQoSPQClassRuleTable.setStatus(_A)
_HpnicfIfQoSPQClassRuleEntry_Object=MibTableRow
hpnicfIfQoSPQClassRuleEntry=_HpnicfIfQoSPQClassRuleEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,1,3,1))
hpnicfIfQoSPQClassRuleEntry.setIndexNames((0,_E,_Q),(0,_E,_m),(0,_E,_n))
if mibBuilder.loadTexts:hpnicfIfQoSPQClassRuleEntry.setStatus(_A)
class _HpnicfIfQoSPQClassRuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_o,1),(_L,2),(_M,3),(_p,4),(_q,5),(_r,6),('tcp',7),('udp',8),('ipall',9),('mpls',10)))
_HpnicfIfQoSPQClassRuleType_Type.__name__=_D
_HpnicfIfQoSPQClassRuleType_Object=MibTableColumn
hpnicfIfQoSPQClassRuleType=_HpnicfIfQoSPQClassRuleType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,1,3,1,1),_HpnicfIfQoSPQClassRuleType_Type())
hpnicfIfQoSPQClassRuleType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSPQClassRuleType.setStatus(_A)
_HpnicfIfQoSPQClassRuleValue_Type=Integer32
_HpnicfIfQoSPQClassRuleValue_Object=MibTableColumn
hpnicfIfQoSPQClassRuleValue=_HpnicfIfQoSPQClassRuleValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,1,3,1,2),_HpnicfIfQoSPQClassRuleValue_Type())
hpnicfIfQoSPQClassRuleValue.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSPQClassRuleValue.setStatus(_A)
_HpnicfIfQoSPQClassRuleQueueType_Type=PriorityQueue
_HpnicfIfQoSPQClassRuleQueueType_Object=MibTableColumn
hpnicfIfQoSPQClassRuleQueueType=_HpnicfIfQoSPQClassRuleQueueType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,1,3,1,3),_HpnicfIfQoSPQClassRuleQueueType_Type())
hpnicfIfQoSPQClassRuleQueueType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSPQClassRuleQueueType.setStatus(_A)
_HpnicfIfQoSPQClassRowStatus_Type=RowStatus
_HpnicfIfQoSPQClassRowStatus_Object=MibTableColumn
hpnicfIfQoSPQClassRowStatus=_HpnicfIfQoSPQClassRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,1,3,1,4),_HpnicfIfQoSPQClassRowStatus_Type())
hpnicfIfQoSPQClassRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSPQClassRowStatus.setStatus(_A)
_HpnicfIfQoSPQApplyTable_Object=MibTable
hpnicfIfQoSPQApplyTable=_HpnicfIfQoSPQApplyTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,1,4))
if mibBuilder.loadTexts:hpnicfIfQoSPQApplyTable.setStatus(_A)
_HpnicfIfQoSPQApplyEntry_Object=MibTableRow
hpnicfIfQoSPQApplyEntry=_HpnicfIfQoSPQApplyEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,1,4,1))
hpnicfIfQoSPQApplyEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hpnicfIfQoSPQApplyEntry.setStatus(_A)
class _HpnicfIfQoSPQApplyListNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HpnicfIfQoSPQApplyListNumber_Type.__name__=_D
_HpnicfIfQoSPQApplyListNumber_Object=MibTableColumn
hpnicfIfQoSPQApplyListNumber=_HpnicfIfQoSPQApplyListNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,1,4,1,1),_HpnicfIfQoSPQApplyListNumber_Type())
hpnicfIfQoSPQApplyListNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSPQApplyListNumber.setStatus(_A)
_HpnicfIfQoSPQApplyRowStatus_Type=RowStatus
_HpnicfIfQoSPQApplyRowStatus_Object=MibTableColumn
hpnicfIfQoSPQApplyRowStatus=_HpnicfIfQoSPQApplyRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,1,4,1,2),_HpnicfIfQoSPQApplyRowStatus_Type())
hpnicfIfQoSPQApplyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSPQApplyRowStatus.setStatus(_A)
_HpnicfIfQoSPQRunInfoGroup_ObjectIdentity=ObjectIdentity
hpnicfIfQoSPQRunInfoGroup=_HpnicfIfQoSPQRunInfoGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,2))
_HpnicfIfQoSPQRunInfoTable_Object=MibTable
hpnicfIfQoSPQRunInfoTable=_HpnicfIfQoSPQRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,2,1))
if mibBuilder.loadTexts:hpnicfIfQoSPQRunInfoTable.setStatus(_A)
_HpnicfIfQoSPQRunInfoEntry_Object=MibTableRow
hpnicfIfQoSPQRunInfoEntry=_HpnicfIfQoSPQRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,2,1,1))
hpnicfIfQoSPQRunInfoEntry.setIndexNames((0,_G,_H),(0,_E,_s))
if mibBuilder.loadTexts:hpnicfIfQoSPQRunInfoEntry.setStatus(_A)
_HpnicfIfQoSPQType_Type=PriorityQueue
_HpnicfIfQoSPQType_Object=MibTableColumn
hpnicfIfQoSPQType=_HpnicfIfQoSPQType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,2,1,1,1),_HpnicfIfQoSPQType_Type())
hpnicfIfQoSPQType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSPQType.setStatus(_A)
_HpnicfIfQoSPQSize_Type=Integer32
_HpnicfIfQoSPQSize_Object=MibTableColumn
hpnicfIfQoSPQSize=_HpnicfIfQoSPQSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,2,1,1,2),_HpnicfIfQoSPQSize_Type())
hpnicfIfQoSPQSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSPQSize.setStatus(_A)
_HpnicfIfQoSPQLength_Type=Integer32
_HpnicfIfQoSPQLength_Object=MibTableColumn
hpnicfIfQoSPQLength=_HpnicfIfQoSPQLength_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,2,1,1,3),_HpnicfIfQoSPQLength_Type())
hpnicfIfQoSPQLength.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSPQLength.setStatus(_A)
_HpnicfIfQoSPQDiscardPackets_Type=Counter64
_HpnicfIfQoSPQDiscardPackets_Object=MibTableColumn
hpnicfIfQoSPQDiscardPackets=_HpnicfIfQoSPQDiscardPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,2,2,1,1,4),_HpnicfIfQoSPQDiscardPackets_Type())
hpnicfIfQoSPQDiscardPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSPQDiscardPackets.setStatus(_A)
_HpnicfIfQoSCQObject_ObjectIdentity=ObjectIdentity
hpnicfIfQoSCQObject=_HpnicfIfQoSCQObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3))
_HpnicfIfQoSCQConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfIfQoSCQConfigGroup=_HpnicfIfQoSCQConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,1))
_HpnicfIfQoSCQDefaultTable_Object=MibTable
hpnicfIfQoSCQDefaultTable=_HpnicfIfQoSCQDefaultTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,1,1))
if mibBuilder.loadTexts:hpnicfIfQoSCQDefaultTable.setStatus(_A)
_HpnicfIfQoSCQDefaultEntry_Object=MibTableRow
hpnicfIfQoSCQDefaultEntry=_HpnicfIfQoSCQDefaultEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,1,1,1))
hpnicfIfQoSCQDefaultEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:hpnicfIfQoSCQDefaultEntry.setStatus(_A)
class _HpnicfIfQoSCQListNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HpnicfIfQoSCQListNumber_Type.__name__=_D
_HpnicfIfQoSCQListNumber_Object=MibTableColumn
hpnicfIfQoSCQListNumber=_HpnicfIfQoSCQListNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,1,1,1,1),_HpnicfIfQoSCQListNumber_Type())
hpnicfIfQoSCQListNumber.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSCQListNumber.setStatus(_A)
class _HpnicfIfQoSCQDefaultQueueID_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16))
_HpnicfIfQoSCQDefaultQueueID_Type.__name__=_D
_HpnicfIfQoSCQDefaultQueueID_Object=MibTableColumn
hpnicfIfQoSCQDefaultQueueID=_HpnicfIfQoSCQDefaultQueueID_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,1,1,1,2),_HpnicfIfQoSCQDefaultQueueID_Type())
hpnicfIfQoSCQDefaultQueueID.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfIfQoSCQDefaultQueueID.setStatus(_A)
_HpnicfIfQoSCQQueueLengthTable_Object=MibTable
hpnicfIfQoSCQQueueLengthTable=_HpnicfIfQoSCQQueueLengthTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,1,2))
if mibBuilder.loadTexts:hpnicfIfQoSCQQueueLengthTable.setStatus(_A)
_HpnicfIfQoSCQQueueLengthEntry_Object=MibTableRow
hpnicfIfQoSCQQueueLengthEntry=_HpnicfIfQoSCQQueueLengthEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,1,2,1))
hpnicfIfQoSCQQueueLengthEntry.setIndexNames((0,_E,_R),(0,_E,_T))
if mibBuilder.loadTexts:hpnicfIfQoSCQQueueLengthEntry.setStatus(_A)
class _HpnicfIfQoSCQQueueID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HpnicfIfQoSCQQueueID_Type.__name__=_D
_HpnicfIfQoSCQQueueID_Object=MibTableColumn
hpnicfIfQoSCQQueueID=_HpnicfIfQoSCQQueueID_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,1,2,1,1),_HpnicfIfQoSCQQueueID_Type())
hpnicfIfQoSCQQueueID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSCQQueueID.setStatus(_A)
class _HpnicfIfQoSCQQueueLength_Type(Integer32):defaultValue=20;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_HpnicfIfQoSCQQueueLength_Type.__name__=_D
_HpnicfIfQoSCQQueueLength_Object=MibTableColumn
hpnicfIfQoSCQQueueLength=_HpnicfIfQoSCQQueueLength_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,1,2,1,2),_HpnicfIfQoSCQQueueLength_Type())
hpnicfIfQoSCQQueueLength.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfIfQoSCQQueueLength.setStatus(_A)
class _HpnicfIfQoSCQQueueServing_Type(Integer32):defaultValue=1500
_HpnicfIfQoSCQQueueServing_Type.__name__=_D
_HpnicfIfQoSCQQueueServing_Object=MibTableColumn
hpnicfIfQoSCQQueueServing=_HpnicfIfQoSCQQueueServing_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,1,2,1,3),_HpnicfIfQoSCQQueueServing_Type())
hpnicfIfQoSCQQueueServing.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfIfQoSCQQueueServing.setStatus(_A)
_HpnicfIfQoSCQClassRuleTable_Object=MibTable
hpnicfIfQoSCQClassRuleTable=_HpnicfIfQoSCQClassRuleTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,1,3))
if mibBuilder.loadTexts:hpnicfIfQoSCQClassRuleTable.setStatus(_A)
_HpnicfIfQoSCQClassRuleEntry_Object=MibTableRow
hpnicfIfQoSCQClassRuleEntry=_HpnicfIfQoSCQClassRuleEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,1,3,1))
hpnicfIfQoSCQClassRuleEntry.setIndexNames((0,_E,_R),(0,_E,_t),(0,_E,_u))
if mibBuilder.loadTexts:hpnicfIfQoSCQClassRuleEntry.setStatus(_A)
class _HpnicfIfQoSCQClassRuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_o,1),(_L,2),(_M,3),(_p,4),(_q,5),(_r,6),('tcp',7),('udp',8),('ipall',9),('mpls',10)))
_HpnicfIfQoSCQClassRuleType_Type.__name__=_D
_HpnicfIfQoSCQClassRuleType_Object=MibTableColumn
hpnicfIfQoSCQClassRuleType=_HpnicfIfQoSCQClassRuleType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,1,3,1,1),_HpnicfIfQoSCQClassRuleType_Type())
hpnicfIfQoSCQClassRuleType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSCQClassRuleType.setStatus(_A)
_HpnicfIfQoSCQClassRuleValue_Type=Integer32
_HpnicfIfQoSCQClassRuleValue_Object=MibTableColumn
hpnicfIfQoSCQClassRuleValue=_HpnicfIfQoSCQClassRuleValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,1,3,1,2),_HpnicfIfQoSCQClassRuleValue_Type())
hpnicfIfQoSCQClassRuleValue.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSCQClassRuleValue.setStatus(_A)
class _HpnicfIfQoSCQClassRuleQueueID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HpnicfIfQoSCQClassRuleQueueID_Type.__name__=_D
_HpnicfIfQoSCQClassRuleQueueID_Object=MibTableColumn
hpnicfIfQoSCQClassRuleQueueID=_HpnicfIfQoSCQClassRuleQueueID_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,1,3,1,3),_HpnicfIfQoSCQClassRuleQueueID_Type())
hpnicfIfQoSCQClassRuleQueueID.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSCQClassRuleQueueID.setStatus(_A)
_HpnicfIfQoSCQClassRowStatus_Type=RowStatus
_HpnicfIfQoSCQClassRowStatus_Object=MibTableColumn
hpnicfIfQoSCQClassRowStatus=_HpnicfIfQoSCQClassRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,1,3,1,4),_HpnicfIfQoSCQClassRowStatus_Type())
hpnicfIfQoSCQClassRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSCQClassRowStatus.setStatus(_A)
_HpnicfIfQoSCQApplyTable_Object=MibTable
hpnicfIfQoSCQApplyTable=_HpnicfIfQoSCQApplyTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,1,4))
if mibBuilder.loadTexts:hpnicfIfQoSCQApplyTable.setStatus(_A)
_HpnicfIfQoSCQApplyEntry_Object=MibTableRow
hpnicfIfQoSCQApplyEntry=_HpnicfIfQoSCQApplyEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,1,4,1))
hpnicfIfQoSCQApplyEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hpnicfIfQoSCQApplyEntry.setStatus(_A)
class _HpnicfIfQoSCQApplyListNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HpnicfIfQoSCQApplyListNumber_Type.__name__=_D
_HpnicfIfQoSCQApplyListNumber_Object=MibTableColumn
hpnicfIfQoSCQApplyListNumber=_HpnicfIfQoSCQApplyListNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,1,4,1,1),_HpnicfIfQoSCQApplyListNumber_Type())
hpnicfIfQoSCQApplyListNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSCQApplyListNumber.setStatus(_A)
_HpnicfIfQoSCQApplyRowStatus_Type=RowStatus
_HpnicfIfQoSCQApplyRowStatus_Object=MibTableColumn
hpnicfIfQoSCQApplyRowStatus=_HpnicfIfQoSCQApplyRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,1,4,1,2),_HpnicfIfQoSCQApplyRowStatus_Type())
hpnicfIfQoSCQApplyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSCQApplyRowStatus.setStatus(_A)
_HpnicfIfQoSCQRunInfoGroup_ObjectIdentity=ObjectIdentity
hpnicfIfQoSCQRunInfoGroup=_HpnicfIfQoSCQRunInfoGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,2))
_HpnicfIfQoSCQRunInfoTable_Object=MibTable
hpnicfIfQoSCQRunInfoTable=_HpnicfIfQoSCQRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,2,1))
if mibBuilder.loadTexts:hpnicfIfQoSCQRunInfoTable.setStatus(_A)
_HpnicfIfQoSCQRunInfoEntry_Object=MibTableRow
hpnicfIfQoSCQRunInfoEntry=_HpnicfIfQoSCQRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,2,1,1))
hpnicfIfQoSCQRunInfoEntry.setIndexNames((0,_G,_H),(0,_E,_T))
if mibBuilder.loadTexts:hpnicfIfQoSCQRunInfoEntry.setStatus(_A)
_HpnicfIfQoSCQRunInfoSize_Type=Integer32
_HpnicfIfQoSCQRunInfoSize_Object=MibTableColumn
hpnicfIfQoSCQRunInfoSize=_HpnicfIfQoSCQRunInfoSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,2,1,1,1),_HpnicfIfQoSCQRunInfoSize_Type())
hpnicfIfQoSCQRunInfoSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSCQRunInfoSize.setStatus(_A)
_HpnicfIfQoSCQRunInfoLength_Type=Integer32
_HpnicfIfQoSCQRunInfoLength_Object=MibTableColumn
hpnicfIfQoSCQRunInfoLength=_HpnicfIfQoSCQRunInfoLength_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,2,1,1,2),_HpnicfIfQoSCQRunInfoLength_Type())
hpnicfIfQoSCQRunInfoLength.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSCQRunInfoLength.setStatus(_A)
_HpnicfIfQoSCQRunInfoDiscardPackets_Type=Counter64
_HpnicfIfQoSCQRunInfoDiscardPackets_Object=MibTableColumn
hpnicfIfQoSCQRunInfoDiscardPackets=_HpnicfIfQoSCQRunInfoDiscardPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,3,2,1,1,3),_HpnicfIfQoSCQRunInfoDiscardPackets_Type())
hpnicfIfQoSCQRunInfoDiscardPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSCQRunInfoDiscardPackets.setStatus(_A)
_HpnicfIfQoSWFQObject_ObjectIdentity=ObjectIdentity
hpnicfIfQoSWFQObject=_HpnicfIfQoSWFQObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,4))
_HpnicfIfQoSWFQConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfIfQoSWFQConfigGroup=_HpnicfIfQoSWFQConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,4,1))
_HpnicfIfQoSWFQTable_Object=MibTable
hpnicfIfQoSWFQTable=_HpnicfIfQoSWFQTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,4,1,1))
if mibBuilder.loadTexts:hpnicfIfQoSWFQTable.setStatus(_A)
_HpnicfIfQoSWFQEntry_Object=MibTableRow
hpnicfIfQoSWFQEntry=_HpnicfIfQoSWFQEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,4,1,1,1))
hpnicfIfQoSWFQEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hpnicfIfQoSWFQEntry.setStatus(_A)
class _HpnicfIfQoSWFQQueueLength_Type(Integer32):defaultValue=64;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_HpnicfIfQoSWFQQueueLength_Type.__name__=_D
_HpnicfIfQoSWFQQueueLength_Object=MibTableColumn
hpnicfIfQoSWFQQueueLength=_HpnicfIfQoSWFQQueueLength_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,4,1,1,1,1),_HpnicfIfQoSWFQQueueLength_Type())
hpnicfIfQoSWFQQueueLength.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSWFQQueueLength.setStatus(_A)
class _HpnicfIfQoSWFQQueueNumber_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('size16',1),('size32',2),('size64',3),('size128',4),('size256',5),('size512',6),('size1024',7),('size2048',8),('size4096',9)))
_HpnicfIfQoSWFQQueueNumber_Type.__name__=_D
_HpnicfIfQoSWFQQueueNumber_Object=MibTableColumn
hpnicfIfQoSWFQQueueNumber=_HpnicfIfQoSWFQQueueNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,4,1,1,1,2),_HpnicfIfQoSWFQQueueNumber_Type())
hpnicfIfQoSWFQQueueNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSWFQQueueNumber.setStatus(_A)
_HpnicfIfQoSWFQRowStatus_Type=RowStatus
_HpnicfIfQoSWFQRowStatus_Object=MibTableColumn
hpnicfIfQoSWFQRowStatus=_HpnicfIfQoSWFQRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,4,1,1,1,3),_HpnicfIfQoSWFQRowStatus_Type())
hpnicfIfQoSWFQRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSWFQRowStatus.setStatus(_A)
class _HpnicfIfQoSWFQType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ip-precedence',1),(_N,2)))
_HpnicfIfQoSWFQType_Type.__name__=_D
_HpnicfIfQoSWFQType_Object=MibTableColumn
hpnicfIfQoSWFQType=_HpnicfIfQoSWFQType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,4,1,1,1,4),_HpnicfIfQoSWFQType_Type())
hpnicfIfQoSWFQType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSWFQType.setStatus(_A)
_HpnicfIfQoSWFQRunInfoGroup_ObjectIdentity=ObjectIdentity
hpnicfIfQoSWFQRunInfoGroup=_HpnicfIfQoSWFQRunInfoGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,4,2))
_HpnicfIfQoSWFQRunInfoTable_Object=MibTable
hpnicfIfQoSWFQRunInfoTable=_HpnicfIfQoSWFQRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,4,2,1))
if mibBuilder.loadTexts:hpnicfIfQoSWFQRunInfoTable.setStatus(_A)
_HpnicfIfQoSWFQRunInfoEntry_Object=MibTableRow
hpnicfIfQoSWFQRunInfoEntry=_HpnicfIfQoSWFQRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,4,2,1,1))
hpnicfIfQoSWFQRunInfoEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hpnicfIfQoSWFQRunInfoEntry.setStatus(_A)
_HpnicfIfQoSWFQSize_Type=Integer32
_HpnicfIfQoSWFQSize_Object=MibTableColumn
hpnicfIfQoSWFQSize=_HpnicfIfQoSWFQSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,4,2,1,1,1),_HpnicfIfQoSWFQSize_Type())
hpnicfIfQoSWFQSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWFQSize.setStatus(_A)
_HpnicfIfQoSWFQLength_Type=Integer32
_HpnicfIfQoSWFQLength_Object=MibTableColumn
hpnicfIfQoSWFQLength=_HpnicfIfQoSWFQLength_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,4,2,1,1,2),_HpnicfIfQoSWFQLength_Type())
hpnicfIfQoSWFQLength.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWFQLength.setStatus(_A)
_HpnicfIfQoSWFQDiscardPackets_Type=Counter64
_HpnicfIfQoSWFQDiscardPackets_Object=MibTableColumn
hpnicfIfQoSWFQDiscardPackets=_HpnicfIfQoSWFQDiscardPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,4,2,1,1,3),_HpnicfIfQoSWFQDiscardPackets_Type())
hpnicfIfQoSWFQDiscardPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWFQDiscardPackets.setStatus(_A)
_HpnicfIfQoSWFQHashedActiveQueues_Type=Integer32
_HpnicfIfQoSWFQHashedActiveQueues_Object=MibTableColumn
hpnicfIfQoSWFQHashedActiveQueues=_HpnicfIfQoSWFQHashedActiveQueues_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,4,2,1,1,4),_HpnicfIfQoSWFQHashedActiveQueues_Type())
hpnicfIfQoSWFQHashedActiveQueues.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWFQHashedActiveQueues.setStatus(_A)
_HpnicfIfQoSWFQHashedMaxActiveQueues_Type=Integer32
_HpnicfIfQoSWFQHashedMaxActiveQueues_Object=MibTableColumn
hpnicfIfQoSWFQHashedMaxActiveQueues=_HpnicfIfQoSWFQHashedMaxActiveQueues_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,4,2,1,1,5),_HpnicfIfQoSWFQHashedMaxActiveQueues_Type())
hpnicfIfQoSWFQHashedMaxActiveQueues.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWFQHashedMaxActiveQueues.setStatus(_A)
_HpnicfIfQosWFQhashedTotalQueues_Type=Integer32
_HpnicfIfQosWFQhashedTotalQueues_Object=MibTableColumn
hpnicfIfQosWFQhashedTotalQueues=_HpnicfIfQosWFQhashedTotalQueues_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,4,2,1,1,6),_HpnicfIfQosWFQhashedTotalQueues_Type())
hpnicfIfQosWFQhashedTotalQueues.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQosWFQhashedTotalQueues.setStatus(_A)
_HpnicfIfQoSBandwidthGroup_ObjectIdentity=ObjectIdentity
hpnicfIfQoSBandwidthGroup=_HpnicfIfQoSBandwidthGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,5))
_HpnicfIfQoSBandwidthTable_Object=MibTable
hpnicfIfQoSBandwidthTable=_HpnicfIfQoSBandwidthTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,5,1))
if mibBuilder.loadTexts:hpnicfIfQoSBandwidthTable.setStatus(_A)
_HpnicfIfQoSBandwidthEntry_Object=MibTableRow
hpnicfIfQoSBandwidthEntry=_HpnicfIfQoSBandwidthEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,5,1,1))
hpnicfIfQoSBandwidthEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hpnicfIfQoSBandwidthEntry.setStatus(_A)
_HpnicfIfQoSMaxBandwidth_Type=Integer32
_HpnicfIfQoSMaxBandwidth_Object=MibTableColumn
hpnicfIfQoSMaxBandwidth=_HpnicfIfQoSMaxBandwidth_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,5,1,1,1),_HpnicfIfQoSMaxBandwidth_Type())
hpnicfIfQoSMaxBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSMaxBandwidth.setStatus(_A)
class _HpnicfIfQoSReservedBandwidthPct_Type(Integer32):defaultValue=75;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpnicfIfQoSReservedBandwidthPct_Type.__name__=_D
_HpnicfIfQoSReservedBandwidthPct_Object=MibTableColumn
hpnicfIfQoSReservedBandwidthPct=_HpnicfIfQoSReservedBandwidthPct_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,5,1,1,2),_HpnicfIfQoSReservedBandwidthPct_Type())
hpnicfIfQoSReservedBandwidthPct.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSReservedBandwidthPct.setStatus(_A)
_HpnicfIfQoSBandwidthRowStatus_Type=RowStatus
_HpnicfIfQoSBandwidthRowStatus_Object=MibTableColumn
hpnicfIfQoSBandwidthRowStatus=_HpnicfIfQoSBandwidthRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,5,1,1,3),_HpnicfIfQoSBandwidthRowStatus_Type())
hpnicfIfQoSBandwidthRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSBandwidthRowStatus.setStatus(_A)
_HpnicfIfQoSQmtokenGroup_ObjectIdentity=ObjectIdentity
hpnicfIfQoSQmtokenGroup=_HpnicfIfQoSQmtokenGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,6))
_HpnicfIfQoSQmtokenTable_Object=MibTable
hpnicfIfQoSQmtokenTable=_HpnicfIfQoSQmtokenTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,6,1))
if mibBuilder.loadTexts:hpnicfIfQoSQmtokenTable.setStatus(_A)
_HpnicfIfQoSQmtokenEntry_Object=MibTableRow
hpnicfIfQoSQmtokenEntry=_HpnicfIfQoSQmtokenEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,6,1,1))
hpnicfIfQoSQmtokenEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hpnicfIfQoSQmtokenEntry.setStatus(_A)
class _HpnicfIfQoSQmtokenNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,50))
_HpnicfIfQoSQmtokenNumber_Type.__name__=_D
_HpnicfIfQoSQmtokenNumber_Object=MibTableColumn
hpnicfIfQoSQmtokenNumber=_HpnicfIfQoSQmtokenNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,6,1,1,1),_HpnicfIfQoSQmtokenNumber_Type())
hpnicfIfQoSQmtokenNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSQmtokenNumber.setStatus(_A)
_HpnicfIfQoSQmtokenRosStatus_Type=RowStatus
_HpnicfIfQoSQmtokenRosStatus_Object=MibTableColumn
hpnicfIfQoSQmtokenRosStatus=_HpnicfIfQoSQmtokenRosStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,6,1,1,2),_HpnicfIfQoSQmtokenRosStatus_Type())
hpnicfIfQoSQmtokenRosStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSQmtokenRosStatus.setStatus(_A)
_HpnicfIfQoSRTPQObject_ObjectIdentity=ObjectIdentity
hpnicfIfQoSRTPQObject=_HpnicfIfQoSRTPQObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,7))
_HpnicfIfQoSRTPQConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfIfQoSRTPQConfigGroup=_HpnicfIfQoSRTPQConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,7,1))
_HpnicfIfQoSRTPQConfigTable_Object=MibTable
hpnicfIfQoSRTPQConfigTable=_HpnicfIfQoSRTPQConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,7,1,1))
if mibBuilder.loadTexts:hpnicfIfQoSRTPQConfigTable.setStatus(_A)
_HpnicfIfQoSRTPQConfigEntry_Object=MibTableRow
hpnicfIfQoSRTPQConfigEntry=_HpnicfIfQoSRTPQConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,7,1,1,1))
hpnicfIfQoSRTPQConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hpnicfIfQoSRTPQConfigEntry.setStatus(_A)
class _HpnicfIfQoSRTPQStartPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2000,65535))
_HpnicfIfQoSRTPQStartPort_Type.__name__=_D
_HpnicfIfQoSRTPQStartPort_Object=MibTableColumn
hpnicfIfQoSRTPQStartPort=_HpnicfIfQoSRTPQStartPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,7,1,1,1,1),_HpnicfIfQoSRTPQStartPort_Type())
hpnicfIfQoSRTPQStartPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSRTPQStartPort.setStatus(_A)
class _HpnicfIfQoSRTPQEndPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2000,65535))
_HpnicfIfQoSRTPQEndPort_Type.__name__=_D
_HpnicfIfQoSRTPQEndPort_Object=MibTableColumn
hpnicfIfQoSRTPQEndPort=_HpnicfIfQoSRTPQEndPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,7,1,1,1,2),_HpnicfIfQoSRTPQEndPort_Type())
hpnicfIfQoSRTPQEndPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSRTPQEndPort.setStatus(_A)
_HpnicfIfQoSRTPQReservedBandwidth_Type=Integer32
_HpnicfIfQoSRTPQReservedBandwidth_Object=MibTableColumn
hpnicfIfQoSRTPQReservedBandwidth=_HpnicfIfQoSRTPQReservedBandwidth_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,7,1,1,1,3),_HpnicfIfQoSRTPQReservedBandwidth_Type())
hpnicfIfQoSRTPQReservedBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSRTPQReservedBandwidth.setStatus(_A)
_HpnicfIfQoSRTPQCbs_Type=Unsigned32
_HpnicfIfQoSRTPQCbs_Object=MibTableColumn
hpnicfIfQoSRTPQCbs=_HpnicfIfQoSRTPQCbs_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,7,1,1,1,4),_HpnicfIfQoSRTPQCbs_Type())
hpnicfIfQoSRTPQCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSRTPQCbs.setStatus(_A)
_HpnicfIfQoSRTPQRowStatus_Type=RowStatus
_HpnicfIfQoSRTPQRowStatus_Object=MibTableColumn
hpnicfIfQoSRTPQRowStatus=_HpnicfIfQoSRTPQRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,7,1,1,1,5),_HpnicfIfQoSRTPQRowStatus_Type())
hpnicfIfQoSRTPQRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSRTPQRowStatus.setStatus(_A)
_HpnicfIfQoSRTPQRunInfoGroup_ObjectIdentity=ObjectIdentity
hpnicfIfQoSRTPQRunInfoGroup=_HpnicfIfQoSRTPQRunInfoGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,7,2))
_HpnicfIfQoSRTPQRunInfoTable_Object=MibTable
hpnicfIfQoSRTPQRunInfoTable=_HpnicfIfQoSRTPQRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,7,2,1))
if mibBuilder.loadTexts:hpnicfIfQoSRTPQRunInfoTable.setStatus(_A)
_HpnicfIfQoSRTPQRunInfoEntry_Object=MibTableRow
hpnicfIfQoSRTPQRunInfoEntry=_HpnicfIfQoSRTPQRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,7,2,1,1))
hpnicfIfQoSRTPQRunInfoEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hpnicfIfQoSRTPQRunInfoEntry.setStatus(_A)
_HpnicfIfQoSRTPQPacketNumber_Type=Integer32
_HpnicfIfQoSRTPQPacketNumber_Object=MibTableColumn
hpnicfIfQoSRTPQPacketNumber=_HpnicfIfQoSRTPQPacketNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,7,2,1,1,1),_HpnicfIfQoSRTPQPacketNumber_Type())
hpnicfIfQoSRTPQPacketNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSRTPQPacketNumber.setStatus(_A)
_HpnicfIfQoSRTPQPacketSize_Type=Integer32
_HpnicfIfQoSRTPQPacketSize_Object=MibTableColumn
hpnicfIfQoSRTPQPacketSize=_HpnicfIfQoSRTPQPacketSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,7,2,1,1,2),_HpnicfIfQoSRTPQPacketSize_Type())
hpnicfIfQoSRTPQPacketSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSRTPQPacketSize.setStatus(_A)
_HpnicfIfQoSRTPQOutputPackets_Type=Counter64
_HpnicfIfQoSRTPQOutputPackets_Object=MibTableColumn
hpnicfIfQoSRTPQOutputPackets=_HpnicfIfQoSRTPQOutputPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,7,2,1,1,3),_HpnicfIfQoSRTPQOutputPackets_Type())
hpnicfIfQoSRTPQOutputPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSRTPQOutputPackets.setStatus(_A)
_HpnicfIfQoSRTPQDiscardPackets_Type=Counter64
_HpnicfIfQoSRTPQDiscardPackets_Object=MibTableColumn
hpnicfIfQoSRTPQDiscardPackets=_HpnicfIfQoSRTPQDiscardPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,7,2,1,1,4),_HpnicfIfQoSRTPQDiscardPackets_Type())
hpnicfIfQoSRTPQDiscardPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSRTPQDiscardPackets.setStatus(_A)
_HpnicfIfQoSCarListObject_ObjectIdentity=ObjectIdentity
hpnicfIfQoSCarListObject=_HpnicfIfQoSCarListObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,8))
_HpnicfIfQoCarListGroup_ObjectIdentity=ObjectIdentity
hpnicfIfQoCarListGroup=_HpnicfIfQoCarListGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,8,1))
_HpnicfIfQoSCarlTable_Object=MibTable
hpnicfIfQoSCarlTable=_HpnicfIfQoSCarlTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,8,1,1))
if mibBuilder.loadTexts:hpnicfIfQoSCarlTable.setStatus(_A)
_HpnicfIfQoSCarlEntry_Object=MibTableRow
hpnicfIfQoSCarlEntry=_HpnicfIfQoSCarlEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,8,1,1,1))
hpnicfIfQoSCarlEntry.setIndexNames((0,_E,_v))
if mibBuilder.loadTexts:hpnicfIfQoSCarlEntry.setStatus(_A)
_HpnicfIfQoSCarlListNum_Type=Integer32
_HpnicfIfQoSCarlListNum_Object=MibTableColumn
hpnicfIfQoSCarlListNum=_HpnicfIfQoSCarlListNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,8,1,1,1,1),_HpnicfIfQoSCarlListNum_Type())
hpnicfIfQoSCarlListNum.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSCarlListNum.setStatus(_A)
class _HpnicfIfQoSCarlParaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('macAddress',1),('precMask',2),('dscpMask',3)))
_HpnicfIfQoSCarlParaType_Type.__name__=_D
_HpnicfIfQoSCarlParaType_Object=MibTableColumn
hpnicfIfQoSCarlParaType=_HpnicfIfQoSCarlParaType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,8,1,1,1,2),_HpnicfIfQoSCarlParaType_Type())
hpnicfIfQoSCarlParaType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSCarlParaType.setStatus(_A)
_HpnicfIfQoSCarlParaValue_Type=OctetString
_HpnicfIfQoSCarlParaValue_Object=MibTableColumn
hpnicfIfQoSCarlParaValue=_HpnicfIfQoSCarlParaValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,8,1,1,1,3),_HpnicfIfQoSCarlParaValue_Type())
hpnicfIfQoSCarlParaValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSCarlParaValue.setStatus(_A)
_HpnicfIfQoSCarlRowStatus_Type=RowStatus
_HpnicfIfQoSCarlRowStatus_Object=MibTableColumn
hpnicfIfQoSCarlRowStatus=_HpnicfIfQoSCarlRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,2,8,1,1,1,4),_HpnicfIfQoSCarlRowStatus_Type())
hpnicfIfQoSCarlRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSCarlRowStatus.setStatus(_A)
_HpnicfIfQoSLineRateObjects_ObjectIdentity=ObjectIdentity
hpnicfIfQoSLineRateObjects=_HpnicfIfQoSLineRateObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,3))
_HpnicfIfQoSLRConfigTable_Object=MibTable
hpnicfIfQoSLRConfigTable=_HpnicfIfQoSLRConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,3,1))
if mibBuilder.loadTexts:hpnicfIfQoSLRConfigTable.setStatus(_A)
_HpnicfIfQoSLRConfigEntry_Object=MibTableRow
hpnicfIfQoSLRConfigEntry=_HpnicfIfQoSLRConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,3,1,1))
hpnicfIfQoSLRConfigEntry.setIndexNames((0,_G,_H),(0,_E,_U))
if mibBuilder.loadTexts:hpnicfIfQoSLRConfigEntry.setStatus(_A)
_HpnicfIfQoSLRDirection_Type=Direction
_HpnicfIfQoSLRDirection_Object=MibTableColumn
hpnicfIfQoSLRDirection=_HpnicfIfQoSLRDirection_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,3,1,1,1),_HpnicfIfQoSLRDirection_Type())
hpnicfIfQoSLRDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSLRDirection.setStatus(_A)
_HpnicfIfQoSLRCir_Type=Unsigned32
_HpnicfIfQoSLRCir_Object=MibTableColumn
hpnicfIfQoSLRCir=_HpnicfIfQoSLRCir_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,3,1,1,2),_HpnicfIfQoSLRCir_Type())
hpnicfIfQoSLRCir.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSLRCir.setStatus(_A)
_HpnicfIfQoSLRCbs_Type=Unsigned32
_HpnicfIfQoSLRCbs_Object=MibTableColumn
hpnicfIfQoSLRCbs=_HpnicfIfQoSLRCbs_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,3,1,1,3),_HpnicfIfQoSLRCbs_Type())
hpnicfIfQoSLRCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSLRCbs.setStatus(_A)
_HpnicfIfQoSLREbs_Type=Unsigned32
_HpnicfIfQoSLREbs_Object=MibTableColumn
hpnicfIfQoSLREbs=_HpnicfIfQoSLREbs_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,3,1,1,4),_HpnicfIfQoSLREbs_Type())
hpnicfIfQoSLREbs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSLREbs.setStatus(_A)
_HpnicfIfQoSRowStatus_Type=RowStatus
_HpnicfIfQoSRowStatus_Object=MibTableColumn
hpnicfIfQoSRowStatus=_HpnicfIfQoSRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,3,1,1,5),_HpnicfIfQoSRowStatus_Type())
hpnicfIfQoSRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSRowStatus.setStatus(_A)
_HpnicfIfQoSLRPir_Type=Unsigned32
_HpnicfIfQoSLRPir_Object=MibTableColumn
hpnicfIfQoSLRPir=_HpnicfIfQoSLRPir_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,3,1,1,6),_HpnicfIfQoSLRPir_Type())
hpnicfIfQoSLRPir.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSLRPir.setStatus(_A)
class _HpnicfIfQoSLRUnit_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unitAbsolute',1),('unitPercent',2)))
_HpnicfIfQoSLRUnit_Type.__name__=_D
_HpnicfIfQoSLRUnit_Object=MibTableColumn
hpnicfIfQoSLRUnit=_HpnicfIfQoSLRUnit_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,3,1,1,7),_HpnicfIfQoSLRUnit_Type())
hpnicfIfQoSLRUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSLRUnit.setStatus(_A)
_HpnicfIfQoSLRRunInfoTable_Object=MibTable
hpnicfIfQoSLRRunInfoTable=_HpnicfIfQoSLRRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,3,2))
if mibBuilder.loadTexts:hpnicfIfQoSLRRunInfoTable.setStatus(_A)
_HpnicfIfQoSLRRunInfoEntry_Object=MibTableRow
hpnicfIfQoSLRRunInfoEntry=_HpnicfIfQoSLRRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,3,2,1))
hpnicfIfQoSLRRunInfoEntry.setIndexNames((0,_G,_H),(0,_E,_U))
if mibBuilder.loadTexts:hpnicfIfQoSLRRunInfoEntry.setStatus(_A)
_HpnicfIfQoSLRRunInfoPassedPackets_Type=Counter64
_HpnicfIfQoSLRRunInfoPassedPackets_Object=MibTableColumn
hpnicfIfQoSLRRunInfoPassedPackets=_HpnicfIfQoSLRRunInfoPassedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,3,2,1,1),_HpnicfIfQoSLRRunInfoPassedPackets_Type())
hpnicfIfQoSLRRunInfoPassedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSLRRunInfoPassedPackets.setStatus(_A)
_HpnicfIfQoSLRRunInfoPassedBytes_Type=Counter64
_HpnicfIfQoSLRRunInfoPassedBytes_Object=MibTableColumn
hpnicfIfQoSLRRunInfoPassedBytes=_HpnicfIfQoSLRRunInfoPassedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,3,2,1,2),_HpnicfIfQoSLRRunInfoPassedBytes_Type())
hpnicfIfQoSLRRunInfoPassedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSLRRunInfoPassedBytes.setStatus(_A)
_HpnicfIfQoSLRRunInfoDelayedPackets_Type=Counter64
_HpnicfIfQoSLRRunInfoDelayedPackets_Object=MibTableColumn
hpnicfIfQoSLRRunInfoDelayedPackets=_HpnicfIfQoSLRRunInfoDelayedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,3,2,1,3),_HpnicfIfQoSLRRunInfoDelayedPackets_Type())
hpnicfIfQoSLRRunInfoDelayedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSLRRunInfoDelayedPackets.setStatus(_A)
_HpnicfIfQoSLRRunInfoDelayedBytes_Type=Counter64
_HpnicfIfQoSLRRunInfoDelayedBytes_Object=MibTableColumn
hpnicfIfQoSLRRunInfoDelayedBytes=_HpnicfIfQoSLRRunInfoDelayedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,3,2,1,4),_HpnicfIfQoSLRRunInfoDelayedBytes_Type())
hpnicfIfQoSLRRunInfoDelayedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSLRRunInfoDelayedBytes.setStatus(_A)
class _HpnicfIfQoSLRRunInfoActiveShaping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_HpnicfIfQoSLRRunInfoActiveShaping_Type.__name__=_D
_HpnicfIfQoSLRRunInfoActiveShaping_Object=MibTableColumn
hpnicfIfQoSLRRunInfoActiveShaping=_HpnicfIfQoSLRRunInfoActiveShaping_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,3,2,1,5),_HpnicfIfQoSLRRunInfoActiveShaping_Type())
hpnicfIfQoSLRRunInfoActiveShaping.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSLRRunInfoActiveShaping.setStatus(_A)
_HpnicfIfQoSCARObjects_ObjectIdentity=ObjectIdentity
hpnicfIfQoSCARObjects=_HpnicfIfQoSCARObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4))
_HpnicfIfQoSAggregativeCarGroup_ObjectIdentity=ObjectIdentity
hpnicfIfQoSAggregativeCarGroup=_HpnicfIfQoSAggregativeCarGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1))
_HpnicfIfQoSAggregativeCarNextIndex_Type=Integer32
_HpnicfIfQoSAggregativeCarNextIndex_Object=MibScalar
hpnicfIfQoSAggregativeCarNextIndex=_HpnicfIfQoSAggregativeCarNextIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,1),_HpnicfIfQoSAggregativeCarNextIndex_Type())
hpnicfIfQoSAggregativeCarNextIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarNextIndex.setStatus(_A)
_HpnicfIfQoSAggregativeCarConfigTable_Object=MibTable
hpnicfIfQoSAggregativeCarConfigTable=_HpnicfIfQoSAggregativeCarConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,2))
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarConfigTable.setStatus(_A)
_HpnicfIfQoSAggregativeCarConfigEntry_Object=MibTableRow
hpnicfIfQoSAggregativeCarConfigEntry=_HpnicfIfQoSAggregativeCarConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,2,1))
hpnicfIfQoSAggregativeCarConfigEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarConfigEntry.setStatus(_A)
class _HpnicfIfQoSAggregativeCarIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65534))
_HpnicfIfQoSAggregativeCarIndex_Type.__name__=_D
_HpnicfIfQoSAggregativeCarIndex_Object=MibTableColumn
hpnicfIfQoSAggregativeCarIndex=_HpnicfIfQoSAggregativeCarIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,2,1,1),_HpnicfIfQoSAggregativeCarIndex_Type())
hpnicfIfQoSAggregativeCarIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarIndex.setStatus(_A)
class _HpnicfIfQoSAggregativeCarName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_HpnicfIfQoSAggregativeCarName_Type.__name__=_K
_HpnicfIfQoSAggregativeCarName_Object=MibTableColumn
hpnicfIfQoSAggregativeCarName=_HpnicfIfQoSAggregativeCarName_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,2,1,2),_HpnicfIfQoSAggregativeCarName_Type())
hpnicfIfQoSAggregativeCarName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarName.setStatus(_A)
_HpnicfIfQoSAggregativeCarCir_Type=Unsigned32
_HpnicfIfQoSAggregativeCarCir_Object=MibTableColumn
hpnicfIfQoSAggregativeCarCir=_HpnicfIfQoSAggregativeCarCir_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,2,1,3),_HpnicfIfQoSAggregativeCarCir_Type())
hpnicfIfQoSAggregativeCarCir.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarCir.setStatus(_A)
_HpnicfIfQoSAggregativeCarCbs_Type=Unsigned32
_HpnicfIfQoSAggregativeCarCbs_Object=MibTableColumn
hpnicfIfQoSAggregativeCarCbs=_HpnicfIfQoSAggregativeCarCbs_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,2,1,4),_HpnicfIfQoSAggregativeCarCbs_Type())
hpnicfIfQoSAggregativeCarCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarCbs.setStatus(_A)
_HpnicfIfQoSAggregativeCarEbs_Type=Unsigned32
_HpnicfIfQoSAggregativeCarEbs_Object=MibTableColumn
hpnicfIfQoSAggregativeCarEbs=_HpnicfIfQoSAggregativeCarEbs_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,2,1,5),_HpnicfIfQoSAggregativeCarEbs_Type())
hpnicfIfQoSAggregativeCarEbs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarEbs.setStatus(_A)
_HpnicfIfQoSAggregativeCarPir_Type=Unsigned32
_HpnicfIfQoSAggregativeCarPir_Object=MibTableColumn
hpnicfIfQoSAggregativeCarPir=_HpnicfIfQoSAggregativeCarPir_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,2,1,6),_HpnicfIfQoSAggregativeCarPir_Type())
hpnicfIfQoSAggregativeCarPir.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarPir.setStatus(_A)
class _HpnicfIfQoSAggregativeCarGreenActionType_Type(CarAction):defaultValue=1
_HpnicfIfQoSAggregativeCarGreenActionType_Type.__name__=_O
_HpnicfIfQoSAggregativeCarGreenActionType_Object=MibTableColumn
hpnicfIfQoSAggregativeCarGreenActionType=_HpnicfIfQoSAggregativeCarGreenActionType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,2,1,7),_HpnicfIfQoSAggregativeCarGreenActionType_Type())
hpnicfIfQoSAggregativeCarGreenActionType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarGreenActionType.setStatus(_A)
class _HpnicfIfQoSAggregativeCarGreenActionValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HpnicfIfQoSAggregativeCarGreenActionValue_Type.__name__=_D
_HpnicfIfQoSAggregativeCarGreenActionValue_Object=MibTableColumn
hpnicfIfQoSAggregativeCarGreenActionValue=_HpnicfIfQoSAggregativeCarGreenActionValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,2,1,8),_HpnicfIfQoSAggregativeCarGreenActionValue_Type())
hpnicfIfQoSAggregativeCarGreenActionValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarGreenActionValue.setStatus(_A)
_HpnicfIfQoSAggregativeCarYellowActionType_Type=CarAction
_HpnicfIfQoSAggregativeCarYellowActionType_Object=MibTableColumn
hpnicfIfQoSAggregativeCarYellowActionType=_HpnicfIfQoSAggregativeCarYellowActionType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,2,1,9),_HpnicfIfQoSAggregativeCarYellowActionType_Type())
hpnicfIfQoSAggregativeCarYellowActionType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarYellowActionType.setStatus(_A)
class _HpnicfIfQoSAggregativeCarYellowActionValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HpnicfIfQoSAggregativeCarYellowActionValue_Type.__name__=_D
_HpnicfIfQoSAggregativeCarYellowActionValue_Object=MibTableColumn
hpnicfIfQoSAggregativeCarYellowActionValue=_HpnicfIfQoSAggregativeCarYellowActionValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,2,1,10),_HpnicfIfQoSAggregativeCarYellowActionValue_Type())
hpnicfIfQoSAggregativeCarYellowActionValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarYellowActionValue.setStatus(_A)
_HpnicfIfQoSAggregativeCarRedActionType_Type=CarAction
_HpnicfIfQoSAggregativeCarRedActionType_Object=MibTableColumn
hpnicfIfQoSAggregativeCarRedActionType=_HpnicfIfQoSAggregativeCarRedActionType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,2,1,11),_HpnicfIfQoSAggregativeCarRedActionType_Type())
hpnicfIfQoSAggregativeCarRedActionType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarRedActionType.setStatus(_A)
_HpnicfIfQoSAggregativeCarRedActionValue_Type=Integer32
_HpnicfIfQoSAggregativeCarRedActionValue_Object=MibTableColumn
hpnicfIfQoSAggregativeCarRedActionValue=_HpnicfIfQoSAggregativeCarRedActionValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,2,1,12),_HpnicfIfQoSAggregativeCarRedActionValue_Type())
hpnicfIfQoSAggregativeCarRedActionValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarRedActionValue.setStatus(_A)
class _HpnicfIfQoSAggregativeCarType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('aggregative',1),('notAggregative',2)))
_HpnicfIfQoSAggregativeCarType_Type.__name__=_D
_HpnicfIfQoSAggregativeCarType_Object=MibTableColumn
hpnicfIfQoSAggregativeCarType=_HpnicfIfQoSAggregativeCarType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,2,1,13),_HpnicfIfQoSAggregativeCarType_Type())
hpnicfIfQoSAggregativeCarType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarType.setStatus(_A)
_HpnicfIfQoSAggregativeCarRowStatus_Type=RowStatus
_HpnicfIfQoSAggregativeCarRowStatus_Object=MibTableColumn
hpnicfIfQoSAggregativeCarRowStatus=_HpnicfIfQoSAggregativeCarRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,2,1,14),_HpnicfIfQoSAggregativeCarRowStatus_Type())
hpnicfIfQoSAggregativeCarRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarRowStatus.setStatus(_A)
_HpnicfIfQoSAggregativeCarApplyTable_Object=MibTable
hpnicfIfQoSAggregativeCarApplyTable=_HpnicfIfQoSAggregativeCarApplyTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,3))
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarApplyTable.setStatus(_A)
_HpnicfIfQoSAggregativeCarApplyEntry_Object=MibTableRow
hpnicfIfQoSAggregativeCarApplyEntry=_HpnicfIfQoSAggregativeCarApplyEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,3,1))
hpnicfIfQoSAggregativeCarApplyEntry.setIndexNames((0,_G,_H),(0,_E,_w),(0,_E,_x),(0,_E,_y))
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarApplyEntry.setStatus(_A)
_HpnicfIfQoSAggregativeCarApplyDirection_Type=Direction
_HpnicfIfQoSAggregativeCarApplyDirection_Object=MibTableColumn
hpnicfIfQoSAggregativeCarApplyDirection=_HpnicfIfQoSAggregativeCarApplyDirection_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,3,1,1),_HpnicfIfQoSAggregativeCarApplyDirection_Type())
hpnicfIfQoSAggregativeCarApplyDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarApplyDirection.setStatus(_A)
class _HpnicfIfQoSAggregativeCarApplyRuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_M,2),('carl',3),(_W,4)))
_HpnicfIfQoSAggregativeCarApplyRuleType_Type.__name__=_D
_HpnicfIfQoSAggregativeCarApplyRuleType_Object=MibTableColumn
hpnicfIfQoSAggregativeCarApplyRuleType=_HpnicfIfQoSAggregativeCarApplyRuleType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,3,1,2),_HpnicfIfQoSAggregativeCarApplyRuleType_Type())
hpnicfIfQoSAggregativeCarApplyRuleType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarApplyRuleType.setStatus(_A)
_HpnicfIfQoSAggregativeCarApplyRuleValue_Type=Integer32
_HpnicfIfQoSAggregativeCarApplyRuleValue_Object=MibTableColumn
hpnicfIfQoSAggregativeCarApplyRuleValue=_HpnicfIfQoSAggregativeCarApplyRuleValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,3,1,3),_HpnicfIfQoSAggregativeCarApplyRuleValue_Type())
hpnicfIfQoSAggregativeCarApplyRuleValue.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarApplyRuleValue.setStatus(_A)
_HpnicfIfQoSAggregativeCarApplyCarIndex_Type=Integer32
_HpnicfIfQoSAggregativeCarApplyCarIndex_Object=MibTableColumn
hpnicfIfQoSAggregativeCarApplyCarIndex=_HpnicfIfQoSAggregativeCarApplyCarIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,3,1,4),_HpnicfIfQoSAggregativeCarApplyCarIndex_Type())
hpnicfIfQoSAggregativeCarApplyCarIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarApplyCarIndex.setStatus(_A)
_HpnicfIfQoSAggregativeCarApplyRowStatus_Type=RowStatus
_HpnicfIfQoSAggregativeCarApplyRowStatus_Object=MibTableColumn
hpnicfIfQoSAggregativeCarApplyRowStatus=_HpnicfIfQoSAggregativeCarApplyRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,3,1,5),_HpnicfIfQoSAggregativeCarApplyRowStatus_Type())
hpnicfIfQoSAggregativeCarApplyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarApplyRowStatus.setStatus(_A)
_HpnicfIfQoSAggregativeCarRunInfoTable_Object=MibTable
hpnicfIfQoSAggregativeCarRunInfoTable=_HpnicfIfQoSAggregativeCarRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,4))
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarRunInfoTable.setStatus(_A)
_HpnicfIfQoSAggregativeCarRunInfoEntry_Object=MibTableRow
hpnicfIfQoSAggregativeCarRunInfoEntry=_HpnicfIfQoSAggregativeCarRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,4,1))
hpnicfIfQoSAggregativeCarRunInfoEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarRunInfoEntry.setStatus(_A)
_HpnicfIfQoSAggregativeCarGreenPackets_Type=Counter64
_HpnicfIfQoSAggregativeCarGreenPackets_Object=MibTableColumn
hpnicfIfQoSAggregativeCarGreenPackets=_HpnicfIfQoSAggregativeCarGreenPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,4,1,1),_HpnicfIfQoSAggregativeCarGreenPackets_Type())
hpnicfIfQoSAggregativeCarGreenPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarGreenPackets.setStatus(_A)
_HpnicfIfQoSAggregativeCarGreenBytes_Type=Counter64
_HpnicfIfQoSAggregativeCarGreenBytes_Object=MibTableColumn
hpnicfIfQoSAggregativeCarGreenBytes=_HpnicfIfQoSAggregativeCarGreenBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,4,1,2),_HpnicfIfQoSAggregativeCarGreenBytes_Type())
hpnicfIfQoSAggregativeCarGreenBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarGreenBytes.setStatus(_A)
_HpnicfIfQoSAggregativeCarYellowPackets_Type=Counter64
_HpnicfIfQoSAggregativeCarYellowPackets_Object=MibTableColumn
hpnicfIfQoSAggregativeCarYellowPackets=_HpnicfIfQoSAggregativeCarYellowPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,4,1,3),_HpnicfIfQoSAggregativeCarYellowPackets_Type())
hpnicfIfQoSAggregativeCarYellowPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarYellowPackets.setStatus(_A)
_HpnicfIfQoSAggregativeCarYellowBytes_Type=Counter64
_HpnicfIfQoSAggregativeCarYellowBytes_Object=MibTableColumn
hpnicfIfQoSAggregativeCarYellowBytes=_HpnicfIfQoSAggregativeCarYellowBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,4,1,4),_HpnicfIfQoSAggregativeCarYellowBytes_Type())
hpnicfIfQoSAggregativeCarYellowBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarYellowBytes.setStatus(_A)
_HpnicfIfQoSAggregativeCarRedPackets_Type=Counter64
_HpnicfIfQoSAggregativeCarRedPackets_Object=MibTableColumn
hpnicfIfQoSAggregativeCarRedPackets=_HpnicfIfQoSAggregativeCarRedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,4,1,5),_HpnicfIfQoSAggregativeCarRedPackets_Type())
hpnicfIfQoSAggregativeCarRedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarRedPackets.setStatus(_A)
_HpnicfIfQoSAggregativeCarRedBytes_Type=Counter64
_HpnicfIfQoSAggregativeCarRedBytes_Object=MibTableColumn
hpnicfIfQoSAggregativeCarRedBytes=_HpnicfIfQoSAggregativeCarRedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,1,4,1,6),_HpnicfIfQoSAggregativeCarRedBytes_Type())
hpnicfIfQoSAggregativeCarRedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSAggregativeCarRedBytes.setStatus(_A)
_HpnicfIfQoSTricolorCarGroup_ObjectIdentity=ObjectIdentity
hpnicfIfQoSTricolorCarGroup=_HpnicfIfQoSTricolorCarGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,2))
_HpnicfIfQoSTricolorCarConfigTable_Object=MibTable
hpnicfIfQoSTricolorCarConfigTable=_HpnicfIfQoSTricolorCarConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,2,1))
if mibBuilder.loadTexts:hpnicfIfQoSTricolorCarConfigTable.setStatus(_A)
_HpnicfIfQoSTricolorCarConfigEntry_Object=MibTableRow
hpnicfIfQoSTricolorCarConfigEntry=_HpnicfIfQoSTricolorCarConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,2,1,1))
hpnicfIfQoSTricolorCarConfigEntry.setIndexNames((0,_G,_H),(0,_E,_X),(0,_E,_Y),(0,_E,_Z))
if mibBuilder.loadTexts:hpnicfIfQoSTricolorCarConfigEntry.setStatus(_A)
_HpnicfIfQoSTricolorCarDirection_Type=Direction
_HpnicfIfQoSTricolorCarDirection_Object=MibTableColumn
hpnicfIfQoSTricolorCarDirection=_HpnicfIfQoSTricolorCarDirection_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,2,1,1,1),_HpnicfIfQoSTricolorCarDirection_Type())
hpnicfIfQoSTricolorCarDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSTricolorCarDirection.setStatus(_A)
class _HpnicfIfQoSTricolorCarType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_M,2),('carl',3),(_W,4)))
_HpnicfIfQoSTricolorCarType_Type.__name__=_D
_HpnicfIfQoSTricolorCarType_Object=MibTableColumn
hpnicfIfQoSTricolorCarType=_HpnicfIfQoSTricolorCarType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,2,1,1,2),_HpnicfIfQoSTricolorCarType_Type())
hpnicfIfQoSTricolorCarType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSTricolorCarType.setStatus(_A)
_HpnicfIfQoSTricolorCarValue_Type=Integer32
_HpnicfIfQoSTricolorCarValue_Object=MibTableColumn
hpnicfIfQoSTricolorCarValue=_HpnicfIfQoSTricolorCarValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,2,1,1,3),_HpnicfIfQoSTricolorCarValue_Type())
hpnicfIfQoSTricolorCarValue.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSTricolorCarValue.setStatus(_A)
_HpnicfIfQoSTricolorCarCir_Type=Unsigned32
_HpnicfIfQoSTricolorCarCir_Object=MibTableColumn
hpnicfIfQoSTricolorCarCir=_HpnicfIfQoSTricolorCarCir_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,2,1,1,4),_HpnicfIfQoSTricolorCarCir_Type())
hpnicfIfQoSTricolorCarCir.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSTricolorCarCir.setStatus(_A)
_HpnicfIfQoSTricolorCarCbs_Type=Unsigned32
_HpnicfIfQoSTricolorCarCbs_Object=MibTableColumn
hpnicfIfQoSTricolorCarCbs=_HpnicfIfQoSTricolorCarCbs_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,2,1,1,5),_HpnicfIfQoSTricolorCarCbs_Type())
hpnicfIfQoSTricolorCarCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSTricolorCarCbs.setStatus(_A)
_HpnicfIfQoSTricolorCarEbs_Type=Unsigned32
_HpnicfIfQoSTricolorCarEbs_Object=MibTableColumn
hpnicfIfQoSTricolorCarEbs=_HpnicfIfQoSTricolorCarEbs_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,2,1,1,6),_HpnicfIfQoSTricolorCarEbs_Type())
hpnicfIfQoSTricolorCarEbs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSTricolorCarEbs.setStatus(_A)
_HpnicfIfQoSTricolorCarPir_Type=Unsigned32
_HpnicfIfQoSTricolorCarPir_Object=MibTableColumn
hpnicfIfQoSTricolorCarPir=_HpnicfIfQoSTricolorCarPir_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,2,1,1,7),_HpnicfIfQoSTricolorCarPir_Type())
hpnicfIfQoSTricolorCarPir.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSTricolorCarPir.setStatus(_A)
class _HpnicfIfQoSTricolorCarGreenActionType_Type(CarAction):defaultValue=1
_HpnicfIfQoSTricolorCarGreenActionType_Type.__name__=_O
_HpnicfIfQoSTricolorCarGreenActionType_Object=MibTableColumn
hpnicfIfQoSTricolorCarGreenActionType=_HpnicfIfQoSTricolorCarGreenActionType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,2,1,1,8),_HpnicfIfQoSTricolorCarGreenActionType_Type())
hpnicfIfQoSTricolorCarGreenActionType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSTricolorCarGreenActionType.setStatus(_A)
class _HpnicfIfQoSTricolorCarGreenActionValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HpnicfIfQoSTricolorCarGreenActionValue_Type.__name__=_D
_HpnicfIfQoSTricolorCarGreenActionValue_Object=MibTableColumn
hpnicfIfQoSTricolorCarGreenActionValue=_HpnicfIfQoSTricolorCarGreenActionValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,2,1,1,9),_HpnicfIfQoSTricolorCarGreenActionValue_Type())
hpnicfIfQoSTricolorCarGreenActionValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSTricolorCarGreenActionValue.setStatus(_A)
class _HpnicfIfQoSTricolorCarYellowActionType_Type(CarAction):defaultValue=1
_HpnicfIfQoSTricolorCarYellowActionType_Type.__name__=_O
_HpnicfIfQoSTricolorCarYellowActionType_Object=MibTableColumn
hpnicfIfQoSTricolorCarYellowActionType=_HpnicfIfQoSTricolorCarYellowActionType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,2,1,1,10),_HpnicfIfQoSTricolorCarYellowActionType_Type())
hpnicfIfQoSTricolorCarYellowActionType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSTricolorCarYellowActionType.setStatus(_A)
class _HpnicfIfQoSTricolorCarYellowActionValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HpnicfIfQoSTricolorCarYellowActionValue_Type.__name__=_D
_HpnicfIfQoSTricolorCarYellowActionValue_Object=MibTableColumn
hpnicfIfQoSTricolorCarYellowActionValue=_HpnicfIfQoSTricolorCarYellowActionValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,2,1,1,11),_HpnicfIfQoSTricolorCarYellowActionValue_Type())
hpnicfIfQoSTricolorCarYellowActionValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSTricolorCarYellowActionValue.setStatus(_A)
class _HpnicfIfQoSTricolorCarRedActionType_Type(CarAction):defaultValue=3
_HpnicfIfQoSTricolorCarRedActionType_Type.__name__=_O
_HpnicfIfQoSTricolorCarRedActionType_Object=MibTableColumn
hpnicfIfQoSTricolorCarRedActionType=_HpnicfIfQoSTricolorCarRedActionType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,2,1,1,12),_HpnicfIfQoSTricolorCarRedActionType_Type())
hpnicfIfQoSTricolorCarRedActionType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSTricolorCarRedActionType.setStatus(_A)
class _HpnicfIfQoSTricolorCarRedActionValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HpnicfIfQoSTricolorCarRedActionValue_Type.__name__=_D
_HpnicfIfQoSTricolorCarRedActionValue_Object=MibTableColumn
hpnicfIfQoSTricolorCarRedActionValue=_HpnicfIfQoSTricolorCarRedActionValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,2,1,1,13),_HpnicfIfQoSTricolorCarRedActionValue_Type())
hpnicfIfQoSTricolorCarRedActionValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSTricolorCarRedActionValue.setStatus(_A)
_HpnicfIfQoSTricolorCarRowStatus_Type=RowStatus
_HpnicfIfQoSTricolorCarRowStatus_Object=MibTableColumn
hpnicfIfQoSTricolorCarRowStatus=_HpnicfIfQoSTricolorCarRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,2,1,1,14),_HpnicfIfQoSTricolorCarRowStatus_Type())
hpnicfIfQoSTricolorCarRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSTricolorCarRowStatus.setStatus(_A)
_HpnicfIfQoSTricolorCarRunInfoTable_Object=MibTable
hpnicfIfQoSTricolorCarRunInfoTable=_HpnicfIfQoSTricolorCarRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,2,2))
if mibBuilder.loadTexts:hpnicfIfQoSTricolorCarRunInfoTable.setStatus(_A)
_HpnicfIfQoSTricolorCarRunInfoEntry_Object=MibTableRow
hpnicfIfQoSTricolorCarRunInfoEntry=_HpnicfIfQoSTricolorCarRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,2,2,1))
hpnicfIfQoSTricolorCarRunInfoEntry.setIndexNames((0,_G,_H),(0,_E,_X),(0,_E,_Y),(0,_E,_Z))
if mibBuilder.loadTexts:hpnicfIfQoSTricolorCarRunInfoEntry.setStatus(_A)
_HpnicfIfQoSTricolorCarGreenPackets_Type=Counter64
_HpnicfIfQoSTricolorCarGreenPackets_Object=MibTableColumn
hpnicfIfQoSTricolorCarGreenPackets=_HpnicfIfQoSTricolorCarGreenPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,2,2,1,1),_HpnicfIfQoSTricolorCarGreenPackets_Type())
hpnicfIfQoSTricolorCarGreenPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSTricolorCarGreenPackets.setStatus(_A)
_HpnicfIfQoSTricolorCarGreenBytes_Type=Counter64
_HpnicfIfQoSTricolorCarGreenBytes_Object=MibTableColumn
hpnicfIfQoSTricolorCarGreenBytes=_HpnicfIfQoSTricolorCarGreenBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,2,2,1,2),_HpnicfIfQoSTricolorCarGreenBytes_Type())
hpnicfIfQoSTricolorCarGreenBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSTricolorCarGreenBytes.setStatus(_A)
_HpnicfIfQoSTricolorCarYellowPackets_Type=Counter64
_HpnicfIfQoSTricolorCarYellowPackets_Object=MibTableColumn
hpnicfIfQoSTricolorCarYellowPackets=_HpnicfIfQoSTricolorCarYellowPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,2,2,1,3),_HpnicfIfQoSTricolorCarYellowPackets_Type())
hpnicfIfQoSTricolorCarYellowPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSTricolorCarYellowPackets.setStatus(_A)
_HpnicfIfQoSTricolorCarYellowBytes_Type=Counter64
_HpnicfIfQoSTricolorCarYellowBytes_Object=MibTableColumn
hpnicfIfQoSTricolorCarYellowBytes=_HpnicfIfQoSTricolorCarYellowBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,2,2,1,4),_HpnicfIfQoSTricolorCarYellowBytes_Type())
hpnicfIfQoSTricolorCarYellowBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSTricolorCarYellowBytes.setStatus(_A)
_HpnicfIfQoSTricolorCarRedPackets_Type=Counter64
_HpnicfIfQoSTricolorCarRedPackets_Object=MibTableColumn
hpnicfIfQoSTricolorCarRedPackets=_HpnicfIfQoSTricolorCarRedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,2,2,1,5),_HpnicfIfQoSTricolorCarRedPackets_Type())
hpnicfIfQoSTricolorCarRedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSTricolorCarRedPackets.setStatus(_A)
_HpnicfIfQoSTricolorCarRedBytes_Type=Counter64
_HpnicfIfQoSTricolorCarRedBytes_Object=MibTableColumn
hpnicfIfQoSTricolorCarRedBytes=_HpnicfIfQoSTricolorCarRedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,4,2,2,1,6),_HpnicfIfQoSTricolorCarRedBytes_Type())
hpnicfIfQoSTricolorCarRedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSTricolorCarRedBytes.setStatus(_A)
_HpnicfIfQoSGTSObjects_ObjectIdentity=ObjectIdentity
hpnicfIfQoSGTSObjects=_HpnicfIfQoSGTSObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,5))
_HpnicfIfQoSGTSConfigTable_Object=MibTable
hpnicfIfQoSGTSConfigTable=_HpnicfIfQoSGTSConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,5,1))
if mibBuilder.loadTexts:hpnicfIfQoSGTSConfigTable.setStatus(_A)
_HpnicfIfQoSGTSConfigEntry_Object=MibTableRow
hpnicfIfQoSGTSConfigEntry=_HpnicfIfQoSGTSConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,5,1,1))
hpnicfIfQoSGTSConfigEntry.setIndexNames((0,_G,_H),(0,_E,_a),(0,_E,_b))
if mibBuilder.loadTexts:hpnicfIfQoSGTSConfigEntry.setStatus(_A)
class _HpnicfIfQoSGTSClassRuleType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_W,1),(_L,2),(_M,3),(_c,4)))
_HpnicfIfQoSGTSClassRuleType_Type.__name__=_D
_HpnicfIfQoSGTSClassRuleType_Object=MibTableColumn
hpnicfIfQoSGTSClassRuleType=_HpnicfIfQoSGTSClassRuleType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,5,1,1,1),_HpnicfIfQoSGTSClassRuleType_Type())
hpnicfIfQoSGTSClassRuleType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSGTSClassRuleType.setStatus(_A)
_HpnicfIfQoSGTSClassRuleValue_Type=Integer32
_HpnicfIfQoSGTSClassRuleValue_Object=MibTableColumn
hpnicfIfQoSGTSClassRuleValue=_HpnicfIfQoSGTSClassRuleValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,5,1,1,2),_HpnicfIfQoSGTSClassRuleValue_Type())
hpnicfIfQoSGTSClassRuleValue.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSGTSClassRuleValue.setStatus(_A)
_HpnicfIfQoSGTSCir_Type=Unsigned32
_HpnicfIfQoSGTSCir_Object=MibTableColumn
hpnicfIfQoSGTSCir=_HpnicfIfQoSGTSCir_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,5,1,1,3),_HpnicfIfQoSGTSCir_Type())
hpnicfIfQoSGTSCir.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSGTSCir.setStatus(_A)
_HpnicfIfQoSGTSCbs_Type=Unsigned32
_HpnicfIfQoSGTSCbs_Object=MibTableColumn
hpnicfIfQoSGTSCbs=_HpnicfIfQoSGTSCbs_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,5,1,1,4),_HpnicfIfQoSGTSCbs_Type())
hpnicfIfQoSGTSCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSGTSCbs.setStatus(_A)
_HpnicfIfQoSGTSEbs_Type=Unsigned32
_HpnicfIfQoSGTSEbs_Object=MibTableColumn
hpnicfIfQoSGTSEbs=_HpnicfIfQoSGTSEbs_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,5,1,1,5),_HpnicfIfQoSGTSEbs_Type())
hpnicfIfQoSGTSEbs.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSGTSEbs.setStatus(_A)
_HpnicfIfQoSGTSQueueLength_Type=Integer32
_HpnicfIfQoSGTSQueueLength_Object=MibTableColumn
hpnicfIfQoSGTSQueueLength=_HpnicfIfQoSGTSQueueLength_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,5,1,1,6),_HpnicfIfQoSGTSQueueLength_Type())
hpnicfIfQoSGTSQueueLength.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSGTSQueueLength.setStatus(_A)
_HpnicfIfQoSGTSConfigRowStatus_Type=RowStatus
_HpnicfIfQoSGTSConfigRowStatus_Object=MibTableColumn
hpnicfIfQoSGTSConfigRowStatus=_HpnicfIfQoSGTSConfigRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,5,1,1,7),_HpnicfIfQoSGTSConfigRowStatus_Type())
hpnicfIfQoSGTSConfigRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSGTSConfigRowStatus.setStatus(_A)
_HpnicfIfQoSGTSRunInfoTable_Object=MibTable
hpnicfIfQoSGTSRunInfoTable=_HpnicfIfQoSGTSRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,5,2))
if mibBuilder.loadTexts:hpnicfIfQoSGTSRunInfoTable.setStatus(_A)
_HpnicfIfQoSGTSRunInfoEntry_Object=MibTableRow
hpnicfIfQoSGTSRunInfoEntry=_HpnicfIfQoSGTSRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,5,2,1))
hpnicfIfQoSGTSRunInfoEntry.setIndexNames((0,_G,_H),(0,_E,_a),(0,_E,_b))
if mibBuilder.loadTexts:hpnicfIfQoSGTSRunInfoEntry.setStatus(_A)
_HpnicfIfQoSGTSQueueSize_Type=Integer32
_HpnicfIfQoSGTSQueueSize_Object=MibTableColumn
hpnicfIfQoSGTSQueueSize=_HpnicfIfQoSGTSQueueSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,5,2,1,1),_HpnicfIfQoSGTSQueueSize_Type())
hpnicfIfQoSGTSQueueSize.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSGTSQueueSize.setStatus(_A)
_HpnicfIfQoSGTSPassedPackets_Type=Counter64
_HpnicfIfQoSGTSPassedPackets_Object=MibTableColumn
hpnicfIfQoSGTSPassedPackets=_HpnicfIfQoSGTSPassedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,5,2,1,2),_HpnicfIfQoSGTSPassedPackets_Type())
hpnicfIfQoSGTSPassedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSGTSPassedPackets.setStatus(_A)
_HpnicfIfQoSGTSPassedBytes_Type=Counter64
_HpnicfIfQoSGTSPassedBytes_Object=MibTableColumn
hpnicfIfQoSGTSPassedBytes=_HpnicfIfQoSGTSPassedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,5,2,1,3),_HpnicfIfQoSGTSPassedBytes_Type())
hpnicfIfQoSGTSPassedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSGTSPassedBytes.setStatus(_A)
_HpnicfIfQoSGTSDiscardPackets_Type=Counter64
_HpnicfIfQoSGTSDiscardPackets_Object=MibTableColumn
hpnicfIfQoSGTSDiscardPackets=_HpnicfIfQoSGTSDiscardPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,5,2,1,4),_HpnicfIfQoSGTSDiscardPackets_Type())
hpnicfIfQoSGTSDiscardPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSGTSDiscardPackets.setStatus(_A)
_HpnicfIfQoSGTSDiscardBytes_Type=Counter64
_HpnicfIfQoSGTSDiscardBytes_Object=MibTableColumn
hpnicfIfQoSGTSDiscardBytes=_HpnicfIfQoSGTSDiscardBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,5,2,1,5),_HpnicfIfQoSGTSDiscardBytes_Type())
hpnicfIfQoSGTSDiscardBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSGTSDiscardBytes.setStatus(_A)
_HpnicfIfQoSGTSDelayedPackets_Type=Counter64
_HpnicfIfQoSGTSDelayedPackets_Object=MibTableColumn
hpnicfIfQoSGTSDelayedPackets=_HpnicfIfQoSGTSDelayedPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,5,2,1,6),_HpnicfIfQoSGTSDelayedPackets_Type())
hpnicfIfQoSGTSDelayedPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSGTSDelayedPackets.setStatus(_A)
_HpnicfIfQoSGTSDelayedBytes_Type=Counter64
_HpnicfIfQoSGTSDelayedBytes_Object=MibTableColumn
hpnicfIfQoSGTSDelayedBytes=_HpnicfIfQoSGTSDelayedBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,5,2,1,7),_HpnicfIfQoSGTSDelayedBytes_Type())
hpnicfIfQoSGTSDelayedBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSGTSDelayedBytes.setStatus(_A)
_HpnicfIfQoSWREDObjects_ObjectIdentity=ObjectIdentity
hpnicfIfQoSWREDObjects=_HpnicfIfQoSWREDObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6))
_HpnicfIfQoSWredGroupGroup_ObjectIdentity=ObjectIdentity
hpnicfIfQoSWredGroupGroup=_HpnicfIfQoSWredGroupGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1))
_HpnicfIfQoSWredGroupNextIndex_Type=Integer32
_HpnicfIfQoSWredGroupNextIndex_Object=MibScalar
hpnicfIfQoSWredGroupNextIndex=_HpnicfIfQoSWredGroupNextIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,1),_HpnicfIfQoSWredGroupNextIndex_Type())
hpnicfIfQoSWredGroupNextIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWredGroupNextIndex.setStatus(_A)
_HpnicfIfQoSWredGroupTable_Object=MibTable
hpnicfIfQoSWredGroupTable=_HpnicfIfQoSWredGroupTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,2))
if mibBuilder.loadTexts:hpnicfIfQoSWredGroupTable.setStatus(_A)
_HpnicfIfQoSWredGroupEntry_Object=MibTableRow
hpnicfIfQoSWredGroupEntry=_HpnicfIfQoSWredGroupEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,2,1))
hpnicfIfQoSWredGroupEntry.setIndexNames((0,_E,_S))
if mibBuilder.loadTexts:hpnicfIfQoSWredGroupEntry.setStatus(_A)
_HpnicfIfQoSWredGroupIndex_Type=Integer32
_HpnicfIfQoSWredGroupIndex_Object=MibTableColumn
hpnicfIfQoSWredGroupIndex=_HpnicfIfQoSWredGroupIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,2,1,1),_HpnicfIfQoSWredGroupIndex_Type())
hpnicfIfQoSWredGroupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSWredGroupIndex.setStatus(_A)
class _HpnicfIfQoSWredGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfIfQoSWredGroupName_Type.__name__=_K
_HpnicfIfQoSWredGroupName_Object=MibTableColumn
hpnicfIfQoSWredGroupName=_HpnicfIfQoSWredGroupName_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,2,1,2),_HpnicfIfQoSWredGroupName_Type())
hpnicfIfQoSWredGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSWredGroupName.setStatus(_A)
class _HpnicfIfQoSWredGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_z,0),(_d,1),('ippre',2),(_N,3),('localpre',4),('atmclp',5),('frde',6),('exp',7),(_c,8),('dropLevel',9)))
_HpnicfIfQoSWredGroupType_Type.__name__=_D
_HpnicfIfQoSWredGroupType_Object=MibTableColumn
hpnicfIfQoSWredGroupType=_HpnicfIfQoSWredGroupType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,2,1,3),_HpnicfIfQoSWredGroupType_Type())
hpnicfIfQoSWredGroupType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSWredGroupType.setStatus(_A)
class _HpnicfIfQoSWredGroupWeightingConstant_Type(Integer32):defaultValue=9;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_HpnicfIfQoSWredGroupWeightingConstant_Type.__name__=_D
_HpnicfIfQoSWredGroupWeightingConstant_Object=MibTableColumn
hpnicfIfQoSWredGroupWeightingConstant=_HpnicfIfQoSWredGroupWeightingConstant_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,2,1,4),_HpnicfIfQoSWredGroupWeightingConstant_Type())
hpnicfIfQoSWredGroupWeightingConstant.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSWredGroupWeightingConstant.setStatus(_A)
_HpnicfIfQoSWredGroupRowStatus_Type=RowStatus
_HpnicfIfQoSWredGroupRowStatus_Object=MibTableColumn
hpnicfIfQoSWredGroupRowStatus=_HpnicfIfQoSWredGroupRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,2,1,6),_HpnicfIfQoSWredGroupRowStatus_Type())
hpnicfIfQoSWredGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSWredGroupRowStatus.setStatus(_A)
_HpnicfIfQoSWredGroupContentTable_Object=MibTable
hpnicfIfQoSWredGroupContentTable=_HpnicfIfQoSWredGroupContentTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,3))
if mibBuilder.loadTexts:hpnicfIfQoSWredGroupContentTable.setStatus(_A)
_HpnicfIfQoSWredGroupContentEntry_Object=MibTableRow
hpnicfIfQoSWredGroupContentEntry=_HpnicfIfQoSWredGroupContentEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,3,1))
hpnicfIfQoSWredGroupContentEntry.setIndexNames((0,_E,_S),(0,_E,_e),(0,_E,_f))
if mibBuilder.loadTexts:hpnicfIfQoSWredGroupContentEntry.setStatus(_A)
class _HpnicfIfQoSWredGroupContentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HpnicfIfQoSWredGroupContentIndex_Type.__name__=_D
_HpnicfIfQoSWredGroupContentIndex_Object=MibTableColumn
hpnicfIfQoSWredGroupContentIndex=_HpnicfIfQoSWredGroupContentIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,3,1,1),_HpnicfIfQoSWredGroupContentIndex_Type())
hpnicfIfQoSWredGroupContentIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSWredGroupContentIndex.setStatus(_A)
class _HpnicfIfQoSWredGroupContentSubIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HpnicfIfQoSWredGroupContentSubIndex_Type.__name__=_D
_HpnicfIfQoSWredGroupContentSubIndex_Object=MibTableColumn
hpnicfIfQoSWredGroupContentSubIndex=_HpnicfIfQoSWredGroupContentSubIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,3,1,2),_HpnicfIfQoSWredGroupContentSubIndex_Type())
hpnicfIfQoSWredGroupContentSubIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSWredGroupContentSubIndex.setStatus(_A)
_HpnicfIfQoSWredLowLimit_Type=Integer32
_HpnicfIfQoSWredLowLimit_Object=MibTableColumn
hpnicfIfQoSWredLowLimit=_HpnicfIfQoSWredLowLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,3,1,3),_HpnicfIfQoSWredLowLimit_Type())
hpnicfIfQoSWredLowLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSWredLowLimit.setStatus(_A)
_HpnicfIfQoSWredHighLimit_Type=Integer32
_HpnicfIfQoSWredHighLimit_Object=MibTableColumn
hpnicfIfQoSWredHighLimit=_HpnicfIfQoSWredHighLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,3,1,4),_HpnicfIfQoSWredHighLimit_Type())
hpnicfIfQoSWredHighLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSWredHighLimit.setStatus(_A)
_HpnicfIfQoSWredDiscardProb_Type=Integer32
_HpnicfIfQoSWredDiscardProb_Object=MibTableColumn
hpnicfIfQoSWredDiscardProb=_HpnicfIfQoSWredDiscardProb_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,3,1,5),_HpnicfIfQoSWredDiscardProb_Type())
hpnicfIfQoSWredDiscardProb.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSWredDiscardProb.setStatus(_A)
class _HpnicfIfQoSWredGroupExponent_Type(Integer32):defaultValue=9;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_HpnicfIfQoSWredGroupExponent_Type.__name__=_D
_HpnicfIfQoSWredGroupExponent_Object=MibTableColumn
hpnicfIfQoSWredGroupExponent=_HpnicfIfQoSWredGroupExponent_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,3,1,6),_HpnicfIfQoSWredGroupExponent_Type())
hpnicfIfQoSWredGroupExponent.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSWredGroupExponent.setStatus(_A)
_HpnicfIfQoSWredRowStatus_Type=RowStatus
_HpnicfIfQoSWredRowStatus_Object=MibTableColumn
hpnicfIfQoSWredRowStatus=_HpnicfIfQoSWredRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,3,1,7),_HpnicfIfQoSWredRowStatus_Type())
hpnicfIfQoSWredRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSWredRowStatus.setStatus(_A)
_HpnicfIfQoSWredGroupApplyIfTable_Object=MibTable
hpnicfIfQoSWredGroupApplyIfTable=_HpnicfIfQoSWredGroupApplyIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,4))
if mibBuilder.loadTexts:hpnicfIfQoSWredGroupApplyIfTable.setStatus(_A)
_HpnicfIfQoSWredGroupApplyIfEntry_Object=MibTableRow
hpnicfIfQoSWredGroupApplyIfEntry=_HpnicfIfQoSWredGroupApplyIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,4,1))
hpnicfIfQoSWredGroupApplyIfEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hpnicfIfQoSWredGroupApplyIfEntry.setStatus(_A)
class _HpnicfIfQoSWredGroupApplyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,256))
_HpnicfIfQoSWredGroupApplyIndex_Type.__name__=_D
_HpnicfIfQoSWredGroupApplyIndex_Object=MibTableColumn
hpnicfIfQoSWredGroupApplyIndex=_HpnicfIfQoSWredGroupApplyIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,4,1,1),_HpnicfIfQoSWredGroupApplyIndex_Type())
hpnicfIfQoSWredGroupApplyIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSWredGroupApplyIndex.setStatus(_A)
_HpnicfIfQoSWredGroupApplyName_Type=OctetString
_HpnicfIfQoSWredGroupApplyName_Object=MibTableColumn
hpnicfIfQoSWredGroupApplyName=_HpnicfIfQoSWredGroupApplyName_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,4,1,2),_HpnicfIfQoSWredGroupApplyName_Type())
hpnicfIfQoSWredGroupApplyName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWredGroupApplyName.setStatus(_A)
_HpnicfIfQoSWredGroupIfRowStatus_Type=RowStatus
_HpnicfIfQoSWredGroupIfRowStatus_Object=MibTableColumn
hpnicfIfQoSWredGroupIfRowStatus=_HpnicfIfQoSWredGroupIfRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,4,1,3),_HpnicfIfQoSWredGroupIfRowStatus_Type())
hpnicfIfQoSWredGroupIfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSWredGroupIfRowStatus.setStatus(_A)
_HpnicfIfQoSWredApplyIfRunInfoTable_Object=MibTable
hpnicfIfQoSWredApplyIfRunInfoTable=_HpnicfIfQoSWredApplyIfRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,5))
if mibBuilder.loadTexts:hpnicfIfQoSWredApplyIfRunInfoTable.setStatus(_A)
_HpnicfIfQoSWredApplyIfRunInfoEntry_Object=MibTableRow
hpnicfIfQoSWredApplyIfRunInfoEntry=_HpnicfIfQoSWredApplyIfRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,5,1))
hpnicfIfQoSWredApplyIfRunInfoEntry.setIndexNames((0,_G,_H),(0,_E,_S),(0,_E,_e),(0,_E,_f))
if mibBuilder.loadTexts:hpnicfIfQoSWredApplyIfRunInfoEntry.setStatus(_A)
_HpnicfIfQoSWredPreRandomDropNum_Type=Counter64
_HpnicfIfQoSWredPreRandomDropNum_Object=MibTableColumn
hpnicfIfQoSWredPreRandomDropNum=_HpnicfIfQoSWredPreRandomDropNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,5,1,1),_HpnicfIfQoSWredPreRandomDropNum_Type())
hpnicfIfQoSWredPreRandomDropNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWredPreRandomDropNum.setStatus(_A)
_HpnicfIfQoSWredPreTailDropNum_Type=Counter64
_HpnicfIfQoSWredPreTailDropNum_Object=MibTableColumn
hpnicfIfQoSWredPreTailDropNum=_HpnicfIfQoSWredPreTailDropNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,1,5,1,2),_HpnicfIfQoSWredPreTailDropNum_Type())
hpnicfIfQoSWredPreTailDropNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWredPreTailDropNum.setStatus(_A)
_HpnicfIfQoSPortWredGroup_ObjectIdentity=ObjectIdentity
hpnicfIfQoSPortWredGroup=_HpnicfIfQoSPortWredGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,2))
_HpnicfIfQoSPortWredWeightConstantTable_Object=MibTable
hpnicfIfQoSPortWredWeightConstantTable=_HpnicfIfQoSPortWredWeightConstantTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,2,1))
if mibBuilder.loadTexts:hpnicfIfQoSPortWredWeightConstantTable.setStatus(_A)
_HpnicfIfQoSPortWredWeightConstantEntry_Object=MibTableRow
hpnicfIfQoSPortWredWeightConstantEntry=_HpnicfIfQoSPortWredWeightConstantEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,2,1,1))
hpnicfIfQoSPortWredWeightConstantEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hpnicfIfQoSPortWredWeightConstantEntry.setStatus(_A)
_HpnicfIfQoSPortWredEnable_Type=TruthValue
_HpnicfIfQoSPortWredEnable_Object=MibTableColumn
hpnicfIfQoSPortWredEnable=_HpnicfIfQoSPortWredEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,2,1,1,1),_HpnicfIfQoSPortWredEnable_Type())
hpnicfIfQoSPortWredEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSPortWredEnable.setStatus(_A)
class _HpnicfIfQoSPortWredWeightConstant_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_HpnicfIfQoSPortWredWeightConstant_Type.__name__=_D
_HpnicfIfQoSPortWredWeightConstant_Object=MibTableColumn
hpnicfIfQoSPortWredWeightConstant=_HpnicfIfQoSPortWredWeightConstant_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,2,1,1,2),_HpnicfIfQoSPortWredWeightConstant_Type())
hpnicfIfQoSPortWredWeightConstant.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSPortWredWeightConstant.setStatus(_A)
_HpnicfIfQoSPortWredWeightConstantRowStatus_Type=RowStatus
_HpnicfIfQoSPortWredWeightConstantRowStatus_Object=MibTableColumn
hpnicfIfQoSPortWredWeightConstantRowStatus=_HpnicfIfQoSPortWredWeightConstantRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,2,1,1,3),_HpnicfIfQoSPortWredWeightConstantRowStatus_Type())
hpnicfIfQoSPortWredWeightConstantRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSPortWredWeightConstantRowStatus.setStatus(_A)
_HpnicfIfQoSPortWredPreConfigTable_Object=MibTable
hpnicfIfQoSPortWredPreConfigTable=_HpnicfIfQoSPortWredPreConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,2,2))
if mibBuilder.loadTexts:hpnicfIfQoSPortWredPreConfigTable.setStatus(_A)
_HpnicfIfQoSPortWredPreConfigEntry_Object=MibTableRow
hpnicfIfQoSPortWredPreConfigEntry=_HpnicfIfQoSPortWredPreConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,2,2,1))
hpnicfIfQoSPortWredPreConfigEntry.setIndexNames((0,_G,_H),(0,_E,_g))
if mibBuilder.loadTexts:hpnicfIfQoSPortWredPreConfigEntry.setStatus(_A)
_HpnicfIfQoSPortWredPreID_Type=Integer32
_HpnicfIfQoSPortWredPreID_Object=MibTableColumn
hpnicfIfQoSPortWredPreID=_HpnicfIfQoSPortWredPreID_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,2,2,1,1),_HpnicfIfQoSPortWredPreID_Type())
hpnicfIfQoSPortWredPreID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSPortWredPreID.setStatus(_A)
_HpnicfIfQoSPortWredPreLowLimit_Type=Integer32
_HpnicfIfQoSPortWredPreLowLimit_Object=MibTableColumn
hpnicfIfQoSPortWredPreLowLimit=_HpnicfIfQoSPortWredPreLowLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,2,2,1,2),_HpnicfIfQoSPortWredPreLowLimit_Type())
hpnicfIfQoSPortWredPreLowLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSPortWredPreLowLimit.setStatus(_A)
_HpnicfIfQoSPortWredPreHighLimit_Type=Integer32
_HpnicfIfQoSPortWredPreHighLimit_Object=MibTableColumn
hpnicfIfQoSPortWredPreHighLimit=_HpnicfIfQoSPortWredPreHighLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,2,2,1,3),_HpnicfIfQoSPortWredPreHighLimit_Type())
hpnicfIfQoSPortWredPreHighLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSPortWredPreHighLimit.setStatus(_A)
_HpnicfIfQoSPortWredPreDiscardProbability_Type=Integer32
_HpnicfIfQoSPortWredPreDiscardProbability_Object=MibTableColumn
hpnicfIfQoSPortWredPreDiscardProbability=_HpnicfIfQoSPortWredPreDiscardProbability_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,2,2,1,4),_HpnicfIfQoSPortWredPreDiscardProbability_Type())
hpnicfIfQoSPortWredPreDiscardProbability.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSPortWredPreDiscardProbability.setStatus(_A)
_HpnicfIfQoSPortWredPreRowStatus_Type=RowStatus
_HpnicfIfQoSPortWredPreRowStatus_Object=MibTableColumn
hpnicfIfQoSPortWredPreRowStatus=_HpnicfIfQoSPortWredPreRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,2,2,1,5),_HpnicfIfQoSPortWredPreRowStatus_Type())
hpnicfIfQoSPortWredPreRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSPortWredPreRowStatus.setStatus(_A)
_HpnicfIfQoSPortWredRunInfoTable_Object=MibTable
hpnicfIfQoSPortWredRunInfoTable=_HpnicfIfQoSPortWredRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,2,3))
if mibBuilder.loadTexts:hpnicfIfQoSPortWredRunInfoTable.setStatus(_A)
_HpnicfIfQoSPortWredRunInfoEntry_Object=MibTableRow
hpnicfIfQoSPortWredRunInfoEntry=_HpnicfIfQoSPortWredRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,2,3,1))
hpnicfIfQoSPortWredRunInfoEntry.setIndexNames((0,_G,_H),(0,_E,_g))
if mibBuilder.loadTexts:hpnicfIfQoSPortWredRunInfoEntry.setStatus(_A)
_HpnicfIfQoSWREDTailDropNum_Type=Counter64
_HpnicfIfQoSWREDTailDropNum_Object=MibTableColumn
hpnicfIfQoSWREDTailDropNum=_HpnicfIfQoSWREDTailDropNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,2,3,1,1),_HpnicfIfQoSWREDTailDropNum_Type())
hpnicfIfQoSWREDTailDropNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWREDTailDropNum.setStatus(_A)
_HpnicfIfQoSWREDRandomDropNum_Type=Counter64
_HpnicfIfQoSWREDRandomDropNum_Object=MibTableColumn
hpnicfIfQoSWREDRandomDropNum=_HpnicfIfQoSWREDRandomDropNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,6,2,3,1,2),_HpnicfIfQoSWREDRandomDropNum_Type())
hpnicfIfQoSWREDRandomDropNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSWREDRandomDropNum.setStatus(_A)
_HpnicfIfQoSPortPriorityObjects_ObjectIdentity=ObjectIdentity
hpnicfIfQoSPortPriorityObjects=_HpnicfIfQoSPortPriorityObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,7))
_HpnicfIfQoSPortPriorityConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfIfQoSPortPriorityConfigGroup=_HpnicfIfQoSPortPriorityConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,7,1))
_HpnicfIfQoSPortPriorityTable_Object=MibTable
hpnicfIfQoSPortPriorityTable=_HpnicfIfQoSPortPriorityTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,7,1,1))
if mibBuilder.loadTexts:hpnicfIfQoSPortPriorityTable.setStatus(_A)
_HpnicfIfQoSPortPriorityEntry_Object=MibTableRow
hpnicfIfQoSPortPriorityEntry=_HpnicfIfQoSPortPriorityEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,7,1,1,1))
hpnicfIfQoSPortPriorityEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hpnicfIfQoSPortPriorityEntry.setStatus(_A)
class _HpnicfIfQoSPortPriorityValue_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_HpnicfIfQoSPortPriorityValue_Type.__name__=_D
_HpnicfIfQoSPortPriorityValue_Object=MibTableColumn
hpnicfIfQoSPortPriorityValue=_HpnicfIfQoSPortPriorityValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,7,1,1,1,1),_HpnicfIfQoSPortPriorityValue_Type())
hpnicfIfQoSPortPriorityValue.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfIfQoSPortPriorityValue.setStatus(_A)
_HpnicfIfQoSPortPirorityTrustTable_Object=MibTable
hpnicfIfQoSPortPirorityTrustTable=_HpnicfIfQoSPortPirorityTrustTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,7,1,2))
if mibBuilder.loadTexts:hpnicfIfQoSPortPirorityTrustTable.setStatus(_A)
_HpnicfIfQoSPortPirorityTrustEntry_Object=MibTableRow
hpnicfIfQoSPortPirorityTrustEntry=_HpnicfIfQoSPortPirorityTrustEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,7,1,2,1))
hpnicfIfQoSPortPirorityTrustEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hpnicfIfQoSPortPirorityTrustEntry.setStatus(_A)
class _HpnicfIfQoSPortPriorityTrustTrustType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('untrust',1),(_d,2),(_N,3),('exp',4),(_A0,5),('dot11e',6),('auto',7)))
_HpnicfIfQoSPortPriorityTrustTrustType_Type.__name__=_D
_HpnicfIfQoSPortPriorityTrustTrustType_Object=MibTableColumn
hpnicfIfQoSPortPriorityTrustTrustType=_HpnicfIfQoSPortPriorityTrustTrustType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,7,1,2,1,1),_HpnicfIfQoSPortPriorityTrustTrustType_Type())
hpnicfIfQoSPortPriorityTrustTrustType.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfIfQoSPortPriorityTrustTrustType.setStatus(_A)
class _HpnicfIfQoSPortPriorityTrustOvercastType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noOvercast',1),('overcastDSCP',2),('overcastCOS',3),('overcast',4)))
_HpnicfIfQoSPortPriorityTrustOvercastType_Type.__name__=_D
_HpnicfIfQoSPortPriorityTrustOvercastType_Object=MibTableColumn
hpnicfIfQoSPortPriorityTrustOvercastType=_HpnicfIfQoSPortPriorityTrustOvercastType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,7,1,2,1,2),_HpnicfIfQoSPortPriorityTrustOvercastType_Type())
hpnicfIfQoSPortPriorityTrustOvercastType.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfIfQoSPortPriorityTrustOvercastType.setStatus(_A)
_HpnicfIfQoSMapObjects_ObjectIdentity=ObjectIdentity
hpnicfIfQoSMapObjects=_HpnicfIfQoSMapObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,9))
_HpnicfIfQoSPriMapConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfIfQoSPriMapConfigGroup=_HpnicfIfQoSPriMapConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,9,1))
_HpnicfIfQoSPriMapGroupNextIndex_Type=Integer32
_HpnicfIfQoSPriMapGroupNextIndex_Object=MibScalar
hpnicfIfQoSPriMapGroupNextIndex=_HpnicfIfQoSPriMapGroupNextIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,9,1,1),_HpnicfIfQoSPriMapGroupNextIndex_Type())
hpnicfIfQoSPriMapGroupNextIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfIfQoSPriMapGroupNextIndex.setStatus(_A)
_HpnicfIfQoSPriMapGroupTable_Object=MibTable
hpnicfIfQoSPriMapGroupTable=_HpnicfIfQoSPriMapGroupTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,9,1,2))
if mibBuilder.loadTexts:hpnicfIfQoSPriMapGroupTable.setStatus(_A)
_HpnicfIfQoSPriMapGroupEntry_Object=MibTableRow
hpnicfIfQoSPriMapGroupEntry=_HpnicfIfQoSPriMapGroupEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,9,1,2,1))
hpnicfIfQoSPriMapGroupEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:hpnicfIfQoSPriMapGroupEntry.setStatus(_A)
_HpnicfIfQoSPriMapGroupIndex_Type=Integer32
_HpnicfIfQoSPriMapGroupIndex_Object=MibTableColumn
hpnicfIfQoSPriMapGroupIndex=_HpnicfIfQoSPriMapGroupIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,9,1,2,1,1),_HpnicfIfQoSPriMapGroupIndex_Type())
hpnicfIfQoSPriMapGroupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSPriMapGroupIndex.setStatus(_A)
class _HpnicfIfQoSPriMapGroupType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_z,1),('dot1p-dp',2),('dot1p-dscp',3),('dot1p-lp',4),('dscp-dot1p',5),('dscp-dp',6),('dscp-dscp',7),('dscp-lp',8),('exp-dp',9),('exp-lp',10)))
_HpnicfIfQoSPriMapGroupType_Type.__name__=_D
_HpnicfIfQoSPriMapGroupType_Object=MibTableColumn
hpnicfIfQoSPriMapGroupType=_HpnicfIfQoSPriMapGroupType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,9,1,2,1,2),_HpnicfIfQoSPriMapGroupType_Type())
hpnicfIfQoSPriMapGroupType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSPriMapGroupType.setStatus(_A)
class _HpnicfIfQoSPriMapGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfIfQoSPriMapGroupName_Type.__name__=_K
_HpnicfIfQoSPriMapGroupName_Object=MibTableColumn
hpnicfIfQoSPriMapGroupName=_HpnicfIfQoSPriMapGroupName_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,9,1,2,1,3),_HpnicfIfQoSPriMapGroupName_Type())
hpnicfIfQoSPriMapGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSPriMapGroupName.setStatus(_A)
_HpnicfIfQoSPriMapGroupRowStatus_Type=RowStatus
_HpnicfIfQoSPriMapGroupRowStatus_Object=MibTableColumn
hpnicfIfQoSPriMapGroupRowStatus=_HpnicfIfQoSPriMapGroupRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,9,1,2,1,4),_HpnicfIfQoSPriMapGroupRowStatus_Type())
hpnicfIfQoSPriMapGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSPriMapGroupRowStatus.setStatus(_A)
_HpnicfIfQoSPriMapContentTable_Object=MibTable
hpnicfIfQoSPriMapContentTable=_HpnicfIfQoSPriMapContentTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,9,1,3))
if mibBuilder.loadTexts:hpnicfIfQoSPriMapContentTable.setStatus(_A)
_HpnicfIfQoSPriMapContentEntry_Object=MibTableRow
hpnicfIfQoSPriMapContentEntry=_HpnicfIfQoSPriMapContentEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,9,1,3,1))
hpnicfIfQoSPriMapContentEntry.setIndexNames((0,_E,_h),(0,_E,_A1))
if mibBuilder.loadTexts:hpnicfIfQoSPriMapContentEntry.setStatus(_A)
class _HpnicfIfQoSPriMapGroupImportValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HpnicfIfQoSPriMapGroupImportValue_Type.__name__=_D
_HpnicfIfQoSPriMapGroupImportValue_Object=MibTableColumn
hpnicfIfQoSPriMapGroupImportValue=_HpnicfIfQoSPriMapGroupImportValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,9,1,3,1,1),_HpnicfIfQoSPriMapGroupImportValue_Type())
hpnicfIfQoSPriMapGroupImportValue.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSPriMapGroupImportValue.setStatus(_A)
class _HpnicfIfQoSPriMapGroupExportValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HpnicfIfQoSPriMapGroupExportValue_Type.__name__=_D
_HpnicfIfQoSPriMapGroupExportValue_Object=MibTableColumn
hpnicfIfQoSPriMapGroupExportValue=_HpnicfIfQoSPriMapGroupExportValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,9,1,3,1,2),_HpnicfIfQoSPriMapGroupExportValue_Type())
hpnicfIfQoSPriMapGroupExportValue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSPriMapGroupExportValue.setStatus(_A)
_HpnicfIfQoSPriMapContentRowStatus_Type=RowStatus
_HpnicfIfQoSPriMapContentRowStatus_Object=MibTableColumn
hpnicfIfQoSPriMapContentRowStatus=_HpnicfIfQoSPriMapContentRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,9,1,3,1,3),_HpnicfIfQoSPriMapContentRowStatus_Type())
hpnicfIfQoSPriMapContentRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSPriMapContentRowStatus.setStatus(_A)
_HpnicfIfQoSPrePriMapTable_Object=MibTable
hpnicfIfQoSPrePriMapTable=_HpnicfIfQoSPrePriMapTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,9,1,4))
if mibBuilder.loadTexts:hpnicfIfQoSPrePriMapTable.setStatus(_A)
_HpnicfIfQoSPrePriMapEntry_Object=MibTableRow
hpnicfIfQoSPrePriMapEntry=_HpnicfIfQoSPrePriMapEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,9,1,4,1))
hpnicfIfQoSPrePriMapEntry.setIndexNames((0,_E,_A2),(0,_E,_A3),(0,_E,_A4),(0,_E,_A5))
if mibBuilder.loadTexts:hpnicfIfQoSPrePriMapEntry.setStatus(_A)
class _HpnicfIfQoSPrePriMapTableType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34)));namedValues=NamedValues(*(('dot1pToLp',1),('dot1pToDp',2),('expToLp',3),('dscpToLp',4),('expToDp',5),('dscpToDp',6),('dscpToDot1p',7),('dot1pToDscp',8),('dscpToDscp',9),('dscpToExp',10),('expToDscp',11),('expToDot1p',12),('expToExp',13),('lpToDot1p',14),('dot1pToRpr',15),('dscpToRpr',16),('expToRpr',17),('ippreToRpr',18),('upToDot1p',19),('upToDscp',20),('upToExp',21),('upToDp',22),('upToLp',23),('upToRpr',24),('upToFc',25),('lpTodscp',26),('dot11eToLp',27),('lpToDot11e',28),('lpToLp',29),('dot1pToExp',30),('lpToExp',31),('lpToDp',32),('upToUp',33),('dot1pToDot1p',34)))
_HpnicfIfQoSPrePriMapTableType_Type.__name__=_D
_HpnicfIfQoSPrePriMapTableType_Object=MibTableColumn
hpnicfIfQoSPrePriMapTableType=_HpnicfIfQoSPrePriMapTableType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,9,1,4,1,1),_HpnicfIfQoSPrePriMapTableType_Type())
hpnicfIfQoSPrePriMapTableType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSPrePriMapTableType.setStatus(_A)
class _HpnicfIfQoSPrePriMapTableColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noColor',1),('green',2),('yellow',3),('red',4)))
_HpnicfIfQoSPrePriMapTableColor_Type.__name__=_D
_HpnicfIfQoSPrePriMapTableColor_Object=MibTableColumn
hpnicfIfQoSPrePriMapTableColor=_HpnicfIfQoSPrePriMapTableColor_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,9,1,4,1,2),_HpnicfIfQoSPrePriMapTableColor_Type())
hpnicfIfQoSPrePriMapTableColor.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSPrePriMapTableColor.setStatus(_A)
class _HpnicfIfQoSPrePriMapTableDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noDirection',1),(_j,2),(_k,3)))
_HpnicfIfQoSPrePriMapTableDirection_Type.__name__=_D
_HpnicfIfQoSPrePriMapTableDirection_Object=MibTableColumn
hpnicfIfQoSPrePriMapTableDirection=_HpnicfIfQoSPrePriMapTableDirection_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,9,1,4,1,3),_HpnicfIfQoSPrePriMapTableDirection_Type())
hpnicfIfQoSPrePriMapTableDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSPrePriMapTableDirection.setStatus(_A)
class _HpnicfIfQoSPrePriMapTableImportValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HpnicfIfQoSPrePriMapTableImportValue_Type.__name__=_D
_HpnicfIfQoSPrePriMapTableImportValue_Object=MibTableColumn
hpnicfIfQoSPrePriMapTableImportValue=_HpnicfIfQoSPrePriMapTableImportValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,9,1,4,1,4),_HpnicfIfQoSPrePriMapTableImportValue_Type())
hpnicfIfQoSPrePriMapTableImportValue.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIfQoSPrePriMapTableImportValue.setStatus(_A)
class _HpnicfIfQoSPrePriMapTableExportValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_HpnicfIfQoSPrePriMapTableExportValue_Type.__name__=_D
_HpnicfIfQoSPrePriMapTableExportValue_Object=MibTableColumn
hpnicfIfQoSPrePriMapTableExportValue=_HpnicfIfQoSPrePriMapTableExportValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,9,1,4,1,5),_HpnicfIfQoSPrePriMapTableExportValue_Type())
hpnicfIfQoSPrePriMapTableExportValue.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfIfQoSPrePriMapTableExportValue.setStatus(_A)
_HpnicfIfQoSL3PlusObjects_ObjectIdentity=ObjectIdentity
hpnicfIfQoSL3PlusObjects=_HpnicfIfQoSL3PlusObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,10))
_HpnicfIfQoSPortBindingGroup_ObjectIdentity=ObjectIdentity
hpnicfIfQoSPortBindingGroup=_HpnicfIfQoSPortBindingGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,10,1))
_HpnicfIfQoSPortBindingTable_Object=MibTable
hpnicfIfQoSPortBindingTable=_HpnicfIfQoSPortBindingTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,10,1,1))
if mibBuilder.loadTexts:hpnicfIfQoSPortBindingTable.setStatus(_A)
_HpnicfIfQoSPortBindingEntry_Object=MibTableRow
hpnicfIfQoSPortBindingEntry=_HpnicfIfQoSPortBindingEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,10,1,1,1))
hpnicfIfQoSPortBindingEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hpnicfIfQoSPortBindingEntry.setStatus(_A)
_HpnicfIfQoSBindingIf_Type=Integer32
_HpnicfIfQoSBindingIf_Object=MibTableColumn
hpnicfIfQoSBindingIf=_HpnicfIfQoSBindingIf_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,10,1,1,1,1),_HpnicfIfQoSBindingIf_Type())
hpnicfIfQoSBindingIf.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSBindingIf.setStatus(_A)
_HpnicfIfQoSBindingRowStatus_Type=RowStatus
_HpnicfIfQoSBindingRowStatus_Object=MibTableColumn
hpnicfIfQoSBindingRowStatus=_HpnicfIfQoSBindingRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,10,1,1,1,2),_HpnicfIfQoSBindingRowStatus_Type())
hpnicfIfQoSBindingRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIfQoSBindingRowStatus.setStatus(_A)
_HpnicfQoSTraStaObjects_ObjectIdentity=ObjectIdentity
hpnicfQoSTraStaObjects=_HpnicfQoSTraStaObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,11))
_HpnicfQoSTraStaConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfQoSTraStaConfigGroup=_HpnicfQoSTraStaConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,11,1))
_HpnicfQoSIfTraStaConfigInfoTable_Object=MibTable
hpnicfQoSIfTraStaConfigInfoTable=_HpnicfQoSIfTraStaConfigInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,11,1,1))
if mibBuilder.loadTexts:hpnicfQoSIfTraStaConfigInfoTable.setStatus(_A)
_HpnicfQoSIfTraStaConfigInfoEntry_Object=MibTableRow
hpnicfQoSIfTraStaConfigInfoEntry=_HpnicfQoSIfTraStaConfigInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,11,1,1,1))
hpnicfQoSIfTraStaConfigInfoEntry.setIndexNames((0,_G,_H),(0,_E,_A6))
if mibBuilder.loadTexts:hpnicfQoSIfTraStaConfigInfoEntry.setStatus(_A)
_HpnicfQoSIfTraStaConfigDirection_Type=Direction
_HpnicfQoSIfTraStaConfigDirection_Object=MibTableColumn
hpnicfQoSIfTraStaConfigDirection=_HpnicfQoSIfTraStaConfigDirection_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,11,1,1,1,1),_HpnicfQoSIfTraStaConfigDirection_Type())
hpnicfQoSIfTraStaConfigDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfQoSIfTraStaConfigDirection.setStatus(_A)
class _HpnicfQoSIfTraStaConfigQueue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_HpnicfQoSIfTraStaConfigQueue_Type.__name__=_K
_HpnicfQoSIfTraStaConfigQueue_Object=MibTableColumn
hpnicfQoSIfTraStaConfigQueue=_HpnicfQoSIfTraStaConfigQueue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,11,1,1,1,2),_HpnicfQoSIfTraStaConfigQueue_Type())
hpnicfQoSIfTraStaConfigQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSIfTraStaConfigQueue.setStatus(_A)
class _HpnicfQoSIfTraStaConfigDot1p_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_HpnicfQoSIfTraStaConfigDot1p_Type.__name__=_K
_HpnicfQoSIfTraStaConfigDot1p_Object=MibTableColumn
hpnicfQoSIfTraStaConfigDot1p=_HpnicfQoSIfTraStaConfigDot1p_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,11,1,1,1,3),_HpnicfQoSIfTraStaConfigDot1p_Type())
hpnicfQoSIfTraStaConfigDot1p.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSIfTraStaConfigDot1p.setStatus(_A)
class _HpnicfQoSIfTraStaConfigDscp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_HpnicfQoSIfTraStaConfigDscp_Type.__name__=_K
_HpnicfQoSIfTraStaConfigDscp_Object=MibTableColumn
hpnicfQoSIfTraStaConfigDscp=_HpnicfQoSIfTraStaConfigDscp_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,11,1,1,1,4),_HpnicfQoSIfTraStaConfigDscp_Type())
hpnicfQoSIfTraStaConfigDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSIfTraStaConfigDscp.setStatus(_A)
class _HpnicfQoSIfTraStaConfigVlan_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(512,512));fixedLength=512
_HpnicfQoSIfTraStaConfigVlan_Type.__name__=_K
_HpnicfQoSIfTraStaConfigVlan_Object=MibTableColumn
hpnicfQoSIfTraStaConfigVlan=_HpnicfQoSIfTraStaConfigVlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,11,1,1,1,5),_HpnicfQoSIfTraStaConfigVlan_Type())
hpnicfQoSIfTraStaConfigVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSIfTraStaConfigVlan.setStatus(_A)
_HpnicfQoSIfTraStaConfigStatus_Type=RowStatus
_HpnicfQoSIfTraStaConfigStatus_Object=MibTableColumn
hpnicfQoSIfTraStaConfigStatus=_HpnicfQoSIfTraStaConfigStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,11,1,1,1,6),_HpnicfQoSIfTraStaConfigStatus_Type())
hpnicfQoSIfTraStaConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSIfTraStaConfigStatus.setStatus(_A)
_HpnicfQoSTraStaRunGroup_ObjectIdentity=ObjectIdentity
hpnicfQoSTraStaRunGroup=_HpnicfQoSTraStaRunGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,11,2))
_HpnicfQoSIfTraStaRunInfoTable_Object=MibTable
hpnicfQoSIfTraStaRunInfoTable=_HpnicfQoSIfTraStaRunInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,11,2,1))
if mibBuilder.loadTexts:hpnicfQoSIfTraStaRunInfoTable.setStatus(_A)
_HpnicfQoSIfTraStaRunInfoEntry_Object=MibTableRow
hpnicfQoSIfTraStaRunInfoEntry=_HpnicfQoSIfTraStaRunInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,11,2,1,1))
hpnicfQoSIfTraStaRunInfoEntry.setIndexNames((0,_G,_H),(0,_E,_A7),(0,_E,_A8),(0,_E,_A9))
if mibBuilder.loadTexts:hpnicfQoSIfTraStaRunInfoEntry.setStatus(_A)
class _HpnicfQoSIfTraStaRunObjectType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_c,1),(_d,2),(_N,3),('vlanID',4)))
_HpnicfQoSIfTraStaRunObjectType_Type.__name__=_D
_HpnicfQoSIfTraStaRunObjectType_Object=MibTableColumn
hpnicfQoSIfTraStaRunObjectType=_HpnicfQoSIfTraStaRunObjectType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,11,2,1,1,1),_HpnicfQoSIfTraStaRunObjectType_Type())
hpnicfQoSIfTraStaRunObjectType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfQoSIfTraStaRunObjectType.setStatus(_A)
_HpnicfQoSIfTraStaRunObjectValue_Type=Integer32
_HpnicfQoSIfTraStaRunObjectValue_Object=MibTableColumn
hpnicfQoSIfTraStaRunObjectValue=_HpnicfQoSIfTraStaRunObjectValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,11,2,1,1,2),_HpnicfQoSIfTraStaRunObjectValue_Type())
hpnicfQoSIfTraStaRunObjectValue.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfQoSIfTraStaRunObjectValue.setStatus(_A)
_HpnicfQoSIfTraStaRunDirection_Type=Direction
_HpnicfQoSIfTraStaRunDirection_Object=MibTableColumn
hpnicfQoSIfTraStaRunDirection=_HpnicfQoSIfTraStaRunDirection_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,11,2,1,1,3),_HpnicfQoSIfTraStaRunDirection_Type())
hpnicfQoSIfTraStaRunDirection.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfQoSIfTraStaRunDirection.setStatus(_A)
_HpnicfQoSIfTraStaRunPassPackets_Type=Counter64
_HpnicfQoSIfTraStaRunPassPackets_Object=MibTableColumn
hpnicfQoSIfTraStaRunPassPackets=_HpnicfQoSIfTraStaRunPassPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,11,2,1,1,4),_HpnicfQoSIfTraStaRunPassPackets_Type())
hpnicfQoSIfTraStaRunPassPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfQoSIfTraStaRunPassPackets.setStatus(_A)
_HpnicfQoSIfTraStaRunDropPackets_Type=Counter64
_HpnicfQoSIfTraStaRunDropPackets_Object=MibTableColumn
hpnicfQoSIfTraStaRunDropPackets=_HpnicfQoSIfTraStaRunDropPackets_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,11,2,1,1,5),_HpnicfQoSIfTraStaRunDropPackets_Type())
hpnicfQoSIfTraStaRunDropPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfQoSIfTraStaRunDropPackets.setStatus(_A)
_HpnicfQoSIfTraStaRunPassBytes_Type=Counter64
_HpnicfQoSIfTraStaRunPassBytes_Object=MibTableColumn
hpnicfQoSIfTraStaRunPassBytes=_HpnicfQoSIfTraStaRunPassBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,11,2,1,1,6),_HpnicfQoSIfTraStaRunPassBytes_Type())
hpnicfQoSIfTraStaRunPassBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfQoSIfTraStaRunPassBytes.setStatus(_A)
_HpnicfQoSIfTraStaRunDropBytes_Type=Counter64
_HpnicfQoSIfTraStaRunDropBytes_Object=MibTableColumn
hpnicfQoSIfTraStaRunDropBytes=_HpnicfQoSIfTraStaRunDropBytes_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,11,2,1,1,7),_HpnicfQoSIfTraStaRunDropBytes_Type())
hpnicfQoSIfTraStaRunDropBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfQoSIfTraStaRunDropBytes.setStatus(_A)
_HpnicfQoSIfTraStaRunPassPPS_Type=Counter64
_HpnicfQoSIfTraStaRunPassPPS_Object=MibTableColumn
hpnicfQoSIfTraStaRunPassPPS=_HpnicfQoSIfTraStaRunPassPPS_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,11,2,1,1,8),_HpnicfQoSIfTraStaRunPassPPS_Type())
hpnicfQoSIfTraStaRunPassPPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfQoSIfTraStaRunPassPPS.setStatus(_A)
_HpnicfQoSIfTraStaRunPassBPS_Type=Counter64
_HpnicfQoSIfTraStaRunPassBPS_Object=MibTableColumn
hpnicfQoSIfTraStaRunPassBPS=_HpnicfQoSIfTraStaRunPassBPS_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,11,2,1,1,9),_HpnicfQoSIfTraStaRunPassBPS_Type())
hpnicfQoSIfTraStaRunPassBPS.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfQoSIfTraStaRunPassBPS.setStatus(_A)
_HpnicfQoSGlobalPriorityObject_ObjectIdentity=ObjectIdentity
hpnicfQoSGlobalPriorityObject=_HpnicfQoSGlobalPriorityObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12))
_HpnicfQoSRemarkTcpPortPriTable_Object=MibTable
hpnicfQoSRemarkTcpPortPriTable=_HpnicfQoSRemarkTcpPortPriTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,1))
if mibBuilder.loadTexts:hpnicfQoSRemarkTcpPortPriTable.setStatus(_A)
_HpnicfQoSRemarkTcpPortPriEntry_Object=MibTableRow
hpnicfQoSRemarkTcpPortPriEntry=_HpnicfQoSRemarkTcpPortPriEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,1,1))
hpnicfQoSRemarkTcpPortPriEntry.setIndexNames((0,_E,_AA))
if mibBuilder.loadTexts:hpnicfQoSRemarkTcpPortPriEntry.setStatus(_A)
class _HpnicfQoSRemarkTcpPortStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfQoSRemarkTcpPortStart_Type.__name__=_D
_HpnicfQoSRemarkTcpPortStart_Object=MibTableColumn
hpnicfQoSRemarkTcpPortStart=_HpnicfQoSRemarkTcpPortStart_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,1,1,1),_HpnicfQoSRemarkTcpPortStart_Type())
hpnicfQoSRemarkTcpPortStart.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfQoSRemarkTcpPortStart.setStatus(_A)
class _HpnicfQoSRemarkTcpPortEnd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfQoSRemarkTcpPortEnd_Type.__name__=_D
_HpnicfQoSRemarkTcpPortEnd_Object=MibTableColumn
hpnicfQoSRemarkTcpPortEnd=_HpnicfQoSRemarkTcpPortEnd_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,1,1,2),_HpnicfQoSRemarkTcpPortEnd_Type())
hpnicfQoSRemarkTcpPortEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSRemarkTcpPortEnd.setStatus(_A)
class _HpnicfQoSRemarkTcpPortType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ipAll',1),('ipv4',2),('ipv6',3)))
_HpnicfQoSRemarkTcpPortType_Type.__name__=_D
_HpnicfQoSRemarkTcpPortType_Object=MibTableColumn
hpnicfQoSRemarkTcpPortType=_HpnicfQoSRemarkTcpPortType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,1,1,3),_HpnicfQoSRemarkTcpPortType_Type())
hpnicfQoSRemarkTcpPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSRemarkTcpPortType.setStatus(_A)
class _HpnicfQoSRemarkTcpPortDot1p_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpnicfQoSRemarkTcpPortDot1p_Type.__name__=_J
_HpnicfQoSRemarkTcpPortDot1p_Object=MibTableColumn
hpnicfQoSRemarkTcpPortDot1p=_HpnicfQoSRemarkTcpPortDot1p_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,1,1,4),_HpnicfQoSRemarkTcpPortDot1p_Type())
hpnicfQoSRemarkTcpPortDot1p.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSRemarkTcpPortDot1p.setStatus(_A)
class _HpnicfQoSRemarkTcpPortDscp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HpnicfQoSRemarkTcpPortDscp_Type.__name__=_J
_HpnicfQoSRemarkTcpPortDscp_Object=MibTableColumn
hpnicfQoSRemarkTcpPortDscp=_HpnicfQoSRemarkTcpPortDscp_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,1,1,5),_HpnicfQoSRemarkTcpPortDscp_Type())
hpnicfQoSRemarkTcpPortDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSRemarkTcpPortDscp.setStatus(_A)
_HpnicfQoSRemarkTcpPortRowStatus_Type=RowStatus
_HpnicfQoSRemarkTcpPortRowStatus_Object=MibTableColumn
hpnicfQoSRemarkTcpPortRowStatus=_HpnicfQoSRemarkTcpPortRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,1,1,6),_HpnicfQoSRemarkTcpPortRowStatus_Type())
hpnicfQoSRemarkTcpPortRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSRemarkTcpPortRowStatus.setStatus(_A)
_HpnicfQoSRemarkUdpPortPriTable_Object=MibTable
hpnicfQoSRemarkUdpPortPriTable=_HpnicfQoSRemarkUdpPortPriTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,2))
if mibBuilder.loadTexts:hpnicfQoSRemarkUdpPortPriTable.setStatus(_A)
_HpnicfQoSRemarkUdpPortPriEntry_Object=MibTableRow
hpnicfQoSRemarkUdpPortPriEntry=_HpnicfQoSRemarkUdpPortPriEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,2,1))
hpnicfQoSRemarkUdpPortPriEntry.setIndexNames((0,_E,_AB))
if mibBuilder.loadTexts:hpnicfQoSRemarkUdpPortPriEntry.setStatus(_A)
class _HpnicfQoSRemarkUdpPortStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfQoSRemarkUdpPortStart_Type.__name__=_D
_HpnicfQoSRemarkUdpPortStart_Object=MibTableColumn
hpnicfQoSRemarkUdpPortStart=_HpnicfQoSRemarkUdpPortStart_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,2,1,1),_HpnicfQoSRemarkUdpPortStart_Type())
hpnicfQoSRemarkUdpPortStart.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfQoSRemarkUdpPortStart.setStatus(_A)
class _HpnicfQoSRemarkUdpPortEnd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfQoSRemarkUdpPortEnd_Type.__name__=_D
_HpnicfQoSRemarkUdpPortEnd_Object=MibTableColumn
hpnicfQoSRemarkUdpPortEnd=_HpnicfQoSRemarkUdpPortEnd_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,2,1,2),_HpnicfQoSRemarkUdpPortEnd_Type())
hpnicfQoSRemarkUdpPortEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSRemarkUdpPortEnd.setStatus(_A)
class _HpnicfQoSRemarkUdpPortType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ipAll',1),('ipv4',2),('ipv6',3)))
_HpnicfQoSRemarkUdpPortType_Type.__name__=_D
_HpnicfQoSRemarkUdpPortType_Object=MibTableColumn
hpnicfQoSRemarkUdpPortType=_HpnicfQoSRemarkUdpPortType_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,2,1,3),_HpnicfQoSRemarkUdpPortType_Type())
hpnicfQoSRemarkUdpPortType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSRemarkUdpPortType.setStatus(_A)
class _HpnicfQoSRemarkUdpPortDot1p_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpnicfQoSRemarkUdpPortDot1p_Type.__name__=_J
_HpnicfQoSRemarkUdpPortDot1p_Object=MibTableColumn
hpnicfQoSRemarkUdpPortDot1p=_HpnicfQoSRemarkUdpPortDot1p_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,2,1,4),_HpnicfQoSRemarkUdpPortDot1p_Type())
hpnicfQoSRemarkUdpPortDot1p.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSRemarkUdpPortDot1p.setStatus(_A)
class _HpnicfQoSRemarkUdpPortDscp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HpnicfQoSRemarkUdpPortDscp_Type.__name__=_J
_HpnicfQoSRemarkUdpPortDscp_Object=MibTableColumn
hpnicfQoSRemarkUdpPortDscp=_HpnicfQoSRemarkUdpPortDscp_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,2,1,5),_HpnicfQoSRemarkUdpPortDscp_Type())
hpnicfQoSRemarkUdpPortDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSRemarkUdpPortDscp.setStatus(_A)
_HpnicfQoSRemarkUdpPortRowStatus_Type=RowStatus
_HpnicfQoSRemarkUdpPortRowStatus_Object=MibTableColumn
hpnicfQoSRemarkUdpPortRowStatus=_HpnicfQoSRemarkUdpPortRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,2,1,6),_HpnicfQoSRemarkUdpPortRowStatus_Type())
hpnicfQoSRemarkUdpPortRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSRemarkUdpPortRowStatus.setStatus(_A)
_HpnicfQoSRemarkIPv4AddrPriTable_Object=MibTable
hpnicfQoSRemarkIPv4AddrPriTable=_HpnicfQoSRemarkIPv4AddrPriTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,3))
if mibBuilder.loadTexts:hpnicfQoSRemarkIPv4AddrPriTable.setStatus(_A)
_HpnicfQoSRemarkIPv4AddrPriEntry_Object=MibTableRow
hpnicfQoSRemarkIPv4AddrPriEntry=_HpnicfQoSRemarkIPv4AddrPriEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,3,1))
hpnicfQoSRemarkIPv4AddrPriEntry.setIndexNames((0,_E,_AC))
if mibBuilder.loadTexts:hpnicfQoSRemarkIPv4AddrPriEntry.setStatus(_A)
_HpnicfQoSRemarkIPv4AddrValue_Type=IpAddress
_HpnicfQoSRemarkIPv4AddrValue_Object=MibTableColumn
hpnicfQoSRemarkIPv4AddrValue=_HpnicfQoSRemarkIPv4AddrValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,3,1,1),_HpnicfQoSRemarkIPv4AddrValue_Type())
hpnicfQoSRemarkIPv4AddrValue.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfQoSRemarkIPv4AddrValue.setStatus(_A)
_HpnicfQoSRemarkIPv4AddrMask_Type=IpAddress
_HpnicfQoSRemarkIPv4AddrMask_Object=MibTableColumn
hpnicfQoSRemarkIPv4AddrMask=_HpnicfQoSRemarkIPv4AddrMask_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,3,1,2),_HpnicfQoSRemarkIPv4AddrMask_Type())
hpnicfQoSRemarkIPv4AddrMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSRemarkIPv4AddrMask.setStatus(_A)
class _HpnicfQoSRemarkIPv4AddrMaskLength_Type(Unsigned32):defaultValue=32;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32),ValueRangeConstraint(4294967295,4294967295))
_HpnicfQoSRemarkIPv4AddrMaskLength_Type.__name__=_J
_HpnicfQoSRemarkIPv4AddrMaskLength_Object=MibTableColumn
hpnicfQoSRemarkIPv4AddrMaskLength=_HpnicfQoSRemarkIPv4AddrMaskLength_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,3,1,3),_HpnicfQoSRemarkIPv4AddrMaskLength_Type())
hpnicfQoSRemarkIPv4AddrMaskLength.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSRemarkIPv4AddrMaskLength.setStatus(_A)
class _HpnicfQoSRemarkIPv4AddrDot1p_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpnicfQoSRemarkIPv4AddrDot1p_Type.__name__=_J
_HpnicfQoSRemarkIPv4AddrDot1p_Object=MibTableColumn
hpnicfQoSRemarkIPv4AddrDot1p=_HpnicfQoSRemarkIPv4AddrDot1p_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,3,1,4),_HpnicfQoSRemarkIPv4AddrDot1p_Type())
hpnicfQoSRemarkIPv4AddrDot1p.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSRemarkIPv4AddrDot1p.setStatus(_A)
class _HpnicfQoSRemarkIPv4AddrDscp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HpnicfQoSRemarkIPv4AddrDscp_Type.__name__=_J
_HpnicfQoSRemarkIPv4AddrDscp_Object=MibTableColumn
hpnicfQoSRemarkIPv4AddrDscp=_HpnicfQoSRemarkIPv4AddrDscp_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,3,1,5),_HpnicfQoSRemarkIPv4AddrDscp_Type())
hpnicfQoSRemarkIPv4AddrDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSRemarkIPv4AddrDscp.setStatus(_A)
_HpnicfQoSRemarkIPv4AddrRowStatus_Type=RowStatus
_HpnicfQoSRemarkIPv4AddrRowStatus_Object=MibTableColumn
hpnicfQoSRemarkIPv4AddrRowStatus=_HpnicfQoSRemarkIPv4AddrRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,3,1,6),_HpnicfQoSRemarkIPv4AddrRowStatus_Type())
hpnicfQoSRemarkIPv4AddrRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSRemarkIPv4AddrRowStatus.setStatus(_A)
_HpnicfQoSRemarkIPv6AddrPriTable_Object=MibTable
hpnicfQoSRemarkIPv6AddrPriTable=_HpnicfQoSRemarkIPv6AddrPriTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,4))
if mibBuilder.loadTexts:hpnicfQoSRemarkIPv6AddrPriTable.setStatus(_A)
_HpnicfQoSRemarkIPv6AddrPriEntry_Object=MibTableRow
hpnicfQoSRemarkIPv6AddrPriEntry=_HpnicfQoSRemarkIPv6AddrPriEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,4,1))
hpnicfQoSRemarkIPv6AddrPriEntry.setIndexNames((0,_E,_AD))
if mibBuilder.loadTexts:hpnicfQoSRemarkIPv6AddrPriEntry.setStatus(_A)
_HpnicfQoSRemarkIPv6AddrValue_Type=InetAddressIPv6
_HpnicfQoSRemarkIPv6AddrValue_Object=MibTableColumn
hpnicfQoSRemarkIPv6AddrValue=_HpnicfQoSRemarkIPv6AddrValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,4,1,1),_HpnicfQoSRemarkIPv6AddrValue_Type())
hpnicfQoSRemarkIPv6AddrValue.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfQoSRemarkIPv6AddrValue.setStatus(_A)
class _HpnicfQoSRemarkIPv6AddrPrefixLength_Type(InetAddressPrefixLength):defaultValue=128
_HpnicfQoSRemarkIPv6AddrPrefixLength_Type.__name__=_i
_HpnicfQoSRemarkIPv6AddrPrefixLength_Object=MibTableColumn
hpnicfQoSRemarkIPv6AddrPrefixLength=_HpnicfQoSRemarkIPv6AddrPrefixLength_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,4,1,2),_HpnicfQoSRemarkIPv6AddrPrefixLength_Type())
hpnicfQoSRemarkIPv6AddrPrefixLength.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSRemarkIPv6AddrPrefixLength.setStatus(_A)
class _HpnicfQoSRemarkIPv6AddrDot1p_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpnicfQoSRemarkIPv6AddrDot1p_Type.__name__=_J
_HpnicfQoSRemarkIPv6AddrDot1p_Object=MibTableColumn
hpnicfQoSRemarkIPv6AddrDot1p=_HpnicfQoSRemarkIPv6AddrDot1p_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,4,1,3),_HpnicfQoSRemarkIPv6AddrDot1p_Type())
hpnicfQoSRemarkIPv6AddrDot1p.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSRemarkIPv6AddrDot1p.setStatus(_A)
class _HpnicfQoSRemarkIPv6AddrDscp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HpnicfQoSRemarkIPv6AddrDscp_Type.__name__=_J
_HpnicfQoSRemarkIPv6AddrDscp_Object=MibTableColumn
hpnicfQoSRemarkIPv6AddrDscp=_HpnicfQoSRemarkIPv6AddrDscp_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,4,1,4),_HpnicfQoSRemarkIPv6AddrDscp_Type())
hpnicfQoSRemarkIPv6AddrDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSRemarkIPv6AddrDscp.setStatus(_A)
_HpnicfQoSRemarkIPv6AddrRowStatus_Type=RowStatus
_HpnicfQoSRemarkIPv6AddrRowStatus_Object=MibTableColumn
hpnicfQoSRemarkIPv6AddrRowStatus=_HpnicfQoSRemarkIPv6AddrRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,4,1,5),_HpnicfQoSRemarkIPv6AddrRowStatus_Type())
hpnicfQoSRemarkIPv6AddrRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSRemarkIPv6AddrRowStatus.setStatus(_A)
_HpnicfQoSRemarkProtocolPriTable_Object=MibTable
hpnicfQoSRemarkProtocolPriTable=_HpnicfQoSRemarkProtocolPriTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,5))
if mibBuilder.loadTexts:hpnicfQoSRemarkProtocolPriTable.setStatus(_A)
_HpnicfQoSRemarkProtocolPriEntry_Object=MibTableRow
hpnicfQoSRemarkProtocolPriEntry=_HpnicfQoSRemarkProtocolPriEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,5,1))
hpnicfQoSRemarkProtocolPriEntry.setIndexNames((0,_E,_AE))
if mibBuilder.loadTexts:hpnicfQoSRemarkProtocolPriEntry.setStatus(_A)
class _HpnicfQoSRemarkProtocolValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ip',1),('ipx',2),('arp',3),('appletalk',4),('sna',5),('netbeui',6)))
_HpnicfQoSRemarkProtocolValue_Type.__name__=_D
_HpnicfQoSRemarkProtocolValue_Object=MibTableColumn
hpnicfQoSRemarkProtocolValue=_HpnicfQoSRemarkProtocolValue_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,5,1,1),_HpnicfQoSRemarkProtocolValue_Type())
hpnicfQoSRemarkProtocolValue.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfQoSRemarkProtocolValue.setStatus(_A)
class _HpnicfQoSRemarkProtocolDot1p_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpnicfQoSRemarkProtocolDot1p_Type.__name__=_J
_HpnicfQoSRemarkProtocolDot1p_Object=MibTableColumn
hpnicfQoSRemarkProtocolDot1p=_HpnicfQoSRemarkProtocolDot1p_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,5,1,2),_HpnicfQoSRemarkProtocolDot1p_Type())
hpnicfQoSRemarkProtocolDot1p.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSRemarkProtocolDot1p.setStatus(_A)
_HpnicfQoSRemarkProtocolRowStatus_Type=RowStatus
_HpnicfQoSRemarkProtocolRowStatus_Object=MibTableColumn
hpnicfQoSRemarkProtocolRowStatus=_HpnicfQoSRemarkProtocolRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,5,1,3),_HpnicfQoSRemarkProtocolRowStatus_Type())
hpnicfQoSRemarkProtocolRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSRemarkProtocolRowStatus.setStatus(_A)
_HpnicfQoSRemarkVlanPriTable_Object=MibTable
hpnicfQoSRemarkVlanPriTable=_HpnicfQoSRemarkVlanPriTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,6))
if mibBuilder.loadTexts:hpnicfQoSRemarkVlanPriTable.setStatus(_A)
_HpnicfQoSRemarkVlanPriEntry_Object=MibTableRow
hpnicfQoSRemarkVlanPriEntry=_HpnicfQoSRemarkVlanPriEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,6,1))
hpnicfQoSRemarkVlanPriEntry.setIndexNames((0,_E,_AF))
if mibBuilder.loadTexts:hpnicfQoSRemarkVlanPriEntry.setStatus(_A)
class _HpnicfQoSRemarkVlanStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpnicfQoSRemarkVlanStart_Type.__name__=_D
_HpnicfQoSRemarkVlanStart_Object=MibTableColumn
hpnicfQoSRemarkVlanStart=_HpnicfQoSRemarkVlanStart_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,6,1,1),_HpnicfQoSRemarkVlanStart_Type())
hpnicfQoSRemarkVlanStart.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfQoSRemarkVlanStart.setStatus(_A)
class _HpnicfQoSRemarkVlanEnd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpnicfQoSRemarkVlanEnd_Type.__name__=_D
_HpnicfQoSRemarkVlanEnd_Object=MibTableColumn
hpnicfQoSRemarkVlanEnd=_HpnicfQoSRemarkVlanEnd_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,6,1,2),_HpnicfQoSRemarkVlanEnd_Type())
hpnicfQoSRemarkVlanEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSRemarkVlanEnd.setStatus(_A)
class _HpnicfQoSRemarkVlanDot1p_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpnicfQoSRemarkVlanDot1p_Type.__name__=_J
_HpnicfQoSRemarkVlanDot1p_Object=MibTableColumn
hpnicfQoSRemarkVlanDot1p=_HpnicfQoSRemarkVlanDot1p_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,6,1,3),_HpnicfQoSRemarkVlanDot1p_Type())
hpnicfQoSRemarkVlanDot1p.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSRemarkVlanDot1p.setStatus(_A)
class _HpnicfQoSRemarkVlanDscp_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HpnicfQoSRemarkVlanDscp_Type.__name__=_J
_HpnicfQoSRemarkVlanDscp_Object=MibTableColumn
hpnicfQoSRemarkVlanDscp=_HpnicfQoSRemarkVlanDscp_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,6,1,4),_HpnicfQoSRemarkVlanDscp_Type())
hpnicfQoSRemarkVlanDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSRemarkVlanDscp.setStatus(_A)
_HpnicfQoSRemarkVlanRowStatus_Type=RowStatus
_HpnicfQoSRemarkVlanRowStatus_Object=MibTableColumn
hpnicfQoSRemarkVlanRowStatus=_HpnicfQoSRemarkVlanRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,6,1,5),_HpnicfQoSRemarkVlanRowStatus_Type())
hpnicfQoSRemarkVlanRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfQoSRemarkVlanRowStatus.setStatus(_A)
_HpnicfQoSTypeOfServiceObjects_ObjectIdentity=ObjectIdentity
hpnicfQoSTypeOfServiceObjects=_HpnicfQoSTypeOfServiceObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,7))
class _HpnicfQoSTypeOfServiceMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('disabled',1),(_A0,2),(_N,3)))
_HpnicfQoSTypeOfServiceMode_Type.__name__=_D
_HpnicfQoSTypeOfServiceMode_Object=MibScalar
hpnicfQoSTypeOfServiceMode=_HpnicfQoSTypeOfServiceMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,65,1,12,7,1),_HpnicfQoSTypeOfServiceMode_Type())
hpnicfQoSTypeOfServiceMode.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfQoSTypeOfServiceMode.setStatus(_A)
mibBuilder.exportSymbols(_E,**{_O:CarAction,'PriorityQueue':PriorityQueue,'Direction':Direction,'hpnicfQos2':hpnicfQos2,'hpnicfIfQos2':hpnicfIfQos2,'hpnicfIfQoSHardwareQueueObjects':hpnicfIfQoSHardwareQueueObjects,'hpnicfIfQoSHardwareQueueConfigGroup':hpnicfIfQoSHardwareQueueConfigGroup,'hpnicfIfQoSQSModeTable':hpnicfIfQoSQSModeTable,'hpnicfIfQoSQSModeEntry':hpnicfIfQoSQSModeEntry,'hpnicfIfQoSQSMode':hpnicfIfQoSQSMode,'hpnicfIfQoSQSWeightTable':hpnicfIfQoSQSWeightTable,'hpnicfIfQoSQSWeightEntry':hpnicfIfQoSQSWeightEntry,_P:hpnicfIfQoSQueueID,'hpnicfIfQoSQueueGroupType':hpnicfIfQoSQueueGroupType,'hpnicfIfQoSQSType':hpnicfIfQoSQSType,'hpnicfIfQoSQSValue':hpnicfIfQoSQSValue,'hpnicfIfQoSQSMaxDelay':hpnicfIfQoSQSMaxDelay,'hpnicfIfQoSQSMinBandwidth':hpnicfIfQoSQSMinBandwidth,'hpnicfIfQoSQSMinBandwidthPercent':hpnicfIfQoSQSMinBandwidthPercent,'hpnicfIfQoSHardwareQueueRunInfoGroup':hpnicfIfQoSHardwareQueueRunInfoGroup,'hpnicfIfQoSHardwareQueueRunInfoTable':hpnicfIfQoSHardwareQueueRunInfoTable,'hpnicfIfQoSHardwareQueueRunInfoEntry':hpnicfIfQoSHardwareQueueRunInfoEntry,'hpnicfIfQoSPassPackets':hpnicfIfQoSPassPackets,'hpnicfIfQoSDropPackets':hpnicfIfQoSDropPackets,'hpnicfIfQoSPassBytes':hpnicfIfQoSPassBytes,'hpnicfIfQoSPassPPS':hpnicfIfQoSPassPPS,'hpnicfIfQoSPassBPS':hpnicfIfQoSPassBPS,'hpnicfIfQoSDropBytes':hpnicfIfQoSDropBytes,'hpnicfIfQoSQueueLengthInPkts':hpnicfIfQoSQueueLengthInPkts,'hpnicfIfQoSQueueLengthInBytes':hpnicfIfQoSQueueLengthInBytes,'hpnicfIfQoSCurQueuePkts':hpnicfIfQoSCurQueuePkts,'hpnicfIfQoSCurQueueBytes':hpnicfIfQoSCurQueueBytes,'hpnicfIfQoSCurQueuePPS':hpnicfIfQoSCurQueuePPS,'hpnicfIfQoSCurQueueBPS':hpnicfIfQoSCurQueueBPS,'hpnicfIfQoSTailDropPkts':hpnicfIfQoSTailDropPkts,'hpnicfIfQoSTailDropBytes':hpnicfIfQoSTailDropBytes,'hpnicfIfQoSTailDropPPS':hpnicfIfQoSTailDropPPS,'hpnicfIfQoSTailDropBPS':hpnicfIfQoSTailDropBPS,'hpnicfIfQoSWredDropPkts':hpnicfIfQoSWredDropPkts,'hpnicfIfQoSWredDropBytes':hpnicfIfQoSWredDropBytes,'hpnicfIfQoSWredDropPPS':hpnicfIfQoSWredDropPPS,'hpnicfIfQoSWredDropBPS':hpnicfIfQoSWredDropBPS,'hpnicfIfQoSHQueueTcpRunInfoTable':hpnicfIfQoSHQueueTcpRunInfoTable,'hpnicfIfQoSHQueueTcpRunInfoEntry':hpnicfIfQoSHQueueTcpRunInfoEntry,'hpnicfIfQoSWredDropLPreNTcpPkts':hpnicfIfQoSWredDropLPreNTcpPkts,'hpnicfIfQoSWredDropLPreNTcpBytes':hpnicfIfQoSWredDropLPreNTcpBytes,'hpnicfIfQoSWredDropLPreNTcpPPS':hpnicfIfQoSWredDropLPreNTcpPPS,'hpnicfIfQoSWredDropLPreNTcpBPS':hpnicfIfQoSWredDropLPreNTcpBPS,'hpnicfIfQoSWredDropLPreTcpPkts':hpnicfIfQoSWredDropLPreTcpPkts,'hpnicfIfQoSWredDropLPreTcpBytes':hpnicfIfQoSWredDropLPreTcpBytes,'hpnicfIfQoSWredDropLPreTcpPPS':hpnicfIfQoSWredDropLPreTcpPPS,'hpnicfIfQoSWredDropLPreTcpBPS':hpnicfIfQoSWredDropLPreTcpBPS,'hpnicfIfQoSWredDropHPreNTcpPkts':hpnicfIfQoSWredDropHPreNTcpPkts,'hpnicfIfQoSWredDropHPreNTcpBytes':hpnicfIfQoSWredDropHPreNTcpBytes,'hpnicfIfQoSWredDropHPreNTcpPPS':hpnicfIfQoSWredDropHPreNTcpPPS,'hpnicfIfQoSWredDropHPreNTcpBPS':hpnicfIfQoSWredDropHPreNTcpBPS,'hpnicfIfQoSWredDropHPreTcpPkts':hpnicfIfQoSWredDropHPreTcpPkts,'hpnicfIfQoSWredDropHPreTcpBytes':hpnicfIfQoSWredDropHPreTcpBytes,'hpnicfIfQoSWredDropHPreTcpPPS':hpnicfIfQoSWredDropHPreTcpPPS,'hpnicfIfQoSWredDropHPreTcpBPS':hpnicfIfQoSWredDropHPreTcpBPS,'hpnicfIfQoSSoftwareQueueObjects':hpnicfIfQoSSoftwareQueueObjects,'hpnicfIfQoSFIFOObject':hpnicfIfQoSFIFOObject,'hpnicfIfQoSFIFOConfigTable':hpnicfIfQoSFIFOConfigTable,'hpnicfIfQoSFIFOConfigEntry':hpnicfIfQoSFIFOConfigEntry,'hpnicfIfQoSFIFOMaxQueueLen':hpnicfIfQoSFIFOMaxQueueLen,'hpnicfIfQoSFIFORunInfoTable':hpnicfIfQoSFIFORunInfoTable,'hpnicfIfQoSFIFORunInfoEntry':hpnicfIfQoSFIFORunInfoEntry,'hpnicfIfQoSFIFOSize':hpnicfIfQoSFIFOSize,'hpnicfIfQoSFIFODiscardPackets':hpnicfIfQoSFIFODiscardPackets,'hpnicfIfQoSPQObject':hpnicfIfQoSPQObject,'hpnicfIfQoSPQConfigGroup':hpnicfIfQoSPQConfigGroup,'hpnicfIfQoSPQDefaultTable':hpnicfIfQoSPQDefaultTable,'hpnicfIfQoSPQDefaultEntry':hpnicfIfQoSPQDefaultEntry,_Q:hpnicfIfQoSPQListNumber,'hpnicfIfQoSPQDefaultQueueType':hpnicfIfQoSPQDefaultQueueType,'hpnicfIfQoSPQQueueLengthTable':hpnicfIfQoSPQQueueLengthTable,'hpnicfIfQoSPQQueueLengthEntry':hpnicfIfQoSPQQueueLengthEntry,_l:hpnicfIfQoSPQQueueLengthType,'hpnicfIfQoSPQQueueLengthValue':hpnicfIfQoSPQQueueLengthValue,'hpnicfIfQoSPQClassRuleTable':hpnicfIfQoSPQClassRuleTable,'hpnicfIfQoSPQClassRuleEntry':hpnicfIfQoSPQClassRuleEntry,_m:hpnicfIfQoSPQClassRuleType,_n:hpnicfIfQoSPQClassRuleValue,'hpnicfIfQoSPQClassRuleQueueType':hpnicfIfQoSPQClassRuleQueueType,'hpnicfIfQoSPQClassRowStatus':hpnicfIfQoSPQClassRowStatus,'hpnicfIfQoSPQApplyTable':hpnicfIfQoSPQApplyTable,'hpnicfIfQoSPQApplyEntry':hpnicfIfQoSPQApplyEntry,'hpnicfIfQoSPQApplyListNumber':hpnicfIfQoSPQApplyListNumber,'hpnicfIfQoSPQApplyRowStatus':hpnicfIfQoSPQApplyRowStatus,'hpnicfIfQoSPQRunInfoGroup':hpnicfIfQoSPQRunInfoGroup,'hpnicfIfQoSPQRunInfoTable':hpnicfIfQoSPQRunInfoTable,'hpnicfIfQoSPQRunInfoEntry':hpnicfIfQoSPQRunInfoEntry,_s:hpnicfIfQoSPQType,'hpnicfIfQoSPQSize':hpnicfIfQoSPQSize,'hpnicfIfQoSPQLength':hpnicfIfQoSPQLength,'hpnicfIfQoSPQDiscardPackets':hpnicfIfQoSPQDiscardPackets,'hpnicfIfQoSCQObject':hpnicfIfQoSCQObject,'hpnicfIfQoSCQConfigGroup':hpnicfIfQoSCQConfigGroup,'hpnicfIfQoSCQDefaultTable':hpnicfIfQoSCQDefaultTable,'hpnicfIfQoSCQDefaultEntry':hpnicfIfQoSCQDefaultEntry,_R:hpnicfIfQoSCQListNumber,'hpnicfIfQoSCQDefaultQueueID':hpnicfIfQoSCQDefaultQueueID,'hpnicfIfQoSCQQueueLengthTable':hpnicfIfQoSCQQueueLengthTable,'hpnicfIfQoSCQQueueLengthEntry':hpnicfIfQoSCQQueueLengthEntry,_T:hpnicfIfQoSCQQueueID,'hpnicfIfQoSCQQueueLength':hpnicfIfQoSCQQueueLength,'hpnicfIfQoSCQQueueServing':hpnicfIfQoSCQQueueServing,'hpnicfIfQoSCQClassRuleTable':hpnicfIfQoSCQClassRuleTable,'hpnicfIfQoSCQClassRuleEntry':hpnicfIfQoSCQClassRuleEntry,_t:hpnicfIfQoSCQClassRuleType,_u:hpnicfIfQoSCQClassRuleValue,'hpnicfIfQoSCQClassRuleQueueID':hpnicfIfQoSCQClassRuleQueueID,'hpnicfIfQoSCQClassRowStatus':hpnicfIfQoSCQClassRowStatus,'hpnicfIfQoSCQApplyTable':hpnicfIfQoSCQApplyTable,'hpnicfIfQoSCQApplyEntry':hpnicfIfQoSCQApplyEntry,'hpnicfIfQoSCQApplyListNumber':hpnicfIfQoSCQApplyListNumber,'hpnicfIfQoSCQApplyRowStatus':hpnicfIfQoSCQApplyRowStatus,'hpnicfIfQoSCQRunInfoGroup':hpnicfIfQoSCQRunInfoGroup,'hpnicfIfQoSCQRunInfoTable':hpnicfIfQoSCQRunInfoTable,'hpnicfIfQoSCQRunInfoEntry':hpnicfIfQoSCQRunInfoEntry,'hpnicfIfQoSCQRunInfoSize':hpnicfIfQoSCQRunInfoSize,'hpnicfIfQoSCQRunInfoLength':hpnicfIfQoSCQRunInfoLength,'hpnicfIfQoSCQRunInfoDiscardPackets':hpnicfIfQoSCQRunInfoDiscardPackets,'hpnicfIfQoSWFQObject':hpnicfIfQoSWFQObject,'hpnicfIfQoSWFQConfigGroup':hpnicfIfQoSWFQConfigGroup,'hpnicfIfQoSWFQTable':hpnicfIfQoSWFQTable,'hpnicfIfQoSWFQEntry':hpnicfIfQoSWFQEntry,'hpnicfIfQoSWFQQueueLength':hpnicfIfQoSWFQQueueLength,'hpnicfIfQoSWFQQueueNumber':hpnicfIfQoSWFQQueueNumber,'hpnicfIfQoSWFQRowStatus':hpnicfIfQoSWFQRowStatus,'hpnicfIfQoSWFQType':hpnicfIfQoSWFQType,'hpnicfIfQoSWFQRunInfoGroup':hpnicfIfQoSWFQRunInfoGroup,'hpnicfIfQoSWFQRunInfoTable':hpnicfIfQoSWFQRunInfoTable,'hpnicfIfQoSWFQRunInfoEntry':hpnicfIfQoSWFQRunInfoEntry,'hpnicfIfQoSWFQSize':hpnicfIfQoSWFQSize,'hpnicfIfQoSWFQLength':hpnicfIfQoSWFQLength,'hpnicfIfQoSWFQDiscardPackets':hpnicfIfQoSWFQDiscardPackets,'hpnicfIfQoSWFQHashedActiveQueues':hpnicfIfQoSWFQHashedActiveQueues,'hpnicfIfQoSWFQHashedMaxActiveQueues':hpnicfIfQoSWFQHashedMaxActiveQueues,'hpnicfIfQosWFQhashedTotalQueues':hpnicfIfQosWFQhashedTotalQueues,'hpnicfIfQoSBandwidthGroup':hpnicfIfQoSBandwidthGroup,'hpnicfIfQoSBandwidthTable':hpnicfIfQoSBandwidthTable,'hpnicfIfQoSBandwidthEntry':hpnicfIfQoSBandwidthEntry,'hpnicfIfQoSMaxBandwidth':hpnicfIfQoSMaxBandwidth,'hpnicfIfQoSReservedBandwidthPct':hpnicfIfQoSReservedBandwidthPct,'hpnicfIfQoSBandwidthRowStatus':hpnicfIfQoSBandwidthRowStatus,'hpnicfIfQoSQmtokenGroup':hpnicfIfQoSQmtokenGroup,'hpnicfIfQoSQmtokenTable':hpnicfIfQoSQmtokenTable,'hpnicfIfQoSQmtokenEntry':hpnicfIfQoSQmtokenEntry,'hpnicfIfQoSQmtokenNumber':hpnicfIfQoSQmtokenNumber,'hpnicfIfQoSQmtokenRosStatus':hpnicfIfQoSQmtokenRosStatus,'hpnicfIfQoSRTPQObject':hpnicfIfQoSRTPQObject,'hpnicfIfQoSRTPQConfigGroup':hpnicfIfQoSRTPQConfigGroup,'hpnicfIfQoSRTPQConfigTable':hpnicfIfQoSRTPQConfigTable,'hpnicfIfQoSRTPQConfigEntry':hpnicfIfQoSRTPQConfigEntry,'hpnicfIfQoSRTPQStartPort':hpnicfIfQoSRTPQStartPort,'hpnicfIfQoSRTPQEndPort':hpnicfIfQoSRTPQEndPort,'hpnicfIfQoSRTPQReservedBandwidth':hpnicfIfQoSRTPQReservedBandwidth,'hpnicfIfQoSRTPQCbs':hpnicfIfQoSRTPQCbs,'hpnicfIfQoSRTPQRowStatus':hpnicfIfQoSRTPQRowStatus,'hpnicfIfQoSRTPQRunInfoGroup':hpnicfIfQoSRTPQRunInfoGroup,'hpnicfIfQoSRTPQRunInfoTable':hpnicfIfQoSRTPQRunInfoTable,'hpnicfIfQoSRTPQRunInfoEntry':hpnicfIfQoSRTPQRunInfoEntry,'hpnicfIfQoSRTPQPacketNumber':hpnicfIfQoSRTPQPacketNumber,'hpnicfIfQoSRTPQPacketSize':hpnicfIfQoSRTPQPacketSize,'hpnicfIfQoSRTPQOutputPackets':hpnicfIfQoSRTPQOutputPackets,'hpnicfIfQoSRTPQDiscardPackets':hpnicfIfQoSRTPQDiscardPackets,'hpnicfIfQoSCarListObject':hpnicfIfQoSCarListObject,'hpnicfIfQoCarListGroup':hpnicfIfQoCarListGroup,'hpnicfIfQoSCarlTable':hpnicfIfQoSCarlTable,'hpnicfIfQoSCarlEntry':hpnicfIfQoSCarlEntry,_v:hpnicfIfQoSCarlListNum,'hpnicfIfQoSCarlParaType':hpnicfIfQoSCarlParaType,'hpnicfIfQoSCarlParaValue':hpnicfIfQoSCarlParaValue,'hpnicfIfQoSCarlRowStatus':hpnicfIfQoSCarlRowStatus,'hpnicfIfQoSLineRateObjects':hpnicfIfQoSLineRateObjects,'hpnicfIfQoSLRConfigTable':hpnicfIfQoSLRConfigTable,'hpnicfIfQoSLRConfigEntry':hpnicfIfQoSLRConfigEntry,_U:hpnicfIfQoSLRDirection,'hpnicfIfQoSLRCir':hpnicfIfQoSLRCir,'hpnicfIfQoSLRCbs':hpnicfIfQoSLRCbs,'hpnicfIfQoSLREbs':hpnicfIfQoSLREbs,'hpnicfIfQoSRowStatus':hpnicfIfQoSRowStatus,'hpnicfIfQoSLRPir':hpnicfIfQoSLRPir,'hpnicfIfQoSLRUnit':hpnicfIfQoSLRUnit,'hpnicfIfQoSLRRunInfoTable':hpnicfIfQoSLRRunInfoTable,'hpnicfIfQoSLRRunInfoEntry':hpnicfIfQoSLRRunInfoEntry,'hpnicfIfQoSLRRunInfoPassedPackets':hpnicfIfQoSLRRunInfoPassedPackets,'hpnicfIfQoSLRRunInfoPassedBytes':hpnicfIfQoSLRRunInfoPassedBytes,'hpnicfIfQoSLRRunInfoDelayedPackets':hpnicfIfQoSLRRunInfoDelayedPackets,'hpnicfIfQoSLRRunInfoDelayedBytes':hpnicfIfQoSLRRunInfoDelayedBytes,'hpnicfIfQoSLRRunInfoActiveShaping':hpnicfIfQoSLRRunInfoActiveShaping,'hpnicfIfQoSCARObjects':hpnicfIfQoSCARObjects,'hpnicfIfQoSAggregativeCarGroup':hpnicfIfQoSAggregativeCarGroup,'hpnicfIfQoSAggregativeCarNextIndex':hpnicfIfQoSAggregativeCarNextIndex,'hpnicfIfQoSAggregativeCarConfigTable':hpnicfIfQoSAggregativeCarConfigTable,'hpnicfIfQoSAggregativeCarConfigEntry':hpnicfIfQoSAggregativeCarConfigEntry,_V:hpnicfIfQoSAggregativeCarIndex,'hpnicfIfQoSAggregativeCarName':hpnicfIfQoSAggregativeCarName,'hpnicfIfQoSAggregativeCarCir':hpnicfIfQoSAggregativeCarCir,'hpnicfIfQoSAggregativeCarCbs':hpnicfIfQoSAggregativeCarCbs,'hpnicfIfQoSAggregativeCarEbs':hpnicfIfQoSAggregativeCarEbs,'hpnicfIfQoSAggregativeCarPir':hpnicfIfQoSAggregativeCarPir,'hpnicfIfQoSAggregativeCarGreenActionType':hpnicfIfQoSAggregativeCarGreenActionType,'hpnicfIfQoSAggregativeCarGreenActionValue':hpnicfIfQoSAggregativeCarGreenActionValue,'hpnicfIfQoSAggregativeCarYellowActionType':hpnicfIfQoSAggregativeCarYellowActionType,'hpnicfIfQoSAggregativeCarYellowActionValue':hpnicfIfQoSAggregativeCarYellowActionValue,'hpnicfIfQoSAggregativeCarRedActionType':hpnicfIfQoSAggregativeCarRedActionType,'hpnicfIfQoSAggregativeCarRedActionValue':hpnicfIfQoSAggregativeCarRedActionValue,'hpnicfIfQoSAggregativeCarType':hpnicfIfQoSAggregativeCarType,'hpnicfIfQoSAggregativeCarRowStatus':hpnicfIfQoSAggregativeCarRowStatus,'hpnicfIfQoSAggregativeCarApplyTable':hpnicfIfQoSAggregativeCarApplyTable,'hpnicfIfQoSAggregativeCarApplyEntry':hpnicfIfQoSAggregativeCarApplyEntry,_w:hpnicfIfQoSAggregativeCarApplyDirection,_x:hpnicfIfQoSAggregativeCarApplyRuleType,_y:hpnicfIfQoSAggregativeCarApplyRuleValue,'hpnicfIfQoSAggregativeCarApplyCarIndex':hpnicfIfQoSAggregativeCarApplyCarIndex,'hpnicfIfQoSAggregativeCarApplyRowStatus':hpnicfIfQoSAggregativeCarApplyRowStatus,'hpnicfIfQoSAggregativeCarRunInfoTable':hpnicfIfQoSAggregativeCarRunInfoTable,'hpnicfIfQoSAggregativeCarRunInfoEntry':hpnicfIfQoSAggregativeCarRunInfoEntry,'hpnicfIfQoSAggregativeCarGreenPackets':hpnicfIfQoSAggregativeCarGreenPackets,'hpnicfIfQoSAggregativeCarGreenBytes':hpnicfIfQoSAggregativeCarGreenBytes,'hpnicfIfQoSAggregativeCarYellowPackets':hpnicfIfQoSAggregativeCarYellowPackets,'hpnicfIfQoSAggregativeCarYellowBytes':hpnicfIfQoSAggregativeCarYellowBytes,'hpnicfIfQoSAggregativeCarRedPackets':hpnicfIfQoSAggregativeCarRedPackets,'hpnicfIfQoSAggregativeCarRedBytes':hpnicfIfQoSAggregativeCarRedBytes,'hpnicfIfQoSTricolorCarGroup':hpnicfIfQoSTricolorCarGroup,'hpnicfIfQoSTricolorCarConfigTable':hpnicfIfQoSTricolorCarConfigTable,'hpnicfIfQoSTricolorCarConfigEntry':hpnicfIfQoSTricolorCarConfigEntry,_X:hpnicfIfQoSTricolorCarDirection,_Y:hpnicfIfQoSTricolorCarType,_Z:hpnicfIfQoSTricolorCarValue,'hpnicfIfQoSTricolorCarCir':hpnicfIfQoSTricolorCarCir,'hpnicfIfQoSTricolorCarCbs':hpnicfIfQoSTricolorCarCbs,'hpnicfIfQoSTricolorCarEbs':hpnicfIfQoSTricolorCarEbs,'hpnicfIfQoSTricolorCarPir':hpnicfIfQoSTricolorCarPir,'hpnicfIfQoSTricolorCarGreenActionType':hpnicfIfQoSTricolorCarGreenActionType,'hpnicfIfQoSTricolorCarGreenActionValue':hpnicfIfQoSTricolorCarGreenActionValue,'hpnicfIfQoSTricolorCarYellowActionType':hpnicfIfQoSTricolorCarYellowActionType,'hpnicfIfQoSTricolorCarYellowActionValue':hpnicfIfQoSTricolorCarYellowActionValue,'hpnicfIfQoSTricolorCarRedActionType':hpnicfIfQoSTricolorCarRedActionType,'hpnicfIfQoSTricolorCarRedActionValue':hpnicfIfQoSTricolorCarRedActionValue,'hpnicfIfQoSTricolorCarRowStatus':hpnicfIfQoSTricolorCarRowStatus,'hpnicfIfQoSTricolorCarRunInfoTable':hpnicfIfQoSTricolorCarRunInfoTable,'hpnicfIfQoSTricolorCarRunInfoEntry':hpnicfIfQoSTricolorCarRunInfoEntry,'hpnicfIfQoSTricolorCarGreenPackets':hpnicfIfQoSTricolorCarGreenPackets,'hpnicfIfQoSTricolorCarGreenBytes':hpnicfIfQoSTricolorCarGreenBytes,'hpnicfIfQoSTricolorCarYellowPackets':hpnicfIfQoSTricolorCarYellowPackets,'hpnicfIfQoSTricolorCarYellowBytes':hpnicfIfQoSTricolorCarYellowBytes,'hpnicfIfQoSTricolorCarRedPackets':hpnicfIfQoSTricolorCarRedPackets,'hpnicfIfQoSTricolorCarRedBytes':hpnicfIfQoSTricolorCarRedBytes,'hpnicfIfQoSGTSObjects':hpnicfIfQoSGTSObjects,'hpnicfIfQoSGTSConfigTable':hpnicfIfQoSGTSConfigTable,'hpnicfIfQoSGTSConfigEntry':hpnicfIfQoSGTSConfigEntry,_a:hpnicfIfQoSGTSClassRuleType,_b:hpnicfIfQoSGTSClassRuleValue,'hpnicfIfQoSGTSCir':hpnicfIfQoSGTSCir,'hpnicfIfQoSGTSCbs':hpnicfIfQoSGTSCbs,'hpnicfIfQoSGTSEbs':hpnicfIfQoSGTSEbs,'hpnicfIfQoSGTSQueueLength':hpnicfIfQoSGTSQueueLength,'hpnicfIfQoSGTSConfigRowStatus':hpnicfIfQoSGTSConfigRowStatus,'hpnicfIfQoSGTSRunInfoTable':hpnicfIfQoSGTSRunInfoTable,'hpnicfIfQoSGTSRunInfoEntry':hpnicfIfQoSGTSRunInfoEntry,'hpnicfIfQoSGTSQueueSize':hpnicfIfQoSGTSQueueSize,'hpnicfIfQoSGTSPassedPackets':hpnicfIfQoSGTSPassedPackets,'hpnicfIfQoSGTSPassedBytes':hpnicfIfQoSGTSPassedBytes,'hpnicfIfQoSGTSDiscardPackets':hpnicfIfQoSGTSDiscardPackets,'hpnicfIfQoSGTSDiscardBytes':hpnicfIfQoSGTSDiscardBytes,'hpnicfIfQoSGTSDelayedPackets':hpnicfIfQoSGTSDelayedPackets,'hpnicfIfQoSGTSDelayedBytes':hpnicfIfQoSGTSDelayedBytes,'hpnicfIfQoSWREDObjects':hpnicfIfQoSWREDObjects,'hpnicfIfQoSWredGroupGroup':hpnicfIfQoSWredGroupGroup,'hpnicfIfQoSWredGroupNextIndex':hpnicfIfQoSWredGroupNextIndex,'hpnicfIfQoSWredGroupTable':hpnicfIfQoSWredGroupTable,'hpnicfIfQoSWredGroupEntry':hpnicfIfQoSWredGroupEntry,_S:hpnicfIfQoSWredGroupIndex,'hpnicfIfQoSWredGroupName':hpnicfIfQoSWredGroupName,'hpnicfIfQoSWredGroupType':hpnicfIfQoSWredGroupType,'hpnicfIfQoSWredGroupWeightingConstant':hpnicfIfQoSWredGroupWeightingConstant,'hpnicfIfQoSWredGroupRowStatus':hpnicfIfQoSWredGroupRowStatus,'hpnicfIfQoSWredGroupContentTable':hpnicfIfQoSWredGroupContentTable,'hpnicfIfQoSWredGroupContentEntry':hpnicfIfQoSWredGroupContentEntry,_e:hpnicfIfQoSWredGroupContentIndex,_f:hpnicfIfQoSWredGroupContentSubIndex,'hpnicfIfQoSWredLowLimit':hpnicfIfQoSWredLowLimit,'hpnicfIfQoSWredHighLimit':hpnicfIfQoSWredHighLimit,'hpnicfIfQoSWredDiscardProb':hpnicfIfQoSWredDiscardProb,'hpnicfIfQoSWredGroupExponent':hpnicfIfQoSWredGroupExponent,'hpnicfIfQoSWredRowStatus':hpnicfIfQoSWredRowStatus,'hpnicfIfQoSWredGroupApplyIfTable':hpnicfIfQoSWredGroupApplyIfTable,'hpnicfIfQoSWredGroupApplyIfEntry':hpnicfIfQoSWredGroupApplyIfEntry,'hpnicfIfQoSWredGroupApplyIndex':hpnicfIfQoSWredGroupApplyIndex,'hpnicfIfQoSWredGroupApplyName':hpnicfIfQoSWredGroupApplyName,'hpnicfIfQoSWredGroupIfRowStatus':hpnicfIfQoSWredGroupIfRowStatus,'hpnicfIfQoSWredApplyIfRunInfoTable':hpnicfIfQoSWredApplyIfRunInfoTable,'hpnicfIfQoSWredApplyIfRunInfoEntry':hpnicfIfQoSWredApplyIfRunInfoEntry,'hpnicfIfQoSWredPreRandomDropNum':hpnicfIfQoSWredPreRandomDropNum,'hpnicfIfQoSWredPreTailDropNum':hpnicfIfQoSWredPreTailDropNum,'hpnicfIfQoSPortWredGroup':hpnicfIfQoSPortWredGroup,'hpnicfIfQoSPortWredWeightConstantTable':hpnicfIfQoSPortWredWeightConstantTable,'hpnicfIfQoSPortWredWeightConstantEntry':hpnicfIfQoSPortWredWeightConstantEntry,'hpnicfIfQoSPortWredEnable':hpnicfIfQoSPortWredEnable,'hpnicfIfQoSPortWredWeightConstant':hpnicfIfQoSPortWredWeightConstant,'hpnicfIfQoSPortWredWeightConstantRowStatus':hpnicfIfQoSPortWredWeightConstantRowStatus,'hpnicfIfQoSPortWredPreConfigTable':hpnicfIfQoSPortWredPreConfigTable,'hpnicfIfQoSPortWredPreConfigEntry':hpnicfIfQoSPortWredPreConfigEntry,_g:hpnicfIfQoSPortWredPreID,'hpnicfIfQoSPortWredPreLowLimit':hpnicfIfQoSPortWredPreLowLimit,'hpnicfIfQoSPortWredPreHighLimit':hpnicfIfQoSPortWredPreHighLimit,'hpnicfIfQoSPortWredPreDiscardProbability':hpnicfIfQoSPortWredPreDiscardProbability,'hpnicfIfQoSPortWredPreRowStatus':hpnicfIfQoSPortWredPreRowStatus,'hpnicfIfQoSPortWredRunInfoTable':hpnicfIfQoSPortWredRunInfoTable,'hpnicfIfQoSPortWredRunInfoEntry':hpnicfIfQoSPortWredRunInfoEntry,'hpnicfIfQoSWREDTailDropNum':hpnicfIfQoSWREDTailDropNum,'hpnicfIfQoSWREDRandomDropNum':hpnicfIfQoSWREDRandomDropNum,'hpnicfIfQoSPortPriorityObjects':hpnicfIfQoSPortPriorityObjects,'hpnicfIfQoSPortPriorityConfigGroup':hpnicfIfQoSPortPriorityConfigGroup,'hpnicfIfQoSPortPriorityTable':hpnicfIfQoSPortPriorityTable,'hpnicfIfQoSPortPriorityEntry':hpnicfIfQoSPortPriorityEntry,'hpnicfIfQoSPortPriorityValue':hpnicfIfQoSPortPriorityValue,'hpnicfIfQoSPortPirorityTrustTable':hpnicfIfQoSPortPirorityTrustTable,'hpnicfIfQoSPortPirorityTrustEntry':hpnicfIfQoSPortPirorityTrustEntry,'hpnicfIfQoSPortPriorityTrustTrustType':hpnicfIfQoSPortPriorityTrustTrustType,'hpnicfIfQoSPortPriorityTrustOvercastType':hpnicfIfQoSPortPriorityTrustOvercastType,'hpnicfIfQoSMapObjects':hpnicfIfQoSMapObjects,'hpnicfIfQoSPriMapConfigGroup':hpnicfIfQoSPriMapConfigGroup,'hpnicfIfQoSPriMapGroupNextIndex':hpnicfIfQoSPriMapGroupNextIndex,'hpnicfIfQoSPriMapGroupTable':hpnicfIfQoSPriMapGroupTable,'hpnicfIfQoSPriMapGroupEntry':hpnicfIfQoSPriMapGroupEntry,_h:hpnicfIfQoSPriMapGroupIndex,'hpnicfIfQoSPriMapGroupType':hpnicfIfQoSPriMapGroupType,'hpnicfIfQoSPriMapGroupName':hpnicfIfQoSPriMapGroupName,'hpnicfIfQoSPriMapGroupRowStatus':hpnicfIfQoSPriMapGroupRowStatus,'hpnicfIfQoSPriMapContentTable':hpnicfIfQoSPriMapContentTable,'hpnicfIfQoSPriMapContentEntry':hpnicfIfQoSPriMapContentEntry,_A1:hpnicfIfQoSPriMapGroupImportValue,'hpnicfIfQoSPriMapGroupExportValue':hpnicfIfQoSPriMapGroupExportValue,'hpnicfIfQoSPriMapContentRowStatus':hpnicfIfQoSPriMapContentRowStatus,'hpnicfIfQoSPrePriMapTable':hpnicfIfQoSPrePriMapTable,'hpnicfIfQoSPrePriMapEntry':hpnicfIfQoSPrePriMapEntry,_A2:hpnicfIfQoSPrePriMapTableType,_A3:hpnicfIfQoSPrePriMapTableColor,_A4:hpnicfIfQoSPrePriMapTableDirection,_A5:hpnicfIfQoSPrePriMapTableImportValue,'hpnicfIfQoSPrePriMapTableExportValue':hpnicfIfQoSPrePriMapTableExportValue,'hpnicfIfQoSL3PlusObjects':hpnicfIfQoSL3PlusObjects,'hpnicfIfQoSPortBindingGroup':hpnicfIfQoSPortBindingGroup,'hpnicfIfQoSPortBindingTable':hpnicfIfQoSPortBindingTable,'hpnicfIfQoSPortBindingEntry':hpnicfIfQoSPortBindingEntry,'hpnicfIfQoSBindingIf':hpnicfIfQoSBindingIf,'hpnicfIfQoSBindingRowStatus':hpnicfIfQoSBindingRowStatus,'hpnicfQoSTraStaObjects':hpnicfQoSTraStaObjects,'hpnicfQoSTraStaConfigGroup':hpnicfQoSTraStaConfigGroup,'hpnicfQoSIfTraStaConfigInfoTable':hpnicfQoSIfTraStaConfigInfoTable,'hpnicfQoSIfTraStaConfigInfoEntry':hpnicfQoSIfTraStaConfigInfoEntry,_A6:hpnicfQoSIfTraStaConfigDirection,'hpnicfQoSIfTraStaConfigQueue':hpnicfQoSIfTraStaConfigQueue,'hpnicfQoSIfTraStaConfigDot1p':hpnicfQoSIfTraStaConfigDot1p,'hpnicfQoSIfTraStaConfigDscp':hpnicfQoSIfTraStaConfigDscp,'hpnicfQoSIfTraStaConfigVlan':hpnicfQoSIfTraStaConfigVlan,'hpnicfQoSIfTraStaConfigStatus':hpnicfQoSIfTraStaConfigStatus,'hpnicfQoSTraStaRunGroup':hpnicfQoSTraStaRunGroup,'hpnicfQoSIfTraStaRunInfoTable':hpnicfQoSIfTraStaRunInfoTable,'hpnicfQoSIfTraStaRunInfoEntry':hpnicfQoSIfTraStaRunInfoEntry,_A7:hpnicfQoSIfTraStaRunObjectType,_A8:hpnicfQoSIfTraStaRunObjectValue,_A9:hpnicfQoSIfTraStaRunDirection,'hpnicfQoSIfTraStaRunPassPackets':hpnicfQoSIfTraStaRunPassPackets,'hpnicfQoSIfTraStaRunDropPackets':hpnicfQoSIfTraStaRunDropPackets,'hpnicfQoSIfTraStaRunPassBytes':hpnicfQoSIfTraStaRunPassBytes,'hpnicfQoSIfTraStaRunDropBytes':hpnicfQoSIfTraStaRunDropBytes,'hpnicfQoSIfTraStaRunPassPPS':hpnicfQoSIfTraStaRunPassPPS,'hpnicfQoSIfTraStaRunPassBPS':hpnicfQoSIfTraStaRunPassBPS,'hpnicfQoSGlobalPriorityObject':hpnicfQoSGlobalPriorityObject,'hpnicfQoSRemarkTcpPortPriTable':hpnicfQoSRemarkTcpPortPriTable,'hpnicfQoSRemarkTcpPortPriEntry':hpnicfQoSRemarkTcpPortPriEntry,_AA:hpnicfQoSRemarkTcpPortStart,'hpnicfQoSRemarkTcpPortEnd':hpnicfQoSRemarkTcpPortEnd,'hpnicfQoSRemarkTcpPortType':hpnicfQoSRemarkTcpPortType,'hpnicfQoSRemarkTcpPortDot1p':hpnicfQoSRemarkTcpPortDot1p,'hpnicfQoSRemarkTcpPortDscp':hpnicfQoSRemarkTcpPortDscp,'hpnicfQoSRemarkTcpPortRowStatus':hpnicfQoSRemarkTcpPortRowStatus,'hpnicfQoSRemarkUdpPortPriTable':hpnicfQoSRemarkUdpPortPriTable,'hpnicfQoSRemarkUdpPortPriEntry':hpnicfQoSRemarkUdpPortPriEntry,_AB:hpnicfQoSRemarkUdpPortStart,'hpnicfQoSRemarkUdpPortEnd':hpnicfQoSRemarkUdpPortEnd,'hpnicfQoSRemarkUdpPortType':hpnicfQoSRemarkUdpPortType,'hpnicfQoSRemarkUdpPortDot1p':hpnicfQoSRemarkUdpPortDot1p,'hpnicfQoSRemarkUdpPortDscp':hpnicfQoSRemarkUdpPortDscp,'hpnicfQoSRemarkUdpPortRowStatus':hpnicfQoSRemarkUdpPortRowStatus,'hpnicfQoSRemarkIPv4AddrPriTable':hpnicfQoSRemarkIPv4AddrPriTable,'hpnicfQoSRemarkIPv4AddrPriEntry':hpnicfQoSRemarkIPv4AddrPriEntry,_AC:hpnicfQoSRemarkIPv4AddrValue,'hpnicfQoSRemarkIPv4AddrMask':hpnicfQoSRemarkIPv4AddrMask,'hpnicfQoSRemarkIPv4AddrMaskLength':hpnicfQoSRemarkIPv4AddrMaskLength,'hpnicfQoSRemarkIPv4AddrDot1p':hpnicfQoSRemarkIPv4AddrDot1p,'hpnicfQoSRemarkIPv4AddrDscp':hpnicfQoSRemarkIPv4AddrDscp,'hpnicfQoSRemarkIPv4AddrRowStatus':hpnicfQoSRemarkIPv4AddrRowStatus,'hpnicfQoSRemarkIPv6AddrPriTable':hpnicfQoSRemarkIPv6AddrPriTable,'hpnicfQoSRemarkIPv6AddrPriEntry':hpnicfQoSRemarkIPv6AddrPriEntry,_AD:hpnicfQoSRemarkIPv6AddrValue,'hpnicfQoSRemarkIPv6AddrPrefixLength':hpnicfQoSRemarkIPv6AddrPrefixLength,'hpnicfQoSRemarkIPv6AddrDot1p':hpnicfQoSRemarkIPv6AddrDot1p,'hpnicfQoSRemarkIPv6AddrDscp':hpnicfQoSRemarkIPv6AddrDscp,'hpnicfQoSRemarkIPv6AddrRowStatus':hpnicfQoSRemarkIPv6AddrRowStatus,'hpnicfQoSRemarkProtocolPriTable':hpnicfQoSRemarkProtocolPriTable,'hpnicfQoSRemarkProtocolPriEntry':hpnicfQoSRemarkProtocolPriEntry,_AE:hpnicfQoSRemarkProtocolValue,'hpnicfQoSRemarkProtocolDot1p':hpnicfQoSRemarkProtocolDot1p,'hpnicfQoSRemarkProtocolRowStatus':hpnicfQoSRemarkProtocolRowStatus,'hpnicfQoSRemarkVlanPriTable':hpnicfQoSRemarkVlanPriTable,'hpnicfQoSRemarkVlanPriEntry':hpnicfQoSRemarkVlanPriEntry,_AF:hpnicfQoSRemarkVlanStart,'hpnicfQoSRemarkVlanEnd':hpnicfQoSRemarkVlanEnd,'hpnicfQoSRemarkVlanDot1p':hpnicfQoSRemarkVlanDot1p,'hpnicfQoSRemarkVlanDscp':hpnicfQoSRemarkVlanDscp,'hpnicfQoSRemarkVlanRowStatus':hpnicfQoSRemarkVlanRowStatus,'hpnicfQoSTypeOfServiceObjects':hpnicfQoSTypeOfServiceObjects,'hpnicfQoSTypeOfServiceMode':hpnicfQoSTypeOfServiceMode})