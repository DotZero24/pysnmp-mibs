_Z='hpicfSavifilteringGroup'
_Y='hpicfSavibindingGroup'
_X='hpicfSaviportGroup'
_W='hpicfSaviObjectsFilteringMacAddr'
_V='hpicfSaviObjectsBindingRowStatus'
_U='hpicfSaviObjectsBindingLifetime'
_T='hpicfSaviObjectsBindingMacAddr'
_S='hpicfSaviObjectsPortFilteringNum'
_R='hpicfSaviObjPortDhcpTrustAttr'
_Q='hpicfSaviObjFilteringIpAddr'
_P='hpicfSaviObjectsFilteringIfIndex'
_O='hpicfSaviObjFilteringIpAddrType'
_N='read-only'
_M='read-create'
_L='hpicfSaviObjectsBindingIpAddress'
_K='hpicfSaviObjectsBindingIfIndex'
_J='hpicfSaviObjectsBindingType'
_I='hpicfSaviObjBindingIpAddrType'
_H='read-write'
_G='hpicfSaviObjectsPortIfIndex'
_F='hpicfSaviObjectsPortIPVersion'
_E='Integer32'
_D='InetAddress'
_C='not-accessible'
_B='HPICF-SAVI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpSwitchExperimental,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitchExperimental')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType,InetVersion=mibBuilder.importSymbols('INET-ADDRESS-MIB',_D,'InetAddressType','InetVersion')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval')
hpicfSaviMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,2,1))
if mibBuilder.loadTexts:hpicfSaviMIB.setRevisions(('2017-11-08 00:00',))
_HpicfSaviObjects_ObjectIdentity=ObjectIdentity
hpicfSaviObjects=_HpicfSaviObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,2,1,1))
_HpicfSaviObjectsPortTable_Object=MibTable
hpicfSaviObjectsPortTable=_HpicfSaviObjectsPortTable_Object((1,3,6,1,4,1,11,2,14,11,5,2,1,1,1))
if mibBuilder.loadTexts:hpicfSaviObjectsPortTable.setStatus(_A)
_HpicfSaviObjectsPortEntry_Object=MibTableRow
hpicfSaviObjectsPortEntry=_HpicfSaviObjectsPortEntry_Object((1,3,6,1,4,1,11,2,14,11,5,2,1,1,1,1))
hpicfSaviObjectsPortEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:hpicfSaviObjectsPortEntry.setStatus(_A)
_HpicfSaviObjectsPortIPVersion_Type=InetVersion
_HpicfSaviObjectsPortIPVersion_Object=MibTableColumn
hpicfSaviObjectsPortIPVersion=_HpicfSaviObjectsPortIPVersion_Object((1,3,6,1,4,1,11,2,14,11,5,2,1,1,1,1,1),_HpicfSaviObjectsPortIPVersion_Type())
hpicfSaviObjectsPortIPVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSaviObjectsPortIPVersion.setStatus(_A)
_HpicfSaviObjectsPortIfIndex_Type=InterfaceIndex
_HpicfSaviObjectsPortIfIndex_Object=MibTableColumn
hpicfSaviObjectsPortIfIndex=_HpicfSaviObjectsPortIfIndex_Object((1,3,6,1,4,1,11,2,14,11,5,2,1,1,1,1,2),_HpicfSaviObjectsPortIfIndex_Type())
hpicfSaviObjectsPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSaviObjectsPortIfIndex.setStatus(_A)
class _HpicfSaviObjPortDhcpTrustAttr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HpicfSaviObjPortDhcpTrustAttr_Type.__name__=_E
_HpicfSaviObjPortDhcpTrustAttr_Object=MibTableColumn
hpicfSaviObjPortDhcpTrustAttr=_HpicfSaviObjPortDhcpTrustAttr_Object((1,3,6,1,4,1,11,2,14,11,5,2,1,1,1,1,3),_HpicfSaviObjPortDhcpTrustAttr_Type())
hpicfSaviObjPortDhcpTrustAttr.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfSaviObjPortDhcpTrustAttr.setStatus(_A)
_HpicfSaviObjectsPortFilteringNum_Type=Unsigned32
_HpicfSaviObjectsPortFilteringNum_Object=MibTableColumn
hpicfSaviObjectsPortFilteringNum=_HpicfSaviObjectsPortFilteringNum_Object((1,3,6,1,4,1,11,2,14,11,5,2,1,1,1,1,4),_HpicfSaviObjectsPortFilteringNum_Type())
hpicfSaviObjectsPortFilteringNum.setMaxAccess(_H)
if mibBuilder.loadTexts:hpicfSaviObjectsPortFilteringNum.setStatus(_A)
_HpicfSaviObjectsBindingTable_Object=MibTable
hpicfSaviObjectsBindingTable=_HpicfSaviObjectsBindingTable_Object((1,3,6,1,4,1,11,2,14,11,5,2,1,1,2))
if mibBuilder.loadTexts:hpicfSaviObjectsBindingTable.setStatus(_A)
_HpicfSaviObjectsBindingEntry_Object=MibTableRow
hpicfSaviObjectsBindingEntry=_HpicfSaviObjectsBindingEntry_Object((1,3,6,1,4,1,11,2,14,11,5,2,1,1,2,1))
hpicfSaviObjectsBindingEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:hpicfSaviObjectsBindingEntry.setStatus(_A)
_HpicfSaviObjBindingIpAddrType_Type=InetAddressType
_HpicfSaviObjBindingIpAddrType_Object=MibTableColumn
hpicfSaviObjBindingIpAddrType=_HpicfSaviObjBindingIpAddrType_Object((1,3,6,1,4,1,11,2,14,11,5,2,1,1,2,1,1),_HpicfSaviObjBindingIpAddrType_Type())
hpicfSaviObjBindingIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSaviObjBindingIpAddrType.setStatus(_A)
class _HpicfSaviObjectsBindingType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('manual',1),('slaac',2),('dhcp',3),('send',4)))
_HpicfSaviObjectsBindingType_Type.__name__=_E
_HpicfSaviObjectsBindingType_Object=MibTableColumn
hpicfSaviObjectsBindingType=_HpicfSaviObjectsBindingType_Object((1,3,6,1,4,1,11,2,14,11,5,2,1,1,2,1,2),_HpicfSaviObjectsBindingType_Type())
hpicfSaviObjectsBindingType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSaviObjectsBindingType.setStatus(_A)
_HpicfSaviObjectsBindingIfIndex_Type=InterfaceIndex
_HpicfSaviObjectsBindingIfIndex_Object=MibTableColumn
hpicfSaviObjectsBindingIfIndex=_HpicfSaviObjectsBindingIfIndex_Object((1,3,6,1,4,1,11,2,14,11,5,2,1,1,2,1,3),_HpicfSaviObjectsBindingIfIndex_Type())
hpicfSaviObjectsBindingIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSaviObjectsBindingIfIndex.setStatus(_A)
class _HpicfSaviObjectsBindingIpAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_HpicfSaviObjectsBindingIpAddress_Type.__name__=_D
_HpicfSaviObjectsBindingIpAddress_Object=MibTableColumn
hpicfSaviObjectsBindingIpAddress=_HpicfSaviObjectsBindingIpAddress_Object((1,3,6,1,4,1,11,2,14,11,5,2,1,1,2,1,4),_HpicfSaviObjectsBindingIpAddress_Type())
hpicfSaviObjectsBindingIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSaviObjectsBindingIpAddress.setStatus(_A)
_HpicfSaviObjectsBindingMacAddr_Type=MacAddress
_HpicfSaviObjectsBindingMacAddr_Object=MibTableColumn
hpicfSaviObjectsBindingMacAddr=_HpicfSaviObjectsBindingMacAddr_Object((1,3,6,1,4,1,11,2,14,11,5,2,1,1,2,1,5),_HpicfSaviObjectsBindingMacAddr_Type())
hpicfSaviObjectsBindingMacAddr.setMaxAccess(_M)
if mibBuilder.loadTexts:hpicfSaviObjectsBindingMacAddr.setStatus(_A)
_HpicfSaviObjectsBindingLifetime_Type=TimeInterval
_HpicfSaviObjectsBindingLifetime_Object=MibTableColumn
hpicfSaviObjectsBindingLifetime=_HpicfSaviObjectsBindingLifetime_Object((1,3,6,1,4,1,11,2,14,11,5,2,1,1,2,1,6),_HpicfSaviObjectsBindingLifetime_Type())
hpicfSaviObjectsBindingLifetime.setMaxAccess(_N)
if mibBuilder.loadTexts:hpicfSaviObjectsBindingLifetime.setStatus(_A)
_HpicfSaviObjectsBindingRowStatus_Type=RowStatus
_HpicfSaviObjectsBindingRowStatus_Object=MibTableColumn
hpicfSaviObjectsBindingRowStatus=_HpicfSaviObjectsBindingRowStatus_Object((1,3,6,1,4,1,11,2,14,11,5,2,1,1,2,1,7),_HpicfSaviObjectsBindingRowStatus_Type())
hpicfSaviObjectsBindingRowStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:hpicfSaviObjectsBindingRowStatus.setStatus(_A)
_HpicfSaviObjectsFilteringTable_Object=MibTable
hpicfSaviObjectsFilteringTable=_HpicfSaviObjectsFilteringTable_Object((1,3,6,1,4,1,11,2,14,11,5,2,1,1,3))
if mibBuilder.loadTexts:hpicfSaviObjectsFilteringTable.setStatus(_A)
_HpicfSaviObjectsFilteringEntry_Object=MibTableRow
hpicfSaviObjectsFilteringEntry=_HpicfSaviObjectsFilteringEntry_Object((1,3,6,1,4,1,11,2,14,11,5,2,1,1,3,1))
hpicfSaviObjectsFilteringEntry.setIndexNames((0,_B,_O),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:hpicfSaviObjectsFilteringEntry.setStatus(_A)
_HpicfSaviObjFilteringIpAddrType_Type=InetAddressType
_HpicfSaviObjFilteringIpAddrType_Object=MibTableColumn
hpicfSaviObjFilteringIpAddrType=_HpicfSaviObjFilteringIpAddrType_Object((1,3,6,1,4,1,11,2,14,11,5,2,1,1,3,1,1),_HpicfSaviObjFilteringIpAddrType_Type())
hpicfSaviObjFilteringIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSaviObjFilteringIpAddrType.setStatus(_A)
_HpicfSaviObjectsFilteringIfIndex_Type=InterfaceIndex
_HpicfSaviObjectsFilteringIfIndex_Object=MibTableColumn
hpicfSaviObjectsFilteringIfIndex=_HpicfSaviObjectsFilteringIfIndex_Object((1,3,6,1,4,1,11,2,14,11,5,2,1,1,3,1,2),_HpicfSaviObjectsFilteringIfIndex_Type())
hpicfSaviObjectsFilteringIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSaviObjectsFilteringIfIndex.setStatus(_A)
class _HpicfSaviObjFilteringIpAddr_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_HpicfSaviObjFilteringIpAddr_Type.__name__=_D
_HpicfSaviObjFilteringIpAddr_Object=MibTableColumn
hpicfSaviObjFilteringIpAddr=_HpicfSaviObjFilteringIpAddr_Object((1,3,6,1,4,1,11,2,14,11,5,2,1,1,3,1,3),_HpicfSaviObjFilteringIpAddr_Type())
hpicfSaviObjFilteringIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfSaviObjFilteringIpAddr.setStatus(_A)
_HpicfSaviObjectsFilteringMacAddr_Type=MacAddress
_HpicfSaviObjectsFilteringMacAddr_Object=MibTableColumn
hpicfSaviObjectsFilteringMacAddr=_HpicfSaviObjectsFilteringMacAddr_Object((1,3,6,1,4,1,11,2,14,11,5,2,1,1,3,1,4),_HpicfSaviObjectsFilteringMacAddr_Type())
hpicfSaviObjectsFilteringMacAddr.setMaxAccess(_N)
if mibBuilder.loadTexts:hpicfSaviObjectsFilteringMacAddr.setStatus(_A)
_HpicfSaviConformance_ObjectIdentity=ObjectIdentity
hpicfSaviConformance=_HpicfSaviConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,2,1,2))
_HpicfSaviCompliances_ObjectIdentity=ObjectIdentity
hpicfSaviCompliances=_HpicfSaviCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,2,1,2,1))
_HpicfSaviGroups_ObjectIdentity=ObjectIdentity
hpicfSaviGroups=_HpicfSaviGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,2,1,2,2))
hpicfSaviportGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,2,1,2,2,1))
hpicfSaviportGroup.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:hpicfSaviportGroup.setStatus(_A)
hpicfSavibindingGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,2,1,2,2,2))
hpicfSavibindingGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:hpicfSavibindingGroup.setStatus(_A)
hpicfSavifilteringGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,2,1,2,2,3))
hpicfSavifilteringGroup.setObjects((_B,_W))
if mibBuilder.loadTexts:hpicfSavifilteringGroup.setStatus(_A)
hpicfSaviCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,2,1,2,1,1))
hpicfSaviCompliance.setObjects(*((_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:hpicfSaviCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpicfSaviMIB':hpicfSaviMIB,'hpicfSaviObjects':hpicfSaviObjects,'hpicfSaviObjectsPortTable':hpicfSaviObjectsPortTable,'hpicfSaviObjectsPortEntry':hpicfSaviObjectsPortEntry,_F:hpicfSaviObjectsPortIPVersion,_G:hpicfSaviObjectsPortIfIndex,_R:hpicfSaviObjPortDhcpTrustAttr,_S:hpicfSaviObjectsPortFilteringNum,'hpicfSaviObjectsBindingTable':hpicfSaviObjectsBindingTable,'hpicfSaviObjectsBindingEntry':hpicfSaviObjectsBindingEntry,_I:hpicfSaviObjBindingIpAddrType,_J:hpicfSaviObjectsBindingType,_K:hpicfSaviObjectsBindingIfIndex,_L:hpicfSaviObjectsBindingIpAddress,_T:hpicfSaviObjectsBindingMacAddr,_U:hpicfSaviObjectsBindingLifetime,_V:hpicfSaviObjectsBindingRowStatus,'hpicfSaviObjectsFilteringTable':hpicfSaviObjectsFilteringTable,'hpicfSaviObjectsFilteringEntry':hpicfSaviObjectsFilteringEntry,_O:hpicfSaviObjFilteringIpAddrType,_P:hpicfSaviObjectsFilteringIfIndex,_Q:hpicfSaviObjFilteringIpAddr,_W:hpicfSaviObjectsFilteringMacAddr,'hpicfSaviConformance':hpicfSaviConformance,'hpicfSaviCompliances':hpicfSaviCompliances,'hpicfSaviCompliance':hpicfSaviCompliance,'hpicfSaviGroups':hpicfSaviGroups,_X:hpicfSaviportGroup,_Y:hpicfSavibindingGroup,_Z:hpicfSavifilteringGroup})