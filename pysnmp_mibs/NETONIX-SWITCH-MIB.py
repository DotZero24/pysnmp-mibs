_K='poeStatusIndex'
_J='voltageIndex'
_I='tempIndex'
_H='fanIndex'
_G='snmpGroup'
_F='not-accessible'
_E='DisplayString'
_D='NETONIX-SWITCH-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
snmpGroup,=mibBuilder.importSymbols('SNMPv2-MIB',_G)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
netonixSwitch=ModuleIdentity((1,3,6,1,4,1,46242))
if mibBuilder.loadTexts:netonixSwitch.setRevisions(('1998-03-23 18:00',))
class VoltageTC(TextualConvention,Integer32):status=_A;displayHint='d-2'
class PowerTC(TextualConvention,Integer32):status=_A;displayHint='d-1'
class CurrentTC(TextualConvention,Integer32):status=_A;displayHint='d-1'
class _FirmwareVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_FirmwareVersion_Type.__name__=_E
_FirmwareVersion_Object=MibScalar
firmwareVersion=_FirmwareVersion_Object((1,3,6,1,4,1,46242,1),_FirmwareVersion_Type())
firmwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:firmwareVersion.setStatus(_A)
_FanTable_Object=MibTable
fanTable=_FanTable_Object((1,3,6,1,4,1,46242,2))
if mibBuilder.loadTexts:fanTable.setStatus(_A)
_FanEntry_Object=MibTableRow
fanEntry=_FanEntry_Object((1,3,6,1,4,1,46242,2,1))
fanEntry.setIndexNames((0,_D,_H))
if mibBuilder.loadTexts:fanEntry.setStatus(_A)
class _FanIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FanIndex_Type.__name__=_C
_FanIndex_Object=MibTableColumn
fanIndex=_FanIndex_Object((1,3,6,1,4,1,46242,2,1,1),_FanIndex_Type())
fanIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:fanIndex.setStatus(_A)
class _FanSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FanSpeed_Type.__name__=_C
_FanSpeed_Object=MibTableColumn
fanSpeed=_FanSpeed_Object((1,3,6,1,4,1,46242,2,1,2),_FanSpeed_Type())
fanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:fanSpeed.setStatus(_A)
_TempTable_Object=MibTable
tempTable=_TempTable_Object((1,3,6,1,4,1,46242,3))
if mibBuilder.loadTexts:tempTable.setStatus(_A)
_TempEntry_Object=MibTableRow
tempEntry=_TempEntry_Object((1,3,6,1,4,1,46242,3,1))
tempEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:tempEntry.setStatus(_A)
class _TempIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_TempIndex_Type.__name__=_C
_TempIndex_Object=MibTableColumn
tempIndex=_TempIndex_Object((1,3,6,1,4,1,46242,3,1,1),_TempIndex_Type())
tempIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:tempIndex.setStatus(_A)
class _TempDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TempDescription_Type.__name__=_E
_TempDescription_Object=MibTableColumn
tempDescription=_TempDescription_Object((1,3,6,1,4,1,46242,3,1,2),_TempDescription_Type())
tempDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:tempDescription.setStatus(_A)
class _Temp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Temp_Type.__name__=_C
_Temp_Object=MibTableColumn
temp=_Temp_Object((1,3,6,1,4,1,46242,3,1,3),_Temp_Type())
temp.setMaxAccess(_B)
if mibBuilder.loadTexts:temp.setStatus(_A)
_VoltageTable_Object=MibTable
voltageTable=_VoltageTable_Object((1,3,6,1,4,1,46242,4))
if mibBuilder.loadTexts:voltageTable.setStatus(_A)
_VoltageEntry_Object=MibTableRow
voltageEntry=_VoltageEntry_Object((1,3,6,1,4,1,46242,4,1))
voltageEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:voltageEntry.setStatus(_A)
class _VoltageIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VoltageIndex_Type.__name__=_C
_VoltageIndex_Object=MibTableColumn
voltageIndex=_VoltageIndex_Object((1,3,6,1,4,1,46242,4,1,1),_VoltageIndex_Type())
voltageIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:voltageIndex.setStatus(_A)
class _VoltageDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_VoltageDescription_Type.__name__=_E
_VoltageDescription_Object=MibTableColumn
voltageDescription=_VoltageDescription_Object((1,3,6,1,4,1,46242,4,1,2),_VoltageDescription_Type())
voltageDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:voltageDescription.setStatus(_A)
_Voltage_Type=VoltageTC
_Voltage_Object=MibTableColumn
voltage=_Voltage_Object((1,3,6,1,4,1,46242,4,1,3),_Voltage_Type())
voltage.setMaxAccess(_B)
if mibBuilder.loadTexts:voltage.setStatus(_A)
_PoeStatusTable_Object=MibTable
poeStatusTable=_PoeStatusTable_Object((1,3,6,1,4,1,46242,5))
if mibBuilder.loadTexts:poeStatusTable.setStatus(_A)
_PoeStatusEntry_Object=MibTableRow
poeStatusEntry=_PoeStatusEntry_Object((1,3,6,1,4,1,46242,5,1))
poeStatusEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:poeStatusEntry.setStatus(_A)
class _PoeStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_PoeStatusIndex_Type.__name__=_C
_PoeStatusIndex_Object=MibTableColumn
poeStatusIndex=_PoeStatusIndex_Object((1,3,6,1,4,1,46242,5,1,1),_PoeStatusIndex_Type())
poeStatusIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:poeStatusIndex.setStatus(_A)
class _PoeStatus_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PoeStatus_Type.__name__=_E
_PoeStatus_Object=MibTableColumn
poeStatus=_PoeStatus_Object((1,3,6,1,4,1,46242,5,1,2),_PoeStatus_Type())
poeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:poeStatus.setStatus(_A)
_TotalPowerConsumption_Type=PowerTC
_TotalPowerConsumption_Object=MibScalar
totalPowerConsumption=_TotalPowerConsumption_Object((1,3,6,1,4,1,46242,6),_TotalPowerConsumption_Type())
totalPowerConsumption.setMaxAccess(_B)
if mibBuilder.loadTexts:totalPowerConsumption.setStatus(_A)
_DcdcInputCurrent_Type=CurrentTC
_DcdcInputCurrent_Object=MibScalar
dcdcInputCurrent=_DcdcInputCurrent_Object((1,3,6,1,4,1,46242,7),_DcdcInputCurrent_Type())
dcdcInputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:dcdcInputCurrent.setStatus(_A)
_DcdcEfficiency_Type=Integer32
_DcdcEfficiency_Object=MibScalar
dcdcEfficiency=_DcdcEfficiency_Object((1,3,6,1,4,1,46242,8),_DcdcEfficiency_Type())
dcdcEfficiency.setMaxAccess(_B)
if mibBuilder.loadTexts:dcdcEfficiency.setStatus(_A)
_NetonixSwitchConformance_ObjectIdentity=ObjectIdentity
netonixSwitchConformance=_NetonixSwitchConformance_ObjectIdentity((1,3,6,1,4,1,46242,99))
_NetonixSwitchGroups_ObjectIdentity=ObjectIdentity
netonixSwitchGroups=_NetonixSwitchGroups_ObjectIdentity((1,3,6,1,4,1,46242,99,1))
_NetonixSwitchCompliances_ObjectIdentity=ObjectIdentity
netonixSwitchCompliances=_NetonixSwitchCompliances_ObjectIdentity((1,3,6,1,4,1,46242,99,2))
netonixSwitchCompliance=ModuleCompliance((1,3,6,1,4,1,46242,99,2,1))
netonixSwitchCompliance.setObjects((_D,_G))
if mibBuilder.loadTexts:netonixSwitchCompliance.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'VoltageTC':VoltageTC,'PowerTC':PowerTC,'CurrentTC':CurrentTC,'netonixSwitch':netonixSwitch,'firmwareVersion':firmwareVersion,'fanTable':fanTable,'fanEntry':fanEntry,_H:fanIndex,'fanSpeed':fanSpeed,'tempTable':tempTable,'tempEntry':tempEntry,_I:tempIndex,'tempDescription':tempDescription,'temp':temp,'voltageTable':voltageTable,'voltageEntry':voltageEntry,_J:voltageIndex,'voltageDescription':voltageDescription,'voltage':voltage,'poeStatusTable':poeStatusTable,'poeStatusEntry':poeStatusEntry,_K:poeStatusIndex,'poeStatus':poeStatus,'totalPowerConsumption':totalPowerConsumption,'dcdcInputCurrent':dcdcInputCurrent,'dcdcEfficiency':dcdcEfficiency,'netonixSwitchConformance':netonixSwitchConformance,'netonixSwitchGroups':netonixSwitchGroups,'netonixSwitchCompliances':netonixSwitchCompliances,'netonixSwitchCompliance':netonixSwitchCompliance})