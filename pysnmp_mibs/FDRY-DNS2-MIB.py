_I='fdryDnsServerIndex'
_H='fdryDnsServerAddrType'
_G='fdryDns2DomainNameIndex'
_F='DisplayString'
_E='not-accessible'
_D='InetAddressType'
_C='read-create'
_B='FDRY-DNS2-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
fdryDns2MIB=ModuleIdentity((1,3,6,1,4,1,1991,1,1,3,34))
if mibBuilder.loadTexts:fdryDns2MIB.setRevisions(('2009-01-30 00:00','2017-08-07 00:00'))
_FdryDns2DomainName_ObjectIdentity=ObjectIdentity
fdryDns2DomainName=_FdryDns2DomainName_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,34,1))
_FdryDns2DomainNameTable_Object=MibTable
fdryDns2DomainNameTable=_FdryDns2DomainNameTable_Object((1,3,6,1,4,1,1991,1,1,3,34,1,1))
if mibBuilder.loadTexts:fdryDns2DomainNameTable.setStatus(_A)
_FdryDns2DomainNameEntry_Object=MibTableRow
fdryDns2DomainNameEntry=_FdryDns2DomainNameEntry_Object((1,3,6,1,4,1,1991,1,1,3,34,1,1,1))
fdryDns2DomainNameEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:fdryDns2DomainNameEntry.setStatus(_A)
_FdryDns2DomainNameIndex_Type=Unsigned32
_FdryDns2DomainNameIndex_Object=MibTableColumn
fdryDns2DomainNameIndex=_FdryDns2DomainNameIndex_Object((1,3,6,1,4,1,1991,1,1,3,34,1,1,1,1),_FdryDns2DomainNameIndex_Type())
fdryDns2DomainNameIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fdryDns2DomainNameIndex.setStatus(_A)
class _FdryDns2DomainNameAddrType_Type(InetAddressType):defaultValue=1
_FdryDns2DomainNameAddrType_Type.__name__=_D
_FdryDns2DomainNameAddrType_Object=MibTableColumn
fdryDns2DomainNameAddrType=_FdryDns2DomainNameAddrType_Object((1,3,6,1,4,1,1991,1,1,3,34,1,1,1,2),_FdryDns2DomainNameAddrType_Type())
fdryDns2DomainNameAddrType.setMaxAccess('read-only')
if mibBuilder.loadTexts:fdryDns2DomainNameAddrType.setStatus(_A)
class _FdryDns2DomainNameName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_FdryDns2DomainNameName_Type.__name__=_F
_FdryDns2DomainNameName_Object=MibTableColumn
fdryDns2DomainNameName=_FdryDns2DomainNameName_Object((1,3,6,1,4,1,1991,1,1,3,34,1,1,1,3),_FdryDns2DomainNameName_Type())
fdryDns2DomainNameName.setMaxAccess(_C)
if mibBuilder.loadTexts:fdryDns2DomainNameName.setStatus(_A)
_FdryDns2DomainNameRowStatus_Type=RowStatus
_FdryDns2DomainNameRowStatus_Object=MibTableColumn
fdryDns2DomainNameRowStatus=_FdryDns2DomainNameRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,34,1,1,1,4),_FdryDns2DomainNameRowStatus_Type())
fdryDns2DomainNameRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fdryDns2DomainNameRowStatus.setStatus(_A)
_FdryDnsServer_ObjectIdentity=ObjectIdentity
fdryDnsServer=_FdryDnsServer_ObjectIdentity((1,3,6,1,4,1,1991,1,1,3,34,2))
_FdryDnsServerTable_Object=MibTable
fdryDnsServerTable=_FdryDnsServerTable_Object((1,3,6,1,4,1,1991,1,1,3,34,2,1))
if mibBuilder.loadTexts:fdryDnsServerTable.setStatus(_A)
_FdryDnsServerEntry_Object=MibTableRow
fdryDnsServerEntry=_FdryDnsServerEntry_Object((1,3,6,1,4,1,1991,1,1,3,34,2,1,1))
fdryDnsServerEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:fdryDnsServerEntry.setStatus(_A)
class _FdryDnsServerAddrType_Type(InetAddressType):defaultValue=1
_FdryDnsServerAddrType_Type.__name__=_D
_FdryDnsServerAddrType_Object=MibTableColumn
fdryDnsServerAddrType=_FdryDnsServerAddrType_Object((1,3,6,1,4,1,1991,1,1,3,34,2,1,1,1),_FdryDnsServerAddrType_Type())
fdryDnsServerAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:fdryDnsServerAddrType.setStatus(_A)
_FdryDnsServerIndex_Type=Unsigned32
_FdryDnsServerIndex_Object=MibTableColumn
fdryDnsServerIndex=_FdryDnsServerIndex_Object((1,3,6,1,4,1,1991,1,1,3,34,2,1,1,2),_FdryDnsServerIndex_Type())
fdryDnsServerIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fdryDnsServerIndex.setStatus(_A)
_FdryDnsServerAddr_Type=InetAddress
_FdryDnsServerAddr_Object=MibTableColumn
fdryDnsServerAddr=_FdryDnsServerAddr_Object((1,3,6,1,4,1,1991,1,1,3,34,2,1,1,3),_FdryDnsServerAddr_Type())
fdryDnsServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:fdryDnsServerAddr.setStatus(_A)
_FdryDnsServerRowStatus_Type=RowStatus
_FdryDnsServerRowStatus_Object=MibTableColumn
fdryDnsServerRowStatus=_FdryDnsServerRowStatus_Object((1,3,6,1,4,1,1991,1,1,3,34,2,1,1,4),_FdryDnsServerRowStatus_Type())
fdryDnsServerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fdryDnsServerRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fdryDns2MIB':fdryDns2MIB,'fdryDns2DomainName':fdryDns2DomainName,'fdryDns2DomainNameTable':fdryDns2DomainNameTable,'fdryDns2DomainNameEntry':fdryDns2DomainNameEntry,_G:fdryDns2DomainNameIndex,'fdryDns2DomainNameAddrType':fdryDns2DomainNameAddrType,'fdryDns2DomainNameName':fdryDns2DomainNameName,'fdryDns2DomainNameRowStatus':fdryDns2DomainNameRowStatus,'fdryDnsServer':fdryDnsServer,'fdryDnsServerTable':fdryDnsServerTable,'fdryDnsServerEntry':fdryDnsServerEntry,_H:fdryDnsServerAddrType,_I:fdryDnsServerIndex,'fdryDnsServerAddr':fdryDnsServerAddr,'fdryDnsServerRowStatus':fdryDnsServerRowStatus})