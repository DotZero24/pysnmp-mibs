_m='pethMainPowerNotificationGroup'
_l='pethMainPseGroup'
_k='pethNotificationControlGroup'
_j='pethPsePortNotificationGroup'
_i='pethPsePortGroup'
_h='pethMainPowerUsageOffNotification'
_g='pethMainPowerUsageOnNotification'
_f='pethPsePortOnOffNotification'
_e='pethNotificationControlEnable'
_d='pethMainPseUsageThreshold'
_c='pethMainPseOperStatus'
_b='pethMainPsePower'
_a='pethPsePortCumulativeEnergy'
_Z='pethPsePortPowerAccuracy'
_Y='pethPsePortActualPower'
_X='pethPsePortPowerClassifications'
_W='pethPsePortType'
_V='pethPsePortShortCounter'
_U='pethPsePortOverLoadCounter'
_T='pethPsePortPowerDeniedCounter'
_S='pethPsePortInvalidSignatureCounter'
_R='pethPsePortMPSAbsentCounter'
_Q='pethPsePortPowerPriority'
_P='pethPsePortPowerPairs'
_O='pethPsePortPowerPairsControlAbility'
_N='pethPsePortAdminEnable'
_M='pethNotificationControlGroupIndex'
_L='pethMainPseGroupIndex'
_K='pethPsePortIndex'
_J='pethPsePortGroupIndex'
_I='Gauge32'
_H='pethPsePortDetectionStatus'
_G='pethMainPseConsumptionPower'
_F='not-accessible'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='POWER-ETHERNET-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_I,_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
powerEthernetMIB=ModuleIdentity((1,3,6,1,2,1,105))
if mibBuilder.loadTexts:powerEthernetMIB.setRevisions(('2003-11-24 00:00',))
_PethNotifications_ObjectIdentity=ObjectIdentity
pethNotifications=_PethNotifications_ObjectIdentity((1,3,6,1,2,1,105,0))
_PethObjects_ObjectIdentity=ObjectIdentity
pethObjects=_PethObjects_ObjectIdentity((1,3,6,1,2,1,105,1))
_PethPsePortTable_Object=MibTable
pethPsePortTable=_PethPsePortTable_Object((1,3,6,1,2,1,105,1,1))
if mibBuilder.loadTexts:pethPsePortTable.setStatus(_A)
_PethPsePortEntry_Object=MibTableRow
pethPsePortEntry=_PethPsePortEntry_Object((1,3,6,1,2,1,105,1,1,1))
pethPsePortEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:pethPsePortEntry.setStatus(_A)
class _PethPsePortGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PethPsePortGroupIndex_Type.__name__=_D
_PethPsePortGroupIndex_Object=MibTableColumn
pethPsePortGroupIndex=_PethPsePortGroupIndex_Object((1,3,6,1,2,1,105,1,1,1,1),_PethPsePortGroupIndex_Type())
pethPsePortGroupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:pethPsePortGroupIndex.setStatus(_A)
class _PethPsePortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PethPsePortIndex_Type.__name__=_D
_PethPsePortIndex_Object=MibTableColumn
pethPsePortIndex=_PethPsePortIndex_Object((1,3,6,1,2,1,105,1,1,1,2),_PethPsePortIndex_Type())
pethPsePortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:pethPsePortIndex.setStatus(_A)
_PethPsePortAdminEnable_Type=TruthValue
_PethPsePortAdminEnable_Object=MibTableColumn
pethPsePortAdminEnable=_PethPsePortAdminEnable_Object((1,3,6,1,2,1,105,1,1,1,3),_PethPsePortAdminEnable_Type())
pethPsePortAdminEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:pethPsePortAdminEnable.setStatus(_A)
_PethPsePortPowerPairsControlAbility_Type=TruthValue
_PethPsePortPowerPairsControlAbility_Object=MibTableColumn
pethPsePortPowerPairsControlAbility=_PethPsePortPowerPairsControlAbility_Object((1,3,6,1,2,1,105,1,1,1,4),_PethPsePortPowerPairsControlAbility_Type())
pethPsePortPowerPairsControlAbility.setMaxAccess(_C)
if mibBuilder.loadTexts:pethPsePortPowerPairsControlAbility.setStatus(_A)
class _PethPsePortPowerPairs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('signal',1),('spare',2)))
_PethPsePortPowerPairs_Type.__name__=_D
_PethPsePortPowerPairs_Object=MibTableColumn
pethPsePortPowerPairs=_PethPsePortPowerPairs_Object((1,3,6,1,2,1,105,1,1,1,5),_PethPsePortPowerPairs_Type())
pethPsePortPowerPairs.setMaxAccess(_E)
if mibBuilder.loadTexts:pethPsePortPowerPairs.setStatus(_A)
class _PethPsePortDetectionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('disabled',1),('searching',2),('deliveringPower',3),('fault',4),('test',5),('otherFault',6)))
_PethPsePortDetectionStatus_Type.__name__=_D
_PethPsePortDetectionStatus_Object=MibTableColumn
pethPsePortDetectionStatus=_PethPsePortDetectionStatus_Object((1,3,6,1,2,1,105,1,1,1,6),_PethPsePortDetectionStatus_Type())
pethPsePortDetectionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pethPsePortDetectionStatus.setStatus(_A)
class _PethPsePortPowerPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('critical',1),('high',2),('low',3)))
_PethPsePortPowerPriority_Type.__name__=_D
_PethPsePortPowerPriority_Object=MibTableColumn
pethPsePortPowerPriority=_PethPsePortPowerPriority_Object((1,3,6,1,2,1,105,1,1,1,7),_PethPsePortPowerPriority_Type())
pethPsePortPowerPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:pethPsePortPowerPriority.setStatus(_A)
_PethPsePortMPSAbsentCounter_Type=Counter32
_PethPsePortMPSAbsentCounter_Object=MibTableColumn
pethPsePortMPSAbsentCounter=_PethPsePortMPSAbsentCounter_Object((1,3,6,1,2,1,105,1,1,1,8),_PethPsePortMPSAbsentCounter_Type())
pethPsePortMPSAbsentCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:pethPsePortMPSAbsentCounter.setStatus(_A)
_PethPsePortType_Type=SnmpAdminString
_PethPsePortType_Object=MibTableColumn
pethPsePortType=_PethPsePortType_Object((1,3,6,1,2,1,105,1,1,1,9),_PethPsePortType_Type())
pethPsePortType.setMaxAccess(_E)
if mibBuilder.loadTexts:pethPsePortType.setStatus(_A)
class _PethPsePortPowerClassifications_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('class0',1),('class1',2),('class2',3),('class3',4),('class4',5)))
_PethPsePortPowerClassifications_Type.__name__=_D
_PethPsePortPowerClassifications_Object=MibTableColumn
pethPsePortPowerClassifications=_PethPsePortPowerClassifications_Object((1,3,6,1,2,1,105,1,1,1,10),_PethPsePortPowerClassifications_Type())
pethPsePortPowerClassifications.setMaxAccess(_C)
if mibBuilder.loadTexts:pethPsePortPowerClassifications.setStatus(_A)
_PethPsePortInvalidSignatureCounter_Type=Counter32
_PethPsePortInvalidSignatureCounter_Object=MibTableColumn
pethPsePortInvalidSignatureCounter=_PethPsePortInvalidSignatureCounter_Object((1,3,6,1,2,1,105,1,1,1,11),_PethPsePortInvalidSignatureCounter_Type())
pethPsePortInvalidSignatureCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:pethPsePortInvalidSignatureCounter.setStatus(_A)
_PethPsePortPowerDeniedCounter_Type=Counter32
_PethPsePortPowerDeniedCounter_Object=MibTableColumn
pethPsePortPowerDeniedCounter=_PethPsePortPowerDeniedCounter_Object((1,3,6,1,2,1,105,1,1,1,12),_PethPsePortPowerDeniedCounter_Type())
pethPsePortPowerDeniedCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:pethPsePortPowerDeniedCounter.setStatus(_A)
_PethPsePortOverLoadCounter_Type=Counter32
_PethPsePortOverLoadCounter_Object=MibTableColumn
pethPsePortOverLoadCounter=_PethPsePortOverLoadCounter_Object((1,3,6,1,2,1,105,1,1,1,13),_PethPsePortOverLoadCounter_Type())
pethPsePortOverLoadCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:pethPsePortOverLoadCounter.setStatus(_A)
_PethPsePortShortCounter_Type=Counter32
_PethPsePortShortCounter_Object=MibTableColumn
pethPsePortShortCounter=_PethPsePortShortCounter_Object((1,3,6,1,2,1,105,1,1,1,14),_PethPsePortShortCounter_Type())
pethPsePortShortCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:pethPsePortShortCounter.setStatus(_A)
_PethPsePortActualPower_Type=Integer32
_PethPsePortActualPower_Object=MibTableColumn
pethPsePortActualPower=_PethPsePortActualPower_Object((1,3,6,1,2,1,105,1,1,1,15),_PethPsePortActualPower_Type())
pethPsePortActualPower.setMaxAccess(_C)
if mibBuilder.loadTexts:pethPsePortActualPower.setStatus(_A)
_PethPsePortPowerAccuracy_Type=Integer32
_PethPsePortPowerAccuracy_Object=MibTableColumn
pethPsePortPowerAccuracy=_PethPsePortPowerAccuracy_Object((1,3,6,1,2,1,105,1,1,1,16),_PethPsePortPowerAccuracy_Type())
pethPsePortPowerAccuracy.setMaxAccess(_C)
if mibBuilder.loadTexts:pethPsePortPowerAccuracy.setStatus(_A)
_PethPsePortCumulativeEnergy_Type=Counter32
_PethPsePortCumulativeEnergy_Object=MibTableColumn
pethPsePortCumulativeEnergy=_PethPsePortCumulativeEnergy_Object((1,3,6,1,2,1,105,1,1,1,17),_PethPsePortCumulativeEnergy_Type())
pethPsePortCumulativeEnergy.setMaxAccess(_C)
if mibBuilder.loadTexts:pethPsePortCumulativeEnergy.setStatus(_A)
_PethMainPseObjects_ObjectIdentity=ObjectIdentity
pethMainPseObjects=_PethMainPseObjects_ObjectIdentity((1,3,6,1,2,1,105,1,3))
_PethMainPseTable_Object=MibTable
pethMainPseTable=_PethMainPseTable_Object((1,3,6,1,2,1,105,1,3,1))
if mibBuilder.loadTexts:pethMainPseTable.setStatus(_A)
_PethMainPseEntry_Object=MibTableRow
pethMainPseEntry=_PethMainPseEntry_Object((1,3,6,1,2,1,105,1,3,1,1))
pethMainPseEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:pethMainPseEntry.setStatus(_A)
class _PethMainPseGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PethMainPseGroupIndex_Type.__name__=_D
_PethMainPseGroupIndex_Object=MibTableColumn
pethMainPseGroupIndex=_PethMainPseGroupIndex_Object((1,3,6,1,2,1,105,1,3,1,1,1),_PethMainPseGroupIndex_Type())
pethMainPseGroupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:pethMainPseGroupIndex.setStatus(_A)
class _PethMainPsePower_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_PethMainPsePower_Type.__name__=_I
_PethMainPsePower_Object=MibTableColumn
pethMainPsePower=_PethMainPsePower_Object((1,3,6,1,2,1,105,1,3,1,1,2),_PethMainPsePower_Type())
pethMainPsePower.setMaxAccess(_C)
if mibBuilder.loadTexts:pethMainPsePower.setStatus(_A)
if mibBuilder.loadTexts:pethMainPsePower.setUnits('Watts')
class _PethMainPseOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('on',1),('off',2),('faulty',3)))
_PethMainPseOperStatus_Type.__name__=_D
_PethMainPseOperStatus_Object=MibTableColumn
pethMainPseOperStatus=_PethMainPseOperStatus_Object((1,3,6,1,2,1,105,1,3,1,1,3),_PethMainPseOperStatus_Type())
pethMainPseOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:pethMainPseOperStatus.setStatus(_A)
_PethMainPseConsumptionPower_Type=Gauge32
_PethMainPseConsumptionPower_Object=MibTableColumn
pethMainPseConsumptionPower=_PethMainPseConsumptionPower_Object((1,3,6,1,2,1,105,1,3,1,1,4),_PethMainPseConsumptionPower_Type())
pethMainPseConsumptionPower.setMaxAccess(_C)
if mibBuilder.loadTexts:pethMainPseConsumptionPower.setStatus(_A)
if mibBuilder.loadTexts:pethMainPseConsumptionPower.setUnits('Watts')
class _PethMainPseUsageThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_PethMainPseUsageThreshold_Type.__name__=_D
_PethMainPseUsageThreshold_Object=MibTableColumn
pethMainPseUsageThreshold=_PethMainPseUsageThreshold_Object((1,3,6,1,2,1,105,1,3,1,1,5),_PethMainPseUsageThreshold_Type())
pethMainPseUsageThreshold.setMaxAccess(_E)
if mibBuilder.loadTexts:pethMainPseUsageThreshold.setStatus(_A)
if mibBuilder.loadTexts:pethMainPseUsageThreshold.setUnits('%')
_PethNotificationControl_ObjectIdentity=ObjectIdentity
pethNotificationControl=_PethNotificationControl_ObjectIdentity((1,3,6,1,2,1,105,1,4))
_PethNotificationControlTable_Object=MibTable
pethNotificationControlTable=_PethNotificationControlTable_Object((1,3,6,1,2,1,105,1,4,1))
if mibBuilder.loadTexts:pethNotificationControlTable.setStatus(_A)
_PethNotificationControlEntry_Object=MibTableRow
pethNotificationControlEntry=_PethNotificationControlEntry_Object((1,3,6,1,2,1,105,1,4,1,1))
pethNotificationControlEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:pethNotificationControlEntry.setStatus(_A)
class _PethNotificationControlGroupIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PethNotificationControlGroupIndex_Type.__name__=_D
_PethNotificationControlGroupIndex_Object=MibTableColumn
pethNotificationControlGroupIndex=_PethNotificationControlGroupIndex_Object((1,3,6,1,2,1,105,1,4,1,1,1),_PethNotificationControlGroupIndex_Type())
pethNotificationControlGroupIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:pethNotificationControlGroupIndex.setStatus(_A)
_PethNotificationControlEnable_Type=TruthValue
_PethNotificationControlEnable_Object=MibTableColumn
pethNotificationControlEnable=_PethNotificationControlEnable_Object((1,3,6,1,2,1,105,1,4,1,1,2),_PethNotificationControlEnable_Type())
pethNotificationControlEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:pethNotificationControlEnable.setStatus(_A)
_PethConformance_ObjectIdentity=ObjectIdentity
pethConformance=_PethConformance_ObjectIdentity((1,3,6,1,2,1,105,2))
_PethCompliances_ObjectIdentity=ObjectIdentity
pethCompliances=_PethCompliances_ObjectIdentity((1,3,6,1,2,1,105,2,1))
_PethGroups_ObjectIdentity=ObjectIdentity
pethGroups=_PethGroups_ObjectIdentity((1,3,6,1,2,1,105,2,2))
pethPsePortGroup=ObjectGroup((1,3,6,1,2,1,105,2,2,1))
pethPsePortGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_H),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:pethPsePortGroup.setStatus(_A)
pethMainPseGroup=ObjectGroup((1,3,6,1,2,1,105,2,2,2))
pethMainPseGroup.setObjects(*((_B,_b),(_B,_c),(_B,_G),(_B,_d)))
if mibBuilder.loadTexts:pethMainPseGroup.setStatus(_A)
pethNotificationControlGroup=ObjectGroup((1,3,6,1,2,1,105,2,2,3))
pethNotificationControlGroup.setObjects((_B,_e))
if mibBuilder.loadTexts:pethNotificationControlGroup.setStatus(_A)
pethPsePortOnOffNotification=NotificationType((1,3,6,1,2,1,105,0,1))
pethPsePortOnOffNotification.setObjects((_B,_H))
if mibBuilder.loadTexts:pethPsePortOnOffNotification.setStatus(_A)
pethMainPowerUsageOnNotification=NotificationType((1,3,6,1,2,1,105,0,2))
pethMainPowerUsageOnNotification.setObjects((_B,_G))
if mibBuilder.loadTexts:pethMainPowerUsageOnNotification.setStatus(_A)
pethMainPowerUsageOffNotification=NotificationType((1,3,6,1,2,1,105,0,3))
pethMainPowerUsageOffNotification.setObjects((_B,_G))
if mibBuilder.loadTexts:pethMainPowerUsageOffNotification.setStatus(_A)
pethPsePortNotificationGroup=NotificationGroup((1,3,6,1,2,1,105,2,2,4))
pethPsePortNotificationGroup.setObjects((_B,_f))
if mibBuilder.loadTexts:pethPsePortNotificationGroup.setStatus(_A)
pethMainPowerNotificationGroup=NotificationGroup((1,3,6,1,2,1,105,2,2,5))
pethMainPowerNotificationGroup.setObjects(*((_B,_g),(_B,_h)))
if mibBuilder.loadTexts:pethMainPowerNotificationGroup.setStatus(_A)
pethCompliance=ModuleCompliance((1,3,6,1,2,1,105,2,1,1))
pethCompliance.setObjects(*((_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m)))
if mibBuilder.loadTexts:pethCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'powerEthernetMIB':powerEthernetMIB,'pethNotifications':pethNotifications,_f:pethPsePortOnOffNotification,_g:pethMainPowerUsageOnNotification,_h:pethMainPowerUsageOffNotification,'pethObjects':pethObjects,'pethPsePortTable':pethPsePortTable,'pethPsePortEntry':pethPsePortEntry,_J:pethPsePortGroupIndex,_K:pethPsePortIndex,_N:pethPsePortAdminEnable,_O:pethPsePortPowerPairsControlAbility,_P:pethPsePortPowerPairs,_H:pethPsePortDetectionStatus,_Q:pethPsePortPowerPriority,_R:pethPsePortMPSAbsentCounter,_W:pethPsePortType,_X:pethPsePortPowerClassifications,_S:pethPsePortInvalidSignatureCounter,_T:pethPsePortPowerDeniedCounter,_U:pethPsePortOverLoadCounter,_V:pethPsePortShortCounter,_Y:pethPsePortActualPower,_Z:pethPsePortPowerAccuracy,_a:pethPsePortCumulativeEnergy,'pethMainPseObjects':pethMainPseObjects,'pethMainPseTable':pethMainPseTable,'pethMainPseEntry':pethMainPseEntry,_L:pethMainPseGroupIndex,_b:pethMainPsePower,_c:pethMainPseOperStatus,_G:pethMainPseConsumptionPower,_d:pethMainPseUsageThreshold,'pethNotificationControl':pethNotificationControl,'pethNotificationControlTable':pethNotificationControlTable,'pethNotificationControlEntry':pethNotificationControlEntry,_M:pethNotificationControlGroupIndex,_e:pethNotificationControlEnable,'pethConformance':pethConformance,'pethCompliances':pethCompliances,'pethCompliance':pethCompliance,'pethGroups':pethGroups,_i:pethPsePortGroup,_l:pethMainPseGroup,_k:pethNotificationControlGroup,_j:pethPsePortNotificationGroup,_m:pethMainPowerNotificationGroup})