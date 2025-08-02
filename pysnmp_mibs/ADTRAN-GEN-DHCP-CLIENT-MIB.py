_G='read-write'
_F='ifIndex'
_E='IF-MIB'
_D='OctetString'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenDhcpClient,adGenDhcpClientId=mibBuilder.importSymbols('ADTRAN-SHARED-DHCP-MIB','adGenDhcpClient','adGenDhcpClientId')
ifIndex,=mibBuilder.importSymbols(_E,_F)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenDhcpClientMib=ModuleIdentity((1,3,6,1,4,1,664,6,10000,80,1,1))
if mibBuilder.loadTexts:adGenDhcpClientMib.setRevisions(('2009-08-13 00:00',))
class AdGenDhcpClientState(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('init',1),('selecting',2),('requesting',3),('bound',4),('renewing',5),('rebinding',6)))
_AdGenDhcpClientMIBObjects_ObjectIdentity=ObjectIdentity
adGenDhcpClientMIBObjects=_AdGenDhcpClientMIBObjects_ObjectIdentity((1,3,6,1,4,1,664,5,80,1,1))
_AdGenDhcpClientStatus_ObjectIdentity=ObjectIdentity
adGenDhcpClientStatus=_AdGenDhcpClientStatus_ObjectIdentity((1,3,6,1,4,1,664,5,80,1,1,1))
_AdGenDhcpClientStatusTable_Object=MibTable
adGenDhcpClientStatusTable=_AdGenDhcpClientStatusTable_Object((1,3,6,1,4,1,664,5,80,1,1,1,1))
if mibBuilder.loadTexts:adGenDhcpClientStatusTable.setStatus(_A)
_AdGenDhcpClientStatusEntry_Object=MibTableRow
adGenDhcpClientStatusEntry=_AdGenDhcpClientStatusEntry_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1))
adGenDhcpClientStatusEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenDhcpClientStatusEntry.setStatus(_A)
_AdGenDhcpClientStatusState_Type=AdGenDhcpClientState
_AdGenDhcpClientStatusState_Object=MibTableColumn
adGenDhcpClientStatusState=_AdGenDhcpClientStatusState_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,1),_AdGenDhcpClientStatusState_Type())
adGenDhcpClientStatusState.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusState.setStatus(_A)
class _AdGenDhcpClientStatusClientIdentifier_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,80))
_AdGenDhcpClientStatusClientIdentifier_Type.__name__=_D
_AdGenDhcpClientStatusClientIdentifier_Object=MibTableColumn
adGenDhcpClientStatusClientIdentifier=_AdGenDhcpClientStatusClientIdentifier_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,2),_AdGenDhcpClientStatusClientIdentifier_Type())
adGenDhcpClientStatusClientIdentifier.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusClientIdentifier.setStatus(_A)
class _AdGenDhcpClientStatusHostName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,35))
_AdGenDhcpClientStatusHostName_Type.__name__=_D
_AdGenDhcpClientStatusHostName_Object=MibTableColumn
adGenDhcpClientStatusHostName=_AdGenDhcpClientStatusHostName_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,3),_AdGenDhcpClientStatusHostName_Type())
adGenDhcpClientStatusHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusHostName.setStatus(_A)
_AdGenDhcpClientStatusIpAddressType_Type=InetAddressType
_AdGenDhcpClientStatusIpAddressType_Object=MibTableColumn
adGenDhcpClientStatusIpAddressType=_AdGenDhcpClientStatusIpAddressType_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,4),_AdGenDhcpClientStatusIpAddressType_Type())
adGenDhcpClientStatusIpAddressType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusIpAddressType.setStatus(_A)
_AdGenDhcpClientStatusIpAddress_Type=InetAddress
_AdGenDhcpClientStatusIpAddress_Object=MibTableColumn
adGenDhcpClientStatusIpAddress=_AdGenDhcpClientStatusIpAddress_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,5),_AdGenDhcpClientStatusIpAddress_Type())
adGenDhcpClientStatusIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusIpAddress.setStatus(_A)
_AdGenDhcpClientStatusSubnetMaskType_Type=InetAddressType
_AdGenDhcpClientStatusSubnetMaskType_Object=MibTableColumn
adGenDhcpClientStatusSubnetMaskType=_AdGenDhcpClientStatusSubnetMaskType_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,6),_AdGenDhcpClientStatusSubnetMaskType_Type())
adGenDhcpClientStatusSubnetMaskType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusSubnetMaskType.setStatus(_A)
_AdGenDhcpClientStatusSubnetMask_Type=InetAddress
_AdGenDhcpClientStatusSubnetMask_Object=MibTableColumn
adGenDhcpClientStatusSubnetMask=_AdGenDhcpClientStatusSubnetMask_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,7),_AdGenDhcpClientStatusSubnetMask_Type())
adGenDhcpClientStatusSubnetMask.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusSubnetMask.setStatus(_A)
_AdGenDhcpClientStatusDhcpLeaseServerType_Type=InetAddressType
_AdGenDhcpClientStatusDhcpLeaseServerType_Object=MibTableColumn
adGenDhcpClientStatusDhcpLeaseServerType=_AdGenDhcpClientStatusDhcpLeaseServerType_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,8),_AdGenDhcpClientStatusDhcpLeaseServerType_Type())
adGenDhcpClientStatusDhcpLeaseServerType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusDhcpLeaseServerType.setStatus(_A)
_AdGenDhcpClientStatusDhcpLeaseServer_Type=InetAddress
_AdGenDhcpClientStatusDhcpLeaseServer_Object=MibTableColumn
adGenDhcpClientStatusDhcpLeaseServer=_AdGenDhcpClientStatusDhcpLeaseServer_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,9),_AdGenDhcpClientStatusDhcpLeaseServer_Type())
adGenDhcpClientStatusDhcpLeaseServer.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusDhcpLeaseServer.setStatus(_A)
_AdGenDhcpClientStatusLease_Type=Unsigned32
_AdGenDhcpClientStatusLease_Object=MibTableColumn
adGenDhcpClientStatusLease=_AdGenDhcpClientStatusLease_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,10),_AdGenDhcpClientStatusLease_Type())
adGenDhcpClientStatusLease.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusLease.setStatus(_A)
_AdGenDhcpClientStatusLeaseRemaining_Type=Unsigned32
_AdGenDhcpClientStatusLeaseRemaining_Object=MibTableColumn
adGenDhcpClientStatusLeaseRemaining=_AdGenDhcpClientStatusLeaseRemaining_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,11),_AdGenDhcpClientStatusLeaseRemaining_Type())
adGenDhcpClientStatusLeaseRemaining.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusLeaseRemaining.setStatus(_A)
_AdGenDhcpClientStatusPrimaryDNSType_Type=InetAddressType
_AdGenDhcpClientStatusPrimaryDNSType_Object=MibTableColumn
adGenDhcpClientStatusPrimaryDNSType=_AdGenDhcpClientStatusPrimaryDNSType_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,12),_AdGenDhcpClientStatusPrimaryDNSType_Type())
adGenDhcpClientStatusPrimaryDNSType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusPrimaryDNSType.setStatus(_A)
_AdGenDhcpClientStatusPrimaryDNS_Type=InetAddress
_AdGenDhcpClientStatusPrimaryDNS_Object=MibTableColumn
adGenDhcpClientStatusPrimaryDNS=_AdGenDhcpClientStatusPrimaryDNS_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,13),_AdGenDhcpClientStatusPrimaryDNS_Type())
adGenDhcpClientStatusPrimaryDNS.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusPrimaryDNS.setStatus(_A)
_AdGenDhcpClientStatusSecondaryDNSType_Type=InetAddressType
_AdGenDhcpClientStatusSecondaryDNSType_Object=MibTableColumn
adGenDhcpClientStatusSecondaryDNSType=_AdGenDhcpClientStatusSecondaryDNSType_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,14),_AdGenDhcpClientStatusSecondaryDNSType_Type())
adGenDhcpClientStatusSecondaryDNSType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusSecondaryDNSType.setStatus(_A)
_AdGenDhcpClientStatusSecondaryDNS_Type=InetAddress
_AdGenDhcpClientStatusSecondaryDNS_Object=MibTableColumn
adGenDhcpClientStatusSecondaryDNS=_AdGenDhcpClientStatusSecondaryDNS_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,15),_AdGenDhcpClientStatusSecondaryDNS_Type())
adGenDhcpClientStatusSecondaryDNS.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusSecondaryDNS.setStatus(_A)
_AdGenDhcpClientStatusRoutersType_Type=InetAddressType
_AdGenDhcpClientStatusRoutersType_Object=MibTableColumn
adGenDhcpClientStatusRoutersType=_AdGenDhcpClientStatusRoutersType_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,16),_AdGenDhcpClientStatusRoutersType_Type())
adGenDhcpClientStatusRoutersType.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusRoutersType.setStatus(_A)
_AdGenDhcpClientStatusRouters_Type=InetAddress
_AdGenDhcpClientStatusRouters_Object=MibTableColumn
adGenDhcpClientStatusRouters=_AdGenDhcpClientStatusRouters_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,17),_AdGenDhcpClientStatusRouters_Type())
adGenDhcpClientStatusRouters.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusRouters.setStatus(_A)
_AdGenDhcpClientStatusTxDiscovery_Type=Counter32
_AdGenDhcpClientStatusTxDiscovery_Object=MibTableColumn
adGenDhcpClientStatusTxDiscovery=_AdGenDhcpClientStatusTxDiscovery_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,18),_AdGenDhcpClientStatusTxDiscovery_Type())
adGenDhcpClientStatusTxDiscovery.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusTxDiscovery.setStatus(_A)
_AdGenDhcpClientStatusTxRequest_Type=Counter32
_AdGenDhcpClientStatusTxRequest_Object=MibTableColumn
adGenDhcpClientStatusTxRequest=_AdGenDhcpClientStatusTxRequest_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,19),_AdGenDhcpClientStatusTxRequest_Type())
adGenDhcpClientStatusTxRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusTxRequest.setStatus(_A)
_AdGenDhcpClientStatusTxDecline_Type=Counter32
_AdGenDhcpClientStatusTxDecline_Object=MibTableColumn
adGenDhcpClientStatusTxDecline=_AdGenDhcpClientStatusTxDecline_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,20),_AdGenDhcpClientStatusTxDecline_Type())
adGenDhcpClientStatusTxDecline.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusTxDecline.setStatus(_A)
_AdGenDhcpClientStatusTxRelease_Type=Counter32
_AdGenDhcpClientStatusTxRelease_Object=MibTableColumn
adGenDhcpClientStatusTxRelease=_AdGenDhcpClientStatusTxRelease_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,21),_AdGenDhcpClientStatusTxRelease_Type())
adGenDhcpClientStatusTxRelease.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusTxRelease.setStatus(_A)
_AdGenDhcpClientStatusTxInform_Type=Counter32
_AdGenDhcpClientStatusTxInform_Object=MibTableColumn
adGenDhcpClientStatusTxInform=_AdGenDhcpClientStatusTxInform_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,22),_AdGenDhcpClientStatusTxInform_Type())
adGenDhcpClientStatusTxInform.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusTxInform.setStatus(_A)
_AdGenDhcpClientStatusRxOffer_Type=Counter32
_AdGenDhcpClientStatusRxOffer_Object=MibTableColumn
adGenDhcpClientStatusRxOffer=_AdGenDhcpClientStatusRxOffer_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,23),_AdGenDhcpClientStatusRxOffer_Type())
adGenDhcpClientStatusRxOffer.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusRxOffer.setStatus(_A)
_AdGenDhcpClientStatusRxAck_Type=Counter32
_AdGenDhcpClientStatusRxAck_Object=MibTableColumn
adGenDhcpClientStatusRxAck=_AdGenDhcpClientStatusRxAck_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,24),_AdGenDhcpClientStatusRxAck_Type())
adGenDhcpClientStatusRxAck.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusRxAck.setStatus(_A)
_AdGenDhcpClientStatusRxNak_Type=Counter32
_AdGenDhcpClientStatusRxNak_Object=MibTableColumn
adGenDhcpClientStatusRxNak=_AdGenDhcpClientStatusRxNak_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,25),_AdGenDhcpClientStatusRxNak_Type())
adGenDhcpClientStatusRxNak.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusRxNak.setStatus(_A)
_AdGenDhcpClientStatusRxRunt_Type=Counter32
_AdGenDhcpClientStatusRxRunt_Object=MibTableColumn
adGenDhcpClientStatusRxRunt=_AdGenDhcpClientStatusRxRunt_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,26),_AdGenDhcpClientStatusRxRunt_Type())
adGenDhcpClientStatusRxRunt.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusRxRunt.setStatus(_A)
_AdGenDhcpClientStatusRxInvalid_Type=Counter32
_AdGenDhcpClientStatusRxInvalid_Object=MibTableColumn
adGenDhcpClientStatusRxInvalid=_AdGenDhcpClientStatusRxInvalid_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,27),_AdGenDhcpClientStatusRxInvalid_Type())
adGenDhcpClientStatusRxInvalid.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusRxInvalid.setStatus(_A)
_AdGenDhcpClientStatusRxOos_Type=Counter32
_AdGenDhcpClientStatusRxOos_Object=MibTableColumn
adGenDhcpClientStatusRxOos=_AdGenDhcpClientStatusRxOos_Object((1,3,6,1,4,1,664,5,80,1,1,1,1,1,28),_AdGenDhcpClientStatusRxOos_Type())
adGenDhcpClientStatusRxOos.setMaxAccess(_B)
if mibBuilder.loadTexts:adGenDhcpClientStatusRxOos.setStatus(_A)
_AdGenDhcpClientCommand_ObjectIdentity=ObjectIdentity
adGenDhcpClientCommand=_AdGenDhcpClientCommand_ObjectIdentity((1,3,6,1,4,1,664,5,80,1,1,2))
_AdGenDhcpClientCommandTable_Object=MibTable
adGenDhcpClientCommandTable=_AdGenDhcpClientCommandTable_Object((1,3,6,1,4,1,664,5,80,1,1,2,1))
if mibBuilder.loadTexts:adGenDhcpClientCommandTable.setStatus(_A)
_AdGenDhcpClientCommandEntry_Object=MibTableRow
adGenDhcpClientCommandEntry=_AdGenDhcpClientCommandEntry_Object((1,3,6,1,4,1,664,5,80,1,1,2,1,1))
adGenDhcpClientCommandEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:adGenDhcpClientCommandEntry.setStatus(_A)
class _AdGenDhcpClientCommandRenew_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('renew',1))
_AdGenDhcpClientCommandRenew_Type.__name__=_C
_AdGenDhcpClientCommandRenew_Object=MibTableColumn
adGenDhcpClientCommandRenew=_AdGenDhcpClientCommandRenew_Object((1,3,6,1,4,1,664,5,80,1,1,2,1,1,1),_AdGenDhcpClientCommandRenew_Type())
adGenDhcpClientCommandRenew.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenDhcpClientCommandRenew.setStatus(_A)
class _AdGenDhcpClientCommandRelease_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('release',1))
_AdGenDhcpClientCommandRelease_Type.__name__=_C
_AdGenDhcpClientCommandRelease_Object=MibTableColumn
adGenDhcpClientCommandRelease=_AdGenDhcpClientCommandRelease_Object((1,3,6,1,4,1,664,5,80,1,1,2,1,1,2),_AdGenDhcpClientCommandRelease_Type())
adGenDhcpClientCommandRelease.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenDhcpClientCommandRelease.setStatus(_A)
class _AdGenDhcpClientCommandResetStats_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('reset',1))
_AdGenDhcpClientCommandResetStats_Type.__name__=_C
_AdGenDhcpClientCommandResetStats_Object=MibTableColumn
adGenDhcpClientCommandResetStats=_AdGenDhcpClientCommandResetStats_Object((1,3,6,1,4,1,664,5,80,1,1,2,1,1,3),_AdGenDhcpClientCommandResetStats_Type())
adGenDhcpClientCommandResetStats.setMaxAccess(_G)
if mibBuilder.loadTexts:adGenDhcpClientCommandResetStats.setStatus(_A)
mibBuilder.exportSymbols('ADTRAN-GEN-DHCP-CLIENT-MIB',**{'AdGenDhcpClientState':AdGenDhcpClientState,'adGenDhcpClientMIBObjects':adGenDhcpClientMIBObjects,'adGenDhcpClientStatus':adGenDhcpClientStatus,'adGenDhcpClientStatusTable':adGenDhcpClientStatusTable,'adGenDhcpClientStatusEntry':adGenDhcpClientStatusEntry,'adGenDhcpClientStatusState':adGenDhcpClientStatusState,'adGenDhcpClientStatusClientIdentifier':adGenDhcpClientStatusClientIdentifier,'adGenDhcpClientStatusHostName':adGenDhcpClientStatusHostName,'adGenDhcpClientStatusIpAddressType':adGenDhcpClientStatusIpAddressType,'adGenDhcpClientStatusIpAddress':adGenDhcpClientStatusIpAddress,'adGenDhcpClientStatusSubnetMaskType':adGenDhcpClientStatusSubnetMaskType,'adGenDhcpClientStatusSubnetMask':adGenDhcpClientStatusSubnetMask,'adGenDhcpClientStatusDhcpLeaseServerType':adGenDhcpClientStatusDhcpLeaseServerType,'adGenDhcpClientStatusDhcpLeaseServer':adGenDhcpClientStatusDhcpLeaseServer,'adGenDhcpClientStatusLease':adGenDhcpClientStatusLease,'adGenDhcpClientStatusLeaseRemaining':adGenDhcpClientStatusLeaseRemaining,'adGenDhcpClientStatusPrimaryDNSType':adGenDhcpClientStatusPrimaryDNSType,'adGenDhcpClientStatusPrimaryDNS':adGenDhcpClientStatusPrimaryDNS,'adGenDhcpClientStatusSecondaryDNSType':adGenDhcpClientStatusSecondaryDNSType,'adGenDhcpClientStatusSecondaryDNS':adGenDhcpClientStatusSecondaryDNS,'adGenDhcpClientStatusRoutersType':adGenDhcpClientStatusRoutersType,'adGenDhcpClientStatusRouters':adGenDhcpClientStatusRouters,'adGenDhcpClientStatusTxDiscovery':adGenDhcpClientStatusTxDiscovery,'adGenDhcpClientStatusTxRequest':adGenDhcpClientStatusTxRequest,'adGenDhcpClientStatusTxDecline':adGenDhcpClientStatusTxDecline,'adGenDhcpClientStatusTxRelease':adGenDhcpClientStatusTxRelease,'adGenDhcpClientStatusTxInform':adGenDhcpClientStatusTxInform,'adGenDhcpClientStatusRxOffer':adGenDhcpClientStatusRxOffer,'adGenDhcpClientStatusRxAck':adGenDhcpClientStatusRxAck,'adGenDhcpClientStatusRxNak':adGenDhcpClientStatusRxNak,'adGenDhcpClientStatusRxRunt':adGenDhcpClientStatusRxRunt,'adGenDhcpClientStatusRxInvalid':adGenDhcpClientStatusRxInvalid,'adGenDhcpClientStatusRxOos':adGenDhcpClientStatusRxOos,'adGenDhcpClientCommand':adGenDhcpClientCommand,'adGenDhcpClientCommandTable':adGenDhcpClientCommandTable,'adGenDhcpClientCommandEntry':adGenDhcpClientCommandEntry,'adGenDhcpClientCommandRenew':adGenDhcpClientCommandRenew,'adGenDhcpClientCommandRelease':adGenDhcpClientCommandRelease,'adGenDhcpClientCommandResetStats':adGenDhcpClientCommandResetStats,'adGenDhcpClientMib':adGenDhcpClientMib})