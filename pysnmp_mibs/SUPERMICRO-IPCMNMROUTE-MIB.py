_p='ipCmnMRouteMIBPktsGroup'
_o='ipCmnMRouteMIBRouteGroup'
_n='ipCmnMRouteMIBBasicGroup'
_m='ipCmnMRouteDifferentInIfPackets'
_l='ipCmnMRoutePkts'
_k='ipCmnMRouteRtType'
_j='ipCmnMRouteRtMask'
_i='ipCmnMRouteRtAddress'
_h='ipCmnMRouteProtocol'
_g='ipCmnMRouteInterfaceRateLimit'
_f='ipCmnMRouteInterfaceProtocol'
_e='ipCmnMRouteInterfaceTtl'
_d='ipCmnMRouteNextHopUpTime'
_c='ipCmnMRouteNextHopState'
_b='ipCmnMRouteUpTime'
_a='ipCmnMRouteInIfIndex'
_Z='ipCmnMRouteUpstreamNeighbor'
_Y='ipCmnMRouteEntryCount'
_X='ipCmnMRouteEnable'
_W='ipCmnMRouteInterfaceAddrType'
_V='ipCmnMRouteInterfaceIfIndex'
_U='ipCmnMRouteNextHopAddress'
_T='ipCmnMRouteNextHopIfIndex'
_S='ipCmnMRouteNextHopSourceMask'
_R='ipCmnMRouteNextHopSource'
_Q='ipCmnMRouteNextHopGroup'
_P='ipCmnMRouteNextHopAddrType'
_O='ipCmnMRouteNextHopOwnerId'
_N='ipCmnMRouteSourceMask'
_M='ipCmnMRouteSource'
_L='ipCmnMRouteGroup'
_K='ipCmnMRouteAddrType'
_J='ipCmnMRouteOwnerId'
_I='disabled'
_H='enable'
_G='read-write'
_F='InetAddress'
_E='not-accessible'
_D='Integer32'
_C='read-only'
_B='SUPERMICRO-IPCMNMROUTE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAipMRouteProtocol,=mibBuilder.importSymbols('IANA-RTPROTO-MIB','IANAipMRouteProtocol')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_F,'InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ipCmnMRouteMIB=ModuleIdentity((1,3,6,1,4,1,10876,101,1,126))
if mibBuilder.loadTexts:ipCmnMRouteMIB.setRevisions(('2007-02-15 00:00','2001-11-30 00:00'))
class Status(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('disable',2)))
_MfwdCmnMIBObjects_ObjectIdentity=ObjectIdentity
mfwdCmnMIBObjects=_MfwdCmnMIBObjects_ObjectIdentity((1,3,6,1,4,1,10876,101,1,126,1))
_MfwdCmnScalars_ObjectIdentity=ObjectIdentity
mfwdCmnScalars=_MfwdCmnScalars_ObjectIdentity((1,3,6,1,4,1,10876,101,1,126,1,1))
class _IpCmnMRouteEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_I,2)))
_IpCmnMRouteEnable_Type.__name__=_D
_IpCmnMRouteEnable_Object=MibScalar
ipCmnMRouteEnable=_IpCmnMRouteEnable_Object((1,3,6,1,4,1,10876,101,1,126,1,1,1),_IpCmnMRouteEnable_Type())
ipCmnMRouteEnable.setMaxAccess(_G)
if mibBuilder.loadTexts:ipCmnMRouteEnable.setStatus(_A)
_IpCmnMRouteEntryCount_Type=Gauge32
_IpCmnMRouteEntryCount_Object=MibScalar
ipCmnMRouteEntryCount=_IpCmnMRouteEntryCount_Object((1,3,6,1,4,1,10876,101,1,126,1,1,2),_IpCmnMRouteEntryCount_Type())
ipCmnMRouteEntryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ipCmnMRouteEntryCount.setStatus(_A)
class _IpCmnMRouteEnableCmdb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_IpCmnMRouteEnableCmdb_Type.__name__=_D
_IpCmnMRouteEnableCmdb_Object=MibScalar
ipCmnMRouteEnableCmdb=_IpCmnMRouteEnableCmdb_Object((1,3,6,1,4,1,10876,101,1,126,1,1,3),_IpCmnMRouteEnableCmdb_Type())
ipCmnMRouteEnableCmdb.setMaxAccess(_G)
if mibBuilder.loadTexts:ipCmnMRouteEnableCmdb.setStatus(_A)
class _MfwdCmnGlobalTrace_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MfwdCmnGlobalTrace_Type.__name__=_D
_MfwdCmnGlobalTrace_Object=MibScalar
mfwdCmnGlobalTrace=_MfwdCmnGlobalTrace_Object((1,3,6,1,4,1,10876,101,1,126,1,1,4),_MfwdCmnGlobalTrace_Type())
mfwdCmnGlobalTrace.setMaxAccess(_G)
if mibBuilder.loadTexts:mfwdCmnGlobalTrace.setStatus(_A)
class _MfwdCmnGlobalDebug_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MfwdCmnGlobalDebug_Type.__name__=_D
_MfwdCmnGlobalDebug_Object=MibScalar
mfwdCmnGlobalDebug=_MfwdCmnGlobalDebug_Object((1,3,6,1,4,1,10876,101,1,126,1,1,5),_MfwdCmnGlobalDebug_Type())
mfwdCmnGlobalDebug.setMaxAccess(_G)
if mibBuilder.loadTexts:mfwdCmnGlobalDebug.setStatus(_A)
_IpCmnMRouteDiscardedPkts_Type=Counter32
_IpCmnMRouteDiscardedPkts_Object=MibScalar
ipCmnMRouteDiscardedPkts=_IpCmnMRouteDiscardedPkts_Object((1,3,6,1,4,1,10876,101,1,126,1,1,6),_IpCmnMRouteDiscardedPkts_Type())
ipCmnMRouteDiscardedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ipCmnMRouteDiscardedPkts.setStatus(_A)
class _MfwdCmnAvgDataRate_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MfwdCmnAvgDataRate_Type.__name__=_D
_MfwdCmnAvgDataRate_Object=MibScalar
mfwdCmnAvgDataRate=_MfwdCmnAvgDataRate_Object((1,3,6,1,4,1,10876,101,1,126,1,1,7),_MfwdCmnAvgDataRate_Type())
mfwdCmnAvgDataRate.setMaxAccess(_G)
if mibBuilder.loadTexts:mfwdCmnAvgDataRate.setStatus(_A)
_MfwdCmnTables_ObjectIdentity=ObjectIdentity
mfwdCmnTables=_MfwdCmnTables_ObjectIdentity((1,3,6,1,4,1,10876,101,1,126,1,2))
_IpCmnMRouteTable_Object=MibTable
ipCmnMRouteTable=_IpCmnMRouteTable_Object((1,3,6,1,4,1,10876,101,1,126,1,2,1))
if mibBuilder.loadTexts:ipCmnMRouteTable.setStatus(_A)
_IpCmnMRouteEntry_Object=MibTableRow
ipCmnMRouteEntry=_IpCmnMRouteEntry_Object((1,3,6,1,4,1,10876,101,1,126,1,2,1,1))
ipCmnMRouteEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:ipCmnMRouteEntry.setStatus(_A)
class _IpCmnMRouteOwnerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IpCmnMRouteOwnerId_Type.__name__=_D
_IpCmnMRouteOwnerId_Object=MibTableColumn
ipCmnMRouteOwnerId=_IpCmnMRouteOwnerId_Object((1,3,6,1,4,1,10876,101,1,126,1,2,1,1,1),_IpCmnMRouteOwnerId_Type())
ipCmnMRouteOwnerId.setMaxAccess(_E)
if mibBuilder.loadTexts:ipCmnMRouteOwnerId.setStatus(_A)
_IpCmnMRouteAddrType_Type=InetAddressType
_IpCmnMRouteAddrType_Object=MibTableColumn
ipCmnMRouteAddrType=_IpCmnMRouteAddrType_Object((1,3,6,1,4,1,10876,101,1,126,1,2,1,1,2),_IpCmnMRouteAddrType_Type())
ipCmnMRouteAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:ipCmnMRouteAddrType.setStatus(_A)
class _IpCmnMRouteGroup_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_IpCmnMRouteGroup_Type.__name__=_F
_IpCmnMRouteGroup_Object=MibTableColumn
ipCmnMRouteGroup=_IpCmnMRouteGroup_Object((1,3,6,1,4,1,10876,101,1,126,1,2,1,1,3),_IpCmnMRouteGroup_Type())
ipCmnMRouteGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:ipCmnMRouteGroup.setStatus(_A)
class _IpCmnMRouteSource_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_IpCmnMRouteSource_Type.__name__=_F
_IpCmnMRouteSource_Object=MibTableColumn
ipCmnMRouteSource=_IpCmnMRouteSource_Object((1,3,6,1,4,1,10876,101,1,126,1,2,1,1,4),_IpCmnMRouteSource_Type())
ipCmnMRouteSource.setMaxAccess(_E)
if mibBuilder.loadTexts:ipCmnMRouteSource.setStatus(_A)
class _IpCmnMRouteSourceMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_IpCmnMRouteSourceMask_Type.__name__=_D
_IpCmnMRouteSourceMask_Object=MibTableColumn
ipCmnMRouteSourceMask=_IpCmnMRouteSourceMask_Object((1,3,6,1,4,1,10876,101,1,126,1,2,1,1,5),_IpCmnMRouteSourceMask_Type())
ipCmnMRouteSourceMask.setMaxAccess(_E)
if mibBuilder.loadTexts:ipCmnMRouteSourceMask.setStatus(_A)
class _IpCmnMRouteUpstreamNeighbor_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_IpCmnMRouteUpstreamNeighbor_Type.__name__=_F
_IpCmnMRouteUpstreamNeighbor_Object=MibTableColumn
ipCmnMRouteUpstreamNeighbor=_IpCmnMRouteUpstreamNeighbor_Object((1,3,6,1,4,1,10876,101,1,126,1,2,1,1,6),_IpCmnMRouteUpstreamNeighbor_Type())
ipCmnMRouteUpstreamNeighbor.setMaxAccess(_C)
if mibBuilder.loadTexts:ipCmnMRouteUpstreamNeighbor.setStatus(_A)
_IpCmnMRouteInIfIndex_Type=InterfaceIndexOrZero
_IpCmnMRouteInIfIndex_Object=MibTableColumn
ipCmnMRouteInIfIndex=_IpCmnMRouteInIfIndex_Object((1,3,6,1,4,1,10876,101,1,126,1,2,1,1,7),_IpCmnMRouteInIfIndex_Type())
ipCmnMRouteInIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipCmnMRouteInIfIndex.setStatus(_A)
_IpCmnMRouteUpTime_Type=TimeTicks
_IpCmnMRouteUpTime_Object=MibTableColumn
ipCmnMRouteUpTime=_IpCmnMRouteUpTime_Object((1,3,6,1,4,1,10876,101,1,126,1,2,1,1,8),_IpCmnMRouteUpTime_Type())
ipCmnMRouteUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipCmnMRouteUpTime.setStatus(_A)
_IpCmnMRoutePkts_Type=Counter32
_IpCmnMRoutePkts_Object=MibTableColumn
ipCmnMRoutePkts=_IpCmnMRoutePkts_Object((1,3,6,1,4,1,10876,101,1,126,1,2,1,1,9),_IpCmnMRoutePkts_Type())
ipCmnMRoutePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ipCmnMRoutePkts.setStatus(_A)
_IpCmnMRouteDifferentInIfPackets_Type=Counter32
_IpCmnMRouteDifferentInIfPackets_Object=MibTableColumn
ipCmnMRouteDifferentInIfPackets=_IpCmnMRouteDifferentInIfPackets_Object((1,3,6,1,4,1,10876,101,1,126,1,2,1,1,10),_IpCmnMRouteDifferentInIfPackets_Type())
ipCmnMRouteDifferentInIfPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipCmnMRouteDifferentInIfPackets.setStatus(_A)
_IpCmnMRouteProtocol_Type=IANAipMRouteProtocol
_IpCmnMRouteProtocol_Object=MibTableColumn
ipCmnMRouteProtocol=_IpCmnMRouteProtocol_Object((1,3,6,1,4,1,10876,101,1,126,1,2,1,1,11),_IpCmnMRouteProtocol_Type())
ipCmnMRouteProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ipCmnMRouteProtocol.setStatus(_A)
class _IpCmnMRouteRtAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_IpCmnMRouteRtAddress_Type.__name__=_F
_IpCmnMRouteRtAddress_Object=MibTableColumn
ipCmnMRouteRtAddress=_IpCmnMRouteRtAddress_Object((1,3,6,1,4,1,10876,101,1,126,1,2,1,1,12),_IpCmnMRouteRtAddress_Type())
ipCmnMRouteRtAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ipCmnMRouteRtAddress.setStatus(_A)
class _IpCmnMRouteRtMask_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_IpCmnMRouteRtMask_Type.__name__=_F
_IpCmnMRouteRtMask_Object=MibTableColumn
ipCmnMRouteRtMask=_IpCmnMRouteRtMask_Object((1,3,6,1,4,1,10876,101,1,126,1,2,1,1,13),_IpCmnMRouteRtMask_Type())
ipCmnMRouteRtMask.setMaxAccess(_C)
if mibBuilder.loadTexts:ipCmnMRouteRtMask.setStatus(_A)
class _IpCmnMRouteRtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unicast',1),('multicast',2)))
_IpCmnMRouteRtType_Type.__name__=_D
_IpCmnMRouteRtType_Object=MibTableColumn
ipCmnMRouteRtType=_IpCmnMRouteRtType_Object((1,3,6,1,4,1,10876,101,1,126,1,2,1,1,14),_IpCmnMRouteRtType_Type())
ipCmnMRouteRtType.setMaxAccess(_C)
if mibBuilder.loadTexts:ipCmnMRouteRtType.setStatus(_A)
_IpCmnMRouteNextHopTable_Object=MibTable
ipCmnMRouteNextHopTable=_IpCmnMRouteNextHopTable_Object((1,3,6,1,4,1,10876,101,1,126,1,2,2))
if mibBuilder.loadTexts:ipCmnMRouteNextHopTable.setStatus(_A)
_IpCmnMRouteNextHopEntry_Object=MibTableRow
ipCmnMRouteNextHopEntry=_IpCmnMRouteNextHopEntry_Object((1,3,6,1,4,1,10876,101,1,126,1,2,2,1))
ipCmnMRouteNextHopEntry.setIndexNames((0,_B,_O),(0,_B,_P),(0,_B,_Q),(0,_B,_R),(0,_B,_S),(0,_B,_T),(0,_B,_U))
if mibBuilder.loadTexts:ipCmnMRouteNextHopEntry.setStatus(_A)
class _IpCmnMRouteNextHopOwnerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IpCmnMRouteNextHopOwnerId_Type.__name__=_D
_IpCmnMRouteNextHopOwnerId_Object=MibTableColumn
ipCmnMRouteNextHopOwnerId=_IpCmnMRouteNextHopOwnerId_Object((1,3,6,1,4,1,10876,101,1,126,1,2,2,1,1),_IpCmnMRouteNextHopOwnerId_Type())
ipCmnMRouteNextHopOwnerId.setMaxAccess(_E)
if mibBuilder.loadTexts:ipCmnMRouteNextHopOwnerId.setStatus(_A)
_IpCmnMRouteNextHopAddrType_Type=InetAddressType
_IpCmnMRouteNextHopAddrType_Object=MibTableColumn
ipCmnMRouteNextHopAddrType=_IpCmnMRouteNextHopAddrType_Object((1,3,6,1,4,1,10876,101,1,126,1,2,2,1,2),_IpCmnMRouteNextHopAddrType_Type())
ipCmnMRouteNextHopAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:ipCmnMRouteNextHopAddrType.setStatus(_A)
class _IpCmnMRouteNextHopGroup_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_IpCmnMRouteNextHopGroup_Type.__name__=_F
_IpCmnMRouteNextHopGroup_Object=MibTableColumn
ipCmnMRouteNextHopGroup=_IpCmnMRouteNextHopGroup_Object((1,3,6,1,4,1,10876,101,1,126,1,2,2,1,3),_IpCmnMRouteNextHopGroup_Type())
ipCmnMRouteNextHopGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:ipCmnMRouteNextHopGroup.setStatus(_A)
class _IpCmnMRouteNextHopSource_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_IpCmnMRouteNextHopSource_Type.__name__=_F
_IpCmnMRouteNextHopSource_Object=MibTableColumn
ipCmnMRouteNextHopSource=_IpCmnMRouteNextHopSource_Object((1,3,6,1,4,1,10876,101,1,126,1,2,2,1,4),_IpCmnMRouteNextHopSource_Type())
ipCmnMRouteNextHopSource.setMaxAccess(_E)
if mibBuilder.loadTexts:ipCmnMRouteNextHopSource.setStatus(_A)
class _IpCmnMRouteNextHopSourceMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_IpCmnMRouteNextHopSourceMask_Type.__name__=_D
_IpCmnMRouteNextHopSourceMask_Object=MibTableColumn
ipCmnMRouteNextHopSourceMask=_IpCmnMRouteNextHopSourceMask_Object((1,3,6,1,4,1,10876,101,1,126,1,2,2,1,5),_IpCmnMRouteNextHopSourceMask_Type())
ipCmnMRouteNextHopSourceMask.setMaxAccess(_E)
if mibBuilder.loadTexts:ipCmnMRouteNextHopSourceMask.setStatus(_A)
_IpCmnMRouteNextHopIfIndex_Type=InterfaceIndex
_IpCmnMRouteNextHopIfIndex_Object=MibTableColumn
ipCmnMRouteNextHopIfIndex=_IpCmnMRouteNextHopIfIndex_Object((1,3,6,1,4,1,10876,101,1,126,1,2,2,1,6),_IpCmnMRouteNextHopIfIndex_Type())
ipCmnMRouteNextHopIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ipCmnMRouteNextHopIfIndex.setStatus(_A)
class _IpCmnMRouteNextHopAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_IpCmnMRouteNextHopAddress_Type.__name__=_F
_IpCmnMRouteNextHopAddress_Object=MibTableColumn
ipCmnMRouteNextHopAddress=_IpCmnMRouteNextHopAddress_Object((1,3,6,1,4,1,10876,101,1,126,1,2,2,1,7),_IpCmnMRouteNextHopAddress_Type())
ipCmnMRouteNextHopAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:ipCmnMRouteNextHopAddress.setStatus(_A)
class _IpCmnMRouteNextHopState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pruned',1),('forwarding',2)))
_IpCmnMRouteNextHopState_Type.__name__=_D
_IpCmnMRouteNextHopState_Object=MibTableColumn
ipCmnMRouteNextHopState=_IpCmnMRouteNextHopState_Object((1,3,6,1,4,1,10876,101,1,126,1,2,2,1,8),_IpCmnMRouteNextHopState_Type())
ipCmnMRouteNextHopState.setMaxAccess(_C)
if mibBuilder.loadTexts:ipCmnMRouteNextHopState.setStatus(_A)
_IpCmnMRouteNextHopUpTime_Type=TimeTicks
_IpCmnMRouteNextHopUpTime_Object=MibTableColumn
ipCmnMRouteNextHopUpTime=_IpCmnMRouteNextHopUpTime_Object((1,3,6,1,4,1,10876,101,1,126,1,2,2,1,9),_IpCmnMRouteNextHopUpTime_Type())
ipCmnMRouteNextHopUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipCmnMRouteNextHopUpTime.setStatus(_A)
_IpCmnMRouteInterfaceTable_Object=MibTable
ipCmnMRouteInterfaceTable=_IpCmnMRouteInterfaceTable_Object((1,3,6,1,4,1,10876,101,1,126,1,2,3))
if mibBuilder.loadTexts:ipCmnMRouteInterfaceTable.setStatus(_A)
_IpCmnMRouteInterfaceEntry_Object=MibTableRow
ipCmnMRouteInterfaceEntry=_IpCmnMRouteInterfaceEntry_Object((1,3,6,1,4,1,10876,101,1,126,1,2,3,1))
ipCmnMRouteInterfaceEntry.setIndexNames((0,_B,_V),(0,_B,_W))
if mibBuilder.loadTexts:ipCmnMRouteInterfaceEntry.setStatus(_A)
_IpCmnMRouteInterfaceIfIndex_Type=InterfaceIndex
_IpCmnMRouteInterfaceIfIndex_Object=MibTableColumn
ipCmnMRouteInterfaceIfIndex=_IpCmnMRouteInterfaceIfIndex_Object((1,3,6,1,4,1,10876,101,1,126,1,2,3,1,1),_IpCmnMRouteInterfaceIfIndex_Type())
ipCmnMRouteInterfaceIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ipCmnMRouteInterfaceIfIndex.setStatus(_A)
_IpCmnMRouteInterfaceAddrType_Type=InetAddressType
_IpCmnMRouteInterfaceAddrType_Object=MibTableColumn
ipCmnMRouteInterfaceAddrType=_IpCmnMRouteInterfaceAddrType_Object((1,3,6,1,4,1,10876,101,1,126,1,2,3,1,2),_IpCmnMRouteInterfaceAddrType_Type())
ipCmnMRouteInterfaceAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:ipCmnMRouteInterfaceAddrType.setStatus(_A)
_IpCmnMRouteInterfaceOwnerId_Type=Integer32
_IpCmnMRouteInterfaceOwnerId_Object=MibTableColumn
ipCmnMRouteInterfaceOwnerId=_IpCmnMRouteInterfaceOwnerId_Object((1,3,6,1,4,1,10876,101,1,126,1,2,3,1,3),_IpCmnMRouteInterfaceOwnerId_Type())
ipCmnMRouteInterfaceOwnerId.setMaxAccess(_C)
if mibBuilder.loadTexts:ipCmnMRouteInterfaceOwnerId.setStatus(_A)
class _IpCmnMRouteInterfaceTtl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IpCmnMRouteInterfaceTtl_Type.__name__=_D
_IpCmnMRouteInterfaceTtl_Object=MibTableColumn
ipCmnMRouteInterfaceTtl=_IpCmnMRouteInterfaceTtl_Object((1,3,6,1,4,1,10876,101,1,126,1,2,3,1,4),_IpCmnMRouteInterfaceTtl_Type())
ipCmnMRouteInterfaceTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:ipCmnMRouteInterfaceTtl.setStatus(_A)
_IpCmnMRouteInterfaceProtocol_Type=IANAipMRouteProtocol
_IpCmnMRouteInterfaceProtocol_Object=MibTableColumn
ipCmnMRouteInterfaceProtocol=_IpCmnMRouteInterfaceProtocol_Object((1,3,6,1,4,1,10876,101,1,126,1,2,3,1,5),_IpCmnMRouteInterfaceProtocol_Type())
ipCmnMRouteInterfaceProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ipCmnMRouteInterfaceProtocol.setStatus(_A)
class _IpCmnMRouteInterfaceRateLimit_Type(Integer32):defaultValue=0
_IpCmnMRouteInterfaceRateLimit_Type.__name__=_D
_IpCmnMRouteInterfaceRateLimit_Object=MibTableColumn
ipCmnMRouteInterfaceRateLimit=_IpCmnMRouteInterfaceRateLimit_Object((1,3,6,1,4,1,10876,101,1,126,1,2,3,1,6),_IpCmnMRouteInterfaceRateLimit_Type())
ipCmnMRouteInterfaceRateLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:ipCmnMRouteInterfaceRateLimit.setStatus(_A)
_IpCmnMRouteInterfaceInMcastOctets_Type=Counter32
_IpCmnMRouteInterfaceInMcastOctets_Object=MibTableColumn
ipCmnMRouteInterfaceInMcastOctets=_IpCmnMRouteInterfaceInMcastOctets_Object((1,3,6,1,4,1,10876,101,1,126,1,2,3,1,7),_IpCmnMRouteInterfaceInMcastOctets_Type())
ipCmnMRouteInterfaceInMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipCmnMRouteInterfaceInMcastOctets.setStatus(_A)
_IpCmnMRouteInterfaceCmdbPktCnt_Type=Counter32
_IpCmnMRouteInterfaceCmdbPktCnt_Object=MibTableColumn
ipCmnMRouteInterfaceCmdbPktCnt=_IpCmnMRouteInterfaceCmdbPktCnt_Object((1,3,6,1,4,1,10876,101,1,126,1,2,3,1,8),_IpCmnMRouteInterfaceCmdbPktCnt_Type())
ipCmnMRouteInterfaceCmdbPktCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:ipCmnMRouteInterfaceCmdbPktCnt.setStatus(_A)
_IpCmnMRouteInterfaceOutMcastOctets_Type=Counter32
_IpCmnMRouteInterfaceOutMcastOctets_Object=MibTableColumn
ipCmnMRouteInterfaceOutMcastOctets=_IpCmnMRouteInterfaceOutMcastOctets_Object((1,3,6,1,4,1,10876,101,1,126,1,2,3,1,9),_IpCmnMRouteInterfaceOutMcastOctets_Type())
ipCmnMRouteInterfaceOutMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipCmnMRouteInterfaceOutMcastOctets.setStatus(_A)
_MfwdCmnTraps_ObjectIdentity=ObjectIdentity
mfwdCmnTraps=_MfwdCmnTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,126,1,3))
_IpCmnMRouteMIBConformance_ObjectIdentity=ObjectIdentity
ipCmnMRouteMIBConformance=_IpCmnMRouteMIBConformance_ObjectIdentity((1,3,6,1,4,1,10876,101,1,126,2))
_IpCmnMRouteMIBCompliances_ObjectIdentity=ObjectIdentity
ipCmnMRouteMIBCompliances=_IpCmnMRouteMIBCompliances_ObjectIdentity((1,3,6,1,4,1,10876,101,1,126,2,1))
_IpCmnMRouteMIBGroups_ObjectIdentity=ObjectIdentity
ipCmnMRouteMIBGroups=_IpCmnMRouteMIBGroups_ObjectIdentity((1,3,6,1,4,1,10876,101,1,126,2,2))
ipCmnMRouteMIBBasicGroup=ObjectGroup((1,3,6,1,4,1,10876,101,1,126,2,2,1))
ipCmnMRouteMIBBasicGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h)))
if mibBuilder.loadTexts:ipCmnMRouteMIBBasicGroup.setStatus(_A)
ipCmnMRouteMIBRouteGroup=ObjectGroup((1,3,6,1,4,1,10876,101,1,126,2,2,2))
ipCmnMRouteMIBRouteGroup.setObjects(*((_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:ipCmnMRouteMIBRouteGroup.setStatus(_A)
ipCmnMRouteMIBPktsGroup=ObjectGroup((1,3,6,1,4,1,10876,101,1,126,2,2,3))
ipCmnMRouteMIBPktsGroup.setObjects(*((_B,_l),(_B,_m)))
if mibBuilder.loadTexts:ipCmnMRouteMIBPktsGroup.setStatus(_A)
ipCmnMRouteMIBCompliance=ModuleCompliance((1,3,6,1,4,1,10876,101,1,126,2,1,1))
ipCmnMRouteMIBCompliance.setObjects(*((_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:ipCmnMRouteMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Status':Status,'ipCmnMRouteMIB':ipCmnMRouteMIB,'mfwdCmnMIBObjects':mfwdCmnMIBObjects,'mfwdCmnScalars':mfwdCmnScalars,_X:ipCmnMRouteEnable,_Y:ipCmnMRouteEntryCount,'ipCmnMRouteEnableCmdb':ipCmnMRouteEnableCmdb,'mfwdCmnGlobalTrace':mfwdCmnGlobalTrace,'mfwdCmnGlobalDebug':mfwdCmnGlobalDebug,'ipCmnMRouteDiscardedPkts':ipCmnMRouteDiscardedPkts,'mfwdCmnAvgDataRate':mfwdCmnAvgDataRate,'mfwdCmnTables':mfwdCmnTables,'ipCmnMRouteTable':ipCmnMRouteTable,'ipCmnMRouteEntry':ipCmnMRouteEntry,_J:ipCmnMRouteOwnerId,_K:ipCmnMRouteAddrType,_L:ipCmnMRouteGroup,_M:ipCmnMRouteSource,_N:ipCmnMRouteSourceMask,_Z:ipCmnMRouteUpstreamNeighbor,_a:ipCmnMRouteInIfIndex,_b:ipCmnMRouteUpTime,_l:ipCmnMRoutePkts,_m:ipCmnMRouteDifferentInIfPackets,_h:ipCmnMRouteProtocol,_i:ipCmnMRouteRtAddress,_j:ipCmnMRouteRtMask,_k:ipCmnMRouteRtType,'ipCmnMRouteNextHopTable':ipCmnMRouteNextHopTable,'ipCmnMRouteNextHopEntry':ipCmnMRouteNextHopEntry,_O:ipCmnMRouteNextHopOwnerId,_P:ipCmnMRouteNextHopAddrType,_Q:ipCmnMRouteNextHopGroup,_R:ipCmnMRouteNextHopSource,_S:ipCmnMRouteNextHopSourceMask,_T:ipCmnMRouteNextHopIfIndex,_U:ipCmnMRouteNextHopAddress,_c:ipCmnMRouteNextHopState,_d:ipCmnMRouteNextHopUpTime,'ipCmnMRouteInterfaceTable':ipCmnMRouteInterfaceTable,'ipCmnMRouteInterfaceEntry':ipCmnMRouteInterfaceEntry,_V:ipCmnMRouteInterfaceIfIndex,_W:ipCmnMRouteInterfaceAddrType,'ipCmnMRouteInterfaceOwnerId':ipCmnMRouteInterfaceOwnerId,_e:ipCmnMRouteInterfaceTtl,_f:ipCmnMRouteInterfaceProtocol,_g:ipCmnMRouteInterfaceRateLimit,'ipCmnMRouteInterfaceInMcastOctets':ipCmnMRouteInterfaceInMcastOctets,'ipCmnMRouteInterfaceCmdbPktCnt':ipCmnMRouteInterfaceCmdbPktCnt,'ipCmnMRouteInterfaceOutMcastOctets':ipCmnMRouteInterfaceOutMcastOctets,'mfwdCmnTraps':mfwdCmnTraps,'ipCmnMRouteMIBConformance':ipCmnMRouteMIBConformance,'ipCmnMRouteMIBCompliances':ipCmnMRouteMIBCompliances,'ipCmnMRouteMIBCompliance':ipCmnMRouteMIBCompliance,'ipCmnMRouteMIBGroups':ipCmnMRouteMIBGroups,_n:ipCmnMRouteMIBBasicGroup,_o:ipCmnMRouteMIBRouteGroup,_p:ipCmnMRouteMIBPktsGroup})