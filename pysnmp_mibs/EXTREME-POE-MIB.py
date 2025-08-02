_S='notApplicable'
_R='external'
_Q='internal'
_P='extremePethSlotNumber'
_O='EXTREME-POE-MIB'
_N='pethPsePortIndex'
_M='pethPsePortGroupIndex'
_L='none'
_K='disable'
_J='enable'
_I='POWER-ETHERNET-MIB'
_H='clear'
_G='set'
_F='watts'
_E='Milliwatts'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,extremeV2Traps=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent','extremeV2Traps')
pethMainPseGroupIndex,pethPsePortGroupIndex,pethPsePortIndex=mibBuilder.importSymbols(_I,'pethMainPseGroupIndex',_M,_N)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
extremePoE=ModuleIdentity((1,3,6,1,4,1,1916,1,27))
_ExtremePethMain_ObjectIdentity=ObjectIdentity
extremePethMain=_ExtremePethMain_ObjectIdentity((1,3,6,1,4,1,1916,1,27,1))
_ExtremePethPseSlotTable_Object=MibTable
extremePethPseSlotTable=_ExtremePethPseSlotTable_Object((1,3,6,1,4,1,1916,1,27,1,2))
if mibBuilder.loadTexts:extremePethPseSlotTable.setStatus(_A)
_ExtremePethPseSlotEntry_Object=MibTableRow
extremePethPseSlotEntry=_ExtremePethPseSlotEntry_Object((1,3,6,1,4,1,1916,1,27,1,2,1))
extremePethPseSlotEntry.setIndexNames((0,_O,_P))
if mibBuilder.loadTexts:extremePethPseSlotEntry.setStatus(_A)
_ExtremePethSlotNumber_Type=Integer32
_ExtremePethSlotNumber_Object=MibTableColumn
extremePethSlotNumber=_ExtremePethSlotNumber_Object((1,3,6,1,4,1,1916,1,27,1,2,1,1),_ExtremePethSlotNumber_Type())
extremePethSlotNumber.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:extremePethSlotNumber.setStatus(_A)
_ExtremePethSlotPowerLimit_Type=Integer32
_ExtremePethSlotPowerLimit_Object=MibTableColumn
extremePethSlotPowerLimit=_ExtremePethSlotPowerLimit_Object((1,3,6,1,4,1,1916,1,27,1,2,1,2),_ExtremePethSlotPowerLimit_Type())
extremePethSlotPowerLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePethSlotPowerLimit.setStatus(_A)
if mibBuilder.loadTexts:extremePethSlotPowerLimit.setUnits(_F)
_ExtremePethSlotConsumptionPower_Type=Gauge32
_ExtremePethSlotConsumptionPower_Object=MibTableColumn
extremePethSlotConsumptionPower=_ExtremePethSlotConsumptionPower_Object((1,3,6,1,4,1,1916,1,27,1,2,1,3),_ExtremePethSlotConsumptionPower_Type())
extremePethSlotConsumptionPower.setMaxAccess(_D)
if mibBuilder.loadTexts:extremePethSlotConsumptionPower.setStatus(_A)
if mibBuilder.loadTexts:extremePethSlotConsumptionPower.setUnits(_F)
class _ExtremePethSlotClearConnectHistory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ExtremePethSlotClearConnectHistory_Type.__name__=_B
_ExtremePethSlotClearConnectHistory_Object=MibTableColumn
extremePethSlotClearConnectHistory=_ExtremePethSlotClearConnectHistory_Object((1,3,6,1,4,1,1916,1,27,1,2,1,4),_ExtremePethSlotClearConnectHistory_Type())
extremePethSlotClearConnectHistory.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePethSlotClearConnectHistory.setStatus(_A)
_ExtremePethSlotReservedConsumptionPower_Type=Gauge32
_ExtremePethSlotReservedConsumptionPower_Object=MibTableColumn
extremePethSlotReservedConsumptionPower=_ExtremePethSlotReservedConsumptionPower_Object((1,3,6,1,4,1,1916,1,27,1,2,1,5),_ExtremePethSlotReservedConsumptionPower_Type())
extremePethSlotReservedConsumptionPower.setMaxAccess(_D)
if mibBuilder.loadTexts:extremePethSlotReservedConsumptionPower.setStatus(_A)
if mibBuilder.loadTexts:extremePethSlotReservedConsumptionPower.setUnits(_E)
_ExtremePethSlotCommonConsumptionPower_Type=Gauge32
_ExtremePethSlotCommonConsumptionPower_Object=MibTableColumn
extremePethSlotCommonConsumptionPower=_ExtremePethSlotCommonConsumptionPower_Object((1,3,6,1,4,1,1916,1,27,1,2,1,6),_ExtremePethSlotCommonConsumptionPower_Type())
extremePethSlotCommonConsumptionPower.setMaxAccess(_D)
if mibBuilder.loadTexts:extremePethSlotCommonConsumptionPower.setStatus(_A)
if mibBuilder.loadTexts:extremePethSlotCommonConsumptionPower.setUnits(_E)
class _ExtremePethSlotAdminEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ExtremePethSlotAdminEnable_Type.__name__=_B
_ExtremePethSlotAdminEnable_Object=MibTableColumn
extremePethSlotAdminEnable=_ExtremePethSlotAdminEnable_Object((1,3,6,1,4,1,1916,1,27,1,2,1,7),_ExtremePethSlotAdminEnable_Type())
extremePethSlotAdminEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePethSlotAdminEnable.setStatus(_A)
class _ExtremePethSlotPoeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('initializing',1),('operational',2),('downloadFail',3),('calibrationRequired',4),('invalidFirmware',5),('mismatchVersion',6),('updating',7),('invalidDevice',8),('notOperational',9),('other',10)))
_ExtremePethSlotPoeStatus_Type.__name__=_B
_ExtremePethSlotPoeStatus_Object=MibTableColumn
extremePethSlotPoeStatus=_ExtremePethSlotPoeStatus_Object((1,3,6,1,4,1,1916,1,27,1,2,1,8),_ExtremePethSlotPoeStatus_Type())
extremePethSlotPoeStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:extremePethSlotPoeStatus.setStatus(_A)
class _ExtremePethSlotPoeResetSystem_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ExtremePethSlotPoeResetSystem_Type.__name__=_B
_ExtremePethSlotPoeResetSystem_Object=MibTableColumn
extremePethSlotPoeResetSystem=_ExtremePethSlotPoeResetSystem_Object((1,3,6,1,4,1,1916,1,27,1,2,1,9),_ExtremePethSlotPoeResetSystem_Type())
extremePethSlotPoeResetSystem.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePethSlotPoeResetSystem.setStatus(_A)
_ExtremePethSlotMaxAvailPower_Type=Gauge32
_ExtremePethSlotMaxAvailPower_Object=MibTableColumn
extremePethSlotMaxAvailPower=_ExtremePethSlotMaxAvailPower_Object((1,3,6,1,4,1,1916,1,27,1,2,1,10),_ExtremePethSlotMaxAvailPower_Type())
extremePethSlotMaxAvailPower.setMaxAccess(_D)
if mibBuilder.loadTexts:extremePethSlotMaxAvailPower.setStatus(_A)
if mibBuilder.loadTexts:extremePethSlotMaxAvailPower.setUnits(_F)
_ExtremePethSlotMaxCapacity_Type=Gauge32
_ExtremePethSlotMaxCapacity_Object=MibTableColumn
extremePethSlotMaxCapacity=_ExtremePethSlotMaxCapacity_Object((1,3,6,1,4,1,1916,1,27,1,2,1,11),_ExtremePethSlotMaxCapacity_Type())
extremePethSlotMaxCapacity.setMaxAccess(_D)
if mibBuilder.loadTexts:extremePethSlotMaxCapacity.setStatus(_A)
if mibBuilder.loadTexts:extremePethSlotMaxCapacity.setUnits(_F)
class _ExtremePethSlotBackupPSU_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_Q,2),(_R,3),(_S,4)))
_ExtremePethSlotBackupPSU_Type.__name__=_B
_ExtremePethSlotBackupPSU_Object=MibTableColumn
extremePethSlotBackupPSU=_ExtremePethSlotBackupPSU_Object((1,3,6,1,4,1,1916,1,27,1,2,1,12),_ExtremePethSlotBackupPSU_Type())
extremePethSlotBackupPSU.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePethSlotBackupPSU.setStatus(_A)
class _ExtremePethSlotPSUActive_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),(_Q,2),(_R,3)))
_ExtremePethSlotPSUActive_Type.__name__=_B
_ExtremePethSlotPSUActive_Object=MibTableColumn
extremePethSlotPSUActive=_ExtremePethSlotPSUActive_Object((1,3,6,1,4,1,1916,1,27,1,2,1,13),_ExtremePethSlotPSUActive_Type())
extremePethSlotPSUActive.setMaxAccess(_D)
if mibBuilder.loadTexts:extremePethSlotPSUActive.setStatus(_A)
_ExtremePethSlotMeasuredPower_Type=Gauge32
_ExtremePethSlotMeasuredPower_Object=MibTableColumn
extremePethSlotMeasuredPower=_ExtremePethSlotMeasuredPower_Object((1,3,6,1,4,1,1916,1,27,1,2,1,14),_ExtremePethSlotMeasuredPower_Type())
extremePethSlotMeasuredPower.setMaxAccess(_D)
if mibBuilder.loadTexts:extremePethSlotMeasuredPower.setStatus(_A)
if mibBuilder.loadTexts:extremePethSlotMeasuredPower.setUnits('milliwatts')
_ExtremePethSlotMainPseIndex_Type=Integer32
_ExtremePethSlotMainPseIndex_Object=MibTableColumn
extremePethSlotMainPseIndex=_ExtremePethSlotMainPseIndex_Object((1,3,6,1,4,1,1916,1,27,1,2,1,15),_ExtremePethSlotMainPseIndex_Type())
extremePethSlotMainPseIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:extremePethSlotMainPseIndex.setStatus(_A)
_ExtremePethPort_ObjectIdentity=ObjectIdentity
extremePethPort=_ExtremePethPort_ObjectIdentity((1,3,6,1,4,1,1916,1,27,2))
_ExtremePethPsePortTable_Object=MibTable
extremePethPsePortTable=_ExtremePethPsePortTable_Object((1,3,6,1,4,1,1916,1,27,2,1))
if mibBuilder.loadTexts:extremePethPsePortTable.setStatus(_A)
_ExtremePethPsePortEntry_Object=MibTableRow
extremePethPsePortEntry=_ExtremePethPsePortEntry_Object((1,3,6,1,4,1,1916,1,27,2,1,1))
extremePethPsePortEntry.setIndexNames((0,_I,_M),(0,_I,_N))
if mibBuilder.loadTexts:extremePethPsePortEntry.setStatus(_A)
class _ExtremePethPortOperatorLimit_Type(Integer32):defaultValue=15400;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3000,60000))
_ExtremePethPortOperatorLimit_Type.__name__=_B
_ExtremePethPortOperatorLimit_Object=MibTableColumn
extremePethPortOperatorLimit=_ExtremePethPortOperatorLimit_Object((1,3,6,1,4,1,1916,1,27,2,1,1,1),_ExtremePethPortOperatorLimit_Type())
extremePethPortOperatorLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePethPortOperatorLimit.setStatus(_A)
if mibBuilder.loadTexts:extremePethPortOperatorLimit.setUnits(_E)
class _ExtremePethPortReservedBudget_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60000))
_ExtremePethPortReservedBudget_Type.__name__=_B
_ExtremePethPortReservedBudget_Object=MibTableColumn
extremePethPortReservedBudget=_ExtremePethPortReservedBudget_Object((1,3,6,1,4,1,1916,1,27,2,1,1,2),_ExtremePethPortReservedBudget_Type())
extremePethPortReservedBudget.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePethPortReservedBudget.setStatus(_A)
if mibBuilder.loadTexts:extremePethPortReservedBudget.setUnits(_E)
class _ExtremePethPortViolationPrecedence_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('advertisedClass',1),('operatorLimit',2),('maxAdvertisedOperator',3),(_L,4)))
_ExtremePethPortViolationPrecedence_Type.__name__=_B
_ExtremePethPortViolationPrecedence_Object=MibTableColumn
extremePethPortViolationPrecedence=_ExtremePethPortViolationPrecedence_Object((1,3,6,1,4,1,1916,1,27,2,1,1,3),_ExtremePethPortViolationPrecedence_Type())
extremePethPortViolationPrecedence.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePethPortViolationPrecedence.setStatus(_A)
class _ExtremePethPortClearFault_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ExtremePethPortClearFault_Type.__name__=_B
_ExtremePethPortClearFault_Object=MibTableColumn
extremePethPortClearFault=_ExtremePethPortClearFault_Object((1,3,6,1,4,1,1916,1,27,2,1,1,4),_ExtremePethPortClearFault_Type())
extremePethPortClearFault.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePethPortClearFault.setStatus(_A)
class _ExtremePethPortResetPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_ExtremePethPortResetPower_Type.__name__=_B
_ExtremePethPortResetPower_Object=MibTableColumn
extremePethPortResetPower=_ExtremePethPortResetPower_Object((1,3,6,1,4,1,1916,1,27,2,1,1,5),_ExtremePethPortResetPower_Type())
extremePethPortResetPower.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePethPortResetPower.setStatus(_A)
_ExtremePethPortMeasuredPower_Type=Gauge32
_ExtremePethPortMeasuredPower_Object=MibTableColumn
extremePethPortMeasuredPower=_ExtremePethPortMeasuredPower_Object((1,3,6,1,4,1,1916,1,27,2,1,1,6),_ExtremePethPortMeasuredPower_Type())
extremePethPortMeasuredPower.setMaxAccess(_D)
if mibBuilder.loadTexts:extremePethPortMeasuredPower.setStatus(_A)
if mibBuilder.loadTexts:extremePethPortMeasuredPower.setUnits(_E)
_ExtremePethSystem_ObjectIdentity=ObjectIdentity
extremePethSystem=_ExtremePethSystem_ObjectIdentity((1,3,6,1,4,1,1916,1,27,4))
class _ExtremePethSystemAdminEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ExtremePethSystemAdminEnable_Type.__name__=_B
_ExtremePethSystemAdminEnable_Object=MibScalar
extremePethSystemAdminEnable=_ExtremePethSystemAdminEnable_Object((1,3,6,1,4,1,1916,1,27,4,1),_ExtremePethSystemAdminEnable_Type())
extremePethSystemAdminEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePethSystemAdminEnable.setStatus(_A)
class _ExtremePethSystemDisconnectPrecedence_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lowest-priority',1),('deny-port',2)))
_ExtremePethSystemDisconnectPrecedence_Type.__name__=_B
_ExtremePethSystemDisconnectPrecedence_Object=MibScalar
extremePethSystemDisconnectPrecedence=_ExtremePethSystemDisconnectPrecedence_Object((1,3,6,1,4,1,1916,1,27,4,2),_ExtremePethSystemDisconnectPrecedence_Type())
extremePethSystemDisconnectPrecedence.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePethSystemDisconnectPrecedence.setStatus(_A)
class _ExtremePethSystemUsageThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_ExtremePethSystemUsageThreshold_Type.__name__=_B
_ExtremePethSystemUsageThreshold_Object=MibScalar
extremePethSystemUsageThreshold=_ExtremePethSystemUsageThreshold_Object((1,3,6,1,4,1,1916,1,27,4,3),_ExtremePethSystemUsageThreshold_Type())
extremePethSystemUsageThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePethSystemUsageThreshold.setStatus(_A)
if mibBuilder.loadTexts:extremePethSystemUsageThreshold.setUnits('%')
class _ExtremePethSystemPowerSupplyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('redundant',1),('loadSharing',2),(_S,3)))
_ExtremePethSystemPowerSupplyMode_Type.__name__=_B
_ExtremePethSystemPowerSupplyMode_Object=MibScalar
extremePethSystemPowerSupplyMode=_ExtremePethSystemPowerSupplyMode_Object((1,3,6,1,4,1,1916,1,27,4,4),_ExtremePethSystemPowerSupplyMode_Type())
extremePethSystemPowerSupplyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePethSystemPowerSupplyMode.setStatus(_A)
class _ExtremePethSystemLegacyEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_ExtremePethSystemLegacyEnable_Type.__name__=_B
_ExtremePethSystemLegacyEnable_Object=MibScalar
extremePethSystemLegacyEnable=_ExtremePethSystemLegacyEnable_Object((1,3,6,1,4,1,1916,1,27,4,5),_ExtremePethSystemLegacyEnable_Type())
extremePethSystemLegacyEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:extremePethSystemLegacyEnable.setStatus(_A)
mibBuilder.exportSymbols(_O,**{'extremePoE':extremePoE,'extremePethMain':extremePethMain,'extremePethPseSlotTable':extremePethPseSlotTable,'extremePethPseSlotEntry':extremePethPseSlotEntry,_P:extremePethSlotNumber,'extremePethSlotPowerLimit':extremePethSlotPowerLimit,'extremePethSlotConsumptionPower':extremePethSlotConsumptionPower,'extremePethSlotClearConnectHistory':extremePethSlotClearConnectHistory,'extremePethSlotReservedConsumptionPower':extremePethSlotReservedConsumptionPower,'extremePethSlotCommonConsumptionPower':extremePethSlotCommonConsumptionPower,'extremePethSlotAdminEnable':extremePethSlotAdminEnable,'extremePethSlotPoeStatus':extremePethSlotPoeStatus,'extremePethSlotPoeResetSystem':extremePethSlotPoeResetSystem,'extremePethSlotMaxAvailPower':extremePethSlotMaxAvailPower,'extremePethSlotMaxCapacity':extremePethSlotMaxCapacity,'extremePethSlotBackupPSU':extremePethSlotBackupPSU,'extremePethSlotPSUActive':extremePethSlotPSUActive,'extremePethSlotMeasuredPower':extremePethSlotMeasuredPower,'extremePethSlotMainPseIndex':extremePethSlotMainPseIndex,'extremePethPort':extremePethPort,'extremePethPsePortTable':extremePethPsePortTable,'extremePethPsePortEntry':extremePethPsePortEntry,'extremePethPortOperatorLimit':extremePethPortOperatorLimit,'extremePethPortReservedBudget':extremePethPortReservedBudget,'extremePethPortViolationPrecedence':extremePethPortViolationPrecedence,'extremePethPortClearFault':extremePethPortClearFault,'extremePethPortResetPower':extremePethPortResetPower,'extremePethPortMeasuredPower':extremePethPortMeasuredPower,'extremePethSystem':extremePethSystem,'extremePethSystemAdminEnable':extremePethSystemAdminEnable,'extremePethSystemDisconnectPrecedence':extremePethSystemDisconnectPrecedence,'extremePethSystemUsageThreshold':extremePethSystemUsageThreshold,'extremePethSystemPowerSupplyMode':extremePethSystemPowerSupplyMode,'extremePethSystemLegacyEnable':extremePethSystemLegacyEnable})