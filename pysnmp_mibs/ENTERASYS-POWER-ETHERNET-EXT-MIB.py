_t='etsysPsePortPowerManagementGroupRev2'
_s='etsysPsePortPowerManagementGroup'
_r='etsysPsePowerSupplyModuleStatusChange'
_q='etsysPseChassisPowerNonRedundant'
_p='etsysPseChassisPowerRedundant'
_o='etsysPsePortDetectionStatus'
_n='etsysPsePortCapabilitySelect'
_m='etsysPsePortCapability'
_l='deprecated'
_k='etsysPseModulePowerUsage'
_j='etsysPseModulePowerClassBudget'
_i='etsysPseModulePowerMode'
_h='etsysPseChassisPowerRedundancy'
_g='etsysPseChassisPowerAssigned'
_f='etsysPseChassisPowerConsumable'
_e='etsysPseChassisPowerAvailable'
_d='etsysPseSlotPowerAssigned'
_c='etsysPseSlotPowerMaximum'
_b='etsysPseChassisPowerAvailableMaximum'
_a='etsysPseChassisPowerSnmpNotification'
_Z='etsysPseChassisPowerAllocationMode'
_Y='etsysPsePortPowerManagementEntry'
_X='etsysPseModulePowerManagementEntry'
_W='ieee8023at'
_V='ieee8023af'
_U='milliwatts'
_T='etsysPsePowerSupplyModuleNumber'
_S='entPhysicalIndex'
_R='ENTITY-MIB'
_Q='etsysPseModulePowerManagementGroup'
_P='etsysPsePortPDType'
_O='etsysPsePortPowerUsage'
_N='etsysPsePortPowerLimit'
_M='etsysPsePowerSupplyModuleStatus'
_L='Unsigned32'
_K='Bits'
_J='etsysPsePowerNotificationGroup'
_I='etsysPseChassisPowerStatusGroup'
_H='etsysPsePowerAllocationControlGroup'
_G='etsysPseChassisPowerDetected'
_F='Watts'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='current'
_A='ENTERASYS-POWER-ETHERNET-EXT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
entPhysicalIndex,=mibBuilder.importSymbols(_R,_S)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
pethMainPseEntry,pethPsePortEntry=mibBuilder.importSymbols('POWER-ETHERNET-MIB','pethMainPseEntry','pethPsePortEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_K,_K,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
etsysPowerEthernetMibExtMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,50))
if mibBuilder.loadTexts:etsysPowerEthernetMibExtMIB.setRevisions(('2009-08-27 20:31','2005-01-10 16:30','2004-08-17 22:27'))
_EtsysPowerEthernetObjects_ObjectIdentity=ObjectIdentity
etsysPowerEthernetObjects=_EtsysPowerEthernetObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,50,1))
_EtsysPsePowerNotification_ObjectIdentity=ObjectIdentity
etsysPsePowerNotification=_EtsysPsePowerNotification_ObjectIdentity((1,3,6,1,4,1,5624,1,2,50,1,0))
_EtsysPseChassisPowerAllocation_ObjectIdentity=ObjectIdentity
etsysPseChassisPowerAllocation=_EtsysPseChassisPowerAllocation_ObjectIdentity((1,3,6,1,4,1,5624,1,2,50,1,1))
class _EtsysPseChassisPowerAllocationMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),('manual',2)))
_EtsysPseChassisPowerAllocationMode_Type.__name__=_D
_EtsysPseChassisPowerAllocationMode_Object=MibScalar
etsysPseChassisPowerAllocationMode=_EtsysPseChassisPowerAllocationMode_Object((1,3,6,1,4,1,5624,1,2,50,1,1,1),_EtsysPseChassisPowerAllocationMode_Type())
etsysPseChassisPowerAllocationMode.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysPseChassisPowerAllocationMode.setStatus(_B)
_EtsysPseChassisPowerSnmpNotification_Type=EnabledStatus
_EtsysPseChassisPowerSnmpNotification_Object=MibScalar
etsysPseChassisPowerSnmpNotification=_EtsysPseChassisPowerSnmpNotification_Object((1,3,6,1,4,1,5624,1,2,50,1,1,2),_EtsysPseChassisPowerSnmpNotification_Type())
etsysPseChassisPowerSnmpNotification.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysPseChassisPowerSnmpNotification.setStatus(_B)
class _EtsysPseChassisPowerAvailableMaximum_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_EtsysPseChassisPowerAvailableMaximum_Type.__name__=_L
_EtsysPseChassisPowerAvailableMaximum_Object=MibScalar
etsysPseChassisPowerAvailableMaximum=_EtsysPseChassisPowerAvailableMaximum_Object((1,3,6,1,4,1,5624,1,2,50,1,1,3),_EtsysPseChassisPowerAvailableMaximum_Type())
etsysPseChassisPowerAvailableMaximum.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysPseChassisPowerAvailableMaximum.setStatus(_B)
if mibBuilder.loadTexts:etsysPseChassisPowerAvailableMaximum.setUnits('percent')
_EtsysPseSlotPowerAllocation_ObjectIdentity=ObjectIdentity
etsysPseSlotPowerAllocation=_EtsysPseSlotPowerAllocation_ObjectIdentity((1,3,6,1,4,1,5624,1,2,50,1,2))
_EtsysPseSlotPowerAllocationTable_Object=MibTable
etsysPseSlotPowerAllocationTable=_EtsysPseSlotPowerAllocationTable_Object((1,3,6,1,4,1,5624,1,2,50,1,2,1))
if mibBuilder.loadTexts:etsysPseSlotPowerAllocationTable.setStatus(_B)
_EtsysPseSlotPowerAllocationEntry_Object=MibTableRow
etsysPseSlotPowerAllocationEntry=_EtsysPseSlotPowerAllocationEntry_Object((1,3,6,1,4,1,5624,1,2,50,1,2,1,1))
etsysPseSlotPowerAllocationEntry.setIndexNames((0,_R,_S))
if mibBuilder.loadTexts:etsysPseSlotPowerAllocationEntry.setStatus(_B)
_EtsysPseSlotPowerMaximum_Type=Unsigned32
_EtsysPseSlotPowerMaximum_Object=MibTableColumn
etsysPseSlotPowerMaximum=_EtsysPseSlotPowerMaximum_Object((1,3,6,1,4,1,5624,1,2,50,1,2,1,1,1),_EtsysPseSlotPowerMaximum_Type())
etsysPseSlotPowerMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPseSlotPowerMaximum.setStatus(_B)
if mibBuilder.loadTexts:etsysPseSlotPowerMaximum.setUnits(_F)
class _EtsysPseSlotPowerAssigned_Type(Unsigned32):defaultValue=0
_EtsysPseSlotPowerAssigned_Type.__name__=_L
_EtsysPseSlotPowerAssigned_Object=MibTableColumn
etsysPseSlotPowerAssigned=_EtsysPseSlotPowerAssigned_Object((1,3,6,1,4,1,5624,1,2,50,1,2,1,1,2),_EtsysPseSlotPowerAssigned_Type())
etsysPseSlotPowerAssigned.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysPseSlotPowerAssigned.setStatus(_B)
if mibBuilder.loadTexts:etsysPseSlotPowerAssigned.setUnits(_F)
_EtsysPseChassisPowerStatus_ObjectIdentity=ObjectIdentity
etsysPseChassisPowerStatus=_EtsysPseChassisPowerStatus_ObjectIdentity((1,3,6,1,4,1,5624,1,2,50,1,3))
_EtsysPseChassisPowerDetected_Type=Gauge32
_EtsysPseChassisPowerDetected_Object=MibScalar
etsysPseChassisPowerDetected=_EtsysPseChassisPowerDetected_Object((1,3,6,1,4,1,5624,1,2,50,1,3,1),_EtsysPseChassisPowerDetected_Type())
etsysPseChassisPowerDetected.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPseChassisPowerDetected.setStatus(_B)
if mibBuilder.loadTexts:etsysPseChassisPowerDetected.setUnits(_F)
_EtsysPseChassisPowerAvailable_Type=Gauge32
_EtsysPseChassisPowerAvailable_Object=MibScalar
etsysPseChassisPowerAvailable=_EtsysPseChassisPowerAvailable_Object((1,3,6,1,4,1,5624,1,2,50,1,3,2),_EtsysPseChassisPowerAvailable_Type())
etsysPseChassisPowerAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPseChassisPowerAvailable.setStatus(_B)
if mibBuilder.loadTexts:etsysPseChassisPowerAvailable.setUnits(_F)
_EtsysPseChassisPowerConsumable_Type=Gauge32
_EtsysPseChassisPowerConsumable_Object=MibScalar
etsysPseChassisPowerConsumable=_EtsysPseChassisPowerConsumable_Object((1,3,6,1,4,1,5624,1,2,50,1,3,3),_EtsysPseChassisPowerConsumable_Type())
etsysPseChassisPowerConsumable.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPseChassisPowerConsumable.setStatus(_B)
if mibBuilder.loadTexts:etsysPseChassisPowerConsumable.setUnits(_F)
_EtsysPseChassisPowerAssigned_Type=Unsigned32
_EtsysPseChassisPowerAssigned_Object=MibScalar
etsysPseChassisPowerAssigned=_EtsysPseChassisPowerAssigned_Object((1,3,6,1,4,1,5624,1,2,50,1,3,4),_EtsysPseChassisPowerAssigned_Type())
etsysPseChassisPowerAssigned.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPseChassisPowerAssigned.setStatus(_B)
if mibBuilder.loadTexts:etsysPseChassisPowerAssigned.setUnits(_F)
class _EtsysPseChassisPowerRedundancy_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('redundant',1),('notRedundant',2),('notSupported',3)))
_EtsysPseChassisPowerRedundancy_Type.__name__=_D
_EtsysPseChassisPowerRedundancy_Object=MibScalar
etsysPseChassisPowerRedundancy=_EtsysPseChassisPowerRedundancy_Object((1,3,6,1,4,1,5624,1,2,50,1,3,5),_EtsysPseChassisPowerRedundancy_Type())
etsysPseChassisPowerRedundancy.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPseChassisPowerRedundancy.setStatus(_B)
_EtsysPsePowerSupplyStatusTable_Object=MibTable
etsysPsePowerSupplyStatusTable=_EtsysPsePowerSupplyStatusTable_Object((1,3,6,1,4,1,5624,1,2,50,1,3,6))
if mibBuilder.loadTexts:etsysPsePowerSupplyStatusTable.setStatus(_B)
_EtsysPsePowerSupplyStatusEntry_Object=MibTableRow
etsysPsePowerSupplyStatusEntry=_EtsysPsePowerSupplyStatusEntry_Object((1,3,6,1,4,1,5624,1,2,50,1,3,6,1))
etsysPsePowerSupplyStatusEntry.setIndexNames((0,_A,_T))
if mibBuilder.loadTexts:etsysPsePowerSupplyStatusEntry.setStatus(_B)
_EtsysPsePowerSupplyModuleNumber_Type=Unsigned32
_EtsysPsePowerSupplyModuleNumber_Object=MibTableColumn
etsysPsePowerSupplyModuleNumber=_EtsysPsePowerSupplyModuleNumber_Object((1,3,6,1,4,1,5624,1,2,50,1,3,6,1,1),_EtsysPsePowerSupplyModuleNumber_Type())
etsysPsePowerSupplyModuleNumber.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:etsysPsePowerSupplyModuleNumber.setStatus(_B)
class _EtsysPsePowerSupplyModuleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('infoNotAvailable',1),('notInstalled',2),('installedAndOperating',3),('installedAndNotOperating',4)))
_EtsysPsePowerSupplyModuleStatus_Type.__name__=_D
_EtsysPsePowerSupplyModuleStatus_Object=MibTableColumn
etsysPsePowerSupplyModuleStatus=_EtsysPsePowerSupplyModuleStatus_Object((1,3,6,1,4,1,5624,1,2,50,1,3,6,1,2),_EtsysPsePowerSupplyModuleStatus_Type())
etsysPsePowerSupplyModuleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPsePowerSupplyModuleStatus.setStatus(_B)
_EtsysPseSlotPowerManagement_ObjectIdentity=ObjectIdentity
etsysPseSlotPowerManagement=_EtsysPseSlotPowerManagement_ObjectIdentity((1,3,6,1,4,1,5624,1,2,50,1,4))
_EtsysPseModulePowerManagementTable_Object=MibTable
etsysPseModulePowerManagementTable=_EtsysPseModulePowerManagementTable_Object((1,3,6,1,4,1,5624,1,2,50,1,4,1))
if mibBuilder.loadTexts:etsysPseModulePowerManagementTable.setStatus(_B)
_EtsysPseModulePowerManagementEntry_Object=MibTableRow
etsysPseModulePowerManagementEntry=_EtsysPseModulePowerManagementEntry_Object((1,3,6,1,4,1,5624,1,2,50,1,4,1,1))
if mibBuilder.loadTexts:etsysPseModulePowerManagementEntry.setStatus(_B)
class _EtsysPseModulePowerMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('realtime',1),('class',2)))
_EtsysPseModulePowerMode_Type.__name__=_D
_EtsysPseModulePowerMode_Object=MibTableColumn
etsysPseModulePowerMode=_EtsysPseModulePowerMode_Object((1,3,6,1,4,1,5624,1,2,50,1,4,1,1,1),_EtsysPseModulePowerMode_Type())
etsysPseModulePowerMode.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysPseModulePowerMode.setStatus(_B)
_EtsysPseModulePowerClassBudget_Type=Gauge32
_EtsysPseModulePowerClassBudget_Object=MibTableColumn
etsysPseModulePowerClassBudget=_EtsysPseModulePowerClassBudget_Object((1,3,6,1,4,1,5624,1,2,50,1,4,1,1,2),_EtsysPseModulePowerClassBudget_Type())
etsysPseModulePowerClassBudget.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPseModulePowerClassBudget.setStatus(_B)
if mibBuilder.loadTexts:etsysPseModulePowerClassBudget.setUnits(_F)
class _EtsysPseModulePowerUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_EtsysPseModulePowerUsage_Type.__name__=_D
_EtsysPseModulePowerUsage_Object=MibTableColumn
etsysPseModulePowerUsage=_EtsysPseModulePowerUsage_Object((1,3,6,1,4,1,5624,1,2,50,1,4,1,1,3),_EtsysPseModulePowerUsage_Type())
etsysPseModulePowerUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPseModulePowerUsage.setStatus(_B)
if mibBuilder.loadTexts:etsysPseModulePowerUsage.setUnits('%')
_EtsysPsePortPowerManagement_ObjectIdentity=ObjectIdentity
etsysPsePortPowerManagement=_EtsysPsePortPowerManagement_ObjectIdentity((1,3,6,1,4,1,5624,1,2,50,1,5))
_EtsysPsePortPowerManagementTable_Object=MibTable
etsysPsePortPowerManagementTable=_EtsysPsePortPowerManagementTable_Object((1,3,6,1,4,1,5624,1,2,50,1,5,1))
if mibBuilder.loadTexts:etsysPsePortPowerManagementTable.setStatus(_B)
_EtsysPsePortPowerManagementEntry_Object=MibTableRow
etsysPsePortPowerManagementEntry=_EtsysPsePortPowerManagementEntry_Object((1,3,6,1,4,1,5624,1,2,50,1,5,1,1))
if mibBuilder.loadTexts:etsysPsePortPowerManagementEntry.setStatus(_B)
class _EtsysPsePortPowerLimit_Type(Integer32):defaultValue=15400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,34000))
_EtsysPsePortPowerLimit_Type.__name__=_D
_EtsysPsePortPowerLimit_Object=MibTableColumn
etsysPsePortPowerLimit=_EtsysPsePortPowerLimit_Object((1,3,6,1,4,1,5624,1,2,50,1,5,1,1,1),_EtsysPsePortPowerLimit_Type())
etsysPsePortPowerLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysPsePortPowerLimit.setStatus(_B)
if mibBuilder.loadTexts:etsysPsePortPowerLimit.setUnits(_U)
_EtsysPsePortPowerUsage_Type=Gauge32
_EtsysPsePortPowerUsage_Object=MibTableColumn
etsysPsePortPowerUsage=_EtsysPsePortPowerUsage_Object((1,3,6,1,4,1,5624,1,2,50,1,5,1,1,2),_EtsysPsePortPowerUsage_Type())
etsysPsePortPowerUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPsePortPowerUsage.setStatus(_B)
if mibBuilder.loadTexts:etsysPsePortPowerUsage.setUnits(_U)
class _EtsysPsePortPDType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('legacy',1),(_V,2),('other',3),('ieee8023',4),(_W,5)))
_EtsysPsePortPDType_Type.__name__=_D
_EtsysPsePortPDType_Object=MibTableColumn
etsysPsePortPDType=_EtsysPsePortPDType_Object((1,3,6,1,4,1,5624,1,2,50,1,5,1,1,3),_EtsysPsePortPDType_Type())
etsysPsePortPDType.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPsePortPDType.setStatus(_B)
class _EtsysPsePortCapability_Type(Bits):namedValues=NamedValues(*(('other',0),('ieee8023afCapable',1),('ieee8023atCapable',2)))
_EtsysPsePortCapability_Type.__name__=_K
_EtsysPsePortCapability_Object=MibTableColumn
etsysPsePortCapability=_EtsysPsePortCapability_Object((1,3,6,1,4,1,5624,1,2,50,1,5,1,1,4),_EtsysPsePortCapability_Type())
etsysPsePortCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPsePortCapability.setStatus(_B)
class _EtsysPsePortCapabilitySelect_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_V,1),(_W,2)))
_EtsysPsePortCapabilitySelect_Type.__name__=_D
_EtsysPsePortCapabilitySelect_Object=MibTableColumn
etsysPsePortCapabilitySelect=_EtsysPsePortCapabilitySelect_Object((1,3,6,1,4,1,5624,1,2,50,1,5,1,1,5),_EtsysPsePortCapabilitySelect_Type())
etsysPsePortCapabilitySelect.setMaxAccess(_E)
if mibBuilder.loadTexts:etsysPsePortCapabilitySelect.setStatus(_B)
class _EtsysPsePortDetectionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('disabled',1),('searching',2),('deliveringPower',3),('fault',4),('test',5),('otherFault',6),('requestingPower',7)))
_EtsysPsePortDetectionStatus_Type.__name__=_D
_EtsysPsePortDetectionStatus_Object=MibTableColumn
etsysPsePortDetectionStatus=_EtsysPsePortDetectionStatus_Object((1,3,6,1,4,1,5624,1,2,50,1,5,1,1,6),_EtsysPsePortDetectionStatus_Type())
etsysPsePortDetectionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysPsePortDetectionStatus.setStatus(_B)
_EtsysPsePowerAllocationConformance_ObjectIdentity=ObjectIdentity
etsysPsePowerAllocationConformance=_EtsysPsePowerAllocationConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,50,2))
_EtsysPsePowerAllocationGroups_ObjectIdentity=ObjectIdentity
etsysPsePowerAllocationGroups=_EtsysPsePowerAllocationGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,50,2,1))
_EtsysPsePowerAllocationCompliances_ObjectIdentity=ObjectIdentity
etsysPsePowerAllocationCompliances=_EtsysPsePowerAllocationCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,50,2,2))
pethMainPseEntry.registerAugmentions((_A,_X))
etsysPseModulePowerManagementEntry.setIndexNames(*pethMainPseEntry.getIndexNames())
pethPsePortEntry.registerAugmentions((_A,_Y))
etsysPsePortPowerManagementEntry.setIndexNames(*pethPsePortEntry.getIndexNames())
etsysPsePowerAllocationControlGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,50,2,1,1))
etsysPsePowerAllocationControlGroup.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d)))
if mibBuilder.loadTexts:etsysPsePowerAllocationControlGroup.setStatus(_B)
etsysPseChassisPowerStatusGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,50,2,1,2))
etsysPseChassisPowerStatusGroup.setObjects(*((_A,_G),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_M)))
if mibBuilder.loadTexts:etsysPseChassisPowerStatusGroup.setStatus(_B)
etsysPseModulePowerManagementGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,50,2,1,4))
etsysPseModulePowerManagementGroup.setObjects(*((_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:etsysPseModulePowerManagementGroup.setStatus(_B)
etsysPsePortPowerManagementGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,50,2,1,5))
etsysPsePortPowerManagementGroup.setObjects(*((_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:etsysPsePortPowerManagementGroup.setStatus(_l)
etsysPsePortPowerManagementGroupRev2=ObjectGroup((1,3,6,1,4,1,5624,1,2,50,2,1,6))
etsysPsePortPowerManagementGroupRev2.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_m),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:etsysPsePortPowerManagementGroupRev2.setStatus(_B)
etsysPseChassisPowerRedundant=NotificationType((1,3,6,1,4,1,5624,1,2,50,1,0,1))
etsysPseChassisPowerRedundant.setObjects((_A,_G))
if mibBuilder.loadTexts:etsysPseChassisPowerRedundant.setStatus(_B)
etsysPseChassisPowerNonRedundant=NotificationType((1,3,6,1,4,1,5624,1,2,50,1,0,2))
etsysPseChassisPowerNonRedundant.setObjects((_A,_G))
if mibBuilder.loadTexts:etsysPseChassisPowerNonRedundant.setStatus(_B)
etsysPsePowerSupplyModuleStatusChange=NotificationType((1,3,6,1,4,1,5624,1,2,50,1,0,3))
etsysPsePowerSupplyModuleStatusChange.setObjects((_A,_M))
if mibBuilder.loadTexts:etsysPsePowerSupplyModuleStatusChange.setStatus(_B)
etsysPsePowerNotificationGroup=NotificationGroup((1,3,6,1,4,1,5624,1,2,50,2,1,3))
etsysPsePowerNotificationGroup.setObjects(*((_A,_p),(_A,_q),(_A,_r)))
if mibBuilder.loadTexts:etsysPsePowerNotificationGroup.setStatus(_B)
etsysPsePowerAllocationCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,50,2,2,1))
etsysPsePowerAllocationCompliance.setObjects(*((_A,_H),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:etsysPsePowerAllocationCompliance.setStatus(_B)
etsysPsePowerAllocationCompliance2=ModuleCompliance((1,3,6,1,4,1,5624,1,2,50,2,2,2))
etsysPsePowerAllocationCompliance2.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_Q),(_A,_s)))
if mibBuilder.loadTexts:etsysPsePowerAllocationCompliance2.setStatus(_l)
etsysPsePowerAllocationCompliance2Rev2=ModuleCompliance((1,3,6,1,4,1,5624,1,2,50,2,2,3))
etsysPsePowerAllocationCompliance2Rev2.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_Q),(_A,_t)))
if mibBuilder.loadTexts:etsysPsePowerAllocationCompliance2Rev2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'etsysPowerEthernetMibExtMIB':etsysPowerEthernetMibExtMIB,'etsysPowerEthernetObjects':etsysPowerEthernetObjects,'etsysPsePowerNotification':etsysPsePowerNotification,_p:etsysPseChassisPowerRedundant,_q:etsysPseChassisPowerNonRedundant,_r:etsysPsePowerSupplyModuleStatusChange,'etsysPseChassisPowerAllocation':etsysPseChassisPowerAllocation,_Z:etsysPseChassisPowerAllocationMode,_a:etsysPseChassisPowerSnmpNotification,_b:etsysPseChassisPowerAvailableMaximum,'etsysPseSlotPowerAllocation':etsysPseSlotPowerAllocation,'etsysPseSlotPowerAllocationTable':etsysPseSlotPowerAllocationTable,'etsysPseSlotPowerAllocationEntry':etsysPseSlotPowerAllocationEntry,_c:etsysPseSlotPowerMaximum,_d:etsysPseSlotPowerAssigned,'etsysPseChassisPowerStatus':etsysPseChassisPowerStatus,_G:etsysPseChassisPowerDetected,_e:etsysPseChassisPowerAvailable,_f:etsysPseChassisPowerConsumable,_g:etsysPseChassisPowerAssigned,_h:etsysPseChassisPowerRedundancy,'etsysPsePowerSupplyStatusTable':etsysPsePowerSupplyStatusTable,'etsysPsePowerSupplyStatusEntry':etsysPsePowerSupplyStatusEntry,_T:etsysPsePowerSupplyModuleNumber,_M:etsysPsePowerSupplyModuleStatus,'etsysPseSlotPowerManagement':etsysPseSlotPowerManagement,'etsysPseModulePowerManagementTable':etsysPseModulePowerManagementTable,_X:etsysPseModulePowerManagementEntry,_i:etsysPseModulePowerMode,_j:etsysPseModulePowerClassBudget,_k:etsysPseModulePowerUsage,'etsysPsePortPowerManagement':etsysPsePortPowerManagement,'etsysPsePortPowerManagementTable':etsysPsePortPowerManagementTable,_Y:etsysPsePortPowerManagementEntry,_N:etsysPsePortPowerLimit,_O:etsysPsePortPowerUsage,_P:etsysPsePortPDType,_m:etsysPsePortCapability,_n:etsysPsePortCapabilitySelect,_o:etsysPsePortDetectionStatus,'etsysPsePowerAllocationConformance':etsysPsePowerAllocationConformance,'etsysPsePowerAllocationGroups':etsysPsePowerAllocationGroups,_H:etsysPsePowerAllocationControlGroup,_I:etsysPseChassisPowerStatusGroup,_J:etsysPsePowerNotificationGroup,_Q:etsysPseModulePowerManagementGroup,_s:etsysPsePortPowerManagementGroup,_t:etsysPsePortPowerManagementGroupRev2,'etsysPsePowerAllocationCompliances':etsysPsePowerAllocationCompliances,'etsysPsePowerAllocationCompliance':etsysPsePowerAllocationCompliance,'etsysPsePowerAllocationCompliance2':etsysPsePowerAllocationCompliance2,'etsysPsePowerAllocationCompliance2Rev2':etsysPsePowerAllocationCompliance2Rev2})