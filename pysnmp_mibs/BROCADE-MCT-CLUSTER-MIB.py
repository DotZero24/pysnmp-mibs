_X='brcdMctClusterClientOperStatus'
_W='brcdMctClusterPeerDownReason'
_V='brcdMctClusterPeerOperStatus'
_U='brcdMctClusterClientName'
_T='noState'
_S='brcdMctClusterPeerAddr'
_R='brcdMctClusterPeerAddrType'
_Q='brcdMctClusterIclName'
_P='rBridgeIdNotConfigured'
_O='BrcdDeployStatus'
_N='TruthValue'
_M='EnabledStatus'
_L='BrcdVlanIdOrNoneTC'
_K='none'
_J='unknown'
_I='not-accessible'
_H='brcdMctClusterId'
_G='DisplayString'
_F='Unsigned32'
_E='Integer32'
_D='read-only'
_C='BROCADE-MCT-CLUSTER-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
brcdMct,=mibBuilder.importSymbols('FOUNDRY-SN-ROOT-MIB','brcdMct')
BrcdVlanIdOrNoneTC,BrcdVlanIdTC=mibBuilder.importSymbols('FOUNDRY-SN-SWITCH-GROUP-MIB',_L,'BrcdVlanIdTC')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_M)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'PhysAddress','RowStatus','TextualConvention','TimeInterval',_N)
brcdMctMIB=ModuleIdentity((1,3,6,1,4,1,1991,1,1,12,1))
if mibBuilder.loadTexts:brcdMctMIB.setRevisions(('2011-12-20 00:00','2017-08-07 00:00'))
class BrcdDeployStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('deploy',1),('undeploy',2)))
_BrcdMctNotifications_ObjectIdentity=ObjectIdentity
brcdMctNotifications=_BrcdMctNotifications_ObjectIdentity((1,3,6,1,4,1,1991,1,1,12,1,0))
_BrcdMctObjects_ObjectIdentity=ObjectIdentity
brcdMctObjects=_BrcdMctObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,12,1,1))
_BrcdMctL2Forward_Type=EnabledStatus
_BrcdMctL2Forward_Object=MibScalar
brcdMctL2Forward=_BrcdMctL2Forward_Object((1,3,6,1,4,1,1991,1,1,12,1,1,1),_BrcdMctL2Forward_Type())
brcdMctL2Forward.setMaxAccess('read-write')
if mibBuilder.loadTexts:brcdMctL2Forward.setStatus(_A)
_BrcdMctClusterTable_Object=MibTable
brcdMctClusterTable=_BrcdMctClusterTable_Object((1,3,6,1,4,1,1991,1,1,12,1,1,2))
if mibBuilder.loadTexts:brcdMctClusterTable.setStatus(_A)
_BrcdMctClusterEntry_Object=MibTableRow
brcdMctClusterEntry=_BrcdMctClusterEntry_Object((1,3,6,1,4,1,1991,1,1,12,1,1,2,1))
brcdMctClusterEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:brcdMctClusterEntry.setStatus(_A)
class _BrcdMctClusterId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BrcdMctClusterId_Type.__name__=_F
_BrcdMctClusterId_Object=MibTableColumn
brcdMctClusterId=_BrcdMctClusterId_Object((1,3,6,1,4,1,1991,1,1,12,1,1,2,1,1),_BrcdMctClusterId_Type())
brcdMctClusterId.setMaxAccess(_I)
if mibBuilder.loadTexts:brcdMctClusterId.setStatus(_A)
class _BrcdMctClusterName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_BrcdMctClusterName_Type.__name__=_G
_BrcdMctClusterName_Object=MibTableColumn
brcdMctClusterName=_BrcdMctClusterName_Object((1,3,6,1,4,1,1991,1,1,12,1,1,2,1,2),_BrcdMctClusterName_Type())
brcdMctClusterName.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdMctClusterName.setStatus(_A)
class _BrcdMctClusterRbridgeId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,35535))
_BrcdMctClusterRbridgeId_Type.__name__=_F
_BrcdMctClusterRbridgeId_Object=MibTableColumn
brcdMctClusterRbridgeId=_BrcdMctClusterRbridgeId_Object((1,3,6,1,4,1,1991,1,1,12,1,1,2,1,3),_BrcdMctClusterRbridgeId_Type())
brcdMctClusterRbridgeId.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdMctClusterRbridgeId.setStatus(_A)
_BrcdMctClusterSessionVlan_Type=BrcdVlanIdTC
_BrcdMctClusterSessionVlan_Object=MibTableColumn
brcdMctClusterSessionVlan=_BrcdMctClusterSessionVlan_Object((1,3,6,1,4,1,1991,1,1,12,1,1,2,1,4),_BrcdMctClusterSessionVlan_Type())
brcdMctClusterSessionVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdMctClusterSessionVlan.setStatus(_A)
class _BrcdMctClusterKeepAliveVlan_Type(BrcdVlanIdOrNoneTC):defaultValue=0
_BrcdMctClusterKeepAliveVlan_Type.__name__=_L
_BrcdMctClusterKeepAliveVlan_Object=MibTableColumn
brcdMctClusterKeepAliveVlan=_BrcdMctClusterKeepAliveVlan_Object((1,3,6,1,4,1,1991,1,1,12,1,1,2,1,5),_BrcdMctClusterKeepAliveVlan_Type())
brcdMctClusterKeepAliveVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdMctClusterKeepAliveVlan.setStatus(_A)
class _BrcdMctClusterClientIsolationMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('loose',1),('strict',2)))
_BrcdMctClusterClientIsolationMode_Type.__name__=_E
_BrcdMctClusterClientIsolationMode_Object=MibTableColumn
brcdMctClusterClientIsolationMode=_BrcdMctClusterClientIsolationMode_Object((1,3,6,1,4,1,1991,1,1,12,1,1,2,1,6),_BrcdMctClusterClientIsolationMode_Type())
brcdMctClusterClientIsolationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdMctClusterClientIsolationMode.setStatus(_A)
class _BrcdMctClusterClientShutdown_Type(TruthValue):defaultValue=2
_BrcdMctClusterClientShutdown_Type.__name__=_N
_BrcdMctClusterClientShutdown_Object=MibTableColumn
brcdMctClusterClientShutdown=_BrcdMctClusterClientShutdown_Object((1,3,6,1,4,1,1991,1,1,12,1,1,2,1,7),_BrcdMctClusterClientShutdown_Type())
brcdMctClusterClientShutdown.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdMctClusterClientShutdown.setStatus(_A)
_BrcdMctClusterMemberVlans_Type=DisplayString
_BrcdMctClusterMemberVlans_Object=MibTableColumn
brcdMctClusterMemberVlans=_BrcdMctClusterMemberVlans_Object((1,3,6,1,4,1,1991,1,1,12,1,1,2,1,8),_BrcdMctClusterMemberVlans_Type())
brcdMctClusterMemberVlans.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdMctClusterMemberVlans.setStatus(_A)
_BrcdMctClusterActiveMemberVlans_Type=DisplayString
_BrcdMctClusterActiveMemberVlans_Object=MibTableColumn
brcdMctClusterActiveMemberVlans=_BrcdMctClusterActiveMemberVlans_Object((1,3,6,1,4,1,1991,1,1,12,1,1,2,1,9),_BrcdMctClusterActiveMemberVlans_Type())
brcdMctClusterActiveMemberVlans.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdMctClusterActiveMemberVlans.setStatus(_A)
class _BrcdMctClusterDeploy_Type(BrcdDeployStatus):defaultValue=2
_BrcdMctClusterDeploy_Type.__name__=_O
_BrcdMctClusterDeploy_Object=MibTableColumn
brcdMctClusterDeploy=_BrcdMctClusterDeploy_Object((1,3,6,1,4,1,1991,1,1,12,1,1,2,1,10),_BrcdMctClusterDeploy_Type())
brcdMctClusterDeploy.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdMctClusterDeploy.setStatus(_A)
class _BrcdMctClusterDeployFailureReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*((_K,1),(_J,2),(_P,3),('sessionVlanNotConfigured',4),('iclNotConfigured',5),('peerNotConfigured',6),('iclIsMrpSecondaryInterface',7),('iclIsErpRplInterface',8),('iclIsErpMsInterface',9),('iclIsErpFsInterface',10),('iclNotInSessionVlan',11),('iclNotInMemberVlans',12),('nonIclInterfacesInSessionVlan',13),('mgmtVeNotConfiguredInSessionVlan',14),('mgmtIpNotConfiguredInSessionVlan',15),('mgmtIpIsUsedInPeerOrClientConfig',16),('mgmtIpNotInSubnetOfPeerIp',17),('rBridgeIdIsUsedInPeerOrClientConfig',18),('clientInterfaceIsNotInMemberVlan',19),('defaultVlanConfigForSessionOrMemberVlan',20)))
_BrcdMctClusterDeployFailureReason_Type.__name__=_E
_BrcdMctClusterDeployFailureReason_Object=MibTableColumn
brcdMctClusterDeployFailureReason=_BrcdMctClusterDeployFailureReason_Object((1,3,6,1,4,1,1991,1,1,12,1,1,2,1,11),_BrcdMctClusterDeployFailureReason_Type())
brcdMctClusterDeployFailureReason.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdMctClusterDeployFailureReason.setStatus(_A)
_BrcdMctClusterRowStatus_Type=RowStatus
_BrcdMctClusterRowStatus_Object=MibTableColumn
brcdMctClusterRowStatus=_BrcdMctClusterRowStatus_Object((1,3,6,1,4,1,1991,1,1,12,1,1,2,1,12),_BrcdMctClusterRowStatus_Type())
brcdMctClusterRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdMctClusterRowStatus.setStatus(_A)
_BrcdMctClusterIclTable_Object=MibTable
brcdMctClusterIclTable=_BrcdMctClusterIclTable_Object((1,3,6,1,4,1,1991,1,1,12,1,1,3))
if mibBuilder.loadTexts:brcdMctClusterIclTable.setStatus(_A)
_BrcdMctClusterIclEntry_Object=MibTableRow
brcdMctClusterIclEntry=_BrcdMctClusterIclEntry_Object((1,3,6,1,4,1,1991,1,1,12,1,1,3,1))
brcdMctClusterIclEntry.setIndexNames((0,_C,_H),(1,_C,_Q))
if mibBuilder.loadTexts:brcdMctClusterIclEntry.setStatus(_A)
class _BrcdMctClusterIclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_BrcdMctClusterIclName_Type.__name__=_G
_BrcdMctClusterIclName_Object=MibTableColumn
brcdMctClusterIclName=_BrcdMctClusterIclName_Object((1,3,6,1,4,1,1991,1,1,12,1,1,3,1,1),_BrcdMctClusterIclName_Type())
brcdMctClusterIclName.setMaxAccess(_I)
if mibBuilder.loadTexts:brcdMctClusterIclName.setStatus(_A)
_BrcdMctClusterIclIfIndex_Type=InterfaceIndex
_BrcdMctClusterIclIfIndex_Object=MibTableColumn
brcdMctClusterIclIfIndex=_BrcdMctClusterIclIfIndex_Object((1,3,6,1,4,1,1991,1,1,12,1,1,3,1,2),_BrcdMctClusterIclIfIndex_Type())
brcdMctClusterIclIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdMctClusterIclIfIndex.setStatus(_A)
_BrcdMctClusterIclRowStatus_Type=RowStatus
_BrcdMctClusterIclRowStatus_Object=MibTableColumn
brcdMctClusterIclRowStatus=_BrcdMctClusterIclRowStatus_Object((1,3,6,1,4,1,1991,1,1,12,1,1,3,1,3),_BrcdMctClusterIclRowStatus_Type())
brcdMctClusterIclRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdMctClusterIclRowStatus.setStatus(_A)
_BrcdMctClusterPeerTable_Object=MibTable
brcdMctClusterPeerTable=_BrcdMctClusterPeerTable_Object((1,3,6,1,4,1,1991,1,1,12,1,1,4))
if mibBuilder.loadTexts:brcdMctClusterPeerTable.setStatus(_A)
_BrcdMctClusterPeerEntry_Object=MibTableRow
brcdMctClusterPeerEntry=_BrcdMctClusterPeerEntry_Object((1,3,6,1,4,1,1991,1,1,12,1,1,4,1))
brcdMctClusterPeerEntry.setIndexNames((0,_C,_H),(0,_C,_R),(0,_C,_S))
if mibBuilder.loadTexts:brcdMctClusterPeerEntry.setStatus(_A)
_BrcdMctClusterPeerAddrType_Type=InetAddressType
_BrcdMctClusterPeerAddrType_Object=MibTableColumn
brcdMctClusterPeerAddrType=_BrcdMctClusterPeerAddrType_Object((1,3,6,1,4,1,1991,1,1,12,1,1,4,1,1),_BrcdMctClusterPeerAddrType_Type())
brcdMctClusterPeerAddrType.setMaxAccess(_I)
if mibBuilder.loadTexts:brcdMctClusterPeerAddrType.setStatus(_A)
_BrcdMctClusterPeerAddr_Type=InetAddress
_BrcdMctClusterPeerAddr_Object=MibTableColumn
brcdMctClusterPeerAddr=_BrcdMctClusterPeerAddr_Object((1,3,6,1,4,1,1991,1,1,12,1,1,4,1,2),_BrcdMctClusterPeerAddr_Type())
brcdMctClusterPeerAddr.setMaxAccess(_I)
if mibBuilder.loadTexts:brcdMctClusterPeerAddr.setStatus(_A)
class _BrcdMctClusterPeerRbridgeId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,35535))
_BrcdMctClusterPeerRbridgeId_Type.__name__=_F
_BrcdMctClusterPeerRbridgeId_Object=MibTableColumn
brcdMctClusterPeerRbridgeId=_BrcdMctClusterPeerRbridgeId_Object((1,3,6,1,4,1,1991,1,1,12,1,1,4,1,3),_BrcdMctClusterPeerRbridgeId_Type())
brcdMctClusterPeerRbridgeId.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdMctClusterPeerRbridgeId.setStatus(_A)
class _BrcdMctClusterPeerIclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_BrcdMctClusterPeerIclName_Type.__name__=_G
_BrcdMctClusterPeerIclName_Object=MibTableColumn
brcdMctClusterPeerIclName=_BrcdMctClusterPeerIclName_Object((1,3,6,1,4,1,1991,1,1,12,1,1,4,1,4),_BrcdMctClusterPeerIclName_Type())
brcdMctClusterPeerIclName.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdMctClusterPeerIclName.setStatus(_A)
class _BrcdMctClusterPeerFastFailover_Type(EnabledStatus):defaultValue=1
_BrcdMctClusterPeerFastFailover_Type.__name__=_M
_BrcdMctClusterPeerFastFailover_Object=MibTableColumn
brcdMctClusterPeerFastFailover=_BrcdMctClusterPeerFastFailover_Object((1,3,6,1,4,1,1991,1,1,12,1,1,4,1,5),_BrcdMctClusterPeerFastFailover_Type())
brcdMctClusterPeerFastFailover.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdMctClusterPeerFastFailover.setStatus(_A)
_BrcdMctClusterPeerKeepAliveTime_Type=Unsigned32
_BrcdMctClusterPeerKeepAliveTime_Object=MibTableColumn
brcdMctClusterPeerKeepAliveTime=_BrcdMctClusterPeerKeepAliveTime_Object((1,3,6,1,4,1,1991,1,1,12,1,1,4,1,6),_BrcdMctClusterPeerKeepAliveTime_Type())
brcdMctClusterPeerKeepAliveTime.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdMctClusterPeerKeepAliveTime.setStatus(_A)
class _BrcdMctClusterPeerHoldTime_Type(Unsigned32):defaultValue=90;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3,65535))
_BrcdMctClusterPeerHoldTime_Type.__name__=_F
_BrcdMctClusterPeerHoldTime_Object=MibTableColumn
brcdMctClusterPeerHoldTime=_BrcdMctClusterPeerHoldTime_Object((1,3,6,1,4,1,1991,1,1,12,1,1,4,1,7),_BrcdMctClusterPeerHoldTime_Type())
brcdMctClusterPeerHoldTime.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdMctClusterPeerHoldTime.setStatus(_A)
_BrcdMctClusterPeerActiveVlans_Type=DisplayString
_BrcdMctClusterPeerActiveVlans_Object=MibTableColumn
brcdMctClusterPeerActiveVlans=_BrcdMctClusterPeerActiveVlans_Object((1,3,6,1,4,1,1991,1,1,12,1,1,4,1,8),_BrcdMctClusterPeerActiveVlans_Type())
brcdMctClusterPeerActiveVlans.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdMctClusterPeerActiveVlans.setStatus(_A)
class _BrcdMctClusterPeerOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_J,1),(_T,2),('init',3),('ccpUp',4),('ccpDown',5),('reachable',6)))
_BrcdMctClusterPeerOperStatus_Type.__name__=_E
_BrcdMctClusterPeerOperStatus_Object=MibTableColumn
brcdMctClusterPeerOperStatus=_BrcdMctClusterPeerOperStatus_Object((1,3,6,1,4,1,1991,1,1,12,1,1,4,1,9),_BrcdMctClusterPeerOperStatus_Type())
brcdMctClusterPeerOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdMctClusterPeerOperStatus.setStatus(_A)
class _BrcdMctClusterPeerDownReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26)));namedValues=NamedValues(*((_K,1),('loopbackInterfaceDown',2),('iclInterfaceDown',3),('upgradeInProgress',4),('routeNotAvailable',5),('iclVeDown',6),('rBridgeIdMismatch',7),('clusterIdMismatch',8),('keepAliveTimeMismatch',9),('holdTimeMismatch',10),('fastFailoverMismatch',11),('shutdownMesgFromPeer',12),('tcpKeepAliveTimeout',13),('tcpConnCloseMesg',14),('holdTimeoutExpired',15),('sendStateTimeoutExpired',16),('recvStateTimeoutExpired',17),('initMesgSendFail',18),('keepAliveMesgSendFail',19),('invalidAppMesgRecv',20),('badProtocolVersionPktRecv',21),('badPduLengthPktRecv',22),('unknownCcpPktRecv',23),('invalidCcpPktRecv',24),('internalCcpErrorRecv',25),('ccpTcpCommFail',26)))
_BrcdMctClusterPeerDownReason_Type.__name__=_E
_BrcdMctClusterPeerDownReason_Object=MibTableColumn
brcdMctClusterPeerDownReason=_BrcdMctClusterPeerDownReason_Object((1,3,6,1,4,1,1991,1,1,12,1,1,4,1,10),_BrcdMctClusterPeerDownReason_Type())
brcdMctClusterPeerDownReason.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdMctClusterPeerDownReason.setStatus(_A)
_BrcdMctClusterPeerUpTime_Type=TimeInterval
_BrcdMctClusterPeerUpTime_Object=MibTableColumn
brcdMctClusterPeerUpTime=_BrcdMctClusterPeerUpTime_Object((1,3,6,1,4,1,1991,1,1,12,1,1,4,1,11),_BrcdMctClusterPeerUpTime_Type())
brcdMctClusterPeerUpTime.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdMctClusterPeerUpTime.setStatus(_A)
_BrcdMctClusterPeerRowStatus_Type=RowStatus
_BrcdMctClusterPeerRowStatus_Object=MibTableColumn
brcdMctClusterPeerRowStatus=_BrcdMctClusterPeerRowStatus_Object((1,3,6,1,4,1,1991,1,1,12,1,1,4,1,12),_BrcdMctClusterPeerRowStatus_Type())
brcdMctClusterPeerRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdMctClusterPeerRowStatus.setStatus(_A)
_BrcdMctClusterClientTable_Object=MibTable
brcdMctClusterClientTable=_BrcdMctClusterClientTable_Object((1,3,6,1,4,1,1991,1,1,12,1,1,5))
if mibBuilder.loadTexts:brcdMctClusterClientTable.setStatus(_A)
_BrcdMctClusterClientEntry_Object=MibTableRow
brcdMctClusterClientEntry=_BrcdMctClusterClientEntry_Object((1,3,6,1,4,1,1991,1,1,12,1,1,5,1))
brcdMctClusterClientEntry.setIndexNames((0,_C,_H),(1,_C,_U))
if mibBuilder.loadTexts:brcdMctClusterClientEntry.setStatus(_A)
class _BrcdMctClusterClientName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_BrcdMctClusterClientName_Type.__name__=_G
_BrcdMctClusterClientName_Object=MibTableColumn
brcdMctClusterClientName=_BrcdMctClusterClientName_Object((1,3,6,1,4,1,1991,1,1,12,1,1,5,1,1),_BrcdMctClusterClientName_Type())
brcdMctClusterClientName.setMaxAccess(_I)
if mibBuilder.loadTexts:brcdMctClusterClientName.setStatus(_A)
class _BrcdMctClusterClientRbridgeId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,35535))
_BrcdMctClusterClientRbridgeId_Type.__name__=_F
_BrcdMctClusterClientRbridgeId_Object=MibTableColumn
brcdMctClusterClientRbridgeId=_BrcdMctClusterClientRbridgeId_Object((1,3,6,1,4,1,1991,1,1,12,1,1,5,1,2),_BrcdMctClusterClientRbridgeId_Type())
brcdMctClusterClientRbridgeId.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdMctClusterClientRbridgeId.setStatus(_A)
_BrcdMctClusterClientIfIndex_Type=InterfaceIndex
_BrcdMctClusterClientIfIndex_Object=MibTableColumn
brcdMctClusterClientIfIndex=_BrcdMctClusterClientIfIndex_Object((1,3,6,1,4,1,1991,1,1,12,1,1,5,1,3),_BrcdMctClusterClientIfIndex_Type())
brcdMctClusterClientIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdMctClusterClientIfIndex.setStatus(_A)
class _BrcdMctClusterClientOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_J,1),(_T,2),('init',3),('localDeploy',4),('adminUp',5),('remoteUp',6),('localUp',7),('up',8),('slave',9),('master',10),('masterPeerUp',11)))
_BrcdMctClusterClientOperStatus_Type.__name__=_E
_BrcdMctClusterClientOperStatus_Object=MibTableColumn
brcdMctClusterClientOperStatus=_BrcdMctClusterClientOperStatus_Object((1,3,6,1,4,1,1991,1,1,12,1,1,5,1,4),_BrcdMctClusterClientOperStatus_Type())
brcdMctClusterClientOperStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdMctClusterClientOperStatus.setStatus(_A)
_BrcdMctClusterClientDeploy_Type=BrcdDeployStatus
_BrcdMctClusterClientDeploy_Object=MibTableColumn
brcdMctClusterClientDeploy=_BrcdMctClusterClientDeploy_Object((1,3,6,1,4,1,1991,1,1,12,1,1,5,1,5),_BrcdMctClusterClientDeploy_Type())
brcdMctClusterClientDeploy.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdMctClusterClientDeploy.setStatus(_A)
class _BrcdMctClusterClientDeployFailureReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*((_K,1),(_J,2),(_P,3),('clientInterfaceNotConfigured',4),('rBridgeIdUsedInClusterOrPeer',5),('clientInterfacePhysicallyNotUp',6),('clientInterfaceIsMrpRingInterface',7),('clientInterfaceIsErpInterface',8),('iclIsNotInMemberVlan',9)))
_BrcdMctClusterClientDeployFailureReason_Type.__name__=_E
_BrcdMctClusterClientDeployFailureReason_Object=MibTableColumn
brcdMctClusterClientDeployFailureReason=_BrcdMctClusterClientDeployFailureReason_Object((1,3,6,1,4,1,1991,1,1,12,1,1,5,1,6),_BrcdMctClusterClientDeployFailureReason_Type())
brcdMctClusterClientDeployFailureReason.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdMctClusterClientDeployFailureReason.setStatus(_A)
_BrcdMctClusterClientRowStatus_Type=RowStatus
_BrcdMctClusterClientRowStatus_Object=MibTableColumn
brcdMctClusterClientRowStatus=_BrcdMctClusterClientRowStatus_Object((1,3,6,1,4,1,1991,1,1,12,1,1,5,1,7),_BrcdMctClusterClientRowStatus_Type())
brcdMctClusterClientRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdMctClusterClientRowStatus.setStatus(_A)
brcdMctClusterPeerStatus=NotificationType((1,3,6,1,4,1,1991,1,1,12,1,0,1))
brcdMctClusterPeerStatus.setObjects(*((_C,_V),(_C,_W)))
if mibBuilder.loadTexts:brcdMctClusterPeerStatus.setStatus(_A)
brcdMctClusterClientStatus=NotificationType((1,3,6,1,4,1,1991,1,1,12,1,0,2))
brcdMctClusterClientStatus.setObjects((_C,_X))
if mibBuilder.loadTexts:brcdMctClusterClientStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{_O:BrcdDeployStatus,'brcdMctMIB':brcdMctMIB,'brcdMctNotifications':brcdMctNotifications,'brcdMctClusterPeerStatus':brcdMctClusterPeerStatus,'brcdMctClusterClientStatus':brcdMctClusterClientStatus,'brcdMctObjects':brcdMctObjects,'brcdMctL2Forward':brcdMctL2Forward,'brcdMctClusterTable':brcdMctClusterTable,'brcdMctClusterEntry':brcdMctClusterEntry,_H:brcdMctClusterId,'brcdMctClusterName':brcdMctClusterName,'brcdMctClusterRbridgeId':brcdMctClusterRbridgeId,'brcdMctClusterSessionVlan':brcdMctClusterSessionVlan,'brcdMctClusterKeepAliveVlan':brcdMctClusterKeepAliveVlan,'brcdMctClusterClientIsolationMode':brcdMctClusterClientIsolationMode,'brcdMctClusterClientShutdown':brcdMctClusterClientShutdown,'brcdMctClusterMemberVlans':brcdMctClusterMemberVlans,'brcdMctClusterActiveMemberVlans':brcdMctClusterActiveMemberVlans,'brcdMctClusterDeploy':brcdMctClusterDeploy,'brcdMctClusterDeployFailureReason':brcdMctClusterDeployFailureReason,'brcdMctClusterRowStatus':brcdMctClusterRowStatus,'brcdMctClusterIclTable':brcdMctClusterIclTable,'brcdMctClusterIclEntry':brcdMctClusterIclEntry,_Q:brcdMctClusterIclName,'brcdMctClusterIclIfIndex':brcdMctClusterIclIfIndex,'brcdMctClusterIclRowStatus':brcdMctClusterIclRowStatus,'brcdMctClusterPeerTable':brcdMctClusterPeerTable,'brcdMctClusterPeerEntry':brcdMctClusterPeerEntry,_R:brcdMctClusterPeerAddrType,_S:brcdMctClusterPeerAddr,'brcdMctClusterPeerRbridgeId':brcdMctClusterPeerRbridgeId,'brcdMctClusterPeerIclName':brcdMctClusterPeerIclName,'brcdMctClusterPeerFastFailover':brcdMctClusterPeerFastFailover,'brcdMctClusterPeerKeepAliveTime':brcdMctClusterPeerKeepAliveTime,'brcdMctClusterPeerHoldTime':brcdMctClusterPeerHoldTime,'brcdMctClusterPeerActiveVlans':brcdMctClusterPeerActiveVlans,_V:brcdMctClusterPeerOperStatus,_W:brcdMctClusterPeerDownReason,'brcdMctClusterPeerUpTime':brcdMctClusterPeerUpTime,'brcdMctClusterPeerRowStatus':brcdMctClusterPeerRowStatus,'brcdMctClusterClientTable':brcdMctClusterClientTable,'brcdMctClusterClientEntry':brcdMctClusterClientEntry,_U:brcdMctClusterClientName,'brcdMctClusterClientRbridgeId':brcdMctClusterClientRbridgeId,'brcdMctClusterClientIfIndex':brcdMctClusterClientIfIndex,_X:brcdMctClusterClientOperStatus,'brcdMctClusterClientDeploy':brcdMctClusterClientDeploy,'brcdMctClusterClientDeployFailureReason':brcdMctClusterClientDeployFailureReason,'brcdMctClusterClientRowStatus':brcdMctClusterClientRowStatus})