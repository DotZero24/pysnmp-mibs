_S='heOpRxInputMandatoryGroup'
_R='heOpRxOutputRFPadLevel'
_Q='heOpRxOutputPower'
_P='heOpRxOutputGainType'
_O='heOpRxOutputControl'
_N='heOpRxInputPower'
_M='heOpRxOutputIndex'
_L='0.1 dBm'
_K='not-accessible'
_J='heOpRxInputIndex'
_I='Integer32'
_H='heOpRxInputWavelengthControl'
_G='heOpRxInputStatus'
_F='read-only'
_E='entPhysicalIndex'
_D='ENTITY-MIB'
_C='read-write'
_B='SCTE-HMS-HE-OPTICAL-RECEIVER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_D,_E)
heOpticalReceiverGroup,=mibBuilder.importSymbols('SCTE-HMS-HE-OPTICS-MIB','heOpticalReceiverGroup')
HeFaultStatus,HeHundredthNanoMeter,HeOnOffControl,HeTenthdB,HeTenthdBm=mibBuilder.importSymbols('SCTE-HMS-HEADENDIDENT-MIB','HeFaultStatus','HeHundredthNanoMeter','HeOnOffControl','HeTenthdB','HeTenthdBm')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
heOpticalReceiverMIB=ModuleIdentity((1,3,6,1,4,1,5591,1,11,1,2,1))
_HeOpRxMIBObjects_ObjectIdentity=ObjectIdentity
heOpRxMIBObjects=_HeOpRxMIBObjects_ObjectIdentity((1,3,6,1,4,1,5591,1,11,1,2,1,1))
_HeOpRxInputTable_Object=MibTable
heOpRxInputTable=_HeOpRxInputTable_Object((1,3,6,1,4,1,5591,1,11,1,2,1,1,1))
if mibBuilder.loadTexts:heOpRxInputTable.setStatus(_A)
_HeOpRxInputEntry_Object=MibTableRow
heOpRxInputEntry=_HeOpRxInputEntry_Object((1,3,6,1,4,1,5591,1,11,1,2,1,1,1,1))
heOpRxInputEntry.setIndexNames((0,_D,_E),(0,_B,_J))
if mibBuilder.loadTexts:heOpRxInputEntry.setStatus(_A)
_HeOpRxInputIndex_Type=Unsigned32
_HeOpRxInputIndex_Object=MibTableColumn
heOpRxInputIndex=_HeOpRxInputIndex_Object((1,3,6,1,4,1,5591,1,11,1,2,1,1,1,1,1),_HeOpRxInputIndex_Type())
heOpRxInputIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:heOpRxInputIndex.setStatus(_A)
_HeOpRxInputPower_Type=HeTenthdBm
_HeOpRxInputPower_Object=MibTableColumn
heOpRxInputPower=_HeOpRxInputPower_Object((1,3,6,1,4,1,5591,1,11,1,2,1,1,1,1,2),_HeOpRxInputPower_Type())
heOpRxInputPower.setMaxAccess(_F)
if mibBuilder.loadTexts:heOpRxInputPower.setStatus(_A)
if mibBuilder.loadTexts:heOpRxInputPower.setUnits(_L)
_HeOpRxInputWavelengthControl_Type=HeHundredthNanoMeter
_HeOpRxInputWavelengthControl_Object=MibTableColumn
heOpRxInputWavelengthControl=_HeOpRxInputWavelengthControl_Object((1,3,6,1,4,1,5591,1,11,1,2,1,1,1,1,3),_HeOpRxInputWavelengthControl_Type())
heOpRxInputWavelengthControl.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpRxInputWavelengthControl.setStatus(_A)
if mibBuilder.loadTexts:heOpRxInputWavelengthControl.setUnits('0.01 nm')
_HeOpRxInputStatus_Type=HeFaultStatus
_HeOpRxInputStatus_Object=MibTableColumn
heOpRxInputStatus=_HeOpRxInputStatus_Object((1,3,6,1,4,1,5591,1,11,1,2,1,1,1,1,4),_HeOpRxInputStatus_Type())
heOpRxInputStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:heOpRxInputStatus.setStatus(_A)
_HeOpRxOutputTable_Object=MibTable
heOpRxOutputTable=_HeOpRxOutputTable_Object((1,3,6,1,4,1,5591,1,11,1,2,1,1,2))
if mibBuilder.loadTexts:heOpRxOutputTable.setStatus(_A)
_HeOpRxOutputEntry_Object=MibTableRow
heOpRxOutputEntry=_HeOpRxOutputEntry_Object((1,3,6,1,4,1,5591,1,11,1,2,1,1,2,1))
heOpRxOutputEntry.setIndexNames((0,_D,_E),(0,_B,_M))
if mibBuilder.loadTexts:heOpRxOutputEntry.setStatus(_A)
_HeOpRxOutputIndex_Type=Unsigned32
_HeOpRxOutputIndex_Object=MibTableColumn
heOpRxOutputIndex=_HeOpRxOutputIndex_Object((1,3,6,1,4,1,5591,1,11,1,2,1,1,2,1,1),_HeOpRxOutputIndex_Type())
heOpRxOutputIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:heOpRxOutputIndex.setStatus(_A)
_HeOpRxOutputControl_Type=HeOnOffControl
_HeOpRxOutputControl_Object=MibTableColumn
heOpRxOutputControl=_HeOpRxOutputControl_Object((1,3,6,1,4,1,5591,1,11,1,2,1,1,2,1,2),_HeOpRxOutputControl_Type())
heOpRxOutputControl.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpRxOutputControl.setStatus(_A)
class _HeOpRxOutputGainType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('constantPower',1),('constantGain',2)))
_HeOpRxOutputGainType_Type.__name__=_I
_HeOpRxOutputGainType_Object=MibTableColumn
heOpRxOutputGainType=_HeOpRxOutputGainType_Object((1,3,6,1,4,1,5591,1,11,1,2,1,1,2,1,3),_HeOpRxOutputGainType_Type())
heOpRxOutputGainType.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpRxOutputGainType.setStatus(_A)
_HeOpRxOutputPower_Type=HeTenthdBm
_HeOpRxOutputPower_Object=MibTableColumn
heOpRxOutputPower=_HeOpRxOutputPower_Object((1,3,6,1,4,1,5591,1,11,1,2,1,1,2,1,4),_HeOpRxOutputPower_Type())
heOpRxOutputPower.setMaxAccess(_F)
if mibBuilder.loadTexts:heOpRxOutputPower.setStatus(_A)
if mibBuilder.loadTexts:heOpRxOutputPower.setUnits(_L)
_HeOpRxOutputRFPadLevel_Type=HeTenthdB
_HeOpRxOutputRFPadLevel_Object=MibTableColumn
heOpRxOutputRFPadLevel=_HeOpRxOutputRFPadLevel_Object((1,3,6,1,4,1,5591,1,11,1,2,1,1,2,1,5),_HeOpRxOutputRFPadLevel_Type())
heOpRxOutputRFPadLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:heOpRxOutputRFPadLevel.setStatus(_A)
if mibBuilder.loadTexts:heOpRxOutputRFPadLevel.setUnits('0.1 dB')
_HeOpRxMIBConformance_ObjectIdentity=ObjectIdentity
heOpRxMIBConformance=_HeOpRxMIBConformance_ObjectIdentity((1,3,6,1,4,1,5591,1,11,1,2,1,2))
_HeOpRxMIBCompliances_ObjectIdentity=ObjectIdentity
heOpRxMIBCompliances=_HeOpRxMIBCompliances_ObjectIdentity((1,3,6,1,4,1,5591,1,11,1,2,1,2,1))
_HeOpRxMIBGroups_ObjectIdentity=ObjectIdentity
heOpRxMIBGroups=_HeOpRxMIBGroups_ObjectIdentity((1,3,6,1,4,1,5591,1,11,1,2,1,2,2))
heOpRxInputMandatoryGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,1,2,1,2,2,1))
heOpRxInputMandatoryGroup.setObjects(*((_B,_G),(_B,_H)))
if mibBuilder.loadTexts:heOpRxInputMandatoryGroup.setStatus(_A)
heOpRxInputTableGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,1,2,1,2,2,2))
heOpRxInputTableGroup.setObjects(*((_B,_N),(_B,_H),(_B,_G)))
if mibBuilder.loadTexts:heOpRxInputTableGroup.setStatus(_A)
heOpRxOutputTableGroup=ObjectGroup((1,3,6,1,4,1,5591,1,11,1,2,1,2,2,3))
heOpRxOutputTableGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:heOpRxOutputTableGroup.setStatus(_A)
heOpRxCompliance=ModuleCompliance((1,3,6,1,4,1,5591,1,11,1,2,1,2,1,1))
heOpRxCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:heOpRxCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'heOpticalReceiverMIB':heOpticalReceiverMIB,'heOpRxMIBObjects':heOpRxMIBObjects,'heOpRxInputTable':heOpRxInputTable,'heOpRxInputEntry':heOpRxInputEntry,_J:heOpRxInputIndex,_N:heOpRxInputPower,_H:heOpRxInputWavelengthControl,_G:heOpRxInputStatus,'heOpRxOutputTable':heOpRxOutputTable,'heOpRxOutputEntry':heOpRxOutputEntry,_M:heOpRxOutputIndex,_O:heOpRxOutputControl,_P:heOpRxOutputGainType,_Q:heOpRxOutputPower,_R:heOpRxOutputRFPadLevel,'heOpRxMIBConformance':heOpRxMIBConformance,'heOpRxMIBCompliances':heOpRxMIBCompliances,'heOpRxCompliance':heOpRxCompliance,'heOpRxMIBGroups':heOpRxMIBGroups,_S:heOpRxInputMandatoryGroup,'heOpRxInputTableGroup':heOpRxInputTableGroup,'heOpRxOutputTableGroup':heOpRxOutputTableGroup})