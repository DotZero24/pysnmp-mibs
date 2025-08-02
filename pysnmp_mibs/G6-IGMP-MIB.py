_L='mldStatusIndex'
_K='statusIndex'
_J='staticMulticastGroupsIndex'
_I='configIndex'
_H='not-accessible'
_G='G6-IGMP-MIB'
_F='enabled'
_E='disabled'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
protocol=ModuleIdentity((1,3,6,1,4,1,3181,10,6,2))
if mibBuilder.loadTexts:protocol.setRevisions(('2018-02-12 16:19',))
_Igmp_ObjectIdentity=ObjectIdentity
igmp=_Igmp_ObjectIdentity((1,3,6,1,4,1,3181,10,6,2,40))
class _IgmpEnableIgmpSnooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_IgmpEnableIgmpSnooping_Type.__name__=_C
_IgmpEnableIgmpSnooping_Object=MibScalar
igmpEnableIgmpSnooping=_IgmpEnableIgmpSnooping_Object((1,3,6,1,4,1,3181,10,6,2,40,1),_IgmpEnableIgmpSnooping_Type())
igmpEnableIgmpSnooping.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpEnableIgmpSnooping.setStatus(_A)
class _IgmpEnableMldSnooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_IgmpEnableMldSnooping_Type.__name__=_C
_IgmpEnableMldSnooping_Object=MibScalar
igmpEnableMldSnooping=_IgmpEnableMldSnooping_Object((1,3,6,1,4,1,3181,10,6,2,40,2),_IgmpEnableMldSnooping_Type())
igmpEnableMldSnooping.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpEnableMldSnooping.setStatus(_A)
_IgmpShowMulticastForVlan_Type=DisplayString
_IgmpShowMulticastForVlan_Object=MibScalar
igmpShowMulticastForVlan=_IgmpShowMulticastForVlan_Object((1,3,6,1,4,1,3181,10,6,2,40,3),_IgmpShowMulticastForVlan_Type())
igmpShowMulticastForVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpShowMulticastForVlan.setStatus(_A)
_IgmpShowMulticastForPort_Type=DisplayString
_IgmpShowMulticastForPort_Object=MibScalar
igmpShowMulticastForPort=_IgmpShowMulticastForPort_Object((1,3,6,1,4,1,3181,10,6,2,40,4),_IgmpShowMulticastForPort_Type())
igmpShowMulticastForPort.setMaxAccess(_B)
if mibBuilder.loadTexts:igmpShowMulticastForPort.setStatus(_A)
_ConfigTable_Object=MibTable
configTable=_ConfigTable_Object((1,3,6,1,4,1,3181,10,6,2,40,5))
if mibBuilder.loadTexts:configTable.setStatus(_A)
_ConfigEntry_Object=MibTableRow
configEntry=_ConfigEntry_Object((1,3,6,1,4,1,3181,10,6,2,40,5,1))
configEntry.setIndexNames((0,_G,_I))
if mibBuilder.loadTexts:configEntry.setStatus(_A)
class _ConfigIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_ConfigIndex_Type.__name__=_C
_ConfigIndex_Object=MibTableColumn
configIndex=_ConfigIndex_Object((1,3,6,1,4,1,3181,10,6,2,40,5,1,1),_ConfigIndex_Type())
configIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:configIndex.setStatus(_A)
_ConfigVlanId_Type=DisplayString
_ConfigVlanId_Object=MibTableColumn
configVlanId=_ConfigVlanId_Object((1,3,6,1,4,1,3181,10,6,2,40,5,1,2),_ConfigVlanId_Type())
configVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:configVlanId.setStatus(_A)
class _ConfigEnableIgmpSnooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ConfigEnableIgmpSnooping_Type.__name__=_C
_ConfigEnableIgmpSnooping_Object=MibTableColumn
configEnableIgmpSnooping=_ConfigEnableIgmpSnooping_Object((1,3,6,1,4,1,3181,10,6,2,40,5,1,3),_ConfigEnableIgmpSnooping_Type())
configEnableIgmpSnooping.setMaxAccess(_B)
if mibBuilder.loadTexts:configEnableIgmpSnooping.setStatus(_A)
class _ConfigEnableMldSnooping_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ConfigEnableMldSnooping_Type.__name__=_C
_ConfigEnableMldSnooping_Object=MibTableColumn
configEnableMldSnooping=_ConfigEnableMldSnooping_Object((1,3,6,1,4,1,3181,10,6,2,40,5,1,4),_ConfigEnableMldSnooping_Type())
configEnableMldSnooping.setMaxAccess(_B)
if mibBuilder.loadTexts:configEnableMldSnooping.setStatus(_A)
_ConfigSnoopingPorts_Type=Integer32
_ConfigSnoopingPorts_Object=MibTableColumn
configSnoopingPorts=_ConfigSnoopingPorts_Object((1,3,6,1,4,1,3181,10,6,2,40,5,1,5),_ConfigSnoopingPorts_Type())
configSnoopingPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:configSnoopingPorts.setStatus(_A)
_ConfigStaticRouterPorts_Type=Integer32
_ConfigStaticRouterPorts_Object=MibTableColumn
configStaticRouterPorts=_ConfigStaticRouterPorts_Object((1,3,6,1,4,1,3181,10,6,2,40,5,1,6),_ConfigStaticRouterPorts_Type())
configStaticRouterPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:configStaticRouterPorts.setStatus(_A)
class _ConfigMulticastRouterDetection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('routerDiscovery',0),('queryMessage',1)))
_ConfigMulticastRouterDetection_Type.__name__=_C
_ConfigMulticastRouterDetection_Object=MibTableColumn
configMulticastRouterDetection=_ConfigMulticastRouterDetection_Object((1,3,6,1,4,1,3181,10,6,2,40,5,1,7),_ConfigMulticastRouterDetection_Type())
configMulticastRouterDetection.setMaxAccess(_B)
if mibBuilder.loadTexts:configMulticastRouterDetection.setStatus(_A)
class _ConfigEnableReportAggregation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ConfigEnableReportAggregation_Type.__name__=_C
_ConfigEnableReportAggregation_Object=MibTableColumn
configEnableReportAggregation=_ConfigEnableReportAggregation_Object((1,3,6,1,4,1,3181,10,6,2,40,5,1,8),_ConfigEnableReportAggregation_Type())
configEnableReportAggregation.setMaxAccess(_B)
if mibBuilder.loadTexts:configEnableReportAggregation.setStatus(_A)
class _ConfigEnableFloodingUnregisterPkt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ConfigEnableFloodingUnregisterPkt_Type.__name__=_C
_ConfigEnableFloodingUnregisterPkt_Object=MibTableColumn
configEnableFloodingUnregisterPkt=_ConfigEnableFloodingUnregisterPkt_Object((1,3,6,1,4,1,3181,10,6,2,40,5,1,9),_ConfigEnableFloodingUnregisterPkt_Type())
configEnableFloodingUnregisterPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:configEnableFloodingUnregisterPkt.setStatus(_A)
class _ConfigMcastGroupLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ConfigMcastGroupLimit_Type.__name__=_C
_ConfigMcastGroupLimit_Object=MibTableColumn
configMcastGroupLimit=_ConfigMcastGroupLimit_Object((1,3,6,1,4,1,3181,10,6,2,40,5,1,10),_ConfigMcastGroupLimit_Type())
configMcastGroupLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:configMcastGroupLimit.setStatus(_A)
class _ConfigGroupMembershipInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ConfigGroupMembershipInterval_Type.__name__=_C
_ConfigGroupMembershipInterval_Object=MibTableColumn
configGroupMembershipInterval=_ConfigGroupMembershipInterval_Object((1,3,6,1,4,1,3181,10,6,2,40,5,1,11),_ConfigGroupMembershipInterval_Type())
configGroupMembershipInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:configGroupMembershipInterval.setStatus(_A)
class _ConfigMaxResponseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ConfigMaxResponseTime_Type.__name__=_C
_ConfigMaxResponseTime_Object=MibTableColumn
configMaxResponseTime=_ConfigMaxResponseTime_Object((1,3,6,1,4,1,3181,10,6,2,40,5,1,12),_ConfigMaxResponseTime_Type())
configMaxResponseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:configMaxResponseTime.setStatus(_A)
class _ConfigEnableFastLeave_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_ConfigEnableFastLeave_Type.__name__=_C
_ConfigEnableFastLeave_Object=MibTableColumn
configEnableFastLeave=_ConfigEnableFastLeave_Object((1,3,6,1,4,1,3181,10,6,2,40,5,1,13),_ConfigEnableFastLeave_Type())
configEnableFastLeave.setMaxAccess(_B)
if mibBuilder.loadTexts:configEnableFastLeave.setStatus(_A)
class _ConfigLastMemberQueryTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ConfigLastMemberQueryTime_Type.__name__=_C
_ConfigLastMemberQueryTime_Object=MibTableColumn
configLastMemberQueryTime=_ConfigLastMemberQueryTime_Object((1,3,6,1,4,1,3181,10,6,2,40,5,1,14),_ConfigLastMemberQueryTime_Type())
configLastMemberQueryTime.setMaxAccess(_B)
if mibBuilder.loadTexts:configLastMemberQueryTime.setStatus(_A)
class _ConfigNeighborDeadInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ConfigNeighborDeadInterval_Type.__name__=_C
_ConfigNeighborDeadInterval_Object=MibTableColumn
configNeighborDeadInterval=_ConfigNeighborDeadInterval_Object((1,3,6,1,4,1,3181,10,6,2,40,5,1,15),_ConfigNeighborDeadInterval_Type())
configNeighborDeadInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:configNeighborDeadInterval.setStatus(_A)
class _ConfigRouterAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_ConfigRouterAgingTime_Type.__name__=_C
_ConfigRouterAgingTime_Object=MibTableColumn
configRouterAgingTime=_ConfigRouterAgingTime_Object((1,3,6,1,4,1,3181,10,6,2,40,5,1,16),_ConfigRouterAgingTime_Type())
configRouterAgingTime.setMaxAccess(_B)
if mibBuilder.loadTexts:configRouterAgingTime.setStatus(_A)
_StaticMulticastGroupsTable_Object=MibTable
staticMulticastGroupsTable=_StaticMulticastGroupsTable_Object((1,3,6,1,4,1,3181,10,6,2,40,6))
if mibBuilder.loadTexts:staticMulticastGroupsTable.setStatus(_A)
_StaticMulticastGroupsEntry_Object=MibTableRow
staticMulticastGroupsEntry=_StaticMulticastGroupsEntry_Object((1,3,6,1,4,1,3181,10,6,2,40,6,1))
staticMulticastGroupsEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:staticMulticastGroupsEntry.setStatus(_A)
class _StaticMulticastGroupsIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_StaticMulticastGroupsIndex_Type.__name__=_C
_StaticMulticastGroupsIndex_Object=MibTableColumn
staticMulticastGroupsIndex=_StaticMulticastGroupsIndex_Object((1,3,6,1,4,1,3181,10,6,2,40,6,1,1),_StaticMulticastGroupsIndex_Type())
staticMulticastGroupsIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:staticMulticastGroupsIndex.setStatus(_A)
_StaticMulticastGroupsName_Type=DisplayString
_StaticMulticastGroupsName_Object=MibTableColumn
staticMulticastGroupsName=_StaticMulticastGroupsName_Object((1,3,6,1,4,1,3181,10,6,2,40,6,1,2),_StaticMulticastGroupsName_Type())
staticMulticastGroupsName.setMaxAccess(_B)
if mibBuilder.loadTexts:staticMulticastGroupsName.setStatus(_A)
_StaticMulticastGroupsDescription_Type=DisplayString
_StaticMulticastGroupsDescription_Object=MibTableColumn
staticMulticastGroupsDescription=_StaticMulticastGroupsDescription_Object((1,3,6,1,4,1,3181,10,6,2,40,6,1,3),_StaticMulticastGroupsDescription_Type())
staticMulticastGroupsDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:staticMulticastGroupsDescription.setStatus(_A)
_StaticMulticastGroupsMulticastMac_Type=MacAddress
_StaticMulticastGroupsMulticastMac_Object=MibTableColumn
staticMulticastGroupsMulticastMac=_StaticMulticastGroupsMulticastMac_Object((1,3,6,1,4,1,3181,10,6,2,40,6,1,4),_StaticMulticastGroupsMulticastMac_Type())
staticMulticastGroupsMulticastMac.setMaxAccess(_B)
if mibBuilder.loadTexts:staticMulticastGroupsMulticastMac.setStatus(_A)
_StaticMulticastGroupsForwardingPortMask_Type=Integer32
_StaticMulticastGroupsForwardingPortMask_Object=MibTableColumn
staticMulticastGroupsForwardingPortMask=_StaticMulticastGroupsForwardingPortMask_Object((1,3,6,1,4,1,3181,10,6,2,40,6,1,5),_StaticMulticastGroupsForwardingPortMask_Type())
staticMulticastGroupsForwardingPortMask.setMaxAccess(_B)
if mibBuilder.loadTexts:staticMulticastGroupsForwardingPortMask.setStatus(_A)
class _StaticMulticastGroupsVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_StaticMulticastGroupsVlanId_Type.__name__=_C
_StaticMulticastGroupsVlanId_Object=MibTableColumn
staticMulticastGroupsVlanId=_StaticMulticastGroupsVlanId_Object((1,3,6,1,4,1,3181,10,6,2,40,6,1,6),_StaticMulticastGroupsVlanId_Type())
staticMulticastGroupsVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:staticMulticastGroupsVlanId.setStatus(_A)
_StatusTable_Object=MibTable
statusTable=_StatusTable_Object((1,3,6,1,4,1,3181,10,6,2,40,100))
if mibBuilder.loadTexts:statusTable.setStatus(_A)
_StatusEntry_Object=MibTableRow
statusEntry=_StatusEntry_Object((1,3,6,1,4,1,3181,10,6,2,40,100,1))
statusEntry.setIndexNames((0,_G,_K))
if mibBuilder.loadTexts:statusEntry.setStatus(_A)
class _StatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_StatusIndex_Type.__name__=_C
_StatusIndex_Object=MibTableColumn
statusIndex=_StatusIndex_Object((1,3,6,1,4,1,3181,10,6,2,40,100,1,1),_StatusIndex_Type())
statusIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:statusIndex.setStatus(_A)
_StatusIgmpRouterPorts_Type=Integer32
_StatusIgmpRouterPorts_Object=MibTableColumn
statusIgmpRouterPorts=_StatusIgmpRouterPorts_Object((1,3,6,1,4,1,3181,10,6,2,40,100,1,2),_StatusIgmpRouterPorts_Type())
statusIgmpRouterPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:statusIgmpRouterPorts.setStatus(_A)
_StatusRxGeneralQueries_Type=Unsigned32
_StatusRxGeneralQueries_Object=MibTableColumn
statusRxGeneralQueries=_StatusRxGeneralQueries_Object((1,3,6,1,4,1,3181,10,6,2,40,100,1,3),_StatusRxGeneralQueries_Type())
statusRxGeneralQueries.setMaxAccess(_D)
if mibBuilder.loadTexts:statusRxGeneralQueries.setStatus(_A)
_StatusRxGroupQueries_Type=Unsigned32
_StatusRxGroupQueries_Object=MibTableColumn
statusRxGroupQueries=_StatusRxGroupQueries_Object((1,3,6,1,4,1,3181,10,6,2,40,100,1,4),_StatusRxGroupQueries_Type())
statusRxGroupQueries.setMaxAccess(_D)
if mibBuilder.loadTexts:statusRxGroupQueries.setStatus(_A)
_StatusRxReports_Type=Unsigned32
_StatusRxReports_Object=MibTableColumn
statusRxReports=_StatusRxReports_Object((1,3,6,1,4,1,3181,10,6,2,40,100,1,5),_StatusRxReports_Type())
statusRxReports.setMaxAccess(_D)
if mibBuilder.loadTexts:statusRxReports.setStatus(_A)
_StatusRxLeaves_Type=Unsigned32
_StatusRxLeaves_Object=MibTableColumn
statusRxLeaves=_StatusRxLeaves_Object((1,3,6,1,4,1,3181,10,6,2,40,100,1,6),_StatusRxLeaves_Type())
statusRxLeaves.setMaxAccess(_D)
if mibBuilder.loadTexts:statusRxLeaves.setStatus(_A)
_StatusRxAdvertisements_Type=Unsigned32
_StatusRxAdvertisements_Object=MibTableColumn
statusRxAdvertisements=_StatusRxAdvertisements_Object((1,3,6,1,4,1,3181,10,6,2,40,100,1,7),_StatusRxAdvertisements_Type())
statusRxAdvertisements.setMaxAccess(_D)
if mibBuilder.loadTexts:statusRxAdvertisements.setStatus(_A)
_StatusRxTerminations_Type=Unsigned32
_StatusRxTerminations_Object=MibTableColumn
statusRxTerminations=_StatusRxTerminations_Object((1,3,6,1,4,1,3181,10,6,2,40,100,1,8),_StatusRxTerminations_Type())
statusRxTerminations.setMaxAccess(_D)
if mibBuilder.loadTexts:statusRxTerminations.setStatus(_A)
_StatusRxUnsupported_Type=Unsigned32
_StatusRxUnsupported_Object=MibTableColumn
statusRxUnsupported=_StatusRxUnsupported_Object((1,3,6,1,4,1,3181,10,6,2,40,100,1,9),_StatusRxUnsupported_Type())
statusRxUnsupported.setMaxAccess(_D)
if mibBuilder.loadTexts:statusRxUnsupported.setStatus(_A)
_StatusRxErrors_Type=Unsigned32
_StatusRxErrors_Object=MibTableColumn
statusRxErrors=_StatusRxErrors_Object((1,3,6,1,4,1,3181,10,6,2,40,100,1,10),_StatusRxErrors_Type())
statusRxErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:statusRxErrors.setStatus(_A)
_StatusTxSolicitations_Type=Unsigned32
_StatusTxSolicitations_Object=MibTableColumn
statusTxSolicitations=_StatusTxSolicitations_Object((1,3,6,1,4,1,3181,10,6,2,40,100,1,11),_StatusTxSolicitations_Type())
statusTxSolicitations.setMaxAccess(_D)
if mibBuilder.loadTexts:statusTxSolicitations.setStatus(_A)
_MldStatusTable_Object=MibTable
mldStatusTable=_MldStatusTable_Object((1,3,6,1,4,1,3181,10,6,2,40,101))
if mibBuilder.loadTexts:mldStatusTable.setStatus(_A)
_MldStatusEntry_Object=MibTableRow
mldStatusEntry=_MldStatusEntry_Object((1,3,6,1,4,1,3181,10,6,2,40,101,1))
mldStatusEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:mldStatusEntry.setStatus(_A)
class _MldStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0))
_MldStatusIndex_Type.__name__=_C
_MldStatusIndex_Object=MibTableColumn
mldStatusIndex=_MldStatusIndex_Object((1,3,6,1,4,1,3181,10,6,2,40,101,1,1),_MldStatusIndex_Type())
mldStatusIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:mldStatusIndex.setStatus(_A)
_MldStatusMldRouterPorts_Type=Integer32
_MldStatusMldRouterPorts_Object=MibTableColumn
mldStatusMldRouterPorts=_MldStatusMldRouterPorts_Object((1,3,6,1,4,1,3181,10,6,2,40,101,1,2),_MldStatusMldRouterPorts_Type())
mldStatusMldRouterPorts.setMaxAccess(_D)
if mibBuilder.loadTexts:mldStatusMldRouterPorts.setStatus(_A)
_MldStatusRxGeneralQueries_Type=Unsigned32
_MldStatusRxGeneralQueries_Object=MibTableColumn
mldStatusRxGeneralQueries=_MldStatusRxGeneralQueries_Object((1,3,6,1,4,1,3181,10,6,2,40,101,1,3),_MldStatusRxGeneralQueries_Type())
mldStatusRxGeneralQueries.setMaxAccess(_D)
if mibBuilder.loadTexts:mldStatusRxGeneralQueries.setStatus(_A)
_MldStatusRxGroupQueries_Type=Unsigned32
_MldStatusRxGroupQueries_Object=MibTableColumn
mldStatusRxGroupQueries=_MldStatusRxGroupQueries_Object((1,3,6,1,4,1,3181,10,6,2,40,101,1,4),_MldStatusRxGroupQueries_Type())
mldStatusRxGroupQueries.setMaxAccess(_D)
if mibBuilder.loadTexts:mldStatusRxGroupQueries.setStatus(_A)
_MldStatusRxReports_Type=Unsigned32
_MldStatusRxReports_Object=MibTableColumn
mldStatusRxReports=_MldStatusRxReports_Object((1,3,6,1,4,1,3181,10,6,2,40,101,1,5),_MldStatusRxReports_Type())
mldStatusRxReports.setMaxAccess(_D)
if mibBuilder.loadTexts:mldStatusRxReports.setStatus(_A)
_MldStatusRxLeaves_Type=Unsigned32
_MldStatusRxLeaves_Object=MibTableColumn
mldStatusRxLeaves=_MldStatusRxLeaves_Object((1,3,6,1,4,1,3181,10,6,2,40,101,1,6),_MldStatusRxLeaves_Type())
mldStatusRxLeaves.setMaxAccess(_D)
if mibBuilder.loadTexts:mldStatusRxLeaves.setStatus(_A)
_MldStatusRxAdvertisements_Type=Unsigned32
_MldStatusRxAdvertisements_Object=MibTableColumn
mldStatusRxAdvertisements=_MldStatusRxAdvertisements_Object((1,3,6,1,4,1,3181,10,6,2,40,101,1,7),_MldStatusRxAdvertisements_Type())
mldStatusRxAdvertisements.setMaxAccess(_D)
if mibBuilder.loadTexts:mldStatusRxAdvertisements.setStatus(_A)
_MldStatusRxTerminations_Type=Unsigned32
_MldStatusRxTerminations_Object=MibTableColumn
mldStatusRxTerminations=_MldStatusRxTerminations_Object((1,3,6,1,4,1,3181,10,6,2,40,101,1,8),_MldStatusRxTerminations_Type())
mldStatusRxTerminations.setMaxAccess(_D)
if mibBuilder.loadTexts:mldStatusRxTerminations.setStatus(_A)
_MldStatusRxUnsupported_Type=Unsigned32
_MldStatusRxUnsupported_Object=MibTableColumn
mldStatusRxUnsupported=_MldStatusRxUnsupported_Object((1,3,6,1,4,1,3181,10,6,2,40,101,1,9),_MldStatusRxUnsupported_Type())
mldStatusRxUnsupported.setMaxAccess(_D)
if mibBuilder.loadTexts:mldStatusRxUnsupported.setStatus(_A)
_MldStatusRxErrors_Type=Unsigned32
_MldStatusRxErrors_Object=MibTableColumn
mldStatusRxErrors=_MldStatusRxErrors_Object((1,3,6,1,4,1,3181,10,6,2,40,101,1,10),_MldStatusRxErrors_Type())
mldStatusRxErrors.setMaxAccess(_D)
if mibBuilder.loadTexts:mldStatusRxErrors.setStatus(_A)
_MldStatusTxSolicitations_Type=Unsigned32
_MldStatusTxSolicitations_Object=MibTableColumn
mldStatusTxSolicitations=_MldStatusTxSolicitations_Object((1,3,6,1,4,1,3181,10,6,2,40,101,1,11),_MldStatusTxSolicitations_Type())
mldStatusTxSolicitations.setMaxAccess(_D)
if mibBuilder.loadTexts:mldStatusTxSolicitations.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'protocol':protocol,'igmp':igmp,'igmpEnableIgmpSnooping':igmpEnableIgmpSnooping,'igmpEnableMldSnooping':igmpEnableMldSnooping,'igmpShowMulticastForVlan':igmpShowMulticastForVlan,'igmpShowMulticastForPort':igmpShowMulticastForPort,'configTable':configTable,'configEntry':configEntry,_I:configIndex,'configVlanId':configVlanId,'configEnableIgmpSnooping':configEnableIgmpSnooping,'configEnableMldSnooping':configEnableMldSnooping,'configSnoopingPorts':configSnoopingPorts,'configStaticRouterPorts':configStaticRouterPorts,'configMulticastRouterDetection':configMulticastRouterDetection,'configEnableReportAggregation':configEnableReportAggregation,'configEnableFloodingUnregisterPkt':configEnableFloodingUnregisterPkt,'configMcastGroupLimit':configMcastGroupLimit,'configGroupMembershipInterval':configGroupMembershipInterval,'configMaxResponseTime':configMaxResponseTime,'configEnableFastLeave':configEnableFastLeave,'configLastMemberQueryTime':configLastMemberQueryTime,'configNeighborDeadInterval':configNeighborDeadInterval,'configRouterAgingTime':configRouterAgingTime,'staticMulticastGroupsTable':staticMulticastGroupsTable,'staticMulticastGroupsEntry':staticMulticastGroupsEntry,_J:staticMulticastGroupsIndex,'staticMulticastGroupsName':staticMulticastGroupsName,'staticMulticastGroupsDescription':staticMulticastGroupsDescription,'staticMulticastGroupsMulticastMac':staticMulticastGroupsMulticastMac,'staticMulticastGroupsForwardingPortMask':staticMulticastGroupsForwardingPortMask,'staticMulticastGroupsVlanId':staticMulticastGroupsVlanId,'statusTable':statusTable,'statusEntry':statusEntry,_K:statusIndex,'statusIgmpRouterPorts':statusIgmpRouterPorts,'statusRxGeneralQueries':statusRxGeneralQueries,'statusRxGroupQueries':statusRxGroupQueries,'statusRxReports':statusRxReports,'statusRxLeaves':statusRxLeaves,'statusRxAdvertisements':statusRxAdvertisements,'statusRxTerminations':statusRxTerminations,'statusRxUnsupported':statusRxUnsupported,'statusRxErrors':statusRxErrors,'statusTxSolicitations':statusTxSolicitations,'mldStatusTable':mldStatusTable,'mldStatusEntry':mldStatusEntry,_L:mldStatusIndex,'mldStatusMldRouterPorts':mldStatusMldRouterPorts,'mldStatusRxGeneralQueries':mldStatusRxGeneralQueries,'mldStatusRxGroupQueries':mldStatusRxGroupQueries,'mldStatusRxReports':mldStatusRxReports,'mldStatusRxLeaves':mldStatusRxLeaves,'mldStatusRxAdvertisements':mldStatusRxAdvertisements,'mldStatusRxTerminations':mldStatusRxTerminations,'mldStatusRxUnsupported':mldStatusRxUnsupported,'mldStatusRxErrors':mldStatusRxErrors,'mldStatusTxSolicitations':mldStatusTxSolicitations})