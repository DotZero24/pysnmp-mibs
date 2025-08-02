_K='energySuppliedPortIndex'
_J='statusPortIndex'
_I='enabled'
_H='configPortIndex'
_G='not-accessible'
_F='disabled'
_E='G6-POE-MIB'
_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
g6,=mibBuilder.importSymbols('MICROSENS-G6-MIB','g6')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
device=ModuleIdentity((1,3,6,1,4,1,3181,10,6,1))
if mibBuilder.loadTexts:device.setRevisions(('2018-02-12 16:19',))
_Poe_ObjectIdentity=ObjectIdentity
poe=_Poe_ObjectIdentity((1,3,6,1,4,1,3181,10,6,1,33))
class _PoePoeMaxPowerAvailable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PoePoeMaxPowerAvailable_Type.__name__=_C
_PoePoeMaxPowerAvailable_Object=MibScalar
poePoeMaxPowerAvailable=_PoePoeMaxPowerAvailable_Object((1,3,6,1,4,1,3181,10,6,1,33,1),_PoePoeMaxPowerAvailable_Type())
poePoeMaxPowerAvailable.setMaxAccess(_D)
if mibBuilder.loadTexts:poePoeMaxPowerAvailable.setStatus(_A)
_PoeRestartPoePort_Type=DisplayString
_PoeRestartPoePort_Object=MibScalar
poeRestartPoePort=_PoeRestartPoePort_Object((1,3,6,1,4,1,3181,10,6,1,33,2),_PoeRestartPoePort_Type())
poeRestartPoePort.setMaxAccess(_D)
if mibBuilder.loadTexts:poeRestartPoePort.setStatus(_A)
_ConfigTable_Object=MibTable
configTable=_ConfigTable_Object((1,3,6,1,4,1,3181,10,6,1,33,3))
if mibBuilder.loadTexts:configTable.setStatus(_A)
_ConfigEntry_Object=MibTableRow
configEntry=_ConfigEntry_Object((1,3,6,1,4,1,3181,10,6,1,33,3,1))
configEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:configEntry.setStatus(_A)
class _ConfigPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_ConfigPortIndex_Type.__name__=_C
_ConfigPortIndex_Object=MibTableColumn
configPortIndex=_ConfigPortIndex_Object((1,3,6,1,4,1,3181,10,6,1,33,3,1,1),_ConfigPortIndex_Type())
configPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:configPortIndex.setStatus(_A)
class _ConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,0),('automatic',1),('class0',2),('class1',3),('class2',4),('class3',5),('class4',6),('forcedOn',7)))
_ConfigMode_Type.__name__=_C
_ConfigMode_Object=MibTableColumn
configMode=_ConfigMode_Object((1,3,6,1,4,1,3181,10,6,1,33,3,1,2),_ConfigMode_Type())
configMode.setMaxAccess(_D)
if mibBuilder.loadTexts:configMode.setStatus(_A)
class _ConfigPriorityPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_I,1)))
_ConfigPriorityPort_Type.__name__=_C
_ConfigPriorityPort_Object=MibTableColumn
configPriorityPort=_ConfigPriorityPort_Object((1,3,6,1,4,1,3181,10,6,1,33,3,1,3),_ConfigPriorityPort_Type())
configPriorityPort.setMaxAccess(_D)
if mibBuilder.loadTexts:configPriorityPort.setStatus(_A)
class _ConfigEnablePoePlus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_I,1),('lldpControlled',2)))
_ConfigEnablePoePlus_Type.__name__=_C
_ConfigEnablePoePlus_Object=MibTableColumn
configEnablePoePlus=_ConfigEnablePoePlus_Object((1,3,6,1,4,1,3181,10,6,1,33,3,1,4),_ConfigEnablePoePlus_Type())
configEnablePoePlus.setMaxAccess(_D)
if mibBuilder.loadTexts:configEnablePoePlus.setStatus(_A)
_PoeTotalPowerConsumed_Type=Unsigned32
_PoeTotalPowerConsumed_Object=MibScalar
poeTotalPowerConsumed=_PoeTotalPowerConsumed_Object((1,3,6,1,4,1,3181,10,6,1,33,100),_PoeTotalPowerConsumed_Type())
poeTotalPowerConsumed.setMaxAccess(_B)
if mibBuilder.loadTexts:poeTotalPowerConsumed.setStatus(_A)
_StatusTable_Object=MibTable
statusTable=_StatusTable_Object((1,3,6,1,4,1,3181,10,6,1,33,101))
if mibBuilder.loadTexts:statusTable.setStatus(_A)
_StatusEntry_Object=MibTableRow
statusEntry=_StatusEntry_Object((1,3,6,1,4,1,3181,10,6,1,33,101,1))
statusEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:statusEntry.setStatus(_A)
class _StatusPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_StatusPortIndex_Type.__name__=_C
_StatusPortIndex_Object=MibTableColumn
statusPortIndex=_StatusPortIndex_Object((1,3,6,1,4,1,3181,10,6,1,33,101,1,1),_StatusPortIndex_Type())
statusPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:statusPortIndex.setStatus(_A)
class _StatusCondition_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_F,0),('powerOff',1),('discovering',2),('powered',3),('classMismatch',4),('shortCircuit',5),('rejected',6),('overCurrent',7),('overTemp',8),('voltageTooLow',9)))
_StatusCondition_Type.__name__=_C
_StatusCondition_Object=MibTableColumn
statusCondition=_StatusCondition_Object((1,3,6,1,4,1,3181,10,6,1,33,101,1,2),_StatusCondition_Type())
statusCondition.setMaxAccess(_B)
if mibBuilder.loadTexts:statusCondition.setStatus(_A)
class _StatusDeterminedClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,7,255)));namedValues=NamedValues(*(('isClass0',0),('isClass1',1),('isClass2',2),('isClass3',3),('isClass4',4),('isOverload',5),('probesNotEqual',7),('isUnknown',255)))
_StatusDeterminedClass_Type.__name__=_C
_StatusDeterminedClass_Object=MibTableColumn
statusDeterminedClass=_StatusDeterminedClass_Object((1,3,6,1,4,1,3181,10,6,1,33,101,1,3),_StatusDeterminedClass_Type())
statusDeterminedClass.setMaxAccess(_B)
if mibBuilder.loadTexts:statusDeterminedClass.setStatus(_A)
class _StatusOutputCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_StatusOutputCurrent_Type.__name__=_C
_StatusOutputCurrent_Object=MibTableColumn
statusOutputCurrent=_StatusOutputCurrent_Object((1,3,6,1,4,1,3181,10,6,1,33,101,1,4),_StatusOutputCurrent_Type())
statusOutputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:statusOutputCurrent.setStatus(_A)
class _StatusOutputVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_StatusOutputVoltage_Type.__name__=_C
_StatusOutputVoltage_Object=MibTableColumn
statusOutputVoltage=_StatusOutputVoltage_Object((1,3,6,1,4,1,3181,10,6,1,33,101,1,5),_StatusOutputVoltage_Type())
statusOutputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:statusOutputVoltage.setStatus(_A)
class _StatusOutputPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_StatusOutputPower_Type.__name__=_C
_StatusOutputPower_Object=MibTableColumn
statusOutputPower=_StatusOutputPower_Object((1,3,6,1,4,1,3181,10,6,1,33,101,1,6),_StatusOutputPower_Type())
statusOutputPower.setMaxAccess(_B)
if mibBuilder.loadTexts:statusOutputPower.setStatus(_A)
_StatusPowerDeniedCounter_Type=Unsigned32
_StatusPowerDeniedCounter_Object=MibTableColumn
statusPowerDeniedCounter=_StatusPowerDeniedCounter_Object((1,3,6,1,4,1,3181,10,6,1,33,101,1,7),_StatusPowerDeniedCounter_Type())
statusPowerDeniedCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:statusPowerDeniedCounter.setStatus(_A)
_StatusOverCurrentCounter_Type=Unsigned32
_StatusOverCurrentCounter_Object=MibTableColumn
statusOverCurrentCounter=_StatusOverCurrentCounter_Object((1,3,6,1,4,1,3181,10,6,1,33,101,1,8),_StatusOverCurrentCounter_Type())
statusOverCurrentCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:statusOverCurrentCounter.setStatus(_A)
_StatusShortCircuitCounter_Type=Unsigned32
_StatusShortCircuitCounter_Object=MibTableColumn
statusShortCircuitCounter=_StatusShortCircuitCounter_Object((1,3,6,1,4,1,3181,10,6,1,33,101,1,9),_StatusShortCircuitCounter_Type())
statusShortCircuitCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:statusShortCircuitCounter.setStatus(_A)
_EnergySuppliedTable_Object=MibTable
energySuppliedTable=_EnergySuppliedTable_Object((1,3,6,1,4,1,3181,10,6,1,33,102))
if mibBuilder.loadTexts:energySuppliedTable.setStatus(_A)
_EnergySuppliedEntry_Object=MibTableRow
energySuppliedEntry=_EnergySuppliedEntry_Object((1,3,6,1,4,1,3181,10,6,1,33,102,1))
energySuppliedEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:energySuppliedEntry.setStatus(_A)
class _EnergySuppliedPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_EnergySuppliedPortIndex_Type.__name__=_C
_EnergySuppliedPortIndex_Object=MibTableColumn
energySuppliedPortIndex=_EnergySuppliedPortIndex_Object((1,3,6,1,4,1,3181,10,6,1,33,102,1,1),_EnergySuppliedPortIndex_Type())
energySuppliedPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:energySuppliedPortIndex.setStatus(_A)
_EnergySuppliedLast5Seconds_Type=Unsigned32
_EnergySuppliedLast5Seconds_Object=MibTableColumn
energySuppliedLast5Seconds=_EnergySuppliedLast5Seconds_Object((1,3,6,1,4,1,3181,10,6,1,33,102,1,2),_EnergySuppliedLast5Seconds_Type())
energySuppliedLast5Seconds.setMaxAccess(_B)
if mibBuilder.loadTexts:energySuppliedLast5Seconds.setStatus(_A)
_EnergySuppliedLast15Seconds_Type=Unsigned32
_EnergySuppliedLast15Seconds_Object=MibTableColumn
energySuppliedLast15Seconds=_EnergySuppliedLast15Seconds_Object((1,3,6,1,4,1,3181,10,6,1,33,102,1,3),_EnergySuppliedLast15Seconds_Type())
energySuppliedLast15Seconds.setMaxAccess(_B)
if mibBuilder.loadTexts:energySuppliedLast15Seconds.setStatus(_A)
_EnergySuppliedLastMinute_Type=Unsigned32
_EnergySuppliedLastMinute_Object=MibTableColumn
energySuppliedLastMinute=_EnergySuppliedLastMinute_Object((1,3,6,1,4,1,3181,10,6,1,33,102,1,4),_EnergySuppliedLastMinute_Type())
energySuppliedLastMinute.setMaxAccess(_B)
if mibBuilder.loadTexts:energySuppliedLastMinute.setStatus(_A)
_EnergySuppliedLast15Minutes_Type=Unsigned32
_EnergySuppliedLast15Minutes_Object=MibTableColumn
energySuppliedLast15Minutes=_EnergySuppliedLast15Minutes_Object((1,3,6,1,4,1,3181,10,6,1,33,102,1,5),_EnergySuppliedLast15Minutes_Type())
energySuppliedLast15Minutes.setMaxAccess(_B)
if mibBuilder.loadTexts:energySuppliedLast15Minutes.setStatus(_A)
_EnergySuppliedLastHour_Type=Unsigned32
_EnergySuppliedLastHour_Object=MibTableColumn
energySuppliedLastHour=_EnergySuppliedLastHour_Object((1,3,6,1,4,1,3181,10,6,1,33,102,1,6),_EnergySuppliedLastHour_Type())
energySuppliedLastHour.setMaxAccess(_B)
if mibBuilder.loadTexts:energySuppliedLastHour.setStatus(_A)
_EnergySuppliedLastDay_Type=Unsigned32
_EnergySuppliedLastDay_Object=MibTableColumn
energySuppliedLastDay=_EnergySuppliedLastDay_Object((1,3,6,1,4,1,3181,10,6,1,33,102,1,7),_EnergySuppliedLastDay_Type())
energySuppliedLastDay.setMaxAccess(_B)
if mibBuilder.loadTexts:energySuppliedLastDay.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'device':device,'poe':poe,'poePoeMaxPowerAvailable':poePoeMaxPowerAvailable,'poeRestartPoePort':poeRestartPoePort,'configTable':configTable,'configEntry':configEntry,_H:configPortIndex,'configMode':configMode,'configPriorityPort':configPriorityPort,'configEnablePoePlus':configEnablePoePlus,'poeTotalPowerConsumed':poeTotalPowerConsumed,'statusTable':statusTable,'statusEntry':statusEntry,_J:statusPortIndex,'statusCondition':statusCondition,'statusDeterminedClass':statusDeterminedClass,'statusOutputCurrent':statusOutputCurrent,'statusOutputVoltage':statusOutputVoltage,'statusOutputPower':statusOutputPower,'statusPowerDeniedCounter':statusPowerDeniedCounter,'statusOverCurrentCounter':statusOverCurrentCounter,'statusShortCircuitCounter':statusShortCircuitCounter,'energySuppliedTable':energySuppliedTable,'energySuppliedEntry':energySuppliedEntry,_K:energySuppliedPortIndex,'energySuppliedLast5Seconds':energySuppliedLast5Seconds,'energySuppliedLast15Seconds':energySuppliedLast15Seconds,'energySuppliedLastMinute':energySuppliedLastMinute,'energySuppliedLast15Minutes':energySuppliedLast15Minutes,'energySuppliedLastHour':energySuppliedLastHour,'energySuppliedLastDay':energySuppliedLastDay})