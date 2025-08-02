_I='read-write'
_H='atDNSServerIndex'
_G='AT-DNS-CLIENT-MIB'
_F='read-only'
_E='RowStatus'
_D='IpAddress'
_C='InetAddressType'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
modules,=mibBuilder.importSymbols('AT-SMI-MIB','modules')
InetAddressType,=mibBuilder.importSymbols('INET-ADDRESS-MIB',_C)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,_D,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress',_E,'TextualConvention')
atDNSClient=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,501,1))
if mibBuilder.loadTexts:atDNSClient.setRevisions(('2010-06-14 04:45','2008-09-18 12:00'))
_AtDns_ObjectIdentity=ObjectIdentity
atDns=_AtDns_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,501))
if mibBuilder.loadTexts:atDns.setStatus(_A)
class _AtDNSServerIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_AtDNSServerIndexNext_Type.__name__=_B
_AtDNSServerIndexNext_Object=MibScalar
atDNSServerIndexNext=_AtDNSServerIndexNext_Object((1,3,6,1,4,1,207,8,4,4,4,501,1,1),_AtDNSServerIndexNext_Type())
atDNSServerIndexNext.setMaxAccess(_F)
if mibBuilder.loadTexts:atDNSServerIndexNext.setStatus(_A)
_AtDNSServerTable_Object=MibTable
atDNSServerTable=_AtDNSServerTable_Object((1,3,6,1,4,1,207,8,4,4,4,501,1,2))
if mibBuilder.loadTexts:atDNSServerTable.setStatus(_A)
_AtDNSServerEntry_Object=MibTableRow
atDNSServerEntry=_AtDNSServerEntry_Object((1,3,6,1,4,1,207,8,4,4,4,501,1,2,1))
atDNSServerEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:atDNSServerEntry.setStatus(_A)
class _AtDNSServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtDNSServerIndex_Type.__name__=_B
_AtDNSServerIndex_Object=MibTableColumn
atDNSServerIndex=_AtDNSServerIndex_Object((1,3,6,1,4,1,207,8,4,4,4,501,1,2,1,1),_AtDNSServerIndex_Type())
atDNSServerIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:atDNSServerIndex.setStatus(_A)
class _AtDNSServerAddrType_Type(InetAddressType):defaultValue=1
_AtDNSServerAddrType_Type.__name__=_C
_AtDNSServerAddrType_Object=MibTableColumn
atDNSServerAddrType=_AtDNSServerAddrType_Object((1,3,6,1,4,1,207,8,4,4,4,501,1,2,1,2),_AtDNSServerAddrType_Type())
atDNSServerAddrType.setMaxAccess(_F)
if mibBuilder.loadTexts:atDNSServerAddrType.setStatus(_A)
class _AtDNSServerAddr_Type(IpAddress):defaultHexValue='00000000'
_AtDNSServerAddr_Type.__name__=_D
_AtDNSServerAddr_Object=MibTableColumn
atDNSServerAddr=_AtDNSServerAddr_Object((1,3,6,1,4,1,207,8,4,4,4,501,1,2,1,3),_AtDNSServerAddr_Type())
atDNSServerAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:atDNSServerAddr.setStatus(_A)
class _AtDNSServerStatus_Type(RowStatus):defaultValue=1
_AtDNSServerStatus_Type.__name__=_E
_AtDNSServerStatus_Object=MibTableColumn
atDNSServerStatus=_AtDNSServerStatus_Object((1,3,6,1,4,1,207,8,4,4,4,501,1,2,1,4),_AtDNSServerStatus_Type())
atDNSServerStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:atDNSServerStatus.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'atDns':atDns,'atDNSClient':atDNSClient,'atDNSServerIndexNext':atDNSServerIndexNext,'atDNSServerTable':atDNSServerTable,'atDNSServerEntry':atDNSServerEntry,_H:atDNSServerIndex,'atDNSServerAddrType':atDNSServerAddrType,'atDNSServerAddr':atDNSServerAddr,'atDNSServerStatus':atDNSServerStatus})