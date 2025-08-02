_R='nsBgpPeerState'
_Q='nsBgpPeerLastError'
_P='nsBgpPeerIdentifier'
_O='nsBgp4PathAttrVRID'
_N='nsBgp4PathAttrPeer'
_M='nsBgp4PathAttrIpAddrPrefixLen'
_L='nsBgp4PathAttrIpAddrPrefix'
_K='nsBgpPeerRemoteAddr'
_J='nsBgpInfoVRID'
_I='netscreenTrapType'
_H='netscreenTrapDesc'
_G='nsBgpPeerVRID'
_F='NETSCREEN-TRAP-MIB'
_E='OctetString'
_D='NETSCREEN-BGP4-MIB'
_C='Integer32'
_B='read-only'
_A='deprecated'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenVR,=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenVR')
netscreenTrapDesc,netscreenTrapType=mibBuilder.importSymbols(_F,_H,_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nsBgp=ModuleIdentity((1,3,6,1,4,1,3224,18,3))
_NsBgpInfoTable_Object=MibTable
nsBgpInfoTable=_NsBgpInfoTable_Object((1,3,6,1,4,1,3224,18,3,1))
if mibBuilder.loadTexts:nsBgpInfoTable.setStatus(_A)
_NsBgpInfoEntry_Object=MibTableRow
nsBgpInfoEntry=_NsBgpInfoEntry_Object((1,3,6,1,4,1,3224,18,3,1,1))
nsBgpInfoEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:nsBgpInfoEntry.setStatus(_A)
class _NsBgpInfoVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_NsBgpInfoVersion_Type.__name__=_E
_NsBgpInfoVersion_Object=MibTableColumn
nsBgpInfoVersion=_NsBgpInfoVersion_Object((1,3,6,1,4,1,3224,18,3,1,1,1),_NsBgpInfoVersion_Type())
nsBgpInfoVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpInfoVersion.setStatus(_A)
class _NsBgpInfoLocalAs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsBgpInfoLocalAs_Type.__name__=_C
_NsBgpInfoLocalAs_Object=MibTableColumn
nsBgpInfoLocalAs=_NsBgpInfoLocalAs_Object((1,3,6,1,4,1,3224,18,3,1,1,2),_NsBgpInfoLocalAs_Type())
nsBgpInfoLocalAs.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpInfoLocalAs.setStatus(_A)
_NsBgpInfoIdentifier_Type=IpAddress
_NsBgpInfoIdentifier_Object=MibTableColumn
nsBgpInfoIdentifier=_NsBgpInfoIdentifier_Object((1,3,6,1,4,1,3224,18,3,1,1,3),_NsBgpInfoIdentifier_Type())
nsBgpInfoIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpInfoIdentifier.setStatus(_A)
class _NsBgpInfoVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsBgpInfoVRID_Type.__name__=_C
_NsBgpInfoVRID_Object=MibTableColumn
nsBgpInfoVRID=_NsBgpInfoVRID_Object((1,3,6,1,4,1,3224,18,3,1,1,4),_NsBgpInfoVRID_Type())
nsBgpInfoVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpInfoVRID.setStatus(_A)
_NsBgpPeerTable_Object=MibTable
nsBgpPeerTable=_NsBgpPeerTable_Object((1,3,6,1,4,1,3224,18,3,3))
if mibBuilder.loadTexts:nsBgpPeerTable.setStatus(_A)
_NsBgpPeerEntry_Object=MibTableRow
nsBgpPeerEntry=_NsBgpPeerEntry_Object((1,3,6,1,4,1,3224,18,3,3,1))
nsBgpPeerEntry.setIndexNames((0,_D,_K),(0,_D,_G))
if mibBuilder.loadTexts:nsBgpPeerEntry.setStatus(_A)
_NsBgpPeerIdentifier_Type=IpAddress
_NsBgpPeerIdentifier_Object=MibTableColumn
nsBgpPeerIdentifier=_NsBgpPeerIdentifier_Object((1,3,6,1,4,1,3224,18,3,3,1,1),_NsBgpPeerIdentifier_Type())
nsBgpPeerIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpPeerIdentifier.setStatus(_A)
class _NsBgpPeerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('idle',1),('connect',2),('active',3),('opensent',4),('openconfirm',5),('established',6)))
_NsBgpPeerState_Type.__name__=_C
_NsBgpPeerState_Object=MibTableColumn
nsBgpPeerState=_NsBgpPeerState_Object((1,3,6,1,4,1,3224,18,3,3,1,2),_NsBgpPeerState_Type())
nsBgpPeerState.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpPeerState.setStatus(_A)
class _NsBgpPeerAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stop',1),('start',2)))
_NsBgpPeerAdminStatus_Type.__name__=_C
_NsBgpPeerAdminStatus_Object=MibTableColumn
nsBgpPeerAdminStatus=_NsBgpPeerAdminStatus_Object((1,3,6,1,4,1,3224,18,3,3,1,3),_NsBgpPeerAdminStatus_Type())
nsBgpPeerAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpPeerAdminStatus.setStatus(_A)
_NsBgpPeerNegotiatedVersion_Type=Integer32
_NsBgpPeerNegotiatedVersion_Object=MibTableColumn
nsBgpPeerNegotiatedVersion=_NsBgpPeerNegotiatedVersion_Object((1,3,6,1,4,1,3224,18,3,3,1,4),_NsBgpPeerNegotiatedVersion_Type())
nsBgpPeerNegotiatedVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpPeerNegotiatedVersion.setStatus(_A)
_NsBgpPeerLocalAddr_Type=IpAddress
_NsBgpPeerLocalAddr_Object=MibTableColumn
nsBgpPeerLocalAddr=_NsBgpPeerLocalAddr_Object((1,3,6,1,4,1,3224,18,3,3,1,5),_NsBgpPeerLocalAddr_Type())
nsBgpPeerLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpPeerLocalAddr.setStatus(_A)
class _NsBgpPeerLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsBgpPeerLocalPort_Type.__name__=_C
_NsBgpPeerLocalPort_Object=MibTableColumn
nsBgpPeerLocalPort=_NsBgpPeerLocalPort_Object((1,3,6,1,4,1,3224,18,3,3,1,6),_NsBgpPeerLocalPort_Type())
nsBgpPeerLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpPeerLocalPort.setStatus(_A)
_NsBgpPeerRemoteAddr_Type=IpAddress
_NsBgpPeerRemoteAddr_Object=MibTableColumn
nsBgpPeerRemoteAddr=_NsBgpPeerRemoteAddr_Object((1,3,6,1,4,1,3224,18,3,3,1,7),_NsBgpPeerRemoteAddr_Type())
nsBgpPeerRemoteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpPeerRemoteAddr.setStatus(_A)
class _NsBgpPeerRemotePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsBgpPeerRemotePort_Type.__name__=_C
_NsBgpPeerRemotePort_Object=MibTableColumn
nsBgpPeerRemotePort=_NsBgpPeerRemotePort_Object((1,3,6,1,4,1,3224,18,3,3,1,8),_NsBgpPeerRemotePort_Type())
nsBgpPeerRemotePort.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpPeerRemotePort.setStatus(_A)
class _NsBgpPeerRemoteAs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsBgpPeerRemoteAs_Type.__name__=_C
_NsBgpPeerRemoteAs_Object=MibTableColumn
nsBgpPeerRemoteAs=_NsBgpPeerRemoteAs_Object((1,3,6,1,4,1,3224,18,3,3,1,9),_NsBgpPeerRemoteAs_Type())
nsBgpPeerRemoteAs.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpPeerRemoteAs.setStatus(_A)
_NsBgpPeerInUpdates_Type=Counter32
_NsBgpPeerInUpdates_Object=MibTableColumn
nsBgpPeerInUpdates=_NsBgpPeerInUpdates_Object((1,3,6,1,4,1,3224,18,3,3,1,10),_NsBgpPeerInUpdates_Type())
nsBgpPeerInUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpPeerInUpdates.setStatus(_A)
_NsBgpPeerOutUpdates_Type=Counter32
_NsBgpPeerOutUpdates_Object=MibTableColumn
nsBgpPeerOutUpdates=_NsBgpPeerOutUpdates_Object((1,3,6,1,4,1,3224,18,3,3,1,11),_NsBgpPeerOutUpdates_Type())
nsBgpPeerOutUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpPeerOutUpdates.setStatus(_A)
_NsBgpPeerInTotalMessages_Type=Counter32
_NsBgpPeerInTotalMessages_Object=MibTableColumn
nsBgpPeerInTotalMessages=_NsBgpPeerInTotalMessages_Object((1,3,6,1,4,1,3224,18,3,3,1,12),_NsBgpPeerInTotalMessages_Type())
nsBgpPeerInTotalMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpPeerInTotalMessages.setStatus(_A)
_NsBgpPeerOutTotalMessages_Type=Counter32
_NsBgpPeerOutTotalMessages_Object=MibTableColumn
nsBgpPeerOutTotalMessages=_NsBgpPeerOutTotalMessages_Object((1,3,6,1,4,1,3224,18,3,3,1,13),_NsBgpPeerOutTotalMessages_Type())
nsBgpPeerOutTotalMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpPeerOutTotalMessages.setStatus(_A)
class _NsBgpPeerLastError_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_NsBgpPeerLastError_Type.__name__=_E
_NsBgpPeerLastError_Object=MibTableColumn
nsBgpPeerLastError=_NsBgpPeerLastError_Object((1,3,6,1,4,1,3224,18,3,3,1,14),_NsBgpPeerLastError_Type())
nsBgpPeerLastError.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpPeerLastError.setStatus(_A)
_NsBgpPeerFsmEstablishedTransitions_Type=Counter32
_NsBgpPeerFsmEstablishedTransitions_Object=MibTableColumn
nsBgpPeerFsmEstablishedTransitions=_NsBgpPeerFsmEstablishedTransitions_Object((1,3,6,1,4,1,3224,18,3,3,1,15),_NsBgpPeerFsmEstablishedTransitions_Type())
nsBgpPeerFsmEstablishedTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpPeerFsmEstablishedTransitions.setStatus(_A)
_NsBgpPeerFsmEstablishedTime_Type=Gauge32
_NsBgpPeerFsmEstablishedTime_Object=MibTableColumn
nsBgpPeerFsmEstablishedTime=_NsBgpPeerFsmEstablishedTime_Object((1,3,6,1,4,1,3224,18,3,3,1,16),_NsBgpPeerFsmEstablishedTime_Type())
nsBgpPeerFsmEstablishedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpPeerFsmEstablishedTime.setStatus(_A)
class _NsBgpPeerConnectRetryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NsBgpPeerConnectRetryInterval_Type.__name__=_C
_NsBgpPeerConnectRetryInterval_Object=MibTableColumn
nsBgpPeerConnectRetryInterval=_NsBgpPeerConnectRetryInterval_Object((1,3,6,1,4,1,3224,18,3,3,1,17),_NsBgpPeerConnectRetryInterval_Type())
nsBgpPeerConnectRetryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpPeerConnectRetryInterval.setStatus(_A)
class _NsBgpPeerHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_NsBgpPeerHoldTime_Type.__name__=_C
_NsBgpPeerHoldTime_Object=MibTableColumn
nsBgpPeerHoldTime=_NsBgpPeerHoldTime_Object((1,3,6,1,4,1,3224,18,3,3,1,18),_NsBgpPeerHoldTime_Type())
nsBgpPeerHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpPeerHoldTime.setStatus(_A)
class _NsBgpPeerKeepAlive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_NsBgpPeerKeepAlive_Type.__name__=_C
_NsBgpPeerKeepAlive_Object=MibTableColumn
nsBgpPeerKeepAlive=_NsBgpPeerKeepAlive_Object((1,3,6,1,4,1,3224,18,3,3,1,19),_NsBgpPeerKeepAlive_Type())
nsBgpPeerKeepAlive.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpPeerKeepAlive.setStatus(_A)
class _NsBgpPeerHoldTimeConfigured_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_NsBgpPeerHoldTimeConfigured_Type.__name__=_C
_NsBgpPeerHoldTimeConfigured_Object=MibTableColumn
nsBgpPeerHoldTimeConfigured=_NsBgpPeerHoldTimeConfigured_Object((1,3,6,1,4,1,3224,18,3,3,1,20),_NsBgpPeerHoldTimeConfigured_Type())
nsBgpPeerHoldTimeConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpPeerHoldTimeConfigured.setStatus(_A)
class _NsBgpPeerKeepAliveConfigured_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_NsBgpPeerKeepAliveConfigured_Type.__name__=_C
_NsBgpPeerKeepAliveConfigured_Object=MibTableColumn
nsBgpPeerKeepAliveConfigured=_NsBgpPeerKeepAliveConfigured_Object((1,3,6,1,4,1,3224,18,3,3,1,21),_NsBgpPeerKeepAliveConfigured_Type())
nsBgpPeerKeepAliveConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpPeerKeepAliveConfigured.setStatus(_A)
class _NsBgpPeerMinASOriginationInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NsBgpPeerMinASOriginationInterval_Type.__name__=_C
_NsBgpPeerMinASOriginationInterval_Object=MibTableColumn
nsBgpPeerMinASOriginationInterval=_NsBgpPeerMinASOriginationInterval_Object((1,3,6,1,4,1,3224,18,3,3,1,22),_NsBgpPeerMinASOriginationInterval_Type())
nsBgpPeerMinASOriginationInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpPeerMinASOriginationInterval.setStatus(_A)
class _NsBgpPeerMinRouteAdvertisementInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NsBgpPeerMinRouteAdvertisementInterval_Type.__name__=_C
_NsBgpPeerMinRouteAdvertisementInterval_Object=MibTableColumn
nsBgpPeerMinRouteAdvertisementInterval=_NsBgpPeerMinRouteAdvertisementInterval_Object((1,3,6,1,4,1,3224,18,3,3,1,23),_NsBgpPeerMinRouteAdvertisementInterval_Type())
nsBgpPeerMinRouteAdvertisementInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpPeerMinRouteAdvertisementInterval.setStatus(_A)
_NsBgpPeerInUpdateElapsedTime_Type=Gauge32
_NsBgpPeerInUpdateElapsedTime_Object=MibTableColumn
nsBgpPeerInUpdateElapsedTime=_NsBgpPeerInUpdateElapsedTime_Object((1,3,6,1,4,1,3224,18,3,3,1,24),_NsBgpPeerInUpdateElapsedTime_Type())
nsBgpPeerInUpdateElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpPeerInUpdateElapsedTime.setStatus(_A)
class _NsBgpPeerVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsBgpPeerVRID_Type.__name__=_C
_NsBgpPeerVRID_Object=MibTableColumn
nsBgpPeerVRID=_NsBgpPeerVRID_Object((1,3,6,1,4,1,3224,18,3,3,1,25),_NsBgpPeerVRID_Type())
nsBgpPeerVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgpPeerVRID.setStatus(_A)
_NsBgp4PathAttrTable_Object=MibTable
nsBgp4PathAttrTable=_NsBgp4PathAttrTable_Object((1,3,6,1,4,1,3224,18,3,6))
if mibBuilder.loadTexts:nsBgp4PathAttrTable.setStatus(_A)
_NsBgp4PathAttrEntry_Object=MibTableRow
nsBgp4PathAttrEntry=_NsBgp4PathAttrEntry_Object((1,3,6,1,4,1,3224,18,3,6,1))
nsBgp4PathAttrEntry.setIndexNames((0,_D,_L),(0,_D,_M),(0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:nsBgp4PathAttrEntry.setStatus(_A)
_NsBgp4PathAttrPeer_Type=IpAddress
_NsBgp4PathAttrPeer_Object=MibTableColumn
nsBgp4PathAttrPeer=_NsBgp4PathAttrPeer_Object((1,3,6,1,4,1,3224,18,3,6,1,1),_NsBgp4PathAttrPeer_Type())
nsBgp4PathAttrPeer.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgp4PathAttrPeer.setStatus(_A)
class _NsBgp4PathAttrIpAddrPrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_NsBgp4PathAttrIpAddrPrefixLen_Type.__name__=_C
_NsBgp4PathAttrIpAddrPrefixLen_Object=MibTableColumn
nsBgp4PathAttrIpAddrPrefixLen=_NsBgp4PathAttrIpAddrPrefixLen_Object((1,3,6,1,4,1,3224,18,3,6,1,2),_NsBgp4PathAttrIpAddrPrefixLen_Type())
nsBgp4PathAttrIpAddrPrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgp4PathAttrIpAddrPrefixLen.setStatus(_A)
_NsBgp4PathAttrIpAddrPrefix_Type=IpAddress
_NsBgp4PathAttrIpAddrPrefix_Object=MibTableColumn
nsBgp4PathAttrIpAddrPrefix=_NsBgp4PathAttrIpAddrPrefix_Object((1,3,6,1,4,1,3224,18,3,6,1,3),_NsBgp4PathAttrIpAddrPrefix_Type())
nsBgp4PathAttrIpAddrPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgp4PathAttrIpAddrPrefix.setStatus(_A)
class _NsBgp4PathAttrOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('igp',1),('egp',2),('incomplete',3)))
_NsBgp4PathAttrOrigin_Type.__name__=_C
_NsBgp4PathAttrOrigin_Object=MibTableColumn
nsBgp4PathAttrOrigin=_NsBgp4PathAttrOrigin_Object((1,3,6,1,4,1,3224,18,3,6,1,4),_NsBgp4PathAttrOrigin_Type())
nsBgp4PathAttrOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgp4PathAttrOrigin.setStatus(_A)
class _NsBgp4PathAttrASPathSegment_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,255))
_NsBgp4PathAttrASPathSegment_Type.__name__=_E
_NsBgp4PathAttrASPathSegment_Object=MibTableColumn
nsBgp4PathAttrASPathSegment=_NsBgp4PathAttrASPathSegment_Object((1,3,6,1,4,1,3224,18,3,6,1,5),_NsBgp4PathAttrASPathSegment_Type())
nsBgp4PathAttrASPathSegment.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgp4PathAttrASPathSegment.setStatus(_A)
_NsBgp4PathAttrNextHop_Type=IpAddress
_NsBgp4PathAttrNextHop_Object=MibTableColumn
nsBgp4PathAttrNextHop=_NsBgp4PathAttrNextHop_Object((1,3,6,1,4,1,3224,18,3,6,1,6),_NsBgp4PathAttrNextHop_Type())
nsBgp4PathAttrNextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgp4PathAttrNextHop.setStatus(_A)
class _NsBgp4PathAttrMultiExitDisc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_NsBgp4PathAttrMultiExitDisc_Type.__name__=_C
_NsBgp4PathAttrMultiExitDisc_Object=MibTableColumn
nsBgp4PathAttrMultiExitDisc=_NsBgp4PathAttrMultiExitDisc_Object((1,3,6,1,4,1,3224,18,3,6,1,7),_NsBgp4PathAttrMultiExitDisc_Type())
nsBgp4PathAttrMultiExitDisc.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgp4PathAttrMultiExitDisc.setStatus(_A)
class _NsBgp4PathAttrLocalPref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_NsBgp4PathAttrLocalPref_Type.__name__=_C
_NsBgp4PathAttrLocalPref_Object=MibTableColumn
nsBgp4PathAttrLocalPref=_NsBgp4PathAttrLocalPref_Object((1,3,6,1,4,1,3224,18,3,6,1,8),_NsBgp4PathAttrLocalPref_Type())
nsBgp4PathAttrLocalPref.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgp4PathAttrLocalPref.setStatus(_A)
class _NsBgp4PathAttrAtomicAggregate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lessSpecificRrouteNotSelected',1),('lessSpecificRouteSelected',2)))
_NsBgp4PathAttrAtomicAggregate_Type.__name__=_C
_NsBgp4PathAttrAtomicAggregate_Object=MibTableColumn
nsBgp4PathAttrAtomicAggregate=_NsBgp4PathAttrAtomicAggregate_Object((1,3,6,1,4,1,3224,18,3,6,1,9),_NsBgp4PathAttrAtomicAggregate_Type())
nsBgp4PathAttrAtomicAggregate.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgp4PathAttrAtomicAggregate.setStatus(_A)
class _NsBgp4PathAttrAggregatorAS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsBgp4PathAttrAggregatorAS_Type.__name__=_C
_NsBgp4PathAttrAggregatorAS_Object=MibTableColumn
nsBgp4PathAttrAggregatorAS=_NsBgp4PathAttrAggregatorAS_Object((1,3,6,1,4,1,3224,18,3,6,1,10),_NsBgp4PathAttrAggregatorAS_Type())
nsBgp4PathAttrAggregatorAS.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgp4PathAttrAggregatorAS.setStatus(_A)
_NsBgp4PathAttrAggregatorAddr_Type=IpAddress
_NsBgp4PathAttrAggregatorAddr_Object=MibTableColumn
nsBgp4PathAttrAggregatorAddr=_NsBgp4PathAttrAggregatorAddr_Object((1,3,6,1,4,1,3224,18,3,6,1,11),_NsBgp4PathAttrAggregatorAddr_Type())
nsBgp4PathAttrAggregatorAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgp4PathAttrAggregatorAddr.setStatus(_A)
class _NsBgp4PathAttrCalcLocalPref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_NsBgp4PathAttrCalcLocalPref_Type.__name__=_C
_NsBgp4PathAttrCalcLocalPref_Object=MibTableColumn
nsBgp4PathAttrCalcLocalPref=_NsBgp4PathAttrCalcLocalPref_Object((1,3,6,1,4,1,3224,18,3,6,1,12),_NsBgp4PathAttrCalcLocalPref_Type())
nsBgp4PathAttrCalcLocalPref.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgp4PathAttrCalcLocalPref.setStatus(_A)
class _NsBgp4PathAttrBest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('false',1),('true',2)))
_NsBgp4PathAttrBest_Type.__name__=_C
_NsBgp4PathAttrBest_Object=MibTableColumn
nsBgp4PathAttrBest=_NsBgp4PathAttrBest_Object((1,3,6,1,4,1,3224,18,3,6,1,13),_NsBgp4PathAttrBest_Type())
nsBgp4PathAttrBest.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgp4PathAttrBest.setStatus(_A)
class _NsBgp4PathAttrUnknown_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NsBgp4PathAttrUnknown_Type.__name__=_E
_NsBgp4PathAttrUnknown_Object=MibTableColumn
nsBgp4PathAttrUnknown=_NsBgp4PathAttrUnknown_Object((1,3,6,1,4,1,3224,18,3,6,1,14),_NsBgp4PathAttrUnknown_Type())
nsBgp4PathAttrUnknown.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgp4PathAttrUnknown.setStatus(_A)
class _NsBgp4PathAttrVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsBgp4PathAttrVRID_Type.__name__=_C
_NsBgp4PathAttrVRID_Object=MibTableColumn
nsBgp4PathAttrVRID=_NsBgp4PathAttrVRID_Object((1,3,6,1,4,1,3224,18,3,6,1,15),_NsBgp4PathAttrVRID_Type())
nsBgp4PathAttrVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsBgp4PathAttrVRID.setStatus(_A)
_NsBgpTraps_ObjectIdentity=ObjectIdentity
nsBgpTraps=_NsBgpTraps_ObjectIdentity((1,3,6,1,4,1,3224,18,3,7))
nsBgpEstablished=NotificationType((1,3,6,1,4,1,3224,18,3,7,1))
nsBgpEstablished.setObjects(*((_F,_I),(_F,_H),(_D,_P),(_D,_G),(_D,_Q),(_D,_R)))
if mibBuilder.loadTexts:nsBgpEstablished.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'nsBgp':nsBgp,'nsBgpInfoTable':nsBgpInfoTable,'nsBgpInfoEntry':nsBgpInfoEntry,'nsBgpInfoVersion':nsBgpInfoVersion,'nsBgpInfoLocalAs':nsBgpInfoLocalAs,'nsBgpInfoIdentifier':nsBgpInfoIdentifier,_J:nsBgpInfoVRID,'nsBgpPeerTable':nsBgpPeerTable,'nsBgpPeerEntry':nsBgpPeerEntry,_P:nsBgpPeerIdentifier,_R:nsBgpPeerState,'nsBgpPeerAdminStatus':nsBgpPeerAdminStatus,'nsBgpPeerNegotiatedVersion':nsBgpPeerNegotiatedVersion,'nsBgpPeerLocalAddr':nsBgpPeerLocalAddr,'nsBgpPeerLocalPort':nsBgpPeerLocalPort,_K:nsBgpPeerRemoteAddr,'nsBgpPeerRemotePort':nsBgpPeerRemotePort,'nsBgpPeerRemoteAs':nsBgpPeerRemoteAs,'nsBgpPeerInUpdates':nsBgpPeerInUpdates,'nsBgpPeerOutUpdates':nsBgpPeerOutUpdates,'nsBgpPeerInTotalMessages':nsBgpPeerInTotalMessages,'nsBgpPeerOutTotalMessages':nsBgpPeerOutTotalMessages,_Q:nsBgpPeerLastError,'nsBgpPeerFsmEstablishedTransitions':nsBgpPeerFsmEstablishedTransitions,'nsBgpPeerFsmEstablishedTime':nsBgpPeerFsmEstablishedTime,'nsBgpPeerConnectRetryInterval':nsBgpPeerConnectRetryInterval,'nsBgpPeerHoldTime':nsBgpPeerHoldTime,'nsBgpPeerKeepAlive':nsBgpPeerKeepAlive,'nsBgpPeerHoldTimeConfigured':nsBgpPeerHoldTimeConfigured,'nsBgpPeerKeepAliveConfigured':nsBgpPeerKeepAliveConfigured,'nsBgpPeerMinASOriginationInterval':nsBgpPeerMinASOriginationInterval,'nsBgpPeerMinRouteAdvertisementInterval':nsBgpPeerMinRouteAdvertisementInterval,'nsBgpPeerInUpdateElapsedTime':nsBgpPeerInUpdateElapsedTime,_G:nsBgpPeerVRID,'nsBgp4PathAttrTable':nsBgp4PathAttrTable,'nsBgp4PathAttrEntry':nsBgp4PathAttrEntry,_N:nsBgp4PathAttrPeer,_M:nsBgp4PathAttrIpAddrPrefixLen,_L:nsBgp4PathAttrIpAddrPrefix,'nsBgp4PathAttrOrigin':nsBgp4PathAttrOrigin,'nsBgp4PathAttrASPathSegment':nsBgp4PathAttrASPathSegment,'nsBgp4PathAttrNextHop':nsBgp4PathAttrNextHop,'nsBgp4PathAttrMultiExitDisc':nsBgp4PathAttrMultiExitDisc,'nsBgp4PathAttrLocalPref':nsBgp4PathAttrLocalPref,'nsBgp4PathAttrAtomicAggregate':nsBgp4PathAttrAtomicAggregate,'nsBgp4PathAttrAggregatorAS':nsBgp4PathAttrAggregatorAS,'nsBgp4PathAttrAggregatorAddr':nsBgp4PathAttrAggregatorAddr,'nsBgp4PathAttrCalcLocalPref':nsBgp4PathAttrCalcLocalPref,'nsBgp4PathAttrBest':nsBgp4PathAttrBest,'nsBgp4PathAttrUnknown':nsBgp4PathAttrUnknown,_O:nsBgp4PathAttrVRID,'nsBgpTraps':nsBgpTraps,'nsBgpEstablished':nsBgpEstablished})