_T='agentVpcStatusId'
_S='agentVpcPeerMemberStatusIntfId'
_R='agentVpcPeerMemberStatusVpcId'
_Q='agentVpcSelfMemberStatusIntfId'
_P='agentVpcSelfMemberStatusVpcId'
_O='agentVpcDomainIndex'
_N='read-create'
_M='agentPeerConfigRowIndex'
_L='agentVpcConfigId'
_K='secondary'
_J='primary'
_I='enable'
_H='DNOS-VPC-MIB'
_G='disable'
_F='obsolete'
_E='Integer32'
_D='Unsigned32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AgentPortMask,dnOS=mibBuilder.importSymbols('DELL-REF-MIB','AgentPortMask','dnOS')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
fastPathVpc=ModuleIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200))
if mibBuilder.loadTexts:fastPathVpc.setRevisions(('2014-01-20 00:00',))
_AgentVpcConfigGroup_ObjectIdentity=ObjectIdentity
agentVpcConfigGroup=_AgentVpcConfigGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1))
class _AgentVpcMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_I,1)))
_AgentVpcMode_Type.__name__=_E
_AgentVpcMode_Object=MibScalar
agentVpcMode=_AgentVpcMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,1),_AgentVpcMode_Type())
agentVpcMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentVpcMode.setStatus(_A)
class _AgentKeepalivePriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AgentKeepalivePriority_Type.__name__=_D
_AgentKeepalivePriority_Object=MibScalar
agentKeepalivePriority=_AgentKeepalivePriority_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,2),_AgentKeepalivePriority_Type())
agentKeepalivePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:agentKeepalivePriority.setStatus(_F)
class _AgentKeepaliveTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,15))
_AgentKeepaliveTimeout_Type.__name__=_D
_AgentKeepaliveTimeout_Object=MibScalar
agentKeepaliveTimeout=_AgentKeepaliveTimeout_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,3),_AgentKeepaliveTimeout_Type())
agentKeepaliveTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:agentKeepaliveTimeout.setStatus(_F)
class _AgentKeepaliveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_I,1)))
_AgentKeepaliveMode_Type.__name__=_E
_AgentKeepaliveMode_Object=MibScalar
agentKeepaliveMode=_AgentKeepaliveMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,4),_AgentKeepaliveMode_Type())
agentKeepaliveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentKeepaliveMode.setStatus(_F)
_AgentPeerLink_Type=InterfaceIndex
_AgentPeerLink_Object=MibScalar
agentPeerLink=_AgentPeerLink_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,5),_AgentPeerLink_Type())
agentPeerLink.setMaxAccess(_C)
if mibBuilder.loadTexts:agentPeerLink.setStatus(_A)
class _AgentPeerDetectionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_I,1)))
_AgentPeerDetectionMode_Type.__name__=_E
_AgentPeerDetectionMode_Object=MibScalar
agentPeerDetectionMode=_AgentPeerDetectionMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,6),_AgentPeerDetectionMode_Type())
agentPeerDetectionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentPeerDetectionMode.setStatus(_F)
_AgentVpcConfigTable_Object=MibTable
agentVpcConfigTable=_AgentVpcConfigTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,7))
if mibBuilder.loadTexts:agentVpcConfigTable.setStatus(_F)
_AgentVpcConfigEntry_Object=MibTableRow
agentVpcConfigEntry=_AgentVpcConfigEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,7,1))
agentVpcConfigEntry.setIndexNames((0,_H,_L))
if mibBuilder.loadTexts:agentVpcConfigEntry.setStatus(_F)
class _AgentVpcConfigId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_AgentVpcConfigId_Type.__name__=_D
_AgentVpcConfigId_Object=MibTableColumn
agentVpcConfigId=_AgentVpcConfigId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,7,1,1),_AgentVpcConfigId_Type())
agentVpcConfigId.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcConfigId.setStatus(_F)
_AgentVpcTrackPortMask_Type=AgentPortMask
_AgentVpcTrackPortMask_Object=MibTableColumn
agentVpcTrackPortMask=_AgentVpcTrackPortMask_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,7,1,2),_AgentVpcTrackPortMask_Type())
agentVpcTrackPortMask.setMaxAccess(_C)
if mibBuilder.loadTexts:agentVpcTrackPortMask.setStatus(_F)
_AgentPeerConfigTable_Object=MibTable
agentPeerConfigTable=_AgentPeerConfigTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,8))
if mibBuilder.loadTexts:agentPeerConfigTable.setStatus(_F)
_AgentPeerConfigEntry_Object=MibTableRow
agentPeerConfigEntry=_AgentPeerConfigEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,8,1))
agentPeerConfigEntry.setIndexNames((0,_H,_M))
if mibBuilder.loadTexts:agentPeerConfigEntry.setStatus(_F)
class _AgentPeerConfigRowIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_AgentPeerConfigRowIndex_Type.__name__=_D
_AgentPeerConfigRowIndex_Object=MibTableColumn
agentPeerConfigRowIndex=_AgentPeerConfigRowIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,8,1,1),_AgentPeerConfigRowIndex_Type())
agentPeerConfigRowIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:agentPeerConfigRowIndex.setStatus(_F)
_AgentPeerIpAddr_Type=IpAddress
_AgentPeerIpAddr_Object=MibTableColumn
agentPeerIpAddr=_AgentPeerIpAddr_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,8,1,2),_AgentPeerIpAddr_Type())
agentPeerIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:agentPeerIpAddr.setStatus(_F)
_AgentSourceIpAddr_Type=IpAddress
_AgentSourceIpAddr_Object=MibTableColumn
agentSourceIpAddr=_AgentSourceIpAddr_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,8,1,3),_AgentSourceIpAddr_Type())
agentSourceIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:agentSourceIpAddr.setStatus(_F)
class _AgentDcpdpUdpPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentDcpdpUdpPort_Type.__name__=_D
_AgentDcpdpUdpPort_Object=MibTableColumn
agentDcpdpUdpPort=_AgentDcpdpUdpPort_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,8,1,4),_AgentDcpdpUdpPort_Type())
agentDcpdpUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDcpdpUdpPort.setStatus(_F)
_AgentPeerRowStatus_Type=RowStatus
_AgentPeerRowStatus_Object=MibTableColumn
agentPeerRowStatus=_AgentPeerRowStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,8,1,5),_AgentPeerRowStatus_Type())
agentPeerRowStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:agentPeerRowStatus.setStatus(_F)
_AgentVpcDomainConfigTable_Object=MibTable
agentVpcDomainConfigTable=_AgentVpcDomainConfigTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,9))
if mibBuilder.loadTexts:agentVpcDomainConfigTable.setStatus(_A)
_AgentVpcDomainConfigEntry_Object=MibTableRow
agentVpcDomainConfigEntry=_AgentVpcDomainConfigEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,9,1))
agentVpcDomainConfigEntry.setIndexNames((0,_H,_O))
if mibBuilder.loadTexts:agentVpcDomainConfigEntry.setStatus(_A)
class _AgentVpcDomainIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AgentVpcDomainIndex_Type.__name__=_D
_AgentVpcDomainIndex_Object=MibTableColumn
agentVpcDomainIndex=_AgentVpcDomainIndex_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,9,1,1),_AgentVpcDomainIndex_Type())
agentVpcDomainIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:agentVpcDomainIndex.setStatus(_A)
class _AgentVpcDomainKeepalivePriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_AgentVpcDomainKeepalivePriority_Type.__name__=_D
_AgentVpcDomainKeepalivePriority_Object=MibTableColumn
agentVpcDomainKeepalivePriority=_AgentVpcDomainKeepalivePriority_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,9,1,2),_AgentVpcDomainKeepalivePriority_Type())
agentVpcDomainKeepalivePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:agentVpcDomainKeepalivePriority.setStatus(_A)
class _AgentVpcDomainKeepaliveTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,15))
_AgentVpcDomainKeepaliveTimeout_Type.__name__=_D
_AgentVpcDomainKeepaliveTimeout_Object=MibTableColumn
agentVpcDomainKeepaliveTimeout=_AgentVpcDomainKeepaliveTimeout_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,9,1,3),_AgentVpcDomainKeepaliveTimeout_Type())
agentVpcDomainKeepaliveTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:agentVpcDomainKeepaliveTimeout.setStatus(_A)
class _AgentVpcDomainKeepaliveMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_I,1)))
_AgentVpcDomainKeepaliveMode_Type.__name__=_E
_AgentVpcDomainKeepaliveMode_Object=MibTableColumn
agentVpcDomainKeepaliveMode=_AgentVpcDomainKeepaliveMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,9,1,4),_AgentVpcDomainKeepaliveMode_Type())
agentVpcDomainKeepaliveMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentVpcDomainKeepaliveMode.setStatus(_A)
class _AgentVpcDomainPeerDetectionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_G,0),(_I,1)))
_AgentVpcDomainPeerDetectionMode_Type.__name__=_E
_AgentVpcDomainPeerDetectionMode_Object=MibTableColumn
agentVpcDomainPeerDetectionMode=_AgentVpcDomainPeerDetectionMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,9,1,5),_AgentVpcDomainPeerDetectionMode_Type())
agentVpcDomainPeerDetectionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentVpcDomainPeerDetectionMode.setStatus(_A)
_AgentVpcDomainSystemMac_Type=MacAddress
_AgentVpcDomainSystemMac_Object=MibTableColumn
agentVpcDomainSystemMac=_AgentVpcDomainSystemMac_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,9,1,6),_AgentVpcDomainSystemMac_Type())
agentVpcDomainSystemMac.setMaxAccess(_C)
if mibBuilder.loadTexts:agentVpcDomainSystemMac.setStatus(_A)
class _AgentVpcDomainSystemPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentVpcDomainSystemPriority_Type.__name__=_D
_AgentVpcDomainSystemPriority_Object=MibTableColumn
agentVpcDomainSystemPriority=_AgentVpcDomainSystemPriority_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,9,1,7),_AgentVpcDomainSystemPriority_Type())
agentVpcDomainSystemPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:agentVpcDomainSystemPriority.setStatus(_A)
class _AgentVpcDomainPeerDetectionInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(200,4000))
_AgentVpcDomainPeerDetectionInterval_Type.__name__=_D
_AgentVpcDomainPeerDetectionInterval_Object=MibTableColumn
agentVpcDomainPeerDetectionInterval=_AgentVpcDomainPeerDetectionInterval_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,9,1,8),_AgentVpcDomainPeerDetectionInterval_Type())
agentVpcDomainPeerDetectionInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:agentVpcDomainPeerDetectionInterval.setStatus(_A)
class _AgentVpcDomainPeerDetectionTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(700,14000))
_AgentVpcDomainPeerDetectionTimeout_Type.__name__=_D
_AgentVpcDomainPeerDetectionTimeout_Object=MibTableColumn
agentVpcDomainPeerDetectionTimeout=_AgentVpcDomainPeerDetectionTimeout_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,9,1,9),_AgentVpcDomainPeerDetectionTimeout_Type())
agentVpcDomainPeerDetectionTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:agentVpcDomainPeerDetectionTimeout.setStatus(_A)
_AgentVpcDomainPeerIpAddr_Type=IpAddress
_AgentVpcDomainPeerIpAddr_Object=MibTableColumn
agentVpcDomainPeerIpAddr=_AgentVpcDomainPeerIpAddr_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,9,1,10),_AgentVpcDomainPeerIpAddr_Type())
agentVpcDomainPeerIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:agentVpcDomainPeerIpAddr.setStatus(_A)
_AgentVpcDomainSourceIpAddr_Type=IpAddress
_AgentVpcDomainSourceIpAddr_Object=MibTableColumn
agentVpcDomainSourceIpAddr=_AgentVpcDomainSourceIpAddr_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,9,1,11),_AgentVpcDomainSourceIpAddr_Type())
agentVpcDomainSourceIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:agentVpcDomainSourceIpAddr.setStatus(_A)
class _AgentVpcDomainDcpdpUdpPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentVpcDomainDcpdpUdpPort_Type.__name__=_D
_AgentVpcDomainDcpdpUdpPort_Object=MibTableColumn
agentVpcDomainDcpdpUdpPort=_AgentVpcDomainDcpdpUdpPort_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,9,1,12),_AgentVpcDomainDcpdpUdpPort_Type())
agentVpcDomainDcpdpUdpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:agentVpcDomainDcpdpUdpPort.setStatus(_A)
_AgentVpcDomainStatus_Type=RowStatus
_AgentVpcDomainStatus_Object=MibTableColumn
agentVpcDomainStatus=_AgentVpcDomainStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,1,9,1,13),_AgentVpcDomainStatus_Type())
agentVpcDomainStatus.setMaxAccess(_N)
if mibBuilder.loadTexts:agentVpcDomainStatus.setStatus(_A)
_AgentVpcPeerKeepAliveStatsGroup_ObjectIdentity=ObjectIdentity
agentVpcPeerKeepAliveStatsGroup=_AgentVpcPeerKeepAliveStatsGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,2))
_AgentVpcPeerKeepAliveTotalTx_Type=Unsigned32
_AgentVpcPeerKeepAliveTotalTx_Object=MibScalar
agentVpcPeerKeepAliveTotalTx=_AgentVpcPeerKeepAliveTotalTx_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,2,1),_AgentVpcPeerKeepAliveTotalTx_Type())
agentVpcPeerKeepAliveTotalTx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerKeepAliveTotalTx.setStatus(_A)
_AgentVpcPeerKeepAliveSuccessTx_Type=Unsigned32
_AgentVpcPeerKeepAliveSuccessTx_Object=MibScalar
agentVpcPeerKeepAliveSuccessTx=_AgentVpcPeerKeepAliveSuccessTx_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,2,2),_AgentVpcPeerKeepAliveSuccessTx_Type())
agentVpcPeerKeepAliveSuccessTx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerKeepAliveSuccessTx.setStatus(_A)
_AgentVpcPeerKeepAliveTxErrors_Type=Unsigned32
_AgentVpcPeerKeepAliveTxErrors_Object=MibScalar
agentVpcPeerKeepAliveTxErrors=_AgentVpcPeerKeepAliveTxErrors_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,2,3),_AgentVpcPeerKeepAliveTxErrors_Type())
agentVpcPeerKeepAliveTxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerKeepAliveTxErrors.setStatus(_A)
_AgentVpcPeerKeepAliveTotalRx_Type=Unsigned32
_AgentVpcPeerKeepAliveTotalRx_Object=MibScalar
agentVpcPeerKeepAliveTotalRx=_AgentVpcPeerKeepAliveTotalRx_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,2,4),_AgentVpcPeerKeepAliveTotalRx_Type())
agentVpcPeerKeepAliveTotalRx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerKeepAliveTotalRx.setStatus(_A)
_AgentVpcPeerKeepAliveSuccessRx_Type=Unsigned32
_AgentVpcPeerKeepAliveSuccessRx_Object=MibScalar
agentVpcPeerKeepAliveSuccessRx=_AgentVpcPeerKeepAliveSuccessRx_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,2,5),_AgentVpcPeerKeepAliveSuccessRx_Type())
agentVpcPeerKeepAliveSuccessRx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerKeepAliveSuccessRx.setStatus(_A)
_AgentVpcPeerKeepAliveRxErrors_Type=Unsigned32
_AgentVpcPeerKeepAliveRxErrors_Object=MibScalar
agentVpcPeerKeepAliveRxErrors=_AgentVpcPeerKeepAliveRxErrors_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,2,6),_AgentVpcPeerKeepAliveRxErrors_Type())
agentVpcPeerKeepAliveRxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerKeepAliveRxErrors.setStatus(_A)
_AgentVpcPeerKeepAliveTimeoutCount_Type=Unsigned32
_AgentVpcPeerKeepAliveTimeoutCount_Object=MibScalar
agentVpcPeerKeepAliveTimeoutCount=_AgentVpcPeerKeepAliveTimeoutCount_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,2,7),_AgentVpcPeerKeepAliveTimeoutCount_Type())
agentVpcPeerKeepAliveTimeoutCount.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerKeepAliveTimeoutCount.setStatus(_A)
_AgentVpcPeerLinkStatsGroup_ObjectIdentity=ObjectIdentity
agentVpcPeerLinkStatsGroup=_AgentVpcPeerLinkStatsGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,3))
_AgentVpcPeerLinkControlMsgTx_Type=Unsigned32
_AgentVpcPeerLinkControlMsgTx_Object=MibScalar
agentVpcPeerLinkControlMsgTx=_AgentVpcPeerLinkControlMsgTx_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,3,1),_AgentVpcPeerLinkControlMsgTx_Type())
agentVpcPeerLinkControlMsgTx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerLinkControlMsgTx.setStatus(_A)
_AgentVpcPeerLinkTxErrors_Type=Unsigned32
_AgentVpcPeerLinkTxErrors_Object=MibScalar
agentVpcPeerLinkTxErrors=_AgentVpcPeerLinkTxErrors_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,3,2),_AgentVpcPeerLinkTxErrors_Type())
agentVpcPeerLinkTxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerLinkTxErrors.setStatus(_A)
_AgentVpcPeerLinkTxTimeout_Type=Unsigned32
_AgentVpcPeerLinkTxTimeout_Object=MibScalar
agentVpcPeerLinkTxTimeout=_AgentVpcPeerLinkTxTimeout_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,3,3),_AgentVpcPeerLinkTxTimeout_Type())
agentVpcPeerLinkTxTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerLinkTxTimeout.setStatus(_A)
_AgentVpcPeerLinkControlMsgAckTx_Type=Unsigned32
_AgentVpcPeerLinkControlMsgAckTx_Object=MibScalar
agentVpcPeerLinkControlMsgAckTx=_AgentVpcPeerLinkControlMsgAckTx_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,3,4),_AgentVpcPeerLinkControlMsgAckTx_Type())
agentVpcPeerLinkControlMsgAckTx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerLinkControlMsgAckTx.setStatus(_A)
_AgentVpcPeerLinkControlMsgAckErrors_Type=Unsigned32
_AgentVpcPeerLinkControlMsgAckErrors_Object=MibScalar
agentVpcPeerLinkControlMsgAckErrors=_AgentVpcPeerLinkControlMsgAckErrors_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,3,5),_AgentVpcPeerLinkControlMsgAckErrors_Type())
agentVpcPeerLinkControlMsgAckErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerLinkControlMsgAckErrors.setStatus(_A)
_AgentVpcPeerLinkControlMsgRx_Type=Unsigned32
_AgentVpcPeerLinkControlMsgRx_Object=MibScalar
agentVpcPeerLinkControlMsgRx=_AgentVpcPeerLinkControlMsgRx_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,3,6),_AgentVpcPeerLinkControlMsgRx_Type())
agentVpcPeerLinkControlMsgRx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerLinkControlMsgRx.setStatus(_A)
_AgentVpcPeerLinkDataMsgTx_Type=Unsigned32
_AgentVpcPeerLinkDataMsgTx_Object=MibScalar
agentVpcPeerLinkDataMsgTx=_AgentVpcPeerLinkDataMsgTx_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,3,7),_AgentVpcPeerLinkDataMsgTx_Type())
agentVpcPeerLinkDataMsgTx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerLinkDataMsgTx.setStatus(_A)
_AgentVpcPeerLinkDataMsgTxErrors_Type=Unsigned32
_AgentVpcPeerLinkDataMsgTxErrors_Object=MibScalar
agentVpcPeerLinkDataMsgTxErrors=_AgentVpcPeerLinkDataMsgTxErrors_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,3,8),_AgentVpcPeerLinkDataMsgTxErrors_Type())
agentVpcPeerLinkDataMsgTxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerLinkDataMsgTxErrors.setStatus(_A)
_AgentVpcPeerLinkDataMsgTxTimeout_Type=Unsigned32
_AgentVpcPeerLinkDataMsgTxTimeout_Object=MibScalar
agentVpcPeerLinkDataMsgTxTimeout=_AgentVpcPeerLinkDataMsgTxTimeout_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,3,9),_AgentVpcPeerLinkDataMsgTxTimeout_Type())
agentVpcPeerLinkDataMsgTxTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerLinkDataMsgTxTimeout.setStatus(_A)
_AgentVpcPeerLinkDataMsgRx_Type=Unsigned32
_AgentVpcPeerLinkDataMsgRx_Object=MibScalar
agentVpcPeerLinkDataMsgRx=_AgentVpcPeerLinkDataMsgRx_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,3,10),_AgentVpcPeerLinkDataMsgRx_Type())
agentVpcPeerLinkDataMsgRx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerLinkDataMsgRx.setStatus(_A)
_AgentVpcPeerLinkBPDUTx_Type=Unsigned32
_AgentVpcPeerLinkBPDUTx_Object=MibScalar
agentVpcPeerLinkBPDUTx=_AgentVpcPeerLinkBPDUTx_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,3,11),_AgentVpcPeerLinkBPDUTx_Type())
agentVpcPeerLinkBPDUTx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerLinkBPDUTx.setStatus(_A)
_AgentVpcPeerLinkBPDUTxErrors_Type=Unsigned32
_AgentVpcPeerLinkBPDUTxErrors_Object=MibScalar
agentVpcPeerLinkBPDUTxErrors=_AgentVpcPeerLinkBPDUTxErrors_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,3,12),_AgentVpcPeerLinkBPDUTxErrors_Type())
agentVpcPeerLinkBPDUTxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerLinkBPDUTxErrors.setStatus(_A)
_AgentVpcPeerLinkBPDUrx_Type=Unsigned32
_AgentVpcPeerLinkBPDUrx_Object=MibScalar
agentVpcPeerLinkBPDUrx=_AgentVpcPeerLinkBPDUrx_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,3,13),_AgentVpcPeerLinkBPDUrx_Type())
agentVpcPeerLinkBPDUrx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerLinkBPDUrx.setStatus(_A)
_AgentVpcPeerLinkBPDURxErrors_Type=Unsigned32
_AgentVpcPeerLinkBPDURxErrors_Object=MibScalar
agentVpcPeerLinkBPDURxErrors=_AgentVpcPeerLinkBPDURxErrors_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,3,14),_AgentVpcPeerLinkBPDURxErrors_Type())
agentVpcPeerLinkBPDURxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerLinkBPDURxErrors.setStatus(_A)
_AgentVpcPeerLinkLACPDUTx_Type=Unsigned32
_AgentVpcPeerLinkLACPDUTx_Object=MibScalar
agentVpcPeerLinkLACPDUTx=_AgentVpcPeerLinkLACPDUTx_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,3,15),_AgentVpcPeerLinkLACPDUTx_Type())
agentVpcPeerLinkLACPDUTx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerLinkLACPDUTx.setStatus(_A)
_AgentVpcPeerLinkLACPDUTxErrors_Type=Unsigned32
_AgentVpcPeerLinkLACPDUTxErrors_Object=MibScalar
agentVpcPeerLinkLACPDUTxErrors=_AgentVpcPeerLinkLACPDUTxErrors_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,3,16),_AgentVpcPeerLinkLACPDUTxErrors_Type())
agentVpcPeerLinkLACPDUTxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerLinkLACPDUTxErrors.setStatus(_A)
_AgentVpcPeerLinkLACPDUrx_Type=Unsigned32
_AgentVpcPeerLinkLACPDUrx_Object=MibScalar
agentVpcPeerLinkLACPDUrx=_AgentVpcPeerLinkLACPDUrx_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,3,17),_AgentVpcPeerLinkLACPDUrx_Type())
agentVpcPeerLinkLACPDUrx.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerLinkLACPDUrx.setStatus(_A)
_AgentVpcPeerLinkLACPDURxErrors_Type=Unsigned32
_AgentVpcPeerLinkLACPDURxErrors_Object=MibScalar
agentVpcPeerLinkLACPDURxErrors=_AgentVpcPeerLinkLACPDURxErrors_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,3,18),_AgentVpcPeerLinkLACPDURxErrors_Type())
agentVpcPeerLinkLACPDURxErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerLinkLACPDURxErrors.setStatus(_A)
_AgentVpcStatusGroup_ObjectIdentity=ObjectIdentity
agentVpcStatusGroup=_AgentVpcStatusGroup_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4))
_AgentVpcPeerLinkStatus_Type=TruthValue
_AgentVpcPeerLinkStatus_Object=MibScalar
agentVpcPeerLinkStatus=_AgentVpcPeerLinkStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,1),_AgentVpcPeerLinkStatus_Type())
agentVpcPeerLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerLinkStatus.setStatus(_A)
_AgentVpcTotalVpcConfigured_Type=Unsigned32
_AgentVpcTotalVpcConfigured_Object=MibScalar
agentVpcTotalVpcConfigured=_AgentVpcTotalVpcConfigured_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,2),_AgentVpcTotalVpcConfigured_Type())
agentVpcTotalVpcConfigured.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcTotalVpcConfigured.setStatus(_A)
_AgentVpcTotalVpcOperational_Type=Unsigned32
_AgentVpcTotalVpcOperational_Object=MibScalar
agentVpcTotalVpcOperational=_AgentVpcTotalVpcOperational_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,3),_AgentVpcTotalVpcOperational_Type())
agentVpcTotalVpcOperational.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcTotalVpcOperational.setStatus(_A)
class _AgentVpcSelfRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),(_J,2),(_K,3)))
_AgentVpcSelfRole_Type.__name__=_E
_AgentVpcSelfRole_Object=MibScalar
agentVpcSelfRole=_AgentVpcSelfRole_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,4),_AgentVpcSelfRole_Type())
agentVpcSelfRole.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcSelfRole.setStatus(_A)
class _AgentVpcOperationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_G,2)))
_AgentVpcOperationMode_Type.__name__=_E
_AgentVpcOperationMode_Object=MibScalar
agentVpcOperationMode=_AgentVpcOperationMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,5),_AgentVpcOperationMode_Type())
agentVpcOperationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcOperationMode.setStatus(_A)
class _AgentVpcPeerRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),(_J,2),(_K,3)))
_AgentVpcPeerRole_Type.__name__=_E
_AgentVpcPeerRole_Object=MibScalar
agentVpcPeerRole=_AgentVpcPeerRole_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,6),_AgentVpcPeerRole_Type())
agentVpcPeerRole.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerRole.setStatus(_A)
class _AgentVpcKeepaliveOperationalMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_G,2)))
_AgentVpcKeepaliveOperationalMode_Type.__name__=_E
_AgentVpcKeepaliveOperationalMode_Object=MibScalar
agentVpcKeepaliveOperationalMode=_AgentVpcKeepaliveOperationalMode_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,7),_AgentVpcKeepaliveOperationalMode_Type())
agentVpcKeepaliveOperationalMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcKeepaliveOperationalMode.setStatus(_A)
_AgentVpcSystemMac_Type=MacAddress
_AgentVpcSystemMac_Object=MibScalar
agentVpcSystemMac=_AgentVpcSystemMac_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,8),_AgentVpcSystemMac_Type())
agentVpcSystemMac.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcSystemMac.setStatus(_A)
class _AgentVpcState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),('listen',2),('ready',3),(_J,4),(_K,5)))
_AgentVpcState_Type.__name__=_E
_AgentVpcState_Object=MibScalar
agentVpcState=_AgentVpcState_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,9),_AgentVpcState_Type())
agentVpcState.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcState.setStatus(_A)
_AgentVpcPeerPriority_Type=Unsigned32
_AgentVpcPeerPriority_Object=MibScalar
agentVpcPeerPriority=_AgentVpcPeerPriority_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,10),_AgentVpcPeerPriority_Type())
agentVpcPeerPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerPriority.setStatus(_A)
_AgentVpcPeerMac_Type=MacAddress
_AgentVpcPeerMac_Object=MibScalar
agentVpcPeerMac=_AgentVpcPeerMac_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,11),_AgentVpcPeerMac_Type())
agentVpcPeerMac.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerMac.setStatus(_A)
_AgentVpcPeerDetectionStatus_Type=TruthValue
_AgentVpcPeerDetectionStatus_Object=MibScalar
agentVpcPeerDetectionStatus=_AgentVpcPeerDetectionStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,12),_AgentVpcPeerDetectionStatus_Type())
agentVpcPeerDetectionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerDetectionStatus.setStatus(_A)
_AgentVpcIsPeerDetected_Type=TruthValue
_AgentVpcIsPeerDetected_Object=MibScalar
agentVpcIsPeerDetected=_AgentVpcIsPeerDetected_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,13),_AgentVpcIsPeerDetected_Type())
agentVpcIsPeerDetected.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcIsPeerDetected.setStatus(_A)
_AgentVpcSelfMemberStatusTable_Object=MibTable
agentVpcSelfMemberStatusTable=_AgentVpcSelfMemberStatusTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,14))
if mibBuilder.loadTexts:agentVpcSelfMemberStatusTable.setStatus(_A)
_AgentVpcSelfMemberStatusEntry_Object=MibTableRow
agentVpcSelfMemberStatusEntry=_AgentVpcSelfMemberStatusEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,14,1))
agentVpcSelfMemberStatusEntry.setIndexNames((0,_H,_P),(0,_H,_Q))
if mibBuilder.loadTexts:agentVpcSelfMemberStatusEntry.setStatus(_A)
class _AgentVpcSelfMemberStatusVpcId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_AgentVpcSelfMemberStatusVpcId_Type.__name__=_D
_AgentVpcSelfMemberStatusVpcId_Object=MibTableColumn
agentVpcSelfMemberStatusVpcId=_AgentVpcSelfMemberStatusVpcId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,14,1,1),_AgentVpcSelfMemberStatusVpcId_Type())
agentVpcSelfMemberStatusVpcId.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcSelfMemberStatusVpcId.setStatus(_A)
_AgentVpcSelfMemberStatusIntfId_Type=InterfaceIndex
_AgentVpcSelfMemberStatusIntfId_Object=MibTableColumn
agentVpcSelfMemberStatusIntfId=_AgentVpcSelfMemberStatusIntfId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,14,1,2),_AgentVpcSelfMemberStatusIntfId_Type())
agentVpcSelfMemberStatusIntfId.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcSelfMemberStatusIntfId.setStatus(_A)
class _AgentVpcSelfMemberStatusIntfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_AgentVpcSelfMemberStatusIntfState_Type.__name__=_E
_AgentVpcSelfMemberStatusIntfState_Object=MibTableColumn
agentVpcSelfMemberStatusIntfState=_AgentVpcSelfMemberStatusIntfState_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,14,1,3),_AgentVpcSelfMemberStatusIntfState_Type())
agentVpcSelfMemberStatusIntfState.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcSelfMemberStatusIntfState.setStatus(_A)
_AgentVpcPeerMemberStatusTable_Object=MibTable
agentVpcPeerMemberStatusTable=_AgentVpcPeerMemberStatusTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,15))
if mibBuilder.loadTexts:agentVpcPeerMemberStatusTable.setStatus(_A)
_AgentVpcPeerMemberStatusEntry_Object=MibTableRow
agentVpcPeerMemberStatusEntry=_AgentVpcPeerMemberStatusEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,15,1))
agentVpcPeerMemberStatusEntry.setIndexNames((0,_H,_R),(0,_H,_S))
if mibBuilder.loadTexts:agentVpcPeerMemberStatusEntry.setStatus(_A)
class _AgentVpcPeerMemberStatusVpcId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_AgentVpcPeerMemberStatusVpcId_Type.__name__=_D
_AgentVpcPeerMemberStatusVpcId_Object=MibTableColumn
agentVpcPeerMemberStatusVpcId=_AgentVpcPeerMemberStatusVpcId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,15,1,1),_AgentVpcPeerMemberStatusVpcId_Type())
agentVpcPeerMemberStatusVpcId.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerMemberStatusVpcId.setStatus(_A)
_AgentVpcPeerMemberStatusIntfId_Type=InterfaceIndex
_AgentVpcPeerMemberStatusIntfId_Object=MibTableColumn
agentVpcPeerMemberStatusIntfId=_AgentVpcPeerMemberStatusIntfId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,15,1,2),_AgentVpcPeerMemberStatusIntfId_Type())
agentVpcPeerMemberStatusIntfId.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerMemberStatusIntfId.setStatus(_A)
class _AgentVpcPeerMemberStatusIntfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_AgentVpcPeerMemberStatusIntfState_Type.__name__=_E
_AgentVpcPeerMemberStatusIntfState_Object=MibTableColumn
agentVpcPeerMemberStatusIntfState=_AgentVpcPeerMemberStatusIntfState_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,15,1,3),_AgentVpcPeerMemberStatusIntfState_Type())
agentVpcPeerMemberStatusIntfState.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcPeerMemberStatusIntfState.setStatus(_A)
_AgentVpcStatusTable_Object=MibTable
agentVpcStatusTable=_AgentVpcStatusTable_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,16))
if mibBuilder.loadTexts:agentVpcStatusTable.setStatus(_A)
_AgentVpcStatusEntry_Object=MibTableRow
agentVpcStatusEntry=_AgentVpcStatusEntry_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,16,1))
agentVpcStatusEntry.setIndexNames((0,_H,_T))
if mibBuilder.loadTexts:agentVpcStatusEntry.setStatus(_A)
class _AgentVpcStatusId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_AgentVpcStatusId_Type.__name__=_D
_AgentVpcStatusId_Object=MibTableColumn
agentVpcStatusId=_AgentVpcStatusId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,16,1,1),_AgentVpcStatusId_Type())
agentVpcStatusId.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcStatusId.setStatus(_A)
class _AgentVpcOperationalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_G,2)))
_AgentVpcOperationalStatus_Type.__name__=_E
_AgentVpcOperationalStatus_Object=MibTableColumn
agentVpcOperationalStatus=_AgentVpcOperationalStatus_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,16,1,2),_AgentVpcOperationalStatus_Type())
agentVpcOperationalStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcOperationalStatus.setStatus(_A)
_AgentPortChannelId_Type=InterfaceIndex
_AgentPortChannelId_Object=MibTableColumn
agentPortChannelId=_AgentPortChannelId_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,16,1,3),_AgentPortChannelId_Type())
agentPortChannelId.setMaxAccess(_B)
if mibBuilder.loadTexts:agentPortChannelId.setStatus(_A)
class _AgentVpcInterfaceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_G,1),('wait',2),('error',3),('active',4),('inactive',5)))
_AgentVpcInterfaceState_Type.__name__=_E
_AgentVpcInterfaceState_Object=MibTableColumn
agentVpcInterfaceState=_AgentVpcInterfaceState_Object((1,3,6,1,4,1,674,10895,5000,2,6132,1,1,200,4,16,1,4),_AgentVpcInterfaceState_Type())
agentVpcInterfaceState.setMaxAccess(_B)
if mibBuilder.loadTexts:agentVpcInterfaceState.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'fastPathVpc':fastPathVpc,'agentVpcConfigGroup':agentVpcConfigGroup,'agentVpcMode':agentVpcMode,'agentKeepalivePriority':agentKeepalivePriority,'agentKeepaliveTimeout':agentKeepaliveTimeout,'agentKeepaliveMode':agentKeepaliveMode,'agentPeerLink':agentPeerLink,'agentPeerDetectionMode':agentPeerDetectionMode,'agentVpcConfigTable':agentVpcConfigTable,'agentVpcConfigEntry':agentVpcConfigEntry,_L:agentVpcConfigId,'agentVpcTrackPortMask':agentVpcTrackPortMask,'agentPeerConfigTable':agentPeerConfigTable,'agentPeerConfigEntry':agentPeerConfigEntry,_M:agentPeerConfigRowIndex,'agentPeerIpAddr':agentPeerIpAddr,'agentSourceIpAddr':agentSourceIpAddr,'agentDcpdpUdpPort':agentDcpdpUdpPort,'agentPeerRowStatus':agentPeerRowStatus,'agentVpcDomainConfigTable':agentVpcDomainConfigTable,'agentVpcDomainConfigEntry':agentVpcDomainConfigEntry,_O:agentVpcDomainIndex,'agentVpcDomainKeepalivePriority':agentVpcDomainKeepalivePriority,'agentVpcDomainKeepaliveTimeout':agentVpcDomainKeepaliveTimeout,'agentVpcDomainKeepaliveMode':agentVpcDomainKeepaliveMode,'agentVpcDomainPeerDetectionMode':agentVpcDomainPeerDetectionMode,'agentVpcDomainSystemMac':agentVpcDomainSystemMac,'agentVpcDomainSystemPriority':agentVpcDomainSystemPriority,'agentVpcDomainPeerDetectionInterval':agentVpcDomainPeerDetectionInterval,'agentVpcDomainPeerDetectionTimeout':agentVpcDomainPeerDetectionTimeout,'agentVpcDomainPeerIpAddr':agentVpcDomainPeerIpAddr,'agentVpcDomainSourceIpAddr':agentVpcDomainSourceIpAddr,'agentVpcDomainDcpdpUdpPort':agentVpcDomainDcpdpUdpPort,'agentVpcDomainStatus':agentVpcDomainStatus,'agentVpcPeerKeepAliveStatsGroup':agentVpcPeerKeepAliveStatsGroup,'agentVpcPeerKeepAliveTotalTx':agentVpcPeerKeepAliveTotalTx,'agentVpcPeerKeepAliveSuccessTx':agentVpcPeerKeepAliveSuccessTx,'agentVpcPeerKeepAliveTxErrors':agentVpcPeerKeepAliveTxErrors,'agentVpcPeerKeepAliveTotalRx':agentVpcPeerKeepAliveTotalRx,'agentVpcPeerKeepAliveSuccessRx':agentVpcPeerKeepAliveSuccessRx,'agentVpcPeerKeepAliveRxErrors':agentVpcPeerKeepAliveRxErrors,'agentVpcPeerKeepAliveTimeoutCount':agentVpcPeerKeepAliveTimeoutCount,'agentVpcPeerLinkStatsGroup':agentVpcPeerLinkStatsGroup,'agentVpcPeerLinkControlMsgTx':agentVpcPeerLinkControlMsgTx,'agentVpcPeerLinkTxErrors':agentVpcPeerLinkTxErrors,'agentVpcPeerLinkTxTimeout':agentVpcPeerLinkTxTimeout,'agentVpcPeerLinkControlMsgAckTx':agentVpcPeerLinkControlMsgAckTx,'agentVpcPeerLinkControlMsgAckErrors':agentVpcPeerLinkControlMsgAckErrors,'agentVpcPeerLinkControlMsgRx':agentVpcPeerLinkControlMsgRx,'agentVpcPeerLinkDataMsgTx':agentVpcPeerLinkDataMsgTx,'agentVpcPeerLinkDataMsgTxErrors':agentVpcPeerLinkDataMsgTxErrors,'agentVpcPeerLinkDataMsgTxTimeout':agentVpcPeerLinkDataMsgTxTimeout,'agentVpcPeerLinkDataMsgRx':agentVpcPeerLinkDataMsgRx,'agentVpcPeerLinkBPDUTx':agentVpcPeerLinkBPDUTx,'agentVpcPeerLinkBPDUTxErrors':agentVpcPeerLinkBPDUTxErrors,'agentVpcPeerLinkBPDUrx':agentVpcPeerLinkBPDUrx,'agentVpcPeerLinkBPDURxErrors':agentVpcPeerLinkBPDURxErrors,'agentVpcPeerLinkLACPDUTx':agentVpcPeerLinkLACPDUTx,'agentVpcPeerLinkLACPDUTxErrors':agentVpcPeerLinkLACPDUTxErrors,'agentVpcPeerLinkLACPDUrx':agentVpcPeerLinkLACPDUrx,'agentVpcPeerLinkLACPDURxErrors':agentVpcPeerLinkLACPDURxErrors,'agentVpcStatusGroup':agentVpcStatusGroup,'agentVpcPeerLinkStatus':agentVpcPeerLinkStatus,'agentVpcTotalVpcConfigured':agentVpcTotalVpcConfigured,'agentVpcTotalVpcOperational':agentVpcTotalVpcOperational,'agentVpcSelfRole':agentVpcSelfRole,'agentVpcOperationMode':agentVpcOperationMode,'agentVpcPeerRole':agentVpcPeerRole,'agentVpcKeepaliveOperationalMode':agentVpcKeepaliveOperationalMode,'agentVpcSystemMac':agentVpcSystemMac,'agentVpcState':agentVpcState,'agentVpcPeerPriority':agentVpcPeerPriority,'agentVpcPeerMac':agentVpcPeerMac,'agentVpcPeerDetectionStatus':agentVpcPeerDetectionStatus,'agentVpcIsPeerDetected':agentVpcIsPeerDetected,'agentVpcSelfMemberStatusTable':agentVpcSelfMemberStatusTable,'agentVpcSelfMemberStatusEntry':agentVpcSelfMemberStatusEntry,_P:agentVpcSelfMemberStatusVpcId,_Q:agentVpcSelfMemberStatusIntfId,'agentVpcSelfMemberStatusIntfState':agentVpcSelfMemberStatusIntfState,'agentVpcPeerMemberStatusTable':agentVpcPeerMemberStatusTable,'agentVpcPeerMemberStatusEntry':agentVpcPeerMemberStatusEntry,_R:agentVpcPeerMemberStatusVpcId,_S:agentVpcPeerMemberStatusIntfId,'agentVpcPeerMemberStatusIntfState':agentVpcPeerMemberStatusIntfState,'agentVpcStatusTable':agentVpcStatusTable,'agentVpcStatusEntry':agentVpcStatusEntry,_T:agentVpcStatusId,'agentVpcOperationalStatus':agentVpcOperationalStatus,'agentPortChannelId':agentPortChannelId,'agentVpcInterfaceState':agentVpcInterfaceState})