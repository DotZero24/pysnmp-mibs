_H='fsDhcpSnpVlanId'
_G='SUPERMICRO-DHCP-SNOOPING-MIB'
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
fsdhcpsnp=ModuleIdentity((1,3,6,1,4,1,10876,101,2,3))
if mibBuilder.loadTexts:fsdhcpsnp.setRevisions(('2012-09-05 00:00',))
_FsDhcpSnpScalars_ObjectIdentity=ObjectIdentity
fsDhcpSnpScalars=_FsDhcpSnpScalars_ObjectIdentity((1,3,6,1,4,1,10876,101,2,3,1))
class _FsDhcpSnpSnoopingAdminStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_FsDhcpSnpSnoopingAdminStatus_Type.__name__=_C
_FsDhcpSnpSnoopingAdminStatus_Object=MibScalar
fsDhcpSnpSnoopingAdminStatus=_FsDhcpSnpSnoopingAdminStatus_Object((1,3,6,1,4,1,10876,101,2,3,1,1),_FsDhcpSnpSnoopingAdminStatus_Type())
fsDhcpSnpSnoopingAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcpSnpSnoopingAdminStatus.setStatus(_A)
class _FsDhcpSnpMacVerifyStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_FsDhcpSnpMacVerifyStatus_Type.__name__=_C
_FsDhcpSnpMacVerifyStatus_Object=MibScalar
fsDhcpSnpMacVerifyStatus=_FsDhcpSnpMacVerifyStatus_Object((1,3,6,1,4,1,10876,101,2,3,1,2),_FsDhcpSnpMacVerifyStatus_Type())
fsDhcpSnpMacVerifyStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcpSnpMacVerifyStatus.setStatus(_A)
_FsDhcpSnpInterface_ObjectIdentity=ObjectIdentity
fsDhcpSnpInterface=_FsDhcpSnpInterface_ObjectIdentity((1,3,6,1,4,1,10876,101,2,3,2))
_FsDhcpSnpInterfaceTable_Object=MibTable
fsDhcpSnpInterfaceTable=_FsDhcpSnpInterfaceTable_Object((1,3,6,1,4,1,10876,101,2,3,2,1))
if mibBuilder.loadTexts:fsDhcpSnpInterfaceTable.setStatus(_A)
_FsDhcpSnpInterfaceEntry_Object=MibTableRow
fsDhcpSnpInterfaceEntry=_FsDhcpSnpInterfaceEntry_Object((1,3,6,1,4,1,10876,101,2,3,2,1,1))
fsDhcpSnpInterfaceEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:fsDhcpSnpInterfaceEntry.setStatus(_A)
class _FsDhcpSnpVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsDhcpSnpVlanId_Type.__name__=_C
_FsDhcpSnpVlanId_Object=MibTableColumn
fsDhcpSnpVlanId=_FsDhcpSnpVlanId_Object((1,3,6,1,4,1,10876,101,2,3,2,1,1,1),_FsDhcpSnpVlanId_Type())
fsDhcpSnpVlanId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fsDhcpSnpVlanId.setStatus(_A)
class _FsDhcpSnpVlanSnpStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_FsDhcpSnpVlanSnpStatus_Type.__name__=_C
_FsDhcpSnpVlanSnpStatus_Object=MibTableColumn
fsDhcpSnpVlanSnpStatus=_FsDhcpSnpVlanSnpStatus_Object((1,3,6,1,4,1,10876,101,2,3,2,1,1,2),_FsDhcpSnpVlanSnpStatus_Type())
fsDhcpSnpVlanSnpStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcpSnpVlanSnpStatus.setStatus(_A)
_FsDhcpSnpRxDiscovers_Type=Counter32
_FsDhcpSnpRxDiscovers_Object=MibTableColumn
fsDhcpSnpRxDiscovers=_FsDhcpSnpRxDiscovers_Object((1,3,6,1,4,1,10876,101,2,3,2,1,1,3),_FsDhcpSnpRxDiscovers_Type())
fsDhcpSnpRxDiscovers.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcpSnpRxDiscovers.setStatus(_A)
_FsDhcpSnpRxRequests_Type=Counter32
_FsDhcpSnpRxRequests_Object=MibTableColumn
fsDhcpSnpRxRequests=_FsDhcpSnpRxRequests_Object((1,3,6,1,4,1,10876,101,2,3,2,1,1,4),_FsDhcpSnpRxRequests_Type())
fsDhcpSnpRxRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcpSnpRxRequests.setStatus(_A)
_FsDhcpSnpRxReleases_Type=Counter32
_FsDhcpSnpRxReleases_Object=MibTableColumn
fsDhcpSnpRxReleases=_FsDhcpSnpRxReleases_Object((1,3,6,1,4,1,10876,101,2,3,2,1,1,5),_FsDhcpSnpRxReleases_Type())
fsDhcpSnpRxReleases.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcpSnpRxReleases.setStatus(_A)
_FsDhcpSnpRxDeclines_Type=Counter32
_FsDhcpSnpRxDeclines_Object=MibTableColumn
fsDhcpSnpRxDeclines=_FsDhcpSnpRxDeclines_Object((1,3,6,1,4,1,10876,101,2,3,2,1,1,6),_FsDhcpSnpRxDeclines_Type())
fsDhcpSnpRxDeclines.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcpSnpRxDeclines.setStatus(_A)
_FsDhcpSnpRxInforms_Type=Counter32
_FsDhcpSnpRxInforms_Object=MibTableColumn
fsDhcpSnpRxInforms=_FsDhcpSnpRxInforms_Object((1,3,6,1,4,1,10876,101,2,3,2,1,1,7),_FsDhcpSnpRxInforms_Type())
fsDhcpSnpRxInforms.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcpSnpRxInforms.setStatus(_A)
_FsDhcpSnpTxOffers_Type=Counter32
_FsDhcpSnpTxOffers_Object=MibTableColumn
fsDhcpSnpTxOffers=_FsDhcpSnpTxOffers_Object((1,3,6,1,4,1,10876,101,2,3,2,1,1,8),_FsDhcpSnpTxOffers_Type())
fsDhcpSnpTxOffers.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcpSnpTxOffers.setStatus(_A)
_FsDhcpSnpTxAcks_Type=Counter32
_FsDhcpSnpTxAcks_Object=MibTableColumn
fsDhcpSnpTxAcks=_FsDhcpSnpTxAcks_Object((1,3,6,1,4,1,10876,101,2,3,2,1,1,9),_FsDhcpSnpTxAcks_Type())
fsDhcpSnpTxAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcpSnpTxAcks.setStatus(_A)
_FsDhcpSnpTxNaks_Type=Counter32
_FsDhcpSnpTxNaks_Object=MibTableColumn
fsDhcpSnpTxNaks=_FsDhcpSnpTxNaks_Object((1,3,6,1,4,1,10876,101,2,3,2,1,1,10),_FsDhcpSnpTxNaks_Type())
fsDhcpSnpTxNaks.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcpSnpTxNaks.setStatus(_A)
_FsDhcpSnpNoOfDiscards_Type=Counter32
_FsDhcpSnpNoOfDiscards_Object=MibTableColumn
fsDhcpSnpNoOfDiscards=_FsDhcpSnpNoOfDiscards_Object((1,3,6,1,4,1,10876,101,2,3,2,1,1,11),_FsDhcpSnpNoOfDiscards_Type())
fsDhcpSnpNoOfDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcpSnpNoOfDiscards.setStatus(_A)
_FsDhcpSnpMacDiscards_Type=Counter32
_FsDhcpSnpMacDiscards_Object=MibTableColumn
fsDhcpSnpMacDiscards=_FsDhcpSnpMacDiscards_Object((1,3,6,1,4,1,10876,101,2,3,2,1,1,12),_FsDhcpSnpMacDiscards_Type())
fsDhcpSnpMacDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcpSnpMacDiscards.setStatus(_A)
_FsDhcpSnpServerDiscards_Type=Counter32
_FsDhcpSnpServerDiscards_Object=MibTableColumn
fsDhcpSnpServerDiscards=_FsDhcpSnpServerDiscards_Object((1,3,6,1,4,1,10876,101,2,3,2,1,1,13),_FsDhcpSnpServerDiscards_Type())
fsDhcpSnpServerDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcpSnpServerDiscards.setStatus(_A)
_FsDhcpSnpOptionDiscards_Type=Counter32
_FsDhcpSnpOptionDiscards_Object=MibTableColumn
fsDhcpSnpOptionDiscards=_FsDhcpSnpOptionDiscards_Object((1,3,6,1,4,1,10876,101,2,3,2,1,1,14),_FsDhcpSnpOptionDiscards_Type())
fsDhcpSnpOptionDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDhcpSnpOptionDiscards.setStatus(_A)
_FsDhcpSnpInterfaceStatus_Type=RowStatus
_FsDhcpSnpInterfaceStatus_Object=MibTableColumn
fsDhcpSnpInterfaceStatus=_FsDhcpSnpInterfaceStatus_Object((1,3,6,1,4,1,10876,101,2,3,2,1,1,15),_FsDhcpSnpInterfaceStatus_Type())
fsDhcpSnpInterfaceStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcpSnpInterfaceStatus.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'fsdhcpsnp':fsdhcpsnp,'fsDhcpSnpScalars':fsDhcpSnpScalars,'fsDhcpSnpSnoopingAdminStatus':fsDhcpSnpSnoopingAdminStatus,'fsDhcpSnpMacVerifyStatus':fsDhcpSnpMacVerifyStatus,'fsDhcpSnpInterface':fsDhcpSnpInterface,'fsDhcpSnpInterfaceTable':fsDhcpSnpInterfaceTable,'fsDhcpSnpInterfaceEntry':fsDhcpSnpInterfaceEntry,_H:fsDhcpSnpVlanId,'fsDhcpSnpVlanSnpStatus':fsDhcpSnpVlanSnpStatus,'fsDhcpSnpRxDiscovers':fsDhcpSnpRxDiscovers,'fsDhcpSnpRxRequests':fsDhcpSnpRxRequests,'fsDhcpSnpRxReleases':fsDhcpSnpRxReleases,'fsDhcpSnpRxDeclines':fsDhcpSnpRxDeclines,'fsDhcpSnpRxInforms':fsDhcpSnpRxInforms,'fsDhcpSnpTxOffers':fsDhcpSnpTxOffers,'fsDhcpSnpTxAcks':fsDhcpSnpTxAcks,'fsDhcpSnpTxNaks':fsDhcpSnpTxNaks,'fsDhcpSnpNoOfDiscards':fsDhcpSnpNoOfDiscards,'fsDhcpSnpMacDiscards':fsDhcpSnpMacDiscards,'fsDhcpSnpServerDiscards':fsDhcpSnpServerDiscards,'fsDhcpSnpOptionDiscards':fsDhcpSnpOptionDiscards,'fsDhcpSnpInterfaceStatus':fsDhcpSnpInterfaceStatus})