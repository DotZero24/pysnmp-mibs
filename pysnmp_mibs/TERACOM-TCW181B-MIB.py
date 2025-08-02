_AL='tcw181bTrapGroup'
_AK='tcw181bIOSetupGroup'
_AJ='tcw181bNetworkGroup'
_AI='tcw181bMonitorGroup'
_AH='tcw181bSnmpSetupGroup'
_AG='tcw181bProductGroup'
_AF='snmp-trap-notification'
_AE='configurationSaved'
_AD='digitalInputDescription'
_AC='relay8PulseDurationMs'
_AB='relay7PulseDurationMs'
_AA='relay6PulseDurationMs'
_A9='relay5PulseDurationMs'
_A8='relay4PulseDurationMs'
_A7='relay3PulseDurationMs'
_A6='relay2PulseDurationMs'
_A5='relay1PulseDurationMs'
_A4='digitalInputBody'
_A3='digitalInputSubject'
_A2='digitalInputTo'
_A1='digitalInputAction'
_A0='relay8description'
_z='relay7description'
_y='relay6description'
_x='relay5description'
_w='relay4description'
_v='relay3description'
_u='relay2description'
_t='relay1description'
_s='relay8PulseDuration'
_r='relay7PulseDuration'
_q='relay6PulseDuration'
_p='relay5PulseDuration'
_o='relay4PulseDuration'
_n='relay3PulseDuration'
_m='relay2PulseDuration'
_l='relay1PulseDuration'
_k='dhcpConfig'
_j='deviceMACAddress'
_i='gateway'
_h='subnetMask'
_g='deviceIPAddress'
_f='allPulse'
_e='allOff'
_d='pulse8'
_c='pulse7'
_b='pulse6'
_a='pulse5'
_Z='pulse4'
_Y='pulse3'
_X='pulse2'
_W='pulse1'
_V='relay8'
_U='relay7'
_T='relay6'
_S='relay5'
_R='relay4'
_Q='relay3'
_P='relay2'
_O='relay1'
_N='trapCommunity'
_M='trapReceiverIPAddress'
_L='trapEnabled'
_K='version'
_J='restartDevice'
_I='digitalInput'
_H='read-only'
_G='DisplayString'
_F='on'
_E='off'
_D='Integer32'
_C='read-write'
_B='current'
_A='TERACOM-TCW181B-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso,snmpModules=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso','snmpModules')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'MacAddress','PhysAddress','TextualConvention')
snmpMIB=ModuleIdentity((1,3,6,1,6,3,1))
if mibBuilder.loadTexts:snmpMIB.setRevisions(('2017-01-26 00:00',))
_Teracom_ObjectIdentity=ObjectIdentity
teracom=_Teracom_ObjectIdentity((1,3,6,1,4,1,38783))
_TrapNotifications_ObjectIdentity=ObjectIdentity
trapNotifications=_TrapNotifications_ObjectIdentity((1,3,6,1,4,1,38783,0))
_Product_ObjectIdentity=ObjectIdentity
product=_Product_ObjectIdentity((1,3,6,1,4,1,38783,1))
_Name_Type=DisplayString
_Name_Object=MibScalar
name=_Name_Object((1,3,6,1,4,1,38783,1,1),_Name_Type())
name.setMaxAccess(_H)
if mibBuilder.loadTexts:name.setStatus(_B)
_Version_Type=DisplayString
_Version_Object=MibScalar
version=_Version_Object((1,3,6,1,4,1,38783,1,2),_Version_Type())
version.setMaxAccess(_H)
if mibBuilder.loadTexts:version.setStatus(_B)
_Date_Type=DisplayString
_Date_Object=MibScalar
date=_Date_Object((1,3,6,1,4,1,38783,1,3),_Date_Type())
date.setMaxAccess(_H)
if mibBuilder.loadTexts:date.setStatus(_B)
_SnmpSetup_ObjectIdentity=ObjectIdentity
snmpSetup=_SnmpSetup_ObjectIdentity((1,3,6,1,4,1,38783,2))
class _TrapEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('no',0),('yes',1)))
_TrapEnabled_Type.__name__=_D
_TrapEnabled_Object=MibScalar
trapEnabled=_TrapEnabled_Object((1,3,6,1,4,1,38783,2,1),_TrapEnabled_Type())
trapEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:trapEnabled.setStatus(_B)
_TrapReceiverIPAddress_Type=IpAddress
_TrapReceiverIPAddress_Object=MibScalar
trapReceiverIPAddress=_TrapReceiverIPAddress_Object((1,3,6,1,4,1,38783,2,2),_TrapReceiverIPAddress_Type())
trapReceiverIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:trapReceiverIPAddress.setStatus(_B)
class _TrapCommunity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,13))
_TrapCommunity_Type.__name__=_G
_TrapCommunity_Object=MibScalar
trapCommunity=_TrapCommunity_Object((1,3,6,1,4,1,38783,2,3),_TrapCommunity_Type())
trapCommunity.setMaxAccess(_C)
if mibBuilder.loadTexts:trapCommunity.setStatus(_B)
_MonitorNcontrol_ObjectIdentity=ObjectIdentity
monitorNcontrol=_MonitorNcontrol_ObjectIdentity((1,3,6,1,4,1,38783,3))
class _DigitalInput_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('closed',0),('open',1)))
_DigitalInput_Type.__name__=_D
_DigitalInput_Object=MibScalar
digitalInput=_DigitalInput_Object((1,3,6,1,4,1,38783,3,1),_DigitalInput_Type())
digitalInput.setMaxAccess(_H)
if mibBuilder.loadTexts:digitalInput.setStatus(_B)
class _Relay1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Relay1_Type.__name__=_D
_Relay1_Object=MibScalar
relay1=_Relay1_Object((1,3,6,1,4,1,38783,3,2),_Relay1_Type())
relay1.setMaxAccess(_C)
if mibBuilder.loadTexts:relay1.setStatus(_B)
class _Relay2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Relay2_Type.__name__=_D
_Relay2_Object=MibScalar
relay2=_Relay2_Object((1,3,6,1,4,1,38783,3,3),_Relay2_Type())
relay2.setMaxAccess(_C)
if mibBuilder.loadTexts:relay2.setStatus(_B)
class _Relay3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Relay3_Type.__name__=_D
_Relay3_Object=MibScalar
relay3=_Relay3_Object((1,3,6,1,4,1,38783,3,4),_Relay3_Type())
relay3.setMaxAccess(_C)
if mibBuilder.loadTexts:relay3.setStatus(_B)
class _Relay4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Relay4_Type.__name__=_D
_Relay4_Object=MibScalar
relay4=_Relay4_Object((1,3,6,1,4,1,38783,3,5),_Relay4_Type())
relay4.setMaxAccess(_C)
if mibBuilder.loadTexts:relay4.setStatus(_B)
class _Relay5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Relay5_Type.__name__=_D
_Relay5_Object=MibScalar
relay5=_Relay5_Object((1,3,6,1,4,1,38783,3,6),_Relay5_Type())
relay5.setMaxAccess(_C)
if mibBuilder.loadTexts:relay5.setStatus(_B)
class _Relay6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Relay6_Type.__name__=_D
_Relay6_Object=MibScalar
relay6=_Relay6_Object((1,3,6,1,4,1,38783,3,7),_Relay6_Type())
relay6.setMaxAccess(_C)
if mibBuilder.loadTexts:relay6.setStatus(_B)
class _Relay7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Relay7_Type.__name__=_D
_Relay7_Object=MibScalar
relay7=_Relay7_Object((1,3,6,1,4,1,38783,3,8),_Relay7_Type())
relay7.setMaxAccess(_C)
if mibBuilder.loadTexts:relay7.setStatus(_B)
class _Relay8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Relay8_Type.__name__=_D
_Relay8_Object=MibScalar
relay8=_Relay8_Object((1,3,6,1,4,1,38783,3,9),_Relay8_Type())
relay8.setMaxAccess(_C)
if mibBuilder.loadTexts:relay8.setStatus(_B)
class _Pulse1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Pulse1_Type.__name__=_D
_Pulse1_Object=MibScalar
pulse1=_Pulse1_Object((1,3,6,1,4,1,38783,3,10),_Pulse1_Type())
pulse1.setMaxAccess(_C)
if mibBuilder.loadTexts:pulse1.setStatus(_B)
class _Pulse2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Pulse2_Type.__name__=_D
_Pulse2_Object=MibScalar
pulse2=_Pulse2_Object((1,3,6,1,4,1,38783,3,11),_Pulse2_Type())
pulse2.setMaxAccess(_C)
if mibBuilder.loadTexts:pulse2.setStatus(_B)
class _Pulse3_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Pulse3_Type.__name__=_D
_Pulse3_Object=MibScalar
pulse3=_Pulse3_Object((1,3,6,1,4,1,38783,3,12),_Pulse3_Type())
pulse3.setMaxAccess(_C)
if mibBuilder.loadTexts:pulse3.setStatus(_B)
class _Pulse4_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Pulse4_Type.__name__=_D
_Pulse4_Object=MibScalar
pulse4=_Pulse4_Object((1,3,6,1,4,1,38783,3,13),_Pulse4_Type())
pulse4.setMaxAccess(_C)
if mibBuilder.loadTexts:pulse4.setStatus(_B)
class _Pulse5_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Pulse5_Type.__name__=_D
_Pulse5_Object=MibScalar
pulse5=_Pulse5_Object((1,3,6,1,4,1,38783,3,14),_Pulse5_Type())
pulse5.setMaxAccess(_C)
if mibBuilder.loadTexts:pulse5.setStatus(_B)
class _Pulse6_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Pulse6_Type.__name__=_D
_Pulse6_Object=MibScalar
pulse6=_Pulse6_Object((1,3,6,1,4,1,38783,3,15),_Pulse6_Type())
pulse6.setMaxAccess(_C)
if mibBuilder.loadTexts:pulse6.setStatus(_B)
class _Pulse7_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Pulse7_Type.__name__=_D
_Pulse7_Object=MibScalar
pulse7=_Pulse7_Object((1,3,6,1,4,1,38783,3,16),_Pulse7_Type())
pulse7.setMaxAccess(_C)
if mibBuilder.loadTexts:pulse7.setStatus(_B)
class _Pulse8_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_Pulse8_Type.__name__=_D
_Pulse8_Object=MibScalar
pulse8=_Pulse8_Object((1,3,6,1,4,1,38783,3,17),_Pulse8_Type())
pulse8.setMaxAccess(_C)
if mibBuilder.loadTexts:pulse8.setStatus(_B)
class _AllOn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_AllOn_Type.__name__=_D
_AllOn_Object=MibScalar
allOn=_AllOn_Object((1,3,6,1,4,1,38783,3,18),_AllOn_Type())
allOn.setMaxAccess(_C)
if mibBuilder.loadTexts:allOn.setStatus(_B)
class _AllOff_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_AllOff_Type.__name__=_D
_AllOff_Object=MibScalar
allOff=_AllOff_Object((1,3,6,1,4,1,38783,3,19),_AllOff_Type())
allOff.setMaxAccess(_C)
if mibBuilder.loadTexts:allOff.setStatus(_B)
class _AllPulse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_AllPulse_Type.__name__=_D
_AllPulse_Object=MibScalar
allPulse=_AllPulse_Object((1,3,6,1,4,1,38783,3,20),_AllPulse_Type())
allPulse.setMaxAccess(_C)
if mibBuilder.loadTexts:allPulse.setStatus(_B)
_Network_ObjectIdentity=ObjectIdentity
network=_Network_ObjectIdentity((1,3,6,1,4,1,38783,4))
_DeviceIPAddress_Type=IpAddress
_DeviceIPAddress_Object=MibScalar
deviceIPAddress=_DeviceIPAddress_Object((1,3,6,1,4,1,38783,4,1),_DeviceIPAddress_Type())
deviceIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceIPAddress.setStatus(_B)
_SubnetMask_Type=IpAddress
_SubnetMask_Object=MibScalar
subnetMask=_SubnetMask_Object((1,3,6,1,4,1,38783,4,2),_SubnetMask_Type())
subnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:subnetMask.setStatus(_B)
_Gateway_Type=IpAddress
_Gateway_Object=MibScalar
gateway=_Gateway_Object((1,3,6,1,4,1,38783,4,3),_Gateway_Type())
gateway.setMaxAccess(_C)
if mibBuilder.loadTexts:gateway.setStatus(_B)
_DeviceMACAddress_Type=MacAddress
_DeviceMACAddress_Object=MibScalar
deviceMACAddress=_DeviceMACAddress_Object((1,3,6,1,4,1,38783,4,4),_DeviceMACAddress_Type())
deviceMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceMACAddress.setStatus(_B)
class _DhcpConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_DhcpConfig_Type.__name__=_D
_DhcpConfig_Object=MibScalar
dhcpConfig=_DhcpConfig_Object((1,3,6,1,4,1,38783,4,5),_DhcpConfig_Type())
dhcpConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:dhcpConfig.setStatus(_B)
_IoSetup_ObjectIdentity=ObjectIdentity
ioSetup=_IoSetup_ObjectIdentity((1,3,6,1,4,1,38783,5))
class _Relay1PulseDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,253))
_Relay1PulseDuration_Type.__name__=_D
_Relay1PulseDuration_Object=MibScalar
relay1PulseDuration=_Relay1PulseDuration_Object((1,3,6,1,4,1,38783,5,1),_Relay1PulseDuration_Type())
relay1PulseDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:relay1PulseDuration.setStatus(_B)
class _Relay2PulseDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,253))
_Relay2PulseDuration_Type.__name__=_D
_Relay2PulseDuration_Object=MibScalar
relay2PulseDuration=_Relay2PulseDuration_Object((1,3,6,1,4,1,38783,5,2),_Relay2PulseDuration_Type())
relay2PulseDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:relay2PulseDuration.setStatus(_B)
class _Relay3PulseDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,253))
_Relay3PulseDuration_Type.__name__=_D
_Relay3PulseDuration_Object=MibScalar
relay3PulseDuration=_Relay3PulseDuration_Object((1,3,6,1,4,1,38783,5,3),_Relay3PulseDuration_Type())
relay3PulseDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:relay3PulseDuration.setStatus(_B)
class _Relay4PulseDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,253))
_Relay4PulseDuration_Type.__name__=_D
_Relay4PulseDuration_Object=MibScalar
relay4PulseDuration=_Relay4PulseDuration_Object((1,3,6,1,4,1,38783,5,4),_Relay4PulseDuration_Type())
relay4PulseDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:relay4PulseDuration.setStatus(_B)
class _Relay5PulseDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,253))
_Relay5PulseDuration_Type.__name__=_D
_Relay5PulseDuration_Object=MibScalar
relay5PulseDuration=_Relay5PulseDuration_Object((1,3,6,1,4,1,38783,5,5),_Relay5PulseDuration_Type())
relay5PulseDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:relay5PulseDuration.setStatus(_B)
class _Relay6PulseDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,253))
_Relay6PulseDuration_Type.__name__=_D
_Relay6PulseDuration_Object=MibScalar
relay6PulseDuration=_Relay6PulseDuration_Object((1,3,6,1,4,1,38783,5,6),_Relay6PulseDuration_Type())
relay6PulseDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:relay6PulseDuration.setStatus(_B)
class _Relay7PulseDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,253))
_Relay7PulseDuration_Type.__name__=_D
_Relay7PulseDuration_Object=MibScalar
relay7PulseDuration=_Relay7PulseDuration_Object((1,3,6,1,4,1,38783,5,7),_Relay7PulseDuration_Type())
relay7PulseDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:relay7PulseDuration.setStatus(_B)
class _Relay8PulseDuration_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,253))
_Relay8PulseDuration_Type.__name__=_D
_Relay8PulseDuration_Object=MibScalar
relay8PulseDuration=_Relay8PulseDuration_Object((1,3,6,1,4,1,38783,5,8),_Relay8PulseDuration_Type())
relay8PulseDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:relay8PulseDuration.setStatus(_B)
class _Relay1description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_Relay1description_Type.__name__=_G
_Relay1description_Object=MibScalar
relay1description=_Relay1description_Object((1,3,6,1,4,1,38783,5,9),_Relay1description_Type())
relay1description.setMaxAccess(_C)
if mibBuilder.loadTexts:relay1description.setStatus(_B)
class _Relay2description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_Relay2description_Type.__name__=_G
_Relay2description_Object=MibScalar
relay2description=_Relay2description_Object((1,3,6,1,4,1,38783,5,10),_Relay2description_Type())
relay2description.setMaxAccess(_C)
if mibBuilder.loadTexts:relay2description.setStatus(_B)
class _Relay3description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_Relay3description_Type.__name__=_G
_Relay3description_Object=MibScalar
relay3description=_Relay3description_Object((1,3,6,1,4,1,38783,5,11),_Relay3description_Type())
relay3description.setMaxAccess(_C)
if mibBuilder.loadTexts:relay3description.setStatus(_B)
class _Relay4description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_Relay4description_Type.__name__=_G
_Relay4description_Object=MibScalar
relay4description=_Relay4description_Object((1,3,6,1,4,1,38783,5,12),_Relay4description_Type())
relay4description.setMaxAccess(_C)
if mibBuilder.loadTexts:relay4description.setStatus(_B)
class _Relay5description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_Relay5description_Type.__name__=_G
_Relay5description_Object=MibScalar
relay5description=_Relay5description_Object((1,3,6,1,4,1,38783,5,13),_Relay5description_Type())
relay5description.setMaxAccess(_C)
if mibBuilder.loadTexts:relay5description.setStatus(_B)
class _Relay6description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_Relay6description_Type.__name__=_G
_Relay6description_Object=MibScalar
relay6description=_Relay6description_Object((1,3,6,1,4,1,38783,5,14),_Relay6description_Type())
relay6description.setMaxAccess(_C)
if mibBuilder.loadTexts:relay6description.setStatus(_B)
class _Relay7description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_Relay7description_Type.__name__=_G
_Relay7description_Object=MibScalar
relay7description=_Relay7description_Object((1,3,6,1,4,1,38783,5,15),_Relay7description_Type())
relay7description.setMaxAccess(_C)
if mibBuilder.loadTexts:relay7description.setStatus(_B)
class _Relay8description_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_Relay8description_Type.__name__=_G
_Relay8description_Object=MibScalar
relay8description=_Relay8description_Object((1,3,6,1,4,1,38783,5,16),_Relay8description_Type())
relay8description.setMaxAccess(_C)
if mibBuilder.loadTexts:relay8description.setStatus(_B)
class _DigitalInputAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('noAction',0),('mailIfOpenToClosed',1),('mailIfClosedToOpen',2)))
_DigitalInputAction_Type.__name__=_D
_DigitalInputAction_Object=MibScalar
digitalInputAction=_DigitalInputAction_Object((1,3,6,1,4,1,38783,5,17),_DigitalInputAction_Type())
digitalInputAction.setMaxAccess(_C)
if mibBuilder.loadTexts:digitalInputAction.setStatus(_B)
class _DigitalInputTo_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,38))
_DigitalInputTo_Type.__name__=_G
_DigitalInputTo_Object=MibScalar
digitalInputTo=_DigitalInputTo_Object((1,3,6,1,4,1,38783,5,18),_DigitalInputTo_Type())
digitalInputTo.setMaxAccess(_C)
if mibBuilder.loadTexts:digitalInputTo.setStatus(_B)
class _DigitalInputSubject_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_DigitalInputSubject_Type.__name__=_G
_DigitalInputSubject_Object=MibScalar
digitalInputSubject=_DigitalInputSubject_Object((1,3,6,1,4,1,38783,5,19),_DigitalInputSubject_Type())
digitalInputSubject.setMaxAccess(_C)
if mibBuilder.loadTexts:digitalInputSubject.setStatus(_B)
class _DigitalInputBody_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,22))
_DigitalInputBody_Type.__name__=_G
_DigitalInputBody_Object=MibScalar
digitalInputBody=_DigitalInputBody_Object((1,3,6,1,4,1,38783,5,20),_DigitalInputBody_Type())
digitalInputBody.setMaxAccess(_C)
if mibBuilder.loadTexts:digitalInputBody.setStatus(_B)
class _Relay1PulseDurationMs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_Relay1PulseDurationMs_Type.__name__=_D
_Relay1PulseDurationMs_Object=MibScalar
relay1PulseDurationMs=_Relay1PulseDurationMs_Object((1,3,6,1,4,1,38783,5,21),_Relay1PulseDurationMs_Type())
relay1PulseDurationMs.setMaxAccess(_C)
if mibBuilder.loadTexts:relay1PulseDurationMs.setStatus(_B)
class _Relay2PulseDurationMs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_Relay2PulseDurationMs_Type.__name__=_D
_Relay2PulseDurationMs_Object=MibScalar
relay2PulseDurationMs=_Relay2PulseDurationMs_Object((1,3,6,1,4,1,38783,5,22),_Relay2PulseDurationMs_Type())
relay2PulseDurationMs.setMaxAccess(_C)
if mibBuilder.loadTexts:relay2PulseDurationMs.setStatus(_B)
class _Relay3PulseDurationMs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_Relay3PulseDurationMs_Type.__name__=_D
_Relay3PulseDurationMs_Object=MibScalar
relay3PulseDurationMs=_Relay3PulseDurationMs_Object((1,3,6,1,4,1,38783,5,23),_Relay3PulseDurationMs_Type())
relay3PulseDurationMs.setMaxAccess(_C)
if mibBuilder.loadTexts:relay3PulseDurationMs.setStatus(_B)
class _Relay4PulseDurationMs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_Relay4PulseDurationMs_Type.__name__=_D
_Relay4PulseDurationMs_Object=MibScalar
relay4PulseDurationMs=_Relay4PulseDurationMs_Object((1,3,6,1,4,1,38783,5,24),_Relay4PulseDurationMs_Type())
relay4PulseDurationMs.setMaxAccess(_C)
if mibBuilder.loadTexts:relay4PulseDurationMs.setStatus(_B)
class _Relay5PulseDurationMs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_Relay5PulseDurationMs_Type.__name__=_D
_Relay5PulseDurationMs_Object=MibScalar
relay5PulseDurationMs=_Relay5PulseDurationMs_Object((1,3,6,1,4,1,38783,5,25),_Relay5PulseDurationMs_Type())
relay5PulseDurationMs.setMaxAccess(_C)
if mibBuilder.loadTexts:relay5PulseDurationMs.setStatus(_B)
class _Relay6PulseDurationMs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_Relay6PulseDurationMs_Type.__name__=_D
_Relay6PulseDurationMs_Object=MibScalar
relay6PulseDurationMs=_Relay6PulseDurationMs_Object((1,3,6,1,4,1,38783,5,26),_Relay6PulseDurationMs_Type())
relay6PulseDurationMs.setMaxAccess(_C)
if mibBuilder.loadTexts:relay6PulseDurationMs.setStatus(_B)
class _Relay7PulseDurationMs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_Relay7PulseDurationMs_Type.__name__=_D
_Relay7PulseDurationMs_Object=MibScalar
relay7PulseDurationMs=_Relay7PulseDurationMs_Object((1,3,6,1,4,1,38783,5,27),_Relay7PulseDurationMs_Type())
relay7PulseDurationMs.setMaxAccess(_C)
if mibBuilder.loadTexts:relay7PulseDurationMs.setStatus(_B)
class _Relay8PulseDurationMs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,9))
_Relay8PulseDurationMs_Type.__name__=_D
_Relay8PulseDurationMs_Object=MibScalar
relay8PulseDurationMs=_Relay8PulseDurationMs_Object((1,3,6,1,4,1,38783,5,28),_Relay8PulseDurationMs_Type())
relay8PulseDurationMs.setMaxAccess(_C)
if mibBuilder.loadTexts:relay8PulseDurationMs.setStatus(_B)
class _DigitalInputDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_DigitalInputDescription_Type.__name__=_G
_DigitalInputDescription_Object=MibScalar
digitalInputDescription=_DigitalInputDescription_Object((1,3,6,1,4,1,38783,5,29),_DigitalInputDescription_Type())
digitalInputDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:digitalInputDescription.setStatus(_B)
class _ConfigurationSaved_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('unsaved',0),('saved',1)))
_ConfigurationSaved_Type.__name__=_D
_ConfigurationSaved_Object=MibScalar
configurationSaved=_ConfigurationSaved_Object((1,3,6,1,4,1,38783,6),_ConfigurationSaved_Type())
configurationSaved.setMaxAccess(_C)
if mibBuilder.loadTexts:configurationSaved.setStatus(_B)
class _RestartDevice_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('cancel',0),('restart',1)))
_RestartDevice_Type.__name__=_D
_RestartDevice_Object=MibScalar
restartDevice=_RestartDevice_Object((1,3,6,1,4,1,38783,7),_RestartDevice_Type())
restartDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:restartDevice.setStatus(_B)
_Tcw181bMIBConformance_ObjectIdentity=ObjectIdentity
tcw181bMIBConformance=_Tcw181bMIBConformance_ObjectIdentity((1,3,6,1,4,1,38783,8))
_Tcw181bMIBCompliances_ObjectIdentity=ObjectIdentity
tcw181bMIBCompliances=_Tcw181bMIBCompliances_ObjectIdentity((1,3,6,1,4,1,38783,8,1))
_Tcw181bMIBGroups_ObjectIdentity=ObjectIdentity
tcw181bMIBGroups=_Tcw181bMIBGroups_ObjectIdentity((1,3,6,1,4,1,38783,8,2))
tcw181bProductGroup=ObjectGroup((1,3,6,1,4,1,38783,8,2,1))
tcw181bProductGroup.setObjects(*((_A,'name'),(_A,_K),(_A,'date')))
if mibBuilder.loadTexts:tcw181bProductGroup.setStatus(_B)
tcw181bSnmpSetupGroup=ObjectGroup((1,3,6,1,4,1,38783,8,2,2))
tcw181bSnmpSetupGroup.setObjects(*((_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:tcw181bSnmpSetupGroup.setStatus(_B)
tcw181bMonitorGroup=ObjectGroup((1,3,6,1,4,1,38783,8,2,3))
tcw181bMonitorGroup.setObjects(*((_A,_I),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,'allOn'),(_A,_e),(_A,_f)))
if mibBuilder.loadTexts:tcw181bMonitorGroup.setStatus(_B)
tcw181bNetworkGroup=ObjectGroup((1,3,6,1,4,1,38783,8,2,4))
tcw181bNetworkGroup.setObjects(*((_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k)))
if mibBuilder.loadTexts:tcw181bNetworkGroup.setStatus(_B)
tcw181bIOSetupGroup=ObjectGroup((1,3,6,1,4,1,38783,8,2,5))
tcw181bIOSetupGroup.setObjects(*((_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_J)))
if mibBuilder.loadTexts:tcw181bIOSetupGroup.setStatus(_B)
snmp_trap_notification=NotificationType((1,3,6,1,4,1,38783,0,1))
snmp_trap_notification.setObjects(*((_A,_I),(_A,_J)))
if mibBuilder.loadTexts:snmp_trap_notification.setStatus(_B)
tcw181bTrapGroup=NotificationGroup((1,3,6,1,4,1,38783,8,2,8))
tcw181bTrapGroup.setObjects((_A,_AF))
if mibBuilder.loadTexts:tcw181bTrapGroup.setStatus(_B)
tcw181bMIBCompliances1=ModuleCompliance((1,3,6,1,4,1,38783,8,1,1))
tcw181bMIBCompliances1.setObjects(*((_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL)))
if mibBuilder.loadTexts:tcw181bMIBCompliances1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'teracom':teracom,'trapNotifications':trapNotifications,_AF:snmp_trap_notification,'product':product,'name':name,_K:version,'date':date,'snmpSetup':snmpSetup,_L:trapEnabled,_M:trapReceiverIPAddress,_N:trapCommunity,'monitorNcontrol':monitorNcontrol,_I:digitalInput,_O:relay1,_P:relay2,_Q:relay3,_R:relay4,_S:relay5,_T:relay6,_U:relay7,_V:relay8,_W:pulse1,_X:pulse2,_Y:pulse3,_Z:pulse4,_a:pulse5,_b:pulse6,_c:pulse7,_d:pulse8,'allOn':allOn,_e:allOff,_f:allPulse,'network':network,_g:deviceIPAddress,_h:subnetMask,_i:gateway,_j:deviceMACAddress,_k:dhcpConfig,'ioSetup':ioSetup,_l:relay1PulseDuration,_m:relay2PulseDuration,_n:relay3PulseDuration,_o:relay4PulseDuration,_p:relay5PulseDuration,_q:relay6PulseDuration,_r:relay7PulseDuration,_s:relay8PulseDuration,_t:relay1description,_u:relay2description,_v:relay3description,_w:relay4description,_x:relay5description,_y:relay6description,_z:relay7description,_A0:relay8description,_A1:digitalInputAction,_A2:digitalInputTo,_A3:digitalInputSubject,_A4:digitalInputBody,_A5:relay1PulseDurationMs,_A6:relay2PulseDurationMs,_A7:relay3PulseDurationMs,_A8:relay4PulseDurationMs,_A9:relay5PulseDurationMs,_AA:relay6PulseDurationMs,_AB:relay7PulseDurationMs,_AC:relay8PulseDurationMs,_AD:digitalInputDescription,_AE:configurationSaved,_J:restartDevice,'tcw181bMIBConformance':tcw181bMIBConformance,'tcw181bMIBCompliances':tcw181bMIBCompliances,'tcw181bMIBCompliances1':tcw181bMIBCompliances1,'tcw181bMIBGroups':tcw181bMIBGroups,_AG:tcw181bProductGroup,_AH:tcw181bSnmpSetupGroup,_AI:tcw181bMonitorGroup,_AJ:tcw181bNetworkGroup,_AK:tcw181bIOSetupGroup,_AL:tcw181bTrapGroup,'snmpMIB':snmpMIB})