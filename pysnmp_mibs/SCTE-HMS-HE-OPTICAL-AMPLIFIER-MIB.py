_f='heOpAmpOutputTableGroup'
_e='heOpAmpLaserTableGroup'
_d='heOpAmpInputTableGroup'
_c='heOpAmpUnitTableGroup'
_b='heOpAmpOutputMandatoryGroup'
_a='heOpAmpInputMandatoryGroup'
_Z='heOpAmpUnitMandatoryGroup'
_Y='heOpAmpOutputGainType'
_X='heOpAmpGainPerWavelength'
_W='heOpAmpSetOpticalOutputPower'
_V='heOpAmpLaserType'
_U='heOpAmpLaserTECCurrent'
_T='heOpAmpLaserOutputPower'
_S='heOpAmpLaserBiasCurrent'
_R='heOpAmpLaserTemp'
_Q='heOpAmpUnitOnOffControl'
_P='heOpAmpOutputIndex'
_O='1.0 mA'
_N='heOpAmpLaserIndex'
_M='heOpAmpInputIndex'
_L='Integer32'
_K='heOpAmpOutputPower'
_J='heOpAmpInputPower'
_I='heOpAmpUnitOutputStatus'
_H='not-accessible'
_G='read-write'
_F='0.1 dBm'
_E='entPhysicalIndex'
_D='ENTITY-MIB'
_C='read-only'
_B='SCTE-HMS-HE-OPTICAL-AMPLIFIER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
heOpticalAmplifierGroup,=mibBuilder.importSymbols('SCTE-HMS-HE-OPTICS-MIB','heOpticalAmplifierGroup')
HeLaserType,HeMilliAmp,HeOnOffControl,HeOnOffStatus,HeTenthCentigrade,HeTenthdB,HeTenthdBm=mibBuilder.importSymbols('SCTE-HMS-HEADENDIDENT-MIB','HeLaserType','HeMilliAmp','HeOnOffControl','HeOnOffStatus','HeTenthCentigrade','HeTenthdB','HeTenthdBm')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_L,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
heOpticalAmplifierMIB=ModuleIdentity((1,3,6,1,4,1,5591,1,11,1,3,1))
_HeOpAmpMIBObjects_ObjectIdentity=ObjectIdentity
heOpAmpMIBObjects=_HeOpAmpMIBObjects_ObjectIdentity((1,3,6,1,4,1,5591,1,11,1,3,1,1))
_HeOpAmpUnitTable_Object=MibTable
heOpAmpUnitTable=_HeOpAmpUnitTable_Object((1,3,6,1,4,1,5591,1,11,1,3,1,1,1))
if mibBuilder.loadTexts:heOpAmpUnitTable.setStatus(_A)
_HeOpAmpUnitEntry_Object=MibTableRow
heOpAmpUnitEntry=_HeOpAmpUnitEntry_Object((1,3,6,1,4,1,5591,1,11,1,3,1,1,1,1))
heOpAmpUnitEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:heOpAmpUnitEntry.setStatus(_A)
_HeOpAmpUnitOutputStatus_Type=HeOnOffStatus
_HeOpAmpUnitOutputStatus_Object=MibTableColumn
heOpAmpUnitOutputStatus=_HeOpAmpUnitOutputStatus_Object((1,3,6,1,4,1,5591,1,11,1,3,1,1,1,1,1),_HeOpAmpUnitOutputStatus_Type())
heOpAmpUnitOutputStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpAmpUnitOutputStatus.setStatus(_A)
_HeOpAmpUnitOnOffControl_Type=HeOnOffControl
_HeOpAmpUnitOnOffControl_Object=MibTableColumn
heOpAmpUnitOnOffControl=_HeOpAmpUnitOnOffControl_Object((1,3,6,1,4,1,5591,1,11,1,3,1,1,1,1,2),_HeOpAmpUnitOnOffControl_Type())
heOpAmpUnitOnOffControl.setMaxAccess(_G)
if mibBuilder.loadTexts:heOpAmpUnitOnOffControl.setStatus(_A)
_HeOpAmpInputTable_Object=MibTable
heOpAmpInputTable=_HeOpAmpInputTable_Object((1,3,6,1,4,1,5591,1,11,1,3,1,1,2))
if mibBuilder.loadTexts:heOpAmpInputTable.setStatus(_A)
_HeOpAmpInputEntry_Object=MibTableRow
heOpAmpInputEntry=_HeOpAmpInputEntry_Object((1,3,6,1,4,1,5591,1,11,1,3,1,1,2,1))
heOpAmpInputEntry.setIndexNames((0,_D,_E),(0,_B,_M))
if mibBuilder.loadTexts:heOpAmpInputEntry.setStatus(_A)
_HeOpAmpInputIndex_Type=Unsigned32
_HeOpAmpInputIndex_Object=MibTableColumn
heOpAmpInputIndex=_HeOpAmpInputIndex_Object((1,3,6,1,4,1,5591,1,11,1,3,1,1,2,1,1),_HeOpAmpInputIndex_Type())
heOpAmpInputIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:heOpAmpInputIndex.setStatus(_A)
_HeOpAmpInputPower_Type=HeTenthdBm
_HeOpAmpInputPower_Object=MibTableColumn
heOpAmpInputPower=_HeOpAmpInputPower_Object((1,3,6,1,4,1,5591,1,11,1,3,1,1,2,1,2),_HeOpAmpInputPower_Type())
heOpAmpInputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpAmpInputPower.setStatus(_A)
if mibBuilder.loadTexts:heOpAmpInputPower.setUnits(_F)
_HeOpAmpLaserTable_Object=MibTable
heOpAmpLaserTable=_HeOpAmpLaserTable_Object((1,3,6,1,4,1,5591,1,11,1,3,1,1,3))
if mibBuilder.loadTexts:heOpAmpLaserTable.setStatus(_A)
_HeOpAmpLaserEntry_Object=MibTableRow
heOpAmpLaserEntry=_HeOpAmpLaserEntry_Object((1,3,6,1,4,1,5591,1,11,1,3,1,1,3,1))
heOpAmpLaserEntry.setIndexNames((0,_D,_E),(0,_B,_N))
if mibBuilder.loadTexts:heOpAmpLaserEntry.setStatus(_A)
_HeOpAmpLaserIndex_Type=Unsigned32
_HeOpAmpLaserIndex_Object=MibTableColumn
heOpAmpLaserIndex=_HeOpAmpLaserIndex_Object((1,3,6,1,4,1,5591,1,11,1,3,1,1,3,1,1),_HeOpAmpLaserIndex_Type())
heOpAmpLaserIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:heOpAmpLaserIndex.setStatus(_A)
_HeOpAmpLaserTemp_Type=HeTenthCentigrade
_HeOpAmpLaserTemp_Object=MibTableColumn
heOpAmpLaserTemp=_HeOpAmpLaserTemp_Object((1,3,6,1,4,1,5591,1,11,1,3,1,1,3,1,2),_HeOpAmpLaserTemp_Type())
heOpAmpLaserTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpAmpLaserTemp.setStatus(_A)
if mibBuilder.loadTexts:heOpAmpLaserTemp.setUnits('0.1 degrees Celsius')
_HeOpAmpLaserBiasCurrent_Type=HeMilliAmp
_HeOpAmpLaserBiasCurrent_Object=MibTableColumn
heOpAmpLaserBiasCurrent=_HeOpAmpLaserBiasCurrent_Object((1,3,6,1,4,1,5591,1,11,1,3,1,1,3,1,3),_HeOpAmpLaserBiasCurrent_Type())
heOpAmpLaserBiasCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpAmpLaserBiasCurrent.setStatus(_A)
if mibBuilder.loadTexts:heOpAmpLaserBiasCurrent.setUnits(_O)
_HeOpAmpLaserOutputPower_Type=HeTenthdBm
_HeOpAmpLaserOutputPower_Object=MibTableColumn
heOpAmpLaserOutputPower=_HeOpAmpLaserOutputPower_Object((1,3,6,1,4,1,5591,1,11,1,3,1,1,3,1,4),_HeOpAmpLaserOutputPower_Type())
heOpAmpLaserOutputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpAmpLaserOutputPower.setStatus(_A)
if mibBuilder.loadTexts:heOpAmpLaserOutputPower.setUnits(_F)
_HeOpAmpLaserTECCurrent_Type=HeMilliAmp
_HeOpAmpLaserTECCurrent_Object=MibTableColumn
heOpAmpLaserTECCurrent=_HeOpAmpLaserTECCurrent_Object((1,3,6,1,4,1,5591,1,11,1,3,1,1,3,1,5),_HeOpAmpLaserTECCurrent_Type())
heOpAmpLaserTECCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpAmpLaserTECCurrent.setStatus(_A)
if mibBuilder.loadTexts:heOpAmpLaserTECCurrent.setUnits(_O)
_HeOpAmpLaserType_Type=HeLaserType
_HeOpAmpLaserType_Object=MibTableColumn
heOpAmpLaserType=_HeOpAmpLaserType_Object((1,3,6,1,4,1,5591,1,11,1,3,1,1,3,1,6),_HeOpAmpLaserType_Type())
heOpAmpLaserType.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpAmpLaserType.setStatus(_A)
_HeOpAmpOutputTable_Object=MibTable
heOpAmpOutputTable=_HeOpAmpOutputTable_Object((1,3,6,1,4,1,5591,1,11,1,3,1,1,4))
if mibBuilder.loadTexts:heOpAmpOutputTable.setStatus(_A)
_HeOpAmpOutputEntry_Object=MibTableRow
heOpAmpOutputEntry=_HeOpAmpOutputEntry_Object((1,3,6,1,4,1,5591,1,11,1,3,1,1,4,1))
heOpAmpOutputEntry.setIndexNames((0,_D,_E),(0,_B,_P))
if mibBuilder.loadTexts:heOpAmpOutputEntry.setStatus(_A)
_HeOpAmpOutputIndex_Type=Unsigned32
_HeOpAmpOutputIndex_Object=MibTableColumn
heOpAmpOutputIndex=_HeOpAmpOutputIndex_Object((1,3,6,1,4,1,5591,1,11,1,3,1,1,4,1,1),_HeOpAmpOutputIndex_Type())
heOpAmpOutputIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:heOpAmpOutputIndex.setStatus(_A)
_HeOpAmpSetOpticalOutputPower_Type=HeTenthdBm
_HeOpAmpSetOpticalOutputPower_Object=MibTableColumn
heOpAmpSetOpticalOutputPower=_HeOpAmpSetOpticalOutputPower_Object((1,3,6,1,4,1,5591,1,11,1,3,1,1,4,1,2),_HeOpAmpSetOpticalOutputPower_Type())
heOpAmpSetOpticalOutputPower.setMaxAccess(_G)
if mibBuilder.loadTexts:heOpAmpSetOpticalOutputPower.setStatus(_A)
if mibBuilder.loadTexts:heOpAmpSetOpticalOutputPower.setUnits(_F)
_HeOpAmpGainPerWavelength_Type=HeTenthdB
_HeOpAmpGainPerWavelength_Object=MibTableColumn
heOpAmpGainPerWavelength=_HeOpAmpGainPerWavelength_Object((1,3,6,1,4,1,5591,1,11,1,3,1,1,4,1,3),_HeOpAmpGainPerWavelength_Type())
heOpAmpGainPerWavelength.setMaxAccess(_G)
if mibBuilder.loadTexts:heOpAmpGainPerWavelength.setStatus(_A)
if mibBuilder.loadTexts:heOpAmpGainPerWavelength.setUnits(_F)
_HeOpAmpOutputPower_Type=HeTenthdBm
_HeOpAmpOutputPower_Object=MibTableColumn
heOpAmpOutputPower=_HeOpAmpOutputPower_Object((1,3,6,1,4,1,5591,1,11,1,3,1,1,4,1,4),_HeOpAmpOutputPower_Type())
heOpAmpOutputPower.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpAmpOutputPower.setStatus(_A)
if mibBuilder.loadTexts:heOpAmpOutputPower.setUnits(_F)
class _HeOpAmpOutputGainType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('constantPower',1),('constantGain',2)))
_HeOpAmpOutputGainType_Type.__name__=_L
_HeOpAmpOutputGainType_Object=MibTableColumn
heOpAmpOutputGainType=_HeOpAmpOutputGainType_Object((1,3,6,1,4,1,5591,1,11,1,3,1,1,4,1,5),_HeOpAmpOutputGainType_Type())
heOpAmpOutputGainType.setMaxAccess(_G)
if mibBuilder.loadTexts:heOpAmpOutputGainType.setStatus(_A)
_HeOpAmpMIBConformance_ObjectIdentity=ObjectIdentity
heOpAmpMIBConformance=_HeOpAmpMIBConformance_ObjectIdentity((1,3,6,1,4,1,5591,1,11,1,3,1,2))
_HeOpAmpMIBCompliances_ObjectIdentity=ObjectIdentity
heOpAmpMIBCompliances=_HeOpAmpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,5591,1,11,1,3,1,2,1))
_HeOpAmpMIBGroups_ObjectIdentity=ObjectIdentity
heOpAmpMIBGroups=_HeOpAmpMIBGroups_ObjectIdentity((1,3,6,1,4,1,5591,1,11,1,3,1,2,2))
heOpAmpUnitMandatoryGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,1,3,1,2,2,1))
heOpAmpUnitMandatoryGroup.setObjects((_B,_I))
if mibBuilder.loadTexts:heOpAmpUnitMandatoryGroup.setStatus(_A)
heOpAmpInputMandatoryGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,1,3,1,2,2,2))
heOpAmpInputMandatoryGroup.setObjects((_B,_J))
if mibBuilder.loadTexts:heOpAmpInputMandatoryGroup.setStatus(_A)
heOpAmpOutputMandatoryGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,1,3,1,2,2,3))
heOpAmpOutputMandatoryGroup.setObjects((_B,_K))
if mibBuilder.loadTexts:heOpAmpOutputMandatoryGroup.setStatus(_A)
heOpAmpUnitTableGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,1,3,1,2,2,4))
heOpAmpUnitTableGroup.setObjects(*((_B,_I),(_B,_Q)))
if mibBuilder.loadTexts:heOpAmpUnitTableGroup.setStatus(_A)
heOpAmpInputTableGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,1,3,1,2,2,5))
heOpAmpInputTableGroup.setObjects((_B,_J))
if mibBuilder.loadTexts:heOpAmpInputTableGroup.setStatus(_A)
heOpAmpLaserTableGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,1,3,1,2,2,6))
heOpAmpLaserTableGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V)))
if mibBuilder.loadTexts:heOpAmpLaserTableGroup.setStatus(_A)
heOpAmpOutputTableGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,1,3,1,2,2,7))
heOpAmpOutputTableGroup.setObjects(*((_B,_W),(_B,_X),(_B,_K),(_B,_Y)))
if mibBuilder.loadTexts:heOpAmpOutputTableGroup.setStatus(_A)
heOpAmpCompliance=ModuleCompliance((1,3,6,1,4,1,5591,1,11,1,3,1,2,1,1))
heOpAmpCompliance.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:heOpAmpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'heOpticalAmplifierMIB':heOpticalAmplifierMIB,'heOpAmpMIBObjects':heOpAmpMIBObjects,'heOpAmpUnitTable':heOpAmpUnitTable,'heOpAmpUnitEntry':heOpAmpUnitEntry,_I:heOpAmpUnitOutputStatus,_Q:heOpAmpUnitOnOffControl,'heOpAmpInputTable':heOpAmpInputTable,'heOpAmpInputEntry':heOpAmpInputEntry,_M:heOpAmpInputIndex,_J:heOpAmpInputPower,'heOpAmpLaserTable':heOpAmpLaserTable,'heOpAmpLaserEntry':heOpAmpLaserEntry,_N:heOpAmpLaserIndex,_R:heOpAmpLaserTemp,_S:heOpAmpLaserBiasCurrent,_T:heOpAmpLaserOutputPower,_U:heOpAmpLaserTECCurrent,_V:heOpAmpLaserType,'heOpAmpOutputTable':heOpAmpOutputTable,'heOpAmpOutputEntry':heOpAmpOutputEntry,_P:heOpAmpOutputIndex,_W:heOpAmpSetOpticalOutputPower,_X:heOpAmpGainPerWavelength,_K:heOpAmpOutputPower,_Y:heOpAmpOutputGainType,'heOpAmpMIBConformance':heOpAmpMIBConformance,'heOpAmpMIBCompliances':heOpAmpMIBCompliances,'heOpAmpCompliance':heOpAmpCompliance,'heOpAmpMIBGroups':heOpAmpMIBGroups,_Z:heOpAmpUnitMandatoryGroup,_a:heOpAmpInputMandatoryGroup,_b:heOpAmpOutputMandatoryGroup,_c:heOpAmpUnitTableGroup,_d:heOpAmpInputTableGroup,_e:heOpAmpLaserTableGroup,_f:heOpAmpOutputTableGroup})