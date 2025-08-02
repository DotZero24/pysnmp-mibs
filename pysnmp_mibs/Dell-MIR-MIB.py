_I='rlMirVlanBaseLogicalPortsIfIndex'
_H='rlMirVlanBaseReservedPortsIfIndex'
_G='rlMirInterfaceIfIndex'
_F='Dell-MIR-MIB'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rnd,=mibBuilder.importSymbols('Dell-MIB','rnd')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
rlMir=ModuleIdentity((1,3,6,1,4,1,89,61))
if mibBuilder.loadTexts:rlMir.setRevisions(('2007-01-02 00:00',))
_RlMirMibVersion_Type=Integer32
_RlMirMibVersion_Object=MibScalar
rlMirMibVersion=_RlMirMibVersion_Object((1,3,6,1,4,1,89,61,1),_RlMirMibVersion_Type())
rlMirMibVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:rlMirMibVersion.setStatus(_A)
class _RlMirMaxNumOfMRIsAfterReset_Type(Integer32):defaultValue=1
_RlMirMaxNumOfMRIsAfterReset_Type.__name__=_C
_RlMirMaxNumOfMRIsAfterReset_Object=MibScalar
rlMirMaxNumOfMRIsAfterReset=_RlMirMaxNumOfMRIsAfterReset_Object((1,3,6,1,4,1,89,61,2),_RlMirMaxNumOfMRIsAfterReset_Type())
rlMirMaxNumOfMRIsAfterReset.setMaxAccess(_E)
if mibBuilder.loadTexts:rlMirMaxNumOfMRIsAfterReset.setStatus(_A)
_RlMirMaxNumOfMRIs_Type=Integer32
_RlMirMaxNumOfMRIs_Object=MibScalar
rlMirMaxNumOfMRIs=_RlMirMaxNumOfMRIs_Object((1,3,6,1,4,1,89,61,3),_RlMirMaxNumOfMRIs_Type())
rlMirMaxNumOfMRIs.setMaxAccess(_D)
if mibBuilder.loadTexts:rlMirMaxNumOfMRIs.setStatus(_A)
_RlMirCurMriNum_Type=Integer32
_RlMirCurMriNum_Object=MibScalar
rlMirCurMriNum=_RlMirCurMriNum_Object((1,3,6,1,4,1,89,61,4),_RlMirCurMriNum_Type())
rlMirCurMriNum.setMaxAccess(_E)
if mibBuilder.loadTexts:rlMirCurMriNum.setStatus(_A)
_RlMirInterfaceTable_Object=MibTable
rlMirInterfaceTable=_RlMirInterfaceTable_Object((1,3,6,1,4,1,89,61,5))
if mibBuilder.loadTexts:rlMirInterfaceTable.setStatus(_A)
_RlMirInterfaceEntry_Object=MibTableRow
rlMirInterfaceEntry=_RlMirInterfaceEntry_Object((1,3,6,1,4,1,89,61,5,1))
rlMirInterfaceEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:rlMirInterfaceEntry.setStatus(_A)
_RlMirInterfaceIfIndex_Type=InterfaceIndex
_RlMirInterfaceIfIndex_Object=MibTableColumn
rlMirInterfaceIfIndex=_RlMirInterfaceIfIndex_Object((1,3,6,1,4,1,89,61,5,1,1),_RlMirInterfaceIfIndex_Type())
rlMirInterfaceIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:rlMirInterfaceIfIndex.setStatus(_A)
class _RlMirInterfaceMrid_Type(Integer32):defaultValue=0
_RlMirInterfaceMrid_Type.__name__=_C
_RlMirInterfaceMrid_Object=MibTableColumn
rlMirInterfaceMrid=_RlMirInterfaceMrid_Object((1,3,6,1,4,1,89,61,5,1,2),_RlMirInterfaceMrid_Type())
rlMirInterfaceMrid.setMaxAccess(_E)
if mibBuilder.loadTexts:rlMirInterfaceMrid.setStatus(_A)
_RlMirVlanBaseReservedPortsTable_Object=MibTable
rlMirVlanBaseReservedPortsTable=_RlMirVlanBaseReservedPortsTable_Object((1,3,6,1,4,1,89,61,6))
if mibBuilder.loadTexts:rlMirVlanBaseReservedPortsTable.setStatus(_A)
_RlMirVlanBaseReservedPortsEntry_Object=MibTableRow
rlMirVlanBaseReservedPortsEntry=_RlMirVlanBaseReservedPortsEntry_Object((1,3,6,1,4,1,89,61,6,1))
rlMirVlanBaseReservedPortsEntry.setIndexNames((0,_F,_H))
if mibBuilder.loadTexts:rlMirVlanBaseReservedPortsEntry.setStatus(_A)
_RlMirVlanBaseReservedPortsIfIndex_Type=InterfaceIndex
_RlMirVlanBaseReservedPortsIfIndex_Object=MibTableColumn
rlMirVlanBaseReservedPortsIfIndex=_RlMirVlanBaseReservedPortsIfIndex_Object((1,3,6,1,4,1,89,61,6,1,1),_RlMirVlanBaseReservedPortsIfIndex_Type())
rlMirVlanBaseReservedPortsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMirVlanBaseReservedPortsIfIndex.setStatus(_A)
_RlMirVlanBaseReservedPortsStatus_Type=RowStatus
_RlMirVlanBaseReservedPortsStatus_Object=MibTableColumn
rlMirVlanBaseReservedPortsStatus=_RlMirVlanBaseReservedPortsStatus_Object((1,3,6,1,4,1,89,61,6,1,2),_RlMirVlanBaseReservedPortsStatus_Type())
rlMirVlanBaseReservedPortsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMirVlanBaseReservedPortsStatus.setStatus(_A)
_RlMirVlanBaseLogicalPortsTable_Object=MibTable
rlMirVlanBaseLogicalPortsTable=_RlMirVlanBaseLogicalPortsTable_Object((1,3,6,1,4,1,89,61,7))
if mibBuilder.loadTexts:rlMirVlanBaseLogicalPortsTable.setStatus(_A)
_RlMirVlanBaseLogicalPortsEntry_Object=MibTableRow
rlMirVlanBaseLogicalPortsEntry=_RlMirVlanBaseLogicalPortsEntry_Object((1,3,6,1,4,1,89,61,7,1))
rlMirVlanBaseLogicalPortsEntry.setIndexNames((0,_F,_I))
if mibBuilder.loadTexts:rlMirVlanBaseLogicalPortsEntry.setStatus(_A)
_RlMirVlanBaseLogicalPortsIfIndex_Type=InterfaceIndex
_RlMirVlanBaseLogicalPortsIfIndex_Object=MibTableColumn
rlMirVlanBaseLogicalPortsIfIndex=_RlMirVlanBaseLogicalPortsIfIndex_Object((1,3,6,1,4,1,89,61,7,1,1),_RlMirVlanBaseLogicalPortsIfIndex_Type())
rlMirVlanBaseLogicalPortsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMirVlanBaseLogicalPortsIfIndex.setStatus(_A)
_RlMirVlanBaseLogicalPortsReservedIfIndex_Type=InterfaceIndex
_RlMirVlanBaseLogicalPortsReservedIfIndex_Object=MibTableColumn
rlMirVlanBaseLogicalPortsReservedIfIndex=_RlMirVlanBaseLogicalPortsReservedIfIndex_Object((1,3,6,1,4,1,89,61,7,1,2),_RlMirVlanBaseLogicalPortsReservedIfIndex_Type())
rlMirVlanBaseLogicalPortsReservedIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMirVlanBaseLogicalPortsReservedIfIndex.setStatus(_A)
class _RlMirVlanBaseLogicalPortsVlanTag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_RlMirVlanBaseLogicalPortsVlanTag_Type.__name__=_C
_RlMirVlanBaseLogicalPortsVlanTag_Object=MibTableColumn
rlMirVlanBaseLogicalPortsVlanTag=_RlMirVlanBaseLogicalPortsVlanTag_Object((1,3,6,1,4,1,89,61,7,1,3),_RlMirVlanBaseLogicalPortsVlanTag_Type())
rlMirVlanBaseLogicalPortsVlanTag.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMirVlanBaseLogicalPortsVlanTag.setStatus(_A)
_RlMirVlanBaseLogicalPortsStatus_Type=RowStatus
_RlMirVlanBaseLogicalPortsStatus_Object=MibTableColumn
rlMirVlanBaseLogicalPortsStatus=_RlMirVlanBaseLogicalPortsStatus_Object((1,3,6,1,4,1,89,61,7,1,4),_RlMirVlanBaseLogicalPortsStatus_Type())
rlMirVlanBaseLogicalPortsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlMirVlanBaseLogicalPortsStatus.setStatus(_A)
_RlMirCurMriNumRouter_Type=Integer32
_RlMirCurMriNumRouter_Object=MibScalar
rlMirCurMriNumRouter=_RlMirCurMriNumRouter_Object((1,3,6,1,4,1,89,61,8),_RlMirCurMriNumRouter_Type())
rlMirCurMriNumRouter.setMaxAccess(_D)
if mibBuilder.loadTexts:rlMirCurMriNumRouter.setStatus(_A)
_RlMirCurMriNumOob_Type=Integer32
_RlMirCurMriNumOob_Object=MibScalar
rlMirCurMriNumOob=_RlMirCurMriNumOob_Object((1,3,6,1,4,1,89,61,9),_RlMirCurMriNumOob_Type())
rlMirCurMriNumOob.setMaxAccess(_D)
if mibBuilder.loadTexts:rlMirCurMriNumOob.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'rlMir':rlMir,'rlMirMibVersion':rlMirMibVersion,'rlMirMaxNumOfMRIsAfterReset':rlMirMaxNumOfMRIsAfterReset,'rlMirMaxNumOfMRIs':rlMirMaxNumOfMRIs,'rlMirCurMriNum':rlMirCurMriNum,'rlMirInterfaceTable':rlMirInterfaceTable,'rlMirInterfaceEntry':rlMirInterfaceEntry,_G:rlMirInterfaceIfIndex,'rlMirInterfaceMrid':rlMirInterfaceMrid,'rlMirVlanBaseReservedPortsTable':rlMirVlanBaseReservedPortsTable,'rlMirVlanBaseReservedPortsEntry':rlMirVlanBaseReservedPortsEntry,_H:rlMirVlanBaseReservedPortsIfIndex,'rlMirVlanBaseReservedPortsStatus':rlMirVlanBaseReservedPortsStatus,'rlMirVlanBaseLogicalPortsTable':rlMirVlanBaseLogicalPortsTable,'rlMirVlanBaseLogicalPortsEntry':rlMirVlanBaseLogicalPortsEntry,_I:rlMirVlanBaseLogicalPortsIfIndex,'rlMirVlanBaseLogicalPortsReservedIfIndex':rlMirVlanBaseLogicalPortsReservedIfIndex,'rlMirVlanBaseLogicalPortsVlanTag':rlMirVlanBaseLogicalPortsVlanTag,'rlMirVlanBaseLogicalPortsStatus':rlMirVlanBaseLogicalPortsStatus,'rlMirCurMriNumRouter':rlMirCurMriNumRouter,'rlMirCurMriNumOob':rlMirCurMriNumOob})