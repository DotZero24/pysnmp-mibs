_M='productStatusTimeStamp'
_L='productStatusLastGlobalStatus'
_K='productStatusGlobalStatus'
_J='envMonSupplyStatusIndex'
_I='envMonFanStatusIndex'
_H='non-critical'
_G='productIdentificationPerBoxIndex'
_F='critical'
_E='DisplayString'
_D='Dell-Vendor-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_E,'PhysAddress','RowStatus','TextualConvention')
powerConnectVendorMIB=ModuleIdentity((1,3,6,1,4,1,674,10895,3000))
if mibBuilder.loadTexts:powerConnectVendorMIB.setRevisions(('2012-05-07 12:00',))
class EnvMonState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('normal',1),('warning',2),(_F,3),('shutdown',4),('notPresent',5),('notFunctioning',6)))
_Dell_ObjectIdentity=ObjectIdentity
dell=_Dell_ObjectIdentity((1,3,6,1,4,1,674))
_DellLan_ObjectIdentity=ObjectIdentity
dellLan=_DellLan_ObjectIdentity((1,3,6,1,4,1,674,10895))
_DellVendorMIBObjects_ObjectIdentity=ObjectIdentity
dellVendorMIBObjects=_DellVendorMIBObjects_ObjectIdentity((1,3,6,1,4,1,674,10895,3000,1))
_Hardware_ObjectIdentity=ObjectIdentity
hardware=_Hardware_ObjectIdentity((1,3,6,1,4,1,674,10895,3000,1,2))
_ProductIdentification_ObjectIdentity=ObjectIdentity
productIdentification=_ProductIdentification_ObjectIdentity((1,3,6,1,4,1,674,10895,3000,1,2,100))
_ProductIdentificationDisplayName_Type=DisplayString
_ProductIdentificationDisplayName_Object=MibScalar
productIdentificationDisplayName=_ProductIdentificationDisplayName_Object((1,3,6,1,4,1,674,10895,3000,1,2,100,1),_ProductIdentificationDisplayName_Type())
productIdentificationDisplayName.setMaxAccess(_B)
if mibBuilder.loadTexts:productIdentificationDisplayName.setStatus(_A)
_ProductIdentificationDescription_Type=DisplayString
_ProductIdentificationDescription_Object=MibScalar
productIdentificationDescription=_ProductIdentificationDescription_Object((1,3,6,1,4,1,674,10895,3000,1,2,100,2),_ProductIdentificationDescription_Type())
productIdentificationDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:productIdentificationDescription.setStatus(_A)
_ProductIdentificationVendor_Type=DisplayString
_ProductIdentificationVendor_Object=MibScalar
productIdentificationVendor=_ProductIdentificationVendor_Object((1,3,6,1,4,1,674,10895,3000,1,2,100,3),_ProductIdentificationVendor_Type())
productIdentificationVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:productIdentificationVendor.setStatus(_A)
_ProductIdentificationVersion_Type=DisplayString
_ProductIdentificationVersion_Object=MibScalar
productIdentificationVersion=_ProductIdentificationVersion_Object((1,3,6,1,4,1,674,10895,3000,1,2,100,4),_ProductIdentificationVersion_Type())
productIdentificationVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:productIdentificationVersion.setStatus(_A)
_ProductIdentificationBuildNumber_Type=DisplayString
_ProductIdentificationBuildNumber_Object=MibScalar
productIdentificationBuildNumber=_ProductIdentificationBuildNumber_Object((1,3,6,1,4,1,674,10895,3000,1,2,100,5),_ProductIdentificationBuildNumber_Type())
productIdentificationBuildNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:productIdentificationBuildNumber.setStatus(_A)
_ProductIdentificationURL_Type=DisplayString
_ProductIdentificationURL_Object=MibScalar
productIdentificationURL=_ProductIdentificationURL_Object((1,3,6,1,4,1,674,10895,3000,1,2,100,6),_ProductIdentificationURL_Type())
productIdentificationURL.setMaxAccess(_B)
if mibBuilder.loadTexts:productIdentificationURL.setStatus(_A)
_ProductIdentificationDeviceNetworkName_Type=DisplayString
_ProductIdentificationDeviceNetworkName_Object=MibScalar
productIdentificationDeviceNetworkName=_ProductIdentificationDeviceNetworkName_Object((1,3,6,1,4,1,674,10895,3000,1,2,100,7),_ProductIdentificationDeviceNetworkName_Type())
productIdentificationDeviceNetworkName.setMaxAccess(_B)
if mibBuilder.loadTexts:productIdentificationDeviceNetworkName.setStatus(_A)
_ProductIdentificationPerUnitTable_Object=MibTable
productIdentificationPerUnitTable=_ProductIdentificationPerUnitTable_Object((1,3,6,1,4,1,674,10895,3000,1,2,100,8))
if mibBuilder.loadTexts:productIdentificationPerUnitTable.setStatus(_A)
_ProductIdentificationPerUnitEntry_Object=MibTableRow
productIdentificationPerUnitEntry=_ProductIdentificationPerUnitEntry_Object((1,3,6,1,4,1,674,10895,3000,1,2,100,8,1))
productIdentificationPerUnitEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:productIdentificationPerUnitEntry.setStatus(_A)
class _ProductIdentificationPerBoxIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ProductIdentificationPerBoxIndex_Type.__name__=_C
_ProductIdentificationPerBoxIndex_Object=MibTableColumn
productIdentificationPerBoxIndex=_ProductIdentificationPerBoxIndex_Object((1,3,6,1,4,1,674,10895,3000,1,2,100,8,1,1),_ProductIdentificationPerBoxIndex_Type())
productIdentificationPerBoxIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:productIdentificationPerBoxIndex.setStatus(_A)
_ProductIdentificationSerialNumber_Type=DisplayString
_ProductIdentificationSerialNumber_Object=MibTableColumn
productIdentificationSerialNumber=_ProductIdentificationSerialNumber_Object((1,3,6,1,4,1,674,10895,3000,1,2,100,8,1,2),_ProductIdentificationSerialNumber_Type())
productIdentificationSerialNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:productIdentificationSerialNumber.setStatus(_A)
_ProductIdentificationAssetTag_Type=DisplayString
_ProductIdentificationAssetTag_Object=MibTableColumn
productIdentificationAssetTag=_ProductIdentificationAssetTag_Object((1,3,6,1,4,1,674,10895,3000,1,2,100,8,1,3),_ProductIdentificationAssetTag_Type())
productIdentificationAssetTag.setMaxAccess(_B)
if mibBuilder.loadTexts:productIdentificationAssetTag.setStatus(_A)
_ProductIdentificationServiceTag_Type=DisplayString
_ProductIdentificationServiceTag_Object=MibTableColumn
productIdentificationServiceTag=_ProductIdentificationServiceTag_Object((1,3,6,1,4,1,674,10895,3000,1,2,100,8,1,4),_ProductIdentificationServiceTag_Type())
productIdentificationServiceTag.setMaxAccess(_B)
if mibBuilder.loadTexts:productIdentificationServiceTag.setStatus(_A)
_ProductIdentificationChassisServiceTag_Type=DisplayString
_ProductIdentificationChassisServiceTag_Object=MibTableColumn
productIdentificationChassisServiceTag=_ProductIdentificationChassisServiceTag_Object((1,3,6,1,4,1,674,10895,3000,1,2,100,8,1,5),_ProductIdentificationChassisServiceTag_Type())
productIdentificationChassisServiceTag.setMaxAccess(_B)
if mibBuilder.loadTexts:productIdentificationChassisServiceTag.setStatus(_A)
_ProductIdentificationBootromVersion_Type=DisplayString
_ProductIdentificationBootromVersion_Object=MibTableColumn
productIdentificationBootromVersion=_ProductIdentificationBootromVersion_Object((1,3,6,1,4,1,674,10895,3000,1,2,100,8,1,6),_ProductIdentificationBootromVersion_Type())
productIdentificationBootromVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:productIdentificationBootromVersion.setStatus(_A)
class _ProductIdentificationPiecePartID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,24))
_ProductIdentificationPiecePartID_Type.__name__=_E
_ProductIdentificationPiecePartID_Object=MibTableColumn
productIdentificationPiecePartID=_ProductIdentificationPiecePartID_Object((1,3,6,1,4,1,674,10895,3000,1,2,100,8,1,7),_ProductIdentificationPiecePartID_Type())
productIdentificationPiecePartID.setMaxAccess(_B)
if mibBuilder.loadTexts:productIdentificationPiecePartID.setStatus(_A)
class _ProductIdentificationPPIDRevision_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,3))
_ProductIdentificationPPIDRevision_Type.__name__=_E
_ProductIdentificationPPIDRevision_Object=MibTableColumn
productIdentificationPPIDRevision=_ProductIdentificationPPIDRevision_Object((1,3,6,1,4,1,674,10895,3000,1,2,100,8,1,8),_ProductIdentificationPPIDRevision_Type())
productIdentificationPPIDRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:productIdentificationPPIDRevision.setStatus(_A)
class _ProductIdentificationExpressServiceCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,14))
_ProductIdentificationExpressServiceCode_Type.__name__=_E
_ProductIdentificationExpressServiceCode_Object=MibTableColumn
productIdentificationExpressServiceCode=_ProductIdentificationExpressServiceCode_Object((1,3,6,1,4,1,674,10895,3000,1,2,100,8,1,9),_ProductIdentificationExpressServiceCode_Type())
productIdentificationExpressServiceCode.setMaxAccess(_B)
if mibBuilder.loadTexts:productIdentificationExpressServiceCode.setStatus(_A)
class _ProductIdentificationBannerMotdAckMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_ProductIdentificationBannerMotdAckMode_Type.__name__=_C
_ProductIdentificationBannerMotdAckMode_Object=MibScalar
productIdentificationBannerMotdAckMode=_ProductIdentificationBannerMotdAckMode_Object((1,3,6,1,4,1,674,10895,3000,1,2,100,9),_ProductIdentificationBannerMotdAckMode_Type())
productIdentificationBannerMotdAckMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:productIdentificationBannerMotdAckMode.setStatus(_A)
_ProductStatus_ObjectIdentity=ObjectIdentity
productStatus=_ProductStatus_ObjectIdentity((1,3,6,1,4,1,674,10895,3000,1,2,110))
class _ProductStatusGlobalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5)));namedValues=NamedValues(*(('ok',3),(_H,4),(_F,5)))
_ProductStatusGlobalStatus_Type.__name__=_C
_ProductStatusGlobalStatus_Object=MibScalar
productStatusGlobalStatus=_ProductStatusGlobalStatus_Object((1,3,6,1,4,1,674,10895,3000,1,2,110,1),_ProductStatusGlobalStatus_Type())
productStatusGlobalStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:productStatusGlobalStatus.setStatus(_A)
class _ProductStatusLastGlobalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(3,4,5)));namedValues=NamedValues(*(('ok',3),(_H,4),(_F,5)))
_ProductStatusLastGlobalStatus_Type.__name__=_C
_ProductStatusLastGlobalStatus_Object=MibScalar
productStatusLastGlobalStatus=_ProductStatusLastGlobalStatus_Object((1,3,6,1,4,1,674,10895,3000,1,2,110,2),_ProductStatusLastGlobalStatus_Type())
productStatusLastGlobalStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:productStatusLastGlobalStatus.setStatus(_A)
_ProductStatusTimeStamp_Type=TimeTicks
_ProductStatusTimeStamp_Object=MibScalar
productStatusTimeStamp=_ProductStatusTimeStamp_Object((1,3,6,1,4,1,674,10895,3000,1,2,110,3),_ProductStatusTimeStamp_Type())
productStatusTimeStamp.setMaxAccess(_B)
if mibBuilder.loadTexts:productStatusTimeStamp.setStatus(_A)
class _ProductStatusGetTimeOut_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_ProductStatusGetTimeOut_Type.__name__=_C
_ProductStatusGetTimeOut_Object=MibScalar
productStatusGetTimeOut=_ProductStatusGetTimeOut_Object((1,3,6,1,4,1,674,10895,3000,1,2,110,4),_ProductStatusGetTimeOut_Type())
productStatusGetTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:productStatusGetTimeOut.setStatus(_A)
class _ProductStatusRefreshRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_ProductStatusRefreshRate_Type.__name__=_C
_ProductStatusRefreshRate_Object=MibScalar
productStatusRefreshRate=_ProductStatusRefreshRate_Object((1,3,6,1,4,1,674,10895,3000,1,2,110,5),_ProductStatusRefreshRate_Type())
productStatusRefreshRate.setMaxAccess(_B)
if mibBuilder.loadTexts:productStatusRefreshRate.setStatus(_A)
class _ProductStatusGeneratingTrapsFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('true',1),('false',2),('disabled',3)))
_ProductStatusGeneratingTrapsFlag_Type.__name__=_C
_ProductStatusGeneratingTrapsFlag_Object=MibScalar
productStatusGeneratingTrapsFlag=_ProductStatusGeneratingTrapsFlag_Object((1,3,6,1,4,1,674,10895,3000,1,2,110,6),_ProductStatusGeneratingTrapsFlag_Type())
productStatusGeneratingTrapsFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:productStatusGeneratingTrapsFlag.setStatus(_A)
_ProductStatusEnvironment_ObjectIdentity=ObjectIdentity
productStatusEnvironment=_ProductStatusEnvironment_ObjectIdentity((1,3,6,1,4,1,674,10895,3000,1,2,110,7))
_EnvMonFanStatusTable_Object=MibTable
envMonFanStatusTable=_EnvMonFanStatusTable_Object((1,3,6,1,4,1,674,10895,3000,1,2,110,7,1))
if mibBuilder.loadTexts:envMonFanStatusTable.setStatus(_A)
_EnvMonFanStatusEntry_Object=MibTableRow
envMonFanStatusEntry=_EnvMonFanStatusEntry_Object((1,3,6,1,4,1,674,10895,3000,1,2,110,7,1,1))
envMonFanStatusEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:envMonFanStatusEntry.setStatus(_A)
class _EnvMonFanStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EnvMonFanStatusIndex_Type.__name__=_C
_EnvMonFanStatusIndex_Object=MibTableColumn
envMonFanStatusIndex=_EnvMonFanStatusIndex_Object((1,3,6,1,4,1,674,10895,3000,1,2,110,7,1,1,1),_EnvMonFanStatusIndex_Type())
envMonFanStatusIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:envMonFanStatusIndex.setStatus(_A)
class _EnvMonFanStatusDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EnvMonFanStatusDescr_Type.__name__=_E
_EnvMonFanStatusDescr_Object=MibTableColumn
envMonFanStatusDescr=_EnvMonFanStatusDescr_Object((1,3,6,1,4,1,674,10895,3000,1,2,110,7,1,1,2),_EnvMonFanStatusDescr_Type())
envMonFanStatusDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:envMonFanStatusDescr.setStatus(_A)
_EnvMonFanState_Type=EnvMonState
_EnvMonFanState_Object=MibTableColumn
envMonFanState=_EnvMonFanState_Object((1,3,6,1,4,1,674,10895,3000,1,2,110,7,1,1,3),_EnvMonFanState_Type())
envMonFanState.setMaxAccess(_B)
if mibBuilder.loadTexts:envMonFanState.setStatus(_A)
class _EnvMonFanSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_EnvMonFanSpeed_Type.__name__=_C
_EnvMonFanSpeed_Object=MibTableColumn
envMonFanSpeed=_EnvMonFanSpeed_Object((1,3,6,1,4,1,674,10895,3000,1,2,110,7,1,1,4),_EnvMonFanSpeed_Type())
envMonFanSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:envMonFanSpeed.setStatus(_A)
_EnvMonSupplyStatusTable_Object=MibTable
envMonSupplyStatusTable=_EnvMonSupplyStatusTable_Object((1,3,6,1,4,1,674,10895,3000,1,2,110,7,2))
if mibBuilder.loadTexts:envMonSupplyStatusTable.setStatus(_A)
_EnvMonSupplyStatusEntry_Object=MibTableRow
envMonSupplyStatusEntry=_EnvMonSupplyStatusEntry_Object((1,3,6,1,4,1,674,10895,3000,1,2,110,7,2,1))
envMonSupplyStatusEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:envMonSupplyStatusEntry.setStatus(_A)
class _EnvMonSupplyStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_EnvMonSupplyStatusIndex_Type.__name__=_C
_EnvMonSupplyStatusIndex_Object=MibTableColumn
envMonSupplyStatusIndex=_EnvMonSupplyStatusIndex_Object((1,3,6,1,4,1,674,10895,3000,1,2,110,7,2,1,1),_EnvMonSupplyStatusIndex_Type())
envMonSupplyStatusIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:envMonSupplyStatusIndex.setStatus(_A)
class _EnvMonSupplyStatusDescr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EnvMonSupplyStatusDescr_Type.__name__=_E
_EnvMonSupplyStatusDescr_Object=MibTableColumn
envMonSupplyStatusDescr=_EnvMonSupplyStatusDescr_Object((1,3,6,1,4,1,674,10895,3000,1,2,110,7,2,1,2),_EnvMonSupplyStatusDescr_Type())
envMonSupplyStatusDescr.setMaxAccess(_B)
if mibBuilder.loadTexts:envMonSupplyStatusDescr.setStatus(_A)
_EnvMonSupplyState_Type=EnvMonState
_EnvMonSupplyState_Object=MibTableColumn
envMonSupplyState=_EnvMonSupplyState_Object((1,3,6,1,4,1,674,10895,3000,1,2,110,7,2,1,3),_EnvMonSupplyState_Type())
envMonSupplyState.setMaxAccess(_B)
if mibBuilder.loadTexts:envMonSupplyState.setStatus(_A)
class _EnvMonSupplySource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('unknown',1),('ac',2),('dc',3),('externalPowerSupply',4),('internalRedundant',5)))
_EnvMonSupplySource_Type.__name__=_C
_EnvMonSupplySource_Object=MibTableColumn
envMonSupplySource=_EnvMonSupplySource_Object((1,3,6,1,4,1,674,10895,3000,1,2,110,7,2,1,4),_EnvMonSupplySource_Type())
envMonSupplySource.setMaxAccess(_B)
if mibBuilder.loadTexts:envMonSupplySource.setStatus(_A)
class _EnvMonSupplyCurrentPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
_EnvMonSupplyCurrentPower_Type.__name__=_C
_EnvMonSupplyCurrentPower_Object=MibTableColumn
envMonSupplyCurrentPower=_EnvMonSupplyCurrentPower_Object((1,3,6,1,4,1,674,10895,3000,1,2,110,7,2,1,5),_EnvMonSupplyCurrentPower_Type())
envMonSupplyCurrentPower.setMaxAccess(_B)
if mibBuilder.loadTexts:envMonSupplyCurrentPower.setStatus(_A)
class _EnvMonSupplyAveragePower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,2147483647))
_EnvMonSupplyAveragePower_Type.__name__=_C
_EnvMonSupplyAveragePower_Object=MibTableColumn
envMonSupplyAveragePower=_EnvMonSupplyAveragePower_Object((1,3,6,1,4,1,674,10895,3000,1,2,110,7,2,1,6),_EnvMonSupplyAveragePower_Type())
envMonSupplyAveragePower.setMaxAccess(_B)
if mibBuilder.loadTexts:envMonSupplyAveragePower.setStatus(_A)
_EnvMonSupplyAvgStartTime_Type=DateAndTime
_EnvMonSupplyAvgStartTime_Object=MibTableColumn
envMonSupplyAvgStartTime=_EnvMonSupplyAvgStartTime_Object((1,3,6,1,4,1,674,10895,3000,1,2,110,7,2,1,7),_EnvMonSupplyAvgStartTime_Type())
envMonSupplyAvgStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:envMonSupplyAvgStartTime.setStatus(_A)
_DellVendorNotifications_ObjectIdentity=ObjectIdentity
dellVendorNotifications=_DellVendorNotifications_ObjectIdentity((1,3,6,1,4,1,674,10895,3000,2))
_DellVendorTraps_ObjectIdentity=ObjectIdentity
dellVendorTraps=_DellVendorTraps_ObjectIdentity((1,3,6,1,4,1,674,10895,3000,2,1))
_DellVendorTrapsPrefix_ObjectIdentity=ObjectIdentity
dellVendorTrapsPrefix=_DellVendorTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,674,10895,3000,2,1,0))
_DellLanStandard_ObjectIdentity=ObjectIdentity
dellLanStandard=_DellLanStandard_ObjectIdentity((1,3,6,1,4,1,674,10895,5000))
_DellLanCommon_ObjectIdentity=ObjectIdentity
dellLanCommon=_DellLanCommon_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,1))
_DellLanExtension_ObjectIdentity=ObjectIdentity
dellLanExtension=_DellLanExtension_ObjectIdentity((1,3,6,1,4,1,674,10895,5000,2))
productStatusGlobalStatusChange=NotificationType((1,3,6,1,4,1,674,10895,3000,2,1,0,1))
productStatusGlobalStatusChange.setObjects(*((_D,_K),(_D,_L),(_D,_M)))
if mibBuilder.loadTexts:productStatusGlobalStatusChange.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'EnvMonState':EnvMonState,'dell':dell,'dellLan':dellLan,'powerConnectVendorMIB':powerConnectVendorMIB,'dellVendorMIBObjects':dellVendorMIBObjects,'hardware':hardware,'productIdentification':productIdentification,'productIdentificationDisplayName':productIdentificationDisplayName,'productIdentificationDescription':productIdentificationDescription,'productIdentificationVendor':productIdentificationVendor,'productIdentificationVersion':productIdentificationVersion,'productIdentificationBuildNumber':productIdentificationBuildNumber,'productIdentificationURL':productIdentificationURL,'productIdentificationDeviceNetworkName':productIdentificationDeviceNetworkName,'productIdentificationPerUnitTable':productIdentificationPerUnitTable,'productIdentificationPerUnitEntry':productIdentificationPerUnitEntry,_G:productIdentificationPerBoxIndex,'productIdentificationSerialNumber':productIdentificationSerialNumber,'productIdentificationAssetTag':productIdentificationAssetTag,'productIdentificationServiceTag':productIdentificationServiceTag,'productIdentificationChassisServiceTag':productIdentificationChassisServiceTag,'productIdentificationBootromVersion':productIdentificationBootromVersion,'productIdentificationPiecePartID':productIdentificationPiecePartID,'productIdentificationPPIDRevision':productIdentificationPPIDRevision,'productIdentificationExpressServiceCode':productIdentificationExpressServiceCode,'productIdentificationBannerMotdAckMode':productIdentificationBannerMotdAckMode,'productStatus':productStatus,_K:productStatusGlobalStatus,_L:productStatusLastGlobalStatus,_M:productStatusTimeStamp,'productStatusGetTimeOut':productStatusGetTimeOut,'productStatusRefreshRate':productStatusRefreshRate,'productStatusGeneratingTrapsFlag':productStatusGeneratingTrapsFlag,'productStatusEnvironment':productStatusEnvironment,'envMonFanStatusTable':envMonFanStatusTable,'envMonFanStatusEntry':envMonFanStatusEntry,_I:envMonFanStatusIndex,'envMonFanStatusDescr':envMonFanStatusDescr,'envMonFanState':envMonFanState,'envMonFanSpeed':envMonFanSpeed,'envMonSupplyStatusTable':envMonSupplyStatusTable,'envMonSupplyStatusEntry':envMonSupplyStatusEntry,_J:envMonSupplyStatusIndex,'envMonSupplyStatusDescr':envMonSupplyStatusDescr,'envMonSupplyState':envMonSupplyState,'envMonSupplySource':envMonSupplySource,'envMonSupplyCurrentPower':envMonSupplyCurrentPower,'envMonSupplyAveragePower':envMonSupplyAveragePower,'envMonSupplyAvgStartTime':envMonSupplyAvgStartTime,'dellVendorNotifications':dellVendorNotifications,'dellVendorTraps':dellVendorTraps,'dellVendorTrapsPrefix':dellVendorTrapsPrefix,'productStatusGlobalStatusChange':productStatusGlobalStatusChange,'dellLanStandard':dellLanStandard,'dellLanCommon':dellLanCommon,'dellLanExtension':dellLanExtension})