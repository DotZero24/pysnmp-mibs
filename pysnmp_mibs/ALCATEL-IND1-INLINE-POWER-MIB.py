_c='pethTrapsGroup'
_b='pethPwrSupplyNotSupported'
_a='pethPwrSupplyConflict'
_Z='alaPethMainPowerRedundancy'
_Y='alaPethMainPseComboPort'
_X='alaPethMainPsePriority'
_W='alaPethMainPseCapacitorDetect'
_V='alaPethMainPsePriorityDisconnect'
_U='alaPethMainPseMaxPower'
_T='alaPethMainPseAdminStatus'
_S='alaPethPsePortPowerClass'
_R='alaPethPsePortPowerStatus'
_Q='alaPethPsePortPowerActual'
_P='alaPethPsePortPowerMaximum'
_O='alaPethMainPseEntry'
_N='alaPethPsePortEntry'
_M='alaPethMainIndex'
_L='alaPethMainPseGroup'
_K='alaPethPsePortGroup'
_J='pethSourcePort'
_I='read-only'
_H='pethSourceSlot'
_G='accessible-for-notify'
_F='disable'
_E='enable'
_D='read-write'
_C='Integer32'
_B='ALCATEL-IND1-INLINE-POWER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
pethTraps,softentIND1InLinePower=mibBuilder.importSymbols('ALCATEL-IND1-BASE','pethTraps','softentIND1InLinePower')
pethMainPseEntry,pethPsePortEntry=mibBuilder.importSymbols('POWER-ETHERNET-MIB','pethMainPseEntry','pethPsePortEntry')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
alcatelIND1INLINEPOWERMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,27,1))
if mibBuilder.loadTexts:alcatelIND1INLINEPOWERMIB.setRevisions(('2009-09-24 00:00','2009-07-05 00:00','2009-04-16 00:00','2007-04-03 00:00'))
_AlaPethObjects_ObjectIdentity=ObjectIdentity
alaPethObjects=_AlaPethObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,27,1,1))
_AlaPethPsePortTable_Object=MibTable
alaPethPsePortTable=_AlaPethPsePortTable_Object((1,3,6,1,4,1,6486,800,1,2,1,27,1,1,1))
if mibBuilder.loadTexts:alaPethPsePortTable.setStatus(_A)
_AlaPethPsePortEntry_Object=MibTableRow
alaPethPsePortEntry=_AlaPethPsePortEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,27,1,1,1,1))
if mibBuilder.loadTexts:alaPethPsePortEntry.setStatus(_A)
class _AlaPethPsePortPowerMaximum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3000,75000))
_AlaPethPsePortPowerMaximum_Type.__name__=_C
_AlaPethPsePortPowerMaximum_Object=MibTableColumn
alaPethPsePortPowerMaximum=_AlaPethPsePortPowerMaximum_Object((1,3,6,1,4,1,6486,800,1,2,1,27,1,1,1,1,1),_AlaPethPsePortPowerMaximum_Type())
alaPethPsePortPowerMaximum.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPethPsePortPowerMaximum.setStatus(_A)
class _AlaPethPsePortPowerActual_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_AlaPethPsePortPowerActual_Type.__name__=_C
_AlaPethPsePortPowerActual_Object=MibTableColumn
alaPethPsePortPowerActual=_AlaPethPsePortPowerActual_Object((1,3,6,1,4,1,6486,800,1,2,1,27,1,1,1,1,2),_AlaPethPsePortPowerActual_Type())
alaPethPsePortPowerActual.setMaxAccess(_I)
if mibBuilder.loadTexts:alaPethPsePortPowerActual.setStatus(_A)
class _AlaPethPsePortPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('powerOn',1),('powerOff',2)))
_AlaPethPsePortPowerStatus_Type.__name__=_C
_AlaPethPsePortPowerStatus_Object=MibTableColumn
alaPethPsePortPowerStatus=_AlaPethPsePortPowerStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,27,1,1,1,1,3),_AlaPethPsePortPowerStatus_Type())
alaPethPsePortPowerStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:alaPethPsePortPowerStatus.setStatus(_A)
class _AlaPethPsePortPowerClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('class0',0),('class1',1),('class2',2),('class3',3),('class4',4),('class5',5)))
_AlaPethPsePortPowerClass_Type.__name__=_C
_AlaPethPsePortPowerClass_Object=MibTableColumn
alaPethPsePortPowerClass=_AlaPethPsePortPowerClass_Object((1,3,6,1,4,1,6486,800,1,2,1,27,1,1,1,1,4),_AlaPethPsePortPowerClass_Type())
alaPethPsePortPowerClass.setMaxAccess(_I)
if mibBuilder.loadTexts:alaPethPsePortPowerClass.setStatus(_A)
_AlaPethMainPseTable_Object=MibTable
alaPethMainPseTable=_AlaPethMainPseTable_Object((1,3,6,1,4,1,6486,800,1,2,1,27,1,1,2))
if mibBuilder.loadTexts:alaPethMainPseTable.setStatus(_A)
_AlaPethMainPseEntry_Object=MibTableRow
alaPethMainPseEntry=_AlaPethMainPseEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,27,1,1,2,1))
if mibBuilder.loadTexts:alaPethMainPseEntry.setStatus(_A)
class _AlaPethMainPseAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_AlaPethMainPseAdminStatus_Type.__name__=_C
_AlaPethMainPseAdminStatus_Object=MibTableColumn
alaPethMainPseAdminStatus=_AlaPethMainPseAdminStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,27,1,1,2,1,1),_AlaPethMainPseAdminStatus_Type())
alaPethMainPseAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPethMainPseAdminStatus.setStatus(_A)
class _AlaPethMainPseMaxPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(36,800))
_AlaPethMainPseMaxPower_Type.__name__=_C
_AlaPethMainPseMaxPower_Object=MibTableColumn
alaPethMainPseMaxPower=_AlaPethMainPseMaxPower_Object((1,3,6,1,4,1,6486,800,1,2,1,27,1,1,2,1,2),_AlaPethMainPseMaxPower_Type())
alaPethMainPseMaxPower.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPethMainPseMaxPower.setStatus(_A)
if mibBuilder.loadTexts:alaPethMainPseMaxPower.setUnits('Watts')
class _AlaPethMainPsePriorityDisconnect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPethMainPsePriorityDisconnect_Type.__name__=_C
_AlaPethMainPsePriorityDisconnect_Object=MibTableColumn
alaPethMainPsePriorityDisconnect=_AlaPethMainPsePriorityDisconnect_Object((1,3,6,1,4,1,6486,800,1,2,1,27,1,1,2,1,3),_AlaPethMainPsePriorityDisconnect_Type())
alaPethMainPsePriorityDisconnect.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPethMainPsePriorityDisconnect.setStatus(_A)
class _AlaPethMainPseCapacitorDetect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPethMainPseCapacitorDetect_Type.__name__=_C
_AlaPethMainPseCapacitorDetect_Object=MibTableColumn
alaPethMainPseCapacitorDetect=_AlaPethMainPseCapacitorDetect_Object((1,3,6,1,4,1,6486,800,1,2,1,27,1,1,2,1,4),_AlaPethMainPseCapacitorDetect_Type())
alaPethMainPseCapacitorDetect.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPethMainPseCapacitorDetect.setStatus(_A)
class _AlaPethMainPsePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('critical',1),('high',2),('low',3)))
_AlaPethMainPsePriority_Type.__name__=_C
_AlaPethMainPsePriority_Object=MibTableColumn
alaPethMainPsePriority=_AlaPethMainPsePriority_Object((1,3,6,1,4,1,6486,800,1,2,1,27,1,1,2,1,5),_AlaPethMainPsePriority_Type())
alaPethMainPsePriority.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPethMainPsePriority.setStatus(_A)
class _AlaPethMainPseComboPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPethMainPseComboPort_Type.__name__=_C
_AlaPethMainPseComboPort_Object=MibTableColumn
alaPethMainPseComboPort=_AlaPethMainPseComboPort_Object((1,3,6,1,4,1,6486,800,1,2,1,27,1,1,2,1,6),_AlaPethMainPseComboPort_Type())
alaPethMainPseComboPort.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPethMainPseComboPort.setStatus(_A)
_AlaPethNotificationObjects_ObjectIdentity=ObjectIdentity
alaPethNotificationObjects=_AlaPethNotificationObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,27,1,1,3))
class _PethSourceSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_PethSourceSlot_Type.__name__=_C
_PethSourceSlot_Object=MibScalar
pethSourceSlot=_PethSourceSlot_Object((1,3,6,1,4,1,6486,800,1,2,1,27,1,1,3,1),_PethSourceSlot_Type())
pethSourceSlot.setMaxAccess(_G)
if mibBuilder.loadTexts:pethSourceSlot.setStatus(_A)
class _PethSourcePort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_PethSourcePort_Type.__name__=_C
_PethSourcePort_Object=MibScalar
pethSourcePort=_PethSourcePort_Object((1,3,6,1,4,1,6486,800,1,2,1,27,1,1,3,2),_PethSourcePort_Type())
pethSourcePort.setMaxAccess(_G)
if mibBuilder.loadTexts:pethSourcePort.setStatus(_A)
class _PethSourcePortDetectionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_PethSourcePortDetectionStatus_Type.__name__=_C
_PethSourcePortDetectionStatus_Object=MibScalar
pethSourcePortDetectionStatus=_PethSourcePortDetectionStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,27,1,1,3,3),_PethSourcePortDetectionStatus_Type())
pethSourcePortDetectionStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:pethSourcePortDetectionStatus.setStatus(_A)
_PethSourcePortStatusChangeReason_Type=SnmpAdminString
_PethSourcePortStatusChangeReason_Object=MibScalar
pethSourcePortStatusChangeReason=_PethSourcePortStatusChangeReason_Object((1,3,6,1,4,1,6486,800,1,2,1,27,1,1,3,4),_PethSourcePortStatusChangeReason_Type())
pethSourcePortStatusChangeReason.setMaxAccess(_G)
if mibBuilder.loadTexts:pethSourcePortStatusChangeReason.setStatus(_A)
_AlaPethConformance_ObjectIdentity=ObjectIdentity
alaPethConformance=_AlaPethConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,27,1,2))
_AlaPethCompliances_ObjectIdentity=ObjectIdentity
alaPethCompliances=_AlaPethCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,27,1,2,1))
_AlaPethGroups_ObjectIdentity=ObjectIdentity
alaPethGroups=_AlaPethGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,27,1,2,2))
_AlaPethMain_ObjectIdentity=ObjectIdentity
alaPethMain=_AlaPethMain_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,27,1,3))
_AlaPethMainTable_Object=MibTable
alaPethMainTable=_AlaPethMainTable_Object((1,3,6,1,4,1,6486,800,1,2,1,27,1,3,1))
if mibBuilder.loadTexts:alaPethMainTable.setStatus(_A)
_AlaPethMainEntry_Object=MibTableRow
alaPethMainEntry=_AlaPethMainEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,27,1,3,1,1))
alaPethMainEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:alaPethMainEntry.setStatus(_A)
class _AlaPethMainIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_AlaPethMainIndex_Type.__name__=_C
_AlaPethMainIndex_Object=MibTableColumn
alaPethMainIndex=_AlaPethMainIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,27,1,3,1,1,1),_AlaPethMainIndex_Type())
alaPethMainIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:alaPethMainIndex.setStatus(_A)
class _AlaPethMainPowerRedundancy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_AlaPethMainPowerRedundancy_Type.__name__=_C
_AlaPethMainPowerRedundancy_Object=MibTableColumn
alaPethMainPowerRedundancy=_AlaPethMainPowerRedundancy_Object((1,3,6,1,4,1,6486,800,1,2,1,27,1,3,1,1,2),_AlaPethMainPowerRedundancy_Type())
alaPethMainPowerRedundancy.setMaxAccess(_D)
if mibBuilder.loadTexts:alaPethMainPowerRedundancy.setStatus(_A)
pethPsePortEntry.registerAugmentions((_B,_N))
alaPethPsePortEntry.setIndexNames(*pethPsePortEntry.getIndexNames())
pethMainPseEntry.registerAugmentions((_B,_O))
alaPethMainPseEntry.setIndexNames(*pethMainPseEntry.getIndexNames())
alaPethPsePortGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,27,1,2,2,1))
alaPethPsePortGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:alaPethPsePortGroup.setStatus(_A)
alaPethMainPseGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,27,1,2,2,2))
alaPethMainPseGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:alaPethMainPseGroup.setStatus(_A)
alaPethTrapObjGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,27,1,2,2,4))
alaPethTrapObjGroup.setObjects(*((_B,_H),(_B,_J)))
if mibBuilder.loadTexts:alaPethTrapObjGroup.setStatus(_A)
pethPwrSupplyConflict=NotificationType((1,3,6,1,4,1,6486,800,1,3,2,17,0,1))
pethPwrSupplyConflict.setObjects((_B,_H))
if mibBuilder.loadTexts:pethPwrSupplyConflict.setStatus(_A)
pethPwrSupplyNotSupported=NotificationType((1,3,6,1,4,1,6486,800,1,3,2,17,0,2))
pethPwrSupplyNotSupported.setObjects(*((_B,_H),(_B,_J)))
if mibBuilder.loadTexts:pethPwrSupplyNotSupported.setStatus(_A)
pethTrapsGroup=NotificationGroup((1,3,6,1,4,1,6486,800,1,2,1,27,1,2,2,3))
pethTrapsGroup.setObjects(*((_B,_a),(_B,_b)))
if mibBuilder.loadTexts:pethTrapsGroup.setStatus(_A)
alaPethCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,27,1,2,1,1))
alaPethCompliance.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:alaPethCompliance.setStatus(_A)
alaPethPseCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,27,1,2,1,2))
alaPethPseCompliance.setObjects(*((_B,_K),(_B,_L),(_B,_c)))
if mibBuilder.loadTexts:alaPethPseCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'alcatelIND1INLINEPOWERMIB':alcatelIND1INLINEPOWERMIB,'alaPethObjects':alaPethObjects,'alaPethPsePortTable':alaPethPsePortTable,_N:alaPethPsePortEntry,_P:alaPethPsePortPowerMaximum,_Q:alaPethPsePortPowerActual,_R:alaPethPsePortPowerStatus,_S:alaPethPsePortPowerClass,'alaPethMainPseTable':alaPethMainPseTable,_O:alaPethMainPseEntry,_T:alaPethMainPseAdminStatus,_U:alaPethMainPseMaxPower,_V:alaPethMainPsePriorityDisconnect,_W:alaPethMainPseCapacitorDetect,_X:alaPethMainPsePriority,_Y:alaPethMainPseComboPort,'alaPethNotificationObjects':alaPethNotificationObjects,_H:pethSourceSlot,_J:pethSourcePort,'pethSourcePortDetectionStatus':pethSourcePortDetectionStatus,'pethSourcePortStatusChangeReason':pethSourcePortStatusChangeReason,'alaPethConformance':alaPethConformance,'alaPethCompliances':alaPethCompliances,'alaPethCompliance':alaPethCompliance,'alaPethPseCompliance':alaPethPseCompliance,'alaPethGroups':alaPethGroups,_K:alaPethPsePortGroup,_L:alaPethMainPseGroup,_c:pethTrapsGroup,'alaPethTrapObjGroup':alaPethTrapObjGroup,'alaPethMain':alaPethMain,'alaPethMainTable':alaPethMainTable,'alaPethMainEntry':alaPethMainEntry,_M:alaPethMainIndex,_Z:alaPethMainPowerRedundancy,_a:pethPwrSupplyConflict,_b:pethPwrSupplyNotSupported})