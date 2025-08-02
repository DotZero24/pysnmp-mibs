_V='pwEnetStatsIllegalLength'
_U='pwEnetStatsIllegalVlan'
_T='pwEnetStorageType'
_S='pwEnetRowStatus'
_R='pwEnetPwIfIndex'
_Q='pwEnetPortIfIndex'
_P='pwEnetPortVlan'
_O='pwEnetVlanMode'
_N='pwEnetPwVlan'
_M='read-only'
_L='pwEnetPwInstance'
_K='StorageType'
_J='Integer32'
_I='VlanIdOrAnyOrNone'
_H='InterfaceIndexOrZero'
_G='pwEnetStatsGroup'
_F='pwEnetGroup'
_E='pwIndex'
_D='PW-STD-MIB'
_C='read-create'
_B='PW-ENET-STD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_H)
pwIndex,=mibBuilder.importSymbols(_D,_E)
VlanIdOrAnyOrNone,=mibBuilder.importSymbols('Q-BRIDGE-MIB',_I)
ZeroBasedCounter32,=mibBuilder.importSymbols('RMON2-MIB','ZeroBasedCounter32')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_J,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_K,'TextualConvention')
pwEnetStdMIB=ModuleIdentity((1,3,6,1,2,1,180))
if mibBuilder.loadTexts:pwEnetStdMIB.setRevisions(('2009-06-15 00:00',))
_PwEnetObjects_ObjectIdentity=ObjectIdentity
pwEnetObjects=_PwEnetObjects_ObjectIdentity((1,3,6,1,2,1,180,1))
_PwEnetTable_Object=MibTable
pwEnetTable=_PwEnetTable_Object((1,3,6,1,2,1,180,1,1))
if mibBuilder.loadTexts:pwEnetTable.setStatus(_A)
_PwEnetEntry_Object=MibTableRow
pwEnetEntry=_PwEnetEntry_Object((1,3,6,1,2,1,180,1,1,1))
pwEnetEntry.setIndexNames((0,_D,_E),(0,_B,_L))
if mibBuilder.loadTexts:pwEnetEntry.setStatus(_A)
_PwEnetPwInstance_Type=Unsigned32
_PwEnetPwInstance_Object=MibTableColumn
pwEnetPwInstance=_PwEnetPwInstance_Object((1,3,6,1,2,1,180,1,1,1,1),_PwEnetPwInstance_Type())
pwEnetPwInstance.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:pwEnetPwInstance.setStatus(_A)
_PwEnetPwVlan_Type=VlanIdOrAnyOrNone
_PwEnetPwVlan_Object=MibTableColumn
pwEnetPwVlan=_PwEnetPwVlan_Object((1,3,6,1,2,1,180,1,1,1,2),_PwEnetPwVlan_Type())
pwEnetPwVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:pwEnetPwVlan.setStatus(_A)
class _PwEnetVlanMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('other',0),('portBased',1),('noChange',2),('changeVlan',3),('addVlan',4),('removeVlan',5)))
_PwEnetVlanMode_Type.__name__=_J
_PwEnetVlanMode_Object=MibTableColumn
pwEnetVlanMode=_PwEnetVlanMode_Object((1,3,6,1,2,1,180,1,1,1,3),_PwEnetVlanMode_Type())
pwEnetVlanMode.setMaxAccess(_C)
if mibBuilder.loadTexts:pwEnetVlanMode.setStatus(_A)
class _PwEnetPortVlan_Type(VlanIdOrAnyOrNone):defaultValue=4095
_PwEnetPortVlan_Type.__name__=_I
_PwEnetPortVlan_Object=MibTableColumn
pwEnetPortVlan=_PwEnetPortVlan_Object((1,3,6,1,2,1,180,1,1,1,4),_PwEnetPortVlan_Type())
pwEnetPortVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:pwEnetPortVlan.setStatus(_A)
_PwEnetPortIfIndex_Type=InterfaceIndexOrZero
_PwEnetPortIfIndex_Object=MibTableColumn
pwEnetPortIfIndex=_PwEnetPortIfIndex_Object((1,3,6,1,2,1,180,1,1,1,5),_PwEnetPortIfIndex_Type())
pwEnetPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pwEnetPortIfIndex.setStatus(_A)
class _PwEnetPwIfIndex_Type(InterfaceIndexOrZero):defaultValue=0
_PwEnetPwIfIndex_Type.__name__=_H
_PwEnetPwIfIndex_Object=MibTableColumn
pwEnetPwIfIndex=_PwEnetPwIfIndex_Object((1,3,6,1,2,1,180,1,1,1,6),_PwEnetPwIfIndex_Type())
pwEnetPwIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:pwEnetPwIfIndex.setStatus(_A)
_PwEnetRowStatus_Type=RowStatus
_PwEnetRowStatus_Object=MibTableColumn
pwEnetRowStatus=_PwEnetRowStatus_Object((1,3,6,1,2,1,180,1,1,1,7),_PwEnetRowStatus_Type())
pwEnetRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pwEnetRowStatus.setStatus(_A)
class _PwEnetStorageType_Type(StorageType):defaultValue=3
_PwEnetStorageType_Type.__name__=_K
_PwEnetStorageType_Object=MibTableColumn
pwEnetStorageType=_PwEnetStorageType_Object((1,3,6,1,2,1,180,1,1,1,8),_PwEnetStorageType_Type())
pwEnetStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:pwEnetStorageType.setStatus(_A)
_PwEnetStatsTable_Object=MibTable
pwEnetStatsTable=_PwEnetStatsTable_Object((1,3,6,1,2,1,180,1,2))
if mibBuilder.loadTexts:pwEnetStatsTable.setStatus(_A)
_PwEnetStatsEntry_Object=MibTableRow
pwEnetStatsEntry=_PwEnetStatsEntry_Object((1,3,6,1,2,1,180,1,2,1))
pwEnetStatsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:pwEnetStatsEntry.setStatus(_A)
_PwEnetStatsIllegalVlan_Type=ZeroBasedCounter32
_PwEnetStatsIllegalVlan_Object=MibTableColumn
pwEnetStatsIllegalVlan=_PwEnetStatsIllegalVlan_Object((1,3,6,1,2,1,180,1,2,1,1),_PwEnetStatsIllegalVlan_Type())
pwEnetStatsIllegalVlan.setMaxAccess(_M)
if mibBuilder.loadTexts:pwEnetStatsIllegalVlan.setStatus(_A)
_PwEnetStatsIllegalLength_Type=ZeroBasedCounter32
_PwEnetStatsIllegalLength_Object=MibTableColumn
pwEnetStatsIllegalLength=_PwEnetStatsIllegalLength_Object((1,3,6,1,2,1,180,1,2,1,2),_PwEnetStatsIllegalLength_Type())
pwEnetStatsIllegalLength.setMaxAccess(_M)
if mibBuilder.loadTexts:pwEnetStatsIllegalLength.setStatus(_A)
_PwEnetConformance_ObjectIdentity=ObjectIdentity
pwEnetConformance=_PwEnetConformance_ObjectIdentity((1,3,6,1,2,1,180,2))
_PwEnetGroups_ObjectIdentity=ObjectIdentity
pwEnetGroups=_PwEnetGroups_ObjectIdentity((1,3,6,1,2,1,180,2,1))
_PwEnetCompliances_ObjectIdentity=ObjectIdentity
pwEnetCompliances=_PwEnetCompliances_ObjectIdentity((1,3,6,1,2,1,180,2,2))
pwEnetGroup=ObjectGroup((1,3,6,1,2,1,180,2,1,1))
pwEnetGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:pwEnetGroup.setStatus(_A)
pwEnetStatsGroup=ObjectGroup((1,3,6,1,2,1,180,2,1,2))
pwEnetStatsGroup.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:pwEnetStatsGroup.setStatus(_A)
pwEnetModuleFullCompliance=ModuleCompliance((1,3,6,1,2,1,180,2,2,1))
pwEnetModuleFullCompliance.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:pwEnetModuleFullCompliance.setStatus(_A)
pwEnetModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,180,2,2,2))
pwEnetModuleReadOnlyCompliance.setObjects(*((_B,_F),(_B,_G)))
if mibBuilder.loadTexts:pwEnetModuleReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pwEnetStdMIB':pwEnetStdMIB,'pwEnetObjects':pwEnetObjects,'pwEnetTable':pwEnetTable,'pwEnetEntry':pwEnetEntry,_L:pwEnetPwInstance,_N:pwEnetPwVlan,_O:pwEnetVlanMode,_P:pwEnetPortVlan,_Q:pwEnetPortIfIndex,_R:pwEnetPwIfIndex,_S:pwEnetRowStatus,_T:pwEnetStorageType,'pwEnetStatsTable':pwEnetStatsTable,'pwEnetStatsEntry':pwEnetStatsEntry,_U:pwEnetStatsIllegalVlan,_V:pwEnetStatsIllegalLength,'pwEnetConformance':pwEnetConformance,'pwEnetGroups':pwEnetGroups,_F:pwEnetGroup,_G:pwEnetStatsGroup,'pwEnetCompliances':pwEnetCompliances,'pwEnetModuleFullCompliance':pwEnetModuleFullCompliance,'pwEnetModuleReadOnlyCompliance':pwEnetModuleReadOnlyCompliance})