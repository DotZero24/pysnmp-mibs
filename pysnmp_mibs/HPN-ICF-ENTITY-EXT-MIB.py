_B0='hpnicfEntityExtPowerGroup'
_A_='hpnicfEntityExtManuGroup'
_Az='hpnicfEntityExtNotificationGroup'
_Ay='hpnicfEntityExtGroup'
_Ax='hpnicfEntityExtVoltageTooHigh'
_Aw='hpnicfEntityExtVoltageHigher'
_Av='hpnicfEntityExtVoltageLower'
_Au='hpnicfEntityExtVoltageTooLow'
_At='hpnicfEntityExtVoltageNormal'
_As='hpnicfEntityExtMemUsageThresholdRecoverTrap'
_Ar='hpnicfEntityExtMemUsageThresholdOverTrap'
_Aq='hpnicfEntityExtSFPInvalidNow'
_Ap='hpnicfEntityExtSFPInvalid'
_Ao='hpnicfEntityExtFanDirectionNotAccord'
_An='hpnicfEntityExtFanDirectionNotPreferred'
_Am='hpnicfEntityExtTemperatureTooLow'
_Al='hpnicfEntityExtCritLowerTempThresholdNotification'
_Ak='hpnicfEntityExtECCParityAlarm'
_Aj='hpnicfEntityExtMemAllocatedFailed'
_Ai='hpnicfEntityExtMemUsageThresholdRecover'
_Ah='hpnicfEntityExtCpuUsageThresholdRecover'
_Ag='hpnicfEntityExternalAlarmRecover'
_Af='hpnicfEntityExternalAlarmOccur'
_Ae='hpnicfEntityExtTemperatureNormal'
_Ad='hpnicfEntityExtTemperatureTooUp'
_Ac='hpnicfEntityExtTemperatureLower'
_Ab='hpnicfEntityExtResourceEnough'
_Aa='hpnicfEntityExtResourceLack'
_AZ='hpnicfEntityExtFaultAlarmOff'
_AY='hpnicfEntityExtFaultAlarmOn'
_AX='hpnicfEntityExtForcedPowerOn'
_AW='hpnicfEntityExtForcedPowerOff'
_AV='hpnicfEntityRemove'
_AU='hpnicfEntityInsert'
_AT='hpnicfEntityExtSFPPhony'
_AS='hpnicfEntityExtSFPAlarmOff'
_AR='hpnicfEntityExtSFPAlarmOn'
_AQ='hpnicfEntityExtCriticalTemperatureThresholdNotification'
_AP='hpnicfEntityExtOperDisabled'
_AO='hpnicfEntityExtOperEnabled'
_AN='hpnicfEntityExtMemUsageThresholdNotification'
_AM='hpnicfEntityExtCpuUsageThresholdNotfication'
_AL='hpnicfEntityExtVoltageHighThresholdNotification'
_AK='hpnicfEntityExtVoltageLowThresholdNotification'
_AJ='hpnicfEntityExtTemperatureThresholdNotification'
_AI='hpnicfEntityExtVoltageFatalHighThreshold'
_AH='hpnicfEntityExtVoltageFatalLowThreshold'
_AG='hpnicfEntityExtSFPInvalidInDays'
_AF='hpnicfEntityExtECCParityAlarmStatus'
_AE='hpnicfEntityExtPeakPower'
_AD='hpnicfEntityExtAveragePower'
_AC='hpnicfEntityExtCurrentPower'
_AB='hpnicfEntityExtNominalPower'
_AA='hpnicfEntityExtMacAddressCount'
_A9='hpnicfEntityExtManuBOM'
_A8='hpnicfEntityExtManuBuildInfo'
_A7='hpnicfEntityExtManuSerialNum'
_A6='hpnicfEntityExtCpuUsageIn5Minutes'
_A5='hpnicfEntityExtCpuUsageIn1Minute'
_A4='hpnicfEntityExtMemType'
_A3='hpnicfEntityExtMemAvgUsage'
_A2='hpnicfEntityExtCpuAvgUsage'
_A1='hpnicfEntityExtFirstUsedDate'
_A0='hpnicfEntityExtPhyCpuFrequency'
_z='hpnicfEntityExtPhyMemSize'
_y='hpnicfEntityExtCpuMaxUsage'
_x='hpnicfEntityExtMacAddress'
_w='hpnicfEntityExtUpTime'
_v='hpnicfEntityExtStandbyStatus'
_u='hpnicfProcessID'
_t='normal'
_s='DisplayString'
_r='DateAndTime'
_q='Unsigned32'
_p='SnmpAdminString'
_o='OctetString'
_n='hpnicfEntityExtVoltageMajorHighThreshold'
_m='hpnicfEntityExtVoltageMajorLowThreshold'
_l='hpnicfEntityExtTrapDescription'
_k='hpnicfEntityExtShutdownLowerTemperatureThreshold'
_j='hpnicfEntityExtCriticalLowerTemperatureThreshold'
_i='hpnicfEntityExtShutdownTemperatureThreshold'
_h='hpnicfEntityExtCriticalTemperatureThreshold'
_g='hpnicfEntityExtVoltageHighThreshold'
_f='hpnicfEntityExtVoltageLowThreshold'
_e='hpnicfEntityExtPowerPhysicalIndex'
_d='hpnicfEntityExtManuPhysicalIndex'
_c='entPhysicalDescr'
_b='hpnicfEntityExtMemSizeRev'
_a='hpnicfEntityExtCpuUsageRecoverThreshold'
_Z='hpnicfEntityExtLowerTemperatureThreshold'
_Y='hpnicfEntityExtVoltage'
_X='hpnicfEntityExtTemperatureThreshold'
_W='hpnicfEntityExtMemSize'
_V='hpnicfEntityExtCpuUsageThreshold'
_U='hpnicfEntityExtCpuUsage'
_T='hpnicfEntityExtOperStatus'
_S='hpnicfEntityExtFirstTrapTime'
_R='notSupported'
_Q='hpnicfEntityExtNominalVoltage'
_P='hpnicfEntityExtCurrentVoltage'
_O='hpnicfEntityExtErrorStatus'
_N='hpnicfEntityExtMemUsageThreshold'
_M='hpnicfEntityExtMemUsage'
_L='accessible-for-notify'
_K='hpnicfEntityExtTemperature'
_J='read-write'
_I='Integer32'
_H='entPhysicalName'
_G='hpnicfEntityExtAlarmLight'
_F='ENTITY-MIB'
_E='hpnicfEntityExtAdminStatus'
_D='read-only'
_C='hpnicfEntityExtPhysicalIndex'
_B='current'
_A='HPN-ICF-ENTITY-EXT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_o,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalDescr,entPhysicalIndex,entPhysicalName=mibBuilder.importSymbols(_F,_c,'entPhysicalIndex',_H)
CounterBasedGauge64,=mibBuilder.importSymbols('HCNUM-TC','CounterBasedGauge64')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_p)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_q,'iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_r,_s,'MacAddress','PhysAddress','TextualConvention')
hpnicfEntityExtend=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,6))
class HpnicfAdminState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),('locked',2),('shuttingDown',3),('unlocked',4)))
class HpnicfOperState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),('disabled',2),('enabled',3),('dangerous',4)))
class HpnicfAlarmStatus(TextualConvention,Bits):status=_B;namedValues=NamedValues(*((_R,0),('underRepair',1),('critical',2),('major',3),('minor',4),('alarmOutstanding',5),('warning',6),('indeterminate',7)))
class HpnicfStandbyStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),('hotStandby',2),('coldStandby',3),('providingService',4)))
_HpnicfEntityExtObjects_ObjectIdentity=ObjectIdentity
hpnicfEntityExtObjects=_HpnicfEntityExtObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,6,1))
_HpnicfEntityExtState_ObjectIdentity=ObjectIdentity
hpnicfEntityExtState=_HpnicfEntityExtState_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1))
_HpnicfEntityExtStateTable_Object=MibTable
hpnicfEntityExtStateTable=_HpnicfEntityExtStateTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1))
if mibBuilder.loadTexts:hpnicfEntityExtStateTable.setStatus(_B)
_HpnicfEntityExtStateEntry_Object=MibTableRow
hpnicfEntityExtStateEntry=_HpnicfEntityExtStateEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1))
hpnicfEntityExtStateEntry.setIndexNames((0,_A,_C))
if mibBuilder.loadTexts:hpnicfEntityExtStateEntry.setStatus(_B)
_HpnicfEntityExtPhysicalIndex_Type=Integer32
_HpnicfEntityExtPhysicalIndex_Object=MibTableColumn
hpnicfEntityExtPhysicalIndex=_HpnicfEntityExtPhysicalIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,1),_HpnicfEntityExtPhysicalIndex_Type())
hpnicfEntityExtPhysicalIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:hpnicfEntityExtPhysicalIndex.setStatus(_B)
_HpnicfEntityExtAdminStatus_Type=HpnicfAdminState
_HpnicfEntityExtAdminStatus_Object=MibTableColumn
hpnicfEntityExtAdminStatus=_HpnicfEntityExtAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,2),_HpnicfEntityExtAdminStatus_Type())
hpnicfEntityExtAdminStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfEntityExtAdminStatus.setStatus(_B)
_HpnicfEntityExtOperStatus_Type=HpnicfOperState
_HpnicfEntityExtOperStatus_Object=MibTableColumn
hpnicfEntityExtOperStatus=_HpnicfEntityExtOperStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,3),_HpnicfEntityExtOperStatus_Type())
hpnicfEntityExtOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtOperStatus.setStatus(_B)
_HpnicfEntityExtStandbyStatus_Type=HpnicfStandbyStatus
_HpnicfEntityExtStandbyStatus_Object=MibTableColumn
hpnicfEntityExtStandbyStatus=_HpnicfEntityExtStandbyStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,4),_HpnicfEntityExtStandbyStatus_Type())
hpnicfEntityExtStandbyStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtStandbyStatus.setStatus(_B)
_HpnicfEntityExtAlarmLight_Type=HpnicfAlarmStatus
_HpnicfEntityExtAlarmLight_Object=MibTableColumn
hpnicfEntityExtAlarmLight=_HpnicfEntityExtAlarmLight_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,5),_HpnicfEntityExtAlarmLight_Type())
hpnicfEntityExtAlarmLight.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtAlarmLight.setStatus(_B)
class _HpnicfEntityExtCpuUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfEntityExtCpuUsage_Type.__name__=_I
_HpnicfEntityExtCpuUsage_Object=MibTableColumn
hpnicfEntityExtCpuUsage=_HpnicfEntityExtCpuUsage_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,6),_HpnicfEntityExtCpuUsage_Type())
hpnicfEntityExtCpuUsage.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtCpuUsage.setStatus(_B)
class _HpnicfEntityExtCpuUsageThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfEntityExtCpuUsageThreshold_Type.__name__=_I
_HpnicfEntityExtCpuUsageThreshold_Object=MibTableColumn
hpnicfEntityExtCpuUsageThreshold=_HpnicfEntityExtCpuUsageThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,7),_HpnicfEntityExtCpuUsageThreshold_Type())
hpnicfEntityExtCpuUsageThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfEntityExtCpuUsageThreshold.setStatus(_B)
class _HpnicfEntityExtMemUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfEntityExtMemUsage_Type.__name__=_I
_HpnicfEntityExtMemUsage_Object=MibTableColumn
hpnicfEntityExtMemUsage=_HpnicfEntityExtMemUsage_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,8),_HpnicfEntityExtMemUsage_Type())
hpnicfEntityExtMemUsage.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtMemUsage.setStatus(_B)
class _HpnicfEntityExtMemUsageThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfEntityExtMemUsageThreshold_Type.__name__=_I
_HpnicfEntityExtMemUsageThreshold_Object=MibTableColumn
hpnicfEntityExtMemUsageThreshold=_HpnicfEntityExtMemUsageThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,9),_HpnicfEntityExtMemUsageThreshold_Type())
hpnicfEntityExtMemUsageThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfEntityExtMemUsageThreshold.setStatus(_B)
_HpnicfEntityExtMemSize_Type=Unsigned32
_HpnicfEntityExtMemSize_Object=MibTableColumn
hpnicfEntityExtMemSize=_HpnicfEntityExtMemSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,10),_HpnicfEntityExtMemSize_Type())
hpnicfEntityExtMemSize.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtMemSize.setStatus(_B)
if mibBuilder.loadTexts:hpnicfEntityExtMemSize.setUnits('bytes')
_HpnicfEntityExtUpTime_Type=Integer32
_HpnicfEntityExtUpTime_Object=MibTableColumn
hpnicfEntityExtUpTime=_HpnicfEntityExtUpTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,11),_HpnicfEntityExtUpTime_Type())
hpnicfEntityExtUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtUpTime.setStatus(_B)
if mibBuilder.loadTexts:hpnicfEntityExtUpTime.setUnits('seconds')
_HpnicfEntityExtTemperature_Type=Integer32
_HpnicfEntityExtTemperature_Object=MibTableColumn
hpnicfEntityExtTemperature=_HpnicfEntityExtTemperature_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,12),_HpnicfEntityExtTemperature_Type())
hpnicfEntityExtTemperature.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtTemperature.setStatus(_B)
_HpnicfEntityExtTemperatureThreshold_Type=Integer32
_HpnicfEntityExtTemperatureThreshold_Object=MibTableColumn
hpnicfEntityExtTemperatureThreshold=_HpnicfEntityExtTemperatureThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,13),_HpnicfEntityExtTemperatureThreshold_Type())
hpnicfEntityExtTemperatureThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfEntityExtTemperatureThreshold.setStatus(_B)
_HpnicfEntityExtVoltage_Type=Integer32
_HpnicfEntityExtVoltage_Object=MibTableColumn
hpnicfEntityExtVoltage=_HpnicfEntityExtVoltage_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,14),_HpnicfEntityExtVoltage_Type())
hpnicfEntityExtVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtVoltage.setStatus(_B)
_HpnicfEntityExtVoltageLowThreshold_Type=Integer32
_HpnicfEntityExtVoltageLowThreshold_Object=MibTableColumn
hpnicfEntityExtVoltageLowThreshold=_HpnicfEntityExtVoltageLowThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,15),_HpnicfEntityExtVoltageLowThreshold_Type())
hpnicfEntityExtVoltageLowThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfEntityExtVoltageLowThreshold.setStatus(_B)
_HpnicfEntityExtVoltageHighThreshold_Type=Integer32
_HpnicfEntityExtVoltageHighThreshold_Object=MibTableColumn
hpnicfEntityExtVoltageHighThreshold=_HpnicfEntityExtVoltageHighThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,16),_HpnicfEntityExtVoltageHighThreshold_Type())
hpnicfEntityExtVoltageHighThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfEntityExtVoltageHighThreshold.setStatus(_B)
_HpnicfEntityExtCriticalTemperatureThreshold_Type=Integer32
_HpnicfEntityExtCriticalTemperatureThreshold_Object=MibTableColumn
hpnicfEntityExtCriticalTemperatureThreshold=_HpnicfEntityExtCriticalTemperatureThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,17),_HpnicfEntityExtCriticalTemperatureThreshold_Type())
hpnicfEntityExtCriticalTemperatureThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfEntityExtCriticalTemperatureThreshold.setStatus(_B)
_HpnicfEntityExtMacAddress_Type=MacAddress
_HpnicfEntityExtMacAddress_Object=MibTableColumn
hpnicfEntityExtMacAddress=_HpnicfEntityExtMacAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,18),_HpnicfEntityExtMacAddress_Type())
hpnicfEntityExtMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtMacAddress.setStatus(_B)
class _HpnicfEntityExtErrorStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,11,21,22,23,31,32,33,41,51,61,71,81,91)));namedValues=NamedValues(*((_R,1),(_t,2),('postFailure',3),('entityAbsent',4),('poeError',11),('stackError',21),('stackPortBlocked',22),('stackPortFailed',23),('sfpRecvError',31),('sfpSendError',32),('sfpBothError',33),('fanError',41),('psuError',51),('rpsError',61),('moduleFaulty',71),('sensorError',81),('hardwareFaulty',91)))
_HpnicfEntityExtErrorStatus_Type.__name__=_I
_HpnicfEntityExtErrorStatus_Object=MibTableColumn
hpnicfEntityExtErrorStatus=_HpnicfEntityExtErrorStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,19),_HpnicfEntityExtErrorStatus_Type())
hpnicfEntityExtErrorStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtErrorStatus.setStatus(_B)
class _HpnicfEntityExtCpuMaxUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfEntityExtCpuMaxUsage_Type.__name__=_I
_HpnicfEntityExtCpuMaxUsage_Object=MibTableColumn
hpnicfEntityExtCpuMaxUsage=_HpnicfEntityExtCpuMaxUsage_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,20),_HpnicfEntityExtCpuMaxUsage_Type())
hpnicfEntityExtCpuMaxUsage.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtCpuMaxUsage.setStatus(_B)
_HpnicfEntityExtLowerTemperatureThreshold_Type=Integer32
_HpnicfEntityExtLowerTemperatureThreshold_Object=MibTableColumn
hpnicfEntityExtLowerTemperatureThreshold=_HpnicfEntityExtLowerTemperatureThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,21),_HpnicfEntityExtLowerTemperatureThreshold_Type())
hpnicfEntityExtLowerTemperatureThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfEntityExtLowerTemperatureThreshold.setStatus(_B)
_HpnicfEntityExtShutdownTemperatureThreshold_Type=Integer32
_HpnicfEntityExtShutdownTemperatureThreshold_Object=MibTableColumn
hpnicfEntityExtShutdownTemperatureThreshold=_HpnicfEntityExtShutdownTemperatureThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,22),_HpnicfEntityExtShutdownTemperatureThreshold_Type())
hpnicfEntityExtShutdownTemperatureThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfEntityExtShutdownTemperatureThreshold.setStatus(_B)
_HpnicfEntityExtPhyMemSize_Type=Unsigned32
_HpnicfEntityExtPhyMemSize_Object=MibTableColumn
hpnicfEntityExtPhyMemSize=_HpnicfEntityExtPhyMemSize_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,23),_HpnicfEntityExtPhyMemSize_Type())
hpnicfEntityExtPhyMemSize.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtPhyMemSize.setStatus(_B)
_HpnicfEntityExtPhyCpuFrequency_Type=Integer32
_HpnicfEntityExtPhyCpuFrequency_Object=MibTableColumn
hpnicfEntityExtPhyCpuFrequency=_HpnicfEntityExtPhyCpuFrequency_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,24),_HpnicfEntityExtPhyCpuFrequency_Type())
hpnicfEntityExtPhyCpuFrequency.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtPhyCpuFrequency.setStatus(_B)
class _HpnicfEntityExtFirstUsedDate_Type(DateAndTime):subtypeSpec=DateAndTime.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_HpnicfEntityExtFirstUsedDate_Type.__name__=_r
_HpnicfEntityExtFirstUsedDate_Object=MibTableColumn
hpnicfEntityExtFirstUsedDate=_HpnicfEntityExtFirstUsedDate_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,25),_HpnicfEntityExtFirstUsedDate_Type())
hpnicfEntityExtFirstUsedDate.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtFirstUsedDate.setStatus(_B)
class _HpnicfEntityExtCpuAvgUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfEntityExtCpuAvgUsage_Type.__name__=_I
_HpnicfEntityExtCpuAvgUsage_Object=MibTableColumn
hpnicfEntityExtCpuAvgUsage=_HpnicfEntityExtCpuAvgUsage_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,26),_HpnicfEntityExtCpuAvgUsage_Type())
hpnicfEntityExtCpuAvgUsage.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtCpuAvgUsage.setStatus(_B)
class _HpnicfEntityExtMemAvgUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfEntityExtMemAvgUsage_Type.__name__=_I
_HpnicfEntityExtMemAvgUsage_Object=MibTableColumn
hpnicfEntityExtMemAvgUsage=_HpnicfEntityExtMemAvgUsage_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,27),_HpnicfEntityExtMemAvgUsage_Type())
hpnicfEntityExtMemAvgUsage.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtMemAvgUsage.setStatus(_B)
class _HpnicfEntityExtMemType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfEntityExtMemType_Type.__name__=_o
_HpnicfEntityExtMemType_Object=MibTableColumn
hpnicfEntityExtMemType=_HpnicfEntityExtMemType_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,28),_HpnicfEntityExtMemType_Type())
hpnicfEntityExtMemType.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtMemType.setStatus(_B)
_HpnicfEntityExtCriticalLowerTemperatureThreshold_Type=Integer32
_HpnicfEntityExtCriticalLowerTemperatureThreshold_Object=MibTableColumn
hpnicfEntityExtCriticalLowerTemperatureThreshold=_HpnicfEntityExtCriticalLowerTemperatureThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,29),_HpnicfEntityExtCriticalLowerTemperatureThreshold_Type())
hpnicfEntityExtCriticalLowerTemperatureThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfEntityExtCriticalLowerTemperatureThreshold.setStatus(_B)
_HpnicfEntityExtShutdownLowerTemperatureThreshold_Type=Integer32
_HpnicfEntityExtShutdownLowerTemperatureThreshold_Object=MibTableColumn
hpnicfEntityExtShutdownLowerTemperatureThreshold=_HpnicfEntityExtShutdownLowerTemperatureThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,30),_HpnicfEntityExtShutdownLowerTemperatureThreshold_Type())
hpnicfEntityExtShutdownLowerTemperatureThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfEntityExtShutdownLowerTemperatureThreshold.setStatus(_B)
class _HpnicfEntityExtCpuUsageRecoverThreshold_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfEntityExtCpuUsageRecoverThreshold_Type.__name__=_I
_HpnicfEntityExtCpuUsageRecoverThreshold_Object=MibTableColumn
hpnicfEntityExtCpuUsageRecoverThreshold=_HpnicfEntityExtCpuUsageRecoverThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,31),_HpnicfEntityExtCpuUsageRecoverThreshold_Type())
hpnicfEntityExtCpuUsageRecoverThreshold.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfEntityExtCpuUsageRecoverThreshold.setStatus(_B)
_HpnicfEntityExtMemSizeRev_Type=CounterBasedGauge64
_HpnicfEntityExtMemSizeRev_Object=MibTableColumn
hpnicfEntityExtMemSizeRev=_HpnicfEntityExtMemSizeRev_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,32),_HpnicfEntityExtMemSizeRev_Type())
hpnicfEntityExtMemSizeRev.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtMemSizeRev.setStatus(_B)
if mibBuilder.loadTexts:hpnicfEntityExtMemSizeRev.setUnits('bytes')
class _HpnicfEntityExtCpuUsageIn1Minute_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfEntityExtCpuUsageIn1Minute_Type.__name__=_I
_HpnicfEntityExtCpuUsageIn1Minute_Object=MibTableColumn
hpnicfEntityExtCpuUsageIn1Minute=_HpnicfEntityExtCpuUsageIn1Minute_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,33),_HpnicfEntityExtCpuUsageIn1Minute_Type())
hpnicfEntityExtCpuUsageIn1Minute.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtCpuUsageIn1Minute.setStatus(_B)
class _HpnicfEntityExtCpuUsageIn5Minutes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfEntityExtCpuUsageIn5Minutes_Type.__name__=_I
_HpnicfEntityExtCpuUsageIn5Minutes_Object=MibTableColumn
hpnicfEntityExtCpuUsageIn5Minutes=_HpnicfEntityExtCpuUsageIn5Minutes_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,1,1,1,34),_HpnicfEntityExtCpuUsageIn5Minutes_Type())
hpnicfEntityExtCpuUsageIn5Minutes.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtCpuUsageIn5Minutes.setStatus(_B)
_HpnicfEntityExtManu_ObjectIdentity=ObjectIdentity
hpnicfEntityExtManu=_HpnicfEntityExtManu_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,6,1,2))
_HpnicfEntityExtManuTable_Object=MibTable
hpnicfEntityExtManuTable=_HpnicfEntityExtManuTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,2,1))
if mibBuilder.loadTexts:hpnicfEntityExtManuTable.setStatus(_B)
_HpnicfEntityExtManuEntry_Object=MibTableRow
hpnicfEntityExtManuEntry=_HpnicfEntityExtManuEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,2,1,1))
hpnicfEntityExtManuEntry.setIndexNames((0,_A,_d))
if mibBuilder.loadTexts:hpnicfEntityExtManuEntry.setStatus(_B)
class _HpnicfEntityExtManuPhysicalIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfEntityExtManuPhysicalIndex_Type.__name__=_I
_HpnicfEntityExtManuPhysicalIndex_Object=MibTableColumn
hpnicfEntityExtManuPhysicalIndex=_HpnicfEntityExtManuPhysicalIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,2,1,1,1),_HpnicfEntityExtManuPhysicalIndex_Type())
hpnicfEntityExtManuPhysicalIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:hpnicfEntityExtManuPhysicalIndex.setStatus(_B)
_HpnicfEntityExtManuSerialNum_Type=SnmpAdminString
_HpnicfEntityExtManuSerialNum_Object=MibTableColumn
hpnicfEntityExtManuSerialNum=_HpnicfEntityExtManuSerialNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,2,1,1,2),_HpnicfEntityExtManuSerialNum_Type())
hpnicfEntityExtManuSerialNum.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtManuSerialNum.setStatus(_B)
_HpnicfEntityExtManuBuildInfo_Type=SnmpAdminString
_HpnicfEntityExtManuBuildInfo_Object=MibTableColumn
hpnicfEntityExtManuBuildInfo=_HpnicfEntityExtManuBuildInfo_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,2,1,1,3),_HpnicfEntityExtManuBuildInfo_Type())
hpnicfEntityExtManuBuildInfo.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtManuBuildInfo.setStatus(_B)
_HpnicfEntityExtManuBOM_Type=SnmpAdminString
_HpnicfEntityExtManuBOM_Object=MibTableColumn
hpnicfEntityExtManuBOM=_HpnicfEntityExtManuBOM_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,2,1,1,4),_HpnicfEntityExtManuBOM_Type())
hpnicfEntityExtManuBOM.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtManuBOM.setStatus(_B)
_HpnicfEntityExtMacAddressCount_Type=Unsigned32
_HpnicfEntityExtMacAddressCount_Object=MibTableColumn
hpnicfEntityExtMacAddressCount=_HpnicfEntityExtMacAddressCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,2,1,1,5),_HpnicfEntityExtMacAddressCount_Type())
hpnicfEntityExtMacAddressCount.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtMacAddressCount.setStatus(_B)
_HpnicfEntityExtPower_ObjectIdentity=ObjectIdentity
hpnicfEntityExtPower=_HpnicfEntityExtPower_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,6,1,3))
_HpnicfEntityExtPowerTable_Object=MibTable
hpnicfEntityExtPowerTable=_HpnicfEntityExtPowerTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,3,1))
if mibBuilder.loadTexts:hpnicfEntityExtPowerTable.setStatus(_B)
_HpnicfEntityExtPowerEntry_Object=MibTableRow
hpnicfEntityExtPowerEntry=_HpnicfEntityExtPowerEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,3,1,1))
hpnicfEntityExtPowerEntry.setIndexNames((0,_A,_e))
if mibBuilder.loadTexts:hpnicfEntityExtPowerEntry.setStatus(_B)
class _HpnicfEntityExtPowerPhysicalIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfEntityExtPowerPhysicalIndex_Type.__name__=_I
_HpnicfEntityExtPowerPhysicalIndex_Object=MibTableColumn
hpnicfEntityExtPowerPhysicalIndex=_HpnicfEntityExtPowerPhysicalIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,3,1,1,1),_HpnicfEntityExtPowerPhysicalIndex_Type())
hpnicfEntityExtPowerPhysicalIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:hpnicfEntityExtPowerPhysicalIndex.setStatus(_B)
_HpnicfEntityExtNominalPower_Type=Gauge32
_HpnicfEntityExtNominalPower_Object=MibTableColumn
hpnicfEntityExtNominalPower=_HpnicfEntityExtNominalPower_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,3,1,1,2),_HpnicfEntityExtNominalPower_Type())
hpnicfEntityExtNominalPower.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtNominalPower.setStatus(_B)
_HpnicfEntityExtCurrentPower_Type=Gauge32
_HpnicfEntityExtCurrentPower_Object=MibTableColumn
hpnicfEntityExtCurrentPower=_HpnicfEntityExtCurrentPower_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,3,1,1,3),_HpnicfEntityExtCurrentPower_Type())
hpnicfEntityExtCurrentPower.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtCurrentPower.setStatus(_B)
_HpnicfEntityExtAveragePower_Type=Integer32
_HpnicfEntityExtAveragePower_Object=MibTableColumn
hpnicfEntityExtAveragePower=_HpnicfEntityExtAveragePower_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,3,1,1,4),_HpnicfEntityExtAveragePower_Type())
hpnicfEntityExtAveragePower.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfEntityExtAveragePower.setStatus(_B)
_HpnicfEntityExtPeakPower_Type=Integer32
_HpnicfEntityExtPeakPower_Object=MibTableColumn
hpnicfEntityExtPeakPower=_HpnicfEntityExtPeakPower_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,3,1,1,5),_HpnicfEntityExtPeakPower_Type())
hpnicfEntityExtPeakPower.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfEntityExtPeakPower.setStatus(_B)
_HpnicfProcessObjects_ObjectIdentity=ObjectIdentity
hpnicfProcessObjects=_HpnicfProcessObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,6,1,4))
_HpnicfProcessTable_Object=MibTable
hpnicfProcessTable=_HpnicfProcessTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,4,1))
if mibBuilder.loadTexts:hpnicfProcessTable.setStatus(_B)
_HpnicfProcessEntry_Object=MibTableRow
hpnicfProcessEntry=_HpnicfProcessEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,4,1,1))
hpnicfProcessEntry.setIndexNames((0,_A,_u))
if mibBuilder.loadTexts:hpnicfProcessEntry.setStatus(_B)
_HpnicfProcessID_Type=Unsigned32
_HpnicfProcessID_Object=MibTableColumn
hpnicfProcessID=_HpnicfProcessID_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,4,1,1,1),_HpnicfProcessID_Type())
hpnicfProcessID.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfProcessID.setStatus(_B)
class _HpnicfProcessName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfProcessName_Type.__name__=_s
_HpnicfProcessName_Object=MibTableColumn
hpnicfProcessName=_HpnicfProcessName_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,4,1,1,2),_HpnicfProcessName_Type())
hpnicfProcessName.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfProcessName.setStatus(_B)
class _HpnicfProcessUtil5Min_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfProcessUtil5Min_Type.__name__=_q
_HpnicfProcessUtil5Min_Object=MibTableColumn
hpnicfProcessUtil5Min=_HpnicfProcessUtil5Min_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,4,1,1,3),_HpnicfProcessUtil5Min_Type())
hpnicfProcessUtil5Min.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfProcessUtil5Min.setStatus(_B)
_HpnicfEntityExtVoltageObjects_ObjectIdentity=ObjectIdentity
hpnicfEntityExtVoltageObjects=_HpnicfEntityExtVoltageObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,6,1,5))
_HpnicfEntityExtVoltageTable_Object=MibTable
hpnicfEntityExtVoltageTable=_HpnicfEntityExtVoltageTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,5,1))
if mibBuilder.loadTexts:hpnicfEntityExtVoltageTable.setStatus(_B)
_HpnicfEntityExtVoltageEntry_Object=MibTableRow
hpnicfEntityExtVoltageEntry=_HpnicfEntityExtVoltageEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,5,1,1))
hpnicfEntityExtVoltageEntry.setIndexNames((0,_A,_C))
if mibBuilder.loadTexts:hpnicfEntityExtVoltageEntry.setStatus(_B)
_HpnicfEntityExtCurrentVoltage_Type=Integer32
_HpnicfEntityExtCurrentVoltage_Object=MibTableColumn
hpnicfEntityExtCurrentVoltage=_HpnicfEntityExtCurrentVoltage_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,5,1,1,1),_HpnicfEntityExtCurrentVoltage_Type())
hpnicfEntityExtCurrentVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtCurrentVoltage.setStatus(_B)
_HpnicfEntityExtNominalVoltage_Type=Integer32
_HpnicfEntityExtNominalVoltage_Object=MibTableColumn
hpnicfEntityExtNominalVoltage=_HpnicfEntityExtNominalVoltage_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,5,1,1,2),_HpnicfEntityExtNominalVoltage_Type())
hpnicfEntityExtNominalVoltage.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtNominalVoltage.setStatus(_B)
class _HpnicfEntityExtVoltageState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_t,0),('low',1),('tooLow',2),('high',3),('tooHigh',4)))
_HpnicfEntityExtVoltageState_Type.__name__=_I
_HpnicfEntityExtVoltageState_Object=MibTableColumn
hpnicfEntityExtVoltageState=_HpnicfEntityExtVoltageState_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,5,1,1,3),_HpnicfEntityExtVoltageState_Type())
hpnicfEntityExtVoltageState.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtVoltageState.setStatus(_B)
_HpnicfEntityExtVoltageMajorLowThreshold_Type=Integer32
_HpnicfEntityExtVoltageMajorLowThreshold_Object=MibTableColumn
hpnicfEntityExtVoltageMajorLowThreshold=_HpnicfEntityExtVoltageMajorLowThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,5,1,1,4),_HpnicfEntityExtVoltageMajorLowThreshold_Type())
hpnicfEntityExtVoltageMajorLowThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtVoltageMajorLowThreshold.setStatus(_B)
_HpnicfEntityExtVoltageFatalLowThreshold_Type=Integer32
_HpnicfEntityExtVoltageFatalLowThreshold_Object=MibTableColumn
hpnicfEntityExtVoltageFatalLowThreshold=_HpnicfEntityExtVoltageFatalLowThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,5,1,1,5),_HpnicfEntityExtVoltageFatalLowThreshold_Type())
hpnicfEntityExtVoltageFatalLowThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtVoltageFatalLowThreshold.setStatus(_B)
_HpnicfEntityExtVoltageMajorHighThreshold_Type=Integer32
_HpnicfEntityExtVoltageMajorHighThreshold_Object=MibTableColumn
hpnicfEntityExtVoltageMajorHighThreshold=_HpnicfEntityExtVoltageMajorHighThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,5,1,1,6),_HpnicfEntityExtVoltageMajorHighThreshold_Type())
hpnicfEntityExtVoltageMajorHighThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtVoltageMajorHighThreshold.setStatus(_B)
_HpnicfEntityExtVoltageFatalHighThreshold_Type=Integer32
_HpnicfEntityExtVoltageFatalHighThreshold_Object=MibTableColumn
hpnicfEntityExtVoltageFatalHighThreshold=_HpnicfEntityExtVoltageFatalHighThreshold_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,1,5,1,1,7),_HpnicfEntityExtVoltageFatalHighThreshold_Type())
hpnicfEntityExtVoltageFatalHighThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:hpnicfEntityExtVoltageFatalHighThreshold.setStatus(_B)
_HpnicfEntityExtTraps_ObjectIdentity=ObjectIdentity
hpnicfEntityExtTraps=_HpnicfEntityExtTraps_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,6,2))
_HpnicfEntityExtTrapsPrefix_ObjectIdentity=ObjectIdentity
hpnicfEntityExtTrapsPrefix=_HpnicfEntityExtTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0))
_HpnicfEntityExtTrapsInfor_ObjectIdentity=ObjectIdentity
hpnicfEntityExtTrapsInfor=_HpnicfEntityExtTrapsInfor_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,6,2,1))
class _HpnicfEntityExtTrapDescription_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfEntityExtTrapDescription_Type.__name__=_p
_HpnicfEntityExtTrapDescription_Object=MibScalar
hpnicfEntityExtTrapDescription=_HpnicfEntityExtTrapDescription_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,2,1,1),_HpnicfEntityExtTrapDescription_Type())
hpnicfEntityExtTrapDescription.setMaxAccess(_L)
if mibBuilder.loadTexts:hpnicfEntityExtTrapDescription.setStatus(_B)
class _HpnicfEntityExtECCParityAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('other',1),('l1cache',2),('l2cache',3),('sdram',4),('mac',5),('tcam',6),('ingressbuffer',7),('egressbuffer',8),('lpm',9),('controlmemory',10)))
_HpnicfEntityExtECCParityAlarmStatus_Type.__name__=_I
_HpnicfEntityExtECCParityAlarmStatus_Object=MibScalar
hpnicfEntityExtECCParityAlarmStatus=_HpnicfEntityExtECCParityAlarmStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,2,1,2),_HpnicfEntityExtECCParityAlarmStatus_Type())
hpnicfEntityExtECCParityAlarmStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:hpnicfEntityExtECCParityAlarmStatus.setStatus(_B)
_HpnicfEntityExtSFPInvalidInDays_Type=Integer32
_HpnicfEntityExtSFPInvalidInDays_Object=MibScalar
hpnicfEntityExtSFPInvalidInDays=_HpnicfEntityExtSFPInvalidInDays_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,2,1,3),_HpnicfEntityExtSFPInvalidInDays_Type())
hpnicfEntityExtSFPInvalidInDays.setMaxAccess(_L)
if mibBuilder.loadTexts:hpnicfEntityExtSFPInvalidInDays.setStatus(_B)
_HpnicfEntityExtFirstTrapTime_Type=TimeTicks
_HpnicfEntityExtFirstTrapTime_Object=MibScalar
hpnicfEntityExtFirstTrapTime=_HpnicfEntityExtFirstTrapTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,6,2,1,4),_HpnicfEntityExtFirstTrapTime_Type())
hpnicfEntityExtFirstTrapTime.setMaxAccess(_L)
if mibBuilder.loadTexts:hpnicfEntityExtFirstTrapTime.setStatus(_B)
_HpnicfEntityExtConformance_ObjectIdentity=ObjectIdentity
hpnicfEntityExtConformance=_HpnicfEntityExtConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,6,3))
_HpnicfEntityExtCompliances_ObjectIdentity=ObjectIdentity
hpnicfEntityExtCompliances=_HpnicfEntityExtCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,6,3,1))
_HpnicfEntityExtGroups_ObjectIdentity=ObjectIdentity
hpnicfEntityExtGroups=_HpnicfEntityExtGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,6,3,2))
hpnicfEntityExtGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,6,3,2,1))
hpnicfEntityExtGroup.setObjects(*((_A,_C),(_A,_E),(_A,_T),(_A,_v),(_A,_G),(_A,_U),(_A,_V),(_A,_M),(_A,_N),(_A,_W),(_A,_w),(_A,_K),(_A,_X),(_A,_Y),(_A,_f),(_A,_g),(_A,_h),(_A,_x),(_A,_O),(_A,_y),(_A,_Z),(_A,_i),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_j),(_A,_k),(_A,_a),(_A,_b),(_A,_A5),(_A,_A6)))
if mibBuilder.loadTexts:hpnicfEntityExtGroup.setStatus(_B)
hpnicfEntityExtManuGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,6,3,2,3))
hpnicfEntityExtManuGroup.setObjects(*((_A,_d),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:hpnicfEntityExtManuGroup.setStatus(_B)
hpnicfEntityExtPowerGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,2,6,3,2,4))
hpnicfEntityExtPowerGroup.setObjects(*((_A,_e),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE)))
if mibBuilder.loadTexts:hpnicfEntityExtPowerGroup.setStatus(_B)
hpnicfEntityExtTemperatureThresholdNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,1))
hpnicfEntityExtTemperatureThresholdNotification.setObjects(*((_A,_C),(_A,_K),(_A,_X),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:hpnicfEntityExtTemperatureThresholdNotification.setStatus(_B)
hpnicfEntityExtVoltageLowThresholdNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,2))
hpnicfEntityExtVoltageLowThresholdNotification.setObjects(*((_A,_C),(_A,_Y),(_A,_f),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:hpnicfEntityExtVoltageLowThresholdNotification.setStatus(_B)
hpnicfEntityExtVoltageHighThresholdNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,3))
hpnicfEntityExtVoltageHighThresholdNotification.setObjects(*((_A,_C),(_A,_Y),(_A,_g),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:hpnicfEntityExtVoltageHighThresholdNotification.setStatus(_B)
hpnicfEntityExtCpuUsageThresholdNotfication=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,4))
hpnicfEntityExtCpuUsageThresholdNotfication.setObjects(*((_A,_C),(_A,_U),(_A,_V),(_A,_E),(_A,_G),(_A,_a),(_A,_S)))
if mibBuilder.loadTexts:hpnicfEntityExtCpuUsageThresholdNotfication.setStatus(_B)
hpnicfEntityExtMemUsageThresholdNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,5))
hpnicfEntityExtMemUsageThresholdNotification.setObjects(*((_A,_C),(_A,_M),(_A,_N),(_A,_W),(_A,_E),(_A,_G),(_A,_S)))
if mibBuilder.loadTexts:hpnicfEntityExtMemUsageThresholdNotification.setStatus(_B)
hpnicfEntityExtOperEnabled=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,6))
hpnicfEntityExtOperEnabled.setObjects(*((_A,_C),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:hpnicfEntityExtOperEnabled.setStatus(_B)
hpnicfEntityExtOperDisabled=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,7))
hpnicfEntityExtOperDisabled.setObjects(*((_A,_C),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:hpnicfEntityExtOperDisabled.setStatus(_B)
hpnicfEntityExtCriticalTemperatureThresholdNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,8))
hpnicfEntityExtCriticalTemperatureThresholdNotification.setObjects(*((_A,_C),(_A,_K),(_A,_h),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:hpnicfEntityExtCriticalTemperatureThresholdNotification.setStatus(_B)
hpnicfEntityExtSFPAlarmOn=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,9))
hpnicfEntityExtSFPAlarmOn.setObjects(*((_A,_C),(_A,_O),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:hpnicfEntityExtSFPAlarmOn.setStatus(_B)
hpnicfEntityExtSFPAlarmOff=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,10))
hpnicfEntityExtSFPAlarmOff.setObjects(*((_A,_C),(_A,_O),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:hpnicfEntityExtSFPAlarmOff.setStatus(_B)
hpnicfEntityExtSFPPhony=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,11))
hpnicfEntityExtSFPPhony.setObjects(*((_A,_C),(_F,_H),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:hpnicfEntityExtSFPPhony.setStatus(_B)
hpnicfEntityInsert=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,12))
hpnicfEntityInsert.setObjects(*((_F,_c),(_A,_E),(_A,_T)))
if mibBuilder.loadTexts:hpnicfEntityInsert.setStatus(_B)
hpnicfEntityRemove=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,13))
hpnicfEntityRemove.setObjects(*((_F,_c),(_A,_E),(_A,_T)))
if mibBuilder.loadTexts:hpnicfEntityRemove.setStatus(_B)
hpnicfEntityExtForcedPowerOff=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,14))
hpnicfEntityExtForcedPowerOff.setObjects(*((_A,_C),(_F,_H),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:hpnicfEntityExtForcedPowerOff.setStatus(_B)
hpnicfEntityExtForcedPowerOn=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,15))
hpnicfEntityExtForcedPowerOn.setObjects(*((_A,_C),(_F,_H),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:hpnicfEntityExtForcedPowerOn.setStatus(_B)
hpnicfEntityExtFaultAlarmOn=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,16))
hpnicfEntityExtFaultAlarmOn.setObjects(*((_A,_C),(_F,_H),(_A,_O),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:hpnicfEntityExtFaultAlarmOn.setStatus(_B)
hpnicfEntityExtFaultAlarmOff=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,17))
hpnicfEntityExtFaultAlarmOff.setObjects(*((_A,_C),(_F,_H),(_A,_O),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:hpnicfEntityExtFaultAlarmOff.setStatus(_B)
hpnicfEntityExtResourceLack=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,18))
hpnicfEntityExtResourceLack.setObjects(*((_A,_C),(_F,_H)))
if mibBuilder.loadTexts:hpnicfEntityExtResourceLack.setStatus(_B)
hpnicfEntityExtResourceEnough=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,19))
hpnicfEntityExtResourceEnough.setObjects(*((_A,_C),(_F,_H)))
if mibBuilder.loadTexts:hpnicfEntityExtResourceEnough.setStatus(_B)
hpnicfEntityExtTemperatureLower=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,20))
hpnicfEntityExtTemperatureLower.setObjects(*((_A,_C),(_F,_H),(_A,_K),(_A,_Z),(_A,_E)))
if mibBuilder.loadTexts:hpnicfEntityExtTemperatureLower.setStatus(_B)
hpnicfEntityExtTemperatureTooUp=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,21))
hpnicfEntityExtTemperatureTooUp.setObjects(*((_A,_C),(_F,_H),(_A,_K),(_A,_i),(_A,_E)))
if mibBuilder.loadTexts:hpnicfEntityExtTemperatureTooUp.setStatus(_B)
hpnicfEntityExtTemperatureNormal=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,22))
hpnicfEntityExtTemperatureNormal.setObjects(*((_A,_C),(_F,_H),(_A,_K),(_A,_Z),(_A,_X),(_A,_E)))
if mibBuilder.loadTexts:hpnicfEntityExtTemperatureNormal.setStatus(_B)
hpnicfEntityExternalAlarmOccur=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,23))
hpnicfEntityExternalAlarmOccur.setObjects(*((_A,_C),(_F,_H)))
if mibBuilder.loadTexts:hpnicfEntityExternalAlarmOccur.setStatus(_B)
hpnicfEntityExternalAlarmRecover=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,24))
hpnicfEntityExternalAlarmRecover.setObjects(*((_A,_C),(_F,_H)))
if mibBuilder.loadTexts:hpnicfEntityExternalAlarmRecover.setStatus(_B)
hpnicfEntityExtCpuUsageThresholdRecover=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,25))
hpnicfEntityExtCpuUsageThresholdRecover.setObjects(*((_A,_C),(_A,_U),(_A,_V),(_A,_E),(_A,_G),(_A,_a),(_A,_S)))
if mibBuilder.loadTexts:hpnicfEntityExtCpuUsageThresholdRecover.setStatus(_B)
hpnicfEntityExtMemUsageThresholdRecover=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,26))
hpnicfEntityExtMemUsageThresholdRecover.setObjects(*((_A,_C),(_A,_M),(_A,_N),(_A,_W),(_A,_E),(_A,_G),(_A,_S)))
if mibBuilder.loadTexts:hpnicfEntityExtMemUsageThresholdRecover.setStatus(_B)
hpnicfEntityExtMemAllocatedFailed=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,27))
hpnicfEntityExtMemAllocatedFailed.setObjects(*((_A,_C),(_A,_l)))
if mibBuilder.loadTexts:hpnicfEntityExtMemAllocatedFailed.setStatus(_B)
hpnicfEntityExtECCParityAlarm=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,28))
hpnicfEntityExtECCParityAlarm.setObjects(*((_A,_C),(_A,_AF),(_A,_l)))
if mibBuilder.loadTexts:hpnicfEntityExtECCParityAlarm.setStatus(_B)
hpnicfEntityExtCritLowerTempThresholdNotification=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,29))
hpnicfEntityExtCritLowerTempThresholdNotification.setObjects(*((_A,_C),(_F,_H),(_A,_K),(_A,_j)))
if mibBuilder.loadTexts:hpnicfEntityExtCritLowerTempThresholdNotification.setStatus(_B)
hpnicfEntityExtTemperatureTooLow=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,30))
hpnicfEntityExtTemperatureTooLow.setObjects(*((_A,_C),(_F,_H),(_A,_K),(_A,_k)))
if mibBuilder.loadTexts:hpnicfEntityExtTemperatureTooLow.setStatus(_B)
hpnicfEntityExtFanDirectionNotPreferred=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,31))
hpnicfEntityExtFanDirectionNotPreferred.setObjects(*((_A,_C),(_F,_H)))
if mibBuilder.loadTexts:hpnicfEntityExtFanDirectionNotPreferred.setStatus(_B)
hpnicfEntityExtFanDirectionNotAccord=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,32))
hpnicfEntityExtFanDirectionNotAccord.setObjects(*((_A,_C),(_F,_H)))
if mibBuilder.loadTexts:hpnicfEntityExtFanDirectionNotAccord.setStatus(_B)
hpnicfEntityExtSFPInvalid=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,33))
hpnicfEntityExtSFPInvalid.setObjects(*((_A,_C),(_F,_H),(_A,_AG)))
if mibBuilder.loadTexts:hpnicfEntityExtSFPInvalid.setStatus(_B)
hpnicfEntityExtSFPInvalidNow=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,34))
hpnicfEntityExtSFPInvalidNow.setObjects(*((_A,_C),(_F,_H)))
if mibBuilder.loadTexts:hpnicfEntityExtSFPInvalidNow.setStatus(_B)
hpnicfEntityExtMemUsageThresholdOverTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,35))
hpnicfEntityExtMemUsageThresholdOverTrap.setObjects(*((_A,_C),(_A,_M),(_A,_N),(_A,_b),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:hpnicfEntityExtMemUsageThresholdOverTrap.setStatus(_B)
hpnicfEntityExtMemUsageThresholdRecoverTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,36))
hpnicfEntityExtMemUsageThresholdRecoverTrap.setObjects(*((_A,_C),(_A,_M),(_A,_N),(_A,_b),(_A,_E),(_A,_G)))
if mibBuilder.loadTexts:hpnicfEntityExtMemUsageThresholdRecoverTrap.setStatus(_B)
hpnicfEntityExtVoltageNormal=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,37))
hpnicfEntityExtVoltageNormal.setObjects(*((_A,_C),(_A,_P),(_A,_Q),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:hpnicfEntityExtVoltageNormal.setStatus(_B)
hpnicfEntityExtVoltageLower=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,38))
hpnicfEntityExtVoltageLower.setObjects(*((_A,_C),(_A,_P),(_A,_Q),(_A,_m)))
if mibBuilder.loadTexts:hpnicfEntityExtVoltageLower.setStatus(_B)
hpnicfEntityExtVoltageTooLow=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,39))
hpnicfEntityExtVoltageTooLow.setObjects(*((_A,_C),(_A,_P),(_A,_Q),(_A,_AH)))
if mibBuilder.loadTexts:hpnicfEntityExtVoltageTooLow.setStatus(_B)
hpnicfEntityExtVoltageHigher=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,40))
hpnicfEntityExtVoltageHigher.setObjects(*((_A,_C),(_A,_P),(_A,_Q),(_A,_n)))
if mibBuilder.loadTexts:hpnicfEntityExtVoltageHigher.setStatus(_B)
hpnicfEntityExtVoltageTooHigh=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,6,2,0,41))
hpnicfEntityExtVoltageTooHigh.setObjects(*((_A,_C),(_A,_P),(_A,_Q),(_A,_AI)))
if mibBuilder.loadTexts:hpnicfEntityExtVoltageTooHigh.setStatus(_B)
hpnicfEntityExtNotificationGroup=NotificationGroup((1,3,6,1,4,1,11,2,14,11,15,2,6,3,2,2))
hpnicfEntityExtNotificationGroup.setObjects(*((_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao),(_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au),(_A,_Av),(_A,_Aw),(_A,_Ax)))
if mibBuilder.loadTexts:hpnicfEntityExtNotificationGroup.setStatus(_B)
hpnicfEntityExtCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,2,6,3,1,1))
hpnicfEntityExtCompliance.setObjects(*((_A,_Ay),(_A,_Az),(_A,_A_),(_A,_B0)))
if mibBuilder.loadTexts:hpnicfEntityExtCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'HpnicfAdminState':HpnicfAdminState,'HpnicfOperState':HpnicfOperState,'HpnicfAlarmStatus':HpnicfAlarmStatus,'HpnicfStandbyStatus':HpnicfStandbyStatus,'hpnicfEntityExtend':hpnicfEntityExtend,'hpnicfEntityExtObjects':hpnicfEntityExtObjects,'hpnicfEntityExtState':hpnicfEntityExtState,'hpnicfEntityExtStateTable':hpnicfEntityExtStateTable,'hpnicfEntityExtStateEntry':hpnicfEntityExtStateEntry,_C:hpnicfEntityExtPhysicalIndex,_E:hpnicfEntityExtAdminStatus,_T:hpnicfEntityExtOperStatus,_v:hpnicfEntityExtStandbyStatus,_G:hpnicfEntityExtAlarmLight,_U:hpnicfEntityExtCpuUsage,_V:hpnicfEntityExtCpuUsageThreshold,_M:hpnicfEntityExtMemUsage,_N:hpnicfEntityExtMemUsageThreshold,_W:hpnicfEntityExtMemSize,_w:hpnicfEntityExtUpTime,_K:hpnicfEntityExtTemperature,_X:hpnicfEntityExtTemperatureThreshold,_Y:hpnicfEntityExtVoltage,_f:hpnicfEntityExtVoltageLowThreshold,_g:hpnicfEntityExtVoltageHighThreshold,_h:hpnicfEntityExtCriticalTemperatureThreshold,_x:hpnicfEntityExtMacAddress,_O:hpnicfEntityExtErrorStatus,_y:hpnicfEntityExtCpuMaxUsage,_Z:hpnicfEntityExtLowerTemperatureThreshold,_i:hpnicfEntityExtShutdownTemperatureThreshold,_z:hpnicfEntityExtPhyMemSize,_A0:hpnicfEntityExtPhyCpuFrequency,_A1:hpnicfEntityExtFirstUsedDate,_A2:hpnicfEntityExtCpuAvgUsage,_A3:hpnicfEntityExtMemAvgUsage,_A4:hpnicfEntityExtMemType,_j:hpnicfEntityExtCriticalLowerTemperatureThreshold,_k:hpnicfEntityExtShutdownLowerTemperatureThreshold,_a:hpnicfEntityExtCpuUsageRecoverThreshold,_b:hpnicfEntityExtMemSizeRev,_A5:hpnicfEntityExtCpuUsageIn1Minute,_A6:hpnicfEntityExtCpuUsageIn5Minutes,'hpnicfEntityExtManu':hpnicfEntityExtManu,'hpnicfEntityExtManuTable':hpnicfEntityExtManuTable,'hpnicfEntityExtManuEntry':hpnicfEntityExtManuEntry,_d:hpnicfEntityExtManuPhysicalIndex,_A7:hpnicfEntityExtManuSerialNum,_A8:hpnicfEntityExtManuBuildInfo,_A9:hpnicfEntityExtManuBOM,_AA:hpnicfEntityExtMacAddressCount,'hpnicfEntityExtPower':hpnicfEntityExtPower,'hpnicfEntityExtPowerTable':hpnicfEntityExtPowerTable,'hpnicfEntityExtPowerEntry':hpnicfEntityExtPowerEntry,_e:hpnicfEntityExtPowerPhysicalIndex,_AB:hpnicfEntityExtNominalPower,_AC:hpnicfEntityExtCurrentPower,_AD:hpnicfEntityExtAveragePower,_AE:hpnicfEntityExtPeakPower,'hpnicfProcessObjects':hpnicfProcessObjects,'hpnicfProcessTable':hpnicfProcessTable,'hpnicfProcessEntry':hpnicfProcessEntry,_u:hpnicfProcessID,'hpnicfProcessName':hpnicfProcessName,'hpnicfProcessUtil5Min':hpnicfProcessUtil5Min,'hpnicfEntityExtVoltageObjects':hpnicfEntityExtVoltageObjects,'hpnicfEntityExtVoltageTable':hpnicfEntityExtVoltageTable,'hpnicfEntityExtVoltageEntry':hpnicfEntityExtVoltageEntry,_P:hpnicfEntityExtCurrentVoltage,_Q:hpnicfEntityExtNominalVoltage,'hpnicfEntityExtVoltageState':hpnicfEntityExtVoltageState,_m:hpnicfEntityExtVoltageMajorLowThreshold,_AH:hpnicfEntityExtVoltageFatalLowThreshold,_n:hpnicfEntityExtVoltageMajorHighThreshold,_AI:hpnicfEntityExtVoltageFatalHighThreshold,'hpnicfEntityExtTraps':hpnicfEntityExtTraps,'hpnicfEntityExtTrapsPrefix':hpnicfEntityExtTrapsPrefix,_AJ:hpnicfEntityExtTemperatureThresholdNotification,_AK:hpnicfEntityExtVoltageLowThresholdNotification,_AL:hpnicfEntityExtVoltageHighThresholdNotification,_AM:hpnicfEntityExtCpuUsageThresholdNotfication,_AN:hpnicfEntityExtMemUsageThresholdNotification,_AO:hpnicfEntityExtOperEnabled,_AP:hpnicfEntityExtOperDisabled,_AQ:hpnicfEntityExtCriticalTemperatureThresholdNotification,_AR:hpnicfEntityExtSFPAlarmOn,_AS:hpnicfEntityExtSFPAlarmOff,_AT:hpnicfEntityExtSFPPhony,_AU:hpnicfEntityInsert,_AV:hpnicfEntityRemove,_AW:hpnicfEntityExtForcedPowerOff,_AX:hpnicfEntityExtForcedPowerOn,_AY:hpnicfEntityExtFaultAlarmOn,_AZ:hpnicfEntityExtFaultAlarmOff,_Aa:hpnicfEntityExtResourceLack,_Ab:hpnicfEntityExtResourceEnough,_Ac:hpnicfEntityExtTemperatureLower,_Ad:hpnicfEntityExtTemperatureTooUp,_Ae:hpnicfEntityExtTemperatureNormal,_Af:hpnicfEntityExternalAlarmOccur,_Ag:hpnicfEntityExternalAlarmRecover,_Ah:hpnicfEntityExtCpuUsageThresholdRecover,_Ai:hpnicfEntityExtMemUsageThresholdRecover,_Aj:hpnicfEntityExtMemAllocatedFailed,_Ak:hpnicfEntityExtECCParityAlarm,_Al:hpnicfEntityExtCritLowerTempThresholdNotification,_Am:hpnicfEntityExtTemperatureTooLow,_An:hpnicfEntityExtFanDirectionNotPreferred,_Ao:hpnicfEntityExtFanDirectionNotAccord,_Ap:hpnicfEntityExtSFPInvalid,_Aq:hpnicfEntityExtSFPInvalidNow,_Ar:hpnicfEntityExtMemUsageThresholdOverTrap,_As:hpnicfEntityExtMemUsageThresholdRecoverTrap,_At:hpnicfEntityExtVoltageNormal,_Av:hpnicfEntityExtVoltageLower,_Au:hpnicfEntityExtVoltageTooLow,_Aw:hpnicfEntityExtVoltageHigher,_Ax:hpnicfEntityExtVoltageTooHigh,'hpnicfEntityExtTrapsInfor':hpnicfEntityExtTrapsInfor,_l:hpnicfEntityExtTrapDescription,_AF:hpnicfEntityExtECCParityAlarmStatus,_AG:hpnicfEntityExtSFPInvalidInDays,_S:hpnicfEntityExtFirstTrapTime,'hpnicfEntityExtConformance':hpnicfEntityExtConformance,'hpnicfEntityExtCompliances':hpnicfEntityExtCompliances,'hpnicfEntityExtCompliance':hpnicfEntityExtCompliance,'hpnicfEntityExtGroups':hpnicfEntityExtGroups,_Ay:hpnicfEntityExtGroup,_Az:hpnicfEntityExtNotificationGroup,_A_:hpnicfEntityExtManuGroup,_B0:hpnicfEntityExtPowerGroup})