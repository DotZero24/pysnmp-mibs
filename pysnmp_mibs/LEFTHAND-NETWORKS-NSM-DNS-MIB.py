_Q='lefthandNetworksNsmDnsGroup'
_P='dnsSuffixRowStatus'
_O='dnsRowStatus'
_N='dnsSuffix'
_M='dnsServer'
_L='dnsSuffixCount'
_K='dnsDomainName'
_J='dnsMode'
_I='dnsNameserverCount'
_H='dnsSuffixIndex'
_G='not-accessible'
_F='dnsIndex'
_E='Integer32'
_D='obsolete'
_C='read-only'
_B='LEFTHAND-NETWORKS-NSM-DNS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lhnModules,lhnNsm=mibBuilder.importSymbols('LEFTHAND-NETWORKS-GLOBAL-REG-MIB','lhnModules','lhnNsm')
lhnNsmDNS,=mibBuilder.importSymbols('LEFTHAND-NETWORKS-NSM-MIB','lhnNsmDNS')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
lhnNsmDNSModule=ModuleIdentity((1,3,6,1,4,1,9804,2,1,4))
if mibBuilder.loadTexts:lhnNsmDNSModule.setRevisions(('2013-11-14 00:00','2013-06-25 00:00','2012-09-04 00:00','2011-06-21 00:00','2010-09-07 00:00','2010-07-19 00:00','2009-11-20 00:00','2009-03-10 00:00','2008-01-24 00:00'))
_LhnNsmDNSModuleConformance_ObjectIdentity=ObjectIdentity
lhnNsmDNSModuleConformance=_LhnNsmDNSModuleConformance_ObjectIdentity((1,3,6,1,4,1,9804,2,1,4,1))
_LhnNsmDNSModuleCompliances_ObjectIdentity=ObjectIdentity
lhnNsmDNSModuleCompliances=_LhnNsmDNSModuleCompliances_ObjectIdentity((1,3,6,1,4,1,9804,2,1,4,1,1))
_LhnNsmDNSModuleGroups_ObjectIdentity=ObjectIdentity
lhnNsmDNSModuleGroups=_LhnNsmDNSModuleGroups_ObjectIdentity((1,3,6,1,4,1,9804,2,1,4,1,2))
_DnsNameserverCount_Type=Integer32
_DnsNameserverCount_Object=MibScalar
dnsNameserverCount=_DnsNameserverCount_Object((1,3,6,1,4,1,9804,3,1,1,2,3,1),_DnsNameserverCount_Type())
dnsNameserverCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dnsNameserverCount.setStatus(_A)
class _DnsMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('auto',2)))
_DnsMode_Type.__name__=_E
_DnsMode_Object=MibScalar
dnsMode=_DnsMode_Object((1,3,6,1,4,1,9804,3,1,1,2,3,2),_DnsMode_Type())
dnsMode.setMaxAccess(_C)
if mibBuilder.loadTexts:dnsMode.setStatus(_A)
_DnsNameserverTable_Object=MibTable
dnsNameserverTable=_DnsNameserverTable_Object((1,3,6,1,4,1,9804,3,1,1,2,3,3))
if mibBuilder.loadTexts:dnsNameserverTable.setStatus(_A)
_DnsNameserverEntry_Object=MibTableRow
dnsNameserverEntry=_DnsNameserverEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,3,3,1))
dnsNameserverEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:dnsNameserverEntry.setStatus(_A)
_DnsIndex_Type=Unsigned32
_DnsIndex_Object=MibTableColumn
dnsIndex=_DnsIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,3,3,1,1),_DnsIndex_Type())
dnsIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:dnsIndex.setStatus(_A)
_DnsServer_Type=DisplayString
_DnsServer_Object=MibTableColumn
dnsServer=_DnsServer_Object((1,3,6,1,4,1,9804,3,1,1,2,3,3,1,2),_DnsServer_Type())
dnsServer.setMaxAccess(_C)
if mibBuilder.loadTexts:dnsServer.setStatus(_A)
_DnsRowStatus_Type=RowStatus
_DnsRowStatus_Object=MibTableColumn
dnsRowStatus=_DnsRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,3,3,1,3),_DnsRowStatus_Type())
dnsRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dnsRowStatus.setStatus(_D)
_DnsDomainName_Type=DisplayString
_DnsDomainName_Object=MibScalar
dnsDomainName=_DnsDomainName_Object((1,3,6,1,4,1,9804,3,1,1,2,3,4),_DnsDomainName_Type())
dnsDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:dnsDomainName.setStatus(_A)
_DnsSuffixCount_Type=Integer32
_DnsSuffixCount_Object=MibScalar
dnsSuffixCount=_DnsSuffixCount_Object((1,3,6,1,4,1,9804,3,1,1,2,3,5),_DnsSuffixCount_Type())
dnsSuffixCount.setMaxAccess(_C)
if mibBuilder.loadTexts:dnsSuffixCount.setStatus(_A)
_DnsSuffixTable_Object=MibTable
dnsSuffixTable=_DnsSuffixTable_Object((1,3,6,1,4,1,9804,3,1,1,2,3,6))
if mibBuilder.loadTexts:dnsSuffixTable.setStatus(_A)
_DnsSuffixEntry_Object=MibTableRow
dnsSuffixEntry=_DnsSuffixEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,3,6,1))
dnsSuffixEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:dnsSuffixEntry.setStatus(_A)
_DnsSuffixIndex_Type=Unsigned32
_DnsSuffixIndex_Object=MibTableColumn
dnsSuffixIndex=_DnsSuffixIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,3,6,1,1),_DnsSuffixIndex_Type())
dnsSuffixIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:dnsSuffixIndex.setStatus(_A)
_DnsSuffix_Type=DisplayString
_DnsSuffix_Object=MibTableColumn
dnsSuffix=_DnsSuffix_Object((1,3,6,1,4,1,9804,3,1,1,2,3,6,1,2),_DnsSuffix_Type())
dnsSuffix.setMaxAccess(_C)
if mibBuilder.loadTexts:dnsSuffix.setStatus(_A)
_DnsSuffixRowStatus_Type=RowStatus
_DnsSuffixRowStatus_Object=MibTableColumn
dnsSuffixRowStatus=_DnsSuffixRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,3,6,1,3),_DnsSuffixRowStatus_Type())
dnsSuffixRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:dnsSuffixRowStatus.setStatus(_D)
lefthandNetworksNsmDnsGroup=ObjectGroup((1,3,6,1,4,1,9804,2,1,4,1,2,1))
lefthandNetworksNsmDnsGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:lefthandNetworksNsmDnsGroup.setStatus(_A)
lefthandNetworksNsmDnsGroupObsolete=ObjectGroup((1,3,6,1,4,1,9804,2,1,4,1,2,2))
lefthandNetworksNsmDnsGroupObsolete.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:lefthandNetworksNsmDnsGroupObsolete.setStatus(_D)
lefthandNetworksNsmDNSMibCompliance=ModuleCompliance((1,3,6,1,4,1,9804,2,1,4,1,1,1))
lefthandNetworksNsmDNSMibCompliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:lefthandNetworksNsmDNSMibCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lhnNsmDNSModule':lhnNsmDNSModule,'lhnNsmDNSModuleConformance':lhnNsmDNSModuleConformance,'lhnNsmDNSModuleCompliances':lhnNsmDNSModuleCompliances,'lefthandNetworksNsmDNSMibCompliance':lefthandNetworksNsmDNSMibCompliance,'lhnNsmDNSModuleGroups':lhnNsmDNSModuleGroups,_Q:lefthandNetworksNsmDnsGroup,'lefthandNetworksNsmDnsGroupObsolete':lefthandNetworksNsmDnsGroupObsolete,_I:dnsNameserverCount,_J:dnsMode,'dnsNameserverTable':dnsNameserverTable,'dnsNameserverEntry':dnsNameserverEntry,_F:dnsIndex,_M:dnsServer,_O:dnsRowStatus,_K:dnsDomainName,_L:dnsSuffixCount,'dnsSuffixTable':dnsSuffixTable,'dnsSuffixEntry':dnsSuffixEntry,_H:dnsSuffixIndex,_N:dnsSuffix,_P:dnsSuffixRowStatus})