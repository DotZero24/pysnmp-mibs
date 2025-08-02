_d='heOpSwitchOutputMandatoryGroup'
_c='heOpSwitchInputMandatoryGroup'
_b='heOpSwitchUnitMandatoryGroup'
_a='heOpSwitchSetInputPowerThreshold'
_Z='heOpSwitchInputOpticalLevel'
_Y='heOpSwitchWaitToRestoreTime'
_X='heOpSwitchHysteresis'
_W='heOpSwitchSelectWavelength'
_V='heOpSwitchBothInputStatus'
_U='heOpSwitchOutputDescription'
_T='heOpSwitchInputDescription'
_S='heOpSwitchInputStatus'
_R='heOpSwitchFailoverStatus'
_Q='heOpSwitchState'
_P='heOpSwitchRevertEnable'
_O='heOpSwitchControl'
_N='heOpSwitchMode'
_M='heOpSwitchOutputIndex'
_L='0.1 dBm'
_K='not-accessible'
_J='heOpSwitchInputIndex'
_I='HeTenthdB'
_H='DisplayString'
_G='Integer32'
_F='entPhysicalIndex'
_E='ENTITY-MIB'
_D='read-only'
_C='read-write'
_B='SCTE-HMS-HE-OPTICAL-SWITCH-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_E,_F)
heOpticalSwitchGroup,=mibBuilder.importSymbols('SCTE-HMS-HE-OPTICS-MIB','heOpticalSwitchGroup')
HeFaultStatus,HeHundredthNanoMeter,HeOnOffControl,HeTenthdB,HeTenthdBm=mibBuilder.importSymbols('SCTE-HMS-HEADENDIDENT-MIB','HeFaultStatus','HeHundredthNanoMeter','HeOnOffControl',_I,'HeTenthdBm')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_H,'PhysAddress','TextualConvention')
heOpticalSwitchMIB=ModuleIdentity((1,3,6,1,4,1,5591,1,11,1,4,1))
if mibBuilder.loadTexts:heOpticalSwitchMIB.setRevisions(('2003-09-11 00:00','2003-05-29 00:00','2003-04-25 00:00','2003-01-21 00:00','2002-12-04 00:00','2002-10-06 00:00','2002-09-25 00:00'))
_HeOpSwitchMIBObjects_ObjectIdentity=ObjectIdentity
heOpSwitchMIBObjects=_HeOpSwitchMIBObjects_ObjectIdentity((1,3,6,1,4,1,5591,1,11,1,4,1,1))
_HeOpSwitchUnitTable_Object=MibTable
heOpSwitchUnitTable=_HeOpSwitchUnitTable_Object((1,3,6,1,4,1,5591,1,11,1,4,1,1,1))
if mibBuilder.loadTexts:heOpSwitchUnitTable.setStatus(_A)
_HeOpSwitchUnitEntry_Object=MibTableRow
heOpSwitchUnitEntry=_HeOpSwitchUnitEntry_Object((1,3,6,1,4,1,5591,1,11,1,4,1,1,1,1))
heOpSwitchUnitEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:heOpSwitchUnitEntry.setStatus(_A)
class _HeOpSwitchMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('automatic',1),('manual',2)))
_HeOpSwitchMode_Type.__name__=_G
_HeOpSwitchMode_Object=MibTableColumn
heOpSwitchMode=_HeOpSwitchMode_Object((1,3,6,1,4,1,5591,1,11,1,4,1,1,1,1,1),_HeOpSwitchMode_Type())
heOpSwitchMode.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpSwitchMode.setStatus(_A)
class _HeOpSwitchControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('pathA',1),('pathB',2),('cross',3),('bar',4),('bothA',5),('bothB',6)))
_HeOpSwitchControl_Type.__name__=_G
_HeOpSwitchControl_Object=MibTableColumn
heOpSwitchControl=_HeOpSwitchControl_Object((1,3,6,1,4,1,5591,1,11,1,4,1,1,1,1,2),_HeOpSwitchControl_Type())
heOpSwitchControl.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpSwitchControl.setStatus(_A)
_HeOpSwitchRevertEnable_Type=HeOnOffControl
_HeOpSwitchRevertEnable_Object=MibTableColumn
heOpSwitchRevertEnable=_HeOpSwitchRevertEnable_Object((1,3,6,1,4,1,5591,1,11,1,4,1,1,1,1,3),_HeOpSwitchRevertEnable_Type())
heOpSwitchRevertEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpSwitchRevertEnable.setStatus(_A)
class _HeOpSwitchState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('pathA',1),('pathB',2),('cross',3),('bar',4),('bothA',5),('bothB',6)))
_HeOpSwitchState_Type.__name__=_G
_HeOpSwitchState_Object=MibTableColumn
heOpSwitchState=_HeOpSwitchState_Object((1,3,6,1,4,1,5591,1,11,1,4,1,1,1,1,4),_HeOpSwitchState_Type())
heOpSwitchState.setMaxAccess(_D)
if mibBuilder.loadTexts:heOpSwitchState.setStatus(_A)
_HeOpSwitchFailoverStatus_Type=HeFaultStatus
_HeOpSwitchFailoverStatus_Object=MibTableColumn
heOpSwitchFailoverStatus=_HeOpSwitchFailoverStatus_Object((1,3,6,1,4,1,5591,1,11,1,4,1,1,1,1,5),_HeOpSwitchFailoverStatus_Type())
heOpSwitchFailoverStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:heOpSwitchFailoverStatus.setStatus(_A)
_HeOpSwitchBothInputStatus_Type=HeFaultStatus
_HeOpSwitchBothInputStatus_Object=MibTableColumn
heOpSwitchBothInputStatus=_HeOpSwitchBothInputStatus_Object((1,3,6,1,4,1,5591,1,11,1,4,1,1,1,1,6),_HeOpSwitchBothInputStatus_Type())
heOpSwitchBothInputStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:heOpSwitchBothInputStatus.setStatus(_A)
_HeOpSwitchSelectWavelength_Type=HeHundredthNanoMeter
_HeOpSwitchSelectWavelength_Object=MibTableColumn
heOpSwitchSelectWavelength=_HeOpSwitchSelectWavelength_Object((1,3,6,1,4,1,5591,1,11,1,4,1,1,1,1,7),_HeOpSwitchSelectWavelength_Type())
heOpSwitchSelectWavelength.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpSwitchSelectWavelength.setStatus(_A)
if mibBuilder.loadTexts:heOpSwitchSelectWavelength.setUnits('0.01 nm')
class _HeOpSwitchHysteresis_Type(HeTenthdB):subtypeSpec=HeTenthdB.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-20,20))
_HeOpSwitchHysteresis_Type.__name__=_I
_HeOpSwitchHysteresis_Object=MibTableColumn
heOpSwitchHysteresis=_HeOpSwitchHysteresis_Object((1,3,6,1,4,1,5591,1,11,1,4,1,1,1,1,8),_HeOpSwitchHysteresis_Type())
heOpSwitchHysteresis.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpSwitchHysteresis.setStatus(_A)
if mibBuilder.loadTexts:heOpSwitchHysteresis.setUnits('0.1 dB')
_HeOpSwitchWaitToRestoreTime_Type=Integer32
_HeOpSwitchWaitToRestoreTime_Object=MibTableColumn
heOpSwitchWaitToRestoreTime=_HeOpSwitchWaitToRestoreTime_Object((1,3,6,1,4,1,5591,1,11,1,4,1,1,1,1,9),_HeOpSwitchWaitToRestoreTime_Type())
heOpSwitchWaitToRestoreTime.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpSwitchWaitToRestoreTime.setStatus(_A)
if mibBuilder.loadTexts:heOpSwitchWaitToRestoreTime.setUnits('1 sec')
_HeOpSwitchInputTable_Object=MibTable
heOpSwitchInputTable=_HeOpSwitchInputTable_Object((1,3,6,1,4,1,5591,1,11,1,4,1,1,2))
if mibBuilder.loadTexts:heOpSwitchInputTable.setStatus(_A)
_HeOpSwitchInputEntry_Object=MibTableRow
heOpSwitchInputEntry=_HeOpSwitchInputEntry_Object((1,3,6,1,4,1,5591,1,11,1,4,1,1,2,1))
heOpSwitchInputEntry.setIndexNames((0,_E,_F),(0,_B,_J))
if mibBuilder.loadTexts:heOpSwitchInputEntry.setStatus(_A)
_HeOpSwitchInputIndex_Type=Unsigned32
_HeOpSwitchInputIndex_Object=MibTableColumn
heOpSwitchInputIndex=_HeOpSwitchInputIndex_Object((1,3,6,1,4,1,5591,1,11,1,4,1,1,2,1,1),_HeOpSwitchInputIndex_Type())
heOpSwitchInputIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:heOpSwitchInputIndex.setStatus(_A)
_HeOpSwitchInputOpticalLevel_Type=HeTenthdBm
_HeOpSwitchInputOpticalLevel_Object=MibTableColumn
heOpSwitchInputOpticalLevel=_HeOpSwitchInputOpticalLevel_Object((1,3,6,1,4,1,5591,1,11,1,4,1,1,2,1,2),_HeOpSwitchInputOpticalLevel_Type())
heOpSwitchInputOpticalLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:heOpSwitchInputOpticalLevel.setStatus(_A)
if mibBuilder.loadTexts:heOpSwitchInputOpticalLevel.setUnits(_L)
_HeOpSwitchSetInputPowerThreshold_Type=HeTenthdBm
_HeOpSwitchSetInputPowerThreshold_Object=MibTableColumn
heOpSwitchSetInputPowerThreshold=_HeOpSwitchSetInputPowerThreshold_Object((1,3,6,1,4,1,5591,1,11,1,4,1,1,2,1,3),_HeOpSwitchSetInputPowerThreshold_Type())
heOpSwitchSetInputPowerThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpSwitchSetInputPowerThreshold.setStatus(_A)
if mibBuilder.loadTexts:heOpSwitchSetInputPowerThreshold.setUnits(_L)
_HeOpSwitchInputStatus_Type=HeFaultStatus
_HeOpSwitchInputStatus_Object=MibTableColumn
heOpSwitchInputStatus=_HeOpSwitchInputStatus_Object((1,3,6,1,4,1,5591,1,11,1,4,1,1,2,1,4),_HeOpSwitchInputStatus_Type())
heOpSwitchInputStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:heOpSwitchInputStatus.setStatus(_A)
class _HeOpSwitchInputDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HeOpSwitchInputDescription_Type.__name__=_H
_HeOpSwitchInputDescription_Object=MibTableColumn
heOpSwitchInputDescription=_HeOpSwitchInputDescription_Object((1,3,6,1,4,1,5591,1,11,1,4,1,1,2,1,5),_HeOpSwitchInputDescription_Type())
heOpSwitchInputDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:heOpSwitchInputDescription.setStatus(_A)
_HeOpSwitchOutputTable_Object=MibTable
heOpSwitchOutputTable=_HeOpSwitchOutputTable_Object((1,3,6,1,4,1,5591,1,11,1,4,1,1,3))
if mibBuilder.loadTexts:heOpSwitchOutputTable.setStatus(_A)
_HeOpSwitchOutputEntry_Object=MibTableRow
heOpSwitchOutputEntry=_HeOpSwitchOutputEntry_Object((1,3,6,1,4,1,5591,1,11,1,4,1,1,3,1))
heOpSwitchOutputEntry.setIndexNames((0,_E,_F),(0,_B,_M))
if mibBuilder.loadTexts:heOpSwitchOutputEntry.setStatus(_A)
_HeOpSwitchOutputIndex_Type=Unsigned32
_HeOpSwitchOutputIndex_Object=MibTableColumn
heOpSwitchOutputIndex=_HeOpSwitchOutputIndex_Object((1,3,6,1,4,1,5591,1,11,1,4,1,1,3,1,1),_HeOpSwitchOutputIndex_Type())
heOpSwitchOutputIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:heOpSwitchOutputIndex.setStatus(_A)
class _HeOpSwitchOutputDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HeOpSwitchOutputDescription_Type.__name__=_H
_HeOpSwitchOutputDescription_Object=MibTableColumn
heOpSwitchOutputDescription=_HeOpSwitchOutputDescription_Object((1,3,6,1,4,1,5591,1,11,1,4,1,1,3,1,2),_HeOpSwitchOutputDescription_Type())
heOpSwitchOutputDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:heOpSwitchOutputDescription.setStatus(_A)
_HeOpSwitchMIBConformance_ObjectIdentity=ObjectIdentity
heOpSwitchMIBConformance=_HeOpSwitchMIBConformance_ObjectIdentity((1,3,6,1,4,1,5591,1,11,1,4,1,2))
_HeOpSwitchMIBCompliances_ObjectIdentity=ObjectIdentity
heOpSwitchMIBCompliances=_HeOpSwitchMIBCompliances_ObjectIdentity((1,3,6,1,4,1,5591,1,11,1,4,1,2,1))
_HeOpSwitchMIBGroups_ObjectIdentity=ObjectIdentity
heOpSwitchMIBGroups=_HeOpSwitchMIBGroups_ObjectIdentity((1,3,6,1,4,1,5591,1,11,1,4,1,2,2))
heOpSwitchUnitMandatoryGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,1,4,1,2,2,1))
heOpSwitchUnitMandatoryGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:heOpSwitchUnitMandatoryGroup.setStatus(_A)
heOpSwitchInputMandatoryGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,1,4,1,2,2,2))
heOpSwitchInputMandatoryGroup.setObjects(*((_B,_S),(_B,_T)))
if mibBuilder.loadTexts:heOpSwitchInputMandatoryGroup.setStatus(_A)
heOpSwitchOutputMandatoryGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,1,4,1,2,2,3))
heOpSwitchOutputMandatoryGroup.setObjects((_B,_U))
if mibBuilder.loadTexts:heOpSwitchOutputMandatoryGroup.setStatus(_A)
heOpSwitchUnitGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,1,4,1,2,2,4))
heOpSwitchUnitGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:heOpSwitchUnitGroup.setStatus(_A)
heOpSwitchInputGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,1,4,1,2,2,5))
heOpSwitchInputGroup.setObjects(*((_B,_Z),(_B,_a)))
if mibBuilder.loadTexts:heOpSwitchInputGroup.setStatus(_A)
heOpSwitchBasicCompliance=ModuleCompliance((1,3,6,1,4,1,5591,1,11,1,4,1,2,1,1))
heOpSwitchBasicCompliance.setObjects(*((_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:heOpSwitchBasicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'heOpticalSwitchMIB':heOpticalSwitchMIB,'heOpSwitchMIBObjects':heOpSwitchMIBObjects,'heOpSwitchUnitTable':heOpSwitchUnitTable,'heOpSwitchUnitEntry':heOpSwitchUnitEntry,_N:heOpSwitchMode,_O:heOpSwitchControl,_P:heOpSwitchRevertEnable,_Q:heOpSwitchState,_R:heOpSwitchFailoverStatus,_V:heOpSwitchBothInputStatus,_W:heOpSwitchSelectWavelength,_X:heOpSwitchHysteresis,_Y:heOpSwitchWaitToRestoreTime,'heOpSwitchInputTable':heOpSwitchInputTable,'heOpSwitchInputEntry':heOpSwitchInputEntry,_J:heOpSwitchInputIndex,_Z:heOpSwitchInputOpticalLevel,_a:heOpSwitchSetInputPowerThreshold,_S:heOpSwitchInputStatus,_T:heOpSwitchInputDescription,'heOpSwitchOutputTable':heOpSwitchOutputTable,'heOpSwitchOutputEntry':heOpSwitchOutputEntry,_M:heOpSwitchOutputIndex,_U:heOpSwitchOutputDescription,'heOpSwitchMIBConformance':heOpSwitchMIBConformance,'heOpSwitchMIBCompliances':heOpSwitchMIBCompliances,'heOpSwitchBasicCompliance':heOpSwitchBasicCompliance,'heOpSwitchMIBGroups':heOpSwitchMIBGroups,_b:heOpSwitchUnitMandatoryGroup,_c:heOpSwitchInputMandatoryGroup,_d:heOpSwitchOutputMandatoryGroup,'heOpSwitchUnitGroup':heOpSwitchUnitGroup,'heOpSwitchInputGroup':heOpSwitchInputGroup})