_d='heOpTxLaserMandatoryGroup'
_c='heOpTxUnitMandatoryGroup'
_b='heOpTxLaserOnOffControl'
_a='heOpTxLaserTECCurrent'
_Z='heOpTxLaserOutputPower'
_Y='heOpTxLaserBiasCurrent'
_X='heOpTxLaserTemp'
_W='heOpTxInputRFPadLevel'
_V='heOpTxInputModulationMode'
_U='heOpTxInputAGCMode'
_T='heOpTxInputModulatorBias'
_S='heOpTxInputRFPower'
_R='heOpTxUnitOnOffControl'
_Q='milli Amperes'
_P='heOpTxLaserIndex'
_O='0.1 dBm'
_N='not-accessible'
_M='heOpTxInputIndex'
_L='HeTenthCentigrade'
_K='heOpTxLaserOutputStatus'
_J='heOpTxLaserWavelength'
_I='heOpTxLaserType'
_H='heOpTxUnitOutputStatus'
_G='Integer32'
_F='entPhysicalIndex'
_E='ENTITY-MIB'
_D='read-write'
_C='read-only'
_B='SCTE-HMS-HE-OPTICAL-TRANSMITTER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_E,_F)
heOpticalTransmitterGroup,=mibBuilder.importSymbols('SCTE-HMS-HE-OPTICS-MIB','heOpticalTransmitterGroup')
HeHundredthNanoMeter,HeLaserType,HeOnOffControl,HeOnOffStatus,HeTenthCentigrade,HeTenthVolt,HeTenthdB,HeTenthdBm=mibBuilder.importSymbols('SCTE-HMS-HEADENDIDENT-MIB','HeHundredthNanoMeter','HeLaserType','HeOnOffControl','HeOnOffStatus',_L,'HeTenthVolt','HeTenthdB','HeTenthdBm')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
heOpticalTransmitterMIB=ModuleIdentity((1,3,6,1,4,1,5591,1,11,1,1,1))
_HeOpTxMIBObjects_ObjectIdentity=ObjectIdentity
heOpTxMIBObjects=_HeOpTxMIBObjects_ObjectIdentity((1,3,6,1,4,1,5591,1,11,1,1,1,1))
_HeOpTxUnitTable_Object=MibTable
heOpTxUnitTable=_HeOpTxUnitTable_Object((1,3,6,1,4,1,5591,1,11,1,1,1,1,1))
if mibBuilder.loadTexts:heOpTxUnitTable.setStatus(_A)
_HeOpTxUnitEntry_Object=MibTableRow
heOpTxUnitEntry=_HeOpTxUnitEntry_Object((1,3,6,1,4,1,5591,1,11,1,1,1,1,1,1))
heOpTxUnitEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:heOpTxUnitEntry.setStatus(_A)
_HeOpTxUnitOutputStatus_Type=HeOnOffStatus
_HeOpTxUnitOutputStatus_Object=MibTableColumn
heOpTxUnitOutputStatus=_HeOpTxUnitOutputStatus_Object((1,3,6,1,4,1,5591,1,11,1,1,1,1,1,1,1),_HeOpTxUnitOutputStatus_Type())
heOpTxUnitOutputStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpTxUnitOutputStatus.setStatus(_A)
_HeOpTxUnitOnOffControl_Type=HeOnOffControl
_HeOpTxUnitOnOffControl_Object=MibTableColumn
heOpTxUnitOnOffControl=_HeOpTxUnitOnOffControl_Object((1,3,6,1,4,1,5591,1,11,1,1,1,1,1,1,2),_HeOpTxUnitOnOffControl_Type())
heOpTxUnitOnOffControl.setMaxAccess(_D)
if mibBuilder.loadTexts:heOpTxUnitOnOffControl.setStatus(_A)
_HeOpTxInputTable_Object=MibTable
heOpTxInputTable=_HeOpTxInputTable_Object((1,3,6,1,4,1,5591,1,11,1,1,1,1,2))
if mibBuilder.loadTexts:heOpTxInputTable.setStatus(_A)
_HeOpTxInputEntry_Object=MibTableRow
heOpTxInputEntry=_HeOpTxInputEntry_Object((1,3,6,1,4,1,5591,1,11,1,1,1,1,2,1))
heOpTxInputEntry.setIndexNames((0,_E,_F),(0,_B,_M))
if mibBuilder.loadTexts:heOpTxInputEntry.setStatus(_A)
_HeOpTxInputIndex_Type=Unsigned32
_HeOpTxInputIndex_Object=MibTableColumn
heOpTxInputIndex=_HeOpTxInputIndex_Object((1,3,6,1,4,1,5591,1,11,1,1,1,1,2,1,1),_HeOpTxInputIndex_Type())
heOpTxInputIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:heOpTxInputIndex.setStatus(_A)
_HeOpTxInputRFPower_Type=HeTenthdBm
_HeOpTxInputRFPower_Object=MibTableColumn
heOpTxInputRFPower=_HeOpTxInputRFPower_Object((1,3,6,1,4,1,5591,1,11,1,1,1,1,2,1,2),_HeOpTxInputRFPower_Type())
heOpTxInputRFPower.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpTxInputRFPower.setStatus(_A)
if mibBuilder.loadTexts:heOpTxInputRFPower.setUnits(_O)
_HeOpTxInputModulatorBias_Type=HeTenthVolt
_HeOpTxInputModulatorBias_Object=MibTableColumn
heOpTxInputModulatorBias=_HeOpTxInputModulatorBias_Object((1,3,6,1,4,1,5591,1,11,1,1,1,1,2,1,3),_HeOpTxInputModulatorBias_Type())
heOpTxInputModulatorBias.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpTxInputModulatorBias.setStatus(_A)
if mibBuilder.loadTexts:heOpTxInputModulatorBias.setUnits('0.1 Volt')
_HeOpTxInputAGCMode_Type=HeOnOffStatus
_HeOpTxInputAGCMode_Object=MibTableColumn
heOpTxInputAGCMode=_HeOpTxInputAGCMode_Object((1,3,6,1,4,1,5591,1,11,1,1,1,1,2,1,4),_HeOpTxInputAGCMode_Type())
heOpTxInputAGCMode.setMaxAccess(_D)
if mibBuilder.loadTexts:heOpTxInputAGCMode.setStatus(_A)
class _HeOpTxInputModulationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cw',1),('modulated',2)))
_HeOpTxInputModulationMode_Type.__name__=_G
_HeOpTxInputModulationMode_Object=MibTableColumn
heOpTxInputModulationMode=_HeOpTxInputModulationMode_Object((1,3,6,1,4,1,5591,1,11,1,1,1,1,2,1,5),_HeOpTxInputModulationMode_Type())
heOpTxInputModulationMode.setMaxAccess(_D)
if mibBuilder.loadTexts:heOpTxInputModulationMode.setStatus(_A)
_HeOpTxInputRFPadLevel_Type=HeTenthdB
_HeOpTxInputRFPadLevel_Object=MibTableColumn
heOpTxInputRFPadLevel=_HeOpTxInputRFPadLevel_Object((1,3,6,1,4,1,5591,1,11,1,1,1,1,2,1,6),_HeOpTxInputRFPadLevel_Type())
heOpTxInputRFPadLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:heOpTxInputRFPadLevel.setStatus(_A)
if mibBuilder.loadTexts:heOpTxInputRFPadLevel.setUnits('0.1 dB')
_HeOpTxLaserTable_Object=MibTable
heOpTxLaserTable=_HeOpTxLaserTable_Object((1,3,6,1,4,1,5591,1,11,1,1,1,1,3))
if mibBuilder.loadTexts:heOpTxLaserTable.setStatus(_A)
_HeOpTxLaserEntry_Object=MibTableRow
heOpTxLaserEntry=_HeOpTxLaserEntry_Object((1,3,6,1,4,1,5591,1,11,1,1,1,1,3,1))
heOpTxLaserEntry.setIndexNames((0,_E,_F),(0,_B,_P))
if mibBuilder.loadTexts:heOpTxLaserEntry.setStatus(_A)
_HeOpTxLaserIndex_Type=Unsigned32
_HeOpTxLaserIndex_Object=MibTableColumn
heOpTxLaserIndex=_HeOpTxLaserIndex_Object((1,3,6,1,4,1,5591,1,11,1,1,1,1,3,1,1),_HeOpTxLaserIndex_Type())
heOpTxLaserIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:heOpTxLaserIndex.setStatus(_A)
class _HeOpTxLaserTemp_Type(HeTenthCentigrade):subtypeSpec=HeTenthCentigrade.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-250,1000))
_HeOpTxLaserTemp_Type.__name__=_L
_HeOpTxLaserTemp_Object=MibTableColumn
heOpTxLaserTemp=_HeOpTxLaserTemp_Object((1,3,6,1,4,1,5591,1,11,1,1,1,1,3,1,2),_HeOpTxLaserTemp_Type())
heOpTxLaserTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpTxLaserTemp.setStatus(_A)
if mibBuilder.loadTexts:heOpTxLaserTemp.setUnits('0.1 degrees Celsius')
class _HeOpTxLaserBiasCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HeOpTxLaserBiasCurrent_Type.__name__=_G
_HeOpTxLaserBiasCurrent_Object=MibTableColumn
heOpTxLaserBiasCurrent=_HeOpTxLaserBiasCurrent_Object((1,3,6,1,4,1,5591,1,11,1,1,1,1,3,1,3),_HeOpTxLaserBiasCurrent_Type())
heOpTxLaserBiasCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpTxLaserBiasCurrent.setStatus(_A)
if mibBuilder.loadTexts:heOpTxLaserBiasCurrent.setUnits(_Q)
_HeOpTxLaserOutputPower_Type=HeTenthdBm
_HeOpTxLaserOutputPower_Object=MibTableColumn
heOpTxLaserOutputPower=_HeOpTxLaserOutputPower_Object((1,3,6,1,4,1,5591,1,11,1,1,1,1,3,1,4),_HeOpTxLaserOutputPower_Type())
heOpTxLaserOutputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpTxLaserOutputPower.setStatus(_A)
if mibBuilder.loadTexts:heOpTxLaserOutputPower.setUnits(_O)
_HeOpTxLaserTECCurrent_Type=Integer32
_HeOpTxLaserTECCurrent_Object=MibTableColumn
heOpTxLaserTECCurrent=_HeOpTxLaserTECCurrent_Object((1,3,6,1,4,1,5591,1,11,1,1,1,1,3,1,5),_HeOpTxLaserTECCurrent_Type())
heOpTxLaserTECCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpTxLaserTECCurrent.setStatus(_A)
if mibBuilder.loadTexts:heOpTxLaserTECCurrent.setUnits(_Q)
_HeOpTxLaserType_Type=HeLaserType
_HeOpTxLaserType_Object=MibTableColumn
heOpTxLaserType=_HeOpTxLaserType_Object((1,3,6,1,4,1,5591,1,11,1,1,1,1,3,1,6),_HeOpTxLaserType_Type())
heOpTxLaserType.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpTxLaserType.setStatus(_A)
_HeOpTxLaserWavelength_Type=HeHundredthNanoMeter
_HeOpTxLaserWavelength_Object=MibTableColumn
heOpTxLaserWavelength=_HeOpTxLaserWavelength_Object((1,3,6,1,4,1,5591,1,11,1,1,1,1,3,1,7),_HeOpTxLaserWavelength_Type())
heOpTxLaserWavelength.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpTxLaserWavelength.setStatus(_A)
if mibBuilder.loadTexts:heOpTxLaserWavelength.setUnits('0.01 nanometer')
_HeOpTxLaserOutputStatus_Type=HeOnOffStatus
_HeOpTxLaserOutputStatus_Object=MibTableColumn
heOpTxLaserOutputStatus=_HeOpTxLaserOutputStatus_Object((1,3,6,1,4,1,5591,1,11,1,1,1,1,3,1,8),_HeOpTxLaserOutputStatus_Type())
heOpTxLaserOutputStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpTxLaserOutputStatus.setStatus(_A)
_HeOpTxLaserOnOffControl_Type=HeOnOffControl
_HeOpTxLaserOnOffControl_Object=MibTableColumn
heOpTxLaserOnOffControl=_HeOpTxLaserOnOffControl_Object((1,3,6,1,4,1,5591,1,11,1,1,1,1,3,1,9),_HeOpTxLaserOnOffControl_Type())
heOpTxLaserOnOffControl.setMaxAccess(_D)
if mibBuilder.loadTexts:heOpTxLaserOnOffControl.setStatus(_A)
_HeOpTxMIBConformance_ObjectIdentity=ObjectIdentity
heOpTxMIBConformance=_HeOpTxMIBConformance_ObjectIdentity((1,3,6,1,4,1,5591,1,11,1,1,1,2))
_HeOpTxMIBCompliances_ObjectIdentity=ObjectIdentity
heOpTxMIBCompliances=_HeOpTxMIBCompliances_ObjectIdentity((1,3,6,1,4,1,5591,1,11,1,1,1,2,1))
_HeOpTxMIBGroups_ObjectIdentity=ObjectIdentity
heOpTxMIBGroups=_HeOpTxMIBGroups_ObjectIdentity((1,3,6,1,4,1,5591,1,11,1,1,1,2,2))
heOpTxUnitMandatoryGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,1,1,1,2,2,1))
heOpTxUnitMandatoryGroup.setObjects((_B,_H))
if mibBuilder.loadTexts:heOpTxUnitMandatoryGroup.setStatus(_A)
heOpTxLaserMandatoryGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,1,1,1,2,2,2))
heOpTxLaserMandatoryGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:heOpTxLaserMandatoryGroup.setStatus(_A)
heOpTxUnitTableGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,1,1,1,2,2,3))
heOpTxUnitTableGroup.setObjects(*((_B,_H),(_B,_R)))
if mibBuilder.loadTexts:heOpTxUnitTableGroup.setStatus(_A)
heOpTxInputTableGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,1,1,1,2,2,4))
heOpTxInputTableGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:heOpTxInputTableGroup.setStatus(_A)
heOpTxLaserTableGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,1,1,1,2,2,5))
heOpTxLaserTableGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_I),(_B,_J),(_B,_K),(_B,_b)))
if mibBuilder.loadTexts:heOpTxLaserTableGroup.setStatus(_A)
heOpTxCompliance=ModuleCompliance((1,3,6,1,4,1,5591,1,11,1,1,1,2,1,1))
heOpTxCompliance.setObjects(*((_B,_c),(_B,_d)))
if mibBuilder.loadTexts:heOpTxCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'heOpticalTransmitterMIB':heOpticalTransmitterMIB,'heOpTxMIBObjects':heOpTxMIBObjects,'heOpTxUnitTable':heOpTxUnitTable,'heOpTxUnitEntry':heOpTxUnitEntry,_H:heOpTxUnitOutputStatus,_R:heOpTxUnitOnOffControl,'heOpTxInputTable':heOpTxInputTable,'heOpTxInputEntry':heOpTxInputEntry,_M:heOpTxInputIndex,_S:heOpTxInputRFPower,_T:heOpTxInputModulatorBias,_U:heOpTxInputAGCMode,_V:heOpTxInputModulationMode,_W:heOpTxInputRFPadLevel,'heOpTxLaserTable':heOpTxLaserTable,'heOpTxLaserEntry':heOpTxLaserEntry,_P:heOpTxLaserIndex,_X:heOpTxLaserTemp,_Y:heOpTxLaserBiasCurrent,_Z:heOpTxLaserOutputPower,_a:heOpTxLaserTECCurrent,_I:heOpTxLaserType,_J:heOpTxLaserWavelength,_K:heOpTxLaserOutputStatus,_b:heOpTxLaserOnOffControl,'heOpTxMIBConformance':heOpTxMIBConformance,'heOpTxMIBCompliances':heOpTxMIBCompliances,'heOpTxCompliance':heOpTxCompliance,'heOpTxMIBGroups':heOpTxMIBGroups,_c:heOpTxUnitMandatoryGroup,_d:heOpTxLaserMandatoryGroup,'heOpTxUnitTableGroup':heOpTxUnitTableGroup,'heOpTxInputTableGroup':heOpTxInputTableGroup,'heOpTxLaserTableGroup':heOpTxLaserTableGroup})