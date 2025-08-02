_k='ipMRouteMIBRouteGroup'
_j='ipMRouteMIBBasicGroup'
_i='ipMRouteDifferentInIfPackets'
_h='ipMRoutePkts'
_g='ipMRouteRtType'
_f='ipMRouteRtMask'
_e='ipMRouteRtAddress'
_d='ipMRouteProtocol'
_c='ipMRouteInterfaceRateLimit'
_b='ipMRouteInterfaceProtocol'
_a='ipMRouteInterfaceTtl'
_Z='ipMRouteNextHopUpTime'
_Y='ipMRouteNextHopState'
_X='ipMRouteUpTime'
_W='ipMRouteInIfIndex'
_V='ipMRouteUpstreamNeighbor'
_U='ipMRouteEntryCount'
_T='ipMRouteEnable'
_S='ipMRouteInterfaceIfIndex'
_R='ipMRouteNextHopAddress'
_Q='ipMRouteNextHopIfIndex'
_P='ipMRouteNextHopSourceMask'
_O='ipMRouteNextHopSource'
_N='ipMRouteNextHopGroup'
_M='ipMRouteNextHopOwnerId'
_L='ipMRouteSourceMask'
_K='ipMRouteSource'
_J='ipMRouteGroup'
_I='ipMRouteOwnerId'
_H='disabled'
_G='enable'
_F='read-write'
_E='not-accessible'
_D='Integer32'
_C='read-only'
_B='ARICENT-IPMROUTE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IANAipMRouteProtocol,=mibBuilder.importSymbols('IANA-RTPROTO-MIB','IANAipMRouteProtocol')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','mib-2')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
ipMRouteMIB=ModuleIdentity((1,3,6,1,4,1,2076,71))
if mibBuilder.loadTexts:ipMRouteMIB.setRevisions(('2012-09-05 00:00',))
class Status(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),('disable',2)))
_MfwdMIBObjects_ObjectIdentity=ObjectIdentity
mfwdMIBObjects=_MfwdMIBObjects_ObjectIdentity((1,3,6,1,4,1,2076,71,1))
_MfwdScalars_ObjectIdentity=ObjectIdentity
mfwdScalars=_MfwdScalars_ObjectIdentity((1,3,6,1,4,1,2076,71,1,1))
class _IpMRouteEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_H,2)))
_IpMRouteEnable_Type.__name__=_D
_IpMRouteEnable_Object=MibScalar
ipMRouteEnable=_IpMRouteEnable_Object((1,3,6,1,4,1,2076,71,1,1,1),_IpMRouteEnable_Type())
ipMRouteEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:ipMRouteEnable.setStatus(_A)
_IpMRouteEntryCount_Type=Gauge32
_IpMRouteEntryCount_Object=MibScalar
ipMRouteEntryCount=_IpMRouteEntryCount_Object((1,3,6,1,4,1,2076,71,1,1,2),_IpMRouteEntryCount_Type())
ipMRouteEntryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteEntryCount.setStatus(_A)
class _IpMRouteEnableCmdb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_IpMRouteEnableCmdb_Type.__name__=_D
_IpMRouteEnableCmdb_Object=MibScalar
ipMRouteEnableCmdb=_IpMRouteEnableCmdb_Object((1,3,6,1,4,1,2076,71,1,1,3),_IpMRouteEnableCmdb_Type())
ipMRouteEnableCmdb.setMaxAccess(_F)
if mibBuilder.loadTexts:ipMRouteEnableCmdb.setStatus(_A)
class _MfwdGlobalTrace_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MfwdGlobalTrace_Type.__name__=_D
_MfwdGlobalTrace_Object=MibScalar
mfwdGlobalTrace=_MfwdGlobalTrace_Object((1,3,6,1,4,1,2076,71,1,1,4),_MfwdGlobalTrace_Type())
mfwdGlobalTrace.setMaxAccess(_F)
if mibBuilder.loadTexts:mfwdGlobalTrace.setStatus(_A)
class _MfwdGlobalDebug_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MfwdGlobalDebug_Type.__name__=_D
_MfwdGlobalDebug_Object=MibScalar
mfwdGlobalDebug=_MfwdGlobalDebug_Object((1,3,6,1,4,1,2076,71,1,1,5),_MfwdGlobalDebug_Type())
mfwdGlobalDebug.setMaxAccess(_F)
if mibBuilder.loadTexts:mfwdGlobalDebug.setStatus(_A)
_IpMRouteDiscardedPkts_Type=Counter32
_IpMRouteDiscardedPkts_Object=MibScalar
ipMRouteDiscardedPkts=_IpMRouteDiscardedPkts_Object((1,3,6,1,4,1,2076,71,1,1,6),_IpMRouteDiscardedPkts_Type())
ipMRouteDiscardedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteDiscardedPkts.setStatus(_A)
class _MfwdAvgDataRate_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MfwdAvgDataRate_Type.__name__=_D
_MfwdAvgDataRate_Object=MibScalar
mfwdAvgDataRate=_MfwdAvgDataRate_Object((1,3,6,1,4,1,2076,71,1,1,7),_MfwdAvgDataRate_Type())
mfwdAvgDataRate.setMaxAccess(_F)
if mibBuilder.loadTexts:mfwdAvgDataRate.setStatus(_A)
_MfwdTables_ObjectIdentity=ObjectIdentity
mfwdTables=_MfwdTables_ObjectIdentity((1,3,6,1,4,1,2076,71,1,2))
_IpMRouteTable_Object=MibTable
ipMRouteTable=_IpMRouteTable_Object((1,3,6,1,4,1,2076,71,1,2,1))
if mibBuilder.loadTexts:ipMRouteTable.setStatus(_A)
_IpMRouteEntry_Object=MibTableRow
ipMRouteEntry=_IpMRouteEntry_Object((1,3,6,1,4,1,2076,71,1,2,1,1))
ipMRouteEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:ipMRouteEntry.setStatus(_A)
class _IpMRouteOwnerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IpMRouteOwnerId_Type.__name__=_D
_IpMRouteOwnerId_Object=MibTableColumn
ipMRouteOwnerId=_IpMRouteOwnerId_Object((1,3,6,1,4,1,2076,71,1,2,1,1,1),_IpMRouteOwnerId_Type())
ipMRouteOwnerId.setMaxAccess(_E)
if mibBuilder.loadTexts:ipMRouteOwnerId.setStatus(_A)
_IpMRouteGroup_Type=IpAddress
_IpMRouteGroup_Object=MibTableColumn
ipMRouteGroup=_IpMRouteGroup_Object((1,3,6,1,4,1,2076,71,1,2,1,1,2),_IpMRouteGroup_Type())
ipMRouteGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:ipMRouteGroup.setStatus(_A)
_IpMRouteSource_Type=IpAddress
_IpMRouteSource_Object=MibTableColumn
ipMRouteSource=_IpMRouteSource_Object((1,3,6,1,4,1,2076,71,1,2,1,1,3),_IpMRouteSource_Type())
ipMRouteSource.setMaxAccess(_E)
if mibBuilder.loadTexts:ipMRouteSource.setStatus(_A)
_IpMRouteSourceMask_Type=IpAddress
_IpMRouteSourceMask_Object=MibTableColumn
ipMRouteSourceMask=_IpMRouteSourceMask_Object((1,3,6,1,4,1,2076,71,1,2,1,1,4),_IpMRouteSourceMask_Type())
ipMRouteSourceMask.setMaxAccess(_E)
if mibBuilder.loadTexts:ipMRouteSourceMask.setStatus(_A)
_IpMRouteUpstreamNeighbor_Type=IpAddress
_IpMRouteUpstreamNeighbor_Object=MibTableColumn
ipMRouteUpstreamNeighbor=_IpMRouteUpstreamNeighbor_Object((1,3,6,1,4,1,2076,71,1,2,1,1,5),_IpMRouteUpstreamNeighbor_Type())
ipMRouteUpstreamNeighbor.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteUpstreamNeighbor.setStatus(_A)
_IpMRouteInIfIndex_Type=InterfaceIndexOrZero
_IpMRouteInIfIndex_Object=MibTableColumn
ipMRouteInIfIndex=_IpMRouteInIfIndex_Object((1,3,6,1,4,1,2076,71,1,2,1,1,6),_IpMRouteInIfIndex_Type())
ipMRouteInIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteInIfIndex.setStatus(_A)
_IpMRouteUpTime_Type=TimeTicks
_IpMRouteUpTime_Object=MibTableColumn
ipMRouteUpTime=_IpMRouteUpTime_Object((1,3,6,1,4,1,2076,71,1,2,1,1,7),_IpMRouteUpTime_Type())
ipMRouteUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteUpTime.setStatus(_A)
_IpMRoutePkts_Type=Counter32
_IpMRoutePkts_Object=MibTableColumn
ipMRoutePkts=_IpMRoutePkts_Object((1,3,6,1,4,1,2076,71,1,2,1,1,8),_IpMRoutePkts_Type())
ipMRoutePkts.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRoutePkts.setStatus(_A)
_IpMRouteDifferentInIfPackets_Type=Counter32
_IpMRouteDifferentInIfPackets_Object=MibTableColumn
ipMRouteDifferentInIfPackets=_IpMRouteDifferentInIfPackets_Object((1,3,6,1,4,1,2076,71,1,2,1,1,9),_IpMRouteDifferentInIfPackets_Type())
ipMRouteDifferentInIfPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteDifferentInIfPackets.setStatus(_A)
_IpMRouteProtocol_Type=IANAipMRouteProtocol
_IpMRouteProtocol_Object=MibTableColumn
ipMRouteProtocol=_IpMRouteProtocol_Object((1,3,6,1,4,1,2076,71,1,2,1,1,10),_IpMRouteProtocol_Type())
ipMRouteProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteProtocol.setStatus(_A)
_IpMRouteRtAddress_Type=IpAddress
_IpMRouteRtAddress_Object=MibTableColumn
ipMRouteRtAddress=_IpMRouteRtAddress_Object((1,3,6,1,4,1,2076,71,1,2,1,1,11),_IpMRouteRtAddress_Type())
ipMRouteRtAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteRtAddress.setStatus(_A)
_IpMRouteRtMask_Type=IpAddress
_IpMRouteRtMask_Object=MibTableColumn
ipMRouteRtMask=_IpMRouteRtMask_Object((1,3,6,1,4,1,2076,71,1,2,1,1,12),_IpMRouteRtMask_Type())
ipMRouteRtMask.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteRtMask.setStatus(_A)
class _IpMRouteRtType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unicast',1),('multicast',2)))
_IpMRouteRtType_Type.__name__=_D
_IpMRouteRtType_Object=MibTableColumn
ipMRouteRtType=_IpMRouteRtType_Object((1,3,6,1,4,1,2076,71,1,2,1,1,13),_IpMRouteRtType_Type())
ipMRouteRtType.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteRtType.setStatus(_A)
_IpMRouteNextHopTable_Object=MibTable
ipMRouteNextHopTable=_IpMRouteNextHopTable_Object((1,3,6,1,4,1,2076,71,1,2,2))
if mibBuilder.loadTexts:ipMRouteNextHopTable.setStatus(_A)
_IpMRouteNextHopEntry_Object=MibTableRow
ipMRouteNextHopEntry=_IpMRouteNextHopEntry_Object((1,3,6,1,4,1,2076,71,1,2,2,1))
ipMRouteNextHopEntry.setIndexNames((0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_P),(0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:ipMRouteNextHopEntry.setStatus(_A)
class _IpMRouteNextHopOwnerId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IpMRouteNextHopOwnerId_Type.__name__=_D
_IpMRouteNextHopOwnerId_Object=MibTableColumn
ipMRouteNextHopOwnerId=_IpMRouteNextHopOwnerId_Object((1,3,6,1,4,1,2076,71,1,2,2,1,1),_IpMRouteNextHopOwnerId_Type())
ipMRouteNextHopOwnerId.setMaxAccess(_E)
if mibBuilder.loadTexts:ipMRouteNextHopOwnerId.setStatus(_A)
_IpMRouteNextHopGroup_Type=IpAddress
_IpMRouteNextHopGroup_Object=MibTableColumn
ipMRouteNextHopGroup=_IpMRouteNextHopGroup_Object((1,3,6,1,4,1,2076,71,1,2,2,1,2),_IpMRouteNextHopGroup_Type())
ipMRouteNextHopGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:ipMRouteNextHopGroup.setStatus(_A)
_IpMRouteNextHopSource_Type=IpAddress
_IpMRouteNextHopSource_Object=MibTableColumn
ipMRouteNextHopSource=_IpMRouteNextHopSource_Object((1,3,6,1,4,1,2076,71,1,2,2,1,3),_IpMRouteNextHopSource_Type())
ipMRouteNextHopSource.setMaxAccess(_E)
if mibBuilder.loadTexts:ipMRouteNextHopSource.setStatus(_A)
_IpMRouteNextHopSourceMask_Type=IpAddress
_IpMRouteNextHopSourceMask_Object=MibTableColumn
ipMRouteNextHopSourceMask=_IpMRouteNextHopSourceMask_Object((1,3,6,1,4,1,2076,71,1,2,2,1,4),_IpMRouteNextHopSourceMask_Type())
ipMRouteNextHopSourceMask.setMaxAccess(_E)
if mibBuilder.loadTexts:ipMRouteNextHopSourceMask.setStatus(_A)
_IpMRouteNextHopIfIndex_Type=InterfaceIndex
_IpMRouteNextHopIfIndex_Object=MibTableColumn
ipMRouteNextHopIfIndex=_IpMRouteNextHopIfIndex_Object((1,3,6,1,4,1,2076,71,1,2,2,1,5),_IpMRouteNextHopIfIndex_Type())
ipMRouteNextHopIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ipMRouteNextHopIfIndex.setStatus(_A)
_IpMRouteNextHopAddress_Type=IpAddress
_IpMRouteNextHopAddress_Object=MibTableColumn
ipMRouteNextHopAddress=_IpMRouteNextHopAddress_Object((1,3,6,1,4,1,2076,71,1,2,2,1,6),_IpMRouteNextHopAddress_Type())
ipMRouteNextHopAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:ipMRouteNextHopAddress.setStatus(_A)
class _IpMRouteNextHopState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pruned',1),('forwarding',2)))
_IpMRouteNextHopState_Type.__name__=_D
_IpMRouteNextHopState_Object=MibTableColumn
ipMRouteNextHopState=_IpMRouteNextHopState_Object((1,3,6,1,4,1,2076,71,1,2,2,1,7),_IpMRouteNextHopState_Type())
ipMRouteNextHopState.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteNextHopState.setStatus(_A)
_IpMRouteNextHopUpTime_Type=TimeTicks
_IpMRouteNextHopUpTime_Object=MibTableColumn
ipMRouteNextHopUpTime=_IpMRouteNextHopUpTime_Object((1,3,6,1,4,1,2076,71,1,2,2,1,8),_IpMRouteNextHopUpTime_Type())
ipMRouteNextHopUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteNextHopUpTime.setStatus(_A)
_IpMRouteInterfaceTable_Object=MibTable
ipMRouteInterfaceTable=_IpMRouteInterfaceTable_Object((1,3,6,1,4,1,2076,71,1,2,3))
if mibBuilder.loadTexts:ipMRouteInterfaceTable.setStatus(_A)
_IpMRouteInterfaceEntry_Object=MibTableRow
ipMRouteInterfaceEntry=_IpMRouteInterfaceEntry_Object((1,3,6,1,4,1,2076,71,1,2,3,1))
ipMRouteInterfaceEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:ipMRouteInterfaceEntry.setStatus(_A)
_IpMRouteInterfaceIfIndex_Type=InterfaceIndex
_IpMRouteInterfaceIfIndex_Object=MibTableColumn
ipMRouteInterfaceIfIndex=_IpMRouteInterfaceIfIndex_Object((1,3,6,1,4,1,2076,71,1,2,3,1,1),_IpMRouteInterfaceIfIndex_Type())
ipMRouteInterfaceIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ipMRouteInterfaceIfIndex.setStatus(_A)
_IpMRouteInterfaceOwnerId_Type=Integer32
_IpMRouteInterfaceOwnerId_Object=MibTableColumn
ipMRouteInterfaceOwnerId=_IpMRouteInterfaceOwnerId_Object((1,3,6,1,4,1,2076,71,1,2,3,1,2),_IpMRouteInterfaceOwnerId_Type())
ipMRouteInterfaceOwnerId.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteInterfaceOwnerId.setStatus(_A)
class _IpMRouteInterfaceTtl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IpMRouteInterfaceTtl_Type.__name__=_D
_IpMRouteInterfaceTtl_Object=MibTableColumn
ipMRouteInterfaceTtl=_IpMRouteInterfaceTtl_Object((1,3,6,1,4,1,2076,71,1,2,3,1,3),_IpMRouteInterfaceTtl_Type())
ipMRouteInterfaceTtl.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteInterfaceTtl.setStatus(_A)
_IpMRouteInterfaceProtocol_Type=IANAipMRouteProtocol
_IpMRouteInterfaceProtocol_Object=MibTableColumn
ipMRouteInterfaceProtocol=_IpMRouteInterfaceProtocol_Object((1,3,6,1,4,1,2076,71,1,2,3,1,4),_IpMRouteInterfaceProtocol_Type())
ipMRouteInterfaceProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteInterfaceProtocol.setStatus(_A)
class _IpMRouteInterfaceRateLimit_Type(Integer32):defaultValue=0
_IpMRouteInterfaceRateLimit_Type.__name__=_D
_IpMRouteInterfaceRateLimit_Object=MibTableColumn
ipMRouteInterfaceRateLimit=_IpMRouteInterfaceRateLimit_Object((1,3,6,1,4,1,2076,71,1,2,3,1,5),_IpMRouteInterfaceRateLimit_Type())
ipMRouteInterfaceRateLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteInterfaceRateLimit.setStatus(_A)
_IpMRouteInterfaceInMcastOctets_Type=Counter32
_IpMRouteInterfaceInMcastOctets_Object=MibTableColumn
ipMRouteInterfaceInMcastOctets=_IpMRouteInterfaceInMcastOctets_Object((1,3,6,1,4,1,2076,71,1,2,3,1,6),_IpMRouteInterfaceInMcastOctets_Type())
ipMRouteInterfaceInMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteInterfaceInMcastOctets.setStatus(_A)
_IpMRouteInterfaceCmdbPktCnt_Type=Counter32
_IpMRouteInterfaceCmdbPktCnt_Object=MibTableColumn
ipMRouteInterfaceCmdbPktCnt=_IpMRouteInterfaceCmdbPktCnt_Object((1,3,6,1,4,1,2076,71,1,2,3,1,7),_IpMRouteInterfaceCmdbPktCnt_Type())
ipMRouteInterfaceCmdbPktCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteInterfaceCmdbPktCnt.setStatus(_A)
_IpMRouteInterfaceOutMcastOctets_Type=Counter32
_IpMRouteInterfaceOutMcastOctets_Object=MibTableColumn
ipMRouteInterfaceOutMcastOctets=_IpMRouteInterfaceOutMcastOctets_Object((1,3,6,1,4,1,2076,71,1,2,3,1,8),_IpMRouteInterfaceOutMcastOctets_Type())
ipMRouteInterfaceOutMcastOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ipMRouteInterfaceOutMcastOctets.setStatus(_A)
_MfwdTraps_ObjectIdentity=ObjectIdentity
mfwdTraps=_MfwdTraps_ObjectIdentity((1,3,6,1,4,1,2076,71,1,3))
_IpMRouteMIBConformance_ObjectIdentity=ObjectIdentity
ipMRouteMIBConformance=_IpMRouteMIBConformance_ObjectIdentity((1,3,6,1,4,1,2076,71,2))
_IpMRouteMIBCompliances_ObjectIdentity=ObjectIdentity
ipMRouteMIBCompliances=_IpMRouteMIBCompliances_ObjectIdentity((1,3,6,1,4,1,2076,71,2,1))
_IpMRouteMIBGroups_ObjectIdentity=ObjectIdentity
ipMRouteMIBGroups=_IpMRouteMIBGroups_ObjectIdentity((1,3,6,1,4,1,2076,71,2,2))
ipMRouteMIBBasicGroup=ObjectGroup((1,3,6,1,4,1,2076,71,2,2,1))
ipMRouteMIBBasicGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:ipMRouteMIBBasicGroup.setStatus(_A)
ipMRouteMIBRouteGroup=ObjectGroup((1,3,6,1,4,1,2076,71,2,2,2))
ipMRouteMIBRouteGroup.setObjects(*((_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:ipMRouteMIBRouteGroup.setStatus(_A)
ipMRouteMIBPktsGroup=ObjectGroup((1,3,6,1,4,1,2076,71,2,2,3))
ipMRouteMIBPktsGroup.setObjects(*((_B,_h),(_B,_i)))
if mibBuilder.loadTexts:ipMRouteMIBPktsGroup.setStatus(_A)
ipMRouteMIBCompliance=ModuleCompliance((1,3,6,1,4,1,2076,71,2,1,1))
ipMRouteMIBCompliance.setObjects(*((_B,_j),(_B,_k)))
if mibBuilder.loadTexts:ipMRouteMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Status':Status,'ipMRouteMIB':ipMRouteMIB,'mfwdMIBObjects':mfwdMIBObjects,'mfwdScalars':mfwdScalars,_T:ipMRouteEnable,_U:ipMRouteEntryCount,'ipMRouteEnableCmdb':ipMRouteEnableCmdb,'mfwdGlobalTrace':mfwdGlobalTrace,'mfwdGlobalDebug':mfwdGlobalDebug,'ipMRouteDiscardedPkts':ipMRouteDiscardedPkts,'mfwdAvgDataRate':mfwdAvgDataRate,'mfwdTables':mfwdTables,'ipMRouteTable':ipMRouteTable,'ipMRouteEntry':ipMRouteEntry,_I:ipMRouteOwnerId,_J:ipMRouteGroup,_K:ipMRouteSource,_L:ipMRouteSourceMask,_V:ipMRouteUpstreamNeighbor,_W:ipMRouteInIfIndex,_X:ipMRouteUpTime,_h:ipMRoutePkts,_i:ipMRouteDifferentInIfPackets,_d:ipMRouteProtocol,_e:ipMRouteRtAddress,_f:ipMRouteRtMask,_g:ipMRouteRtType,'ipMRouteNextHopTable':ipMRouteNextHopTable,'ipMRouteNextHopEntry':ipMRouteNextHopEntry,_M:ipMRouteNextHopOwnerId,_N:ipMRouteNextHopGroup,_O:ipMRouteNextHopSource,_P:ipMRouteNextHopSourceMask,_Q:ipMRouteNextHopIfIndex,_R:ipMRouteNextHopAddress,_Y:ipMRouteNextHopState,_Z:ipMRouteNextHopUpTime,'ipMRouteInterfaceTable':ipMRouteInterfaceTable,'ipMRouteInterfaceEntry':ipMRouteInterfaceEntry,_S:ipMRouteInterfaceIfIndex,'ipMRouteInterfaceOwnerId':ipMRouteInterfaceOwnerId,_a:ipMRouteInterfaceTtl,_b:ipMRouteInterfaceProtocol,_c:ipMRouteInterfaceRateLimit,'ipMRouteInterfaceInMcastOctets':ipMRouteInterfaceInMcastOctets,'ipMRouteInterfaceCmdbPktCnt':ipMRouteInterfaceCmdbPktCnt,'ipMRouteInterfaceOutMcastOctets':ipMRouteInterfaceOutMcastOctets,'mfwdTraps':mfwdTraps,'ipMRouteMIBConformance':ipMRouteMIBConformance,'ipMRouteMIBCompliances':ipMRouteMIBCompliances,'ipMRouteMIBCompliance':ipMRouteMIBCompliance,'ipMRouteMIBGroups':ipMRouteMIBGroups,_j:ipMRouteMIBBasicGroup,_k:ipMRouteMIBRouteGroup,'ipMRouteMIBPktsGroup':ipMRouteMIBPktsGroup})