_A_='tripNotificationErr'
_Az='tripCease'
_Ay='tripConnectionCollision'
_Ax='tripHoldTimerExpired'
_Aw='tripUpdateMessageError'
_Av='tripOpenMessageError'
_Au='tripConnectionDropped'
_At='tripConnectionEstablished'
_As='tripItadTopologySeqNum'
_Ar='tripRouteCommunityItad'
_Aq='tripRouteReceivedTime'
_Ap='tripRouteConverted'
_Ao='tripRouteWithdrawn'
_An='tripRouteUnknown'
_Am='tripRouteAtomicAggregate'
_Al='tripRouteRoutedPath'
_Ak='tripRouteAdvertisementPath'
_Aj='tripRouteLocalPref'
_Ai='tripRouteMultiExitDisc'
_Ah='tripRouteNextHopServerItad'
_Ag='tripRouteNextHopServerPort'
_Af='tripRouteNextHopServer'
_Ae='tripRouteNextHopServerIAddrType'
_Ad='tripRouteAddressOriginatorId'
_Ac='tripRouteAddressSequenceNumber'
_Ab='tripRouteTRIBMask'
_Aa='tripPeerStateChangeTime'
_AZ='tripPeerInUpdateElapsedTime'
_AY='tripPeerFsmEstablishedTime'
_AX='tripPeerFsmEstablishedTransitions'
_AW='tripPeerOutTotalMessages'
_AV='tripPeerInTotalMessages'
_AU='tripPeerOutUpdates'
_AT='tripPeerInUpdates'
_AS='tripPeerRowStatus'
_AR='tripPeerStorage'
_AQ='tripPeerLearned'
_AP='tripPeerDisableTime'
_AO='tripPeerMaxPurgeTime'
_AN='tripPeerKeepAliveConfigured'
_AM='tripPeerHoldTimeConfigured'
_AL='tripPeerKeepAlive'
_AK='tripPeerHoldTime'
_AJ='tripPeerMaxRetryInterval'
_AI='tripPeerConnectRetryInterval'
_AH='tripPeerRemoteItad'
_AG='tripPeerSendReceiveMode'
_AF='tripPeerNegotiatedVersion'
_AE='tripPeerAdminStatus'
_AD='tripPeerIdentifier'
_AC='tripSupportedCommunityRowStatus'
_AB='tripRouteTypePeer'
_AA='tripSupportedCommunityStorage'
_A9='tripSupportedCommunityItad'
_A8='tripCfgStorage'
_A7='tripCfgSendReceiveMode'
_A6='tripCfgDisableTime'
_A5='tripCfgMaxPurgeTime'
_A4='tripCfgMinRouteAdvertisementInterval'
_A3='tripCfgMinItadOriginationInterval'
_A2='tripCfgPort'
_A1='tripCfgAddr'
_A0='tripCfgAddrIAddrType'
_z='tripCfgAdminStatus'
_y='tripCfgOperStatus'
_x='tripCfgIdentifier'
_w='tripCfgItad'
_v='tripCfgProtocolVersion'
_u='tripPeerStatisticsEntry'
_t='tripRouteCommunityId'
_s='tripPeerRemotePort'
_r='tripPeerRemoteAddr'
_q='tripPeerRemoteAddrInetType'
_p='tripSupportedCommunityId'
_o='tripRouteTypeAddrFamilyId'
_n='tripRouteTypeProtocolId'
_m='tripRouteTypePort'
_l='tripRouteTypeAddr'
_k='tripRouteTypeAddrInetType'
_j='TruthValue'
_i='tripNotifObjectGroup'
_h='tripNotificationGroup'
_g='tripPeerTableStatsGroup'
_f='tripItadTopologyGroup'
_e='tripRouteGroup'
_d='tripPeerTableConfigGroup'
_c='tripConfigGroup'
_b='tripItadTopologyId'
_a='tripItadTopologyOrigId'
_Z='tripRoutePeer'
_Y='tripRouteAddress'
_X='tripRouteAddressFamily'
_W='tripRouteAppProtocol'
_V='down'
_U='applRFC2788Group'
_T='StorageType'
_S='accessible-for-notify'
_R='OctetString'
_Q='tripNotifPeerErrSubcode'
_P='tripNotifPeerErrCode'
_O='tripPeerState'
_N='read-write'
_M='Integer32'
_L='tripNotifPeerAddr'
_K='tripNotifPeerAddrInetType'
_J='applIndex'
_I='tripNotifApplIndex'
_H='NETWORK-SERVICES-MIB'
_G='read-create'
_F='Seconds'
_E='not-accessible'
_D='Unsigned32'
_C='read-only'
_B='current'
_A='TRIP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_R,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType','InetPortNumber')
applIndex,applRFC2788Group=mibBuilder.importSymbols(_H,_J,_U)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_M,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso','mib-2')
DateAndTime,DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus',_T,'TextualConvention','TimeInterval','TimeStamp',_j)
TripAddressFamily,TripAppProtocol,TripCommunityId,TripId,TripItad,TripProtocolVersion,TripSendReceiveMode=mibBuilder.importSymbols('TRIP-TC-MIB','TripAddressFamily','TripAppProtocol','TripCommunityId','TripId','TripItad','TripProtocolVersion','TripSendReceiveMode')
tripMIB=ModuleIdentity((1,3,6,1,2,1,116))
if mibBuilder.loadTexts:tripMIB.setRevisions(('2004-09-02 00:00',))
_TripMIBNotifications_ObjectIdentity=ObjectIdentity
tripMIBNotifications=_TripMIBNotifications_ObjectIdentity((1,3,6,1,2,1,116,0))
_TripMIBObjects_ObjectIdentity=ObjectIdentity
tripMIBObjects=_TripMIBObjects_ObjectIdentity((1,3,6,1,2,1,116,1))
_TripCfgTable_Object=MibTable
tripCfgTable=_TripCfgTable_Object((1,3,6,1,2,1,116,1,1))
if mibBuilder.loadTexts:tripCfgTable.setStatus(_B)
_TripCfgEntry_Object=MibTableRow
tripCfgEntry=_TripCfgEntry_Object((1,3,6,1,2,1,116,1,1,1))
tripCfgEntry.setIndexNames((0,_H,_J))
if mibBuilder.loadTexts:tripCfgEntry.setStatus(_B)
_TripCfgProtocolVersion_Type=TripProtocolVersion
_TripCfgProtocolVersion_Object=MibTableColumn
tripCfgProtocolVersion=_TripCfgProtocolVersion_Object((1,3,6,1,2,1,116,1,1,1,1),_TripCfgProtocolVersion_Type())
tripCfgProtocolVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:tripCfgProtocolVersion.setStatus(_B)
_TripCfgItad_Type=TripItad
_TripCfgItad_Object=MibTableColumn
tripCfgItad=_TripCfgItad_Object((1,3,6,1,2,1,116,1,1,1,2),_TripCfgItad_Type())
tripCfgItad.setMaxAccess(_N)
if mibBuilder.loadTexts:tripCfgItad.setStatus(_B)
_TripCfgIdentifier_Type=TripId
_TripCfgIdentifier_Object=MibTableColumn
tripCfgIdentifier=_TripCfgIdentifier_Object((1,3,6,1,2,1,116,1,1,1,3),_TripCfgIdentifier_Type())
tripCfgIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:tripCfgIdentifier.setStatus(_B)
class _TripCfgAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_V,2)))
_TripCfgAdminStatus_Type.__name__=_M
_TripCfgAdminStatus_Object=MibTableColumn
tripCfgAdminStatus=_TripCfgAdminStatus_Object((1,3,6,1,2,1,116,1,1,1,4),_TripCfgAdminStatus_Type())
tripCfgAdminStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:tripCfgAdminStatus.setStatus(_B)
class _TripCfgOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('unknown',0),('up',1),(_V,2),('faulty',3)))
_TripCfgOperStatus_Type.__name__=_M
_TripCfgOperStatus_Object=MibTableColumn
tripCfgOperStatus=_TripCfgOperStatus_Object((1,3,6,1,2,1,116,1,1,1,5),_TripCfgOperStatus_Type())
tripCfgOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:tripCfgOperStatus.setStatus(_B)
_TripCfgAddrIAddrType_Type=InetAddressType
_TripCfgAddrIAddrType_Object=MibTableColumn
tripCfgAddrIAddrType=_TripCfgAddrIAddrType_Object((1,3,6,1,2,1,116,1,1,1,6),_TripCfgAddrIAddrType_Type())
tripCfgAddrIAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tripCfgAddrIAddrType.setStatus(_B)
_TripCfgAddr_Type=InetAddress
_TripCfgAddr_Object=MibTableColumn
tripCfgAddr=_TripCfgAddr_Object((1,3,6,1,2,1,116,1,1,1,7),_TripCfgAddr_Type())
tripCfgAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:tripCfgAddr.setStatus(_B)
_TripCfgPort_Type=InetPortNumber
_TripCfgPort_Object=MibTableColumn
tripCfgPort=_TripCfgPort_Object((1,3,6,1,2,1,116,1,1,1,8),_TripCfgPort_Type())
tripCfgPort.setMaxAccess(_N)
if mibBuilder.loadTexts:tripCfgPort.setStatus(_B)
class _TripCfgMinItadOriginationInterval_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TripCfgMinItadOriginationInterval_Type.__name__=_D
_TripCfgMinItadOriginationInterval_Object=MibTableColumn
tripCfgMinItadOriginationInterval=_TripCfgMinItadOriginationInterval_Object((1,3,6,1,2,1,116,1,1,1,9),_TripCfgMinItadOriginationInterval_Type())
tripCfgMinItadOriginationInterval.setMaxAccess(_N)
if mibBuilder.loadTexts:tripCfgMinItadOriginationInterval.setStatus(_B)
if mibBuilder.loadTexts:tripCfgMinItadOriginationInterval.setUnits(_F)
class _TripCfgMinRouteAdvertisementInterval_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TripCfgMinRouteAdvertisementInterval_Type.__name__=_D
_TripCfgMinRouteAdvertisementInterval_Object=MibTableColumn
tripCfgMinRouteAdvertisementInterval=_TripCfgMinRouteAdvertisementInterval_Object((1,3,6,1,2,1,116,1,1,1,10),_TripCfgMinRouteAdvertisementInterval_Type())
tripCfgMinRouteAdvertisementInterval.setMaxAccess(_N)
if mibBuilder.loadTexts:tripCfgMinRouteAdvertisementInterval.setStatus(_B)
if mibBuilder.loadTexts:tripCfgMinRouteAdvertisementInterval.setUnits(_F)
class _TripCfgMaxPurgeTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TripCfgMaxPurgeTime_Type.__name__=_D
_TripCfgMaxPurgeTime_Object=MibTableColumn
tripCfgMaxPurgeTime=_TripCfgMaxPurgeTime_Object((1,3,6,1,2,1,116,1,1,1,11),_TripCfgMaxPurgeTime_Type())
tripCfgMaxPurgeTime.setMaxAccess(_N)
if mibBuilder.loadTexts:tripCfgMaxPurgeTime.setStatus(_B)
if mibBuilder.loadTexts:tripCfgMaxPurgeTime.setUnits(_F)
class _TripCfgDisableTime_Type(Unsigned32):defaultValue=180;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TripCfgDisableTime_Type.__name__=_D
_TripCfgDisableTime_Object=MibTableColumn
tripCfgDisableTime=_TripCfgDisableTime_Object((1,3,6,1,2,1,116,1,1,1,12),_TripCfgDisableTime_Type())
tripCfgDisableTime.setMaxAccess(_N)
if mibBuilder.loadTexts:tripCfgDisableTime.setStatus(_B)
if mibBuilder.loadTexts:tripCfgDisableTime.setUnits(_F)
_TripCfgSendReceiveMode_Type=TripSendReceiveMode
_TripCfgSendReceiveMode_Object=MibTableColumn
tripCfgSendReceiveMode=_TripCfgSendReceiveMode_Object((1,3,6,1,2,1,116,1,1,1,13),_TripCfgSendReceiveMode_Type())
tripCfgSendReceiveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tripCfgSendReceiveMode.setStatus(_B)
class _TripCfgStorage_Type(StorageType):defaultValue=3
_TripCfgStorage_Type.__name__=_T
_TripCfgStorage_Object=MibTableColumn
tripCfgStorage=_TripCfgStorage_Object((1,3,6,1,2,1,116,1,1,1,14),_TripCfgStorage_Type())
tripCfgStorage.setMaxAccess(_N)
if mibBuilder.loadTexts:tripCfgStorage.setStatus(_B)
_TripRouteTypeTable_Object=MibTable
tripRouteTypeTable=_TripRouteTypeTable_Object((1,3,6,1,2,1,116,1,2))
if mibBuilder.loadTexts:tripRouteTypeTable.setStatus(_B)
_TripRouteTypeEntry_Object=MibTableRow
tripRouteTypeEntry=_TripRouteTypeEntry_Object((1,3,6,1,2,1,116,1,2,1))
tripRouteTypeEntry.setIndexNames((0,_H,_J),(0,_A,_k),(0,_A,_l),(0,_A,_m),(0,_A,_n),(0,_A,_o))
if mibBuilder.loadTexts:tripRouteTypeEntry.setStatus(_B)
_TripRouteTypeAddrInetType_Type=InetAddressType
_TripRouteTypeAddrInetType_Object=MibTableColumn
tripRouteTypeAddrInetType=_TripRouteTypeAddrInetType_Object((1,3,6,1,2,1,116,1,2,1,1),_TripRouteTypeAddrInetType_Type())
tripRouteTypeAddrInetType.setMaxAccess(_E)
if mibBuilder.loadTexts:tripRouteTypeAddrInetType.setStatus(_B)
_TripRouteTypeAddr_Type=InetAddress
_TripRouteTypeAddr_Object=MibTableColumn
tripRouteTypeAddr=_TripRouteTypeAddr_Object((1,3,6,1,2,1,116,1,2,1,2),_TripRouteTypeAddr_Type())
tripRouteTypeAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:tripRouteTypeAddr.setStatus(_B)
_TripRouteTypePort_Type=InetPortNumber
_TripRouteTypePort_Object=MibTableColumn
tripRouteTypePort=_TripRouteTypePort_Object((1,3,6,1,2,1,116,1,2,1,3),_TripRouteTypePort_Type())
tripRouteTypePort.setMaxAccess(_E)
if mibBuilder.loadTexts:tripRouteTypePort.setStatus(_B)
_TripRouteTypeProtocolId_Type=TripAppProtocol
_TripRouteTypeProtocolId_Object=MibTableColumn
tripRouteTypeProtocolId=_TripRouteTypeProtocolId_Object((1,3,6,1,2,1,116,1,2,1,4),_TripRouteTypeProtocolId_Type())
tripRouteTypeProtocolId.setMaxAccess(_E)
if mibBuilder.loadTexts:tripRouteTypeProtocolId.setStatus(_B)
_TripRouteTypeAddrFamilyId_Type=TripAddressFamily
_TripRouteTypeAddrFamilyId_Object=MibTableColumn
tripRouteTypeAddrFamilyId=_TripRouteTypeAddrFamilyId_Object((1,3,6,1,2,1,116,1,2,1,5),_TripRouteTypeAddrFamilyId_Type())
tripRouteTypeAddrFamilyId.setMaxAccess(_E)
if mibBuilder.loadTexts:tripRouteTypeAddrFamilyId.setStatus(_B)
class _TripRouteTypePeer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('remote',2)))
_TripRouteTypePeer_Type.__name__=_M
_TripRouteTypePeer_Object=MibTableColumn
tripRouteTypePeer=_TripRouteTypePeer_Object((1,3,6,1,2,1,116,1,2,1,6),_TripRouteTypePeer_Type())
tripRouteTypePeer.setMaxAccess(_C)
if mibBuilder.loadTexts:tripRouteTypePeer.setStatus(_B)
_TripSupportedCommunityTable_Object=MibTable
tripSupportedCommunityTable=_TripSupportedCommunityTable_Object((1,3,6,1,2,1,116,1,3))
if mibBuilder.loadTexts:tripSupportedCommunityTable.setStatus(_B)
_TripSupportedCommunityEntry_Object=MibTableRow
tripSupportedCommunityEntry=_TripSupportedCommunityEntry_Object((1,3,6,1,2,1,116,1,3,1))
tripSupportedCommunityEntry.setIndexNames((0,_H,_J),(0,_A,_p))
if mibBuilder.loadTexts:tripSupportedCommunityEntry.setStatus(_B)
_TripSupportedCommunityId_Type=TripCommunityId
_TripSupportedCommunityId_Object=MibTableColumn
tripSupportedCommunityId=_TripSupportedCommunityId_Object((1,3,6,1,2,1,116,1,3,1,1),_TripSupportedCommunityId_Type())
tripSupportedCommunityId.setMaxAccess(_E)
if mibBuilder.loadTexts:tripSupportedCommunityId.setStatus(_B)
_TripSupportedCommunityItad_Type=TripItad
_TripSupportedCommunityItad_Object=MibTableColumn
tripSupportedCommunityItad=_TripSupportedCommunityItad_Object((1,3,6,1,2,1,116,1,3,1,2),_TripSupportedCommunityItad_Type())
tripSupportedCommunityItad.setMaxAccess(_G)
if mibBuilder.loadTexts:tripSupportedCommunityItad.setStatus(_B)
class _TripSupportedCommunityStorage_Type(StorageType):defaultValue=3
_TripSupportedCommunityStorage_Type.__name__=_T
_TripSupportedCommunityStorage_Object=MibTableColumn
tripSupportedCommunityStorage=_TripSupportedCommunityStorage_Object((1,3,6,1,2,1,116,1,3,1,3),_TripSupportedCommunityStorage_Type())
tripSupportedCommunityStorage.setMaxAccess(_G)
if mibBuilder.loadTexts:tripSupportedCommunityStorage.setStatus(_B)
_TripSupportedCommunityRowStatus_Type=RowStatus
_TripSupportedCommunityRowStatus_Object=MibTableColumn
tripSupportedCommunityRowStatus=_TripSupportedCommunityRowStatus_Object((1,3,6,1,2,1,116,1,3,1,4),_TripSupportedCommunityRowStatus_Type())
tripSupportedCommunityRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:tripSupportedCommunityRowStatus.setStatus(_B)
_TripPeerTable_Object=MibTable
tripPeerTable=_TripPeerTable_Object((1,3,6,1,2,1,116,1,4))
if mibBuilder.loadTexts:tripPeerTable.setStatus(_B)
_TripPeerEntry_Object=MibTableRow
tripPeerEntry=_TripPeerEntry_Object((1,3,6,1,2,1,116,1,4,1))
tripPeerEntry.setIndexNames((0,_H,_J),(0,_A,_q),(0,_A,_r),(0,_A,_s))
if mibBuilder.loadTexts:tripPeerEntry.setStatus(_B)
_TripPeerRemoteAddrInetType_Type=InetAddressType
_TripPeerRemoteAddrInetType_Object=MibTableColumn
tripPeerRemoteAddrInetType=_TripPeerRemoteAddrInetType_Object((1,3,6,1,2,1,116,1,4,1,1),_TripPeerRemoteAddrInetType_Type())
tripPeerRemoteAddrInetType.setMaxAccess(_E)
if mibBuilder.loadTexts:tripPeerRemoteAddrInetType.setStatus(_B)
_TripPeerRemoteAddr_Type=InetAddress
_TripPeerRemoteAddr_Object=MibTableColumn
tripPeerRemoteAddr=_TripPeerRemoteAddr_Object((1,3,6,1,2,1,116,1,4,1,2),_TripPeerRemoteAddr_Type())
tripPeerRemoteAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:tripPeerRemoteAddr.setStatus(_B)
_TripPeerRemotePort_Type=InetPortNumber
_TripPeerRemotePort_Object=MibTableColumn
tripPeerRemotePort=_TripPeerRemotePort_Object((1,3,6,1,2,1,116,1,4,1,3),_TripPeerRemotePort_Type())
tripPeerRemotePort.setMaxAccess(_E)
if mibBuilder.loadTexts:tripPeerRemotePort.setStatus(_B)
_TripPeerIdentifier_Type=TripId
_TripPeerIdentifier_Object=MibTableColumn
tripPeerIdentifier=_TripPeerIdentifier_Object((1,3,6,1,2,1,116,1,4,1,4),_TripPeerIdentifier_Type())
tripPeerIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:tripPeerIdentifier.setStatus(_B)
class _TripPeerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('idle',1),('connect',2),('active',3),('openSent',4),('openConfirm',5),('established',6)))
_TripPeerState_Type.__name__=_M
_TripPeerState_Object=MibTableColumn
tripPeerState=_TripPeerState_Object((1,3,6,1,2,1,116,1,4,1,5),_TripPeerState_Type())
tripPeerState.setMaxAccess(_C)
if mibBuilder.loadTexts:tripPeerState.setStatus(_B)
class _TripPeerAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_V,2)))
_TripPeerAdminStatus_Type.__name__=_M
_TripPeerAdminStatus_Object=MibTableColumn
tripPeerAdminStatus=_TripPeerAdminStatus_Object((1,3,6,1,2,1,116,1,4,1,6),_TripPeerAdminStatus_Type())
tripPeerAdminStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:tripPeerAdminStatus.setStatus(_B)
_TripPeerNegotiatedVersion_Type=TripProtocolVersion
_TripPeerNegotiatedVersion_Object=MibTableColumn
tripPeerNegotiatedVersion=_TripPeerNegotiatedVersion_Object((1,3,6,1,2,1,116,1,4,1,7),_TripPeerNegotiatedVersion_Type())
tripPeerNegotiatedVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:tripPeerNegotiatedVersion.setStatus(_B)
_TripPeerSendReceiveMode_Type=TripSendReceiveMode
_TripPeerSendReceiveMode_Object=MibTableColumn
tripPeerSendReceiveMode=_TripPeerSendReceiveMode_Object((1,3,6,1,2,1,116,1,4,1,8),_TripPeerSendReceiveMode_Type())
tripPeerSendReceiveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:tripPeerSendReceiveMode.setStatus(_B)
_TripPeerRemoteItad_Type=TripItad
_TripPeerRemoteItad_Object=MibTableColumn
tripPeerRemoteItad=_TripPeerRemoteItad_Object((1,3,6,1,2,1,116,1,4,1,9),_TripPeerRemoteItad_Type())
tripPeerRemoteItad.setMaxAccess(_C)
if mibBuilder.loadTexts:tripPeerRemoteItad.setStatus(_B)
class _TripPeerConnectRetryInterval_Type(Unsigned32):defaultValue=120;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_TripPeerConnectRetryInterval_Type.__name__=_D
_TripPeerConnectRetryInterval_Object=MibTableColumn
tripPeerConnectRetryInterval=_TripPeerConnectRetryInterval_Object((1,3,6,1,2,1,116,1,4,1,10),_TripPeerConnectRetryInterval_Type())
tripPeerConnectRetryInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:tripPeerConnectRetryInterval.setStatus(_B)
if mibBuilder.loadTexts:tripPeerConnectRetryInterval.setUnits(_F)
class _TripPeerMaxRetryInterval_Type(Unsigned32):defaultValue=360;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_TripPeerMaxRetryInterval_Type.__name__=_D
_TripPeerMaxRetryInterval_Object=MibTableColumn
tripPeerMaxRetryInterval=_TripPeerMaxRetryInterval_Object((1,3,6,1,2,1,116,1,4,1,11),_TripPeerMaxRetryInterval_Type())
tripPeerMaxRetryInterval.setMaxAccess(_G)
if mibBuilder.loadTexts:tripPeerMaxRetryInterval.setStatus(_B)
if mibBuilder.loadTexts:tripPeerMaxRetryInterval.setUnits(_F)
class _TripPeerHoldTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TripPeerHoldTime_Type.__name__=_D
_TripPeerHoldTime_Object=MibTableColumn
tripPeerHoldTime=_TripPeerHoldTime_Object((1,3,6,1,2,1,116,1,4,1,12),_TripPeerHoldTime_Type())
tripPeerHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tripPeerHoldTime.setStatus(_B)
if mibBuilder.loadTexts:tripPeerHoldTime.setUnits(_F)
class _TripPeerKeepAlive_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TripPeerKeepAlive_Type.__name__=_D
_TripPeerKeepAlive_Object=MibTableColumn
tripPeerKeepAlive=_TripPeerKeepAlive_Object((1,3,6,1,2,1,116,1,4,1,13),_TripPeerKeepAlive_Type())
tripPeerKeepAlive.setMaxAccess(_C)
if mibBuilder.loadTexts:tripPeerKeepAlive.setStatus(_B)
if mibBuilder.loadTexts:tripPeerKeepAlive.setUnits(_F)
class _TripPeerHoldTimeConfigured_Type(Unsigned32):defaultValue=240;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_TripPeerHoldTimeConfigured_Type.__name__=_D
_TripPeerHoldTimeConfigured_Object=MibTableColumn
tripPeerHoldTimeConfigured=_TripPeerHoldTimeConfigured_Object((1,3,6,1,2,1,116,1,4,1,14),_TripPeerHoldTimeConfigured_Type())
tripPeerHoldTimeConfigured.setMaxAccess(_G)
if mibBuilder.loadTexts:tripPeerHoldTimeConfigured.setStatus(_B)
if mibBuilder.loadTexts:tripPeerHoldTimeConfigured.setUnits(_F)
class _TripPeerKeepAliveConfigured_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TripPeerKeepAliveConfigured_Type.__name__=_D
_TripPeerKeepAliveConfigured_Object=MibTableColumn
tripPeerKeepAliveConfigured=_TripPeerKeepAliveConfigured_Object((1,3,6,1,2,1,116,1,4,1,15),_TripPeerKeepAliveConfigured_Type())
tripPeerKeepAliveConfigured.setMaxAccess(_G)
if mibBuilder.loadTexts:tripPeerKeepAliveConfigured.setStatus(_B)
if mibBuilder.loadTexts:tripPeerKeepAliveConfigured.setUnits(_F)
class _TripPeerMaxPurgeTime_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TripPeerMaxPurgeTime_Type.__name__=_D
_TripPeerMaxPurgeTime_Object=MibTableColumn
tripPeerMaxPurgeTime=_TripPeerMaxPurgeTime_Object((1,3,6,1,2,1,116,1,4,1,16),_TripPeerMaxPurgeTime_Type())
tripPeerMaxPurgeTime.setMaxAccess(_G)
if mibBuilder.loadTexts:tripPeerMaxPurgeTime.setStatus(_B)
if mibBuilder.loadTexts:tripPeerMaxPurgeTime.setUnits(_F)
class _TripPeerDisableTime_Type(Unsigned32):defaultValue=180;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TripPeerDisableTime_Type.__name__=_D
_TripPeerDisableTime_Object=MibTableColumn
tripPeerDisableTime=_TripPeerDisableTime_Object((1,3,6,1,2,1,116,1,4,1,17),_TripPeerDisableTime_Type())
tripPeerDisableTime.setMaxAccess(_G)
if mibBuilder.loadTexts:tripPeerDisableTime.setStatus(_B)
if mibBuilder.loadTexts:tripPeerDisableTime.setUnits(_F)
class _TripPeerLearned_Type(TruthValue):defaultValue=2
_TripPeerLearned_Type.__name__=_j
_TripPeerLearned_Object=MibTableColumn
tripPeerLearned=_TripPeerLearned_Object((1,3,6,1,2,1,116,1,4,1,18),_TripPeerLearned_Type())
tripPeerLearned.setMaxAccess(_C)
if mibBuilder.loadTexts:tripPeerLearned.setStatus(_B)
class _TripPeerStorage_Type(StorageType):defaultValue=3
_TripPeerStorage_Type.__name__=_T
_TripPeerStorage_Object=MibTableColumn
tripPeerStorage=_TripPeerStorage_Object((1,3,6,1,2,1,116,1,4,1,19),_TripPeerStorage_Type())
tripPeerStorage.setMaxAccess(_G)
if mibBuilder.loadTexts:tripPeerStorage.setStatus(_B)
_TripPeerRowStatus_Type=RowStatus
_TripPeerRowStatus_Object=MibTableColumn
tripPeerRowStatus=_TripPeerRowStatus_Object((1,3,6,1,2,1,116,1,4,1,20),_TripPeerRowStatus_Type())
tripPeerRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:tripPeerRowStatus.setStatus(_B)
_TripPeerStatisticsTable_Object=MibTable
tripPeerStatisticsTable=_TripPeerStatisticsTable_Object((1,3,6,1,2,1,116,1,5))
if mibBuilder.loadTexts:tripPeerStatisticsTable.setStatus(_B)
_TripPeerStatisticsEntry_Object=MibTableRow
tripPeerStatisticsEntry=_TripPeerStatisticsEntry_Object((1,3,6,1,2,1,116,1,5,1))
if mibBuilder.loadTexts:tripPeerStatisticsEntry.setStatus(_B)
_TripPeerInUpdates_Type=Counter32
_TripPeerInUpdates_Object=MibTableColumn
tripPeerInUpdates=_TripPeerInUpdates_Object((1,3,6,1,2,1,116,1,5,1,1),_TripPeerInUpdates_Type())
tripPeerInUpdates.setMaxAccess(_C)
if mibBuilder.loadTexts:tripPeerInUpdates.setStatus(_B)
_TripPeerOutUpdates_Type=Counter32
_TripPeerOutUpdates_Object=MibTableColumn
tripPeerOutUpdates=_TripPeerOutUpdates_Object((1,3,6,1,2,1,116,1,5,1,2),_TripPeerOutUpdates_Type())
tripPeerOutUpdates.setMaxAccess(_C)
if mibBuilder.loadTexts:tripPeerOutUpdates.setStatus(_B)
_TripPeerInTotalMessages_Type=Counter32
_TripPeerInTotalMessages_Object=MibTableColumn
tripPeerInTotalMessages=_TripPeerInTotalMessages_Object((1,3,6,1,2,1,116,1,5,1,3),_TripPeerInTotalMessages_Type())
tripPeerInTotalMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:tripPeerInTotalMessages.setStatus(_B)
_TripPeerOutTotalMessages_Type=Counter32
_TripPeerOutTotalMessages_Object=MibTableColumn
tripPeerOutTotalMessages=_TripPeerOutTotalMessages_Object((1,3,6,1,2,1,116,1,5,1,4),_TripPeerOutTotalMessages_Type())
tripPeerOutTotalMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:tripPeerOutTotalMessages.setStatus(_B)
_TripPeerFsmEstablishedTransitions_Type=Counter32
_TripPeerFsmEstablishedTransitions_Object=MibTableColumn
tripPeerFsmEstablishedTransitions=_TripPeerFsmEstablishedTransitions_Object((1,3,6,1,2,1,116,1,5,1,5),_TripPeerFsmEstablishedTransitions_Type())
tripPeerFsmEstablishedTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:tripPeerFsmEstablishedTransitions.setStatus(_B)
_TripPeerFsmEstablishedTime_Type=DateAndTime
_TripPeerFsmEstablishedTime_Object=MibTableColumn
tripPeerFsmEstablishedTime=_TripPeerFsmEstablishedTime_Object((1,3,6,1,2,1,116,1,5,1,6),_TripPeerFsmEstablishedTime_Type())
tripPeerFsmEstablishedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tripPeerFsmEstablishedTime.setStatus(_B)
_TripPeerInUpdateElapsedTime_Type=TimeInterval
_TripPeerInUpdateElapsedTime_Object=MibTableColumn
tripPeerInUpdateElapsedTime=_TripPeerInUpdateElapsedTime_Object((1,3,6,1,2,1,116,1,5,1,7),_TripPeerInUpdateElapsedTime_Type())
tripPeerInUpdateElapsedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tripPeerInUpdateElapsedTime.setStatus(_B)
_TripPeerStateChangeTime_Type=TimeStamp
_TripPeerStateChangeTime_Object=MibTableColumn
tripPeerStateChangeTime=_TripPeerStateChangeTime_Object((1,3,6,1,2,1,116,1,5,1,8),_TripPeerStateChangeTime_Type())
tripPeerStateChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tripPeerStateChangeTime.setStatus(_B)
_TripRouteTable_Object=MibTable
tripRouteTable=_TripRouteTable_Object((1,3,6,1,2,1,116,1,6))
if mibBuilder.loadTexts:tripRouteTable.setStatus(_B)
_TripRouteEntry_Object=MibTableRow
tripRouteEntry=_TripRouteEntry_Object((1,3,6,1,2,1,116,1,6,1))
tripRouteEntry.setIndexNames((0,_H,_J),(0,_A,_W),(0,_A,_X),(0,_A,_Y),(0,_A,_Z))
if mibBuilder.loadTexts:tripRouteEntry.setStatus(_B)
_TripRouteAppProtocol_Type=TripAppProtocol
_TripRouteAppProtocol_Object=MibTableColumn
tripRouteAppProtocol=_TripRouteAppProtocol_Object((1,3,6,1,2,1,116,1,6,1,1),_TripRouteAppProtocol_Type())
tripRouteAppProtocol.setMaxAccess(_E)
if mibBuilder.loadTexts:tripRouteAppProtocol.setStatus(_B)
_TripRouteAddressFamily_Type=TripAddressFamily
_TripRouteAddressFamily_Object=MibTableColumn
tripRouteAddressFamily=_TripRouteAddressFamily_Object((1,3,6,1,2,1,116,1,6,1,2),_TripRouteAddressFamily_Type())
tripRouteAddressFamily.setMaxAccess(_E)
if mibBuilder.loadTexts:tripRouteAddressFamily.setStatus(_B)
class _TripRouteAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,105))
_TripRouteAddress_Type.__name__=_R
_TripRouteAddress_Object=MibTableColumn
tripRouteAddress=_TripRouteAddress_Object((1,3,6,1,2,1,116,1,6,1,3),_TripRouteAddress_Type())
tripRouteAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:tripRouteAddress.setStatus(_B)
_TripRoutePeer_Type=TripId
_TripRoutePeer_Object=MibTableColumn
tripRoutePeer=_TripRoutePeer_Object((1,3,6,1,2,1,116,1,6,1,4),_TripRoutePeer_Type())
tripRoutePeer.setMaxAccess(_E)
if mibBuilder.loadTexts:tripRoutePeer.setStatus(_B)
class _TripRouteTRIBMask_Type(Bits):namedValues=NamedValues(*(('adjTribIns',0),('extTrib',1),('locTrib',2),('adjTribOut',3)))
_TripRouteTRIBMask_Type.__name__='Bits'
_TripRouteTRIBMask_Object=MibTableColumn
tripRouteTRIBMask=_TripRouteTRIBMask_Object((1,3,6,1,2,1,116,1,6,1,5),_TripRouteTRIBMask_Type())
tripRouteTRIBMask.setMaxAccess(_C)
if mibBuilder.loadTexts:tripRouteTRIBMask.setStatus(_B)
class _TripRouteAddressSequenceNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TripRouteAddressSequenceNumber_Type.__name__=_D
_TripRouteAddressSequenceNumber_Object=MibTableColumn
tripRouteAddressSequenceNumber=_TripRouteAddressSequenceNumber_Object((1,3,6,1,2,1,116,1,6,1,6),_TripRouteAddressSequenceNumber_Type())
tripRouteAddressSequenceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:tripRouteAddressSequenceNumber.setStatus(_B)
_TripRouteAddressOriginatorId_Type=TripId
_TripRouteAddressOriginatorId_Object=MibTableColumn
tripRouteAddressOriginatorId=_TripRouteAddressOriginatorId_Object((1,3,6,1,2,1,116,1,6,1,7),_TripRouteAddressOriginatorId_Type())
tripRouteAddressOriginatorId.setMaxAccess(_C)
if mibBuilder.loadTexts:tripRouteAddressOriginatorId.setStatus(_B)
_TripRouteNextHopServerIAddrType_Type=InetAddressType
_TripRouteNextHopServerIAddrType_Object=MibTableColumn
tripRouteNextHopServerIAddrType=_TripRouteNextHopServerIAddrType_Object((1,3,6,1,2,1,116,1,6,1,8),_TripRouteNextHopServerIAddrType_Type())
tripRouteNextHopServerIAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:tripRouteNextHopServerIAddrType.setStatus(_B)
_TripRouteNextHopServer_Type=InetAddress
_TripRouteNextHopServer_Object=MibTableColumn
tripRouteNextHopServer=_TripRouteNextHopServer_Object((1,3,6,1,2,1,116,1,6,1,9),_TripRouteNextHopServer_Type())
tripRouteNextHopServer.setMaxAccess(_C)
if mibBuilder.loadTexts:tripRouteNextHopServer.setStatus(_B)
_TripRouteNextHopServerPort_Type=InetPortNumber
_TripRouteNextHopServerPort_Object=MibTableColumn
tripRouteNextHopServerPort=_TripRouteNextHopServerPort_Object((1,3,6,1,2,1,116,1,6,1,10),_TripRouteNextHopServerPort_Type())
tripRouteNextHopServerPort.setMaxAccess(_C)
if mibBuilder.loadTexts:tripRouteNextHopServerPort.setStatus(_B)
_TripRouteNextHopServerItad_Type=TripItad
_TripRouteNextHopServerItad_Object=MibTableColumn
tripRouteNextHopServerItad=_TripRouteNextHopServerItad_Object((1,3,6,1,2,1,116,1,6,1,11),_TripRouteNextHopServerItad_Type())
tripRouteNextHopServerItad.setMaxAccess(_C)
if mibBuilder.loadTexts:tripRouteNextHopServerItad.setStatus(_B)
class _TripRouteMultiExitDisc_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_TripRouteMultiExitDisc_Type.__name__=_D
_TripRouteMultiExitDisc_Object=MibTableColumn
tripRouteMultiExitDisc=_TripRouteMultiExitDisc_Object((1,3,6,1,2,1,116,1,6,1,12),_TripRouteMultiExitDisc_Type())
tripRouteMultiExitDisc.setMaxAccess(_C)
if mibBuilder.loadTexts:tripRouteMultiExitDisc.setStatus(_B)
class _TripRouteLocalPref_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_TripRouteLocalPref_Type.__name__=_D
_TripRouteLocalPref_Object=MibTableColumn
tripRouteLocalPref=_TripRouteLocalPref_Object((1,3,6,1,2,1,116,1,6,1,13),_TripRouteLocalPref_Type())
tripRouteLocalPref.setMaxAccess(_C)
if mibBuilder.loadTexts:tripRouteLocalPref.setStatus(_B)
class _TripRouteAdvertisementPath_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,252))
_TripRouteAdvertisementPath_Type.__name__=_R
_TripRouteAdvertisementPath_Object=MibTableColumn
tripRouteAdvertisementPath=_TripRouteAdvertisementPath_Object((1,3,6,1,2,1,116,1,6,1,14),_TripRouteAdvertisementPath_Type())
tripRouteAdvertisementPath.setMaxAccess(_C)
if mibBuilder.loadTexts:tripRouteAdvertisementPath.setStatus(_B)
class _TripRouteRoutedPath_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,252))
_TripRouteRoutedPath_Type.__name__=_R
_TripRouteRoutedPath_Object=MibTableColumn
tripRouteRoutedPath=_TripRouteRoutedPath_Object((1,3,6,1,2,1,116,1,6,1,15),_TripRouteRoutedPath_Type())
tripRouteRoutedPath.setMaxAccess(_C)
if mibBuilder.loadTexts:tripRouteRoutedPath.setStatus(_B)
_TripRouteAtomicAggregate_Type=TruthValue
_TripRouteAtomicAggregate_Object=MibTableColumn
tripRouteAtomicAggregate=_TripRouteAtomicAggregate_Object((1,3,6,1,2,1,116,1,6,1,16),_TripRouteAtomicAggregate_Type())
tripRouteAtomicAggregate.setMaxAccess(_C)
if mibBuilder.loadTexts:tripRouteAtomicAggregate.setStatus(_B)
class _TripRouteUnknown_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TripRouteUnknown_Type.__name__=_R
_TripRouteUnknown_Object=MibTableColumn
tripRouteUnknown=_TripRouteUnknown_Object((1,3,6,1,2,1,116,1,6,1,17),_TripRouteUnknown_Type())
tripRouteUnknown.setMaxAccess(_C)
if mibBuilder.loadTexts:tripRouteUnknown.setStatus(_B)
_TripRouteWithdrawn_Type=TruthValue
_TripRouteWithdrawn_Object=MibTableColumn
tripRouteWithdrawn=_TripRouteWithdrawn_Object((1,3,6,1,2,1,116,1,6,1,18),_TripRouteWithdrawn_Type())
tripRouteWithdrawn.setMaxAccess(_C)
if mibBuilder.loadTexts:tripRouteWithdrawn.setStatus(_B)
_TripRouteConverted_Type=TruthValue
_TripRouteConverted_Object=MibTableColumn
tripRouteConverted=_TripRouteConverted_Object((1,3,6,1,2,1,116,1,6,1,19),_TripRouteConverted_Type())
tripRouteConverted.setMaxAccess(_C)
if mibBuilder.loadTexts:tripRouteConverted.setStatus(_B)
_TripRouteReceivedTime_Type=TimeStamp
_TripRouteReceivedTime_Object=MibTableColumn
tripRouteReceivedTime=_TripRouteReceivedTime_Object((1,3,6,1,2,1,116,1,6,1,20),_TripRouteReceivedTime_Type())
tripRouteReceivedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tripRouteReceivedTime.setStatus(_B)
_TripRouteCommunityTable_Object=MibTable
tripRouteCommunityTable=_TripRouteCommunityTable_Object((1,3,6,1,2,1,116,1,7))
if mibBuilder.loadTexts:tripRouteCommunityTable.setStatus(_B)
_TripRouteCommunityEntry_Object=MibTableRow
tripRouteCommunityEntry=_TripRouteCommunityEntry_Object((1,3,6,1,2,1,116,1,7,1))
tripRouteCommunityEntry.setIndexNames((0,_H,_J),(0,_A,_W),(0,_A,_X),(0,_A,_Y),(0,_A,_Z),(0,_A,_t))
if mibBuilder.loadTexts:tripRouteCommunityEntry.setStatus(_B)
_TripRouteCommunityId_Type=TripCommunityId
_TripRouteCommunityId_Object=MibTableColumn
tripRouteCommunityId=_TripRouteCommunityId_Object((1,3,6,1,2,1,116,1,7,1,1),_TripRouteCommunityId_Type())
tripRouteCommunityId.setMaxAccess(_E)
if mibBuilder.loadTexts:tripRouteCommunityId.setStatus(_B)
_TripRouteCommunityItad_Type=TripItad
_TripRouteCommunityItad_Object=MibTableColumn
tripRouteCommunityItad=_TripRouteCommunityItad_Object((1,3,6,1,2,1,116,1,7,1,2),_TripRouteCommunityItad_Type())
tripRouteCommunityItad.setMaxAccess(_C)
if mibBuilder.loadTexts:tripRouteCommunityItad.setStatus(_B)
_TripItadTopologyTable_Object=MibTable
tripItadTopologyTable=_TripItadTopologyTable_Object((1,3,6,1,2,1,116,1,8))
if mibBuilder.loadTexts:tripItadTopologyTable.setStatus(_B)
_TripItadTopologyEntry_Object=MibTableRow
tripItadTopologyEntry=_TripItadTopologyEntry_Object((1,3,6,1,2,1,116,1,8,1))
tripItadTopologyEntry.setIndexNames((0,_H,_J),(0,_A,_a))
if mibBuilder.loadTexts:tripItadTopologyEntry.setStatus(_B)
_TripItadTopologyOrigId_Type=TripId
_TripItadTopologyOrigId_Object=MibTableColumn
tripItadTopologyOrigId=_TripItadTopologyOrigId_Object((1,3,6,1,2,1,116,1,8,1,1),_TripItadTopologyOrigId_Type())
tripItadTopologyOrigId.setMaxAccess(_E)
if mibBuilder.loadTexts:tripItadTopologyOrigId.setStatus(_B)
class _TripItadTopologySeqNum_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TripItadTopologySeqNum_Type.__name__=_D
_TripItadTopologySeqNum_Object=MibTableColumn
tripItadTopologySeqNum=_TripItadTopologySeqNum_Object((1,3,6,1,2,1,116,1,8,1,2),_TripItadTopologySeqNum_Type())
tripItadTopologySeqNum.setMaxAccess(_C)
if mibBuilder.loadTexts:tripItadTopologySeqNum.setStatus(_B)
_TripItadTopologyIdTable_Object=MibTable
tripItadTopologyIdTable=_TripItadTopologyIdTable_Object((1,3,6,1,2,1,116,1,9))
if mibBuilder.loadTexts:tripItadTopologyIdTable.setStatus(_B)
_TripItadTopologyIdEntry_Object=MibTableRow
tripItadTopologyIdEntry=_TripItadTopologyIdEntry_Object((1,3,6,1,2,1,116,1,9,1))
tripItadTopologyIdEntry.setIndexNames((0,_H,_J),(0,_A,_a),(0,_A,_b))
if mibBuilder.loadTexts:tripItadTopologyIdEntry.setStatus(_B)
_TripItadTopologyId_Type=TripId
_TripItadTopologyId_Object=MibTableColumn
tripItadTopologyId=_TripItadTopologyId_Object((1,3,6,1,2,1,116,1,9,1,1),_TripItadTopologyId_Type())
tripItadTopologyId.setMaxAccess(_C)
if mibBuilder.loadTexts:tripItadTopologyId.setStatus(_B)
_TripMIBConformance_ObjectIdentity=ObjectIdentity
tripMIBConformance=_TripMIBConformance_ObjectIdentity((1,3,6,1,2,1,116,2))
_TripMIBCompliances_ObjectIdentity=ObjectIdentity
tripMIBCompliances=_TripMIBCompliances_ObjectIdentity((1,3,6,1,2,1,116,2,1))
_TripMIBGroups_ObjectIdentity=ObjectIdentity
tripMIBGroups=_TripMIBGroups_ObjectIdentity((1,3,6,1,2,1,116,2,2))
_TripMIBNotifObjects_ObjectIdentity=ObjectIdentity
tripMIBNotifObjects=_TripMIBNotifObjects_ObjectIdentity((1,3,6,1,2,1,116,3))
class _TripNotifApplIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TripNotifApplIndex_Type.__name__=_M
_TripNotifApplIndex_Object=MibScalar
tripNotifApplIndex=_TripNotifApplIndex_Object((1,3,6,1,2,1,116,3,1),_TripNotifApplIndex_Type())
tripNotifApplIndex.setMaxAccess(_S)
if mibBuilder.loadTexts:tripNotifApplIndex.setStatus(_B)
_TripNotifPeerAddrInetType_Type=InetAddressType
_TripNotifPeerAddrInetType_Object=MibScalar
tripNotifPeerAddrInetType=_TripNotifPeerAddrInetType_Object((1,3,6,1,2,1,116,3,2),_TripNotifPeerAddrInetType_Type())
tripNotifPeerAddrInetType.setMaxAccess(_S)
if mibBuilder.loadTexts:tripNotifPeerAddrInetType.setStatus(_B)
_TripNotifPeerAddr_Type=InetAddress
_TripNotifPeerAddr_Object=MibScalar
tripNotifPeerAddr=_TripNotifPeerAddr_Object((1,3,6,1,2,1,116,3,3),_TripNotifPeerAddr_Type())
tripNotifPeerAddr.setMaxAccess(_S)
if mibBuilder.loadTexts:tripNotifPeerAddr.setStatus(_B)
class _TripNotifPeerErrCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('messageHeader',1),('openMessage',2),('updateMessage',3),('holdTimerExpired',4),('finiteStateMachine',5),('cease',6),('tripNotification',7)))
_TripNotifPeerErrCode_Type.__name__=_M
_TripNotifPeerErrCode_Object=MibScalar
tripNotifPeerErrCode=_TripNotifPeerErrCode_Object((1,3,6,1,2,1,116,3,4),_TripNotifPeerErrCode_Type())
tripNotifPeerErrCode.setMaxAccess(_S)
if mibBuilder.loadTexts:tripNotifPeerErrCode.setStatus(_B)
class _TripNotifPeerErrSubcode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_TripNotifPeerErrSubcode_Type.__name__=_D
_TripNotifPeerErrSubcode_Object=MibScalar
tripNotifPeerErrSubcode=_TripNotifPeerErrSubcode_Object((1,3,6,1,2,1,116,3,5),_TripNotifPeerErrSubcode_Type())
tripNotifPeerErrSubcode.setMaxAccess(_S)
if mibBuilder.loadTexts:tripNotifPeerErrSubcode.setStatus(_B)
tripPeerEntry.registerAugmentions((_A,_u))
tripPeerStatisticsEntry.setIndexNames(*tripPeerEntry.getIndexNames())
tripConfigGroup=ObjectGroup((1,3,6,1,2,1,116,2,2,1))
tripConfigGroup.setObjects(*((_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:tripConfigGroup.setStatus(_B)
tripPeerTableConfigGroup=ObjectGroup((1,3,6,1,2,1,116,2,2,2))
tripPeerTableConfigGroup.setObjects(*((_A,_AD),(_A,_O),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS)))
if mibBuilder.loadTexts:tripPeerTableConfigGroup.setStatus(_B)
tripPeerTableStatsGroup=ObjectGroup((1,3,6,1,2,1,116,2,2,3))
tripPeerTableStatsGroup.setObjects(*((_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa)))
if mibBuilder.loadTexts:tripPeerTableStatsGroup.setStatus(_B)
tripRouteGroup=ObjectGroup((1,3,6,1,2,1,116,2,2,4))
tripRouteGroup.setObjects(*((_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar)))
if mibBuilder.loadTexts:tripRouteGroup.setStatus(_B)
tripItadTopologyGroup=ObjectGroup((1,3,6,1,2,1,116,2,2,5))
tripItadTopologyGroup.setObjects(*((_A,_As),(_A,_b)))
if mibBuilder.loadTexts:tripItadTopologyGroup.setStatus(_B)
tripNotifObjectGroup=ObjectGroup((1,3,6,1,2,1,116,2,2,7))
tripNotifObjectGroup.setObjects(*((_A,_I),(_A,_K),(_A,_L),(_A,_P),(_A,_Q)))
if mibBuilder.loadTexts:tripNotifObjectGroup.setStatus(_B)
tripConnectionEstablished=NotificationType((1,3,6,1,2,1,116,0,1))
tripConnectionEstablished.setObjects(*((_A,_I),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:tripConnectionEstablished.setStatus(_B)
tripConnectionDropped=NotificationType((1,3,6,1,2,1,116,0,2))
tripConnectionDropped.setObjects(*((_A,_I),(_A,_K),(_A,_L)))
if mibBuilder.loadTexts:tripConnectionDropped.setStatus(_B)
tripFSM=NotificationType((1,3,6,1,2,1,116,0,3))
tripFSM.setObjects(*((_A,_I),(_A,_K),(_A,_L),(_A,_P),(_A,_Q),(_A,_O)))
if mibBuilder.loadTexts:tripFSM.setStatus(_B)
tripOpenMessageError=NotificationType((1,3,6,1,2,1,116,0,4))
tripOpenMessageError.setObjects(*((_A,_I),(_A,_K),(_A,_L),(_A,_P),(_A,_Q),(_A,_O)))
if mibBuilder.loadTexts:tripOpenMessageError.setStatus(_B)
tripUpdateMessageError=NotificationType((1,3,6,1,2,1,116,0,5))
tripUpdateMessageError.setObjects(*((_A,_I),(_A,_K),(_A,_L),(_A,_P),(_A,_Q),(_A,_O)))
if mibBuilder.loadTexts:tripUpdateMessageError.setStatus(_B)
tripHoldTimerExpired=NotificationType((1,3,6,1,2,1,116,0,6))
tripHoldTimerExpired.setObjects(*((_A,_I),(_A,_K),(_A,_L),(_A,_P),(_A,_Q),(_A,_O)))
if mibBuilder.loadTexts:tripHoldTimerExpired.setStatus(_B)
tripConnectionCollision=NotificationType((1,3,6,1,2,1,116,0,7))
tripConnectionCollision.setObjects((_A,_I))
if mibBuilder.loadTexts:tripConnectionCollision.setStatus(_B)
tripCease=NotificationType((1,3,6,1,2,1,116,0,8))
tripCease.setObjects(*((_A,_I),(_A,_K),(_A,_L),(_A,_P),(_A,_Q),(_A,_O)))
if mibBuilder.loadTexts:tripCease.setStatus(_B)
tripNotificationErr=NotificationType((1,3,6,1,2,1,116,0,9))
tripNotificationErr.setObjects((_A,_I))
if mibBuilder.loadTexts:tripNotificationErr.setStatus(_B)
tripNotificationGroup=NotificationGroup((1,3,6,1,2,1,116,2,2,6))
tripNotificationGroup.setObjects(*((_A,_At),(_A,_Au),(_A,'tripFSM'),(_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az),(_A,_A_)))
if mibBuilder.loadTexts:tripNotificationGroup.setStatus(_B)
tripMIBFullCompliance=ModuleCompliance((1,3,6,1,2,1,116,2,1,1))
tripMIBFullCompliance.setObjects(*((_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_H,_U)))
if mibBuilder.loadTexts:tripMIBFullCompliance.setStatus(_B)
tripMIBReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,116,2,1,2))
tripMIBReadOnlyCompliance.setObjects(*((_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_H,_U)))
if mibBuilder.loadTexts:tripMIBReadOnlyCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'tripMIB':tripMIB,'tripMIBNotifications':tripMIBNotifications,_At:tripConnectionEstablished,_Au:tripConnectionDropped,'tripFSM':tripFSM,_Av:tripOpenMessageError,_Aw:tripUpdateMessageError,_Ax:tripHoldTimerExpired,_Ay:tripConnectionCollision,_Az:tripCease,_A_:tripNotificationErr,'tripMIBObjects':tripMIBObjects,'tripCfgTable':tripCfgTable,'tripCfgEntry':tripCfgEntry,_v:tripCfgProtocolVersion,_w:tripCfgItad,_x:tripCfgIdentifier,_z:tripCfgAdminStatus,_y:tripCfgOperStatus,_A0:tripCfgAddrIAddrType,_A1:tripCfgAddr,_A2:tripCfgPort,_A3:tripCfgMinItadOriginationInterval,_A4:tripCfgMinRouteAdvertisementInterval,_A5:tripCfgMaxPurgeTime,_A6:tripCfgDisableTime,_A7:tripCfgSendReceiveMode,_A8:tripCfgStorage,'tripRouteTypeTable':tripRouteTypeTable,'tripRouteTypeEntry':tripRouteTypeEntry,_k:tripRouteTypeAddrInetType,_l:tripRouteTypeAddr,_m:tripRouteTypePort,_n:tripRouteTypeProtocolId,_o:tripRouteTypeAddrFamilyId,_AB:tripRouteTypePeer,'tripSupportedCommunityTable':tripSupportedCommunityTable,'tripSupportedCommunityEntry':tripSupportedCommunityEntry,_p:tripSupportedCommunityId,_A9:tripSupportedCommunityItad,_AA:tripSupportedCommunityStorage,_AC:tripSupportedCommunityRowStatus,'tripPeerTable':tripPeerTable,'tripPeerEntry':tripPeerEntry,_q:tripPeerRemoteAddrInetType,_r:tripPeerRemoteAddr,_s:tripPeerRemotePort,_AD:tripPeerIdentifier,_O:tripPeerState,_AE:tripPeerAdminStatus,_AF:tripPeerNegotiatedVersion,_AG:tripPeerSendReceiveMode,_AH:tripPeerRemoteItad,_AI:tripPeerConnectRetryInterval,_AJ:tripPeerMaxRetryInterval,_AK:tripPeerHoldTime,_AL:tripPeerKeepAlive,_AM:tripPeerHoldTimeConfigured,_AN:tripPeerKeepAliveConfigured,_AO:tripPeerMaxPurgeTime,_AP:tripPeerDisableTime,_AQ:tripPeerLearned,_AR:tripPeerStorage,_AS:tripPeerRowStatus,'tripPeerStatisticsTable':tripPeerStatisticsTable,_u:tripPeerStatisticsEntry,_AT:tripPeerInUpdates,_AU:tripPeerOutUpdates,_AV:tripPeerInTotalMessages,_AW:tripPeerOutTotalMessages,_AX:tripPeerFsmEstablishedTransitions,_AY:tripPeerFsmEstablishedTime,_AZ:tripPeerInUpdateElapsedTime,_Aa:tripPeerStateChangeTime,'tripRouteTable':tripRouteTable,'tripRouteEntry':tripRouteEntry,_W:tripRouteAppProtocol,_X:tripRouteAddressFamily,_Y:tripRouteAddress,_Z:tripRoutePeer,_Ab:tripRouteTRIBMask,_Ac:tripRouteAddressSequenceNumber,_Ad:tripRouteAddressOriginatorId,_Ae:tripRouteNextHopServerIAddrType,_Af:tripRouteNextHopServer,_Ag:tripRouteNextHopServerPort,_Ah:tripRouteNextHopServerItad,_Ai:tripRouteMultiExitDisc,_Aj:tripRouteLocalPref,_Ak:tripRouteAdvertisementPath,_Al:tripRouteRoutedPath,_Am:tripRouteAtomicAggregate,_An:tripRouteUnknown,_Ao:tripRouteWithdrawn,_Ap:tripRouteConverted,_Aq:tripRouteReceivedTime,'tripRouteCommunityTable':tripRouteCommunityTable,'tripRouteCommunityEntry':tripRouteCommunityEntry,_t:tripRouteCommunityId,_Ar:tripRouteCommunityItad,'tripItadTopologyTable':tripItadTopologyTable,'tripItadTopologyEntry':tripItadTopologyEntry,_a:tripItadTopologyOrigId,_As:tripItadTopologySeqNum,'tripItadTopologyIdTable':tripItadTopologyIdTable,'tripItadTopologyIdEntry':tripItadTopologyIdEntry,_b:tripItadTopologyId,'tripMIBConformance':tripMIBConformance,'tripMIBCompliances':tripMIBCompliances,'tripMIBFullCompliance':tripMIBFullCompliance,'tripMIBReadOnlyCompliance':tripMIBReadOnlyCompliance,'tripMIBGroups':tripMIBGroups,_c:tripConfigGroup,_d:tripPeerTableConfigGroup,_g:tripPeerTableStatsGroup,_e:tripRouteGroup,_f:tripItadTopologyGroup,_h:tripNotificationGroup,_i:tripNotifObjectGroup,'tripMIBNotifObjects':tripMIBNotifObjects,_I:tripNotifApplIndex,_K:tripNotifPeerAddrInetType,_L:tripNotifPeerAddr,_P:tripNotifPeerErrCode,_Q:tripNotifPeerErrSubcode})