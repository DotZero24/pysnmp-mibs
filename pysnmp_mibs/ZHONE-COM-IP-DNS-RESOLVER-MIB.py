_L='zhDnsResConfigEntry'
_K='zhDnsResHostsIpAddress'
_J='ZhoneRowStatus'
_I='rdIndex'
_H='ZHONE-COM-IP-RD-MIB'
_G='Integer32'
_F='ZHONE-COM-IP-DNS-RESOLVER-MIB'
_E='00000000'
_D='IpAddress'
_C='read-write'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,_D,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rdEntry,rdIndex=mibBuilder.importSymbols(_H,'rdEntry',_I)
zhoneIp,zhoneModules=mibBuilder.importSymbols('Zhone','zhoneIp','zhoneModules')
ZhoneAdminString,ZhoneRowStatus=mibBuilder.importSymbols('Zhone-TC','ZhoneAdminString',_J)
comIpDnsResolver=ModuleIdentity((1,3,6,1,4,1,5504,6,62))
if mibBuilder.loadTexts:comIpDnsResolver.setRevisions(('1900-09-11 16:08','1900-09-29 09:33'))
_DnsResolver_ObjectIdentity=ObjectIdentity
dnsResolver=_DnsResolver_ObjectIdentity((1,3,6,1,4,1,5504,4,1,12))
if mibBuilder.loadTexts:dnsResolver.setStatus(_A)
_ZhDnsResConfigImplementIdent_Type=ZhoneAdminString
_ZhDnsResConfigImplementIdent_Object=MibScalar
zhDnsResConfigImplementIdent=_ZhDnsResConfigImplementIdent_Object((1,3,6,1,4,1,5504,4,1,12,1),_ZhDnsResConfigImplementIdent_Type())
zhDnsResConfigImplementIdent.setMaxAccess('read-only')
if mibBuilder.loadTexts:zhDnsResConfigImplementIdent.setStatus(_A)
_ZhDnsResConfigTable_Object=MibTable
zhDnsResConfigTable=_ZhDnsResConfigTable_Object((1,3,6,1,4,1,5504,4,1,12,2))
if mibBuilder.loadTexts:zhDnsResConfigTable.setStatus(_A)
_ZhDnsResConfigEntry_Object=MibTableRow
zhDnsResConfigEntry=_ZhDnsResConfigEntry_Object((1,3,6,1,4,1,5504,4,1,12,2,1))
if mibBuilder.loadTexts:zhDnsResConfigEntry.setStatus(_A)
class _ZhDnsResConfigQueryOrder_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('hostsFirst',1),('dnsFirst',2),('dnsOnly',3)))
_ZhDnsResConfigQueryOrder_Type.__name__=_G
_ZhDnsResConfigQueryOrder_Object=MibTableColumn
zhDnsResConfigQueryOrder=_ZhDnsResConfigQueryOrder_Object((1,3,6,1,4,1,5504,4,1,12,2,1,1),_ZhDnsResConfigQueryOrder_Type())
zhDnsResConfigQueryOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:zhDnsResConfigQueryOrder.setStatus(_A)
_ZhDnsResConfigDomainName_Type=SnmpAdminString
_ZhDnsResConfigDomainName_Object=MibTableColumn
zhDnsResConfigDomainName=_ZhDnsResConfigDomainName_Object((1,3,6,1,4,1,5504,4,1,12,2,1,2),_ZhDnsResConfigDomainName_Type())
zhDnsResConfigDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:zhDnsResConfigDomainName.setStatus(_A)
class _ZhDnsResConfigFirstNameServer_Type(IpAddress):defaultHexValue=_E
_ZhDnsResConfigFirstNameServer_Type.__name__=_D
_ZhDnsResConfigFirstNameServer_Object=MibTableColumn
zhDnsResConfigFirstNameServer=_ZhDnsResConfigFirstNameServer_Object((1,3,6,1,4,1,5504,4,1,12,2,1,3),_ZhDnsResConfigFirstNameServer_Type())
zhDnsResConfigFirstNameServer.setMaxAccess(_C)
if mibBuilder.loadTexts:zhDnsResConfigFirstNameServer.setStatus(_A)
class _ZhDnsResConfigSecondNameServer_Type(IpAddress):defaultHexValue=_E
_ZhDnsResConfigSecondNameServer_Type.__name__=_D
_ZhDnsResConfigSecondNameServer_Object=MibTableColumn
zhDnsResConfigSecondNameServer=_ZhDnsResConfigSecondNameServer_Object((1,3,6,1,4,1,5504,4,1,12,2,1,4),_ZhDnsResConfigSecondNameServer_Type())
zhDnsResConfigSecondNameServer.setMaxAccess(_C)
if mibBuilder.loadTexts:zhDnsResConfigSecondNameServer.setStatus(_A)
class _ZhDnsResConfigThirdNameServer_Type(IpAddress):defaultHexValue=_E
_ZhDnsResConfigThirdNameServer_Type.__name__=_D
_ZhDnsResConfigThirdNameServer_Object=MibTableColumn
zhDnsResConfigThirdNameServer=_ZhDnsResConfigThirdNameServer_Object((1,3,6,1,4,1,5504,4,1,12,2,1,5),_ZhDnsResConfigThirdNameServer_Type())
zhDnsResConfigThirdNameServer.setMaxAccess(_C)
if mibBuilder.loadTexts:zhDnsResConfigThirdNameServer.setStatus(_A)
_ZhDnsResHostsTable_Object=MibTable
zhDnsResHostsTable=_ZhDnsResHostsTable_Object((1,3,6,1,4,1,5504,4,1,12,3))
if mibBuilder.loadTexts:zhDnsResHostsTable.setStatus(_A)
_ZhDnsResHostsEntry_Object=MibTableRow
zhDnsResHostsEntry=_ZhDnsResHostsEntry_Object((1,3,6,1,4,1,5504,4,1,12,3,1))
zhDnsResHostsEntry.setIndexNames((0,_H,_I),(0,_F,_K))
if mibBuilder.loadTexts:zhDnsResHostsEntry.setStatus(_A)
_ZhDnsResHostsIpAddress_Type=IpAddress
_ZhDnsResHostsIpAddress_Object=MibTableColumn
zhDnsResHostsIpAddress=_ZhDnsResHostsIpAddress_Object((1,3,6,1,4,1,5504,4,1,12,3,1,1),_ZhDnsResHostsIpAddress_Type())
zhDnsResHostsIpAddress.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zhDnsResHostsIpAddress.setStatus(_A)
_ZhDnsResHostsName_Type=SnmpAdminString
_ZhDnsResHostsName_Object=MibTableColumn
zhDnsResHostsName=_ZhDnsResHostsName_Object((1,3,6,1,4,1,5504,4,1,12,3,1,2),_ZhDnsResHostsName_Type())
zhDnsResHostsName.setMaxAccess(_B)
if mibBuilder.loadTexts:zhDnsResHostsName.setStatus(_A)
_ZhDnsResHostsAlias1_Type=SnmpAdminString
_ZhDnsResHostsAlias1_Object=MibTableColumn
zhDnsResHostsAlias1=_ZhDnsResHostsAlias1_Object((1,3,6,1,4,1,5504,4,1,12,3,1,3),_ZhDnsResHostsAlias1_Type())
zhDnsResHostsAlias1.setMaxAccess(_B)
if mibBuilder.loadTexts:zhDnsResHostsAlias1.setStatus(_A)
_ZhDnsResHostsAlias2_Type=SnmpAdminString
_ZhDnsResHostsAlias2_Object=MibTableColumn
zhDnsResHostsAlias2=_ZhDnsResHostsAlias2_Object((1,3,6,1,4,1,5504,4,1,12,3,1,4),_ZhDnsResHostsAlias2_Type())
zhDnsResHostsAlias2.setMaxAccess(_B)
if mibBuilder.loadTexts:zhDnsResHostsAlias2.setStatus(_A)
_ZhDnsResHostsAlias3_Type=SnmpAdminString
_ZhDnsResHostsAlias3_Object=MibTableColumn
zhDnsResHostsAlias3=_ZhDnsResHostsAlias3_Object((1,3,6,1,4,1,5504,4,1,12,3,1,5),_ZhDnsResHostsAlias3_Type())
zhDnsResHostsAlias3.setMaxAccess(_B)
if mibBuilder.loadTexts:zhDnsResHostsAlias3.setStatus(_A)
_ZhDnsResHostsAlias4_Type=SnmpAdminString
_ZhDnsResHostsAlias4_Object=MibTableColumn
zhDnsResHostsAlias4=_ZhDnsResHostsAlias4_Object((1,3,6,1,4,1,5504,4,1,12,3,1,6),_ZhDnsResHostsAlias4_Type())
zhDnsResHostsAlias4.setMaxAccess(_B)
if mibBuilder.loadTexts:zhDnsResHostsAlias4.setStatus(_A)
class _ZhDnsResHostsRowStatus_Type(ZhoneRowStatus):defaultValue=1
_ZhDnsResHostsRowStatus_Type.__name__=_J
_ZhDnsResHostsRowStatus_Object=MibTableColumn
zhDnsResHostsRowStatus=_ZhDnsResHostsRowStatus_Object((1,3,6,1,4,1,5504,4,1,12,3,1,7),_ZhDnsResHostsRowStatus_Type())
zhDnsResHostsRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:zhDnsResHostsRowStatus.setStatus(_A)
rdEntry.registerAugmentions((_F,_L))
zhDnsResConfigEntry.setIndexNames(*rdEntry.getIndexNames())
mibBuilder.exportSymbols(_F,**{'dnsResolver':dnsResolver,'zhDnsResConfigImplementIdent':zhDnsResConfigImplementIdent,'zhDnsResConfigTable':zhDnsResConfigTable,_L:zhDnsResConfigEntry,'zhDnsResConfigQueryOrder':zhDnsResConfigQueryOrder,'zhDnsResConfigDomainName':zhDnsResConfigDomainName,'zhDnsResConfigFirstNameServer':zhDnsResConfigFirstNameServer,'zhDnsResConfigSecondNameServer':zhDnsResConfigSecondNameServer,'zhDnsResConfigThirdNameServer':zhDnsResConfigThirdNameServer,'zhDnsResHostsTable':zhDnsResHostsTable,'zhDnsResHostsEntry':zhDnsResHostsEntry,_K:zhDnsResHostsIpAddress,'zhDnsResHostsName':zhDnsResHostsName,'zhDnsResHostsAlias1':zhDnsResHostsAlias1,'zhDnsResHostsAlias2':zhDnsResHostsAlias2,'zhDnsResHostsAlias3':zhDnsResHostsAlias3,'zhDnsResHostsAlias4':zhDnsResHostsAlias4,'zhDnsResHostsRowStatus':zhDnsResHostsRowStatus,'comIpDnsResolver':comIpDnsResolver})