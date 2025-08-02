_N='h3cIpv6AddrReadAddr'
_M='h3cIpv6AddrReadAddrType'
_L='h3cIpv6AddrReadIfIndex'
_K='assignedEUI64Ip'
_J='assignedIp'
_I='h3cIpv6AddrSetAddr'
_H='h3cIpv6AddrSetAddrType'
_G='h3cIpv6AddrSetIfIndex'
_F='read-only'
_E='read-create'
_D='not-accessible'
_C='A3COM-HUAWEI-IPV6-ADDRESS-MIB'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cIpv6AddrMIB=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,71))
if mibBuilder.loadTexts:h3cIpv6AddrMIB.setRevisions(('2006-03-15 00:00',))
_H3cIpv6AddressObjects_ObjectIdentity=ObjectIdentity
h3cIpv6AddressObjects=_H3cIpv6AddressObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,71,1))
_H3cIpv6AddressConfig_ObjectIdentity=ObjectIdentity
h3cIpv6AddressConfig=_H3cIpv6AddressConfig_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,71,1,1))
_H3cIpv6AddrSetTable_Object=MibTable
h3cIpv6AddrSetTable=_H3cIpv6AddrSetTable_Object((1,3,6,1,4,1,43,45,1,10,2,71,1,1,1))
if mibBuilder.loadTexts:h3cIpv6AddrSetTable.setStatus(_A)
_H3cIpv6AddrSetEntry_Object=MibTableRow
h3cIpv6AddrSetEntry=_H3cIpv6AddrSetEntry_Object((1,3,6,1,4,1,43,45,1,10,2,71,1,1,1,1))
h3cIpv6AddrSetEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:h3cIpv6AddrSetEntry.setStatus(_A)
class _H3cIpv6AddrSetIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cIpv6AddrSetIfIndex_Type.__name__=_B
_H3cIpv6AddrSetIfIndex_Object=MibTableColumn
h3cIpv6AddrSetIfIndex=_H3cIpv6AddrSetIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,71,1,1,1,1,1),_H3cIpv6AddrSetIfIndex_Type())
h3cIpv6AddrSetIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpv6AddrSetIfIndex.setStatus(_A)
_H3cIpv6AddrSetAddrType_Type=InetAddressType
_H3cIpv6AddrSetAddrType_Object=MibTableColumn
h3cIpv6AddrSetAddrType=_H3cIpv6AddrSetAddrType_Object((1,3,6,1,4,1,43,45,1,10,2,71,1,1,1,1,2),_H3cIpv6AddrSetAddrType_Type())
h3cIpv6AddrSetAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpv6AddrSetAddrType.setStatus(_A)
_H3cIpv6AddrSetAddr_Type=InetAddress
_H3cIpv6AddrSetAddr_Object=MibTableColumn
h3cIpv6AddrSetAddr=_H3cIpv6AddrSetAddr_Object((1,3,6,1,4,1,43,45,1,10,2,71,1,1,1,1,3),_H3cIpv6AddrSetAddr_Type())
h3cIpv6AddrSetAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpv6AddrSetAddr.setStatus(_A)
class _H3cIpv6AddrSetPfxLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_H3cIpv6AddrSetPfxLength_Type.__name__=_B
_H3cIpv6AddrSetPfxLength_Object=MibTableColumn
h3cIpv6AddrSetPfxLength=_H3cIpv6AddrSetPfxLength_Object((1,3,6,1,4,1,43,45,1,10,2,71,1,1,1,1,4),_H3cIpv6AddrSetPfxLength_Type())
h3cIpv6AddrSetPfxLength.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIpv6AddrSetPfxLength.setStatus(_A)
class _H3cIpv6AddrSetSourceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),(_K,2),('assignedLinklocalIp',3)))
_H3cIpv6AddrSetSourceType_Type.__name__=_B
_H3cIpv6AddrSetSourceType_Object=MibTableColumn
h3cIpv6AddrSetSourceType=_H3cIpv6AddrSetSourceType_Object((1,3,6,1,4,1,43,45,1,10,2,71,1,1,1,1,5),_H3cIpv6AddrSetSourceType_Type())
h3cIpv6AddrSetSourceType.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIpv6AddrSetSourceType.setStatus(_A)
_H3cIpv6AddrSetRowStatus_Type=RowStatus
_H3cIpv6AddrSetRowStatus_Object=MibTableColumn
h3cIpv6AddrSetRowStatus=_H3cIpv6AddrSetRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,71,1,1,1,1,6),_H3cIpv6AddrSetRowStatus_Type())
h3cIpv6AddrSetRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cIpv6AddrSetRowStatus.setStatus(_A)
_H3cIpv6AddrReadTable_Object=MibTable
h3cIpv6AddrReadTable=_H3cIpv6AddrReadTable_Object((1,3,6,1,4,1,43,45,1,10,2,71,1,1,2))
if mibBuilder.loadTexts:h3cIpv6AddrReadTable.setStatus(_A)
_H3cIpv6AddrReadEntry_Object=MibTableRow
h3cIpv6AddrReadEntry=_H3cIpv6AddrReadEntry_Object((1,3,6,1,4,1,43,45,1,10,2,71,1,1,2,1))
h3cIpv6AddrReadEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_N))
if mibBuilder.loadTexts:h3cIpv6AddrReadEntry.setStatus(_A)
class _H3cIpv6AddrReadIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cIpv6AddrReadIfIndex_Type.__name__=_B
_H3cIpv6AddrReadIfIndex_Object=MibTableColumn
h3cIpv6AddrReadIfIndex=_H3cIpv6AddrReadIfIndex_Object((1,3,6,1,4,1,43,45,1,10,2,71,1,1,2,1,1),_H3cIpv6AddrReadIfIndex_Type())
h3cIpv6AddrReadIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpv6AddrReadIfIndex.setStatus(_A)
_H3cIpv6AddrReadAddrType_Type=InetAddressType
_H3cIpv6AddrReadAddrType_Object=MibTableColumn
h3cIpv6AddrReadAddrType=_H3cIpv6AddrReadAddrType_Object((1,3,6,1,4,1,43,45,1,10,2,71,1,1,2,1,2),_H3cIpv6AddrReadAddrType_Type())
h3cIpv6AddrReadAddrType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpv6AddrReadAddrType.setStatus(_A)
_H3cIpv6AddrReadAddr_Type=InetAddress
_H3cIpv6AddrReadAddr_Object=MibTableColumn
h3cIpv6AddrReadAddr=_H3cIpv6AddrReadAddr_Object((1,3,6,1,4,1,43,45,1,10,2,71,1,1,2,1,3),_H3cIpv6AddrReadAddr_Type())
h3cIpv6AddrReadAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cIpv6AddrReadAddr.setStatus(_A)
class _H3cIpv6AddrReadPfxLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_H3cIpv6AddrReadPfxLength_Type.__name__=_B
_H3cIpv6AddrReadPfxLength_Object=MibTableColumn
h3cIpv6AddrReadPfxLength=_H3cIpv6AddrReadPfxLength_Object((1,3,6,1,4,1,43,45,1,10,2,71,1,1,2,1,4),_H3cIpv6AddrReadPfxLength_Type())
h3cIpv6AddrReadPfxLength.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIpv6AddrReadPfxLength.setStatus(_A)
class _H3cIpv6AddrReadSourceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_J,1),(_K,2),('assignedAutoIp',3),('autoIp',4),('dhcpv6',5),('negotiate',6),('cluster',7)))
_H3cIpv6AddrReadSourceType_Type.__name__=_B
_H3cIpv6AddrReadSourceType_Object=MibTableColumn
h3cIpv6AddrReadSourceType=_H3cIpv6AddrReadSourceType_Object((1,3,6,1,4,1,43,45,1,10,2,71,1,1,2,1,5),_H3cIpv6AddrReadSourceType_Type())
h3cIpv6AddrReadSourceType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIpv6AddrReadSourceType.setStatus(_A)
class _H3cIpv6AddrReadCatalog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('nodelocal',1),('linklocal',2),('sitelocal',3),('orglocal',4),('global',5)))
_H3cIpv6AddrReadCatalog_Type.__name__=_B
_H3cIpv6AddrReadCatalog_Object=MibTableColumn
h3cIpv6AddrReadCatalog=_H3cIpv6AddrReadCatalog_Object((1,3,6,1,4,1,43,45,1,10,2,71,1,1,2,1,6),_H3cIpv6AddrReadCatalog_Type())
h3cIpv6AddrReadCatalog.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cIpv6AddrReadCatalog.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'h3cIpv6AddrMIB':h3cIpv6AddrMIB,'h3cIpv6AddressObjects':h3cIpv6AddressObjects,'h3cIpv6AddressConfig':h3cIpv6AddressConfig,'h3cIpv6AddrSetTable':h3cIpv6AddrSetTable,'h3cIpv6AddrSetEntry':h3cIpv6AddrSetEntry,_G:h3cIpv6AddrSetIfIndex,_H:h3cIpv6AddrSetAddrType,_I:h3cIpv6AddrSetAddr,'h3cIpv6AddrSetPfxLength':h3cIpv6AddrSetPfxLength,'h3cIpv6AddrSetSourceType':h3cIpv6AddrSetSourceType,'h3cIpv6AddrSetRowStatus':h3cIpv6AddrSetRowStatus,'h3cIpv6AddrReadTable':h3cIpv6AddrReadTable,'h3cIpv6AddrReadEntry':h3cIpv6AddrReadEntry,_L:h3cIpv6AddrReadIfIndex,_M:h3cIpv6AddrReadAddrType,_N:h3cIpv6AddrReadAddr,'h3cIpv6AddrReadPfxLength':h3cIpv6AddrReadPfxLength,'h3cIpv6AddrReadSourceType':h3cIpv6AddrReadSourceType,'h3cIpv6AddrReadCatalog':h3cIpv6AddrReadCatalog})