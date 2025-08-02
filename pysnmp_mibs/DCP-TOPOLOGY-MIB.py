_H='dcpTopologyTableGroupV1'
_G='dcpTopologyInternalDestination'
_F='dcpTopologyInternalSource'
_E='read-only'
_D='dcpTopologyInternalId'
_C='Unsigned32'
_B='DCP-TOPOLOGY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dcpGeneric,=mibBuilder.importSymbols('DCP-MIB','dcpGeneric')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
dcpTopology=ModuleIdentity((1,3,6,1,4,1,30826,2,2,5))
if mibBuilder.loadTexts:dcpTopology.setRevisions(('2021-12-30 08:00',))
_DcpTopologyObjects_ObjectIdentity=ObjectIdentity
dcpTopologyObjects=_DcpTopologyObjects_ObjectIdentity((1,3,6,1,4,1,30826,2,2,5,1))
_DcpTopologyInternalTable_Object=MibTable
dcpTopologyInternalTable=_DcpTopologyInternalTable_Object((1,3,6,1,4,1,30826,2,2,5,1,1))
if mibBuilder.loadTexts:dcpTopologyInternalTable.setStatus(_A)
_DcpTopologyInternalEntry_Object=MibTableRow
dcpTopologyInternalEntry=_DcpTopologyInternalEntry_Object((1,3,6,1,4,1,30826,2,2,5,1,1,1))
dcpTopologyInternalEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:dcpTopologyInternalEntry.setStatus(_A)
class _DcpTopologyInternalId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000000))
_DcpTopologyInternalId_Type.__name__=_C
_DcpTopologyInternalId_Object=MibTableColumn
dcpTopologyInternalId=_DcpTopologyInternalId_Object((1,3,6,1,4,1,30826,2,2,5,1,1,1,1),_DcpTopologyInternalId_Type())
dcpTopologyInternalId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:dcpTopologyInternalId.setStatus(_A)
_DcpTopologyInternalSource_Type=DisplayString
_DcpTopologyInternalSource_Object=MibTableColumn
dcpTopologyInternalSource=_DcpTopologyInternalSource_Object((1,3,6,1,4,1,30826,2,2,5,1,1,1,2),_DcpTopologyInternalSource_Type())
dcpTopologyInternalSource.setMaxAccess(_E)
if mibBuilder.loadTexts:dcpTopologyInternalSource.setStatus(_A)
_DcpTopologyInternalDestination_Type=DisplayString
_DcpTopologyInternalDestination_Object=MibTableColumn
dcpTopologyInternalDestination=_DcpTopologyInternalDestination_Object((1,3,6,1,4,1,30826,2,2,5,1,1,1,3),_DcpTopologyInternalDestination_Type())
dcpTopologyInternalDestination.setMaxAccess(_E)
if mibBuilder.loadTexts:dcpTopologyInternalDestination.setStatus(_A)
_DcpTopologyMIBCompliance_ObjectIdentity=ObjectIdentity
dcpTopologyMIBCompliance=_DcpTopologyMIBCompliance_ObjectIdentity((1,3,6,1,4,1,30826,2,2,5,2))
_DcpTopologyMIBGroups_ObjectIdentity=ObjectIdentity
dcpTopologyMIBGroups=_DcpTopologyMIBGroups_ObjectIdentity((1,3,6,1,4,1,30826,2,2,5,2,1))
_DcpTopologyMIBCompliances_ObjectIdentity=ObjectIdentity
dcpTopologyMIBCompliances=_DcpTopologyMIBCompliances_ObjectIdentity((1,3,6,1,4,1,30826,2,2,5,2,2))
dcpTopologyTableGroupV1=ObjectGroup((1,3,6,1,4,1,30826,2,2,5,2,1,1))
dcpTopologyTableGroupV1.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:dcpTopologyTableGroupV1.setStatus(_A)
dcpTopologyBasicComplV1=ModuleCompliance((1,3,6,1,4,1,30826,2,2,5,2,2,1))
dcpTopologyBasicComplV1.setObjects((_B,_H))
if mibBuilder.loadTexts:dcpTopologyBasicComplV1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'dcpTopology':dcpTopology,'dcpTopologyObjects':dcpTopologyObjects,'dcpTopologyInternalTable':dcpTopologyInternalTable,'dcpTopologyInternalEntry':dcpTopologyInternalEntry,_D:dcpTopologyInternalId,_F:dcpTopologyInternalSource,_G:dcpTopologyInternalDestination,'dcpTopologyMIBCompliance':dcpTopologyMIBCompliance,'dcpTopologyMIBGroups':dcpTopologyMIBGroups,_H:dcpTopologyTableGroupV1,'dcpTopologyMIBCompliances':dcpTopologyMIBCompliances,'dcpTopologyBasicComplV1':dcpTopologyBasicComplV1})