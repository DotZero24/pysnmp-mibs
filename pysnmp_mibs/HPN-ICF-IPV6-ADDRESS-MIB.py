_N='hpnicfIpv6AddrReadAddr'
_M='hpnicfIpv6AddrReadAddrType'
_L='hpnicfIpv6AddrReadIfIndex'
_K='assignedEUI64Ip'
_J='assignedIp'
_I='hpnicfIpv6AddrSetAddr'
_H='hpnicfIpv6AddrSetAddrType'
_G='hpnicfIpv6AddrSetIfIndex'
_F='read-only'
_E='read-create'
_D='not-accessible'
_C='HPN-ICF-IPV6-ADDRESS-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfIpv6AddrMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,71))
if mibBuilder.loadTexts:hpnicfIpv6AddrMIB.setRevisions(('2006-03-15 00:00',))
_HpnicfIpv6AddressObjects_ObjectIdentity=ObjectIdentity
hpnicfIpv6AddressObjects=_HpnicfIpv6AddressObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,71,1))
_HpnicfIpv6AddressConfig_ObjectIdentity=ObjectIdentity
hpnicfIpv6AddressConfig=_HpnicfIpv6AddressConfig_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,71,1,1))
_HpnicfIpv6AddrSetTable_Object=MibTable
hpnicfIpv6AddrSetTable=_HpnicfIpv6AddrSetTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,71,1,1,1))
if mibBuilder.loadTexts:hpnicfIpv6AddrSetTable.setStatus(_A)
_HpnicfIpv6AddrSetEntry_Object=MibTableRow
hpnicfIpv6AddrSetEntry=_HpnicfIpv6AddrSetEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,71,1,1,1,1))
hpnicfIpv6AddrSetEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:hpnicfIpv6AddrSetEntry.setStatus(_A)
class _HpnicfIpv6AddrSetIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfIpv6AddrSetIfIndex_Type.__name__=_B
_HpnicfIpv6AddrSetIfIndex_Object=MibTableColumn
hpnicfIpv6AddrSetIfIndex=_HpnicfIpv6AddrSetIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,71,1,1,1,1,1),_HpnicfIpv6AddrSetIfIndex_Type())
hpnicfIpv6AddrSetIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpv6AddrSetIfIndex.setStatus(_A)
_HpnicfIpv6AddrSetAddrType_Type=InetAddressType
_HpnicfIpv6AddrSetAddrType_Object=MibTableColumn
hpnicfIpv6AddrSetAddrType=_HpnicfIpv6AddrSetAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,71,1,1,1,1,2),_HpnicfIpv6AddrSetAddrType_Type())
hpnicfIpv6AddrSetAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpv6AddrSetAddrType.setStatus(_A)
_HpnicfIpv6AddrSetAddr_Type=InetAddress
_HpnicfIpv6AddrSetAddr_Object=MibTableColumn
hpnicfIpv6AddrSetAddr=_HpnicfIpv6AddrSetAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,71,1,1,1,1,3),_HpnicfIpv6AddrSetAddr_Type())
hpnicfIpv6AddrSetAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpv6AddrSetAddr.setStatus(_A)
class _HpnicfIpv6AddrSetPfxLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_HpnicfIpv6AddrSetPfxLength_Type.__name__=_B
_HpnicfIpv6AddrSetPfxLength_Object=MibTableColumn
hpnicfIpv6AddrSetPfxLength=_HpnicfIpv6AddrSetPfxLength_Object((1,3,6,1,4,1,11,2,14,11,15,2,71,1,1,1,1,4),_HpnicfIpv6AddrSetPfxLength_Type())
hpnicfIpv6AddrSetPfxLength.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfIpv6AddrSetPfxLength.setStatus(_A)
class _HpnicfIpv6AddrSetSourceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),('assignedLinklocalIp',3)))
_HpnicfIpv6AddrSetSourceType_Type.__name__=_B
_HpnicfIpv6AddrSetSourceType_Object=MibTableColumn
hpnicfIpv6AddrSetSourceType=_HpnicfIpv6AddrSetSourceType_Object((1,3,6,1,4,1,11,2,14,11,15,2,71,1,1,1,1,5),_HpnicfIpv6AddrSetSourceType_Type())
hpnicfIpv6AddrSetSourceType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfIpv6AddrSetSourceType.setStatus(_A)
_HpnicfIpv6AddrSetRowStatus_Type=RowStatus
_HpnicfIpv6AddrSetRowStatus_Object=MibTableColumn
hpnicfIpv6AddrSetRowStatus=_HpnicfIpv6AddrSetRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,71,1,1,1,1,6),_HpnicfIpv6AddrSetRowStatus_Type())
hpnicfIpv6AddrSetRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfIpv6AddrSetRowStatus.setStatus(_A)
_HpnicfIpv6AddrReadTable_Object=MibTable
hpnicfIpv6AddrReadTable=_HpnicfIpv6AddrReadTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,71,1,1,2))
if mibBuilder.loadTexts:hpnicfIpv6AddrReadTable.setStatus(_A)
_HpnicfIpv6AddrReadEntry_Object=MibTableRow
hpnicfIpv6AddrReadEntry=_HpnicfIpv6AddrReadEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,71,1,1,2,1))
hpnicfIpv6AddrReadEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_N))
if mibBuilder.loadTexts:hpnicfIpv6AddrReadEntry.setStatus(_A)
class _HpnicfIpv6AddrReadIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfIpv6AddrReadIfIndex_Type.__name__=_B
_HpnicfIpv6AddrReadIfIndex_Object=MibTableColumn
hpnicfIpv6AddrReadIfIndex=_HpnicfIpv6AddrReadIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,71,1,1,2,1,1),_HpnicfIpv6AddrReadIfIndex_Type())
hpnicfIpv6AddrReadIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpv6AddrReadIfIndex.setStatus(_A)
_HpnicfIpv6AddrReadAddrType_Type=InetAddressType
_HpnicfIpv6AddrReadAddrType_Object=MibTableColumn
hpnicfIpv6AddrReadAddrType=_HpnicfIpv6AddrReadAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,71,1,1,2,1,2),_HpnicfIpv6AddrReadAddrType_Type())
hpnicfIpv6AddrReadAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpv6AddrReadAddrType.setStatus(_A)
_HpnicfIpv6AddrReadAddr_Type=InetAddress
_HpnicfIpv6AddrReadAddr_Object=MibTableColumn
hpnicfIpv6AddrReadAddr=_HpnicfIpv6AddrReadAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,71,1,1,2,1,3),_HpnicfIpv6AddrReadAddr_Type())
hpnicfIpv6AddrReadAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfIpv6AddrReadAddr.setStatus(_A)
class _HpnicfIpv6AddrReadPfxLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_HpnicfIpv6AddrReadPfxLength_Type.__name__=_B
_HpnicfIpv6AddrReadPfxLength_Object=MibTableColumn
hpnicfIpv6AddrReadPfxLength=_HpnicfIpv6AddrReadPfxLength_Object((1,3,6,1,4,1,11,2,14,11,15,2,71,1,1,2,1,4),_HpnicfIpv6AddrReadPfxLength_Type())
hpnicfIpv6AddrReadPfxLength.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIpv6AddrReadPfxLength.setStatus(_A)
class _HpnicfIpv6AddrReadSourceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_J,1),(_K,2),('assignedAutoIp',3),('autoIp',4),('dhcpv6',5),('negotiate',6),('cluster',7)))
_HpnicfIpv6AddrReadSourceType_Type.__name__=_B
_HpnicfIpv6AddrReadSourceType_Object=MibTableColumn
hpnicfIpv6AddrReadSourceType=_HpnicfIpv6AddrReadSourceType_Object((1,3,6,1,4,1,11,2,14,11,15,2,71,1,1,2,1,5),_HpnicfIpv6AddrReadSourceType_Type())
hpnicfIpv6AddrReadSourceType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIpv6AddrReadSourceType.setStatus(_A)
class _HpnicfIpv6AddrReadCatalog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('nodelocal',1),('linklocal',2),('sitelocal',3),('orglocal',4),('global',5)))
_HpnicfIpv6AddrReadCatalog_Type.__name__=_B
_HpnicfIpv6AddrReadCatalog_Object=MibTableColumn
hpnicfIpv6AddrReadCatalog=_HpnicfIpv6AddrReadCatalog_Object((1,3,6,1,4,1,11,2,14,11,15,2,71,1,1,2,1,6),_HpnicfIpv6AddrReadCatalog_Type())
hpnicfIpv6AddrReadCatalog.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfIpv6AddrReadCatalog.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'hpnicfIpv6AddrMIB':hpnicfIpv6AddrMIB,'hpnicfIpv6AddressObjects':hpnicfIpv6AddressObjects,'hpnicfIpv6AddressConfig':hpnicfIpv6AddressConfig,'hpnicfIpv6AddrSetTable':hpnicfIpv6AddrSetTable,'hpnicfIpv6AddrSetEntry':hpnicfIpv6AddrSetEntry,_G:hpnicfIpv6AddrSetIfIndex,_H:hpnicfIpv6AddrSetAddrType,_I:hpnicfIpv6AddrSetAddr,'hpnicfIpv6AddrSetPfxLength':hpnicfIpv6AddrSetPfxLength,'hpnicfIpv6AddrSetSourceType':hpnicfIpv6AddrSetSourceType,'hpnicfIpv6AddrSetRowStatus':hpnicfIpv6AddrSetRowStatus,'hpnicfIpv6AddrReadTable':hpnicfIpv6AddrReadTable,'hpnicfIpv6AddrReadEntry':hpnicfIpv6AddrReadEntry,_L:hpnicfIpv6AddrReadIfIndex,_M:hpnicfIpv6AddrReadAddrType,_N:hpnicfIpv6AddrReadAddr,'hpnicfIpv6AddrReadPfxLength':hpnicfIpv6AddrReadPfxLength,'hpnicfIpv6AddrReadSourceType':hpnicfIpv6AddrReadSourceType,'hpnicfIpv6AddrReadCatalog':hpnicfIpv6AddrReadCatalog})