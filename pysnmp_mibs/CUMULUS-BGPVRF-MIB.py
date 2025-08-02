_N='bgp4PathAttrPeer'
_M='bgp4PathAttrIpAddrPrefixLen'
_L='bgp4PathAttrIpAddrPrefix'
_K='bgpPeerIfindex'
_J='bgpPeerIdType'
_I='bgpVrfTable'
_H='bgpPeerState'
_G='bgpPeerLastError'
_F='read-write'
_E='OctetString'
_D='CUMULUS-BGPVRF-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cumulusMib,=mibBuilder.importSymbols('CUMULUS-SNMP-MIB','cumulusMib')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
InetAddress,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressIPv6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
bgp=ModuleIdentity((1,3,6,1,4,1,40310,7))
if mibBuilder.loadTexts:bgp.setRevisions(('2020-10-12 00:00',))
class _BgpVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_BgpVersion_Type.__name__=_E
_BgpVersion_Object=MibScalar
bgpVersion=_BgpVersion_Object((1,3,6,1,4,1,40310,7,1),_BgpVersion_Type())
bgpVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpVersion.setStatus(_A)
class _BgpLocalAs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BgpLocalAs_Type.__name__=_C
_BgpLocalAs_Object=MibScalar
bgpLocalAs=_BgpLocalAs_Object((1,3,6,1,4,1,40310,7,2),_BgpLocalAs_Type())
bgpLocalAs.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpLocalAs.setStatus(_A)
_BgpOuterTable_ObjectIdentity=ObjectIdentity
bgpOuterTable=_BgpOuterTable_ObjectIdentity((1,3,6,1,4,1,40310,7,3))
_BgpPeerTable_Object=MibTable
bgpPeerTable=_BgpPeerTable_Object((1,3,6,1,4,1,40310,7,3,1))
if mibBuilder.loadTexts:bgpPeerTable.setStatus(_A)
_BgpPeerEntry_Object=MibTableRow
bgpPeerEntry=_BgpPeerEntry_Object((1,3,6,1,4,1,40310,7,3,1,1))
bgpPeerEntry.setIndexNames((0,_D,_I),(0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:bgpPeerEntry.setStatus(_A)
_BgpPeerIdentifier_Type=IpAddress
_BgpPeerIdentifier_Object=MibTableColumn
bgpPeerIdentifier=_BgpPeerIdentifier_Object((1,3,6,1,4,1,40310,7,3,1,1,1),_BgpPeerIdentifier_Type())
bgpPeerIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpPeerIdentifier.setStatus(_A)
class _BgpPeerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('idle',1),('connect',2),('active',3),('opensent',4),('openconfirm',5),('established',6)))
_BgpPeerState_Type.__name__=_C
_BgpPeerState_Object=MibTableColumn
bgpPeerState=_BgpPeerState_Object((1,3,6,1,4,1,40310,7,3,1,1,2),_BgpPeerState_Type())
bgpPeerState.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpPeerState.setStatus(_A)
class _BgpPeerAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stop',1),('start',2)))
_BgpPeerAdminStatus_Type.__name__=_C
_BgpPeerAdminStatus_Object=MibTableColumn
bgpPeerAdminStatus=_BgpPeerAdminStatus_Object((1,3,6,1,4,1,40310,7,3,1,1,3),_BgpPeerAdminStatus_Type())
bgpPeerAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpPeerAdminStatus.setStatus(_A)
_BgpPeerNegotiatedVersion_Type=Integer32
_BgpPeerNegotiatedVersion_Object=MibTableColumn
bgpPeerNegotiatedVersion=_BgpPeerNegotiatedVersion_Object((1,3,6,1,4,1,40310,7,3,1,1,4),_BgpPeerNegotiatedVersion_Type())
bgpPeerNegotiatedVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpPeerNegotiatedVersion.setStatus(_A)
_BgpPeerLocalAddr_Type=InetAddress
_BgpPeerLocalAddr_Object=MibTableColumn
bgpPeerLocalAddr=_BgpPeerLocalAddr_Object((1,3,6,1,4,1,40310,7,3,1,1,5),_BgpPeerLocalAddr_Type())
bgpPeerLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpPeerLocalAddr.setStatus(_A)
class _BgpPeerLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BgpPeerLocalPort_Type.__name__=_C
_BgpPeerLocalPort_Object=MibTableColumn
bgpPeerLocalPort=_BgpPeerLocalPort_Object((1,3,6,1,4,1,40310,7,3,1,1,6),_BgpPeerLocalPort_Type())
bgpPeerLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpPeerLocalPort.setStatus(_A)
_BgpPeerRemoteAddr_Type=InetAddress
_BgpPeerRemoteAddr_Object=MibTableColumn
bgpPeerRemoteAddr=_BgpPeerRemoteAddr_Object((1,3,6,1,4,1,40310,7,3,1,1,7),_BgpPeerRemoteAddr_Type())
bgpPeerRemoteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpPeerRemoteAddr.setStatus(_A)
class _BgpPeerRemotePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BgpPeerRemotePort_Type.__name__=_C
_BgpPeerRemotePort_Object=MibTableColumn
bgpPeerRemotePort=_BgpPeerRemotePort_Object((1,3,6,1,4,1,40310,7,3,1,1,8),_BgpPeerRemotePort_Type())
bgpPeerRemotePort.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpPeerRemotePort.setStatus(_A)
class _BgpPeerRemoteAs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BgpPeerRemoteAs_Type.__name__=_C
_BgpPeerRemoteAs_Object=MibTableColumn
bgpPeerRemoteAs=_BgpPeerRemoteAs_Object((1,3,6,1,4,1,40310,7,3,1,1,9),_BgpPeerRemoteAs_Type())
bgpPeerRemoteAs.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpPeerRemoteAs.setStatus(_A)
_BgpPeerInUpdates_Type=Counter32
_BgpPeerInUpdates_Object=MibTableColumn
bgpPeerInUpdates=_BgpPeerInUpdates_Object((1,3,6,1,4,1,40310,7,3,1,1,10),_BgpPeerInUpdates_Type())
bgpPeerInUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpPeerInUpdates.setStatus(_A)
_BgpPeerOutUpdates_Type=Counter32
_BgpPeerOutUpdates_Object=MibTableColumn
bgpPeerOutUpdates=_BgpPeerOutUpdates_Object((1,3,6,1,4,1,40310,7,3,1,1,11),_BgpPeerOutUpdates_Type())
bgpPeerOutUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpPeerOutUpdates.setStatus(_A)
_BgpPeerInTotalMessages_Type=Counter32
_BgpPeerInTotalMessages_Object=MibTableColumn
bgpPeerInTotalMessages=_BgpPeerInTotalMessages_Object((1,3,6,1,4,1,40310,7,3,1,1,12),_BgpPeerInTotalMessages_Type())
bgpPeerInTotalMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpPeerInTotalMessages.setStatus(_A)
_BgpPeerOutTotalMessages_Type=Counter32
_BgpPeerOutTotalMessages_Object=MibTableColumn
bgpPeerOutTotalMessages=_BgpPeerOutTotalMessages_Object((1,3,6,1,4,1,40310,7,3,1,1,13),_BgpPeerOutTotalMessages_Type())
bgpPeerOutTotalMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpPeerOutTotalMessages.setStatus(_A)
class _BgpPeerLastError_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_BgpPeerLastError_Type.__name__=_E
_BgpPeerLastError_Object=MibTableColumn
bgpPeerLastError=_BgpPeerLastError_Object((1,3,6,1,4,1,40310,7,3,1,1,14),_BgpPeerLastError_Type())
bgpPeerLastError.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpPeerLastError.setStatus(_A)
_BgpPeerFsmEstablishedTransitions_Type=Counter32
_BgpPeerFsmEstablishedTransitions_Object=MibTableColumn
bgpPeerFsmEstablishedTransitions=_BgpPeerFsmEstablishedTransitions_Object((1,3,6,1,4,1,40310,7,3,1,1,15),_BgpPeerFsmEstablishedTransitions_Type())
bgpPeerFsmEstablishedTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpPeerFsmEstablishedTransitions.setStatus(_A)
_BgpPeerFsmEstablishedTime_Type=Gauge32
_BgpPeerFsmEstablishedTime_Object=MibTableColumn
bgpPeerFsmEstablishedTime=_BgpPeerFsmEstablishedTime_Object((1,3,6,1,4,1,40310,7,3,1,1,16),_BgpPeerFsmEstablishedTime_Type())
bgpPeerFsmEstablishedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpPeerFsmEstablishedTime.setStatus(_A)
class _BgpPeerConnectRetryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BgpPeerConnectRetryInterval_Type.__name__=_C
_BgpPeerConnectRetryInterval_Object=MibTableColumn
bgpPeerConnectRetryInterval=_BgpPeerConnectRetryInterval_Object((1,3,6,1,4,1,40310,7,3,1,1,17),_BgpPeerConnectRetryInterval_Type())
bgpPeerConnectRetryInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:bgpPeerConnectRetryInterval.setStatus(_A)
class _BgpPeerHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_BgpPeerHoldTime_Type.__name__=_C
_BgpPeerHoldTime_Object=MibTableColumn
bgpPeerHoldTime=_BgpPeerHoldTime_Object((1,3,6,1,4,1,40310,7,3,1,1,18),_BgpPeerHoldTime_Type())
bgpPeerHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpPeerHoldTime.setStatus(_A)
class _BgpPeerKeepAlive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_BgpPeerKeepAlive_Type.__name__=_C
_BgpPeerKeepAlive_Object=MibTableColumn
bgpPeerKeepAlive=_BgpPeerKeepAlive_Object((1,3,6,1,4,1,40310,7,3,1,1,19),_BgpPeerKeepAlive_Type())
bgpPeerKeepAlive.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpPeerKeepAlive.setStatus(_A)
class _BgpPeerHoldTimeConfigured_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_BgpPeerHoldTimeConfigured_Type.__name__=_C
_BgpPeerHoldTimeConfigured_Object=MibTableColumn
bgpPeerHoldTimeConfigured=_BgpPeerHoldTimeConfigured_Object((1,3,6,1,4,1,40310,7,3,1,1,20),_BgpPeerHoldTimeConfigured_Type())
bgpPeerHoldTimeConfigured.setMaxAccess(_F)
if mibBuilder.loadTexts:bgpPeerHoldTimeConfigured.setStatus(_A)
class _BgpPeerKeepAliveConfigured_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_BgpPeerKeepAliveConfigured_Type.__name__=_C
_BgpPeerKeepAliveConfigured_Object=MibTableColumn
bgpPeerKeepAliveConfigured=_BgpPeerKeepAliveConfigured_Object((1,3,6,1,4,1,40310,7,3,1,1,21),_BgpPeerKeepAliveConfigured_Type())
bgpPeerKeepAliveConfigured.setMaxAccess(_F)
if mibBuilder.loadTexts:bgpPeerKeepAliveConfigured.setStatus(_A)
class _BgpPeerMinRouteAdvertisementInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BgpPeerMinRouteAdvertisementInterval_Type.__name__=_C
_BgpPeerMinRouteAdvertisementInterval_Object=MibTableColumn
bgpPeerMinRouteAdvertisementInterval=_BgpPeerMinRouteAdvertisementInterval_Object((1,3,6,1,4,1,40310,7,3,1,1,23),_BgpPeerMinRouteAdvertisementInterval_Type())
bgpPeerMinRouteAdvertisementInterval.setMaxAccess(_F)
if mibBuilder.loadTexts:bgpPeerMinRouteAdvertisementInterval.setStatus(_A)
_BgpPeerInUpdateElapsedTime_Type=Gauge32
_BgpPeerInUpdateElapsedTime_Object=MibTableColumn
bgpPeerInUpdateElapsedTime=_BgpPeerInUpdateElapsedTime_Object((1,3,6,1,4,1,40310,7,3,1,1,24),_BgpPeerInUpdateElapsedTime_Type())
bgpPeerInUpdateElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpPeerInUpdateElapsedTime.setStatus(_A)
_BgpPeerIface_Type=DisplayString
_BgpPeerIface_Object=MibTableColumn
bgpPeerIface=_BgpPeerIface_Object((1,3,6,1,4,1,40310,7,3,1,1,25),_BgpPeerIface_Type())
bgpPeerIface.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpPeerIface.setStatus(_A)
_BgpPeerDesc_Type=DisplayString
_BgpPeerDesc_Object=MibTableColumn
bgpPeerDesc=_BgpPeerDesc_Object((1,3,6,1,4,1,40310,7,3,1,1,26),_BgpPeerDesc_Type())
bgpPeerDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpPeerDesc.setStatus(_A)
_BgpPeerIfindex_Type=Integer32
_BgpPeerIfindex_Object=MibTableColumn
bgpPeerIfindex=_BgpPeerIfindex_Object((1,3,6,1,4,1,40310,7,3,1,1,27),_BgpPeerIfindex_Type())
bgpPeerIfindex.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpPeerIfindex.setStatus(_A)
class _BgpPeerIdType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('interface',0),('ipv4',1),('ipv6',2)))
_BgpPeerIdType_Type.__name__=_C
_BgpPeerIdType_Object=MibTableColumn
bgpPeerIdType=_BgpPeerIdType_Object((1,3,6,1,4,1,40310,7,3,1,1,28),_BgpPeerIdType_Type())
bgpPeerIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpPeerIdType.setStatus(_A)
_BgpIdentifier_Type=IpAddress
_BgpIdentifier_Object=MibScalar
bgpIdentifier=_BgpIdentifier_Object((1,3,6,1,4,1,40310,7,4),_BgpIdentifier_Type())
bgpIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpIdentifier.setStatus(_A)
_Bgp4PathAttrTable_Object=MibTable
bgp4PathAttrTable=_Bgp4PathAttrTable_Object((1,3,6,1,4,1,40310,7,5))
if mibBuilder.loadTexts:bgp4PathAttrTable.setStatus(_A)
_Bgp4PathAttrEntry_Object=MibTableRow
bgp4PathAttrEntry=_Bgp4PathAttrEntry_Object((1,3,6,1,4,1,40310,7,5,1))
bgp4PathAttrEntry.setIndexNames((0,_D,_L),(0,_D,_M),(0,_D,_N))
if mibBuilder.loadTexts:bgp4PathAttrEntry.setStatus(_A)
_Bgp4PathAttrPeer_Type=InetAddress
_Bgp4PathAttrPeer_Object=MibTableColumn
bgp4PathAttrPeer=_Bgp4PathAttrPeer_Object((1,3,6,1,4,1,40310,7,5,1,1),_Bgp4PathAttrPeer_Type())
bgp4PathAttrPeer.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4PathAttrPeer.setStatus(_A)
class _Bgp4PathAttrIpAddrPrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_Bgp4PathAttrIpAddrPrefixLen_Type.__name__=_C
_Bgp4PathAttrIpAddrPrefixLen_Object=MibTableColumn
bgp4PathAttrIpAddrPrefixLen=_Bgp4PathAttrIpAddrPrefixLen_Object((1,3,6,1,4,1,40310,7,5,1,2),_Bgp4PathAttrIpAddrPrefixLen_Type())
bgp4PathAttrIpAddrPrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4PathAttrIpAddrPrefixLen.setStatus(_A)
_Bgp4PathAttrIpAddrPrefix_Type=IpAddress
_Bgp4PathAttrIpAddrPrefix_Object=MibTableColumn
bgp4PathAttrIpAddrPrefix=_Bgp4PathAttrIpAddrPrefix_Object((1,3,6,1,4,1,40310,7,5,1,3),_Bgp4PathAttrIpAddrPrefix_Type())
bgp4PathAttrIpAddrPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4PathAttrIpAddrPrefix.setStatus(_A)
class _Bgp4PathAttrOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('igp',1),('egp',2),('incomplete',3)))
_Bgp4PathAttrOrigin_Type.__name__=_C
_Bgp4PathAttrOrigin_Object=MibTableColumn
bgp4PathAttrOrigin=_Bgp4PathAttrOrigin_Object((1,3,6,1,4,1,40310,7,5,1,4),_Bgp4PathAttrOrigin_Type())
bgp4PathAttrOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4PathAttrOrigin.setStatus(_A)
class _Bgp4PathAttrASPathSegment_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,255))
_Bgp4PathAttrASPathSegment_Type.__name__=_E
_Bgp4PathAttrASPathSegment_Object=MibTableColumn
bgp4PathAttrASPathSegment=_Bgp4PathAttrASPathSegment_Object((1,3,6,1,4,1,40310,7,5,1,5),_Bgp4PathAttrASPathSegment_Type())
bgp4PathAttrASPathSegment.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4PathAttrASPathSegment.setStatus(_A)
_Bgp4PathAttrNextHop_Type=InetAddress
_Bgp4PathAttrNextHop_Object=MibTableColumn
bgp4PathAttrNextHop=_Bgp4PathAttrNextHop_Object((1,3,6,1,4,1,40310,7,5,1,6),_Bgp4PathAttrNextHop_Type())
bgp4PathAttrNextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4PathAttrNextHop.setStatus(_A)
class _Bgp4PathAttrMultiExitDisc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_Bgp4PathAttrMultiExitDisc_Type.__name__=_C
_Bgp4PathAttrMultiExitDisc_Object=MibTableColumn
bgp4PathAttrMultiExitDisc=_Bgp4PathAttrMultiExitDisc_Object((1,3,6,1,4,1,40310,7,5,1,7),_Bgp4PathAttrMultiExitDisc_Type())
bgp4PathAttrMultiExitDisc.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4PathAttrMultiExitDisc.setStatus(_A)
class _Bgp4PathAttrLocalPref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_Bgp4PathAttrLocalPref_Type.__name__=_C
_Bgp4PathAttrLocalPref_Object=MibTableColumn
bgp4PathAttrLocalPref=_Bgp4PathAttrLocalPref_Object((1,3,6,1,4,1,40310,7,5,1,8),_Bgp4PathAttrLocalPref_Type())
bgp4PathAttrLocalPref.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4PathAttrLocalPref.setStatus(_A)
class _Bgp4PathAttrAtomicAggregate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lessSpecificRrouteNotSelected',1),('lessSpecificRouteSelected',2)))
_Bgp4PathAttrAtomicAggregate_Type.__name__=_C
_Bgp4PathAttrAtomicAggregate_Object=MibTableColumn
bgp4PathAttrAtomicAggregate=_Bgp4PathAttrAtomicAggregate_Object((1,3,6,1,4,1,40310,7,5,1,9),_Bgp4PathAttrAtomicAggregate_Type())
bgp4PathAttrAtomicAggregate.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4PathAttrAtomicAggregate.setStatus(_A)
class _Bgp4PathAttrAggregatorAS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Bgp4PathAttrAggregatorAS_Type.__name__=_C
_Bgp4PathAttrAggregatorAS_Object=MibTableColumn
bgp4PathAttrAggregatorAS=_Bgp4PathAttrAggregatorAS_Object((1,3,6,1,4,1,40310,7,5,1,10),_Bgp4PathAttrAggregatorAS_Type())
bgp4PathAttrAggregatorAS.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4PathAttrAggregatorAS.setStatus(_A)
_Bgp4PathAttrAggregatorAddr_Type=IpAddress
_Bgp4PathAttrAggregatorAddr_Object=MibTableColumn
bgp4PathAttrAggregatorAddr=_Bgp4PathAttrAggregatorAddr_Object((1,3,6,1,4,1,40310,7,5,1,11),_Bgp4PathAttrAggregatorAddr_Type())
bgp4PathAttrAggregatorAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4PathAttrAggregatorAddr.setStatus(_A)
class _Bgp4PathAttrCalcLocalPref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_Bgp4PathAttrCalcLocalPref_Type.__name__=_C
_Bgp4PathAttrCalcLocalPref_Object=MibTableColumn
bgp4PathAttrCalcLocalPref=_Bgp4PathAttrCalcLocalPref_Object((1,3,6,1,4,1,40310,7,5,1,12),_Bgp4PathAttrCalcLocalPref_Type())
bgp4PathAttrCalcLocalPref.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4PathAttrCalcLocalPref.setStatus(_A)
class _Bgp4PathAttrBest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('false',1),('true',2)))
_Bgp4PathAttrBest_Type.__name__=_C
_Bgp4PathAttrBest_Object=MibTableColumn
bgp4PathAttrBest=_Bgp4PathAttrBest_Object((1,3,6,1,4,1,40310,7,5,1,13),_Bgp4PathAttrBest_Type())
bgp4PathAttrBest.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4PathAttrBest.setStatus(_A)
class _Bgp4PathAttrUnknown_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_Bgp4PathAttrUnknown_Type.__name__=_E
_Bgp4PathAttrUnknown_Object=MibTableColumn
bgp4PathAttrUnknown=_Bgp4PathAttrUnknown_Object((1,3,6,1,4,1,40310,7,5,1,14),_Bgp4PathAttrUnknown_Type())
bgp4PathAttrUnknown.setMaxAccess(_B)
if mibBuilder.loadTexts:bgp4PathAttrUnknown.setStatus(_A)
class _BgpVrfTable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BgpVrfTable_Type.__name__=_C
_BgpVrfTable_Object=MibScalar
bgpVrfTable=_BgpVrfTable_Object((1,3,6,1,4,1,40310,7,6),_BgpVrfTable_Type())
bgpVrfTable.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpVrfTable.setStatus(_A)
class _BgpVrfId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BgpVrfId_Type.__name__=_C
_BgpVrfId_Object=MibScalar
bgpVrfId=_BgpVrfId_Object((1,3,6,1,4,1,40310,7,7),_BgpVrfId_Type())
bgpVrfId.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpVrfId.setStatus(_A)
_BgpVrfName_Type=DisplayString
_BgpVrfName_Object=MibScalar
bgpVrfName=_BgpVrfName_Object((1,3,6,1,4,1,40310,7,8),_BgpVrfName_Type())
bgpVrfName.setMaxAccess(_B)
if mibBuilder.loadTexts:bgpVrfName.setStatus(_A)
_BgpTraps_ObjectIdentity=ObjectIdentity
bgpTraps=_BgpTraps_ObjectIdentity((1,3,6,1,4,1,40310,7,9))
bgpEstablished=NotificationType((1,3,6,1,4,1,40310,7,9,1))
bgpEstablished.setObjects(*((_D,_G),(_D,_H)))
if mibBuilder.loadTexts:bgpEstablished.setStatus(_A)
bgpBackwardTransition=NotificationType((1,3,6,1,4,1,40310,7,9,2))
bgpBackwardTransition.setObjects(*((_D,_G),(_D,_H)))
if mibBuilder.loadTexts:bgpBackwardTransition.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'bgp':bgp,'bgpVersion':bgpVersion,'bgpLocalAs':bgpLocalAs,'bgpOuterTable':bgpOuterTable,'bgpPeerTable':bgpPeerTable,'bgpPeerEntry':bgpPeerEntry,'bgpPeerIdentifier':bgpPeerIdentifier,_H:bgpPeerState,'bgpPeerAdminStatus':bgpPeerAdminStatus,'bgpPeerNegotiatedVersion':bgpPeerNegotiatedVersion,'bgpPeerLocalAddr':bgpPeerLocalAddr,'bgpPeerLocalPort':bgpPeerLocalPort,'bgpPeerRemoteAddr':bgpPeerRemoteAddr,'bgpPeerRemotePort':bgpPeerRemotePort,'bgpPeerRemoteAs':bgpPeerRemoteAs,'bgpPeerInUpdates':bgpPeerInUpdates,'bgpPeerOutUpdates':bgpPeerOutUpdates,'bgpPeerInTotalMessages':bgpPeerInTotalMessages,'bgpPeerOutTotalMessages':bgpPeerOutTotalMessages,_G:bgpPeerLastError,'bgpPeerFsmEstablishedTransitions':bgpPeerFsmEstablishedTransitions,'bgpPeerFsmEstablishedTime':bgpPeerFsmEstablishedTime,'bgpPeerConnectRetryInterval':bgpPeerConnectRetryInterval,'bgpPeerHoldTime':bgpPeerHoldTime,'bgpPeerKeepAlive':bgpPeerKeepAlive,'bgpPeerHoldTimeConfigured':bgpPeerHoldTimeConfigured,'bgpPeerKeepAliveConfigured':bgpPeerKeepAliveConfigured,'bgpPeerMinRouteAdvertisementInterval':bgpPeerMinRouteAdvertisementInterval,'bgpPeerInUpdateElapsedTime':bgpPeerInUpdateElapsedTime,'bgpPeerIface':bgpPeerIface,'bgpPeerDesc':bgpPeerDesc,_K:bgpPeerIfindex,_J:bgpPeerIdType,'bgpIdentifier':bgpIdentifier,'bgp4PathAttrTable':bgp4PathAttrTable,'bgp4PathAttrEntry':bgp4PathAttrEntry,_N:bgp4PathAttrPeer,_M:bgp4PathAttrIpAddrPrefixLen,_L:bgp4PathAttrIpAddrPrefix,'bgp4PathAttrOrigin':bgp4PathAttrOrigin,'bgp4PathAttrASPathSegment':bgp4PathAttrASPathSegment,'bgp4PathAttrNextHop':bgp4PathAttrNextHop,'bgp4PathAttrMultiExitDisc':bgp4PathAttrMultiExitDisc,'bgp4PathAttrLocalPref':bgp4PathAttrLocalPref,'bgp4PathAttrAtomicAggregate':bgp4PathAttrAtomicAggregate,'bgp4PathAttrAggregatorAS':bgp4PathAttrAggregatorAS,'bgp4PathAttrAggregatorAddr':bgp4PathAttrAggregatorAddr,'bgp4PathAttrCalcLocalPref':bgp4PathAttrCalcLocalPref,'bgp4PathAttrBest':bgp4PathAttrBest,'bgp4PathAttrUnknown':bgp4PathAttrUnknown,_I:bgpVrfTable,'bgpVrfId':bgpVrfId,'bgpVrfName':bgpVrfName,'bgpTraps':bgpTraps,'bgpEstablished':bgpEstablished,'bgpBackwardTransition':bgpBackwardTransition})