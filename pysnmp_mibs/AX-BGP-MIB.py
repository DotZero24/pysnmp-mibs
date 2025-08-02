_A9='axBgpMIBNotificationGroup'
_A8='axBgpMIBPathAttrGroup'
_A7='axBgpMIBPeerGroup'
_A6='axBgpMIBGlobalsGroup'
_A5='axBgpPrefixThresholdClearNotification'
_A4='axBgpPrefixThresholdExceededNotification'
_A3='axBgpBackwardTransNotification'
_A2='axBgpEstablishedNotification'
_A1='axBgpPathAttrUnknown'
_A0='axBgpPathAttrBest'
_z='axBgpPathAttrCalcLocalPref'
_y='axBgpPathAttrAggregatorAddr'
_x='axBgpPathAttrAggregatorAS'
_w='axBgpPathAttrAtomicAggregate'
_v='axBgpPathAttrLocalPref'
_u='axBgpPathAttrMultiExitDisc'
_t='axBgpPathAttrNextHop'
_s='axBgpPathAttrNextHopType'
_r='axBgpPathAttrASPathSegment'
_q='axBgpPathAttrOrigin'
_p='axBgpPeerInUpdateElapsedTime'
_o='axBgpPeerMinRouteAdvertisementInterval'
_n='axBgpPeerMinASOriginationInterval'
_m='axBgpPeerKeepAliveConfigured'
_l='axBgpPeerHoldTimeConfigured'
_k='axBgpPeerKeepAlive'
_j='axBgpPeerHoldTime'
_i='axBgpPeerConnectRetryInterval'
_h='axBgpPeerFsmEstablishedTime'
_g='axBgpPeerFsmEstablishedTransitions'
_f='axBgpPeerOutTotalMessages'
_e='axBgpPeerInTotalMessages'
_d='axBgpPeerOutUpdates'
_c='axBgpPeerInUpdates'
_b='axBgpPeerRemoteAs'
_a='axBgpPeerRemotePort'
_Z='axBgpPeerLocalPort'
_Y='axBgpPeerLocalAddr'
_X='axBgpPeerNegotiatedVersion'
_W='axBgpPeerAdminStatus'
_V='axBgpPeerIdentifier'
_U='axBgpIdentifier'
_T='axBgpLocalAs'
_S='axBgpVersion'
_R='axBgpPathAttrPeer'
_Q='axBgpPathAttrPeerType'
_P='axBgpPathAttrIpAddrPrefixLen'
_O='axBgpPathAttrIpAddrPrefix'
_N='axBgpPathAttrIpAddrType'
_M='not-accessible'
_L='axBgpPeerType'
_K='axBgpPeerThreshold'
_J='axBgpPeerMaxPrefixLimit'
_I='axBgpPeerLastError'
_H='axBgpPeerState'
_G='OctetString'
_F='axBgpPeerRemoteAddr'
_E='seconds'
_D='Integer32'
_C='read-only'
_B='current'
_A='AX-BGP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
a10Mgmt,=mibBuilder.importSymbols('A10-COMMON-MIB','a10Mgmt')
InetAddress,InetAddressPrefixLength,InetAddressType,InetAutonomousSystemNumber,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType','InetAutonomousSystemNumber','InetPortNumber')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
axBgpMIB=ModuleIdentity((1,3,6,1,4,1,22610,2,5))
_AxBgpNotification_ObjectIdentity=ObjectIdentity
axBgpNotification=_AxBgpNotification_ObjectIdentity((1,3,6,1,4,1,22610,2,5,0))
class _AxBgpVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_AxBgpVersion_Type.__name__=_G
_AxBgpVersion_Object=MibScalar
axBgpVersion=_AxBgpVersion_Object((1,3,6,1,4,1,22610,2,5,1),_AxBgpVersion_Type())
axBgpVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpVersion.setStatus(_B)
_AxBgpLocalAs_Type=InetAutonomousSystemNumber
_AxBgpLocalAs_Object=MibScalar
axBgpLocalAs=_AxBgpLocalAs_Object((1,3,6,1,4,1,22610,2,5,2),_AxBgpLocalAs_Type())
axBgpLocalAs.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpLocalAs.setStatus(_B)
_AxBgpIdentifier_Type=IpAddress
_AxBgpIdentifier_Object=MibScalar
axBgpIdentifier=_AxBgpIdentifier_Object((1,3,6,1,4,1,22610,2,5,3),_AxBgpIdentifier_Type())
axBgpIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpIdentifier.setStatus(_B)
_AxBgpPeerTable_Object=MibTable
axBgpPeerTable=_AxBgpPeerTable_Object((1,3,6,1,4,1,22610,2,5,4))
if mibBuilder.loadTexts:axBgpPeerTable.setStatus(_B)
_AxBgpPeerEntry_Object=MibTableRow
axBgpPeerEntry=_AxBgpPeerEntry_Object((1,3,6,1,4,1,22610,2,5,4,1))
axBgpPeerEntry.setIndexNames((0,_A,_L),(0,_A,_F))
if mibBuilder.loadTexts:axBgpPeerEntry.setStatus(_B)
_AxBgpPeerType_Type=InetAddressType
_AxBgpPeerType_Object=MibTableColumn
axBgpPeerType=_AxBgpPeerType_Object((1,3,6,1,4,1,22610,2,5,4,1,1),_AxBgpPeerType_Type())
axBgpPeerType.setMaxAccess(_M)
if mibBuilder.loadTexts:axBgpPeerType.setStatus(_B)
_AxBgpPeerIdentifier_Type=IpAddress
_AxBgpPeerIdentifier_Object=MibTableColumn
axBgpPeerIdentifier=_AxBgpPeerIdentifier_Object((1,3,6,1,4,1,22610,2,5,4,1,2),_AxBgpPeerIdentifier_Type())
axBgpPeerIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerIdentifier.setStatus(_B)
class _AxBgpPeerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('idle',1),('connect',2),('active',3),('opensent',4),('openconfirm',5),('established',6)))
_AxBgpPeerState_Type.__name__=_D
_AxBgpPeerState_Object=MibTableColumn
axBgpPeerState=_AxBgpPeerState_Object((1,3,6,1,4,1,22610,2,5,4,1,3),_AxBgpPeerState_Type())
axBgpPeerState.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerState.setStatus(_B)
class _AxBgpPeerAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('stop',1),('start',2)))
_AxBgpPeerAdminStatus_Type.__name__=_D
_AxBgpPeerAdminStatus_Object=MibTableColumn
axBgpPeerAdminStatus=_AxBgpPeerAdminStatus_Object((1,3,6,1,4,1,22610,2,5,4,1,4),_AxBgpPeerAdminStatus_Type())
axBgpPeerAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerAdminStatus.setStatus(_B)
_AxBgpPeerNegotiatedVersion_Type=Integer32
_AxBgpPeerNegotiatedVersion_Object=MibTableColumn
axBgpPeerNegotiatedVersion=_AxBgpPeerNegotiatedVersion_Object((1,3,6,1,4,1,22610,2,5,4,1,5),_AxBgpPeerNegotiatedVersion_Type())
axBgpPeerNegotiatedVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerNegotiatedVersion.setStatus(_B)
_AxBgpPeerLocalAddr_Type=InetAddress
_AxBgpPeerLocalAddr_Object=MibTableColumn
axBgpPeerLocalAddr=_AxBgpPeerLocalAddr_Object((1,3,6,1,4,1,22610,2,5,4,1,6),_AxBgpPeerLocalAddr_Type())
axBgpPeerLocalAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerLocalAddr.setStatus(_B)
class _AxBgpPeerLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AxBgpPeerLocalPort_Type.__name__=_D
_AxBgpPeerLocalPort_Object=MibTableColumn
axBgpPeerLocalPort=_AxBgpPeerLocalPort_Object((1,3,6,1,4,1,22610,2,5,4,1,7),_AxBgpPeerLocalPort_Type())
axBgpPeerLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerLocalPort.setStatus(_B)
_AxBgpPeerRemoteAddr_Type=InetAddress
_AxBgpPeerRemoteAddr_Object=MibTableColumn
axBgpPeerRemoteAddr=_AxBgpPeerRemoteAddr_Object((1,3,6,1,4,1,22610,2,5,4,1,8),_AxBgpPeerRemoteAddr_Type())
axBgpPeerRemoteAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerRemoteAddr.setStatus(_B)
class _AxBgpPeerRemotePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AxBgpPeerRemotePort_Type.__name__=_D
_AxBgpPeerRemotePort_Object=MibTableColumn
axBgpPeerRemotePort=_AxBgpPeerRemotePort_Object((1,3,6,1,4,1,22610,2,5,4,1,9),_AxBgpPeerRemotePort_Type())
axBgpPeerRemotePort.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerRemotePort.setStatus(_B)
_AxBgpPeerRemoteAs_Type=InetAutonomousSystemNumber
_AxBgpPeerRemoteAs_Object=MibTableColumn
axBgpPeerRemoteAs=_AxBgpPeerRemoteAs_Object((1,3,6,1,4,1,22610,2,5,4,1,10),_AxBgpPeerRemoteAs_Type())
axBgpPeerRemoteAs.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerRemoteAs.setStatus(_B)
_AxBgpPeerInUpdates_Type=Counter32
_AxBgpPeerInUpdates_Object=MibTableColumn
axBgpPeerInUpdates=_AxBgpPeerInUpdates_Object((1,3,6,1,4,1,22610,2,5,4,1,11),_AxBgpPeerInUpdates_Type())
axBgpPeerInUpdates.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerInUpdates.setStatus(_B)
_AxBgpPeerOutUpdates_Type=Counter32
_AxBgpPeerOutUpdates_Object=MibTableColumn
axBgpPeerOutUpdates=_AxBgpPeerOutUpdates_Object((1,3,6,1,4,1,22610,2,5,4,1,12),_AxBgpPeerOutUpdates_Type())
axBgpPeerOutUpdates.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerOutUpdates.setStatus(_B)
_AxBgpPeerInTotalMessages_Type=Counter32
_AxBgpPeerInTotalMessages_Object=MibTableColumn
axBgpPeerInTotalMessages=_AxBgpPeerInTotalMessages_Object((1,3,6,1,4,1,22610,2,5,4,1,13),_AxBgpPeerInTotalMessages_Type())
axBgpPeerInTotalMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerInTotalMessages.setStatus(_B)
_AxBgpPeerOutTotalMessages_Type=Counter32
_AxBgpPeerOutTotalMessages_Object=MibTableColumn
axBgpPeerOutTotalMessages=_AxBgpPeerOutTotalMessages_Object((1,3,6,1,4,1,22610,2,5,4,1,14),_AxBgpPeerOutTotalMessages_Type())
axBgpPeerOutTotalMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerOutTotalMessages.setStatus(_B)
class _AxBgpPeerLastError_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_AxBgpPeerLastError_Type.__name__=_G
_AxBgpPeerLastError_Object=MibTableColumn
axBgpPeerLastError=_AxBgpPeerLastError_Object((1,3,6,1,4,1,22610,2,5,4,1,15),_AxBgpPeerLastError_Type())
axBgpPeerLastError.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerLastError.setStatus(_B)
_AxBgpPeerFsmEstablishedTransitions_Type=Counter32
_AxBgpPeerFsmEstablishedTransitions_Object=MibTableColumn
axBgpPeerFsmEstablishedTransitions=_AxBgpPeerFsmEstablishedTransitions_Object((1,3,6,1,4,1,22610,2,5,4,1,16),_AxBgpPeerFsmEstablishedTransitions_Type())
axBgpPeerFsmEstablishedTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerFsmEstablishedTransitions.setStatus(_B)
_AxBgpPeerFsmEstablishedTime_Type=Gauge32
_AxBgpPeerFsmEstablishedTime_Object=MibTableColumn
axBgpPeerFsmEstablishedTime=_AxBgpPeerFsmEstablishedTime_Object((1,3,6,1,4,1,22610,2,5,4,1,17),_AxBgpPeerFsmEstablishedTime_Type())
axBgpPeerFsmEstablishedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerFsmEstablishedTime.setStatus(_B)
if mibBuilder.loadTexts:axBgpPeerFsmEstablishedTime.setUnits(_E)
class _AxBgpPeerConnectRetryInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AxBgpPeerConnectRetryInterval_Type.__name__=_D
_AxBgpPeerConnectRetryInterval_Object=MibTableColumn
axBgpPeerConnectRetryInterval=_AxBgpPeerConnectRetryInterval_Object((1,3,6,1,4,1,22610,2,5,4,1,18),_AxBgpPeerConnectRetryInterval_Type())
axBgpPeerConnectRetryInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerConnectRetryInterval.setStatus(_B)
if mibBuilder.loadTexts:axBgpPeerConnectRetryInterval.setUnits(_E)
class _AxBgpPeerHoldTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_AxBgpPeerHoldTime_Type.__name__=_D
_AxBgpPeerHoldTime_Object=MibTableColumn
axBgpPeerHoldTime=_AxBgpPeerHoldTime_Object((1,3,6,1,4,1,22610,2,5,4,1,19),_AxBgpPeerHoldTime_Type())
axBgpPeerHoldTime.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerHoldTime.setStatus(_B)
if mibBuilder.loadTexts:axBgpPeerHoldTime.setUnits(_E)
class _AxBgpPeerKeepAlive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_AxBgpPeerKeepAlive_Type.__name__=_D
_AxBgpPeerKeepAlive_Object=MibTableColumn
axBgpPeerKeepAlive=_AxBgpPeerKeepAlive_Object((1,3,6,1,4,1,22610,2,5,4,1,20),_AxBgpPeerKeepAlive_Type())
axBgpPeerKeepAlive.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerKeepAlive.setStatus(_B)
if mibBuilder.loadTexts:axBgpPeerKeepAlive.setUnits(_E)
class _AxBgpPeerHoldTimeConfigured_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_AxBgpPeerHoldTimeConfigured_Type.__name__=_D
_AxBgpPeerHoldTimeConfigured_Object=MibTableColumn
axBgpPeerHoldTimeConfigured=_AxBgpPeerHoldTimeConfigured_Object((1,3,6,1,4,1,22610,2,5,4,1,21),_AxBgpPeerHoldTimeConfigured_Type())
axBgpPeerHoldTimeConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerHoldTimeConfigured.setStatus(_B)
if mibBuilder.loadTexts:axBgpPeerHoldTimeConfigured.setUnits(_E)
class _AxBgpPeerKeepAliveConfigured_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_AxBgpPeerKeepAliveConfigured_Type.__name__=_D
_AxBgpPeerKeepAliveConfigured_Object=MibTableColumn
axBgpPeerKeepAliveConfigured=_AxBgpPeerKeepAliveConfigured_Object((1,3,6,1,4,1,22610,2,5,4,1,22),_AxBgpPeerKeepAliveConfigured_Type())
axBgpPeerKeepAliveConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerKeepAliveConfigured.setStatus(_B)
if mibBuilder.loadTexts:axBgpPeerKeepAliveConfigured.setUnits(_E)
class _AxBgpPeerMinASOriginationInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AxBgpPeerMinASOriginationInterval_Type.__name__=_D
_AxBgpPeerMinASOriginationInterval_Object=MibTableColumn
axBgpPeerMinASOriginationInterval=_AxBgpPeerMinASOriginationInterval_Object((1,3,6,1,4,1,22610,2,5,4,1,23),_AxBgpPeerMinASOriginationInterval_Type())
axBgpPeerMinASOriginationInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerMinASOriginationInterval.setStatus(_B)
if mibBuilder.loadTexts:axBgpPeerMinASOriginationInterval.setUnits(_E)
class _AxBgpPeerMinRouteAdvertisementInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AxBgpPeerMinRouteAdvertisementInterval_Type.__name__=_D
_AxBgpPeerMinRouteAdvertisementInterval_Object=MibTableColumn
axBgpPeerMinRouteAdvertisementInterval=_AxBgpPeerMinRouteAdvertisementInterval_Object((1,3,6,1,4,1,22610,2,5,4,1,24),_AxBgpPeerMinRouteAdvertisementInterval_Type())
axBgpPeerMinRouteAdvertisementInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerMinRouteAdvertisementInterval.setStatus(_B)
if mibBuilder.loadTexts:axBgpPeerMinRouteAdvertisementInterval.setUnits(_E)
_AxBgpPeerInUpdateElapsedTime_Type=Gauge32
_AxBgpPeerInUpdateElapsedTime_Object=MibTableColumn
axBgpPeerInUpdateElapsedTime=_AxBgpPeerInUpdateElapsedTime_Object((1,3,6,1,4,1,22610,2,5,4,1,25),_AxBgpPeerInUpdateElapsedTime_Type())
axBgpPeerInUpdateElapsedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerInUpdateElapsedTime.setStatus(_B)
if mibBuilder.loadTexts:axBgpPeerInUpdateElapsedTime.setUnits(_E)
_AxBgpPeerMaxPrefixLimit_Type=Gauge32
_AxBgpPeerMaxPrefixLimit_Object=MibTableColumn
axBgpPeerMaxPrefixLimit=_AxBgpPeerMaxPrefixLimit_Object((1,3,6,1,4,1,22610,2,5,4,1,26),_AxBgpPeerMaxPrefixLimit_Type())
axBgpPeerMaxPrefixLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerMaxPrefixLimit.setStatus(_B)
class _AxBgpPeerThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_AxBgpPeerThreshold_Type.__name__=_D
_AxBgpPeerThreshold_Object=MibTableColumn
axBgpPeerThreshold=_AxBgpPeerThreshold_Object((1,3,6,1,4,1,22610,2,5,4,1,27),_AxBgpPeerThreshold_Type())
axBgpPeerThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPeerThreshold.setStatus(_B)
if mibBuilder.loadTexts:axBgpPeerThreshold.setUnits('percent')
_AxBgpPathAttrTable_Object=MibTable
axBgpPathAttrTable=_AxBgpPathAttrTable_Object((1,3,6,1,4,1,22610,2,5,5))
if mibBuilder.loadTexts:axBgpPathAttrTable.setStatus(_B)
_AxBgpPathAttrEntry_Object=MibTableRow
axBgpPathAttrEntry=_AxBgpPathAttrEntry_Object((1,3,6,1,4,1,22610,2,5,5,1))
axBgpPathAttrEntry.setIndexNames((0,_A,_N),(0,_A,_O),(0,_A,_P),(0,_A,_Q),(0,_A,_R))
if mibBuilder.loadTexts:axBgpPathAttrEntry.setStatus(_B)
_AxBgpPathAttrIpAddrType_Type=InetAddressType
_AxBgpPathAttrIpAddrType_Object=MibTableColumn
axBgpPathAttrIpAddrType=_AxBgpPathAttrIpAddrType_Object((1,3,6,1,4,1,22610,2,5,5,1,1),_AxBgpPathAttrIpAddrType_Type())
axBgpPathAttrIpAddrType.setMaxAccess(_M)
if mibBuilder.loadTexts:axBgpPathAttrIpAddrType.setStatus(_B)
_AxBgpPathAttrPeerType_Type=InetAddress
_AxBgpPathAttrPeerType_Object=MibTableColumn
axBgpPathAttrPeerType=_AxBgpPathAttrPeerType_Object((1,3,6,1,4,1,22610,2,5,5,1,2),_AxBgpPathAttrPeerType_Type())
axBgpPathAttrPeerType.setMaxAccess(_M)
if mibBuilder.loadTexts:axBgpPathAttrPeerType.setStatus(_B)
_AxBgpPathAttrPeer_Type=InetAddress
_AxBgpPathAttrPeer_Object=MibTableColumn
axBgpPathAttrPeer=_AxBgpPathAttrPeer_Object((1,3,6,1,4,1,22610,2,5,5,1,3),_AxBgpPathAttrPeer_Type())
axBgpPathAttrPeer.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPathAttrPeer.setStatus(_B)
_AxBgpPathAttrIpAddrPrefixLen_Type=InetAddressPrefixLength
_AxBgpPathAttrIpAddrPrefixLen_Object=MibTableColumn
axBgpPathAttrIpAddrPrefixLen=_AxBgpPathAttrIpAddrPrefixLen_Object((1,3,6,1,4,1,22610,2,5,5,1,4),_AxBgpPathAttrIpAddrPrefixLen_Type())
axBgpPathAttrIpAddrPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPathAttrIpAddrPrefixLen.setStatus(_B)
_AxBgpPathAttrIpAddrPrefix_Type=InetAddress
_AxBgpPathAttrIpAddrPrefix_Object=MibTableColumn
axBgpPathAttrIpAddrPrefix=_AxBgpPathAttrIpAddrPrefix_Object((1,3,6,1,4,1,22610,2,5,5,1,5),_AxBgpPathAttrIpAddrPrefix_Type())
axBgpPathAttrIpAddrPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPathAttrIpAddrPrefix.setStatus(_B)
class _AxBgpPathAttrOrigin_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('igp',1),('egp',2),('incomplete',3)))
_AxBgpPathAttrOrigin_Type.__name__=_D
_AxBgpPathAttrOrigin_Object=MibTableColumn
axBgpPathAttrOrigin=_AxBgpPathAttrOrigin_Object((1,3,6,1,4,1,22610,2,5,5,1,6),_AxBgpPathAttrOrigin_Type())
axBgpPathAttrOrigin.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPathAttrOrigin.setStatus(_B)
class _AxBgpPathAttrASPathSegment_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,255))
_AxBgpPathAttrASPathSegment_Type.__name__=_G
_AxBgpPathAttrASPathSegment_Object=MibTableColumn
axBgpPathAttrASPathSegment=_AxBgpPathAttrASPathSegment_Object((1,3,6,1,4,1,22610,2,5,5,1,7),_AxBgpPathAttrASPathSegment_Type())
axBgpPathAttrASPathSegment.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPathAttrASPathSegment.setStatus(_B)
_AxBgpPathAttrNextHopType_Type=InetAddressType
_AxBgpPathAttrNextHopType_Object=MibTableColumn
axBgpPathAttrNextHopType=_AxBgpPathAttrNextHopType_Object((1,3,6,1,4,1,22610,2,5,5,1,8),_AxBgpPathAttrNextHopType_Type())
axBgpPathAttrNextHopType.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPathAttrNextHopType.setStatus(_B)
_AxBgpPathAttrNextHop_Type=InetAddress
_AxBgpPathAttrNextHop_Object=MibTableColumn
axBgpPathAttrNextHop=_AxBgpPathAttrNextHop_Object((1,3,6,1,4,1,22610,2,5,5,1,9),_AxBgpPathAttrNextHop_Type())
axBgpPathAttrNextHop.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPathAttrNextHop.setStatus(_B)
class _AxBgpPathAttrMultiExitDisc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AxBgpPathAttrMultiExitDisc_Type.__name__=_D
_AxBgpPathAttrMultiExitDisc_Object=MibTableColumn
axBgpPathAttrMultiExitDisc=_AxBgpPathAttrMultiExitDisc_Object((1,3,6,1,4,1,22610,2,5,5,1,10),_AxBgpPathAttrMultiExitDisc_Type())
axBgpPathAttrMultiExitDisc.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPathAttrMultiExitDisc.setStatus(_B)
class _AxBgpPathAttrLocalPref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AxBgpPathAttrLocalPref_Type.__name__=_D
_AxBgpPathAttrLocalPref_Object=MibTableColumn
axBgpPathAttrLocalPref=_AxBgpPathAttrLocalPref_Object((1,3,6,1,4,1,22610,2,5,5,1,11),_AxBgpPathAttrLocalPref_Type())
axBgpPathAttrLocalPref.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPathAttrLocalPref.setStatus(_B)
class _AxBgpPathAttrAtomicAggregate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lessSpecificRouteNotSelected',1),('lessSpecificRouteSelected',2)))
_AxBgpPathAttrAtomicAggregate_Type.__name__=_D
_AxBgpPathAttrAtomicAggregate_Object=MibTableColumn
axBgpPathAttrAtomicAggregate=_AxBgpPathAttrAtomicAggregate_Object((1,3,6,1,4,1,22610,2,5,5,1,12),_AxBgpPathAttrAtomicAggregate_Type())
axBgpPathAttrAtomicAggregate.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPathAttrAtomicAggregate.setStatus(_B)
class _AxBgpPathAttrAggregatorAS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AxBgpPathAttrAggregatorAS_Type.__name__=_D
_AxBgpPathAttrAggregatorAS_Object=MibTableColumn
axBgpPathAttrAggregatorAS=_AxBgpPathAttrAggregatorAS_Object((1,3,6,1,4,1,22610,2,5,5,1,13),_AxBgpPathAttrAggregatorAS_Type())
axBgpPathAttrAggregatorAS.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPathAttrAggregatorAS.setStatus(_B)
_AxBgpPathAttrAggregatorAddr_Type=IpAddress
_AxBgpPathAttrAggregatorAddr_Object=MibTableColumn
axBgpPathAttrAggregatorAddr=_AxBgpPathAttrAggregatorAddr_Object((1,3,6,1,4,1,22610,2,5,5,1,14),_AxBgpPathAttrAggregatorAddr_Type())
axBgpPathAttrAggregatorAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPathAttrAggregatorAddr.setStatus(_B)
class _AxBgpPathAttrCalcLocalPref_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,2147483647))
_AxBgpPathAttrCalcLocalPref_Type.__name__=_D
_AxBgpPathAttrCalcLocalPref_Object=MibTableColumn
axBgpPathAttrCalcLocalPref=_AxBgpPathAttrCalcLocalPref_Object((1,3,6,1,4,1,22610,2,5,5,1,15),_AxBgpPathAttrCalcLocalPref_Type())
axBgpPathAttrCalcLocalPref.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPathAttrCalcLocalPref.setStatus(_B)
class _AxBgpPathAttrBest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('false',1),('true',2)))
_AxBgpPathAttrBest_Type.__name__=_D
_AxBgpPathAttrBest_Object=MibTableColumn
axBgpPathAttrBest=_AxBgpPathAttrBest_Object((1,3,6,1,4,1,22610,2,5,5,1,16),_AxBgpPathAttrBest_Type())
axBgpPathAttrBest.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPathAttrBest.setStatus(_B)
class _AxBgpPathAttrUnknown_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_AxBgpPathAttrUnknown_Type.__name__=_G
_AxBgpPathAttrUnknown_Object=MibTableColumn
axBgpPathAttrUnknown=_AxBgpPathAttrUnknown_Object((1,3,6,1,4,1,22610,2,5,5,1,17),_AxBgpPathAttrUnknown_Type())
axBgpPathAttrUnknown.setMaxAccess(_C)
if mibBuilder.loadTexts:axBgpPathAttrUnknown.setStatus(_B)
_AxBgpMIBConformance_ObjectIdentity=ObjectIdentity
axBgpMIBConformance=_AxBgpMIBConformance_ObjectIdentity((1,3,6,1,4,1,22610,2,5,8))
_AxBgpMIBCompliances_ObjectIdentity=ObjectIdentity
axBgpMIBCompliances=_AxBgpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,22610,2,5,8,1))
_AxBgpMIBGroups_ObjectIdentity=ObjectIdentity
axBgpMIBGroups=_AxBgpMIBGroups_ObjectIdentity((1,3,6,1,4,1,22610,2,5,8,2))
axBgpMIBGlobalsGroup=ObjectGroup((1,3,6,1,4,1,22610,2,5,8,2,1))
axBgpMIBGlobalsGroup.setObjects(*((_A,_S),(_A,_T),(_A,_U)))
if mibBuilder.loadTexts:axBgpMIBGlobalsGroup.setStatus(_B)
axBgpMIBPeerGroup=ObjectGroup((1,3,6,1,4,1,22610,2,5,8,2,2))
axBgpMIBPeerGroup.setObjects(*((_A,_L),(_A,_V),(_A,_H),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_F),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_I),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:axBgpMIBPeerGroup.setStatus(_B)
axBgpMIBPathAttrGroup=ObjectGroup((1,3,6,1,4,1,22610,2,5,8,2,3))
axBgpMIBPathAttrGroup.setObjects(*((_A,_N),(_A,_Q),(_A,_R),(_A,_P),(_A,_O),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:axBgpMIBPathAttrGroup.setStatus(_B)
axBgpEstablishedNotification=NotificationType((1,3,6,1,4,1,22610,2,5,0,1))
axBgpEstablishedNotification.setObjects(*((_A,_F),(_A,_I),(_A,_H)))
if mibBuilder.loadTexts:axBgpEstablishedNotification.setStatus(_B)
axBgpBackwardTransNotification=NotificationType((1,3,6,1,4,1,22610,2,5,0,2))
axBgpBackwardTransNotification.setObjects(*((_A,_F),(_A,_I),(_A,_H)))
if mibBuilder.loadTexts:axBgpBackwardTransNotification.setStatus(_B)
axBgpPrefixThresholdExceededNotification=NotificationType((1,3,6,1,4,1,22610,2,5,0,3))
axBgpPrefixThresholdExceededNotification.setObjects(*((_A,_F),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:axBgpPrefixThresholdExceededNotification.setStatus(_B)
axBgpPrefixThresholdClearNotification=NotificationType((1,3,6,1,4,1,22610,2,5,0,4))
axBgpPrefixThresholdClearNotification.setObjects(*((_A,_F),(_A,_J),(_A,_K)))
if mibBuilder.loadTexts:axBgpPrefixThresholdClearNotification.setStatus(_B)
axBgpMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,22610,2,5,8,2,4))
axBgpMIBNotificationGroup.setObjects(*((_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:axBgpMIBNotificationGroup.setStatus(_B)
axBgpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,22610,2,5,8,1,1))
axBgpMIBCompliance.setObjects(*((_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:axBgpMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'axBgpMIB':axBgpMIB,'axBgpNotification':axBgpNotification,_A2:axBgpEstablishedNotification,_A3:axBgpBackwardTransNotification,_A4:axBgpPrefixThresholdExceededNotification,_A5:axBgpPrefixThresholdClearNotification,_S:axBgpVersion,_T:axBgpLocalAs,_U:axBgpIdentifier,'axBgpPeerTable':axBgpPeerTable,'axBgpPeerEntry':axBgpPeerEntry,_L:axBgpPeerType,_V:axBgpPeerIdentifier,_H:axBgpPeerState,_W:axBgpPeerAdminStatus,_X:axBgpPeerNegotiatedVersion,_Y:axBgpPeerLocalAddr,_Z:axBgpPeerLocalPort,_F:axBgpPeerRemoteAddr,_a:axBgpPeerRemotePort,_b:axBgpPeerRemoteAs,_c:axBgpPeerInUpdates,_d:axBgpPeerOutUpdates,_e:axBgpPeerInTotalMessages,_f:axBgpPeerOutTotalMessages,_I:axBgpPeerLastError,_g:axBgpPeerFsmEstablishedTransitions,_h:axBgpPeerFsmEstablishedTime,_i:axBgpPeerConnectRetryInterval,_j:axBgpPeerHoldTime,_k:axBgpPeerKeepAlive,_l:axBgpPeerHoldTimeConfigured,_m:axBgpPeerKeepAliveConfigured,_n:axBgpPeerMinASOriginationInterval,_o:axBgpPeerMinRouteAdvertisementInterval,_p:axBgpPeerInUpdateElapsedTime,_J:axBgpPeerMaxPrefixLimit,_K:axBgpPeerThreshold,'axBgpPathAttrTable':axBgpPathAttrTable,'axBgpPathAttrEntry':axBgpPathAttrEntry,_N:axBgpPathAttrIpAddrType,_Q:axBgpPathAttrPeerType,_R:axBgpPathAttrPeer,_P:axBgpPathAttrIpAddrPrefixLen,_O:axBgpPathAttrIpAddrPrefix,_q:axBgpPathAttrOrigin,_r:axBgpPathAttrASPathSegment,_s:axBgpPathAttrNextHopType,_t:axBgpPathAttrNextHop,_u:axBgpPathAttrMultiExitDisc,_v:axBgpPathAttrLocalPref,_w:axBgpPathAttrAtomicAggregate,_x:axBgpPathAttrAggregatorAS,_y:axBgpPathAttrAggregatorAddr,_z:axBgpPathAttrCalcLocalPref,_A0:axBgpPathAttrBest,_A1:axBgpPathAttrUnknown,'axBgpMIBConformance':axBgpMIBConformance,'axBgpMIBCompliances':axBgpMIBCompliances,'axBgpMIBCompliance':axBgpMIBCompliance,'axBgpMIBGroups':axBgpMIBGroups,_A6:axBgpMIBGlobalsGroup,_A7:axBgpMIBPeerGroup,_A8:axBgpMIBPathAttrGroup,_A9:axBgpMIBNotificationGroup})