_A9='fsCapwapDhcpRelayIntfConfigGroup'
_A8='fsCapwapDhcpRelayGlobalConfigGroup'
_A7='fsCapwapDhcpServerConfigGroup'
_A6='fsCapwapDhcpMIBGroup'
_A5='fsDhcpServerTlv'
_A4='fsDhcpServerTlvNum'
_A3='fsDhcpClientMacAddress'
_A2='fsDhcpIntfServerRowStatus'
_A1='fsDhcpIntfServerAddress'
_A0='fsDhcpGlobalServerRowStatus'
_z='fsDhcpGlobalServerAddress'
_y='fsDhcpoption138'
_x='fsDhcpoption43'
_w='fsDhcpIPPoolUsage'
_v='fsDhcpScopeRowStatus'
_u='fsDhcpScopeState'
_t='fsDhcpScopeNetbiosNameServerAddress3'
_s='fsDhcpScopeNetbiosNameServerAddress2'
_r='fsDhcpScopeNetbiosNameServerAddress1'
_q='fsDhcpScopeDnsServerAddress3'
_p='fsDhcpScopeDnsServerAddress2'
_o='fsDhcpScopeDnsServerAddress1'
_n='fsDhcpScopeDnsDomainName'
_m='fsDhcpScopeDefaultRouterAddress3'
_l='fsDhcpScopeDefaultRouterAddress2'
_k='fsDhcpScopeDefaultRouterAddress1'
_j='fsDhcpScopeNetmask'
_i='fsDhcpScopeNetwork'
_h='fsDhcpScopeLeaseTime'
_g='fsLDhcpReqSucTimes'
_f='fsLDhcpReqTimes'
_e='fsLDhcpNakPkts'
_d='fsLDhcpAckPkts'
_c='fsLDhcpOfferPkts'
_b='fsLDhcpReplyPkts'
_a='fsLDhcpReleasePkts'
_Z='fsLDhcpInformPkts'
_Y='fsLDhcpDeclinePkts'
_X='fsLDhcpRequestPkts'
_W='fsLDhcpDiscoverPkts'
_V='fsLDhcpStartService'
_U='fsLDhcpClearAllStats'
_T='fsDhcpIntfServerIndex'
_S='fsDhcpGlobalServerIndex'
_R='fsDhcpServerIpVlanIndex'
_Q='fsDhcpScopeIndex'
_P='fsIfIndex'
_O='FS-INTERFACE-MIB'
_N='accessible-for-notify'
_M='enable'
_L='disable'
_K='read-write'
_J='DisplayString'
_I='Unsigned32'
_H='fsDhcpScopeName'
_G='not-accessible'
_F='Integer32'
_E='packets'
_D='read-only'
_C='read-create'
_B='FS-CAPWAP-DHCP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsIfIndex,=mibBuilder.importSymbols(_O,_P)
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_J,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
fsCapwapDhcpMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,58))
if mibBuilder.loadTexts:fsCapwapDhcpMIB.setRevisions(('2009-11-10 00:00',))
_FsCapwapDhcpMIBTrap_ObjectIdentity=ObjectIdentity
fsCapwapDhcpMIBTrap=_FsCapwapDhcpMIBTrap_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,58,0))
_FsCapwapDhcpMIBObjects_ObjectIdentity=ObjectIdentity
fsCapwapDhcpMIBObjects=_FsCapwapDhcpMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,58,1))
_FsCapwapDhcpGlobalConfig_ObjectIdentity=ObjectIdentity
fsCapwapDhcpGlobalConfig=_FsCapwapDhcpGlobalConfig_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,58,1,1))
_FsLDhcpClearAllStats_Type=TruthValue
_FsLDhcpClearAllStats_Object=MibScalar
fsLDhcpClearAllStats=_FsLDhcpClearAllStats_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,1,1),_FsLDhcpClearAllStats_Type())
fsLDhcpClearAllStats.setMaxAccess(_K)
if mibBuilder.loadTexts:fsLDhcpClearAllStats.setStatus(_A)
class _FsLDhcpStartService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_FsLDhcpStartService_Type.__name__=_F
_FsLDhcpStartService_Object=MibScalar
fsLDhcpStartService=_FsLDhcpStartService_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,1,2),_FsLDhcpStartService_Type())
fsLDhcpStartService.setMaxAccess(_K)
if mibBuilder.loadTexts:fsLDhcpStartService.setStatus(_A)
_FsDhcpClientMacAddress_Type=MacAddress
_FsDhcpClientMacAddress_Object=MibScalar
fsDhcpClientMacAddress=_FsDhcpClientMacAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,1,3),_FsDhcpClientMacAddress_Type())
fsDhcpClientMacAddress.setMaxAccess(_N)
if mibBuilder.loadTexts:fsDhcpClientMacAddress.setStatus(_A)
class _FsLDhcpStartTIService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_FsLDhcpStartTIService_Type.__name__=_F
_FsLDhcpStartTIService_Object=MibScalar
fsLDhcpStartTIService=_FsLDhcpStartTIService_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,1,4),_FsLDhcpStartTIService_Type())
fsLDhcpStartTIService.setMaxAccess(_K)
if mibBuilder.loadTexts:fsLDhcpStartTIService.setStatus(_A)
_FsDhcpServerTlvNum_Type=Integer32
_FsDhcpServerTlvNum_Object=MibScalar
fsDhcpServerTlvNum=_FsDhcpServerTlvNum_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,1,5),_FsDhcpServerTlvNum_Type())
fsDhcpServerTlvNum.setMaxAccess(_N)
if mibBuilder.loadTexts:fsDhcpServerTlvNum.setStatus(_A)
_FsDhcpServerTlv_Type=DisplayString
_FsDhcpServerTlv_Object=MibScalar
fsDhcpServerTlv=_FsDhcpServerTlv_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,1,6),_FsDhcpServerTlv_Type())
fsDhcpServerTlv.setMaxAccess(_N)
if mibBuilder.loadTexts:fsDhcpServerTlv.setStatus(_A)
_FsCapwapDhcpShowStats_ObjectIdentity=ObjectIdentity
fsCapwapDhcpShowStats=_FsCapwapDhcpShowStats_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,58,1,2))
_FsLDhcpDiscoverPkts_Type=Unsigned32
_FsLDhcpDiscoverPkts_Object=MibScalar
fsLDhcpDiscoverPkts=_FsLDhcpDiscoverPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,2,1),_FsLDhcpDiscoverPkts_Type())
fsLDhcpDiscoverPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLDhcpDiscoverPkts.setStatus(_A)
if mibBuilder.loadTexts:fsLDhcpDiscoverPkts.setUnits(_E)
_FsLDhcpRequestPkts_Type=Unsigned32
_FsLDhcpRequestPkts_Object=MibScalar
fsLDhcpRequestPkts=_FsLDhcpRequestPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,2,2),_FsLDhcpRequestPkts_Type())
fsLDhcpRequestPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLDhcpRequestPkts.setStatus(_A)
if mibBuilder.loadTexts:fsLDhcpRequestPkts.setUnits(_E)
_FsLDhcpDeclinePkts_Type=Unsigned32
_FsLDhcpDeclinePkts_Object=MibScalar
fsLDhcpDeclinePkts=_FsLDhcpDeclinePkts_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,2,3),_FsLDhcpDeclinePkts_Type())
fsLDhcpDeclinePkts.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLDhcpDeclinePkts.setStatus(_A)
if mibBuilder.loadTexts:fsLDhcpDeclinePkts.setUnits(_E)
_FsLDhcpInformPkts_Type=Unsigned32
_FsLDhcpInformPkts_Object=MibScalar
fsLDhcpInformPkts=_FsLDhcpInformPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,2,4),_FsLDhcpInformPkts_Type())
fsLDhcpInformPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLDhcpInformPkts.setStatus(_A)
if mibBuilder.loadTexts:fsLDhcpInformPkts.setUnits(_E)
_FsLDhcpReleasePkts_Type=Unsigned32
_FsLDhcpReleasePkts_Object=MibScalar
fsLDhcpReleasePkts=_FsLDhcpReleasePkts_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,2,5),_FsLDhcpReleasePkts_Type())
fsLDhcpReleasePkts.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLDhcpReleasePkts.setStatus(_A)
if mibBuilder.loadTexts:fsLDhcpReleasePkts.setUnits(_E)
_FsLDhcpReplyPkts_Type=Unsigned32
_FsLDhcpReplyPkts_Object=MibScalar
fsLDhcpReplyPkts=_FsLDhcpReplyPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,2,6),_FsLDhcpReplyPkts_Type())
fsLDhcpReplyPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLDhcpReplyPkts.setStatus(_A)
if mibBuilder.loadTexts:fsLDhcpReplyPkts.setUnits(_E)
_FsLDhcpOfferPkts_Type=Unsigned32
_FsLDhcpOfferPkts_Object=MibScalar
fsLDhcpOfferPkts=_FsLDhcpOfferPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,2,7),_FsLDhcpOfferPkts_Type())
fsLDhcpOfferPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLDhcpOfferPkts.setStatus(_A)
if mibBuilder.loadTexts:fsLDhcpOfferPkts.setUnits(_E)
_FsLDhcpAckPkts_Type=Unsigned32
_FsLDhcpAckPkts_Object=MibScalar
fsLDhcpAckPkts=_FsLDhcpAckPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,2,8),_FsLDhcpAckPkts_Type())
fsLDhcpAckPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLDhcpAckPkts.setStatus(_A)
if mibBuilder.loadTexts:fsLDhcpAckPkts.setUnits(_E)
_FsLDhcpNakPkts_Type=Unsigned32
_FsLDhcpNakPkts_Object=MibScalar
fsLDhcpNakPkts=_FsLDhcpNakPkts_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,2,9),_FsLDhcpNakPkts_Type())
fsLDhcpNakPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLDhcpNakPkts.setStatus(_A)
if mibBuilder.loadTexts:fsLDhcpNakPkts.setUnits(_E)
_FsLDhcpReqTimes_Type=Unsigned32
_FsLDhcpReqTimes_Object=MibScalar
fsLDhcpReqTimes=_FsLDhcpReqTimes_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,2,10),_FsLDhcpReqTimes_Type())
fsLDhcpReqTimes.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLDhcpReqTimes.setStatus(_A)
if mibBuilder.loadTexts:fsLDhcpReqTimes.setUnits(_E)
_FsLDhcpReqSucTimes_Type=Unsigned32
_FsLDhcpReqSucTimes_Object=MibScalar
fsLDhcpReqSucTimes=_FsLDhcpReqSucTimes_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,2,11),_FsLDhcpReqSucTimes_Type())
fsLDhcpReqSucTimes.setMaxAccess(_D)
if mibBuilder.loadTexts:fsLDhcpReqSucTimes.setStatus(_A)
if mibBuilder.loadTexts:fsLDhcpReqSucTimes.setUnits(_E)
_FsCapwapDhcpServerConfig_ObjectIdentity=ObjectIdentity
fsCapwapDhcpServerConfig=_FsCapwapDhcpServerConfig_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,58,1,3))
_FsDhcpScopeTable_Object=MibTable
fsDhcpScopeTable=_FsDhcpScopeTable_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1))
if mibBuilder.loadTexts:fsDhcpScopeTable.setStatus(_A)
_FsDhcpScopeEntry_Object=MibTableRow
fsDhcpScopeEntry=_FsDhcpScopeEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1))
fsDhcpScopeEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:fsDhcpScopeEntry.setStatus(_A)
class _FsDhcpScopeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_FsDhcpScopeIndex_Type.__name__=_I
_FsDhcpScopeIndex_Object=MibTableColumn
fsDhcpScopeIndex=_FsDhcpScopeIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,1),_FsDhcpScopeIndex_Type())
fsDhcpScopeIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fsDhcpScopeIndex.setStatus(_A)
class _FsDhcpScopeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_FsDhcpScopeName_Type.__name__=_J
_FsDhcpScopeName_Object=MibTableColumn
fsDhcpScopeName=_FsDhcpScopeName_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,2),_FsDhcpScopeName_Type())
fsDhcpScopeName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpScopeName.setStatus(_A)
class _FsDhcpScopeLeaseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(120,8640000))
_FsDhcpScopeLeaseTime_Type.__name__=_F
_FsDhcpScopeLeaseTime_Object=MibTableColumn
fsDhcpScopeLeaseTime=_FsDhcpScopeLeaseTime_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,3),_FsDhcpScopeLeaseTime_Type())
fsDhcpScopeLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpScopeLeaseTime.setStatus(_A)
_FsDhcpScopeNetwork_Type=IpAddress
_FsDhcpScopeNetwork_Object=MibTableColumn
fsDhcpScopeNetwork=_FsDhcpScopeNetwork_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,4),_FsDhcpScopeNetwork_Type())
fsDhcpScopeNetwork.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpScopeNetwork.setStatus(_A)
_FsDhcpScopeNetmask_Type=IpAddress
_FsDhcpScopeNetmask_Object=MibTableColumn
fsDhcpScopeNetmask=_FsDhcpScopeNetmask_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,5),_FsDhcpScopeNetmask_Type())
fsDhcpScopeNetmask.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpScopeNetmask.setStatus(_A)
_FsDhcpScopePoolStartAddress_Type=IpAddress
_FsDhcpScopePoolStartAddress_Object=MibTableColumn
fsDhcpScopePoolStartAddress=_FsDhcpScopePoolStartAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,6),_FsDhcpScopePoolStartAddress_Type())
fsDhcpScopePoolStartAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpScopePoolStartAddress.setStatus(_A)
_FsDhcpScopePoolEndAddress_Type=IpAddress
_FsDhcpScopePoolEndAddress_Object=MibTableColumn
fsDhcpScopePoolEndAddress=_FsDhcpScopePoolEndAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,7),_FsDhcpScopePoolEndAddress_Type())
fsDhcpScopePoolEndAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpScopePoolEndAddress.setStatus(_A)
_FsDhcpScopeDefaultRouterAddress1_Type=IpAddress
_FsDhcpScopeDefaultRouterAddress1_Object=MibTableColumn
fsDhcpScopeDefaultRouterAddress1=_FsDhcpScopeDefaultRouterAddress1_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,8),_FsDhcpScopeDefaultRouterAddress1_Type())
fsDhcpScopeDefaultRouterAddress1.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpScopeDefaultRouterAddress1.setStatus(_A)
_FsDhcpScopeDefaultRouterAddress2_Type=IpAddress
_FsDhcpScopeDefaultRouterAddress2_Object=MibTableColumn
fsDhcpScopeDefaultRouterAddress2=_FsDhcpScopeDefaultRouterAddress2_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,9),_FsDhcpScopeDefaultRouterAddress2_Type())
fsDhcpScopeDefaultRouterAddress2.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpScopeDefaultRouterAddress2.setStatus(_A)
_FsDhcpScopeDefaultRouterAddress3_Type=IpAddress
_FsDhcpScopeDefaultRouterAddress3_Object=MibTableColumn
fsDhcpScopeDefaultRouterAddress3=_FsDhcpScopeDefaultRouterAddress3_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,10),_FsDhcpScopeDefaultRouterAddress3_Type())
fsDhcpScopeDefaultRouterAddress3.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpScopeDefaultRouterAddress3.setStatus(_A)
class _FsDhcpScopeDnsDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_FsDhcpScopeDnsDomainName_Type.__name__=_J
_FsDhcpScopeDnsDomainName_Object=MibTableColumn
fsDhcpScopeDnsDomainName=_FsDhcpScopeDnsDomainName_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,11),_FsDhcpScopeDnsDomainName_Type())
fsDhcpScopeDnsDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpScopeDnsDomainName.setStatus(_A)
_FsDhcpScopeDnsServerAddress1_Type=IpAddress
_FsDhcpScopeDnsServerAddress1_Object=MibTableColumn
fsDhcpScopeDnsServerAddress1=_FsDhcpScopeDnsServerAddress1_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,12),_FsDhcpScopeDnsServerAddress1_Type())
fsDhcpScopeDnsServerAddress1.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpScopeDnsServerAddress1.setStatus(_A)
_FsDhcpScopeDnsServerAddress2_Type=IpAddress
_FsDhcpScopeDnsServerAddress2_Object=MibTableColumn
fsDhcpScopeDnsServerAddress2=_FsDhcpScopeDnsServerAddress2_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,13),_FsDhcpScopeDnsServerAddress2_Type())
fsDhcpScopeDnsServerAddress2.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpScopeDnsServerAddress2.setStatus(_A)
_FsDhcpScopeDnsServerAddress3_Type=IpAddress
_FsDhcpScopeDnsServerAddress3_Object=MibTableColumn
fsDhcpScopeDnsServerAddress3=_FsDhcpScopeDnsServerAddress3_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,14),_FsDhcpScopeDnsServerAddress3_Type())
fsDhcpScopeDnsServerAddress3.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpScopeDnsServerAddress3.setStatus(_A)
_FsDhcpScopeNetbiosNameServerAddress1_Type=IpAddress
_FsDhcpScopeNetbiosNameServerAddress1_Object=MibTableColumn
fsDhcpScopeNetbiosNameServerAddress1=_FsDhcpScopeNetbiosNameServerAddress1_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,15),_FsDhcpScopeNetbiosNameServerAddress1_Type())
fsDhcpScopeNetbiosNameServerAddress1.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpScopeNetbiosNameServerAddress1.setStatus(_A)
_FsDhcpScopeNetbiosNameServerAddress2_Type=IpAddress
_FsDhcpScopeNetbiosNameServerAddress2_Object=MibTableColumn
fsDhcpScopeNetbiosNameServerAddress2=_FsDhcpScopeNetbiosNameServerAddress2_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,16),_FsDhcpScopeNetbiosNameServerAddress2_Type())
fsDhcpScopeNetbiosNameServerAddress2.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpScopeNetbiosNameServerAddress2.setStatus(_A)
_FsDhcpScopeNetbiosNameServerAddress3_Type=IpAddress
_FsDhcpScopeNetbiosNameServerAddress3_Object=MibTableColumn
fsDhcpScopeNetbiosNameServerAddress3=_FsDhcpScopeNetbiosNameServerAddress3_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,17),_FsDhcpScopeNetbiosNameServerAddress3_Type())
fsDhcpScopeNetbiosNameServerAddress3.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpScopeNetbiosNameServerAddress3.setStatus(_A)
class _FsDhcpScopeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_L,0),(_M,1)))
_FsDhcpScopeState_Type.__name__=_F
_FsDhcpScopeState_Object=MibTableColumn
fsDhcpScopeState=_FsDhcpScopeState_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,18),_FsDhcpScopeState_Type())
fsDhcpScopeState.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpScopeState.setStatus(_A)
_FsDhcpScopeRowStatus_Type=RowStatus
_FsDhcpScopeRowStatus_Object=MibTableColumn
fsDhcpScopeRowStatus=_FsDhcpScopeRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,19),_FsDhcpScopeRowStatus_Type())
fsDhcpScopeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpScopeRowStatus.setStatus(_A)
class _FsDhcpIPPoolUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_FsDhcpIPPoolUsage_Type.__name__=_F
_FsDhcpIPPoolUsage_Object=MibTableColumn
fsDhcpIPPoolUsage=_FsDhcpIPPoolUsage_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,20),_FsDhcpIPPoolUsage_Type())
fsDhcpIPPoolUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpIPPoolUsage.setStatus(_A)
_FsDhcpoption43_Type=IpAddress
_FsDhcpoption43_Object=MibTableColumn
fsDhcpoption43=_FsDhcpoption43_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,21),_FsDhcpoption43_Type())
fsDhcpoption43.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpoption43.setStatus(_A)
_FsDhcpoption138_Type=IpAddress
_FsDhcpoption138_Object=MibTableColumn
fsDhcpoption138=_FsDhcpoption138_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,22),_FsDhcpoption138_Type())
fsDhcpoption138.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpoption138.setStatus(_A)
_FsDhcpReqtimes_Type=Unsigned32
_FsDhcpReqtimes_Object=MibTableColumn
fsDhcpReqtimes=_FsDhcpReqtimes_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,23),_FsDhcpReqtimes_Type())
fsDhcpReqtimes.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcpReqtimes.setStatus(_A)
_FsDhcpReqSuctimes_Type=Unsigned32
_FsDhcpReqSuctimes_Object=MibTableColumn
fsDhcpReqSuctimes=_FsDhcpReqSuctimes_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,24),_FsDhcpReqSuctimes_Type())
fsDhcpReqSuctimes.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcpReqSuctimes.setStatus(_A)
_FsDhcpTotalIPNum_Type=Integer32
_FsDhcpTotalIPNum_Object=MibTableColumn
fsDhcpTotalIPNum=_FsDhcpTotalIPNum_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,25),_FsDhcpTotalIPNum_Type())
fsDhcpTotalIPNum.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcpTotalIPNum.setStatus(_A)
_FsDhcpCurrentUsedIPNum_Type=Integer32
_FsDhcpCurrentUsedIPNum_Object=MibTableColumn
fsDhcpCurrentUsedIPNum=_FsDhcpCurrentUsedIPNum_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,26),_FsDhcpCurrentUsedIPNum_Type())
fsDhcpCurrentUsedIPNum.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcpCurrentUsedIPNum.setStatus(_A)
_FsDhcpOffertimes_Type=Unsigned32
_FsDhcpOffertimes_Object=MibTableColumn
fsDhcpOffertimes=_FsDhcpOffertimes_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,27),_FsDhcpOffertimes_Type())
fsDhcpOffertimes.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcpOffertimes.setStatus(_A)
_FsDhcpAcktimes_Type=Unsigned32
_FsDhcpAcktimes_Object=MibTableColumn
fsDhcpAcktimes=_FsDhcpAcktimes_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,1,1,28),_FsDhcpAcktimes_Type())
fsDhcpAcktimes.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcpAcktimes.setStatus(_A)
_FsDhcpServerIpVlanTable_Object=MibTable
fsDhcpServerIpVlanTable=_FsDhcpServerIpVlanTable_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,2))
if mibBuilder.loadTexts:fsDhcpServerIpVlanTable.setStatus(_A)
_FsDhcpServerIpVlanEntry_Object=MibTableRow
fsDhcpServerIpVlanEntry=_FsDhcpServerIpVlanEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,2,1))
fsDhcpServerIpVlanEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:fsDhcpServerIpVlanEntry.setStatus(_A)
class _FsDhcpServerIpVlanIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsDhcpServerIpVlanIndex_Type.__name__=_I
_FsDhcpServerIpVlanIndex_Object=MibTableColumn
fsDhcpServerIpVlanIndex=_FsDhcpServerIpVlanIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,2,1,1),_FsDhcpServerIpVlanIndex_Type())
fsDhcpServerIpVlanIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fsDhcpServerIpVlanIndex.setStatus(_A)
_FsDhcpServerIpVlanOnlineUserNum_Type=Unsigned32
_FsDhcpServerIpVlanOnlineUserNum_Object=MibTableColumn
fsDhcpServerIpVlanOnlineUserNum=_FsDhcpServerIpVlanOnlineUserNum_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,3,2,1,2),_FsDhcpServerIpVlanOnlineUserNum_Type())
fsDhcpServerIpVlanOnlineUserNum.setMaxAccess(_D)
if mibBuilder.loadTexts:fsDhcpServerIpVlanOnlineUserNum.setStatus(_A)
_FsCapwapDhcpRelayConfig_ObjectIdentity=ObjectIdentity
fsCapwapDhcpRelayConfig=_FsCapwapDhcpRelayConfig_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,58,1,4))
_FsDhcpGlobalServerAddrTable_Object=MibTable
fsDhcpGlobalServerAddrTable=_FsDhcpGlobalServerAddrTable_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,4,1))
if mibBuilder.loadTexts:fsDhcpGlobalServerAddrTable.setStatus(_A)
_FsDhcpGlobalServerAddrEntry_Object=MibTableRow
fsDhcpGlobalServerAddrEntry=_FsDhcpGlobalServerAddrEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,4,1,1))
fsDhcpGlobalServerAddrEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:fsDhcpGlobalServerAddrEntry.setStatus(_A)
class _FsDhcpGlobalServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_FsDhcpGlobalServerIndex_Type.__name__=_F
_FsDhcpGlobalServerIndex_Object=MibTableColumn
fsDhcpGlobalServerIndex=_FsDhcpGlobalServerIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,4,1,1,1),_FsDhcpGlobalServerIndex_Type())
fsDhcpGlobalServerIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fsDhcpGlobalServerIndex.setStatus(_A)
_FsDhcpGlobalServerAddress_Type=IpAddress
_FsDhcpGlobalServerAddress_Object=MibTableColumn
fsDhcpGlobalServerAddress=_FsDhcpGlobalServerAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,4,1,1,2),_FsDhcpGlobalServerAddress_Type())
fsDhcpGlobalServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpGlobalServerAddress.setStatus(_A)
_FsDhcpGlobalServerRowStatus_Type=RowStatus
_FsDhcpGlobalServerRowStatus_Object=MibTableColumn
fsDhcpGlobalServerRowStatus=_FsDhcpGlobalServerRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,4,1,1,3),_FsDhcpGlobalServerRowStatus_Type())
fsDhcpGlobalServerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpGlobalServerRowStatus.setStatus(_A)
_FsDhcpIntfServerAddrTable_Object=MibTable
fsDhcpIntfServerAddrTable=_FsDhcpIntfServerAddrTable_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,4,2))
if mibBuilder.loadTexts:fsDhcpIntfServerAddrTable.setStatus(_A)
_FsDhcpIntfServerAddrEntry_Object=MibTableRow
fsDhcpIntfServerAddrEntry=_FsDhcpIntfServerAddrEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,4,2,1))
fsDhcpIntfServerAddrEntry.setIndexNames((0,_O,_P),(0,_B,_T))
if mibBuilder.loadTexts:fsDhcpIntfServerAddrEntry.setStatus(_A)
class _FsDhcpIntfServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_FsDhcpIntfServerIndex_Type.__name__=_F
_FsDhcpIntfServerIndex_Object=MibTableColumn
fsDhcpIntfServerIndex=_FsDhcpIntfServerIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,4,2,1,1),_FsDhcpIntfServerIndex_Type())
fsDhcpIntfServerIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:fsDhcpIntfServerIndex.setStatus(_A)
_FsDhcpIntfServerAddress_Type=IpAddress
_FsDhcpIntfServerAddress_Object=MibTableColumn
fsDhcpIntfServerAddress=_FsDhcpIntfServerAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,4,2,1,2),_FsDhcpIntfServerAddress_Type())
fsDhcpIntfServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpIntfServerAddress.setStatus(_A)
_FsDhcpIntfServerRowStatus_Type=RowStatus
_FsDhcpIntfServerRowStatus_Object=MibTableColumn
fsDhcpIntfServerRowStatus=_FsDhcpIntfServerRowStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,58,1,4,2,1,3),_FsDhcpIntfServerRowStatus_Type())
fsDhcpIntfServerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsDhcpIntfServerRowStatus.setStatus(_A)
_FsCapwapDhcpMIBConformance_ObjectIdentity=ObjectIdentity
fsCapwapDhcpMIBConformance=_FsCapwapDhcpMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,58,2))
_FsCapwapDhcpMIBCompliances_ObjectIdentity=ObjectIdentity
fsCapwapDhcpMIBCompliances=_FsCapwapDhcpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,58,2,1))
_FsCapwapDhcpMIBGroups_ObjectIdentity=ObjectIdentity
fsCapwapDhcpMIBGroups=_FsCapwapDhcpMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,58,2,2))
fsCapwapDhcpMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,58,2,2,1))
fsCapwapDhcpMIBGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:fsCapwapDhcpMIBGroup.setStatus(_A)
fsCapwapDhcpServerConfigGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,58,2,2,2))
fsCapwapDhcpServerConfigGroup.setObjects(*((_B,_H),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y)))
if mibBuilder.loadTexts:fsCapwapDhcpServerConfigGroup.setStatus(_A)
fsCapwapDhcpRelayGlobalConfigGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,58,2,2,3))
fsCapwapDhcpRelayGlobalConfigGroup.setObjects(*((_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:fsCapwapDhcpRelayGlobalConfigGroup.setStatus(_A)
fsCapwapDhcpRelayIntfConfigGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,58,2,2,4))
fsCapwapDhcpRelayIntfConfigGroup.setObjects(*((_B,_A1),(_B,_A2)))
if mibBuilder.loadTexts:fsCapwapDhcpRelayIntfConfigGroup.setStatus(_A)
fsDhcpAddressExhaustTrap=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,58,0,1))
fsDhcpAddressExhaustTrap.setObjects((_B,_H))
if mibBuilder.loadTexts:fsDhcpAddressExhaustTrap.setStatus(_A)
fsDhcpAddressExhaustRecovTrap=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,58,0,2))
fsDhcpAddressExhaustRecovTrap.setObjects((_B,_H))
if mibBuilder.loadTexts:fsDhcpAddressExhaustRecovTrap.setStatus(_A)
fsDhcpClientFailTrap=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,58,0,3))
fsDhcpClientFailTrap.setObjects((_B,_A3))
if mibBuilder.loadTexts:fsDhcpClientFailTrap.setStatus(_A)
fsDhcpServerInfoTrap=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,58,0,4))
fsDhcpServerInfoTrap.setObjects(*((_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:fsDhcpServerInfoTrap.setStatus(_A)
fsCapwapDhcpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,58,2,1,1))
fsCapwapDhcpMIBCompliance.setObjects(*((_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:fsCapwapDhcpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsCapwapDhcpMIB':fsCapwapDhcpMIB,'fsCapwapDhcpMIBTrap':fsCapwapDhcpMIBTrap,'fsDhcpAddressExhaustTrap':fsDhcpAddressExhaustTrap,'fsDhcpAddressExhaustRecovTrap':fsDhcpAddressExhaustRecovTrap,'fsDhcpClientFailTrap':fsDhcpClientFailTrap,'fsDhcpServerInfoTrap':fsDhcpServerInfoTrap,'fsCapwapDhcpMIBObjects':fsCapwapDhcpMIBObjects,'fsCapwapDhcpGlobalConfig':fsCapwapDhcpGlobalConfig,_U:fsLDhcpClearAllStats,_V:fsLDhcpStartService,_A3:fsDhcpClientMacAddress,'fsLDhcpStartTIService':fsLDhcpStartTIService,_A4:fsDhcpServerTlvNum,_A5:fsDhcpServerTlv,'fsCapwapDhcpShowStats':fsCapwapDhcpShowStats,_W:fsLDhcpDiscoverPkts,_X:fsLDhcpRequestPkts,_Y:fsLDhcpDeclinePkts,_Z:fsLDhcpInformPkts,_a:fsLDhcpReleasePkts,_b:fsLDhcpReplyPkts,_c:fsLDhcpOfferPkts,_d:fsLDhcpAckPkts,_e:fsLDhcpNakPkts,_f:fsLDhcpReqTimes,_g:fsLDhcpReqSucTimes,'fsCapwapDhcpServerConfig':fsCapwapDhcpServerConfig,'fsDhcpScopeTable':fsDhcpScopeTable,'fsDhcpScopeEntry':fsDhcpScopeEntry,_Q:fsDhcpScopeIndex,_H:fsDhcpScopeName,_h:fsDhcpScopeLeaseTime,_i:fsDhcpScopeNetwork,_j:fsDhcpScopeNetmask,'fsDhcpScopePoolStartAddress':fsDhcpScopePoolStartAddress,'fsDhcpScopePoolEndAddress':fsDhcpScopePoolEndAddress,_k:fsDhcpScopeDefaultRouterAddress1,_l:fsDhcpScopeDefaultRouterAddress2,_m:fsDhcpScopeDefaultRouterAddress3,_n:fsDhcpScopeDnsDomainName,_o:fsDhcpScopeDnsServerAddress1,_p:fsDhcpScopeDnsServerAddress2,_q:fsDhcpScopeDnsServerAddress3,_r:fsDhcpScopeNetbiosNameServerAddress1,_s:fsDhcpScopeNetbiosNameServerAddress2,_t:fsDhcpScopeNetbiosNameServerAddress3,_u:fsDhcpScopeState,_v:fsDhcpScopeRowStatus,_w:fsDhcpIPPoolUsage,_x:fsDhcpoption43,_y:fsDhcpoption138,'fsDhcpReqtimes':fsDhcpReqtimes,'fsDhcpReqSuctimes':fsDhcpReqSuctimes,'fsDhcpTotalIPNum':fsDhcpTotalIPNum,'fsDhcpCurrentUsedIPNum':fsDhcpCurrentUsedIPNum,'fsDhcpOffertimes':fsDhcpOffertimes,'fsDhcpAcktimes':fsDhcpAcktimes,'fsDhcpServerIpVlanTable':fsDhcpServerIpVlanTable,'fsDhcpServerIpVlanEntry':fsDhcpServerIpVlanEntry,_R:fsDhcpServerIpVlanIndex,'fsDhcpServerIpVlanOnlineUserNum':fsDhcpServerIpVlanOnlineUserNum,'fsCapwapDhcpRelayConfig':fsCapwapDhcpRelayConfig,'fsDhcpGlobalServerAddrTable':fsDhcpGlobalServerAddrTable,'fsDhcpGlobalServerAddrEntry':fsDhcpGlobalServerAddrEntry,_S:fsDhcpGlobalServerIndex,_z:fsDhcpGlobalServerAddress,_A0:fsDhcpGlobalServerRowStatus,'fsDhcpIntfServerAddrTable':fsDhcpIntfServerAddrTable,'fsDhcpIntfServerAddrEntry':fsDhcpIntfServerAddrEntry,_T:fsDhcpIntfServerIndex,_A1:fsDhcpIntfServerAddress,_A2:fsDhcpIntfServerRowStatus,'fsCapwapDhcpMIBConformance':fsCapwapDhcpMIBConformance,'fsCapwapDhcpMIBCompliances':fsCapwapDhcpMIBCompliances,'fsCapwapDhcpMIBCompliance':fsCapwapDhcpMIBCompliance,'fsCapwapDhcpMIBGroups':fsCapwapDhcpMIBGroups,_A6:fsCapwapDhcpMIBGroup,_A7:fsCapwapDhcpServerConfigGroup,_A8:fsCapwapDhcpRelayGlobalConfigGroup,_A9:fsCapwapDhcpRelayIntfConfigGroup})