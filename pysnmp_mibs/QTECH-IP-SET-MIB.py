_K='qtechIpSetMIBGroup'
_J='qtechIPSetipAddressType'
_I='qtechIPSetipAddressStatus'
_H='qtechIPSetipAddressMask'
_G='qtechIPSetipAddressAddr'
_F='read-create'
_E='read-write'
_D='qtechIPSetipAddressIfIndex'
_C='Integer32'
_B='QTECH-IP-SET-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
qtechIPSetMgmt=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,111))
if mibBuilder.loadTexts:qtechIPSetMgmt.setRevisions(('2012-02-15 00:00',))
_QtechIPSetMIBObjects_ObjectIdentity=ObjectIdentity
qtechIPSetMIBObjects=_QtechIPSetMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,111,1))
_QtechIPSetipAddressTable_Object=MibTable
qtechIPSetipAddressTable=_QtechIPSetipAddressTable_Object((1,3,6,1,4,1,27514,1,1,10,2,111,1,1))
if mibBuilder.loadTexts:qtechIPSetipAddressTable.setStatus(_A)
_QtechIPSetIpAddressEntry_Object=MibTableRow
qtechIPSetIpAddressEntry=_QtechIPSetIpAddressEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,111,1,1,1))
qtechIPSetIpAddressEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:qtechIPSetIpAddressEntry.setStatus(_A)
_QtechIPSetipAddressIfIndex_Type=InterfaceIndex
_QtechIPSetipAddressIfIndex_Object=MibTableColumn
qtechIPSetipAddressIfIndex=_QtechIPSetipAddressIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,111,1,1,1,1),_QtechIPSetipAddressIfIndex_Type())
qtechIPSetipAddressIfIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:qtechIPSetipAddressIfIndex.setStatus(_A)
_QtechIPSetipAddressAddr_Type=IpAddress
_QtechIPSetipAddressAddr_Object=MibTableColumn
qtechIPSetipAddressAddr=_QtechIPSetipAddressAddr_Object((1,3,6,1,4,1,27514,1,1,10,2,111,1,1,1,2),_QtechIPSetipAddressAddr_Type())
qtechIPSetipAddressAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechIPSetipAddressAddr.setStatus(_A)
_QtechIPSetipAddressMask_Type=IpAddress
_QtechIPSetipAddressMask_Object=MibTableColumn
qtechIPSetipAddressMask=_QtechIPSetipAddressMask_Object((1,3,6,1,4,1,27514,1,1,10,2,111,1,1,1,3),_QtechIPSetipAddressMask_Type())
qtechIPSetipAddressMask.setMaxAccess(_E)
if mibBuilder.loadTexts:qtechIPSetipAddressMask.setStatus(_A)
class _QtechIPSetipAddressStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('delete',0),('add',1)))
_QtechIPSetipAddressStatus_Type.__name__=_C
_QtechIPSetipAddressStatus_Object=MibTableColumn
qtechIPSetipAddressStatus=_QtechIPSetipAddressStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,111,1,1,1,4),_QtechIPSetipAddressStatus_Type())
qtechIPSetipAddressStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechIPSetipAddressStatus.setStatus(_A)
class _QtechIPSetipAddressType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unicast',1),('anycast',2),('broadcast',3)))
_QtechIPSetipAddressType_Type.__name__=_C
_QtechIPSetipAddressType_Object=MibTableColumn
qtechIPSetipAddressType=_QtechIPSetipAddressType_Object((1,3,6,1,4,1,27514,1,1,10,2,111,1,1,1,5),_QtechIPSetipAddressType_Type())
qtechIPSetipAddressType.setMaxAccess(_F)
if mibBuilder.loadTexts:qtechIPSetipAddressType.setStatus(_A)
_QtechIpSetMIBConformance_ObjectIdentity=ObjectIdentity
qtechIpSetMIBConformance=_QtechIpSetMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,111,2))
_QtechIpSetMIBCompliances_ObjectIdentity=ObjectIdentity
qtechIpSetMIBCompliances=_QtechIpSetMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,111,2,1))
_QtechIpSetMIBGroups_ObjectIdentity=ObjectIdentity
qtechIpSetMIBGroups=_QtechIpSetMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,111,2,2))
qtechIpSetMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,111,2,2,1))
qtechIpSetMIBGroup.setObjects(*((_B,_D),(_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:qtechIpSetMIBGroup.setStatus(_A)
qtechIcmpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,111,2,1,1))
qtechIcmpMIBCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:qtechIcmpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechIPSetMgmt':qtechIPSetMgmt,'qtechIPSetMIBObjects':qtechIPSetMIBObjects,'qtechIPSetipAddressTable':qtechIPSetipAddressTable,'qtechIPSetIpAddressEntry':qtechIPSetIpAddressEntry,_D:qtechIPSetipAddressIfIndex,_G:qtechIPSetipAddressAddr,_H:qtechIPSetipAddressMask,_I:qtechIPSetipAddressStatus,_J:qtechIPSetipAddressType,'qtechIpSetMIBConformance':qtechIpSetMIBConformance,'qtechIpSetMIBCompliances':qtechIpSetMIBCompliances,'qtechIcmpMIBCompliance':qtechIcmpMIBCompliance,'qtechIpSetMIBGroups':qtechIpSetMIBGroups,_K:qtechIpSetMIBGroup})