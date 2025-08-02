_G='portMappingLogicalPort'
_F='portMappingLogicalSlot'
_E='Integer32'
_D='OctetString'
_C='TPT-PORT-MAPPING-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tpt_tpa_objs,=mibBuilder.importSymbols('TPT-TPAMIBS-MIB','tpt-tpa-objs')
tpt_port_mapping_objs=ModuleIdentity((1,3,6,1,4,1,10734,3,3,2,16))
if mibBuilder.loadTexts:tpt_port_mapping_objs.setRevisions(('2016-10-03 12:00','2016-05-25 18:54'))
_PortMappingTable_Object=MibTable
portMappingTable=_PortMappingTable_Object((1,3,6,1,4,1,10734,3,3,2,16,1))
if mibBuilder.loadTexts:portMappingTable.setStatus(_A)
_PortMappingEntry_Object=MibTableRow
portMappingEntry=_PortMappingEntry_Object((1,3,6,1,4,1,10734,3,3,2,16,1,1))
portMappingEntry.setIndexNames((0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:portMappingEntry.setStatus(_A)
_PortMappingLogicalSlot_Type=Unsigned32
_PortMappingLogicalSlot_Object=MibTableColumn
portMappingLogicalSlot=_PortMappingLogicalSlot_Object((1,3,6,1,4,1,10734,3,3,2,16,1,1,1),_PortMappingLogicalSlot_Type())
portMappingLogicalSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:portMappingLogicalSlot.setStatus(_A)
_PortMappingLogicalPort_Type=Unsigned32
_PortMappingLogicalPort_Object=MibTableColumn
portMappingLogicalPort=_PortMappingLogicalPort_Object((1,3,6,1,4,1,10734,3,3,2,16,1,1,2),_PortMappingLogicalPort_Type())
portMappingLogicalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:portMappingLogicalPort.setStatus(_A)
_PortMappingLogicalIfIndex_Type=InterfaceIndex
_PortMappingLogicalIfIndex_Object=MibTableColumn
portMappingLogicalIfIndex=_PortMappingLogicalIfIndex_Object((1,3,6,1,4,1,10734,3,3,2,16,1,1,3),_PortMappingLogicalIfIndex_Type())
portMappingLogicalIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:portMappingLogicalIfIndex.setStatus(_A)
_PortMappingPhysicalSlot_Type=Unsigned32
_PortMappingPhysicalSlot_Object=MibTableColumn
portMappingPhysicalSlot=_PortMappingPhysicalSlot_Object((1,3,6,1,4,1,10734,3,3,2,16,1,1,4),_PortMappingPhysicalSlot_Type())
portMappingPhysicalSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:portMappingPhysicalSlot.setStatus(_A)
_PortMappingPhysicalPort_Type=Unsigned32
_PortMappingPhysicalPort_Object=MibTableColumn
portMappingPhysicalPort=_PortMappingPhysicalPort_Object((1,3,6,1,4,1,10734,3,3,2,16,1,1,5),_PortMappingPhysicalPort_Type())
portMappingPhysicalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:portMappingPhysicalPort.setStatus(_A)
_PortMappingPhysicalIfIndex_Type=InterfaceIndex
_PortMappingPhysicalIfIndex_Object=MibTableColumn
portMappingPhysicalIfIndex=_PortMappingPhysicalIfIndex_Object((1,3,6,1,4,1,10734,3,3,2,16,1,1,6),_PortMappingPhysicalIfIndex_Type())
portMappingPhysicalIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:portMappingPhysicalIfIndex.setStatus(_A)
class _PortMappingSegmentName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_PortMappingSegmentName_Type.__name__=_D
_PortMappingSegmentName_Object=MibTableColumn
portMappingSegmentName=_PortMappingSegmentName_Object((1,3,6,1,4,1,10734,3,3,2,16,1,1,7),_PortMappingSegmentName_Type())
portMappingSegmentName.setMaxAccess(_B)
if mibBuilder.loadTexts:portMappingSegmentName.setStatus('obsolete')
class _PortMappingPhysicalVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_PortMappingPhysicalVlanId_Type.__name__=_E
_PortMappingPhysicalVlanId_Object=MibTableColumn
portMappingPhysicalVlanId=_PortMappingPhysicalVlanId_Object((1,3,6,1,4,1,10734,3,3,2,16,1,1,8),_PortMappingPhysicalVlanId_Type())
portMappingPhysicalVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:portMappingPhysicalVlanId.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'tpt-port-mapping-objs':tpt_port_mapping_objs,'portMappingTable':portMappingTable,'portMappingEntry':portMappingEntry,_F:portMappingLogicalSlot,_G:portMappingLogicalPort,'portMappingLogicalIfIndex':portMappingLogicalIfIndex,'portMappingPhysicalSlot':portMappingPhysicalSlot,'portMappingPhysicalPort':portMappingPhysicalPort,'portMappingPhysicalIfIndex':portMappingPhysicalIfIndex,'portMappingSegmentName':portMappingSegmentName,'portMappingPhysicalVlanId':portMappingPhysicalVlanId})