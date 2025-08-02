_A6='ipMRoute1MIBHCInterfaceGroup'
_A5='ipMRoute1MIBBoundaryGroup'
_A4='ipMRoute1MIBRouteGroup'
_A3='ipMRoute1MIBBasicGroup'
_A2='ipMRoute1Octets'
_A1='ipMRoute1DifferentInIfPackets'
_A0='ipMRoute1Pkts'
_z='ipMRoute1RtType'
_y='ipMRoute1RtMask'
_x='ipMRoute1RtAddress'
_w='ipMRoute1RtProto'
_v='ipMRoute1HCOctets'
_u='ipMRoute1InterfaceHCOutMcastOctets'
_t='ipMRoute1InterfaceHCInMcastOctets'
_s='ipMRoute1ScopeNameStatus'
_r='ipMRoute1ScopeNameDefault'
_q='ipMRoute1ScopeNameString'
_p='ipMRoute1BoundaryStatus'
_o='ipMRoute1NextHopClosestMemberHops'
_n='ipMRoute1Protocol'
_m='ipMRoute1InterfaceOutMcastOctets'
_l='ipMRoute1InterfaceInMcastOctets'
_k='ipMRoute1InterfaceRateLimit'
_j='ipMRoute1InterfaceProtocol'
_i='ipMRoute1InterfaceTtl'
_h='ipMRoute1NextHopProtocol'
_g='ipMRoute1NextHopExpiryTime'
_f='ipMRoute1NextHopUpTime'
_e='ipMRoute1NextHopState'
_d='ipMRoute1ExpiryTime'
_c='ipMRoute1UpTime'
_b='ipMRoute1InIfIndex'
_a='ipMRoute1UpstreamNeighbor'
_Z='ipMRoute1EntryCount'
_Y='ipMRoute1Enable'
_X='ipMRoute1ScopeNameLanguage'
_W='ipMRoute1ScopeNameAddressMask'
_V='ipMRoute1ScopeNameAddress'
_U='ipMRoute1BoundaryAddressMask'
_T='ipMRoute1BoundaryAddress'
_S='ipMRoute1BoundaryIfIndex'
_R='ipMRoute1InterfaceIfIndex'
_Q='ipMRoute1NextHopAddress'
_P='ipMRoute1NextHopIfIndex'
_O='ipMRoute1NextHopSourceMask'
_N='ipMRoute1NextHopSource'
_M='ipMRoute1NextHopGroup'
_L='ipMRoute1SourceMask'
_K='ipMRoute1Source'
_J='ipMRoute1Group'
_I='netmgmt'
_H='TruthValue'
_G='DisplayString'
_F='ipMRoute1NextHopPkts'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='DRAFT-IPMROUTE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','experimental','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention',_H)
ipMRoute1MIB=ModuleIdentity((1,3,6,1,3,60))
if mibBuilder.loadTexts:ipMRoute1MIB.setRevisions(('1999-07-22 12:00',))
class IpMRoute1Protocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('other',1),('local',2),(_I,3),('dvmrp',4),('mospf',5),('pimSparseDense',6),('cbt',7),('pimSparseMode',8),('pimDenseMode',9),('igmpOnly',10),('bgmp',11),('msdp',12)))
_IpMRoute1MIBObjects_ObjectIdentity=ObjectIdentity
ipMRoute1MIBObjects=_IpMRoute1MIBObjects_ObjectIdentity((1,3,6,1,3,60,1))
_IpMRoute1_ObjectIdentity=ObjectIdentity
ipMRoute1=_IpMRoute1_ObjectIdentity((1,3,6,1,3,60,1,1))
class _IpMRoute1Enable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_IpMRoute1Enable_Type.__name__=_E
_IpMRoute1Enable_Object=MibScalar
ipMRoute1Enable=_IpMRoute1Enable_Object((1,3,6,1,3,60,1,1,1),_IpMRoute1Enable_Type())
ipMRoute1Enable.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1Enable.setStatus(_A)
_IpMRoute1Table_Object=MibTable
ipMRoute1Table=_IpMRoute1Table_Object((1,3,6,1,3,60,1,1,2))
if mibBuilder.loadTexts:ipMRoute1Table.setStatus(_A)
_IpMRoute1Entry_Object=MibTableRow
ipMRoute1Entry=_IpMRoute1Entry_Object((1,3,6,1,3,60,1,1,2,1))
ipMRoute1Entry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:ipMRoute1Entry.setStatus(_A)
_IpMRoute1Group_Type=IpAddress
_IpMRoute1Group_Object=MibTableColumn
ipMRoute1Group=_IpMRoute1Group_Object((1,3,6,1,3,60,1,1,2,1,1),_IpMRoute1Group_Type())
ipMRoute1Group.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRoute1Group.setStatus(_A)
_IpMRoute1Source_Type=IpAddress
_IpMRoute1Source_Object=MibTableColumn
ipMRoute1Source=_IpMRoute1Source_Object((1,3,6,1,3,60,1,1,2,1,2),_IpMRoute1Source_Type())
ipMRoute1Source.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRoute1Source.setStatus(_A)
_IpMRoute1SourceMask_Type=IpAddress
_IpMRoute1SourceMask_Object=MibTableColumn
ipMRoute1SourceMask=_IpMRoute1SourceMask_Object((1,3,6,1,3,60,1,1,2,1,3),_IpMRoute1SourceMask_Type())
ipMRoute1SourceMask.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRoute1SourceMask.setStatus(_A)
_IpMRoute1UpstreamNeighbor_Type=IpAddress
_IpMRoute1UpstreamNeighbor_Object=MibTableColumn
ipMRoute1UpstreamNeighbor=_IpMRoute1UpstreamNeighbor_Object((1,3,6,1,3,60,1,1,2,1,4),_IpMRoute1UpstreamNeighbor_Type())
ipMRoute1UpstreamNeighbor.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1UpstreamNeighbor.setStatus(_A)
_IpMRoute1InIfIndex_Type=InterfaceIndexOrZero
_IpMRoute1InIfIndex_Object=MibTableColumn
ipMRoute1InIfIndex=_IpMRoute1InIfIndex_Object((1,3,6,1,3,60,1,1,2,1,5),_IpMRoute1InIfIndex_Type())
ipMRoute1InIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1InIfIndex.setStatus(_A)
_IpMRoute1UpTime_Type=TimeTicks
_IpMRoute1UpTime_Object=MibTableColumn
ipMRoute1UpTime=_IpMRoute1UpTime_Object((1,3,6,1,3,60,1,1,2,1,6),_IpMRoute1UpTime_Type())
ipMRoute1UpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1UpTime.setStatus(_A)
_IpMRoute1ExpiryTime_Type=TimeTicks
_IpMRoute1ExpiryTime_Object=MibTableColumn
ipMRoute1ExpiryTime=_IpMRoute1ExpiryTime_Object((1,3,6,1,3,60,1,1,2,1,7),_IpMRoute1ExpiryTime_Type())
ipMRoute1ExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1ExpiryTime.setStatus(_A)
_IpMRoute1Pkts_Type=Counter32
_IpMRoute1Pkts_Object=MibTableColumn
ipMRoute1Pkts=_IpMRoute1Pkts_Object((1,3,6,1,3,60,1,1,2,1,8),_IpMRoute1Pkts_Type())
ipMRoute1Pkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1Pkts.setStatus(_A)
_IpMRoute1DifferentInIfPackets_Type=Counter32
_IpMRoute1DifferentInIfPackets_Object=MibTableColumn
ipMRoute1DifferentInIfPackets=_IpMRoute1DifferentInIfPackets_Object((1,3,6,1,3,60,1,1,2,1,9),_IpMRoute1DifferentInIfPackets_Type())
ipMRoute1DifferentInIfPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1DifferentInIfPackets.setStatus(_A)
_IpMRoute1Octets_Type=Counter32
_IpMRoute1Octets_Object=MibTableColumn
ipMRoute1Octets=_IpMRoute1Octets_Object((1,3,6,1,3,60,1,1,2,1,10),_IpMRoute1Octets_Type())
ipMRoute1Octets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1Octets.setStatus(_A)
_IpMRoute1Protocol_Type=IpMRoute1Protocol
_IpMRoute1Protocol_Object=MibTableColumn
ipMRoute1Protocol=_IpMRoute1Protocol_Object((1,3,6,1,3,60,1,1,2,1,11),_IpMRoute1Protocol_Type())
ipMRoute1Protocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1Protocol.setStatus(_A)
class _IpMRoute1RtProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17)));namedValues=NamedValues(*(('other',1),('local',2),(_I,3),('icmp',4),('egp',5),('ggp',6),('hello',7),('rip',8),('isIs',9),('esIs',10),('ciscoIgrp',11),('bbnSpfIgp',12),('ospf',13),('bgp',14),('idpr',15),('ciscoEigrp',16),('dvmrp',17)))
_IpMRoute1RtProto_Type.__name__=_E
_IpMRoute1RtProto_Object=MibTableColumn
ipMRoute1RtProto=_IpMRoute1RtProto_Object((1,3,6,1,3,60,1,1,2,1,12),_IpMRoute1RtProto_Type())
ipMRoute1RtProto.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1RtProto.setStatus(_A)
_IpMRoute1RtAddress_Type=IpAddress
_IpMRoute1RtAddress_Object=MibTableColumn
ipMRoute1RtAddress=_IpMRoute1RtAddress_Object((1,3,6,1,3,60,1,1,2,1,13),_IpMRoute1RtAddress_Type())
ipMRoute1RtAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1RtAddress.setStatus(_A)
_IpMRoute1RtMask_Type=IpAddress
_IpMRoute1RtMask_Object=MibTableColumn
ipMRoute1RtMask=_IpMRoute1RtMask_Object((1,3,6,1,3,60,1,1,2,1,14),_IpMRoute1RtMask_Type())
ipMRoute1RtMask.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1RtMask.setStatus(_A)
class _IpMRoute1RtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unicast',1),('multicast',2)))
_IpMRoute1RtType_Type.__name__=_E
_IpMRoute1RtType_Object=MibTableColumn
ipMRoute1RtType=_IpMRoute1RtType_Object((1,3,6,1,3,60,1,1,2,1,15),_IpMRoute1RtType_Type())
ipMRoute1RtType.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1RtType.setStatus(_A)
_IpMRoute1HCOctets_Type=Counter64
_IpMRoute1HCOctets_Object=MibTableColumn
ipMRoute1HCOctets=_IpMRoute1HCOctets_Object((1,3,6,1,3,60,1,1,2,1,16),_IpMRoute1HCOctets_Type())
ipMRoute1HCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1HCOctets.setStatus(_A)
_IpMRoute1NextHopTable_Object=MibTable
ipMRoute1NextHopTable=_IpMRoute1NextHopTable_Object((1,3,6,1,3,60,1,1,3))
if mibBuilder.loadTexts:ipMRoute1NextHopTable.setStatus(_A)
_IpMRoute1NextHopEntry_Object=MibTableRow
ipMRoute1NextHopEntry=_IpMRoute1NextHopEntry_Object((1,3,6,1,3,60,1,1,3,1))
ipMRoute1NextHopEntry.setIndexNames((0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:ipMRoute1NextHopEntry.setStatus(_A)
_IpMRoute1NextHopGroup_Type=IpAddress
_IpMRoute1NextHopGroup_Object=MibTableColumn
ipMRoute1NextHopGroup=_IpMRoute1NextHopGroup_Object((1,3,6,1,3,60,1,1,3,1,1),_IpMRoute1NextHopGroup_Type())
ipMRoute1NextHopGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRoute1NextHopGroup.setStatus(_A)
_IpMRoute1NextHopSource_Type=IpAddress
_IpMRoute1NextHopSource_Object=MibTableColumn
ipMRoute1NextHopSource=_IpMRoute1NextHopSource_Object((1,3,6,1,3,60,1,1,3,1,2),_IpMRoute1NextHopSource_Type())
ipMRoute1NextHopSource.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRoute1NextHopSource.setStatus(_A)
_IpMRoute1NextHopSourceMask_Type=IpAddress
_IpMRoute1NextHopSourceMask_Object=MibTableColumn
ipMRoute1NextHopSourceMask=_IpMRoute1NextHopSourceMask_Object((1,3,6,1,3,60,1,1,3,1,3),_IpMRoute1NextHopSourceMask_Type())
ipMRoute1NextHopSourceMask.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRoute1NextHopSourceMask.setStatus(_A)
_IpMRoute1NextHopIfIndex_Type=InterfaceIndex
_IpMRoute1NextHopIfIndex_Object=MibTableColumn
ipMRoute1NextHopIfIndex=_IpMRoute1NextHopIfIndex_Object((1,3,6,1,3,60,1,1,3,1,4),_IpMRoute1NextHopIfIndex_Type())
ipMRoute1NextHopIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRoute1NextHopIfIndex.setStatus(_A)
_IpMRoute1NextHopAddress_Type=IpAddress
_IpMRoute1NextHopAddress_Object=MibTableColumn
ipMRoute1NextHopAddress=_IpMRoute1NextHopAddress_Object((1,3,6,1,3,60,1,1,3,1,5),_IpMRoute1NextHopAddress_Type())
ipMRoute1NextHopAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRoute1NextHopAddress.setStatus(_A)
class _IpMRoute1NextHopState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pruned',1),('forwarding',2)))
_IpMRoute1NextHopState_Type.__name__=_E
_IpMRoute1NextHopState_Object=MibTableColumn
ipMRoute1NextHopState=_IpMRoute1NextHopState_Object((1,3,6,1,3,60,1,1,3,1,6),_IpMRoute1NextHopState_Type())
ipMRoute1NextHopState.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1NextHopState.setStatus(_A)
_IpMRoute1NextHopUpTime_Type=TimeTicks
_IpMRoute1NextHopUpTime_Object=MibTableColumn
ipMRoute1NextHopUpTime=_IpMRoute1NextHopUpTime_Object((1,3,6,1,3,60,1,1,3,1,7),_IpMRoute1NextHopUpTime_Type())
ipMRoute1NextHopUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1NextHopUpTime.setStatus(_A)
_IpMRoute1NextHopExpiryTime_Type=TimeTicks
_IpMRoute1NextHopExpiryTime_Object=MibTableColumn
ipMRoute1NextHopExpiryTime=_IpMRoute1NextHopExpiryTime_Object((1,3,6,1,3,60,1,1,3,1,8),_IpMRoute1NextHopExpiryTime_Type())
ipMRoute1NextHopExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1NextHopExpiryTime.setStatus(_A)
_IpMRoute1NextHopClosestMemberHops_Type=Integer32
_IpMRoute1NextHopClosestMemberHops_Object=MibTableColumn
ipMRoute1NextHopClosestMemberHops=_IpMRoute1NextHopClosestMemberHops_Object((1,3,6,1,3,60,1,1,3,1,9),_IpMRoute1NextHopClosestMemberHops_Type())
ipMRoute1NextHopClosestMemberHops.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1NextHopClosestMemberHops.setStatus(_A)
_IpMRoute1NextHopProtocol_Type=IpMRoute1Protocol
_IpMRoute1NextHopProtocol_Object=MibTableColumn
ipMRoute1NextHopProtocol=_IpMRoute1NextHopProtocol_Object((1,3,6,1,3,60,1,1,3,1,10),_IpMRoute1NextHopProtocol_Type())
ipMRoute1NextHopProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1NextHopProtocol.setStatus(_A)
_IpMRoute1NextHopPkts_Type=Counter32
_IpMRoute1NextHopPkts_Object=MibTableColumn
ipMRoute1NextHopPkts=_IpMRoute1NextHopPkts_Object((1,3,6,1,3,60,1,1,3,1,11),_IpMRoute1NextHopPkts_Type())
ipMRoute1NextHopPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1NextHopPkts.setStatus(_A)
_IpMRoute1InterfaceTable_Object=MibTable
ipMRoute1InterfaceTable=_IpMRoute1InterfaceTable_Object((1,3,6,1,3,60,1,1,4))
if mibBuilder.loadTexts:ipMRoute1InterfaceTable.setStatus(_A)
_IpMRoute1InterfaceEntry_Object=MibTableRow
ipMRoute1InterfaceEntry=_IpMRoute1InterfaceEntry_Object((1,3,6,1,3,60,1,1,4,1))
ipMRoute1InterfaceEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:ipMRoute1InterfaceEntry.setStatus(_A)
_IpMRoute1InterfaceIfIndex_Type=InterfaceIndex
_IpMRoute1InterfaceIfIndex_Object=MibTableColumn
ipMRoute1InterfaceIfIndex=_IpMRoute1InterfaceIfIndex_Object((1,3,6,1,3,60,1,1,4,1,1),_IpMRoute1InterfaceIfIndex_Type())
ipMRoute1InterfaceIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRoute1InterfaceIfIndex.setStatus(_A)
class _IpMRoute1InterfaceTtl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IpMRoute1InterfaceTtl_Type.__name__=_E
_IpMRoute1InterfaceTtl_Object=MibTableColumn
ipMRoute1InterfaceTtl=_IpMRoute1InterfaceTtl_Object((1,3,6,1,3,60,1,1,4,1,2),_IpMRoute1InterfaceTtl_Type())
ipMRoute1InterfaceTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1InterfaceTtl.setStatus(_A)
_IpMRoute1InterfaceProtocol_Type=IpMRoute1Protocol
_IpMRoute1InterfaceProtocol_Object=MibTableColumn
ipMRoute1InterfaceProtocol=_IpMRoute1InterfaceProtocol_Object((1,3,6,1,3,60,1,1,4,1,3),_IpMRoute1InterfaceProtocol_Type())
ipMRoute1InterfaceProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1InterfaceProtocol.setStatus(_A)
class _IpMRoute1InterfaceRateLimit_Type(Integer32):defaultValue=0
_IpMRoute1InterfaceRateLimit_Type.__name__=_E
_IpMRoute1InterfaceRateLimit_Object=MibTableColumn
ipMRoute1InterfaceRateLimit=_IpMRoute1InterfaceRateLimit_Object((1,3,6,1,3,60,1,1,4,1,4),_IpMRoute1InterfaceRateLimit_Type())
ipMRoute1InterfaceRateLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1InterfaceRateLimit.setStatus(_A)
_IpMRoute1InterfaceInMcastOctets_Type=Counter32
_IpMRoute1InterfaceInMcastOctets_Object=MibTableColumn
ipMRoute1InterfaceInMcastOctets=_IpMRoute1InterfaceInMcastOctets_Object((1,3,6,1,3,60,1,1,4,1,5),_IpMRoute1InterfaceInMcastOctets_Type())
ipMRoute1InterfaceInMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1InterfaceInMcastOctets.setStatus(_A)
_IpMRoute1InterfaceOutMcastOctets_Type=Counter32
_IpMRoute1InterfaceOutMcastOctets_Object=MibTableColumn
ipMRoute1InterfaceOutMcastOctets=_IpMRoute1InterfaceOutMcastOctets_Object((1,3,6,1,3,60,1,1,4,1,6),_IpMRoute1InterfaceOutMcastOctets_Type())
ipMRoute1InterfaceOutMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1InterfaceOutMcastOctets.setStatus(_A)
_IpMRoute1InterfaceHCInMcastOctets_Type=Counter64
_IpMRoute1InterfaceHCInMcastOctets_Object=MibTableColumn
ipMRoute1InterfaceHCInMcastOctets=_IpMRoute1InterfaceHCInMcastOctets_Object((1,3,6,1,3,60,1,1,4,1,7),_IpMRoute1InterfaceHCInMcastOctets_Type())
ipMRoute1InterfaceHCInMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1InterfaceHCInMcastOctets.setStatus(_A)
_IpMRoute1InterfaceHCOutMcastOctets_Type=Counter64
_IpMRoute1InterfaceHCOutMcastOctets_Object=MibTableColumn
ipMRoute1InterfaceHCOutMcastOctets=_IpMRoute1InterfaceHCOutMcastOctets_Object((1,3,6,1,3,60,1,1,4,1,8),_IpMRoute1InterfaceHCOutMcastOctets_Type())
ipMRoute1InterfaceHCOutMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1InterfaceHCOutMcastOctets.setStatus(_A)
_IpMRoute1BoundaryTable_Object=MibTable
ipMRoute1BoundaryTable=_IpMRoute1BoundaryTable_Object((1,3,6,1,3,60,1,1,5))
if mibBuilder.loadTexts:ipMRoute1BoundaryTable.setStatus(_A)
_IpMRoute1BoundaryEntry_Object=MibTableRow
ipMRoute1BoundaryEntry=_IpMRoute1BoundaryEntry_Object((1,3,6,1,3,60,1,1,5,1))
ipMRoute1BoundaryEntry.setIndexNames((0,_B,_S),(0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:ipMRoute1BoundaryEntry.setStatus(_A)
_IpMRoute1BoundaryIfIndex_Type=InterfaceIndex
_IpMRoute1BoundaryIfIndex_Object=MibTableColumn
ipMRoute1BoundaryIfIndex=_IpMRoute1BoundaryIfIndex_Object((1,3,6,1,3,60,1,1,5,1,1),_IpMRoute1BoundaryIfIndex_Type())
ipMRoute1BoundaryIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRoute1BoundaryIfIndex.setStatus(_A)
_IpMRoute1BoundaryAddress_Type=IpAddress
_IpMRoute1BoundaryAddress_Object=MibTableColumn
ipMRoute1BoundaryAddress=_IpMRoute1BoundaryAddress_Object((1,3,6,1,3,60,1,1,5,1,2),_IpMRoute1BoundaryAddress_Type())
ipMRoute1BoundaryAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRoute1BoundaryAddress.setStatus(_A)
_IpMRoute1BoundaryAddressMask_Type=IpAddress
_IpMRoute1BoundaryAddressMask_Object=MibTableColumn
ipMRoute1BoundaryAddressMask=_IpMRoute1BoundaryAddressMask_Object((1,3,6,1,3,60,1,1,5,1,3),_IpMRoute1BoundaryAddressMask_Type())
ipMRoute1BoundaryAddressMask.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRoute1BoundaryAddressMask.setStatus(_A)
_IpMRoute1BoundaryStatus_Type=RowStatus
_IpMRoute1BoundaryStatus_Object=MibTableColumn
ipMRoute1BoundaryStatus=_IpMRoute1BoundaryStatus_Object((1,3,6,1,3,60,1,1,5,1,4),_IpMRoute1BoundaryStatus_Type())
ipMRoute1BoundaryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1BoundaryStatus.setStatus(_A)
_IpMRoute1ScopeNameTable_Object=MibTable
ipMRoute1ScopeNameTable=_IpMRoute1ScopeNameTable_Object((1,3,6,1,3,60,1,1,6))
if mibBuilder.loadTexts:ipMRoute1ScopeNameTable.setStatus(_A)
_IpMRoute1ScopeNameEntry_Object=MibTableRow
ipMRoute1ScopeNameEntry=_IpMRoute1ScopeNameEntry_Object((1,3,6,1,3,60,1,1,6,1))
ipMRoute1ScopeNameEntry.setIndexNames((0,_B,_V),(0,_B,_W),(1,_B,_X))
if mibBuilder.loadTexts:ipMRoute1ScopeNameEntry.setStatus(_A)
_IpMRoute1ScopeNameAddress_Type=IpAddress
_IpMRoute1ScopeNameAddress_Object=MibTableColumn
ipMRoute1ScopeNameAddress=_IpMRoute1ScopeNameAddress_Object((1,3,6,1,3,60,1,1,6,1,1),_IpMRoute1ScopeNameAddress_Type())
ipMRoute1ScopeNameAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRoute1ScopeNameAddress.setStatus(_A)
_IpMRoute1ScopeNameAddressMask_Type=IpAddress
_IpMRoute1ScopeNameAddressMask_Object=MibTableColumn
ipMRoute1ScopeNameAddressMask=_IpMRoute1ScopeNameAddressMask_Object((1,3,6,1,3,60,1,1,6,1,2),_IpMRoute1ScopeNameAddressMask_Type())
ipMRoute1ScopeNameAddressMask.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRoute1ScopeNameAddressMask.setStatus(_A)
class _IpMRoute1ScopeNameLanguage_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,8))
_IpMRoute1ScopeNameLanguage_Type.__name__=_G
_IpMRoute1ScopeNameLanguage_Object=MibTableColumn
ipMRoute1ScopeNameLanguage=_IpMRoute1ScopeNameLanguage_Object((1,3,6,1,3,60,1,1,6,1,3),_IpMRoute1ScopeNameLanguage_Type())
ipMRoute1ScopeNameLanguage.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRoute1ScopeNameLanguage.setStatus(_A)
_IpMRoute1ScopeNameString_Type=SnmpAdminString
_IpMRoute1ScopeNameString_Object=MibTableColumn
ipMRoute1ScopeNameString=_IpMRoute1ScopeNameString_Object((1,3,6,1,3,60,1,1,6,1,4),_IpMRoute1ScopeNameString_Type())
ipMRoute1ScopeNameString.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1ScopeNameString.setStatus(_A)
class _IpMRoute1ScopeNameDefault_Type(TruthValue):defaultValue=2
_IpMRoute1ScopeNameDefault_Type.__name__=_H
_IpMRoute1ScopeNameDefault_Object=MibTableColumn
ipMRoute1ScopeNameDefault=_IpMRoute1ScopeNameDefault_Object((1,3,6,1,3,60,1,1,6,1,5),_IpMRoute1ScopeNameDefault_Type())
ipMRoute1ScopeNameDefault.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1ScopeNameDefault.setStatus(_A)
_IpMRoute1ScopeNameStatus_Type=RowStatus
_IpMRoute1ScopeNameStatus_Object=MibTableColumn
ipMRoute1ScopeNameStatus=_IpMRoute1ScopeNameStatus_Object((1,3,6,1,3,60,1,1,6,1,6),_IpMRoute1ScopeNameStatus_Type())
ipMRoute1ScopeNameStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1ScopeNameStatus.setStatus(_A)
_IpMRoute1EntryCount_Type=Gauge32
_IpMRoute1EntryCount_Object=MibScalar
ipMRoute1EntryCount=_IpMRoute1EntryCount_Object((1,3,6,1,3,60,1,1,7),_IpMRoute1EntryCount_Type())
ipMRoute1EntryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoute1EntryCount.setStatus(_A)
_IpMRoute1MIBConformance_ObjectIdentity=ObjectIdentity
ipMRoute1MIBConformance=_IpMRoute1MIBConformance_ObjectIdentity((1,3,6,1,3,60,2))
_IpMRoute1MIBCompliances_ObjectIdentity=ObjectIdentity
ipMRoute1MIBCompliances=_IpMRoute1MIBCompliances_ObjectIdentity((1,3,6,1,3,60,2,1))
_IpMRoute1MIBGroups_ObjectIdentity=ObjectIdentity
ipMRoute1MIBGroups=_IpMRoute1MIBGroups_ObjectIdentity((1,3,6,1,3,60,2,2))
ipMRoute1MIBBasicGroup=ObjectGroup((1,3,6,1,3,60,2,2,1))
ipMRoute1MIBBasicGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_F),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:ipMRoute1MIBBasicGroup.setStatus(_A)
ipMRoute1MIBHopCountGroup=ObjectGroup((1,3,6,1,3,60,2,2,2))
ipMRoute1MIBHopCountGroup.setObjects((_B,_o))
if mibBuilder.loadTexts:ipMRoute1MIBHopCountGroup.setStatus(_A)
ipMRoute1MIBBoundaryGroup=ObjectGroup((1,3,6,1,3,60,2,2,3))
ipMRoute1MIBBoundaryGroup.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:ipMRoute1MIBBoundaryGroup.setStatus(_A)
ipMRoute1MIBPktsOutGroup=ObjectGroup((1,3,6,1,3,60,2,2,4))
ipMRoute1MIBPktsOutGroup.setObjects((_B,_F))
if mibBuilder.loadTexts:ipMRoute1MIBPktsOutGroup.setStatus(_A)
ipMRoute1MIBHCInterfaceGroup=ObjectGroup((1,3,6,1,3,60,2,2,5))
ipMRoute1MIBHCInterfaceGroup.setObjects(*((_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:ipMRoute1MIBHCInterfaceGroup.setStatus(_A)
ipMRoute1MIBRouteGroup=ObjectGroup((1,3,6,1,3,60,2,2,6))
ipMRoute1MIBRouteGroup.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:ipMRoute1MIBRouteGroup.setStatus(_A)
ipMRoute1MIBPktsGroup=ObjectGroup((1,3,6,1,3,60,2,2,7))
ipMRoute1MIBPktsGroup.setObjects(*((_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:ipMRoute1MIBPktsGroup.setStatus(_A)
ipMRoute1MIBCompliance=ModuleCompliance((1,3,6,1,3,60,2,1,1))
ipMRoute1MIBCompliance.setObjects(*((_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:ipMRoute1MIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'IpMRoute1Protocol':IpMRoute1Protocol,'ipMRoute1MIB':ipMRoute1MIB,'ipMRoute1MIBObjects':ipMRoute1MIBObjects,'ipMRoute1':ipMRoute1,_Y:ipMRoute1Enable,'ipMRoute1Table':ipMRoute1Table,'ipMRoute1Entry':ipMRoute1Entry,_J:ipMRoute1Group,_K:ipMRoute1Source,_L:ipMRoute1SourceMask,_a:ipMRoute1UpstreamNeighbor,_b:ipMRoute1InIfIndex,_c:ipMRoute1UpTime,_d:ipMRoute1ExpiryTime,_A0:ipMRoute1Pkts,_A1:ipMRoute1DifferentInIfPackets,_A2:ipMRoute1Octets,_n:ipMRoute1Protocol,_w:ipMRoute1RtProto,_x:ipMRoute1RtAddress,_y:ipMRoute1RtMask,_z:ipMRoute1RtType,_v:ipMRoute1HCOctets,'ipMRoute1NextHopTable':ipMRoute1NextHopTable,'ipMRoute1NextHopEntry':ipMRoute1NextHopEntry,_M:ipMRoute1NextHopGroup,_N:ipMRoute1NextHopSource,_O:ipMRoute1NextHopSourceMask,_P:ipMRoute1NextHopIfIndex,_Q:ipMRoute1NextHopAddress,_e:ipMRoute1NextHopState,_f:ipMRoute1NextHopUpTime,_g:ipMRoute1NextHopExpiryTime,_o:ipMRoute1NextHopClosestMemberHops,_h:ipMRoute1NextHopProtocol,_F:ipMRoute1NextHopPkts,'ipMRoute1InterfaceTable':ipMRoute1InterfaceTable,'ipMRoute1InterfaceEntry':ipMRoute1InterfaceEntry,_R:ipMRoute1InterfaceIfIndex,_i:ipMRoute1InterfaceTtl,_j:ipMRoute1InterfaceProtocol,_k:ipMRoute1InterfaceRateLimit,_l:ipMRoute1InterfaceInMcastOctets,_m:ipMRoute1InterfaceOutMcastOctets,_t:ipMRoute1InterfaceHCInMcastOctets,_u:ipMRoute1InterfaceHCOutMcastOctets,'ipMRoute1BoundaryTable':ipMRoute1BoundaryTable,'ipMRoute1BoundaryEntry':ipMRoute1BoundaryEntry,_S:ipMRoute1BoundaryIfIndex,_T:ipMRoute1BoundaryAddress,_U:ipMRoute1BoundaryAddressMask,_p:ipMRoute1BoundaryStatus,'ipMRoute1ScopeNameTable':ipMRoute1ScopeNameTable,'ipMRoute1ScopeNameEntry':ipMRoute1ScopeNameEntry,_V:ipMRoute1ScopeNameAddress,_W:ipMRoute1ScopeNameAddressMask,_X:ipMRoute1ScopeNameLanguage,_q:ipMRoute1ScopeNameString,_r:ipMRoute1ScopeNameDefault,_s:ipMRoute1ScopeNameStatus,_Z:ipMRoute1EntryCount,'ipMRoute1MIBConformance':ipMRoute1MIBConformance,'ipMRoute1MIBCompliances':ipMRoute1MIBCompliances,'ipMRoute1MIBCompliance':ipMRoute1MIBCompliance,'ipMRoute1MIBGroups':ipMRoute1MIBGroups,_A3:ipMRoute1MIBBasicGroup,'ipMRoute1MIBHopCountGroup':ipMRoute1MIBHopCountGroup,_A5:ipMRoute1MIBBoundaryGroup,'ipMRoute1MIBPktsOutGroup':ipMRoute1MIBPktsOutGroup,_A6:ipMRoute1MIBHCInterfaceGroup,_A4:ipMRoute1MIBRouteGroup,'ipMRoute1MIBPktsGroup':ipMRoute1MIBPktsGroup})