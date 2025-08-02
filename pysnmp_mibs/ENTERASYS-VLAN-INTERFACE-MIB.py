_O='etsysVlanInterfaceGroup'
_N='etsysVlanInterfaceVlanIndex'
_M='etsysVlanInterfaceRowStatus'
_L='etsysVlanInterfaceStorageType'
_K='etsysVlanInterfaceIfIndex'
_J='etsysVlanInterfaceCurrentEntries'
_I='etsysVlanInterfaceMaximumEntries'
_H='read-create'
_G='etsysVlanInterfaceVlanID'
_F='StorageType'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='ENTERASYS-VLAN-INTERFACE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_D,'InterfaceIndexOrZero',_E)
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_F,'TextualConvention')
etsysVlanInterfaceMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,22))
if mibBuilder.loadTexts:etsysVlanInterfaceMIB.setRevisions(('2002-06-07 20:34','2002-06-07 15:37','2002-05-07 17:55'))
_EtsysVlanInterface_ObjectIdentity=ObjectIdentity
etsysVlanInterface=_EtsysVlanInterface_ObjectIdentity((1,3,6,1,4,1,5624,1,2,22,1))
_EtsysVlanInterfaceMaximumEntries_Type=Unsigned32
_EtsysVlanInterfaceMaximumEntries_Object=MibScalar
etsysVlanInterfaceMaximumEntries=_EtsysVlanInterfaceMaximumEntries_Object((1,3,6,1,4,1,5624,1,2,22,1,1),_EtsysVlanInterfaceMaximumEntries_Type())
etsysVlanInterfaceMaximumEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysVlanInterfaceMaximumEntries.setStatus(_A)
_EtsysVlanInterfaceCurrentEntries_Type=Unsigned32
_EtsysVlanInterfaceCurrentEntries_Object=MibScalar
etsysVlanInterfaceCurrentEntries=_EtsysVlanInterfaceCurrentEntries_Object((1,3,6,1,4,1,5624,1,2,22,1,2),_EtsysVlanInterfaceCurrentEntries_Type())
etsysVlanInterfaceCurrentEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysVlanInterfaceCurrentEntries.setStatus(_A)
_EtsysVlanInterfaceTable_Object=MibTable
etsysVlanInterfaceTable=_EtsysVlanInterfaceTable_Object((1,3,6,1,4,1,5624,1,2,22,1,3))
if mibBuilder.loadTexts:etsysVlanInterfaceTable.setStatus(_A)
_EtsysVlanInterfaceEntry_Object=MibTableRow
etsysVlanInterfaceEntry=_EtsysVlanInterfaceEntry_Object((1,3,6,1,4,1,5624,1,2,22,1,3,1))
etsysVlanInterfaceEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:etsysVlanInterfaceEntry.setStatus(_A)
_EtsysVlanInterfaceVlanID_Type=VlanIndex
_EtsysVlanInterfaceVlanID_Object=MibTableColumn
etsysVlanInterfaceVlanID=_EtsysVlanInterfaceVlanID_Object((1,3,6,1,4,1,5624,1,2,22,1,3,1,1),_EtsysVlanInterfaceVlanID_Type())
etsysVlanInterfaceVlanID.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:etsysVlanInterfaceVlanID.setStatus(_A)
_EtsysVlanInterfaceIfIndex_Type=InterfaceIndexOrZero
_EtsysVlanInterfaceIfIndex_Object=MibTableColumn
etsysVlanInterfaceIfIndex=_EtsysVlanInterfaceIfIndex_Object((1,3,6,1,4,1,5624,1,2,22,1,3,1,2),_EtsysVlanInterfaceIfIndex_Type())
etsysVlanInterfaceIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysVlanInterfaceIfIndex.setStatus(_A)
class _EtsysVlanInterfaceStorageType_Type(StorageType):defaultValue=3
_EtsysVlanInterfaceStorageType_Type.__name__=_F
_EtsysVlanInterfaceStorageType_Object=MibTableColumn
etsysVlanInterfaceStorageType=_EtsysVlanInterfaceStorageType_Object((1,3,6,1,4,1,5624,1,2,22,1,3,1,3),_EtsysVlanInterfaceStorageType_Type())
etsysVlanInterfaceStorageType.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysVlanInterfaceStorageType.setStatus(_A)
_EtsysVlanInterfaceRowStatus_Type=RowStatus
_EtsysVlanInterfaceRowStatus_Object=MibTableColumn
etsysVlanInterfaceRowStatus=_EtsysVlanInterfaceRowStatus_Object((1,3,6,1,4,1,5624,1,2,22,1,3,1,4),_EtsysVlanInterfaceRowStatus_Type())
etsysVlanInterfaceRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysVlanInterfaceRowStatus.setStatus(_A)
_EtsysVlanInterfaceVlanLookup_ObjectIdentity=ObjectIdentity
etsysVlanInterfaceVlanLookup=_EtsysVlanInterfaceVlanLookup_ObjectIdentity((1,3,6,1,4,1,5624,1,2,22,2))
_EtsysVlanInterfaceVlanLookupTable_Object=MibTable
etsysVlanInterfaceVlanLookupTable=_EtsysVlanInterfaceVlanLookupTable_Object((1,3,6,1,4,1,5624,1,2,22,2,1))
if mibBuilder.loadTexts:etsysVlanInterfaceVlanLookupTable.setStatus(_A)
_EtsysVlanInterfaceVlanLookupEntry_Object=MibTableRow
etsysVlanInterfaceVlanLookupEntry=_EtsysVlanInterfaceVlanLookupEntry_Object((1,3,6,1,4,1,5624,1,2,22,2,1,1))
etsysVlanInterfaceVlanLookupEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:etsysVlanInterfaceVlanLookupEntry.setStatus(_A)
_EtsysVlanInterfaceVlanIndex_Type=VlanIndex
_EtsysVlanInterfaceVlanIndex_Object=MibTableColumn
etsysVlanInterfaceVlanIndex=_EtsysVlanInterfaceVlanIndex_Object((1,3,6,1,4,1,5624,1,2,22,2,1,1,1),_EtsysVlanInterfaceVlanIndex_Type())
etsysVlanInterfaceVlanIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysVlanInterfaceVlanIndex.setStatus(_A)
_EtsysVlanInterfaceConformance_ObjectIdentity=ObjectIdentity
etsysVlanInterfaceConformance=_EtsysVlanInterfaceConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,22,3))
_EtsysVlanInterfaceGroups_ObjectIdentity=ObjectIdentity
etsysVlanInterfaceGroups=_EtsysVlanInterfaceGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,22,3,1))
_EtsysVlanInterfaceCompliances_ObjectIdentity=ObjectIdentity
etsysVlanInterfaceCompliances=_EtsysVlanInterfaceCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,22,3,2))
etsysVlanInterfaceGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,22,3,1,1))
etsysVlanInterfaceGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:etsysVlanInterfaceGroup.setStatus(_A)
etsysVlanInterfaceCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,22,3,2,1))
etsysVlanInterfaceCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:etsysVlanInterfaceCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsysVlanInterfaceMIB':etsysVlanInterfaceMIB,'etsysVlanInterface':etsysVlanInterface,_I:etsysVlanInterfaceMaximumEntries,_J:etsysVlanInterfaceCurrentEntries,'etsysVlanInterfaceTable':etsysVlanInterfaceTable,'etsysVlanInterfaceEntry':etsysVlanInterfaceEntry,_G:etsysVlanInterfaceVlanID,_K:etsysVlanInterfaceIfIndex,_L:etsysVlanInterfaceStorageType,_M:etsysVlanInterfaceRowStatus,'etsysVlanInterfaceVlanLookup':etsysVlanInterfaceVlanLookup,'etsysVlanInterfaceVlanLookupTable':etsysVlanInterfaceVlanLookupTable,'etsysVlanInterfaceVlanLookupEntry':etsysVlanInterfaceVlanLookupEntry,_N:etsysVlanInterfaceVlanIndex,'etsysVlanInterfaceConformance':etsysVlanInterfaceConformance,'etsysVlanInterfaceGroups':etsysVlanInterfaceGroups,_O:etsysVlanInterfaceGroup,'etsysVlanInterfaceCompliances':etsysVlanInterfaceCompliances,'etsysVlanInterfaceCompliance':etsysVlanInterfaceCompliance})