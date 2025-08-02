_N='hpnicfDSPState'
_M='hpnicfDSPEnPhysicalIndex'
_L='hpnicfDSPVPMIndex'
_K='hpnicfVPMState'
_J='hpnicfVPMEnPhysicalIndex'
_I='offLine'
_H='normal'
_G='accessible-for-notify'
_F='hpnicfDSPIndex'
_E='hpnicfVPMIndex'
_D='Integer32'
_C='HPN-ICF-DSP-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PhysicalIndex,=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndex')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfDSP=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,89))
if mibBuilder.loadTexts:hpnicfDSP.setRevisions(('2008-01-16 13:00',))
_HpnicfVPMStatusTable_Object=MibTable
hpnicfVPMStatusTable=_HpnicfVPMStatusTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,89,1))
if mibBuilder.loadTexts:hpnicfVPMStatusTable.setStatus(_A)
_HpnicfVPMStatusEntry_Object=MibTableRow
hpnicfVPMStatusEntry=_HpnicfVPMStatusEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,89,1,1))
hpnicfVPMStatusEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:hpnicfVPMStatusEntry.setStatus(_A)
class _HpnicfVPMIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_HpnicfVPMIndex_Type.__name__=_D
_HpnicfVPMIndex_Object=MibTableColumn
hpnicfVPMIndex=_HpnicfVPMIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,89,1,1,1),_HpnicfVPMIndex_Type())
hpnicfVPMIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfVPMIndex.setStatus(_A)
_HpnicfVPMEnPhysicalIndex_Type=PhysicalIndex
_HpnicfVPMEnPhysicalIndex_Object=MibTableColumn
hpnicfVPMEnPhysicalIndex=_HpnicfVPMEnPhysicalIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,89,1,1,2),_HpnicfVPMEnPhysicalIndex_Type())
hpnicfVPMEnPhysicalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVPMEnPhysicalIndex.setStatus(_A)
class _HpnicfVPMState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_H,1),('warning',2),('fatal',3),(_I,4)))
_HpnicfVPMState_Type.__name__=_D
_HpnicfVPMState_Object=MibTableColumn
hpnicfVPMState=_HpnicfVPMState_Object((1,3,6,1,4,1,11,2,14,11,15,2,89,1,1,3),_HpnicfVPMState_Type())
hpnicfVPMState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVPMState.setStatus(_A)
class _HpnicfVPMResourceUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfVPMResourceUtilization_Type.__name__=_D
_HpnicfVPMResourceUtilization_Object=MibTableColumn
hpnicfVPMResourceUtilization=_HpnicfVPMResourceUtilization_Object((1,3,6,1,4,1,11,2,14,11,15,2,89,1,1,4),_HpnicfVPMResourceUtilization_Type())
hpnicfVPMResourceUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVPMResourceUtilization.setStatus(_A)
class _HpnicfVPMHiWaterUtilization_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfVPMHiWaterUtilization_Type.__name__=_D
_HpnicfVPMHiWaterUtilization_Object=MibTableColumn
hpnicfVPMHiWaterUtilization=_HpnicfVPMHiWaterUtilization_Object((1,3,6,1,4,1,11,2,14,11,15,2,89,1,1,5),_HpnicfVPMHiWaterUtilization_Type())
hpnicfVPMHiWaterUtilization.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVPMHiWaterUtilization.setStatus(_A)
_HpnicfVPMMaxChannel_Type=Integer32
_HpnicfVPMMaxChannel_Object=MibTableColumn
hpnicfVPMMaxChannel=_HpnicfVPMMaxChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,89,1,1,6),_HpnicfVPMMaxChannel_Type())
hpnicfVPMMaxChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfVPMMaxChannel.setStatus(_A)
_HpnicfDSPStatusTable_Object=MibTable
hpnicfDSPStatusTable=_HpnicfDSPStatusTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,89,2))
if mibBuilder.loadTexts:hpnicfDSPStatusTable.setStatus(_A)
_HpnicfDSPStatusEntry_Object=MibTableRow
hpnicfDSPStatusEntry=_HpnicfDSPStatusEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,89,2,1))
hpnicfDSPStatusEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:hpnicfDSPStatusEntry.setStatus(_A)
class _HpnicfDSPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_HpnicfDSPIndex_Type.__name__=_D
_HpnicfDSPIndex_Object=MibTableColumn
hpnicfDSPIndex=_HpnicfDSPIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,89,2,1,1),_HpnicfDSPIndex_Type())
hpnicfDSPIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDSPIndex.setStatus(_A)
class _HpnicfDSPVPMIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_HpnicfDSPVPMIndex_Type.__name__=_D
_HpnicfDSPVPMIndex_Object=MibTableColumn
hpnicfDSPVPMIndex=_HpnicfDSPVPMIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,89,2,1,2),_HpnicfDSPVPMIndex_Type())
hpnicfDSPVPMIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDSPVPMIndex.setStatus(_A)
_HpnicfDSPEnPhysicalIndex_Type=PhysicalIndex
_HpnicfDSPEnPhysicalIndex_Object=MibTableColumn
hpnicfDSPEnPhysicalIndex=_HpnicfDSPEnPhysicalIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,89,2,1,3),_HpnicfDSPEnPhysicalIndex_Type())
hpnicfDSPEnPhysicalIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDSPEnPhysicalIndex.setStatus(_A)
_HpnicfDSPResetTime_Type=TimeTicks
_HpnicfDSPResetTime_Object=MibTableColumn
hpnicfDSPResetTime=_HpnicfDSPResetTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,89,2,1,4),_HpnicfDSPResetTime_Type())
hpnicfDSPResetTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDSPResetTime.setStatus(_A)
_HpnicfDSPMaxChannel_Type=Integer32
_HpnicfDSPMaxChannel_Object=MibTableColumn
hpnicfDSPMaxChannel=_HpnicfDSPMaxChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,89,2,1,5),_HpnicfDSPMaxChannel_Type())
hpnicfDSPMaxChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDSPMaxChannel.setStatus(_A)
class _HpnicfDSPState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,4)));namedValues=NamedValues(*((_H,1),('fatal',3),(_I,4)))
_HpnicfDSPState_Type.__name__=_D
_HpnicfDSPState_Object=MibTableColumn
hpnicfDSPState=_HpnicfDSPState_Object((1,3,6,1,4,1,11,2,14,11,15,2,89,2,1,6),_HpnicfDSPState_Type())
hpnicfDSPState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDSPState.setStatus(_A)
_HpnicfDSPInUseChannel_Type=Integer32
_HpnicfDSPInUseChannel_Object=MibTableColumn
hpnicfDSPInUseChannel=_HpnicfDSPInUseChannel_Object((1,3,6,1,4,1,11,2,14,11,15,2,89,2,1,7),_HpnicfDSPInUseChannel_Type())
hpnicfDSPInUseChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDSPInUseChannel.setStatus(_A)
_HpnicfDSPTrap_ObjectIdentity=ObjectIdentity
hpnicfDSPTrap=_HpnicfDSPTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,89,3))
_HpnicfDSPTrapPrex_ObjectIdentity=ObjectIdentity
hpnicfDSPTrapPrex=_HpnicfDSPTrapPrex_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,89,3,0))
hpnicfVPMStateChange=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,89,3,0,1))
hpnicfVPMStateChange.setObjects(*((_C,_E),(_C,_J),(_C,_K)))
if mibBuilder.loadTexts:hpnicfVPMStateChange.setStatus(_A)
hpnicfDSPStateChange=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,89,3,0,2))
hpnicfDSPStateChange.setObjects(*((_C,_F),(_C,_L),(_C,_M),(_C,_N)))
if mibBuilder.loadTexts:hpnicfDSPStateChange.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'hpnicfDSP':hpnicfDSP,'hpnicfVPMStatusTable':hpnicfVPMStatusTable,'hpnicfVPMStatusEntry':hpnicfVPMStatusEntry,_E:hpnicfVPMIndex,_J:hpnicfVPMEnPhysicalIndex,_K:hpnicfVPMState,'hpnicfVPMResourceUtilization':hpnicfVPMResourceUtilization,'hpnicfVPMHiWaterUtilization':hpnicfVPMHiWaterUtilization,'hpnicfVPMMaxChannel':hpnicfVPMMaxChannel,'hpnicfDSPStatusTable':hpnicfDSPStatusTable,'hpnicfDSPStatusEntry':hpnicfDSPStatusEntry,_F:hpnicfDSPIndex,_L:hpnicfDSPVPMIndex,_M:hpnicfDSPEnPhysicalIndex,'hpnicfDSPResetTime':hpnicfDSPResetTime,'hpnicfDSPMaxChannel':hpnicfDSPMaxChannel,_N:hpnicfDSPState,'hpnicfDSPInUseChannel':hpnicfDSPInUseChannel,'hpnicfDSPTrap':hpnicfDSPTrap,'hpnicfDSPTrapPrex':hpnicfDSPTrapPrex,'hpnicfVPMStateChange':hpnicfVPMStateChange,'hpnicfDSPStateChange':hpnicfDSPStateChange})