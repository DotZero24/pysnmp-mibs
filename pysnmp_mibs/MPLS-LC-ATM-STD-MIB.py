_R='mplsLcAtmStdIfConfStorageType'
_Q='mplsLcAtmStdIfConfRowStatus'
_P='mplsLcAtmLcAtmVPI'
_O='mplsLcAtmVcDirectlyConnected'
_N='mplsLcAtmStdVcMerge'
_M='mplsLcAtmStdUnlabTrafVci'
_L='mplsLcAtmStdUnlabTrafVpi'
_K='mplsLcAtmStdCtrlVci'
_J='mplsLcAtmStdCtrlVpi'
_I='StorageType'
_H='mplsInterfaceIndex'
_G='MPLS-LSR-STD-MIB'
_F='AtmVpIdentifier'
_E='mplsLcAtmStdIfGroup'
_D='TruthValue'
_C='read-create'
_B='MPLS-LC-ATM-STD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AtmVpIdentifier,=mibBuilder.importSymbols('ATM-TC-MIB',_F)
mplsInterfaceIndex,=mibBuilder.importSymbols(_G,_H)
MplsAtmVcIdentifier,mplsStdMIB=mibBuilder.importSymbols('MPLS-TC-STD-MIB','MplsAtmVcIdentifier','mplsStdMIB')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_I,'TextualConvention',_D)
mplsLcAtmStdMIB=ModuleIdentity((1,3,6,1,2,1,10,166,9))
if mibBuilder.loadTexts:mplsLcAtmStdMIB.setRevisions(('2006-01-12 00:00',))
_MplsLcAtmStdNotifications_ObjectIdentity=ObjectIdentity
mplsLcAtmStdNotifications=_MplsLcAtmStdNotifications_ObjectIdentity((1,3,6,1,2,1,10,166,9,0))
_MplsLcAtmStdObjects_ObjectIdentity=ObjectIdentity
mplsLcAtmStdObjects=_MplsLcAtmStdObjects_ObjectIdentity((1,3,6,1,2,1,10,166,9,1))
_MplsLcAtmStdInterfaceConfTable_Object=MibTable
mplsLcAtmStdInterfaceConfTable=_MplsLcAtmStdInterfaceConfTable_Object((1,3,6,1,2,1,10,166,9,1,1))
if mibBuilder.loadTexts:mplsLcAtmStdInterfaceConfTable.setStatus(_A)
_MplsLcAtmStdInterfaceConfEntry_Object=MibTableRow
mplsLcAtmStdInterfaceConfEntry=_MplsLcAtmStdInterfaceConfEntry_Object((1,3,6,1,2,1,10,166,9,1,1,1))
mplsLcAtmStdInterfaceConfEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:mplsLcAtmStdInterfaceConfEntry.setStatus(_A)
_MplsLcAtmStdCtrlVpi_Type=AtmVpIdentifier
_MplsLcAtmStdCtrlVpi_Object=MibTableColumn
mplsLcAtmStdCtrlVpi=_MplsLcAtmStdCtrlVpi_Object((1,3,6,1,2,1,10,166,9,1,1,1,1),_MplsLcAtmStdCtrlVpi_Type())
mplsLcAtmStdCtrlVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLcAtmStdCtrlVpi.setStatus(_A)
_MplsLcAtmStdCtrlVci_Type=MplsAtmVcIdentifier
_MplsLcAtmStdCtrlVci_Object=MibTableColumn
mplsLcAtmStdCtrlVci=_MplsLcAtmStdCtrlVci_Object((1,3,6,1,2,1,10,166,9,1,1,1,2),_MplsLcAtmStdCtrlVci_Type())
mplsLcAtmStdCtrlVci.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLcAtmStdCtrlVci.setStatus(_A)
_MplsLcAtmStdUnlabTrafVpi_Type=AtmVpIdentifier
_MplsLcAtmStdUnlabTrafVpi_Object=MibTableColumn
mplsLcAtmStdUnlabTrafVpi=_MplsLcAtmStdUnlabTrafVpi_Object((1,3,6,1,2,1,10,166,9,1,1,1,3),_MplsLcAtmStdUnlabTrafVpi_Type())
mplsLcAtmStdUnlabTrafVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLcAtmStdUnlabTrafVpi.setStatus(_A)
_MplsLcAtmStdUnlabTrafVci_Type=MplsAtmVcIdentifier
_MplsLcAtmStdUnlabTrafVci_Object=MibTableColumn
mplsLcAtmStdUnlabTrafVci=_MplsLcAtmStdUnlabTrafVci_Object((1,3,6,1,2,1,10,166,9,1,1,1,4),_MplsLcAtmStdUnlabTrafVci_Type())
mplsLcAtmStdUnlabTrafVci.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLcAtmStdUnlabTrafVci.setStatus(_A)
class _MplsLcAtmStdVcMerge_Type(TruthValue):defaultValue=2
_MplsLcAtmStdVcMerge_Type.__name__=_D
_MplsLcAtmStdVcMerge_Object=MibTableColumn
mplsLcAtmStdVcMerge=_MplsLcAtmStdVcMerge_Object((1,3,6,1,2,1,10,166,9,1,1,1,5),_MplsLcAtmStdVcMerge_Type())
mplsLcAtmStdVcMerge.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLcAtmStdVcMerge.setStatus(_A)
class _MplsLcAtmVcDirectlyConnected_Type(TruthValue):defaultValue=1
_MplsLcAtmVcDirectlyConnected_Type.__name__=_D
_MplsLcAtmVcDirectlyConnected_Object=MibTableColumn
mplsLcAtmVcDirectlyConnected=_MplsLcAtmVcDirectlyConnected_Object((1,3,6,1,2,1,10,166,9,1,1,1,6),_MplsLcAtmVcDirectlyConnected_Type())
mplsLcAtmVcDirectlyConnected.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLcAtmVcDirectlyConnected.setStatus(_A)
class _MplsLcAtmLcAtmVPI_Type(AtmVpIdentifier):defaultValue=0
_MplsLcAtmLcAtmVPI_Type.__name__=_F
_MplsLcAtmLcAtmVPI_Object=MibTableColumn
mplsLcAtmLcAtmVPI=_MplsLcAtmLcAtmVPI_Object((1,3,6,1,2,1,10,166,9,1,1,1,7),_MplsLcAtmLcAtmVPI_Type())
mplsLcAtmLcAtmVPI.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLcAtmLcAtmVPI.setStatus(_A)
_MplsLcAtmStdIfConfRowStatus_Type=RowStatus
_MplsLcAtmStdIfConfRowStatus_Object=MibTableColumn
mplsLcAtmStdIfConfRowStatus=_MplsLcAtmStdIfConfRowStatus_Object((1,3,6,1,2,1,10,166,9,1,1,1,8),_MplsLcAtmStdIfConfRowStatus_Type())
mplsLcAtmStdIfConfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLcAtmStdIfConfRowStatus.setStatus(_A)
class _MplsLcAtmStdIfConfStorageType_Type(StorageType):defaultValue=3
_MplsLcAtmStdIfConfStorageType_Type.__name__=_I
_MplsLcAtmStdIfConfStorageType_Object=MibTableColumn
mplsLcAtmStdIfConfStorageType=_MplsLcAtmStdIfConfStorageType_Object((1,3,6,1,2,1,10,166,9,1,1,1,9),_MplsLcAtmStdIfConfStorageType_Type())
mplsLcAtmStdIfConfStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLcAtmStdIfConfStorageType.setStatus(_A)
_MplsLcAtmStdConformance_ObjectIdentity=ObjectIdentity
mplsLcAtmStdConformance=_MplsLcAtmStdConformance_ObjectIdentity((1,3,6,1,2,1,10,166,9,2))
_MplsLcAtmStdCompliances_ObjectIdentity=ObjectIdentity
mplsLcAtmStdCompliances=_MplsLcAtmStdCompliances_ObjectIdentity((1,3,6,1,2,1,10,166,9,2,1))
_MplsLcAtmStdGroups_ObjectIdentity=ObjectIdentity
mplsLcAtmStdGroups=_MplsLcAtmStdGroups_ObjectIdentity((1,3,6,1,2,1,10,166,9,2,2))
mplsLcAtmStdIfGroup=ObjectGroup((1,3,6,1,2,1,10,166,9,2,2,1))
mplsLcAtmStdIfGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:mplsLcAtmStdIfGroup.setStatus(_A)
mplsLcAtmStdModuleFullCompliance=ModuleCompliance((1,3,6,1,2,1,10,166,9,2,1,1))
mplsLcAtmStdModuleFullCompliance.setObjects((_B,_E))
if mibBuilder.loadTexts:mplsLcAtmStdModuleFullCompliance.setStatus(_A)
mplsLcAtmStdModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,10,166,9,2,1,2))
mplsLcAtmStdModuleReadOnlyCompliance.setObjects((_B,_E))
if mibBuilder.loadTexts:mplsLcAtmStdModuleReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mplsLcAtmStdMIB':mplsLcAtmStdMIB,'mplsLcAtmStdNotifications':mplsLcAtmStdNotifications,'mplsLcAtmStdObjects':mplsLcAtmStdObjects,'mplsLcAtmStdInterfaceConfTable':mplsLcAtmStdInterfaceConfTable,'mplsLcAtmStdInterfaceConfEntry':mplsLcAtmStdInterfaceConfEntry,_J:mplsLcAtmStdCtrlVpi,_K:mplsLcAtmStdCtrlVci,_L:mplsLcAtmStdUnlabTrafVpi,_M:mplsLcAtmStdUnlabTrafVci,_N:mplsLcAtmStdVcMerge,_O:mplsLcAtmVcDirectlyConnected,_P:mplsLcAtmLcAtmVPI,_Q:mplsLcAtmStdIfConfRowStatus,_R:mplsLcAtmStdIfConfStorageType,'mplsLcAtmStdConformance':mplsLcAtmStdConformance,'mplsLcAtmStdCompliances':mplsLcAtmStdCompliances,'mplsLcAtmStdModuleFullCompliance':mplsLcAtmStdModuleFullCompliance,'mplsLcAtmStdModuleReadOnlyCompliance':mplsLcAtmStdModuleReadOnlyCompliance,'mplsLcAtmStdGroups':mplsLcAtmStdGroups,_E:mplsLcAtmStdIfGroup})