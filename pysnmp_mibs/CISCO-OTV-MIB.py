_B3='ciscoOtvMcastRouteInfoGroup'
_B2='ciscoOtvMcastRouteGroup'
_B1='ciscoOtvRouteGroup'
_B0='ciscoOtvArpNdCacheGroup'
_A_='ciscoOtvAdjacencyGroup'
_Az='ciscoOtvDataGroupInfoGroup'
_Ay='ciscoOtvDataGroupConfigGroup'
_Ax='ciscoOtvVlanGroup'
_Aw='ciscoOtvOverlayGroup'
_Av='ciscoOtvSiteGroup'
_Au='cotvMcastRouteInfoUpTime'
_At='cotvMcastRouteInfoMetric'
_As='cotvMcastRouteInfoProtocolOwners'
_Ar='cotvMcastRouteInfoHostAddr'
_Aq='cotvMcastRouteInfoHostAddrType'
_Ap='cotvMcastRouteUpTime'
_Ao='cotvMcastRouteMetric'
_An='cotvMcastRouteOwners'
_Am='cotvRouteNextHopAddr'
_Al='cotvRouteNextHopAddrType'
_Ak='cotvRouteNextHopIf'
_Aj='cotvRouteOwner'
_Ai='cotvRouteUpTime'
_Ah='cotvRouteMetric'
_Ag='cotvArpNdCacheTimeToExpire'
_Af='cotvArpNdCacheAge'
_Ae='cotvArpNdCacheMacAddr'
_Ad='cotvAdjacentDevUpTime'
_Ac='cotvAdjacentDevState'
_Ab='cotvAdjacentDevName'
_Aa='cotvAdjacentDevSystemID'
_AZ='cotvDataGroupLocalActiveSrcState'
_AY='cotvDataGroupJoinInterface'
_AX='cotvDataGroupRowStatus'
_AW='cotvDataGroupStorageType'
_AV='cotvVlanEdgeDevIsAed'
_AU='cotvVlanAedAddr'
_AT='cotvVlanAedAddrType'
_AS='cotvVlanInactiveReason'
_AR='cotvVlanState'
_AQ='cotvOverlayRowStatus'
_AP='cotvOverlayStorageType'
_AO='cotvOverlaySuppressArpND'
_AN='cotvOverlaySecondaryAdjServerAddr'
_AM='cotvOverlaySecondaryAdjServerAddrType'
_AL='cotvOverlayPrimaryAdjServerAddr'
_AK='cotvOverlayPrimaryAdjServerAddrType'
_AJ='cotvOverlayAdjServerEnable'
_AI='cotvOverlayAdjServerTransportType'
_AH='cotvOverlayAedIncapableReason'
_AG='cotvOverlayAedCapable'
_AF='cotvOverlaySourceInterface'
_AE='cotvOverlayJoinInterface'
_AD='cotvOverlayBroadcastGroupAddr'
_AC='cotvOverlayBroadcastGroupAddrType'
_AB='cotvOverlayControlGroupAddr'
_AA='cotvOverlayControlGroupAddrType'
_A9='cotvOverlayVlansExtendedSecond2k'
_A8='cotvOverlayVlansExtendedFirst2k'
_A7='cotvOverlayVpnDownReason'
_A6='cotvOverlayVpnState'
_A5='cotvOverlayVpnName'
_A4='cotvSiteVlanState'
_A3='cotvSiteVlan'
_A2='cotvSiteIdOper'
_A1='cotvSiteIdAdmin'
_A0='cotvMcastRouteInfoIf'
_z='cotvMcastRouteInfoActiveGroupAddr'
_y='cotvMcastRouteInfoActiveGroupAddrType'
_x='cotvMcastRouteInfoActiveSrcAddr'
_w='cotvMcastRouteInfoActiveSrcAddrType'
_v='cotvMcastRouteInfoVlanId'
_u='cotvMcastRouteActiveGroupAddr'
_t='cotvMcastRouteActiveGroupAddrType'
_s='cotvMcastRouteActiveSrcAddr'
_r='cotvMcastRouteActiveSrcAddrType'
_q='cotvMcastRouteVlanId'
_p='cotvRouteMacAddr'
_o='cotvRouteVlanId'
_n='cotvArpNdCacheL3Addr'
_m='cotvArpNdCacheL3AddrType'
_l='cotvAdjacentDevAddr'
_k='cotvAdjacentDevAddrType'
_j='remote'
_i='cotvDataGroupDeliverySrcAddr'
_h='cotvDataGroupDeliverySrcAddrType'
_g='cotvDataGroupDeliveryGroupAddr'
_f='cotvDataGroupDeliveryGroupAddrType'
_e='cotvDataGroupActiveSrcAddr'
_d='cotvDataGroupActiveSrcAddrType'
_c='cotvDataGroupActiveGroupAddr'
_b='cotvDataGroupActiveGroupAddrType'
_a='cotvDataGroupVlanId'
_Z='cotvDataGroupActiveSrcLocation'
_Y='cotvDataGroupMcastRangePrefixLength'
_X='cotvDataGroupMcastRangeAddr'
_W='cotvDataGroupMcastRangeAddrType'
_V='overlayDown'
_U='siteIdMismatch'
_T='deleteHoldDown'
_S='read-write'
_R='cotvVlanId'
_Q='down'
_P='TruthValue'
_O='StorageType'
_N='InterfaceIndexOrZero'
_M='Cisco2KVlanList'
_L='OctetString'
_K='other'
_J='InetAddressType'
_I='seconds'
_H='cotvOverlayNumber'
_G='Integer32'
_F='InetAddress'
_E='read-create'
_D='not-accessible'
_C='read-only'
_B='CISCO-OTV-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_L,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
Cisco2KVlanList,=mibBuilder.importSymbols('CISCO-TC',_M)
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_N)
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_F,'InetAddressPrefixLength',_J)
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus',_O,'TextualConvention',_P)
ciscoOtvMIB=ModuleIdentity((1,3,6,1,4,1,9,9,810))
if mibBuilder.loadTexts:ciscoOtvMIB.setRevisions(('2013-08-05 00:00',))
_CiscoOtvMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoOtvMIBNotifs=_CiscoOtvMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,810,0))
_CiscoOtvMIBObjects_ObjectIdentity=ObjectIdentity
ciscoOtvMIBObjects=_CiscoOtvMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,810,1))
_CotvGlobalObjects_ObjectIdentity=ObjectIdentity
cotvGlobalObjects=_CotvGlobalObjects_ObjectIdentity((1,3,6,1,4,1,9,9,810,1,1))
_CotvSiteObjects_ObjectIdentity=ObjectIdentity
cotvSiteObjects=_CotvSiteObjects_ObjectIdentity((1,3,6,1,4,1,9,9,810,1,1,1))
class _CotvSiteIdAdmin_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(6,6))
_CotvSiteIdAdmin_Type.__name__=_L
_CotvSiteIdAdmin_Object=MibScalar
cotvSiteIdAdmin=_CotvSiteIdAdmin_Object((1,3,6,1,4,1,9,9,810,1,1,1,1),_CotvSiteIdAdmin_Type())
cotvSiteIdAdmin.setMaxAccess(_S)
if mibBuilder.loadTexts:cotvSiteIdAdmin.setStatus(_A)
class _CotvSiteIdOper_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_CotvSiteIdOper_Type.__name__=_L
_CotvSiteIdOper_Object=MibScalar
cotvSiteIdOper=_CotvSiteIdOper_Object((1,3,6,1,4,1,9,9,810,1,1,1,2),_CotvSiteIdOper_Type())
cotvSiteIdOper.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvSiteIdOper.setStatus(_A)
_CotvSiteVlan_Type=VlanIndex
_CotvSiteVlan_Object=MibScalar
cotvSiteVlan=_CotvSiteVlan_Object((1,3,6,1,4,1,9,9,810,1,1,1,3),_CotvSiteVlan_Type())
cotvSiteVlan.setMaxAccess(_S)
if mibBuilder.loadTexts:cotvSiteVlan.setStatus(_A)
class _CotvSiteVlanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_Q,2)))
_CotvSiteVlanState_Type.__name__=_G
_CotvSiteVlanState_Object=MibScalar
cotvSiteVlanState=_CotvSiteVlanState_Object((1,3,6,1,4,1,9,9,810,1,1,1,4),_CotvSiteVlanState_Type())
cotvSiteVlanState.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvSiteVlanState.setStatus(_A)
_CotvGlobalStatsObjects_ObjectIdentity=ObjectIdentity
cotvGlobalStatsObjects=_CotvGlobalStatsObjects_ObjectIdentity((1,3,6,1,4,1,9,9,810,1,1,2))
_CotvOverlayObjects_ObjectIdentity=ObjectIdentity
cotvOverlayObjects=_CotvOverlayObjects_ObjectIdentity((1,3,6,1,4,1,9,9,810,1,2))
_CotvOverlayTable_Object=MibTable
cotvOverlayTable=_CotvOverlayTable_Object((1,3,6,1,4,1,9,9,810,1,2,1))
if mibBuilder.loadTexts:cotvOverlayTable.setStatus(_A)
_CotvOverlayEntry_Object=MibTableRow
cotvOverlayEntry=_CotvOverlayEntry_Object((1,3,6,1,4,1,9,9,810,1,2,1,1))
cotvOverlayEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:cotvOverlayEntry.setStatus(_A)
_CotvOverlayNumber_Type=Unsigned32
_CotvOverlayNumber_Object=MibTableColumn
cotvOverlayNumber=_CotvOverlayNumber_Object((1,3,6,1,4,1,9,9,810,1,2,1,1,1),_CotvOverlayNumber_Type())
cotvOverlayNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvOverlayNumber.setStatus(_A)
_CotvOverlayVpnName_Type=SnmpAdminString
_CotvOverlayVpnName_Object=MibTableColumn
cotvOverlayVpnName=_CotvOverlayVpnName_Object((1,3,6,1,4,1,9,9,810,1,2,1,1,2),_CotvOverlayVpnName_Type())
cotvOverlayVpnName.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvOverlayVpnName.setStatus(_A)
class _CotvOverlayVpnState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),(_Q,1),('up',2)))
_CotvOverlayVpnState_Type.__name__=_G
_CotvOverlayVpnState_Object=MibTableColumn
cotvOverlayVpnState=_CotvOverlayVpnState_Object((1,3,6,1,4,1,9,9,810,1,2,1,1,3),_CotvOverlayVpnState_Type())
cotvOverlayVpnState.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvOverlayVpnState.setStatus(_A)
class _CotvOverlayVpnDownReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19)));namedValues=NamedValues(*((_K,0),('configChange',1),('missingControlGroup',2),('missingDataGroupRange',3),('missingJoinOrSourceInterface',4),('missingVpnName',5),('missingJoinInterfaceAddr',6),('joinInterfaceDown',7),('adminDown',8),(_T,9),('reinit',10),('missingSiteId',11),(_U,12),('missingSourceInterfaceAddr',13),('sourceInterfaceDown',14),('changingSiteId',15),('changingControlGroup',16),('missingDeviceId',17),('changingDeviceId',18),('cleanupInProgress',19)))
_CotvOverlayVpnDownReason_Type.__name__=_G
_CotvOverlayVpnDownReason_Object=MibTableColumn
cotvOverlayVpnDownReason=_CotvOverlayVpnDownReason_Object((1,3,6,1,4,1,9,9,810,1,2,1,1,4),_CotvOverlayVpnDownReason_Type())
cotvOverlayVpnDownReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvOverlayVpnDownReason.setStatus(_A)
class _CotvOverlayVlansExtendedFirst2k_Type(Cisco2KVlanList):defaultValue=OctetString('')
_CotvOverlayVlansExtendedFirst2k_Type.__name__=_M
_CotvOverlayVlansExtendedFirst2k_Object=MibTableColumn
cotvOverlayVlansExtendedFirst2k=_CotvOverlayVlansExtendedFirst2k_Object((1,3,6,1,4,1,9,9,810,1,2,1,1,5),_CotvOverlayVlansExtendedFirst2k_Type())
cotvOverlayVlansExtendedFirst2k.setMaxAccess(_E)
if mibBuilder.loadTexts:cotvOverlayVlansExtendedFirst2k.setStatus(_A)
class _CotvOverlayVlansExtendedSecond2k_Type(Cisco2KVlanList):defaultValue=OctetString('')
_CotvOverlayVlansExtendedSecond2k_Type.__name__=_M
_CotvOverlayVlansExtendedSecond2k_Object=MibTableColumn
cotvOverlayVlansExtendedSecond2k=_CotvOverlayVlansExtendedSecond2k_Object((1,3,6,1,4,1,9,9,810,1,2,1,1,6),_CotvOverlayVlansExtendedSecond2k_Type())
cotvOverlayVlansExtendedSecond2k.setMaxAccess(_E)
if mibBuilder.loadTexts:cotvOverlayVlansExtendedSecond2k.setStatus(_A)
class _CotvOverlayControlGroupAddrType_Type(InetAddressType):defaultValue=0
_CotvOverlayControlGroupAddrType_Type.__name__=_J
_CotvOverlayControlGroupAddrType_Object=MibTableColumn
cotvOverlayControlGroupAddrType=_CotvOverlayControlGroupAddrType_Object((1,3,6,1,4,1,9,9,810,1,2,1,1,7),_CotvOverlayControlGroupAddrType_Type())
cotvOverlayControlGroupAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:cotvOverlayControlGroupAddrType.setStatus(_A)
class _CotvOverlayControlGroupAddr_Type(InetAddress):defaultValue=OctetString('')
_CotvOverlayControlGroupAddr_Type.__name__=_F
_CotvOverlayControlGroupAddr_Object=MibTableColumn
cotvOverlayControlGroupAddr=_CotvOverlayControlGroupAddr_Object((1,3,6,1,4,1,9,9,810,1,2,1,1,8),_CotvOverlayControlGroupAddr_Type())
cotvOverlayControlGroupAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:cotvOverlayControlGroupAddr.setStatus(_A)
class _CotvOverlayBroadcastGroupAddrType_Type(InetAddressType):defaultValue=0
_CotvOverlayBroadcastGroupAddrType_Type.__name__=_J
_CotvOverlayBroadcastGroupAddrType_Object=MibTableColumn
cotvOverlayBroadcastGroupAddrType=_CotvOverlayBroadcastGroupAddrType_Object((1,3,6,1,4,1,9,9,810,1,2,1,1,9),_CotvOverlayBroadcastGroupAddrType_Type())
cotvOverlayBroadcastGroupAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:cotvOverlayBroadcastGroupAddrType.setStatus(_A)
class _CotvOverlayBroadcastGroupAddr_Type(InetAddress):defaultValue=OctetString('')
_CotvOverlayBroadcastGroupAddr_Type.__name__=_F
_CotvOverlayBroadcastGroupAddr_Object=MibTableColumn
cotvOverlayBroadcastGroupAddr=_CotvOverlayBroadcastGroupAddr_Object((1,3,6,1,4,1,9,9,810,1,2,1,1,10),_CotvOverlayBroadcastGroupAddr_Type())
cotvOverlayBroadcastGroupAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:cotvOverlayBroadcastGroupAddr.setStatus(_A)
class _CotvOverlayJoinInterface_Type(InterfaceIndexOrZero):defaultValue=0
_CotvOverlayJoinInterface_Type.__name__=_N
_CotvOverlayJoinInterface_Object=MibTableColumn
cotvOverlayJoinInterface=_CotvOverlayJoinInterface_Object((1,3,6,1,4,1,9,9,810,1,2,1,1,11),_CotvOverlayJoinInterface_Type())
cotvOverlayJoinInterface.setMaxAccess(_E)
if mibBuilder.loadTexts:cotvOverlayJoinInterface.setStatus(_A)
class _CotvOverlaySourceInterface_Type(InterfaceIndexOrZero):defaultValue=0
_CotvOverlaySourceInterface_Type.__name__=_N
_CotvOverlaySourceInterface_Object=MibTableColumn
cotvOverlaySourceInterface=_CotvOverlaySourceInterface_Object((1,3,6,1,4,1,9,9,810,1,2,1,1,12),_CotvOverlaySourceInterface_Type())
cotvOverlaySourceInterface.setMaxAccess(_E)
if mibBuilder.loadTexts:cotvOverlaySourceInterface.setStatus(_A)
_CotvOverlayAedCapable_Type=TruthValue
_CotvOverlayAedCapable_Object=MibTableColumn
cotvOverlayAedCapable=_CotvOverlayAedCapable_Object((1,3,6,1,4,1,9,9,810,1,2,1,1,13),_CotvOverlayAedCapable_Type())
cotvOverlayAedCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvOverlayAedCapable.setStatus(_A)
class _CotvOverlayAedIncapableReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_K,0),(_V,1),('siteIdNotConfigured',2),(_U,3),('versionMismatch',4),('siteVlanDown',5),('noExtendedVlanUp',6),('noOverlayAdjacencyUp',7),('lspdbSyncIncomplete',8),('overlayDownInProgress',9),('isisControlGroupSyncPending',10)))
_CotvOverlayAedIncapableReason_Type.__name__=_G
_CotvOverlayAedIncapableReason_Object=MibTableColumn
cotvOverlayAedIncapableReason=_CotvOverlayAedIncapableReason_Object((1,3,6,1,4,1,9,9,810,1,2,1,1,14),_CotvOverlayAedIncapableReason_Type())
cotvOverlayAedIncapableReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvOverlayAedIncapableReason.setStatus(_A)
class _CotvOverlayAdjServerTransportType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('multicastAndUnicast',1),('unicastOnly',2)))
_CotvOverlayAdjServerTransportType_Type.__name__=_G
_CotvOverlayAdjServerTransportType_Object=MibTableColumn
cotvOverlayAdjServerTransportType=_CotvOverlayAdjServerTransportType_Object((1,3,6,1,4,1,9,9,810,1,2,1,1,15),_CotvOverlayAdjServerTransportType_Type())
cotvOverlayAdjServerTransportType.setMaxAccess(_E)
if mibBuilder.loadTexts:cotvOverlayAdjServerTransportType.setStatus(_A)
class _CotvOverlayAdjServerEnable_Type(TruthValue):defaultValue=2
_CotvOverlayAdjServerEnable_Type.__name__=_P
_CotvOverlayAdjServerEnable_Object=MibTableColumn
cotvOverlayAdjServerEnable=_CotvOverlayAdjServerEnable_Object((1,3,6,1,4,1,9,9,810,1,2,1,1,16),_CotvOverlayAdjServerEnable_Type())
cotvOverlayAdjServerEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cotvOverlayAdjServerEnable.setStatus(_A)
class _CotvOverlayPrimaryAdjServerAddrType_Type(InetAddressType):defaultValue=0
_CotvOverlayPrimaryAdjServerAddrType_Type.__name__=_J
_CotvOverlayPrimaryAdjServerAddrType_Object=MibTableColumn
cotvOverlayPrimaryAdjServerAddrType=_CotvOverlayPrimaryAdjServerAddrType_Object((1,3,6,1,4,1,9,9,810,1,2,1,1,17),_CotvOverlayPrimaryAdjServerAddrType_Type())
cotvOverlayPrimaryAdjServerAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:cotvOverlayPrimaryAdjServerAddrType.setStatus(_A)
class _CotvOverlayPrimaryAdjServerAddr_Type(InetAddress):defaultValue=OctetString('')
_CotvOverlayPrimaryAdjServerAddr_Type.__name__=_F
_CotvOverlayPrimaryAdjServerAddr_Object=MibTableColumn
cotvOverlayPrimaryAdjServerAddr=_CotvOverlayPrimaryAdjServerAddr_Object((1,3,6,1,4,1,9,9,810,1,2,1,1,18),_CotvOverlayPrimaryAdjServerAddr_Type())
cotvOverlayPrimaryAdjServerAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:cotvOverlayPrimaryAdjServerAddr.setStatus(_A)
class _CotvOverlaySecondaryAdjServerAddrType_Type(InetAddressType):defaultValue=0
_CotvOverlaySecondaryAdjServerAddrType_Type.__name__=_J
_CotvOverlaySecondaryAdjServerAddrType_Object=MibTableColumn
cotvOverlaySecondaryAdjServerAddrType=_CotvOverlaySecondaryAdjServerAddrType_Object((1,3,6,1,4,1,9,9,810,1,2,1,1,19),_CotvOverlaySecondaryAdjServerAddrType_Type())
cotvOverlaySecondaryAdjServerAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:cotvOverlaySecondaryAdjServerAddrType.setStatus(_A)
class _CotvOverlaySecondaryAdjServerAddr_Type(InetAddress):defaultValue=OctetString('')
_CotvOverlaySecondaryAdjServerAddr_Type.__name__=_F
_CotvOverlaySecondaryAdjServerAddr_Object=MibTableColumn
cotvOverlaySecondaryAdjServerAddr=_CotvOverlaySecondaryAdjServerAddr_Object((1,3,6,1,4,1,9,9,810,1,2,1,1,20),_CotvOverlaySecondaryAdjServerAddr_Type())
cotvOverlaySecondaryAdjServerAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:cotvOverlaySecondaryAdjServerAddr.setStatus(_A)
class _CotvOverlaySuppressArpND_Type(TruthValue):defaultValue=2
_CotvOverlaySuppressArpND_Type.__name__=_P
_CotvOverlaySuppressArpND_Object=MibTableColumn
cotvOverlaySuppressArpND=_CotvOverlaySuppressArpND_Object((1,3,6,1,4,1,9,9,810,1,2,1,1,21),_CotvOverlaySuppressArpND_Type())
cotvOverlaySuppressArpND.setMaxAccess(_E)
if mibBuilder.loadTexts:cotvOverlaySuppressArpND.setStatus(_A)
class _CotvOverlayStorageType_Type(StorageType):defaultValue=2
_CotvOverlayStorageType_Type.__name__=_O
_CotvOverlayStorageType_Object=MibTableColumn
cotvOverlayStorageType=_CotvOverlayStorageType_Object((1,3,6,1,4,1,9,9,810,1,2,1,1,22),_CotvOverlayStorageType_Type())
cotvOverlayStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:cotvOverlayStorageType.setStatus(_A)
_CotvOverlayRowStatus_Type=RowStatus
_CotvOverlayRowStatus_Object=MibTableColumn
cotvOverlayRowStatus=_CotvOverlayRowStatus_Object((1,3,6,1,4,1,9,9,810,1,2,1,1,23),_CotvOverlayRowStatus_Type())
cotvOverlayRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cotvOverlayRowStatus.setStatus(_A)
_CotvVlansTable_Object=MibTable
cotvVlansTable=_CotvVlansTable_Object((1,3,6,1,4,1,9,9,810,1,2,2))
if mibBuilder.loadTexts:cotvVlansTable.setStatus(_A)
_CotvVlansEntry_Object=MibTableRow
cotvVlansEntry=_CotvVlansEntry_Object((1,3,6,1,4,1,9,9,810,1,2,2,1))
cotvVlansEntry.setIndexNames((0,_B,_H),(0,_B,_R))
if mibBuilder.loadTexts:cotvVlansEntry.setStatus(_A)
_CotvVlanId_Type=VlanIndex
_CotvVlanId_Object=MibTableColumn
cotvVlanId=_CotvVlanId_Object((1,3,6,1,4,1,9,9,810,1,2,2,1,1),_CotvVlanId_Type())
cotvVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvVlanId.setStatus(_A)
class _CotvVlanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_CotvVlanState_Type.__name__=_G
_CotvVlanState_Object=MibTableColumn
cotvVlanState=_CotvVlanState_Object((1,3,6,1,4,1,9,9,810,1,2,2,1,2),_CotvVlanState_Type())
cotvVlanState.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvVlanState.setStatus(_A)
class _CotvVlanInactiveReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_K,1),('nonAed',2),('vlanDisabled',3),(_V,4),(_T,5),('hwDown',6)))
_CotvVlanInactiveReason_Type.__name__=_G
_CotvVlanInactiveReason_Object=MibTableColumn
cotvVlanInactiveReason=_CotvVlanInactiveReason_Object((1,3,6,1,4,1,9,9,810,1,2,2,1,3),_CotvVlanInactiveReason_Type())
cotvVlanInactiveReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvVlanInactiveReason.setStatus(_A)
_CotvVlanAedAddrType_Type=InetAddressType
_CotvVlanAedAddrType_Object=MibTableColumn
cotvVlanAedAddrType=_CotvVlanAedAddrType_Object((1,3,6,1,4,1,9,9,810,1,2,2,1,4),_CotvVlanAedAddrType_Type())
cotvVlanAedAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvVlanAedAddrType.setStatus(_A)
_CotvVlanAedAddr_Type=InetAddress
_CotvVlanAedAddr_Object=MibTableColumn
cotvVlanAedAddr=_CotvVlanAedAddr_Object((1,3,6,1,4,1,9,9,810,1,2,2,1,5),_CotvVlanAedAddr_Type())
cotvVlanAedAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvVlanAedAddr.setStatus(_A)
_CotvVlanEdgeDevIsAed_Type=TruthValue
_CotvVlanEdgeDevIsAed_Object=MibTableColumn
cotvVlanEdgeDevIsAed=_CotvVlanEdgeDevIsAed_Object((1,3,6,1,4,1,9,9,810,1,2,2,1,6),_CotvVlanEdgeDevIsAed_Type())
cotvVlanEdgeDevIsAed.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvVlanEdgeDevIsAed.setStatus(_A)
_CotvDataGroupConfigTable_Object=MibTable
cotvDataGroupConfigTable=_CotvDataGroupConfigTable_Object((1,3,6,1,4,1,9,9,810,1,2,3))
if mibBuilder.loadTexts:cotvDataGroupConfigTable.setStatus(_A)
_CotvDataGroupConfigEntry_Object=MibTableRow
cotvDataGroupConfigEntry=_CotvDataGroupConfigEntry_Object((1,3,6,1,4,1,9,9,810,1,2,3,1))
cotvDataGroupConfigEntry.setIndexNames((0,_B,_H),(0,_B,_W),(0,_B,_X),(0,_B,_Y))
if mibBuilder.loadTexts:cotvDataGroupConfigEntry.setStatus(_A)
_CotvDataGroupMcastRangeAddrType_Type=InetAddressType
_CotvDataGroupMcastRangeAddrType_Object=MibTableColumn
cotvDataGroupMcastRangeAddrType=_CotvDataGroupMcastRangeAddrType_Object((1,3,6,1,4,1,9,9,810,1,2,3,1,1),_CotvDataGroupMcastRangeAddrType_Type())
cotvDataGroupMcastRangeAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvDataGroupMcastRangeAddrType.setStatus(_A)
class _CotvDataGroupMcastRangeAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_CotvDataGroupMcastRangeAddr_Type.__name__=_F
_CotvDataGroupMcastRangeAddr_Object=MibTableColumn
cotvDataGroupMcastRangeAddr=_CotvDataGroupMcastRangeAddr_Object((1,3,6,1,4,1,9,9,810,1,2,3,1,2),_CotvDataGroupMcastRangeAddr_Type())
cotvDataGroupMcastRangeAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvDataGroupMcastRangeAddr.setStatus(_A)
_CotvDataGroupMcastRangePrefixLength_Type=InetAddressPrefixLength
_CotvDataGroupMcastRangePrefixLength_Object=MibTableColumn
cotvDataGroupMcastRangePrefixLength=_CotvDataGroupMcastRangePrefixLength_Object((1,3,6,1,4,1,9,9,810,1,2,3,1,3),_CotvDataGroupMcastRangePrefixLength_Type())
cotvDataGroupMcastRangePrefixLength.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvDataGroupMcastRangePrefixLength.setStatus(_A)
class _CotvDataGroupStorageType_Type(StorageType):defaultValue=2
_CotvDataGroupStorageType_Type.__name__=_O
_CotvDataGroupStorageType_Object=MibTableColumn
cotvDataGroupStorageType=_CotvDataGroupStorageType_Object((1,3,6,1,4,1,9,9,810,1,2,3,1,4),_CotvDataGroupStorageType_Type())
cotvDataGroupStorageType.setMaxAccess(_E)
if mibBuilder.loadTexts:cotvDataGroupStorageType.setStatus(_A)
_CotvDataGroupRowStatus_Type=RowStatus
_CotvDataGroupRowStatus_Object=MibTableColumn
cotvDataGroupRowStatus=_CotvDataGroupRowStatus_Object((1,3,6,1,4,1,9,9,810,1,2,3,1,5),_CotvDataGroupRowStatus_Type())
cotvDataGroupRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cotvDataGroupRowStatus.setStatus(_A)
_CotvDataGroupInfoTable_Object=MibTable
cotvDataGroupInfoTable=_CotvDataGroupInfoTable_Object((1,3,6,1,4,1,9,9,810,1,2,4))
if mibBuilder.loadTexts:cotvDataGroupInfoTable.setStatus(_A)
_CotvDataGroupInfoEntry_Object=MibTableRow
cotvDataGroupInfoEntry=_CotvDataGroupInfoEntry_Object((1,3,6,1,4,1,9,9,810,1,2,4,1))
cotvDataGroupInfoEntry.setIndexNames((0,_B,_H),(0,_B,_Z),(0,_B,_a),(0,_B,_b),(0,_B,_c),(0,_B,_d),(0,_B,_e),(0,_B,_f),(0,_B,_g),(0,_B,_h),(0,_B,_i))
if mibBuilder.loadTexts:cotvDataGroupInfoEntry.setStatus(_A)
class _CotvDataGroupActiveSrcLocation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),(_j,2)))
_CotvDataGroupActiveSrcLocation_Type.__name__=_G
_CotvDataGroupActiveSrcLocation_Object=MibTableColumn
cotvDataGroupActiveSrcLocation=_CotvDataGroupActiveSrcLocation_Object((1,3,6,1,4,1,9,9,810,1,2,4,1,1),_CotvDataGroupActiveSrcLocation_Type())
cotvDataGroupActiveSrcLocation.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvDataGroupActiveSrcLocation.setStatus(_A)
_CotvDataGroupVlanId_Type=VlanIndex
_CotvDataGroupVlanId_Object=MibTableColumn
cotvDataGroupVlanId=_CotvDataGroupVlanId_Object((1,3,6,1,4,1,9,9,810,1,2,4,1,2),_CotvDataGroupVlanId_Type())
cotvDataGroupVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvDataGroupVlanId.setStatus(_A)
_CotvDataGroupActiveGroupAddrType_Type=InetAddressType
_CotvDataGroupActiveGroupAddrType_Object=MibTableColumn
cotvDataGroupActiveGroupAddrType=_CotvDataGroupActiveGroupAddrType_Object((1,3,6,1,4,1,9,9,810,1,2,4,1,3),_CotvDataGroupActiveGroupAddrType_Type())
cotvDataGroupActiveGroupAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvDataGroupActiveGroupAddrType.setStatus(_A)
class _CotvDataGroupActiveGroupAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_CotvDataGroupActiveGroupAddr_Type.__name__=_F
_CotvDataGroupActiveGroupAddr_Object=MibTableColumn
cotvDataGroupActiveGroupAddr=_CotvDataGroupActiveGroupAddr_Object((1,3,6,1,4,1,9,9,810,1,2,4,1,4),_CotvDataGroupActiveGroupAddr_Type())
cotvDataGroupActiveGroupAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvDataGroupActiveGroupAddr.setStatus(_A)
_CotvDataGroupActiveSrcAddrType_Type=InetAddressType
_CotvDataGroupActiveSrcAddrType_Object=MibTableColumn
cotvDataGroupActiveSrcAddrType=_CotvDataGroupActiveSrcAddrType_Object((1,3,6,1,4,1,9,9,810,1,2,4,1,5),_CotvDataGroupActiveSrcAddrType_Type())
cotvDataGroupActiveSrcAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvDataGroupActiveSrcAddrType.setStatus(_A)
class _CotvDataGroupActiveSrcAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_CotvDataGroupActiveSrcAddr_Type.__name__=_F
_CotvDataGroupActiveSrcAddr_Object=MibTableColumn
cotvDataGroupActiveSrcAddr=_CotvDataGroupActiveSrcAddr_Object((1,3,6,1,4,1,9,9,810,1,2,4,1,6),_CotvDataGroupActiveSrcAddr_Type())
cotvDataGroupActiveSrcAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvDataGroupActiveSrcAddr.setStatus(_A)
_CotvDataGroupDeliveryGroupAddrType_Type=InetAddressType
_CotvDataGroupDeliveryGroupAddrType_Object=MibTableColumn
cotvDataGroupDeliveryGroupAddrType=_CotvDataGroupDeliveryGroupAddrType_Object((1,3,6,1,4,1,9,9,810,1,2,4,1,7),_CotvDataGroupDeliveryGroupAddrType_Type())
cotvDataGroupDeliveryGroupAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvDataGroupDeliveryGroupAddrType.setStatus(_A)
class _CotvDataGroupDeliveryGroupAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_CotvDataGroupDeliveryGroupAddr_Type.__name__=_F
_CotvDataGroupDeliveryGroupAddr_Object=MibTableColumn
cotvDataGroupDeliveryGroupAddr=_CotvDataGroupDeliveryGroupAddr_Object((1,3,6,1,4,1,9,9,810,1,2,4,1,8),_CotvDataGroupDeliveryGroupAddr_Type())
cotvDataGroupDeliveryGroupAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvDataGroupDeliveryGroupAddr.setStatus(_A)
_CotvDataGroupDeliverySrcAddrType_Type=InetAddressType
_CotvDataGroupDeliverySrcAddrType_Object=MibTableColumn
cotvDataGroupDeliverySrcAddrType=_CotvDataGroupDeliverySrcAddrType_Object((1,3,6,1,4,1,9,9,810,1,2,4,1,9),_CotvDataGroupDeliverySrcAddrType_Type())
cotvDataGroupDeliverySrcAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvDataGroupDeliverySrcAddrType.setStatus(_A)
class _CotvDataGroupDeliverySrcAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_CotvDataGroupDeliverySrcAddr_Type.__name__=_F
_CotvDataGroupDeliverySrcAddr_Object=MibTableColumn
cotvDataGroupDeliverySrcAddr=_CotvDataGroupDeliverySrcAddr_Object((1,3,6,1,4,1,9,9,810,1,2,4,1,10),_CotvDataGroupDeliverySrcAddr_Type())
cotvDataGroupDeliverySrcAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvDataGroupDeliverySrcAddr.setStatus(_A)
_CotvDataGroupJoinInterface_Type=InterfaceIndexOrZero
_CotvDataGroupJoinInterface_Object=MibTableColumn
cotvDataGroupJoinInterface=_CotvDataGroupJoinInterface_Object((1,3,6,1,4,1,9,9,810,1,2,4,1,11),_CotvDataGroupJoinInterface_Type())
cotvDataGroupJoinInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvDataGroupJoinInterface.setStatus(_A)
class _CotvDataGroupLocalActiveSrcState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('local',2),(_j,3),('orphan',4)))
_CotvDataGroupLocalActiveSrcState_Type.__name__=_G
_CotvDataGroupLocalActiveSrcState_Object=MibTableColumn
cotvDataGroupLocalActiveSrcState=_CotvDataGroupLocalActiveSrcState_Object((1,3,6,1,4,1,9,9,810,1,2,4,1,12),_CotvDataGroupLocalActiveSrcState_Type())
cotvDataGroupLocalActiveSrcState.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvDataGroupLocalActiveSrcState.setStatus(_A)
_CotvAdjacencyObjects_ObjectIdentity=ObjectIdentity
cotvAdjacencyObjects=_CotvAdjacencyObjects_ObjectIdentity((1,3,6,1,4,1,9,9,810,1,3))
_CotvAdjacencyDatabaseTable_Object=MibTable
cotvAdjacencyDatabaseTable=_CotvAdjacencyDatabaseTable_Object((1,3,6,1,4,1,9,9,810,1,3,1))
if mibBuilder.loadTexts:cotvAdjacencyDatabaseTable.setStatus(_A)
_CotvAdjacencyDatabaseEntry_Object=MibTableRow
cotvAdjacencyDatabaseEntry=_CotvAdjacencyDatabaseEntry_Object((1,3,6,1,4,1,9,9,810,1,3,1,1))
cotvAdjacencyDatabaseEntry.setIndexNames((0,_B,_H),(0,_B,_k),(0,_B,_l))
if mibBuilder.loadTexts:cotvAdjacencyDatabaseEntry.setStatus(_A)
_CotvAdjacentDevAddrType_Type=InetAddressType
_CotvAdjacentDevAddrType_Object=MibTableColumn
cotvAdjacentDevAddrType=_CotvAdjacentDevAddrType_Object((1,3,6,1,4,1,9,9,810,1,3,1,1,1),_CotvAdjacentDevAddrType_Type())
cotvAdjacentDevAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvAdjacentDevAddrType.setStatus(_A)
class _CotvAdjacentDevAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CotvAdjacentDevAddr_Type.__name__=_F
_CotvAdjacentDevAddr_Object=MibTableColumn
cotvAdjacentDevAddr=_CotvAdjacentDevAddr_Object((1,3,6,1,4,1,9,9,810,1,3,1,1,2),_CotvAdjacentDevAddr_Type())
cotvAdjacentDevAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvAdjacentDevAddr.setStatus(_A)
class _CotvAdjacentDevSystemID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(6,6))
_CotvAdjacentDevSystemID_Type.__name__=_L
_CotvAdjacentDevSystemID_Object=MibTableColumn
cotvAdjacentDevSystemID=_CotvAdjacentDevSystemID_Object((1,3,6,1,4,1,9,9,810,1,3,1,1,3),_CotvAdjacentDevSystemID_Type())
cotvAdjacentDevSystemID.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvAdjacentDevSystemID.setStatus(_A)
_CotvAdjacentDevName_Type=SnmpAdminString
_CotvAdjacentDevName_Object=MibTableColumn
cotvAdjacentDevName=_CotvAdjacentDevName_Object((1,3,6,1,4,1,9,9,810,1,3,1,1,4),_CotvAdjacentDevName_Type())
cotvAdjacentDevName.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvAdjacentDevName.setStatus(_A)
class _CotvAdjacentDevState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_K,0),('up',1),(_Q,2)))
_CotvAdjacentDevState_Type.__name__=_G
_CotvAdjacentDevState_Object=MibTableColumn
cotvAdjacentDevState=_CotvAdjacentDevState_Object((1,3,6,1,4,1,9,9,810,1,3,1,1,5),_CotvAdjacentDevState_Type())
cotvAdjacentDevState.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvAdjacentDevState.setStatus(_A)
_CotvAdjacentDevUpTime_Type=Unsigned32
_CotvAdjacentDevUpTime_Object=MibTableColumn
cotvAdjacentDevUpTime=_CotvAdjacentDevUpTime_Object((1,3,6,1,4,1,9,9,810,1,3,1,1,6),_CotvAdjacentDevUpTime_Type())
cotvAdjacentDevUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvAdjacentDevUpTime.setStatus(_A)
if mibBuilder.loadTexts:cotvAdjacentDevUpTime.setUnits(_I)
_CotvArpNdObjects_ObjectIdentity=ObjectIdentity
cotvArpNdObjects=_CotvArpNdObjects_ObjectIdentity((1,3,6,1,4,1,9,9,810,1,4))
_CotvArpNdCacheTable_Object=MibTable
cotvArpNdCacheTable=_CotvArpNdCacheTable_Object((1,3,6,1,4,1,9,9,810,1,4,1))
if mibBuilder.loadTexts:cotvArpNdCacheTable.setStatus(_A)
_CotvArpNdCacheEntry_Object=MibTableRow
cotvArpNdCacheEntry=_CotvArpNdCacheEntry_Object((1,3,6,1,4,1,9,9,810,1,4,1,1))
cotvArpNdCacheEntry.setIndexNames((0,_B,_H),(0,_B,_R),(0,_B,_m),(0,_B,_n))
if mibBuilder.loadTexts:cotvArpNdCacheEntry.setStatus(_A)
_CotvArpNdCacheL3AddrType_Type=InetAddressType
_CotvArpNdCacheL3AddrType_Object=MibTableColumn
cotvArpNdCacheL3AddrType=_CotvArpNdCacheL3AddrType_Object((1,3,6,1,4,1,9,9,810,1,4,1,1,1),_CotvArpNdCacheL3AddrType_Type())
cotvArpNdCacheL3AddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvArpNdCacheL3AddrType.setStatus(_A)
class _CotvArpNdCacheL3Addr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CotvArpNdCacheL3Addr_Type.__name__=_F
_CotvArpNdCacheL3Addr_Object=MibTableColumn
cotvArpNdCacheL3Addr=_CotvArpNdCacheL3Addr_Object((1,3,6,1,4,1,9,9,810,1,4,1,1,2),_CotvArpNdCacheL3Addr_Type())
cotvArpNdCacheL3Addr.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvArpNdCacheL3Addr.setStatus(_A)
_CotvArpNdCacheMacAddr_Type=MacAddress
_CotvArpNdCacheMacAddr_Object=MibTableColumn
cotvArpNdCacheMacAddr=_CotvArpNdCacheMacAddr_Object((1,3,6,1,4,1,9,9,810,1,4,1,1,3),_CotvArpNdCacheMacAddr_Type())
cotvArpNdCacheMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvArpNdCacheMacAddr.setStatus(_A)
_CotvArpNdCacheAge_Type=Unsigned32
_CotvArpNdCacheAge_Object=MibTableColumn
cotvArpNdCacheAge=_CotvArpNdCacheAge_Object((1,3,6,1,4,1,9,9,810,1,4,1,1,4),_CotvArpNdCacheAge_Type())
cotvArpNdCacheAge.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvArpNdCacheAge.setStatus(_A)
if mibBuilder.loadTexts:cotvArpNdCacheAge.setUnits(_I)
_CotvArpNdCacheTimeToExpire_Type=Unsigned32
_CotvArpNdCacheTimeToExpire_Object=MibTableColumn
cotvArpNdCacheTimeToExpire=_CotvArpNdCacheTimeToExpire_Object((1,3,6,1,4,1,9,9,810,1,4,1,1,5),_CotvArpNdCacheTimeToExpire_Type())
cotvArpNdCacheTimeToExpire.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvArpNdCacheTimeToExpire.setStatus(_A)
if mibBuilder.loadTexts:cotvArpNdCacheTimeToExpire.setUnits(_I)
_CotvRouteObjects_ObjectIdentity=ObjectIdentity
cotvRouteObjects=_CotvRouteObjects_ObjectIdentity((1,3,6,1,4,1,9,9,810,1,5))
_CotvRouteTable_Object=MibTable
cotvRouteTable=_CotvRouteTable_Object((1,3,6,1,4,1,9,9,810,1,5,1))
if mibBuilder.loadTexts:cotvRouteTable.setStatus(_A)
_CotvRouteEntry_Object=MibTableRow
cotvRouteEntry=_CotvRouteEntry_Object((1,3,6,1,4,1,9,9,810,1,5,1,1))
cotvRouteEntry.setIndexNames((0,_B,_o),(0,_B,_p))
if mibBuilder.loadTexts:cotvRouteEntry.setStatus(_A)
_CotvRouteVlanId_Type=VlanIndex
_CotvRouteVlanId_Object=MibTableColumn
cotvRouteVlanId=_CotvRouteVlanId_Object((1,3,6,1,4,1,9,9,810,1,5,1,1,1),_CotvRouteVlanId_Type())
cotvRouteVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvRouteVlanId.setStatus(_A)
_CotvRouteMacAddr_Type=MacAddress
_CotvRouteMacAddr_Object=MibTableColumn
cotvRouteMacAddr=_CotvRouteMacAddr_Object((1,3,6,1,4,1,9,9,810,1,5,1,1,2),_CotvRouteMacAddr_Type())
cotvRouteMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvRouteMacAddr.setStatus(_A)
_CotvRouteMetric_Type=Unsigned32
_CotvRouteMetric_Object=MibTableColumn
cotvRouteMetric=_CotvRouteMetric_Object((1,3,6,1,4,1,9,9,810,1,5,1,1,3),_CotvRouteMetric_Type())
cotvRouteMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvRouteMetric.setStatus(_A)
_CotvRouteUpTime_Type=Unsigned32
_CotvRouteUpTime_Object=MibTableColumn
cotvRouteUpTime=_CotvRouteUpTime_Object((1,3,6,1,4,1,9,9,810,1,5,1,1,4),_CotvRouteUpTime_Type())
cotvRouteUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvRouteUpTime.setStatus(_A)
if mibBuilder.loadTexts:cotvRouteUpTime.setUnits(_I)
_CotvRouteOwner_Type=SnmpAdminString
_CotvRouteOwner_Object=MibTableColumn
cotvRouteOwner=_CotvRouteOwner_Object((1,3,6,1,4,1,9,9,810,1,5,1,1,5),_CotvRouteOwner_Type())
cotvRouteOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvRouteOwner.setStatus(_A)
_CotvRouteNextHopIf_Type=InterfaceIndexOrZero
_CotvRouteNextHopIf_Object=MibTableColumn
cotvRouteNextHopIf=_CotvRouteNextHopIf_Object((1,3,6,1,4,1,9,9,810,1,5,1,1,6),_CotvRouteNextHopIf_Type())
cotvRouteNextHopIf.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvRouteNextHopIf.setStatus(_A)
_CotvRouteNextHopAddrType_Type=InetAddressType
_CotvRouteNextHopAddrType_Object=MibTableColumn
cotvRouteNextHopAddrType=_CotvRouteNextHopAddrType_Object((1,3,6,1,4,1,9,9,810,1,5,1,1,7),_CotvRouteNextHopAddrType_Type())
cotvRouteNextHopAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvRouteNextHopAddrType.setStatus(_A)
_CotvRouteNextHopAddr_Type=InetAddress
_CotvRouteNextHopAddr_Object=MibTableColumn
cotvRouteNextHopAddr=_CotvRouteNextHopAddr_Object((1,3,6,1,4,1,9,9,810,1,5,1,1,8),_CotvRouteNextHopAddr_Type())
cotvRouteNextHopAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvRouteNextHopAddr.setStatus(_A)
_CotvMcastRouteTable_Object=MibTable
cotvMcastRouteTable=_CotvMcastRouteTable_Object((1,3,6,1,4,1,9,9,810,1,5,2))
if mibBuilder.loadTexts:cotvMcastRouteTable.setStatus(_A)
_CotvMcastRouteEntry_Object=MibTableRow
cotvMcastRouteEntry=_CotvMcastRouteEntry_Object((1,3,6,1,4,1,9,9,810,1,5,2,1))
cotvMcastRouteEntry.setIndexNames((0,_B,_q),(0,_B,_r),(0,_B,_s),(0,_B,_t),(0,_B,_u))
if mibBuilder.loadTexts:cotvMcastRouteEntry.setStatus(_A)
_CotvMcastRouteVlanId_Type=VlanIndex
_CotvMcastRouteVlanId_Object=MibTableColumn
cotvMcastRouteVlanId=_CotvMcastRouteVlanId_Object((1,3,6,1,4,1,9,9,810,1,5,2,1,1),_CotvMcastRouteVlanId_Type())
cotvMcastRouteVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvMcastRouteVlanId.setStatus(_A)
_CotvMcastRouteActiveSrcAddrType_Type=InetAddressType
_CotvMcastRouteActiveSrcAddrType_Object=MibTableColumn
cotvMcastRouteActiveSrcAddrType=_CotvMcastRouteActiveSrcAddrType_Object((1,3,6,1,4,1,9,9,810,1,5,2,1,2),_CotvMcastRouteActiveSrcAddrType_Type())
cotvMcastRouteActiveSrcAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvMcastRouteActiveSrcAddrType.setStatus(_A)
class _CotvMcastRouteActiveSrcAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_CotvMcastRouteActiveSrcAddr_Type.__name__=_F
_CotvMcastRouteActiveSrcAddr_Object=MibTableColumn
cotvMcastRouteActiveSrcAddr=_CotvMcastRouteActiveSrcAddr_Object((1,3,6,1,4,1,9,9,810,1,5,2,1,3),_CotvMcastRouteActiveSrcAddr_Type())
cotvMcastRouteActiveSrcAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvMcastRouteActiveSrcAddr.setStatus(_A)
_CotvMcastRouteActiveGroupAddrType_Type=InetAddressType
_CotvMcastRouteActiveGroupAddrType_Object=MibTableColumn
cotvMcastRouteActiveGroupAddrType=_CotvMcastRouteActiveGroupAddrType_Object((1,3,6,1,4,1,9,9,810,1,5,2,1,4),_CotvMcastRouteActiveGroupAddrType_Type())
cotvMcastRouteActiveGroupAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvMcastRouteActiveGroupAddrType.setStatus(_A)
class _CotvMcastRouteActiveGroupAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_CotvMcastRouteActiveGroupAddr_Type.__name__=_F
_CotvMcastRouteActiveGroupAddr_Object=MibTableColumn
cotvMcastRouteActiveGroupAddr=_CotvMcastRouteActiveGroupAddr_Object((1,3,6,1,4,1,9,9,810,1,5,2,1,5),_CotvMcastRouteActiveGroupAddr_Type())
cotvMcastRouteActiveGroupAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvMcastRouteActiveGroupAddr.setStatus(_A)
_CotvMcastRouteOwners_Type=SnmpAdminString
_CotvMcastRouteOwners_Object=MibTableColumn
cotvMcastRouteOwners=_CotvMcastRouteOwners_Object((1,3,6,1,4,1,9,9,810,1,5,2,1,6),_CotvMcastRouteOwners_Type())
cotvMcastRouteOwners.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvMcastRouteOwners.setStatus(_A)
_CotvMcastRouteMetric_Type=Unsigned32
_CotvMcastRouteMetric_Object=MibTableColumn
cotvMcastRouteMetric=_CotvMcastRouteMetric_Object((1,3,6,1,4,1,9,9,810,1,5,2,1,7),_CotvMcastRouteMetric_Type())
cotvMcastRouteMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvMcastRouteMetric.setStatus(_A)
_CotvMcastRouteUpTime_Type=Unsigned32
_CotvMcastRouteUpTime_Object=MibTableColumn
cotvMcastRouteUpTime=_CotvMcastRouteUpTime_Object((1,3,6,1,4,1,9,9,810,1,5,2,1,8),_CotvMcastRouteUpTime_Type())
cotvMcastRouteUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvMcastRouteUpTime.setStatus(_A)
if mibBuilder.loadTexts:cotvMcastRouteUpTime.setUnits(_I)
_CotvMcastRouteInfoTable_Object=MibTable
cotvMcastRouteInfoTable=_CotvMcastRouteInfoTable_Object((1,3,6,1,4,1,9,9,810,1,5,3))
if mibBuilder.loadTexts:cotvMcastRouteInfoTable.setStatus(_A)
_CotvMcastRouteInfoEntry_Object=MibTableRow
cotvMcastRouteInfoEntry=_CotvMcastRouteInfoEntry_Object((1,3,6,1,4,1,9,9,810,1,5,3,1))
cotvMcastRouteInfoEntry.setIndexNames((0,_B,_v),(0,_B,_w),(0,_B,_x),(0,_B,_y),(0,_B,_z),(0,_B,_A0))
if mibBuilder.loadTexts:cotvMcastRouteInfoEntry.setStatus(_A)
_CotvMcastRouteInfoVlanId_Type=VlanIndex
_CotvMcastRouteInfoVlanId_Object=MibTableColumn
cotvMcastRouteInfoVlanId=_CotvMcastRouteInfoVlanId_Object((1,3,6,1,4,1,9,9,810,1,5,3,1,1),_CotvMcastRouteInfoVlanId_Type())
cotvMcastRouteInfoVlanId.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvMcastRouteInfoVlanId.setStatus(_A)
_CotvMcastRouteInfoActiveSrcAddrType_Type=InetAddressType
_CotvMcastRouteInfoActiveSrcAddrType_Object=MibTableColumn
cotvMcastRouteInfoActiveSrcAddrType=_CotvMcastRouteInfoActiveSrcAddrType_Object((1,3,6,1,4,1,9,9,810,1,5,3,1,2),_CotvMcastRouteInfoActiveSrcAddrType_Type())
cotvMcastRouteInfoActiveSrcAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvMcastRouteInfoActiveSrcAddrType.setStatus(_A)
class _CotvMcastRouteInfoActiveSrcAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_CotvMcastRouteInfoActiveSrcAddr_Type.__name__=_F
_CotvMcastRouteInfoActiveSrcAddr_Object=MibTableColumn
cotvMcastRouteInfoActiveSrcAddr=_CotvMcastRouteInfoActiveSrcAddr_Object((1,3,6,1,4,1,9,9,810,1,5,3,1,3),_CotvMcastRouteInfoActiveSrcAddr_Type())
cotvMcastRouteInfoActiveSrcAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvMcastRouteInfoActiveSrcAddr.setStatus(_A)
_CotvMcastRouteInfoActiveGroupAddrType_Type=InetAddressType
_CotvMcastRouteInfoActiveGroupAddrType_Object=MibTableColumn
cotvMcastRouteInfoActiveGroupAddrType=_CotvMcastRouteInfoActiveGroupAddrType_Object((1,3,6,1,4,1,9,9,810,1,5,3,1,4),_CotvMcastRouteInfoActiveGroupAddrType_Type())
cotvMcastRouteInfoActiveGroupAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvMcastRouteInfoActiveGroupAddrType.setStatus(_A)
class _CotvMcastRouteInfoActiveGroupAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_CotvMcastRouteInfoActiveGroupAddr_Type.__name__=_F
_CotvMcastRouteInfoActiveGroupAddr_Object=MibTableColumn
cotvMcastRouteInfoActiveGroupAddr=_CotvMcastRouteInfoActiveGroupAddr_Object((1,3,6,1,4,1,9,9,810,1,5,3,1,5),_CotvMcastRouteInfoActiveGroupAddr_Type())
cotvMcastRouteInfoActiveGroupAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvMcastRouteInfoActiveGroupAddr.setStatus(_A)
_CotvMcastRouteInfoIf_Type=InterfaceIndexOrZero
_CotvMcastRouteInfoIf_Object=MibTableColumn
cotvMcastRouteInfoIf=_CotvMcastRouteInfoIf_Object((1,3,6,1,4,1,9,9,810,1,5,3,1,6),_CotvMcastRouteInfoIf_Type())
cotvMcastRouteInfoIf.setMaxAccess(_D)
if mibBuilder.loadTexts:cotvMcastRouteInfoIf.setStatus(_A)
_CotvMcastRouteInfoHostAddrType_Type=InetAddressType
_CotvMcastRouteInfoHostAddrType_Object=MibTableColumn
cotvMcastRouteInfoHostAddrType=_CotvMcastRouteInfoHostAddrType_Object((1,3,6,1,4,1,9,9,810,1,5,3,1,7),_CotvMcastRouteInfoHostAddrType_Type())
cotvMcastRouteInfoHostAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvMcastRouteInfoHostAddrType.setStatus(_A)
_CotvMcastRouteInfoHostAddr_Type=InetAddress
_CotvMcastRouteInfoHostAddr_Object=MibTableColumn
cotvMcastRouteInfoHostAddr=_CotvMcastRouteInfoHostAddr_Object((1,3,6,1,4,1,9,9,810,1,5,3,1,8),_CotvMcastRouteInfoHostAddr_Type())
cotvMcastRouteInfoHostAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvMcastRouteInfoHostAddr.setStatus(_A)
_CotvMcastRouteInfoProtocolOwners_Type=SnmpAdminString
_CotvMcastRouteInfoProtocolOwners_Object=MibTableColumn
cotvMcastRouteInfoProtocolOwners=_CotvMcastRouteInfoProtocolOwners_Object((1,3,6,1,4,1,9,9,810,1,5,3,1,9),_CotvMcastRouteInfoProtocolOwners_Type())
cotvMcastRouteInfoProtocolOwners.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvMcastRouteInfoProtocolOwners.setStatus(_A)
_CotvMcastRouteInfoMetric_Type=Unsigned32
_CotvMcastRouteInfoMetric_Object=MibTableColumn
cotvMcastRouteInfoMetric=_CotvMcastRouteInfoMetric_Object((1,3,6,1,4,1,9,9,810,1,5,3,1,10),_CotvMcastRouteInfoMetric_Type())
cotvMcastRouteInfoMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvMcastRouteInfoMetric.setStatus(_A)
_CotvMcastRouteInfoUpTime_Type=Unsigned32
_CotvMcastRouteInfoUpTime_Object=MibTableColumn
cotvMcastRouteInfoUpTime=_CotvMcastRouteInfoUpTime_Object((1,3,6,1,4,1,9,9,810,1,5,3,1,11),_CotvMcastRouteInfoUpTime_Type())
cotvMcastRouteInfoUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cotvMcastRouteInfoUpTime.setStatus(_A)
if mibBuilder.loadTexts:cotvMcastRouteInfoUpTime.setUnits(_I)
_CiscoOtvMIBConform_ObjectIdentity=ObjectIdentity
ciscoOtvMIBConform=_CiscoOtvMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,810,2))
_CiscoOtvMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoOtvMIBCompliances=_CiscoOtvMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,810,2,1))
_CiscoOtvMIBGroups_ObjectIdentity=ObjectIdentity
ciscoOtvMIBGroups=_CiscoOtvMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,810,2,2))
ciscoOtvSiteGroup=ObjectGroup((1,3,6,1,4,1,9,9,810,2,2,1))
ciscoOtvSiteGroup.setObjects(*((_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:ciscoOtvSiteGroup.setStatus(_A)
ciscoOtvOverlayGroup=ObjectGroup((1,3,6,1,4,1,9,9,810,2,2,2))
ciscoOtvOverlayGroup.setObjects(*((_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ)))
if mibBuilder.loadTexts:ciscoOtvOverlayGroup.setStatus(_A)
ciscoOtvVlanGroup=ObjectGroup((1,3,6,1,4,1,9,9,810,2,2,3))
ciscoOtvVlanGroup.setObjects(*((_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV)))
if mibBuilder.loadTexts:ciscoOtvVlanGroup.setStatus(_A)
ciscoOtvDataGroupConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,810,2,2,4))
ciscoOtvDataGroupConfigGroup.setObjects(*((_B,_AW),(_B,_AX)))
if mibBuilder.loadTexts:ciscoOtvDataGroupConfigGroup.setStatus(_A)
ciscoOtvDataGroupInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,810,2,2,5))
ciscoOtvDataGroupInfoGroup.setObjects(*((_B,_AY),(_B,_AZ)))
if mibBuilder.loadTexts:ciscoOtvDataGroupInfoGroup.setStatus(_A)
ciscoOtvAdjacencyGroup=ObjectGroup((1,3,6,1,4,1,9,9,810,2,2,6))
ciscoOtvAdjacencyGroup.setObjects(*((_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad)))
if mibBuilder.loadTexts:ciscoOtvAdjacencyGroup.setStatus(_A)
ciscoOtvArpNdCacheGroup=ObjectGroup((1,3,6,1,4,1,9,9,810,2,2,7))
ciscoOtvArpNdCacheGroup.setObjects(*((_B,_Ae),(_B,_Af),(_B,_Ag)))
if mibBuilder.loadTexts:ciscoOtvArpNdCacheGroup.setStatus(_A)
ciscoOtvRouteGroup=ObjectGroup((1,3,6,1,4,1,9,9,810,2,2,8))
ciscoOtvRouteGroup.setObjects(*((_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am)))
if mibBuilder.loadTexts:ciscoOtvRouteGroup.setStatus(_A)
ciscoOtvMcastRouteGroup=ObjectGroup((1,3,6,1,4,1,9,9,810,2,2,9))
ciscoOtvMcastRouteGroup.setObjects(*((_B,_An),(_B,_Ao),(_B,_Ap)))
if mibBuilder.loadTexts:ciscoOtvMcastRouteGroup.setStatus(_A)
ciscoOtvMcastRouteInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,810,2,2,10))
ciscoOtvMcastRouteInfoGroup.setObjects(*((_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au)))
if mibBuilder.loadTexts:ciscoOtvMcastRouteInfoGroup.setStatus(_A)
ciscoOtvMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,810,2,1,1))
ciscoOtvMIBCompliance.setObjects(*((_B,_Av),(_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_),(_B,_B0),(_B,_B1),(_B,_B2),(_B,_B3)))
if mibBuilder.loadTexts:ciscoOtvMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoOtvMIB':ciscoOtvMIB,'ciscoOtvMIBNotifs':ciscoOtvMIBNotifs,'ciscoOtvMIBObjects':ciscoOtvMIBObjects,'cotvGlobalObjects':cotvGlobalObjects,'cotvSiteObjects':cotvSiteObjects,_A1:cotvSiteIdAdmin,_A2:cotvSiteIdOper,_A3:cotvSiteVlan,_A4:cotvSiteVlanState,'cotvGlobalStatsObjects':cotvGlobalStatsObjects,'cotvOverlayObjects':cotvOverlayObjects,'cotvOverlayTable':cotvOverlayTable,'cotvOverlayEntry':cotvOverlayEntry,_H:cotvOverlayNumber,_A5:cotvOverlayVpnName,_A6:cotvOverlayVpnState,_A7:cotvOverlayVpnDownReason,_A8:cotvOverlayVlansExtendedFirst2k,_A9:cotvOverlayVlansExtendedSecond2k,_AA:cotvOverlayControlGroupAddrType,_AB:cotvOverlayControlGroupAddr,_AC:cotvOverlayBroadcastGroupAddrType,_AD:cotvOverlayBroadcastGroupAddr,_AE:cotvOverlayJoinInterface,_AF:cotvOverlaySourceInterface,_AG:cotvOverlayAedCapable,_AH:cotvOverlayAedIncapableReason,_AI:cotvOverlayAdjServerTransportType,_AJ:cotvOverlayAdjServerEnable,_AK:cotvOverlayPrimaryAdjServerAddrType,_AL:cotvOverlayPrimaryAdjServerAddr,_AM:cotvOverlaySecondaryAdjServerAddrType,_AN:cotvOverlaySecondaryAdjServerAddr,_AO:cotvOverlaySuppressArpND,_AP:cotvOverlayStorageType,_AQ:cotvOverlayRowStatus,'cotvVlansTable':cotvVlansTable,'cotvVlansEntry':cotvVlansEntry,_R:cotvVlanId,_AR:cotvVlanState,_AS:cotvVlanInactiveReason,_AT:cotvVlanAedAddrType,_AU:cotvVlanAedAddr,_AV:cotvVlanEdgeDevIsAed,'cotvDataGroupConfigTable':cotvDataGroupConfigTable,'cotvDataGroupConfigEntry':cotvDataGroupConfigEntry,_W:cotvDataGroupMcastRangeAddrType,_X:cotvDataGroupMcastRangeAddr,_Y:cotvDataGroupMcastRangePrefixLength,_AW:cotvDataGroupStorageType,_AX:cotvDataGroupRowStatus,'cotvDataGroupInfoTable':cotvDataGroupInfoTable,'cotvDataGroupInfoEntry':cotvDataGroupInfoEntry,_Z:cotvDataGroupActiveSrcLocation,_a:cotvDataGroupVlanId,_b:cotvDataGroupActiveGroupAddrType,_c:cotvDataGroupActiveGroupAddr,_d:cotvDataGroupActiveSrcAddrType,_e:cotvDataGroupActiveSrcAddr,_f:cotvDataGroupDeliveryGroupAddrType,_g:cotvDataGroupDeliveryGroupAddr,_h:cotvDataGroupDeliverySrcAddrType,_i:cotvDataGroupDeliverySrcAddr,_AY:cotvDataGroupJoinInterface,_AZ:cotvDataGroupLocalActiveSrcState,'cotvAdjacencyObjects':cotvAdjacencyObjects,'cotvAdjacencyDatabaseTable':cotvAdjacencyDatabaseTable,'cotvAdjacencyDatabaseEntry':cotvAdjacencyDatabaseEntry,_k:cotvAdjacentDevAddrType,_l:cotvAdjacentDevAddr,_Aa:cotvAdjacentDevSystemID,_Ab:cotvAdjacentDevName,_Ac:cotvAdjacentDevState,_Ad:cotvAdjacentDevUpTime,'cotvArpNdObjects':cotvArpNdObjects,'cotvArpNdCacheTable':cotvArpNdCacheTable,'cotvArpNdCacheEntry':cotvArpNdCacheEntry,_m:cotvArpNdCacheL3AddrType,_n:cotvArpNdCacheL3Addr,_Ae:cotvArpNdCacheMacAddr,_Af:cotvArpNdCacheAge,_Ag:cotvArpNdCacheTimeToExpire,'cotvRouteObjects':cotvRouteObjects,'cotvRouteTable':cotvRouteTable,'cotvRouteEntry':cotvRouteEntry,_o:cotvRouteVlanId,_p:cotvRouteMacAddr,_Ah:cotvRouteMetric,_Ai:cotvRouteUpTime,_Aj:cotvRouteOwner,_Ak:cotvRouteNextHopIf,_Al:cotvRouteNextHopAddrType,_Am:cotvRouteNextHopAddr,'cotvMcastRouteTable':cotvMcastRouteTable,'cotvMcastRouteEntry':cotvMcastRouteEntry,_q:cotvMcastRouteVlanId,_r:cotvMcastRouteActiveSrcAddrType,_s:cotvMcastRouteActiveSrcAddr,_t:cotvMcastRouteActiveGroupAddrType,_u:cotvMcastRouteActiveGroupAddr,_An:cotvMcastRouteOwners,_Ao:cotvMcastRouteMetric,_Ap:cotvMcastRouteUpTime,'cotvMcastRouteInfoTable':cotvMcastRouteInfoTable,'cotvMcastRouteInfoEntry':cotvMcastRouteInfoEntry,_v:cotvMcastRouteInfoVlanId,_w:cotvMcastRouteInfoActiveSrcAddrType,_x:cotvMcastRouteInfoActiveSrcAddr,_y:cotvMcastRouteInfoActiveGroupAddrType,_z:cotvMcastRouteInfoActiveGroupAddr,_A0:cotvMcastRouteInfoIf,_Aq:cotvMcastRouteInfoHostAddrType,_Ar:cotvMcastRouteInfoHostAddr,_As:cotvMcastRouteInfoProtocolOwners,_At:cotvMcastRouteInfoMetric,_Au:cotvMcastRouteInfoUpTime,'ciscoOtvMIBConform':ciscoOtvMIBConform,'ciscoOtvMIBCompliances':ciscoOtvMIBCompliances,'ciscoOtvMIBCompliance':ciscoOtvMIBCompliance,'ciscoOtvMIBGroups':ciscoOtvMIBGroups,_Av:ciscoOtvSiteGroup,_Aw:ciscoOtvOverlayGroup,_Ax:ciscoOtvVlanGroup,_Ay:ciscoOtvDataGroupConfigGroup,_Az:ciscoOtvDataGroupInfoGroup,_A_:ciscoOtvAdjacencyGroup,_B0:ciscoOtvArpNdCacheGroup,_B1:ciscoOtvRouteGroup,_B2:ciscoOtvMcastRouteGroup,_B3:ciscoOtvMcastRouteInfoGroup})