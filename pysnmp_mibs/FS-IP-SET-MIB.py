_K='fsIpSetMIBGroup'
_J='fsIPSetipAddressType'
_I='fsIPSetipAddressStatus'
_H='fsIPSetipAddressMask'
_G='fsIPSetipAddressAddr'
_F='read-create'
_E='read-write'
_D='fsIPSetipAddressIfIndex'
_C='Integer32'
_B='FS-IP-SET-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsIPSetMgmt=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,111))
if mibBuilder.loadTexts:fsIPSetMgmt.setRevisions(('2012-02-15 00:00',))
_FsIPSetMIBObjects_ObjectIdentity=ObjectIdentity
fsIPSetMIBObjects=_FsIPSetMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,111,1))
_FsIPSetipAddressTable_Object=MibTable
fsIPSetipAddressTable=_FsIPSetipAddressTable_Object((1,3,6,1,4,1,52642,1,1,10,2,111,1,1))
if mibBuilder.loadTexts:fsIPSetipAddressTable.setStatus(_A)
_FsIPSetIpAddressEntry_Object=MibTableRow
fsIPSetIpAddressEntry=_FsIPSetIpAddressEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,111,1,1,1))
fsIPSetIpAddressEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:fsIPSetIpAddressEntry.setStatus(_A)
_FsIPSetipAddressIfIndex_Type=InterfaceIndex
_FsIPSetipAddressIfIndex_Object=MibTableColumn
fsIPSetipAddressIfIndex=_FsIPSetipAddressIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,111,1,1,1,1),_FsIPSetipAddressIfIndex_Type())
fsIPSetipAddressIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:fsIPSetipAddressIfIndex.setStatus(_A)
_FsIPSetipAddressAddr_Type=IpAddress
_FsIPSetipAddressAddr_Object=MibTableColumn
fsIPSetipAddressAddr=_FsIPSetipAddressAddr_Object((1,3,6,1,4,1,52642,1,1,10,2,111,1,1,1,2),_FsIPSetipAddressAddr_Type())
fsIPSetipAddressAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIPSetipAddressAddr.setStatus(_A)
_FsIPSetipAddressMask_Type=IpAddress
_FsIPSetipAddressMask_Object=MibTableColumn
fsIPSetipAddressMask=_FsIPSetipAddressMask_Object((1,3,6,1,4,1,52642,1,1,10,2,111,1,1,1,3),_FsIPSetipAddressMask_Type())
fsIPSetipAddressMask.setMaxAccess(_E)
if mibBuilder.loadTexts:fsIPSetipAddressMask.setStatus(_A)
class _FsIPSetipAddressStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('delete',0),('add',1)))
_FsIPSetipAddressStatus_Type.__name__=_C
_FsIPSetipAddressStatus_Object=MibTableColumn
fsIPSetipAddressStatus=_FsIPSetipAddressStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,111,1,1,1,4),_FsIPSetipAddressStatus_Type())
fsIPSetipAddressStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIPSetipAddressStatus.setStatus(_A)
class _FsIPSetipAddressType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unicast',1),('anycast',2),('broadcast',3)))
_FsIPSetipAddressType_Type.__name__=_C
_FsIPSetipAddressType_Object=MibTableColumn
fsIPSetipAddressType=_FsIPSetipAddressType_Object((1,3,6,1,4,1,52642,1,1,10,2,111,1,1,1,5),_FsIPSetipAddressType_Type())
fsIPSetipAddressType.setMaxAccess(_F)
if mibBuilder.loadTexts:fsIPSetipAddressType.setStatus(_A)
_FsIpSetMIBConformance_ObjectIdentity=ObjectIdentity
fsIpSetMIBConformance=_FsIpSetMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,111,2))
_FsIpSetMIBCompliances_ObjectIdentity=ObjectIdentity
fsIpSetMIBCompliances=_FsIpSetMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,111,2,1))
_FsIpSetMIBGroups_ObjectIdentity=ObjectIdentity
fsIpSetMIBGroups=_FsIpSetMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,111,2,2))
fsIpSetMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,111,2,2,1))
fsIpSetMIBGroup.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:fsIpSetMIBGroup.setStatus(_A)
fsIcmpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,111,2,1,1))
fsIcmpMIBCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:fsIcmpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsIPSetMgmt':fsIPSetMgmt,'fsIPSetMIBObjects':fsIPSetMIBObjects,'fsIPSetipAddressTable':fsIPSetipAddressTable,'fsIPSetIpAddressEntry':fsIPSetIpAddressEntry,_D:fsIPSetipAddressIfIndex,_G:fsIPSetipAddressAddr,_H:fsIPSetipAddressMask,_I:fsIPSetipAddressStatus,_J:fsIPSetipAddressType,'fsIpSetMIBConformance':fsIpSetMIBConformance,'fsIpSetMIBCompliances':fsIpSetMIBCompliances,'fsIcmpMIBCompliance':fsIcmpMIBCompliance,'fsIpSetMIBGroups':fsIpSetMIBGroups,_K:fsIpSetMIBGroup})