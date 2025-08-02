_I='key-128bits'
_H='key-64bits'
_G='NotificationType'
_F='enable'
_E='disable'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso,mgmt=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_G,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_G,'TimeTicks','Unsigned32','enterprises','iso','mgmt')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_SenaoMIB_ObjectIdentity=ObjectIdentity
senaoMIB=_SenaoMIB_ObjectIdentity((1,3,6,1,4,1,14125))
_SenaoRFC1213Group_ObjectIdentity=ObjectIdentity
senaoRFC1213Group=_SenaoRFC1213Group_ObjectIdentity((1,3,6,1,4,1,14125,1))
_Ip_ObjectIdentity=ObjectIdentity
ip=_Ip_ObjectIdentity((1,3,6,1,4,1,14125,1,1))
_IpInReceives_Type=Counter32
_IpInReceives_Object=MibScalar
ipInReceives=_IpInReceives_Object((1,3,6,1,4,1,14125,1,1,1),_IpInReceives_Type())
ipInReceives.setMaxAccess(_C)
if mibBuilder.loadTexts:ipInReceives.setStatus(_A)
_IpForwDatagrams_Type=Counter32
_IpForwDatagrams_Object=MibScalar
ipForwDatagrams=_IpForwDatagrams_Object((1,3,6,1,4,1,14125,1,1,2),_IpForwDatagrams_Type())
ipForwDatagrams.setMaxAccess(_C)
if mibBuilder.loadTexts:ipForwDatagrams.setStatus(_A)
_Icmp_ObjectIdentity=ObjectIdentity
icmp=_Icmp_ObjectIdentity((1,3,6,1,4,1,14125,1,2))
_IcmpInMsgs_Type=Counter32
_IcmpInMsgs_Object=MibScalar
icmpInMsgs=_IcmpInMsgs_Object((1,3,6,1,4,1,14125,1,2,1),_IcmpInMsgs_Type())
icmpInMsgs.setMaxAccess(_C)
if mibBuilder.loadTexts:icmpInMsgs.setStatus(_A)
_IcmpOutMsgs_Type=Counter32
_IcmpOutMsgs_Object=MibScalar
icmpOutMsgs=_IcmpOutMsgs_Object((1,3,6,1,4,1,14125,1,2,2),_IcmpOutMsgs_Type())
icmpOutMsgs.setMaxAccess(_C)
if mibBuilder.loadTexts:icmpOutMsgs.setStatus(_A)
_Tcp_ObjectIdentity=ObjectIdentity
tcp=_Tcp_ObjectIdentity((1,3,6,1,4,1,14125,1,3))
_TcpInSegs_Type=Counter32
_TcpInSegs_Object=MibScalar
tcpInSegs=_TcpInSegs_Object((1,3,6,1,4,1,14125,1,3,1),_TcpInSegs_Type())
tcpInSegs.setMaxAccess(_C)
if mibBuilder.loadTexts:tcpInSegs.setStatus(_A)
_TcpOutSegs_Type=Counter32
_TcpOutSegs_Object=MibScalar
tcpOutSegs=_TcpOutSegs_Object((1,3,6,1,4,1,14125,1,3,2),_TcpOutSegs_Type())
tcpOutSegs.setMaxAccess(_C)
if mibBuilder.loadTexts:tcpOutSegs.setStatus(_A)
_Udp_ObjectIdentity=ObjectIdentity
udp=_Udp_ObjectIdentity((1,3,6,1,4,1,14125,1,4))
_UdpInDatagrams_Type=Counter32
_UdpInDatagrams_Object=MibScalar
udpInDatagrams=_UdpInDatagrams_Object((1,3,6,1,4,1,14125,1,4,1),_UdpInDatagrams_Type())
udpInDatagrams.setMaxAccess(_C)
if mibBuilder.loadTexts:udpInDatagrams.setStatus(_A)
_UdpOutDatagrams_Type=Counter32
_UdpOutDatagrams_Object=MibScalar
udpOutDatagrams=_UdpOutDatagrams_Object((1,3,6,1,4,1,14125,1,4,2),_UdpOutDatagrams_Type())
udpOutDatagrams.setMaxAccess(_C)
if mibBuilder.loadTexts:udpOutDatagrams.setStatus(_A)
_StatusInformationGroup_ObjectIdentity=ObjectIdentity
statusInformationGroup=_StatusInformationGroup_ObjectIdentity((1,3,6,1,4,1,14125,2))
_ConnectedToSSID_Type=DisplayString
_ConnectedToSSID_Object=MibScalar
connectedToSSID=_ConnectedToSSID_Object((1,3,6,1,4,1,14125,2,1),_ConnectedToSSID_Type())
connectedToSSID.setMaxAccess(_B)
if mibBuilder.loadTexts:connectedToSSID.setStatus(_A)
class _UsingChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('channel1',1),('channel2',2),('channel3',3),('channel4',4),('channel5',5),('channel6',6),('channel7',7),('channel8',8),('channel9',9),('channel10',10),('channel11',11)))
_UsingChannel_Type.__name__=_D
_UsingChannel_Object=MibScalar
usingChannel=_UsingChannel_Object((1,3,6,1,4,1,14125,2,2),_UsingChannel_Type())
usingChannel.setMaxAccess(_C)
if mibBuilder.loadTexts:usingChannel.setStatus(_A)
_AccessPointMACAddress_Type=PhysAddress
_AccessPointMACAddress_Object=MibScalar
accessPointMACAddress=_AccessPointMACAddress_Object((1,3,6,1,4,1,14125,2,3),_AccessPointMACAddress_Type())
accessPointMACAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:accessPointMACAddress.setStatus(_A)
_CurrentTransmissionRate_Type=Integer32
_CurrentTransmissionRate_Object=MibScalar
currentTransmissionRate=_CurrentTransmissionRate_Object((1,3,6,1,4,1,14125,2,4),_CurrentTransmissionRate_Type())
currentTransmissionRate.setMaxAccess(_C)
if mibBuilder.loadTexts:currentTransmissionRate.setStatus(_A)
_CurrentIPAddress_Type=IpAddress
_CurrentIPAddress_Object=MibScalar
currentIPAddress=_CurrentIPAddress_Object((1,3,6,1,4,1,14125,2,5),_CurrentIPAddress_Type())
currentIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:currentIPAddress.setStatus(_A)
class _CurrentTXPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('high',1),('medium',2),('low',3)))
_CurrentTXPower_Type.__name__=_D
_CurrentTXPower_Object=MibScalar
currentTXPower=_CurrentTXPower_Object((1,3,6,1,4,1,14125,2,6),_CurrentTXPower_Type())
currentTXPower.setMaxAccess(_B)
if mibBuilder.loadTexts:currentTXPower.setStatus(_A)
_CountersGroup_ObjectIdentity=ObjectIdentity
countersGroup=_CountersGroup_ObjectIdentity((1,3,6,1,4,1,14125,3))
_ReceivedPacketsGoodCount_Type=Counter32
_ReceivedPacketsGoodCount_Object=MibScalar
receivedPacketsGoodCount=_ReceivedPacketsGoodCount_Object((1,3,6,1,4,1,14125,3,1),_ReceivedPacketsGoodCount_Type())
receivedPacketsGoodCount.setMaxAccess(_C)
if mibBuilder.loadTexts:receivedPacketsGoodCount.setStatus(_A)
_ReceivedPacketsBadCount_Type=Counter32
_ReceivedPacketsBadCount_Object=MibScalar
receivedPacketsBadCount=_ReceivedPacketsBadCount_Object((1,3,6,1,4,1,14125,3,2),_ReceivedPacketsBadCount_Type())
receivedPacketsBadCount.setMaxAccess(_C)
if mibBuilder.loadTexts:receivedPacketsBadCount.setStatus(_A)
_SendPacketsGoodCount_Type=Counter32
_SendPacketsGoodCount_Object=MibScalar
sendPacketsGoodCount=_SendPacketsGoodCount_Object((1,3,6,1,4,1,14125,3,3),_SendPacketsGoodCount_Type())
sendPacketsGoodCount.setMaxAccess(_C)
if mibBuilder.loadTexts:sendPacketsGoodCount.setStatus(_A)
_SendPacketsBadCount_Type=Counter32
_SendPacketsBadCount_Object=MibScalar
sendPacketsBadCount=_SendPacketsBadCount_Object((1,3,6,1,4,1,14125,3,4),_SendPacketsBadCount_Type())
sendPacketsBadCount.setMaxAccess(_C)
if mibBuilder.loadTexts:sendPacketsBadCount.setStatus(_A)
_PrivacySettingsGroup_ObjectIdentity=ObjectIdentity
privacySettingsGroup=_PrivacySettingsGroup_ObjectIdentity((1,3,6,1,4,1,14125,4))
class _WepEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_WepEnabled_Type.__name__=_D
_WepEnabled_Object=MibScalar
wepEnabled=_WepEnabled_Object((1,3,6,1,4,1,14125,4,1),_WepEnabled_Type())
wepEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:wepEnabled.setStatus(_A)
class _WepKeyLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_WepKeyLength_Type.__name__=_D
_WepKeyLength_Object=MibScalar
wepKeyLength=_WepKeyLength_Object((1,3,6,1,4,1,14125,4,2),_WepKeyLength_Type())
wepKeyLength.setMaxAccess(_B)
if mibBuilder.loadTexts:wepKeyLength.setStatus(_A)
class _WepKeyNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('wep-key1',1),('wep-key2',2),('wep-key3',3),('wep-key4',4)))
_WepKeyNumber_Type.__name__=_D
_WepKeyNumber_Object=MibScalar
wepKeyNumber=_WepKeyNumber_Object((1,3,6,1,4,1,14125,4,3),_WepKeyNumber_Type())
wepKeyNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:wepKeyNumber.setStatus(_A)
_WepKey_Type=DisplayString
_WepKey_Object=MibScalar
wepKey=_WepKey_Object((1,3,6,1,4,1,14125,4,4),_WepKey_Type())
wepKey.setMaxAccess(_B)
if mibBuilder.loadTexts:wepKey.setStatus(_A)
_SystemSettingsGroup_ObjectIdentity=ObjectIdentity
systemSettingsGroup=_SystemSettingsGroup_ObjectIdentity((1,3,6,1,4,1,14125,5))
class _OperationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bridge',1),('ap-wds',2)))
_OperationMode_Type.__name__=_D
_OperationMode_Object=MibScalar
operationMode=_OperationMode_Object((1,3,6,1,4,1,14125,5,1),_OperationMode_Type())
operationMode.setMaxAccess(_C)
if mibBuilder.loadTexts:operationMode.setStatus(_A)
_IpAddress_Type=IpAddress
_IpAddress_Object=MibScalar
ipAddress=_IpAddress_Object((1,3,6,1,4,1,14125,5,2),_IpAddress_Type())
ipAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:ipAddress.setStatus(_A)
_SubnetMask_Type=IpAddress
_SubnetMask_Object=MibScalar
subnetMask=_SubnetMask_Object((1,3,6,1,4,1,14125,5,3),_SubnetMask_Type())
subnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:subnetMask.setStatus(_A)
_IpGateway_Type=IpAddress
_IpGateway_Object=MibScalar
ipGateway=_IpGateway_Object((1,3,6,1,4,1,14125,5,4),_IpGateway_Type())
ipGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:ipGateway.setStatus(_A)
_DeviceName_Type=DisplayString
_DeviceName_Object=MibScalar
deviceName=_DeviceName_Object((1,3,6,1,4,1,14125,5,5),_DeviceName_Type())
deviceName.setMaxAccess(_B)
if mibBuilder.loadTexts:deviceName.setStatus(_A)
_SaveReboot_Type=Integer32
_SaveReboot_Object=MibScalar
saveReboot=_SaveReboot_Object((1,3,6,1,4,1,14125,5,6),_SaveReboot_Type())
saveReboot.setMaxAccess(_B)
if mibBuilder.loadTexts:saveReboot.setStatus(_A)
_WebAdministratorSettingsGroup_ObjectIdentity=ObjectIdentity
webAdministratorSettingsGroup=_WebAdministratorSettingsGroup_ObjectIdentity((1,3,6,1,4,1,14125,6))
_UserName_Type=DisplayString
_UserName_Object=MibScalar
userName=_UserName_Object((1,3,6,1,4,1,14125,6,1),_UserName_Type())
userName.setMaxAccess(_B)
if mibBuilder.loadTexts:userName.setStatus(_A)
_Password_Type=DisplayString
_Password_Object=MibScalar
password=_Password_Object((1,3,6,1,4,1,14125,6,2),_Password_Type())
password.setMaxAccess(_B)
if mibBuilder.loadTexts:password.setStatus(_A)
_DhcpSettingsGroup_ObjectIdentity=ObjectIdentity
dhcpSettingsGroup=_DhcpSettingsGroup_ObjectIdentity((1,3,6,1,4,1,14125,7))
class _DhcpEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_DhcpEnabled_Type.__name__=_D
_DhcpEnabled_Object=MibScalar
dhcpEnabled=_DhcpEnabled_Object((1,3,6,1,4,1,14125,7,1),_DhcpEnabled_Type())
dhcpEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpEnabled.setStatus(_A)
class _DhcpLeaseTimes_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_DhcpLeaseTimes_Type.__name__=_D
_DhcpLeaseTimes_Object=MibScalar
dhcpLeaseTimes=_DhcpLeaseTimes_Object((1,3,6,1,4,1,14125,7,2),_DhcpLeaseTimes_Type())
dhcpLeaseTimes.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpLeaseTimes.setStatus(_A)
_DhcpIPAddressFrom_Type=IpAddress
_DhcpIPAddressFrom_Object=MibScalar
dhcpIPAddressFrom=_DhcpIPAddressFrom_Object((1,3,6,1,4,1,14125,7,3),_DhcpIPAddressFrom_Type())
dhcpIPAddressFrom.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpIPAddressFrom.setStatus(_A)
_DhcpIPAddressTo_Type=IpAddress
_DhcpIPAddressTo_Object=MibScalar
dhcpIPAddressTo=_DhcpIPAddressTo_Object((1,3,6,1,4,1,14125,7,4),_DhcpIPAddressTo_Type())
dhcpIPAddressTo.setMaxAccess(_B)
if mibBuilder.loadTexts:dhcpIPAddressTo.setStatus(_A)
_WdsSettingsGroup_ObjectIdentity=ObjectIdentity
wdsSettingsGroup=_WdsSettingsGroup_ObjectIdentity((1,3,6,1,4,1,14125,8))
class _WdsEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_WdsEnabled_Type.__name__=_D
_WdsEnabled_Object=MibScalar
wdsEnabled=_WdsEnabled_Object((1,3,6,1,4,1,14125,8,1),_WdsEnabled_Type())
wdsEnabled.setMaxAccess(_B)
if mibBuilder.loadTexts:wdsEnabled.setStatus(_A)
_WdsAPMACAddress1_Type=PhysAddress
_WdsAPMACAddress1_Object=MibScalar
wdsAPMACAddress1=_WdsAPMACAddress1_Object((1,3,6,1,4,1,14125,8,2),_WdsAPMACAddress1_Type())
wdsAPMACAddress1.setMaxAccess(_B)
if mibBuilder.loadTexts:wdsAPMACAddress1.setStatus(_A)
_WdsAPMACAddress2_Type=PhysAddress
_WdsAPMACAddress2_Object=MibScalar
wdsAPMACAddress2=_WdsAPMACAddress2_Object((1,3,6,1,4,1,14125,8,3),_WdsAPMACAddress2_Type())
wdsAPMACAddress2.setMaxAccess(_B)
if mibBuilder.loadTexts:wdsAPMACAddress2.setStatus(_A)
_WdsAPMACAddress3_Type=PhysAddress
_WdsAPMACAddress3_Object=MibScalar
wdsAPMACAddress3=_WdsAPMACAddress3_Object((1,3,6,1,4,1,14125,8,4),_WdsAPMACAddress3_Type())
wdsAPMACAddress3.setMaxAccess(_B)
if mibBuilder.loadTexts:wdsAPMACAddress3.setStatus(_A)
_WdsAPMACAddress4_Type=PhysAddress
_WdsAPMACAddress4_Object=MibScalar
wdsAPMACAddress4=_WdsAPMACAddress4_Object((1,3,6,1,4,1,14125,8,5),_WdsAPMACAddress4_Type())
wdsAPMACAddress4.setMaxAccess(_B)
if mibBuilder.loadTexts:wdsAPMACAddress4.setStatus(_A)
_WdsAPMACAddress5_Type=PhysAddress
_WdsAPMACAddress5_Object=MibScalar
wdsAPMACAddress5=_WdsAPMACAddress5_Object((1,3,6,1,4,1,14125,8,6),_WdsAPMACAddress5_Type())
wdsAPMACAddress5.setMaxAccess(_B)
if mibBuilder.loadTexts:wdsAPMACAddress5.setStatus(_A)
_WdsAPMACAddress6_Type=PhysAddress
_WdsAPMACAddress6_Object=MibScalar
wdsAPMACAddress6=_WdsAPMACAddress6_Object((1,3,6,1,4,1,14125,8,7),_WdsAPMACAddress6_Type())
wdsAPMACAddress6.setMaxAccess(_B)
if mibBuilder.loadTexts:wdsAPMACAddress6.setStatus(_A)
class _WdsKeyUsed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('wep',2)))
_WdsKeyUsed_Type.__name__=_D
_WdsKeyUsed_Object=MibScalar
wdsKeyUsed=_WdsKeyUsed_Object((1,3,6,1,4,1,14125,8,8),_WdsKeyUsed_Type())
wdsKeyUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:wdsKeyUsed.setStatus(_A)
class _WdsKeyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),(_H,2),(_I,3)))
_WdsKeyType_Type.__name__=_D
_WdsKeyType_Object=MibScalar
wdsKeyType=_WdsKeyType_Object((1,3,6,1,4,1,14125,8,9),_WdsKeyType_Type())
wdsKeyType.setMaxAccess(_C)
if mibBuilder.loadTexts:wdsKeyType.setStatus(_A)
mibBuilder.exportSymbols('SENAO-WLAN-AP-MIB',**{'senaoMIB':senaoMIB,'senaoRFC1213Group':senaoRFC1213Group,'ip':ip,'ipInReceives':ipInReceives,'ipForwDatagrams':ipForwDatagrams,'icmp':icmp,'icmpInMsgs':icmpInMsgs,'icmpOutMsgs':icmpOutMsgs,'tcp':tcp,'tcpInSegs':tcpInSegs,'tcpOutSegs':tcpOutSegs,'udp':udp,'udpInDatagrams':udpInDatagrams,'udpOutDatagrams':udpOutDatagrams,'statusInformationGroup':statusInformationGroup,'connectedToSSID':connectedToSSID,'usingChannel':usingChannel,'accessPointMACAddress':accessPointMACAddress,'currentTransmissionRate':currentTransmissionRate,'currentIPAddress':currentIPAddress,'currentTXPower':currentTXPower,'countersGroup':countersGroup,'receivedPacketsGoodCount':receivedPacketsGoodCount,'receivedPacketsBadCount':receivedPacketsBadCount,'sendPacketsGoodCount':sendPacketsGoodCount,'sendPacketsBadCount':sendPacketsBadCount,'privacySettingsGroup':privacySettingsGroup,'wepEnabled':wepEnabled,'wepKeyLength':wepKeyLength,'wepKeyNumber':wepKeyNumber,'wepKey':wepKey,'systemSettingsGroup':systemSettingsGroup,'operationMode':operationMode,'ipAddress':ipAddress,'subnetMask':subnetMask,'ipGateway':ipGateway,'deviceName':deviceName,'saveReboot':saveReboot,'webAdministratorSettingsGroup':webAdministratorSettingsGroup,'userName':userName,'password':password,'dhcpSettingsGroup':dhcpSettingsGroup,'dhcpEnabled':dhcpEnabled,'dhcpLeaseTimes':dhcpLeaseTimes,'dhcpIPAddressFrom':dhcpIPAddressFrom,'dhcpIPAddressTo':dhcpIPAddressTo,'wdsSettingsGroup':wdsSettingsGroup,'wdsEnabled':wdsEnabled,'wdsAPMACAddress1':wdsAPMACAddress1,'wdsAPMACAddress2':wdsAPMACAddress2,'wdsAPMACAddress3':wdsAPMACAddress3,'wdsAPMACAddress4':wdsAPMACAddress4,'wdsAPMACAddress5':wdsAPMACAddress5,'wdsAPMACAddress6':wdsAPMACAddress6,'wdsKeyUsed':wdsKeyUsed,'wdsKeyType':wdsKeyType})