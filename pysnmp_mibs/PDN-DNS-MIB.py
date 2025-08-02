_G='devHostMappingIpAddress'
_F='read-only'
_E='devDNSServerIP'
_D='DisplayString'
_C='PDN-DNS-MIB'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pdn_dns,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-dns')
DNSServerType,DomainName=mibBuilder.importSymbols('PDN-TC','DNSServerType','DomainName')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention')
_PdnDNSMIBObjects_ObjectIdentity=ObjectIdentity
pdnDNSMIBObjects=_PdnDNSMIBObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,17,1))
_DevDNSDefaultDomainName_Type=DomainName
_DevDNSDefaultDomainName_Object=MibScalar
devDNSDefaultDomainName=_DevDNSDefaultDomainName_Object((1,3,6,1,4,1,1795,2,24,2,17,1,1),_DevDNSDefaultDomainName_Type())
devDNSDefaultDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:devDNSDefaultDomainName.setStatus(_A)
_DevDNSRetryTimeout_Type=Integer32
_DevDNSRetryTimeout_Object=MibScalar
devDNSRetryTimeout=_DevDNSRetryTimeout_Object((1,3,6,1,4,1,1795,2,24,2,17,1,2),_DevDNSRetryTimeout_Type())
devDNSRetryTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:devDNSRetryTimeout.setStatus(_A)
_DevDNSMaxRetries_Type=Integer32
_DevDNSMaxRetries_Object=MibScalar
devDNSMaxRetries=_DevDNSMaxRetries_Object((1,3,6,1,4,1,1795,2,24,2,17,1,3),_DevDNSMaxRetries_Type())
devDNSMaxRetries.setMaxAccess(_B)
if mibBuilder.loadTexts:devDNSMaxRetries.setStatus(_A)
_DevDNSServerTable_Object=MibTable
devDNSServerTable=_DevDNSServerTable_Object((1,3,6,1,4,1,1795,2,24,2,17,1,4))
if mibBuilder.loadTexts:devDNSServerTable.setStatus(_A)
_DevDNSServerEntry_Object=MibTableRow
devDNSServerEntry=_DevDNSServerEntry_Object((1,3,6,1,4,1,1795,2,24,2,17,1,4,1))
devDNSServerEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:devDNSServerEntry.setStatus(_A)
_DevDNSServerIP_Type=IpAddress
_DevDNSServerIP_Object=MibTableColumn
devDNSServerIP=_DevDNSServerIP_Object((1,3,6,1,4,1,1795,2,24,2,17,1,4,1,1),_DevDNSServerIP_Type())
devDNSServerIP.setMaxAccess(_F)
if mibBuilder.loadTexts:devDNSServerIP.setStatus(_A)
_DevDNSServerType_Type=DNSServerType
_DevDNSServerType_Object=MibTableColumn
devDNSServerType=_DevDNSServerType_Object((1,3,6,1,4,1,1795,2,24,2,17,1,4,1,2),_DevDNSServerType_Type())
devDNSServerType.setMaxAccess(_B)
if mibBuilder.loadTexts:devDNSServerType.setStatus(_A)
_DevDNSRowStatus_Type=RowStatus
_DevDNSRowStatus_Object=MibTableColumn
devDNSRowStatus=_DevDNSRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,17,1,4,1,3),_DevDNSRowStatus_Type())
devDNSRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:devDNSRowStatus.setStatus(_A)
_DevHostMappingTable_Object=MibTable
devHostMappingTable=_DevHostMappingTable_Object((1,3,6,1,4,1,1795,2,24,2,17,1,5))
if mibBuilder.loadTexts:devHostMappingTable.setStatus(_A)
_DevHostMappingEntry_Object=MibTableRow
devHostMappingEntry=_DevHostMappingEntry_Object((1,3,6,1,4,1,1795,2,24,2,17,1,5,1))
devHostMappingEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:devHostMappingEntry.setStatus(_A)
_DevHostMappingIpAddress_Type=IpAddress
_DevHostMappingIpAddress_Object=MibTableColumn
devHostMappingIpAddress=_DevHostMappingIpAddress_Object((1,3,6,1,4,1,1795,2,24,2,17,1,5,1,1),_DevHostMappingIpAddress_Type())
devHostMappingIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:devHostMappingIpAddress.setStatus(_A)
class _DevHostMappingHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_DevHostMappingHostName_Type.__name__=_D
_DevHostMappingHostName_Object=MibTableColumn
devHostMappingHostName=_DevHostMappingHostName_Object((1,3,6,1,4,1,1795,2,24,2,17,1,5,1,2),_DevHostMappingHostName_Type())
devHostMappingHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:devHostMappingHostName.setStatus(_A)
_DevHostMappingRowStatus_Type=RowStatus
_DevHostMappingRowStatus_Object=MibTableColumn
devHostMappingRowStatus=_DevHostMappingRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,17,1,5,1,3),_DevHostMappingRowStatus_Type())
devHostMappingRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:devHostMappingRowStatus.setStatus(_A)
_PdnDNSMIBTraps_ObjectIdentity=ObjectIdentity
pdnDNSMIBTraps=_PdnDNSMIBTraps_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,17,2))
mibBuilder.exportSymbols(_C,**{'pdnDNSMIBObjects':pdnDNSMIBObjects,'devDNSDefaultDomainName':devDNSDefaultDomainName,'devDNSRetryTimeout':devDNSRetryTimeout,'devDNSMaxRetries':devDNSMaxRetries,'devDNSServerTable':devDNSServerTable,'devDNSServerEntry':devDNSServerEntry,_E:devDNSServerIP,'devDNSServerType':devDNSServerType,'devDNSRowStatus':devDNSRowStatus,'devHostMappingTable':devHostMappingTable,'devHostMappingEntry':devHostMappingEntry,_G:devHostMappingIpAddress,'devHostMappingHostName':devHostMappingHostName,'devHostMappingRowStatus':devHostMappingRowStatus,'pdnDNSMIBTraps':pdnDNSMIBTraps})