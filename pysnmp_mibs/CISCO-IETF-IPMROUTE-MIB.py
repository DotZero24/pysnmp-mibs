_AM='cIpMRouteMIBHCInterfaceGroupSup1'
_AL='cIpMRouteInterfaceHCOutMPkts'
_AK='cIpMRouteInterfaceHCInMPkts'
_AJ='cIpMRouteOctets'
_AI='cIpMRouteDifferentInIfPackets'
_AH='cIpMRoutePkts'
_AG='cIpMRouteRtType'
_AF='cIpMRouteRtMask'
_AE='cIpMRouteRtAddress'
_AD='cIpMRouteRtProto'
_AC='cIpMRouteHCOctets'
_AB='cIpMRouteInterfaceHCOutMOctets'
_AA='cIpMRouteInterfaceHCInMOctets'
_A9='cIpMRouteNextHopPkts'
_A8='cIpMRouteBoundaryNameString'
_A7='cIpMRouteScopeNameStatus'
_A6='cIpMRouteScopeNameDefault'
_A5='cIpMRouteScopeNameString'
_A4='cIpMRouteBoundaryStatus'
_A3='cIpMRouteNextHopClosestHops'
_A2='cIpMRouteProtocol'
_A1='cIpMRouteInterfaceOutMcastOctets'
_A0='cIpMRouteInterfaceInMcastOctets'
_z='cIpMRouteInterfaceOutMcastPkts'
_y='cIpMRouteInterfaceInMcastPkts'
_x='cIpMRouteInterfaceRateLimit'
_w='cIpMRouteInterfaceProtocol'
_v='cIpMRouteInterfaceTtl'
_u='cIpMRouteNextHopProtocol'
_t='cIpMRouteNextHopExpiryTime'
_s='cIpMRouteNextHopUpTime'
_r='cIpMRouteNextHopState'
_q='cIpMRouteExpiryTime'
_p='cIpMRouteUpTime'
_o='cIpMRouteInIfIndex'
_n='cIpMRouteUpstreamNeighbor'
_m='cIpMRouteEntryCount'
_l='cIpMRouteEnable'
_k='cIpMRouteScopeNameLanguage'
_j='cIpMRouteScopeNameAddressMask'
_i='cIpMRouteScopeNameAddress'
_h='cIpMRouteScopeNameAddressType'
_g='cIpMRouteBoundaryAddressMask'
_f='cIpMRouteBoundaryAddress'
_e='cIpMRouteBoundaryAddressType'
_d='cIpMRouteBoundaryIfIndex'
_c='cIpMRouteBoundaryScopeId'
_b='cIpMRouteInterfaceIPVersion'
_a='cIpMRouteInterfaceIfIndex'
_Z='cIpMRouteNextHopAddress'
_Y='cIpMRouteNextHopIfIndex'
_X='cIpMRouteNextHopSourceMask'
_W='cIpMRouteNextHopSource'
_V='cIpMRouteNextHopGroup'
_U='cIpMRouteNextHopAddrType'
_T='cIpMRouteSourceMask'
_S='cIpMRouteSource'
_R='cIpMRouteGroup'
_Q='cIpMRouteAddrType'
_P='TruthValue'
_O='cIpMRouteMIBPktsGroup'
_N='cIpMRouteMIBPktsOutGroup'
_M='cIpMRouteMIBHopCountGroup'
_L='cIpMRouteMIBHCInterfaceGroup'
_K='cIpMRouteMIBBoundaryGroup'
_J='cIpMRouteMIBRouteGroup'
_I='cIpMRouteMIBBasicGroup'
_H='read-write'
_G='read-create'
_F='Integer32'
_E='InetAddress'
_D='not-accessible'
_C='read-only'
_B='CISCO-IETF-IPMROUTE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
IANAipMRouteProtocol,IANAipRouteProtocol=mibBuilder.importSymbols('IANA-RTPROTO-MIB','IANAipMRouteProtocol','IANAipRouteProtocol')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddress,InetAddressPrefixLength,InetAddressType,InetVersion=mibBuilder.importSymbols('INET-ADDRESS-MIB',_E,'InetAddressPrefixLength','InetAddressType','InetVersion')
LanguageTag,=mibBuilder.importSymbols('IPMROUTE-STD-MIB','LanguageTag')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_P)
ciscoIetfIpMRouteMIB=ModuleIdentity((1,3,6,1,4,1,9,10,117))
if mibBuilder.loadTexts:ciscoIetfIpMRouteMIB.setRevisions(('2006-08-24 00:00','2004-12-02 00:00'))
_CIpMRouteMIBObjects_ObjectIdentity=ObjectIdentity
cIpMRouteMIBObjects=_CIpMRouteMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,10,117,1))
_CIpMRoute_ObjectIdentity=ObjectIdentity
cIpMRoute=_CIpMRoute_ObjectIdentity((1,3,6,1,4,1,9,10,117,1,1))
class _CIpMRouteEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_CIpMRouteEnable_Type.__name__=_F
_CIpMRouteEnable_Object=MibScalar
cIpMRouteEnable=_CIpMRouteEnable_Object((1,3,6,1,4,1,9,10,117,1,1,1),_CIpMRouteEnable_Type())
cIpMRouteEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:cIpMRouteEnable.setStatus(_A)
_CIpMRouteTable_Object=MibTable
cIpMRouteTable=_CIpMRouteTable_Object((1,3,6,1,4,1,9,10,117,1,1,2))
if mibBuilder.loadTexts:cIpMRouteTable.setStatus(_A)
_CIpMRouteEntry_Object=MibTableRow
cIpMRouteEntry=_CIpMRouteEntry_Object((1,3,6,1,4,1,9,10,117,1,1,2,1))
cIpMRouteEntry.setIndexNames((0,_B,_Q),(0,_B,_R),(0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:cIpMRouteEntry.setStatus(_A)
_CIpMRouteAddrType_Type=InetAddressType
_CIpMRouteAddrType_Object=MibTableColumn
cIpMRouteAddrType=_CIpMRouteAddrType_Object((1,3,6,1,4,1,9,10,117,1,1,2,1,1),_CIpMRouteAddrType_Type())
cIpMRouteAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpMRouteAddrType.setStatus(_A)
class _CIpMRouteGroup_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CIpMRouteGroup_Type.__name__=_E
_CIpMRouteGroup_Object=MibTableColumn
cIpMRouteGroup=_CIpMRouteGroup_Object((1,3,6,1,4,1,9,10,117,1,1,2,1,2),_CIpMRouteGroup_Type())
cIpMRouteGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpMRouteGroup.setStatus(_A)
class _CIpMRouteSource_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CIpMRouteSource_Type.__name__=_E
_CIpMRouteSource_Object=MibTableColumn
cIpMRouteSource=_CIpMRouteSource_Object((1,3,6,1,4,1,9,10,117,1,1,2,1,3),_CIpMRouteSource_Type())
cIpMRouteSource.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpMRouteSource.setStatus(_A)
_CIpMRouteSourceMask_Type=InetAddressPrefixLength
_CIpMRouteSourceMask_Object=MibTableColumn
cIpMRouteSourceMask=_CIpMRouteSourceMask_Object((1,3,6,1,4,1,9,10,117,1,1,2,1,4),_CIpMRouteSourceMask_Type())
cIpMRouteSourceMask.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpMRouteSourceMask.setStatus(_A)
class _CIpMRouteUpstreamNeighbor_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CIpMRouteUpstreamNeighbor_Type.__name__=_E
_CIpMRouteUpstreamNeighbor_Object=MibTableColumn
cIpMRouteUpstreamNeighbor=_CIpMRouteUpstreamNeighbor_Object((1,3,6,1,4,1,9,10,117,1,1,2,1,5),_CIpMRouteUpstreamNeighbor_Type())
cIpMRouteUpstreamNeighbor.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteUpstreamNeighbor.setStatus(_A)
_CIpMRouteInIfIndex_Type=InterfaceIndexOrZero
_CIpMRouteInIfIndex_Object=MibTableColumn
cIpMRouteInIfIndex=_CIpMRouteInIfIndex_Object((1,3,6,1,4,1,9,10,117,1,1,2,1,6),_CIpMRouteInIfIndex_Type())
cIpMRouteInIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteInIfIndex.setStatus(_A)
_CIpMRouteUpTime_Type=TimeTicks
_CIpMRouteUpTime_Object=MibTableColumn
cIpMRouteUpTime=_CIpMRouteUpTime_Object((1,3,6,1,4,1,9,10,117,1,1,2,1,7),_CIpMRouteUpTime_Type())
cIpMRouteUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteUpTime.setStatus(_A)
_CIpMRouteExpiryTime_Type=TimeTicks
_CIpMRouteExpiryTime_Object=MibTableColumn
cIpMRouteExpiryTime=_CIpMRouteExpiryTime_Object((1,3,6,1,4,1,9,10,117,1,1,2,1,8),_CIpMRouteExpiryTime_Type())
cIpMRouteExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteExpiryTime.setStatus(_A)
_CIpMRoutePkts_Type=Counter32
_CIpMRoutePkts_Object=MibTableColumn
cIpMRoutePkts=_CIpMRoutePkts_Object((1,3,6,1,4,1,9,10,117,1,1,2,1,9),_CIpMRoutePkts_Type())
cIpMRoutePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRoutePkts.setStatus(_A)
_CIpMRouteDifferentInIfPackets_Type=Counter32
_CIpMRouteDifferentInIfPackets_Object=MibTableColumn
cIpMRouteDifferentInIfPackets=_CIpMRouteDifferentInIfPackets_Object((1,3,6,1,4,1,9,10,117,1,1,2,1,10),_CIpMRouteDifferentInIfPackets_Type())
cIpMRouteDifferentInIfPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteDifferentInIfPackets.setStatus(_A)
_CIpMRouteOctets_Type=Counter32
_CIpMRouteOctets_Object=MibTableColumn
cIpMRouteOctets=_CIpMRouteOctets_Object((1,3,6,1,4,1,9,10,117,1,1,2,1,11),_CIpMRouteOctets_Type())
cIpMRouteOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteOctets.setStatus(_A)
_CIpMRouteProtocol_Type=IANAipMRouteProtocol
_CIpMRouteProtocol_Object=MibTableColumn
cIpMRouteProtocol=_CIpMRouteProtocol_Object((1,3,6,1,4,1,9,10,117,1,1,2,1,12),_CIpMRouteProtocol_Type())
cIpMRouteProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteProtocol.setStatus(_A)
_CIpMRouteRtProto_Type=IANAipRouteProtocol
_CIpMRouteRtProto_Object=MibTableColumn
cIpMRouteRtProto=_CIpMRouteRtProto_Object((1,3,6,1,4,1,9,10,117,1,1,2,1,13),_CIpMRouteRtProto_Type())
cIpMRouteRtProto.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteRtProto.setStatus(_A)
class _CIpMRouteRtAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CIpMRouteRtAddress_Type.__name__=_E
_CIpMRouteRtAddress_Object=MibTableColumn
cIpMRouteRtAddress=_CIpMRouteRtAddress_Object((1,3,6,1,4,1,9,10,117,1,1,2,1,14),_CIpMRouteRtAddress_Type())
cIpMRouteRtAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteRtAddress.setStatus(_A)
_CIpMRouteRtMask_Type=InetAddressPrefixLength
_CIpMRouteRtMask_Object=MibTableColumn
cIpMRouteRtMask=_CIpMRouteRtMask_Object((1,3,6,1,4,1,9,10,117,1,1,2,1,15),_CIpMRouteRtMask_Type())
cIpMRouteRtMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteRtMask.setStatus(_A)
class _CIpMRouteRtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unicast',1),('multicast',2)))
_CIpMRouteRtType_Type.__name__=_F
_CIpMRouteRtType_Object=MibTableColumn
cIpMRouteRtType=_CIpMRouteRtType_Object((1,3,6,1,4,1,9,10,117,1,1,2,1,16),_CIpMRouteRtType_Type())
cIpMRouteRtType.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteRtType.setStatus(_A)
_CIpMRouteHCOctets_Type=Counter64
_CIpMRouteHCOctets_Object=MibTableColumn
cIpMRouteHCOctets=_CIpMRouteHCOctets_Object((1,3,6,1,4,1,9,10,117,1,1,2,1,17),_CIpMRouteHCOctets_Type())
cIpMRouteHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteHCOctets.setStatus(_A)
_CIpMRouteNextHopTable_Object=MibTable
cIpMRouteNextHopTable=_CIpMRouteNextHopTable_Object((1,3,6,1,4,1,9,10,117,1,1,3))
if mibBuilder.loadTexts:cIpMRouteNextHopTable.setStatus(_A)
_CIpMRouteNextHopEntry_Object=MibTableRow
cIpMRouteNextHopEntry=_CIpMRouteNextHopEntry_Object((1,3,6,1,4,1,9,10,117,1,1,3,1))
cIpMRouteNextHopEntry.setIndexNames((0,_B,_U),(0,_B,_V),(0,_B,_W),(0,_B,_X),(0,_B,_Y),(0,_B,_Z))
if mibBuilder.loadTexts:cIpMRouteNextHopEntry.setStatus(_A)
_CIpMRouteNextHopAddrType_Type=InetAddressType
_CIpMRouteNextHopAddrType_Object=MibTableColumn
cIpMRouteNextHopAddrType=_CIpMRouteNextHopAddrType_Object((1,3,6,1,4,1,9,10,117,1,1,3,1,1),_CIpMRouteNextHopAddrType_Type())
cIpMRouteNextHopAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpMRouteNextHopAddrType.setStatus(_A)
class _CIpMRouteNextHopGroup_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CIpMRouteNextHopGroup_Type.__name__=_E
_CIpMRouteNextHopGroup_Object=MibTableColumn
cIpMRouteNextHopGroup=_CIpMRouteNextHopGroup_Object((1,3,6,1,4,1,9,10,117,1,1,3,1,2),_CIpMRouteNextHopGroup_Type())
cIpMRouteNextHopGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpMRouteNextHopGroup.setStatus(_A)
class _CIpMRouteNextHopSource_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CIpMRouteNextHopSource_Type.__name__=_E
_CIpMRouteNextHopSource_Object=MibTableColumn
cIpMRouteNextHopSource=_CIpMRouteNextHopSource_Object((1,3,6,1,4,1,9,10,117,1,1,3,1,3),_CIpMRouteNextHopSource_Type())
cIpMRouteNextHopSource.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpMRouteNextHopSource.setStatus(_A)
_CIpMRouteNextHopSourceMask_Type=InetAddressPrefixLength
_CIpMRouteNextHopSourceMask_Object=MibTableColumn
cIpMRouteNextHopSourceMask=_CIpMRouteNextHopSourceMask_Object((1,3,6,1,4,1,9,10,117,1,1,3,1,4),_CIpMRouteNextHopSourceMask_Type())
cIpMRouteNextHopSourceMask.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpMRouteNextHopSourceMask.setStatus(_A)
_CIpMRouteNextHopIfIndex_Type=InterfaceIndex
_CIpMRouteNextHopIfIndex_Object=MibTableColumn
cIpMRouteNextHopIfIndex=_CIpMRouteNextHopIfIndex_Object((1,3,6,1,4,1,9,10,117,1,1,3,1,5),_CIpMRouteNextHopIfIndex_Type())
cIpMRouteNextHopIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpMRouteNextHopIfIndex.setStatus(_A)
class _CIpMRouteNextHopAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CIpMRouteNextHopAddress_Type.__name__=_E
_CIpMRouteNextHopAddress_Object=MibTableColumn
cIpMRouteNextHopAddress=_CIpMRouteNextHopAddress_Object((1,3,6,1,4,1,9,10,117,1,1,3,1,6),_CIpMRouteNextHopAddress_Type())
cIpMRouteNextHopAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpMRouteNextHopAddress.setStatus(_A)
class _CIpMRouteNextHopState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pruned',1),('forwarding',2)))
_CIpMRouteNextHopState_Type.__name__=_F
_CIpMRouteNextHopState_Object=MibTableColumn
cIpMRouteNextHopState=_CIpMRouteNextHopState_Object((1,3,6,1,4,1,9,10,117,1,1,3,1,7),_CIpMRouteNextHopState_Type())
cIpMRouteNextHopState.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteNextHopState.setStatus(_A)
_CIpMRouteNextHopUpTime_Type=TimeTicks
_CIpMRouteNextHopUpTime_Object=MibTableColumn
cIpMRouteNextHopUpTime=_CIpMRouteNextHopUpTime_Object((1,3,6,1,4,1,9,10,117,1,1,3,1,8),_CIpMRouteNextHopUpTime_Type())
cIpMRouteNextHopUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteNextHopUpTime.setStatus(_A)
_CIpMRouteNextHopExpiryTime_Type=TimeTicks
_CIpMRouteNextHopExpiryTime_Object=MibTableColumn
cIpMRouteNextHopExpiryTime=_CIpMRouteNextHopExpiryTime_Object((1,3,6,1,4,1,9,10,117,1,1,3,1,9),_CIpMRouteNextHopExpiryTime_Type())
cIpMRouteNextHopExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteNextHopExpiryTime.setStatus(_A)
class _CIpMRouteNextHopClosestHops_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CIpMRouteNextHopClosestHops_Type.__name__=_F
_CIpMRouteNextHopClosestHops_Object=MibTableColumn
cIpMRouteNextHopClosestHops=_CIpMRouteNextHopClosestHops_Object((1,3,6,1,4,1,9,10,117,1,1,3,1,10),_CIpMRouteNextHopClosestHops_Type())
cIpMRouteNextHopClosestHops.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteNextHopClosestHops.setStatus(_A)
_CIpMRouteNextHopProtocol_Type=IANAipMRouteProtocol
_CIpMRouteNextHopProtocol_Object=MibTableColumn
cIpMRouteNextHopProtocol=_CIpMRouteNextHopProtocol_Object((1,3,6,1,4,1,9,10,117,1,1,3,1,11),_CIpMRouteNextHopProtocol_Type())
cIpMRouteNextHopProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteNextHopProtocol.setStatus(_A)
_CIpMRouteNextHopPkts_Type=Counter32
_CIpMRouteNextHopPkts_Object=MibTableColumn
cIpMRouteNextHopPkts=_CIpMRouteNextHopPkts_Object((1,3,6,1,4,1,9,10,117,1,1,3,1,12),_CIpMRouteNextHopPkts_Type())
cIpMRouteNextHopPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteNextHopPkts.setStatus(_A)
_CIpMRouteInterfaceTable_Object=MibTable
cIpMRouteInterfaceTable=_CIpMRouteInterfaceTable_Object((1,3,6,1,4,1,9,10,117,1,1,4))
if mibBuilder.loadTexts:cIpMRouteInterfaceTable.setStatus(_A)
_CIpMRouteInterfaceEntry_Object=MibTableRow
cIpMRouteInterfaceEntry=_CIpMRouteInterfaceEntry_Object((1,3,6,1,4,1,9,10,117,1,1,4,1))
cIpMRouteInterfaceEntry.setIndexNames((0,_B,_a),(0,_B,_b))
if mibBuilder.loadTexts:cIpMRouteInterfaceEntry.setStatus(_A)
_CIpMRouteInterfaceIfIndex_Type=InterfaceIndex
_CIpMRouteInterfaceIfIndex_Object=MibTableColumn
cIpMRouteInterfaceIfIndex=_CIpMRouteInterfaceIfIndex_Object((1,3,6,1,4,1,9,10,117,1,1,4,1,1),_CIpMRouteInterfaceIfIndex_Type())
cIpMRouteInterfaceIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpMRouteInterfaceIfIndex.setStatus(_A)
_CIpMRouteInterfaceIPVersion_Type=InetVersion
_CIpMRouteInterfaceIPVersion_Object=MibTableColumn
cIpMRouteInterfaceIPVersion=_CIpMRouteInterfaceIPVersion_Object((1,3,6,1,4,1,9,10,117,1,1,4,1,2),_CIpMRouteInterfaceIPVersion_Type())
cIpMRouteInterfaceIPVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpMRouteInterfaceIPVersion.setStatus(_A)
class _CIpMRouteInterfaceTtl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CIpMRouteInterfaceTtl_Type.__name__=_F
_CIpMRouteInterfaceTtl_Object=MibTableColumn
cIpMRouteInterfaceTtl=_CIpMRouteInterfaceTtl_Object((1,3,6,1,4,1,9,10,117,1,1,4,1,3),_CIpMRouteInterfaceTtl_Type())
cIpMRouteInterfaceTtl.setMaxAccess(_H)
if mibBuilder.loadTexts:cIpMRouteInterfaceTtl.setStatus(_A)
_CIpMRouteInterfaceProtocol_Type=IANAipMRouteProtocol
_CIpMRouteInterfaceProtocol_Object=MibTableColumn
cIpMRouteInterfaceProtocol=_CIpMRouteInterfaceProtocol_Object((1,3,6,1,4,1,9,10,117,1,1,4,1,4),_CIpMRouteInterfaceProtocol_Type())
cIpMRouteInterfaceProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteInterfaceProtocol.setStatus(_A)
class _CIpMRouteInterfaceRateLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,429496295))
_CIpMRouteInterfaceRateLimit_Type.__name__=_F
_CIpMRouteInterfaceRateLimit_Object=MibTableColumn
cIpMRouteInterfaceRateLimit=_CIpMRouteInterfaceRateLimit_Object((1,3,6,1,4,1,9,10,117,1,1,4,1,5),_CIpMRouteInterfaceRateLimit_Type())
cIpMRouteInterfaceRateLimit.setMaxAccess(_H)
if mibBuilder.loadTexts:cIpMRouteInterfaceRateLimit.setStatus(_A)
_CIpMRouteInterfaceInMcastPkts_Type=Counter32
_CIpMRouteInterfaceInMcastPkts_Object=MibTableColumn
cIpMRouteInterfaceInMcastPkts=_CIpMRouteInterfaceInMcastPkts_Object((1,3,6,1,4,1,9,10,117,1,1,4,1,6),_CIpMRouteInterfaceInMcastPkts_Type())
cIpMRouteInterfaceInMcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteInterfaceInMcastPkts.setStatus(_A)
_CIpMRouteInterfaceOutMcastPkts_Type=Counter32
_CIpMRouteInterfaceOutMcastPkts_Object=MibTableColumn
cIpMRouteInterfaceOutMcastPkts=_CIpMRouteInterfaceOutMcastPkts_Object((1,3,6,1,4,1,9,10,117,1,1,4,1,7),_CIpMRouteInterfaceOutMcastPkts_Type())
cIpMRouteInterfaceOutMcastPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteInterfaceOutMcastPkts.setStatus(_A)
_CIpMRouteInterfaceInMcastOctets_Type=Counter32
_CIpMRouteInterfaceInMcastOctets_Object=MibTableColumn
cIpMRouteInterfaceInMcastOctets=_CIpMRouteInterfaceInMcastOctets_Object((1,3,6,1,4,1,9,10,117,1,1,4,1,8),_CIpMRouteInterfaceInMcastOctets_Type())
cIpMRouteInterfaceInMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteInterfaceInMcastOctets.setStatus(_A)
_CIpMRouteInterfaceOutMcastOctets_Type=Counter32
_CIpMRouteInterfaceOutMcastOctets_Object=MibTableColumn
cIpMRouteInterfaceOutMcastOctets=_CIpMRouteInterfaceOutMcastOctets_Object((1,3,6,1,4,1,9,10,117,1,1,4,1,9),_CIpMRouteInterfaceOutMcastOctets_Type())
cIpMRouteInterfaceOutMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteInterfaceOutMcastOctets.setStatus(_A)
_CIpMRouteInterfaceHCInMOctets_Type=Counter64
_CIpMRouteInterfaceHCInMOctets_Object=MibTableColumn
cIpMRouteInterfaceHCInMOctets=_CIpMRouteInterfaceHCInMOctets_Object((1,3,6,1,4,1,9,10,117,1,1,4,1,10),_CIpMRouteInterfaceHCInMOctets_Type())
cIpMRouteInterfaceHCInMOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteInterfaceHCInMOctets.setStatus(_A)
_CIpMRouteInterfaceHCOutMOctets_Type=Counter64
_CIpMRouteInterfaceHCOutMOctets_Object=MibTableColumn
cIpMRouteInterfaceHCOutMOctets=_CIpMRouteInterfaceHCOutMOctets_Object((1,3,6,1,4,1,9,10,117,1,1,4,1,11),_CIpMRouteInterfaceHCOutMOctets_Type())
cIpMRouteInterfaceHCOutMOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteInterfaceHCOutMOctets.setStatus(_A)
_CIpMRouteInterfaceHCInMPkts_Type=Counter64
_CIpMRouteInterfaceHCInMPkts_Object=MibTableColumn
cIpMRouteInterfaceHCInMPkts=_CIpMRouteInterfaceHCInMPkts_Object((1,3,6,1,4,1,9,10,117,1,1,4,1,12),_CIpMRouteInterfaceHCInMPkts_Type())
cIpMRouteInterfaceHCInMPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteInterfaceHCInMPkts.setStatus(_A)
_CIpMRouteInterfaceHCOutMPkts_Type=Counter64
_CIpMRouteInterfaceHCOutMPkts_Object=MibTableColumn
cIpMRouteInterfaceHCOutMPkts=_CIpMRouteInterfaceHCOutMPkts_Object((1,3,6,1,4,1,9,10,117,1,1,4,1,13),_CIpMRouteInterfaceHCOutMPkts_Type())
cIpMRouteInterfaceHCOutMPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteInterfaceHCOutMPkts.setStatus(_A)
_CIpMRouteBoundaryTable_Object=MibTable
cIpMRouteBoundaryTable=_CIpMRouteBoundaryTable_Object((1,3,6,1,4,1,9,10,117,1,1,5))
if mibBuilder.loadTexts:cIpMRouteBoundaryTable.setStatus(_A)
_CIpMRouteBoundaryEntry_Object=MibTableRow
cIpMRouteBoundaryEntry=_CIpMRouteBoundaryEntry_Object((1,3,6,1,4,1,9,10,117,1,1,5,1))
cIpMRouteBoundaryEntry.setIndexNames((0,_B,_c),(0,_B,_d),(0,_B,_e),(0,_B,_f),(0,_B,_g))
if mibBuilder.loadTexts:cIpMRouteBoundaryEntry.setStatus(_A)
class _CIpMRouteBoundaryScopeId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_CIpMRouteBoundaryScopeId_Type.__name__=_F
_CIpMRouteBoundaryScopeId_Object=MibTableColumn
cIpMRouteBoundaryScopeId=_CIpMRouteBoundaryScopeId_Object((1,3,6,1,4,1,9,10,117,1,1,5,1,1),_CIpMRouteBoundaryScopeId_Type())
cIpMRouteBoundaryScopeId.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpMRouteBoundaryScopeId.setStatus(_A)
_CIpMRouteBoundaryIfIndex_Type=InterfaceIndex
_CIpMRouteBoundaryIfIndex_Object=MibTableColumn
cIpMRouteBoundaryIfIndex=_CIpMRouteBoundaryIfIndex_Object((1,3,6,1,4,1,9,10,117,1,1,5,1,2),_CIpMRouteBoundaryIfIndex_Type())
cIpMRouteBoundaryIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpMRouteBoundaryIfIndex.setStatus(_A)
_CIpMRouteBoundaryAddressType_Type=InetAddressType
_CIpMRouteBoundaryAddressType_Object=MibTableColumn
cIpMRouteBoundaryAddressType=_CIpMRouteBoundaryAddressType_Object((1,3,6,1,4,1,9,10,117,1,1,5,1,3),_CIpMRouteBoundaryAddressType_Type())
cIpMRouteBoundaryAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpMRouteBoundaryAddressType.setStatus(_A)
class _CIpMRouteBoundaryAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CIpMRouteBoundaryAddress_Type.__name__=_E
_CIpMRouteBoundaryAddress_Object=MibTableColumn
cIpMRouteBoundaryAddress=_CIpMRouteBoundaryAddress_Object((1,3,6,1,4,1,9,10,117,1,1,5,1,4),_CIpMRouteBoundaryAddress_Type())
cIpMRouteBoundaryAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpMRouteBoundaryAddress.setStatus(_A)
_CIpMRouteBoundaryAddressMask_Type=InetAddressPrefixLength
_CIpMRouteBoundaryAddressMask_Object=MibTableColumn
cIpMRouteBoundaryAddressMask=_CIpMRouteBoundaryAddressMask_Object((1,3,6,1,4,1,9,10,117,1,1,5,1,5),_CIpMRouteBoundaryAddressMask_Type())
cIpMRouteBoundaryAddressMask.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpMRouteBoundaryAddressMask.setStatus(_A)
_CIpMRouteBoundaryNameString_Type=SnmpAdminString
_CIpMRouteBoundaryNameString_Object=MibTableColumn
cIpMRouteBoundaryNameString=_CIpMRouteBoundaryNameString_Object((1,3,6,1,4,1,9,10,117,1,1,5,1,6),_CIpMRouteBoundaryNameString_Type())
cIpMRouteBoundaryNameString.setMaxAccess(_G)
if mibBuilder.loadTexts:cIpMRouteBoundaryNameString.setStatus(_A)
_CIpMRouteBoundaryStatus_Type=RowStatus
_CIpMRouteBoundaryStatus_Object=MibTableColumn
cIpMRouteBoundaryStatus=_CIpMRouteBoundaryStatus_Object((1,3,6,1,4,1,9,10,117,1,1,5,1,7),_CIpMRouteBoundaryStatus_Type())
cIpMRouteBoundaryStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cIpMRouteBoundaryStatus.setStatus(_A)
_CIpMRouteScopeNameTable_Object=MibTable
cIpMRouteScopeNameTable=_CIpMRouteScopeNameTable_Object((1,3,6,1,4,1,9,10,117,1,1,6))
if mibBuilder.loadTexts:cIpMRouteScopeNameTable.setStatus(_A)
_CIpMRouteScopeNameEntry_Object=MibTableRow
cIpMRouteScopeNameEntry=_CIpMRouteScopeNameEntry_Object((1,3,6,1,4,1,9,10,117,1,1,6,1))
cIpMRouteScopeNameEntry.setIndexNames((0,_B,_h),(0,_B,_i),(0,_B,_j),(1,_B,_k))
if mibBuilder.loadTexts:cIpMRouteScopeNameEntry.setStatus(_A)
_CIpMRouteScopeNameAddressType_Type=InetAddressType
_CIpMRouteScopeNameAddressType_Object=MibTableColumn
cIpMRouteScopeNameAddressType=_CIpMRouteScopeNameAddressType_Object((1,3,6,1,4,1,9,10,117,1,1,6,1,1),_CIpMRouteScopeNameAddressType_Type())
cIpMRouteScopeNameAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpMRouteScopeNameAddressType.setStatus(_A)
class _CIpMRouteScopeNameAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16),ValueSizeConstraint(20,20))
_CIpMRouteScopeNameAddress_Type.__name__=_E
_CIpMRouteScopeNameAddress_Object=MibTableColumn
cIpMRouteScopeNameAddress=_CIpMRouteScopeNameAddress_Object((1,3,6,1,4,1,9,10,117,1,1,6,1,2),_CIpMRouteScopeNameAddress_Type())
cIpMRouteScopeNameAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpMRouteScopeNameAddress.setStatus(_A)
_CIpMRouteScopeNameAddressMask_Type=InetAddressPrefixLength
_CIpMRouteScopeNameAddressMask_Object=MibTableColumn
cIpMRouteScopeNameAddressMask=_CIpMRouteScopeNameAddressMask_Object((1,3,6,1,4,1,9,10,117,1,1,6,1,3),_CIpMRouteScopeNameAddressMask_Type())
cIpMRouteScopeNameAddressMask.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpMRouteScopeNameAddressMask.setStatus(_A)
_CIpMRouteScopeNameLanguage_Type=LanguageTag
_CIpMRouteScopeNameLanguage_Object=MibTableColumn
cIpMRouteScopeNameLanguage=_CIpMRouteScopeNameLanguage_Object((1,3,6,1,4,1,9,10,117,1,1,6,1,4),_CIpMRouteScopeNameLanguage_Type())
cIpMRouteScopeNameLanguage.setMaxAccess(_D)
if mibBuilder.loadTexts:cIpMRouteScopeNameLanguage.setStatus(_A)
_CIpMRouteScopeNameString_Type=SnmpAdminString
_CIpMRouteScopeNameString_Object=MibTableColumn
cIpMRouteScopeNameString=_CIpMRouteScopeNameString_Object((1,3,6,1,4,1,9,10,117,1,1,6,1,5),_CIpMRouteScopeNameString_Type())
cIpMRouteScopeNameString.setMaxAccess(_G)
if mibBuilder.loadTexts:cIpMRouteScopeNameString.setStatus(_A)
class _CIpMRouteScopeNameDefault_Type(TruthValue):defaultValue=2
_CIpMRouteScopeNameDefault_Type.__name__=_P
_CIpMRouteScopeNameDefault_Object=MibTableColumn
cIpMRouteScopeNameDefault=_CIpMRouteScopeNameDefault_Object((1,3,6,1,4,1,9,10,117,1,1,6,1,6),_CIpMRouteScopeNameDefault_Type())
cIpMRouteScopeNameDefault.setMaxAccess(_G)
if mibBuilder.loadTexts:cIpMRouteScopeNameDefault.setStatus(_A)
_CIpMRouteScopeNameStatus_Type=RowStatus
_CIpMRouteScopeNameStatus_Object=MibTableColumn
cIpMRouteScopeNameStatus=_CIpMRouteScopeNameStatus_Object((1,3,6,1,4,1,9,10,117,1,1,6,1,7),_CIpMRouteScopeNameStatus_Type())
cIpMRouteScopeNameStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:cIpMRouteScopeNameStatus.setStatus(_A)
_CIpMRouteEntryCount_Type=Gauge32
_CIpMRouteEntryCount_Object=MibScalar
cIpMRouteEntryCount=_CIpMRouteEntryCount_Object((1,3,6,1,4,1,9,10,117,1,1,7),_CIpMRouteEntryCount_Type())
cIpMRouteEntryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:cIpMRouteEntryCount.setStatus(_A)
_CIpMRouteMIBConformance_ObjectIdentity=ObjectIdentity
cIpMRouteMIBConformance=_CIpMRouteMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,10,117,2))
_CIpMRouteMIBCompliances_ObjectIdentity=ObjectIdentity
cIpMRouteMIBCompliances=_CIpMRouteMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,117,2,1))
_CIpMRouteMIBGroups_ObjectIdentity=ObjectIdentity
cIpMRouteMIBGroups=_CIpMRouteMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,10,117,2,2))
cIpMRouteMIBBasicGroup=ObjectGroup((1,3,6,1,4,1,9,10,117,2,2,1))
cIpMRouteMIBBasicGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:cIpMRouteMIBBasicGroup.setStatus(_A)
cIpMRouteMIBHopCountGroup=ObjectGroup((1,3,6,1,4,1,9,10,117,2,2,2))
cIpMRouteMIBHopCountGroup.setObjects((_B,_A3))
if mibBuilder.loadTexts:cIpMRouteMIBHopCountGroup.setStatus(_A)
cIpMRouteMIBBoundaryGroup=ObjectGroup((1,3,6,1,4,1,9,10,117,2,2,3))
cIpMRouteMIBBoundaryGroup.setObjects(*((_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:cIpMRouteMIBBoundaryGroup.setStatus(_A)
cIpMRouteMIBPktsOutGroup=ObjectGroup((1,3,6,1,4,1,9,10,117,2,2,4))
cIpMRouteMIBPktsOutGroup.setObjects((_B,_A9))
if mibBuilder.loadTexts:cIpMRouteMIBPktsOutGroup.setStatus(_A)
cIpMRouteMIBHCInterfaceGroup=ObjectGroup((1,3,6,1,4,1,9,10,117,2,2,5))
cIpMRouteMIBHCInterfaceGroup.setObjects(*((_B,_AA),(_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:cIpMRouteMIBHCInterfaceGroup.setStatus(_A)
cIpMRouteMIBRouteGroup=ObjectGroup((1,3,6,1,4,1,9,10,117,2,2,6))
cIpMRouteMIBRouteGroup.setObjects(*((_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG)))
if mibBuilder.loadTexts:cIpMRouteMIBRouteGroup.setStatus(_A)
cIpMRouteMIBPktsGroup=ObjectGroup((1,3,6,1,4,1,9,10,117,2,2,7))
cIpMRouteMIBPktsGroup.setObjects(*((_B,_AH),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:cIpMRouteMIBPktsGroup.setStatus(_A)
cIpMRouteMIBHCInterfaceGroupSup1=ObjectGroup((1,3,6,1,4,1,9,10,117,2,2,8))
cIpMRouteMIBHCInterfaceGroupSup1.setObjects(*((_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:cIpMRouteMIBHCInterfaceGroupSup1.setStatus(_A)
cIpMRouteMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,117,2,1,1))
cIpMRouteMIBCompliance.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:cIpMRouteMIBCompliance.setStatus('deprecated')
cIpMRouteMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,10,117,2,1,2))
cIpMRouteMIBComplianceRev1.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_AM)))
if mibBuilder.loadTexts:cIpMRouteMIBComplianceRev1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoIetfIpMRouteMIB':ciscoIetfIpMRouteMIB,'cIpMRouteMIBObjects':cIpMRouteMIBObjects,'cIpMRoute':cIpMRoute,_l:cIpMRouteEnable,'cIpMRouteTable':cIpMRouteTable,'cIpMRouteEntry':cIpMRouteEntry,_Q:cIpMRouteAddrType,_R:cIpMRouteGroup,_S:cIpMRouteSource,_T:cIpMRouteSourceMask,_n:cIpMRouteUpstreamNeighbor,_o:cIpMRouteInIfIndex,_p:cIpMRouteUpTime,_q:cIpMRouteExpiryTime,_AH:cIpMRoutePkts,_AI:cIpMRouteDifferentInIfPackets,_AJ:cIpMRouteOctets,_A2:cIpMRouteProtocol,_AD:cIpMRouteRtProto,_AE:cIpMRouteRtAddress,_AF:cIpMRouteRtMask,_AG:cIpMRouteRtType,_AC:cIpMRouteHCOctets,'cIpMRouteNextHopTable':cIpMRouteNextHopTable,'cIpMRouteNextHopEntry':cIpMRouteNextHopEntry,_U:cIpMRouteNextHopAddrType,_V:cIpMRouteNextHopGroup,_W:cIpMRouteNextHopSource,_X:cIpMRouteNextHopSourceMask,_Y:cIpMRouteNextHopIfIndex,_Z:cIpMRouteNextHopAddress,_r:cIpMRouteNextHopState,_s:cIpMRouteNextHopUpTime,_t:cIpMRouteNextHopExpiryTime,_A3:cIpMRouteNextHopClosestHops,_u:cIpMRouteNextHopProtocol,_A9:cIpMRouteNextHopPkts,'cIpMRouteInterfaceTable':cIpMRouteInterfaceTable,'cIpMRouteInterfaceEntry':cIpMRouteInterfaceEntry,_a:cIpMRouteInterfaceIfIndex,_b:cIpMRouteInterfaceIPVersion,_v:cIpMRouteInterfaceTtl,_w:cIpMRouteInterfaceProtocol,_x:cIpMRouteInterfaceRateLimit,_y:cIpMRouteInterfaceInMcastPkts,_z:cIpMRouteInterfaceOutMcastPkts,_A0:cIpMRouteInterfaceInMcastOctets,_A1:cIpMRouteInterfaceOutMcastOctets,_AA:cIpMRouteInterfaceHCInMOctets,_AB:cIpMRouteInterfaceHCOutMOctets,_AK:cIpMRouteInterfaceHCInMPkts,_AL:cIpMRouteInterfaceHCOutMPkts,'cIpMRouteBoundaryTable':cIpMRouteBoundaryTable,'cIpMRouteBoundaryEntry':cIpMRouteBoundaryEntry,_c:cIpMRouteBoundaryScopeId,_d:cIpMRouteBoundaryIfIndex,_e:cIpMRouteBoundaryAddressType,_f:cIpMRouteBoundaryAddress,_g:cIpMRouteBoundaryAddressMask,_A8:cIpMRouteBoundaryNameString,_A4:cIpMRouteBoundaryStatus,'cIpMRouteScopeNameTable':cIpMRouteScopeNameTable,'cIpMRouteScopeNameEntry':cIpMRouteScopeNameEntry,_h:cIpMRouteScopeNameAddressType,_i:cIpMRouteScopeNameAddress,_j:cIpMRouteScopeNameAddressMask,_k:cIpMRouteScopeNameLanguage,_A5:cIpMRouteScopeNameString,_A6:cIpMRouteScopeNameDefault,_A7:cIpMRouteScopeNameStatus,_m:cIpMRouteEntryCount,'cIpMRouteMIBConformance':cIpMRouteMIBConformance,'cIpMRouteMIBCompliances':cIpMRouteMIBCompliances,'cIpMRouteMIBCompliance':cIpMRouteMIBCompliance,'cIpMRouteMIBComplianceRev1':cIpMRouteMIBComplianceRev1,'cIpMRouteMIBGroups':cIpMRouteMIBGroups,_I:cIpMRouteMIBBasicGroup,_M:cIpMRouteMIBHopCountGroup,_K:cIpMRouteMIBBoundaryGroup,_N:cIpMRouteMIBPktsOutGroup,_L:cIpMRouteMIBHCInterfaceGroup,_J:cIpMRouteMIBRouteGroup,_O:cIpMRouteMIBPktsGroup,_AM:cIpMRouteMIBHCInterfaceGroupSup1})