_O='DisplayString'
_N='Unsigned32'
_M='h3cFailoverSecondaryCpuID'
_L='h3cFailoverSecondarySlotID'
_K='h3cFailoverSecondaryChassisID'
_J='h3cFailoverPrimaryCpuID'
_I='h3cFailoverPrimarySlotID'
_H='h3cFailoverPrimaryChassisID'
_G='read-only'
_F='h3cFailoverName'
_E='read-create'
_D='h3cFailoverIndex'
_C='Integer32'
_B='current'
_A='H3C-FAILOVER-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_O,'PhysAddress','RowStatus','TextualConvention')
h3cFailover=ModuleIdentity((1,3,6,1,4,1,2011,10,2,164))
if mibBuilder.loadTexts:h3cFailover.setRevisions(('2015-10-27 10:40',))
_H3cFailoverScalarObjects_ObjectIdentity=ObjectIdentity
h3cFailoverScalarObjects=_H3cFailoverScalarObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,164,1))
_H3cFailoverMaxNum_Type=Unsigned32
_H3cFailoverMaxNum_Object=MibScalar
h3cFailoverMaxNum=_H3cFailoverMaxNum_Object((1,3,6,1,4,1,2011,10,2,164,1,1),_H3cFailoverMaxNum_Type())
h3cFailoverMaxNum.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cFailoverMaxNum.setStatus(_B)
_H3cFailoverCurrentNum_Type=Unsigned32
_H3cFailoverCurrentNum_Object=MibScalar
h3cFailoverCurrentNum=_H3cFailoverCurrentNum_Object((1,3,6,1,4,1,2011,10,2,164,1,2),_H3cFailoverCurrentNum_Type())
h3cFailoverCurrentNum.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cFailoverCurrentNum.setStatus(_B)
_H3cFailoverTables_ObjectIdentity=ObjectIdentity
h3cFailoverTables=_H3cFailoverTables_ObjectIdentity((1,3,6,1,4,1,2011,10,2,164,2))
_H3cFailoverCfgTable_Object=MibTable
h3cFailoverCfgTable=_H3cFailoverCfgTable_Object((1,3,6,1,4,1,2011,10,2,164,2,1))
if mibBuilder.loadTexts:h3cFailoverCfgTable.setStatus(_B)
_H3cFailoverCfgEntry_Object=MibTableRow
h3cFailoverCfgEntry=_H3cFailoverCfgEntry_Object((1,3,6,1,4,1,2011,10,2,164,2,1,1))
h3cFailoverCfgEntry.setIndexNames((0,_A,_D))
if mibBuilder.loadTexts:h3cFailoverCfgEntry.setStatus(_B)
class _H3cFailoverIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_H3cFailoverIndex_Type.__name__=_N
_H3cFailoverIndex_Object=MibTableColumn
h3cFailoverIndex=_H3cFailoverIndex_Object((1,3,6,1,4,1,2011,10,2,164,2,1,1,1),_H3cFailoverIndex_Type())
h3cFailoverIndex.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:h3cFailoverIndex.setStatus(_B)
class _H3cFailoverName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_H3cFailoverName_Type.__name__=_O
_H3cFailoverName_Object=MibTableColumn
h3cFailoverName=_H3cFailoverName_Object((1,3,6,1,4,1,2011,10,2,164,2,1,1,2),_H3cFailoverName_Type())
h3cFailoverName.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cFailoverName.setStatus(_B)
class _H3cFailoverPrimaryChassisID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_H3cFailoverPrimaryChassisID_Type.__name__=_C
_H3cFailoverPrimaryChassisID_Object=MibTableColumn
h3cFailoverPrimaryChassisID=_H3cFailoverPrimaryChassisID_Object((1,3,6,1,4,1,2011,10,2,164,2,1,1,3),_H3cFailoverPrimaryChassisID_Type())
h3cFailoverPrimaryChassisID.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cFailoverPrimaryChassisID.setStatus(_B)
class _H3cFailoverPrimarySlotID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_H3cFailoverPrimarySlotID_Type.__name__=_C
_H3cFailoverPrimarySlotID_Object=MibTableColumn
h3cFailoverPrimarySlotID=_H3cFailoverPrimarySlotID_Object((1,3,6,1,4,1,2011,10,2,164,2,1,1,4),_H3cFailoverPrimarySlotID_Type())
h3cFailoverPrimarySlotID.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cFailoverPrimarySlotID.setStatus(_B)
class _H3cFailoverPrimaryCpuID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,7))
_H3cFailoverPrimaryCpuID_Type.__name__=_C
_H3cFailoverPrimaryCpuID_Object=MibTableColumn
h3cFailoverPrimaryCpuID=_H3cFailoverPrimaryCpuID_Object((1,3,6,1,4,1,2011,10,2,164,2,1,1,5),_H3cFailoverPrimaryCpuID_Type())
h3cFailoverPrimaryCpuID.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cFailoverPrimaryCpuID.setStatus(_B)
class _H3cFailoverSecondaryChassisID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_H3cFailoverSecondaryChassisID_Type.__name__=_C
_H3cFailoverSecondaryChassisID_Object=MibTableColumn
h3cFailoverSecondaryChassisID=_H3cFailoverSecondaryChassisID_Object((1,3,6,1,4,1,2011,10,2,164,2,1,1,6),_H3cFailoverSecondaryChassisID_Type())
h3cFailoverSecondaryChassisID.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cFailoverSecondaryChassisID.setStatus(_B)
class _H3cFailoverSecondarySlotID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,255))
_H3cFailoverSecondarySlotID_Type.__name__=_C
_H3cFailoverSecondarySlotID_Object=MibTableColumn
h3cFailoverSecondarySlotID=_H3cFailoverSecondarySlotID_Object((1,3,6,1,4,1,2011,10,2,164,2,1,1,7),_H3cFailoverSecondarySlotID_Type())
h3cFailoverSecondarySlotID.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cFailoverSecondarySlotID.setStatus(_B)
class _H3cFailoverSecondaryCpuID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,7))
_H3cFailoverSecondaryCpuID_Type.__name__=_C
_H3cFailoverSecondaryCpuID_Object=MibTableColumn
h3cFailoverSecondaryCpuID=_H3cFailoverSecondaryCpuID_Object((1,3,6,1,4,1,2011,10,2,164,2,1,1,8),_H3cFailoverSecondaryCpuID_Type())
h3cFailoverSecondaryCpuID.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cFailoverSecondaryCpuID.setStatus(_B)
class _H3cFailoverState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('initial',1),('normal',2),('fault',3)))
_H3cFailoverState_Type.__name__=_C
_H3cFailoverState_Object=MibTableColumn
h3cFailoverState=_H3cFailoverState_Object((1,3,6,1,4,1,2011,10,2,164,2,1,1,9),_H3cFailoverState_Type())
h3cFailoverState.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cFailoverState.setStatus(_B)
_H3cFailoverRowStatus_Type=RowStatus
_H3cFailoverRowStatus_Object=MibTableColumn
h3cFailoverRowStatus=_H3cFailoverRowStatus_Object((1,3,6,1,4,1,2011,10,2,164,2,1,1,10),_H3cFailoverRowStatus_Type())
h3cFailoverRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cFailoverRowStatus.setStatus(_B)
_H3cFailoverNotification_ObjectIdentity=ObjectIdentity
h3cFailoverNotification=_H3cFailoverNotification_ObjectIdentity((1,3,6,1,4,1,2011,10,2,164,3))
_H3cFailoverTrap_ObjectIdentity=ObjectIdentity
h3cFailoverTrap=_H3cFailoverTrap_ObjectIdentity((1,3,6,1,4,1,2011,10,2,164,3,0))
h3cFailoverCreate=NotificationType((1,3,6,1,4,1,2011,10,2,164,3,0,1))
h3cFailoverCreate.setObjects(*((_A,_D),(_A,_F)))
if mibBuilder.loadTexts:h3cFailoverCreate.setStatus(_B)
h3cFailoverDelete=NotificationType((1,3,6,1,4,1,2011,10,2,164,3,0,2))
h3cFailoverDelete.setObjects(*((_A,_D),(_A,_F)))
if mibBuilder.loadTexts:h3cFailoverDelete.setStatus(_B)
h3cFailoverPrimaryNodeAdd=NotificationType((1,3,6,1,4,1,2011,10,2,164,3,0,3))
h3cFailoverPrimaryNodeAdd.setObjects(*((_A,_D),(_A,_F),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:h3cFailoverPrimaryNodeAdd.setStatus(_B)
h3cFailoverPrimaryNodeRemove=NotificationType((1,3,6,1,4,1,2011,10,2,164,3,0,4))
h3cFailoverPrimaryNodeRemove.setObjects(*((_A,_D),(_A,_F),(_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:h3cFailoverPrimaryNodeRemove.setStatus(_B)
h3cFailoverSecondaryNodeAdd=NotificationType((1,3,6,1,4,1,2011,10,2,164,3,0,5))
h3cFailoverSecondaryNodeAdd.setObjects(*((_A,_D),(_A,_F),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:h3cFailoverSecondaryNodeAdd.setStatus(_B)
h3cFailoverSecondaryNodeRemove=NotificationType((1,3,6,1,4,1,2011,10,2,164,3,0,6))
h3cFailoverSecondaryNodeRemove.setObjects(*((_A,_D),(_A,_F),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:h3cFailoverSecondaryNodeRemove.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'h3cFailover':h3cFailover,'h3cFailoverScalarObjects':h3cFailoverScalarObjects,'h3cFailoverMaxNum':h3cFailoverMaxNum,'h3cFailoverCurrentNum':h3cFailoverCurrentNum,'h3cFailoverTables':h3cFailoverTables,'h3cFailoverCfgTable':h3cFailoverCfgTable,'h3cFailoverCfgEntry':h3cFailoverCfgEntry,_D:h3cFailoverIndex,_F:h3cFailoverName,_H:h3cFailoverPrimaryChassisID,_I:h3cFailoverPrimarySlotID,_J:h3cFailoverPrimaryCpuID,_K:h3cFailoverSecondaryChassisID,_L:h3cFailoverSecondarySlotID,_M:h3cFailoverSecondaryCpuID,'h3cFailoverState':h3cFailoverState,'h3cFailoverRowStatus':h3cFailoverRowStatus,'h3cFailoverNotification':h3cFailoverNotification,'h3cFailoverTrap':h3cFailoverTrap,'h3cFailoverCreate':h3cFailoverCreate,'h3cFailoverDelete':h3cFailoverDelete,'h3cFailoverPrimaryNodeAdd':h3cFailoverPrimaryNodeAdd,'h3cFailoverPrimaryNodeRemove':h3cFailoverPrimaryNodeRemove,'h3cFailoverSecondaryNodeAdd':h3cFailoverSecondaryNodeAdd,'h3cFailoverSecondaryNodeRemove':h3cFailoverSecondaryNodeRemove})