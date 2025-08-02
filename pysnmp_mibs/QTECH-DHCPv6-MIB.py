_l='qtechDhcpv6ServerConfigurationObjects'
_k='qtechDhcpv6ServerCountersObjects'
_j='qtechDhcpv6ServerDHCPIPPoolUsage'
_i='qtechDhcpv6ServerBindingsIfIndex'
_h='qtechDhcpv6ServerBindingsDuration'
_g='qtechDhcpv6ServerBindingsPrefixLength'
_f='qtechDhcpv6ServerBindingsPrefix'
_e='qtechDhcpv6ServerBindingsAddress'
_d='qtechDhcpv6ServerNumBindings'
_c='qtechDhcpv6ServerHCountReqSuctimes'
_b='qtechDhcpv6ServerHCountReqtimes'
_a='qtechDhcpv6ServerHCountRelayreply'
_Z='qtechDhcpv6ServerHCountRelayforward'
_Y='qtechDhcpv6ServerHCountDroppedError'
_X='qtechDhcpv6ServerHCountDroppedUnknown'
_W='qtechDhcpv6ServerHCountOutPkts'
_V='qtechDhcpv6ServerHCountInPkts'
_U='qtechDhcpv6ServerHCountFailReplies'
_T='qtechDhcpv6ServerHCountSuccReplies'
_S='qtechDhcpv6ServerHCountAdvertises'
_R='qtechDhcpv6ServerHCountRebinds'
_Q='qtechDhcpv6ServerHCountConfirms'
_P='qtechDhcpv6ServerHCountInforms'
_O='qtechDhcpv6ServerHCountReleases'
_N='qtechDhcpv6ServerHCountDeclines'
_M='qtechDhcpv6ServerHCountRenews'
_L='qtechDhcpv6ServerHCountSolicits'
_K='OctetString'
_J='qtechDhcpv6ServerIPPoolName'
_I='qtechDhcpv6ServerBindingsIaId'
_H='qtechDhcpv6ServerBindingsIaType'
_G='qtechDhcpv6ServerBindingsClientDuid'
_F='qtechDhcpv6ServerBindingsPoolName'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='QTECH-DHCPv6-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
Ipv6Address,Ipv6AddressPrefix=mibBuilder.importSymbols('IPV6-TC','Ipv6Address','Ipv6AddressPrefix')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeInterval=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention','TimeInterval')
qtechDhcpv6MIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,45))
if mibBuilder.loadTexts:qtechDhcpv6MIB.setRevisions(('2009-03-16 00:00',))
_QtechDhcpv6MIBObjects_ObjectIdentity=ObjectIdentity
qtechDhcpv6MIBObjects=_QtechDhcpv6MIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,45,1))
if mibBuilder.loadTexts:qtechDhcpv6MIBObjects.setStatus(_A)
_QtechDhcpv6ServerMIBObjects_ObjectIdentity=ObjectIdentity
qtechDhcpv6ServerMIBObjects=_QtechDhcpv6ServerMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,45,1,1))
if mibBuilder.loadTexts:qtechDhcpv6ServerMIBObjects.setStatus(_A)
_QtechDhcpv6ServerCounters_ObjectIdentity=ObjectIdentity
qtechDhcpv6ServerCounters=_QtechDhcpv6ServerCounters_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,1))
if mibBuilder.loadTexts:qtechDhcpv6ServerCounters.setStatus(_A)
_QtechDhcpv6ServerHCountSolicits_Type=Counter64
_QtechDhcpv6ServerHCountSolicits_Object=MibScalar
qtechDhcpv6ServerHCountSolicits=_QtechDhcpv6ServerHCountSolicits_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,1,1),_QtechDhcpv6ServerHCountSolicits_Type())
qtechDhcpv6ServerHCountSolicits.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerHCountSolicits.setStatus(_A)
_QtechDhcpv6ServerHCountRequests_Type=Counter64
_QtechDhcpv6ServerHCountRequests_Object=MibScalar
qtechDhcpv6ServerHCountRequests=_QtechDhcpv6ServerHCountRequests_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,1,2),_QtechDhcpv6ServerHCountRequests_Type())
qtechDhcpv6ServerHCountRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerHCountRequests.setStatus(_A)
_QtechDhcpv6ServerHCountRenews_Type=Counter64
_QtechDhcpv6ServerHCountRenews_Object=MibScalar
qtechDhcpv6ServerHCountRenews=_QtechDhcpv6ServerHCountRenews_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,1,3),_QtechDhcpv6ServerHCountRenews_Type())
qtechDhcpv6ServerHCountRenews.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerHCountRenews.setStatus(_A)
_QtechDhcpv6ServerHCountDeclines_Type=Counter64
_QtechDhcpv6ServerHCountDeclines_Object=MibScalar
qtechDhcpv6ServerHCountDeclines=_QtechDhcpv6ServerHCountDeclines_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,1,4),_QtechDhcpv6ServerHCountDeclines_Type())
qtechDhcpv6ServerHCountDeclines.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerHCountDeclines.setStatus(_A)
_QtechDhcpv6ServerHCountReleases_Type=Counter64
_QtechDhcpv6ServerHCountReleases_Object=MibScalar
qtechDhcpv6ServerHCountReleases=_QtechDhcpv6ServerHCountReleases_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,1,5),_QtechDhcpv6ServerHCountReleases_Type())
qtechDhcpv6ServerHCountReleases.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerHCountReleases.setStatus(_A)
_QtechDhcpv6ServerHCountInforms_Type=Counter64
_QtechDhcpv6ServerHCountInforms_Object=MibScalar
qtechDhcpv6ServerHCountInforms=_QtechDhcpv6ServerHCountInforms_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,1,6),_QtechDhcpv6ServerHCountInforms_Type())
qtechDhcpv6ServerHCountInforms.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerHCountInforms.setStatus(_A)
_QtechDhcpv6ServerHCountConfirms_Type=Counter64
_QtechDhcpv6ServerHCountConfirms_Object=MibScalar
qtechDhcpv6ServerHCountConfirms=_QtechDhcpv6ServerHCountConfirms_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,1,7),_QtechDhcpv6ServerHCountConfirms_Type())
qtechDhcpv6ServerHCountConfirms.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerHCountConfirms.setStatus(_A)
_QtechDhcpv6ServerHCountRebinds_Type=Counter64
_QtechDhcpv6ServerHCountRebinds_Object=MibScalar
qtechDhcpv6ServerHCountRebinds=_QtechDhcpv6ServerHCountRebinds_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,1,8),_QtechDhcpv6ServerHCountRebinds_Type())
qtechDhcpv6ServerHCountRebinds.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerHCountRebinds.setStatus(_A)
_QtechDhcpv6ServerHCountAdvertises_Type=Counter64
_QtechDhcpv6ServerHCountAdvertises_Object=MibScalar
qtechDhcpv6ServerHCountAdvertises=_QtechDhcpv6ServerHCountAdvertises_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,1,9),_QtechDhcpv6ServerHCountAdvertises_Type())
qtechDhcpv6ServerHCountAdvertises.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerHCountAdvertises.setStatus(_A)
_QtechDhcpv6ServerHCountSuccReplies_Type=Counter64
_QtechDhcpv6ServerHCountSuccReplies_Object=MibScalar
qtechDhcpv6ServerHCountSuccReplies=_QtechDhcpv6ServerHCountSuccReplies_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,1,10),_QtechDhcpv6ServerHCountSuccReplies_Type())
qtechDhcpv6ServerHCountSuccReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerHCountSuccReplies.setStatus(_A)
_QtechDhcpv6ServerHCountFailReplies_Type=Counter64
_QtechDhcpv6ServerHCountFailReplies_Object=MibScalar
qtechDhcpv6ServerHCountFailReplies=_QtechDhcpv6ServerHCountFailReplies_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,1,11),_QtechDhcpv6ServerHCountFailReplies_Type())
qtechDhcpv6ServerHCountFailReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerHCountFailReplies.setStatus(_A)
_QtechDhcpv6ServerHCountInPkts_Type=Counter64
_QtechDhcpv6ServerHCountInPkts_Object=MibScalar
qtechDhcpv6ServerHCountInPkts=_QtechDhcpv6ServerHCountInPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,1,12),_QtechDhcpv6ServerHCountInPkts_Type())
qtechDhcpv6ServerHCountInPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerHCountInPkts.setStatus(_A)
_QtechDhcpv6ServerHCountOutPkts_Type=Counter64
_QtechDhcpv6ServerHCountOutPkts_Object=MibScalar
qtechDhcpv6ServerHCountOutPkts=_QtechDhcpv6ServerHCountOutPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,1,13),_QtechDhcpv6ServerHCountOutPkts_Type())
qtechDhcpv6ServerHCountOutPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerHCountOutPkts.setStatus(_A)
_QtechDhcpv6ServerHCountDroppedUnknown_Type=Counter64
_QtechDhcpv6ServerHCountDroppedUnknown_Object=MibScalar
qtechDhcpv6ServerHCountDroppedUnknown=_QtechDhcpv6ServerHCountDroppedUnknown_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,1,14),_QtechDhcpv6ServerHCountDroppedUnknown_Type())
qtechDhcpv6ServerHCountDroppedUnknown.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerHCountDroppedUnknown.setStatus(_A)
_QtechDhcpv6ServerHCountDroppedError_Type=Counter64
_QtechDhcpv6ServerHCountDroppedError_Object=MibScalar
qtechDhcpv6ServerHCountDroppedError=_QtechDhcpv6ServerHCountDroppedError_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,1,15),_QtechDhcpv6ServerHCountDroppedError_Type())
qtechDhcpv6ServerHCountDroppedError.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerHCountDroppedError.setStatus(_A)
_QtechDhcpv6ServerHCountRelayforward_Type=Counter64
_QtechDhcpv6ServerHCountRelayforward_Object=MibScalar
qtechDhcpv6ServerHCountRelayforward=_QtechDhcpv6ServerHCountRelayforward_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,1,16),_QtechDhcpv6ServerHCountRelayforward_Type())
qtechDhcpv6ServerHCountRelayforward.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerHCountRelayforward.setStatus(_A)
_QtechDhcpv6ServerHCountRelayreply_Type=Counter64
_QtechDhcpv6ServerHCountRelayreply_Object=MibScalar
qtechDhcpv6ServerHCountRelayreply=_QtechDhcpv6ServerHCountRelayreply_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,1,17),_QtechDhcpv6ServerHCountRelayreply_Type())
qtechDhcpv6ServerHCountRelayreply.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerHCountRelayreply.setStatus(_A)
_QtechDhcpv6ServerHCountReqtimes_Type=Counter64
_QtechDhcpv6ServerHCountReqtimes_Object=MibScalar
qtechDhcpv6ServerHCountReqtimes=_QtechDhcpv6ServerHCountReqtimes_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,1,18),_QtechDhcpv6ServerHCountReqtimes_Type())
qtechDhcpv6ServerHCountReqtimes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerHCountReqtimes.setStatus(_A)
_QtechDhcpv6ServerHCountReqSuctimes_Type=Counter64
_QtechDhcpv6ServerHCountReqSuctimes_Object=MibScalar
qtechDhcpv6ServerHCountReqSuctimes=_QtechDhcpv6ServerHCountReqSuctimes_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,1,19),_QtechDhcpv6ServerHCountReqSuctimes_Type())
qtechDhcpv6ServerHCountReqSuctimes.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerHCountReqSuctimes.setStatus(_A)
_QtechDhcpv6ServerConfiguration_ObjectIdentity=ObjectIdentity
qtechDhcpv6ServerConfiguration=_QtechDhcpv6ServerConfiguration_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,2))
if mibBuilder.loadTexts:qtechDhcpv6ServerConfiguration.setStatus(_A)
_QtechDhcpv6ServerNumBindings_Type=Counter32
_QtechDhcpv6ServerNumBindings_Object=MibScalar
qtechDhcpv6ServerNumBindings=_QtechDhcpv6ServerNumBindings_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,2,1),_QtechDhcpv6ServerNumBindings_Type())
qtechDhcpv6ServerNumBindings.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerNumBindings.setStatus(_A)
_QtechDhcpv6ServerBindingsTable_Object=MibTable
qtechDhcpv6ServerBindingsTable=_QtechDhcpv6ServerBindingsTable_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,2,2))
if mibBuilder.loadTexts:qtechDhcpv6ServerBindingsTable.setStatus(_A)
_QtechDhcpv6ServerBindingsEntry_Object=MibTableRow
qtechDhcpv6ServerBindingsEntry=_QtechDhcpv6ServerBindingsEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,2,2,1))
qtechDhcpv6ServerBindingsEntry.setIndexNames((0,_B,_F),(0,_B,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:qtechDhcpv6ServerBindingsEntry.setStatus(_A)
class _QtechDhcpv6ServerBindingsPoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechDhcpv6ServerBindingsPoolName_Type.__name__=_E
_QtechDhcpv6ServerBindingsPoolName_Object=MibTableColumn
qtechDhcpv6ServerBindingsPoolName=_QtechDhcpv6ServerBindingsPoolName_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,2,2,1,1),_QtechDhcpv6ServerBindingsPoolName_Type())
qtechDhcpv6ServerBindingsPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerBindingsPoolName.setStatus(_A)
class _QtechDhcpv6ServerBindingsClientDuid_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,130))
_QtechDhcpv6ServerBindingsClientDuid_Type.__name__=_K
_QtechDhcpv6ServerBindingsClientDuid_Object=MibTableColumn
qtechDhcpv6ServerBindingsClientDuid=_QtechDhcpv6ServerBindingsClientDuid_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,2,2,1,2),_QtechDhcpv6ServerBindingsClientDuid_Type())
qtechDhcpv6ServerBindingsClientDuid.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerBindingsClientDuid.setStatus(_A)
class _QtechDhcpv6ServerBindingsIaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('iana',1),('iata',2),('iapd',3)))
_QtechDhcpv6ServerBindingsIaType_Type.__name__=_D
_QtechDhcpv6ServerBindingsIaType_Object=MibTableColumn
qtechDhcpv6ServerBindingsIaType=_QtechDhcpv6ServerBindingsIaType_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,2,2,1,3),_QtechDhcpv6ServerBindingsIaType_Type())
qtechDhcpv6ServerBindingsIaType.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerBindingsIaType.setStatus(_A)
_QtechDhcpv6ServerBindingsIaId_Type=Unsigned32
_QtechDhcpv6ServerBindingsIaId_Object=MibTableColumn
qtechDhcpv6ServerBindingsIaId=_QtechDhcpv6ServerBindingsIaId_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,2,2,1,4),_QtechDhcpv6ServerBindingsIaId_Type())
qtechDhcpv6ServerBindingsIaId.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerBindingsIaId.setStatus(_A)
_QtechDhcpv6ServerBindingsAddress_Type=Ipv6Address
_QtechDhcpv6ServerBindingsAddress_Object=MibTableColumn
qtechDhcpv6ServerBindingsAddress=_QtechDhcpv6ServerBindingsAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,2,2,1,5),_QtechDhcpv6ServerBindingsAddress_Type())
qtechDhcpv6ServerBindingsAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerBindingsAddress.setStatus(_A)
_QtechDhcpv6ServerBindingsPrefix_Type=Ipv6AddressPrefix
_QtechDhcpv6ServerBindingsPrefix_Object=MibTableColumn
qtechDhcpv6ServerBindingsPrefix=_QtechDhcpv6ServerBindingsPrefix_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,2,2,1,6),_QtechDhcpv6ServerBindingsPrefix_Type())
qtechDhcpv6ServerBindingsPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerBindingsPrefix.setStatus(_A)
class _QtechDhcpv6ServerBindingsPrefixLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,128))
_QtechDhcpv6ServerBindingsPrefixLength_Type.__name__=_D
_QtechDhcpv6ServerBindingsPrefixLength_Object=MibTableColumn
qtechDhcpv6ServerBindingsPrefixLength=_QtechDhcpv6ServerBindingsPrefixLength_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,2,2,1,7),_QtechDhcpv6ServerBindingsPrefixLength_Type())
qtechDhcpv6ServerBindingsPrefixLength.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerBindingsPrefixLength.setStatus(_A)
_QtechDhcpv6ServerBindingsDuration_Type=Unsigned32
_QtechDhcpv6ServerBindingsDuration_Object=MibTableColumn
qtechDhcpv6ServerBindingsDuration=_QtechDhcpv6ServerBindingsDuration_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,2,2,1,8),_QtechDhcpv6ServerBindingsDuration_Type())
qtechDhcpv6ServerBindingsDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerBindingsDuration.setStatus(_A)
_QtechDhcpv6ServerBindingsIfIndex_Type=InterfaceIndex
_QtechDhcpv6ServerBindingsIfIndex_Object=MibTableColumn
qtechDhcpv6ServerBindingsIfIndex=_QtechDhcpv6ServerBindingsIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,2,2,1,9),_QtechDhcpv6ServerBindingsIfIndex_Type())
qtechDhcpv6ServerBindingsIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerBindingsIfIndex.setStatus(_A)
_QtechDhcpv6ServerPoolTable_Object=MibTable
qtechDhcpv6ServerPoolTable=_QtechDhcpv6ServerPoolTable_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,2,3))
if mibBuilder.loadTexts:qtechDhcpv6ServerPoolTable.setStatus(_A)
_QtechDhcpv6ServerPoolEntry_Object=MibTableRow
qtechDhcpv6ServerPoolEntry=_QtechDhcpv6ServerPoolEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,2,3,1))
qtechDhcpv6ServerPoolEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:qtechDhcpv6ServerPoolEntry.setStatus(_A)
class _QtechDhcpv6ServerIPPoolName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechDhcpv6ServerIPPoolName_Type.__name__=_E
_QtechDhcpv6ServerIPPoolName_Object=MibTableColumn
qtechDhcpv6ServerIPPoolName=_QtechDhcpv6ServerIPPoolName_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,2,3,1,1),_QtechDhcpv6ServerIPPoolName_Type())
qtechDhcpv6ServerIPPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerIPPoolName.setStatus(_A)
_QtechDhcpv6ServerDHCPIPPoolUsage_Type=Unsigned32
_QtechDhcpv6ServerDHCPIPPoolUsage_Object=MibTableColumn
qtechDhcpv6ServerDHCPIPPoolUsage=_QtechDhcpv6ServerDHCPIPPoolUsage_Object((1,3,6,1,4,1,27514,1,1,10,2,45,1,1,2,3,1,2),_QtechDhcpv6ServerDHCPIPPoolUsage_Type())
qtechDhcpv6ServerDHCPIPPoolUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpv6ServerDHCPIPPoolUsage.setStatus(_A)
_QtechDhcpv6MIBConformance_ObjectIdentity=ObjectIdentity
qtechDhcpv6MIBConformance=_QtechDhcpv6MIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,45,2))
if mibBuilder.loadTexts:qtechDhcpv6MIBConformance.setStatus(_A)
_QtechDhcpv6MIBCompliances_ObjectIdentity=ObjectIdentity
qtechDhcpv6MIBCompliances=_QtechDhcpv6MIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,45,2,1))
_QtechDhcpv6MIBGroups_ObjectIdentity=ObjectIdentity
qtechDhcpv6MIBGroups=_QtechDhcpv6MIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,45,2,2))
qtechDhcpv6ServerCountersObjects=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,45,2,2,1))
qtechDhcpv6ServerCountersObjects.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c)))
if mibBuilder.loadTexts:qtechDhcpv6ServerCountersObjects.setStatus(_A)
qtechDhcpv6ServerConfigurationObjects=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,45,2,2,2))
qtechDhcpv6ServerConfigurationObjects.setObjects(*((_B,_d),(_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:qtechDhcpv6ServerConfigurationObjects.setStatus(_A)
qtechDhcpv6ServerPoolTableObjects=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,45,2,2,3))
qtechDhcpv6ServerPoolTableObjects.setObjects(*((_B,_J),(_B,_j)))
if mibBuilder.loadTexts:qtechDhcpv6ServerPoolTableObjects.setStatus(_A)
qtechDhcpv6ServerCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,45,2,1,1))
qtechDhcpv6ServerCompliance.setObjects(*((_B,_k),(_B,_l)))
if mibBuilder.loadTexts:qtechDhcpv6ServerCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechDhcpv6MIB':qtechDhcpv6MIB,'qtechDhcpv6MIBObjects':qtechDhcpv6MIBObjects,'qtechDhcpv6ServerMIBObjects':qtechDhcpv6ServerMIBObjects,'qtechDhcpv6ServerCounters':qtechDhcpv6ServerCounters,_L:qtechDhcpv6ServerHCountSolicits,'qtechDhcpv6ServerHCountRequests':qtechDhcpv6ServerHCountRequests,_M:qtechDhcpv6ServerHCountRenews,_N:qtechDhcpv6ServerHCountDeclines,_O:qtechDhcpv6ServerHCountReleases,_P:qtechDhcpv6ServerHCountInforms,_Q:qtechDhcpv6ServerHCountConfirms,_R:qtechDhcpv6ServerHCountRebinds,_S:qtechDhcpv6ServerHCountAdvertises,_T:qtechDhcpv6ServerHCountSuccReplies,_U:qtechDhcpv6ServerHCountFailReplies,_V:qtechDhcpv6ServerHCountInPkts,_W:qtechDhcpv6ServerHCountOutPkts,_X:qtechDhcpv6ServerHCountDroppedUnknown,_Y:qtechDhcpv6ServerHCountDroppedError,_Z:qtechDhcpv6ServerHCountRelayforward,_a:qtechDhcpv6ServerHCountRelayreply,_b:qtechDhcpv6ServerHCountReqtimes,_c:qtechDhcpv6ServerHCountReqSuctimes,'qtechDhcpv6ServerConfiguration':qtechDhcpv6ServerConfiguration,_d:qtechDhcpv6ServerNumBindings,'qtechDhcpv6ServerBindingsTable':qtechDhcpv6ServerBindingsTable,'qtechDhcpv6ServerBindingsEntry':qtechDhcpv6ServerBindingsEntry,_F:qtechDhcpv6ServerBindingsPoolName,_G:qtechDhcpv6ServerBindingsClientDuid,_H:qtechDhcpv6ServerBindingsIaType,_I:qtechDhcpv6ServerBindingsIaId,_e:qtechDhcpv6ServerBindingsAddress,_f:qtechDhcpv6ServerBindingsPrefix,_g:qtechDhcpv6ServerBindingsPrefixLength,_h:qtechDhcpv6ServerBindingsDuration,_i:qtechDhcpv6ServerBindingsIfIndex,'qtechDhcpv6ServerPoolTable':qtechDhcpv6ServerPoolTable,'qtechDhcpv6ServerPoolEntry':qtechDhcpv6ServerPoolEntry,_J:qtechDhcpv6ServerIPPoolName,_j:qtechDhcpv6ServerDHCPIPPoolUsage,'qtechDhcpv6MIBConformance':qtechDhcpv6MIBConformance,'qtechDhcpv6MIBCompliances':qtechDhcpv6MIBCompliances,'qtechDhcpv6ServerCompliance':qtechDhcpv6ServerCompliance,'qtechDhcpv6MIBGroups':qtechDhcpv6MIBGroups,_k:qtechDhcpv6ServerCountersObjects,_l:qtechDhcpv6ServerConfigurationObjects,'qtechDhcpv6ServerPoolTableObjects':qtechDhcpv6ServerPoolTableObjects})