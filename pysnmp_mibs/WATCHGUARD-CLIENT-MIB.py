_H='wgClientDHCPServerConnIPAddr'
_G='WATCHGUARD-CLIENT-MIB'
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
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','TextualConvention')
watchguard,=mibBuilder.importSymbols('WATCHGUARD-SMI','watchguard')
wgInfoModule=ModuleIdentity((1,3,6,1,4,1,3097,6))
if mibBuilder.loadTexts:wgInfoModule.setRevisions(('2007-01-25 12:00',))
_WgClientMIB_ObjectIdentity=ObjectIdentity
wgClientMIB=_WgClientMIB_ObjectIdentity((1,3,6,1,4,1,3097,6,2))
if mibBuilder.loadTexts:wgClientMIB.setStatus(_A)
_WgClientDHCPServer_ObjectIdentity=ObjectIdentity
wgClientDHCPServer=_WgClientDHCPServer_ObjectIdentity((1,3,6,1,4,1,3097,6,2,1))
if mibBuilder.loadTexts:wgClientDHCPServer.setStatus(_A)
class _WgClientDHCPServerEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_E,0),(_F,1),('relay',2)))
_WgClientDHCPServerEnable_Type.__name__=_C
_WgClientDHCPServerEnable_Object=MibScalar
wgClientDHCPServerEnable=_WgClientDHCPServerEnable_Object((1,3,6,1,4,1,3097,6,2,1,1),_WgClientDHCPServerEnable_Type())
wgClientDHCPServerEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClientDHCPServerEnable.setStatus(_A)
_WgClientDHCPServerStartIpAddress_Type=IpAddress
_WgClientDHCPServerStartIpAddress_Object=MibScalar
wgClientDHCPServerStartIpAddress=_WgClientDHCPServerStartIpAddress_Object((1,3,6,1,4,1,3097,6,2,1,2),_WgClientDHCPServerStartIpAddress_Type())
wgClientDHCPServerStartIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClientDHCPServerStartIpAddress.setStatus(_A)
_WgClientDHCPServerEndIpAddress_Type=IpAddress
_WgClientDHCPServerEndIpAddress_Object=MibScalar
wgClientDHCPServerEndIpAddress=_WgClientDHCPServerEndIpAddress_Object((1,3,6,1,4,1,3097,6,2,1,3),_WgClientDHCPServerEndIpAddress_Type())
wgClientDHCPServerEndIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClientDHCPServerEndIpAddress.setStatus(_A)
_WgClientDHCPServerLeaseTime_Type=TimeTicks
_WgClientDHCPServerLeaseTime_Object=MibScalar
wgClientDHCPServerLeaseTime=_WgClientDHCPServerLeaseTime_Object((1,3,6,1,4,1,3097,6,2,1,4),_WgClientDHCPServerLeaseTime_Type())
wgClientDHCPServerLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClientDHCPServerLeaseTime.setStatus(_A)
_WgClientDHCPServerNum_Type=Unsigned32
_WgClientDHCPServerNum_Object=MibScalar
wgClientDHCPServerNum=_WgClientDHCPServerNum_Object((1,3,6,1,4,1,3097,6,2,1,5),_WgClientDHCPServerNum_Type())
wgClientDHCPServerNum.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClientDHCPServerNum.setStatus(_A)
_WgClientDHCPServerConnTable_Object=MibTable
wgClientDHCPServerConnTable=_WgClientDHCPServerConnTable_Object((1,3,6,1,4,1,3097,6,2,1,6))
if mibBuilder.loadTexts:wgClientDHCPServerConnTable.setStatus(_A)
_WgClientDHCPServerConnEntry_Object=MibTableRow
wgClientDHCPServerConnEntry=_WgClientDHCPServerConnEntry_Object((1,3,6,1,4,1,3097,6,2,1,6,1))
wgClientDHCPServerConnEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:wgClientDHCPServerConnEntry.setStatus(_A)
_WgClientDHCPServerConnClientHostName_Type=OctetString
_WgClientDHCPServerConnClientHostName_Object=MibTableColumn
wgClientDHCPServerConnClientHostName=_WgClientDHCPServerConnClientHostName_Object((1,3,6,1,4,1,3097,6,2,1,6,1,1),_WgClientDHCPServerConnClientHostName_Type())
wgClientDHCPServerConnClientHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClientDHCPServerConnClientHostName.setStatus(_A)
_WgClientDHCPServerConnIPAddr_Type=IpAddress
_WgClientDHCPServerConnIPAddr_Object=MibTableColumn
wgClientDHCPServerConnIPAddr=_WgClientDHCPServerConnIPAddr_Object((1,3,6,1,4,1,3097,6,2,1,6,1,2),_WgClientDHCPServerConnIPAddr_Type())
wgClientDHCPServerConnIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClientDHCPServerConnIPAddr.setStatus(_A)
class _WgClientDHCPServerConnMACAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_WgClientDHCPServerConnMACAddr_Type.__name__=_D
_WgClientDHCPServerConnMACAddr_Object=MibTableColumn
wgClientDHCPServerConnMACAddr=_WgClientDHCPServerConnMACAddr_Object((1,3,6,1,4,1,3097,6,2,1,6,1,3),_WgClientDHCPServerConnMACAddr_Type())
wgClientDHCPServerConnMACAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClientDHCPServerConnMACAddr.setStatus(_A)
_WgClientDHCPServerConnLeaseTimeStart_Type=DateAndTime
_WgClientDHCPServerConnLeaseTimeStart_Object=MibTableColumn
wgClientDHCPServerConnLeaseTimeStart=_WgClientDHCPServerConnLeaseTimeStart_Object((1,3,6,1,4,1,3097,6,2,1,6,1,4),_WgClientDHCPServerConnLeaseTimeStart_Type())
wgClientDHCPServerConnLeaseTimeStart.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClientDHCPServerConnLeaseTimeStart.setStatus(_A)
_WgClientDHCPServerConnLeaseTimeEnd_Type=DateAndTime
_WgClientDHCPServerConnLeaseTimeEnd_Object=MibTableColumn
wgClientDHCPServerConnLeaseTimeEnd=_WgClientDHCPServerConnLeaseTimeEnd_Object((1,3,6,1,4,1,3097,6,2,1,6,1,5),_WgClientDHCPServerConnLeaseTimeEnd_Type())
wgClientDHCPServerConnLeaseTimeEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClientDHCPServerConnLeaseTimeEnd.setStatus(_A)
_WgClientDHCPServerRelayServer_Type=IpAddress
_WgClientDHCPServerRelayServer_Object=MibScalar
wgClientDHCPServerRelayServer=_WgClientDHCPServerRelayServer_Object((1,3,6,1,4,1,3097,6,2,1,7),_WgClientDHCPServerRelayServer_Type())
wgClientDHCPServerRelayServer.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClientDHCPServerRelayServer.setStatus(_A)
_WgClientDHCPClient_ObjectIdentity=ObjectIdentity
wgClientDHCPClient=_WgClientDHCPClient_ObjectIdentity((1,3,6,1,4,1,3097,6,2,2))
if mibBuilder.loadTexts:wgClientDHCPClient.setStatus(_A)
class _WgClientDHCPClientEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_WgClientDHCPClientEnable_Type.__name__=_C
_WgClientDHCPClientEnable_Object=MibScalar
wgClientDHCPClientEnable=_WgClientDHCPClientEnable_Object((1,3,6,1,4,1,3097,6,2,2,1),_WgClientDHCPClientEnable_Type())
wgClientDHCPClientEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClientDHCPClientEnable.setStatus(_A)
_WgClientDHCPClientDomainName_Type=OctetString
_WgClientDHCPClientDomainName_Object=MibScalar
wgClientDHCPClientDomainName=_WgClientDHCPClientDomainName_Object((1,3,6,1,4,1,3097,6,2,2,2),_WgClientDHCPClientDomainName_Type())
wgClientDHCPClientDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClientDHCPClientDomainName.setStatus(_A)
_WgClientDHCPClientDefaultGateway_Type=IpAddress
_WgClientDHCPClientDefaultGateway_Object=MibScalar
wgClientDHCPClientDefaultGateway=_WgClientDHCPClientDefaultGateway_Object((1,3,6,1,4,1,3097,6,2,2,3),_WgClientDHCPClientDefaultGateway_Type())
wgClientDHCPClientDefaultGateway.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClientDHCPClientDefaultGateway.setStatus(_A)
_WgClientDHCPClientDNSOne_Type=IpAddress
_WgClientDHCPClientDNSOne_Object=MibScalar
wgClientDHCPClientDNSOne=_WgClientDHCPClientDNSOne_Object((1,3,6,1,4,1,3097,6,2,2,4),_WgClientDHCPClientDNSOne_Type())
wgClientDHCPClientDNSOne.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClientDHCPClientDNSOne.setStatus(_A)
_WgClientDHCPClientDNSTwo_Type=IpAddress
_WgClientDHCPClientDNSTwo_Object=MibScalar
wgClientDHCPClientDNSTwo=_WgClientDHCPClientDNSTwo_Object((1,3,6,1,4,1,3097,6,2,2,5),_WgClientDHCPClientDNSTwo_Type())
wgClientDHCPClientDNSTwo.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClientDHCPClientDNSTwo.setStatus(_A)
_WgClientPPPoEClient_ObjectIdentity=ObjectIdentity
wgClientPPPoEClient=_WgClientPPPoEClient_ObjectIdentity((1,3,6,1,4,1,3097,6,2,3))
if mibBuilder.loadTexts:wgClientPPPoEClient.setStatus(_A)
class _WgClientPPPoEClientEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_WgClientPPPoEClientEnable_Type.__name__=_C
_WgClientPPPoEClientEnable_Object=MibScalar
wgClientPPPoEClientEnable=_WgClientPPPoEClientEnable_Object((1,3,6,1,4,1,3097,6,2,3,1),_WgClientPPPoEClientEnable_Type())
wgClientPPPoEClientEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClientPPPoEClientEnable.setStatus(_A)
class _WgClientPPPoEClientADSLStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('disconnect',0),('initialize',1),('establish',2),('authenticate',3),('network',4),('running',5)))
_WgClientPPPoEClientADSLStatus_Type.__name__=_C
_WgClientPPPoEClientADSLStatus_Object=MibScalar
wgClientPPPoEClientADSLStatus=_WgClientPPPoEClientADSLStatus_Object((1,3,6,1,4,1,3097,6,2,3,2),_WgClientPPPoEClientADSLStatus_Type())
wgClientPPPoEClientADSLStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClientPPPoEClientADSLStatus.setStatus(_A)
_WgClientPPPoEClientLocalIPAddr_Type=IpAddress
_WgClientPPPoEClientLocalIPAddr_Object=MibScalar
wgClientPPPoEClientLocalIPAddr=_WgClientPPPoEClientLocalIPAddr_Object((1,3,6,1,4,1,3097,6,2,3,3),_WgClientPPPoEClientLocalIPAddr_Type())
wgClientPPPoEClientLocalIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClientPPPoEClientLocalIPAddr.setStatus(_A)
_WgClientPPPoEClientRemoteIPAddr_Type=IpAddress
_WgClientPPPoEClientRemoteIPAddr_Object=MibScalar
wgClientPPPoEClientRemoteIPAddr=_WgClientPPPoEClientRemoteIPAddr_Object((1,3,6,1,4,1,3097,6,2,3,4),_WgClientPPPoEClientRemoteIPAddr_Type())
wgClientPPPoEClientRemoteIPAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClientPPPoEClientRemoteIPAddr.setStatus(_A)
_WgClientPPPoEClientNetMask_Type=IpAddress
_WgClientPPPoEClientNetMask_Object=MibScalar
wgClientPPPoEClientNetMask=_WgClientPPPoEClientNetMask_Object((1,3,6,1,4,1,3097,6,2,3,5),_WgClientPPPoEClientNetMask_Type())
wgClientPPPoEClientNetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClientPPPoEClientNetMask.setStatus(_A)
_WgClientPPPoEClientDNSOne_Type=IpAddress
_WgClientPPPoEClientDNSOne_Object=MibScalar
wgClientPPPoEClientDNSOne=_WgClientPPPoEClientDNSOne_Object((1,3,6,1,4,1,3097,6,2,3,6),_WgClientPPPoEClientDNSOne_Type())
wgClientPPPoEClientDNSOne.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClientPPPoEClientDNSOne.setStatus(_A)
_WgClientPPPoEClientDNSTwo_Type=IpAddress
_WgClientPPPoEClientDNSTwo_Object=MibScalar
wgClientPPPoEClientDNSTwo=_WgClientPPPoEClientDNSTwo_Object((1,3,6,1,4,1,3097,6,2,3,7),_WgClientPPPoEClientDNSTwo_Type())
wgClientPPPoEClientDNSTwo.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClientPPPoEClientDNSTwo.setStatus(_A)
class _WgClientPPPoEADSLPeerMACAddr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
_WgClientPPPoEADSLPeerMACAddr_Type.__name__=_D
_WgClientPPPoEADSLPeerMACAddr_Object=MibScalar
wgClientPPPoEADSLPeerMACAddr=_WgClientPPPoEADSLPeerMACAddr_Object((1,3,6,1,4,1,3097,6,2,3,8),_WgClientPPPoEADSLPeerMACAddr_Type())
wgClientPPPoEADSLPeerMACAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClientPPPoEADSLPeerMACAddr.setStatus(_A)
_WgClientPPPoEClientConnTime_Type=TimeTicks
_WgClientPPPoEClientConnTime_Object=MibScalar
wgClientPPPoEClientConnTime=_WgClientPPPoEClientConnTime_Object((1,3,6,1,4,1,3097,6,2,3,9),_WgClientPPPoEClientConnTime_Type())
wgClientPPPoEClientConnTime.setMaxAccess(_B)
if mibBuilder.loadTexts:wgClientPPPoEClientConnTime.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'wgInfoModule':wgInfoModule,'wgClientMIB':wgClientMIB,'wgClientDHCPServer':wgClientDHCPServer,'wgClientDHCPServerEnable':wgClientDHCPServerEnable,'wgClientDHCPServerStartIpAddress':wgClientDHCPServerStartIpAddress,'wgClientDHCPServerEndIpAddress':wgClientDHCPServerEndIpAddress,'wgClientDHCPServerLeaseTime':wgClientDHCPServerLeaseTime,'wgClientDHCPServerNum':wgClientDHCPServerNum,'wgClientDHCPServerConnTable':wgClientDHCPServerConnTable,'wgClientDHCPServerConnEntry':wgClientDHCPServerConnEntry,'wgClientDHCPServerConnClientHostName':wgClientDHCPServerConnClientHostName,_H:wgClientDHCPServerConnIPAddr,'wgClientDHCPServerConnMACAddr':wgClientDHCPServerConnMACAddr,'wgClientDHCPServerConnLeaseTimeStart':wgClientDHCPServerConnLeaseTimeStart,'wgClientDHCPServerConnLeaseTimeEnd':wgClientDHCPServerConnLeaseTimeEnd,'wgClientDHCPServerRelayServer':wgClientDHCPServerRelayServer,'wgClientDHCPClient':wgClientDHCPClient,'wgClientDHCPClientEnable':wgClientDHCPClientEnable,'wgClientDHCPClientDomainName':wgClientDHCPClientDomainName,'wgClientDHCPClientDefaultGateway':wgClientDHCPClientDefaultGateway,'wgClientDHCPClientDNSOne':wgClientDHCPClientDNSOne,'wgClientDHCPClientDNSTwo':wgClientDHCPClientDNSTwo,'wgClientPPPoEClient':wgClientPPPoEClient,'wgClientPPPoEClientEnable':wgClientPPPoEClientEnable,'wgClientPPPoEClientADSLStatus':wgClientPPPoEClientADSLStatus,'wgClientPPPoEClientLocalIPAddr':wgClientPPPoEClientLocalIPAddr,'wgClientPPPoEClientRemoteIPAddr':wgClientPPPoEClientRemoteIPAddr,'wgClientPPPoEClientNetMask':wgClientPPPoEClientNetMask,'wgClientPPPoEClientDNSOne':wgClientPPPoEClientDNSOne,'wgClientPPPoEClientDNSTwo':wgClientPPPoEClientDNSTwo,'wgClientPPPoEADSLPeerMACAddr':wgClientPPPoEADSLPeerMACAddr,'wgClientPPPoEClientConnTime':wgClientPPPoEClientConnTime})