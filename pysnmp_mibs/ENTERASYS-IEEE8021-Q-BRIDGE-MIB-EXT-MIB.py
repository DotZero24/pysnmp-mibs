_R='etsysIeee8021QBridgeMibExtFdbGroup'
_Q='etsysIeee8021QBridgeMibExtPortVlanGroup'
_P='etsysIeee8021QBridgeMibExtMvrpGroup'
_O='etsysIeee8021QBridgeFdbOperMaxNumEntries'
_N='etsysIeee8021QBridgeFdbMaxNumEntries'
_M='etsysIeee8021QBridgeFdbMaxNumEntriesCapabilities'
_L='etsysIeee8021QBridgePortMvrpTxVidTranslationErrors'
_K='etsysIeee8021QBridgePortMvrpRxVidTranslationErrors'
_J='etsysIeee8021QVlanMvrpRestrictedStatus'
_I='etsysIeee8021QBridgeMibExtPortVlanEntry'
_H='read-write'
_G='not-accessible'
_F='etsysIeee8021QVlanMvrpRestrictedIndex'
_E='etsysIeee8021QVlanMvrpRestrictedComponentId'
_D='EnabledStatus'
_C='read-only'
_B='ENTERASYS-IEEE8021-Q-BRIDGE-MIB-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
ieee8021BridgeBasePortEntry,=mibBuilder.importSymbols('IEEE8021-BRIDGE-MIB','ieee8021BridgeBasePortEntry')
IEEE8021PbbComponentIdentifier,IEEE8021VlanIndex=mibBuilder.importSymbols('IEEE8021-TC-MIB','IEEE8021PbbComponentIdentifier','IEEE8021VlanIndex')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
etsysIeee8021QBridgeMibExtMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,88))
if mibBuilder.loadTexts:etsysIeee8021QBridgeMibExtMIB.setRevisions(('2013-02-15 18:53','2012-02-07 13:59'))
class EtsysIeee8021QBridgeFdbEntries(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4096,8192,16384,32768,65536,131072)));namedValues=NamedValues(*(('is4K',4096),('is8K',8192),('is16K',16384),('is32K',32768),('is64K',65536),('is128K',131072)))
_EtsysIeee8021QBridgeMibExtObjects_ObjectIdentity=ObjectIdentity
etsysIeee8021QBridgeMibExtObjects=_EtsysIeee8021QBridgeMibExtObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,88,1))
_EtsysIeee8021QBridgeMibExtMvrpBranch_ObjectIdentity=ObjectIdentity
etsysIeee8021QBridgeMibExtMvrpBranch=_EtsysIeee8021QBridgeMibExtMvrpBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,88,1,1))
_EtsysIeee8021QVlanMvrpRestrictedTable_Object=MibTable
etsysIeee8021QVlanMvrpRestrictedTable=_EtsysIeee8021QVlanMvrpRestrictedTable_Object((1,3,6,1,4,1,5624,1,2,88,1,1,1))
if mibBuilder.loadTexts:etsysIeee8021QVlanMvrpRestrictedTable.setStatus(_A)
_EtsysIeee8021QVlanMvrpRestrictedEntry_Object=MibTableRow
etsysIeee8021QVlanMvrpRestrictedEntry=_EtsysIeee8021QVlanMvrpRestrictedEntry_Object((1,3,6,1,4,1,5624,1,2,88,1,1,1,1))
etsysIeee8021QVlanMvrpRestrictedEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:etsysIeee8021QVlanMvrpRestrictedEntry.setStatus(_A)
_EtsysIeee8021QVlanMvrpRestrictedComponentId_Type=IEEE8021PbbComponentIdentifier
_EtsysIeee8021QVlanMvrpRestrictedComponentId_Object=MibTableColumn
etsysIeee8021QVlanMvrpRestrictedComponentId=_EtsysIeee8021QVlanMvrpRestrictedComponentId_Object((1,3,6,1,4,1,5624,1,2,88,1,1,1,1,1),_EtsysIeee8021QVlanMvrpRestrictedComponentId_Type())
etsysIeee8021QVlanMvrpRestrictedComponentId.setMaxAccess(_G)
if mibBuilder.loadTexts:etsysIeee8021QVlanMvrpRestrictedComponentId.setStatus(_A)
_EtsysIeee8021QVlanMvrpRestrictedIndex_Type=IEEE8021VlanIndex
_EtsysIeee8021QVlanMvrpRestrictedIndex_Object=MibTableColumn
etsysIeee8021QVlanMvrpRestrictedIndex=_EtsysIeee8021QVlanMvrpRestrictedIndex_Object((1,3,6,1,4,1,5624,1,2,88,1,1,1,1,2),_EtsysIeee8021QVlanMvrpRestrictedIndex_Type())
etsysIeee8021QVlanMvrpRestrictedIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:etsysIeee8021QVlanMvrpRestrictedIndex.setStatus(_A)
class _EtsysIeee8021QVlanMvrpRestrictedStatus_Type(EnabledStatus):defaultValue=2
_EtsysIeee8021QVlanMvrpRestrictedStatus_Type.__name__=_D
_EtsysIeee8021QVlanMvrpRestrictedStatus_Object=MibTableColumn
etsysIeee8021QVlanMvrpRestrictedStatus=_EtsysIeee8021QVlanMvrpRestrictedStatus_Object((1,3,6,1,4,1,5624,1,2,88,1,1,1,1,3),_EtsysIeee8021QVlanMvrpRestrictedStatus_Type())
etsysIeee8021QVlanMvrpRestrictedStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysIeee8021QVlanMvrpRestrictedStatus.setStatus(_A)
_EtsysIeee8021QBridgeMibExtPortVlanBranch_ObjectIdentity=ObjectIdentity
etsysIeee8021QBridgeMibExtPortVlanBranch=_EtsysIeee8021QBridgeMibExtPortVlanBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,88,1,2))
_EtsysIeee8021QBridgeMibExtPortVlanTable_Object=MibTable
etsysIeee8021QBridgeMibExtPortVlanTable=_EtsysIeee8021QBridgeMibExtPortVlanTable_Object((1,3,6,1,4,1,5624,1,2,88,1,2,1))
if mibBuilder.loadTexts:etsysIeee8021QBridgeMibExtPortVlanTable.setStatus(_A)
_EtsysIeee8021QBridgeMibExtPortVlanEntry_Object=MibTableRow
etsysIeee8021QBridgeMibExtPortVlanEntry=_EtsysIeee8021QBridgeMibExtPortVlanEntry_Object((1,3,6,1,4,1,5624,1,2,88,1,2,1,1))
if mibBuilder.loadTexts:etsysIeee8021QBridgeMibExtPortVlanEntry.setStatus(_A)
_EtsysIeee8021QBridgePortMvrpRxVidTranslationErrors_Type=Counter64
_EtsysIeee8021QBridgePortMvrpRxVidTranslationErrors_Object=MibTableColumn
etsysIeee8021QBridgePortMvrpRxVidTranslationErrors=_EtsysIeee8021QBridgePortMvrpRxVidTranslationErrors_Object((1,3,6,1,4,1,5624,1,2,88,1,2,1,1,1),_EtsysIeee8021QBridgePortMvrpRxVidTranslationErrors_Type())
etsysIeee8021QBridgePortMvrpRxVidTranslationErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIeee8021QBridgePortMvrpRxVidTranslationErrors.setStatus(_A)
if mibBuilder.loadTexts:etsysIeee8021QBridgePortMvrpRxVidTranslationErrors.setUnits('MVRP receive VID translation errors')
_EtsysIeee8021QBridgePortMvrpTxVidTranslationErrors_Type=Counter64
_EtsysIeee8021QBridgePortMvrpTxVidTranslationErrors_Object=MibTableColumn
etsysIeee8021QBridgePortMvrpTxVidTranslationErrors=_EtsysIeee8021QBridgePortMvrpTxVidTranslationErrors_Object((1,3,6,1,4,1,5624,1,2,88,1,2,1,1,2),_EtsysIeee8021QBridgePortMvrpTxVidTranslationErrors_Type())
etsysIeee8021QBridgePortMvrpTxVidTranslationErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIeee8021QBridgePortMvrpTxVidTranslationErrors.setStatus(_A)
if mibBuilder.loadTexts:etsysIeee8021QBridgePortMvrpTxVidTranslationErrors.setUnits('MVRP transmit VID translation errors')
_EtsysIeee8021QBridgeMibExtFdbBranch_ObjectIdentity=ObjectIdentity
etsysIeee8021QBridgeMibExtFdbBranch=_EtsysIeee8021QBridgeMibExtFdbBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,88,1,3))
_EtsysIeee8021QBridgeFdb_ObjectIdentity=ObjectIdentity
etsysIeee8021QBridgeFdb=_EtsysIeee8021QBridgeFdb_ObjectIdentity((1,3,6,1,4,1,5624,1,2,88,1,3,1))
class _EtsysIeee8021QBridgeFdbMaxNumEntriesCapabilities_Type(Bits):namedValues=NamedValues(*(('fdbMaxNumEntries4K',0),('fdbMaxNumEntries8K',1),('fdbMaxNumEntries16K',2),('fdbMaxNumEntries32K',3),('fdbMaxNumEntries64K',4),('fdbMaxNumEntries128K',5)))
_EtsysIeee8021QBridgeFdbMaxNumEntriesCapabilities_Type.__name__='Bits'
_EtsysIeee8021QBridgeFdbMaxNumEntriesCapabilities_Object=MibScalar
etsysIeee8021QBridgeFdbMaxNumEntriesCapabilities=_EtsysIeee8021QBridgeFdbMaxNumEntriesCapabilities_Object((1,3,6,1,4,1,5624,1,2,88,1,3,1,1),_EtsysIeee8021QBridgeFdbMaxNumEntriesCapabilities_Type())
etsysIeee8021QBridgeFdbMaxNumEntriesCapabilities.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIeee8021QBridgeFdbMaxNumEntriesCapabilities.setStatus(_A)
_EtsysIeee8021QBridgeFdbMaxNumEntries_Type=EtsysIeee8021QBridgeFdbEntries
_EtsysIeee8021QBridgeFdbMaxNumEntries_Object=MibScalar
etsysIeee8021QBridgeFdbMaxNumEntries=_EtsysIeee8021QBridgeFdbMaxNumEntries_Object((1,3,6,1,4,1,5624,1,2,88,1,3,1,2),_EtsysIeee8021QBridgeFdbMaxNumEntries_Type())
etsysIeee8021QBridgeFdbMaxNumEntries.setMaxAccess(_H)
if mibBuilder.loadTexts:etsysIeee8021QBridgeFdbMaxNumEntries.setStatus(_A)
_EtsysIeee8021QBridgeFdbOperMaxNumEntries_Type=EtsysIeee8021QBridgeFdbEntries
_EtsysIeee8021QBridgeFdbOperMaxNumEntries_Object=MibScalar
etsysIeee8021QBridgeFdbOperMaxNumEntries=_EtsysIeee8021QBridgeFdbOperMaxNumEntries_Object((1,3,6,1,4,1,5624,1,2,88,1,3,1,3),_EtsysIeee8021QBridgeFdbOperMaxNumEntries_Type())
etsysIeee8021QBridgeFdbOperMaxNumEntries.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysIeee8021QBridgeFdbOperMaxNumEntries.setStatus(_A)
_EtsysIeee8021QBridgeMibExtConformance_ObjectIdentity=ObjectIdentity
etsysIeee8021QBridgeMibExtConformance=_EtsysIeee8021QBridgeMibExtConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,88,2))
_EtsysIeee8021QBridgeMibExtGroups_ObjectIdentity=ObjectIdentity
etsysIeee8021QBridgeMibExtGroups=_EtsysIeee8021QBridgeMibExtGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,88,2,1))
_EtsysIeee8021QBridgeMibExtCompliances_ObjectIdentity=ObjectIdentity
etsysIeee8021QBridgeMibExtCompliances=_EtsysIeee8021QBridgeMibExtCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,88,2,2))
ieee8021BridgeBasePortEntry.registerAugmentions((_B,_I))
etsysIeee8021QBridgeMibExtPortVlanEntry.setIndexNames(*ieee8021BridgeBasePortEntry.getIndexNames())
etsysIeee8021QBridgeMibExtMvrpGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,88,2,1,1))
etsysIeee8021QBridgeMibExtMvrpGroup.setObjects((_B,_J))
if mibBuilder.loadTexts:etsysIeee8021QBridgeMibExtMvrpGroup.setStatus(_A)
etsysIeee8021QBridgeMibExtPortVlanGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,88,2,1,2))
etsysIeee8021QBridgeMibExtPortVlanGroup.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:etsysIeee8021QBridgeMibExtPortVlanGroup.setStatus(_A)
etsysIeee8021QBridgeMibExtFdbGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,88,2,1,3))
etsysIeee8021QBridgeMibExtFdbGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:etsysIeee8021QBridgeMibExtFdbGroup.setStatus(_A)
etsysIeee8021QBridgeMibExtMvrp=ModuleCompliance((1,3,6,1,4,1,5624,1,2,88,2,2,1))
etsysIeee8021QBridgeMibExtMvrp.setObjects((_B,_P))
if mibBuilder.loadTexts:etsysIeee8021QBridgeMibExtMvrp.setStatus(_A)
etsysIeee8021QBridgeMibExtPortVlan=ModuleCompliance((1,3,6,1,4,1,5624,1,2,88,2,2,2))
etsysIeee8021QBridgeMibExtPortVlan.setObjects((_B,_Q))
if mibBuilder.loadTexts:etsysIeee8021QBridgeMibExtPortVlan.setStatus(_A)
etsysIeee8021QBridgeMibExtFdb=ModuleCompliance((1,3,6,1,4,1,5624,1,2,88,2,2,3))
etsysIeee8021QBridgeMibExtFdb.setObjects((_B,_R))
if mibBuilder.loadTexts:etsysIeee8021QBridgeMibExtFdb.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'EtsysIeee8021QBridgeFdbEntries':EtsysIeee8021QBridgeFdbEntries,'etsysIeee8021QBridgeMibExtMIB':etsysIeee8021QBridgeMibExtMIB,'etsysIeee8021QBridgeMibExtObjects':etsysIeee8021QBridgeMibExtObjects,'etsysIeee8021QBridgeMibExtMvrpBranch':etsysIeee8021QBridgeMibExtMvrpBranch,'etsysIeee8021QVlanMvrpRestrictedTable':etsysIeee8021QVlanMvrpRestrictedTable,'etsysIeee8021QVlanMvrpRestrictedEntry':etsysIeee8021QVlanMvrpRestrictedEntry,_E:etsysIeee8021QVlanMvrpRestrictedComponentId,_F:etsysIeee8021QVlanMvrpRestrictedIndex,_J:etsysIeee8021QVlanMvrpRestrictedStatus,'etsysIeee8021QBridgeMibExtPortVlanBranch':etsysIeee8021QBridgeMibExtPortVlanBranch,'etsysIeee8021QBridgeMibExtPortVlanTable':etsysIeee8021QBridgeMibExtPortVlanTable,_I:etsysIeee8021QBridgeMibExtPortVlanEntry,_K:etsysIeee8021QBridgePortMvrpRxVidTranslationErrors,_L:etsysIeee8021QBridgePortMvrpTxVidTranslationErrors,'etsysIeee8021QBridgeMibExtFdbBranch':etsysIeee8021QBridgeMibExtFdbBranch,'etsysIeee8021QBridgeFdb':etsysIeee8021QBridgeFdb,_M:etsysIeee8021QBridgeFdbMaxNumEntriesCapabilities,_N:etsysIeee8021QBridgeFdbMaxNumEntries,_O:etsysIeee8021QBridgeFdbOperMaxNumEntries,'etsysIeee8021QBridgeMibExtConformance':etsysIeee8021QBridgeMibExtConformance,'etsysIeee8021QBridgeMibExtGroups':etsysIeee8021QBridgeMibExtGroups,_P:etsysIeee8021QBridgeMibExtMvrpGroup,_Q:etsysIeee8021QBridgeMibExtPortVlanGroup,_R:etsysIeee8021QBridgeMibExtFdbGroup,'etsysIeee8021QBridgeMibExtCompliances':etsysIeee8021QBridgeMibExtCompliances,'etsysIeee8021QBridgeMibExtMvrp':etsysIeee8021QBridgeMibExtMvrp,'etsysIeee8021QBridgeMibExtPortVlan':etsysIeee8021QBridgeMibExtPortVlan,'etsysIeee8021QBridgeMibExtFdb':etsysIeee8021QBridgeMibExtFdb})