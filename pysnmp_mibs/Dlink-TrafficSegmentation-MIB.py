_H='rlTrafficSegIndex'
_G='read-create'
_F='not-accessible'
_E='rlTrafficSegConfigIndex'
_D='Dlink-TrafficSegmentation-MIB'
_C='Unsigned32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('DLINK-3100-MIB','rnd')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
rlTrafficSeg=ModuleIdentity((1,3,6,1,4,1,171,10,94,89,89,138))
if mibBuilder.loadTexts:rlTrafficSeg.setRevisions(('2008-05-03 12:34',))
_RlTrafficSegConfigTable_Object=MibTable
rlTrafficSegConfigTable=_RlTrafficSegConfigTable_Object((1,3,6,1,4,1,171,10,94,89,89,138,1))
if mibBuilder.loadTexts:rlTrafficSegConfigTable.setStatus(_A)
_RlTrafficSegConfigEntry_Object=MibTableRow
rlTrafficSegConfigEntry=_RlTrafficSegConfigEntry_Object((1,3,6,1,4,1,171,10,94,89,89,138,1,1))
rlTrafficSegConfigEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:rlTrafficSegConfigEntry.setStatus(_A)
class _RlTrafficSegConfigIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RlTrafficSegConfigIndex_Type.__name__=_C
_RlTrafficSegConfigIndex_Object=MibTableColumn
rlTrafficSegConfigIndex=_RlTrafficSegConfigIndex_Object((1,3,6,1,4,1,171,10,94,89,89,138,1,1,1),_RlTrafficSegConfigIndex_Type())
rlTrafficSegConfigIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlTrafficSegConfigIndex.setStatus(_A)
_RlTrafficSegConfigIngressPorts_Type=PortList
_RlTrafficSegConfigIngressPorts_Object=MibTableColumn
rlTrafficSegConfigIngressPorts=_RlTrafficSegConfigIngressPorts_Object((1,3,6,1,4,1,171,10,94,89,89,138,1,1,2),_RlTrafficSegConfigIngressPorts_Type())
rlTrafficSegConfigIngressPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:rlTrafficSegConfigIngressPorts.setStatus(_A)
_RlTrafficSegConfigEgressPorts_Type=PortList
_RlTrafficSegConfigEgressPorts_Object=MibTableColumn
rlTrafficSegConfigEgressPorts=_RlTrafficSegConfigEgressPorts_Object((1,3,6,1,4,1,171,10,94,89,89,138,1,1,3),_RlTrafficSegConfigEgressPorts_Type())
rlTrafficSegConfigEgressPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:rlTrafficSegConfigEgressPorts.setStatus(_A)
_RlTrafficSegConfigRowStatus_Type=RowStatus
_RlTrafficSegConfigRowStatus_Object=MibTableColumn
rlTrafficSegConfigRowStatus=_RlTrafficSegConfigRowStatus_Object((1,3,6,1,4,1,171,10,94,89,89,138,1,1,4),_RlTrafficSegConfigRowStatus_Type())
rlTrafficSegConfigRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:rlTrafficSegConfigRowStatus.setStatus(_A)
_RlTrafficSegTable_Object=MibTable
rlTrafficSegTable=_RlTrafficSegTable_Object((1,3,6,1,4,1,171,10,94,89,89,138,2))
if mibBuilder.loadTexts:rlTrafficSegTable.setStatus(_A)
_RlTrafficSegEntry_Object=MibTableRow
rlTrafficSegEntry=_RlTrafficSegEntry_Object((1,3,6,1,4,1,171,10,94,89,89,138,2,1))
rlTrafficSegEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:rlTrafficSegEntry.setStatus(_A)
class _RlTrafficSegIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RlTrafficSegIndex_Type.__name__=_C
_RlTrafficSegIndex_Object=MibTableColumn
rlTrafficSegIndex=_RlTrafficSegIndex_Object((1,3,6,1,4,1,171,10,94,89,89,138,2,1,1),_RlTrafficSegIndex_Type())
rlTrafficSegIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:rlTrafficSegIndex.setStatus(_A)
_RlTrafficSegIngressPorts_Type=PortList
_RlTrafficSegIngressPorts_Object=MibTableColumn
rlTrafficSegIngressPorts=_RlTrafficSegIngressPorts_Object((1,3,6,1,4,1,171,10,94,89,89,138,2,1,2),_RlTrafficSegIngressPorts_Type())
rlTrafficSegIngressPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:rlTrafficSegIngressPorts.setStatus(_A)
_RlTrafficSegEgressPorts_Type=PortList
_RlTrafficSegEgressPorts_Object=MibTableColumn
rlTrafficSegEgressPorts=_RlTrafficSegEgressPorts_Object((1,3,6,1,4,1,171,10,94,89,89,138,2,1,3),_RlTrafficSegEgressPorts_Type())
rlTrafficSegEgressPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:rlTrafficSegEgressPorts.setStatus(_A)
_RlTrafficSegRowStatus_Type=RowStatus
_RlTrafficSegRowStatus_Object=MibTableColumn
rlTrafficSegRowStatus=_RlTrafficSegRowStatus_Object((1,3,6,1,4,1,171,10,94,89,89,138,2,1,4),_RlTrafficSegRowStatus_Type())
rlTrafficSegRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:rlTrafficSegRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'rlTrafficSeg':rlTrafficSeg,'rlTrafficSegConfigTable':rlTrafficSegConfigTable,'rlTrafficSegConfigEntry':rlTrafficSegConfigEntry,_E:rlTrafficSegConfigIndex,'rlTrafficSegConfigIngressPorts':rlTrafficSegConfigIngressPorts,'rlTrafficSegConfigEgressPorts':rlTrafficSegConfigEgressPorts,'rlTrafficSegConfigRowStatus':rlTrafficSegConfigRowStatus,'rlTrafficSegTable':rlTrafficSegTable,'rlTrafficSegEntry':rlTrafficSegEntry,_H:rlTrafficSegIndex,'rlTrafficSegIngressPorts':rlTrafficSegIngressPorts,'rlTrafficSegEgressPorts':rlTrafficSegEgressPorts,'rlTrafficSegRowStatus':rlTrafficSegRowStatus})