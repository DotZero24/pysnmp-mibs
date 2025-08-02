_M='mplsLcFrStdInterfaceConfStorageType'
_L='mplsLcFrStdInterfaceConfRowStatus'
_K='mplsLcFrStdCtrlMaxDlci'
_J='mplsLcFrStdCtrlMinDlci'
_I='mplsLcFrStdTrafficMaxDlci'
_H='mplsLcFrStdTrafficMinDlci'
_G='StorageType'
_F='mplsInterfaceIndex'
_E='MPLS-LSR-STD-MIB'
_D='mplsLcFrStdIfGroup'
_C='read-create'
_B='MPLS-LC-FR-STD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DLCI,=mibBuilder.importSymbols('FRAME-RELAY-DTE-MIB','DLCI')
mplsInterfaceIndex,=mibBuilder.importSymbols(_E,_F)
mplsStdMIB,=mibBuilder.importSymbols('MPLS-TC-STD-MIB','mplsStdMIB')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_G,'TextualConvention')
mplsLcFrStdMIB=ModuleIdentity((1,3,6,1,2,1,10,166,10))
if mibBuilder.loadTexts:mplsLcFrStdMIB.setRevisions(('2006-01-12 00:00',))
_MplsLcFrStdNotifications_ObjectIdentity=ObjectIdentity
mplsLcFrStdNotifications=_MplsLcFrStdNotifications_ObjectIdentity((1,3,6,1,2,1,10,166,10,0))
_MplsLcFrStdObjects_ObjectIdentity=ObjectIdentity
mplsLcFrStdObjects=_MplsLcFrStdObjects_ObjectIdentity((1,3,6,1,2,1,10,166,10,1))
_MplsLcFrStdInterfaceConfTable_Object=MibTable
mplsLcFrStdInterfaceConfTable=_MplsLcFrStdInterfaceConfTable_Object((1,3,6,1,2,1,10,166,10,1,1))
if mibBuilder.loadTexts:mplsLcFrStdInterfaceConfTable.setStatus(_A)
_MplsLcFrStdInterfaceConfEntry_Object=MibTableRow
mplsLcFrStdInterfaceConfEntry=_MplsLcFrStdInterfaceConfEntry_Object((1,3,6,1,2,1,10,166,10,1,1,1))
mplsLcFrStdInterfaceConfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:mplsLcFrStdInterfaceConfEntry.setStatus(_A)
_MplsLcFrStdTrafficMinDlci_Type=DLCI
_MplsLcFrStdTrafficMinDlci_Object=MibTableColumn
mplsLcFrStdTrafficMinDlci=_MplsLcFrStdTrafficMinDlci_Object((1,3,6,1,2,1,10,166,10,1,1,1,1),_MplsLcFrStdTrafficMinDlci_Type())
mplsLcFrStdTrafficMinDlci.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLcFrStdTrafficMinDlci.setStatus(_A)
_MplsLcFrStdTrafficMaxDlci_Type=DLCI
_MplsLcFrStdTrafficMaxDlci_Object=MibTableColumn
mplsLcFrStdTrafficMaxDlci=_MplsLcFrStdTrafficMaxDlci_Object((1,3,6,1,2,1,10,166,10,1,1,1,2),_MplsLcFrStdTrafficMaxDlci_Type())
mplsLcFrStdTrafficMaxDlci.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLcFrStdTrafficMaxDlci.setStatus(_A)
_MplsLcFrStdCtrlMinDlci_Type=DLCI
_MplsLcFrStdCtrlMinDlci_Object=MibTableColumn
mplsLcFrStdCtrlMinDlci=_MplsLcFrStdCtrlMinDlci_Object((1,3,6,1,2,1,10,166,10,1,1,1,3),_MplsLcFrStdCtrlMinDlci_Type())
mplsLcFrStdCtrlMinDlci.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLcFrStdCtrlMinDlci.setStatus(_A)
_MplsLcFrStdCtrlMaxDlci_Type=DLCI
_MplsLcFrStdCtrlMaxDlci_Object=MibTableColumn
mplsLcFrStdCtrlMaxDlci=_MplsLcFrStdCtrlMaxDlci_Object((1,3,6,1,2,1,10,166,10,1,1,1,4),_MplsLcFrStdCtrlMaxDlci_Type())
mplsLcFrStdCtrlMaxDlci.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLcFrStdCtrlMaxDlci.setStatus(_A)
_MplsLcFrStdInterfaceConfRowStatus_Type=RowStatus
_MplsLcFrStdInterfaceConfRowStatus_Object=MibTableColumn
mplsLcFrStdInterfaceConfRowStatus=_MplsLcFrStdInterfaceConfRowStatus_Object((1,3,6,1,2,1,10,166,10,1,1,1,5),_MplsLcFrStdInterfaceConfRowStatus_Type())
mplsLcFrStdInterfaceConfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLcFrStdInterfaceConfRowStatus.setStatus(_A)
class _MplsLcFrStdInterfaceConfStorageType_Type(StorageType):defaultValue=3
_MplsLcFrStdInterfaceConfStorageType_Type.__name__=_G
_MplsLcFrStdInterfaceConfStorageType_Object=MibTableColumn
mplsLcFrStdInterfaceConfStorageType=_MplsLcFrStdInterfaceConfStorageType_Object((1,3,6,1,2,1,10,166,10,1,1,1,6),_MplsLcFrStdInterfaceConfStorageType_Type())
mplsLcFrStdInterfaceConfStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:mplsLcFrStdInterfaceConfStorageType.setStatus(_A)
_MplsLcFrStdConformance_ObjectIdentity=ObjectIdentity
mplsLcFrStdConformance=_MplsLcFrStdConformance_ObjectIdentity((1,3,6,1,2,1,10,166,10,2))
_MplsLcFrStdCompliances_ObjectIdentity=ObjectIdentity
mplsLcFrStdCompliances=_MplsLcFrStdCompliances_ObjectIdentity((1,3,6,1,2,1,10,166,10,2,1))
_MplsLcFrStdGroups_ObjectIdentity=ObjectIdentity
mplsLcFrStdGroups=_MplsLcFrStdGroups_ObjectIdentity((1,3,6,1,2,1,10,166,10,2,2))
mplsLcFrStdIfGroup=ObjectGroup((1,3,6,1,2,1,10,166,10,2,2,1))
mplsLcFrStdIfGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M)))
if mibBuilder.loadTexts:mplsLcFrStdIfGroup.setStatus(_A)
mplsLcFrStdModuleFullCompliance=ModuleCompliance((1,3,6,1,2,1,10,166,10,2,1,1))
mplsLcFrStdModuleFullCompliance.setObjects((_B,_D))
if mibBuilder.loadTexts:mplsLcFrStdModuleFullCompliance.setStatus(_A)
mplsLcFrStdModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,10,166,10,2,1,2))
mplsLcFrStdModuleReadOnlyCompliance.setObjects((_B,_D))
if mibBuilder.loadTexts:mplsLcFrStdModuleReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mplsLcFrStdMIB':mplsLcFrStdMIB,'mplsLcFrStdNotifications':mplsLcFrStdNotifications,'mplsLcFrStdObjects':mplsLcFrStdObjects,'mplsLcFrStdInterfaceConfTable':mplsLcFrStdInterfaceConfTable,'mplsLcFrStdInterfaceConfEntry':mplsLcFrStdInterfaceConfEntry,_H:mplsLcFrStdTrafficMinDlci,_I:mplsLcFrStdTrafficMaxDlci,_J:mplsLcFrStdCtrlMinDlci,_K:mplsLcFrStdCtrlMaxDlci,_L:mplsLcFrStdInterfaceConfRowStatus,_M:mplsLcFrStdInterfaceConfStorageType,'mplsLcFrStdConformance':mplsLcFrStdConformance,'mplsLcFrStdCompliances':mplsLcFrStdCompliances,'mplsLcFrStdModuleFullCompliance':mplsLcFrStdModuleFullCompliance,'mplsLcFrStdModuleReadOnlyCompliance':mplsLcFrStdModuleReadOnlyCompliance,'mplsLcFrStdGroups':mplsLcFrStdGroups,_D:mplsLcFrStdIfGroup})