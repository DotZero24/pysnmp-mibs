_X='rcPoeUndervoltage'
_W='rcPoeOverload'
_V='rcPoeOverheat'
_U='rcPoePortPriority'
_T='rcPoePortCurrent'
_S='rcPoePortVoltage'
_R='rcPoePortClass'
_Q='rcPoePortPowered'
_P='rcPoePortAdmin'
_O='rcPoePort'
_N='rcPoeUndervoltageStatus'
_M='rcPoeOverloadStatus'
_L='rcPoeOverheatStatus'
_K='rcPoeConsumption'
_J='rcPoeReenableTime'
_I='rcPoeMinimumVoltage'
_H='rcPoeCapacity'
_G='seconds'
_F='Unsigned32'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='RUGGEDCOM-POE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ruggedcomMgmt,ruggedcomTraps=mibBuilder.importSymbols('RUGGEDCOM-MIB','ruggedcomMgmt','ruggedcomTraps')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
rcPoe=ModuleIdentity((1,3,6,1,4,1,15004,4,7))
if mibBuilder.loadTexts:rcPoe.setRevisions(('2021-09-07 14:00','2012-06-01 17:00','2011-02-20 10:00'))
_RcPoeBase_ObjectIdentity=ObjectIdentity
rcPoeBase=_RcPoeBase_ObjectIdentity((1,3,6,1,4,1,15004,4,7,1))
class _RcPoeCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RcPoeCapacity_Type.__name__=_C
_RcPoeCapacity_Object=MibScalar
rcPoeCapacity=_RcPoeCapacity_Object((1,3,6,1,4,1,15004,4,7,1,1),_RcPoeCapacity_Type())
rcPoeCapacity.setMaxAccess(_E)
if mibBuilder.loadTexts:rcPoeCapacity.setStatus(_A)
if mibBuilder.loadTexts:rcPoeCapacity.setUnits('W')
class _RcPoeMinimumVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(39,57))
_RcPoeMinimumVoltage_Type.__name__=_C
_RcPoeMinimumVoltage_Object=MibScalar
rcPoeMinimumVoltage=_RcPoeMinimumVoltage_Object((1,3,6,1,4,1,15004,4,7,1,2),_RcPoeMinimumVoltage_Type())
rcPoeMinimumVoltage.setMaxAccess(_E)
if mibBuilder.loadTexts:rcPoeMinimumVoltage.setStatus(_A)
if mibBuilder.loadTexts:rcPoeMinimumVoltage.setUnits('V')
class _RcPoeReenableTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(10,4294967295))
_RcPoeReenableTime_Type.__name__=_F
_RcPoeReenableTime_Object=MibScalar
rcPoeReenableTime=_RcPoeReenableTime_Object((1,3,6,1,4,1,15004,4,7,1,3),_RcPoeReenableTime_Type())
rcPoeReenableTime.setMaxAccess(_E)
if mibBuilder.loadTexts:rcPoeReenableTime.setStatus(_A)
if mibBuilder.loadTexts:rcPoeReenableTime.setUnits(_G)
_RcPoeConsumption_Type=Integer32
_RcPoeConsumption_Object=MibScalar
rcPoeConsumption=_RcPoeConsumption_Object((1,3,6,1,4,1,15004,4,7,1,4),_RcPoeConsumption_Type())
rcPoeConsumption.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPoeConsumption.setStatus(_A)
if mibBuilder.loadTexts:rcPoeConsumption.setUnits(_G)
_RcPoeOverheatStatus_Type=TruthValue
_RcPoeOverheatStatus_Object=MibScalar
rcPoeOverheatStatus=_RcPoeOverheatStatus_Object((1,3,6,1,4,1,15004,4,7,1,5),_RcPoeOverheatStatus_Type())
rcPoeOverheatStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPoeOverheatStatus.setStatus(_A)
_RcPoeOverloadStatus_Type=TruthValue
_RcPoeOverloadStatus_Object=MibScalar
rcPoeOverloadStatus=_RcPoeOverloadStatus_Object((1,3,6,1,4,1,15004,4,7,1,6),_RcPoeOverloadStatus_Type())
rcPoeOverloadStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPoeOverloadStatus.setStatus(_A)
_RcPoeUndervoltageStatus_Type=TruthValue
_RcPoeUndervoltageStatus_Object=MibScalar
rcPoeUndervoltageStatus=_RcPoeUndervoltageStatus_Object((1,3,6,1,4,1,15004,4,7,1,7),_RcPoeUndervoltageStatus_Type())
rcPoeUndervoltageStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPoeUndervoltageStatus.setStatus(_A)
_RcPoeTables_ObjectIdentity=ObjectIdentity
rcPoeTables=_RcPoeTables_ObjectIdentity((1,3,6,1,4,1,15004,4,7,2))
_RcPoePortTable_Object=MibTable
rcPoePortTable=_RcPoePortTable_Object((1,3,6,1,4,1,15004,4,7,2,1))
if mibBuilder.loadTexts:rcPoePortTable.setStatus(_A)
_RcPoePortEntry_Object=MibTableRow
rcPoePortEntry=_RcPoePortEntry_Object((1,3,6,1,4,1,15004,4,7,2,1,1))
rcPoePortEntry.setIndexNames((0,_B,'rcPoePortNumber'))
if mibBuilder.loadTexts:rcPoePortEntry.setStatus(_A)
class _RcPoePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RcPoePort_Type.__name__=_C
_RcPoePort_Object=MibTableColumn
rcPoePort=_RcPoePort_Object((1,3,6,1,4,1,15004,4,7,2,1,1,1),_RcPoePort_Type())
rcPoePort.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rcPoePort.setStatus(_A)
_RcPoePortAdmin_Type=TruthValue
_RcPoePortAdmin_Object=MibTableColumn
rcPoePortAdmin=_RcPoePortAdmin_Object((1,3,6,1,4,1,15004,4,7,2,1,1,2),_RcPoePortAdmin_Type())
rcPoePortAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:rcPoePortAdmin.setStatus(_A)
class _RcPoePortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('low',2)))
_RcPoePortPriority_Type.__name__=_C
_RcPoePortPriority_Object=MibTableColumn
rcPoePortPriority=_RcPoePortPriority_Object((1,3,6,1,4,1,15004,4,7,2,1,1,3),_RcPoePortPriority_Type())
rcPoePortPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:rcPoePortPriority.setStatus(_A)
class _RcPoePortPowered_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('powerOn',1),('powerOff',2),('twoPairsOn',3),('fourPairsOn',4)))
_RcPoePortPowered_Type.__name__=_C
_RcPoePortPowered_Object=MibTableColumn
rcPoePortPowered=_RcPoePortPowered_Object((1,3,6,1,4,1,15004,4,7,2,1,1,4),_RcPoePortPowered_Type())
rcPoePortPowered.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPoePortPowered.setStatus(_A)
class _RcPoePortClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RcPoePortClass_Type.__name__=_C
_RcPoePortClass_Object=MibTableColumn
rcPoePortClass=_RcPoePortClass_Object((1,3,6,1,4,1,15004,4,7,2,1,1,5),_RcPoePortClass_Type())
rcPoePortClass.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPoePortClass.setStatus(_A)
class _RcPoePortVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RcPoePortVoltage_Type.__name__=_C
_RcPoePortVoltage_Object=MibTableColumn
rcPoePortVoltage=_RcPoePortVoltage_Object((1,3,6,1,4,1,15004,4,7,2,1,1,6),_RcPoePortVoltage_Type())
rcPoePortVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPoePortVoltage.setStatus(_A)
if mibBuilder.loadTexts:rcPoePortVoltage.setUnits('V')
class _RcPoePortCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RcPoePortCurrent_Type.__name__=_C
_RcPoePortCurrent_Object=MibTableColumn
rcPoePortCurrent=_RcPoePortCurrent_Object((1,3,6,1,4,1,15004,4,7,2,1,1,7),_RcPoePortCurrent_Type())
rcPoePortCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:rcPoePortCurrent.setStatus(_A)
if mibBuilder.loadTexts:rcPoePortCurrent.setUnits('mA')
_RcPoeConformance_ObjectIdentity=ObjectIdentity
rcPoeConformance=_RcPoeConformance_ObjectIdentity((1,3,6,1,4,1,15004,4,7,3))
_RcPoeGroups_ObjectIdentity=ObjectIdentity
rcPoeGroups=_RcPoeGroups_ObjectIdentity((1,3,6,1,4,1,15004,4,7,3,2))
_RuggedcomPoeTraps_ObjectIdentity=ObjectIdentity
ruggedcomPoeTraps=_RuggedcomPoeTraps_ObjectIdentity((1,3,6,1,4,1,15004,5,12))
rcBasePoeGroup=ObjectGroup((1,3,6,1,4,1,15004,4,7,3,2,1))
rcBasePoeGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:rcBasePoeGroup.setStatus(_A)
rcBasePoeStatusGroup=ObjectGroup((1,3,6,1,4,1,15004,4,7,3,2,2))
rcBasePoeStatusGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:rcBasePoeStatusGroup.setStatus(_A)
rcPoeTableGroup=ObjectGroup((1,3,6,1,4,1,15004,4,7,3,2,3))
rcPoeTableGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:rcPoeTableGroup.setStatus(_A)
rcPoeTablePriorityGroup=ObjectGroup((1,3,6,1,4,1,15004,4,7,3,2,4))
rcPoeTablePriorityGroup.setObjects((_B,_U))
if mibBuilder.loadTexts:rcPoeTablePriorityGroup.setStatus(_A)
rcPoeNotifyGroup=ObjectGroup((1,3,6,1,4,1,15004,4,7,3,2,5))
rcPoeNotifyGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:rcPoeNotifyGroup.setStatus(_A)
rcPoeOverheat=NotificationType((1,3,6,1,4,1,15004,5,12,1))
if mibBuilder.loadTexts:rcPoeOverheat.setStatus(_A)
rcPoeOverload=NotificationType((1,3,6,1,4,1,15004,5,12,2))
if mibBuilder.loadTexts:rcPoeOverload.setStatus(_A)
rcPoeUndervoltage=NotificationType((1,3,6,1,4,1,15004,5,12,3))
if mibBuilder.loadTexts:rcPoeUndervoltage.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rcPoe':rcPoe,'rcPoeBase':rcPoeBase,_H:rcPoeCapacity,_I:rcPoeMinimumVoltage,_J:rcPoeReenableTime,_K:rcPoeConsumption,_L:rcPoeOverheatStatus,_M:rcPoeOverloadStatus,_N:rcPoeUndervoltageStatus,'rcPoeTables':rcPoeTables,'rcPoePortTable':rcPoePortTable,'rcPoePortEntry':rcPoePortEntry,_O:rcPoePort,_P:rcPoePortAdmin,_U:rcPoePortPriority,_Q:rcPoePortPowered,_R:rcPoePortClass,_S:rcPoePortVoltage,_T:rcPoePortCurrent,'rcPoeConformance':rcPoeConformance,'rcPoeGroups':rcPoeGroups,'rcBasePoeGroup':rcBasePoeGroup,'rcBasePoeStatusGroup':rcBasePoeStatusGroup,'rcPoeTableGroup':rcPoeTableGroup,'rcPoeTablePriorityGroup':rcPoeTablePriorityGroup,'rcPoeNotifyGroup':rcPoeNotifyGroup,'ruggedcomPoeTraps':ruggedcomPoeTraps,_V:rcPoeOverheat,_W:rcPoeOverload,_X:rcPoeUndervoltage})