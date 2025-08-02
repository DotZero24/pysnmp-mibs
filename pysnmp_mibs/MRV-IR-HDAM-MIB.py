_V='irAnalogPointIndex'
_U='irAnalogSlotIndex'
_T='irAnalogPortIndex'
_S='irControlPointIndex'
_R='irControlSlotIndex'
_Q='irControlPortIndex'
_P='irAlarmPointIndex'
_O='irAlarmSlotIndex'
_N='irAlarmPortIndex'
_M='irHdamPowerIndex'
_L='irHdamSlotIndex'
_K='irHdamUnitPortIndex'
_J='off'
_I='irHdamPortIndex'
_H='enabled'
_G='disabled'
_F='MRV-IR-HDAM-MIB'
_E='DisplayString'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
TrapSeverity,=mibBuilder.importSymbols('MRV-IR-SYSTEM-MIB','TrapSeverity')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention')
irHdamMib=ModuleIdentity((1,3,6,1,4,1,33,100,4))
class IrHdamModuleType(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('empty',1),('alarmModule',2),('controlModule',3),('analoglModule',4)))
class IrContactState(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('open',1),('closed',2)))
class IrAnalogStatus(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_MrvBpd_ObjectIdentity=ObjectIdentity
mrvBpd=_MrvBpd_ObjectIdentity((1,3,6,1,4,1,33))
_MrvLx_ObjectIdentity=ObjectIdentity
mrvLx=_MrvLx_ObjectIdentity((1,3,6,1,4,1,33,100))
_IrHdam_ObjectIdentity=ObjectIdentity
irHdam=_IrHdam_ObjectIdentity((1,3,6,1,4,1,33,100,4,1))
_IrHdamUnitTable_Object=MibTable
irHdamUnitTable=_IrHdamUnitTable_Object((1,3,6,1,4,1,33,100,4,1,1))
if mibBuilder.loadTexts:irHdamUnitTable.setStatus(_A)
_IrHdamUnitEntry_Object=MibTableRow
irHdamUnitEntry=_IrHdamUnitEntry_Object((1,3,6,1,4,1,33,100,4,1,1,1))
irHdamUnitEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:irHdamUnitEntry.setStatus(_A)
_IrHdamUnitPortIndex_Type=Integer32
_IrHdamUnitPortIndex_Object=MibTableColumn
irHdamUnitPortIndex=_IrHdamUnitPortIndex_Object((1,3,6,1,4,1,33,100,4,1,1,1,1),_IrHdamUnitPortIndex_Type())
irHdamUnitPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:irHdamUnitPortIndex.setStatus(_A)
class _IrHdamFwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_IrHdamFwVersion_Type.__name__=_E
_IrHdamFwVersion_Object=MibTableColumn
irHdamFwVersion=_IrHdamFwVersion_Object((1,3,6,1,4,1,33,100,4,1,1,1,2),_IrHdamFwVersion_Type())
irHdamFwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:irHdamFwVersion.setStatus(_A)
class _IrHdamConnectStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('connected',1),('disconnected',2)))
_IrHdamConnectStatus_Type.__name__=_D
_IrHdamConnectStatus_Object=MibTableColumn
irHdamConnectStatus=_IrHdamConnectStatus_Object((1,3,6,1,4,1,33,100,4,1,1,1,3),_IrHdamConnectStatus_Type())
irHdamConnectStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:irHdamConnectStatus.setStatus(_A)
class _IrHdamPowerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('powerAC',1),('powerDC',2)))
_IrHdamPowerType_Type.__name__=_D
_IrHdamPowerType_Object=MibTableColumn
irHdamPowerType=_IrHdamPowerType_Object((1,3,6,1,4,1,33,100,4,1,1,1,4),_IrHdamPowerType_Type())
irHdamPowerType.setMaxAccess(_B)
if mibBuilder.loadTexts:irHdamPowerType.setStatus(_A)
class _IrHdamAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('reset',2)))
_IrHdamAction_Type.__name__=_D
_IrHdamAction_Object=MibTableColumn
irHdamAction=_IrHdamAction_Object((1,3,6,1,4,1,33,100,4,1,1,1,5),_IrHdamAction_Type())
irHdamAction.setMaxAccess(_C)
if mibBuilder.loadTexts:irHdamAction.setStatus(_A)
_IrHdamModuleTable_Object=MibTable
irHdamModuleTable=_IrHdamModuleTable_Object((1,3,6,1,4,1,33,100,4,1,2))
if mibBuilder.loadTexts:irHdamModuleTable.setStatus(_A)
_IrHdamModuleEntry_Object=MibTableRow
irHdamModuleEntry=_IrHdamModuleEntry_Object((1,3,6,1,4,1,33,100,4,1,2,1))
irHdamModuleEntry.setIndexNames((0,_F,_I),(0,_F,_L))
if mibBuilder.loadTexts:irHdamModuleEntry.setStatus(_A)
_IrHdamPortIndex_Type=Integer32
_IrHdamPortIndex_Object=MibTableColumn
irHdamPortIndex=_IrHdamPortIndex_Object((1,3,6,1,4,1,33,100,4,1,2,1,1),_IrHdamPortIndex_Type())
irHdamPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:irHdamPortIndex.setStatus(_A)
class _IrHdamSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_IrHdamSlotIndex_Type.__name__=_D
_IrHdamSlotIndex_Object=MibTableColumn
irHdamSlotIndex=_IrHdamSlotIndex_Object((1,3,6,1,4,1,33,100,4,1,2,1,2),_IrHdamSlotIndex_Type())
irHdamSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:irHdamSlotIndex.setStatus(_A)
_IrHdamModuleType_Type=IrHdamModuleType
_IrHdamModuleType_Object=MibTableColumn
irHdamModuleType=_IrHdamModuleType_Object((1,3,6,1,4,1,33,100,4,1,2,1,3),_IrHdamModuleType_Type())
irHdamModuleType.setMaxAccess(_B)
if mibBuilder.loadTexts:irHdamModuleType.setStatus(_A)
_IrHdamPowerSupplyTable_Object=MibTable
irHdamPowerSupplyTable=_IrHdamPowerSupplyTable_Object((1,3,6,1,4,1,33,100,4,1,3))
if mibBuilder.loadTexts:irHdamPowerSupplyTable.setStatus(_A)
_IrHdamPowerSupplyEntry_Object=MibTableRow
irHdamPowerSupplyEntry=_IrHdamPowerSupplyEntry_Object((1,3,6,1,4,1,33,100,4,1,3,1))
irHdamPowerSupplyEntry.setIndexNames((0,_F,_I),(0,_F,_M))
if mibBuilder.loadTexts:irHdamPowerSupplyEntry.setStatus(_A)
_IrHdamPowerPortIndex_Type=Integer32
_IrHdamPowerPortIndex_Object=MibTableColumn
irHdamPowerPortIndex=_IrHdamPowerPortIndex_Object((1,3,6,1,4,1,33,100,4,1,3,1,1),_IrHdamPowerPortIndex_Type())
irHdamPowerPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:irHdamPowerPortIndex.setStatus(_A)
class _IrHdamPowerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2))
_IrHdamPowerIndex_Type.__name__=_D
_IrHdamPowerIndex_Object=MibTableColumn
irHdamPowerIndex=_IrHdamPowerIndex_Object((1,3,6,1,4,1,33,100,4,1,3,1,2),_IrHdamPowerIndex_Type())
irHdamPowerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:irHdamPowerIndex.setStatus(_A)
class _IrHdamPowerUnitPresent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_IrHdamPowerUnitPresent_Type.__name__=_D
_IrHdamPowerUnitPresent_Object=MibTableColumn
irHdamPowerUnitPresent=_IrHdamPowerUnitPresent_Object((1,3,6,1,4,1,33,100,4,1,3,1,3),_IrHdamPowerUnitPresent_Type())
irHdamPowerUnitPresent.setMaxAccess(_B)
if mibBuilder.loadTexts:irHdamPowerUnitPresent.setStatus(_A)
class _IrHdamPowerInputStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_J,2)))
_IrHdamPowerInputStatus_Type.__name__=_D
_IrHdamPowerInputStatus_Object=MibTableColumn
irHdamPowerInputStatus=_IrHdamPowerInputStatus_Object((1,3,6,1,4,1,33,100,4,1,3,1,4),_IrHdamPowerInputStatus_Type())
irHdamPowerInputStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:irHdamPowerInputStatus.setStatus(_A)
class _IrHdamPowerOutputStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),(_J,2)))
_IrHdamPowerOutputStatus_Type.__name__=_D
_IrHdamPowerOutputStatus_Object=MibTableColumn
irHdamPowerOutputStatus=_IrHdamPowerOutputStatus_Object((1,3,6,1,4,1,33,100,4,1,3,1,5),_IrHdamPowerOutputStatus_Type())
irHdamPowerOutputStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:irHdamPowerOutputStatus.setStatus(_A)
class _IrHdamPowerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('on',1),(_J,2),('failed',3)))
_IrHdamPowerStatus_Type.__name__=_D
_IrHdamPowerStatus_Object=MibTableColumn
irHdamPowerStatus=_IrHdamPowerStatus_Object((1,3,6,1,4,1,33,100,4,1,3,1,6),_IrHdamPowerStatus_Type())
irHdamPowerStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:irHdamPowerStatus.setStatus(_A)
_IrHdamAlarm_ObjectIdentity=ObjectIdentity
irHdamAlarm=_IrHdamAlarm_ObjectIdentity((1,3,6,1,4,1,33,100,4,2))
_IrAlarmConfigTable_Object=MibTable
irAlarmConfigTable=_IrAlarmConfigTable_Object((1,3,6,1,4,1,33,100,4,2,1))
if mibBuilder.loadTexts:irAlarmConfigTable.setStatus(_A)
_IrAlarmConfigEntry_Object=MibTableRow
irAlarmConfigEntry=_IrAlarmConfigEntry_Object((1,3,6,1,4,1,33,100,4,2,1,1))
irAlarmConfigEntry.setIndexNames((0,_F,_N),(0,_F,_O),(0,_F,_P))
if mibBuilder.loadTexts:irAlarmConfigEntry.setStatus(_A)
class _IrAlarmPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_IrAlarmPortIndex_Type.__name__=_D
_IrAlarmPortIndex_Object=MibTableColumn
irAlarmPortIndex=_IrAlarmPortIndex_Object((1,3,6,1,4,1,33,100,4,2,1,1,1),_IrAlarmPortIndex_Type())
irAlarmPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:irAlarmPortIndex.setStatus(_A)
class _IrAlarmSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_IrAlarmSlotIndex_Type.__name__=_D
_IrAlarmSlotIndex_Object=MibTableColumn
irAlarmSlotIndex=_IrAlarmSlotIndex_Object((1,3,6,1,4,1,33,100,4,2,1,1,2),_IrAlarmSlotIndex_Type())
irAlarmSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:irAlarmSlotIndex.setStatus(_A)
class _IrAlarmPointIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_IrAlarmPointIndex_Type.__name__=_D
_IrAlarmPointIndex_Object=MibTableColumn
irAlarmPointIndex=_IrAlarmPointIndex_Object((1,3,6,1,4,1,33,100,4,2,1,1,3),_IrAlarmPointIndex_Type())
irAlarmPointIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:irAlarmPointIndex.setStatus(_A)
class _IrAlarmName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_IrAlarmName_Type.__name__=_E
_IrAlarmName_Object=MibTableColumn
irAlarmName=_IrAlarmName_Object((1,3,6,1,4,1,33,100,4,2,1,1,4),_IrAlarmName_Type())
irAlarmName.setMaxAccess(_C)
if mibBuilder.loadTexts:irAlarmName.setStatus(_A)
_IrAlarmContactState_Type=IrContactState
_IrAlarmContactState_Object=MibTableColumn
irAlarmContactState=_IrAlarmContactState_Object((1,3,6,1,4,1,33,100,4,2,1,1,5),_IrAlarmContactState_Type())
irAlarmContactState.setMaxAccess(_B)
if mibBuilder.loadTexts:irAlarmContactState.setStatus(_A)
_IrAlarmContactFaultState_Type=IrContactState
_IrAlarmContactFaultState_Object=MibTableColumn
irAlarmContactFaultState=_IrAlarmContactFaultState_Object((1,3,6,1,4,1,33,100,4,2,1,1,6),_IrAlarmContactFaultState_Type())
irAlarmContactFaultState.setMaxAccess(_C)
if mibBuilder.loadTexts:irAlarmContactFaultState.setStatus(_A)
class _IrAlarmDebounceInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1800))
_IrAlarmDebounceInterval_Type.__name__=_D
_IrAlarmDebounceInterval_Object=MibTableColumn
irAlarmDebounceInterval=_IrAlarmDebounceInterval_Object((1,3,6,1,4,1,33,100,4,2,1,1,7),_IrAlarmDebounceInterval_Type())
irAlarmDebounceInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:irAlarmDebounceInterval.setStatus(_A)
class _IrAlarmAudibleStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_IrAlarmAudibleStatus_Type.__name__=_D
_IrAlarmAudibleStatus_Object=MibTableColumn
irAlarmAudibleStatus=_IrAlarmAudibleStatus_Object((1,3,6,1,4,1,33,100,4,2,1,1,8),_IrAlarmAudibleStatus_Type())
irAlarmAudibleStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:irAlarmAudibleStatus.setStatus(_A)
class _IrAlarmTrapStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_IrAlarmTrapStatus_Type.__name__=_D
_IrAlarmTrapStatus_Object=MibTableColumn
irAlarmTrapStatus=_IrAlarmTrapStatus_Object((1,3,6,1,4,1,33,100,4,2,1,1,9),_IrAlarmTrapStatus_Type())
irAlarmTrapStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:irAlarmTrapStatus.setStatus(_A)
_IrAlarmTrapSeverity_Type=TrapSeverity
_IrAlarmTrapSeverity_Object=MibTableColumn
irAlarmTrapSeverity=_IrAlarmTrapSeverity_Object((1,3,6,1,4,1,33,100,4,2,1,1,10),_IrAlarmTrapSeverity_Type())
irAlarmTrapSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:irAlarmTrapSeverity.setStatus(_A)
_IrAlarmCount_Type=Counter32
_IrAlarmCount_Object=MibTableColumn
irAlarmCount=_IrAlarmCount_Object((1,3,6,1,4,1,33,100,4,2,1,1,11),_IrAlarmCount_Type())
irAlarmCount.setMaxAccess(_B)
if mibBuilder.loadTexts:irAlarmCount.setStatus(_A)
class _IrAlarmTimestamp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_IrAlarmTimestamp_Type.__name__=_E
_IrAlarmTimestamp_Object=MibTableColumn
irAlarmTimestamp=_IrAlarmTimestamp_Object((1,3,6,1,4,1,33,100,4,2,1,1,12),_IrAlarmTimestamp_Type())
irAlarmTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:irAlarmTimestamp.setStatus(_A)
class _IrAlarmDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_IrAlarmDescription_Type.__name__=_E
_IrAlarmDescription_Object=MibTableColumn
irAlarmDescription=_IrAlarmDescription_Object((1,3,6,1,4,1,33,100,4,2,1,1,13),_IrAlarmDescription_Type())
irAlarmDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:irAlarmDescription.setStatus(_A)
_IrHdamControl_ObjectIdentity=ObjectIdentity
irHdamControl=_IrHdamControl_ObjectIdentity((1,3,6,1,4,1,33,100,4,3))
_IrControlConfigTable_Object=MibTable
irControlConfigTable=_IrControlConfigTable_Object((1,3,6,1,4,1,33,100,4,3,1))
if mibBuilder.loadTexts:irControlConfigTable.setStatus(_A)
_IrControlConfigEntry_Object=MibTableRow
irControlConfigEntry=_IrControlConfigEntry_Object((1,3,6,1,4,1,33,100,4,3,1,1))
irControlConfigEntry.setIndexNames((0,_F,_Q),(0,_F,_R),(0,_F,_S))
if mibBuilder.loadTexts:irControlConfigEntry.setStatus(_A)
class _IrControlPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_IrControlPortIndex_Type.__name__=_D
_IrControlPortIndex_Object=MibTableColumn
irControlPortIndex=_IrControlPortIndex_Object((1,3,6,1,4,1,33,100,4,3,1,1,1),_IrControlPortIndex_Type())
irControlPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:irControlPortIndex.setStatus(_A)
class _IrControlSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_IrControlSlotIndex_Type.__name__=_D
_IrControlSlotIndex_Object=MibTableColumn
irControlSlotIndex=_IrControlSlotIndex_Object((1,3,6,1,4,1,33,100,4,3,1,1,2),_IrControlSlotIndex_Type())
irControlSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:irControlSlotIndex.setStatus(_A)
class _IrControlPointIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_IrControlPointIndex_Type.__name__=_D
_IrControlPointIndex_Object=MibTableColumn
irControlPointIndex=_IrControlPointIndex_Object((1,3,6,1,4,1,33,100,4,3,1,1,3),_IrControlPointIndex_Type())
irControlPointIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:irControlPointIndex.setStatus(_A)
class _IrControlName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_IrControlName_Type.__name__=_E
_IrControlName_Object=MibTableColumn
irControlName=_IrControlName_Object((1,3,6,1,4,1,33,100,4,3,1,1,4),_IrControlName_Type())
irControlName.setMaxAccess(_C)
if mibBuilder.loadTexts:irControlName.setStatus(_A)
_IrControlState_Type=IrContactState
_IrControlState_Object=MibTableColumn
irControlState=_IrControlState_Object((1,3,6,1,4,1,33,100,4,3,1,1,5),_IrControlState_Type())
irControlState.setMaxAccess(_C)
if mibBuilder.loadTexts:irControlState.setStatus(_A)
_IrControlActiveState_Type=IrContactState
_IrControlActiveState_Object=MibTableColumn
irControlActiveState=_IrControlActiveState_Object((1,3,6,1,4,1,33,100,4,3,1,1,6),_IrControlActiveState_Type())
irControlActiveState.setMaxAccess(_C)
if mibBuilder.loadTexts:irControlActiveState.setStatus(_A)
class _IrControlDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_IrControlDescription_Type.__name__=_E
_IrControlDescription_Object=MibTableColumn
irControlDescription=_IrControlDescription_Object((1,3,6,1,4,1,33,100,4,3,1,1,7),_IrControlDescription_Type())
irControlDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:irControlDescription.setStatus(_A)
_IrHdamAnalog_ObjectIdentity=ObjectIdentity
irHdamAnalog=_IrHdamAnalog_ObjectIdentity((1,3,6,1,4,1,33,100,4,4))
_IrAnalogConfigTable_Object=MibTable
irAnalogConfigTable=_IrAnalogConfigTable_Object((1,3,6,1,4,1,33,100,4,4,1))
if mibBuilder.loadTexts:irAnalogConfigTable.setStatus(_A)
_IrAnalogConfigEntry_Object=MibTableRow
irAnalogConfigEntry=_IrAnalogConfigEntry_Object((1,3,6,1,4,1,33,100,4,4,1,1))
irAnalogConfigEntry.setIndexNames((0,_F,_T),(0,_F,_U),(0,_F,_V))
if mibBuilder.loadTexts:irAnalogConfigEntry.setStatus(_A)
class _IrAnalogPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_IrAnalogPortIndex_Type.__name__=_D
_IrAnalogPortIndex_Object=MibTableColumn
irAnalogPortIndex=_IrAnalogPortIndex_Object((1,3,6,1,4,1,33,100,4,4,1,1,1),_IrAnalogPortIndex_Type())
irAnalogPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:irAnalogPortIndex.setStatus(_A)
class _IrAnalogSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_IrAnalogSlotIndex_Type.__name__=_D
_IrAnalogSlotIndex_Object=MibTableColumn
irAnalogSlotIndex=_IrAnalogSlotIndex_Object((1,3,6,1,4,1,33,100,4,4,1,1,2),_IrAnalogSlotIndex_Type())
irAnalogSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:irAnalogSlotIndex.setStatus(_A)
class _IrAnalogPointIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_IrAnalogPointIndex_Type.__name__=_D
_IrAnalogPointIndex_Object=MibTableColumn
irAnalogPointIndex=_IrAnalogPointIndex_Object((1,3,6,1,4,1,33,100,4,4,1,1,3),_IrAnalogPointIndex_Type())
irAnalogPointIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:irAnalogPointIndex.setStatus(_A)
class _IrAnalogName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_IrAnalogName_Type.__name__=_E
_IrAnalogName_Object=MibTableColumn
irAnalogName=_IrAnalogName_Object((1,3,6,1,4,1,33,100,4,4,1,1,4),_IrAnalogName_Type())
irAnalogName.setMaxAccess(_C)
if mibBuilder.loadTexts:irAnalogName.setStatus(_A)
class _IrAnalogDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_IrAnalogDescription_Type.__name__=_E
_IrAnalogDescription_Object=MibTableColumn
irAnalogDescription=_IrAnalogDescription_Object((1,3,6,1,4,1,33,100,4,4,1,1,5),_IrAnalogDescription_Type())
irAnalogDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:irAnalogDescription.setStatus(_A)
_IrAnalogStatus_Type=IrAnalogStatus
_IrAnalogStatus_Object=MibTableColumn
irAnalogStatus=_IrAnalogStatus_Object((1,3,6,1,4,1,33,100,4,4,1,1,6),_IrAnalogStatus_Type())
irAnalogStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:irAnalogStatus.setStatus(_A)
class _IrAnalogValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_IrAnalogValue_Type.__name__=_E
_IrAnalogValue_Object=MibTableColumn
irAnalogValue=_IrAnalogValue_Object((1,3,6,1,4,1,33,100,4,4,1,1,7),_IrAnalogValue_Type())
irAnalogValue.setMaxAccess(_B)
if mibBuilder.loadTexts:irAnalogValue.setStatus(_A)
class _IrAnalogCalValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_IrAnalogCalValue_Type.__name__=_E
_IrAnalogCalValue_Object=MibTableColumn
irAnalogCalValue=_IrAnalogCalValue_Object((1,3,6,1,4,1,33,100,4,4,1,1,8),_IrAnalogCalValue_Type())
irAnalogCalValue.setMaxAccess(_B)
if mibBuilder.loadTexts:irAnalogCalValue.setStatus(_A)
class _IrAnalogCalMinValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_IrAnalogCalMinValue_Type.__name__=_E
_IrAnalogCalMinValue_Object=MibTableColumn
irAnalogCalMinValue=_IrAnalogCalMinValue_Object((1,3,6,1,4,1,33,100,4,4,1,1,9),_IrAnalogCalMinValue_Type())
irAnalogCalMinValue.setMaxAccess(_C)
if mibBuilder.loadTexts:irAnalogCalMinValue.setStatus(_A)
class _IrAnalogCalMaxValue_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_IrAnalogCalMaxValue_Type.__name__=_E
_IrAnalogCalMaxValue_Object=MibTableColumn
irAnalogCalMaxValue=_IrAnalogCalMaxValue_Object((1,3,6,1,4,1,33,100,4,4,1,1,10),_IrAnalogCalMaxValue_Type())
irAnalogCalMaxValue.setMaxAccess(_C)
if mibBuilder.loadTexts:irAnalogCalMaxValue.setStatus(_A)
class _IrAnalogCalMargin_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_IrAnalogCalMargin_Type.__name__=_E
_IrAnalogCalMargin_Object=MibTableColumn
irAnalogCalMargin=_IrAnalogCalMargin_Object((1,3,6,1,4,1,33,100,4,4,1,1,11),_IrAnalogCalMargin_Type())
irAnalogCalMargin.setMaxAccess(_C)
if mibBuilder.loadTexts:irAnalogCalMargin.setStatus(_A)
class _IrAnalogCalUnits_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,8))
_IrAnalogCalUnits_Type.__name__=_E
_IrAnalogCalUnits_Object=MibTableColumn
irAnalogCalUnits=_IrAnalogCalUnits_Object((1,3,6,1,4,1,33,100,4,4,1,1,12),_IrAnalogCalUnits_Type())
irAnalogCalUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:irAnalogCalUnits.setStatus(_A)
class _IrAnalogThresholdHigh_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_IrAnalogThresholdHigh_Type.__name__=_E
_IrAnalogThresholdHigh_Object=MibTableColumn
irAnalogThresholdHigh=_IrAnalogThresholdHigh_Object((1,3,6,1,4,1,33,100,4,4,1,1,13),_IrAnalogThresholdHigh_Type())
irAnalogThresholdHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:irAnalogThresholdHigh.setStatus(_A)
class _IrAnalogThresholdLow_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_IrAnalogThresholdLow_Type.__name__=_E
_IrAnalogThresholdLow_Object=MibTableColumn
irAnalogThresholdLow=_IrAnalogThresholdLow_Object((1,3,6,1,4,1,33,100,4,4,1,1,14),_IrAnalogThresholdLow_Type())
irAnalogThresholdLow.setMaxAccess(_C)
if mibBuilder.loadTexts:irAnalogThresholdLow.setStatus(_A)
_IrAnalogThresholdSeverity_Type=TrapSeverity
_IrAnalogThresholdSeverity_Object=MibTableColumn
irAnalogThresholdSeverity=_IrAnalogThresholdSeverity_Object((1,3,6,1,4,1,33,100,4,4,1,1,15),_IrAnalogThresholdSeverity_Type())
irAnalogThresholdSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:irAnalogThresholdSeverity.setStatus(_A)
class _IrAnalogThresholdHysteresis_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_IrAnalogThresholdHysteresis_Type.__name__=_E
_IrAnalogThresholdHysteresis_Object=MibTableColumn
irAnalogThresholdHysteresis=_IrAnalogThresholdHysteresis_Object((1,3,6,1,4,1,33,100,4,4,1,1,16),_IrAnalogThresholdHysteresis_Type())
irAnalogThresholdHysteresis.setMaxAccess(_C)
if mibBuilder.loadTexts:irAnalogThresholdHysteresis.setStatus(_A)
_IrAnalogThresholdHighAlarmCount_Type=Counter32
_IrAnalogThresholdHighAlarmCount_Object=MibTableColumn
irAnalogThresholdHighAlarmCount=_IrAnalogThresholdHighAlarmCount_Object((1,3,6,1,4,1,33,100,4,4,1,1,17),_IrAnalogThresholdHighAlarmCount_Type())
irAnalogThresholdHighAlarmCount.setMaxAccess(_B)
if mibBuilder.loadTexts:irAnalogThresholdHighAlarmCount.setStatus(_A)
_IrAnalogThresholdLowAlarmCount_Type=Counter32
_IrAnalogThresholdLowAlarmCount_Object=MibTableColumn
irAnalogThresholdLowAlarmCount=_IrAnalogThresholdLowAlarmCount_Object((1,3,6,1,4,1,33,100,4,4,1,1,18),_IrAnalogThresholdLowAlarmCount_Type())
irAnalogThresholdLowAlarmCount.setMaxAccess(_B)
if mibBuilder.loadTexts:irAnalogThresholdLowAlarmCount.setStatus(_A)
class _IrAnalogThresholdHighTimestamp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_IrAnalogThresholdHighTimestamp_Type.__name__=_E
_IrAnalogThresholdHighTimestamp_Object=MibTableColumn
irAnalogThresholdHighTimestamp=_IrAnalogThresholdHighTimestamp_Object((1,3,6,1,4,1,33,100,4,4,1,1,19),_IrAnalogThresholdHighTimestamp_Type())
irAnalogThresholdHighTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:irAnalogThresholdHighTimestamp.setStatus(_A)
class _IrAnalogThresholdLowTimestamp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_IrAnalogThresholdLowTimestamp_Type.__name__=_E
_IrAnalogThresholdLowTimestamp_Object=MibTableColumn
irAnalogThresholdLowTimestamp=_IrAnalogThresholdLowTimestamp_Object((1,3,6,1,4,1,33,100,4,4,1,1,20),_IrAnalogThresholdLowTimestamp_Type())
irAnalogThresholdLowTimestamp.setMaxAccess(_B)
if mibBuilder.loadTexts:irAnalogThresholdLowTimestamp.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'IrHdamModuleType':IrHdamModuleType,'IrContactState':IrContactState,'IrAnalogStatus':IrAnalogStatus,'mrvBpd':mrvBpd,'mrvLx':mrvLx,'irHdamMib':irHdamMib,'irHdam':irHdam,'irHdamUnitTable':irHdamUnitTable,'irHdamUnitEntry':irHdamUnitEntry,_K:irHdamUnitPortIndex,'irHdamFwVersion':irHdamFwVersion,'irHdamConnectStatus':irHdamConnectStatus,'irHdamPowerType':irHdamPowerType,'irHdamAction':irHdamAction,'irHdamModuleTable':irHdamModuleTable,'irHdamModuleEntry':irHdamModuleEntry,_I:irHdamPortIndex,_L:irHdamSlotIndex,'irHdamModuleType':irHdamModuleType,'irHdamPowerSupplyTable':irHdamPowerSupplyTable,'irHdamPowerSupplyEntry':irHdamPowerSupplyEntry,'irHdamPowerPortIndex':irHdamPowerPortIndex,_M:irHdamPowerIndex,'irHdamPowerUnitPresent':irHdamPowerUnitPresent,'irHdamPowerInputStatus':irHdamPowerInputStatus,'irHdamPowerOutputStatus':irHdamPowerOutputStatus,'irHdamPowerStatus':irHdamPowerStatus,'irHdamAlarm':irHdamAlarm,'irAlarmConfigTable':irAlarmConfigTable,'irAlarmConfigEntry':irAlarmConfigEntry,_N:irAlarmPortIndex,_O:irAlarmSlotIndex,_P:irAlarmPointIndex,'irAlarmName':irAlarmName,'irAlarmContactState':irAlarmContactState,'irAlarmContactFaultState':irAlarmContactFaultState,'irAlarmDebounceInterval':irAlarmDebounceInterval,'irAlarmAudibleStatus':irAlarmAudibleStatus,'irAlarmTrapStatus':irAlarmTrapStatus,'irAlarmTrapSeverity':irAlarmTrapSeverity,'irAlarmCount':irAlarmCount,'irAlarmTimestamp':irAlarmTimestamp,'irAlarmDescription':irAlarmDescription,'irHdamControl':irHdamControl,'irControlConfigTable':irControlConfigTable,'irControlConfigEntry':irControlConfigEntry,_Q:irControlPortIndex,_R:irControlSlotIndex,_S:irControlPointIndex,'irControlName':irControlName,'irControlState':irControlState,'irControlActiveState':irControlActiveState,'irControlDescription':irControlDescription,'irHdamAnalog':irHdamAnalog,'irAnalogConfigTable':irAnalogConfigTable,'irAnalogConfigEntry':irAnalogConfigEntry,_T:irAnalogPortIndex,_U:irAnalogSlotIndex,_V:irAnalogPointIndex,'irAnalogName':irAnalogName,'irAnalogDescription':irAnalogDescription,'irAnalogStatus':irAnalogStatus,'irAnalogValue':irAnalogValue,'irAnalogCalValue':irAnalogCalValue,'irAnalogCalMinValue':irAnalogCalMinValue,'irAnalogCalMaxValue':irAnalogCalMaxValue,'irAnalogCalMargin':irAnalogCalMargin,'irAnalogCalUnits':irAnalogCalUnits,'irAnalogThresholdHigh':irAnalogThresholdHigh,'irAnalogThresholdLow':irAnalogThresholdLow,'irAnalogThresholdSeverity':irAnalogThresholdSeverity,'irAnalogThresholdHysteresis':irAnalogThresholdHysteresis,'irAnalogThresholdHighAlarmCount':irAnalogThresholdHighAlarmCount,'irAnalogThresholdLowAlarmCount':irAnalogThresholdLowAlarmCount,'irAnalogThresholdHighTimestamp':irAnalogThresholdHighTimestamp,'irAnalogThresholdLowTimestamp':irAnalogThresholdLowTimestamp})