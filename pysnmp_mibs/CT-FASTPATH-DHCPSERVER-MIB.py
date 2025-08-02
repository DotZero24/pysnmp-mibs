_S='ctAgentDhcpServerPoolAllocationEntry'
_R='ctAgentDhcpServerAddressConflictIP'
_Q='ctAgentDhcpServerLeaseIPAddress'
_P='ctAgentDhcpServerPoolOptionCode'
_O='ctAgentDhcpServerPoolOptionIndex'
_N='ctAgentDhcpServerExcludedRangeIndex'
_M='dynamic'
_L='un-allocated'
_K='ctAgentDhcpServerPoolIndex'
_J='manual'
_I='Unsigned32'
_H='disable'
_G='enable'
_F='CT-FASTPATH-DHCPSERVER-MIB'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctDhcpServerExpMib,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctDhcpServerExpMib')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,MacAddress,PhysAddress,RowPointer,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'MacAddress','PhysAddress','RowPointer','RowStatus','StorageType','TextualConvention','TruthValue')
ctFastPathDHCPServerMIB=ModuleIdentity((1,3,6,1,4,1,52,4,2,32,1))
_CtAgentDhcpServerGroup_ObjectIdentity=ObjectIdentity
ctAgentDhcpServerGroup=_CtAgentDhcpServerGroup_ObjectIdentity((1,3,6,1,4,1,52,4,2,32,1,1))
class _CtAgentDhcpServerAdminMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CtAgentDhcpServerAdminMode_Type.__name__=_D
_CtAgentDhcpServerAdminMode_Object=MibScalar
ctAgentDhcpServerAdminMode=_CtAgentDhcpServerAdminMode_Object((1,3,6,1,4,1,52,4,2,32,1,1,1),_CtAgentDhcpServerAdminMode_Type())
ctAgentDhcpServerAdminMode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerAdminMode.setStatus(_A)
class _CtAgentDhcpServerPingPktNos_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(2,10))
_CtAgentDhcpServerPingPktNos_Type.__name__=_D
_CtAgentDhcpServerPingPktNos_Object=MibScalar
ctAgentDhcpServerPingPktNos=_CtAgentDhcpServerPingPktNos_Object((1,3,6,1,4,1,52,4,2,32,1,1,2),_CtAgentDhcpServerPingPktNos_Type())
ctAgentDhcpServerPingPktNos.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerPingPktNos.setStatus(_A)
_CtAgentDhcpServerAutomaticBindingsNos_Type=Counter32
_CtAgentDhcpServerAutomaticBindingsNos_Object=MibScalar
ctAgentDhcpServerAutomaticBindingsNos=_CtAgentDhcpServerAutomaticBindingsNos_Object((1,3,6,1,4,1,52,4,2,32,1,1,3),_CtAgentDhcpServerAutomaticBindingsNos_Type())
ctAgentDhcpServerAutomaticBindingsNos.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerAutomaticBindingsNos.setStatus(_A)
_CtAgentDhcpServerExpiredBindingsNos_Type=Counter32
_CtAgentDhcpServerExpiredBindingsNos_Object=MibScalar
ctAgentDhcpServerExpiredBindingsNos=_CtAgentDhcpServerExpiredBindingsNos_Object((1,3,6,1,4,1,52,4,2,32,1,1,4),_CtAgentDhcpServerExpiredBindingsNos_Type())
ctAgentDhcpServerExpiredBindingsNos.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerExpiredBindingsNos.setStatus(_A)
_CtAgentDhcpServerMalformedMessagesReceived_Type=Counter32
_CtAgentDhcpServerMalformedMessagesReceived_Object=MibScalar
ctAgentDhcpServerMalformedMessagesReceived=_CtAgentDhcpServerMalformedMessagesReceived_Object((1,3,6,1,4,1,52,4,2,32,1,1,5),_CtAgentDhcpServerMalformedMessagesReceived_Type())
ctAgentDhcpServerMalformedMessagesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerMalformedMessagesReceived.setStatus(_A)
_CtAgentDhcpServerDISCOVERMessagesReceived_Type=Counter32
_CtAgentDhcpServerDISCOVERMessagesReceived_Object=MibScalar
ctAgentDhcpServerDISCOVERMessagesReceived=_CtAgentDhcpServerDISCOVERMessagesReceived_Object((1,3,6,1,4,1,52,4,2,32,1,1,6),_CtAgentDhcpServerDISCOVERMessagesReceived_Type())
ctAgentDhcpServerDISCOVERMessagesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerDISCOVERMessagesReceived.setStatus(_A)
_CtAgentDhcpServerREQUESTMessagesReceived_Type=Counter32
_CtAgentDhcpServerREQUESTMessagesReceived_Object=MibScalar
ctAgentDhcpServerREQUESTMessagesReceived=_CtAgentDhcpServerREQUESTMessagesReceived_Object((1,3,6,1,4,1,52,4,2,32,1,1,7),_CtAgentDhcpServerREQUESTMessagesReceived_Type())
ctAgentDhcpServerREQUESTMessagesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerREQUESTMessagesReceived.setStatus(_A)
_CtAgentDhcpServerDECLINEMessagesReceived_Type=Counter32
_CtAgentDhcpServerDECLINEMessagesReceived_Object=MibScalar
ctAgentDhcpServerDECLINEMessagesReceived=_CtAgentDhcpServerDECLINEMessagesReceived_Object((1,3,6,1,4,1,52,4,2,32,1,1,8),_CtAgentDhcpServerDECLINEMessagesReceived_Type())
ctAgentDhcpServerDECLINEMessagesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerDECLINEMessagesReceived.setStatus(_A)
_CtAgentDhcpServerRELEASEMessagesReceived_Type=Counter32
_CtAgentDhcpServerRELEASEMessagesReceived_Object=MibScalar
ctAgentDhcpServerRELEASEMessagesReceived=_CtAgentDhcpServerRELEASEMessagesReceived_Object((1,3,6,1,4,1,52,4,2,32,1,1,9),_CtAgentDhcpServerRELEASEMessagesReceived_Type())
ctAgentDhcpServerRELEASEMessagesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerRELEASEMessagesReceived.setStatus(_A)
_CtAgentDhcpServerINFORMMessagesReceived_Type=Counter32
_CtAgentDhcpServerINFORMMessagesReceived_Object=MibScalar
ctAgentDhcpServerINFORMMessagesReceived=_CtAgentDhcpServerINFORMMessagesReceived_Object((1,3,6,1,4,1,52,4,2,32,1,1,10),_CtAgentDhcpServerINFORMMessagesReceived_Type())
ctAgentDhcpServerINFORMMessagesReceived.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerINFORMMessagesReceived.setStatus(_A)
_CtAgentDhcpServerOFFERMessagesSent_Type=Counter32
_CtAgentDhcpServerOFFERMessagesSent_Object=MibScalar
ctAgentDhcpServerOFFERMessagesSent=_CtAgentDhcpServerOFFERMessagesSent_Object((1,3,6,1,4,1,52,4,2,32,1,1,11),_CtAgentDhcpServerOFFERMessagesSent_Type())
ctAgentDhcpServerOFFERMessagesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerOFFERMessagesSent.setStatus(_A)
_CtAgentDhcpServerACKMessagesSent_Type=Counter32
_CtAgentDhcpServerACKMessagesSent_Object=MibScalar
ctAgentDhcpServerACKMessagesSent=_CtAgentDhcpServerACKMessagesSent_Object((1,3,6,1,4,1,52,4,2,32,1,1,12),_CtAgentDhcpServerACKMessagesSent_Type())
ctAgentDhcpServerACKMessagesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerACKMessagesSent.setStatus(_A)
_CtAgentDhcpServerNAKMessagesSent_Type=Counter32
_CtAgentDhcpServerNAKMessagesSent_Object=MibScalar
ctAgentDhcpServerNAKMessagesSent=_CtAgentDhcpServerNAKMessagesSent_Object((1,3,6,1,4,1,52,4,2,32,1,1,13),_CtAgentDhcpServerNAKMessagesSent_Type())
ctAgentDhcpServerNAKMessagesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerNAKMessagesSent.setStatus(_A)
class _CtAgentDhcpServerClearStatistics_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CtAgentDhcpServerClearStatistics_Type.__name__=_D
_CtAgentDhcpServerClearStatistics_Object=MibScalar
ctAgentDhcpServerClearStatistics=_CtAgentDhcpServerClearStatistics_Object((1,3,6,1,4,1,52,4,2,32,1,1,14),_CtAgentDhcpServerClearStatistics_Type())
ctAgentDhcpServerClearStatistics.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerClearStatistics.setStatus(_A)
class _CtAgentDhcpServerBootpAutomatic_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CtAgentDhcpServerBootpAutomatic_Type.__name__=_D
_CtAgentDhcpServerBootpAutomatic_Object=MibScalar
ctAgentDhcpServerBootpAutomatic=_CtAgentDhcpServerBootpAutomatic_Object((1,3,6,1,4,1,52,4,2,32,1,1,15),_CtAgentDhcpServerBootpAutomatic_Type())
ctAgentDhcpServerBootpAutomatic.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerBootpAutomatic.setStatus(_A)
_CtAgentDhcpServerPoolConfigGroup_ObjectIdentity=ObjectIdentity
ctAgentDhcpServerPoolConfigGroup=_CtAgentDhcpServerPoolConfigGroup_ObjectIdentity((1,3,6,1,4,1,52,4,2,32,1,2))
class _CtAgentDhcpServerPoolNameCreate_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(1,31))
_CtAgentDhcpServerPoolNameCreate_Type.__name__=_E
_CtAgentDhcpServerPoolNameCreate_Object=MibScalar
ctAgentDhcpServerPoolNameCreate=_CtAgentDhcpServerPoolNameCreate_Object((1,3,6,1,4,1,52,4,2,32,1,2,1),_CtAgentDhcpServerPoolNameCreate_Type())
ctAgentDhcpServerPoolNameCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerPoolNameCreate.setStatus(_A)
_CtAgentDhcpServerPoolConfigTable_Object=MibTable
ctAgentDhcpServerPoolConfigTable=_CtAgentDhcpServerPoolConfigTable_Object((1,3,6,1,4,1,52,4,2,32,1,2,2))
if mibBuilder.loadTexts:ctAgentDhcpServerPoolConfigTable.setStatus(_A)
_CtAgentDhcpServerPoolConfigEntry_Object=MibTableRow
ctAgentDhcpServerPoolConfigEntry=_CtAgentDhcpServerPoolConfigEntry_Object((1,3,6,1,4,1,52,4,2,32,1,2,2,1))
ctAgentDhcpServerPoolConfigEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:ctAgentDhcpServerPoolConfigEntry.setStatus(_A)
class _CtAgentDhcpServerPoolIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_CtAgentDhcpServerPoolIndex_Type.__name__=_I
_CtAgentDhcpServerPoolIndex_Object=MibTableColumn
ctAgentDhcpServerPoolIndex=_CtAgentDhcpServerPoolIndex_Object((1,3,6,1,4,1,52,4,2,32,1,2,2,1,1),_CtAgentDhcpServerPoolIndex_Type())
ctAgentDhcpServerPoolIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerPoolIndex.setStatus(_A)
class _CtAgentDhcpServerPoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_CtAgentDhcpServerPoolName_Type.__name__=_E
_CtAgentDhcpServerPoolName_Object=MibTableColumn
ctAgentDhcpServerPoolName=_CtAgentDhcpServerPoolName_Object((1,3,6,1,4,1,52,4,2,32,1,2,2,1,2),_CtAgentDhcpServerPoolName_Type())
ctAgentDhcpServerPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerPoolName.setStatus(_A)
_CtAgentDhcpServerPoolDefRouter_Type=DisplayString
_CtAgentDhcpServerPoolDefRouter_Object=MibTableColumn
ctAgentDhcpServerPoolDefRouter=_CtAgentDhcpServerPoolDefRouter_Object((1,3,6,1,4,1,52,4,2,32,1,2,2,1,3),_CtAgentDhcpServerPoolDefRouter_Type())
ctAgentDhcpServerPoolDefRouter.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerPoolDefRouter.setStatus(_A)
_CtAgentDhcpServerPoolDNSServer_Type=DisplayString
_CtAgentDhcpServerPoolDNSServer_Object=MibTableColumn
ctAgentDhcpServerPoolDNSServer=_CtAgentDhcpServerPoolDNSServer_Object((1,3,6,1,4,1,52,4,2,32,1,2,2,1,4),_CtAgentDhcpServerPoolDNSServer_Type())
ctAgentDhcpServerPoolDNSServer.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerPoolDNSServer.setStatus(_A)
class _CtAgentDhcpServerPoolLeaseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_CtAgentDhcpServerPoolLeaseTime_Type.__name__=_D
_CtAgentDhcpServerPoolLeaseTime_Object=MibTableColumn
ctAgentDhcpServerPoolLeaseTime=_CtAgentDhcpServerPoolLeaseTime_Object((1,3,6,1,4,1,52,4,2,32,1,2,2,1,5),_CtAgentDhcpServerPoolLeaseTime_Type())
ctAgentDhcpServerPoolLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerPoolLeaseTime.setStatus(_A)
class _CtAgentDhcpServerPoolType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_L,0),(_M,1),(_J,2)))
_CtAgentDhcpServerPoolType_Type.__name__=_D
_CtAgentDhcpServerPoolType_Object=MibTableColumn
ctAgentDhcpServerPoolType=_CtAgentDhcpServerPoolType_Object((1,3,6,1,4,1,52,4,2,32,1,2,2,1,6),_CtAgentDhcpServerPoolType_Type())
ctAgentDhcpServerPoolType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerPoolType.setStatus(_A)
_CtAgentDhcpServerPoolNetbiosNameServer_Type=DisplayString
_CtAgentDhcpServerPoolNetbiosNameServer_Object=MibTableColumn
ctAgentDhcpServerPoolNetbiosNameServer=_CtAgentDhcpServerPoolNetbiosNameServer_Object((1,3,6,1,4,1,52,4,2,32,1,2,2,1,7),_CtAgentDhcpServerPoolNetbiosNameServer_Type())
ctAgentDhcpServerPoolNetbiosNameServer.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerPoolNetbiosNameServer.setStatus(_A)
class _CtAgentDhcpServerPoolNetbiosNodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,8)));namedValues=NamedValues(*(('none',0),('b-node',1),('p-node',2),('m-node',4),('h-node',8)))
_CtAgentDhcpServerPoolNetbiosNodeType_Type.__name__=_D
_CtAgentDhcpServerPoolNetbiosNodeType_Object=MibTableColumn
ctAgentDhcpServerPoolNetbiosNodeType=_CtAgentDhcpServerPoolNetbiosNodeType_Object((1,3,6,1,4,1,52,4,2,32,1,2,2,1,8),_CtAgentDhcpServerPoolNetbiosNodeType_Type())
ctAgentDhcpServerPoolNetbiosNodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerPoolNetbiosNodeType.setStatus(_A)
_CtAgentDhcpServerPoolNextServer_Type=IpAddress
_CtAgentDhcpServerPoolNextServer_Object=MibTableColumn
ctAgentDhcpServerPoolNextServer=_CtAgentDhcpServerPoolNextServer_Object((1,3,6,1,4,1,52,4,2,32,1,2,2,1,9),_CtAgentDhcpServerPoolNextServer_Type())
ctAgentDhcpServerPoolNextServer.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerPoolNextServer.setStatus(_A)
class _CtAgentDhcpServerPoolDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CtAgentDhcpServerPoolDomainName_Type.__name__=_E
_CtAgentDhcpServerPoolDomainName_Object=MibTableColumn
ctAgentDhcpServerPoolDomainName=_CtAgentDhcpServerPoolDomainName_Object((1,3,6,1,4,1,52,4,2,32,1,2,2,1,10),_CtAgentDhcpServerPoolDomainName_Type())
ctAgentDhcpServerPoolDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerPoolDomainName.setStatus(_A)
class _CtAgentDhcpServerPoolBootfile_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_CtAgentDhcpServerPoolBootfile_Type.__name__=_E
_CtAgentDhcpServerPoolBootfile_Object=MibTableColumn
ctAgentDhcpServerPoolBootfile=_CtAgentDhcpServerPoolBootfile_Object((1,3,6,1,4,1,52,4,2,32,1,2,2,1,11),_CtAgentDhcpServerPoolBootfile_Type())
ctAgentDhcpServerPoolBootfile.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerPoolBootfile.setStatus(_A)
_CtAgentDhcpServerPoolRowStatus_Type=RowStatus
_CtAgentDhcpServerPoolRowStatus_Object=MibTableColumn
ctAgentDhcpServerPoolRowStatus=_CtAgentDhcpServerPoolRowStatus_Object((1,3,6,1,4,1,52,4,2,32,1,2,2,1,12),_CtAgentDhcpServerPoolRowStatus_Type())
ctAgentDhcpServerPoolRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerPoolRowStatus.setStatus(_A)
_CtAgentDhcpServerPoolAllocationTable_Object=MibTable
ctAgentDhcpServerPoolAllocationTable=_CtAgentDhcpServerPoolAllocationTable_Object((1,3,6,1,4,1,52,4,2,32,1,2,3))
if mibBuilder.loadTexts:ctAgentDhcpServerPoolAllocationTable.setStatus(_A)
_CtAgentDhcpServerPoolAllocationEntry_Object=MibTableRow
ctAgentDhcpServerPoolAllocationEntry=_CtAgentDhcpServerPoolAllocationEntry_Object((1,3,6,1,4,1,52,4,2,32,1,2,3,1))
if mibBuilder.loadTexts:ctAgentDhcpServerPoolAllocationEntry.setStatus(_A)
class _CtAgentDhcpServerPoolAllocationName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_CtAgentDhcpServerPoolAllocationName_Type.__name__=_E
_CtAgentDhcpServerPoolAllocationName_Object=MibTableColumn
ctAgentDhcpServerPoolAllocationName=_CtAgentDhcpServerPoolAllocationName_Object((1,3,6,1,4,1,52,4,2,32,1,2,3,1,1),_CtAgentDhcpServerPoolAllocationName_Type())
ctAgentDhcpServerPoolAllocationName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerPoolAllocationName.setStatus(_A)
_CtAgentDhcpServerDynamicPoolIpAddress_Type=IpAddress
_CtAgentDhcpServerDynamicPoolIpAddress_Object=MibTableColumn
ctAgentDhcpServerDynamicPoolIpAddress=_CtAgentDhcpServerDynamicPoolIpAddress_Object((1,3,6,1,4,1,52,4,2,32,1,2,3,1,2),_CtAgentDhcpServerDynamicPoolIpAddress_Type())
ctAgentDhcpServerDynamicPoolIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerDynamicPoolIpAddress.setStatus(_A)
_CtAgentDhcpServerDynamicPoolIpMask_Type=IpAddress
_CtAgentDhcpServerDynamicPoolIpMask_Object=MibTableColumn
ctAgentDhcpServerDynamicPoolIpMask=_CtAgentDhcpServerDynamicPoolIpMask_Object((1,3,6,1,4,1,52,4,2,32,1,2,3,1,3),_CtAgentDhcpServerDynamicPoolIpMask_Type())
ctAgentDhcpServerDynamicPoolIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerDynamicPoolIpMask.setStatus(_A)
_CtAgentDhcpServerDynamicPoolIpPrefixLength_Type=Unsigned32
_CtAgentDhcpServerDynamicPoolIpPrefixLength_Object=MibTableColumn
ctAgentDhcpServerDynamicPoolIpPrefixLength=_CtAgentDhcpServerDynamicPoolIpPrefixLength_Object((1,3,6,1,4,1,52,4,2,32,1,2,3,1,4),_CtAgentDhcpServerDynamicPoolIpPrefixLength_Type())
ctAgentDhcpServerDynamicPoolIpPrefixLength.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerDynamicPoolIpPrefixLength.setStatus(_A)
class _CtAgentDhcpServerPoolAllocationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_L,0),(_M,1),(_J,2)))
_CtAgentDhcpServerPoolAllocationType_Type.__name__=_D
_CtAgentDhcpServerPoolAllocationType_Object=MibTableColumn
ctAgentDhcpServerPoolAllocationType=_CtAgentDhcpServerPoolAllocationType_Object((1,3,6,1,4,1,52,4,2,32,1,2,3,1,5),_CtAgentDhcpServerPoolAllocationType_Type())
ctAgentDhcpServerPoolAllocationType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerPoolAllocationType.setStatus(_A)
_CtAgentDhcpServerManualPoolClientIdentifier_Type=DisplayString
_CtAgentDhcpServerManualPoolClientIdentifier_Object=MibTableColumn
ctAgentDhcpServerManualPoolClientIdentifier=_CtAgentDhcpServerManualPoolClientIdentifier_Object((1,3,6,1,4,1,52,4,2,32,1,2,3,1,6),_CtAgentDhcpServerManualPoolClientIdentifier_Type())
ctAgentDhcpServerManualPoolClientIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerManualPoolClientIdentifier.setStatus(_A)
class _CtAgentDhcpServerManualPoolClientName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_CtAgentDhcpServerManualPoolClientName_Type.__name__=_E
_CtAgentDhcpServerManualPoolClientName_Object=MibTableColumn
ctAgentDhcpServerManualPoolClientName=_CtAgentDhcpServerManualPoolClientName_Object((1,3,6,1,4,1,52,4,2,32,1,2,3,1,7),_CtAgentDhcpServerManualPoolClientName_Type())
ctAgentDhcpServerManualPoolClientName.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerManualPoolClientName.setStatus(_A)
_CtAgentDhcpServerManualPoolClientHWAddr_Type=DisplayString
_CtAgentDhcpServerManualPoolClientHWAddr_Object=MibTableColumn
ctAgentDhcpServerManualPoolClientHWAddr=_CtAgentDhcpServerManualPoolClientHWAddr_Object((1,3,6,1,4,1,52,4,2,32,1,2,3,1,8),_CtAgentDhcpServerManualPoolClientHWAddr_Type())
ctAgentDhcpServerManualPoolClientHWAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerManualPoolClientHWAddr.setStatus(_A)
class _CtAgentDhcpServerManualPoolClientHWType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,6)));namedValues=NamedValues(*(('ethernet',1),('ieee802',6)))
_CtAgentDhcpServerManualPoolClientHWType_Type.__name__=_D
_CtAgentDhcpServerManualPoolClientHWType_Object=MibTableColumn
ctAgentDhcpServerManualPoolClientHWType=_CtAgentDhcpServerManualPoolClientHWType_Object((1,3,6,1,4,1,52,4,2,32,1,2,3,1,9),_CtAgentDhcpServerManualPoolClientHWType_Type())
ctAgentDhcpServerManualPoolClientHWType.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerManualPoolClientHWType.setStatus(_A)
_CtAgentDhcpServerManualPoolIpAddress_Type=IpAddress
_CtAgentDhcpServerManualPoolIpAddress_Object=MibTableColumn
ctAgentDhcpServerManualPoolIpAddress=_CtAgentDhcpServerManualPoolIpAddress_Object((1,3,6,1,4,1,52,4,2,32,1,2,3,1,10),_CtAgentDhcpServerManualPoolIpAddress_Type())
ctAgentDhcpServerManualPoolIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerManualPoolIpAddress.setStatus(_A)
_CtAgentDhcpServerManualPoolIpMask_Type=IpAddress
_CtAgentDhcpServerManualPoolIpMask_Object=MibTableColumn
ctAgentDhcpServerManualPoolIpMask=_CtAgentDhcpServerManualPoolIpMask_Object((1,3,6,1,4,1,52,4,2,32,1,2,3,1,11),_CtAgentDhcpServerManualPoolIpMask_Type())
ctAgentDhcpServerManualPoolIpMask.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerManualPoolIpMask.setStatus(_A)
_CtAgentDhcpServerManualPoolIpPrefixLength_Type=Unsigned32
_CtAgentDhcpServerManualPoolIpPrefixLength_Object=MibTableColumn
ctAgentDhcpServerManualPoolIpPrefixLength=_CtAgentDhcpServerManualPoolIpPrefixLength_Object((1,3,6,1,4,1,52,4,2,32,1,2,3,1,12),_CtAgentDhcpServerManualPoolIpPrefixLength_Type())
ctAgentDhcpServerManualPoolIpPrefixLength.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerManualPoolIpPrefixLength.setStatus(_A)
_CtAgentDhcpServerExcludedAddressRangeCreate_Type=DisplayString
_CtAgentDhcpServerExcludedAddressRangeCreate_Object=MibScalar
ctAgentDhcpServerExcludedAddressRangeCreate=_CtAgentDhcpServerExcludedAddressRangeCreate_Object((1,3,6,1,4,1,52,4,2,32,1,2,4),_CtAgentDhcpServerExcludedAddressRangeCreate_Type())
ctAgentDhcpServerExcludedAddressRangeCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerExcludedAddressRangeCreate.setStatus(_A)
_CtAgentDhcpServerExcludedAddressRangeTable_Object=MibTable
ctAgentDhcpServerExcludedAddressRangeTable=_CtAgentDhcpServerExcludedAddressRangeTable_Object((1,3,6,1,4,1,52,4,2,32,1,2,5))
if mibBuilder.loadTexts:ctAgentDhcpServerExcludedAddressRangeTable.setStatus(_A)
_CtAgentDhcpServerExcludedAddressRangeEntry_Object=MibTableRow
ctAgentDhcpServerExcludedAddressRangeEntry=_CtAgentDhcpServerExcludedAddressRangeEntry_Object((1,3,6,1,4,1,52,4,2,32,1,2,5,1))
ctAgentDhcpServerExcludedAddressRangeEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:ctAgentDhcpServerExcludedAddressRangeEntry.setStatus(_A)
class _CtAgentDhcpServerExcludedRangeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_CtAgentDhcpServerExcludedRangeIndex_Type.__name__=_I
_CtAgentDhcpServerExcludedRangeIndex_Object=MibTableColumn
ctAgentDhcpServerExcludedRangeIndex=_CtAgentDhcpServerExcludedRangeIndex_Object((1,3,6,1,4,1,52,4,2,32,1,2,5,1,1),_CtAgentDhcpServerExcludedRangeIndex_Type())
ctAgentDhcpServerExcludedRangeIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerExcludedRangeIndex.setStatus(_A)
_CtAgentDhcpServerExcludedStartIpAddress_Type=IpAddress
_CtAgentDhcpServerExcludedStartIpAddress_Object=MibTableColumn
ctAgentDhcpServerExcludedStartIpAddress=_CtAgentDhcpServerExcludedStartIpAddress_Object((1,3,6,1,4,1,52,4,2,32,1,2,5,1,2),_CtAgentDhcpServerExcludedStartIpAddress_Type())
ctAgentDhcpServerExcludedStartIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerExcludedStartIpAddress.setStatus(_A)
_CtAgentDhcpServerExcludedEndIpAddress_Type=IpAddress
_CtAgentDhcpServerExcludedEndIpAddress_Object=MibTableColumn
ctAgentDhcpServerExcludedEndIpAddress=_CtAgentDhcpServerExcludedEndIpAddress_Object((1,3,6,1,4,1,52,4,2,32,1,2,5,1,3),_CtAgentDhcpServerExcludedEndIpAddress_Type())
ctAgentDhcpServerExcludedEndIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerExcludedEndIpAddress.setStatus(_A)
_CtAgentDhcpServerExcludedAddressRangeStatus_Type=RowStatus
_CtAgentDhcpServerExcludedAddressRangeStatus_Object=MibTableColumn
ctAgentDhcpServerExcludedAddressRangeStatus=_CtAgentDhcpServerExcludedAddressRangeStatus_Object((1,3,6,1,4,1,52,4,2,32,1,2,5,1,4),_CtAgentDhcpServerExcludedAddressRangeStatus_Type())
ctAgentDhcpServerExcludedAddressRangeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerExcludedAddressRangeStatus.setStatus(_A)
_CtAgentDhcpServerPoolOptionCreate_Type=DisplayString
_CtAgentDhcpServerPoolOptionCreate_Object=MibScalar
ctAgentDhcpServerPoolOptionCreate=_CtAgentDhcpServerPoolOptionCreate_Object((1,3,6,1,4,1,52,4,2,32,1,2,6),_CtAgentDhcpServerPoolOptionCreate_Type())
ctAgentDhcpServerPoolOptionCreate.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerPoolOptionCreate.setStatus(_A)
_CtAgentDhcpServerPoolOptionTable_Object=MibTable
ctAgentDhcpServerPoolOptionTable=_CtAgentDhcpServerPoolOptionTable_Object((1,3,6,1,4,1,52,4,2,32,1,2,7))
if mibBuilder.loadTexts:ctAgentDhcpServerPoolOptionTable.setStatus(_A)
_CtAgentDhcpServerPoolOptionEntry_Object=MibTableRow
ctAgentDhcpServerPoolOptionEntry=_CtAgentDhcpServerPoolOptionEntry_Object((1,3,6,1,4,1,52,4,2,32,1,2,7,1))
ctAgentDhcpServerPoolOptionEntry.setIndexNames((0,_F,_O),(0,_F,_P))
if mibBuilder.loadTexts:ctAgentDhcpServerPoolOptionEntry.setStatus(_A)
class _CtAgentDhcpServerPoolOptionIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,512))
_CtAgentDhcpServerPoolOptionIndex_Type.__name__=_I
_CtAgentDhcpServerPoolOptionIndex_Object=MibTableColumn
ctAgentDhcpServerPoolOptionIndex=_CtAgentDhcpServerPoolOptionIndex_Object((1,3,6,1,4,1,52,4,2,32,1,2,7,1,1),_CtAgentDhcpServerPoolOptionIndex_Type())
ctAgentDhcpServerPoolOptionIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerPoolOptionIndex.setStatus(_A)
class _CtAgentDhcpServerPoolOptionCode_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,254))
_CtAgentDhcpServerPoolOptionCode_Type.__name__=_I
_CtAgentDhcpServerPoolOptionCode_Object=MibTableColumn
ctAgentDhcpServerPoolOptionCode=_CtAgentDhcpServerPoolOptionCode_Object((1,3,6,1,4,1,52,4,2,32,1,2,7,1,2),_CtAgentDhcpServerPoolOptionCode_Type())
ctAgentDhcpServerPoolOptionCode.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerPoolOptionCode.setStatus(_A)
class _CtAgentDhcpServerOptionPoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,31))
_CtAgentDhcpServerOptionPoolName_Type.__name__=_E
_CtAgentDhcpServerOptionPoolName_Object=MibTableColumn
ctAgentDhcpServerOptionPoolName=_CtAgentDhcpServerOptionPoolName_Object((1,3,6,1,4,1,52,4,2,32,1,2,7,1,3),_CtAgentDhcpServerOptionPoolName_Type())
ctAgentDhcpServerOptionPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerOptionPoolName.setStatus(_A)
class _CtAgentDhcpServerPoolOptionAsciiData_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,441))
_CtAgentDhcpServerPoolOptionAsciiData_Type.__name__=_E
_CtAgentDhcpServerPoolOptionAsciiData_Object=MibTableColumn
ctAgentDhcpServerPoolOptionAsciiData=_CtAgentDhcpServerPoolOptionAsciiData_Object((1,3,6,1,4,1,52,4,2,32,1,2,7,1,4),_CtAgentDhcpServerPoolOptionAsciiData_Type())
ctAgentDhcpServerPoolOptionAsciiData.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerPoolOptionAsciiData.setStatus(_A)
class _CtAgentDhcpServerPoolOptionHexData_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,1324))
_CtAgentDhcpServerPoolOptionHexData_Type.__name__=_E
_CtAgentDhcpServerPoolOptionHexData_Object=MibTableColumn
ctAgentDhcpServerPoolOptionHexData=_CtAgentDhcpServerPoolOptionHexData_Object((1,3,6,1,4,1,52,4,2,32,1,2,7,1,5),_CtAgentDhcpServerPoolOptionHexData_Type())
ctAgentDhcpServerPoolOptionHexData.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerPoolOptionHexData.setStatus(_A)
_CtAgentDhcpServerPoolOptionIpAddressData_Type=DisplayString
_CtAgentDhcpServerPoolOptionIpAddressData_Object=MibTableColumn
ctAgentDhcpServerPoolOptionIpAddressData=_CtAgentDhcpServerPoolOptionIpAddressData_Object((1,3,6,1,4,1,52,4,2,32,1,2,7,1,6),_CtAgentDhcpServerPoolOptionIpAddressData_Type())
ctAgentDhcpServerPoolOptionIpAddressData.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerPoolOptionIpAddressData.setStatus(_A)
_CtAgentDhcpServerPoolOptionStatus_Type=RowStatus
_CtAgentDhcpServerPoolOptionStatus_Object=MibTableColumn
ctAgentDhcpServerPoolOptionStatus=_CtAgentDhcpServerPoolOptionStatus_Object((1,3,6,1,4,1,52,4,2,32,1,2,7,1,7),_CtAgentDhcpServerPoolOptionStatus_Type())
ctAgentDhcpServerPoolOptionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerPoolOptionStatus.setStatus(_A)
_CtAgentDhcpServerLeaseGroup_ObjectIdentity=ObjectIdentity
ctAgentDhcpServerLeaseGroup=_CtAgentDhcpServerLeaseGroup_ObjectIdentity((1,3,6,1,4,1,52,4,2,32,1,3))
class _CtAgentDhcpServerLeaseClearAllBindings_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CtAgentDhcpServerLeaseClearAllBindings_Type.__name__=_D
_CtAgentDhcpServerLeaseClearAllBindings_Object=MibScalar
ctAgentDhcpServerLeaseClearAllBindings=_CtAgentDhcpServerLeaseClearAllBindings_Object((1,3,6,1,4,1,52,4,2,32,1,3,1),_CtAgentDhcpServerLeaseClearAllBindings_Type())
ctAgentDhcpServerLeaseClearAllBindings.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerLeaseClearAllBindings.setStatus(_A)
_CtAgentDhcpServerLeaseTable_Object=MibTable
ctAgentDhcpServerLeaseTable=_CtAgentDhcpServerLeaseTable_Object((1,3,6,1,4,1,52,4,2,32,1,3,2))
if mibBuilder.loadTexts:ctAgentDhcpServerLeaseTable.setStatus(_A)
_CtAgentDhcpServerLeaseEntry_Object=MibTableRow
ctAgentDhcpServerLeaseEntry=_CtAgentDhcpServerLeaseEntry_Object((1,3,6,1,4,1,52,4,2,32,1,3,2,1))
ctAgentDhcpServerLeaseEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:ctAgentDhcpServerLeaseEntry.setStatus(_A)
_CtAgentDhcpServerLeaseIPAddress_Type=IpAddress
_CtAgentDhcpServerLeaseIPAddress_Object=MibTableColumn
ctAgentDhcpServerLeaseIPAddress=_CtAgentDhcpServerLeaseIPAddress_Object((1,3,6,1,4,1,52,4,2,32,1,3,2,1,1),_CtAgentDhcpServerLeaseIPAddress_Type())
ctAgentDhcpServerLeaseIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerLeaseIPAddress.setStatus(_A)
_CtAgentDhcpServerLeaseIPMask_Type=IpAddress
_CtAgentDhcpServerLeaseIPMask_Object=MibTableColumn
ctAgentDhcpServerLeaseIPMask=_CtAgentDhcpServerLeaseIPMask_Object((1,3,6,1,4,1,52,4,2,32,1,3,2,1,2),_CtAgentDhcpServerLeaseIPMask_Type())
ctAgentDhcpServerLeaseIPMask.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerLeaseIPMask.setStatus(_A)
_CtAgentDhcpServerLeaseHWAddress_Type=MacAddress
_CtAgentDhcpServerLeaseHWAddress_Object=MibTableColumn
ctAgentDhcpServerLeaseHWAddress=_CtAgentDhcpServerLeaseHWAddress_Object((1,3,6,1,4,1,52,4,2,32,1,3,2,1,3),_CtAgentDhcpServerLeaseHWAddress_Type())
ctAgentDhcpServerLeaseHWAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerLeaseHWAddress.setStatus(_A)
_CtAgentDhcpServerLeaseRemainingTime_Type=TimeTicks
_CtAgentDhcpServerLeaseRemainingTime_Object=MibTableColumn
ctAgentDhcpServerLeaseRemainingTime=_CtAgentDhcpServerLeaseRemainingTime_Object((1,3,6,1,4,1,52,4,2,32,1,3,2,1,4),_CtAgentDhcpServerLeaseRemainingTime_Type())
ctAgentDhcpServerLeaseRemainingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerLeaseRemainingTime.setStatus(_A)
class _CtAgentDhcpServerLeaseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('automatic',1),(_J,2)))
_CtAgentDhcpServerLeaseType_Type.__name__=_D
_CtAgentDhcpServerLeaseType_Object=MibTableColumn
ctAgentDhcpServerLeaseType=_CtAgentDhcpServerLeaseType_Object((1,3,6,1,4,1,52,4,2,32,1,3,2,1,5),_CtAgentDhcpServerLeaseType_Type())
ctAgentDhcpServerLeaseType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerLeaseType.setStatus(_A)
_CtAgentDhcpServerLeaseStatus_Type=RowStatus
_CtAgentDhcpServerLeaseStatus_Object=MibTableColumn
ctAgentDhcpServerLeaseStatus=_CtAgentDhcpServerLeaseStatus_Object((1,3,6,1,4,1,52,4,2,32,1,3,2,1,6),_CtAgentDhcpServerLeaseStatus_Type())
ctAgentDhcpServerLeaseStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerLeaseStatus.setStatus(_A)
_CtAgentDhcpServerAddressConflictGroup_ObjectIdentity=ObjectIdentity
ctAgentDhcpServerAddressConflictGroup=_CtAgentDhcpServerAddressConflictGroup_ObjectIdentity((1,3,6,1,4,1,52,4,2,32,1,4))
class _CtAgentDhcpServerClearAllAddressConflicts_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CtAgentDhcpServerClearAllAddressConflicts_Type.__name__=_D
_CtAgentDhcpServerClearAllAddressConflicts_Object=MibScalar
ctAgentDhcpServerClearAllAddressConflicts=_CtAgentDhcpServerClearAllAddressConflicts_Object((1,3,6,1,4,1,52,4,2,32,1,4,1),_CtAgentDhcpServerClearAllAddressConflicts_Type())
ctAgentDhcpServerClearAllAddressConflicts.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerClearAllAddressConflicts.setStatus(_A)
class _CtAgentDhcpServerAddressConflictLogging_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_CtAgentDhcpServerAddressConflictLogging_Type.__name__=_D
_CtAgentDhcpServerAddressConflictLogging_Object=MibScalar
ctAgentDhcpServerAddressConflictLogging=_CtAgentDhcpServerAddressConflictLogging_Object((1,3,6,1,4,1,52,4,2,32,1,4,2),_CtAgentDhcpServerAddressConflictLogging_Type())
ctAgentDhcpServerAddressConflictLogging.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerAddressConflictLogging.setStatus(_A)
_CtAgentDhcpServerAddressConflictTable_Object=MibTable
ctAgentDhcpServerAddressConflictTable=_CtAgentDhcpServerAddressConflictTable_Object((1,3,6,1,4,1,52,4,2,32,1,4,3))
if mibBuilder.loadTexts:ctAgentDhcpServerAddressConflictTable.setStatus(_A)
_CtAgentDhcpServerAddressConflictEntry_Object=MibTableRow
ctAgentDhcpServerAddressConflictEntry=_CtAgentDhcpServerAddressConflictEntry_Object((1,3,6,1,4,1,52,4,2,32,1,4,3,1))
ctAgentDhcpServerAddressConflictEntry.setIndexNames((0,_F,_R))
if mibBuilder.loadTexts:ctAgentDhcpServerAddressConflictEntry.setStatus(_A)
_CtAgentDhcpServerAddressConflictIP_Type=IpAddress
_CtAgentDhcpServerAddressConflictIP_Object=MibTableColumn
ctAgentDhcpServerAddressConflictIP=_CtAgentDhcpServerAddressConflictIP_Object((1,3,6,1,4,1,52,4,2,32,1,4,3,1,1),_CtAgentDhcpServerAddressConflictIP_Type())
ctAgentDhcpServerAddressConflictIP.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerAddressConflictIP.setStatus(_A)
class _CtAgentDhcpServerAddressConflictDetectionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ping',1),('gratuitousArp',2)))
_CtAgentDhcpServerAddressConflictDetectionType_Type.__name__=_D
_CtAgentDhcpServerAddressConflictDetectionType_Object=MibTableColumn
ctAgentDhcpServerAddressConflictDetectionType=_CtAgentDhcpServerAddressConflictDetectionType_Object((1,3,6,1,4,1,52,4,2,32,1,4,3,1,2),_CtAgentDhcpServerAddressConflictDetectionType_Type())
ctAgentDhcpServerAddressConflictDetectionType.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerAddressConflictDetectionType.setStatus(_A)
_CtAgentDhcpServerAddressConflictDetectionTime_Type=TimeTicks
_CtAgentDhcpServerAddressConflictDetectionTime_Object=MibTableColumn
ctAgentDhcpServerAddressConflictDetectionTime=_CtAgentDhcpServerAddressConflictDetectionTime_Object((1,3,6,1,4,1,52,4,2,32,1,4,3,1,3),_CtAgentDhcpServerAddressConflictDetectionTime_Type())
ctAgentDhcpServerAddressConflictDetectionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ctAgentDhcpServerAddressConflictDetectionTime.setStatus(_A)
_CtAgentDhcpServerAddressConflictStatus_Type=RowStatus
_CtAgentDhcpServerAddressConflictStatus_Object=MibTableColumn
ctAgentDhcpServerAddressConflictStatus=_CtAgentDhcpServerAddressConflictStatus_Object((1,3,6,1,4,1,52,4,2,32,1,4,3,1,4),_CtAgentDhcpServerAddressConflictStatus_Type())
ctAgentDhcpServerAddressConflictStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ctAgentDhcpServerAddressConflictStatus.setStatus(_A)
ctAgentDhcpServerPoolConfigEntry.registerAugmentions((_F,_S))
ctAgentDhcpServerPoolAllocationEntry.setIndexNames(*ctAgentDhcpServerPoolConfigEntry.getIndexNames())
mibBuilder.exportSymbols(_F,**{'ctFastPathDHCPServerMIB':ctFastPathDHCPServerMIB,'ctAgentDhcpServerGroup':ctAgentDhcpServerGroup,'ctAgentDhcpServerAdminMode':ctAgentDhcpServerAdminMode,'ctAgentDhcpServerPingPktNos':ctAgentDhcpServerPingPktNos,'ctAgentDhcpServerAutomaticBindingsNos':ctAgentDhcpServerAutomaticBindingsNos,'ctAgentDhcpServerExpiredBindingsNos':ctAgentDhcpServerExpiredBindingsNos,'ctAgentDhcpServerMalformedMessagesReceived':ctAgentDhcpServerMalformedMessagesReceived,'ctAgentDhcpServerDISCOVERMessagesReceived':ctAgentDhcpServerDISCOVERMessagesReceived,'ctAgentDhcpServerREQUESTMessagesReceived':ctAgentDhcpServerREQUESTMessagesReceived,'ctAgentDhcpServerDECLINEMessagesReceived':ctAgentDhcpServerDECLINEMessagesReceived,'ctAgentDhcpServerRELEASEMessagesReceived':ctAgentDhcpServerRELEASEMessagesReceived,'ctAgentDhcpServerINFORMMessagesReceived':ctAgentDhcpServerINFORMMessagesReceived,'ctAgentDhcpServerOFFERMessagesSent':ctAgentDhcpServerOFFERMessagesSent,'ctAgentDhcpServerACKMessagesSent':ctAgentDhcpServerACKMessagesSent,'ctAgentDhcpServerNAKMessagesSent':ctAgentDhcpServerNAKMessagesSent,'ctAgentDhcpServerClearStatistics':ctAgentDhcpServerClearStatistics,'ctAgentDhcpServerBootpAutomatic':ctAgentDhcpServerBootpAutomatic,'ctAgentDhcpServerPoolConfigGroup':ctAgentDhcpServerPoolConfigGroup,'ctAgentDhcpServerPoolNameCreate':ctAgentDhcpServerPoolNameCreate,'ctAgentDhcpServerPoolConfigTable':ctAgentDhcpServerPoolConfigTable,'ctAgentDhcpServerPoolConfigEntry':ctAgentDhcpServerPoolConfigEntry,_K:ctAgentDhcpServerPoolIndex,'ctAgentDhcpServerPoolName':ctAgentDhcpServerPoolName,'ctAgentDhcpServerPoolDefRouter':ctAgentDhcpServerPoolDefRouter,'ctAgentDhcpServerPoolDNSServer':ctAgentDhcpServerPoolDNSServer,'ctAgentDhcpServerPoolLeaseTime':ctAgentDhcpServerPoolLeaseTime,'ctAgentDhcpServerPoolType':ctAgentDhcpServerPoolType,'ctAgentDhcpServerPoolNetbiosNameServer':ctAgentDhcpServerPoolNetbiosNameServer,'ctAgentDhcpServerPoolNetbiosNodeType':ctAgentDhcpServerPoolNetbiosNodeType,'ctAgentDhcpServerPoolNextServer':ctAgentDhcpServerPoolNextServer,'ctAgentDhcpServerPoolDomainName':ctAgentDhcpServerPoolDomainName,'ctAgentDhcpServerPoolBootfile':ctAgentDhcpServerPoolBootfile,'ctAgentDhcpServerPoolRowStatus':ctAgentDhcpServerPoolRowStatus,'ctAgentDhcpServerPoolAllocationTable':ctAgentDhcpServerPoolAllocationTable,_S:ctAgentDhcpServerPoolAllocationEntry,'ctAgentDhcpServerPoolAllocationName':ctAgentDhcpServerPoolAllocationName,'ctAgentDhcpServerDynamicPoolIpAddress':ctAgentDhcpServerDynamicPoolIpAddress,'ctAgentDhcpServerDynamicPoolIpMask':ctAgentDhcpServerDynamicPoolIpMask,'ctAgentDhcpServerDynamicPoolIpPrefixLength':ctAgentDhcpServerDynamicPoolIpPrefixLength,'ctAgentDhcpServerPoolAllocationType':ctAgentDhcpServerPoolAllocationType,'ctAgentDhcpServerManualPoolClientIdentifier':ctAgentDhcpServerManualPoolClientIdentifier,'ctAgentDhcpServerManualPoolClientName':ctAgentDhcpServerManualPoolClientName,'ctAgentDhcpServerManualPoolClientHWAddr':ctAgentDhcpServerManualPoolClientHWAddr,'ctAgentDhcpServerManualPoolClientHWType':ctAgentDhcpServerManualPoolClientHWType,'ctAgentDhcpServerManualPoolIpAddress':ctAgentDhcpServerManualPoolIpAddress,'ctAgentDhcpServerManualPoolIpMask':ctAgentDhcpServerManualPoolIpMask,'ctAgentDhcpServerManualPoolIpPrefixLength':ctAgentDhcpServerManualPoolIpPrefixLength,'ctAgentDhcpServerExcludedAddressRangeCreate':ctAgentDhcpServerExcludedAddressRangeCreate,'ctAgentDhcpServerExcludedAddressRangeTable':ctAgentDhcpServerExcludedAddressRangeTable,'ctAgentDhcpServerExcludedAddressRangeEntry':ctAgentDhcpServerExcludedAddressRangeEntry,_N:ctAgentDhcpServerExcludedRangeIndex,'ctAgentDhcpServerExcludedStartIpAddress':ctAgentDhcpServerExcludedStartIpAddress,'ctAgentDhcpServerExcludedEndIpAddress':ctAgentDhcpServerExcludedEndIpAddress,'ctAgentDhcpServerExcludedAddressRangeStatus':ctAgentDhcpServerExcludedAddressRangeStatus,'ctAgentDhcpServerPoolOptionCreate':ctAgentDhcpServerPoolOptionCreate,'ctAgentDhcpServerPoolOptionTable':ctAgentDhcpServerPoolOptionTable,'ctAgentDhcpServerPoolOptionEntry':ctAgentDhcpServerPoolOptionEntry,_O:ctAgentDhcpServerPoolOptionIndex,_P:ctAgentDhcpServerPoolOptionCode,'ctAgentDhcpServerOptionPoolName':ctAgentDhcpServerOptionPoolName,'ctAgentDhcpServerPoolOptionAsciiData':ctAgentDhcpServerPoolOptionAsciiData,'ctAgentDhcpServerPoolOptionHexData':ctAgentDhcpServerPoolOptionHexData,'ctAgentDhcpServerPoolOptionIpAddressData':ctAgentDhcpServerPoolOptionIpAddressData,'ctAgentDhcpServerPoolOptionStatus':ctAgentDhcpServerPoolOptionStatus,'ctAgentDhcpServerLeaseGroup':ctAgentDhcpServerLeaseGroup,'ctAgentDhcpServerLeaseClearAllBindings':ctAgentDhcpServerLeaseClearAllBindings,'ctAgentDhcpServerLeaseTable':ctAgentDhcpServerLeaseTable,'ctAgentDhcpServerLeaseEntry':ctAgentDhcpServerLeaseEntry,_Q:ctAgentDhcpServerLeaseIPAddress,'ctAgentDhcpServerLeaseIPMask':ctAgentDhcpServerLeaseIPMask,'ctAgentDhcpServerLeaseHWAddress':ctAgentDhcpServerLeaseHWAddress,'ctAgentDhcpServerLeaseRemainingTime':ctAgentDhcpServerLeaseRemainingTime,'ctAgentDhcpServerLeaseType':ctAgentDhcpServerLeaseType,'ctAgentDhcpServerLeaseStatus':ctAgentDhcpServerLeaseStatus,'ctAgentDhcpServerAddressConflictGroup':ctAgentDhcpServerAddressConflictGroup,'ctAgentDhcpServerClearAllAddressConflicts':ctAgentDhcpServerClearAllAddressConflicts,'ctAgentDhcpServerAddressConflictLogging':ctAgentDhcpServerAddressConflictLogging,'ctAgentDhcpServerAddressConflictTable':ctAgentDhcpServerAddressConflictTable,'ctAgentDhcpServerAddressConflictEntry':ctAgentDhcpServerAddressConflictEntry,_R:ctAgentDhcpServerAddressConflictIP,'ctAgentDhcpServerAddressConflictDetectionType':ctAgentDhcpServerAddressConflictDetectionType,'ctAgentDhcpServerAddressConflictDetectionTime':ctAgentDhcpServerAddressConflictDetectionTime,'ctAgentDhcpServerAddressConflictStatus':ctAgentDhcpServerAddressConflictStatus})