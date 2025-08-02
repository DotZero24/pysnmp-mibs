_V='notebookLineNumber'
_U='repairIndex'
_T='regIndex'
_S='notSupported'
_R='productKeyFeatureIndex'
_Q='receiverEntryId'
_P='softReset'
_O='hardReset'
_N='noReset'
_M='closed'
_L='unknown'
_K='productKeyIndex'
_J='enabled'
_I='disabled'
_H='OctetString'
_G='moduleId'
_F='TELESTE-COMMON-MIB'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='mandatory'
_A='optional'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
DateAndTime,TPhysAddress,Uint16,common=mibBuilder.importSymbols('TELESTE-ROOT-MIB','DateAndTime','TPhysAddress','Uint16','common')
_Element_ObjectIdentity=ObjectIdentity
element=_Element_ObjectIdentity((1,3,6,1,4,1,3715,99,1))
_ElementInformation_ObjectIdentity=ObjectIdentity
elementInformation=_ElementInformation_ObjectIdentity((1,3,6,1,4,1,3715,99,1,1))
_ElementName_Type=DisplayString
_ElementName_Object=MibScalar
elementName=_ElementName_Object((1,3,6,1,4,1,3715,99,1,1,1),_ElementName_Type())
elementName.setMaxAccess(_D)
if mibBuilder.loadTexts:elementName.setStatus(_B)
class _ElementStructure_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_L,1),('compact',2),('modular',3)))
_ElementStructure_Type.__name__=_E
_ElementStructure_Object=MibScalar
elementStructure=_ElementStructure_Object((1,3,6,1,4,1,3715,99,1,1,2),_ElementStructure_Type())
elementStructure.setMaxAccess(_C)
if mibBuilder.loadTexts:elementStructure.setStatus(_B)
_ElementConfigChangeCode_Type=Integer32
_ElementConfigChangeCode_Object=MibScalar
elementConfigChangeCode=_ElementConfigChangeCode_Object((1,3,6,1,4,1,3715,99,1,1,3),_ElementConfigChangeCode_Type())
elementConfigChangeCode.setMaxAccess(_C)
if mibBuilder.loadTexts:elementConfigChangeCode.setStatus(_A)
_ElementResetCount_Type=Integer32
_ElementResetCount_Object=MibScalar
elementResetCount=_ElementResetCount_Object((1,3,6,1,4,1,3715,99,1,1,4),_ElementResetCount_Type())
elementResetCount.setMaxAccess(_C)
if mibBuilder.loadTexts:elementResetCount.setStatus(_A)
_ElementTotalUpTime_Type=Integer32
_ElementTotalUpTime_Object=MibScalar
elementTotalUpTime=_ElementTotalUpTime_Object((1,3,6,1,4,1,3715,99,1,1,5),_ElementTotalUpTime_Type())
elementTotalUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:elementTotalUpTime.setStatus(_B)
_ElementLatitude_Type=Integer32
_ElementLatitude_Object=MibScalar
elementLatitude=_ElementLatitude_Object((1,3,6,1,4,1,3715,99,1,1,6),_ElementLatitude_Type())
elementLatitude.setMaxAccess(_D)
if mibBuilder.loadTexts:elementLatitude.setStatus(_A)
_ElementLongitude_Type=Integer32
_ElementLongitude_Object=MibScalar
elementLongitude=_ElementLongitude_Object((1,3,6,1,4,1,3715,99,1,1,7),_ElementLongitude_Type())
elementLongitude.setMaxAccess(_D)
if mibBuilder.loadTexts:elementLongitude.setStatus(_A)
_ElementAltitude_Type=Integer32
_ElementAltitude_Object=MibScalar
elementAltitude=_ElementAltitude_Object((1,3,6,1,4,1,3715,99,1,1,8),_ElementAltitude_Type())
elementAltitude.setMaxAccess(_D)
if mibBuilder.loadTexts:elementAltitude.setStatus(_A)
_ElementStatus_ObjectIdentity=ObjectIdentity
elementStatus=_ElementStatus_ObjectIdentity((1,3,6,1,4,1,3715,99,1,2))
class _StatusGeneral_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normal',1),('notification',2),('warning',3),('alarm',4)))
_StatusGeneral_Type.__name__=_E
_StatusGeneral_Object=MibScalar
statusGeneral=_StatusGeneral_Object((1,3,6,1,4,1,3715,99,1,2,1),_StatusGeneral_Type())
statusGeneral.setMaxAccess(_C)
if mibBuilder.loadTexts:statusGeneral.setStatus(_B)
class _StatusBusMaster_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('slaveOnly',1),('configuredSlave',2),('currentlySlave',3),('currentlyMaster',4)))
_StatusBusMaster_Type.__name__=_E
_StatusBusMaster_Object=MibScalar
statusBusMaster=_StatusBusMaster_Object((1,3,6,1,4,1,3715,99,1,2,2),_StatusBusMaster_Type())
statusBusMaster.setMaxAccess(_C)
if mibBuilder.loadTexts:statusBusMaster.setStatus(_A)
class _StatusLmt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noLmtInterface',1),('stateUnknown',2),('notConnected',3),('connected',4)))
_StatusLmt_Type.__name__=_E
_StatusLmt_Object=MibScalar
statusLmt=_StatusLmt_Object((1,3,6,1,4,1,3715,99,1,2,3),_StatusLmt_Type())
statusLmt.setMaxAccess(_C)
if mibBuilder.loadTexts:statusLmt.setStatus(_A)
class _StatusLid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noLid',1),(_M,2),('open',3)))
_StatusLid_Type.__name__=_E
_StatusLid_Object=MibScalar
statusLid=_StatusLid_Object((1,3,6,1,4,1,3715,99,1,2,4),_StatusLid_Type())
statusLid.setMaxAccess(_C)
if mibBuilder.loadTexts:statusLid.setStatus(_A)
class _StatusTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('tempNormal',1),('tempHIHI',2),('tempHi',3),('tempLo',4),('tempLOLO',5)))
_StatusTemperature_Type.__name__=_E
_StatusTemperature_Object=MibScalar
statusTemperature=_StatusTemperature_Object((1,3,6,1,4,1,3715,99,1,2,5),_StatusTemperature_Type())
statusTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:statusTemperature.setStatus(_A)
class _StatusFan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fanNormal',1),('fanFailure',2)))
_StatusFan_Type.__name__=_E
_StatusFan_Object=MibScalar
statusFan=_StatusFan_Object((1,3,6,1,4,1,3715,99,1,2,6),_StatusFan_Type())
statusFan.setMaxAccess(_C)
if mibBuilder.loadTexts:statusFan.setStatus(_B)
class _StatusHardware_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('hwNormal',1),('hwFailure',2)))
_StatusHardware_Type.__name__=_E
_StatusHardware_Object=MibScalar
statusHardware=_StatusHardware_Object((1,3,6,1,4,1,3715,99,1,2,7),_StatusHardware_Type())
statusHardware.setMaxAccess(_C)
if mibBuilder.loadTexts:statusHardware.setStatus(_B)
class _StatusSoftware_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('swNormal',1),('swFailure',2),('swMissing',3),('swInitialising',4)))
_StatusSoftware_Type.__name__=_E
_StatusSoftware_Object=MibScalar
statusSoftware=_StatusSoftware_Object((1,3,6,1,4,1,3715,99,1,2,8),_StatusSoftware_Type())
statusSoftware.setMaxAccess(_C)
if mibBuilder.loadTexts:statusSoftware.setStatus(_B)
class _StatusSettings_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('settingsStable',1),('settingsChanged',2),('settingsNotAvailable',3)))
_StatusSettings_Type.__name__=_E
_StatusSettings_Object=MibScalar
statusSettings=_StatusSettings_Object((1,3,6,1,4,1,3715,99,1,2,9),_StatusSettings_Type())
statusSettings.setMaxAccess(_C)
if mibBuilder.loadTexts:statusSettings.setStatus(_B)
_ElementControl_ObjectIdentity=ObjectIdentity
elementControl=_ElementControl_ObjectIdentity((1,3,6,1,4,1,3715,99,1,3))
class _ControlResetElement_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3)))
_ControlResetElement_Type.__name__=_E
_ControlResetElement_Object=MibScalar
controlResetElement=_ControlResetElement_Object((1,3,6,1,4,1,3715,99,1,3,1),_ControlResetElement_Type())
controlResetElement.setMaxAccess(_D)
if mibBuilder.loadTexts:controlResetElement.setStatus(_B)
class _ControlBusMasterAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('master',1),('slave',2)))
_ControlBusMasterAdminState_Type.__name__=_E
_ControlBusMasterAdminState_Object=MibScalar
controlBusMasterAdminState=_ControlBusMasterAdminState_Object((1,3,6,1,4,1,3715,99,1,3,2),_ControlBusMasterAdminState_Type())
controlBusMasterAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:controlBusMasterAdminState.setStatus(_A)
class _ControlAlarmDetection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_J,2),('restart',3)))
_ControlAlarmDetection_Type.__name__=_E
_ControlAlarmDetection_Object=MibScalar
controlAlarmDetection=_ControlAlarmDetection_Object((1,3,6,1,4,1,3715,99,1,3,3),_ControlAlarmDetection_Type())
controlAlarmDetection.setMaxAccess(_D)
if mibBuilder.loadTexts:controlAlarmDetection.setStatus(_B)
_ControlMaxNumberTrapReceivers_Type=Integer32
_ControlMaxNumberTrapReceivers_Object=MibScalar
controlMaxNumberTrapReceivers=_ControlMaxNumberTrapReceivers_Object((1,3,6,1,4,1,3715,99,1,3,4),_ControlMaxNumberTrapReceivers_Type())
controlMaxNumberTrapReceivers.setMaxAccess(_C)
if mibBuilder.loadTexts:controlMaxNumberTrapReceivers.setStatus(_B)
_ControlTrapReceiverTable_Object=MibTable
controlTrapReceiverTable=_ControlTrapReceiverTable_Object((1,3,6,1,4,1,3715,99,1,3,5))
if mibBuilder.loadTexts:controlTrapReceiverTable.setStatus(_A)
_ControlTrapReceiverEntry_Object=MibTableRow
controlTrapReceiverEntry=_ControlTrapReceiverEntry_Object((1,3,6,1,4,1,3715,99,1,3,5,1))
controlTrapReceiverEntry.setIndexNames((0,_F,_Q))
if mibBuilder.loadTexts:controlTrapReceiverEntry.setStatus(_A)
class _ReceiverEntryId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_ReceiverEntryId_Type.__name__=_E
_ReceiverEntryId_Object=MibTableColumn
receiverEntryId=_ReceiverEntryId_Object((1,3,6,1,4,1,3715,99,1,3,5,1,1),_ReceiverEntryId_Type())
receiverEntryId.setMaxAccess(_C)
if mibBuilder.loadTexts:receiverEntryId.setStatus(_B)
_ReceiverAddress_Type=IpAddress
_ReceiverAddress_Object=MibTableColumn
receiverAddress=_ReceiverAddress_Object((1,3,6,1,4,1,3715,99,1,3,5,1,2),_ReceiverAddress_Type())
receiverAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:receiverAddress.setStatus(_B)
class _ReceiverPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ReceiverPort_Type.__name__=_E
_ReceiverPort_Object=MibTableColumn
receiverPort=_ReceiverPort_Object((1,3,6,1,4,1,3715,99,1,3,5,1,3),_ReceiverPort_Type())
receiverPort.setMaxAccess(_D)
if mibBuilder.loadTexts:receiverPort.setStatus(_B)
_ReceiverCommunity_Type=DisplayString
_ReceiverCommunity_Object=MibTableColumn
receiverCommunity=_ReceiverCommunity_Object((1,3,6,1,4,1,3715,99,1,3,5,1,4),_ReceiverCommunity_Type())
receiverCommunity.setMaxAccess(_D)
if mibBuilder.loadTexts:receiverCommunity.setStatus(_B)
class _ControlTrapSending_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_I,2)))
_ControlTrapSending_Type.__name__=_E
_ControlTrapSending_Object=MibScalar
controlTrapSending=_ControlTrapSending_Object((1,3,6,1,4,1,3715,99,1,3,6),_ControlTrapSending_Type())
controlTrapSending.setMaxAccess(_D)
if mibBuilder.loadTexts:controlTrapSending.setStatus(_A)
_ControlTrapInterval_Type=Integer32
_ControlTrapInterval_Object=MibScalar
controlTrapInterval=_ControlTrapInterval_Object((1,3,6,1,4,1,3715,99,1,3,7),_ControlTrapInterval_Type())
controlTrapInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:controlTrapInterval.setStatus(_A)
_ControlTrapLifeTime_Type=Integer32
_ControlTrapLifeTime_Object=MibScalar
controlTrapLifeTime=_ControlTrapLifeTime_Object((1,3,6,1,4,1,3715,99,1,3,8),_ControlTrapLifeTime_Type())
controlTrapLifeTime.setMaxAccess(_D)
if mibBuilder.loadTexts:controlTrapLifeTime.setStatus(_A)
_ControlAlarmOnDelay_Type=Integer32
_ControlAlarmOnDelay_Object=MibScalar
controlAlarmOnDelay=_ControlAlarmOnDelay_Object((1,3,6,1,4,1,3715,99,1,3,9),_ControlAlarmOnDelay_Type())
controlAlarmOnDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:controlAlarmOnDelay.setStatus(_A)
_ControlAlarmOffDelay_Type=Integer32
_ControlAlarmOffDelay_Object=MibScalar
controlAlarmOffDelay=_ControlAlarmOffDelay_Object((1,3,6,1,4,1,3715,99,1,3,10),_ControlAlarmOffDelay_Type())
controlAlarmOffDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:controlAlarmOffDelay.setStatus(_A)
_ControlTrapDelay_Type=Integer32
_ControlTrapDelay_Object=MibScalar
controlTrapDelay=_ControlTrapDelay_Object((1,3,6,1,4,1,3715,99,1,3,11),_ControlTrapDelay_Type())
controlTrapDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:controlTrapDelay.setStatus(_A)
_ElementProductKey_ObjectIdentity=ObjectIdentity
elementProductKey=_ElementProductKey_ObjectIdentity((1,3,6,1,4,1,3715,99,1,4))
_ProductKeyNumberOfKeys_Type=Integer32
_ProductKeyNumberOfKeys_Object=MibScalar
productKeyNumberOfKeys=_ProductKeyNumberOfKeys_Object((1,3,6,1,4,1,3715,99,1,4,4),_ProductKeyNumberOfKeys_Type())
productKeyNumberOfKeys.setMaxAccess(_C)
if mibBuilder.loadTexts:productKeyNumberOfKeys.setStatus(_A)
_ProductKeyTable_Object=MibTable
productKeyTable=_ProductKeyTable_Object((1,3,6,1,4,1,3715,99,1,4,5))
if mibBuilder.loadTexts:productKeyTable.setStatus(_B)
_ProductKeyEntry_Object=MibTableRow
productKeyEntry=_ProductKeyEntry_Object((1,3,6,1,4,1,3715,99,1,4,5,1))
productKeyEntry.setIndexNames((0,_F,_K))
if mibBuilder.loadTexts:productKeyEntry.setStatus(_B)
class _ProductKeyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_ProductKeyIndex_Type.__name__=_E
_ProductKeyIndex_Object=MibTableColumn
productKeyIndex=_ProductKeyIndex_Object((1,3,6,1,4,1,3715,99,1,4,5,1,1),_ProductKeyIndex_Type())
productKeyIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:productKeyIndex.setStatus(_B)
_ProductKeyValue_Type=OctetString
_ProductKeyValue_Object=MibTableColumn
productKeyValue=_ProductKeyValue_Object((1,3,6,1,4,1,3715,99,1,4,5,1,2),_ProductKeyValue_Type())
productKeyValue.setMaxAccess(_D)
if mibBuilder.loadTexts:productKeyValue.setStatus(_B)
_ProductKeyMask_Type=OctetString
_ProductKeyMask_Object=MibTableColumn
productKeyMask=_ProductKeyMask_Object((1,3,6,1,4,1,3715,99,1,4,5,1,3),_ProductKeyMask_Type())
productKeyMask.setMaxAccess(_C)
if mibBuilder.loadTexts:productKeyMask.setStatus(_B)
class _ProductKeyStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('keyInvalid',1),('keyValid',2)))
_ProductKeyStatus_Type.__name__=_E
_ProductKeyStatus_Object=MibTableColumn
productKeyStatus=_ProductKeyStatus_Object((1,3,6,1,4,1,3715,99,1,4,5,1,4),_ProductKeyStatus_Type())
productKeyStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:productKeyStatus.setStatus(_B)
class _ProductKeyCipher_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('cipherOther',1),('cipherBlowFish',2),('cipherXXTEA',3)))
_ProductKeyCipher_Type.__name__=_E
_ProductKeyCipher_Object=MibTableColumn
productKeyCipher=_ProductKeyCipher_Object((1,3,6,1,4,1,3715,99,1,4,5,1,5),_ProductKeyCipher_Type())
productKeyCipher.setMaxAccess(_C)
if mibBuilder.loadTexts:productKeyCipher.setStatus(_B)
_ProductKeyNumberOfFeatures_Type=Integer32
_ProductKeyNumberOfFeatures_Object=MibTableColumn
productKeyNumberOfFeatures=_ProductKeyNumberOfFeatures_Object((1,3,6,1,4,1,3715,99,1,4,5,1,6),_ProductKeyNumberOfFeatures_Type())
productKeyNumberOfFeatures.setMaxAccess(_C)
if mibBuilder.loadTexts:productKeyNumberOfFeatures.setStatus(_B)
_ProductKeyFeatureTable_Object=MibTable
productKeyFeatureTable=_ProductKeyFeatureTable_Object((1,3,6,1,4,1,3715,99,1,4,6))
if mibBuilder.loadTexts:productKeyFeatureTable.setStatus(_B)
_ProductKeyFeatureEntry_Object=MibTableRow
productKeyFeatureEntry=_ProductKeyFeatureEntry_Object((1,3,6,1,4,1,3715,99,1,4,6,1))
productKeyFeatureEntry.setIndexNames((0,_F,_K),(0,_F,_R))
if mibBuilder.loadTexts:productKeyFeatureEntry.setStatus(_B)
class _ProductKeyFeatureIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_ProductKeyFeatureIndex_Type.__name__=_E
_ProductKeyFeatureIndex_Object=MibTableColumn
productKeyFeatureIndex=_ProductKeyFeatureIndex_Object((1,3,6,1,4,1,3715,99,1,4,6,1,1),_ProductKeyFeatureIndex_Type())
productKeyFeatureIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:productKeyFeatureIndex.setStatus(_B)
_ProductKeyFeatureName_Type=OctetString
_ProductKeyFeatureName_Object=MibTableColumn
productKeyFeatureName=_ProductKeyFeatureName_Object((1,3,6,1,4,1,3715,99,1,4,6,1,2),_ProductKeyFeatureName_Type())
productKeyFeatureName.setMaxAccess(_C)
if mibBuilder.loadTexts:productKeyFeatureName.setStatus(_B)
class _ProductKeyFeatureEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('featureDisable',1),('featureEnable',2)))
_ProductKeyFeatureEnable_Type.__name__=_E
_ProductKeyFeatureEnable_Object=MibTableColumn
productKeyFeatureEnable=_ProductKeyFeatureEnable_Object((1,3,6,1,4,1,3715,99,1,4,6,1,3),_ProductKeyFeatureEnable_Type())
productKeyFeatureEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:productKeyFeatureEnable.setStatus(_B)
_ProductKeyFeatureExpirationTime_Type=Integer32
_ProductKeyFeatureExpirationTime_Object=MibTableColumn
productKeyFeatureExpirationTime=_ProductKeyFeatureExpirationTime_Object((1,3,6,1,4,1,3715,99,1,4,6,1,4),_ProductKeyFeatureExpirationTime_Type())
productKeyFeatureExpirationTime.setMaxAccess(_C)
if mibBuilder.loadTexts:productKeyFeatureExpirationTime.setStatus(_B)
_Module_ObjectIdentity=ObjectIdentity
module=_Module_ObjectIdentity((1,3,6,1,4,1,3715,99,2))
_ModuleInformation_ObjectIdentity=ObjectIdentity
moduleInformation=_ModuleInformation_ObjectIdentity((1,3,6,1,4,1,3715,99,2,1))
_ModuleTable_Object=MibTable
moduleTable=_ModuleTable_Object((1,3,6,1,4,1,3715,99,2,1,1))
if mibBuilder.loadTexts:moduleTable.setStatus(_B)
_ModuleEntry_Object=MibTableRow
moduleEntry=_ModuleEntry_Object((1,3,6,1,4,1,3715,99,2,1,1,1))
moduleEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:moduleEntry.setStatus(_B)
class _ModuleId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_ModuleId_Type.__name__=_E
_ModuleId_Object=MibTableColumn
moduleId=_ModuleId_Object((1,3,6,1,4,1,3715,99,2,1,1,1,1),_ModuleId_Type())
moduleId.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleId.setStatus(_B)
_ModuleName_Type=DisplayString
_ModuleName_Object=MibTableColumn
moduleName=_ModuleName_Object((1,3,6,1,4,1,3715,99,2,1,1,1,2),_ModuleName_Type())
moduleName.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleName.setStatus(_A)
_ModuleHwType_Type=DisplayString
_ModuleHwType_Object=MibTableColumn
moduleHwType=_ModuleHwType_Object((1,3,6,1,4,1,3715,99,2,1,1,1,3),_ModuleHwType_Type())
moduleHwType.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleHwType.setStatus(_B)
_ModuleRackNo_Type=Integer32
_ModuleRackNo_Object=MibTableColumn
moduleRackNo=_ModuleRackNo_Object((1,3,6,1,4,1,3715,99,2,1,1,1,4),_ModuleRackNo_Type())
moduleRackNo.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleRackNo.setStatus(_A)
_ModuleSlotNo_Type=Integer32
_ModuleSlotNo_Object=MibTableColumn
moduleSlotNo=_ModuleSlotNo_Object((1,3,6,1,4,1,3715,99,2,1,1,1,5),_ModuleSlotNo_Type())
moduleSlotNo.setMaxAccess(_D)
if mibBuilder.loadTexts:moduleSlotNo.setStatus(_A)
_ModuleDetailTable_Object=MibTable
moduleDetailTable=_ModuleDetailTable_Object((1,3,6,1,4,1,3715,99,2,1,2))
if mibBuilder.loadTexts:moduleDetailTable.setStatus(_B)
_ModuleDetailEntry_Object=MibTableRow
moduleDetailEntry=_ModuleDetailEntry_Object((1,3,6,1,4,1,3715,99,2,1,2,1))
moduleDetailEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:moduleDetailEntry.setStatus(_B)
_ModuleMacAddress_Type=TPhysAddress
_ModuleMacAddress_Object=MibTableColumn
moduleMacAddress=_ModuleMacAddress_Object((1,3,6,1,4,1,3715,99,2,1,2,1,1),_ModuleMacAddress_Type())
moduleMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleMacAddress.setStatus(_A)
_ModuleBusAddress_Type=Integer32
_ModuleBusAddress_Object=MibTableColumn
moduleBusAddress=_ModuleBusAddress_Object((1,3,6,1,4,1,3715,99,2,1,2,1,2),_ModuleBusAddress_Type())
moduleBusAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleBusAddress.setStatus(_A)
_ModuleAppDate_Type=DateAndTime
_ModuleAppDate_Object=MibTableColumn
moduleAppDate=_ModuleAppDate_Object((1,3,6,1,4,1,3715,99,2,1,2,1,3),_ModuleAppDate_Type())
moduleAppDate.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleAppDate.setStatus(_B)
_ModuleAppVersion_Type=DisplayString
_ModuleAppVersion_Object=MibTableColumn
moduleAppVersion=_ModuleAppVersion_Object((1,3,6,1,4,1,3715,99,2,1,2,1,4),_ModuleAppVersion_Type())
moduleAppVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleAppVersion.setStatus(_B)
_ModuleBiosDate_Type=DateAndTime
_ModuleBiosDate_Object=MibTableColumn
moduleBiosDate=_ModuleBiosDate_Object((1,3,6,1,4,1,3715,99,2,1,2,1,5),_ModuleBiosDate_Type())
moduleBiosDate.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleBiosDate.setStatus(_B)
_ModuleBiosVersion_Type=DisplayString
_ModuleBiosVersion_Object=MibTableColumn
moduleBiosVersion=_ModuleBiosVersion_Object((1,3,6,1,4,1,3715,99,2,1,2,1,6),_ModuleBiosVersion_Type())
moduleBiosVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleBiosVersion.setStatus(_B)
_ModuleHwSerialNumber_Type=DisplayString
_ModuleHwSerialNumber_Object=MibTableColumn
moduleHwSerialNumber=_ModuleHwSerialNumber_Object((1,3,6,1,4,1,3715,99,2,1,2,1,7),_ModuleHwSerialNumber_Type())
moduleHwSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleHwSerialNumber.setStatus(_B)
_ModuleHwVersion_Type=DisplayString
_ModuleHwVersion_Object=MibTableColumn
moduleHwVersion=_ModuleHwVersion_Object((1,3,6,1,4,1,3715,99,2,1,2,1,8),_ModuleHwVersion_Type())
moduleHwVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:moduleHwVersion.setStatus(_B)
_ModuleStatus_ObjectIdentity=ObjectIdentity
moduleStatus=_ModuleStatus_ObjectIdentity((1,3,6,1,4,1,3715,99,2,2))
_ModuleStatusTable_Object=MibTable
moduleStatusTable=_ModuleStatusTable_Object((1,3,6,1,4,1,3715,99,2,2,1))
if mibBuilder.loadTexts:moduleStatusTable.setStatus(_B)
_ModuleStatusEntry_Object=MibTableRow
moduleStatusEntry=_ModuleStatusEntry_Object((1,3,6,1,4,1,3715,99,2,2,1,1))
moduleStatusEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:moduleStatusEntry.setStatus(_B)
class _StatusResetCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_L,1),('selfReset',2),('powerReset',3),('commandedReset',4),('softdownloadReset',5)))
_StatusResetCause_Type.__name__=_E
_StatusResetCause_Object=MibTableColumn
statusResetCause=_StatusResetCause_Object((1,3,6,1,4,1,3715,99,2,2,1,1,1),_StatusResetCause_Type())
statusResetCause.setMaxAccess(_C)
if mibBuilder.loadTexts:statusResetCause.setStatus(_B)
_StatusRunningSwImage_Type=Integer32
_StatusRunningSwImage_Object=MibTableColumn
statusRunningSwImage=_StatusRunningSwImage_Object((1,3,6,1,4,1,3715,99,2,2,1,1,2),_StatusRunningSwImage_Type())
statusRunningSwImage.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRunningSwImage.setStatus(_B)
class _StatusInternalTemperature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-600,1300))
_StatusInternalTemperature_Type.__name__=_E
_StatusInternalTemperature_Object=MibTableColumn
statusInternalTemperature=_StatusInternalTemperature_Object((1,3,6,1,4,1,3715,99,2,2,1,1,3),_StatusInternalTemperature_Type())
statusInternalTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:statusInternalTemperature.setStatus(_B)
class _StatusLidStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noLid',1),(_M,2),('open',3)))
_StatusLidStatus_Type.__name__=_E
_StatusLidStatus_Object=MibTableColumn
statusLidStatus=_StatusLidStatus_Object((1,3,6,1,4,1,3715,99,2,2,1,1,4),_StatusLidStatus_Type())
statusLidStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:statusLidStatus.setStatus(_A)
_StatusRestartCounter_Type=Counter32
_StatusRestartCounter_Object=MibTableColumn
statusRestartCounter=_StatusRestartCounter_Object((1,3,6,1,4,1,3715,99,2,2,1,1,5),_StatusRestartCounter_Type())
statusRestartCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:statusRestartCounter.setStatus(_A)
_ModuleControl_ObjectIdentity=ObjectIdentity
moduleControl=_ModuleControl_ObjectIdentity((1,3,6,1,4,1,3715,99,2,3))
_ModuleControlTable_Object=MibTable
moduleControlTable=_ModuleControlTable_Object((1,3,6,1,4,1,3715,99,2,3,1))
if mibBuilder.loadTexts:moduleControlTable.setStatus(_A)
_ModuleControlEntry_Object=MibTableRow
moduleControlEntry=_ModuleControlEntry_Object((1,3,6,1,4,1,3715,99,2,3,1,1))
moduleControlEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:moduleControlEntry.setStatus(_A)
class _ControlLedUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),('alwaysOn',2),('offWhenLidClosed',3)))
_ControlLedUsage_Type.__name__=_E
_ControlLedUsage_Object=MibTableColumn
controlLedUsage=_ControlLedUsage_Object((1,3,6,1,4,1,3715,99,2,3,1,1,1),_ControlLedUsage_Type())
controlLedUsage.setMaxAccess(_D)
if mibBuilder.loadTexts:controlLedUsage.setStatus(_A)
class _ControlMarkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),('on',2),('off',3)))
_ControlMarkState_Type.__name__=_E
_ControlMarkState_Object=MibTableColumn
controlMarkState=_ControlMarkState_Object((1,3,6,1,4,1,3715,99,2,3,1,1,2),_ControlMarkState_Type())
controlMarkState.setMaxAccess(_D)
if mibBuilder.loadTexts:controlMarkState.setStatus(_A)
class _ControlReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),(_O,2),(_P,3)))
_ControlReset_Type.__name__=_E
_ControlReset_Object=MibTableColumn
controlReset=_ControlReset_Object((1,3,6,1,4,1,3715,99,2,3,1,1,3),_ControlReset_Type())
controlReset.setMaxAccess(_D)
if mibBuilder.loadTexts:controlReset.setStatus(_A)
_ControlTempLimitHiHi_Type=Integer32
_ControlTempLimitHiHi_Object=MibTableColumn
controlTempLimitHiHi=_ControlTempLimitHiHi_Object((1,3,6,1,4,1,3715,99,2,3,1,1,4),_ControlTempLimitHiHi_Type())
controlTempLimitHiHi.setMaxAccess(_D)
if mibBuilder.loadTexts:controlTempLimitHiHi.setStatus(_A)
_ControlTempLimitHi_Type=Integer32
_ControlTempLimitHi_Object=MibTableColumn
controlTempLimitHi=_ControlTempLimitHi_Object((1,3,6,1,4,1,3715,99,2,3,1,1,5),_ControlTempLimitHi_Type())
controlTempLimitHi.setMaxAccess(_D)
if mibBuilder.loadTexts:controlTempLimitHi.setStatus(_A)
_ControlTempLimitLo_Type=Integer32
_ControlTempLimitLo_Object=MibTableColumn
controlTempLimitLo=_ControlTempLimitLo_Object((1,3,6,1,4,1,3715,99,2,3,1,1,7),_ControlTempLimitLo_Type())
controlTempLimitLo.setMaxAccess(_D)
if mibBuilder.loadTexts:controlTempLimitLo.setStatus(_A)
_ControlTempLimitLoLo_Type=Integer32
_ControlTempLimitLoLo_Object=MibTableColumn
controlTempLimitLoLo=_ControlTempLimitLoLo_Object((1,3,6,1,4,1,3715,99,2,3,1,1,8),_ControlTempLimitLoLo_Type())
controlTempLimitLoLo.setMaxAccess(_D)
if mibBuilder.loadTexts:controlTempLimitLoLo.setStatus(_A)
_ControlTempDeadBand_Type=Integer32
_ControlTempDeadBand_Object=MibTableColumn
controlTempDeadBand=_ControlTempDeadBand_Object((1,3,6,1,4,1,3715,99,2,3,1,1,9),_ControlTempDeadBand_Type())
controlTempDeadBand.setMaxAccess(_D)
if mibBuilder.loadTexts:controlTempDeadBand.setStatus(_A)
class _ControlInternalAppAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('allowIntControl',1),('denyIntControl',2)))
_ControlInternalAppAccess_Type.__name__=_E
_ControlInternalAppAccess_Object=MibTableColumn
controlInternalAppAccess=_ControlInternalAppAccess_Object((1,3,6,1,4,1,3715,99,2,3,1,1,10),_ControlInternalAppAccess_Type())
controlInternalAppAccess.setMaxAccess(_D)
if mibBuilder.loadTexts:controlInternalAppAccess.setStatus(_A)
class _ControlLocalAccess_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_ControlLocalAccess_Type.__name__=_E
_ControlLocalAccess_Object=MibTableColumn
controlLocalAccess=_ControlLocalAccess_Object((1,3,6,1,4,1,3715,99,2,3,1,1,11),_ControlLocalAccess_Type())
controlLocalAccess.setMaxAccess(_D)
if mibBuilder.loadTexts:controlLocalAccess.setStatus(_A)
_ModuleSWUpdateTable_Object=MibTable
moduleSWUpdateTable=_ModuleSWUpdateTable_Object((1,3,6,1,4,1,3715,99,2,3,2))
if mibBuilder.loadTexts:moduleSWUpdateTable.setStatus(_A)
_ModuleSWUpdateEntry_Object=MibTableRow
moduleSWUpdateEntry=_ModuleSWUpdateEntry_Object((1,3,6,1,4,1,3715,99,2,3,2,1))
moduleSWUpdateEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:moduleSWUpdateEntry.setStatus(_A)
class _SWUpdateControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('updateIdle',1),('updateRunning',2),('updateFailed',3),('updateStart',4)))
_SWUpdateControl_Type.__name__=_E
_SWUpdateControl_Object=MibTableColumn
sWUpdateControl=_SWUpdateControl_Object((1,3,6,1,4,1,3715,99,2,3,2,1,1),_SWUpdateControl_Type())
sWUpdateControl.setMaxAccess(_D)
if mibBuilder.loadTexts:sWUpdateControl.setStatus(_A)
_SwUpdateURL_Type=DisplayString
_SwUpdateURL_Object=MibTableColumn
swUpdateURL=_SwUpdateURL_Object((1,3,6,1,4,1,3715,99,2,3,2,1,2),_SwUpdateURL_Type())
swUpdateURL.setMaxAccess(_D)
if mibBuilder.loadTexts:swUpdateURL.setStatus(_A)
_SWUpdateFileName_Type=DisplayString
_SWUpdateFileName_Object=MibTableColumn
sWUpdateFileName=_SWUpdateFileName_Object((1,3,6,1,4,1,3715,99,2,3,2,1,3),_SWUpdateFileName_Type())
sWUpdateFileName.setMaxAccess(_D)
if mibBuilder.loadTexts:sWUpdateFileName.setStatus(_A)
_SWUpdateStatus_Type=DisplayString
_SWUpdateStatus_Object=MibTableColumn
sWUpdateStatus=_SWUpdateStatus_Object((1,3,6,1,4,1,3715,99,2,3,2,1,4),_SWUpdateStatus_Type())
sWUpdateStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sWUpdateStatus.setStatus(_A)
_ModuleRegistry_ObjectIdentity=ObjectIdentity
moduleRegistry=_ModuleRegistry_ObjectIdentity((1,3,6,1,4,1,3715,99,2,4))
_ModuleSizeOfTable_Object=MibTable
moduleSizeOfTable=_ModuleSizeOfTable_Object((1,3,6,1,4,1,3715,99,2,4,1))
if mibBuilder.loadTexts:moduleSizeOfTable.setStatus(_A)
_ModuleSizeOfEntry_Object=MibTableRow
moduleSizeOfEntry=_ModuleSizeOfEntry_Object((1,3,6,1,4,1,3715,99,2,4,1,1))
moduleSizeOfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:moduleSizeOfEntry.setStatus(_A)
_SizeOfRegistry_Type=Integer32
_SizeOfRegistry_Object=MibTableColumn
sizeOfRegistry=_SizeOfRegistry_Object((1,3,6,1,4,1,3715,99,2,4,1,1,1),_SizeOfRegistry_Type())
sizeOfRegistry.setMaxAccess(_C)
if mibBuilder.loadTexts:sizeOfRegistry.setStatus(_B)
_SizeOfRepairlog_Type=Integer32
_SizeOfRepairlog_Object=MibTableColumn
sizeOfRepairlog=_SizeOfRepairlog_Object((1,3,6,1,4,1,3715,99,2,4,1,1,2),_SizeOfRepairlog_Type())
sizeOfRepairlog.setMaxAccess(_C)
if mibBuilder.loadTexts:sizeOfRepairlog.setStatus(_A)
_SizeOfNotebook_Type=Integer32
_SizeOfNotebook_Object=MibTableColumn
sizeOfNotebook=_SizeOfNotebook_Object((1,3,6,1,4,1,3715,99,2,4,1,1,3),_SizeOfNotebook_Type())
sizeOfNotebook.setMaxAccess(_C)
if mibBuilder.loadTexts:sizeOfNotebook.setStatus(_A)
_ModuleRegistryTable_Object=MibTable
moduleRegistryTable=_ModuleRegistryTable_Object((1,3,6,1,4,1,3715,99,2,4,2))
if mibBuilder.loadTexts:moduleRegistryTable.setStatus(_A)
_ModuleRegistryEntry_Object=MibTableRow
moduleRegistryEntry=_ModuleRegistryEntry_Object((1,3,6,1,4,1,3715,99,2,4,2,1))
moduleRegistryEntry.setIndexNames((0,_F,_G),(0,_F,_T))
if mibBuilder.loadTexts:moduleRegistryEntry.setStatus(_A)
class _RegIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_RegIndex_Type.__name__=_E
_RegIndex_Object=MibTableColumn
regIndex=_RegIndex_Object((1,3,6,1,4,1,3715,99,2,4,2,1,1),_RegIndex_Type())
regIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:regIndex.setStatus(_A)
_RegName_Type=DisplayString
_RegName_Object=MibTableColumn
regName=_RegName_Object((1,3,6,1,4,1,3715,99,2,4,2,1,2),_RegName_Type())
regName.setMaxAccess(_D)
if mibBuilder.loadTexts:regName.setStatus(_A)
_RegValue_Type=DisplayString
_RegValue_Object=MibTableColumn
regValue=_RegValue_Object((1,3,6,1,4,1,3715,99,2,4,2,1,3),_RegValue_Type())
regValue.setMaxAccess(_D)
if mibBuilder.loadTexts:regValue.setStatus(_A)
_ModuleRepairLogTable_Object=MibTable
moduleRepairLogTable=_ModuleRepairLogTable_Object((1,3,6,1,4,1,3715,99,2,4,3))
if mibBuilder.loadTexts:moduleRepairLogTable.setStatus(_A)
_ModuleRepairLogEntry_Object=MibTableRow
moduleRepairLogEntry=_ModuleRepairLogEntry_Object((1,3,6,1,4,1,3715,99,2,4,3,1))
moduleRepairLogEntry.setIndexNames((0,_F,_G),(0,_F,_U))
if mibBuilder.loadTexts:moduleRepairLogEntry.setStatus(_A)
class _RepairIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_RepairIndex_Type.__name__=_E
_RepairIndex_Object=MibTableColumn
repairIndex=_RepairIndex_Object((1,3,6,1,4,1,3715,99,2,4,3,1,1),_RepairIndex_Type())
repairIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:repairIndex.setStatus(_A)
_RepairDate_Type=DisplayString
_RepairDate_Object=MibTableColumn
repairDate=_RepairDate_Object((1,3,6,1,4,1,3715,99,2,4,3,1,2),_RepairDate_Type())
repairDate.setMaxAccess(_D)
if mibBuilder.loadTexts:repairDate.setStatus(_A)
class _RepairReasonCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_RepairReasonCode_Type.__name__=_H
_RepairReasonCode_Object=MibTableColumn
repairReasonCode=_RepairReasonCode_Object((1,3,6,1,4,1,3715,99,2,4,3,1,3),_RepairReasonCode_Type())
repairReasonCode.setMaxAccess(_D)
if mibBuilder.loadTexts:repairReasonCode.setStatus(_A)
class _RepairNameCode_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_RepairNameCode_Type.__name__=_H
_RepairNameCode_Object=MibTableColumn
repairNameCode=_RepairNameCode_Object((1,3,6,1,4,1,3715,99,2,4,3,1,4),_RepairNameCode_Type())
repairNameCode.setMaxAccess(_D)
if mibBuilder.loadTexts:repairNameCode.setStatus(_A)
_RepairComment_Type=DisplayString
_RepairComment_Object=MibTableColumn
repairComment=_RepairComment_Object((1,3,6,1,4,1,3715,99,2,4,3,1,5),_RepairComment_Type())
repairComment.setMaxAccess(_D)
if mibBuilder.loadTexts:repairComment.setStatus(_A)
_ModuleNotebookTable_Object=MibTable
moduleNotebookTable=_ModuleNotebookTable_Object((1,3,6,1,4,1,3715,99,2,4,4))
if mibBuilder.loadTexts:moduleNotebookTable.setStatus(_A)
_ModuleNotebookEntry_Object=MibTableRow
moduleNotebookEntry=_ModuleNotebookEntry_Object((1,3,6,1,4,1,3715,99,2,4,4,1))
moduleNotebookEntry.setIndexNames((0,_F,_G),(0,_F,_V))
if mibBuilder.loadTexts:moduleNotebookEntry.setStatus(_A)
class _NotebookLineNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_NotebookLineNumber_Type.__name__=_E
_NotebookLineNumber_Object=MibTableColumn
notebookLineNumber=_NotebookLineNumber_Object((1,3,6,1,4,1,3715,99,2,4,4,1,1),_NotebookLineNumber_Type())
notebookLineNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:notebookLineNumber.setStatus(_A)
class _NotebookLineText_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_NotebookLineText_Type.__name__=_H
_NotebookLineText_Object=MibTableColumn
notebookLineText=_NotebookLineText_Object((1,3,6,1,4,1,3715,99,2,4,4,1,2),_NotebookLineText_Type())
notebookLineText.setMaxAccess(_D)
if mibBuilder.loadTexts:notebookLineText.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'element':element,'elementInformation':elementInformation,'elementName':elementName,'elementStructure':elementStructure,'elementConfigChangeCode':elementConfigChangeCode,'elementResetCount':elementResetCount,'elementTotalUpTime':elementTotalUpTime,'elementLatitude':elementLatitude,'elementLongitude':elementLongitude,'elementAltitude':elementAltitude,'elementStatus':elementStatus,'statusGeneral':statusGeneral,'statusBusMaster':statusBusMaster,'statusLmt':statusLmt,'statusLid':statusLid,'statusTemperature':statusTemperature,'statusFan':statusFan,'statusHardware':statusHardware,'statusSoftware':statusSoftware,'statusSettings':statusSettings,'elementControl':elementControl,'controlResetElement':controlResetElement,'controlBusMasterAdminState':controlBusMasterAdminState,'controlAlarmDetection':controlAlarmDetection,'controlMaxNumberTrapReceivers':controlMaxNumberTrapReceivers,'controlTrapReceiverTable':controlTrapReceiverTable,'controlTrapReceiverEntry':controlTrapReceiverEntry,_Q:receiverEntryId,'receiverAddress':receiverAddress,'receiverPort':receiverPort,'receiverCommunity':receiverCommunity,'controlTrapSending':controlTrapSending,'controlTrapInterval':controlTrapInterval,'controlTrapLifeTime':controlTrapLifeTime,'controlAlarmOnDelay':controlAlarmOnDelay,'controlAlarmOffDelay':controlAlarmOffDelay,'controlTrapDelay':controlTrapDelay,'elementProductKey':elementProductKey,'productKeyNumberOfKeys':productKeyNumberOfKeys,'productKeyTable':productKeyTable,'productKeyEntry':productKeyEntry,_K:productKeyIndex,'productKeyValue':productKeyValue,'productKeyMask':productKeyMask,'productKeyStatus':productKeyStatus,'productKeyCipher':productKeyCipher,'productKeyNumberOfFeatures':productKeyNumberOfFeatures,'productKeyFeatureTable':productKeyFeatureTable,'productKeyFeatureEntry':productKeyFeatureEntry,_R:productKeyFeatureIndex,'productKeyFeatureName':productKeyFeatureName,'productKeyFeatureEnable':productKeyFeatureEnable,'productKeyFeatureExpirationTime':productKeyFeatureExpirationTime,'module':module,'moduleInformation':moduleInformation,'moduleTable':moduleTable,'moduleEntry':moduleEntry,_G:moduleId,'moduleName':moduleName,'moduleHwType':moduleHwType,'moduleRackNo':moduleRackNo,'moduleSlotNo':moduleSlotNo,'moduleDetailTable':moduleDetailTable,'moduleDetailEntry':moduleDetailEntry,'moduleMacAddress':moduleMacAddress,'moduleBusAddress':moduleBusAddress,'moduleAppDate':moduleAppDate,'moduleAppVersion':moduleAppVersion,'moduleBiosDate':moduleBiosDate,'moduleBiosVersion':moduleBiosVersion,'moduleHwSerialNumber':moduleHwSerialNumber,'moduleHwVersion':moduleHwVersion,'moduleStatus':moduleStatus,'moduleStatusTable':moduleStatusTable,'moduleStatusEntry':moduleStatusEntry,'statusResetCause':statusResetCause,'statusRunningSwImage':statusRunningSwImage,'statusInternalTemperature':statusInternalTemperature,'statusLidStatus':statusLidStatus,'statusRestartCounter':statusRestartCounter,'moduleControl':moduleControl,'moduleControlTable':moduleControlTable,'moduleControlEntry':moduleControlEntry,'controlLedUsage':controlLedUsage,'controlMarkState':controlMarkState,'controlReset':controlReset,'controlTempLimitHiHi':controlTempLimitHiHi,'controlTempLimitHi':controlTempLimitHi,'controlTempLimitLo':controlTempLimitLo,'controlTempLimitLoLo':controlTempLimitLoLo,'controlTempDeadBand':controlTempDeadBand,'controlInternalAppAccess':controlInternalAppAccess,'controlLocalAccess':controlLocalAccess,'moduleSWUpdateTable':moduleSWUpdateTable,'moduleSWUpdateEntry':moduleSWUpdateEntry,'sWUpdateControl':sWUpdateControl,'swUpdateURL':swUpdateURL,'sWUpdateFileName':sWUpdateFileName,'sWUpdateStatus':sWUpdateStatus,'moduleRegistry':moduleRegistry,'moduleSizeOfTable':moduleSizeOfTable,'moduleSizeOfEntry':moduleSizeOfEntry,'sizeOfRegistry':sizeOfRegistry,'sizeOfRepairlog':sizeOfRepairlog,'sizeOfNotebook':sizeOfNotebook,'moduleRegistryTable':moduleRegistryTable,'moduleRegistryEntry':moduleRegistryEntry,_T:regIndex,'regName':regName,'regValue':regValue,'moduleRepairLogTable':moduleRepairLogTable,'moduleRepairLogEntry':moduleRepairLogEntry,_U:repairIndex,'repairDate':repairDate,'repairReasonCode':repairReasonCode,'repairNameCode':repairNameCode,'repairComment':repairComment,'moduleNotebookTable':moduleNotebookTable,'moduleNotebookEntry':moduleNotebookEntry,_V:notebookLineNumber,'notebookLineText':notebookLineText})