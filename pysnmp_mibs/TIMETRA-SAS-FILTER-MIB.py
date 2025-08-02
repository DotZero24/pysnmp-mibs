_G='tIPv6FilterExtnEntry'
_F='tIPFilterExtnEntry'
_E='read-create'
_D='TruthValue'
_C='Integer32'
_B='TIMETRA-SAS-FILTER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddressIPv6,InetAddressPrefixLength=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv6','InetAddressPrefixLength')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,Opaque,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','Opaque','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowPointer,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowPointer','RowStatus','TextualConvention','TimeStamp',_D)
tIPFilterEntry,tIPv6FilterEntry=mibBuilder.importSymbols('TIMETRA-FILTER-MIB','tIPFilterEntry','tIPv6FilterEntry')
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
timetraSASConfs,timetraSASModules,timetraSASNotifyPrefix,timetraSASObjs=mibBuilder.importSymbols('TIMETRA-SAS-GLOBAL-MIB','timetraSASConfs','timetraSASModules','timetraSASNotifyPrefix','timetraSASObjs')
Dot1PPriority,IpAddressPrefixLength,SdpBindId,ServiceAccessPoint,TDSCPFilterActionValue,TDSCPNameOrEmpty,TFrameType,TIpOption,TIpProtocol,TItemDescription,TNamedItem,TNamedItemOrEmpty,TTcpUdpPort,TTcpUdpPortOperator,TmnxAdminState,TmnxEncapVal,TmnxOperState,TmnxPortID,TmnxServId=mibBuilder.importSymbols('TIMETRA-TC-MIB','Dot1PPriority','IpAddressPrefixLength','SdpBindId','ServiceAccessPoint','TDSCPFilterActionValue','TDSCPNameOrEmpty','TFrameType','TIpOption','TIpProtocol','TItemDescription','TNamedItem','TNamedItemOrEmpty','TTcpUdpPort','TTcpUdpPortOperator','TmnxAdminState','TmnxEncapVal','TmnxOperState','TmnxPortID','TmnxServId')
timetraSASFilterMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,6,2,1,1,16))
if mibBuilder.loadTexts:timetraSASFilterMIBModule.setRevisions(('1912-04-01 00:00',))
_TmnxSASFilterObjs_ObjectIdentity=ObjectIdentity
tmnxSASFilterObjs=_TmnxSASFilterObjs_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,21))
_TSASFilterObjects_ObjectIdentity=ObjectIdentity
tSASFilterObjects=_TSASFilterObjects_ObjectIdentity((1,3,6,1,4,1,6527,6,2,2,2,21,1))
_TIPFilterExtnTable_Object=MibTable
tIPFilterExtnTable=_TIPFilterExtnTable_Object((1,3,6,1,4,1,6527,6,2,2,2,21,1,1))
if mibBuilder.loadTexts:tIPFilterExtnTable.setStatus(_A)
_TIPFilterExtnEntry_Object=MibTableRow
tIPFilterExtnEntry=_TIPFilterExtnEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,21,1,1,1))
if mibBuilder.loadTexts:tIPFilterExtnEntry.setStatus(_A)
class _TFilterUseIpv6Resource_Type(TruthValue):defaultValue=2
_TFilterUseIpv6Resource_Type.__name__=_D
_TFilterUseIpv6Resource_Object=MibTableColumn
tFilterUseIpv6Resource=_TFilterUseIpv6Resource_Object((1,3,6,1,4,1,6527,6,2,2,2,21,1,1,1,1),_TFilterUseIpv6Resource_Type())
tFilterUseIpv6Resource.setMaxAccess(_E)
if mibBuilder.loadTexts:tFilterUseIpv6Resource.setStatus(_A)
_TIPv6FilterExtnTable_Object=MibTable
tIPv6FilterExtnTable=_TIPv6FilterExtnTable_Object((1,3,6,1,4,1,6527,6,2,2,2,21,1,2))
if mibBuilder.loadTexts:tIPv6FilterExtnTable.setStatus(_A)
_TIPv6FilterExtnEntry_Object=MibTableRow
tIPv6FilterExtnEntry=_TIPv6FilterExtnEntry_Object((1,3,6,1,4,1,6527,6,2,2,2,21,1,2,1))
if mibBuilder.loadTexts:tIPv6FilterExtnEntry.setStatus(_A)
class _TFilter64Bitsor128_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ipv6128',1),('ipv664',2)))
_TFilter64Bitsor128_Type.__name__=_C
_TFilter64Bitsor128_Object=MibTableColumn
tFilter64Bitsor128=_TFilter64Bitsor128_Object((1,3,6,1,4,1,6527,6,2,2,2,21,1,2,1,1),_TFilter64Bitsor128_Type())
tFilter64Bitsor128.setMaxAccess(_E)
if mibBuilder.loadTexts:tFilter64Bitsor128.setStatus(_A)
tIPFilterEntry.registerAugmentions((_B,_F))
tIPFilterExtnEntry.setIndexNames(*tIPFilterEntry.getIndexNames())
tIPv6FilterEntry.registerAugmentions((_B,_G))
tIPv6FilterExtnEntry.setIndexNames(*tIPv6FilterEntry.getIndexNames())
mibBuilder.exportSymbols(_B,**{'timetraSASFilterMIBModule':timetraSASFilterMIBModule,'tmnxSASFilterObjs':tmnxSASFilterObjs,'tSASFilterObjects':tSASFilterObjects,'tIPFilterExtnTable':tIPFilterExtnTable,_F:tIPFilterExtnEntry,'tFilterUseIpv6Resource':tFilterUseIpv6Resource,'tIPv6FilterExtnTable':tIPv6FilterExtnTable,_G:tIPv6FilterExtnEntry,'tFilter64Bitsor128':tFilter64Bitsor128})