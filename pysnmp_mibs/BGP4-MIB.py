_AB='bgp4MIBNewNotificationGroup'
_AA='bgp4MIBNotificationGroup'
_A9='bgp4MIBPathAttrGroup'
_A8='bgp4MIBPeerGroup'
_A7='bgp4MIBGlobalsGroup'
_A6='bgpBackwardTransNotification'
_A5='bgpEstablishedNotification'
_A4='bgpBackwardTransition'
_A3='bgpEstablished'
_A2='bgp4PathAttrUnknown'
_A1='bgp4PathAttrBest'
_A0='bgp4PathAttrCalcLocalPref'
_z='bgp4PathAttrAggregatorAddr'
_y='bgp4PathAttrAggregatorAS'
_x='bgp4PathAttrAtomicAggregate'
_w='bgp4PathAttrLocalPref'
_v='bgp4PathAttrMultiExitDisc'
_u='bgp4PathAttrNextHop'
_t='bgp4PathAttrASPathSegment'
_s='bgp4PathAttrOrigin'
_r='bgpPathAttrInterASMetric'
_q='bgpPathAttrNextHop'
_p='bgpPathAttrASPath'
_o='bgpPathAttrOrigin'
_n='bgpPeerInUpdateElapsedTime'
_m='bgpPeerMinRouteAdvertisementInterval'
_l='bgpPeerMinASOriginationInterval'
_k='bgpPeerKeepAliveConfigured'
_j='bgpPeerHoldTimeConfigured'
_i='bgpPeerKeepAlive'
_h='bgpPeerHoldTime'
_g='bgpPeerConnectRetryInterval'
_f='bgpPeerFsmEstablishedTime'
_e='bgpPeerFsmEstablishedTransitions'
_d='bgpPeerOutTotalMessages'
_c='bgpPeerInTotalMessages'
_b='bgpPeerOutUpdates'
_a='bgpPeerInUpdates'
_Z='bgpPeerRemoteAs'
_Y='bgpPeerRemotePort'
_X='bgpPeerLocalPort'
_W='bgpPeerLocalAddr'
_V='bgpPeerNegotiatedVersion'
_U='bgpPeerAdminStatus'
_T='bgpPeerIdentifier'
_S='bgpIdentifier'
_R='bgpLocalAs'
_Q='bgpVersion'
_P='incomplete'
_O='bgp4PathAttrPeer'
_N='bgp4PathAttrIpAddrPrefixLen'
_M='bgp4PathAttrIpAddrPrefix'
_L='bgpPathAttrPeer'
_K='bgpPathAttrDestNetwork'
_J='bgpPeerLastError'
_I='bgpPeerState'
_H='read-write'
_G='OctetString'
_F='bgpPeerRemoteAddr'
_E='obsolete'
_D='Integer32'
_C='read-only'
_B='current'
_A='BGP4-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bgp=ModuleIdentity((1,3,6,1,2,1,15))
if mibBuilder.loadTexts:bgp.setRevisions(('2001-06-01 00:00','1994-05-05 00:00'))
_BgpNotification_ObjectIdentity=ObjectIdentity
bgpNotification=_BgpNotification_ObjectIdentity((1,3,6,1,2,1,15,0))
class _BgpVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_BgpVersion_Type.__name__=_G
_BgpVersion_Object=MibScalar
bgpVersion=_BgpVersion_Object((1,3,6,1,2,1,15,1),_BgpVersion_Type())
bgpVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpVersion.setStatus(_B)
class _BgpLocalAs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BgpLocalAs_Type.__name__=_D
_BgpLocalAs_Object=MibScalar
bgpLocalAs=_BgpLocalAs_Object((1,3,6,1,2,1,15,2),_BgpLocalAs_Type())
bgpLocalAs.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpLocalAs.setStatus(_B)
_BgpPeerTable_Object=MibTable
bgpPeerTable=_BgpPeerTable_Object((1,3,6,1,2,1,15,3))
if mibBuilder.loadTexts:bgpPeerTable.setStatus(_B)
_BgpPeerEntry_Object=MibTableRow
bgpPeerEntry=_BgpPeerEntry_Object((1,3,6,1,2,1,15,3,1))
bgpPeerEntry.setIndexNames((0,_A,_F))
if mibBuilder.loadTexts:bgpPeerEntry.setStatus(_B)
_BgpPeerIdentifier_Type=IpAddress
_BgpPeerIdentifier_Object=MibTableColumn
bgpPeerIdentifier=_BgpPeerIdentifier_Object((1,3,6,1,2,1,15,3,1,1),_BgpPeerIdentifier_Type())
bgpPeerIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerIdentifier.setStatus(_B)
class _BgpPeerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('idle',1),('connect',2),('active',3),('opensent',4),('openconfirm',5),('established',6)))
_BgpPeerState_Type.__name__=_D
_BgpPeerState_Object=MibTableColumn
bgpPeerState=_BgpPeerState_Object((1,3,6,1,2,1,15,3,1,2),_BgpPeerState_Type())
bgpPeerState.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerState.setStatus(_B)
class _BgpPeerAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stop',1),('start',2)))
_BgpPeerAdminStatus_Type.__name__=_D
_BgpPeerAdminStatus_Object=MibTableColumn
bgpPeerAdminStatus=_BgpPeerAdminStatus_Object((1,3,6,1,2,1,15,3,1,3),_BgpPeerAdminStatus_Type())
bgpPeerAdminStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:bgpPeerAdminStatus.setStatus(_B)
class _BgpPeerNegotiatedVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_BgpPeerNegotiatedVersion_Type.__name__=_D
_BgpPeerNegotiatedVersion_Object=MibTableColumn
bgpPeerNegotiatedVersion=_BgpPeerNegotiatedVersion_Object((1,3,6,1,2,1,15,3,1,4),_BgpPeerNegotiatedVersion_Type())
bgpPeerNegotiatedVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerNegotiatedVersion.setStatus(_B)
_BgpPeerLocalAddr_Type=IpAddress
_BgpPeerLocalAddr_Object=MibTableColumn
bgpPeerLocalAddr=_BgpPeerLocalAddr_Object((1,3,6,1,2,1,15,3,1,5),_BgpPeerLocalAddr_Type())
bgpPeerLocalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerLocalAddr.setStatus(_B)
class _BgpPeerLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BgpPeerLocalPort_Type.__name__=_D
_BgpPeerLocalPort_Object=MibTableColumn
bgpPeerLocalPort=_BgpPeerLocalPort_Object((1,3,6,1,2,1,15,3,1,6),_BgpPeerLocalPort_Type())
bgpPeerLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerLocalPort.setStatus(_B)
_BgpPeerRemoteAddr_Type=IpAddress
_BgpPeerRemoteAddr_Object=MibTableColumn
bgpPeerRemoteAddr=_BgpPeerRemoteAddr_Object((1,3,6,1,2,1,15,3,1,7),_BgpPeerRemoteAddr_Type())
bgpPeerRemoteAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerRemoteAddr.setStatus(_B)
class _BgpPeerRemotePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BgpPeerRemotePort_Type.__name__=_D
_BgpPeerRemotePort_Object=MibTableColumn
bgpPeerRemotePort=_BgpPeerRemotePort_Object((1,3,6,1,2,1,15,3,1,8),_BgpPeerRemotePort_Type())
bgpPeerRemotePort.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerRemotePort.setStatus(_B)
class _BgpPeerRemoteAs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BgpPeerRemoteAs_Type.__name__=_D
_BgpPeerRemoteAs_Object=MibTableColumn
bgpPeerRemoteAs=_BgpPeerRemoteAs_Object((1,3,6,1,2,1,15,3,1,9),_BgpPeerRemoteAs_Type())
bgpPeerRemoteAs.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerRemoteAs.setStatus(_B)
_BgpPeerInUpdates_Type=Counter32
_BgpPeerInUpdates_Object=MibTableColumn
bgpPeerInUpdates=_BgpPeerInUpdates_Object((1,3,6,1,2,1,15,3,1,10),_BgpPeerInUpdates_Type())
bgpPeerInUpdates.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerInUpdates.setStatus(_B)
_BgpPeerOutUpdates_Type=Counter32
_BgpPeerOutUpdates_Object=MibTableColumn
bgpPeerOutUpdates=_BgpPeerOutUpdates_Object((1,3,6,1,2,1,15,3,1,11),_BgpPeerOutUpdates_Type())
bgpPeerOutUpdates.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerOutUpdates.setStatus(_B)
_BgpPeerInTotalMessages_Type=Counter32
_BgpPeerInTotalMessages_Object=MibTableColumn
bgpPeerInTotalMessages=_BgpPeerInTotalMessages_Object((1,3,6,1,2,1,15,3,1,12),_BgpPeerInTotalMessages_Type())
bgpPeerInTotalMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerInTotalMessages.setStatus(_B)
_BgpPeerOutTotalMessages_Type=Counter32
_BgpPeerOutTotalMessages_Object=MibTableColumn
bgpPeerOutTotalMessages=_BgpPeerOutTotalMessages_Object((1,3,6,1,2,1,15,3,1,13),_BgpPeerOutTotalMessages_Type())
bgpPeerOutTotalMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerOutTotalMessages.setStatus(_B)
class _BgpPeerLastError_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_BgpPeerLastError_Type.__name__=_G
_BgpPeerLastError_Object=MibTableColumn
bgpPeerLastError=_BgpPeerLastError_Object((1,3,6,1,2,1,15,3,1,14),_BgpPeerLastError_Type())
bgpPeerLastError.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerLastError.setStatus(_B)
_BgpPeerFsmEstablishedTransitions_Type=Counter32
_BgpPeerFsmEstablishedTransitions_Object=MibTableColumn
bgpPeerFsmEstablishedTransitions=_BgpPeerFsmEstablishedTransitions_Object((1,3,6,1,2,1,15,3,1,15),_BgpPeerFsmEstablishedTransitions_Type())
bgpPeerFsmEstablishedTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerFsmEstablishedTransitions.setStatus(_B)
_BgpPeerFsmEstablishedTime_Type=Gauge32
_BgpPeerFsmEstablishedTime_Object=MibTableColumn
bgpPeerFsmEstablishedTime=_BgpPeerFsmEstablishedTime_Object((1,3,6,1,2,1,15,3,1,16),_BgpPeerFsmEstablishedTime_Type())
bgpPeerFsmEstablishedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerFsmEstablishedTime.setStatus(_B)
class _BgpPeerConnectRetryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BgpPeerConnectRetryInterval_Type.__name__=_D
_BgpPeerConnectRetryInterval_Object=MibTableColumn
bgpPeerConnectRetryInterval=_BgpPeerConnectRetryInterval_Object((1,3,6,1,2,1,15,3,1,17),_BgpPeerConnectRetryInterval_Type())
bgpPeerConnectRetryInterval.setMaxAccess(_H)
if mibBuilder.loadTexts:bgpPeerConnectRetryInterval.setStatus(_B)
class _BgpPeerHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_BgpPeerHoldTime_Type.__name__=_D
_BgpPeerHoldTime_Object=MibTableColumn
bgpPeerHoldTime=_BgpPeerHoldTime_Object((1,3,6,1,2,1,15,3,1,18),_BgpPeerHoldTime_Type())
bgpPeerHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerHoldTime.setStatus(_B)
class _BgpPeerKeepAlive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_BgpPeerKeepAlive_Type.__name__=_D
_BgpPeerKeepAlive_Object=MibTableColumn
bgpPeerKeepAlive=_BgpPeerKeepAlive_Object((1,3,6,1,2,1,15,3,1,19),_BgpPeerKeepAlive_Type())
bgpPeerKeepAlive.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerKeepAlive.setStatus(_B)
class _BgpPeerHoldTimeConfigured_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_BgpPeerHoldTimeConfigured_Type.__name__=_D
_BgpPeerHoldTimeConfigured_Object=MibTableColumn
bgpPeerHoldTimeConfigured=_BgpPeerHoldTimeConfigured_Object((1,3,6,1,2,1,15,3,1,20),_BgpPeerHoldTimeConfigured_Type())
bgpPeerHoldTimeConfigured.setMaxAccess(_H)
if mibBuilder.loadTexts:bgpPeerHoldTimeConfigured.setStatus(_B)
class _BgpPeerKeepAliveConfigured_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_BgpPeerKeepAliveConfigured_Type.__name__=_D
_BgpPeerKeepAliveConfigured_Object=MibTableColumn
bgpPeerKeepAliveConfigured=_BgpPeerKeepAliveConfigured_Object((1,3,6,1,2,1,15,3,1,21),_BgpPeerKeepAliveConfigured_Type())
bgpPeerKeepAliveConfigured.setMaxAccess(_H)
if mibBuilder.loadTexts:bgpPeerKeepAliveConfigured.setStatus(_B)
class _BgpPeerMinASOriginationInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BgpPeerMinASOriginationInterval_Type.__name__=_D
_BgpPeerMinASOriginationInterval_Object=MibTableColumn
bgpPeerMinASOriginationInterval=_BgpPeerMinASOriginationInterval_Object((1,3,6,1,2,1,15,3,1,22),_BgpPeerMinASOriginationInterval_Type())
bgpPeerMinASOriginationInterval.setMaxAccess(_H)
if mibBuilder.loadTexts:bgpPeerMinASOriginationInterval.setStatus(_B)
class _BgpPeerMinRouteAdvertisementInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BgpPeerMinRouteAdvertisementInterval_Type.__name__=_D
_BgpPeerMinRouteAdvertisementInterval_Object=MibTableColumn
bgpPeerMinRouteAdvertisementInterval=_BgpPeerMinRouteAdvertisementInterval_Object((1,3,6,1,2,1,15,3,1,23),_BgpPeerMinRouteAdvertisementInterval_Type())
bgpPeerMinRouteAdvertisementInterval.setMaxAccess(_H)
if mibBuilder.loadTexts:bgpPeerMinRouteAdvertisementInterval.setStatus(_B)
_BgpPeerInUpdateElapsedTime_Type=Gauge32
_BgpPeerInUpdateElapsedTime_Object=MibTableColumn
bgpPeerInUpdateElapsedTime=_BgpPeerInUpdateElapsedTime_Object((1,3,6,1,2,1,15,3,1,24),_BgpPeerInUpdateElapsedTime_Type())
bgpPeerInUpdateElapsedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPeerInUpdateElapsedTime.setStatus(_B)
_BgpIdentifier_Type=IpAddress
_BgpIdentifier_Object=MibScalar
bgpIdentifier=_BgpIdentifier_Object((1,3,6,1,2,1,15,4),_BgpIdentifier_Type())
bgpIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpIdentifier.setStatus(_B)
_BgpRcvdPathAttrTable_Object=MibTable
bgpRcvdPathAttrTable=_BgpRcvdPathAttrTable_Object((1,3,6,1,2,1,15,5))
if mibBuilder.loadTexts:bgpRcvdPathAttrTable.setStatus(_E)
_BgpPathAttrEntry_Object=MibTableRow
bgpPathAttrEntry=_BgpPathAttrEntry_Object((1,3,6,1,2,1,15,5,1))
bgpPathAttrEntry.setIndexNames((0,_A,_K),(0,_A,_L))
if mibBuilder.loadTexts:bgpPathAttrEntry.setStatus(_E)
_BgpPathAttrPeer_Type=IpAddress
_BgpPathAttrPeer_Object=MibTableColumn
bgpPathAttrPeer=_BgpPathAttrPeer_Object((1,3,6,1,2,1,15,5,1,1),_BgpPathAttrPeer_Type())
bgpPathAttrPeer.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPathAttrPeer.setStatus(_E)
_BgpPathAttrDestNetwork_Type=IpAddress
_BgpPathAttrDestNetwork_Object=MibTableColumn
bgpPathAttrDestNetwork=_BgpPathAttrDestNetwork_Object((1,3,6,1,2,1,15,5,1,2),_BgpPathAttrDestNetwork_Type())
bgpPathAttrDestNetwork.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPathAttrDestNetwork.setStatus(_E)
class _BgpPathAttrOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('igp',1),('egp',2),(_P,3)))
_BgpPathAttrOrigin_Type.__name__=_D
_BgpPathAttrOrigin_Object=MibTableColumn
bgpPathAttrOrigin=_BgpPathAttrOrigin_Object((1,3,6,1,2,1,15,5,1,3),_BgpPathAttrOrigin_Type())
bgpPathAttrOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPathAttrOrigin.setStatus(_E)
class _BgpPathAttrASPath_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,255))
_BgpPathAttrASPath_Type.__name__=_G
_BgpPathAttrASPath_Object=MibTableColumn
bgpPathAttrASPath=_BgpPathAttrASPath_Object((1,3,6,1,2,1,15,5,1,4),_BgpPathAttrASPath_Type())
bgpPathAttrASPath.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPathAttrASPath.setStatus(_E)
_BgpPathAttrNextHop_Type=IpAddress
_BgpPathAttrNextHop_Object=MibTableColumn
bgpPathAttrNextHop=_BgpPathAttrNextHop_Object((1,3,6,1,2,1,15,5,1,5),_BgpPathAttrNextHop_Type())
bgpPathAttrNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPathAttrNextHop.setStatus(_E)
_BgpPathAttrInterASMetric_Type=Integer32
_BgpPathAttrInterASMetric_Object=MibTableColumn
bgpPathAttrInterASMetric=_BgpPathAttrInterASMetric_Object((1,3,6,1,2,1,15,5,1,6),_BgpPathAttrInterASMetric_Type())
bgpPathAttrInterASMetric.setMaxAccess(_C)
if mibBuilder.loadTexts:bgpPathAttrInterASMetric.setStatus(_E)
_Bgp4PathAttrTable_Object=MibTable
bgp4PathAttrTable=_Bgp4PathAttrTable_Object((1,3,6,1,2,1,15,6))
if mibBuilder.loadTexts:bgp4PathAttrTable.setStatus(_B)
_Bgp4PathAttrEntry_Object=MibTableRow
bgp4PathAttrEntry=_Bgp4PathAttrEntry_Object((1,3,6,1,2,1,15,6,1))
bgp4PathAttrEntry.setIndexNames((0,_A,_M),(0,_A,_N),(0,_A,_O))
if mibBuilder.loadTexts:bgp4PathAttrEntry.setStatus(_B)
_Bgp4PathAttrPeer_Type=IpAddress
_Bgp4PathAttrPeer_Object=MibTableColumn
bgp4PathAttrPeer=_Bgp4PathAttrPeer_Object((1,3,6,1,2,1,15,6,1,1),_Bgp4PathAttrPeer_Type())
bgp4PathAttrPeer.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4PathAttrPeer.setStatus(_B)
class _Bgp4PathAttrIpAddrPrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_Bgp4PathAttrIpAddrPrefixLen_Type.__name__=_D
_Bgp4PathAttrIpAddrPrefixLen_Object=MibTableColumn
bgp4PathAttrIpAddrPrefixLen=_Bgp4PathAttrIpAddrPrefixLen_Object((1,3,6,1,2,1,15,6,1,2),_Bgp4PathAttrIpAddrPrefixLen_Type())
bgp4PathAttrIpAddrPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4PathAttrIpAddrPrefixLen.setStatus(_B)
_Bgp4PathAttrIpAddrPrefix_Type=IpAddress
_Bgp4PathAttrIpAddrPrefix_Object=MibTableColumn
bgp4PathAttrIpAddrPrefix=_Bgp4PathAttrIpAddrPrefix_Object((1,3,6,1,2,1,15,6,1,3),_Bgp4PathAttrIpAddrPrefix_Type())
bgp4PathAttrIpAddrPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4PathAttrIpAddrPrefix.setStatus(_B)
class _Bgp4PathAttrOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('igp',1),('egp',2),(_P,3)))
_Bgp4PathAttrOrigin_Type.__name__=_D
_Bgp4PathAttrOrigin_Object=MibTableColumn
bgp4PathAttrOrigin=_Bgp4PathAttrOrigin_Object((1,3,6,1,2,1,15,6,1,4),_Bgp4PathAttrOrigin_Type())
bgp4PathAttrOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4PathAttrOrigin.setStatus(_B)
class _Bgp4PathAttrASPathSegment_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,255))
_Bgp4PathAttrASPathSegment_Type.__name__=_G
_Bgp4PathAttrASPathSegment_Object=MibTableColumn
bgp4PathAttrASPathSegment=_Bgp4PathAttrASPathSegment_Object((1,3,6,1,2,1,15,6,1,5),_Bgp4PathAttrASPathSegment_Type())
bgp4PathAttrASPathSegment.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4PathAttrASPathSegment.setStatus(_B)
_Bgp4PathAttrNextHop_Type=IpAddress
_Bgp4PathAttrNextHop_Object=MibTableColumn
bgp4PathAttrNextHop=_Bgp4PathAttrNextHop_Object((1,3,6,1,2,1,15,6,1,6),_Bgp4PathAttrNextHop_Type())
bgp4PathAttrNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4PathAttrNextHop.setStatus(_B)
class _Bgp4PathAttrMultiExitDisc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_Bgp4PathAttrMultiExitDisc_Type.__name__=_D
_Bgp4PathAttrMultiExitDisc_Object=MibTableColumn
bgp4PathAttrMultiExitDisc=_Bgp4PathAttrMultiExitDisc_Object((1,3,6,1,2,1,15,6,1,7),_Bgp4PathAttrMultiExitDisc_Type())
bgp4PathAttrMultiExitDisc.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4PathAttrMultiExitDisc.setStatus(_B)
class _Bgp4PathAttrLocalPref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_Bgp4PathAttrLocalPref_Type.__name__=_D
_Bgp4PathAttrLocalPref_Object=MibTableColumn
bgp4PathAttrLocalPref=_Bgp4PathAttrLocalPref_Object((1,3,6,1,2,1,15,6,1,8),_Bgp4PathAttrLocalPref_Type())
bgp4PathAttrLocalPref.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4PathAttrLocalPref.setStatus(_B)
class _Bgp4PathAttrAtomicAggregate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lessSpecificRouteNotSelected',1),('lessSpecificRouteSelected',2)))
_Bgp4PathAttrAtomicAggregate_Type.__name__=_D
_Bgp4PathAttrAtomicAggregate_Object=MibTableColumn
bgp4PathAttrAtomicAggregate=_Bgp4PathAttrAtomicAggregate_Object((1,3,6,1,2,1,15,6,1,9),_Bgp4PathAttrAtomicAggregate_Type())
bgp4PathAttrAtomicAggregate.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4PathAttrAtomicAggregate.setStatus(_B)
class _Bgp4PathAttrAggregatorAS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Bgp4PathAttrAggregatorAS_Type.__name__=_D
_Bgp4PathAttrAggregatorAS_Object=MibTableColumn
bgp4PathAttrAggregatorAS=_Bgp4PathAttrAggregatorAS_Object((1,3,6,1,2,1,15,6,1,10),_Bgp4PathAttrAggregatorAS_Type())
bgp4PathAttrAggregatorAS.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4PathAttrAggregatorAS.setStatus(_B)
_Bgp4PathAttrAggregatorAddr_Type=IpAddress
_Bgp4PathAttrAggregatorAddr_Object=MibTableColumn
bgp4PathAttrAggregatorAddr=_Bgp4PathAttrAggregatorAddr_Object((1,3,6,1,2,1,15,6,1,11),_Bgp4PathAttrAggregatorAddr_Type())
bgp4PathAttrAggregatorAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4PathAttrAggregatorAddr.setStatus(_B)
class _Bgp4PathAttrCalcLocalPref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_Bgp4PathAttrCalcLocalPref_Type.__name__=_D
_Bgp4PathAttrCalcLocalPref_Object=MibTableColumn
bgp4PathAttrCalcLocalPref=_Bgp4PathAttrCalcLocalPref_Object((1,3,6,1,2,1,15,6,1,12),_Bgp4PathAttrCalcLocalPref_Type())
bgp4PathAttrCalcLocalPref.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4PathAttrCalcLocalPref.setStatus(_B)
class _Bgp4PathAttrBest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('false',1),('true',2)))
_Bgp4PathAttrBest_Type.__name__=_D
_Bgp4PathAttrBest_Object=MibTableColumn
bgp4PathAttrBest=_Bgp4PathAttrBest_Object((1,3,6,1,2,1,15,6,1,13),_Bgp4PathAttrBest_Type())
bgp4PathAttrBest.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4PathAttrBest.setStatus(_B)
class _Bgp4PathAttrUnknown_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Bgp4PathAttrUnknown_Type.__name__=_G
_Bgp4PathAttrUnknown_Object=MibTableColumn
bgp4PathAttrUnknown=_Bgp4PathAttrUnknown_Object((1,3,6,1,2,1,15,6,1,14),_Bgp4PathAttrUnknown_Type())
bgp4PathAttrUnknown.setMaxAccess(_C)
if mibBuilder.loadTexts:bgp4PathAttrUnknown.setStatus(_B)
_BgpTraps_ObjectIdentity=ObjectIdentity
bgpTraps=_BgpTraps_ObjectIdentity((1,3,6,1,2,1,15,7))
_BgpMIBConformance_ObjectIdentity=ObjectIdentity
bgpMIBConformance=_BgpMIBConformance_ObjectIdentity((1,3,6,1,2,1,15,8))
_BgpMIBCompliances_ObjectIdentity=ObjectIdentity
bgpMIBCompliances=_BgpMIBCompliances_ObjectIdentity((1,3,6,1,2,1,15,8,1))
_BgpMIBGroups_ObjectIdentity=ObjectIdentity
bgpMIBGroups=_BgpMIBGroups_ObjectIdentity((1,3,6,1,2,1,15,8,2))
bgp4MIBGlobalsGroup=ObjectGroup((1,3,6,1,2,1,15,8,2,1))
bgp4MIBGlobalsGroup.setObjects(*((_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:bgp4MIBGlobalsGroup.setStatus(_B)
bgp4MIBPeerGroup=ObjectGroup((1,3,6,1,2,1,15,8,2,2))
bgp4MIBPeerGroup.setObjects(*((_A,_T),(_A,_I),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_F),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_J),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:bgp4MIBPeerGroup.setStatus(_B)
bgp4MIBRcvdPathAttrGroup=ObjectGroup((1,3,6,1,2,1,15,8,2,3))
bgp4MIBRcvdPathAttrGroup.setObjects(*((_A,_L),(_A,_K),(_A,_o),(_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:bgp4MIBRcvdPathAttrGroup.setStatus(_E)
bgp4MIBPathAttrGroup=ObjectGroup((1,3,6,1,2,1,15,8,2,4))
bgp4MIBPathAttrGroup.setObjects(*((_A,_O),(_A,_N),(_A,_M),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:bgp4MIBPathAttrGroup.setStatus(_B)
bgpEstablishedNotification=NotificationType((1,3,6,1,2,1,15,0,1))
bgpEstablishedNotification.setObjects(*((_A,_F),(_A,_J),(_A,_I)))
if mibBuilder.loadTexts:bgpEstablishedNotification.setStatus(_B)
bgpBackwardTransNotification=NotificationType((1,3,6,1,2,1,15,0,2))
bgpBackwardTransNotification.setObjects(*((_A,_F),(_A,_J),(_A,_I)))
if mibBuilder.loadTexts:bgpBackwardTransNotification.setStatus(_B)
bgpEstablished=NotificationType((1,3,6,1,2,1,15,7,1))
bgpEstablished.setObjects(*((_A,_F),(_A,_J),(_A,_I)))
if mibBuilder.loadTexts:bgpEstablished.setStatus(_E)
bgpBackwardTransition=NotificationType((1,3,6,1,2,1,15,7,2))
bgpBackwardTransition.setObjects(*((_A,_F),(_A,_J),(_A,_I)))
if mibBuilder.loadTexts:bgpBackwardTransition.setStatus(_E)
bgp4MIBNotificationGroup=NotificationGroup((1,3,6,1,2,1,15,8,2,5))
bgp4MIBNotificationGroup.setObjects(*((_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:bgp4MIBNotificationGroup.setStatus(_E)
bgp4MIBNewNotificationGroup=NotificationGroup((1,3,6,1,2,1,15,8,2,6))
bgp4MIBNewNotificationGroup.setObjects(*((_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:bgp4MIBNewNotificationGroup.setStatus(_B)
bgpMIBCompliance=ModuleCompliance((1,3,6,1,2,1,15,8,1,1))
bgpMIBCompliance.setObjects(*((_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:bgpMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'bgp':bgp,'bgpNotification':bgpNotification,_A5:bgpEstablishedNotification,_A6:bgpBackwardTransNotification,_Q:bgpVersion,_R:bgpLocalAs,'bgpPeerTable':bgpPeerTable,'bgpPeerEntry':bgpPeerEntry,_T:bgpPeerIdentifier,_I:bgpPeerState,_U:bgpPeerAdminStatus,_V:bgpPeerNegotiatedVersion,_W:bgpPeerLocalAddr,_X:bgpPeerLocalPort,_F:bgpPeerRemoteAddr,_Y:bgpPeerRemotePort,_Z:bgpPeerRemoteAs,_a:bgpPeerInUpdates,_b:bgpPeerOutUpdates,_c:bgpPeerInTotalMessages,_d:bgpPeerOutTotalMessages,_J:bgpPeerLastError,_e:bgpPeerFsmEstablishedTransitions,_f:bgpPeerFsmEstablishedTime,_g:bgpPeerConnectRetryInterval,_h:bgpPeerHoldTime,_i:bgpPeerKeepAlive,_j:bgpPeerHoldTimeConfigured,_k:bgpPeerKeepAliveConfigured,_l:bgpPeerMinASOriginationInterval,_m:bgpPeerMinRouteAdvertisementInterval,_n:bgpPeerInUpdateElapsedTime,_S:bgpIdentifier,'bgpRcvdPathAttrTable':bgpRcvdPathAttrTable,'bgpPathAttrEntry':bgpPathAttrEntry,_L:bgpPathAttrPeer,_K:bgpPathAttrDestNetwork,_o:bgpPathAttrOrigin,_p:bgpPathAttrASPath,_q:bgpPathAttrNextHop,_r:bgpPathAttrInterASMetric,'bgp4PathAttrTable':bgp4PathAttrTable,'bgp4PathAttrEntry':bgp4PathAttrEntry,_O:bgp4PathAttrPeer,_N:bgp4PathAttrIpAddrPrefixLen,_M:bgp4PathAttrIpAddrPrefix,_s:bgp4PathAttrOrigin,_t:bgp4PathAttrASPathSegment,_u:bgp4PathAttrNextHop,_v:bgp4PathAttrMultiExitDisc,_w:bgp4PathAttrLocalPref,_x:bgp4PathAttrAtomicAggregate,_y:bgp4PathAttrAggregatorAS,_z:bgp4PathAttrAggregatorAddr,_A0:bgp4PathAttrCalcLocalPref,_A1:bgp4PathAttrBest,_A2:bgp4PathAttrUnknown,'bgpTraps':bgpTraps,_A3:bgpEstablished,_A4:bgpBackwardTransition,'bgpMIBConformance':bgpMIBConformance,'bgpMIBCompliances':bgpMIBCompliances,'bgpMIBCompliance':bgpMIBCompliance,'bgpMIBGroups':bgpMIBGroups,_A7:bgp4MIBGlobalsGroup,_A8:bgp4MIBPeerGroup,'bgp4MIBRcvdPathAttrGroup':bgp4MIBRcvdPathAttrGroup,_A9:bgp4MIBPathAttrGroup,_AA:bgp4MIBNotificationGroup,_AB:bgp4MIBNewNotificationGroup})