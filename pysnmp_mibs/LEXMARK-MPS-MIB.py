_BZ='deviceAlertGroup'
_BY='statsSupplyHistogramGroup'
_BX='statsSupplyHistoryGroup'
_BW='statsCurrentSuppliesGroup'
_BV='statsScanGroup'
_BU='statsPaperJobSizeGroup'
_BT='statsPaperNupCountGroup'
_BS='statsPaperSheetsCountGroup'
_BR='statsPaperSidesCountGroup'
_BQ='statsPaperGeneralCountGroup'
_BP='statsGeneralCountGroup'
_BO='swInventoryGroup'
_BN='supplyInventoryGroup'
_BM='hwInventoryGroup'
_BL='supplyHistogramCountUnits'
_BK='supplyHistogramCount'
_BJ='supplyHistogramCapacity'
_BI='supplyHistogramCapacityUnit'
_BH='supplyHistogramDescription'
_BG='supplyHistogramColorantValue'
_BF='supplyHistogramSupplyType'
_BE='supplyHistogramInventoryIndex'
_BD='supplyHistoryCoverage'
_BC='supplyHistoryCalibrations'
_BB='supplyHistoryUsage'
_BA='supplyHistoryLastLevel'
_B9='supplyHistoryCapacity'
_B8='supplyHistoryCapacityUnit'
_B7='supplyHistoryPageCount'
_B6='supplyHistoryInstallDate'
_B5='supplyHistoryCartridgeType'
_B4='supplyHistorySerialNumber'
_B3='supplyHistoryDescription'
_B2='supplyHistoryColorantValue'
_B1='supplyHistorySupplyType'
_B0='supplyHistoryInventoryIndex'
_A_='currentSupplyFirstKnownLevel'
_Az='currentSupplyCalibrations'
_Ay='currentSupplyCoverage'
_Ax='currentSupplyUsage'
_Aw='currentSupplyCurrentStatus'
_Av='currentSupplyCurrentLevel'
_Au='currentSupplyDescription'
_At='currentSupplyInstallDate'
_As='currentSupplyCartridgeType'
_Ar='currentSupplyClass'
_Aq='currentSupplyCapacityUnit'
_Ap='currentSupplyPageCountAtInstall'
_Ao='currentSupplyCapacity'
_An='currentSupplyPartNumber'
_Am='currentSupplySerialNumber'
_Al='currentSupplyColorantValue'
_Ak='currentSupplyType'
_Aj='currentSupplyInventoryIndex'
_Ai='scanCountSheets'
_Ah='scanCountSides'
_Ag='scanCountSize'
_Af='scanCountType'
_Ae='paperJobSizeJobCount'
_Ad='paperJobSizeSideCount'
_Ac='paperJobSizeMaximum'
_Ab='paperJobSizeMinimum'
_Aa='paperNupLogicalSides'
_AZ='paperNupSides'
_AY='paperNupNumber'
_AX='paperSheetsSafe'
_AW='paperSheetsPicked'
_AV='paperSheetsPaperType'
_AU='paperSheetsPaperSize'
_AT='paperSidesColorSafe'
_AS='paperSidesMonoSafe'
_AR='paperSidesColorPicked'
_AQ='paperSidesMonoPicked'
_AP='paperSidesPaperType'
_AO='paperSidesPaperSize'
_AN='paperGeneralCountValue'
_AM='paperGeneralCountUnits'
_AL='paperGeneralCountType'
_AK='genCountValue'
_AJ='genCountUnits'
_AI='genCountType'
_AH='swInventoryData'
_AG='swInventoryHWIndex'
_AF='swInventoryDescription'
_AE='swInventoryStatus'
_AD='swInventoryAdminStatus'
_AC='swInventoryRevision'
_AB='swInventoryName'
_AA='swInventoryType'
_A9='swInventoryParentIndex'
_A8='supplyInventoryDescription'
_A7='supplyInventoryColorantValue'
_A6='supplyInventoryType'
_A5='hwInventoryData'
_A4='hwInventoryDescription'
_A3='hwInventorySerialNumber'
_A2='hwInventoryPartNumber'
_A1='hwInventoryStatus'
_A0='hwInventoryAdminStatus'
_z='hwInventoryType'
_y='hwInventoryParentIndex'
_x='deviceMibSupportLevel'
_w='deviceInstallDate'
_v='deviceMibVersion'
_u='deviceSerialNumber'
_t='deviceModel'
_s='deviceHrDeviceIndex'
_r='devicePort'
_q='deviceMibLocalization'
_p='supported'
_o='notSupported'
_n='outputOptionIndex'
_m='swInventoryTable'
_l='supplyInventoryTable'
_k='hwInventoryTable'
_j='supplyHistogramHistoryCountIndex'
_i='supplyHistogramHistoryIndex'
_h='supplyHistogramIndex'
_g='supplyHistoryIndex'
_f='currentSupplyIndex'
_e='scanCountIndex'
_d='paperJobSizeIndex'
_c='paperNupCountIndex'
_b='paperSheetsCountIndex'
_a='paperSidesCountIndex'
_Z='paperGeneralCountIndex'
_Y='genCountIndex'
_X='swInventoryIndex'
_W='supplyInventoryIndex'
_V='hwInventoryIndex'
_U='invalid'
_T='SnmpAdminString'
_S='deviceGroup'
_R='deviceAlertTime'
_Q='deviceAlertData'
_P='deviceAlertDescription'
_O='deviceAlertCode'
_N='deviceAlertSeverity'
_M='deviceAlertConfigTableIndex'
_L='deviceAlertConfigTableNode'
_K='read-write'
_J='deviceAlertIndex'
_I='other'
_H='unknown'
_G='DisplayString'
_F='not-accessible'
_E='deviceIndex'
_D='Integer32'
_C='read-only'
_B='LEXMARK-MPS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lexmark,lexmarkModules=mibBuilder.importSymbols('LEXMARK-ROOT-MIB','lexmark','lexmarkModules')
AdminStatusTC,KeyValueTC,PaperSizeTC,PaperTypeTC,StatusTC,UnitsTC=mibBuilder.importSymbols('LEXMARK-TC-MIB','AdminStatusTC','KeyValueTC','PaperSizeTC','PaperTypeTC','StatusTC','UnitsTC')
PrtAlertCodeTC,PrtAlertSeverityLevelTC,PrtAlertTrainingLevelTC,PrtOutputPageDeliveryOrientationTC=mibBuilder.importSymbols('Printer-MIB','PrtAlertCodeTC','PrtAlertSeverityLevelTC','PrtAlertTrainingLevelTC','PrtOutputPageDeliveryOrientationTC')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_T)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_G,'PhysAddress','TextualConvention')
mpsMibModule=ModuleIdentity((1,3,6,1,4,1,641,4,4))
if mibBuilder.loadTexts:mpsMibModule.setRevisions(('2019-05-02 15:14','2019-02-14 08:50','2017-09-20 08:50','2017-09-15 15:30','2017-08-18 16:07','2017-01-19 16:32','2016-12-14 16:46','2011-05-17 13:42','2011-04-04 12:57','2010-12-22 20:06','2010-12-01 23:00','2009-11-24 20:40'))
class SupplyTypeTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*((_H,1),(_I,2),('inkCartridge',3),('inkBottle',4),('inkPrinthead',5),('toner',6),('photoconductor',7),('transferModule',8),('fuser',9),('wastetonerBox',10),('staples',11),('holepunchBox',12),('tonerMicr',13),('photoconductorMicr',14)))
class CartridgeTypeTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,21,22,23,24,25,26,27,37,38,39,53,54,55)));namedValues=NamedValues(*((_H,1),(_I,2),(_U,3),('shipWith',4),('standard',5),('highYieldStandard',6),('extraHighYieldStandard',7),('otherGenuine',8),('standardGenuine',9),('otherNonGenuine',10),('standardNonGenuine',11),('returnProgram',21),('highYieldReturnProgram',22),('extraHighYieldReturnProgram',23),('standardReturnProgramGenuine',24),('otherReturnProgramGenuine',25),('standardNonReturnProgram',26),('otherNonReturnProgram',27),('refilledStandard',37),('refilledHighYieldStandard',38),('refilledExtraHighYieldStandard',39),('refilledReturnProgram',53),('refilledHighYieldReturnProgram',54),('refilledExtraHighYieldReturnProgram',55)))
class SeverityTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_H,1),(_I,2),('informational',3),('warning',4),('critical',5),('serviceRequired',6)))
class AlertCodeTC(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,100,101,102,103,104,105,106,107,108,109,110,200,201,202,203,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,300,301,302,303,304,305,400,401,402,403,404,500,501,600,601,602,603,604,605,606,607,700,701,702,703,704,705,706,707,708,709,800,801,802,803,804,805,900,901,1000,1001,1002,20000)));namedValues=NamedValues(*((_H,1),(_I,2),('coverOpen',3),('coverClosed',4),('interlockOpen',5),('interlockClosed',6),('doorOpen',7),('doorClosed',8),('calibrating',9),('alignmentFailed',10),('warrantyOverrideRequired',11),('printHeadCarrierPathObstructed',12),('heldJobsMayNotBeRestored',13),('busy',14),('waiting',15),('subunitErrorOther',100),('subunitLifeAlmostOver',101),('subunitLifeOver',102),('subunitJammed',103),('subunitUnderTemperature',104),('subunitOverTemperature',105),('subunitInsufficientMemory',106),('subunitMemoryFull',107),('subunitNVFailure',108),('subunitDisabled',109),('subunitCommunicationError',110),('supplyErrorOther',200),('supplyOk',201),('supplyEarlyWarning',202),('supplyNearFull',203),('supplyFull',205),('supplyNearLow',206),('supplyLow',207),('supplyNearEmpty',208),('supplyEmpty',209),('supplyLifeAlmostOver',210),('supplyLifeOver',211),('supplyNearReplace',212),('supplyReplace',213),('supplyMissing',214),('supplyInvalid',215),('supplyDefective',216),('supplyImproperInstall',217),('supplyUnsupported',218),('supplyUncalibrated',219),('inputMediaErrorOther',300),('inputMediaTrayMissing',301),('inputMediaSupplyLow',302),('inputMediaSupplyEmpty',303),('inputMediaChangeRequest',304),('inputMediaLoadRequest',305),('outputMediaErrorOther',400),('outputMediaTrayMissing',401),('outputMediaNearFull',402),('outputMediaFull',403),('outputMediaEmptyRequest',404),('mediaPathErrorOther',500),('mediaPathPaperJam',501),('scannerErrorOther',600),('scannerLampWarming',601),('scannerLampLifeWarning',602),('scannerLampError',603),('scannerADFJam',604),('scannerStalled',605),('scannerLocked',606),('scannerDisabled',607),('faxErrorOther',700),('faxStorageNearFull',701),('faxStorageFull',702),('faxStorageSendNearFull',703),('faxStorageSendFull',704),('faxStorageReceiveNearFull',705),('faxStorageReceiveFull',706),('faxPhoneLineDisconnected',707),('faxDisabled',708),('faxConfigurationError',709),('interpreterErrorOther',800),('interpreterInsufficientMemory',801),('interpreterOutOfMemory',802),('interpreterComplexPage',803),('interpreterJobHardwareMismatch',804),('interpreterPrintDataExceedsMediaSize',805),('emailErrorOther',900),('emailConfigurationError',901),('storageErrorOther',1000),('storageUnformatted',1001),('storageFull',1002),('neverError',20000)))
_Mps_ObjectIdentity=ObjectIdentity
mps=_Mps_ObjectIdentity((1,3,6,1,4,1,641,6))
_MpsMIBAdminInfo_ObjectIdentity=ObjectIdentity
mpsMIBAdminInfo=_MpsMIBAdminInfo_ObjectIdentity((1,3,6,1,4,1,641,6,1))
_MpsMIBCompliances_ObjectIdentity=ObjectIdentity
mpsMIBCompliances=_MpsMIBCompliances_ObjectIdentity((1,3,6,1,4,1,641,6,1,1))
_MpsMIBGroups_ObjectIdentity=ObjectIdentity
mpsMIBGroups=_MpsMIBGroups_ObjectIdentity((1,3,6,1,4,1,641,6,1,2))
_Device_ObjectIdentity=ObjectIdentity
device=_Device_ObjectIdentity((1,3,6,1,4,1,641,6,2))
_DeviceMibLocalization_Type=Integer32
_DeviceMibLocalization_Object=MibScalar
deviceMibLocalization=_DeviceMibLocalization_Object((1,3,6,1,4,1,641,6,2,1),_DeviceMibLocalization_Type())
deviceMibLocalization.setMaxAccess(_K)
if mibBuilder.loadTexts:deviceMibLocalization.setStatus(_A)
_DeviceTable_Object=MibTable
deviceTable=_DeviceTable_Object((1,3,6,1,4,1,641,6,2,3))
if mibBuilder.loadTexts:deviceTable.setStatus(_A)
_DeviceEntry_Object=MibTableRow
deviceEntry=_DeviceEntry_Object((1,3,6,1,4,1,641,6,2,3,1))
deviceEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:deviceEntry.setStatus(_A)
class _DeviceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DeviceIndex_Type.__name__=_D
_DeviceIndex_Object=MibTableColumn
deviceIndex=_DeviceIndex_Object((1,3,6,1,4,1,641,6,2,3,1,1),_DeviceIndex_Type())
deviceIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:deviceIndex.setStatus(_A)
_DevicePort_Type=Integer32
_DevicePort_Object=MibTableColumn
devicePort=_DevicePort_Object((1,3,6,1,4,1,641,6,2,3,1,2),_DevicePort_Type())
devicePort.setMaxAccess(_C)
if mibBuilder.loadTexts:devicePort.setStatus(_A)
_DeviceHrDeviceIndex_Type=Integer32
_DeviceHrDeviceIndex_Object=MibTableColumn
deviceHrDeviceIndex=_DeviceHrDeviceIndex_Object((1,3,6,1,4,1,641,6,2,3,1,3),_DeviceHrDeviceIndex_Type())
deviceHrDeviceIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceHrDeviceIndex.setStatus(_A)
class _DeviceModel_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_DeviceModel_Type.__name__=_T
_DeviceModel_Object=MibTableColumn
deviceModel=_DeviceModel_Object((1,3,6,1,4,1,641,6,2,3,1,4),_DeviceModel_Type())
deviceModel.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceModel.setStatus(_A)
class _DeviceSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_DeviceSerialNumber_Type.__name__=_G
_DeviceSerialNumber_Object=MibTableColumn
deviceSerialNumber=_DeviceSerialNumber_Object((1,3,6,1,4,1,641,6,2,3,1,5),_DeviceSerialNumber_Type())
deviceSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceSerialNumber.setStatus(_A)
class _DeviceMibVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DeviceMibVersion_Type.__name__=_G
_DeviceMibVersion_Object=MibTableColumn
deviceMibVersion=_DeviceMibVersion_Object((1,3,6,1,4,1,641,6,2,3,1,6),_DeviceMibVersion_Type())
deviceMibVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceMibVersion.setStatus(_A)
_DeviceInstallDate_Type=DateAndTime
_DeviceInstallDate_Object=MibTableColumn
deviceInstallDate=_DeviceInstallDate_Object((1,3,6,1,4,1,641,6,2,3,1,7),_DeviceInstallDate_Type())
deviceInstallDate.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceInstallDate.setStatus(_A)
class _DeviceMibSupportLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,16,32,48)));namedValues=NamedValues(*(('none',0),('minimum',1),('value',16),('feature',32),('enterprise',48)))
_DeviceMibSupportLevel_Type.__name__=_D
_DeviceMibSupportLevel_Object=MibTableColumn
deviceMibSupportLevel=_DeviceMibSupportLevel_Object((1,3,6,1,4,1,641,6,2,3,1,8),_DeviceMibSupportLevel_Type())
deviceMibSupportLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceMibSupportLevel.setStatus(_A)
class _DeviceMachineType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DeviceMachineType_Type.__name__=_G
_DeviceMachineType_Object=MibTableColumn
deviceMachineType=_DeviceMachineType_Object((1,3,6,1,4,1,641,6,2,3,1,9),_DeviceMachineType_Type())
deviceMachineType.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceMachineType.setStatus(_A)
class _DeviceTLI_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_DeviceTLI_Type.__name__=_G
_DeviceTLI_Object=MibTableColumn
deviceTLI=_DeviceTLI_Object((1,3,6,1,4,1,641,6,2,3,1,10),_DeviceTLI_Type())
deviceTLI.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceTLI.setStatus(_A)
_Inventory_ObjectIdentity=ObjectIdentity
inventory=_Inventory_ObjectIdentity((1,3,6,1,4,1,641,6,3))
_HwInventoryTable_Object=MibTable
hwInventoryTable=_HwInventoryTable_Object((1,3,6,1,4,1,641,6,3,1))
if mibBuilder.loadTexts:hwInventoryTable.setStatus(_A)
_HwInventoryEntry_Object=MibTableRow
hwInventoryEntry=_HwInventoryEntry_Object((1,3,6,1,4,1,641,6,3,1,1))
hwInventoryEntry.setIndexNames((0,_B,_E),(0,_B,_V))
if mibBuilder.loadTexts:hwInventoryEntry.setStatus(_A)
class _HwInventoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HwInventoryIndex_Type.__name__=_D
_HwInventoryIndex_Object=MibTableColumn
hwInventoryIndex=_HwInventoryIndex_Object((1,3,6,1,4,1,641,6,3,1,1,1),_HwInventoryIndex_Type())
hwInventoryIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:hwInventoryIndex.setStatus(_A)
class _HwInventoryParentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HwInventoryParentIndex_Type.__name__=_D
_HwInventoryParentIndex_Object=MibTableColumn
hwInventoryParentIndex=_HwInventoryParentIndex_Object((1,3,6,1,4,1,641,6,3,1,1,2),_HwInventoryParentIndex_Type())
hwInventoryParentIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInventoryParentIndex.setStatus(_A)
class _HwInventoryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,257,258,261,262,263,264,265,266,267,268,269,270,271,272)));namedValues=NamedValues(*((_H,1),(_I,2),('printEngine',3),('electronicCard',4),('duplexer',5),('inputTray',6),('outputTray',7),('finishingDevice',8),('scanner',9),('faxCard',10),('memory',11),('nonVolitileMemory',12),('keyboard',13),('panel',14),('cardSwipe',15),('transferUnit',16),('connectivityModule',17),('optionUnknown',257),('optionOther',258),('optionDuplexer',261),('optionInputTray',262),('optionOutputTray',263),('optionFinishingDevice',264),('optionScanner',265),('optionFaxCard',266),('optionMemory',267),('optionNonVolitileMemory',268),('optionKeyboard',269),('optionPanel',270),('optionCardSwipe',271),('optionTransferUnit',272)))
_HwInventoryType_Type.__name__=_D
_HwInventoryType_Object=MibTableColumn
hwInventoryType=_HwInventoryType_Object((1,3,6,1,4,1,641,6,3,1,1,3),_HwInventoryType_Type())
hwInventoryType.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInventoryType.setStatus(_A)
_HwInventoryAdminStatus_Type=AdminStatusTC
_HwInventoryAdminStatus_Object=MibTableColumn
hwInventoryAdminStatus=_HwInventoryAdminStatus_Object((1,3,6,1,4,1,641,6,3,1,1,4),_HwInventoryAdminStatus_Type())
hwInventoryAdminStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:hwInventoryAdminStatus.setStatus(_A)
_HwInventoryStatus_Type=StatusTC
_HwInventoryStatus_Object=MibTableColumn
hwInventoryStatus=_HwInventoryStatus_Object((1,3,6,1,4,1,641,6,3,1,1,5),_HwInventoryStatus_Type())
hwInventoryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInventoryStatus.setStatus(_A)
_HwInventoryPartNumber_Type=DisplayString
_HwInventoryPartNumber_Object=MibTableColumn
hwInventoryPartNumber=_HwInventoryPartNumber_Object((1,3,6,1,4,1,641,6,3,1,1,6),_HwInventoryPartNumber_Type())
hwInventoryPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInventoryPartNumber.setStatus(_A)
_HwInventorySerialNumber_Type=DisplayString
_HwInventorySerialNumber_Object=MibTableColumn
hwInventorySerialNumber=_HwInventorySerialNumber_Object((1,3,6,1,4,1,641,6,3,1,1,7),_HwInventorySerialNumber_Type())
hwInventorySerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInventorySerialNumber.setStatus(_A)
_HwInventoryDescription_Type=SnmpAdminString
_HwInventoryDescription_Object=MibTableColumn
hwInventoryDescription=_HwInventoryDescription_Object((1,3,6,1,4,1,641,6,3,1,1,8),_HwInventoryDescription_Type())
hwInventoryDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInventoryDescription.setStatus(_A)
_HwInventoryData_Type=KeyValueTC
_HwInventoryData_Object=MibTableColumn
hwInventoryData=_HwInventoryData_Object((1,3,6,1,4,1,641,6,3,1,1,9),_HwInventoryData_Type())
hwInventoryData.setMaxAccess(_C)
if mibBuilder.loadTexts:hwInventoryData.setStatus(_A)
_SupplyInventoryTable_Object=MibTable
supplyInventoryTable=_SupplyInventoryTable_Object((1,3,6,1,4,1,641,6,3,2))
if mibBuilder.loadTexts:supplyInventoryTable.setStatus(_A)
_SupplyInventoryEntry_Object=MibTableRow
supplyInventoryEntry=_SupplyInventoryEntry_Object((1,3,6,1,4,1,641,6,3,2,1))
supplyInventoryEntry.setIndexNames((0,_B,_E),(0,_B,_W))
if mibBuilder.loadTexts:supplyInventoryEntry.setStatus(_A)
class _SupplyInventoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SupplyInventoryIndex_Type.__name__=_D
_SupplyInventoryIndex_Object=MibTableColumn
supplyInventoryIndex=_SupplyInventoryIndex_Object((1,3,6,1,4,1,641,6,3,2,1,1),_SupplyInventoryIndex_Type())
supplyInventoryIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:supplyInventoryIndex.setStatus(_A)
_SupplyInventoryType_Type=SupplyTypeTC
_SupplyInventoryType_Object=MibTableColumn
supplyInventoryType=_SupplyInventoryType_Object((1,3,6,1,4,1,641,6,3,2,1,2),_SupplyInventoryType_Type())
supplyInventoryType.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyInventoryType.setStatus(_A)
_SupplyInventoryColorantValue_Type=DisplayString
_SupplyInventoryColorantValue_Object=MibTableColumn
supplyInventoryColorantValue=_SupplyInventoryColorantValue_Object((1,3,6,1,4,1,641,6,3,2,1,3),_SupplyInventoryColorantValue_Type())
supplyInventoryColorantValue.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyInventoryColorantValue.setStatus(_A)
_SupplyInventoryDescription_Type=SnmpAdminString
_SupplyInventoryDescription_Object=MibTableColumn
supplyInventoryDescription=_SupplyInventoryDescription_Object((1,3,6,1,4,1,641,6,3,2,1,4),_SupplyInventoryDescription_Type())
supplyInventoryDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyInventoryDescription.setStatus(_A)
_SupplyDynamicIndex_Type=DisplayString
_SupplyDynamicIndex_Object=MibTableColumn
supplyDynamicIndex=_SupplyDynamicIndex_Object((1,3,6,1,4,1,641,6,3,2,1,5),_SupplyDynamicIndex_Type())
supplyDynamicIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyDynamicIndex.setStatus(_A)
_SwInventoryTable_Object=MibTable
swInventoryTable=_SwInventoryTable_Object((1,3,6,1,4,1,641,6,3,3))
if mibBuilder.loadTexts:swInventoryTable.setStatus(_A)
_SwInventoryEntry_Object=MibTableRow
swInventoryEntry=_SwInventoryEntry_Object((1,3,6,1,4,1,641,6,3,3,1))
swInventoryEntry.setIndexNames((0,_B,_E),(0,_B,_X))
if mibBuilder.loadTexts:swInventoryEntry.setStatus(_A)
class _SwInventoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SwInventoryIndex_Type.__name__=_D
_SwInventoryIndex_Object=MibTableColumn
swInventoryIndex=_SwInventoryIndex_Object((1,3,6,1,4,1,641,6,3,3,1,1),_SwInventoryIndex_Type())
swInventoryIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:swInventoryIndex.setStatus(_A)
class _SwInventoryParentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwInventoryParentIndex_Type.__name__=_D
_SwInventoryParentIndex_Object=MibTableColumn
swInventoryParentIndex=_SwInventoryParentIndex_Object((1,3,6,1,4,1,641,6,3,3,1,2),_SwInventoryParentIndex_Type())
swInventoryParentIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swInventoryParentIndex.setStatus(_A)
class _SwInventoryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_H,1),(_I,2),('operatingSystem',3),('hardware',4),('application',5)))
_SwInventoryType_Type.__name__=_D
_SwInventoryType_Object=MibTableColumn
swInventoryType=_SwInventoryType_Object((1,3,6,1,4,1,641,6,3,3,1,3),_SwInventoryType_Type())
swInventoryType.setMaxAccess(_C)
if mibBuilder.loadTexts:swInventoryType.setStatus(_A)
_SwInventoryAdminStatus_Type=AdminStatusTC
_SwInventoryAdminStatus_Object=MibTableColumn
swInventoryAdminStatus=_SwInventoryAdminStatus_Object((1,3,6,1,4,1,641,6,3,3,1,4),_SwInventoryAdminStatus_Type())
swInventoryAdminStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:swInventoryAdminStatus.setStatus(_A)
_SwInventoryStatus_Type=StatusTC
_SwInventoryStatus_Object=MibTableColumn
swInventoryStatus=_SwInventoryStatus_Object((1,3,6,1,4,1,641,6,3,3,1,5),_SwInventoryStatus_Type())
swInventoryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swInventoryStatus.setStatus(_A)
_SwInventoryName_Type=DisplayString
_SwInventoryName_Object=MibTableColumn
swInventoryName=_SwInventoryName_Object((1,3,6,1,4,1,641,6,3,3,1,6),_SwInventoryName_Type())
swInventoryName.setMaxAccess(_C)
if mibBuilder.loadTexts:swInventoryName.setStatus(_A)
_SwInventoryRevision_Type=DisplayString
_SwInventoryRevision_Object=MibTableColumn
swInventoryRevision=_SwInventoryRevision_Object((1,3,6,1,4,1,641,6,3,3,1,7),_SwInventoryRevision_Type())
swInventoryRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:swInventoryRevision.setStatus(_A)
_SwInventoryDescription_Type=SnmpAdminString
_SwInventoryDescription_Object=MibTableColumn
swInventoryDescription=_SwInventoryDescription_Object((1,3,6,1,4,1,641,6,3,3,1,8),_SwInventoryDescription_Type())
swInventoryDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:swInventoryDescription.setStatus(_A)
class _SwInventoryHWIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SwInventoryHWIndex_Type.__name__=_D
_SwInventoryHWIndex_Object=MibTableColumn
swInventoryHWIndex=_SwInventoryHWIndex_Object((1,3,6,1,4,1,641,6,3,3,1,9),_SwInventoryHWIndex_Type())
swInventoryHWIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:swInventoryHWIndex.setStatus(_A)
_SwInventoryData_Type=KeyValueTC
_SwInventoryData_Object=MibTableColumn
swInventoryData=_SwInventoryData_Object((1,3,6,1,4,1,641,6,3,3,1,10),_SwInventoryData_Type())
swInventoryData.setMaxAccess(_C)
if mibBuilder.loadTexts:swInventoryData.setStatus(_A)
_Stats_ObjectIdentity=ObjectIdentity
stats=_Stats_ObjectIdentity((1,3,6,1,4,1,641,6,4))
_GeneralStats_ObjectIdentity=ObjectIdentity
generalStats=_GeneralStats_ObjectIdentity((1,3,6,1,4,1,641,6,4,1))
_GenCountTable_Object=MibTable
genCountTable=_GenCountTable_Object((1,3,6,1,4,1,641,6,4,1,1))
if mibBuilder.loadTexts:genCountTable.setStatus(_A)
_GenCountEntry_Object=MibTableRow
genCountEntry=_GenCountEntry_Object((1,3,6,1,4,1,641,6,4,1,1,1))
genCountEntry.setIndexNames((0,_B,_E),(0,_B,_Y))
if mibBuilder.loadTexts:genCountEntry.setStatus(_A)
class _GenCountIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_GenCountIndex_Type.__name__=_D
_GenCountIndex_Object=MibTableColumn
genCountIndex=_GenCountIndex_Object((1,3,6,1,4,1,641,6,4,1,1,1,1),_GenCountIndex_Type())
genCountIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:genCountIndex.setStatus(_A)
class _GenCountType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,32,33,34,35,36,37,38,64,65,66,67,68,69,70,71,96,97,98,99,100,101,102,128)));namedValues=NamedValues(*(('porCount',1),('sleepCount',2),('hibernateCount',3),('printCalibrateCount',4),('powerOnTime',32),('powerActiveTime',33),('powerIdleTime',34),('powerSleepTime',35),('powerHibernateTime',36),('powerOffTime',37),('warmupTotalTime',38),('lifetimeBlackCoverage',64),('lifetimeCyanCoverage',65),('lifetimeYellowCoverage',66),('lifetimeMagentaCoverage',67),('rawLifetimeBlackCoverage',68),('rawLifetimeCyanCoverage',69),('rawLifetimeYellowCoverage',70),('rawLifetimeMagentaCoverage',71),('faxesSent',96),('paperJams',97),('scannerJams',98),('loadPaperPrompts',99),('changePaperPrompts',100),('coverOpens',101),('printerIRTime',102),('usbInsertions',128)))
_GenCountType_Type.__name__=_D
_GenCountType_Object=MibTableColumn
genCountType=_GenCountType_Object((1,3,6,1,4,1,641,6,4,1,1,1,2),_GenCountType_Type())
genCountType.setMaxAccess(_C)
if mibBuilder.loadTexts:genCountType.setStatus(_A)
_GenCountUnits_Type=UnitsTC
_GenCountUnits_Object=MibTableColumn
genCountUnits=_GenCountUnits_Object((1,3,6,1,4,1,641,6,4,1,1,1,3),_GenCountUnits_Type())
genCountUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:genCountUnits.setStatus(_A)
_GenCountValue_Type=Counter32
_GenCountValue_Object=MibTableColumn
genCountValue=_GenCountValue_Object((1,3,6,1,4,1,641,6,4,1,1,1,4),_GenCountValue_Type())
genCountValue.setMaxAccess(_C)
if mibBuilder.loadTexts:genCountValue.setStatus(_A)
_PaperStats_ObjectIdentity=ObjectIdentity
paperStats=_PaperStats_ObjectIdentity((1,3,6,1,4,1,641,6,4,2))
_PaperGeneralCountTable_Object=MibTable
paperGeneralCountTable=_PaperGeneralCountTable_Object((1,3,6,1,4,1,641,6,4,2,1))
if mibBuilder.loadTexts:paperGeneralCountTable.setStatus(_A)
_PaperGeneralCountEntry_Object=MibTableRow
paperGeneralCountEntry=_PaperGeneralCountEntry_Object((1,3,6,1,4,1,641,6,4,2,1,1))
paperGeneralCountEntry.setIndexNames((0,_B,_E),(0,_B,_Z))
if mibBuilder.loadTexts:paperGeneralCountEntry.setStatus(_A)
class _PaperGeneralCountIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PaperGeneralCountIndex_Type.__name__=_D
_PaperGeneralCountIndex_Object=MibTableColumn
paperGeneralCountIndex=_PaperGeneralCountIndex_Object((1,3,6,1,4,1,641,6,4,2,1,1,1),_PaperGeneralCountIndex_Type())
paperGeneralCountIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:paperGeneralCountIndex.setStatus(_A)
class _PaperGeneralCountType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,16,17,18,32,33,34,48,49,50,64,65,66,67,80,81,90,91,92,100,101,102,103,104,105,106,107,108,109,120,121,122,130,131,132)));namedValues=NamedValues(*(('totalPicked',1),('totalSafe',2),('totalMonoSafe',3),('totalColorSafe',4),('printNHold',5),('usbDirect',6),('continuousPrint',7),('printTotal',16),('printMono',17),('printColor',18),('copyTotal',32),('copyMono',33),('copyColor',34),('faxTotal',48),('faxMono',49),('faxColor',50),('blankTotal',64),('blankPrint',65),('blankCopy',66),('blankFax',67),('printerPageCount',80),('modularPageCount',81),('highlightColor',90),('businessColor',91),('graphicsColor',92),('tonerDarkness1',100),('tonerDarkness2',101),('tonerDarkness3',102),('tonerDarkness4',103),('tonerDarkness5',104),('tonerDarkness6',105),('tonerDarkness7',106),('tonerDarkness8',107),('tonerDarkness9',108),('tonerDarkness10',109),('stapleEmpty1',120),('stapleEmpty2',121),('stapleEmpty3',122),('clickCountPrintMono',130),('clickCountPrintColor',131),('clickCountScan',132)))
_PaperGeneralCountType_Type.__name__=_D
_PaperGeneralCountType_Object=MibTableColumn
paperGeneralCountType=_PaperGeneralCountType_Object((1,3,6,1,4,1,641,6,4,2,1,1,2),_PaperGeneralCountType_Type())
paperGeneralCountType.setMaxAccess(_C)
if mibBuilder.loadTexts:paperGeneralCountType.setStatus(_A)
_PaperGeneralCountUnits_Type=UnitsTC
_PaperGeneralCountUnits_Object=MibTableColumn
paperGeneralCountUnits=_PaperGeneralCountUnits_Object((1,3,6,1,4,1,641,6,4,2,1,1,3),_PaperGeneralCountUnits_Type())
paperGeneralCountUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:paperGeneralCountUnits.setStatus(_A)
_PaperGeneralCountValue_Type=Counter32
_PaperGeneralCountValue_Object=MibTableColumn
paperGeneralCountValue=_PaperGeneralCountValue_Object((1,3,6,1,4,1,641,6,4,2,1,1,4),_PaperGeneralCountValue_Type())
paperGeneralCountValue.setMaxAccess(_C)
if mibBuilder.loadTexts:paperGeneralCountValue.setStatus(_A)
_PaperSidesCountTable_Object=MibTable
paperSidesCountTable=_PaperSidesCountTable_Object((1,3,6,1,4,1,641,6,4,2,2))
if mibBuilder.loadTexts:paperSidesCountTable.setStatus(_A)
_PaperSidesCountEntry_Object=MibTableRow
paperSidesCountEntry=_PaperSidesCountEntry_Object((1,3,6,1,4,1,641,6,4,2,2,1))
paperSidesCountEntry.setIndexNames((0,_B,_E),(0,_B,_a))
if mibBuilder.loadTexts:paperSidesCountEntry.setStatus(_A)
class _PaperSidesCountIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PaperSidesCountIndex_Type.__name__=_D
_PaperSidesCountIndex_Object=MibTableColumn
paperSidesCountIndex=_PaperSidesCountIndex_Object((1,3,6,1,4,1,641,6,4,2,2,1,1),_PaperSidesCountIndex_Type())
paperSidesCountIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:paperSidesCountIndex.setStatus(_A)
_PaperSidesPaperSize_Type=PaperSizeTC
_PaperSidesPaperSize_Object=MibTableColumn
paperSidesPaperSize=_PaperSidesPaperSize_Object((1,3,6,1,4,1,641,6,4,2,2,1,2),_PaperSidesPaperSize_Type())
paperSidesPaperSize.setMaxAccess(_C)
if mibBuilder.loadTexts:paperSidesPaperSize.setStatus(_A)
_PaperSidesPaperType_Type=PaperTypeTC
_PaperSidesPaperType_Object=MibTableColumn
paperSidesPaperType=_PaperSidesPaperType_Object((1,3,6,1,4,1,641,6,4,2,2,1,3),_PaperSidesPaperType_Type())
paperSidesPaperType.setMaxAccess(_C)
if mibBuilder.loadTexts:paperSidesPaperType.setStatus(_A)
_PaperSidesMonoPicked_Type=Counter32
_PaperSidesMonoPicked_Object=MibTableColumn
paperSidesMonoPicked=_PaperSidesMonoPicked_Object((1,3,6,1,4,1,641,6,4,2,2,1,4),_PaperSidesMonoPicked_Type())
paperSidesMonoPicked.setMaxAccess(_C)
if mibBuilder.loadTexts:paperSidesMonoPicked.setStatus(_A)
_PaperSidesColorPicked_Type=Counter32
_PaperSidesColorPicked_Object=MibTableColumn
paperSidesColorPicked=_PaperSidesColorPicked_Object((1,3,6,1,4,1,641,6,4,2,2,1,5),_PaperSidesColorPicked_Type())
paperSidesColorPicked.setMaxAccess(_C)
if mibBuilder.loadTexts:paperSidesColorPicked.setStatus(_A)
_PaperSidesMonoSafe_Type=Counter32
_PaperSidesMonoSafe_Object=MibTableColumn
paperSidesMonoSafe=_PaperSidesMonoSafe_Object((1,3,6,1,4,1,641,6,4,2,2,1,6),_PaperSidesMonoSafe_Type())
paperSidesMonoSafe.setMaxAccess(_C)
if mibBuilder.loadTexts:paperSidesMonoSafe.setStatus(_A)
_PaperSidesColorSafe_Type=Counter32
_PaperSidesColorSafe_Object=MibTableColumn
paperSidesColorSafe=_PaperSidesColorSafe_Object((1,3,6,1,4,1,641,6,4,2,2,1,7),_PaperSidesColorSafe_Type())
paperSidesColorSafe.setMaxAccess(_C)
if mibBuilder.loadTexts:paperSidesColorSafe.setStatus(_A)
_PaperSheetsCountTable_Object=MibTable
paperSheetsCountTable=_PaperSheetsCountTable_Object((1,3,6,1,4,1,641,6,4,2,3))
if mibBuilder.loadTexts:paperSheetsCountTable.setStatus(_A)
_PaperSheetsCountEntry_Object=MibTableRow
paperSheetsCountEntry=_PaperSheetsCountEntry_Object((1,3,6,1,4,1,641,6,4,2,3,1))
paperSheetsCountEntry.setIndexNames((0,_B,_E),(0,_B,_b))
if mibBuilder.loadTexts:paperSheetsCountEntry.setStatus(_A)
class _PaperSheetsCountIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PaperSheetsCountIndex_Type.__name__=_D
_PaperSheetsCountIndex_Object=MibTableColumn
paperSheetsCountIndex=_PaperSheetsCountIndex_Object((1,3,6,1,4,1,641,6,4,2,3,1,1),_PaperSheetsCountIndex_Type())
paperSheetsCountIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:paperSheetsCountIndex.setStatus(_A)
_PaperSheetsPaperSize_Type=PaperSizeTC
_PaperSheetsPaperSize_Object=MibTableColumn
paperSheetsPaperSize=_PaperSheetsPaperSize_Object((1,3,6,1,4,1,641,6,4,2,3,1,2),_PaperSheetsPaperSize_Type())
paperSheetsPaperSize.setMaxAccess(_C)
if mibBuilder.loadTexts:paperSheetsPaperSize.setStatus(_A)
_PaperSheetsPaperType_Type=PaperTypeTC
_PaperSheetsPaperType_Object=MibTableColumn
paperSheetsPaperType=_PaperSheetsPaperType_Object((1,3,6,1,4,1,641,6,4,2,3,1,3),_PaperSheetsPaperType_Type())
paperSheetsPaperType.setMaxAccess(_C)
if mibBuilder.loadTexts:paperSheetsPaperType.setStatus(_A)
_PaperSheetsPicked_Type=Counter32
_PaperSheetsPicked_Object=MibTableColumn
paperSheetsPicked=_PaperSheetsPicked_Object((1,3,6,1,4,1,641,6,4,2,3,1,4),_PaperSheetsPicked_Type())
paperSheetsPicked.setMaxAccess(_C)
if mibBuilder.loadTexts:paperSheetsPicked.setStatus(_A)
_PaperSheetsSafe_Type=Counter32
_PaperSheetsSafe_Object=MibTableColumn
paperSheetsSafe=_PaperSheetsSafe_Object((1,3,6,1,4,1,641,6,4,2,3,1,5),_PaperSheetsSafe_Type())
paperSheetsSafe.setMaxAccess(_C)
if mibBuilder.loadTexts:paperSheetsSafe.setStatus(_A)
_PaperNupCountTable_Object=MibTable
paperNupCountTable=_PaperNupCountTable_Object((1,3,6,1,4,1,641,6,4,2,4))
if mibBuilder.loadTexts:paperNupCountTable.setStatus(_A)
_PaperNupCountEntry_Object=MibTableRow
paperNupCountEntry=_PaperNupCountEntry_Object((1,3,6,1,4,1,641,6,4,2,4,1))
paperNupCountEntry.setIndexNames((0,_B,_E),(0,_B,_c))
if mibBuilder.loadTexts:paperNupCountEntry.setStatus(_A)
class _PaperNupCountIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PaperNupCountIndex_Type.__name__=_D
_PaperNupCountIndex_Object=MibTableColumn
paperNupCountIndex=_PaperNupCountIndex_Object((1,3,6,1,4,1,641,6,4,2,4,1,1),_PaperNupCountIndex_Type())
paperNupCountIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:paperNupCountIndex.setStatus(_A)
class _PaperNupNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,6,9,12,16)));namedValues=NamedValues(*(('off',1),('twoUp',2),('threeUp',3),('fourUp',4),('sixUp',6),('nineUp',9),('twelveUp',12),('sixteenUp',16)))
_PaperNupNumber_Type.__name__=_D
_PaperNupNumber_Object=MibTableColumn
paperNupNumber=_PaperNupNumber_Object((1,3,6,1,4,1,641,6,4,2,4,1,2),_PaperNupNumber_Type())
paperNupNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:paperNupNumber.setStatus(_A)
_PaperNupSides_Type=Counter32
_PaperNupSides_Object=MibTableColumn
paperNupSides=_PaperNupSides_Object((1,3,6,1,4,1,641,6,4,2,4,1,3),_PaperNupSides_Type())
paperNupSides.setMaxAccess(_C)
if mibBuilder.loadTexts:paperNupSides.setStatus(_A)
_PaperNupLogicalSides_Type=Counter32
_PaperNupLogicalSides_Object=MibTableColumn
paperNupLogicalSides=_PaperNupLogicalSides_Object((1,3,6,1,4,1,641,6,4,2,4,1,4),_PaperNupLogicalSides_Type())
paperNupLogicalSides.setMaxAccess(_C)
if mibBuilder.loadTexts:paperNupLogicalSides.setStatus(_A)
_PaperJobSizeTable_Object=MibTable
paperJobSizeTable=_PaperJobSizeTable_Object((1,3,6,1,4,1,641,6,4,2,5))
if mibBuilder.loadTexts:paperJobSizeTable.setStatus(_A)
_PaperJobSizeEntry_Object=MibTableRow
paperJobSizeEntry=_PaperJobSizeEntry_Object((1,3,6,1,4,1,641,6,4,2,5,1))
paperJobSizeEntry.setIndexNames((0,_B,_E),(0,_B,_d))
if mibBuilder.loadTexts:paperJobSizeEntry.setStatus(_A)
class _PaperJobSizeIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PaperJobSizeIndex_Type.__name__=_D
_PaperJobSizeIndex_Object=MibTableColumn
paperJobSizeIndex=_PaperJobSizeIndex_Object((1,3,6,1,4,1,641,6,4,2,5,1,1),_PaperJobSizeIndex_Type())
paperJobSizeIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:paperJobSizeIndex.setStatus(_A)
class _PaperJobSizeMinimum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_PaperJobSizeMinimum_Type.__name__=_D
_PaperJobSizeMinimum_Object=MibTableColumn
paperJobSizeMinimum=_PaperJobSizeMinimum_Object((1,3,6,1,4,1,641,6,4,2,5,1,2),_PaperJobSizeMinimum_Type())
paperJobSizeMinimum.setMaxAccess(_C)
if mibBuilder.loadTexts:paperJobSizeMinimum.setStatus(_A)
class _PaperJobSizeMaximum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_PaperJobSizeMaximum_Type.__name__=_D
_PaperJobSizeMaximum_Object=MibTableColumn
paperJobSizeMaximum=_PaperJobSizeMaximum_Object((1,3,6,1,4,1,641,6,4,2,5,1,3),_PaperJobSizeMaximum_Type())
paperJobSizeMaximum.setMaxAccess(_C)
if mibBuilder.loadTexts:paperJobSizeMaximum.setStatus(_A)
_PaperJobSizeSideCount_Type=Counter32
_PaperJobSizeSideCount_Object=MibTableColumn
paperJobSizeSideCount=_PaperJobSizeSideCount_Object((1,3,6,1,4,1,641,6,4,2,5,1,4),_PaperJobSizeSideCount_Type())
paperJobSizeSideCount.setMaxAccess(_C)
if mibBuilder.loadTexts:paperJobSizeSideCount.setStatus(_A)
_PaperJobSizeJobCount_Type=Counter32
_PaperJobSizeJobCount_Object=MibTableColumn
paperJobSizeJobCount=_PaperJobSizeJobCount_Object((1,3,6,1,4,1,641,6,4,2,5,1,5),_PaperJobSizeJobCount_Type())
paperJobSizeJobCount.setMaxAccess(_C)
if mibBuilder.loadTexts:paperJobSizeJobCount.setStatus(_A)
_ScanStats_ObjectIdentity=ObjectIdentity
scanStats=_ScanStats_ObjectIdentity((1,3,6,1,4,1,641,6,4,3))
_ScanCountTable_Object=MibTable
scanCountTable=_ScanCountTable_Object((1,3,6,1,4,1,641,6,4,3,1))
if mibBuilder.loadTexts:scanCountTable.setStatus(_A)
_ScanCountEntry_Object=MibTableRow
scanCountEntry=_ScanCountEntry_Object((1,3,6,1,4,1,641,6,4,3,1,1))
scanCountEntry.setIndexNames((0,_B,_E),(0,_B,_e))
if mibBuilder.loadTexts:scanCountEntry.setStatus(_A)
class _ScanCountIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_ScanCountIndex_Type.__name__=_D
_ScanCountIndex_Object=MibTableColumn
scanCountIndex=_ScanCountIndex_Object((1,3,6,1,4,1,641,6,4,3,1,1,1),_ScanCountIndex_Type())
scanCountIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:scanCountIndex.setStatus(_A)
class _ScanCountType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,257,258,259,260,261,262,263,769,770,771,772,773,774,775)));namedValues=NamedValues(*(('copyAdf',1),('faxAdf',2),('scanToEmailAdf',3),('scanToNetAdf',4),('scanToLocalHostAdf',5),('scanToUsbAdf',6),('scanToFtpAdf',7),('copyFlatbed',257),('faxFlatbed',258),('scanToEmailFlatbed',259),('scanToNetFlatbed',260),('scanToLocalHostFlatbed',261),('scanToUsbFlatbed',262),('scanToFtpFlatbed',263),('copyDuplex',769),('faxDuplex',770),('scanToEmailDuplex',771),('scanToNetDuplex',772),('scanToLocalHostDuplex',773),('scanToUsbDuplex',774),('scanToFtpDuplex',775)))
_ScanCountType_Type.__name__=_D
_ScanCountType_Object=MibTableColumn
scanCountType=_ScanCountType_Object((1,3,6,1,4,1,641,6,4,3,1,1,2),_ScanCountType_Type())
scanCountType.setMaxAccess(_C)
if mibBuilder.loadTexts:scanCountType.setStatus(_A)
_ScanCountSize_Type=PaperSizeTC
_ScanCountSize_Object=MibTableColumn
scanCountSize=_ScanCountSize_Object((1,3,6,1,4,1,641,6,4,3,1,1,3),_ScanCountSize_Type())
scanCountSize.setMaxAccess(_C)
if mibBuilder.loadTexts:scanCountSize.setStatus(_A)
_ScanCountSides_Type=Counter32
_ScanCountSides_Object=MibTableColumn
scanCountSides=_ScanCountSides_Object((1,3,6,1,4,1,641,6,4,3,1,1,4),_ScanCountSides_Type())
scanCountSides.setMaxAccess(_C)
if mibBuilder.loadTexts:scanCountSides.setStatus(_A)
_ScanCountSheets_Type=Counter32
_ScanCountSheets_Object=MibTableColumn
scanCountSheets=_ScanCountSheets_Object((1,3,6,1,4,1,641,6,4,3,1,1,5),_ScanCountSheets_Type())
scanCountSheets.setMaxAccess(_C)
if mibBuilder.loadTexts:scanCountSheets.setStatus(_A)
_SupplyStats_ObjectIdentity=ObjectIdentity
supplyStats=_SupplyStats_ObjectIdentity((1,3,6,1,4,1,641,6,4,4))
_CurrentSuppliesTable_Object=MibTable
currentSuppliesTable=_CurrentSuppliesTable_Object((1,3,6,1,4,1,641,6,4,4,1))
if mibBuilder.loadTexts:currentSuppliesTable.setStatus(_A)
_CurrentSuppliesEntry_Object=MibTableRow
currentSuppliesEntry=_CurrentSuppliesEntry_Object((1,3,6,1,4,1,641,6,4,4,1,1))
currentSuppliesEntry.setIndexNames((0,_B,_E),(0,_B,_f))
if mibBuilder.loadTexts:currentSuppliesEntry.setStatus(_A)
class _CurrentSupplyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CurrentSupplyIndex_Type.__name__=_D
_CurrentSupplyIndex_Object=MibTableColumn
currentSupplyIndex=_CurrentSupplyIndex_Object((1,3,6,1,4,1,641,6,4,4,1,1,1),_CurrentSupplyIndex_Type())
currentSupplyIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:currentSupplyIndex.setStatus(_A)
class _CurrentSupplyInventoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_CurrentSupplyInventoryIndex_Type.__name__=_D
_CurrentSupplyInventoryIndex_Object=MibTableColumn
currentSupplyInventoryIndex=_CurrentSupplyInventoryIndex_Object((1,3,6,1,4,1,641,6,4,4,1,1,2),_CurrentSupplyInventoryIndex_Type())
currentSupplyInventoryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:currentSupplyInventoryIndex.setStatus(_A)
_CurrentSupplyType_Type=SupplyTypeTC
_CurrentSupplyType_Object=MibTableColumn
currentSupplyType=_CurrentSupplyType_Object((1,3,6,1,4,1,641,6,4,4,1,1,3),_CurrentSupplyType_Type())
currentSupplyType.setMaxAccess(_C)
if mibBuilder.loadTexts:currentSupplyType.setStatus(_A)
_CurrentSupplyColorantValue_Type=DisplayString
_CurrentSupplyColorantValue_Object=MibTableColumn
currentSupplyColorantValue=_CurrentSupplyColorantValue_Object((1,3,6,1,4,1,641,6,4,4,1,1,4),_CurrentSupplyColorantValue_Type())
currentSupplyColorantValue.setMaxAccess(_C)
if mibBuilder.loadTexts:currentSupplyColorantValue.setStatus(_A)
_CurrentSupplyDescription_Type=SnmpAdminString
_CurrentSupplyDescription_Object=MibTableColumn
currentSupplyDescription=_CurrentSupplyDescription_Object((1,3,6,1,4,1,641,6,4,4,1,1,5),_CurrentSupplyDescription_Type())
currentSupplyDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:currentSupplyDescription.setStatus(_A)
class _CurrentSupplySerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CurrentSupplySerialNumber_Type.__name__=_G
_CurrentSupplySerialNumber_Object=MibTableColumn
currentSupplySerialNumber=_CurrentSupplySerialNumber_Object((1,3,6,1,4,1,641,6,4,4,1,1,6),_CurrentSupplySerialNumber_Type())
currentSupplySerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:currentSupplySerialNumber.setStatus(_A)
class _CurrentSupplyPartNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_CurrentSupplyPartNumber_Type.__name__=_G
_CurrentSupplyPartNumber_Object=MibTableColumn
currentSupplyPartNumber=_CurrentSupplyPartNumber_Object((1,3,6,1,4,1,641,6,4,4,1,1,7),_CurrentSupplyPartNumber_Type())
currentSupplyPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:currentSupplyPartNumber.setStatus(_A)
class _CurrentSupplyClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('filled',1),('consumed',2)))
_CurrentSupplyClass_Type.__name__=_D
_CurrentSupplyClass_Object=MibTableColumn
currentSupplyClass=_CurrentSupplyClass_Object((1,3,6,1,4,1,641,6,4,4,1,1,8),_CurrentSupplyClass_Type())
currentSupplyClass.setMaxAccess(_C)
if mibBuilder.loadTexts:currentSupplyClass.setStatus(_A)
_CurrentSupplyCartridgeType_Type=CartridgeTypeTC
_CurrentSupplyCartridgeType_Object=MibTableColumn
currentSupplyCartridgeType=_CurrentSupplyCartridgeType_Object((1,3,6,1,4,1,641,6,4,4,1,1,9),_CurrentSupplyCartridgeType_Type())
currentSupplyCartridgeType.setMaxAccess(_C)
if mibBuilder.loadTexts:currentSupplyCartridgeType.setStatus(_A)
_CurrentSupplyInstallDate_Type=DateAndTime
_CurrentSupplyInstallDate_Object=MibTableColumn
currentSupplyInstallDate=_CurrentSupplyInstallDate_Object((1,3,6,1,4,1,641,6,4,4,1,1,10),_CurrentSupplyInstallDate_Type())
currentSupplyInstallDate.setMaxAccess(_C)
if mibBuilder.loadTexts:currentSupplyInstallDate.setStatus(_A)
_CurrentSupplyPageCountAtInstall_Type=Counter32
_CurrentSupplyPageCountAtInstall_Object=MibTableColumn
currentSupplyPageCountAtInstall=_CurrentSupplyPageCountAtInstall_Object((1,3,6,1,4,1,641,6,4,4,1,1,11),_CurrentSupplyPageCountAtInstall_Type())
currentSupplyPageCountAtInstall.setMaxAccess(_C)
if mibBuilder.loadTexts:currentSupplyPageCountAtInstall.setStatus(_A)
class _CurrentSupplyCurrentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_I,1),(_H,2),('ok',3),('low',4),('empty',5),(_U,6)))
_CurrentSupplyCurrentStatus_Type.__name__=_D
_CurrentSupplyCurrentStatus_Object=MibTableColumn
currentSupplyCurrentStatus=_CurrentSupplyCurrentStatus_Object((1,3,6,1,4,1,641,6,4,4,1,1,12),_CurrentSupplyCurrentStatus_Type())
currentSupplyCurrentStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:currentSupplyCurrentStatus.setStatus(_A)
_CurrentSupplyCapacityUnit_Type=UnitsTC
_CurrentSupplyCapacityUnit_Object=MibTableColumn
currentSupplyCapacityUnit=_CurrentSupplyCapacityUnit_Object((1,3,6,1,4,1,641,6,4,4,1,1,13),_CurrentSupplyCapacityUnit_Type())
currentSupplyCapacityUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:currentSupplyCapacityUnit.setStatus(_A)
class _CurrentSupplyCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CurrentSupplyCapacity_Type.__name__=_D
_CurrentSupplyCapacity_Object=MibTableColumn
currentSupplyCapacity=_CurrentSupplyCapacity_Object((1,3,6,1,4,1,641,6,4,4,1,1,14),_CurrentSupplyCapacity_Type())
currentSupplyCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:currentSupplyCapacity.setStatus(_A)
_CurrentSupplyFirstKnownLevel_Type=Counter32
_CurrentSupplyFirstKnownLevel_Object=MibTableColumn
currentSupplyFirstKnownLevel=_CurrentSupplyFirstKnownLevel_Object((1,3,6,1,4,1,641,6,4,4,1,1,15),_CurrentSupplyFirstKnownLevel_Type())
currentSupplyFirstKnownLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:currentSupplyFirstKnownLevel.setStatus(_A)
_CurrentSupplyCurrentLevel_Type=Counter32
_CurrentSupplyCurrentLevel_Object=MibTableColumn
currentSupplyCurrentLevel=_CurrentSupplyCurrentLevel_Object((1,3,6,1,4,1,641,6,4,4,1,1,16),_CurrentSupplyCurrentLevel_Type())
currentSupplyCurrentLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:currentSupplyCurrentLevel.setStatus(_A)
_CurrentSupplyUsage_Type=Counter32
_CurrentSupplyUsage_Object=MibTableColumn
currentSupplyUsage=_CurrentSupplyUsage_Object((1,3,6,1,4,1,641,6,4,4,1,1,17),_CurrentSupplyUsage_Type())
currentSupplyUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:currentSupplyUsage.setStatus(_A)
_CurrentSupplyCalibrations_Type=Counter32
_CurrentSupplyCalibrations_Object=MibTableColumn
currentSupplyCalibrations=_CurrentSupplyCalibrations_Object((1,3,6,1,4,1,641,6,4,4,1,1,18),_CurrentSupplyCalibrations_Type())
currentSupplyCalibrations.setMaxAccess(_C)
if mibBuilder.loadTexts:currentSupplyCalibrations.setStatus(_A)
_CurrentSupplyCoverage_Type=Counter32
_CurrentSupplyCoverage_Object=MibTableColumn
currentSupplyCoverage=_CurrentSupplyCoverage_Object((1,3,6,1,4,1,641,6,4,4,1,1,19),_CurrentSupplyCoverage_Type())
currentSupplyCoverage.setMaxAccess(_C)
if mibBuilder.loadTexts:currentSupplyCoverage.setStatus(_A)
_CurrentSupplyDaysRemaining_Type=Integer32
_CurrentSupplyDaysRemaining_Object=MibTableColumn
currentSupplyDaysRemaining=_CurrentSupplyDaysRemaining_Object((1,3,6,1,4,1,641,6,4,4,1,1,20),_CurrentSupplyDaysRemaining_Type())
currentSupplyDaysRemaining.setMaxAccess(_C)
if mibBuilder.loadTexts:currentSupplyDaysRemaining.setStatus(_A)
_SupplyHistoryTable_Object=MibTable
supplyHistoryTable=_SupplyHistoryTable_Object((1,3,6,1,4,1,641,6,4,4,2))
if mibBuilder.loadTexts:supplyHistoryTable.setStatus(_A)
_SupplyHistoryEntry_Object=MibTableRow
supplyHistoryEntry=_SupplyHistoryEntry_Object((1,3,6,1,4,1,641,6,4,4,2,1))
supplyHistoryEntry.setIndexNames((0,_B,_E),(0,_B,_g))
if mibBuilder.loadTexts:supplyHistoryEntry.setStatus(_A)
class _SupplyHistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SupplyHistoryIndex_Type.__name__=_D
_SupplyHistoryIndex_Object=MibTableColumn
supplyHistoryIndex=_SupplyHistoryIndex_Object((1,3,6,1,4,1,641,6,4,4,2,1,1),_SupplyHistoryIndex_Type())
supplyHistoryIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:supplyHistoryIndex.setStatus(_A)
class _SupplyHistoryInventoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SupplyHistoryInventoryIndex_Type.__name__=_D
_SupplyHistoryInventoryIndex_Object=MibTableColumn
supplyHistoryInventoryIndex=_SupplyHistoryInventoryIndex_Object((1,3,6,1,4,1,641,6,4,4,2,1,2),_SupplyHistoryInventoryIndex_Type())
supplyHistoryInventoryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistoryInventoryIndex.setStatus(_A)
_SupplyHistorySupplyType_Type=SupplyTypeTC
_SupplyHistorySupplyType_Object=MibTableColumn
supplyHistorySupplyType=_SupplyHistorySupplyType_Object((1,3,6,1,4,1,641,6,4,4,2,1,3),_SupplyHistorySupplyType_Type())
supplyHistorySupplyType.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistorySupplyType.setStatus(_A)
_SupplyHistoryColorantValue_Type=DisplayString
_SupplyHistoryColorantValue_Object=MibTableColumn
supplyHistoryColorantValue=_SupplyHistoryColorantValue_Object((1,3,6,1,4,1,641,6,4,4,2,1,4),_SupplyHistoryColorantValue_Type())
supplyHistoryColorantValue.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistoryColorantValue.setStatus(_A)
_SupplyHistoryDescription_Type=SnmpAdminString
_SupplyHistoryDescription_Object=MibTableColumn
supplyHistoryDescription=_SupplyHistoryDescription_Object((1,3,6,1,4,1,641,6,4,4,2,1,5),_SupplyHistoryDescription_Type())
supplyHistoryDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistoryDescription.setStatus(_A)
class _SupplyHistorySerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_SupplyHistorySerialNumber_Type.__name__=_G
_SupplyHistorySerialNumber_Object=MibTableColumn
supplyHistorySerialNumber=_SupplyHistorySerialNumber_Object((1,3,6,1,4,1,641,6,4,4,2,1,6),_SupplyHistorySerialNumber_Type())
supplyHistorySerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistorySerialNumber.setStatus(_A)
_SupplyHistoryCartridgeType_Type=CartridgeTypeTC
_SupplyHistoryCartridgeType_Object=MibTableColumn
supplyHistoryCartridgeType=_SupplyHistoryCartridgeType_Object((1,3,6,1,4,1,641,6,4,4,2,1,7),_SupplyHistoryCartridgeType_Type())
supplyHistoryCartridgeType.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistoryCartridgeType.setStatus(_A)
_SupplyHistoryInstallDate_Type=DateAndTime
_SupplyHistoryInstallDate_Object=MibTableColumn
supplyHistoryInstallDate=_SupplyHistoryInstallDate_Object((1,3,6,1,4,1,641,6,4,4,2,1,8),_SupplyHistoryInstallDate_Type())
supplyHistoryInstallDate.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistoryInstallDate.setStatus(_A)
_SupplyHistoryPageCount_Type=Counter32
_SupplyHistoryPageCount_Object=MibTableColumn
supplyHistoryPageCount=_SupplyHistoryPageCount_Object((1,3,6,1,4,1,641,6,4,4,2,1,9),_SupplyHistoryPageCount_Type())
supplyHistoryPageCount.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistoryPageCount.setStatus(_A)
_SupplyHistoryCapacityUnit_Type=UnitsTC
_SupplyHistoryCapacityUnit_Object=MibTableColumn
supplyHistoryCapacityUnit=_SupplyHistoryCapacityUnit_Object((1,3,6,1,4,1,641,6,4,4,2,1,10),_SupplyHistoryCapacityUnit_Type())
supplyHistoryCapacityUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistoryCapacityUnit.setStatus(_A)
class _SupplyHistoryCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SupplyHistoryCapacity_Type.__name__=_D
_SupplyHistoryCapacity_Object=MibTableColumn
supplyHistoryCapacity=_SupplyHistoryCapacity_Object((1,3,6,1,4,1,641,6,4,4,2,1,11),_SupplyHistoryCapacity_Type())
supplyHistoryCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistoryCapacity.setStatus(_A)
_SupplyHistoryLastLevel_Type=Counter32
_SupplyHistoryLastLevel_Object=MibTableColumn
supplyHistoryLastLevel=_SupplyHistoryLastLevel_Object((1,3,6,1,4,1,641,6,4,4,2,1,12),_SupplyHistoryLastLevel_Type())
supplyHistoryLastLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistoryLastLevel.setStatus(_A)
_SupplyHistoryUsage_Type=Counter32
_SupplyHistoryUsage_Object=MibTableColumn
supplyHistoryUsage=_SupplyHistoryUsage_Object((1,3,6,1,4,1,641,6,4,4,2,1,13),_SupplyHistoryUsage_Type())
supplyHistoryUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistoryUsage.setStatus(_A)
_SupplyHistoryCalibrations_Type=Counter32
_SupplyHistoryCalibrations_Object=MibTableColumn
supplyHistoryCalibrations=_SupplyHistoryCalibrations_Object((1,3,6,1,4,1,641,6,4,4,2,1,14),_SupplyHistoryCalibrations_Type())
supplyHistoryCalibrations.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistoryCalibrations.setStatus(_A)
_SupplyHistoryCoverage_Type=Counter32
_SupplyHistoryCoverage_Object=MibTableColumn
supplyHistoryCoverage=_SupplyHistoryCoverage_Object((1,3,6,1,4,1,641,6,4,4,2,1,15),_SupplyHistoryCoverage_Type())
supplyHistoryCoverage.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistoryCoverage.setStatus(_A)
_SupplyHistogramTable_Object=MibTable
supplyHistogramTable=_SupplyHistogramTable_Object((1,3,6,1,4,1,641,6,4,4,3))
if mibBuilder.loadTexts:supplyHistogramTable.setStatus(_A)
_SupplyHistogramEntry_Object=MibTableRow
supplyHistogramEntry=_SupplyHistogramEntry_Object((1,3,6,1,4,1,641,6,4,4,3,1))
supplyHistogramEntry.setIndexNames((0,_B,_E),(0,_B,_h))
if mibBuilder.loadTexts:supplyHistogramEntry.setStatus(_A)
class _SupplyHistogramIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SupplyHistogramIndex_Type.__name__=_D
_SupplyHistogramIndex_Object=MibTableColumn
supplyHistogramIndex=_SupplyHistogramIndex_Object((1,3,6,1,4,1,641,6,4,4,3,1,1),_SupplyHistogramIndex_Type())
supplyHistogramIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:supplyHistogramIndex.setStatus(_A)
class _SupplyHistogramInventoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SupplyHistogramInventoryIndex_Type.__name__=_D
_SupplyHistogramInventoryIndex_Object=MibTableColumn
supplyHistogramInventoryIndex=_SupplyHistogramInventoryIndex_Object((1,3,6,1,4,1,641,6,4,4,3,1,2),_SupplyHistogramInventoryIndex_Type())
supplyHistogramInventoryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistogramInventoryIndex.setStatus(_A)
_SupplyHistogramSupplyType_Type=SupplyTypeTC
_SupplyHistogramSupplyType_Object=MibTableColumn
supplyHistogramSupplyType=_SupplyHistogramSupplyType_Object((1,3,6,1,4,1,641,6,4,4,3,1,3),_SupplyHistogramSupplyType_Type())
supplyHistogramSupplyType.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistogramSupplyType.setStatus(_A)
_SupplyHistogramColorantValue_Type=DisplayString
_SupplyHistogramColorantValue_Object=MibTableColumn
supplyHistogramColorantValue=_SupplyHistogramColorantValue_Object((1,3,6,1,4,1,641,6,4,4,3,1,4),_SupplyHistogramColorantValue_Type())
supplyHistogramColorantValue.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistogramColorantValue.setStatus(_A)
_SupplyHistogramDescription_Type=SnmpAdminString
_SupplyHistogramDescription_Object=MibTableColumn
supplyHistogramDescription=_SupplyHistogramDescription_Object((1,3,6,1,4,1,641,6,4,4,3,1,5),_SupplyHistogramDescription_Type())
supplyHistogramDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistogramDescription.setStatus(_A)
_SupplyHistogramCapacityUnit_Type=UnitsTC
_SupplyHistogramCapacityUnit_Object=MibTableColumn
supplyHistogramCapacityUnit=_SupplyHistogramCapacityUnit_Object((1,3,6,1,4,1,641,6,4,4,3,1,6),_SupplyHistogramCapacityUnit_Type())
supplyHistogramCapacityUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistogramCapacityUnit.setStatus(_A)
class _SupplyHistogramCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SupplyHistogramCapacity_Type.__name__=_D
_SupplyHistogramCapacity_Object=MibTableColumn
supplyHistogramCapacity=_SupplyHistogramCapacity_Object((1,3,6,1,4,1,641,6,4,4,3,1,7),_SupplyHistogramCapacity_Type())
supplyHistogramCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistogramCapacity.setStatus(_A)
_SupplyHistogramCount_Type=Counter32
_SupplyHistogramCount_Object=MibTableColumn
supplyHistogramCount=_SupplyHistogramCount_Object((1,3,6,1,4,1,641,6,4,4,3,1,8),_SupplyHistogramCount_Type())
supplyHistogramCount.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistogramCount.setStatus(_A)
_SupplyHistogramCountUnits_Type=UnitsTC
_SupplyHistogramCountUnits_Object=MibTableColumn
supplyHistogramCountUnits=_SupplyHistogramCountUnits_Object((1,3,6,1,4,1,641,6,4,4,3,1,9),_SupplyHistogramCountUnits_Type())
supplyHistogramCountUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistogramCountUnits.setStatus(_A)
_SupplyHistogramWithHistoryTable_Object=MibTable
supplyHistogramWithHistoryTable=_SupplyHistogramWithHistoryTable_Object((1,3,6,1,4,1,641,6,4,4,4))
if mibBuilder.loadTexts:supplyHistogramWithHistoryTable.setStatus(_A)
_SupplyHistogramHistoryEntry_Object=MibTableRow
supplyHistogramHistoryEntry=_SupplyHistogramHistoryEntry_Object((1,3,6,1,4,1,641,6,4,4,4,1))
supplyHistogramHistoryEntry.setIndexNames((0,_B,_E),(0,_B,_i),(0,_B,_j))
if mibBuilder.loadTexts:supplyHistogramHistoryEntry.setStatus(_A)
class _SupplyHistogramHistoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SupplyHistogramHistoryIndex_Type.__name__=_D
_SupplyHistogramHistoryIndex_Object=MibTableColumn
supplyHistogramHistoryIndex=_SupplyHistogramHistoryIndex_Object((1,3,6,1,4,1,641,6,4,4,4,1,1),_SupplyHistogramHistoryIndex_Type())
supplyHistogramHistoryIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:supplyHistogramHistoryIndex.setStatus(_A)
class _SupplyHistogramHistoryInventoryIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SupplyHistogramHistoryInventoryIndex_Type.__name__=_D
_SupplyHistogramHistoryInventoryIndex_Object=MibTableColumn
supplyHistogramHistoryInventoryIndex=_SupplyHistogramHistoryInventoryIndex_Object((1,3,6,1,4,1,641,6,4,4,4,1,2),_SupplyHistogramHistoryInventoryIndex_Type())
supplyHistogramHistoryInventoryIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistogramHistoryInventoryIndex.setStatus(_A)
class _SupplyHistogramHistoryCountIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_SupplyHistogramHistoryCountIndex_Type.__name__=_D
_SupplyHistogramHistoryCountIndex_Object=MibTableColumn
supplyHistogramHistoryCountIndex=_SupplyHistogramHistoryCountIndex_Object((1,3,6,1,4,1,641,6,4,4,4,1,3),_SupplyHistogramHistoryCountIndex_Type())
supplyHistogramHistoryCountIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistogramHistoryCountIndex.setStatus(_A)
_SupplyHistogramHistorySupplyType_Type=SupplyTypeTC
_SupplyHistogramHistorySupplyType_Object=MibTableColumn
supplyHistogramHistorySupplyType=_SupplyHistogramHistorySupplyType_Object((1,3,6,1,4,1,641,6,4,4,4,1,4),_SupplyHistogramHistorySupplyType_Type())
supplyHistogramHistorySupplyType.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistogramHistorySupplyType.setStatus(_A)
_SupplyHistogramHistoryColorantValue_Type=DisplayString
_SupplyHistogramHistoryColorantValue_Object=MibTableColumn
supplyHistogramHistoryColorantValue=_SupplyHistogramHistoryColorantValue_Object((1,3,6,1,4,1,641,6,4,4,4,1,5),_SupplyHistogramHistoryColorantValue_Type())
supplyHistogramHistoryColorantValue.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistogramHistoryColorantValue.setStatus(_A)
_SupplyHistogramHistoryDescription_Type=SnmpAdminString
_SupplyHistogramHistoryDescription_Object=MibTableColumn
supplyHistogramHistoryDescription=_SupplyHistogramHistoryDescription_Object((1,3,6,1,4,1,641,6,4,4,4,1,6),_SupplyHistogramHistoryDescription_Type())
supplyHistogramHistoryDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistogramHistoryDescription.setStatus(_A)
_SupplyHistogramHistoryCapacityUnit_Type=UnitsTC
_SupplyHistogramHistoryCapacityUnit_Object=MibTableColumn
supplyHistogramHistoryCapacityUnit=_SupplyHistogramHistoryCapacityUnit_Object((1,3,6,1,4,1,641,6,4,4,4,1,7),_SupplyHistogramHistoryCapacityUnit_Type())
supplyHistogramHistoryCapacityUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistogramHistoryCapacityUnit.setStatus(_A)
class _SupplyHistogramHistoryCapacity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_SupplyHistogramHistoryCapacity_Type.__name__=_D
_SupplyHistogramHistoryCapacity_Object=MibTableColumn
supplyHistogramHistoryCapacity=_SupplyHistogramHistoryCapacity_Object((1,3,6,1,4,1,641,6,4,4,4,1,8),_SupplyHistogramHistoryCapacity_Type())
supplyHistogramHistoryCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistogramHistoryCapacity.setStatus(_A)
_SupplyHistogramHistoryCount_Type=Counter32
_SupplyHistogramHistoryCount_Object=MibTableColumn
supplyHistogramHistoryCount=_SupplyHistogramHistoryCount_Object((1,3,6,1,4,1,641,6,4,4,4,1,9),_SupplyHistogramHistoryCount_Type())
supplyHistogramHistoryCount.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistogramHistoryCount.setStatus(_A)
_SupplyHistogramHistoryCountUnits_Type=UnitsTC
_SupplyHistogramHistoryCountUnits_Object=MibTableColumn
supplyHistogramHistoryCountUnits=_SupplyHistogramHistoryCountUnits_Object((1,3,6,1,4,1,641,6,4,4,4,1,10),_SupplyHistogramHistoryCountUnits_Type())
supplyHistogramHistoryCountUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:supplyHistogramHistoryCountUnits.setStatus(_A)
_Alerts_ObjectIdentity=ObjectIdentity
alerts=_Alerts_ObjectIdentity((1,3,6,1,4,1,641,6,5))
_DeviceAlertTable_Object=MibTable
deviceAlertTable=_DeviceAlertTable_Object((1,3,6,1,4,1,641,6,5,1))
if mibBuilder.loadTexts:deviceAlertTable.setStatus(_A)
_DeviceAlertEntry_Object=MibTableRow
deviceAlertEntry=_DeviceAlertEntry_Object((1,3,6,1,4,1,641,6,5,1,1))
deviceAlertEntry.setIndexNames((0,_B,_E),(0,_B,_J))
if mibBuilder.loadTexts:deviceAlertEntry.setStatus(_A)
class _DeviceAlertIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DeviceAlertIndex_Type.__name__=_D
_DeviceAlertIndex_Object=MibTableColumn
deviceAlertIndex=_DeviceAlertIndex_Object((1,3,6,1,4,1,641,6,5,1,1,1),_DeviceAlertIndex_Type())
deviceAlertIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceAlertIndex.setStatus(_A)
class _DeviceAlertConfigTableNode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4)));namedValues=NamedValues(*((_H,0),(_k,2),(_l,3),(_m,4)))
_DeviceAlertConfigTableNode_Type.__name__=_D
_DeviceAlertConfigTableNode_Object=MibTableColumn
deviceAlertConfigTableNode=_DeviceAlertConfigTableNode_Object((1,3,6,1,4,1,641,6,5,1,1,2),_DeviceAlertConfigTableNode_Type())
deviceAlertConfigTableNode.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceAlertConfigTableNode.setStatus(_A)
class _DeviceAlertConfigTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_DeviceAlertConfigTableIndex_Type.__name__=_D
_DeviceAlertConfigTableIndex_Object=MibTableColumn
deviceAlertConfigTableIndex=_DeviceAlertConfigTableIndex_Object((1,3,6,1,4,1,641,6,5,1,1,3),_DeviceAlertConfigTableIndex_Type())
deviceAlertConfigTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceAlertConfigTableIndex.setStatus(_A)
_DeviceAlertSeverity_Type=SeverityTC
_DeviceAlertSeverity_Object=MibTableColumn
deviceAlertSeverity=_DeviceAlertSeverity_Object((1,3,6,1,4,1,641,6,5,1,1,4),_DeviceAlertSeverity_Type())
deviceAlertSeverity.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceAlertSeverity.setStatus(_A)
_DeviceAlertCode_Type=AlertCodeTC
_DeviceAlertCode_Object=MibTableColumn
deviceAlertCode=_DeviceAlertCode_Object((1,3,6,1,4,1,641,6,5,1,1,5),_DeviceAlertCode_Type())
deviceAlertCode.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceAlertCode.setStatus(_A)
_DeviceAlertDescription_Type=SnmpAdminString
_DeviceAlertDescription_Object=MibTableColumn
deviceAlertDescription=_DeviceAlertDescription_Object((1,3,6,1,4,1,641,6,5,1,1,6),_DeviceAlertDescription_Type())
deviceAlertDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceAlertDescription.setStatus(_A)
_DeviceAlertData_Type=KeyValueTC
_DeviceAlertData_Object=MibTableColumn
deviceAlertData=_DeviceAlertData_Object((1,3,6,1,4,1,641,6,5,1,1,7),_DeviceAlertData_Type())
deviceAlertData.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceAlertData.setStatus(_A)
_DeviceAlertTime_Type=DateAndTime
_DeviceAlertTime_Object=MibTableColumn
deviceAlertTime=_DeviceAlertTime_Object((1,3,6,1,4,1,641,6,5,1,1,8),_DeviceAlertTime_Type())
deviceAlertTime.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceAlertTime.setStatus(_A)
_DeviceAlertSeverityLevel_Type=PrtAlertSeverityLevelTC
_DeviceAlertSeverityLevel_Object=MibTableColumn
deviceAlertSeverityLevel=_DeviceAlertSeverityLevel_Object((1,3,6,1,4,1,641,6,5,1,1,9),_DeviceAlertSeverityLevel_Type())
deviceAlertSeverityLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceAlertSeverityLevel.setStatus(_A)
_DeviceAlertTrainingLevel_Type=PrtAlertTrainingLevelTC
_DeviceAlertTrainingLevel_Object=MibTableColumn
deviceAlertTrainingLevel=_DeviceAlertTrainingLevel_Object((1,3,6,1,4,1,641,6,5,1,1,10),_DeviceAlertTrainingLevel_Type())
deviceAlertTrainingLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceAlertTrainingLevel.setStatus(_A)
_DeviceAlertPrtCode_Type=PrtAlertCodeTC
_DeviceAlertPrtCode_Object=MibTableColumn
deviceAlertPrtCode=_DeviceAlertPrtCode_Object((1,3,6,1,4,1,641,6,5,1,1,11),_DeviceAlertPrtCode_Type())
deviceAlertPrtCode.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceAlertPrtCode.setStatus(_A)
_DeviceV1AlertMPS_ObjectIdentity=ObjectIdentity
deviceV1AlertMPS=_DeviceV1AlertMPS_ObjectIdentity((1,3,6,1,4,1,641,6,5,2))
_DeviceV2AlertMPSPrefix_ObjectIdentity=ObjectIdentity
deviceV2AlertMPSPrefix=_DeviceV2AlertMPSPrefix_ObjectIdentity((1,3,6,1,4,1,641,6,5,2,0))
_Logs_ObjectIdentity=ObjectIdentity
logs=_Logs_ObjectIdentity((1,3,6,1,4,1,641,6,6))
_Applications_ObjectIdentity=ObjectIdentity
applications=_Applications_ObjectIdentity((1,3,6,1,4,1,641,6,7))
_Outputfeature_ObjectIdentity=ObjectIdentity
outputfeature=_Outputfeature_ObjectIdentity((1,3,6,1,4,1,641,6,8))
_OutputOptionFeatureTable_Object=MibTable
outputOptionFeatureTable=_OutputOptionFeatureTable_Object((1,3,6,1,4,1,641,6,8,1))
if mibBuilder.loadTexts:outputOptionFeatureTable.setStatus(_A)
_OutputOptionEntry_Object=MibTableRow
outputOptionEntry=_OutputOptionEntry_Object((1,3,6,1,4,1,641,6,8,1,1))
outputOptionEntry.setIndexNames((0,_B,_E),(0,_B,_n))
if mibBuilder.loadTexts:outputOptionEntry.setStatus(_A)
class _OutputOptionIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OutputOptionIndex_Type.__name__=_D
_OutputOptionIndex_Object=MibTableColumn
outputOptionIndex=_OutputOptionIndex_Object((1,3,6,1,4,1,641,6,8,1,1,1),_OutputOptionIndex_Type())
outputOptionIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:outputOptionIndex.setStatus(_A)
_OutputOptionName_Type=DisplayString
_OutputOptionName_Object=MibTableColumn
outputOptionName=_OutputOptionName_Object((1,3,6,1,4,1,641,6,8,1,1,2),_OutputOptionName_Type())
outputOptionName.setMaxAccess(_C)
if mibBuilder.loadTexts:outputOptionName.setStatus(_A)
class _OutputLevelSensing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_o,0),(_p,1)))
_OutputLevelSensing_Type.__name__=_D
_OutputLevelSensing_Object=MibTableColumn
outputLevelSensing=_OutputLevelSensing_Object((1,3,6,1,4,1,641,6,8,1,1,3),_OutputLevelSensing_Type())
outputLevelSensing.setMaxAccess(_C)
if mibBuilder.loadTexts:outputLevelSensing.setStatus(_A)
class _OutputOffsetting_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_o,0),(_p,1)))
_OutputOffsetting_Type.__name__=_D
_OutputOffsetting_Object=MibTableColumn
outputOffsetting=_OutputOffsetting_Object((1,3,6,1,4,1,641,6,8,1,1,4),_OutputOffsetting_Type())
outputOffsetting.setMaxAccess(_C)
if mibBuilder.loadTexts:outputOffsetting.setStatus(_A)
class _OutputFoldSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OutputFoldSupport_Type.__name__=_D
_OutputFoldSupport_Object=MibTableColumn
outputFoldSupport=_OutputFoldSupport_Object((1,3,6,1,4,1,641,6,8,1,1,5),_OutputFoldSupport_Type())
outputFoldSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:outputFoldSupport.setStatus(_A)
_OutputfaceOrientation_Type=PrtOutputPageDeliveryOrientationTC
_OutputfaceOrientation_Object=MibTableColumn
outputfaceOrientation=_OutputfaceOrientation_Object((1,3,6,1,4,1,641,6,8,1,1,6),_OutputfaceOrientation_Type())
outputfaceOrientation.setMaxAccess(_C)
if mibBuilder.loadTexts:outputfaceOrientation.setStatus(_A)
class _OutputBindingCapable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OutputBindingCapable_Type.__name__=_D
_OutputBindingCapable_Object=MibTableColumn
outputBindingCapable=_OutputBindingCapable_Object((1,3,6,1,4,1,641,6,8,1,1,7),_OutputBindingCapable_Type())
outputBindingCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:outputBindingCapable.setStatus(_A)
class _OutputSeparationCapable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OutputSeparationCapable_Type.__name__=_D
_OutputSeparationCapable_Object=MibTableColumn
outputSeparationCapable=_OutputSeparationCapable_Object((1,3,6,1,4,1,641,6,8,1,1,8),_OutputSeparationCapable_Type())
outputSeparationCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:outputSeparationCapable.setStatus(_A)
class _OutputStitchingCapable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OutputStitchingCapable_Type.__name__=_D
_OutputStitchingCapable_Object=MibTableColumn
outputStitchingCapable=_OutputStitchingCapable_Object((1,3,6,1,4,1,641,6,8,1,1,9),_OutputStitchingCapable_Type())
outputStitchingCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:outputStitchingCapable.setStatus(_A)
class _OutputPunchingCapable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_OutputPunchingCapable_Type.__name__=_D
_OutputPunchingCapable_Object=MibTableColumn
outputPunchingCapable=_OutputPunchingCapable_Object((1,3,6,1,4,1,641,6,8,1,1,10),_OutputPunchingCapable_Type())
outputPunchingCapable.setMaxAccess(_C)
if mibBuilder.loadTexts:outputPunchingCapable.setStatus(_A)
deviceGroup=ObjectGroup((1,3,6,1,4,1,641,6,1,2,1))
deviceGroup.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:deviceGroup.setStatus(_A)
hwInventoryGroup=ObjectGroup((1,3,6,1,4,1,641,6,1,2,2))
hwInventoryGroup.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:hwInventoryGroup.setStatus(_A)
supplyInventoryGroup=ObjectGroup((1,3,6,1,4,1,641,6,1,2,3))
supplyInventoryGroup.setObjects(*((_B,_A6),(_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:supplyInventoryGroup.setStatus(_A)
swInventoryGroup=ObjectGroup((1,3,6,1,4,1,641,6,1,2,4))
swInventoryGroup.setObjects(*((_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:swInventoryGroup.setStatus(_A)
statsGeneralCountGroup=ObjectGroup((1,3,6,1,4,1,641,6,1,2,5))
statsGeneralCountGroup.setObjects(*((_B,_AI),(_B,_AJ),(_B,_AK)))
if mibBuilder.loadTexts:statsGeneralCountGroup.setStatus(_A)
statsPaperGeneralCountGroup=ObjectGroup((1,3,6,1,4,1,641,6,1,2,6))
statsPaperGeneralCountGroup.setObjects(*((_B,_AL),(_B,_AM),(_B,_AN)))
if mibBuilder.loadTexts:statsPaperGeneralCountGroup.setStatus(_A)
statsPaperSidesCountGroup=ObjectGroup((1,3,6,1,4,1,641,6,1,2,7))
statsPaperSidesCountGroup.setObjects(*((_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT)))
if mibBuilder.loadTexts:statsPaperSidesCountGroup.setStatus(_A)
statsPaperSheetsCountGroup=ObjectGroup((1,3,6,1,4,1,641,6,1,2,8))
statsPaperSheetsCountGroup.setObjects(*((_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX)))
if mibBuilder.loadTexts:statsPaperSheetsCountGroup.setStatus(_A)
statsPaperNupCountGroup=ObjectGroup((1,3,6,1,4,1,641,6,1,2,9))
statsPaperNupCountGroup.setObjects(*((_B,_AY),(_B,_AZ),(_B,_Aa)))
if mibBuilder.loadTexts:statsPaperNupCountGroup.setStatus(_A)
statsPaperJobSizeGroup=ObjectGroup((1,3,6,1,4,1,641,6,1,2,10))
statsPaperJobSizeGroup.setObjects(*((_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae)))
if mibBuilder.loadTexts:statsPaperJobSizeGroup.setStatus(_A)
statsScanGroup=ObjectGroup((1,3,6,1,4,1,641,6,1,2,11))
statsScanGroup.setObjects(*((_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai)))
if mibBuilder.loadTexts:statsScanGroup.setStatus(_A)
statsCurrentSuppliesGroup=ObjectGroup((1,3,6,1,4,1,641,6,1,2,12))
statsCurrentSuppliesGroup.setObjects(*((_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw),(_B,_Ax),(_B,_Ay),(_B,_Az),(_B,_A_)))
if mibBuilder.loadTexts:statsCurrentSuppliesGroup.setStatus(_A)
statsSupplyHistoryGroup=ObjectGroup((1,3,6,1,4,1,641,6,1,2,13))
statsSupplyHistoryGroup.setObjects(*((_B,_B0),(_B,_B1),(_B,_B2),(_B,_B3),(_B,_B4),(_B,_B5),(_B,_B6),(_B,_B7),(_B,_B8),(_B,_B9),(_B,_BA),(_B,_BB),(_B,_BC),(_B,_BD)))
if mibBuilder.loadTexts:statsSupplyHistoryGroup.setStatus(_A)
statsSupplyHistogramGroup=ObjectGroup((1,3,6,1,4,1,641,6,1,2,14))
statsSupplyHistogramGroup.setObjects(*((_B,_BE),(_B,_BF),(_B,_BG),(_B,_BH),(_B,_BI),(_B,_BJ),(_B,_BK),(_B,_BL)))
if mibBuilder.loadTexts:statsSupplyHistogramGroup.setStatus(_A)
deviceAlertGroup=ObjectGroup((1,3,6,1,4,1,641,6,1,2,16))
deviceAlertGroup.setObjects(*((_B,_J),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:deviceAlertGroup.setStatus(_A)
deviceV2AlertMPS=NotificationType((1,3,6,1,4,1,641,6,5,2,0,1))
deviceV2AlertMPS.setObjects(*((_B,_J),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:deviceV2AlertMPS.setStatus(_A)
mpsMIBCompliance=ModuleCompliance((1,3,6,1,4,1,641,6,1,1,1))
mpsMIBCompliance.setObjects(*((_B,_S),(_B,_S),(_B,_BM),(_B,_BN),(_B,_BO),(_B,_BP),(_B,_BQ),(_B,_BR),(_B,_BS),(_B,_BT),(_B,_BU),(_B,_BV),(_B,_BW),(_B,_BX),(_B,_BY),(_B,_BZ)))
if mibBuilder.loadTexts:mpsMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SupplyTypeTC':SupplyTypeTC,'CartridgeTypeTC':CartridgeTypeTC,'SeverityTC':SeverityTC,'AlertCodeTC':AlertCodeTC,'mpsMibModule':mpsMibModule,'mps':mps,'mpsMIBAdminInfo':mpsMIBAdminInfo,'mpsMIBCompliances':mpsMIBCompliances,'mpsMIBCompliance':mpsMIBCompliance,'mpsMIBGroups':mpsMIBGroups,_S:deviceGroup,_BM:hwInventoryGroup,_BN:supplyInventoryGroup,_BO:swInventoryGroup,_BP:statsGeneralCountGroup,_BQ:statsPaperGeneralCountGroup,_BR:statsPaperSidesCountGroup,_BS:statsPaperSheetsCountGroup,_BT:statsPaperNupCountGroup,_BU:statsPaperJobSizeGroup,_BV:statsScanGroup,_BW:statsCurrentSuppliesGroup,_BX:statsSupplyHistoryGroup,_BY:statsSupplyHistogramGroup,_BZ:deviceAlertGroup,'device':device,_q:deviceMibLocalization,'deviceTable':deviceTable,'deviceEntry':deviceEntry,_E:deviceIndex,_r:devicePort,_s:deviceHrDeviceIndex,_t:deviceModel,_u:deviceSerialNumber,_v:deviceMibVersion,_w:deviceInstallDate,_x:deviceMibSupportLevel,'deviceMachineType':deviceMachineType,'deviceTLI':deviceTLI,'inventory':inventory,_k:hwInventoryTable,'hwInventoryEntry':hwInventoryEntry,_V:hwInventoryIndex,_y:hwInventoryParentIndex,_z:hwInventoryType,_A0:hwInventoryAdminStatus,_A1:hwInventoryStatus,_A2:hwInventoryPartNumber,_A3:hwInventorySerialNumber,_A4:hwInventoryDescription,_A5:hwInventoryData,_l:supplyInventoryTable,'supplyInventoryEntry':supplyInventoryEntry,_W:supplyInventoryIndex,_A6:supplyInventoryType,_A7:supplyInventoryColorantValue,_A8:supplyInventoryDescription,'supplyDynamicIndex':supplyDynamicIndex,_m:swInventoryTable,'swInventoryEntry':swInventoryEntry,_X:swInventoryIndex,_A9:swInventoryParentIndex,_AA:swInventoryType,_AD:swInventoryAdminStatus,_AE:swInventoryStatus,_AB:swInventoryName,_AC:swInventoryRevision,_AF:swInventoryDescription,_AG:swInventoryHWIndex,_AH:swInventoryData,'stats':stats,'generalStats':generalStats,'genCountTable':genCountTable,'genCountEntry':genCountEntry,_Y:genCountIndex,_AI:genCountType,_AJ:genCountUnits,_AK:genCountValue,'paperStats':paperStats,'paperGeneralCountTable':paperGeneralCountTable,'paperGeneralCountEntry':paperGeneralCountEntry,_Z:paperGeneralCountIndex,_AL:paperGeneralCountType,_AM:paperGeneralCountUnits,_AN:paperGeneralCountValue,'paperSidesCountTable':paperSidesCountTable,'paperSidesCountEntry':paperSidesCountEntry,_a:paperSidesCountIndex,_AO:paperSidesPaperSize,_AP:paperSidesPaperType,_AQ:paperSidesMonoPicked,_AR:paperSidesColorPicked,_AS:paperSidesMonoSafe,_AT:paperSidesColorSafe,'paperSheetsCountTable':paperSheetsCountTable,'paperSheetsCountEntry':paperSheetsCountEntry,_b:paperSheetsCountIndex,_AU:paperSheetsPaperSize,_AV:paperSheetsPaperType,_AW:paperSheetsPicked,_AX:paperSheetsSafe,'paperNupCountTable':paperNupCountTable,'paperNupCountEntry':paperNupCountEntry,_c:paperNupCountIndex,_AY:paperNupNumber,_AZ:paperNupSides,_Aa:paperNupLogicalSides,'paperJobSizeTable':paperJobSizeTable,'paperJobSizeEntry':paperJobSizeEntry,_d:paperJobSizeIndex,_Ab:paperJobSizeMinimum,_Ac:paperJobSizeMaximum,_Ad:paperJobSizeSideCount,_Ae:paperJobSizeJobCount,'scanStats':scanStats,'scanCountTable':scanCountTable,'scanCountEntry':scanCountEntry,_e:scanCountIndex,_Af:scanCountType,_Ag:scanCountSize,_Ah:scanCountSides,_Ai:scanCountSheets,'supplyStats':supplyStats,'currentSuppliesTable':currentSuppliesTable,'currentSuppliesEntry':currentSuppliesEntry,_f:currentSupplyIndex,_Aj:currentSupplyInventoryIndex,_Ak:currentSupplyType,_Al:currentSupplyColorantValue,_Au:currentSupplyDescription,_Am:currentSupplySerialNumber,_An:currentSupplyPartNumber,_Ar:currentSupplyClass,_As:currentSupplyCartridgeType,_At:currentSupplyInstallDate,_Ap:currentSupplyPageCountAtInstall,_Aw:currentSupplyCurrentStatus,_Aq:currentSupplyCapacityUnit,_Ao:currentSupplyCapacity,_A_:currentSupplyFirstKnownLevel,_Av:currentSupplyCurrentLevel,_Ax:currentSupplyUsage,_Az:currentSupplyCalibrations,_Ay:currentSupplyCoverage,'currentSupplyDaysRemaining':currentSupplyDaysRemaining,'supplyHistoryTable':supplyHistoryTable,'supplyHistoryEntry':supplyHistoryEntry,_g:supplyHistoryIndex,_B0:supplyHistoryInventoryIndex,_B1:supplyHistorySupplyType,_B2:supplyHistoryColorantValue,_B3:supplyHistoryDescription,_B4:supplyHistorySerialNumber,_B5:supplyHistoryCartridgeType,_B6:supplyHistoryInstallDate,_B7:supplyHistoryPageCount,_B8:supplyHistoryCapacityUnit,_B9:supplyHistoryCapacity,_BA:supplyHistoryLastLevel,_BB:supplyHistoryUsage,_BC:supplyHistoryCalibrations,_BD:supplyHistoryCoverage,'supplyHistogramTable':supplyHistogramTable,'supplyHistogramEntry':supplyHistogramEntry,_h:supplyHistogramIndex,_BE:supplyHistogramInventoryIndex,_BF:supplyHistogramSupplyType,_BG:supplyHistogramColorantValue,_BH:supplyHistogramDescription,_BI:supplyHistogramCapacityUnit,_BJ:supplyHistogramCapacity,_BK:supplyHistogramCount,_BL:supplyHistogramCountUnits,'supplyHistogramWithHistoryTable':supplyHistogramWithHistoryTable,'supplyHistogramHistoryEntry':supplyHistogramHistoryEntry,_i:supplyHistogramHistoryIndex,'supplyHistogramHistoryInventoryIndex':supplyHistogramHistoryInventoryIndex,_j:supplyHistogramHistoryCountIndex,'supplyHistogramHistorySupplyType':supplyHistogramHistorySupplyType,'supplyHistogramHistoryColorantValue':supplyHistogramHistoryColorantValue,'supplyHistogramHistoryDescription':supplyHistogramHistoryDescription,'supplyHistogramHistoryCapacityUnit':supplyHistogramHistoryCapacityUnit,'supplyHistogramHistoryCapacity':supplyHistogramHistoryCapacity,'supplyHistogramHistoryCount':supplyHistogramHistoryCount,'supplyHistogramHistoryCountUnits':supplyHistogramHistoryCountUnits,'alerts':alerts,'deviceAlertTable':deviceAlertTable,'deviceAlertEntry':deviceAlertEntry,_J:deviceAlertIndex,_L:deviceAlertConfigTableNode,_M:deviceAlertConfigTableIndex,_N:deviceAlertSeverity,_O:deviceAlertCode,_P:deviceAlertDescription,_Q:deviceAlertData,_R:deviceAlertTime,'deviceAlertSeverityLevel':deviceAlertSeverityLevel,'deviceAlertTrainingLevel':deviceAlertTrainingLevel,'deviceAlertPrtCode':deviceAlertPrtCode,'deviceV1AlertMPS':deviceV1AlertMPS,'deviceV2AlertMPSPrefix':deviceV2AlertMPSPrefix,'deviceV2AlertMPS':deviceV2AlertMPS,'logs':logs,'applications':applications,'outputfeature':outputfeature,'outputOptionFeatureTable':outputOptionFeatureTable,'outputOptionEntry':outputOptionEntry,_n:outputOptionIndex,'outputOptionName':outputOptionName,'outputLevelSensing':outputLevelSensing,'outputOffsetting':outputOffsetting,'outputFoldSupport':outputFoldSupport,'outputfaceOrientation':outputfaceOrientation,'outputBindingCapable':outputBindingCapable,'outputSeparationCapable':outputSeparationCapable,'outputStitchingCapable':outputStitchingCapable,'outputPunchingCapable':outputPunchingCapable})