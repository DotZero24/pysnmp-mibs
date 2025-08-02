_G='subnetAdd'
_F='DHCP-MIB'
_E='DisplayString'
_D='software'
_C='microsoft'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
microsoft,software=mibBuilder.importSymbols('MSFT-MIB',_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
_Microsoft_ObjectIdentity=ObjectIdentity
microsoft=_Microsoft_ObjectIdentity((1,3,6,1,4,1,311))
_Software_ObjectIdentity=ObjectIdentity
software=_Software_ObjectIdentity((1,3,6,1,4,1,311,1))
_Dhcp_ObjectIdentity=ObjectIdentity
dhcp=_Dhcp_ObjectIdentity((1,3,6,1,4,1,311,1,3))
_DhcpPar_ObjectIdentity=ObjectIdentity
dhcpPar=_DhcpPar_ObjectIdentity((1,3,6,1,4,1,311,1,3,1))
class _ParDhcpStartTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,30))
_ParDhcpStartTime_Type.__name__=_E
_ParDhcpStartTime_Object=MibScalar
parDhcpStartTime=_ParDhcpStartTime_Object((1,3,6,1,4,1,311,1,3,1,1),_ParDhcpStartTime_Type())
parDhcpStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:parDhcpStartTime.setStatus(_A)
_ParDhcpTotalNoOfDiscovers_Type=Counter32
_ParDhcpTotalNoOfDiscovers_Object=MibScalar
parDhcpTotalNoOfDiscovers=_ParDhcpTotalNoOfDiscovers_Object((1,3,6,1,4,1,311,1,3,1,2),_ParDhcpTotalNoOfDiscovers_Type())
parDhcpTotalNoOfDiscovers.setMaxAccess(_B)
if mibBuilder.loadTexts:parDhcpTotalNoOfDiscovers.setStatus(_A)
_ParDhcpTotalNoOfRequests_Type=Counter32
_ParDhcpTotalNoOfRequests_Object=MibScalar
parDhcpTotalNoOfRequests=_ParDhcpTotalNoOfRequests_Object((1,3,6,1,4,1,311,1,3,1,3),_ParDhcpTotalNoOfRequests_Type())
parDhcpTotalNoOfRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:parDhcpTotalNoOfRequests.setStatus(_A)
_ParDhcpTotalNoOfReleases_Type=Counter32
_ParDhcpTotalNoOfReleases_Object=MibScalar
parDhcpTotalNoOfReleases=_ParDhcpTotalNoOfReleases_Object((1,3,6,1,4,1,311,1,3,1,4),_ParDhcpTotalNoOfReleases_Type())
parDhcpTotalNoOfReleases.setMaxAccess(_B)
if mibBuilder.loadTexts:parDhcpTotalNoOfReleases.setStatus(_A)
_ParDhcpTotalNoOfOffers_Type=Counter32
_ParDhcpTotalNoOfOffers_Object=MibScalar
parDhcpTotalNoOfOffers=_ParDhcpTotalNoOfOffers_Object((1,3,6,1,4,1,311,1,3,1,5),_ParDhcpTotalNoOfOffers_Type())
parDhcpTotalNoOfOffers.setMaxAccess(_B)
if mibBuilder.loadTexts:parDhcpTotalNoOfOffers.setStatus(_A)
_ParDhcpTotalNoOfAcks_Type=Counter32
_ParDhcpTotalNoOfAcks_Object=MibScalar
parDhcpTotalNoOfAcks=_ParDhcpTotalNoOfAcks_Object((1,3,6,1,4,1,311,1,3,1,6),_ParDhcpTotalNoOfAcks_Type())
parDhcpTotalNoOfAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:parDhcpTotalNoOfAcks.setStatus(_A)
_ParDhcpTotalNoOfNacks_Type=Counter32
_ParDhcpTotalNoOfNacks_Object=MibScalar
parDhcpTotalNoOfNacks=_ParDhcpTotalNoOfNacks_Object((1,3,6,1,4,1,311,1,3,1,7),_ParDhcpTotalNoOfNacks_Type())
parDhcpTotalNoOfNacks.setMaxAccess(_B)
if mibBuilder.loadTexts:parDhcpTotalNoOfNacks.setStatus(_A)
_ParDhcpTotalNoOfDeclines_Type=Counter32
_ParDhcpTotalNoOfDeclines_Object=MibScalar
parDhcpTotalNoOfDeclines=_ParDhcpTotalNoOfDeclines_Object((1,3,6,1,4,1,311,1,3,1,8),_ParDhcpTotalNoOfDeclines_Type())
parDhcpTotalNoOfDeclines.setMaxAccess(_B)
if mibBuilder.loadTexts:parDhcpTotalNoOfDeclines.setStatus(_A)
_DhcpScope_ObjectIdentity=ObjectIdentity
dhcpScope=_DhcpScope_ObjectIdentity((1,3,6,1,4,1,311,1,3,2))
_ScopeTable_Object=MibTable
scopeTable=_ScopeTable_Object((1,3,6,1,4,1,311,1,3,2,1))
if mibBuilder.loadTexts:scopeTable.setStatus(_A)
_ScopeTableEntry_Object=MibTableRow
scopeTableEntry=_ScopeTableEntry_Object((1,3,6,1,4,1,311,1,3,2,1,1))
scopeTableEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:scopeTableEntry.setStatus(_A)
_SubnetAdd_Type=IpAddress
_SubnetAdd_Object=MibTableColumn
subnetAdd=_SubnetAdd_Object((1,3,6,1,4,1,311,1,3,2,1,1,1),_SubnetAdd_Type())
subnetAdd.setMaxAccess(_B)
if mibBuilder.loadTexts:subnetAdd.setStatus(_A)
_NoAddInUse_Type=Counter32
_NoAddInUse_Object=MibTableColumn
noAddInUse=_NoAddInUse_Object((1,3,6,1,4,1,311,1,3,2,1,1,2),_NoAddInUse_Type())
noAddInUse.setMaxAccess(_B)
if mibBuilder.loadTexts:noAddInUse.setStatus(_A)
_NoAddFree_Type=Counter32
_NoAddFree_Object=MibTableColumn
noAddFree=_NoAddFree_Object((1,3,6,1,4,1,311,1,3,2,1,1,3),_NoAddFree_Type())
noAddFree.setMaxAccess(_B)
if mibBuilder.loadTexts:noAddFree.setStatus(_A)
_NoPendingOffers_Type=Counter32
_NoPendingOffers_Object=MibTableColumn
noPendingOffers=_NoPendingOffers_Object((1,3,6,1,4,1,311,1,3,2,1,1,4),_NoPendingOffers_Type())
noPendingOffers.setMaxAccess(_B)
if mibBuilder.loadTexts:noPendingOffers.setStatus(_A)
mibBuilder.exportSymbols(_F,**{_C:microsoft,_D:software,'dhcp':dhcp,'dhcpPar':dhcpPar,'parDhcpStartTime':parDhcpStartTime,'parDhcpTotalNoOfDiscovers':parDhcpTotalNoOfDiscovers,'parDhcpTotalNoOfRequests':parDhcpTotalNoOfRequests,'parDhcpTotalNoOfReleases':parDhcpTotalNoOfReleases,'parDhcpTotalNoOfOffers':parDhcpTotalNoOfOffers,'parDhcpTotalNoOfAcks':parDhcpTotalNoOfAcks,'parDhcpTotalNoOfNacks':parDhcpTotalNoOfNacks,'parDhcpTotalNoOfDeclines':parDhcpTotalNoOfDeclines,'dhcpScope':dhcpScope,'scopeTable':scopeTable,'scopeTableEntry':scopeTableEntry,_G:subnetAdd,'noAddInUse':noAddInUse,'noAddFree':noAddFree,'noPendingOffers':noPendingOffers})