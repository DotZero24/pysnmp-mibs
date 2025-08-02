_R='agentDhcp6ServerBindingIndex'
_Q='agentDhcp6InterfaceStatsIndex'
_P='not-accessible'
_O='agentDhcp6InterfaceIndex'
_N='agentDhcp6ServerPoolAllocationIndex'
_M='agentDhcp6ServerPoolDnsServerIndex'
_L='agentDhcp6ServerPoolDnsDomainIndex'
_K='enable'
_J='disable'
_I='Unsigned32'
_H='agentDhcp6ServerPoolIndex'
_G='read-write'
_F='DisplayString'
_E='FASTPATH-DHCP6SERVER-PRIVATE-MIB'
_D='Integer32'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fastPath,=mibBuilder.importSymbols('BROADCOM-REF-MIB','fastPath')
Ipv6Address,Ipv6AddressIfIdentifier,Ipv6AddressPrefix,Ipv6IfIndex,Ipv6IfIndexOrZero=mibBuilder.importSymbols('IPV6-TC','Ipv6Address','Ipv6AddressIfIdentifier','Ipv6AddressPrefix','Ipv6IfIndex','Ipv6IfIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,MacAddress,PhysAddress,RowPointer,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','RowPointer','RowStatus','StorageType','TextualConvention','TruthValue')
fastPathDHCP6ServerPrivate=ModuleIdentity((1,3,6,1,4,1,4413,1,1,25))
if mibBuilder.loadTexts:fastPathDHCP6ServerPrivate.setRevisions(('2007-05-23 00:00',))
_AgentDhcp6ServerGroup_ObjectIdentity=ObjectIdentity
agentDhcp6ServerGroup=_AgentDhcp6ServerGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,25,1))
class _AgentDhcp6ServerAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_AgentDhcp6ServerAdminMode_Type.__name__=_D
_AgentDhcp6ServerAdminMode_Object=MibScalar
agentDhcp6ServerAdminMode=_AgentDhcp6ServerAdminMode_Object((1,3,6,1,4,1,4413,1,1,25,1,1),_AgentDhcp6ServerAdminMode_Type())
agentDhcp6ServerAdminMode.setMaxAccess(_G)
if mibBuilder.loadTexts:agentDhcp6ServerAdminMode.setStatus(_A)
class _AgentDhcp6ServerRelayOptParm_Type(Integer32):defaultValue=54;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(54,65535))
_AgentDhcp6ServerRelayOptParm_Type.__name__=_D
_AgentDhcp6ServerRelayOptParm_Object=MibScalar
agentDhcp6ServerRelayOptParm=_AgentDhcp6ServerRelayOptParm_Object((1,3,6,1,4,1,4413,1,1,25,1,2),_AgentDhcp6ServerRelayOptParm_Type())
agentDhcp6ServerRelayOptParm.setMaxAccess(_G)
if mibBuilder.loadTexts:agentDhcp6ServerRelayOptParm.setStatus(_A)
class _AgentDhcp6ServerRelayOptRemoteIdSuboptParm_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AgentDhcp6ServerRelayOptRemoteIdSuboptParm_Type.__name__=_D
_AgentDhcp6ServerRelayOptRemoteIdSuboptParm_Object=MibScalar
agentDhcp6ServerRelayOptRemoteIdSuboptParm=_AgentDhcp6ServerRelayOptRemoteIdSuboptParm_Object((1,3,6,1,4,1,4413,1,1,25,1,3),_AgentDhcp6ServerRelayOptRemoteIdSuboptParm_Type())
agentDhcp6ServerRelayOptRemoteIdSuboptParm.setMaxAccess(_G)
if mibBuilder.loadTexts:agentDhcp6ServerRelayOptRemoteIdSuboptParm.setStatus(_A)
class _AgentDhcp6ServerDuid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_AgentDhcp6ServerDuid_Type.__name__=_F
_AgentDhcp6ServerDuid_Object=MibScalar
agentDhcp6ServerDuid=_AgentDhcp6ServerDuid_Object((1,3,6,1,4,1,4413,1,1,25,1,4),_AgentDhcp6ServerDuid_Type())
agentDhcp6ServerDuid.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerDuid.setStatus(_A)
_AgentDhcp6ServerMalformedMessagesReceived_Type=Counter32
_AgentDhcp6ServerMalformedMessagesReceived_Object=MibScalar
agentDhcp6ServerMalformedMessagesReceived=_AgentDhcp6ServerMalformedMessagesReceived_Object((1,3,6,1,4,1,4413,1,1,25,1,5),_AgentDhcp6ServerMalformedMessagesReceived_Type())
agentDhcp6ServerMalformedMessagesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerMalformedMessagesReceived.setStatus(_A)
_AgentDhcp6ServerDiscardedMessages_Type=Counter32
_AgentDhcp6ServerDiscardedMessages_Object=MibScalar
agentDhcp6ServerDiscardedMessages=_AgentDhcp6ServerDiscardedMessages_Object((1,3,6,1,4,1,4413,1,1,25,1,6),_AgentDhcp6ServerDiscardedMessages_Type())
agentDhcp6ServerDiscardedMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerDiscardedMessages.setStatus(_A)
_AgentDhcp6ServerSOLICITMessagesReceived_Type=Counter32
_AgentDhcp6ServerSOLICITMessagesReceived_Object=MibScalar
agentDhcp6ServerSOLICITMessagesReceived=_AgentDhcp6ServerSOLICITMessagesReceived_Object((1,3,6,1,4,1,4413,1,1,25,1,7),_AgentDhcp6ServerSOLICITMessagesReceived_Type())
agentDhcp6ServerSOLICITMessagesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerSOLICITMessagesReceived.setStatus(_A)
_AgentDhcp6ServerREQUESTMessagesReceived_Type=Counter32
_AgentDhcp6ServerREQUESTMessagesReceived_Object=MibScalar
agentDhcp6ServerREQUESTMessagesReceived=_AgentDhcp6ServerREQUESTMessagesReceived_Object((1,3,6,1,4,1,4413,1,1,25,1,8),_AgentDhcp6ServerREQUESTMessagesReceived_Type())
agentDhcp6ServerREQUESTMessagesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerREQUESTMessagesReceived.setStatus(_A)
_AgentDhcp6ServerCONFIRMMessagesReceived_Type=Counter32
_AgentDhcp6ServerCONFIRMMessagesReceived_Object=MibScalar
agentDhcp6ServerCONFIRMMessagesReceived=_AgentDhcp6ServerCONFIRMMessagesReceived_Object((1,3,6,1,4,1,4413,1,1,25,1,9),_AgentDhcp6ServerCONFIRMMessagesReceived_Type())
agentDhcp6ServerCONFIRMMessagesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerCONFIRMMessagesReceived.setStatus(_A)
_AgentDhcp6ServerRENEWMessagesReceived_Type=Counter32
_AgentDhcp6ServerRENEWMessagesReceived_Object=MibScalar
agentDhcp6ServerRENEWMessagesReceived=_AgentDhcp6ServerRENEWMessagesReceived_Object((1,3,6,1,4,1,4413,1,1,25,1,10),_AgentDhcp6ServerRENEWMessagesReceived_Type())
agentDhcp6ServerRENEWMessagesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerRENEWMessagesReceived.setStatus(_A)
_AgentDhcp6ServerREBINDMessagesReceived_Type=Counter32
_AgentDhcp6ServerREBINDMessagesReceived_Object=MibScalar
agentDhcp6ServerREBINDMessagesReceived=_AgentDhcp6ServerREBINDMessagesReceived_Object((1,3,6,1,4,1,4413,1,1,25,1,11),_AgentDhcp6ServerREBINDMessagesReceived_Type())
agentDhcp6ServerREBINDMessagesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerREBINDMessagesReceived.setStatus(_A)
_AgentDhcp6ServerRELEASEMessagesReceived_Type=Counter32
_AgentDhcp6ServerRELEASEMessagesReceived_Object=MibScalar
agentDhcp6ServerRELEASEMessagesReceived=_AgentDhcp6ServerRELEASEMessagesReceived_Object((1,3,6,1,4,1,4413,1,1,25,1,12),_AgentDhcp6ServerRELEASEMessagesReceived_Type())
agentDhcp6ServerRELEASEMessagesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerRELEASEMessagesReceived.setStatus(_A)
_AgentDhcp6ServerDECLINEMessagesReceived_Type=Counter32
_AgentDhcp6ServerDECLINEMessagesReceived_Object=MibScalar
agentDhcp6ServerDECLINEMessagesReceived=_AgentDhcp6ServerDECLINEMessagesReceived_Object((1,3,6,1,4,1,4413,1,1,25,1,13),_AgentDhcp6ServerDECLINEMessagesReceived_Type())
agentDhcp6ServerDECLINEMessagesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerDECLINEMessagesReceived.setStatus(_A)
_AgentDhcp6ServerINFORMREQMessagesReceived_Type=Counter32
_AgentDhcp6ServerINFORMREQMessagesReceived_Object=MibScalar
agentDhcp6ServerINFORMREQMessagesReceived=_AgentDhcp6ServerINFORMREQMessagesReceived_Object((1,3,6,1,4,1,4413,1,1,25,1,14),_AgentDhcp6ServerINFORMREQMessagesReceived_Type())
agentDhcp6ServerINFORMREQMessagesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerINFORMREQMessagesReceived.setStatus(_A)
_AgentDhcp6ServerRELAYREPLYMessagesReceived_Type=Counter32
_AgentDhcp6ServerRELAYREPLYMessagesReceived_Object=MibScalar
agentDhcp6ServerRELAYREPLYMessagesReceived=_AgentDhcp6ServerRELAYREPLYMessagesReceived_Object((1,3,6,1,4,1,4413,1,1,25,1,15),_AgentDhcp6ServerRELAYREPLYMessagesReceived_Type())
agentDhcp6ServerRELAYREPLYMessagesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerRELAYREPLYMessagesReceived.setStatus(_A)
_AgentDhcp6ServerRELAYFORWMessagesReceived_Type=Counter32
_AgentDhcp6ServerRELAYFORWMessagesReceived_Object=MibScalar
agentDhcp6ServerRELAYFORWMessagesReceived=_AgentDhcp6ServerRELAYFORWMessagesReceived_Object((1,3,6,1,4,1,4413,1,1,25,1,16),_AgentDhcp6ServerRELAYFORWMessagesReceived_Type())
agentDhcp6ServerRELAYFORWMessagesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerRELAYFORWMessagesReceived.setStatus(_A)
_AgentDhcp6ServerADVERTISEMessagesSent_Type=Counter32
_AgentDhcp6ServerADVERTISEMessagesSent_Object=MibScalar
agentDhcp6ServerADVERTISEMessagesSent=_AgentDhcp6ServerADVERTISEMessagesSent_Object((1,3,6,1,4,1,4413,1,1,25,1,17),_AgentDhcp6ServerADVERTISEMessagesSent_Type())
agentDhcp6ServerADVERTISEMessagesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerADVERTISEMessagesSent.setStatus(_A)
_AgentDhcp6ServerREPLYMessagesSent_Type=Counter32
_AgentDhcp6ServerREPLYMessagesSent_Object=MibScalar
agentDhcp6ServerREPLYMessagesSent=_AgentDhcp6ServerREPLYMessagesSent_Object((1,3,6,1,4,1,4413,1,1,25,1,18),_AgentDhcp6ServerREPLYMessagesSent_Type())
agentDhcp6ServerREPLYMessagesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerREPLYMessagesSent.setStatus(_A)
_AgentDhcp6ServerRECONFIGUREMessagesSent_Type=Counter32
_AgentDhcp6ServerRECONFIGUREMessagesSent_Object=MibScalar
agentDhcp6ServerRECONFIGUREMessagesSent=_AgentDhcp6ServerRECONFIGUREMessagesSent_Object((1,3,6,1,4,1,4413,1,1,25,1,19),_AgentDhcp6ServerRECONFIGUREMessagesSent_Type())
agentDhcp6ServerRECONFIGUREMessagesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerRECONFIGUREMessagesSent.setStatus(_A)
_AgentDhcp6ServerRELAYREPLYMessagesSent_Type=Counter32
_AgentDhcp6ServerRELAYREPLYMessagesSent_Object=MibScalar
agentDhcp6ServerRELAYREPLYMessagesSent=_AgentDhcp6ServerRELAYREPLYMessagesSent_Object((1,3,6,1,4,1,4413,1,1,25,1,20),_AgentDhcp6ServerRELAYREPLYMessagesSent_Type())
agentDhcp6ServerRELAYREPLYMessagesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerRELAYREPLYMessagesSent.setStatus(_A)
_AgentDhcp6ServerRELAYFORWMessagesSent_Type=Counter32
_AgentDhcp6ServerRELAYFORWMessagesSent_Object=MibScalar
agentDhcp6ServerRELAYFORWMessagesSent=_AgentDhcp6ServerRELAYFORWMessagesSent_Object((1,3,6,1,4,1,4413,1,1,25,1,21),_AgentDhcp6ServerRELAYFORWMessagesSent_Type())
agentDhcp6ServerRELAYFORWMessagesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerRELAYFORWMessagesSent.setStatus(_A)
class _AgentDhcp6ServerClearStatistics_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_AgentDhcp6ServerClearStatistics_Type.__name__=_D
_AgentDhcp6ServerClearStatistics_Object=MibScalar
agentDhcp6ServerClearStatistics=_AgentDhcp6ServerClearStatistics_Object((1,3,6,1,4,1,4413,1,1,25,1,22),_AgentDhcp6ServerClearStatistics_Type())
agentDhcp6ServerClearStatistics.setMaxAccess(_G)
if mibBuilder.loadTexts:agentDhcp6ServerClearStatistics.setStatus(_A)
_AgentDhcp6ServerPoolConfigGroup_ObjectIdentity=ObjectIdentity
agentDhcp6ServerPoolConfigGroup=_AgentDhcp6ServerPoolConfigGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,25,2))
class _AgentDhcp6ServerPoolNameCreate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(1,31))
_AgentDhcp6ServerPoolNameCreate_Type.__name__=_F
_AgentDhcp6ServerPoolNameCreate_Object=MibScalar
agentDhcp6ServerPoolNameCreate=_AgentDhcp6ServerPoolNameCreate_Object((1,3,6,1,4,1,4413,1,1,25,2,1),_AgentDhcp6ServerPoolNameCreate_Type())
agentDhcp6ServerPoolNameCreate.setMaxAccess(_G)
if mibBuilder.loadTexts:agentDhcp6ServerPoolNameCreate.setStatus(_A)
_AgentDhcp6ServerPoolConfigTable_Object=MibTable
agentDhcp6ServerPoolConfigTable=_AgentDhcp6ServerPoolConfigTable_Object((1,3,6,1,4,1,4413,1,1,25,2,2))
if mibBuilder.loadTexts:agentDhcp6ServerPoolConfigTable.setStatus(_A)
_AgentDhcp6ServerPoolConfigEntry_Object=MibTableRow
agentDhcp6ServerPoolConfigEntry=_AgentDhcp6ServerPoolConfigEntry_Object((1,3,6,1,4,1,4413,1,1,25,2,2,1))
agentDhcp6ServerPoolConfigEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:agentDhcp6ServerPoolConfigEntry.setStatus(_A)
class _AgentDhcp6ServerPoolIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_AgentDhcp6ServerPoolIndex_Type.__name__=_I
_AgentDhcp6ServerPoolIndex_Object=MibTableColumn
agentDhcp6ServerPoolIndex=_AgentDhcp6ServerPoolIndex_Object((1,3,6,1,4,1,4413,1,1,25,2,2,1,1),_AgentDhcp6ServerPoolIndex_Type())
agentDhcp6ServerPoolIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerPoolIndex.setStatus(_A)
class _AgentDhcp6ServerPoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AgentDhcp6ServerPoolName_Type.__name__=_F
_AgentDhcp6ServerPoolName_Object=MibTableColumn
agentDhcp6ServerPoolName=_AgentDhcp6ServerPoolName_Object((1,3,6,1,4,1,4413,1,1,25,2,2,1,2),_AgentDhcp6ServerPoolName_Type())
agentDhcp6ServerPoolName.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerPoolName.setStatus(_A)
class _AgentDhcp6ServerPoolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('un-allocated',0),('dynamic',1),('manual',2)))
_AgentDhcp6ServerPoolType_Type.__name__=_D
_AgentDhcp6ServerPoolType_Object=MibTableColumn
agentDhcp6ServerPoolType=_AgentDhcp6ServerPoolType_Object((1,3,6,1,4,1,4413,1,1,25,2,2,1,3),_AgentDhcp6ServerPoolType_Type())
agentDhcp6ServerPoolType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerPoolType.setStatus(_A)
_AgentDhcp6ServerPoolDnsDomainCreate_Type=DisplayString
_AgentDhcp6ServerPoolDnsDomainCreate_Object=MibTableColumn
agentDhcp6ServerPoolDnsDomainCreate=_AgentDhcp6ServerPoolDnsDomainCreate_Object((1,3,6,1,4,1,4413,1,1,25,2,2,1,4),_AgentDhcp6ServerPoolDnsDomainCreate_Type())
agentDhcp6ServerPoolDnsDomainCreate.setMaxAccess(_G)
if mibBuilder.loadTexts:agentDhcp6ServerPoolDnsDomainCreate.setStatus(_A)
_AgentDhcp6ServerPoolDnsServerCreate_Type=Ipv6Address
_AgentDhcp6ServerPoolDnsServerCreate_Object=MibTableColumn
agentDhcp6ServerPoolDnsServerCreate=_AgentDhcp6ServerPoolDnsServerCreate_Object((1,3,6,1,4,1,4413,1,1,25,2,2,1,5),_AgentDhcp6ServerPoolDnsServerCreate_Type())
agentDhcp6ServerPoolDnsServerCreate.setMaxAccess(_G)
if mibBuilder.loadTexts:agentDhcp6ServerPoolDnsServerCreate.setStatus(_A)
_AgentDhcp6ServerPoolRowStatus_Type=RowStatus
_AgentDhcp6ServerPoolRowStatus_Object=MibTableColumn
agentDhcp6ServerPoolRowStatus=_AgentDhcp6ServerPoolRowStatus_Object((1,3,6,1,4,1,4413,1,1,25,2,2,1,6),_AgentDhcp6ServerPoolRowStatus_Type())
agentDhcp6ServerPoolRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:agentDhcp6ServerPoolRowStatus.setStatus(_A)
_AgentDhcp6ServerPoolDnsDomainTable_Object=MibTable
agentDhcp6ServerPoolDnsDomainTable=_AgentDhcp6ServerPoolDnsDomainTable_Object((1,3,6,1,4,1,4413,1,1,25,2,4))
if mibBuilder.loadTexts:agentDhcp6ServerPoolDnsDomainTable.setStatus(_A)
_AgentDhcp6ServerPoolDnsDomainEntry_Object=MibTableRow
agentDhcp6ServerPoolDnsDomainEntry=_AgentDhcp6ServerPoolDnsDomainEntry_Object((1,3,6,1,4,1,4413,1,1,25,2,4,1))
agentDhcp6ServerPoolDnsDomainEntry.setIndexNames((0,_E,_H),(0,_E,_L))
if mibBuilder.loadTexts:agentDhcp6ServerPoolDnsDomainEntry.setStatus(_A)
class _AgentDhcp6ServerPoolDnsDomainIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_AgentDhcp6ServerPoolDnsDomainIndex_Type.__name__=_I
_AgentDhcp6ServerPoolDnsDomainIndex_Object=MibTableColumn
agentDhcp6ServerPoolDnsDomainIndex=_AgentDhcp6ServerPoolDnsDomainIndex_Object((1,3,6,1,4,1,4413,1,1,25,2,4,1,1),_AgentDhcp6ServerPoolDnsDomainIndex_Type())
agentDhcp6ServerPoolDnsDomainIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerPoolDnsDomainIndex.setStatus(_A)
class _AgentDhcp6ServerPoolDnsDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_AgentDhcp6ServerPoolDnsDomainName_Type.__name__=_F
_AgentDhcp6ServerPoolDnsDomainName_Object=MibTableColumn
agentDhcp6ServerPoolDnsDomainName=_AgentDhcp6ServerPoolDnsDomainName_Object((1,3,6,1,4,1,4413,1,1,25,2,4,1,2),_AgentDhcp6ServerPoolDnsDomainName_Type())
agentDhcp6ServerPoolDnsDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerPoolDnsDomainName.setStatus(_A)
_AgentDhcp6ServerPoolDnsDomainRowStatus_Type=RowStatus
_AgentDhcp6ServerPoolDnsDomainRowStatus_Object=MibTableColumn
agentDhcp6ServerPoolDnsDomainRowStatus=_AgentDhcp6ServerPoolDnsDomainRowStatus_Object((1,3,6,1,4,1,4413,1,1,25,2,4,1,3),_AgentDhcp6ServerPoolDnsDomainRowStatus_Type())
agentDhcp6ServerPoolDnsDomainRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:agentDhcp6ServerPoolDnsDomainRowStatus.setStatus(_A)
_AgentDhcp6ServerPoolDnsServerTable_Object=MibTable
agentDhcp6ServerPoolDnsServerTable=_AgentDhcp6ServerPoolDnsServerTable_Object((1,3,6,1,4,1,4413,1,1,25,2,6))
if mibBuilder.loadTexts:agentDhcp6ServerPoolDnsServerTable.setStatus(_A)
_AgentDhcp6ServerPoolDnsServerEntry_Object=MibTableRow
agentDhcp6ServerPoolDnsServerEntry=_AgentDhcp6ServerPoolDnsServerEntry_Object((1,3,6,1,4,1,4413,1,1,25,2,6,1))
agentDhcp6ServerPoolDnsServerEntry.setIndexNames((0,_E,_H),(0,_E,_M))
if mibBuilder.loadTexts:agentDhcp6ServerPoolDnsServerEntry.setStatus(_A)
class _AgentDhcp6ServerPoolDnsServerIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_AgentDhcp6ServerPoolDnsServerIndex_Type.__name__=_I
_AgentDhcp6ServerPoolDnsServerIndex_Object=MibTableColumn
agentDhcp6ServerPoolDnsServerIndex=_AgentDhcp6ServerPoolDnsServerIndex_Object((1,3,6,1,4,1,4413,1,1,25,2,6,1,1),_AgentDhcp6ServerPoolDnsServerIndex_Type())
agentDhcp6ServerPoolDnsServerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerPoolDnsServerIndex.setStatus(_A)
_AgentDhcp6ServerPoolDnsServerAddress_Type=Ipv6Address
_AgentDhcp6ServerPoolDnsServerAddress_Object=MibTableColumn
agentDhcp6ServerPoolDnsServerAddress=_AgentDhcp6ServerPoolDnsServerAddress_Object((1,3,6,1,4,1,4413,1,1,25,2,6,1,2),_AgentDhcp6ServerPoolDnsServerAddress_Type())
agentDhcp6ServerPoolDnsServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerPoolDnsServerAddress.setStatus(_A)
_AgentDhcp6ServerPoolDnsServerRowStatus_Type=RowStatus
_AgentDhcp6ServerPoolDnsServerRowStatus_Object=MibTableColumn
agentDhcp6ServerPoolDnsServerRowStatus=_AgentDhcp6ServerPoolDnsServerRowStatus_Object((1,3,6,1,4,1,4413,1,1,25,2,6,1,3),_AgentDhcp6ServerPoolDnsServerRowStatus_Type())
agentDhcp6ServerPoolDnsServerRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:agentDhcp6ServerPoolDnsServerRowStatus.setStatus(_A)
_AgentDhcp6ServerPoolAllocationTable_Object=MibTable
agentDhcp6ServerPoolAllocationTable=_AgentDhcp6ServerPoolAllocationTable_Object((1,3,6,1,4,1,4413,1,1,25,2,7))
if mibBuilder.loadTexts:agentDhcp6ServerPoolAllocationTable.setStatus(_A)
_AgentDhcp6ServerPoolAllocationEntry_Object=MibTableRow
agentDhcp6ServerPoolAllocationEntry=_AgentDhcp6ServerPoolAllocationEntry_Object((1,3,6,1,4,1,4413,1,1,25,2,7,1))
agentDhcp6ServerPoolAllocationEntry.setIndexNames((0,_E,_H),(0,_E,_N))
if mibBuilder.loadTexts:agentDhcp6ServerPoolAllocationEntry.setStatus(_A)
_AgentDhcp6ServerPoolAllocationIndex_Type=Unsigned32
_AgentDhcp6ServerPoolAllocationIndex_Object=MibTableColumn
agentDhcp6ServerPoolAllocationIndex=_AgentDhcp6ServerPoolAllocationIndex_Object((1,3,6,1,4,1,4413,1,1,25,2,7,1,1),_AgentDhcp6ServerPoolAllocationIndex_Type())
agentDhcp6ServerPoolAllocationIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerPoolAllocationIndex.setStatus(_A)
class _AgentDhcp6ServerPoolAllocationClientIdentifier_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_AgentDhcp6ServerPoolAllocationClientIdentifier_Type.__name__=_F
_AgentDhcp6ServerPoolAllocationClientIdentifier_Object=MibTableColumn
agentDhcp6ServerPoolAllocationClientIdentifier=_AgentDhcp6ServerPoolAllocationClientIdentifier_Object((1,3,6,1,4,1,4413,1,1,25,2,7,1,2),_AgentDhcp6ServerPoolAllocationClientIdentifier_Type())
agentDhcp6ServerPoolAllocationClientIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcp6ServerPoolAllocationClientIdentifier.setStatus(_A)
_AgentDhcp6ServerPoolAllocationPrefix_Type=Ipv6AddressPrefix
_AgentDhcp6ServerPoolAllocationPrefix_Object=MibTableColumn
agentDhcp6ServerPoolAllocationPrefix=_AgentDhcp6ServerPoolAllocationPrefix_Object((1,3,6,1,4,1,4413,1,1,25,2,7,1,3),_AgentDhcp6ServerPoolAllocationPrefix_Type())
agentDhcp6ServerPoolAllocationPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcp6ServerPoolAllocationPrefix.setStatus(_A)
class _AgentDhcp6ServerPoolAllocationPrefixLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AgentDhcp6ServerPoolAllocationPrefixLength_Type.__name__=_D
_AgentDhcp6ServerPoolAllocationPrefixLength_Object=MibTableColumn
agentDhcp6ServerPoolAllocationPrefixLength=_AgentDhcp6ServerPoolAllocationPrefixLength_Object((1,3,6,1,4,1,4413,1,1,25,2,7,1,4),_AgentDhcp6ServerPoolAllocationPrefixLength_Type())
agentDhcp6ServerPoolAllocationPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcp6ServerPoolAllocationPrefixLength.setStatus(_A)
class _AgentDhcp6ServerPoolAllocationClientName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AgentDhcp6ServerPoolAllocationClientName_Type.__name__=_F
_AgentDhcp6ServerPoolAllocationClientName_Object=MibTableColumn
agentDhcp6ServerPoolAllocationClientName=_AgentDhcp6ServerPoolAllocationClientName_Object((1,3,6,1,4,1,4413,1,1,25,2,7,1,5),_AgentDhcp6ServerPoolAllocationClientName_Type())
agentDhcp6ServerPoolAllocationClientName.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcp6ServerPoolAllocationClientName.setStatus(_A)
_AgentDhcp6ServerPoolAllocationIaid_Type=Unsigned32
_AgentDhcp6ServerPoolAllocationIaid_Object=MibTableColumn
agentDhcp6ServerPoolAllocationIaid=_AgentDhcp6ServerPoolAllocationIaid_Object((1,3,6,1,4,1,4413,1,1,25,2,7,1,6),_AgentDhcp6ServerPoolAllocationIaid_Type())
agentDhcp6ServerPoolAllocationIaid.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcp6ServerPoolAllocationIaid.setStatus(_A)
_AgentDhcp6ServerPoolAllocationValidLifetime_Type=Unsigned32
_AgentDhcp6ServerPoolAllocationValidLifetime_Object=MibTableColumn
agentDhcp6ServerPoolAllocationValidLifetime=_AgentDhcp6ServerPoolAllocationValidLifetime_Object((1,3,6,1,4,1,4413,1,1,25,2,7,1,7),_AgentDhcp6ServerPoolAllocationValidLifetime_Type())
agentDhcp6ServerPoolAllocationValidLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcp6ServerPoolAllocationValidLifetime.setStatus(_A)
_AgentDhcp6ServerPoolAllocationPreferLifetime_Type=Unsigned32
_AgentDhcp6ServerPoolAllocationPreferLifetime_Object=MibTableColumn
agentDhcp6ServerPoolAllocationPreferLifetime=_AgentDhcp6ServerPoolAllocationPreferLifetime_Object((1,3,6,1,4,1,4413,1,1,25,2,7,1,8),_AgentDhcp6ServerPoolAllocationPreferLifetime_Type())
agentDhcp6ServerPoolAllocationPreferLifetime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcp6ServerPoolAllocationPreferLifetime.setStatus(_A)
_AgentDhcp6ServerPoolAllocationRowStatus_Type=RowStatus
_AgentDhcp6ServerPoolAllocationRowStatus_Object=MibTableColumn
agentDhcp6ServerPoolAllocationRowStatus=_AgentDhcp6ServerPoolAllocationRowStatus_Object((1,3,6,1,4,1,4413,1,1,25,2,7,1,9),_AgentDhcp6ServerPoolAllocationRowStatus_Type())
agentDhcp6ServerPoolAllocationRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcp6ServerPoolAllocationRowStatus.setStatus(_A)
_AgentDhcp6InterfaceGroup_ObjectIdentity=ObjectIdentity
agentDhcp6InterfaceGroup=_AgentDhcp6InterfaceGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,25,3))
_AgentDhcp6InterfaceTable_Object=MibTable
agentDhcp6InterfaceTable=_AgentDhcp6InterfaceTable_Object((1,3,6,1,4,1,4413,1,1,25,3,1))
if mibBuilder.loadTexts:agentDhcp6InterfaceTable.setStatus(_A)
_AgentDhcp6InterfaceEntry_Object=MibTableRow
agentDhcp6InterfaceEntry=_AgentDhcp6InterfaceEntry_Object((1,3,6,1,4,1,4413,1,1,25,3,1,1))
agentDhcp6InterfaceEntry.setIndexNames((0,_E,_O))
if mibBuilder.loadTexts:agentDhcp6InterfaceEntry.setStatus(_A)
_AgentDhcp6InterfaceIndex_Type=Ipv6IfIndex
_AgentDhcp6InterfaceIndex_Object=MibTableColumn
agentDhcp6InterfaceIndex=_AgentDhcp6InterfaceIndex_Object((1,3,6,1,4,1,4413,1,1,25,3,1,1,1),_AgentDhcp6InterfaceIndex_Type())
agentDhcp6InterfaceIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:agentDhcp6InterfaceIndex.setStatus(_A)
class _AgentDhcp6InterfaceMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_J,0),('server',1),('relay',2)))
_AgentDhcp6InterfaceMode_Type.__name__=_D
_AgentDhcp6InterfaceMode_Object=MibTableColumn
agentDhcp6InterfaceMode=_AgentDhcp6InterfaceMode_Object((1,3,6,1,4,1,4413,1,1,25,3,1,1,2),_AgentDhcp6InterfaceMode_Type())
agentDhcp6InterfaceMode.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcp6InterfaceMode.setStatus(_A)
class _AgentDhcp6InterfaceServerPoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AgentDhcp6InterfaceServerPoolName_Type.__name__=_F
_AgentDhcp6InterfaceServerPoolName_Object=MibTableColumn
agentDhcp6InterfaceServerPoolName=_AgentDhcp6InterfaceServerPoolName_Object((1,3,6,1,4,1,4413,1,1,25,3,1,1,3),_AgentDhcp6InterfaceServerPoolName_Type())
agentDhcp6InterfaceServerPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcp6InterfaceServerPoolName.setStatus(_A)
_AgentDhcp6InterfaceServerPreference_Type=Unsigned32
_AgentDhcp6InterfaceServerPreference_Object=MibTableColumn
agentDhcp6InterfaceServerPreference=_AgentDhcp6InterfaceServerPreference_Object((1,3,6,1,4,1,4413,1,1,25,3,1,1,4),_AgentDhcp6InterfaceServerPreference_Type())
agentDhcp6InterfaceServerPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcp6InterfaceServerPreference.setStatus(_A)
_AgentDhcp6InterfaceRelayAddress_Type=Ipv6Address
_AgentDhcp6InterfaceRelayAddress_Object=MibTableColumn
agentDhcp6InterfaceRelayAddress=_AgentDhcp6InterfaceRelayAddress_Object((1,3,6,1,4,1,4413,1,1,25,3,1,1,5),_AgentDhcp6InterfaceRelayAddress_Type())
agentDhcp6InterfaceRelayAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcp6InterfaceRelayAddress.setStatus(_A)
_AgentDhcp6InterfaceRelayInterface_Type=Ipv6IfIndexOrZero
_AgentDhcp6InterfaceRelayInterface_Object=MibTableColumn
agentDhcp6InterfaceRelayInterface=_AgentDhcp6InterfaceRelayInterface_Object((1,3,6,1,4,1,4413,1,1,25,3,1,1,6),_AgentDhcp6InterfaceRelayInterface_Type())
agentDhcp6InterfaceRelayInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcp6InterfaceRelayInterface.setStatus(_A)
class _AgentDhcp6InterfaceRemoteIdentifier_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AgentDhcp6InterfaceRemoteIdentifier_Type.__name__=_F
_AgentDhcp6InterfaceRemoteIdentifier_Object=MibTableColumn
agentDhcp6InterfaceRemoteIdentifier=_AgentDhcp6InterfaceRemoteIdentifier_Object((1,3,6,1,4,1,4413,1,1,25,3,1,1,7),_AgentDhcp6InterfaceRemoteIdentifier_Type())
agentDhcp6InterfaceRemoteIdentifier.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcp6InterfaceRemoteIdentifier.setStatus(_A)
class _AgentDhcp6InterfaceOptionFlags_Type(Bits):namedValues=NamedValues(*(('rapid-commit',0),('allow-unicast',1)))
_AgentDhcp6InterfaceOptionFlags_Type.__name__='Bits'
_AgentDhcp6InterfaceOptionFlags_Object=MibTableColumn
agentDhcp6InterfaceOptionFlags=_AgentDhcp6InterfaceOptionFlags_Object((1,3,6,1,4,1,4413,1,1,25,3,1,1,8),_AgentDhcp6InterfaceOptionFlags_Type())
agentDhcp6InterfaceOptionFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcp6InterfaceOptionFlags.setStatus(_A)
_AgentDhcp6InterfaceStatsTable_Object=MibTable
agentDhcp6InterfaceStatsTable=_AgentDhcp6InterfaceStatsTable_Object((1,3,6,1,4,1,4413,1,1,25,3,2))
if mibBuilder.loadTexts:agentDhcp6InterfaceStatsTable.setStatus(_A)
_AgentDhcp6InterfaceStatsEntry_Object=MibTableRow
agentDhcp6InterfaceStatsEntry=_AgentDhcp6InterfaceStatsEntry_Object((1,3,6,1,4,1,4413,1,1,25,3,2,1))
agentDhcp6InterfaceStatsEntry.setIndexNames((0,_E,_Q))
if mibBuilder.loadTexts:agentDhcp6InterfaceStatsEntry.setStatus(_A)
_AgentDhcp6InterfaceStatsIndex_Type=Ipv6IfIndex
_AgentDhcp6InterfaceStatsIndex_Object=MibTableColumn
agentDhcp6InterfaceStatsIndex=_AgentDhcp6InterfaceStatsIndex_Object((1,3,6,1,4,1,4413,1,1,25,3,2,1,1),_AgentDhcp6InterfaceStatsIndex_Type())
agentDhcp6InterfaceStatsIndex.setMaxAccess(_P)
if mibBuilder.loadTexts:agentDhcp6InterfaceStatsIndex.setStatus(_A)
_AgentDhcp6InterfaceMalformedMessagesReceived_Type=Counter32
_AgentDhcp6InterfaceMalformedMessagesReceived_Object=MibTableColumn
agentDhcp6InterfaceMalformedMessagesReceived=_AgentDhcp6InterfaceMalformedMessagesReceived_Object((1,3,6,1,4,1,4413,1,1,25,3,2,1,2),_AgentDhcp6InterfaceMalformedMessagesReceived_Type())
agentDhcp6InterfaceMalformedMessagesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6InterfaceMalformedMessagesReceived.setStatus(_A)
_AgentDhcp6InterfaceDiscardedMessages_Type=Counter32
_AgentDhcp6InterfaceDiscardedMessages_Object=MibTableColumn
agentDhcp6InterfaceDiscardedMessages=_AgentDhcp6InterfaceDiscardedMessages_Object((1,3,6,1,4,1,4413,1,1,25,3,2,1,3),_AgentDhcp6InterfaceDiscardedMessages_Type())
agentDhcp6InterfaceDiscardedMessages.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6InterfaceDiscardedMessages.setStatus(_A)
_AgentDhcp6InterfaceSOLICITMessagesReceived_Type=Counter32
_AgentDhcp6InterfaceSOLICITMessagesReceived_Object=MibTableColumn
agentDhcp6InterfaceSOLICITMessagesReceived=_AgentDhcp6InterfaceSOLICITMessagesReceived_Object((1,3,6,1,4,1,4413,1,1,25,3,2,1,4),_AgentDhcp6InterfaceSOLICITMessagesReceived_Type())
agentDhcp6InterfaceSOLICITMessagesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6InterfaceSOLICITMessagesReceived.setStatus(_A)
_AgentDhcp6InterfaceREQUESTMessagesReceived_Type=Counter32
_AgentDhcp6InterfaceREQUESTMessagesReceived_Object=MibTableColumn
agentDhcp6InterfaceREQUESTMessagesReceived=_AgentDhcp6InterfaceREQUESTMessagesReceived_Object((1,3,6,1,4,1,4413,1,1,25,3,2,1,5),_AgentDhcp6InterfaceREQUESTMessagesReceived_Type())
agentDhcp6InterfaceREQUESTMessagesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6InterfaceREQUESTMessagesReceived.setStatus(_A)
_AgentDhcp6InterfaceCONFIRMMessagesReceived_Type=Counter32
_AgentDhcp6InterfaceCONFIRMMessagesReceived_Object=MibTableColumn
agentDhcp6InterfaceCONFIRMMessagesReceived=_AgentDhcp6InterfaceCONFIRMMessagesReceived_Object((1,3,6,1,4,1,4413,1,1,25,3,2,1,6),_AgentDhcp6InterfaceCONFIRMMessagesReceived_Type())
agentDhcp6InterfaceCONFIRMMessagesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6InterfaceCONFIRMMessagesReceived.setStatus(_A)
_AgentDhcp6InterfaceRENEWMessagesReceived_Type=Counter32
_AgentDhcp6InterfaceRENEWMessagesReceived_Object=MibTableColumn
agentDhcp6InterfaceRENEWMessagesReceived=_AgentDhcp6InterfaceRENEWMessagesReceived_Object((1,3,6,1,4,1,4413,1,1,25,3,2,1,7),_AgentDhcp6InterfaceRENEWMessagesReceived_Type())
agentDhcp6InterfaceRENEWMessagesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6InterfaceRENEWMessagesReceived.setStatus(_A)
_AgentDhcp6InterfaceREBINDMessagesReceived_Type=Counter32
_AgentDhcp6InterfaceREBINDMessagesReceived_Object=MibTableColumn
agentDhcp6InterfaceREBINDMessagesReceived=_AgentDhcp6InterfaceREBINDMessagesReceived_Object((1,3,6,1,4,1,4413,1,1,25,3,2,1,8),_AgentDhcp6InterfaceREBINDMessagesReceived_Type())
agentDhcp6InterfaceREBINDMessagesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6InterfaceREBINDMessagesReceived.setStatus(_A)
_AgentDhcp6InterfaceRELEASEMessagesReceived_Type=Counter32
_AgentDhcp6InterfaceRELEASEMessagesReceived_Object=MibTableColumn
agentDhcp6InterfaceRELEASEMessagesReceived=_AgentDhcp6InterfaceRELEASEMessagesReceived_Object((1,3,6,1,4,1,4413,1,1,25,3,2,1,9),_AgentDhcp6InterfaceRELEASEMessagesReceived_Type())
agentDhcp6InterfaceRELEASEMessagesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6InterfaceRELEASEMessagesReceived.setStatus(_A)
_AgentDhcp6InterfaceDECLINEMessagesReceived_Type=Counter32
_AgentDhcp6InterfaceDECLINEMessagesReceived_Object=MibTableColumn
agentDhcp6InterfaceDECLINEMessagesReceived=_AgentDhcp6InterfaceDECLINEMessagesReceived_Object((1,3,6,1,4,1,4413,1,1,25,3,2,1,10),_AgentDhcp6InterfaceDECLINEMessagesReceived_Type())
agentDhcp6InterfaceDECLINEMessagesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6InterfaceDECLINEMessagesReceived.setStatus(_A)
_AgentDhcp6InterfaceINFORMREQMessagesReceived_Type=Counter32
_AgentDhcp6InterfaceINFORMREQMessagesReceived_Object=MibTableColumn
agentDhcp6InterfaceINFORMREQMessagesReceived=_AgentDhcp6InterfaceINFORMREQMessagesReceived_Object((1,3,6,1,4,1,4413,1,1,25,3,2,1,11),_AgentDhcp6InterfaceINFORMREQMessagesReceived_Type())
agentDhcp6InterfaceINFORMREQMessagesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6InterfaceINFORMREQMessagesReceived.setStatus(_A)
_AgentDhcp6InterfaceRELAYREPLYMessagesReceived_Type=Counter32
_AgentDhcp6InterfaceRELAYREPLYMessagesReceived_Object=MibTableColumn
agentDhcp6InterfaceRELAYREPLYMessagesReceived=_AgentDhcp6InterfaceRELAYREPLYMessagesReceived_Object((1,3,6,1,4,1,4413,1,1,25,3,2,1,12),_AgentDhcp6InterfaceRELAYREPLYMessagesReceived_Type())
agentDhcp6InterfaceRELAYREPLYMessagesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6InterfaceRELAYREPLYMessagesReceived.setStatus(_A)
_AgentDhcp6InterfaceRELAYFORWMessagesReceived_Type=Counter32
_AgentDhcp6InterfaceRELAYFORWMessagesReceived_Object=MibTableColumn
agentDhcp6InterfaceRELAYFORWMessagesReceived=_AgentDhcp6InterfaceRELAYFORWMessagesReceived_Object((1,3,6,1,4,1,4413,1,1,25,3,2,1,13),_AgentDhcp6InterfaceRELAYFORWMessagesReceived_Type())
agentDhcp6InterfaceRELAYFORWMessagesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6InterfaceRELAYFORWMessagesReceived.setStatus(_A)
_AgentDhcp6InterfaceADVERTISEMessagesSent_Type=Counter32
_AgentDhcp6InterfaceADVERTISEMessagesSent_Object=MibTableColumn
agentDhcp6InterfaceADVERTISEMessagesSent=_AgentDhcp6InterfaceADVERTISEMessagesSent_Object((1,3,6,1,4,1,4413,1,1,25,3,2,1,14),_AgentDhcp6InterfaceADVERTISEMessagesSent_Type())
agentDhcp6InterfaceADVERTISEMessagesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6InterfaceADVERTISEMessagesSent.setStatus(_A)
_AgentDhcp6InterfaceREPLYMessagesSent_Type=Counter32
_AgentDhcp6InterfaceREPLYMessagesSent_Object=MibTableColumn
agentDhcp6InterfaceREPLYMessagesSent=_AgentDhcp6InterfaceREPLYMessagesSent_Object((1,3,6,1,4,1,4413,1,1,25,3,2,1,15),_AgentDhcp6InterfaceREPLYMessagesSent_Type())
agentDhcp6InterfaceREPLYMessagesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6InterfaceREPLYMessagesSent.setStatus(_A)
_AgentDhcp6InterfaceRECONFIGUREMessagesSent_Type=Counter32
_AgentDhcp6InterfaceRECONFIGUREMessagesSent_Object=MibTableColumn
agentDhcp6InterfaceRECONFIGUREMessagesSent=_AgentDhcp6InterfaceRECONFIGUREMessagesSent_Object((1,3,6,1,4,1,4413,1,1,25,3,2,1,16),_AgentDhcp6InterfaceRECONFIGUREMessagesSent_Type())
agentDhcp6InterfaceRECONFIGUREMessagesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6InterfaceRECONFIGUREMessagesSent.setStatus(_A)
_AgentDhcp6InterfaceRELAYREPLYMessagesSent_Type=Counter32
_AgentDhcp6InterfaceRELAYREPLYMessagesSent_Object=MibTableColumn
agentDhcp6InterfaceRELAYREPLYMessagesSent=_AgentDhcp6InterfaceRELAYREPLYMessagesSent_Object((1,3,6,1,4,1,4413,1,1,25,3,2,1,17),_AgentDhcp6InterfaceRELAYREPLYMessagesSent_Type())
agentDhcp6InterfaceRELAYREPLYMessagesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6InterfaceRELAYREPLYMessagesSent.setStatus(_A)
_AgentDhcp6InterfaceRELAYFORWMessagesSent_Type=Counter32
_AgentDhcp6InterfaceRELAYFORWMessagesSent_Object=MibTableColumn
agentDhcp6InterfaceRELAYFORWMessagesSent=_AgentDhcp6InterfaceRELAYFORWMessagesSent_Object((1,3,6,1,4,1,4413,1,1,25,3,2,1,18),_AgentDhcp6InterfaceRELAYFORWMessagesSent_Type())
agentDhcp6InterfaceRELAYFORWMessagesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6InterfaceRELAYFORWMessagesSent.setStatus(_A)
class _AgentDhcp6InterfaceClearStatistics_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_J,2)))
_AgentDhcp6InterfaceClearStatistics_Type.__name__=_D
_AgentDhcp6InterfaceClearStatistics_Object=MibTableColumn
agentDhcp6InterfaceClearStatistics=_AgentDhcp6InterfaceClearStatistics_Object((1,3,6,1,4,1,4413,1,1,25,3,2,1,19),_AgentDhcp6InterfaceClearStatistics_Type())
agentDhcp6InterfaceClearStatistics.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcp6InterfaceClearStatistics.setStatus(_A)
_AgentDhcp6ServerBindingGroup_ObjectIdentity=ObjectIdentity
agentDhcp6ServerBindingGroup=_AgentDhcp6ServerBindingGroup_ObjectIdentity((1,3,6,1,4,1,4413,1,1,25,4))
_AgentDhcp6ServerBindingTable_Object=MibTable
agentDhcp6ServerBindingTable=_AgentDhcp6ServerBindingTable_Object((1,3,6,1,4,1,4413,1,1,25,4,1))
if mibBuilder.loadTexts:agentDhcp6ServerBindingTable.setStatus(_A)
_AgentDhcp6ServerBindingEntry_Object=MibTableRow
agentDhcp6ServerBindingEntry=_AgentDhcp6ServerBindingEntry_Object((1,3,6,1,4,1,4413,1,1,25,4,1,1))
agentDhcp6ServerBindingEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:agentDhcp6ServerBindingEntry.setStatus(_A)
_AgentDhcp6ServerBindingIndex_Type=Unsigned32
_AgentDhcp6ServerBindingIndex_Object=MibTableColumn
agentDhcp6ServerBindingIndex=_AgentDhcp6ServerBindingIndex_Object((1,3,6,1,4,1,4413,1,1,25,4,1,1,1),_AgentDhcp6ServerBindingIndex_Type())
agentDhcp6ServerBindingIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerBindingIndex.setStatus(_A)
_AgentDhcp6ServerBindingPrefix_Type=Ipv6AddressPrefix
_AgentDhcp6ServerBindingPrefix_Object=MibTableColumn
agentDhcp6ServerBindingPrefix=_AgentDhcp6ServerBindingPrefix_Object((1,3,6,1,4,1,4413,1,1,25,4,1,1,2),_AgentDhcp6ServerBindingPrefix_Type())
agentDhcp6ServerBindingPrefix.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerBindingPrefix.setStatus(_A)
class _AgentDhcp6ServerBindingPrefixLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_AgentDhcp6ServerBindingPrefixLength_Type.__name__=_D
_AgentDhcp6ServerBindingPrefixLength_Object=MibTableColumn
agentDhcp6ServerBindingPrefixLength=_AgentDhcp6ServerBindingPrefixLength_Object((1,3,6,1,4,1,4413,1,1,25,4,1,1,3),_AgentDhcp6ServerBindingPrefixLength_Type())
agentDhcp6ServerBindingPrefixLength.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerBindingPrefixLength.setStatus(_A)
class _AgentDhcp6ServerBindingPrefixType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('iapd',0))
_AgentDhcp6ServerBindingPrefixType_Type.__name__=_D
_AgentDhcp6ServerBindingPrefixType_Object=MibTableColumn
agentDhcp6ServerBindingPrefixType=_AgentDhcp6ServerBindingPrefixType_Object((1,3,6,1,4,1,4413,1,1,25,4,1,1,4),_AgentDhcp6ServerBindingPrefixType_Type())
agentDhcp6ServerBindingPrefixType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerBindingPrefixType.setStatus(_A)
class _AgentDhcp6ServerBindingClientIdentifier_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_AgentDhcp6ServerBindingClientIdentifier_Type.__name__=_F
_AgentDhcp6ServerBindingClientIdentifier_Object=MibTableColumn
agentDhcp6ServerBindingClientIdentifier=_AgentDhcp6ServerBindingClientIdentifier_Object((1,3,6,1,4,1,4413,1,1,25,4,1,1,5),_AgentDhcp6ServerBindingClientIdentifier_Type())
agentDhcp6ServerBindingClientIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerBindingClientIdentifier.setStatus(_A)
_AgentDhcp6ServerBindingClientAddress_Type=Ipv6Address
_AgentDhcp6ServerBindingClientAddress_Object=MibTableColumn
agentDhcp6ServerBindingClientAddress=_AgentDhcp6ServerBindingClientAddress_Object((1,3,6,1,4,1,4413,1,1,25,4,1,1,6),_AgentDhcp6ServerBindingClientAddress_Type())
agentDhcp6ServerBindingClientAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerBindingClientAddress.setStatus(_A)
_AgentDhcp6ServerBindingClientInterface_Type=Ipv6IfIndex
_AgentDhcp6ServerBindingClientInterface_Object=MibTableColumn
agentDhcp6ServerBindingClientInterface=_AgentDhcp6ServerBindingClientInterface_Object((1,3,6,1,4,1,4413,1,1,25,4,1,1,7),_AgentDhcp6ServerBindingClientInterface_Type())
agentDhcp6ServerBindingClientInterface.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerBindingClientInterface.setStatus(_A)
_AgentDhcp6ServerBindingIaid_Type=Unsigned32
_AgentDhcp6ServerBindingIaid_Object=MibTableColumn
agentDhcp6ServerBindingIaid=_AgentDhcp6ServerBindingIaid_Object((1,3,6,1,4,1,4413,1,1,25,4,1,1,8),_AgentDhcp6ServerBindingIaid_Type())
agentDhcp6ServerBindingIaid.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerBindingIaid.setStatus(_A)
_AgentDhcp6ServerBindingValidLifetime_Type=Unsigned32
_AgentDhcp6ServerBindingValidLifetime_Object=MibTableColumn
agentDhcp6ServerBindingValidLifetime=_AgentDhcp6ServerBindingValidLifetime_Object((1,3,6,1,4,1,4413,1,1,25,4,1,1,9),_AgentDhcp6ServerBindingValidLifetime_Type())
agentDhcp6ServerBindingValidLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerBindingValidLifetime.setStatus(_A)
_AgentDhcp6ServerBindingPreferLifetime_Type=Unsigned32
_AgentDhcp6ServerBindingPreferLifetime_Object=MibTableColumn
agentDhcp6ServerBindingPreferLifetime=_AgentDhcp6ServerBindingPreferLifetime_Object((1,3,6,1,4,1,4413,1,1,25,4,1,1,10),_AgentDhcp6ServerBindingPreferLifetime_Type())
agentDhcp6ServerBindingPreferLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerBindingPreferLifetime.setStatus(_A)
_AgentDhcp6ServerBindingExpiration_Type=Unsigned32
_AgentDhcp6ServerBindingExpiration_Object=MibTableColumn
agentDhcp6ServerBindingExpiration=_AgentDhcp6ServerBindingExpiration_Object((1,3,6,1,4,1,4413,1,1,25,4,1,1,11),_AgentDhcp6ServerBindingExpiration_Type())
agentDhcp6ServerBindingExpiration.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcp6ServerBindingExpiration.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'fastPathDHCP6ServerPrivate':fastPathDHCP6ServerPrivate,'agentDhcp6ServerGroup':agentDhcp6ServerGroup,'agentDhcp6ServerAdminMode':agentDhcp6ServerAdminMode,'agentDhcp6ServerRelayOptParm':agentDhcp6ServerRelayOptParm,'agentDhcp6ServerRelayOptRemoteIdSuboptParm':agentDhcp6ServerRelayOptRemoteIdSuboptParm,'agentDhcp6ServerDuid':agentDhcp6ServerDuid,'agentDhcp6ServerMalformedMessagesReceived':agentDhcp6ServerMalformedMessagesReceived,'agentDhcp6ServerDiscardedMessages':agentDhcp6ServerDiscardedMessages,'agentDhcp6ServerSOLICITMessagesReceived':agentDhcp6ServerSOLICITMessagesReceived,'agentDhcp6ServerREQUESTMessagesReceived':agentDhcp6ServerREQUESTMessagesReceived,'agentDhcp6ServerCONFIRMMessagesReceived':agentDhcp6ServerCONFIRMMessagesReceived,'agentDhcp6ServerRENEWMessagesReceived':agentDhcp6ServerRENEWMessagesReceived,'agentDhcp6ServerREBINDMessagesReceived':agentDhcp6ServerREBINDMessagesReceived,'agentDhcp6ServerRELEASEMessagesReceived':agentDhcp6ServerRELEASEMessagesReceived,'agentDhcp6ServerDECLINEMessagesReceived':agentDhcp6ServerDECLINEMessagesReceived,'agentDhcp6ServerINFORMREQMessagesReceived':agentDhcp6ServerINFORMREQMessagesReceived,'agentDhcp6ServerRELAYREPLYMessagesReceived':agentDhcp6ServerRELAYREPLYMessagesReceived,'agentDhcp6ServerRELAYFORWMessagesReceived':agentDhcp6ServerRELAYFORWMessagesReceived,'agentDhcp6ServerADVERTISEMessagesSent':agentDhcp6ServerADVERTISEMessagesSent,'agentDhcp6ServerREPLYMessagesSent':agentDhcp6ServerREPLYMessagesSent,'agentDhcp6ServerRECONFIGUREMessagesSent':agentDhcp6ServerRECONFIGUREMessagesSent,'agentDhcp6ServerRELAYREPLYMessagesSent':agentDhcp6ServerRELAYREPLYMessagesSent,'agentDhcp6ServerRELAYFORWMessagesSent':agentDhcp6ServerRELAYFORWMessagesSent,'agentDhcp6ServerClearStatistics':agentDhcp6ServerClearStatistics,'agentDhcp6ServerPoolConfigGroup':agentDhcp6ServerPoolConfigGroup,'agentDhcp6ServerPoolNameCreate':agentDhcp6ServerPoolNameCreate,'agentDhcp6ServerPoolConfigTable':agentDhcp6ServerPoolConfigTable,'agentDhcp6ServerPoolConfigEntry':agentDhcp6ServerPoolConfigEntry,_H:agentDhcp6ServerPoolIndex,'agentDhcp6ServerPoolName':agentDhcp6ServerPoolName,'agentDhcp6ServerPoolType':agentDhcp6ServerPoolType,'agentDhcp6ServerPoolDnsDomainCreate':agentDhcp6ServerPoolDnsDomainCreate,'agentDhcp6ServerPoolDnsServerCreate':agentDhcp6ServerPoolDnsServerCreate,'agentDhcp6ServerPoolRowStatus':agentDhcp6ServerPoolRowStatus,'agentDhcp6ServerPoolDnsDomainTable':agentDhcp6ServerPoolDnsDomainTable,'agentDhcp6ServerPoolDnsDomainEntry':agentDhcp6ServerPoolDnsDomainEntry,_L:agentDhcp6ServerPoolDnsDomainIndex,'agentDhcp6ServerPoolDnsDomainName':agentDhcp6ServerPoolDnsDomainName,'agentDhcp6ServerPoolDnsDomainRowStatus':agentDhcp6ServerPoolDnsDomainRowStatus,'agentDhcp6ServerPoolDnsServerTable':agentDhcp6ServerPoolDnsServerTable,'agentDhcp6ServerPoolDnsServerEntry':agentDhcp6ServerPoolDnsServerEntry,_M:agentDhcp6ServerPoolDnsServerIndex,'agentDhcp6ServerPoolDnsServerAddress':agentDhcp6ServerPoolDnsServerAddress,'agentDhcp6ServerPoolDnsServerRowStatus':agentDhcp6ServerPoolDnsServerRowStatus,'agentDhcp6ServerPoolAllocationTable':agentDhcp6ServerPoolAllocationTable,'agentDhcp6ServerPoolAllocationEntry':agentDhcp6ServerPoolAllocationEntry,_N:agentDhcp6ServerPoolAllocationIndex,'agentDhcp6ServerPoolAllocationClientIdentifier':agentDhcp6ServerPoolAllocationClientIdentifier,'agentDhcp6ServerPoolAllocationPrefix':agentDhcp6ServerPoolAllocationPrefix,'agentDhcp6ServerPoolAllocationPrefixLength':agentDhcp6ServerPoolAllocationPrefixLength,'agentDhcp6ServerPoolAllocationClientName':agentDhcp6ServerPoolAllocationClientName,'agentDhcp6ServerPoolAllocationIaid':agentDhcp6ServerPoolAllocationIaid,'agentDhcp6ServerPoolAllocationValidLifetime':agentDhcp6ServerPoolAllocationValidLifetime,'agentDhcp6ServerPoolAllocationPreferLifetime':agentDhcp6ServerPoolAllocationPreferLifetime,'agentDhcp6ServerPoolAllocationRowStatus':agentDhcp6ServerPoolAllocationRowStatus,'agentDhcp6InterfaceGroup':agentDhcp6InterfaceGroup,'agentDhcp6InterfaceTable':agentDhcp6InterfaceTable,'agentDhcp6InterfaceEntry':agentDhcp6InterfaceEntry,_O:agentDhcp6InterfaceIndex,'agentDhcp6InterfaceMode':agentDhcp6InterfaceMode,'agentDhcp6InterfaceServerPoolName':agentDhcp6InterfaceServerPoolName,'agentDhcp6InterfaceServerPreference':agentDhcp6InterfaceServerPreference,'agentDhcp6InterfaceRelayAddress':agentDhcp6InterfaceRelayAddress,'agentDhcp6InterfaceRelayInterface':agentDhcp6InterfaceRelayInterface,'agentDhcp6InterfaceRemoteIdentifier':agentDhcp6InterfaceRemoteIdentifier,'agentDhcp6InterfaceOptionFlags':agentDhcp6InterfaceOptionFlags,'agentDhcp6InterfaceStatsTable':agentDhcp6InterfaceStatsTable,'agentDhcp6InterfaceStatsEntry':agentDhcp6InterfaceStatsEntry,_Q:agentDhcp6InterfaceStatsIndex,'agentDhcp6InterfaceMalformedMessagesReceived':agentDhcp6InterfaceMalformedMessagesReceived,'agentDhcp6InterfaceDiscardedMessages':agentDhcp6InterfaceDiscardedMessages,'agentDhcp6InterfaceSOLICITMessagesReceived':agentDhcp6InterfaceSOLICITMessagesReceived,'agentDhcp6InterfaceREQUESTMessagesReceived':agentDhcp6InterfaceREQUESTMessagesReceived,'agentDhcp6InterfaceCONFIRMMessagesReceived':agentDhcp6InterfaceCONFIRMMessagesReceived,'agentDhcp6InterfaceRENEWMessagesReceived':agentDhcp6InterfaceRENEWMessagesReceived,'agentDhcp6InterfaceREBINDMessagesReceived':agentDhcp6InterfaceREBINDMessagesReceived,'agentDhcp6InterfaceRELEASEMessagesReceived':agentDhcp6InterfaceRELEASEMessagesReceived,'agentDhcp6InterfaceDECLINEMessagesReceived':agentDhcp6InterfaceDECLINEMessagesReceived,'agentDhcp6InterfaceINFORMREQMessagesReceived':agentDhcp6InterfaceINFORMREQMessagesReceived,'agentDhcp6InterfaceRELAYREPLYMessagesReceived':agentDhcp6InterfaceRELAYREPLYMessagesReceived,'agentDhcp6InterfaceRELAYFORWMessagesReceived':agentDhcp6InterfaceRELAYFORWMessagesReceived,'agentDhcp6InterfaceADVERTISEMessagesSent':agentDhcp6InterfaceADVERTISEMessagesSent,'agentDhcp6InterfaceREPLYMessagesSent':agentDhcp6InterfaceREPLYMessagesSent,'agentDhcp6InterfaceRECONFIGUREMessagesSent':agentDhcp6InterfaceRECONFIGUREMessagesSent,'agentDhcp6InterfaceRELAYREPLYMessagesSent':agentDhcp6InterfaceRELAYREPLYMessagesSent,'agentDhcp6InterfaceRELAYFORWMessagesSent':agentDhcp6InterfaceRELAYFORWMessagesSent,'agentDhcp6InterfaceClearStatistics':agentDhcp6InterfaceClearStatistics,'agentDhcp6ServerBindingGroup':agentDhcp6ServerBindingGroup,'agentDhcp6ServerBindingTable':agentDhcp6ServerBindingTable,'agentDhcp6ServerBindingEntry':agentDhcp6ServerBindingEntry,_R:agentDhcp6ServerBindingIndex,'agentDhcp6ServerBindingPrefix':agentDhcp6ServerBindingPrefix,'agentDhcp6ServerBindingPrefixLength':agentDhcp6ServerBindingPrefixLength,'agentDhcp6ServerBindingPrefixType':agentDhcp6ServerBindingPrefixType,'agentDhcp6ServerBindingClientIdentifier':agentDhcp6ServerBindingClientIdentifier,'agentDhcp6ServerBindingClientAddress':agentDhcp6ServerBindingClientAddress,'agentDhcp6ServerBindingClientInterface':agentDhcp6ServerBindingClientInterface,'agentDhcp6ServerBindingIaid':agentDhcp6ServerBindingIaid,'agentDhcp6ServerBindingValidLifetime':agentDhcp6ServerBindingValidLifetime,'agentDhcp6ServerBindingPreferLifetime':agentDhcp6ServerBindingPreferLifetime,'agentDhcp6ServerBindingExpiration':agentDhcp6ServerBindingExpiration})