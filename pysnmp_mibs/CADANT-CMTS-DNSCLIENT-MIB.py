_I='cadDnsClientDomainName'
_H='read-create'
_G='not-accessible'
_F='cadDnsClientServerIpAddr'
_E='read-write'
_D='TruthValue'
_C='Integer32'
_B='CADANT-CMTS-DNSCLIENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cadLayer3,=mibBuilder.importSymbols('CADANT-PRODUCTS-MIB','cadLayer3')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_D)
cadDnsClientMib=ModuleIdentity((1,3,6,1,4,1,4998,1,1,25,8))
if mibBuilder.loadTexts:cadDnsClientMib.setRevisions(('2003-07-14 00:00',))
_CadDnsClientObjects_ObjectIdentity=ObjectIdentity
cadDnsClientObjects=_CadDnsClientObjects_ObjectIdentity((1,3,6,1,4,1,4998,1,1,25,8,1))
class _CadDnsClientEnable_Type(TruthValue):defaultValue=1
_CadDnsClientEnable_Type.__name__=_D
_CadDnsClientEnable_Object=MibScalar
cadDnsClientEnable=_CadDnsClientEnable_Object((1,3,6,1,4,1,4998,1,1,25,8,1,1),_CadDnsClientEnable_Type())
cadDnsClientEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cadDnsClientEnable.setStatus(_A)
_CadDnsClientDefaultDomain_Type=DisplayString
_CadDnsClientDefaultDomain_Object=MibScalar
cadDnsClientDefaultDomain=_CadDnsClientDefaultDomain_Object((1,3,6,1,4,1,4998,1,1,25,8,1,2),_CadDnsClientDefaultDomain_Type())
cadDnsClientDefaultDomain.setMaxAccess(_E)
if mibBuilder.loadTexts:cadDnsClientDefaultDomain.setStatus(_A)
_CadDnsClientServerTable_Object=MibTable
cadDnsClientServerTable=_CadDnsClientServerTable_Object((1,3,6,1,4,1,4998,1,1,25,8,2))
if mibBuilder.loadTexts:cadDnsClientServerTable.setStatus(_A)
_CadDnsClientServerEntry_Object=MibTableRow
cadDnsClientServerEntry=_CadDnsClientServerEntry_Object((1,3,6,1,4,1,4998,1,1,25,8,2,1))
cadDnsClientServerEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:cadDnsClientServerEntry.setStatus(_A)
_CadDnsClientServerIpAddr_Type=IpAddress
_CadDnsClientServerIpAddr_Object=MibTableColumn
cadDnsClientServerIpAddr=_CadDnsClientServerIpAddr_Object((1,3,6,1,4,1,4998,1,1,25,8,2,1,1),_CadDnsClientServerIpAddr_Type())
cadDnsClientServerIpAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:cadDnsClientServerIpAddr.setStatus(_A)
class _CadDnsClientServerPrefId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6))
_CadDnsClientServerPrefId_Type.__name__=_C
_CadDnsClientServerPrefId_Object=MibTableColumn
cadDnsClientServerPrefId=_CadDnsClientServerPrefId_Object((1,3,6,1,4,1,4998,1,1,25,8,2,1,2),_CadDnsClientServerPrefId_Type())
cadDnsClientServerPrefId.setMaxAccess('read-only')
if mibBuilder.loadTexts:cadDnsClientServerPrefId.setStatus(_A)
_CadDnsClientServerRowStatus_Type=RowStatus
_CadDnsClientServerRowStatus_Object=MibTableColumn
cadDnsClientServerRowStatus=_CadDnsClientServerRowStatus_Object((1,3,6,1,4,1,4998,1,1,25,8,2,1,3),_CadDnsClientServerRowStatus_Type())
cadDnsClientServerRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:cadDnsClientServerRowStatus.setStatus(_A)
_CadDnsClientDomainNameTable_Object=MibTable
cadDnsClientDomainNameTable=_CadDnsClientDomainNameTable_Object((1,3,6,1,4,1,4998,1,1,25,8,3))
if mibBuilder.loadTexts:cadDnsClientDomainNameTable.setStatus(_A)
_CadDnsClientDomainNameEntry_Object=MibTableRow
cadDnsClientDomainNameEntry=_CadDnsClientDomainNameEntry_Object((1,3,6,1,4,1,4998,1,1,25,8,3,1))
cadDnsClientDomainNameEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:cadDnsClientDomainNameEntry.setStatus(_A)
_CadDnsClientDomainName_Type=DisplayString
_CadDnsClientDomainName_Object=MibTableColumn
cadDnsClientDomainName=_CadDnsClientDomainName_Object((1,3,6,1,4,1,4998,1,1,25,8,3,1,1),_CadDnsClientDomainName_Type())
cadDnsClientDomainName.setMaxAccess(_G)
if mibBuilder.loadTexts:cadDnsClientDomainName.setStatus(_A)
_CadDnsClientDomainNameRowStatus_Type=RowStatus
_CadDnsClientDomainNameRowStatus_Object=MibTableColumn
cadDnsClientDomainNameRowStatus=_CadDnsClientDomainNameRowStatus_Object((1,3,6,1,4,1,4998,1,1,25,8,3,1,2),_CadDnsClientDomainNameRowStatus_Type())
cadDnsClientDomainNameRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:cadDnsClientDomainNameRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cadDnsClientMib':cadDnsClientMib,'cadDnsClientObjects':cadDnsClientObjects,'cadDnsClientEnable':cadDnsClientEnable,'cadDnsClientDefaultDomain':cadDnsClientDefaultDomain,'cadDnsClientServerTable':cadDnsClientServerTable,'cadDnsClientServerEntry':cadDnsClientServerEntry,_F:cadDnsClientServerIpAddr,'cadDnsClientServerPrefId':cadDnsClientServerPrefId,'cadDnsClientServerRowStatus':cadDnsClientServerRowStatus,'cadDnsClientDomainNameTable':cadDnsClientDomainNameTable,'cadDnsClientDomainNameEntry':cadDnsClientDomainNameEntry,_I:cadDnsClientDomainName,'cadDnsClientDomainNameRowStatus':cadDnsClientDomainNameRowStatus})