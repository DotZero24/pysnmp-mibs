_N='extremeMlagPortLocalPortIfIndex'
_M='extremeMlagAlternatePeerIP'
_L='extremeMlagAlternatePeerAddrType'
_K='down'
_J='TruthValue'
_I='InetAddressType'
_H='read-write'
_G='extremeMlagPeerName'
_F='DisplayString'
_E='EXTREME-MLAG-MIB'
_D='Integer32'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extremeAgent,=mibBuilder.importSymbols('EXTREME-BASE-MIB','extremeAgent')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_I)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp',_J)
extremeMlag=ModuleIdentity((1,3,6,1,4,1,1916,1,41))
if mibBuilder.loadTexts:extremeMlag.setRevisions(('2018-05-17 14:05','2018-04-04 05:00','2017-01-05 00:00','2013-08-08 00:00'))
_ExtremeMlagObjects_ObjectIdentity=ObjectIdentity
extremeMlagObjects=_ExtremeMlagObjects_ObjectIdentity((1,3,6,1,4,1,1916,1,41,1))
_ExtremeMlagPeerTable_Object=MibTable
extremeMlagPeerTable=_ExtremeMlagPeerTable_Object((1,3,6,1,4,1,1916,1,41,1,1))
if mibBuilder.loadTexts:extremeMlagPeerTable.setStatus(_A)
_ExtremeMlagPeerEntry_Object=MibTableRow
extremeMlagPeerEntry=_ExtremeMlagPeerEntry_Object((1,3,6,1,4,1,1916,1,41,1,1,1))
extremeMlagPeerEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:extremeMlagPeerEntry.setStatus(_A)
class _ExtremeMlagPeerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ExtremeMlagPeerName_Type.__name__=_F
_ExtremeMlagPeerName_Object=MibTableColumn
extremeMlagPeerName=_ExtremeMlagPeerName_Object((1,3,6,1,4,1,1916,1,41,1,1,1,1),_ExtremeMlagPeerName_Type())
extremeMlagPeerName.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeMlagPeerName.setStatus(_A)
class _ExtremeMlagPeerVlan_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ExtremeMlagPeerVlan_Type.__name__=_F
_ExtremeMlagPeerVlan_Object=MibTableColumn
extremeMlagPeerVlan=_ExtremeMlagPeerVlan_Object((1,3,6,1,4,1,1916,1,41,1,1,1,2),_ExtremeMlagPeerVlan_Type())
extremeMlagPeerVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMlagPeerVlan.setStatus(_A)
class _ExtremeMlagPeerVR_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ExtremeMlagPeerVR_Type.__name__=_F
_ExtremeMlagPeerVR_Object=MibTableColumn
extremeMlagPeerVR=_ExtremeMlagPeerVR_Object((1,3,6,1,4,1,1916,1,41,1,1,1,3),_ExtremeMlagPeerVR_Type())
extremeMlagPeerVR.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeMlagPeerVR.setStatus(_A)
_ExtremeMlagLocalAddrType_Type=InetAddressType
_ExtremeMlagLocalAddrType_Object=MibTableColumn
extremeMlagLocalAddrType=_ExtremeMlagLocalAddrType_Object((1,3,6,1,4,1,1916,1,41,1,1,1,4),_ExtremeMlagLocalAddrType_Type())
extremeMlagLocalAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeMlagLocalAddrType.setStatus(_A)
_ExtremeMlagLocalIP_Type=InetAddress
_ExtremeMlagLocalIP_Object=MibTableColumn
extremeMlagLocalIP=_ExtremeMlagLocalIP_Object((1,3,6,1,4,1,1916,1,41,1,1,1,5),_ExtremeMlagLocalIP_Type())
extremeMlagLocalIP.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeMlagLocalIP.setStatus(_A)
class _ExtremeMlagPeerAddrType_Type(InetAddressType):defaultValue=1
_ExtremeMlagPeerAddrType_Type.__name__=_I
_ExtremeMlagPeerAddrType_Object=MibTableColumn
extremeMlagPeerAddrType=_ExtremeMlagPeerAddrType_Object((1,3,6,1,4,1,1916,1,41,1,1,1,6),_ExtremeMlagPeerAddrType_Type())
extremeMlagPeerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeMlagPeerAddrType.setStatus(_A)
_ExtremeMlagPeerIP_Type=InetAddress
_ExtremeMlagPeerIP_Object=MibTableColumn
extremeMlagPeerIP=_ExtremeMlagPeerIP_Object((1,3,6,1,4,1,1916,1,41,1,1,1,7),_ExtremeMlagPeerIP_Type())
extremeMlagPeerIP.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeMlagPeerIP.setStatus(_A)
_ExtremeMlagPeerPortCount_Type=Integer32
_ExtremeMlagPeerPortCount_Object=MibTableColumn
extremeMlagPeerPortCount=_ExtremeMlagPeerPortCount_Object((1,3,6,1,4,1,1916,1,41,1,1,1,8),_ExtremeMlagPeerPortCount_Type())
extremeMlagPeerPortCount.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMlagPeerPortCount.setStatus(_A)
class _ExtremeMlagPeerCheckPointStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_K,2)))
_ExtremeMlagPeerCheckPointStatus_Type.__name__=_D
_ExtremeMlagPeerCheckPointStatus_Object=MibTableColumn
extremeMlagPeerCheckPointStatus=_ExtremeMlagPeerCheckPointStatus_Object((1,3,6,1,4,1,1916,1,41,1,1,1,9),_ExtremeMlagPeerCheckPointStatus_Type())
extremeMlagPeerCheckPointStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMlagPeerCheckPointStatus.setStatus(_A)
_ExtremeMlagPeerRxHellos_Type=Counter32
_ExtremeMlagPeerRxHellos_Object=MibTableColumn
extremeMlagPeerRxHellos=_ExtremeMlagPeerRxHellos_Object((1,3,6,1,4,1,1916,1,41,1,1,1,10),_ExtremeMlagPeerRxHellos_Type())
extremeMlagPeerRxHellos.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMlagPeerRxHellos.setStatus(_A)
_ExtremeMlagPeerRxCheckpointMsgs_Type=Counter32
_ExtremeMlagPeerRxCheckpointMsgs_Object=MibTableColumn
extremeMlagPeerRxCheckpointMsgs=_ExtremeMlagPeerRxCheckpointMsgs_Object((1,3,6,1,4,1,1916,1,41,1,1,1,11),_ExtremeMlagPeerRxCheckpointMsgs_Type())
extremeMlagPeerRxCheckpointMsgs.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMlagPeerRxCheckpointMsgs.setStatus(_A)
_ExtremeMlagPeerHelloErrors_Type=Counter32
_ExtremeMlagPeerHelloErrors_Object=MibTableColumn
extremeMlagPeerHelloErrors=_ExtremeMlagPeerHelloErrors_Object((1,3,6,1,4,1,1916,1,41,1,1,1,12),_ExtremeMlagPeerHelloErrors_Type())
extremeMlagPeerHelloErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMlagPeerHelloErrors.setStatus(_A)
_ExtremeMlagPeerHelloTimeouts_Type=Counter32
_ExtremeMlagPeerHelloTimeouts_Object=MibTableColumn
extremeMlagPeerHelloTimeouts=_ExtremeMlagPeerHelloTimeouts_Object((1,3,6,1,4,1,1916,1,41,1,1,1,13),_ExtremeMlagPeerHelloTimeouts_Type())
extremeMlagPeerHelloTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMlagPeerHelloTimeouts.setStatus(_A)
_ExtremeMlagPeerUptime_Type=TimeStamp
_ExtremeMlagPeerUptime_Object=MibTableColumn
extremeMlagPeerUptime=_ExtremeMlagPeerUptime_Object((1,3,6,1,4,1,1916,1,41,1,1,1,14),_ExtremeMlagPeerUptime_Type())
extremeMlagPeerUptime.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMlagPeerUptime.setStatus(_A)
class _ExtremeMlagPeerLocalTxInterval_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,10000))
_ExtremeMlagPeerLocalTxInterval_Type.__name__=_D
_ExtremeMlagPeerLocalTxInterval_Object=MibTableColumn
extremeMlagPeerLocalTxInterval=_ExtremeMlagPeerLocalTxInterval_Object((1,3,6,1,4,1,1916,1,41,1,1,1,15),_ExtremeMlagPeerLocalTxInterval_Type())
extremeMlagPeerLocalTxInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeMlagPeerLocalTxInterval.setStatus(_A)
class _ExtremeMlagPeerRemoteTxInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,10000))
_ExtremeMlagPeerRemoteTxInterval_Type.__name__=_D
_ExtremeMlagPeerRemoteTxInterval_Object=MibTableColumn
extremeMlagPeerRemoteTxInterval=_ExtremeMlagPeerRemoteTxInterval_Object((1,3,6,1,4,1,1916,1,41,1,1,1,16),_ExtremeMlagPeerRemoteTxInterval_Type())
extremeMlagPeerRemoteTxInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMlagPeerRemoteTxInterval.setStatus(_A)
_ExtremeMlagPeerTxHellos_Type=Counter32
_ExtremeMlagPeerTxHellos_Object=MibTableColumn
extremeMlagPeerTxHellos=_ExtremeMlagPeerTxHellos_Object((1,3,6,1,4,1,1916,1,41,1,1,1,17),_ExtremeMlagPeerTxHellos_Type())
extremeMlagPeerTxHellos.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMlagPeerTxHellos.setStatus(_A)
_ExtremeMlagPeerTxCheckpoints_Type=Counter32
_ExtremeMlagPeerTxCheckpoints_Object=MibTableColumn
extremeMlagPeerTxCheckpoints=_ExtremeMlagPeerTxCheckpoints_Object((1,3,6,1,4,1,1916,1,41,1,1,1,18),_ExtremeMlagPeerTxCheckpoints_Type())
extremeMlagPeerTxCheckpoints.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMlagPeerTxCheckpoints.setStatus(_A)
_ExtremeMlagPeerCheckpointErrors_Type=Counter32
_ExtremeMlagPeerCheckpointErrors_Object=MibTableColumn
extremeMlagPeerCheckpointErrors=_ExtremeMlagPeerCheckpointErrors_Object((1,3,6,1,4,1,1916,1,41,1,1,1,19),_ExtremeMlagPeerCheckpointErrors_Type())
extremeMlagPeerCheckpointErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMlagPeerCheckpointErrors.setStatus(_A)
_ExtremeMlagPeerConnnectErrors_Type=Counter32
_ExtremeMlagPeerConnnectErrors_Object=MibTableColumn
extremeMlagPeerConnnectErrors=_ExtremeMlagPeerConnnectErrors_Object((1,3,6,1,4,1,1916,1,41,1,1,1,20),_ExtremeMlagPeerConnnectErrors_Type())
extremeMlagPeerConnnectErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMlagPeerConnnectErrors.setStatus(_A)
_ExtremeMlagPeerRowStatus_Type=RowStatus
_ExtremeMlagPeerRowStatus_Object=MibTableColumn
extremeMlagPeerRowStatus=_ExtremeMlagPeerRowStatus_Object((1,3,6,1,4,1,1916,1,41,1,1,1,21),_ExtremeMlagPeerRowStatus_Type())
extremeMlagPeerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeMlagPeerRowStatus.setStatus(_A)
_ExtremeMlagPeerCfgLacpMac_Type=MacAddress
_ExtremeMlagPeerCfgLacpMac_Object=MibTableColumn
extremeMlagPeerCfgLacpMac=_ExtremeMlagPeerCfgLacpMac_Object((1,3,6,1,4,1,1916,1,41,1,1,1,22),_ExtremeMlagPeerCfgLacpMac_Type())
extremeMlagPeerCfgLacpMac.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeMlagPeerCfgLacpMac.setStatus(_A)
_ExtremeMlagPeerOperLacpMac_Type=MacAddress
_ExtremeMlagPeerOperLacpMac_Object=MibTableColumn
extremeMlagPeerOperLacpMac=_ExtremeMlagPeerOperLacpMac_Object((1,3,6,1,4,1,1916,1,41,1,1,1,23),_ExtremeMlagPeerOperLacpMac_Type())
extremeMlagPeerOperLacpMac.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMlagPeerOperLacpMac.setStatus(_A)
class _ExtremeMlagPeerAlternateVlan_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ExtremeMlagPeerAlternateVlan_Type.__name__=_F
_ExtremeMlagPeerAlternateVlan_Object=MibTableColumn
extremeMlagPeerAlternateVlan=_ExtremeMlagPeerAlternateVlan_Object((1,3,6,1,4,1,1916,1,41,1,1,1,24),_ExtremeMlagPeerAlternateVlan_Type())
extremeMlagPeerAlternateVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMlagPeerAlternateVlan.setStatus(_A)
class _ExtremeMlagPeerAlternateVR_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ExtremeMlagPeerAlternateVR_Type.__name__=_F
_ExtremeMlagPeerAlternateVR_Object=MibTableColumn
extremeMlagPeerAlternateVR=_ExtremeMlagPeerAlternateVR_Object((1,3,6,1,4,1,1916,1,41,1,1,1,25),_ExtremeMlagPeerAlternateVR_Type())
extremeMlagPeerAlternateVR.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeMlagPeerAlternateVR.setStatus(_A)
_ExtremeMlagAlternateLocalAddrType_Type=InetAddressType
_ExtremeMlagAlternateLocalAddrType_Object=MibTableColumn
extremeMlagAlternateLocalAddrType=_ExtremeMlagAlternateLocalAddrType_Object((1,3,6,1,4,1,1916,1,41,1,1,1,26),_ExtremeMlagAlternateLocalAddrType_Type())
extremeMlagAlternateLocalAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeMlagAlternateLocalAddrType.setStatus(_A)
_ExtremeMlagAlternateLocalIP_Type=InetAddress
_ExtremeMlagAlternateLocalIP_Object=MibTableColumn
extremeMlagAlternateLocalIP=_ExtremeMlagAlternateLocalIP_Object((1,3,6,1,4,1,1916,1,41,1,1,1,27),_ExtremeMlagAlternateLocalIP_Type())
extremeMlagAlternateLocalIP.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeMlagAlternateLocalIP.setStatus(_A)
class _ExtremeMlagAlternatePeerAddrType_Type(InetAddressType):defaultValue=1
_ExtremeMlagAlternatePeerAddrType_Type.__name__=_I
_ExtremeMlagAlternatePeerAddrType_Object=MibTableColumn
extremeMlagAlternatePeerAddrType=_ExtremeMlagAlternatePeerAddrType_Object((1,3,6,1,4,1,1916,1,41,1,1,1,28),_ExtremeMlagAlternatePeerAddrType_Type())
extremeMlagAlternatePeerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeMlagAlternatePeerAddrType.setStatus(_A)
_ExtremeMlagAlternatePeerIP_Type=InetAddress
_ExtremeMlagAlternatePeerIP_Object=MibTableColumn
extremeMlagAlternatePeerIP=_ExtremeMlagAlternatePeerIP_Object((1,3,6,1,4,1,1916,1,41,1,1,1,29),_ExtremeMlagAlternatePeerIP_Type())
extremeMlagAlternatePeerIP.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeMlagAlternatePeerIP.setStatus(_A)
_ExtremeMlagPeerAlternateRxHellos_Type=Counter32
_ExtremeMlagPeerAlternateRxHellos_Object=MibTableColumn
extremeMlagPeerAlternateRxHellos=_ExtremeMlagPeerAlternateRxHellos_Object((1,3,6,1,4,1,1916,1,41,1,1,1,30),_ExtremeMlagPeerAlternateRxHellos_Type())
extremeMlagPeerAlternateRxHellos.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMlagPeerAlternateRxHellos.setStatus(_A)
_ExtremeMlagPeerAlternateHelloErrors_Type=Counter32
_ExtremeMlagPeerAlternateHelloErrors_Object=MibTableColumn
extremeMlagPeerAlternateHelloErrors=_ExtremeMlagPeerAlternateHelloErrors_Object((1,3,6,1,4,1,1916,1,41,1,1,1,31),_ExtremeMlagPeerAlternateHelloErrors_Type())
extremeMlagPeerAlternateHelloErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMlagPeerAlternateHelloErrors.setStatus(_A)
_ExtremeMlagPeerAlternateHelloTimeouts_Type=Counter32
_ExtremeMlagPeerAlternateHelloTimeouts_Object=MibTableColumn
extremeMlagPeerAlternateHelloTimeouts=_ExtremeMlagPeerAlternateHelloTimeouts_Object((1,3,6,1,4,1,1916,1,41,1,1,1,32),_ExtremeMlagPeerAlternateHelloTimeouts_Type())
extremeMlagPeerAlternateHelloTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMlagPeerAlternateHelloTimeouts.setStatus(_A)
_ExtremeMlagPeerAlternateTxHellos_Type=Counter32
_ExtremeMlagPeerAlternateTxHellos_Object=MibTableColumn
extremeMlagPeerAlternateTxHellos=_ExtremeMlagPeerAlternateTxHellos_Object((1,3,6,1,4,1,1916,1,41,1,1,1,33),_ExtremeMlagPeerAlternateTxHellos_Type())
extremeMlagPeerAlternateTxHellos.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMlagPeerAlternateTxHellos.setStatus(_A)
class _ExtremeMlagPeerCheckPointAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('none',1),('md5',2)))
_ExtremeMlagPeerCheckPointAuthType_Type.__name__=_D
_ExtremeMlagPeerCheckPointAuthType_Object=MibTableColumn
extremeMlagPeerCheckPointAuthType=_ExtremeMlagPeerCheckPointAuthType_Object((1,3,6,1,4,1,1916,1,41,1,1,1,34),_ExtremeMlagPeerCheckPointAuthType_Type())
extremeMlagPeerCheckPointAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeMlagPeerCheckPointAuthType.setStatus(_A)
class _ExtremeMlagPeerCheckpointAuthKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,32))
_ExtremeMlagPeerCheckpointAuthKey_Type.__name__=_F
_ExtremeMlagPeerCheckpointAuthKey_Object=MibTableColumn
extremeMlagPeerCheckpointAuthKey=_ExtremeMlagPeerCheckpointAuthKey_Object((1,3,6,1,4,1,1916,1,41,1,1,1,35),_ExtremeMlagPeerCheckpointAuthKey_Type())
extremeMlagPeerCheckpointAuthKey.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeMlagPeerCheckpointAuthKey.setStatus(_A)
_ExtremeMlagPortTable_Object=MibTable
extremeMlagPortTable=_ExtremeMlagPortTable_Object((1,3,6,1,4,1,1916,1,41,1,2))
if mibBuilder.loadTexts:extremeMlagPortTable.setStatus(_A)
_ExtremeMlagPortEntry_Object=MibTableRow
extremeMlagPortEntry=_ExtremeMlagPortEntry_Object((1,3,6,1,4,1,1916,1,41,1,2,1))
extremeMlagPortEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:extremeMlagPortEntry.setStatus(_A)
_ExtremeMlagPortLocalPortIfIndex_Type=Unsigned32
_ExtremeMlagPortLocalPortIfIndex_Object=MibTableColumn
extremeMlagPortLocalPortIfIndex=_ExtremeMlagPortLocalPortIfIndex_Object((1,3,6,1,4,1,1916,1,41,1,2,1,1),_ExtremeMlagPortLocalPortIfIndex_Type())
extremeMlagPortLocalPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeMlagPortLocalPortIfIndex.setStatus(_A)
class _ExtremeMlagPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65000))
_ExtremeMlagPortId_Type.__name__=_D
_ExtremeMlagPortId_Object=MibTableColumn
extremeMlagPortId=_ExtremeMlagPortId_Object((1,3,6,1,4,1,1916,1,41,1,2,1,2),_ExtremeMlagPortId_Type())
extremeMlagPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeMlagPortId.setStatus(_A)
_ExtremeMlagPortPeer_Type=DisplayString
_ExtremeMlagPortPeer_Object=MibTableColumn
extremeMlagPortPeer=_ExtremeMlagPortPeer_Object((1,3,6,1,4,1,1916,1,41,1,2,1,3),_ExtremeMlagPortPeer_Type())
extremeMlagPortPeer.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeMlagPortPeer.setStatus(_A)
class _ExtremeMlagPortLocalLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('active',1),('disabled',2),('ready',3),('portNotPresent',4)))
_ExtremeMlagPortLocalLinkStatus_Type.__name__=_D
_ExtremeMlagPortLocalLinkStatus_Object=MibTableColumn
extremeMlagPortLocalLinkStatus=_ExtremeMlagPortLocalLinkStatus_Object((1,3,6,1,4,1,1916,1,41,1,2,1,4),_ExtremeMlagPortLocalLinkStatus_Type())
extremeMlagPortLocalLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMlagPortLocalLinkStatus.setStatus(_A)
class _ExtremeMlagPortRemoteLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),(_K,2),('notAvailable',3)))
_ExtremeMlagPortRemoteLinkStatus_Type.__name__=_D
_ExtremeMlagPortRemoteLinkStatus_Object=MibTableColumn
extremeMlagPortRemoteLinkStatus=_ExtremeMlagPortRemoteLinkStatus_Object((1,3,6,1,4,1,1916,1,41,1,2,1,5),_ExtremeMlagPortRemoteLinkStatus_Type())
extremeMlagPortRemoteLinkStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMlagPortRemoteLinkStatus.setStatus(_A)
class _ExtremeMlagPortPeerState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),(_K,2)))
_ExtremeMlagPortPeerState_Type.__name__=_D
_ExtremeMlagPortPeerState_Object=MibTableColumn
extremeMlagPortPeerState=_ExtremeMlagPortPeerState_Object((1,3,6,1,4,1,1916,1,41,1,2,1,6),_ExtremeMlagPortPeerState_Type())
extremeMlagPortPeerState.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMlagPortPeerState.setStatus(_A)
_ExtremeMlagPortLocalFailures_Type=Counter32
_ExtremeMlagPortLocalFailures_Object=MibTableColumn
extremeMlagPortLocalFailures=_ExtremeMlagPortLocalFailures_Object((1,3,6,1,4,1,1916,1,41,1,2,1,7),_ExtremeMlagPortLocalFailures_Type())
extremeMlagPortLocalFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMlagPortLocalFailures.setStatus(_A)
_ExtremeMlagPortRemoteFailures_Type=Counter32
_ExtremeMlagPortRemoteFailures_Object=MibTableColumn
extremeMlagPortRemoteFailures=_ExtremeMlagPortRemoteFailures_Object((1,3,6,1,4,1,1916,1,41,1,2,1,8),_ExtremeMlagPortRemoteFailures_Type())
extremeMlagPortRemoteFailures.setMaxAccess(_B)
if mibBuilder.loadTexts:extremeMlagPortRemoteFailures.setStatus(_A)
_ExtremeMlagPortRowStatus_Type=RowStatus
_ExtremeMlagPortRowStatus_Object=MibTableColumn
extremeMlagPortRowStatus=_ExtremeMlagPortRowStatus_Object((1,3,6,1,4,1,1916,1,41,1,2,1,9),_ExtremeMlagPortRowStatus_Type())
extremeMlagPortRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:extremeMlagPortRowStatus.setStatus(_A)
class _ExtremeMlagConvergenceControl_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('fastConvergence',1),('conserveAccessLists',2)))
_ExtremeMlagConvergenceControl_Type.__name__=_D
_ExtremeMlagConvergenceControl_Object=MibScalar
extremeMlagConvergenceControl=_ExtremeMlagConvergenceControl_Object((1,3,6,1,4,1,1916,1,41,1,3),_ExtremeMlagConvergenceControl_Type())
extremeMlagConvergenceControl.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeMlagConvergenceControl.setStatus(_A)
class _ExtremeMlagReloadDelayInterval_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1200))
_ExtremeMlagReloadDelayInterval_Type.__name__=_D
_ExtremeMlagReloadDelayInterval_Object=MibScalar
extremeMlagReloadDelayInterval=_ExtremeMlagReloadDelayInterval_Object((1,3,6,1,4,1,1916,1,41,1,4),_ExtremeMlagReloadDelayInterval_Type())
extremeMlagReloadDelayInterval.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeMlagReloadDelayInterval.setStatus(_A)
class _ExtremeMlagReloadDelayEnable_Type(TruthValue):defaultValue=2
_ExtremeMlagReloadDelayEnable_Type.__name__=_J
_ExtremeMlagReloadDelayEnable_Object=MibScalar
extremeMlagReloadDelayEnable=_ExtremeMlagReloadDelayEnable_Object((1,3,6,1,4,1,1916,1,41,1,5),_ExtremeMlagReloadDelayEnable_Type())
extremeMlagReloadDelayEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeMlagReloadDelayEnable.setStatus(_A)
class _ExtremeMlagLinkupIsolationEnable_Type(TruthValue):defaultValue=2
_ExtremeMlagLinkupIsolationEnable_Type.__name__=_J
_ExtremeMlagLinkupIsolationEnable_Object=MibScalar
extremeMlagLinkupIsolationEnable=_ExtremeMlagLinkupIsolationEnable_Object((1,3,6,1,4,1,1916,1,41,1,6),_ExtremeMlagLinkupIsolationEnable_Type())
extremeMlagLinkupIsolationEnable.setMaxAccess(_H)
if mibBuilder.loadTexts:extremeMlagLinkupIsolationEnable.setStatus(_A)
_ExtremeMlagNotificationObjects_ObjectIdentity=ObjectIdentity
extremeMlagNotificationObjects=_ExtremeMlagNotificationObjects_ObjectIdentity((1,3,6,1,4,1,1916,1,41,2))
_ExtremeMlagNotifications_ObjectIdentity=ObjectIdentity
extremeMlagNotifications=_ExtremeMlagNotifications_ObjectIdentity((1,3,6,1,4,1,1916,1,41,3))
_ExtremeMlagNotificationsPrefix_ObjectIdentity=ObjectIdentity
extremeMlagNotificationsPrefix=_ExtremeMlagNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,1916,1,41,3,0))
extremeMlagPeerUp=NotificationType((1,3,6,1,4,1,1916,1,41,3,0,1))
extremeMlagPeerUp.setObjects((_E,_G))
if mibBuilder.loadTexts:extremeMlagPeerUp.setStatus(_A)
extremeMlagPeerDown=NotificationType((1,3,6,1,4,1,1916,1,41,3,0,2))
extremeMlagPeerDown.setObjects((_E,_G))
if mibBuilder.loadTexts:extremeMlagPeerDown.setStatus(_A)
extremeMlagAltPathUp=NotificationType((1,3,6,1,4,1,1916,1,41,3,0,3))
extremeMlagAltPathUp.setObjects(*((_E,_L),(_E,_M)))
if mibBuilder.loadTexts:extremeMlagAltPathUp.setStatus(_A)
extremeMlagAltPathDown=NotificationType((1,3,6,1,4,1,1916,1,41,3,0,4))
extremeMlagAltPathDown.setObjects(*((_E,_L),(_E,_M)))
if mibBuilder.loadTexts:extremeMlagAltPathDown.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'extremeMlag':extremeMlag,'extremeMlagObjects':extremeMlagObjects,'extremeMlagPeerTable':extremeMlagPeerTable,'extremeMlagPeerEntry':extremeMlagPeerEntry,_G:extremeMlagPeerName,'extremeMlagPeerVlan':extremeMlagPeerVlan,'extremeMlagPeerVR':extremeMlagPeerVR,'extremeMlagLocalAddrType':extremeMlagLocalAddrType,'extremeMlagLocalIP':extremeMlagLocalIP,'extremeMlagPeerAddrType':extremeMlagPeerAddrType,'extremeMlagPeerIP':extremeMlagPeerIP,'extremeMlagPeerPortCount':extremeMlagPeerPortCount,'extremeMlagPeerCheckPointStatus':extremeMlagPeerCheckPointStatus,'extremeMlagPeerRxHellos':extremeMlagPeerRxHellos,'extremeMlagPeerRxCheckpointMsgs':extremeMlagPeerRxCheckpointMsgs,'extremeMlagPeerHelloErrors':extremeMlagPeerHelloErrors,'extremeMlagPeerHelloTimeouts':extremeMlagPeerHelloTimeouts,'extremeMlagPeerUptime':extremeMlagPeerUptime,'extremeMlagPeerLocalTxInterval':extremeMlagPeerLocalTxInterval,'extremeMlagPeerRemoteTxInterval':extremeMlagPeerRemoteTxInterval,'extremeMlagPeerTxHellos':extremeMlagPeerTxHellos,'extremeMlagPeerTxCheckpoints':extremeMlagPeerTxCheckpoints,'extremeMlagPeerCheckpointErrors':extremeMlagPeerCheckpointErrors,'extremeMlagPeerConnnectErrors':extremeMlagPeerConnnectErrors,'extremeMlagPeerRowStatus':extremeMlagPeerRowStatus,'extremeMlagPeerCfgLacpMac':extremeMlagPeerCfgLacpMac,'extremeMlagPeerOperLacpMac':extremeMlagPeerOperLacpMac,'extremeMlagPeerAlternateVlan':extremeMlagPeerAlternateVlan,'extremeMlagPeerAlternateVR':extremeMlagPeerAlternateVR,'extremeMlagAlternateLocalAddrType':extremeMlagAlternateLocalAddrType,'extremeMlagAlternateLocalIP':extremeMlagAlternateLocalIP,_L:extremeMlagAlternatePeerAddrType,_M:extremeMlagAlternatePeerIP,'extremeMlagPeerAlternateRxHellos':extremeMlagPeerAlternateRxHellos,'extremeMlagPeerAlternateHelloErrors':extremeMlagPeerAlternateHelloErrors,'extremeMlagPeerAlternateHelloTimeouts':extremeMlagPeerAlternateHelloTimeouts,'extremeMlagPeerAlternateTxHellos':extremeMlagPeerAlternateTxHellos,'extremeMlagPeerCheckPointAuthType':extremeMlagPeerCheckPointAuthType,'extremeMlagPeerCheckpointAuthKey':extremeMlagPeerCheckpointAuthKey,'extremeMlagPortTable':extremeMlagPortTable,'extremeMlagPortEntry':extremeMlagPortEntry,_N:extremeMlagPortLocalPortIfIndex,'extremeMlagPortId':extremeMlagPortId,'extremeMlagPortPeer':extremeMlagPortPeer,'extremeMlagPortLocalLinkStatus':extremeMlagPortLocalLinkStatus,'extremeMlagPortRemoteLinkStatus':extremeMlagPortRemoteLinkStatus,'extremeMlagPortPeerState':extremeMlagPortPeerState,'extremeMlagPortLocalFailures':extremeMlagPortLocalFailures,'extremeMlagPortRemoteFailures':extremeMlagPortRemoteFailures,'extremeMlagPortRowStatus':extremeMlagPortRowStatus,'extremeMlagConvergenceControl':extremeMlagConvergenceControl,'extremeMlagReloadDelayInterval':extremeMlagReloadDelayInterval,'extremeMlagReloadDelayEnable':extremeMlagReloadDelayEnable,'extremeMlagLinkupIsolationEnable':extremeMlagLinkupIsolationEnable,'extremeMlagNotificationObjects':extremeMlagNotificationObjects,'extremeMlagNotifications':extremeMlagNotifications,'extremeMlagNotificationsPrefix':extremeMlagNotificationsPrefix,'extremeMlagPeerUp':extremeMlagPeerUp,'extremeMlagPeerDown':extremeMlagPeerDown,'extremeMlagAltPathUp':extremeMlagAltPathUp,'extremeMlagAltPathDown':extremeMlagAltPathDown})