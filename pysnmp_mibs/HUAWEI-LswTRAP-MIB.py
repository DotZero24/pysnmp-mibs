_p='hwBoardRequiredPower'
_o='hwBoardAvailablePower'
_n='hwLswTrapCoreProcessInfo'
_m='hwLswTrapCpuUsage'
_l='hwLswCoreTrapUsage'
_k='hwLswCoreThreshold'
_j='hwLswCoreIndex'
_i='hwDevMFirstTrapTime'
_h='hwDevMFanNum'
_g='hwLswSubslotIndex'
_f='hwLswCpuUsageRecoverThreshold'
_e='hwLswCpuUsageSevereThreshold'
_d='hwLswCpuUsageMinorThreshold'
_c='hwLswCpuRatio'
_b='hwsLswTrapProcessCpuInfo'
_a='hwsLswTrapCpuCoreInfo'
_Z='SnmpAdminString'
_Y='hwLswCpuMemoryCurrentState'
_X='hwLswCpuMemoryCriticalThreshold'
_W='hwLswCpuMemorySevereThreshold'
_V='hwLswCpuMemoryMinorThreshold'
_U='hwLswCpuMemoryNormalThreshold'
_T='hwLswCpuMemoryEarlyWarningThreshold'
_S='hwLswCpuMemorySecureThreshold'
_R='hwLswCpuMemoryLowFree'
_Q='hwLswCpuMemoryLowTotal'
_P='hwLswCpuMemoryHighFree'
_O='hwLswCpuMemoryHighTotal'
_N='hwLswCpuMemoryFreeRatio'
_M='hwLswCpuMemoryFree'
_L='hwLswCpuMemory'
_K='hwDevMPowerNum'
_J='hwsLswTrapSlubInfo'
_I='hwsLswTrapProcessMemoryInfo'
_H='accessible-for-notify'
_G='HUAWEI-LswDEVM-MIB'
_F='hwLswCpuIndex'
_E='hwLswSlotIndex'
_D='hwLswFrameIndex'
_C='current'
_B='HUAWEI-LSW-DEV-ADM-MIB'
_A='HUAWEI-LswTRAP-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lswCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','lswCommon')
hwLswCoreIndex,hwLswCoreThreshold,hwLswCpuIndex,hwLswFrameIndex,hwLswSlotIndex,hwLswSubslotIndex=mibBuilder.importSymbols(_B,_j,_k,_F,_D,_E,_g)
hwDevMFanNum,hwDevMFirstTrapTime,hwDevMPowerNum=mibBuilder.importSymbols(_G,_h,_i,_K)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_Z)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hwsLswTrapMib=ModuleIdentity((1,3,6,1,4,1,2011,2,23,1,12))
if mibBuilder.loadTexts:hwsLswTrapMib.setRevisions(('2017-12-05 00:00','2017-07-17 00:00','2017-06-24 00:00','2017-01-12 00:00','2011-11-26 00:00'))
_HwsLswTRAPMibObject_ObjectIdentity=ObjectIdentity
hwsLswTRAPMibObject=_HwsLswTRAPMibObject_ObjectIdentity((1,3,6,1,4,1,2011,2,23,1,12,1))
_HwNetworkHealthMonitorFailure_ObjectIdentity=ObjectIdentity
hwNetworkHealthMonitorFailure=_HwNetworkHealthMonitorFailure_ObjectIdentity((1,3,6,1,4,1,2011,2,23,1,12,1,98))
_HwNetworkHealthMonitorNormal_ObjectIdentity=ObjectIdentity
hwNetworkHealthMonitorNormal=_HwNetworkHealthMonitorNormal_ObjectIdentity((1,3,6,1,4,1,2011,2,23,1,12,1,99))
_HwsLswTRAPMibInfor_ObjectIdentity=ObjectIdentity
hwsLswTRAPMibInfor=_HwsLswTRAPMibInfor_ObjectIdentity((1,3,6,1,4,1,2011,2,23,1,12,2))
class _HwsLswTrapCpuCoreInfo_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HwsLswTrapCpuCoreInfo_Type.__name__=_Z
_HwsLswTrapCpuCoreInfo_Object=MibScalar
hwsLswTrapCpuCoreInfo=_HwsLswTrapCpuCoreInfo_Object((1,3,6,1,4,1,2011,2,23,1,12,2,1),_HwsLswTrapCpuCoreInfo_Type())
hwsLswTrapCpuCoreInfo.setMaxAccess(_H)
if mibBuilder.loadTexts:hwsLswTrapCpuCoreInfo.setStatus(_C)
class _HwsLswTrapProcessCpuInfo_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HwsLswTrapProcessCpuInfo_Type.__name__=_Z
_HwsLswTrapProcessCpuInfo_Object=MibScalar
hwsLswTrapProcessCpuInfo=_HwsLswTrapProcessCpuInfo_Object((1,3,6,1,4,1,2011,2,23,1,12,2,2),_HwsLswTrapProcessCpuInfo_Type())
hwsLswTrapProcessCpuInfo.setMaxAccess(_H)
if mibBuilder.loadTexts:hwsLswTrapProcessCpuInfo.setStatus(_C)
class _HwsLswTrapProcessMemoryInfo_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HwsLswTrapProcessMemoryInfo_Type.__name__=_Z
_HwsLswTrapProcessMemoryInfo_Object=MibScalar
hwsLswTrapProcessMemoryInfo=_HwsLswTrapProcessMemoryInfo_Object((1,3,6,1,4,1,2011,2,23,1,12,2,3),_HwsLswTrapProcessMemoryInfo_Type())
hwsLswTrapProcessMemoryInfo.setMaxAccess(_H)
if mibBuilder.loadTexts:hwsLswTrapProcessMemoryInfo.setStatus(_C)
class _HwsLswTrapSlubInfo_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HwsLswTrapSlubInfo_Type.__name__=_Z
_HwsLswTrapSlubInfo_Object=MibScalar
hwsLswTrapSlubInfo=_HwsLswTrapSlubInfo_Object((1,3,6,1,4,1,2011,2,23,1,12,2,4),_HwsLswTrapSlubInfo_Type())
hwsLswTrapSlubInfo.setMaxAccess(_H)
if mibBuilder.loadTexts:hwsLswTrapSlubInfo.setStatus(_C)
class _HwLswTrapCpuUsage_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HwLswTrapCpuUsage_Type.__name__=_Z
_HwLswTrapCpuUsage_Object=MibScalar
hwLswTrapCpuUsage=_HwLswTrapCpuUsage_Object((1,3,6,1,4,1,2011,2,23,1,12,2,5),_HwLswTrapCpuUsage_Type())
hwLswTrapCpuUsage.setMaxAccess(_H)
if mibBuilder.loadTexts:hwLswTrapCpuUsage.setStatus(_C)
class _HwLswTrapCoreProcessInfo_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HwLswTrapCoreProcessInfo_Type.__name__=_Z
_HwLswTrapCoreProcessInfo_Object=MibScalar
hwLswTrapCoreProcessInfo=_HwLswTrapCoreProcessInfo_Object((1,3,6,1,4,1,2011,2,23,1,12,2,6),_HwLswTrapCoreProcessInfo_Type())
hwLswTrapCoreProcessInfo.setMaxAccess(_H)
if mibBuilder.loadTexts:hwLswTrapCoreProcessInfo.setStatus(_C)
_HwLswCoreTrapUsage_Type=Unsigned32
_HwLswCoreTrapUsage_Object=MibScalar
hwLswCoreTrapUsage=_HwLswCoreTrapUsage_Object((1,3,6,1,4,1,2011,2,23,1,12,2,7),_HwLswCoreTrapUsage_Type())
hwLswCoreTrapUsage.setMaxAccess(_H)
if mibBuilder.loadTexts:hwLswCoreTrapUsage.setStatus(_C)
_HwBoardAvailablePower_Type=Integer32
_HwBoardAvailablePower_Object=MibScalar
hwBoardAvailablePower=_HwBoardAvailablePower_Object((1,3,6,1,4,1,2011,2,23,1,12,2,8),_HwBoardAvailablePower_Type())
hwBoardAvailablePower.setMaxAccess(_H)
if mibBuilder.loadTexts:hwBoardAvailablePower.setStatus(_C)
_HwBoardRequiredPower_Type=Integer32
_HwBoardRequiredPower_Object=MibScalar
hwBoardRequiredPower=_HwBoardRequiredPower_Object((1,3,6,1,4,1,2011,2,23,1,12,2,9),_HwBoardRequiredPower_Type())
hwBoardRequiredPower.setMaxAccess(_H)
if mibBuilder.loadTexts:hwBoardRequiredPower.setStatus(_C)
_HwsLswTRAPMibObjectV2_ObjectIdentity=ObjectIdentity
hwsLswTRAPMibObjectV2=_HwsLswTRAPMibObjectV2_ObjectIdentity((1,3,6,1,4,1,2011,2,23,1,12,3))
_HwsLswTRAPMibObjectV2Prefix_ObjectIdentity=ObjectIdentity
hwsLswTRAPMibObjectV2Prefix=_HwsLswTRAPMibObjectV2Prefix_ObjectIdentity((1,3,6,1,4,1,2011,2,23,1,12,3,0))
powerfailure=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,1))
powerfailure.setObjects(*((_G,_K),(_G,_i)))
if mibBuilder.loadTexts:powerfailure.setStatus(_C)
hwPowerNormal=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,2))
hwPowerNormal.setObjects(*((_G,_K),(_G,_i)))
if mibBuilder.loadTexts:hwPowerNormal.setStatus(_C)
hwMasterPowerNormal=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,3))
hwMasterPowerNormal.setObjects((_G,_K))
if mibBuilder.loadTexts:hwMasterPowerNormal.setStatus(_C)
hwSlavePowerNormal=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,4))
hwSlavePowerNormal.setObjects((_G,_K))
if mibBuilder.loadTexts:hwSlavePowerNormal.setStatus(_C)
hwPowerRemoved=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,5))
hwPowerRemoved.setObjects((_G,_K))
if mibBuilder.loadTexts:hwPowerRemoved.setStatus(_C)
fanfailure=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,6))
fanfailure.setObjects((_G,_h))
if mibBuilder.loadTexts:fanfailure.setStatus(_C)
hwFanNormal=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,7))
hwFanNormal.setObjects((_G,_h))
if mibBuilder.loadTexts:hwFanNormal.setStatus(_C)
hwBoardRemoved=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,8))
hwBoardRemoved.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:hwBoardRemoved.setStatus(_C)
hwBoardInserted=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,9))
hwBoardInserted.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:hwBoardInserted.setStatus(_C)
hwBoardFailure=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,10))
hwBoardFailure.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:hwBoardFailure.setStatus(_C)
hwBoardNormal=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,11))
hwBoardNormal.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:hwBoardNormal.setStatus(_C)
hwSubcardRemove=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,12))
hwSubcardRemove.setObjects(*((_B,_D),(_B,_E),(_B,_g)))
if mibBuilder.loadTexts:hwSubcardRemove.setStatus(_C)
hwSubcardInsert=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,13))
hwSubcardInsert.setObjects(*((_B,_D),(_B,_E),(_B,_g)))
if mibBuilder.loadTexts:hwSubcardInsert.setStatus(_C)
hwBoaardTemperatureLower=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,14))
hwBoaardTemperatureLower.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:hwBoaardTemperatureLower.setStatus(_C)
hwBoaardTemperatureFromLowerToNormal=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,15))
hwBoaardTemperatureFromLowerToNormal.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:hwBoaardTemperatureFromLowerToNormal.setStatus(_C)
hwBoaardTemperatureHigher=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,16))
hwBoaardTemperatureHigher.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:hwBoaardTemperatureHigher.setStatus(_C)
hwBoaardTemperatureFormHigherToNormal=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,17))
hwBoaardTemperatureFormHigherToNormal.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:hwBoaardTemperatureFormHigherToNormal.setStatus(_C)
hwRequestLoading=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,18))
hwRequestLoading.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:hwRequestLoading.setStatus(_C)
hwLoadFailure=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,19))
hwLoadFailure.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:hwLoadFailure.setStatus(_C)
hwLoadFinished=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,20))
hwLoadFinished.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:hwLoadFinished.setStatus(_C)
hwBackBoardModeSetFuilure=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,21))
hwBackBoardModeSetFuilure.setObjects((_B,_D))
if mibBuilder.loadTexts:hwBackBoardModeSetFuilure.setStatus(_C)
hwBackBoardModeSetOK=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,22))
hwBackBoardModeSetOK.setObjects((_B,_D))
if mibBuilder.loadTexts:hwBackBoardModeSetOK.setStatus(_C)
hwPowerInserted=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,23))
hwPowerInserted.setObjects((_G,_K))
if mibBuilder.loadTexts:hwPowerInserted.setStatus(_C)
hwBootImageUpdated=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,24))
hwBootImageUpdated.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:hwBootImageUpdated.setStatus(_C)
hwCpuRemoved=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,25))
hwCpuRemoved.setObjects(*((_B,_D),(_B,_E),(_B,_F)))
if mibBuilder.loadTexts:hwCpuRemoved.setStatus(_C)
hwCpuFailure=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,26))
hwCpuFailure.setObjects(*((_B,_D),(_B,_E),(_B,_F)))
if mibBuilder.loadTexts:hwCpuFailure.setStatus(_C)
hwCpuNormal=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,27))
hwCpuNormal.setObjects(*((_B,_D),(_B,_E),(_B,_F)))
if mibBuilder.loadTexts:hwCpuNormal.setStatus(_C)
hwPowerIncompatible=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,28))
hwPowerIncompatible.setObjects((_G,_K))
if mibBuilder.loadTexts:hwPowerIncompatible.setStatus(_C)
hwCpuUsageSevereNotification=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,29))
hwCpuUsageSevereNotification.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:hwCpuUsageSevereNotification.setStatus(_C)
hwCpuUsageSevereRecoverNotification=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,30))
hwCpuUsageSevereRecoverNotification.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:hwCpuUsageSevereRecoverNotification.setStatus(_C)
hwCpuUsageMinorNotification=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,31))
hwCpuUsageMinorNotification.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:hwCpuUsageMinorNotification.setStatus(_C)
hwCpuUsageMinorRecoverNotification=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,32))
hwCpuUsageMinorRecoverNotification.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_a),(_A,_b)))
if mibBuilder.loadTexts:hwCpuUsageMinorRecoverNotification.setStatus(_C)
hwMemoryUsageEarlyWarningNotification=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,33))
hwMemoryUsageEarlyWarningNotification.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:hwMemoryUsageEarlyWarningNotification.setStatus(_C)
hwMemoryUsageEarlyWarningRecoverNotification=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,34))
hwMemoryUsageEarlyWarningRecoverNotification.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:hwMemoryUsageEarlyWarningRecoverNotification.setStatus(_C)
hwMemoryUsageMinorNotification=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,35))
hwMemoryUsageMinorNotification.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:hwMemoryUsageMinorNotification.setStatus(_C)
hwMemoryUsageMinorRecoverNotification=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,36))
hwMemoryUsageMinorRecoverNotification.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:hwMemoryUsageMinorRecoverNotification.setStatus(_C)
hwMemoryUsageSevereNotification=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,37))
hwMemoryUsageSevereNotification.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:hwMemoryUsageSevereNotification.setStatus(_C)
hwMemoryUsageSevereRecoverNotification=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,38))
hwMemoryUsageSevereRecoverNotification.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:hwMemoryUsageSevereRecoverNotification.setStatus(_C)
hwMemoryUsageCriticalNotification=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,39))
hwMemoryUsageCriticalNotification.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:hwMemoryUsageCriticalNotification.setStatus(_C)
hwMemoryUsageCriticalRecoverNotification=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,1,40))
hwMemoryUsageCriticalRecoverNotification.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_I),(_A,_J)))
if mibBuilder.loadTexts:hwMemoryUsageCriticalRecoverNotification.setStatus(_C)
hwCoreUsageNotification=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,3,0,1))
hwCoreUsageNotification.setObjects(*((_B,_D),(_B,_E),(_B,_F),(_B,_j),(_A,_l),(_B,_k),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:hwCoreUsageNotification.setStatus(_C)
hwBoardPowerNotEnough=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,3,0,2))
hwBoardPowerNotEnough.setObjects(*((_B,_D),(_B,_E),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:hwBoardPowerNotEnough.setStatus(_C)
hwAlarmInPortIn=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,3,0,3))
hwAlarmInPortIn.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:hwAlarmInPortIn.setStatus(_C)
hwAlarmInPortRecover=NotificationType((1,3,6,1,4,1,2011,2,23,1,12,3,0,4))
hwAlarmInPortRecover.setObjects(*((_B,_D),(_B,_E)))
if mibBuilder.loadTexts:hwAlarmInPortRecover.setStatus(_C)
mibBuilder.exportSymbols(_A,**{'hwsLswTrapMib':hwsLswTrapMib,'hwsLswTRAPMibObject':hwsLswTRAPMibObject,'powerfailure':powerfailure,'hwPowerNormal':hwPowerNormal,'hwMasterPowerNormal':hwMasterPowerNormal,'hwSlavePowerNormal':hwSlavePowerNormal,'hwPowerRemoved':hwPowerRemoved,'fanfailure':fanfailure,'hwFanNormal':hwFanNormal,'hwBoardRemoved':hwBoardRemoved,'hwBoardInserted':hwBoardInserted,'hwBoardFailure':hwBoardFailure,'hwBoardNormal':hwBoardNormal,'hwSubcardRemove':hwSubcardRemove,'hwSubcardInsert':hwSubcardInsert,'hwBoaardTemperatureLower':hwBoaardTemperatureLower,'hwBoaardTemperatureFromLowerToNormal':hwBoaardTemperatureFromLowerToNormal,'hwBoaardTemperatureHigher':hwBoaardTemperatureHigher,'hwBoaardTemperatureFormHigherToNormal':hwBoaardTemperatureFormHigherToNormal,'hwRequestLoading':hwRequestLoading,'hwLoadFailure':hwLoadFailure,'hwLoadFinished':hwLoadFinished,'hwBackBoardModeSetFuilure':hwBackBoardModeSetFuilure,'hwBackBoardModeSetOK':hwBackBoardModeSetOK,'hwPowerInserted':hwPowerInserted,'hwBootImageUpdated':hwBootImageUpdated,'hwCpuRemoved':hwCpuRemoved,'hwCpuFailure':hwCpuFailure,'hwCpuNormal':hwCpuNormal,'hwPowerIncompatible':hwPowerIncompatible,'hwCpuUsageSevereNotification':hwCpuUsageSevereNotification,'hwCpuUsageSevereRecoverNotification':hwCpuUsageSevereRecoverNotification,'hwCpuUsageMinorNotification':hwCpuUsageMinorNotification,'hwCpuUsageMinorRecoverNotification':hwCpuUsageMinorRecoverNotification,'hwMemoryUsageEarlyWarningNotification':hwMemoryUsageEarlyWarningNotification,'hwMemoryUsageEarlyWarningRecoverNotification':hwMemoryUsageEarlyWarningRecoverNotification,'hwMemoryUsageMinorNotification':hwMemoryUsageMinorNotification,'hwMemoryUsageMinorRecoverNotification':hwMemoryUsageMinorRecoverNotification,'hwMemoryUsageSevereNotification':hwMemoryUsageSevereNotification,'hwMemoryUsageSevereRecoverNotification':hwMemoryUsageSevereRecoverNotification,'hwMemoryUsageCriticalNotification':hwMemoryUsageCriticalNotification,'hwMemoryUsageCriticalRecoverNotification':hwMemoryUsageCriticalRecoverNotification,'hwNetworkHealthMonitorFailure':hwNetworkHealthMonitorFailure,'hwNetworkHealthMonitorNormal':hwNetworkHealthMonitorNormal,'hwsLswTRAPMibInfor':hwsLswTRAPMibInfor,_a:hwsLswTrapCpuCoreInfo,_b:hwsLswTrapProcessCpuInfo,_I:hwsLswTrapProcessMemoryInfo,_J:hwsLswTrapSlubInfo,_m:hwLswTrapCpuUsage,_n:hwLswTrapCoreProcessInfo,_l:hwLswCoreTrapUsage,_o:hwBoardAvailablePower,_p:hwBoardRequiredPower,'hwsLswTRAPMibObjectV2':hwsLswTRAPMibObjectV2,'hwsLswTRAPMibObjectV2Prefix':hwsLswTRAPMibObjectV2Prefix,'hwCoreUsageNotification':hwCoreUsageNotification,'hwBoardPowerNotEnough':hwBoardPowerNotEnough,'hwAlarmInPortIn':hwAlarmInPortIn,'hwAlarmInPortRecover':hwAlarmInPortRecover})