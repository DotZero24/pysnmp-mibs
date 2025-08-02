_H='rsClientDHCPServerConnIPAddr'
_G='RAPID-CLIENT-MIB'
_F='enabled'
_E='disabled'
_D='OctetString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rapidstream,=mibBuilder.importSymbols('RAPID-MIB','rapidstream')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
rsInfoModule=ModuleIdentity((1,3,6,1,4,1,4355,6))
if mibBuilder.loadTexts:rsInfoModule.setRevisions(('2001-04-20 12:00','2002-11-01 12:00'))
_RsClientMIB_ObjectIdentity=ObjectIdentity
rsClientMIB=_RsClientMIB_ObjectIdentity((1,3,6,1,4,1,4355,6,2))
if mibBuilder.loadTexts:rsClientMIB.setStatus(_A)
_RsClientDHCPServer_ObjectIdentity=ObjectIdentity
rsClientDHCPServer=_RsClientDHCPServer_ObjectIdentity((1,3,6,1,4,1,4355,6,2,1))
if mibBuilder.loadTexts:rsClientDHCPServer.setStatus(_A)
class _RsClientDHCPServerEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_F,1),('relay',2)))
_RsClientDHCPServerEnable_Type.__name__=_C
_RsClientDHCPServerEnable_Object=MibScalar
rsClientDHCPServerEnable=_RsClientDHCPServerEnable_Object((1,3,6,1,4,1,4355,6,2,1,1),_RsClientDHCPServerEnable_Type())
rsClientDHCPServerEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rsClientDHCPServerEnable.setStatus(_A)
_RsClientDHCPServerStartIpAddress_Type=IpAddress
_RsClientDHCPServerStartIpAddress_Object=MibScalar
rsClientDHCPServerStartIpAddress=_RsClientDHCPServerStartIpAddress_Object((1,3,6,1,4,1,4355,6,2,1,2),_RsClientDHCPServerStartIpAddress_Type())
rsClientDHCPServerStartIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rsClientDHCPServerStartIpAddress.setStatus(_A)
_RsClientDHCPServerEndIpAddress_Type=IpAddress
_RsClientDHCPServerEndIpAddress_Object=MibScalar
rsClientDHCPServerEndIpAddress=_RsClientDHCPServerEndIpAddress_Object((1,3,6,1,4,1,4355,6,2,1,3),_RsClientDHCPServerEndIpAddress_Type())
rsClientDHCPServerEndIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:rsClientDHCPServerEndIpAddress.setStatus(_A)
_RsClientDHCPServerLeaseTime_Type=TimeTicks
_RsClientDHCPServerLeaseTime_Object=MibScalar
rsClientDHCPServerLeaseTime=_RsClientDHCPServerLeaseTime_Object((1,3,6,1,4,1,4355,6,2,1,4),_RsClientDHCPServerLeaseTime_Type())
rsClientDHCPServerLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rsClientDHCPServerLeaseTime.setStatus(_A)
_RsClientDHCPServerNum_Type=Unsigned32
_RsClientDHCPServerNum_Object=MibScalar
rsClientDHCPServerNum=_RsClientDHCPServerNum_Object((1,3,6,1,4,1,4355,6,2,1,5),_RsClientDHCPServerNum_Type())
rsClientDHCPServerNum.setMaxAccess(_B)
if mibBuilder.loadTexts:rsClientDHCPServerNum.setStatus(_A)
_RsClientDHCPServerConnTable_Object=MibTable
rsClientDHCPServerConnTable=_RsClientDHCPServerConnTable_Object((1,3,6,1,4,1,4355,6,2,1,6))
if mibBuilder.loadTexts:rsClientDHCPServerConnTable.setStatus(_A)
_RsClientDHCPServerConnEntry_Object=MibTableRow
rsClientDHCPServerConnEntry=_RsClientDHCPServerConnEntry_Object((1,3,6,1,4,1,4355,6,2,1,6,1))
rsClientDHCPServerConnEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:rsClientDHCPServerConnEntry.setStatus(_A)
_RsClientDHCPServerConnClientHostName_Type=OctetString
_RsClientDHCPServerConnClientHostName_Object=MibTableColumn
rsClientDHCPServerConnClientHostName=_RsClientDHCPServerConnClientHostName_Object((1,3,6,1,4,1,4355,6,2,1,6,1,1),_RsClientDHCPServerConnClientHostName_Type())
rsClientDHCPServerConnClientHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:rsClientDHCPServerConnClientHostName.setStatus(_A)
_RsClientDHCPServerConnIPAddr_Type=IpAddress
_RsClientDHCPServerConnIPAddr_Object=MibTableColumn
rsClientDHCPServerConnIPAddr=_RsClientDHCPServerConnIPAddr_Object((1,3,6,1,4,1,4355,6,2,1,6,1,2),_RsClientDHCPServerConnIPAddr_Type())
rsClientDHCPServerConnIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rsClientDHCPServerConnIPAddr.setStatus(_A)
class _RsClientDHCPServerConnMACAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_RsClientDHCPServerConnMACAddr_Type.__name__=_D
_RsClientDHCPServerConnMACAddr_Object=MibTableColumn
rsClientDHCPServerConnMACAddr=_RsClientDHCPServerConnMACAddr_Object((1,3,6,1,4,1,4355,6,2,1,6,1,3),_RsClientDHCPServerConnMACAddr_Type())
rsClientDHCPServerConnMACAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rsClientDHCPServerConnMACAddr.setStatus(_A)
_RsClientDHCPServerConnLeaseTimeStart_Type=DateAndTime
_RsClientDHCPServerConnLeaseTimeStart_Object=MibTableColumn
rsClientDHCPServerConnLeaseTimeStart=_RsClientDHCPServerConnLeaseTimeStart_Object((1,3,6,1,4,1,4355,6,2,1,6,1,4),_RsClientDHCPServerConnLeaseTimeStart_Type())
rsClientDHCPServerConnLeaseTimeStart.setMaxAccess(_B)
if mibBuilder.loadTexts:rsClientDHCPServerConnLeaseTimeStart.setStatus(_A)
_RsClientDHCPServerConnLeaseTimeEnd_Type=DateAndTime
_RsClientDHCPServerConnLeaseTimeEnd_Object=MibTableColumn
rsClientDHCPServerConnLeaseTimeEnd=_RsClientDHCPServerConnLeaseTimeEnd_Object((1,3,6,1,4,1,4355,6,2,1,6,1,5),_RsClientDHCPServerConnLeaseTimeEnd_Type())
rsClientDHCPServerConnLeaseTimeEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:rsClientDHCPServerConnLeaseTimeEnd.setStatus(_A)
_RsClientDHCPServerRelayServer_Type=IpAddress
_RsClientDHCPServerRelayServer_Object=MibScalar
rsClientDHCPServerRelayServer=_RsClientDHCPServerRelayServer_Object((1,3,6,1,4,1,4355,6,2,1,7),_RsClientDHCPServerRelayServer_Type())
rsClientDHCPServerRelayServer.setMaxAccess(_B)
if mibBuilder.loadTexts:rsClientDHCPServerRelayServer.setStatus(_A)
_RsClientDHCPClient_ObjectIdentity=ObjectIdentity
rsClientDHCPClient=_RsClientDHCPClient_ObjectIdentity((1,3,6,1,4,1,4355,6,2,2))
if mibBuilder.loadTexts:rsClientDHCPClient.setStatus(_A)
class _RsClientDHCPClientEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_RsClientDHCPClientEnable_Type.__name__=_C
_RsClientDHCPClientEnable_Object=MibScalar
rsClientDHCPClientEnable=_RsClientDHCPClientEnable_Object((1,3,6,1,4,1,4355,6,2,2,1),_RsClientDHCPClientEnable_Type())
rsClientDHCPClientEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rsClientDHCPClientEnable.setStatus(_A)
_RsClientDHCPClientDomainName_Type=OctetString
_RsClientDHCPClientDomainName_Object=MibScalar
rsClientDHCPClientDomainName=_RsClientDHCPClientDomainName_Object((1,3,6,1,4,1,4355,6,2,2,2),_RsClientDHCPClientDomainName_Type())
rsClientDHCPClientDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:rsClientDHCPClientDomainName.setStatus(_A)
_RsClientDHCPClientDefaultGateway_Type=IpAddress
_RsClientDHCPClientDefaultGateway_Object=MibScalar
rsClientDHCPClientDefaultGateway=_RsClientDHCPClientDefaultGateway_Object((1,3,6,1,4,1,4355,6,2,2,3),_RsClientDHCPClientDefaultGateway_Type())
rsClientDHCPClientDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:rsClientDHCPClientDefaultGateway.setStatus(_A)
_RsClientDHCPClientDNSOne_Type=IpAddress
_RsClientDHCPClientDNSOne_Object=MibScalar
rsClientDHCPClientDNSOne=_RsClientDHCPClientDNSOne_Object((1,3,6,1,4,1,4355,6,2,2,4),_RsClientDHCPClientDNSOne_Type())
rsClientDHCPClientDNSOne.setMaxAccess(_B)
if mibBuilder.loadTexts:rsClientDHCPClientDNSOne.setStatus(_A)
_RsClientDHCPClientDNSTwo_Type=IpAddress
_RsClientDHCPClientDNSTwo_Object=MibScalar
rsClientDHCPClientDNSTwo=_RsClientDHCPClientDNSTwo_Object((1,3,6,1,4,1,4355,6,2,2,5),_RsClientDHCPClientDNSTwo_Type())
rsClientDHCPClientDNSTwo.setMaxAccess(_B)
if mibBuilder.loadTexts:rsClientDHCPClientDNSTwo.setStatus(_A)
_RsClientPPPoEClient_ObjectIdentity=ObjectIdentity
rsClientPPPoEClient=_RsClientPPPoEClient_ObjectIdentity((1,3,6,1,4,1,4355,6,2,3))
if mibBuilder.loadTexts:rsClientPPPoEClient.setStatus(_A)
class _RsClientPPPoEClientEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_RsClientPPPoEClientEnable_Type.__name__=_C
_RsClientPPPoEClientEnable_Object=MibScalar
rsClientPPPoEClientEnable=_RsClientPPPoEClientEnable_Object((1,3,6,1,4,1,4355,6,2,3,1),_RsClientPPPoEClientEnable_Type())
rsClientPPPoEClientEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rsClientPPPoEClientEnable.setStatus(_A)
class _RsClientPPPoEClientADSLStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('disconnect',0),('initialize',1),('establish',2),('authenticate',3),('network',4),('running',5)))
_RsClientPPPoEClientADSLStatus_Type.__name__=_C
_RsClientPPPoEClientADSLStatus_Object=MibScalar
rsClientPPPoEClientADSLStatus=_RsClientPPPoEClientADSLStatus_Object((1,3,6,1,4,1,4355,6,2,3,2),_RsClientPPPoEClientADSLStatus_Type())
rsClientPPPoEClientADSLStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rsClientPPPoEClientADSLStatus.setStatus(_A)
_RsClientPPPoEClientLocalIPAddr_Type=IpAddress
_RsClientPPPoEClientLocalIPAddr_Object=MibScalar
rsClientPPPoEClientLocalIPAddr=_RsClientPPPoEClientLocalIPAddr_Object((1,3,6,1,4,1,4355,6,2,3,3),_RsClientPPPoEClientLocalIPAddr_Type())
rsClientPPPoEClientLocalIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rsClientPPPoEClientLocalIPAddr.setStatus(_A)
_RsClientPPPoEClientRemoteIPAddr_Type=IpAddress
_RsClientPPPoEClientRemoteIPAddr_Object=MibScalar
rsClientPPPoEClientRemoteIPAddr=_RsClientPPPoEClientRemoteIPAddr_Object((1,3,6,1,4,1,4355,6,2,3,4),_RsClientPPPoEClientRemoteIPAddr_Type())
rsClientPPPoEClientRemoteIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rsClientPPPoEClientRemoteIPAddr.setStatus(_A)
_RsClientPPPoEClientNetMask_Type=IpAddress
_RsClientPPPoEClientNetMask_Object=MibScalar
rsClientPPPoEClientNetMask=_RsClientPPPoEClientNetMask_Object((1,3,6,1,4,1,4355,6,2,3,5),_RsClientPPPoEClientNetMask_Type())
rsClientPPPoEClientNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:rsClientPPPoEClientNetMask.setStatus(_A)
_RsClientPPPoEClientDNSOne_Type=IpAddress
_RsClientPPPoEClientDNSOne_Object=MibScalar
rsClientPPPoEClientDNSOne=_RsClientPPPoEClientDNSOne_Object((1,3,6,1,4,1,4355,6,2,3,6),_RsClientPPPoEClientDNSOne_Type())
rsClientPPPoEClientDNSOne.setMaxAccess(_B)
if mibBuilder.loadTexts:rsClientPPPoEClientDNSOne.setStatus(_A)
_RsClientPPPoEClientDNSTwo_Type=IpAddress
_RsClientPPPoEClientDNSTwo_Object=MibScalar
rsClientPPPoEClientDNSTwo=_RsClientPPPoEClientDNSTwo_Object((1,3,6,1,4,1,4355,6,2,3,7),_RsClientPPPoEClientDNSTwo_Type())
rsClientPPPoEClientDNSTwo.setMaxAccess(_B)
if mibBuilder.loadTexts:rsClientPPPoEClientDNSTwo.setStatus(_A)
class _RsClientPPPoEADSLPeerMACAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_RsClientPPPoEADSLPeerMACAddr_Type.__name__=_D
_RsClientPPPoEADSLPeerMACAddr_Object=MibScalar
rsClientPPPoEADSLPeerMACAddr=_RsClientPPPoEADSLPeerMACAddr_Object((1,3,6,1,4,1,4355,6,2,3,8),_RsClientPPPoEADSLPeerMACAddr_Type())
rsClientPPPoEADSLPeerMACAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:rsClientPPPoEADSLPeerMACAddr.setStatus(_A)
_RsClientPPPoEClientConnTime_Type=TimeTicks
_RsClientPPPoEClientConnTime_Object=MibScalar
rsClientPPPoEClientConnTime=_RsClientPPPoEClientConnTime_Object((1,3,6,1,4,1,4355,6,2,3,9),_RsClientPPPoEClientConnTime_Type())
rsClientPPPoEClientConnTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rsClientPPPoEClientConnTime.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'rsInfoModule':rsInfoModule,'rsClientMIB':rsClientMIB,'rsClientDHCPServer':rsClientDHCPServer,'rsClientDHCPServerEnable':rsClientDHCPServerEnable,'rsClientDHCPServerStartIpAddress':rsClientDHCPServerStartIpAddress,'rsClientDHCPServerEndIpAddress':rsClientDHCPServerEndIpAddress,'rsClientDHCPServerLeaseTime':rsClientDHCPServerLeaseTime,'rsClientDHCPServerNum':rsClientDHCPServerNum,'rsClientDHCPServerConnTable':rsClientDHCPServerConnTable,'rsClientDHCPServerConnEntry':rsClientDHCPServerConnEntry,'rsClientDHCPServerConnClientHostName':rsClientDHCPServerConnClientHostName,_H:rsClientDHCPServerConnIPAddr,'rsClientDHCPServerConnMACAddr':rsClientDHCPServerConnMACAddr,'rsClientDHCPServerConnLeaseTimeStart':rsClientDHCPServerConnLeaseTimeStart,'rsClientDHCPServerConnLeaseTimeEnd':rsClientDHCPServerConnLeaseTimeEnd,'rsClientDHCPServerRelayServer':rsClientDHCPServerRelayServer,'rsClientDHCPClient':rsClientDHCPClient,'rsClientDHCPClientEnable':rsClientDHCPClientEnable,'rsClientDHCPClientDomainName':rsClientDHCPClientDomainName,'rsClientDHCPClientDefaultGateway':rsClientDHCPClientDefaultGateway,'rsClientDHCPClientDNSOne':rsClientDHCPClientDNSOne,'rsClientDHCPClientDNSTwo':rsClientDHCPClientDNSTwo,'rsClientPPPoEClient':rsClientPPPoEClient,'rsClientPPPoEClientEnable':rsClientPPPoEClientEnable,'rsClientPPPoEClientADSLStatus':rsClientPPPoEClientADSLStatus,'rsClientPPPoEClientLocalIPAddr':rsClientPPPoEClientLocalIPAddr,'rsClientPPPoEClientRemoteIPAddr':rsClientPPPoEClientRemoteIPAddr,'rsClientPPPoEClientNetMask':rsClientPPPoEClientNetMask,'rsClientPPPoEClientDNSOne':rsClientPPPoEClientDNSOne,'rsClientPPPoEClientDNSTwo':rsClientPPPoEClientDNSTwo,'rsClientPPPoEADSLPeerMACAddr':rsClientPPPoEADSLPeerMACAddr,'rsClientPPPoEClientConnTime':rsClientPPPoEClientConnTime})