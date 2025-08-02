_X='ccdsgIfDownstreamGroup'
_W='ccdsgIfTunnelGroup'
_V='ccdsgIfCaVendorGroup'
_U='ccdsgIfDownRowStatus'
_T='ccdsgIfDownIfIndex'
_S='ccdsgIfDownTunnelIndex'
_R='ccdsgIfTunnelRowStatus'
_Q='ccdsgIfTunnelCaVendorIndex'
_P='ccdsgIfTunnelMacAddress'
_O='ccdsgIfTunnelInIpAddress'
_N='ccdsgIfTunnelInAddressType'
_M='ccdsgIfCaVendorRowStatus'
_L='ccdsgIfCaVendorTunnelCnt'
_K='ccdsgIfCaVendorName'
_J='ccdsgIfDownDsgIndex'
_I='ccdsgIfTunnelIndex'
_H='ccdsgIfCaVendorIndex'
_G='Integer32'
_F='SnmpAdminString'
_E='not-accessible'
_D='Unsigned32'
_C='read-create'
_B='CISCO-CABLE-DSG-IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
ciscoCableDsgIfMIB=ModuleIdentity((1,3,6,1,4,1,9,10,999))
if mibBuilder.loadTexts:ciscoCableDsgIfMIB.setRevisions(('2004-03-29 00:00',))
_CcdsgIfCaVendor_ObjectIdentity=ObjectIdentity
ccdsgIfCaVendor=_CcdsgIfCaVendor_ObjectIdentity((1,3,6,1,4,1,9,10,999,1))
_CcdsgIfCaVendorTable_Object=MibTable
ccdsgIfCaVendorTable=_CcdsgIfCaVendorTable_Object((1,3,6,1,4,1,9,10,999,1,1))
if mibBuilder.loadTexts:ccdsgIfCaVendorTable.setStatus(_A)
_CcdsgIfCaVendorEntry_Object=MibTableRow
ccdsgIfCaVendorEntry=_CcdsgIfCaVendorEntry_Object((1,3,6,1,4,1,9,10,999,1,1,1))
ccdsgIfCaVendorEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:ccdsgIfCaVendorEntry.setStatus(_A)
class _CcdsgIfCaVendorIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CcdsgIfCaVendorIndex_Type.__name__=_D
_CcdsgIfCaVendorIndex_Object=MibTableColumn
ccdsgIfCaVendorIndex=_CcdsgIfCaVendorIndex_Object((1,3,6,1,4,1,9,10,999,1,1,1,1),_CcdsgIfCaVendorIndex_Type())
ccdsgIfCaVendorIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ccdsgIfCaVendorIndex.setStatus(_A)
class _CcdsgIfCaVendorName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,20))
_CcdsgIfCaVendorName_Type.__name__=_F
_CcdsgIfCaVendorName_Object=MibTableColumn
ccdsgIfCaVendorName=_CcdsgIfCaVendorName_Object((1,3,6,1,4,1,9,10,999,1,1,1,2),_CcdsgIfCaVendorName_Type())
ccdsgIfCaVendorName.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsgIfCaVendorName.setStatus(_A)
class _CcdsgIfCaVendorTunnelCnt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_CcdsgIfCaVendorTunnelCnt_Type.__name__=_G
_CcdsgIfCaVendorTunnelCnt_Object=MibTableColumn
ccdsgIfCaVendorTunnelCnt=_CcdsgIfCaVendorTunnelCnt_Object((1,3,6,1,4,1,9,10,999,1,1,1,3),_CcdsgIfCaVendorTunnelCnt_Type())
ccdsgIfCaVendorTunnelCnt.setMaxAccess('read-only')
if mibBuilder.loadTexts:ccdsgIfCaVendorTunnelCnt.setStatus(_A)
_CcdsgIfCaVendorRowStatus_Type=RowStatus
_CcdsgIfCaVendorRowStatus_Object=MibTableColumn
ccdsgIfCaVendorRowStatus=_CcdsgIfCaVendorRowStatus_Object((1,3,6,1,4,1,9,10,999,1,1,1,4),_CcdsgIfCaVendorRowStatus_Type())
ccdsgIfCaVendorRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsgIfCaVendorRowStatus.setStatus(_A)
_CcdsgIfTunnel_ObjectIdentity=ObjectIdentity
ccdsgIfTunnel=_CcdsgIfTunnel_ObjectIdentity((1,3,6,1,4,1,9,10,999,2))
_CcdsgIfTunnelTable_Object=MibTable
ccdsgIfTunnelTable=_CcdsgIfTunnelTable_Object((1,3,6,1,4,1,9,10,999,2,1))
if mibBuilder.loadTexts:ccdsgIfTunnelTable.setStatus(_A)
_CcdsgIfTunnelEntry_Object=MibTableRow
ccdsgIfTunnelEntry=_CcdsgIfTunnelEntry_Object((1,3,6,1,4,1,9,10,999,2,1,1))
ccdsgIfTunnelEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:ccdsgIfTunnelEntry.setStatus(_A)
class _CcdsgIfTunnelIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CcdsgIfTunnelIndex_Type.__name__=_D
_CcdsgIfTunnelIndex_Object=MibTableColumn
ccdsgIfTunnelIndex=_CcdsgIfTunnelIndex_Object((1,3,6,1,4,1,9,10,999,2,1,1,1),_CcdsgIfTunnelIndex_Type())
ccdsgIfTunnelIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ccdsgIfTunnelIndex.setStatus(_A)
_CcdsgIfTunnelInAddressType_Type=InetAddressType
_CcdsgIfTunnelInAddressType_Object=MibTableColumn
ccdsgIfTunnelInAddressType=_CcdsgIfTunnelInAddressType_Object((1,3,6,1,4,1,9,10,999,2,1,1,2),_CcdsgIfTunnelInAddressType_Type())
ccdsgIfTunnelInAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsgIfTunnelInAddressType.setStatus(_A)
_CcdsgIfTunnelInIpAddress_Type=InetAddress
_CcdsgIfTunnelInIpAddress_Object=MibTableColumn
ccdsgIfTunnelInIpAddress=_CcdsgIfTunnelInIpAddress_Object((1,3,6,1,4,1,9,10,999,2,1,1,3),_CcdsgIfTunnelInIpAddress_Type())
ccdsgIfTunnelInIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsgIfTunnelInIpAddress.setStatus(_A)
_CcdsgIfTunnelMacAddress_Type=MacAddress
_CcdsgIfTunnelMacAddress_Object=MibTableColumn
ccdsgIfTunnelMacAddress=_CcdsgIfTunnelMacAddress_Object((1,3,6,1,4,1,9,10,999,2,1,1,4),_CcdsgIfTunnelMacAddress_Type())
ccdsgIfTunnelMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsgIfTunnelMacAddress.setStatus(_A)
class _CcdsgIfTunnelCaVendorIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CcdsgIfTunnelCaVendorIndex_Type.__name__=_D
_CcdsgIfTunnelCaVendorIndex_Object=MibTableColumn
ccdsgIfTunnelCaVendorIndex=_CcdsgIfTunnelCaVendorIndex_Object((1,3,6,1,4,1,9,10,999,2,1,1,5),_CcdsgIfTunnelCaVendorIndex_Type())
ccdsgIfTunnelCaVendorIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsgIfTunnelCaVendorIndex.setStatus(_A)
_CcdsgIfTunnelRowStatus_Type=RowStatus
_CcdsgIfTunnelRowStatus_Object=MibTableColumn
ccdsgIfTunnelRowStatus=_CcdsgIfTunnelRowStatus_Object((1,3,6,1,4,1,9,10,999,2,1,1,6),_CcdsgIfTunnelRowStatus_Type())
ccdsgIfTunnelRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsgIfTunnelRowStatus.setStatus(_A)
_CcdsgIfDownstream_ObjectIdentity=ObjectIdentity
ccdsgIfDownstream=_CcdsgIfDownstream_ObjectIdentity((1,3,6,1,4,1,9,10,999,3))
_CcdsgIfDownstreamTable_Object=MibTable
ccdsgIfDownstreamTable=_CcdsgIfDownstreamTable_Object((1,3,6,1,4,1,9,10,999,3,1))
if mibBuilder.loadTexts:ccdsgIfDownstreamTable.setStatus(_A)
_CcdsgIfDownstreamEntry_Object=MibTableRow
ccdsgIfDownstreamEntry=_CcdsgIfDownstreamEntry_Object((1,3,6,1,4,1,9,10,999,3,1,1))
ccdsgIfDownstreamEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:ccdsgIfDownstreamEntry.setStatus(_A)
class _CcdsgIfDownDsgIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CcdsgIfDownDsgIndex_Type.__name__=_D
_CcdsgIfDownDsgIndex_Object=MibTableColumn
ccdsgIfDownDsgIndex=_CcdsgIfDownDsgIndex_Object((1,3,6,1,4,1,9,10,999,3,1,1,1),_CcdsgIfDownDsgIndex_Type())
ccdsgIfDownDsgIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:ccdsgIfDownDsgIndex.setStatus(_A)
class _CcdsgIfDownTunnelIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CcdsgIfDownTunnelIndex_Type.__name__=_D
_CcdsgIfDownTunnelIndex_Object=MibTableColumn
ccdsgIfDownTunnelIndex=_CcdsgIfDownTunnelIndex_Object((1,3,6,1,4,1,9,10,999,3,1,1,2),_CcdsgIfDownTunnelIndex_Type())
ccdsgIfDownTunnelIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsgIfDownTunnelIndex.setStatus(_A)
_CcdsgIfDownIfIndex_Type=InterfaceIndex
_CcdsgIfDownIfIndex_Object=MibTableColumn
ccdsgIfDownIfIndex=_CcdsgIfDownIfIndex_Object((1,3,6,1,4,1,9,10,999,3,1,1,3),_CcdsgIfDownIfIndex_Type())
ccdsgIfDownIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsgIfDownIfIndex.setStatus(_A)
_CcdsgIfDownRowStatus_Type=RowStatus
_CcdsgIfDownRowStatus_Object=MibTableColumn
ccdsgIfDownRowStatus=_CcdsgIfDownRowStatus_Object((1,3,6,1,4,1,9,10,999,3,1,1,4),_CcdsgIfDownRowStatus_Type())
ccdsgIfDownRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ccdsgIfDownRowStatus.setStatus(_A)
_CiscoCableDsgIfConformance_ObjectIdentity=ObjectIdentity
ciscoCableDsgIfConformance=_CiscoCableDsgIfConformance_ObjectIdentity((1,3,6,1,4,1,9,10,999,4))
_CiscoCableDsgIfCompliances_ObjectIdentity=ObjectIdentity
ciscoCableDsgIfCompliances=_CiscoCableDsgIfCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,999,4,1))
_CiscoCableDsgIfGroups_ObjectIdentity=ObjectIdentity
ciscoCableDsgIfGroups=_CiscoCableDsgIfGroups_ObjectIdentity((1,3,6,1,4,1,9,10,999,4,2))
ccdsgIfCaVendorGroup=ObjectGroup((1,3,6,1,4,1,9,10,999,4,2,1))
ccdsgIfCaVendorGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:ccdsgIfCaVendorGroup.setStatus(_A)
ccdsgIfTunnelGroup=ObjectGroup((1,3,6,1,4,1,9,10,999,4,2,2))
ccdsgIfTunnelGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:ccdsgIfTunnelGroup.setStatus(_A)
ccdsgIfDownstreamGroup=ObjectGroup((1,3,6,1,4,1,9,10,999,4,2,3))
ccdsgIfDownstreamGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:ccdsgIfDownstreamGroup.setStatus(_A)
ccdsgIfBasicCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,999,4,1,1))
ccdsgIfBasicCompliance.setObjects(*((_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ccdsgIfBasicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoCableDsgIfMIB':ciscoCableDsgIfMIB,'ccdsgIfCaVendor':ccdsgIfCaVendor,'ccdsgIfCaVendorTable':ccdsgIfCaVendorTable,'ccdsgIfCaVendorEntry':ccdsgIfCaVendorEntry,_H:ccdsgIfCaVendorIndex,_K:ccdsgIfCaVendorName,_L:ccdsgIfCaVendorTunnelCnt,_M:ccdsgIfCaVendorRowStatus,'ccdsgIfTunnel':ccdsgIfTunnel,'ccdsgIfTunnelTable':ccdsgIfTunnelTable,'ccdsgIfTunnelEntry':ccdsgIfTunnelEntry,_I:ccdsgIfTunnelIndex,_N:ccdsgIfTunnelInAddressType,_O:ccdsgIfTunnelInIpAddress,_P:ccdsgIfTunnelMacAddress,_Q:ccdsgIfTunnelCaVendorIndex,_R:ccdsgIfTunnelRowStatus,'ccdsgIfDownstream':ccdsgIfDownstream,'ccdsgIfDownstreamTable':ccdsgIfDownstreamTable,'ccdsgIfDownstreamEntry':ccdsgIfDownstreamEntry,_J:ccdsgIfDownDsgIndex,_S:ccdsgIfDownTunnelIndex,_T:ccdsgIfDownIfIndex,_U:ccdsgIfDownRowStatus,'ciscoCableDsgIfConformance':ciscoCableDsgIfConformance,'ciscoCableDsgIfCompliances':ciscoCableDsgIfCompliances,'ccdsgIfBasicCompliance':ccdsgIfBasicCompliance,'ciscoCableDsgIfGroups':ciscoCableDsgIfGroups,_V:ccdsgIfCaVendorGroup,_W:ccdsgIfTunnelGroup,_X:ccdsgIfDownstreamGroup})