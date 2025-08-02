_J='fsMIDhcpSnpVlanId'
_I='not-accessible'
_H='fsMIDhcpSnpContextId'
_G='Aricent-MI-DHCP-SNOOPING-MIB'
_F='disabled'
_E='enabled'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
fsMIDhcpSnp=ModuleIdentity((1,3,6,1,4,1,29601,2,49))
if mibBuilder.loadTexts:fsMIDhcpSnp.setRevisions(('2012-09-05 00:00',))
_FsMIDhcpSnpGlobalConfig_ObjectIdentity=ObjectIdentity
fsMIDhcpSnpGlobalConfig=_FsMIDhcpSnpGlobalConfig_ObjectIdentity((1,3,6,1,4,1,29601,2,49,1))
_FsMIDhcpSnpGlobalConfigTable_Object=MibTable
fsMIDhcpSnpGlobalConfigTable=_FsMIDhcpSnpGlobalConfigTable_Object((1,3,6,1,4,1,29601,2,49,1,1))
if mibBuilder.loadTexts:fsMIDhcpSnpGlobalConfigTable.setStatus(_A)
_FsMIDhcpSnpGlobalConfigEntry_Object=MibTableRow
fsMIDhcpSnpGlobalConfigEntry=_FsMIDhcpSnpGlobalConfigEntry_Object((1,3,6,1,4,1,29601,2,49,1,1,1))
fsMIDhcpSnpGlobalConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:fsMIDhcpSnpGlobalConfigEntry.setStatus(_A)
class _FsMIDhcpSnpContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIDhcpSnpContextId_Type.__name__=_C
_FsMIDhcpSnpContextId_Object=MibTableColumn
fsMIDhcpSnpContextId=_FsMIDhcpSnpContextId_Object((1,3,6,1,4,1,29601,2,49,1,1,1,1),_FsMIDhcpSnpContextId_Type())
fsMIDhcpSnpContextId.setMaxAccess(_I)
if mibBuilder.loadTexts:fsMIDhcpSnpContextId.setStatus(_A)
class _FsMIDhcpSnpSnoopingAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_FsMIDhcpSnpSnoopingAdminStatus_Type.__name__=_C
_FsMIDhcpSnpSnoopingAdminStatus_Object=MibTableColumn
fsMIDhcpSnpSnoopingAdminStatus=_FsMIDhcpSnpSnoopingAdminStatus_Object((1,3,6,1,4,1,29601,2,49,1,1,1,2),_FsMIDhcpSnpSnoopingAdminStatus_Type())
fsMIDhcpSnpSnoopingAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIDhcpSnpSnoopingAdminStatus.setStatus(_A)
class _FsMIDhcpSnpMacVerifyStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_FsMIDhcpSnpMacVerifyStatus_Type.__name__=_C
_FsMIDhcpSnpMacVerifyStatus_Object=MibTableColumn
fsMIDhcpSnpMacVerifyStatus=_FsMIDhcpSnpMacVerifyStatus_Object((1,3,6,1,4,1,29601,2,49,1,1,1,3),_FsMIDhcpSnpMacVerifyStatus_Type())
fsMIDhcpSnpMacVerifyStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIDhcpSnpMacVerifyStatus.setStatus(_A)
class _FsMIDhcpSnpV6AdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_FsMIDhcpSnpV6AdminStatus_Type.__name__=_C
_FsMIDhcpSnpV6AdminStatus_Object=MibTableColumn
fsMIDhcpSnpV6AdminStatus=_FsMIDhcpSnpV6AdminStatus_Object((1,3,6,1,4,1,29601,2,49,1,1,1,4),_FsMIDhcpSnpV6AdminStatus_Type())
fsMIDhcpSnpV6AdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIDhcpSnpV6AdminStatus.setStatus(_A)
class _FsMIDhcpSnpTraceValue_Type(Integer32):defaultValue=7
_FsMIDhcpSnpTraceValue_Type.__name__=_C
_FsMIDhcpSnpTraceValue_Object=MibTableColumn
fsMIDhcpSnpTraceValue=_FsMIDhcpSnpTraceValue_Object((1,3,6,1,4,1,29601,2,49,1,1,1,5),_FsMIDhcpSnpTraceValue_Type())
fsMIDhcpSnpTraceValue.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIDhcpSnpTraceValue.setStatus(_A)
class _FsMIDhcpSnpV6EnterpriseId_Type(Integer32):defaultValue=3561
_FsMIDhcpSnpV6EnterpriseId_Type.__name__=_C
_FsMIDhcpSnpV6EnterpriseId_Object=MibTableColumn
fsMIDhcpSnpV6EnterpriseId=_FsMIDhcpSnpV6EnterpriseId_Object((1,3,6,1,4,1,29601,2,49,1,1,1,6),_FsMIDhcpSnpV6EnterpriseId_Type())
fsMIDhcpSnpV6EnterpriseId.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIDhcpSnpV6EnterpriseId.setStatus(_A)
_FsMIDhcpSnpInterface_ObjectIdentity=ObjectIdentity
fsMIDhcpSnpInterface=_FsMIDhcpSnpInterface_ObjectIdentity((1,3,6,1,4,1,29601,2,49,2))
_FsMIDhcpSnpInterfaceTable_Object=MibTable
fsMIDhcpSnpInterfaceTable=_FsMIDhcpSnpInterfaceTable_Object((1,3,6,1,4,1,29601,2,49,2,1))
if mibBuilder.loadTexts:fsMIDhcpSnpInterfaceTable.setStatus(_A)
_FsMIDhcpSnpInterfaceEntry_Object=MibTableRow
fsMIDhcpSnpInterfaceEntry=_FsMIDhcpSnpInterfaceEntry_Object((1,3,6,1,4,1,29601,2,49,2,1,1))
fsMIDhcpSnpInterfaceEntry.setIndexNames((0,_G,_H),(0,_G,_J))
if mibBuilder.loadTexts:fsMIDhcpSnpInterfaceEntry.setStatus(_A)
class _FsMIDhcpSnpVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsMIDhcpSnpVlanId_Type.__name__=_C
_FsMIDhcpSnpVlanId_Object=MibTableColumn
fsMIDhcpSnpVlanId=_FsMIDhcpSnpVlanId_Object((1,3,6,1,4,1,29601,2,49,2,1,1,2),_FsMIDhcpSnpVlanId_Type())
fsMIDhcpSnpVlanId.setMaxAccess(_I)
if mibBuilder.loadTexts:fsMIDhcpSnpVlanId.setStatus(_A)
class _FsMIDhcpSnpVlanSnpStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_FsMIDhcpSnpVlanSnpStatus_Type.__name__=_C
_FsMIDhcpSnpVlanSnpStatus_Object=MibTableColumn
fsMIDhcpSnpVlanSnpStatus=_FsMIDhcpSnpVlanSnpStatus_Object((1,3,6,1,4,1,29601,2,49,2,1,1,3),_FsMIDhcpSnpVlanSnpStatus_Type())
fsMIDhcpSnpVlanSnpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIDhcpSnpVlanSnpStatus.setStatus(_A)
_FsMIDhcpSnpRxDiscovers_Type=Counter32
_FsMIDhcpSnpRxDiscovers_Object=MibTableColumn
fsMIDhcpSnpRxDiscovers=_FsMIDhcpSnpRxDiscovers_Object((1,3,6,1,4,1,29601,2,49,2,1,1,4),_FsMIDhcpSnpRxDiscovers_Type())
fsMIDhcpSnpRxDiscovers.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpRxDiscovers.setStatus(_A)
_FsMIDhcpSnpRxRequests_Type=Counter32
_FsMIDhcpSnpRxRequests_Object=MibTableColumn
fsMIDhcpSnpRxRequests=_FsMIDhcpSnpRxRequests_Object((1,3,6,1,4,1,29601,2,49,2,1,1,5),_FsMIDhcpSnpRxRequests_Type())
fsMIDhcpSnpRxRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpRxRequests.setStatus(_A)
_FsMIDhcpSnpRxReleases_Type=Counter32
_FsMIDhcpSnpRxReleases_Object=MibTableColumn
fsMIDhcpSnpRxReleases=_FsMIDhcpSnpRxReleases_Object((1,3,6,1,4,1,29601,2,49,2,1,1,6),_FsMIDhcpSnpRxReleases_Type())
fsMIDhcpSnpRxReleases.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpRxReleases.setStatus(_A)
_FsMIDhcpSnpRxDeclines_Type=Counter32
_FsMIDhcpSnpRxDeclines_Object=MibTableColumn
fsMIDhcpSnpRxDeclines=_FsMIDhcpSnpRxDeclines_Object((1,3,6,1,4,1,29601,2,49,2,1,1,7),_FsMIDhcpSnpRxDeclines_Type())
fsMIDhcpSnpRxDeclines.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpRxDeclines.setStatus(_A)
_FsMIDhcpSnpRxInforms_Type=Counter32
_FsMIDhcpSnpRxInforms_Object=MibTableColumn
fsMIDhcpSnpRxInforms=_FsMIDhcpSnpRxInforms_Object((1,3,6,1,4,1,29601,2,49,2,1,1,8),_FsMIDhcpSnpRxInforms_Type())
fsMIDhcpSnpRxInforms.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpRxInforms.setStatus(_A)
_FsMIDhcpSnpTxOffers_Type=Counter32
_FsMIDhcpSnpTxOffers_Object=MibTableColumn
fsMIDhcpSnpTxOffers=_FsMIDhcpSnpTxOffers_Object((1,3,6,1,4,1,29601,2,49,2,1,1,9),_FsMIDhcpSnpTxOffers_Type())
fsMIDhcpSnpTxOffers.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpTxOffers.setStatus(_A)
_FsMIDhcpSnpTxAcks_Type=Counter32
_FsMIDhcpSnpTxAcks_Object=MibTableColumn
fsMIDhcpSnpTxAcks=_FsMIDhcpSnpTxAcks_Object((1,3,6,1,4,1,29601,2,49,2,1,1,10),_FsMIDhcpSnpTxAcks_Type())
fsMIDhcpSnpTxAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpTxAcks.setStatus(_A)
_FsMIDhcpSnpTxNaks_Type=Counter32
_FsMIDhcpSnpTxNaks_Object=MibTableColumn
fsMIDhcpSnpTxNaks=_FsMIDhcpSnpTxNaks_Object((1,3,6,1,4,1,29601,2,49,2,1,1,11),_FsMIDhcpSnpTxNaks_Type())
fsMIDhcpSnpTxNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpTxNaks.setStatus(_A)
_FsMIDhcpSnpNoOfDiscards_Type=Counter32
_FsMIDhcpSnpNoOfDiscards_Object=MibTableColumn
fsMIDhcpSnpNoOfDiscards=_FsMIDhcpSnpNoOfDiscards_Object((1,3,6,1,4,1,29601,2,49,2,1,1,12),_FsMIDhcpSnpNoOfDiscards_Type())
fsMIDhcpSnpNoOfDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpNoOfDiscards.setStatus(_A)
_FsMIDhcpSnpMacDiscards_Type=Counter32
_FsMIDhcpSnpMacDiscards_Object=MibTableColumn
fsMIDhcpSnpMacDiscards=_FsMIDhcpSnpMacDiscards_Object((1,3,6,1,4,1,29601,2,49,2,1,1,13),_FsMIDhcpSnpMacDiscards_Type())
fsMIDhcpSnpMacDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpMacDiscards.setStatus(_A)
_FsMIDhcpSnpServerDiscards_Type=Counter32
_FsMIDhcpSnpServerDiscards_Object=MibTableColumn
fsMIDhcpSnpServerDiscards=_FsMIDhcpSnpServerDiscards_Object((1,3,6,1,4,1,29601,2,49,2,1,1,14),_FsMIDhcpSnpServerDiscards_Type())
fsMIDhcpSnpServerDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpServerDiscards.setStatus(_A)
_FsMIDhcpSnpOptionDiscards_Type=Counter32
_FsMIDhcpSnpOptionDiscards_Object=MibTableColumn
fsMIDhcpSnpOptionDiscards=_FsMIDhcpSnpOptionDiscards_Object((1,3,6,1,4,1,29601,2,49,2,1,1,15),_FsMIDhcpSnpOptionDiscards_Type())
fsMIDhcpSnpOptionDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpOptionDiscards.setStatus(_A)
_FsMIDhcpSnpInterfaceStatus_Type=RowStatus
_FsMIDhcpSnpInterfaceStatus_Object=MibTableColumn
fsMIDhcpSnpInterfaceStatus=_FsMIDhcpSnpInterfaceStatus_Object((1,3,6,1,4,1,29601,2,49,2,1,1,16),_FsMIDhcpSnpInterfaceStatus_Type())
fsMIDhcpSnpInterfaceStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIDhcpSnpInterfaceStatus.setStatus(_A)
class _FsMIDhcpSnpV6VlanSnpStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_FsMIDhcpSnpV6VlanSnpStatus_Type.__name__=_C
_FsMIDhcpSnpV6VlanSnpStatus_Object=MibTableColumn
fsMIDhcpSnpV6VlanSnpStatus=_FsMIDhcpSnpV6VlanSnpStatus_Object((1,3,6,1,4,1,29601,2,49,2,1,1,17),_FsMIDhcpSnpV6VlanSnpStatus_Type())
fsMIDhcpSnpV6VlanSnpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIDhcpSnpV6VlanSnpStatus.setStatus(_A)
_FsMIDhcpSnpV6RxClientPkts_Type=Counter32
_FsMIDhcpSnpV6RxClientPkts_Object=MibTableColumn
fsMIDhcpSnpV6RxClientPkts=_FsMIDhcpSnpV6RxClientPkts_Object((1,3,6,1,4,1,29601,2,49,2,1,1,18),_FsMIDhcpSnpV6RxClientPkts_Type())
fsMIDhcpSnpV6RxClientPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpV6RxClientPkts.setStatus(_A)
_FsMIDhcpSnpV6TxClientPkts_Type=Counter32
_FsMIDhcpSnpV6TxClientPkts_Object=MibTableColumn
fsMIDhcpSnpV6TxClientPkts=_FsMIDhcpSnpV6TxClientPkts_Object((1,3,6,1,4,1,29601,2,49,2,1,1,19),_FsMIDhcpSnpV6TxClientPkts_Type())
fsMIDhcpSnpV6TxClientPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpV6TxClientPkts.setStatus(_A)
_FsMIDhcpSnpV6TxRelayForwards_Type=Counter32
_FsMIDhcpSnpV6TxRelayForwards_Object=MibTableColumn
fsMIDhcpSnpV6TxRelayForwards=_FsMIDhcpSnpV6TxRelayForwards_Object((1,3,6,1,4,1,29601,2,49,2,1,1,20),_FsMIDhcpSnpV6TxRelayForwards_Type())
fsMIDhcpSnpV6TxRelayForwards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpV6TxRelayForwards.setStatus(_A)
_FsMIDhcpSnpV6RxRelayReplys_Type=Counter32
_FsMIDhcpSnpV6RxRelayReplys_Object=MibTableColumn
fsMIDhcpSnpV6RxRelayReplys=_FsMIDhcpSnpV6RxRelayReplys_Object((1,3,6,1,4,1,29601,2,49,2,1,1,21),_FsMIDhcpSnpV6RxRelayReplys_Type())
fsMIDhcpSnpV6RxRelayReplys.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpV6RxRelayReplys.setStatus(_A)
_FsMIDhcpSnpV6PktDrops_Type=Counter32
_FsMIDhcpSnpV6PktDrops_Object=MibTableColumn
fsMIDhcpSnpV6PktDrops=_FsMIDhcpSnpV6PktDrops_Object((1,3,6,1,4,1,29601,2,49,2,1,1,22),_FsMIDhcpSnpV6PktDrops_Type())
fsMIDhcpSnpV6PktDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpV6PktDrops.setStatus(_A)
class _FsMIDhcpSnpV6ClearStatistics_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_FsMIDhcpSnpV6ClearStatistics_Type.__name__=_C
_FsMIDhcpSnpV6ClearStatistics_Object=MibTableColumn
fsMIDhcpSnpV6ClearStatistics=_FsMIDhcpSnpV6ClearStatistics_Object((1,3,6,1,4,1,29601,2,49,2,1,1,23),_FsMIDhcpSnpV6ClearStatistics_Type())
fsMIDhcpSnpV6ClearStatistics.setMaxAccess(_D)
if mibBuilder.loadTexts:fsMIDhcpSnpV6ClearStatistics.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'fsMIDhcpSnp':fsMIDhcpSnp,'fsMIDhcpSnpGlobalConfig':fsMIDhcpSnpGlobalConfig,'fsMIDhcpSnpGlobalConfigTable':fsMIDhcpSnpGlobalConfigTable,'fsMIDhcpSnpGlobalConfigEntry':fsMIDhcpSnpGlobalConfigEntry,_H:fsMIDhcpSnpContextId,'fsMIDhcpSnpSnoopingAdminStatus':fsMIDhcpSnpSnoopingAdminStatus,'fsMIDhcpSnpMacVerifyStatus':fsMIDhcpSnpMacVerifyStatus,'fsMIDhcpSnpV6AdminStatus':fsMIDhcpSnpV6AdminStatus,'fsMIDhcpSnpTraceValue':fsMIDhcpSnpTraceValue,'fsMIDhcpSnpV6EnterpriseId':fsMIDhcpSnpV6EnterpriseId,'fsMIDhcpSnpInterface':fsMIDhcpSnpInterface,'fsMIDhcpSnpInterfaceTable':fsMIDhcpSnpInterfaceTable,'fsMIDhcpSnpInterfaceEntry':fsMIDhcpSnpInterfaceEntry,_J:fsMIDhcpSnpVlanId,'fsMIDhcpSnpVlanSnpStatus':fsMIDhcpSnpVlanSnpStatus,'fsMIDhcpSnpRxDiscovers':fsMIDhcpSnpRxDiscovers,'fsMIDhcpSnpRxRequests':fsMIDhcpSnpRxRequests,'fsMIDhcpSnpRxReleases':fsMIDhcpSnpRxReleases,'fsMIDhcpSnpRxDeclines':fsMIDhcpSnpRxDeclines,'fsMIDhcpSnpRxInforms':fsMIDhcpSnpRxInforms,'fsMIDhcpSnpTxOffers':fsMIDhcpSnpTxOffers,'fsMIDhcpSnpTxAcks':fsMIDhcpSnpTxAcks,'fsMIDhcpSnpTxNaks':fsMIDhcpSnpTxNaks,'fsMIDhcpSnpNoOfDiscards':fsMIDhcpSnpNoOfDiscards,'fsMIDhcpSnpMacDiscards':fsMIDhcpSnpMacDiscards,'fsMIDhcpSnpServerDiscards':fsMIDhcpSnpServerDiscards,'fsMIDhcpSnpOptionDiscards':fsMIDhcpSnpOptionDiscards,'fsMIDhcpSnpInterfaceStatus':fsMIDhcpSnpInterfaceStatus,'fsMIDhcpSnpV6VlanSnpStatus':fsMIDhcpSnpV6VlanSnpStatus,'fsMIDhcpSnpV6RxClientPkts':fsMIDhcpSnpV6RxClientPkts,'fsMIDhcpSnpV6TxClientPkts':fsMIDhcpSnpV6TxClientPkts,'fsMIDhcpSnpV6TxRelayForwards':fsMIDhcpSnpV6TxRelayForwards,'fsMIDhcpSnpV6RxRelayReplys':fsMIDhcpSnpV6RxRelayReplys,'fsMIDhcpSnpV6PktDrops':fsMIDhcpSnpV6PktDrops,'fsMIDhcpSnpV6ClearStatistics':fsMIDhcpSnpV6ClearStatistics})