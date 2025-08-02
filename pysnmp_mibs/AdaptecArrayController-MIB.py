_L='adaptecArrayControllerDevIndex'
_K='adaptecArrayControllerContIndex'
_J='adaptecArrayControllerAdapterIndex'
_I='nonRecoverable'
_H='critical'
_G='nonCritical'
_F='unknown'
_E='other'
_D='AdaptecArrayController-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Adaptec_ObjectIdentity=ObjectIdentity
adaptec=_Adaptec_ObjectIdentity((1,3,6,1,4,1,795))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,795,3))
_AdaptecArrayController_ObjectIdentity=ObjectIdentity
adaptecArrayController=_AdaptecArrayController_ObjectIdentity((1,3,6,1,4,1,795,3,5))
_AdaptecArrayControllerSoftwareVersion_Type=DisplayString
_AdaptecArrayControllerSoftwareVersion_Object=MibScalar
adaptecArrayControllerSoftwareVersion=_AdaptecArrayControllerSoftwareVersion_Object((1,3,6,1,4,1,795,3,5,1),_AdaptecArrayControllerSoftwareVersion_Type())
adaptecArrayControllerSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerSoftwareVersion.setStatus(_A)
_AdaptecArrayControllerAdapterNumber_Type=Integer32
_AdaptecArrayControllerAdapterNumber_Object=MibScalar
adaptecArrayControllerAdapterNumber=_AdaptecArrayControllerAdapterNumber_Object((1,3,6,1,4,1,795,3,5,2),_AdaptecArrayControllerAdapterNumber_Type())
adaptecArrayControllerAdapterNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerAdapterNumber.setStatus(_A)
_AdaptecArrayControllerAdapterTable_Object=MibTable
adaptecArrayControllerAdapterTable=_AdaptecArrayControllerAdapterTable_Object((1,3,6,1,4,1,795,3,5,3))
if mibBuilder.loadTexts:adaptecArrayControllerAdapterTable.setStatus(_A)
_AdaptecArrayControllerAdapterEntry_Object=MibTableRow
adaptecArrayControllerAdapterEntry=_AdaptecArrayControllerAdapterEntry_Object((1,3,6,1,4,1,795,3,5,3,1))
adaptecArrayControllerAdapterEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:adaptecArrayControllerAdapterEntry.setStatus(_A)
_AdaptecArrayControllerAdapterIndex_Type=Integer32
_AdaptecArrayControllerAdapterIndex_Object=MibTableColumn
adaptecArrayControllerAdapterIndex=_AdaptecArrayControllerAdapterIndex_Object((1,3,6,1,4,1,795,3,5,3,1,1),_AdaptecArrayControllerAdapterIndex_Type())
adaptecArrayControllerAdapterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerAdapterIndex.setStatus(_A)
_AdaptecArrayControllerAdapterDescription_Type=DisplayString
_AdaptecArrayControllerAdapterDescription_Object=MibTableColumn
adaptecArrayControllerAdapterDescription=_AdaptecArrayControllerAdapterDescription_Object((1,3,6,1,4,1,795,3,5,3,1,2),_AdaptecArrayControllerAdapterDescription_Type())
adaptecArrayControllerAdapterDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerAdapterDescription.setStatus(_A)
_AdaptecArrayControllerAdapterType_Type=DisplayString
_AdaptecArrayControllerAdapterType_Object=MibTableColumn
adaptecArrayControllerAdapterType=_AdaptecArrayControllerAdapterType_Object((1,3,6,1,4,1,795,3,5,3,1,3),_AdaptecArrayControllerAdapterType_Type())
adaptecArrayControllerAdapterType.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerAdapterType.setStatus(_A)
_AdaptecArrayControllerAdapterVersion_Type=DisplayString
_AdaptecArrayControllerAdapterVersion_Object=MibTableColumn
adaptecArrayControllerAdapterVersion=_AdaptecArrayControllerAdapterVersion_Object((1,3,6,1,4,1,795,3,5,3,1,4),_AdaptecArrayControllerAdapterVersion_Type())
adaptecArrayControllerAdapterVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerAdapterVersion.setStatus(_A)
_AdaptecArrayControllerAdapterChannelCount_Type=Integer32
_AdaptecArrayControllerAdapterChannelCount_Object=MibTableColumn
adaptecArrayControllerAdapterChannelCount=_AdaptecArrayControllerAdapterChannelCount_Object((1,3,6,1,4,1,795,3,5,3,1,5),_AdaptecArrayControllerAdapterChannelCount_Type())
adaptecArrayControllerAdapterChannelCount.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerAdapterChannelCount.setStatus(_A)
class _AdaptecArrayControllerAdapterStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),('ok',3),(_G,4),(_H,5),(_I,6)))
_AdaptecArrayControllerAdapterStatus_Type.__name__=_C
_AdaptecArrayControllerAdapterStatus_Object=MibTableColumn
adaptecArrayControllerAdapterStatus=_AdaptecArrayControllerAdapterStatus_Object((1,3,6,1,4,1,795,3,5,3,1,6),_AdaptecArrayControllerAdapterStatus_Type())
adaptecArrayControllerAdapterStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerAdapterStatus.setStatus(_A)
_AdaptecArrayControllerContainerTable_Object=MibTable
adaptecArrayControllerContainerTable=_AdaptecArrayControllerContainerTable_Object((1,3,6,1,4,1,795,3,5,4))
if mibBuilder.loadTexts:adaptecArrayControllerContainerTable.setStatus(_A)
_AdaptecArrayControllerContainerEntry_Object=MibTableRow
adaptecArrayControllerContainerEntry=_AdaptecArrayControllerContainerEntry_Object((1,3,6,1,4,1,795,3,5,4,1))
adaptecArrayControllerContainerEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:adaptecArrayControllerContainerEntry.setStatus(_A)
_AdaptecArrayControllerContIndex_Type=Integer32
_AdaptecArrayControllerContIndex_Object=MibTableColumn
adaptecArrayControllerContIndex=_AdaptecArrayControllerContIndex_Object((1,3,6,1,4,1,795,3,5,4,1,1),_AdaptecArrayControllerContIndex_Type())
adaptecArrayControllerContIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerContIndex.setStatus(_A)
_AdapterArrayControllerContAdapterIndex_Type=Integer32
_AdapterArrayControllerContAdapterIndex_Object=MibTableColumn
adapterArrayControllerContAdapterIndex=_AdapterArrayControllerContAdapterIndex_Object((1,3,6,1,4,1,795,3,5,4,1,2),_AdapterArrayControllerContAdapterIndex_Type())
adapterArrayControllerContAdapterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:adapterArrayControllerContAdapterIndex.setStatus(_A)
_AdaptecArrayControllerContNumber_Type=Integer32
_AdaptecArrayControllerContNumber_Object=MibTableColumn
adaptecArrayControllerContNumber=_AdaptecArrayControllerContNumber_Object((1,3,6,1,4,1,795,3,5,4,1,3),_AdaptecArrayControllerContNumber_Type())
adaptecArrayControllerContNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerContNumber.setStatus(_A)
_AdaptecArrayControllerContSize_Type=Integer32
_AdaptecArrayControllerContSize_Object=MibTableColumn
adaptecArrayControllerContSize=_AdaptecArrayControllerContSize_Object((1,3,6,1,4,1,795,3,5,4,1,4),_AdaptecArrayControllerContSize_Type())
adaptecArrayControllerContSize.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerContSize.setStatus(_A)
_AdaptecArrayControllerContMountPoint_Type=DisplayString
_AdaptecArrayControllerContMountPoint_Object=MibTableColumn
adaptecArrayControllerContMountPoint=_AdaptecArrayControllerContMountPoint_Object((1,3,6,1,4,1,795,3,5,4,1,5),_AdaptecArrayControllerContMountPoint_Type())
adaptecArrayControllerContMountPoint.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerContMountPoint.setStatus(_A)
_AdaptecArrayControllerContType_Type=DisplayString
_AdaptecArrayControllerContType_Object=MibTableColumn
adaptecArrayControllerContType=_AdaptecArrayControllerContType_Object((1,3,6,1,4,1,795,3,5,4,1,6),_AdaptecArrayControllerContType_Type())
adaptecArrayControllerContType.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerContType.setStatus(_A)
_AdaptecArrayControllerContUsage_Type=DisplayString
_AdaptecArrayControllerContUsage_Object=MibTableColumn
adaptecArrayControllerContUsage=_AdaptecArrayControllerContUsage_Object((1,3,6,1,4,1,795,3,5,4,1,7),_AdaptecArrayControllerContUsage_Type())
adaptecArrayControllerContUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerContUsage.setStatus(_A)
class _AdaptecArrayControllerContStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),('ok',3),(_G,4),(_H,5),(_I,6)))
_AdaptecArrayControllerContStatus_Type.__name__=_C
_AdaptecArrayControllerContStatus_Object=MibTableColumn
adaptecArrayControllerContStatus=_AdaptecArrayControllerContStatus_Object((1,3,6,1,4,1,795,3,5,4,1,8),_AdaptecArrayControllerContStatus_Type())
adaptecArrayControllerContStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerContStatus.setStatus(_A)
_AdaptecArrayControllerDeviceTable_Object=MibTable
adaptecArrayControllerDeviceTable=_AdaptecArrayControllerDeviceTable_Object((1,3,6,1,4,1,795,3,5,5))
if mibBuilder.loadTexts:adaptecArrayControllerDeviceTable.setStatus(_A)
_AdaptecArrayControllerDeviceEntry_Object=MibTableRow
adaptecArrayControllerDeviceEntry=_AdaptecArrayControllerDeviceEntry_Object((1,3,6,1,4,1,795,3,5,5,1))
adaptecArrayControllerDeviceEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:adaptecArrayControllerDeviceEntry.setStatus(_A)
_AdaptecArrayControllerDevIndex_Type=Integer32
_AdaptecArrayControllerDevIndex_Object=MibTableColumn
adaptecArrayControllerDevIndex=_AdaptecArrayControllerDevIndex_Object((1,3,6,1,4,1,795,3,5,5,1,1),_AdaptecArrayControllerDevIndex_Type())
adaptecArrayControllerDevIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerDevIndex.setStatus(_A)
_AdaptecArrayControllerDevAdapterIndex_Type=Integer32
_AdaptecArrayControllerDevAdapterIndex_Object=MibTableColumn
adaptecArrayControllerDevAdapterIndex=_AdaptecArrayControllerDevAdapterIndex_Object((1,3,6,1,4,1,795,3,5,5,1,2),_AdaptecArrayControllerDevAdapterIndex_Type())
adaptecArrayControllerDevAdapterIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerDevAdapterIndex.setStatus(_A)
_AdaptecArrayControllerDevChannelId_Type=Integer32
_AdaptecArrayControllerDevChannelId_Object=MibTableColumn
adaptecArrayControllerDevChannelId=_AdaptecArrayControllerDevChannelId_Object((1,3,6,1,4,1,795,3,5,5,1,3),_AdaptecArrayControllerDevChannelId_Type())
adaptecArrayControllerDevChannelId.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerDevChannelId.setStatus(_A)
_AdaptecArrayControllerDevId_Type=Integer32
_AdaptecArrayControllerDevId_Object=MibTableColumn
adaptecArrayControllerDevId=_AdaptecArrayControllerDevId_Object((1,3,6,1,4,1,795,3,5,5,1,4),_AdaptecArrayControllerDevId_Type())
adaptecArrayControllerDevId.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerDevId.setStatus(_A)
_AdaptecArrayControllerDevLogicalNumber_Type=Integer32
_AdaptecArrayControllerDevLogicalNumber_Object=MibTableColumn
adaptecArrayControllerDevLogicalNumber=_AdaptecArrayControllerDevLogicalNumber_Object((1,3,6,1,4,1,795,3,5,5,1,5),_AdaptecArrayControllerDevLogicalNumber_Type())
adaptecArrayControllerDevLogicalNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerDevLogicalNumber.setStatus(_A)
_AdaptecArrayControllerDevType_Type=Integer32
_AdaptecArrayControllerDevType_Object=MibTableColumn
adaptecArrayControllerDevType=_AdaptecArrayControllerDevType_Object((1,3,6,1,4,1,795,3,5,5,1,6),_AdaptecArrayControllerDevType_Type())
adaptecArrayControllerDevType.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerDevType.setStatus(_A)
_AdaptecArrayControllerDevVendor_Type=DisplayString
_AdaptecArrayControllerDevVendor_Object=MibTableColumn
adaptecArrayControllerDevVendor=_AdaptecArrayControllerDevVendor_Object((1,3,6,1,4,1,795,3,5,5,1,7),_AdaptecArrayControllerDevVendor_Type())
adaptecArrayControllerDevVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerDevVendor.setStatus(_A)
_AdaptecArrayControllerDevProduct_Type=DisplayString
_AdaptecArrayControllerDevProduct_Object=MibTableColumn
adaptecArrayControllerDevProduct=_AdaptecArrayControllerDevProduct_Object((1,3,6,1,4,1,795,3,5,5,1,8),_AdaptecArrayControllerDevProduct_Type())
adaptecArrayControllerDevProduct.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerDevProduct.setStatus(_A)
_AdaptecArrayControllerDevRevision_Type=DisplayString
_AdaptecArrayControllerDevRevision_Object=MibTableColumn
adaptecArrayControllerDevRevision=_AdaptecArrayControllerDevRevision_Object((1,3,6,1,4,1,795,3,5,5,1,9),_AdaptecArrayControllerDevRevision_Type())
adaptecArrayControllerDevRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerDevRevision.setStatus(_A)
_AdaptecArrayControllerDevBlocks_Type=Integer32
_AdaptecArrayControllerDevBlocks_Object=MibTableColumn
adaptecArrayControllerDevBlocks=_AdaptecArrayControllerDevBlocks_Object((1,3,6,1,4,1,795,3,5,5,1,10),_AdaptecArrayControllerDevBlocks_Type())
adaptecArrayControllerDevBlocks.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerDevBlocks.setStatus(_A)
_AdaptecArrayControllerDevBytesPerBlock_Type=Integer32
_AdaptecArrayControllerDevBytesPerBlock_Object=MibTableColumn
adaptecArrayControllerDevBytesPerBlock=_AdaptecArrayControllerDevBytesPerBlock_Object((1,3,6,1,4,1,795,3,5,5,1,11),_AdaptecArrayControllerDevBytesPerBlock_Type())
adaptecArrayControllerDevBytesPerBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerDevBytesPerBlock.setStatus(_A)
_AdaptecArrayControllerDevUsage_Type=DisplayString
_AdaptecArrayControllerDevUsage_Object=MibTableColumn
adaptecArrayControllerDevUsage=_AdaptecArrayControllerDevUsage_Object((1,3,6,1,4,1,795,3,5,5,1,12),_AdaptecArrayControllerDevUsage_Type())
adaptecArrayControllerDevUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerDevUsage.setStatus(_A)
class _AdaptecArrayControllerDevStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),('ok',3),(_G,4),(_H,5),(_I,6)))
_AdaptecArrayControllerDevStatus_Type.__name__=_C
_AdaptecArrayControllerDevStatus_Object=MibTableColumn
adaptecArrayControllerDevStatus=_AdaptecArrayControllerDevStatus_Object((1,3,6,1,4,1,795,3,5,5,1,13),_AdaptecArrayControllerDevStatus_Type())
adaptecArrayControllerDevStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:adaptecArrayControllerDevStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'adaptec':adaptec,'products':products,'adaptecArrayController':adaptecArrayController,'adaptecArrayControllerSoftwareVersion':adaptecArrayControllerSoftwareVersion,'adaptecArrayControllerAdapterNumber':adaptecArrayControllerAdapterNumber,'adaptecArrayControllerAdapterTable':adaptecArrayControllerAdapterTable,'adaptecArrayControllerAdapterEntry':adaptecArrayControllerAdapterEntry,_J:adaptecArrayControllerAdapterIndex,'adaptecArrayControllerAdapterDescription':adaptecArrayControllerAdapterDescription,'adaptecArrayControllerAdapterType':adaptecArrayControllerAdapterType,'adaptecArrayControllerAdapterVersion':adaptecArrayControllerAdapterVersion,'adaptecArrayControllerAdapterChannelCount':adaptecArrayControllerAdapterChannelCount,'adaptecArrayControllerAdapterStatus':adaptecArrayControllerAdapterStatus,'adaptecArrayControllerContainerTable':adaptecArrayControllerContainerTable,'adaptecArrayControllerContainerEntry':adaptecArrayControllerContainerEntry,_K:adaptecArrayControllerContIndex,'adapterArrayControllerContAdapterIndex':adapterArrayControllerContAdapterIndex,'adaptecArrayControllerContNumber':adaptecArrayControllerContNumber,'adaptecArrayControllerContSize':adaptecArrayControllerContSize,'adaptecArrayControllerContMountPoint':adaptecArrayControllerContMountPoint,'adaptecArrayControllerContType':adaptecArrayControllerContType,'adaptecArrayControllerContUsage':adaptecArrayControllerContUsage,'adaptecArrayControllerContStatus':adaptecArrayControllerContStatus,'adaptecArrayControllerDeviceTable':adaptecArrayControllerDeviceTable,'adaptecArrayControllerDeviceEntry':adaptecArrayControllerDeviceEntry,_L:adaptecArrayControllerDevIndex,'adaptecArrayControllerDevAdapterIndex':adaptecArrayControllerDevAdapterIndex,'adaptecArrayControllerDevChannelId':adaptecArrayControllerDevChannelId,'adaptecArrayControllerDevId':adaptecArrayControllerDevId,'adaptecArrayControllerDevLogicalNumber':adaptecArrayControllerDevLogicalNumber,'adaptecArrayControllerDevType':adaptecArrayControllerDevType,'adaptecArrayControllerDevVendor':adaptecArrayControllerDevVendor,'adaptecArrayControllerDevProduct':adaptecArrayControllerDevProduct,'adaptecArrayControllerDevRevision':adaptecArrayControllerDevRevision,'adaptecArrayControllerDevBlocks':adaptecArrayControllerDevBlocks,'adaptecArrayControllerDevBytesPerBlock':adaptecArrayControllerDevBytesPerBlock,'adaptecArrayControllerDevUsage':adaptecArrayControllerDevUsage,'adaptecArrayControllerDevStatus':adaptecArrayControllerDevStatus})