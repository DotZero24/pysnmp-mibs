_e='heRFSwitchOutputMandatoryGroup'
_d='heRFSwitchInputMandatoryGroup'
_c='heRFSwitchUnitMandatoryGroup'
_b='heRFSwitchInputExternalControl'
_a='heRFSwitchSetInputPowerThreshold'
_Z='heRFSwitchInputRFLevel'
_Y='heRFSwitchSensorMode'
_X='heRFSwitchWaitToRestoreTime'
_W='heRFSwitchHysteresis'
_V='heRFSwitchBothInputStatus'
_U='heRFSwitchOutputDescription'
_T='heRFSwitchInputDescription'
_S='heRFSwitchInputStatus'
_R='heRFSwitchFailoverStatus'
_Q='heRFSwitchState'
_P='heRFSwitchRevertEnable'
_O='heRFSwitchControl'
_N='heRFSwitchMode'
_M='heRFSwitchOutputIndex'
_L='0.1 dBmV'
_K='not-accessible'
_J='heRFSwitchInputIndex'
_I='HeTenthdB'
_H='DisplayString'
_G='entPhysicalIndex'
_F='ENTITY-MIB'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='SCTE-HMS-HE-RF-SWITCH-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_F,_G)
heRFSwitchGroup,=mibBuilder.importSymbols('SCTE-HMS-HE-RF-MIB','heRFSwitchGroup')
HeFaultStatus,HeOnOffControl,HeTenthdB,HeTenthdBm,HeTenthdBmV=mibBuilder.importSymbols('SCTE-HMS-HEADENDIDENT-MIB','HeFaultStatus','HeOnOffControl',_I,'HeTenthdBm','HeTenthdBmV')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
heRFSwitchMIB=ModuleIdentity((1,3,6,1,4,1,5591,1,11,4,2,1))
if mibBuilder.loadTexts:heRFSwitchMIB.setRevisions(('2003-09-11 00:00','2003-05-29 00:00'))
_HeRFSwitchMIBObjects_ObjectIdentity=ObjectIdentity
heRFSwitchMIBObjects=_HeRFSwitchMIBObjects_ObjectIdentity((1,3,6,1,4,1,5591,1,11,4,2,1,1))
_HeRFSwitchUnitTable_Object=MibTable
heRFSwitchUnitTable=_HeRFSwitchUnitTable_Object((1,3,6,1,4,1,5591,1,11,4,2,1,1,1))
if mibBuilder.loadTexts:heRFSwitchUnitTable.setStatus(_A)
_HeRFSwitchUnitEntry_Object=MibTableRow
heRFSwitchUnitEntry=_HeRFSwitchUnitEntry_Object((1,3,6,1,4,1,5591,1,11,4,2,1,1,1,1))
heRFSwitchUnitEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:heRFSwitchUnitEntry.setStatus(_A)
class _HeRFSwitchMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('automatic',1),('manual',2)))
_HeRFSwitchMode_Type.__name__=_E
_HeRFSwitchMode_Object=MibTableColumn
heRFSwitchMode=_HeRFSwitchMode_Object((1,3,6,1,4,1,5591,1,11,4,2,1,1,1,1,1),_HeRFSwitchMode_Type())
heRFSwitchMode.setMaxAccess(_D)
if mibBuilder.loadTexts:heRFSwitchMode.setStatus(_A)
class _HeRFSwitchControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('pathA',1),('pathB',2),('cross',3),('bar',4),('bothA',5),('bothB',6)))
_HeRFSwitchControl_Type.__name__=_E
_HeRFSwitchControl_Object=MibTableColumn
heRFSwitchControl=_HeRFSwitchControl_Object((1,3,6,1,4,1,5591,1,11,4,2,1,1,1,1,2),_HeRFSwitchControl_Type())
heRFSwitchControl.setMaxAccess(_D)
if mibBuilder.loadTexts:heRFSwitchControl.setStatus(_A)
_HeRFSwitchRevertEnable_Type=HeOnOffControl
_HeRFSwitchRevertEnable_Object=MibTableColumn
heRFSwitchRevertEnable=_HeRFSwitchRevertEnable_Object((1,3,6,1,4,1,5591,1,11,4,2,1,1,1,1,3),_HeRFSwitchRevertEnable_Type())
heRFSwitchRevertEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:heRFSwitchRevertEnable.setStatus(_A)
class _HeRFSwitchState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('pathA',1),('pathB',2),('cross',3),('bar',4),('bothA',5),('bothB',6)))
_HeRFSwitchState_Type.__name__=_E
_HeRFSwitchState_Object=MibTableColumn
heRFSwitchState=_HeRFSwitchState_Object((1,3,6,1,4,1,5591,1,11,4,2,1,1,1,1,4),_HeRFSwitchState_Type())
heRFSwitchState.setMaxAccess(_C)
if mibBuilder.loadTexts:heRFSwitchState.setStatus(_A)
_HeRFSwitchFailoverStatus_Type=HeFaultStatus
_HeRFSwitchFailoverStatus_Object=MibTableColumn
heRFSwitchFailoverStatus=_HeRFSwitchFailoverStatus_Object((1,3,6,1,4,1,5591,1,11,4,2,1,1,1,1,5),_HeRFSwitchFailoverStatus_Type())
heRFSwitchFailoverStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:heRFSwitchFailoverStatus.setStatus(_A)
_HeRFSwitchBothInputStatus_Type=HeFaultStatus
_HeRFSwitchBothInputStatus_Object=MibTableColumn
heRFSwitchBothInputStatus=_HeRFSwitchBothInputStatus_Object((1,3,6,1,4,1,5591,1,11,4,2,1,1,1,1,6),_HeRFSwitchBothInputStatus_Type())
heRFSwitchBothInputStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:heRFSwitchBothInputStatus.setStatus(_A)
class _HeRFSwitchHysteresis_Type(HeTenthdB):subtypeSpec=HeTenthdB.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
_HeRFSwitchHysteresis_Type.__name__=_I
_HeRFSwitchHysteresis_Object=MibTableColumn
heRFSwitchHysteresis=_HeRFSwitchHysteresis_Object((1,3,6,1,4,1,5591,1,11,4,2,1,1,1,1,7),_HeRFSwitchHysteresis_Type())
heRFSwitchHysteresis.setMaxAccess(_D)
if mibBuilder.loadTexts:heRFSwitchHysteresis.setStatus(_A)
if mibBuilder.loadTexts:heRFSwitchHysteresis.setUnits('0.1 dB')
_HeRFSwitchWaitToRestoreTime_Type=Integer32
_HeRFSwitchWaitToRestoreTime_Object=MibTableColumn
heRFSwitchWaitToRestoreTime=_HeRFSwitchWaitToRestoreTime_Object((1,3,6,1,4,1,5591,1,11,4,2,1,1,1,1,8),_HeRFSwitchWaitToRestoreTime_Type())
heRFSwitchWaitToRestoreTime.setMaxAccess(_D)
if mibBuilder.loadTexts:heRFSwitchWaitToRestoreTime.setStatus(_A)
if mibBuilder.loadTexts:heRFSwitchWaitToRestoreTime.setUnits('1 sec')
class _HeRFSwitchSensorMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('internal',1),('external',2)))
_HeRFSwitchSensorMode_Type.__name__=_E
_HeRFSwitchSensorMode_Object=MibTableColumn
heRFSwitchSensorMode=_HeRFSwitchSensorMode_Object((1,3,6,1,4,1,5591,1,11,4,2,1,1,1,1,9),_HeRFSwitchSensorMode_Type())
heRFSwitchSensorMode.setMaxAccess(_D)
if mibBuilder.loadTexts:heRFSwitchSensorMode.setStatus(_A)
_HeRFSwitchInputTable_Object=MibTable
heRFSwitchInputTable=_HeRFSwitchInputTable_Object((1,3,6,1,4,1,5591,1,11,4,2,1,1,2))
if mibBuilder.loadTexts:heRFSwitchInputTable.setStatus(_A)
_HeRFSwitchInputEntry_Object=MibTableRow
heRFSwitchInputEntry=_HeRFSwitchInputEntry_Object((1,3,6,1,4,1,5591,1,11,4,2,1,1,2,1))
heRFSwitchInputEntry.setIndexNames((0,_F,_G),(0,_B,_J))
if mibBuilder.loadTexts:heRFSwitchInputEntry.setStatus(_A)
_HeRFSwitchInputIndex_Type=Unsigned32
_HeRFSwitchInputIndex_Object=MibTableColumn
heRFSwitchInputIndex=_HeRFSwitchInputIndex_Object((1,3,6,1,4,1,5591,1,11,4,2,1,1,2,1,1),_HeRFSwitchInputIndex_Type())
heRFSwitchInputIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:heRFSwitchInputIndex.setStatus(_A)
_HeRFSwitchInputRFLevel_Type=HeTenthdBmV
_HeRFSwitchInputRFLevel_Object=MibTableColumn
heRFSwitchInputRFLevel=_HeRFSwitchInputRFLevel_Object((1,3,6,1,4,1,5591,1,11,4,2,1,1,2,1,2),_HeRFSwitchInputRFLevel_Type())
heRFSwitchInputRFLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:heRFSwitchInputRFLevel.setStatus(_A)
if mibBuilder.loadTexts:heRFSwitchInputRFLevel.setUnits(_L)
_HeRFSwitchSetInputPowerThreshold_Type=HeTenthdBmV
_HeRFSwitchSetInputPowerThreshold_Object=MibTableColumn
heRFSwitchSetInputPowerThreshold=_HeRFSwitchSetInputPowerThreshold_Object((1,3,6,1,4,1,5591,1,11,4,2,1,1,2,1,3),_HeRFSwitchSetInputPowerThreshold_Type())
heRFSwitchSetInputPowerThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:heRFSwitchSetInputPowerThreshold.setStatus(_A)
if mibBuilder.loadTexts:heRFSwitchSetInputPowerThreshold.setUnits(_L)
_HeRFSwitchInputStatus_Type=HeFaultStatus
_HeRFSwitchInputStatus_Object=MibTableColumn
heRFSwitchInputStatus=_HeRFSwitchInputStatus_Object((1,3,6,1,4,1,5591,1,11,4,2,1,1,2,1,4),_HeRFSwitchInputStatus_Type())
heRFSwitchInputStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:heRFSwitchInputStatus.setStatus(_A)
class _HeRFSwitchInputDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HeRFSwitchInputDescription_Type.__name__=_H
_HeRFSwitchInputDescription_Object=MibTableColumn
heRFSwitchInputDescription=_HeRFSwitchInputDescription_Object((1,3,6,1,4,1,5591,1,11,4,2,1,1,2,1,5),_HeRFSwitchInputDescription_Type())
heRFSwitchInputDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:heRFSwitchInputDescription.setStatus(_A)
_HeRFSwitchInputExternalControl_Type=HeFaultStatus
_HeRFSwitchInputExternalControl_Object=MibTableColumn
heRFSwitchInputExternalControl=_HeRFSwitchInputExternalControl_Object((1,3,6,1,4,1,5591,1,11,4,2,1,1,2,1,6),_HeRFSwitchInputExternalControl_Type())
heRFSwitchInputExternalControl.setMaxAccess(_C)
if mibBuilder.loadTexts:heRFSwitchInputExternalControl.setStatus(_A)
_HeRFSwitchOutputTable_Object=MibTable
heRFSwitchOutputTable=_HeRFSwitchOutputTable_Object((1,3,6,1,4,1,5591,1,11,4,2,1,1,3))
if mibBuilder.loadTexts:heRFSwitchOutputTable.setStatus(_A)
_HeRFSwitchOutputEntry_Object=MibTableRow
heRFSwitchOutputEntry=_HeRFSwitchOutputEntry_Object((1,3,6,1,4,1,5591,1,11,4,2,1,1,3,1))
heRFSwitchOutputEntry.setIndexNames((0,_F,_G),(0,_B,_M))
if mibBuilder.loadTexts:heRFSwitchOutputEntry.setStatus(_A)
_HeRFSwitchOutputIndex_Type=Unsigned32
_HeRFSwitchOutputIndex_Object=MibTableColumn
heRFSwitchOutputIndex=_HeRFSwitchOutputIndex_Object((1,3,6,1,4,1,5591,1,11,4,2,1,1,3,1,1),_HeRFSwitchOutputIndex_Type())
heRFSwitchOutputIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:heRFSwitchOutputIndex.setStatus(_A)
class _HeRFSwitchOutputDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HeRFSwitchOutputDescription_Type.__name__=_H
_HeRFSwitchOutputDescription_Object=MibTableColumn
heRFSwitchOutputDescription=_HeRFSwitchOutputDescription_Object((1,3,6,1,4,1,5591,1,11,4,2,1,1,3,1,2),_HeRFSwitchOutputDescription_Type())
heRFSwitchOutputDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:heRFSwitchOutputDescription.setStatus(_A)
_HeRFSwitchMIBConformance_ObjectIdentity=ObjectIdentity
heRFSwitchMIBConformance=_HeRFSwitchMIBConformance_ObjectIdentity((1,3,6,1,4,1,5591,1,11,4,2,1,2))
_HeRFSwitchMIBCompliances_ObjectIdentity=ObjectIdentity
heRFSwitchMIBCompliances=_HeRFSwitchMIBCompliances_ObjectIdentity((1,3,6,1,4,1,5591,1,11,4,2,1,2,1))
_HeRFSwitchMIBGroups_ObjectIdentity=ObjectIdentity
heRFSwitchMIBGroups=_HeRFSwitchMIBGroups_ObjectIdentity((1,3,6,1,4,1,5591,1,11,4,2,1,2,2))
heRFSwitchUnitMandatoryGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,4,2,1,2,2,1))
heRFSwitchUnitMandatoryGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:heRFSwitchUnitMandatoryGroup.setStatus(_A)
heRFSwitchInputMandatoryGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,4,2,1,2,2,2))
heRFSwitchInputMandatoryGroup.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:heRFSwitchInputMandatoryGroup.setStatus(_A)
heRFSwitchOutputMandatoryGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,4,2,1,2,2,3))
heRFSwitchOutputMandatoryGroup.setObjects((_B,_U))
if mibBuilder.loadTexts:heRFSwitchOutputMandatoryGroup.setStatus(_A)
heRFSwitchUnitGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,4,2,1,2,2,4))
heRFSwitchUnitGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:heRFSwitchUnitGroup.setStatus(_A)
heRFSwitchInputGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,4,2,1,2,2,5))
heRFSwitchInputGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:heRFSwitchInputGroup.setStatus(_A)
heRFSwitchBasicCompliance=ModuleCompliance((1,3,6,1,4,1,5591,1,11,4,2,1,2,1,1))
heRFSwitchBasicCompliance.setObjects(*((_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:heRFSwitchBasicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'heRFSwitchMIB':heRFSwitchMIB,'heRFSwitchMIBObjects':heRFSwitchMIBObjects,'heRFSwitchUnitTable':heRFSwitchUnitTable,'heRFSwitchUnitEntry':heRFSwitchUnitEntry,_N:heRFSwitchMode,_O:heRFSwitchControl,_P:heRFSwitchRevertEnable,_Q:heRFSwitchState,_R:heRFSwitchFailoverStatus,_V:heRFSwitchBothInputStatus,_W:heRFSwitchHysteresis,_X:heRFSwitchWaitToRestoreTime,_Y:heRFSwitchSensorMode,'heRFSwitchInputTable':heRFSwitchInputTable,'heRFSwitchInputEntry':heRFSwitchInputEntry,_J:heRFSwitchInputIndex,_Z:heRFSwitchInputRFLevel,_a:heRFSwitchSetInputPowerThreshold,_S:heRFSwitchInputStatus,_T:heRFSwitchInputDescription,_b:heRFSwitchInputExternalControl,'heRFSwitchOutputTable':heRFSwitchOutputTable,'heRFSwitchOutputEntry':heRFSwitchOutputEntry,_M:heRFSwitchOutputIndex,_U:heRFSwitchOutputDescription,'heRFSwitchMIBConformance':heRFSwitchMIBConformance,'heRFSwitchMIBCompliances':heRFSwitchMIBCompliances,'heRFSwitchBasicCompliance':heRFSwitchBasicCompliance,'heRFSwitchMIBGroups':heRFSwitchMIBGroups,_c:heRFSwitchUnitMandatoryGroup,_d:heRFSwitchInputMandatoryGroup,_e:heRFSwitchOutputMandatoryGroup,'heRFSwitchUnitGroup':heRFSwitchUnitGroup,'heRFSwitchInputGroup':heRFSwitchInputGroup})