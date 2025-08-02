_H='read-write'
_G='vj-tcp'
_F='none'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ppp,=mibBuilder.importSymbols('PPP-LCP-MIB','ppp')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_PppIp_ObjectIdentity=ObjectIdentity
pppIp=_PppIp_ObjectIdentity((1,3,6,1,2,1,10,23,3))
_PppIpTable_Object=MibTable
pppIpTable=_PppIpTable_Object((1,3,6,1,2,1,10,23,3,1))
if mibBuilder.loadTexts:pppIpTable.setStatus(_A)
_PppIpEntry_Object=MibTableRow
pppIpEntry=_PppIpEntry_Object((1,3,6,1,2,1,10,23,3,1,1))
pppIpEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:pppIpEntry.setStatus(_A)
class _PppIpOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('opened',1),('not-opened',2)))
_PppIpOperStatus_Type.__name__=_B
_PppIpOperStatus_Object=MibTableColumn
pppIpOperStatus=_PppIpOperStatus_Object((1,3,6,1,2,1,10,23,3,1,1,1),_PppIpOperStatus_Type())
pppIpOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pppIpOperStatus.setStatus(_A)
class _PppIpLocalToRemoteCompressionProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PppIpLocalToRemoteCompressionProtocol_Type.__name__=_B
_PppIpLocalToRemoteCompressionProtocol_Object=MibTableColumn
pppIpLocalToRemoteCompressionProtocol=_PppIpLocalToRemoteCompressionProtocol_Object((1,3,6,1,2,1,10,23,3,1,1,2),_PppIpLocalToRemoteCompressionProtocol_Type())
pppIpLocalToRemoteCompressionProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:pppIpLocalToRemoteCompressionProtocol.setStatus(_A)
class _PppIpRemoteToLocalCompressionProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PppIpRemoteToLocalCompressionProtocol_Type.__name__=_B
_PppIpRemoteToLocalCompressionProtocol_Object=MibTableColumn
pppIpRemoteToLocalCompressionProtocol=_PppIpRemoteToLocalCompressionProtocol_Object((1,3,6,1,2,1,10,23,3,1,1,3),_PppIpRemoteToLocalCompressionProtocol_Type())
pppIpRemoteToLocalCompressionProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:pppIpRemoteToLocalCompressionProtocol.setStatus(_A)
class _PppIpRemoteMaxSlotId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PppIpRemoteMaxSlotId_Type.__name__=_B
_PppIpRemoteMaxSlotId_Object=MibTableColumn
pppIpRemoteMaxSlotId=_PppIpRemoteMaxSlotId_Object((1,3,6,1,2,1,10,23,3,1,1,4),_PppIpRemoteMaxSlotId_Type())
pppIpRemoteMaxSlotId.setMaxAccess(_C)
if mibBuilder.loadTexts:pppIpRemoteMaxSlotId.setStatus(_A)
class _PppIpLocalMaxSlotId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_PppIpLocalMaxSlotId_Type.__name__=_B
_PppIpLocalMaxSlotId_Object=MibTableColumn
pppIpLocalMaxSlotId=_PppIpLocalMaxSlotId_Object((1,3,6,1,2,1,10,23,3,1,1,5),_PppIpLocalMaxSlotId_Type())
pppIpLocalMaxSlotId.setMaxAccess(_C)
if mibBuilder.loadTexts:pppIpLocalMaxSlotId.setStatus(_A)
_PppIpConfigTable_Object=MibTable
pppIpConfigTable=_PppIpConfigTable_Object((1,3,6,1,2,1,10,23,3,2))
if mibBuilder.loadTexts:pppIpConfigTable.setStatus(_A)
_PppIpConfigEntry_Object=MibTableRow
pppIpConfigEntry=_PppIpConfigEntry_Object((1,3,6,1,2,1,10,23,3,2,1))
pppIpConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:pppIpConfigEntry.setStatus(_A)
class _PppIpConfigAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('open',1),('close',2)))
_PppIpConfigAdminStatus_Type.__name__=_B
_PppIpConfigAdminStatus_Object=MibTableColumn
pppIpConfigAdminStatus=_PppIpConfigAdminStatus_Object((1,3,6,1,2,1,10,23,3,2,1,1),_PppIpConfigAdminStatus_Type())
pppIpConfigAdminStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:pppIpConfigAdminStatus.setStatus(_A)
class _PppIpConfigCompression_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_PppIpConfigCompression_Type.__name__=_B
_PppIpConfigCompression_Object=MibTableColumn
pppIpConfigCompression=_PppIpConfigCompression_Object((1,3,6,1,2,1,10,23,3,2,1,2),_PppIpConfigCompression_Type())
pppIpConfigCompression.setMaxAccess(_H)
if mibBuilder.loadTexts:pppIpConfigCompression.setStatus(_A)
mibBuilder.exportSymbols('PPP-IP-NCP-MIB',**{'pppIp':pppIp,'pppIpTable':pppIpTable,'pppIpEntry':pppIpEntry,'pppIpOperStatus':pppIpOperStatus,'pppIpLocalToRemoteCompressionProtocol':pppIpLocalToRemoteCompressionProtocol,'pppIpRemoteToLocalCompressionProtocol':pppIpRemoteToLocalCompressionProtocol,'pppIpRemoteMaxSlotId':pppIpRemoteMaxSlotId,'pppIpLocalMaxSlotId':pppIpLocalMaxSlotId,'pppIpConfigTable':pppIpConfigTable,'pppIpConfigEntry':pppIpConfigEntry,'pppIpConfigAdminStatus':pppIpConfigAdminStatus,'pppIpConfigCompression':pppIpConfigCompression})