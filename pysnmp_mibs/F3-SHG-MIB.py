_U='f3ShgMemberFlowPointGroup'
_T='f3ShgMemberFlowGroup'
_S='f3ShgMemberPortGroup'
_R='f3ShgGroup'
_Q='f3ShgMemberPortRowStatus'
_P='f3ShgMemberPortStorageType'
_O='f3ShgRowStatus'
_N='f3ShgStorageType'
_M='f3ShgAlias'
_L='read-only'
_K='f3ShgMemberPort'
_J='not-accessible'
_I='DisplayString'
_H='f3ShgMemberFlowPoint'
_G='f3ShgMemberFlow'
_F='read-create'
_E='f3ShgIndex'
_D='neIndex'
_C='CM-ENTITY-MIB'
_B='F3-SHG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsp150cm,=mibBuilder.importSymbols('ADVA-MIB','fsp150cm')
neIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,VariablePointer=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','RowStatus','StorageType','TextualConvention','VariablePointer')
f3SHGMIB=ModuleIdentity((1,3,6,1,4,1,2544,1,12,27))
if mibBuilder.loadTexts:f3SHGMIB.setRevisions(('2012-12-04 00:00',))
_F3ShgConfigObjects_ObjectIdentity=ObjectIdentity
f3ShgConfigObjects=_F3ShgConfigObjects_ObjectIdentity((1,3,6,1,4,1,2544,1,12,27,1))
_F3ShgTable_Object=MibTable
f3ShgTable=_F3ShgTable_Object((1,3,6,1,4,1,2544,1,12,27,1,1))
if mibBuilder.loadTexts:f3ShgTable.setStatus(_A)
_F3ShgEntry_Object=MibTableRow
f3ShgEntry=_F3ShgEntry_Object((1,3,6,1,4,1,2544,1,12,27,1,1,1))
f3ShgEntry.setIndexNames((0,_C,_D),(0,_B,_E))
if mibBuilder.loadTexts:f3ShgEntry.setStatus(_A)
_F3ShgIndex_Type=Unsigned32
_F3ShgIndex_Object=MibTableColumn
f3ShgIndex=_F3ShgIndex_Object((1,3,6,1,4,1,2544,1,12,27,1,1,1,1),_F3ShgIndex_Type())
f3ShgIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:f3ShgIndex.setStatus(_A)
class _F3ShgAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_F3ShgAlias_Type.__name__=_I
_F3ShgAlias_Object=MibTableColumn
f3ShgAlias=_F3ShgAlias_Object((1,3,6,1,4,1,2544,1,12,27,1,1,1,2),_F3ShgAlias_Type())
f3ShgAlias.setMaxAccess(_F)
if mibBuilder.loadTexts:f3ShgAlias.setStatus(_A)
_F3ShgStorageType_Type=StorageType
_F3ShgStorageType_Object=MibTableColumn
f3ShgStorageType=_F3ShgStorageType_Object((1,3,6,1,4,1,2544,1,12,27,1,1,1,3),_F3ShgStorageType_Type())
f3ShgStorageType.setMaxAccess(_F)
if mibBuilder.loadTexts:f3ShgStorageType.setStatus(_A)
_F3ShgRowStatus_Type=RowStatus
_F3ShgRowStatus_Object=MibTableColumn
f3ShgRowStatus=_F3ShgRowStatus_Object((1,3,6,1,4,1,2544,1,12,27,1,1,1,4),_F3ShgRowStatus_Type())
f3ShgRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:f3ShgRowStatus.setStatus(_A)
_F3ShgMemberPortTable_Object=MibTable
f3ShgMemberPortTable=_F3ShgMemberPortTable_Object((1,3,6,1,4,1,2544,1,12,27,1,2))
if mibBuilder.loadTexts:f3ShgMemberPortTable.setStatus(_A)
_F3ShgMemberPortEntry_Object=MibTableRow
f3ShgMemberPortEntry=_F3ShgMemberPortEntry_Object((1,3,6,1,4,1,2544,1,12,27,1,2,1))
f3ShgMemberPortEntry.setIndexNames((0,_C,_D),(0,_B,_E),(0,_B,_K))
if mibBuilder.loadTexts:f3ShgMemberPortEntry.setStatus(_A)
_F3ShgMemberPort_Type=VariablePointer
_F3ShgMemberPort_Object=MibTableColumn
f3ShgMemberPort=_F3ShgMemberPort_Object((1,3,6,1,4,1,2544,1,12,27,1,2,1,1),_F3ShgMemberPort_Type())
f3ShgMemberPort.setMaxAccess(_J)
if mibBuilder.loadTexts:f3ShgMemberPort.setStatus(_A)
_F3ShgMemberPortStorageType_Type=StorageType
_F3ShgMemberPortStorageType_Object=MibTableColumn
f3ShgMemberPortStorageType=_F3ShgMemberPortStorageType_Object((1,3,6,1,4,1,2544,1,12,27,1,2,1,2),_F3ShgMemberPortStorageType_Type())
f3ShgMemberPortStorageType.setMaxAccess(_F)
if mibBuilder.loadTexts:f3ShgMemberPortStorageType.setStatus(_A)
_F3ShgMemberPortRowStatus_Type=RowStatus
_F3ShgMemberPortRowStatus_Object=MibTableColumn
f3ShgMemberPortRowStatus=_F3ShgMemberPortRowStatus_Object((1,3,6,1,4,1,2544,1,12,27,1,2,1,3),_F3ShgMemberPortRowStatus_Type())
f3ShgMemberPortRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:f3ShgMemberPortRowStatus.setStatus(_A)
_F3ShgMemberFlowTable_Object=MibTable
f3ShgMemberFlowTable=_F3ShgMemberFlowTable_Object((1,3,6,1,4,1,2544,1,12,27,1,3))
if mibBuilder.loadTexts:f3ShgMemberFlowTable.setStatus(_A)
_F3ShgMemberFlowEntry_Object=MibTableRow
f3ShgMemberFlowEntry=_F3ShgMemberFlowEntry_Object((1,3,6,1,4,1,2544,1,12,27,1,3,1))
f3ShgMemberFlowEntry.setIndexNames((0,_C,_D),(0,_B,_E),(0,_B,_G))
if mibBuilder.loadTexts:f3ShgMemberFlowEntry.setStatus(_A)
_F3ShgMemberFlow_Type=VariablePointer
_F3ShgMemberFlow_Object=MibTableColumn
f3ShgMemberFlow=_F3ShgMemberFlow_Object((1,3,6,1,4,1,2544,1,12,27,1,3,1,1),_F3ShgMemberFlow_Type())
f3ShgMemberFlow.setMaxAccess(_L)
if mibBuilder.loadTexts:f3ShgMemberFlow.setStatus(_A)
_F3ShgMemberFlowPointTable_Object=MibTable
f3ShgMemberFlowPointTable=_F3ShgMemberFlowPointTable_Object((1,3,6,1,4,1,2544,1,12,27,1,4))
if mibBuilder.loadTexts:f3ShgMemberFlowPointTable.setStatus(_A)
_F3ShgMemberFlowPointEntry_Object=MibTableRow
f3ShgMemberFlowPointEntry=_F3ShgMemberFlowPointEntry_Object((1,3,6,1,4,1,2544,1,12,27,1,4,1))
f3ShgMemberFlowPointEntry.setIndexNames((0,_C,_D),(0,_B,_E),(0,_B,_H))
if mibBuilder.loadTexts:f3ShgMemberFlowPointEntry.setStatus(_A)
_F3ShgMemberFlowPoint_Type=VariablePointer
_F3ShgMemberFlowPoint_Object=MibTableColumn
f3ShgMemberFlowPoint=_F3ShgMemberFlowPoint_Object((1,3,6,1,4,1,2544,1,12,27,1,4,1,1),_F3ShgMemberFlowPoint_Type())
f3ShgMemberFlowPoint.setMaxAccess(_L)
if mibBuilder.loadTexts:f3ShgMemberFlowPoint.setStatus(_A)
_F3ShgConformance_ObjectIdentity=ObjectIdentity
f3ShgConformance=_F3ShgConformance_ObjectIdentity((1,3,6,1,4,1,2544,1,12,27,2))
_F3ShgCompliances_ObjectIdentity=ObjectIdentity
f3ShgCompliances=_F3ShgCompliances_ObjectIdentity((1,3,6,1,4,1,2544,1,12,27,2,1))
_F3ShgGroups_ObjectIdentity=ObjectIdentity
f3ShgGroups=_F3ShgGroups_ObjectIdentity((1,3,6,1,4,1,2544,1,12,27,2,2))
f3ShgGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,27,2,2,1))
f3ShgGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:f3ShgGroup.setStatus(_A)
f3ShgMemberPortGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,27,2,2,2))
f3ShgMemberPortGroup.setObjects(*((_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:f3ShgMemberPortGroup.setStatus(_A)
f3ShgMemberFlowGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,27,2,2,3))
f3ShgMemberFlowGroup.setObjects((_B,_G))
if mibBuilder.loadTexts:f3ShgMemberFlowGroup.setStatus(_A)
f3ShgMemberFlowPointGroup=ObjectGroup((1,3,6,1,4,1,2544,1,12,27,2,2,4))
f3ShgMemberFlowPointGroup.setObjects((_B,_H))
if mibBuilder.loadTexts:f3ShgMemberFlowPointGroup.setStatus(_A)
f3ShgCompliance=ModuleCompliance((1,3,6,1,4,1,2544,1,12,27,2,1,1))
f3ShgCompliance.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:f3ShgCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'f3SHGMIB':f3SHGMIB,'f3ShgConfigObjects':f3ShgConfigObjects,'f3ShgTable':f3ShgTable,'f3ShgEntry':f3ShgEntry,_E:f3ShgIndex,_M:f3ShgAlias,_N:f3ShgStorageType,_O:f3ShgRowStatus,'f3ShgMemberPortTable':f3ShgMemberPortTable,'f3ShgMemberPortEntry':f3ShgMemberPortEntry,_K:f3ShgMemberPort,_P:f3ShgMemberPortStorageType,_Q:f3ShgMemberPortRowStatus,'f3ShgMemberFlowTable':f3ShgMemberFlowTable,'f3ShgMemberFlowEntry':f3ShgMemberFlowEntry,_G:f3ShgMemberFlow,'f3ShgMemberFlowPointTable':f3ShgMemberFlowPointTable,'f3ShgMemberFlowPointEntry':f3ShgMemberFlowPointEntry,_H:f3ShgMemberFlowPoint,'f3ShgConformance':f3ShgConformance,'f3ShgCompliances':f3ShgCompliances,'f3ShgCompliance':f3ShgCompliance,'f3ShgGroups':f3ShgGroups,_R:f3ShgGroup,_S:f3ShgMemberPortGroup,_T:f3ShgMemberFlowGroup,_U:f3ShgMemberFlowPointGroup})