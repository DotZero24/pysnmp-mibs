_N='h3cDSPState'
_M='h3cDSPEnPhysicalIndex'
_L='h3cDSPVPMIndex'
_K='h3cVPMState'
_J='h3cVPMEnPhysicalIndex'
_I='offLine'
_H='normal'
_G='accessible-for-notify'
_F='h3cDSPIndex'
_E='h3cVPMIndex'
_D='Integer32'
_C='A3COM-HUAWEI-DSP-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
PhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cDSP=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,89))
if mibBuilder.loadTexts:h3cDSP.setRevisions(('2008-01-16 13:00',))
_H3cVPMStatusTable_Object=MibTable
h3cVPMStatusTable=_H3cVPMStatusTable_Object((1,3,6,1,4,1,43,45,1,10,2,89,1))
if mibBuilder.loadTexts:h3cVPMStatusTable.setStatus(_A)
_H3cVPMStatusEntry_Object=MibTableRow
h3cVPMStatusEntry=_H3cVPMStatusEntry_Object((1,3,6,1,4,1,43,45,1,10,2,89,1,1))
h3cVPMStatusEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:h3cVPMStatusEntry.setStatus(_A)
class _H3cVPMIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_H3cVPMIndex_Type.__name__=_D
_H3cVPMIndex_Object=MibTableColumn
h3cVPMIndex=_H3cVPMIndex_Object((1,3,6,1,4,1,43,45,1,10,2,89,1,1,1),_H3cVPMIndex_Type())
h3cVPMIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cVPMIndex.setStatus(_A)
_H3cVPMEnPhysicalIndex_Type=PhysicalIndex
_H3cVPMEnPhysicalIndex_Object=MibTableColumn
h3cVPMEnPhysicalIndex=_H3cVPMEnPhysicalIndex_Object((1,3,6,1,4,1,43,45,1,10,2,89,1,1,2),_H3cVPMEnPhysicalIndex_Type())
h3cVPMEnPhysicalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVPMEnPhysicalIndex.setStatus(_A)
class _H3cVPMState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('warning',2),('fatal',3),(_I,4)))
_H3cVPMState_Type.__name__=_D
_H3cVPMState_Object=MibTableColumn
h3cVPMState=_H3cVPMState_Object((1,3,6,1,4,1,43,45,1,10,2,89,1,1,3),_H3cVPMState_Type())
h3cVPMState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVPMState.setStatus(_A)
class _H3cVPMResourceUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cVPMResourceUtilization_Type.__name__=_D
_H3cVPMResourceUtilization_Object=MibTableColumn
h3cVPMResourceUtilization=_H3cVPMResourceUtilization_Object((1,3,6,1,4,1,43,45,1,10,2,89,1,1,4),_H3cVPMResourceUtilization_Type())
h3cVPMResourceUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVPMResourceUtilization.setStatus(_A)
class _H3cVPMHiWaterUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cVPMHiWaterUtilization_Type.__name__=_D
_H3cVPMHiWaterUtilization_Object=MibTableColumn
h3cVPMHiWaterUtilization=_H3cVPMHiWaterUtilization_Object((1,3,6,1,4,1,43,45,1,10,2,89,1,1,5),_H3cVPMHiWaterUtilization_Type())
h3cVPMHiWaterUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVPMHiWaterUtilization.setStatus(_A)
_H3cVPMMaxChannel_Type=Integer32
_H3cVPMMaxChannel_Object=MibTableColumn
h3cVPMMaxChannel=_H3cVPMMaxChannel_Object((1,3,6,1,4,1,43,45,1,10,2,89,1,1,6),_H3cVPMMaxChannel_Type())
h3cVPMMaxChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cVPMMaxChannel.setStatus(_A)
_H3cDSPStatusTable_Object=MibTable
h3cDSPStatusTable=_H3cDSPStatusTable_Object((1,3,6,1,4,1,43,45,1,10,2,89,2))
if mibBuilder.loadTexts:h3cDSPStatusTable.setStatus(_A)
_H3cDSPStatusEntry_Object=MibTableRow
h3cDSPStatusEntry=_H3cDSPStatusEntry_Object((1,3,6,1,4,1,43,45,1,10,2,89,2,1))
h3cDSPStatusEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:h3cDSPStatusEntry.setStatus(_A)
class _H3cDSPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_H3cDSPIndex_Type.__name__=_D
_H3cDSPIndex_Object=MibTableColumn
h3cDSPIndex=_H3cDSPIndex_Object((1,3,6,1,4,1,43,45,1,10,2,89,2,1,1),_H3cDSPIndex_Type())
h3cDSPIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDSPIndex.setStatus(_A)
class _H3cDSPVPMIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_H3cDSPVPMIndex_Type.__name__=_D
_H3cDSPVPMIndex_Object=MibTableColumn
h3cDSPVPMIndex=_H3cDSPVPMIndex_Object((1,3,6,1,4,1,43,45,1,10,2,89,2,1,2),_H3cDSPVPMIndex_Type())
h3cDSPVPMIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDSPVPMIndex.setStatus(_A)
_H3cDSPEnPhysicalIndex_Type=PhysicalIndex
_H3cDSPEnPhysicalIndex_Object=MibTableColumn
h3cDSPEnPhysicalIndex=_H3cDSPEnPhysicalIndex_Object((1,3,6,1,4,1,43,45,1,10,2,89,2,1,3),_H3cDSPEnPhysicalIndex_Type())
h3cDSPEnPhysicalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDSPEnPhysicalIndex.setStatus(_A)
_H3cDSPResetTime_Type=TimeTicks
_H3cDSPResetTime_Object=MibTableColumn
h3cDSPResetTime=_H3cDSPResetTime_Object((1,3,6,1,4,1,43,45,1,10,2,89,2,1,4),_H3cDSPResetTime_Type())
h3cDSPResetTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDSPResetTime.setStatus(_A)
_H3cDSPMaxChannel_Type=Integer32
_H3cDSPMaxChannel_Object=MibTableColumn
h3cDSPMaxChannel=_H3cDSPMaxChannel_Object((1,3,6,1,4,1,43,45,1,10,2,89,2,1,5),_H3cDSPMaxChannel_Type())
h3cDSPMaxChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDSPMaxChannel.setStatus(_A)
class _H3cDSPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4)));namedValues=NamedValues(*((_H,1),('fatal',3),(_I,4)))
_H3cDSPState_Type.__name__=_D
_H3cDSPState_Object=MibTableColumn
h3cDSPState=_H3cDSPState_Object((1,3,6,1,4,1,43,45,1,10,2,89,2,1,6),_H3cDSPState_Type())
h3cDSPState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDSPState.setStatus(_A)
_H3cDSPInUseChannel_Type=Integer32
_H3cDSPInUseChannel_Object=MibTableColumn
h3cDSPInUseChannel=_H3cDSPInUseChannel_Object((1,3,6,1,4,1,43,45,1,10,2,89,2,1,7),_H3cDSPInUseChannel_Type())
h3cDSPInUseChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDSPInUseChannel.setStatus(_A)
_H3cDSPTrap_ObjectIdentity=ObjectIdentity
h3cDSPTrap=_H3cDSPTrap_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,89,3))
_H3cDSPTrapPrex_ObjectIdentity=ObjectIdentity
h3cDSPTrapPrex=_H3cDSPTrapPrex_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,89,3,0))
h3cVPMStateChange=NotificationType((1,3,6,1,4,1,43,45,1,10,2,89,3,0,1))
h3cVPMStateChange.setObjects(*((_C,_E),(_C,_J),(_C,_K)))
if mibBuilder.loadTexts:h3cVPMStateChange.setStatus(_A)
h3cDSPStateChange=NotificationType((1,3,6,1,4,1,43,45,1,10,2,89,3,0,2))
h3cDSPStateChange.setObjects(*((_C,_F),(_C,_L),(_C,_M),(_C,_N)))
if mibBuilder.loadTexts:h3cDSPStateChange.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'h3cDSP':h3cDSP,'h3cVPMStatusTable':h3cVPMStatusTable,'h3cVPMStatusEntry':h3cVPMStatusEntry,_E:h3cVPMIndex,_J:h3cVPMEnPhysicalIndex,_K:h3cVPMState,'h3cVPMResourceUtilization':h3cVPMResourceUtilization,'h3cVPMHiWaterUtilization':h3cVPMHiWaterUtilization,'h3cVPMMaxChannel':h3cVPMMaxChannel,'h3cDSPStatusTable':h3cDSPStatusTable,'h3cDSPStatusEntry':h3cDSPStatusEntry,_F:h3cDSPIndex,_L:h3cDSPVPMIndex,_M:h3cDSPEnPhysicalIndex,'h3cDSPResetTime':h3cDSPResetTime,'h3cDSPMaxChannel':h3cDSPMaxChannel,_N:h3cDSPState,'h3cDSPInUseChannel':h3cDSPInUseChannel,'h3cDSPTrap':h3cDSPTrap,'h3cDSPTrapPrex':h3cDSPTrapPrex,'h3cVPMStateChange':h3cVPMStateChange,'h3cDSPStateChange':h3cDSPStateChange})