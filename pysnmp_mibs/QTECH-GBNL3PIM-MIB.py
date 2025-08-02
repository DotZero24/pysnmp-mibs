_E='pimInterfaceIndex'
_D='QTECH-GBNL3PIM-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
gbnL3,=mibBuilder.importSymbols('QTECH-MASTER-MIB','gbnL3')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
gbnL3PimMib=ModuleIdentity((1,3,6,1,4,1,27514,1,2,5,8))
if mibBuilder.loadTexts:gbnL3PimMib.setRevisions(('1905-07-04 00:01',))
_GbnL3PimGroup_ObjectIdentity=ObjectIdentity
gbnL3PimGroup=_GbnL3PimGroup_ObjectIdentity((1,3,6,1,4,1,27514,1,2,5,8,1))
_PimCommonTraceOption_Type=Unsigned32
_PimCommonTraceOption_Object=MibScalar
pimCommonTraceOption=_PimCommonTraceOption_Object((1,3,6,1,4,1,27514,1,2,5,8,1,1),_PimCommonTraceOption_Type())
pimCommonTraceOption.setMaxAccess(_B)
if mibBuilder.loadTexts:pimCommonTraceOption.setStatus(_A)
_PimDmTraceOption_Type=Unsigned32
_PimDmTraceOption_Object=MibScalar
pimDmTraceOption=_PimDmTraceOption_Object((1,3,6,1,4,1,27514,1,2,5,8,1,2),_PimDmTraceOption_Type())
pimDmTraceOption.setMaxAccess(_B)
if mibBuilder.loadTexts:pimDmTraceOption.setStatus(_A)
_PimSmTraceOption_Type=Unsigned32
_PimSmTraceOption_Object=MibScalar
pimSmTraceOption=_PimSmTraceOption_Object((1,3,6,1,4,1,27514,1,2,5,8,1,3),_PimSmTraceOption_Type())
pimSmTraceOption.setMaxAccess(_B)
if mibBuilder.loadTexts:pimSmTraceOption.setStatus(_A)
class _PimSourcePolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_PimSourcePolicy_Type.__name__=_C
_PimSourcePolicy_Object=MibScalar
pimSourcePolicy=_PimSourcePolicy_Object((1,3,6,1,4,1,27514,1,2,5,8,1,4),_PimSourcePolicy_Type())
pimSourcePolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:pimSourcePolicy.setStatus(_A)
_PimInterfaceExtraTable_Object=MibTable
pimInterfaceExtraTable=_PimInterfaceExtraTable_Object((1,3,6,1,4,1,27514,1,2,5,8,2))
if mibBuilder.loadTexts:pimInterfaceExtraTable.setStatus(_A)
_PimInterfaceExtraEntry_Object=MibTableRow
pimInterfaceExtraEntry=_PimInterfaceExtraEntry_Object((1,3,6,1,4,1,27514,1,2,5,8,2,1))
pimInterfaceExtraEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:pimInterfaceExtraEntry.setStatus(_A)
_PimInterfaceIndex_Type=InterfaceIndex
_PimInterfaceIndex_Object=MibTableColumn
pimInterfaceIndex=_PimInterfaceIndex_Object((1,3,6,1,4,1,27514,1,2,5,8,2,1,1),_PimInterfaceIndex_Type())
pimInterfaceIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:pimInterfaceIndex.setStatus(_A)
class _PimInterfaceNeighborLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_PimInterfaceNeighborLimit_Type.__name__=_C
_PimInterfaceNeighborLimit_Object=MibTableColumn
pimInterfaceNeighborLimit=_PimInterfaceNeighborLimit_Object((1,3,6,1,4,1,27514,1,2,5,8,2,1,2),_PimInterfaceNeighborLimit_Type())
pimInterfaceNeighborLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:pimInterfaceNeighborLimit.setStatus(_A)
class _PimInterfaceNeighborPolicy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_PimInterfaceNeighborPolicy_Type.__name__=_C
_PimInterfaceNeighborPolicy_Object=MibTableColumn
pimInterfaceNeighborPolicy=_PimInterfaceNeighborPolicy_Object((1,3,6,1,4,1,27514,1,2,5,8,2,1,3),_PimInterfaceNeighborPolicy_Type())
pimInterfaceNeighborPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:pimInterfaceNeighborPolicy.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'gbnL3PimMib':gbnL3PimMib,'gbnL3PimGroup':gbnL3PimGroup,'pimCommonTraceOption':pimCommonTraceOption,'pimDmTraceOption':pimDmTraceOption,'pimSmTraceOption':pimSmTraceOption,'pimSourcePolicy':pimSourcePolicy,'pimInterfaceExtraTable':pimInterfaceExtraTable,'pimInterfaceExtraEntry':pimInterfaceExtraEntry,_E:pimInterfaceIndex,'pimInterfaceNeighborLimit':pimInterfaceNeighborLimit,'pimInterfaceNeighborPolicy':pimInterfaceNeighborPolicy})