_w='fsDhcpv6ServerConfigurationObjects'
_v='fsDhcpv6ServerCountersObjects'
_u='fsIPv6RawStatus'
_t='fsIPv6AddrLease'
_s='fsSeconDNSServerIPv6Address'
_r='fsPrimDNSServerIPv6Address'
_q='fsIPv6NetPrefixLen'
_p='fsIPv6PoolStopAddr'
_o='fsIPv6PoolStartAddr'
_n='fsIPv6PoolUsageRawStatus'
_m='fsIPv6DHCPIPPoolUsage'
_l='fsDhcpv6ServerBindingsIfIndex'
_k='fsDhcpv6ServerBindingsDuration'
_j='fsDhcpv6ServerBindingsPrefixLength'
_i='fsDhcpv6ServerBindingsPrefix'
_h='fsDhcpv6ServerBindingsAddress'
_g='fsDhcpv6ServerNumBindings'
_f='fsDhcpv6ServerHCountReqSuctimes'
_e='fsDhcpv6ServerHCountReqtimes'
_d='fsDhcpv6ServerHCountRelayreply'
_c='fsDhcpv6ServerHCountRelayforward'
_b='fsDhcpv6ServerHCountDroppedError'
_a='fsDhcpv6ServerHCountDroppedUnknown'
_Z='fsDhcpv6ServerHCountOutPkts'
_Y='fsDhcpv6ServerHCountInPkts'
_X='fsDhcpv6ServerHCountFailReplies'
_W='fsDhcpv6ServerHCountSuccReplies'
_V='fsDhcpv6ServerHCountAdvertises'
_U='fsDhcpv6ServerHCountRebinds'
_T='fsDhcpv6ServerHCountConfirms'
_S='fsDhcpv6ServerHCountInforms'
_R='fsDhcpv6ServerHCountReleases'
_Q='fsDhcpv6ServerHCountDeclines'
_P='fsDhcpv6ServerHCountRenews'
_O='fsDhcpv6ServerHCountSolicits'
_N='OctetString'
_M='fsIPv6PoolName'
_L='fsIPv6PoolCfgIndex'
_K='fsIPv6PoolUsageIndex'
_J='fsDhcpv6ServerBindingsIaId'
_I='fsDhcpv6ServerBindingsIaType'
_H='fsDhcpv6ServerBindingsClientDuid'
_G='fsDhcpv6ServerBindingsPoolName'
_F='Integer32'
_E='DisplayString'
_D='read-create'
_C='read-only'
_B='FS-DHCPv6-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddressIPv6,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv6')
Ipv6Address,Ipv6AddressPrefix=mibBuilder.importSymbols('IPV6-TC','Ipv6Address','Ipv6AddressPrefix')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeInterval=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention','TimeInterval')
fsDhcpv6MIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,45))
if mibBuilder.loadTexts:fsDhcpv6MIB.setRevisions(('2009-03-16 00:00',))
_FsDhcpv6MIBObjects_ObjectIdentity=ObjectIdentity
fsDhcpv6MIBObjects=_FsDhcpv6MIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,45,1))
if mibBuilder.loadTexts:fsDhcpv6MIBObjects.setStatus(_A)
_FsDhcpv6ServerMIBObjects_ObjectIdentity=ObjectIdentity
fsDhcpv6ServerMIBObjects=_FsDhcpv6ServerMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,45,1,1))
if mibBuilder.loadTexts:fsDhcpv6ServerMIBObjects.setStatus(_A)
_FsDhcpv6ServerCounters_ObjectIdentity=ObjectIdentity
fsDhcpv6ServerCounters=_FsDhcpv6ServerCounters_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,1))
if mibBuilder.loadTexts:fsDhcpv6ServerCounters.setStatus(_A)
_FsDhcpv6ServerHCountSolicits_Type=Counter64
_FsDhcpv6ServerHCountSolicits_Object=MibScalar
fsDhcpv6ServerHCountSolicits=_FsDhcpv6ServerHCountSolicits_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,1,1),_FsDhcpv6ServerHCountSolicits_Type())
fsDhcpv6ServerHCountSolicits.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerHCountSolicits.setStatus(_A)
_FsDhcpv6ServerHCountRequests_Type=Counter64
_FsDhcpv6ServerHCountRequests_Object=MibScalar
fsDhcpv6ServerHCountRequests=_FsDhcpv6ServerHCountRequests_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,1,2),_FsDhcpv6ServerHCountRequests_Type())
fsDhcpv6ServerHCountRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerHCountRequests.setStatus(_A)
_FsDhcpv6ServerHCountRenews_Type=Counter64
_FsDhcpv6ServerHCountRenews_Object=MibScalar
fsDhcpv6ServerHCountRenews=_FsDhcpv6ServerHCountRenews_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,1,3),_FsDhcpv6ServerHCountRenews_Type())
fsDhcpv6ServerHCountRenews.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerHCountRenews.setStatus(_A)
_FsDhcpv6ServerHCountDeclines_Type=Counter64
_FsDhcpv6ServerHCountDeclines_Object=MibScalar
fsDhcpv6ServerHCountDeclines=_FsDhcpv6ServerHCountDeclines_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,1,4),_FsDhcpv6ServerHCountDeclines_Type())
fsDhcpv6ServerHCountDeclines.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerHCountDeclines.setStatus(_A)
_FsDhcpv6ServerHCountReleases_Type=Counter64
_FsDhcpv6ServerHCountReleases_Object=MibScalar
fsDhcpv6ServerHCountReleases=_FsDhcpv6ServerHCountReleases_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,1,5),_FsDhcpv6ServerHCountReleases_Type())
fsDhcpv6ServerHCountReleases.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerHCountReleases.setStatus(_A)
_FsDhcpv6ServerHCountInforms_Type=Counter64
_FsDhcpv6ServerHCountInforms_Object=MibScalar
fsDhcpv6ServerHCountInforms=_FsDhcpv6ServerHCountInforms_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,1,6),_FsDhcpv6ServerHCountInforms_Type())
fsDhcpv6ServerHCountInforms.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerHCountInforms.setStatus(_A)
_FsDhcpv6ServerHCountConfirms_Type=Counter64
_FsDhcpv6ServerHCountConfirms_Object=MibScalar
fsDhcpv6ServerHCountConfirms=_FsDhcpv6ServerHCountConfirms_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,1,7),_FsDhcpv6ServerHCountConfirms_Type())
fsDhcpv6ServerHCountConfirms.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerHCountConfirms.setStatus(_A)
_FsDhcpv6ServerHCountRebinds_Type=Counter64
_FsDhcpv6ServerHCountRebinds_Object=MibScalar
fsDhcpv6ServerHCountRebinds=_FsDhcpv6ServerHCountRebinds_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,1,8),_FsDhcpv6ServerHCountRebinds_Type())
fsDhcpv6ServerHCountRebinds.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerHCountRebinds.setStatus(_A)
_FsDhcpv6ServerHCountAdvertises_Type=Counter64
_FsDhcpv6ServerHCountAdvertises_Object=MibScalar
fsDhcpv6ServerHCountAdvertises=_FsDhcpv6ServerHCountAdvertises_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,1,9),_FsDhcpv6ServerHCountAdvertises_Type())
fsDhcpv6ServerHCountAdvertises.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerHCountAdvertises.setStatus(_A)
_FsDhcpv6ServerHCountSuccReplies_Type=Counter64
_FsDhcpv6ServerHCountSuccReplies_Object=MibScalar
fsDhcpv6ServerHCountSuccReplies=_FsDhcpv6ServerHCountSuccReplies_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,1,10),_FsDhcpv6ServerHCountSuccReplies_Type())
fsDhcpv6ServerHCountSuccReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerHCountSuccReplies.setStatus(_A)
_FsDhcpv6ServerHCountFailReplies_Type=Counter64
_FsDhcpv6ServerHCountFailReplies_Object=MibScalar
fsDhcpv6ServerHCountFailReplies=_FsDhcpv6ServerHCountFailReplies_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,1,11),_FsDhcpv6ServerHCountFailReplies_Type())
fsDhcpv6ServerHCountFailReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerHCountFailReplies.setStatus(_A)
_FsDhcpv6ServerHCountInPkts_Type=Counter64
_FsDhcpv6ServerHCountInPkts_Object=MibScalar
fsDhcpv6ServerHCountInPkts=_FsDhcpv6ServerHCountInPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,1,12),_FsDhcpv6ServerHCountInPkts_Type())
fsDhcpv6ServerHCountInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerHCountInPkts.setStatus(_A)
_FsDhcpv6ServerHCountOutPkts_Type=Counter64
_FsDhcpv6ServerHCountOutPkts_Object=MibScalar
fsDhcpv6ServerHCountOutPkts=_FsDhcpv6ServerHCountOutPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,1,13),_FsDhcpv6ServerHCountOutPkts_Type())
fsDhcpv6ServerHCountOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerHCountOutPkts.setStatus(_A)
_FsDhcpv6ServerHCountDroppedUnknown_Type=Counter64
_FsDhcpv6ServerHCountDroppedUnknown_Object=MibScalar
fsDhcpv6ServerHCountDroppedUnknown=_FsDhcpv6ServerHCountDroppedUnknown_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,1,14),_FsDhcpv6ServerHCountDroppedUnknown_Type())
fsDhcpv6ServerHCountDroppedUnknown.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerHCountDroppedUnknown.setStatus(_A)
_FsDhcpv6ServerHCountDroppedError_Type=Counter64
_FsDhcpv6ServerHCountDroppedError_Object=MibScalar
fsDhcpv6ServerHCountDroppedError=_FsDhcpv6ServerHCountDroppedError_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,1,15),_FsDhcpv6ServerHCountDroppedError_Type())
fsDhcpv6ServerHCountDroppedError.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerHCountDroppedError.setStatus(_A)
_FsDhcpv6ServerHCountRelayforward_Type=Counter64
_FsDhcpv6ServerHCountRelayforward_Object=MibScalar
fsDhcpv6ServerHCountRelayforward=_FsDhcpv6ServerHCountRelayforward_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,1,16),_FsDhcpv6ServerHCountRelayforward_Type())
fsDhcpv6ServerHCountRelayforward.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerHCountRelayforward.setStatus(_A)
_FsDhcpv6ServerHCountRelayreply_Type=Counter64
_FsDhcpv6ServerHCountRelayreply_Object=MibScalar
fsDhcpv6ServerHCountRelayreply=_FsDhcpv6ServerHCountRelayreply_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,1,17),_FsDhcpv6ServerHCountRelayreply_Type())
fsDhcpv6ServerHCountRelayreply.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerHCountRelayreply.setStatus(_A)
_FsDhcpv6ServerHCountReqtimes_Type=Counter64
_FsDhcpv6ServerHCountReqtimes_Object=MibScalar
fsDhcpv6ServerHCountReqtimes=_FsDhcpv6ServerHCountReqtimes_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,1,18),_FsDhcpv6ServerHCountReqtimes_Type())
fsDhcpv6ServerHCountReqtimes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerHCountReqtimes.setStatus(_A)
_FsDhcpv6ServerHCountReqSuctimes_Type=Counter64
_FsDhcpv6ServerHCountReqSuctimes_Object=MibScalar
fsDhcpv6ServerHCountReqSuctimes=_FsDhcpv6ServerHCountReqSuctimes_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,1,19),_FsDhcpv6ServerHCountReqSuctimes_Type())
fsDhcpv6ServerHCountReqSuctimes.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerHCountReqSuctimes.setStatus(_A)
_FsDhcpv6ServerConfiguration_ObjectIdentity=ObjectIdentity
fsDhcpv6ServerConfiguration=_FsDhcpv6ServerConfiguration_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2))
if mibBuilder.loadTexts:fsDhcpv6ServerConfiguration.setStatus(_A)
_FsDhcpv6ServerNumBindings_Type=Counter32
_FsDhcpv6ServerNumBindings_Object=MibScalar
fsDhcpv6ServerNumBindings=_FsDhcpv6ServerNumBindings_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,1),_FsDhcpv6ServerNumBindings_Type())
fsDhcpv6ServerNumBindings.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerNumBindings.setStatus(_A)
_FsDhcpv6ServerBindingsTable_Object=MibTable
fsDhcpv6ServerBindingsTable=_FsDhcpv6ServerBindingsTable_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,2))
if mibBuilder.loadTexts:fsDhcpv6ServerBindingsTable.setStatus(_A)
_FsDhcpv6ServerBindingsEntry_Object=MibTableRow
fsDhcpv6ServerBindingsEntry=_FsDhcpv6ServerBindingsEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,2,1))
fsDhcpv6ServerBindingsEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:fsDhcpv6ServerBindingsEntry.setStatus(_A)
class _FsDhcpv6ServerBindingsPoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsDhcpv6ServerBindingsPoolName_Type.__name__=_E
_FsDhcpv6ServerBindingsPoolName_Object=MibTableColumn
fsDhcpv6ServerBindingsPoolName=_FsDhcpv6ServerBindingsPoolName_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,2,1,1),_FsDhcpv6ServerBindingsPoolName_Type())
fsDhcpv6ServerBindingsPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerBindingsPoolName.setStatus(_A)
class _FsDhcpv6ServerBindingsClientDuid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,130))
_FsDhcpv6ServerBindingsClientDuid_Type.__name__=_N
_FsDhcpv6ServerBindingsClientDuid_Object=MibTableColumn
fsDhcpv6ServerBindingsClientDuid=_FsDhcpv6ServerBindingsClientDuid_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,2,1,2),_FsDhcpv6ServerBindingsClientDuid_Type())
fsDhcpv6ServerBindingsClientDuid.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerBindingsClientDuid.setStatus(_A)
class _FsDhcpv6ServerBindingsIaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('iana',1),('iata',2),('iapd',3)))
_FsDhcpv6ServerBindingsIaType_Type.__name__=_F
_FsDhcpv6ServerBindingsIaType_Object=MibTableColumn
fsDhcpv6ServerBindingsIaType=_FsDhcpv6ServerBindingsIaType_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,2,1,3),_FsDhcpv6ServerBindingsIaType_Type())
fsDhcpv6ServerBindingsIaType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerBindingsIaType.setStatus(_A)
_FsDhcpv6ServerBindingsIaId_Type=Unsigned32
_FsDhcpv6ServerBindingsIaId_Object=MibTableColumn
fsDhcpv6ServerBindingsIaId=_FsDhcpv6ServerBindingsIaId_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,2,1,4),_FsDhcpv6ServerBindingsIaId_Type())
fsDhcpv6ServerBindingsIaId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerBindingsIaId.setStatus(_A)
_FsDhcpv6ServerBindingsAddress_Type=Ipv6Address
_FsDhcpv6ServerBindingsAddress_Object=MibTableColumn
fsDhcpv6ServerBindingsAddress=_FsDhcpv6ServerBindingsAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,2,1,5),_FsDhcpv6ServerBindingsAddress_Type())
fsDhcpv6ServerBindingsAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerBindingsAddress.setStatus(_A)
_FsDhcpv6ServerBindingsPrefix_Type=Ipv6AddressPrefix
_FsDhcpv6ServerBindingsPrefix_Object=MibTableColumn
fsDhcpv6ServerBindingsPrefix=_FsDhcpv6ServerBindingsPrefix_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,2,1,6),_FsDhcpv6ServerBindingsPrefix_Type())
fsDhcpv6ServerBindingsPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerBindingsPrefix.setStatus(_A)
class _FsDhcpv6ServerBindingsPrefixLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_FsDhcpv6ServerBindingsPrefixLength_Type.__name__=_F
_FsDhcpv6ServerBindingsPrefixLength_Object=MibTableColumn
fsDhcpv6ServerBindingsPrefixLength=_FsDhcpv6ServerBindingsPrefixLength_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,2,1,7),_FsDhcpv6ServerBindingsPrefixLength_Type())
fsDhcpv6ServerBindingsPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerBindingsPrefixLength.setStatus(_A)
_FsDhcpv6ServerBindingsDuration_Type=Unsigned32
_FsDhcpv6ServerBindingsDuration_Object=MibTableColumn
fsDhcpv6ServerBindingsDuration=_FsDhcpv6ServerBindingsDuration_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,2,1,8),_FsDhcpv6ServerBindingsDuration_Type())
fsDhcpv6ServerBindingsDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerBindingsDuration.setStatus(_A)
_FsDhcpv6ServerBindingsIfIndex_Type=InterfaceIndex
_FsDhcpv6ServerBindingsIfIndex_Object=MibTableColumn
fsDhcpv6ServerBindingsIfIndex=_FsDhcpv6ServerBindingsIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,2,1,9),_FsDhcpv6ServerBindingsIfIndex_Type())
fsDhcpv6ServerBindingsIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpv6ServerBindingsIfIndex.setStatus(_A)
_FsDhcpv6ServerPoolUsageTable_Object=MibTable
fsDhcpv6ServerPoolUsageTable=_FsDhcpv6ServerPoolUsageTable_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,3))
if mibBuilder.loadTexts:fsDhcpv6ServerPoolUsageTable.setStatus(_A)
_FsDhcpv6ServerPoolEntry_Object=MibTableRow
fsDhcpv6ServerPoolEntry=_FsDhcpv6ServerPoolEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,3,1))
fsDhcpv6ServerPoolEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:fsDhcpv6ServerPoolEntry.setStatus(_A)
_FsIPv6PoolUsageIndex_Type=Unsigned32
_FsIPv6PoolUsageIndex_Object=MibTableColumn
fsIPv6PoolUsageIndex=_FsIPv6PoolUsageIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,3,1,1),_FsIPv6PoolUsageIndex_Type())
fsIPv6PoolUsageIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPv6PoolUsageIndex.setStatus(_A)
class _FsIPv6PoolUsageName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsIPv6PoolUsageName_Type.__name__=_E
_FsIPv6PoolUsageName_Object=MibTableColumn
fsIPv6PoolUsageName=_FsIPv6PoolUsageName_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,3,1,2),_FsIPv6PoolUsageName_Type())
fsIPv6PoolUsageName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIPv6PoolUsageName.setStatus(_A)
_FsIPv6DHCPIPPoolUsage_Type=Unsigned32
_FsIPv6DHCPIPPoolUsage_Object=MibTableColumn
fsIPv6DHCPIPPoolUsage=_FsIPv6DHCPIPPoolUsage_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,3,1,3),_FsIPv6DHCPIPPoolUsage_Type())
fsIPv6DHCPIPPoolUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPv6DHCPIPPoolUsage.setStatus(_A)
_FsIPv6PoolUsageRawStatus_Type=RowStatus
_FsIPv6PoolUsageRawStatus_Object=MibTableColumn
fsIPv6PoolUsageRawStatus=_FsIPv6PoolUsageRawStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,3,1,4),_FsIPv6PoolUsageRawStatus_Type())
fsIPv6PoolUsageRawStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIPv6PoolUsageRawStatus.setStatus(_A)
_FsDhcpv6ServerPoolConfigTable_Object=MibTable
fsDhcpv6ServerPoolConfigTable=_FsDhcpv6ServerPoolConfigTable_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,4))
if mibBuilder.loadTexts:fsDhcpv6ServerPoolConfigTable.setStatus(_A)
_FsDhcpv6ServerPoolCfgEntry_Object=MibTableRow
fsDhcpv6ServerPoolCfgEntry=_FsDhcpv6ServerPoolCfgEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,4,1))
fsDhcpv6ServerPoolCfgEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:fsDhcpv6ServerPoolCfgEntry.setStatus(_A)
_FsIPv6PoolCfgIndex_Type=Unsigned32
_FsIPv6PoolCfgIndex_Object=MibTableColumn
fsIPv6PoolCfgIndex=_FsIPv6PoolCfgIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,4,1,1),_FsIPv6PoolCfgIndex_Type())
fsIPv6PoolCfgIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsIPv6PoolCfgIndex.setStatus(_A)
class _FsIPv6PoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsIPv6PoolName_Type.__name__=_E
_FsIPv6PoolName_Object=MibTableColumn
fsIPv6PoolName=_FsIPv6PoolName_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,4,1,2),_FsIPv6PoolName_Type())
fsIPv6PoolName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIPv6PoolName.setStatus(_A)
_FsIPv6PoolStartAddr_Type=InetAddressIPv6
_FsIPv6PoolStartAddr_Object=MibTableColumn
fsIPv6PoolStartAddr=_FsIPv6PoolStartAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,4,1,3),_FsIPv6PoolStartAddr_Type())
fsIPv6PoolStartAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIPv6PoolStartAddr.setStatus(_A)
_FsIPv6PoolStopAddr_Type=InetAddressIPv6
_FsIPv6PoolStopAddr_Object=MibTableColumn
fsIPv6PoolStopAddr=_FsIPv6PoolStopAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,4,1,4),_FsIPv6PoolStopAddr_Type())
fsIPv6PoolStopAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIPv6PoolStopAddr.setStatus(_A)
_FsIPv6NetPrefixLen_Type=Unsigned32
_FsIPv6NetPrefixLen_Object=MibTableColumn
fsIPv6NetPrefixLen=_FsIPv6NetPrefixLen_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,4,1,5),_FsIPv6NetPrefixLen_Type())
fsIPv6NetPrefixLen.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIPv6NetPrefixLen.setStatus(_A)
_FsPrimDNSServerIPv6Address_Type=InetAddressIPv6
_FsPrimDNSServerIPv6Address_Object=MibTableColumn
fsPrimDNSServerIPv6Address=_FsPrimDNSServerIPv6Address_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,4,1,6),_FsPrimDNSServerIPv6Address_Type())
fsPrimDNSServerIPv6Address.setMaxAccess(_D)
if mibBuilder.loadTexts:fsPrimDNSServerIPv6Address.setStatus(_A)
_FsSeconDNSServerIPv6Address_Type=InetAddressIPv6
_FsSeconDNSServerIPv6Address_Object=MibTableColumn
fsSeconDNSServerIPv6Address=_FsSeconDNSServerIPv6Address_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,4,1,7),_FsSeconDNSServerIPv6Address_Type())
fsSeconDNSServerIPv6Address.setMaxAccess(_D)
if mibBuilder.loadTexts:fsSeconDNSServerIPv6Address.setStatus(_A)
_FsIPv6AddrLease_Type=TimeTicks
_FsIPv6AddrLease_Object=MibTableColumn
fsIPv6AddrLease=_FsIPv6AddrLease_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,4,1,8),_FsIPv6AddrLease_Type())
fsIPv6AddrLease.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIPv6AddrLease.setStatus(_A)
_FsIPv6RawStatus_Type=RowStatus
_FsIPv6RawStatus_Object=MibTableColumn
fsIPv6RawStatus=_FsIPv6RawStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,45,1,1,2,4,1,9),_FsIPv6RawStatus_Type())
fsIPv6RawStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsIPv6RawStatus.setStatus(_A)
_FsDhcpv6MIBConformance_ObjectIdentity=ObjectIdentity
fsDhcpv6MIBConformance=_FsDhcpv6MIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,45,2))
if mibBuilder.loadTexts:fsDhcpv6MIBConformance.setStatus(_A)
_FsDhcpv6MIBCompliances_ObjectIdentity=ObjectIdentity
fsDhcpv6MIBCompliances=_FsDhcpv6MIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,45,2,1))
_FsDhcpv6MIBGroups_ObjectIdentity=ObjectIdentity
fsDhcpv6MIBGroups=_FsDhcpv6MIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,45,2,2))
fsDhcpv6ServerCountersObjects=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,45,2,2,1))
fsDhcpv6ServerCountersObjects.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:fsDhcpv6ServerCountersObjects.setStatus(_A)
fsDhcpv6ServerConfigurationObjects=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,45,2,2,2))
fsDhcpv6ServerConfigurationObjects.setObjects(*((_B,_g),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:fsDhcpv6ServerConfigurationObjects.setStatus(_A)
fsDhcpv6ServerPoolUsageTableObjects=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,45,2,2,3))
fsDhcpv6ServerPoolUsageTableObjects.setObjects(*((_B,_K),(_B,_M),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:fsDhcpv6ServerPoolUsageTableObjects.setStatus(_A)
fsDhcpv6ServerPoolConfigGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,45,2,2,4))
fsDhcpv6ServerPoolConfigGroup.setObjects(*((_B,_L),(_B,_M),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:fsDhcpv6ServerPoolConfigGroup.setStatus(_A)
fsDhcpv6ServerCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,45,2,1,1))
fsDhcpv6ServerCompliance.setObjects(*((_B,_v),(_B,_w)))
if mibBuilder.loadTexts:fsDhcpv6ServerCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsDhcpv6MIB':fsDhcpv6MIB,'fsDhcpv6MIBObjects':fsDhcpv6MIBObjects,'fsDhcpv6ServerMIBObjects':fsDhcpv6ServerMIBObjects,'fsDhcpv6ServerCounters':fsDhcpv6ServerCounters,_O:fsDhcpv6ServerHCountSolicits,'fsDhcpv6ServerHCountRequests':fsDhcpv6ServerHCountRequests,_P:fsDhcpv6ServerHCountRenews,_Q:fsDhcpv6ServerHCountDeclines,_R:fsDhcpv6ServerHCountReleases,_S:fsDhcpv6ServerHCountInforms,_T:fsDhcpv6ServerHCountConfirms,_U:fsDhcpv6ServerHCountRebinds,_V:fsDhcpv6ServerHCountAdvertises,_W:fsDhcpv6ServerHCountSuccReplies,_X:fsDhcpv6ServerHCountFailReplies,_Y:fsDhcpv6ServerHCountInPkts,_Z:fsDhcpv6ServerHCountOutPkts,_a:fsDhcpv6ServerHCountDroppedUnknown,_b:fsDhcpv6ServerHCountDroppedError,_c:fsDhcpv6ServerHCountRelayforward,_d:fsDhcpv6ServerHCountRelayreply,_e:fsDhcpv6ServerHCountReqtimes,_f:fsDhcpv6ServerHCountReqSuctimes,'fsDhcpv6ServerConfiguration':fsDhcpv6ServerConfiguration,_g:fsDhcpv6ServerNumBindings,'fsDhcpv6ServerBindingsTable':fsDhcpv6ServerBindingsTable,'fsDhcpv6ServerBindingsEntry':fsDhcpv6ServerBindingsEntry,_G:fsDhcpv6ServerBindingsPoolName,_H:fsDhcpv6ServerBindingsClientDuid,_I:fsDhcpv6ServerBindingsIaType,_J:fsDhcpv6ServerBindingsIaId,_h:fsDhcpv6ServerBindingsAddress,_i:fsDhcpv6ServerBindingsPrefix,_j:fsDhcpv6ServerBindingsPrefixLength,_k:fsDhcpv6ServerBindingsDuration,_l:fsDhcpv6ServerBindingsIfIndex,'fsDhcpv6ServerPoolUsageTable':fsDhcpv6ServerPoolUsageTable,'fsDhcpv6ServerPoolEntry':fsDhcpv6ServerPoolEntry,_K:fsIPv6PoolUsageIndex,'fsIPv6PoolUsageName':fsIPv6PoolUsageName,_m:fsIPv6DHCPIPPoolUsage,_n:fsIPv6PoolUsageRawStatus,'fsDhcpv6ServerPoolConfigTable':fsDhcpv6ServerPoolConfigTable,'fsDhcpv6ServerPoolCfgEntry':fsDhcpv6ServerPoolCfgEntry,_L:fsIPv6PoolCfgIndex,_M:fsIPv6PoolName,_o:fsIPv6PoolStartAddr,_p:fsIPv6PoolStopAddr,_q:fsIPv6NetPrefixLen,_r:fsPrimDNSServerIPv6Address,_s:fsSeconDNSServerIPv6Address,_t:fsIPv6AddrLease,_u:fsIPv6RawStatus,'fsDhcpv6MIBConformance':fsDhcpv6MIBConformance,'fsDhcpv6MIBCompliances':fsDhcpv6MIBCompliances,'fsDhcpv6ServerCompliance':fsDhcpv6ServerCompliance,'fsDhcpv6MIBGroups':fsDhcpv6MIBGroups,_v:fsDhcpv6ServerCountersObjects,_w:fsDhcpv6ServerConfigurationObjects,'fsDhcpv6ServerPoolUsageTableObjects':fsDhcpv6ServerPoolUsageTableObjects,'fsDhcpv6ServerPoolConfigGroup':fsDhcpv6ServerPoolConfigGroup})