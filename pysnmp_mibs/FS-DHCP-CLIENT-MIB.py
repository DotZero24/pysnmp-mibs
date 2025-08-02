_F='fsDhcpClientIntfConfigGroup'
_E='fsDhcpClientIpAddrDhcpStatus'
_D='fsDhcpIntfClientIndex'
_C='Integer32'
_B='FS-DHCP-CLIENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
fsDhcpClientMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,135))
if mibBuilder.loadTexts:fsDhcpClientMIB.setRevisions(('2015-02-09 00:00',))
_FsDhcpClientMIBObjects_ObjectIdentity=ObjectIdentity
fsDhcpClientMIBObjects=_FsDhcpClientMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,135,0))
_FsDhcpClientConfig_ObjectIdentity=ObjectIdentity
fsDhcpClientConfig=_FsDhcpClientConfig_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,135,0,1))
_FsDhcpClientIntfTable_Object=MibTable
fsDhcpClientIntfTable=_FsDhcpClientIntfTable_Object((1,3,6,1,4,1,52642,1,1,10,2,135,0,1,2))
if mibBuilder.loadTexts:fsDhcpClientIntfTable.setStatus(_A)
_FsDhcpClientIntfEntry_Object=MibTableRow
fsDhcpClientIntfEntry=_FsDhcpClientIntfEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,135,0,1,2,1))
fsDhcpClientIntfEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:fsDhcpClientIntfEntry.setStatus(_A)
_FsDhcpIntfClientIndex_Type=InterfaceIndex
_FsDhcpIntfClientIndex_Object=MibTableColumn
fsDhcpIntfClientIndex=_FsDhcpIntfClientIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,135,0,1,2,1,1),_FsDhcpIntfClientIndex_Type())
fsDhcpIntfClientIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:fsDhcpIntfClientIndex.setStatus(_A)
class _FsDhcpClientIpAddrDhcpStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_FsDhcpClientIpAddrDhcpStatus_Type.__name__=_C
_FsDhcpClientIpAddrDhcpStatus_Object=MibTableColumn
fsDhcpClientIpAddrDhcpStatus=_FsDhcpClientIpAddrDhcpStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,135,0,1,2,1,2),_FsDhcpClientIpAddrDhcpStatus_Type())
fsDhcpClientIpAddrDhcpStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:fsDhcpClientIpAddrDhcpStatus.setStatus(_A)
_FsDhcpClientMIBConformance_ObjectIdentity=ObjectIdentity
fsDhcpClientMIBConformance=_FsDhcpClientMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,135,2))
_FsDhcpClientMIBCompliances_ObjectIdentity=ObjectIdentity
fsDhcpClientMIBCompliances=_FsDhcpClientMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,135,2,1))
_FsDhcpClientMIBGroups_ObjectIdentity=ObjectIdentity
fsDhcpClientMIBGroups=_FsDhcpClientMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,135,2,2))
fsDhcpClientIntfConfigGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,135,2,2,1))
fsDhcpClientIntfConfigGroup.setObjects((_B,_E))
if mibBuilder.loadTexts:fsDhcpClientIntfConfigGroup.setStatus(_A)
fsDhcpClientMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,135,2,1,1))
fsDhcpClientMIBCompliance.setObjects((_B,_F))
if mibBuilder.loadTexts:fsDhcpClientMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsDhcpClientMIB':fsDhcpClientMIB,'fsDhcpClientMIBObjects':fsDhcpClientMIBObjects,'fsDhcpClientConfig':fsDhcpClientConfig,'fsDhcpClientIntfTable':fsDhcpClientIntfTable,'fsDhcpClientIntfEntry':fsDhcpClientIntfEntry,_D:fsDhcpIntfClientIndex,_E:fsDhcpClientIpAddrDhcpStatus,'fsDhcpClientMIBConformance':fsDhcpClientMIBConformance,'fsDhcpClientMIBCompliances':fsDhcpClientMIBCompliances,'fsDhcpClientMIBCompliance':fsDhcpClientMIBCompliance,'fsDhcpClientMIBGroups':fsDhcpClientMIBGroups,_F:fsDhcpClientIntfConfigGroup})