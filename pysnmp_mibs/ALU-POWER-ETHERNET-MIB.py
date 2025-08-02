_m='pethMainPowerUsageOffNotification'
_l='pethMainPowerUsageOnNotification'
_k='pethPsePortPowerMaintenanceStatusNotification'
_j='pethPsePortOnOffNotification'
_i='pethNotificationControlEnable'
_h='pethMainPseUsageThreshold'
_g='pethMainPseOperStatus'
_f='pethMainPsePower'
_e='pethPdPortAdminEnable'
_d='pethPsePortPowerClassifications'
_c='pethPsePortType'
_b='pethPsePortOverCurrentCounter'
_a='pethPsePortMPSAbsentCounter'
_Z='pethPsePortPowerPriority'
_Y='pethPsePortPowerPairs'
_X='pethPsePortPowerDetectionControl'
_W='pethPsePortPowerPairsControlAbility'
_V='pethPsePortAdminEnable'
_U='pethNotificationControlGroupIndex'
_T='pethMainPseGroupIndex'
_S='pethPdPortIndex'
_R='pethPsePortIndex'
_Q='pethPsePortGroupIndex'
_P='Gauge32'
_O='pethNotificationControlGroup'
_N='pethMainPseGroup'
_M='pethPdPortGroup'
_L='pethPsePortGroup'
_K='pethPsePortPowerMaintenanceStatus'
_J='pethPsePortDetectionStatus'
_I='disable'
_H='enable'
_G='pethMainPseConsumptionPower'
_F='not-accessible'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='ALU-POWER-ETHERNET-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1InLinePower,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1InLinePower')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_P,_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
powerEthernetMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,27,999))
if mibBuilder.loadTexts:powerEthernetMIB.setRevisions(('2002-12-02 00:00',))
_PethNotifications_ObjectIdentity=ObjectIdentity
pethNotifications=_PethNotifications_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,27,999,0))
_PethObjects_ObjectIdentity=ObjectIdentity
pethObjects=_PethObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,27,999,1))
_PethPsePortTable_Object=MibTable
pethPsePortTable=_PethPsePortTable_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,1))
if mibBuilder.loadTexts:pethPsePortTable.setStatus(_A)
_PethPsePortEntry_Object=MibTableRow
pethPsePortEntry=_PethPsePortEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,1,1))
pethPsePortEntry.setIndexNames((0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:pethPsePortEntry.setStatus(_A)
class _PethPsePortGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PethPsePortGroupIndex_Type.__name__=_C
_PethPsePortGroupIndex_Object=MibTableColumn
pethPsePortGroupIndex=_PethPsePortGroupIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,1,1,1),_PethPsePortGroupIndex_Type())
pethPsePortGroupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:pethPsePortGroupIndex.setStatus(_A)
class _PethPsePortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PethPsePortIndex_Type.__name__=_C
_PethPsePortIndex_Object=MibTableColumn
pethPsePortIndex=_PethPsePortIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,1,1,2),_PethPsePortIndex_Type())
pethPsePortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:pethPsePortIndex.setStatus(_A)
class _PethPsePortAdminEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_PethPsePortAdminEnable_Type.__name__=_C
_PethPsePortAdminEnable_Object=MibTableColumn
pethPsePortAdminEnable=_PethPsePortAdminEnable_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,1,1,3),_PethPsePortAdminEnable_Type())
pethPsePortAdminEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:pethPsePortAdminEnable.setStatus(_A)
_PethPsePortPowerPairsControlAbility_Type=TruthValue
_PethPsePortPowerPairsControlAbility_Object=MibTableColumn
pethPsePortPowerPairsControlAbility=_PethPsePortPowerPairsControlAbility_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,1,1,4),_PethPsePortPowerPairsControlAbility_Type())
pethPsePortPowerPairsControlAbility.setMaxAccess(_D)
if mibBuilder.loadTexts:pethPsePortPowerPairsControlAbility.setStatus(_A)
class _PethPsePortPowerPairs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('signal',1),('spare',2)))
_PethPsePortPowerPairs_Type.__name__=_C
_PethPsePortPowerPairs_Object=MibTableColumn
pethPsePortPowerPairs=_PethPsePortPowerPairs_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,1,1,5),_PethPsePortPowerPairs_Type())
pethPsePortPowerPairs.setMaxAccess(_E)
if mibBuilder.loadTexts:pethPsePortPowerPairs.setStatus(_A)
class _PethPsePortPowerDetectionControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),('test',2)))
_PethPsePortPowerDetectionControl_Type.__name__=_C
_PethPsePortPowerDetectionControl_Object=MibTableColumn
pethPsePortPowerDetectionControl=_PethPsePortPowerDetectionControl_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,1,1,6),_PethPsePortPowerDetectionControl_Type())
pethPsePortPowerDetectionControl.setMaxAccess(_E)
if mibBuilder.loadTexts:pethPsePortPowerDetectionControl.setStatus(_A)
class _PethPsePortDetectionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,7,8)));namedValues=NamedValues(*(('disabled',1),('searching',2),('deliveringPower',4),('fault',5),('test',7),('denyLowPriority',8)))
_PethPsePortDetectionStatus_Type.__name__=_C
_PethPsePortDetectionStatus_Object=MibTableColumn
pethPsePortDetectionStatus=_PethPsePortDetectionStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,1,1,7),_PethPsePortDetectionStatus_Type())
pethPsePortDetectionStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pethPsePortDetectionStatus.setStatus(_A)
class _PethPsePortPowerPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('critical',1),('high',2),('low',3)))
_PethPsePortPowerPriority_Type.__name__=_C
_PethPsePortPowerPriority_Object=MibTableColumn
pethPsePortPowerPriority=_PethPsePortPowerPriority_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,1,1,8),_PethPsePortPowerPriority_Type())
pethPsePortPowerPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:pethPsePortPowerPriority.setStatus(_A)
class _PethPsePortPowerMaintenanceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ok',1),('underCurrent',2),('mPSAbsent',3)))
_PethPsePortPowerMaintenanceStatus_Type.__name__=_C
_PethPsePortPowerMaintenanceStatus_Object=MibTableColumn
pethPsePortPowerMaintenanceStatus=_PethPsePortPowerMaintenanceStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,1,1,10),_PethPsePortPowerMaintenanceStatus_Type())
pethPsePortPowerMaintenanceStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pethPsePortPowerMaintenanceStatus.setStatus(_A)
_PethPsePortMPSAbsentCounter_Type=Counter32
_PethPsePortMPSAbsentCounter_Object=MibTableColumn
pethPsePortMPSAbsentCounter=_PethPsePortMPSAbsentCounter_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,1,1,11),_PethPsePortMPSAbsentCounter_Type())
pethPsePortMPSAbsentCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:pethPsePortMPSAbsentCounter.setStatus(_A)
_PethPsePortOverCurrentCounter_Type=Counter32
_PethPsePortOverCurrentCounter_Object=MibTableColumn
pethPsePortOverCurrentCounter=_PethPsePortOverCurrentCounter_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,1,1,12),_PethPsePortOverCurrentCounter_Type())
pethPsePortOverCurrentCounter.setMaxAccess(_D)
if mibBuilder.loadTexts:pethPsePortOverCurrentCounter.setStatus(_A)
class _PethPsePortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('telephone',2),('webcam',3),('wireless',4)))
_PethPsePortType_Type.__name__=_C
_PethPsePortType_Object=MibTableColumn
pethPsePortType=_PethPsePortType_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,1,1,13),_PethPsePortType_Type())
pethPsePortType.setMaxAccess(_E)
if mibBuilder.loadTexts:pethPsePortType.setStatus(_A)
class _PethPsePortPowerClassifications_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('class0',1),('class1',2),('class2',3),('class3',4),('class4',5)))
_PethPsePortPowerClassifications_Type.__name__=_C
_PethPsePortPowerClassifications_Object=MibTableColumn
pethPsePortPowerClassifications=_PethPsePortPowerClassifications_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,1,1,14),_PethPsePortPowerClassifications_Type())
pethPsePortPowerClassifications.setMaxAccess(_D)
if mibBuilder.loadTexts:pethPsePortPowerClassifications.setStatus(_A)
_PethPdPortTable_Object=MibTable
pethPdPortTable=_PethPdPortTable_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,2))
if mibBuilder.loadTexts:pethPdPortTable.setStatus(_A)
_PethPdPortEntry_Object=MibTableRow
pethPdPortEntry=_PethPdPortEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,2,1))
pethPdPortEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:pethPdPortEntry.setStatus(_A)
_PethPdPortIndex_Type=InterfaceIndex
_PethPdPortIndex_Object=MibTableColumn
pethPdPortIndex=_PethPdPortIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,2,1,1),_PethPdPortIndex_Type())
pethPdPortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:pethPdPortIndex.setStatus(_A)
class _PethPdPortAdminEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_PethPdPortAdminEnable_Type.__name__=_C
_PethPdPortAdminEnable_Object=MibTableColumn
pethPdPortAdminEnable=_PethPdPortAdminEnable_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,2,1,2),_PethPdPortAdminEnable_Type())
pethPdPortAdminEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:pethPdPortAdminEnable.setStatus(_A)
_PethMainPseObjects_ObjectIdentity=ObjectIdentity
pethMainPseObjects=_PethMainPseObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,3))
_PethMainPseTable_Object=MibTable
pethMainPseTable=_PethMainPseTable_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,3,1))
if mibBuilder.loadTexts:pethMainPseTable.setStatus(_A)
_PethMainPseEntry_Object=MibTableRow
pethMainPseEntry=_PethMainPseEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,3,1,1))
pethMainPseEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:pethMainPseEntry.setStatus(_A)
class _PethMainPseGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PethMainPseGroupIndex_Type.__name__=_C
_PethMainPseGroupIndex_Object=MibTableColumn
pethMainPseGroupIndex=_PethMainPseGroupIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,3,1,1,1),_PethMainPseGroupIndex_Type())
pethMainPseGroupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:pethMainPseGroupIndex.setStatus(_A)
class _PethMainPsePower_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PethMainPsePower_Type.__name__=_P
_PethMainPsePower_Object=MibTableColumn
pethMainPsePower=_PethMainPsePower_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,3,1,1,2),_PethMainPsePower_Type())
pethMainPsePower.setMaxAccess(_D)
if mibBuilder.loadTexts:pethMainPsePower.setStatus(_A)
if mibBuilder.loadTexts:pethMainPsePower.setUnits('Watts')
class _PethMainPseOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('on',1),('off',2),('faulty',3)))
_PethMainPseOperStatus_Type.__name__=_C
_PethMainPseOperStatus_Object=MibTableColumn
pethMainPseOperStatus=_PethMainPseOperStatus_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,3,1,1,3),_PethMainPseOperStatus_Type())
pethMainPseOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:pethMainPseOperStatus.setStatus(_A)
_PethMainPseConsumptionPower_Type=Gauge32
_PethMainPseConsumptionPower_Object=MibTableColumn
pethMainPseConsumptionPower=_PethMainPseConsumptionPower_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,3,1,1,4),_PethMainPseConsumptionPower_Type())
pethMainPseConsumptionPower.setMaxAccess(_D)
if mibBuilder.loadTexts:pethMainPseConsumptionPower.setStatus(_A)
if mibBuilder.loadTexts:pethMainPseConsumptionPower.setUnits('Watts')
class _PethMainPseUsageThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_PethMainPseUsageThreshold_Type.__name__=_C
_PethMainPseUsageThreshold_Object=MibTableColumn
pethMainPseUsageThreshold=_PethMainPseUsageThreshold_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,3,1,1,7),_PethMainPseUsageThreshold_Type())
pethMainPseUsageThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:pethMainPseUsageThreshold.setStatus(_A)
if mibBuilder.loadTexts:pethMainPseUsageThreshold.setUnits('%')
_PethNotificationControl_ObjectIdentity=ObjectIdentity
pethNotificationControl=_PethNotificationControl_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,4))
_PethNotificationControlTable_Object=MibTable
pethNotificationControlTable=_PethNotificationControlTable_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,4,1))
if mibBuilder.loadTexts:pethNotificationControlTable.setStatus(_A)
_PethNotificationControlEntry_Object=MibTableRow
pethNotificationControlEntry=_PethNotificationControlEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,4,1,1))
pethNotificationControlEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:pethNotificationControlEntry.setStatus(_A)
class _PethNotificationControlGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PethNotificationControlGroupIndex_Type.__name__=_C
_PethNotificationControlGroupIndex_Object=MibTableColumn
pethNotificationControlGroupIndex=_PethNotificationControlGroupIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,4,1,1,1),_PethNotificationControlGroupIndex_Type())
pethNotificationControlGroupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:pethNotificationControlGroupIndex.setStatus(_A)
class _PethNotificationControlEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_PethNotificationControlEnable_Type.__name__=_C
_PethNotificationControlEnable_Object=MibTableColumn
pethNotificationControlEnable=_PethNotificationControlEnable_Object((1,3,6,1,4,1,6486,800,1,2,1,27,999,1,4,1,1,2),_PethNotificationControlEnable_Type())
pethNotificationControlEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:pethNotificationControlEnable.setStatus(_A)
_PethConformance_ObjectIdentity=ObjectIdentity
pethConformance=_PethConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,27,999,2))
_PethCompliances_ObjectIdentity=ObjectIdentity
pethCompliances=_PethCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,27,999,2,1))
_PethGroups_ObjectIdentity=ObjectIdentity
pethGroups=_PethGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,27,999,2,2))
pethPsePortGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,27,999,2,2,1))
pethPsePortGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_J),(_B,_Z),(_B,_K),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:pethPsePortGroup.setStatus(_A)
pethPdPortGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,27,999,2,2,2))
pethPdPortGroup.setObjects((_B,_e))
if mibBuilder.loadTexts:pethPdPortGroup.setStatus(_A)
pethMainPseGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,27,999,2,2,3))
pethMainPseGroup.setObjects(*((_B,_f),(_B,_g),(_B,_G),(_B,_h)))
if mibBuilder.loadTexts:pethMainPseGroup.setStatus(_A)
pethNotificationControlGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,27,999,2,2,4))
pethNotificationControlGroup.setObjects((_B,_i))
if mibBuilder.loadTexts:pethNotificationControlGroup.setStatus(_A)
pethPsePortOnOffNotification=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,27,999,0,1))
pethPsePortOnOffNotification.setObjects((_B,_J))
if mibBuilder.loadTexts:pethPsePortOnOffNotification.setStatus(_A)
pethPsePortPowerMaintenanceStatusNotification=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,27,999,0,2))
pethPsePortPowerMaintenanceStatusNotification.setObjects((_B,_K))
if mibBuilder.loadTexts:pethPsePortPowerMaintenanceStatusNotification.setStatus(_A)
pethMainPowerUsageOnNotification=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,27,999,0,4))
pethMainPowerUsageOnNotification.setObjects((_B,_G))
if mibBuilder.loadTexts:pethMainPowerUsageOnNotification.setStatus(_A)
pethMainPowerUsageOffNotification=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,27,999,0,5))
pethMainPowerUsageOffNotification.setObjects((_B,_G))
if mibBuilder.loadTexts:pethMainPowerUsageOffNotification.setStatus(_A)
pethPsePortNotificationGroup=NotificationGroup((1,3,6,1,4,1,6486,800,1,2,1,27,999,2,1,4))
pethPsePortNotificationGroup.setObjects(*((_B,_j),(_B,_k)))
if mibBuilder.loadTexts:pethPsePortNotificationGroup.setStatus(_A)
pethMainPowerNotificationGroup=NotificationGroup((1,3,6,1,4,1,6486,800,1,2,1,27,999,2,1,5))
pethMainPowerNotificationGroup.setObjects(*((_B,_l),(_B,_m)))
if mibBuilder.loadTexts:pethMainPowerNotificationGroup.setStatus(_A)
pethCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,27,999,2,1,1))
pethCompliance.setObjects(*((_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:pethCompliance.setStatus(_A)
pethPseCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,27,999,2,1,2))
pethPseCompliance.setObjects(*((_B,_L),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:pethPseCompliance.setStatus(_A)
pethPdCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,27,999,2,1,3))
pethPdCompliance.setObjects((_B,_M))
if mibBuilder.loadTexts:pethPdCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'powerEthernetMIB':powerEthernetMIB,'pethNotifications':pethNotifications,_j:pethPsePortOnOffNotification,_k:pethPsePortPowerMaintenanceStatusNotification,_l:pethMainPowerUsageOnNotification,_m:pethMainPowerUsageOffNotification,'pethObjects':pethObjects,'pethPsePortTable':pethPsePortTable,'pethPsePortEntry':pethPsePortEntry,_Q:pethPsePortGroupIndex,_R:pethPsePortIndex,_V:pethPsePortAdminEnable,_W:pethPsePortPowerPairsControlAbility,_Y:pethPsePortPowerPairs,_X:pethPsePortPowerDetectionControl,_J:pethPsePortDetectionStatus,_Z:pethPsePortPowerPriority,_K:pethPsePortPowerMaintenanceStatus,_a:pethPsePortMPSAbsentCounter,_b:pethPsePortOverCurrentCounter,_c:pethPsePortType,_d:pethPsePortPowerClassifications,'pethPdPortTable':pethPdPortTable,'pethPdPortEntry':pethPdPortEntry,_S:pethPdPortIndex,_e:pethPdPortAdminEnable,'pethMainPseObjects':pethMainPseObjects,'pethMainPseTable':pethMainPseTable,'pethMainPseEntry':pethMainPseEntry,_T:pethMainPseGroupIndex,_f:pethMainPsePower,_g:pethMainPseOperStatus,_G:pethMainPseConsumptionPower,_h:pethMainPseUsageThreshold,'pethNotificationControl':pethNotificationControl,'pethNotificationControlTable':pethNotificationControlTable,'pethNotificationControlEntry':pethNotificationControlEntry,_U:pethNotificationControlGroupIndex,_i:pethNotificationControlEnable,'pethConformance':pethConformance,'pethCompliances':pethCompliances,'pethCompliance':pethCompliance,'pethPseCompliance':pethPseCompliance,'pethPdCompliance':pethPdCompliance,'pethPsePortNotificationGroup':pethPsePortNotificationGroup,'pethMainPowerNotificationGroup':pethMainPowerNotificationGroup,'pethGroups':pethGroups,_L:pethPsePortGroup,_M:pethPdPortGroup,_N:pethMainPseGroup,_O:pethNotificationControlGroup})