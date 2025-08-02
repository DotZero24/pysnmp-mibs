_G='swNlbMulticastFdbMacAddress'
_F='swNlbMulticastFdbVlanIndex'
_E='swNlbUnicastFdbMacAddress'
_D='not-accessible'
_C='read-create'
_B='NLB-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
PortList,VlanIndex=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
swNlbMIB=ModuleIdentity((1,3,6,1,4,1,171,12,77))
_SwNlbMgmt_ObjectIdentity=ObjectIdentity
swNlbMgmt=_SwNlbMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,77,3))
_SwNlbUnicastFdbTable_Object=MibTable
swNlbUnicastFdbTable=_SwNlbUnicastFdbTable_Object((1,3,6,1,4,1,171,12,77,3,1))
if mibBuilder.loadTexts:swNlbUnicastFdbTable.setStatus(_A)
_SwNlbUnicastFdbEntry_Object=MibTableRow
swNlbUnicastFdbEntry=_SwNlbUnicastFdbEntry_Object((1,3,6,1,4,1,171,12,77,3,1,1))
swNlbUnicastFdbEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:swNlbUnicastFdbEntry.setStatus(_A)
_SwNlbUnicastFdbMacAddress_Type=MacAddress
_SwNlbUnicastFdbMacAddress_Object=MibTableColumn
swNlbUnicastFdbMacAddress=_SwNlbUnicastFdbMacAddress_Object((1,3,6,1,4,1,171,12,77,3,1,1,1),_SwNlbUnicastFdbMacAddress_Type())
swNlbUnicastFdbMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:swNlbUnicastFdbMacAddress.setStatus(_A)
_SwNlbUnicastFdbEgressPorts_Type=PortList
_SwNlbUnicastFdbEgressPorts_Object=MibTableColumn
swNlbUnicastFdbEgressPorts=_SwNlbUnicastFdbEgressPorts_Object((1,3,6,1,4,1,171,12,77,3,1,1,2),_SwNlbUnicastFdbEgressPorts_Type())
swNlbUnicastFdbEgressPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:swNlbUnicastFdbEgressPorts.setStatus(_A)
_SwNlbUnicastFdbRowStatus_Type=RowStatus
_SwNlbUnicastFdbRowStatus_Object=MibTableColumn
swNlbUnicastFdbRowStatus=_SwNlbUnicastFdbRowStatus_Object((1,3,6,1,4,1,171,12,77,3,1,1,3),_SwNlbUnicastFdbRowStatus_Type())
swNlbUnicastFdbRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swNlbUnicastFdbRowStatus.setStatus(_A)
_SwNlbMulticastFdbTable_Object=MibTable
swNlbMulticastFdbTable=_SwNlbMulticastFdbTable_Object((1,3,6,1,4,1,171,12,77,3,2))
if mibBuilder.loadTexts:swNlbMulticastFdbTable.setStatus(_A)
_SwNlbMulticastFdbEntry_Object=MibTableRow
swNlbMulticastFdbEntry=_SwNlbMulticastFdbEntry_Object((1,3,6,1,4,1,171,12,77,3,2,1))
swNlbMulticastFdbEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:swNlbMulticastFdbEntry.setStatus(_A)
_SwNlbMulticastFdbVlanIndex_Type=VlanIndex
_SwNlbMulticastFdbVlanIndex_Object=MibTableColumn
swNlbMulticastFdbVlanIndex=_SwNlbMulticastFdbVlanIndex_Object((1,3,6,1,4,1,171,12,77,3,2,1,1),_SwNlbMulticastFdbVlanIndex_Type())
swNlbMulticastFdbVlanIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:swNlbMulticastFdbVlanIndex.setStatus(_A)
_SwNlbMulticastFdbMacAddress_Type=MacAddress
_SwNlbMulticastFdbMacAddress_Object=MibTableColumn
swNlbMulticastFdbMacAddress=_SwNlbMulticastFdbMacAddress_Object((1,3,6,1,4,1,171,12,77,3,2,1,2),_SwNlbMulticastFdbMacAddress_Type())
swNlbMulticastFdbMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:swNlbMulticastFdbMacAddress.setStatus(_A)
_SwNlbMulticastFdbEgressPorts_Type=PortList
_SwNlbMulticastFdbEgressPorts_Object=MibTableColumn
swNlbMulticastFdbEgressPorts=_SwNlbMulticastFdbEgressPorts_Object((1,3,6,1,4,1,171,12,77,3,2,1,3),_SwNlbMulticastFdbEgressPorts_Type())
swNlbMulticastFdbEgressPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:swNlbMulticastFdbEgressPorts.setStatus(_A)
_SwNlbMulticastFdbRowStatus_Type=RowStatus
_SwNlbMulticastFdbRowStatus_Object=MibTableColumn
swNlbMulticastFdbRowStatus=_SwNlbMulticastFdbRowStatus_Object((1,3,6,1,4,1,171,12,77,3,2,1,4),_SwNlbMulticastFdbRowStatus_Type())
swNlbMulticastFdbRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swNlbMulticastFdbRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'swNlbMIB':swNlbMIB,'swNlbMgmt':swNlbMgmt,'swNlbUnicastFdbTable':swNlbUnicastFdbTable,'swNlbUnicastFdbEntry':swNlbUnicastFdbEntry,_E:swNlbUnicastFdbMacAddress,'swNlbUnicastFdbEgressPorts':swNlbUnicastFdbEgressPorts,'swNlbUnicastFdbRowStatus':swNlbUnicastFdbRowStatus,'swNlbMulticastFdbTable':swNlbMulticastFdbTable,'swNlbMulticastFdbEntry':swNlbMulticastFdbEntry,_F:swNlbMulticastFdbVlanIndex,_G:swNlbMulticastFdbMacAddress,'swNlbMulticastFdbEgressPorts':swNlbMulticastFdbEgressPorts,'swNlbMulticastFdbRowStatus':swNlbMulticastFdbRowStatus})