_A6='msdpSACacheGroup'
_A5='msdpMIBGlobalsGroup'
_A4='msdpSACacheStatus'
_A3='msdpSACacheExpiryTime'
_A2='msdpSACacheUpTime'
_A1='msdpSACacheInDataPackets'
_A0='msdpSACacheInSAs'
_z='msdpSACacheRPFPeer'
_y='msdpSACachePeerLearnedFrom'
_x='msdpSAHoldDownPeriod'
_w='msdpNumSACacheEntries'
_v='msdpCacheLifetime'
_u='msdpPeerStatus'
_t='msdpPeerLastError'
_s='msdpPeerConnectionAttempts'
_r='msdpPeerEncapsulationType'
_q='msdpPeerEncapsulationState'
_p='msdpPeerProcessRequestsFrom'
_o='msdpPeerDataTtl'
_n='msdpPeerInMessageElapsedTime'
_m='msdpPeerKeepAliveConfigured'
_l='msdpPeerHoldTimeConfigured'
_k='msdpPeerConnectRetryInterval'
_j='msdpPeerSAAdvPeriod'
_i='msdpPeerLocalPort'
_h='msdpPeerRemotePort'
_g='msdpPeerLocalAddress'
_f='msdpPeerFsmEstablishedTime'
_e='msdpPeerOutDataPackets'
_d='msdpPeerInDataPackets'
_c='msdpPeerOutControlMessages'
_b='msdpPeerInControlMessages'
_a='msdpPeerOutNotifications'
_Z='msdpPeerInNotifications'
_Y='msdpPeerOutSAResponses'
_X='msdpPeerInSAResponses'
_W='msdpPeerOutSARequests'
_V='msdpPeerInSARequests'
_U='msdpPeerOutSAs'
_T='msdpPeerInSAs'
_S='msdpPeerRPFFailures'
_R='msdpEnabled'
_Q='msdpSACacheOriginRP'
_P='msdpSACacheSourceAddr'
_O='msdpSACacheGroupAddr'
_N='msdpPeerRemoteAddress'
_M='msdpRequestsGroupMask'
_L='msdpRequestsGroupAddress'
_K='OctetString'
_J='msdpPeerFsmEstablishedTransitions'
_I='msdpPeerState'
_H='read-write'
_G='not-accessible'
_F='seconds'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='DRAFT-MSDP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','experimental','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
msdpMIB=ModuleIdentity((1,3,6,1,3,92))
_MsdpMIBobjects_ObjectIdentity=ObjectIdentity
msdpMIBobjects=_MsdpMIBobjects_ObjectIdentity((1,3,6,1,3,92,1))
_Msdp_ObjectIdentity=ObjectIdentity
msdp=_Msdp_ObjectIdentity((1,3,6,1,3,92,1,1))
_MsdpEnabled_Type=TruthValue
_MsdpEnabled_Object=MibScalar
msdpEnabled=_MsdpEnabled_Object((1,3,6,1,3,92,1,1,1),_MsdpEnabled_Type())
msdpEnabled.setMaxAccess(_H)
if mibBuilder.loadTexts:msdpEnabled.setStatus(_A)
_MsdpCacheLifetime_Type=TimeTicks
_MsdpCacheLifetime_Object=MibScalar
msdpCacheLifetime=_MsdpCacheLifetime_Object((1,3,6,1,3,92,1,1,2),_MsdpCacheLifetime_Type())
msdpCacheLifetime.setMaxAccess(_H)
if mibBuilder.loadTexts:msdpCacheLifetime.setStatus(_A)
_MsdpNumSACacheEntries_Type=Gauge32
_MsdpNumSACacheEntries_Object=MibScalar
msdpNumSACacheEntries=_MsdpNumSACacheEntries_Object((1,3,6,1,3,92,1,1,3),_MsdpNumSACacheEntries_Type())
msdpNumSACacheEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpNumSACacheEntries.setStatus(_A)
_MsdpRequestsTable_Object=MibTable
msdpRequestsTable=_MsdpRequestsTable_Object((1,3,6,1,3,92,1,1,4))
if mibBuilder.loadTexts:msdpRequestsTable.setStatus(_A)
_MsdpRequestsEntry_Object=MibTableRow
msdpRequestsEntry=_MsdpRequestsEntry_Object((1,3,6,1,3,92,1,1,4,1))
msdpRequestsEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:msdpRequestsEntry.setStatus(_A)
_MsdpRequestsGroupAddress_Type=IpAddress
_MsdpRequestsGroupAddress_Object=MibTableColumn
msdpRequestsGroupAddress=_MsdpRequestsGroupAddress_Object((1,3,6,1,3,92,1,1,4,1,1),_MsdpRequestsGroupAddress_Type())
msdpRequestsGroupAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:msdpRequestsGroupAddress.setStatus(_A)
_MsdpRequestsGroupMask_Type=IpAddress
_MsdpRequestsGroupMask_Object=MibTableColumn
msdpRequestsGroupMask=_MsdpRequestsGroupMask_Object((1,3,6,1,3,92,1,1,4,1,2),_MsdpRequestsGroupMask_Type())
msdpRequestsGroupMask.setMaxAccess(_G)
if mibBuilder.loadTexts:msdpRequestsGroupMask.setStatus(_A)
_MsdpRequestsPeer_Type=IpAddress
_MsdpRequestsPeer_Object=MibTableColumn
msdpRequestsPeer=_MsdpRequestsPeer_Object((1,3,6,1,3,92,1,1,4,1,3),_MsdpRequestsPeer_Type())
msdpRequestsPeer.setMaxAccess(_E)
if mibBuilder.loadTexts:msdpRequestsPeer.setStatus(_A)
_MsdpRequestsStatus_Type=RowStatus
_MsdpRequestsStatus_Object=MibTableColumn
msdpRequestsStatus=_MsdpRequestsStatus_Object((1,3,6,1,3,92,1,1,4,1,4),_MsdpRequestsStatus_Type())
msdpRequestsStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:msdpRequestsStatus.setStatus(_A)
_MsdpPeerTable_Object=MibTable
msdpPeerTable=_MsdpPeerTable_Object((1,3,6,1,3,92,1,1,5))
if mibBuilder.loadTexts:msdpPeerTable.setStatus(_A)
_MsdpPeerEntry_Object=MibTableRow
msdpPeerEntry=_MsdpPeerEntry_Object((1,3,6,1,3,92,1,1,5,1))
msdpPeerEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:msdpPeerEntry.setStatus(_A)
_MsdpPeerRemoteAddress_Type=IpAddress
_MsdpPeerRemoteAddress_Object=MibTableColumn
msdpPeerRemoteAddress=_MsdpPeerRemoteAddress_Object((1,3,6,1,3,92,1,1,5,1,1),_MsdpPeerRemoteAddress_Type())
msdpPeerRemoteAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:msdpPeerRemoteAddress.setStatus(_A)
class _MsdpPeerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('inactive',1),('listen',2),('connecting',3),('established',4),('disabled',5)))
_MsdpPeerState_Type.__name__=_D
_MsdpPeerState_Object=MibTableColumn
msdpPeerState=_MsdpPeerState_Object((1,3,6,1,3,92,1,1,5,1,3),_MsdpPeerState_Type())
msdpPeerState.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerState.setStatus(_A)
_MsdpPeerRPFFailures_Type=Counter32
_MsdpPeerRPFFailures_Object=MibTableColumn
msdpPeerRPFFailures=_MsdpPeerRPFFailures_Object((1,3,6,1,3,92,1,1,5,1,4),_MsdpPeerRPFFailures_Type())
msdpPeerRPFFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerRPFFailures.setStatus(_A)
_MsdpPeerInSAs_Type=Counter32
_MsdpPeerInSAs_Object=MibTableColumn
msdpPeerInSAs=_MsdpPeerInSAs_Object((1,3,6,1,3,92,1,1,5,1,5),_MsdpPeerInSAs_Type())
msdpPeerInSAs.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerInSAs.setStatus(_A)
_MsdpPeerOutSAs_Type=Counter32
_MsdpPeerOutSAs_Object=MibTableColumn
msdpPeerOutSAs=_MsdpPeerOutSAs_Object((1,3,6,1,3,92,1,1,5,1,6),_MsdpPeerOutSAs_Type())
msdpPeerOutSAs.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerOutSAs.setStatus(_A)
_MsdpPeerInSARequests_Type=Counter32
_MsdpPeerInSARequests_Object=MibTableColumn
msdpPeerInSARequests=_MsdpPeerInSARequests_Object((1,3,6,1,3,92,1,1,5,1,7),_MsdpPeerInSARequests_Type())
msdpPeerInSARequests.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerInSARequests.setStatus(_A)
_MsdpPeerOutSARequests_Type=Counter32
_MsdpPeerOutSARequests_Object=MibTableColumn
msdpPeerOutSARequests=_MsdpPeerOutSARequests_Object((1,3,6,1,3,92,1,1,5,1,8),_MsdpPeerOutSARequests_Type())
msdpPeerOutSARequests.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerOutSARequests.setStatus(_A)
_MsdpPeerInSAResponses_Type=Counter32
_MsdpPeerInSAResponses_Object=MibTableColumn
msdpPeerInSAResponses=_MsdpPeerInSAResponses_Object((1,3,6,1,3,92,1,1,5,1,9),_MsdpPeerInSAResponses_Type())
msdpPeerInSAResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerInSAResponses.setStatus(_A)
_MsdpPeerOutSAResponses_Type=Counter32
_MsdpPeerOutSAResponses_Object=MibTableColumn
msdpPeerOutSAResponses=_MsdpPeerOutSAResponses_Object((1,3,6,1,3,92,1,1,5,1,10),_MsdpPeerOutSAResponses_Type())
msdpPeerOutSAResponses.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerOutSAResponses.setStatus(_A)
_MsdpPeerInControlMessages_Type=Counter32
_MsdpPeerInControlMessages_Object=MibTableColumn
msdpPeerInControlMessages=_MsdpPeerInControlMessages_Object((1,3,6,1,3,92,1,1,5,1,11),_MsdpPeerInControlMessages_Type())
msdpPeerInControlMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerInControlMessages.setStatus(_A)
_MsdpPeerOutControlMessages_Type=Counter32
_MsdpPeerOutControlMessages_Object=MibTableColumn
msdpPeerOutControlMessages=_MsdpPeerOutControlMessages_Object((1,3,6,1,3,92,1,1,5,1,12),_MsdpPeerOutControlMessages_Type())
msdpPeerOutControlMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerOutControlMessages.setStatus(_A)
_MsdpPeerInDataPackets_Type=Counter32
_MsdpPeerInDataPackets_Object=MibTableColumn
msdpPeerInDataPackets=_MsdpPeerInDataPackets_Object((1,3,6,1,3,92,1,1,5,1,13),_MsdpPeerInDataPackets_Type())
msdpPeerInDataPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerInDataPackets.setStatus(_A)
_MsdpPeerOutDataPackets_Type=Counter32
_MsdpPeerOutDataPackets_Object=MibTableColumn
msdpPeerOutDataPackets=_MsdpPeerOutDataPackets_Object((1,3,6,1,3,92,1,1,5,1,14),_MsdpPeerOutDataPackets_Type())
msdpPeerOutDataPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerOutDataPackets.setStatus(_A)
_MsdpPeerFsmEstablishedTransitions_Type=Counter32
_MsdpPeerFsmEstablishedTransitions_Object=MibTableColumn
msdpPeerFsmEstablishedTransitions=_MsdpPeerFsmEstablishedTransitions_Object((1,3,6,1,3,92,1,1,5,1,15),_MsdpPeerFsmEstablishedTransitions_Type())
msdpPeerFsmEstablishedTransitions.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerFsmEstablishedTransitions.setStatus(_A)
_MsdpPeerFsmEstablishedTime_Type=Gauge32
_MsdpPeerFsmEstablishedTime_Object=MibTableColumn
msdpPeerFsmEstablishedTime=_MsdpPeerFsmEstablishedTime_Object((1,3,6,1,3,92,1,1,5,1,16),_MsdpPeerFsmEstablishedTime_Type())
msdpPeerFsmEstablishedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerFsmEstablishedTime.setStatus(_A)
if mibBuilder.loadTexts:msdpPeerFsmEstablishedTime.setUnits(_F)
_MsdpPeerInMessageElapsedTime_Type=Gauge32
_MsdpPeerInMessageElapsedTime_Object=MibTableColumn
msdpPeerInMessageElapsedTime=_MsdpPeerInMessageElapsedTime_Object((1,3,6,1,3,92,1,1,5,1,17),_MsdpPeerInMessageElapsedTime_Type())
msdpPeerInMessageElapsedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerInMessageElapsedTime.setStatus(_A)
if mibBuilder.loadTexts:msdpPeerInMessageElapsedTime.setUnits(_F)
_MsdpPeerLocalAddress_Type=IpAddress
_MsdpPeerLocalAddress_Object=MibTableColumn
msdpPeerLocalAddress=_MsdpPeerLocalAddress_Object((1,3,6,1,3,92,1,1,5,1,18),_MsdpPeerLocalAddress_Type())
msdpPeerLocalAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:msdpPeerLocalAddress.setStatus(_A)
class _MsdpPeerSAAdvPeriod_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MsdpPeerSAAdvPeriod_Type.__name__=_D
_MsdpPeerSAAdvPeriod_Object=MibTableColumn
msdpPeerSAAdvPeriod=_MsdpPeerSAAdvPeriod_Object((1,3,6,1,3,92,1,1,5,1,19),_MsdpPeerSAAdvPeriod_Type())
msdpPeerSAAdvPeriod.setMaxAccess(_E)
if mibBuilder.loadTexts:msdpPeerSAAdvPeriod.setStatus(_A)
if mibBuilder.loadTexts:msdpPeerSAAdvPeriod.setUnits(_F)
class _MsdpPeerConnectRetryInterval_Type(Integer32):defaultValue=120;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_MsdpPeerConnectRetryInterval_Type.__name__=_D
_MsdpPeerConnectRetryInterval_Object=MibTableColumn
msdpPeerConnectRetryInterval=_MsdpPeerConnectRetryInterval_Object((1,3,6,1,3,92,1,1,5,1,20),_MsdpPeerConnectRetryInterval_Type())
msdpPeerConnectRetryInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:msdpPeerConnectRetryInterval.setStatus(_A)
if mibBuilder.loadTexts:msdpPeerConnectRetryInterval.setUnits(_F)
class _MsdpPeerHoldTimeConfigured_Type(Integer32):defaultValue=90;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(3,65535))
_MsdpPeerHoldTimeConfigured_Type.__name__=_D
_MsdpPeerHoldTimeConfigured_Object=MibTableColumn
msdpPeerHoldTimeConfigured=_MsdpPeerHoldTimeConfigured_Object((1,3,6,1,3,92,1,1,5,1,21),_MsdpPeerHoldTimeConfigured_Type())
msdpPeerHoldTimeConfigured.setMaxAccess(_E)
if mibBuilder.loadTexts:msdpPeerHoldTimeConfigured.setStatus(_A)
if mibBuilder.loadTexts:msdpPeerHoldTimeConfigured.setUnits(_F)
class _MsdpPeerKeepAliveConfigured_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,21845))
_MsdpPeerKeepAliveConfigured_Type.__name__=_D
_MsdpPeerKeepAliveConfigured_Object=MibTableColumn
msdpPeerKeepAliveConfigured=_MsdpPeerKeepAliveConfigured_Object((1,3,6,1,3,92,1,1,5,1,22),_MsdpPeerKeepAliveConfigured_Type())
msdpPeerKeepAliveConfigured.setMaxAccess(_E)
if mibBuilder.loadTexts:msdpPeerKeepAliveConfigured.setStatus(_A)
if mibBuilder.loadTexts:msdpPeerKeepAliveConfigured.setUnits(_F)
class _MsdpPeerDataTtl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MsdpPeerDataTtl_Type.__name__=_D
_MsdpPeerDataTtl_Object=MibTableColumn
msdpPeerDataTtl=_MsdpPeerDataTtl_Object((1,3,6,1,3,92,1,1,5,1,23),_MsdpPeerDataTtl_Type())
msdpPeerDataTtl.setMaxAccess(_E)
if mibBuilder.loadTexts:msdpPeerDataTtl.setStatus(_A)
_MsdpPeerProcessRequestsFrom_Type=TruthValue
_MsdpPeerProcessRequestsFrom_Object=MibTableColumn
msdpPeerProcessRequestsFrom=_MsdpPeerProcessRequestsFrom_Object((1,3,6,1,3,92,1,1,5,1,24),_MsdpPeerProcessRequestsFrom_Type())
msdpPeerProcessRequestsFrom.setMaxAccess(_E)
if mibBuilder.loadTexts:msdpPeerProcessRequestsFrom.setStatus(_A)
_MsdpPeerStatus_Type=RowStatus
_MsdpPeerStatus_Object=MibTableColumn
msdpPeerStatus=_MsdpPeerStatus_Object((1,3,6,1,3,92,1,1,5,1,25),_MsdpPeerStatus_Type())
msdpPeerStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:msdpPeerStatus.setStatus(_A)
class _MsdpPeerRemotePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MsdpPeerRemotePort_Type.__name__=_D
_MsdpPeerRemotePort_Object=MibTableColumn
msdpPeerRemotePort=_MsdpPeerRemotePort_Object((1,3,6,1,3,92,1,1,5,1,26),_MsdpPeerRemotePort_Type())
msdpPeerRemotePort.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerRemotePort.setStatus(_A)
class _MsdpPeerLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MsdpPeerLocalPort_Type.__name__=_D
_MsdpPeerLocalPort_Object=MibTableColumn
msdpPeerLocalPort=_MsdpPeerLocalPort_Object((1,3,6,1,3,92,1,1,5,1,27),_MsdpPeerLocalPort_Type())
msdpPeerLocalPort.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerLocalPort.setStatus(_A)
class _MsdpPeerEncapsulationState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('default',1),('received',2),('advertising',3),('sent',4),('agreed',5),('failed',6)))
_MsdpPeerEncapsulationState_Type.__name__=_D
_MsdpPeerEncapsulationState_Object=MibTableColumn
msdpPeerEncapsulationState=_MsdpPeerEncapsulationState_Object((1,3,6,1,3,92,1,1,5,1,28),_MsdpPeerEncapsulationState_Type())
msdpPeerEncapsulationState.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerEncapsulationState.setStatus(_A)
class _MsdpPeerEncapsulationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('tcp',1),('udp',2),('gre',3)))
_MsdpPeerEncapsulationType_Type.__name__=_D
_MsdpPeerEncapsulationType_Object=MibTableColumn
msdpPeerEncapsulationType=_MsdpPeerEncapsulationType_Object((1,3,6,1,3,92,1,1,5,1,29),_MsdpPeerEncapsulationType_Type())
msdpPeerEncapsulationType.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerEncapsulationType.setStatus(_A)
_MsdpPeerConnectionAttempts_Type=Counter32
_MsdpPeerConnectionAttempts_Object=MibTableColumn
msdpPeerConnectionAttempts=_MsdpPeerConnectionAttempts_Object((1,3,6,1,3,92,1,1,5,1,30),_MsdpPeerConnectionAttempts_Type())
msdpPeerConnectionAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerConnectionAttempts.setStatus(_A)
_MsdpPeerInNotifications_Type=Counter32
_MsdpPeerInNotifications_Object=MibTableColumn
msdpPeerInNotifications=_MsdpPeerInNotifications_Object((1,3,6,1,3,92,1,1,5,1,31),_MsdpPeerInNotifications_Type())
msdpPeerInNotifications.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerInNotifications.setStatus(_A)
_MsdpPeerOutNotifications_Type=Counter32
_MsdpPeerOutNotifications_Object=MibTableColumn
msdpPeerOutNotifications=_MsdpPeerOutNotifications_Object((1,3,6,1,3,92,1,1,5,1,32),_MsdpPeerOutNotifications_Type())
msdpPeerOutNotifications.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerOutNotifications.setStatus(_A)
class _MsdpPeerLastError_Type(OctetString):defaultHexValue='0000';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_MsdpPeerLastError_Type.__name__=_K
_MsdpPeerLastError_Object=MibTableColumn
msdpPeerLastError=_MsdpPeerLastError_Object((1,3,6,1,3,92,1,1,5,1,33),_MsdpPeerLastError_Type())
msdpPeerLastError.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpPeerLastError.setStatus(_A)
_MsdpSACacheTable_Object=MibTable
msdpSACacheTable=_MsdpSACacheTable_Object((1,3,6,1,3,92,1,1,6))
if mibBuilder.loadTexts:msdpSACacheTable.setStatus(_A)
_MsdpSACacheEntry_Object=MibTableRow
msdpSACacheEntry=_MsdpSACacheEntry_Object((1,3,6,1,3,92,1,1,6,1))
msdpSACacheEntry.setIndexNames((0,_B,_O),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:msdpSACacheEntry.setStatus(_A)
_MsdpSACacheGroupAddr_Type=IpAddress
_MsdpSACacheGroupAddr_Object=MibTableColumn
msdpSACacheGroupAddr=_MsdpSACacheGroupAddr_Object((1,3,6,1,3,92,1,1,6,1,1),_MsdpSACacheGroupAddr_Type())
msdpSACacheGroupAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:msdpSACacheGroupAddr.setStatus(_A)
_MsdpSACacheSourceAddr_Type=IpAddress
_MsdpSACacheSourceAddr_Object=MibTableColumn
msdpSACacheSourceAddr=_MsdpSACacheSourceAddr_Object((1,3,6,1,3,92,1,1,6,1,2),_MsdpSACacheSourceAddr_Type())
msdpSACacheSourceAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:msdpSACacheSourceAddr.setStatus(_A)
_MsdpSACacheOriginRP_Type=IpAddress
_MsdpSACacheOriginRP_Object=MibTableColumn
msdpSACacheOriginRP=_MsdpSACacheOriginRP_Object((1,3,6,1,3,92,1,1,6,1,3),_MsdpSACacheOriginRP_Type())
msdpSACacheOriginRP.setMaxAccess(_G)
if mibBuilder.loadTexts:msdpSACacheOriginRP.setStatus(_A)
_MsdpSACachePeerLearnedFrom_Type=IpAddress
_MsdpSACachePeerLearnedFrom_Object=MibTableColumn
msdpSACachePeerLearnedFrom=_MsdpSACachePeerLearnedFrom_Object((1,3,6,1,3,92,1,1,6,1,4),_MsdpSACachePeerLearnedFrom_Type())
msdpSACachePeerLearnedFrom.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpSACachePeerLearnedFrom.setStatus(_A)
_MsdpSACacheRPFPeer_Type=IpAddress
_MsdpSACacheRPFPeer_Object=MibTableColumn
msdpSACacheRPFPeer=_MsdpSACacheRPFPeer_Object((1,3,6,1,3,92,1,1,6,1,5),_MsdpSACacheRPFPeer_Type())
msdpSACacheRPFPeer.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpSACacheRPFPeer.setStatus(_A)
_MsdpSACacheInSAs_Type=Counter32
_MsdpSACacheInSAs_Object=MibTableColumn
msdpSACacheInSAs=_MsdpSACacheInSAs_Object((1,3,6,1,3,92,1,1,6,1,6),_MsdpSACacheInSAs_Type())
msdpSACacheInSAs.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpSACacheInSAs.setStatus(_A)
_MsdpSACacheInDataPackets_Type=Counter32
_MsdpSACacheInDataPackets_Object=MibTableColumn
msdpSACacheInDataPackets=_MsdpSACacheInDataPackets_Object((1,3,6,1,3,92,1,1,6,1,7),_MsdpSACacheInDataPackets_Type())
msdpSACacheInDataPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpSACacheInDataPackets.setStatus(_A)
_MsdpSACacheUpTime_Type=TimeTicks
_MsdpSACacheUpTime_Object=MibTableColumn
msdpSACacheUpTime=_MsdpSACacheUpTime_Object((1,3,6,1,3,92,1,1,6,1,8),_MsdpSACacheUpTime_Type())
msdpSACacheUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpSACacheUpTime.setStatus(_A)
_MsdpSACacheExpiryTime_Type=TimeTicks
_MsdpSACacheExpiryTime_Object=MibTableColumn
msdpSACacheExpiryTime=_MsdpSACacheExpiryTime_Object((1,3,6,1,3,92,1,1,6,1,9),_MsdpSACacheExpiryTime_Type())
msdpSACacheExpiryTime.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpSACacheExpiryTime.setStatus(_A)
_MsdpSACacheStatus_Type=RowStatus
_MsdpSACacheStatus_Object=MibTableColumn
msdpSACacheStatus=_MsdpSACacheStatus_Object((1,3,6,1,3,92,1,1,6,1,10),_MsdpSACacheStatus_Type())
msdpSACacheStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:msdpSACacheStatus.setStatus(_A)
_MsdpTraps_ObjectIdentity=ObjectIdentity
msdpTraps=_MsdpTraps_ObjectIdentity((1,3,6,1,3,92,1,1,7))
_MsdpMIBConformance_ObjectIdentity=ObjectIdentity
msdpMIBConformance=_MsdpMIBConformance_ObjectIdentity((1,3,6,1,3,92,1,1,8))
_MsdpMIBCompliances_ObjectIdentity=ObjectIdentity
msdpMIBCompliances=_MsdpMIBCompliances_ObjectIdentity((1,3,6,1,3,92,1,1,8,1))
_MsdpMIBGroups_ObjectIdentity=ObjectIdentity
msdpMIBGroups=_MsdpMIBGroups_ObjectIdentity((1,3,6,1,3,92,1,1,8,2))
class _MsdpSAHoldDownPeriod_Type(Integer32):defaultValue=90;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_MsdpSAHoldDownPeriod_Type.__name__=_D
_MsdpSAHoldDownPeriod_Object=MibScalar
msdpSAHoldDownPeriod=_MsdpSAHoldDownPeriod_Object((1,3,6,1,3,92,1,1,9),_MsdpSAHoldDownPeriod_Type())
msdpSAHoldDownPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:msdpSAHoldDownPeriod.setStatus(_A)
if mibBuilder.loadTexts:msdpSAHoldDownPeriod.setUnits(_F)
msdpMIBGlobalsGroup=ObjectGroup((1,3,6,1,3,92,1,1,8,2,1))
msdpMIBGlobalsGroup.setObjects((_B,_R))
if mibBuilder.loadTexts:msdpMIBGlobalsGroup.setStatus(_A)
msdpMIBPeerGroup=ObjectGroup((1,3,6,1,3,92,1,1,8,2,2))
msdpMIBPeerGroup.setObjects(*((_B,_S),(_B,_I),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_J),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:msdpMIBPeerGroup.setStatus(_A)
msdpSACacheGroup=ObjectGroup((1,3,6,1,3,92,1,1,8,2,3))
msdpSACacheGroup.setObjects(*((_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:msdpSACacheGroup.setStatus(_A)
msdpEstablished=NotificationType((1,3,6,1,3,92,1,1,7,1))
msdpEstablished.setObjects((_B,_J))
if mibBuilder.loadTexts:msdpEstablished.setStatus(_A)
msdpBackwardTransition=NotificationType((1,3,6,1,3,92,1,1,7,2))
msdpBackwardTransition.setObjects((_B,_I))
if mibBuilder.loadTexts:msdpBackwardTransition.setStatus(_A)
msdpMIBCompliance=ModuleCompliance((1,3,6,1,3,92,1,1,8,1,1))
msdpMIBCompliance.setObjects(*((_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:msdpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'msdpMIB':msdpMIB,'msdpMIBobjects':msdpMIBobjects,'msdp':msdp,_R:msdpEnabled,_v:msdpCacheLifetime,_w:msdpNumSACacheEntries,'msdpRequestsTable':msdpRequestsTable,'msdpRequestsEntry':msdpRequestsEntry,_L:msdpRequestsGroupAddress,_M:msdpRequestsGroupMask,'msdpRequestsPeer':msdpRequestsPeer,'msdpRequestsStatus':msdpRequestsStatus,'msdpPeerTable':msdpPeerTable,'msdpPeerEntry':msdpPeerEntry,_N:msdpPeerRemoteAddress,_I:msdpPeerState,_S:msdpPeerRPFFailures,_T:msdpPeerInSAs,_U:msdpPeerOutSAs,_V:msdpPeerInSARequests,_W:msdpPeerOutSARequests,_X:msdpPeerInSAResponses,_Y:msdpPeerOutSAResponses,_b:msdpPeerInControlMessages,_c:msdpPeerOutControlMessages,_d:msdpPeerInDataPackets,_e:msdpPeerOutDataPackets,_J:msdpPeerFsmEstablishedTransitions,_f:msdpPeerFsmEstablishedTime,_n:msdpPeerInMessageElapsedTime,_g:msdpPeerLocalAddress,_j:msdpPeerSAAdvPeriod,_k:msdpPeerConnectRetryInterval,_l:msdpPeerHoldTimeConfigured,_m:msdpPeerKeepAliveConfigured,_o:msdpPeerDataTtl,_p:msdpPeerProcessRequestsFrom,_u:msdpPeerStatus,_h:msdpPeerRemotePort,_i:msdpPeerLocalPort,_q:msdpPeerEncapsulationState,_r:msdpPeerEncapsulationType,_s:msdpPeerConnectionAttempts,_Z:msdpPeerInNotifications,_a:msdpPeerOutNotifications,_t:msdpPeerLastError,'msdpSACacheTable':msdpSACacheTable,'msdpSACacheEntry':msdpSACacheEntry,_O:msdpSACacheGroupAddr,_P:msdpSACacheSourceAddr,_Q:msdpSACacheOriginRP,_y:msdpSACachePeerLearnedFrom,_z:msdpSACacheRPFPeer,_A0:msdpSACacheInSAs,_A1:msdpSACacheInDataPackets,_A2:msdpSACacheUpTime,_A3:msdpSACacheExpiryTime,_A4:msdpSACacheStatus,'msdpTraps':msdpTraps,'msdpEstablished':msdpEstablished,'msdpBackwardTransition':msdpBackwardTransition,'msdpMIBConformance':msdpMIBConformance,'msdpMIBCompliances':msdpMIBCompliances,'msdpMIBCompliance':msdpMIBCompliance,'msdpMIBGroups':msdpMIBGroups,_A5:msdpMIBGlobalsGroup,'msdpMIBPeerGroup':msdpMIBPeerGroup,_A6:msdpSACacheGroup,_x:msdpSAHoldDownPeriod})