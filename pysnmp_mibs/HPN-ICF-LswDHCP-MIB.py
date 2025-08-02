_I='hpnicfDhcpToL3VlanIfIndex'
_H='read-only'
_G='hpnicfDhcpClientIpAddress'
_F='hpnicfDhcpGroupID'
_E='read-create'
_D='HPN-ICF-LswDHCP-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicflswCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicflswCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
hpnicfLswDhcpMib=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,8))
if mibBuilder.loadTexts:hpnicfLswDhcpMib.setRevisions(('2001-06-29 00:00',))
_HpnicfLswDhcpMibObject_ObjectIdentity=ObjectIdentity
hpnicfLswDhcpMibObject=_HpnicfLswDhcpMibObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,35,8,1))
_HpnicfDhcpGroupTable_Object=MibTable
hpnicfDhcpGroupTable=_HpnicfDhcpGroupTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,8,1,1))
if mibBuilder.loadTexts:hpnicfDhcpGroupTable.setStatus(_A)
_HpnicfDhcpGroupEntry_Object=MibTableRow
hpnicfDhcpGroupEntry=_HpnicfDhcpGroupEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,8,1,1,1))
hpnicfDhcpGroupEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:hpnicfDhcpGroupEntry.setStatus(_A)
class _HpnicfDhcpGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,19))
_HpnicfDhcpGroupID_Type.__name__=_C
_HpnicfDhcpGroupID_Object=MibTableColumn
hpnicfDhcpGroupID=_HpnicfDhcpGroupID_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,8,1,1,1,1),_HpnicfDhcpGroupID_Type())
hpnicfDhcpGroupID.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDhcpGroupID.setStatus(_A)
_HpnicfIpDhcpServerAddress1_Type=IpAddress
_HpnicfIpDhcpServerAddress1_Object=MibTableColumn
hpnicfIpDhcpServerAddress1=_HpnicfIpDhcpServerAddress1_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,8,1,1,1,2),_HpnicfIpDhcpServerAddress1_Type())
hpnicfIpDhcpServerAddress1.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpDhcpServerAddress1.setStatus(_A)
_HpnicfIpDhcpServerAddress2_Type=IpAddress
_HpnicfIpDhcpServerAddress2_Object=MibTableColumn
hpnicfIpDhcpServerAddress2=_HpnicfIpDhcpServerAddress2_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,8,1,1,1,3),_HpnicfIpDhcpServerAddress2_Type())
hpnicfIpDhcpServerAddress2.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpDhcpServerAddress2.setStatus(_A)
_HpnicfDhcpRowStatus_Type=RowStatus
_HpnicfDhcpRowStatus_Object=MibTableColumn
hpnicfDhcpRowStatus=_HpnicfDhcpRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,8,1,1,1,4),_HpnicfDhcpRowStatus_Type())
hpnicfDhcpRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDhcpRowStatus.setStatus(_A)
_HpnicfDhcpSecurityTable_Object=MibTable
hpnicfDhcpSecurityTable=_HpnicfDhcpSecurityTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,8,1,2))
if mibBuilder.loadTexts:hpnicfDhcpSecurityTable.setStatus(_A)
_HpnicfDhcpSecurityEntry_Object=MibTableRow
hpnicfDhcpSecurityEntry=_HpnicfDhcpSecurityEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,8,1,2,1))
hpnicfDhcpSecurityEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:hpnicfDhcpSecurityEntry.setStatus(_A)
_HpnicfDhcpClientIpAddress_Type=IpAddress
_HpnicfDhcpClientIpAddress_Object=MibTableColumn
hpnicfDhcpClientIpAddress=_HpnicfDhcpClientIpAddress_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,8,1,2,1,1),_HpnicfDhcpClientIpAddress_Type())
hpnicfDhcpClientIpAddress.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpClientIpAddress.setStatus(_A)
_HpnicfDhcpClientMacAddress_Type=MacAddress
_HpnicfDhcpClientMacAddress_Object=MibTableColumn
hpnicfDhcpClientMacAddress=_HpnicfDhcpClientMacAddress_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,8,1,2,1,2),_HpnicfDhcpClientMacAddress_Type())
hpnicfDhcpClientMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpClientMacAddress.setStatus(_A)
class _HpnicfDhcpClientProperty_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_HpnicfDhcpClientProperty_Type.__name__=_C
_HpnicfDhcpClientProperty_Object=MibTableColumn
hpnicfDhcpClientProperty=_HpnicfDhcpClientProperty_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,8,1,2,1,3),_HpnicfDhcpClientProperty_Type())
hpnicfDhcpClientProperty.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpClientProperty.setStatus(_A)
_HpnicfDhcpClientRowStatus_Type=RowStatus
_HpnicfDhcpClientRowStatus_Object=MibTableColumn
hpnicfDhcpClientRowStatus=_HpnicfDhcpClientRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,8,1,2,1,4),_HpnicfDhcpClientRowStatus_Type())
hpnicfDhcpClientRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDhcpClientRowStatus.setStatus(_A)
_HpnicfDhcpToL3IfTable_Object=MibTable
hpnicfDhcpToL3IfTable=_HpnicfDhcpToL3IfTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,8,1,3))
if mibBuilder.loadTexts:hpnicfDhcpToL3IfTable.setStatus(_A)
_HpnicfDhcpToL3IfEntry_Object=MibTableRow
hpnicfDhcpToL3IfEntry=_HpnicfDhcpToL3IfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,8,1,3,1))
hpnicfDhcpToL3IfEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:hpnicfDhcpToL3IfEntry.setStatus(_A)
_HpnicfDhcpToL3VlanIfIndex_Type=Integer32
_HpnicfDhcpToL3VlanIfIndex_Object=MibTableColumn
hpnicfDhcpToL3VlanIfIndex=_HpnicfDhcpToL3VlanIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,8,1,3,1,1),_HpnicfDhcpToL3VlanIfIndex_Type())
hpnicfDhcpToL3VlanIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDhcpToL3VlanIfIndex.setStatus(_A)
class _HpnicfDhcpToL3GroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,19))
_HpnicfDhcpToL3GroupId_Type.__name__=_C
_HpnicfDhcpToL3GroupId_Object=MibTableColumn
hpnicfDhcpToL3GroupId=_HpnicfDhcpToL3GroupId_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,8,1,3,1,2),_HpnicfDhcpToL3GroupId_Type())
hpnicfDhcpToL3GroupId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpToL3GroupId.setStatus(_A)
class _HpnicfDhcpToL3AddressCheck_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_HpnicfDhcpToL3AddressCheck_Type.__name__=_C
_HpnicfDhcpToL3AddressCheck_Object=MibTableColumn
hpnicfDhcpToL3AddressCheck=_HpnicfDhcpToL3AddressCheck_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,8,1,3,1,3),_HpnicfDhcpToL3AddressCheck_Type())
hpnicfDhcpToL3AddressCheck.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpToL3AddressCheck.setStatus(_A)
_HpnicfDhcpToL3RowStatus_Type=RowStatus
_HpnicfDhcpToL3RowStatus_Object=MibTableColumn
hpnicfDhcpToL3RowStatus=_HpnicfDhcpToL3RowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,35,8,1,3,1,4),_HpnicfDhcpToL3RowStatus_Type())
hpnicfDhcpToL3RowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfDhcpToL3RowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hpnicfLswDhcpMib':hpnicfLswDhcpMib,'hpnicfLswDhcpMibObject':hpnicfLswDhcpMibObject,'hpnicfDhcpGroupTable':hpnicfDhcpGroupTable,'hpnicfDhcpGroupEntry':hpnicfDhcpGroupEntry,_F:hpnicfDhcpGroupID,'hpnicfIpDhcpServerAddress1':hpnicfIpDhcpServerAddress1,'hpnicfIpDhcpServerAddress2':hpnicfIpDhcpServerAddress2,'hpnicfDhcpRowStatus':hpnicfDhcpRowStatus,'hpnicfDhcpSecurityTable':hpnicfDhcpSecurityTable,'hpnicfDhcpSecurityEntry':hpnicfDhcpSecurityEntry,_G:hpnicfDhcpClientIpAddress,'hpnicfDhcpClientMacAddress':hpnicfDhcpClientMacAddress,'hpnicfDhcpClientProperty':hpnicfDhcpClientProperty,'hpnicfDhcpClientRowStatus':hpnicfDhcpClientRowStatus,'hpnicfDhcpToL3IfTable':hpnicfDhcpToL3IfTable,'hpnicfDhcpToL3IfEntry':hpnicfDhcpToL3IfEntry,_I:hpnicfDhcpToL3VlanIfIndex,'hpnicfDhcpToL3GroupId':hpnicfDhcpToL3GroupId,'hpnicfDhcpToL3AddressCheck':hpnicfDhcpToL3AddressCheck,'hpnicfDhcpToL3RowStatus':hpnicfDhcpToL3RowStatus})