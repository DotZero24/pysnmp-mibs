_AI='rlQosTimeBasedAclPeriodicEnd'
_AH='rlQosTimeBasedAclPeriodicStart'
_AG='rlQosTimeBasedAclPeriodicWeekList'
_AF='rlQosTimeBasedAclPeriodicName'
_AE='rlQosTimeBasedAclRangeName'
_AD='rlQosPort'
_AC='rlQosClassifierUtilizationUnitId'
_AB='rlQosGlobalStatisticsCntrsType'
_AA='rlQosOutQueueStatisticsCountrID'
_A9='rlQosPortPolicyStatisticsCntrType'
_A8='rlQosDscp'
_A7='rlQosDscpQueueDefaultMapDscp'
_A6='rlQosAceTidxIndex'
_A5='rlQosAceTidxAclIndex'
_A4='rlQosPredefBlockAclIfType'
_A3='rlQosPredefBlockAclIfIndex'
_A2='rlQosCosQueueDefaultMapVpt'
_A1='rlQosNamesToIndexesName'
_A0='rlQosNamesToIndexesTableId'
_z='policy'
_y='rlQosFreeIndexesTableId'
_x='rlQosAclCounterAceIndex'
_w='rlQosAclCounterAclIndex'
_v='rlQosAclCounterInterface'
_u='rlQosQueueShapeIndex'
_t='rlQueueProfileName'
_s='rlQosEfQueueId'
_r='rlQosUdpPort'
_q='rlQosTcpPort'
_p='rlQosDscpIndex'
_o='rlQosCosIndex'
_n='rlQosRmOldDscp'
_m='rlQosOldDscp'
_l='rlQosQueueId'
_k='rlIfProfileName'
_j='rlQosPolicyClassRefClassPointer'
_i='rlQosPolicyMapIndex'
_h='ClassMapAction'
_g='ClassMapType'
_f='rlQosClassMapIndex'
_e='rlQosAclAceRefAcePointer'
_d='rlQosAclIndex'
_c='rlQosAceIndex'
_b='rlQosTupleIndex'
_a='rlQosOffsetIndex'
_Z='disable'
_Y='inner-vlan'
_X='out-port'
_W='in-port'
_V='2006-02-12 00:00'
_U='TruthValue'
_T='rlIfType'
_S='bytes'
_R='BinaryStatus'
_Q='none'
_P='vpt'
_O='vlan'
_N='OctetString'
_M='rlIfIndex'
_L='rlQosPolicerIndex'
_K='Unsigned32'
_J='percent'
_I='deprecated'
_H='DisplayString'
_G='read-write'
_F='not-accessible'
_E='read-only'
_D='Integer32'
_C='DLINK-3100-QOS-CLI-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Percents,rnd=mibBuilder.importSymbols('DLINK-3100-MIB','Percents','rnd')
StatisticsClearActionType,StatisticsDPType=mibBuilder.importSymbols('DLINK-3100-POLICY-MIB','StatisticsClearActionType','StatisticsDPType')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_K,'iso')
DisplayString,PhysAddress,RowPointer,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','RowPointer','RowStatus','TextualConvention',_U)
rlQosCliMib=ModuleIdentity((1,3,6,1,4,1,171,10,94,89,89,88))
if mibBuilder.loadTexts:rlQosCliMib.setRevisions((_V,_V,'2005-03-14 00:00','2005-02-07 00:00','2005-01-27 00:00','2004-11-15 00:00','2003-09-29 00:00','2003-09-21 00:00','2005-04-17 00:00'))
class ClassOffsetType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('packetStart',1),('layer2-start',2),('mpls-start',3),('layer3-start',4),('layer4-start',5),('layer5-start',6),(_O,7),(_W,8),(_X,9),(_P,10),('ethertype',11),(_Y,12),('layer3-ipv6-start',13)))
class ClassTupleType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)));namedValues=NamedValues(*(('protocol',1),('ip-src',2),('ip-dest',3),('dscp',4),('ip-precedence',5),('udp-port-src',6),('udp-port-dest',7),('tcp-port-src',8),('tcp-port-dest',9),('mac-src',10),('mac-dest',11),(_O,12),(_W,13),(_X,14),('general',15),(_P,16),('ether-type',17),('tcp-flags',18),('icmp-type',19),('icmp-code',20),('igmp-type',21),(_Y,22),('ipv6-src',23),('ipv6-dest',24)))
class AceActionType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('permit',1),('deny',2),('deny-DisablePort',3)))
class AceObjectType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13)));namedValues=NamedValues(*(('ip',1),('ip-TCP',2),('ip-UDP',3),('ip-Offset',4),('mac',5),('mac-Offset',6),('ip-ICMP',7),('ip-IGMP',8),('ipv6',9),('ipv6-TCP',10),('ipv6-UDP',11),('ipv6-Offset',12),('ipv6-ICMP',13)))
class AclObjectType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mac',1),('ip',2),('ipv6',3)))
class ClassMapType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('matchAll',1),('matchAny',2)))
class ClassMapAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_Q,1),('setIP-Precedence',2),('setDSCP',3),('setQueue',4),('setCos',5),('trustCos',6),('trustDSCP',7),('trustTCP-UDPport',8),('trustCosDscp',9)))
class PolicerType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('single',1),('aggregate',2),('cascade',3)))
class PolicerAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Q,1),('drop',2),('remark',3),('explicit-remark',4),('cascadePointer',5)))
class QosObjectMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Z,1),('basic',2),('advance',3),('service',4)))
class QosObjectBasicMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_Q,1),(_P,2),('dscp',3),('dscp-mutation',4),('tcp-udp',5)))
class BinaryStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_Z,1),('enable',2)))
class QueueType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ef',1),('wrr',2)))
class AclDefaultAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('deny-all',1),('forward-all',2)))
class InterfaceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_O,1),('port',2)))
class StatisticsCntrNumOfBitsType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(32,48,64)));namedValues=NamedValues(*(('uint32',32),('uint48',48),('uint64',64)))
class StatisticsCntrType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('statisticsCntrTypeSetDSCP',1),('statisticsCntrTypeDeny',2)))
class RlQosTimeBasedAclWeekPeriodicList(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('monday',0),('tuesday',1),('wednesday',2),('thursday',3),('friday',4),('saturday',5),('sunday',6)))
_RlQosCliQosMode_Type=QosObjectMode
_RlQosCliQosMode_Object=MibScalar
rlQosCliQosMode=_RlQosCliQosMode_Object((1,3,6,1,4,1,171,10,94,89,89,88,1),_RlQosCliQosMode_Type())
rlQosCliQosMode.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosCliQosMode.setStatus(_A)
_RlQosCliBasicModeCfg_Type=QosObjectBasicMode
_RlQosCliBasicModeCfg_Object=MibScalar
rlQosCliBasicModeCfg=_RlQosCliBasicModeCfg_Object((1,3,6,1,4,1,171,10,94,89,89,88,2),_RlQosCliBasicModeCfg_Type())
rlQosCliBasicModeCfg.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosCliBasicModeCfg.setStatus(_A)
_RlQosMaxNumOfAce_Type=Integer32
_RlQosMaxNumOfAce_Object=MibScalar
rlQosMaxNumOfAce=_RlQosMaxNumOfAce_Object((1,3,6,1,4,1,171,10,94,89,89,88,3),_RlQosMaxNumOfAce_Type())
rlQosMaxNumOfAce.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosMaxNumOfAce.setStatus(_A)
_RlQosOffsetTable_Object=MibTable
rlQosOffsetTable=_RlQosOffsetTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,4))
if mibBuilder.loadTexts:rlQosOffsetTable.setStatus(_I)
_RlQosOffsetEntry_Object=MibTableRow
rlQosOffsetEntry=_RlQosOffsetEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,4,1))
rlQosOffsetEntry.setIndexNames((0,_C,_a))
if mibBuilder.loadTexts:rlQosOffsetEntry.setStatus(_I)
_RlQosOffsetIndex_Type=Integer32
_RlQosOffsetIndex_Object=MibTableColumn
rlQosOffsetIndex=_RlQosOffsetIndex_Object((1,3,6,1,4,1,171,10,94,89,89,88,4,1,1),_RlQosOffsetIndex_Type())
rlQosOffsetIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosOffsetIndex.setStatus(_I)
_RlQosOffsetType_Type=ClassOffsetType
_RlQosOffsetType_Object=MibTableColumn
rlQosOffsetType=_RlQosOffsetType_Object((1,3,6,1,4,1,171,10,94,89,89,88,4,1,2),_RlQosOffsetType_Type())
rlQosOffsetType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosOffsetType.setStatus(_I)
_RlQosOffsetValue_Type=Integer32
_RlQosOffsetValue_Object=MibTableColumn
rlQosOffsetValue=_RlQosOffsetValue_Object((1,3,6,1,4,1,171,10,94,89,89,88,4,1,3),_RlQosOffsetValue_Type())
rlQosOffsetValue.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosOffsetValue.setStatus(_I)
class _RlQosOffsetMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RlQosOffsetMask_Type.__name__=_D
_RlQosOffsetMask_Object=MibTableColumn
rlQosOffsetMask=_RlQosOffsetMask_Object((1,3,6,1,4,1,171,10,94,89,89,88,4,1,4),_RlQosOffsetMask_Type())
rlQosOffsetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosOffsetMask.setStatus(_I)
class _RlQosOffsetPattern_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RlQosOffsetPattern_Type.__name__=_D
_RlQosOffsetPattern_Object=MibTableColumn
rlQosOffsetPattern=_RlQosOffsetPattern_Object((1,3,6,1,4,1,171,10,94,89,89,88,4,1,5),_RlQosOffsetPattern_Type())
rlQosOffsetPattern.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosOffsetPattern.setStatus(_I)
_RlQosOffsetTuplePointer_Type=Integer32
_RlQosOffsetTuplePointer_Object=MibTableColumn
rlQosOffsetTuplePointer=_RlQosOffsetTuplePointer_Object((1,3,6,1,4,1,171,10,94,89,89,88,4,1,6),_RlQosOffsetTuplePointer_Type())
rlQosOffsetTuplePointer.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosOffsetTuplePointer.setStatus(_I)
_RlQosOffsetStatus_Type=RowStatus
_RlQosOffsetStatus_Object=MibTableColumn
rlQosOffsetStatus=_RlQosOffsetStatus_Object((1,3,6,1,4,1,171,10,94,89,89,88,4,1,7),_RlQosOffsetStatus_Type())
rlQosOffsetStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosOffsetStatus.setStatus(_I)
_RlQosTupleTable_Object=MibTable
rlQosTupleTable=_RlQosTupleTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,5))
if mibBuilder.loadTexts:rlQosTupleTable.setStatus(_A)
_RlQosTupleEntry_Object=MibTableRow
rlQosTupleEntry=_RlQosTupleEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,5,1))
rlQosTupleEntry.setIndexNames((0,_C,_b))
if mibBuilder.loadTexts:rlQosTupleEntry.setStatus(_A)
_RlQosTupleIndex_Type=Integer32
_RlQosTupleIndex_Object=MibTableColumn
rlQosTupleIndex=_RlQosTupleIndex_Object((1,3,6,1,4,1,171,10,94,89,89,88,5,1,1),_RlQosTupleIndex_Type())
rlQosTupleIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosTupleIndex.setStatus(_A)
_RlQosTupleType_Type=ClassTupleType
_RlQosTupleType_Object=MibTableColumn
rlQosTupleType=_RlQosTupleType_Object((1,3,6,1,4,1,171,10,94,89,89,88,5,1,2),_RlQosTupleType_Type())
rlQosTupleType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosTupleType.setStatus(_A)
_RlQosTupleValue1_Type=Integer32
_RlQosTupleValue1_Object=MibTableColumn
rlQosTupleValue1=_RlQosTupleValue1_Object((1,3,6,1,4,1,171,10,94,89,89,88,5,1,3),_RlQosTupleValue1_Type())
rlQosTupleValue1.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosTupleValue1.setStatus(_A)
class _RlQosTupleValue2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlQosTupleValue2_Type.__name__=_N
_RlQosTupleValue2_Object=MibTableColumn
rlQosTupleValue2=_RlQosTupleValue2_Object((1,3,6,1,4,1,171,10,94,89,89,88,5,1,4),_RlQosTupleValue2_Type())
rlQosTupleValue2.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosTupleValue2.setStatus(_A)
_RlQosTupleStatus_Type=RowStatus
_RlQosTupleStatus_Object=MibTableColumn
rlQosTupleStatus=_RlQosTupleStatus_Object((1,3,6,1,4,1,171,10,94,89,89,88,5,1,5),_RlQosTupleStatus_Type())
rlQosTupleStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosTupleStatus.setStatus(_A)
_RlQosAceTable_Object=MibTable
rlQosAceTable=_RlQosAceTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,6))
if mibBuilder.loadTexts:rlQosAceTable.setStatus(_A)
_RlQosAceEntry_Object=MibTableRow
rlQosAceEntry=_RlQosAceEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,6,1))
rlQosAceEntry.setIndexNames((0,_C,_c))
if mibBuilder.loadTexts:rlQosAceEntry.setStatus(_A)
_RlQosAceIndex_Type=Integer32
_RlQosAceIndex_Object=MibTableColumn
rlQosAceIndex=_RlQosAceIndex_Object((1,3,6,1,4,1,171,10,94,89,89,88,6,1,1),_RlQosAceIndex_Type())
rlQosAceIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosAceIndex.setStatus(_A)
_RlQosAceAction_Type=AceActionType
_RlQosAceAction_Object=MibTableColumn
rlQosAceAction=_RlQosAceAction_Object((1,3,6,1,4,1,171,10,94,89,89,88,6,1,2),_RlQosAceAction_Type())
rlQosAceAction.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAceAction.setStatus(_A)
_RlQosAceType_Type=AceObjectType
_RlQosAceType_Object=MibTableColumn
rlQosAceType=_RlQosAceType_Object((1,3,6,1,4,1,171,10,94,89,89,88,6,1,3),_RlQosAceType_Type())
rlQosAceType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAceType.setStatus(_A)
_RlQosAceTuple1_Type=Integer32
_RlQosAceTuple1_Object=MibTableColumn
rlQosAceTuple1=_RlQosAceTuple1_Object((1,3,6,1,4,1,171,10,94,89,89,88,6,1,4),_RlQosAceTuple1_Type())
rlQosAceTuple1.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAceTuple1.setStatus(_A)
_RlQosAceTuple2_Type=Integer32
_RlQosAceTuple2_Object=MibTableColumn
rlQosAceTuple2=_RlQosAceTuple2_Object((1,3,6,1,4,1,171,10,94,89,89,88,6,1,5),_RlQosAceTuple2_Type())
rlQosAceTuple2.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAceTuple2.setStatus(_A)
_RlQosAceTuple3_Type=Integer32
_RlQosAceTuple3_Object=MibTableColumn
rlQosAceTuple3=_RlQosAceTuple3_Object((1,3,6,1,4,1,171,10,94,89,89,88,6,1,6),_RlQosAceTuple3_Type())
rlQosAceTuple3.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAceTuple3.setStatus(_A)
_RlQosAceTuple4_Type=Integer32
_RlQosAceTuple4_Object=MibTableColumn
rlQosAceTuple4=_RlQosAceTuple4_Object((1,3,6,1,4,1,171,10,94,89,89,88,6,1,7),_RlQosAceTuple4_Type())
rlQosAceTuple4.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAceTuple4.setStatus(_A)
_RlQosAceTuple5_Type=Integer32
_RlQosAceTuple5_Object=MibTableColumn
rlQosAceTuple5=_RlQosAceTuple5_Object((1,3,6,1,4,1,171,10,94,89,89,88,6,1,8),_RlQosAceTuple5_Type())
rlQosAceTuple5.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAceTuple5.setStatus(_A)
_RlQosAceTuple6_Type=Integer32
_RlQosAceTuple6_Object=MibTableColumn
rlQosAceTuple6=_RlQosAceTuple6_Object((1,3,6,1,4,1,171,10,94,89,89,88,6,1,9),_RlQosAceTuple6_Type())
rlQosAceTuple6.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAceTuple6.setStatus(_A)
_RlQosAceTuple7_Type=Integer32
_RlQosAceTuple7_Object=MibTableColumn
rlQosAceTuple7=_RlQosAceTuple7_Object((1,3,6,1,4,1,171,10,94,89,89,88,6,1,10),_RlQosAceTuple7_Type())
rlQosAceTuple7.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAceTuple7.setStatus(_A)
_RlQosAceTuple8_Type=Integer32
_RlQosAceTuple8_Object=MibTableColumn
rlQosAceTuple8=_RlQosAceTuple8_Object((1,3,6,1,4,1,171,10,94,89,89,88,6,1,11),_RlQosAceTuple8_Type())
rlQosAceTuple8.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAceTuple8.setStatus(_A)
_RlQosAceAccount_Type=BinaryStatus
_RlQosAceAccount_Object=MibTableColumn
rlQosAceAccount=_RlQosAceAccount_Object((1,3,6,1,4,1,171,10,94,89,89,88,6,1,12),_RlQosAceAccount_Type())
rlQosAceAccount.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAceAccount.setStatus(_A)
_RlQosAceStatus_Type=RowStatus
_RlQosAceStatus_Object=MibTableColumn
rlQosAceStatus=_RlQosAceStatus_Object((1,3,6,1,4,1,171,10,94,89,89,88,6,1,13),_RlQosAceStatus_Type())
rlQosAceStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAceStatus.setStatus(_A)
_RlQosAclTable_Object=MibTable
rlQosAclTable=_RlQosAclTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,7))
if mibBuilder.loadTexts:rlQosAclTable.setStatus(_A)
_RlQosAclEntry_Object=MibTableRow
rlQosAclEntry=_RlQosAclEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,7,1))
rlQosAclEntry.setIndexNames((0,_C,_d))
if mibBuilder.loadTexts:rlQosAclEntry.setStatus(_A)
_RlQosAclIndex_Type=Integer32
_RlQosAclIndex_Object=MibTableColumn
rlQosAclIndex=_RlQosAclIndex_Object((1,3,6,1,4,1,171,10,94,89,89,88,7,1,1),_RlQosAclIndex_Type())
rlQosAclIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosAclIndex.setStatus(_A)
class _RlQosAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlQosAclName_Type.__name__=_H
_RlQosAclName_Object=MibTableColumn
rlQosAclName=_RlQosAclName_Object((1,3,6,1,4,1,171,10,94,89,89,88,7,1,2),_RlQosAclName_Type())
rlQosAclName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAclName.setStatus(_A)
_RlQosAclType_Type=AclObjectType
_RlQosAclType_Object=MibTableColumn
rlQosAclType=_RlQosAclType_Object((1,3,6,1,4,1,171,10,94,89,89,88,7,1,3),_RlQosAclType_Type())
rlQosAclType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAclType.setStatus(_A)
_RlQosAclStatus_Type=RowStatus
_RlQosAclStatus_Object=MibTableColumn
rlQosAclStatus=_RlQosAclStatus_Object((1,3,6,1,4,1,171,10,94,89,89,88,7,1,4),_RlQosAclStatus_Type())
rlQosAclStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAclStatus.setStatus(_A)
_RlQosAclAceRefTable_Object=MibTable
rlQosAclAceRefTable=_RlQosAclAceRefTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,8))
if mibBuilder.loadTexts:rlQosAclAceRefTable.setStatus(_A)
_RlQosAclAceRefEntry_Object=MibTableRow
rlQosAclAceRefEntry=_RlQosAclAceRefEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,8,1))
rlQosAclAceRefEntry.setIndexNames((0,_C,_e))
if mibBuilder.loadTexts:rlQosAclAceRefEntry.setStatus(_A)
_RlQosAclAceRefAcePointer_Type=Integer32
_RlQosAclAceRefAcePointer_Object=MibTableColumn
rlQosAclAceRefAcePointer=_RlQosAclAceRefAcePointer_Object((1,3,6,1,4,1,171,10,94,89,89,88,8,1,1),_RlQosAclAceRefAcePointer_Type())
rlQosAclAceRefAcePointer.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosAclAceRefAcePointer.setStatus(_A)
_RlQosAclAceRefAclPointer_Type=Integer32
_RlQosAclAceRefAclPointer_Object=MibTableColumn
rlQosAclAceRefAclPointer=_RlQosAclAceRefAclPointer_Object((1,3,6,1,4,1,171,10,94,89,89,88,8,1,2),_RlQosAclAceRefAclPointer_Type())
rlQosAclAceRefAclPointer.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAclAceRefAclPointer.setStatus(_A)
_RlQosAclAceRefStatus_Type=RowStatus
_RlQosAclAceRefStatus_Object=MibTableColumn
rlQosAclAceRefStatus=_RlQosAclAceRefStatus_Object((1,3,6,1,4,1,171,10,94,89,89,88,8,1,3),_RlQosAclAceRefStatus_Type())
rlQosAclAceRefStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAclAceRefStatus.setStatus(_A)
_RlQosClassMapTable_Object=MibTable
rlQosClassMapTable=_RlQosClassMapTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,9))
if mibBuilder.loadTexts:rlQosClassMapTable.setStatus(_A)
_RlQosClassMapEntry_Object=MibTableRow
rlQosClassMapEntry=_RlQosClassMapEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,9,1))
rlQosClassMapEntry.setIndexNames((0,_C,_f))
if mibBuilder.loadTexts:rlQosClassMapEntry.setStatus(_A)
_RlQosClassMapIndex_Type=Integer32
_RlQosClassMapIndex_Object=MibTableColumn
rlQosClassMapIndex=_RlQosClassMapIndex_Object((1,3,6,1,4,1,171,10,94,89,89,88,9,1,1),_RlQosClassMapIndex_Type())
rlQosClassMapIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosClassMapIndex.setStatus(_A)
class _RlQosClassMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlQosClassMapName_Type.__name__=_H
_RlQosClassMapName_Object=MibTableColumn
rlQosClassMapName=_RlQosClassMapName_Object((1,3,6,1,4,1,171,10,94,89,89,88,9,1,2),_RlQosClassMapName_Type())
rlQosClassMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosClassMapName.setStatus(_A)
class _RlQosClassMapType_Type(ClassMapType):defaultValue=1
_RlQosClassMapType_Type.__name__=_g
_RlQosClassMapType_Object=MibTableColumn
rlQosClassMapType=_RlQosClassMapType_Object((1,3,6,1,4,1,171,10,94,89,89,88,9,1,3),_RlQosClassMapType_Type())
rlQosClassMapType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosClassMapType.setStatus(_A)
class _RlQosClassMapAction_Type(ClassMapAction):defaultValue=1
_RlQosClassMapAction_Type.__name__=_h
_RlQosClassMapAction_Object=MibTableColumn
rlQosClassMapAction=_RlQosClassMapAction_Object((1,3,6,1,4,1,171,10,94,89,89,88,9,1,4),_RlQosClassMapAction_Type())
rlQosClassMapAction.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosClassMapAction.setStatus(_A)
class _RlQosClassMapMarkValue_Type(Integer32):defaultValue=0
_RlQosClassMapMarkValue_Type.__name__=_D
_RlQosClassMapMarkValue_Object=MibTableColumn
rlQosClassMapMarkValue=_RlQosClassMapMarkValue_Object((1,3,6,1,4,1,171,10,94,89,89,88,9,1,5),_RlQosClassMapMarkValue_Type())
rlQosClassMapMarkValue.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosClassMapMarkValue.setStatus(_A)
class _RlQosClassMapPolicer_Type(Integer32):defaultValue=0
_RlQosClassMapPolicer_Type.__name__=_D
_RlQosClassMapPolicer_Object=MibTableColumn
rlQosClassMapPolicer=_RlQosClassMapPolicer_Object((1,3,6,1,4,1,171,10,94,89,89,88,9,1,6),_RlQosClassMapPolicer_Type())
rlQosClassMapPolicer.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosClassMapPolicer.setStatus(_A)
_RlQosClassMapMatch1_Type=Integer32
_RlQosClassMapMatch1_Object=MibTableColumn
rlQosClassMapMatch1=_RlQosClassMapMatch1_Object((1,3,6,1,4,1,171,10,94,89,89,88,9,1,7),_RlQosClassMapMatch1_Type())
rlQosClassMapMatch1.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosClassMapMatch1.setStatus(_A)
class _RlQosClassMapMatch2_Type(Integer32):defaultValue=0
_RlQosClassMapMatch2_Type.__name__=_D
_RlQosClassMapMatch2_Object=MibTableColumn
rlQosClassMapMatch2=_RlQosClassMapMatch2_Object((1,3,6,1,4,1,171,10,94,89,89,88,9,1,8),_RlQosClassMapMatch2_Type())
rlQosClassMapMatch2.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosClassMapMatch2.setStatus(_A)
class _RlQosClassMapMarkVlan_Type(BinaryStatus):defaultValue=1
_RlQosClassMapMarkVlan_Type.__name__=_R
_RlQosClassMapMarkVlan_Object=MibTableColumn
rlQosClassMapMarkVlan=_RlQosClassMapMarkVlan_Object((1,3,6,1,4,1,171,10,94,89,89,88,9,1,9),_RlQosClassMapMarkVlan_Type())
rlQosClassMapMarkVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosClassMapMarkVlan.setStatus(_A)
class _RlQosClassMapNewVlan_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_RlQosClassMapNewVlan_Type.__name__=_D
_RlQosClassMapNewVlan_Object=MibTableColumn
rlQosClassMapNewVlan=_RlQosClassMapNewVlan_Object((1,3,6,1,4,1,171,10,94,89,89,88,9,1,10),_RlQosClassMapNewVlan_Type())
rlQosClassMapNewVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosClassMapNewVlan.setStatus(_A)
class _RlQosClassMapNewPort_Type(Integer32):defaultValue=0
_RlQosClassMapNewPort_Type.__name__=_D
_RlQosClassMapNewPort_Object=MibTableColumn
rlQosClassMapNewPort=_RlQosClassMapNewPort_Object((1,3,6,1,4,1,171,10,94,89,89,88,9,1,11),_RlQosClassMapNewPort_Type())
rlQosClassMapNewPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosClassMapNewPort.setStatus(_A)
class _RlQosClassMapCopyPort_Type(Integer32):defaultValue=0
_RlQosClassMapCopyPort_Type.__name__=_D
_RlQosClassMapCopyPort_Object=MibTableColumn
rlQosClassMapCopyPort=_RlQosClassMapCopyPort_Object((1,3,6,1,4,1,171,10,94,89,89,88,9,1,12),_RlQosClassMapCopyPort_Type())
rlQosClassMapCopyPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosClassMapCopyPort.setStatus(_A)
_RlQosClassMapStatus_Type=RowStatus
_RlQosClassMapStatus_Object=MibTableColumn
rlQosClassMapStatus=_RlQosClassMapStatus_Object((1,3,6,1,4,1,171,10,94,89,89,88,9,1,13),_RlQosClassMapStatus_Type())
rlQosClassMapStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosClassMapStatus.setStatus(_A)
class _RlQosClassMapMatch3_Type(Integer32):defaultValue=0
_RlQosClassMapMatch3_Type.__name__=_D
_RlQosClassMapMatch3_Object=MibTableColumn
rlQosClassMapMatch3=_RlQosClassMapMatch3_Object((1,3,6,1,4,1,171,10,94,89,89,88,9,1,14),_RlQosClassMapMatch3_Type())
rlQosClassMapMatch3.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosClassMapMatch3.setStatus(_A)
_RlQosPolicerTable_Object=MibTable
rlQosPolicerTable=_RlQosPolicerTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,10))
if mibBuilder.loadTexts:rlQosPolicerTable.setStatus(_A)
_RlQosPolicerEntry_Object=MibTableRow
rlQosPolicerEntry=_RlQosPolicerEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,10,1))
rlQosPolicerEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:rlQosPolicerEntry.setStatus(_A)
_RlQosPolicerIndex_Type=Integer32
_RlQosPolicerIndex_Object=MibTableColumn
rlQosPolicerIndex=_RlQosPolicerIndex_Object((1,3,6,1,4,1,171,10,94,89,89,88,10,1,1),_RlQosPolicerIndex_Type())
rlQosPolicerIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosPolicerIndex.setStatus(_A)
class _RlQosPolicerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlQosPolicerName_Type.__name__=_H
_RlQosPolicerName_Object=MibTableColumn
rlQosPolicerName=_RlQosPolicerName_Object((1,3,6,1,4,1,171,10,94,89,89,88,10,1,2),_RlQosPolicerName_Type())
rlQosPolicerName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosPolicerName.setStatus(_A)
_RlQosPolicerType_Type=PolicerType
_RlQosPolicerType_Object=MibTableColumn
rlQosPolicerType=_RlQosPolicerType_Object((1,3,6,1,4,1,171,10,94,89,89,88,10,1,3),_RlQosPolicerType_Type())
rlQosPolicerType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosPolicerType.setStatus(_A)
_RlQosPolicerCir_Type=Unsigned32
_RlQosPolicerCir_Object=MibTableColumn
rlQosPolicerCir=_RlQosPolicerCir_Object((1,3,6,1,4,1,171,10,94,89,89,88,10,1,4),_RlQosPolicerCir_Type())
rlQosPolicerCir.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosPolicerCir.setStatus(_A)
if mibBuilder.loadTexts:rlQosPolicerCir.setUnits('kbps')
_RlQosPolicerCbs_Type=Unsigned32
_RlQosPolicerCbs_Object=MibTableColumn
rlQosPolicerCbs=_RlQosPolicerCbs_Object((1,3,6,1,4,1,171,10,94,89,89,88,10,1,5),_RlQosPolicerCbs_Type())
rlQosPolicerCbs.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosPolicerCbs.setStatus(_A)
if mibBuilder.loadTexts:rlQosPolicerCbs.setUnits(_S)
_RlQosPolicerAction_Type=PolicerAction
_RlQosPolicerAction_Object=MibTableColumn
rlQosPolicerAction=_RlQosPolicerAction_Object((1,3,6,1,4,1,171,10,94,89,89,88,10,1,6),_RlQosPolicerAction_Type())
rlQosPolicerAction.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosPolicerAction.setStatus(_A)
_RlQosPolicerCasPointerRemVal_Type=Integer32
_RlQosPolicerCasPointerRemVal_Object=MibTableColumn
rlQosPolicerCasPointerRemVal=_RlQosPolicerCasPointerRemVal_Object((1,3,6,1,4,1,171,10,94,89,89,88,10,1,7),_RlQosPolicerCasPointerRemVal_Type())
rlQosPolicerCasPointerRemVal.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosPolicerCasPointerRemVal.setStatus(_A)
_RlQosPolicerStatus_Type=RowStatus
_RlQosPolicerStatus_Object=MibTableColumn
rlQosPolicerStatus=_RlQosPolicerStatus_Object((1,3,6,1,4,1,171,10,94,89,89,88,10,1,8),_RlQosPolicerStatus_Type())
rlQosPolicerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosPolicerStatus.setStatus(_A)
_RlQosPolicyMapTable_Object=MibTable
rlQosPolicyMapTable=_RlQosPolicyMapTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,11))
if mibBuilder.loadTexts:rlQosPolicyMapTable.setStatus(_A)
_RlQosPolicyMapEntry_Object=MibTableRow
rlQosPolicyMapEntry=_RlQosPolicyMapEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,11,1))
rlQosPolicyMapEntry.setIndexNames((0,_C,_i))
if mibBuilder.loadTexts:rlQosPolicyMapEntry.setStatus(_A)
_RlQosPolicyMapIndex_Type=Integer32
_RlQosPolicyMapIndex_Object=MibTableColumn
rlQosPolicyMapIndex=_RlQosPolicyMapIndex_Object((1,3,6,1,4,1,171,10,94,89,89,88,11,1,1),_RlQosPolicyMapIndex_Type())
rlQosPolicyMapIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosPolicyMapIndex.setStatus(_A)
class _RlQosPolicyMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlQosPolicyMapName_Type.__name__=_H
_RlQosPolicyMapName_Object=MibTableColumn
rlQosPolicyMapName=_RlQosPolicyMapName_Object((1,3,6,1,4,1,171,10,94,89,89,88,11,1,2),_RlQosPolicyMapName_Type())
rlQosPolicyMapName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosPolicyMapName.setStatus(_A)
_RlQosPolicyMapStatus_Type=RowStatus
_RlQosPolicyMapStatus_Object=MibTableColumn
rlQosPolicyMapStatus=_RlQosPolicyMapStatus_Object((1,3,6,1,4,1,171,10,94,89,89,88,11,1,3),_RlQosPolicyMapStatus_Type())
rlQosPolicyMapStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosPolicyMapStatus.setStatus(_A)
_RlQosPolicyClassRefTable_Object=MibTable
rlQosPolicyClassRefTable=_RlQosPolicyClassRefTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,12))
if mibBuilder.loadTexts:rlQosPolicyClassRefTable.setStatus(_A)
_RlQosPolicyClassRefEntry_Object=MibTableRow
rlQosPolicyClassRefEntry=_RlQosPolicyClassRefEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,12,1))
rlQosPolicyClassRefEntry.setIndexNames((0,_C,_j))
if mibBuilder.loadTexts:rlQosPolicyClassRefEntry.setStatus(_A)
_RlQosPolicyClassRefClassPointer_Type=Integer32
_RlQosPolicyClassRefClassPointer_Object=MibTableColumn
rlQosPolicyClassRefClassPointer=_RlQosPolicyClassRefClassPointer_Object((1,3,6,1,4,1,171,10,94,89,89,88,12,1,1),_RlQosPolicyClassRefClassPointer_Type())
rlQosPolicyClassRefClassPointer.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosPolicyClassRefClassPointer.setStatus(_A)
_RlQosPolicyClassRefPolicyPointer_Type=Integer32
_RlQosPolicyClassRefPolicyPointer_Object=MibTableColumn
rlQosPolicyClassRefPolicyPointer=_RlQosPolicyClassRefPolicyPointer_Object((1,3,6,1,4,1,171,10,94,89,89,88,12,1,2),_RlQosPolicyClassRefPolicyPointer_Type())
rlQosPolicyClassRefPolicyPointer.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosPolicyClassRefPolicyPointer.setStatus(_A)
_RlQosPolicyClassRefStatus_Type=RowStatus
_RlQosPolicyClassRefStatus_Object=MibTableColumn
rlQosPolicyClassRefStatus=_RlQosPolicyClassRefStatus_Object((1,3,6,1,4,1,171,10,94,89,89,88,12,1,3),_RlQosPolicyClassRefStatus_Type())
rlQosPolicyClassRefStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosPolicyClassRefStatus.setStatus(_A)
_RlQosIfPolicyTable_Object=MibTable
rlQosIfPolicyTable=_RlQosIfPolicyTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,13))
if mibBuilder.loadTexts:rlQosIfPolicyTable.setStatus(_A)
_RlQosIfPolicyEntry_Object=MibTableRow
rlQosIfPolicyEntry=_RlQosIfPolicyEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,13,1))
rlQosIfPolicyEntry.setIndexNames((0,_C,_M),(0,_C,_T))
if mibBuilder.loadTexts:rlQosIfPolicyEntry.setStatus(_A)
_RlIfIndex_Type=Integer32
_RlIfIndex_Object=MibTableColumn
rlIfIndex=_RlIfIndex_Object((1,3,6,1,4,1,171,10,94,89,89,88,13,1,1),_RlIfIndex_Type())
rlIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlIfIndex.setStatus(_A)
_RlIfType_Type=InterfaceType
_RlIfType_Object=MibTableColumn
rlIfType=_RlIfType_Object((1,3,6,1,4,1,171,10,94,89,89,88,13,1,2),_RlIfType_Type())
rlIfType.setMaxAccess(_F)
if mibBuilder.loadTexts:rlIfType.setStatus(_A)
_RlQosIfPolicyMapPointerIn_Type=Integer32
_RlQosIfPolicyMapPointerIn_Object=MibTableColumn
rlQosIfPolicyMapPointerIn=_RlQosIfPolicyMapPointerIn_Object((1,3,6,1,4,1,171,10,94,89,89,88,13,1,3),_RlQosIfPolicyMapPointerIn_Type())
rlQosIfPolicyMapPointerIn.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosIfPolicyMapPointerIn.setStatus(_A)
_RlQosIfPolicyMapPointerOut_Type=Integer32
_RlQosIfPolicyMapPointerOut_Object=MibTableColumn
rlQosIfPolicyMapPointerOut=_RlQosIfPolicyMapPointerOut_Object((1,3,6,1,4,1,171,10,94,89,89,88,13,1,4),_RlQosIfPolicyMapPointerOut_Type())
rlQosIfPolicyMapPointerOut.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosIfPolicyMapPointerOut.setStatus(_A)
_RlQosIfTrustActive_Type=BinaryStatus
_RlQosIfTrustActive_Object=MibTableColumn
rlQosIfTrustActive=_RlQosIfTrustActive_Object((1,3,6,1,4,1,171,10,94,89,89,88,13,1,5),_RlQosIfTrustActive_Type())
rlQosIfTrustActive.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosIfTrustActive.setStatus(_A)
_RlQosPortShaperStatus_Type=BinaryStatus
_RlQosPortShaperStatus_Object=MibTableColumn
rlQosPortShaperStatus=_RlQosPortShaperStatus_Object((1,3,6,1,4,1,171,10,94,89,89,88,13,1,6),_RlQosPortShaperStatus_Type())
rlQosPortShaperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosPortShaperStatus.setStatus(_A)
_RlQosCirPortShaper_Type=Integer32
_RlQosCirPortShaper_Object=MibTableColumn
rlQosCirPortShaper=_RlQosCirPortShaper_Object((1,3,6,1,4,1,171,10,94,89,89,88,13,1,7),_RlQosCirPortShaper_Type())
rlQosCirPortShaper.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosCirPortShaper.setStatus(_A)
if mibBuilder.loadTexts:rlQosCirPortShaper.setUnits('bps')
_RlQosCbsPortShaper_Type=Integer32
_RlQosCbsPortShaper_Object=MibTableColumn
rlQosCbsPortShaper=_RlQosCbsPortShaper_Object((1,3,6,1,4,1,171,10,94,89,89,88,13,1,8),_RlQosCbsPortShaper_Type())
rlQosCbsPortShaper.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosCbsPortShaper.setStatus(_A)
if mibBuilder.loadTexts:rlQosCbsPortShaper.setUnits(_S)
class _RlQosIfProfilePointer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlQosIfProfilePointer_Type.__name__=_H
_RlQosIfProfilePointer_Object=MibTableColumn
rlQosIfProfilePointer=_RlQosIfProfilePointer_Object((1,3,6,1,4,1,171,10,94,89,89,88,13,1,9),_RlQosIfProfilePointer_Type())
rlQosIfProfilePointer.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosIfProfilePointer.setStatus(_A)
class _RlQosQueueProfilePointer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlQosQueueProfilePointer_Type.__name__=_H
_RlQosQueueProfilePointer_Object=MibTableColumn
rlQosQueueProfilePointer=_RlQosQueueProfilePointer_Object((1,3,6,1,4,1,171,10,94,89,89,88,13,1,10),_RlQosQueueProfilePointer_Type())
rlQosQueueProfilePointer.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosQueueProfilePointer.setStatus(_A)
_RlQosQueueShapeProfilePointer_Type=Integer32
_RlQosQueueShapeProfilePointer_Object=MibTableColumn
rlQosQueueShapeProfilePointer=_RlQosQueueShapeProfilePointer_Object((1,3,6,1,4,1,171,10,94,89,89,88,13,1,11),_RlQosQueueShapeProfilePointer_Type())
rlQosQueueShapeProfilePointer.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosQueueShapeProfilePointer.setStatus(_A)
_RlQosAclDefaultAction_Type=AclDefaultAction
_RlQosAclDefaultAction_Object=MibTableColumn
rlQosAclDefaultAction=_RlQosAclDefaultAction_Object((1,3,6,1,4,1,171,10,94,89,89,88,13,1,12),_RlQosAclDefaultAction_Type())
rlQosAclDefaultAction.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAclDefaultAction.setStatus(_A)
_RlQosIfPolicyMapStatus_Type=RowStatus
_RlQosIfPolicyMapStatus_Object=MibTableColumn
rlQosIfPolicyMapStatus=_RlQosIfPolicyMapStatus_Object((1,3,6,1,4,1,171,10,94,89,89,88,13,1,13),_RlQosIfPolicyMapStatus_Type())
rlQosIfPolicyMapStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosIfPolicyMapStatus.setStatus(_A)
class _RlQosIfAclIn_Type(Integer32):defaultValue=0
_RlQosIfAclIn_Type.__name__=_D
_RlQosIfAclIn_Object=MibTableColumn
rlQosIfAclIn=_RlQosIfAclIn_Object((1,3,6,1,4,1,171,10,94,89,89,88,13,1,14),_RlQosIfAclIn_Type())
rlQosIfAclIn.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosIfAclIn.setStatus(_A)
class _RlQosIfAclOut_Type(Integer32):defaultValue=0
_RlQosIfAclOut_Type.__name__=_D
_RlQosIfAclOut_Object=MibTableColumn
rlQosIfAclOut=_RlQosIfAclOut_Object((1,3,6,1,4,1,171,10,94,89,89,88,13,1,15),_RlQosIfAclOut_Type())
rlQosIfAclOut.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosIfAclOut.setStatus(_A)
class _RlQosIfPolicerIn_Type(Integer32):defaultValue=0
_RlQosIfPolicerIn_Type.__name__=_D
_RlQosIfPolicerIn_Object=MibTableColumn
rlQosIfPolicerIn=_RlQosIfPolicerIn_Object((1,3,6,1,4,1,171,10,94,89,89,88,13,1,16),_RlQosIfPolicerIn_Type())
rlQosIfPolicerIn.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosIfPolicerIn.setStatus(_A)
class _RlQosPortRateLimitStatus_Type(BinaryStatus):defaultValue=1
_RlQosPortRateLimitStatus_Type.__name__=_R
_RlQosPortRateLimitStatus_Object=MibTableColumn
rlQosPortRateLimitStatus=_RlQosPortRateLimitStatus_Object((1,3,6,1,4,1,171,10,94,89,89,88,13,1,17),_RlQosPortRateLimitStatus_Type())
rlQosPortRateLimitStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosPortRateLimitStatus.setStatus(_A)
class _RlQosCirPortRateLimit_Type(Integer32):defaultValue=0
_RlQosCirPortRateLimit_Type.__name__=_D
_RlQosCirPortRateLimit_Object=MibTableColumn
rlQosCirPortRateLimit=_RlQosCirPortRateLimit_Object((1,3,6,1,4,1,171,10,94,89,89,88,13,1,18),_RlQosCirPortRateLimit_Type())
rlQosCirPortRateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosCirPortRateLimit.setStatus(_A)
if mibBuilder.loadTexts:rlQosCirPortRateLimit.setUnits('bps')
class _RlQosCbsPortRateLimit_Type(Integer32):defaultValue=0
_RlQosCbsPortRateLimit_Type.__name__=_D
_RlQosCbsPortRateLimit_Object=MibTableColumn
rlQosCbsPortRateLimit=_RlQosCbsPortRateLimit_Object((1,3,6,1,4,1,171,10,94,89,89,88,13,1,19),_RlQosCbsPortRateLimit_Type())
rlQosCbsPortRateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosCbsPortRateLimit.setStatus(_A)
if mibBuilder.loadTexts:rlQosCbsPortRateLimit.setUnits(_S)
class _RlQosIfIpv6AclIn_Type(Integer32):defaultValue=0
_RlQosIfIpv6AclIn_Type.__name__=_D
_RlQosIfIpv6AclIn_Object=MibTableColumn
rlQosIfIpv6AclIn=_RlQosIfIpv6AclIn_Object((1,3,6,1,4,1,171,10,94,89,89,88,13,1,20),_RlQosIfIpv6AclIn_Type())
rlQosIfIpv6AclIn.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosIfIpv6AclIn.setStatus(_A)
class _RlQosIfIpv6AclOut_Type(Integer32):defaultValue=0
_RlQosIfIpv6AclOut_Type.__name__=_D
_RlQosIfIpv6AclOut_Object=MibTableColumn
rlQosIfIpv6AclOut=_RlQosIfIpv6AclOut_Object((1,3,6,1,4,1,171,10,94,89,89,88,13,1,21),_RlQosIfIpv6AclOut_Type())
rlQosIfIpv6AclOut.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosIfIpv6AclOut.setStatus(_A)
_RlQosIfProfileCfgTable_Object=MibTable
rlQosIfProfileCfgTable=_RlQosIfProfileCfgTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,14))
if mibBuilder.loadTexts:rlQosIfProfileCfgTable.setStatus(_A)
_RlQosIfProfileCfgEntry_Object=MibTableRow
rlQosIfProfileCfgEntry=_RlQosIfProfileCfgEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,14,1))
rlQosIfProfileCfgEntry.setIndexNames((0,_C,_k),(0,_C,_l))
if mibBuilder.loadTexts:rlQosIfProfileCfgEntry.setStatus(_A)
class _RlIfProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlIfProfileName_Type.__name__=_H
_RlIfProfileName_Object=MibTableColumn
rlIfProfileName=_RlIfProfileName_Object((1,3,6,1,4,1,171,10,94,89,89,88,14,1,1),_RlIfProfileName_Type())
rlIfProfileName.setMaxAccess(_F)
if mibBuilder.loadTexts:rlIfProfileName.setStatus(_A)
class _RlQosQueueId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RlQosQueueId_Type.__name__=_D
_RlQosQueueId_Object=MibTableColumn
rlQosQueueId=_RlQosQueueId_Object((1,3,6,1,4,1,171,10,94,89,89,88,14,1,2),_RlQosQueueId_Type())
rlQosQueueId.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosQueueId.setStatus(_A)
class _RlQosTdThersholdDp0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RlQosTdThersholdDp0_Type.__name__=_D
_RlQosTdThersholdDp0_Object=MibTableColumn
rlQosTdThersholdDp0=_RlQosTdThersholdDp0_Object((1,3,6,1,4,1,171,10,94,89,89,88,14,1,3),_RlQosTdThersholdDp0_Type())
rlQosTdThersholdDp0.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosTdThersholdDp0.setStatus(_A)
if mibBuilder.loadTexts:rlQosTdThersholdDp0.setUnits(_J)
class _RlQosTdThersholdDp1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RlQosTdThersholdDp1_Type.__name__=_D
_RlQosTdThersholdDp1_Object=MibTableColumn
rlQosTdThersholdDp1=_RlQosTdThersholdDp1_Object((1,3,6,1,4,1,171,10,94,89,89,88,14,1,4),_RlQosTdThersholdDp1_Type())
rlQosTdThersholdDp1.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosTdThersholdDp1.setStatus(_A)
if mibBuilder.loadTexts:rlQosTdThersholdDp1.setUnits(_J)
class _RlQosTdThersholdDp2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RlQosTdThersholdDp2_Type.__name__=_D
_RlQosTdThersholdDp2_Object=MibTableColumn
rlQosTdThersholdDp2=_RlQosTdThersholdDp2_Object((1,3,6,1,4,1,171,10,94,89,89,88,14,1,5),_RlQosTdThersholdDp2_Type())
rlQosTdThersholdDp2.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosTdThersholdDp2.setStatus(_A)
if mibBuilder.loadTexts:rlQosTdThersholdDp2.setUnits(_J)
class _RlQosRedMinDp0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RlQosRedMinDp0_Type.__name__=_D
_RlQosRedMinDp0_Object=MibTableColumn
rlQosRedMinDp0=_RlQosRedMinDp0_Object((1,3,6,1,4,1,171,10,94,89,89,88,14,1,6),_RlQosRedMinDp0_Type())
rlQosRedMinDp0.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosRedMinDp0.setStatus(_A)
if mibBuilder.loadTexts:rlQosRedMinDp0.setUnits(_J)
class _RlQosRedMaxDp0_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RlQosRedMaxDp0_Type.__name__=_D
_RlQosRedMaxDp0_Object=MibTableColumn
rlQosRedMaxDp0=_RlQosRedMaxDp0_Object((1,3,6,1,4,1,171,10,94,89,89,88,14,1,7),_RlQosRedMaxDp0_Type())
rlQosRedMaxDp0.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosRedMaxDp0.setStatus(_A)
if mibBuilder.loadTexts:rlQosRedMaxDp0.setUnits(_J)
_RlQosRedProbDp0_Type=Integer32
_RlQosRedProbDp0_Object=MibTableColumn
rlQosRedProbDp0=_RlQosRedProbDp0_Object((1,3,6,1,4,1,171,10,94,89,89,88,14,1,8),_RlQosRedProbDp0_Type())
rlQosRedProbDp0.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosRedProbDp0.setStatus(_A)
class _RlQosRedMinDp1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RlQosRedMinDp1_Type.__name__=_D
_RlQosRedMinDp1_Object=MibTableColumn
rlQosRedMinDp1=_RlQosRedMinDp1_Object((1,3,6,1,4,1,171,10,94,89,89,88,14,1,9),_RlQosRedMinDp1_Type())
rlQosRedMinDp1.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosRedMinDp1.setStatus(_A)
if mibBuilder.loadTexts:rlQosRedMinDp1.setUnits(_J)
class _RlQosRedMaxDp1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RlQosRedMaxDp1_Type.__name__=_D
_RlQosRedMaxDp1_Object=MibTableColumn
rlQosRedMaxDp1=_RlQosRedMaxDp1_Object((1,3,6,1,4,1,171,10,94,89,89,88,14,1,10),_RlQosRedMaxDp1_Type())
rlQosRedMaxDp1.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosRedMaxDp1.setStatus(_A)
if mibBuilder.loadTexts:rlQosRedMaxDp1.setUnits(_J)
_RlQosRedProbDp1_Type=Integer32
_RlQosRedProbDp1_Object=MibTableColumn
rlQosRedProbDp1=_RlQosRedProbDp1_Object((1,3,6,1,4,1,171,10,94,89,89,88,14,1,11),_RlQosRedProbDp1_Type())
rlQosRedProbDp1.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosRedProbDp1.setStatus(_A)
class _RlQosRedMinDp2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RlQosRedMinDp2_Type.__name__=_D
_RlQosRedMinDp2_Object=MibTableColumn
rlQosRedMinDp2=_RlQosRedMinDp2_Object((1,3,6,1,4,1,171,10,94,89,89,88,14,1,12),_RlQosRedMinDp2_Type())
rlQosRedMinDp2.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosRedMinDp2.setStatus(_A)
if mibBuilder.loadTexts:rlQosRedMinDp2.setUnits(_J)
class _RlQosRedMaxDp2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RlQosRedMaxDp2_Type.__name__=_D
_RlQosRedMaxDp2_Object=MibTableColumn
rlQosRedMaxDp2=_RlQosRedMaxDp2_Object((1,3,6,1,4,1,171,10,94,89,89,88,14,1,13),_RlQosRedMaxDp2_Type())
rlQosRedMaxDp2.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosRedMaxDp2.setStatus(_A)
if mibBuilder.loadTexts:rlQosRedMaxDp2.setUnits(_J)
_RlQosRedProbDp2_Type=Integer32
_RlQosRedProbDp2_Object=MibTableColumn
rlQosRedProbDp2=_RlQosRedProbDp2_Object((1,3,6,1,4,1,171,10,94,89,89,88,14,1,14),_RlQosRedProbDp2_Type())
rlQosRedProbDp2.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosRedProbDp2.setStatus(_A)
_RlQosRedQweight_Type=Integer32
_RlQosRedQweight_Object=MibTableColumn
rlQosRedQweight=_RlQosRedQweight_Object((1,3,6,1,4,1,171,10,94,89,89,88,14,1,15),_RlQosRedQweight_Type())
rlQosRedQweight.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosRedQweight.setStatus(_A)
_RlQosIfprofileStatus_Type=RowStatus
_RlQosIfprofileStatus_Object=MibTableColumn
rlQosIfprofileStatus=_RlQosIfprofileStatus_Object((1,3,6,1,4,1,171,10,94,89,89,88,14,1,16),_RlQosIfprofileStatus_Type())
rlQosIfprofileStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosIfprofileStatus.setStatus(_A)
_RlQosDscpMutationTable_Object=MibTable
rlQosDscpMutationTable=_RlQosDscpMutationTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,15))
if mibBuilder.loadTexts:rlQosDscpMutationTable.setStatus(_A)
_RlQosDscpMutationEntry_Object=MibTableRow
rlQosDscpMutationEntry=_RlQosDscpMutationEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,15,1))
rlQosDscpMutationEntry.setIndexNames((0,_C,_m))
if mibBuilder.loadTexts:rlQosDscpMutationEntry.setStatus(_A)
class _RlQosOldDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RlQosOldDscp_Type.__name__=_D
_RlQosOldDscp_Object=MibTableColumn
rlQosOldDscp=_RlQosOldDscp_Object((1,3,6,1,4,1,171,10,94,89,89,88,15,1,1),_RlQosOldDscp_Type())
rlQosOldDscp.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosOldDscp.setStatus(_A)
class _RlQosNewDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RlQosNewDscp_Type.__name__=_D
_RlQosNewDscp_Object=MibTableColumn
rlQosNewDscp=_RlQosNewDscp_Object((1,3,6,1,4,1,171,10,94,89,89,88,15,1,2),_RlQosNewDscp_Type())
rlQosNewDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosNewDscp.setStatus(_A)
_RlQosDscpRemarkTable_Object=MibTable
rlQosDscpRemarkTable=_RlQosDscpRemarkTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,16))
if mibBuilder.loadTexts:rlQosDscpRemarkTable.setStatus(_A)
_RlQosDscpRemarkEntry_Object=MibTableRow
rlQosDscpRemarkEntry=_RlQosDscpRemarkEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,16,1))
rlQosDscpRemarkEntry.setIndexNames((0,_C,_n))
if mibBuilder.loadTexts:rlQosDscpRemarkEntry.setStatus(_A)
class _RlQosRmOldDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RlQosRmOldDscp_Type.__name__=_D
_RlQosRmOldDscp_Object=MibTableColumn
rlQosRmOldDscp=_RlQosRmOldDscp_Object((1,3,6,1,4,1,171,10,94,89,89,88,16,1,1),_RlQosRmOldDscp_Type())
rlQosRmOldDscp.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosRmOldDscp.setStatus(_A)
class _RlQosRmNewDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RlQosRmNewDscp_Type.__name__=_D
_RlQosRmNewDscp_Object=MibTableColumn
rlQosRmNewDscp=_RlQosRmNewDscp_Object((1,3,6,1,4,1,171,10,94,89,89,88,16,1,2),_RlQosRmNewDscp_Type())
rlQosRmNewDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosRmNewDscp.setStatus(_A)
_RlQosCosQueueTable_Object=MibTable
rlQosCosQueueTable=_RlQosCosQueueTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,17))
if mibBuilder.loadTexts:rlQosCosQueueTable.setStatus(_A)
_RlQosCosQueueEntry_Object=MibTableRow
rlQosCosQueueEntry=_RlQosCosQueueEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,17,1))
rlQosCosQueueEntry.setIndexNames((0,_C,_o))
if mibBuilder.loadTexts:rlQosCosQueueEntry.setStatus(_A)
class _RlQosCosIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RlQosCosIndex_Type.__name__=_D
_RlQosCosIndex_Object=MibTableColumn
rlQosCosIndex=_RlQosCosIndex_Object((1,3,6,1,4,1,171,10,94,89,89,88,17,1,1),_RlQosCosIndex_Type())
rlQosCosIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosCosIndex.setStatus(_A)
class _RlQosCosQueueId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RlQosCosQueueId_Type.__name__=_D
_RlQosCosQueueId_Object=MibTableColumn
rlQosCosQueueId=_RlQosCosQueueId_Object((1,3,6,1,4,1,171,10,94,89,89,88,17,1,2),_RlQosCosQueueId_Type())
rlQosCosQueueId.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosCosQueueId.setStatus(_A)
_RlQosDscpQueueTable_Object=MibTable
rlQosDscpQueueTable=_RlQosDscpQueueTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,18))
if mibBuilder.loadTexts:rlQosDscpQueueTable.setStatus(_A)
_RlQosDscpQueueEntry_Object=MibTableRow
rlQosDscpQueueEntry=_RlQosDscpQueueEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,18,1))
rlQosDscpQueueEntry.setIndexNames((0,_C,_p))
if mibBuilder.loadTexts:rlQosDscpQueueEntry.setStatus(_A)
class _RlQosDscpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RlQosDscpIndex_Type.__name__=_D
_RlQosDscpIndex_Object=MibTableColumn
rlQosDscpIndex=_RlQosDscpIndex_Object((1,3,6,1,4,1,171,10,94,89,89,88,18,1,1),_RlQosDscpIndex_Type())
rlQosDscpIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosDscpIndex.setStatus(_A)
class _RlQosQueueNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RlQosQueueNum_Type.__name__=_D
_RlQosQueueNum_Object=MibTableColumn
rlQosQueueNum=_RlQosQueueNum_Object((1,3,6,1,4,1,171,10,94,89,89,88,18,1,2),_RlQosQueueNum_Type())
rlQosQueueNum.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosQueueNum.setStatus(_A)
_RlQosTcpPortQueueTable_Object=MibTable
rlQosTcpPortQueueTable=_RlQosTcpPortQueueTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,19))
if mibBuilder.loadTexts:rlQosTcpPortQueueTable.setStatus(_A)
_RlQosTcpPortQueueEntry_Object=MibTableRow
rlQosTcpPortQueueEntry=_RlQosTcpPortQueueEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,19,1))
rlQosTcpPortQueueEntry.setIndexNames((0,_C,_q))
if mibBuilder.loadTexts:rlQosTcpPortQueueEntry.setStatus(_A)
_RlQosTcpPort_Type=Integer32
_RlQosTcpPort_Object=MibTableColumn
rlQosTcpPort=_RlQosTcpPort_Object((1,3,6,1,4,1,171,10,94,89,89,88,19,1,1),_RlQosTcpPort_Type())
rlQosTcpPort.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosTcpPort.setStatus(_A)
class _RlQosTcpQueueValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RlQosTcpQueueValue_Type.__name__=_D
_RlQosTcpQueueValue_Object=MibTableColumn
rlQosTcpQueueValue=_RlQosTcpQueueValue_Object((1,3,6,1,4,1,171,10,94,89,89,88,19,1,2),_RlQosTcpQueueValue_Type())
rlQosTcpQueueValue.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosTcpQueueValue.setStatus(_A)
_RlQosTcpPortQueueStatus_Type=RowStatus
_RlQosTcpPortQueueStatus_Object=MibTableColumn
rlQosTcpPortQueueStatus=_RlQosTcpPortQueueStatus_Object((1,3,6,1,4,1,171,10,94,89,89,88,19,1,3),_RlQosTcpPortQueueStatus_Type())
rlQosTcpPortQueueStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosTcpPortQueueStatus.setStatus(_A)
_RlQosUdpPortQueueTable_Object=MibTable
rlQosUdpPortQueueTable=_RlQosUdpPortQueueTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,20))
if mibBuilder.loadTexts:rlQosUdpPortQueueTable.setStatus(_A)
_RlQosUdpPortQueueEntry_Object=MibTableRow
rlQosUdpPortQueueEntry=_RlQosUdpPortQueueEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,20,1))
rlQosUdpPortQueueEntry.setIndexNames((0,_C,_r))
if mibBuilder.loadTexts:rlQosUdpPortQueueEntry.setStatus(_A)
_RlQosUdpPort_Type=Integer32
_RlQosUdpPort_Object=MibTableColumn
rlQosUdpPort=_RlQosUdpPort_Object((1,3,6,1,4,1,171,10,94,89,89,88,20,1,1),_RlQosUdpPort_Type())
rlQosUdpPort.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosUdpPort.setStatus(_A)
class _RlQosUdpQueueValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RlQosUdpQueueValue_Type.__name__=_D
_RlQosUdpQueueValue_Object=MibTableColumn
rlQosUdpQueueValue=_RlQosUdpQueueValue_Object((1,3,6,1,4,1,171,10,94,89,89,88,20,1,2),_RlQosUdpQueueValue_Type())
rlQosUdpQueueValue.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosUdpQueueValue.setStatus(_A)
_RlQosUdpPortQueueStatus_Type=RowStatus
_RlQosUdpPortQueueStatus_Object=MibTableColumn
rlQosUdpPortQueueStatus=_RlQosUdpPortQueueStatus_Object((1,3,6,1,4,1,171,10,94,89,89,88,20,1,3),_RlQosUdpPortQueueStatus_Type())
rlQosUdpPortQueueStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosUdpPortQueueStatus.setStatus(_A)
_RlQosEfManageTable_Object=MibTable
rlQosEfManageTable=_RlQosEfManageTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,21))
if mibBuilder.loadTexts:rlQosEfManageTable.setStatus(_A)
_RlQosEfManageEntry_Object=MibTableRow
rlQosEfManageEntry=_RlQosEfManageEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,21,1))
rlQosEfManageEntry.setIndexNames((0,_C,_s))
if mibBuilder.loadTexts:rlQosEfManageEntry.setStatus(_A)
class _RlQosEfQueueId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RlQosEfQueueId_Type.__name__=_D
_RlQosEfQueueId_Object=MibTableColumn
rlQosEfQueueId=_RlQosEfQueueId_Object((1,3,6,1,4,1,171,10,94,89,89,88,21,1,1),_RlQosEfQueueId_Type())
rlQosEfQueueId.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosEfQueueId.setStatus(_A)
_RlQosEfState_Type=BinaryStatus
_RlQosEfState_Object=MibTableColumn
rlQosEfState=_RlQosEfState_Object((1,3,6,1,4,1,171,10,94,89,89,88,21,1,2),_RlQosEfState_Type())
rlQosEfState.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosEfState.setStatus(_A)
class _RlQosEfPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RlQosEfPriority_Type.__name__=_D
_RlQosEfPriority_Object=MibTableColumn
rlQosEfPriority=_RlQosEfPriority_Object((1,3,6,1,4,1,171,10,94,89,89,88,21,1,3),_RlQosEfPriority_Type())
rlQosEfPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosEfPriority.setStatus(_A)
_RlQosQueueProfileTable_Object=MibTable
rlQosQueueProfileTable=_RlQosQueueProfileTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,22))
if mibBuilder.loadTexts:rlQosQueueProfileTable.setStatus(_A)
_RlQosQueueProfileEntry_Object=MibTableRow
rlQosQueueProfileEntry=_RlQosQueueProfileEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,22,1))
rlQosQueueProfileEntry.setIndexNames((0,_C,_t))
if mibBuilder.loadTexts:rlQosQueueProfileEntry.setStatus(_A)
class _RlQueueProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlQueueProfileName_Type.__name__=_H
_RlQueueProfileName_Object=MibTableColumn
rlQueueProfileName=_RlQueueProfileName_Object((1,3,6,1,4,1,171,10,94,89,89,88,22,1,1),_RlQueueProfileName_Type())
rlQueueProfileName.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQueueProfileName.setStatus(_A)
_RlQosTypeQueue1_Type=QueueType
_RlQosTypeQueue1_Object=MibTableColumn
rlQosTypeQueue1=_RlQosTypeQueue1_Object((1,3,6,1,4,1,171,10,94,89,89,88,22,1,2),_RlQosTypeQueue1_Type())
rlQosTypeQueue1.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosTypeQueue1.setStatus(_A)
_RlQosValueQueue1_Type=Integer32
_RlQosValueQueue1_Object=MibTableColumn
rlQosValueQueue1=_RlQosValueQueue1_Object((1,3,6,1,4,1,171,10,94,89,89,88,22,1,3),_RlQosValueQueue1_Type())
rlQosValueQueue1.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosValueQueue1.setStatus(_A)
_RlQosTypeQueue2_Type=QueueType
_RlQosTypeQueue2_Object=MibTableColumn
rlQosTypeQueue2=_RlQosTypeQueue2_Object((1,3,6,1,4,1,171,10,94,89,89,88,22,1,4),_RlQosTypeQueue2_Type())
rlQosTypeQueue2.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosTypeQueue2.setStatus(_A)
_RlQosValueQueue2_Type=Integer32
_RlQosValueQueue2_Object=MibTableColumn
rlQosValueQueue2=_RlQosValueQueue2_Object((1,3,6,1,4,1,171,10,94,89,89,88,22,1,5),_RlQosValueQueue2_Type())
rlQosValueQueue2.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosValueQueue2.setStatus(_A)
_RlQosTypeQueue3_Type=QueueType
_RlQosTypeQueue3_Object=MibTableColumn
rlQosTypeQueue3=_RlQosTypeQueue3_Object((1,3,6,1,4,1,171,10,94,89,89,88,22,1,6),_RlQosTypeQueue3_Type())
rlQosTypeQueue3.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosTypeQueue3.setStatus(_A)
_RlQosValueQueue3_Type=Integer32
_RlQosValueQueue3_Object=MibTableColumn
rlQosValueQueue3=_RlQosValueQueue3_Object((1,3,6,1,4,1,171,10,94,89,89,88,22,1,7),_RlQosValueQueue3_Type())
rlQosValueQueue3.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosValueQueue3.setStatus(_A)
_RlQosTypeQueue4_Type=QueueType
_RlQosTypeQueue4_Object=MibTableColumn
rlQosTypeQueue4=_RlQosTypeQueue4_Object((1,3,6,1,4,1,171,10,94,89,89,88,22,1,8),_RlQosTypeQueue4_Type())
rlQosTypeQueue4.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosTypeQueue4.setStatus(_A)
_RlQosValueQueue4_Type=Integer32
_RlQosValueQueue4_Object=MibTableColumn
rlQosValueQueue4=_RlQosValueQueue4_Object((1,3,6,1,4,1,171,10,94,89,89,88,22,1,9),_RlQosValueQueue4_Type())
rlQosValueQueue4.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosValueQueue4.setStatus(_A)
_RlQosTypeQueue5_Type=QueueType
_RlQosTypeQueue5_Object=MibTableColumn
rlQosTypeQueue5=_RlQosTypeQueue5_Object((1,3,6,1,4,1,171,10,94,89,89,88,22,1,10),_RlQosTypeQueue5_Type())
rlQosTypeQueue5.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosTypeQueue5.setStatus(_A)
_RlQosValueQueue5_Type=Integer32
_RlQosValueQueue5_Object=MibTableColumn
rlQosValueQueue5=_RlQosValueQueue5_Object((1,3,6,1,4,1,171,10,94,89,89,88,22,1,11),_RlQosValueQueue5_Type())
rlQosValueQueue5.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosValueQueue5.setStatus(_A)
_RlQosTypeQueue6_Type=QueueType
_RlQosTypeQueue6_Object=MibTableColumn
rlQosTypeQueue6=_RlQosTypeQueue6_Object((1,3,6,1,4,1,171,10,94,89,89,88,22,1,12),_RlQosTypeQueue6_Type())
rlQosTypeQueue6.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosTypeQueue6.setStatus(_A)
_RlQosValueQueue6_Type=Integer32
_RlQosValueQueue6_Object=MibTableColumn
rlQosValueQueue6=_RlQosValueQueue6_Object((1,3,6,1,4,1,171,10,94,89,89,88,22,1,13),_RlQosValueQueue6_Type())
rlQosValueQueue6.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosValueQueue6.setStatus(_A)
_RlQosTypeQueue7_Type=QueueType
_RlQosTypeQueue7_Object=MibTableColumn
rlQosTypeQueue7=_RlQosTypeQueue7_Object((1,3,6,1,4,1,171,10,94,89,89,88,22,1,14),_RlQosTypeQueue7_Type())
rlQosTypeQueue7.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosTypeQueue7.setStatus(_A)
_RlQosValueQueue7_Type=Integer32
_RlQosValueQueue7_Object=MibTableColumn
rlQosValueQueue7=_RlQosValueQueue7_Object((1,3,6,1,4,1,171,10,94,89,89,88,22,1,15),_RlQosValueQueue7_Type())
rlQosValueQueue7.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosValueQueue7.setStatus(_A)
_RlQosTypeQueue8_Type=QueueType
_RlQosTypeQueue8_Object=MibTableColumn
rlQosTypeQueue8=_RlQosTypeQueue8_Object((1,3,6,1,4,1,171,10,94,89,89,88,22,1,16),_RlQosTypeQueue8_Type())
rlQosTypeQueue8.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosTypeQueue8.setStatus(_A)
_RlQosValueQueue8_Type=Integer32
_RlQosValueQueue8_Object=MibTableColumn
rlQosValueQueue8=_RlQosValueQueue8_Object((1,3,6,1,4,1,171,10,94,89,89,88,22,1,17),_RlQosValueQueue8_Type())
rlQosValueQueue8.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosValueQueue8.setStatus(_A)
_RlQosQueueProfileStatus_Type=RowStatus
_RlQosQueueProfileStatus_Object=MibTableColumn
rlQosQueueProfileStatus=_RlQosQueueProfileStatus_Object((1,3,6,1,4,1,171,10,94,89,89,88,22,1,18),_RlQosQueueProfileStatus_Type())
rlQosQueueProfileStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosQueueProfileStatus.setStatus(_A)
_RlQosNumOfIfConnections_Type=Integer32
_RlQosNumOfIfConnections_Object=MibTableColumn
rlQosNumOfIfConnections=_RlQosNumOfIfConnections_Object((1,3,6,1,4,1,171,10,94,89,89,88,22,1,19),_RlQosNumOfIfConnections_Type())
rlQosNumOfIfConnections.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosNumOfIfConnections.setStatus(_A)
_RlQosQueueShapeProfileTable_Object=MibTable
rlQosQueueShapeProfileTable=_RlQosQueueShapeProfileTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,23))
if mibBuilder.loadTexts:rlQosQueueShapeProfileTable.setStatus(_A)
_RlQosQueueShapeProfileEntry_Object=MibTableRow
rlQosQueueShapeProfileEntry=_RlQosQueueShapeProfileEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,23,1))
rlQosQueueShapeProfileEntry.setIndexNames((0,_C,_u))
if mibBuilder.loadTexts:rlQosQueueShapeProfileEntry.setStatus(_A)
_RlQosQueueShapeIndex_Type=Integer32
_RlQosQueueShapeIndex_Object=MibTableColumn
rlQosQueueShapeIndex=_RlQosQueueShapeIndex_Object((1,3,6,1,4,1,171,10,94,89,89,88,23,1,1),_RlQosQueueShapeIndex_Type())
rlQosQueueShapeIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosQueueShapeIndex.setStatus(_A)
_RlQosCirQueue1_Type=Integer32
_RlQosCirQueue1_Object=MibTableColumn
rlQosCirQueue1=_RlQosCirQueue1_Object((1,3,6,1,4,1,171,10,94,89,89,88,23,1,2),_RlQosCirQueue1_Type())
rlQosCirQueue1.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosCirQueue1.setStatus(_A)
_RlQosCbsQueue1_Type=Integer32
_RlQosCbsQueue1_Object=MibTableColumn
rlQosCbsQueue1=_RlQosCbsQueue1_Object((1,3,6,1,4,1,171,10,94,89,89,88,23,1,3),_RlQosCbsQueue1_Type())
rlQosCbsQueue1.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosCbsQueue1.setStatus(_A)
_RlQosCirQueue2_Type=Integer32
_RlQosCirQueue2_Object=MibTableColumn
rlQosCirQueue2=_RlQosCirQueue2_Object((1,3,6,1,4,1,171,10,94,89,89,88,23,1,4),_RlQosCirQueue2_Type())
rlQosCirQueue2.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosCirQueue2.setStatus(_A)
_RlQosCbsQueue2_Type=Integer32
_RlQosCbsQueue2_Object=MibTableColumn
rlQosCbsQueue2=_RlQosCbsQueue2_Object((1,3,6,1,4,1,171,10,94,89,89,88,23,1,5),_RlQosCbsQueue2_Type())
rlQosCbsQueue2.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosCbsQueue2.setStatus(_A)
_RlQosCirQueue3_Type=Integer32
_RlQosCirQueue3_Object=MibTableColumn
rlQosCirQueue3=_RlQosCirQueue3_Object((1,3,6,1,4,1,171,10,94,89,89,88,23,1,6),_RlQosCirQueue3_Type())
rlQosCirQueue3.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosCirQueue3.setStatus(_A)
_RlQosCbsQueue3_Type=Integer32
_RlQosCbsQueue3_Object=MibTableColumn
rlQosCbsQueue3=_RlQosCbsQueue3_Object((1,3,6,1,4,1,171,10,94,89,89,88,23,1,7),_RlQosCbsQueue3_Type())
rlQosCbsQueue3.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosCbsQueue3.setStatus(_A)
_RlQosCirQueue4_Type=Integer32
_RlQosCirQueue4_Object=MibTableColumn
rlQosCirQueue4=_RlQosCirQueue4_Object((1,3,6,1,4,1,171,10,94,89,89,88,23,1,8),_RlQosCirQueue4_Type())
rlQosCirQueue4.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosCirQueue4.setStatus(_A)
_RlQosCbsQueue4_Type=Integer32
_RlQosCbsQueue4_Object=MibTableColumn
rlQosCbsQueue4=_RlQosCbsQueue4_Object((1,3,6,1,4,1,171,10,94,89,89,88,23,1,9),_RlQosCbsQueue4_Type())
rlQosCbsQueue4.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosCbsQueue4.setStatus(_A)
_RlQosCirQueue5_Type=Integer32
_RlQosCirQueue5_Object=MibTableColumn
rlQosCirQueue5=_RlQosCirQueue5_Object((1,3,6,1,4,1,171,10,94,89,89,88,23,1,10),_RlQosCirQueue5_Type())
rlQosCirQueue5.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosCirQueue5.setStatus(_A)
_RlQosCbsQueue5_Type=Integer32
_RlQosCbsQueue5_Object=MibTableColumn
rlQosCbsQueue5=_RlQosCbsQueue5_Object((1,3,6,1,4,1,171,10,94,89,89,88,23,1,11),_RlQosCbsQueue5_Type())
rlQosCbsQueue5.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosCbsQueue5.setStatus(_A)
_RlQosCirQueue6_Type=Integer32
_RlQosCirQueue6_Object=MibTableColumn
rlQosCirQueue6=_RlQosCirQueue6_Object((1,3,6,1,4,1,171,10,94,89,89,88,23,1,12),_RlQosCirQueue6_Type())
rlQosCirQueue6.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosCirQueue6.setStatus(_A)
_RlQosCbsQueue6_Type=Integer32
_RlQosCbsQueue6_Object=MibTableColumn
rlQosCbsQueue6=_RlQosCbsQueue6_Object((1,3,6,1,4,1,171,10,94,89,89,88,23,1,13),_RlQosCbsQueue6_Type())
rlQosCbsQueue6.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosCbsQueue6.setStatus(_A)
_RlQosCirQueue7_Type=Integer32
_RlQosCirQueue7_Object=MibTableColumn
rlQosCirQueue7=_RlQosCirQueue7_Object((1,3,6,1,4,1,171,10,94,89,89,88,23,1,14),_RlQosCirQueue7_Type())
rlQosCirQueue7.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosCirQueue7.setStatus(_A)
_RlQosCbsQueue7_Type=Integer32
_RlQosCbsQueue7_Object=MibTableColumn
rlQosCbsQueue7=_RlQosCbsQueue7_Object((1,3,6,1,4,1,171,10,94,89,89,88,23,1,15),_RlQosCbsQueue7_Type())
rlQosCbsQueue7.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosCbsQueue7.setStatus(_A)
_RlQosCirQueue8_Type=Integer32
_RlQosCirQueue8_Object=MibTableColumn
rlQosCirQueue8=_RlQosCirQueue8_Object((1,3,6,1,4,1,171,10,94,89,89,88,23,1,16),_RlQosCirQueue8_Type())
rlQosCirQueue8.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosCirQueue8.setStatus(_A)
_RlQosCbsQueue8_Type=Integer32
_RlQosCbsQueue8_Object=MibTableColumn
rlQosCbsQueue8=_RlQosCbsQueue8_Object((1,3,6,1,4,1,171,10,94,89,89,88,23,1,17),_RlQosCbsQueue8_Type())
rlQosCbsQueue8.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosCbsQueue8.setStatus(_A)
_RlQosQueueShapeProfileStatus_Type=RowStatus
_RlQosQueueShapeProfileStatus_Object=MibTableColumn
rlQosQueueShapeProfileStatus=_RlQosQueueShapeProfileStatus_Object((1,3,6,1,4,1,171,10,94,89,89,88,23,1,18),_RlQosQueueShapeProfileStatus_Type())
rlQosQueueShapeProfileStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosQueueShapeProfileStatus.setStatus(_A)
_RlQosAclCounterTable_Object=MibTable
rlQosAclCounterTable=_RlQosAclCounterTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,24))
if mibBuilder.loadTexts:rlQosAclCounterTable.setStatus(_A)
_RlQosAclCounterEntry_Object=MibTableRow
rlQosAclCounterEntry=_RlQosAclCounterEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,24,1))
rlQosAclCounterEntry.setIndexNames((0,_C,_v),(0,_C,_w),(0,_C,_x))
if mibBuilder.loadTexts:rlQosAclCounterEntry.setStatus(_A)
_RlQosAclCounterInterface_Type=InterfaceIndex
_RlQosAclCounterInterface_Object=MibTableColumn
rlQosAclCounterInterface=_RlQosAclCounterInterface_Object((1,3,6,1,4,1,171,10,94,89,89,88,24,1,1),_RlQosAclCounterInterface_Type())
rlQosAclCounterInterface.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosAclCounterInterface.setStatus(_A)
_RlQosAclCounterAclIndex_Type=Integer32
_RlQosAclCounterAclIndex_Object=MibTableColumn
rlQosAclCounterAclIndex=_RlQosAclCounterAclIndex_Object((1,3,6,1,4,1,171,10,94,89,89,88,24,1,2),_RlQosAclCounterAclIndex_Type())
rlQosAclCounterAclIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosAclCounterAclIndex.setStatus(_A)
_RlQosAclCounterAceIndex_Type=Integer32
_RlQosAclCounterAceIndex_Object=MibTableColumn
rlQosAclCounterAceIndex=_RlQosAclCounterAceIndex_Object((1,3,6,1,4,1,171,10,94,89,89,88,24,1,3),_RlQosAclCounterAceIndex_Type())
rlQosAclCounterAceIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosAclCounterAceIndex.setStatus(_A)
_RlQosAclCounterValue_Type=Counter32
_RlQosAclCounterValue_Object=MibTableColumn
rlQosAclCounterValue=_RlQosAclCounterValue_Object((1,3,6,1,4,1,171,10,94,89,89,88,24,1,4),_RlQosAclCounterValue_Type())
rlQosAclCounterValue.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosAclCounterValue.setStatus(_A)
_RlQosFreeIndexesTable_Object=MibTable
rlQosFreeIndexesTable=_RlQosFreeIndexesTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,25))
if mibBuilder.loadTexts:rlQosFreeIndexesTable.setStatus(_A)
_RlQosFreeIndexesEntry_Object=MibTableRow
rlQosFreeIndexesEntry=_RlQosFreeIndexesEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,25,1))
rlQosFreeIndexesEntry.setIndexNames((0,_C,_y))
if mibBuilder.loadTexts:rlQosFreeIndexesEntry.setStatus(_A)
class _RlQosFreeIndexesTableId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('tuple',1),('offset',2),('ace',3),('acl',4),('class',5),(_z,6),('policer',7),('shaper',8)))
_RlQosFreeIndexesTableId_Type.__name__=_D
_RlQosFreeIndexesTableId_Object=MibTableColumn
rlQosFreeIndexesTableId=_RlQosFreeIndexesTableId_Object((1,3,6,1,4,1,171,10,94,89,89,88,25,1,1),_RlQosFreeIndexesTableId_Type())
rlQosFreeIndexesTableId.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosFreeIndexesTableId.setStatus(_A)
_RlQosFreeIndexesValue_Type=Integer32
_RlQosFreeIndexesValue_Object=MibTableColumn
rlQosFreeIndexesValue=_RlQosFreeIndexesValue_Object((1,3,6,1,4,1,171,10,94,89,89,88,25,1,2),_RlQosFreeIndexesValue_Type())
rlQosFreeIndexesValue.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosFreeIndexesValue.setStatus(_A)
_RlQosNamesToIndexesTable_Object=MibTable
rlQosNamesToIndexesTable=_RlQosNamesToIndexesTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,26))
if mibBuilder.loadTexts:rlQosNamesToIndexesTable.setStatus(_A)
_RlQosNamesToIndexesEntry_Object=MibTableRow
rlQosNamesToIndexesEntry=_RlQosNamesToIndexesEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,26,1))
rlQosNamesToIndexesEntry.setIndexNames((0,_C,_A0),(0,_C,_A1))
if mibBuilder.loadTexts:rlQosNamesToIndexesEntry.setStatus(_A)
class _RlQosNamesToIndexesTableId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('acl',1),('class',2),(_z,3),('policer',4)))
_RlQosNamesToIndexesTableId_Type.__name__=_D
_RlQosNamesToIndexesTableId_Object=MibTableColumn
rlQosNamesToIndexesTableId=_RlQosNamesToIndexesTableId_Object((1,3,6,1,4,1,171,10,94,89,89,88,26,1,1),_RlQosNamesToIndexesTableId_Type())
rlQosNamesToIndexesTableId.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosNamesToIndexesTableId.setStatus(_A)
class _RlQosNamesToIndexesName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlQosNamesToIndexesName_Type.__name__=_H
_RlQosNamesToIndexesName_Object=MibTableColumn
rlQosNamesToIndexesName=_RlQosNamesToIndexesName_Object((1,3,6,1,4,1,171,10,94,89,89,88,26,1,2),_RlQosNamesToIndexesName_Type())
rlQosNamesToIndexesName.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosNamesToIndexesName.setStatus(_A)
_RlQosNamesToIndexesValue_Type=Integer32
_RlQosNamesToIndexesValue_Object=MibTableColumn
rlQosNamesToIndexesValue=_RlQosNamesToIndexesValue_Object((1,3,6,1,4,1,171,10,94,89,89,88,26,1,3),_RlQosNamesToIndexesValue_Type())
rlQosNamesToIndexesValue.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosNamesToIndexesValue.setStatus(_A)
_RlQosStackControlQueue_Type=Integer32
_RlQosStackControlQueue_Object=MibScalar
rlQosStackControlQueue=_RlQosStackControlQueue_Object((1,3,6,1,4,1,171,10,94,89,89,88,27),_RlQosStackControlQueue_Type())
rlQosStackControlQueue.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosStackControlQueue.setStatus(_A)
_RlQosStackControlCos_Type=Integer32
_RlQosStackControlCos_Object=MibScalar
rlQosStackControlCos=_RlQosStackControlCos_Object((1,3,6,1,4,1,171,10,94,89,89,88,28),_RlQosStackControlCos_Type())
rlQosStackControlCos.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosStackControlCos.setStatus(_A)
_RlQosCosQueueDefaultMapTable_Object=MibTable
rlQosCosQueueDefaultMapTable=_RlQosCosQueueDefaultMapTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,29))
if mibBuilder.loadTexts:rlQosCosQueueDefaultMapTable.setStatus(_A)
_RlQosCosQueueDefaultMapEntry_Object=MibTableRow
rlQosCosQueueDefaultMapEntry=_RlQosCosQueueDefaultMapEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,29,1))
rlQosCosQueueDefaultMapEntry.setIndexNames((0,_C,_A2))
if mibBuilder.loadTexts:rlQosCosQueueDefaultMapEntry.setStatus(_A)
class _RlQosCosQueueDefaultMapVpt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RlQosCosQueueDefaultMapVpt_Type.__name__=_D
_RlQosCosQueueDefaultMapVpt_Object=MibTableColumn
rlQosCosQueueDefaultMapVpt=_RlQosCosQueueDefaultMapVpt_Object((1,3,6,1,4,1,171,10,94,89,89,88,29,1,1),_RlQosCosQueueDefaultMapVpt_Type())
rlQosCosQueueDefaultMapVpt.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosCosQueueDefaultMapVpt.setStatus(_A)
class _RlQosCosQueueDefaultMapQueueId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RlQosCosQueueDefaultMapQueueId_Type.__name__=_D
_RlQosCosQueueDefaultMapQueueId_Object=MibTableColumn
rlQosCosQueueDefaultMapQueueId=_RlQosCosQueueDefaultMapQueueId_Object((1,3,6,1,4,1,171,10,94,89,89,88,29,1,2),_RlQosCosQueueDefaultMapQueueId_Type())
rlQosCosQueueDefaultMapQueueId.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosCosQueueDefaultMapQueueId.setStatus(_A)
_RlQosPredefBlockAclTable_Object=MibTable
rlQosPredefBlockAclTable=_RlQosPredefBlockAclTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,30))
if mibBuilder.loadTexts:rlQosPredefBlockAclTable.setStatus(_A)
_RlQosPredefBlockAclEntry_Object=MibTableRow
rlQosPredefBlockAclEntry=_RlQosPredefBlockAclEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,30,1))
rlQosPredefBlockAclEntry.setIndexNames((0,_C,_A3),(0,_C,_A4))
if mibBuilder.loadTexts:rlQosPredefBlockAclEntry.setStatus(_A)
_RlQosPredefBlockAclIfIndex_Type=InterfaceIndex
_RlQosPredefBlockAclIfIndex_Object=MibTableColumn
rlQosPredefBlockAclIfIndex=_RlQosPredefBlockAclIfIndex_Object((1,3,6,1,4,1,171,10,94,89,89,88,30,1,1),_RlQosPredefBlockAclIfIndex_Type())
rlQosPredefBlockAclIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosPredefBlockAclIfIndex.setStatus(_A)
_RlQosPredefBlockAclIfType_Type=InterfaceType
_RlQosPredefBlockAclIfType_Object=MibTableColumn
rlQosPredefBlockAclIfType=_RlQosPredefBlockAclIfType_Object((1,3,6,1,4,1,171,10,94,89,89,88,30,1,2),_RlQosPredefBlockAclIfType_Type())
rlQosPredefBlockAclIfType.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosPredefBlockAclIfType.setStatus(_A)
class _RlQosPredefBlockAclMask_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1));fixedLength=1
_RlQosPredefBlockAclMask_Type.__name__=_N
_RlQosPredefBlockAclMask_Object=MibTableColumn
rlQosPredefBlockAclMask=_RlQosPredefBlockAclMask_Object((1,3,6,1,4,1,171,10,94,89,89,88,30,1,3),_RlQosPredefBlockAclMask_Type())
rlQosPredefBlockAclMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosPredefBlockAclMask.setStatus(_A)
_RlQosPredefBlockAclStatus_Type=RowStatus
_RlQosPredefBlockAclStatus_Object=MibTableColumn
rlQosPredefBlockAclStatus=_RlQosPredefBlockAclStatus_Object((1,3,6,1,4,1,171,10,94,89,89,88,30,1,4),_RlQosPredefBlockAclStatus_Type())
rlQosPredefBlockAclStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosPredefBlockAclStatus.setStatus(_A)
_RlQosAceTidxTable_Object=MibTable
rlQosAceTidxTable=_RlQosAceTidxTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,31))
if mibBuilder.loadTexts:rlQosAceTidxTable.setStatus(_A)
_RlQosAceTidxEntry_Object=MibTableRow
rlQosAceTidxEntry=_RlQosAceTidxEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,31,1))
rlQosAceTidxEntry.setIndexNames((0,_C,_A5),(0,_C,_A6))
if mibBuilder.loadTexts:rlQosAceTidxEntry.setStatus(_A)
_RlQosAceTidxAclIndex_Type=Integer32
_RlQosAceTidxAclIndex_Object=MibTableColumn
rlQosAceTidxAclIndex=_RlQosAceTidxAclIndex_Object((1,3,6,1,4,1,171,10,94,89,89,88,31,1,1),_RlQosAceTidxAclIndex_Type())
rlQosAceTidxAclIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosAceTidxAclIndex.setStatus(_A)
_RlQosAceTidxIndex_Type=Integer32
_RlQosAceTidxIndex_Object=MibTableColumn
rlQosAceTidxIndex=_RlQosAceTidxIndex_Object((1,3,6,1,4,1,171,10,94,89,89,88,31,1,2),_RlQosAceTidxIndex_Type())
rlQosAceTidxIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosAceTidxIndex.setStatus(_A)
_RlQosAceTidxAction_Type=AceActionType
_RlQosAceTidxAction_Object=MibTableColumn
rlQosAceTidxAction=_RlQosAceTidxAction_Object((1,3,6,1,4,1,171,10,94,89,89,88,31,1,3),_RlQosAceTidxAction_Type())
rlQosAceTidxAction.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAceTidxAction.setStatus(_A)
_RlQosAceTidxType_Type=AceObjectType
_RlQosAceTidxType_Object=MibTableColumn
rlQosAceTidxType=_RlQosAceTidxType_Object((1,3,6,1,4,1,171,10,94,89,89,88,31,1,4),_RlQosAceTidxType_Type())
rlQosAceTidxType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAceTidxType.setStatus(_A)
_RlQosAceTidxTuple1_Type=Integer32
_RlQosAceTidxTuple1_Object=MibTableColumn
rlQosAceTidxTuple1=_RlQosAceTidxTuple1_Object((1,3,6,1,4,1,171,10,94,89,89,88,31,1,5),_RlQosAceTidxTuple1_Type())
rlQosAceTidxTuple1.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAceTidxTuple1.setStatus(_A)
_RlQosAceTidxTuple2_Type=Integer32
_RlQosAceTidxTuple2_Object=MibTableColumn
rlQosAceTidxTuple2=_RlQosAceTidxTuple2_Object((1,3,6,1,4,1,171,10,94,89,89,88,31,1,6),_RlQosAceTidxTuple2_Type())
rlQosAceTidxTuple2.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAceTidxTuple2.setStatus(_A)
_RlQosAceTidxTuple3_Type=Integer32
_RlQosAceTidxTuple3_Object=MibTableColumn
rlQosAceTidxTuple3=_RlQosAceTidxTuple3_Object((1,3,6,1,4,1,171,10,94,89,89,88,31,1,7),_RlQosAceTidxTuple3_Type())
rlQosAceTidxTuple3.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAceTidxTuple3.setStatus(_A)
_RlQosAceTidxTuple4_Type=Integer32
_RlQosAceTidxTuple4_Object=MibTableColumn
rlQosAceTidxTuple4=_RlQosAceTidxTuple4_Object((1,3,6,1,4,1,171,10,94,89,89,88,31,1,8),_RlQosAceTidxTuple4_Type())
rlQosAceTidxTuple4.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAceTidxTuple4.setStatus(_A)
_RlQosAceTidxTuple5_Type=Integer32
_RlQosAceTidxTuple5_Object=MibTableColumn
rlQosAceTidxTuple5=_RlQosAceTidxTuple5_Object((1,3,6,1,4,1,171,10,94,89,89,88,31,1,9),_RlQosAceTidxTuple5_Type())
rlQosAceTidxTuple5.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAceTidxTuple5.setStatus(_A)
_RlQosAceTidxTuple6_Type=Integer32
_RlQosAceTidxTuple6_Object=MibTableColumn
rlQosAceTidxTuple6=_RlQosAceTidxTuple6_Object((1,3,6,1,4,1,171,10,94,89,89,88,31,1,10),_RlQosAceTidxTuple6_Type())
rlQosAceTidxTuple6.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAceTidxTuple6.setStatus(_A)
_RlQosAceTidxTuple7_Type=Integer32
_RlQosAceTidxTuple7_Object=MibTableColumn
rlQosAceTidxTuple7=_RlQosAceTidxTuple7_Object((1,3,6,1,4,1,171,10,94,89,89,88,31,1,11),_RlQosAceTidxTuple7_Type())
rlQosAceTidxTuple7.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAceTidxTuple7.setStatus(_A)
_RlQosAceTidxTuple8_Type=Integer32
_RlQosAceTidxTuple8_Object=MibTableColumn
rlQosAceTidxTuple8=_RlQosAceTidxTuple8_Object((1,3,6,1,4,1,171,10,94,89,89,88,31,1,12),_RlQosAceTidxTuple8_Type())
rlQosAceTidxTuple8.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAceTidxTuple8.setStatus(_A)
_RlQosAceTidxAccount_Type=BinaryStatus
_RlQosAceTidxAccount_Object=MibTableColumn
rlQosAceTidxAccount=_RlQosAceTidxAccount_Object((1,3,6,1,4,1,171,10,94,89,89,88,31,1,13),_RlQosAceTidxAccount_Type())
rlQosAceTidxAccount.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAceTidxAccount.setStatus(_A)
_RlQosAceTidxStatus_Type=RowStatus
_RlQosAceTidxStatus_Object=MibTableColumn
rlQosAceTidxStatus=_RlQosAceTidxStatus_Object((1,3,6,1,4,1,171,10,94,89,89,88,31,1,14),_RlQosAceTidxStatus_Type())
rlQosAceTidxStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAceTidxStatus.setStatus(_A)
class _RlQosAceTidxTimeRange_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlQosAceTidxTimeRange_Type.__name__=_H
_RlQosAceTidxTimeRange_Object=MibTableColumn
rlQosAceTidxTimeRange=_RlQosAceTidxTimeRange_Object((1,3,6,1,4,1,171,10,94,89,89,88,31,1,15),_RlQosAceTidxTimeRange_Type())
rlQosAceTidxTimeRange.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosAceTidxTimeRange.setStatus(_A)
_RlQosAceTidxTimeRangeIsActive_Type=TruthValue
_RlQosAceTidxTimeRangeIsActive_Object=MibTableColumn
rlQosAceTidxTimeRangeIsActive=_RlQosAceTidxTimeRangeIsActive_Object((1,3,6,1,4,1,171,10,94,89,89,88,31,1,16),_RlQosAceTidxTimeRangeIsActive_Type())
rlQosAceTidxTimeRangeIsActive.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosAceTidxTimeRangeIsActive.setStatus(_A)
_RlQosMibVersion_Type=Integer32
_RlQosMibVersion_Object=MibScalar
rlQosMibVersion=_RlQosMibVersion_Object((1,3,6,1,4,1,171,10,94,89,89,88,32),_RlQosMibVersion_Type())
rlQosMibVersion.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosMibVersion.setStatus(_A)
_RlQosDscpQueueDefaultMapTable_Object=MibTable
rlQosDscpQueueDefaultMapTable=_RlQosDscpQueueDefaultMapTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,33))
if mibBuilder.loadTexts:rlQosDscpQueueDefaultMapTable.setStatus(_A)
_RlQosDscpQueueDefaultMapEntry_Object=MibTableRow
rlQosDscpQueueDefaultMapEntry=_RlQosDscpQueueDefaultMapEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,33,1))
rlQosDscpQueueDefaultMapEntry.setIndexNames((0,_C,_A7))
if mibBuilder.loadTexts:rlQosDscpQueueDefaultMapEntry.setStatus(_A)
class _RlQosDscpQueueDefaultMapDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RlQosDscpQueueDefaultMapDscp_Type.__name__=_D
_RlQosDscpQueueDefaultMapDscp_Object=MibTableColumn
rlQosDscpQueueDefaultMapDscp=_RlQosDscpQueueDefaultMapDscp_Object((1,3,6,1,4,1,171,10,94,89,89,88,33,1,1),_RlQosDscpQueueDefaultMapDscp_Type())
rlQosDscpQueueDefaultMapDscp.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosDscpQueueDefaultMapDscp.setStatus(_A)
class _RlQosDscpQueueDefaultMapQueueId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RlQosDscpQueueDefaultMapQueueId_Type.__name__=_D
_RlQosDscpQueueDefaultMapQueueId_Object=MibTableColumn
rlQosDscpQueueDefaultMapQueueId=_RlQosDscpQueueDefaultMapQueueId_Object((1,3,6,1,4,1,171,10,94,89,89,88,33,1,2),_RlQosDscpQueueDefaultMapQueueId_Type())
rlQosDscpQueueDefaultMapQueueId.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosDscpQueueDefaultMapQueueId.setStatus(_A)
_RlQosDscpToDpTable_Object=MibTable
rlQosDscpToDpTable=_RlQosDscpToDpTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,34))
if mibBuilder.loadTexts:rlQosDscpToDpTable.setStatus(_A)
_RlQosDscpToDpEntry_Object=MibTableRow
rlQosDscpToDpEntry=_RlQosDscpToDpEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,34,1))
rlQosDscpToDpEntry.setIndexNames((0,_C,_A8))
if mibBuilder.loadTexts:rlQosDscpToDpEntry.setStatus(_A)
class _RlQosDscp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RlQosDscp_Type.__name__=_D
_RlQosDscp_Object=MibTableColumn
rlQosDscp=_RlQosDscp_Object((1,3,6,1,4,1,171,10,94,89,89,88,34,1,1),_RlQosDscp_Type())
rlQosDscp.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosDscp.setStatus(_A)
class _RlQosDp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_RlQosDp_Type.__name__=_D
_RlQosDp_Object=MibTableColumn
rlQosDp=_RlQosDp_Object((1,3,6,1,4,1,171,10,94,89,89,88,34,1,2),_RlQosDp_Type())
rlQosDp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlQosDp.setStatus(_A)
_RlQosStatistics_ObjectIdentity=ObjectIdentity
rlQosStatistics=_RlQosStatistics_ObjectIdentity((1,3,6,1,4,1,171,10,94,89,89,88,35))
_RlQosPortPolicyStatisticsTable_Object=MibTable
rlQosPortPolicyStatisticsTable=_RlQosPortPolicyStatisticsTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,1))
if mibBuilder.loadTexts:rlQosPortPolicyStatisticsTable.setStatus(_A)
_RlQosPortPolicyStatisticsEntry_Object=MibTableRow
rlQosPortPolicyStatisticsEntry=_RlQosPortPolicyStatisticsEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,1,1))
rlQosPortPolicyStatisticsEntry.setIndexNames((0,_C,_M),(0,_C,_T),(0,_C,_A9))
if mibBuilder.loadTexts:rlQosPortPolicyStatisticsEntry.setStatus(_A)
_RlQosPortPolicyStatisticsCntrType_Type=StatisticsCntrType
_RlQosPortPolicyStatisticsCntrType_Object=MibTableColumn
rlQosPortPolicyStatisticsCntrType=_RlQosPortPolicyStatisticsCntrType_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,1,1,1),_RlQosPortPolicyStatisticsCntrType_Type())
rlQosPortPolicyStatisticsCntrType.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosPortPolicyStatisticsCntrType.setStatus(_A)
_RlQosPortPolicyStatisticsCntrNumOfBits_Type=StatisticsCntrNumOfBitsType
_RlQosPortPolicyStatisticsCntrNumOfBits_Object=MibTableColumn
rlQosPortPolicyStatisticsCntrNumOfBits=_RlQosPortPolicyStatisticsCntrNumOfBits_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,1,1,2),_RlQosPortPolicyStatisticsCntrNumOfBits_Type())
rlQosPortPolicyStatisticsCntrNumOfBits.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosPortPolicyStatisticsCntrNumOfBits.setStatus(_A)
class _RlQosPortPolicyStatisticsEnableCounting_Type(TruthValue):defaultValue=2
_RlQosPortPolicyStatisticsEnableCounting_Type.__name__=_U
_RlQosPortPolicyStatisticsEnableCounting_Object=MibTableColumn
rlQosPortPolicyStatisticsEnableCounting=_RlQosPortPolicyStatisticsEnableCounting_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,1,1,3),_RlQosPortPolicyStatisticsEnableCounting_Type())
rlQosPortPolicyStatisticsEnableCounting.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosPortPolicyStatisticsEnableCounting.setStatus(_A)
_RlQosPortPolicyStatisticsCounterValue_Type=Counter64
_RlQosPortPolicyStatisticsCounterValue_Object=MibTableColumn
rlQosPortPolicyStatisticsCounterValue=_RlQosPortPolicyStatisticsCounterValue_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,1,1,4),_RlQosPortPolicyStatisticsCounterValue_Type())
rlQosPortPolicyStatisticsCounterValue.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosPortPolicyStatisticsCounterValue.setStatus(_A)
_RlQosSinglePolicerStatisticsTable_Object=MibTable
rlQosSinglePolicerStatisticsTable=_RlQosSinglePolicerStatisticsTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,2))
if mibBuilder.loadTexts:rlQosSinglePolicerStatisticsTable.setStatus(_A)
_RlQosSinglePolicerStatisticsEntry_Object=MibTableRow
rlQosSinglePolicerStatisticsEntry=_RlQosSinglePolicerStatisticsEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,2,1))
rlQosSinglePolicerStatisticsEntry.setIndexNames((0,_C,_M),(0,_C,_L))
if mibBuilder.loadTexts:rlQosSinglePolicerStatisticsEntry.setStatus(_A)
_RlQosSinglePolicerStatisticsInProfileCounterValue_Type=Counter64
_RlQosSinglePolicerStatisticsInProfileCounterValue_Object=MibTableColumn
rlQosSinglePolicerStatisticsInProfileCounterValue=_RlQosSinglePolicerStatisticsInProfileCounterValue_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,2,1,1),_RlQosSinglePolicerStatisticsInProfileCounterValue_Type())
rlQosSinglePolicerStatisticsInProfileCounterValue.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosSinglePolicerStatisticsInProfileCounterValue.setStatus(_A)
_RlQosSinglePolicerStatisticsInProfileCntrNumOfBits_Type=StatisticsCntrNumOfBitsType
_RlQosSinglePolicerStatisticsInProfileCntrNumOfBits_Object=MibTableColumn
rlQosSinglePolicerStatisticsInProfileCntrNumOfBits=_RlQosSinglePolicerStatisticsInProfileCntrNumOfBits_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,2,1,2),_RlQosSinglePolicerStatisticsInProfileCntrNumOfBits_Type())
rlQosSinglePolicerStatisticsInProfileCntrNumOfBits.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosSinglePolicerStatisticsInProfileCntrNumOfBits.setStatus(_A)
_RlQosSinglePolicerStatisticsOutProfileCounterValue_Type=Counter64
_RlQosSinglePolicerStatisticsOutProfileCounterValue_Object=MibTableColumn
rlQosSinglePolicerStatisticsOutProfileCounterValue=_RlQosSinglePolicerStatisticsOutProfileCounterValue_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,2,1,3),_RlQosSinglePolicerStatisticsOutProfileCounterValue_Type())
rlQosSinglePolicerStatisticsOutProfileCounterValue.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosSinglePolicerStatisticsOutProfileCounterValue.setStatus(_A)
_RlQosSinglePolicerStatisticsOutProfileCntrNumOfBits_Type=StatisticsCntrNumOfBitsType
_RlQosSinglePolicerStatisticsOutProfileCntrNumOfBits_Object=MibTableColumn
rlQosSinglePolicerStatisticsOutProfileCntrNumOfBits=_RlQosSinglePolicerStatisticsOutProfileCntrNumOfBits_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,2,1,4),_RlQosSinglePolicerStatisticsOutProfileCntrNumOfBits_Type())
rlQosSinglePolicerStatisticsOutProfileCntrNumOfBits.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosSinglePolicerStatisticsOutProfileCntrNumOfBits.setStatus(_A)
_RlQosSinglePolicerStatisticsStatus_Type=RowStatus
_RlQosSinglePolicerStatisticsStatus_Object=MibTableColumn
rlQosSinglePolicerStatisticsStatus=_RlQosSinglePolicerStatisticsStatus_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,2,1,5),_RlQosSinglePolicerStatisticsStatus_Type())
rlQosSinglePolicerStatisticsStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosSinglePolicerStatisticsStatus.setStatus(_A)
_RlQosAggregatePolicerStatisticsTable_Object=MibTable
rlQosAggregatePolicerStatisticsTable=_RlQosAggregatePolicerStatisticsTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,3))
if mibBuilder.loadTexts:rlQosAggregatePolicerStatisticsTable.setStatus(_A)
_RlQosAggregatePolicerStatisticsEntry_Object=MibTableRow
rlQosAggregatePolicerStatisticsEntry=_RlQosAggregatePolicerStatisticsEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,3,1))
rlQosAggregatePolicerStatisticsEntry.setIndexNames((0,_C,_L))
if mibBuilder.loadTexts:rlQosAggregatePolicerStatisticsEntry.setStatus(_A)
_RlQosAggregatePolicerStatisticsInProfileCounterValue_Type=Counter64
_RlQosAggregatePolicerStatisticsInProfileCounterValue_Object=MibTableColumn
rlQosAggregatePolicerStatisticsInProfileCounterValue=_RlQosAggregatePolicerStatisticsInProfileCounterValue_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,3,1,1),_RlQosAggregatePolicerStatisticsInProfileCounterValue_Type())
rlQosAggregatePolicerStatisticsInProfileCounterValue.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosAggregatePolicerStatisticsInProfileCounterValue.setStatus(_A)
_RlQosAggregatePolicerStatisticsInProfileCntrNumOfBits_Type=StatisticsCntrNumOfBitsType
_RlQosAggregatePolicerStatisticsInProfileCntrNumOfBits_Object=MibTableColumn
rlQosAggregatePolicerStatisticsInProfileCntrNumOfBits=_RlQosAggregatePolicerStatisticsInProfileCntrNumOfBits_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,3,1,2),_RlQosAggregatePolicerStatisticsInProfileCntrNumOfBits_Type())
rlQosAggregatePolicerStatisticsInProfileCntrNumOfBits.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosAggregatePolicerStatisticsInProfileCntrNumOfBits.setStatus(_A)
_RlQosAggregatePolicerStatisticsOutProfileCounterValue_Type=Counter64
_RlQosAggregatePolicerStatisticsOutProfileCounterValue_Object=MibTableColumn
rlQosAggregatePolicerStatisticsOutProfileCounterValue=_RlQosAggregatePolicerStatisticsOutProfileCounterValue_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,3,1,3),_RlQosAggregatePolicerStatisticsOutProfileCounterValue_Type())
rlQosAggregatePolicerStatisticsOutProfileCounterValue.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosAggregatePolicerStatisticsOutProfileCounterValue.setStatus(_A)
_RlQosAggregatePolicerStatisticsOutProfileCntrNumOfBits_Type=StatisticsCntrNumOfBitsType
_RlQosAggregatePolicerStatisticsOutProfileCntrNumOfBits_Object=MibTableColumn
rlQosAggregatePolicerStatisticsOutProfileCntrNumOfBits=_RlQosAggregatePolicerStatisticsOutProfileCntrNumOfBits_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,3,1,4),_RlQosAggregatePolicerStatisticsOutProfileCntrNumOfBits_Type())
rlQosAggregatePolicerStatisticsOutProfileCntrNumOfBits.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosAggregatePolicerStatisticsOutProfileCntrNumOfBits.setStatus(_A)
_RlQosAggregatePolicerStatisticsStatus_Type=RowStatus
_RlQosAggregatePolicerStatisticsStatus_Object=MibTableColumn
rlQosAggregatePolicerStatisticsStatus=_RlQosAggregatePolicerStatisticsStatus_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,3,1,5),_RlQosAggregatePolicerStatisticsStatus_Type())
rlQosAggregatePolicerStatisticsStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosAggregatePolicerStatisticsStatus.setStatus(_A)
_RlQosOutQueueStatisticsTable_Object=MibTable
rlQosOutQueueStatisticsTable=_RlQosOutQueueStatisticsTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,4))
if mibBuilder.loadTexts:rlQosOutQueueStatisticsTable.setStatus(_A)
_RlQosOutQueueStatisticsEntry_Object=MibTableRow
rlQosOutQueueStatisticsEntry=_RlQosOutQueueStatisticsEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,4,1))
rlQosOutQueueStatisticsEntry.setIndexNames((0,_C,_AA))
if mibBuilder.loadTexts:rlQosOutQueueStatisticsEntry.setStatus(_A)
_RlQosOutQueueStatisticsCountrID_Type=Integer32
_RlQosOutQueueStatisticsCountrID_Object=MibTableColumn
rlQosOutQueueStatisticsCountrID=_RlQosOutQueueStatisticsCountrID_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,4,1,1),_RlQosOutQueueStatisticsCountrID_Type())
rlQosOutQueueStatisticsCountrID.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosOutQueueStatisticsCountrID.setStatus(_A)
_RlQosOutQueueStatisticsIfIndexList_Type=PortList
_RlQosOutQueueStatisticsIfIndexList_Object=MibTableColumn
rlQosOutQueueStatisticsIfIndexList=_RlQosOutQueueStatisticsIfIndexList_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,4,1,2),_RlQosOutQueueStatisticsIfIndexList_Type())
rlQosOutQueueStatisticsIfIndexList.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosOutQueueStatisticsIfIndexList.setStatus(_A)
_RlQosOutQueueStatisticsPortAll_Type=TruthValue
_RlQosOutQueueStatisticsPortAll_Object=MibTableColumn
rlQosOutQueueStatisticsPortAll=_RlQosOutQueueStatisticsPortAll_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,4,1,3),_RlQosOutQueueStatisticsPortAll_Type())
rlQosOutQueueStatisticsPortAll.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosOutQueueStatisticsPortAll.setStatus(_A)
_RlQosOutQueueStatisticsVlan_Type=Integer32
_RlQosOutQueueStatisticsVlan_Object=MibTableColumn
rlQosOutQueueStatisticsVlan=_RlQosOutQueueStatisticsVlan_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,4,1,4),_RlQosOutQueueStatisticsVlan_Type())
rlQosOutQueueStatisticsVlan.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosOutQueueStatisticsVlan.setStatus(_A)
_RlQosOutQueueStatisticsVlanAll_Type=TruthValue
_RlQosOutQueueStatisticsVlanAll_Object=MibTableColumn
rlQosOutQueueStatisticsVlanAll=_RlQosOutQueueStatisticsVlanAll_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,4,1,5),_RlQosOutQueueStatisticsVlanAll_Type())
rlQosOutQueueStatisticsVlanAll.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosOutQueueStatisticsVlanAll.setStatus(_A)
class _RlQosOutQueueStatisticsQueue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RlQosOutQueueStatisticsQueue_Type.__name__=_D
_RlQosOutQueueStatisticsQueue_Object=MibTableColumn
rlQosOutQueueStatisticsQueue=_RlQosOutQueueStatisticsQueue_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,4,1,6),_RlQosOutQueueStatisticsQueue_Type())
rlQosOutQueueStatisticsQueue.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosOutQueueStatisticsQueue.setStatus(_A)
_RlQosOutQueueStatisticsQueueAll_Type=TruthValue
_RlQosOutQueueStatisticsQueueAll_Object=MibTableColumn
rlQosOutQueueStatisticsQueueAll=_RlQosOutQueueStatisticsQueueAll_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,4,1,7),_RlQosOutQueueStatisticsQueueAll_Type())
rlQosOutQueueStatisticsQueueAll.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosOutQueueStatisticsQueueAll.setStatus(_A)
_RlQosOutQueueStatisticsDP_Type=StatisticsDPType
_RlQosOutQueueStatisticsDP_Object=MibTableColumn
rlQosOutQueueStatisticsDP=_RlQosOutQueueStatisticsDP_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,4,1,8),_RlQosOutQueueStatisticsDP_Type())
rlQosOutQueueStatisticsDP.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosOutQueueStatisticsDP.setStatus(_A)
_RlQosOutQueueStatisticsDPAll_Type=TruthValue
_RlQosOutQueueStatisticsDPAll_Object=MibTableColumn
rlQosOutQueueStatisticsDPAll=_RlQosOutQueueStatisticsDPAll_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,4,1,9),_RlQosOutQueueStatisticsDPAll_Type())
rlQosOutQueueStatisticsDPAll.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosOutQueueStatisticsDPAll.setStatus(_A)
_RlQosOutQueueStatisticsCounterTailDropValue_Type=Counter64
_RlQosOutQueueStatisticsCounterTailDropValue_Object=MibTableColumn
rlQosOutQueueStatisticsCounterTailDropValue=_RlQosOutQueueStatisticsCounterTailDropValue_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,4,1,10),_RlQosOutQueueStatisticsCounterTailDropValue_Type())
rlQosOutQueueStatisticsCounterTailDropValue.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosOutQueueStatisticsCounterTailDropValue.setStatus(_A)
_RlQosOutQueueStatisticsCounterAllValue_Type=Counter64
_RlQosOutQueueStatisticsCounterAllValue_Object=MibTableColumn
rlQosOutQueueStatisticsCounterAllValue=_RlQosOutQueueStatisticsCounterAllValue_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,4,1,11),_RlQosOutQueueStatisticsCounterAllValue_Type())
rlQosOutQueueStatisticsCounterAllValue.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosOutQueueStatisticsCounterAllValue.setStatus(_A)
_RlQosOutQueueStatisticsCntrNumOfBits_Type=StatisticsCntrNumOfBitsType
_RlQosOutQueueStatisticsCntrNumOfBits_Object=MibTableColumn
rlQosOutQueueStatisticsCntrNumOfBits=_RlQosOutQueueStatisticsCntrNumOfBits_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,4,1,12),_RlQosOutQueueStatisticsCntrNumOfBits_Type())
rlQosOutQueueStatisticsCntrNumOfBits.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosOutQueueStatisticsCntrNumOfBits.setStatus(_A)
_RlQosOutQueueStatisticsStatus_Type=RowStatus
_RlQosOutQueueStatisticsStatus_Object=MibTableColumn
rlQosOutQueueStatisticsStatus=_RlQosOutQueueStatisticsStatus_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,4,1,13),_RlQosOutQueueStatisticsStatus_Type())
rlQosOutQueueStatisticsStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosOutQueueStatisticsStatus.setStatus(_A)
_RlQosGlobalStatisticsCntrsTable_Object=MibTable
rlQosGlobalStatisticsCntrsTable=_RlQosGlobalStatisticsCntrsTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,5))
if mibBuilder.loadTexts:rlQosGlobalStatisticsCntrsTable.setStatus(_A)
_RlQosGlobalStatisticsCntrsEntry_Object=MibTableRow
rlQosGlobalStatisticsCntrsEntry=_RlQosGlobalStatisticsCntrsEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,5,1))
rlQosGlobalStatisticsCntrsEntry.setIndexNames((0,_C,_AB))
if mibBuilder.loadTexts:rlQosGlobalStatisticsCntrsEntry.setStatus(_A)
_RlQosGlobalStatisticsCntrsType_Type=StatisticsCntrType
_RlQosGlobalStatisticsCntrsType_Object=MibTableColumn
rlQosGlobalStatisticsCntrsType=_RlQosGlobalStatisticsCntrsType_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,5,1,1),_RlQosGlobalStatisticsCntrsType_Type())
rlQosGlobalStatisticsCntrsType.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosGlobalStatisticsCntrsType.setStatus(_A)
_RlQosGlobalStatisticsCntrsNumOfBits_Type=StatisticsCntrNumOfBitsType
_RlQosGlobalStatisticsCntrsNumOfBits_Object=MibTableColumn
rlQosGlobalStatisticsCntrsNumOfBits=_RlQosGlobalStatisticsCntrsNumOfBits_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,5,1,2),_RlQosGlobalStatisticsCntrsNumOfBits_Type())
rlQosGlobalStatisticsCntrsNumOfBits.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosGlobalStatisticsCntrsNumOfBits.setStatus(_A)
_RlQosGlobalStatisticsCntrsCounterValue_Type=Counter64
_RlQosGlobalStatisticsCntrsCounterValue_Object=MibTableColumn
rlQosGlobalStatisticsCntrsCounterValue=_RlQosGlobalStatisticsCntrsCounterValue_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,5,1,3),_RlQosGlobalStatisticsCntrsCounterValue_Type())
rlQosGlobalStatisticsCntrsCounterValue.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosGlobalStatisticsCntrsCounterValue.setStatus(_A)
_RlQosGlobalStatisticsStatus_Type=RowStatus
_RlQosGlobalStatisticsStatus_Object=MibTableColumn
rlQosGlobalStatisticsStatus=_RlQosGlobalStatisticsStatus_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,5,1,4),_RlQosGlobalStatisticsStatus_Type())
rlQosGlobalStatisticsStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosGlobalStatisticsStatus.setStatus(_A)
_RlQosClearCounters_Type=Integer32
_RlQosClearCounters_Object=MibScalar
rlQosClearCounters=_RlQosClearCounters_Object((1,3,6,1,4,1,171,10,94,89,89,88,35,6),_RlQosClearCounters_Type())
rlQosClearCounters.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosClearCounters.setStatus(_A)
_RlQosClassifierUtilization_ObjectIdentity=ObjectIdentity
rlQosClassifierUtilization=_RlQosClassifierUtilization_ObjectIdentity((1,3,6,1,4,1,171,10,94,89,89,88,36))
_RlQosClassifierUtilizationTable_Object=MibTable
rlQosClassifierUtilizationTable=_RlQosClassifierUtilizationTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,36,1))
if mibBuilder.loadTexts:rlQosClassifierUtilizationTable.setStatus(_A)
_RlQosClassifierUtilizationEntry_Object=MibTableRow
rlQosClassifierUtilizationEntry=_RlQosClassifierUtilizationEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,36,1,1))
rlQosClassifierUtilizationEntry.setIndexNames((0,_C,_AC))
if mibBuilder.loadTexts:rlQosClassifierUtilizationEntry.setStatus(_A)
class _RlQosClassifierUtilizationUnitId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RlQosClassifierUtilizationUnitId_Type.__name__=_K
_RlQosClassifierUtilizationUnitId_Object=MibTableColumn
rlQosClassifierUtilizationUnitId=_RlQosClassifierUtilizationUnitId_Object((1,3,6,1,4,1,171,10,94,89,89,88,36,1,1,1),_RlQosClassifierUtilizationUnitId_Type())
rlQosClassifierUtilizationUnitId.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosClassifierUtilizationUnitId.setStatus(_A)
class _RlQosClassifierUtilizationPercent_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RlQosClassifierUtilizationPercent_Type.__name__=_K
_RlQosClassifierUtilizationPercent_Object=MibTableColumn
rlQosClassifierUtilizationPercent=_RlQosClassifierUtilizationPercent_Object((1,3,6,1,4,1,171,10,94,89,89,88,36,1,1,2),_RlQosClassifierUtilizationPercent_Type())
rlQosClassifierUtilizationPercent.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosClassifierUtilizationPercent.setStatus(_A)
class _RlQosClassifierUtilizationRulesNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RlQosClassifierUtilizationRulesNumber_Type.__name__=_K
_RlQosClassifierUtilizationRulesNumber_Object=MibTableColumn
rlQosClassifierUtilizationRulesNumber=_RlQosClassifierUtilizationRulesNumber_Object((1,3,6,1,4,1,171,10,94,89,89,88,36,1,1,3),_RlQosClassifierUtilizationRulesNumber_Type())
rlQosClassifierUtilizationRulesNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosClassifierUtilizationRulesNumber.setStatus(_A)
class _RlQosClassifierUtilizationSystem_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RlQosClassifierUtilizationSystem_Type.__name__=_K
_RlQosClassifierUtilizationSystem_Object=MibScalar
rlQosClassifierUtilizationSystem=_RlQosClassifierUtilizationSystem_Object((1,3,6,1,4,1,171,10,94,89,89,88,36,2),_RlQosClassifierUtilizationSystem_Type())
rlQosClassifierUtilizationSystem.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosClassifierUtilizationSystem.setStatus(_A)
_RlQosClassifierRulesNumberUtilizationSystem_Type=Unsigned32
_RlQosClassifierRulesNumberUtilizationSystem_Object=MibScalar
rlQosClassifierRulesNumberUtilizationSystem=_RlQosClassifierRulesNumberUtilizationSystem_Object((1,3,6,1,4,1,171,10,94,89,89,88,36,3),_RlQosClassifierRulesNumberUtilizationSystem_Type())
rlQosClassifierRulesNumberUtilizationSystem.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosClassifierRulesNumberUtilizationSystem.setStatus(_A)
_RlQosPortToProfileMappingTable_Object=MibTable
rlQosPortToProfileMappingTable=_RlQosPortToProfileMappingTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,37))
if mibBuilder.loadTexts:rlQosPortToProfileMappingTable.setStatus(_A)
_RlQosPortToProfileMappingEntry_Object=MibTableRow
rlQosPortToProfileMappingEntry=_RlQosPortToProfileMappingEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,37,1))
rlQosPortToProfileMappingEntry.setIndexNames((0,_C,_AD))
if mibBuilder.loadTexts:rlQosPortToProfileMappingEntry.setStatus(_A)
_RlQosPort_Type=Integer32
_RlQosPort_Object=MibTableColumn
rlQosPort=_RlQosPort_Object((1,3,6,1,4,1,171,10,94,89,89,88,37,1,1),_RlQosPort_Type())
rlQosPort.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosPort.setStatus(_A)
_RlQosProfileName_Type=DisplayString
_RlQosProfileName_Object=MibTableColumn
rlQosProfileName=_RlQosProfileName_Object((1,3,6,1,4,1,171,10,94,89,89,88,37,1,2),_RlQosProfileName_Type())
rlQosProfileName.setMaxAccess(_E)
if mibBuilder.loadTexts:rlQosProfileName.setStatus(_A)
_RlQosTimeBasedAclTable_Object=MibTable
rlQosTimeBasedAclTable=_RlQosTimeBasedAclTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,38))
if mibBuilder.loadTexts:rlQosTimeBasedAclTable.setStatus(_A)
_RlQosTimeBasedAclEntry_Object=MibTableRow
rlQosTimeBasedAclEntry=_RlQosTimeBasedAclEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,38,1))
rlQosTimeBasedAclEntry.setIndexNames((1,_C,_AE))
if mibBuilder.loadTexts:rlQosTimeBasedAclEntry.setStatus(_A)
class _RlQosTimeBasedAclRangeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RlQosTimeBasedAclRangeName_Type.__name__=_H
_RlQosTimeBasedAclRangeName_Object=MibTableColumn
rlQosTimeBasedAclRangeName=_RlQosTimeBasedAclRangeName_Object((1,3,6,1,4,1,171,10,94,89,89,88,38,1,1),_RlQosTimeBasedAclRangeName_Type())
rlQosTimeBasedAclRangeName.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosTimeBasedAclRangeName.setStatus(_A)
class _RlQosTimeBasedAclAbsStart_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_RlQosTimeBasedAclAbsStart_Type.__name__=_H
_RlQosTimeBasedAclAbsStart_Object=MibTableColumn
rlQosTimeBasedAclAbsStart=_RlQosTimeBasedAclAbsStart_Object((1,3,6,1,4,1,171,10,94,89,89,88,38,1,2),_RlQosTimeBasedAclAbsStart_Type())
rlQosTimeBasedAclAbsStart.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosTimeBasedAclAbsStart.setStatus(_A)
class _RlQosTimeBasedAclAbsEnd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_RlQosTimeBasedAclAbsEnd_Type.__name__=_H
_RlQosTimeBasedAclAbsEnd_Object=MibTableColumn
rlQosTimeBasedAclAbsEnd=_RlQosTimeBasedAclAbsEnd_Object((1,3,6,1,4,1,171,10,94,89,89,88,38,1,3),_RlQosTimeBasedAclAbsEnd_Type())
rlQosTimeBasedAclAbsEnd.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosTimeBasedAclAbsEnd.setStatus(_A)
_RlQosTimeBasedAclStatus_Type=RowStatus
_RlQosTimeBasedAclStatus_Object=MibTableColumn
rlQosTimeBasedAclStatus=_RlQosTimeBasedAclStatus_Object((1,3,6,1,4,1,171,10,94,89,89,88,38,1,4),_RlQosTimeBasedAclStatus_Type())
rlQosTimeBasedAclStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosTimeBasedAclStatus.setStatus(_A)
_RlQosTimeBasedAclPeriodicTable_Object=MibTable
rlQosTimeBasedAclPeriodicTable=_RlQosTimeBasedAclPeriodicTable_Object((1,3,6,1,4,1,171,10,94,89,89,88,39))
if mibBuilder.loadTexts:rlQosTimeBasedAclPeriodicTable.setStatus(_A)
_RlQosTimeBasedAclPeriodicEntry_Object=MibTableRow
rlQosTimeBasedAclPeriodicEntry=_RlQosTimeBasedAclPeriodicEntry_Object((1,3,6,1,4,1,171,10,94,89,89,88,39,1))
rlQosTimeBasedAclPeriodicEntry.setIndexNames((0,_C,_AF),(0,_C,_AG),(0,_C,_AH),(0,_C,_AI))
if mibBuilder.loadTexts:rlQosTimeBasedAclPeriodicEntry.setStatus(_A)
class _RlQosTimeBasedAclPeriodicName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RlQosTimeBasedAclPeriodicName_Type.__name__=_H
_RlQosTimeBasedAclPeriodicName_Object=MibTableColumn
rlQosTimeBasedAclPeriodicName=_RlQosTimeBasedAclPeriodicName_Object((1,3,6,1,4,1,171,10,94,89,89,88,39,1,1),_RlQosTimeBasedAclPeriodicName_Type())
rlQosTimeBasedAclPeriodicName.setMaxAccess(_F)
if mibBuilder.loadTexts:rlQosTimeBasedAclPeriodicName.setStatus(_A)
_RlQosTimeBasedAclPeriodicWeekList_Type=RlQosTimeBasedAclWeekPeriodicList
_RlQosTimeBasedAclPeriodicWeekList_Object=MibTableColumn
rlQosTimeBasedAclPeriodicWeekList=_RlQosTimeBasedAclPeriodicWeekList_Object((1,3,6,1,4,1,171,10,94,89,89,88,39,1,2),_RlQosTimeBasedAclPeriodicWeekList_Type())
rlQosTimeBasedAclPeriodicWeekList.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosTimeBasedAclPeriodicWeekList.setStatus(_A)
class _RlQosTimeBasedAclPeriodicStart_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_RlQosTimeBasedAclPeriodicStart_Type.__name__=_H
_RlQosTimeBasedAclPeriodicStart_Object=MibTableColumn
rlQosTimeBasedAclPeriodicStart=_RlQosTimeBasedAclPeriodicStart_Object((1,3,6,1,4,1,171,10,94,89,89,88,39,1,3),_RlQosTimeBasedAclPeriodicStart_Type())
rlQosTimeBasedAclPeriodicStart.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosTimeBasedAclPeriodicStart.setStatus(_A)
class _RlQosTimeBasedAclPeriodicEnd_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,7))
_RlQosTimeBasedAclPeriodicEnd_Type.__name__=_H
_RlQosTimeBasedAclPeriodicEnd_Object=MibTableColumn
rlQosTimeBasedAclPeriodicEnd=_RlQosTimeBasedAclPeriodicEnd_Object((1,3,6,1,4,1,171,10,94,89,89,88,39,1,4),_RlQosTimeBasedAclPeriodicEnd_Type())
rlQosTimeBasedAclPeriodicEnd.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosTimeBasedAclPeriodicEnd.setStatus(_A)
_RlQosTimeBasedAclPeriodicStatus_Type=RowStatus
_RlQosTimeBasedAclPeriodicStatus_Object=MibTableColumn
rlQosTimeBasedAclPeriodicStatus=_RlQosTimeBasedAclPeriodicStatus_Object((1,3,6,1,4,1,171,10,94,89,89,88,39,1,5),_RlQosTimeBasedAclPeriodicStatus_Type())
rlQosTimeBasedAclPeriodicStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosTimeBasedAclPeriodicStatus.setStatus(_A)
_RlQosCPUSafeGuardEnable_Type=Integer32
_RlQosCPUSafeGuardEnable_Object=MibScalar
rlQosCPUSafeGuardEnable=_RlQosCPUSafeGuardEnable_Object((1,3,6,1,4,1,171,10,94,89,89,88,40),_RlQosCPUSafeGuardEnable_Type())
rlQosCPUSafeGuardEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosCPUSafeGuardEnable.setStatus(_A)
_RlQosTcamUpdateSemaphore_Type=TruthValue
_RlQosTcamUpdateSemaphore_Object=MibScalar
rlQosTcamUpdateSemaphore=_RlQosTcamUpdateSemaphore_Object((1,3,6,1,4,1,171,10,94,89,89,88,41),_RlQosTcamUpdateSemaphore_Type())
rlQosTcamUpdateSemaphore.setMaxAccess(_G)
if mibBuilder.loadTexts:rlQosTcamUpdateSemaphore.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ClassOffsetType':ClassOffsetType,'ClassTupleType':ClassTupleType,'AceActionType':AceActionType,'AceObjectType':AceObjectType,'AclObjectType':AclObjectType,_g:ClassMapType,_h:ClassMapAction,'PolicerType':PolicerType,'PolicerAction':PolicerAction,'QosObjectMode':QosObjectMode,'QosObjectBasicMode':QosObjectBasicMode,_R:BinaryStatus,'QueueType':QueueType,'AclDefaultAction':AclDefaultAction,'InterfaceType':InterfaceType,'StatisticsCntrNumOfBitsType':StatisticsCntrNumOfBitsType,'StatisticsCntrType':StatisticsCntrType,'RlQosTimeBasedAclWeekPeriodicList':RlQosTimeBasedAclWeekPeriodicList,'rlQosCliMib':rlQosCliMib,'rlQosCliQosMode':rlQosCliQosMode,'rlQosCliBasicModeCfg':rlQosCliBasicModeCfg,'rlQosMaxNumOfAce':rlQosMaxNumOfAce,'rlQosOffsetTable':rlQosOffsetTable,'rlQosOffsetEntry':rlQosOffsetEntry,_a:rlQosOffsetIndex,'rlQosOffsetType':rlQosOffsetType,'rlQosOffsetValue':rlQosOffsetValue,'rlQosOffsetMask':rlQosOffsetMask,'rlQosOffsetPattern':rlQosOffsetPattern,'rlQosOffsetTuplePointer':rlQosOffsetTuplePointer,'rlQosOffsetStatus':rlQosOffsetStatus,'rlQosTupleTable':rlQosTupleTable,'rlQosTupleEntry':rlQosTupleEntry,_b:rlQosTupleIndex,'rlQosTupleType':rlQosTupleType,'rlQosTupleValue1':rlQosTupleValue1,'rlQosTupleValue2':rlQosTupleValue2,'rlQosTupleStatus':rlQosTupleStatus,'rlQosAceTable':rlQosAceTable,'rlQosAceEntry':rlQosAceEntry,_c:rlQosAceIndex,'rlQosAceAction':rlQosAceAction,'rlQosAceType':rlQosAceType,'rlQosAceTuple1':rlQosAceTuple1,'rlQosAceTuple2':rlQosAceTuple2,'rlQosAceTuple3':rlQosAceTuple3,'rlQosAceTuple4':rlQosAceTuple4,'rlQosAceTuple5':rlQosAceTuple5,'rlQosAceTuple6':rlQosAceTuple6,'rlQosAceTuple7':rlQosAceTuple7,'rlQosAceTuple8':rlQosAceTuple8,'rlQosAceAccount':rlQosAceAccount,'rlQosAceStatus':rlQosAceStatus,'rlQosAclTable':rlQosAclTable,'rlQosAclEntry':rlQosAclEntry,_d:rlQosAclIndex,'rlQosAclName':rlQosAclName,'rlQosAclType':rlQosAclType,'rlQosAclStatus':rlQosAclStatus,'rlQosAclAceRefTable':rlQosAclAceRefTable,'rlQosAclAceRefEntry':rlQosAclAceRefEntry,_e:rlQosAclAceRefAcePointer,'rlQosAclAceRefAclPointer':rlQosAclAceRefAclPointer,'rlQosAclAceRefStatus':rlQosAclAceRefStatus,'rlQosClassMapTable':rlQosClassMapTable,'rlQosClassMapEntry':rlQosClassMapEntry,_f:rlQosClassMapIndex,'rlQosClassMapName':rlQosClassMapName,'rlQosClassMapType':rlQosClassMapType,'rlQosClassMapAction':rlQosClassMapAction,'rlQosClassMapMarkValue':rlQosClassMapMarkValue,'rlQosClassMapPolicer':rlQosClassMapPolicer,'rlQosClassMapMatch1':rlQosClassMapMatch1,'rlQosClassMapMatch2':rlQosClassMapMatch2,'rlQosClassMapMarkVlan':rlQosClassMapMarkVlan,'rlQosClassMapNewVlan':rlQosClassMapNewVlan,'rlQosClassMapNewPort':rlQosClassMapNewPort,'rlQosClassMapCopyPort':rlQosClassMapCopyPort,'rlQosClassMapStatus':rlQosClassMapStatus,'rlQosClassMapMatch3':rlQosClassMapMatch3,'rlQosPolicerTable':rlQosPolicerTable,'rlQosPolicerEntry':rlQosPolicerEntry,_L:rlQosPolicerIndex,'rlQosPolicerName':rlQosPolicerName,'rlQosPolicerType':rlQosPolicerType,'rlQosPolicerCir':rlQosPolicerCir,'rlQosPolicerCbs':rlQosPolicerCbs,'rlQosPolicerAction':rlQosPolicerAction,'rlQosPolicerCasPointerRemVal':rlQosPolicerCasPointerRemVal,'rlQosPolicerStatus':rlQosPolicerStatus,'rlQosPolicyMapTable':rlQosPolicyMapTable,'rlQosPolicyMapEntry':rlQosPolicyMapEntry,_i:rlQosPolicyMapIndex,'rlQosPolicyMapName':rlQosPolicyMapName,'rlQosPolicyMapStatus':rlQosPolicyMapStatus,'rlQosPolicyClassRefTable':rlQosPolicyClassRefTable,'rlQosPolicyClassRefEntry':rlQosPolicyClassRefEntry,_j:rlQosPolicyClassRefClassPointer,'rlQosPolicyClassRefPolicyPointer':rlQosPolicyClassRefPolicyPointer,'rlQosPolicyClassRefStatus':rlQosPolicyClassRefStatus,'rlQosIfPolicyTable':rlQosIfPolicyTable,'rlQosIfPolicyEntry':rlQosIfPolicyEntry,_M:rlIfIndex,_T:rlIfType,'rlQosIfPolicyMapPointerIn':rlQosIfPolicyMapPointerIn,'rlQosIfPolicyMapPointerOut':rlQosIfPolicyMapPointerOut,'rlQosIfTrustActive':rlQosIfTrustActive,'rlQosPortShaperStatus':rlQosPortShaperStatus,'rlQosCirPortShaper':rlQosCirPortShaper,'rlQosCbsPortShaper':rlQosCbsPortShaper,'rlQosIfProfilePointer':rlQosIfProfilePointer,'rlQosQueueProfilePointer':rlQosQueueProfilePointer,'rlQosQueueShapeProfilePointer':rlQosQueueShapeProfilePointer,'rlQosAclDefaultAction':rlQosAclDefaultAction,'rlQosIfPolicyMapStatus':rlQosIfPolicyMapStatus,'rlQosIfAclIn':rlQosIfAclIn,'rlQosIfAclOut':rlQosIfAclOut,'rlQosIfPolicerIn':rlQosIfPolicerIn,'rlQosPortRateLimitStatus':rlQosPortRateLimitStatus,'rlQosCirPortRateLimit':rlQosCirPortRateLimit,'rlQosCbsPortRateLimit':rlQosCbsPortRateLimit,'rlQosIfIpv6AclIn':rlQosIfIpv6AclIn,'rlQosIfIpv6AclOut':rlQosIfIpv6AclOut,'rlQosIfProfileCfgTable':rlQosIfProfileCfgTable,'rlQosIfProfileCfgEntry':rlQosIfProfileCfgEntry,_k:rlIfProfileName,_l:rlQosQueueId,'rlQosTdThersholdDp0':rlQosTdThersholdDp0,'rlQosTdThersholdDp1':rlQosTdThersholdDp1,'rlQosTdThersholdDp2':rlQosTdThersholdDp2,'rlQosRedMinDp0':rlQosRedMinDp0,'rlQosRedMaxDp0':rlQosRedMaxDp0,'rlQosRedProbDp0':rlQosRedProbDp0,'rlQosRedMinDp1':rlQosRedMinDp1,'rlQosRedMaxDp1':rlQosRedMaxDp1,'rlQosRedProbDp1':rlQosRedProbDp1,'rlQosRedMinDp2':rlQosRedMinDp2,'rlQosRedMaxDp2':rlQosRedMaxDp2,'rlQosRedProbDp2':rlQosRedProbDp2,'rlQosRedQweight':rlQosRedQweight,'rlQosIfprofileStatus':rlQosIfprofileStatus,'rlQosDscpMutationTable':rlQosDscpMutationTable,'rlQosDscpMutationEntry':rlQosDscpMutationEntry,_m:rlQosOldDscp,'rlQosNewDscp':rlQosNewDscp,'rlQosDscpRemarkTable':rlQosDscpRemarkTable,'rlQosDscpRemarkEntry':rlQosDscpRemarkEntry,_n:rlQosRmOldDscp,'rlQosRmNewDscp':rlQosRmNewDscp,'rlQosCosQueueTable':rlQosCosQueueTable,'rlQosCosQueueEntry':rlQosCosQueueEntry,_o:rlQosCosIndex,'rlQosCosQueueId':rlQosCosQueueId,'rlQosDscpQueueTable':rlQosDscpQueueTable,'rlQosDscpQueueEntry':rlQosDscpQueueEntry,_p:rlQosDscpIndex,'rlQosQueueNum':rlQosQueueNum,'rlQosTcpPortQueueTable':rlQosTcpPortQueueTable,'rlQosTcpPortQueueEntry':rlQosTcpPortQueueEntry,_q:rlQosTcpPort,'rlQosTcpQueueValue':rlQosTcpQueueValue,'rlQosTcpPortQueueStatus':rlQosTcpPortQueueStatus,'rlQosUdpPortQueueTable':rlQosUdpPortQueueTable,'rlQosUdpPortQueueEntry':rlQosUdpPortQueueEntry,_r:rlQosUdpPort,'rlQosUdpQueueValue':rlQosUdpQueueValue,'rlQosUdpPortQueueStatus':rlQosUdpPortQueueStatus,'rlQosEfManageTable':rlQosEfManageTable,'rlQosEfManageEntry':rlQosEfManageEntry,_s:rlQosEfQueueId,'rlQosEfState':rlQosEfState,'rlQosEfPriority':rlQosEfPriority,'rlQosQueueProfileTable':rlQosQueueProfileTable,'rlQosQueueProfileEntry':rlQosQueueProfileEntry,_t:rlQueueProfileName,'rlQosTypeQueue1':rlQosTypeQueue1,'rlQosValueQueue1':rlQosValueQueue1,'rlQosTypeQueue2':rlQosTypeQueue2,'rlQosValueQueue2':rlQosValueQueue2,'rlQosTypeQueue3':rlQosTypeQueue3,'rlQosValueQueue3':rlQosValueQueue3,'rlQosTypeQueue4':rlQosTypeQueue4,'rlQosValueQueue4':rlQosValueQueue4,'rlQosTypeQueue5':rlQosTypeQueue5,'rlQosValueQueue5':rlQosValueQueue5,'rlQosTypeQueue6':rlQosTypeQueue6,'rlQosValueQueue6':rlQosValueQueue6,'rlQosTypeQueue7':rlQosTypeQueue7,'rlQosValueQueue7':rlQosValueQueue7,'rlQosTypeQueue8':rlQosTypeQueue8,'rlQosValueQueue8':rlQosValueQueue8,'rlQosQueueProfileStatus':rlQosQueueProfileStatus,'rlQosNumOfIfConnections':rlQosNumOfIfConnections,'rlQosQueueShapeProfileTable':rlQosQueueShapeProfileTable,'rlQosQueueShapeProfileEntry':rlQosQueueShapeProfileEntry,_u:rlQosQueueShapeIndex,'rlQosCirQueue1':rlQosCirQueue1,'rlQosCbsQueue1':rlQosCbsQueue1,'rlQosCirQueue2':rlQosCirQueue2,'rlQosCbsQueue2':rlQosCbsQueue2,'rlQosCirQueue3':rlQosCirQueue3,'rlQosCbsQueue3':rlQosCbsQueue3,'rlQosCirQueue4':rlQosCirQueue4,'rlQosCbsQueue4':rlQosCbsQueue4,'rlQosCirQueue5':rlQosCirQueue5,'rlQosCbsQueue5':rlQosCbsQueue5,'rlQosCirQueue6':rlQosCirQueue6,'rlQosCbsQueue6':rlQosCbsQueue6,'rlQosCirQueue7':rlQosCirQueue7,'rlQosCbsQueue7':rlQosCbsQueue7,'rlQosCirQueue8':rlQosCirQueue8,'rlQosCbsQueue8':rlQosCbsQueue8,'rlQosQueueShapeProfileStatus':rlQosQueueShapeProfileStatus,'rlQosAclCounterTable':rlQosAclCounterTable,'rlQosAclCounterEntry':rlQosAclCounterEntry,_v:rlQosAclCounterInterface,_w:rlQosAclCounterAclIndex,_x:rlQosAclCounterAceIndex,'rlQosAclCounterValue':rlQosAclCounterValue,'rlQosFreeIndexesTable':rlQosFreeIndexesTable,'rlQosFreeIndexesEntry':rlQosFreeIndexesEntry,_y:rlQosFreeIndexesTableId,'rlQosFreeIndexesValue':rlQosFreeIndexesValue,'rlQosNamesToIndexesTable':rlQosNamesToIndexesTable,'rlQosNamesToIndexesEntry':rlQosNamesToIndexesEntry,_A0:rlQosNamesToIndexesTableId,_A1:rlQosNamesToIndexesName,'rlQosNamesToIndexesValue':rlQosNamesToIndexesValue,'rlQosStackControlQueue':rlQosStackControlQueue,'rlQosStackControlCos':rlQosStackControlCos,'rlQosCosQueueDefaultMapTable':rlQosCosQueueDefaultMapTable,'rlQosCosQueueDefaultMapEntry':rlQosCosQueueDefaultMapEntry,_A2:rlQosCosQueueDefaultMapVpt,'rlQosCosQueueDefaultMapQueueId':rlQosCosQueueDefaultMapQueueId,'rlQosPredefBlockAclTable':rlQosPredefBlockAclTable,'rlQosPredefBlockAclEntry':rlQosPredefBlockAclEntry,_A3:rlQosPredefBlockAclIfIndex,_A4:rlQosPredefBlockAclIfType,'rlQosPredefBlockAclMask':rlQosPredefBlockAclMask,'rlQosPredefBlockAclStatus':rlQosPredefBlockAclStatus,'rlQosAceTidxTable':rlQosAceTidxTable,'rlQosAceTidxEntry':rlQosAceTidxEntry,_A5:rlQosAceTidxAclIndex,_A6:rlQosAceTidxIndex,'rlQosAceTidxAction':rlQosAceTidxAction,'rlQosAceTidxType':rlQosAceTidxType,'rlQosAceTidxTuple1':rlQosAceTidxTuple1,'rlQosAceTidxTuple2':rlQosAceTidxTuple2,'rlQosAceTidxTuple3':rlQosAceTidxTuple3,'rlQosAceTidxTuple4':rlQosAceTidxTuple4,'rlQosAceTidxTuple5':rlQosAceTidxTuple5,'rlQosAceTidxTuple6':rlQosAceTidxTuple6,'rlQosAceTidxTuple7':rlQosAceTidxTuple7,'rlQosAceTidxTuple8':rlQosAceTidxTuple8,'rlQosAceTidxAccount':rlQosAceTidxAccount,'rlQosAceTidxStatus':rlQosAceTidxStatus,'rlQosAceTidxTimeRange':rlQosAceTidxTimeRange,'rlQosAceTidxTimeRangeIsActive':rlQosAceTidxTimeRangeIsActive,'rlQosMibVersion':rlQosMibVersion,'rlQosDscpQueueDefaultMapTable':rlQosDscpQueueDefaultMapTable,'rlQosDscpQueueDefaultMapEntry':rlQosDscpQueueDefaultMapEntry,_A7:rlQosDscpQueueDefaultMapDscp,'rlQosDscpQueueDefaultMapQueueId':rlQosDscpQueueDefaultMapQueueId,'rlQosDscpToDpTable':rlQosDscpToDpTable,'rlQosDscpToDpEntry':rlQosDscpToDpEntry,_A8:rlQosDscp,'rlQosDp':rlQosDp,'rlQosStatistics':rlQosStatistics,'rlQosPortPolicyStatisticsTable':rlQosPortPolicyStatisticsTable,'rlQosPortPolicyStatisticsEntry':rlQosPortPolicyStatisticsEntry,_A9:rlQosPortPolicyStatisticsCntrType,'rlQosPortPolicyStatisticsCntrNumOfBits':rlQosPortPolicyStatisticsCntrNumOfBits,'rlQosPortPolicyStatisticsEnableCounting':rlQosPortPolicyStatisticsEnableCounting,'rlQosPortPolicyStatisticsCounterValue':rlQosPortPolicyStatisticsCounterValue,'rlQosSinglePolicerStatisticsTable':rlQosSinglePolicerStatisticsTable,'rlQosSinglePolicerStatisticsEntry':rlQosSinglePolicerStatisticsEntry,'rlQosSinglePolicerStatisticsInProfileCounterValue':rlQosSinglePolicerStatisticsInProfileCounterValue,'rlQosSinglePolicerStatisticsInProfileCntrNumOfBits':rlQosSinglePolicerStatisticsInProfileCntrNumOfBits,'rlQosSinglePolicerStatisticsOutProfileCounterValue':rlQosSinglePolicerStatisticsOutProfileCounterValue,'rlQosSinglePolicerStatisticsOutProfileCntrNumOfBits':rlQosSinglePolicerStatisticsOutProfileCntrNumOfBits,'rlQosSinglePolicerStatisticsStatus':rlQosSinglePolicerStatisticsStatus,'rlQosAggregatePolicerStatisticsTable':rlQosAggregatePolicerStatisticsTable,'rlQosAggregatePolicerStatisticsEntry':rlQosAggregatePolicerStatisticsEntry,'rlQosAggregatePolicerStatisticsInProfileCounterValue':rlQosAggregatePolicerStatisticsInProfileCounterValue,'rlQosAggregatePolicerStatisticsInProfileCntrNumOfBits':rlQosAggregatePolicerStatisticsInProfileCntrNumOfBits,'rlQosAggregatePolicerStatisticsOutProfileCounterValue':rlQosAggregatePolicerStatisticsOutProfileCounterValue,'rlQosAggregatePolicerStatisticsOutProfileCntrNumOfBits':rlQosAggregatePolicerStatisticsOutProfileCntrNumOfBits,'rlQosAggregatePolicerStatisticsStatus':rlQosAggregatePolicerStatisticsStatus,'rlQosOutQueueStatisticsTable':rlQosOutQueueStatisticsTable,'rlQosOutQueueStatisticsEntry':rlQosOutQueueStatisticsEntry,_AA:rlQosOutQueueStatisticsCountrID,'rlQosOutQueueStatisticsIfIndexList':rlQosOutQueueStatisticsIfIndexList,'rlQosOutQueueStatisticsPortAll':rlQosOutQueueStatisticsPortAll,'rlQosOutQueueStatisticsVlan':rlQosOutQueueStatisticsVlan,'rlQosOutQueueStatisticsVlanAll':rlQosOutQueueStatisticsVlanAll,'rlQosOutQueueStatisticsQueue':rlQosOutQueueStatisticsQueue,'rlQosOutQueueStatisticsQueueAll':rlQosOutQueueStatisticsQueueAll,'rlQosOutQueueStatisticsDP':rlQosOutQueueStatisticsDP,'rlQosOutQueueStatisticsDPAll':rlQosOutQueueStatisticsDPAll,'rlQosOutQueueStatisticsCounterTailDropValue':rlQosOutQueueStatisticsCounterTailDropValue,'rlQosOutQueueStatisticsCounterAllValue':rlQosOutQueueStatisticsCounterAllValue,'rlQosOutQueueStatisticsCntrNumOfBits':rlQosOutQueueStatisticsCntrNumOfBits,'rlQosOutQueueStatisticsStatus':rlQosOutQueueStatisticsStatus,'rlQosGlobalStatisticsCntrsTable':rlQosGlobalStatisticsCntrsTable,'rlQosGlobalStatisticsCntrsEntry':rlQosGlobalStatisticsCntrsEntry,_AB:rlQosGlobalStatisticsCntrsType,'rlQosGlobalStatisticsCntrsNumOfBits':rlQosGlobalStatisticsCntrsNumOfBits,'rlQosGlobalStatisticsCntrsCounterValue':rlQosGlobalStatisticsCntrsCounterValue,'rlQosGlobalStatisticsStatus':rlQosGlobalStatisticsStatus,'rlQosClearCounters':rlQosClearCounters,'rlQosClassifierUtilization':rlQosClassifierUtilization,'rlQosClassifierUtilizationTable':rlQosClassifierUtilizationTable,'rlQosClassifierUtilizationEntry':rlQosClassifierUtilizationEntry,_AC:rlQosClassifierUtilizationUnitId,'rlQosClassifierUtilizationPercent':rlQosClassifierUtilizationPercent,'rlQosClassifierUtilizationRulesNumber':rlQosClassifierUtilizationRulesNumber,'rlQosClassifierUtilizationSystem':rlQosClassifierUtilizationSystem,'rlQosClassifierRulesNumberUtilizationSystem':rlQosClassifierRulesNumberUtilizationSystem,'rlQosPortToProfileMappingTable':rlQosPortToProfileMappingTable,'rlQosPortToProfileMappingEntry':rlQosPortToProfileMappingEntry,_AD:rlQosPort,'rlQosProfileName':rlQosProfileName,'rlQosTimeBasedAclTable':rlQosTimeBasedAclTable,'rlQosTimeBasedAclEntry':rlQosTimeBasedAclEntry,_AE:rlQosTimeBasedAclRangeName,'rlQosTimeBasedAclAbsStart':rlQosTimeBasedAclAbsStart,'rlQosTimeBasedAclAbsEnd':rlQosTimeBasedAclAbsEnd,'rlQosTimeBasedAclStatus':rlQosTimeBasedAclStatus,'rlQosTimeBasedAclPeriodicTable':rlQosTimeBasedAclPeriodicTable,'rlQosTimeBasedAclPeriodicEntry':rlQosTimeBasedAclPeriodicEntry,_AF:rlQosTimeBasedAclPeriodicName,_AG:rlQosTimeBasedAclPeriodicWeekList,_AH:rlQosTimeBasedAclPeriodicStart,_AI:rlQosTimeBasedAclPeriodicEnd,'rlQosTimeBasedAclPeriodicStatus':rlQosTimeBasedAclPeriodicStatus,'rlQosCPUSafeGuardEnable':rlQosCPUSafeGuardEnable,'rlQosTcamUpdateSemaphore':rlQosTcamUpdateSemaphore})