_R='nsVrBgpPeerState'
_Q='nsVrBgpPeerLastError'
_P='nsVrBgpPeerIdentifier'
_O='nsVrBgp4PathAttrPeer'
_N='nsVrBgp4PathAttrIpAddrPrefixLen'
_M='nsVrBgp4PathAttrIpAddrPrefix'
_L='nsVrBgpPeerRemoteAddr'
_K='nsVrBgpPeerVRID'
_J='nsVrBgpInfoVRID'
_I='netscreenTrapType'
_H='netscreenTrapDesc'
_G='nsVrBgp4PathAttrVRID'
_F='NETSCREEN-TRAP-MIB'
_E='OctetString'
_D='NETSCREEN-VR-BGP4-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
netscreenVR,=mibBuilder.importSymbols('NETSCREEN-SMI','netscreenVR')
netscreenTrapDesc,netscreenTrapType=mibBuilder.importSymbols(_F,_H,_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nsVrBgp=ModuleIdentity((1,3,6,1,4,1,3224,18,6))
_NsVrBgpInfoTable_Object=MibTable
nsVrBgpInfoTable=_NsVrBgpInfoTable_Object((1,3,6,1,4,1,3224,18,6,1))
if mibBuilder.loadTexts:nsVrBgpInfoTable.setStatus(_A)
_NsVrBgpInfoEntry_Object=MibTableRow
nsVrBgpInfoEntry=_NsVrBgpInfoEntry_Object((1,3,6,1,4,1,3224,18,6,1,1))
nsVrBgpInfoEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:nsVrBgpInfoEntry.setStatus(_A)
class _NsVrBgpInfoVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_NsVrBgpInfoVersion_Type.__name__=_E
_NsVrBgpInfoVersion_Object=MibTableColumn
nsVrBgpInfoVersion=_NsVrBgpInfoVersion_Object((1,3,6,1,4,1,3224,18,6,1,1,1),_NsVrBgpInfoVersion_Type())
nsVrBgpInfoVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpInfoVersion.setStatus(_A)
class _NsVrBgpInfoLocalAs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsVrBgpInfoLocalAs_Type.__name__=_C
_NsVrBgpInfoLocalAs_Object=MibTableColumn
nsVrBgpInfoLocalAs=_NsVrBgpInfoLocalAs_Object((1,3,6,1,4,1,3224,18,6,1,1,2),_NsVrBgpInfoLocalAs_Type())
nsVrBgpInfoLocalAs.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpInfoLocalAs.setStatus(_A)
_NsVrBgpInfoIdentifier_Type=IpAddress
_NsVrBgpInfoIdentifier_Object=MibTableColumn
nsVrBgpInfoIdentifier=_NsVrBgpInfoIdentifier_Object((1,3,6,1,4,1,3224,18,6,1,1,3),_NsVrBgpInfoIdentifier_Type())
nsVrBgpInfoIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpInfoIdentifier.setStatus(_A)
class _NsVrBgpInfoVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsVrBgpInfoVRID_Type.__name__=_C
_NsVrBgpInfoVRID_Object=MibTableColumn
nsVrBgpInfoVRID=_NsVrBgpInfoVRID_Object((1,3,6,1,4,1,3224,18,6,1,1,4),_NsVrBgpInfoVRID_Type())
nsVrBgpInfoVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpInfoVRID.setStatus(_A)
_NsVrBgpPeerTable_Object=MibTable
nsVrBgpPeerTable=_NsVrBgpPeerTable_Object((1,3,6,1,4,1,3224,18,6,3))
if mibBuilder.loadTexts:nsVrBgpPeerTable.setStatus(_A)
_NsVrBgpPeerEntry_Object=MibTableRow
nsVrBgpPeerEntry=_NsVrBgpPeerEntry_Object((1,3,6,1,4,1,3224,18,6,3,1))
nsVrBgpPeerEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:nsVrBgpPeerEntry.setStatus(_A)
_NsVrBgpPeerIdentifier_Type=IpAddress
_NsVrBgpPeerIdentifier_Object=MibTableColumn
nsVrBgpPeerIdentifier=_NsVrBgpPeerIdentifier_Object((1,3,6,1,4,1,3224,18,6,3,1,1),_NsVrBgpPeerIdentifier_Type())
nsVrBgpPeerIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpPeerIdentifier.setStatus(_A)
class _NsVrBgpPeerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('idle',1),('connect',2),('active',3),('opensent',4),('openconfirm',5),('established',6)))
_NsVrBgpPeerState_Type.__name__=_C
_NsVrBgpPeerState_Object=MibTableColumn
nsVrBgpPeerState=_NsVrBgpPeerState_Object((1,3,6,1,4,1,3224,18,6,3,1,2),_NsVrBgpPeerState_Type())
nsVrBgpPeerState.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpPeerState.setStatus(_A)
class _NsVrBgpPeerAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stop',1),('start',2)))
_NsVrBgpPeerAdminStatus_Type.__name__=_C
_NsVrBgpPeerAdminStatus_Object=MibTableColumn
nsVrBgpPeerAdminStatus=_NsVrBgpPeerAdminStatus_Object((1,3,6,1,4,1,3224,18,6,3,1,3),_NsVrBgpPeerAdminStatus_Type())
nsVrBgpPeerAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpPeerAdminStatus.setStatus(_A)
_NsVrBgpPeerNegotiatedVersion_Type=Integer32
_NsVrBgpPeerNegotiatedVersion_Object=MibTableColumn
nsVrBgpPeerNegotiatedVersion=_NsVrBgpPeerNegotiatedVersion_Object((1,3,6,1,4,1,3224,18,6,3,1,4),_NsVrBgpPeerNegotiatedVersion_Type())
nsVrBgpPeerNegotiatedVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpPeerNegotiatedVersion.setStatus(_A)
_NsVrBgpPeerLocalAddr_Type=IpAddress
_NsVrBgpPeerLocalAddr_Object=MibTableColumn
nsVrBgpPeerLocalAddr=_NsVrBgpPeerLocalAddr_Object((1,3,6,1,4,1,3224,18,6,3,1,5),_NsVrBgpPeerLocalAddr_Type())
nsVrBgpPeerLocalAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpPeerLocalAddr.setStatus(_A)
class _NsVrBgpPeerLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsVrBgpPeerLocalPort_Type.__name__=_C
_NsVrBgpPeerLocalPort_Object=MibTableColumn
nsVrBgpPeerLocalPort=_NsVrBgpPeerLocalPort_Object((1,3,6,1,4,1,3224,18,6,3,1,6),_NsVrBgpPeerLocalPort_Type())
nsVrBgpPeerLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpPeerLocalPort.setStatus(_A)
_NsVrBgpPeerRemoteAddr_Type=IpAddress
_NsVrBgpPeerRemoteAddr_Object=MibTableColumn
nsVrBgpPeerRemoteAddr=_NsVrBgpPeerRemoteAddr_Object((1,3,6,1,4,1,3224,18,6,3,1,7),_NsVrBgpPeerRemoteAddr_Type())
nsVrBgpPeerRemoteAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpPeerRemoteAddr.setStatus(_A)
class _NsVrBgpPeerRemotePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsVrBgpPeerRemotePort_Type.__name__=_C
_NsVrBgpPeerRemotePort_Object=MibTableColumn
nsVrBgpPeerRemotePort=_NsVrBgpPeerRemotePort_Object((1,3,6,1,4,1,3224,18,6,3,1,8),_NsVrBgpPeerRemotePort_Type())
nsVrBgpPeerRemotePort.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpPeerRemotePort.setStatus(_A)
class _NsVrBgpPeerRemoteAs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsVrBgpPeerRemoteAs_Type.__name__=_C
_NsVrBgpPeerRemoteAs_Object=MibTableColumn
nsVrBgpPeerRemoteAs=_NsVrBgpPeerRemoteAs_Object((1,3,6,1,4,1,3224,18,6,3,1,9),_NsVrBgpPeerRemoteAs_Type())
nsVrBgpPeerRemoteAs.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpPeerRemoteAs.setStatus(_A)
_NsVrBgpPeerInUpdates_Type=Counter32
_NsVrBgpPeerInUpdates_Object=MibTableColumn
nsVrBgpPeerInUpdates=_NsVrBgpPeerInUpdates_Object((1,3,6,1,4,1,3224,18,6,3,1,10),_NsVrBgpPeerInUpdates_Type())
nsVrBgpPeerInUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpPeerInUpdates.setStatus(_A)
_NsVrBgpPeerOutUpdates_Type=Counter32
_NsVrBgpPeerOutUpdates_Object=MibTableColumn
nsVrBgpPeerOutUpdates=_NsVrBgpPeerOutUpdates_Object((1,3,6,1,4,1,3224,18,6,3,1,11),_NsVrBgpPeerOutUpdates_Type())
nsVrBgpPeerOutUpdates.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpPeerOutUpdates.setStatus(_A)
_NsVrBgpPeerInTotalMessages_Type=Counter32
_NsVrBgpPeerInTotalMessages_Object=MibTableColumn
nsVrBgpPeerInTotalMessages=_NsVrBgpPeerInTotalMessages_Object((1,3,6,1,4,1,3224,18,6,3,1,12),_NsVrBgpPeerInTotalMessages_Type())
nsVrBgpPeerInTotalMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpPeerInTotalMessages.setStatus(_A)
_NsVrBgpPeerOutTotalMessages_Type=Counter32
_NsVrBgpPeerOutTotalMessages_Object=MibTableColumn
nsVrBgpPeerOutTotalMessages=_NsVrBgpPeerOutTotalMessages_Object((1,3,6,1,4,1,3224,18,6,3,1,13),_NsVrBgpPeerOutTotalMessages_Type())
nsVrBgpPeerOutTotalMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpPeerOutTotalMessages.setStatus(_A)
class _NsVrBgpPeerLastError_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_NsVrBgpPeerLastError_Type.__name__=_E
_NsVrBgpPeerLastError_Object=MibTableColumn
nsVrBgpPeerLastError=_NsVrBgpPeerLastError_Object((1,3,6,1,4,1,3224,18,6,3,1,14),_NsVrBgpPeerLastError_Type())
nsVrBgpPeerLastError.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpPeerLastError.setStatus(_A)
_NsVrBgpPeerFsmEstablishedTransitions_Type=Counter32
_NsVrBgpPeerFsmEstablishedTransitions_Object=MibTableColumn
nsVrBgpPeerFsmEstablishedTransitions=_NsVrBgpPeerFsmEstablishedTransitions_Object((1,3,6,1,4,1,3224,18,6,3,1,15),_NsVrBgpPeerFsmEstablishedTransitions_Type())
nsVrBgpPeerFsmEstablishedTransitions.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpPeerFsmEstablishedTransitions.setStatus(_A)
_NsVrBgpPeerFsmEstablishedTime_Type=Gauge32
_NsVrBgpPeerFsmEstablishedTime_Object=MibTableColumn
nsVrBgpPeerFsmEstablishedTime=_NsVrBgpPeerFsmEstablishedTime_Object((1,3,6,1,4,1,3224,18,6,3,1,16),_NsVrBgpPeerFsmEstablishedTime_Type())
nsVrBgpPeerFsmEstablishedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpPeerFsmEstablishedTime.setStatus(_A)
class _NsVrBgpPeerConnectRetryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NsVrBgpPeerConnectRetryInterval_Type.__name__=_C
_NsVrBgpPeerConnectRetryInterval_Object=MibTableColumn
nsVrBgpPeerConnectRetryInterval=_NsVrBgpPeerConnectRetryInterval_Object((1,3,6,1,4,1,3224,18,6,3,1,17),_NsVrBgpPeerConnectRetryInterval_Type())
nsVrBgpPeerConnectRetryInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpPeerConnectRetryInterval.setStatus(_A)
class _NsVrBgpPeerHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_NsVrBgpPeerHoldTime_Type.__name__=_C
_NsVrBgpPeerHoldTime_Object=MibTableColumn
nsVrBgpPeerHoldTime=_NsVrBgpPeerHoldTime_Object((1,3,6,1,4,1,3224,18,6,3,1,18),_NsVrBgpPeerHoldTime_Type())
nsVrBgpPeerHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpPeerHoldTime.setStatus(_A)
class _NsVrBgpPeerKeepAlive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_NsVrBgpPeerKeepAlive_Type.__name__=_C
_NsVrBgpPeerKeepAlive_Object=MibTableColumn
nsVrBgpPeerKeepAlive=_NsVrBgpPeerKeepAlive_Object((1,3,6,1,4,1,3224,18,6,3,1,19),_NsVrBgpPeerKeepAlive_Type())
nsVrBgpPeerKeepAlive.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpPeerKeepAlive.setStatus(_A)
class _NsVrBgpPeerHoldTimeConfigured_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_NsVrBgpPeerHoldTimeConfigured_Type.__name__=_C
_NsVrBgpPeerHoldTimeConfigured_Object=MibTableColumn
nsVrBgpPeerHoldTimeConfigured=_NsVrBgpPeerHoldTimeConfigured_Object((1,3,6,1,4,1,3224,18,6,3,1,20),_NsVrBgpPeerHoldTimeConfigured_Type())
nsVrBgpPeerHoldTimeConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpPeerHoldTimeConfigured.setStatus(_A)
class _NsVrBgpPeerKeepAliveConfigured_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_NsVrBgpPeerKeepAliveConfigured_Type.__name__=_C
_NsVrBgpPeerKeepAliveConfigured_Object=MibTableColumn
nsVrBgpPeerKeepAliveConfigured=_NsVrBgpPeerKeepAliveConfigured_Object((1,3,6,1,4,1,3224,18,6,3,1,21),_NsVrBgpPeerKeepAliveConfigured_Type())
nsVrBgpPeerKeepAliveConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpPeerKeepAliveConfigured.setStatus(_A)
class _NsVrBgpPeerMinASOriginationInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NsVrBgpPeerMinASOriginationInterval_Type.__name__=_C
_NsVrBgpPeerMinASOriginationInterval_Object=MibTableColumn
nsVrBgpPeerMinASOriginationInterval=_NsVrBgpPeerMinASOriginationInterval_Object((1,3,6,1,4,1,3224,18,6,3,1,22),_NsVrBgpPeerMinASOriginationInterval_Type())
nsVrBgpPeerMinASOriginationInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpPeerMinASOriginationInterval.setStatus(_A)
class _NsVrBgpPeerMinRouteAdvertisementInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NsVrBgpPeerMinRouteAdvertisementInterval_Type.__name__=_C
_NsVrBgpPeerMinRouteAdvertisementInterval_Object=MibTableColumn
nsVrBgpPeerMinRouteAdvertisementInterval=_NsVrBgpPeerMinRouteAdvertisementInterval_Object((1,3,6,1,4,1,3224,18,6,3,1,23),_NsVrBgpPeerMinRouteAdvertisementInterval_Type())
nsVrBgpPeerMinRouteAdvertisementInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpPeerMinRouteAdvertisementInterval.setStatus(_A)
_NsVrBgpPeerInUpdateElapsedTime_Type=Gauge32
_NsVrBgpPeerInUpdateElapsedTime_Object=MibTableColumn
nsVrBgpPeerInUpdateElapsedTime=_NsVrBgpPeerInUpdateElapsedTime_Object((1,3,6,1,4,1,3224,18,6,3,1,24),_NsVrBgpPeerInUpdateElapsedTime_Type())
nsVrBgpPeerInUpdateElapsedTime.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpPeerInUpdateElapsedTime.setStatus(_A)
class _NsVrBgpPeerVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsVrBgpPeerVRID_Type.__name__=_C
_NsVrBgpPeerVRID_Object=MibTableColumn
nsVrBgpPeerVRID=_NsVrBgpPeerVRID_Object((1,3,6,1,4,1,3224,18,6,3,1,25),_NsVrBgpPeerVRID_Type())
nsVrBgpPeerVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgpPeerVRID.setStatus(_A)
_NsVrBgp4PathAttrTable_Object=MibTable
nsVrBgp4PathAttrTable=_NsVrBgp4PathAttrTable_Object((1,3,6,1,4,1,3224,18,6,6))
if mibBuilder.loadTexts:nsVrBgp4PathAttrTable.setStatus(_A)
_NsVrBgp4PathAttrEntry_Object=MibTableRow
nsVrBgp4PathAttrEntry=_NsVrBgp4PathAttrEntry_Object((1,3,6,1,4,1,3224,18,6,6,1))
nsVrBgp4PathAttrEntry.setIndexNames((0,_D,_G),(0,_D,_M),(0,_D,_N),(0,_D,_O))
if mibBuilder.loadTexts:nsVrBgp4PathAttrEntry.setStatus(_A)
_NsVrBgp4PathAttrPeer_Type=IpAddress
_NsVrBgp4PathAttrPeer_Object=MibTableColumn
nsVrBgp4PathAttrPeer=_NsVrBgp4PathAttrPeer_Object((1,3,6,1,4,1,3224,18,6,6,1,1),_NsVrBgp4PathAttrPeer_Type())
nsVrBgp4PathAttrPeer.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgp4PathAttrPeer.setStatus(_A)
class _NsVrBgp4PathAttrIpAddrPrefixLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_NsVrBgp4PathAttrIpAddrPrefixLen_Type.__name__=_C
_NsVrBgp4PathAttrIpAddrPrefixLen_Object=MibTableColumn
nsVrBgp4PathAttrIpAddrPrefixLen=_NsVrBgp4PathAttrIpAddrPrefixLen_Object((1,3,6,1,4,1,3224,18,6,6,1,2),_NsVrBgp4PathAttrIpAddrPrefixLen_Type())
nsVrBgp4PathAttrIpAddrPrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgp4PathAttrIpAddrPrefixLen.setStatus(_A)
_NsVrBgp4PathAttrIpAddrPrefix_Type=IpAddress
_NsVrBgp4PathAttrIpAddrPrefix_Object=MibTableColumn
nsVrBgp4PathAttrIpAddrPrefix=_NsVrBgp4PathAttrIpAddrPrefix_Object((1,3,6,1,4,1,3224,18,6,6,1,3),_NsVrBgp4PathAttrIpAddrPrefix_Type())
nsVrBgp4PathAttrIpAddrPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgp4PathAttrIpAddrPrefix.setStatus(_A)
class _NsVrBgp4PathAttrOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('igp',1),('egp',2),('incomplete',3)))
_NsVrBgp4PathAttrOrigin_Type.__name__=_C
_NsVrBgp4PathAttrOrigin_Object=MibTableColumn
nsVrBgp4PathAttrOrigin=_NsVrBgp4PathAttrOrigin_Object((1,3,6,1,4,1,3224,18,6,6,1,4),_NsVrBgp4PathAttrOrigin_Type())
nsVrBgp4PathAttrOrigin.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgp4PathAttrOrigin.setStatus(_A)
class _NsVrBgp4PathAttrASPathSegment_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,255))
_NsVrBgp4PathAttrASPathSegment_Type.__name__=_E
_NsVrBgp4PathAttrASPathSegment_Object=MibTableColumn
nsVrBgp4PathAttrASPathSegment=_NsVrBgp4PathAttrASPathSegment_Object((1,3,6,1,4,1,3224,18,6,6,1,5),_NsVrBgp4PathAttrASPathSegment_Type())
nsVrBgp4PathAttrASPathSegment.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgp4PathAttrASPathSegment.setStatus(_A)
_NsVrBgp4PathAttrNextHop_Type=IpAddress
_NsVrBgp4PathAttrNextHop_Object=MibTableColumn
nsVrBgp4PathAttrNextHop=_NsVrBgp4PathAttrNextHop_Object((1,3,6,1,4,1,3224,18,6,6,1,6),_NsVrBgp4PathAttrNextHop_Type())
nsVrBgp4PathAttrNextHop.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgp4PathAttrNextHop.setStatus(_A)
class _NsVrBgp4PathAttrMultiExitDisc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_NsVrBgp4PathAttrMultiExitDisc_Type.__name__=_C
_NsVrBgp4PathAttrMultiExitDisc_Object=MibTableColumn
nsVrBgp4PathAttrMultiExitDisc=_NsVrBgp4PathAttrMultiExitDisc_Object((1,3,6,1,4,1,3224,18,6,6,1,7),_NsVrBgp4PathAttrMultiExitDisc_Type())
nsVrBgp4PathAttrMultiExitDisc.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgp4PathAttrMultiExitDisc.setStatus(_A)
class _NsVrBgp4PathAttrLocalPref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_NsVrBgp4PathAttrLocalPref_Type.__name__=_C
_NsVrBgp4PathAttrLocalPref_Object=MibTableColumn
nsVrBgp4PathAttrLocalPref=_NsVrBgp4PathAttrLocalPref_Object((1,3,6,1,4,1,3224,18,6,6,1,8),_NsVrBgp4PathAttrLocalPref_Type())
nsVrBgp4PathAttrLocalPref.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgp4PathAttrLocalPref.setStatus(_A)
class _NsVrBgp4PathAttrAtomicAggregate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lessSpecificRrouteNotSelected',1),('lessSpecificRouteSelected',2)))
_NsVrBgp4PathAttrAtomicAggregate_Type.__name__=_C
_NsVrBgp4PathAttrAtomicAggregate_Object=MibTableColumn
nsVrBgp4PathAttrAtomicAggregate=_NsVrBgp4PathAttrAtomicAggregate_Object((1,3,6,1,4,1,3224,18,6,6,1,9),_NsVrBgp4PathAttrAtomicAggregate_Type())
nsVrBgp4PathAttrAtomicAggregate.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgp4PathAttrAtomicAggregate.setStatus(_A)
class _NsVrBgp4PathAttrAggregatorAS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsVrBgp4PathAttrAggregatorAS_Type.__name__=_C
_NsVrBgp4PathAttrAggregatorAS_Object=MibTableColumn
nsVrBgp4PathAttrAggregatorAS=_NsVrBgp4PathAttrAggregatorAS_Object((1,3,6,1,4,1,3224,18,6,6,1,10),_NsVrBgp4PathAttrAggregatorAS_Type())
nsVrBgp4PathAttrAggregatorAS.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgp4PathAttrAggregatorAS.setStatus(_A)
_NsVrBgp4PathAttrAggregatorAddr_Type=IpAddress
_NsVrBgp4PathAttrAggregatorAddr_Object=MibTableColumn
nsVrBgp4PathAttrAggregatorAddr=_NsVrBgp4PathAttrAggregatorAddr_Object((1,3,6,1,4,1,3224,18,6,6,1,11),_NsVrBgp4PathAttrAggregatorAddr_Type())
nsVrBgp4PathAttrAggregatorAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgp4PathAttrAggregatorAddr.setStatus(_A)
class _NsVrBgp4PathAttrCalcLocalPref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_NsVrBgp4PathAttrCalcLocalPref_Type.__name__=_C
_NsVrBgp4PathAttrCalcLocalPref_Object=MibTableColumn
nsVrBgp4PathAttrCalcLocalPref=_NsVrBgp4PathAttrCalcLocalPref_Object((1,3,6,1,4,1,3224,18,6,6,1,12),_NsVrBgp4PathAttrCalcLocalPref_Type())
nsVrBgp4PathAttrCalcLocalPref.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgp4PathAttrCalcLocalPref.setStatus(_A)
class _NsVrBgp4PathAttrBest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('false',1),('true',2)))
_NsVrBgp4PathAttrBest_Type.__name__=_C
_NsVrBgp4PathAttrBest_Object=MibTableColumn
nsVrBgp4PathAttrBest=_NsVrBgp4PathAttrBest_Object((1,3,6,1,4,1,3224,18,6,6,1,13),_NsVrBgp4PathAttrBest_Type())
nsVrBgp4PathAttrBest.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgp4PathAttrBest.setStatus(_A)
class _NsVrBgp4PathAttrUnknown_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_NsVrBgp4PathAttrUnknown_Type.__name__=_E
_NsVrBgp4PathAttrUnknown_Object=MibTableColumn
nsVrBgp4PathAttrUnknown=_NsVrBgp4PathAttrUnknown_Object((1,3,6,1,4,1,3224,18,6,6,1,14),_NsVrBgp4PathAttrUnknown_Type())
nsVrBgp4PathAttrUnknown.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgp4PathAttrUnknown.setStatus(_A)
class _NsVrBgp4PathAttrVRID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_NsVrBgp4PathAttrVRID_Type.__name__=_C
_NsVrBgp4PathAttrVRID_Object=MibTableColumn
nsVrBgp4PathAttrVRID=_NsVrBgp4PathAttrVRID_Object((1,3,6,1,4,1,3224,18,6,6,1,15),_NsVrBgp4PathAttrVRID_Type())
nsVrBgp4PathAttrVRID.setMaxAccess(_B)
if mibBuilder.loadTexts:nsVrBgp4PathAttrVRID.setStatus(_A)
_NsVrBgpTraps_ObjectIdentity=ObjectIdentity
nsVrBgpTraps=_NsVrBgpTraps_ObjectIdentity((1,3,6,1,4,1,3224,18,6,7))
nsVrBgpEstablished=NotificationType((1,3,6,1,4,1,3224,18,6,7,1))
nsVrBgpEstablished.setObjects(*((_D,_G),(_F,_I),(_F,_H),(_D,_P),(_D,_Q),(_D,_R)))
if mibBuilder.loadTexts:nsVrBgpEstablished.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'nsVrBgp':nsVrBgp,'nsVrBgpInfoTable':nsVrBgpInfoTable,'nsVrBgpInfoEntry':nsVrBgpInfoEntry,'nsVrBgpInfoVersion':nsVrBgpInfoVersion,'nsVrBgpInfoLocalAs':nsVrBgpInfoLocalAs,'nsVrBgpInfoIdentifier':nsVrBgpInfoIdentifier,_J:nsVrBgpInfoVRID,'nsVrBgpPeerTable':nsVrBgpPeerTable,'nsVrBgpPeerEntry':nsVrBgpPeerEntry,_P:nsVrBgpPeerIdentifier,_R:nsVrBgpPeerState,'nsVrBgpPeerAdminStatus':nsVrBgpPeerAdminStatus,'nsVrBgpPeerNegotiatedVersion':nsVrBgpPeerNegotiatedVersion,'nsVrBgpPeerLocalAddr':nsVrBgpPeerLocalAddr,'nsVrBgpPeerLocalPort':nsVrBgpPeerLocalPort,_L:nsVrBgpPeerRemoteAddr,'nsVrBgpPeerRemotePort':nsVrBgpPeerRemotePort,'nsVrBgpPeerRemoteAs':nsVrBgpPeerRemoteAs,'nsVrBgpPeerInUpdates':nsVrBgpPeerInUpdates,'nsVrBgpPeerOutUpdates':nsVrBgpPeerOutUpdates,'nsVrBgpPeerInTotalMessages':nsVrBgpPeerInTotalMessages,'nsVrBgpPeerOutTotalMessages':nsVrBgpPeerOutTotalMessages,_Q:nsVrBgpPeerLastError,'nsVrBgpPeerFsmEstablishedTransitions':nsVrBgpPeerFsmEstablishedTransitions,'nsVrBgpPeerFsmEstablishedTime':nsVrBgpPeerFsmEstablishedTime,'nsVrBgpPeerConnectRetryInterval':nsVrBgpPeerConnectRetryInterval,'nsVrBgpPeerHoldTime':nsVrBgpPeerHoldTime,'nsVrBgpPeerKeepAlive':nsVrBgpPeerKeepAlive,'nsVrBgpPeerHoldTimeConfigured':nsVrBgpPeerHoldTimeConfigured,'nsVrBgpPeerKeepAliveConfigured':nsVrBgpPeerKeepAliveConfigured,'nsVrBgpPeerMinASOriginationInterval':nsVrBgpPeerMinASOriginationInterval,'nsVrBgpPeerMinRouteAdvertisementInterval':nsVrBgpPeerMinRouteAdvertisementInterval,'nsVrBgpPeerInUpdateElapsedTime':nsVrBgpPeerInUpdateElapsedTime,_K:nsVrBgpPeerVRID,'nsVrBgp4PathAttrTable':nsVrBgp4PathAttrTable,'nsVrBgp4PathAttrEntry':nsVrBgp4PathAttrEntry,_O:nsVrBgp4PathAttrPeer,_N:nsVrBgp4PathAttrIpAddrPrefixLen,_M:nsVrBgp4PathAttrIpAddrPrefix,'nsVrBgp4PathAttrOrigin':nsVrBgp4PathAttrOrigin,'nsVrBgp4PathAttrASPathSegment':nsVrBgp4PathAttrASPathSegment,'nsVrBgp4PathAttrNextHop':nsVrBgp4PathAttrNextHop,'nsVrBgp4PathAttrMultiExitDisc':nsVrBgp4PathAttrMultiExitDisc,'nsVrBgp4PathAttrLocalPref':nsVrBgp4PathAttrLocalPref,'nsVrBgp4PathAttrAtomicAggregate':nsVrBgp4PathAttrAtomicAggregate,'nsVrBgp4PathAttrAggregatorAS':nsVrBgp4PathAttrAggregatorAS,'nsVrBgp4PathAttrAggregatorAddr':nsVrBgp4PathAttrAggregatorAddr,'nsVrBgp4PathAttrCalcLocalPref':nsVrBgp4PathAttrCalcLocalPref,'nsVrBgp4PathAttrBest':nsVrBgp4PathAttrBest,'nsVrBgp4PathAttrUnknown':nsVrBgp4PathAttrUnknown,_G:nsVrBgp4PathAttrVRID,'nsVrBgpTraps':nsVrBgpTraps,'nsVrBgpEstablished':nsVrBgpEstablished})