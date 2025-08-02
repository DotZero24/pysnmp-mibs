_Z='restartDevice'
_Y='humi2x10Int'
_X='humi1x10Int'
_W='temp2x10Int'
_V='temp1x10Int'
_U='voltage2x10Int'
_T='voltage1x10Int'
_S='digitalInput2State'
_R='digitalInput1State'
_Q='noAction'
_P='humidity2'
_O='temperature2'
_N='humidity1'
_M='temperature1'
_L='NotificationType'
_K='DisplayString'
_J='enabled'
_I='disabled'
_H='OctetString'
_G='on'
_F='off'
_E='TERACOM-TCW121-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_L,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_L,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','TextualConvention')
class RANGE(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('range-0-5V',0),('range-0-100V',1)))
class CONTROLLED(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('manual',0),(_M,1),(_N,2),('analogInput1',3),('digitalInput1',4),(_O,5),(_P,6),('analogInput2',7),('digitalInput2',8)))
class ACTION(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_Q,0),('sendMail',1)))
class DACTION(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_Q,0),('mailIfFalled',1),('mailIfRised',2)))
_Teracom_ObjectIdentity=ObjectIdentity
teracom=_Teracom_ObjectIdentity((1,3,6,1,4,1,38783))
_Product_ObjectIdentity=ObjectIdentity
product=_Product_ObjectIdentity((1,3,6,1,4,1,38783,1))
_Name_Type=DisplayString
_Name_Object=MibScalar
name=_Name_Object((1,3,6,1,4,1,38783,1,1),_Name_Type())
name.setMaxAccess(_D)
if mibBuilder.loadTexts:name.setStatus(_A)
_Version_Type=DisplayString
_Version_Object=MibScalar
version=_Version_Object((1,3,6,1,4,1,38783,1,2),_Version_Type())
version.setMaxAccess(_D)
if mibBuilder.loadTexts:version.setStatus(_A)
_Date_Type=DisplayString
_Date_Object=MibScalar
date=_Date_Object((1,3,6,1,4,1,38783,1,3),_Date_Type())
date.setMaxAccess(_D)
if mibBuilder.loadTexts:date.setStatus(_A)
_Setup_ObjectIdentity=ObjectIdentity
setup=_Setup_ObjectIdentity((1,3,6,1,4,1,38783,2))
_Network_ObjectIdentity=ObjectIdentity
network=_Network_ObjectIdentity((1,3,6,1,4,1,38783,2,1))
_DeviceIPAddress_Type=IpAddress
_DeviceIPAddress_Object=MibScalar
deviceIPAddress=_DeviceIPAddress_Object((1,3,6,1,4,1,38783,2,1,1),_DeviceIPAddress_Type())
deviceIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceIPAddress.setStatus(_A)
_SubnetMask_Type=IpAddress
_SubnetMask_Object=MibScalar
subnetMask=_SubnetMask_Object((1,3,6,1,4,1,38783,2,1,2),_SubnetMask_Type())
subnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:subnetMask.setStatus(_A)
_Gateway_Type=IpAddress
_Gateway_Object=MibScalar
gateway=_Gateway_Object((1,3,6,1,4,1,38783,2,1,3),_Gateway_Type())
gateway.setMaxAccess(_B)
if mibBuilder.loadTexts:gateway.setStatus(_A)
class _DeviceMACAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_DeviceMACAddress_Type.__name__=_H
_DeviceMACAddress_Object=MibScalar
deviceMACAddress=_DeviceMACAddress_Object((1,3,6,1,4,1,38783,2,1,4),_DeviceMACAddress_Type())
deviceMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceMACAddress.setStatus(_A)
class _DhcpConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_DhcpConfig_Type.__name__=_C
_DhcpConfig_Object=MibScalar
dhcpConfig=_DhcpConfig_Object((1,3,6,1,4,1,38783,2,1,5),_DhcpConfig_Type())
dhcpConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpConfig.setStatus(_A)
_Dns_Type=IpAddress
_Dns_Object=MibScalar
dns=_Dns_Object((1,3,6,1,4,1,38783,2,1,6),_Dns_Type())
dns.setMaxAccess(_B)
if mibBuilder.loadTexts:dns.setStatus(_A)
class _HostName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,38))
_HostName_Type.__name__=_K
_HostName_Object=MibScalar
hostName=_HostName_Object((1,3,6,1,4,1,38783,2,1,7),_HostName_Type())
hostName.setMaxAccess(_B)
if mibBuilder.loadTexts:hostName.setStatus(_A)
_Vlan_ObjectIdentity=ObjectIdentity
vlan=_Vlan_ObjectIdentity((1,3,6,1,4,1,38783,2,2))
class _VlanStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_VlanStatus_Type.__name__=_C
_VlanStatus_Object=MibScalar
vlanStatus=_VlanStatus_Object((1,3,6,1,4,1,38783,2,2,1),_VlanStatus_Type())
vlanStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanStatus.setStatus(_A)
class _VlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_VlanId_Type.__name__=_C
_VlanId_Object=MibScalar
vlanId=_VlanId_Object((1,3,6,1,4,1,38783,2,2,2),_VlanId_Type())
vlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:vlanId.setStatus(_A)
_MacFilter_ObjectIdentity=ObjectIdentity
macFilter=_MacFilter_ObjectIdentity((1,3,6,1,4,1,38783,2,3))
class _FilterMACAddress1_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_FilterMACAddress1_Type.__name__=_H
_FilterMACAddress1_Object=MibScalar
filterMACAddress1=_FilterMACAddress1_Object((1,3,6,1,4,1,38783,2,3,1),_FilterMACAddress1_Type())
filterMACAddress1.setMaxAccess(_D)
if mibBuilder.loadTexts:filterMACAddress1.setStatus(_A)
class _FilterMACEnable1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_FilterMACEnable1_Type.__name__=_C
_FilterMACEnable1_Object=MibScalar
filterMACEnable1=_FilterMACEnable1_Object((1,3,6,1,4,1,38783,2,3,2),_FilterMACEnable1_Type())
filterMACEnable1.setMaxAccess(_B)
if mibBuilder.loadTexts:filterMACEnable1.setStatus(_A)
class _FilterMACAddress2_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_FilterMACAddress2_Type.__name__=_H
_FilterMACAddress2_Object=MibScalar
filterMACAddress2=_FilterMACAddress2_Object((1,3,6,1,4,1,38783,2,3,3),_FilterMACAddress2_Type())
filterMACAddress2.setMaxAccess(_B)
if mibBuilder.loadTexts:filterMACAddress2.setStatus(_A)
class _FilterMACEnable2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_FilterMACEnable2_Type.__name__=_C
_FilterMACEnable2_Object=MibScalar
filterMACEnable2=_FilterMACEnable2_Object((1,3,6,1,4,1,38783,2,3,4),_FilterMACEnable2_Type())
filterMACEnable2.setMaxAccess(_B)
if mibBuilder.loadTexts:filterMACEnable2.setStatus(_A)
class _FilterMACAddress3_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_FilterMACAddress3_Type.__name__=_H
_FilterMACAddress3_Object=MibScalar
filterMACAddress3=_FilterMACAddress3_Object((1,3,6,1,4,1,38783,2,3,5),_FilterMACAddress3_Type())
filterMACAddress3.setMaxAccess(_B)
if mibBuilder.loadTexts:filterMACAddress3.setStatus(_A)
class _FilterMACEnable3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_FilterMACEnable3_Type.__name__=_C
_FilterMACEnable3_Object=MibScalar
filterMACEnable3=_FilterMACEnable3_Object((1,3,6,1,4,1,38783,2,3,6),_FilterMACEnable3_Type())
filterMACEnable3.setMaxAccess(_B)
if mibBuilder.loadTexts:filterMACEnable3.setStatus(_A)
_SnmpSetup_ObjectIdentity=ObjectIdentity
snmpSetup=_SnmpSetup_ObjectIdentity((1,3,6,1,4,1,38783,2,4))
class _SnmpConfiguration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_I,0),(_J,1)))
_SnmpConfiguration_Type.__name__=_C
_SnmpConfiguration_Object=MibScalar
snmpConfiguration=_SnmpConfiguration_Object((1,3,6,1,4,1,38783,2,4,1),_SnmpConfiguration_Type())
snmpConfiguration.setMaxAccess(_B)
if mibBuilder.loadTexts:snmpConfiguration.setStatus(_A)
class _TrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_TrapEnabled_Type.__name__=_C
_TrapEnabled_Object=MibScalar
trapEnabled=_TrapEnabled_Object((1,3,6,1,4,1,38783,2,4,2),_TrapEnabled_Type())
trapEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:trapEnabled.setStatus(_A)
_TrapReceiverIPAddress_Type=IpAddress
_TrapReceiverIPAddress_Object=MibScalar
trapReceiverIPAddress=_TrapReceiverIPAddress_Object((1,3,6,1,4,1,38783,2,4,3),_TrapReceiverIPAddress_Type())
trapReceiverIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:trapReceiverIPAddress.setStatus(_A)
class _TrapCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,13))
_TrapCommunity_Type.__name__=_K
_TrapCommunity_Object=MibScalar
trapCommunity=_TrapCommunity_Object((1,3,6,1,4,1,38783,2,4,4),_TrapCommunity_Type())
trapCommunity.setMaxAccess(_B)
if mibBuilder.loadTexts:trapCommunity.setStatus(_A)
class _TrapInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_TrapInterval_Type.__name__=_C
_TrapInterval_Object=MibScalar
trapInterval=_TrapInterval_Object((1,3,6,1,4,1,38783,2,4,5),_TrapInterval_Type())
trapInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:trapInterval.setStatus(_A)
class _MaxNumberOfTraps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MaxNumberOfTraps_Type.__name__=_C
_MaxNumberOfTraps_Object=MibScalar
maxNumberOfTraps=_MaxNumberOfTraps_Object((1,3,6,1,4,1,38783,2,4,6),_MaxNumberOfTraps_Type())
maxNumberOfTraps.setMaxAccess(_B)
if mibBuilder.loadTexts:maxNumberOfTraps.setStatus(_A)
_Sensor1_ObjectIdentity=ObjectIdentity
sensor1=_Sensor1_ObjectIdentity((1,3,6,1,4,1,38783,2,5))
_Temperature1_ObjectIdentity=ObjectIdentity
temperature1=_Temperature1_ObjectIdentity((1,3,6,1,4,1,38783,2,5,1))
class _Temperature1Min_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400,1250))
_Temperature1Min_Type.__name__=_C
_Temperature1Min_Object=MibScalar
temperature1Min=_Temperature1Min_Object((1,3,6,1,4,1,38783,2,5,1,1),_Temperature1Min_Type())
temperature1Min.setMaxAccess(_B)
if mibBuilder.loadTexts:temperature1Min.setStatus(_A)
class _Temperature1Max_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400,1250))
_Temperature1Max_Type.__name__=_C
_Temperature1Max_Object=MibScalar
temperature1Max=_Temperature1Max_Object((1,3,6,1,4,1,38783,2,5,1,2),_Temperature1Max_Type())
temperature1Max.setMaxAccess(_B)
if mibBuilder.loadTexts:temperature1Max.setStatus(_A)
class _Temperature1Hyst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400,1250))
_Temperature1Hyst_Type.__name__=_C
_Temperature1Hyst_Object=MibScalar
temperature1Hyst=_Temperature1Hyst_Object((1,3,6,1,4,1,38783,2,5,1,3),_Temperature1Hyst_Type())
temperature1Hyst.setMaxAccess(_B)
if mibBuilder.loadTexts:temperature1Hyst.setStatus(_A)
_Temperature1Action_Type=ACTION
_Temperature1Action_Object=MibScalar
temperature1Action=_Temperature1Action_Object((1,3,6,1,4,1,38783,2,5,1,4),_Temperature1Action_Type())
temperature1Action.setMaxAccess(_B)
if mibBuilder.loadTexts:temperature1Action.setStatus(_A)
_Humidity1_ObjectIdentity=ObjectIdentity
humidity1=_Humidity1_ObjectIdentity((1,3,6,1,4,1,38783,2,5,2))
class _Humidity1Min_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_Humidity1Min_Type.__name__=_C
_Humidity1Min_Object=MibScalar
humidity1Min=_Humidity1Min_Object((1,3,6,1,4,1,38783,2,5,2,1),_Humidity1Min_Type())
humidity1Min.setMaxAccess(_B)
if mibBuilder.loadTexts:humidity1Min.setStatus(_A)
class _Humidity1Max_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_Humidity1Max_Type.__name__=_C
_Humidity1Max_Object=MibScalar
humidity1Max=_Humidity1Max_Object((1,3,6,1,4,1,38783,2,5,2,2),_Humidity1Max_Type())
humidity1Max.setMaxAccess(_B)
if mibBuilder.loadTexts:humidity1Max.setStatus(_A)
class _Humidity1Hyst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_Humidity1Hyst_Type.__name__=_C
_Humidity1Hyst_Object=MibScalar
humidity1Hyst=_Humidity1Hyst_Object((1,3,6,1,4,1,38783,2,5,2,3),_Humidity1Hyst_Type())
humidity1Hyst.setMaxAccess(_B)
if mibBuilder.loadTexts:humidity1Hyst.setStatus(_A)
_Humidity1Action_Type=ACTION
_Humidity1Action_Object=MibScalar
humidity1Action=_Humidity1Action_Object((1,3,6,1,4,1,38783,2,5,2,4),_Humidity1Action_Type())
humidity1Action.setMaxAccess(_B)
if mibBuilder.loadTexts:humidity1Action.setStatus(_A)
_Sensor2_ObjectIdentity=ObjectIdentity
sensor2=_Sensor2_ObjectIdentity((1,3,6,1,4,1,38783,2,6))
_Temperature2_ObjectIdentity=ObjectIdentity
temperature2=_Temperature2_ObjectIdentity((1,3,6,1,4,1,38783,2,6,1))
class _Temperature2Min_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400,1250))
_Temperature2Min_Type.__name__=_C
_Temperature2Min_Object=MibScalar
temperature2Min=_Temperature2Min_Object((1,3,6,1,4,1,38783,2,6,1,1),_Temperature2Min_Type())
temperature2Min.setMaxAccess(_B)
if mibBuilder.loadTexts:temperature2Min.setStatus(_A)
class _Temperature2Max_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400,1250))
_Temperature2Max_Type.__name__=_C
_Temperature2Max_Object=MibScalar
temperature2Max=_Temperature2Max_Object((1,3,6,1,4,1,38783,2,6,1,2),_Temperature2Max_Type())
temperature2Max.setMaxAccess(_B)
if mibBuilder.loadTexts:temperature2Max.setStatus(_A)
class _Temperature2Hyst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400,1250))
_Temperature2Hyst_Type.__name__=_C
_Temperature2Hyst_Object=MibScalar
temperature2Hyst=_Temperature2Hyst_Object((1,3,6,1,4,1,38783,2,6,1,3),_Temperature2Hyst_Type())
temperature2Hyst.setMaxAccess(_B)
if mibBuilder.loadTexts:temperature2Hyst.setStatus(_A)
_Temperature2Action_Type=ACTION
_Temperature2Action_Object=MibScalar
temperature2Action=_Temperature2Action_Object((1,3,6,1,4,1,38783,2,6,1,4),_Temperature2Action_Type())
temperature2Action.setMaxAccess(_B)
if mibBuilder.loadTexts:temperature2Action.setStatus(_A)
_Humidity2_ObjectIdentity=ObjectIdentity
humidity2=_Humidity2_ObjectIdentity((1,3,6,1,4,1,38783,2,6,2))
class _Humidity2Min_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_Humidity2Min_Type.__name__=_C
_Humidity2Min_Object=MibScalar
humidity2Min=_Humidity2Min_Object((1,3,6,1,4,1,38783,2,6,2,1),_Humidity2Min_Type())
humidity2Min.setMaxAccess(_B)
if mibBuilder.loadTexts:humidity2Min.setStatus(_A)
class _Humidity2Max_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_Humidity2Max_Type.__name__=_C
_Humidity2Max_Object=MibScalar
humidity2Max=_Humidity2Max_Object((1,3,6,1,4,1,38783,2,6,2,2),_Humidity2Max_Type())
humidity2Max.setMaxAccess(_B)
if mibBuilder.loadTexts:humidity2Max.setStatus(_A)
class _Humidity2Hyst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_Humidity2Hyst_Type.__name__=_C
_Humidity2Hyst_Object=MibScalar
humidity2Hyst=_Humidity2Hyst_Object((1,3,6,1,4,1,38783,2,6,2,3),_Humidity2Hyst_Type())
humidity2Hyst.setMaxAccess(_B)
if mibBuilder.loadTexts:humidity2Hyst.setStatus(_A)
_Humidity2Action_Type=ACTION
_Humidity2Action_Object=MibScalar
humidity2Action=_Humidity2Action_Object((1,3,6,1,4,1,38783,2,6,2,4),_Humidity2Action_Type())
humidity2Action.setMaxAccess(_B)
if mibBuilder.loadTexts:humidity2Action.setStatus(_A)
_AnalogInput_ObjectIdentity=ObjectIdentity
analogInput=_AnalogInput_ObjectIdentity((1,3,6,1,4,1,38783,2,7))
_Input1_ObjectIdentity=ObjectIdentity
input1=_Input1_ObjectIdentity((1,3,6,1,4,1,38783,2,7,1))
class _Voltage1Min_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_Voltage1Min_Type.__name__=_C
_Voltage1Min_Object=MibScalar
voltage1Min=_Voltage1Min_Object((1,3,6,1,4,1,38783,2,7,1,1),_Voltage1Min_Type())
voltage1Min.setMaxAccess(_B)
if mibBuilder.loadTexts:voltage1Min.setStatus(_A)
class _Voltage1Max_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_Voltage1Max_Type.__name__=_C
_Voltage1Max_Object=MibScalar
voltage1Max=_Voltage1Max_Object((1,3,6,1,4,1,38783,2,7,1,2),_Voltage1Max_Type())
voltage1Max.setMaxAccess(_B)
if mibBuilder.loadTexts:voltage1Max.setStatus(_A)
class _Voltage1Hyst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_Voltage1Hyst_Type.__name__=_C
_Voltage1Hyst_Object=MibScalar
voltage1Hyst=_Voltage1Hyst_Object((1,3,6,1,4,1,38783,2,7,1,3),_Voltage1Hyst_Type())
voltage1Hyst.setMaxAccess(_B)
if mibBuilder.loadTexts:voltage1Hyst.setStatus(_A)
_Voltage1Action_Type=ACTION
_Voltage1Action_Object=MibScalar
voltage1Action=_Voltage1Action_Object((1,3,6,1,4,1,38783,2,7,1,4),_Voltage1Action_Type())
voltage1Action.setMaxAccess(_B)
if mibBuilder.loadTexts:voltage1Action.setStatus(_A)
_Voltage1Range_Type=RANGE
_Voltage1Range_Object=MibScalar
voltage1Range=_Voltage1Range_Object((1,3,6,1,4,1,38783,2,7,1,5),_Voltage1Range_Type())
voltage1Range.setMaxAccess(_B)
if mibBuilder.loadTexts:voltage1Range.setStatus(_A)
_Input2_ObjectIdentity=ObjectIdentity
input2=_Input2_ObjectIdentity((1,3,6,1,4,1,38783,2,7,2))
class _Voltage2Min_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_Voltage2Min_Type.__name__=_C
_Voltage2Min_Object=MibScalar
voltage2Min=_Voltage2Min_Object((1,3,6,1,4,1,38783,2,7,2,1),_Voltage2Min_Type())
voltage2Min.setMaxAccess(_B)
if mibBuilder.loadTexts:voltage2Min.setStatus(_A)
class _Voltage2Max_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_Voltage2Max_Type.__name__=_C
_Voltage2Max_Object=MibScalar
voltage2Max=_Voltage2Max_Object((1,3,6,1,4,1,38783,2,7,2,2),_Voltage2Max_Type())
voltage2Max.setMaxAccess(_B)
if mibBuilder.loadTexts:voltage2Max.setStatus(_A)
class _Voltage2Hyst_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_Voltage2Hyst_Type.__name__=_C
_Voltage2Hyst_Object=MibScalar
voltage2Hyst=_Voltage2Hyst_Object((1,3,6,1,4,1,38783,2,7,2,3),_Voltage2Hyst_Type())
voltage2Hyst.setMaxAccess(_B)
if mibBuilder.loadTexts:voltage2Hyst.setStatus(_A)
_Voltage2Action_Type=ACTION
_Voltage2Action_Object=MibScalar
voltage2Action=_Voltage2Action_Object((1,3,6,1,4,1,38783,2,7,2,4),_Voltage2Action_Type())
voltage2Action.setMaxAccess(_B)
if mibBuilder.loadTexts:voltage2Action.setStatus(_A)
_Voltage2Range_Type=RANGE
_Voltage2Range_Object=MibScalar
voltage2Range=_Voltage2Range_Object((1,3,6,1,4,1,38783,2,7,2,5),_Voltage2Range_Type())
voltage2Range.setMaxAccess(_B)
if mibBuilder.loadTexts:voltage2Range.setStatus(_A)
_DigitalInput_ObjectIdentity=ObjectIdentity
digitalInput=_DigitalInput_ObjectIdentity((1,3,6,1,4,1,38783,2,8))
_DigitalInput1Action_Type=DACTION
_DigitalInput1Action_Object=MibScalar
digitalInput1Action=_DigitalInput1Action_Object((1,3,6,1,4,1,38783,2,8,1),_DigitalInput1Action_Type())
digitalInput1Action.setMaxAccess(_B)
if mibBuilder.loadTexts:digitalInput1Action.setStatus(_A)
_DigitalInput2Action_Type=DACTION
_DigitalInput2Action_Object=MibScalar
digitalInput2Action=_DigitalInput2Action_Object((1,3,6,1,4,1,38783,2,8,2),_DigitalInput2Action_Type())
digitalInput2Action.setMaxAccess(_B)
if mibBuilder.loadTexts:digitalInput2Action.setStatus(_A)
_Relay_ObjectIdentity=ObjectIdentity
relay=_Relay_ObjectIdentity((1,3,6,1,4,1,38783,2,9))
_Relay1ControledBy_Type=CONTROLLED
_Relay1ControledBy_Object=MibScalar
relay1ControledBy=_Relay1ControledBy_Object((1,3,6,1,4,1,38783,2,9,1),_Relay1ControledBy_Type())
relay1ControledBy.setMaxAccess(_B)
if mibBuilder.loadTexts:relay1ControledBy.setStatus(_A)
_Relay2ControledBy_Type=CONTROLLED
_Relay2ControledBy_Object=MibScalar
relay2ControledBy=_Relay2ControledBy_Object((1,3,6,1,4,1,38783,2,9,2),_Relay2ControledBy_Type())
relay2ControledBy.setMaxAccess(_B)
if mibBuilder.loadTexts:relay2ControledBy.setStatus(_A)
class _RelayPulseWidth_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RelayPulseWidth_Type.__name__=_C
_RelayPulseWidth_Object=MibScalar
relayPulseWidth=_RelayPulseWidth_Object((1,3,6,1,4,1,38783,2,9,3),_RelayPulseWidth_Type())
relayPulseWidth.setMaxAccess(_B)
if mibBuilder.loadTexts:relayPulseWidth.setStatus(_A)
_Recipients_ObjectIdentity=ObjectIdentity
recipients=_Recipients_ObjectIdentity((1,3,6,1,4,1,38783,2,10))
class _Recipient1EmailAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,38))
_Recipient1EmailAddress_Type.__name__=_K
_Recipient1EmailAddress_Object=MibScalar
recipient1EmailAddress=_Recipient1EmailAddress_Object((1,3,6,1,4,1,38783,2,10,1),_Recipient1EmailAddress_Type())
recipient1EmailAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:recipient1EmailAddress.setStatus(_A)
_MonitorNcontrol_ObjectIdentity=ObjectIdentity
monitorNcontrol=_MonitorNcontrol_ObjectIdentity((1,3,6,1,4,1,38783,3))
class _DigitalInput1State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_DigitalInput1State_Type.__name__=_C
_DigitalInput1State_Object=MibScalar
digitalInput1State=_DigitalInput1State_Object((1,3,6,1,4,1,38783,3,1),_DigitalInput1State_Type())
digitalInput1State.setMaxAccess(_D)
if mibBuilder.loadTexts:digitalInput1State.setStatus(_A)
class _DigitalInput2State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_DigitalInput2State_Type.__name__=_C
_DigitalInput2State_Object=MibScalar
digitalInput2State=_DigitalInput2State_Object((1,3,6,1,4,1,38783,3,2),_DigitalInput2State_Type())
digitalInput2State.setMaxAccess(_D)
if mibBuilder.loadTexts:digitalInput2State.setStatus(_A)
class _Relay1State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_Relay1State_Type.__name__=_C
_Relay1State_Object=MibScalar
relay1State=_Relay1State_Object((1,3,6,1,4,1,38783,3,3),_Relay1State_Type())
relay1State.setMaxAccess(_B)
if mibBuilder.loadTexts:relay1State.setStatus(_A)
class _Relay1Pulse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_Relay1Pulse_Type.__name__=_C
_Relay1Pulse_Object=MibScalar
relay1Pulse=_Relay1Pulse_Object((1,3,6,1,4,1,38783,3,4),_Relay1Pulse_Type())
relay1Pulse.setMaxAccess(_B)
if mibBuilder.loadTexts:relay1Pulse.setStatus(_A)
class _Relay2State_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_Relay2State_Type.__name__=_C
_Relay2State_Object=MibScalar
relay2State=_Relay2State_Object((1,3,6,1,4,1,38783,3,5),_Relay2State_Type())
relay2State.setMaxAccess(_B)
if mibBuilder.loadTexts:relay2State.setStatus(_A)
class _Relay2Pulse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_F,0),(_G,1)))
_Relay2Pulse_Type.__name__=_C
_Relay2Pulse_Object=MibScalar
relay2Pulse=_Relay2Pulse_Object((1,3,6,1,4,1,38783,3,6),_Relay2Pulse_Type())
relay2Pulse.setMaxAccess(_B)
if mibBuilder.loadTexts:relay2Pulse.setStatus(_A)
class _Voltage1x10Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_Voltage1x10Int_Type.__name__=_C
_Voltage1x10Int_Object=MibScalar
voltage1x10Int=_Voltage1x10Int_Object((1,3,6,1,4,1,38783,3,7),_Voltage1x10Int_Type())
voltage1x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:voltage1x10Int.setStatus(_A)
class _Voltage2x10Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_Voltage2x10Int_Type.__name__=_C
_Voltage2x10Int_Object=MibScalar
voltage2x10Int=_Voltage2x10Int_Object((1,3,6,1,4,1,38783,3,8),_Voltage2x10Int_Type())
voltage2x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:voltage2x10Int.setStatus(_A)
class _Temp1x10Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400,1250))
_Temp1x10Int_Type.__name__=_C
_Temp1x10Int_Object=MibScalar
temp1x10Int=_Temp1x10Int_Object((1,3,6,1,4,1,38783,3,9),_Temp1x10Int_Type())
temp1x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:temp1x10Int.setStatus(_A)
class _Temp2x10Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-400,1250))
_Temp2x10Int_Type.__name__=_C
_Temp2x10Int_Object=MibScalar
temp2x10Int=_Temp2x10Int_Object((1,3,6,1,4,1,38783,3,10),_Temp2x10Int_Type())
temp2x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:temp2x10Int.setStatus(_A)
class _Humi1x10Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_Humi1x10Int_Type.__name__=_C
_Humi1x10Int_Object=MibScalar
humi1x10Int=_Humi1x10Int_Object((1,3,6,1,4,1,38783,3,11),_Humi1x10Int_Type())
humi1x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:humi1x10Int.setStatus(_A)
class _Humi2x10Int_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_Humi2x10Int_Type.__name__=_C
_Humi2x10Int_Object=MibScalar
humi2x10Int=_Humi2x10Int_Object((1,3,6,1,4,1,38783,3,12),_Humi2x10Int_Type())
humi2x10Int.setMaxAccess(_D)
if mibBuilder.loadTexts:humi2x10Int.setStatus(_A)
class _ConfigurationSaved_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unsaved',0),('saved',1)))
_ConfigurationSaved_Type.__name__=_C
_ConfigurationSaved_Object=MibScalar
configurationSaved=_ConfigurationSaved_Object((1,3,6,1,4,1,38783,3,13),_ConfigurationSaved_Type())
configurationSaved.setMaxAccess(_B)
if mibBuilder.loadTexts:configurationSaved.setStatus(_A)
class _RestartDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('cancel',0),('restart',1)))
_RestartDevice_Type.__name__=_C
_RestartDevice_Object=MibScalar
restartDevice=_RestartDevice_Object((1,3,6,1,4,1,38783,3,14),_RestartDevice_Type())
restartDevice.setMaxAccess(_B)
if mibBuilder.loadTexts:restartDevice.setStatus(_A)
trcDigitalInput1State=NotificationType((1,3,6,1,4,1,38783,0,101))
trcDigitalInput1State.setObjects((_E,_R))
if mibBuilder.loadTexts:trcDigitalInput1State.setStatus('')
trcDigitalInput2State=NotificationType((1,3,6,1,4,1,38783,0,102))
trcDigitalInput2State.setObjects((_E,_S))
if mibBuilder.loadTexts:trcDigitalInput2State.setStatus('')
trcVoltage1x10Int=NotificationType((1,3,6,1,4,1,38783,0,103))
trcVoltage1x10Int.setObjects((_E,_T))
if mibBuilder.loadTexts:trcVoltage1x10Int.setStatus('')
trcVoltage2x10Int=NotificationType((1,3,6,1,4,1,38783,0,104))
trcVoltage2x10Int.setObjects((_E,_U))
if mibBuilder.loadTexts:trcVoltage2x10Int.setStatus('')
trcTemp1x10Int=NotificationType((1,3,6,1,4,1,38783,0,105))
trcTemp1x10Int.setObjects((_E,_V))
if mibBuilder.loadTexts:trcTemp1x10Int.setStatus('')
trcTemp2x10Int=NotificationType((1,3,6,1,4,1,38783,0,106))
trcTemp2x10Int.setObjects((_E,_W))
if mibBuilder.loadTexts:trcTemp2x10Int.setStatus('')
trcHumi1x10Int=NotificationType((1,3,6,1,4,1,38783,0,107))
trcHumi1x10Int.setObjects((_E,_X))
if mibBuilder.loadTexts:trcHumi1x10Int.setStatus('')
trcHumi2x10Int=NotificationType((1,3,6,1,4,1,38783,0,108))
trcHumi2x10Int.setObjects((_E,_Y))
if mibBuilder.loadTexts:trcHumi2x10Int.setStatus('')
trcRestartDevice=NotificationType((1,3,6,1,4,1,38783,0,109))
trcRestartDevice.setObjects((_E,_Z))
if mibBuilder.loadTexts:trcRestartDevice.setStatus('')
mibBuilder.exportSymbols(_E,**{'RANGE':RANGE,'CONTROLLED':CONTROLLED,'ACTION':ACTION,'DACTION':DACTION,'teracom':teracom,'trcDigitalInput1State':trcDigitalInput1State,'trcDigitalInput2State':trcDigitalInput2State,'trcVoltage1x10Int':trcVoltage1x10Int,'trcVoltage2x10Int':trcVoltage2x10Int,'trcTemp1x10Int':trcTemp1x10Int,'trcTemp2x10Int':trcTemp2x10Int,'trcHumi1x10Int':trcHumi1x10Int,'trcHumi2x10Int':trcHumi2x10Int,'trcRestartDevice':trcRestartDevice,'product':product,'name':name,'version':version,'date':date,'setup':setup,'network':network,'deviceIPAddress':deviceIPAddress,'subnetMask':subnetMask,'gateway':gateway,'deviceMACAddress':deviceMACAddress,'dhcpConfig':dhcpConfig,'dns':dns,'hostName':hostName,'vlan':vlan,'vlanStatus':vlanStatus,'vlanId':vlanId,'macFilter':macFilter,'filterMACAddress1':filterMACAddress1,'filterMACEnable1':filterMACEnable1,'filterMACAddress2':filterMACAddress2,'filterMACEnable2':filterMACEnable2,'filterMACAddress3':filterMACAddress3,'filterMACEnable3':filterMACEnable3,'snmpSetup':snmpSetup,'snmpConfiguration':snmpConfiguration,'trapEnabled':trapEnabled,'trapReceiverIPAddress':trapReceiverIPAddress,'trapCommunity':trapCommunity,'trapInterval':trapInterval,'maxNumberOfTraps':maxNumberOfTraps,'sensor1':sensor1,_M:temperature1,'temperature1Min':temperature1Min,'temperature1Max':temperature1Max,'temperature1Hyst':temperature1Hyst,'temperature1Action':temperature1Action,_N:humidity1,'humidity1Min':humidity1Min,'humidity1Max':humidity1Max,'humidity1Hyst':humidity1Hyst,'humidity1Action':humidity1Action,'sensor2':sensor2,_O:temperature2,'temperature2Min':temperature2Min,'temperature2Max':temperature2Max,'temperature2Hyst':temperature2Hyst,'temperature2Action':temperature2Action,_P:humidity2,'humidity2Min':humidity2Min,'humidity2Max':humidity2Max,'humidity2Hyst':humidity2Hyst,'humidity2Action':humidity2Action,'analogInput':analogInput,'input1':input1,'voltage1Min':voltage1Min,'voltage1Max':voltage1Max,'voltage1Hyst':voltage1Hyst,'voltage1Action':voltage1Action,'voltage1Range':voltage1Range,'input2':input2,'voltage2Min':voltage2Min,'voltage2Max':voltage2Max,'voltage2Hyst':voltage2Hyst,'voltage2Action':voltage2Action,'voltage2Range':voltage2Range,'digitalInput':digitalInput,'digitalInput1Action':digitalInput1Action,'digitalInput2Action':digitalInput2Action,'relay':relay,'relay1ControledBy':relay1ControledBy,'relay2ControledBy':relay2ControledBy,'relayPulseWidth':relayPulseWidth,'recipients':recipients,'recipient1EmailAddress':recipient1EmailAddress,'monitorNcontrol':monitorNcontrol,_R:digitalInput1State,_S:digitalInput2State,'relay1State':relay1State,'relay1Pulse':relay1Pulse,'relay2State':relay2State,'relay2Pulse':relay2Pulse,_T:voltage1x10Int,_U:voltage2x10Int,_V:temp1x10Int,_W:temp2x10Int,_X:humi1x10Int,_Y:humi2x10Int,'configurationSaved':configurationSaved,_Z:restartDevice})