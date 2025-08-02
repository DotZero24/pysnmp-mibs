_z='finDeviceAttributeGroup'
_y='finSupplyGroup'
_x='finDeviceGroup'
_w='finDeviceAttributeValueAsOctets'
_v='finDeviceAttributeValueAsInteger'
_u='finSupplyMediaInputMediaType'
_t='finSupplyMediaInputMediaThickness'
_s='finSupplyMediaInputMediaWeight'
_r='finSupplyMediaInputSecurity'
_q='finSupplyMediaInputDescription'
_p='finSupplyMediaInputName'
_o='finSupplyMediaInputMediaName'
_n='finSupplyMediaInputStatus'
_m='finSupplyMediaInputMediaDimXFeedDir'
_l='finSupplyMediaInputMediaDimFeedDir'
_k='finSupplyMediaInputDimUnit'
_j='finSupplyMediaInputType'
_i='finSupplyMediaInputSupplyIndex'
_h='finSupplyMediaInputDeviceIndex'
_g='finSupplyColorName'
_f='finSupplyCurrentLevel'
_e='finSupplyMaxCapacity'
_d='finSupplyUnit'
_c='finSupplyDescription'
_b='finSupplyType'
_a='finSupplyClass'
_Z='finSupplyDeviceIndex'
_Y='finDeviceDescription'
_X='finDeviceStatus'
_W='finDeviceAssociatedOutputs'
_V='finDeviceAssociatedMediaPaths'
_U='finDeviceCurrentCapacity'
_T='finDeviceMaxCapacity'
_S='finDeviceCapacityUnit'
_R='finDevicePresentOnOff'
_Q='finDeviceType'
_P='finDeviceAttributeInstanceIndex'
_O='finDeviceAttributeTypeIndex'
_N='finSupplyMediaInputIndex'
_M='finSupplyIndex'
_L='PresentOnOff'
_K='finDeviceIndex'
_J='PrtSubUnitStatusTC'
_I='not-accessible'
_H='hrDeviceIndex'
_G='HOST-RESOURCES-MIB'
_F='OctetString'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='Finisher-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hrDeviceIndex,=mibBuilder.importSymbols(_G,_H)
FinAttributeTypeTC,FinDeviceTypeTC=mibBuilder.importSymbols('IANA-FINISHER-MIB','FinAttributeTypeTC','FinDeviceTypeTC')
PrtInputTypeTC,PrtMarkerSuppliesTypeTC=mibBuilder.importSymbols('IANA-PRINTER-MIB','PrtInputTypeTC','PrtMarkerSuppliesTypeTC')
PresentOnOff,PrtCapacityUnitTC,PrtLocalizedDescriptionStringTC,PrtMarkerSuppliesClassTC,PrtMarkerSuppliesSupplyUnitTC,PrtMediaUnitTC,PrtSubUnitStatusTC,printmib,prtMIBConformance=mibBuilder.importSymbols('Printer-MIB',_L,'PrtCapacityUnitTC','PrtLocalizedDescriptionStringTC','PrtMarkerSuppliesClassTC','PrtMarkerSuppliesSupplyUnitTC','PrtMediaUnitTC',_J,'printmib','prtMIBConformance')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
finisherMIB=ModuleIdentity((1,3,6,1,2,1,111))
if mibBuilder.loadTexts:finisherMIB.setRevisions(('2004-06-02 00:00',))
_FinMIBGroups_ObjectIdentity=ObjectIdentity
finMIBGroups=_FinMIBGroups_ObjectIdentity((1,3,6,1,2,1,43,2,6))
_FinDevice_ObjectIdentity=ObjectIdentity
finDevice=_FinDevice_ObjectIdentity((1,3,6,1,2,1,43,30))
_FinDeviceTable_Object=MibTable
finDeviceTable=_FinDeviceTable_Object((1,3,6,1,2,1,43,30,1))
if mibBuilder.loadTexts:finDeviceTable.setStatus(_A)
_FinDeviceEntry_Object=MibTableRow
finDeviceEntry=_FinDeviceEntry_Object((1,3,6,1,2,1,43,30,1,1))
finDeviceEntry.setIndexNames((0,_G,_H),(0,_B,_K))
if mibBuilder.loadTexts:finDeviceEntry.setStatus(_A)
class _FinDeviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FinDeviceIndex_Type.__name__=_D
_FinDeviceIndex_Object=MibTableColumn
finDeviceIndex=_FinDeviceIndex_Object((1,3,6,1,2,1,43,30,1,1,1),_FinDeviceIndex_Type())
finDeviceIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:finDeviceIndex.setStatus(_A)
_FinDeviceType_Type=FinDeviceTypeTC
_FinDeviceType_Object=MibTableColumn
finDeviceType=_FinDeviceType_Object((1,3,6,1,2,1,43,30,1,1,2),_FinDeviceType_Type())
finDeviceType.setMaxAccess(_C)
if mibBuilder.loadTexts:finDeviceType.setStatus(_A)
class _FinDevicePresentOnOff_Type(PresentOnOff):defaultValue=5
_FinDevicePresentOnOff_Type.__name__=_L
_FinDevicePresentOnOff_Object=MibTableColumn
finDevicePresentOnOff=_FinDevicePresentOnOff_Object((1,3,6,1,2,1,43,30,1,1,3),_FinDevicePresentOnOff_Type())
finDevicePresentOnOff.setMaxAccess(_E)
if mibBuilder.loadTexts:finDevicePresentOnOff.setStatus(_A)
_FinDeviceCapacityUnit_Type=PrtCapacityUnitTC
_FinDeviceCapacityUnit_Object=MibTableColumn
finDeviceCapacityUnit=_FinDeviceCapacityUnit_Object((1,3,6,1,2,1,43,30,1,1,4),_FinDeviceCapacityUnit_Type())
finDeviceCapacityUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:finDeviceCapacityUnit.setStatus(_A)
class _FinDeviceMaxCapacity_Type(Integer32):defaultValue=-2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_FinDeviceMaxCapacity_Type.__name__=_D
_FinDeviceMaxCapacity_Object=MibTableColumn
finDeviceMaxCapacity=_FinDeviceMaxCapacity_Object((1,3,6,1,2,1,43,30,1,1,5),_FinDeviceMaxCapacity_Type())
finDeviceMaxCapacity.setMaxAccess(_E)
if mibBuilder.loadTexts:finDeviceMaxCapacity.setStatus(_A)
class _FinDeviceCurrentCapacity_Type(Integer32):defaultValue=-2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_FinDeviceCurrentCapacity_Type.__name__=_D
_FinDeviceCurrentCapacity_Object=MibTableColumn
finDeviceCurrentCapacity=_FinDeviceCurrentCapacity_Object((1,3,6,1,2,1,43,30,1,1,6),_FinDeviceCurrentCapacity_Type())
finDeviceCurrentCapacity.setMaxAccess(_E)
if mibBuilder.loadTexts:finDeviceCurrentCapacity.setStatus(_A)
class _FinDeviceAssociatedMediaPaths_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_FinDeviceAssociatedMediaPaths_Type.__name__=_F
_FinDeviceAssociatedMediaPaths_Object=MibTableColumn
finDeviceAssociatedMediaPaths=_FinDeviceAssociatedMediaPaths_Object((1,3,6,1,2,1,43,30,1,1,7),_FinDeviceAssociatedMediaPaths_Type())
finDeviceAssociatedMediaPaths.setMaxAccess(_C)
if mibBuilder.loadTexts:finDeviceAssociatedMediaPaths.setStatus(_A)
class _FinDeviceAssociatedOutputs_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,63))
_FinDeviceAssociatedOutputs_Type.__name__=_F
_FinDeviceAssociatedOutputs_Object=MibTableColumn
finDeviceAssociatedOutputs=_FinDeviceAssociatedOutputs_Object((1,3,6,1,2,1,43,30,1,1,8),_FinDeviceAssociatedOutputs_Type())
finDeviceAssociatedOutputs.setMaxAccess(_C)
if mibBuilder.loadTexts:finDeviceAssociatedOutputs.setStatus(_A)
class _FinDeviceStatus_Type(PrtSubUnitStatusTC):defaultValue=5
_FinDeviceStatus_Type.__name__=_J
_FinDeviceStatus_Object=MibTableColumn
finDeviceStatus=_FinDeviceStatus_Object((1,3,6,1,2,1,43,30,1,1,9),_FinDeviceStatus_Type())
finDeviceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:finDeviceStatus.setStatus(_A)
_FinDeviceDescription_Type=PrtLocalizedDescriptionStringTC
_FinDeviceDescription_Object=MibTableColumn
finDeviceDescription=_FinDeviceDescription_Object((1,3,6,1,2,1,43,30,1,1,10),_FinDeviceDescription_Type())
finDeviceDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:finDeviceDescription.setStatus(_A)
_FinSupply_ObjectIdentity=ObjectIdentity
finSupply=_FinSupply_ObjectIdentity((1,3,6,1,2,1,43,31))
_FinSupplyTable_Object=MibTable
finSupplyTable=_FinSupplyTable_Object((1,3,6,1,2,1,43,31,1))
if mibBuilder.loadTexts:finSupplyTable.setStatus(_A)
_FinSupplyEntry_Object=MibTableRow
finSupplyEntry=_FinSupplyEntry_Object((1,3,6,1,2,1,43,31,1,1))
finSupplyEntry.setIndexNames((0,_G,_H),(0,_B,_M))
if mibBuilder.loadTexts:finSupplyEntry.setStatus(_A)
class _FinSupplyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FinSupplyIndex_Type.__name__=_D
_FinSupplyIndex_Object=MibTableColumn
finSupplyIndex=_FinSupplyIndex_Object((1,3,6,1,2,1,43,31,1,1,1),_FinSupplyIndex_Type())
finSupplyIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:finSupplyIndex.setStatus(_A)
class _FinSupplyDeviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FinSupplyDeviceIndex_Type.__name__=_D
_FinSupplyDeviceIndex_Object=MibTableColumn
finSupplyDeviceIndex=_FinSupplyDeviceIndex_Object((1,3,6,1,2,1,43,31,1,1,2),_FinSupplyDeviceIndex_Type())
finSupplyDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:finSupplyDeviceIndex.setStatus(_A)
_FinSupplyClass_Type=PrtMarkerSuppliesClassTC
_FinSupplyClass_Object=MibTableColumn
finSupplyClass=_FinSupplyClass_Object((1,3,6,1,2,1,43,31,1,1,3),_FinSupplyClass_Type())
finSupplyClass.setMaxAccess(_C)
if mibBuilder.loadTexts:finSupplyClass.setStatus(_A)
_FinSupplyType_Type=PrtMarkerSuppliesTypeTC
_FinSupplyType_Object=MibTableColumn
finSupplyType=_FinSupplyType_Object((1,3,6,1,2,1,43,31,1,1,4),_FinSupplyType_Type())
finSupplyType.setMaxAccess(_C)
if mibBuilder.loadTexts:finSupplyType.setStatus(_A)
_FinSupplyDescription_Type=PrtLocalizedDescriptionStringTC
_FinSupplyDescription_Object=MibTableColumn
finSupplyDescription=_FinSupplyDescription_Object((1,3,6,1,2,1,43,31,1,1,5),_FinSupplyDescription_Type())
finSupplyDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:finSupplyDescription.setStatus(_A)
_FinSupplyUnit_Type=PrtMarkerSuppliesSupplyUnitTC
_FinSupplyUnit_Object=MibTableColumn
finSupplyUnit=_FinSupplyUnit_Object((1,3,6,1,2,1,43,31,1,1,6),_FinSupplyUnit_Type())
finSupplyUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:finSupplyUnit.setStatus(_A)
class _FinSupplyMaxCapacity_Type(Integer32):defaultValue=-2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_FinSupplyMaxCapacity_Type.__name__=_D
_FinSupplyMaxCapacity_Object=MibTableColumn
finSupplyMaxCapacity=_FinSupplyMaxCapacity_Object((1,3,6,1,2,1,43,31,1,1,7),_FinSupplyMaxCapacity_Type())
finSupplyMaxCapacity.setMaxAccess(_E)
if mibBuilder.loadTexts:finSupplyMaxCapacity.setStatus(_A)
class _FinSupplyCurrentLevel_Type(Integer32):defaultValue=-2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-3,2147483647))
_FinSupplyCurrentLevel_Type.__name__=_D
_FinSupplyCurrentLevel_Object=MibTableColumn
finSupplyCurrentLevel=_FinSupplyCurrentLevel_Object((1,3,6,1,2,1,43,31,1,1,8),_FinSupplyCurrentLevel_Type())
finSupplyCurrentLevel.setMaxAccess(_E)
if mibBuilder.loadTexts:finSupplyCurrentLevel.setStatus(_A)
class _FinSupplyColorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_FinSupplyColorName_Type.__name__=_F
_FinSupplyColorName_Object=MibTableColumn
finSupplyColorName=_FinSupplyColorName_Object((1,3,6,1,2,1,43,31,1,1,9),_FinSupplyColorName_Type())
finSupplyColorName.setMaxAccess(_C)
if mibBuilder.loadTexts:finSupplyColorName.setStatus(_A)
_FinSupplyMediaInput_ObjectIdentity=ObjectIdentity
finSupplyMediaInput=_FinSupplyMediaInput_ObjectIdentity((1,3,6,1,2,1,43,32))
_FinSupplyMediaInputTable_Object=MibTable
finSupplyMediaInputTable=_FinSupplyMediaInputTable_Object((1,3,6,1,2,1,43,32,1))
if mibBuilder.loadTexts:finSupplyMediaInputTable.setStatus(_A)
_FinSupplyMediaInputEntry_Object=MibTableRow
finSupplyMediaInputEntry=_FinSupplyMediaInputEntry_Object((1,3,6,1,2,1,43,32,1,1))
finSupplyMediaInputEntry.setIndexNames((0,_G,_H),(0,_B,_N))
if mibBuilder.loadTexts:finSupplyMediaInputEntry.setStatus(_A)
class _FinSupplyMediaInputIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FinSupplyMediaInputIndex_Type.__name__=_D
_FinSupplyMediaInputIndex_Object=MibTableColumn
finSupplyMediaInputIndex=_FinSupplyMediaInputIndex_Object((1,3,6,1,2,1,43,32,1,1,1),_FinSupplyMediaInputIndex_Type())
finSupplyMediaInputIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:finSupplyMediaInputIndex.setStatus(_A)
class _FinSupplyMediaInputDeviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FinSupplyMediaInputDeviceIndex_Type.__name__=_D
_FinSupplyMediaInputDeviceIndex_Object=MibTableColumn
finSupplyMediaInputDeviceIndex=_FinSupplyMediaInputDeviceIndex_Object((1,3,6,1,2,1,43,32,1,1,2),_FinSupplyMediaInputDeviceIndex_Type())
finSupplyMediaInputDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:finSupplyMediaInputDeviceIndex.setStatus(_A)
class _FinSupplyMediaInputSupplyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FinSupplyMediaInputSupplyIndex_Type.__name__=_D
_FinSupplyMediaInputSupplyIndex_Object=MibTableColumn
finSupplyMediaInputSupplyIndex=_FinSupplyMediaInputSupplyIndex_Object((1,3,6,1,2,1,43,32,1,1,3),_FinSupplyMediaInputSupplyIndex_Type())
finSupplyMediaInputSupplyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:finSupplyMediaInputSupplyIndex.setStatus(_A)
_FinSupplyMediaInputType_Type=PrtInputTypeTC
_FinSupplyMediaInputType_Object=MibTableColumn
finSupplyMediaInputType=_FinSupplyMediaInputType_Object((1,3,6,1,2,1,43,32,1,1,4),_FinSupplyMediaInputType_Type())
finSupplyMediaInputType.setMaxAccess(_C)
if mibBuilder.loadTexts:finSupplyMediaInputType.setStatus(_A)
_FinSupplyMediaInputDimUnit_Type=PrtMediaUnitTC
_FinSupplyMediaInputDimUnit_Object=MibTableColumn
finSupplyMediaInputDimUnit=_FinSupplyMediaInputDimUnit_Object((1,3,6,1,2,1,43,32,1,1,5),_FinSupplyMediaInputDimUnit_Type())
finSupplyMediaInputDimUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:finSupplyMediaInputDimUnit.setStatus(_A)
class _FinSupplyMediaInputMediaDimFeedDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_FinSupplyMediaInputMediaDimFeedDir_Type.__name__=_D
_FinSupplyMediaInputMediaDimFeedDir_Object=MibTableColumn
finSupplyMediaInputMediaDimFeedDir=_FinSupplyMediaInputMediaDimFeedDir_Object((1,3,6,1,2,1,43,32,1,1,6),_FinSupplyMediaInputMediaDimFeedDir_Type())
finSupplyMediaInputMediaDimFeedDir.setMaxAccess(_E)
if mibBuilder.loadTexts:finSupplyMediaInputMediaDimFeedDir.setStatus(_A)
class _FinSupplyMediaInputMediaDimXFeedDir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_FinSupplyMediaInputMediaDimXFeedDir_Type.__name__=_D
_FinSupplyMediaInputMediaDimXFeedDir_Object=MibTableColumn
finSupplyMediaInputMediaDimXFeedDir=_FinSupplyMediaInputMediaDimXFeedDir_Object((1,3,6,1,2,1,43,32,1,1,7),_FinSupplyMediaInputMediaDimXFeedDir_Type())
finSupplyMediaInputMediaDimXFeedDir.setMaxAccess(_E)
if mibBuilder.loadTexts:finSupplyMediaInputMediaDimXFeedDir.setStatus(_A)
class _FinSupplyMediaInputStatus_Type(PrtSubUnitStatusTC):defaultValue=5
_FinSupplyMediaInputStatus_Type.__name__=_J
_FinSupplyMediaInputStatus_Object=MibTableColumn
finSupplyMediaInputStatus=_FinSupplyMediaInputStatus_Object((1,3,6,1,2,1,43,32,1,1,8),_FinSupplyMediaInputStatus_Type())
finSupplyMediaInputStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:finSupplyMediaInputStatus.setStatus(_A)
class _FinSupplyMediaInputMediaName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_FinSupplyMediaInputMediaName_Type.__name__=_F
_FinSupplyMediaInputMediaName_Object=MibTableColumn
finSupplyMediaInputMediaName=_FinSupplyMediaInputMediaName_Object((1,3,6,1,2,1,43,32,1,1,9),_FinSupplyMediaInputMediaName_Type())
finSupplyMediaInputMediaName.setMaxAccess(_E)
if mibBuilder.loadTexts:finSupplyMediaInputMediaName.setStatus(_A)
class _FinSupplyMediaInputName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_FinSupplyMediaInputName_Type.__name__=_F
_FinSupplyMediaInputName_Object=MibTableColumn
finSupplyMediaInputName=_FinSupplyMediaInputName_Object((1,3,6,1,2,1,43,32,1,1,10),_FinSupplyMediaInputName_Type())
finSupplyMediaInputName.setMaxAccess(_E)
if mibBuilder.loadTexts:finSupplyMediaInputName.setStatus(_A)
_FinSupplyMediaInputDescription_Type=PrtLocalizedDescriptionStringTC
_FinSupplyMediaInputDescription_Object=MibTableColumn
finSupplyMediaInputDescription=_FinSupplyMediaInputDescription_Object((1,3,6,1,2,1,43,32,1,1,11),_FinSupplyMediaInputDescription_Type())
finSupplyMediaInputDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:finSupplyMediaInputDescription.setStatus(_A)
_FinSupplyMediaInputSecurity_Type=PresentOnOff
_FinSupplyMediaInputSecurity_Object=MibTableColumn
finSupplyMediaInputSecurity=_FinSupplyMediaInputSecurity_Object((1,3,6,1,2,1,43,32,1,1,12),_FinSupplyMediaInputSecurity_Type())
finSupplyMediaInputSecurity.setMaxAccess(_E)
if mibBuilder.loadTexts:finSupplyMediaInputSecurity.setStatus(_A)
_FinSupplyMediaInputMediaWeight_Type=Integer32
_FinSupplyMediaInputMediaWeight_Object=MibTableColumn
finSupplyMediaInputMediaWeight=_FinSupplyMediaInputMediaWeight_Object((1,3,6,1,2,1,43,32,1,1,13),_FinSupplyMediaInputMediaWeight_Type())
finSupplyMediaInputMediaWeight.setMaxAccess(_E)
if mibBuilder.loadTexts:finSupplyMediaInputMediaWeight.setStatus(_A)
class _FinSupplyMediaInputMediaThickness_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_FinSupplyMediaInputMediaThickness_Type.__name__=_D
_FinSupplyMediaInputMediaThickness_Object=MibTableColumn
finSupplyMediaInputMediaThickness=_FinSupplyMediaInputMediaThickness_Object((1,3,6,1,2,1,43,32,1,1,14),_FinSupplyMediaInputMediaThickness_Type())
finSupplyMediaInputMediaThickness.setMaxAccess(_E)
if mibBuilder.loadTexts:finSupplyMediaInputMediaThickness.setStatus(_A)
class _FinSupplyMediaInputMediaType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_FinSupplyMediaInputMediaType_Type.__name__=_F
_FinSupplyMediaInputMediaType_Object=MibTableColumn
finSupplyMediaInputMediaType=_FinSupplyMediaInputMediaType_Object((1,3,6,1,2,1,43,32,1,1,15),_FinSupplyMediaInputMediaType_Type())
finSupplyMediaInputMediaType.setMaxAccess(_E)
if mibBuilder.loadTexts:finSupplyMediaInputMediaType.setStatus(_A)
_FinDeviceAttribute_ObjectIdentity=ObjectIdentity
finDeviceAttribute=_FinDeviceAttribute_ObjectIdentity((1,3,6,1,2,1,43,33))
_FinDeviceAttributeTable_Object=MibTable
finDeviceAttributeTable=_FinDeviceAttributeTable_Object((1,3,6,1,2,1,43,33,1))
if mibBuilder.loadTexts:finDeviceAttributeTable.setStatus(_A)
_FinDeviceAttributeEntry_Object=MibTableRow
finDeviceAttributeEntry=_FinDeviceAttributeEntry_Object((1,3,6,1,2,1,43,33,1,1))
finDeviceAttributeEntry.setIndexNames((0,_G,_H),(0,_B,_K),(0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:finDeviceAttributeEntry.setStatus(_A)
_FinDeviceAttributeTypeIndex_Type=FinAttributeTypeTC
_FinDeviceAttributeTypeIndex_Object=MibTableColumn
finDeviceAttributeTypeIndex=_FinDeviceAttributeTypeIndex_Object((1,3,6,1,2,1,43,33,1,1,1),_FinDeviceAttributeTypeIndex_Type())
finDeviceAttributeTypeIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:finDeviceAttributeTypeIndex.setStatus(_A)
class _FinDeviceAttributeInstanceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FinDeviceAttributeInstanceIndex_Type.__name__=_D
_FinDeviceAttributeInstanceIndex_Object=MibTableColumn
finDeviceAttributeInstanceIndex=_FinDeviceAttributeInstanceIndex_Object((1,3,6,1,2,1,43,33,1,1,2),_FinDeviceAttributeInstanceIndex_Type())
finDeviceAttributeInstanceIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:finDeviceAttributeInstanceIndex.setStatus(_A)
class _FinDeviceAttributeValueAsInteger_Type(Integer32):defaultValue=-2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,2147483647))
_FinDeviceAttributeValueAsInteger_Type.__name__=_D
_FinDeviceAttributeValueAsInteger_Object=MibTableColumn
finDeviceAttributeValueAsInteger=_FinDeviceAttributeValueAsInteger_Object((1,3,6,1,2,1,43,33,1,1,3),_FinDeviceAttributeValueAsInteger_Type())
finDeviceAttributeValueAsInteger.setMaxAccess(_E)
if mibBuilder.loadTexts:finDeviceAttributeValueAsInteger.setStatus(_A)
class _FinDeviceAttributeValueAsOctets_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_FinDeviceAttributeValueAsOctets_Type.__name__=_F
_FinDeviceAttributeValueAsOctets_Object=MibTableColumn
finDeviceAttributeValueAsOctets=_FinDeviceAttributeValueAsOctets_Object((1,3,6,1,2,1,43,33,1,1,4),_FinDeviceAttributeValueAsOctets_Type())
finDeviceAttributeValueAsOctets.setMaxAccess(_E)
if mibBuilder.loadTexts:finDeviceAttributeValueAsOctets.setStatus(_A)
finDeviceGroup=ObjectGroup((1,3,6,1,2,1,43,2,6,1))
finDeviceGroup.setObjects(*((_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:finDeviceGroup.setStatus(_A)
finSupplyGroup=ObjectGroup((1,3,6,1,2,1,43,2,6,2))
finSupplyGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:finSupplyGroup.setStatus(_A)
finSupplyMediaInputGroup=ObjectGroup((1,3,6,1,2,1,43,2,6,3))
finSupplyMediaInputGroup.setObjects(*((_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u)))
if mibBuilder.loadTexts:finSupplyMediaInputGroup.setStatus(_A)
finDeviceAttributeGroup=ObjectGroup((1,3,6,1,2,1,43,2,6,4))
finDeviceAttributeGroup.setObjects(*((_B,_v),(_B,_w)))
if mibBuilder.loadTexts:finDeviceAttributeGroup.setStatus(_A)
finMIBCompliance=ModuleCompliance((1,3,6,1,2,1,43,2,5))
finMIBCompliance.setObjects(*((_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:finMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'finMIBCompliance':finMIBCompliance,'finMIBGroups':finMIBGroups,_x:finDeviceGroup,_y:finSupplyGroup,'finSupplyMediaInputGroup':finSupplyMediaInputGroup,_z:finDeviceAttributeGroup,'finDevice':finDevice,'finDeviceTable':finDeviceTable,'finDeviceEntry':finDeviceEntry,_K:finDeviceIndex,_Q:finDeviceType,_R:finDevicePresentOnOff,_S:finDeviceCapacityUnit,_T:finDeviceMaxCapacity,_U:finDeviceCurrentCapacity,_V:finDeviceAssociatedMediaPaths,_W:finDeviceAssociatedOutputs,_X:finDeviceStatus,_Y:finDeviceDescription,'finSupply':finSupply,'finSupplyTable':finSupplyTable,'finSupplyEntry':finSupplyEntry,_M:finSupplyIndex,_Z:finSupplyDeviceIndex,_a:finSupplyClass,_b:finSupplyType,_c:finSupplyDescription,_d:finSupplyUnit,_e:finSupplyMaxCapacity,_f:finSupplyCurrentLevel,_g:finSupplyColorName,'finSupplyMediaInput':finSupplyMediaInput,'finSupplyMediaInputTable':finSupplyMediaInputTable,'finSupplyMediaInputEntry':finSupplyMediaInputEntry,_N:finSupplyMediaInputIndex,_h:finSupplyMediaInputDeviceIndex,_i:finSupplyMediaInputSupplyIndex,_j:finSupplyMediaInputType,_k:finSupplyMediaInputDimUnit,_l:finSupplyMediaInputMediaDimFeedDir,_m:finSupplyMediaInputMediaDimXFeedDir,_n:finSupplyMediaInputStatus,_o:finSupplyMediaInputMediaName,_p:finSupplyMediaInputName,_q:finSupplyMediaInputDescription,_r:finSupplyMediaInputSecurity,_s:finSupplyMediaInputMediaWeight,_t:finSupplyMediaInputMediaThickness,_u:finSupplyMediaInputMediaType,'finDeviceAttribute':finDeviceAttribute,'finDeviceAttributeTable':finDeviceAttributeTable,'finDeviceAttributeEntry':finDeviceAttributeEntry,_O:finDeviceAttributeTypeIndex,_P:finDeviceAttributeInstanceIndex,_v:finDeviceAttributeValueAsInteger,_w:finDeviceAttributeValueAsOctets,'finisherMIB':finisherMIB})