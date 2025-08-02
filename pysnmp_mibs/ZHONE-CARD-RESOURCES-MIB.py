_A9='znidBatteryStatusNotification'
_A8='zhoneTrapProcessorUsage'
_A7='zhoneTrapCardMemStatus'
_A6='zhoneMxkAlarmInputTrap'
_A5='zhoneExternalAlarmTrap'
_A4='zrgBatteryRelayStatus'
_A3='zhoneExternalRelayNormalState'
_A2='standbyServiceSlot'
_A1='standbyServiceShelf'
_A0='cardServiceStatus'
_z='cardPweTimingMode'
_y='cardProcessorHighUsage'
_x='cardProcessorLowUsage'
_w='cardProcessorFrameworkUsage'
_v='cardProcessorServicesUsage'
_u='cardProcessorIdle'
_t='cardTotalMem'
_s='cardAvailMem'
_r='cardPeakMemUsage'
_q='cardSwStatus'
_p='cardSwAdmin'
_o='cardSwUpgradeVers'
_n='cardSwRunningVers'
_m='cardInterfaceType'
_l='cardPortStatus'
_k='cardProcessorType'
_j='cardUpTime'
_i='cardAdminStatsEnable'
_h='cardOperStatus'
_g='cardAdminStatus'
_f='cardPostResults'
_e='cardMfgBootRevision'
_d='cardMfgRevisionCode'
_c='cardMfgCLEICode'
_b='cardMfgSerialNumber'
_a='cardZhoneType'
_Z='cardIdentification'
_Y='cardRuntimeEntry'
_X='cardSoftwareEntry'
_W='deprecated'
_V='maintenance'
_U='disable'
_T='ZhoneAdminString'
_S='znidSerialNumber'
_R='znidBatteryStatus'
_Q='cardMemStatus'
_P='cardProcessorUsage'
_O='zhoneExternalRelayId'
_N='Bits'
_M='zhoneExternalRelayState'
_L='accessible-for-notify'
_K='cardServiceInstance'
_J='cardServiceId'
_I='zhoneSlotIndex'
_H='zhoneShelfIndex'
_G='zhoneExternalRelayName'
_F='Zhone'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='ZHONE-CARD-RESOURCES-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_N,'Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
zhoneCard,zhoneModules,zhoneShelfIndex,zhoneSlotIndex=mibBuilder.importSymbols(_F,'zhoneCard','zhoneModules',_H,_I)
ZhoneAdminString,ZhoneCardType,ZhoneDiagAction=mibBuilder.importSymbols('Zhone-TC',_T,'ZhoneCardType','ZhoneDiagAction')
zhoneCardResourcesModule=ModuleIdentity((1,3,6,1,4,1,5504,6,4))
if mibBuilder.loadTexts:zhoneCardResourcesModule.setRevisions(('2011-10-24 14:47','2011-10-12 12:44','2011-08-24 15:33','2010-07-13 10:41','2009-05-12 07:58','2009-04-24 08:51','2008-10-22 03:11','2007-08-15 17:30','2006-10-17 15:03','2006-09-28 11:42','2005-10-11 16:47','2005-10-05 11:16','2005-05-23 14:22','2004-04-15 13:27','2003-12-22 12:14','2003-11-21 15:18','2002-10-29 15:30','2002-10-24 17:24','2002-07-09 11:27','2002-06-07 17:38','2002-05-24 12:58','2002-03-22 14:55','2001-11-16 18:11','2001-10-23 11:10','2001-10-09 10:00','2001-10-08 13:36','2001-10-04 12:26','2001-09-17 16:50','2001-09-07 16:40','2001-09-06 16:03','2001-09-05 20:38','2001-08-29 11:23','2001-08-09 10:43','2001-07-26 10:47','2001-07-20 13:20','2000-09-12 10:59','2000-09-20 11:00','2000-11-11 10:59','2000-11-21 18:31','2000-12-01 12:18','2000-12-18 19:11','2001-01-22 14:56','2001-03-27 10:29','2001-04-06 14:25','2001-04-27 11:49','2001-05-24 13:15'))
class Kbytes(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
class ZhoneServiceId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28)));namedValues=NamedValues(*(('dspResource',1),('numberService',2),('tadService',3),('aal2Resource',4),('ctrpCallResource',5),('callControlResource',6),('mprrResource',7),('mamaResource',8),('raFtdResource',9),('voiceCall',10),('shelfControllerService',11),('snmpMasterAgent',12),('trapService',13),('informationServices',14),('lineResource',15),('ifCfgMgrResource',16),('logServer',17),('cardServer',18),('dhcpServer',19),('filterUpdate',20),('ringGenerator',21),('zhoneRouteTableService',22),('pppResourceProvider',23),('rootDirectoryService',24),('cssService',25),('sipResource',26),('mgcpResource',27),('npRedundantServer',28)))
_CardResourceTable_Object=MibTable
cardResourceTable=_CardResourceTable_Object((1,3,6,1,4,1,5504,3,3,1))
if mibBuilder.loadTexts:cardResourceTable.setStatus(_A)
_CardResourceEntry_Object=MibTableRow
cardResourceEntry=_CardResourceEntry_Object((1,3,6,1,4,1,5504,3,3,1,1))
cardResourceEntry.setIndexNames((0,_F,_H),(0,_F,_I))
if mibBuilder.loadTexts:cardResourceEntry.setStatus(_A)
_CardIdentification_Type=ZhoneAdminString
_CardIdentification_Object=MibTableColumn
cardIdentification=_CardIdentification_Object((1,3,6,1,4,1,5504,3,3,1,1,1),_CardIdentification_Type())
cardIdentification.setMaxAccess(_C)
if mibBuilder.loadTexts:cardIdentification.setStatus(_A)
_CardZhoneType_Type=ZhoneCardType
_CardZhoneType_Object=MibTableColumn
cardZhoneType=_CardZhoneType_Object((1,3,6,1,4,1,5504,3,3,1,1,2),_CardZhoneType_Type())
cardZhoneType.setMaxAccess(_C)
if mibBuilder.loadTexts:cardZhoneType.setStatus(_A)
_CardMfgSerialNumber_Type=ZhoneAdminString
_CardMfgSerialNumber_Object=MibTableColumn
cardMfgSerialNumber=_CardMfgSerialNumber_Object((1,3,6,1,4,1,5504,3,3,1,1,3),_CardMfgSerialNumber_Type())
cardMfgSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cardMfgSerialNumber.setStatus(_A)
_CardMfgCLEICode_Type=ZhoneAdminString
_CardMfgCLEICode_Object=MibTableColumn
cardMfgCLEICode=_CardMfgCLEICode_Object((1,3,6,1,4,1,5504,3,3,1,1,4),_CardMfgCLEICode_Type())
cardMfgCLEICode.setMaxAccess(_C)
if mibBuilder.loadTexts:cardMfgCLEICode.setStatus(_A)
_CardMfgRevisionCode_Type=ZhoneAdminString
_CardMfgRevisionCode_Object=MibTableColumn
cardMfgRevisionCode=_CardMfgRevisionCode_Object((1,3,6,1,4,1,5504,3,3,1,1,5),_CardMfgRevisionCode_Type())
cardMfgRevisionCode.setMaxAccess(_C)
if mibBuilder.loadTexts:cardMfgRevisionCode.setStatus(_A)
_CardMfgBootRevision_Type=ZhoneAdminString
_CardMfgBootRevision_Object=MibTableColumn
cardMfgBootRevision=_CardMfgBootRevision_Object((1,3,6,1,4,1,5504,3,3,1,1,6),_CardMfgBootRevision_Type())
cardMfgBootRevision.setMaxAccess(_C)
if mibBuilder.loadTexts:cardMfgBootRevision.setStatus(_A)
_CardPostResults_Type=ZhoneAdminString
_CardPostResults_Object=MibTableColumn
cardPostResults=_CardPostResults_Object((1,3,6,1,4,1,5504,3,3,1,1,7),_CardPostResults_Type())
cardPostResults.setMaxAccess(_C)
if mibBuilder.loadTexts:cardPostResults.setStatus(_A)
class _CardAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('operational',1),(_U,2),(_V,3),('warmreset',4),('reset',5)))
_CardAdminStatus_Type.__name__=_D
_CardAdminStatus_Object=MibTableColumn
cardAdminStatus=_CardAdminStatus_Object((1,3,6,1,4,1,5504,3,3,1,1,8),_CardAdminStatus_Type())
cardAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cardAdminStatus.setStatus(_A)
class _CardOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unknown',1),('operating',2),('nonoperating',3),(_V,4)))
_CardOperStatus_Type.__name__=_D
_CardOperStatus_Object=MibTableColumn
cardOperStatus=_CardOperStatus_Object((1,3,6,1,4,1,5504,3,3,1,1,9),_CardOperStatus_Type())
cardOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cardOperStatus.setStatus(_A)
class _CardAdminStatsEnable_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),(_U,2)))
_CardAdminStatsEnable_Type.__name__=_D
_CardAdminStatsEnable_Object=MibTableColumn
cardAdminStatsEnable=_CardAdminStatsEnable_Object((1,3,6,1,4,1,5504,3,3,1,1,10),_CardAdminStatsEnable_Type())
cardAdminStatsEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cardAdminStatsEnable.setStatus(_A)
_CardUpTime_Type=TimeTicks
_CardUpTime_Object=MibTableColumn
cardUpTime=_CardUpTime_Object((1,3,6,1,4,1,5504,3,3,1,1,11),_CardUpTime_Type())
cardUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cardUpTime.setStatus(_A)
_CardProcessorType_Type=ZhoneAdminString
_CardProcessorType_Object=MibTableColumn
cardProcessorType=_CardProcessorType_Object((1,3,6,1,4,1,5504,3,3,1,1,12),_CardProcessorType_Type())
cardProcessorType.setMaxAccess(_C)
if mibBuilder.loadTexts:cardProcessorType.setStatus(_A)
_CardPortStatus_Type=OctetString
_CardPortStatus_Object=MibTableColumn
cardPortStatus=_CardPortStatus_Object((1,3,6,1,4,1,5504,3,3,1,1,13),_CardPortStatus_Type())
cardPortStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cardPortStatus.setStatus(_A)
_CardInterfaceType_Type=ZhoneCardType
_CardInterfaceType_Object=MibTableColumn
cardInterfaceType=_CardInterfaceType_Object((1,3,6,1,4,1,5504,3,3,1,1,14),_CardInterfaceType_Type())
cardInterfaceType.setMaxAccess(_C)
if mibBuilder.loadTexts:cardInterfaceType.setStatus(_A)
class _CardAtmManualAal2bw_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CardAtmManualAal2bw_Type.__name__=_D
_CardAtmManualAal2bw_Object=MibTableColumn
cardAtmManualAal2bw=_CardAtmManualAal2bw_Object((1,3,6,1,4,1,5504,3,3,1,1,15),_CardAtmManualAal2bw_Type())
cardAtmManualAal2bw.setMaxAccess(_E)
if mibBuilder.loadTexts:cardAtmManualAal2bw.setStatus(_A)
class _CardAtmManualAal2h_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CardAtmManualAal2h_Type.__name__=_D
_CardAtmManualAal2h_Object=MibTableColumn
cardAtmManualAal2h=_CardAtmManualAal2h_Object((1,3,6,1,4,1,5504,3,3,1,1,16),_CardAtmManualAal2h_Type())
cardAtmManualAal2h.setMaxAccess(_E)
if mibBuilder.loadTexts:cardAtmManualAal2h.setStatus(_A)
class _CardLineVoltage_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('line-voltage-not-used',1),('line-voltage-60-volts',2),('line-voltage-68-volts',3),('line-voltage-95-volts',4),('line-voltage-100-volts',5),('line-voltage-110-volts',6)))
_CardLineVoltage_Type.__name__=_D
_CardLineVoltage_Object=MibTableColumn
cardLineVoltage=_CardLineVoltage_Object((1,3,6,1,4,1,5504,3,3,1,1,17),_CardLineVoltage_Type())
cardLineVoltage.setMaxAccess(_E)
if mibBuilder.loadTexts:cardLineVoltage.setStatus(_W)
class _CardVpiVciRange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('vpivci-range-not-applicable',1),('vpivci-range-vpi-15-vci-63',2),('vpivci-range-vpi-7-vci-127',3)))
_CardVpiVciRange_Type.__name__=_D
_CardVpiVciRange_Object=MibTableColumn
cardVpiVciRange=_CardVpiVciRange_Object((1,3,6,1,4,1,5504,3,3,1,1,18),_CardVpiVciRange_Type())
cardVpiVciRange.setMaxAccess(_E)
if mibBuilder.loadTexts:cardVpiVciRange.setStatus(_W)
class _CardPweTimingMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('source-differential',2),('source-adaptive',3),('remote-differential',4),('remote-adaptive',5)))
_CardPweTimingMode_Type.__name__=_D
_CardPweTimingMode_Object=MibTableColumn
cardPweTimingMode=_CardPweTimingMode_Object((1,3,6,1,4,1,5504,3,3,1,1,19),_CardPweTimingMode_Type())
cardPweTimingMode.setMaxAccess(_E)
if mibBuilder.loadTexts:cardPweTimingMode.setStatus(_A)
_CardSoftwareTable_Object=MibTable
cardSoftwareTable=_CardSoftwareTable_Object((1,3,6,1,4,1,5504,3,3,2))
if mibBuilder.loadTexts:cardSoftwareTable.setStatus(_A)
_CardSoftwareEntry_Object=MibTableRow
cardSoftwareEntry=_CardSoftwareEntry_Object((1,3,6,1,4,1,5504,3,3,2,1))
if mibBuilder.loadTexts:cardSoftwareEntry.setStatus(_A)
_CardSwRunningVers_Type=ZhoneAdminString
_CardSwRunningVers_Object=MibTableColumn
cardSwRunningVers=_CardSwRunningVers_Object((1,3,6,1,4,1,5504,3,3,2,1,1),_CardSwRunningVers_Type())
cardSwRunningVers.setMaxAccess(_C)
if mibBuilder.loadTexts:cardSwRunningVers.setStatus(_A)
_CardSwUpgradeVers_Type=ZhoneAdminString
_CardSwUpgradeVers_Object=MibTableColumn
cardSwUpgradeVers=_CardSwUpgradeVers_Object((1,3,6,1,4,1,5504,3,3,2,1,2),_CardSwUpgradeVers_Type())
cardSwUpgradeVers.setMaxAccess(_C)
if mibBuilder.loadTexts:cardSwUpgradeVers.setStatus(_A)
class _CardSwAdmin_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('loadUpgradeSw',1),('upgradeNow',2),('upgradeOnReset',3),('reloadCurrRev',4)))
_CardSwAdmin_Type.__name__=_D
_CardSwAdmin_Object=MibTableColumn
cardSwAdmin=_CardSwAdmin_Object((1,3,6,1,4,1,5504,3,3,2,1,3),_CardSwAdmin_Type())
cardSwAdmin.setMaxAccess(_E)
if mibBuilder.loadTexts:cardSwAdmin.setStatus(_A)
class _CardSwStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('upgradeLoadSuccessful',1),('loadingSw',2),('upgrading',3),('upgradeLoadFailed',4),('upgradeFailed',5),('upgradeImageNotAvail',6),('pendingUpgradeOnReset',7),('upgradeNotRequested',8)))
_CardSwStatus_Type.__name__=_D
_CardSwStatus_Object=MibTableColumn
cardSwStatus=_CardSwStatus_Object((1,3,6,1,4,1,5504,3,3,2,1,4),_CardSwStatus_Type())
cardSwStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cardSwStatus.setStatus(_A)
_CardRuntimeTable_Object=MibTable
cardRuntimeTable=_CardRuntimeTable_Object((1,3,6,1,4,1,5504,3,3,3))
if mibBuilder.loadTexts:cardRuntimeTable.setStatus(_A)
_CardRuntimeEntry_Object=MibTableRow
cardRuntimeEntry=_CardRuntimeEntry_Object((1,3,6,1,4,1,5504,3,3,3,1))
if mibBuilder.loadTexts:cardRuntimeEntry.setStatus(_A)
_CardPeakMemUsage_Type=Kbytes
_CardPeakMemUsage_Object=MibTableColumn
cardPeakMemUsage=_CardPeakMemUsage_Object((1,3,6,1,4,1,5504,3,3,3,1,1),_CardPeakMemUsage_Type())
cardPeakMemUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cardPeakMemUsage.setStatus(_A)
_CardAvailMem_Type=Kbytes
_CardAvailMem_Object=MibTableColumn
cardAvailMem=_CardAvailMem_Object((1,3,6,1,4,1,5504,3,3,3,1,2),_CardAvailMem_Type())
cardAvailMem.setMaxAccess(_C)
if mibBuilder.loadTexts:cardAvailMem.setStatus(_A)
_CardTotalMem_Type=Kbytes
_CardTotalMem_Object=MibTableColumn
cardTotalMem=_CardTotalMem_Object((1,3,6,1,4,1,5504,3,3,3,1,3),_CardTotalMem_Type())
cardTotalMem.setMaxAccess(_C)
if mibBuilder.loadTexts:cardTotalMem.setStatus(_A)
_CardProcessorIdle_Type=Integer32
_CardProcessorIdle_Object=MibTableColumn
cardProcessorIdle=_CardProcessorIdle_Object((1,3,6,1,4,1,5504,3,3,3,1,4),_CardProcessorIdle_Type())
cardProcessorIdle.setMaxAccess(_C)
if mibBuilder.loadTexts:cardProcessorIdle.setStatus(_A)
_CardProcessorUsage_Type=Integer32
_CardProcessorUsage_Object=MibTableColumn
cardProcessorUsage=_CardProcessorUsage_Object((1,3,6,1,4,1,5504,3,3,3,1,5),_CardProcessorUsage_Type())
cardProcessorUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cardProcessorUsage.setStatus(_A)
class _CardMemStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('ramMemOK',1),('ramMemLow',2),('flashMemOK',3),('flashMemLow',4),('flashMemOut',5)))
_CardMemStatus_Type.__name__=_D
_CardMemStatus_Object=MibTableColumn
cardMemStatus=_CardMemStatus_Object((1,3,6,1,4,1,5504,3,3,3,1,6),_CardMemStatus_Type())
cardMemStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cardMemStatus.setStatus(_A)
class _CardProcessorHighUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CardProcessorHighUsage_Type.__name__=_D
_CardProcessorHighUsage_Object=MibTableColumn
cardProcessorHighUsage=_CardProcessorHighUsage_Object((1,3,6,1,4,1,5504,3,3,3,1,7),_CardProcessorHighUsage_Type())
cardProcessorHighUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cardProcessorHighUsage.setStatus(_A)
class _CardProcessorServicesUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CardProcessorServicesUsage_Type.__name__=_D
_CardProcessorServicesUsage_Object=MibTableColumn
cardProcessorServicesUsage=_CardProcessorServicesUsage_Object((1,3,6,1,4,1,5504,3,3,3,1,8),_CardProcessorServicesUsage_Type())
cardProcessorServicesUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cardProcessorServicesUsage.setStatus(_A)
class _CardProcessorFrameworkUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CardProcessorFrameworkUsage_Type.__name__=_D
_CardProcessorFrameworkUsage_Object=MibTableColumn
cardProcessorFrameworkUsage=_CardProcessorFrameworkUsage_Object((1,3,6,1,4,1,5504,3,3,3,1,9),_CardProcessorFrameworkUsage_Type())
cardProcessorFrameworkUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cardProcessorFrameworkUsage.setStatus(_A)
class _CardProcessorLowUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CardProcessorLowUsage_Type.__name__=_D
_CardProcessorLowUsage_Object=MibTableColumn
cardProcessorLowUsage=_CardProcessorLowUsage_Object((1,3,6,1,4,1,5504,3,3,3,1,10),_CardProcessorLowUsage_Type())
cardProcessorLowUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:cardProcessorLowUsage.setStatus(_A)
_ZhoneCardServices_ObjectIdentity=ObjectIdentity
zhoneCardServices=_ZhoneCardServices_ObjectIdentity((1,3,6,1,4,1,5504,3,3,4))
_CardServicesTable_Object=MibTable
cardServicesTable=_CardServicesTable_Object((1,3,6,1,4,1,5504,3,3,4,1))
if mibBuilder.loadTexts:cardServicesTable.setStatus(_A)
_CardServicesEntry_Object=MibTableRow
cardServicesEntry=_CardServicesEntry_Object((1,3,6,1,4,1,5504,3,3,4,1,1))
cardServicesEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:cardServicesEntry.setStatus(_A)
_CardServiceId_Type=ZhoneServiceId
_CardServiceId_Object=MibTableColumn
cardServiceId=_CardServiceId_Object((1,3,6,1,4,1,5504,3,3,4,1,1,1),_CardServiceId_Type())
cardServiceId.setMaxAccess(_L)
if mibBuilder.loadTexts:cardServiceId.setStatus(_A)
_CardServiceInstance_Type=Unsigned32
_CardServiceInstance_Object=MibTableColumn
cardServiceInstance=_CardServiceInstance_Object((1,3,6,1,4,1,5504,3,3,4,1,1,2),_CardServiceInstance_Type())
cardServiceInstance.setMaxAccess(_L)
if mibBuilder.loadTexts:cardServiceInstance.setStatus(_A)
_CardServiceChangeTime_Type=TimeTicks
_CardServiceChangeTime_Object=MibTableColumn
cardServiceChangeTime=_CardServiceChangeTime_Object((1,3,6,1,4,1,5504,3,3,4,1,1,3),_CardServiceChangeTime_Type())
cardServiceChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cardServiceChangeTime.setStatus(_A)
class _CardServiceStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('unAvailable',1),('inActive',2),('standBy',3),('active',4)))
_CardServiceStatus_Type.__name__=_D
_CardServiceStatus_Object=MibTableColumn
cardServiceStatus=_CardServiceStatus_Object((1,3,6,1,4,1,5504,3,3,4,1,1,4),_CardServiceStatus_Type())
cardServiceStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cardServiceStatus.setStatus(_A)
_ActiveServicesTable_Object=MibTable
activeServicesTable=_ActiveServicesTable_Object((1,3,6,1,4,1,5504,3,3,4,2))
if mibBuilder.loadTexts:activeServicesTable.setStatus(_A)
_ActiveServicesEntry_Object=MibTableRow
activeServicesEntry=_ActiveServicesEntry_Object((1,3,6,1,4,1,5504,3,3,4,2,1))
activeServicesEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:activeServicesEntry.setStatus(_A)
_ActiveServiceShelf_Type=Integer32
_ActiveServiceShelf_Object=MibTableColumn
activeServiceShelf=_ActiveServiceShelf_Object((1,3,6,1,4,1,5504,3,3,4,2,1,1),_ActiveServiceShelf_Type())
activeServiceShelf.setMaxAccess(_C)
if mibBuilder.loadTexts:activeServiceShelf.setStatus(_A)
_ActiveServiceSlot_Type=Integer32
_ActiveServiceSlot_Object=MibTableColumn
activeServiceSlot=_ActiveServiceSlot_Object((1,3,6,1,4,1,5504,3,3,4,2,1,2),_ActiveServiceSlot_Type())
activeServiceSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:activeServiceSlot.setStatus(_A)
_ActiveServiceChangeTime_Type=TimeTicks
_ActiveServiceChangeTime_Object=MibTableColumn
activeServiceChangeTime=_ActiveServiceChangeTime_Object((1,3,6,1,4,1,5504,3,3,4,2,1,3),_ActiveServiceChangeTime_Type())
activeServiceChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:activeServiceChangeTime.setStatus(_A)
_StandbyServicesTable_Object=MibTable
standbyServicesTable=_StandbyServicesTable_Object((1,3,6,1,4,1,5504,3,3,4,3))
if mibBuilder.loadTexts:standbyServicesTable.setStatus(_A)
_StandbyServicesEntry_Object=MibTableRow
standbyServicesEntry=_StandbyServicesEntry_Object((1,3,6,1,4,1,5504,3,3,4,3,1))
standbyServicesEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:standbyServicesEntry.setStatus(_A)
_StandbyServiceShelf_Type=Integer32
_StandbyServiceShelf_Object=MibTableColumn
standbyServiceShelf=_StandbyServiceShelf_Object((1,3,6,1,4,1,5504,3,3,4,3,1,1),_StandbyServiceShelf_Type())
standbyServiceShelf.setMaxAccess(_C)
if mibBuilder.loadTexts:standbyServiceShelf.setStatus(_A)
_StandbyServiceSlot_Type=Integer32
_StandbyServiceSlot_Object=MibTableColumn
standbyServiceSlot=_StandbyServiceSlot_Object((1,3,6,1,4,1,5504,3,3,4,3,1,2),_StandbyServiceSlot_Type())
standbyServiceSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:standbyServiceSlot.setStatus(_A)
_StandbyServiceChangeTime_Type=TimeTicks
_StandbyServiceChangeTime_Object=MibTableColumn
standbyServiceChangeTime=_StandbyServiceChangeTime_Object((1,3,6,1,4,1,5504,3,3,4,3,1,3),_StandbyServiceChangeTime_Type())
standbyServiceChangeTime.setMaxAccess(_C)
if mibBuilder.loadTexts:standbyServiceChangeTime.setStatus(_A)
_ZhoneTrapCardServices_ObjectIdentity=ObjectIdentity
zhoneTrapCardServices=_ZhoneTrapCardServices_ObjectIdentity((1,3,6,1,4,1,5504,3,3,4,4))
if mibBuilder.loadTexts:zhoneTrapCardServices.setStatus(_A)
_ZhoneTrapCardServicesV2Traps_ObjectIdentity=ObjectIdentity
zhoneTrapCardServicesV2Traps=_ZhoneTrapCardServicesV2Traps_ObjectIdentity((1,3,6,1,4,1,5504,3,3,4,4,0))
if mibBuilder.loadTexts:zhoneTrapCardServicesV2Traps.setStatus(_A)
_ZhoneExternalRelay_ObjectIdentity=ObjectIdentity
zhoneExternalRelay=_ZhoneExternalRelay_ObjectIdentity((1,3,6,1,4,1,5504,3,3,8))
if mibBuilder.loadTexts:zhoneExternalRelay.setStatus(_A)
_ZhoneExternalRelayTable_Object=MibTable
zhoneExternalRelayTable=_ZhoneExternalRelayTable_Object((1,3,6,1,4,1,5504,3,3,8,1))
if mibBuilder.loadTexts:zhoneExternalRelayTable.setStatus(_A)
_ZhoneExternalRelayEntry_Object=MibTableRow
zhoneExternalRelayEntry=_ZhoneExternalRelayEntry_Object((1,3,6,1,4,1,5504,3,3,8,1,1))
zhoneExternalRelayEntry.setIndexNames((0,_F,_H),(0,_F,_I),(0,_B,_O))
if mibBuilder.loadTexts:zhoneExternalRelayEntry.setStatus(_A)
class _ZhoneExternalRelayName_Type(ZhoneAdminString):subtypeSpec=ZhoneAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZhoneExternalRelayName_Type.__name__=_T
_ZhoneExternalRelayName_Object=MibTableColumn
zhoneExternalRelayName=_ZhoneExternalRelayName_Object((1,3,6,1,4,1,5504,3,3,8,1,1,1),_ZhoneExternalRelayName_Type())
zhoneExternalRelayName.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneExternalRelayName.setStatus(_A)
class _ZhoneExternalRelayState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('relayStateOpen',1),('relayStateClosed',2)))
_ZhoneExternalRelayState_Type.__name__=_D
_ZhoneExternalRelayState_Object=MibTableColumn
zhoneExternalRelayState=_ZhoneExternalRelayState_Object((1,3,6,1,4,1,5504,3,3,8,1,1,2),_ZhoneExternalRelayState_Type())
zhoneExternalRelayState.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneExternalRelayState.setStatus(_A)
class _ZhoneExternalRelayNormalState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notSpecified',1),('normallyOpen',2),('normallyClosed',3)))
_ZhoneExternalRelayNormalState_Type.__name__=_D
_ZhoneExternalRelayNormalState_Object=MibTableColumn
zhoneExternalRelayNormalState=_ZhoneExternalRelayNormalState_Object((1,3,6,1,4,1,5504,3,3,8,1,1,3),_ZhoneExternalRelayNormalState_Type())
zhoneExternalRelayNormalState.setMaxAccess(_E)
if mibBuilder.loadTexts:zhoneExternalRelayNormalState.setStatus(_A)
_ZhoneExternalRelayMappingTable_Object=MibTable
zhoneExternalRelayMappingTable=_ZhoneExternalRelayMappingTable_Object((1,3,6,1,4,1,5504,3,3,8,2))
if mibBuilder.loadTexts:zhoneExternalRelayMappingTable.setStatus(_A)
_ZhoneExternalRelayMappingEntry_Object=MibTableRow
zhoneExternalRelayMappingEntry=_ZhoneExternalRelayMappingEntry_Object((1,3,6,1,4,1,5504,3,3,8,2,1))
zhoneExternalRelayMappingEntry.setIndexNames((1,_B,_G))
if mibBuilder.loadTexts:zhoneExternalRelayMappingEntry.setStatus(_A)
class _ZhoneExternalRelayId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_ZhoneExternalRelayId_Type.__name__=_D
_ZhoneExternalRelayId_Object=MibTableColumn
zhoneExternalRelayId=_ZhoneExternalRelayId_Object((1,3,6,1,4,1,5504,3,3,8,2,1,1),_ZhoneExternalRelayId_Type())
zhoneExternalRelayId.setMaxAccess(_C)
if mibBuilder.loadTexts:zhoneExternalRelayId.setStatus(_A)
_ZhoneTrapExternalRelay_ObjectIdentity=ObjectIdentity
zhoneTrapExternalRelay=_ZhoneTrapExternalRelay_ObjectIdentity((1,3,6,1,4,1,5504,3,3,8,3))
if mibBuilder.loadTexts:zhoneTrapExternalRelay.setStatus(_A)
_ZhoneTrapExternalRelayV2Traps_ObjectIdentity=ObjectIdentity
zhoneTrapExternalRelayV2Traps=_ZhoneTrapExternalRelayV2Traps_ObjectIdentity((1,3,6,1,4,1,5504,3,3,8,3,0))
if mibBuilder.loadTexts:zhoneTrapExternalRelayV2Traps.setStatus(_A)
_ZhoneCardCompliances_ObjectIdentity=ObjectIdentity
zhoneCardCompliances=_ZhoneCardCompliances_ObjectIdentity((1,3,6,1,4,1,5504,3,3,9))
_ZhoneCardGroups_ObjectIdentity=ObjectIdentity
zhoneCardGroups=_ZhoneCardGroups_ObjectIdentity((1,3,6,1,4,1,5504,3,3,9,1))
_ZhoneTrapCardMemV2Traps_ObjectIdentity=ObjectIdentity
zhoneTrapCardMemV2Traps=_ZhoneTrapCardMemV2Traps_ObjectIdentity((1,3,6,1,4,1,5504,3,3,10))
if mibBuilder.loadTexts:zhoneTrapCardMemV2Traps.setStatus(_A)
_ZrgResources_ObjectIdentity=ObjectIdentity
zrgResources=_ZrgResources_ObjectIdentity((1,3,6,1,4,1,5504,3,3,11))
if mibBuilder.loadTexts:zrgResources.setStatus(_A)
class _ZrgBatteryRelayStatus_Type(Bits):namedValues=NamedValues(*(('normalMode',0),('batteryON',1),('batteryLOW',2),('batteryBAD',3),('batteryGone',4),('noUPS',5)))
_ZrgBatteryRelayStatus_Type.__name__=_N
_ZrgBatteryRelayStatus_Object=MibScalar
zrgBatteryRelayStatus=_ZrgBatteryRelayStatus_Object((1,3,6,1,4,1,5504,3,3,11,1),_ZrgBatteryRelayStatus_Type())
zrgBatteryRelayStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zrgBatteryRelayStatus.setStatus(_A)
_ZrgTrapBatteryRelay_ObjectIdentity=ObjectIdentity
zrgTrapBatteryRelay=_ZrgTrapBatteryRelay_ObjectIdentity((1,3,6,1,4,1,5504,3,3,11,2))
if mibBuilder.loadTexts:zrgTrapBatteryRelay.setStatus(_A)
_ZrgBatterRelayTrapV2_ObjectIdentity=ObjectIdentity
zrgBatterRelayTrapV2=_ZrgBatterRelayTrapV2_ObjectIdentity((1,3,6,1,4,1,5504,3,3,11,2,0))
if mibBuilder.loadTexts:zrgBatterRelayTrapV2.setStatus(_A)
_ZnidResources_ObjectIdentity=ObjectIdentity
znidResources=_ZnidResources_ObjectIdentity((1,3,6,1,4,1,5504,3,3,14))
if mibBuilder.loadTexts:znidResources.setStatus(_A)
class _ZnidBatteryStatus_Type(Bits):namedValues=NamedValues(*(('normal',0),('onBatteryPower',1),('batteryPowerLow',2),('replaceBattery',3),('batteryRemoved',4),('noUPS',5)))
_ZnidBatteryStatus_Type.__name__=_N
_ZnidBatteryStatus_Object=MibScalar
znidBatteryStatus=_ZnidBatteryStatus_Object((1,3,6,1,4,1,5504,3,3,14,1),_ZnidBatteryStatus_Type())
znidBatteryStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:znidBatteryStatus.setStatus(_A)
_ZnidSerialNumber_Type=Unsigned32
_ZnidSerialNumber_Object=MibScalar
znidSerialNumber=_ZnidSerialNumber_Object((1,3,6,1,4,1,5504,3,3,14,2),_ZnidSerialNumber_Type())
znidSerialNumber.setMaxAccess(_L)
if mibBuilder.loadTexts:znidSerialNumber.setStatus(_A)
_ZnidNotificationObjects_ObjectIdentity=ObjectIdentity
znidNotificationObjects=_ZnidNotificationObjects_ObjectIdentity((1,3,6,1,4,1,5504,3,3,14,3))
if mibBuilder.loadTexts:znidNotificationObjects.setStatus(_A)
_ZnidNotifications_ObjectIdentity=ObjectIdentity
znidNotifications=_ZnidNotifications_ObjectIdentity((1,3,6,1,4,1,5504,3,3,14,3,0))
if mibBuilder.loadTexts:znidNotifications.setStatus(_A)
cardResourceEntry.registerAugmentions((_B,_X))
cardSoftwareEntry.setIndexNames(*cardResourceEntry.getIndexNames())
cardResourceEntry.registerAugmentions((_B,_Y))
cardRuntimeEntry.setIndexNames(*cardResourceEntry.getIndexNames())
zhoneCardResourcesGroup=ObjectGroup((1,3,6,1,4,1,5504,3,3,9,1,1))
zhoneCardResourcesGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_P),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_Q),(_B,_z)))
if mibBuilder.loadTexts:zhoneCardResourcesGroup.setStatus(_A)
zhoneExternalRelayGroup=ObjectGroup((1,3,6,1,4,1,5504,3,3,9,1,2))
zhoneExternalRelayGroup.setObjects(*((_B,_G),(_B,_M),(_B,_O)))
if mibBuilder.loadTexts:zhoneExternalRelayGroup.setStatus(_A)
znidOjectGroup=ObjectGroup((1,3,6,1,4,1,5504,3,3,14,3,2))
znidOjectGroup.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:znidOjectGroup.setStatus(_A)
zhoneCardServicesStatusChange=NotificationType((1,3,6,1,4,1,5504,3,3,4,4,0,1))
zhoneCardServicesStatusChange.setObjects((_B,_A0))
if mibBuilder.loadTexts:zhoneCardServicesStatusChange.setStatus(_A)
zhoneCardServicesStandbyReady=NotificationType((1,3,6,1,4,1,5504,3,3,4,4,0,2))
zhoneCardServicesStandbyReady.setObjects(*((_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:zhoneCardServicesStandbyReady.setStatus(_A)
zhoneExternalAlarmTrap=NotificationType((1,3,6,1,4,1,5504,3,3,8,3,0,1))
zhoneExternalAlarmTrap.setObjects(*((_B,_G),(_B,_M)))
if mibBuilder.loadTexts:zhoneExternalAlarmTrap.setStatus(_A)
zhoneMxkAlarmInputTrap=NotificationType((1,3,6,1,4,1,5504,3,3,8,3,0,2))
zhoneMxkAlarmInputTrap.setObjects(*((_B,_G),(_B,_M),(_B,_A3)))
if mibBuilder.loadTexts:zhoneMxkAlarmInputTrap.setStatus(_A)
zhoneTrapCardMemStatus=NotificationType((1,3,6,1,4,1,5504,3,3,10,2))
zhoneTrapCardMemStatus.setObjects((_B,_Q))
if mibBuilder.loadTexts:zhoneTrapCardMemStatus.setStatus(_A)
zhoneTrapProcessorUsage=NotificationType((1,3,6,1,4,1,5504,3,3,10,3))
zhoneTrapProcessorUsage.setObjects((_B,_P))
if mibBuilder.loadTexts:zhoneTrapProcessorUsage.setStatus(_A)
zrgBatteryRelayNotification=NotificationType((1,3,6,1,4,1,5504,3,3,11,2,0,1))
zrgBatteryRelayNotification.setObjects((_B,_A4))
if mibBuilder.loadTexts:zrgBatteryRelayNotification.setStatus(_A)
znidBatteryStatusNotification=NotificationType((1,3,6,1,4,1,5504,3,3,14,3,0,1))
znidBatteryStatusNotification.setObjects(*((_B,_S),(_B,_R)))
if mibBuilder.loadTexts:znidBatteryStatusNotification.setStatus(_A)
zhoneExternalAlarmTrapGroup=NotificationGroup((1,3,6,1,4,1,5504,3,3,9,1,3))
zhoneExternalAlarmTrapGroup.setObjects(*((_B,_A5),(_B,_A6)))
if mibBuilder.loadTexts:zhoneExternalAlarmTrapGroup.setStatus(_A)
zhoneTrapCardMemGroup=NotificationGroup((1,3,6,1,4,1,5504,3,3,10,1))
zhoneTrapCardMemGroup.setObjects(*((_B,_A7),(_B,_A8)))
if mibBuilder.loadTexts:zhoneTrapCardMemGroup.setStatus(_A)
znidNotificationGroup=NotificationGroup((1,3,6,1,4,1,5504,3,3,14,3,1))
znidNotificationGroup.setObjects((_B,_A9))
if mibBuilder.loadTexts:znidNotificationGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'Kbytes':Kbytes,'ZhoneServiceId':ZhoneServiceId,'cardResourceTable':cardResourceTable,'cardResourceEntry':cardResourceEntry,_Z:cardIdentification,_a:cardZhoneType,_b:cardMfgSerialNumber,_c:cardMfgCLEICode,_d:cardMfgRevisionCode,_e:cardMfgBootRevision,_f:cardPostResults,_g:cardAdminStatus,_h:cardOperStatus,_i:cardAdminStatsEnable,_j:cardUpTime,_k:cardProcessorType,_l:cardPortStatus,_m:cardInterfaceType,'cardAtmManualAal2bw':cardAtmManualAal2bw,'cardAtmManualAal2h':cardAtmManualAal2h,'cardLineVoltage':cardLineVoltage,'cardVpiVciRange':cardVpiVciRange,_z:cardPweTimingMode,'cardSoftwareTable':cardSoftwareTable,_X:cardSoftwareEntry,_n:cardSwRunningVers,_o:cardSwUpgradeVers,_p:cardSwAdmin,_q:cardSwStatus,'cardRuntimeTable':cardRuntimeTable,_Y:cardRuntimeEntry,_r:cardPeakMemUsage,_s:cardAvailMem,_t:cardTotalMem,_u:cardProcessorIdle,_P:cardProcessorUsage,_Q:cardMemStatus,_y:cardProcessorHighUsage,_v:cardProcessorServicesUsage,_w:cardProcessorFrameworkUsage,_x:cardProcessorLowUsage,'zhoneCardServices':zhoneCardServices,'cardServicesTable':cardServicesTable,'cardServicesEntry':cardServicesEntry,_J:cardServiceId,_K:cardServiceInstance,'cardServiceChangeTime':cardServiceChangeTime,_A0:cardServiceStatus,'activeServicesTable':activeServicesTable,'activeServicesEntry':activeServicesEntry,'activeServiceShelf':activeServiceShelf,'activeServiceSlot':activeServiceSlot,'activeServiceChangeTime':activeServiceChangeTime,'standbyServicesTable':standbyServicesTable,'standbyServicesEntry':standbyServicesEntry,_A1:standbyServiceShelf,_A2:standbyServiceSlot,'standbyServiceChangeTime':standbyServiceChangeTime,'zhoneTrapCardServices':zhoneTrapCardServices,'zhoneTrapCardServicesV2Traps':zhoneTrapCardServicesV2Traps,'zhoneCardServicesStatusChange':zhoneCardServicesStatusChange,'zhoneCardServicesStandbyReady':zhoneCardServicesStandbyReady,'zhoneExternalRelay':zhoneExternalRelay,'zhoneExternalRelayTable':zhoneExternalRelayTable,'zhoneExternalRelayEntry':zhoneExternalRelayEntry,_G:zhoneExternalRelayName,_M:zhoneExternalRelayState,_A3:zhoneExternalRelayNormalState,'zhoneExternalRelayMappingTable':zhoneExternalRelayMappingTable,'zhoneExternalRelayMappingEntry':zhoneExternalRelayMappingEntry,_O:zhoneExternalRelayId,'zhoneTrapExternalRelay':zhoneTrapExternalRelay,'zhoneTrapExternalRelayV2Traps':zhoneTrapExternalRelayV2Traps,_A5:zhoneExternalAlarmTrap,_A6:zhoneMxkAlarmInputTrap,'zhoneCardCompliances':zhoneCardCompliances,'zhoneCardGroups':zhoneCardGroups,'zhoneCardResourcesGroup':zhoneCardResourcesGroup,'zhoneExternalRelayGroup':zhoneExternalRelayGroup,'zhoneExternalAlarmTrapGroup':zhoneExternalAlarmTrapGroup,'zhoneTrapCardMemV2Traps':zhoneTrapCardMemV2Traps,'zhoneTrapCardMemGroup':zhoneTrapCardMemGroup,_A7:zhoneTrapCardMemStatus,_A8:zhoneTrapProcessorUsage,'zrgResources':zrgResources,_A4:zrgBatteryRelayStatus,'zrgTrapBatteryRelay':zrgTrapBatteryRelay,'zrgBatterRelayTrapV2':zrgBatterRelayTrapV2,'zrgBatteryRelayNotification':zrgBatteryRelayNotification,'znidResources':znidResources,_R:znidBatteryStatus,_S:znidSerialNumber,'znidNotificationObjects':znidNotificationObjects,'znidNotifications':znidNotifications,_A9:znidBatteryStatusNotification,'znidNotificationGroup':znidNotificationGroup,'znidOjectGroup':znidOjectGroup,'zhoneCardResourcesModule':zhoneCardResourcesModule})