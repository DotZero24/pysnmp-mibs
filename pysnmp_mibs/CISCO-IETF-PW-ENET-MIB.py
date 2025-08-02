_W='cpwVcEnetMplsPriGroup'
_V='cpwVcStatsGroup'
_U='cpwVcEnetGroup'
_T='cpwVcEnetMplsPriMappingStorageType'
_S='cpwVcEnetMplsPriMappingRowStatus'
_R='cpwVcEnetMplsPriMapping'
_Q='cpwVcEnetStatsIllegalLength'
_P='cpwVcEnetStatsIllegalVlan'
_O='cpwVcEnetStorageType'
_N='cpwVcEnetRowStatus'
_M='cpwVcEnetVcIfIndex'
_L='cpwVcEnetPortIfIndex'
_K='cpwVcEnetPortVlan'
_J='cpwVcEnetVlanMode'
_I='read-only'
_H='cpwVcEnetPwVlan'
_G='Integer32'
_F='CpwVcVlanCfg'
_E='cpwVcIndex'
_D='CISCO-IETF-PW-MIB'
_C='read-create'
_B='CISCO-IETF-PW-ENET-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cpwVcIndex,=mibBuilder.importSymbols(_D,_E)
CpwVcVlanCfg,=mibBuilder.importSymbols('CISCO-IETF-PW-TC-MIB',_F)
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','experimental','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','StorageType','TextualConvention')
cpwVcEnetMIB=ModuleIdentity((1,3,6,1,4,1,9,10,108))
if mibBuilder.loadTexts:cpwVcEnetMIB.setRevisions(('2002-09-22 12:00','2002-08-20 12:00','2002-02-03 12:00'))
_CpwVcEnetNotifications_ObjectIdentity=ObjectIdentity
cpwVcEnetNotifications=_CpwVcEnetNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,108,0))
_CpwVcEnetObjects_ObjectIdentity=ObjectIdentity
cpwVcEnetObjects=_CpwVcEnetObjects_ObjectIdentity((1,3,6,1,4,1,9,10,108,1))
_CpwVcEnetTable_Object=MibTable
cpwVcEnetTable=_CpwVcEnetTable_Object((1,3,6,1,4,1,9,10,108,1,1))
if mibBuilder.loadTexts:cpwVcEnetTable.setStatus(_A)
_CpwVcEnetEntry_Object=MibTableRow
cpwVcEnetEntry=_CpwVcEnetEntry_Object((1,3,6,1,4,1,9,10,108,1,1,1))
cpwVcEnetEntry.setIndexNames((0,_D,_E),(0,_B,_H))
if mibBuilder.loadTexts:cpwVcEnetEntry.setStatus(_A)
_CpwVcEnetPwVlan_Type=CpwVcVlanCfg
_CpwVcEnetPwVlan_Object=MibTableColumn
cpwVcEnetPwVlan=_CpwVcEnetPwVlan_Object((1,3,6,1,4,1,9,10,108,1,1,1,1),_CpwVcEnetPwVlan_Type())
cpwVcEnetPwVlan.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:cpwVcEnetPwVlan.setStatus(_A)
class _CpwVcEnetVlanMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('other',0),('portBased',1),('noChange',2),('changeVlan',3),('addVlan',4),('removeVlan',5)))
_CpwVcEnetVlanMode_Type.__name__=_G
_CpwVcEnetVlanMode_Object=MibTableColumn
cpwVcEnetVlanMode=_CpwVcEnetVlanMode_Object((1,3,6,1,4,1,9,10,108,1,1,1,2),_CpwVcEnetVlanMode_Type())
cpwVcEnetVlanMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcEnetVlanMode.setStatus(_A)
class _CpwVcEnetPortVlan_Type(CpwVcVlanCfg):defaultValue=4097
_CpwVcEnetPortVlan_Type.__name__=_F
_CpwVcEnetPortVlan_Object=MibTableColumn
cpwVcEnetPortVlan=_CpwVcEnetPortVlan_Object((1,3,6,1,4,1,9,10,108,1,1,1,3),_CpwVcEnetPortVlan_Type())
cpwVcEnetPortVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcEnetPortVlan.setStatus(_A)
_CpwVcEnetVcIfIndex_Type=InterfaceIndexOrZero
_CpwVcEnetVcIfIndex_Object=MibTableColumn
cpwVcEnetVcIfIndex=_CpwVcEnetVcIfIndex_Object((1,3,6,1,4,1,9,10,108,1,1,1,4),_CpwVcEnetVcIfIndex_Type())
cpwVcEnetVcIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcEnetVcIfIndex.setStatus(_A)
_CpwVcEnetPortIfIndex_Type=InterfaceIndexOrZero
_CpwVcEnetPortIfIndex_Object=MibTableColumn
cpwVcEnetPortIfIndex=_CpwVcEnetPortIfIndex_Object((1,3,6,1,4,1,9,10,108,1,1,1,5),_CpwVcEnetPortIfIndex_Type())
cpwVcEnetPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcEnetPortIfIndex.setStatus(_A)
_CpwVcEnetRowStatus_Type=RowStatus
_CpwVcEnetRowStatus_Object=MibTableColumn
cpwVcEnetRowStatus=_CpwVcEnetRowStatus_Object((1,3,6,1,4,1,9,10,108,1,1,1,6),_CpwVcEnetRowStatus_Type())
cpwVcEnetRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcEnetRowStatus.setStatus(_A)
_CpwVcEnetStorageType_Type=StorageType
_CpwVcEnetStorageType_Object=MibTableColumn
cpwVcEnetStorageType=_CpwVcEnetStorageType_Object((1,3,6,1,4,1,9,10,108,1,1,1,7),_CpwVcEnetStorageType_Type())
cpwVcEnetStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcEnetStorageType.setStatus(_A)
_CpwVcEnetMplsPriMappingTable_Object=MibTable
cpwVcEnetMplsPriMappingTable=_CpwVcEnetMplsPriMappingTable_Object((1,3,6,1,4,1,9,10,108,1,2))
if mibBuilder.loadTexts:cpwVcEnetMplsPriMappingTable.setStatus(_A)
_CpwVcEnetMplsPriMappingTableEntry_Object=MibTableRow
cpwVcEnetMplsPriMappingTableEntry=_CpwVcEnetMplsPriMappingTableEntry_Object((1,3,6,1,4,1,9,10,108,1,2,1))
cpwVcEnetMplsPriMappingTableEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cpwVcEnetMplsPriMappingTableEntry.setStatus(_A)
class _CpwVcEnetMplsPriMapping_Type(Bits):namedValues=NamedValues(*(('pri000',0),('pri001',1),('pri010',2),('pri011',3),('pri100',4),('pri101',5),('pri110',6),('pri111',7),('untagged',8)))
_CpwVcEnetMplsPriMapping_Type.__name__='Bits'
_CpwVcEnetMplsPriMapping_Object=MibTableColumn
cpwVcEnetMplsPriMapping=_CpwVcEnetMplsPriMapping_Object((1,3,6,1,4,1,9,10,108,1,2,1,1),_CpwVcEnetMplsPriMapping_Type())
cpwVcEnetMplsPriMapping.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcEnetMplsPriMapping.setStatus(_A)
_CpwVcEnetMplsPriMappingRowStatus_Type=RowStatus
_CpwVcEnetMplsPriMappingRowStatus_Object=MibTableColumn
cpwVcEnetMplsPriMappingRowStatus=_CpwVcEnetMplsPriMappingRowStatus_Object((1,3,6,1,4,1,9,10,108,1,2,1,2),_CpwVcEnetMplsPriMappingRowStatus_Type())
cpwVcEnetMplsPriMappingRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcEnetMplsPriMappingRowStatus.setStatus(_A)
_CpwVcEnetMplsPriMappingStorageType_Type=StorageType
_CpwVcEnetMplsPriMappingStorageType_Object=MibTableColumn
cpwVcEnetMplsPriMappingStorageType=_CpwVcEnetMplsPriMappingStorageType_Object((1,3,6,1,4,1,9,10,108,1,2,1,3),_CpwVcEnetMplsPriMappingStorageType_Type())
cpwVcEnetMplsPriMappingStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cpwVcEnetMplsPriMappingStorageType.setStatus(_A)
_CpwVcEnetStatsTable_Object=MibTable
cpwVcEnetStatsTable=_CpwVcEnetStatsTable_Object((1,3,6,1,4,1,9,10,108,1,3))
if mibBuilder.loadTexts:cpwVcEnetStatsTable.setStatus(_A)
_CpwVcEnetStatsEntry_Object=MibTableRow
cpwVcEnetStatsEntry=_CpwVcEnetStatsEntry_Object((1,3,6,1,4,1,9,10,108,1,3,1))
cpwVcEnetStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cpwVcEnetStatsEntry.setStatus(_A)
_CpwVcEnetStatsIllegalVlan_Type=Counter64
_CpwVcEnetStatsIllegalVlan_Object=MibTableColumn
cpwVcEnetStatsIllegalVlan=_CpwVcEnetStatsIllegalVlan_Object((1,3,6,1,4,1,9,10,108,1,3,1,1),_CpwVcEnetStatsIllegalVlan_Type())
cpwVcEnetStatsIllegalVlan.setMaxAccess(_I)
if mibBuilder.loadTexts:cpwVcEnetStatsIllegalVlan.setStatus(_A)
_CpwVcEnetStatsIllegalLength_Type=Counter64
_CpwVcEnetStatsIllegalLength_Object=MibTableColumn
cpwVcEnetStatsIllegalLength=_CpwVcEnetStatsIllegalLength_Object((1,3,6,1,4,1,9,10,108,1,3,1,2),_CpwVcEnetStatsIllegalLength_Type())
cpwVcEnetStatsIllegalLength.setMaxAccess(_I)
if mibBuilder.loadTexts:cpwVcEnetStatsIllegalLength.setStatus(_A)
_CpwVcEnetConformance_ObjectIdentity=ObjectIdentity
cpwVcEnetConformance=_CpwVcEnetConformance_ObjectIdentity((1,3,6,1,4,1,9,10,108,2))
_CpwVcEnetGroups_ObjectIdentity=ObjectIdentity
cpwVcEnetGroups=_CpwVcEnetGroups_ObjectIdentity((1,3,6,1,4,1,9,10,108,2,1))
_CpwVcEnetCompliances_ObjectIdentity=ObjectIdentity
cpwVcEnetCompliances=_CpwVcEnetCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,108,2,2))
cpwVcEnetGroup=ObjectGroup((1,3,6,1,4,1,9,10,108,2,1,1))
cpwVcEnetGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:cpwVcEnetGroup.setStatus(_A)
cpwVcStatsGroup=ObjectGroup((1,3,6,1,4,1,9,10,108,2,1,2))
cpwVcStatsGroup.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:cpwVcStatsGroup.setStatus(_A)
cpwVcEnetMplsPriGroup=ObjectGroup((1,3,6,1,4,1,9,10,108,2,1,3))
cpwVcEnetMplsPriGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:cpwVcEnetMplsPriGroup.setStatus(_A)
cpwVcEnetModuleCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,108,2,2,1))
cpwVcEnetModuleCompliance.setObjects(*((_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:cpwVcEnetModuleCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'cpwVcEnetMIB':cpwVcEnetMIB,'cpwVcEnetNotifications':cpwVcEnetNotifications,'cpwVcEnetObjects':cpwVcEnetObjects,'cpwVcEnetTable':cpwVcEnetTable,'cpwVcEnetEntry':cpwVcEnetEntry,_H:cpwVcEnetPwVlan,_J:cpwVcEnetVlanMode,_K:cpwVcEnetPortVlan,_M:cpwVcEnetVcIfIndex,_L:cpwVcEnetPortIfIndex,_N:cpwVcEnetRowStatus,_O:cpwVcEnetStorageType,'cpwVcEnetMplsPriMappingTable':cpwVcEnetMplsPriMappingTable,'cpwVcEnetMplsPriMappingTableEntry':cpwVcEnetMplsPriMappingTableEntry,_R:cpwVcEnetMplsPriMapping,_S:cpwVcEnetMplsPriMappingRowStatus,_T:cpwVcEnetMplsPriMappingStorageType,'cpwVcEnetStatsTable':cpwVcEnetStatsTable,'cpwVcEnetStatsEntry':cpwVcEnetStatsEntry,_P:cpwVcEnetStatsIllegalVlan,_Q:cpwVcEnetStatsIllegalLength,'cpwVcEnetConformance':cpwVcEnetConformance,'cpwVcEnetGroups':cpwVcEnetGroups,_U:cpwVcEnetGroup,_V:cpwVcStatsGroup,_W:cpwVcEnetMplsPriGroup,'cpwVcEnetCompliances':cpwVcEnetCompliances,'cpwVcEnetModuleCompliance':cpwVcEnetModuleCompliance})