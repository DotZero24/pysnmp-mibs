_F='TruthValue'
_E='read-write'
_D='Integer32'
_C='ifIndex'
_B='IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_B,_C)
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
rnd,=mibBuilder.importSymbols('RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_F)
rlProtectedPorts=ModuleIdentity((1,3,6,1,4,1,89,132))
if mibBuilder.loadTexts:rlProtectedPorts.setRevisions(('2008-05-03 12:34',))
_RlProtectedPortsTable_Object=MibTable
rlProtectedPortsTable=_RlProtectedPortsTable_Object((1,3,6,1,4,1,89,132,1))
if mibBuilder.loadTexts:rlProtectedPortsTable.setStatus(_A)
_RlProtectedPortsEntry_Object=MibTableRow
rlProtectedPortsEntry=_RlProtectedPortsEntry_Object((1,3,6,1,4,1,89,132,1,1))
rlProtectedPortsEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:rlProtectedPortsEntry.setStatus(_A)
class _RlProtectedPortType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('not-protected',1),('protected',2)))
_RlProtectedPortType_Type.__name__=_D
_RlProtectedPortType_Object=MibTableColumn
rlProtectedPortType=_RlProtectedPortType_Object((1,3,6,1,4,1,89,132,1,1,1),_RlProtectedPortType_Type())
rlProtectedPortType.setMaxAccess(_E)
if mibBuilder.loadTexts:rlProtectedPortType.setStatus(_A)
class _RlProtectedPortCommunity_Type(Integer32):defaultValue=0
_RlProtectedPortCommunity_Type.__name__=_D
_RlProtectedPortCommunity_Object=MibTableColumn
rlProtectedPortCommunity=_RlProtectedPortCommunity_Object((1,3,6,1,4,1,89,132,1,1,2),_RlProtectedPortCommunity_Type())
rlProtectedPortCommunity.setMaxAccess(_E)
if mibBuilder.loadTexts:rlProtectedPortCommunity.setStatus(_A)
_RlProtectedPortsStatusTable_Object=MibTable
rlProtectedPortsStatusTable=_RlProtectedPortsStatusTable_Object((1,3,6,1,4,1,89,132,2))
if mibBuilder.loadTexts:rlProtectedPortsStatusTable.setStatus(_A)
_RlProtectedPortsStatusEntry_Object=MibTableRow
rlProtectedPortsStatusEntry=_RlProtectedPortsStatusEntry_Object((1,3,6,1,4,1,89,132,2,1))
rlProtectedPortsStatusEntry.setIndexNames((0,_B,_C))
if mibBuilder.loadTexts:rlProtectedPortsStatusEntry.setStatus(_A)
_RlProtectedPortEgressPorts_Type=PortList
_RlProtectedPortEgressPorts_Object=MibTableColumn
rlProtectedPortEgressPorts=_RlProtectedPortEgressPorts_Object((1,3,6,1,4,1,89,132,2,1,1),_RlProtectedPortEgressPorts_Type())
rlProtectedPortEgressPorts.setMaxAccess('read-only')
if mibBuilder.loadTexts:rlProtectedPortEgressPorts.setStatus(_A)
class _RlProtectedPortsGlobalEnable_Type(TruthValue):defaultValue=2
_RlProtectedPortsGlobalEnable_Type.__name__=_F
_RlProtectedPortsGlobalEnable_Object=MibScalar
rlProtectedPortsGlobalEnable=_RlProtectedPortsGlobalEnable_Object((1,3,6,1,4,1,89,132,3),_RlProtectedPortsGlobalEnable_Type())
rlProtectedPortsGlobalEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:rlProtectedPortsGlobalEnable.setStatus(_A)
mibBuilder.exportSymbols('MARVELL-ProtectedPorts-MIB',**{'rlProtectedPorts':rlProtectedPorts,'rlProtectedPortsTable':rlProtectedPortsTable,'rlProtectedPortsEntry':rlProtectedPortsEntry,'rlProtectedPortType':rlProtectedPortType,'rlProtectedPortCommunity':rlProtectedPortCommunity,'rlProtectedPortsStatusTable':rlProtectedPortsStatusTable,'rlProtectedPortsStatusEntry':rlProtectedPortsStatusEntry,'rlProtectedPortEgressPorts':rlProtectedPortEgressPorts,'rlProtectedPortsGlobalEnable':rlProtectedPortsGlobalEnable})