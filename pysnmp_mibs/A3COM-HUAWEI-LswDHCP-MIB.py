_I='hwDhcpToL3VlanIfIndex'
_H='read-only'
_G='hwDhcpClientIpAddress'
_F='hwDhcpGroupID'
_E='read-create'
_D='A3COM-HUAWEI-LswDHCP-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lswCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','lswCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
hwLswDhcpMib=ModuleIdentity((1,3,6,1,4,1,43,45,1,2,23,1,8))
if mibBuilder.loadTexts:hwLswDhcpMib.setRevisions(('2001-06-29 00:00',))
_HwLswDhcpMibObject_ObjectIdentity=ObjectIdentity
hwLswDhcpMibObject=_HwLswDhcpMibObject_ObjectIdentity((1,3,6,1,4,1,43,45,1,2,23,1,8,1))
_HwDhcpGroupTable_Object=MibTable
hwDhcpGroupTable=_HwDhcpGroupTable_Object((1,3,6,1,4,1,43,45,1,2,23,1,8,1,1))
if mibBuilder.loadTexts:hwDhcpGroupTable.setStatus(_A)
_HwDhcpGroupEntry_Object=MibTableRow
hwDhcpGroupEntry=_HwDhcpGroupEntry_Object((1,3,6,1,4,1,43,45,1,2,23,1,8,1,1,1))
hwDhcpGroupEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hwDhcpGroupEntry.setStatus(_A)
class _HwDhcpGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,19))
_HwDhcpGroupID_Type.__name__=_C
_HwDhcpGroupID_Object=MibTableColumn
hwDhcpGroupID=_HwDhcpGroupID_Object((1,3,6,1,4,1,43,45,1,2,23,1,8,1,1,1,1),_HwDhcpGroupID_Type())
hwDhcpGroupID.setMaxAccess(_E)
if mibBuilder.loadTexts:hwDhcpGroupID.setStatus(_A)
_HwIpDhcpServerAddress1_Type=IpAddress
_HwIpDhcpServerAddress1_Object=MibTableColumn
hwIpDhcpServerAddress1=_HwIpDhcpServerAddress1_Object((1,3,6,1,4,1,43,45,1,2,23,1,8,1,1,1,2),_HwIpDhcpServerAddress1_Type())
hwIpDhcpServerAddress1.setMaxAccess(_B)
if mibBuilder.loadTexts:hwIpDhcpServerAddress1.setStatus(_A)
_HwIpDhcpServerAddress2_Type=IpAddress
_HwIpDhcpServerAddress2_Object=MibTableColumn
hwIpDhcpServerAddress2=_HwIpDhcpServerAddress2_Object((1,3,6,1,4,1,43,45,1,2,23,1,8,1,1,1,3),_HwIpDhcpServerAddress2_Type())
hwIpDhcpServerAddress2.setMaxAccess(_B)
if mibBuilder.loadTexts:hwIpDhcpServerAddress2.setStatus(_A)
_HwDhcpRowStatus_Type=RowStatus
_HwDhcpRowStatus_Object=MibTableColumn
hwDhcpRowStatus=_HwDhcpRowStatus_Object((1,3,6,1,4,1,43,45,1,2,23,1,8,1,1,1,4),_HwDhcpRowStatus_Type())
hwDhcpRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hwDhcpRowStatus.setStatus(_A)
_HwDhcpSecurityTable_Object=MibTable
hwDhcpSecurityTable=_HwDhcpSecurityTable_Object((1,3,6,1,4,1,43,45,1,2,23,1,8,1,2))
if mibBuilder.loadTexts:hwDhcpSecurityTable.setStatus(_A)
_HwDhcpSecurityEntry_Object=MibTableRow
hwDhcpSecurityEntry=_HwDhcpSecurityEntry_Object((1,3,6,1,4,1,43,45,1,2,23,1,8,1,2,1))
hwDhcpSecurityEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:hwDhcpSecurityEntry.setStatus(_A)
_HwDhcpClientIpAddress_Type=IpAddress
_HwDhcpClientIpAddress_Object=MibTableColumn
hwDhcpClientIpAddress=_HwDhcpClientIpAddress_Object((1,3,6,1,4,1,43,45,1,2,23,1,8,1,2,1,1),_HwDhcpClientIpAddress_Type())
hwDhcpClientIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:hwDhcpClientIpAddress.setStatus(_A)
_HwDhcpClientMacAddress_Type=MacAddress
_HwDhcpClientMacAddress_Object=MibTableColumn
hwDhcpClientMacAddress=_HwDhcpClientMacAddress_Object((1,3,6,1,4,1,43,45,1,2,23,1,8,1,2,1,2),_HwDhcpClientMacAddress_Type())
hwDhcpClientMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hwDhcpClientMacAddress.setStatus(_A)
class _HwDhcpClientProperty_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_HwDhcpClientProperty_Type.__name__=_C
_HwDhcpClientProperty_Object=MibTableColumn
hwDhcpClientProperty=_HwDhcpClientProperty_Object((1,3,6,1,4,1,43,45,1,2,23,1,8,1,2,1,3),_HwDhcpClientProperty_Type())
hwDhcpClientProperty.setMaxAccess(_B)
if mibBuilder.loadTexts:hwDhcpClientProperty.setStatus(_A)
_HwDhcpClientRowStatus_Type=RowStatus
_HwDhcpClientRowStatus_Object=MibTableColumn
hwDhcpClientRowStatus=_HwDhcpClientRowStatus_Object((1,3,6,1,4,1,43,45,1,2,23,1,8,1,2,1,4),_HwDhcpClientRowStatus_Type())
hwDhcpClientRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hwDhcpClientRowStatus.setStatus(_A)
_HwDhcpToL3IfTable_Object=MibTable
hwDhcpToL3IfTable=_HwDhcpToL3IfTable_Object((1,3,6,1,4,1,43,45,1,2,23,1,8,1,3))
if mibBuilder.loadTexts:hwDhcpToL3IfTable.setStatus(_A)
_HwDhcpToL3IfEntry_Object=MibTableRow
hwDhcpToL3IfEntry=_HwDhcpToL3IfEntry_Object((1,3,6,1,4,1,43,45,1,2,23,1,8,1,3,1))
hwDhcpToL3IfEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:hwDhcpToL3IfEntry.setStatus(_A)
_HwDhcpToL3VlanIfIndex_Type=Integer32
_HwDhcpToL3VlanIfIndex_Object=MibTableColumn
hwDhcpToL3VlanIfIndex=_HwDhcpToL3VlanIfIndex_Object((1,3,6,1,4,1,43,45,1,2,23,1,8,1,3,1,1),_HwDhcpToL3VlanIfIndex_Type())
hwDhcpToL3VlanIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hwDhcpToL3VlanIfIndex.setStatus(_A)
class _HwDhcpToL3GroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,19))
_HwDhcpToL3GroupId_Type.__name__=_C
_HwDhcpToL3GroupId_Object=MibTableColumn
hwDhcpToL3GroupId=_HwDhcpToL3GroupId_Object((1,3,6,1,4,1,43,45,1,2,23,1,8,1,3,1,2),_HwDhcpToL3GroupId_Type())
hwDhcpToL3GroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:hwDhcpToL3GroupId.setStatus(_A)
class _HwDhcpToL3AddressCheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HwDhcpToL3AddressCheck_Type.__name__=_C
_HwDhcpToL3AddressCheck_Object=MibTableColumn
hwDhcpToL3AddressCheck=_HwDhcpToL3AddressCheck_Object((1,3,6,1,4,1,43,45,1,2,23,1,8,1,3,1,3),_HwDhcpToL3AddressCheck_Type())
hwDhcpToL3AddressCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:hwDhcpToL3AddressCheck.setStatus(_A)
_HwDhcpToL3RowStatus_Type=RowStatus
_HwDhcpToL3RowStatus_Object=MibTableColumn
hwDhcpToL3RowStatus=_HwDhcpToL3RowStatus_Object((1,3,6,1,4,1,43,45,1,2,23,1,8,1,3,1,4),_HwDhcpToL3RowStatus_Type())
hwDhcpToL3RowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hwDhcpToL3RowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hwLswDhcpMib':hwLswDhcpMib,'hwLswDhcpMibObject':hwLswDhcpMibObject,'hwDhcpGroupTable':hwDhcpGroupTable,'hwDhcpGroupEntry':hwDhcpGroupEntry,_F:hwDhcpGroupID,'hwIpDhcpServerAddress1':hwIpDhcpServerAddress1,'hwIpDhcpServerAddress2':hwIpDhcpServerAddress2,'hwDhcpRowStatus':hwDhcpRowStatus,'hwDhcpSecurityTable':hwDhcpSecurityTable,'hwDhcpSecurityEntry':hwDhcpSecurityEntry,_G:hwDhcpClientIpAddress,'hwDhcpClientMacAddress':hwDhcpClientMacAddress,'hwDhcpClientProperty':hwDhcpClientProperty,'hwDhcpClientRowStatus':hwDhcpClientRowStatus,'hwDhcpToL3IfTable':hwDhcpToL3IfTable,'hwDhcpToL3IfEntry':hwDhcpToL3IfEntry,_I:hwDhcpToL3VlanIfIndex,'hwDhcpToL3GroupId':hwDhcpToL3GroupId,'hwDhcpToL3AddressCheck':hwDhcpToL3AddressCheck,'hwDhcpToL3RowStatus':hwDhcpToL3RowStatus})