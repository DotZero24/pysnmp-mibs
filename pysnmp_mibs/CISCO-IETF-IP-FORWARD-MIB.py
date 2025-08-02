_AK='cInetForwardCidrRouteGroup'
_AJ='cIpForwardMultiPathGroup'
_AI='cIpForwardCidrRouteGroup'
_AH='cInetCidrRouteStatus'
_AG='cInetCidrRouteMetric5'
_AF='cInetCidrRouteMetric4'
_AE='cInetCidrRouteMetric3'
_AD='cInetCidrRouteMetric2'
_AC='cInetCidrRouteMetric1'
_AB='cInetCidrRouteNextHopAS'
_AA='cInetCidrRouteAge'
_A9='cInetCidrRouteProto'
_A8='cInetCidrRouteType'
_A7='cInetCidrRouteIfIndex'
_A6='cInetCidrRouteDiscards'
_A5='cInetCidrRouteNumber'
_A4='cIpCidrRouteStatus'
_A3='cIpCidrRouteMetric5'
_A2='cIpCidrRouteMetric4'
_A1='cIpCidrRouteMetric3'
_A0='cIpCidrRouteMetric2'
_z='cIpCidrRouteMetric1'
_y='cIpCidrRouteNextHopAS'
_x='cIpCidrRouteInfo'
_w='cIpCidrRouteAge'
_v='cIpCidrRouteProto'
_u='cIpCidrRouteType'
_t='cIpCidrRouteIfIndex'
_s='cIpCidrRouteNumber'
_r='cIpForwardMetric5'
_q='cIpForwardMetric4'
_p='cIpForwardMetric3'
_o='cIpForwardMetric2'
_n='cIpForwardMetric1'
_m='cIpForwardNextHopAS'
_l='cIpForwardInfo'
_k='cIpForwardAge'
_j='cIpForwardType'
_i='cIpForwardIfIndex'
_h='cIpForwardMask'
_g='cIpForwardNumber'
_f='cInetCidrRouteNextHop'
_e='cInetCidrRouteNextHopType'
_d='cInetCidrRoutePfxLen'
_c='cInetCidrRouteDest'
_b='cInetCidrRouteDestType'
_a='cInetCidrRouteInstance'
_Z='reject'
_Y='bbnSpfIgp'
_X='ciscoIgrp'
_W='netmgmt'
_V='IpAddress'
_U='InetAutonomousSystemNumber'
_T='cIpCidrRouteNextHop'
_S='cIpCidrRouteTos'
_R='cIpCidrRouteMask'
_Q='cIpCidrRouteDest'
_P='remote'
_O='cIpForwardNextHop'
_N='cIpForwardPolicy'
_M='cIpForwardProto'
_L='cIpForwardDest'
_K='InetAddress'
_J='local'
_I='other'
_H='not-accessible'
_G='read-only'
_F='obsolete'
_E='deprecated'
_D='current'
_C='read-create'
_B='Integer32'
_A='CISCO-IETF-IP-FORWARD-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
IANAipRouteProtocol,=mibBuilder.importSymbols('IANA-RTPROTO-MIB','IANAipRouteProtocol')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressPrefixLength,InetAddressType,InetAutonomousSystemNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB',_K,'InetAddressPrefixLength','InetAddressType',_U)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,_V,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoIetfIpForward=ModuleIdentity((1,3,6,1,4,1,9,10,85))
_CIpForwardNumber_Type=Gauge32
_CIpForwardNumber_Object=MibScalar
cIpForwardNumber=_CIpForwardNumber_Object((1,3,6,1,4,1,9,10,85,1),_CIpForwardNumber_Type())
cIpForwardNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:cIpForwardNumber.setStatus(_F)
_CIpForwardTable_Object=MibTable
cIpForwardTable=_CIpForwardTable_Object((1,3,6,1,4,1,9,10,85,2))
if mibBuilder.loadTexts:cIpForwardTable.setStatus(_F)
_CIpForwardEntry_Object=MibTableRow
cIpForwardEntry=_CIpForwardEntry_Object((1,3,6,1,4,1,9,10,85,2,1))
cIpForwardEntry.setIndexNames((0,_A,_L),(0,_A,_M),(0,_A,_N),(0,_A,_O))
if mibBuilder.loadTexts:cIpForwardEntry.setStatus(_F)
_CIpForwardDest_Type=IpAddress
_CIpForwardDest_Object=MibTableColumn
cIpForwardDest=_CIpForwardDest_Object((1,3,6,1,4,1,9,10,85,2,1,1),_CIpForwardDest_Type())
cIpForwardDest.setMaxAccess(_G)
if mibBuilder.loadTexts:cIpForwardDest.setStatus(_F)
class _CIpForwardMask_Type(IpAddress):defaultHexValue='00000000'
_CIpForwardMask_Type.__name__=_V
_CIpForwardMask_Object=MibTableColumn
cIpForwardMask=_CIpForwardMask_Object((1,3,6,1,4,1,9,10,85,2,1,2),_CIpForwardMask_Type())
cIpForwardMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpForwardMask.setStatus(_F)
class _CIpForwardPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CIpForwardPolicy_Type.__name__=_B
_CIpForwardPolicy_Object=MibTableColumn
cIpForwardPolicy=_CIpForwardPolicy_Object((1,3,6,1,4,1,9,10,85,2,1,3),_CIpForwardPolicy_Type())
cIpForwardPolicy.setMaxAccess(_G)
if mibBuilder.loadTexts:cIpForwardPolicy.setStatus(_F)
_CIpForwardNextHop_Type=IpAddress
_CIpForwardNextHop_Object=MibTableColumn
cIpForwardNextHop=_CIpForwardNextHop_Object((1,3,6,1,4,1,9,10,85,2,1,4),_CIpForwardNextHop_Type())
cIpForwardNextHop.setMaxAccess(_G)
if mibBuilder.loadTexts:cIpForwardNextHop.setStatus(_F)
class _CIpForwardIfIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CIpForwardIfIndex_Type.__name__=_B
_CIpForwardIfIndex_Object=MibTableColumn
cIpForwardIfIndex=_CIpForwardIfIndex_Object((1,3,6,1,4,1,9,10,85,2,1,5),_CIpForwardIfIndex_Type())
cIpForwardIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpForwardIfIndex.setStatus(_F)
class _CIpForwardType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),('invalid',2),(_J,3),(_P,4)))
_CIpForwardType_Type.__name__=_B
_CIpForwardType_Object=MibTableColumn
cIpForwardType=_CIpForwardType_Object((1,3,6,1,4,1,9,10,85,2,1,6),_CIpForwardType_Type())
cIpForwardType.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpForwardType.setStatus(_F)
class _CIpForwardProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_I,1),(_J,2),(_W,3),('icmp',4),('egp',5),('ggp',6),('hello',7),('rip',8),('is-is',9),('es-is',10),(_X,11),(_Y,12),('ospf',13),('bgp',14),('idpr',15)))
_CIpForwardProto_Type.__name__=_B
_CIpForwardProto_Object=MibTableColumn
cIpForwardProto=_CIpForwardProto_Object((1,3,6,1,4,1,9,10,85,2,1,7),_CIpForwardProto_Type())
cIpForwardProto.setMaxAccess(_G)
if mibBuilder.loadTexts:cIpForwardProto.setStatus(_F)
class _CIpForwardAge_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CIpForwardAge_Type.__name__=_B
_CIpForwardAge_Object=MibTableColumn
cIpForwardAge=_CIpForwardAge_Object((1,3,6,1,4,1,9,10,85,2,1,8),_CIpForwardAge_Type())
cIpForwardAge.setMaxAccess(_G)
if mibBuilder.loadTexts:cIpForwardAge.setStatus(_F)
_CIpForwardInfo_Type=ObjectIdentifier
_CIpForwardInfo_Object=MibTableColumn
cIpForwardInfo=_CIpForwardInfo_Object((1,3,6,1,4,1,9,10,85,2,1,9),_CIpForwardInfo_Type())
cIpForwardInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpForwardInfo.setStatus(_F)
class _CIpForwardNextHopAS_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CIpForwardNextHopAS_Type.__name__=_B
_CIpForwardNextHopAS_Object=MibTableColumn
cIpForwardNextHopAS=_CIpForwardNextHopAS_Object((1,3,6,1,4,1,9,10,85,2,1,10),_CIpForwardNextHopAS_Type())
cIpForwardNextHopAS.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpForwardNextHopAS.setStatus(_F)
class _CIpForwardMetric1_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483647,2147483647))
_CIpForwardMetric1_Type.__name__=_B
_CIpForwardMetric1_Object=MibTableColumn
cIpForwardMetric1=_CIpForwardMetric1_Object((1,3,6,1,4,1,9,10,85,2,1,11),_CIpForwardMetric1_Type())
cIpForwardMetric1.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpForwardMetric1.setStatus(_F)
class _CIpForwardMetric2_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483647,2147483647))
_CIpForwardMetric2_Type.__name__=_B
_CIpForwardMetric2_Object=MibTableColumn
cIpForwardMetric2=_CIpForwardMetric2_Object((1,3,6,1,4,1,9,10,85,2,1,12),_CIpForwardMetric2_Type())
cIpForwardMetric2.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpForwardMetric2.setStatus(_F)
class _CIpForwardMetric3_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483647,2147483647))
_CIpForwardMetric3_Type.__name__=_B
_CIpForwardMetric3_Object=MibTableColumn
cIpForwardMetric3=_CIpForwardMetric3_Object((1,3,6,1,4,1,9,10,85,2,1,13),_CIpForwardMetric3_Type())
cIpForwardMetric3.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpForwardMetric3.setStatus(_F)
class _CIpForwardMetric4_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483647,2147483647))
_CIpForwardMetric4_Type.__name__=_B
_CIpForwardMetric4_Object=MibTableColumn
cIpForwardMetric4=_CIpForwardMetric4_Object((1,3,6,1,4,1,9,10,85,2,1,14),_CIpForwardMetric4_Type())
cIpForwardMetric4.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpForwardMetric4.setStatus(_F)
class _CIpForwardMetric5_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483647,2147483647))
_CIpForwardMetric5_Type.__name__=_B
_CIpForwardMetric5_Object=MibTableColumn
cIpForwardMetric5=_CIpForwardMetric5_Object((1,3,6,1,4,1,9,10,85,2,1,15),_CIpForwardMetric5_Type())
cIpForwardMetric5.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpForwardMetric5.setStatus(_F)
_CIpCidrRouteNumber_Type=Gauge32
_CIpCidrRouteNumber_Object=MibScalar
cIpCidrRouteNumber=_CIpCidrRouteNumber_Object((1,3,6,1,4,1,9,10,85,3),_CIpCidrRouteNumber_Type())
cIpCidrRouteNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:cIpCidrRouteNumber.setStatus(_E)
_CIpCidrRouteTable_Object=MibTable
cIpCidrRouteTable=_CIpCidrRouteTable_Object((1,3,6,1,4,1,9,10,85,4))
if mibBuilder.loadTexts:cIpCidrRouteTable.setStatus(_E)
_CIpCidrRouteEntry_Object=MibTableRow
cIpCidrRouteEntry=_CIpCidrRouteEntry_Object((1,3,6,1,4,1,9,10,85,4,1))
cIpCidrRouteEntry.setIndexNames((0,_A,_Q),(0,_A,_R),(0,_A,_S),(0,_A,_T))
if mibBuilder.loadTexts:cIpCidrRouteEntry.setStatus(_E)
_CIpCidrRouteDest_Type=IpAddress
_CIpCidrRouteDest_Object=MibTableColumn
cIpCidrRouteDest=_CIpCidrRouteDest_Object((1,3,6,1,4,1,9,10,85,4,1,1),_CIpCidrRouteDest_Type())
cIpCidrRouteDest.setMaxAccess(_G)
if mibBuilder.loadTexts:cIpCidrRouteDest.setStatus(_E)
_CIpCidrRouteMask_Type=IpAddress
_CIpCidrRouteMask_Object=MibTableColumn
cIpCidrRouteMask=_CIpCidrRouteMask_Object((1,3,6,1,4,1,9,10,85,4,1,2),_CIpCidrRouteMask_Type())
cIpCidrRouteMask.setMaxAccess(_G)
if mibBuilder.loadTexts:cIpCidrRouteMask.setStatus(_E)
class _CIpCidrRouteTos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CIpCidrRouteTos_Type.__name__=_B
_CIpCidrRouteTos_Object=MibTableColumn
cIpCidrRouteTos=_CIpCidrRouteTos_Object((1,3,6,1,4,1,9,10,85,4,1,3),_CIpCidrRouteTos_Type())
cIpCidrRouteTos.setMaxAccess(_G)
if mibBuilder.loadTexts:cIpCidrRouteTos.setStatus(_E)
_CIpCidrRouteNextHop_Type=IpAddress
_CIpCidrRouteNextHop_Object=MibTableColumn
cIpCidrRouteNextHop=_CIpCidrRouteNextHop_Object((1,3,6,1,4,1,9,10,85,4,1,4),_CIpCidrRouteNextHop_Type())
cIpCidrRouteNextHop.setMaxAccess(_G)
if mibBuilder.loadTexts:cIpCidrRouteNextHop.setStatus(_E)
class _CIpCidrRouteIfIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CIpCidrRouteIfIndex_Type.__name__=_B
_CIpCidrRouteIfIndex_Object=MibTableColumn
cIpCidrRouteIfIndex=_CIpCidrRouteIfIndex_Object((1,3,6,1,4,1,9,10,85,4,1,5),_CIpCidrRouteIfIndex_Type())
cIpCidrRouteIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpCidrRouteIfIndex.setStatus(_E)
class _CIpCidrRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_I,1),(_Z,2),(_J,3),(_P,4)))
_CIpCidrRouteType_Type.__name__=_B
_CIpCidrRouteType_Object=MibTableColumn
cIpCidrRouteType=_CIpCidrRouteType_Object((1,3,6,1,4,1,9,10,85,4,1,6),_CIpCidrRouteType_Type())
cIpCidrRouteType.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpCidrRouteType.setStatus(_E)
class _CIpCidrRouteProto_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*((_I,1),(_J,2),(_W,3),('icmp',4),('egp',5),('ggp',6),('hello',7),('rip',8),('isIs',9),('esIs',10),(_X,11),(_Y,12),('ospf',13),('bgp',14),('idpr',15),('ciscoEigrp',16)))
_CIpCidrRouteProto_Type.__name__=_B
_CIpCidrRouteProto_Object=MibTableColumn
cIpCidrRouteProto=_CIpCidrRouteProto_Object((1,3,6,1,4,1,9,10,85,4,1,7),_CIpCidrRouteProto_Type())
cIpCidrRouteProto.setMaxAccess(_G)
if mibBuilder.loadTexts:cIpCidrRouteProto.setStatus(_E)
class _CIpCidrRouteAge_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CIpCidrRouteAge_Type.__name__=_B
_CIpCidrRouteAge_Object=MibTableColumn
cIpCidrRouteAge=_CIpCidrRouteAge_Object((1,3,6,1,4,1,9,10,85,4,1,8),_CIpCidrRouteAge_Type())
cIpCidrRouteAge.setMaxAccess(_G)
if mibBuilder.loadTexts:cIpCidrRouteAge.setStatus(_E)
_CIpCidrRouteInfo_Type=ObjectIdentifier
_CIpCidrRouteInfo_Object=MibTableColumn
cIpCidrRouteInfo=_CIpCidrRouteInfo_Object((1,3,6,1,4,1,9,10,85,4,1,9),_CIpCidrRouteInfo_Type())
cIpCidrRouteInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpCidrRouteInfo.setStatus(_E)
class _CIpCidrRouteNextHopAS_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CIpCidrRouteNextHopAS_Type.__name__=_B
_CIpCidrRouteNextHopAS_Object=MibTableColumn
cIpCidrRouteNextHopAS=_CIpCidrRouteNextHopAS_Object((1,3,6,1,4,1,9,10,85,4,1,10),_CIpCidrRouteNextHopAS_Type())
cIpCidrRouteNextHopAS.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpCidrRouteNextHopAS.setStatus(_E)
class _CIpCidrRouteMetric1_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483647,2147483647))
_CIpCidrRouteMetric1_Type.__name__=_B
_CIpCidrRouteMetric1_Object=MibTableColumn
cIpCidrRouteMetric1=_CIpCidrRouteMetric1_Object((1,3,6,1,4,1,9,10,85,4,1,11),_CIpCidrRouteMetric1_Type())
cIpCidrRouteMetric1.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpCidrRouteMetric1.setStatus(_E)
class _CIpCidrRouteMetric2_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483647,2147483647))
_CIpCidrRouteMetric2_Type.__name__=_B
_CIpCidrRouteMetric2_Object=MibTableColumn
cIpCidrRouteMetric2=_CIpCidrRouteMetric2_Object((1,3,6,1,4,1,9,10,85,4,1,12),_CIpCidrRouteMetric2_Type())
cIpCidrRouteMetric2.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpCidrRouteMetric2.setStatus(_E)
class _CIpCidrRouteMetric3_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483647,2147483647))
_CIpCidrRouteMetric3_Type.__name__=_B
_CIpCidrRouteMetric3_Object=MibTableColumn
cIpCidrRouteMetric3=_CIpCidrRouteMetric3_Object((1,3,6,1,4,1,9,10,85,4,1,13),_CIpCidrRouteMetric3_Type())
cIpCidrRouteMetric3.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpCidrRouteMetric3.setStatus(_E)
class _CIpCidrRouteMetric4_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483647,2147483647))
_CIpCidrRouteMetric4_Type.__name__=_B
_CIpCidrRouteMetric4_Object=MibTableColumn
cIpCidrRouteMetric4=_CIpCidrRouteMetric4_Object((1,3,6,1,4,1,9,10,85,4,1,14),_CIpCidrRouteMetric4_Type())
cIpCidrRouteMetric4.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpCidrRouteMetric4.setStatus(_E)
class _CIpCidrRouteMetric5_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483647,2147483647))
_CIpCidrRouteMetric5_Type.__name__=_B
_CIpCidrRouteMetric5_Object=MibTableColumn
cIpCidrRouteMetric5=_CIpCidrRouteMetric5_Object((1,3,6,1,4,1,9,10,85,4,1,15),_CIpCidrRouteMetric5_Type())
cIpCidrRouteMetric5.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpCidrRouteMetric5.setStatus(_E)
_CIpCidrRouteStatus_Type=RowStatus
_CIpCidrRouteStatus_Object=MibTableColumn
cIpCidrRouteStatus=_CIpCidrRouteStatus_Object((1,3,6,1,4,1,9,10,85,4,1,16),_CIpCidrRouteStatus_Type())
cIpCidrRouteStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpCidrRouteStatus.setStatus(_E)
_CIpForwardConformance_ObjectIdentity=ObjectIdentity
cIpForwardConformance=_CIpForwardConformance_ObjectIdentity((1,3,6,1,4,1,9,10,85,5))
_CIpForwardGroups_ObjectIdentity=ObjectIdentity
cIpForwardGroups=_CIpForwardGroups_ObjectIdentity((1,3,6,1,4,1,9,10,85,5,1))
_CIpForwardCompliances_ObjectIdentity=ObjectIdentity
cIpForwardCompliances=_CIpForwardCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,85,5,2))
_CInetCidrRouteNumber_Type=Gauge32
_CInetCidrRouteNumber_Object=MibScalar
cInetCidrRouteNumber=_CInetCidrRouteNumber_Object((1,3,6,1,4,1,9,10,85,6),_CInetCidrRouteNumber_Type())
cInetCidrRouteNumber.setMaxAccess(_G)
if mibBuilder.loadTexts:cInetCidrRouteNumber.setStatus(_D)
_CInetCidrRouteTable_Object=MibTable
cInetCidrRouteTable=_CInetCidrRouteTable_Object((1,3,6,1,4,1,9,10,85,7))
if mibBuilder.loadTexts:cInetCidrRouteTable.setStatus(_D)
_CInetCidrRouteEntry_Object=MibTableRow
cInetCidrRouteEntry=_CInetCidrRouteEntry_Object((1,3,6,1,4,1,9,10,85,7,1))
cInetCidrRouteEntry.setIndexNames((0,_A,_a),(0,_A,_b),(0,_A,_c),(0,_A,_d),(0,_A,_e),(0,_A,_f))
if mibBuilder.loadTexts:cInetCidrRouteEntry.setStatus(_D)
_CInetCidrRouteInstance_Type=Unsigned32
_CInetCidrRouteInstance_Object=MibTableColumn
cInetCidrRouteInstance=_CInetCidrRouteInstance_Object((1,3,6,1,4,1,9,10,85,7,1,1),_CInetCidrRouteInstance_Type())
cInetCidrRouteInstance.setMaxAccess(_H)
if mibBuilder.loadTexts:cInetCidrRouteInstance.setStatus(_D)
_CInetCidrRouteDestType_Type=InetAddressType
_CInetCidrRouteDestType_Object=MibTableColumn
cInetCidrRouteDestType=_CInetCidrRouteDestType_Object((1,3,6,1,4,1,9,10,85,7,1,2),_CInetCidrRouteDestType_Type())
cInetCidrRouteDestType.setMaxAccess(_H)
if mibBuilder.loadTexts:cInetCidrRouteDestType.setStatus(_D)
class _CInetCidrRouteDest_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,36))
_CInetCidrRouteDest_Type.__name__=_K
_CInetCidrRouteDest_Object=MibTableColumn
cInetCidrRouteDest=_CInetCidrRouteDest_Object((1,3,6,1,4,1,9,10,85,7,1,3),_CInetCidrRouteDest_Type())
cInetCidrRouteDest.setMaxAccess(_H)
if mibBuilder.loadTexts:cInetCidrRouteDest.setStatus(_D)
_CInetCidrRoutePfxLen_Type=InetAddressPrefixLength
_CInetCidrRoutePfxLen_Object=MibTableColumn
cInetCidrRoutePfxLen=_CInetCidrRoutePfxLen_Object((1,3,6,1,4,1,9,10,85,7,1,4),_CInetCidrRoutePfxLen_Type())
cInetCidrRoutePfxLen.setMaxAccess(_H)
if mibBuilder.loadTexts:cInetCidrRoutePfxLen.setStatus(_D)
_CInetCidrRouteNextHopType_Type=InetAddressType
_CInetCidrRouteNextHopType_Object=MibTableColumn
cInetCidrRouteNextHopType=_CInetCidrRouteNextHopType_Object((1,3,6,1,4,1,9,10,85,7,1,5),_CInetCidrRouteNextHopType_Type())
cInetCidrRouteNextHopType.setMaxAccess(_H)
if mibBuilder.loadTexts:cInetCidrRouteNextHopType.setStatus(_D)
class _CInetCidrRouteNextHop_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,36))
_CInetCidrRouteNextHop_Type.__name__=_K
_CInetCidrRouteNextHop_Object=MibTableColumn
cInetCidrRouteNextHop=_CInetCidrRouteNextHop_Object((1,3,6,1,4,1,9,10,85,7,1,6),_CInetCidrRouteNextHop_Type())
cInetCidrRouteNextHop.setMaxAccess(_H)
if mibBuilder.loadTexts:cInetCidrRouteNextHop.setStatus(_D)
_CInetCidrRouteIfIndex_Type=InterfaceIndex
_CInetCidrRouteIfIndex_Object=MibTableColumn
cInetCidrRouteIfIndex=_CInetCidrRouteIfIndex_Object((1,3,6,1,4,1,9,10,85,7,1,7),_CInetCidrRouteIfIndex_Type())
cInetCidrRouteIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cInetCidrRouteIfIndex.setStatus(_D)
class _CInetCidrRouteType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_I,1),(_Z,2),(_J,3),(_P,4),('blackhole',5)))
_CInetCidrRouteType_Type.__name__=_B
_CInetCidrRouteType_Object=MibTableColumn
cInetCidrRouteType=_CInetCidrRouteType_Object((1,3,6,1,4,1,9,10,85,7,1,8),_CInetCidrRouteType_Type())
cInetCidrRouteType.setMaxAccess(_C)
if mibBuilder.loadTexts:cInetCidrRouteType.setStatus(_D)
_CInetCidrRouteProto_Type=IANAipRouteProtocol
_CInetCidrRouteProto_Object=MibTableColumn
cInetCidrRouteProto=_CInetCidrRouteProto_Object((1,3,6,1,4,1,9,10,85,7,1,9),_CInetCidrRouteProto_Type())
cInetCidrRouteProto.setMaxAccess(_G)
if mibBuilder.loadTexts:cInetCidrRouteProto.setStatus(_D)
class _CInetCidrRouteAge_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CInetCidrRouteAge_Type.__name__=_B
_CInetCidrRouteAge_Object=MibTableColumn
cInetCidrRouteAge=_CInetCidrRouteAge_Object((1,3,6,1,4,1,9,10,85,7,1,10),_CInetCidrRouteAge_Type())
cInetCidrRouteAge.setMaxAccess(_G)
if mibBuilder.loadTexts:cInetCidrRouteAge.setStatus(_D)
class _CInetCidrRouteNextHopAS_Type(InetAutonomousSystemNumber):defaultValue=0
_CInetCidrRouteNextHopAS_Type.__name__=_U
_CInetCidrRouteNextHopAS_Object=MibTableColumn
cInetCidrRouteNextHopAS=_CInetCidrRouteNextHopAS_Object((1,3,6,1,4,1,9,10,85,7,1,11),_CInetCidrRouteNextHopAS_Type())
cInetCidrRouteNextHopAS.setMaxAccess(_C)
if mibBuilder.loadTexts:cInetCidrRouteNextHopAS.setStatus(_D)
class _CInetCidrRouteMetric1_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_CInetCidrRouteMetric1_Type.__name__=_B
_CInetCidrRouteMetric1_Object=MibTableColumn
cInetCidrRouteMetric1=_CInetCidrRouteMetric1_Object((1,3,6,1,4,1,9,10,85,7,1,12),_CInetCidrRouteMetric1_Type())
cInetCidrRouteMetric1.setMaxAccess(_C)
if mibBuilder.loadTexts:cInetCidrRouteMetric1.setStatus(_D)
class _CInetCidrRouteMetric2_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_CInetCidrRouteMetric2_Type.__name__=_B
_CInetCidrRouteMetric2_Object=MibTableColumn
cInetCidrRouteMetric2=_CInetCidrRouteMetric2_Object((1,3,6,1,4,1,9,10,85,7,1,13),_CInetCidrRouteMetric2_Type())
cInetCidrRouteMetric2.setMaxAccess(_C)
if mibBuilder.loadTexts:cInetCidrRouteMetric2.setStatus(_D)
class _CInetCidrRouteMetric3_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_CInetCidrRouteMetric3_Type.__name__=_B
_CInetCidrRouteMetric3_Object=MibTableColumn
cInetCidrRouteMetric3=_CInetCidrRouteMetric3_Object((1,3,6,1,4,1,9,10,85,7,1,14),_CInetCidrRouteMetric3_Type())
cInetCidrRouteMetric3.setMaxAccess(_C)
if mibBuilder.loadTexts:cInetCidrRouteMetric3.setStatus(_D)
class _CInetCidrRouteMetric4_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_CInetCidrRouteMetric4_Type.__name__=_B
_CInetCidrRouteMetric4_Object=MibTableColumn
cInetCidrRouteMetric4=_CInetCidrRouteMetric4_Object((1,3,6,1,4,1,9,10,85,7,1,15),_CInetCidrRouteMetric4_Type())
cInetCidrRouteMetric4.setMaxAccess(_C)
if mibBuilder.loadTexts:cInetCidrRouteMetric4.setStatus(_D)
class _CInetCidrRouteMetric5_Type(Integer32):defaultValue=-1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2147483648,2147483647))
_CInetCidrRouteMetric5_Type.__name__=_B
_CInetCidrRouteMetric5_Object=MibTableColumn
cInetCidrRouteMetric5=_CInetCidrRouteMetric5_Object((1,3,6,1,4,1,9,10,85,7,1,16),_CInetCidrRouteMetric5_Type())
cInetCidrRouteMetric5.setMaxAccess(_C)
if mibBuilder.loadTexts:cInetCidrRouteMetric5.setStatus(_D)
_CInetCidrRouteStatus_Type=RowStatus
_CInetCidrRouteStatus_Object=MibTableColumn
cInetCidrRouteStatus=_CInetCidrRouteStatus_Object((1,3,6,1,4,1,9,10,85,7,1,17),_CInetCidrRouteStatus_Type())
cInetCidrRouteStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cInetCidrRouteStatus.setStatus(_D)
_CInetCidrRouteDiscards_Type=Counter32
_CInetCidrRouteDiscards_Object=MibScalar
cInetCidrRouteDiscards=_CInetCidrRouteDiscards_Object((1,3,6,1,4,1,9,10,85,8),_CInetCidrRouteDiscards_Type())
cInetCidrRouteDiscards.setMaxAccess(_G)
if mibBuilder.loadTexts:cInetCidrRouteDiscards.setStatus(_D)
cIpForwardMultiPathGroup=ObjectGroup((1,3,6,1,4,1,9,10,85,5,1,2))
cIpForwardMultiPathGroup.setObjects(*((_A,_g),(_A,_L),(_A,_h),(_A,_N),(_A,_O),(_A,_i),(_A,_j),(_A,_M),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:cIpForwardMultiPathGroup.setStatus(_F)
cIpForwardCidrRouteGroup=ObjectGroup((1,3,6,1,4,1,9,10,85,5,1,3))
cIpForwardCidrRouteGroup.setObjects(*((_A,_s),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:cIpForwardCidrRouteGroup.setStatus(_E)
cInetForwardCidrRouteGroup=ObjectGroup((1,3,6,1,4,1,9,10,85,5,1,4))
cInetForwardCidrRouteGroup.setObjects(*((_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH)))
if mibBuilder.loadTexts:cInetForwardCidrRouteGroup.setStatus(_D)
cIpForwardCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,85,5,2,1))
cIpForwardCompliance.setObjects((_A,_AI))
if mibBuilder.loadTexts:cIpForwardCompliance.setStatus(_E)
cIpForwardOldCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,85,5,2,2))
cIpForwardOldCompliance.setObjects((_A,_AJ))
if mibBuilder.loadTexts:cIpForwardOldCompliance.setStatus(_F)
cIpForwardCompliance2=ModuleCompliance((1,3,6,1,4,1,9,10,85,5,2,3))
cIpForwardCompliance2.setObjects((_A,_AK))
if mibBuilder.loadTexts:cIpForwardCompliance2.setStatus(_D)
mibBuilder.exportSymbols(_A,**{'ciscoIetfIpForward':ciscoIetfIpForward,_g:cIpForwardNumber,'cIpForwardTable':cIpForwardTable,'cIpForwardEntry':cIpForwardEntry,_L:cIpForwardDest,_h:cIpForwardMask,_N:cIpForwardPolicy,_O:cIpForwardNextHop,_i:cIpForwardIfIndex,_j:cIpForwardType,_M:cIpForwardProto,_k:cIpForwardAge,_l:cIpForwardInfo,_m:cIpForwardNextHopAS,_n:cIpForwardMetric1,_o:cIpForwardMetric2,_p:cIpForwardMetric3,_q:cIpForwardMetric4,_r:cIpForwardMetric5,_s:cIpCidrRouteNumber,'cIpCidrRouteTable':cIpCidrRouteTable,'cIpCidrRouteEntry':cIpCidrRouteEntry,_Q:cIpCidrRouteDest,_R:cIpCidrRouteMask,_S:cIpCidrRouteTos,_T:cIpCidrRouteNextHop,_t:cIpCidrRouteIfIndex,_u:cIpCidrRouteType,_v:cIpCidrRouteProto,_w:cIpCidrRouteAge,_x:cIpCidrRouteInfo,_y:cIpCidrRouteNextHopAS,_z:cIpCidrRouteMetric1,_A0:cIpCidrRouteMetric2,_A1:cIpCidrRouteMetric3,_A2:cIpCidrRouteMetric4,_A3:cIpCidrRouteMetric5,_A4:cIpCidrRouteStatus,'cIpForwardConformance':cIpForwardConformance,'cIpForwardGroups':cIpForwardGroups,_AJ:cIpForwardMultiPathGroup,_AI:cIpForwardCidrRouteGroup,_AK:cInetForwardCidrRouteGroup,'cIpForwardCompliances':cIpForwardCompliances,'cIpForwardCompliance':cIpForwardCompliance,'cIpForwardOldCompliance':cIpForwardOldCompliance,'cIpForwardCompliance2':cIpForwardCompliance2,_A5:cInetCidrRouteNumber,'cInetCidrRouteTable':cInetCidrRouteTable,'cInetCidrRouteEntry':cInetCidrRouteEntry,_a:cInetCidrRouteInstance,_b:cInetCidrRouteDestType,_c:cInetCidrRouteDest,_d:cInetCidrRoutePfxLen,_e:cInetCidrRouteNextHopType,_f:cInetCidrRouteNextHop,_A7:cInetCidrRouteIfIndex,_A8:cInetCidrRouteType,_A9:cInetCidrRouteProto,_AA:cInetCidrRouteAge,_AB:cInetCidrRouteNextHopAS,_AC:cInetCidrRouteMetric1,_AD:cInetCidrRouteMetric2,_AE:cInetCidrRouteMetric3,_AF:cInetCidrRouteMetric4,_AG:cInetCidrRouteMetric5,_AH:cInetCidrRouteStatus,_A6:cInetCidrRouteDiscards})