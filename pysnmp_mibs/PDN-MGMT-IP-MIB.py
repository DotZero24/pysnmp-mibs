_X='pdnMgmtIpConfigGroup'
_W='pdnMgmtIpDefaultRouter'
_V='pdnMgmtAtmInvArpRowStatus'
_U='pdnMgmtNextHopIp'
_T='pdnMgmtIpPortIfIndex'
_S='pdnMgmtIpAdminStatus'
_R='pdnMgmtBootVci'
_Q='pdnMgmtBootVpi'
_P='pdnMgmtBootIfIndex'
_O='pdnMgmtIpConfigMode'
_N='pdnMgmtIpPhysAddress'
_M='pdnMgmtIpEthGateway'
_L='pdnMgmtIpNetMask'
_K='pdnMgmtIpAddress'
_J='pdnMgmtAtmVci'
_I='pdnMgmtAtmVpi'
_H='pdnMgmtAtmIfIndex'
_G='pdnMgmtIpPortIndex'
_F='read-create'
_E='Integer32'
_D='not-accessible'
_C='read-write'
_B='PDN-MGMT-IP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AtmVcIdentifier,AtmVpIdentifier=mibBuilder.importSymbols('ATM-TC-MIB','AtmVcIdentifier','AtmVpIdentifier')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
pdn_interfaces,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-interfaces')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
pdnMgmtIpMIB=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,6,21))
_PdnMgmtIpConfObjects_ObjectIdentity=ObjectIdentity
pdnMgmtIpConfObjects=_PdnMgmtIpConfObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,21,1))
_PdnMgmtIpPortTable_Object=MibTable
pdnMgmtIpPortTable=_PdnMgmtIpPortTable_Object((1,3,6,1,4,1,1795,2,24,2,6,21,1,1))
if mibBuilder.loadTexts:pdnMgmtIpPortTable.setStatus(_A)
_PdnMgmtIpPortEntry_Object=MibTableRow
pdnMgmtIpPortEntry=_PdnMgmtIpPortEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,21,1,1,1))
pdnMgmtIpPortEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:pdnMgmtIpPortEntry.setStatus(_A)
_PdnMgmtIpPortIndex_Type=InterfaceIndex
_PdnMgmtIpPortIndex_Object=MibTableColumn
pdnMgmtIpPortIndex=_PdnMgmtIpPortIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,21,1,1,1,1),_PdnMgmtIpPortIndex_Type())
pdnMgmtIpPortIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnMgmtIpPortIndex.setStatus(_A)
_PdnMgmtIpAddress_Type=IpAddress
_PdnMgmtIpAddress_Object=MibTableColumn
pdnMgmtIpAddress=_PdnMgmtIpAddress_Object((1,3,6,1,4,1,1795,2,24,2,6,21,1,1,1,2),_PdnMgmtIpAddress_Type())
pdnMgmtIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnMgmtIpAddress.setStatus(_A)
_PdnMgmtIpNetMask_Type=IpAddress
_PdnMgmtIpNetMask_Object=MibTableColumn
pdnMgmtIpNetMask=_PdnMgmtIpNetMask_Object((1,3,6,1,4,1,1795,2,24,2,6,21,1,1,1,3),_PdnMgmtIpNetMask_Type())
pdnMgmtIpNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnMgmtIpNetMask.setStatus(_A)
_PdnMgmtIpEthGateway_Type=IpAddress
_PdnMgmtIpEthGateway_Object=MibTableColumn
pdnMgmtIpEthGateway=_PdnMgmtIpEthGateway_Object((1,3,6,1,4,1,1795,2,24,2,6,21,1,1,1,4),_PdnMgmtIpEthGateway_Type())
pdnMgmtIpEthGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnMgmtIpEthGateway.setStatus(_A)
_PdnMgmtIpPhysAddress_Type=PhysAddress
_PdnMgmtIpPhysAddress_Object=MibTableColumn
pdnMgmtIpPhysAddress=_PdnMgmtIpPhysAddress_Object((1,3,6,1,4,1,1795,2,24,2,6,21,1,1,1,5),_PdnMgmtIpPhysAddress_Type())
pdnMgmtIpPhysAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnMgmtIpPhysAddress.setStatus(_A)
class _PdnMgmtIpConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('manual',1),('dhcp',2),('bootp',3)))
_PdnMgmtIpConfigMode_Type.__name__=_E
_PdnMgmtIpConfigMode_Object=MibTableColumn
pdnMgmtIpConfigMode=_PdnMgmtIpConfigMode_Object((1,3,6,1,4,1,1795,2,24,2,6,21,1,1,1,6),_PdnMgmtIpConfigMode_Type())
pdnMgmtIpConfigMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnMgmtIpConfigMode.setStatus(_A)
_PdnMgmtBootIfIndex_Type=InterfaceIndex
_PdnMgmtBootIfIndex_Object=MibTableColumn
pdnMgmtBootIfIndex=_PdnMgmtBootIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,21,1,1,1,7),_PdnMgmtBootIfIndex_Type())
pdnMgmtBootIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnMgmtBootIfIndex.setStatus(_A)
_PdnMgmtBootVpi_Type=AtmVpIdentifier
_PdnMgmtBootVpi_Object=MibTableColumn
pdnMgmtBootVpi=_PdnMgmtBootVpi_Object((1,3,6,1,4,1,1795,2,24,2,6,21,1,1,1,8),_PdnMgmtBootVpi_Type())
pdnMgmtBootVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnMgmtBootVpi.setStatus(_A)
_PdnMgmtBootVci_Type=AtmVcIdentifier
_PdnMgmtBootVci_Object=MibTableColumn
pdnMgmtBootVci=_PdnMgmtBootVci_Object((1,3,6,1,4,1,1795,2,24,2,6,21,1,1,1,9),_PdnMgmtBootVci_Type())
pdnMgmtBootVci.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnMgmtBootVci.setStatus(_A)
class _PdnMgmtIpAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_PdnMgmtIpAdminStatus_Type.__name__=_E
_PdnMgmtIpAdminStatus_Object=MibTableColumn
pdnMgmtIpAdminStatus=_PdnMgmtIpAdminStatus_Object((1,3,6,1,4,1,1795,2,24,2,6,21,1,1,1,10),_PdnMgmtIpAdminStatus_Type())
pdnMgmtIpAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnMgmtIpAdminStatus.setStatus(_A)
_PdnMgmtAtmInvArpTable_Object=MibTable
pdnMgmtAtmInvArpTable=_PdnMgmtAtmInvArpTable_Object((1,3,6,1,4,1,1795,2,24,2,6,21,1,2))
if mibBuilder.loadTexts:pdnMgmtAtmInvArpTable.setStatus(_A)
_PdnMgmtAtmInvArpEntry_Object=MibTableRow
pdnMgmtAtmInvArpEntry=_PdnMgmtAtmInvArpEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,21,1,2,1))
pdnMgmtAtmInvArpEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:pdnMgmtAtmInvArpEntry.setStatus(_A)
_PdnMgmtAtmIfIndex_Type=InterfaceIndex
_PdnMgmtAtmIfIndex_Object=MibTableColumn
pdnMgmtAtmIfIndex=_PdnMgmtAtmIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,21,1,2,1,1),_PdnMgmtAtmIfIndex_Type())
pdnMgmtAtmIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnMgmtAtmIfIndex.setStatus(_A)
_PdnMgmtAtmVpi_Type=AtmVpIdentifier
_PdnMgmtAtmVpi_Object=MibTableColumn
pdnMgmtAtmVpi=_PdnMgmtAtmVpi_Object((1,3,6,1,4,1,1795,2,24,2,6,21,1,2,1,2),_PdnMgmtAtmVpi_Type())
pdnMgmtAtmVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnMgmtAtmVpi.setStatus(_A)
_PdnMgmtAtmVci_Type=AtmVcIdentifier
_PdnMgmtAtmVci_Object=MibTableColumn
pdnMgmtAtmVci=_PdnMgmtAtmVci_Object((1,3,6,1,4,1,1795,2,24,2,6,21,1,2,1,3),_PdnMgmtAtmVci_Type())
pdnMgmtAtmVci.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnMgmtAtmVci.setStatus(_A)
_PdnMgmtIpPortIfIndex_Type=InterfaceIndex
_PdnMgmtIpPortIfIndex_Object=MibTableColumn
pdnMgmtIpPortIfIndex=_PdnMgmtIpPortIfIndex_Object((1,3,6,1,4,1,1795,2,24,2,6,21,1,2,1,4),_PdnMgmtIpPortIfIndex_Type())
pdnMgmtIpPortIfIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnMgmtIpPortIfIndex.setStatus(_A)
_PdnMgmtNextHopIp_Type=IpAddress
_PdnMgmtNextHopIp_Object=MibTableColumn
pdnMgmtNextHopIp=_PdnMgmtNextHopIp_Object((1,3,6,1,4,1,1795,2,24,2,6,21,1,2,1,5),_PdnMgmtNextHopIp_Type())
pdnMgmtNextHopIp.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnMgmtNextHopIp.setStatus(_A)
_PdnMgmtAtmInvArpRowStatus_Type=RowStatus
_PdnMgmtAtmInvArpRowStatus_Object=MibTableColumn
pdnMgmtAtmInvArpRowStatus=_PdnMgmtAtmInvArpRowStatus_Object((1,3,6,1,4,1,1795,2,24,2,6,21,1,2,1,6),_PdnMgmtAtmInvArpRowStatus_Type())
pdnMgmtAtmInvArpRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:pdnMgmtAtmInvArpRowStatus.setStatus(_A)
_PdnMgmtIpDefaultRouter_Type=IpAddress
_PdnMgmtIpDefaultRouter_Object=MibScalar
pdnMgmtIpDefaultRouter=_PdnMgmtIpDefaultRouter_Object((1,3,6,1,4,1,1795,2,24,2,6,21,1,3),_PdnMgmtIpDefaultRouter_Type())
pdnMgmtIpDefaultRouter.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnMgmtIpDefaultRouter.setStatus(_A)
_PdnMgmtIpConformance_ObjectIdentity=ObjectIdentity
pdnMgmtIpConformance=_PdnMgmtIpConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,21,2))
_PdnMgmtIpGroups_ObjectIdentity=ObjectIdentity
pdnMgmtIpGroups=_PdnMgmtIpGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,21,2,1))
_PdnMgmtIpCompliances_ObjectIdentity=ObjectIdentity
pdnMgmtIpCompliances=_PdnMgmtIpCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,21,2,2))
pdnMgmtIpConfigGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,21,2,1,1))
pdnMgmtIpConfigGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:pdnMgmtIpConfigGroup.setStatus(_A)
pdnMgmtIpConfigCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,6,21,2,2,1))
pdnMgmtIpConfigCompliance.setObjects((_B,_X))
if mibBuilder.loadTexts:pdnMgmtIpConfigCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pdnMgmtIpMIB':pdnMgmtIpMIB,'pdnMgmtIpConfObjects':pdnMgmtIpConfObjects,'pdnMgmtIpPortTable':pdnMgmtIpPortTable,'pdnMgmtIpPortEntry':pdnMgmtIpPortEntry,_G:pdnMgmtIpPortIndex,_K:pdnMgmtIpAddress,_L:pdnMgmtIpNetMask,_M:pdnMgmtIpEthGateway,_N:pdnMgmtIpPhysAddress,_O:pdnMgmtIpConfigMode,_P:pdnMgmtBootIfIndex,_Q:pdnMgmtBootVpi,_R:pdnMgmtBootVci,_S:pdnMgmtIpAdminStatus,'pdnMgmtAtmInvArpTable':pdnMgmtAtmInvArpTable,'pdnMgmtAtmInvArpEntry':pdnMgmtAtmInvArpEntry,_H:pdnMgmtAtmIfIndex,_I:pdnMgmtAtmVpi,_J:pdnMgmtAtmVci,_T:pdnMgmtIpPortIfIndex,_U:pdnMgmtNextHopIp,_V:pdnMgmtAtmInvArpRowStatus,_W:pdnMgmtIpDefaultRouter,'pdnMgmtIpConformance':pdnMgmtIpConformance,'pdnMgmtIpGroups':pdnMgmtIpGroups,_X:pdnMgmtIpConfigGroup,'pdnMgmtIpCompliances':pdnMgmtIpCompliances,'pdnMgmtIpConfigCompliance':pdnMgmtIpConfigCompliance})