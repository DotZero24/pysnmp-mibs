_L='rcDhcpRelayIndex'
_K='not-accessible'
_J='rcDhcpIpIndex'
_I='EnableVar'
_H='OctetString'
_G='DHCP-SERVER-MIB'
_F='read-write'
_E='Integer32'
_D='mandatory'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
EnableVar,Vlanset=mibBuilder.importSymbols('SWITCH-TC',_I,'Vlanset')
rcDhcpServer=ModuleIdentity((1,3,6,1,4,1,8886,6,1,12))
if mibBuilder.loadTexts:rcDhcpServer.setRevisions(('2004-12-20 00:00',))
_RcDhcpServerMibObjects_ObjectIdentity=ObjectIdentity
rcDhcpServerMibObjects=_RcDhcpServerMibObjects_ObjectIdentity((1,3,6,1,4,1,8886,6,1,12,1))
_RcDhcpDot1dDhcp_ObjectIdentity=ObjectIdentity
rcDhcpDot1dDhcp=_RcDhcpDot1dDhcp_ObjectIdentity((1,3,6,1,4,1,8886,6,1,12,1,1))
class _RcDhcpPropEnable_Type(EnableVar):defaultValue=2
_RcDhcpPropEnable_Type.__name__=_I
_RcDhcpPropEnable_Object=MibScalar
rcDhcpPropEnable=_RcDhcpPropEnable_Object((1,3,6,1,4,1,8886,6,1,12,1,1,1),_RcDhcpPropEnable_Type())
rcDhcpPropEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:rcDhcpPropEnable.setStatus(_A)
_RcDhcpVlanActive_Type=Vlanset
_RcDhcpVlanActive_Object=MibScalar
rcDhcpVlanActive=_RcDhcpVlanActive_Object((1,3,6,1,4,1,8886,6,1,12,1,1,2),_RcDhcpVlanActive_Type())
rcDhcpVlanActive.setMaxAccess(_F)
if mibBuilder.loadTexts:rcDhcpVlanActive.setStatus(_A)
class _RcDhcpIpNextIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_RcDhcpIpNextIndex_Type.__name__=_E
_RcDhcpIpNextIndex_Object=MibScalar
rcDhcpIpNextIndex=_RcDhcpIpNextIndex_Object((1,3,6,1,4,1,8886,6,1,12,1,1,3),_RcDhcpIpNextIndex_Type())
rcDhcpIpNextIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpIpNextIndex.setStatus(_A)
class _RcDhcpMaxLease_Type(Integer32):defaultValue=10080;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,10080))
_RcDhcpMaxLease_Type.__name__=_E
_RcDhcpMaxLease_Object=MibScalar
rcDhcpMaxLease=_RcDhcpMaxLease_Object((1,3,6,1,4,1,8886,6,1,12,1,1,4),_RcDhcpMaxLease_Type())
rcDhcpMaxLease.setMaxAccess(_F)
if mibBuilder.loadTexts:rcDhcpMaxLease.setStatus(_A)
class _RcDhcpMinLease_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,10080))
_RcDhcpMinLease_Type.__name__=_E
_RcDhcpMinLease_Object=MibScalar
rcDhcpMinLease=_RcDhcpMinLease_Object((1,3,6,1,4,1,8886,6,1,12,1,1,5),_RcDhcpMinLease_Type())
rcDhcpMinLease.setMaxAccess(_F)
if mibBuilder.loadTexts:rcDhcpMinLease.setStatus(_A)
class _RcDhcpDefLease_Type(Integer32):defaultValue=30;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,10080))
_RcDhcpDefLease_Type.__name__=_E
_RcDhcpDefLease_Object=MibScalar
rcDhcpDefLease=_RcDhcpDefLease_Object((1,3,6,1,4,1,8886,6,1,12,1,1,6),_RcDhcpDefLease_Type())
rcDhcpDefLease.setMaxAccess(_F)
if mibBuilder.loadTexts:rcDhcpDefLease.setStatus(_A)
_RcDhcpVlanAuth_Type=Vlanset
_RcDhcpVlanAuth_Object=MibScalar
rcDhcpVlanAuth=_RcDhcpVlanAuth_Object((1,3,6,1,4,1,8886,6,1,12,1,1,7),_RcDhcpVlanAuth_Type())
rcDhcpVlanAuth.setMaxAccess(_F)
if mibBuilder.loadTexts:rcDhcpVlanAuth.setStatus(_A)
_RcDhcpServerStartTime_Type=TimeTicks
_RcDhcpServerStartTime_Object=MibScalar
rcDhcpServerStartTime=_RcDhcpServerStartTime_Object((1,3,6,1,4,1,8886,6,1,12,1,1,8),_RcDhcpServerStartTime_Type())
rcDhcpServerStartTime.setMaxAccess(_F)
if mibBuilder.loadTexts:rcDhcpServerStartTime.setStatus(_A)
_RcDhcpIpTable_Object=MibTable
rcDhcpIpTable=_RcDhcpIpTable_Object((1,3,6,1,4,1,8886,6,1,12,1,1,9))
if mibBuilder.loadTexts:rcDhcpIpTable.setStatus(_A)
_RcDhcpIpEntry_Object=MibTableRow
rcDhcpIpEntry=_RcDhcpIpEntry_Object((1,3,6,1,4,1,8886,6,1,12,1,1,9,1))
rcDhcpIpEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:rcDhcpIpEntry.setStatus(_A)
class _RcDhcpIpIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_RcDhcpIpIndex_Type.__name__=_E
_RcDhcpIpIndex_Object=MibTableColumn
rcDhcpIpIndex=_RcDhcpIpIndex_Object((1,3,6,1,4,1,8886,6,1,12,1,1,9,1,1),_RcDhcpIpIndex_Type())
rcDhcpIpIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:rcDhcpIpIndex.setStatus(_A)
class _RcDhcpIpEntryName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,16))
_RcDhcpIpEntryName_Type.__name__=_H
_RcDhcpIpEntryName_Object=MibTableColumn
rcDhcpIpEntryName=_RcDhcpIpEntryName_Object((1,3,6,1,4,1,8886,6,1,12,1,1,9,1,2),_RcDhcpIpEntryName_Type())
rcDhcpIpEntryName.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDhcpIpEntryName.setStatus(_A)
_RcDhcpIpVlanset_Type=Vlanset
_RcDhcpIpVlanset_Object=MibTableColumn
rcDhcpIpVlanset=_RcDhcpIpVlanset_Object((1,3,6,1,4,1,8886,6,1,12,1,1,9,1,3),_RcDhcpIpVlanset_Type())
rcDhcpIpVlanset.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDhcpIpVlanset.setStatus(_A)
_RcDhcpIpStartIp_Type=IpAddress
_RcDhcpIpStartIp_Object=MibTableColumn
rcDhcpIpStartIp=_RcDhcpIpStartIp_Object((1,3,6,1,4,1,8886,6,1,12,1,1,9,1,4),_RcDhcpIpStartIp_Type())
rcDhcpIpStartIp.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDhcpIpStartIp.setStatus(_A)
_RcDhcpIpEndIp_Type=IpAddress
_RcDhcpIpEndIp_Object=MibTableColumn
rcDhcpIpEndIp=_RcDhcpIpEndIp_Object((1,3,6,1,4,1,8886,6,1,12,1,1,9,1,5),_RcDhcpIpEndIp_Type())
rcDhcpIpEndIp.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDhcpIpEndIp.setStatus(_A)
_RcDhcpIpNetmask_Type=IpAddress
_RcDhcpIpNetmask_Object=MibTableColumn
rcDhcpIpNetmask=_RcDhcpIpNetmask_Object((1,3,6,1,4,1,8886,6,1,12,1,1,9,1,6),_RcDhcpIpNetmask_Type())
rcDhcpIpNetmask.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDhcpIpNetmask.setStatus(_A)
_RcDhcpIpGateway_Type=IpAddress
_RcDhcpIpGateway_Object=MibTableColumn
rcDhcpIpGateway=_RcDhcpIpGateway_Object((1,3,6,1,4,1,8886,6,1,12,1,1,9,1,7),_RcDhcpIpGateway_Type())
rcDhcpIpGateway.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDhcpIpGateway.setStatus(_A)
_RcDhcpIpDnsServer_Type=IpAddress
_RcDhcpIpDnsServer_Object=MibTableColumn
rcDhcpIpDnsServer=_RcDhcpIpDnsServer_Object((1,3,6,1,4,1,8886,6,1,12,1,1,9,1,8),_RcDhcpIpDnsServer_Type())
rcDhcpIpDnsServer.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDhcpIpDnsServer.setStatus(_A)
_RcDhcpIpSecondaryDnsServer_Type=IpAddress
_RcDhcpIpSecondaryDnsServer_Object=MibTableColumn
rcDhcpIpSecondaryDnsServer=_RcDhcpIpSecondaryDnsServer_Object((1,3,6,1,4,1,8886,6,1,12,1,1,9,1,9),_RcDhcpIpSecondaryDnsServer_Type())
rcDhcpIpSecondaryDnsServer.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDhcpIpSecondaryDnsServer.setStatus(_A)
_RcDhcpIpRowStatus_Type=RowStatus
_RcDhcpIpRowStatus_Object=MibTableColumn
rcDhcpIpRowStatus=_RcDhcpIpRowStatus_Object((1,3,6,1,4,1,8886,6,1,12,1,1,9,1,10),_RcDhcpIpRowStatus_Type())
rcDhcpIpRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDhcpIpRowStatus.setStatus(_A)
class _RcDhcpRelayNextIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_RcDhcpRelayNextIndex_Type.__name__=_E
_RcDhcpRelayNextIndex_Object=MibScalar
rcDhcpRelayNextIndex=_RcDhcpRelayNextIndex_Object((1,3,6,1,4,1,8886,6,1,12,1,1,10),_RcDhcpRelayNextIndex_Type())
rcDhcpRelayNextIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpRelayNextIndex.setStatus(_A)
_RcDhcpRelayTable_Object=MibTable
rcDhcpRelayTable=_RcDhcpRelayTable_Object((1,3,6,1,4,1,8886,6,1,12,1,1,11))
if mibBuilder.loadTexts:rcDhcpRelayTable.setStatus(_A)
_RcDhcpRelayEntry_Object=MibTableRow
rcDhcpRelayEntry=_RcDhcpRelayEntry_Object((1,3,6,1,4,1,8886,6,1,12,1,1,11,1))
rcDhcpRelayEntry.setIndexNames((0,_G,_L))
if mibBuilder.loadTexts:rcDhcpRelayEntry.setStatus(_A)
_RcDhcpRelayIndex_Type=Integer32
_RcDhcpRelayIndex_Object=MibTableColumn
rcDhcpRelayIndex=_RcDhcpRelayIndex_Object((1,3,6,1,4,1,8886,6,1,12,1,1,11,1,1),_RcDhcpRelayIndex_Type())
rcDhcpRelayIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:rcDhcpRelayIndex.setStatus(_A)
_RcDhcpRelayAddress_Type=IpAddress
_RcDhcpRelayAddress_Object=MibTableColumn
rcDhcpRelayAddress=_RcDhcpRelayAddress_Object((1,3,6,1,4,1,8886,6,1,12,1,1,11,1,2),_RcDhcpRelayAddress_Type())
rcDhcpRelayAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDhcpRelayAddress.setStatus(_A)
_RcDhcpRelayMask_Type=IpAddress
_RcDhcpRelayMask_Object=MibTableColumn
rcDhcpRelayMask=_RcDhcpRelayMask_Object((1,3,6,1,4,1,8886,6,1,12,1,1,11,1,3),_RcDhcpRelayMask_Type())
rcDhcpRelayMask.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDhcpRelayMask.setStatus(_A)
_RcDhcpRelayRowStatus_Type=RowStatus
_RcDhcpRelayRowStatus_Object=MibTableColumn
rcDhcpRelayRowStatus=_RcDhcpRelayRowStatus_Object((1,3,6,1,4,1,8886,6,1,12,1,1,11,1,4),_RcDhcpRelayRowStatus_Type())
rcDhcpRelayRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDhcpRelayRowStatus.setStatus(_A)
_RcDhcpServerStatistics_ObjectIdentity=ObjectIdentity
rcDhcpServerStatistics=_RcDhcpServerStatistics_ObjectIdentity((1,3,6,1,4,1,8886,6,1,12,1,2))
_RcDhcpServerStatsBootps_Type=Counter32
_RcDhcpServerStatsBootps_Object=MibScalar
rcDhcpServerStatsBootps=_RcDhcpServerStatsBootps_Object((1,3,6,1,4,1,8886,6,1,12,1,2,1),_RcDhcpServerStatsBootps_Type())
rcDhcpServerStatsBootps.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpServerStatsBootps.setStatus(_D)
_RcDhcpServerStatsDiscovers_Type=Counter32
_RcDhcpServerStatsDiscovers_Object=MibScalar
rcDhcpServerStatsDiscovers=_RcDhcpServerStatsDiscovers_Object((1,3,6,1,4,1,8886,6,1,12,1,2,2),_RcDhcpServerStatsDiscovers_Type())
rcDhcpServerStatsDiscovers.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpServerStatsDiscovers.setStatus(_D)
_RcDhcpServerStatsRequests_Type=Counter32
_RcDhcpServerStatsRequests_Object=MibScalar
rcDhcpServerStatsRequests=_RcDhcpServerStatsRequests_Object((1,3,6,1,4,1,8886,6,1,12,1,2,3),_RcDhcpServerStatsRequests_Type())
rcDhcpServerStatsRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpServerStatsRequests.setStatus(_D)
_RcDhcpServerStatsReleases_Type=Counter32
_RcDhcpServerStatsReleases_Object=MibScalar
rcDhcpServerStatsReleases=_RcDhcpServerStatsReleases_Object((1,3,6,1,4,1,8886,6,1,12,1,2,4),_RcDhcpServerStatsReleases_Type())
rcDhcpServerStatsReleases.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpServerStatsReleases.setStatus(_D)
_RcDhcpServerStatsOffers_Type=Counter32
_RcDhcpServerStatsOffers_Object=MibScalar
rcDhcpServerStatsOffers=_RcDhcpServerStatsOffers_Object((1,3,6,1,4,1,8886,6,1,12,1,2,5),_RcDhcpServerStatsOffers_Type())
rcDhcpServerStatsOffers.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpServerStatsOffers.setStatus(_D)
_RcDhcpServerStatsAcks_Type=Counter32
_RcDhcpServerStatsAcks_Object=MibScalar
rcDhcpServerStatsAcks=_RcDhcpServerStatsAcks_Object((1,3,6,1,4,1,8886,6,1,12,1,2,6),_RcDhcpServerStatsAcks_Type())
rcDhcpServerStatsAcks.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpServerStatsAcks.setStatus(_D)
_RcDhcpServerStatsNacks_Type=Counter32
_RcDhcpServerStatsNacks_Object=MibScalar
rcDhcpServerStatsNacks=_RcDhcpServerStatsNacks_Object((1,3,6,1,4,1,8886,6,1,12,1,2,7),_RcDhcpServerStatsNacks_Type())
rcDhcpServerStatsNacks.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpServerStatsNacks.setStatus(_D)
_RcDhcpServerStatsDeclines_Type=Counter32
_RcDhcpServerStatsDeclines_Object=MibScalar
rcDhcpServerStatsDeclines=_RcDhcpServerStatsDeclines_Object((1,3,6,1,4,1,8886,6,1,12,1,2,8),_RcDhcpServerStatsDeclines_Type())
rcDhcpServerStatsDeclines.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpServerStatsDeclines.setStatus(_D)
_RcDhcpServerStatsInformations_Type=Counter32
_RcDhcpServerStatsInformations_Object=MibScalar
rcDhcpServerStatsInformations=_RcDhcpServerStatsInformations_Object((1,3,6,1,4,1,8886,6,1,12,1,2,9),_RcDhcpServerStatsInformations_Type())
rcDhcpServerStatsInformations.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpServerStatsInformations.setStatus(_D)
_RcDhcpServerStatsUnknows_Type=Counter32
_RcDhcpServerStatsUnknows_Object=MibScalar
rcDhcpServerStatsUnknows=_RcDhcpServerStatsUnknows_Object((1,3,6,1,4,1,8886,6,1,12,1,2,10),_RcDhcpServerStatsUnknows_Type())
rcDhcpServerStatsUnknows.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpServerStatsUnknows.setStatus(_D)
_RcDhcpServerStatsPackets_Type=Counter32
_RcDhcpServerStatsPackets_Object=MibScalar
rcDhcpServerStatsPackets=_RcDhcpServerStatsPackets_Object((1,3,6,1,4,1,8886,6,1,12,1,2,11),_RcDhcpServerStatsPackets_Type())
rcDhcpServerStatsPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpServerStatsPackets.setStatus(_D)
mibBuilder.exportSymbols(_G,**{'rcDhcpServer':rcDhcpServer,'rcDhcpServerMibObjects':rcDhcpServerMibObjects,'rcDhcpDot1dDhcp':rcDhcpDot1dDhcp,'rcDhcpPropEnable':rcDhcpPropEnable,'rcDhcpVlanActive':rcDhcpVlanActive,'rcDhcpIpNextIndex':rcDhcpIpNextIndex,'rcDhcpMaxLease':rcDhcpMaxLease,'rcDhcpMinLease':rcDhcpMinLease,'rcDhcpDefLease':rcDhcpDefLease,'rcDhcpVlanAuth':rcDhcpVlanAuth,'rcDhcpServerStartTime':rcDhcpServerStartTime,'rcDhcpIpTable':rcDhcpIpTable,'rcDhcpIpEntry':rcDhcpIpEntry,_J:rcDhcpIpIndex,'rcDhcpIpEntryName':rcDhcpIpEntryName,'rcDhcpIpVlanset':rcDhcpIpVlanset,'rcDhcpIpStartIp':rcDhcpIpStartIp,'rcDhcpIpEndIp':rcDhcpIpEndIp,'rcDhcpIpNetmask':rcDhcpIpNetmask,'rcDhcpIpGateway':rcDhcpIpGateway,'rcDhcpIpDnsServer':rcDhcpIpDnsServer,'rcDhcpIpSecondaryDnsServer':rcDhcpIpSecondaryDnsServer,'rcDhcpIpRowStatus':rcDhcpIpRowStatus,'rcDhcpRelayNextIndex':rcDhcpRelayNextIndex,'rcDhcpRelayTable':rcDhcpRelayTable,'rcDhcpRelayEntry':rcDhcpRelayEntry,_L:rcDhcpRelayIndex,'rcDhcpRelayAddress':rcDhcpRelayAddress,'rcDhcpRelayMask':rcDhcpRelayMask,'rcDhcpRelayRowStatus':rcDhcpRelayRowStatus,'rcDhcpServerStatistics':rcDhcpServerStatistics,'rcDhcpServerStatsBootps':rcDhcpServerStatsBootps,'rcDhcpServerStatsDiscovers':rcDhcpServerStatsDiscovers,'rcDhcpServerStatsRequests':rcDhcpServerStatsRequests,'rcDhcpServerStatsReleases':rcDhcpServerStatsReleases,'rcDhcpServerStatsOffers':rcDhcpServerStatsOffers,'rcDhcpServerStatsAcks':rcDhcpServerStatsAcks,'rcDhcpServerStatsNacks':rcDhcpServerStatsNacks,'rcDhcpServerStatsDeclines':rcDhcpServerStatsDeclines,'rcDhcpServerStatsInformations':rcDhcpServerStatsInformations,'rcDhcpServerStatsUnknows':rcDhcpServerStatsUnknows,'rcDhcpServerStatsPackets':rcDhcpServerStatsPackets})