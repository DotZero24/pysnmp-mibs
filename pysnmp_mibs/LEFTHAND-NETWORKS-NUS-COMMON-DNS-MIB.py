_H='dnsSuffixIndex'
_G='dnsIndex'
_F='read-only'
_E='Integer32'
_D='LEFTHAND-NETWORKS-NUS-COMMON-DNS-MIB'
_C='read-create'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lhnModules,=mibBuilder.importSymbols('LEFTHAND-NETWORKS-GLOBAL-REG','lhnModules')
lhnNusCommonDNS,=mibBuilder.importSymbols('LEFTHAND-NETWORKS-NUS-COMMON-MIB','lhnNusCommonDNS')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
lhnNusCommonDNSModule=ModuleIdentity((1,3,6,1,4,1,9804,1,1,3))
_DnsNameserverCount_Type=Integer32
_DnsNameserverCount_Object=MibScalar
dnsNameserverCount=_DnsNameserverCount_Object((1,3,6,1,4,1,9804,3,1,1,2,3,1),_DnsNameserverCount_Type())
dnsNameserverCount.setMaxAccess(_F)
if mibBuilder.loadTexts:dnsNameserverCount.setStatus(_A)
class _DnsMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('auto',2)))
_DnsMode_Type.__name__=_E
_DnsMode_Object=MibScalar
dnsMode=_DnsMode_Object((1,3,6,1,4,1,9804,3,1,1,2,3,2),_DnsMode_Type())
dnsMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsMode.setStatus(_A)
_DnsNameserverTable_Object=MibTable
dnsNameserverTable=_DnsNameserverTable_Object((1,3,6,1,4,1,9804,3,1,1,2,3,3))
if mibBuilder.loadTexts:dnsNameserverTable.setStatus(_A)
_DnsNameserverEntry_Object=MibTableRow
dnsNameserverEntry=_DnsNameserverEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,3,3,1))
dnsNameserverEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:dnsNameserverEntry.setStatus(_A)
_DnsIndex_Type=Integer32
_DnsIndex_Object=MibTableColumn
dnsIndex=_DnsIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,3,3,1,1),_DnsIndex_Type())
dnsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dnsIndex.setStatus(_A)
_DnsServer_Type=OctetString
_DnsServer_Object=MibTableColumn
dnsServer=_DnsServer_Object((1,3,6,1,4,1,9804,3,1,1,2,3,3,1,2),_DnsServer_Type())
dnsServer.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsServer.setStatus(_A)
_DnsRowStatus_Type=RowStatus
_DnsRowStatus_Object=MibTableColumn
dnsRowStatus=_DnsRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,3,3,1,3),_DnsRowStatus_Type())
dnsRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dnsRowStatus.setStatus(_A)
_DnsDomainName_Type=OctetString
_DnsDomainName_Object=MibScalar
dnsDomainName=_DnsDomainName_Object((1,3,6,1,4,1,9804,3,1,1,2,3,4),_DnsDomainName_Type())
dnsDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsDomainName.setStatus(_A)
_DnsSuffixCount_Type=Integer32
_DnsSuffixCount_Object=MibScalar
dnsSuffixCount=_DnsSuffixCount_Object((1,3,6,1,4,1,9804,3,1,1,2,3,5),_DnsSuffixCount_Type())
dnsSuffixCount.setMaxAccess(_F)
if mibBuilder.loadTexts:dnsSuffixCount.setStatus(_A)
_DnsSuffixTable_Object=MibTable
dnsSuffixTable=_DnsSuffixTable_Object((1,3,6,1,4,1,9804,3,1,1,2,3,6))
if mibBuilder.loadTexts:dnsSuffixTable.setStatus(_A)
_DnsSuffixEntry_Object=MibTableRow
dnsSuffixEntry=_DnsSuffixEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,3,6,1))
dnsSuffixEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:dnsSuffixEntry.setStatus(_A)
_DnsSuffixIndex_Type=Integer32
_DnsSuffixIndex_Object=MibTableColumn
dnsSuffixIndex=_DnsSuffixIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,3,6,1,1),_DnsSuffixIndex_Type())
dnsSuffixIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:dnsSuffixIndex.setStatus(_A)
_DnsSuffix_Type=OctetString
_DnsSuffix_Object=MibTableColumn
dnsSuffix=_DnsSuffix_Object((1,3,6,1,4,1,9804,3,1,1,2,3,6,1,2),_DnsSuffix_Type())
dnsSuffix.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsSuffix.setStatus(_A)
_DnsSuffixRowStatus_Type=RowStatus
_DnsSuffixRowStatus_Object=MibTableColumn
dnsSuffixRowStatus=_DnsSuffixRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,3,6,1,3),_DnsSuffixRowStatus_Type())
dnsSuffixRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dnsSuffixRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'lhnNusCommonDNSModule':lhnNusCommonDNSModule,'dnsNameserverCount':dnsNameserverCount,'dnsMode':dnsMode,'dnsNameserverTable':dnsNameserverTable,'dnsNameserverEntry':dnsNameserverEntry,_G:dnsIndex,'dnsServer':dnsServer,'dnsRowStatus':dnsRowStatus,'dnsDomainName':dnsDomainName,'dnsSuffixCount':dnsSuffixCount,'dnsSuffixTable':dnsSuffixTable,'dnsSuffixEntry':dnsSuffixEntry,_H:dnsSuffixIndex,'dnsSuffix':dnsSuffix,'dnsSuffixRowStatus':dnsSuffixRowStatus})