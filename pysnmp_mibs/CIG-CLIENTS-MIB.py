_V='cigDhcpClientsServerIpAddr'
_U='cigDhcpClientsClientId'
_T='cigDhcpClientsHostName'
_S='cigDhcpClientsIPAddress'
_R='cigDhcpClientsIfAlias'
_Q='cigDnsResolverDomainIndex'
_P='cigDnsResolverDnsServerIndex'
_O='cigDnsResolverDnsServerListIndex'
_N='cigDnsResolverDnsServersListIndex'
_M='release'
_L='cigDhcpClientsIfIndex'
_K='TruthValue'
_J='IpAddress'
_I='idle'
_H='OctetString'
_G='Integer32'
_F='DisplayString'
_E='Unsigned32'
_D='CIG-CLIENTS-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,_J,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'enterprises','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'PhysAddress','RowStatus','TextualConvention','TimeInterval',_K)
cigClients=ModuleIdentity((1,3,6,1,4,1,6889,2,1,17))
_Avaya_ObjectIdentity=ObjectIdentity
avaya=_Avaya_ObjectIdentity((1,3,6,1,4,1,6889))
_Mibs_ObjectIdentity=ObjectIdentity
mibs=_Mibs_ObjectIdentity((1,3,6,1,4,1,6889,2))
_Lsg_ObjectIdentity=ObjectIdentity
lsg=_Lsg_ObjectIdentity((1,3,6,1,4,1,6889,2,1))
_CigDhcpClients_ObjectIdentity=ObjectIdentity
cigDhcpClients=_CigDhcpClients_ObjectIdentity((1,3,6,1,4,1,6889,2,1,17,1))
_CigDhcpClientsNotification_ObjectIdentity=ObjectIdentity
cigDhcpClientsNotification=_CigDhcpClientsNotification_ObjectIdentity((1,3,6,1,4,1,6889,2,1,17,1,0))
_CigDhcpClientsTable_Object=MibTable
cigDhcpClientsTable=_CigDhcpClientsTable_Object((1,3,6,1,4,1,6889,2,1,17,1,1))
if mibBuilder.loadTexts:cigDhcpClientsTable.setStatus(_A)
_CigDhcpClientsEntry_Object=MibTableRow
cigDhcpClientsEntry=_CigDhcpClientsEntry_Object((1,3,6,1,4,1,6889,2,1,17,1,1,1))
cigDhcpClientsEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:cigDhcpClientsEntry.setStatus(_A)
_CigDhcpClientsIfIndex_Type=Integer32
_CigDhcpClientsIfIndex_Object=MibTableColumn
cigDhcpClientsIfIndex=_CigDhcpClientsIfIndex_Object((1,3,6,1,4,1,6889,2,1,17,1,1,1,1),_CigDhcpClientsIfIndex_Type())
cigDhcpClientsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpClientsIfIndex.setStatus(_A)
_CigDhcpClientsRowStatus_Type=RowStatus
_CigDhcpClientsRowStatus_Object=MibTableColumn
cigDhcpClientsRowStatus=_CigDhcpClientsRowStatus_Object((1,3,6,1,4,1,6889,2,1,17,1,1,1,2),_CigDhcpClientsRowStatus_Type())
cigDhcpClientsRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDhcpClientsRowStatus.setStatus(_A)
class _CigDhcpClientsIfAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CigDhcpClientsIfAlias_Type.__name__=_F
_CigDhcpClientsIfAlias_Object=MibTableColumn
cigDhcpClientsIfAlias=_CigDhcpClientsIfAlias_Object((1,3,6,1,4,1,6889,2,1,17,1,1,1,3),_CigDhcpClientsIfAlias_Type())
cigDhcpClientsIfAlias.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpClientsIfAlias.setStatus(_A)
class _CigDhcpClientsIPAddress_Type(IpAddress):defaultHexValue='00000000'
_CigDhcpClientsIPAddress_Type.__name__=_J
_CigDhcpClientsIPAddress_Object=MibTableColumn
cigDhcpClientsIPAddress=_CigDhcpClientsIPAddress_Object((1,3,6,1,4,1,6889,2,1,17,1,1,1,4),_CigDhcpClientsIPAddress_Type())
cigDhcpClientsIPAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpClientsIPAddress.setStatus(_A)
_CigDhcpClientsSubnetMask_Type=IpAddress
_CigDhcpClientsSubnetMask_Object=MibTableColumn
cigDhcpClientsSubnetMask=_CigDhcpClientsSubnetMask_Object((1,3,6,1,4,1,6889,2,1,17,1,1,1,5),_CigDhcpClientsSubnetMask_Type())
cigDhcpClientsSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpClientsSubnetMask.setStatus(_A)
class _CigDhcpClientsClientId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CigDhcpClientsClientId_Type.__name__=_H
_CigDhcpClientsClientId_Object=MibTableColumn
cigDhcpClientsClientId=_CigDhcpClientsClientId_Object((1,3,6,1,4,1,6889,2,1,17,1,1,1,6),_CigDhcpClientsClientId_Type())
cigDhcpClientsClientId.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDhcpClientsClientId.setStatus(_A)
class _CigDhcpClientsHostName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_CigDhcpClientsHostName_Type.__name__=_F
_CigDhcpClientsHostName_Object=MibTableColumn
cigDhcpClientsHostName=_CigDhcpClientsHostName_Object((1,3,6,1,4,1,6889,2,1,17,1,1,1,7),_CigDhcpClientsHostName_Type())
cigDhcpClientsHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDhcpClientsHostName.setStatus(_A)
class _CigDhcpClientsRequestLeaseTime_Type(Unsigned32):defaultValue=0
_CigDhcpClientsRequestLeaseTime_Type.__name__=_E
_CigDhcpClientsRequestLeaseTime_Object=MibTableColumn
cigDhcpClientsRequestLeaseTime=_CigDhcpClientsRequestLeaseTime_Object((1,3,6,1,4,1,6889,2,1,17,1,1,1,8),_CigDhcpClientsRequestLeaseTime_Type())
cigDhcpClientsRequestLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDhcpClientsRequestLeaseTime.setStatus(_A)
class _CigDhcpClientsReceiveLeaseTime_Type(Unsigned32):defaultValue=0
_CigDhcpClientsReceiveLeaseTime_Type.__name__=_E
_CigDhcpClientsReceiveLeaseTime_Object=MibTableColumn
cigDhcpClientsReceiveLeaseTime=_CigDhcpClientsReceiveLeaseTime_Object((1,3,6,1,4,1,6889,2,1,17,1,1,1,9),_CigDhcpClientsReceiveLeaseTime_Type())
cigDhcpClientsReceiveLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpClientsReceiveLeaseTime.setStatus(_A)
class _CigDhcpClientsRemainLeaseTime_Type(Unsigned32):defaultValue=0
_CigDhcpClientsRemainLeaseTime_Type.__name__=_E
_CigDhcpClientsRemainLeaseTime_Object=MibTableColumn
cigDhcpClientsRemainLeaseTime=_CigDhcpClientsRemainLeaseTime_Object((1,3,6,1,4,1,6889,2,1,17,1,1,1,10),_CigDhcpClientsRemainLeaseTime_Type())
cigDhcpClientsRemainLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpClientsRemainLeaseTime.setStatus(_A)
class _CigDhcpClientsRenewLeaseTime_Type(Unsigned32):defaultValue=0
_CigDhcpClientsRenewLeaseTime_Type.__name__=_E
_CigDhcpClientsRenewLeaseTime_Object=MibTableColumn
cigDhcpClientsRenewLeaseTime=_CigDhcpClientsRenewLeaseTime_Object((1,3,6,1,4,1,6889,2,1,17,1,1,1,11),_CigDhcpClientsRenewLeaseTime_Type())
cigDhcpClientsRenewLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpClientsRenewLeaseTime.setStatus(_A)
class _CigDhcpClientsRebindLeaseTime_Type(Unsigned32):defaultValue=0
_CigDhcpClientsRebindLeaseTime_Type.__name__=_E
_CigDhcpClientsRebindLeaseTime_Object=MibTableColumn
cigDhcpClientsRebindLeaseTime=_CigDhcpClientsRebindLeaseTime_Object((1,3,6,1,4,1,6889,2,1,17,1,1,1,12),_CigDhcpClientsRebindLeaseTime_Type())
cigDhcpClientsRebindLeaseTime.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpClientsRebindLeaseTime.setStatus(_A)
class _CigDhcpClientsDefaultGatewayList_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CigDhcpClientsDefaultGatewayList_Type.__name__=_F
_CigDhcpClientsDefaultGatewayList_Object=MibTableColumn
cigDhcpClientsDefaultGatewayList=_CigDhcpClientsDefaultGatewayList_Object((1,3,6,1,4,1,6889,2,1,17,1,1,1,13),_CigDhcpClientsDefaultGatewayList_Type())
cigDhcpClientsDefaultGatewayList.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpClientsDefaultGatewayList.setStatus(_A)
class _CigDhcpClientsDnsServerList_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CigDhcpClientsDnsServerList_Type.__name__=_F
_CigDhcpClientsDnsServerList_Object=MibTableColumn
cigDhcpClientsDnsServerList=_CigDhcpClientsDnsServerList_Object((1,3,6,1,4,1,6889,2,1,17,1,1,1,14),_CigDhcpClientsDnsServerList_Type())
cigDhcpClientsDnsServerList.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpClientsDnsServerList.setStatus(_A)
class _CigDhcpClientsDomainName_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CigDhcpClientsDomainName_Type.__name__=_F
_CigDhcpClientsDomainName_Object=MibTableColumn
cigDhcpClientsDomainName=_CigDhcpClientsDomainName_Object((1,3,6,1,4,1,6889,2,1,17,1,1,1,15),_CigDhcpClientsDomainName_Type())
cigDhcpClientsDomainName.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpClientsDomainName.setStatus(_A)
_CigDhcpClientsServerIpAddr_Type=IpAddress
_CigDhcpClientsServerIpAddr_Object=MibTableColumn
cigDhcpClientsServerIpAddr=_CigDhcpClientsServerIpAddr_Object((1,3,6,1,4,1,6889,2,1,17,1,1,1,16),_CigDhcpClientsServerIpAddr_Type())
cigDhcpClientsServerIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpClientsServerIpAddr.setStatus(_A)
class _CigDhcpClientsOperations_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_M,2),('renew',3)))
_CigDhcpClientsOperations_Type.__name__=_G
_CigDhcpClientsOperations_Object=MibTableColumn
cigDhcpClientsOperations=_CigDhcpClientsOperations_Object((1,3,6,1,4,1,6889,2,1,17,1,1,1,17),_CigDhcpClientsOperations_Type())
cigDhcpClientsOperations.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDhcpClientsOperations.setStatus(_A)
class _CigDhcpClientsStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,255)));namedValues=NamedValues(*(('select',1),('request',2),('bound',3),('rebind',4),('renew',5),(_M,6),('decline',7),('reboot',8),(_I,9),('notSupported',255)))
_CigDhcpClientsStatus_Type.__name__=_G
_CigDhcpClientsStatus_Object=MibTableColumn
cigDhcpClientsStatus=_CigDhcpClientsStatus_Object((1,3,6,1,4,1,6889,2,1,17,1,1,1,18),_CigDhcpClientsStatus_Type())
cigDhcpClientsStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDhcpClientsStatus.setStatus(_A)
class _CigDhcpClientsRequestBitmap_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CigDhcpClientsRequestBitmap_Type.__name__=_H
_CigDhcpClientsRequestBitmap_Object=MibTableColumn
cigDhcpClientsRequestBitmap=_CigDhcpClientsRequestBitmap_Object((1,3,6,1,4,1,6889,2,1,17,1,1,1,19),_CigDhcpClientsRequestBitmap_Type())
cigDhcpClientsRequestBitmap.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDhcpClientsRequestBitmap.setStatus(_A)
class _CigDhcpClientsDefaultRouterTrackId_Type(Unsigned32):defaultValue=0
_CigDhcpClientsDefaultRouterTrackId_Type.__name__=_E
_CigDhcpClientsDefaultRouterTrackId_Object=MibTableColumn
cigDhcpClientsDefaultRouterTrackId=_CigDhcpClientsDefaultRouterTrackId_Object((1,3,6,1,4,1,6889,2,1,17,1,1,1,20),_CigDhcpClientsDefaultRouterTrackId_Type())
cigDhcpClientsDefaultRouterTrackId.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDhcpClientsDefaultRouterTrackId.setStatus(_A)
_CigDnsResolver_ObjectIdentity=ObjectIdentity
cigDnsResolver=_CigDnsResolver_ObjectIdentity((1,3,6,1,4,1,6889,2,1,17,2))
_CigDnsResolverGenConfig_ObjectIdentity=ObjectIdentity
cigDnsResolverGenConfig=_CigDnsResolverGenConfig_ObjectIdentity((1,3,6,1,4,1,6889,2,1,17,2,1))
class _CigDnsResolverMode_Type(TruthValue):defaultValue=1
_CigDnsResolverMode_Type.__name__=_K
_CigDnsResolverMode_Object=MibScalar
cigDnsResolverMode=_CigDnsResolverMode_Object((1,3,6,1,4,1,6889,2,1,17,2,1,1),_CigDnsResolverMode_Type())
cigDnsResolverMode.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDnsResolverMode.setStatus(_A)
class _CigDnsResolverRetry_Type(Unsigned32):defaultValue=2
_CigDnsResolverRetry_Type.__name__=_E
_CigDnsResolverRetry_Object=MibScalar
cigDnsResolverRetry=_CigDnsResolverRetry_Object((1,3,6,1,4,1,6889,2,1,17,2,1,2),_CigDnsResolverRetry_Type())
cigDnsResolverRetry.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDnsResolverRetry.setStatus(_A)
class _CigDnsResolverTimeout_Type(Unsigned32):defaultValue=3
_CigDnsResolverTimeout_Type.__name__=_E
_CigDnsResolverTimeout_Object=MibScalar
cigDnsResolverTimeout=_CigDnsResolverTimeout_Object((1,3,6,1,4,1,6889,2,1,17,2,1,3),_CigDnsResolverTimeout_Type())
cigDnsResolverTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDnsResolverTimeout.setStatus(_A)
class _CigDnsResolverOperations_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),('clearDynamicServers',2),('clearDNSCache',3)))
_CigDnsResolverOperations_Type.__name__=_G
_CigDnsResolverOperations_Object=MibScalar
cigDnsResolverOperations=_CigDnsResolverOperations_Object((1,3,6,1,4,1,6889,2,1,17,2,1,4),_CigDnsResolverOperations_Type())
cigDnsResolverOperations.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDnsResolverOperations.setStatus(_A)
_CigDnsResolverDnsServersListTable_Object=MibTable
cigDnsResolverDnsServersListTable=_CigDnsResolverDnsServersListTable_Object((1,3,6,1,4,1,6889,2,1,17,2,2))
if mibBuilder.loadTexts:cigDnsResolverDnsServersListTable.setStatus(_A)
_CigDnsResolverDnsServersListEntry_Object=MibTableRow
cigDnsResolverDnsServersListEntry=_CigDnsResolverDnsServersListEntry_Object((1,3,6,1,4,1,6889,2,1,17,2,2,1))
cigDnsResolverDnsServersListEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:cigDnsResolverDnsServersListEntry.setStatus(_A)
_CigDnsResolverDnsServersListIndex_Type=Integer32
_CigDnsResolverDnsServersListIndex_Object=MibTableColumn
cigDnsResolverDnsServersListIndex=_CigDnsResolverDnsServersListIndex_Object((1,3,6,1,4,1,6889,2,1,17,2,2,1,1),_CigDnsResolverDnsServersListIndex_Type())
cigDnsResolverDnsServersListIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDnsResolverDnsServersListIndex.setStatus(_A)
class _CigDnsResolverDnsServersListDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CigDnsResolverDnsServersListDescription_Type.__name__=_F
_CigDnsResolverDnsServersListDescription_Object=MibTableColumn
cigDnsResolverDnsServersListDescription=_CigDnsResolverDnsServersListDescription_Object((1,3,6,1,4,1,6889,2,1,17,2,2,1,2),_CigDnsResolverDnsServersListDescription_Type())
cigDnsResolverDnsServersListDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDnsResolverDnsServersListDescription.setStatus(_A)
_CigDnsResolverDnsServersListRowStatus_Type=RowStatus
_CigDnsResolverDnsServersListRowStatus_Object=MibTableColumn
cigDnsResolverDnsServersListRowStatus=_CigDnsResolverDnsServersListRowStatus_Object((1,3,6,1,4,1,6889,2,1,17,2,2,1,3),_CigDnsResolverDnsServersListRowStatus_Type())
cigDnsResolverDnsServersListRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDnsResolverDnsServersListRowStatus.setStatus(_A)
_CigDnsResolverDnsServerTable_Object=MibTable
cigDnsResolverDnsServerTable=_CigDnsResolverDnsServerTable_Object((1,3,6,1,4,1,6889,2,1,17,2,3))
if mibBuilder.loadTexts:cigDnsResolverDnsServerTable.setStatus(_A)
_CigDnsResolverDnsServerEntry_Object=MibTableRow
cigDnsResolverDnsServerEntry=_CigDnsResolverDnsServerEntry_Object((1,3,6,1,4,1,6889,2,1,17,2,3,1))
cigDnsResolverDnsServerEntry.setIndexNames((0,_D,_O),(0,_D,_P))
if mibBuilder.loadTexts:cigDnsResolverDnsServerEntry.setStatus(_A)
_CigDnsResolverDnsServerListIndex_Type=Integer32
_CigDnsResolverDnsServerListIndex_Object=MibTableColumn
cigDnsResolverDnsServerListIndex=_CigDnsResolverDnsServerListIndex_Object((1,3,6,1,4,1,6889,2,1,17,2,3,1,1),_CigDnsResolverDnsServerListIndex_Type())
cigDnsResolverDnsServerListIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDnsResolverDnsServerListIndex.setStatus(_A)
_CigDnsResolverDnsServerIndex_Type=Integer32
_CigDnsResolverDnsServerIndex_Object=MibTableColumn
cigDnsResolverDnsServerIndex=_CigDnsResolverDnsServerIndex_Object((1,3,6,1,4,1,6889,2,1,17,2,3,1,2),_CigDnsResolverDnsServerIndex_Type())
cigDnsResolverDnsServerIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDnsResolverDnsServerIndex.setStatus(_A)
_CigDnsResolverDnsServerIpAddress_Type=IpAddress
_CigDnsResolverDnsServerIpAddress_Object=MibTableColumn
cigDnsResolverDnsServerIpAddress=_CigDnsResolverDnsServerIpAddress_Object((1,3,6,1,4,1,6889,2,1,17,2,3,1,3),_CigDnsResolverDnsServerIpAddress_Type())
cigDnsResolverDnsServerIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDnsResolverDnsServerIpAddress.setStatus(_A)
_CigDnsResolverDnsServerIfIndex_Type=Integer32
_CigDnsResolverDnsServerIfIndex_Object=MibTableColumn
cigDnsResolverDnsServerIfIndex=_CigDnsResolverDnsServerIfIndex_Object((1,3,6,1,4,1,6889,2,1,17,2,3,1,4),_CigDnsResolverDnsServerIfIndex_Type())
cigDnsResolverDnsServerIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDnsResolverDnsServerIfIndex.setStatus(_A)
class _CigDnsResolverDnsServerType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('static',1),('dynamic-dhcp',2),('dynamic-ppp',3)))
_CigDnsResolverDnsServerType_Type.__name__=_G
_CigDnsResolverDnsServerType_Object=MibTableColumn
cigDnsResolverDnsServerType=_CigDnsResolverDnsServerType_Object((1,3,6,1,4,1,6889,2,1,17,2,3,1,5),_CigDnsResolverDnsServerType_Type())
cigDnsResolverDnsServerType.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDnsResolverDnsServerType.setStatus(_A)
_CigDnsResolverDnsServerRowStatus_Type=RowStatus
_CigDnsResolverDnsServerRowStatus_Object=MibTableColumn
cigDnsResolverDnsServerRowStatus=_CigDnsResolverDnsServerRowStatus_Object((1,3,6,1,4,1,6889,2,1,17,2,3,1,6),_CigDnsResolverDnsServerRowStatus_Type())
cigDnsResolverDnsServerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDnsResolverDnsServerRowStatus.setStatus(_A)
_CigDnsResolverDnsServerInetAddressType_Type=InetAddressType
_CigDnsResolverDnsServerInetAddressType_Object=MibTableColumn
cigDnsResolverDnsServerInetAddressType=_CigDnsResolverDnsServerInetAddressType_Object((1,3,6,1,4,1,6889,2,1,17,2,3,1,7),_CigDnsResolverDnsServerInetAddressType_Type())
cigDnsResolverDnsServerInetAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDnsResolverDnsServerInetAddressType.setStatus(_A)
_CigDnsResolverDnsServerInetAddress_Type=InetAddress
_CigDnsResolverDnsServerInetAddress_Object=MibTableColumn
cigDnsResolverDnsServerInetAddress=_CigDnsResolverDnsServerInetAddress_Object((1,3,6,1,4,1,6889,2,1,17,2,3,1,8),_CigDnsResolverDnsServerInetAddress_Type())
cigDnsResolverDnsServerInetAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDnsResolverDnsServerInetAddress.setStatus(_A)
_CigDnsResolverDomainTable_Object=MibTable
cigDnsResolverDomainTable=_CigDnsResolverDomainTable_Object((1,3,6,1,4,1,6889,2,1,17,2,4))
if mibBuilder.loadTexts:cigDnsResolverDomainTable.setStatus(_A)
_CigDnsResolverDomainEntry_Object=MibTableRow
cigDnsResolverDomainEntry=_CigDnsResolverDomainEntry_Object((1,3,6,1,4,1,6889,2,1,17,2,4,1))
cigDnsResolverDomainEntry.setIndexNames((0,_D,_Q))
if mibBuilder.loadTexts:cigDnsResolverDomainEntry.setStatus(_A)
_CigDnsResolverDomainIndex_Type=Integer32
_CigDnsResolverDomainIndex_Object=MibTableColumn
cigDnsResolverDomainIndex=_CigDnsResolverDomainIndex_Object((1,3,6,1,4,1,6889,2,1,17,2,4,1,1),_CigDnsResolverDomainIndex_Type())
cigDnsResolverDomainIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cigDnsResolverDomainIndex.setStatus(_A)
class _CigDnsResolverDomain_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_CigDnsResolverDomain_Type.__name__=_F
_CigDnsResolverDomain_Object=MibTableColumn
cigDnsResolverDomain=_CigDnsResolverDomain_Object((1,3,6,1,4,1,6889,2,1,17,2,4,1,2),_CigDnsResolverDomain_Type())
cigDnsResolverDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDnsResolverDomain.setStatus(_A)
_CigDnsResolverDomainRowStatus_Type=RowStatus
_CigDnsResolverDomainRowStatus_Object=MibTableColumn
cigDnsResolverDomainRowStatus=_CigDnsResolverDomainRowStatus_Object((1,3,6,1,4,1,6889,2,1,17,2,4,1,3),_CigDnsResolverDomainRowStatus_Type())
cigDnsResolverDomainRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cigDnsResolverDomainRowStatus.setStatus(_A)
cigDhcpClientsConflictDetectionTrap=NotificationType((1,3,6,1,4,1,6889,2,1,17,1,0,1))
cigDhcpClientsConflictDetectionTrap.setObjects(*((_D,_R),(_D,_S),(_D,_T),(_D,_U),(_D,_V)))
if mibBuilder.loadTexts:cigDhcpClientsConflictDetectionTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'avaya':avaya,'mibs':mibs,'lsg':lsg,'cigClients':cigClients,'cigDhcpClients':cigDhcpClients,'cigDhcpClientsNotification':cigDhcpClientsNotification,'cigDhcpClientsConflictDetectionTrap':cigDhcpClientsConflictDetectionTrap,'cigDhcpClientsTable':cigDhcpClientsTable,'cigDhcpClientsEntry':cigDhcpClientsEntry,_L:cigDhcpClientsIfIndex,'cigDhcpClientsRowStatus':cigDhcpClientsRowStatus,_R:cigDhcpClientsIfAlias,_S:cigDhcpClientsIPAddress,'cigDhcpClientsSubnetMask':cigDhcpClientsSubnetMask,_U:cigDhcpClientsClientId,_T:cigDhcpClientsHostName,'cigDhcpClientsRequestLeaseTime':cigDhcpClientsRequestLeaseTime,'cigDhcpClientsReceiveLeaseTime':cigDhcpClientsReceiveLeaseTime,'cigDhcpClientsRemainLeaseTime':cigDhcpClientsRemainLeaseTime,'cigDhcpClientsRenewLeaseTime':cigDhcpClientsRenewLeaseTime,'cigDhcpClientsRebindLeaseTime':cigDhcpClientsRebindLeaseTime,'cigDhcpClientsDefaultGatewayList':cigDhcpClientsDefaultGatewayList,'cigDhcpClientsDnsServerList':cigDhcpClientsDnsServerList,'cigDhcpClientsDomainName':cigDhcpClientsDomainName,_V:cigDhcpClientsServerIpAddr,'cigDhcpClientsOperations':cigDhcpClientsOperations,'cigDhcpClientsStatus':cigDhcpClientsStatus,'cigDhcpClientsRequestBitmap':cigDhcpClientsRequestBitmap,'cigDhcpClientsDefaultRouterTrackId':cigDhcpClientsDefaultRouterTrackId,'cigDnsResolver':cigDnsResolver,'cigDnsResolverGenConfig':cigDnsResolverGenConfig,'cigDnsResolverMode':cigDnsResolverMode,'cigDnsResolverRetry':cigDnsResolverRetry,'cigDnsResolverTimeout':cigDnsResolverTimeout,'cigDnsResolverOperations':cigDnsResolverOperations,'cigDnsResolverDnsServersListTable':cigDnsResolverDnsServersListTable,'cigDnsResolverDnsServersListEntry':cigDnsResolverDnsServersListEntry,_N:cigDnsResolverDnsServersListIndex,'cigDnsResolverDnsServersListDescription':cigDnsResolverDnsServersListDescription,'cigDnsResolverDnsServersListRowStatus':cigDnsResolverDnsServersListRowStatus,'cigDnsResolverDnsServerTable':cigDnsResolverDnsServerTable,'cigDnsResolverDnsServerEntry':cigDnsResolverDnsServerEntry,_O:cigDnsResolverDnsServerListIndex,_P:cigDnsResolverDnsServerIndex,'cigDnsResolverDnsServerIpAddress':cigDnsResolverDnsServerIpAddress,'cigDnsResolverDnsServerIfIndex':cigDnsResolverDnsServerIfIndex,'cigDnsResolverDnsServerType':cigDnsResolverDnsServerType,'cigDnsResolverDnsServerRowStatus':cigDnsResolverDnsServerRowStatus,'cigDnsResolverDnsServerInetAddressType':cigDnsResolverDnsServerInetAddressType,'cigDnsResolverDnsServerInetAddress':cigDnsResolverDnsServerInetAddress,'cigDnsResolverDomainTable':cigDnsResolverDomainTable,'cigDnsResolverDomainEntry':cigDnsResolverDomainEntry,_Q:cigDnsResolverDomainIndex,'cigDnsResolverDomain':cigDnsResolverDomain,'cigDnsResolverDomainRowStatus':cigDnsResolverDomainRowStatus})