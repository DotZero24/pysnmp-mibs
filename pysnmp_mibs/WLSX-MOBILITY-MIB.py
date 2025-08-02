_I='mobilityHostMac'
_H='mobilityHomeAgentIp'
_G='mobilityHomeAgentMask'
_F='mobilityHomeAgentSubnet'
_E='mobilityDomainName'
_D='not-accessible'
_C='WLSX-MOBILITY-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
wlsxEnterpriseMibModules,=mibBuilder.importSymbols('ARUBA-MIB','wlsxEnterpriseMibModules')
ArubaActiveState,ArubaAuthenticationMethods,ArubaEnableValue,ArubaEncryptionMethods,ArubaFrameType,ArubaPhyType,ArubaRogueApType=mibBuilder.importSymbols('ARUBA-TC','ArubaActiveState','ArubaAuthenticationMethods','ArubaEnableValue','ArubaEncryptionMethods','ArubaFrameType','ArubaPhyType','ArubaRogueApType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,snmpModules=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','snmpModules')
DisplayString,MacAddress,PhysAddress,RowStatus,StorageType,TAddress,TDomain,TextualConvention,TestAndIncr,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','StorageType','TAddress','TDomain','TextualConvention','TestAndIncr','TimeInterval','TruthValue')
wlsxMobilityMIB=ModuleIdentity((1,3,6,1,4,1,14823,2,2,1,9))
if mibBuilder.loadTexts:wlsxMobilityMIB.setRevisions(('2020-08-14 17:45',))
_WlsxMobilityConfigGroup_ObjectIdentity=ObjectIdentity
wlsxMobilityConfigGroup=_WlsxMobilityConfigGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,9,1))
_WlsxMobilityDomainTable_Object=MibTable
wlsxMobilityDomainTable=_WlsxMobilityDomainTable_Object((1,3,6,1,4,1,14823,2,2,1,9,1,1))
if mibBuilder.loadTexts:wlsxMobilityDomainTable.setStatus(_A)
_WlsxMobilityDomainEntry_Object=MibTableRow
wlsxMobilityDomainEntry=_WlsxMobilityDomainEntry_Object((1,3,6,1,4,1,14823,2,2,1,9,1,1,1))
wlsxMobilityDomainEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:wlsxMobilityDomainEntry.setStatus(_A)
_MobilityDomainName_Type=DisplayString
_MobilityDomainName_Object=MibTableColumn
mobilityDomainName=_MobilityDomainName_Object((1,3,6,1,4,1,14823,2,2,1,9,1,1,1,1),_MobilityDomainName_Type())
mobilityDomainName.setMaxAccess(_D)
if mibBuilder.loadTexts:mobilityDomainName.setStatus(_A)
_MobilityDomainIsExclusive_Type=ArubaEnableValue
_MobilityDomainIsExclusive_Object=MibTableColumn
mobilityDomainIsExclusive=_MobilityDomainIsExclusive_Object((1,3,6,1,4,1,14823,2,2,1,9,1,1,1,2),_MobilityDomainIsExclusive_Type())
mobilityDomainIsExclusive.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityDomainIsExclusive.setStatus('deprecated')
_MobilityDomainStatus_Type=RowStatus
_MobilityDomainStatus_Object=MibTableColumn
mobilityDomainStatus=_MobilityDomainStatus_Object((1,3,6,1,4,1,14823,2,2,1,9,1,1,1,3),_MobilityDomainStatus_Type())
mobilityDomainStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:mobilityDomainStatus.setStatus(_A)
_WlsxMobilityHomeAgentTable_Object=MibTable
wlsxMobilityHomeAgentTable=_WlsxMobilityHomeAgentTable_Object((1,3,6,1,4,1,14823,2,2,1,9,1,3))
if mibBuilder.loadTexts:wlsxMobilityHomeAgentTable.setStatus(_A)
_WlsxMobilityHomeAgentEntry_Object=MibTableRow
wlsxMobilityHomeAgentEntry=_WlsxMobilityHomeAgentEntry_Object((1,3,6,1,4,1,14823,2,2,1,9,1,3,1))
wlsxMobilityHomeAgentEntry.setIndexNames((0,_C,_F),(0,_C,_G),(0,_C,_H))
if mibBuilder.loadTexts:wlsxMobilityHomeAgentEntry.setStatus(_A)
_MobilityHomeAgentSubnet_Type=IpAddress
_MobilityHomeAgentSubnet_Object=MibTableColumn
mobilityHomeAgentSubnet=_MobilityHomeAgentSubnet_Object((1,3,6,1,4,1,14823,2,2,1,9,1,3,1,1),_MobilityHomeAgentSubnet_Type())
mobilityHomeAgentSubnet.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityHomeAgentSubnet.setStatus(_A)
_MobilityHomeAgentMask_Type=IpAddress
_MobilityHomeAgentMask_Object=MibTableColumn
mobilityHomeAgentMask=_MobilityHomeAgentMask_Object((1,3,6,1,4,1,14823,2,2,1,9,1,3,1,2),_MobilityHomeAgentMask_Type())
mobilityHomeAgentMask.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityHomeAgentMask.setStatus(_A)
_MobilityHomeAgentIp_Type=IpAddress
_MobilityHomeAgentIp_Object=MibTableColumn
mobilityHomeAgentIp=_MobilityHomeAgentIp_Object((1,3,6,1,4,1,14823,2,2,1,9,1,3,1,3),_MobilityHomeAgentIp_Type())
mobilityHomeAgentIp.setMaxAccess(_D)
if mibBuilder.loadTexts:mobilityHomeAgentIp.setStatus(_A)
_MobilityHomeAgentVlan_Type=Integer32
_MobilityHomeAgentVlan_Object=MibTableColumn
mobilityHomeAgentVlan=_MobilityHomeAgentVlan_Object((1,3,6,1,4,1,14823,2,2,1,9,1,3,1,4),_MobilityHomeAgentVlan_Type())
mobilityHomeAgentVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityHomeAgentVlan.setStatus(_A)
_WlsxMobilityHostTable_Object=MibTable
wlsxMobilityHostTable=_WlsxMobilityHostTable_Object((1,3,6,1,4,1,14823,2,2,1,9,1,4))
if mibBuilder.loadTexts:wlsxMobilityHostTable.setStatus(_A)
_WlsxMobilityHostEntry_Object=MibTableRow
wlsxMobilityHostEntry=_WlsxMobilityHostEntry_Object((1,3,6,1,4,1,14823,2,2,1,9,1,4,1))
wlsxMobilityHostEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:wlsxMobilityHostEntry.setStatus(_A)
_MobilityHostMac_Type=MacAddress
_MobilityHostMac_Object=MibTableColumn
mobilityHostMac=_MobilityHostMac_Object((1,3,6,1,4,1,14823,2,2,1,9,1,4,1,1),_MobilityHostMac_Type())
mobilityHostMac.setMaxAccess(_D)
if mibBuilder.loadTexts:mobilityHostMac.setStatus(_A)
_MobilityHostIp_Type=IpAddress
_MobilityHostIp_Object=MibTableColumn
mobilityHostIp=_MobilityHostIp_Object((1,3,6,1,4,1,14823,2,2,1,9,1,4,1,2),_MobilityHostIp_Type())
mobilityHostIp.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityHostIp.setStatus(_A)
_MobilityHostStatus_Type=DisplayString
_MobilityHostStatus_Object=MibTableColumn
mobilityHostStatus=_MobilityHostStatus_Object((1,3,6,1,4,1,14823,2,2,1,9,1,4,1,3),_MobilityHostStatus_Type())
mobilityHostStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityHostStatus.setStatus(_A)
_MobilityHostServiceTime_Type=Integer32
_MobilityHostServiceTime_Object=MibTableColumn
mobilityHostServiceTime=_MobilityHostServiceTime_Object((1,3,6,1,4,1,14823,2,2,1,9,1,4,1,4),_MobilityHostServiceTime_Type())
mobilityHostServiceTime.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityHostServiceTime.setStatus(_A)
_MobilityHostHomeVlan_Type=Integer32
_MobilityHostHomeVlan_Object=MibTableColumn
mobilityHostHomeVlan=_MobilityHostHomeVlan_Object((1,3,6,1,4,1,14823,2,2,1,9,1,4,1,5),_MobilityHostHomeVlan_Type())
mobilityHostHomeVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityHostHomeVlan.setStatus(_A)
_MobilityHostHomeNetwork_Type=IpAddress
_MobilityHostHomeNetwork_Object=MibTableColumn
mobilityHostHomeNetwork=_MobilityHostHomeNetwork_Object((1,3,6,1,4,1,14823,2,2,1,9,1,4,1,6),_MobilityHostHomeNetwork_Type())
mobilityHostHomeNetwork.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityHostHomeNetwork.setStatus(_A)
_MobilityHostHomeMask_Type=IpAddress
_MobilityHostHomeMask_Object=MibTableColumn
mobilityHostHomeMask=_MobilityHostHomeMask_Object((1,3,6,1,4,1,14823,2,2,1,9,1,4,1,7),_MobilityHostHomeMask_Type())
mobilityHostHomeMask.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityHostHomeMask.setStatus(_A)
_MobilityHostDhcpInfo_Type=DisplayString
_MobilityHostDhcpInfo_Object=MibTableColumn
mobilityHostDhcpInfo=_MobilityHostDhcpInfo_Object((1,3,6,1,4,1,14823,2,2,1,9,1,4,1,8),_MobilityHostDhcpInfo_Type())
mobilityHostDhcpInfo.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityHostDhcpInfo.setStatus(_A)
_WlsxMobilityProxyStatsGroup_ObjectIdentity=ObjectIdentity
wlsxMobilityProxyStatsGroup=_WlsxMobilityProxyStatsGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,9,2))
_MobilityProxyPktRx_Type=Counter32
_MobilityProxyPktRx_Object=MibScalar
mobilityProxyPktRx=_MobilityProxyPktRx_Object((1,3,6,1,4,1,14823,2,2,1,9,2,1),_MobilityProxyPktRx_Type())
mobilityProxyPktRx.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityProxyPktRx.setStatus(_A)
_MobilityProxyPktHandled_Type=Counter32
_MobilityProxyPktHandled_Object=MibScalar
mobilityProxyPktHandled=_MobilityProxyPktHandled_Object((1,3,6,1,4,1,14823,2,2,1,9,2,2),_MobilityProxyPktHandled_Type())
mobilityProxyPktHandled.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityProxyPktHandled.setStatus(_A)
_MobilityProxyPktFwd_Type=Counter32
_MobilityProxyPktFwd_Object=MibScalar
mobilityProxyPktFwd=_MobilityProxyPktFwd_Object((1,3,6,1,4,1,14823,2,2,1,9,2,3),_MobilityProxyPktFwd_Type())
mobilityProxyPktFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityProxyPktFwd.setStatus(_A)
_MobilityProxyPktDrop_Type=Counter32
_MobilityProxyPktDrop_Object=MibScalar
mobilityProxyPktDrop=_MobilityProxyPktDrop_Object((1,3,6,1,4,1,14823,2,2,1,9,2,4),_MobilityProxyPktDrop_Type())
mobilityProxyPktDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityProxyPktDrop.setStatus(_A)
_MobilityProxyBusy_Type=Counter32
_MobilityProxyBusy_Object=MibScalar
mobilityProxyBusy=_MobilityProxyBusy_Object((1,3,6,1,4,1,14823,2,2,1,9,2,5),_MobilityProxyBusy_Type())
mobilityProxyBusy.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityProxyBusy.setStatus(_A)
_MobilityProxyNoMobility_Type=Counter32
_MobilityProxyNoMobility_Object=MibScalar
mobilityProxyNoMobility=_MobilityProxyNoMobility_Object((1,3,6,1,4,1,14823,2,2,1,9,2,6),_MobilityProxyNoMobility_Type())
mobilityProxyNoMobility.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityProxyNoMobility.setStatus(_A)
_MobilityProxyClientIPChg_Type=Counter32
_MobilityProxyClientIPChg_Object=MibScalar
mobilityProxyClientIPChg=_MobilityProxyClientIPChg_Object((1,3,6,1,4,1,14823,2,2,1,9,2,7),_MobilityProxyClientIPChg_Type())
mobilityProxyClientIPChg.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityProxyClientIPChg.setStatus(_A)
_MobilityProxyClientEssidChg_Type=Counter32
_MobilityProxyClientEssidChg_Object=MibScalar
mobilityProxyClientEssidChg=_MobilityProxyClientEssidChg_Object((1,3,6,1,4,1,14823,2,2,1,9,2,8),_MobilityProxyClientEssidChg_Type())
mobilityProxyClientEssidChg.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityProxyClientEssidChg.setStatus(_A)
_WlsxMobilityProxyDHCPStatsGroup_ObjectIdentity=ObjectIdentity
wlsxMobilityProxyDHCPStatsGroup=_WlsxMobilityProxyDHCPStatsGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,9,3))
_MobilityProxyDhcpBootpRx_Type=Counter32
_MobilityProxyDhcpBootpRx_Object=MibScalar
mobilityProxyDhcpBootpRx=_MobilityProxyDhcpBootpRx_Object((1,3,6,1,4,1,14823,2,2,1,9,3,1),_MobilityProxyDhcpBootpRx_Type())
mobilityProxyDhcpBootpRx.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityProxyDhcpBootpRx.setStatus(_A)
_MobilityProxyDhcpPktProc_Type=Counter32
_MobilityProxyDhcpPktProc_Object=MibScalar
mobilityProxyDhcpPktProc=_MobilityProxyDhcpPktProc_Object((1,3,6,1,4,1,14823,2,2,1,9,3,2),_MobilityProxyDhcpPktProc_Type())
mobilityProxyDhcpPktProc.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityProxyDhcpPktProc.setStatus(_A)
_MobilityProxyDhcpPktFwd_Type=Counter32
_MobilityProxyDhcpPktFwd_Object=MibScalar
mobilityProxyDhcpPktFwd=_MobilityProxyDhcpPktFwd_Object((1,3,6,1,4,1,14823,2,2,1,9,3,3),_MobilityProxyDhcpPktFwd_Type())
mobilityProxyDhcpPktFwd.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityProxyDhcpPktFwd.setStatus(_A)
_MobilityProxyDhcpPktDrop_Type=Counter32
_MobilityProxyDhcpPktDrop_Object=MibScalar
mobilityProxyDhcpPktDrop=_MobilityProxyDhcpPktDrop_Object((1,3,6,1,4,1,14823,2,2,1,9,3,4),_MobilityProxyDhcpPktDrop_Type())
mobilityProxyDhcpPktDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityProxyDhcpPktDrop.setStatus(_A)
_MobilityProxyDHCPNak_Type=Counter32
_MobilityProxyDHCPNak_Object=MibScalar
mobilityProxyDHCPNak=_MobilityProxyDHCPNak_Object((1,3,6,1,4,1,14823,2,2,1,9,3,5),_MobilityProxyDHCPNak_Type())
mobilityProxyDHCPNak.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityProxyDHCPNak.setStatus(_A)
_MobilityProxyBadDHCPPkt_Type=Counter32
_MobilityProxyBadDHCPPkt_Object=MibScalar
mobilityProxyBadDHCPPkt=_MobilityProxyBadDHCPPkt_Object((1,3,6,1,4,1,14823,2,2,1,9,3,6),_MobilityProxyBadDHCPPkt_Type())
mobilityProxyBadDHCPPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityProxyBadDHCPPkt.setStatus(_A)
_MobilityProxyNotDHCP_Type=Counter32
_MobilityProxyNotDHCP_Object=MibScalar
mobilityProxyNotDHCP=_MobilityProxyNotDHCP_Object((1,3,6,1,4,1,14823,2,2,1,9,3,7),_MobilityProxyNotDHCP_Type())
mobilityProxyNotDHCP.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityProxyNotDHCP.setStatus(_A)
_MobilityProxyDHCPNoHomeVlan_Type=Counter32
_MobilityProxyDHCPNoHomeVlan_Object=MibScalar
mobilityProxyDHCPNoHomeVlan=_MobilityProxyDHCPNoHomeVlan_Object((1,3,6,1,4,1,14823,2,2,1,9,3,8),_MobilityProxyDHCPNoHomeVlan_Type())
mobilityProxyDHCPNoHomeVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityProxyDHCPNoHomeVlan.setStatus(_A)
_MobilityProxyDHCPUnexpFrame_Type=Counter32
_MobilityProxyDHCPUnexpFrame_Object=MibScalar
mobilityProxyDHCPUnexpFrame=_MobilityProxyDHCPUnexpFrame_Object((1,3,6,1,4,1,14823,2,2,1,9,3,9),_MobilityProxyDHCPUnexpFrame_Type())
mobilityProxyDHCPUnexpFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityProxyDHCPUnexpFrame.setStatus(_A)
_MobilityProxyDHCPUnexpRemote_Type=Counter32
_MobilityProxyDHCPUnexpRemote_Object=MibScalar
mobilityProxyDHCPUnexpRemote=_MobilityProxyDHCPUnexpRemote_Object((1,3,6,1,4,1,14823,2,2,1,9,3,10),_MobilityProxyDHCPUnexpRemote_Type())
mobilityProxyDHCPUnexpRemote.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityProxyDHCPUnexpRemote.setStatus(_A)
_WlsxMobilityHAStatsGroup_ObjectIdentity=ObjectIdentity
wlsxMobilityHAStatsGroup=_WlsxMobilityHAStatsGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,9,4))
_MobilityHARxRRQ_Type=Counter32
_MobilityHARxRRQ_Object=MibScalar
mobilityHARxRRQ=_MobilityHARxRRQ_Object((1,3,6,1,4,1,14823,2,2,1,9,4,1),_MobilityHARxRRQ_Type())
mobilityHARxRRQ.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityHARxRRQ.setStatus(_A)
_MobilityHASentRRP_Type=Counter32
_MobilityHASentRRP_Object=MibScalar
mobilityHASentRRP=_MobilityHASentRRP_Object((1,3,6,1,4,1,14823,2,2,1,9,4,2),_MobilityHASentRRP_Type())
mobilityHASentRRP.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityHASentRRP.setStatus(_A)
_MobilityHARRQAccept_Type=Counter32
_MobilityHARRQAccept_Object=MibScalar
mobilityHARRQAccept=_MobilityHARRQAccept_Object((1,3,6,1,4,1,14823,2,2,1,9,4,3),_MobilityHARRQAccept_Type())
mobilityHARRQAccept.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityHARRQAccept.setStatus(_A)
_MobilityHARRQDenied_Type=Counter32
_MobilityHARRQDenied_Object=MibScalar
mobilityHARRQDenied=_MobilityHARRQDenied_Object((1,3,6,1,4,1,14823,2,2,1,9,4,4),_MobilityHARRQDenied_Type())
mobilityHARRQDenied.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityHARRQDenied.setStatus(_A)
_MobilityHARRQIgnore_Type=Counter32
_MobilityHARRQIgnore_Object=MibScalar
mobilityHARRQIgnore=_MobilityHARRQIgnore_Object((1,3,6,1,4,1,14823,2,2,1,9,4,5),_MobilityHARRQIgnore_Type())
mobilityHARRQIgnore.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityHARRQIgnore.setStatus(_A)
_MobilityHARRQAdminDeny_Type=Counter32
_MobilityHARRQAdminDeny_Object=MibScalar
mobilityHARRQAdminDeny=_MobilityHARRQAdminDeny_Object((1,3,6,1,4,1,14823,2,2,1,9,4,6),_MobilityHARRQAdminDeny_Type())
mobilityHARRQAdminDeny.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityHARRQAdminDeny.setStatus(_A)
_MobilityHARRQNoResource_Type=Counter32
_MobilityHARRQNoResource_Object=MibScalar
mobilityHARRQNoResource=_MobilityHARRQNoResource_Object((1,3,6,1,4,1,14823,2,2,1,9,4,7),_MobilityHARRQNoResource_Type())
mobilityHARRQNoResource.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityHARRQNoResource.setStatus(_A)
_MobilityHAMNauthFail_Type=Counter32
_MobilityHAMNauthFail_Object=MibScalar
mobilityHAMNauthFail=_MobilityHAMNauthFail_Object((1,3,6,1,4,1,14823,2,2,1,9,4,8),_MobilityHAMNauthFail_Type())
mobilityHAMNauthFail.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityHAMNauthFail.setStatus(_A)
_MobilityHAFAauthFail_Type=Counter32
_MobilityHAFAauthFail_Object=MibScalar
mobilityHAFAauthFail=_MobilityHAFAauthFail_Object((1,3,6,1,4,1,14823,2,2,1,9,4,9),_MobilityHAFAauthFail_Type())
mobilityHAFAauthFail.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityHAFAauthFail.setStatus(_A)
_MobilityHABadID_Type=Counter32
_MobilityHABadID_Object=MibScalar
mobilityHABadID=_MobilityHABadID_Object((1,3,6,1,4,1,14823,2,2,1,9,4,10),_MobilityHABadID_Type())
mobilityHABadID.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityHABadID.setStatus(_A)
_MobilityHAMalform_Type=Counter32
_MobilityHAMalform_Object=MibScalar
mobilityHAMalform=_MobilityHAMalform_Object((1,3,6,1,4,1,14823,2,2,1,9,4,11),_MobilityHAMalform_Type())
mobilityHAMalform.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityHAMalform.setStatus(_A)
_MobilityHATooManyBnd_Type=Counter32
_MobilityHATooManyBnd_Object=MibScalar
mobilityHATooManyBnd=_MobilityHATooManyBnd_Object((1,3,6,1,4,1,14823,2,2,1,9,4,12),_MobilityHATooManyBnd_Type())
mobilityHATooManyBnd.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityHATooManyBnd.setStatus(_A)
_MobilityHABndExpire_Type=Counter32
_MobilityHABndExpire_Object=MibScalar
mobilityHABndExpire=_MobilityHABndExpire_Object((1,3,6,1,4,1,14823,2,2,1,9,4,13),_MobilityHABndExpire_Type())
mobilityHABndExpire.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityHABndExpire.setStatus(_A)
_WlsxMobilityFAStatsGroup_ObjectIdentity=ObjectIdentity
wlsxMobilityFAStatsGroup=_WlsxMobilityFAStatsGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,9,5))
_MobilityFASentRRQ_Type=Counter32
_MobilityFASentRRQ_Object=MibScalar
mobilityFASentRRQ=_MobilityFASentRRQ_Object((1,3,6,1,4,1,14823,2,2,1,9,5,1),_MobilityFASentRRQ_Type())
mobilityFASentRRQ.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityFASentRRQ.setStatus(_A)
_MobilityFARcvRRP_Type=Counter32
_MobilityFARcvRRP_Object=MibScalar
mobilityFARcvRRP=_MobilityFARcvRRP_Object((1,3,6,1,4,1,14823,2,2,1,9,5,2),_MobilityFARcvRRP_Type())
mobilityFARcvRRP.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityFARcvRRP.setStatus(_A)
_MobilityFARRQAccept_Type=Counter32
_MobilityFARRQAccept_Object=MibScalar
mobilityFARRQAccept=_MobilityFARRQAccept_Object((1,3,6,1,4,1,14823,2,2,1,9,5,3),_MobilityFARRQAccept_Type())
mobilityFARRQAccept.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityFARRQAccept.setStatus(_A)
_MobilityFARRQReject_Type=Counter32
_MobilityFARRQReject_Object=MibScalar
mobilityFARRQReject=_MobilityFARRQReject_Object((1,3,6,1,4,1,14823,2,2,1,9,5,4),_MobilityFARRQReject_Type())
mobilityFARRQReject.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityFARRQReject.setStatus(_A)
_MobilityMNHAauthFAIL_Type=Counter32
_MobilityMNHAauthFAIL_Object=MibScalar
mobilityMNHAauthFAIL=_MobilityMNHAauthFAIL_Object((1,3,6,1,4,1,14823,2,2,1,9,5,5),_MobilityMNHAauthFAIL_Type())
mobilityMNHAauthFAIL.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityMNHAauthFAIL.setStatus(_A)
_MobilityFAHAauthFAIL_Type=Counter32
_MobilityFAHAauthFAIL_Object=MibScalar
mobilityFAHAauthFAIL=_MobilityFAHAauthFAIL_Object((1,3,6,1,4,1,14823,2,2,1,9,5,6),_MobilityFAHAauthFAIL_Type())
mobilityFAHAauthFAIL.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityFAHAauthFAIL.setStatus(_A)
_MobilityFABadID_Type=Counter32
_MobilityFABadID_Object=MibScalar
mobilityFABadID=_MobilityFABadID_Object((1,3,6,1,4,1,14823,2,2,1,9,5,7),_MobilityFABadID_Type())
mobilityFABadID.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityFABadID.setStatus(_A)
_MobilityFAMalform_Type=Counter32
_MobilityFAMalform_Object=MibScalar
mobilityFAMalform=_MobilityFAMalform_Object((1,3,6,1,4,1,14823,2,2,1,9,5,8),_MobilityFAMalform_Type())
mobilityFAMalform.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityFAMalform.setStatus(_A)
_WlsxMobilityHAFARevocationStatsGroup_ObjectIdentity=ObjectIdentity
wlsxMobilityHAFARevocationStatsGroup=_WlsxMobilityHAFARevocationStatsGroup_ObjectIdentity((1,3,6,1,4,1,14823,2,2,1,9,6))
_MobilitySentRRVRQ_Type=Counter32
_MobilitySentRRVRQ_Object=MibScalar
mobilitySentRRVRQ=_MobilitySentRRVRQ_Object((1,3,6,1,4,1,14823,2,2,1,9,6,1),_MobilitySentRRVRQ_Type())
mobilitySentRRVRQ.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilitySentRRVRQ.setStatus(_A)
_MobilityRcvRRVAck_Type=Counter32
_MobilityRcvRRVAck_Object=MibScalar
mobilityRcvRRVAck=_MobilityRcvRRVAck_Object((1,3,6,1,4,1,14823,2,2,1,9,6,2),_MobilityRcvRRVAck_Type())
mobilityRcvRRVAck.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityRcvRRVAck.setStatus(_A)
_MobilityRcvRRV_Type=Counter32
_MobilityRcvRRV_Object=MibScalar
mobilityRcvRRV=_MobilityRcvRRV_Object((1,3,6,1,4,1,14823,2,2,1,9,6,3),_MobilityRcvRRV_Type())
mobilityRcvRRV.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityRcvRRV.setStatus(_A)
_MobilitySentRRVAck_Type=Counter32
_MobilitySentRRVAck_Object=MibScalar
mobilitySentRRVAck=_MobilitySentRRVAck_Object((1,3,6,1,4,1,14823,2,2,1,9,6,4),_MobilitySentRRVAck_Type())
mobilitySentRRVAck.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilitySentRRVAck.setStatus(_A)
_MobilityRRVRQIgnore_Type=Counter32
_MobilityRRVRQIgnore_Object=MibScalar
mobilityRRVRQIgnore=_MobilityRRVRQIgnore_Object((1,3,6,1,4,1,14823,2,2,1,9,6,5),_MobilityRRVRQIgnore_Type())
mobilityRRVRQIgnore.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityRRVRQIgnore.setStatus(_A)
_MobilityRRVAckIgnore_Type=Counter32
_MobilityRRVAckIgnore_Object=MibScalar
mobilityRRVAckIgnore=_MobilityRRVAckIgnore_Object((1,3,6,1,4,1,14823,2,2,1,9,6,6),_MobilityRRVAckIgnore_Type())
mobilityRRVAckIgnore.setMaxAccess(_B)
if mibBuilder.loadTexts:mobilityRRVAckIgnore.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'wlsxMobilityMIB':wlsxMobilityMIB,'wlsxMobilityConfigGroup':wlsxMobilityConfigGroup,'wlsxMobilityDomainTable':wlsxMobilityDomainTable,'wlsxMobilityDomainEntry':wlsxMobilityDomainEntry,_E:mobilityDomainName,'mobilityDomainIsExclusive':mobilityDomainIsExclusive,'mobilityDomainStatus':mobilityDomainStatus,'wlsxMobilityHomeAgentTable':wlsxMobilityHomeAgentTable,'wlsxMobilityHomeAgentEntry':wlsxMobilityHomeAgentEntry,_F:mobilityHomeAgentSubnet,_G:mobilityHomeAgentMask,_H:mobilityHomeAgentIp,'mobilityHomeAgentVlan':mobilityHomeAgentVlan,'wlsxMobilityHostTable':wlsxMobilityHostTable,'wlsxMobilityHostEntry':wlsxMobilityHostEntry,_I:mobilityHostMac,'mobilityHostIp':mobilityHostIp,'mobilityHostStatus':mobilityHostStatus,'mobilityHostServiceTime':mobilityHostServiceTime,'mobilityHostHomeVlan':mobilityHostHomeVlan,'mobilityHostHomeNetwork':mobilityHostHomeNetwork,'mobilityHostHomeMask':mobilityHostHomeMask,'mobilityHostDhcpInfo':mobilityHostDhcpInfo,'wlsxMobilityProxyStatsGroup':wlsxMobilityProxyStatsGroup,'mobilityProxyPktRx':mobilityProxyPktRx,'mobilityProxyPktHandled':mobilityProxyPktHandled,'mobilityProxyPktFwd':mobilityProxyPktFwd,'mobilityProxyPktDrop':mobilityProxyPktDrop,'mobilityProxyBusy':mobilityProxyBusy,'mobilityProxyNoMobility':mobilityProxyNoMobility,'mobilityProxyClientIPChg':mobilityProxyClientIPChg,'mobilityProxyClientEssidChg':mobilityProxyClientEssidChg,'wlsxMobilityProxyDHCPStatsGroup':wlsxMobilityProxyDHCPStatsGroup,'mobilityProxyDhcpBootpRx':mobilityProxyDhcpBootpRx,'mobilityProxyDhcpPktProc':mobilityProxyDhcpPktProc,'mobilityProxyDhcpPktFwd':mobilityProxyDhcpPktFwd,'mobilityProxyDhcpPktDrop':mobilityProxyDhcpPktDrop,'mobilityProxyDHCPNak':mobilityProxyDHCPNak,'mobilityProxyBadDHCPPkt':mobilityProxyBadDHCPPkt,'mobilityProxyNotDHCP':mobilityProxyNotDHCP,'mobilityProxyDHCPNoHomeVlan':mobilityProxyDHCPNoHomeVlan,'mobilityProxyDHCPUnexpFrame':mobilityProxyDHCPUnexpFrame,'mobilityProxyDHCPUnexpRemote':mobilityProxyDHCPUnexpRemote,'wlsxMobilityHAStatsGroup':wlsxMobilityHAStatsGroup,'mobilityHARxRRQ':mobilityHARxRRQ,'mobilityHASentRRP':mobilityHASentRRP,'mobilityHARRQAccept':mobilityHARRQAccept,'mobilityHARRQDenied':mobilityHARRQDenied,'mobilityHARRQIgnore':mobilityHARRQIgnore,'mobilityHARRQAdminDeny':mobilityHARRQAdminDeny,'mobilityHARRQNoResource':mobilityHARRQNoResource,'mobilityHAMNauthFail':mobilityHAMNauthFail,'mobilityHAFAauthFail':mobilityHAFAauthFail,'mobilityHABadID':mobilityHABadID,'mobilityHAMalform':mobilityHAMalform,'mobilityHATooManyBnd':mobilityHATooManyBnd,'mobilityHABndExpire':mobilityHABndExpire,'wlsxMobilityFAStatsGroup':wlsxMobilityFAStatsGroup,'mobilityFASentRRQ':mobilityFASentRRQ,'mobilityFARcvRRP':mobilityFARcvRRP,'mobilityFARRQAccept':mobilityFARRQAccept,'mobilityFARRQReject':mobilityFARRQReject,'mobilityMNHAauthFAIL':mobilityMNHAauthFAIL,'mobilityFAHAauthFAIL':mobilityFAHAauthFAIL,'mobilityFABadID':mobilityFABadID,'mobilityFAMalform':mobilityFAMalform,'wlsxMobilityHAFARevocationStatsGroup':wlsxMobilityHAFARevocationStatsGroup,'mobilitySentRRVRQ':mobilitySentRRVRQ,'mobilityRcvRRVAck':mobilityRcvRRVAck,'mobilityRcvRRV':mobilityRcvRRV,'mobilitySentRRVAck':mobilitySentRRVAck,'mobilityRRVRQIgnore':mobilityRRVRQIgnore,'mobilityRRVAckIgnore':mobilityRRVAckIgnore})