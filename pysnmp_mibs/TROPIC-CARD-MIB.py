_Ax='tnCardPrbsTestIdTableGroup'
_Aw='tnCardAssemblyTableGroup'
_Av='tnCardTableGroup'
_Au='tnCardScalarsGroup'
_At='tnCardPrbsTestIdOidList'
_As='tnCardAssemblyMarketingPartNumber'
_Ar='tnCardAssemblyManufacturingPartNumber'
_Aq='tnCardAssemblySerialNumber'
_Ap='tnCardAssemblyHFD'
_Ao='tnCardAssemblyCLEI'
_An='tnCardAssemblyName'
_Am='tnCardTargetAddPortInputPower'
_Al='tnCardMgracd'
_Ak='tnCardSapLoopbackMacAddr'
_Aj='tnCardLOLCKDetectionEnable'
_Ai='tnCardAddPowerMode'
_Ah='tnCardAseMode'
_Ag='tnCardMainDeviceTemperature'
_Af='tnCardCpuTemperature'
_Ae='tnCardShutdownCmd'
_Ad='tnCardClkSelectedValue'
_Ac='tnCardSlotClkStatus'
_Ab='tnCardOAMTestUnit'
_Aa='tnCardVirtual'
_AZ='tnCardInitConfProfile'
_AY='tnCardLineMode'
_AX='tnCardLicenseRestricted'
_AW='tnCardModuleCfg'
_AV='tnCardTransportModeOSC'
_AU='tnCardTotalRam'
_AT='tnCardIntWrkMode'
_AS='tnCardL1andL2Decoupled'
_AR='tnCardRpmRead'
_AQ='tnCardAmbientTemp'
_AP='tnCardTestHdNoServPort'
_AO='tnCardDNRLEDColor'
_AN='tnCardMirrorLoopbackNoServPort'
_AM='tnCardLicenseRmaKey'
_AL='tnCardLicenseTimeStamp'
_AK='tnCardLicenseCap2Val'
_AJ='tnCardLicenseCap1Val'
_AI='tnCardLicenseAction'
_AH='tnCardLicenseData'
_AG='tnCardAlmProfEnvName'
_AF='tnCardAlmProfName'
_AE='tnCardLoopbackNoServPort'
_AD='tnCardUplinkAdminMode'
_AC='tnCardCurrent'
_AB='tnCardPower'
_AA='tnCardWtClkMeasureValues'
_A9='tnCardRtrvClkSwitch'
_A8='tnCardClkSwitch'
_A7='tnCardEthOamCcmFaultMgntMode'
_A6='tnCardMaxPower'
_A5='tnCardLACPSystemPriority'
_A4='tnCardCapacity'
_A3='tnCardFactoryID'
_A2='tnCardNextFwBundleVer'
_A1='tnCardLastBootedFwBundleVer'
_A0='tnCardAnyPortsInService'
_z='tnCardExtraData'
_y='tnCardDate'
_x='tnCardSWPartNum'
_w='tnCardMnemonic'
_v='tnCardCompanyID'
_u='tnCardActivityLEDState'
_t='tnCardActivityLEDColor'
_s='tnCardStatusLEDState'
_r='tnCardStatusLEDColor'
_q='tnCardTemperatureTolerance'
_p='tnCardLowTemperatureThresh'
_o='tnCardHighTemperatureThresh'
_n='tnCardTemperature'
_m='tnCardWidth'
_l='tnCardHeight'
_k='tnCardSWGenericLoadName'
_j='tnCardMarketingPartNumber'
_i='tnCardManufacturingPartNumber'
_h='tnCardSerialNumber'
_g='tnCardHFD'
_f='tnCardCLEI'
_e='tnCardDescr'
_d='tnCardName'
_c='tnCardTotal'
_b='tnCardAssemblyIndex'
_a='standard'
_Z='milli-Watts'
_Y='TropicCardSerialNumber'
_X='TropicCardSWGenericLoadName'
_W='TropicCardMarketingPartNumber'
_V='TropicCardManufacturingPartNumber'
_U='TropicCardHFD'
_T='TropicCardCLEI'
_S='AluWdmWtClkValues'
_R='AluWdmCardCapacity'
_Q='MacAddress'
_P='TruthValue'
_O='InterfaceIndexOrZero'
_N='OctetString'
_M='unknown'
_L='tnSlotIndex'
_K='TROPIC-SLOT-MIB'
_J='tnShelfIndex'
_I='TROPIC-SHELF-MIB'
_H='Celsius'
_G='Unsigned32'
_F='SnmpAdminString'
_E='Integer32'
_D='read-create'
_C='read-only'
_B='TROPIC-CARD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB',_O)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString',_Q,'PhysAddress','TextualConvention',_P)
tnCardMIB,tnCardModules=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnCardMIB','tnCardModules')
tnShelfIndex,=mibBuilder.importSymbols(_I,_J)
tnSlotIndex,=mibBuilder.importSymbols(_K,_L)
AluWdmCardCapacity,AluWdmWtClkValues,TropicCardCLEI,TropicCardHFD,TropicCardManufacturingPartNumber,TropicCardMarketingPartNumber,TropicCardSWGenericLoadName,TropicCardSerialNumber,TropicLEDColorType,TropicLEDStateType=mibBuilder.importSymbols('TROPIC-TC',_R,_S,_T,_U,_V,_W,_X,_Y,'TropicLEDColorType','TropicLEDStateType')
tnCardMibModule=ModuleIdentity((1,3,6,1,4,1,7483,1,1,2,2,3,1))
if mibBuilder.loadTexts:tnCardMibModule.setRevisions(('2021-06-18 12:00','2021-03-19 12:00','2020-12-18 12:00','2020-12-04 12:00','2020-11-13 12:00','2020-09-11 12:00','2020-06-19 12:00','2020-06-12 12:00','2020-03-20 12:00','2020-02-21 12:00','2020-02-14 12:00','2019-12-13 12:00','2019-10-25 12:00','2019-10-18 12:00','2019-08-30 12:00','2019-07-12 12:00','2019-06-07 12:00','2019-03-22 12:00','2019-02-22 12:00','2019-01-25 12:00','2018-05-18 12:00','2018-03-09 12:00','2018-02-23 12:00','2017-12-26 12:00','2017-09-15 12:00','2017-05-26 12:00','2017-04-28 12:00','2017-03-31 12:00','2017-02-24 12:00','2017-02-10 12:00','2016-11-16 12:00','2016-09-09 12:00','2016-08-08 12:00','2016-07-29 12:00','2015-10-05 12:00','2015-09-30 12:00','2015-07-30 12:00','2015-05-29 12:00','2015-03-11 12:00','2015-02-06 12:00','2014-02-26 12:00','2013-12-26 12:00','2013-12-15 12:00','2013-11-18 12:00','2013-08-16 12:00','2013-05-21 12:00','2012-09-06 12:00','2012-07-17 12:00','2012-07-10 12:00','2011-05-23 12:00','2011-05-19 12:00','2009-03-31 12:00','2009-02-10 12:00','2009-02-01 12:00','2008-09-26 12:00','2008-09-24 12:00','2008-09-19 12:00','2008-06-05 12:00','2008-05-29 12:00','2008-04-11 12:00'))
class NokiaOAMTestUnitType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('microseconds',1),('hundred-nano-seconds',2),('nano-seconds',3)))
_TnCardConf_ObjectIdentity=ObjectIdentity
tnCardConf=_TnCardConf_ObjectIdentity((1,3,6,1,4,1,7483,2,2,3,1,1))
_TnCardGroups_ObjectIdentity=ObjectIdentity
tnCardGroups=_TnCardGroups_ObjectIdentity((1,3,6,1,4,1,7483,2,2,3,1,1,1))
_TnCardCompliances_ObjectIdentity=ObjectIdentity
tnCardCompliances=_TnCardCompliances_ObjectIdentity((1,3,6,1,4,1,7483,2,2,3,1,1,2))
_TnCardObjs_ObjectIdentity=ObjectIdentity
tnCardObjs=_TnCardObjs_ObjectIdentity((1,3,6,1,4,1,7483,2,2,3,1,2))
_TnCardBasics_ObjectIdentity=ObjectIdentity
tnCardBasics=_TnCardBasics_ObjectIdentity((1,3,6,1,4,1,7483,2,2,3,1,2,1))
_TnCardTotal_Type=Integer32
_TnCardTotal_Object=MibScalar
tnCardTotal=_TnCardTotal_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,1),_TnCardTotal_Type())
tnCardTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardTotal.setStatus(_A)
_TnCardTable_Object=MibTable
tnCardTable=_TnCardTable_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2))
if mibBuilder.loadTexts:tnCardTable.setStatus(_A)
_TnCardEntry_Object=MibTableRow
tnCardEntry=_TnCardEntry_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1))
tnCardEntry.setIndexNames((0,_I,_J),(0,_K,_L))
if mibBuilder.loadTexts:tnCardEntry.setStatus(_A)
class _TnCardName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_TnCardName_Type.__name__=_F
_TnCardName_Object=MibTableColumn
tnCardName=_TnCardName_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,1),_TnCardName_Type())
tnCardName.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardName.setStatus(_A)
class _TnCardDescr_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TnCardDescr_Type.__name__=_F
_TnCardDescr_Object=MibTableColumn
tnCardDescr=_TnCardDescr_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,2),_TnCardDescr_Type())
tnCardDescr.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardDescr.setStatus(_A)
class _TnCardCLEI_Type(TropicCardCLEI):defaultValue=OctetString('')
_TnCardCLEI_Type.__name__=_T
_TnCardCLEI_Object=MibTableColumn
tnCardCLEI=_TnCardCLEI_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,3),_TnCardCLEI_Type())
tnCardCLEI.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardCLEI.setStatus(_A)
class _TnCardHFD_Type(TropicCardHFD):defaultValue=OctetString('')
_TnCardHFD_Type.__name__=_U
_TnCardHFD_Object=MibTableColumn
tnCardHFD=_TnCardHFD_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,4),_TnCardHFD_Type())
tnCardHFD.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardHFD.setStatus(_A)
class _TnCardSerialNumber_Type(TropicCardSerialNumber):defaultValue=OctetString('')
_TnCardSerialNumber_Type.__name__=_Y
_TnCardSerialNumber_Object=MibTableColumn
tnCardSerialNumber=_TnCardSerialNumber_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,5),_TnCardSerialNumber_Type())
tnCardSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardSerialNumber.setStatus(_A)
class _TnCardManufacturingPartNumber_Type(TropicCardManufacturingPartNumber):defaultValue=OctetString('')
_TnCardManufacturingPartNumber_Type.__name__=_V
_TnCardManufacturingPartNumber_Object=MibTableColumn
tnCardManufacturingPartNumber=_TnCardManufacturingPartNumber_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,6),_TnCardManufacturingPartNumber_Type())
tnCardManufacturingPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardManufacturingPartNumber.setStatus(_A)
class _TnCardMarketingPartNumber_Type(TropicCardMarketingPartNumber):defaultValue=OctetString('')
_TnCardMarketingPartNumber_Type.__name__=_W
_TnCardMarketingPartNumber_Object=MibTableColumn
tnCardMarketingPartNumber=_TnCardMarketingPartNumber_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,7),_TnCardMarketingPartNumber_Type())
tnCardMarketingPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardMarketingPartNumber.setStatus(_A)
class _TnCardSWGenericLoadName_Type(TropicCardSWGenericLoadName):defaultValue=OctetString('')
_TnCardSWGenericLoadName_Type.__name__=_X
_TnCardSWGenericLoadName_Object=MibTableColumn
tnCardSWGenericLoadName=_TnCardSWGenericLoadName_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,8),_TnCardSWGenericLoadName_Type())
tnCardSWGenericLoadName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardSWGenericLoadName.setStatus(_A)
class _TnCardHeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),('halfHeight',2),('fullHeight',3),('extendedHeight',4)))
_TnCardHeight_Type.__name__=_E
_TnCardHeight_Object=MibTableColumn
tnCardHeight=_TnCardHeight_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,10),_TnCardHeight_Type())
tnCardHeight.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardHeight.setStatus(_A)
class _TnCardWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),('singleWidth',2),('doubleWidth',3),('tripleWidth',4)))
_TnCardWidth_Type.__name__=_E
_TnCardWidth_Object=MibTableColumn
tnCardWidth=_TnCardWidth_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,11),_TnCardWidth_Type())
tnCardWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardWidth.setStatus(_A)
_TnCardTemperature_Type=Integer32
_TnCardTemperature_Object=MibTableColumn
tnCardTemperature=_TnCardTemperature_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,13),_TnCardTemperature_Type())
tnCardTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardTemperature.setStatus(_A)
if mibBuilder.loadTexts:tnCardTemperature.setUnits(_H)
class _TnCardHighTemperatureThresh_Type(Integer32):defaultValue=90
_TnCardHighTemperatureThresh_Type.__name__=_E
_TnCardHighTemperatureThresh_Object=MibTableColumn
tnCardHighTemperatureThresh=_TnCardHighTemperatureThresh_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,14),_TnCardHighTemperatureThresh_Type())
tnCardHighTemperatureThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardHighTemperatureThresh.setStatus(_A)
if mibBuilder.loadTexts:tnCardHighTemperatureThresh.setUnits(_H)
class _TnCardLowTemperatureThresh_Type(Integer32):defaultValue=-5
_TnCardLowTemperatureThresh_Type.__name__=_E
_TnCardLowTemperatureThresh_Object=MibTableColumn
tnCardLowTemperatureThresh=_TnCardLowTemperatureThresh_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,15),_TnCardLowTemperatureThresh_Type())
tnCardLowTemperatureThresh.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardLowTemperatureThresh.setStatus(_A)
if mibBuilder.loadTexts:tnCardLowTemperatureThresh.setUnits(_H)
class _TnCardTemperatureTolerance_Type(Unsigned32):defaultValue=3
_TnCardTemperatureTolerance_Type.__name__=_G
_TnCardTemperatureTolerance_Object=MibTableColumn
tnCardTemperatureTolerance=_TnCardTemperatureTolerance_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,16),_TnCardTemperatureTolerance_Type())
tnCardTemperatureTolerance.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardTemperatureTolerance.setStatus(_A)
if mibBuilder.loadTexts:tnCardTemperatureTolerance.setUnits(_H)
_TnCardStatusLEDColor_Type=TropicLEDColorType
_TnCardStatusLEDColor_Object=MibTableColumn
tnCardStatusLEDColor=_TnCardStatusLEDColor_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,17),_TnCardStatusLEDColor_Type())
tnCardStatusLEDColor.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardStatusLEDColor.setStatus(_A)
_TnCardStatusLEDState_Type=TropicLEDStateType
_TnCardStatusLEDState_Object=MibTableColumn
tnCardStatusLEDState=_TnCardStatusLEDState_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,18),_TnCardStatusLEDState_Type())
tnCardStatusLEDState.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardStatusLEDState.setStatus(_A)
_TnCardActivityLEDColor_Type=TropicLEDColorType
_TnCardActivityLEDColor_Object=MibTableColumn
tnCardActivityLEDColor=_TnCardActivityLEDColor_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,19),_TnCardActivityLEDColor_Type())
tnCardActivityLEDColor.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardActivityLEDColor.setStatus(_A)
_TnCardActivityLEDState_Type=TropicLEDStateType
_TnCardActivityLEDState_Object=MibTableColumn
tnCardActivityLEDState=_TnCardActivityLEDState_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,20),_TnCardActivityLEDState_Type())
tnCardActivityLEDState.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardActivityLEDState.setStatus(_A)
class _TnCardCompanyID_Type(SnmpAdminString):defaultValue=OctetString('')
_TnCardCompanyID_Type.__name__=_F
_TnCardCompanyID_Object=MibTableColumn
tnCardCompanyID=_TnCardCompanyID_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,21),_TnCardCompanyID_Type())
tnCardCompanyID.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardCompanyID.setStatus(_A)
class _TnCardMnemonic_Type(SnmpAdminString):defaultValue=OctetString('')
_TnCardMnemonic_Type.__name__=_F
_TnCardMnemonic_Object=MibTableColumn
tnCardMnemonic=_TnCardMnemonic_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,22),_TnCardMnemonic_Type())
tnCardMnemonic.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardMnemonic.setStatus(_A)
class _TnCardSWPartNum_Type(SnmpAdminString):defaultValue=OctetString('')
_TnCardSWPartNum_Type.__name__=_F
_TnCardSWPartNum_Object=MibTableColumn
tnCardSWPartNum=_TnCardSWPartNum_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,23),_TnCardSWPartNum_Type())
tnCardSWPartNum.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardSWPartNum.setStatus(_A)
class _TnCardDate_Type(SnmpAdminString):defaultValue=OctetString('')
_TnCardDate_Type.__name__=_F
_TnCardDate_Object=MibTableColumn
tnCardDate=_TnCardDate_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,24),_TnCardDate_Type())
tnCardDate.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardDate.setStatus(_A)
class _TnCardExtraData_Type(SnmpAdminString):defaultValue=OctetString('')
_TnCardExtraData_Type.__name__=_F
_TnCardExtraData_Object=MibTableColumn
tnCardExtraData=_TnCardExtraData_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,25),_TnCardExtraData_Type())
tnCardExtraData.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardExtraData.setStatus(_A)
_TnCardAnyPortsInService_Type=TruthValue
_TnCardAnyPortsInService_Object=MibTableColumn
tnCardAnyPortsInService=_TnCardAnyPortsInService_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,27),_TnCardAnyPortsInService_Type())
tnCardAnyPortsInService.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardAnyPortsInService.setStatus(_A)
class _TnCardLastBootedFwBundleVer_Type(SnmpAdminString):defaultValue=OctetString('')
_TnCardLastBootedFwBundleVer_Type.__name__=_F
_TnCardLastBootedFwBundleVer_Object=MibTableColumn
tnCardLastBootedFwBundleVer=_TnCardLastBootedFwBundleVer_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,28),_TnCardLastBootedFwBundleVer_Type())
tnCardLastBootedFwBundleVer.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardLastBootedFwBundleVer.setStatus(_A)
class _TnCardNextFwBundleVer_Type(SnmpAdminString):defaultValue=OctetString('')
_TnCardNextFwBundleVer_Type.__name__=_F
_TnCardNextFwBundleVer_Object=MibTableColumn
tnCardNextFwBundleVer=_TnCardNextFwBundleVer_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,29),_TnCardNextFwBundleVer_Type())
tnCardNextFwBundleVer.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardNextFwBundleVer.setStatus(_A)
class _TnCardFactoryID_Type(SnmpAdminString):defaultValue=OctetString('')
_TnCardFactoryID_Type.__name__=_F
_TnCardFactoryID_Object=MibTableColumn
tnCardFactoryID=_TnCardFactoryID_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,30),_TnCardFactoryID_Type())
tnCardFactoryID.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardFactoryID.setStatus(_A)
class _TnCardCapacity_Type(AluWdmCardCapacity):defaultValue=1
_TnCardCapacity_Type.__name__=_R
_TnCardCapacity_Object=MibTableColumn
tnCardCapacity=_TnCardCapacity_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,31),_TnCardCapacity_Type())
tnCardCapacity.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardCapacity.setStatus(_A)
class _TnCardLACPSystemPriority_Type(Unsigned32):defaultValue=32768;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TnCardLACPSystemPriority_Type.__name__=_G
_TnCardLACPSystemPriority_Object=MibTableColumn
tnCardLACPSystemPriority=_TnCardLACPSystemPriority_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,32),_TnCardLACPSystemPriority_Type())
tnCardLACPSystemPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardLACPSystemPriority.setStatus(_A)
_TnCardMaxPower_Type=Unsigned32
_TnCardMaxPower_Object=MibTableColumn
tnCardMaxPower=_TnCardMaxPower_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,33),_TnCardMaxPower_Type())
tnCardMaxPower.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardMaxPower.setStatus(_A)
if mibBuilder.loadTexts:tnCardMaxPower.setUnits(_Z)
class _TnCardEthOamCcmFaultMgntMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ieee',1),('itu',2)))
_TnCardEthOamCcmFaultMgntMode_Type.__name__=_E
_TnCardEthOamCcmFaultMgntMode_Object=MibTableColumn
tnCardEthOamCcmFaultMgntMode=_TnCardEthOamCcmFaultMgntMode_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,34),_TnCardEthOamCcmFaultMgntMode_Type())
tnCardEthOamCcmFaultMgntMode.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardEthOamCcmFaultMgntMode.setStatus(_A)
class _TnCardClkSwitch_Type(AluWdmWtClkValues):defaultValue=1
_TnCardClkSwitch_Type.__name__=_S
_TnCardClkSwitch_Object=MibTableColumn
tnCardClkSwitch=_TnCardClkSwitch_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,35),_TnCardClkSwitch_Type())
tnCardClkSwitch.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardClkSwitch.setStatus(_A)
_TnCardRtrvClkSwitch_Type=AluWdmWtClkValues
_TnCardRtrvClkSwitch_Object=MibTableColumn
tnCardRtrvClkSwitch=_TnCardRtrvClkSwitch_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,36),_TnCardRtrvClkSwitch_Type())
tnCardRtrvClkSwitch.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardRtrvClkSwitch.setStatus(_A)
class _TnCardWtClkMeasureValues_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_TnCardWtClkMeasureValues_Type.__name__=_N
_TnCardWtClkMeasureValues_Object=MibTableColumn
tnCardWtClkMeasureValues=_TnCardWtClkMeasureValues_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,37),_TnCardWtClkMeasureValues_Type())
tnCardWtClkMeasureValues.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardWtClkMeasureValues.setStatus(_A)
_TnCardPower_Type=Integer32
_TnCardPower_Object=MibTableColumn
tnCardPower=_TnCardPower_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,38),_TnCardPower_Type())
tnCardPower.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardPower.setStatus(_A)
if mibBuilder.loadTexts:tnCardPower.setUnits(_Z)
_TnCardCurrent_Type=Unsigned32
_TnCardCurrent_Object=MibTableColumn
tnCardCurrent=_TnCardCurrent_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,39),_TnCardCurrent_Type())
tnCardCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardCurrent.setStatus(_A)
if mibBuilder.loadTexts:tnCardCurrent.setUnits('milli-Amperes')
class _TnCardUplinkAdminMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('unassigned',0),('network',1),('accessUplink',2)))
_TnCardUplinkAdminMode_Type.__name__=_E
_TnCardUplinkAdminMode_Object=MibTableColumn
tnCardUplinkAdminMode=_TnCardUplinkAdminMode_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,40),_TnCardUplinkAdminMode_Type())
tnCardUplinkAdminMode.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardUplinkAdminMode.setStatus(_A)
class _TnCardLoopbackNoServPort_Type(InterfaceIndexOrZero):defaultValue=0
_TnCardLoopbackNoServPort_Type.__name__=_O
_TnCardLoopbackNoServPort_Object=MibTableColumn
tnCardLoopbackNoServPort=_TnCardLoopbackNoServPort_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,41),_TnCardLoopbackNoServPort_Type())
tnCardLoopbackNoServPort.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardLoopbackNoServPort.setStatus(_A)
class _TnCardAlmProfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_TnCardAlmProfName_Type.__name__=_N
_TnCardAlmProfName_Object=MibTableColumn
tnCardAlmProfName=_TnCardAlmProfName_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,42),_TnCardAlmProfName_Type())
tnCardAlmProfName.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardAlmProfName.setStatus(_A)
class _TnCardAlmProfEnvName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,40))
_TnCardAlmProfEnvName_Type.__name__=_N
_TnCardAlmProfEnvName_Object=MibTableColumn
tnCardAlmProfEnvName=_TnCardAlmProfEnvName_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,43),_TnCardAlmProfEnvName_Type())
tnCardAlmProfEnvName.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardAlmProfEnvName.setStatus(_A)
class _TnCardLicenseData_Type(SnmpAdminString):defaultValue=OctetString('')
_TnCardLicenseData_Type.__name__=_F
_TnCardLicenseData_Object=MibTableColumn
tnCardLicenseData=_TnCardLicenseData_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,44),_TnCardLicenseData_Type())
tnCardLicenseData.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardLicenseData.setStatus(_A)
class _TnCardLicenseAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('apply',2),('delete',3)))
_TnCardLicenseAction_Type.__name__=_E
_TnCardLicenseAction_Object=MibTableColumn
tnCardLicenseAction=_TnCardLicenseAction_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,45),_TnCardLicenseAction_Type())
tnCardLicenseAction.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardLicenseAction.setStatus(_A)
class _TnCardLicenseCap1Val_Type(Unsigned32):defaultValue=0
_TnCardLicenseCap1Val_Type.__name__=_G
_TnCardLicenseCap1Val_Object=MibTableColumn
tnCardLicenseCap1Val=_TnCardLicenseCap1Val_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,46),_TnCardLicenseCap1Val_Type())
tnCardLicenseCap1Val.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardLicenseCap1Val.setStatus(_A)
class _TnCardLicenseCap2Val_Type(Unsigned32):defaultValue=0
_TnCardLicenseCap2Val_Type.__name__=_G
_TnCardLicenseCap2Val_Object=MibTableColumn
tnCardLicenseCap2Val=_TnCardLicenseCap2Val_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,47),_TnCardLicenseCap2Val_Type())
tnCardLicenseCap2Val.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardLicenseCap2Val.setStatus(_A)
class _TnCardLicenseTimeStamp_Type(Unsigned32):defaultValue=0
_TnCardLicenseTimeStamp_Type.__name__=_G
_TnCardLicenseTimeStamp_Object=MibTableColumn
tnCardLicenseTimeStamp=_TnCardLicenseTimeStamp_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,48),_TnCardLicenseTimeStamp_Type())
tnCardLicenseTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardLicenseTimeStamp.setStatus(_A)
class _TnCardLicenseRmaKey_Type(SnmpAdminString):defaultValue=OctetString('')
_TnCardLicenseRmaKey_Type.__name__=_F
_TnCardLicenseRmaKey_Object=MibTableColumn
tnCardLicenseRmaKey=_TnCardLicenseRmaKey_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,49),_TnCardLicenseRmaKey_Type())
tnCardLicenseRmaKey.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardLicenseRmaKey.setStatus(_A)
class _TnCardMirrorLoopbackNoServPort_Type(InterfaceIndexOrZero):defaultValue=0
_TnCardMirrorLoopbackNoServPort_Type.__name__=_O
_TnCardMirrorLoopbackNoServPort_Object=MibTableColumn
tnCardMirrorLoopbackNoServPort=_TnCardMirrorLoopbackNoServPort_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,50),_TnCardMirrorLoopbackNoServPort_Type())
tnCardMirrorLoopbackNoServPort.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardMirrorLoopbackNoServPort.setStatus(_A)
class _TnCardDNRLEDColor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('orange',2)))
_TnCardDNRLEDColor_Type.__name__=_E
_TnCardDNRLEDColor_Object=MibTableColumn
tnCardDNRLEDColor=_TnCardDNRLEDColor_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,51),_TnCardDNRLEDColor_Type())
tnCardDNRLEDColor.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardDNRLEDColor.setStatus(_A)
class _TnCardTestHdNoServPort_Type(InterfaceIndexOrZero):defaultValue=0
_TnCardTestHdNoServPort_Type.__name__=_O
_TnCardTestHdNoServPort_Object=MibTableColumn
tnCardTestHdNoServPort=_TnCardTestHdNoServPort_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,52),_TnCardTestHdNoServPort_Type())
tnCardTestHdNoServPort.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardTestHdNoServPort.setStatus(_A)
_TnCardAmbientTemp_Type=Integer32
_TnCardAmbientTemp_Object=MibTableColumn
tnCardAmbientTemp=_TnCardAmbientTemp_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,53),_TnCardAmbientTemp_Type())
tnCardAmbientTemp.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardAmbientTemp.setStatus(_A)
if mibBuilder.loadTexts:tnCardAmbientTemp.setUnits(_H)
_TnCardRpmRead_Type=Integer32
_TnCardRpmRead_Object=MibTableColumn
tnCardRpmRead=_TnCardRpmRead_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,54),_TnCardRpmRead_Type())
tnCardRpmRead.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardRpmRead.setStatus(_A)
class _TnCardL1andL2Decoupled_Type(TruthValue):defaultValue=1
_TnCardL1andL2Decoupled_Type.__name__=_P
_TnCardL1andL2Decoupled_Object=MibTableColumn
tnCardL1andL2Decoupled=_TnCardL1andL2Decoupled_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,55),_TnCardL1andL2Decoupled_Type())
tnCardL1andL2Decoupled.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardL1andL2Decoupled.setStatus(_A)
class _TnCardIntWrkMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('legacy',1),(_a,2)))
_TnCardIntWrkMode_Type.__name__=_E
_TnCardIntWrkMode_Object=MibTableColumn
tnCardIntWrkMode=_TnCardIntWrkMode_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,56),_TnCardIntWrkMode_Type())
tnCardIntWrkMode.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardIntWrkMode.setStatus(_A)
_TnCardTotalRam_Type=Unsigned32
_TnCardTotalRam_Object=MibTableColumn
tnCardTotalRam=_TnCardTotalRam_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,57),_TnCardTotalRam_Type())
tnCardTotalRam.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardTotalRam.setStatus(_A)
class _TnCardTransportModeOSC_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('layer2',1),('layer3',2)))
_TnCardTransportModeOSC_Type.__name__=_E
_TnCardTransportModeOSC_Object=MibTableColumn
tnCardTransportModeOSC=_TnCardTransportModeOSC_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,58),_TnCardTransportModeOSC_Type())
tnCardTransportModeOSC.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardTransportModeOSC.setStatus(_A)
class _TnCardModuleCfg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('plugLimit40',1),('plugLimit32',2),('plugLimit20',3),('elplugs',4),('thirtyPlugs',5),('twelvePlugs',6),('ninePlugs',7)))
_TnCardModuleCfg_Type.__name__=_E
_TnCardModuleCfg_Object=MibTableColumn
tnCardModuleCfg=_TnCardModuleCfg_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,59),_TnCardModuleCfg_Type())
tnCardModuleCfg.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardModuleCfg.setStatus(_A)
_TnCardLicenseRestricted_Type=TruthValue
_TnCardLicenseRestricted_Object=MibTableColumn
tnCardLicenseRestricted=_TnCardLicenseRestricted_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,60),_TnCardLicenseRestricted_Type())
tnCardLicenseRestricted.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardLicenseRestricted.setStatus(_A)
class _TnCardLineMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notApplicable',1),('fixed',2),('dynamic',3)))
_TnCardLineMode_Type.__name__=_E
_TnCardLineMode_Object=MibTableColumn
tnCardLineMode=_TnCardLineMode_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,61),_TnCardLineMode_Type())
tnCardLineMode.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardLineMode.setStatus(_A)
class _TnCardInitConfProfile_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_TnCardInitConfProfile_Type.__name__=_G
_TnCardInitConfProfile_Object=MibTableColumn
tnCardInitConfProfile=_TnCardInitConfProfile_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,62),_TnCardInitConfProfile_Type())
tnCardInitConfProfile.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardInitConfProfile.setStatus(_A)
_TnCardVirtual_Type=TruthValue
_TnCardVirtual_Object=MibTableColumn
tnCardVirtual=_TnCardVirtual_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,63),_TnCardVirtual_Type())
tnCardVirtual.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardVirtual.setStatus(_A)
_TnCardOAMTestUnit_Type=NokiaOAMTestUnitType
_TnCardOAMTestUnit_Object=MibTableColumn
tnCardOAMTestUnit=_TnCardOAMTestUnit_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,64),_TnCardOAMTestUnit_Type())
tnCardOAMTestUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardOAMTestUnit.setStatus(_A)
class _TnCardSlotClkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('onFreq',2),('fail',3)))
_TnCardSlotClkStatus_Type.__name__=_E
_TnCardSlotClkStatus_Object=MibTableColumn
tnCardSlotClkStatus=_TnCardSlotClkStatus_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,65),_TnCardSlotClkStatus_Type())
tnCardSlotClkStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardSlotClkStatus.setStatus(_A)
class _TnCardClkSelectedValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_M,1),('yes',2),('no',3)))
_TnCardClkSelectedValue_Type.__name__=_E
_TnCardClkSelectedValue_Object=MibTableColumn
tnCardClkSelectedValue=_TnCardClkSelectedValue_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,66),_TnCardClkSelectedValue_Type())
tnCardClkSelectedValue.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardClkSelectedValue.setStatus(_A)
class _TnCardShutdownCmd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('shutdownForce',2)))
_TnCardShutdownCmd_Type.__name__=_E
_TnCardShutdownCmd_Object=MibTableColumn
tnCardShutdownCmd=_TnCardShutdownCmd_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,67),_TnCardShutdownCmd_Type())
tnCardShutdownCmd.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardShutdownCmd.setStatus(_A)
_TnCardCpuTemperature_Type=Integer32
_TnCardCpuTemperature_Object=MibTableColumn
tnCardCpuTemperature=_TnCardCpuTemperature_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,68),_TnCardCpuTemperature_Type())
tnCardCpuTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardCpuTemperature.setStatus(_A)
if mibBuilder.loadTexts:tnCardCpuTemperature.setUnits(_H)
_TnCardMainDeviceTemperature_Type=Integer32
_TnCardMainDeviceTemperature_Object=MibTableColumn
tnCardMainDeviceTemperature=_TnCardMainDeviceTemperature_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,69),_TnCardMainDeviceTemperature_Type())
tnCardMainDeviceTemperature.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardMainDeviceTemperature.setStatus(_A)
if mibBuilder.loadTexts:tnCardMainDeviceTemperature.setUnits(_H)
class _TnCardAseMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unconfigured',1),('noNoise',2),('low',3),(_a,4)))
_TnCardAseMode_Type.__name__=_E
_TnCardAseMode_Object=MibTableColumn
tnCardAseMode=_TnCardAseMode_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,70),_TnCardAseMode_Type())
tnCardAseMode.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardAseMode.setStatus(_A)
class _TnCardAddPowerMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('low',1),('high',2)))
_TnCardAddPowerMode_Type.__name__=_E
_TnCardAddPowerMode_Object=MibTableColumn
tnCardAddPowerMode=_TnCardAddPowerMode_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,71),_TnCardAddPowerMode_Type())
tnCardAddPowerMode.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardAddPowerMode.setStatus(_A)
class _TnCardLOLCKDetectionEnable_Type(TruthValue):defaultValue=2
_TnCardLOLCKDetectionEnable_Type.__name__=_P
_TnCardLOLCKDetectionEnable_Object=MibTableColumn
tnCardLOLCKDetectionEnable=_TnCardLOLCKDetectionEnable_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,72),_TnCardLOLCKDetectionEnable_Type())
tnCardLOLCKDetectionEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardLOLCKDetectionEnable.setStatus(_A)
class _TnCardSapLoopbackMacAddr_Type(MacAddress):defaultHexValue='000000000000'
_TnCardSapLoopbackMacAddr_Type.__name__=_Q
_TnCardSapLoopbackMacAddr_Object=MibTableColumn
tnCardSapLoopbackMacAddr=_TnCardSapLoopbackMacAddr_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,73),_TnCardSapLoopbackMacAddr_Type())
tnCardSapLoopbackMacAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardSapLoopbackMacAddr.setStatus(_A)
class _TnCardMgracd_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('cp',2),('mgnpln',3),('cpmgnpln',4)))
_TnCardMgracd_Type.__name__=_E
_TnCardMgracd_Object=MibTableColumn
tnCardMgracd=_TnCardMgracd_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,74),_TnCardMgracd_Type())
tnCardMgracd.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardMgracd.setStatus(_A)
_TnCardTargetAddPortInputPower_Type=Integer32
_TnCardTargetAddPortInputPower_Object=MibTableColumn
tnCardTargetAddPortInputPower=_TnCardTargetAddPortInputPower_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,2,1,75),_TnCardTargetAddPortInputPower_Type())
tnCardTargetAddPortInputPower.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardTargetAddPortInputPower.setStatus(_A)
if mibBuilder.loadTexts:tnCardTargetAddPortInputPower.setUnits('mBm')
_TnCardAssemblyTable_Object=MibTable
tnCardAssemblyTable=_TnCardAssemblyTable_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,3))
if mibBuilder.loadTexts:tnCardAssemblyTable.setStatus(_A)
_TnCardAssemblyEntry_Object=MibTableRow
tnCardAssemblyEntry=_TnCardAssemblyEntry_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,3,1))
tnCardAssemblyEntry.setIndexNames((0,_I,_J),(0,_K,_L),(0,_B,_b))
if mibBuilder.loadTexts:tnCardAssemblyEntry.setStatus(_A)
class _TnCardAssemblyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_TnCardAssemblyIndex_Type.__name__=_E
_TnCardAssemblyIndex_Object=MibTableColumn
tnCardAssemblyIndex=_TnCardAssemblyIndex_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,3,1,1),_TnCardAssemblyIndex_Type())
tnCardAssemblyIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:tnCardAssemblyIndex.setStatus(_A)
class _TnCardAssemblyName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,31))
_TnCardAssemblyName_Type.__name__=_F
_TnCardAssemblyName_Object=MibTableColumn
tnCardAssemblyName=_TnCardAssemblyName_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,3,1,2),_TnCardAssemblyName_Type())
tnCardAssemblyName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardAssemblyName.setStatus(_A)
_TnCardAssemblyCLEI_Type=TropicCardCLEI
_TnCardAssemblyCLEI_Object=MibTableColumn
tnCardAssemblyCLEI=_TnCardAssemblyCLEI_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,3,1,3),_TnCardAssemblyCLEI_Type())
tnCardAssemblyCLEI.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardAssemblyCLEI.setStatus(_A)
_TnCardAssemblyHFD_Type=TropicCardHFD
_TnCardAssemblyHFD_Object=MibTableColumn
tnCardAssemblyHFD=_TnCardAssemblyHFD_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,3,1,4),_TnCardAssemblyHFD_Type())
tnCardAssemblyHFD.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardAssemblyHFD.setStatus(_A)
_TnCardAssemblySerialNumber_Type=TropicCardSerialNumber
_TnCardAssemblySerialNumber_Object=MibTableColumn
tnCardAssemblySerialNumber=_TnCardAssemblySerialNumber_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,3,1,5),_TnCardAssemblySerialNumber_Type())
tnCardAssemblySerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardAssemblySerialNumber.setStatus(_A)
_TnCardAssemblyManufacturingPartNumber_Type=TropicCardManufacturingPartNumber
_TnCardAssemblyManufacturingPartNumber_Object=MibTableColumn
tnCardAssemblyManufacturingPartNumber=_TnCardAssemblyManufacturingPartNumber_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,3,1,6),_TnCardAssemblyManufacturingPartNumber_Type())
tnCardAssemblyManufacturingPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardAssemblyManufacturingPartNumber.setStatus(_A)
_TnCardAssemblyMarketingPartNumber_Type=TropicCardMarketingPartNumber
_TnCardAssemblyMarketingPartNumber_Object=MibTableColumn
tnCardAssemblyMarketingPartNumber=_TnCardAssemblyMarketingPartNumber_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,3,1,7),_TnCardAssemblyMarketingPartNumber_Type())
tnCardAssemblyMarketingPartNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardAssemblyMarketingPartNumber.setStatus(_A)
_TnCardDbSyncTable_Object=MibTable
tnCardDbSyncTable=_TnCardDbSyncTable_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,5))
if mibBuilder.loadTexts:tnCardDbSyncTable.setStatus(_A)
_TnCardDbSyncEntry_Object=MibTableRow
tnCardDbSyncEntry=_TnCardDbSyncEntry_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,5,1))
tnCardDbSyncEntry.setIndexNames((0,_I,_J),(0,_K,_L))
if mibBuilder.loadTexts:tnCardDbSyncEntry.setStatus(_A)
class _TnCardDBSyncEnabledByUser_Type(TruthValue):defaultValue=2
_TnCardDBSyncEnabledByUser_Type.__name__=_P
_TnCardDBSyncEnabledByUser_Object=MibTableColumn
tnCardDBSyncEnabledByUser=_TnCardDBSyncEnabledByUser_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,5,1,1),_TnCardDBSyncEnabledByUser_Type())
tnCardDBSyncEnabledByUser.setMaxAccess(_D)
if mibBuilder.loadTexts:tnCardDBSyncEnabledByUser.setStatus(_A)
_TnCardPrbsTestIdTable_Object=MibTable
tnCardPrbsTestIdTable=_TnCardPrbsTestIdTable_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,6))
if mibBuilder.loadTexts:tnCardPrbsTestIdTable.setStatus(_A)
_TnCardPrbsTestIdEntry_Object=MibTableRow
tnCardPrbsTestIdEntry=_TnCardPrbsTestIdEntry_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,6,1))
tnCardPrbsTestIdEntry.setIndexNames((0,_I,_J),(0,_K,_L))
if mibBuilder.loadTexts:tnCardPrbsTestIdEntry.setStatus(_A)
class _TnCardPrbsTestIdOidList_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,2048))
_TnCardPrbsTestIdOidList_Type.__name__=_F
_TnCardPrbsTestIdOidList_Object=MibTableColumn
tnCardPrbsTestIdOidList=_TnCardPrbsTestIdOidList_Object((1,3,6,1,4,1,7483,2,2,3,1,2,1,6,1,1),_TnCardPrbsTestIdOidList_Type())
tnCardPrbsTestIdOidList.setMaxAccess(_C)
if mibBuilder.loadTexts:tnCardPrbsTestIdOidList.setStatus(_A)
tnCardScalarsGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,3,1,1,1,1))
tnCardScalarsGroup.setObjects((_B,_c))
if mibBuilder.loadTexts:tnCardScalarsGroup.setStatus(_A)
tnCardTableGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,3,1,1,1,2))
tnCardTableGroup.setObjects(*((_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am)))
if mibBuilder.loadTexts:tnCardTableGroup.setStatus(_A)
tnCardAssemblyTableGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,3,1,1,1,3))
tnCardAssemblyTableGroup.setObjects(*((_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As)))
if mibBuilder.loadTexts:tnCardAssemblyTableGroup.setStatus(_A)
tnCardPrbsTestIdTableGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,3,1,1,1,5))
tnCardPrbsTestIdTableGroup.setObjects((_B,_At))
if mibBuilder.loadTexts:tnCardPrbsTestIdTableGroup.setStatus(_A)
tnCardCompliance=ModuleCompliance((1,3,6,1,4,1,7483,2,2,3,1,1,2,1))
tnCardCompliance.setObjects(*((_B,_Au),(_B,_Av),(_B,_Aw),(_B,_Ax)))
if mibBuilder.loadTexts:tnCardCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'NokiaOAMTestUnitType':NokiaOAMTestUnitType,'tnCardMibModule':tnCardMibModule,'tnCardConf':tnCardConf,'tnCardGroups':tnCardGroups,_Au:tnCardScalarsGroup,_Av:tnCardTableGroup,_Aw:tnCardAssemblyTableGroup,_Ax:tnCardPrbsTestIdTableGroup,'tnCardCompliances':tnCardCompliances,'tnCardCompliance':tnCardCompliance,'tnCardObjs':tnCardObjs,'tnCardBasics':tnCardBasics,_c:tnCardTotal,'tnCardTable':tnCardTable,'tnCardEntry':tnCardEntry,_d:tnCardName,_e:tnCardDescr,_f:tnCardCLEI,_g:tnCardHFD,_h:tnCardSerialNumber,_i:tnCardManufacturingPartNumber,_j:tnCardMarketingPartNumber,_k:tnCardSWGenericLoadName,_l:tnCardHeight,_m:tnCardWidth,_n:tnCardTemperature,_o:tnCardHighTemperatureThresh,_p:tnCardLowTemperatureThresh,_q:tnCardTemperatureTolerance,_r:tnCardStatusLEDColor,_s:tnCardStatusLEDState,_t:tnCardActivityLEDColor,_u:tnCardActivityLEDState,_v:tnCardCompanyID,_w:tnCardMnemonic,_x:tnCardSWPartNum,_y:tnCardDate,_z:tnCardExtraData,_A0:tnCardAnyPortsInService,_A1:tnCardLastBootedFwBundleVer,_A2:tnCardNextFwBundleVer,_A3:tnCardFactoryID,_A4:tnCardCapacity,_A5:tnCardLACPSystemPriority,_A6:tnCardMaxPower,_A7:tnCardEthOamCcmFaultMgntMode,_A8:tnCardClkSwitch,_A9:tnCardRtrvClkSwitch,_AA:tnCardWtClkMeasureValues,_AB:tnCardPower,_AC:tnCardCurrent,_AD:tnCardUplinkAdminMode,_AE:tnCardLoopbackNoServPort,_AF:tnCardAlmProfName,_AG:tnCardAlmProfEnvName,_AH:tnCardLicenseData,_AI:tnCardLicenseAction,_AJ:tnCardLicenseCap1Val,_AK:tnCardLicenseCap2Val,_AL:tnCardLicenseTimeStamp,_AM:tnCardLicenseRmaKey,_AN:tnCardMirrorLoopbackNoServPort,_AO:tnCardDNRLEDColor,_AP:tnCardTestHdNoServPort,_AQ:tnCardAmbientTemp,_AR:tnCardRpmRead,_AS:tnCardL1andL2Decoupled,_AT:tnCardIntWrkMode,_AU:tnCardTotalRam,_AV:tnCardTransportModeOSC,_AW:tnCardModuleCfg,_AX:tnCardLicenseRestricted,_AY:tnCardLineMode,_AZ:tnCardInitConfProfile,_Aa:tnCardVirtual,_Ab:tnCardOAMTestUnit,_Ac:tnCardSlotClkStatus,_Ad:tnCardClkSelectedValue,_Ae:tnCardShutdownCmd,_Af:tnCardCpuTemperature,_Ag:tnCardMainDeviceTemperature,_Ah:tnCardAseMode,_Ai:tnCardAddPowerMode,_Aj:tnCardLOLCKDetectionEnable,_Ak:tnCardSapLoopbackMacAddr,_Al:tnCardMgracd,_Am:tnCardTargetAddPortInputPower,'tnCardAssemblyTable':tnCardAssemblyTable,'tnCardAssemblyEntry':tnCardAssemblyEntry,_b:tnCardAssemblyIndex,_An:tnCardAssemblyName,_Ao:tnCardAssemblyCLEI,_Ap:tnCardAssemblyHFD,_Aq:tnCardAssemblySerialNumber,_Ar:tnCardAssemblyManufacturingPartNumber,_As:tnCardAssemblyMarketingPartNumber,'tnCardDbSyncTable':tnCardDbSyncTable,'tnCardDbSyncEntry':tnCardDbSyncEntry,'tnCardDBSyncEnabledByUser':tnCardDBSyncEnabledByUser,'tnCardPrbsTestIdTable':tnCardPrbsTestIdTable,'tnCardPrbsTestIdEntry':tnCardPrbsTestIdEntry,_At:tnCardPrbsTestIdOidList})