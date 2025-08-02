_V='hm2PoeMgmtPortPowerLimit'
_U='hm2PoeMgmtPortMaxConsumptionPower'
_T='not-accessible'
_S='hm2PoeMgmtModuleSlotIndex'
_R='hm2PoeMgmtModuleUnitIndex'
_Q='class4'
_P='class3'
_O='class2'
_N='class1'
_M='class0'
_L='hm2PoeMgmtModulePowerSource'
_K='SnmpAdminString'
_J='hm2PoeMgmtModuleDeliveredPower'
_I='HmTimeHHMM24'
_H='hm2IfacePhysIndex'
_G='HM2-DEVMGMT-MIB'
_F='HmEnabledStatus'
_E='HM2-POE-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hm2IfacePhysIndex,=mibBuilder.importSymbols(_G,_H)
HmEnabledStatus,HmTimeHHMM24,hm2ConfigurationMibs=mibBuilder.importSymbols('HM2-TC-MIB',_F,_I,'hm2ConfigurationMibs')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_K)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hm2PoeMgmtMib=ModuleIdentity((1,3,6,1,4,1,248,11,12))
if mibBuilder.loadTexts:hm2PoeMgmtMib.setRevisions(('2011-10-31 00:00',))
_Hm2PoeMgmtMibNotifications_ObjectIdentity=ObjectIdentity
hm2PoeMgmtMibNotifications=_Hm2PoeMgmtMibNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,12,0))
_Hm2PoeMgmtMibObjects_ObjectIdentity=ObjectIdentity
hm2PoeMgmtMibObjects=_Hm2PoeMgmtMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,12,1))
_Hm2PoeMgmtGroup_ObjectIdentity=ObjectIdentity
hm2PoeMgmtGroup=_Hm2PoeMgmtGroup_ObjectIdentity((1,3,6,1,4,1,248,11,12,1,1))
_Hm2PoeMgmtGlobalGroup_ObjectIdentity=ObjectIdentity
hm2PoeMgmtGlobalGroup=_Hm2PoeMgmtGlobalGroup_ObjectIdentity((1,3,6,1,4,1,248,11,12,1,1,1))
class _Hm2PoeMgmtAdminStatus_Type(HmEnabledStatus):defaultValue=1
_Hm2PoeMgmtAdminStatus_Type.__name__=_F
_Hm2PoeMgmtAdminStatus_Object=MibScalar
hm2PoeMgmtAdminStatus=_Hm2PoeMgmtAdminStatus_Object((1,3,6,1,4,1,248,11,12,1,1,1,1),_Hm2PoeMgmtAdminStatus_Type())
hm2PoeMgmtAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PoeMgmtAdminStatus.setStatus(_A)
_Hm2PoeMgmtReservedPower_Type=Integer32
_Hm2PoeMgmtReservedPower_Object=MibScalar
hm2PoeMgmtReservedPower=_Hm2PoeMgmtReservedPower_Object((1,3,6,1,4,1,248,11,12,1,1,1,2),_Hm2PoeMgmtReservedPower_Type())
hm2PoeMgmtReservedPower.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PoeMgmtReservedPower.setStatus(_A)
_Hm2PoeMgmtDeliveredCurrent_Type=Integer32
_Hm2PoeMgmtDeliveredCurrent_Object=MibScalar
hm2PoeMgmtDeliveredCurrent=_Hm2PoeMgmtDeliveredCurrent_Object((1,3,6,1,4,1,248,11,12,1,1,1,3),_Hm2PoeMgmtDeliveredCurrent_Type())
hm2PoeMgmtDeliveredCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PoeMgmtDeliveredCurrent.setStatus(_A)
_Hm2PoeMgmtPsuTable_Object=MibTable
hm2PoeMgmtPsuTable=_Hm2PoeMgmtPsuTable_Object((1,3,6,1,4,1,248,11,12,1,1,2))
if mibBuilder.loadTexts:hm2PoeMgmtPsuTable.setStatus(_A)
_Hm2PoeMgmtPsuEntry_Object=MibTableRow
hm2PoeMgmtPsuEntry=_Hm2PoeMgmtPsuEntry_Object((1,3,6,1,4,1,248,11,12,1,1,2,1))
hm2PoeMgmtPsuEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:hm2PoeMgmtPsuEntry.setStatus(_A)
_Hm2PoeMgmtPsuPower_Type=Integer32
_Hm2PoeMgmtPsuPower_Object=MibTableColumn
hm2PoeMgmtPsuPower=_Hm2PoeMgmtPsuPower_Object((1,3,6,1,4,1,248,11,12,1,1,2,1,1),_Hm2PoeMgmtPsuPower_Type())
hm2PoeMgmtPsuPower.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PoeMgmtPsuPower.setStatus(_A)
_Hm2PoeMgmtPsuReservedPower_Type=Integer32
_Hm2PoeMgmtPsuReservedPower_Object=MibTableColumn
hm2PoeMgmtPsuReservedPower=_Hm2PoeMgmtPsuReservedPower_Object((1,3,6,1,4,1,248,11,12,1,1,2,1,2),_Hm2PoeMgmtPsuReservedPower_Type())
hm2PoeMgmtPsuReservedPower.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PoeMgmtPsuReservedPower.setStatus(_A)
_Hm2PoeMgmtPsuDeliveredPower_Type=Integer32
_Hm2PoeMgmtPsuDeliveredPower_Object=MibTableColumn
hm2PoeMgmtPsuDeliveredPower=_Hm2PoeMgmtPsuDeliveredPower_Object((1,3,6,1,4,1,248,11,12,1,1,2,1,3),_Hm2PoeMgmtPsuDeliveredPower_Type())
hm2PoeMgmtPsuDeliveredPower.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PoeMgmtPsuDeliveredPower.setStatus(_A)
_Hm2PoeMgmtPsuDeliveredCurrent_Type=Integer32
_Hm2PoeMgmtPsuDeliveredCurrent_Object=MibTableColumn
hm2PoeMgmtPsuDeliveredCurrent=_Hm2PoeMgmtPsuDeliveredCurrent_Object((1,3,6,1,4,1,248,11,12,1,1,2,1,4),_Hm2PoeMgmtPsuDeliveredCurrent_Type())
hm2PoeMgmtPsuDeliveredCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PoeMgmtPsuDeliveredCurrent.setStatus(_A)
_Hm2PoeMgmtPortTable_Object=MibTable
hm2PoeMgmtPortTable=_Hm2PoeMgmtPortTable_Object((1,3,6,1,4,1,248,11,12,1,1,3))
if mibBuilder.loadTexts:hm2PoeMgmtPortTable.setStatus(_A)
_Hm2PoeMgmtPortEntry_Object=MibTableRow
hm2PoeMgmtPortEntry=_Hm2PoeMgmtPortEntry_Object((1,3,6,1,4,1,248,11,12,1,1,3,1))
hm2PoeMgmtPortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:hm2PoeMgmtPortEntry.setStatus(_A)
class _Hm2PoeMgmtPortAdminEnable_Type(HmEnabledStatus):defaultValue=1
_Hm2PoeMgmtPortAdminEnable_Type.__name__=_F
_Hm2PoeMgmtPortAdminEnable_Object=MibTableColumn
hm2PoeMgmtPortAdminEnable=_Hm2PoeMgmtPortAdminEnable_Object((1,3,6,1,4,1,248,11,12,1,1,3,1,1),_Hm2PoeMgmtPortAdminEnable_Type())
hm2PoeMgmtPortAdminEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PoeMgmtPortAdminEnable.setStatus(_A)
_Hm2PoeMgmtPortConsumptionPower_Type=Integer32
_Hm2PoeMgmtPortConsumptionPower_Object=MibTableColumn
hm2PoeMgmtPortConsumptionPower=_Hm2PoeMgmtPortConsumptionPower_Object((1,3,6,1,4,1,248,11,12,1,1,3,1,2),_Hm2PoeMgmtPortConsumptionPower_Type())
hm2PoeMgmtPortConsumptionPower.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PoeMgmtPortConsumptionPower.setStatus(_A)
class _Hm2PoeMgmtPortDetectionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('disabled',1),('searching',2),('deliveringPower',3),('fault',4),('test',5),('otherFault',6)))
_Hm2PoeMgmtPortDetectionStatus_Type.__name__=_D
_Hm2PoeMgmtPortDetectionStatus_Object=MibTableColumn
hm2PoeMgmtPortDetectionStatus=_Hm2PoeMgmtPortDetectionStatus_Object((1,3,6,1,4,1,248,11,12,1,1,3,1,3),_Hm2PoeMgmtPortDetectionStatus_Type())
hm2PoeMgmtPortDetectionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PoeMgmtPortDetectionStatus.setStatus(_A)
class _Hm2PoeMgmtPortPowerPriority_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('critical',1),('high',2),('low',3)))
_Hm2PoeMgmtPortPowerPriority_Type.__name__=_D
_Hm2PoeMgmtPortPowerPriority_Object=MibTableColumn
hm2PoeMgmtPortPowerPriority=_Hm2PoeMgmtPortPowerPriority_Object((1,3,6,1,4,1,248,11,12,1,1,3,1,4),_Hm2PoeMgmtPortPowerPriority_Type())
hm2PoeMgmtPortPowerPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PoeMgmtPortPowerPriority.setStatus(_A)
class _Hm2PoeMgmtPortPowerClassification_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4),(_Q,5)))
_Hm2PoeMgmtPortPowerClassification_Type.__name__=_D
_Hm2PoeMgmtPortPowerClassification_Object=MibTableColumn
hm2PoeMgmtPortPowerClassification=_Hm2PoeMgmtPortPowerClassification_Object((1,3,6,1,4,1,248,11,12,1,1,3,1,5),_Hm2PoeMgmtPortPowerClassification_Type())
hm2PoeMgmtPortPowerClassification.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PoeMgmtPortPowerClassification.setStatus(_A)
class _Hm2PoeMgmtPortName_Type(SnmpAdminString):defaultValue=OctetString(' ');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_Hm2PoeMgmtPortName_Type.__name__=_K
_Hm2PoeMgmtPortName_Object=MibTableColumn
hm2PoeMgmtPortName=_Hm2PoeMgmtPortName_Object((1,3,6,1,4,1,248,11,12,1,1,3,1,6),_Hm2PoeMgmtPortName_Type())
hm2PoeMgmtPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PoeMgmtPortName.setStatus(_A)
class _Hm2PoeMgmtPortAllowedClassBits_Type(Bits):defaultBinValue='11111';namedValues=NamedValues(*((_M,0),(_N,1),(_O,2),(_P,3),(_Q,4)))
_Hm2PoeMgmtPortAllowedClassBits_Type.__name__='Bits'
_Hm2PoeMgmtPortAllowedClassBits_Object=MibTableColumn
hm2PoeMgmtPortAllowedClassBits=_Hm2PoeMgmtPortAllowedClassBits_Object((1,3,6,1,4,1,248,11,12,1,1,3,1,7),_Hm2PoeMgmtPortAllowedClassBits_Type())
hm2PoeMgmtPortAllowedClassBits.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PoeMgmtPortAllowedClassBits.setStatus(_A)
class _Hm2PoeMgmtPortAutoShutdown_Type(HmEnabledStatus):defaultValue=2
_Hm2PoeMgmtPortAutoShutdown_Type.__name__=_F
_Hm2PoeMgmtPortAutoShutdown_Object=MibTableColumn
hm2PoeMgmtPortAutoShutdown=_Hm2PoeMgmtPortAutoShutdown_Object((1,3,6,1,4,1,248,11,12,1,1,3,1,8),_Hm2PoeMgmtPortAutoShutdown_Type())
hm2PoeMgmtPortAutoShutdown.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PoeMgmtPortAutoShutdown.setStatus(_A)
class _Hm2PoeMgmtPortAutoShutdownTimeStart_Type(HmTimeHHMM24):defaultValue=OctetString('00:00')
_Hm2PoeMgmtPortAutoShutdownTimeStart_Type.__name__=_I
_Hm2PoeMgmtPortAutoShutdownTimeStart_Object=MibTableColumn
hm2PoeMgmtPortAutoShutdownTimeStart=_Hm2PoeMgmtPortAutoShutdownTimeStart_Object((1,3,6,1,4,1,248,11,12,1,1,3,1,9),_Hm2PoeMgmtPortAutoShutdownTimeStart_Type())
hm2PoeMgmtPortAutoShutdownTimeStart.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PoeMgmtPortAutoShutdownTimeStart.setStatus(_A)
class _Hm2PoeMgmtPortAutoShutdownTimeEnd_Type(HmTimeHHMM24):defaultValue=OctetString('00:00')
_Hm2PoeMgmtPortAutoShutdownTimeEnd_Type.__name__=_I
_Hm2PoeMgmtPortAutoShutdownTimeEnd_Object=MibTableColumn
hm2PoeMgmtPortAutoShutdownTimeEnd=_Hm2PoeMgmtPortAutoShutdownTimeEnd_Object((1,3,6,1,4,1,248,11,12,1,1,3,1,10),_Hm2PoeMgmtPortAutoShutdownTimeEnd_Type())
hm2PoeMgmtPortAutoShutdownTimeEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PoeMgmtPortAutoShutdownTimeEnd.setStatus(_A)
class _Hm2PoeMgmtPortClassValid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('invalid',0),('valid',1)))
_Hm2PoeMgmtPortClassValid_Type.__name__=_D
_Hm2PoeMgmtPortClassValid_Object=MibTableColumn
hm2PoeMgmtPortClassValid=_Hm2PoeMgmtPortClassValid_Object((1,3,6,1,4,1,248,11,12,1,1,3,1,11),_Hm2PoeMgmtPortClassValid_Type())
hm2PoeMgmtPortClassValid.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PoeMgmtPortClassValid.setStatus(_A)
class _Hm2PoeMgmtPortFastStartup_Type(HmEnabledStatus):defaultValue=2
_Hm2PoeMgmtPortFastStartup_Type.__name__=_F
_Hm2PoeMgmtPortFastStartup_Object=MibTableColumn
hm2PoeMgmtPortFastStartup=_Hm2PoeMgmtPortFastStartup_Object((1,3,6,1,4,1,248,11,12,1,1,3,1,12),_Hm2PoeMgmtPortFastStartup_Type())
hm2PoeMgmtPortFastStartup.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PoeMgmtPortFastStartup.setStatus(_A)
_Hm2PoeMgmtPortMaxConsumptionPower_Type=Integer32
_Hm2PoeMgmtPortMaxConsumptionPower_Object=MibTableColumn
hm2PoeMgmtPortMaxConsumptionPower=_Hm2PoeMgmtPortMaxConsumptionPower_Object((1,3,6,1,4,1,248,11,12,1,1,3,1,13),_Hm2PoeMgmtPortMaxConsumptionPower_Type())
hm2PoeMgmtPortMaxConsumptionPower.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PoeMgmtPortMaxConsumptionPower.setStatus(_A)
class _Hm2PoeMgmtPortPowerLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,30000))
_Hm2PoeMgmtPortPowerLimit_Type.__name__=_D
_Hm2PoeMgmtPortPowerLimit_Object=MibTableColumn
hm2PoeMgmtPortPowerLimit=_Hm2PoeMgmtPortPowerLimit_Object((1,3,6,1,4,1,248,11,12,1,1,3,1,14),_Hm2PoeMgmtPortPowerLimit_Type())
hm2PoeMgmtPortPowerLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PoeMgmtPortPowerLimit.setStatus(_A)
_Hm2PoeMgmtPortConsumptionCurrent_Type=Integer32
_Hm2PoeMgmtPortConsumptionCurrent_Object=MibTableColumn
hm2PoeMgmtPortConsumptionCurrent=_Hm2PoeMgmtPortConsumptionCurrent_Object((1,3,6,1,4,1,248,11,12,1,1,3,1,15),_Hm2PoeMgmtPortConsumptionCurrent_Type())
hm2PoeMgmtPortConsumptionCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PoeMgmtPortConsumptionCurrent.setStatus(_A)
_Hm2PoeMgmtModuleTable_Object=MibTable
hm2PoeMgmtModuleTable=_Hm2PoeMgmtModuleTable_Object((1,3,6,1,4,1,248,11,12,1,1,4))
if mibBuilder.loadTexts:hm2PoeMgmtModuleTable.setStatus(_A)
_Hm2PoeMgmtModuleEntry_Object=MibTableRow
hm2PoeMgmtModuleEntry=_Hm2PoeMgmtModuleEntry_Object((1,3,6,1,4,1,248,11,12,1,1,4,1))
hm2PoeMgmtModuleEntry.setIndexNames((0,_E,_R),(0,_E,_S))
if mibBuilder.loadTexts:hm2PoeMgmtModuleEntry.setStatus(_A)
_Hm2PoeMgmtModuleUnitIndex_Type=Integer32
_Hm2PoeMgmtModuleUnitIndex_Object=MibTableColumn
hm2PoeMgmtModuleUnitIndex=_Hm2PoeMgmtModuleUnitIndex_Object((1,3,6,1,4,1,248,11,12,1,1,4,1,1),_Hm2PoeMgmtModuleUnitIndex_Type())
hm2PoeMgmtModuleUnitIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:hm2PoeMgmtModuleUnitIndex.setStatus(_A)
_Hm2PoeMgmtModuleSlotIndex_Type=Integer32
_Hm2PoeMgmtModuleSlotIndex_Object=MibTableColumn
hm2PoeMgmtModuleSlotIndex=_Hm2PoeMgmtModuleSlotIndex_Object((1,3,6,1,4,1,248,11,12,1,1,4,1,2),_Hm2PoeMgmtModuleSlotIndex_Type())
hm2PoeMgmtModuleSlotIndex.setMaxAccess(_T)
if mibBuilder.loadTexts:hm2PoeMgmtModuleSlotIndex.setStatus(_A)
class _Hm2PoeMgmtModulePower_Type(Integer32):defaultValue=1000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_Hm2PoeMgmtModulePower_Type.__name__=_D
_Hm2PoeMgmtModulePower_Object=MibTableColumn
hm2PoeMgmtModulePower=_Hm2PoeMgmtModulePower_Object((1,3,6,1,4,1,248,11,12,1,1,4,1,3),_Hm2PoeMgmtModulePower_Type())
hm2PoeMgmtModulePower.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PoeMgmtModulePower.setStatus(_A)
class _Hm2PoeMgmtModuleMaximumPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_Hm2PoeMgmtModuleMaximumPower_Type.__name__=_D
_Hm2PoeMgmtModuleMaximumPower_Object=MibTableColumn
hm2PoeMgmtModuleMaximumPower=_Hm2PoeMgmtModuleMaximumPower_Object((1,3,6,1,4,1,248,11,12,1,1,4,1,4),_Hm2PoeMgmtModuleMaximumPower_Type())
hm2PoeMgmtModuleMaximumPower.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PoeMgmtModuleMaximumPower.setStatus(_A)
_Hm2PoeMgmtModuleReservedPower_Type=Integer32
_Hm2PoeMgmtModuleReservedPower_Object=MibTableColumn
hm2PoeMgmtModuleReservedPower=_Hm2PoeMgmtModuleReservedPower_Object((1,3,6,1,4,1,248,11,12,1,1,4,1,5),_Hm2PoeMgmtModuleReservedPower_Type())
hm2PoeMgmtModuleReservedPower.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PoeMgmtModuleReservedPower.setStatus(_A)
_Hm2PoeMgmtModuleDeliveredPower_Type=Integer32
_Hm2PoeMgmtModuleDeliveredPower_Object=MibTableColumn
hm2PoeMgmtModuleDeliveredPower=_Hm2PoeMgmtModuleDeliveredPower_Object((1,3,6,1,4,1,248,11,12,1,1,4,1,6),_Hm2PoeMgmtModuleDeliveredPower_Type())
hm2PoeMgmtModuleDeliveredPower.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PoeMgmtModuleDeliveredPower.setStatus(_A)
class _Hm2PoeMgmtModulePowerSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('internal',0),('external',1)))
_Hm2PoeMgmtModulePowerSource_Type.__name__=_D
_Hm2PoeMgmtModulePowerSource_Object=MibTableColumn
hm2PoeMgmtModulePowerSource=_Hm2PoeMgmtModulePowerSource_Object((1,3,6,1,4,1,248,11,12,1,1,4,1,7),_Hm2PoeMgmtModulePowerSource_Type())
hm2PoeMgmtModulePowerSource.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PoeMgmtModulePowerSource.setStatus(_A)
class _Hm2PoeMgmtModuleUsageThreshold_Type(Integer32):defaultValue=90;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,99))
_Hm2PoeMgmtModuleUsageThreshold_Type.__name__=_D
_Hm2PoeMgmtModuleUsageThreshold_Object=MibTableColumn
hm2PoeMgmtModuleUsageThreshold=_Hm2PoeMgmtModuleUsageThreshold_Object((1,3,6,1,4,1,248,11,12,1,1,4,1,8),_Hm2PoeMgmtModuleUsageThreshold_Type())
hm2PoeMgmtModuleUsageThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PoeMgmtModuleUsageThreshold.setStatus(_A)
class _Hm2PoeMgmtModuleNotificationControlEnable_Type(HmEnabledStatus):defaultValue=1
_Hm2PoeMgmtModuleNotificationControlEnable_Type.__name__=_F
_Hm2PoeMgmtModuleNotificationControlEnable_Object=MibTableColumn
hm2PoeMgmtModuleNotificationControlEnable=_Hm2PoeMgmtModuleNotificationControlEnable_Object((1,3,6,1,4,1,248,11,12,1,1,4,1,9),_Hm2PoeMgmtModuleNotificationControlEnable_Type())
hm2PoeMgmtModuleNotificationControlEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hm2PoeMgmtModuleNotificationControlEnable.setStatus(_A)
_Hm2PoeMgmtModuleDeliveredCurrent_Type=Integer32
_Hm2PoeMgmtModuleDeliveredCurrent_Object=MibTableColumn
hm2PoeMgmtModuleDeliveredCurrent=_Hm2PoeMgmtModuleDeliveredCurrent_Object((1,3,6,1,4,1,248,11,12,1,1,4,1,10),_Hm2PoeMgmtModuleDeliveredCurrent_Type())
hm2PoeMgmtModuleDeliveredCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2PoeMgmtModuleDeliveredCurrent.setStatus(_A)
hm2PoeMgmtModulePowerUsageOnNotification=NotificationType((1,3,6,1,4,1,248,11,12,0,1))
hm2PoeMgmtModulePowerUsageOnNotification.setObjects((_E,_J))
if mibBuilder.loadTexts:hm2PoeMgmtModulePowerUsageOnNotification.setStatus(_A)
hm2PoeMgmtModulePowerUsageOffNotification=NotificationType((1,3,6,1,4,1,248,11,12,0,2))
hm2PoeMgmtModulePowerUsageOffNotification.setObjects((_E,_J))
if mibBuilder.loadTexts:hm2PoeMgmtModulePowerUsageOffNotification.setStatus(_A)
hm2PoeMgmtPortMaxConfiguredPowerLimitExceeded=NotificationType((1,3,6,1,4,1,248,11,12,0,3))
hm2PoeMgmtPortMaxConfiguredPowerLimitExceeded.setObjects(*((_G,_H),(_E,_U),(_E,_V)))
if mibBuilder.loadTexts:hm2PoeMgmtPortMaxConfiguredPowerLimitExceeded.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'hm2PoeMgmtMib':hm2PoeMgmtMib,'hm2PoeMgmtMibNotifications':hm2PoeMgmtMibNotifications,'hm2PoeMgmtModulePowerUsageOnNotification':hm2PoeMgmtModulePowerUsageOnNotification,'hm2PoeMgmtModulePowerUsageOffNotification':hm2PoeMgmtModulePowerUsageOffNotification,'hm2PoeMgmtPortMaxConfiguredPowerLimitExceeded':hm2PoeMgmtPortMaxConfiguredPowerLimitExceeded,'hm2PoeMgmtMibObjects':hm2PoeMgmtMibObjects,'hm2PoeMgmtGroup':hm2PoeMgmtGroup,'hm2PoeMgmtGlobalGroup':hm2PoeMgmtGlobalGroup,'hm2PoeMgmtAdminStatus':hm2PoeMgmtAdminStatus,'hm2PoeMgmtReservedPower':hm2PoeMgmtReservedPower,'hm2PoeMgmtDeliveredCurrent':hm2PoeMgmtDeliveredCurrent,'hm2PoeMgmtPsuTable':hm2PoeMgmtPsuTable,'hm2PoeMgmtPsuEntry':hm2PoeMgmtPsuEntry,'hm2PoeMgmtPsuPower':hm2PoeMgmtPsuPower,'hm2PoeMgmtPsuReservedPower':hm2PoeMgmtPsuReservedPower,'hm2PoeMgmtPsuDeliveredPower':hm2PoeMgmtPsuDeliveredPower,'hm2PoeMgmtPsuDeliveredCurrent':hm2PoeMgmtPsuDeliveredCurrent,'hm2PoeMgmtPortTable':hm2PoeMgmtPortTable,'hm2PoeMgmtPortEntry':hm2PoeMgmtPortEntry,'hm2PoeMgmtPortAdminEnable':hm2PoeMgmtPortAdminEnable,'hm2PoeMgmtPortConsumptionPower':hm2PoeMgmtPortConsumptionPower,'hm2PoeMgmtPortDetectionStatus':hm2PoeMgmtPortDetectionStatus,'hm2PoeMgmtPortPowerPriority':hm2PoeMgmtPortPowerPriority,'hm2PoeMgmtPortPowerClassification':hm2PoeMgmtPortPowerClassification,'hm2PoeMgmtPortName':hm2PoeMgmtPortName,'hm2PoeMgmtPortAllowedClassBits':hm2PoeMgmtPortAllowedClassBits,'hm2PoeMgmtPortAutoShutdown':hm2PoeMgmtPortAutoShutdown,'hm2PoeMgmtPortAutoShutdownTimeStart':hm2PoeMgmtPortAutoShutdownTimeStart,'hm2PoeMgmtPortAutoShutdownTimeEnd':hm2PoeMgmtPortAutoShutdownTimeEnd,'hm2PoeMgmtPortClassValid':hm2PoeMgmtPortClassValid,'hm2PoeMgmtPortFastStartup':hm2PoeMgmtPortFastStartup,_U:hm2PoeMgmtPortMaxConsumptionPower,_V:hm2PoeMgmtPortPowerLimit,'hm2PoeMgmtPortConsumptionCurrent':hm2PoeMgmtPortConsumptionCurrent,'hm2PoeMgmtModuleTable':hm2PoeMgmtModuleTable,'hm2PoeMgmtModuleEntry':hm2PoeMgmtModuleEntry,_R:hm2PoeMgmtModuleUnitIndex,_S:hm2PoeMgmtModuleSlotIndex,'hm2PoeMgmtModulePower':hm2PoeMgmtModulePower,'hm2PoeMgmtModuleMaximumPower':hm2PoeMgmtModuleMaximumPower,'hm2PoeMgmtModuleReservedPower':hm2PoeMgmtModuleReservedPower,_J:hm2PoeMgmtModuleDeliveredPower,_L:hm2PoeMgmtModulePowerSource,'hm2PoeMgmtModuleUsageThreshold':hm2PoeMgmtModuleUsageThreshold,'hm2PoeMgmtModuleNotificationControlEnable':hm2PoeMgmtModuleNotificationControlEnable,'hm2PoeMgmtModuleDeliveredCurrent':hm2PoeMgmtModuleDeliveredCurrent})