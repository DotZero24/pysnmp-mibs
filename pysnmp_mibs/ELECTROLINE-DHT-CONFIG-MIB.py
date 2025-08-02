_J='cfgHmsSnmpAccessIndex'
_I='disable'
_H='cfgHmsEmsAddressIndex'
_G='ELECTROLINE-DHT-CONFIG-MIB'
_F='read-only'
_E='OctetString'
_D='deprecated'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dhtConfiguration,=mibBuilder.importSymbols('ELECTROLINE-DHT-ROOT-MIB','dhtConfiguration')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
_DhtCfgGlobal_ObjectIdentity=ObjectIdentity
dhtCfgGlobal=_DhtCfgGlobal_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,2,1))
if mibBuilder.loadTexts:dhtCfgGlobal.setStatus(_A)
_DhtCfgHmsEms_ObjectIdentity=ObjectIdentity
dhtCfgHmsEms=_DhtCfgHmsEms_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,2,1,1))
if mibBuilder.loadTexts:dhtCfgHmsEms.setStatus(_A)
_CfgHmsEmsAddressTable_Object=MibTable
cfgHmsEmsAddressTable=_CfgHmsEmsAddressTable_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,1,1))
if mibBuilder.loadTexts:cfgHmsEmsAddressTable.setStatus(_A)
_CfgHmsEmsAddressEntry_Object=MibTableRow
cfgHmsEmsAddressEntry=_CfgHmsEmsAddressEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,1,1,1))
cfgHmsEmsAddressEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cfgHmsEmsAddressEntry.setStatus(_A)
_CfgHmsEmsAddressIndex_Type=Integer32
_CfgHmsEmsAddressIndex_Object=MibTableColumn
cfgHmsEmsAddressIndex=_CfgHmsEmsAddressIndex_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,1,1,1,1),_CfgHmsEmsAddressIndex_Type())
cfgHmsEmsAddressIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cfgHmsEmsAddressIndex.setStatus(_A)
_CfgHmsEmsAddressIP_Type=IpAddress
_CfgHmsEmsAddressIP_Object=MibTableColumn
cfgHmsEmsAddressIP=_CfgHmsEmsAddressIP_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,1,1,1,2),_CfgHmsEmsAddressIP_Type())
cfgHmsEmsAddressIP.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgHmsEmsAddressIP.setStatus(_D)
_CfgHmsEmsAddressStartTrapAssurance_Type=TruthValue
_CfgHmsEmsAddressStartTrapAssurance_Object=MibTableColumn
cfgHmsEmsAddressStartTrapAssurance=_CfgHmsEmsAddressStartTrapAssurance_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,1,1,1,3),_CfgHmsEmsAddressStartTrapAssurance_Type())
cfgHmsEmsAddressStartTrapAssurance.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgHmsEmsAddressStartTrapAssurance.setStatus(_A)
_CfgHmsEmsAddressAlarmTrapAssurance_Type=TruthValue
_CfgHmsEmsAddressAlarmTrapAssurance_Object=MibTableColumn
cfgHmsEmsAddressAlarmTrapAssurance=_CfgHmsEmsAddressAlarmTrapAssurance_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,1,1,1,4),_CfgHmsEmsAddressAlarmTrapAssurance_Type())
cfgHmsEmsAddressAlarmTrapAssurance.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgHmsEmsAddressAlarmTrapAssurance.setStatus(_A)
class _CfgHmsEmsAddressTrapPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CfgHmsEmsAddressTrapPortNumber_Type.__name__=_C
_CfgHmsEmsAddressTrapPortNumber_Object=MibTableColumn
cfgHmsEmsAddressTrapPortNumber=_CfgHmsEmsAddressTrapPortNumber_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,1,1,1,5),_CfgHmsEmsAddressTrapPortNumber_Type())
cfgHmsEmsAddressTrapPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgHmsEmsAddressTrapPortNumber.setStatus(_A)
_CfgHmsEmsAddressTypeInet_Type=InetAddressType
_CfgHmsEmsAddressTypeInet_Object=MibTableColumn
cfgHmsEmsAddressTypeInet=_CfgHmsEmsAddressTypeInet_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,1,1,1,6),_CfgHmsEmsAddressTypeInet_Type())
cfgHmsEmsAddressTypeInet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgHmsEmsAddressTypeInet.setStatus(_A)
_CfgHmsEmsAddressInet_Type=InetAddress
_CfgHmsEmsAddressInet_Object=MibTableColumn
cfgHmsEmsAddressInet=_CfgHmsEmsAddressInet_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,1,1,1,7),_CfgHmsEmsAddressInet_Type())
cfgHmsEmsAddressInet.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgHmsEmsAddressInet.setStatus(_A)
class _CfgEmsTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,86400))
_CfgEmsTimeout_Type.__name__=_C
_CfgEmsTimeout_Object=MibScalar
cfgEmsTimeout=_CfgEmsTimeout_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,1,2),_CfgEmsTimeout_Type())
cfgEmsTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgEmsTimeout.setStatus(_A)
_CfgEmsRetry_Type=Integer32
_CfgEmsRetry_Object=MibScalar
cfgEmsRetry=_CfgEmsRetry_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,1,3),_CfgEmsRetry_Type())
cfgEmsRetry.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgEmsRetry.setStatus(_A)
class _CfgEmsDefaultHmsProperties_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('setToDefault',1))
_CfgEmsDefaultHmsProperties_Type.__name__=_C
_CfgEmsDefaultHmsProperties_Object=MibScalar
cfgEmsDefaultHmsProperties=_CfgEmsDefaultHmsProperties_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,1,4),_CfgEmsDefaultHmsProperties_Type())
cfgEmsDefaultHmsProperties.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgEmsDefaultHmsProperties.setStatus(_A)
class _CfgEmsCompatibilityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('hmsMode',0),('dhtMode',1)))
_CfgEmsCompatibilityMode_Type.__name__=_C
_CfgEmsCompatibilityMode_Object=MibScalar
cfgEmsCompatibilityMode=_CfgEmsCompatibilityMode_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,1,5),_CfgEmsCompatibilityMode_Type())
cfgEmsCompatibilityMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgEmsCompatibilityMode.setStatus('obsolete')
class _CfgEmsXpdrName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CfgEmsXpdrName_Type.__name__=_E
_CfgEmsXpdrName_Object=MibScalar
cfgEmsXpdrName=_CfgEmsXpdrName_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,1,6),_CfgEmsXpdrName_Type())
cfgEmsXpdrName.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgEmsXpdrName.setStatus(_A)
class _CfgEmsXpdrLocation_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CfgEmsXpdrLocation_Type.__name__=_E
_CfgEmsXpdrLocation_Object=MibScalar
cfgEmsXpdrLocation=_CfgEmsXpdrLocation_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,1,7),_CfgEmsXpdrLocation_Type())
cfgEmsXpdrLocation.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgEmsXpdrLocation.setStatus(_A)
class _CfgEmsXpdrDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CfgEmsXpdrDescription_Type.__name__=_E
_CfgEmsXpdrDescription_Object=MibScalar
cfgEmsXpdrDescription=_CfgEmsXpdrDescription_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,1,8),_CfgEmsXpdrDescription_Type())
cfgEmsXpdrDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgEmsXpdrDescription.setStatus(_A)
class _CfgEmsXpdrGroupPath_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CfgEmsXpdrGroupPath_Type.__name__=_E
_CfgEmsXpdrGroupPath_Object=MibScalar
cfgEmsXpdrGroupPath=_CfgEmsXpdrGroupPath_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,1,9),_CfgEmsXpdrGroupPath_Type())
cfgEmsXpdrGroupPath.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgEmsXpdrGroupPath.setStatus(_A)
class _CfgEmsXpdrCustomField1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CfgEmsXpdrCustomField1_Type.__name__=_E
_CfgEmsXpdrCustomField1_Object=MibScalar
cfgEmsXpdrCustomField1=_CfgEmsXpdrCustomField1_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,1,10),_CfgEmsXpdrCustomField1_Type())
cfgEmsXpdrCustomField1.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgEmsXpdrCustomField1.setStatus(_A)
class _CfgEmsXpdrCustomField2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CfgEmsXpdrCustomField2_Type.__name__=_E
_CfgEmsXpdrCustomField2_Object=MibScalar
cfgEmsXpdrCustomField2=_CfgEmsXpdrCustomField2_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,1,11),_CfgEmsXpdrCustomField2_Type())
cfgEmsXpdrCustomField2.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgEmsXpdrCustomField2.setStatus(_A)
class _CfgEmsXpdrCustomField3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_CfgEmsXpdrCustomField3_Type.__name__=_E
_CfgEmsXpdrCustomField3_Object=MibScalar
cfgEmsXpdrCustomField3=_CfgEmsXpdrCustomField3_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,1,12),_CfgEmsXpdrCustomField3_Type())
cfgEmsXpdrCustomField3.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgEmsXpdrCustomField3.setStatus(_A)
class _DhtCfgResetToFactory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_DhtCfgResetToFactory_Type.__name__=_C
_DhtCfgResetToFactory_Object=MibScalar
dhtCfgResetToFactory=_DhtCfgResetToFactory_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,2),_DhtCfgResetToFactory_Type())
dhtCfgResetToFactory.setMaxAccess(_B)
if mibBuilder.loadTexts:dhtCfgResetToFactory.setStatus(_D)
class _DhtCfgUsbMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_I,0),('cpe',1),('craft',2)))
_DhtCfgUsbMode_Type.__name__=_C
_DhtCfgUsbMode_Object=MibScalar
dhtCfgUsbMode=_DhtCfgUsbMode_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,3),_DhtCfgUsbMode_Type())
dhtCfgUsbMode.setMaxAccess(_B)
if mibBuilder.loadTexts:dhtCfgUsbMode.setStatus(_D)
_DhtCfgTimers_ObjectIdentity=ObjectIdentity
dhtCfgTimers=_DhtCfgTimers_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,2,1,4))
if mibBuilder.loadTexts:dhtCfgTimers.setStatus(_D)
class _CfgSnmpTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10080))
_CfgSnmpTimeout_Type.__name__=_C
_CfgSnmpTimeout_Object=MibScalar
cfgSnmpTimeout=_CfgSnmpTimeout_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,4,1),_CfgSnmpTimeout_Type())
cfgSnmpTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgSnmpTimeout.setStatus(_D)
_DhtCfgIpInterfaces_ObjectIdentity=ObjectIdentity
dhtCfgIpInterfaces=_DhtCfgIpInterfaces_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,2,1,5))
if mibBuilder.loadTexts:dhtCfgIpInterfaces.setStatus(_D)
class _CfgDhtIpMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('singleIp',1),('dualIp',2)))
_CfgDhtIpMode_Type.__name__=_C
_CfgDhtIpMode_Object=MibScalar
cfgDhtIpMode=_CfgDhtIpMode_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,5,1),_CfgDhtIpMode_Type())
cfgDhtIpMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgDhtIpMode.setStatus(_D)
_CfgHmsSnmpAgent_ObjectIdentity=ObjectIdentity
cfgHmsSnmpAgent=_CfgHmsSnmpAgent_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,2,1,5,50))
if mibBuilder.loadTexts:cfgHmsSnmpAgent.setStatus(_D)
_HmsSnmpManagerCommunity_Type=DisplayString
_HmsSnmpManagerCommunity_Object=MibScalar
hmsSnmpManagerCommunity=_HmsSnmpManagerCommunity_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,5,50,1),_HmsSnmpManagerCommunity_Type())
hmsSnmpManagerCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:hmsSnmpManagerCommunity.setStatus(_D)
_HmsSnmpMonitorCommunity_Type=DisplayString
_HmsSnmpMonitorCommunity_Object=MibScalar
hmsSnmpMonitorCommunity=_HmsSnmpMonitorCommunity_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,5,50,2),_HmsSnmpMonitorCommunity_Type())
hmsSnmpMonitorCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:hmsSnmpMonitorCommunity.setStatus(_D)
_CfgHmsSnmpAccess_ObjectIdentity=ObjectIdentity
cfgHmsSnmpAccess=_CfgHmsSnmpAccess_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,2,1,5,50,3))
if mibBuilder.loadTexts:cfgHmsSnmpAccess.setStatus(_D)
_CfgHmsSnmpAccessTable_Object=MibTable
cfgHmsSnmpAccessTable=_CfgHmsSnmpAccessTable_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,5,50,3,1))
if mibBuilder.loadTexts:cfgHmsSnmpAccessTable.setStatus(_D)
_CfgHmsSnmpAccessEntry_Object=MibTableRow
cfgHmsSnmpAccessEntry=_CfgHmsSnmpAccessEntry_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,5,50,3,1,1))
cfgHmsSnmpAccessEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:cfgHmsSnmpAccessEntry.setStatus(_D)
_CfgHmsSnmpAccessIndex_Type=Integer32
_CfgHmsSnmpAccessIndex_Object=MibTableColumn
cfgHmsSnmpAccessIndex=_CfgHmsSnmpAccessIndex_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,5,50,3,1,1,1),_CfgHmsSnmpAccessIndex_Type())
cfgHmsSnmpAccessIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:cfgHmsSnmpAccessIndex.setStatus(_D)
_CfgHmsSnmpAccessIP_Type=IpAddress
_CfgHmsSnmpAccessIP_Object=MibTableColumn
cfgHmsSnmpAccessIP=_CfgHmsSnmpAccessIP_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,5,50,3,1,1,2),_CfgHmsSnmpAccessIP_Type())
cfgHmsSnmpAccessIP.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgHmsSnmpAccessIP.setStatus(_D)
_CfgHmsSnmpAccessIPMask_Type=IpAddress
_CfgHmsSnmpAccessIPMask_Object=MibTableColumn
cfgHmsSnmpAccessIPMask=_CfgHmsSnmpAccessIPMask_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,5,50,3,1,1,3),_CfgHmsSnmpAccessIPMask_Type())
cfgHmsSnmpAccessIPMask.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgHmsSnmpAccessIPMask.setStatus(_D)
class _DhtCfgVendorInfo_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_DhtCfgVendorInfo_Type.__name__=_E
_DhtCfgVendorInfo_Object=MibScalar
dhtCfgVendorInfo=_DhtCfgVendorInfo_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,6),_DhtCfgVendorInfo_Type())
dhtCfgVendorInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:dhtCfgVendorInfo.setStatus(_D)
class _DhtCfgHmsTimeReference_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('utc',2)))
_DhtCfgHmsTimeReference_Type.__name__=_C
_DhtCfgHmsTimeReference_Object=MibScalar
dhtCfgHmsTimeReference=_DhtCfgHmsTimeReference_Object((1,3,6,1,4,1,5802,1,3,1,2,2,1,7),_DhtCfgHmsTimeReference_Type())
dhtCfgHmsTimeReference.setMaxAccess(_B)
if mibBuilder.loadTexts:dhtCfgHmsTimeReference.setStatus(_D)
_DhtCfgPowerSupply_ObjectIdentity=ObjectIdentity
dhtCfgPowerSupply=_DhtCfgPowerSupply_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,2,2))
if mibBuilder.loadTexts:dhtCfgPowerSupply.setStatus(_A)
_DhtCfgBatterySave_ObjectIdentity=ObjectIdentity
dhtCfgBatterySave=_DhtCfgBatterySave_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,2,2,1))
if mibBuilder.loadTexts:dhtCfgBatterySave.setStatus(_A)
class _CfgSleepVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1500))
_CfgSleepVoltage_Type.__name__=_C
_CfgSleepVoltage_Object=MibScalar
cfgSleepVoltage=_CfgSleepVoltage_Object((1,3,6,1,4,1,5802,1,3,1,2,2,2,1,1),_CfgSleepVoltage_Type())
cfgSleepVoltage.setMaxAccess(_F)
if mibBuilder.loadTexts:cfgSleepVoltage.setStatus(_A)
class _CfgWakeUpDeltaVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,500))
_CfgWakeUpDeltaVoltage_Type.__name__=_C
_CfgWakeUpDeltaVoltage_Object=MibScalar
cfgWakeUpDeltaVoltage=_CfgWakeUpDeltaVoltage_Object((1,3,6,1,4,1,5802,1,3,1,2,2,2,1,2),_CfgWakeUpDeltaVoltage_Type())
cfgWakeUpDeltaVoltage.setMaxAccess(_F)
if mibBuilder.loadTexts:cfgWakeUpDeltaVoltage.setStatus(_A)
class _CfgBatterySaveEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('enable',1),(_I,2),('unavailable',3)))
_CfgBatterySaveEnable_Type.__name__=_C
_CfgBatterySaveEnable_Object=MibScalar
cfgBatterySaveEnable=_CfgBatterySaveEnable_Object((1,3,6,1,4,1,5802,1,3,1,2,2,2,1,3),_CfgBatterySaveEnable_Type())
cfgBatterySaveEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgBatterySaveEnable.setStatus(_A)
_DhtCfgPsInverterTest_ObjectIdentity=ObjectIdentity
dhtCfgPsInverterTest=_DhtCfgPsInverterTest_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,2,2,2))
if mibBuilder.loadTexts:dhtCfgPsInverterTest.setStatus(_A)
class _CfgPsInvTestAutoStopTimer_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_CfgPsInvTestAutoStopTimer_Type.__name__=_C
_CfgPsInvTestAutoStopTimer_Object=MibScalar
cfgPsInvTestAutoStopTimer=_CfgPsInvTestAutoStopTimer_Object((1,3,6,1,4,1,5802,1,3,1,2,2,2,2,1),_CfgPsInvTestAutoStopTimer_Type())
cfgPsInvTestAutoStopTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgPsInvTestAutoStopTimer.setStatus(_A)
_DhtCfgPsSetting_ObjectIdentity=ObjectIdentity
dhtCfgPsSetting=_DhtCfgPsSetting_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,2,2,3))
if mibBuilder.loadTexts:dhtCfgPsSetting.setStatus(_A)
class _CfgPsNominalInputVoltage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oneHundredTwenty',1),('twoHundredFourty',2)))
_CfgPsNominalInputVoltage_Type.__name__=_C
_CfgPsNominalInputVoltage_Object=MibScalar
cfgPsNominalInputVoltage=_CfgPsNominalInputVoltage_Object((1,3,6,1,4,1,5802,1,3,1,2,2,2,3,1),_CfgPsNominalInputVoltage_Type())
cfgPsNominalInputVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgPsNominalInputVoltage.setStatus(_A)
_CfgPsTemperatureCalibrationOffset_Type=Integer32
_CfgPsTemperatureCalibrationOffset_Object=MibScalar
cfgPsTemperatureCalibrationOffset=_CfgPsTemperatureCalibrationOffset_Object((1,3,6,1,4,1,5802,1,3,1,2,2,2,3,2),_CfgPsTemperatureCalibrationOffset_Type())
cfgPsTemperatureCalibrationOffset.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgPsTemperatureCalibrationOffset.setStatus(_A)
class _CfgPsOutputCurrent_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('high',2)))
_CfgPsOutputCurrent_Type.__name__=_C
_CfgPsOutputCurrent_Object=MibScalar
cfgPsOutputCurrent=_CfgPsOutputCurrent_Object((1,3,6,1,4,1,5802,1,3,1,2,2,2,3,3),_CfgPsOutputCurrent_Type())
cfgPsOutputCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgPsOutputCurrent.setStatus(_A)
_DhtCfgUsmUnified_ObjectIdentity=ObjectIdentity
dhtCfgUsmUnified=_DhtCfgUsmUnified_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,2,2,3,4))
if mibBuilder.loadTexts:dhtCfgUsmUnified.setStatus(_A)
class _CfgUsmUnifiedMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('auto',1),('usm',2),('usm2',3),('usm25',4),('apcSm7WithInputCurrent',5),('apcSm7WithoutInputCurrent',6)))
_CfgUsmUnifiedMode_Type.__name__=_C
_CfgUsmUnifiedMode_Object=MibScalar
cfgUsmUnifiedMode=_CfgUsmUnifiedMode_Object((1,3,6,1,4,1,5802,1,3,1,2,2,2,3,4,1),_CfgUsmUnifiedMode_Type())
cfgUsmUnifiedMode.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgUsmUnifiedMode.setStatus(_A)
_CfgPsGenericCreation_Type=TruthValue
_CfgPsGenericCreation_Object=MibScalar
cfgPsGenericCreation=_CfgPsGenericCreation_Object((1,3,6,1,4,1,5802,1,3,1,2,2,2,3,5),_CfgPsGenericCreation_Type())
cfgPsGenericCreation.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgPsGenericCreation.setStatus(_A)
class _CfgPsMeasurementSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('analogPort',1),('communicationPort',2)))
_CfgPsMeasurementSource_Type.__name__=_C
_CfgPsMeasurementSource_Object=MibScalar
cfgPsMeasurementSource=_CfgPsMeasurementSource_Object((1,3,6,1,4,1,5802,1,3,1,2,2,2,3,6),_CfgPsMeasurementSource_Type())
cfgPsMeasurementSource.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgPsMeasurementSource.setStatus(_A)
_DhtCfgHMS022_ObjectIdentity=ObjectIdentity
dhtCfgHMS022=_DhtCfgHMS022_ObjectIdentity((1,3,6,1,4,1,5802,1,3,1,2,2,3))
if mibBuilder.loadTexts:dhtCfgHMS022.setStatus(_A)
class _CfgStartAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_CfgStartAddress_Type.__name__=_C
_CfgStartAddress_Object=MibScalar
cfgStartAddress=_CfgStartAddress_Object((1,3,6,1,4,1,5802,1,3,1,2,2,3,1),_CfgStartAddress_Type())
cfgStartAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgStartAddress.setStatus(_A)
class _CfgEndAddress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,31))
_CfgEndAddress_Type.__name__=_C
_CfgEndAddress_Object=MibScalar
cfgEndAddress=_CfgEndAddress_Object((1,3,6,1,4,1,5802,1,3,1,2,2,3,2),_CfgEndAddress_Type())
cfgEndAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cfgEndAddress.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'dhtCfgGlobal':dhtCfgGlobal,'dhtCfgHmsEms':dhtCfgHmsEms,'cfgHmsEmsAddressTable':cfgHmsEmsAddressTable,'cfgHmsEmsAddressEntry':cfgHmsEmsAddressEntry,_H:cfgHmsEmsAddressIndex,'cfgHmsEmsAddressIP':cfgHmsEmsAddressIP,'cfgHmsEmsAddressStartTrapAssurance':cfgHmsEmsAddressStartTrapAssurance,'cfgHmsEmsAddressAlarmTrapAssurance':cfgHmsEmsAddressAlarmTrapAssurance,'cfgHmsEmsAddressTrapPortNumber':cfgHmsEmsAddressTrapPortNumber,'cfgHmsEmsAddressTypeInet':cfgHmsEmsAddressTypeInet,'cfgHmsEmsAddressInet':cfgHmsEmsAddressInet,'cfgEmsTimeout':cfgEmsTimeout,'cfgEmsRetry':cfgEmsRetry,'cfgEmsDefaultHmsProperties':cfgEmsDefaultHmsProperties,'cfgEmsCompatibilityMode':cfgEmsCompatibilityMode,'cfgEmsXpdrName':cfgEmsXpdrName,'cfgEmsXpdrLocation':cfgEmsXpdrLocation,'cfgEmsXpdrDescription':cfgEmsXpdrDescription,'cfgEmsXpdrGroupPath':cfgEmsXpdrGroupPath,'cfgEmsXpdrCustomField1':cfgEmsXpdrCustomField1,'cfgEmsXpdrCustomField2':cfgEmsXpdrCustomField2,'cfgEmsXpdrCustomField3':cfgEmsXpdrCustomField3,'dhtCfgResetToFactory':dhtCfgResetToFactory,'dhtCfgUsbMode':dhtCfgUsbMode,'dhtCfgTimers':dhtCfgTimers,'cfgSnmpTimeout':cfgSnmpTimeout,'dhtCfgIpInterfaces':dhtCfgIpInterfaces,'cfgDhtIpMode':cfgDhtIpMode,'cfgHmsSnmpAgent':cfgHmsSnmpAgent,'hmsSnmpManagerCommunity':hmsSnmpManagerCommunity,'hmsSnmpMonitorCommunity':hmsSnmpMonitorCommunity,'cfgHmsSnmpAccess':cfgHmsSnmpAccess,'cfgHmsSnmpAccessTable':cfgHmsSnmpAccessTable,'cfgHmsSnmpAccessEntry':cfgHmsSnmpAccessEntry,_J:cfgHmsSnmpAccessIndex,'cfgHmsSnmpAccessIP':cfgHmsSnmpAccessIP,'cfgHmsSnmpAccessIPMask':cfgHmsSnmpAccessIPMask,'dhtCfgVendorInfo':dhtCfgVendorInfo,'dhtCfgHmsTimeReference':dhtCfgHmsTimeReference,'dhtCfgPowerSupply':dhtCfgPowerSupply,'dhtCfgBatterySave':dhtCfgBatterySave,'cfgSleepVoltage':cfgSleepVoltage,'cfgWakeUpDeltaVoltage':cfgWakeUpDeltaVoltage,'cfgBatterySaveEnable':cfgBatterySaveEnable,'dhtCfgPsInverterTest':dhtCfgPsInverterTest,'cfgPsInvTestAutoStopTimer':cfgPsInvTestAutoStopTimer,'dhtCfgPsSetting':dhtCfgPsSetting,'cfgPsNominalInputVoltage':cfgPsNominalInputVoltage,'cfgPsTemperatureCalibrationOffset':cfgPsTemperatureCalibrationOffset,'cfgPsOutputCurrent':cfgPsOutputCurrent,'dhtCfgUsmUnified':dhtCfgUsmUnified,'cfgUsmUnifiedMode':cfgUsmUnifiedMode,'cfgPsGenericCreation':cfgPsGenericCreation,'cfgPsMeasurementSource':cfgPsMeasurementSource,'dhtCfgHMS022':dhtCfgHMS022,'cfgStartAddress':cfgStartAddress,'cfgEndAddress':cfgEndAddress})