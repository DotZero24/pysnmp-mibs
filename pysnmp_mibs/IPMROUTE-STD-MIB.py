_A6='ipMRouteMIBHCInterfaceGroup'
_A5='ipMRouteMIBBoundaryGroup'
_A4='ipMRouteMIBRouteGroup'
_A3='ipMRouteMIBBasicGroup'
_A2='ipMRouteOctets'
_A1='ipMRouteDifferentInIfPackets'
_A0='ipMRoutePkts'
_z='ipMRouteRtType'
_y='ipMRouteRtMask'
_x='ipMRouteRtAddress'
_w='ipMRouteRtProto'
_v='ipMRouteHCOctets'
_u='ipMRouteInterfaceHCOutMcastOctets'
_t='ipMRouteInterfaceHCInMcastOctets'
_s='ipMRouteScopeNameStatus'
_r='ipMRouteScopeNameDefault'
_q='ipMRouteScopeNameString'
_p='ipMRouteBoundaryStatus'
_o='ipMRouteNextHopClosestMemberHops'
_n='ipMRouteProtocol'
_m='ipMRouteInterfaceOutMcastOctets'
_l='ipMRouteInterfaceInMcastOctets'
_k='ipMRouteInterfaceRateLimit'
_j='ipMRouteInterfaceProtocol'
_i='ipMRouteInterfaceTtl'
_h='ipMRouteNextHopProtocol'
_g='ipMRouteNextHopExpiryTime'
_f='ipMRouteNextHopUpTime'
_e='ipMRouteNextHopState'
_d='ipMRouteExpiryTime'
_c='ipMRouteUpTime'
_b='ipMRouteInIfIndex'
_a='ipMRouteUpstreamNeighbor'
_Z='ipMRouteEntryCount'
_Y='ipMRouteEnable'
_X='ipMRouteScopeNameLanguage'
_W='ipMRouteScopeNameAddressMask'
_V='ipMRouteScopeNameAddress'
_U='ipMRouteBoundaryAddressMask'
_T='ipMRouteBoundaryAddress'
_S='ipMRouteBoundaryIfIndex'
_R='ipMRouteInterfaceIfIndex'
_Q='ipMRouteNextHopAddress'
_P='ipMRouteNextHopIfIndex'
_O='ipMRouteNextHopSourceMask'
_N='ipMRouteNextHopSource'
_M='ipMRouteNextHopGroup'
_L='ipMRouteSourceMask'
_K='ipMRouteSource'
_J='ipMRouteGroup'
_I='TruthValue'
_H='ipMRouteNextHopPkts'
_G='read-write'
_F='read-create'
_E='Integer32'
_D='not-accessible'
_C='read-only'
_B='IPMROUTE-STD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAipMRouteProtocol,IANAipRouteProtocol=mibBuilder.importSymbols('IANA-RTPROTO-MIB','IANAipMRouteProtocol','IANAipRouteProtocol')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_I)
ipMRouteStdMIB=ModuleIdentity((1,3,6,1,2,1,83))
if mibBuilder.loadTexts:ipMRouteStdMIB.setRevisions(('2000-09-22 00:00',))
class LanguageTag(TextualConvention,OctetString):status=_A;displayHint='100a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,100))
_IpMRouteMIBObjects_ObjectIdentity=ObjectIdentity
ipMRouteMIBObjects=_IpMRouteMIBObjects_ObjectIdentity((1,3,6,1,2,1,83,1))
_IpMRoute_ObjectIdentity=ObjectIdentity
ipMRoute=_IpMRoute_ObjectIdentity((1,3,6,1,2,1,83,1,1))
class _IpMRouteEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_IpMRouteEnable_Type.__name__=_E
_IpMRouteEnable_Object=MibScalar
ipMRouteEnable=_IpMRouteEnable_Object((1,3,6,1,2,1,83,1,1,1),_IpMRouteEnable_Type())
ipMRouteEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:ipMRouteEnable.setStatus(_A)
_IpMRouteTable_Object=MibTable
ipMRouteTable=_IpMRouteTable_Object((1,3,6,1,2,1,83,1,1,2))
if mibBuilder.loadTexts:ipMRouteTable.setStatus(_A)
_IpMRouteEntry_Object=MibTableRow
ipMRouteEntry=_IpMRouteEntry_Object((1,3,6,1,2,1,83,1,1,2,1))
ipMRouteEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:ipMRouteEntry.setStatus(_A)
_IpMRouteGroup_Type=IpAddress
_IpMRouteGroup_Object=MibTableColumn
ipMRouteGroup=_IpMRouteGroup_Object((1,3,6,1,2,1,83,1,1,2,1,1),_IpMRouteGroup_Type())
ipMRouteGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRouteGroup.setStatus(_A)
_IpMRouteSource_Type=IpAddress
_IpMRouteSource_Object=MibTableColumn
ipMRouteSource=_IpMRouteSource_Object((1,3,6,1,2,1,83,1,1,2,1,2),_IpMRouteSource_Type())
ipMRouteSource.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRouteSource.setStatus(_A)
_IpMRouteSourceMask_Type=IpAddress
_IpMRouteSourceMask_Object=MibTableColumn
ipMRouteSourceMask=_IpMRouteSourceMask_Object((1,3,6,1,2,1,83,1,1,2,1,3),_IpMRouteSourceMask_Type())
ipMRouteSourceMask.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRouteSourceMask.setStatus(_A)
_IpMRouteUpstreamNeighbor_Type=IpAddress
_IpMRouteUpstreamNeighbor_Object=MibTableColumn
ipMRouteUpstreamNeighbor=_IpMRouteUpstreamNeighbor_Object((1,3,6,1,2,1,83,1,1,2,1,4),_IpMRouteUpstreamNeighbor_Type())
ipMRouteUpstreamNeighbor.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteUpstreamNeighbor.setStatus(_A)
_IpMRouteInIfIndex_Type=InterfaceIndexOrZero
_IpMRouteInIfIndex_Object=MibTableColumn
ipMRouteInIfIndex=_IpMRouteInIfIndex_Object((1,3,6,1,2,1,83,1,1,2,1,5),_IpMRouteInIfIndex_Type())
ipMRouteInIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteInIfIndex.setStatus(_A)
_IpMRouteUpTime_Type=TimeTicks
_IpMRouteUpTime_Object=MibTableColumn
ipMRouteUpTime=_IpMRouteUpTime_Object((1,3,6,1,2,1,83,1,1,2,1,6),_IpMRouteUpTime_Type())
ipMRouteUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteUpTime.setStatus(_A)
_IpMRouteExpiryTime_Type=TimeTicks
_IpMRouteExpiryTime_Object=MibTableColumn
ipMRouteExpiryTime=_IpMRouteExpiryTime_Object((1,3,6,1,2,1,83,1,1,2,1,7),_IpMRouteExpiryTime_Type())
ipMRouteExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteExpiryTime.setStatus(_A)
_IpMRoutePkts_Type=Counter32
_IpMRoutePkts_Object=MibTableColumn
ipMRoutePkts=_IpMRoutePkts_Object((1,3,6,1,2,1,83,1,1,2,1,8),_IpMRoutePkts_Type())
ipMRoutePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoutePkts.setStatus(_A)
_IpMRouteDifferentInIfPackets_Type=Counter32
_IpMRouteDifferentInIfPackets_Object=MibTableColumn
ipMRouteDifferentInIfPackets=_IpMRouteDifferentInIfPackets_Object((1,3,6,1,2,1,83,1,1,2,1,9),_IpMRouteDifferentInIfPackets_Type())
ipMRouteDifferentInIfPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteDifferentInIfPackets.setStatus(_A)
_IpMRouteOctets_Type=Counter32
_IpMRouteOctets_Object=MibTableColumn
ipMRouteOctets=_IpMRouteOctets_Object((1,3,6,1,2,1,83,1,1,2,1,10),_IpMRouteOctets_Type())
ipMRouteOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteOctets.setStatus(_A)
_IpMRouteProtocol_Type=IANAipMRouteProtocol
_IpMRouteProtocol_Object=MibTableColumn
ipMRouteProtocol=_IpMRouteProtocol_Object((1,3,6,1,2,1,83,1,1,2,1,11),_IpMRouteProtocol_Type())
ipMRouteProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteProtocol.setStatus(_A)
_IpMRouteRtProto_Type=IANAipRouteProtocol
_IpMRouteRtProto_Object=MibTableColumn
ipMRouteRtProto=_IpMRouteRtProto_Object((1,3,6,1,2,1,83,1,1,2,1,12),_IpMRouteRtProto_Type())
ipMRouteRtProto.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteRtProto.setStatus(_A)
_IpMRouteRtAddress_Type=IpAddress
_IpMRouteRtAddress_Object=MibTableColumn
ipMRouteRtAddress=_IpMRouteRtAddress_Object((1,3,6,1,2,1,83,1,1,2,1,13),_IpMRouteRtAddress_Type())
ipMRouteRtAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteRtAddress.setStatus(_A)
_IpMRouteRtMask_Type=IpAddress
_IpMRouteRtMask_Object=MibTableColumn
ipMRouteRtMask=_IpMRouteRtMask_Object((1,3,6,1,2,1,83,1,1,2,1,14),_IpMRouteRtMask_Type())
ipMRouteRtMask.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteRtMask.setStatus(_A)
class _IpMRouteRtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unicast',1),('multicast',2)))
_IpMRouteRtType_Type.__name__=_E
_IpMRouteRtType_Object=MibTableColumn
ipMRouteRtType=_IpMRouteRtType_Object((1,3,6,1,2,1,83,1,1,2,1,15),_IpMRouteRtType_Type())
ipMRouteRtType.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteRtType.setStatus(_A)
_IpMRouteHCOctets_Type=Counter64
_IpMRouteHCOctets_Object=MibTableColumn
ipMRouteHCOctets=_IpMRouteHCOctets_Object((1,3,6,1,2,1,83,1,1,2,1,16),_IpMRouteHCOctets_Type())
ipMRouteHCOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteHCOctets.setStatus(_A)
_IpMRouteNextHopTable_Object=MibTable
ipMRouteNextHopTable=_IpMRouteNextHopTable_Object((1,3,6,1,2,1,83,1,1,3))
if mibBuilder.loadTexts:ipMRouteNextHopTable.setStatus(_A)
_IpMRouteNextHopEntry_Object=MibTableRow
ipMRouteNextHopEntry=_IpMRouteNextHopEntry_Object((1,3,6,1,2,1,83,1,1,3,1))
ipMRouteNextHopEntry.setIndexNames((0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:ipMRouteNextHopEntry.setStatus(_A)
_IpMRouteNextHopGroup_Type=IpAddress
_IpMRouteNextHopGroup_Object=MibTableColumn
ipMRouteNextHopGroup=_IpMRouteNextHopGroup_Object((1,3,6,1,2,1,83,1,1,3,1,1),_IpMRouteNextHopGroup_Type())
ipMRouteNextHopGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRouteNextHopGroup.setStatus(_A)
_IpMRouteNextHopSource_Type=IpAddress
_IpMRouteNextHopSource_Object=MibTableColumn
ipMRouteNextHopSource=_IpMRouteNextHopSource_Object((1,3,6,1,2,1,83,1,1,3,1,2),_IpMRouteNextHopSource_Type())
ipMRouteNextHopSource.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRouteNextHopSource.setStatus(_A)
_IpMRouteNextHopSourceMask_Type=IpAddress
_IpMRouteNextHopSourceMask_Object=MibTableColumn
ipMRouteNextHopSourceMask=_IpMRouteNextHopSourceMask_Object((1,3,6,1,2,1,83,1,1,3,1,3),_IpMRouteNextHopSourceMask_Type())
ipMRouteNextHopSourceMask.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRouteNextHopSourceMask.setStatus(_A)
_IpMRouteNextHopIfIndex_Type=InterfaceIndex
_IpMRouteNextHopIfIndex_Object=MibTableColumn
ipMRouteNextHopIfIndex=_IpMRouteNextHopIfIndex_Object((1,3,6,1,2,1,83,1,1,3,1,4),_IpMRouteNextHopIfIndex_Type())
ipMRouteNextHopIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRouteNextHopIfIndex.setStatus(_A)
_IpMRouteNextHopAddress_Type=IpAddress
_IpMRouteNextHopAddress_Object=MibTableColumn
ipMRouteNextHopAddress=_IpMRouteNextHopAddress_Object((1,3,6,1,2,1,83,1,1,3,1,5),_IpMRouteNextHopAddress_Type())
ipMRouteNextHopAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRouteNextHopAddress.setStatus(_A)
class _IpMRouteNextHopState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pruned',1),('forwarding',2)))
_IpMRouteNextHopState_Type.__name__=_E
_IpMRouteNextHopState_Object=MibTableColumn
ipMRouteNextHopState=_IpMRouteNextHopState_Object((1,3,6,1,2,1,83,1,1,3,1,6),_IpMRouteNextHopState_Type())
ipMRouteNextHopState.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteNextHopState.setStatus(_A)
_IpMRouteNextHopUpTime_Type=TimeTicks
_IpMRouteNextHopUpTime_Object=MibTableColumn
ipMRouteNextHopUpTime=_IpMRouteNextHopUpTime_Object((1,3,6,1,2,1,83,1,1,3,1,7),_IpMRouteNextHopUpTime_Type())
ipMRouteNextHopUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteNextHopUpTime.setStatus(_A)
_IpMRouteNextHopExpiryTime_Type=TimeTicks
_IpMRouteNextHopExpiryTime_Object=MibTableColumn
ipMRouteNextHopExpiryTime=_IpMRouteNextHopExpiryTime_Object((1,3,6,1,2,1,83,1,1,3,1,8),_IpMRouteNextHopExpiryTime_Type())
ipMRouteNextHopExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteNextHopExpiryTime.setStatus(_A)
_IpMRouteNextHopClosestMemberHops_Type=Integer32
_IpMRouteNextHopClosestMemberHops_Object=MibTableColumn
ipMRouteNextHopClosestMemberHops=_IpMRouteNextHopClosestMemberHops_Object((1,3,6,1,2,1,83,1,1,3,1,9),_IpMRouteNextHopClosestMemberHops_Type())
ipMRouteNextHopClosestMemberHops.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteNextHopClosestMemberHops.setStatus(_A)
_IpMRouteNextHopProtocol_Type=IANAipMRouteProtocol
_IpMRouteNextHopProtocol_Object=MibTableColumn
ipMRouteNextHopProtocol=_IpMRouteNextHopProtocol_Object((1,3,6,1,2,1,83,1,1,3,1,10),_IpMRouteNextHopProtocol_Type())
ipMRouteNextHopProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteNextHopProtocol.setStatus(_A)
_IpMRouteNextHopPkts_Type=Counter32
_IpMRouteNextHopPkts_Object=MibTableColumn
ipMRouteNextHopPkts=_IpMRouteNextHopPkts_Object((1,3,6,1,2,1,83,1,1,3,1,11),_IpMRouteNextHopPkts_Type())
ipMRouteNextHopPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteNextHopPkts.setStatus(_A)
_IpMRouteInterfaceTable_Object=MibTable
ipMRouteInterfaceTable=_IpMRouteInterfaceTable_Object((1,3,6,1,2,1,83,1,1,4))
if mibBuilder.loadTexts:ipMRouteInterfaceTable.setStatus(_A)
_IpMRouteInterfaceEntry_Object=MibTableRow
ipMRouteInterfaceEntry=_IpMRouteInterfaceEntry_Object((1,3,6,1,2,1,83,1,1,4,1))
ipMRouteInterfaceEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:ipMRouteInterfaceEntry.setStatus(_A)
_IpMRouteInterfaceIfIndex_Type=InterfaceIndex
_IpMRouteInterfaceIfIndex_Object=MibTableColumn
ipMRouteInterfaceIfIndex=_IpMRouteInterfaceIfIndex_Object((1,3,6,1,2,1,83,1,1,4,1,1),_IpMRouteInterfaceIfIndex_Type())
ipMRouteInterfaceIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRouteInterfaceIfIndex.setStatus(_A)
class _IpMRouteInterfaceTtl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IpMRouteInterfaceTtl_Type.__name__=_E
_IpMRouteInterfaceTtl_Object=MibTableColumn
ipMRouteInterfaceTtl=_IpMRouteInterfaceTtl_Object((1,3,6,1,2,1,83,1,1,4,1,2),_IpMRouteInterfaceTtl_Type())
ipMRouteInterfaceTtl.setMaxAccess(_G)
if mibBuilder.loadTexts:ipMRouteInterfaceTtl.setStatus(_A)
_IpMRouteInterfaceProtocol_Type=IANAipMRouteProtocol
_IpMRouteInterfaceProtocol_Object=MibTableColumn
ipMRouteInterfaceProtocol=_IpMRouteInterfaceProtocol_Object((1,3,6,1,2,1,83,1,1,4,1,3),_IpMRouteInterfaceProtocol_Type())
ipMRouteInterfaceProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteInterfaceProtocol.setStatus(_A)
class _IpMRouteInterfaceRateLimit_Type(Integer32):defaultValue=0
_IpMRouteInterfaceRateLimit_Type.__name__=_E
_IpMRouteInterfaceRateLimit_Object=MibTableColumn
ipMRouteInterfaceRateLimit=_IpMRouteInterfaceRateLimit_Object((1,3,6,1,2,1,83,1,1,4,1,4),_IpMRouteInterfaceRateLimit_Type())
ipMRouteInterfaceRateLimit.setMaxAccess(_G)
if mibBuilder.loadTexts:ipMRouteInterfaceRateLimit.setStatus(_A)
_IpMRouteInterfaceInMcastOctets_Type=Counter32
_IpMRouteInterfaceInMcastOctets_Object=MibTableColumn
ipMRouteInterfaceInMcastOctets=_IpMRouteInterfaceInMcastOctets_Object((1,3,6,1,2,1,83,1,1,4,1,5),_IpMRouteInterfaceInMcastOctets_Type())
ipMRouteInterfaceInMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteInterfaceInMcastOctets.setStatus(_A)
_IpMRouteInterfaceOutMcastOctets_Type=Counter32
_IpMRouteInterfaceOutMcastOctets_Object=MibTableColumn
ipMRouteInterfaceOutMcastOctets=_IpMRouteInterfaceOutMcastOctets_Object((1,3,6,1,2,1,83,1,1,4,1,6),_IpMRouteInterfaceOutMcastOctets_Type())
ipMRouteInterfaceOutMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteInterfaceOutMcastOctets.setStatus(_A)
_IpMRouteInterfaceHCInMcastOctets_Type=Counter64
_IpMRouteInterfaceHCInMcastOctets_Object=MibTableColumn
ipMRouteInterfaceHCInMcastOctets=_IpMRouteInterfaceHCInMcastOctets_Object((1,3,6,1,2,1,83,1,1,4,1,7),_IpMRouteInterfaceHCInMcastOctets_Type())
ipMRouteInterfaceHCInMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteInterfaceHCInMcastOctets.setStatus(_A)
_IpMRouteInterfaceHCOutMcastOctets_Type=Counter64
_IpMRouteInterfaceHCOutMcastOctets_Object=MibTableColumn
ipMRouteInterfaceHCOutMcastOctets=_IpMRouteInterfaceHCOutMcastOctets_Object((1,3,6,1,2,1,83,1,1,4,1,8),_IpMRouteInterfaceHCOutMcastOctets_Type())
ipMRouteInterfaceHCOutMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteInterfaceHCOutMcastOctets.setStatus(_A)
_IpMRouteBoundaryTable_Object=MibTable
ipMRouteBoundaryTable=_IpMRouteBoundaryTable_Object((1,3,6,1,2,1,83,1,1,5))
if mibBuilder.loadTexts:ipMRouteBoundaryTable.setStatus(_A)
_IpMRouteBoundaryEntry_Object=MibTableRow
ipMRouteBoundaryEntry=_IpMRouteBoundaryEntry_Object((1,3,6,1,2,1,83,1,1,5,1))
ipMRouteBoundaryEntry.setIndexNames((0,_B,_S),(0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:ipMRouteBoundaryEntry.setStatus(_A)
_IpMRouteBoundaryIfIndex_Type=InterfaceIndex
_IpMRouteBoundaryIfIndex_Object=MibTableColumn
ipMRouteBoundaryIfIndex=_IpMRouteBoundaryIfIndex_Object((1,3,6,1,2,1,83,1,1,5,1,1),_IpMRouteBoundaryIfIndex_Type())
ipMRouteBoundaryIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRouteBoundaryIfIndex.setStatus(_A)
_IpMRouteBoundaryAddress_Type=IpAddress
_IpMRouteBoundaryAddress_Object=MibTableColumn
ipMRouteBoundaryAddress=_IpMRouteBoundaryAddress_Object((1,3,6,1,2,1,83,1,1,5,1,2),_IpMRouteBoundaryAddress_Type())
ipMRouteBoundaryAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRouteBoundaryAddress.setStatus(_A)
_IpMRouteBoundaryAddressMask_Type=IpAddress
_IpMRouteBoundaryAddressMask_Object=MibTableColumn
ipMRouteBoundaryAddressMask=_IpMRouteBoundaryAddressMask_Object((1,3,6,1,2,1,83,1,1,5,1,3),_IpMRouteBoundaryAddressMask_Type())
ipMRouteBoundaryAddressMask.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRouteBoundaryAddressMask.setStatus(_A)
_IpMRouteBoundaryStatus_Type=RowStatus
_IpMRouteBoundaryStatus_Object=MibTableColumn
ipMRouteBoundaryStatus=_IpMRouteBoundaryStatus_Object((1,3,6,1,2,1,83,1,1,5,1,4),_IpMRouteBoundaryStatus_Type())
ipMRouteBoundaryStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ipMRouteBoundaryStatus.setStatus(_A)
_IpMRouteScopeNameTable_Object=MibTable
ipMRouteScopeNameTable=_IpMRouteScopeNameTable_Object((1,3,6,1,2,1,83,1,1,6))
if mibBuilder.loadTexts:ipMRouteScopeNameTable.setStatus(_A)
_IpMRouteScopeNameEntry_Object=MibTableRow
ipMRouteScopeNameEntry=_IpMRouteScopeNameEntry_Object((1,3,6,1,2,1,83,1,1,6,1))
ipMRouteScopeNameEntry.setIndexNames((0,_B,_V),(0,_B,_W),(1,_B,_X))
if mibBuilder.loadTexts:ipMRouteScopeNameEntry.setStatus(_A)
_IpMRouteScopeNameAddress_Type=IpAddress
_IpMRouteScopeNameAddress_Object=MibTableColumn
ipMRouteScopeNameAddress=_IpMRouteScopeNameAddress_Object((1,3,6,1,2,1,83,1,1,6,1,1),_IpMRouteScopeNameAddress_Type())
ipMRouteScopeNameAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRouteScopeNameAddress.setStatus(_A)
_IpMRouteScopeNameAddressMask_Type=IpAddress
_IpMRouteScopeNameAddressMask_Object=MibTableColumn
ipMRouteScopeNameAddressMask=_IpMRouteScopeNameAddressMask_Object((1,3,6,1,2,1,83,1,1,6,1,2),_IpMRouteScopeNameAddressMask_Type())
ipMRouteScopeNameAddressMask.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRouteScopeNameAddressMask.setStatus(_A)
_IpMRouteScopeNameLanguage_Type=LanguageTag
_IpMRouteScopeNameLanguage_Object=MibTableColumn
ipMRouteScopeNameLanguage=_IpMRouteScopeNameLanguage_Object((1,3,6,1,2,1,83,1,1,6,1,3),_IpMRouteScopeNameLanguage_Type())
ipMRouteScopeNameLanguage.setMaxAccess(_D)
if mibBuilder.loadTexts:ipMRouteScopeNameLanguage.setStatus(_A)
_IpMRouteScopeNameString_Type=SnmpAdminString
_IpMRouteScopeNameString_Object=MibTableColumn
ipMRouteScopeNameString=_IpMRouteScopeNameString_Object((1,3,6,1,2,1,83,1,1,6,1,4),_IpMRouteScopeNameString_Type())
ipMRouteScopeNameString.setMaxAccess(_F)
if mibBuilder.loadTexts:ipMRouteScopeNameString.setStatus(_A)
class _IpMRouteScopeNameDefault_Type(TruthValue):defaultValue=2
_IpMRouteScopeNameDefault_Type.__name__=_I
_IpMRouteScopeNameDefault_Object=MibTableColumn
ipMRouteScopeNameDefault=_IpMRouteScopeNameDefault_Object((1,3,6,1,2,1,83,1,1,6,1,5),_IpMRouteScopeNameDefault_Type())
ipMRouteScopeNameDefault.setMaxAccess(_F)
if mibBuilder.loadTexts:ipMRouteScopeNameDefault.setStatus(_A)
_IpMRouteScopeNameStatus_Type=RowStatus
_IpMRouteScopeNameStatus_Object=MibTableColumn
ipMRouteScopeNameStatus=_IpMRouteScopeNameStatus_Object((1,3,6,1,2,1,83,1,1,6,1,6),_IpMRouteScopeNameStatus_Type())
ipMRouteScopeNameStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:ipMRouteScopeNameStatus.setStatus(_A)
_IpMRouteEntryCount_Type=Gauge32
_IpMRouteEntryCount_Object=MibScalar
ipMRouteEntryCount=_IpMRouteEntryCount_Object((1,3,6,1,2,1,83,1,1,7),_IpMRouteEntryCount_Type())
ipMRouteEntryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteEntryCount.setStatus(_A)
_IpMRouteMIBConformance_ObjectIdentity=ObjectIdentity
ipMRouteMIBConformance=_IpMRouteMIBConformance_ObjectIdentity((1,3,6,1,2,1,83,2))
_IpMRouteMIBCompliances_ObjectIdentity=ObjectIdentity
ipMRouteMIBCompliances=_IpMRouteMIBCompliances_ObjectIdentity((1,3,6,1,2,1,83,2,1))
_IpMRouteMIBGroups_ObjectIdentity=ObjectIdentity
ipMRouteMIBGroups=_IpMRouteMIBGroups_ObjectIdentity((1,3,6,1,2,1,83,2,2))
ipMRouteMIBBasicGroup=ObjectGroup((1,3,6,1,2,1,83,2,2,1))
ipMRouteMIBBasicGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_H),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:ipMRouteMIBBasicGroup.setStatus(_A)
ipMRouteMIBHopCountGroup=ObjectGroup((1,3,6,1,2,1,83,2,2,2))
ipMRouteMIBHopCountGroup.setObjects((_B,_o))
if mibBuilder.loadTexts:ipMRouteMIBHopCountGroup.setStatus(_A)
ipMRouteMIBBoundaryGroup=ObjectGroup((1,3,6,1,2,1,83,2,2,3))
ipMRouteMIBBoundaryGroup.setObjects(*((_B,_p),(_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:ipMRouteMIBBoundaryGroup.setStatus(_A)
ipMRouteMIBPktsOutGroup=ObjectGroup((1,3,6,1,2,1,83,2,2,4))
ipMRouteMIBPktsOutGroup.setObjects((_B,_H))
if mibBuilder.loadTexts:ipMRouteMIBPktsOutGroup.setStatus(_A)
ipMRouteMIBHCInterfaceGroup=ObjectGroup((1,3,6,1,2,1,83,2,2,5))
ipMRouteMIBHCInterfaceGroup.setObjects(*((_B,_t),(_B,_u),(_B,_v)))
if mibBuilder.loadTexts:ipMRouteMIBHCInterfaceGroup.setStatus(_A)
ipMRouteMIBRouteGroup=ObjectGroup((1,3,6,1,2,1,83,2,2,6))
ipMRouteMIBRouteGroup.setObjects(*((_B,_w),(_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:ipMRouteMIBRouteGroup.setStatus(_A)
ipMRouteMIBPktsGroup=ObjectGroup((1,3,6,1,2,1,83,2,2,7))
ipMRouteMIBPktsGroup.setObjects(*((_B,_A0),(_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:ipMRouteMIBPktsGroup.setStatus(_A)
ipMRouteMIBCompliance=ModuleCompliance((1,3,6,1,2,1,83,2,1,1))
ipMRouteMIBCompliance.setObjects(*((_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:ipMRouteMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'LanguageTag':LanguageTag,'ipMRouteStdMIB':ipMRouteStdMIB,'ipMRouteMIBObjects':ipMRouteMIBObjects,'ipMRoute':ipMRoute,_Y:ipMRouteEnable,'ipMRouteTable':ipMRouteTable,'ipMRouteEntry':ipMRouteEntry,_J:ipMRouteGroup,_K:ipMRouteSource,_L:ipMRouteSourceMask,_a:ipMRouteUpstreamNeighbor,_b:ipMRouteInIfIndex,_c:ipMRouteUpTime,_d:ipMRouteExpiryTime,_A0:ipMRoutePkts,_A1:ipMRouteDifferentInIfPackets,_A2:ipMRouteOctets,_n:ipMRouteProtocol,_w:ipMRouteRtProto,_x:ipMRouteRtAddress,_y:ipMRouteRtMask,_z:ipMRouteRtType,_v:ipMRouteHCOctets,'ipMRouteNextHopTable':ipMRouteNextHopTable,'ipMRouteNextHopEntry':ipMRouteNextHopEntry,_M:ipMRouteNextHopGroup,_N:ipMRouteNextHopSource,_O:ipMRouteNextHopSourceMask,_P:ipMRouteNextHopIfIndex,_Q:ipMRouteNextHopAddress,_e:ipMRouteNextHopState,_f:ipMRouteNextHopUpTime,_g:ipMRouteNextHopExpiryTime,_o:ipMRouteNextHopClosestMemberHops,_h:ipMRouteNextHopProtocol,_H:ipMRouteNextHopPkts,'ipMRouteInterfaceTable':ipMRouteInterfaceTable,'ipMRouteInterfaceEntry':ipMRouteInterfaceEntry,_R:ipMRouteInterfaceIfIndex,_i:ipMRouteInterfaceTtl,_j:ipMRouteInterfaceProtocol,_k:ipMRouteInterfaceRateLimit,_l:ipMRouteInterfaceInMcastOctets,_m:ipMRouteInterfaceOutMcastOctets,_t:ipMRouteInterfaceHCInMcastOctets,_u:ipMRouteInterfaceHCOutMcastOctets,'ipMRouteBoundaryTable':ipMRouteBoundaryTable,'ipMRouteBoundaryEntry':ipMRouteBoundaryEntry,_S:ipMRouteBoundaryIfIndex,_T:ipMRouteBoundaryAddress,_U:ipMRouteBoundaryAddressMask,_p:ipMRouteBoundaryStatus,'ipMRouteScopeNameTable':ipMRouteScopeNameTable,'ipMRouteScopeNameEntry':ipMRouteScopeNameEntry,_V:ipMRouteScopeNameAddress,_W:ipMRouteScopeNameAddressMask,_X:ipMRouteScopeNameLanguage,_q:ipMRouteScopeNameString,_r:ipMRouteScopeNameDefault,_s:ipMRouteScopeNameStatus,_Z:ipMRouteEntryCount,'ipMRouteMIBConformance':ipMRouteMIBConformance,'ipMRouteMIBCompliances':ipMRouteMIBCompliances,'ipMRouteMIBCompliance':ipMRouteMIBCompliance,'ipMRouteMIBGroups':ipMRouteMIBGroups,_A3:ipMRouteMIBBasicGroup,'ipMRouteMIBHopCountGroup':ipMRouteMIBHopCountGroup,_A5:ipMRouteMIBBoundaryGroup,'ipMRouteMIBPktsOutGroup':ipMRouteMIBPktsOutGroup,_A6:ipMRouteMIBHCInterfaceGroup,_A4:ipMRouteMIBRouteGroup,'ipMRouteMIBPktsGroup':ipMRouteMIBPktsGroup})