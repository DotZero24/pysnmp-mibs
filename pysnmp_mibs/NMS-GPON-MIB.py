_AI='gponOnuDyingGaspStatus'
_AH='gponOnuStatusChange'
_AG='onuEquipmentID'
_AF='onuVendorID'
_AE='gponOnuOpticalPowerTxPower'
_AD='gponOnuOpticalPowerRxPower'
_AC='gponOnuSfpParameterAlarmStatus'
_AB='gponOltPonPortOpticalParameterTxPower'
_AA='gponOltPonPortOpticalParameterCurrent'
_A9='gponOltPonPortOpticalParameterVoltage'
_A8='gponOltPonPortOpticalParameterTemperature'
_A7='gponOltPonSfpParameterAlarmStatus'
_A6='onuEthernetUNIPortProfileIndex'
_A5='onuRateCtlProfileIndex'
_A4='onuFlowProfileIndex2'
_A3='onuFlowProfileIndex1'
_A2='onuVirportProfileIndex'
_A1='onuTcontVirportBindProfileIndex'
_A0='onuBandwidthProfileIndex'
_z='onuTcontServiceProfileIndex'
_y='onuVLANTranslationIndex2'
_x='onuVLANTranslationIndex1'
_w='onuVLANProfileIndex'
_v='onuVirPort15MinStatisticIntervalID'
_u='onuVirPort15MinStatisticVirPortIndex'
_t='onuVirPort15MinStatisticDeviceIndex'
_s='onuVirPortStatisticVirPortIndex'
_r='onuVirPortStatisticDeviceIndex'
_q='onuVirPortConfigPortIndex'
_p='onuVirPortConfigDeviceIndex'
_o='onuUniPort15MinStatisticIntervalID'
_n='onuUniPort15MinStatisticUniPortIndex'
_m='onuUniPort15MinStatisticDeviceIndex'
_l='onuUniPortStatisticUniPortIndex'
_k='onuUniPortStatisticDeviceIndex'
_j='onuUniPortConfigPortIndex'
_i='onuUniPortConfigDeviceIndex'
_h='gponOnuBatchUpdateLLIDs'
_g='gponOnuOpticalParameterAlarmDeviceIndex'
_f='gponOnuOpticalPowerDeviceIndex'
_e='gponOnuStatusDeviceIndex'
_d='gponOnuConfigDeviceIndex'
_c='reboot'
_b='shutdown-locks'
_a='priority-controlled'
_Z='gponONUInfoDeviceIndex'
_Y='gponOltONUBindPortIndex'
_X='normal'
_W='gponOltPonPortPowerAlarmIndex'
_V='gponOltPonPortOpticalRxPowerPortIndex'
_U='gponOltPonPortOpticalParameterPortIndex'
_T='shutdown'
_S='no-shutdown'
_R='gponOltPonPortPortIndex'
_Q='onuSerialNum'
_P='current'
_O='write-only'
_N='auto'
_M='ifIndex'
_L='ifDescr'
_K='false'
_J='true'
_I='IF-MIB'
_H='read-create'
_G='enable'
_F='disable'
_E='NMS-GPON-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifDescr,ifIndex=mibBuilder.importSymbols(_I,_L,_M)
nms,=mibBuilder.importSymbols('NMS-SMI','nms')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
nmsGponMIB=ModuleIdentity((1,3,6,1,4,1,3320,10))
_NmsGponOltObj_ObjectIdentity=ObjectIdentity
nmsGponOltObj=_NmsGponOltObj_ObjectIdentity((1,3,6,1,4,1,3320,10,1))
_GponOltConfigTable_ObjectIdentity=ObjectIdentity
gponOltConfigTable=_GponOltConfigTable_ObjectIdentity((1,3,6,1,4,1,3320,10,1,1))
_GponOltConfigEntry_ObjectIdentity=ObjectIdentity
gponOltConfigEntry=_GponOltConfigEntry_ObjectIdentity((1,3,6,1,4,1,3320,10,1,1,1))
class _GponOnuAuthenticationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('serial_number_only',1),('password_only',2),('serial_number_and_password',3),(_F,4)))
_GponOnuAuthenticationMode_Type.__name__=_D
_GponOnuAuthenticationMode_Object=MibScalar
gponOnuAuthenticationMode=_GponOnuAuthenticationMode_Object((1,3,6,1,4,1,3320,10,1,1,1,1),_GponOnuAuthenticationMode_Type())
gponOnuAuthenticationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOnuAuthenticationMode.setStatus(_A)
_GponBroadcastGEMPort_Type=Integer32
_GponBroadcastGEMPort_Object=MibScalar
gponBroadcastGEMPort=_GponBroadcastGEMPort_Object((1,3,6,1,4,1,3320,10,1,1,1,2),_GponBroadcastGEMPort_Type())
gponBroadcastGEMPort.setMaxAccess(_C)
if mibBuilder.loadTexts:gponBroadcastGEMPort.setStatus(_A)
class _GponEncryption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_GponEncryption_Type.__name__=_D
_GponEncryption_Object=MibScalar
gponEncryption=_GponEncryption_Object((1,3,6,1,4,1,3320,10,1,1,1,3),_GponEncryption_Type())
gponEncryption.setMaxAccess(_C)
if mibBuilder.loadTexts:gponEncryption.setStatus(_A)
class _GponKeyExchangeInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,3600))
_GponKeyExchangeInterval_Type.__name__=_D
_GponKeyExchangeInterval_Object=MibScalar
gponKeyExchangeInterval=_GponKeyExchangeInterval_Object((1,3,6,1,4,1,3320,10,1,1,1,4),_GponKeyExchangeInterval_Type())
gponKeyExchangeInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:gponKeyExchangeInterval.setStatus(_A)
_NmsGponOltPonPortObj_ObjectIdentity=ObjectIdentity
nmsGponOltPonPortObj=_NmsGponOltPonPortObj_ObjectIdentity((1,3,6,1,4,1,3320,10,2))
_GponOltPonPortConfigTable_Object=MibTable
gponOltPonPortConfigTable=_GponOltPonPortConfigTable_Object((1,3,6,1,4,1,3320,10,2,1))
if mibBuilder.loadTexts:gponOltPonPortConfigTable.setStatus(_A)
_GponOltPonPortConfigEntry_Object=MibTableRow
gponOltPonPortConfigEntry=_GponOltPonPortConfigEntry_Object((1,3,6,1,4,1,3320,10,2,1,1))
gponOltPonPortConfigEntry.setIndexNames((0,_E,_R))
if mibBuilder.loadTexts:gponOltPonPortConfigEntry.setStatus(_A)
_GponOltPonPortPortIndex_Type=Integer32
_GponOltPonPortPortIndex_Object=MibTableColumn
gponOltPonPortPortIndex=_GponOltPonPortPortIndex_Object((1,3,6,1,4,1,3320,10,2,1,1,1),_GponOltPonPortPortIndex_Type())
gponOltPonPortPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOltPonPortPortIndex.setStatus(_A)
class _GponOltPonPortPortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_GponOltPonPortPortAdminStatus_Type.__name__=_D
_GponOltPonPortPortAdminStatus_Object=MibTableColumn
gponOltPonPortPortAdminStatus=_GponOltPonPortPortAdminStatus_Object((1,3,6,1,4,1,3320,10,2,1,1,2),_GponOltPonPortPortAdminStatus_Type())
gponOltPonPortPortAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortPortAdminStatus.setStatus(_A)
class _GponOltPonPortOnuDiscoveryMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_N,1),('manual',2),(_F,3)))
_GponOltPonPortOnuDiscoveryMode_Type.__name__=_D
_GponOltPonPortOnuDiscoveryMode_Object=MibTableColumn
gponOltPonPortOnuDiscoveryMode=_GponOltPonPortOnuDiscoveryMode_Object((1,3,6,1,4,1,3320,10,2,1,1,3),_GponOltPonPortOnuDiscoveryMode_Type())
gponOltPonPortOnuDiscoveryMode.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortOnuDiscoveryMode.setStatus(_A)
_GponOltPonPortPortActiveOnuNum_Type=Integer32
_GponOltPonPortPortActiveOnuNum_Object=MibTableColumn
gponOltPonPortPortActiveOnuNum=_GponOltPonPortPortActiveOnuNum_Object((1,3,6,1,4,1,3320,10,2,1,1,4),_GponOltPonPortPortActiveOnuNum_Type())
gponOltPonPortPortActiveOnuNum.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOltPonPortPortActiveOnuNum.setStatus(_A)
_GponOltPonPortPortInactiveOnuNum_Type=Integer32
_GponOltPonPortPortInactiveOnuNum_Object=MibTableColumn
gponOltPonPortPortInactiveOnuNum=_GponOltPonPortPortInactiveOnuNum_Object((1,3,6,1,4,1,3320,10,2,1,1,5),_GponOltPonPortPortInactiveOnuNum_Type())
gponOltPonPortPortInactiveOnuNum.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOltPonPortPortInactiveOnuNum.setStatus(_A)
_GponOltPonPortPortLlidIfIndexString_Type=OctetString
_GponOltPonPortPortLlidIfIndexString_Object=MibTableColumn
gponOltPonPortPortLlidIfIndexString=_GponOltPonPortPortLlidIfIndexString_Object((1,3,6,1,4,1,3320,10,2,1,1,6),_GponOltPonPortPortLlidIfIndexString_Type())
gponOltPonPortPortLlidIfIndexString.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOltPonPortPortLlidIfIndexString.setStatus(_A)
_GponOltPonPortOpticalParameterTable_Object=MibTable
gponOltPonPortOpticalParameterTable=_GponOltPonPortOpticalParameterTable_Object((1,3,6,1,4,1,3320,10,2,2))
if mibBuilder.loadTexts:gponOltPonPortOpticalParameterTable.setStatus(_A)
_GponOltPonPortOpticalParameterEntry_Object=MibTableRow
gponOltPonPortOpticalParameterEntry=_GponOltPonPortOpticalParameterEntry_Object((1,3,6,1,4,1,3320,10,2,2,1))
gponOltPonPortOpticalParameterEntry.setIndexNames((0,_E,_U))
if mibBuilder.loadTexts:gponOltPonPortOpticalParameterEntry.setStatus(_A)
_GponOltPonPortOpticalParameterPortIndex_Type=Integer32
_GponOltPonPortOpticalParameterPortIndex_Object=MibTableColumn
gponOltPonPortOpticalParameterPortIndex=_GponOltPonPortOpticalParameterPortIndex_Object((1,3,6,1,4,1,3320,10,2,2,1,1),_GponOltPonPortOpticalParameterPortIndex_Type())
gponOltPonPortOpticalParameterPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOltPonPortOpticalParameterPortIndex.setStatus(_A)
_GponOltPonPortOpticalParameterTemperature_Type=Integer32
_GponOltPonPortOpticalParameterTemperature_Object=MibTableColumn
gponOltPonPortOpticalParameterTemperature=_GponOltPonPortOpticalParameterTemperature_Object((1,3,6,1,4,1,3320,10,2,2,1,2),_GponOltPonPortOpticalParameterTemperature_Type())
gponOltPonPortOpticalParameterTemperature.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOltPonPortOpticalParameterTemperature.setStatus(_A)
_GponOltPonPortOpticalParameterVoltage_Type=Integer32
_GponOltPonPortOpticalParameterVoltage_Object=MibTableColumn
gponOltPonPortOpticalParameterVoltage=_GponOltPonPortOpticalParameterVoltage_Object((1,3,6,1,4,1,3320,10,2,2,1,3),_GponOltPonPortOpticalParameterVoltage_Type())
gponOltPonPortOpticalParameterVoltage.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOltPonPortOpticalParameterVoltage.setStatus(_A)
_GponOltPonPortOpticalParameterCurrent_Type=Integer32
_GponOltPonPortOpticalParameterCurrent_Object=MibTableColumn
gponOltPonPortOpticalParameterCurrent=_GponOltPonPortOpticalParameterCurrent_Object((1,3,6,1,4,1,3320,10,2,2,1,4),_GponOltPonPortOpticalParameterCurrent_Type())
gponOltPonPortOpticalParameterCurrent.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOltPonPortOpticalParameterCurrent.setStatus(_A)
_GponOltPonPortOpticalParameterTxPower_Type=Integer32
_GponOltPonPortOpticalParameterTxPower_Object=MibTableColumn
gponOltPonPortOpticalParameterTxPower=_GponOltPonPortOpticalParameterTxPower_Object((1,3,6,1,4,1,3320,10,2,2,1,5),_GponOltPonPortOpticalParameterTxPower_Type())
gponOltPonPortOpticalParameterTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOltPonPortOpticalParameterTxPower.setStatus(_A)
_GponOltPonPortOpticalRxPowerTable_Object=MibTable
gponOltPonPortOpticalRxPowerTable=_GponOltPonPortOpticalRxPowerTable_Object((1,3,6,1,4,1,3320,10,2,3))
if mibBuilder.loadTexts:gponOltPonPortOpticalRxPowerTable.setStatus(_A)
_GponOltPonPortOpticalRxPowerEntry_Object=MibTableRow
gponOltPonPortOpticalRxPowerEntry=_GponOltPonPortOpticalRxPowerEntry_Object((1,3,6,1,4,1,3320,10,2,3,1))
gponOltPonPortOpticalRxPowerEntry.setIndexNames((0,_E,_V))
if mibBuilder.loadTexts:gponOltPonPortOpticalRxPowerEntry.setStatus(_A)
_GponOltPonPortOpticalRxPowerPortIndex_Type=Integer32
_GponOltPonPortOpticalRxPowerPortIndex_Object=MibTableColumn
gponOltPonPortOpticalRxPowerPortIndex=_GponOltPonPortOpticalRxPowerPortIndex_Object((1,3,6,1,4,1,3320,10,2,3,1,1),_GponOltPonPortOpticalRxPowerPortIndex_Type())
gponOltPonPortOpticalRxPowerPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOltPonPortOpticalRxPowerPortIndex.setStatus(_A)
class _GponOltPonPortOpticalRxPowerLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('link-up',1),('link-down',2)))
_GponOltPonPortOpticalRxPowerLinkStatus_Type.__name__=_D
_GponOltPonPortOpticalRxPowerLinkStatus_Object=MibTableColumn
gponOltPonPortOpticalRxPowerLinkStatus=_GponOltPonPortOpticalRxPowerLinkStatus_Object((1,3,6,1,4,1,3320,10,2,3,1,2),_GponOltPonPortOpticalRxPowerLinkStatus_Type())
gponOltPonPortOpticalRxPowerLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOltPonPortOpticalRxPowerLinkStatus.setStatus(_A)
_GponOltPonPortOpticalRxPowerRxPower_Type=Integer32
_GponOltPonPortOpticalRxPowerRxPower_Object=MibTableColumn
gponOltPonPortOpticalRxPowerRxPower=_GponOltPonPortOpticalRxPowerRxPower_Object((1,3,6,1,4,1,3320,10,2,3,1,3),_GponOltPonPortOpticalRxPowerRxPower_Type())
gponOltPonPortOpticalRxPowerRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOltPonPortOpticalRxPowerRxPower.setStatus(_A)
_GponOltPonPortOpticalParameterAlarmTable_Object=MibTable
gponOltPonPortOpticalParameterAlarmTable=_GponOltPonPortOpticalParameterAlarmTable_Object((1,3,6,1,4,1,3320,10,2,4))
if mibBuilder.loadTexts:gponOltPonPortOpticalParameterAlarmTable.setStatus(_A)
_GponOltPonPortOpticalParameterAlarmEntry_Object=MibTableRow
gponOltPonPortOpticalParameterAlarmEntry=_GponOltPonPortOpticalParameterAlarmEntry_Object((1,3,6,1,4,1,3320,10,2,4,1))
gponOltPonPortOpticalParameterAlarmEntry.setIndexNames((0,_E,_W))
if mibBuilder.loadTexts:gponOltPonPortOpticalParameterAlarmEntry.setStatus(_A)
_GponOltPonPortPowerAlarmIndex_Type=Integer32
_GponOltPonPortPowerAlarmIndex_Object=MibTableColumn
gponOltPonPortPowerAlarmIndex=_GponOltPonPortPowerAlarmIndex_Object((1,3,6,1,4,1,3320,10,2,4,1,1),_GponOltPonPortPowerAlarmIndex_Type())
gponOltPonPortPowerAlarmIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOltPonPortPowerAlarmIndex.setStatus(_A)
class _GponOltPonPortTxPowerAlarmUpLimitEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_GponOltPonPortTxPowerAlarmUpLimitEnable_Type.__name__=_D
_GponOltPonPortTxPowerAlarmUpLimitEnable_Object=MibTableColumn
gponOltPonPortTxPowerAlarmUpLimitEnable=_GponOltPonPortTxPowerAlarmUpLimitEnable_Object((1,3,6,1,4,1,3320,10,2,4,1,2),_GponOltPonPortTxPowerAlarmUpLimitEnable_Type())
gponOltPonPortTxPowerAlarmUpLimitEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortTxPowerAlarmUpLimitEnable.setStatus(_A)
_GponOltPonPortTxPowerAlarmUpLimitThreshold_Type=Integer32
_GponOltPonPortTxPowerAlarmUpLimitThreshold_Object=MibTableColumn
gponOltPonPortTxPowerAlarmUpLimitThreshold=_GponOltPonPortTxPowerAlarmUpLimitThreshold_Object((1,3,6,1,4,1,3320,10,2,4,1,3),_GponOltPonPortTxPowerAlarmUpLimitThreshold_Type())
gponOltPonPortTxPowerAlarmUpLimitThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortTxPowerAlarmUpLimitThreshold.setStatus(_A)
_GponOltPonPortTxPowerAlarmUpLimitClearThreshold_Type=Integer32
_GponOltPonPortTxPowerAlarmUpLimitClearThreshold_Object=MibTableColumn
gponOltPonPortTxPowerAlarmUpLimitClearThreshold=_GponOltPonPortTxPowerAlarmUpLimitClearThreshold_Object((1,3,6,1,4,1,3320,10,2,4,1,4),_GponOltPonPortTxPowerAlarmUpLimitClearThreshold_Type())
gponOltPonPortTxPowerAlarmUpLimitClearThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortTxPowerAlarmUpLimitClearThreshold.setStatus(_A)
class _GponOltPonPortTxPowerAlarmLowLimitEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_GponOltPonPortTxPowerAlarmLowLimitEnable_Type.__name__=_D
_GponOltPonPortTxPowerAlarmLowLimitEnable_Object=MibTableColumn
gponOltPonPortTxPowerAlarmLowLimitEnable=_GponOltPonPortTxPowerAlarmLowLimitEnable_Object((1,3,6,1,4,1,3320,10,2,4,1,5),_GponOltPonPortTxPowerAlarmLowLimitEnable_Type())
gponOltPonPortTxPowerAlarmLowLimitEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortTxPowerAlarmLowLimitEnable.setStatus(_A)
_GponOltPonPortTxPowerAlarmLowLimitThreshold_Type=Integer32
_GponOltPonPortTxPowerAlarmLowLimitThreshold_Object=MibTableColumn
gponOltPonPortTxPowerAlarmLowLimitThreshold=_GponOltPonPortTxPowerAlarmLowLimitThreshold_Object((1,3,6,1,4,1,3320,10,2,4,1,6),_GponOltPonPortTxPowerAlarmLowLimitThreshold_Type())
gponOltPonPortTxPowerAlarmLowLimitThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortTxPowerAlarmLowLimitThreshold.setStatus(_A)
_GponOltPonPortTxPowerAlarmLowLimitClearThreshold_Type=Integer32
_GponOltPonPortTxPowerAlarmLowLimitClearThreshold_Object=MibTableColumn
gponOltPonPortTxPowerAlarmLowLimitClearThreshold=_GponOltPonPortTxPowerAlarmLowLimitClearThreshold_Object((1,3,6,1,4,1,3320,10,2,4,1,7),_GponOltPonPortTxPowerAlarmLowLimitClearThreshold_Type())
gponOltPonPortTxPowerAlarmLowLimitClearThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortTxPowerAlarmLowLimitClearThreshold.setStatus(_A)
class _GponOltPonPortTemperatureAlarmUpLimitEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_GponOltPonPortTemperatureAlarmUpLimitEnable_Type.__name__=_D
_GponOltPonPortTemperatureAlarmUpLimitEnable_Object=MibTableColumn
gponOltPonPortTemperatureAlarmUpLimitEnable=_GponOltPonPortTemperatureAlarmUpLimitEnable_Object((1,3,6,1,4,1,3320,10,2,4,1,8),_GponOltPonPortTemperatureAlarmUpLimitEnable_Type())
gponOltPonPortTemperatureAlarmUpLimitEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortTemperatureAlarmUpLimitEnable.setStatus(_A)
_GponOltPonPortTemperatureAlarmUpLimitThreshold_Type=Integer32
_GponOltPonPortTemperatureAlarmUpLimitThreshold_Object=MibTableColumn
gponOltPonPortTemperatureAlarmUpLimitThreshold=_GponOltPonPortTemperatureAlarmUpLimitThreshold_Object((1,3,6,1,4,1,3320,10,2,4,1,9),_GponOltPonPortTemperatureAlarmUpLimitThreshold_Type())
gponOltPonPortTemperatureAlarmUpLimitThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortTemperatureAlarmUpLimitThreshold.setStatus(_A)
_GponOltPonPortTemperatureAlarmUpLimitClearThreshold_Type=Integer32
_GponOltPonPortTemperatureAlarmUpLimitClearThreshold_Object=MibTableColumn
gponOltPonPortTemperatureAlarmUpLimitClearThreshold=_GponOltPonPortTemperatureAlarmUpLimitClearThreshold_Object((1,3,6,1,4,1,3320,10,2,4,1,10),_GponOltPonPortTemperatureAlarmUpLimitClearThreshold_Type())
gponOltPonPortTemperatureAlarmUpLimitClearThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortTemperatureAlarmUpLimitClearThreshold.setStatus(_A)
class _GponOltPonPortTemperatureAlarmLowLimitEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_GponOltPonPortTemperatureAlarmLowLimitEnable_Type.__name__=_D
_GponOltPonPortTemperatureAlarmLowLimitEnable_Object=MibTableColumn
gponOltPonPortTemperatureAlarmLowLimitEnable=_GponOltPonPortTemperatureAlarmLowLimitEnable_Object((1,3,6,1,4,1,3320,10,2,4,1,11),_GponOltPonPortTemperatureAlarmLowLimitEnable_Type())
gponOltPonPortTemperatureAlarmLowLimitEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortTemperatureAlarmLowLimitEnable.setStatus(_A)
_GponOltPonPortTemperatureAlarmLowLimitThreshold_Type=Integer32
_GponOltPonPortTemperatureAlarmLowLimitThreshold_Object=MibTableColumn
gponOltPonPortTemperatureAlarmLowLimitThreshold=_GponOltPonPortTemperatureAlarmLowLimitThreshold_Object((1,3,6,1,4,1,3320,10,2,4,1,12),_GponOltPonPortTemperatureAlarmLowLimitThreshold_Type())
gponOltPonPortTemperatureAlarmLowLimitThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortTemperatureAlarmLowLimitThreshold.setStatus(_A)
_GponOltPonPortTemperatureAlarmLowLimitClearThreshold_Type=Integer32
_GponOltPonPortTemperatureAlarmLowLimitClearThreshold_Object=MibTableColumn
gponOltPonPortTemperatureAlarmLowLimitClearThreshold=_GponOltPonPortTemperatureAlarmLowLimitClearThreshold_Object((1,3,6,1,4,1,3320,10,2,4,1,13),_GponOltPonPortTemperatureAlarmLowLimitClearThreshold_Type())
gponOltPonPortTemperatureAlarmLowLimitClearThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortTemperatureAlarmLowLimitClearThreshold.setStatus(_A)
class _GponOltPonPortVoltageAlarmUpLimitEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_GponOltPonPortVoltageAlarmUpLimitEnable_Type.__name__=_D
_GponOltPonPortVoltageAlarmUpLimitEnable_Object=MibTableColumn
gponOltPonPortVoltageAlarmUpLimitEnable=_GponOltPonPortVoltageAlarmUpLimitEnable_Object((1,3,6,1,4,1,3320,10,2,4,1,14),_GponOltPonPortVoltageAlarmUpLimitEnable_Type())
gponOltPonPortVoltageAlarmUpLimitEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortVoltageAlarmUpLimitEnable.setStatus(_A)
_GponOltPonPortVoltageAlarmUpLimitThreshold_Type=Integer32
_GponOltPonPortVoltageAlarmUpLimitThreshold_Object=MibTableColumn
gponOltPonPortVoltageAlarmUpLimitThreshold=_GponOltPonPortVoltageAlarmUpLimitThreshold_Object((1,3,6,1,4,1,3320,10,2,4,1,15),_GponOltPonPortVoltageAlarmUpLimitThreshold_Type())
gponOltPonPortVoltageAlarmUpLimitThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortVoltageAlarmUpLimitThreshold.setStatus(_A)
_GponOltPonPortVoltageAlarmUpLimitClearThreshold_Type=Integer32
_GponOltPonPortVoltageAlarmUpLimitClearThreshold_Object=MibTableColumn
gponOltPonPortVoltageAlarmUpLimitClearThreshold=_GponOltPonPortVoltageAlarmUpLimitClearThreshold_Object((1,3,6,1,4,1,3320,10,2,4,1,16),_GponOltPonPortVoltageAlarmUpLimitClearThreshold_Type())
gponOltPonPortVoltageAlarmUpLimitClearThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortVoltageAlarmUpLimitClearThreshold.setStatus(_A)
class _GponOltPonPortVoltageAlarmLowLimitEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_GponOltPonPortVoltageAlarmLowLimitEnable_Type.__name__=_D
_GponOltPonPortVoltageAlarmLowLimitEnable_Object=MibTableColumn
gponOltPonPortVoltageAlarmLowLimitEnable=_GponOltPonPortVoltageAlarmLowLimitEnable_Object((1,3,6,1,4,1,3320,10,2,4,1,17),_GponOltPonPortVoltageAlarmLowLimitEnable_Type())
gponOltPonPortVoltageAlarmLowLimitEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortVoltageAlarmLowLimitEnable.setStatus(_A)
_GponOltPonPortVoltageAlarmLowLimitThreshold_Type=Integer32
_GponOltPonPortVoltageAlarmLowLimitThreshold_Object=MibTableColumn
gponOltPonPortVoltageAlarmLowLimitThreshold=_GponOltPonPortVoltageAlarmLowLimitThreshold_Object((1,3,6,1,4,1,3320,10,2,4,1,18),_GponOltPonPortVoltageAlarmLowLimitThreshold_Type())
gponOltPonPortVoltageAlarmLowLimitThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortVoltageAlarmLowLimitThreshold.setStatus(_A)
_GponOltPonPortVoltageAlarmLowLimitClearThreshold_Type=Integer32
_GponOltPonPortVoltageAlarmLowLimitClearThreshold_Object=MibTableColumn
gponOltPonPortVoltageAlarmLowLimitClearThreshold=_GponOltPonPortVoltageAlarmLowLimitClearThreshold_Object((1,3,6,1,4,1,3320,10,2,4,1,19),_GponOltPonPortVoltageAlarmLowLimitClearThreshold_Type())
gponOltPonPortVoltageAlarmLowLimitClearThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortVoltageAlarmLowLimitClearThreshold.setStatus(_A)
class _GponOltPonPortCurrentAlarmUpLimitEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_GponOltPonPortCurrentAlarmUpLimitEnable_Type.__name__=_D
_GponOltPonPortCurrentAlarmUpLimitEnable_Object=MibTableColumn
gponOltPonPortCurrentAlarmUpLimitEnable=_GponOltPonPortCurrentAlarmUpLimitEnable_Object((1,3,6,1,4,1,3320,10,2,4,1,20),_GponOltPonPortCurrentAlarmUpLimitEnable_Type())
gponOltPonPortCurrentAlarmUpLimitEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortCurrentAlarmUpLimitEnable.setStatus(_A)
_GponOltPonPortCurrentAlarmUpLimitThreshold_Type=Integer32
_GponOltPonPortCurrentAlarmUpLimitThreshold_Object=MibTableColumn
gponOltPonPortCurrentAlarmUpLimitThreshold=_GponOltPonPortCurrentAlarmUpLimitThreshold_Object((1,3,6,1,4,1,3320,10,2,4,1,21),_GponOltPonPortCurrentAlarmUpLimitThreshold_Type())
gponOltPonPortCurrentAlarmUpLimitThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortCurrentAlarmUpLimitThreshold.setStatus(_A)
_GponOltPonPortCurrentAlarmUpLimitClearThreshold_Type=Integer32
_GponOltPonPortCurrentAlarmUpLimitClearThreshold_Object=MibTableColumn
gponOltPonPortCurrentAlarmUpLimitClearThreshold=_GponOltPonPortCurrentAlarmUpLimitClearThreshold_Object((1,3,6,1,4,1,3320,10,2,4,1,22),_GponOltPonPortCurrentAlarmUpLimitClearThreshold_Type())
gponOltPonPortCurrentAlarmUpLimitClearThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortCurrentAlarmUpLimitClearThreshold.setStatus(_A)
class _GponOltPonPortCurrentAlarmLowLimitEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_GponOltPonPortCurrentAlarmLowLimitEnable_Type.__name__=_D
_GponOltPonPortCurrentAlarmLowLimitEnable_Object=MibTableColumn
gponOltPonPortCurrentAlarmLowLimitEnable=_GponOltPonPortCurrentAlarmLowLimitEnable_Object((1,3,6,1,4,1,3320,10,2,4,1,23),_GponOltPonPortCurrentAlarmLowLimitEnable_Type())
gponOltPonPortCurrentAlarmLowLimitEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortCurrentAlarmLowLimitEnable.setStatus(_A)
_GponOltPonPortCurrentAlarmLowLimitThreshold_Type=Integer32
_GponOltPonPortCurrentAlarmLowLimitThreshold_Object=MibTableColumn
gponOltPonPortCurrentAlarmLowLimitThreshold=_GponOltPonPortCurrentAlarmLowLimitThreshold_Object((1,3,6,1,4,1,3320,10,2,4,1,24),_GponOltPonPortCurrentAlarmLowLimitThreshold_Type())
gponOltPonPortCurrentAlarmLowLimitThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortCurrentAlarmLowLimitThreshold.setStatus(_A)
_GponOltPonPortCurrentAlarmLowLimitClearThreshold_Type=Integer32
_GponOltPonPortCurrentAlarmLowLimitClearThreshold_Object=MibTableColumn
gponOltPonPortCurrentAlarmLowLimitClearThreshold=_GponOltPonPortCurrentAlarmLowLimitClearThreshold_Object((1,3,6,1,4,1,3320,10,2,4,1,25),_GponOltPonPortCurrentAlarmLowLimitClearThreshold_Type())
gponOltPonPortCurrentAlarmLowLimitClearThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonPortCurrentAlarmLowLimitClearThreshold.setStatus(_A)
_GponOltPonSfpParameterAlarmTrap_ObjectIdentity=ObjectIdentity
gponOltPonSfpParameterAlarmTrap=_GponOltPonSfpParameterAlarmTrap_ObjectIdentity((1,3,6,1,4,1,3320,10,2,5))
class _GponOltPonSfpParameterAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('above',1),('below',2),(_X,3)))
_GponOltPonSfpParameterAlarmStatus_Type.__name__=_D
_GponOltPonSfpParameterAlarmStatus_Object=MibScalar
gponOltPonSfpParameterAlarmStatus=_GponOltPonSfpParameterAlarmStatus_Object((1,3,6,1,4,1,3320,10,2,5,1),_GponOltPonSfpParameterAlarmStatus_Type())
gponOltPonSfpParameterAlarmStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltPonSfpParameterAlarmStatus.setStatus(_A)
_GponOltONUBindTable_Object=MibTable
gponOltONUBindTable=_GponOltONUBindTable_Object((1,3,6,1,4,1,3320,10,2,6))
if mibBuilder.loadTexts:gponOltONUBindTable.setStatus(_A)
_GponOltONUBindEntry_Object=MibTableRow
gponOltONUBindEntry=_GponOltONUBindEntry_Object((1,3,6,1,4,1,3320,10,2,6,1))
gponOltONUBindEntry.setIndexNames((0,_E,_Y))
if mibBuilder.loadTexts:gponOltONUBindEntry.setStatus(_A)
_GponOltONUBindPortIndex_Type=Integer32
_GponOltONUBindPortIndex_Object=MibTableColumn
gponOltONUBindPortIndex=_GponOltONUBindPortIndex_Object((1,3,6,1,4,1,3320,10,2,6,1,1),_GponOltONUBindPortIndex_Type())
gponOltONUBindPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOltONUBindPortIndex.setStatus(_A)
class _GponOltONUBindONUId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_GponOltONUBindONUId_Type.__name__=_D
_GponOltONUBindONUId_Object=MibTableColumn
gponOltONUBindONUId=_GponOltONUBindONUId_Object((1,3,6,1,4,1,3320,10,2,6,1,2),_GponOltONUBindONUId_Type())
gponOltONUBindONUId.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltONUBindONUId.setStatus(_A)
_GponOltONUBindSN_Type=OctetString
_GponOltONUBindSN_Object=MibTableColumn
gponOltONUBindSN=_GponOltONUBindSN_Object((1,3,6,1,4,1,3320,10,2,6,1,3),_GponOltONUBindSN_Type())
gponOltONUBindSN.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltONUBindSN.setStatus(_A)
_GponOltONUBindPassword_Type=OctetString
_GponOltONUBindPassword_Object=MibTableColumn
gponOltONUBindPassword=_GponOltONUBindPassword_Object((1,3,6,1,4,1,3320,10,2,6,1,4),_GponOltONUBindPassword_Type())
gponOltONUBindPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOltONUBindPassword.setStatus(_A)
_GponOltONUBindRowStatus_Type=RowStatus
_GponOltONUBindRowStatus_Object=MibTableColumn
gponOltONUBindRowStatus=_GponOltONUBindRowStatus_Object((1,3,6,1,4,1,3320,10,2,6,1,5),_GponOltONUBindRowStatus_Type())
gponOltONUBindRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:gponOltONUBindRowStatus.setStatus(_A)
_NmsGponONUObj_ObjectIdentity=ObjectIdentity
nmsGponONUObj=_NmsGponONUObj_ObjectIdentity((1,3,6,1,4,1,3320,10,3))
_GponOnuInfoTable_Object=MibTable
gponOnuInfoTable=_GponOnuInfoTable_Object((1,3,6,1,4,1,3320,10,3,1))
if mibBuilder.loadTexts:gponOnuInfoTable.setStatus(_A)
_GponOnuInfoEntry_Object=MibTableRow
gponOnuInfoEntry=_GponOnuInfoEntry_Object((1,3,6,1,4,1,3320,10,3,1,1))
gponOnuInfoEntry.setIndexNames((0,_E,_Z))
if mibBuilder.loadTexts:gponOnuInfoEntry.setStatus(_A)
_GponONUInfoDeviceIndex_Type=Integer32
_GponONUInfoDeviceIndex_Object=MibTableColumn
gponONUInfoDeviceIndex=_GponONUInfoDeviceIndex_Object((1,3,6,1,4,1,3320,10,3,1,1,1),_GponONUInfoDeviceIndex_Type())
gponONUInfoDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:gponONUInfoDeviceIndex.setStatus(_A)
_OnuVendorID_Type=OctetString
_OnuVendorID_Object=MibTableColumn
onuVendorID=_OnuVendorID_Object((1,3,6,1,4,1,3320,10,3,1,1,2),_OnuVendorID_Type())
onuVendorID.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVendorID.setStatus(_A)
_OnuVersion_Type=OctetString
_OnuVersion_Object=MibTableColumn
onuVersion=_OnuVersion_Object((1,3,6,1,4,1,3320,10,3,1,1,3),_OnuVersion_Type())
onuVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVersion.setStatus(_A)
_OnuSerialNum_Type=OctetString
_OnuSerialNum_Object=MibTableColumn
onuSerialNum=_OnuSerialNum_Object((1,3,6,1,4,1,3320,10,3,1,1,4),_OnuSerialNum_Type())
onuSerialNum.setMaxAccess(_B)
if mibBuilder.loadTexts:onuSerialNum.setStatus(_A)
class _OnuTrafficManagementOption_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_a,0),('rate-controlled',1),('priority-and-rate-controlled',2)))
_OnuTrafficManagementOption_Type.__name__=_D
_OnuTrafficManagementOption_Object=MibTableColumn
onuTrafficManagementOption=_OnuTrafficManagementOption_Object((1,3,6,1,4,1,3320,10,3,1,1,5),_OnuTrafficManagementOption_Type())
onuTrafficManagementOption.setMaxAccess(_B)
if mibBuilder.loadTexts:onuTrafficManagementOption.setStatus(_A)
class _OnuBatteryBackup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_OnuBatteryBackup_Type.__name__=_D
_OnuBatteryBackup_Object=MibTableColumn
onuBatteryBackup=_OnuBatteryBackup_Object((1,3,6,1,4,1,3320,10,3,1,1,6),_OnuBatteryBackup_Type())
onuBatteryBackup.setMaxAccess(_C)
if mibBuilder.loadTexts:onuBatteryBackup.setStatus(_A)
class _OnuAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noshutdown-unlocks',1),(_b,2)))
_OnuAdminState_Type.__name__=_D
_OnuAdminState_Object=MibTableColumn
onuAdminState=_OnuAdminState_Object((1,3,6,1,4,1,3320,10,3,1,1,7),_OnuAdminState_Type())
onuAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:onuAdminState.setStatus(_A)
class _OnuOperationalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_OnuOperationalState_Type.__name__=_D
_OnuOperationalState_Object=MibTableColumn
onuOperationalState=_OnuOperationalState_Object((1,3,6,1,4,1,3320,10,3,1,1,8),_OnuOperationalState_Type())
onuOperationalState.setMaxAccess(_B)
if mibBuilder.loadTexts:onuOperationalState.setStatus(_A)
_OnuEquipmentID_Type=OctetString
_OnuEquipmentID_Object=MibTableColumn
onuEquipmentID=_OnuEquipmentID_Object((1,3,6,1,4,1,3320,10,3,1,1,9),_OnuEquipmentID_Type())
onuEquipmentID.setMaxAccess(_B)
if mibBuilder.loadTexts:onuEquipmentID.setStatus(_A)
_OnuOMCCVersion_Type=Integer32
_OnuOMCCVersion_Object=MibTableColumn
onuOMCCVersion=_OnuOMCCVersion_Object((1,3,6,1,4,1,3320,10,3,1,1,10),_OnuOMCCVersion_Type())
onuOMCCVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:onuOMCCVersion.setStatus(_A)
_OnuHardwareType_Type=Integer32
_OnuHardwareType_Object=MibTableColumn
onuHardwareType=_OnuHardwareType_Object((1,3,6,1,4,1,3320,10,3,1,1,11),_OnuHardwareType_Type())
onuHardwareType.setMaxAccess(_B)
if mibBuilder.loadTexts:onuHardwareType.setStatus(_A)
_OnuHardwareRevision_Type=Integer32
_OnuHardwareRevision_Object=MibTableColumn
onuHardwareRevision=_OnuHardwareRevision_Object((1,3,6,1,4,1,3320,10,3,1,1,12),_OnuHardwareRevision_Type())
onuHardwareRevision.setMaxAccess(_B)
if mibBuilder.loadTexts:onuHardwareRevision.setStatus(_A)
_OnuSecurityCapability_Type=Integer32
_OnuSecurityCapability_Object=MibTableColumn
onuSecurityCapability=_OnuSecurityCapability_Object((1,3,6,1,4,1,3320,10,3,1,1,13),_OnuSecurityCapability_Type())
onuSecurityCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:onuSecurityCapability.setStatus(_A)
class _OnuSecurityMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OnuSecurityMode_Type.__name__=_D
_OnuSecurityMode_Object=MibTableColumn
onuSecurityMode=_OnuSecurityMode_Object((1,3,6,1,4,1,3320,10,3,1,1,14),_OnuSecurityMode_Type())
onuSecurityMode.setMaxAccess(_C)
if mibBuilder.loadTexts:onuSecurityMode.setStatus(_A)
_OnuTotalPriorityQueueNumber_Type=Integer32
_OnuTotalPriorityQueueNumber_Object=MibTableColumn
onuTotalPriorityQueueNumber=_OnuTotalPriorityQueueNumber_Object((1,3,6,1,4,1,3320,10,3,1,1,15),_OnuTotalPriorityQueueNumber_Type())
onuTotalPriorityQueueNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:onuTotalPriorityQueueNumber.setStatus(_A)
_OnuTotalTrafficSchedulerNumber_Type=Integer32
_OnuTotalTrafficSchedulerNumber_Object=MibTableColumn
onuTotalTrafficSchedulerNumber=_OnuTotalTrafficSchedulerNumber_Object((1,3,6,1,4,1,3320,10,3,1,1,16),_OnuTotalTrafficSchedulerNumber_Type())
onuTotalTrafficSchedulerNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:onuTotalTrafficSchedulerNumber.setStatus(_A)
_OnuTotalGEMPortNumber_Type=Integer32
_OnuTotalGEMPortNumber_Object=MibTableColumn
onuTotalGEMPortNumber=_OnuTotalGEMPortNumber_Object((1,3,6,1,4,1,3320,10,3,1,1,17),_OnuTotalGEMPortNumber_Type())
onuTotalGEMPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:onuTotalGEMPortNumber.setStatus(_A)
_OnuTotalPOTSUNInumber_Type=Integer32
_OnuTotalPOTSUNInumber_Object=MibTableColumn
onuTotalPOTSUNInumber=_OnuTotalPOTSUNInumber_Object((1,3,6,1,4,1,3320,10,3,1,1,18),_OnuTotalPOTSUNInumber_Type())
onuTotalPOTSUNInumber.setMaxAccess(_B)
if mibBuilder.loadTexts:onuTotalPOTSUNInumber.setStatus(_A)
_OnuSysUpTime_Type=Integer32
_OnuSysUpTime_Object=MibTableColumn
onuSysUpTime=_OnuSysUpTime_Object((1,3,6,1,4,1,3320,10,3,1,1,19),_OnuSysUpTime_Type())
onuSysUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:onuSysUpTime.setStatus(_A)
_OnuImageInstance0Version_Type=OctetString
_OnuImageInstance0Version_Object=MibTableColumn
onuImageInstance0Version=_OnuImageInstance0Version_Object((1,3,6,1,4,1,3320,10,3,1,1,20),_OnuImageInstance0Version_Type())
onuImageInstance0Version.setMaxAccess(_B)
if mibBuilder.loadTexts:onuImageInstance0Version.setStatus(_A)
class _OnuImageInstance0Valid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_OnuImageInstance0Valid_Type.__name__=_D
_OnuImageInstance0Valid_Object=MibTableColumn
onuImageInstance0Valid=_OnuImageInstance0Valid_Object((1,3,6,1,4,1,3320,10,3,1,1,21),_OnuImageInstance0Valid_Type())
onuImageInstance0Valid.setMaxAccess(_B)
if mibBuilder.loadTexts:onuImageInstance0Valid.setStatus(_A)
class _OnuImageInstance0Activate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_OnuImageInstance0Activate_Type.__name__=_D
_OnuImageInstance0Activate_Object=MibTableColumn
onuImageInstance0Activate=_OnuImageInstance0Activate_Object((1,3,6,1,4,1,3320,10,3,1,1,22),_OnuImageInstance0Activate_Type())
onuImageInstance0Activate.setMaxAccess(_B)
if mibBuilder.loadTexts:onuImageInstance0Activate.setStatus(_A)
class _OnuImageInstance0Commit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_OnuImageInstance0Commit_Type.__name__=_D
_OnuImageInstance0Commit_Object=MibTableColumn
onuImageInstance0Commit=_OnuImageInstance0Commit_Object((1,3,6,1,4,1,3320,10,3,1,1,23),_OnuImageInstance0Commit_Type())
onuImageInstance0Commit.setMaxAccess(_B)
if mibBuilder.loadTexts:onuImageInstance0Commit.setStatus(_A)
_OnuImageInstance1Version_Type=OctetString
_OnuImageInstance1Version_Object=MibTableColumn
onuImageInstance1Version=_OnuImageInstance1Version_Object((1,3,6,1,4,1,3320,10,3,1,1,24),_OnuImageInstance1Version_Type())
onuImageInstance1Version.setMaxAccess(_B)
if mibBuilder.loadTexts:onuImageInstance1Version.setStatus(_A)
class _OnuImageInstance1Valid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_OnuImageInstance1Valid_Type.__name__=_D
_OnuImageInstance1Valid_Object=MibTableColumn
onuImageInstance1Valid=_OnuImageInstance1Valid_Object((1,3,6,1,4,1,3320,10,3,1,1,25),_OnuImageInstance1Valid_Type())
onuImageInstance1Valid.setMaxAccess(_B)
if mibBuilder.loadTexts:onuImageInstance1Valid.setStatus(_A)
class _OnuImageInstance1Activate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_OnuImageInstance1Activate_Type.__name__=_D
_OnuImageInstance1Activate_Object=MibTableColumn
onuImageInstance1Activate=_OnuImageInstance1Activate_Object((1,3,6,1,4,1,3320,10,3,1,1,26),_OnuImageInstance1Activate_Type())
onuImageInstance1Activate.setMaxAccess(_B)
if mibBuilder.loadTexts:onuImageInstance1Activate.setStatus(_A)
class _OnuImageInstance1Commit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_OnuImageInstance1Commit_Type.__name__=_D
_OnuImageInstance1Commit_Object=MibTableColumn
onuImageInstance1Commit=_OnuImageInstance1Commit_Object((1,3,6,1,4,1,3320,10,3,1,1,27),_OnuImageInstance1Commit_Type())
onuImageInstance1Commit.setMaxAccess(_B)
if mibBuilder.loadTexts:onuImageInstance1Commit.setStatus(_A)
_OnuInfoOonuMacAddress_Type=PhysAddress
_OnuInfoOonuMacAddress_Object=MibTableColumn
onuInfoOonuMacAddress=_OnuInfoOonuMacAddress_Object((1,3,6,1,4,1,3320,10,3,1,1,28),_OnuInfoOonuMacAddress_Type())
onuInfoOonuMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:onuInfoOonuMacAddress.setStatus(_A)
_OnuFastLeaveCapability_Type=Integer32
_OnuFastLeaveCapability_Object=MibTableColumn
onuFastLeaveCapability=_OnuFastLeaveCapability_Object((1,3,6,1,4,1,3320,10,3,1,1,29),_OnuFastLeaveCapability_Type())
onuFastLeaveCapability.setMaxAccess(_B)
if mibBuilder.loadTexts:onuFastLeaveCapability.setStatus(_A)
_OnuPiggybackDbaRep_Type=Integer32
_OnuPiggybackDbaRep_Object=MibTableColumn
onuPiggybackDbaRep=_OnuPiggybackDbaRep_Object((1,3,6,1,4,1,3320,10,3,1,1,30),_OnuPiggybackDbaRep_Type())
onuPiggybackDbaRep.setMaxAccess(_B)
if mibBuilder.loadTexts:onuPiggybackDbaRep.setStatus(_A)
_OnuWholeOnuDbaRep_Type=Integer32
_OnuWholeOnuDbaRep_Object=MibTableColumn
onuWholeOnuDbaRep=_OnuWholeOnuDbaRep_Object((1,3,6,1,4,1,3320,10,3,1,1,31),_OnuWholeOnuDbaRep_Type())
onuWholeOnuDbaRep.setMaxAccess(_B)
if mibBuilder.loadTexts:onuWholeOnuDbaRep.setStatus(_A)
class _OnuProtectionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('type-b-scheme',1),('type-c-scheme',2)))
_OnuProtectionMode_Type.__name__=_D
_OnuProtectionMode_Object=MibTableColumn
onuProtectionMode=_OnuProtectionMode_Object((1,3,6,1,4,1,3320,10,3,1,1,32),_OnuProtectionMode_Type())
onuProtectionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:onuProtectionMode.setStatus(_A)
_OnuDistance_Type=Integer32
_OnuDistance_Object=MibTableColumn
onuDistance=_OnuDistance_Object((1,3,6,1,4,1,3320,10,3,1,1,33),_OnuDistance_Type())
onuDistance.setMaxAccess(_B)
if mibBuilder.loadTexts:onuDistance.setStatus(_A)
_OnuSwdlState_Type=Integer32
_OnuSwdlState_Object=MibTableColumn
onuSwdlState=_OnuSwdlState_Object((1,3,6,1,4,1,3320,10,3,1,1,34),_OnuSwdlState_Type())
onuSwdlState.setMaxAccess(_B)
if mibBuilder.loadTexts:onuSwdlState.setStatus(_A)
class _OnuDeActiveReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('none',0),('dying-gasp',1),('laser-always-on',2),('admin-down',3),('omcc-down',4),('unknown',5),('pon-los',6),('lcdg',7),('wire-down',8),('omci-mismatch',9),('password-mismatch',10),(_c,11),('ranging-failed',12)))
_OnuDeActiveReason_Type.__name__=_D
_OnuDeActiveReason_Object=MibTableColumn
onuDeActiveReason=_OnuDeActiveReason_Object((1,3,6,1,4,1,3320,10,3,1,1,35),_OnuDeActiveReason_Type())
onuDeActiveReason.setMaxAccess(_B)
if mibBuilder.loadTexts:onuDeActiveReason.setStatus(_A)
_GponOnuConfigTable_Object=MibTable
gponOnuConfigTable=_GponOnuConfigTable_Object((1,3,6,1,4,1,3320,10,3,2))
if mibBuilder.loadTexts:gponOnuConfigTable.setStatus(_A)
_GponOnuConfigEntry_Object=MibTableRow
gponOnuConfigEntry=_GponOnuConfigEntry_Object((1,3,6,1,4,1,3320,10,3,2,1))
gponOnuConfigEntry.setIndexNames((0,_E,_d))
if mibBuilder.loadTexts:gponOnuConfigEntry.setStatus(_A)
_GponOnuConfigDeviceIndex_Type=Integer32
_GponOnuConfigDeviceIndex_Object=MibTableColumn
gponOnuConfigDeviceIndex=_GponOnuConfigDeviceIndex_Object((1,3,6,1,4,1,3320,10,3,2,1,1),_GponOnuConfigDeviceIndex_Type())
gponOnuConfigDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOnuConfigDeviceIndex.setStatus(_A)
class _GponOnuConfigActicate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('acticate',1),('deacticate',2)))
_GponOnuConfigActicate_Type.__name__=_D
_GponOnuConfigActicate_Object=MibTableColumn
gponOnuConfigActicate=_GponOnuConfigActicate_Object((1,3,6,1,4,1,3320,10,3,2,1,2),_GponOnuConfigActicate_Type())
gponOnuConfigActicate.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOnuConfigActicate.setStatus(_A)
class _GponOnuConfigEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_GponOnuConfigEnable_Type.__name__=_D
_GponOnuConfigEnable_Object=MibTableColumn
gponOnuConfigEnable=_GponOnuConfigEnable_Object((1,3,6,1,4,1,3320,10,3,2,1,3),_GponOnuConfigEnable_Type())
gponOnuConfigEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOnuConfigEnable.setStatus(_A)
class _GponOnuConfigReboot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues((_c,1))
_GponOnuConfigReboot_Type.__name__=_D
_GponOnuConfigReboot_Object=MibTableColumn
gponOnuConfigReboot=_GponOnuConfigReboot_Object((1,3,6,1,4,1,3320,10,3,2,1,4),_GponOnuConfigReboot_Type())
gponOnuConfigReboot.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOnuConfigReboot.setStatus(_A)
class _GponOnuConfigEnablePM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_GponOnuConfigEnablePM_Type.__name__=_D
_GponOnuConfigEnablePM_Object=MibTableColumn
gponOnuConfigEnablePM=_GponOnuConfigEnablePM_Object((1,3,6,1,4,1,3320,10,3,2,1,5),_GponOnuConfigEnablePM_Type())
gponOnuConfigEnablePM.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOnuConfigEnablePM.setStatus(_A)
_GponOnuConfigFlowProfileID_Type=Integer32
_GponOnuConfigFlowProfileID_Object=MibTableColumn
gponOnuConfigFlowProfileID=_GponOnuConfigFlowProfileID_Object((1,3,6,1,4,1,3320,10,3,2,1,6),_GponOnuConfigFlowProfileID_Type())
gponOnuConfigFlowProfileID.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOnuConfigFlowProfileID.setStatus(_A)
_GponOnuConfigTcontVirPortBindingProfileID_Type=Integer32
_GponOnuConfigTcontVirPortBindingProfileID_Object=MibTableColumn
gponOnuConfigTcontVirPortBindingProfileID=_GponOnuConfigTcontVirPortBindingProfileID_Object((1,3,6,1,4,1,3320,10,3,2,1,7),_GponOnuConfigTcontVirPortBindingProfileID_Type())
gponOnuConfigTcontVirPortBindingProfileID.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOnuConfigTcontVirPortBindingProfileID.setStatus(_A)
_GponOnuConfigOnuProfileID_Type=Integer32
_GponOnuConfigOnuProfileID_Object=MibTableColumn
gponOnuConfigOnuProfileID=_GponOnuConfigOnuProfileID_Object((1,3,6,1,4,1,3320,10,3,2,1,8),_GponOnuConfigOnuProfileID_Type())
gponOnuConfigOnuProfileID.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOnuConfigOnuProfileID.setStatus(_A)
_GponOnuConfigUsMapProfileID_Type=Integer32
_GponOnuConfigUsMapProfileID_Object=MibTableColumn
gponOnuConfigUsMapProfileID=_GponOnuConfigUsMapProfileID_Object((1,3,6,1,4,1,3320,10,3,2,1,9),_GponOnuConfigUsMapProfileID_Type())
gponOnuConfigUsMapProfileID.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOnuConfigUsMapProfileID.setStatus(_A)
_GponOnuStatusTable_Object=MibTable
gponOnuStatusTable=_GponOnuStatusTable_Object((1,3,6,1,4,1,3320,10,3,3))
if mibBuilder.loadTexts:gponOnuStatusTable.setStatus(_A)
_GponOnuStatusEntry_Object=MibTableRow
gponOnuStatusEntry=_GponOnuStatusEntry_Object((1,3,6,1,4,1,3320,10,3,3,1))
gponOnuStatusEntry.setIndexNames((0,_E,_e))
if mibBuilder.loadTexts:gponOnuStatusEntry.setStatus(_A)
_GponOnuStatusDeviceIndex_Type=Integer32
_GponOnuStatusDeviceIndex_Object=MibTableColumn
gponOnuStatusDeviceIndex=_GponOnuStatusDeviceIndex_Object((1,3,6,1,4,1,3320,10,3,3,1,1),_GponOnuStatusDeviceIndex_Type())
gponOnuStatusDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOnuStatusDeviceIndex.setStatus(_A)
_GponOnuStatusOnuSn_Type=OctetString
_GponOnuStatusOnuSn_Object=MibTableColumn
gponOnuStatusOnuSn=_GponOnuStatusOnuSn_Object((1,3,6,1,4,1,3320,10,3,3,1,2),_GponOnuStatusOnuSn_Type())
gponOnuStatusOnuSn.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOnuStatusOnuSn.setStatus(_A)
_GponOnuStatusPonPortID_Type=Integer32
_GponOnuStatusPonPortID_Object=MibTableColumn
gponOnuStatusPonPortID=_GponOnuStatusPonPortID_Object((1,3,6,1,4,1,3320,10,3,3,1,3),_GponOnuStatusPonPortID_Type())
gponOnuStatusPonPortID.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOnuStatusPonPortID.setStatus(_A)
class _GponOnuStatusOnuStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('off-line',0),('inactive',1),(_F,2),('active',3)))
_GponOnuStatusOnuStatus_Type.__name__=_D
_GponOnuStatusOnuStatus_Object=MibTableColumn
gponOnuStatusOnuStatus=_GponOnuStatusOnuStatus_Object((1,3,6,1,4,1,3320,10,3,3,1,4),_GponOnuStatusOnuStatus_Type())
gponOnuStatusOnuStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOnuStatusOnuStatus.setStatus(_A)
_GponOnuOpticalPowerTable_Object=MibTable
gponOnuOpticalPowerTable=_GponOnuOpticalPowerTable_Object((1,3,6,1,4,1,3320,10,3,4))
if mibBuilder.loadTexts:gponOnuOpticalPowerTable.setStatus(_A)
_GponOnuOpticalPowerEntry_Object=MibTableRow
gponOnuOpticalPowerEntry=_GponOnuOpticalPowerEntry_Object((1,3,6,1,4,1,3320,10,3,4,1))
gponOnuOpticalPowerEntry.setIndexNames((0,_E,_f))
if mibBuilder.loadTexts:gponOnuOpticalPowerEntry.setStatus(_A)
_GponOnuOpticalPowerDeviceIndex_Type=Integer32
_GponOnuOpticalPowerDeviceIndex_Object=MibTableColumn
gponOnuOpticalPowerDeviceIndex=_GponOnuOpticalPowerDeviceIndex_Object((1,3,6,1,4,1,3320,10,3,4,1,1),_GponOnuOpticalPowerDeviceIndex_Type())
gponOnuOpticalPowerDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOnuOpticalPowerDeviceIndex.setStatus(_A)
_GponOnuOpticalPowerRxPower_Type=Integer32
_GponOnuOpticalPowerRxPower_Object=MibTableColumn
gponOnuOpticalPowerRxPower=_GponOnuOpticalPowerRxPower_Object((1,3,6,1,4,1,3320,10,3,4,1,2),_GponOnuOpticalPowerRxPower_Type())
gponOnuOpticalPowerRxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOnuOpticalPowerRxPower.setStatus(_A)
_GponOnuOpticalPowerTxPower_Type=Integer32
_GponOnuOpticalPowerTxPower_Object=MibTableColumn
gponOnuOpticalPowerTxPower=_GponOnuOpticalPowerTxPower_Object((1,3,6,1,4,1,3320,10,3,4,1,3),_GponOnuOpticalPowerTxPower_Type())
gponOnuOpticalPowerTxPower.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOnuOpticalPowerTxPower.setStatus(_A)
_GponOnuOpticalParameterAlarmTable_Object=MibTable
gponOnuOpticalParameterAlarmTable=_GponOnuOpticalParameterAlarmTable_Object((1,3,6,1,4,1,3320,10,3,5))
if mibBuilder.loadTexts:gponOnuOpticalParameterAlarmTable.setStatus(_A)
_GponOnuOpticalParameterAlarmEntry_Object=MibTableRow
gponOnuOpticalParameterAlarmEntry=_GponOnuOpticalParameterAlarmEntry_Object((1,3,6,1,4,1,3320,10,3,5,1))
gponOnuOpticalParameterAlarmEntry.setIndexNames((0,_E,_g))
if mibBuilder.loadTexts:gponOnuOpticalParameterAlarmEntry.setStatus(_A)
_GponOnuOpticalParameterAlarmDeviceIndex_Type=Integer32
_GponOnuOpticalParameterAlarmDeviceIndex_Object=MibTableColumn
gponOnuOpticalParameterAlarmDeviceIndex=_GponOnuOpticalParameterAlarmDeviceIndex_Object((1,3,6,1,4,1,3320,10,3,5,1,1),_GponOnuOpticalParameterAlarmDeviceIndex_Type())
gponOnuOpticalParameterAlarmDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOnuOpticalParameterAlarmDeviceIndex.setStatus(_A)
class _GponOnuOpticalTxPowerAlarmUpLimitEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_GponOnuOpticalTxPowerAlarmUpLimitEnable_Type.__name__=_D
_GponOnuOpticalTxPowerAlarmUpLimitEnable_Object=MibTableColumn
gponOnuOpticalTxPowerAlarmUpLimitEnable=_GponOnuOpticalTxPowerAlarmUpLimitEnable_Object((1,3,6,1,4,1,3320,10,3,5,1,2),_GponOnuOpticalTxPowerAlarmUpLimitEnable_Type())
gponOnuOpticalTxPowerAlarmUpLimitEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOnuOpticalTxPowerAlarmUpLimitEnable.setStatus(_A)
_GponOnuOpticalTxPowerAlarmUpLimitThreshold_Type=Integer32
_GponOnuOpticalTxPowerAlarmUpLimitThreshold_Object=MibTableColumn
gponOnuOpticalTxPowerAlarmUpLimitThreshold=_GponOnuOpticalTxPowerAlarmUpLimitThreshold_Object((1,3,6,1,4,1,3320,10,3,5,1,3),_GponOnuOpticalTxPowerAlarmUpLimitThreshold_Type())
gponOnuOpticalTxPowerAlarmUpLimitThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOnuOpticalTxPowerAlarmUpLimitThreshold.setStatus(_A)
_GponOnuOpticalTxPowerAlarmUpLimitClearThreshold_Type=Integer32
_GponOnuOpticalTxPowerAlarmUpLimitClearThreshold_Object=MibTableColumn
gponOnuOpticalTxPowerAlarmUpLimitClearThreshold=_GponOnuOpticalTxPowerAlarmUpLimitClearThreshold_Object((1,3,6,1,4,1,3320,10,3,5,1,4),_GponOnuOpticalTxPowerAlarmUpLimitClearThreshold_Type())
gponOnuOpticalTxPowerAlarmUpLimitClearThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOnuOpticalTxPowerAlarmUpLimitClearThreshold.setStatus(_A)
_GponOnuOpticalTxPowerAlarmUpLimitRowStatus_Type=RowStatus
_GponOnuOpticalTxPowerAlarmUpLimitRowStatus_Object=MibTableColumn
gponOnuOpticalTxPowerAlarmUpLimitRowStatus=_GponOnuOpticalTxPowerAlarmUpLimitRowStatus_Object((1,3,6,1,4,1,3320,10,3,5,1,5),_GponOnuOpticalTxPowerAlarmUpLimitRowStatus_Type())
gponOnuOpticalTxPowerAlarmUpLimitRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOnuOpticalTxPowerAlarmUpLimitRowStatus.setStatus(_A)
class _GponOnuOpticalTxPowerAlarmLowLimitEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_GponOnuOpticalTxPowerAlarmLowLimitEnable_Type.__name__=_D
_GponOnuOpticalTxPowerAlarmLowLimitEnable_Object=MibTableColumn
gponOnuOpticalTxPowerAlarmLowLimitEnable=_GponOnuOpticalTxPowerAlarmLowLimitEnable_Object((1,3,6,1,4,1,3320,10,3,5,1,6),_GponOnuOpticalTxPowerAlarmLowLimitEnable_Type())
gponOnuOpticalTxPowerAlarmLowLimitEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOnuOpticalTxPowerAlarmLowLimitEnable.setStatus(_A)
_GponOnuOpticalTxPowerAlarmLowLimitThreshold_Type=Integer32
_GponOnuOpticalTxPowerAlarmLowLimitThreshold_Object=MibTableColumn
gponOnuOpticalTxPowerAlarmLowLimitThreshold=_GponOnuOpticalTxPowerAlarmLowLimitThreshold_Object((1,3,6,1,4,1,3320,10,3,5,1,7),_GponOnuOpticalTxPowerAlarmLowLimitThreshold_Type())
gponOnuOpticalTxPowerAlarmLowLimitThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOnuOpticalTxPowerAlarmLowLimitThreshold.setStatus(_A)
_GponOnuOpticalTxPowerAlarmLowLimitClearThreshold_Type=Integer32
_GponOnuOpticalTxPowerAlarmLowLimitClearThreshold_Object=MibTableColumn
gponOnuOpticalTxPowerAlarmLowLimitClearThreshold=_GponOnuOpticalTxPowerAlarmLowLimitClearThreshold_Object((1,3,6,1,4,1,3320,10,3,5,1,8),_GponOnuOpticalTxPowerAlarmLowLimitClearThreshold_Type())
gponOnuOpticalTxPowerAlarmLowLimitClearThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOnuOpticalTxPowerAlarmLowLimitClearThreshold.setStatus(_A)
_GponOnuOpticalTxPowerAlarmLowLimitRowStatus_Type=RowStatus
_GponOnuOpticalTxPowerAlarmLowLimitRowStatus_Object=MibTableColumn
gponOnuOpticalTxPowerAlarmLowLimitRowStatus=_GponOnuOpticalTxPowerAlarmLowLimitRowStatus_Object((1,3,6,1,4,1,3320,10,3,5,1,9),_GponOnuOpticalTxPowerAlarmLowLimitRowStatus_Type())
gponOnuOpticalTxPowerAlarmLowLimitRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOnuOpticalTxPowerAlarmLowLimitRowStatus.setStatus(_A)
class _GponOnuOpticalRxPowerAlarmUpLimitEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_GponOnuOpticalRxPowerAlarmUpLimitEnable_Type.__name__=_D
_GponOnuOpticalRxPowerAlarmUpLimitEnable_Object=MibTableColumn
gponOnuOpticalRxPowerAlarmUpLimitEnable=_GponOnuOpticalRxPowerAlarmUpLimitEnable_Object((1,3,6,1,4,1,3320,10,3,5,1,10),_GponOnuOpticalRxPowerAlarmUpLimitEnable_Type())
gponOnuOpticalRxPowerAlarmUpLimitEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOnuOpticalRxPowerAlarmUpLimitEnable.setStatus(_A)
_GponOnuOpticalRxPowerAlarmUpLimitThreshold_Type=Integer32
_GponOnuOpticalRxPowerAlarmUpLimitThreshold_Object=MibTableColumn
gponOnuOpticalRxPowerAlarmUpLimitThreshold=_GponOnuOpticalRxPowerAlarmUpLimitThreshold_Object((1,3,6,1,4,1,3320,10,3,5,1,11),_GponOnuOpticalRxPowerAlarmUpLimitThreshold_Type())
gponOnuOpticalRxPowerAlarmUpLimitThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOnuOpticalRxPowerAlarmUpLimitThreshold.setStatus(_A)
_GponOnuOpticalRxPowerAlarmUpLimitClearThreshold_Type=Integer32
_GponOnuOpticalRxPowerAlarmUpLimitClearThreshold_Object=MibTableColumn
gponOnuOpticalRxPowerAlarmUpLimitClearThreshold=_GponOnuOpticalRxPowerAlarmUpLimitClearThreshold_Object((1,3,6,1,4,1,3320,10,3,5,1,12),_GponOnuOpticalRxPowerAlarmUpLimitClearThreshold_Type())
gponOnuOpticalRxPowerAlarmUpLimitClearThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOnuOpticalRxPowerAlarmUpLimitClearThreshold.setStatus(_A)
_GponOnuOpticalRxPowerAlarmUpLimitRowStatus_Type=RowStatus
_GponOnuOpticalRxPowerAlarmUpLimitRowStatus_Object=MibTableColumn
gponOnuOpticalRxPowerAlarmUpLimitRowStatus=_GponOnuOpticalRxPowerAlarmUpLimitRowStatus_Object((1,3,6,1,4,1,3320,10,3,5,1,13),_GponOnuOpticalRxPowerAlarmUpLimitRowStatus_Type())
gponOnuOpticalRxPowerAlarmUpLimitRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOnuOpticalRxPowerAlarmUpLimitRowStatus.setStatus(_A)
class _GponOnuOpticalRxPowerAlarmLowLimitEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_GponOnuOpticalRxPowerAlarmLowLimitEnable_Type.__name__=_D
_GponOnuOpticalRxPowerAlarmLowLimitEnable_Object=MibTableColumn
gponOnuOpticalRxPowerAlarmLowLimitEnable=_GponOnuOpticalRxPowerAlarmLowLimitEnable_Object((1,3,6,1,4,1,3320,10,3,5,1,14),_GponOnuOpticalRxPowerAlarmLowLimitEnable_Type())
gponOnuOpticalRxPowerAlarmLowLimitEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOnuOpticalRxPowerAlarmLowLimitEnable.setStatus(_A)
_GponOnuOpticalRxPowerAlarmLowLimitThreshold_Type=Integer32
_GponOnuOpticalRxPowerAlarmLowLimitThreshold_Object=MibTableColumn
gponOnuOpticalRxPowerAlarmLowLimitThreshold=_GponOnuOpticalRxPowerAlarmLowLimitThreshold_Object((1,3,6,1,4,1,3320,10,3,5,1,15),_GponOnuOpticalRxPowerAlarmLowLimitThreshold_Type())
gponOnuOpticalRxPowerAlarmLowLimitThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOnuOpticalRxPowerAlarmLowLimitThreshold.setStatus(_A)
_GponOnuOpticalRxPowerAlarmLowLimitClearThreshold_Type=Integer32
_GponOnuOpticalRxPowerAlarmLowLimitClearThreshold_Object=MibTableColumn
gponOnuOpticalRxPowerAlarmLowLimitClearThreshold=_GponOnuOpticalRxPowerAlarmLowLimitClearThreshold_Object((1,3,6,1,4,1,3320,10,3,5,1,16),_GponOnuOpticalRxPowerAlarmLowLimitClearThreshold_Type())
gponOnuOpticalRxPowerAlarmLowLimitClearThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOnuOpticalRxPowerAlarmLowLimitClearThreshold.setStatus(_A)
_GponOnuOpticalRxPowerAlarmLowLimitRowStatus_Type=RowStatus
_GponOnuOpticalRxPowerAlarmLowLimitRowStatus_Object=MibTableColumn
gponOnuOpticalRxPowerAlarmLowLimitRowStatus=_GponOnuOpticalRxPowerAlarmLowLimitRowStatus_Object((1,3,6,1,4,1,3320,10,3,5,1,17),_GponOnuOpticalRxPowerAlarmLowLimitRowStatus_Type())
gponOnuOpticalRxPowerAlarmLowLimitRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:gponOnuOpticalRxPowerAlarmLowLimitRowStatus.setStatus(_A)
_GponOnuSfpParameterAlarmTrap_ObjectIdentity=ObjectIdentity
gponOnuSfpParameterAlarmTrap=_GponOnuSfpParameterAlarmTrap_ObjectIdentity((1,3,6,1,4,1,3320,10,3,6))
class _GponOnuSfpParameterAlarmStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('above',1),('below',2),(_X,3)))
_GponOnuSfpParameterAlarmStatus_Type.__name__=_D
_GponOnuSfpParameterAlarmStatus_Object=MibScalar
gponOnuSfpParameterAlarmStatus=_GponOnuSfpParameterAlarmStatus_Object((1,3,6,1,4,1,3320,10,3,6,1),_GponOnuSfpParameterAlarmStatus_Type())
gponOnuSfpParameterAlarmStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOnuSfpParameterAlarmStatus.setStatus(_A)
_GponOnuSfpParameterAlarmThreshold_Type=Integer32
_GponOnuSfpParameterAlarmThreshold_Object=MibScalar
gponOnuSfpParameterAlarmThreshold=_GponOnuSfpParameterAlarmThreshold_Object((1,3,6,1,4,1,3320,10,3,6,2),_GponOnuSfpParameterAlarmThreshold_Type())
gponOnuSfpParameterAlarmThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOnuSfpParameterAlarmThreshold.setStatus(_A)
_GponOnuStatusAlarmTrap_ObjectIdentity=ObjectIdentity
gponOnuStatusAlarmTrap=_GponOnuStatusAlarmTrap_ObjectIdentity((1,3,6,1,4,1,3320,10,3,7))
class _GponOnuStatusChange_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('discovered',1),('activated',2),('deactivated',3),('disable-complete',4),('enable-complete',5),('mib-ready',6),('mib-not-ready',7),('onu-los',8)))
_GponOnuStatusChange_Type.__name__=_D
_GponOnuStatusChange_Object=MibScalar
gponOnuStatusChange=_GponOnuStatusChange_Object((1,3,6,1,4,1,3320,10,3,7,1),_GponOnuStatusChange_Type())
gponOnuStatusChange.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOnuStatusChange.setStatus(_A)
_GponOnuDyingGaspAlarmTrap_ObjectIdentity=ObjectIdentity
gponOnuDyingGaspAlarmTrap=_GponOnuDyingGaspAlarmTrap_ObjectIdentity((1,3,6,1,4,1,3320,10,3,8))
class _GponOnuDyingGaspStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_GponOnuDyingGaspStatus_Type.__name__=_D
_GponOnuDyingGaspStatus_Object=MibScalar
gponOnuDyingGaspStatus=_GponOnuDyingGaspStatus_Object((1,3,6,1,4,1,3320,10,3,8,1),_GponOnuDyingGaspStatus_Type())
gponOnuDyingGaspStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:gponOnuDyingGaspStatus.setStatus(_A)
_GponOnuBatchUpdateTable_Object=MibTable
gponOnuBatchUpdateTable=_GponOnuBatchUpdateTable_Object((1,3,6,1,4,1,3320,10,3,9))
if mibBuilder.loadTexts:gponOnuBatchUpdateTable.setStatus(_A)
_GponOnuBatchUpdateEntry_Object=MibTableRow
gponOnuBatchUpdateEntry=_GponOnuBatchUpdateEntry_Object((1,3,6,1,4,1,3320,10,3,9,1))
gponOnuBatchUpdateEntry.setIndexNames((0,_E,_h))
if mibBuilder.loadTexts:gponOnuBatchUpdateEntry.setStatus(_A)
_GponOnuBatchUpdateLLIDs_Type=OctetString
_GponOnuBatchUpdateLLIDs_Object=MibTableColumn
gponOnuBatchUpdateLLIDs=_GponOnuBatchUpdateLLIDs_Object((1,3,6,1,4,1,3320,10,3,9,1,1),_GponOnuBatchUpdateLLIDs_Type())
gponOnuBatchUpdateLLIDs.setMaxAccess(_O)
if mibBuilder.loadTexts:gponOnuBatchUpdateLLIDs.setStatus(_A)
_GponOnuBatchUpdateFileName_Type=OctetString
_GponOnuBatchUpdateFileName_Object=MibTableColumn
gponOnuBatchUpdateFileName=_GponOnuBatchUpdateFileName_Object((1,3,6,1,4,1,3320,10,3,9,1,2),_GponOnuBatchUpdateFileName_Type())
gponOnuBatchUpdateFileName.setMaxAccess(_O)
if mibBuilder.loadTexts:gponOnuBatchUpdateFileName.setStatus(_A)
class _GponOnuBatchUpdateAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('no-action',0),('action',1),('action-for-actvie',2)))
_GponOnuBatchUpdateAction_Type.__name__=_D
_GponOnuBatchUpdateAction_Object=MibTableColumn
gponOnuBatchUpdateAction=_GponOnuBatchUpdateAction_Object((1,3,6,1,4,1,3320,10,3,9,1,3),_GponOnuBatchUpdateAction_Type())
gponOnuBatchUpdateAction.setMaxAccess(_O)
if mibBuilder.loadTexts:gponOnuBatchUpdateAction.setStatus(_A)
class _GponOnuBatchUpdateResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('success',0),('processing',1),('other',2)))
_GponOnuBatchUpdateResult_Type.__name__=_D
_GponOnuBatchUpdateResult_Object=MibTableColumn
gponOnuBatchUpdateResult=_GponOnuBatchUpdateResult_Object((1,3,6,1,4,1,3320,10,3,9,1,4),_GponOnuBatchUpdateResult_Type())
gponOnuBatchUpdateResult.setMaxAccess(_O)
if mibBuilder.loadTexts:gponOnuBatchUpdateResult.setStatus(_A)
_NmsGponUNIPortObj_ObjectIdentity=ObjectIdentity
nmsGponUNIPortObj=_NmsGponUNIPortObj_ObjectIdentity((1,3,6,1,4,1,3320,10,4))
_OnuUniPortConfigTable_Object=MibTable
onuUniPortConfigTable=_OnuUniPortConfigTable_Object((1,3,6,1,4,1,3320,10,4,1))
if mibBuilder.loadTexts:onuUniPortConfigTable.setStatus(_A)
_OnuUniPortConfigEntry_Object=MibTableRow
onuUniPortConfigEntry=_OnuUniPortConfigEntry_Object((1,3,6,1,4,1,3320,10,4,1,1))
onuUniPortConfigEntry.setIndexNames((0,_E,_i),(0,_E,_j))
if mibBuilder.loadTexts:onuUniPortConfigEntry.setStatus(_A)
_OnuUniPortConfigDeviceIndex_Type=Integer32
_OnuUniPortConfigDeviceIndex_Object=MibTableColumn
onuUniPortConfigDeviceIndex=_OnuUniPortConfigDeviceIndex_Object((1,3,6,1,4,1,3320,10,4,1,1,1),_OnuUniPortConfigDeviceIndex_Type())
onuUniPortConfigDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortConfigDeviceIndex.setStatus(_A)
_OnuUniPortConfigPortIndex_Type=Integer32
_OnuUniPortConfigPortIndex_Object=MibTableColumn
onuUniPortConfigPortIndex=_OnuUniPortConfigPortIndex_Object((1,3,6,1,4,1,3320,10,4,1,1,2),_OnuUniPortConfigPortIndex_Type())
onuUniPortConfigPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortConfigPortIndex.setStatus(_A)
class _OnuUniPortConfigAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_S,1),(_T,2)))
_OnuUniPortConfigAdminState_Type.__name__=_D
_OnuUniPortConfigAdminState_Object=MibTableColumn
onuUniPortConfigAdminState=_OnuUniPortConfigAdminState_Object((1,3,6,1,4,1,3320,10,4,1,1,3),_OnuUniPortConfigAdminState_Type())
onuUniPortConfigAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:onuUniPortConfigAdminState.setStatus(_A)
class _OnuUniPortConfigOperationalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_OnuUniPortConfigOperationalState_Type.__name__=_D
_OnuUniPortConfigOperationalState_Object=MibTableColumn
onuUniPortConfigOperationalState=_OnuUniPortConfigOperationalState_Object((1,3,6,1,4,1,3320,10,4,1,1,4),_OnuUniPortConfigOperationalState_Type())
onuUniPortConfigOperationalState.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortConfigOperationalState.setStatus(_A)
_OnuUniPortConfigEthernetProfileID_Type=Integer32
_OnuUniPortConfigEthernetProfileID_Object=MibTableColumn
onuUniPortConfigEthernetProfileID=_OnuUniPortConfigEthernetProfileID_Object((1,3,6,1,4,1,3320,10,4,1,1,5),_OnuUniPortConfigEthernetProfileID_Type())
onuUniPortConfigEthernetProfileID.setMaxAccess(_C)
if mibBuilder.loadTexts:onuUniPortConfigEthernetProfileID.setStatus(_A)
_OnuUniPortConfigOnuVLANTranslationProfileID_Type=Integer32
_OnuUniPortConfigOnuVLANTranslationProfileID_Object=MibTableColumn
onuUniPortConfigOnuVLANTranslationProfileID=_OnuUniPortConfigOnuVLANTranslationProfileID_Object((1,3,6,1,4,1,3320,10,4,1,1,6),_OnuUniPortConfigOnuVLANTranslationProfileID_Type())
onuUniPortConfigOnuVLANTranslationProfileID.setMaxAccess(_C)
if mibBuilder.loadTexts:onuUniPortConfigOnuVLANTranslationProfileID.setStatus(_A)
_OnuUniPortConfigRowStatus_Type=RowStatus
_OnuUniPortConfigRowStatus_Object=MibTableColumn
onuUniPortConfigRowStatus=_OnuUniPortConfigRowStatus_Object((1,3,6,1,4,1,3320,10,4,1,1,7),_OnuUniPortConfigRowStatus_Type())
onuUniPortConfigRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:onuUniPortConfigRowStatus.setStatus(_A)
_OnuUniPortStatisticTable_Object=MibTable
onuUniPortStatisticTable=_OnuUniPortStatisticTable_Object((1,3,6,1,4,1,3320,10,4,2))
if mibBuilder.loadTexts:onuUniPortStatisticTable.setStatus(_A)
_OnuUniPortStatisticEntry_Object=MibTableRow
onuUniPortStatisticEntry=_OnuUniPortStatisticEntry_Object((1,3,6,1,4,1,3320,10,4,2,1))
onuUniPortStatisticEntry.setIndexNames((0,_E,_k),(0,_E,_l))
if mibBuilder.loadTexts:onuUniPortStatisticEntry.setStatus(_A)
_OnuUniPortStatisticDeviceIndex_Type=Integer32
_OnuUniPortStatisticDeviceIndex_Object=MibTableColumn
onuUniPortStatisticDeviceIndex=_OnuUniPortStatisticDeviceIndex_Object((1,3,6,1,4,1,3320,10,4,2,1,1),_OnuUniPortStatisticDeviceIndex_Type())
onuUniPortStatisticDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticDeviceIndex.setStatus(_A)
_OnuUniPortStatisticUniPortIndex_Type=Integer32
_OnuUniPortStatisticUniPortIndex_Object=MibTableColumn
onuUniPortStatisticUniPortIndex=_OnuUniPortStatisticUniPortIndex_Object((1,3,6,1,4,1,3320,10,4,2,1,2),_OnuUniPortStatisticUniPortIndex_Type())
onuUniPortStatisticUniPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticUniPortIndex.setStatus(_A)
_OnuUniPortStatisticTime_Type=Counter64
_OnuUniPortStatisticTime_Object=MibTableColumn
onuUniPortStatisticTime=_OnuUniPortStatisticTime_Object((1,3,6,1,4,1,3320,10,4,2,1,3),_OnuUniPortStatisticTime_Type())
onuUniPortStatisticTime.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticTime.setStatus(_A)
_OnuUniPortStatisticRxTotalPackets_Type=Counter64
_OnuUniPortStatisticRxTotalPackets_Object=MibTableColumn
onuUniPortStatisticRxTotalPackets=_OnuUniPortStatisticRxTotalPackets_Object((1,3,6,1,4,1,3320,10,4,2,1,4),_OnuUniPortStatisticRxTotalPackets_Type())
onuUniPortStatisticRxTotalPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticRxTotalPackets.setStatus(_A)
_OnuUniPortStatisticRxUnicastPackets_Type=Counter64
_OnuUniPortStatisticRxUnicastPackets_Object=MibTableColumn
onuUniPortStatisticRxUnicastPackets=_OnuUniPortStatisticRxUnicastPackets_Object((1,3,6,1,4,1,3320,10,4,2,1,5),_OnuUniPortStatisticRxUnicastPackets_Type())
onuUniPortStatisticRxUnicastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticRxUnicastPackets.setStatus(_A)
_OnuUniPortStatisticRxMulticastPackets_Type=Counter64
_OnuUniPortStatisticRxMulticastPackets_Object=MibTableColumn
onuUniPortStatisticRxMulticastPackets=_OnuUniPortStatisticRxMulticastPackets_Object((1,3,6,1,4,1,3320,10,4,2,1,6),_OnuUniPortStatisticRxMulticastPackets_Type())
onuUniPortStatisticRxMulticastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticRxMulticastPackets.setStatus(_A)
_OnuUniPortStatisticRxBroadcastPackets_Type=Counter64
_OnuUniPortStatisticRxBroadcastPackets_Object=MibTableColumn
onuUniPortStatisticRxBroadcastPackets=_OnuUniPortStatisticRxBroadcastPackets_Object((1,3,6,1,4,1,3320,10,4,2,1,7),_OnuUniPortStatisticRxBroadcastPackets_Type())
onuUniPortStatisticRxBroadcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticRxBroadcastPackets.setStatus(_A)
_OnuUniPortStatisticRxDiscardedPackets_Type=Counter64
_OnuUniPortStatisticRxDiscardedPackets_Object=MibTableColumn
onuUniPortStatisticRxDiscardedPackets=_OnuUniPortStatisticRxDiscardedPackets_Object((1,3,6,1,4,1,3320,10,4,2,1,8),_OnuUniPortStatisticRxDiscardedPackets_Type())
onuUniPortStatisticRxDiscardedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticRxDiscardedPackets.setStatus(_A)
_OnuUniPortStatisticTxTotalPackets_Type=Counter64
_OnuUniPortStatisticTxTotalPackets_Object=MibTableColumn
onuUniPortStatisticTxTotalPackets=_OnuUniPortStatisticTxTotalPackets_Object((1,3,6,1,4,1,3320,10,4,2,1,9),_OnuUniPortStatisticTxTotalPackets_Type())
onuUniPortStatisticTxTotalPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticTxTotalPackets.setStatus(_A)
_OnuUniPortStatisticTxUnicastPackets_Type=Counter64
_OnuUniPortStatisticTxUnicastPackets_Object=MibTableColumn
onuUniPortStatisticTxUnicastPackets=_OnuUniPortStatisticTxUnicastPackets_Object((1,3,6,1,4,1,3320,10,4,2,1,10),_OnuUniPortStatisticTxUnicastPackets_Type())
onuUniPortStatisticTxUnicastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticTxUnicastPackets.setStatus(_A)
_OnuUniPortStatisticTxMulticastPackets_Type=Counter64
_OnuUniPortStatisticTxMulticastPackets_Object=MibTableColumn
onuUniPortStatisticTxMulticastPackets=_OnuUniPortStatisticTxMulticastPackets_Object((1,3,6,1,4,1,3320,10,4,2,1,11),_OnuUniPortStatisticTxMulticastPackets_Type())
onuUniPortStatisticTxMulticastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticTxMulticastPackets.setStatus(_A)
_OnuUniPortStatisticTxBroadcastPackets_Type=Counter64
_OnuUniPortStatisticTxBroadcastPackets_Object=MibTableColumn
onuUniPortStatisticTxBroadcastPackets=_OnuUniPortStatisticTxBroadcastPackets_Object((1,3,6,1,4,1,3320,10,4,2,1,12),_OnuUniPortStatisticTxBroadcastPackets_Type())
onuUniPortStatisticTxBroadcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticTxBroadcastPackets.setStatus(_A)
_OnuUniPortStatisticTxDiscardedPackets_Type=Counter64
_OnuUniPortStatisticTxDiscardedPackets_Object=MibTableColumn
onuUniPortStatisticTxDiscardedPackets=_OnuUniPortStatisticTxDiscardedPackets_Object((1,3,6,1,4,1,3320,10,4,2,1,13),_OnuUniPortStatisticTxDiscardedPackets_Type())
onuUniPortStatisticTxDiscardedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticTxDiscardedPackets.setStatus(_A)
_OnuUniPortStatisticRxUndersizePackets_Type=Counter64
_OnuUniPortStatisticRxUndersizePackets_Object=MibTableColumn
onuUniPortStatisticRxUndersizePackets=_OnuUniPortStatisticRxUndersizePackets_Object((1,3,6,1,4,1,3320,10,4,2,1,14),_OnuUniPortStatisticRxUndersizePackets_Type())
onuUniPortStatisticRxUndersizePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticRxUndersizePackets.setStatus(_A)
_OnuUniPortStatisticRxFragments_Type=Counter64
_OnuUniPortStatisticRxFragments_Object=MibTableColumn
onuUniPortStatisticRxFragments=_OnuUniPortStatisticRxFragments_Object((1,3,6,1,4,1,3320,10,4,2,1,15),_OnuUniPortStatisticRxFragments_Type())
onuUniPortStatisticRxFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticRxFragments.setStatus(_A)
_OnuUniPortStatisticRxJabbers_Type=Counter64
_OnuUniPortStatisticRxJabbers_Object=MibTableColumn
onuUniPortStatisticRxJabbers=_OnuUniPortStatisticRxJabbers_Object((1,3,6,1,4,1,3320,10,4,2,1,16),_OnuUniPortStatisticRxJabbers_Type())
onuUniPortStatisticRxJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticRxJabbers.setStatus(_A)
_OnuUniPortStatisticRxPackets64Octets_Type=Counter64
_OnuUniPortStatisticRxPackets64Octets_Object=MibTableColumn
onuUniPortStatisticRxPackets64Octets=_OnuUniPortStatisticRxPackets64Octets_Object((1,3,6,1,4,1,3320,10,4,2,1,17),_OnuUniPortStatisticRxPackets64Octets_Type())
onuUniPortStatisticRxPackets64Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticRxPackets64Octets.setStatus(_A)
_OnuUniPortStatisticRxPackets65to127Octets_Type=Counter64
_OnuUniPortStatisticRxPackets65to127Octets_Object=MibTableColumn
onuUniPortStatisticRxPackets65to127Octets=_OnuUniPortStatisticRxPackets65to127Octets_Object((1,3,6,1,4,1,3320,10,4,2,1,18),_OnuUniPortStatisticRxPackets65to127Octets_Type())
onuUniPortStatisticRxPackets65to127Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticRxPackets65to127Octets.setStatus(_A)
_OnuUniPortStatisticRxPackets128to255Octets_Type=Counter64
_OnuUniPortStatisticRxPackets128to255Octets_Object=MibTableColumn
onuUniPortStatisticRxPackets128to255Octets=_OnuUniPortStatisticRxPackets128to255Octets_Object((1,3,6,1,4,1,3320,10,4,2,1,19),_OnuUniPortStatisticRxPackets128to255Octets_Type())
onuUniPortStatisticRxPackets128to255Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticRxPackets128to255Octets.setStatus(_A)
_OnuUniPortStatisticRxPackets256to511Octets_Type=Counter64
_OnuUniPortStatisticRxPackets256to511Octets_Object=MibTableColumn
onuUniPortStatisticRxPackets256to511Octets=_OnuUniPortStatisticRxPackets256to511Octets_Object((1,3,6,1,4,1,3320,10,4,2,1,20),_OnuUniPortStatisticRxPackets256to511Octets_Type())
onuUniPortStatisticRxPackets256to511Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticRxPackets256to511Octets.setStatus(_A)
_OnuUniPortStatisticRxPackets512to1023Octets_Type=Counter64
_OnuUniPortStatisticRxPackets512to1023Octets_Object=MibTableColumn
onuUniPortStatisticRxPackets512to1023Octets=_OnuUniPortStatisticRxPackets512to1023Octets_Object((1,3,6,1,4,1,3320,10,4,2,1,21),_OnuUniPortStatisticRxPackets512to1023Octets_Type())
onuUniPortStatisticRxPackets512to1023Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticRxPackets512to1023Octets.setStatus(_A)
_OnuUniPortStatisticRxPackets1024to1518Octets_Type=Counter64
_OnuUniPortStatisticRxPackets1024to1518Octets_Object=MibTableColumn
onuUniPortStatisticRxPackets1024to1518Octets=_OnuUniPortStatisticRxPackets1024to1518Octets_Object((1,3,6,1,4,1,3320,10,4,2,1,22),_OnuUniPortStatisticRxPackets1024to1518Octets_Type())
onuUniPortStatisticRxPackets1024to1518Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticRxPackets1024to1518Octets.setStatus(_A)
_OnuUniPortStatisticRxFcsErrors_Type=Counter64
_OnuUniPortStatisticRxFcsErrors_Object=MibTableColumn
onuUniPortStatisticRxFcsErrors=_OnuUniPortStatisticRxFcsErrors_Object((1,3,6,1,4,1,3320,10,4,2,1,23),_OnuUniPortStatisticRxFcsErrors_Type())
onuUniPortStatisticRxFcsErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticRxFcsErrors.setStatus(_A)
_OnuUniPortStatisticTxFcsErrors_Type=Counter64
_OnuUniPortStatisticTxFcsErrors_Object=MibTableColumn
onuUniPortStatisticTxFcsErrors=_OnuUniPortStatisticTxFcsErrors_Object((1,3,6,1,4,1,3320,10,4,2,1,24),_OnuUniPortStatisticTxFcsErrors_Type())
onuUniPortStatisticTxFcsErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticTxFcsErrors.setStatus(_A)
_OnuUniPortStatisticTxExcessiveCollisions_Type=Counter64
_OnuUniPortStatisticTxExcessiveCollisions_Object=MibTableColumn
onuUniPortStatisticTxExcessiveCollisions=_OnuUniPortStatisticTxExcessiveCollisions_Object((1,3,6,1,4,1,3320,10,4,2,1,25),_OnuUniPortStatisticTxExcessiveCollisions_Type())
onuUniPortStatisticTxExcessiveCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticTxExcessiveCollisions.setStatus(_A)
_OnuUniPortStatisticTxLateCollisions_Type=Counter64
_OnuUniPortStatisticTxLateCollisions_Object=MibTableColumn
onuUniPortStatisticTxLateCollisions=_OnuUniPortStatisticTxLateCollisions_Object((1,3,6,1,4,1,3320,10,4,2,1,26),_OnuUniPortStatisticTxLateCollisions_Type())
onuUniPortStatisticTxLateCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticTxLateCollisions.setStatus(_A)
_OnuUniPortStatisticRxPacketsTooLong_Type=Counter64
_OnuUniPortStatisticRxPacketsTooLong_Object=MibTableColumn
onuUniPortStatisticRxPacketsTooLong=_OnuUniPortStatisticRxPacketsTooLong_Object((1,3,6,1,4,1,3320,10,4,2,1,27),_OnuUniPortStatisticRxPacketsTooLong_Type())
onuUniPortStatisticRxPacketsTooLong.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticRxPacketsTooLong.setStatus(_A)
_OnuUniPortStatisticRxBufferOverflows_Type=Counter64
_OnuUniPortStatisticRxBufferOverflows_Object=MibTableColumn
onuUniPortStatisticRxBufferOverflows=_OnuUniPortStatisticRxBufferOverflows_Object((1,3,6,1,4,1,3320,10,4,2,1,28),_OnuUniPortStatisticRxBufferOverflows_Type())
onuUniPortStatisticRxBufferOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticRxBufferOverflows.setStatus(_A)
_OnuUniPortStatisticTxBufferOverflows_Type=Counter64
_OnuUniPortStatisticTxBufferOverflows_Object=MibTableColumn
onuUniPortStatisticTxBufferOverflows=_OnuUniPortStatisticTxBufferOverflows_Object((1,3,6,1,4,1,3320,10,4,2,1,29),_OnuUniPortStatisticTxBufferOverflows_Type())
onuUniPortStatisticTxBufferOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticTxBufferOverflows.setStatus(_A)
_OnuUniPortStatisticTxSingleCollisionPackets_Type=Counter64
_OnuUniPortStatisticTxSingleCollisionPackets_Object=MibTableColumn
onuUniPortStatisticTxSingleCollisionPackets=_OnuUniPortStatisticTxSingleCollisionPackets_Object((1,3,6,1,4,1,3320,10,4,2,1,30),_OnuUniPortStatisticTxSingleCollisionPackets_Type())
onuUniPortStatisticTxSingleCollisionPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticTxSingleCollisionPackets.setStatus(_A)
_OnuUniPortStatisticTxMultipleCollisionsPackets_Type=Counter64
_OnuUniPortStatisticTxMultipleCollisionsPackets_Object=MibTableColumn
onuUniPortStatisticTxMultipleCollisionsPackets=_OnuUniPortStatisticTxMultipleCollisionsPackets_Object((1,3,6,1,4,1,3320,10,4,2,1,31),_OnuUniPortStatisticTxMultipleCollisionsPackets_Type())
onuUniPortStatisticTxMultipleCollisionsPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticTxMultipleCollisionsPackets.setStatus(_A)
_OnuUniPortStatisticSQEs_Type=Counter64
_OnuUniPortStatisticSQEs_Object=MibTableColumn
onuUniPortStatisticSQEs=_OnuUniPortStatisticSQEs_Object((1,3,6,1,4,1,3320,10,4,2,1,32),_OnuUniPortStatisticSQEs_Type())
onuUniPortStatisticSQEs.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticSQEs.setStatus(_A)
_OnuUniPortStatisticTxDeferredTransmissio_Type=Counter64
_OnuUniPortStatisticTxDeferredTransmissio_Object=MibTableColumn
onuUniPortStatisticTxDeferredTransmissio=_OnuUniPortStatisticTxDeferredTransmissio_Object((1,3,6,1,4,1,3320,10,4,2,1,33),_OnuUniPortStatisticTxDeferredTransmissio_Type())
onuUniPortStatisticTxDeferredTransmissio.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticTxDeferredTransmissio.setStatus(_A)
_OnuUniPortStatisticTxInternalMACTransmitError_Type=Counter64
_OnuUniPortStatisticTxInternalMACTransmitError_Object=MibTableColumn
onuUniPortStatisticTxInternalMACTransmitError=_OnuUniPortStatisticTxInternalMACTransmitError_Object((1,3,6,1,4,1,3320,10,4,2,1,34),_OnuUniPortStatisticTxInternalMACTransmitError_Type())
onuUniPortStatisticTxInternalMACTransmitError.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticTxInternalMACTransmitError.setStatus(_A)
_OnuUniPortStatisticCarrierSenseError_Type=Counter64
_OnuUniPortStatisticCarrierSenseError_Object=MibTableColumn
onuUniPortStatisticCarrierSenseError=_OnuUniPortStatisticCarrierSenseError_Object((1,3,6,1,4,1,3320,10,4,2,1,35),_OnuUniPortStatisticCarrierSenseError_Type())
onuUniPortStatisticCarrierSenseError.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticCarrierSenseError.setStatus(_A)
_OnuUniPortStatisticRxAlignmentError_Type=Counter64
_OnuUniPortStatisticRxAlignmentError_Object=MibTableColumn
onuUniPortStatisticRxAlignmentError=_OnuUniPortStatisticRxAlignmentError_Object((1,3,6,1,4,1,3320,10,4,2,1,36),_OnuUniPortStatisticRxAlignmentError_Type())
onuUniPortStatisticRxAlignmentError.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticRxAlignmentError.setStatus(_A)
_OnuUniPortStatisticRxInternalMACReceiveError_Type=Counter64
_OnuUniPortStatisticRxInternalMACReceiveError_Object=MibTableColumn
onuUniPortStatisticRxInternalMACReceiveError=_OnuUniPortStatisticRxInternalMACReceiveError_Object((1,3,6,1,4,1,3320,10,4,2,1,37),_OnuUniPortStatisticRxInternalMACReceiveError_Type())
onuUniPortStatisticRxInternalMACReceiveError.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticRxInternalMACReceiveError.setStatus(_A)
_OnuUniPortStatisticRxOctets_Type=Counter64
_OnuUniPortStatisticRxOctets_Object=MibTableColumn
onuUniPortStatisticRxOctets=_OnuUniPortStatisticRxOctets_Object((1,3,6,1,4,1,3320,10,4,2,1,38),_OnuUniPortStatisticRxOctets_Type())
onuUniPortStatisticRxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticRxOctets.setStatus(_A)
_OnuUniPortStatisticTxOctets_Type=Counter64
_OnuUniPortStatisticTxOctets_Object=MibTableColumn
onuUniPortStatisticTxOctets=_OnuUniPortStatisticTxOctets_Object((1,3,6,1,4,1,3320,10,4,2,1,39),_OnuUniPortStatisticTxOctets_Type())
onuUniPortStatisticTxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPortStatisticTxOctets.setStatus(_A)
_OnuUniPort15MinStatisticTable_Object=MibTable
onuUniPort15MinStatisticTable=_OnuUniPort15MinStatisticTable_Object((1,3,6,1,4,1,3320,10,4,3))
if mibBuilder.loadTexts:onuUniPort15MinStatisticTable.setStatus(_A)
_OnuUniPort15MinStatisticEntry_Object=MibTableRow
onuUniPort15MinStatisticEntry=_OnuUniPort15MinStatisticEntry_Object((1,3,6,1,4,1,3320,10,4,3,1))
onuUniPort15MinStatisticEntry.setIndexNames((0,_E,_m),(0,_E,_n),(0,_E,_o))
if mibBuilder.loadTexts:onuUniPort15MinStatisticEntry.setStatus(_A)
_OnuUniPort15MinStatisticDeviceIndex_Type=Integer32
_OnuUniPort15MinStatisticDeviceIndex_Object=MibTableColumn
onuUniPort15MinStatisticDeviceIndex=_OnuUniPort15MinStatisticDeviceIndex_Object((1,3,6,1,4,1,3320,10,4,3,1,1),_OnuUniPort15MinStatisticDeviceIndex_Type())
onuUniPort15MinStatisticDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticDeviceIndex.setStatus(_A)
_OnuUniPort15MinStatisticUniPortIndex_Type=Integer32
_OnuUniPort15MinStatisticUniPortIndex_Object=MibTableColumn
onuUniPort15MinStatisticUniPortIndex=_OnuUniPort15MinStatisticUniPortIndex_Object((1,3,6,1,4,1,3320,10,4,3,1,2),_OnuUniPort15MinStatisticUniPortIndex_Type())
onuUniPort15MinStatisticUniPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticUniPortIndex.setStatus(_A)
_OnuUniPort15MinStatisticIntervalID_Type=Integer32
_OnuUniPort15MinStatisticIntervalID_Object=MibTableColumn
onuUniPort15MinStatisticIntervalID=_OnuUniPort15MinStatisticIntervalID_Object((1,3,6,1,4,1,3320,10,4,3,1,3),_OnuUniPort15MinStatisticIntervalID_Type())
onuUniPort15MinStatisticIntervalID.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticIntervalID.setStatus(_A)
_OnuUniPort15MinStatisticRxTotalPackets_Type=Counter64
_OnuUniPort15MinStatisticRxTotalPackets_Object=MibTableColumn
onuUniPort15MinStatisticRxTotalPackets=_OnuUniPort15MinStatisticRxTotalPackets_Object((1,3,6,1,4,1,3320,10,4,3,1,4),_OnuUniPort15MinStatisticRxTotalPackets_Type())
onuUniPort15MinStatisticRxTotalPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticRxTotalPackets.setStatus(_A)
_OnuUniPort15MinStatisticRxUnicastPackets_Type=Counter64
_OnuUniPort15MinStatisticRxUnicastPackets_Object=MibTableColumn
onuUniPort15MinStatisticRxUnicastPackets=_OnuUniPort15MinStatisticRxUnicastPackets_Object((1,3,6,1,4,1,3320,10,4,3,1,5),_OnuUniPort15MinStatisticRxUnicastPackets_Type())
onuUniPort15MinStatisticRxUnicastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticRxUnicastPackets.setStatus(_A)
_OnuUniPort15MinStatisticRxMulticastPackets_Type=Counter64
_OnuUniPort15MinStatisticRxMulticastPackets_Object=MibTableColumn
onuUniPort15MinStatisticRxMulticastPackets=_OnuUniPort15MinStatisticRxMulticastPackets_Object((1,3,6,1,4,1,3320,10,4,3,1,6),_OnuUniPort15MinStatisticRxMulticastPackets_Type())
onuUniPort15MinStatisticRxMulticastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticRxMulticastPackets.setStatus(_A)
_OnuUniPort15MinStatisticRxBroadcastPackets_Type=Counter64
_OnuUniPort15MinStatisticRxBroadcastPackets_Object=MibTableColumn
onuUniPort15MinStatisticRxBroadcastPackets=_OnuUniPort15MinStatisticRxBroadcastPackets_Object((1,3,6,1,4,1,3320,10,4,3,1,7),_OnuUniPort15MinStatisticRxBroadcastPackets_Type())
onuUniPort15MinStatisticRxBroadcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticRxBroadcastPackets.setStatus(_A)
_OnuUniPort15MinStatisticRxDiscardedPackets_Type=Counter64
_OnuUniPort15MinStatisticRxDiscardedPackets_Object=MibTableColumn
onuUniPort15MinStatisticRxDiscardedPackets=_OnuUniPort15MinStatisticRxDiscardedPackets_Object((1,3,6,1,4,1,3320,10,4,3,1,8),_OnuUniPort15MinStatisticRxDiscardedPackets_Type())
onuUniPort15MinStatisticRxDiscardedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticRxDiscardedPackets.setStatus(_A)
_OnuUniPort15MinStatisticTxTotalPackets_Type=Counter64
_OnuUniPort15MinStatisticTxTotalPackets_Object=MibTableColumn
onuUniPort15MinStatisticTxTotalPackets=_OnuUniPort15MinStatisticTxTotalPackets_Object((1,3,6,1,4,1,3320,10,4,3,1,9),_OnuUniPort15MinStatisticTxTotalPackets_Type())
onuUniPort15MinStatisticTxTotalPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticTxTotalPackets.setStatus(_A)
_OnuUniPort15MinStatisticTxUnicastPackets_Type=Counter64
_OnuUniPort15MinStatisticTxUnicastPackets_Object=MibTableColumn
onuUniPort15MinStatisticTxUnicastPackets=_OnuUniPort15MinStatisticTxUnicastPackets_Object((1,3,6,1,4,1,3320,10,4,3,1,10),_OnuUniPort15MinStatisticTxUnicastPackets_Type())
onuUniPort15MinStatisticTxUnicastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticTxUnicastPackets.setStatus(_A)
_OnuUniPort15MinStatisticTxMulticastPackets_Type=Counter64
_OnuUniPort15MinStatisticTxMulticastPackets_Object=MibTableColumn
onuUniPort15MinStatisticTxMulticastPackets=_OnuUniPort15MinStatisticTxMulticastPackets_Object((1,3,6,1,4,1,3320,10,4,3,1,11),_OnuUniPort15MinStatisticTxMulticastPackets_Type())
onuUniPort15MinStatisticTxMulticastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticTxMulticastPackets.setStatus(_A)
_OnuUniPort15MinStatisticTxBroadcastPackets_Type=Counter64
_OnuUniPort15MinStatisticTxBroadcastPackets_Object=MibTableColumn
onuUniPort15MinStatisticTxBroadcastPackets=_OnuUniPort15MinStatisticTxBroadcastPackets_Object((1,3,6,1,4,1,3320,10,4,3,1,12),_OnuUniPort15MinStatisticTxBroadcastPackets_Type())
onuUniPort15MinStatisticTxBroadcastPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticTxBroadcastPackets.setStatus(_A)
_OnuUniPort15MinStatisticTxDiscardedPackets_Type=Counter64
_OnuUniPort15MinStatisticTxDiscardedPackets_Object=MibTableColumn
onuUniPort15MinStatisticTxDiscardedPackets=_OnuUniPort15MinStatisticTxDiscardedPackets_Object((1,3,6,1,4,1,3320,10,4,3,1,13),_OnuUniPort15MinStatisticTxDiscardedPackets_Type())
onuUniPort15MinStatisticTxDiscardedPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticTxDiscardedPackets.setStatus(_A)
_OnuUniPort15MinStatisticRxUndersizePackets_Type=Counter64
_OnuUniPort15MinStatisticRxUndersizePackets_Object=MibTableColumn
onuUniPort15MinStatisticRxUndersizePackets=_OnuUniPort15MinStatisticRxUndersizePackets_Object((1,3,6,1,4,1,3320,10,4,3,1,14),_OnuUniPort15MinStatisticRxUndersizePackets_Type())
onuUniPort15MinStatisticRxUndersizePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticRxUndersizePackets.setStatus(_A)
_OnuUniPort15MinStatisticRxFragments_Type=Counter64
_OnuUniPort15MinStatisticRxFragments_Object=MibTableColumn
onuUniPort15MinStatisticRxFragments=_OnuUniPort15MinStatisticRxFragments_Object((1,3,6,1,4,1,3320,10,4,3,1,15),_OnuUniPort15MinStatisticRxFragments_Type())
onuUniPort15MinStatisticRxFragments.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticRxFragments.setStatus(_A)
_OnuUniPort15MinStatisticRxJabbers_Type=Counter64
_OnuUniPort15MinStatisticRxJabbers_Object=MibTableColumn
onuUniPort15MinStatisticRxJabbers=_OnuUniPort15MinStatisticRxJabbers_Object((1,3,6,1,4,1,3320,10,4,3,1,16),_OnuUniPort15MinStatisticRxJabbers_Type())
onuUniPort15MinStatisticRxJabbers.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticRxJabbers.setStatus(_A)
_OnuUniPort15MinStatisticRxPackets64Octets_Type=Counter64
_OnuUniPort15MinStatisticRxPackets64Octets_Object=MibTableColumn
onuUniPort15MinStatisticRxPackets64Octets=_OnuUniPort15MinStatisticRxPackets64Octets_Object((1,3,6,1,4,1,3320,10,4,3,1,17),_OnuUniPort15MinStatisticRxPackets64Octets_Type())
onuUniPort15MinStatisticRxPackets64Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticRxPackets64Octets.setStatus(_A)
_OnuUniPort15MinStatisticRxPackets65to127Octets_Type=Counter64
_OnuUniPort15MinStatisticRxPackets65to127Octets_Object=MibTableColumn
onuUniPort15MinStatisticRxPackets65to127Octets=_OnuUniPort15MinStatisticRxPackets65to127Octets_Object((1,3,6,1,4,1,3320,10,4,3,1,18),_OnuUniPort15MinStatisticRxPackets65to127Octets_Type())
onuUniPort15MinStatisticRxPackets65to127Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticRxPackets65to127Octets.setStatus(_A)
_OnuUniPort15MinStatisticRxPackets128to255Octets_Type=Counter64
_OnuUniPort15MinStatisticRxPackets128to255Octets_Object=MibTableColumn
onuUniPort15MinStatisticRxPackets128to255Octets=_OnuUniPort15MinStatisticRxPackets128to255Octets_Object((1,3,6,1,4,1,3320,10,4,3,1,19),_OnuUniPort15MinStatisticRxPackets128to255Octets_Type())
onuUniPort15MinStatisticRxPackets128to255Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticRxPackets128to255Octets.setStatus(_A)
_OnuUniPort15MinStatisticRxPackets256to511Octets_Type=Counter64
_OnuUniPort15MinStatisticRxPackets256to511Octets_Object=MibTableColumn
onuUniPort15MinStatisticRxPackets256to511Octets=_OnuUniPort15MinStatisticRxPackets256to511Octets_Object((1,3,6,1,4,1,3320,10,4,3,1,20),_OnuUniPort15MinStatisticRxPackets256to511Octets_Type())
onuUniPort15MinStatisticRxPackets256to511Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticRxPackets256to511Octets.setStatus(_A)
_OnuUniPort15MinStatisticRxPackets512to1023Octets_Type=Counter64
_OnuUniPort15MinStatisticRxPackets512to1023Octets_Object=MibTableColumn
onuUniPort15MinStatisticRxPackets512to1023Octets=_OnuUniPort15MinStatisticRxPackets512to1023Octets_Object((1,3,6,1,4,1,3320,10,4,3,1,21),_OnuUniPort15MinStatisticRxPackets512to1023Octets_Type())
onuUniPort15MinStatisticRxPackets512to1023Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticRxPackets512to1023Octets.setStatus(_A)
_OnuUniPort15MinStatisticRxPackets1024to1518Octets_Type=Counter64
_OnuUniPort15MinStatisticRxPackets1024to1518Octets_Object=MibTableColumn
onuUniPort15MinStatisticRxPackets1024to1518Octets=_OnuUniPort15MinStatisticRxPackets1024to1518Octets_Object((1,3,6,1,4,1,3320,10,4,3,1,22),_OnuUniPort15MinStatisticRxPackets1024to1518Octets_Type())
onuUniPort15MinStatisticRxPackets1024to1518Octets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticRxPackets1024to1518Octets.setStatus(_A)
_OnuUniPort15MinStatisticRxFcsErrors_Type=Counter64
_OnuUniPort15MinStatisticRxFcsErrors_Object=MibTableColumn
onuUniPort15MinStatisticRxFcsErrors=_OnuUniPort15MinStatisticRxFcsErrors_Object((1,3,6,1,4,1,3320,10,4,3,1,23),_OnuUniPort15MinStatisticRxFcsErrors_Type())
onuUniPort15MinStatisticRxFcsErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticRxFcsErrors.setStatus(_A)
_OnuUniPort15MinStatisticTxFcsErrors_Type=Counter64
_OnuUniPort15MinStatisticTxFcsErrors_Object=MibTableColumn
onuUniPort15MinStatisticTxFcsErrors=_OnuUniPort15MinStatisticTxFcsErrors_Object((1,3,6,1,4,1,3320,10,4,3,1,24),_OnuUniPort15MinStatisticTxFcsErrors_Type())
onuUniPort15MinStatisticTxFcsErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticTxFcsErrors.setStatus(_A)
_OnuUniPort15MinStatisticTxExcessiveCollisions_Type=Counter64
_OnuUniPort15MinStatisticTxExcessiveCollisions_Object=MibTableColumn
onuUniPort15MinStatisticTxExcessiveCollisions=_OnuUniPort15MinStatisticTxExcessiveCollisions_Object((1,3,6,1,4,1,3320,10,4,3,1,25),_OnuUniPort15MinStatisticTxExcessiveCollisions_Type())
onuUniPort15MinStatisticTxExcessiveCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticTxExcessiveCollisions.setStatus(_A)
_OnuUniPort15MinStatisticTxLateCollisions_Type=Counter64
_OnuUniPort15MinStatisticTxLateCollisions_Object=MibTableColumn
onuUniPort15MinStatisticTxLateCollisions=_OnuUniPort15MinStatisticTxLateCollisions_Object((1,3,6,1,4,1,3320,10,4,3,1,26),_OnuUniPort15MinStatisticTxLateCollisions_Type())
onuUniPort15MinStatisticTxLateCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticTxLateCollisions.setStatus(_A)
_OnuUniPort15MinStatisticRxPacketsTooLong_Type=Counter64
_OnuUniPort15MinStatisticRxPacketsTooLong_Object=MibTableColumn
onuUniPort15MinStatisticRxPacketsTooLong=_OnuUniPort15MinStatisticRxPacketsTooLong_Object((1,3,6,1,4,1,3320,10,4,3,1,27),_OnuUniPort15MinStatisticRxPacketsTooLong_Type())
onuUniPort15MinStatisticRxPacketsTooLong.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticRxPacketsTooLong.setStatus(_A)
_OnuUniPort15MinStatisticRxBufferOverflows_Type=Counter64
_OnuUniPort15MinStatisticRxBufferOverflows_Object=MibTableColumn
onuUniPort15MinStatisticRxBufferOverflows=_OnuUniPort15MinStatisticRxBufferOverflows_Object((1,3,6,1,4,1,3320,10,4,3,1,28),_OnuUniPort15MinStatisticRxBufferOverflows_Type())
onuUniPort15MinStatisticRxBufferOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticRxBufferOverflows.setStatus(_A)
_OnuUniPort15MinStatisticTxBufferOverflows_Type=Counter64
_OnuUniPort15MinStatisticTxBufferOverflows_Object=MibTableColumn
onuUniPort15MinStatisticTxBufferOverflows=_OnuUniPort15MinStatisticTxBufferOverflows_Object((1,3,6,1,4,1,3320,10,4,3,1,29),_OnuUniPort15MinStatisticTxBufferOverflows_Type())
onuUniPort15MinStatisticTxBufferOverflows.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticTxBufferOverflows.setStatus(_A)
_OnuUniPort15MinStatisticTxSingleCollisionPackets_Type=Counter64
_OnuUniPort15MinStatisticTxSingleCollisionPackets_Object=MibTableColumn
onuUniPort15MinStatisticTxSingleCollisionPackets=_OnuUniPort15MinStatisticTxSingleCollisionPackets_Object((1,3,6,1,4,1,3320,10,4,3,1,30),_OnuUniPort15MinStatisticTxSingleCollisionPackets_Type())
onuUniPort15MinStatisticTxSingleCollisionPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticTxSingleCollisionPackets.setStatus(_A)
_OnuUniPort15MinStatisticTxMultipleCollisionsPackets_Type=Counter64
_OnuUniPort15MinStatisticTxMultipleCollisionsPackets_Object=MibTableColumn
onuUniPort15MinStatisticTxMultipleCollisionsPackets=_OnuUniPort15MinStatisticTxMultipleCollisionsPackets_Object((1,3,6,1,4,1,3320,10,4,3,1,31),_OnuUniPort15MinStatisticTxMultipleCollisionsPackets_Type())
onuUniPort15MinStatisticTxMultipleCollisionsPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticTxMultipleCollisionsPackets.setStatus(_A)
_OnuUniPort15MinStatisticSQEs_Type=Counter64
_OnuUniPort15MinStatisticSQEs_Object=MibTableColumn
onuUniPort15MinStatisticSQEs=_OnuUniPort15MinStatisticSQEs_Object((1,3,6,1,4,1,3320,10,4,3,1,32),_OnuUniPort15MinStatisticSQEs_Type())
onuUniPort15MinStatisticSQEs.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticSQEs.setStatus(_A)
_OnuUniPort15MinStatisticTxDeferredTransmissio_Type=Counter64
_OnuUniPort15MinStatisticTxDeferredTransmissio_Object=MibTableColumn
onuUniPort15MinStatisticTxDeferredTransmissio=_OnuUniPort15MinStatisticTxDeferredTransmissio_Object((1,3,6,1,4,1,3320,10,4,3,1,33),_OnuUniPort15MinStatisticTxDeferredTransmissio_Type())
onuUniPort15MinStatisticTxDeferredTransmissio.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticTxDeferredTransmissio.setStatus(_A)
_OnuUniPort15MinStatisticTxInternalMACTransmitError_Type=Counter64
_OnuUniPort15MinStatisticTxInternalMACTransmitError_Object=MibTableColumn
onuUniPort15MinStatisticTxInternalMACTransmitError=_OnuUniPort15MinStatisticTxInternalMACTransmitError_Object((1,3,6,1,4,1,3320,10,4,3,1,34),_OnuUniPort15MinStatisticTxInternalMACTransmitError_Type())
onuUniPort15MinStatisticTxInternalMACTransmitError.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticTxInternalMACTransmitError.setStatus(_A)
_OnuUniPort15MinStatisticCarrierSenseError_Type=Counter64
_OnuUniPort15MinStatisticCarrierSenseError_Object=MibTableColumn
onuUniPort15MinStatisticCarrierSenseError=_OnuUniPort15MinStatisticCarrierSenseError_Object((1,3,6,1,4,1,3320,10,4,3,1,35),_OnuUniPort15MinStatisticCarrierSenseError_Type())
onuUniPort15MinStatisticCarrierSenseError.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticCarrierSenseError.setStatus(_A)
_OnuUniPort15MinStatisticRxAlignmentError_Type=Counter64
_OnuUniPort15MinStatisticRxAlignmentError_Object=MibTableColumn
onuUniPort15MinStatisticRxAlignmentError=_OnuUniPort15MinStatisticRxAlignmentError_Object((1,3,6,1,4,1,3320,10,4,3,1,36),_OnuUniPort15MinStatisticRxAlignmentError_Type())
onuUniPort15MinStatisticRxAlignmentError.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticRxAlignmentError.setStatus(_A)
_OnuUniPort15MinStatisticRxInternalMACReceiveError_Type=Counter64
_OnuUniPort15MinStatisticRxInternalMACReceiveError_Object=MibTableColumn
onuUniPort15MinStatisticRxInternalMACReceiveError=_OnuUniPort15MinStatisticRxInternalMACReceiveError_Object((1,3,6,1,4,1,3320,10,4,3,1,37),_OnuUniPort15MinStatisticRxInternalMACReceiveError_Type())
onuUniPort15MinStatisticRxInternalMACReceiveError.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticRxInternalMACReceiveError.setStatus(_A)
_OnuUniPort15MinStatisticRxOctets_Type=Counter64
_OnuUniPort15MinStatisticRxOctets_Object=MibTableColumn
onuUniPort15MinStatisticRxOctets=_OnuUniPort15MinStatisticRxOctets_Object((1,3,6,1,4,1,3320,10,4,3,1,38),_OnuUniPort15MinStatisticRxOctets_Type())
onuUniPort15MinStatisticRxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticRxOctets.setStatus(_A)
_OnuUniPort15MinStatisticTxOctets_Type=Counter64
_OnuUniPort15MinStatisticTxOctets_Object=MibTableColumn
onuUniPort15MinStatisticTxOctets=_OnuUniPort15MinStatisticTxOctets_Object((1,3,6,1,4,1,3320,10,4,3,1,39),_OnuUniPort15MinStatisticTxOctets_Type())
onuUniPort15MinStatisticTxOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:onuUniPort15MinStatisticTxOctets.setStatus(_A)
_NmsGponVirPortObj_ObjectIdentity=ObjectIdentity
nmsGponVirPortObj=_NmsGponVirPortObj_ObjectIdentity((1,3,6,1,4,1,3320,10,5))
_OnuVirPortConfigTable_Object=MibTable
onuVirPortConfigTable=_OnuVirPortConfigTable_Object((1,3,6,1,4,1,3320,10,5,1))
if mibBuilder.loadTexts:onuVirPortConfigTable.setStatus(_A)
_OnuVirPortConfigEntry_Object=MibTableRow
onuVirPortConfigEntry=_OnuVirPortConfigEntry_Object((1,3,6,1,4,1,3320,10,5,1,1))
onuVirPortConfigEntry.setIndexNames((0,_E,_p),(0,_E,_q))
if mibBuilder.loadTexts:onuVirPortConfigEntry.setStatus(_A)
_OnuVirPortConfigDeviceIndex_Type=Integer32
_OnuVirPortConfigDeviceIndex_Object=MibTableColumn
onuVirPortConfigDeviceIndex=_OnuVirPortConfigDeviceIndex_Object((1,3,6,1,4,1,3320,10,5,1,1,1),_OnuVirPortConfigDeviceIndex_Type())
onuVirPortConfigDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVirPortConfigDeviceIndex.setStatus(_A)
_OnuVirPortConfigPortIndex_Type=Integer32
_OnuVirPortConfigPortIndex_Object=MibTableColumn
onuVirPortConfigPortIndex=_OnuVirPortConfigPortIndex_Object((1,3,6,1,4,1,3320,10,5,1,1,2),_OnuVirPortConfigPortIndex_Type())
onuVirPortConfigPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVirPortConfigPortIndex.setStatus(_A)
_OnuVirPortConfigTCONTID_Type=Integer32
_OnuVirPortConfigTCONTID_Object=MibTableColumn
onuVirPortConfigTCONTID=_OnuVirPortConfigTCONTID_Object((1,3,6,1,4,1,3320,10,5,1,1,3),_OnuVirPortConfigTCONTID_Type())
onuVirPortConfigTCONTID.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVirPortConfigTCONTID.setStatus(_A)
_OnuVirPortConfigOltGEMPortID_Type=Integer32
_OnuVirPortConfigOltGEMPortID_Object=MibTableColumn
onuVirPortConfigOltGEMPortID=_OnuVirPortConfigOltGEMPortID_Object((1,3,6,1,4,1,3320,10,5,1,1,4),_OnuVirPortConfigOltGEMPortID_Type())
onuVirPortConfigOltGEMPortID.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVirPortConfigOltGEMPortID.setStatus(_A)
_OnuVirPortConfigOltAllocID_Type=Integer32
_OnuVirPortConfigOltAllocID_Object=MibTableColumn
onuVirPortConfigOltAllocID=_OnuVirPortConfigOltAllocID_Object((1,3,6,1,4,1,3320,10,5,1,1,5),_OnuVirPortConfigOltAllocID_Type())
onuVirPortConfigOltAllocID.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVirPortConfigOltAllocID.setStatus(_A)
class _OnuVirPortConfigVirPortAdminState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('no-shutdown-unlocks',1),(_b,2)))
_OnuVirPortConfigVirPortAdminState_Type.__name__=_D
_OnuVirPortConfigVirPortAdminState_Object=MibTableColumn
onuVirPortConfigVirPortAdminState=_OnuVirPortConfigVirPortAdminState_Object((1,3,6,1,4,1,3320,10,5,1,1,6),_OnuVirPortConfigVirPortAdminState_Type())
onuVirPortConfigVirPortAdminState.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVirPortConfigVirPortAdminState.setStatus(_A)
class _OnuVirPortConfigEncryptionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_OnuVirPortConfigEncryptionMode_Type.__name__=_D
_OnuVirPortConfigEncryptionMode_Object=MibTableColumn
onuVirPortConfigEncryptionMode=_OnuVirPortConfigEncryptionMode_Object((1,3,6,1,4,1,3320,10,5,1,1,7),_OnuVirPortConfigEncryptionMode_Type())
onuVirPortConfigEncryptionMode.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVirPortConfigEncryptionMode.setStatus(_A)
_OnuVirPortConfigDownstreamRateLimit_Type=Integer32
_OnuVirPortConfigDownstreamRateLimit_Object=MibTableColumn
onuVirPortConfigDownstreamRateLimit=_OnuVirPortConfigDownstreamRateLimit_Object((1,3,6,1,4,1,3320,10,5,1,1,8),_OnuVirPortConfigDownstreamRateLimit_Type())
onuVirPortConfigDownstreamRateLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVirPortConfigDownstreamRateLimit.setStatus(_A)
class _OnuVirPortConfigOltVLANTranslationProfileID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_OnuVirPortConfigOltVLANTranslationProfileID_Type.__name__=_D
_OnuVirPortConfigOltVLANTranslationProfileID_Object=MibTableColumn
onuVirPortConfigOltVLANTranslationProfileID=_OnuVirPortConfigOltVLANTranslationProfileID_Object((1,3,6,1,4,1,3320,10,5,1,1,9),_OnuVirPortConfigOltVLANTranslationProfileID_Type())
onuVirPortConfigOltVLANTranslationProfileID.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVirPortConfigOltVLANTranslationProfileID.setStatus(_A)
_OnuVirPortConfigONUMacFilterProfileID_Type=Integer32
_OnuVirPortConfigONUMacFilterProfileID_Object=MibTableColumn
onuVirPortConfigONUMacFilterProfileID=_OnuVirPortConfigONUMacFilterProfileID_Object((1,3,6,1,4,1,3320,10,5,1,1,10),_OnuVirPortConfigONUMacFilterProfileID_Type())
onuVirPortConfigONUMacFilterProfileID.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVirPortConfigONUMacFilterProfileID.setStatus(_A)
_OnuVirPortConfigONUMacFilterPreassignProfileID_Type=Integer32
_OnuVirPortConfigONUMacFilterPreassignProfileID_Object=MibTableColumn
onuVirPortConfigONUMacFilterPreassignProfileID=_OnuVirPortConfigONUMacFilterPreassignProfileID_Object((1,3,6,1,4,1,3320,10,5,1,1,11),_OnuVirPortConfigONUMacFilterPreassignProfileID_Type())
onuVirPortConfigONUMacFilterPreassignProfileID.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVirPortConfigONUMacFilterPreassignProfileID.setStatus(_A)
_OnuVirPortConfigRowStatus_Type=RowStatus
_OnuVirPortConfigRowStatus_Object=MibTableColumn
onuVirPortConfigRowStatus=_OnuVirPortConfigRowStatus_Object((1,3,6,1,4,1,3320,10,5,1,1,12),_OnuVirPortConfigRowStatus_Type())
onuVirPortConfigRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:onuVirPortConfigRowStatus.setStatus(_A)
_OnuVirPortStatisticTable_Object=MibTable
onuVirPortStatisticTable=_OnuVirPortStatisticTable_Object((1,3,6,1,4,1,3320,10,5,2))
if mibBuilder.loadTexts:onuVirPortStatisticTable.setStatus(_A)
_OnuVirPortStatisticEntry_Object=MibTableRow
onuVirPortStatisticEntry=_OnuVirPortStatisticEntry_Object((1,3,6,1,4,1,3320,10,5,2,1))
onuVirPortStatisticEntry.setIndexNames((0,_E,_r),(0,_E,_s))
if mibBuilder.loadTexts:onuVirPortStatisticEntry.setStatus(_A)
_OnuVirPortStatisticDeviceIndex_Type=Integer32
_OnuVirPortStatisticDeviceIndex_Object=MibTableColumn
onuVirPortStatisticDeviceIndex=_OnuVirPortStatisticDeviceIndex_Object((1,3,6,1,4,1,3320,10,5,2,1,1),_OnuVirPortStatisticDeviceIndex_Type())
onuVirPortStatisticDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVirPortStatisticDeviceIndex.setStatus(_A)
_OnuVirPortStatisticVirPortIndex_Type=Integer32
_OnuVirPortStatisticVirPortIndex_Object=MibTableColumn
onuVirPortStatisticVirPortIndex=_OnuVirPortStatisticVirPortIndex_Object((1,3,6,1,4,1,3320,10,5,2,1,2),_OnuVirPortStatisticVirPortIndex_Type())
onuVirPortStatisticVirPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVirPortStatisticVirPortIndex.setStatus(_A)
_OnuVirPortStatisticTime_Type=Counter64
_OnuVirPortStatisticTime_Object=MibTableColumn
onuVirPortStatisticTime=_OnuVirPortStatisticTime_Object((1,3,6,1,4,1,3320,10,5,2,1,3),_OnuVirPortStatisticTime_Type())
onuVirPortStatisticTime.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVirPortStatisticTime.setStatus(_A)
_OnuVirPortStatisticRxTotalFrames_Type=Counter64
_OnuVirPortStatisticRxTotalFrames_Object=MibTableColumn
onuVirPortStatisticRxTotalFrames=_OnuVirPortStatisticRxTotalFrames_Object((1,3,6,1,4,1,3320,10,5,2,1,4),_OnuVirPortStatisticRxTotalFrames_Type())
onuVirPortStatisticRxTotalFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVirPortStatisticRxTotalFrames.setStatus(_A)
_OnuVirPortStatisticTxTotalFrames_Type=Counter64
_OnuVirPortStatisticTxTotalFrames_Object=MibTableColumn
onuVirPortStatisticTxTotalFrames=_OnuVirPortStatisticTxTotalFrames_Object((1,3,6,1,4,1,3320,10,5,2,1,5),_OnuVirPortStatisticTxTotalFrames_Type())
onuVirPortStatisticTxTotalFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVirPortStatisticTxTotalFrames.setStatus(_A)
_OnuVirPortStatisticRxTotalBytes_Type=Counter64
_OnuVirPortStatisticRxTotalBytes_Object=MibTableColumn
onuVirPortStatisticRxTotalBytes=_OnuVirPortStatisticRxTotalBytes_Object((1,3,6,1,4,1,3320,10,5,2,1,6),_OnuVirPortStatisticRxTotalBytes_Type())
onuVirPortStatisticRxTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVirPortStatisticRxTotalBytes.setStatus(_A)
_OnuVirPortStatisticTxTotalBytes_Type=Counter64
_OnuVirPortStatisticTxTotalBytes_Object=MibTableColumn
onuVirPortStatisticTxTotalBytes=_OnuVirPortStatisticTxTotalBytes_Object((1,3,6,1,4,1,3320,10,5,2,1,7),_OnuVirPortStatisticTxTotalBytes_Type())
onuVirPortStatisticTxTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVirPortStatisticTxTotalBytes.setStatus(_A)
_OnuVirPortStatisticEncryptKeyErrors_Type=Counter64
_OnuVirPortStatisticEncryptKeyErrors_Object=MibTableColumn
onuVirPortStatisticEncryptKeyErrors=_OnuVirPortStatisticEncryptKeyErrors_Object((1,3,6,1,4,1,3320,10,5,2,1,8),_OnuVirPortStatisticEncryptKeyErrors_Type())
onuVirPortStatisticEncryptKeyErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVirPortStatisticEncryptKeyErrors.setStatus(_A)
_OnuVirPort15MinStatisticTable_Object=MibTable
onuVirPort15MinStatisticTable=_OnuVirPort15MinStatisticTable_Object((1,3,6,1,4,1,3320,10,5,3))
if mibBuilder.loadTexts:onuVirPort15MinStatisticTable.setStatus(_A)
_OnuVirPort15MinStatisticEntry_Object=MibTableRow
onuVirPort15MinStatisticEntry=_OnuVirPort15MinStatisticEntry_Object((1,3,6,1,4,1,3320,10,5,3,1))
onuVirPort15MinStatisticEntry.setIndexNames((0,_E,_t),(0,_E,_u),(0,_E,_v))
if mibBuilder.loadTexts:onuVirPort15MinStatisticEntry.setStatus(_A)
_OnuVirPort15MinStatisticDeviceIndex_Type=Integer32
_OnuVirPort15MinStatisticDeviceIndex_Object=MibTableColumn
onuVirPort15MinStatisticDeviceIndex=_OnuVirPort15MinStatisticDeviceIndex_Object((1,3,6,1,4,1,3320,10,5,3,1,1),_OnuVirPort15MinStatisticDeviceIndex_Type())
onuVirPort15MinStatisticDeviceIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVirPort15MinStatisticDeviceIndex.setStatus(_A)
_OnuVirPort15MinStatisticVirPortIndex_Type=Integer32
_OnuVirPort15MinStatisticVirPortIndex_Object=MibTableColumn
onuVirPort15MinStatisticVirPortIndex=_OnuVirPort15MinStatisticVirPortIndex_Object((1,3,6,1,4,1,3320,10,5,3,1,2),_OnuVirPort15MinStatisticVirPortIndex_Type())
onuVirPort15MinStatisticVirPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVirPort15MinStatisticVirPortIndex.setStatus(_A)
_OnuVirPort15MinStatisticIntervalID_Type=Integer32
_OnuVirPort15MinStatisticIntervalID_Object=MibTableColumn
onuVirPort15MinStatisticIntervalID=_OnuVirPort15MinStatisticIntervalID_Object((1,3,6,1,4,1,3320,10,5,3,1,3),_OnuVirPort15MinStatisticIntervalID_Type())
onuVirPort15MinStatisticIntervalID.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVirPort15MinStatisticIntervalID.setStatus(_A)
_OnuVirPort15MinStatisticRxTotalFrames_Type=Counter64
_OnuVirPort15MinStatisticRxTotalFrames_Object=MibTableColumn
onuVirPort15MinStatisticRxTotalFrames=_OnuVirPort15MinStatisticRxTotalFrames_Object((1,3,6,1,4,1,3320,10,5,3,1,4),_OnuVirPort15MinStatisticRxTotalFrames_Type())
onuVirPort15MinStatisticRxTotalFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVirPort15MinStatisticRxTotalFrames.setStatus(_A)
_OnuVirPort15MinStatisticTxTotalFrames_Type=Counter64
_OnuVirPort15MinStatisticTxTotalFrames_Object=MibTableColumn
onuVirPort15MinStatisticTxTotalFrames=_OnuVirPort15MinStatisticTxTotalFrames_Object((1,3,6,1,4,1,3320,10,5,3,1,5),_OnuVirPort15MinStatisticTxTotalFrames_Type())
onuVirPort15MinStatisticTxTotalFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVirPort15MinStatisticTxTotalFrames.setStatus(_A)
_OnuVirPort15MinStatisticRxTotalBytes_Type=Counter64
_OnuVirPort15MinStatisticRxTotalBytes_Object=MibTableColumn
onuVirPort15MinStatisticRxTotalBytes=_OnuVirPort15MinStatisticRxTotalBytes_Object((1,3,6,1,4,1,3320,10,5,3,1,6),_OnuVirPort15MinStatisticRxTotalBytes_Type())
onuVirPort15MinStatisticRxTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVirPort15MinStatisticRxTotalBytes.setStatus(_A)
_OnuVirPort15MinStatisticTxTotalBytes_Type=Counter64
_OnuVirPort15MinStatisticTxTotalBytes_Object=MibTableColumn
onuVirPort15MinStatisticTxTotalBytes=_OnuVirPort15MinStatisticTxTotalBytes_Object((1,3,6,1,4,1,3320,10,5,3,1,7),_OnuVirPort15MinStatisticTxTotalBytes_Type())
onuVirPort15MinStatisticTxTotalBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVirPort15MinStatisticTxTotalBytes.setStatus(_A)
_OnuVirPort15MinStatisticEncryptKeyErrors_Type=Counter64
_OnuVirPort15MinStatisticEncryptKeyErrors_Object=MibTableColumn
onuVirPort15MinStatisticEncryptKeyErrors=_OnuVirPort15MinStatisticEncryptKeyErrors_Object((1,3,6,1,4,1,3320,10,5,3,1,8),_OnuVirPort15MinStatisticEncryptKeyErrors_Type())
onuVirPort15MinStatisticEncryptKeyErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVirPort15MinStatisticEncryptKeyErrors.setStatus(_A)
_NmsGponProfile_ObjectIdentity=ObjectIdentity
nmsGponProfile=_NmsGponProfile_ObjectIdentity((1,3,6,1,4,1,3320,10,6))
_OnuVLANProfile_ObjectIdentity=ObjectIdentity
onuVLANProfile=_OnuVLANProfile_ObjectIdentity((1,3,6,1,4,1,3320,10,6,1))
_OnuVLANProfileTable_Object=MibTable
onuVLANProfileTable=_OnuVLANProfileTable_Object((1,3,6,1,4,1,3320,10,6,1,1))
if mibBuilder.loadTexts:onuVLANProfileTable.setStatus(_A)
_OnuVLANProfileEntry_Object=MibTableRow
onuVLANProfileEntry=_OnuVLANProfileEntry_Object((1,3,6,1,4,1,3320,10,6,1,1,1))
onuVLANProfileEntry.setIndexNames((0,_E,_w))
if mibBuilder.loadTexts:onuVLANProfileEntry.setStatus(_A)
_OnuVLANProfileIndex_Type=Integer32
_OnuVLANProfileIndex_Object=MibTableColumn
onuVLANProfileIndex=_OnuVLANProfileIndex_Object((1,3,6,1,4,1,3320,10,6,1,1,1,1),_OnuVLANProfileIndex_Type())
onuVLANProfileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVLANProfileIndex.setStatus(_A)
_OnuVLANProfileName_Type=OctetString
_OnuVLANProfileName_Object=MibTableColumn
onuVLANProfileName=_OnuVLANProfileName_Object((1,3,6,1,4,1,3320,10,6,1,1,1,2),_OnuVLANProfileName_Type())
onuVLANProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVLANProfileName.setStatus(_A)
class _OnuVLANProfileVlanMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('transparent',1),('tag',2),('translation',3),('vlan-stacking',4),('aggregation',5),('trunk',6)))
_OnuVLANProfileVlanMode_Type.__name__=_D
_OnuVLANProfileVlanMode_Object=MibTableColumn
onuVLANProfileVlanMode=_OnuVLANProfileVlanMode_Object((1,3,6,1,4,1,3320,10,6,1,1,1,3),_OnuVLANProfileVlanMode_Type())
onuVLANProfileVlanMode.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVLANProfileVlanMode.setStatus(_A)
class _OnuVLANProfilePVID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_OnuVLANProfilePVID_Type.__name__=_D
_OnuVLANProfilePVID_Object=MibTableColumn
onuVLANProfilePVID=_OnuVLANProfilePVID_Object((1,3,6,1,4,1,3320,10,6,1,1,1,4),_OnuVLANProfilePVID_Type())
onuVLANProfilePVID.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVLANProfilePVID.setStatus(_A)
_OnuVLANProfileTrunkVlans_Type=OctetString
_OnuVLANProfileTrunkVlans_Object=MibTableColumn
onuVLANProfileTrunkVlans=_OnuVLANProfileTrunkVlans_Object((1,3,6,1,4,1,3320,10,6,1,1,1,5),_OnuVLANProfileTrunkVlans_Type())
onuVLANProfileTrunkVlans.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVLANProfileTrunkVlans.setStatus(_A)
class _OnuVLANProfileEtherTypeIPOEVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_OnuVLANProfileEtherTypeIPOEVlan_Type.__name__=_D
_OnuVLANProfileEtherTypeIPOEVlan_Object=MibTableColumn
onuVLANProfileEtherTypeIPOEVlan=_OnuVLANProfileEtherTypeIPOEVlan_Object((1,3,6,1,4,1,3320,10,6,1,1,1,6),_OnuVLANProfileEtherTypeIPOEVlan_Type())
onuVLANProfileEtherTypeIPOEVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVLANProfileEtherTypeIPOEVlan.setStatus(_A)
class _OnuVLANProfileEtherTypePPPOEVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_OnuVLANProfileEtherTypePPPOEVlan_Type.__name__=_D
_OnuVLANProfileEtherTypePPPOEVlan_Object=MibTableColumn
onuVLANProfileEtherTypePPPOEVlan=_OnuVLANProfileEtherTypePPPOEVlan_Object((1,3,6,1,4,1,3320,10,6,1,1,1,7),_OnuVLANProfileEtherTypePPPOEVlan_Type())
onuVLANProfileEtherTypePPPOEVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVLANProfileEtherTypePPPOEVlan.setStatus(_A)
class _OnuVLANProfileEtherTypeARPVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_OnuVLANProfileEtherTypeARPVlan_Type.__name__=_D
_OnuVLANProfileEtherTypeARPVlan_Object=MibTableColumn
onuVLANProfileEtherTypeARPVlan=_OnuVLANProfileEtherTypeARPVlan_Object((1,3,6,1,4,1,3320,10,6,1,1,1,8),_OnuVLANProfileEtherTypeARPVlan_Type())
onuVLANProfileEtherTypeARPVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVLANProfileEtherTypeARPVlan.setStatus(_A)
_OnuVLANProfileRowStatus_Type=RowStatus
_OnuVLANProfileRowStatus_Object=MibTableColumn
onuVLANProfileRowStatus=_OnuVLANProfileRowStatus_Object((1,3,6,1,4,1,3320,10,6,1,1,1,9),_OnuVLANProfileRowStatus_Type())
onuVLANProfileRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:onuVLANProfileRowStatus.setStatus(_A)
_OnuVLANTranslationTable_Object=MibTable
onuVLANTranslationTable=_OnuVLANTranslationTable_Object((1,3,6,1,4,1,3320,10,6,1,2))
if mibBuilder.loadTexts:onuVLANTranslationTable.setStatus(_A)
_OnuVLANTranslationEntry_Object=MibTableRow
onuVLANTranslationEntry=_OnuVLANTranslationEntry_Object((1,3,6,1,4,1,3320,10,6,1,2,1))
onuVLANTranslationEntry.setIndexNames((0,_E,_x),(0,_E,_y))
if mibBuilder.loadTexts:onuVLANTranslationEntry.setStatus(_A)
_OnuVLANTranslationIndex1_Type=Integer32
_OnuVLANTranslationIndex1_Object=MibTableColumn
onuVLANTranslationIndex1=_OnuVLANTranslationIndex1_Object((1,3,6,1,4,1,3320,10,6,1,2,1,1),_OnuVLANTranslationIndex1_Type())
onuVLANTranslationIndex1.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVLANTranslationIndex1.setStatus(_A)
_OnuVLANTranslationIndex2_Type=Integer32
_OnuVLANTranslationIndex2_Object=MibTableColumn
onuVLANTranslationIndex2=_OnuVLANTranslationIndex2_Object((1,3,6,1,4,1,3320,10,6,1,2,1,2),_OnuVLANTranslationIndex2_Type())
onuVLANTranslationIndex2.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVLANTranslationIndex2.setStatus(_A)
_OnuVLANTranslationName_Type=OctetString
_OnuVLANTranslationName_Object=MibTableColumn
onuVLANTranslationName=_OnuVLANTranslationName_Object((1,3,6,1,4,1,3320,10,6,1,2,1,3),_OnuVLANTranslationName_Type())
onuVLANTranslationName.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVLANTranslationName.setStatus(_A)
_OnuVLANTranslationSrcVlan_Type=Integer32
_OnuVLANTranslationSrcVlan_Object=MibTableColumn
onuVLANTranslationSrcVlan=_OnuVLANTranslationSrcVlan_Object((1,3,6,1,4,1,3320,10,6,1,2,1,4),_OnuVLANTranslationSrcVlan_Type())
onuVLANTranslationSrcVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVLANTranslationSrcVlan.setStatus(_A)
_OnuVLANTranslationDstVlan_Type=Integer32
_OnuVLANTranslationDstVlan_Object=MibTableColumn
onuVLANTranslationDstVlan=_OnuVLANTranslationDstVlan_Object((1,3,6,1,4,1,3320,10,6,1,2,1,5),_OnuVLANTranslationDstVlan_Type())
onuVLANTranslationDstVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVLANTranslationDstVlan.setStatus(_A)
_OnuVLANTranslationRowStatus_Type=RowStatus
_OnuVLANTranslationRowStatus_Object=MibTableColumn
onuVLANTranslationRowStatus=_OnuVLANTranslationRowStatus_Object((1,3,6,1,4,1,3320,10,6,1,2,1,6),_OnuVLANTranslationRowStatus_Type())
onuVLANTranslationRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:onuVLANTranslationRowStatus.setStatus(_A)
_OnuTCONTServiceProfileTable_Object=MibTable
onuTCONTServiceProfileTable=_OnuTCONTServiceProfileTable_Object((1,3,6,1,4,1,3320,10,6,2))
if mibBuilder.loadTexts:onuTCONTServiceProfileTable.setStatus(_A)
_OnuTCONTServiceProfileEntry_Object=MibTableRow
onuTCONTServiceProfileEntry=_OnuTCONTServiceProfileEntry_Object((1,3,6,1,4,1,3320,10,6,2,1))
onuTCONTServiceProfileEntry.setIndexNames((0,_E,_z))
if mibBuilder.loadTexts:onuTCONTServiceProfileEntry.setStatus(_A)
_OnuTcontServiceProfileIndex_Type=Integer32
_OnuTcontServiceProfileIndex_Object=MibTableColumn
onuTcontServiceProfileIndex=_OnuTcontServiceProfileIndex_Object((1,3,6,1,4,1,3320,10,6,2,1,1),_OnuTcontServiceProfileIndex_Type())
onuTcontServiceProfileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:onuTcontServiceProfileIndex.setStatus(_A)
_OnuTcontServiceProfileName_Type=OctetString
_OnuTcontServiceProfileName_Object=MibTableColumn
onuTcontServiceProfileName=_OnuTcontServiceProfileName_Object((1,3,6,1,4,1,3320,10,6,2,1,2),_OnuTcontServiceProfileName_Type())
onuTcontServiceProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:onuTcontServiceProfileName.setStatus(_A)
class _OnuTcontServiceProfileTcontType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('t-cont-type1',1),('t-cont-type2',2),('t-cont-type3',3),('t-cont-type4',4),('t-cont-type5',5)))
_OnuTcontServiceProfileTcontType_Type.__name__=_D
_OnuTcontServiceProfileTcontType_Object=MibTableColumn
onuTcontServiceProfileTcontType=_OnuTcontServiceProfileTcontType_Object((1,3,6,1,4,1,3320,10,6,2,1,3),_OnuTcontServiceProfileTcontType_Type())
onuTcontServiceProfileTcontType.setMaxAccess(_C)
if mibBuilder.loadTexts:onuTcontServiceProfileTcontType.setStatus(_A)
class _OnuTcontServiceProfileFir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,830976))
_OnuTcontServiceProfileFir_Type.__name__=_D
_OnuTcontServiceProfileFir_Object=MibTableColumn
onuTcontServiceProfileFir=_OnuTcontServiceProfileFir_Object((1,3,6,1,4,1,3320,10,6,2,1,4),_OnuTcontServiceProfileFir_Type())
onuTcontServiceProfileFir.setMaxAccess(_C)
if mibBuilder.loadTexts:onuTcontServiceProfileFir.setStatus(_A)
class _OnuTcontServiceProfileCir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(256,1238272))
_OnuTcontServiceProfileCir_Type.__name__=_D
_OnuTcontServiceProfileCir_Object=MibTableColumn
onuTcontServiceProfileCir=_OnuTcontServiceProfileCir_Object((1,3,6,1,4,1,3320,10,6,2,1,5),_OnuTcontServiceProfileCir_Type())
onuTcontServiceProfileCir.setMaxAccess(_C)
if mibBuilder.loadTexts:onuTcontServiceProfileCir.setStatus(_A)
class _OnuTcontServiceProfilePir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(512,1244160))
_OnuTcontServiceProfilePir_Type.__name__=_D
_OnuTcontServiceProfilePir_Object=MibTableColumn
onuTcontServiceProfilePir=_OnuTcontServiceProfilePir_Object((1,3,6,1,4,1,3320,10,6,2,1,6),_OnuTcontServiceProfilePir_Type())
onuTcontServiceProfilePir.setMaxAccess(_C)
if mibBuilder.loadTexts:onuTcontServiceProfilePir.setStatus(_A)
_OnuTcontServiceProfileRowStatus_Type=RowStatus
_OnuTcontServiceProfileRowStatus_Object=MibTableColumn
onuTcontServiceProfileRowStatus=_OnuTcontServiceProfileRowStatus_Object((1,3,6,1,4,1,3320,10,6,2,1,7),_OnuTcontServiceProfileRowStatus_Type())
onuTcontServiceProfileRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:onuTcontServiceProfileRowStatus.setStatus(_A)
_OnuBandwidthProfileTable_Object=MibTable
onuBandwidthProfileTable=_OnuBandwidthProfileTable_Object((1,3,6,1,4,1,3320,10,6,3))
if mibBuilder.loadTexts:onuBandwidthProfileTable.setStatus(_A)
_OnuBandwidthProfileEntry_Object=MibTableRow
onuBandwidthProfileEntry=_OnuBandwidthProfileEntry_Object((1,3,6,1,4,1,3320,10,6,3,1))
onuBandwidthProfileEntry.setIndexNames((0,_E,_A0))
if mibBuilder.loadTexts:onuBandwidthProfileEntry.setStatus(_A)
_OnuBandwidthProfileIndex_Type=Integer32
_OnuBandwidthProfileIndex_Object=MibTableColumn
onuBandwidthProfileIndex=_OnuBandwidthProfileIndex_Object((1,3,6,1,4,1,3320,10,6,3,1,1),_OnuBandwidthProfileIndex_Type())
onuBandwidthProfileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:onuBandwidthProfileIndex.setStatus(_A)
_OnuBandwidthProfileName_Type=OctetString
_OnuBandwidthProfileName_Object=MibTableColumn
onuBandwidthProfileName=_OnuBandwidthProfileName_Object((1,3,6,1,4,1,3320,10,6,3,1,2),_OnuBandwidthProfileName_Type())
onuBandwidthProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:onuBandwidthProfileName.setStatus(_A)
class _OnuBandwidthProfileTcontType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('type1',1),('type2',2),('type3',3),('type4',4),('type5',5)))
_OnuBandwidthProfileTcontType_Type.__name__=_D
_OnuBandwidthProfileTcontType_Object=MibTableColumn
onuBandwidthProfileTcontType=_OnuBandwidthProfileTcontType_Object((1,3,6,1,4,1,3320,10,6,3,1,3),_OnuBandwidthProfileTcontType_Type())
onuBandwidthProfileTcontType.setMaxAccess(_C)
if mibBuilder.loadTexts:onuBandwidthProfileTcontType.setStatus(_A)
class _OnuBandwidthProfileFixedBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(128,2500000))
_OnuBandwidthProfileFixedBandwidth_Type.__name__=_D
_OnuBandwidthProfileFixedBandwidth_Object=MibTableColumn
onuBandwidthProfileFixedBandwidth=_OnuBandwidthProfileFixedBandwidth_Object((1,3,6,1,4,1,3320,10,6,3,1,4),_OnuBandwidthProfileFixedBandwidth_Type())
onuBandwidthProfileFixedBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:onuBandwidthProfileFixedBandwidth.setStatus(_A)
class _OnuBandwidthProfileAssuredBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2500000))
_OnuBandwidthProfileAssuredBandwidth_Type.__name__=_D
_OnuBandwidthProfileAssuredBandwidth_Object=MibTableColumn
onuBandwidthProfileAssuredBandwidth=_OnuBandwidthProfileAssuredBandwidth_Object((1,3,6,1,4,1,3320,10,6,3,1,5),_OnuBandwidthProfileAssuredBandwidth_Type())
onuBandwidthProfileAssuredBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:onuBandwidthProfileAssuredBandwidth.setStatus(_A)
class _OnuBandwidthProfileMaximumBandwidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(128,2500000))
_OnuBandwidthProfileMaximumBandwidth_Type.__name__=_D
_OnuBandwidthProfileMaximumBandwidth_Object=MibTableColumn
onuBandwidthProfileMaximumBandwidth=_OnuBandwidthProfileMaximumBandwidth_Object((1,3,6,1,4,1,3320,10,6,3,1,6),_OnuBandwidthProfileMaximumBandwidth_Type())
onuBandwidthProfileMaximumBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:onuBandwidthProfileMaximumBandwidth.setStatus(_A)
_OnuBandwidthProfileRowStatus_Type=RowStatus
_OnuBandwidthProfileRowStatus_Object=MibTableColumn
onuBandwidthProfileRowStatus=_OnuBandwidthProfileRowStatus_Object((1,3,6,1,4,1,3320,10,6,3,1,7),_OnuBandwidthProfileRowStatus_Type())
onuBandwidthProfileRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:onuBandwidthProfileRowStatus.setStatus(_A)
_OnuTcontVirportBindProfileTable_Object=MibTable
onuTcontVirportBindProfileTable=_OnuTcontVirportBindProfileTable_Object((1,3,6,1,4,1,3320,10,6,4))
if mibBuilder.loadTexts:onuTcontVirportBindProfileTable.setStatus(_A)
_OnuTcontVirportBindProfileEntry_Object=MibTableRow
onuTcontVirportBindProfileEntry=_OnuTcontVirportBindProfileEntry_Object((1,3,6,1,4,1,3320,10,6,4,1))
onuTcontVirportBindProfileEntry.setIndexNames((0,_E,_A1))
if mibBuilder.loadTexts:onuTcontVirportBindProfileEntry.setStatus(_A)
_OnuTcontVirportBindProfileIndex_Type=Integer32
_OnuTcontVirportBindProfileIndex_Object=MibTableColumn
onuTcontVirportBindProfileIndex=_OnuTcontVirportBindProfileIndex_Object((1,3,6,1,4,1,3320,10,6,4,1,1),_OnuTcontVirportBindProfileIndex_Type())
onuTcontVirportBindProfileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:onuTcontVirportBindProfileIndex.setStatus(_A)
_OnuTcontVirportBindProfileVirportIndex_Type=Integer32
_OnuTcontVirportBindProfileVirportIndex_Object=MibTableColumn
onuTcontVirportBindProfileVirportIndex=_OnuTcontVirportBindProfileVirportIndex_Object((1,3,6,1,4,1,3320,10,6,4,1,2),_OnuTcontVirportBindProfileVirportIndex_Type())
onuTcontVirportBindProfileVirportIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:onuTcontVirportBindProfileVirportIndex.setStatus(_A)
_OnuTcontVirportBindProfileName_Type=OctetString
_OnuTcontVirportBindProfileName_Object=MibTableColumn
onuTcontVirportBindProfileName=_OnuTcontVirportBindProfileName_Object((1,3,6,1,4,1,3320,10,6,4,1,3),_OnuTcontVirportBindProfileName_Type())
onuTcontVirportBindProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:onuTcontVirportBindProfileName.setStatus(_A)
_OnuTcontVirportBindProfileTcontID_Type=Integer32
_OnuTcontVirportBindProfileTcontID_Object=MibTableColumn
onuTcontVirportBindProfileTcontID=_OnuTcontVirportBindProfileTcontID_Object((1,3,6,1,4,1,3320,10,6,4,1,4),_OnuTcontVirportBindProfileTcontID_Type())
onuTcontVirportBindProfileTcontID.setMaxAccess(_C)
if mibBuilder.loadTexts:onuTcontVirportBindProfileTcontID.setStatus(_A)
_OnuTcontVirportBindProfileTcontServiceProfileID_Type=Integer32
_OnuTcontVirportBindProfileTcontServiceProfileID_Object=MibTableColumn
onuTcontVirportBindProfileTcontServiceProfileID=_OnuTcontVirportBindProfileTcontServiceProfileID_Object((1,3,6,1,4,1,3320,10,6,4,1,5),_OnuTcontVirportBindProfileTcontServiceProfileID_Type())
onuTcontVirportBindProfileTcontServiceProfileID.setMaxAccess(_C)
if mibBuilder.loadTexts:onuTcontVirportBindProfileTcontServiceProfileID.setStatus(_A)
_OnuTcontVirportBindProfileVirportServiceProfileID_Type=Integer32
_OnuTcontVirportBindProfileVirportServiceProfileID_Object=MibTableColumn
onuTcontVirportBindProfileVirportServiceProfileID=_OnuTcontVirportBindProfileVirportServiceProfileID_Object((1,3,6,1,4,1,3320,10,6,4,1,6),_OnuTcontVirportBindProfileVirportServiceProfileID_Type())
onuTcontVirportBindProfileVirportServiceProfileID.setMaxAccess(_C)
if mibBuilder.loadTexts:onuTcontVirportBindProfileVirportServiceProfileID.setStatus(_A)
_OnuTcontVirportBindProfileRowStatus_Type=RowStatus
_OnuTcontVirportBindProfileRowStatus_Object=MibTableColumn
onuTcontVirportBindProfileRowStatus=_OnuTcontVirportBindProfileRowStatus_Object((1,3,6,1,4,1,3320,10,6,4,1,7),_OnuTcontVirportBindProfileRowStatus_Type())
onuTcontVirportBindProfileRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:onuTcontVirportBindProfileRowStatus.setStatus(_A)
_OnuVirtualPortServiceProfileTable_Object=MibTable
onuVirtualPortServiceProfileTable=_OnuVirtualPortServiceProfileTable_Object((1,3,6,1,4,1,3320,10,6,5))
if mibBuilder.loadTexts:onuVirtualPortServiceProfileTable.setStatus(_A)
_OnuVirtualPortServiceProfileEntry_Object=MibTableRow
onuVirtualPortServiceProfileEntry=_OnuVirtualPortServiceProfileEntry_Object((1,3,6,1,4,1,3320,10,6,5,1))
onuVirtualPortServiceProfileEntry.setIndexNames((0,_E,_A2))
if mibBuilder.loadTexts:onuVirtualPortServiceProfileEntry.setStatus(_A)
_OnuVirportProfileIndex_Type=Integer32
_OnuVirportProfileIndex_Object=MibTableColumn
onuVirportProfileIndex=_OnuVirportProfileIndex_Object((1,3,6,1,4,1,3320,10,6,5,1,1),_OnuVirportProfileIndex_Type())
onuVirportProfileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVirportProfileIndex.setStatus(_A)
_OnuVirportProfileName_Type=OctetString
_OnuVirportProfileName_Object=MibTableColumn
onuVirportProfileName=_OnuVirportProfileName_Object((1,3,6,1,4,1,3320,10,6,5,1,2),_OnuVirportProfileName_Type())
onuVirportProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVirportProfileName.setStatus(_A)
_OnuVirportProfileUsTrafficMapType_Type=Integer32
_OnuVirportProfileUsTrafficMapType_Object=MibTableColumn
onuVirportProfileUsTrafficMapType=_OnuVirportProfileUsTrafficMapType_Object((1,3,6,1,4,1,3320,10,6,5,1,3),_OnuVirportProfileUsTrafficMapType_Type())
onuVirportProfileUsTrafficMapType.setMaxAccess(_B)
if mibBuilder.loadTexts:onuVirportProfileUsTrafficMapType.setStatus(_A)
class _OnuVirportProfileTypeOfService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('data',1),('iptv',2),('video-on-demand',3),('voip',4),('ti',5),('e1',6),('hpna',7),('others',8)))
_OnuVirportProfileTypeOfService_Type.__name__=_D
_OnuVirportProfileTypeOfService_Object=MibTableColumn
onuVirportProfileTypeOfService=_OnuVirportProfileTypeOfService_Object((1,3,6,1,4,1,3320,10,6,5,1,4),_OnuVirportProfileTypeOfService_Type())
onuVirportProfileTypeOfService.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVirportProfileTypeOfService.setStatus(_A)
class _OnuVirportProfileEncrypMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_OnuVirportProfileEncrypMode_Type.__name__=_D
_OnuVirportProfileEncrypMode_Object=MibTableColumn
onuVirportProfileEncrypMode=_OnuVirportProfileEncrypMode_Object((1,3,6,1,4,1,3320,10,6,5,1,5),_OnuVirportProfileEncrypMode_Type())
onuVirportProfileEncrypMode.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVirportProfileEncrypMode.setStatus(_A)
_OnuVirportProfileUsBwProID_Type=Integer32
_OnuVirportProfileUsBwProID_Object=MibTableColumn
onuVirportProfileUsBwProID=_OnuVirportProfileUsBwProID_Object((1,3,6,1,4,1,3320,10,6,5,1,6),_OnuVirportProfileUsBwProID_Type())
onuVirportProfileUsBwProID.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVirportProfileUsBwProID.setStatus(_A)
class _OnuVirportProfileUsFlowPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_OnuVirportProfileUsFlowPriority_Type.__name__=_D
_OnuVirportProfileUsFlowPriority_Object=MibTableColumn
onuVirportProfileUsFlowPriority=_OnuVirportProfileUsFlowPriority_Object((1,3,6,1,4,1,3320,10,6,5,1,7),_OnuVirportProfileUsFlowPriority_Type())
onuVirportProfileUsFlowPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVirportProfileUsFlowPriority.setStatus(_A)
class _OnuVirportProfileUsFlowWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OnuVirportProfileUsFlowWeight_Type.__name__=_D
_OnuVirportProfileUsFlowWeight_Object=MibTableColumn
onuVirportProfileUsFlowWeight=_OnuVirportProfileUsFlowWeight_Object((1,3,6,1,4,1,3320,10,6,5,1,8),_OnuVirportProfileUsFlowWeight_Type())
onuVirportProfileUsFlowWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVirportProfileUsFlowWeight.setStatus(_A)
_OnuVirportProfileUsRateCtlSchedulerProID_Type=Integer32
_OnuVirportProfileUsRateCtlSchedulerProID_Object=MibTableColumn
onuVirportProfileUsRateCtlSchedulerProID=_OnuVirportProfileUsRateCtlSchedulerProID_Object((1,3,6,1,4,1,3320,10,6,5,1,9),_OnuVirportProfileUsRateCtlSchedulerProID_Type())
onuVirportProfileUsRateCtlSchedulerProID.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVirportProfileUsRateCtlSchedulerProID.setStatus(_A)
_OnuVirportProfileDsBwProID_Type=Integer32
_OnuVirportProfileDsBwProID_Object=MibTableColumn
onuVirportProfileDsBwProID=_OnuVirportProfileDsBwProID_Object((1,3,6,1,4,1,3320,10,6,5,1,10),_OnuVirportProfileDsBwProID_Type())
onuVirportProfileDsBwProID.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVirportProfileDsBwProID.setStatus(_A)
class _OnuVirportProfileDsQueueSchType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_a,0),('flow-based-priority-controlled',1)))
_OnuVirportProfileDsQueueSchType_Type.__name__=_D
_OnuVirportProfileDsQueueSchType_Object=MibTableColumn
onuVirportProfileDsQueueSchType=_OnuVirportProfileDsQueueSchType_Object((1,3,6,1,4,1,3320,10,6,5,1,11),_OnuVirportProfileDsQueueSchType_Type())
onuVirportProfileDsQueueSchType.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVirportProfileDsQueueSchType.setStatus(_A)
class _OnuVirportProfileDsFlowPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_OnuVirportProfileDsFlowPriority_Type.__name__=_D
_OnuVirportProfileDsFlowPriority_Object=MibTableColumn
onuVirportProfileDsFlowPriority=_OnuVirportProfileDsFlowPriority_Object((1,3,6,1,4,1,3320,10,6,5,1,12),_OnuVirportProfileDsFlowPriority_Type())
onuVirportProfileDsFlowPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:onuVirportProfileDsFlowPriority.setStatus(_A)
_OnuVirportProfileRowStatus_Type=RowStatus
_OnuVirportProfileRowStatus_Object=MibTableColumn
onuVirportProfileRowStatus=_OnuVirportProfileRowStatus_Object((1,3,6,1,4,1,3320,10,6,5,1,13),_OnuVirportProfileRowStatus_Type())
onuVirportProfileRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:onuVirportProfileRowStatus.setStatus(_A)
_OnuFlowProfileTable_Object=MibTable
onuFlowProfileTable=_OnuFlowProfileTable_Object((1,3,6,1,4,1,3320,10,6,6))
if mibBuilder.loadTexts:onuFlowProfileTable.setStatus(_A)
_OnuFlowProfileEntry_Object=MibTableRow
onuFlowProfileEntry=_OnuFlowProfileEntry_Object((1,3,6,1,4,1,3320,10,6,6,1))
onuFlowProfileEntry.setIndexNames((0,_E,_A3),(0,_E,_A4))
if mibBuilder.loadTexts:onuFlowProfileEntry.setStatus(_A)
_OnuFlowProfileIndex1_Type=Integer32
_OnuFlowProfileIndex1_Object=MibTableColumn
onuFlowProfileIndex1=_OnuFlowProfileIndex1_Object((1,3,6,1,4,1,3320,10,6,6,1,1),_OnuFlowProfileIndex1_Type())
onuFlowProfileIndex1.setMaxAccess(_B)
if mibBuilder.loadTexts:onuFlowProfileIndex1.setStatus(_A)
_OnuFlowProfileIndex2_Type=Integer32
_OnuFlowProfileIndex2_Object=MibTableColumn
onuFlowProfileIndex2=_OnuFlowProfileIndex2_Object((1,3,6,1,4,1,3320,10,6,6,1,2),_OnuFlowProfileIndex2_Type())
onuFlowProfileIndex2.setMaxAccess(_B)
if mibBuilder.loadTexts:onuFlowProfileIndex2.setStatus(_A)
_OnuFlowProfileName_Type=OctetString
_OnuFlowProfileName_Object=MibTableColumn
onuFlowProfileName=_OnuFlowProfileName_Object((1,3,6,1,4,1,3320,10,6,6,1,3),_OnuFlowProfileName_Type())
onuFlowProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:onuFlowProfileName.setStatus(_A)
class _OnuFlowProfileUniType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ethernet-uni',1),('pots-uni',2),('t1',3),('e1',4),('hpna',5),('ip-host',6)))
_OnuFlowProfileUniType_Type.__name__=_D
_OnuFlowProfileUniType_Object=MibTableColumn
onuFlowProfileUniType=_OnuFlowProfileUniType_Object((1,3,6,1,4,1,3320,10,6,6,1,4),_OnuFlowProfileUniType_Type())
onuFlowProfileUniType.setMaxAccess(_C)
if mibBuilder.loadTexts:onuFlowProfileUniType.setStatus(_A)
_OnuFlowProfileUniPortBitMap_Type=Integer32
_OnuFlowProfileUniPortBitMap_Object=MibTableColumn
onuFlowProfileUniPortBitMap=_OnuFlowProfileUniPortBitMap_Object((1,3,6,1,4,1,3320,10,6,6,1,5),_OnuFlowProfileUniPortBitMap_Type())
onuFlowProfileUniPortBitMap.setMaxAccess(_C)
if mibBuilder.loadTexts:onuFlowProfileUniPortBitMap.setStatus(_A)
class _OnuFlowProfileUsMapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('user-port',1),('vlan-id',2),('pbit',3),('vlan-id-pbit',4),('ehter-type',5),('dscp',6),('user-port-pbits',7),('user-port-dscp',8)))
_OnuFlowProfileUsMapType_Type.__name__=_D
_OnuFlowProfileUsMapType_Object=MibTableColumn
onuFlowProfileUsMapType=_OnuFlowProfileUsMapType_Object((1,3,6,1,4,1,3320,10,6,6,1,6),_OnuFlowProfileUsMapType_Type())
onuFlowProfileUsMapType.setMaxAccess(_C)
if mibBuilder.loadTexts:onuFlowProfileUsMapType.setStatus(_A)
class _OnuFlowProfileVlanIdStart_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_OnuFlowProfileVlanIdStart_Type.__name__=_D
_OnuFlowProfileVlanIdStart_Object=MibTableColumn
onuFlowProfileVlanIdStart=_OnuFlowProfileVlanIdStart_Object((1,3,6,1,4,1,3320,10,6,6,1,7),_OnuFlowProfileVlanIdStart_Type())
onuFlowProfileVlanIdStart.setMaxAccess(_C)
if mibBuilder.loadTexts:onuFlowProfileVlanIdStart.setStatus(_A)
class _OnuFlowProfileVlanIdStop_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_OnuFlowProfileVlanIdStop_Type.__name__=_D
_OnuFlowProfileVlanIdStop_Object=MibTableColumn
onuFlowProfileVlanIdStop=_OnuFlowProfileVlanIdStop_Object((1,3,6,1,4,1,3320,10,6,6,1,8),_OnuFlowProfileVlanIdStop_Type())
onuFlowProfileVlanIdStop.setMaxAccess(_C)
if mibBuilder.loadTexts:onuFlowProfileVlanIdStop.setStatus(_A)
_OnuFlowProfilePBITsMap_Type=Integer32
_OnuFlowProfilePBITsMap_Object=MibTableColumn
onuFlowProfilePBITsMap=_OnuFlowProfilePBITsMap_Object((1,3,6,1,4,1,3320,10,6,6,1,9),_OnuFlowProfilePBITsMap_Type())
onuFlowProfilePBITsMap.setMaxAccess(_C)
if mibBuilder.loadTexts:onuFlowProfilePBITsMap.setStatus(_A)
_OnuFlowProfileVirportNo_Type=Integer32
_OnuFlowProfileVirportNo_Object=MibTableColumn
onuFlowProfileVirportNo=_OnuFlowProfileVirportNo_Object((1,3,6,1,4,1,3320,10,6,6,1,10),_OnuFlowProfileVirportNo_Type())
onuFlowProfileVirportNo.setMaxAccess(_C)
if mibBuilder.loadTexts:onuFlowProfileVirportNo.setStatus(_A)
_OnuFlowProfileRowStatus_Type=RowStatus
_OnuFlowProfileRowStatus_Object=MibTableColumn
onuFlowProfileRowStatus=_OnuFlowProfileRowStatus_Object((1,3,6,1,4,1,3320,10,6,6,1,11),_OnuFlowProfileRowStatus_Type())
onuFlowProfileRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:onuFlowProfileRowStatus.setStatus(_A)
_OnuRateControlSchedulerProfileTable_Object=MibTable
onuRateControlSchedulerProfileTable=_OnuRateControlSchedulerProfileTable_Object((1,3,6,1,4,1,3320,10,6,7))
if mibBuilder.loadTexts:onuRateControlSchedulerProfileTable.setStatus(_A)
_OnuRateControlSchedulerProfileEntry_Object=MibTableRow
onuRateControlSchedulerProfileEntry=_OnuRateControlSchedulerProfileEntry_Object((1,3,6,1,4,1,3320,10,6,7,1))
onuRateControlSchedulerProfileEntry.setIndexNames((0,_E,_A5))
if mibBuilder.loadTexts:onuRateControlSchedulerProfileEntry.setStatus(_A)
_OnuRateCtlProfileIndex_Type=Integer32
_OnuRateCtlProfileIndex_Object=MibTableColumn
onuRateCtlProfileIndex=_OnuRateCtlProfileIndex_Object((1,3,6,1,4,1,3320,10,6,7,1,1),_OnuRateCtlProfileIndex_Type())
onuRateCtlProfileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:onuRateCtlProfileIndex.setStatus(_A)
_OnuRateCtlProfileName_Type=OctetString
_OnuRateCtlProfileName_Object=MibTableColumn
onuRateCtlProfileName=_OnuRateCtlProfileName_Object((1,3,6,1,4,1,3320,10,6,7,1,2),_OnuRateCtlProfileName_Type())
onuRateCtlProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:onuRateCtlProfileName.setStatus(_A)
_OnuRateCtlProfileCir_Type=Integer32
_OnuRateCtlProfileCir_Object=MibTableColumn
onuRateCtlProfileCir=_OnuRateCtlProfileCir_Object((1,3,6,1,4,1,3320,10,6,7,1,3),_OnuRateCtlProfileCir_Type())
onuRateCtlProfileCir.setMaxAccess(_C)
if mibBuilder.loadTexts:onuRateCtlProfileCir.setStatus(_A)
class _OnuRateCtlProfilePir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(128,2500000))
_OnuRateCtlProfilePir_Type.__name__=_D
_OnuRateCtlProfilePir_Object=MibTableColumn
onuRateCtlProfilePir=_OnuRateCtlProfilePir_Object((1,3,6,1,4,1,3320,10,6,7,1,4),_OnuRateCtlProfilePir_Type())
onuRateCtlProfilePir.setMaxAccess(_C)
if mibBuilder.loadTexts:onuRateCtlProfilePir.setStatus(_A)
class _OnuRateCtlProfileScheduleWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_OnuRateCtlProfileScheduleWeight_Type.__name__=_D
_OnuRateCtlProfileScheduleWeight_Object=MibTableColumn
onuRateCtlProfileScheduleWeight=_OnuRateCtlProfileScheduleWeight_Object((1,3,6,1,4,1,3320,10,6,7,1,5),_OnuRateCtlProfileScheduleWeight_Type())
onuRateCtlProfileScheduleWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:onuRateCtlProfileScheduleWeight.setStatus(_A)
_OnuRateCtlProfileRowStatus_Type=RowStatus
_OnuRateCtlProfileRowStatus_Object=MibTableColumn
onuRateCtlProfileRowStatus=_OnuRateCtlProfileRowStatus_Object((1,3,6,1,4,1,3320,10,6,7,1,6),_OnuRateCtlProfileRowStatus_Type())
onuRateCtlProfileRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:onuRateCtlProfileRowStatus.setStatus(_A)
_OnuEthernetUNIConfigProfileTable_Object=MibTable
onuEthernetUNIConfigProfileTable=_OnuEthernetUNIConfigProfileTable_Object((1,3,6,1,4,1,3320,10,6,8))
if mibBuilder.loadTexts:onuEthernetUNIConfigProfileTable.setStatus(_A)
_OnuEthernetUNIConfigProfileEntry_Object=MibTableRow
onuEthernetUNIConfigProfileEntry=_OnuEthernetUNIConfigProfileEntry_Object((1,3,6,1,4,1,3320,10,6,8,1))
onuEthernetUNIConfigProfileEntry.setIndexNames((0,_E,_A6))
if mibBuilder.loadTexts:onuEthernetUNIConfigProfileEntry.setStatus(_A)
_OnuEthernetUNIPortProfileIndex_Type=Integer32
_OnuEthernetUNIPortProfileIndex_Object=MibTableColumn
onuEthernetUNIPortProfileIndex=_OnuEthernetUNIPortProfileIndex_Object((1,3,6,1,4,1,3320,10,6,8,1,1),_OnuEthernetUNIPortProfileIndex_Type())
onuEthernetUNIPortProfileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:onuEthernetUNIPortProfileIndex.setStatus(_A)
_OnuEthernetUNIPortProfileName_Type=OctetString
_OnuEthernetUNIPortProfileName_Object=MibTableColumn
onuEthernetUNIPortProfileName=_OnuEthernetUNIPortProfileName_Object((1,3,6,1,4,1,3320,10,6,8,1,2),_OnuEthernetUNIPortProfileName_Type())
onuEthernetUNIPortProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:onuEthernetUNIPortProfileName.setStatus(_A)
class _OnuEthernetUNIPortAutoNegotiation_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_F,2)))
_OnuEthernetUNIPortAutoNegotiation_Type.__name__=_D
_OnuEthernetUNIPortAutoNegotiation_Object=MibTableColumn
onuEthernetUNIPortAutoNegotiation=_OnuEthernetUNIPortAutoNegotiation_Object((1,3,6,1,4,1,3320,10,6,8,1,3),_OnuEthernetUNIPortAutoNegotiation_Type())
onuEthernetUNIPortAutoNegotiation.setMaxAccess(_C)
if mibBuilder.loadTexts:onuEthernetUNIPortAutoNegotiation.setStatus(_A)
class _OnuEthernetUNIPortSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_N,0),('s10Mbps',1),('s100Mbps',2),('s1000Mbps',3)))
_OnuEthernetUNIPortSpeed_Type.__name__=_D
_OnuEthernetUNIPortSpeed_Object=MibTableColumn
onuEthernetUNIPortSpeed=_OnuEthernetUNIPortSpeed_Object((1,3,6,1,4,1,3320,10,6,8,1,4),_OnuEthernetUNIPortSpeed_Type())
onuEthernetUNIPortSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:onuEthernetUNIPortSpeed.setStatus(_A)
class _OnuEthernetUNIPortDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_N,0),('full',1),('half',2)))
_OnuEthernetUNIPortDuplex_Type.__name__=_D
_OnuEthernetUNIPortDuplex_Object=MibTableColumn
onuEthernetUNIPortDuplex=_OnuEthernetUNIPortDuplex_Object((1,3,6,1,4,1,3320,10,6,8,1,5),_OnuEthernetUNIPortDuplex_Type())
onuEthernetUNIPortDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:onuEthernetUNIPortDuplex.setStatus(_A)
_OnuEthernetUNIPortExpectedType_Type=Integer32
_OnuEthernetUNIPortExpectedType_Object=MibTableColumn
onuEthernetUNIPortExpectedType=_OnuEthernetUNIPortExpectedType_Object((1,3,6,1,4,1,3320,10,6,8,1,6),_OnuEthernetUNIPortExpectedType_Type())
onuEthernetUNIPortExpectedType.setMaxAccess(_C)
if mibBuilder.loadTexts:onuEthernetUNIPortExpectedType.setStatus(_A)
class _OnuEthernetUNIPortMaxFrameSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1500,2048))
_OnuEthernetUNIPortMaxFrameSize_Type.__name__=_D
_OnuEthernetUNIPortMaxFrameSize_Object=MibTableColumn
onuEthernetUNIPortMaxFrameSize=_OnuEthernetUNIPortMaxFrameSize_Object((1,3,6,1,4,1,3320,10,6,8,1,7),_OnuEthernetUNIPortMaxFrameSize_Type())
onuEthernetUNIPortMaxFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:onuEthernetUNIPortMaxFrameSize.setStatus(_A)
class _OnuEthernetUNIPortEthernetInterfaceWiring_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('dce',0),('dte',1),(_N,2)))
_OnuEthernetUNIPortEthernetInterfaceWiring_Type.__name__=_D
_OnuEthernetUNIPortEthernetInterfaceWiring_Object=MibTableColumn
onuEthernetUNIPortEthernetInterfaceWiring=_OnuEthernetUNIPortEthernetInterfaceWiring_Object((1,3,6,1,4,1,3320,10,6,8,1,8),_OnuEthernetUNIPortEthernetInterfaceWiring_Type())
onuEthernetUNIPortEthernetInterfaceWiring.setMaxAccess(_C)
if mibBuilder.loadTexts:onuEthernetUNIPortEthernetInterfaceWiring.setStatus(_A)
_OnuEthernetUNIPortProfileRowStatus_Type=RowStatus
_OnuEthernetUNIPortProfileRowStatus_Object=MibTableColumn
onuEthernetUNIPortProfileRowStatus=_OnuEthernetUNIPortProfileRowStatus_Object((1,3,6,1,4,1,3320,10,6,8,1,9),_OnuEthernetUNIPortProfileRowStatus_Type())
onuEthernetUNIPortProfileRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:onuEthernetUNIPortProfileRowStatus.setStatus(_A)
gponOltPonSfpParameterAlarmNotification=NotificationType((1,3,6,1,4,1,3320,10,2,5,2))
gponOltPonSfpParameterAlarmNotification.setObjects(*((_I,_M),(_I,_L),(_E,_A7),(_E,_A8),(_E,_A9),(_E,_AA),(_E,_AB)))
if mibBuilder.loadTexts:gponOltPonSfpParameterAlarmNotification.setStatus(_P)
gponOnuSfpParameterAlarmNotification=NotificationType((1,3,6,1,4,1,3320,10,3,6,3))
gponOnuSfpParameterAlarmNotification.setObjects(*((_I,_M),(_I,_L),(_E,_Q),(_E,_AC),(_E,_AD),(_E,_AE)))
if mibBuilder.loadTexts:gponOnuSfpParameterAlarmNotification.setStatus(_P)
gponOnuStatusChangeNotification=NotificationType((1,3,6,1,4,1,3320,10,3,7,2))
gponOnuStatusChangeNotification.setObjects(*((_I,_M),(_I,_L),(_E,_Q),(_E,_AF),(_E,_AG),(_E,_AH)))
if mibBuilder.loadTexts:gponOnuStatusChangeNotification.setStatus(_P)
gponOnuDyingGaspNotification=NotificationType((1,3,6,1,4,1,3320,10,3,8,2))
gponOnuDyingGaspNotification.setObjects(*((_I,_M),(_I,_L),(_E,_Q),(_E,_AI)))
if mibBuilder.loadTexts:gponOnuDyingGaspNotification.setStatus(_P)
mibBuilder.exportSymbols(_E,**{'nmsGponMIB':nmsGponMIB,'nmsGponOltObj':nmsGponOltObj,'gponOltConfigTable':gponOltConfigTable,'gponOltConfigEntry':gponOltConfigEntry,'gponOnuAuthenticationMode':gponOnuAuthenticationMode,'gponBroadcastGEMPort':gponBroadcastGEMPort,'gponEncryption':gponEncryption,'gponKeyExchangeInterval':gponKeyExchangeInterval,'nmsGponOltPonPortObj':nmsGponOltPonPortObj,'gponOltPonPortConfigTable':gponOltPonPortConfigTable,'gponOltPonPortConfigEntry':gponOltPonPortConfigEntry,_R:gponOltPonPortPortIndex,'gponOltPonPortPortAdminStatus':gponOltPonPortPortAdminStatus,'gponOltPonPortOnuDiscoveryMode':gponOltPonPortOnuDiscoveryMode,'gponOltPonPortPortActiveOnuNum':gponOltPonPortPortActiveOnuNum,'gponOltPonPortPortInactiveOnuNum':gponOltPonPortPortInactiveOnuNum,'gponOltPonPortPortLlidIfIndexString':gponOltPonPortPortLlidIfIndexString,'gponOltPonPortOpticalParameterTable':gponOltPonPortOpticalParameterTable,'gponOltPonPortOpticalParameterEntry':gponOltPonPortOpticalParameterEntry,_U:gponOltPonPortOpticalParameterPortIndex,_A8:gponOltPonPortOpticalParameterTemperature,_A9:gponOltPonPortOpticalParameterVoltage,_AA:gponOltPonPortOpticalParameterCurrent,_AB:gponOltPonPortOpticalParameterTxPower,'gponOltPonPortOpticalRxPowerTable':gponOltPonPortOpticalRxPowerTable,'gponOltPonPortOpticalRxPowerEntry':gponOltPonPortOpticalRxPowerEntry,_V:gponOltPonPortOpticalRxPowerPortIndex,'gponOltPonPortOpticalRxPowerLinkStatus':gponOltPonPortOpticalRxPowerLinkStatus,'gponOltPonPortOpticalRxPowerRxPower':gponOltPonPortOpticalRxPowerRxPower,'gponOltPonPortOpticalParameterAlarmTable':gponOltPonPortOpticalParameterAlarmTable,'gponOltPonPortOpticalParameterAlarmEntry':gponOltPonPortOpticalParameterAlarmEntry,_W:gponOltPonPortPowerAlarmIndex,'gponOltPonPortTxPowerAlarmUpLimitEnable':gponOltPonPortTxPowerAlarmUpLimitEnable,'gponOltPonPortTxPowerAlarmUpLimitThreshold':gponOltPonPortTxPowerAlarmUpLimitThreshold,'gponOltPonPortTxPowerAlarmUpLimitClearThreshold':gponOltPonPortTxPowerAlarmUpLimitClearThreshold,'gponOltPonPortTxPowerAlarmLowLimitEnable':gponOltPonPortTxPowerAlarmLowLimitEnable,'gponOltPonPortTxPowerAlarmLowLimitThreshold':gponOltPonPortTxPowerAlarmLowLimitThreshold,'gponOltPonPortTxPowerAlarmLowLimitClearThreshold':gponOltPonPortTxPowerAlarmLowLimitClearThreshold,'gponOltPonPortTemperatureAlarmUpLimitEnable':gponOltPonPortTemperatureAlarmUpLimitEnable,'gponOltPonPortTemperatureAlarmUpLimitThreshold':gponOltPonPortTemperatureAlarmUpLimitThreshold,'gponOltPonPortTemperatureAlarmUpLimitClearThreshold':gponOltPonPortTemperatureAlarmUpLimitClearThreshold,'gponOltPonPortTemperatureAlarmLowLimitEnable':gponOltPonPortTemperatureAlarmLowLimitEnable,'gponOltPonPortTemperatureAlarmLowLimitThreshold':gponOltPonPortTemperatureAlarmLowLimitThreshold,'gponOltPonPortTemperatureAlarmLowLimitClearThreshold':gponOltPonPortTemperatureAlarmLowLimitClearThreshold,'gponOltPonPortVoltageAlarmUpLimitEnable':gponOltPonPortVoltageAlarmUpLimitEnable,'gponOltPonPortVoltageAlarmUpLimitThreshold':gponOltPonPortVoltageAlarmUpLimitThreshold,'gponOltPonPortVoltageAlarmUpLimitClearThreshold':gponOltPonPortVoltageAlarmUpLimitClearThreshold,'gponOltPonPortVoltageAlarmLowLimitEnable':gponOltPonPortVoltageAlarmLowLimitEnable,'gponOltPonPortVoltageAlarmLowLimitThreshold':gponOltPonPortVoltageAlarmLowLimitThreshold,'gponOltPonPortVoltageAlarmLowLimitClearThreshold':gponOltPonPortVoltageAlarmLowLimitClearThreshold,'gponOltPonPortCurrentAlarmUpLimitEnable':gponOltPonPortCurrentAlarmUpLimitEnable,'gponOltPonPortCurrentAlarmUpLimitThreshold':gponOltPonPortCurrentAlarmUpLimitThreshold,'gponOltPonPortCurrentAlarmUpLimitClearThreshold':gponOltPonPortCurrentAlarmUpLimitClearThreshold,'gponOltPonPortCurrentAlarmLowLimitEnable':gponOltPonPortCurrentAlarmLowLimitEnable,'gponOltPonPortCurrentAlarmLowLimitThreshold':gponOltPonPortCurrentAlarmLowLimitThreshold,'gponOltPonPortCurrentAlarmLowLimitClearThreshold':gponOltPonPortCurrentAlarmLowLimitClearThreshold,'gponOltPonSfpParameterAlarmTrap':gponOltPonSfpParameterAlarmTrap,_A7:gponOltPonSfpParameterAlarmStatus,'gponOltPonSfpParameterAlarmNotification':gponOltPonSfpParameterAlarmNotification,'gponOltONUBindTable':gponOltONUBindTable,'gponOltONUBindEntry':gponOltONUBindEntry,_Y:gponOltONUBindPortIndex,'gponOltONUBindONUId':gponOltONUBindONUId,'gponOltONUBindSN':gponOltONUBindSN,'gponOltONUBindPassword':gponOltONUBindPassword,'gponOltONUBindRowStatus':gponOltONUBindRowStatus,'nmsGponONUObj':nmsGponONUObj,'gponOnuInfoTable':gponOnuInfoTable,'gponOnuInfoEntry':gponOnuInfoEntry,_Z:gponONUInfoDeviceIndex,_AF:onuVendorID,'onuVersion':onuVersion,_Q:onuSerialNum,'onuTrafficManagementOption':onuTrafficManagementOption,'onuBatteryBackup':onuBatteryBackup,'onuAdminState':onuAdminState,'onuOperationalState':onuOperationalState,_AG:onuEquipmentID,'onuOMCCVersion':onuOMCCVersion,'onuHardwareType':onuHardwareType,'onuHardwareRevision':onuHardwareRevision,'onuSecurityCapability':onuSecurityCapability,'onuSecurityMode':onuSecurityMode,'onuTotalPriorityQueueNumber':onuTotalPriorityQueueNumber,'onuTotalTrafficSchedulerNumber':onuTotalTrafficSchedulerNumber,'onuTotalGEMPortNumber':onuTotalGEMPortNumber,'onuTotalPOTSUNInumber':onuTotalPOTSUNInumber,'onuSysUpTime':onuSysUpTime,'onuImageInstance0Version':onuImageInstance0Version,'onuImageInstance0Valid':onuImageInstance0Valid,'onuImageInstance0Activate':onuImageInstance0Activate,'onuImageInstance0Commit':onuImageInstance0Commit,'onuImageInstance1Version':onuImageInstance1Version,'onuImageInstance1Valid':onuImageInstance1Valid,'onuImageInstance1Activate':onuImageInstance1Activate,'onuImageInstance1Commit':onuImageInstance1Commit,'onuInfoOonuMacAddress':onuInfoOonuMacAddress,'onuFastLeaveCapability':onuFastLeaveCapability,'onuPiggybackDbaRep':onuPiggybackDbaRep,'onuWholeOnuDbaRep':onuWholeOnuDbaRep,'onuProtectionMode':onuProtectionMode,'onuDistance':onuDistance,'onuSwdlState':onuSwdlState,'onuDeActiveReason':onuDeActiveReason,'gponOnuConfigTable':gponOnuConfigTable,'gponOnuConfigEntry':gponOnuConfigEntry,_d:gponOnuConfigDeviceIndex,'gponOnuConfigActicate':gponOnuConfigActicate,'gponOnuConfigEnable':gponOnuConfigEnable,'gponOnuConfigReboot':gponOnuConfigReboot,'gponOnuConfigEnablePM':gponOnuConfigEnablePM,'gponOnuConfigFlowProfileID':gponOnuConfigFlowProfileID,'gponOnuConfigTcontVirPortBindingProfileID':gponOnuConfigTcontVirPortBindingProfileID,'gponOnuConfigOnuProfileID':gponOnuConfigOnuProfileID,'gponOnuConfigUsMapProfileID':gponOnuConfigUsMapProfileID,'gponOnuStatusTable':gponOnuStatusTable,'gponOnuStatusEntry':gponOnuStatusEntry,_e:gponOnuStatusDeviceIndex,'gponOnuStatusOnuSn':gponOnuStatusOnuSn,'gponOnuStatusPonPortID':gponOnuStatusPonPortID,'gponOnuStatusOnuStatus':gponOnuStatusOnuStatus,'gponOnuOpticalPowerTable':gponOnuOpticalPowerTable,'gponOnuOpticalPowerEntry':gponOnuOpticalPowerEntry,_f:gponOnuOpticalPowerDeviceIndex,_AD:gponOnuOpticalPowerRxPower,_AE:gponOnuOpticalPowerTxPower,'gponOnuOpticalParameterAlarmTable':gponOnuOpticalParameterAlarmTable,'gponOnuOpticalParameterAlarmEntry':gponOnuOpticalParameterAlarmEntry,_g:gponOnuOpticalParameterAlarmDeviceIndex,'gponOnuOpticalTxPowerAlarmUpLimitEnable':gponOnuOpticalTxPowerAlarmUpLimitEnable,'gponOnuOpticalTxPowerAlarmUpLimitThreshold':gponOnuOpticalTxPowerAlarmUpLimitThreshold,'gponOnuOpticalTxPowerAlarmUpLimitClearThreshold':gponOnuOpticalTxPowerAlarmUpLimitClearThreshold,'gponOnuOpticalTxPowerAlarmUpLimitRowStatus':gponOnuOpticalTxPowerAlarmUpLimitRowStatus,'gponOnuOpticalTxPowerAlarmLowLimitEnable':gponOnuOpticalTxPowerAlarmLowLimitEnable,'gponOnuOpticalTxPowerAlarmLowLimitThreshold':gponOnuOpticalTxPowerAlarmLowLimitThreshold,'gponOnuOpticalTxPowerAlarmLowLimitClearThreshold':gponOnuOpticalTxPowerAlarmLowLimitClearThreshold,'gponOnuOpticalTxPowerAlarmLowLimitRowStatus':gponOnuOpticalTxPowerAlarmLowLimitRowStatus,'gponOnuOpticalRxPowerAlarmUpLimitEnable':gponOnuOpticalRxPowerAlarmUpLimitEnable,'gponOnuOpticalRxPowerAlarmUpLimitThreshold':gponOnuOpticalRxPowerAlarmUpLimitThreshold,'gponOnuOpticalRxPowerAlarmUpLimitClearThreshold':gponOnuOpticalRxPowerAlarmUpLimitClearThreshold,'gponOnuOpticalRxPowerAlarmUpLimitRowStatus':gponOnuOpticalRxPowerAlarmUpLimitRowStatus,'gponOnuOpticalRxPowerAlarmLowLimitEnable':gponOnuOpticalRxPowerAlarmLowLimitEnable,'gponOnuOpticalRxPowerAlarmLowLimitThreshold':gponOnuOpticalRxPowerAlarmLowLimitThreshold,'gponOnuOpticalRxPowerAlarmLowLimitClearThreshold':gponOnuOpticalRxPowerAlarmLowLimitClearThreshold,'gponOnuOpticalRxPowerAlarmLowLimitRowStatus':gponOnuOpticalRxPowerAlarmLowLimitRowStatus,'gponOnuSfpParameterAlarmTrap':gponOnuSfpParameterAlarmTrap,_AC:gponOnuSfpParameterAlarmStatus,'gponOnuSfpParameterAlarmThreshold':gponOnuSfpParameterAlarmThreshold,'gponOnuSfpParameterAlarmNotification':gponOnuSfpParameterAlarmNotification,'gponOnuStatusAlarmTrap':gponOnuStatusAlarmTrap,_AH:gponOnuStatusChange,'gponOnuStatusChangeNotification':gponOnuStatusChangeNotification,'gponOnuDyingGaspAlarmTrap':gponOnuDyingGaspAlarmTrap,_AI:gponOnuDyingGaspStatus,'gponOnuDyingGaspNotification':gponOnuDyingGaspNotification,'gponOnuBatchUpdateTable':gponOnuBatchUpdateTable,'gponOnuBatchUpdateEntry':gponOnuBatchUpdateEntry,_h:gponOnuBatchUpdateLLIDs,'gponOnuBatchUpdateFileName':gponOnuBatchUpdateFileName,'gponOnuBatchUpdateAction':gponOnuBatchUpdateAction,'gponOnuBatchUpdateResult':gponOnuBatchUpdateResult,'nmsGponUNIPortObj':nmsGponUNIPortObj,'onuUniPortConfigTable':onuUniPortConfigTable,'onuUniPortConfigEntry':onuUniPortConfigEntry,_i:onuUniPortConfigDeviceIndex,_j:onuUniPortConfigPortIndex,'onuUniPortConfigAdminState':onuUniPortConfigAdminState,'onuUniPortConfigOperationalState':onuUniPortConfigOperationalState,'onuUniPortConfigEthernetProfileID':onuUniPortConfigEthernetProfileID,'onuUniPortConfigOnuVLANTranslationProfileID':onuUniPortConfigOnuVLANTranslationProfileID,'onuUniPortConfigRowStatus':onuUniPortConfigRowStatus,'onuUniPortStatisticTable':onuUniPortStatisticTable,'onuUniPortStatisticEntry':onuUniPortStatisticEntry,_k:onuUniPortStatisticDeviceIndex,_l:onuUniPortStatisticUniPortIndex,'onuUniPortStatisticTime':onuUniPortStatisticTime,'onuUniPortStatisticRxTotalPackets':onuUniPortStatisticRxTotalPackets,'onuUniPortStatisticRxUnicastPackets':onuUniPortStatisticRxUnicastPackets,'onuUniPortStatisticRxMulticastPackets':onuUniPortStatisticRxMulticastPackets,'onuUniPortStatisticRxBroadcastPackets':onuUniPortStatisticRxBroadcastPackets,'onuUniPortStatisticRxDiscardedPackets':onuUniPortStatisticRxDiscardedPackets,'onuUniPortStatisticTxTotalPackets':onuUniPortStatisticTxTotalPackets,'onuUniPortStatisticTxUnicastPackets':onuUniPortStatisticTxUnicastPackets,'onuUniPortStatisticTxMulticastPackets':onuUniPortStatisticTxMulticastPackets,'onuUniPortStatisticTxBroadcastPackets':onuUniPortStatisticTxBroadcastPackets,'onuUniPortStatisticTxDiscardedPackets':onuUniPortStatisticTxDiscardedPackets,'onuUniPortStatisticRxUndersizePackets':onuUniPortStatisticRxUndersizePackets,'onuUniPortStatisticRxFragments':onuUniPortStatisticRxFragments,'onuUniPortStatisticRxJabbers':onuUniPortStatisticRxJabbers,'onuUniPortStatisticRxPackets64Octets':onuUniPortStatisticRxPackets64Octets,'onuUniPortStatisticRxPackets65to127Octets':onuUniPortStatisticRxPackets65to127Octets,'onuUniPortStatisticRxPackets128to255Octets':onuUniPortStatisticRxPackets128to255Octets,'onuUniPortStatisticRxPackets256to511Octets':onuUniPortStatisticRxPackets256to511Octets,'onuUniPortStatisticRxPackets512to1023Octets':onuUniPortStatisticRxPackets512to1023Octets,'onuUniPortStatisticRxPackets1024to1518Octets':onuUniPortStatisticRxPackets1024to1518Octets,'onuUniPortStatisticRxFcsErrors':onuUniPortStatisticRxFcsErrors,'onuUniPortStatisticTxFcsErrors':onuUniPortStatisticTxFcsErrors,'onuUniPortStatisticTxExcessiveCollisions':onuUniPortStatisticTxExcessiveCollisions,'onuUniPortStatisticTxLateCollisions':onuUniPortStatisticTxLateCollisions,'onuUniPortStatisticRxPacketsTooLong':onuUniPortStatisticRxPacketsTooLong,'onuUniPortStatisticRxBufferOverflows':onuUniPortStatisticRxBufferOverflows,'onuUniPortStatisticTxBufferOverflows':onuUniPortStatisticTxBufferOverflows,'onuUniPortStatisticTxSingleCollisionPackets':onuUniPortStatisticTxSingleCollisionPackets,'onuUniPortStatisticTxMultipleCollisionsPackets':onuUniPortStatisticTxMultipleCollisionsPackets,'onuUniPortStatisticSQEs':onuUniPortStatisticSQEs,'onuUniPortStatisticTxDeferredTransmissio':onuUniPortStatisticTxDeferredTransmissio,'onuUniPortStatisticTxInternalMACTransmitError':onuUniPortStatisticTxInternalMACTransmitError,'onuUniPortStatisticCarrierSenseError':onuUniPortStatisticCarrierSenseError,'onuUniPortStatisticRxAlignmentError':onuUniPortStatisticRxAlignmentError,'onuUniPortStatisticRxInternalMACReceiveError':onuUniPortStatisticRxInternalMACReceiveError,'onuUniPortStatisticRxOctets':onuUniPortStatisticRxOctets,'onuUniPortStatisticTxOctets':onuUniPortStatisticTxOctets,'onuUniPort15MinStatisticTable':onuUniPort15MinStatisticTable,'onuUniPort15MinStatisticEntry':onuUniPort15MinStatisticEntry,_m:onuUniPort15MinStatisticDeviceIndex,_n:onuUniPort15MinStatisticUniPortIndex,_o:onuUniPort15MinStatisticIntervalID,'onuUniPort15MinStatisticRxTotalPackets':onuUniPort15MinStatisticRxTotalPackets,'onuUniPort15MinStatisticRxUnicastPackets':onuUniPort15MinStatisticRxUnicastPackets,'onuUniPort15MinStatisticRxMulticastPackets':onuUniPort15MinStatisticRxMulticastPackets,'onuUniPort15MinStatisticRxBroadcastPackets':onuUniPort15MinStatisticRxBroadcastPackets,'onuUniPort15MinStatisticRxDiscardedPackets':onuUniPort15MinStatisticRxDiscardedPackets,'onuUniPort15MinStatisticTxTotalPackets':onuUniPort15MinStatisticTxTotalPackets,'onuUniPort15MinStatisticTxUnicastPackets':onuUniPort15MinStatisticTxUnicastPackets,'onuUniPort15MinStatisticTxMulticastPackets':onuUniPort15MinStatisticTxMulticastPackets,'onuUniPort15MinStatisticTxBroadcastPackets':onuUniPort15MinStatisticTxBroadcastPackets,'onuUniPort15MinStatisticTxDiscardedPackets':onuUniPort15MinStatisticTxDiscardedPackets,'onuUniPort15MinStatisticRxUndersizePackets':onuUniPort15MinStatisticRxUndersizePackets,'onuUniPort15MinStatisticRxFragments':onuUniPort15MinStatisticRxFragments,'onuUniPort15MinStatisticRxJabbers':onuUniPort15MinStatisticRxJabbers,'onuUniPort15MinStatisticRxPackets64Octets':onuUniPort15MinStatisticRxPackets64Octets,'onuUniPort15MinStatisticRxPackets65to127Octets':onuUniPort15MinStatisticRxPackets65to127Octets,'onuUniPort15MinStatisticRxPackets128to255Octets':onuUniPort15MinStatisticRxPackets128to255Octets,'onuUniPort15MinStatisticRxPackets256to511Octets':onuUniPort15MinStatisticRxPackets256to511Octets,'onuUniPort15MinStatisticRxPackets512to1023Octets':onuUniPort15MinStatisticRxPackets512to1023Octets,'onuUniPort15MinStatisticRxPackets1024to1518Octets':onuUniPort15MinStatisticRxPackets1024to1518Octets,'onuUniPort15MinStatisticRxFcsErrors':onuUniPort15MinStatisticRxFcsErrors,'onuUniPort15MinStatisticTxFcsErrors':onuUniPort15MinStatisticTxFcsErrors,'onuUniPort15MinStatisticTxExcessiveCollisions':onuUniPort15MinStatisticTxExcessiveCollisions,'onuUniPort15MinStatisticTxLateCollisions':onuUniPort15MinStatisticTxLateCollisions,'onuUniPort15MinStatisticRxPacketsTooLong':onuUniPort15MinStatisticRxPacketsTooLong,'onuUniPort15MinStatisticRxBufferOverflows':onuUniPort15MinStatisticRxBufferOverflows,'onuUniPort15MinStatisticTxBufferOverflows':onuUniPort15MinStatisticTxBufferOverflows,'onuUniPort15MinStatisticTxSingleCollisionPackets':onuUniPort15MinStatisticTxSingleCollisionPackets,'onuUniPort15MinStatisticTxMultipleCollisionsPackets':onuUniPort15MinStatisticTxMultipleCollisionsPackets,'onuUniPort15MinStatisticSQEs':onuUniPort15MinStatisticSQEs,'onuUniPort15MinStatisticTxDeferredTransmissio':onuUniPort15MinStatisticTxDeferredTransmissio,'onuUniPort15MinStatisticTxInternalMACTransmitError':onuUniPort15MinStatisticTxInternalMACTransmitError,'onuUniPort15MinStatisticCarrierSenseError':onuUniPort15MinStatisticCarrierSenseError,'onuUniPort15MinStatisticRxAlignmentError':onuUniPort15MinStatisticRxAlignmentError,'onuUniPort15MinStatisticRxInternalMACReceiveError':onuUniPort15MinStatisticRxInternalMACReceiveError,'onuUniPort15MinStatisticRxOctets':onuUniPort15MinStatisticRxOctets,'onuUniPort15MinStatisticTxOctets':onuUniPort15MinStatisticTxOctets,'nmsGponVirPortObj':nmsGponVirPortObj,'onuVirPortConfigTable':onuVirPortConfigTable,'onuVirPortConfigEntry':onuVirPortConfigEntry,_p:onuVirPortConfigDeviceIndex,_q:onuVirPortConfigPortIndex,'onuVirPortConfigTCONTID':onuVirPortConfigTCONTID,'onuVirPortConfigOltGEMPortID':onuVirPortConfigOltGEMPortID,'onuVirPortConfigOltAllocID':onuVirPortConfigOltAllocID,'onuVirPortConfigVirPortAdminState':onuVirPortConfigVirPortAdminState,'onuVirPortConfigEncryptionMode':onuVirPortConfigEncryptionMode,'onuVirPortConfigDownstreamRateLimit':onuVirPortConfigDownstreamRateLimit,'onuVirPortConfigOltVLANTranslationProfileID':onuVirPortConfigOltVLANTranslationProfileID,'onuVirPortConfigONUMacFilterProfileID':onuVirPortConfigONUMacFilterProfileID,'onuVirPortConfigONUMacFilterPreassignProfileID':onuVirPortConfigONUMacFilterPreassignProfileID,'onuVirPortConfigRowStatus':onuVirPortConfigRowStatus,'onuVirPortStatisticTable':onuVirPortStatisticTable,'onuVirPortStatisticEntry':onuVirPortStatisticEntry,_r:onuVirPortStatisticDeviceIndex,_s:onuVirPortStatisticVirPortIndex,'onuVirPortStatisticTime':onuVirPortStatisticTime,'onuVirPortStatisticRxTotalFrames':onuVirPortStatisticRxTotalFrames,'onuVirPortStatisticTxTotalFrames':onuVirPortStatisticTxTotalFrames,'onuVirPortStatisticRxTotalBytes':onuVirPortStatisticRxTotalBytes,'onuVirPortStatisticTxTotalBytes':onuVirPortStatisticTxTotalBytes,'onuVirPortStatisticEncryptKeyErrors':onuVirPortStatisticEncryptKeyErrors,'onuVirPort15MinStatisticTable':onuVirPort15MinStatisticTable,'onuVirPort15MinStatisticEntry':onuVirPort15MinStatisticEntry,_t:onuVirPort15MinStatisticDeviceIndex,_u:onuVirPort15MinStatisticVirPortIndex,_v:onuVirPort15MinStatisticIntervalID,'onuVirPort15MinStatisticRxTotalFrames':onuVirPort15MinStatisticRxTotalFrames,'onuVirPort15MinStatisticTxTotalFrames':onuVirPort15MinStatisticTxTotalFrames,'onuVirPort15MinStatisticRxTotalBytes':onuVirPort15MinStatisticRxTotalBytes,'onuVirPort15MinStatisticTxTotalBytes':onuVirPort15MinStatisticTxTotalBytes,'onuVirPort15MinStatisticEncryptKeyErrors':onuVirPort15MinStatisticEncryptKeyErrors,'nmsGponProfile':nmsGponProfile,'onuVLANProfile':onuVLANProfile,'onuVLANProfileTable':onuVLANProfileTable,'onuVLANProfileEntry':onuVLANProfileEntry,_w:onuVLANProfileIndex,'onuVLANProfileName':onuVLANProfileName,'onuVLANProfileVlanMode':onuVLANProfileVlanMode,'onuVLANProfilePVID':onuVLANProfilePVID,'onuVLANProfileTrunkVlans':onuVLANProfileTrunkVlans,'onuVLANProfileEtherTypeIPOEVlan':onuVLANProfileEtherTypeIPOEVlan,'onuVLANProfileEtherTypePPPOEVlan':onuVLANProfileEtherTypePPPOEVlan,'onuVLANProfileEtherTypeARPVlan':onuVLANProfileEtherTypeARPVlan,'onuVLANProfileRowStatus':onuVLANProfileRowStatus,'onuVLANTranslationTable':onuVLANTranslationTable,'onuVLANTranslationEntry':onuVLANTranslationEntry,_x:onuVLANTranslationIndex1,_y:onuVLANTranslationIndex2,'onuVLANTranslationName':onuVLANTranslationName,'onuVLANTranslationSrcVlan':onuVLANTranslationSrcVlan,'onuVLANTranslationDstVlan':onuVLANTranslationDstVlan,'onuVLANTranslationRowStatus':onuVLANTranslationRowStatus,'onuTCONTServiceProfileTable':onuTCONTServiceProfileTable,'onuTCONTServiceProfileEntry':onuTCONTServiceProfileEntry,_z:onuTcontServiceProfileIndex,'onuTcontServiceProfileName':onuTcontServiceProfileName,'onuTcontServiceProfileTcontType':onuTcontServiceProfileTcontType,'onuTcontServiceProfileFir':onuTcontServiceProfileFir,'onuTcontServiceProfileCir':onuTcontServiceProfileCir,'onuTcontServiceProfilePir':onuTcontServiceProfilePir,'onuTcontServiceProfileRowStatus':onuTcontServiceProfileRowStatus,'onuBandwidthProfileTable':onuBandwidthProfileTable,'onuBandwidthProfileEntry':onuBandwidthProfileEntry,_A0:onuBandwidthProfileIndex,'onuBandwidthProfileName':onuBandwidthProfileName,'onuBandwidthProfileTcontType':onuBandwidthProfileTcontType,'onuBandwidthProfileFixedBandwidth':onuBandwidthProfileFixedBandwidth,'onuBandwidthProfileAssuredBandwidth':onuBandwidthProfileAssuredBandwidth,'onuBandwidthProfileMaximumBandwidth':onuBandwidthProfileMaximumBandwidth,'onuBandwidthProfileRowStatus':onuBandwidthProfileRowStatus,'onuTcontVirportBindProfileTable':onuTcontVirportBindProfileTable,'onuTcontVirportBindProfileEntry':onuTcontVirportBindProfileEntry,_A1:onuTcontVirportBindProfileIndex,'onuTcontVirportBindProfileVirportIndex':onuTcontVirportBindProfileVirportIndex,'onuTcontVirportBindProfileName':onuTcontVirportBindProfileName,'onuTcontVirportBindProfileTcontID':onuTcontVirportBindProfileTcontID,'onuTcontVirportBindProfileTcontServiceProfileID':onuTcontVirportBindProfileTcontServiceProfileID,'onuTcontVirportBindProfileVirportServiceProfileID':onuTcontVirportBindProfileVirportServiceProfileID,'onuTcontVirportBindProfileRowStatus':onuTcontVirportBindProfileRowStatus,'onuVirtualPortServiceProfileTable':onuVirtualPortServiceProfileTable,'onuVirtualPortServiceProfileEntry':onuVirtualPortServiceProfileEntry,_A2:onuVirportProfileIndex,'onuVirportProfileName':onuVirportProfileName,'onuVirportProfileUsTrafficMapType':onuVirportProfileUsTrafficMapType,'onuVirportProfileTypeOfService':onuVirportProfileTypeOfService,'onuVirportProfileEncrypMode':onuVirportProfileEncrypMode,'onuVirportProfileUsBwProID':onuVirportProfileUsBwProID,'onuVirportProfileUsFlowPriority':onuVirportProfileUsFlowPriority,'onuVirportProfileUsFlowWeight':onuVirportProfileUsFlowWeight,'onuVirportProfileUsRateCtlSchedulerProID':onuVirportProfileUsRateCtlSchedulerProID,'onuVirportProfileDsBwProID':onuVirportProfileDsBwProID,'onuVirportProfileDsQueueSchType':onuVirportProfileDsQueueSchType,'onuVirportProfileDsFlowPriority':onuVirportProfileDsFlowPriority,'onuVirportProfileRowStatus':onuVirportProfileRowStatus,'onuFlowProfileTable':onuFlowProfileTable,'onuFlowProfileEntry':onuFlowProfileEntry,_A3:onuFlowProfileIndex1,_A4:onuFlowProfileIndex2,'onuFlowProfileName':onuFlowProfileName,'onuFlowProfileUniType':onuFlowProfileUniType,'onuFlowProfileUniPortBitMap':onuFlowProfileUniPortBitMap,'onuFlowProfileUsMapType':onuFlowProfileUsMapType,'onuFlowProfileVlanIdStart':onuFlowProfileVlanIdStart,'onuFlowProfileVlanIdStop':onuFlowProfileVlanIdStop,'onuFlowProfilePBITsMap':onuFlowProfilePBITsMap,'onuFlowProfileVirportNo':onuFlowProfileVirportNo,'onuFlowProfileRowStatus':onuFlowProfileRowStatus,'onuRateControlSchedulerProfileTable':onuRateControlSchedulerProfileTable,'onuRateControlSchedulerProfileEntry':onuRateControlSchedulerProfileEntry,_A5:onuRateCtlProfileIndex,'onuRateCtlProfileName':onuRateCtlProfileName,'onuRateCtlProfileCir':onuRateCtlProfileCir,'onuRateCtlProfilePir':onuRateCtlProfilePir,'onuRateCtlProfileScheduleWeight':onuRateCtlProfileScheduleWeight,'onuRateCtlProfileRowStatus':onuRateCtlProfileRowStatus,'onuEthernetUNIConfigProfileTable':onuEthernetUNIConfigProfileTable,'onuEthernetUNIConfigProfileEntry':onuEthernetUNIConfigProfileEntry,_A6:onuEthernetUNIPortProfileIndex,'onuEthernetUNIPortProfileName':onuEthernetUNIPortProfileName,'onuEthernetUNIPortAutoNegotiation':onuEthernetUNIPortAutoNegotiation,'onuEthernetUNIPortSpeed':onuEthernetUNIPortSpeed,'onuEthernetUNIPortDuplex':onuEthernetUNIPortDuplex,'onuEthernetUNIPortExpectedType':onuEthernetUNIPortExpectedType,'onuEthernetUNIPortMaxFrameSize':onuEthernetUNIPortMaxFrameSize,'onuEthernetUNIPortEthernetInterfaceWiring':onuEthernetUNIPortEthernetInterfaceWiring,'onuEthernetUNIPortProfileRowStatus':onuEthernetUNIPortProfileRowStatus})