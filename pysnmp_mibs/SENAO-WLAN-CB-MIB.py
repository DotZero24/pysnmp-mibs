_E='NotificationType'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso,mgmt=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier',_E,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_E,'TimeTicks','Unsigned32','enterprises','iso','mgmt')
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
ipInReceives.setMaxAccess(_B)
if mibBuilder.loadTexts:ipInReceives.setStatus(_A)
_IpForwDatagrams_Type=Counter32
_IpForwDatagrams_Object=MibScalar
ipForwDatagrams=_IpForwDatagrams_Object((1,3,6,1,4,1,14125,1,1,2),_IpForwDatagrams_Type())
ipForwDatagrams.setMaxAccess(_B)
if mibBuilder.loadTexts:ipForwDatagrams.setStatus(_A)
_Icmp_ObjectIdentity=ObjectIdentity
icmp=_Icmp_ObjectIdentity((1,3,6,1,4,1,14125,1,2))
_IcmpInMsgs_Type=Counter32
_IcmpInMsgs_Object=MibScalar
icmpInMsgs=_IcmpInMsgs_Object((1,3,6,1,4,1,14125,1,2,1),_IcmpInMsgs_Type())
icmpInMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:icmpInMsgs.setStatus(_A)
_IcmpOutMsgs_Type=Counter32
_IcmpOutMsgs_Object=MibScalar
icmpOutMsgs=_IcmpOutMsgs_Object((1,3,6,1,4,1,14125,1,2,2),_IcmpOutMsgs_Type())
icmpOutMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:icmpOutMsgs.setStatus(_A)
_Tcp_ObjectIdentity=ObjectIdentity
tcp=_Tcp_ObjectIdentity((1,3,6,1,4,1,14125,1,3))
_TcpInSegs_Type=Counter32
_TcpInSegs_Object=MibScalar
tcpInSegs=_TcpInSegs_Object((1,3,6,1,4,1,14125,1,3,1),_TcpInSegs_Type())
tcpInSegs.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpInSegs.setStatus(_A)
_TcpOutSegs_Type=Counter32
_TcpOutSegs_Object=MibScalar
tcpOutSegs=_TcpOutSegs_Object((1,3,6,1,4,1,14125,1,3,2),_TcpOutSegs_Type())
tcpOutSegs.setMaxAccess(_B)
if mibBuilder.loadTexts:tcpOutSegs.setStatus(_A)
_Udp_ObjectIdentity=ObjectIdentity
udp=_Udp_ObjectIdentity((1,3,6,1,4,1,14125,1,4))
_UdpInDatagrams_Type=Counter32
_UdpInDatagrams_Object=MibScalar
udpInDatagrams=_UdpInDatagrams_Object((1,3,6,1,4,1,14125,1,4,1),_UdpInDatagrams_Type())
udpInDatagrams.setMaxAccess(_B)
if mibBuilder.loadTexts:udpInDatagrams.setStatus(_A)
_UdpOutDatagrams_Type=Counter32
_UdpOutDatagrams_Object=MibScalar
udpOutDatagrams=_UdpOutDatagrams_Object((1,3,6,1,4,1,14125,1,4,2),_UdpOutDatagrams_Type())
udpOutDatagrams.setMaxAccess(_B)
if mibBuilder.loadTexts:udpOutDatagrams.setStatus(_A)
_StatusInformationGroup_ObjectIdentity=ObjectIdentity
statusInformationGroup=_StatusInformationGroup_ObjectIdentity((1,3,6,1,4,1,14125,2))
_ConnectedToSSID_Type=DisplayString
_ConnectedToSSID_Object=MibScalar
connectedToSSID=_ConnectedToSSID_Object((1,3,6,1,4,1,14125,2,1),_ConnectedToSSID_Type())
connectedToSSID.setMaxAccess(_C)
if mibBuilder.loadTexts:connectedToSSID.setStatus(_A)
class _UsingChannel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('channel1',1),('channel2',2),('channel3',3),('channel4',4),('channel5',5),('channel6',6),('channel7',7),('channel8',8),('channel9',9),('channel10',10),('channel11',11)))
_UsingChannel_Type.__name__=_D
_UsingChannel_Object=MibScalar
usingChannel=_UsingChannel_Object((1,3,6,1,4,1,14125,2,2),_UsingChannel_Type())
usingChannel.setMaxAccess(_B)
if mibBuilder.loadTexts:usingChannel.setStatus(_A)
_ClientBridgeMACAddress_Type=PhysAddress
_ClientBridgeMACAddress_Object=MibScalar
clientBridgeMACAddress=_ClientBridgeMACAddress_Object((1,3,6,1,4,1,14125,2,3),_ClientBridgeMACAddress_Type())
clientBridgeMACAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:clientBridgeMACAddress.setStatus(_A)
_CurrentIPAddress_Type=IpAddress
_CurrentIPAddress_Object=MibScalar
currentIPAddress=_CurrentIPAddress_Object((1,3,6,1,4,1,14125,2,4),_CurrentIPAddress_Type())
currentIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:currentIPAddress.setStatus(_A)
_LinkUpIndicator_Type=Integer32
_LinkUpIndicator_Object=MibScalar
linkUpIndicator=_LinkUpIndicator_Object((1,3,6,1,4,1,14125,2,5),_LinkUpIndicator_Type())
linkUpIndicator.setMaxAccess(_B)
if mibBuilder.loadTexts:linkUpIndicator.setStatus(_A)
class _ClientSignalStrength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_ClientSignalStrength_Type.__name__=_D
_ClientSignalStrength_Object=MibScalar
clientSignalStrength=_ClientSignalStrength_Object((1,3,6,1,4,1,14125,2,6),_ClientSignalStrength_Type())
clientSignalStrength.setMaxAccess(_B)
if mibBuilder.loadTexts:clientSignalStrength.setStatus(_A)
_ClientAssociationTime_Type=TimeTicks
_ClientAssociationTime_Object=MibScalar
clientAssociationTime=_ClientAssociationTime_Object((1,3,6,1,4,1,14125,2,7),_ClientAssociationTime_Type())
clientAssociationTime.setMaxAccess(_B)
if mibBuilder.loadTexts:clientAssociationTime.setStatus(_A)
class _CurrentTXPower_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('high',1),('medium',2),('low',3)))
_CurrentTXPower_Type.__name__=_D
_CurrentTXPower_Object=MibScalar
currentTXPower=_CurrentTXPower_Object((1,3,6,1,4,1,14125,2,8),_CurrentTXPower_Type())
currentTXPower.setMaxAccess(_C)
if mibBuilder.loadTexts:currentTXPower.setStatus(_A)
_CountersGroup_ObjectIdentity=ObjectIdentity
countersGroup=_CountersGroup_ObjectIdentity((1,3,6,1,4,1,14125,3))
_ReceivedPacketsGoodCount_Type=Counter32
_ReceivedPacketsGoodCount_Object=MibScalar
receivedPacketsGoodCount=_ReceivedPacketsGoodCount_Object((1,3,6,1,4,1,14125,3,1),_ReceivedPacketsGoodCount_Type())
receivedPacketsGoodCount.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedPacketsGoodCount.setStatus(_A)
_ReceivedPacketsBadCount_Type=Counter32
_ReceivedPacketsBadCount_Object=MibScalar
receivedPacketsBadCount=_ReceivedPacketsBadCount_Object((1,3,6,1,4,1,14125,3,2),_ReceivedPacketsBadCount_Type())
receivedPacketsBadCount.setMaxAccess(_B)
if mibBuilder.loadTexts:receivedPacketsBadCount.setStatus(_A)
_SendPacketsGoodCount_Type=Counter32
_SendPacketsGoodCount_Object=MibScalar
sendPacketsGoodCount=_SendPacketsGoodCount_Object((1,3,6,1,4,1,14125,3,3),_SendPacketsGoodCount_Type())
sendPacketsGoodCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sendPacketsGoodCount.setStatus(_A)
_SendPacketsBadCount_Type=Counter32
_SendPacketsBadCount_Object=MibScalar
sendPacketsBadCount=_SendPacketsBadCount_Object((1,3,6,1,4,1,14125,3,4),_SendPacketsBadCount_Type())
sendPacketsBadCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sendPacketsBadCount.setStatus(_A)
_PrivacySettingsGroup_ObjectIdentity=ObjectIdentity
privacySettingsGroup=_PrivacySettingsGroup_ObjectIdentity((1,3,6,1,4,1,14125,4))
class _WepEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_WepEnabled_Type.__name__=_D
_WepEnabled_Object=MibScalar
wepEnabled=_WepEnabled_Object((1,3,6,1,4,1,14125,4,1),_WepEnabled_Type())
wepEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:wepEnabled.setStatus(_A)
class _WepKeyLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('key-64bits',1),('key-128bits',2)))
_WepKeyLength_Type.__name__=_D
_WepKeyLength_Object=MibScalar
wepKeyLength=_WepKeyLength_Object((1,3,6,1,4,1,14125,4,2),_WepKeyLength_Type())
wepKeyLength.setMaxAccess(_C)
if mibBuilder.loadTexts:wepKeyLength.setStatus(_A)
class _WepKeyNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('wep-key1',1),('wep-key2',2),('wep-key3',3),('wep-key4',4)))
_WepKeyNumber_Type.__name__=_D
_WepKeyNumber_Object=MibScalar
wepKeyNumber=_WepKeyNumber_Object((1,3,6,1,4,1,14125,4,3),_WepKeyNumber_Type())
wepKeyNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:wepKeyNumber.setStatus(_A)
_WepKey_Type=DisplayString
_WepKey_Object=MibScalar
wepKey=_WepKey_Object((1,3,6,1,4,1,14125,4,4),_WepKey_Type())
wepKey.setMaxAccess(_C)
if mibBuilder.loadTexts:wepKey.setStatus(_A)
_SystemSettingsGroup_ObjectIdentity=ObjectIdentity
systemSettingsGroup=_SystemSettingsGroup_ObjectIdentity((1,3,6,1,4,1,14125,5))
class _OperationMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bridge',1),('ap-wds',2)))
_OperationMode_Type.__name__=_D
_OperationMode_Object=MibScalar
operationMode=_OperationMode_Object((1,3,6,1,4,1,14125,5,1),_OperationMode_Type())
operationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:operationMode.setStatus(_A)
_IpAddress_Type=IpAddress
_IpAddress_Object=MibScalar
ipAddress=_IpAddress_Object((1,3,6,1,4,1,14125,5,2),_IpAddress_Type())
ipAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ipAddress.setStatus(_A)
_SubnetMask_Type=IpAddress
_SubnetMask_Object=MibScalar
subnetMask=_SubnetMask_Object((1,3,6,1,4,1,14125,5,3),_SubnetMask_Type())
subnetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:subnetMask.setStatus(_A)
_IpGateway_Type=IpAddress
_IpGateway_Object=MibScalar
ipGateway=_IpGateway_Object((1,3,6,1,4,1,14125,5,4),_IpGateway_Type())
ipGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:ipGateway.setStatus(_A)
_DeviceName_Type=DisplayString
_DeviceName_Object=MibScalar
deviceName=_DeviceName_Object((1,3,6,1,4,1,14125,5,5),_DeviceName_Type())
deviceName.setMaxAccess(_C)
if mibBuilder.loadTexts:deviceName.setStatus(_A)
_SaveReboot_Type=Integer32
_SaveReboot_Object=MibScalar
saveReboot=_SaveReboot_Object((1,3,6,1,4,1,14125,5,6),_SaveReboot_Type())
saveReboot.setMaxAccess(_C)
if mibBuilder.loadTexts:saveReboot.setStatus(_A)
_WebAdministratorSettingsGroup_ObjectIdentity=ObjectIdentity
webAdministratorSettingsGroup=_WebAdministratorSettingsGroup_ObjectIdentity((1,3,6,1,4,1,14125,6))
_UserName_Type=DisplayString
_UserName_Object=MibScalar
userName=_UserName_Object((1,3,6,1,4,1,14125,6,1),_UserName_Type())
userName.setMaxAccess(_C)
if mibBuilder.loadTexts:userName.setStatus(_A)
_Password_Type=DisplayString
_Password_Object=MibScalar
password=_Password_Object((1,3,6,1,4,1,14125,6,2),_Password_Type())
password.setMaxAccess(_C)
if mibBuilder.loadTexts:password.setStatus(_A)
mibBuilder.exportSymbols('SENAO-WLAN-CB-MIB',**{'senaoMIB':senaoMIB,'senaoRFC1213Group':senaoRFC1213Group,'ip':ip,'ipInReceives':ipInReceives,'ipForwDatagrams':ipForwDatagrams,'icmp':icmp,'icmpInMsgs':icmpInMsgs,'icmpOutMsgs':icmpOutMsgs,'tcp':tcp,'tcpInSegs':tcpInSegs,'tcpOutSegs':tcpOutSegs,'udp':udp,'udpInDatagrams':udpInDatagrams,'udpOutDatagrams':udpOutDatagrams,'statusInformationGroup':statusInformationGroup,'connectedToSSID':connectedToSSID,'usingChannel':usingChannel,'clientBridgeMACAddress':clientBridgeMACAddress,'currentIPAddress':currentIPAddress,'linkUpIndicator':linkUpIndicator,'clientSignalStrength':clientSignalStrength,'clientAssociationTime':clientAssociationTime,'currentTXPower':currentTXPower,'countersGroup':countersGroup,'receivedPacketsGoodCount':receivedPacketsGoodCount,'receivedPacketsBadCount':receivedPacketsBadCount,'sendPacketsGoodCount':sendPacketsGoodCount,'sendPacketsBadCount':sendPacketsBadCount,'privacySettingsGroup':privacySettingsGroup,'wepEnabled':wepEnabled,'wepKeyLength':wepKeyLength,'wepKeyNumber':wepKeyNumber,'wepKey':wepKey,'systemSettingsGroup':systemSettingsGroup,'operationMode':operationMode,'ipAddress':ipAddress,'subnetMask':subnetMask,'ipGateway':ipGateway,'deviceName':deviceName,'saveReboot':saveReboot,'webAdministratorSettingsGroup':webAdministratorSettingsGroup,'userName':userName,'password':password})