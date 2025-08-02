_AM='msdpMIBRequestsGroup'
_AL='msdpMIBNotificationGroup'
_AK='msdpMIBPeerGroup'
_AJ='msdpBackwardTransition'
_AI='msdpEstablished'
_AH='msdpMeshGroupStatus'
_AG='msdpRPAddress'
_AF='msdpRequestsStatus'
_AE='msdpRequestsPeer'
_AD='msdpSACacheStatus'
_AC='msdpSACacheExpiryTime'
_AB='msdpSACacheUpTime'
_AA='msdpSACacheInDataPackets'
_A9='msdpSACacheInSAs'
_A8='msdpSACacheRPFPeer'
_A7='msdpSACachePeerLearnedFrom'
_A6='msdpNumSACacheEntries'
_A5='msdpCacheLifetime'
_A4='msdpPeerEncapsulationType'
_A3='msdpPeerDataTtl'
_A2='msdpPeerOutDataPackets'
_A1='msdpPeerInDataPackets'
_A0='msdpPeerLastError'
_z='msdpPeerProcessRequestsFrom'
_y='msdpPeerOutNotifications'
_x='msdpPeerInNotifications'
_w='msdpPeerOutSAResponses'
_v='msdpPeerInSAResponses'
_u='msdpEnabled'
_t='msdpMeshGroupPeerAddress'
_s='msdpMeshGroupName'
_r='msdpSACacheOriginRP'
_q='msdpSACacheSourceAddr'
_p='msdpSACacheGroupAddr'
_o='msdpPeerRemoteAddress'
_n='msdpRequestsGroupMask'
_m='msdpRequestsGroupAddress'
_l='RowStatus'
_k='DisplayString'
_j='OctetString'
_i='msdpMIBPeerGroup2'
_h='msdpPeerDiscontinuityTime'
_g='msdpPeerStatus'
_f='msdpPeerConnectionAttempts'
_e='msdpPeerInMessageTime'
_d='msdpPeerKeepAliveConfigured'
_c='msdpPeerHoldTimeConfigured'
_b='msdpPeerConnectRetryInterval'
_a='msdpPeerLocalPort'
_Z='msdpPeerRemotePort'
_Y='msdpPeerLocalAddress'
_X='msdpPeerFsmEstablishedTime'
_W='msdpPeerOutControlMessages'
_V='msdpPeerInControlMessages'
_U='msdpPeerOutSARequests'
_T='msdpPeerInSARequests'
_S='msdpPeerOutSAs'
_R='msdpPeerInSAs'
_Q='msdpPeerRPFFailures'
_P='seconds'
_O='msdpMIBMeshGroupGroup'
_N='msdpMIBRPGroup'
_M='msdpMIBSACacheGroup'
_L='msdpMIBEncapsulationGroup'
_K='msdpMIBGlobalsGroup'
_J='msdpPeerFsmEstablishedTransitions'
_I='msdpPeerState'
_H='read-write'
_G='not-accessible'
_F='Integer32'
_E='read-create'
_D='deprecated'
_C='read-only'
_B='current'
_A='MSDP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_j,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','experimental','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_k,'PhysAddress',_l,'TextualConvention','TimeStamp','TruthValue')
msdpMIB=ModuleIdentity((1,3,6,1,3,92))
if mibBuilder.loadTexts:msdpMIB.setRevisions(('2006-08-01 00:00',))
_MsdpMIBobjects_ObjectIdentity=ObjectIdentity
msdpMIBobjects=_MsdpMIBobjects_ObjectIdentity((1,3,6,1,3,92,1))
_Msdp_ObjectIdentity=ObjectIdentity
msdp=_Msdp_ObjectIdentity((1,3,6,1,3,92,1,1))
_MsdpTraps_ObjectIdentity=ObjectIdentity
msdpTraps=_MsdpTraps_ObjectIdentity((1,3,6,1,3,92,1,1,0))
_MsdpEnabled_Type=TruthValue
_MsdpEnabled_Object=MibScalar
msdpEnabled=_MsdpEnabled_Object((1,3,6,1,3,92,1,1,1),_MsdpEnabled_Type())
msdpEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:msdpEnabled.setStatus(_B)
_MsdpCacheLifetime_Type=TimeTicks
_MsdpCacheLifetime_Object=MibScalar
msdpCacheLifetime=_MsdpCacheLifetime_Object((1,3,6,1,3,92,1,1,2),_MsdpCacheLifetime_Type())
msdpCacheLifetime.setMaxAccess(_H)
if mibBuilder.loadTexts:msdpCacheLifetime.setStatus(_B)
_MsdpNumSACacheEntries_Type=Gauge32
_MsdpNumSACacheEntries_Object=MibScalar
msdpNumSACacheEntries=_MsdpNumSACacheEntries_Object((1,3,6,1,3,92,1,1,3),_MsdpNumSACacheEntries_Type())
msdpNumSACacheEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpNumSACacheEntries.setStatus(_B)
_MsdpRequestsTable_Object=MibTable
msdpRequestsTable=_MsdpRequestsTable_Object((1,3,6,1,3,92,1,1,4))
if mibBuilder.loadTexts:msdpRequestsTable.setStatus(_D)
_MsdpRequestsEntry_Object=MibTableRow
msdpRequestsEntry=_MsdpRequestsEntry_Object((1,3,6,1,3,92,1,1,4,1))
msdpRequestsEntry.setIndexNames((0,_A,_m),(0,_A,_n))
if mibBuilder.loadTexts:msdpRequestsEntry.setStatus(_D)
_MsdpRequestsGroupAddress_Type=IpAddress
_MsdpRequestsGroupAddress_Object=MibTableColumn
msdpRequestsGroupAddress=_MsdpRequestsGroupAddress_Object((1,3,6,1,3,92,1,1,4,1,1),_MsdpRequestsGroupAddress_Type())
msdpRequestsGroupAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:msdpRequestsGroupAddress.setStatus(_D)
_MsdpRequestsGroupMask_Type=IpAddress
_MsdpRequestsGroupMask_Object=MibTableColumn
msdpRequestsGroupMask=_MsdpRequestsGroupMask_Object((1,3,6,1,3,92,1,1,4,1,2),_MsdpRequestsGroupMask_Type())
msdpRequestsGroupMask.setMaxAccess(_G)
if mibBuilder.loadTexts:msdpRequestsGroupMask.setStatus(_D)
_MsdpRequestsPeer_Type=IpAddress
_MsdpRequestsPeer_Object=MibTableColumn
msdpRequestsPeer=_MsdpRequestsPeer_Object((1,3,6,1,3,92,1,1,4,1,3),_MsdpRequestsPeer_Type())
msdpRequestsPeer.setMaxAccess(_E)
if mibBuilder.loadTexts:msdpRequestsPeer.setStatus(_D)
_MsdpRequestsStatus_Type=RowStatus
_MsdpRequestsStatus_Object=MibTableColumn
msdpRequestsStatus=_MsdpRequestsStatus_Object((1,3,6,1,3,92,1,1,4,1,4),_MsdpRequestsStatus_Type())
msdpRequestsStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:msdpRequestsStatus.setStatus(_D)
_MsdpPeerTable_Object=MibTable
msdpPeerTable=_MsdpPeerTable_Object((1,3,6,1,3,92,1,1,5))
if mibBuilder.loadTexts:msdpPeerTable.setStatus(_B)
_MsdpPeerEntry_Object=MibTableRow
msdpPeerEntry=_MsdpPeerEntry_Object((1,3,6,1,3,92,1,1,5,1))
msdpPeerEntry.setIndexNames((0,_A,_o))
if mibBuilder.loadTexts:msdpPeerEntry.setStatus(_B)
_MsdpPeerRemoteAddress_Type=IpAddress
_MsdpPeerRemoteAddress_Object=MibTableColumn
msdpPeerRemoteAddress=_MsdpPeerRemoteAddress_Object((1,3,6,1,3,92,1,1,5,1,1),_MsdpPeerRemoteAddress_Type())
msdpPeerRemoteAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:msdpPeerRemoteAddress.setStatus(_B)
class _MsdpPeerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('inactive',1),('listen',2),('connecting',3),('established',4),('disabled',5)))
_MsdpPeerState_Type.__name__=_F
_MsdpPeerState_Object=MibTableColumn
msdpPeerState=_MsdpPeerState_Object((1,3,6,1,3,92,1,1,5,1,3),_MsdpPeerState_Type())
msdpPeerState.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerState.setStatus(_B)
_MsdpPeerRPFFailures_Type=Counter32
_MsdpPeerRPFFailures_Object=MibTableColumn
msdpPeerRPFFailures=_MsdpPeerRPFFailures_Object((1,3,6,1,3,92,1,1,5,1,4),_MsdpPeerRPFFailures_Type())
msdpPeerRPFFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerRPFFailures.setStatus(_B)
_MsdpPeerInSAs_Type=Counter32
_MsdpPeerInSAs_Object=MibTableColumn
msdpPeerInSAs=_MsdpPeerInSAs_Object((1,3,6,1,3,92,1,1,5,1,5),_MsdpPeerInSAs_Type())
msdpPeerInSAs.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerInSAs.setStatus(_B)
_MsdpPeerOutSAs_Type=Counter32
_MsdpPeerOutSAs_Object=MibTableColumn
msdpPeerOutSAs=_MsdpPeerOutSAs_Object((1,3,6,1,3,92,1,1,5,1,6),_MsdpPeerOutSAs_Type())
msdpPeerOutSAs.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerOutSAs.setStatus(_B)
_MsdpPeerInSARequests_Type=Counter32
_MsdpPeerInSARequests_Object=MibTableColumn
msdpPeerInSARequests=_MsdpPeerInSARequests_Object((1,3,6,1,3,92,1,1,5,1,7),_MsdpPeerInSARequests_Type())
msdpPeerInSARequests.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerInSARequests.setStatus(_B)
_MsdpPeerOutSARequests_Type=Counter32
_MsdpPeerOutSARequests_Object=MibTableColumn
msdpPeerOutSARequests=_MsdpPeerOutSARequests_Object((1,3,6,1,3,92,1,1,5,1,8),_MsdpPeerOutSARequests_Type())
msdpPeerOutSARequests.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerOutSARequests.setStatus(_B)
_MsdpPeerInSAResponses_Type=Counter32
_MsdpPeerInSAResponses_Object=MibTableColumn
msdpPeerInSAResponses=_MsdpPeerInSAResponses_Object((1,3,6,1,3,92,1,1,5,1,9),_MsdpPeerInSAResponses_Type())
msdpPeerInSAResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerInSAResponses.setStatus(_D)
_MsdpPeerOutSAResponses_Type=Counter32
_MsdpPeerOutSAResponses_Object=MibTableColumn
msdpPeerOutSAResponses=_MsdpPeerOutSAResponses_Object((1,3,6,1,3,92,1,1,5,1,10),_MsdpPeerOutSAResponses_Type())
msdpPeerOutSAResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerOutSAResponses.setStatus(_D)
_MsdpPeerInControlMessages_Type=Counter32
_MsdpPeerInControlMessages_Object=MibTableColumn
msdpPeerInControlMessages=_MsdpPeerInControlMessages_Object((1,3,6,1,3,92,1,1,5,1,11),_MsdpPeerInControlMessages_Type())
msdpPeerInControlMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerInControlMessages.setStatus(_B)
_MsdpPeerOutControlMessages_Type=Counter32
_MsdpPeerOutControlMessages_Object=MibTableColumn
msdpPeerOutControlMessages=_MsdpPeerOutControlMessages_Object((1,3,6,1,3,92,1,1,5,1,12),_MsdpPeerOutControlMessages_Type())
msdpPeerOutControlMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerOutControlMessages.setStatus(_B)
_MsdpPeerInDataPackets_Type=Counter32
_MsdpPeerInDataPackets_Object=MibTableColumn
msdpPeerInDataPackets=_MsdpPeerInDataPackets_Object((1,3,6,1,3,92,1,1,5,1,13),_MsdpPeerInDataPackets_Type())
msdpPeerInDataPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerInDataPackets.setStatus(_B)
_MsdpPeerOutDataPackets_Type=Counter32
_MsdpPeerOutDataPackets_Object=MibTableColumn
msdpPeerOutDataPackets=_MsdpPeerOutDataPackets_Object((1,3,6,1,3,92,1,1,5,1,14),_MsdpPeerOutDataPackets_Type())
msdpPeerOutDataPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerOutDataPackets.setStatus(_B)
_MsdpPeerFsmEstablishedTransitions_Type=Counter32
_MsdpPeerFsmEstablishedTransitions_Object=MibTableColumn
msdpPeerFsmEstablishedTransitions=_MsdpPeerFsmEstablishedTransitions_Object((1,3,6,1,3,92,1,1,5,1,15),_MsdpPeerFsmEstablishedTransitions_Type())
msdpPeerFsmEstablishedTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerFsmEstablishedTransitions.setStatus(_B)
_MsdpPeerFsmEstablishedTime_Type=TimeStamp
_MsdpPeerFsmEstablishedTime_Object=MibTableColumn
msdpPeerFsmEstablishedTime=_MsdpPeerFsmEstablishedTime_Object((1,3,6,1,3,92,1,1,5,1,16),_MsdpPeerFsmEstablishedTime_Type())
msdpPeerFsmEstablishedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerFsmEstablishedTime.setStatus(_B)
_MsdpPeerInMessageTime_Type=TimeStamp
_MsdpPeerInMessageTime_Object=MibTableColumn
msdpPeerInMessageTime=_MsdpPeerInMessageTime_Object((1,3,6,1,3,92,1,1,5,1,17),_MsdpPeerInMessageTime_Type())
msdpPeerInMessageTime.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerInMessageTime.setStatus(_B)
_MsdpPeerLocalAddress_Type=IpAddress
_MsdpPeerLocalAddress_Object=MibTableColumn
msdpPeerLocalAddress=_MsdpPeerLocalAddress_Object((1,3,6,1,3,92,1,1,5,1,18),_MsdpPeerLocalAddress_Type())
msdpPeerLocalAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:msdpPeerLocalAddress.setStatus(_B)
class _MsdpPeerConnectRetryInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_MsdpPeerConnectRetryInterval_Type.__name__=_F
_MsdpPeerConnectRetryInterval_Object=MibTableColumn
msdpPeerConnectRetryInterval=_MsdpPeerConnectRetryInterval_Object((1,3,6,1,3,92,1,1,5,1,20),_MsdpPeerConnectRetryInterval_Type())
msdpPeerConnectRetryInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:msdpPeerConnectRetryInterval.setStatus(_B)
if mibBuilder.loadTexts:msdpPeerConnectRetryInterval.setUnits(_P)
class _MsdpPeerHoldTimeConfigured_Type(Integer32):defaultValue=75;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_MsdpPeerHoldTimeConfigured_Type.__name__=_F
_MsdpPeerHoldTimeConfigured_Object=MibTableColumn
msdpPeerHoldTimeConfigured=_MsdpPeerHoldTimeConfigured_Object((1,3,6,1,3,92,1,1,5,1,21),_MsdpPeerHoldTimeConfigured_Type())
msdpPeerHoldTimeConfigured.setMaxAccess(_E)
if mibBuilder.loadTexts:msdpPeerHoldTimeConfigured.setStatus(_B)
if mibBuilder.loadTexts:msdpPeerHoldTimeConfigured.setUnits(_P)
class _MsdpPeerKeepAliveConfigured_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_MsdpPeerKeepAliveConfigured_Type.__name__=_F
_MsdpPeerKeepAliveConfigured_Object=MibTableColumn
msdpPeerKeepAliveConfigured=_MsdpPeerKeepAliveConfigured_Object((1,3,6,1,3,92,1,1,5,1,22),_MsdpPeerKeepAliveConfigured_Type())
msdpPeerKeepAliveConfigured.setMaxAccess(_E)
if mibBuilder.loadTexts:msdpPeerKeepAliveConfigured.setStatus(_B)
if mibBuilder.loadTexts:msdpPeerKeepAliveConfigured.setUnits(_P)
class _MsdpPeerDataTtl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsdpPeerDataTtl_Type.__name__=_F
_MsdpPeerDataTtl_Object=MibTableColumn
msdpPeerDataTtl=_MsdpPeerDataTtl_Object((1,3,6,1,3,92,1,1,5,1,23),_MsdpPeerDataTtl_Type())
msdpPeerDataTtl.setMaxAccess(_E)
if mibBuilder.loadTexts:msdpPeerDataTtl.setStatus(_B)
_MsdpPeerProcessRequestsFrom_Type=TruthValue
_MsdpPeerProcessRequestsFrom_Object=MibTableColumn
msdpPeerProcessRequestsFrom=_MsdpPeerProcessRequestsFrom_Object((1,3,6,1,3,92,1,1,5,1,24),_MsdpPeerProcessRequestsFrom_Type())
msdpPeerProcessRequestsFrom.setMaxAccess(_E)
if mibBuilder.loadTexts:msdpPeerProcessRequestsFrom.setStatus(_D)
_MsdpPeerStatus_Type=RowStatus
_MsdpPeerStatus_Object=MibTableColumn
msdpPeerStatus=_MsdpPeerStatus_Object((1,3,6,1,3,92,1,1,5,1,25),_MsdpPeerStatus_Type())
msdpPeerStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:msdpPeerStatus.setStatus(_B)
class _MsdpPeerRemotePort_Type(Integer32):defaultValue=639;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MsdpPeerRemotePort_Type.__name__=_F
_MsdpPeerRemotePort_Object=MibTableColumn
msdpPeerRemotePort=_MsdpPeerRemotePort_Object((1,3,6,1,3,92,1,1,5,1,26),_MsdpPeerRemotePort_Type())
msdpPeerRemotePort.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerRemotePort.setStatus(_B)
class _MsdpPeerLocalPort_Type(Integer32):defaultValue=639;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MsdpPeerLocalPort_Type.__name__=_F
_MsdpPeerLocalPort_Object=MibTableColumn
msdpPeerLocalPort=_MsdpPeerLocalPort_Object((1,3,6,1,3,92,1,1,5,1,27),_MsdpPeerLocalPort_Type())
msdpPeerLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerLocalPort.setStatus(_B)
class _MsdpPeerEncapsulationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('none',0),('tcp',1)))
_MsdpPeerEncapsulationType_Type.__name__=_F
_MsdpPeerEncapsulationType_Object=MibTableColumn
msdpPeerEncapsulationType=_MsdpPeerEncapsulationType_Object((1,3,6,1,3,92,1,1,5,1,29),_MsdpPeerEncapsulationType_Type())
msdpPeerEncapsulationType.setMaxAccess(_E)
if mibBuilder.loadTexts:msdpPeerEncapsulationType.setStatus(_B)
_MsdpPeerConnectionAttempts_Type=Counter32
_MsdpPeerConnectionAttempts_Object=MibTableColumn
msdpPeerConnectionAttempts=_MsdpPeerConnectionAttempts_Object((1,3,6,1,3,92,1,1,5,1,30),_MsdpPeerConnectionAttempts_Type())
msdpPeerConnectionAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerConnectionAttempts.setStatus(_B)
_MsdpPeerInNotifications_Type=Counter32
_MsdpPeerInNotifications_Object=MibTableColumn
msdpPeerInNotifications=_MsdpPeerInNotifications_Object((1,3,6,1,3,92,1,1,5,1,31),_MsdpPeerInNotifications_Type())
msdpPeerInNotifications.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerInNotifications.setStatus(_D)
_MsdpPeerOutNotifications_Type=Counter32
_MsdpPeerOutNotifications_Object=MibTableColumn
msdpPeerOutNotifications=_MsdpPeerOutNotifications_Object((1,3,6,1,3,92,1,1,5,1,32),_MsdpPeerOutNotifications_Type())
msdpPeerOutNotifications.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerOutNotifications.setStatus(_D)
class _MsdpPeerLastError_Type(OctetString):defaultHexValue='0000';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_MsdpPeerLastError_Type.__name__=_j
_MsdpPeerLastError_Object=MibTableColumn
msdpPeerLastError=_MsdpPeerLastError_Object((1,3,6,1,3,92,1,1,5,1,33),_MsdpPeerLastError_Type())
msdpPeerLastError.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerLastError.setStatus(_D)
_MsdpPeerDiscontinuityTime_Type=TimeStamp
_MsdpPeerDiscontinuityTime_Object=MibTableColumn
msdpPeerDiscontinuityTime=_MsdpPeerDiscontinuityTime_Object((1,3,6,1,3,92,1,1,5,1,34),_MsdpPeerDiscontinuityTime_Type())
msdpPeerDiscontinuityTime.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerDiscontinuityTime.setStatus(_B)
_MsdpSACacheTable_Object=MibTable
msdpSACacheTable=_MsdpSACacheTable_Object((1,3,6,1,3,92,1,1,6))
if mibBuilder.loadTexts:msdpSACacheTable.setStatus(_B)
_MsdpSACacheEntry_Object=MibTableRow
msdpSACacheEntry=_MsdpSACacheEntry_Object((1,3,6,1,3,92,1,1,6,1))
msdpSACacheEntry.setIndexNames((0,_A,_p),(0,_A,_q),(0,_A,_r))
if mibBuilder.loadTexts:msdpSACacheEntry.setStatus(_B)
_MsdpSACacheGroupAddr_Type=IpAddress
_MsdpSACacheGroupAddr_Object=MibTableColumn
msdpSACacheGroupAddr=_MsdpSACacheGroupAddr_Object((1,3,6,1,3,92,1,1,6,1,1),_MsdpSACacheGroupAddr_Type())
msdpSACacheGroupAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:msdpSACacheGroupAddr.setStatus(_B)
_MsdpSACacheSourceAddr_Type=IpAddress
_MsdpSACacheSourceAddr_Object=MibTableColumn
msdpSACacheSourceAddr=_MsdpSACacheSourceAddr_Object((1,3,6,1,3,92,1,1,6,1,2),_MsdpSACacheSourceAddr_Type())
msdpSACacheSourceAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:msdpSACacheSourceAddr.setStatus(_B)
_MsdpSACacheOriginRP_Type=IpAddress
_MsdpSACacheOriginRP_Object=MibTableColumn
msdpSACacheOriginRP=_MsdpSACacheOriginRP_Object((1,3,6,1,3,92,1,1,6,1,3),_MsdpSACacheOriginRP_Type())
msdpSACacheOriginRP.setMaxAccess(_G)
if mibBuilder.loadTexts:msdpSACacheOriginRP.setStatus(_B)
_MsdpSACachePeerLearnedFrom_Type=IpAddress
_MsdpSACachePeerLearnedFrom_Object=MibTableColumn
msdpSACachePeerLearnedFrom=_MsdpSACachePeerLearnedFrom_Object((1,3,6,1,3,92,1,1,6,1,4),_MsdpSACachePeerLearnedFrom_Type())
msdpSACachePeerLearnedFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpSACachePeerLearnedFrom.setStatus(_B)
_MsdpSACacheRPFPeer_Type=IpAddress
_MsdpSACacheRPFPeer_Object=MibTableColumn
msdpSACacheRPFPeer=_MsdpSACacheRPFPeer_Object((1,3,6,1,3,92,1,1,6,1,5),_MsdpSACacheRPFPeer_Type())
msdpSACacheRPFPeer.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpSACacheRPFPeer.setStatus(_B)
_MsdpSACacheInSAs_Type=Counter32
_MsdpSACacheInSAs_Object=MibTableColumn
msdpSACacheInSAs=_MsdpSACacheInSAs_Object((1,3,6,1,3,92,1,1,6,1,6),_MsdpSACacheInSAs_Type())
msdpSACacheInSAs.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpSACacheInSAs.setStatus(_B)
_MsdpSACacheInDataPackets_Type=Counter32
_MsdpSACacheInDataPackets_Object=MibTableColumn
msdpSACacheInDataPackets=_MsdpSACacheInDataPackets_Object((1,3,6,1,3,92,1,1,6,1,7),_MsdpSACacheInDataPackets_Type())
msdpSACacheInDataPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpSACacheInDataPackets.setStatus(_B)
_MsdpSACacheUpTime_Type=TimeTicks
_MsdpSACacheUpTime_Object=MibTableColumn
msdpSACacheUpTime=_MsdpSACacheUpTime_Object((1,3,6,1,3,92,1,1,6,1,8),_MsdpSACacheUpTime_Type())
msdpSACacheUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpSACacheUpTime.setStatus(_B)
_MsdpSACacheExpiryTime_Type=TimeTicks
_MsdpSACacheExpiryTime_Object=MibTableColumn
msdpSACacheExpiryTime=_MsdpSACacheExpiryTime_Object((1,3,6,1,3,92,1,1,6,1,9),_MsdpSACacheExpiryTime_Type())
msdpSACacheExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpSACacheExpiryTime.setStatus(_B)
class _MsdpSACacheStatus_Type(RowStatus):subtypeSpec=RowStatus.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,6)));namedValues=NamedValues(*(('active',1),('destroy',6)))
_MsdpSACacheStatus_Type.__name__=_l
_MsdpSACacheStatus_Object=MibTableColumn
msdpSACacheStatus=_MsdpSACacheStatus_Object((1,3,6,1,3,92,1,1,6,1,10),_MsdpSACacheStatus_Type())
msdpSACacheStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:msdpSACacheStatus.setStatus(_B)
_MsdpMIBConformance_ObjectIdentity=ObjectIdentity
msdpMIBConformance=_MsdpMIBConformance_ObjectIdentity((1,3,6,1,3,92,1,1,8))
_MsdpMIBCompliances_ObjectIdentity=ObjectIdentity
msdpMIBCompliances=_MsdpMIBCompliances_ObjectIdentity((1,3,6,1,3,92,1,1,8,1))
_MsdpMIBGroups_ObjectIdentity=ObjectIdentity
msdpMIBGroups=_MsdpMIBGroups_ObjectIdentity((1,3,6,1,3,92,1,1,8,2))
_MsdpRPAddress_Type=IpAddress
_MsdpRPAddress_Object=MibScalar
msdpRPAddress=_MsdpRPAddress_Object((1,3,6,1,3,92,1,1,11),_MsdpRPAddress_Type())
msdpRPAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:msdpRPAddress.setStatus(_B)
_MsdpMeshGroupTable_Object=MibTable
msdpMeshGroupTable=_MsdpMeshGroupTable_Object((1,3,6,1,3,92,1,1,12))
if mibBuilder.loadTexts:msdpMeshGroupTable.setStatus(_B)
_MsdpMeshGroupEntry_Object=MibTableRow
msdpMeshGroupEntry=_MsdpMeshGroupEntry_Object((1,3,6,1,3,92,1,1,12,1))
msdpMeshGroupEntry.setIndexNames((0,_A,_s),(0,_A,_t))
if mibBuilder.loadTexts:msdpMeshGroupEntry.setStatus(_B)
class _MsdpMeshGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_MsdpMeshGroupName_Type.__name__=_k
_MsdpMeshGroupName_Object=MibTableColumn
msdpMeshGroupName=_MsdpMeshGroupName_Object((1,3,6,1,3,92,1,1,12,1,1),_MsdpMeshGroupName_Type())
msdpMeshGroupName.setMaxAccess(_G)
if mibBuilder.loadTexts:msdpMeshGroupName.setStatus(_B)
_MsdpMeshGroupPeerAddress_Type=IpAddress
_MsdpMeshGroupPeerAddress_Object=MibTableColumn
msdpMeshGroupPeerAddress=_MsdpMeshGroupPeerAddress_Object((1,3,6,1,3,92,1,1,12,1,2),_MsdpMeshGroupPeerAddress_Type())
msdpMeshGroupPeerAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:msdpMeshGroupPeerAddress.setStatus(_B)
_MsdpMeshGroupStatus_Type=RowStatus
_MsdpMeshGroupStatus_Object=MibTableColumn
msdpMeshGroupStatus=_MsdpMeshGroupStatus_Object((1,3,6,1,3,92,1,1,12,1,3),_MsdpMeshGroupStatus_Type())
msdpMeshGroupStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:msdpMeshGroupStatus.setStatus(_B)
msdpMIBGlobalsGroup=ObjectGroup((1,3,6,1,3,92,1,1,8,2,1))
msdpMIBGlobalsGroup.setObjects((_A,_u))
if mibBuilder.loadTexts:msdpMIBGlobalsGroup.setStatus(_B)
msdpMIBPeerGroup=ObjectGroup((1,3,6,1,3,92,1,1,8,2,2))
msdpMIBPeerGroup.setObjects(*((_A,_Q),(_A,_I),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_V),(_A,_W),(_A,_J),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_z),(_A,_f),(_A,_A0),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:msdpMIBPeerGroup.setStatus(_D)
msdpMIBEncapsulationGroup=ObjectGroup((1,3,6,1,3,92,1,1,8,2,3))
msdpMIBEncapsulationGroup.setObjects(*((_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:msdpMIBEncapsulationGroup.setStatus(_B)
msdpMIBSACacheGroup=ObjectGroup((1,3,6,1,3,92,1,1,8,2,4))
msdpMIBSACacheGroup.setObjects(*((_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD)))
if mibBuilder.loadTexts:msdpMIBSACacheGroup.setStatus(_B)
msdpMIBRequestsGroup=ObjectGroup((1,3,6,1,3,92,1,1,8,2,6))
msdpMIBRequestsGroup.setObjects(*((_A,_AE),(_A,_AF)))
if mibBuilder.loadTexts:msdpMIBRequestsGroup.setStatus(_D)
msdpMIBRPGroup=ObjectGroup((1,3,6,1,3,92,1,1,8,2,7))
msdpMIBRPGroup.setObjects((_A,_AG))
if mibBuilder.loadTexts:msdpMIBRPGroup.setStatus(_B)
msdpMIBMeshGroupGroup=ObjectGroup((1,3,6,1,3,92,1,1,8,2,8))
msdpMIBMeshGroupGroup.setObjects((_A,_AH))
if mibBuilder.loadTexts:msdpMIBMeshGroupGroup.setStatus(_B)
msdpMIBPeerGroup2=ObjectGroup((1,3,6,1,3,92,1,1,8,2,9))
msdpMIBPeerGroup2.setObjects(*((_A,_Q),(_A,_I),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_J),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:msdpMIBPeerGroup2.setStatus(_B)
msdpEstablished=NotificationType((1,3,6,1,3,92,1,1,0,1))
msdpEstablished.setObjects((_A,_J))
if mibBuilder.loadTexts:msdpEstablished.setStatus(_B)
msdpBackwardTransition=NotificationType((1,3,6,1,3,92,1,1,0,2))
msdpBackwardTransition.setObjects((_A,_I))
if mibBuilder.loadTexts:msdpBackwardTransition.setStatus(_B)
msdpMIBNotificationGroup=NotificationGroup((1,3,6,1,3,92,1,1,8,2,5))
msdpMIBNotificationGroup.setObjects(*((_A,_AI),(_A,_AJ)))
if mibBuilder.loadTexts:msdpMIBNotificationGroup.setStatus(_B)
msdpMIBCompliance=ModuleCompliance((1,3,6,1,3,92,1,1,8,1,1))
msdpMIBCompliance.setObjects(*((_A,_K),(_A,_AK),(_A,_AL),(_A,_L),(_A,_M),(_A,_AM),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:msdpMIBCompliance.setStatus(_D)
msdpMIBFullCompliance=ModuleCompliance((1,3,6,1,3,92,1,1,8,1,2))
msdpMIBFullCompliance.setObjects(*((_A,_K),(_A,_i),(_A,_M),(_A,_L),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:msdpMIBFullCompliance.setStatus(_B)
msdpMIBReadOnlyCompliance=ModuleCompliance((1,3,6,1,3,92,1,1,8,1,3))
msdpMIBReadOnlyCompliance.setObjects(*((_A,_K),(_A,_i),(_A,_M),(_A,_L),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:msdpMIBReadOnlyCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'msdpMIB':msdpMIB,'msdpMIBobjects':msdpMIBobjects,'msdp':msdp,'msdpTraps':msdpTraps,_AI:msdpEstablished,_AJ:msdpBackwardTransition,_u:msdpEnabled,_A5:msdpCacheLifetime,_A6:msdpNumSACacheEntries,'msdpRequestsTable':msdpRequestsTable,'msdpRequestsEntry':msdpRequestsEntry,_m:msdpRequestsGroupAddress,_n:msdpRequestsGroupMask,_AE:msdpRequestsPeer,_AF:msdpRequestsStatus,'msdpPeerTable':msdpPeerTable,'msdpPeerEntry':msdpPeerEntry,_o:msdpPeerRemoteAddress,_I:msdpPeerState,_Q:msdpPeerRPFFailures,_R:msdpPeerInSAs,_S:msdpPeerOutSAs,_T:msdpPeerInSARequests,_U:msdpPeerOutSARequests,_v:msdpPeerInSAResponses,_w:msdpPeerOutSAResponses,_V:msdpPeerInControlMessages,_W:msdpPeerOutControlMessages,_A1:msdpPeerInDataPackets,_A2:msdpPeerOutDataPackets,_J:msdpPeerFsmEstablishedTransitions,_X:msdpPeerFsmEstablishedTime,_e:msdpPeerInMessageTime,_Y:msdpPeerLocalAddress,_b:msdpPeerConnectRetryInterval,_c:msdpPeerHoldTimeConfigured,_d:msdpPeerKeepAliveConfigured,_A3:msdpPeerDataTtl,_z:msdpPeerProcessRequestsFrom,_g:msdpPeerStatus,_Z:msdpPeerRemotePort,_a:msdpPeerLocalPort,_A4:msdpPeerEncapsulationType,_f:msdpPeerConnectionAttempts,_x:msdpPeerInNotifications,_y:msdpPeerOutNotifications,_A0:msdpPeerLastError,_h:msdpPeerDiscontinuityTime,'msdpSACacheTable':msdpSACacheTable,'msdpSACacheEntry':msdpSACacheEntry,_p:msdpSACacheGroupAddr,_q:msdpSACacheSourceAddr,_r:msdpSACacheOriginRP,_A7:msdpSACachePeerLearnedFrom,_A8:msdpSACacheRPFPeer,_A9:msdpSACacheInSAs,_AA:msdpSACacheInDataPackets,_AB:msdpSACacheUpTime,_AC:msdpSACacheExpiryTime,_AD:msdpSACacheStatus,'msdpMIBConformance':msdpMIBConformance,'msdpMIBCompliances':msdpMIBCompliances,'msdpMIBCompliance':msdpMIBCompliance,'msdpMIBFullCompliance':msdpMIBFullCompliance,'msdpMIBReadOnlyCompliance':msdpMIBReadOnlyCompliance,'msdpMIBGroups':msdpMIBGroups,_K:msdpMIBGlobalsGroup,_AK:msdpMIBPeerGroup,_L:msdpMIBEncapsulationGroup,_M:msdpMIBSACacheGroup,_AL:msdpMIBNotificationGroup,_AM:msdpMIBRequestsGroup,_N:msdpMIBRPGroup,_O:msdpMIBMeshGroupGroup,_i:msdpMIBPeerGroup2,_AG:msdpRPAddress,'msdpMeshGroupTable':msdpMeshGroupTable,'msdpMeshGroupEntry':msdpMeshGroupEntry,_s:msdpMeshGroupName,_t:msdpMeshGroupPeerAddress,_AH:msdpMeshGroupStatus})