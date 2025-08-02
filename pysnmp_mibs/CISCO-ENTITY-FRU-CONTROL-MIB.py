_B5='cefcVmModuleNotifsGroup'
_B4='cefcVmModuleGroup'
_B3='cefcPowerSupplyActualGroup'
_B2='cefcFanSpeedGroup'
_B1='cefcFanDirectionGroup'
_B0='cefcVmModuleStatusChangeNotif'
_A_='cefcPowerSupplyOutputChange'
_Az='cefcFanTrayStatusChange'
_Ay='cefcUnrecognizedFRU'
_Ax='cefcFRURemoved'
_Aw='cefcFRUInserted'
_Av='cefcPowerStatusChange'
_Au='cefcModuleStatusChange'
_At='cefcFRUActualOutputCurrent'
_As='cefcFRUActualInputCurrent'
_Ar='cefcFanSpeedPercent'
_Aq='cefcFanSpeed'
_Ap='cefcFanTrayDirection'
_Ao='cefcFanCoolingCapCapacityUnit'
_An='cefcFanCoolingCapacityUnit'
_Am='cefcModuleCoolingUnit'
_Al='cefcChassisPerSlotCoolingUnit'
_Ak='cefcFRUPowerCapability'
_Aj='cefcFRURealTimeCurrent'
_Ai='cefcModuleLocalSwitchingMode'
_Ah='cefcFanCoolingCapCurrent'
_Ag='cefcFanCoolingCapCapacity'
_Af='cefcFanCoolingCapModeDescr'
_Ae='cefcPowerNonRedundantReason'
_Ad='cefcTotalDrawnInlineCurrent'
_Ac='cefcEnablePSOutputChangeNotif'
_Ab='cefcModulePowerConsumption'
_Aa='cefcConnectorRating'
_AZ='cefcPSOutputModeInOperation'
_AY='cefcPowerSupplyInputType'
_AX='cefcIntelliModuleIPAddr'
_AW='cefcIntelliModuleIPAddrType'
_AV='cefcModuleUpTime'
_AU='cefcModuleStateChangeReasonDescr'
_AT='cefcMaxDefaultHighInLinePower'
_AS='cefcPowerRedundancyOperMode'
_AR='cefcFRUDrawnInlineCurrent'
_AQ='cefcFRUTotalInlineCurrent'
_AP='cefcFRUDrawnSystemCurrent'
_AO='cefcFRUTotalSystemCurrent'
_AN='cefcModuleResetReasonDescription'
_AM='cefcModuleLastClearConfigTime'
_AL='cefcMIBEnableStatusNotification'
_AK='cefcMaxDefaultInLinePower'
_AJ='cefcModuleResetReason'
_AI='cefcModuleAdminStatus'
_AH='cefcFRUCurrent'
_AG='cefcTotalDrawnCurrent'
_AF='cefcTotalAvailableCurrent'
_AE='cefcPowerUnits'
_AD='cefcPowerRedundancyMode'
_AC='cefcFanCoolingCapIndex'
_AB='cefcPSOutputModeIndex'
_AA='cefcPowerSupplyInputIndex'
_A9='miliwatts'
_A8='outOfServiceAdmin'
_A7='Unsigned32'
_A6='entPhysicalVendorType'
_A5='entPhysicalClass'
_A4='cefcFanCoolingGroup'
_A3='cefcCoolingGroup2'
_A2='cefcFRUFanCoolingUnitGroup'
_A1='cefcFRUCoolingUnitGroup'
_A0='cefcFRUPowerCapabilityGroup'
_z='cefcFRUPowerRealTimeStatusGroup'
_y='cefcMIBModuleLocalSwitchingGroup'
_x='cefcCoolingGroup'
_w='cefcVmModuleStatusLastChangeTime'
_v='cefcVmModuleOperStatus'
_u='cefcModuleCooling'
_t='cefcFanCoolingCapacity'
_s='cefcChassisPerSlotCoolingCap'
_r='cefcPSOutputModeCurrent'
_q='cefcPhysicalStatus'
_p='cefcFanTrayOperStatus'
_o='cefcModuleStatusLastChangeTime'
_n='cefcModuleOperStatus'
_m='cefcFRUPowerOperStatus'
_l='cefcFRUPowerAdminStatus'
_k='not-accessible'
_j='disabled'
_i='TruthValue'
_h='entPhysicalName'
_g='entPhysicalModelName'
_f='entPhysicalContainedIn'
_e='cefcFanCoolingCapGroup'
_d='cefcMIBPowerRedundancyInfoGroup'
_c='cefcMIBInLinePowerCurrentGroup'
_b='cefcMgmtNotificationsGroup3'
_a='cefcMIBNotificationEnablesGroup2'
_Z='cefcConnectorRatingGroup'
_Y='cefcPowerCapacityGroup'
_X='cefcMIBInLinePowerControlGroup'
_W='cefcIntelliModuleGroup'
_V='cefcModuleExtGroup'
_U='cefcMIBPowerOperModeGroup'
_T='cefcMIBInLinePowerControlGroupRev1'
_S='cefcMIBPhysicalGroup'
_R='cefcMIBFanTrayStatusGroup'
_Q='cefcMgmtNotificationsGroup2'
_P='unknown'
_O='cefcMIBPowerFRUValueGroup'
_N='Integer32'
_M='cefcModuleGroupRev1'
_L='cefcMIBNotificationEnablesGroup'
_K='cefcMIBModuleGroup'
_J='cefcMgmtNotificationsGroup'
_I='deprecated'
_H='cefcMIBPowerFRUControlGroup'
_G='cefcMIBPowerModeGroup'
_F='read-write'
_E='entPhysicalIndex'
_D='ENTITY-MIB'
_C='read-only'
_B='current'
_A='CISCO-ENTITY-FRU-CONTROL-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
entPhysicalClass,entPhysicalContainedIn,entPhysicalIndex,entPhysicalModelName,entPhysicalName,entPhysicalVendorType=mibBuilder.importSymbols(_D,_A5,_f,_E,_g,_h,_A6)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_N,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_A7,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_i)
ciscoEntityFRUControlMIB=ModuleIdentity((1,3,6,1,4,1,9,9,117))
if mibBuilder.loadTexts:ciscoEntityFRUControlMIB.setRevisions(('2018-11-05 00:00','2018-08-20 00:00','2018-07-25 00:00','2017-12-06 00:00','2013-08-19 00:00','2011-12-22 00:00','2011-03-18 00:00','2010-12-10 00:00','2008-10-08 00:00','2007-06-21 00:00','2007-03-14 00:00','2006-06-23 00:00','2005-09-06 00:00','2004-12-09 00:00','2004-10-19 00:00','2003-11-24 00:00','2003-10-27 00:00','2003-10-23 00:00','2003-07-22 00:00','2002-10-16 00:00','2002-10-03 00:00','2002-09-15 00:00','2002-07-12 00:00','2001-05-22 00:00','2000-01-13 00:00','1999-04-05 00:00'))
class PowerRedundancyType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('notsupported',1),('redundant',2),('combined',3),('nonRedundant',4),('psRedundant',5),('inPwrSrcRedundant',6),('psRedundantSingleInput',7)))
class PowerAdminType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('on',1),('off',2),('inlineAuto',3),('inlineOn',4),('powerCycle',5)))
class PowerOperType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('offEnvOther',1),('on',2),('offAdmin',3),('offDenied',4),('offEnvPower',5),('offEnvTemp',6),('offEnvFan',7),('failed',8),('onButFanFail',9),('offCooling',10),('offConnectorRating',11),('onButInlinePowerFail',12)))
class FRUCurrentType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1000000000,1000000000))
class ModuleAdminType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('enabled',1),(_j,2),('reset',3),(_A8,4)))
class ModuleOperType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27)));namedValues=NamedValues(*((_P,1),('ok',2),(_j,3),('okButDiagFailed',4),('boot',5),('selfTest',6),('failed',7),('missing',8),('mismatchWithParent',9),('mismatchConfig',10),('diagFailed',11),('dormant',12),(_A8,13),('outOfServiceEnvTemp',14),('poweredDown',15),('poweredUp',16),('powerDenied',17),('powerCycled',18),('okButPowerOverWarning',19),('okButPowerOverCritical',20),('syncInProgress',21),('upgrading',22),('okButAuthFailed',23),('mdr',24),('fwMismatchFound',25),('fwDownloadSuccess',26),('fwDownloadFailure',27)))
class ModuleResetReasonType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23)));namedValues=NamedValues(*((_P,1),('powerUp',2),('parityError',3),('clearConfigReset',4),('manualReset',5),('watchDogTimeoutReset',6),('resourceOverflowReset',7),('missingTaskReset',8),('lowVoltageReset',9),('controllerReset',10),('systemReset',11),('switchoverReset',12),('upgradeReset',13),('downgradeReset',14),('cacheErrorReset',15),('deviceDriverReset',16),('softwareExceptionReset',17),('restoreConfigReset',18),('abortRevReset',19),('burnBootReset',20),('standbyCdHealthierReset',21),('nonNativeConfigClearReset',22),('memoryProtectionErrorReset',23)))
class FRUTimeSeconds(TextualConvention,Unsigned32):status=_B
class FRUCoolingUnit(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cfm',1),('watts',2)))
class CefcPercentOrMinusOne(TextualConvention,Integer32):status=_B;displayHint='d';subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,100))
class CefcVmModuleOperType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('down',1),('up',2),(_P,3),('goingDown',4)))
_CefcMIBObjects_ObjectIdentity=ObjectIdentity
cefcMIBObjects=_CefcMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,117,1))
_CefcFRUPower_ObjectIdentity=ObjectIdentity
cefcFRUPower=_CefcFRUPower_ObjectIdentity((1,3,6,1,4,1,9,9,117,1,1))
_CefcFRUPowerSupplyGroupTable_Object=MibTable
cefcFRUPowerSupplyGroupTable=_CefcFRUPowerSupplyGroupTable_Object((1,3,6,1,4,1,9,9,117,1,1,1))
if mibBuilder.loadTexts:cefcFRUPowerSupplyGroupTable.setStatus(_B)
_CefcFRUPowerSupplyGroupEntry_Object=MibTableRow
cefcFRUPowerSupplyGroupEntry=_CefcFRUPowerSupplyGroupEntry_Object((1,3,6,1,4,1,9,9,117,1,1,1,1))
cefcFRUPowerSupplyGroupEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cefcFRUPowerSupplyGroupEntry.setStatus(_B)
_CefcPowerRedundancyMode_Type=PowerRedundancyType
_CefcPowerRedundancyMode_Object=MibTableColumn
cefcPowerRedundancyMode=_CefcPowerRedundancyMode_Object((1,3,6,1,4,1,9,9,117,1,1,1,1,1),_CefcPowerRedundancyMode_Type())
cefcPowerRedundancyMode.setMaxAccess(_F)
if mibBuilder.loadTexts:cefcPowerRedundancyMode.setStatus(_B)
_CefcPowerUnits_Type=DisplayString
_CefcPowerUnits_Object=MibTableColumn
cefcPowerUnits=_CefcPowerUnits_Object((1,3,6,1,4,1,9,9,117,1,1,1,1,2),_CefcPowerUnits_Type())
cefcPowerUnits.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcPowerUnits.setStatus(_B)
_CefcTotalAvailableCurrent_Type=FRUCurrentType
_CefcTotalAvailableCurrent_Object=MibTableColumn
cefcTotalAvailableCurrent=_CefcTotalAvailableCurrent_Object((1,3,6,1,4,1,9,9,117,1,1,1,1,3),_CefcTotalAvailableCurrent_Type())
cefcTotalAvailableCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcTotalAvailableCurrent.setStatus(_B)
_CefcTotalDrawnCurrent_Type=FRUCurrentType
_CefcTotalDrawnCurrent_Object=MibTableColumn
cefcTotalDrawnCurrent=_CefcTotalDrawnCurrent_Object((1,3,6,1,4,1,9,9,117,1,1,1,1,4),_CefcTotalDrawnCurrent_Type())
cefcTotalDrawnCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcTotalDrawnCurrent.setStatus(_B)
_CefcPowerRedundancyOperMode_Type=PowerRedundancyType
_CefcPowerRedundancyOperMode_Object=MibTableColumn
cefcPowerRedundancyOperMode=_CefcPowerRedundancyOperMode_Object((1,3,6,1,4,1,9,9,117,1,1,1,1,5),_CefcPowerRedundancyOperMode_Type())
cefcPowerRedundancyOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcPowerRedundancyOperMode.setStatus(_B)
class _CefcPowerNonRedundantReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('notApplicable',1),(_P,2),('singleSupply',3),('mismatchedSupplies',4),('supplyError',5)))
_CefcPowerNonRedundantReason_Type.__name__=_N
_CefcPowerNonRedundantReason_Object=MibTableColumn
cefcPowerNonRedundantReason=_CefcPowerNonRedundantReason_Object((1,3,6,1,4,1,9,9,117,1,1,1,1,6),_CefcPowerNonRedundantReason_Type())
cefcPowerNonRedundantReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcPowerNonRedundantReason.setStatus(_B)
_CefcTotalDrawnInlineCurrent_Type=FRUCurrentType
_CefcTotalDrawnInlineCurrent_Object=MibTableColumn
cefcTotalDrawnInlineCurrent=_CefcTotalDrawnInlineCurrent_Object((1,3,6,1,4,1,9,9,117,1,1,1,1,7),_CefcTotalDrawnInlineCurrent_Type())
cefcTotalDrawnInlineCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcTotalDrawnInlineCurrent.setStatus(_B)
_CefcFRUPowerStatusTable_Object=MibTable
cefcFRUPowerStatusTable=_CefcFRUPowerStatusTable_Object((1,3,6,1,4,1,9,9,117,1,1,2))
if mibBuilder.loadTexts:cefcFRUPowerStatusTable.setStatus(_B)
_CefcFRUPowerStatusEntry_Object=MibTableRow
cefcFRUPowerStatusEntry=_CefcFRUPowerStatusEntry_Object((1,3,6,1,4,1,9,9,117,1,1,2,1))
cefcFRUPowerStatusEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cefcFRUPowerStatusEntry.setStatus(_B)
_CefcFRUPowerAdminStatus_Type=PowerAdminType
_CefcFRUPowerAdminStatus_Object=MibTableColumn
cefcFRUPowerAdminStatus=_CefcFRUPowerAdminStatus_Object((1,3,6,1,4,1,9,9,117,1,1,2,1,1),_CefcFRUPowerAdminStatus_Type())
cefcFRUPowerAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cefcFRUPowerAdminStatus.setStatus(_B)
_CefcFRUPowerOperStatus_Type=PowerOperType
_CefcFRUPowerOperStatus_Object=MibTableColumn
cefcFRUPowerOperStatus=_CefcFRUPowerOperStatus_Object((1,3,6,1,4,1,9,9,117,1,1,2,1,2),_CefcFRUPowerOperStatus_Type())
cefcFRUPowerOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcFRUPowerOperStatus.setStatus(_B)
_CefcFRUCurrent_Type=FRUCurrentType
_CefcFRUCurrent_Object=MibTableColumn
cefcFRUCurrent=_CefcFRUCurrent_Object((1,3,6,1,4,1,9,9,117,1,1,2,1,3),_CefcFRUCurrent_Type())
cefcFRUCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcFRUCurrent.setStatus(_B)
class _CefcFRUPowerCapability_Type(Bits):namedValues=NamedValues(('realTimeCurrent',0))
_CefcFRUPowerCapability_Type.__name__='Bits'
_CefcFRUPowerCapability_Object=MibTableColumn
cefcFRUPowerCapability=_CefcFRUPowerCapability_Object((1,3,6,1,4,1,9,9,117,1,1,2,1,4),_CefcFRUPowerCapability_Type())
cefcFRUPowerCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcFRUPowerCapability.setStatus(_B)
_CefcFRURealTimeCurrent_Type=FRUCurrentType
_CefcFRURealTimeCurrent_Object=MibTableColumn
cefcFRURealTimeCurrent=_CefcFRURealTimeCurrent_Object((1,3,6,1,4,1,9,9,117,1,1,2,1,5),_CefcFRURealTimeCurrent_Type())
cefcFRURealTimeCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcFRURealTimeCurrent.setStatus(_B)
class _CefcMaxDefaultInLinePower_Type(Integer32):defaultValue=12500;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12500))
_CefcMaxDefaultInLinePower_Type.__name__=_N
_CefcMaxDefaultInLinePower_Object=MibScalar
cefcMaxDefaultInLinePower=_CefcMaxDefaultInLinePower_Object((1,3,6,1,4,1,9,9,117,1,1,3),_CefcMaxDefaultInLinePower_Type())
cefcMaxDefaultInLinePower.setMaxAccess(_F)
if mibBuilder.loadTexts:cefcMaxDefaultInLinePower.setStatus(_I)
if mibBuilder.loadTexts:cefcMaxDefaultInLinePower.setUnits(_A9)
_CefcFRUPowerSupplyValueTable_Object=MibTable
cefcFRUPowerSupplyValueTable=_CefcFRUPowerSupplyValueTable_Object((1,3,6,1,4,1,9,9,117,1,1,4))
if mibBuilder.loadTexts:cefcFRUPowerSupplyValueTable.setStatus(_B)
_CefcFRUPowerSupplyValueEntry_Object=MibTableRow
cefcFRUPowerSupplyValueEntry=_CefcFRUPowerSupplyValueEntry_Object((1,3,6,1,4,1,9,9,117,1,1,4,1))
cefcFRUPowerSupplyValueEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cefcFRUPowerSupplyValueEntry.setStatus(_B)
_CefcFRUTotalSystemCurrent_Type=FRUCurrentType
_CefcFRUTotalSystemCurrent_Object=MibTableColumn
cefcFRUTotalSystemCurrent=_CefcFRUTotalSystemCurrent_Object((1,3,6,1,4,1,9,9,117,1,1,4,1,1),_CefcFRUTotalSystemCurrent_Type())
cefcFRUTotalSystemCurrent.setMaxAccess(_F)
if mibBuilder.loadTexts:cefcFRUTotalSystemCurrent.setStatus(_B)
_CefcFRUDrawnSystemCurrent_Type=FRUCurrentType
_CefcFRUDrawnSystemCurrent_Object=MibTableColumn
cefcFRUDrawnSystemCurrent=_CefcFRUDrawnSystemCurrent_Object((1,3,6,1,4,1,9,9,117,1,1,4,1,2),_CefcFRUDrawnSystemCurrent_Type())
cefcFRUDrawnSystemCurrent.setMaxAccess(_F)
if mibBuilder.loadTexts:cefcFRUDrawnSystemCurrent.setStatus(_B)
_CefcFRUTotalInlineCurrent_Type=FRUCurrentType
_CefcFRUTotalInlineCurrent_Object=MibTableColumn
cefcFRUTotalInlineCurrent=_CefcFRUTotalInlineCurrent_Object((1,3,6,1,4,1,9,9,117,1,1,4,1,3),_CefcFRUTotalInlineCurrent_Type())
cefcFRUTotalInlineCurrent.setMaxAccess(_F)
if mibBuilder.loadTexts:cefcFRUTotalInlineCurrent.setStatus(_B)
_CefcFRUDrawnInlineCurrent_Type=FRUCurrentType
_CefcFRUDrawnInlineCurrent_Object=MibTableColumn
cefcFRUDrawnInlineCurrent=_CefcFRUDrawnInlineCurrent_Object((1,3,6,1,4,1,9,9,117,1,1,4,1,4),_CefcFRUDrawnInlineCurrent_Type())
cefcFRUDrawnInlineCurrent.setMaxAccess(_F)
if mibBuilder.loadTexts:cefcFRUDrawnInlineCurrent.setStatus(_B)
_CefcFRUActualInputCurrent_Type=FRUCurrentType
_CefcFRUActualInputCurrent_Object=MibTableColumn
cefcFRUActualInputCurrent=_CefcFRUActualInputCurrent_Object((1,3,6,1,4,1,9,9,117,1,1,4,1,5),_CefcFRUActualInputCurrent_Type())
cefcFRUActualInputCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcFRUActualInputCurrent.setStatus(_B)
_CefcFRUActualOutputCurrent_Type=FRUCurrentType
_CefcFRUActualOutputCurrent_Object=MibTableColumn
cefcFRUActualOutputCurrent=_CefcFRUActualOutputCurrent_Object((1,3,6,1,4,1,9,9,117,1,1,4,1,6),_CefcFRUActualOutputCurrent_Type())
cefcFRUActualOutputCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcFRUActualOutputCurrent.setStatus(_B)
_CefcMaxDefaultHighInLinePower_Type=Unsigned32
_CefcMaxDefaultHighInLinePower_Object=MibScalar
cefcMaxDefaultHighInLinePower=_CefcMaxDefaultHighInLinePower_Object((1,3,6,1,4,1,9,9,117,1,1,5),_CefcMaxDefaultHighInLinePower_Type())
cefcMaxDefaultHighInLinePower.setMaxAccess(_F)
if mibBuilder.loadTexts:cefcMaxDefaultHighInLinePower.setStatus(_B)
if mibBuilder.loadTexts:cefcMaxDefaultHighInLinePower.setUnits(_A9)
_CefcModule_ObjectIdentity=ObjectIdentity
cefcModule=_CefcModule_ObjectIdentity((1,3,6,1,4,1,9,9,117,1,2))
_CefcModuleTable_Object=MibTable
cefcModuleTable=_CefcModuleTable_Object((1,3,6,1,4,1,9,9,117,1,2,1))
if mibBuilder.loadTexts:cefcModuleTable.setStatus(_B)
_CefcModuleEntry_Object=MibTableRow
cefcModuleEntry=_CefcModuleEntry_Object((1,3,6,1,4,1,9,9,117,1,2,1,1))
cefcModuleEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cefcModuleEntry.setStatus(_B)
_CefcModuleAdminStatus_Type=ModuleAdminType
_CefcModuleAdminStatus_Object=MibTableColumn
cefcModuleAdminStatus=_CefcModuleAdminStatus_Object((1,3,6,1,4,1,9,9,117,1,2,1,1,1),_CefcModuleAdminStatus_Type())
cefcModuleAdminStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:cefcModuleAdminStatus.setStatus(_B)
_CefcModuleOperStatus_Type=ModuleOperType
_CefcModuleOperStatus_Object=MibTableColumn
cefcModuleOperStatus=_CefcModuleOperStatus_Object((1,3,6,1,4,1,9,9,117,1,2,1,1,2),_CefcModuleOperStatus_Type())
cefcModuleOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcModuleOperStatus.setStatus(_B)
_CefcModuleResetReason_Type=ModuleResetReasonType
_CefcModuleResetReason_Object=MibTableColumn
cefcModuleResetReason=_CefcModuleResetReason_Object((1,3,6,1,4,1,9,9,117,1,2,1,1,3),_CefcModuleResetReason_Type())
cefcModuleResetReason.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcModuleResetReason.setStatus(_B)
_CefcModuleStatusLastChangeTime_Type=TimeStamp
_CefcModuleStatusLastChangeTime_Object=MibTableColumn
cefcModuleStatusLastChangeTime=_CefcModuleStatusLastChangeTime_Object((1,3,6,1,4,1,9,9,117,1,2,1,1,4),_CefcModuleStatusLastChangeTime_Type())
cefcModuleStatusLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcModuleStatusLastChangeTime.setStatus(_B)
_CefcModuleLastClearConfigTime_Type=TimeStamp
_CefcModuleLastClearConfigTime_Object=MibTableColumn
cefcModuleLastClearConfigTime=_CefcModuleLastClearConfigTime_Object((1,3,6,1,4,1,9,9,117,1,2,1,1,5),_CefcModuleLastClearConfigTime_Type())
cefcModuleLastClearConfigTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcModuleLastClearConfigTime.setStatus(_B)
_CefcModuleResetReasonDescription_Type=DisplayString
_CefcModuleResetReasonDescription_Object=MibTableColumn
cefcModuleResetReasonDescription=_CefcModuleResetReasonDescription_Object((1,3,6,1,4,1,9,9,117,1,2,1,1,6),_CefcModuleResetReasonDescription_Type())
cefcModuleResetReasonDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcModuleResetReasonDescription.setStatus(_B)
_CefcModuleStateChangeReasonDescr_Type=DisplayString
_CefcModuleStateChangeReasonDescr_Object=MibTableColumn
cefcModuleStateChangeReasonDescr=_CefcModuleStateChangeReasonDescr_Object((1,3,6,1,4,1,9,9,117,1,2,1,1,7),_CefcModuleStateChangeReasonDescr_Type())
cefcModuleStateChangeReasonDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcModuleStateChangeReasonDescr.setStatus(_B)
_CefcModuleUpTime_Type=FRUTimeSeconds
_CefcModuleUpTime_Object=MibTableColumn
cefcModuleUpTime=_CefcModuleUpTime_Object((1,3,6,1,4,1,9,9,117,1,2,1,1,8),_CefcModuleUpTime_Type())
cefcModuleUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcModuleUpTime.setStatus(_B)
_CefcVmModuleOperStatus_Type=CefcVmModuleOperType
_CefcVmModuleOperStatus_Object=MibTableColumn
cefcVmModuleOperStatus=_CefcVmModuleOperStatus_Object((1,3,6,1,4,1,9,9,117,1,2,1,1,9),_CefcVmModuleOperStatus_Type())
cefcVmModuleOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcVmModuleOperStatus.setStatus(_B)
_CefcVmModuleStatusLastChangeTime_Type=TimeStamp
_CefcVmModuleStatusLastChangeTime_Object=MibTableColumn
cefcVmModuleStatusLastChangeTime=_CefcVmModuleStatusLastChangeTime_Object((1,3,6,1,4,1,9,9,117,1,2,1,1,10),_CefcVmModuleStatusLastChangeTime_Type())
cefcVmModuleStatusLastChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcVmModuleStatusLastChangeTime.setStatus(_B)
_CefcIntelliModuleTable_Object=MibTable
cefcIntelliModuleTable=_CefcIntelliModuleTable_Object((1,3,6,1,4,1,9,9,117,1,2,2))
if mibBuilder.loadTexts:cefcIntelliModuleTable.setStatus(_B)
_CefcIntelliModuleEntry_Object=MibTableRow
cefcIntelliModuleEntry=_CefcIntelliModuleEntry_Object((1,3,6,1,4,1,9,9,117,1,2,2,1))
cefcIntelliModuleEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cefcIntelliModuleEntry.setStatus(_B)
_CefcIntelliModuleIPAddrType_Type=InetAddressType
_CefcIntelliModuleIPAddrType_Object=MibTableColumn
cefcIntelliModuleIPAddrType=_CefcIntelliModuleIPAddrType_Object((1,3,6,1,4,1,9,9,117,1,2,2,1,1),_CefcIntelliModuleIPAddrType_Type())
cefcIntelliModuleIPAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcIntelliModuleIPAddrType.setStatus(_B)
_CefcIntelliModuleIPAddr_Type=InetAddress
_CefcIntelliModuleIPAddr_Object=MibTableColumn
cefcIntelliModuleIPAddr=_CefcIntelliModuleIPAddr_Object((1,3,6,1,4,1,9,9,117,1,2,2,1,2),_CefcIntelliModuleIPAddr_Type())
cefcIntelliModuleIPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcIntelliModuleIPAddr.setStatus(_B)
_CefcModuleLocalSwitchingTable_Object=MibTable
cefcModuleLocalSwitchingTable=_CefcModuleLocalSwitchingTable_Object((1,3,6,1,4,1,9,9,117,1,2,3))
if mibBuilder.loadTexts:cefcModuleLocalSwitchingTable.setStatus(_B)
_CefcModuleLocalSwitchingEntry_Object=MibTableRow
cefcModuleLocalSwitchingEntry=_CefcModuleLocalSwitchingEntry_Object((1,3,6,1,4,1,9,9,117,1,2,3,1))
cefcModuleLocalSwitchingEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cefcModuleLocalSwitchingEntry.setStatus(_B)
class _CefcModuleLocalSwitchingMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),(_j,2)))
_CefcModuleLocalSwitchingMode_Type.__name__=_N
_CefcModuleLocalSwitchingMode_Object=MibTableColumn
cefcModuleLocalSwitchingMode=_CefcModuleLocalSwitchingMode_Object((1,3,6,1,4,1,9,9,117,1,2,3,1,1),_CefcModuleLocalSwitchingMode_Type())
cefcModuleLocalSwitchingMode.setMaxAccess(_F)
if mibBuilder.loadTexts:cefcModuleLocalSwitchingMode.setStatus(_B)
_CefcMIBNotificationEnables_ObjectIdentity=ObjectIdentity
cefcMIBNotificationEnables=_CefcMIBNotificationEnables_ObjectIdentity((1,3,6,1,4,1,9,9,117,1,3))
class _CefcMIBEnableStatusNotification_Type(TruthValue):defaultValue=2
_CefcMIBEnableStatusNotification_Type.__name__=_i
_CefcMIBEnableStatusNotification_Object=MibScalar
cefcMIBEnableStatusNotification=_CefcMIBEnableStatusNotification_Object((1,3,6,1,4,1,9,9,117,1,3,1),_CefcMIBEnableStatusNotification_Type())
cefcMIBEnableStatusNotification.setMaxAccess(_F)
if mibBuilder.loadTexts:cefcMIBEnableStatusNotification.setStatus(_B)
class _CefcEnablePSOutputChangeNotif_Type(TruthValue):defaultValue=2
_CefcEnablePSOutputChangeNotif_Type.__name__=_i
_CefcEnablePSOutputChangeNotif_Object=MibScalar
cefcEnablePSOutputChangeNotif=_CefcEnablePSOutputChangeNotif_Object((1,3,6,1,4,1,9,9,117,1,3,2),_CefcEnablePSOutputChangeNotif_Type())
cefcEnablePSOutputChangeNotif.setMaxAccess(_F)
if mibBuilder.loadTexts:cefcEnablePSOutputChangeNotif.setStatus(_B)
_CefcFRUFan_ObjectIdentity=ObjectIdentity
cefcFRUFan=_CefcFRUFan_ObjectIdentity((1,3,6,1,4,1,9,9,117,1,4))
_CefcFanTrayStatusTable_Object=MibTable
cefcFanTrayStatusTable=_CefcFanTrayStatusTable_Object((1,3,6,1,4,1,9,9,117,1,4,1))
if mibBuilder.loadTexts:cefcFanTrayStatusTable.setStatus(_B)
_CefcFanTrayStatusEntry_Object=MibTableRow
cefcFanTrayStatusEntry=_CefcFanTrayStatusEntry_Object((1,3,6,1,4,1,9,9,117,1,4,1,1))
cefcFanTrayStatusEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cefcFanTrayStatusEntry.setStatus(_B)
class _CefcFanTrayOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_P,1),('up',2),('down',3),('warning',4)))
_CefcFanTrayOperStatus_Type.__name__=_N
_CefcFanTrayOperStatus_Object=MibTableColumn
cefcFanTrayOperStatus=_CefcFanTrayOperStatus_Object((1,3,6,1,4,1,9,9,117,1,4,1,1,1),_CefcFanTrayOperStatus_Type())
cefcFanTrayOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcFanTrayOperStatus.setStatus(_B)
class _CefcFanTrayDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_P,1),('frontToBack',2),('backToFront',3)))
_CefcFanTrayDirection_Type.__name__=_N
_CefcFanTrayDirection_Object=MibTableColumn
cefcFanTrayDirection=_CefcFanTrayDirection_Object((1,3,6,1,4,1,9,9,117,1,4,1,1,2),_CefcFanTrayDirection_Type())
cefcFanTrayDirection.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcFanTrayDirection.setStatus(_B)
_CefcFanTable_Object=MibTable
cefcFanTable=_CefcFanTable_Object((1,3,6,1,4,1,9,9,117,1,4,2))
if mibBuilder.loadTexts:cefcFanTable.setStatus(_B)
_CefcFanEntry_Object=MibTableRow
cefcFanEntry=_CefcFanEntry_Object((1,3,6,1,4,1,9,9,117,1,4,2,1))
cefcFanEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cefcFanEntry.setStatus(_B)
_CefcFanSpeed_Type=Unsigned32
_CefcFanSpeed_Object=MibTableColumn
cefcFanSpeed=_CefcFanSpeed_Object((1,3,6,1,4,1,9,9,117,1,4,2,1,1),_CefcFanSpeed_Type())
cefcFanSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcFanSpeed.setStatus(_B)
if mibBuilder.loadTexts:cefcFanSpeed.setUnits('rpm')
_CefcFanSpeedPercent_Type=CefcPercentOrMinusOne
_CefcFanSpeedPercent_Object=MibTableColumn
cefcFanSpeedPercent=_CefcFanSpeedPercent_Object((1,3,6,1,4,1,9,9,117,1,4,2,1,2),_CefcFanSpeedPercent_Type())
cefcFanSpeedPercent.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcFanSpeedPercent.setStatus(_B)
if mibBuilder.loadTexts:cefcFanSpeedPercent.setUnits('percent')
_CefcPhysical_ObjectIdentity=ObjectIdentity
cefcPhysical=_CefcPhysical_ObjectIdentity((1,3,6,1,4,1,9,9,117,1,5))
_CefcPhysicalTable_Object=MibTable
cefcPhysicalTable=_CefcPhysicalTable_Object((1,3,6,1,4,1,9,9,117,1,5,1))
if mibBuilder.loadTexts:cefcPhysicalTable.setStatus(_B)
_CefcPhysicalEntry_Object=MibTableRow
cefcPhysicalEntry=_CefcPhysicalEntry_Object((1,3,6,1,4,1,9,9,117,1,5,1,1))
cefcPhysicalEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cefcPhysicalEntry.setStatus(_B)
class _CefcPhysicalStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('supported',2),('unsupported',3),('incompatible',4)))
_CefcPhysicalStatus_Type.__name__=_N
_CefcPhysicalStatus_Object=MibTableColumn
cefcPhysicalStatus=_CefcPhysicalStatus_Object((1,3,6,1,4,1,9,9,117,1,5,1,1,1),_CefcPhysicalStatus_Type())
cefcPhysicalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcPhysicalStatus.setStatus(_B)
_CefcPowerCapacity_ObjectIdentity=ObjectIdentity
cefcPowerCapacity=_CefcPowerCapacity_ObjectIdentity((1,3,6,1,4,1,9,9,117,1,6))
_CefcPowerSupplyInputTable_Object=MibTable
cefcPowerSupplyInputTable=_CefcPowerSupplyInputTable_Object((1,3,6,1,4,1,9,9,117,1,6,1))
if mibBuilder.loadTexts:cefcPowerSupplyInputTable.setStatus(_B)
_CefcPowerSupplyInputEntry_Object=MibTableRow
cefcPowerSupplyInputEntry=_CefcPowerSupplyInputEntry_Object((1,3,6,1,4,1,9,9,117,1,6,1,1))
cefcPowerSupplyInputEntry.setIndexNames((0,_D,_E),(0,_A,_AA))
if mibBuilder.loadTexts:cefcPowerSupplyInputEntry.setStatus(_B)
_CefcPowerSupplyInputIndex_Type=Unsigned32
_CefcPowerSupplyInputIndex_Object=MibTableColumn
cefcPowerSupplyInputIndex=_CefcPowerSupplyInputIndex_Object((1,3,6,1,4,1,9,9,117,1,6,1,1,1),_CefcPowerSupplyInputIndex_Type())
cefcPowerSupplyInputIndex.setMaxAccess(_k)
if mibBuilder.loadTexts:cefcPowerSupplyInputIndex.setStatus(_B)
class _CefcPowerSupplyInputType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_P,1),('acLow',2),('acHigh',3),('dcLow',4),('dcHigh',5)))
_CefcPowerSupplyInputType_Type.__name__=_N
_CefcPowerSupplyInputType_Object=MibTableColumn
cefcPowerSupplyInputType=_CefcPowerSupplyInputType_Object((1,3,6,1,4,1,9,9,117,1,6,1,1,2),_CefcPowerSupplyInputType_Type())
cefcPowerSupplyInputType.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcPowerSupplyInputType.setStatus(_B)
_CefcPowerSupplyOutputTable_Object=MibTable
cefcPowerSupplyOutputTable=_CefcPowerSupplyOutputTable_Object((1,3,6,1,4,1,9,9,117,1,6,2))
if mibBuilder.loadTexts:cefcPowerSupplyOutputTable.setStatus(_B)
_CefcPowerSupplyOutputEntry_Object=MibTableRow
cefcPowerSupplyOutputEntry=_CefcPowerSupplyOutputEntry_Object((1,3,6,1,4,1,9,9,117,1,6,2,1))
cefcPowerSupplyOutputEntry.setIndexNames((0,_D,_E),(0,_A,_AB))
if mibBuilder.loadTexts:cefcPowerSupplyOutputEntry.setStatus(_B)
_CefcPSOutputModeIndex_Type=Unsigned32
_CefcPSOutputModeIndex_Object=MibTableColumn
cefcPSOutputModeIndex=_CefcPSOutputModeIndex_Object((1,3,6,1,4,1,9,9,117,1,6,2,1,1),_CefcPSOutputModeIndex_Type())
cefcPSOutputModeIndex.setMaxAccess(_k)
if mibBuilder.loadTexts:cefcPSOutputModeIndex.setStatus(_B)
_CefcPSOutputModeCurrent_Type=FRUCurrentType
_CefcPSOutputModeCurrent_Object=MibTableColumn
cefcPSOutputModeCurrent=_CefcPSOutputModeCurrent_Object((1,3,6,1,4,1,9,9,117,1,6,2,1,2),_CefcPSOutputModeCurrent_Type())
cefcPSOutputModeCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcPSOutputModeCurrent.setStatus(_B)
_CefcPSOutputModeInOperation_Type=TruthValue
_CefcPSOutputModeInOperation_Object=MibTableColumn
cefcPSOutputModeInOperation=_CefcPSOutputModeInOperation_Object((1,3,6,1,4,1,9,9,117,1,6,2,1,3),_CefcPSOutputModeInOperation_Type())
cefcPSOutputModeInOperation.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcPSOutputModeInOperation.setStatus(_B)
_CefcCooling_ObjectIdentity=ObjectIdentity
cefcCooling=_CefcCooling_ObjectIdentity((1,3,6,1,4,1,9,9,117,1,7))
_CefcChassisCoolingTable_Object=MibTable
cefcChassisCoolingTable=_CefcChassisCoolingTable_Object((1,3,6,1,4,1,9,9,117,1,7,1))
if mibBuilder.loadTexts:cefcChassisCoolingTable.setStatus(_B)
_CefcChassisCoolingEntry_Object=MibTableRow
cefcChassisCoolingEntry=_CefcChassisCoolingEntry_Object((1,3,6,1,4,1,9,9,117,1,7,1,1))
cefcChassisCoolingEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cefcChassisCoolingEntry.setStatus(_B)
_CefcChassisPerSlotCoolingCap_Type=Unsigned32
_CefcChassisPerSlotCoolingCap_Object=MibTableColumn
cefcChassisPerSlotCoolingCap=_CefcChassisPerSlotCoolingCap_Object((1,3,6,1,4,1,9,9,117,1,7,1,1,1),_CefcChassisPerSlotCoolingCap_Type())
cefcChassisPerSlotCoolingCap.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcChassisPerSlotCoolingCap.setStatus(_B)
_CefcChassisPerSlotCoolingUnit_Type=FRUCoolingUnit
_CefcChassisPerSlotCoolingUnit_Object=MibTableColumn
cefcChassisPerSlotCoolingUnit=_CefcChassisPerSlotCoolingUnit_Object((1,3,6,1,4,1,9,9,117,1,7,1,1,2),_CefcChassisPerSlotCoolingUnit_Type())
cefcChassisPerSlotCoolingUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcChassisPerSlotCoolingUnit.setStatus(_B)
_CefcFanCoolingTable_Object=MibTable
cefcFanCoolingTable=_CefcFanCoolingTable_Object((1,3,6,1,4,1,9,9,117,1,7,2))
if mibBuilder.loadTexts:cefcFanCoolingTable.setStatus(_B)
_CefcFanCoolingEntry_Object=MibTableRow
cefcFanCoolingEntry=_CefcFanCoolingEntry_Object((1,3,6,1,4,1,9,9,117,1,7,2,1))
cefcFanCoolingEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cefcFanCoolingEntry.setStatus(_B)
_CefcFanCoolingCapacity_Type=Unsigned32
_CefcFanCoolingCapacity_Object=MibTableColumn
cefcFanCoolingCapacity=_CefcFanCoolingCapacity_Object((1,3,6,1,4,1,9,9,117,1,7,2,1,1),_CefcFanCoolingCapacity_Type())
cefcFanCoolingCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcFanCoolingCapacity.setStatus(_B)
_CefcFanCoolingCapacityUnit_Type=FRUCoolingUnit
_CefcFanCoolingCapacityUnit_Object=MibTableColumn
cefcFanCoolingCapacityUnit=_CefcFanCoolingCapacityUnit_Object((1,3,6,1,4,1,9,9,117,1,7,2,1,2),_CefcFanCoolingCapacityUnit_Type())
cefcFanCoolingCapacityUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcFanCoolingCapacityUnit.setStatus(_B)
_CefcModuleCoolingTable_Object=MibTable
cefcModuleCoolingTable=_CefcModuleCoolingTable_Object((1,3,6,1,4,1,9,9,117,1,7,3))
if mibBuilder.loadTexts:cefcModuleCoolingTable.setStatus(_B)
_CefcModuleCoolingEntry_Object=MibTableRow
cefcModuleCoolingEntry=_CefcModuleCoolingEntry_Object((1,3,6,1,4,1,9,9,117,1,7,3,1))
cefcModuleCoolingEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cefcModuleCoolingEntry.setStatus(_B)
_CefcModuleCooling_Type=Unsigned32
_CefcModuleCooling_Object=MibTableColumn
cefcModuleCooling=_CefcModuleCooling_Object((1,3,6,1,4,1,9,9,117,1,7,3,1,1),_CefcModuleCooling_Type())
cefcModuleCooling.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcModuleCooling.setStatus(_B)
_CefcModuleCoolingUnit_Type=FRUCoolingUnit
_CefcModuleCoolingUnit_Object=MibTableColumn
cefcModuleCoolingUnit=_CefcModuleCoolingUnit_Object((1,3,6,1,4,1,9,9,117,1,7,3,1,2),_CefcModuleCoolingUnit_Type())
cefcModuleCoolingUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcModuleCoolingUnit.setStatus(_B)
_CefcFanCoolingCapTable_Object=MibTable
cefcFanCoolingCapTable=_CefcFanCoolingCapTable_Object((1,3,6,1,4,1,9,9,117,1,7,4))
if mibBuilder.loadTexts:cefcFanCoolingCapTable.setStatus(_B)
_CefcFanCoolingCapEntry_Object=MibTableRow
cefcFanCoolingCapEntry=_CefcFanCoolingCapEntry_Object((1,3,6,1,4,1,9,9,117,1,7,4,1))
cefcFanCoolingCapEntry.setIndexNames((0,_D,_E),(0,_A,_AC))
if mibBuilder.loadTexts:cefcFanCoolingCapEntry.setStatus(_B)
class _CefcFanCoolingCapIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_CefcFanCoolingCapIndex_Type.__name__=_A7
_CefcFanCoolingCapIndex_Object=MibTableColumn
cefcFanCoolingCapIndex=_CefcFanCoolingCapIndex_Object((1,3,6,1,4,1,9,9,117,1,7,4,1,1),_CefcFanCoolingCapIndex_Type())
cefcFanCoolingCapIndex.setMaxAccess(_k)
if mibBuilder.loadTexts:cefcFanCoolingCapIndex.setStatus(_B)
_CefcFanCoolingCapModeDescr_Type=SnmpAdminString
_CefcFanCoolingCapModeDescr_Object=MibTableColumn
cefcFanCoolingCapModeDescr=_CefcFanCoolingCapModeDescr_Object((1,3,6,1,4,1,9,9,117,1,7,4,1,2),_CefcFanCoolingCapModeDescr_Type())
cefcFanCoolingCapModeDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcFanCoolingCapModeDescr.setStatus(_B)
_CefcFanCoolingCapCapacity_Type=Unsigned32
_CefcFanCoolingCapCapacity_Object=MibTableColumn
cefcFanCoolingCapCapacity=_CefcFanCoolingCapCapacity_Object((1,3,6,1,4,1,9,9,117,1,7,4,1,3),_CefcFanCoolingCapCapacity_Type())
cefcFanCoolingCapCapacity.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcFanCoolingCapCapacity.setStatus(_B)
_CefcFanCoolingCapCurrent_Type=FRUCurrentType
_CefcFanCoolingCapCurrent_Object=MibTableColumn
cefcFanCoolingCapCurrent=_CefcFanCoolingCapCurrent_Object((1,3,6,1,4,1,9,9,117,1,7,4,1,4),_CefcFanCoolingCapCurrent_Type())
cefcFanCoolingCapCurrent.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcFanCoolingCapCurrent.setStatus(_B)
_CefcFanCoolingCapCapacityUnit_Type=FRUCoolingUnit
_CefcFanCoolingCapCapacityUnit_Object=MibTableColumn
cefcFanCoolingCapCapacityUnit=_CefcFanCoolingCapCapacityUnit_Object((1,3,6,1,4,1,9,9,117,1,7,4,1,5),_CefcFanCoolingCapCapacityUnit_Type())
cefcFanCoolingCapCapacityUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcFanCoolingCapCapacityUnit.setStatus(_B)
_CefcConnector_ObjectIdentity=ObjectIdentity
cefcConnector=_CefcConnector_ObjectIdentity((1,3,6,1,4,1,9,9,117,1,8))
_CefcConnectorRatingTable_Object=MibTable
cefcConnectorRatingTable=_CefcConnectorRatingTable_Object((1,3,6,1,4,1,9,9,117,1,8,1))
if mibBuilder.loadTexts:cefcConnectorRatingTable.setStatus(_B)
_CefcConnectorRatingEntry_Object=MibTableRow
cefcConnectorRatingEntry=_CefcConnectorRatingEntry_Object((1,3,6,1,4,1,9,9,117,1,8,1,1))
cefcConnectorRatingEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cefcConnectorRatingEntry.setStatus(_B)
_CefcConnectorRating_Type=FRUCurrentType
_CefcConnectorRating_Object=MibTableColumn
cefcConnectorRating=_CefcConnectorRating_Object((1,3,6,1,4,1,9,9,117,1,8,1,1,1),_CefcConnectorRating_Type())
cefcConnectorRating.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcConnectorRating.setStatus(_B)
_CefcModulePowerConsumptionTable_Object=MibTable
cefcModulePowerConsumptionTable=_CefcModulePowerConsumptionTable_Object((1,3,6,1,4,1,9,9,117,1,8,2))
if mibBuilder.loadTexts:cefcModulePowerConsumptionTable.setStatus(_B)
_CefcModulePowerConsumptionEntry_Object=MibTableRow
cefcModulePowerConsumptionEntry=_CefcModulePowerConsumptionEntry_Object((1,3,6,1,4,1,9,9,117,1,8,2,1))
cefcModulePowerConsumptionEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:cefcModulePowerConsumptionEntry.setStatus(_B)
_CefcModulePowerConsumption_Type=FRUCurrentType
_CefcModulePowerConsumption_Object=MibTableColumn
cefcModulePowerConsumption=_CefcModulePowerConsumption_Object((1,3,6,1,4,1,9,9,117,1,8,2,1,1),_CefcModulePowerConsumption_Type())
cefcModulePowerConsumption.setMaxAccess(_C)
if mibBuilder.loadTexts:cefcModulePowerConsumption.setStatus(_B)
_CefcFRUMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
cefcFRUMIBNotificationPrefix=_CefcFRUMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,117,2))
_CefcMIBNotifications_ObjectIdentity=ObjectIdentity
cefcMIBNotifications=_CefcMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,117,2,0))
_CefcMIBConformance_ObjectIdentity=ObjectIdentity
cefcMIBConformance=_CefcMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,117,3))
_CefcMIBCompliances_ObjectIdentity=ObjectIdentity
cefcMIBCompliances=_CefcMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,117,3,1))
_CefcMIBGroups_ObjectIdentity=ObjectIdentity
cefcMIBGroups=_CefcMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,117,3,2))
cefcMIBPowerModeGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,1))
cefcMIBPowerModeGroup.setObjects(*((_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG)))
if mibBuilder.loadTexts:cefcMIBPowerModeGroup.setStatus(_B)
cefcMIBPowerFRUControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,2))
cefcMIBPowerFRUControlGroup.setObjects(*((_A,_l),(_A,_m),(_A,_AH)))
if mibBuilder.loadTexts:cefcMIBPowerFRUControlGroup.setStatus(_B)
cefcMIBModuleGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,3))
cefcMIBModuleGroup.setObjects(*((_A,_AI),(_A,_n),(_A,_AJ),(_A,_o)))
if mibBuilder.loadTexts:cefcMIBModuleGroup.setStatus(_B)
cefcMIBInLinePowerControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,4))
cefcMIBInLinePowerControlGroup.setObjects((_A,_AK))
if mibBuilder.loadTexts:cefcMIBInLinePowerControlGroup.setStatus(_I)
cefcMIBNotificationEnablesGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,5))
cefcMIBNotificationEnablesGroup.setObjects((_A,_AL))
if mibBuilder.loadTexts:cefcMIBNotificationEnablesGroup.setStatus(_B)
cefcModuleGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,7))
cefcModuleGroupRev1.setObjects(*((_A,_AM),(_A,_AN)))
if mibBuilder.loadTexts:cefcModuleGroupRev1.setStatus(_B)
cefcMIBPowerFRUValueGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,8))
cefcMIBPowerFRUValueGroup.setObjects(*((_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR)))
if mibBuilder.loadTexts:cefcMIBPowerFRUValueGroup.setStatus(_B)
cefcMIBFanTrayStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,9))
cefcMIBFanTrayStatusGroup.setObjects((_A,_p))
if mibBuilder.loadTexts:cefcMIBFanTrayStatusGroup.setStatus(_B)
cefcMIBPhysicalGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,10))
cefcMIBPhysicalGroup.setObjects((_A,_q))
if mibBuilder.loadTexts:cefcMIBPhysicalGroup.setStatus(_B)
cefcMIBPowerOperModeGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,12))
cefcMIBPowerOperModeGroup.setObjects((_A,_AS))
if mibBuilder.loadTexts:cefcMIBPowerOperModeGroup.setStatus(_B)
cefcMIBInLinePowerControlGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,13))
cefcMIBInLinePowerControlGroupRev1.setObjects((_A,_AT))
if mibBuilder.loadTexts:cefcMIBInLinePowerControlGroupRev1.setStatus(_B)
cefcModuleExtGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,14))
cefcModuleExtGroup.setObjects(*((_A,_AU),(_A,_AV)))
if mibBuilder.loadTexts:cefcModuleExtGroup.setStatus(_B)
cefcIntelliModuleGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,15))
cefcIntelliModuleGroup.setObjects(*((_A,_AW),(_A,_AX)))
if mibBuilder.loadTexts:cefcIntelliModuleGroup.setStatus(_B)
cefcPowerCapacityGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,16))
cefcPowerCapacityGroup.setObjects(*((_A,_AY),(_A,_r),(_A,_AZ)))
if mibBuilder.loadTexts:cefcPowerCapacityGroup.setStatus(_B)
cefcCoolingGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,17))
cefcCoolingGroup.setObjects(*((_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:cefcCoolingGroup.setStatus(_I)
cefcConnectorRatingGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,18))
cefcConnectorRatingGroup.setObjects(*((_A,_Aa),(_A,_Ab)))
if mibBuilder.loadTexts:cefcConnectorRatingGroup.setStatus(_B)
cefcMIBNotificationEnablesGroup2=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,19))
cefcMIBNotificationEnablesGroup2.setObjects((_A,_Ac))
if mibBuilder.loadTexts:cefcMIBNotificationEnablesGroup2.setStatus(_B)
cefcMIBInLinePowerCurrentGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,21))
cefcMIBInLinePowerCurrentGroup.setObjects((_A,_Ad))
if mibBuilder.loadTexts:cefcMIBInLinePowerCurrentGroup.setStatus(_B)
cefcMIBPowerRedundancyInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,22))
cefcMIBPowerRedundancyInfoGroup.setObjects((_A,_Ae))
if mibBuilder.loadTexts:cefcMIBPowerRedundancyInfoGroup.setStatus(_B)
cefcFanCoolingCapGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,23))
cefcFanCoolingCapGroup.setObjects(*((_A,_Af),(_A,_Ag),(_A,_Ah)))
if mibBuilder.loadTexts:cefcFanCoolingCapGroup.setStatus(_B)
cefcMIBModuleLocalSwitchingGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,24))
cefcMIBModuleLocalSwitchingGroup.setObjects((_A,_Ai))
if mibBuilder.loadTexts:cefcMIBModuleLocalSwitchingGroup.setStatus(_B)
cefcFRUPowerRealTimeStatusGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,25))
cefcFRUPowerRealTimeStatusGroup.setObjects((_A,_Aj))
if mibBuilder.loadTexts:cefcFRUPowerRealTimeStatusGroup.setStatus(_B)
cefcFRUPowerCapabilityGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,26))
cefcFRUPowerCapabilityGroup.setObjects((_A,_Ak))
if mibBuilder.loadTexts:cefcFRUPowerCapabilityGroup.setStatus(_B)
cefcFRUCoolingUnitGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,27))
cefcFRUCoolingUnitGroup.setObjects(*((_A,_Al),(_A,_Am)))
if mibBuilder.loadTexts:cefcFRUCoolingUnitGroup.setStatus(_B)
cefcFRUFanCoolingUnitGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,28))
cefcFRUFanCoolingUnitGroup.setObjects(*((_A,_An),(_A,_Ao)))
if mibBuilder.loadTexts:cefcFRUFanCoolingUnitGroup.setStatus(_B)
cefcCoolingGroup2=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,29))
cefcCoolingGroup2.setObjects(*((_A,_s),(_A,_u)))
if mibBuilder.loadTexts:cefcCoolingGroup2.setStatus(_B)
cefcFanCoolingGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,30))
cefcFanCoolingGroup.setObjects((_A,_t))
if mibBuilder.loadTexts:cefcFanCoolingGroup.setStatus(_B)
cefcFanDirectionGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,31))
cefcFanDirectionGroup.setObjects((_A,_Ap))
if mibBuilder.loadTexts:cefcFanDirectionGroup.setStatus(_B)
cefcFanSpeedGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,32))
cefcFanSpeedGroup.setObjects(*((_A,_Aq),(_A,_Ar)))
if mibBuilder.loadTexts:cefcFanSpeedGroup.setStatus(_B)
cefcPowerSupplyActualGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,33))
cefcPowerSupplyActualGroup.setObjects(*((_A,_As),(_A,_At)))
if mibBuilder.loadTexts:cefcPowerSupplyActualGroup.setStatus(_B)
cefcVmModuleGroup=ObjectGroup((1,3,6,1,4,1,9,9,117,3,2,34))
cefcVmModuleGroup.setObjects(*((_A,_v),(_A,_w)))
if mibBuilder.loadTexts:cefcVmModuleGroup.setStatus(_B)
cefcModuleStatusChange=NotificationType((1,3,6,1,4,1,9,9,117,2,0,1))
cefcModuleStatusChange.setObjects(*((_A,_n),(_A,_o)))
if mibBuilder.loadTexts:cefcModuleStatusChange.setStatus(_B)
cefcPowerStatusChange=NotificationType((1,3,6,1,4,1,9,9,117,2,0,2))
cefcPowerStatusChange.setObjects(*((_A,_m),(_A,_l)))
if mibBuilder.loadTexts:cefcPowerStatusChange.setStatus(_B)
cefcFRUInserted=NotificationType((1,3,6,1,4,1,9,9,117,2,0,3))
cefcFRUInserted.setObjects((_D,_f))
if mibBuilder.loadTexts:cefcFRUInserted.setStatus(_B)
cefcFRURemoved=NotificationType((1,3,6,1,4,1,9,9,117,2,0,4))
cefcFRURemoved.setObjects((_D,_f))
if mibBuilder.loadTexts:cefcFRURemoved.setStatus(_B)
cefcUnrecognizedFRU=NotificationType((1,3,6,1,4,1,9,9,117,2,0,5))
cefcUnrecognizedFRU.setObjects(*((_D,_A5),(_D,_A6),(_D,_h),(_D,_g),(_A,_q)))
if mibBuilder.loadTexts:cefcUnrecognizedFRU.setStatus(_B)
cefcFanTrayStatusChange=NotificationType((1,3,6,1,4,1,9,9,117,2,0,6))
cefcFanTrayStatusChange.setObjects((_A,_p))
if mibBuilder.loadTexts:cefcFanTrayStatusChange.setStatus(_B)
cefcPowerSupplyOutputChange=NotificationType((1,3,6,1,4,1,9,9,117,2,0,7))
cefcPowerSupplyOutputChange.setObjects(*((_D,_h),(_D,_g),(_A,_r)))
if mibBuilder.loadTexts:cefcPowerSupplyOutputChange.setStatus(_B)
cefcVmModuleStatusChangeNotif=NotificationType((1,3,6,1,4,1,9,9,117,2,0,8))
cefcVmModuleStatusChangeNotif.setObjects(*((_A,_v),(_A,_w)))
if mibBuilder.loadTexts:cefcVmModuleStatusChangeNotif.setStatus(_B)
cefcMgmtNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,9,117,3,2,6))
cefcMgmtNotificationsGroup.setObjects(*((_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax)))
if mibBuilder.loadTexts:cefcMgmtNotificationsGroup.setStatus(_B)
cefcMgmtNotificationsGroup2=NotificationGroup((1,3,6,1,4,1,9,9,117,3,2,11))
cefcMgmtNotificationsGroup2.setObjects(*((_A,_Ay),(_A,_Az)))
if mibBuilder.loadTexts:cefcMgmtNotificationsGroup2.setStatus(_B)
cefcMgmtNotificationsGroup3=NotificationGroup((1,3,6,1,4,1,9,9,117,3,2,20))
cefcMgmtNotificationsGroup3.setObjects((_A,_A_))
if mibBuilder.loadTexts:cefcMgmtNotificationsGroup3.setStatus(_B)
cefcVmModuleNotifsGroup=NotificationGroup((1,3,6,1,4,1,9,9,117,3,2,35))
cefcVmModuleNotifsGroup.setObjects((_A,_B0))
if mibBuilder.loadTexts:cefcVmModuleNotifsGroup.setStatus(_B)
cefcMIBPowerCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,117,3,1,1))
cefcMIBPowerCompliance.setObjects(*((_A,_G),(_A,_H)))
if mibBuilder.loadTexts:cefcMIBPowerCompliance.setStatus('obsolete')
cefcMIBPowerCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,117,3,1,2))
cefcMIBPowerCompliance2.setObjects(*((_A,_G),(_A,_J),(_A,_H),(_A,_K),(_A,_X),(_A,_L)))
if mibBuilder.loadTexts:cefcMIBPowerCompliance2.setStatus(_I)
cefcMIBPowerCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,117,3,1,3))
cefcMIBPowerCompliance3.setObjects(*((_A,_G),(_A,_J),(_A,_H),(_A,_K),(_A,_X),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:cefcMIBPowerCompliance3.setStatus(_I)
cefcMIBPowerCompliance4=ModuleCompliance((1,3,6,1,4,1,9,9,117,3,1,4))
cefcMIBPowerCompliance4.setObjects(*((_A,_G),(_A,_J),(_A,_H),(_A,_K),(_A,_X),(_A,_L),(_A,_M),(_A,_O)))
if mibBuilder.loadTexts:cefcMIBPowerCompliance4.setStatus(_I)
cefcMIBPowerCompliance5=ModuleCompliance((1,3,6,1,4,1,9,9,117,3,1,5))
cefcMIBPowerCompliance5.setObjects(*((_A,_G),(_A,_J),(_A,_Q),(_A,_H),(_A,_K),(_A,_X),(_A,_L),(_A,_M),(_A,_O),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:cefcMIBPowerCompliance5.setStatus(_I)
cefcMIBPowerCompliance6=ModuleCompliance((1,3,6,1,4,1,9,9,117,3,1,6))
cefcMIBPowerCompliance6.setObjects(*((_A,_G),(_A,_J),(_A,_H),(_A,_K),(_A,_T),(_A,_L),(_A,_M),(_A,_O),(_A,_R),(_A,_S),(_A,_Q),(_A,_U),(_A,_V),(_A,_W)))
if mibBuilder.loadTexts:cefcMIBPowerCompliance6.setStatus(_B)
cefcMIBPowerCompliance7=ModuleCompliance((1,3,6,1,4,1,9,9,117,3,1,7))
cefcMIBPowerCompliance7.setObjects(*((_A,_G),(_A,_J),(_A,_H),(_A,_K),(_A,_T),(_A,_L),(_A,_M),(_A,_O),(_A,_R),(_A,_S),(_A,_Q),(_A,_U),(_A,_V),(_A,_W),(_A,_Y),(_A,_x),(_A,_Z),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:cefcMIBPowerCompliance7.setStatus(_I)
cefcMIBPowerCompliance8=ModuleCompliance((1,3,6,1,4,1,9,9,117,3,1,8))
cefcMIBPowerCompliance8.setObjects(*((_A,_G),(_A,_J),(_A,_H),(_A,_K),(_A,_T),(_A,_L),(_A,_M),(_A,_O),(_A,_R),(_A,_S),(_A,_Q),(_A,_U),(_A,_V),(_A,_W),(_A,_Y),(_A,_x),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:cefcMIBPowerCompliance8.setStatus(_I)
cefcMIBPowerCompliance9=ModuleCompliance((1,3,6,1,4,1,9,9,117,3,1,9))
cefcMIBPowerCompliance9.setObjects(*((_A,_G),(_A,_J),(_A,_H),(_A,_K),(_A,_T),(_A,_L),(_A,_M),(_A,_O),(_A,_R),(_A,_S),(_A,_Q),(_A,_U),(_A,_V),(_A,_W),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4)))
if mibBuilder.loadTexts:cefcMIBPowerCompliance9.setStatus(_I)
cefcMIBPowerCompliance10=ModuleCompliance((1,3,6,1,4,1,9,9,117,3,1,10))
cefcMIBPowerCompliance10.setObjects(*((_A,_G),(_A,_J),(_A,_H),(_A,_K),(_A,_T),(_A,_L),(_A,_M),(_A,_O),(_A,_R),(_A,_S),(_A,_Q),(_A,_U),(_A,_V),(_A,_W),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_B1),(_A,_B2),(_A,_B3),(_A,_B4),(_A,_B5)))
if mibBuilder.loadTexts:cefcMIBPowerCompliance10.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'PowerRedundancyType':PowerRedundancyType,'PowerAdminType':PowerAdminType,'PowerOperType':PowerOperType,'FRUCurrentType':FRUCurrentType,'ModuleAdminType':ModuleAdminType,'ModuleOperType':ModuleOperType,'ModuleResetReasonType':ModuleResetReasonType,'FRUTimeSeconds':FRUTimeSeconds,'FRUCoolingUnit':FRUCoolingUnit,'CefcPercentOrMinusOne':CefcPercentOrMinusOne,'CefcVmModuleOperType':CefcVmModuleOperType,'ciscoEntityFRUControlMIB':ciscoEntityFRUControlMIB,'cefcMIBObjects':cefcMIBObjects,'cefcFRUPower':cefcFRUPower,'cefcFRUPowerSupplyGroupTable':cefcFRUPowerSupplyGroupTable,'cefcFRUPowerSupplyGroupEntry':cefcFRUPowerSupplyGroupEntry,_AD:cefcPowerRedundancyMode,_AE:cefcPowerUnits,_AF:cefcTotalAvailableCurrent,_AG:cefcTotalDrawnCurrent,_AS:cefcPowerRedundancyOperMode,_Ae:cefcPowerNonRedundantReason,_Ad:cefcTotalDrawnInlineCurrent,'cefcFRUPowerStatusTable':cefcFRUPowerStatusTable,'cefcFRUPowerStatusEntry':cefcFRUPowerStatusEntry,_l:cefcFRUPowerAdminStatus,_m:cefcFRUPowerOperStatus,_AH:cefcFRUCurrent,_Ak:cefcFRUPowerCapability,_Aj:cefcFRURealTimeCurrent,_AK:cefcMaxDefaultInLinePower,'cefcFRUPowerSupplyValueTable':cefcFRUPowerSupplyValueTable,'cefcFRUPowerSupplyValueEntry':cefcFRUPowerSupplyValueEntry,_AO:cefcFRUTotalSystemCurrent,_AP:cefcFRUDrawnSystemCurrent,_AQ:cefcFRUTotalInlineCurrent,_AR:cefcFRUDrawnInlineCurrent,_As:cefcFRUActualInputCurrent,_At:cefcFRUActualOutputCurrent,_AT:cefcMaxDefaultHighInLinePower,'cefcModule':cefcModule,'cefcModuleTable':cefcModuleTable,'cefcModuleEntry':cefcModuleEntry,_AI:cefcModuleAdminStatus,_n:cefcModuleOperStatus,_AJ:cefcModuleResetReason,_o:cefcModuleStatusLastChangeTime,_AM:cefcModuleLastClearConfigTime,_AN:cefcModuleResetReasonDescription,_AU:cefcModuleStateChangeReasonDescr,_AV:cefcModuleUpTime,_v:cefcVmModuleOperStatus,_w:cefcVmModuleStatusLastChangeTime,'cefcIntelliModuleTable':cefcIntelliModuleTable,'cefcIntelliModuleEntry':cefcIntelliModuleEntry,_AW:cefcIntelliModuleIPAddrType,_AX:cefcIntelliModuleIPAddr,'cefcModuleLocalSwitchingTable':cefcModuleLocalSwitchingTable,'cefcModuleLocalSwitchingEntry':cefcModuleLocalSwitchingEntry,_Ai:cefcModuleLocalSwitchingMode,'cefcMIBNotificationEnables':cefcMIBNotificationEnables,_AL:cefcMIBEnableStatusNotification,_Ac:cefcEnablePSOutputChangeNotif,'cefcFRUFan':cefcFRUFan,'cefcFanTrayStatusTable':cefcFanTrayStatusTable,'cefcFanTrayStatusEntry':cefcFanTrayStatusEntry,_p:cefcFanTrayOperStatus,_Ap:cefcFanTrayDirection,'cefcFanTable':cefcFanTable,'cefcFanEntry':cefcFanEntry,_Aq:cefcFanSpeed,_Ar:cefcFanSpeedPercent,'cefcPhysical':cefcPhysical,'cefcPhysicalTable':cefcPhysicalTable,'cefcPhysicalEntry':cefcPhysicalEntry,_q:cefcPhysicalStatus,'cefcPowerCapacity':cefcPowerCapacity,'cefcPowerSupplyInputTable':cefcPowerSupplyInputTable,'cefcPowerSupplyInputEntry':cefcPowerSupplyInputEntry,_AA:cefcPowerSupplyInputIndex,_AY:cefcPowerSupplyInputType,'cefcPowerSupplyOutputTable':cefcPowerSupplyOutputTable,'cefcPowerSupplyOutputEntry':cefcPowerSupplyOutputEntry,_AB:cefcPSOutputModeIndex,_r:cefcPSOutputModeCurrent,_AZ:cefcPSOutputModeInOperation,'cefcCooling':cefcCooling,'cefcChassisCoolingTable':cefcChassisCoolingTable,'cefcChassisCoolingEntry':cefcChassisCoolingEntry,_s:cefcChassisPerSlotCoolingCap,_Al:cefcChassisPerSlotCoolingUnit,'cefcFanCoolingTable':cefcFanCoolingTable,'cefcFanCoolingEntry':cefcFanCoolingEntry,_t:cefcFanCoolingCapacity,_An:cefcFanCoolingCapacityUnit,'cefcModuleCoolingTable':cefcModuleCoolingTable,'cefcModuleCoolingEntry':cefcModuleCoolingEntry,_u:cefcModuleCooling,_Am:cefcModuleCoolingUnit,'cefcFanCoolingCapTable':cefcFanCoolingCapTable,'cefcFanCoolingCapEntry':cefcFanCoolingCapEntry,_AC:cefcFanCoolingCapIndex,_Af:cefcFanCoolingCapModeDescr,_Ag:cefcFanCoolingCapCapacity,_Ah:cefcFanCoolingCapCurrent,_Ao:cefcFanCoolingCapCapacityUnit,'cefcConnector':cefcConnector,'cefcConnectorRatingTable':cefcConnectorRatingTable,'cefcConnectorRatingEntry':cefcConnectorRatingEntry,_Aa:cefcConnectorRating,'cefcModulePowerConsumptionTable':cefcModulePowerConsumptionTable,'cefcModulePowerConsumptionEntry':cefcModulePowerConsumptionEntry,_Ab:cefcModulePowerConsumption,'cefcFRUMIBNotificationPrefix':cefcFRUMIBNotificationPrefix,'cefcMIBNotifications':cefcMIBNotifications,_Au:cefcModuleStatusChange,_Av:cefcPowerStatusChange,_Aw:cefcFRUInserted,_Ax:cefcFRURemoved,_Ay:cefcUnrecognizedFRU,_Az:cefcFanTrayStatusChange,_A_:cefcPowerSupplyOutputChange,_B0:cefcVmModuleStatusChangeNotif,'cefcMIBConformance':cefcMIBConformance,'cefcMIBCompliances':cefcMIBCompliances,'cefcMIBPowerCompliance':cefcMIBPowerCompliance,'cefcMIBPowerCompliance2':cefcMIBPowerCompliance2,'cefcMIBPowerCompliance3':cefcMIBPowerCompliance3,'cefcMIBPowerCompliance4':cefcMIBPowerCompliance4,'cefcMIBPowerCompliance5':cefcMIBPowerCompliance5,'cefcMIBPowerCompliance6':cefcMIBPowerCompliance6,'cefcMIBPowerCompliance7':cefcMIBPowerCompliance7,'cefcMIBPowerCompliance8':cefcMIBPowerCompliance8,'cefcMIBPowerCompliance9':cefcMIBPowerCompliance9,'cefcMIBPowerCompliance10':cefcMIBPowerCompliance10,'cefcMIBGroups':cefcMIBGroups,_G:cefcMIBPowerModeGroup,_H:cefcMIBPowerFRUControlGroup,_K:cefcMIBModuleGroup,_X:cefcMIBInLinePowerControlGroup,_L:cefcMIBNotificationEnablesGroup,_J:cefcMgmtNotificationsGroup,_M:cefcModuleGroupRev1,_O:cefcMIBPowerFRUValueGroup,_R:cefcMIBFanTrayStatusGroup,_S:cefcMIBPhysicalGroup,_Q:cefcMgmtNotificationsGroup2,_U:cefcMIBPowerOperModeGroup,_T:cefcMIBInLinePowerControlGroupRev1,_V:cefcModuleExtGroup,_W:cefcIntelliModuleGroup,_Y:cefcPowerCapacityGroup,_x:cefcCoolingGroup,_Z:cefcConnectorRatingGroup,_a:cefcMIBNotificationEnablesGroup2,_b:cefcMgmtNotificationsGroup3,_c:cefcMIBInLinePowerCurrentGroup,_d:cefcMIBPowerRedundancyInfoGroup,_e:cefcFanCoolingCapGroup,_y:cefcMIBModuleLocalSwitchingGroup,_z:cefcFRUPowerRealTimeStatusGroup,_A0:cefcFRUPowerCapabilityGroup,_A1:cefcFRUCoolingUnitGroup,_A2:cefcFRUFanCoolingUnitGroup,_A3:cefcCoolingGroup2,_A4:cefcFanCoolingGroup,_B1:cefcFanDirectionGroup,_B2:cefcFanSpeedGroup,_B3:cefcPowerSupplyActualGroup,_B4:cefcVmModuleGroup,_B5:cefcVmModuleNotifsGroup})