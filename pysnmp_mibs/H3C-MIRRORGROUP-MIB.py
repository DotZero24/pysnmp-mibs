_R='h3cMGMirrorCpuSlot'
_Q='h3cMGMirrorCpuChassis'
_P='h3cMGMirrorVlanID'
_O='h3cMGEgressIfIndex'
_N='h3cMGRprobeVlanID'
_M='h3cMGReflectorIfIndex'
_L='h3cMGMonitorIfIndex'
_K='h3cMGMirrorDirection'
_J='h3cMGMirrorIfIndex'
_I='both'
_H='outbound'
_G='inbound'
_F='h3cMGID'
_E='not-accessible'
_D='Integer32'
_C='read-create'
_B='H3C-MIRRORGROUP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
h3cMirrGroup=ModuleIdentity((1,3,6,1,4,1,2011,10,2,68))
if mibBuilder.loadTexts:h3cMirrGroup.setRevisions(('2006-01-10 19:03',))
_H3cMGInfoObjects_ObjectIdentity=ObjectIdentity
h3cMGInfoObjects=_H3cMGInfoObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,68,1))
_H3cMGObjects_ObjectIdentity=ObjectIdentity
h3cMGObjects=_H3cMGObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,68,1,1))
_H3cMGTable_Object=MibTable
h3cMGTable=_H3cMGTable_Object((1,3,6,1,4,1,2011,10,2,68,1,1,1))
if mibBuilder.loadTexts:h3cMGTable.setStatus(_A)
_H3cMGEntry_Object=MibTableRow
h3cMGEntry=_H3cMGEntry_Object((1,3,6,1,4,1,2011,10,2,68,1,1,1,1))
h3cMGEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:h3cMGEntry.setStatus(_A)
class _H3cMGID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cMGID_Type.__name__=_D
_H3cMGID_Object=MibTableColumn
h3cMGID=_H3cMGID_Object((1,3,6,1,4,1,2011,10,2,68,1,1,1,1,1),_H3cMGID_Type())
h3cMGID.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMGID.setStatus(_A)
class _H3cMGType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('local',1),('remoteSource',2),('remoteDestination',3)))
_H3cMGType_Type.__name__=_D
_H3cMGType_Object=MibTableColumn
h3cMGType=_H3cMGType_Object((1,3,6,1,4,1,2011,10,2,68,1,1,1,1,2),_H3cMGType_Type())
h3cMGType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMGType.setStatus(_A)
class _H3cMGStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_H3cMGStatus_Type.__name__=_D
_H3cMGStatus_Object=MibTableColumn
h3cMGStatus=_H3cMGStatus_Object((1,3,6,1,4,1,2011,10,2,68,1,1,1,1,3),_H3cMGStatus_Type())
h3cMGStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:h3cMGStatus.setStatus(_A)
_H3cMGRowStatus_Type=RowStatus
_H3cMGRowStatus_Object=MibTableColumn
h3cMGRowStatus=_H3cMGRowStatus_Object((1,3,6,1,4,1,2011,10,2,68,1,1,1,1,4),_H3cMGRowStatus_Type())
h3cMGRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMGRowStatus.setStatus(_A)
_H3cMGMirrorIfObjects_ObjectIdentity=ObjectIdentity
h3cMGMirrorIfObjects=_H3cMGMirrorIfObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,68,1,2))
_H3cMGMirrorIfTable_Object=MibTable
h3cMGMirrorIfTable=_H3cMGMirrorIfTable_Object((1,3,6,1,4,1,2011,10,2,68,1,2,1))
if mibBuilder.loadTexts:h3cMGMirrorIfTable.setStatus(_A)
_H3cMGMirrorIfEntry_Object=MibTableRow
h3cMGMirrorIfEntry=_H3cMGMirrorIfEntry_Object((1,3,6,1,4,1,2011,10,2,68,1,2,1,1))
h3cMGMirrorIfEntry.setIndexNames((0,_B,_F),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:h3cMGMirrorIfEntry.setStatus(_A)
_H3cMGMirrorIfIndex_Type=Integer32
_H3cMGMirrorIfIndex_Object=MibTableColumn
h3cMGMirrorIfIndex=_H3cMGMirrorIfIndex_Object((1,3,6,1,4,1,2011,10,2,68,1,2,1,1,1),_H3cMGMirrorIfIndex_Type())
h3cMGMirrorIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMGMirrorIfIndex.setStatus(_A)
class _H3cMGMirrorDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_H3cMGMirrorDirection_Type.__name__=_D
_H3cMGMirrorDirection_Object=MibTableColumn
h3cMGMirrorDirection=_H3cMGMirrorDirection_Object((1,3,6,1,4,1,2011,10,2,68,1,2,1,1,2),_H3cMGMirrorDirection_Type())
h3cMGMirrorDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMGMirrorDirection.setStatus(_A)
_H3cMGMirrorRowStatus_Type=RowStatus
_H3cMGMirrorRowStatus_Object=MibTableColumn
h3cMGMirrorRowStatus=_H3cMGMirrorRowStatus_Object((1,3,6,1,4,1,2011,10,2,68,1,2,1,1,3),_H3cMGMirrorRowStatus_Type())
h3cMGMirrorRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMGMirrorRowStatus.setStatus(_A)
_H3cMGMonitorIfObjects_ObjectIdentity=ObjectIdentity
h3cMGMonitorIfObjects=_H3cMGMonitorIfObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,68,1,3))
_H3cMGMonitorIfTable_Object=MibTable
h3cMGMonitorIfTable=_H3cMGMonitorIfTable_Object((1,3,6,1,4,1,2011,10,2,68,1,3,1))
if mibBuilder.loadTexts:h3cMGMonitorIfTable.setStatus(_A)
_H3cMGMonitorIfEntry_Object=MibTableRow
h3cMGMonitorIfEntry=_H3cMGMonitorIfEntry_Object((1,3,6,1,4,1,2011,10,2,68,1,3,1,1))
h3cMGMonitorIfEntry.setIndexNames((0,_B,_F),(0,_B,_L))
if mibBuilder.loadTexts:h3cMGMonitorIfEntry.setStatus(_A)
_H3cMGMonitorIfIndex_Type=Integer32
_H3cMGMonitorIfIndex_Object=MibTableColumn
h3cMGMonitorIfIndex=_H3cMGMonitorIfIndex_Object((1,3,6,1,4,1,2011,10,2,68,1,3,1,1,1),_H3cMGMonitorIfIndex_Type())
h3cMGMonitorIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMGMonitorIfIndex.setStatus(_A)
_H3cMGMonitorRowStatus_Type=RowStatus
_H3cMGMonitorRowStatus_Object=MibTableColumn
h3cMGMonitorRowStatus=_H3cMGMonitorRowStatus_Object((1,3,6,1,4,1,2011,10,2,68,1,3,1,1,2),_H3cMGMonitorRowStatus_Type())
h3cMGMonitorRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMGMonitorRowStatus.setStatus(_A)
_H3cMGReflectorIfObjects_ObjectIdentity=ObjectIdentity
h3cMGReflectorIfObjects=_H3cMGReflectorIfObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,68,1,4))
_H3cMGReflectorIfTable_Object=MibTable
h3cMGReflectorIfTable=_H3cMGReflectorIfTable_Object((1,3,6,1,4,1,2011,10,2,68,1,4,1))
if mibBuilder.loadTexts:h3cMGReflectorIfTable.setStatus(_A)
_H3cMGReflectorIfEntry_Object=MibTableRow
h3cMGReflectorIfEntry=_H3cMGReflectorIfEntry_Object((1,3,6,1,4,1,2011,10,2,68,1,4,1,1))
h3cMGReflectorIfEntry.setIndexNames((0,_B,_F),(0,_B,_M))
if mibBuilder.loadTexts:h3cMGReflectorIfEntry.setStatus(_A)
_H3cMGReflectorIfIndex_Type=Integer32
_H3cMGReflectorIfIndex_Object=MibTableColumn
h3cMGReflectorIfIndex=_H3cMGReflectorIfIndex_Object((1,3,6,1,4,1,2011,10,2,68,1,4,1,1,1),_H3cMGReflectorIfIndex_Type())
h3cMGReflectorIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMGReflectorIfIndex.setStatus(_A)
_H3cMGReflectorRowStatus_Type=RowStatus
_H3cMGReflectorRowStatus_Object=MibTableColumn
h3cMGReflectorRowStatus=_H3cMGReflectorRowStatus_Object((1,3,6,1,4,1,2011,10,2,68,1,4,1,1,2),_H3cMGReflectorRowStatus_Type())
h3cMGReflectorRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMGReflectorRowStatus.setStatus(_A)
_H3cMGRprobeVlanObjects_ObjectIdentity=ObjectIdentity
h3cMGRprobeVlanObjects=_H3cMGRprobeVlanObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,68,1,5))
_H3cMGRprobeVlanTable_Object=MibTable
h3cMGRprobeVlanTable=_H3cMGRprobeVlanTable_Object((1,3,6,1,4,1,2011,10,2,68,1,5,1))
if mibBuilder.loadTexts:h3cMGRprobeVlanTable.setStatus(_A)
_H3cMGRprobeVlanEntry_Object=MibTableRow
h3cMGRprobeVlanEntry=_H3cMGRprobeVlanEntry_Object((1,3,6,1,4,1,2011,10,2,68,1,5,1,1))
h3cMGRprobeVlanEntry.setIndexNames((0,_B,_F),(0,_B,_N))
if mibBuilder.loadTexts:h3cMGRprobeVlanEntry.setStatus(_A)
class _H3cMGRprobeVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_H3cMGRprobeVlanID_Type.__name__=_D
_H3cMGRprobeVlanID_Object=MibTableColumn
h3cMGRprobeVlanID=_H3cMGRprobeVlanID_Object((1,3,6,1,4,1,2011,10,2,68,1,5,1,1,1),_H3cMGRprobeVlanID_Type())
h3cMGRprobeVlanID.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMGRprobeVlanID.setStatus(_A)
_H3cMGRprobeVlanRowStatus_Type=RowStatus
_H3cMGRprobeVlanRowStatus_Object=MibTableColumn
h3cMGRprobeVlanRowStatus=_H3cMGRprobeVlanRowStatus_Object((1,3,6,1,4,1,2011,10,2,68,1,5,1,1,2),_H3cMGRprobeVlanRowStatus_Type())
h3cMGRprobeVlanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMGRprobeVlanRowStatus.setStatus(_A)
_H3cMGEgressIfObjects_ObjectIdentity=ObjectIdentity
h3cMGEgressIfObjects=_H3cMGEgressIfObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,68,1,6))
_H3cMGEgressIfTable_Object=MibTable
h3cMGEgressIfTable=_H3cMGEgressIfTable_Object((1,3,6,1,4,1,2011,10,2,68,1,6,1))
if mibBuilder.loadTexts:h3cMGEgressIfTable.setStatus(_A)
_H3cMGEgressIfEntry_Object=MibTableRow
h3cMGEgressIfEntry=_H3cMGEgressIfEntry_Object((1,3,6,1,4,1,2011,10,2,68,1,6,1,1))
h3cMGEgressIfEntry.setIndexNames((0,_B,_F),(0,_B,_O))
if mibBuilder.loadTexts:h3cMGEgressIfEntry.setStatus(_A)
class _H3cMGEgressIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cMGEgressIfIndex_Type.__name__=_D
_H3cMGEgressIfIndex_Object=MibTableColumn
h3cMGEgressIfIndex=_H3cMGEgressIfIndex_Object((1,3,6,1,4,1,2011,10,2,68,1,6,1,1,1),_H3cMGEgressIfIndex_Type())
h3cMGEgressIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMGEgressIfIndex.setStatus(_A)
_H3cMGEgressRowStatus_Type=RowStatus
_H3cMGEgressRowStatus_Object=MibTableColumn
h3cMGEgressRowStatus=_H3cMGEgressRowStatus_Object((1,3,6,1,4,1,2011,10,2,68,1,6,1,1,2),_H3cMGEgressRowStatus_Type())
h3cMGEgressRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMGEgressRowStatus.setStatus(_A)
_H3cMGMirrorVlanObjects_ObjectIdentity=ObjectIdentity
h3cMGMirrorVlanObjects=_H3cMGMirrorVlanObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,68,1,7))
_H3cMGMirrorVlanTable_Object=MibTable
h3cMGMirrorVlanTable=_H3cMGMirrorVlanTable_Object((1,3,6,1,4,1,2011,10,2,68,1,7,1))
if mibBuilder.loadTexts:h3cMGMirrorVlanTable.setStatus(_A)
_H3cMGMirrorVlanEntry_Object=MibTableRow
h3cMGMirrorVlanEntry=_H3cMGMirrorVlanEntry_Object((1,3,6,1,4,1,2011,10,2,68,1,7,1,1))
h3cMGMirrorVlanEntry.setIndexNames((0,_B,_F),(0,_B,_P))
if mibBuilder.loadTexts:h3cMGMirrorVlanEntry.setStatus(_A)
class _H3cMGMirrorVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_H3cMGMirrorVlanID_Type.__name__=_D
_H3cMGMirrorVlanID_Object=MibTableColumn
h3cMGMirrorVlanID=_H3cMGMirrorVlanID_Object((1,3,6,1,4,1,2011,10,2,68,1,7,1,1,1),_H3cMGMirrorVlanID_Type())
h3cMGMirrorVlanID.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMGMirrorVlanID.setStatus(_A)
class _H3cMGMirrorVlanDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_H3cMGMirrorVlanDirection_Type.__name__=_D
_H3cMGMirrorVlanDirection_Object=MibTableColumn
h3cMGMirrorVlanDirection=_H3cMGMirrorVlanDirection_Object((1,3,6,1,4,1,2011,10,2,68,1,7,1,1,2),_H3cMGMirrorVlanDirection_Type())
h3cMGMirrorVlanDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMGMirrorVlanDirection.setStatus(_A)
_H3cMGMirrorVlanRowStatus_Type=RowStatus
_H3cMGMirrorVlanRowStatus_Object=MibTableColumn
h3cMGMirrorVlanRowStatus=_H3cMGMirrorVlanRowStatus_Object((1,3,6,1,4,1,2011,10,2,68,1,7,1,1,3),_H3cMGMirrorVlanRowStatus_Type())
h3cMGMirrorVlanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMGMirrorVlanRowStatus.setStatus(_A)
_H3cMGMirrorCpuObjects_ObjectIdentity=ObjectIdentity
h3cMGMirrorCpuObjects=_H3cMGMirrorCpuObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,68,1,8))
_H3cMGMirrorCpuTable_Object=MibTable
h3cMGMirrorCpuTable=_H3cMGMirrorCpuTable_Object((1,3,6,1,4,1,2011,10,2,68,1,8,1))
if mibBuilder.loadTexts:h3cMGMirrorCpuTable.setStatus(_A)
_H3cMGMirrorCpuEntry_Object=MibTableRow
h3cMGMirrorCpuEntry=_H3cMGMirrorCpuEntry_Object((1,3,6,1,4,1,2011,10,2,68,1,8,1,1))
h3cMGMirrorCpuEntry.setIndexNames((0,_B,_F),(0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:h3cMGMirrorCpuEntry.setStatus(_A)
_H3cMGMirrorCpuChassis_Type=Unsigned32
_H3cMGMirrorCpuChassis_Object=MibTableColumn
h3cMGMirrorCpuChassis=_H3cMGMirrorCpuChassis_Object((1,3,6,1,4,1,2011,10,2,68,1,8,1,1,1),_H3cMGMirrorCpuChassis_Type())
h3cMGMirrorCpuChassis.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMGMirrorCpuChassis.setStatus(_A)
_H3cMGMirrorCpuSlot_Type=Unsigned32
_H3cMGMirrorCpuSlot_Object=MibTableColumn
h3cMGMirrorCpuSlot=_H3cMGMirrorCpuSlot_Object((1,3,6,1,4,1,2011,10,2,68,1,8,1,1,2),_H3cMGMirrorCpuSlot_Type())
h3cMGMirrorCpuSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:h3cMGMirrorCpuSlot.setStatus(_A)
class _H3cMGMirrorCpuDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_H3cMGMirrorCpuDirection_Type.__name__=_D
_H3cMGMirrorCpuDirection_Object=MibTableColumn
h3cMGMirrorCpuDirection=_H3cMGMirrorCpuDirection_Object((1,3,6,1,4,1,2011,10,2,68,1,8,1,1,3),_H3cMGMirrorCpuDirection_Type())
h3cMGMirrorCpuDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMGMirrorCpuDirection.setStatus(_A)
_H3cMGMirrorCpuRowStatus_Type=RowStatus
_H3cMGMirrorCpuRowStatus_Object=MibTableColumn
h3cMGMirrorCpuRowStatus=_H3cMGMirrorCpuRowStatus_Object((1,3,6,1,4,1,2011,10,2,68,1,8,1,1,4),_H3cMGMirrorCpuRowStatus_Type())
h3cMGMirrorCpuRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMGMirrorCpuRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h3cMirrGroup':h3cMirrGroup,'h3cMGInfoObjects':h3cMGInfoObjects,'h3cMGObjects':h3cMGObjects,'h3cMGTable':h3cMGTable,'h3cMGEntry':h3cMGEntry,_F:h3cMGID,'h3cMGType':h3cMGType,'h3cMGStatus':h3cMGStatus,'h3cMGRowStatus':h3cMGRowStatus,'h3cMGMirrorIfObjects':h3cMGMirrorIfObjects,'h3cMGMirrorIfTable':h3cMGMirrorIfTable,'h3cMGMirrorIfEntry':h3cMGMirrorIfEntry,_J:h3cMGMirrorIfIndex,_K:h3cMGMirrorDirection,'h3cMGMirrorRowStatus':h3cMGMirrorRowStatus,'h3cMGMonitorIfObjects':h3cMGMonitorIfObjects,'h3cMGMonitorIfTable':h3cMGMonitorIfTable,'h3cMGMonitorIfEntry':h3cMGMonitorIfEntry,_L:h3cMGMonitorIfIndex,'h3cMGMonitorRowStatus':h3cMGMonitorRowStatus,'h3cMGReflectorIfObjects':h3cMGReflectorIfObjects,'h3cMGReflectorIfTable':h3cMGReflectorIfTable,'h3cMGReflectorIfEntry':h3cMGReflectorIfEntry,_M:h3cMGReflectorIfIndex,'h3cMGReflectorRowStatus':h3cMGReflectorRowStatus,'h3cMGRprobeVlanObjects':h3cMGRprobeVlanObjects,'h3cMGRprobeVlanTable':h3cMGRprobeVlanTable,'h3cMGRprobeVlanEntry':h3cMGRprobeVlanEntry,_N:h3cMGRprobeVlanID,'h3cMGRprobeVlanRowStatus':h3cMGRprobeVlanRowStatus,'h3cMGEgressIfObjects':h3cMGEgressIfObjects,'h3cMGEgressIfTable':h3cMGEgressIfTable,'h3cMGEgressIfEntry':h3cMGEgressIfEntry,_O:h3cMGEgressIfIndex,'h3cMGEgressRowStatus':h3cMGEgressRowStatus,'h3cMGMirrorVlanObjects':h3cMGMirrorVlanObjects,'h3cMGMirrorVlanTable':h3cMGMirrorVlanTable,'h3cMGMirrorVlanEntry':h3cMGMirrorVlanEntry,_P:h3cMGMirrorVlanID,'h3cMGMirrorVlanDirection':h3cMGMirrorVlanDirection,'h3cMGMirrorVlanRowStatus':h3cMGMirrorVlanRowStatus,'h3cMGMirrorCpuObjects':h3cMGMirrorCpuObjects,'h3cMGMirrorCpuTable':h3cMGMirrorCpuTable,'h3cMGMirrorCpuEntry':h3cMGMirrorCpuEntry,_Q:h3cMGMirrorCpuChassis,_R:h3cMGMirrorCpuSlot,'h3cMGMirrorCpuDirection':h3cMGMirrorCpuDirection,'h3cMGMirrorCpuRowStatus':h3cMGMirrorCpuRowStatus})