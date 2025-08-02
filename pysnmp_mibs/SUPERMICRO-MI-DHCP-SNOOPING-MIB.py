_J='fsMIDhcpSnpVlanId'
_I='not-accessible'
_H='disabled'
_G='enabled'
_F='fsMIDhcpSnpContextId'
_E='read-write'
_D='SUPERMICRO-MI-DHCP-SNOOPING-MIB'
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
fsMIDhcpSnp=ModuleIdentity((1,3,6,1,4,1,10876,101,2,49))
if mibBuilder.loadTexts:fsMIDhcpSnp.setRevisions(('2012-09-05 00:00',))
_FsMIDhcpSnpGlobalConfig_ObjectIdentity=ObjectIdentity
fsMIDhcpSnpGlobalConfig=_FsMIDhcpSnpGlobalConfig_ObjectIdentity((1,3,6,1,4,1,10876,101,2,49,1))
_FsMIDhcpSnpGlobalConfigTable_Object=MibTable
fsMIDhcpSnpGlobalConfigTable=_FsMIDhcpSnpGlobalConfigTable_Object((1,3,6,1,4,1,10876,101,2,49,1,1))
if mibBuilder.loadTexts:fsMIDhcpSnpGlobalConfigTable.setStatus(_A)
_FsMIDhcpSnpGlobalConfigEntry_Object=MibTableRow
fsMIDhcpSnpGlobalConfigEntry=_FsMIDhcpSnpGlobalConfigEntry_Object((1,3,6,1,4,1,10876,101,2,49,1,1,1))
fsMIDhcpSnpGlobalConfigEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:fsMIDhcpSnpGlobalConfigEntry.setStatus(_A)
class _FsMIDhcpSnpContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIDhcpSnpContextId_Type.__name__=_C
_FsMIDhcpSnpContextId_Object=MibTableColumn
fsMIDhcpSnpContextId=_FsMIDhcpSnpContextId_Object((1,3,6,1,4,1,10876,101,2,49,1,1,1,1),_FsMIDhcpSnpContextId_Type())
fsMIDhcpSnpContextId.setMaxAccess(_I)
if mibBuilder.loadTexts:fsMIDhcpSnpContextId.setStatus(_A)
class _FsMIDhcpSnpSnoopingAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FsMIDhcpSnpSnoopingAdminStatus_Type.__name__=_C
_FsMIDhcpSnpSnoopingAdminStatus_Object=MibTableColumn
fsMIDhcpSnpSnoopingAdminStatus=_FsMIDhcpSnpSnoopingAdminStatus_Object((1,3,6,1,4,1,10876,101,2,49,1,1,1,2),_FsMIDhcpSnpSnoopingAdminStatus_Type())
fsMIDhcpSnpSnoopingAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIDhcpSnpSnoopingAdminStatus.setStatus(_A)
class _FsMIDhcpSnpMacVerifyStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FsMIDhcpSnpMacVerifyStatus_Type.__name__=_C
_FsMIDhcpSnpMacVerifyStatus_Object=MibTableColumn
fsMIDhcpSnpMacVerifyStatus=_FsMIDhcpSnpMacVerifyStatus_Object((1,3,6,1,4,1,10876,101,2,49,1,1,1,3),_FsMIDhcpSnpMacVerifyStatus_Type())
fsMIDhcpSnpMacVerifyStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIDhcpSnpMacVerifyStatus.setStatus(_A)
_FsMIDhcpSnpInterface_ObjectIdentity=ObjectIdentity
fsMIDhcpSnpInterface=_FsMIDhcpSnpInterface_ObjectIdentity((1,3,6,1,4,1,10876,101,2,49,2))
_FsMIDhcpSnpInterfaceTable_Object=MibTable
fsMIDhcpSnpInterfaceTable=_FsMIDhcpSnpInterfaceTable_Object((1,3,6,1,4,1,10876,101,2,49,2,1))
if mibBuilder.loadTexts:fsMIDhcpSnpInterfaceTable.setStatus(_A)
_FsMIDhcpSnpInterfaceEntry_Object=MibTableRow
fsMIDhcpSnpInterfaceEntry=_FsMIDhcpSnpInterfaceEntry_Object((1,3,6,1,4,1,10876,101,2,49,2,1,1))
fsMIDhcpSnpInterfaceEntry.setIndexNames((0,_D,_F),(0,_D,_J))
if mibBuilder.loadTexts:fsMIDhcpSnpInterfaceEntry.setStatus(_A)
class _FsMIDhcpSnpVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsMIDhcpSnpVlanId_Type.__name__=_C
_FsMIDhcpSnpVlanId_Object=MibTableColumn
fsMIDhcpSnpVlanId=_FsMIDhcpSnpVlanId_Object((1,3,6,1,4,1,10876,101,2,49,2,1,1,2),_FsMIDhcpSnpVlanId_Type())
fsMIDhcpSnpVlanId.setMaxAccess(_I)
if mibBuilder.loadTexts:fsMIDhcpSnpVlanId.setStatus(_A)
class _FsMIDhcpSnpVlanSnpStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_FsMIDhcpSnpVlanSnpStatus_Type.__name__=_C
_FsMIDhcpSnpVlanSnpStatus_Object=MibTableColumn
fsMIDhcpSnpVlanSnpStatus=_FsMIDhcpSnpVlanSnpStatus_Object((1,3,6,1,4,1,10876,101,2,49,2,1,1,3),_FsMIDhcpSnpVlanSnpStatus_Type())
fsMIDhcpSnpVlanSnpStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIDhcpSnpVlanSnpStatus.setStatus(_A)
_FsMIDhcpSnpRxDiscovers_Type=Counter32
_FsMIDhcpSnpRxDiscovers_Object=MibTableColumn
fsMIDhcpSnpRxDiscovers=_FsMIDhcpSnpRxDiscovers_Object((1,3,6,1,4,1,10876,101,2,49,2,1,1,4),_FsMIDhcpSnpRxDiscovers_Type())
fsMIDhcpSnpRxDiscovers.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpRxDiscovers.setStatus(_A)
_FsMIDhcpSnpRxRequests_Type=Counter32
_FsMIDhcpSnpRxRequests_Object=MibTableColumn
fsMIDhcpSnpRxRequests=_FsMIDhcpSnpRxRequests_Object((1,3,6,1,4,1,10876,101,2,49,2,1,1,5),_FsMIDhcpSnpRxRequests_Type())
fsMIDhcpSnpRxRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpRxRequests.setStatus(_A)
_FsMIDhcpSnpRxReleases_Type=Counter32
_FsMIDhcpSnpRxReleases_Object=MibTableColumn
fsMIDhcpSnpRxReleases=_FsMIDhcpSnpRxReleases_Object((1,3,6,1,4,1,10876,101,2,49,2,1,1,6),_FsMIDhcpSnpRxReleases_Type())
fsMIDhcpSnpRxReleases.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpRxReleases.setStatus(_A)
_FsMIDhcpSnpRxDeclines_Type=Counter32
_FsMIDhcpSnpRxDeclines_Object=MibTableColumn
fsMIDhcpSnpRxDeclines=_FsMIDhcpSnpRxDeclines_Object((1,3,6,1,4,1,10876,101,2,49,2,1,1,7),_FsMIDhcpSnpRxDeclines_Type())
fsMIDhcpSnpRxDeclines.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpRxDeclines.setStatus(_A)
_FsMIDhcpSnpRxInforms_Type=Counter32
_FsMIDhcpSnpRxInforms_Object=MibTableColumn
fsMIDhcpSnpRxInforms=_FsMIDhcpSnpRxInforms_Object((1,3,6,1,4,1,10876,101,2,49,2,1,1,8),_FsMIDhcpSnpRxInforms_Type())
fsMIDhcpSnpRxInforms.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpRxInforms.setStatus(_A)
_FsMIDhcpSnpTxOffers_Type=Counter32
_FsMIDhcpSnpTxOffers_Object=MibTableColumn
fsMIDhcpSnpTxOffers=_FsMIDhcpSnpTxOffers_Object((1,3,6,1,4,1,10876,101,2,49,2,1,1,9),_FsMIDhcpSnpTxOffers_Type())
fsMIDhcpSnpTxOffers.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpTxOffers.setStatus(_A)
_FsMIDhcpSnpTxAcks_Type=Counter32
_FsMIDhcpSnpTxAcks_Object=MibTableColumn
fsMIDhcpSnpTxAcks=_FsMIDhcpSnpTxAcks_Object((1,3,6,1,4,1,10876,101,2,49,2,1,1,10),_FsMIDhcpSnpTxAcks_Type())
fsMIDhcpSnpTxAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpTxAcks.setStatus(_A)
_FsMIDhcpSnpTxNaks_Type=Counter32
_FsMIDhcpSnpTxNaks_Object=MibTableColumn
fsMIDhcpSnpTxNaks=_FsMIDhcpSnpTxNaks_Object((1,3,6,1,4,1,10876,101,2,49,2,1,1,11),_FsMIDhcpSnpTxNaks_Type())
fsMIDhcpSnpTxNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpTxNaks.setStatus(_A)
_FsMIDhcpSnpNoOfDiscards_Type=Counter32
_FsMIDhcpSnpNoOfDiscards_Object=MibTableColumn
fsMIDhcpSnpNoOfDiscards=_FsMIDhcpSnpNoOfDiscards_Object((1,3,6,1,4,1,10876,101,2,49,2,1,1,12),_FsMIDhcpSnpNoOfDiscards_Type())
fsMIDhcpSnpNoOfDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpNoOfDiscards.setStatus(_A)
_FsMIDhcpSnpMacDiscards_Type=Counter32
_FsMIDhcpSnpMacDiscards_Object=MibTableColumn
fsMIDhcpSnpMacDiscards=_FsMIDhcpSnpMacDiscards_Object((1,3,6,1,4,1,10876,101,2,49,2,1,1,13),_FsMIDhcpSnpMacDiscards_Type())
fsMIDhcpSnpMacDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpMacDiscards.setStatus(_A)
_FsMIDhcpSnpServerDiscards_Type=Counter32
_FsMIDhcpSnpServerDiscards_Object=MibTableColumn
fsMIDhcpSnpServerDiscards=_FsMIDhcpSnpServerDiscards_Object((1,3,6,1,4,1,10876,101,2,49,2,1,1,14),_FsMIDhcpSnpServerDiscards_Type())
fsMIDhcpSnpServerDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpServerDiscards.setStatus(_A)
_FsMIDhcpSnpOptionDiscards_Type=Counter32
_FsMIDhcpSnpOptionDiscards_Object=MibTableColumn
fsMIDhcpSnpOptionDiscards=_FsMIDhcpSnpOptionDiscards_Object((1,3,6,1,4,1,10876,101,2,49,2,1,1,15),_FsMIDhcpSnpOptionDiscards_Type())
fsMIDhcpSnpOptionDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIDhcpSnpOptionDiscards.setStatus(_A)
_FsMIDhcpSnpInterfaceStatus_Type=RowStatus
_FsMIDhcpSnpInterfaceStatus_Object=MibTableColumn
fsMIDhcpSnpInterfaceStatus=_FsMIDhcpSnpInterfaceStatus_Object((1,3,6,1,4,1,10876,101,2,49,2,1,1,16),_FsMIDhcpSnpInterfaceStatus_Type())
fsMIDhcpSnpInterfaceStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:fsMIDhcpSnpInterfaceStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'fsMIDhcpSnp':fsMIDhcpSnp,'fsMIDhcpSnpGlobalConfig':fsMIDhcpSnpGlobalConfig,'fsMIDhcpSnpGlobalConfigTable':fsMIDhcpSnpGlobalConfigTable,'fsMIDhcpSnpGlobalConfigEntry':fsMIDhcpSnpGlobalConfigEntry,_F:fsMIDhcpSnpContextId,'fsMIDhcpSnpSnoopingAdminStatus':fsMIDhcpSnpSnoopingAdminStatus,'fsMIDhcpSnpMacVerifyStatus':fsMIDhcpSnpMacVerifyStatus,'fsMIDhcpSnpInterface':fsMIDhcpSnpInterface,'fsMIDhcpSnpInterfaceTable':fsMIDhcpSnpInterfaceTable,'fsMIDhcpSnpInterfaceEntry':fsMIDhcpSnpInterfaceEntry,_J:fsMIDhcpSnpVlanId,'fsMIDhcpSnpVlanSnpStatus':fsMIDhcpSnpVlanSnpStatus,'fsMIDhcpSnpRxDiscovers':fsMIDhcpSnpRxDiscovers,'fsMIDhcpSnpRxRequests':fsMIDhcpSnpRxRequests,'fsMIDhcpSnpRxReleases':fsMIDhcpSnpRxReleases,'fsMIDhcpSnpRxDeclines':fsMIDhcpSnpRxDeclines,'fsMIDhcpSnpRxInforms':fsMIDhcpSnpRxInforms,'fsMIDhcpSnpTxOffers':fsMIDhcpSnpTxOffers,'fsMIDhcpSnpTxAcks':fsMIDhcpSnpTxAcks,'fsMIDhcpSnpTxNaks':fsMIDhcpSnpTxNaks,'fsMIDhcpSnpNoOfDiscards':fsMIDhcpSnpNoOfDiscards,'fsMIDhcpSnpMacDiscards':fsMIDhcpSnpMacDiscards,'fsMIDhcpSnpServerDiscards':fsMIDhcpSnpServerDiscards,'fsMIDhcpSnpOptionDiscards':fsMIDhcpSnpOptionDiscards,'fsMIDhcpSnpInterfaceStatus':fsMIDhcpSnpInterfaceStatus})