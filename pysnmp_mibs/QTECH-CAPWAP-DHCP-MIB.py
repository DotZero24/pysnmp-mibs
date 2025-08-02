_A5='qtechCapwapDhcpRelayIntfConfigGroup'
_A4='qtechCapwapDhcpRelayGlobalConfigGroup'
_A3='qtechCapwapDhcpServerConfigGroup'
_A2='qtechCapwapDhcpMIBGroup'
_A1='qtechDhcpClientMacAddress'
_A0='qtechDhcpIntfServerRowStatus'
_z='qtechDhcpIntfServerAddress'
_y='qtechDhcpGlobalServerRowStatus'
_x='qtechDhcpGlobalServerAddress'
_w='qtechDhcpoption138'
_v='qtechDhcpoption43'
_u='qtechDhcpIPPoolUsage'
_t='qtechDhcpScopeRowStatus'
_s='qtechDhcpScopeState'
_r='qtechDhcpScopeNetbiosNameServerAddress3'
_q='qtechDhcpScopeNetbiosNameServerAddress2'
_p='qtechDhcpScopeNetbiosNameServerAddress1'
_o='qtechDhcpScopeDnsServerAddress3'
_n='qtechDhcpScopeDnsServerAddress2'
_m='qtechDhcpScopeDnsServerAddress1'
_l='qtechDhcpScopeDnsDomainName'
_k='qtechDhcpScopeDefaultRouterAddress3'
_j='qtechDhcpScopeDefaultRouterAddress2'
_i='qtechDhcpScopeDefaultRouterAddress1'
_h='qtechDhcpScopeNetmask'
_g='qtechDhcpScopeNetwork'
_f='qtechDhcpScopeLeaseTime'
_e='qtechLDhcpReqSucTimes'
_d='qtechLDhcpReqTimes'
_c='qtechLDhcpNakPkts'
_b='qtechLDhcpAckPkts'
_a='qtechLDhcpOfferPkts'
_Z='qtechLDhcpReplyPkts'
_Y='qtechLDhcpReleasePkts'
_X='qtechLDhcpInformPkts'
_W='qtechLDhcpDeclinePkts'
_V='qtechLDhcpRequestPkts'
_U='qtechLDhcpDiscoverPkts'
_T='qtechLDhcpStartService'
_S='qtechLDhcpClearAllStats'
_R='qtechDhcpIntfServerIndex'
_Q='qtechDhcpGlobalServerIndex'
_P='qtechDhcpScopeIndex'
_O='Unsigned32'
_N='qtechIfIndex'
_M='QTECH-INTERFACE-MIB'
_L='not-accessible'
_K='enable'
_J='disable'
_I='read-write'
_H='DisplayString'
_G='qtechDhcpScopeName'
_F='Integer32'
_E='packets'
_D='read-only'
_C='read-create'
_B='QTECH-CAPWAP-DHCP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechIfIndex,=mibBuilder.importSymbols(_M,_N)
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_O,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_H,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
qtechCapwapDhcpMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,58))
if mibBuilder.loadTexts:qtechCapwapDhcpMIB.setRevisions(('2009-11-10 00:00',))
_QtechCapwapDhcpMIBTrap_ObjectIdentity=ObjectIdentity
qtechCapwapDhcpMIBTrap=_QtechCapwapDhcpMIBTrap_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,58,0))
_QtechCapwapDhcpMIBObjects_ObjectIdentity=ObjectIdentity
qtechCapwapDhcpMIBObjects=_QtechCapwapDhcpMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,58,1))
_QtechCapwapDhcpGlobalConfig_ObjectIdentity=ObjectIdentity
qtechCapwapDhcpGlobalConfig=_QtechCapwapDhcpGlobalConfig_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,58,1,1))
_QtechLDhcpClearAllStats_Type=TruthValue
_QtechLDhcpClearAllStats_Object=MibScalar
qtechLDhcpClearAllStats=_QtechLDhcpClearAllStats_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,1,1),_QtechLDhcpClearAllStats_Type())
qtechLDhcpClearAllStats.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechLDhcpClearAllStats.setStatus(_A)
class _QtechLDhcpStartService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_QtechLDhcpStartService_Type.__name__=_F
_QtechLDhcpStartService_Object=MibScalar
qtechLDhcpStartService=_QtechLDhcpStartService_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,1,2),_QtechLDhcpStartService_Type())
qtechLDhcpStartService.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechLDhcpStartService.setStatus(_A)
_QtechDhcpClientMacAddress_Type=MacAddress
_QtechDhcpClientMacAddress_Object=MibScalar
qtechDhcpClientMacAddress=_QtechDhcpClientMacAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,1,3),_QtechDhcpClientMacAddress_Type())
qtechDhcpClientMacAddress.setMaxAccess('accessible-for-notify')
if mibBuilder.loadTexts:qtechDhcpClientMacAddress.setStatus(_A)
class _QtechLDhcpStartTIService_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_QtechLDhcpStartTIService_Type.__name__=_F
_QtechLDhcpStartTIService_Object=MibScalar
qtechLDhcpStartTIService=_QtechLDhcpStartTIService_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,1,4),_QtechLDhcpStartTIService_Type())
qtechLDhcpStartTIService.setMaxAccess(_I)
if mibBuilder.loadTexts:qtechLDhcpStartTIService.setStatus(_A)
_QtechCapwapDhcpShowStats_ObjectIdentity=ObjectIdentity
qtechCapwapDhcpShowStats=_QtechCapwapDhcpShowStats_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,58,1,2))
_QtechLDhcpDiscoverPkts_Type=Unsigned32
_QtechLDhcpDiscoverPkts_Object=MibScalar
qtechLDhcpDiscoverPkts=_QtechLDhcpDiscoverPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,2,1),_QtechLDhcpDiscoverPkts_Type())
qtechLDhcpDiscoverPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechLDhcpDiscoverPkts.setStatus(_A)
if mibBuilder.loadTexts:qtechLDhcpDiscoverPkts.setUnits(_E)
_QtechLDhcpRequestPkts_Type=Unsigned32
_QtechLDhcpRequestPkts_Object=MibScalar
qtechLDhcpRequestPkts=_QtechLDhcpRequestPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,2,2),_QtechLDhcpRequestPkts_Type())
qtechLDhcpRequestPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechLDhcpRequestPkts.setStatus(_A)
if mibBuilder.loadTexts:qtechLDhcpRequestPkts.setUnits(_E)
_QtechLDhcpDeclinePkts_Type=Unsigned32
_QtechLDhcpDeclinePkts_Object=MibScalar
qtechLDhcpDeclinePkts=_QtechLDhcpDeclinePkts_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,2,3),_QtechLDhcpDeclinePkts_Type())
qtechLDhcpDeclinePkts.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechLDhcpDeclinePkts.setStatus(_A)
if mibBuilder.loadTexts:qtechLDhcpDeclinePkts.setUnits(_E)
_QtechLDhcpInformPkts_Type=Unsigned32
_QtechLDhcpInformPkts_Object=MibScalar
qtechLDhcpInformPkts=_QtechLDhcpInformPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,2,4),_QtechLDhcpInformPkts_Type())
qtechLDhcpInformPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechLDhcpInformPkts.setStatus(_A)
if mibBuilder.loadTexts:qtechLDhcpInformPkts.setUnits(_E)
_QtechLDhcpReleasePkts_Type=Unsigned32
_QtechLDhcpReleasePkts_Object=MibScalar
qtechLDhcpReleasePkts=_QtechLDhcpReleasePkts_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,2,5),_QtechLDhcpReleasePkts_Type())
qtechLDhcpReleasePkts.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechLDhcpReleasePkts.setStatus(_A)
if mibBuilder.loadTexts:qtechLDhcpReleasePkts.setUnits(_E)
_QtechLDhcpReplyPkts_Type=Unsigned32
_QtechLDhcpReplyPkts_Object=MibScalar
qtechLDhcpReplyPkts=_QtechLDhcpReplyPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,2,6),_QtechLDhcpReplyPkts_Type())
qtechLDhcpReplyPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechLDhcpReplyPkts.setStatus(_A)
if mibBuilder.loadTexts:qtechLDhcpReplyPkts.setUnits(_E)
_QtechLDhcpOfferPkts_Type=Unsigned32
_QtechLDhcpOfferPkts_Object=MibScalar
qtechLDhcpOfferPkts=_QtechLDhcpOfferPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,2,7),_QtechLDhcpOfferPkts_Type())
qtechLDhcpOfferPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechLDhcpOfferPkts.setStatus(_A)
if mibBuilder.loadTexts:qtechLDhcpOfferPkts.setUnits(_E)
_QtechLDhcpAckPkts_Type=Unsigned32
_QtechLDhcpAckPkts_Object=MibScalar
qtechLDhcpAckPkts=_QtechLDhcpAckPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,2,8),_QtechLDhcpAckPkts_Type())
qtechLDhcpAckPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechLDhcpAckPkts.setStatus(_A)
if mibBuilder.loadTexts:qtechLDhcpAckPkts.setUnits(_E)
_QtechLDhcpNakPkts_Type=Unsigned32
_QtechLDhcpNakPkts_Object=MibScalar
qtechLDhcpNakPkts=_QtechLDhcpNakPkts_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,2,9),_QtechLDhcpNakPkts_Type())
qtechLDhcpNakPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechLDhcpNakPkts.setStatus(_A)
if mibBuilder.loadTexts:qtechLDhcpNakPkts.setUnits(_E)
_QtechLDhcpReqTimes_Type=Unsigned32
_QtechLDhcpReqTimes_Object=MibScalar
qtechLDhcpReqTimes=_QtechLDhcpReqTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,2,10),_QtechLDhcpReqTimes_Type())
qtechLDhcpReqTimes.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechLDhcpReqTimes.setStatus(_A)
if mibBuilder.loadTexts:qtechLDhcpReqTimes.setUnits(_E)
_QtechLDhcpReqSucTimes_Type=Unsigned32
_QtechLDhcpReqSucTimes_Object=MibScalar
qtechLDhcpReqSucTimes=_QtechLDhcpReqSucTimes_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,2,11),_QtechLDhcpReqSucTimes_Type())
qtechLDhcpReqSucTimes.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechLDhcpReqSucTimes.setStatus(_A)
if mibBuilder.loadTexts:qtechLDhcpReqSucTimes.setUnits(_E)
_QtechCapwapDhcpServerConfig_ObjectIdentity=ObjectIdentity
qtechCapwapDhcpServerConfig=_QtechCapwapDhcpServerConfig_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,58,1,3))
_QtechDhcpScopeTable_Object=MibTable
qtechDhcpScopeTable=_QtechDhcpScopeTable_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1))
if mibBuilder.loadTexts:qtechDhcpScopeTable.setStatus(_A)
_QtechDhcpScopeEntry_Object=MibTableRow
qtechDhcpScopeEntry=_QtechDhcpScopeEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1))
qtechDhcpScopeEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:qtechDhcpScopeEntry.setStatus(_A)
class _QtechDhcpScopeIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_QtechDhcpScopeIndex_Type.__name__=_O
_QtechDhcpScopeIndex_Object=MibTableColumn
qtechDhcpScopeIndex=_QtechDhcpScopeIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,1),_QtechDhcpScopeIndex_Type())
qtechDhcpScopeIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:qtechDhcpScopeIndex.setStatus(_A)
class _QtechDhcpScopeName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_QtechDhcpScopeName_Type.__name__=_H
_QtechDhcpScopeName_Object=MibTableColumn
qtechDhcpScopeName=_QtechDhcpScopeName_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,2),_QtechDhcpScopeName_Type())
qtechDhcpScopeName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpScopeName.setStatus(_A)
class _QtechDhcpScopeLeaseTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(120,8640000))
_QtechDhcpScopeLeaseTime_Type.__name__=_F
_QtechDhcpScopeLeaseTime_Object=MibTableColumn
qtechDhcpScopeLeaseTime=_QtechDhcpScopeLeaseTime_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,3),_QtechDhcpScopeLeaseTime_Type())
qtechDhcpScopeLeaseTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpScopeLeaseTime.setStatus(_A)
_QtechDhcpScopeNetwork_Type=IpAddress
_QtechDhcpScopeNetwork_Object=MibTableColumn
qtechDhcpScopeNetwork=_QtechDhcpScopeNetwork_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,4),_QtechDhcpScopeNetwork_Type())
qtechDhcpScopeNetwork.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpScopeNetwork.setStatus(_A)
_QtechDhcpScopeNetmask_Type=IpAddress
_QtechDhcpScopeNetmask_Object=MibTableColumn
qtechDhcpScopeNetmask=_QtechDhcpScopeNetmask_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,5),_QtechDhcpScopeNetmask_Type())
qtechDhcpScopeNetmask.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpScopeNetmask.setStatus(_A)
_QtechDhcpScopePoolStartAddress_Type=IpAddress
_QtechDhcpScopePoolStartAddress_Object=MibTableColumn
qtechDhcpScopePoolStartAddress=_QtechDhcpScopePoolStartAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,6),_QtechDhcpScopePoolStartAddress_Type())
qtechDhcpScopePoolStartAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpScopePoolStartAddress.setStatus(_A)
_QtechDhcpScopePoolEndAddress_Type=IpAddress
_QtechDhcpScopePoolEndAddress_Object=MibTableColumn
qtechDhcpScopePoolEndAddress=_QtechDhcpScopePoolEndAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,7),_QtechDhcpScopePoolEndAddress_Type())
qtechDhcpScopePoolEndAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpScopePoolEndAddress.setStatus(_A)
_QtechDhcpScopeDefaultRouterAddress1_Type=IpAddress
_QtechDhcpScopeDefaultRouterAddress1_Object=MibTableColumn
qtechDhcpScopeDefaultRouterAddress1=_QtechDhcpScopeDefaultRouterAddress1_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,8),_QtechDhcpScopeDefaultRouterAddress1_Type())
qtechDhcpScopeDefaultRouterAddress1.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpScopeDefaultRouterAddress1.setStatus(_A)
_QtechDhcpScopeDefaultRouterAddress2_Type=IpAddress
_QtechDhcpScopeDefaultRouterAddress2_Object=MibTableColumn
qtechDhcpScopeDefaultRouterAddress2=_QtechDhcpScopeDefaultRouterAddress2_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,9),_QtechDhcpScopeDefaultRouterAddress2_Type())
qtechDhcpScopeDefaultRouterAddress2.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpScopeDefaultRouterAddress2.setStatus(_A)
_QtechDhcpScopeDefaultRouterAddress3_Type=IpAddress
_QtechDhcpScopeDefaultRouterAddress3_Object=MibTableColumn
qtechDhcpScopeDefaultRouterAddress3=_QtechDhcpScopeDefaultRouterAddress3_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,10),_QtechDhcpScopeDefaultRouterAddress3_Type())
qtechDhcpScopeDefaultRouterAddress3.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpScopeDefaultRouterAddress3.setStatus(_A)
class _QtechDhcpScopeDnsDomainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_QtechDhcpScopeDnsDomainName_Type.__name__=_H
_QtechDhcpScopeDnsDomainName_Object=MibTableColumn
qtechDhcpScopeDnsDomainName=_QtechDhcpScopeDnsDomainName_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,11),_QtechDhcpScopeDnsDomainName_Type())
qtechDhcpScopeDnsDomainName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpScopeDnsDomainName.setStatus(_A)
_QtechDhcpScopeDnsServerAddress1_Type=IpAddress
_QtechDhcpScopeDnsServerAddress1_Object=MibTableColumn
qtechDhcpScopeDnsServerAddress1=_QtechDhcpScopeDnsServerAddress1_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,12),_QtechDhcpScopeDnsServerAddress1_Type())
qtechDhcpScopeDnsServerAddress1.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpScopeDnsServerAddress1.setStatus(_A)
_QtechDhcpScopeDnsServerAddress2_Type=IpAddress
_QtechDhcpScopeDnsServerAddress2_Object=MibTableColumn
qtechDhcpScopeDnsServerAddress2=_QtechDhcpScopeDnsServerAddress2_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,13),_QtechDhcpScopeDnsServerAddress2_Type())
qtechDhcpScopeDnsServerAddress2.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpScopeDnsServerAddress2.setStatus(_A)
_QtechDhcpScopeDnsServerAddress3_Type=IpAddress
_QtechDhcpScopeDnsServerAddress3_Object=MibTableColumn
qtechDhcpScopeDnsServerAddress3=_QtechDhcpScopeDnsServerAddress3_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,14),_QtechDhcpScopeDnsServerAddress3_Type())
qtechDhcpScopeDnsServerAddress3.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpScopeDnsServerAddress3.setStatus(_A)
_QtechDhcpScopeNetbiosNameServerAddress1_Type=IpAddress
_QtechDhcpScopeNetbiosNameServerAddress1_Object=MibTableColumn
qtechDhcpScopeNetbiosNameServerAddress1=_QtechDhcpScopeNetbiosNameServerAddress1_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,15),_QtechDhcpScopeNetbiosNameServerAddress1_Type())
qtechDhcpScopeNetbiosNameServerAddress1.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpScopeNetbiosNameServerAddress1.setStatus(_A)
_QtechDhcpScopeNetbiosNameServerAddress2_Type=IpAddress
_QtechDhcpScopeNetbiosNameServerAddress2_Object=MibTableColumn
qtechDhcpScopeNetbiosNameServerAddress2=_QtechDhcpScopeNetbiosNameServerAddress2_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,16),_QtechDhcpScopeNetbiosNameServerAddress2_Type())
qtechDhcpScopeNetbiosNameServerAddress2.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpScopeNetbiosNameServerAddress2.setStatus(_A)
_QtechDhcpScopeNetbiosNameServerAddress3_Type=IpAddress
_QtechDhcpScopeNetbiosNameServerAddress3_Object=MibTableColumn
qtechDhcpScopeNetbiosNameServerAddress3=_QtechDhcpScopeNetbiosNameServerAddress3_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,17),_QtechDhcpScopeNetbiosNameServerAddress3_Type())
qtechDhcpScopeNetbiosNameServerAddress3.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpScopeNetbiosNameServerAddress3.setStatus(_A)
class _QtechDhcpScopeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_J,0),(_K,1)))
_QtechDhcpScopeState_Type.__name__=_F
_QtechDhcpScopeState_Object=MibTableColumn
qtechDhcpScopeState=_QtechDhcpScopeState_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,18),_QtechDhcpScopeState_Type())
qtechDhcpScopeState.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpScopeState.setStatus(_A)
_QtechDhcpScopeRowStatus_Type=RowStatus
_QtechDhcpScopeRowStatus_Object=MibTableColumn
qtechDhcpScopeRowStatus=_QtechDhcpScopeRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,19),_QtechDhcpScopeRowStatus_Type())
qtechDhcpScopeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpScopeRowStatus.setStatus(_A)
class _QtechDhcpIPPoolUsage_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_QtechDhcpIPPoolUsage_Type.__name__=_F
_QtechDhcpIPPoolUsage_Object=MibTableColumn
qtechDhcpIPPoolUsage=_QtechDhcpIPPoolUsage_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,20),_QtechDhcpIPPoolUsage_Type())
qtechDhcpIPPoolUsage.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpIPPoolUsage.setStatus(_A)
_QtechDhcpoption43_Type=IpAddress
_QtechDhcpoption43_Object=MibTableColumn
qtechDhcpoption43=_QtechDhcpoption43_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,21),_QtechDhcpoption43_Type())
qtechDhcpoption43.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpoption43.setStatus(_A)
_QtechDhcpoption138_Type=IpAddress
_QtechDhcpoption138_Object=MibTableColumn
qtechDhcpoption138=_QtechDhcpoption138_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,22),_QtechDhcpoption138_Type())
qtechDhcpoption138.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpoption138.setStatus(_A)
_QtechDhcpReqtimes_Type=Unsigned32
_QtechDhcpReqtimes_Object=MibTableColumn
qtechDhcpReqtimes=_QtechDhcpReqtimes_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,23),_QtechDhcpReqtimes_Type())
qtechDhcpReqtimes.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDhcpReqtimes.setStatus(_A)
_QtechDhcpReqSuctimes_Type=Unsigned32
_QtechDhcpReqSuctimes_Object=MibTableColumn
qtechDhcpReqSuctimes=_QtechDhcpReqSuctimes_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,24),_QtechDhcpReqSuctimes_Type())
qtechDhcpReqSuctimes.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDhcpReqSuctimes.setStatus(_A)
_QtechDhcpTotalIPNum_Type=Integer32
_QtechDhcpTotalIPNum_Object=MibTableColumn
qtechDhcpTotalIPNum=_QtechDhcpTotalIPNum_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,25),_QtechDhcpTotalIPNum_Type())
qtechDhcpTotalIPNum.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDhcpTotalIPNum.setStatus(_A)
_QtechDhcpCurrentUsedIPNum_Type=Integer32
_QtechDhcpCurrentUsedIPNum_Object=MibTableColumn
qtechDhcpCurrentUsedIPNum=_QtechDhcpCurrentUsedIPNum_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,3,1,1,26),_QtechDhcpCurrentUsedIPNum_Type())
qtechDhcpCurrentUsedIPNum.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechDhcpCurrentUsedIPNum.setStatus(_A)
_QtechCapwapDhcpRelayConfig_ObjectIdentity=ObjectIdentity
qtechCapwapDhcpRelayConfig=_QtechCapwapDhcpRelayConfig_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,58,1,4))
_QtechDhcpGlobalServerAddrTable_Object=MibTable
qtechDhcpGlobalServerAddrTable=_QtechDhcpGlobalServerAddrTable_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,4,1))
if mibBuilder.loadTexts:qtechDhcpGlobalServerAddrTable.setStatus(_A)
_QtechDhcpGlobalServerAddrEntry_Object=MibTableRow
qtechDhcpGlobalServerAddrEntry=_QtechDhcpGlobalServerAddrEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,4,1,1))
qtechDhcpGlobalServerAddrEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:qtechDhcpGlobalServerAddrEntry.setStatus(_A)
class _QtechDhcpGlobalServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_QtechDhcpGlobalServerIndex_Type.__name__=_F
_QtechDhcpGlobalServerIndex_Object=MibTableColumn
qtechDhcpGlobalServerIndex=_QtechDhcpGlobalServerIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,4,1,1,1),_QtechDhcpGlobalServerIndex_Type())
qtechDhcpGlobalServerIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:qtechDhcpGlobalServerIndex.setStatus(_A)
_QtechDhcpGlobalServerAddress_Type=IpAddress
_QtechDhcpGlobalServerAddress_Object=MibTableColumn
qtechDhcpGlobalServerAddress=_QtechDhcpGlobalServerAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,4,1,1,2),_QtechDhcpGlobalServerAddress_Type())
qtechDhcpGlobalServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpGlobalServerAddress.setStatus(_A)
_QtechDhcpGlobalServerRowStatus_Type=RowStatus
_QtechDhcpGlobalServerRowStatus_Object=MibTableColumn
qtechDhcpGlobalServerRowStatus=_QtechDhcpGlobalServerRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,4,1,1,3),_QtechDhcpGlobalServerRowStatus_Type())
qtechDhcpGlobalServerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpGlobalServerRowStatus.setStatus(_A)
_QtechDhcpIntfServerAddrTable_Object=MibTable
qtechDhcpIntfServerAddrTable=_QtechDhcpIntfServerAddrTable_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,4,2))
if mibBuilder.loadTexts:qtechDhcpIntfServerAddrTable.setStatus(_A)
_QtechDhcpIntfServerAddrEntry_Object=MibTableRow
qtechDhcpIntfServerAddrEntry=_QtechDhcpIntfServerAddrEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,4,2,1))
qtechDhcpIntfServerAddrEntry.setIndexNames((0,_M,_N),(0,_B,_R))
if mibBuilder.loadTexts:qtechDhcpIntfServerAddrEntry.setStatus(_A)
class _QtechDhcpIntfServerIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_QtechDhcpIntfServerIndex_Type.__name__=_F
_QtechDhcpIntfServerIndex_Object=MibTableColumn
qtechDhcpIntfServerIndex=_QtechDhcpIntfServerIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,4,2,1,1),_QtechDhcpIntfServerIndex_Type())
qtechDhcpIntfServerIndex.setMaxAccess(_L)
if mibBuilder.loadTexts:qtechDhcpIntfServerIndex.setStatus(_A)
_QtechDhcpIntfServerAddress_Type=IpAddress
_QtechDhcpIntfServerAddress_Object=MibTableColumn
qtechDhcpIntfServerAddress=_QtechDhcpIntfServerAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,4,2,1,2),_QtechDhcpIntfServerAddress_Type())
qtechDhcpIntfServerAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpIntfServerAddress.setStatus(_A)
_QtechDhcpIntfServerRowStatus_Type=RowStatus
_QtechDhcpIntfServerRowStatus_Object=MibTableColumn
qtechDhcpIntfServerRowStatus=_QtechDhcpIntfServerRowStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,58,1,4,2,1,3),_QtechDhcpIntfServerRowStatus_Type())
qtechDhcpIntfServerRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechDhcpIntfServerRowStatus.setStatus(_A)
_QtechCapwapDhcpMIBConformance_ObjectIdentity=ObjectIdentity
qtechCapwapDhcpMIBConformance=_QtechCapwapDhcpMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,58,2))
_QtechCapwapDhcpMIBCompliances_ObjectIdentity=ObjectIdentity
qtechCapwapDhcpMIBCompliances=_QtechCapwapDhcpMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,58,2,1))
_QtechCapwapDhcpMIBGroups_ObjectIdentity=ObjectIdentity
qtechCapwapDhcpMIBGroups=_QtechCapwapDhcpMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,58,2,2))
qtechCapwapDhcpMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,58,2,2,1))
qtechCapwapDhcpMIBGroup.setObjects(*((_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:qtechCapwapDhcpMIBGroup.setStatus(_A)
qtechCapwapDhcpServerConfigGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,58,2,2,2))
qtechCapwapDhcpServerConfigGroup.setObjects(*((_B,_G),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w)))
if mibBuilder.loadTexts:qtechCapwapDhcpServerConfigGroup.setStatus(_A)
qtechCapwapDhcpRelayGlobalConfigGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,58,2,2,3))
qtechCapwapDhcpRelayGlobalConfigGroup.setObjects(*((_B,_x),(_B,_y)))
if mibBuilder.loadTexts:qtechCapwapDhcpRelayGlobalConfigGroup.setStatus(_A)
qtechCapwapDhcpRelayIntfConfigGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,58,2,2,4))
qtechCapwapDhcpRelayIntfConfigGroup.setObjects(*((_B,_z),(_B,_A0)))
if mibBuilder.loadTexts:qtechCapwapDhcpRelayIntfConfigGroup.setStatus(_A)
qtechDhcpAddressExhaustTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,58,0,1))
qtechDhcpAddressExhaustTrap.setObjects((_B,_G))
if mibBuilder.loadTexts:qtechDhcpAddressExhaustTrap.setStatus(_A)
qtechDhcpAddressExhaustRecovTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,58,0,2))
qtechDhcpAddressExhaustRecovTrap.setObjects((_B,_G))
if mibBuilder.loadTexts:qtechDhcpAddressExhaustRecovTrap.setStatus(_A)
qtechDhcpClientFailTrap=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,58,0,3))
qtechDhcpClientFailTrap.setObjects((_B,_A1))
if mibBuilder.loadTexts:qtechDhcpClientFailTrap.setStatus(_A)
qtechCapwapDhcpMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,58,2,1,1))
qtechCapwapDhcpMIBCompliance.setObjects(*((_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:qtechCapwapDhcpMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechCapwapDhcpMIB':qtechCapwapDhcpMIB,'qtechCapwapDhcpMIBTrap':qtechCapwapDhcpMIBTrap,'qtechDhcpAddressExhaustTrap':qtechDhcpAddressExhaustTrap,'qtechDhcpAddressExhaustRecovTrap':qtechDhcpAddressExhaustRecovTrap,'qtechDhcpClientFailTrap':qtechDhcpClientFailTrap,'qtechCapwapDhcpMIBObjects':qtechCapwapDhcpMIBObjects,'qtechCapwapDhcpGlobalConfig':qtechCapwapDhcpGlobalConfig,_S:qtechLDhcpClearAllStats,_T:qtechLDhcpStartService,_A1:qtechDhcpClientMacAddress,'qtechLDhcpStartTIService':qtechLDhcpStartTIService,'qtechCapwapDhcpShowStats':qtechCapwapDhcpShowStats,_U:qtechLDhcpDiscoverPkts,_V:qtechLDhcpRequestPkts,_W:qtechLDhcpDeclinePkts,_X:qtechLDhcpInformPkts,_Y:qtechLDhcpReleasePkts,_Z:qtechLDhcpReplyPkts,_a:qtechLDhcpOfferPkts,_b:qtechLDhcpAckPkts,_c:qtechLDhcpNakPkts,_d:qtechLDhcpReqTimes,_e:qtechLDhcpReqSucTimes,'qtechCapwapDhcpServerConfig':qtechCapwapDhcpServerConfig,'qtechDhcpScopeTable':qtechDhcpScopeTable,'qtechDhcpScopeEntry':qtechDhcpScopeEntry,_P:qtechDhcpScopeIndex,_G:qtechDhcpScopeName,_f:qtechDhcpScopeLeaseTime,_g:qtechDhcpScopeNetwork,_h:qtechDhcpScopeNetmask,'qtechDhcpScopePoolStartAddress':qtechDhcpScopePoolStartAddress,'qtechDhcpScopePoolEndAddress':qtechDhcpScopePoolEndAddress,_i:qtechDhcpScopeDefaultRouterAddress1,_j:qtechDhcpScopeDefaultRouterAddress2,_k:qtechDhcpScopeDefaultRouterAddress3,_l:qtechDhcpScopeDnsDomainName,_m:qtechDhcpScopeDnsServerAddress1,_n:qtechDhcpScopeDnsServerAddress2,_o:qtechDhcpScopeDnsServerAddress3,_p:qtechDhcpScopeNetbiosNameServerAddress1,_q:qtechDhcpScopeNetbiosNameServerAddress2,_r:qtechDhcpScopeNetbiosNameServerAddress3,_s:qtechDhcpScopeState,_t:qtechDhcpScopeRowStatus,_u:qtechDhcpIPPoolUsage,_v:qtechDhcpoption43,_w:qtechDhcpoption138,'qtechDhcpReqtimes':qtechDhcpReqtimes,'qtechDhcpReqSuctimes':qtechDhcpReqSuctimes,'qtechDhcpTotalIPNum':qtechDhcpTotalIPNum,'qtechDhcpCurrentUsedIPNum':qtechDhcpCurrentUsedIPNum,'qtechCapwapDhcpRelayConfig':qtechCapwapDhcpRelayConfig,'qtechDhcpGlobalServerAddrTable':qtechDhcpGlobalServerAddrTable,'qtechDhcpGlobalServerAddrEntry':qtechDhcpGlobalServerAddrEntry,_Q:qtechDhcpGlobalServerIndex,_x:qtechDhcpGlobalServerAddress,_y:qtechDhcpGlobalServerRowStatus,'qtechDhcpIntfServerAddrTable':qtechDhcpIntfServerAddrTable,'qtechDhcpIntfServerAddrEntry':qtechDhcpIntfServerAddrEntry,_R:qtechDhcpIntfServerIndex,_z:qtechDhcpIntfServerAddress,_A0:qtechDhcpIntfServerRowStatus,'qtechCapwapDhcpMIBConformance':qtechCapwapDhcpMIBConformance,'qtechCapwapDhcpMIBCompliances':qtechCapwapDhcpMIBCompliances,'qtechCapwapDhcpMIBCompliance':qtechCapwapDhcpMIBCompliance,'qtechCapwapDhcpMIBGroups':qtechCapwapDhcpMIBGroups,_A2:qtechCapwapDhcpMIBGroup,_A3:qtechCapwapDhcpServerConfigGroup,_A4:qtechCapwapDhcpRelayGlobalConfigGroup,_A5:qtechCapwapDhcpRelayIntfConfigGroup})