_F='qtechDhcpClientIntfConfigGroup'
_E='qtechDhcpClientIpAddrDhcpStatus'
_D='qtechDhcpIntfClientIndex'
_C='Integer32'
_B='QTECH-DHCP-CLIENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
qtechDhcpClientMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,135))
if mibBuilder.loadTexts:qtechDhcpClientMIB.setRevisions(('2015-02-09 00:00',))
_QtechDhcpClientMIBObjects_ObjectIdentity=ObjectIdentity
qtechDhcpClientMIBObjects=_QtechDhcpClientMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,135,0))
_QtechDhcpClientConfig_ObjectIdentity=ObjectIdentity
qtechDhcpClientConfig=_QtechDhcpClientConfig_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,135,0,1))
_QtechDhcpClientIntfTable_Object=MibTable
qtechDhcpClientIntfTable=_QtechDhcpClientIntfTable_Object((1,3,6,1,4,1,27514,1,1,10,2,135,0,1,2))
if mibBuilder.loadTexts:qtechDhcpClientIntfTable.setStatus(_A)
_QtechDhcpClientIntfEntry_Object=MibTableRow
qtechDhcpClientIntfEntry=_QtechDhcpClientIntfEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,135,0,1,2,1))
qtechDhcpClientIntfEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:qtechDhcpClientIntfEntry.setStatus(_A)
_QtechDhcpIntfClientIndex_Type=InterfaceIndex
_QtechDhcpIntfClientIndex_Object=MibTableColumn
qtechDhcpIntfClientIndex=_QtechDhcpIntfClientIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,135,0,1,2,1,1),_QtechDhcpIntfClientIndex_Type())
qtechDhcpIntfClientIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:qtechDhcpIntfClientIndex.setStatus(_A)
class _QtechDhcpClientIpAddrDhcpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_QtechDhcpClientIpAddrDhcpStatus_Type.__name__=_C
_QtechDhcpClientIpAddrDhcpStatus_Object=MibTableColumn
qtechDhcpClientIpAddrDhcpStatus=_QtechDhcpClientIpAddrDhcpStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,135,0,1,2,1,2),_QtechDhcpClientIpAddrDhcpStatus_Type())
qtechDhcpClientIpAddrDhcpStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:qtechDhcpClientIpAddrDhcpStatus.setStatus(_A)
_QtechDhcpClientMIBConformance_ObjectIdentity=ObjectIdentity
qtechDhcpClientMIBConformance=_QtechDhcpClientMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,135,2))
_QtechDhcpClientMIBCompliances_ObjectIdentity=ObjectIdentity
qtechDhcpClientMIBCompliances=_QtechDhcpClientMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,135,2,1))
_QtechDhcpClientMIBGroups_ObjectIdentity=ObjectIdentity
qtechDhcpClientMIBGroups=_QtechDhcpClientMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,135,2,2))
qtechDhcpClientIntfConfigGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,135,2,2,1))
qtechDhcpClientIntfConfigGroup.setObjects((_B,_E))
if mibBuilder.loadTexts:qtechDhcpClientIntfConfigGroup.setStatus(_A)
qtechDhcpClientMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,135,2,1,1))
qtechDhcpClientMIBCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:qtechDhcpClientMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechDhcpClientMIB':qtechDhcpClientMIB,'qtechDhcpClientMIBObjects':qtechDhcpClientMIBObjects,'qtechDhcpClientConfig':qtechDhcpClientConfig,'qtechDhcpClientIntfTable':qtechDhcpClientIntfTable,'qtechDhcpClientIntfEntry':qtechDhcpClientIntfEntry,_D:qtechDhcpIntfClientIndex,_E:qtechDhcpClientIpAddrDhcpStatus,'qtechDhcpClientMIBConformance':qtechDhcpClientMIBConformance,'qtechDhcpClientMIBCompliances':qtechDhcpClientMIBCompliances,'qtechDhcpClientMIBCompliance':qtechDhcpClientMIBCompliance,'qtechDhcpClientMIBGroups':qtechDhcpClientMIBGroups,_F:qtechDhcpClientIntfConfigGroup})