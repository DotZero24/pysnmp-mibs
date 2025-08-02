_H='fsHttpRedirectionURL'
_G='ARICENT-HTTP-MIB'
_F='digest'
_E='default'
_D='DisplayString'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','RowStatus','TextualConvention')
fsHttpMIB=ModuleIdentity((1,3,6,1,4,1,29601,2,44))
if mibBuilder.loadTexts:fsHttpMIB.setRevisions(('2012-09-05 00:00',))
_FsHttpMIBObjects_ObjectIdentity=ObjectIdentity
fsHttpMIBObjects=_FsHttpMIBObjects_ObjectIdentity((1,3,6,1,4,1,29601,2,44,1))
_FutureHttpScalars_ObjectIdentity=ObjectIdentity
futureHttpScalars=_FutureHttpScalars_ObjectIdentity((1,3,6,1,4,1,29601,2,44,1,1))
class _FsHttpRedirectionStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_FsHttpRedirectionStatus_Type.__name__=_C
_FsHttpRedirectionStatus_Object=MibScalar
fsHttpRedirectionStatus=_FsHttpRedirectionStatus_Object((1,3,6,1,4,1,29601,2,44,1,1,1),_FsHttpRedirectionStatus_Type())
fsHttpRedirectionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHttpRedirectionStatus.setStatus(_A)
class _FsOperHttpAuthScheme_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('basic',1),(_F,2)))
_FsOperHttpAuthScheme_Type.__name__=_C
_FsOperHttpAuthScheme_Object=MibScalar
fsOperHttpAuthScheme=_FsOperHttpAuthScheme_Object((1,3,6,1,4,1,29601,2,44,1,1,2),_FsOperHttpAuthScheme_Type())
fsOperHttpAuthScheme.setMaxAccess('read-only')
if mibBuilder.loadTexts:fsOperHttpAuthScheme.setStatus(_A)
class _FsConfigHttpAuthScheme_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),('basic',1),(_F,2)))
_FsConfigHttpAuthScheme_Type.__name__=_C
_FsConfigHttpAuthScheme_Object=MibScalar
fsConfigHttpAuthScheme=_FsConfigHttpAuthScheme_Object((1,3,6,1,4,1,29601,2,44,1,1,3),_FsConfigHttpAuthScheme_Type())
fsConfigHttpAuthScheme.setMaxAccess(_B)
if mibBuilder.loadTexts:fsConfigHttpAuthScheme.setStatus(_A)
class _FsHttpRequestCount_Type(Integer32):defaultValue=0
_FsHttpRequestCount_Type.__name__=_C
_FsHttpRequestCount_Object=MibScalar
fsHttpRequestCount=_FsHttpRequestCount_Object((1,3,6,1,4,1,29601,2,44,1,1,4),_FsHttpRequestCount_Type())
fsHttpRequestCount.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHttpRequestCount.setStatus(_A)
class _FsHttpRequestDiscards_Type(Integer32):defaultValue=0
_FsHttpRequestDiscards_Type.__name__=_C
_FsHttpRequestDiscards_Object=MibScalar
fsHttpRequestDiscards=_FsHttpRequestDiscards_Object((1,3,6,1,4,1,29601,2,44,1,1,5),_FsHttpRequestDiscards_Type())
fsHttpRequestDiscards.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHttpRequestDiscards.setStatus(_A)
_FutureHttpTables_ObjectIdentity=ObjectIdentity
futureHttpTables=_FutureHttpTables_ObjectIdentity((1,3,6,1,4,1,29601,2,44,1,2))
_FsHttpRedirectionTable_Object=MibTable
fsHttpRedirectionTable=_FsHttpRedirectionTable_Object((1,3,6,1,4,1,29601,2,44,1,2,1))
if mibBuilder.loadTexts:fsHttpRedirectionTable.setStatus(_A)
_FsHttpRedirectionEntry_Object=MibTableRow
fsHttpRedirectionEntry=_FsHttpRedirectionEntry_Object((1,3,6,1,4,1,29601,2,44,1,2,1,1))
fsHttpRedirectionEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:fsHttpRedirectionEntry.setStatus(_A)
class _FsHttpRedirectionURL_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(100,100));fixedLength=100
_FsHttpRedirectionURL_Type.__name__=_D
_FsHttpRedirectionURL_Object=MibTableColumn
fsHttpRedirectionURL=_FsHttpRedirectionURL_Object((1,3,6,1,4,1,29601,2,44,1,2,1,1,1),_FsHttpRedirectionURL_Type())
fsHttpRedirectionURL.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:fsHttpRedirectionURL.setStatus(_A)
_FsHttpRedirectedSrvAddrType_Type=InetAddressType
_FsHttpRedirectedSrvAddrType_Object=MibTableColumn
fsHttpRedirectedSrvAddrType=_FsHttpRedirectedSrvAddrType_Object((1,3,6,1,4,1,29601,2,44,1,2,1,1,2),_FsHttpRedirectedSrvAddrType_Type())
fsHttpRedirectedSrvAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHttpRedirectedSrvAddrType.setStatus(_A)
_FsHttpRedirectedSrvIP_Type=InetAddress
_FsHttpRedirectedSrvIP_Object=MibTableColumn
fsHttpRedirectedSrvIP=_FsHttpRedirectedSrvIP_Object((1,3,6,1,4,1,29601,2,44,1,2,1,1,3),_FsHttpRedirectedSrvIP_Type())
fsHttpRedirectedSrvIP.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHttpRedirectedSrvIP.setStatus(_A)
_FsHttpRedirectedSrvDomainName_Type=DisplayString
_FsHttpRedirectedSrvDomainName_Object=MibTableColumn
fsHttpRedirectedSrvDomainName=_FsHttpRedirectedSrvDomainName_Object((1,3,6,1,4,1,29601,2,44,1,2,1,1,4),_FsHttpRedirectedSrvDomainName_Type())
fsHttpRedirectedSrvDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsHttpRedirectedSrvDomainName.setStatus(_A)
_FsHttpRedirectionEntryStatus_Type=RowStatus
_FsHttpRedirectionEntryStatus_Object=MibTableColumn
fsHttpRedirectionEntryStatus=_FsHttpRedirectionEntryStatus_Object((1,3,6,1,4,1,29601,2,44,1,2,1,1,5),_FsHttpRedirectionEntryStatus_Type())
fsHttpRedirectionEntryStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:fsHttpRedirectionEntryStatus.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'fsHttpMIB':fsHttpMIB,'fsHttpMIBObjects':fsHttpMIBObjects,'futureHttpScalars':futureHttpScalars,'fsHttpRedirectionStatus':fsHttpRedirectionStatus,'fsOperHttpAuthScheme':fsOperHttpAuthScheme,'fsConfigHttpAuthScheme':fsConfigHttpAuthScheme,'fsHttpRequestCount':fsHttpRequestCount,'fsHttpRequestDiscards':fsHttpRequestDiscards,'futureHttpTables':futureHttpTables,'fsHttpRedirectionTable':fsHttpRedirectionTable,'fsHttpRedirectionEntry':fsHttpRedirectionEntry,_H:fsHttpRedirectionURL,'fsHttpRedirectedSrvAddrType':fsHttpRedirectedSrvAddrType,'fsHttpRedirectedSrvIP':fsHttpRedirectedSrvIP,'fsHttpRedirectedSrvDomainName':fsHttpRedirectedSrvDomainName,'fsHttpRedirectionEntryStatus':fsHttpRedirectionEntryStatus})