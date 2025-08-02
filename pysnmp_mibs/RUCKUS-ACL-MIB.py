_Ax='ruckusAclGroup'
_Aw='ruckusAclVPortBindRowStatus'
_Av='ruckusAclVPortBindLog'
_Au='ruckusAclVPortBindName'
_At='ruckusAclVlanBindRowStatus'
_As='ruckusAclVlanBindLog'
_Ar='ruckusAclVlanBindName'
_Aq='ruckusAclIfBindRowStatus'
_Ap='ruckusAclIfBindLog'
_Ao='ruckusAclIfBindName'
_An='ruckusMacAclFilterRowStatus'
_Am='ruckusMacAclFilterLogEnable'
_Al='ruckusMacAclFilterMirrorPkts'
_Ak='ruckusMacAclFilterExtEtherType'
_Aj='ruckusMacAclFilterEtherType'
_Ai='ruckusMacAclFilterDestMask'
_Ah='ruckusMacAclFilterDestAddr'
_Ag='ruckusMacAclFilterSrcMask'
_Af='ruckusMacAclFilterSrcAddr'
_Ae='ruckusMacAclFilterAction'
_Ad='ruckusIpv6AclFilterRowStatus'
_Ac='ruckusIpv6AclFilterComments'
_Ab='ruckusIpv6AclFilterLogEnable'
_Aa='ruckusIpv6AclFilterMirrorPkts'
_AZ='ruckusIpv6AclFilterSourceRoute'
_AY='ruckusIpv6AclFilterFragments'
_AX='ruckusIpv6AclFilterInternalPriority'
_AW='ruckusIpv6AclFilterPriorityForce'
_AV='ruckusIpv6AclFilterPriorityMatch'
_AU='ruckusIpv6AclFilterDscpForce'
_AT='ruckusIpv6AclFilterDscpMatch'
_AS='ruckusIpv6AclFilterPolicyName'
_AR='ruckusIpv6AclFilterIcmpCode'
_AQ='ruckusIpv6AclFilterIcmpType'
_AP='ruckusIpv6AclFilterEstablished'
_AO='ruckusIpv6AclFilterDestPortHigh'
_AN='ruckusIpv6AclFilterDestPortLow'
_AM='ruckusIpv6AclFilterDestOperator'
_AL='ruckusIpv6AclFilterDestPrefixLen'
_AK='ruckusIpv6AclFilterDestAddr'
_AJ='ruckusIpv6AclFilterSrcPortHigh'
_AI='ruckusIpv6AclFilterSrcPortLow'
_AH='ruckusIpv6AclFilterSrcOperator'
_AG='ruckusIpv6AclFilterSrcPrefixLen'
_AF='ruckusIpv6AclFilterSrcAddr'
_AE='ruckusIpv6AclFilterExtProtocol'
_AD='ruckusIpv6AclFilterStdProtocol'
_AC='ruckusIpv6AclFilterAction'
_AB='ruckusIpv4AclFilterRowStatus'
_AA='ruckusIpv4AclFilterComments'
_A9='ruckusIpv4AclFilterLogEnable'
_A8='ruckusIpv4AclFilterMirrorPkts'
_A7='ruckusIpv4AclFilterInternalPriority'
_A6='ruckusIpv4AclFilterPriorityForce'
_A5='ruckusIpv4AclFilterPriorityMatch'
_A4='ruckusIpv4AclFilterDscpForce'
_A3='ruckusIpv4AclFilterDscpMatch'
_A2='ruckusIpv4AclFilterPolicyName'
_A1='ruckusIpv4AclFilterIcmpCode'
_A0='ruckusIpv4AclFilterIcmpType'
_z='ruckusIpv4AclFilterTos'
_y='ruckusIpv4AclFilterPrecedence'
_x='ruckusIpv4AclFilterEstablished'
_w='ruckusIpv4AclFilterDestPortHigh'
_v='ruckusIpv4AclFilterDestPortLow'
_u='ruckusIpv4AclFilterDestOperator'
_t='ruckusIpv4AclFilterDestMask'
_s='ruckusIpv4AclFilterDestAddr'
_r='ruckusIpv4AclFilterSrcPortHigh'
_q='ruckusIpv4AclFilterSrcPortLow'
_p='ruckusIpv4AclFilterSrcOperator'
_o='ruckusIpv4AclFilterSrcMask'
_n='ruckusIpv4AclFilterSrcAddr'
_m='ruckusIpv4AclFilterExtProtocol'
_l='ruckusIpv4AclFilterStdProtocol'
_k='ruckusIpv4AclFilterAction'
_j='ruckusAclRowStatus'
_i='ruckusAclAcctEnable'
_h='ruckusAclVPortBindDirection'
_g='ruckusAclVPortBindType'
_f='ruckusAclVPortBindPort'
_e='ruckusAclVPortBindId'
_d='ruckusAclVlanBindDirection'
_c='ruckusAclVlanBindType'
_b='ruckusAclVlanBindId'
_a='ruckusAclIfBindDirection'
_Z='ruckusAclIfBindType'
_Y='ruckusAclIfBindPort'
_X='ruckusMacAclFilterSeqNum'
_W='ruckusIpv6AclFilterSeqNum'
_V='paramProblem'
_U='timeExceed'
_T='routerSolicit'
_S='routerAdv'
_R='echoReq'
_Q='destUnreachable'
_P='echoReply'
_O='ruckusIpv4AclFilterSeqNum'
_N='ruckusAclType'
_M='read-only'
_L='DisplayString'
_K='000000000000'
_J='extended'
_I='ruckusAclName'
_H='MacAddress'
_G='TruthValue'
_F='Unsigned32'
_E='not-accessible'
_D='Integer32'
_C='read-create'
_B='RUCKUS-ACL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
snSwitch,=mibBuilder.importSymbols('FOUNDRY-SN-SWITCH-GROUP-MIB','snSwitch')
InterfaceIndex,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','ifIndex')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_L,_H,'PhysAddress','RowStatus','TextualConvention',_G)
ruckusAclMIB=ModuleIdentity((1,3,6,1,4,1,1991,1,1,3,45))
if mibBuilder.loadTexts:ruckusAclMIB.setRevisions(('2019-08-07 00:00',))
class VlanId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
class AclName(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
class AclPolicyName(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
class AclType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mac',1),('ipv4',2),('ipv6',3)))
class AclAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('deny',1),('permit',2)))
class AclDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ingress',1),('egress',2)))
class AclOperator(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('eq',1),('neq',2),('lt',3),('gt',4),('range',5),('none',6)))
class IpPrecedence(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('routine',1),('priority',2),('immediate',3),('flash',4),('flashOverride',5),('critical',6),('internet',7),('network',8),('other',9)))
class IpTos(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('normal',1),('lowCost',2),('maxReliability',3),('maxThroughput',4),('minDelay',5)))
class EtherType(TextualConvention,Unsigned32):status=_A;displayHint='x'
_RuckusAclNotify_ObjectIdentity=ObjectIdentity
ruckusAclNotify=_RuckusAclNotify_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,45,0))
_RuckusAclObjects_ObjectIdentity=ObjectIdentity
ruckusAclObjects=_RuckusAclObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,45,1))
_RuckusAcls_ObjectIdentity=ObjectIdentity
ruckusAcls=_RuckusAcls_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,45,1,1))
_RuckusAclTable_Object=MibTable
ruckusAclTable=_RuckusAclTable_Object((1,3,6,1,4,1,1991,1,1,3,45,1,1,1))
if mibBuilder.loadTexts:ruckusAclTable.setStatus(_A)
_RuckusAclEntry_Object=MibTableRow
ruckusAclEntry=_RuckusAclEntry_Object((1,3,6,1,4,1,1991,1,1,3,45,1,1,1,1))
ruckusAclEntry.setIndexNames((0,_B,_N),(0,_B,_I))
if mibBuilder.loadTexts:ruckusAclEntry.setStatus(_A)
_RuckusAclType_Type=AclType
_RuckusAclType_Object=MibTableColumn
ruckusAclType=_RuckusAclType_Object((1,3,6,1,4,1,1991,1,1,3,45,1,1,1,1,1),_RuckusAclType_Type())
ruckusAclType.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusAclType.setStatus(_A)
_RuckusAclName_Type=AclName
_RuckusAclName_Object=MibTableColumn
ruckusAclName=_RuckusAclName_Object((1,3,6,1,4,1,1991,1,1,3,45,1,1,1,1,2),_RuckusAclName_Type())
ruckusAclName.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusAclName.setStatus(_A)
_RuckusAclAcctEnable_Type=TruthValue
_RuckusAclAcctEnable_Object=MibTableColumn
ruckusAclAcctEnable=_RuckusAclAcctEnable_Object((1,3,6,1,4,1,1991,1,1,3,45,1,1,1,1,3),_RuckusAclAcctEnable_Type())
ruckusAclAcctEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusAclAcctEnable.setStatus(_A)
_RuckusAclStandard_Type=TruthValue
_RuckusAclStandard_Object=MibTableColumn
ruckusAclStandard=_RuckusAclStandard_Object((1,3,6,1,4,1,1991,1,1,3,45,1,1,1,1,4),_RuckusAclStandard_Type())
ruckusAclStandard.setMaxAccess(_M)
if mibBuilder.loadTexts:ruckusAclStandard.setStatus(_A)
_RuckusAclRowStatus_Type=RowStatus
_RuckusAclRowStatus_Object=MibTableColumn
ruckusAclRowStatus=_RuckusAclRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,45,1,1,1,1,5),_RuckusAclRowStatus_Type())
ruckusAclRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusAclRowStatus.setStatus(_A)
_RuckusAclFilters_ObjectIdentity=ObjectIdentity
ruckusAclFilters=_RuckusAclFilters_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,45,1,2))
_RuckusIpv4Filters_ObjectIdentity=ObjectIdentity
ruckusIpv4Filters=_RuckusIpv4Filters_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,45,1,2,1))
_RuckusIpv4AclFilterTable_Object=MibTable
ruckusIpv4AclFilterTable=_RuckusIpv4AclFilterTable_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1))
if mibBuilder.loadTexts:ruckusIpv4AclFilterTable.setStatus(_A)
_RuckusIpv4AclFilterEntry_Object=MibTableRow
ruckusIpv4AclFilterEntry=_RuckusIpv4AclFilterEntry_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1))
ruckusIpv4AclFilterEntry.setIndexNames((0,_B,_I),(0,_B,_O))
if mibBuilder.loadTexts:ruckusIpv4AclFilterEntry.setStatus(_A)
_RuckusIpv4AclFilterSeqNum_Type=Unsigned32
_RuckusIpv4AclFilterSeqNum_Object=MibTableColumn
ruckusIpv4AclFilterSeqNum=_RuckusIpv4AclFilterSeqNum_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,1),_RuckusIpv4AclFilterSeqNum_Type())
ruckusIpv4AclFilterSeqNum.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusIpv4AclFilterSeqNum.setStatus(_A)
_RuckusIpv4AclFilterAction_Type=AclAction
_RuckusIpv4AclFilterAction_Object=MibTableColumn
ruckusIpv4AclFilterAction=_RuckusIpv4AclFilterAction_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,2),_RuckusIpv4AclFilterAction_Type())
ruckusIpv4AclFilterAction.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterAction.setStatus(_A)
class _RuckusIpv4AclFilterStdProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,6,17,41,46,47,50,89,103,255)));namedValues=NamedValues(*(('ip',0),('icmp',1),('igmp',2),('tcp',6),('udp',17),('ip6',41),('rsvp',46),('gre',47),('esp',50),('ospf',89),('pim',103),(_J,255)))
_RuckusIpv4AclFilterStdProtocol_Type.__name__=_D
_RuckusIpv4AclFilterStdProtocol_Object=MibTableColumn
ruckusIpv4AclFilterStdProtocol=_RuckusIpv4AclFilterStdProtocol_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,3),_RuckusIpv4AclFilterStdProtocol_Type())
ruckusIpv4AclFilterStdProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterStdProtocol.setStatus(_A)
class _RuckusIpv4AclFilterExtProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RuckusIpv4AclFilterExtProtocol_Type.__name__=_D
_RuckusIpv4AclFilterExtProtocol_Object=MibTableColumn
ruckusIpv4AclFilterExtProtocol=_RuckusIpv4AclFilterExtProtocol_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,4),_RuckusIpv4AclFilterExtProtocol_Type())
ruckusIpv4AclFilterExtProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterExtProtocol.setStatus(_A)
_RuckusIpv4AclFilterSrcAddr_Type=InetAddressIPv4
_RuckusIpv4AclFilterSrcAddr_Object=MibTableColumn
ruckusIpv4AclFilterSrcAddr=_RuckusIpv4AclFilterSrcAddr_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,5),_RuckusIpv4AclFilterSrcAddr_Type())
ruckusIpv4AclFilterSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterSrcAddr.setStatus(_A)
_RuckusIpv4AclFilterSrcMask_Type=InetAddressIPv4
_RuckusIpv4AclFilterSrcMask_Object=MibTableColumn
ruckusIpv4AclFilterSrcMask=_RuckusIpv4AclFilterSrcMask_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,6),_RuckusIpv4AclFilterSrcMask_Type())
ruckusIpv4AclFilterSrcMask.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterSrcMask.setStatus(_A)
_RuckusIpv4AclFilterSrcOperator_Type=AclOperator
_RuckusIpv4AclFilterSrcOperator_Object=MibTableColumn
ruckusIpv4AclFilterSrcOperator=_RuckusIpv4AclFilterSrcOperator_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,7),_RuckusIpv4AclFilterSrcOperator_Type())
ruckusIpv4AclFilterSrcOperator.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterSrcOperator.setStatus(_A)
class _RuckusIpv4AclFilterSrcPortLow_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RuckusIpv4AclFilterSrcPortLow_Type.__name__=_F
_RuckusIpv4AclFilterSrcPortLow_Object=MibTableColumn
ruckusIpv4AclFilterSrcPortLow=_RuckusIpv4AclFilterSrcPortLow_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,8),_RuckusIpv4AclFilterSrcPortLow_Type())
ruckusIpv4AclFilterSrcPortLow.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterSrcPortLow.setStatus(_A)
class _RuckusIpv4AclFilterSrcPortHigh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RuckusIpv4AclFilterSrcPortHigh_Type.__name__=_F
_RuckusIpv4AclFilterSrcPortHigh_Object=MibTableColumn
ruckusIpv4AclFilterSrcPortHigh=_RuckusIpv4AclFilterSrcPortHigh_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,9),_RuckusIpv4AclFilterSrcPortHigh_Type())
ruckusIpv4AclFilterSrcPortHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterSrcPortHigh.setStatus(_A)
_RuckusIpv4AclFilterDestAddr_Type=InetAddressIPv4
_RuckusIpv4AclFilterDestAddr_Object=MibTableColumn
ruckusIpv4AclFilterDestAddr=_RuckusIpv4AclFilterDestAddr_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,10),_RuckusIpv4AclFilterDestAddr_Type())
ruckusIpv4AclFilterDestAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterDestAddr.setStatus(_A)
_RuckusIpv4AclFilterDestMask_Type=InetAddressIPv4
_RuckusIpv4AclFilterDestMask_Object=MibTableColumn
ruckusIpv4AclFilterDestMask=_RuckusIpv4AclFilterDestMask_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,11),_RuckusIpv4AclFilterDestMask_Type())
ruckusIpv4AclFilterDestMask.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterDestMask.setStatus(_A)
_RuckusIpv4AclFilterDestOperator_Type=AclOperator
_RuckusIpv4AclFilterDestOperator_Object=MibTableColumn
ruckusIpv4AclFilterDestOperator=_RuckusIpv4AclFilterDestOperator_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,12),_RuckusIpv4AclFilterDestOperator_Type())
ruckusIpv4AclFilterDestOperator.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterDestOperator.setStatus(_A)
class _RuckusIpv4AclFilterDestPortLow_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RuckusIpv4AclFilterDestPortLow_Type.__name__=_F
_RuckusIpv4AclFilterDestPortLow_Object=MibTableColumn
ruckusIpv4AclFilterDestPortLow=_RuckusIpv4AclFilterDestPortLow_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,13),_RuckusIpv4AclFilterDestPortLow_Type())
ruckusIpv4AclFilterDestPortLow.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterDestPortLow.setStatus(_A)
class _RuckusIpv4AclFilterDestPortHigh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RuckusIpv4AclFilterDestPortHigh_Type.__name__=_F
_RuckusIpv4AclFilterDestPortHigh_Object=MibTableColumn
ruckusIpv4AclFilterDestPortHigh=_RuckusIpv4AclFilterDestPortHigh_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,14),_RuckusIpv4AclFilterDestPortHigh_Type())
ruckusIpv4AclFilterDestPortHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterDestPortHigh.setStatus(_A)
_RuckusIpv4AclFilterEstablished_Type=TruthValue
_RuckusIpv4AclFilterEstablished_Object=MibTableColumn
ruckusIpv4AclFilterEstablished=_RuckusIpv4AclFilterEstablished_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,15),_RuckusIpv4AclFilterEstablished_Type())
ruckusIpv4AclFilterEstablished.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterEstablished.setStatus(_A)
_RuckusIpv4AclFilterPrecedence_Type=IpPrecedence
_RuckusIpv4AclFilterPrecedence_Object=MibTableColumn
ruckusIpv4AclFilterPrecedence=_RuckusIpv4AclFilterPrecedence_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,16),_RuckusIpv4AclFilterPrecedence_Type())
ruckusIpv4AclFilterPrecedence.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterPrecedence.setStatus(_A)
_RuckusIpv4AclFilterTos_Type=IpTos
_RuckusIpv4AclFilterTos_Object=MibTableColumn
ruckusIpv4AclFilterTos=_RuckusIpv4AclFilterTos_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,17),_RuckusIpv4AclFilterTos_Type())
ruckusIpv4AclFilterTos.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterTos.setStatus(_A)
class _RuckusIpv4AclFilterIcmpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,3,4,5,8,9,10,11,12,13,14,15,16,17,18,255)));namedValues=NamedValues(*((_P,0),(_Q,3),('srcQuench',4),('redirect',5),(_R,8),(_S,9),(_T,10),(_U,11),(_V,12),('timestampReq',13),('timestampReply',14),('infoReq',15),('infoReply',16),('addrMaskReq',17),('addrMaskReply',18),(_J,255)))
_RuckusIpv4AclFilterIcmpType_Type.__name__=_D
_RuckusIpv4AclFilterIcmpType_Object=MibTableColumn
ruckusIpv4AclFilterIcmpType=_RuckusIpv4AclFilterIcmpType_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,18),_RuckusIpv4AclFilterIcmpType_Type())
ruckusIpv4AclFilterIcmpType.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterIcmpType.setStatus(_A)
class _RuckusIpv4AclFilterIcmpCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RuckusIpv4AclFilterIcmpCode_Type.__name__=_D
_RuckusIpv4AclFilterIcmpCode_Object=MibTableColumn
ruckusIpv4AclFilterIcmpCode=_RuckusIpv4AclFilterIcmpCode_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,19),_RuckusIpv4AclFilterIcmpCode_Type())
ruckusIpv4AclFilterIcmpCode.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterIcmpCode.setStatus(_A)
class _RuckusIpv4AclFilterExtIcmpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RuckusIpv4AclFilterExtIcmpType_Type.__name__=_D
_RuckusIpv4AclFilterExtIcmpType_Object=MibTableColumn
ruckusIpv4AclFilterExtIcmpType=_RuckusIpv4AclFilterExtIcmpType_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,20),_RuckusIpv4AclFilterExtIcmpType_Type())
ruckusIpv4AclFilterExtIcmpType.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterExtIcmpType.setStatus(_A)
_RuckusIpv4AclFilterPolicyName_Type=AclPolicyName
_RuckusIpv4AclFilterPolicyName_Object=MibTableColumn
ruckusIpv4AclFilterPolicyName=_RuckusIpv4AclFilterPolicyName_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,21),_RuckusIpv4AclFilterPolicyName_Type())
ruckusIpv4AclFilterPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterPolicyName.setStatus(_A)
class _RuckusIpv4AclFilterDscpMatch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RuckusIpv4AclFilterDscpMatch_Type.__name__=_D
_RuckusIpv4AclFilterDscpMatch_Object=MibTableColumn
ruckusIpv4AclFilterDscpMatch=_RuckusIpv4AclFilterDscpMatch_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,22),_RuckusIpv4AclFilterDscpMatch_Type())
ruckusIpv4AclFilterDscpMatch.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterDscpMatch.setStatus(_A)
class _RuckusIpv4AclFilterDscpForce_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RuckusIpv4AclFilterDscpForce_Type.__name__=_D
_RuckusIpv4AclFilterDscpForce_Object=MibTableColumn
ruckusIpv4AclFilterDscpForce=_RuckusIpv4AclFilterDscpForce_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,23),_RuckusIpv4AclFilterDscpForce_Type())
ruckusIpv4AclFilterDscpForce.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterDscpForce.setStatus(_A)
class _RuckusIpv4AclFilterPriorityMatch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RuckusIpv4AclFilterPriorityMatch_Type.__name__=_D
_RuckusIpv4AclFilterPriorityMatch_Object=MibTableColumn
ruckusIpv4AclFilterPriorityMatch=_RuckusIpv4AclFilterPriorityMatch_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,24),_RuckusIpv4AclFilterPriorityMatch_Type())
ruckusIpv4AclFilterPriorityMatch.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterPriorityMatch.setStatus(_A)
class _RuckusIpv4AclFilterPriorityForce_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RuckusIpv4AclFilterPriorityForce_Type.__name__=_D
_RuckusIpv4AclFilterPriorityForce_Object=MibTableColumn
ruckusIpv4AclFilterPriorityForce=_RuckusIpv4AclFilterPriorityForce_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,25),_RuckusIpv4AclFilterPriorityForce_Type())
ruckusIpv4AclFilterPriorityForce.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterPriorityForce.setStatus(_A)
class _RuckusIpv4AclFilterInternalPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RuckusIpv4AclFilterInternalPriority_Type.__name__=_D
_RuckusIpv4AclFilterInternalPriority_Object=MibTableColumn
ruckusIpv4AclFilterInternalPriority=_RuckusIpv4AclFilterInternalPriority_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,26),_RuckusIpv4AclFilterInternalPriority_Type())
ruckusIpv4AclFilterInternalPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterInternalPriority.setStatus(_A)
class _RuckusIpv4AclFilterMirrorPkts_Type(TruthValue):defaultValue=2
_RuckusIpv4AclFilterMirrorPkts_Type.__name__=_G
_RuckusIpv4AclFilterMirrorPkts_Object=MibTableColumn
ruckusIpv4AclFilterMirrorPkts=_RuckusIpv4AclFilterMirrorPkts_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,27),_RuckusIpv4AclFilterMirrorPkts_Type())
ruckusIpv4AclFilterMirrorPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterMirrorPkts.setStatus(_A)
_RuckusIpv4AclFilterLogEnable_Type=TruthValue
_RuckusIpv4AclFilterLogEnable_Object=MibTableColumn
ruckusIpv4AclFilterLogEnable=_RuckusIpv4AclFilterLogEnable_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,28),_RuckusIpv4AclFilterLogEnable_Type())
ruckusIpv4AclFilterLogEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterLogEnable.setStatus(_A)
class _RuckusIpv4AclFilterComments_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RuckusIpv4AclFilterComments_Type.__name__=_L
_RuckusIpv4AclFilterComments_Object=MibTableColumn
ruckusIpv4AclFilterComments=_RuckusIpv4AclFilterComments_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,29),_RuckusIpv4AclFilterComments_Type())
ruckusIpv4AclFilterComments.setMaxAccess(_M)
if mibBuilder.loadTexts:ruckusIpv4AclFilterComments.setStatus(_A)
_RuckusIpv4AclFilterRowStatus_Type=RowStatus
_RuckusIpv4AclFilterRowStatus_Object=MibTableColumn
ruckusIpv4AclFilterRowStatus=_RuckusIpv4AclFilterRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,1,1,1,30),_RuckusIpv4AclFilterRowStatus_Type())
ruckusIpv4AclFilterRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv4AclFilterRowStatus.setStatus(_A)
_RuckusIpv6Filters_ObjectIdentity=ObjectIdentity
ruckusIpv6Filters=_RuckusIpv6Filters_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,45,1,2,2))
_RuckusIpv6AclFilterTable_Object=MibTable
ruckusIpv6AclFilterTable=_RuckusIpv6AclFilterTable_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1))
if mibBuilder.loadTexts:ruckusIpv6AclFilterTable.setStatus(_A)
_RuckusIpv6AclFilterEntry_Object=MibTableRow
ruckusIpv6AclFilterEntry=_RuckusIpv6AclFilterEntry_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1))
ruckusIpv6AclFilterEntry.setIndexNames((0,_B,_I),(0,_B,_W))
if mibBuilder.loadTexts:ruckusIpv6AclFilterEntry.setStatus(_A)
_RuckusIpv6AclFilterSeqNum_Type=Unsigned32
_RuckusIpv6AclFilterSeqNum_Object=MibTableColumn
ruckusIpv6AclFilterSeqNum=_RuckusIpv6AclFilterSeqNum_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,1),_RuckusIpv6AclFilterSeqNum_Type())
ruckusIpv6AclFilterSeqNum.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusIpv6AclFilterSeqNum.setStatus(_A)
_RuckusIpv6AclFilterAction_Type=AclAction
_RuckusIpv6AclFilterAction_Object=MibTableColumn
ruckusIpv6AclFilterAction=_RuckusIpv6AclFilterAction_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,2),_RuckusIpv6AclFilterAction_Type())
ruckusIpv6AclFilterAction.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterAction.setStatus(_A)
class _RuckusIpv6AclFilterStdProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(6,17,41,50,51,58,132,255)));namedValues=NamedValues(*(('tcp',6),('udp',17),('ip6',41),('esp',50),('ahp',51),('icmp',58),('sctp',132),(_J,255)))
_RuckusIpv6AclFilterStdProtocol_Type.__name__=_D
_RuckusIpv6AclFilterStdProtocol_Object=MibTableColumn
ruckusIpv6AclFilterStdProtocol=_RuckusIpv6AclFilterStdProtocol_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,3),_RuckusIpv6AclFilterStdProtocol_Type())
ruckusIpv6AclFilterStdProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterStdProtocol.setStatus(_A)
class _RuckusIpv6AclFilterExtProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RuckusIpv6AclFilterExtProtocol_Type.__name__=_D
_RuckusIpv6AclFilterExtProtocol_Object=MibTableColumn
ruckusIpv6AclFilterExtProtocol=_RuckusIpv6AclFilterExtProtocol_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,4),_RuckusIpv6AclFilterExtProtocol_Type())
ruckusIpv6AclFilterExtProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterExtProtocol.setStatus(_A)
_RuckusIpv6AclFilterSrcAddr_Type=InetAddressIPv6
_RuckusIpv6AclFilterSrcAddr_Object=MibTableColumn
ruckusIpv6AclFilterSrcAddr=_RuckusIpv6AclFilterSrcAddr_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,5),_RuckusIpv6AclFilterSrcAddr_Type())
ruckusIpv6AclFilterSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterSrcAddr.setStatus(_A)
class _RuckusIpv6AclFilterSrcPrefixLen_Type(Unsigned32):defaultValue=64;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_RuckusIpv6AclFilterSrcPrefixLen_Type.__name__=_F
_RuckusIpv6AclFilterSrcPrefixLen_Object=MibTableColumn
ruckusIpv6AclFilterSrcPrefixLen=_RuckusIpv6AclFilterSrcPrefixLen_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,6),_RuckusIpv6AclFilterSrcPrefixLen_Type())
ruckusIpv6AclFilterSrcPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterSrcPrefixLen.setStatus(_A)
_RuckusIpv6AclFilterSrcOperator_Type=AclOperator
_RuckusIpv6AclFilterSrcOperator_Object=MibTableColumn
ruckusIpv6AclFilterSrcOperator=_RuckusIpv6AclFilterSrcOperator_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,7),_RuckusIpv6AclFilterSrcOperator_Type())
ruckusIpv6AclFilterSrcOperator.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterSrcOperator.setStatus(_A)
class _RuckusIpv6AclFilterSrcPortLow_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RuckusIpv6AclFilterSrcPortLow_Type.__name__=_F
_RuckusIpv6AclFilterSrcPortLow_Object=MibTableColumn
ruckusIpv6AclFilterSrcPortLow=_RuckusIpv6AclFilterSrcPortLow_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,8),_RuckusIpv6AclFilterSrcPortLow_Type())
ruckusIpv6AclFilterSrcPortLow.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterSrcPortLow.setStatus(_A)
class _RuckusIpv6AclFilterSrcPortHigh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RuckusIpv6AclFilterSrcPortHigh_Type.__name__=_F
_RuckusIpv6AclFilterSrcPortHigh_Object=MibTableColumn
ruckusIpv6AclFilterSrcPortHigh=_RuckusIpv6AclFilterSrcPortHigh_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,9),_RuckusIpv6AclFilterSrcPortHigh_Type())
ruckusIpv6AclFilterSrcPortHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterSrcPortHigh.setStatus(_A)
_RuckusIpv6AclFilterDestAddr_Type=InetAddressIPv6
_RuckusIpv6AclFilterDestAddr_Object=MibTableColumn
ruckusIpv6AclFilterDestAddr=_RuckusIpv6AclFilterDestAddr_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,10),_RuckusIpv6AclFilterDestAddr_Type())
ruckusIpv6AclFilterDestAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterDestAddr.setStatus(_A)
class _RuckusIpv6AclFilterDestPrefixLen_Type(Unsigned32):defaultValue=64;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_RuckusIpv6AclFilterDestPrefixLen_Type.__name__=_F
_RuckusIpv6AclFilterDestPrefixLen_Object=MibTableColumn
ruckusIpv6AclFilterDestPrefixLen=_RuckusIpv6AclFilterDestPrefixLen_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,11),_RuckusIpv6AclFilterDestPrefixLen_Type())
ruckusIpv6AclFilterDestPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterDestPrefixLen.setStatus(_A)
_RuckusIpv6AclFilterDestOperator_Type=AclOperator
_RuckusIpv6AclFilterDestOperator_Object=MibTableColumn
ruckusIpv6AclFilterDestOperator=_RuckusIpv6AclFilterDestOperator_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,12),_RuckusIpv6AclFilterDestOperator_Type())
ruckusIpv6AclFilterDestOperator.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterDestOperator.setStatus(_A)
class _RuckusIpv6AclFilterDestPortLow_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RuckusIpv6AclFilterDestPortLow_Type.__name__=_F
_RuckusIpv6AclFilterDestPortLow_Object=MibTableColumn
ruckusIpv6AclFilterDestPortLow=_RuckusIpv6AclFilterDestPortLow_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,13),_RuckusIpv6AclFilterDestPortLow_Type())
ruckusIpv6AclFilterDestPortLow.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterDestPortLow.setStatus(_A)
class _RuckusIpv6AclFilterDestPortHigh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RuckusIpv6AclFilterDestPortHigh_Type.__name__=_F
_RuckusIpv6AclFilterDestPortHigh_Object=MibTableColumn
ruckusIpv6AclFilterDestPortHigh=_RuckusIpv6AclFilterDestPortHigh_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,14),_RuckusIpv6AclFilterDestPortHigh_Type())
ruckusIpv6AclFilterDestPortHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterDestPortHigh.setStatus(_A)
_RuckusIpv6AclFilterEstablished_Type=TruthValue
_RuckusIpv6AclFilterEstablished_Object=MibTableColumn
ruckusIpv6AclFilterEstablished=_RuckusIpv6AclFilterEstablished_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,15),_RuckusIpv6AclFilterEstablished_Type())
ruckusIpv6AclFilterEstablished.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterEstablished.setStatus(_A)
class _RuckusIpv6AclFilterIcmpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,128,129,130,131,132,133,134,135,136,138,255)));namedValues=NamedValues(*((_Q,1),('largePackets',2),(_U,3),(_V,4),(_R,128),(_P,129),('mldQueries',130),('mldReport',131),('mldReduction',132),(_T,133),(_S,134),('neighborSolicit',135),('neighborAdv',136),('routerRenumbering',138),(_J,255)))
_RuckusIpv6AclFilterIcmpType_Type.__name__=_D
_RuckusIpv6AclFilterIcmpType_Object=MibTableColumn
ruckusIpv6AclFilterIcmpType=_RuckusIpv6AclFilterIcmpType_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,16),_RuckusIpv6AclFilterIcmpType_Type())
ruckusIpv6AclFilterIcmpType.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterIcmpType.setStatus(_A)
class _RuckusIpv6AclFilterIcmpCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RuckusIpv6AclFilterIcmpCode_Type.__name__=_D
_RuckusIpv6AclFilterIcmpCode_Object=MibTableColumn
ruckusIpv6AclFilterIcmpCode=_RuckusIpv6AclFilterIcmpCode_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,17),_RuckusIpv6AclFilterIcmpCode_Type())
ruckusIpv6AclFilterIcmpCode.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterIcmpCode.setStatus(_A)
class _RuckusIpv6AclFilterExtIcmpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RuckusIpv6AclFilterExtIcmpType_Type.__name__=_D
_RuckusIpv6AclFilterExtIcmpType_Object=MibTableColumn
ruckusIpv6AclFilterExtIcmpType=_RuckusIpv6AclFilterExtIcmpType_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,18),_RuckusIpv6AclFilterExtIcmpType_Type())
ruckusIpv6AclFilterExtIcmpType.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterExtIcmpType.setStatus(_A)
_RuckusIpv6AclFilterPolicyName_Type=AclPolicyName
_RuckusIpv6AclFilterPolicyName_Object=MibTableColumn
ruckusIpv6AclFilterPolicyName=_RuckusIpv6AclFilterPolicyName_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,19),_RuckusIpv6AclFilterPolicyName_Type())
ruckusIpv6AclFilterPolicyName.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterPolicyName.setStatus(_A)
class _RuckusIpv6AclFilterDscpMatch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RuckusIpv6AclFilterDscpMatch_Type.__name__=_D
_RuckusIpv6AclFilterDscpMatch_Object=MibTableColumn
ruckusIpv6AclFilterDscpMatch=_RuckusIpv6AclFilterDscpMatch_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,20),_RuckusIpv6AclFilterDscpMatch_Type())
ruckusIpv6AclFilterDscpMatch.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterDscpMatch.setStatus(_A)
class _RuckusIpv6AclFilterDscpForce_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_RuckusIpv6AclFilterDscpForce_Type.__name__=_D
_RuckusIpv6AclFilterDscpForce_Object=MibTableColumn
ruckusIpv6AclFilterDscpForce=_RuckusIpv6AclFilterDscpForce_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,21),_RuckusIpv6AclFilterDscpForce_Type())
ruckusIpv6AclFilterDscpForce.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterDscpForce.setStatus(_A)
class _RuckusIpv6AclFilterPriorityMatch_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RuckusIpv6AclFilterPriorityMatch_Type.__name__=_D
_RuckusIpv6AclFilterPriorityMatch_Object=MibTableColumn
ruckusIpv6AclFilterPriorityMatch=_RuckusIpv6AclFilterPriorityMatch_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,22),_RuckusIpv6AclFilterPriorityMatch_Type())
ruckusIpv6AclFilterPriorityMatch.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterPriorityMatch.setStatus(_A)
class _RuckusIpv6AclFilterPriorityForce_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RuckusIpv6AclFilterPriorityForce_Type.__name__=_D
_RuckusIpv6AclFilterPriorityForce_Object=MibTableColumn
ruckusIpv6AclFilterPriorityForce=_RuckusIpv6AclFilterPriorityForce_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,23),_RuckusIpv6AclFilterPriorityForce_Type())
ruckusIpv6AclFilterPriorityForce.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterPriorityForce.setStatus(_A)
class _RuckusIpv6AclFilterInternalPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RuckusIpv6AclFilterInternalPriority_Type.__name__=_D
_RuckusIpv6AclFilterInternalPriority_Object=MibTableColumn
ruckusIpv6AclFilterInternalPriority=_RuckusIpv6AclFilterInternalPriority_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,24),_RuckusIpv6AclFilterInternalPriority_Type())
ruckusIpv6AclFilterInternalPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterInternalPriority.setStatus(_A)
class _RuckusIpv6AclFilterFragments_Type(TruthValue):defaultValue=2
_RuckusIpv6AclFilterFragments_Type.__name__=_G
_RuckusIpv6AclFilterFragments_Object=MibTableColumn
ruckusIpv6AclFilterFragments=_RuckusIpv6AclFilterFragments_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,25),_RuckusIpv6AclFilterFragments_Type())
ruckusIpv6AclFilterFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterFragments.setStatus(_A)
class _RuckusIpv6AclFilterSourceRoute_Type(TruthValue):defaultValue=2
_RuckusIpv6AclFilterSourceRoute_Type.__name__=_G
_RuckusIpv6AclFilterSourceRoute_Object=MibTableColumn
ruckusIpv6AclFilterSourceRoute=_RuckusIpv6AclFilterSourceRoute_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,26),_RuckusIpv6AclFilterSourceRoute_Type())
ruckusIpv6AclFilterSourceRoute.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterSourceRoute.setStatus(_A)
class _RuckusIpv6AclFilterMirrorPkts_Type(TruthValue):defaultValue=2
_RuckusIpv6AclFilterMirrorPkts_Type.__name__=_G
_RuckusIpv6AclFilterMirrorPkts_Object=MibTableColumn
ruckusIpv6AclFilterMirrorPkts=_RuckusIpv6AclFilterMirrorPkts_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,27),_RuckusIpv6AclFilterMirrorPkts_Type())
ruckusIpv6AclFilterMirrorPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterMirrorPkts.setStatus(_A)
_RuckusIpv6AclFilterLogEnable_Type=TruthValue
_RuckusIpv6AclFilterLogEnable_Object=MibTableColumn
ruckusIpv6AclFilterLogEnable=_RuckusIpv6AclFilterLogEnable_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,28),_RuckusIpv6AclFilterLogEnable_Type())
ruckusIpv6AclFilterLogEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterLogEnable.setStatus(_A)
class _RuckusIpv6AclFilterComments_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_RuckusIpv6AclFilterComments_Type.__name__=_L
_RuckusIpv6AclFilterComments_Object=MibTableColumn
ruckusIpv6AclFilterComments=_RuckusIpv6AclFilterComments_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,29),_RuckusIpv6AclFilterComments_Type())
ruckusIpv6AclFilterComments.setMaxAccess(_M)
if mibBuilder.loadTexts:ruckusIpv6AclFilterComments.setStatus(_A)
_RuckusIpv6AclFilterRowStatus_Type=RowStatus
_RuckusIpv6AclFilterRowStatus_Object=MibTableColumn
ruckusIpv6AclFilterRowStatus=_RuckusIpv6AclFilterRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,2,1,1,30),_RuckusIpv6AclFilterRowStatus_Type())
ruckusIpv6AclFilterRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusIpv6AclFilterRowStatus.setStatus(_A)
_RuckusMacFilters_ObjectIdentity=ObjectIdentity
ruckusMacFilters=_RuckusMacFilters_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,45,1,2,3))
_RuckusMacAclFilterTable_Object=MibTable
ruckusMacAclFilterTable=_RuckusMacAclFilterTable_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,3,1))
if mibBuilder.loadTexts:ruckusMacAclFilterTable.setStatus(_A)
_RuckusMacAclFilterEntry_Object=MibTableRow
ruckusMacAclFilterEntry=_RuckusMacAclFilterEntry_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,3,1,1))
ruckusMacAclFilterEntry.setIndexNames((0,_B,_I),(0,_B,_X))
if mibBuilder.loadTexts:ruckusMacAclFilterEntry.setStatus(_A)
_RuckusMacAclFilterSeqNum_Type=Unsigned32
_RuckusMacAclFilterSeqNum_Object=MibTableColumn
ruckusMacAclFilterSeqNum=_RuckusMacAclFilterSeqNum_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,3,1,1,1),_RuckusMacAclFilterSeqNum_Type())
ruckusMacAclFilterSeqNum.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusMacAclFilterSeqNum.setStatus(_A)
_RuckusMacAclFilterAction_Type=AclAction
_RuckusMacAclFilterAction_Object=MibTableColumn
ruckusMacAclFilterAction=_RuckusMacAclFilterAction_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,3,1,1,2),_RuckusMacAclFilterAction_Type())
ruckusMacAclFilterAction.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusMacAclFilterAction.setStatus(_A)
class _RuckusMacAclFilterSrcAddr_Type(MacAddress):defaultHexValue=_K
_RuckusMacAclFilterSrcAddr_Type.__name__=_H
_RuckusMacAclFilterSrcAddr_Object=MibTableColumn
ruckusMacAclFilterSrcAddr=_RuckusMacAclFilterSrcAddr_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,3,1,1,3),_RuckusMacAclFilterSrcAddr_Type())
ruckusMacAclFilterSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusMacAclFilterSrcAddr.setStatus(_A)
class _RuckusMacAclFilterSrcMask_Type(MacAddress):defaultHexValue=_K
_RuckusMacAclFilterSrcMask_Type.__name__=_H
_RuckusMacAclFilterSrcMask_Object=MibTableColumn
ruckusMacAclFilterSrcMask=_RuckusMacAclFilterSrcMask_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,3,1,1,4),_RuckusMacAclFilterSrcMask_Type())
ruckusMacAclFilterSrcMask.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusMacAclFilterSrcMask.setStatus(_A)
class _RuckusMacAclFilterDestAddr_Type(MacAddress):defaultHexValue=_K
_RuckusMacAclFilterDestAddr_Type.__name__=_H
_RuckusMacAclFilterDestAddr_Object=MibTableColumn
ruckusMacAclFilterDestAddr=_RuckusMacAclFilterDestAddr_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,3,1,1,5),_RuckusMacAclFilterDestAddr_Type())
ruckusMacAclFilterDestAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusMacAclFilterDestAddr.setStatus(_A)
class _RuckusMacAclFilterDestMask_Type(MacAddress):defaultHexValue=_K
_RuckusMacAclFilterDestMask_Type.__name__=_H
_RuckusMacAclFilterDestMask_Object=MibTableColumn
ruckusMacAclFilterDestMask=_RuckusMacAclFilterDestMask_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,3,1,1,6),_RuckusMacAclFilterDestMask_Type())
ruckusMacAclFilterDestMask.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusMacAclFilterDestMask.setStatus(_A)
class _RuckusMacAclFilterEtherType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('arp',1),('ipv4',2),('ipv6',3),(_J,4)))
_RuckusMacAclFilterEtherType_Type.__name__=_D
_RuckusMacAclFilterEtherType_Object=MibTableColumn
ruckusMacAclFilterEtherType=_RuckusMacAclFilterEtherType_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,3,1,1,7),_RuckusMacAclFilterEtherType_Type())
ruckusMacAclFilterEtherType.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusMacAclFilterEtherType.setStatus(_A)
_RuckusMacAclFilterExtEtherType_Type=EtherType
_RuckusMacAclFilterExtEtherType_Object=MibTableColumn
ruckusMacAclFilterExtEtherType=_RuckusMacAclFilterExtEtherType_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,3,1,1,8),_RuckusMacAclFilterExtEtherType_Type())
ruckusMacAclFilterExtEtherType.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusMacAclFilterExtEtherType.setStatus(_A)
class _RuckusMacAclFilterMirrorPkts_Type(TruthValue):defaultValue=2
_RuckusMacAclFilterMirrorPkts_Type.__name__=_G
_RuckusMacAclFilterMirrorPkts_Object=MibTableColumn
ruckusMacAclFilterMirrorPkts=_RuckusMacAclFilterMirrorPkts_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,3,1,1,9),_RuckusMacAclFilterMirrorPkts_Type())
ruckusMacAclFilterMirrorPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusMacAclFilterMirrorPkts.setStatus(_A)
_RuckusMacAclFilterLogEnable_Type=TruthValue
_RuckusMacAclFilterLogEnable_Object=MibTableColumn
ruckusMacAclFilterLogEnable=_RuckusMacAclFilterLogEnable_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,3,1,1,10),_RuckusMacAclFilterLogEnable_Type())
ruckusMacAclFilterLogEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusMacAclFilterLogEnable.setStatus(_A)
_RuckusMacAclFilterRowStatus_Type=RowStatus
_RuckusMacAclFilterRowStatus_Object=MibTableColumn
ruckusMacAclFilterRowStatus=_RuckusMacAclFilterRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,45,1,2,3,1,1,11),_RuckusMacAclFilterRowStatus_Type())
ruckusMacAclFilterRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusMacAclFilterRowStatus.setStatus(_A)
_RuckusAclBindings_ObjectIdentity=ObjectIdentity
ruckusAclBindings=_RuckusAclBindings_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,45,1,3))
_RuckusAclIfBindTable_Object=MibTable
ruckusAclIfBindTable=_RuckusAclIfBindTable_Object((1,3,6,1,4,1,1991,1,1,3,45,1,3,1))
if mibBuilder.loadTexts:ruckusAclIfBindTable.setStatus(_A)
_RuckusAclIfBindEntry_Object=MibTableRow
ruckusAclIfBindEntry=_RuckusAclIfBindEntry_Object((1,3,6,1,4,1,1991,1,1,3,45,1,3,1,1))
ruckusAclIfBindEntry.setIndexNames((0,_B,_Y),(0,_B,_Z),(0,_B,_a))
if mibBuilder.loadTexts:ruckusAclIfBindEntry.setStatus(_A)
_RuckusAclIfBindPort_Type=InterfaceIndex
_RuckusAclIfBindPort_Object=MibTableColumn
ruckusAclIfBindPort=_RuckusAclIfBindPort_Object((1,3,6,1,4,1,1991,1,1,3,45,1,3,1,1,1),_RuckusAclIfBindPort_Type())
ruckusAclIfBindPort.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusAclIfBindPort.setStatus(_A)
_RuckusAclIfBindType_Type=AclType
_RuckusAclIfBindType_Object=MibTableColumn
ruckusAclIfBindType=_RuckusAclIfBindType_Object((1,3,6,1,4,1,1991,1,1,3,45,1,3,1,1,2),_RuckusAclIfBindType_Type())
ruckusAclIfBindType.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusAclIfBindType.setStatus(_A)
_RuckusAclIfBindDirection_Type=AclDirection
_RuckusAclIfBindDirection_Object=MibTableColumn
ruckusAclIfBindDirection=_RuckusAclIfBindDirection_Object((1,3,6,1,4,1,1991,1,1,3,45,1,3,1,1,3),_RuckusAclIfBindDirection_Type())
ruckusAclIfBindDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusAclIfBindDirection.setStatus(_A)
_RuckusAclIfBindName_Type=AclName
_RuckusAclIfBindName_Object=MibTableColumn
ruckusAclIfBindName=_RuckusAclIfBindName_Object((1,3,6,1,4,1,1991,1,1,3,45,1,3,1,1,4),_RuckusAclIfBindName_Type())
ruckusAclIfBindName.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusAclIfBindName.setStatus(_A)
class _RuckusAclIfBindLog_Type(TruthValue):defaultValue=2
_RuckusAclIfBindLog_Type.__name__=_G
_RuckusAclIfBindLog_Object=MibTableColumn
ruckusAclIfBindLog=_RuckusAclIfBindLog_Object((1,3,6,1,4,1,1991,1,1,3,45,1,3,1,1,5),_RuckusAclIfBindLog_Type())
ruckusAclIfBindLog.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusAclIfBindLog.setStatus(_A)
_RuckusAclIfBindRowStatus_Type=RowStatus
_RuckusAclIfBindRowStatus_Object=MibTableColumn
ruckusAclIfBindRowStatus=_RuckusAclIfBindRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,45,1,3,1,1,6),_RuckusAclIfBindRowStatus_Type())
ruckusAclIfBindRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusAclIfBindRowStatus.setStatus(_A)
_RuckusAclVlanBindTable_Object=MibTable
ruckusAclVlanBindTable=_RuckusAclVlanBindTable_Object((1,3,6,1,4,1,1991,1,1,3,45,1,3,2))
if mibBuilder.loadTexts:ruckusAclVlanBindTable.setStatus(_A)
_RuckusAclVlanBindEntry_Object=MibTableRow
ruckusAclVlanBindEntry=_RuckusAclVlanBindEntry_Object((1,3,6,1,4,1,1991,1,1,3,45,1,3,2,1))
ruckusAclVlanBindEntry.setIndexNames((0,_B,_b),(0,_B,_c),(0,_B,_d))
if mibBuilder.loadTexts:ruckusAclVlanBindEntry.setStatus(_A)
_RuckusAclVlanBindId_Type=VlanId
_RuckusAclVlanBindId_Object=MibTableColumn
ruckusAclVlanBindId=_RuckusAclVlanBindId_Object((1,3,6,1,4,1,1991,1,1,3,45,1,3,2,1,1),_RuckusAclVlanBindId_Type())
ruckusAclVlanBindId.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusAclVlanBindId.setStatus(_A)
_RuckusAclVlanBindType_Type=AclType
_RuckusAclVlanBindType_Object=MibTableColumn
ruckusAclVlanBindType=_RuckusAclVlanBindType_Object((1,3,6,1,4,1,1991,1,1,3,45,1,3,2,1,2),_RuckusAclVlanBindType_Type())
ruckusAclVlanBindType.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusAclVlanBindType.setStatus(_A)
_RuckusAclVlanBindDirection_Type=AclDirection
_RuckusAclVlanBindDirection_Object=MibTableColumn
ruckusAclVlanBindDirection=_RuckusAclVlanBindDirection_Object((1,3,6,1,4,1,1991,1,1,3,45,1,3,2,1,3),_RuckusAclVlanBindDirection_Type())
ruckusAclVlanBindDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusAclVlanBindDirection.setStatus(_A)
_RuckusAclVlanBindName_Type=AclName
_RuckusAclVlanBindName_Object=MibTableColumn
ruckusAclVlanBindName=_RuckusAclVlanBindName_Object((1,3,6,1,4,1,1991,1,1,3,45,1,3,2,1,4),_RuckusAclVlanBindName_Type())
ruckusAclVlanBindName.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusAclVlanBindName.setStatus(_A)
class _RuckusAclVlanBindLog_Type(TruthValue):defaultValue=2
_RuckusAclVlanBindLog_Type.__name__=_G
_RuckusAclVlanBindLog_Object=MibTableColumn
ruckusAclVlanBindLog=_RuckusAclVlanBindLog_Object((1,3,6,1,4,1,1991,1,1,3,45,1,3,2,1,5),_RuckusAclVlanBindLog_Type())
ruckusAclVlanBindLog.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusAclVlanBindLog.setStatus(_A)
_RuckusAclVlanBindRowStatus_Type=RowStatus
_RuckusAclVlanBindRowStatus_Object=MibTableColumn
ruckusAclVlanBindRowStatus=_RuckusAclVlanBindRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,45,1,3,2,1,6),_RuckusAclVlanBindRowStatus_Type())
ruckusAclVlanBindRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusAclVlanBindRowStatus.setStatus(_A)
_RuckusAclVPortBindTable_Object=MibTable
ruckusAclVPortBindTable=_RuckusAclVPortBindTable_Object((1,3,6,1,4,1,1991,1,1,3,45,1,3,3))
if mibBuilder.loadTexts:ruckusAclVPortBindTable.setStatus(_A)
_RuckusAclVPortBindEntry_Object=MibTableRow
ruckusAclVPortBindEntry=_RuckusAclVPortBindEntry_Object((1,3,6,1,4,1,1991,1,1,3,45,1,3,3,1))
ruckusAclVPortBindEntry.setIndexNames((0,_B,_e),(0,_B,_f),(0,_B,_g),(0,_B,_h))
if mibBuilder.loadTexts:ruckusAclVPortBindEntry.setStatus(_A)
_RuckusAclVPortBindId_Type=VlanId
_RuckusAclVPortBindId_Object=MibTableColumn
ruckusAclVPortBindId=_RuckusAclVPortBindId_Object((1,3,6,1,4,1,1991,1,1,3,45,1,3,3,1,1),_RuckusAclVPortBindId_Type())
ruckusAclVPortBindId.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusAclVPortBindId.setStatus(_A)
_RuckusAclVPortBindPort_Type=InterfaceIndex
_RuckusAclVPortBindPort_Object=MibTableColumn
ruckusAclVPortBindPort=_RuckusAclVPortBindPort_Object((1,3,6,1,4,1,1991,1,1,3,45,1,3,3,1,2),_RuckusAclVPortBindPort_Type())
ruckusAclVPortBindPort.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusAclVPortBindPort.setStatus(_A)
_RuckusAclVPortBindType_Type=AclType
_RuckusAclVPortBindType_Object=MibTableColumn
ruckusAclVPortBindType=_RuckusAclVPortBindType_Object((1,3,6,1,4,1,1991,1,1,3,45,1,3,3,1,3),_RuckusAclVPortBindType_Type())
ruckusAclVPortBindType.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusAclVPortBindType.setStatus(_A)
_RuckusAclVPortBindDirection_Type=AclDirection
_RuckusAclVPortBindDirection_Object=MibTableColumn
ruckusAclVPortBindDirection=_RuckusAclVPortBindDirection_Object((1,3,6,1,4,1,1991,1,1,3,45,1,3,3,1,4),_RuckusAclVPortBindDirection_Type())
ruckusAclVPortBindDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:ruckusAclVPortBindDirection.setStatus(_A)
_RuckusAclVPortBindName_Type=AclName
_RuckusAclVPortBindName_Object=MibTableColumn
ruckusAclVPortBindName=_RuckusAclVPortBindName_Object((1,3,6,1,4,1,1991,1,1,3,45,1,3,3,1,5),_RuckusAclVPortBindName_Type())
ruckusAclVPortBindName.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusAclVPortBindName.setStatus(_A)
class _RuckusAclVPortBindLog_Type(TruthValue):defaultValue=2
_RuckusAclVPortBindLog_Type.__name__=_G
_RuckusAclVPortBindLog_Object=MibTableColumn
ruckusAclVPortBindLog=_RuckusAclVPortBindLog_Object((1,3,6,1,4,1,1991,1,1,3,45,1,3,3,1,6),_RuckusAclVPortBindLog_Type())
ruckusAclVPortBindLog.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusAclVPortBindLog.setStatus(_A)
_RuckusAclVPortBindRowStatus_Type=RowStatus
_RuckusAclVPortBindRowStatus_Object=MibTableColumn
ruckusAclVPortBindRowStatus=_RuckusAclVPortBindRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,45,1,3,3,1,7),_RuckusAclVPortBindRowStatus_Type())
ruckusAclVPortBindRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ruckusAclVPortBindRowStatus.setStatus(_A)
_RuckusAclConformance_ObjectIdentity=ObjectIdentity
ruckusAclConformance=_RuckusAclConformance_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,45,2))
_RuckusAclCompliances_ObjectIdentity=ObjectIdentity
ruckusAclCompliances=_RuckusAclCompliances_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,45,2,1))
_RuckusAclGroups_ObjectIdentity=ObjectIdentity
ruckusAclGroups=_RuckusAclGroups_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,45,2,2))
ruckusAclGroup=ObjectGroup((1,3,6,1,4,1,1991,1,1,3,45,2,2,1))
ruckusAclGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw)))
if mibBuilder.loadTexts:ruckusAclGroup.setStatus(_A)
ruckusAclCompliance=ModuleCompliance((1,3,6,1,4,1,1991,1,1,3,45,2,1,1))
ruckusAclCompliance.setObjects((_B,_Ax))
if mibBuilder.loadTexts:ruckusAclCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'VlanId':VlanId,'AclName':AclName,'AclPolicyName':AclPolicyName,'AclType':AclType,'AclAction':AclAction,'AclDirection':AclDirection,'AclOperator':AclOperator,'IpPrecedence':IpPrecedence,'IpTos':IpTos,'EtherType':EtherType,'ruckusAclMIB':ruckusAclMIB,'ruckusAclNotify':ruckusAclNotify,'ruckusAclObjects':ruckusAclObjects,'ruckusAcls':ruckusAcls,'ruckusAclTable':ruckusAclTable,'ruckusAclEntry':ruckusAclEntry,_N:ruckusAclType,_I:ruckusAclName,_i:ruckusAclAcctEnable,'ruckusAclStandard':ruckusAclStandard,_j:ruckusAclRowStatus,'ruckusAclFilters':ruckusAclFilters,'ruckusIpv4Filters':ruckusIpv4Filters,'ruckusIpv4AclFilterTable':ruckusIpv4AclFilterTable,'ruckusIpv4AclFilterEntry':ruckusIpv4AclFilterEntry,_O:ruckusIpv4AclFilterSeqNum,_k:ruckusIpv4AclFilterAction,_l:ruckusIpv4AclFilterStdProtocol,_m:ruckusIpv4AclFilterExtProtocol,_n:ruckusIpv4AclFilterSrcAddr,_o:ruckusIpv4AclFilterSrcMask,_p:ruckusIpv4AclFilterSrcOperator,_q:ruckusIpv4AclFilterSrcPortLow,_r:ruckusIpv4AclFilterSrcPortHigh,_s:ruckusIpv4AclFilterDestAddr,_t:ruckusIpv4AclFilterDestMask,_u:ruckusIpv4AclFilterDestOperator,_v:ruckusIpv4AclFilterDestPortLow,_w:ruckusIpv4AclFilterDestPortHigh,_x:ruckusIpv4AclFilterEstablished,_y:ruckusIpv4AclFilterPrecedence,_z:ruckusIpv4AclFilterTos,_A0:ruckusIpv4AclFilterIcmpType,_A1:ruckusIpv4AclFilterIcmpCode,'ruckusIpv4AclFilterExtIcmpType':ruckusIpv4AclFilterExtIcmpType,_A2:ruckusIpv4AclFilterPolicyName,_A3:ruckusIpv4AclFilterDscpMatch,_A4:ruckusIpv4AclFilterDscpForce,_A5:ruckusIpv4AclFilterPriorityMatch,_A6:ruckusIpv4AclFilterPriorityForce,_A7:ruckusIpv4AclFilterInternalPriority,_A8:ruckusIpv4AclFilterMirrorPkts,_A9:ruckusIpv4AclFilterLogEnable,_AA:ruckusIpv4AclFilterComments,_AB:ruckusIpv4AclFilterRowStatus,'ruckusIpv6Filters':ruckusIpv6Filters,'ruckusIpv6AclFilterTable':ruckusIpv6AclFilterTable,'ruckusIpv6AclFilterEntry':ruckusIpv6AclFilterEntry,_W:ruckusIpv6AclFilterSeqNum,_AC:ruckusIpv6AclFilterAction,_AD:ruckusIpv6AclFilterStdProtocol,_AE:ruckusIpv6AclFilterExtProtocol,_AF:ruckusIpv6AclFilterSrcAddr,_AG:ruckusIpv6AclFilterSrcPrefixLen,_AH:ruckusIpv6AclFilterSrcOperator,_AI:ruckusIpv6AclFilterSrcPortLow,_AJ:ruckusIpv6AclFilterSrcPortHigh,_AK:ruckusIpv6AclFilterDestAddr,_AL:ruckusIpv6AclFilterDestPrefixLen,_AM:ruckusIpv6AclFilterDestOperator,_AN:ruckusIpv6AclFilterDestPortLow,_AO:ruckusIpv6AclFilterDestPortHigh,_AP:ruckusIpv6AclFilterEstablished,_AQ:ruckusIpv6AclFilterIcmpType,_AR:ruckusIpv6AclFilterIcmpCode,'ruckusIpv6AclFilterExtIcmpType':ruckusIpv6AclFilterExtIcmpType,_AS:ruckusIpv6AclFilterPolicyName,_AT:ruckusIpv6AclFilterDscpMatch,_AU:ruckusIpv6AclFilterDscpForce,_AV:ruckusIpv6AclFilterPriorityMatch,_AW:ruckusIpv6AclFilterPriorityForce,_AX:ruckusIpv6AclFilterInternalPriority,_AY:ruckusIpv6AclFilterFragments,_AZ:ruckusIpv6AclFilterSourceRoute,_Aa:ruckusIpv6AclFilterMirrorPkts,_Ab:ruckusIpv6AclFilterLogEnable,_Ac:ruckusIpv6AclFilterComments,_Ad:ruckusIpv6AclFilterRowStatus,'ruckusMacFilters':ruckusMacFilters,'ruckusMacAclFilterTable':ruckusMacAclFilterTable,'ruckusMacAclFilterEntry':ruckusMacAclFilterEntry,_X:ruckusMacAclFilterSeqNum,_Ae:ruckusMacAclFilterAction,_Af:ruckusMacAclFilterSrcAddr,_Ag:ruckusMacAclFilterSrcMask,_Ah:ruckusMacAclFilterDestAddr,_Ai:ruckusMacAclFilterDestMask,_Aj:ruckusMacAclFilterEtherType,_Ak:ruckusMacAclFilterExtEtherType,_Al:ruckusMacAclFilterMirrorPkts,_Am:ruckusMacAclFilterLogEnable,_An:ruckusMacAclFilterRowStatus,'ruckusAclBindings':ruckusAclBindings,'ruckusAclIfBindTable':ruckusAclIfBindTable,'ruckusAclIfBindEntry':ruckusAclIfBindEntry,_Y:ruckusAclIfBindPort,_Z:ruckusAclIfBindType,_a:ruckusAclIfBindDirection,_Ao:ruckusAclIfBindName,_Ap:ruckusAclIfBindLog,_Aq:ruckusAclIfBindRowStatus,'ruckusAclVlanBindTable':ruckusAclVlanBindTable,'ruckusAclVlanBindEntry':ruckusAclVlanBindEntry,_b:ruckusAclVlanBindId,_c:ruckusAclVlanBindType,_d:ruckusAclVlanBindDirection,_Ar:ruckusAclVlanBindName,_As:ruckusAclVlanBindLog,_At:ruckusAclVlanBindRowStatus,'ruckusAclVPortBindTable':ruckusAclVPortBindTable,'ruckusAclVPortBindEntry':ruckusAclVPortBindEntry,_e:ruckusAclVPortBindId,_f:ruckusAclVPortBindPort,_g:ruckusAclVPortBindType,_h:ruckusAclVPortBindDirection,_Au:ruckusAclVPortBindName,_Av:ruckusAclVPortBindLog,_Aw:ruckusAclVPortBindRowStatus,'ruckusAclConformance':ruckusAclConformance,'ruckusAclCompliances':ruckusAclCompliances,'ruckusAclCompliance':ruckusAclCompliance,'ruckusAclGroups':ruckusAclGroups,_Ax:ruckusAclGroup})