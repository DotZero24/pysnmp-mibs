_B2='h3cEntityExtPowerGroup'
_B1='h3cEntityExtManuGroup'
_B0='h3cEntityExtNotificationGroup'
_A_='h3cEntityExtGroup'
_Az='h3cEntityExtSFPAlarmOffEx'
_Ay='h3cEntityExtSFPAlarmOnEx'
_Ax='h3cEntityExtVoltageTooHigh'
_Aw='h3cEntityExtVoltageHigher'
_Av='h3cEntityExtVoltageLower'
_Au='h3cEntityExtVoltageTooLow'
_At='h3cEntityExtVoltageNormal'
_As='h3cEntityExtMemUsageThresholdRecoverTrap'
_Ar='h3cEntityExtMemUsageThresholdOverTrap'
_Aq='h3cEntityExtSFPInvalidNow'
_Ap='h3cEntityExtSFPInvalid'
_Ao='h3cEntityExtFanDirectionNotAccord'
_An='h3cEntityExtFanDirectionNotPreferred'
_Am='h3cEntityExtTemperatureTooLow'
_Al='h3cEntityExtCritLowerTempThresholdNotification'
_Ak='h3cEntityExtECCParityAlarm'
_Aj='h3cEntityExtMemAllocatedFailed'
_Ai='h3cEntityExtMemUsageThresholdRecover'
_Ah='h3cEntityExtCpuUsageThresholdRecover'
_Ag='h3cEntityExternalAlarmRecover'
_Af='h3cEntityExternalAlarmOccur'
_Ae='h3cEntityExtTemperatureNormal'
_Ad='h3cEntityExtTemperatureTooUp'
_Ac='h3cEntityExtTemperatureLower'
_Ab='h3cEntityExtResourceEnough'
_Aa='h3cEntityExtResourceLack'
_AZ='h3cEntityExtFaultAlarmOff'
_AY='h3cEntityExtFaultAlarmOn'
_AX='h3cEntityExtForcedPowerOn'
_AW='h3cEntityExtForcedPowerOff'
_AV='h3cEntityRemove'
_AU='h3cEntityInsert'
_AT='h3cEntityExtSFPPhony'
_AS='h3cEntityExtSFPAlarmOff'
_AR='h3cEntityExtSFPAlarmOn'
_AQ='h3cEntityExtCriticalTemperatureThresholdNotification'
_AP='h3cEntityExtOperDisabled'
_AO='h3cEntityExtOperEnabled'
_AN='h3cEntityExtMemUsageThresholdNotification'
_AM='h3cEntityExtCpuUsageThresholdNotfication'
_AL='h3cEntityExtVoltageHighThresholdNotification'
_AK='h3cEntityExtVoltageLowThresholdNotification'
_AJ='h3cEntityExtTemperatureThresholdNotification'
_AI='h3cEntityExtVoltageFatalHighThreshold'
_AH='h3cEntityExtVoltageFatalLowThreshold'
_AG='h3cEntityExtSFPInvalidInDays'
_AF='h3cEntityExtECCParityAlarmStatus'
_AE='h3cEntityExtPeakPower'
_AD='h3cEntityExtAveragePower'
_AC='h3cEntityExtCurrentPower'
_AB='h3cEntityExtNominalPower'
_AA='h3cEntityExtMacAddressCount'
_A9='h3cEntityExtManuBOM'
_A8='h3cEntityExtManuBuildInfo'
_A7='h3cEntityExtManuSerialNum'
_A6='h3cEntityExtCpuUsageIn5Minutes'
_A5='h3cEntityExtCpuUsageIn1Minute'
_A4='h3cEntityExtMemType'
_A3='h3cEntityExtMemAvgUsage'
_A2='h3cEntityExtCpuAvgUsage'
_A1='h3cEntityExtFirstUsedDate'
_A0='h3cEntityExtPhyCpuFrequency'
_z='h3cEntityExtPhyMemSize'
_y='h3cEntityExtCpuMaxUsage'
_x='h3cEntityExtMacAddress'
_w='h3cEntityExtUpTime'
_v='h3cEntityExtStandbyStatus'
_u='h3cProcessID'
_t='normal'
_s='DisplayString'
_r='DateAndTime'
_q='Unsigned32'
_p='SnmpAdminString'
_o='OctetString'
_n='h3cEntityExtVoltageMajorHighThreshold'
_m='h3cEntityExtVoltageMajorLowThreshold'
_l='h3cEntityExtTrapDescription'
_k='h3cEntityExtShutdownLowerTemperatureThreshold'
_j='h3cEntityExtCriticalLowerTemperatureThreshold'
_i='h3cEntityExtShutdownTemperatureThreshold'
_h='h3cEntityExtCriticalTemperatureThreshold'
_g='h3cEntityExtVoltageHighThreshold'
_f='h3cEntityExtVoltageLowThreshold'
_e='h3cEntityExtPowerPhysicalIndex'
_d='h3cEntityExtManuPhysicalIndex'
_c='entPhysicalDescr'
_b='h3cEntityExtMemSizeRev'
_a='h3cEntityExtCpuUsageRecoverThreshold'
_Z='h3cEntityExtLowerTemperatureThreshold'
_Y='h3cEntityExtVoltage'
_X='h3cEntityExtTemperatureThreshold'
_W='h3cEntityExtMemSize'
_V='h3cEntityExtCpuUsageThreshold'
_U='h3cEntityExtCpuUsage'
_T='h3cEntityExtOperStatus'
_S='h3cEntityExtFirstTrapTime'
_R='notSupported'
_Q='h3cEntityExtNominalVoltage'
_P='h3cEntityExtCurrentVoltage'
_O='h3cEntityExtMemUsageThreshold'
_N='h3cEntityExtMemUsage'
_M='accessible-for-notify'
_L='h3cEntityExtErrorStatus'
_K='h3cEntityExtTemperature'
_J='read-write'
_I='Integer32'
_H='entPhysicalName'
_G='h3cEntityExtAlarmLight'
_F='ENTITY-MIB'
_E='h3cEntityExtAdminStatus'
_D='read-only'
_C='h3cEntityExtPhysicalIndex'
_B='current'
_A='H3C-ENTITY-EXT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_o,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalDescr,entPhysicalIndex,entPhysicalName=mibBuilder.importSymbols(_F,_c,'entPhysicalIndex',_H)
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_p)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_q,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_r,_s,'MacAddress','PhysAddress','TextualConvention')
h3cEntityExtend=ModuleIdentity((1,3,6,1,4,1,2011,10,2,6))
class H3cAdminState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),('locked',2),('shuttingDown',3),('unlocked',4)))
class H3cOperState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),('disabled',2),('enabled',3),('dangerous',4)))
class H3cAlarmStatus(TextualConvention,Bits):status=_B;namedValues=NamedValues(*((_R,0),('underRepair',1),('critical',2),('major',3),('minor',4),('alarmOutstanding',5),('warning',6),('indeterminate',7)))
class H3cStandbyStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),('hotStandby',2),('coldStandby',3),('providingService',4)))
_H3cEntityExtObjects_ObjectIdentity=ObjectIdentity
h3cEntityExtObjects=_H3cEntityExtObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,6,1))
_H3cEntityExtState_ObjectIdentity=ObjectIdentity
h3cEntityExtState=_H3cEntityExtState_ObjectIdentity((1,3,6,1,4,1,2011,10,2,6,1,1))
_H3cEntityExtStateTable_Object=MibTable
h3cEntityExtStateTable=_H3cEntityExtStateTable_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1))
if mibBuilder.loadTexts:h3cEntityExtStateTable.setStatus(_B)
_H3cEntityExtStateEntry_Object=MibTableRow
h3cEntityExtStateEntry=_H3cEntityExtStateEntry_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1))
h3cEntityExtStateEntry.setIndexNames((0,_A,_C))
if mibBuilder.loadTexts:h3cEntityExtStateEntry.setStatus(_B)
_H3cEntityExtPhysicalIndex_Type=Integer32
_H3cEntityExtPhysicalIndex_Object=MibTableColumn
h3cEntityExtPhysicalIndex=_H3cEntityExtPhysicalIndex_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,1),_H3cEntityExtPhysicalIndex_Type())
h3cEntityExtPhysicalIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cEntityExtPhysicalIndex.setStatus(_B)
_H3cEntityExtAdminStatus_Type=H3cAdminState
_H3cEntityExtAdminStatus_Object=MibTableColumn
h3cEntityExtAdminStatus=_H3cEntityExtAdminStatus_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,2),_H3cEntityExtAdminStatus_Type())
h3cEntityExtAdminStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cEntityExtAdminStatus.setStatus(_B)
_H3cEntityExtOperStatus_Type=H3cOperState
_H3cEntityExtOperStatus_Object=MibTableColumn
h3cEntityExtOperStatus=_H3cEntityExtOperStatus_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,3),_H3cEntityExtOperStatus_Type())
h3cEntityExtOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtOperStatus.setStatus(_B)
_H3cEntityExtStandbyStatus_Type=H3cStandbyStatus
_H3cEntityExtStandbyStatus_Object=MibTableColumn
h3cEntityExtStandbyStatus=_H3cEntityExtStandbyStatus_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,4),_H3cEntityExtStandbyStatus_Type())
h3cEntityExtStandbyStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtStandbyStatus.setStatus(_B)
_H3cEntityExtAlarmLight_Type=H3cAlarmStatus
_H3cEntityExtAlarmLight_Object=MibTableColumn
h3cEntityExtAlarmLight=_H3cEntityExtAlarmLight_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,5),_H3cEntityExtAlarmLight_Type())
h3cEntityExtAlarmLight.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtAlarmLight.setStatus(_B)
class _H3cEntityExtCpuUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cEntityExtCpuUsage_Type.__name__=_I
_H3cEntityExtCpuUsage_Object=MibTableColumn
h3cEntityExtCpuUsage=_H3cEntityExtCpuUsage_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,6),_H3cEntityExtCpuUsage_Type())
h3cEntityExtCpuUsage.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtCpuUsage.setStatus(_B)
class _H3cEntityExtCpuUsageThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cEntityExtCpuUsageThreshold_Type.__name__=_I
_H3cEntityExtCpuUsageThreshold_Object=MibTableColumn
h3cEntityExtCpuUsageThreshold=_H3cEntityExtCpuUsageThreshold_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,7),_H3cEntityExtCpuUsageThreshold_Type())
h3cEntityExtCpuUsageThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cEntityExtCpuUsageThreshold.setStatus(_B)
class _H3cEntityExtMemUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cEntityExtMemUsage_Type.__name__=_I
_H3cEntityExtMemUsage_Object=MibTableColumn
h3cEntityExtMemUsage=_H3cEntityExtMemUsage_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,8),_H3cEntityExtMemUsage_Type())
h3cEntityExtMemUsage.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtMemUsage.setStatus(_B)
class _H3cEntityExtMemUsageThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cEntityExtMemUsageThreshold_Type.__name__=_I
_H3cEntityExtMemUsageThreshold_Object=MibTableColumn
h3cEntityExtMemUsageThreshold=_H3cEntityExtMemUsageThreshold_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,9),_H3cEntityExtMemUsageThreshold_Type())
h3cEntityExtMemUsageThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cEntityExtMemUsageThreshold.setStatus(_B)
_H3cEntityExtMemSize_Type=Unsigned32
_H3cEntityExtMemSize_Object=MibTableColumn
h3cEntityExtMemSize=_H3cEntityExtMemSize_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,10),_H3cEntityExtMemSize_Type())
h3cEntityExtMemSize.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtMemSize.setStatus(_B)
if mibBuilder.loadTexts:h3cEntityExtMemSize.setUnits('bytes')
_H3cEntityExtUpTime_Type=Integer32
_H3cEntityExtUpTime_Object=MibTableColumn
h3cEntityExtUpTime=_H3cEntityExtUpTime_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,11),_H3cEntityExtUpTime_Type())
h3cEntityExtUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtUpTime.setStatus(_B)
if mibBuilder.loadTexts:h3cEntityExtUpTime.setUnits('seconds')
_H3cEntityExtTemperature_Type=Integer32
_H3cEntityExtTemperature_Object=MibTableColumn
h3cEntityExtTemperature=_H3cEntityExtTemperature_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,12),_H3cEntityExtTemperature_Type())
h3cEntityExtTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtTemperature.setStatus(_B)
_H3cEntityExtTemperatureThreshold_Type=Integer32
_H3cEntityExtTemperatureThreshold_Object=MibTableColumn
h3cEntityExtTemperatureThreshold=_H3cEntityExtTemperatureThreshold_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,13),_H3cEntityExtTemperatureThreshold_Type())
h3cEntityExtTemperatureThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cEntityExtTemperatureThreshold.setStatus(_B)
_H3cEntityExtVoltage_Type=Integer32
_H3cEntityExtVoltage_Object=MibTableColumn
h3cEntityExtVoltage=_H3cEntityExtVoltage_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,14),_H3cEntityExtVoltage_Type())
h3cEntityExtVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtVoltage.setStatus(_B)
_H3cEntityExtVoltageLowThreshold_Type=Integer32
_H3cEntityExtVoltageLowThreshold_Object=MibTableColumn
h3cEntityExtVoltageLowThreshold=_H3cEntityExtVoltageLowThreshold_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,15),_H3cEntityExtVoltageLowThreshold_Type())
h3cEntityExtVoltageLowThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cEntityExtVoltageLowThreshold.setStatus(_B)
_H3cEntityExtVoltageHighThreshold_Type=Integer32
_H3cEntityExtVoltageHighThreshold_Object=MibTableColumn
h3cEntityExtVoltageHighThreshold=_H3cEntityExtVoltageHighThreshold_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,16),_H3cEntityExtVoltageHighThreshold_Type())
h3cEntityExtVoltageHighThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cEntityExtVoltageHighThreshold.setStatus(_B)
_H3cEntityExtCriticalTemperatureThreshold_Type=Integer32
_H3cEntityExtCriticalTemperatureThreshold_Object=MibTableColumn
h3cEntityExtCriticalTemperatureThreshold=_H3cEntityExtCriticalTemperatureThreshold_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,17),_H3cEntityExtCriticalTemperatureThreshold_Type())
h3cEntityExtCriticalTemperatureThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cEntityExtCriticalTemperatureThreshold.setStatus(_B)
_H3cEntityExtMacAddress_Type=MacAddress
_H3cEntityExtMacAddress_Object=MibTableColumn
h3cEntityExtMacAddress=_H3cEntityExtMacAddress_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,18),_H3cEntityExtMacAddress_Type())
h3cEntityExtMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtMacAddress.setStatus(_B)
class _H3cEntityExtErrorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,11,21,22,23,31,32,33,41,51,61,71,81,91)));namedValues=NamedValues(*((_R,1),(_t,2),('postFailure',3),('entityAbsent',4),('poeError',11),('stackError',21),('stackPortBlocked',22),('stackPortFailed',23),('sfpRecvError',31),('sfpSendError',32),('sfpBothError',33),('fanError',41),('psuError',51),('rpsError',61),('moduleFaulty',71),('sensorError',81),('hardwareFaulty',91)))
_H3cEntityExtErrorStatus_Type.__name__=_I
_H3cEntityExtErrorStatus_Object=MibTableColumn
h3cEntityExtErrorStatus=_H3cEntityExtErrorStatus_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,19),_H3cEntityExtErrorStatus_Type())
h3cEntityExtErrorStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtErrorStatus.setStatus(_B)
class _H3cEntityExtCpuMaxUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cEntityExtCpuMaxUsage_Type.__name__=_I
_H3cEntityExtCpuMaxUsage_Object=MibTableColumn
h3cEntityExtCpuMaxUsage=_H3cEntityExtCpuMaxUsage_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,20),_H3cEntityExtCpuMaxUsage_Type())
h3cEntityExtCpuMaxUsage.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtCpuMaxUsage.setStatus(_B)
_H3cEntityExtLowerTemperatureThreshold_Type=Integer32
_H3cEntityExtLowerTemperatureThreshold_Object=MibTableColumn
h3cEntityExtLowerTemperatureThreshold=_H3cEntityExtLowerTemperatureThreshold_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,21),_H3cEntityExtLowerTemperatureThreshold_Type())
h3cEntityExtLowerTemperatureThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cEntityExtLowerTemperatureThreshold.setStatus(_B)
_H3cEntityExtShutdownTemperatureThreshold_Type=Integer32
_H3cEntityExtShutdownTemperatureThreshold_Object=MibTableColumn
h3cEntityExtShutdownTemperatureThreshold=_H3cEntityExtShutdownTemperatureThreshold_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,22),_H3cEntityExtShutdownTemperatureThreshold_Type())
h3cEntityExtShutdownTemperatureThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cEntityExtShutdownTemperatureThreshold.setStatus(_B)
_H3cEntityExtPhyMemSize_Type=Unsigned32
_H3cEntityExtPhyMemSize_Object=MibTableColumn
h3cEntityExtPhyMemSize=_H3cEntityExtPhyMemSize_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,23),_H3cEntityExtPhyMemSize_Type())
h3cEntityExtPhyMemSize.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtPhyMemSize.setStatus(_B)
_H3cEntityExtPhyCpuFrequency_Type=Integer32
_H3cEntityExtPhyCpuFrequency_Object=MibTableColumn
h3cEntityExtPhyCpuFrequency=_H3cEntityExtPhyCpuFrequency_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,24),_H3cEntityExtPhyCpuFrequency_Type())
h3cEntityExtPhyCpuFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtPhyCpuFrequency.setStatus(_B)
class _H3cEntityExtFirstUsedDate_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_H3cEntityExtFirstUsedDate_Type.__name__=_r
_H3cEntityExtFirstUsedDate_Object=MibTableColumn
h3cEntityExtFirstUsedDate=_H3cEntityExtFirstUsedDate_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,25),_H3cEntityExtFirstUsedDate_Type())
h3cEntityExtFirstUsedDate.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtFirstUsedDate.setStatus(_B)
class _H3cEntityExtCpuAvgUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cEntityExtCpuAvgUsage_Type.__name__=_I
_H3cEntityExtCpuAvgUsage_Object=MibTableColumn
h3cEntityExtCpuAvgUsage=_H3cEntityExtCpuAvgUsage_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,26),_H3cEntityExtCpuAvgUsage_Type())
h3cEntityExtCpuAvgUsage.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtCpuAvgUsage.setStatus(_B)
class _H3cEntityExtMemAvgUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cEntityExtMemAvgUsage_Type.__name__=_I
_H3cEntityExtMemAvgUsage_Object=MibTableColumn
h3cEntityExtMemAvgUsage=_H3cEntityExtMemAvgUsage_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,27),_H3cEntityExtMemAvgUsage_Type())
h3cEntityExtMemAvgUsage.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtMemAvgUsage.setStatus(_B)
class _H3cEntityExtMemType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_H3cEntityExtMemType_Type.__name__=_o
_H3cEntityExtMemType_Object=MibTableColumn
h3cEntityExtMemType=_H3cEntityExtMemType_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,28),_H3cEntityExtMemType_Type())
h3cEntityExtMemType.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtMemType.setStatus(_B)
_H3cEntityExtCriticalLowerTemperatureThreshold_Type=Integer32
_H3cEntityExtCriticalLowerTemperatureThreshold_Object=MibTableColumn
h3cEntityExtCriticalLowerTemperatureThreshold=_H3cEntityExtCriticalLowerTemperatureThreshold_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,29),_H3cEntityExtCriticalLowerTemperatureThreshold_Type())
h3cEntityExtCriticalLowerTemperatureThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cEntityExtCriticalLowerTemperatureThreshold.setStatus(_B)
_H3cEntityExtShutdownLowerTemperatureThreshold_Type=Integer32
_H3cEntityExtShutdownLowerTemperatureThreshold_Object=MibTableColumn
h3cEntityExtShutdownLowerTemperatureThreshold=_H3cEntityExtShutdownLowerTemperatureThreshold_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,30),_H3cEntityExtShutdownLowerTemperatureThreshold_Type())
h3cEntityExtShutdownLowerTemperatureThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cEntityExtShutdownLowerTemperatureThreshold.setStatus(_B)
class _H3cEntityExtCpuUsageRecoverThreshold_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cEntityExtCpuUsageRecoverThreshold_Type.__name__=_I
_H3cEntityExtCpuUsageRecoverThreshold_Object=MibTableColumn
h3cEntityExtCpuUsageRecoverThreshold=_H3cEntityExtCpuUsageRecoverThreshold_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,31),_H3cEntityExtCpuUsageRecoverThreshold_Type())
h3cEntityExtCpuUsageRecoverThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cEntityExtCpuUsageRecoverThreshold.setStatus(_B)
_H3cEntityExtMemSizeRev_Type=CounterBasedGauge64
_H3cEntityExtMemSizeRev_Object=MibTableColumn
h3cEntityExtMemSizeRev=_H3cEntityExtMemSizeRev_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,32),_H3cEntityExtMemSizeRev_Type())
h3cEntityExtMemSizeRev.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtMemSizeRev.setStatus(_B)
if mibBuilder.loadTexts:h3cEntityExtMemSizeRev.setUnits('bytes')
class _H3cEntityExtCpuUsageIn1Minute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cEntityExtCpuUsageIn1Minute_Type.__name__=_I
_H3cEntityExtCpuUsageIn1Minute_Object=MibTableColumn
h3cEntityExtCpuUsageIn1Minute=_H3cEntityExtCpuUsageIn1Minute_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,33),_H3cEntityExtCpuUsageIn1Minute_Type())
h3cEntityExtCpuUsageIn1Minute.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtCpuUsageIn1Minute.setStatus(_B)
class _H3cEntityExtCpuUsageIn5Minutes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cEntityExtCpuUsageIn5Minutes_Type.__name__=_I
_H3cEntityExtCpuUsageIn5Minutes_Object=MibTableColumn
h3cEntityExtCpuUsageIn5Minutes=_H3cEntityExtCpuUsageIn5Minutes_Object((1,3,6,1,4,1,2011,10,2,6,1,1,1,1,34),_H3cEntityExtCpuUsageIn5Minutes_Type())
h3cEntityExtCpuUsageIn5Minutes.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtCpuUsageIn5Minutes.setStatus(_B)
_H3cEntityExtManu_ObjectIdentity=ObjectIdentity
h3cEntityExtManu=_H3cEntityExtManu_ObjectIdentity((1,3,6,1,4,1,2011,10,2,6,1,2))
_H3cEntityExtManuTable_Object=MibTable
h3cEntityExtManuTable=_H3cEntityExtManuTable_Object((1,3,6,1,4,1,2011,10,2,6,1,2,1))
if mibBuilder.loadTexts:h3cEntityExtManuTable.setStatus(_B)
_H3cEntityExtManuEntry_Object=MibTableRow
h3cEntityExtManuEntry=_H3cEntityExtManuEntry_Object((1,3,6,1,4,1,2011,10,2,6,1,2,1,1))
h3cEntityExtManuEntry.setIndexNames((0,_A,_d))
if mibBuilder.loadTexts:h3cEntityExtManuEntry.setStatus(_B)
class _H3cEntityExtManuPhysicalIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cEntityExtManuPhysicalIndex_Type.__name__=_I
_H3cEntityExtManuPhysicalIndex_Object=MibTableColumn
h3cEntityExtManuPhysicalIndex=_H3cEntityExtManuPhysicalIndex_Object((1,3,6,1,4,1,2011,10,2,6,1,2,1,1,1),_H3cEntityExtManuPhysicalIndex_Type())
h3cEntityExtManuPhysicalIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cEntityExtManuPhysicalIndex.setStatus(_B)
_H3cEntityExtManuSerialNum_Type=SnmpAdminString
_H3cEntityExtManuSerialNum_Object=MibTableColumn
h3cEntityExtManuSerialNum=_H3cEntityExtManuSerialNum_Object((1,3,6,1,4,1,2011,10,2,6,1,2,1,1,2),_H3cEntityExtManuSerialNum_Type())
h3cEntityExtManuSerialNum.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtManuSerialNum.setStatus(_B)
_H3cEntityExtManuBuildInfo_Type=SnmpAdminString
_H3cEntityExtManuBuildInfo_Object=MibTableColumn
h3cEntityExtManuBuildInfo=_H3cEntityExtManuBuildInfo_Object((1,3,6,1,4,1,2011,10,2,6,1,2,1,1,3),_H3cEntityExtManuBuildInfo_Type())
h3cEntityExtManuBuildInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtManuBuildInfo.setStatus(_B)
_H3cEntityExtManuBOM_Type=SnmpAdminString
_H3cEntityExtManuBOM_Object=MibTableColumn
h3cEntityExtManuBOM=_H3cEntityExtManuBOM_Object((1,3,6,1,4,1,2011,10,2,6,1,2,1,1,4),_H3cEntityExtManuBOM_Type())
h3cEntityExtManuBOM.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtManuBOM.setStatus(_B)
_H3cEntityExtMacAddressCount_Type=Unsigned32
_H3cEntityExtMacAddressCount_Object=MibTableColumn
h3cEntityExtMacAddressCount=_H3cEntityExtMacAddressCount_Object((1,3,6,1,4,1,2011,10,2,6,1,2,1,1,5),_H3cEntityExtMacAddressCount_Type())
h3cEntityExtMacAddressCount.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtMacAddressCount.setStatus(_B)
_H3cEntityExtPower_ObjectIdentity=ObjectIdentity
h3cEntityExtPower=_H3cEntityExtPower_ObjectIdentity((1,3,6,1,4,1,2011,10,2,6,1,3))
_H3cEntityExtPowerTable_Object=MibTable
h3cEntityExtPowerTable=_H3cEntityExtPowerTable_Object((1,3,6,1,4,1,2011,10,2,6,1,3,1))
if mibBuilder.loadTexts:h3cEntityExtPowerTable.setStatus(_B)
_H3cEntityExtPowerEntry_Object=MibTableRow
h3cEntityExtPowerEntry=_H3cEntityExtPowerEntry_Object((1,3,6,1,4,1,2011,10,2,6,1,3,1,1))
h3cEntityExtPowerEntry.setIndexNames((0,_A,_e))
if mibBuilder.loadTexts:h3cEntityExtPowerEntry.setStatus(_B)
class _H3cEntityExtPowerPhysicalIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cEntityExtPowerPhysicalIndex_Type.__name__=_I
_H3cEntityExtPowerPhysicalIndex_Object=MibTableColumn
h3cEntityExtPowerPhysicalIndex=_H3cEntityExtPowerPhysicalIndex_Object((1,3,6,1,4,1,2011,10,2,6,1,3,1,1,1),_H3cEntityExtPowerPhysicalIndex_Type())
h3cEntityExtPowerPhysicalIndex.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cEntityExtPowerPhysicalIndex.setStatus(_B)
_H3cEntityExtNominalPower_Type=Gauge32
_H3cEntityExtNominalPower_Object=MibTableColumn
h3cEntityExtNominalPower=_H3cEntityExtNominalPower_Object((1,3,6,1,4,1,2011,10,2,6,1,3,1,1,2),_H3cEntityExtNominalPower_Type())
h3cEntityExtNominalPower.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtNominalPower.setStatus(_B)
_H3cEntityExtCurrentPower_Type=Gauge32
_H3cEntityExtCurrentPower_Object=MibTableColumn
h3cEntityExtCurrentPower=_H3cEntityExtCurrentPower_Object((1,3,6,1,4,1,2011,10,2,6,1,3,1,1,3),_H3cEntityExtCurrentPower_Type())
h3cEntityExtCurrentPower.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtCurrentPower.setStatus(_B)
_H3cEntityExtAveragePower_Type=Integer32
_H3cEntityExtAveragePower_Object=MibTableColumn
h3cEntityExtAveragePower=_H3cEntityExtAveragePower_Object((1,3,6,1,4,1,2011,10,2,6,1,3,1,1,4),_H3cEntityExtAveragePower_Type())
h3cEntityExtAveragePower.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cEntityExtAveragePower.setStatus(_B)
_H3cEntityExtPeakPower_Type=Integer32
_H3cEntityExtPeakPower_Object=MibTableColumn
h3cEntityExtPeakPower=_H3cEntityExtPeakPower_Object((1,3,6,1,4,1,2011,10,2,6,1,3,1,1,5),_H3cEntityExtPeakPower_Type())
h3cEntityExtPeakPower.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cEntityExtPeakPower.setStatus(_B)
_H3cProcessObjects_ObjectIdentity=ObjectIdentity
h3cProcessObjects=_H3cProcessObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,6,1,4))
_H3cProcessTable_Object=MibTable
h3cProcessTable=_H3cProcessTable_Object((1,3,6,1,4,1,2011,10,2,6,1,4,1))
if mibBuilder.loadTexts:h3cProcessTable.setStatus(_B)
_H3cProcessEntry_Object=MibTableRow
h3cProcessEntry=_H3cProcessEntry_Object((1,3,6,1,4,1,2011,10,2,6,1,4,1,1))
h3cProcessEntry.setIndexNames((0,_A,_u))
if mibBuilder.loadTexts:h3cProcessEntry.setStatus(_B)
_H3cProcessID_Type=Unsigned32
_H3cProcessID_Object=MibTableColumn
h3cProcessID=_H3cProcessID_Object((1,3,6,1,4,1,2011,10,2,6,1,4,1,1,1),_H3cProcessID_Type())
h3cProcessID.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cProcessID.setStatus(_B)
class _H3cProcessName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_H3cProcessName_Type.__name__=_s
_H3cProcessName_Object=MibTableColumn
h3cProcessName=_H3cProcessName_Object((1,3,6,1,4,1,2011,10,2,6,1,4,1,1,2),_H3cProcessName_Type())
h3cProcessName.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cProcessName.setStatus(_B)
class _H3cProcessUtil5Min_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_H3cProcessUtil5Min_Type.__name__=_q
_H3cProcessUtil5Min_Object=MibTableColumn
h3cProcessUtil5Min=_H3cProcessUtil5Min_Object((1,3,6,1,4,1,2011,10,2,6,1,4,1,1,3),_H3cProcessUtil5Min_Type())
h3cProcessUtil5Min.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cProcessUtil5Min.setStatus(_B)
_H3cEntityExtVoltageObjects_ObjectIdentity=ObjectIdentity
h3cEntityExtVoltageObjects=_H3cEntityExtVoltageObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,6,1,5))
_H3cEntityExtVoltageTable_Object=MibTable
h3cEntityExtVoltageTable=_H3cEntityExtVoltageTable_Object((1,3,6,1,4,1,2011,10,2,6,1,5,1))
if mibBuilder.loadTexts:h3cEntityExtVoltageTable.setStatus(_B)
_H3cEntityExtVoltageEntry_Object=MibTableRow
h3cEntityExtVoltageEntry=_H3cEntityExtVoltageEntry_Object((1,3,6,1,4,1,2011,10,2,6,1,5,1,1))
h3cEntityExtVoltageEntry.setIndexNames((0,_A,_C))
if mibBuilder.loadTexts:h3cEntityExtVoltageEntry.setStatus(_B)
_H3cEntityExtCurrentVoltage_Type=Integer32
_H3cEntityExtCurrentVoltage_Object=MibTableColumn
h3cEntityExtCurrentVoltage=_H3cEntityExtCurrentVoltage_Object((1,3,6,1,4,1,2011,10,2,6,1,5,1,1,1),_H3cEntityExtCurrentVoltage_Type())
h3cEntityExtCurrentVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtCurrentVoltage.setStatus(_B)
_H3cEntityExtNominalVoltage_Type=Integer32
_H3cEntityExtNominalVoltage_Object=MibTableColumn
h3cEntityExtNominalVoltage=_H3cEntityExtNominalVoltage_Object((1,3,6,1,4,1,2011,10,2,6,1,5,1,1,2),_H3cEntityExtNominalVoltage_Type())
h3cEntityExtNominalVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtNominalVoltage.setStatus(_B)
class _H3cEntityExtVoltageState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_t,0),('low',1),('tooLow',2),('high',3),('tooHigh',4)))
_H3cEntityExtVoltageState_Type.__name__=_I
_H3cEntityExtVoltageState_Object=MibTableColumn
h3cEntityExtVoltageState=_H3cEntityExtVoltageState_Object((1,3,6,1,4,1,2011,10,2,6,1,5,1,1,3),_H3cEntityExtVoltageState_Type())
h3cEntityExtVoltageState.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtVoltageState.setStatus(_B)
_H3cEntityExtVoltageMajorLowThreshold_Type=Integer32
_H3cEntityExtVoltageMajorLowThreshold_Object=MibTableColumn
h3cEntityExtVoltageMajorLowThreshold=_H3cEntityExtVoltageMajorLowThreshold_Object((1,3,6,1,4,1,2011,10,2,6,1,5,1,1,4),_H3cEntityExtVoltageMajorLowThreshold_Type())
h3cEntityExtVoltageMajorLowThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtVoltageMajorLowThreshold.setStatus(_B)
_H3cEntityExtVoltageFatalLowThreshold_Type=Integer32
_H3cEntityExtVoltageFatalLowThreshold_Object=MibTableColumn
h3cEntityExtVoltageFatalLowThreshold=_H3cEntityExtVoltageFatalLowThreshold_Object((1,3,6,1,4,1,2011,10,2,6,1,5,1,1,5),_H3cEntityExtVoltageFatalLowThreshold_Type())
h3cEntityExtVoltageFatalLowThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtVoltageFatalLowThreshold.setStatus(_B)
_H3cEntityExtVoltageMajorHighThreshold_Type=Integer32
_H3cEntityExtVoltageMajorHighThreshold_Object=MibTableColumn
h3cEntityExtVoltageMajorHighThreshold=_H3cEntityExtVoltageMajorHighThreshold_Object((1,3,6,1,4,1,2011,10,2,6,1,5,1,1,6),_H3cEntityExtVoltageMajorHighThreshold_Type())
h3cEntityExtVoltageMajorHighThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtVoltageMajorHighThreshold.setStatus(_B)
_H3cEntityExtVoltageFatalHighThreshold_Type=Integer32
_H3cEntityExtVoltageFatalHighThreshold_Object=MibTableColumn
h3cEntityExtVoltageFatalHighThreshold=_H3cEntityExtVoltageFatalHighThreshold_Object((1,3,6,1,4,1,2011,10,2,6,1,5,1,1,7),_H3cEntityExtVoltageFatalHighThreshold_Type())
h3cEntityExtVoltageFatalHighThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cEntityExtVoltageFatalHighThreshold.setStatus(_B)
_H3cEntityExtTraps_ObjectIdentity=ObjectIdentity
h3cEntityExtTraps=_H3cEntityExtTraps_ObjectIdentity((1,3,6,1,4,1,2011,10,2,6,2))
_H3cEntityExtTrapsPrefix_ObjectIdentity=ObjectIdentity
h3cEntityExtTrapsPrefix=_H3cEntityExtTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,6,2,0))
_H3cEntityExtTrapsInfor_ObjectIdentity=ObjectIdentity
h3cEntityExtTrapsInfor=_H3cEntityExtTrapsInfor_ObjectIdentity((1,3,6,1,4,1,2011,10,2,6,2,1))
class _H3cEntityExtTrapDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cEntityExtTrapDescription_Type.__name__=_p
_H3cEntityExtTrapDescription_Object=MibScalar
h3cEntityExtTrapDescription=_H3cEntityExtTrapDescription_Object((1,3,6,1,4,1,2011,10,2,6,2,1,1),_H3cEntityExtTrapDescription_Type())
h3cEntityExtTrapDescription.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cEntityExtTrapDescription.setStatus(_B)
class _H3cEntityExtECCParityAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('other',1),('l1cache',2),('l2cache',3),('sdram',4),('mac',5),('tcam',6),('ingressbuffer',7),('egressbuffer',8),('lpm',9),('controlmemory',10)))
_H3cEntityExtECCParityAlarmStatus_Type.__name__=_I
_H3cEntityExtECCParityAlarmStatus_Object=MibScalar
h3cEntityExtECCParityAlarmStatus=_H3cEntityExtECCParityAlarmStatus_Object((1,3,6,1,4,1,2011,10,2,6,2,1,2),_H3cEntityExtECCParityAlarmStatus_Type())
h3cEntityExtECCParityAlarmStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cEntityExtECCParityAlarmStatus.setStatus(_B)
_H3cEntityExtSFPInvalidInDays_Type=Integer32
_H3cEntityExtSFPInvalidInDays_Object=MibScalar
h3cEntityExtSFPInvalidInDays=_H3cEntityExtSFPInvalidInDays_Object((1,3,6,1,4,1,2011,10,2,6,2,1,3),_H3cEntityExtSFPInvalidInDays_Type())
h3cEntityExtSFPInvalidInDays.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cEntityExtSFPInvalidInDays.setStatus(_B)
_H3cEntityExtFirstTrapTime_Type=TimeTicks
_H3cEntityExtFirstTrapTime_Object=MibScalar
h3cEntityExtFirstTrapTime=_H3cEntityExtFirstTrapTime_Object((1,3,6,1,4,1,2011,10,2,6,2,1,4),_H3cEntityExtFirstTrapTime_Type())
h3cEntityExtFirstTrapTime.setMaxAccess(_M)
if mibBuilder.loadTexts:h3cEntityExtFirstTrapTime.setStatus(_B)
_H3cEntityExtConformance_ObjectIdentity=ObjectIdentity
h3cEntityExtConformance=_H3cEntityExtConformance_ObjectIdentity((1,3,6,1,4,1,2011,10,2,6,3))
_H3cEntityExtCompliances_ObjectIdentity=ObjectIdentity
h3cEntityExtCompliances=_H3cEntityExtCompliances_ObjectIdentity((1,3,6,1,4,1,2011,10,2,6,3,1))
_H3cEntityExtGroups_ObjectIdentity=ObjectIdentity
h3cEntityExtGroups=_H3cEntityExtGroups_ObjectIdentity((1,3,6,1,4,1,2011,10,2,6,3,2))
h3cEntityExtGroup=ObjectGroup((1,3,6,1,4,1,2011,10,2,6,3,2,1))
h3cEntityExtGroup.setObjects(*((_A,_C),(_A,_E),(_A,_T),(_A,_v),(_A,_G),(_A,_U),(_A,_V),(_A,_N),(_A,_O),(_A,_W),(_A,_w),(_A,_K),(_A,_X),(_A,_Y),(_A,_f),(_A,_g),(_A,_h),(_A,_x),(_A,_L),(_A,_y),(_A,_Z),(_A,_i),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_j),(_A,_k),(_A,_a),(_A,_b),(_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:h3cEntityExtGroup.setStatus(_B)
h3cEntityExtManuGroup=ObjectGroup((1,3,6,1,4,1,2011,10,2,6,3,2,3))
h3cEntityExtManuGroup.setObjects(*((_A,_d),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:h3cEntityExtManuGroup.setStatus(_B)
h3cEntityExtPowerGroup=ObjectGroup((1,3,6,1,4,1,2011,10,2,6,3,2,4))
h3cEntityExtPowerGroup.setObjects(*((_A,_e),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:h3cEntityExtPowerGroup.setStatus(_B)
h3cEntityExtTemperatureThresholdNotification=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,1))
h3cEntityExtTemperatureThresholdNotification.setObjects(*((_A,_C),(_A,_K),(_A,_X),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:h3cEntityExtTemperatureThresholdNotification.setStatus(_B)
h3cEntityExtVoltageLowThresholdNotification=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,2))
h3cEntityExtVoltageLowThresholdNotification.setObjects(*((_A,_C),(_A,_Y),(_A,_f),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:h3cEntityExtVoltageLowThresholdNotification.setStatus(_B)
h3cEntityExtVoltageHighThresholdNotification=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,3))
h3cEntityExtVoltageHighThresholdNotification.setObjects(*((_A,_C),(_A,_Y),(_A,_g),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:h3cEntityExtVoltageHighThresholdNotification.setStatus(_B)
h3cEntityExtCpuUsageThresholdNotfication=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,4))
h3cEntityExtCpuUsageThresholdNotfication.setObjects(*((_A,_C),(_A,_U),(_A,_V),(_A,_E),(_A,_G),(_A,_a),(_A,_S)))
if mibBuilder.loadTexts:h3cEntityExtCpuUsageThresholdNotfication.setStatus(_B)
h3cEntityExtMemUsageThresholdNotification=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,5))
h3cEntityExtMemUsageThresholdNotification.setObjects(*((_A,_C),(_A,_N),(_A,_O),(_A,_W),(_A,_E),(_A,_G),(_A,_S)))
if mibBuilder.loadTexts:h3cEntityExtMemUsageThresholdNotification.setStatus(_B)
h3cEntityExtOperEnabled=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,6))
h3cEntityExtOperEnabled.setObjects(*((_A,_C),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:h3cEntityExtOperEnabled.setStatus(_B)
h3cEntityExtOperDisabled=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,7))
h3cEntityExtOperDisabled.setObjects(*((_A,_C),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:h3cEntityExtOperDisabled.setStatus(_B)
h3cEntityExtCriticalTemperatureThresholdNotification=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,8))
h3cEntityExtCriticalTemperatureThresholdNotification.setObjects(*((_A,_C),(_A,_K),(_A,_h),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:h3cEntityExtCriticalTemperatureThresholdNotification.setStatus(_B)
h3cEntityExtSFPAlarmOn=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,9))
h3cEntityExtSFPAlarmOn.setObjects(*((_A,_C),(_A,_L),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:h3cEntityExtSFPAlarmOn.setStatus(_B)
h3cEntityExtSFPAlarmOff=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,10))
h3cEntityExtSFPAlarmOff.setObjects(*((_A,_C),(_A,_L),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:h3cEntityExtSFPAlarmOff.setStatus(_B)
h3cEntityExtSFPPhony=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,11))
h3cEntityExtSFPPhony.setObjects(*((_A,_C),(_F,_H),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:h3cEntityExtSFPPhony.setStatus(_B)
h3cEntityInsert=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,12))
h3cEntityInsert.setObjects(*((_F,_c),(_A,_E),(_A,_T)))
if mibBuilder.loadTexts:h3cEntityInsert.setStatus(_B)
h3cEntityRemove=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,13))
h3cEntityRemove.setObjects(*((_F,_c),(_A,_E),(_A,_T)))
if mibBuilder.loadTexts:h3cEntityRemove.setStatus(_B)
h3cEntityExtForcedPowerOff=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,14))
h3cEntityExtForcedPowerOff.setObjects(*((_A,_C),(_F,_H),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:h3cEntityExtForcedPowerOff.setStatus(_B)
h3cEntityExtForcedPowerOn=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,15))
h3cEntityExtForcedPowerOn.setObjects(*((_A,_C),(_F,_H),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:h3cEntityExtForcedPowerOn.setStatus(_B)
h3cEntityExtFaultAlarmOn=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,16))
h3cEntityExtFaultAlarmOn.setObjects(*((_A,_C),(_F,_H),(_A,_L),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:h3cEntityExtFaultAlarmOn.setStatus(_B)
h3cEntityExtFaultAlarmOff=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,17))
h3cEntityExtFaultAlarmOff.setObjects(*((_A,_C),(_F,_H),(_A,_L),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:h3cEntityExtFaultAlarmOff.setStatus(_B)
h3cEntityExtResourceLack=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,18))
h3cEntityExtResourceLack.setObjects(*((_A,_C),(_F,_H)))
if mibBuilder.loadTexts:h3cEntityExtResourceLack.setStatus(_B)
h3cEntityExtResourceEnough=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,19))
h3cEntityExtResourceEnough.setObjects(*((_A,_C),(_F,_H)))
if mibBuilder.loadTexts:h3cEntityExtResourceEnough.setStatus(_B)
h3cEntityExtTemperatureLower=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,20))
h3cEntityExtTemperatureLower.setObjects(*((_A,_C),(_F,_H),(_A,_K),(_A,_Z),(_A,_E)))
if mibBuilder.loadTexts:h3cEntityExtTemperatureLower.setStatus(_B)
h3cEntityExtTemperatureTooUp=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,21))
h3cEntityExtTemperatureTooUp.setObjects(*((_A,_C),(_F,_H),(_A,_K),(_A,_i),(_A,_E)))
if mibBuilder.loadTexts:h3cEntityExtTemperatureTooUp.setStatus(_B)
h3cEntityExtTemperatureNormal=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,22))
h3cEntityExtTemperatureNormal.setObjects(*((_A,_C),(_F,_H),(_A,_K),(_A,_Z),(_A,_X),(_A,_E)))
if mibBuilder.loadTexts:h3cEntityExtTemperatureNormal.setStatus(_B)
h3cEntityExternalAlarmOccur=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,23))
h3cEntityExternalAlarmOccur.setObjects(*((_A,_C),(_F,_H)))
if mibBuilder.loadTexts:h3cEntityExternalAlarmOccur.setStatus(_B)
h3cEntityExternalAlarmRecover=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,24))
h3cEntityExternalAlarmRecover.setObjects(*((_A,_C),(_F,_H)))
if mibBuilder.loadTexts:h3cEntityExternalAlarmRecover.setStatus(_B)
h3cEntityExtCpuUsageThresholdRecover=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,25))
h3cEntityExtCpuUsageThresholdRecover.setObjects(*((_A,_C),(_A,_U),(_A,_V),(_A,_E),(_A,_G),(_A,_a),(_A,_S)))
if mibBuilder.loadTexts:h3cEntityExtCpuUsageThresholdRecover.setStatus(_B)
h3cEntityExtMemUsageThresholdRecover=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,26))
h3cEntityExtMemUsageThresholdRecover.setObjects(*((_A,_C),(_A,_N),(_A,_O),(_A,_W),(_A,_E),(_A,_G),(_A,_S)))
if mibBuilder.loadTexts:h3cEntityExtMemUsageThresholdRecover.setStatus(_B)
h3cEntityExtMemAllocatedFailed=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,27))
h3cEntityExtMemAllocatedFailed.setObjects(*((_A,_C),(_A,_l)))
if mibBuilder.loadTexts:h3cEntityExtMemAllocatedFailed.setStatus(_B)
h3cEntityExtECCParityAlarm=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,28))
h3cEntityExtECCParityAlarm.setObjects(*((_A,_C),(_A,_AF),(_A,_l)))
if mibBuilder.loadTexts:h3cEntityExtECCParityAlarm.setStatus(_B)
h3cEntityExtCritLowerTempThresholdNotification=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,29))
h3cEntityExtCritLowerTempThresholdNotification.setObjects(*((_A,_C),(_F,_H),(_A,_K),(_A,_j)))
if mibBuilder.loadTexts:h3cEntityExtCritLowerTempThresholdNotification.setStatus(_B)
h3cEntityExtTemperatureTooLow=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,30))
h3cEntityExtTemperatureTooLow.setObjects(*((_A,_C),(_F,_H),(_A,_K),(_A,_k)))
if mibBuilder.loadTexts:h3cEntityExtTemperatureTooLow.setStatus(_B)
h3cEntityExtFanDirectionNotPreferred=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,31))
h3cEntityExtFanDirectionNotPreferred.setObjects(*((_A,_C),(_F,_H)))
if mibBuilder.loadTexts:h3cEntityExtFanDirectionNotPreferred.setStatus(_B)
h3cEntityExtFanDirectionNotAccord=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,32))
h3cEntityExtFanDirectionNotAccord.setObjects(*((_A,_C),(_F,_H)))
if mibBuilder.loadTexts:h3cEntityExtFanDirectionNotAccord.setStatus(_B)
h3cEntityExtSFPInvalid=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,33))
h3cEntityExtSFPInvalid.setObjects(*((_A,_C),(_F,_H),(_A,_AG)))
if mibBuilder.loadTexts:h3cEntityExtSFPInvalid.setStatus(_B)
h3cEntityExtSFPInvalidNow=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,34))
h3cEntityExtSFPInvalidNow.setObjects(*((_A,_C),(_F,_H)))
if mibBuilder.loadTexts:h3cEntityExtSFPInvalidNow.setStatus(_B)
h3cEntityExtMemUsageThresholdOverTrap=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,35))
h3cEntityExtMemUsageThresholdOverTrap.setObjects(*((_A,_C),(_A,_N),(_A,_O),(_A,_b),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:h3cEntityExtMemUsageThresholdOverTrap.setStatus(_B)
h3cEntityExtMemUsageThresholdRecoverTrap=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,36))
h3cEntityExtMemUsageThresholdRecoverTrap.setObjects(*((_A,_C),(_A,_N),(_A,_O),(_A,_b),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:h3cEntityExtMemUsageThresholdRecoverTrap.setStatus(_B)
h3cEntityExtVoltageNormal=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,37))
h3cEntityExtVoltageNormal.setObjects(*((_A,_C),(_A,_P),(_A,_Q),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:h3cEntityExtVoltageNormal.setStatus(_B)
h3cEntityExtVoltageLower=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,38))
h3cEntityExtVoltageLower.setObjects(*((_A,_C),(_A,_P),(_A,_Q),(_A,_m)))
if mibBuilder.loadTexts:h3cEntityExtVoltageLower.setStatus(_B)
h3cEntityExtVoltageTooLow=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,39))
h3cEntityExtVoltageTooLow.setObjects(*((_A,_C),(_A,_P),(_A,_Q),(_A,_AH)))
if mibBuilder.loadTexts:h3cEntityExtVoltageTooLow.setStatus(_B)
h3cEntityExtVoltageHigher=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,40))
h3cEntityExtVoltageHigher.setObjects(*((_A,_C),(_A,_P),(_A,_Q),(_A,_n)))
if mibBuilder.loadTexts:h3cEntityExtVoltageHigher.setStatus(_B)
h3cEntityExtVoltageTooHigh=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,41))
h3cEntityExtVoltageTooHigh.setObjects(*((_A,_C),(_A,_P),(_A,_Q),(_A,_AI)))
if mibBuilder.loadTexts:h3cEntityExtVoltageTooHigh.setStatus(_B)
h3cEntityExtSFPAlarmOnEx=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,42))
h3cEntityExtSFPAlarmOnEx.setObjects(*((_A,_C),(_F,_H),(_A,_E),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:h3cEntityExtSFPAlarmOnEx.setStatus(_B)
h3cEntityExtSFPAlarmOffEx=NotificationType((1,3,6,1,4,1,2011,10,2,6,2,0,43))
h3cEntityExtSFPAlarmOffEx.setObjects(*((_A,_C),(_F,_H),(_A,_E),(_A,_G),(_A,_L)))
if mibBuilder.loadTexts:h3cEntityExtSFPAlarmOffEx.setStatus(_B)
h3cEntityExtNotificationGroup=NotificationGroup((1,3,6,1,4,1,2011,10,2,6,3,2,2))
h3cEntityExtNotificationGroup.setObjects(*((_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az)))
if mibBuilder.loadTexts:h3cEntityExtNotificationGroup.setStatus(_B)
h3cEntityExtCompliance=ModuleCompliance((1,3,6,1,4,1,2011,10,2,6,3,1,1))
h3cEntityExtCompliance.setObjects(*((_A,_A_),(_A,_B0),(_A,_B1),(_A,_B2)))
if mibBuilder.loadTexts:h3cEntityExtCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'H3cAdminState':H3cAdminState,'H3cOperState':H3cOperState,'H3cAlarmStatus':H3cAlarmStatus,'H3cStandbyStatus':H3cStandbyStatus,'h3cEntityExtend':h3cEntityExtend,'h3cEntityExtObjects':h3cEntityExtObjects,'h3cEntityExtState':h3cEntityExtState,'h3cEntityExtStateTable':h3cEntityExtStateTable,'h3cEntityExtStateEntry':h3cEntityExtStateEntry,_C:h3cEntityExtPhysicalIndex,_E:h3cEntityExtAdminStatus,_T:h3cEntityExtOperStatus,_v:h3cEntityExtStandbyStatus,_G:h3cEntityExtAlarmLight,_U:h3cEntityExtCpuUsage,_V:h3cEntityExtCpuUsageThreshold,_N:h3cEntityExtMemUsage,_O:h3cEntityExtMemUsageThreshold,_W:h3cEntityExtMemSize,_w:h3cEntityExtUpTime,_K:h3cEntityExtTemperature,_X:h3cEntityExtTemperatureThreshold,_Y:h3cEntityExtVoltage,_f:h3cEntityExtVoltageLowThreshold,_g:h3cEntityExtVoltageHighThreshold,_h:h3cEntityExtCriticalTemperatureThreshold,_x:h3cEntityExtMacAddress,_L:h3cEntityExtErrorStatus,_y:h3cEntityExtCpuMaxUsage,_Z:h3cEntityExtLowerTemperatureThreshold,_i:h3cEntityExtShutdownTemperatureThreshold,_z:h3cEntityExtPhyMemSize,_A0:h3cEntityExtPhyCpuFrequency,_A1:h3cEntityExtFirstUsedDate,_A2:h3cEntityExtCpuAvgUsage,_A3:h3cEntityExtMemAvgUsage,_A4:h3cEntityExtMemType,_j:h3cEntityExtCriticalLowerTemperatureThreshold,_k:h3cEntityExtShutdownLowerTemperatureThreshold,_a:h3cEntityExtCpuUsageRecoverThreshold,_b:h3cEntityExtMemSizeRev,_A5:h3cEntityExtCpuUsageIn1Minute,_A6:h3cEntityExtCpuUsageIn5Minutes,'h3cEntityExtManu':h3cEntityExtManu,'h3cEntityExtManuTable':h3cEntityExtManuTable,'h3cEntityExtManuEntry':h3cEntityExtManuEntry,_d:h3cEntityExtManuPhysicalIndex,_A7:h3cEntityExtManuSerialNum,_A8:h3cEntityExtManuBuildInfo,_A9:h3cEntityExtManuBOM,_AA:h3cEntityExtMacAddressCount,'h3cEntityExtPower':h3cEntityExtPower,'h3cEntityExtPowerTable':h3cEntityExtPowerTable,'h3cEntityExtPowerEntry':h3cEntityExtPowerEntry,_e:h3cEntityExtPowerPhysicalIndex,_AB:h3cEntityExtNominalPower,_AC:h3cEntityExtCurrentPower,_AD:h3cEntityExtAveragePower,_AE:h3cEntityExtPeakPower,'h3cProcessObjects':h3cProcessObjects,'h3cProcessTable':h3cProcessTable,'h3cProcessEntry':h3cProcessEntry,_u:h3cProcessID,'h3cProcessName':h3cProcessName,'h3cProcessUtil5Min':h3cProcessUtil5Min,'h3cEntityExtVoltageObjects':h3cEntityExtVoltageObjects,'h3cEntityExtVoltageTable':h3cEntityExtVoltageTable,'h3cEntityExtVoltageEntry':h3cEntityExtVoltageEntry,_P:h3cEntityExtCurrentVoltage,_Q:h3cEntityExtNominalVoltage,'h3cEntityExtVoltageState':h3cEntityExtVoltageState,_m:h3cEntityExtVoltageMajorLowThreshold,_AH:h3cEntityExtVoltageFatalLowThreshold,_n:h3cEntityExtVoltageMajorHighThreshold,_AI:h3cEntityExtVoltageFatalHighThreshold,'h3cEntityExtTraps':h3cEntityExtTraps,'h3cEntityExtTrapsPrefix':h3cEntityExtTrapsPrefix,_AJ:h3cEntityExtTemperatureThresholdNotification,_AK:h3cEntityExtVoltageLowThresholdNotification,_AL:h3cEntityExtVoltageHighThresholdNotification,_AM:h3cEntityExtCpuUsageThresholdNotfication,_AN:h3cEntityExtMemUsageThresholdNotification,_AO:h3cEntityExtOperEnabled,_AP:h3cEntityExtOperDisabled,_AQ:h3cEntityExtCriticalTemperatureThresholdNotification,_AR:h3cEntityExtSFPAlarmOn,_AS:h3cEntityExtSFPAlarmOff,_AT:h3cEntityExtSFPPhony,_AU:h3cEntityInsert,_AV:h3cEntityRemove,_AW:h3cEntityExtForcedPowerOff,_AX:h3cEntityExtForcedPowerOn,_AY:h3cEntityExtFaultAlarmOn,_AZ:h3cEntityExtFaultAlarmOff,_Aa:h3cEntityExtResourceLack,_Ab:h3cEntityExtResourceEnough,_Ac:h3cEntityExtTemperatureLower,_Ad:h3cEntityExtTemperatureTooUp,_Ae:h3cEntityExtTemperatureNormal,_Af:h3cEntityExternalAlarmOccur,_Ag:h3cEntityExternalAlarmRecover,_Ah:h3cEntityExtCpuUsageThresholdRecover,_Ai:h3cEntityExtMemUsageThresholdRecover,_Aj:h3cEntityExtMemAllocatedFailed,_Ak:h3cEntityExtECCParityAlarm,_Al:h3cEntityExtCritLowerTempThresholdNotification,_Am:h3cEntityExtTemperatureTooLow,_An:h3cEntityExtFanDirectionNotPreferred,_Ao:h3cEntityExtFanDirectionNotAccord,_Ap:h3cEntityExtSFPInvalid,_Aq:h3cEntityExtSFPInvalidNow,_Ar:h3cEntityExtMemUsageThresholdOverTrap,_As:h3cEntityExtMemUsageThresholdRecoverTrap,_At:h3cEntityExtVoltageNormal,_Av:h3cEntityExtVoltageLower,_Au:h3cEntityExtVoltageTooLow,_Aw:h3cEntityExtVoltageHigher,_Ax:h3cEntityExtVoltageTooHigh,_Ay:h3cEntityExtSFPAlarmOnEx,_Az:h3cEntityExtSFPAlarmOffEx,'h3cEntityExtTrapsInfor':h3cEntityExtTrapsInfor,_l:h3cEntityExtTrapDescription,_AF:h3cEntityExtECCParityAlarmStatus,_AG:h3cEntityExtSFPInvalidInDays,_S:h3cEntityExtFirstTrapTime,'h3cEntityExtConformance':h3cEntityExtConformance,'h3cEntityExtCompliances':h3cEntityExtCompliances,'h3cEntityExtCompliance':h3cEntityExtCompliance,'h3cEntityExtGroups':h3cEntityExtGroups,_A_:h3cEntityExtGroup,_B0:h3cEntityExtNotificationGroup,_B1:h3cEntityExtManuGroup,_B2:h3cEntityExtPowerGroup})