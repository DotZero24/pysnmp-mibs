_R='hpnicfMGMirrorCpuSlot'
_Q='hpnicfMGMirrorCpuChassis'
_P='hpnicfMGMirrorVlanID'
_O='hpnicfMGEgressIfIndex'
_N='hpnicfMGRprobeVlanID'
_M='hpnicfMGReflectorIfIndex'
_L='hpnicfMGMonitorIfIndex'
_K='hpnicfMGMirrorDirection'
_J='hpnicfMGMirrorIfIndex'
_I='both'
_H='outbound'
_G='inbound'
_F='hpnicfMGID'
_E='not-accessible'
_D='Integer32'
_C='read-create'
_B='HPN-ICF-MIRRORGROUP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
hpnicfMirrGroup=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,68))
if mibBuilder.loadTexts:hpnicfMirrGroup.setRevisions(('2006-01-10 19:03',))
_HpnicfMGInfoObjects_ObjectIdentity=ObjectIdentity
hpnicfMGInfoObjects=_HpnicfMGInfoObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,68,1))
_HpnicfMGObjects_ObjectIdentity=ObjectIdentity
hpnicfMGObjects=_HpnicfMGObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,68,1,1))
_HpnicfMGTable_Object=MibTable
hpnicfMGTable=_HpnicfMGTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,1,1))
if mibBuilder.loadTexts:hpnicfMGTable.setStatus(_A)
_HpnicfMGEntry_Object=MibTableRow
hpnicfMGEntry=_HpnicfMGEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,1,1,1))
hpnicfMGEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:hpnicfMGEntry.setStatus(_A)
class _HpnicfMGID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfMGID_Type.__name__=_D
_HpnicfMGID_Object=MibTableColumn
hpnicfMGID=_HpnicfMGID_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,1,1,1,1),_HpnicfMGID_Type())
hpnicfMGID.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMGID.setStatus(_A)
class _HpnicfMGType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('local',1),('remoteSource',2),('remoteDestination',3)))
_HpnicfMGType_Type.__name__=_D
_HpnicfMGType_Object=MibTableColumn
hpnicfMGType=_HpnicfMGType_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,1,1,1,2),_HpnicfMGType_Type())
hpnicfMGType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMGType.setStatus(_A)
class _HpnicfMGStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_HpnicfMGStatus_Type.__name__=_D
_HpnicfMGStatus_Object=MibTableColumn
hpnicfMGStatus=_HpnicfMGStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,1,1,1,3),_HpnicfMGStatus_Type())
hpnicfMGStatus.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpnicfMGStatus.setStatus(_A)
_HpnicfMGRowStatus_Type=RowStatus
_HpnicfMGRowStatus_Object=MibTableColumn
hpnicfMGRowStatus=_HpnicfMGRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,1,1,1,4),_HpnicfMGRowStatus_Type())
hpnicfMGRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMGRowStatus.setStatus(_A)
_HpnicfMGMirrorIfObjects_ObjectIdentity=ObjectIdentity
hpnicfMGMirrorIfObjects=_HpnicfMGMirrorIfObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,68,1,2))
_HpnicfMGMirrorIfTable_Object=MibTable
hpnicfMGMirrorIfTable=_HpnicfMGMirrorIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,2,1))
if mibBuilder.loadTexts:hpnicfMGMirrorIfTable.setStatus(_A)
_HpnicfMGMirrorIfEntry_Object=MibTableRow
hpnicfMGMirrorIfEntry=_HpnicfMGMirrorIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,2,1,1))
hpnicfMGMirrorIfEntry.setIndexNames((0,_B,_F),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:hpnicfMGMirrorIfEntry.setStatus(_A)
_HpnicfMGMirrorIfIndex_Type=Integer32
_HpnicfMGMirrorIfIndex_Object=MibTableColumn
hpnicfMGMirrorIfIndex=_HpnicfMGMirrorIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,2,1,1,1),_HpnicfMGMirrorIfIndex_Type())
hpnicfMGMirrorIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMGMirrorIfIndex.setStatus(_A)
class _HpnicfMGMirrorDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_HpnicfMGMirrorDirection_Type.__name__=_D
_HpnicfMGMirrorDirection_Object=MibTableColumn
hpnicfMGMirrorDirection=_HpnicfMGMirrorDirection_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,2,1,1,2),_HpnicfMGMirrorDirection_Type())
hpnicfMGMirrorDirection.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMGMirrorDirection.setStatus(_A)
_HpnicfMGMirrorRowStatus_Type=RowStatus
_HpnicfMGMirrorRowStatus_Object=MibTableColumn
hpnicfMGMirrorRowStatus=_HpnicfMGMirrorRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,2,1,1,3),_HpnicfMGMirrorRowStatus_Type())
hpnicfMGMirrorRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMGMirrorRowStatus.setStatus(_A)
_HpnicfMGMonitorIfObjects_ObjectIdentity=ObjectIdentity
hpnicfMGMonitorIfObjects=_HpnicfMGMonitorIfObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,68,1,3))
_HpnicfMGMonitorIfTable_Object=MibTable
hpnicfMGMonitorIfTable=_HpnicfMGMonitorIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,3,1))
if mibBuilder.loadTexts:hpnicfMGMonitorIfTable.setStatus(_A)
_HpnicfMGMonitorIfEntry_Object=MibTableRow
hpnicfMGMonitorIfEntry=_HpnicfMGMonitorIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,3,1,1))
hpnicfMGMonitorIfEntry.setIndexNames((0,_B,_F),(0,_B,_L))
if mibBuilder.loadTexts:hpnicfMGMonitorIfEntry.setStatus(_A)
_HpnicfMGMonitorIfIndex_Type=Integer32
_HpnicfMGMonitorIfIndex_Object=MibTableColumn
hpnicfMGMonitorIfIndex=_HpnicfMGMonitorIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,3,1,1,1),_HpnicfMGMonitorIfIndex_Type())
hpnicfMGMonitorIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMGMonitorIfIndex.setStatus(_A)
_HpnicfMGMonitorRowStatus_Type=RowStatus
_HpnicfMGMonitorRowStatus_Object=MibTableColumn
hpnicfMGMonitorRowStatus=_HpnicfMGMonitorRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,3,1,1,2),_HpnicfMGMonitorRowStatus_Type())
hpnicfMGMonitorRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMGMonitorRowStatus.setStatus(_A)
_HpnicfMGReflectorIfObjects_ObjectIdentity=ObjectIdentity
hpnicfMGReflectorIfObjects=_HpnicfMGReflectorIfObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,68,1,4))
_HpnicfMGReflectorIfTable_Object=MibTable
hpnicfMGReflectorIfTable=_HpnicfMGReflectorIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,4,1))
if mibBuilder.loadTexts:hpnicfMGReflectorIfTable.setStatus(_A)
_HpnicfMGReflectorIfEntry_Object=MibTableRow
hpnicfMGReflectorIfEntry=_HpnicfMGReflectorIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,4,1,1))
hpnicfMGReflectorIfEntry.setIndexNames((0,_B,_F),(0,_B,_M))
if mibBuilder.loadTexts:hpnicfMGReflectorIfEntry.setStatus(_A)
_HpnicfMGReflectorIfIndex_Type=Integer32
_HpnicfMGReflectorIfIndex_Object=MibTableColumn
hpnicfMGReflectorIfIndex=_HpnicfMGReflectorIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,4,1,1,1),_HpnicfMGReflectorIfIndex_Type())
hpnicfMGReflectorIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMGReflectorIfIndex.setStatus(_A)
_HpnicfMGReflectorRowStatus_Type=RowStatus
_HpnicfMGReflectorRowStatus_Object=MibTableColumn
hpnicfMGReflectorRowStatus=_HpnicfMGReflectorRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,4,1,1,2),_HpnicfMGReflectorRowStatus_Type())
hpnicfMGReflectorRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMGReflectorRowStatus.setStatus(_A)
_HpnicfMGRprobeVlanObjects_ObjectIdentity=ObjectIdentity
hpnicfMGRprobeVlanObjects=_HpnicfMGRprobeVlanObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,68,1,5))
_HpnicfMGRprobeVlanTable_Object=MibTable
hpnicfMGRprobeVlanTable=_HpnicfMGRprobeVlanTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,5,1))
if mibBuilder.loadTexts:hpnicfMGRprobeVlanTable.setStatus(_A)
_HpnicfMGRprobeVlanEntry_Object=MibTableRow
hpnicfMGRprobeVlanEntry=_HpnicfMGRprobeVlanEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,5,1,1))
hpnicfMGRprobeVlanEntry.setIndexNames((0,_B,_F),(0,_B,_N))
if mibBuilder.loadTexts:hpnicfMGRprobeVlanEntry.setStatus(_A)
class _HpnicfMGRprobeVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpnicfMGRprobeVlanID_Type.__name__=_D
_HpnicfMGRprobeVlanID_Object=MibTableColumn
hpnicfMGRprobeVlanID=_HpnicfMGRprobeVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,5,1,1,1),_HpnicfMGRprobeVlanID_Type())
hpnicfMGRprobeVlanID.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMGRprobeVlanID.setStatus(_A)
_HpnicfMGRprobeVlanRowStatus_Type=RowStatus
_HpnicfMGRprobeVlanRowStatus_Object=MibTableColumn
hpnicfMGRprobeVlanRowStatus=_HpnicfMGRprobeVlanRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,5,1,1,2),_HpnicfMGRprobeVlanRowStatus_Type())
hpnicfMGRprobeVlanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMGRprobeVlanRowStatus.setStatus(_A)
_HpnicfMGEgressIfObjects_ObjectIdentity=ObjectIdentity
hpnicfMGEgressIfObjects=_HpnicfMGEgressIfObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,68,1,6))
_HpnicfMGEgressIfTable_Object=MibTable
hpnicfMGEgressIfTable=_HpnicfMGEgressIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,6,1))
if mibBuilder.loadTexts:hpnicfMGEgressIfTable.setStatus(_A)
_HpnicfMGEgressIfEntry_Object=MibTableRow
hpnicfMGEgressIfEntry=_HpnicfMGEgressIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,6,1,1))
hpnicfMGEgressIfEntry.setIndexNames((0,_B,_F),(0,_B,_O))
if mibBuilder.loadTexts:hpnicfMGEgressIfEntry.setStatus(_A)
class _HpnicfMGEgressIfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfMGEgressIfIndex_Type.__name__=_D
_HpnicfMGEgressIfIndex_Object=MibTableColumn
hpnicfMGEgressIfIndex=_HpnicfMGEgressIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,6,1,1,1),_HpnicfMGEgressIfIndex_Type())
hpnicfMGEgressIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMGEgressIfIndex.setStatus(_A)
_HpnicfMGEgressRowStatus_Type=RowStatus
_HpnicfMGEgressRowStatus_Object=MibTableColumn
hpnicfMGEgressRowStatus=_HpnicfMGEgressRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,6,1,1,2),_HpnicfMGEgressRowStatus_Type())
hpnicfMGEgressRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMGEgressRowStatus.setStatus(_A)
_HpnicfMGMirrorVlanObjects_ObjectIdentity=ObjectIdentity
hpnicfMGMirrorVlanObjects=_HpnicfMGMirrorVlanObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,68,1,7))
_HpnicfMGMirrorVlanTable_Object=MibTable
hpnicfMGMirrorVlanTable=_HpnicfMGMirrorVlanTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,7,1))
if mibBuilder.loadTexts:hpnicfMGMirrorVlanTable.setStatus(_A)
_HpnicfMGMirrorVlanEntry_Object=MibTableRow
hpnicfMGMirrorVlanEntry=_HpnicfMGMirrorVlanEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,7,1,1))
hpnicfMGMirrorVlanEntry.setIndexNames((0,_B,_F),(0,_B,_P))
if mibBuilder.loadTexts:hpnicfMGMirrorVlanEntry.setStatus(_A)
class _HpnicfMGMirrorVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpnicfMGMirrorVlanID_Type.__name__=_D
_HpnicfMGMirrorVlanID_Object=MibTableColumn
hpnicfMGMirrorVlanID=_HpnicfMGMirrorVlanID_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,7,1,1,1),_HpnicfMGMirrorVlanID_Type())
hpnicfMGMirrorVlanID.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMGMirrorVlanID.setStatus(_A)
class _HpnicfMGMirrorVlanDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_HpnicfMGMirrorVlanDirection_Type.__name__=_D
_HpnicfMGMirrorVlanDirection_Object=MibTableColumn
hpnicfMGMirrorVlanDirection=_HpnicfMGMirrorVlanDirection_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,7,1,1,2),_HpnicfMGMirrorVlanDirection_Type())
hpnicfMGMirrorVlanDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMGMirrorVlanDirection.setStatus(_A)
_HpnicfMGMirrorVlanRowStatus_Type=RowStatus
_HpnicfMGMirrorVlanRowStatus_Object=MibTableColumn
hpnicfMGMirrorVlanRowStatus=_HpnicfMGMirrorVlanRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,7,1,1,3),_HpnicfMGMirrorVlanRowStatus_Type())
hpnicfMGMirrorVlanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMGMirrorVlanRowStatus.setStatus(_A)
_HpnicfMGMirrorCpuObjects_ObjectIdentity=ObjectIdentity
hpnicfMGMirrorCpuObjects=_HpnicfMGMirrorCpuObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,68,1,8))
_HpnicfMGMirrorCpuTable_Object=MibTable
hpnicfMGMirrorCpuTable=_HpnicfMGMirrorCpuTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,8,1))
if mibBuilder.loadTexts:hpnicfMGMirrorCpuTable.setStatus(_A)
_HpnicfMGMirrorCpuEntry_Object=MibTableRow
hpnicfMGMirrorCpuEntry=_HpnicfMGMirrorCpuEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,8,1,1))
hpnicfMGMirrorCpuEntry.setIndexNames((0,_B,_F),(0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:hpnicfMGMirrorCpuEntry.setStatus(_A)
_HpnicfMGMirrorCpuChassis_Type=Unsigned32
_HpnicfMGMirrorCpuChassis_Object=MibTableColumn
hpnicfMGMirrorCpuChassis=_HpnicfMGMirrorCpuChassis_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,8,1,1,1),_HpnicfMGMirrorCpuChassis_Type())
hpnicfMGMirrorCpuChassis.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMGMirrorCpuChassis.setStatus(_A)
_HpnicfMGMirrorCpuSlot_Type=Unsigned32
_HpnicfMGMirrorCpuSlot_Object=MibTableColumn
hpnicfMGMirrorCpuSlot=_HpnicfMGMirrorCpuSlot_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,8,1,1,2),_HpnicfMGMirrorCpuSlot_Type())
hpnicfMGMirrorCpuSlot.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMGMirrorCpuSlot.setStatus(_A)
class _HpnicfMGMirrorCpuDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_H,2),(_I,3)))
_HpnicfMGMirrorCpuDirection_Type.__name__=_D
_HpnicfMGMirrorCpuDirection_Object=MibTableColumn
hpnicfMGMirrorCpuDirection=_HpnicfMGMirrorCpuDirection_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,8,1,1,3),_HpnicfMGMirrorCpuDirection_Type())
hpnicfMGMirrorCpuDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMGMirrorCpuDirection.setStatus(_A)
_HpnicfMGMirrorCpuRowStatus_Type=RowStatus
_HpnicfMGMirrorCpuRowStatus_Object=MibTableColumn
hpnicfMGMirrorCpuRowStatus=_HpnicfMGMirrorCpuRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,68,1,8,1,1,4),_HpnicfMGMirrorCpuRowStatus_Type())
hpnicfMGMirrorCpuRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMGMirrorCpuRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfMirrGroup':hpnicfMirrGroup,'hpnicfMGInfoObjects':hpnicfMGInfoObjects,'hpnicfMGObjects':hpnicfMGObjects,'hpnicfMGTable':hpnicfMGTable,'hpnicfMGEntry':hpnicfMGEntry,_F:hpnicfMGID,'hpnicfMGType':hpnicfMGType,'hpnicfMGStatus':hpnicfMGStatus,'hpnicfMGRowStatus':hpnicfMGRowStatus,'hpnicfMGMirrorIfObjects':hpnicfMGMirrorIfObjects,'hpnicfMGMirrorIfTable':hpnicfMGMirrorIfTable,'hpnicfMGMirrorIfEntry':hpnicfMGMirrorIfEntry,_J:hpnicfMGMirrorIfIndex,_K:hpnicfMGMirrorDirection,'hpnicfMGMirrorRowStatus':hpnicfMGMirrorRowStatus,'hpnicfMGMonitorIfObjects':hpnicfMGMonitorIfObjects,'hpnicfMGMonitorIfTable':hpnicfMGMonitorIfTable,'hpnicfMGMonitorIfEntry':hpnicfMGMonitorIfEntry,_L:hpnicfMGMonitorIfIndex,'hpnicfMGMonitorRowStatus':hpnicfMGMonitorRowStatus,'hpnicfMGReflectorIfObjects':hpnicfMGReflectorIfObjects,'hpnicfMGReflectorIfTable':hpnicfMGReflectorIfTable,'hpnicfMGReflectorIfEntry':hpnicfMGReflectorIfEntry,_M:hpnicfMGReflectorIfIndex,'hpnicfMGReflectorRowStatus':hpnicfMGReflectorRowStatus,'hpnicfMGRprobeVlanObjects':hpnicfMGRprobeVlanObjects,'hpnicfMGRprobeVlanTable':hpnicfMGRprobeVlanTable,'hpnicfMGRprobeVlanEntry':hpnicfMGRprobeVlanEntry,_N:hpnicfMGRprobeVlanID,'hpnicfMGRprobeVlanRowStatus':hpnicfMGRprobeVlanRowStatus,'hpnicfMGEgressIfObjects':hpnicfMGEgressIfObjects,'hpnicfMGEgressIfTable':hpnicfMGEgressIfTable,'hpnicfMGEgressIfEntry':hpnicfMGEgressIfEntry,_O:hpnicfMGEgressIfIndex,'hpnicfMGEgressRowStatus':hpnicfMGEgressRowStatus,'hpnicfMGMirrorVlanObjects':hpnicfMGMirrorVlanObjects,'hpnicfMGMirrorVlanTable':hpnicfMGMirrorVlanTable,'hpnicfMGMirrorVlanEntry':hpnicfMGMirrorVlanEntry,_P:hpnicfMGMirrorVlanID,'hpnicfMGMirrorVlanDirection':hpnicfMGMirrorVlanDirection,'hpnicfMGMirrorVlanRowStatus':hpnicfMGMirrorVlanRowStatus,'hpnicfMGMirrorCpuObjects':hpnicfMGMirrorCpuObjects,'hpnicfMGMirrorCpuTable':hpnicfMGMirrorCpuTable,'hpnicfMGMirrorCpuEntry':hpnicfMGMirrorCpuEntry,_Q:hpnicfMGMirrorCpuChassis,_R:hpnicfMGMirrorCpuSlot,'hpnicfMGMirrorCpuDirection':hpnicfMGMirrorCpuDirection,'hpnicfMGMirrorCpuRowStatus':hpnicfMGMirrorCpuRowStatus})