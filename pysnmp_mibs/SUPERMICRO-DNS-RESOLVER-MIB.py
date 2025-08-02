_M='fsDnsQueryIndex'
_L='fsDnsDomainNameIndex'
_K='fsDnsNameServerIndex'
_J='not-accessible'
_I='DisplayString'
_H='Unsigned32'
_G='InetAddress'
_F='SUPERMICRO-DNS-RESOLVER-MIB'
_E='Integer32'
_D='read-create'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_G,'InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'enterprises','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','RowStatus','TextualConvention')
fsDns=ModuleIdentity((1,3,6,1,4,1,10876,101,2,99))
if mibBuilder.loadTexts:fsDns.setRevisions(('2012-09-05 00:00',))
_FsDnsSystem_ObjectIdentity=ObjectIdentity
fsDnsSystem=_FsDnsSystem_ObjectIdentity((1,3,6,1,4,1,10876,101,2,99,1))
class _FsDnsSystemControl_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('start',1),('shutdown',2)))
_FsDnsSystemControl_Type.__name__=_E
_FsDnsSystemControl_Object=MibScalar
fsDnsSystemControl=_FsDnsSystemControl_Object((1,3,6,1,4,1,10876,101,2,99,1,1),_FsDnsSystemControl_Type())
fsDnsSystemControl.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDnsSystemControl.setStatus(_A)
class _FsDnsModuleStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_FsDnsModuleStatus_Type.__name__=_E
_FsDnsModuleStatus_Object=MibScalar
fsDnsModuleStatus=_FsDnsModuleStatus_Object((1,3,6,1,4,1,10876,101,2,99,1,2),_FsDnsModuleStatus_Type())
fsDnsModuleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDnsModuleStatus.setStatus(_A)
class _FsDnsTraceOption_Type(Integer32):defaultValue=0
_FsDnsTraceOption_Type.__name__=_E
_FsDnsTraceOption_Object=MibScalar
fsDnsTraceOption=_FsDnsTraceOption_Object((1,3,6,1,4,1,10876,101,2,99,1,3),_FsDnsTraceOption_Type())
fsDnsTraceOption.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDnsTraceOption.setStatus(_A)
class _FsDnsQueryRetryCount_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_FsDnsQueryRetryCount_Type.__name__=_H
_FsDnsQueryRetryCount_Object=MibScalar
fsDnsQueryRetryCount=_FsDnsQueryRetryCount_Object((1,3,6,1,4,1,10876,101,2,99,1,4),_FsDnsQueryRetryCount_Type())
fsDnsQueryRetryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDnsQueryRetryCount.setStatus(_A)
class _FsDnsQueryTimeOut_Type(Unsigned32):defaultValue=5;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_FsDnsQueryTimeOut_Type.__name__=_H
_FsDnsQueryTimeOut_Object=MibScalar
fsDnsQueryTimeOut=_FsDnsQueryTimeOut_Object((1,3,6,1,4,1,10876,101,2,99,1,5),_FsDnsQueryTimeOut_Type())
fsDnsQueryTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDnsQueryTimeOut.setStatus(_A)
_FsDnsNameServer_ObjectIdentity=ObjectIdentity
fsDnsNameServer=_FsDnsNameServer_ObjectIdentity((1,3,6,1,4,1,10876,101,2,99,2))
_FsDnsNameServerTable_Object=MibTable
fsDnsNameServerTable=_FsDnsNameServerTable_Object((1,3,6,1,4,1,10876,101,2,99,2,1))
if mibBuilder.loadTexts:fsDnsNameServerTable.setStatus(_A)
_FsDnsNameServerEntry_Object=MibTableRow
fsDnsNameServerEntry=_FsDnsNameServerEntry_Object((1,3,6,1,4,1,10876,101,2,99,2,1,1))
fsDnsNameServerEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:fsDnsNameServerEntry.setStatus(_A)
_FsDnsNameServerIndex_Type=Unsigned32
_FsDnsNameServerIndex_Object=MibTableColumn
fsDnsNameServerIndex=_FsDnsNameServerIndex_Object((1,3,6,1,4,1,10876,101,2,99,2,1,1,1),_FsDnsNameServerIndex_Type())
fsDnsNameServerIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:fsDnsNameServerIndex.setStatus(_A)
_FsDnsServerIPAddressType_Type=InetAddressType
_FsDnsServerIPAddressType_Object=MibTableColumn
fsDnsServerIPAddressType=_FsDnsServerIPAddressType_Object((1,3,6,1,4,1,10876,101,2,99,2,1,1,2),_FsDnsServerIPAddressType_Type())
fsDnsServerIPAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDnsServerIPAddressType.setStatus(_A)
class _FsDnsServerIPAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,16))
_FsDnsServerIPAddress_Type.__name__=_G
_FsDnsServerIPAddress_Object=MibTableColumn
fsDnsServerIPAddress=_FsDnsServerIPAddress_Object((1,3,6,1,4,1,10876,101,2,99,2,1,1,3),_FsDnsServerIPAddress_Type())
fsDnsServerIPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDnsServerIPAddress.setStatus(_A)
_FsDnsNameServerRowStatus_Type=RowStatus
_FsDnsNameServerRowStatus_Object=MibTableColumn
fsDnsNameServerRowStatus=_FsDnsNameServerRowStatus_Object((1,3,6,1,4,1,10876,101,2,99,2,1,1,4),_FsDnsNameServerRowStatus_Type())
fsDnsNameServerRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDnsNameServerRowStatus.setStatus(_A)
_FsDnsDomain_ObjectIdentity=ObjectIdentity
fsDnsDomain=_FsDnsDomain_ObjectIdentity((1,3,6,1,4,1,10876,101,2,99,3))
_FsDnsDomainNameTable_Object=MibTable
fsDnsDomainNameTable=_FsDnsDomainNameTable_Object((1,3,6,1,4,1,10876,101,2,99,3,1))
if mibBuilder.loadTexts:fsDnsDomainNameTable.setStatus(_A)
_FsDnsDomainNameEntry_Object=MibTableRow
fsDnsDomainNameEntry=_FsDnsDomainNameEntry_Object((1,3,6,1,4,1,10876,101,2,99,3,1,1))
fsDnsDomainNameEntry.setIndexNames((0,_F,_L))
if mibBuilder.loadTexts:fsDnsDomainNameEntry.setStatus(_A)
_FsDnsDomainNameIndex_Type=Unsigned32
_FsDnsDomainNameIndex_Object=MibTableColumn
fsDnsDomainNameIndex=_FsDnsDomainNameIndex_Object((1,3,6,1,4,1,10876,101,2,99,3,1,1,1),_FsDnsDomainNameIndex_Type())
fsDnsDomainNameIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:fsDnsDomainNameIndex.setStatus(_A)
class _FsDnsDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_FsDnsDomainName_Type.__name__=_I
_FsDnsDomainName_Object=MibTableColumn
fsDnsDomainName=_FsDnsDomainName_Object((1,3,6,1,4,1,10876,101,2,99,3,1,1,2),_FsDnsDomainName_Type())
fsDnsDomainName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDnsDomainName.setStatus(_A)
_FsDnsDomainNameRowStatus_Type=RowStatus
_FsDnsDomainNameRowStatus_Object=MibTableColumn
fsDnsDomainNameRowStatus=_FsDnsDomainNameRowStatus_Object((1,3,6,1,4,1,10876,101,2,99,3,1,1,3),_FsDnsDomainNameRowStatus_Type())
fsDnsDomainNameRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDnsDomainNameRowStatus.setStatus(_A)
_FsDnsQuery_ObjectIdentity=ObjectIdentity
fsDnsQuery=_FsDnsQuery_ObjectIdentity((1,3,6,1,4,1,10876,101,2,99,4))
_FsDnsQueryTable_Object=MibTable
fsDnsQueryTable=_FsDnsQueryTable_Object((1,3,6,1,4,1,10876,101,2,99,4,1))
if mibBuilder.loadTexts:fsDnsQueryTable.setStatus(_A)
_FsDnsQueryEntry_Object=MibTableRow
fsDnsQueryEntry=_FsDnsQueryEntry_Object((1,3,6,1,4,1,10876,101,2,99,4,1,1))
fsDnsQueryEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:fsDnsQueryEntry.setStatus(_A)
_FsDnsQueryIndex_Type=Unsigned32
_FsDnsQueryIndex_Object=MibTableColumn
fsDnsQueryIndex=_FsDnsQueryIndex_Object((1,3,6,1,4,1,10876,101,2,99,4,1,1,1),_FsDnsQueryIndex_Type())
fsDnsQueryIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:fsDnsQueryIndex.setStatus(_A)
class _FsDnsQueryName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_FsDnsQueryName_Type.__name__=_I
_FsDnsQueryName_Object=MibTableColumn
fsDnsQueryName=_FsDnsQueryName_Object((1,3,6,1,4,1,10876,101,2,99,4,1,1,2),_FsDnsQueryName_Type())
fsDnsQueryName.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDnsQueryName.setStatus(_A)
_FsDnsQueryNSAddressType_Type=InetAddressType
_FsDnsQueryNSAddressType_Object=MibTableColumn
fsDnsQueryNSAddressType=_FsDnsQueryNSAddressType_Object((1,3,6,1,4,1,10876,101,2,99,4,1,1,3),_FsDnsQueryNSAddressType_Type())
fsDnsQueryNSAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDnsQueryNSAddressType.setStatus(_A)
class _FsDnsQueryNSAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,16))
_FsDnsQueryNSAddress_Type.__name__=_G
_FsDnsQueryNSAddress_Object=MibTableColumn
fsDnsQueryNSAddress=_FsDnsQueryNSAddress_Object((1,3,6,1,4,1,10876,101,2,99,4,1,1,4),_FsDnsQueryNSAddress_Type())
fsDnsQueryNSAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDnsQueryNSAddress.setStatus(_A)
_FsDnsStatistics_ObjectIdentity=ObjectIdentity
fsDnsStatistics=_FsDnsStatistics_ObjectIdentity((1,3,6,1,4,1,10876,101,2,99,5))
_FsDnsQueriesSent_Type=Counter32
_FsDnsQueriesSent_Object=MibScalar
fsDnsQueriesSent=_FsDnsQueriesSent_Object((1,3,6,1,4,1,10876,101,2,99,5,1),_FsDnsQueriesSent_Type())
fsDnsQueriesSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDnsQueriesSent.setStatus(_A)
_FsDnsResponseReceived_Type=Counter32
_FsDnsResponseReceived_Object=MibScalar
fsDnsResponseReceived=_FsDnsResponseReceived_Object((1,3,6,1,4,1,10876,101,2,99,5,2),_FsDnsResponseReceived_Type())
fsDnsResponseReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDnsResponseReceived.setStatus(_A)
_FsDnsDroppedResponse_Type=Counter32
_FsDnsDroppedResponse_Object=MibScalar
fsDnsDroppedResponse=_FsDnsDroppedResponse_Object((1,3,6,1,4,1,10876,101,2,99,5,3),_FsDnsDroppedResponse_Type())
fsDnsDroppedResponse.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDnsDroppedResponse.setStatus(_A)
_FsDnsUnAnsweredQueries_Type=Counter32
_FsDnsUnAnsweredQueries_Object=MibScalar
fsDnsUnAnsweredQueries=_FsDnsUnAnsweredQueries_Object((1,3,6,1,4,1,10876,101,2,99,5,4),_FsDnsUnAnsweredQueries_Type())
fsDnsUnAnsweredQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDnsUnAnsweredQueries.setStatus(_A)
_FsDnsFailedQueries_Type=Counter32
_FsDnsFailedQueries_Object=MibScalar
fsDnsFailedQueries=_FsDnsFailedQueries_Object((1,3,6,1,4,1,10876,101,2,99,5,5),_FsDnsFailedQueries_Type())
fsDnsFailedQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDnsFailedQueries.setStatus(_A)
_FsDnsReTransQueries_Type=Counter32
_FsDnsReTransQueries_Object=MibScalar
fsDnsReTransQueries=_FsDnsReTransQueries_Object((1,3,6,1,4,1,10876,101,2,99,5,6),_FsDnsReTransQueries_Type())
fsDnsReTransQueries.setMaxAccess(_B)
if mibBuilder.loadTexts:fsDnsReTransQueries.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'fsDns':fsDns,'fsDnsSystem':fsDnsSystem,'fsDnsSystemControl':fsDnsSystemControl,'fsDnsModuleStatus':fsDnsModuleStatus,'fsDnsTraceOption':fsDnsTraceOption,'fsDnsQueryRetryCount':fsDnsQueryRetryCount,'fsDnsQueryTimeOut':fsDnsQueryTimeOut,'fsDnsNameServer':fsDnsNameServer,'fsDnsNameServerTable':fsDnsNameServerTable,'fsDnsNameServerEntry':fsDnsNameServerEntry,_K:fsDnsNameServerIndex,'fsDnsServerIPAddressType':fsDnsServerIPAddressType,'fsDnsServerIPAddress':fsDnsServerIPAddress,'fsDnsNameServerRowStatus':fsDnsNameServerRowStatus,'fsDnsDomain':fsDnsDomain,'fsDnsDomainNameTable':fsDnsDomainNameTable,'fsDnsDomainNameEntry':fsDnsDomainNameEntry,_L:fsDnsDomainNameIndex,'fsDnsDomainName':fsDnsDomainName,'fsDnsDomainNameRowStatus':fsDnsDomainNameRowStatus,'fsDnsQuery':fsDnsQuery,'fsDnsQueryTable':fsDnsQueryTable,'fsDnsQueryEntry':fsDnsQueryEntry,_M:fsDnsQueryIndex,'fsDnsQueryName':fsDnsQueryName,'fsDnsQueryNSAddressType':fsDnsQueryNSAddressType,'fsDnsQueryNSAddress':fsDnsQueryNSAddress,'fsDnsStatistics':fsDnsStatistics,'fsDnsQueriesSent':fsDnsQueriesSent,'fsDnsResponseReceived':fsDnsResponseReceived,'fsDnsDroppedResponse':fsDnsDroppedResponse,'fsDnsUnAnsweredQueries':fsDnsUnAnsweredQueries,'fsDnsFailedQueries':fsDnsFailedQueries,'fsDnsReTransQueries':fsDnsReTransQueries})