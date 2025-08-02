_P='dnsHostXVrf'
_O='dnsHostXName'
_N='dnsHostXIPAddress'
_M='dnsNameServerXVrf'
_L='dnsNameServerXIPAddress'
_K='dnsDomainTblNameVrf'
_J='dnsHostName'
_I='dnsHostIPAddress'
_H='dnsNameServerIPAddress'
_G='Integer32'
_F='read-write'
_E='read-create'
_D='DisplayString'
_C='MAIPU-DNS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,ObjectName,ObjectSyntax,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','ObjectName','ObjectSyntax','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_D,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
dnsMib=ModuleIdentity((1,3,6,1,4,1,5651,3,109))
_DnsGlobal_ObjectIdentity=ObjectIdentity
dnsGlobal=_DnsGlobal_ObjectIdentity((1,3,6,1,4,1,5651,3,109,1))
class _DnsDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_DnsDomainName_Type.__name__=_D
_DnsDomainName_Object=MibScalar
dnsDomainName=_DnsDomainName_Object((1,3,6,1,4,1,5651,3,109,1,1),_DnsDomainName_Type())
dnsDomainName.setMaxAccess(_F)
if mibBuilder.loadTexts:dnsDomainName.setStatus(_A)
class _DnsDomainOrder_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('localfirst',1),('dnsfirst',2),('dnsonly',3)))
_DnsDomainOrder_Type.__name__=_G
_DnsDomainOrder_Object=MibScalar
dnsDomainOrder=_DnsDomainOrder_Object((1,3,6,1,4,1,5651,3,109,1,2),_DnsDomainOrder_Type())
dnsDomainOrder.setMaxAccess(_F)
if mibBuilder.loadTexts:dnsDomainOrder.setStatus(_A)
_DnsNameServerTable_Object=MibTable
dnsNameServerTable=_DnsNameServerTable_Object((1,3,6,1,4,1,5651,3,109,2))
if mibBuilder.loadTexts:dnsNameServerTable.setStatus(_A)
_DnsNameServerEntry_Object=MibTableRow
dnsNameServerEntry=_DnsNameServerEntry_Object((1,3,6,1,4,1,5651,3,109,2,1))
dnsNameServerEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:dnsNameServerEntry.setStatus(_A)
_DnsNameServerIPAddress_Type=IpAddress
_DnsNameServerIPAddress_Object=MibTableColumn
dnsNameServerIPAddress=_DnsNameServerIPAddress_Object((1,3,6,1,4,1,5651,3,109,2,1,1),_DnsNameServerIPAddress_Type())
dnsNameServerIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsNameServerIPAddress.setStatus(_A)
_DnsNameServerRowStatus_Type=RowStatus
_DnsNameServerRowStatus_Object=MibTableColumn
dnsNameServerRowStatus=_DnsNameServerRowStatus_Object((1,3,6,1,4,1,5651,3,109,2,1,2),_DnsNameServerRowStatus_Type())
dnsNameServerRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dnsNameServerRowStatus.setStatus(_A)
_DnsHostNameTable_Object=MibTable
dnsHostNameTable=_DnsHostNameTable_Object((1,3,6,1,4,1,5651,3,109,3))
if mibBuilder.loadTexts:dnsHostNameTable.setStatus(_A)
_DnsHostNameEntry_Object=MibTableRow
dnsHostNameEntry=_DnsHostNameEntry_Object((1,3,6,1,4,1,5651,3,109,3,1))
dnsHostNameEntry.setIndexNames((0,_C,_I),(0,_C,_J))
if mibBuilder.loadTexts:dnsHostNameEntry.setStatus(_A)
_DnsHostIPAddress_Type=IpAddress
_DnsHostIPAddress_Object=MibTableColumn
dnsHostIPAddress=_DnsHostIPAddress_Object((1,3,6,1,4,1,5651,3,109,3,1,1),_DnsHostIPAddress_Type())
dnsHostIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsHostIPAddress.setStatus(_A)
class _DnsHostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DnsHostName_Type.__name__=_D
_DnsHostName_Object=MibTableColumn
dnsHostName=_DnsHostName_Object((1,3,6,1,4,1,5651,3,109,3,1,2),_DnsHostName_Type())
dnsHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsHostName.setStatus(_A)
_DnsHostAlias_Type=TruthValue
_DnsHostAlias_Object=MibTableColumn
dnsHostAlias=_DnsHostAlias_Object((1,3,6,1,4,1,5651,3,109,3,1,3),_DnsHostAlias_Type())
dnsHostAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsHostAlias.setStatus(_A)
_DnsHostRawStatus_Type=RowStatus
_DnsHostRawStatus_Object=MibTableColumn
dnsHostRawStatus=_DnsHostRawStatus_Object((1,3,6,1,4,1,5651,3,109,3,1,4),_DnsHostRawStatus_Type())
dnsHostRawStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dnsHostRawStatus.setStatus(_A)
_DnsDomainNameTable_Object=MibTable
dnsDomainNameTable=_DnsDomainNameTable_Object((1,3,6,1,4,1,5651,3,109,4))
if mibBuilder.loadTexts:dnsDomainNameTable.setStatus(_A)
_DnsDomainNameEntry_Object=MibTableRow
dnsDomainNameEntry=_DnsDomainNameEntry_Object((1,3,6,1,4,1,5651,3,109,4,1))
dnsDomainNameEntry.setIndexNames((0,_C,_K))
if mibBuilder.loadTexts:dnsDomainNameEntry.setStatus(_A)
class _DnsDomainTblName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_DnsDomainTblName_Type.__name__=_D
_DnsDomainTblName_Object=MibTableColumn
dnsDomainTblName=_DnsDomainTblName_Object((1,3,6,1,4,1,5651,3,109,4,1,1),_DnsDomainTblName_Type())
dnsDomainTblName.setMaxAccess(_F)
if mibBuilder.loadTexts:dnsDomainTblName.setStatus(_A)
class _DnsDomainTblNameVrf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_DnsDomainTblNameVrf_Type.__name__=_D
_DnsDomainTblNameVrf_Object=MibTableColumn
dnsDomainTblNameVrf=_DnsDomainTblNameVrf_Object((1,3,6,1,4,1,5651,3,109,4,1,2),_DnsDomainTblNameVrf_Type())
dnsDomainTblNameVrf.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsDomainTblNameVrf.setStatus(_A)
_DnsNameServerXTable_Object=MibTable
dnsNameServerXTable=_DnsNameServerXTable_Object((1,3,6,1,4,1,5651,3,109,5))
if mibBuilder.loadTexts:dnsNameServerXTable.setStatus(_A)
_DnsNameServerXEntry_Object=MibTableRow
dnsNameServerXEntry=_DnsNameServerXEntry_Object((1,3,6,1,4,1,5651,3,109,5,1))
dnsNameServerXEntry.setIndexNames((0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:dnsNameServerXEntry.setStatus(_A)
_DnsNameServerXIPAddress_Type=IpAddress
_DnsNameServerXIPAddress_Object=MibTableColumn
dnsNameServerXIPAddress=_DnsNameServerXIPAddress_Object((1,3,6,1,4,1,5651,3,109,5,1,1),_DnsNameServerXIPAddress_Type())
dnsNameServerXIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsNameServerXIPAddress.setStatus(_A)
class _DnsNameServerXVrf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_DnsNameServerXVrf_Type.__name__=_D
_DnsNameServerXVrf_Object=MibTableColumn
dnsNameServerXVrf=_DnsNameServerXVrf_Object((1,3,6,1,4,1,5651,3,109,5,1,2),_DnsNameServerXVrf_Type())
dnsNameServerXVrf.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsNameServerXVrf.setStatus(_A)
_DnsNameServerXRowStatus_Type=RowStatus
_DnsNameServerXRowStatus_Object=MibTableColumn
dnsNameServerXRowStatus=_DnsNameServerXRowStatus_Object((1,3,6,1,4,1,5651,3,109,5,1,3),_DnsNameServerXRowStatus_Type())
dnsNameServerXRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dnsNameServerXRowStatus.setStatus(_A)
_DnsHostNameXTable_Object=MibTable
dnsHostNameXTable=_DnsHostNameXTable_Object((1,3,6,1,4,1,5651,3,109,6))
if mibBuilder.loadTexts:dnsHostNameXTable.setStatus(_A)
_DnsHostNameXEntry_Object=MibTableRow
dnsHostNameXEntry=_DnsHostNameXEntry_Object((1,3,6,1,4,1,5651,3,109,6,1))
dnsHostNameXEntry.setIndexNames((0,_C,_N),(0,_C,_O),(0,_C,_P))
if mibBuilder.loadTexts:dnsHostNameXEntry.setStatus(_A)
_DnsHostXIPAddress_Type=IpAddress
_DnsHostXIPAddress_Object=MibTableColumn
dnsHostXIPAddress=_DnsHostXIPAddress_Object((1,3,6,1,4,1,5651,3,109,6,1,1),_DnsHostXIPAddress_Type())
dnsHostXIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsHostXIPAddress.setStatus(_A)
class _DnsHostXName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_DnsHostXName_Type.__name__=_D
_DnsHostXName_Object=MibTableColumn
dnsHostXName=_DnsHostXName_Object((1,3,6,1,4,1,5651,3,109,6,1,2),_DnsHostXName_Type())
dnsHostXName.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsHostXName.setStatus(_A)
class _DnsHostXVrf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_DnsHostXVrf_Type.__name__=_D
_DnsHostXVrf_Object=MibTableColumn
dnsHostXVrf=_DnsHostXVrf_Object((1,3,6,1,4,1,5651,3,109,6,1,3),_DnsHostXVrf_Type())
dnsHostXVrf.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsHostXVrf.setStatus(_A)
_DnsHostXAlias_Type=TruthValue
_DnsHostXAlias_Object=MibTableColumn
dnsHostXAlias=_DnsHostXAlias_Object((1,3,6,1,4,1,5651,3,109,6,1,4),_DnsHostXAlias_Type())
dnsHostXAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:dnsHostXAlias.setStatus(_A)
_DnsHostXRawStatus_Type=RowStatus
_DnsHostXRawStatus_Object=MibTableColumn
dnsHostXRawStatus=_DnsHostXRawStatus_Object((1,3,6,1,4,1,5651,3,109,6,1,5),_DnsHostXRawStatus_Type())
dnsHostXRawStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dnsHostXRawStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'dnsMib':dnsMib,'dnsGlobal':dnsGlobal,'dnsDomainName':dnsDomainName,'dnsDomainOrder':dnsDomainOrder,'dnsNameServerTable':dnsNameServerTable,'dnsNameServerEntry':dnsNameServerEntry,_H:dnsNameServerIPAddress,'dnsNameServerRowStatus':dnsNameServerRowStatus,'dnsHostNameTable':dnsHostNameTable,'dnsHostNameEntry':dnsHostNameEntry,_I:dnsHostIPAddress,_J:dnsHostName,'dnsHostAlias':dnsHostAlias,'dnsHostRawStatus':dnsHostRawStatus,'dnsDomainNameTable':dnsDomainNameTable,'dnsDomainNameEntry':dnsDomainNameEntry,'dnsDomainTblName':dnsDomainTblName,_K:dnsDomainTblNameVrf,'dnsNameServerXTable':dnsNameServerXTable,'dnsNameServerXEntry':dnsNameServerXEntry,_L:dnsNameServerXIPAddress,_M:dnsNameServerXVrf,'dnsNameServerXRowStatus':dnsNameServerXRowStatus,'dnsHostNameXTable':dnsHostNameXTable,'dnsHostNameXEntry':dnsHostNameXEntry,_N:dnsHostXIPAddress,_O:dnsHostXName,_P:dnsHostXVrf,'dnsHostXAlias':dnsHostXAlias,'dnsHostXRawStatus':dnsHostXRawStatus})