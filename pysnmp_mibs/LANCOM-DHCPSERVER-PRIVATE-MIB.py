_S='agentDhcpServerPoolAllocationEntry'
_R='agentDhcpServerAddressConflictIP'
_Q='agentDhcpServerLeaseLeaseIndex'
_P='agentDhcpServerPoolOptionCode'
_O='agentDhcpServerPoolOptionIndex'
_N='agentDhcpServerExcludedRangeIndex'
_M='dynamic'
_L='un-allocated'
_K='agentDhcpServerPoolIndex'
_J='manual'
_I='disable'
_H='enable'
_G='Unsigned32'
_F='LANCOM-DHCPSERVER-PRIVATE-MIB'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fastPath,=mibBuilder.importSymbols('LANCOM-REF-MIB','fastPath')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,MacAddress,PhysAddress,RowPointer,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'MacAddress','PhysAddress','RowPointer','RowStatus','StorageType','TextualConvention','TruthValue')
fastPathDHCPServerPrivate=ModuleIdentity((1,3,6,1,4,1,2356,16,1,12))
if mibBuilder.loadTexts:fastPathDHCPServerPrivate.setRevisions(('2011-01-26 00:00','2007-05-23 00:00'))
_AgentDhcpServerGroup_ObjectIdentity=ObjectIdentity
agentDhcpServerGroup=_AgentDhcpServerGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,12,1))
class _AgentDhcpServerAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AgentDhcpServerAdminMode_Type.__name__=_D
_AgentDhcpServerAdminMode_Object=MibScalar
agentDhcpServerAdminMode=_AgentDhcpServerAdminMode_Object((1,3,6,1,4,1,2356,16,1,12,1,1),_AgentDhcpServerAdminMode_Type())
agentDhcpServerAdminMode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerAdminMode.setStatus(_A)
class _AgentDhcpServerPingPktNos_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2,10))
_AgentDhcpServerPingPktNos_Type.__name__=_D
_AgentDhcpServerPingPktNos_Object=MibScalar
agentDhcpServerPingPktNos=_AgentDhcpServerPingPktNos_Object((1,3,6,1,4,1,2356,16,1,12,1,2),_AgentDhcpServerPingPktNos_Type())
agentDhcpServerPingPktNos.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerPingPktNos.setStatus(_A)
_AgentDhcpServerAutomaticBindingsNos_Type=Counter32
_AgentDhcpServerAutomaticBindingsNos_Object=MibScalar
agentDhcpServerAutomaticBindingsNos=_AgentDhcpServerAutomaticBindingsNos_Object((1,3,6,1,4,1,2356,16,1,12,1,3),_AgentDhcpServerAutomaticBindingsNos_Type())
agentDhcpServerAutomaticBindingsNos.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerAutomaticBindingsNos.setStatus(_A)
_AgentDhcpServerExpiredBindingsNos_Type=Counter32
_AgentDhcpServerExpiredBindingsNos_Object=MibScalar
agentDhcpServerExpiredBindingsNos=_AgentDhcpServerExpiredBindingsNos_Object((1,3,6,1,4,1,2356,16,1,12,1,4),_AgentDhcpServerExpiredBindingsNos_Type())
agentDhcpServerExpiredBindingsNos.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerExpiredBindingsNos.setStatus(_A)
_AgentDhcpServerMalformedMessagesReceived_Type=Counter32
_AgentDhcpServerMalformedMessagesReceived_Object=MibScalar
agentDhcpServerMalformedMessagesReceived=_AgentDhcpServerMalformedMessagesReceived_Object((1,3,6,1,4,1,2356,16,1,12,1,5),_AgentDhcpServerMalformedMessagesReceived_Type())
agentDhcpServerMalformedMessagesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerMalformedMessagesReceived.setStatus(_A)
_AgentDhcpServerDISCOVERMessagesReceived_Type=Counter32
_AgentDhcpServerDISCOVERMessagesReceived_Object=MibScalar
agentDhcpServerDISCOVERMessagesReceived=_AgentDhcpServerDISCOVERMessagesReceived_Object((1,3,6,1,4,1,2356,16,1,12,1,6),_AgentDhcpServerDISCOVERMessagesReceived_Type())
agentDhcpServerDISCOVERMessagesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerDISCOVERMessagesReceived.setStatus(_A)
_AgentDhcpServerREQUESTMessagesReceived_Type=Counter32
_AgentDhcpServerREQUESTMessagesReceived_Object=MibScalar
agentDhcpServerREQUESTMessagesReceived=_AgentDhcpServerREQUESTMessagesReceived_Object((1,3,6,1,4,1,2356,16,1,12,1,7),_AgentDhcpServerREQUESTMessagesReceived_Type())
agentDhcpServerREQUESTMessagesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerREQUESTMessagesReceived.setStatus(_A)
_AgentDhcpServerDECLINEMessagesReceived_Type=Counter32
_AgentDhcpServerDECLINEMessagesReceived_Object=MibScalar
agentDhcpServerDECLINEMessagesReceived=_AgentDhcpServerDECLINEMessagesReceived_Object((1,3,6,1,4,1,2356,16,1,12,1,8),_AgentDhcpServerDECLINEMessagesReceived_Type())
agentDhcpServerDECLINEMessagesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerDECLINEMessagesReceived.setStatus(_A)
_AgentDhcpServerRELEASEMessagesReceived_Type=Counter32
_AgentDhcpServerRELEASEMessagesReceived_Object=MibScalar
agentDhcpServerRELEASEMessagesReceived=_AgentDhcpServerRELEASEMessagesReceived_Object((1,3,6,1,4,1,2356,16,1,12,1,9),_AgentDhcpServerRELEASEMessagesReceived_Type())
agentDhcpServerRELEASEMessagesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerRELEASEMessagesReceived.setStatus(_A)
_AgentDhcpServerINFORMMessagesReceived_Type=Counter32
_AgentDhcpServerINFORMMessagesReceived_Object=MibScalar
agentDhcpServerINFORMMessagesReceived=_AgentDhcpServerINFORMMessagesReceived_Object((1,3,6,1,4,1,2356,16,1,12,1,10),_AgentDhcpServerINFORMMessagesReceived_Type())
agentDhcpServerINFORMMessagesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerINFORMMessagesReceived.setStatus(_A)
_AgentDhcpServerOFFERMessagesSent_Type=Counter32
_AgentDhcpServerOFFERMessagesSent_Object=MibScalar
agentDhcpServerOFFERMessagesSent=_AgentDhcpServerOFFERMessagesSent_Object((1,3,6,1,4,1,2356,16,1,12,1,11),_AgentDhcpServerOFFERMessagesSent_Type())
agentDhcpServerOFFERMessagesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerOFFERMessagesSent.setStatus(_A)
_AgentDhcpServerACKMessagesSent_Type=Counter32
_AgentDhcpServerACKMessagesSent_Object=MibScalar
agentDhcpServerACKMessagesSent=_AgentDhcpServerACKMessagesSent_Object((1,3,6,1,4,1,2356,16,1,12,1,12),_AgentDhcpServerACKMessagesSent_Type())
agentDhcpServerACKMessagesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerACKMessagesSent.setStatus(_A)
_AgentDhcpServerNAKMessagesSent_Type=Counter32
_AgentDhcpServerNAKMessagesSent_Object=MibScalar
agentDhcpServerNAKMessagesSent=_AgentDhcpServerNAKMessagesSent_Object((1,3,6,1,4,1,2356,16,1,12,1,13),_AgentDhcpServerNAKMessagesSent_Type())
agentDhcpServerNAKMessagesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerNAKMessagesSent.setStatus(_A)
class _AgentDhcpServerClearStatistics_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AgentDhcpServerClearStatistics_Type.__name__=_D
_AgentDhcpServerClearStatistics_Object=MibScalar
agentDhcpServerClearStatistics=_AgentDhcpServerClearStatistics_Object((1,3,6,1,4,1,2356,16,1,12,1,14),_AgentDhcpServerClearStatistics_Type())
agentDhcpServerClearStatistics.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerClearStatistics.setStatus(_A)
class _AgentDhcpServerBootpAutomatic_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AgentDhcpServerBootpAutomatic_Type.__name__=_D
_AgentDhcpServerBootpAutomatic_Object=MibScalar
agentDhcpServerBootpAutomatic=_AgentDhcpServerBootpAutomatic_Object((1,3,6,1,4,1,2356,16,1,12,1,15),_AgentDhcpServerBootpAutomatic_Type())
agentDhcpServerBootpAutomatic.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerBootpAutomatic.setStatus(_A)
_AgentDhcpServerDISCOVERMessagesDiscarded_Type=Counter32
_AgentDhcpServerDISCOVERMessagesDiscarded_Object=MibScalar
agentDhcpServerDISCOVERMessagesDiscarded=_AgentDhcpServerDISCOVERMessagesDiscarded_Object((1,3,6,1,4,1,2356,16,1,12,1,16),_AgentDhcpServerDISCOVERMessagesDiscarded_Type())
agentDhcpServerDISCOVERMessagesDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerDISCOVERMessagesDiscarded.setStatus(_A)
_AgentDhcpServerPoolConfigGroup_ObjectIdentity=ObjectIdentity
agentDhcpServerPoolConfigGroup=_AgentDhcpServerPoolConfigGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,12,2))
class _AgentDhcpServerPoolNameCreate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(1,31))
_AgentDhcpServerPoolNameCreate_Type.__name__=_E
_AgentDhcpServerPoolNameCreate_Object=MibScalar
agentDhcpServerPoolNameCreate=_AgentDhcpServerPoolNameCreate_Object((1,3,6,1,4,1,2356,16,1,12,2,1),_AgentDhcpServerPoolNameCreate_Type())
agentDhcpServerPoolNameCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerPoolNameCreate.setStatus(_A)
_AgentDhcpServerPoolConfigTable_Object=MibTable
agentDhcpServerPoolConfigTable=_AgentDhcpServerPoolConfigTable_Object((1,3,6,1,4,1,2356,16,1,12,2,2))
if mibBuilder.loadTexts:agentDhcpServerPoolConfigTable.setStatus(_A)
_AgentDhcpServerPoolConfigEntry_Object=MibTableRow
agentDhcpServerPoolConfigEntry=_AgentDhcpServerPoolConfigEntry_Object((1,3,6,1,4,1,2356,16,1,12,2,2,1))
agentDhcpServerPoolConfigEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:agentDhcpServerPoolConfigEntry.setStatus(_A)
class _AgentDhcpServerPoolIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_AgentDhcpServerPoolIndex_Type.__name__=_G
_AgentDhcpServerPoolIndex_Object=MibTableColumn
agentDhcpServerPoolIndex=_AgentDhcpServerPoolIndex_Object((1,3,6,1,4,1,2356,16,1,12,2,2,1,1),_AgentDhcpServerPoolIndex_Type())
agentDhcpServerPoolIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerPoolIndex.setStatus(_A)
class _AgentDhcpServerPoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AgentDhcpServerPoolName_Type.__name__=_E
_AgentDhcpServerPoolName_Object=MibTableColumn
agentDhcpServerPoolName=_AgentDhcpServerPoolName_Object((1,3,6,1,4,1,2356,16,1,12,2,2,1,2),_AgentDhcpServerPoolName_Type())
agentDhcpServerPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerPoolName.setStatus(_A)
_AgentDhcpServerPoolDefRouter_Type=DisplayString
_AgentDhcpServerPoolDefRouter_Object=MibTableColumn
agentDhcpServerPoolDefRouter=_AgentDhcpServerPoolDefRouter_Object((1,3,6,1,4,1,2356,16,1,12,2,2,1,3),_AgentDhcpServerPoolDefRouter_Type())
agentDhcpServerPoolDefRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerPoolDefRouter.setStatus(_A)
_AgentDhcpServerPoolDNSServer_Type=DisplayString
_AgentDhcpServerPoolDNSServer_Object=MibTableColumn
agentDhcpServerPoolDNSServer=_AgentDhcpServerPoolDNSServer_Object((1,3,6,1,4,1,2356,16,1,12,2,2,1,4),_AgentDhcpServerPoolDNSServer_Type())
agentDhcpServerPoolDNSServer.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerPoolDNSServer.setStatus(_A)
class _AgentDhcpServerPoolLeaseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_AgentDhcpServerPoolLeaseTime_Type.__name__=_D
_AgentDhcpServerPoolLeaseTime_Object=MibTableColumn
agentDhcpServerPoolLeaseTime=_AgentDhcpServerPoolLeaseTime_Object((1,3,6,1,4,1,2356,16,1,12,2,2,1,5),_AgentDhcpServerPoolLeaseTime_Type())
agentDhcpServerPoolLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerPoolLeaseTime.setStatus(_A)
class _AgentDhcpServerPoolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_L,0),(_M,1),(_J,2)))
_AgentDhcpServerPoolType_Type.__name__=_D
_AgentDhcpServerPoolType_Object=MibTableColumn
agentDhcpServerPoolType=_AgentDhcpServerPoolType_Object((1,3,6,1,4,1,2356,16,1,12,2,2,1,6),_AgentDhcpServerPoolType_Type())
agentDhcpServerPoolType.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerPoolType.setStatus(_A)
_AgentDhcpServerPoolNetbiosNameServer_Type=DisplayString
_AgentDhcpServerPoolNetbiosNameServer_Object=MibTableColumn
agentDhcpServerPoolNetbiosNameServer=_AgentDhcpServerPoolNetbiosNameServer_Object((1,3,6,1,4,1,2356,16,1,12,2,2,1,7),_AgentDhcpServerPoolNetbiosNameServer_Type())
agentDhcpServerPoolNetbiosNameServer.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerPoolNetbiosNameServer.setStatus(_A)
class _AgentDhcpServerPoolNetbiosNodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8)));namedValues=NamedValues(*(('none',0),('b-node',1),('p-node',2),('m-node',4),('h-node',8)))
_AgentDhcpServerPoolNetbiosNodeType_Type.__name__=_D
_AgentDhcpServerPoolNetbiosNodeType_Object=MibTableColumn
agentDhcpServerPoolNetbiosNodeType=_AgentDhcpServerPoolNetbiosNodeType_Object((1,3,6,1,4,1,2356,16,1,12,2,2,1,8),_AgentDhcpServerPoolNetbiosNodeType_Type())
agentDhcpServerPoolNetbiosNodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerPoolNetbiosNodeType.setStatus(_A)
_AgentDhcpServerPoolSNTPServer_Type=IpAddress
_AgentDhcpServerPoolSNTPServer_Object=MibTableColumn
agentDhcpServerPoolSNTPServer=_AgentDhcpServerPoolSNTPServer_Object((1,3,6,1,4,1,2356,16,1,12,2,2,1,9),_AgentDhcpServerPoolSNTPServer_Type())
agentDhcpServerPoolSNTPServer.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerPoolSNTPServer.setStatus(_A)
_AgentDhcpServerPoolNextServer_Type=IpAddress
_AgentDhcpServerPoolNextServer_Object=MibTableColumn
agentDhcpServerPoolNextServer=_AgentDhcpServerPoolNextServer_Object((1,3,6,1,4,1,2356,16,1,12,2,2,1,10),_AgentDhcpServerPoolNextServer_Type())
agentDhcpServerPoolNextServer.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerPoolNextServer.setStatus(_A)
class _AgentDhcpServerPoolDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_AgentDhcpServerPoolDomainName_Type.__name__=_E
_AgentDhcpServerPoolDomainName_Object=MibTableColumn
agentDhcpServerPoolDomainName=_AgentDhcpServerPoolDomainName_Object((1,3,6,1,4,1,2356,16,1,12,2,2,1,11),_AgentDhcpServerPoolDomainName_Type())
agentDhcpServerPoolDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerPoolDomainName.setStatus(_A)
class _AgentDhcpServerPoolBootfile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_AgentDhcpServerPoolBootfile_Type.__name__=_E
_AgentDhcpServerPoolBootfile_Object=MibTableColumn
agentDhcpServerPoolBootfile=_AgentDhcpServerPoolBootfile_Object((1,3,6,1,4,1,2356,16,1,12,2,2,1,12),_AgentDhcpServerPoolBootfile_Type())
agentDhcpServerPoolBootfile.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerPoolBootfile.setStatus(_A)
_AgentDhcpServerPoolRowStatus_Type=RowStatus
_AgentDhcpServerPoolRowStatus_Object=MibTableColumn
agentDhcpServerPoolRowStatus=_AgentDhcpServerPoolRowStatus_Object((1,3,6,1,4,1,2356,16,1,12,2,2,1,13),_AgentDhcpServerPoolRowStatus_Type())
agentDhcpServerPoolRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerPoolRowStatus.setStatus(_A)
_AgentDhcpServerPoolAllocationTable_Object=MibTable
agentDhcpServerPoolAllocationTable=_AgentDhcpServerPoolAllocationTable_Object((1,3,6,1,4,1,2356,16,1,12,2,3))
if mibBuilder.loadTexts:agentDhcpServerPoolAllocationTable.setStatus(_A)
_AgentDhcpServerPoolAllocationEntry_Object=MibTableRow
agentDhcpServerPoolAllocationEntry=_AgentDhcpServerPoolAllocationEntry_Object((1,3,6,1,4,1,2356,16,1,12,2,3,1))
if mibBuilder.loadTexts:agentDhcpServerPoolAllocationEntry.setStatus(_A)
class _AgentDhcpServerPoolAllocationName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_AgentDhcpServerPoolAllocationName_Type.__name__=_E
_AgentDhcpServerPoolAllocationName_Object=MibTableColumn
agentDhcpServerPoolAllocationName=_AgentDhcpServerPoolAllocationName_Object((1,3,6,1,4,1,2356,16,1,12,2,3,1,1),_AgentDhcpServerPoolAllocationName_Type())
agentDhcpServerPoolAllocationName.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerPoolAllocationName.setStatus(_A)
_AgentDhcpServerDynamicPoolIpAddress_Type=IpAddress
_AgentDhcpServerDynamicPoolIpAddress_Object=MibTableColumn
agentDhcpServerDynamicPoolIpAddress=_AgentDhcpServerDynamicPoolIpAddress_Object((1,3,6,1,4,1,2356,16,1,12,2,3,1,2),_AgentDhcpServerDynamicPoolIpAddress_Type())
agentDhcpServerDynamicPoolIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerDynamicPoolIpAddress.setStatus(_A)
_AgentDhcpServerDynamicPoolIpMask_Type=IpAddress
_AgentDhcpServerDynamicPoolIpMask_Object=MibTableColumn
agentDhcpServerDynamicPoolIpMask=_AgentDhcpServerDynamicPoolIpMask_Object((1,3,6,1,4,1,2356,16,1,12,2,3,1,3),_AgentDhcpServerDynamicPoolIpMask_Type())
agentDhcpServerDynamicPoolIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerDynamicPoolIpMask.setStatus(_A)
_AgentDhcpServerDynamicPoolIpPrefixLength_Type=Unsigned32
_AgentDhcpServerDynamicPoolIpPrefixLength_Object=MibTableColumn
agentDhcpServerDynamicPoolIpPrefixLength=_AgentDhcpServerDynamicPoolIpPrefixLength_Object((1,3,6,1,4,1,2356,16,1,12,2,3,1,4),_AgentDhcpServerDynamicPoolIpPrefixLength_Type())
agentDhcpServerDynamicPoolIpPrefixLength.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerDynamicPoolIpPrefixLength.setStatus(_A)
class _AgentDhcpServerPoolAllocationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_L,0),(_M,1),(_J,2)))
_AgentDhcpServerPoolAllocationType_Type.__name__=_D
_AgentDhcpServerPoolAllocationType_Object=MibTableColumn
agentDhcpServerPoolAllocationType=_AgentDhcpServerPoolAllocationType_Object((1,3,6,1,4,1,2356,16,1,12,2,3,1,5),_AgentDhcpServerPoolAllocationType_Type())
agentDhcpServerPoolAllocationType.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerPoolAllocationType.setStatus(_A)
_AgentDhcpServerManualPoolClientIdentifier_Type=DisplayString
_AgentDhcpServerManualPoolClientIdentifier_Object=MibTableColumn
agentDhcpServerManualPoolClientIdentifier=_AgentDhcpServerManualPoolClientIdentifier_Object((1,3,6,1,4,1,2356,16,1,12,2,3,1,6),_AgentDhcpServerManualPoolClientIdentifier_Type())
agentDhcpServerManualPoolClientIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerManualPoolClientIdentifier.setStatus(_A)
class _AgentDhcpServerManualPoolClientName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_AgentDhcpServerManualPoolClientName_Type.__name__=_E
_AgentDhcpServerManualPoolClientName_Object=MibTableColumn
agentDhcpServerManualPoolClientName=_AgentDhcpServerManualPoolClientName_Object((1,3,6,1,4,1,2356,16,1,12,2,3,1,7),_AgentDhcpServerManualPoolClientName_Type())
agentDhcpServerManualPoolClientName.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerManualPoolClientName.setStatus(_A)
_AgentDhcpServerManualPoolClientHWAddr_Type=DisplayString
_AgentDhcpServerManualPoolClientHWAddr_Object=MibTableColumn
agentDhcpServerManualPoolClientHWAddr=_AgentDhcpServerManualPoolClientHWAddr_Object((1,3,6,1,4,1,2356,16,1,12,2,3,1,8),_AgentDhcpServerManualPoolClientHWAddr_Type())
agentDhcpServerManualPoolClientHWAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerManualPoolClientHWAddr.setStatus(_A)
class _AgentDhcpServerManualPoolClientHWType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,6)));namedValues=NamedValues(*(('ethernet',1),('ieee802',6)))
_AgentDhcpServerManualPoolClientHWType_Type.__name__=_D
_AgentDhcpServerManualPoolClientHWType_Object=MibTableColumn
agentDhcpServerManualPoolClientHWType=_AgentDhcpServerManualPoolClientHWType_Object((1,3,6,1,4,1,2356,16,1,12,2,3,1,9),_AgentDhcpServerManualPoolClientHWType_Type())
agentDhcpServerManualPoolClientHWType.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerManualPoolClientHWType.setStatus(_A)
_AgentDhcpServerManualPoolIpAddress_Type=IpAddress
_AgentDhcpServerManualPoolIpAddress_Object=MibTableColumn
agentDhcpServerManualPoolIpAddress=_AgentDhcpServerManualPoolIpAddress_Object((1,3,6,1,4,1,2356,16,1,12,2,3,1,10),_AgentDhcpServerManualPoolIpAddress_Type())
agentDhcpServerManualPoolIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerManualPoolIpAddress.setStatus(_A)
_AgentDhcpServerManualPoolIpMask_Type=IpAddress
_AgentDhcpServerManualPoolIpMask_Object=MibTableColumn
agentDhcpServerManualPoolIpMask=_AgentDhcpServerManualPoolIpMask_Object((1,3,6,1,4,1,2356,16,1,12,2,3,1,11),_AgentDhcpServerManualPoolIpMask_Type())
agentDhcpServerManualPoolIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerManualPoolIpMask.setStatus(_A)
_AgentDhcpServerManualPoolIpPrefixLength_Type=Unsigned32
_AgentDhcpServerManualPoolIpPrefixLength_Object=MibTableColumn
agentDhcpServerManualPoolIpPrefixLength=_AgentDhcpServerManualPoolIpPrefixLength_Object((1,3,6,1,4,1,2356,16,1,12,2,3,1,12),_AgentDhcpServerManualPoolIpPrefixLength_Type())
agentDhcpServerManualPoolIpPrefixLength.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerManualPoolIpPrefixLength.setStatus(_A)
class _AgentDhcpServerPoolVrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AgentDhcpServerPoolVrfName_Type.__name__=_E
_AgentDhcpServerPoolVrfName_Object=MibTableColumn
agentDhcpServerPoolVrfName=_AgentDhcpServerPoolVrfName_Object((1,3,6,1,4,1,2356,16,1,12,2,3,1,13),_AgentDhcpServerPoolVrfName_Type())
agentDhcpServerPoolVrfName.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerPoolVrfName.setStatus(_A)
_AgentDhcpServerExcludedAddressRangeCreate_Type=DisplayString
_AgentDhcpServerExcludedAddressRangeCreate_Object=MibScalar
agentDhcpServerExcludedAddressRangeCreate=_AgentDhcpServerExcludedAddressRangeCreate_Object((1,3,6,1,4,1,2356,16,1,12,2,4),_AgentDhcpServerExcludedAddressRangeCreate_Type())
agentDhcpServerExcludedAddressRangeCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerExcludedAddressRangeCreate.setStatus(_A)
_AgentDhcpServerExcludedAddressRangeTable_Object=MibTable
agentDhcpServerExcludedAddressRangeTable=_AgentDhcpServerExcludedAddressRangeTable_Object((1,3,6,1,4,1,2356,16,1,12,2,5))
if mibBuilder.loadTexts:agentDhcpServerExcludedAddressRangeTable.setStatus(_A)
_AgentDhcpServerExcludedAddressRangeEntry_Object=MibTableRow
agentDhcpServerExcludedAddressRangeEntry=_AgentDhcpServerExcludedAddressRangeEntry_Object((1,3,6,1,4,1,2356,16,1,12,2,5,1))
agentDhcpServerExcludedAddressRangeEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:agentDhcpServerExcludedAddressRangeEntry.setStatus(_A)
class _AgentDhcpServerExcludedRangeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_AgentDhcpServerExcludedRangeIndex_Type.__name__=_G
_AgentDhcpServerExcludedRangeIndex_Object=MibTableColumn
agentDhcpServerExcludedRangeIndex=_AgentDhcpServerExcludedRangeIndex_Object((1,3,6,1,4,1,2356,16,1,12,2,5,1,1),_AgentDhcpServerExcludedRangeIndex_Type())
agentDhcpServerExcludedRangeIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerExcludedRangeIndex.setStatus(_A)
_AgentDhcpServerExcludedStartIpAddress_Type=IpAddress
_AgentDhcpServerExcludedStartIpAddress_Object=MibTableColumn
agentDhcpServerExcludedStartIpAddress=_AgentDhcpServerExcludedStartIpAddress_Object((1,3,6,1,4,1,2356,16,1,12,2,5,1,2),_AgentDhcpServerExcludedStartIpAddress_Type())
agentDhcpServerExcludedStartIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerExcludedStartIpAddress.setStatus(_A)
_AgentDhcpServerExcludedEndIpAddress_Type=IpAddress
_AgentDhcpServerExcludedEndIpAddress_Object=MibTableColumn
agentDhcpServerExcludedEndIpAddress=_AgentDhcpServerExcludedEndIpAddress_Object((1,3,6,1,4,1,2356,16,1,12,2,5,1,3),_AgentDhcpServerExcludedEndIpAddress_Type())
agentDhcpServerExcludedEndIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerExcludedEndIpAddress.setStatus(_A)
_AgentDhcpServerExcludedAddressRangeStatus_Type=RowStatus
_AgentDhcpServerExcludedAddressRangeStatus_Object=MibTableColumn
agentDhcpServerExcludedAddressRangeStatus=_AgentDhcpServerExcludedAddressRangeStatus_Object((1,3,6,1,4,1,2356,16,1,12,2,5,1,4),_AgentDhcpServerExcludedAddressRangeStatus_Type())
agentDhcpServerExcludedAddressRangeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerExcludedAddressRangeStatus.setStatus(_A)
class _AgentDhcpServerExcludedVrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AgentDhcpServerExcludedVrfName_Type.__name__=_E
_AgentDhcpServerExcludedVrfName_Object=MibTableColumn
agentDhcpServerExcludedVrfName=_AgentDhcpServerExcludedVrfName_Object((1,3,6,1,4,1,2356,16,1,12,2,5,1,5),_AgentDhcpServerExcludedVrfName_Type())
agentDhcpServerExcludedVrfName.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerExcludedVrfName.setStatus(_A)
_AgentDhcpServerPoolOptionCreate_Type=DisplayString
_AgentDhcpServerPoolOptionCreate_Object=MibScalar
agentDhcpServerPoolOptionCreate=_AgentDhcpServerPoolOptionCreate_Object((1,3,6,1,4,1,2356,16,1,12,2,6),_AgentDhcpServerPoolOptionCreate_Type())
agentDhcpServerPoolOptionCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerPoolOptionCreate.setStatus(_A)
_AgentDhcpServerPoolOptionTable_Object=MibTable
agentDhcpServerPoolOptionTable=_AgentDhcpServerPoolOptionTable_Object((1,3,6,1,4,1,2356,16,1,12,2,7))
if mibBuilder.loadTexts:agentDhcpServerPoolOptionTable.setStatus(_A)
_AgentDhcpServerPoolOptionEntry_Object=MibTableRow
agentDhcpServerPoolOptionEntry=_AgentDhcpServerPoolOptionEntry_Object((1,3,6,1,4,1,2356,16,1,12,2,7,1))
agentDhcpServerPoolOptionEntry.setIndexNames((0,_F,_O),(0,_F,_P))
if mibBuilder.loadTexts:agentDhcpServerPoolOptionEntry.setStatus(_A)
class _AgentDhcpServerPoolOptionIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_AgentDhcpServerPoolOptionIndex_Type.__name__=_G
_AgentDhcpServerPoolOptionIndex_Object=MibTableColumn
agentDhcpServerPoolOptionIndex=_AgentDhcpServerPoolOptionIndex_Object((1,3,6,1,4,1,2356,16,1,12,2,7,1,1),_AgentDhcpServerPoolOptionIndex_Type())
agentDhcpServerPoolOptionIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerPoolOptionIndex.setStatus(_A)
class _AgentDhcpServerPoolOptionCode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_AgentDhcpServerPoolOptionCode_Type.__name__=_G
_AgentDhcpServerPoolOptionCode_Object=MibTableColumn
agentDhcpServerPoolOptionCode=_AgentDhcpServerPoolOptionCode_Object((1,3,6,1,4,1,2356,16,1,12,2,7,1,2),_AgentDhcpServerPoolOptionCode_Type())
agentDhcpServerPoolOptionCode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerPoolOptionCode.setStatus(_A)
class _AgentDhcpServerOptionPoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AgentDhcpServerOptionPoolName_Type.__name__=_E
_AgentDhcpServerOptionPoolName_Object=MibTableColumn
agentDhcpServerOptionPoolName=_AgentDhcpServerOptionPoolName_Object((1,3,6,1,4,1,2356,16,1,12,2,7,1,3),_AgentDhcpServerOptionPoolName_Type())
agentDhcpServerOptionPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerOptionPoolName.setStatus(_A)
class _AgentDhcpServerPoolOptionAsciiData_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,441))
_AgentDhcpServerPoolOptionAsciiData_Type.__name__=_E
_AgentDhcpServerPoolOptionAsciiData_Object=MibTableColumn
agentDhcpServerPoolOptionAsciiData=_AgentDhcpServerPoolOptionAsciiData_Object((1,3,6,1,4,1,2356,16,1,12,2,7,1,4),_AgentDhcpServerPoolOptionAsciiData_Type())
agentDhcpServerPoolOptionAsciiData.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerPoolOptionAsciiData.setStatus(_A)
class _AgentDhcpServerPoolOptionHexData_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1324))
_AgentDhcpServerPoolOptionHexData_Type.__name__=_E
_AgentDhcpServerPoolOptionHexData_Object=MibTableColumn
agentDhcpServerPoolOptionHexData=_AgentDhcpServerPoolOptionHexData_Object((1,3,6,1,4,1,2356,16,1,12,2,7,1,5),_AgentDhcpServerPoolOptionHexData_Type())
agentDhcpServerPoolOptionHexData.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerPoolOptionHexData.setStatus(_A)
_AgentDhcpServerPoolOptionIpAddressData_Type=DisplayString
_AgentDhcpServerPoolOptionIpAddressData_Object=MibTableColumn
agentDhcpServerPoolOptionIpAddressData=_AgentDhcpServerPoolOptionIpAddressData_Object((1,3,6,1,4,1,2356,16,1,12,2,7,1,6),_AgentDhcpServerPoolOptionIpAddressData_Type())
agentDhcpServerPoolOptionIpAddressData.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerPoolOptionIpAddressData.setStatus(_A)
_AgentDhcpServerPoolOptionStatus_Type=RowStatus
_AgentDhcpServerPoolOptionStatus_Object=MibTableColumn
agentDhcpServerPoolOptionStatus=_AgentDhcpServerPoolOptionStatus_Object((1,3,6,1,4,1,2356,16,1,12,2,7,1,7),_AgentDhcpServerPoolOptionStatus_Type())
agentDhcpServerPoolOptionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerPoolOptionStatus.setStatus(_A)
_AgentDhcpServerLeaseGroup_ObjectIdentity=ObjectIdentity
agentDhcpServerLeaseGroup=_AgentDhcpServerLeaseGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,12,3))
class _AgentDhcpServerLeaseClearAllBindings_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AgentDhcpServerLeaseClearAllBindings_Type.__name__=_D
_AgentDhcpServerLeaseClearAllBindings_Object=MibScalar
agentDhcpServerLeaseClearAllBindings=_AgentDhcpServerLeaseClearAllBindings_Object((1,3,6,1,4,1,2356,16,1,12,3,1),_AgentDhcpServerLeaseClearAllBindings_Type())
agentDhcpServerLeaseClearAllBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerLeaseClearAllBindings.setStatus(_A)
_AgentDhcpServerLeaseTable_Object=MibTable
agentDhcpServerLeaseTable=_AgentDhcpServerLeaseTable_Object((1,3,6,1,4,1,2356,16,1,12,3,2))
if mibBuilder.loadTexts:agentDhcpServerLeaseTable.setStatus(_A)
_AgentDhcpServerLeaseEntry_Object=MibTableRow
agentDhcpServerLeaseEntry=_AgentDhcpServerLeaseEntry_Object((1,3,6,1,4,1,2356,16,1,12,3,2,1))
agentDhcpServerLeaseEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:agentDhcpServerLeaseEntry.setStatus(_A)
_AgentDhcpServerLeaseIPAddress_Type=IpAddress
_AgentDhcpServerLeaseIPAddress_Object=MibTableColumn
agentDhcpServerLeaseIPAddress=_AgentDhcpServerLeaseIPAddress_Object((1,3,6,1,4,1,2356,16,1,12,3,2,1,1),_AgentDhcpServerLeaseIPAddress_Type())
agentDhcpServerLeaseIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerLeaseIPAddress.setStatus(_A)
_AgentDhcpServerLeaseIPMask_Type=IpAddress
_AgentDhcpServerLeaseIPMask_Object=MibTableColumn
agentDhcpServerLeaseIPMask=_AgentDhcpServerLeaseIPMask_Object((1,3,6,1,4,1,2356,16,1,12,3,2,1,2),_AgentDhcpServerLeaseIPMask_Type())
agentDhcpServerLeaseIPMask.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerLeaseIPMask.setStatus(_A)
_AgentDhcpServerLeaseHWAddress_Type=MacAddress
_AgentDhcpServerLeaseHWAddress_Object=MibTableColumn
agentDhcpServerLeaseHWAddress=_AgentDhcpServerLeaseHWAddress_Object((1,3,6,1,4,1,2356,16,1,12,3,2,1,3),_AgentDhcpServerLeaseHWAddress_Type())
agentDhcpServerLeaseHWAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerLeaseHWAddress.setStatus(_A)
_AgentDhcpServerLeaseRemainingTime_Type=TimeTicks
_AgentDhcpServerLeaseRemainingTime_Object=MibTableColumn
agentDhcpServerLeaseRemainingTime=_AgentDhcpServerLeaseRemainingTime_Object((1,3,6,1,4,1,2356,16,1,12,3,2,1,4),_AgentDhcpServerLeaseRemainingTime_Type())
agentDhcpServerLeaseRemainingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerLeaseRemainingTime.setStatus(_A)
class _AgentDhcpServerLeaseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('automatic',1),(_J,2)))
_AgentDhcpServerLeaseType_Type.__name__=_D
_AgentDhcpServerLeaseType_Object=MibTableColumn
agentDhcpServerLeaseType=_AgentDhcpServerLeaseType_Object((1,3,6,1,4,1,2356,16,1,12,3,2,1,5),_AgentDhcpServerLeaseType_Type())
agentDhcpServerLeaseType.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerLeaseType.setStatus(_A)
_AgentDhcpServerLeaseStatus_Type=RowStatus
_AgentDhcpServerLeaseStatus_Object=MibTableColumn
agentDhcpServerLeaseStatus=_AgentDhcpServerLeaseStatus_Object((1,3,6,1,4,1,2356,16,1,12,3,2,1,6),_AgentDhcpServerLeaseStatus_Type())
agentDhcpServerLeaseStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerLeaseStatus.setStatus(_A)
class _AgentDhcpServerLeasePoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_AgentDhcpServerLeasePoolName_Type.__name__=_E
_AgentDhcpServerLeasePoolName_Object=MibTableColumn
agentDhcpServerLeasePoolName=_AgentDhcpServerLeasePoolName_Object((1,3,6,1,4,1,2356,16,1,12,3,2,1,7),_AgentDhcpServerLeasePoolName_Type())
agentDhcpServerLeasePoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerLeasePoolName.setStatus(_A)
class _AgentDhcpServerLeaseVrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_AgentDhcpServerLeaseVrfName_Type.__name__=_E
_AgentDhcpServerLeaseVrfName_Object=MibTableColumn
agentDhcpServerLeaseVrfName=_AgentDhcpServerLeaseVrfName_Object((1,3,6,1,4,1,2356,16,1,12,3,2,1,8),_AgentDhcpServerLeaseVrfName_Type())
agentDhcpServerLeaseVrfName.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerLeaseVrfName.setStatus(_A)
class _AgentDhcpServerLeaseLeaseIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4096))
_AgentDhcpServerLeaseLeaseIndex_Type.__name__=_G
_AgentDhcpServerLeaseLeaseIndex_Object=MibTableColumn
agentDhcpServerLeaseLeaseIndex=_AgentDhcpServerLeaseLeaseIndex_Object((1,3,6,1,4,1,2356,16,1,12,3,2,1,9),_AgentDhcpServerLeaseLeaseIndex_Type())
agentDhcpServerLeaseLeaseIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerLeaseLeaseIndex.setStatus(_A)
_AgentDhcpServerLeaseClearVrfAndIPaddrSpecificBindings_Type=DisplayString
_AgentDhcpServerLeaseClearVrfAndIPaddrSpecificBindings_Object=MibScalar
agentDhcpServerLeaseClearVrfAndIPaddrSpecificBindings=_AgentDhcpServerLeaseClearVrfAndIPaddrSpecificBindings_Object((1,3,6,1,4,1,2356,16,1,12,3,3),_AgentDhcpServerLeaseClearVrfAndIPaddrSpecificBindings_Type())
agentDhcpServerLeaseClearVrfAndIPaddrSpecificBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerLeaseClearVrfAndIPaddrSpecificBindings.setStatus(_A)
_AgentDhcpServerLeaseClearPoolAndIPaddrSpecificBindings_Type=DisplayString
_AgentDhcpServerLeaseClearPoolAndIPaddrSpecificBindings_Object=MibScalar
agentDhcpServerLeaseClearPoolAndIPaddrSpecificBindings=_AgentDhcpServerLeaseClearPoolAndIPaddrSpecificBindings_Object((1,3,6,1,4,1,2356,16,1,12,3,4),_AgentDhcpServerLeaseClearPoolAndIPaddrSpecificBindings_Type())
agentDhcpServerLeaseClearPoolAndIPaddrSpecificBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerLeaseClearPoolAndIPaddrSpecificBindings.setStatus(_A)
_AgentDhcpServerAddressConflictGroup_ObjectIdentity=ObjectIdentity
agentDhcpServerAddressConflictGroup=_AgentDhcpServerAddressConflictGroup_ObjectIdentity((1,3,6,1,4,1,2356,16,1,12,4))
class _AgentDhcpServerClearAllAddressConflicts_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AgentDhcpServerClearAllAddressConflicts_Type.__name__=_D
_AgentDhcpServerClearAllAddressConflicts_Object=MibScalar
agentDhcpServerClearAllAddressConflicts=_AgentDhcpServerClearAllAddressConflicts_Object((1,3,6,1,4,1,2356,16,1,12,4,1),_AgentDhcpServerClearAllAddressConflicts_Type())
agentDhcpServerClearAllAddressConflicts.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerClearAllAddressConflicts.setStatus(_A)
class _AgentDhcpServerAddressConflictLogging_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_AgentDhcpServerAddressConflictLogging_Type.__name__=_D
_AgentDhcpServerAddressConflictLogging_Object=MibScalar
agentDhcpServerAddressConflictLogging=_AgentDhcpServerAddressConflictLogging_Object((1,3,6,1,4,1,2356,16,1,12,4,2),_AgentDhcpServerAddressConflictLogging_Type())
agentDhcpServerAddressConflictLogging.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerAddressConflictLogging.setStatus(_A)
_AgentDhcpServerAddressConflictTable_Object=MibTable
agentDhcpServerAddressConflictTable=_AgentDhcpServerAddressConflictTable_Object((1,3,6,1,4,1,2356,16,1,12,4,3))
if mibBuilder.loadTexts:agentDhcpServerAddressConflictTable.setStatus(_A)
_AgentDhcpServerAddressConflictEntry_Object=MibTableRow
agentDhcpServerAddressConflictEntry=_AgentDhcpServerAddressConflictEntry_Object((1,3,6,1,4,1,2356,16,1,12,4,3,1))
agentDhcpServerAddressConflictEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:agentDhcpServerAddressConflictEntry.setStatus(_A)
_AgentDhcpServerAddressConflictIP_Type=IpAddress
_AgentDhcpServerAddressConflictIP_Object=MibTableColumn
agentDhcpServerAddressConflictIP=_AgentDhcpServerAddressConflictIP_Object((1,3,6,1,4,1,2356,16,1,12,4,3,1,1),_AgentDhcpServerAddressConflictIP_Type())
agentDhcpServerAddressConflictIP.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerAddressConflictIP.setStatus(_A)
class _AgentDhcpServerAddressConflictDetectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ping',1),('gratuitousArp',2)))
_AgentDhcpServerAddressConflictDetectionType_Type.__name__=_D
_AgentDhcpServerAddressConflictDetectionType_Object=MibTableColumn
agentDhcpServerAddressConflictDetectionType=_AgentDhcpServerAddressConflictDetectionType_Object((1,3,6,1,4,1,2356,16,1,12,4,3,1,2),_AgentDhcpServerAddressConflictDetectionType_Type())
agentDhcpServerAddressConflictDetectionType.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerAddressConflictDetectionType.setStatus(_A)
_AgentDhcpServerAddressConflictDetectionTime_Type=TimeTicks
_AgentDhcpServerAddressConflictDetectionTime_Object=MibTableColumn
agentDhcpServerAddressConflictDetectionTime=_AgentDhcpServerAddressConflictDetectionTime_Object((1,3,6,1,4,1,2356,16,1,12,4,3,1,3),_AgentDhcpServerAddressConflictDetectionTime_Type())
agentDhcpServerAddressConflictDetectionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:agentDhcpServerAddressConflictDetectionTime.setStatus(_A)
_AgentDhcpServerAddressConflictStatus_Type=RowStatus
_AgentDhcpServerAddressConflictStatus_Object=MibTableColumn
agentDhcpServerAddressConflictStatus=_AgentDhcpServerAddressConflictStatus_Object((1,3,6,1,4,1,2356,16,1,12,4,3,1,4),_AgentDhcpServerAddressConflictStatus_Type())
agentDhcpServerAddressConflictStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentDhcpServerAddressConflictStatus.setStatus(_A)
agentDhcpServerPoolConfigEntry.registerAugmentions((_F,_S))
agentDhcpServerPoolAllocationEntry.setIndexNames(*agentDhcpServerPoolConfigEntry.getIndexNames())
mibBuilder.exportSymbols(_F,**{'fastPathDHCPServerPrivate':fastPathDHCPServerPrivate,'agentDhcpServerGroup':agentDhcpServerGroup,'agentDhcpServerAdminMode':agentDhcpServerAdminMode,'agentDhcpServerPingPktNos':agentDhcpServerPingPktNos,'agentDhcpServerAutomaticBindingsNos':agentDhcpServerAutomaticBindingsNos,'agentDhcpServerExpiredBindingsNos':agentDhcpServerExpiredBindingsNos,'agentDhcpServerMalformedMessagesReceived':agentDhcpServerMalformedMessagesReceived,'agentDhcpServerDISCOVERMessagesReceived':agentDhcpServerDISCOVERMessagesReceived,'agentDhcpServerREQUESTMessagesReceived':agentDhcpServerREQUESTMessagesReceived,'agentDhcpServerDECLINEMessagesReceived':agentDhcpServerDECLINEMessagesReceived,'agentDhcpServerRELEASEMessagesReceived':agentDhcpServerRELEASEMessagesReceived,'agentDhcpServerINFORMMessagesReceived':agentDhcpServerINFORMMessagesReceived,'agentDhcpServerOFFERMessagesSent':agentDhcpServerOFFERMessagesSent,'agentDhcpServerACKMessagesSent':agentDhcpServerACKMessagesSent,'agentDhcpServerNAKMessagesSent':agentDhcpServerNAKMessagesSent,'agentDhcpServerClearStatistics':agentDhcpServerClearStatistics,'agentDhcpServerBootpAutomatic':agentDhcpServerBootpAutomatic,'agentDhcpServerDISCOVERMessagesDiscarded':agentDhcpServerDISCOVERMessagesDiscarded,'agentDhcpServerPoolConfigGroup':agentDhcpServerPoolConfigGroup,'agentDhcpServerPoolNameCreate':agentDhcpServerPoolNameCreate,'agentDhcpServerPoolConfigTable':agentDhcpServerPoolConfigTable,'agentDhcpServerPoolConfigEntry':agentDhcpServerPoolConfigEntry,_K:agentDhcpServerPoolIndex,'agentDhcpServerPoolName':agentDhcpServerPoolName,'agentDhcpServerPoolDefRouter':agentDhcpServerPoolDefRouter,'agentDhcpServerPoolDNSServer':agentDhcpServerPoolDNSServer,'agentDhcpServerPoolLeaseTime':agentDhcpServerPoolLeaseTime,'agentDhcpServerPoolType':agentDhcpServerPoolType,'agentDhcpServerPoolNetbiosNameServer':agentDhcpServerPoolNetbiosNameServer,'agentDhcpServerPoolNetbiosNodeType':agentDhcpServerPoolNetbiosNodeType,'agentDhcpServerPoolSNTPServer':agentDhcpServerPoolSNTPServer,'agentDhcpServerPoolNextServer':agentDhcpServerPoolNextServer,'agentDhcpServerPoolDomainName':agentDhcpServerPoolDomainName,'agentDhcpServerPoolBootfile':agentDhcpServerPoolBootfile,'agentDhcpServerPoolRowStatus':agentDhcpServerPoolRowStatus,'agentDhcpServerPoolAllocationTable':agentDhcpServerPoolAllocationTable,_S:agentDhcpServerPoolAllocationEntry,'agentDhcpServerPoolAllocationName':agentDhcpServerPoolAllocationName,'agentDhcpServerDynamicPoolIpAddress':agentDhcpServerDynamicPoolIpAddress,'agentDhcpServerDynamicPoolIpMask':agentDhcpServerDynamicPoolIpMask,'agentDhcpServerDynamicPoolIpPrefixLength':agentDhcpServerDynamicPoolIpPrefixLength,'agentDhcpServerPoolAllocationType':agentDhcpServerPoolAllocationType,'agentDhcpServerManualPoolClientIdentifier':agentDhcpServerManualPoolClientIdentifier,'agentDhcpServerManualPoolClientName':agentDhcpServerManualPoolClientName,'agentDhcpServerManualPoolClientHWAddr':agentDhcpServerManualPoolClientHWAddr,'agentDhcpServerManualPoolClientHWType':agentDhcpServerManualPoolClientHWType,'agentDhcpServerManualPoolIpAddress':agentDhcpServerManualPoolIpAddress,'agentDhcpServerManualPoolIpMask':agentDhcpServerManualPoolIpMask,'agentDhcpServerManualPoolIpPrefixLength':agentDhcpServerManualPoolIpPrefixLength,'agentDhcpServerPoolVrfName':agentDhcpServerPoolVrfName,'agentDhcpServerExcludedAddressRangeCreate':agentDhcpServerExcludedAddressRangeCreate,'agentDhcpServerExcludedAddressRangeTable':agentDhcpServerExcludedAddressRangeTable,'agentDhcpServerExcludedAddressRangeEntry':agentDhcpServerExcludedAddressRangeEntry,_N:agentDhcpServerExcludedRangeIndex,'agentDhcpServerExcludedStartIpAddress':agentDhcpServerExcludedStartIpAddress,'agentDhcpServerExcludedEndIpAddress':agentDhcpServerExcludedEndIpAddress,'agentDhcpServerExcludedAddressRangeStatus':agentDhcpServerExcludedAddressRangeStatus,'agentDhcpServerExcludedVrfName':agentDhcpServerExcludedVrfName,'agentDhcpServerPoolOptionCreate':agentDhcpServerPoolOptionCreate,'agentDhcpServerPoolOptionTable':agentDhcpServerPoolOptionTable,'agentDhcpServerPoolOptionEntry':agentDhcpServerPoolOptionEntry,_O:agentDhcpServerPoolOptionIndex,_P:agentDhcpServerPoolOptionCode,'agentDhcpServerOptionPoolName':agentDhcpServerOptionPoolName,'agentDhcpServerPoolOptionAsciiData':agentDhcpServerPoolOptionAsciiData,'agentDhcpServerPoolOptionHexData':agentDhcpServerPoolOptionHexData,'agentDhcpServerPoolOptionIpAddressData':agentDhcpServerPoolOptionIpAddressData,'agentDhcpServerPoolOptionStatus':agentDhcpServerPoolOptionStatus,'agentDhcpServerLeaseGroup':agentDhcpServerLeaseGroup,'agentDhcpServerLeaseClearAllBindings':agentDhcpServerLeaseClearAllBindings,'agentDhcpServerLeaseTable':agentDhcpServerLeaseTable,'agentDhcpServerLeaseEntry':agentDhcpServerLeaseEntry,'agentDhcpServerLeaseIPAddress':agentDhcpServerLeaseIPAddress,'agentDhcpServerLeaseIPMask':agentDhcpServerLeaseIPMask,'agentDhcpServerLeaseHWAddress':agentDhcpServerLeaseHWAddress,'agentDhcpServerLeaseRemainingTime':agentDhcpServerLeaseRemainingTime,'agentDhcpServerLeaseType':agentDhcpServerLeaseType,'agentDhcpServerLeaseStatus':agentDhcpServerLeaseStatus,'agentDhcpServerLeasePoolName':agentDhcpServerLeasePoolName,'agentDhcpServerLeaseVrfName':agentDhcpServerLeaseVrfName,_Q:agentDhcpServerLeaseLeaseIndex,'agentDhcpServerLeaseClearVrfAndIPaddrSpecificBindings':agentDhcpServerLeaseClearVrfAndIPaddrSpecificBindings,'agentDhcpServerLeaseClearPoolAndIPaddrSpecificBindings':agentDhcpServerLeaseClearPoolAndIPaddrSpecificBindings,'agentDhcpServerAddressConflictGroup':agentDhcpServerAddressConflictGroup,'agentDhcpServerClearAllAddressConflicts':agentDhcpServerClearAllAddressConflicts,'agentDhcpServerAddressConflictLogging':agentDhcpServerAddressConflictLogging,'agentDhcpServerAddressConflictTable':agentDhcpServerAddressConflictTable,'agentDhcpServerAddressConflictEntry':agentDhcpServerAddressConflictEntry,_R:agentDhcpServerAddressConflictIP,'agentDhcpServerAddressConflictDetectionType':agentDhcpServerAddressConflictDetectionType,'agentDhcpServerAddressConflictDetectionTime':agentDhcpServerAddressConflictDetectionTime,'agentDhcpServerAddressConflictStatus':agentDhcpServerAddressConflictStatus})