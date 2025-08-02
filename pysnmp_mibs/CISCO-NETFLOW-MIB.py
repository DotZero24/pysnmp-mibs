_BJ='cnfTopFlowsReportGenerateGroup'
_BI='cnfTopFlowsGroup'
_BH='cnfTopFlowsReportSource'
_BG='cnfTopFlowsNextGenActionEffect'
_BF='cnfCIBridgedFlowStatsExpEnable'
_BE='cnfCIBridgedFlowStatsCrtEnable'
_BD='cnfCIMcastNetflowRPFFailedEnable'
_BC='cnfCIMcastNetflowEnable'
_BB='cnfTopFlowsReportAvailable'
_BA='cnfTopFlowsGenerate'
_B9='cnfTopFlowsVlan'
_B8='cnfTemplateExportVer9OptRefreshRate'
_B7='cnfTemplateExportVer9TplRefreshRate'
_B6='cnfTemplateExportVer9OptTimeout'
_B5='cnfTemplateExportVer9TplTimeout'
_B4='cnfTemplateExportVer9Enable'
_B3='cnfTemplateAgerPolls'
_B2='cnfTemplateActive'
_B1='cnfTemplateAdded'
_B0='cnfTemplateOptionsFlag'
_A_='cnfESPktsDropped'
_Az='cnfESPktsFailed'
_Ay='cnfESPktsExported'
_Ax='cnfESRecordsExported'
_Aw='cnfESExportRate'
_Av='cnfESSampledPacket'
_Au='cnfEICollectorStatus'
_At='cnfEIMaxCollectors'
_As='cnfEIBgpNextHop'
_Ar='cnfEIOriginAS'
_Aq='cnfEIPeerAS'
_Ap='cnfEIExportVersion'
_Ao='cnfPSInactive'
_An='cnfPSActive'
_Am='cnfPSBytes'
_Al='cnfPSPackets'
_Ak='cnfPSExpiredFlows'
_Aj='cnfPSLastClearElapsedTime'
_Ai='cnfPSPacketSizeDistribution'
_Ah='cnfCIMinDestinationMask'
_Ag='cnfCIMinSourceMask'
_Af='cnfCIInactiveTimeOut'
_Ae='cnfCIActiveTimeOut'
_Ad='cnfCIInactiveFlows'
_Ac='cnfCIActiveFlows'
_Ab='cnfCICacheEntries'
_Aa='cnfCICacheEnable'
_AZ='cnfCINetflowEnable'
_AY='cnfTopFlowsIndex'
_AX='cnfTemplateType'
_AW='cnfPSProtocolType'
_AV='cnfEICollectorPort'
_AU='cnfEICollectorAddress'
_AT='cnfEICollectorAddressType'
_AS='cnfCIBridgedFlowVlan'
_AR='OctetString'
_AQ='cnfBridgedFlowStatsCtrlGroup'
_AP='cnfMcastNetflowControlGroup'
_AO='cnfTopFlowsMatchDirection'
_AN='cnfTopFlowsMatchMaxBytes'
_AM='cnfTopFlowsMatchMinBytes'
_AL='cnfTopFlowsMatchMaxPackets'
_AK='cnfTopFlowsMatchMinPackets'
_AJ='cnfTopFlowsMatchClass'
_AI='cnfTopFlowsMatchSampler'
_AH='cnfTopFlowsMatchProtocol'
_AG='cnfTopFlowsMatchTOSByte'
_AF='cnfTopFlowsMatchOutputIf'
_AE='cnfTopFlowsMatchInputIf'
_AD='cnfTopFlowsMatchDstAS'
_AC='cnfTopFlowsMatchSrcAS'
_AB='cnfTopFlowsMatchDstPortHi'
_AA='cnfTopFlowsMatchDstPortLo'
_A9='cnfTopFlowsMatchSrcPortHi'
_A8='cnfTopFlowsMatchSrcPortLo'
_A7='cnfTopFlowsMatchNhAddressMask'
_A6='cnfTopFlowsMatchNhAddress'
_A5='cnfTopFlowsMatchNhAddressType'
_A4='cnfTopFlowsMatchDstAddressMask'
_A3='cnfTopFlowsMatchDstAddress'
_A2='cnfTopFlowsMatchDstAddressType'
_A1='cnfTopFlowsMatchSrcAddressMask'
_A0='cnfTopFlowsMatchSrcAddress'
_z='cnfTopFlowsMatchSrcAddressType'
_y='cnfTopFlowsPackets'
_x='cnfTopFlowsBytes'
_w='cnfTopFlowsFlags'
_v='cnfTopFlowsClassID'
_u='cnfTopFlowsSamplerID'
_t='cnfTopFlowsTCPFlags'
_s='cnfTopFlowsProtocol'
_r='cnfTopFlowsTOS'
_q='cnfTopFlowsLastSwitched'
_p='cnfTopFlowsFirstSwitched'
_o='cnfTopFlowsOutputIfIndex'
_n='cnfTopFlowsInputIfIndex'
_m='cnfTopFlowsDstAS'
_l='cnfTopFlowsSrcAS'
_k='cnfTopFlowsDstPort'
_j='cnfTopFlowsSrcPort'
_i='cnfTopFlowsNhAddress'
_h='cnfTopFlowsNhAddressType'
_g='cnfTopFlowsDstAddressMask'
_f='cnfTopFlowsDstAddress'
_e='cnfTopFlowsDstAddressType'
_d='cnfTopFlowsSrcAddressMask'
_c='cnfTopFlowsSrcAddress'
_b='cnfTopFlowsSrcAddressType'
_a='cnfTopFlowsCacheTimeout'
_Z='cnfTopFlowsSortBy'
_Y='cnfTopFlowsTotalFlows'
_X='cnfTopFlowsMatchingFlows'
_W='cnfTopFlowsAvailableFlows'
_V='cnfTopFlowsTopN'
_U='cnfTopFlowsTimeStamp'
_T='minutes'
_S='cnfTopFlowsControlGroup2'
_R='cnfTopFlowsControlGroup1'
_Q='cnfTopFlowsVlanGroup'
_P='cnfTopFlowsDataGroup2'
_O='cnfTopFlowsDataGroup1'
_N='deprecated'
_M='milliseconds'
_L='cnfExportTemplateGroup'
_K='cnfExportStatisticsGroup'
_J='cnfExportInfoGroup'
_I='cnfProtocolStatGroup'
_H='cnfCacheInfoGroup'
_G='cnfCICacheType'
_F='Integer32'
_E='not-accessible'
_D='read-write'
_C='read-only'
_B='current'
_A='CISCO-NETFLOW-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_AR,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero','ifIndex')
InetAddress,InetAddressPrefixLength,InetAddressType,InetAutonomousSystemNumber,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType','InetAutonomousSystemNumber','InetPortNumber')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
ciscoNetflowMIB=ModuleIdentity((1,3,6,1,4,1,9,9,387))
if mibBuilder.loadTexts:ciscoNetflowMIB.setRevisions(('2006-04-27 00:00','2006-04-20 00:00','2005-08-30 00:00','2005-03-27 00:00','2004-05-18 00:00','2004-01-09 00:00'))
class NfInterfaceDirectionTypes(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('interfaceDirNone',0),('interfaceDirIngress',1),('interfaceDirEgress',2),('interfaceDirBoth',3)))
class NfCacheTypes(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,23)));namedValues=NamedValues(*(('main',0),('as',1),('protocolPort',2),('sourcePrefix',3),('destinationPrefix',4),('prefix',5),('destinationOnly',6),('sourceDestination',7),('fullFlow',8),('asTos',9),('protocolPortTos',10),('sourcePrefixTos',11),('destinationPrefixTos',12),('prefixTos',13),('prefixPort',14),('bgpNexthopTos',15),('expBgpPrefix',23)))
class NfProtocolTypes(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22)));namedValues=NamedValues(*(('tcpTelnet',1),('tcpFtp',2),('tcpFtpd',3),('tcpWww',4),('tcpSmtp',5),('tcpX',6),('tcpBgp',7),('tcpNntp',8),('tcpFrag',9),('tcpOther',10),('udpDns',11),('udpNtp',12),('udpTftp',13),('udpFrag',14),('udpOther',15),('icmp',16),('igmp',17),('ipInIp',18),('ipv6InIp',19),('gre',20),('ipOther',21),('all',22)))
class NfTemplateTypes(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('template',1),('optionTemplate',2)))
class NfTopFlowsSortTypes(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noSort',1),('byPackets',2),('byBytes',3)))
class NfFlowDirectionTypes(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('flowDirNone',0),('flowDirIngress',1),('flowDirEgress',2)))
_CiscoNetflowMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoNetflowMIBNotifs=_CiscoNetflowMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,387,0))
_CiscoNetflowMIBObjects_ObjectIdentity=ObjectIdentity
ciscoNetflowMIBObjects=_CiscoNetflowMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,387,1))
_CnfCacheInfo_ObjectIdentity=ObjectIdentity
cnfCacheInfo=_CnfCacheInfo_ObjectIdentity((1,3,6,1,4,1,9,9,387,1,1))
_CnfCIInterfaceTable_Object=MibTable
cnfCIInterfaceTable=_CnfCIInterfaceTable_Object((1,3,6,1,4,1,9,9,387,1,1,1))
if mibBuilder.loadTexts:cnfCIInterfaceTable.setStatus(_B)
_CnfCIInterfaceEntry_Object=MibTableRow
cnfCIInterfaceEntry=_CnfCIInterfaceEntry_Object((1,3,6,1,4,1,9,9,387,1,1,1,1))
cnfCIInterfaceEntry.setIndexNames((0,'IF-MIB','ifIndex'))
if mibBuilder.loadTexts:cnfCIInterfaceEntry.setStatus(_B)
_CnfCINetflowEnable_Type=NfInterfaceDirectionTypes
_CnfCINetflowEnable_Object=MibTableColumn
cnfCINetflowEnable=_CnfCINetflowEnable_Object((1,3,6,1,4,1,9,9,387,1,1,1,1,1),_CnfCINetflowEnable_Type())
cnfCINetflowEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfCINetflowEnable.setStatus(_B)
_CnfCIMcastNetflowEnable_Type=NfInterfaceDirectionTypes
_CnfCIMcastNetflowEnable_Object=MibTableColumn
cnfCIMcastNetflowEnable=_CnfCIMcastNetflowEnable_Object((1,3,6,1,4,1,9,9,387,1,1,1,1,2),_CnfCIMcastNetflowEnable_Type())
cnfCIMcastNetflowEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfCIMcastNetflowEnable.setStatus(_B)
_CnfCICacheTable_Object=MibTable
cnfCICacheTable=_CnfCICacheTable_Object((1,3,6,1,4,1,9,9,387,1,1,2))
if mibBuilder.loadTexts:cnfCICacheTable.setStatus(_B)
_CnfCICacheEntry_Object=MibTableRow
cnfCICacheEntry=_CnfCICacheEntry_Object((1,3,6,1,4,1,9,9,387,1,1,2,1))
cnfCICacheEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:cnfCICacheEntry.setStatus(_B)
_CnfCICacheType_Type=NfCacheTypes
_CnfCICacheType_Object=MibTableColumn
cnfCICacheType=_CnfCICacheType_Object((1,3,6,1,4,1,9,9,387,1,1,2,1,1),_CnfCICacheType_Type())
cnfCICacheType.setMaxAccess(_E)
if mibBuilder.loadTexts:cnfCICacheType.setStatus(_B)
_CnfCICacheEnable_Type=TruthValue
_CnfCICacheEnable_Object=MibTableColumn
cnfCICacheEnable=_CnfCICacheEnable_Object((1,3,6,1,4,1,9,9,387,1,1,2,1,2),_CnfCICacheEnable_Type())
cnfCICacheEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfCICacheEnable.setStatus(_B)
_CnfCICacheEntries_Type=Unsigned32
_CnfCICacheEntries_Object=MibTableColumn
cnfCICacheEntries=_CnfCICacheEntries_Object((1,3,6,1,4,1,9,9,387,1,1,2,1,3),_CnfCICacheEntries_Type())
cnfCICacheEntries.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfCICacheEntries.setStatus(_B)
_CnfCIActiveFlows_Type=Unsigned32
_CnfCIActiveFlows_Object=MibTableColumn
cnfCIActiveFlows=_CnfCIActiveFlows_Object((1,3,6,1,4,1,9,9,387,1,1,2,1,4),_CnfCIActiveFlows_Type())
cnfCIActiveFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfCIActiveFlows.setStatus(_B)
_CnfCIInactiveFlows_Type=Unsigned32
_CnfCIInactiveFlows_Object=MibTableColumn
cnfCIInactiveFlows=_CnfCIInactiveFlows_Object((1,3,6,1,4,1,9,9,387,1,1,2,1,5),_CnfCIInactiveFlows_Type())
cnfCIInactiveFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfCIInactiveFlows.setStatus(_B)
_CnfCIActiveTimeOut_Type=Unsigned32
_CnfCIActiveTimeOut_Object=MibTableColumn
cnfCIActiveTimeOut=_CnfCIActiveTimeOut_Object((1,3,6,1,4,1,9,9,387,1,1,2,1,6),_CnfCIActiveTimeOut_Type())
cnfCIActiveTimeOut.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfCIActiveTimeOut.setStatus(_B)
if mibBuilder.loadTexts:cnfCIActiveTimeOut.setUnits(_T)
_CnfCIInactiveTimeOut_Type=Unsigned32
_CnfCIInactiveTimeOut_Object=MibTableColumn
cnfCIInactiveTimeOut=_CnfCIInactiveTimeOut_Object((1,3,6,1,4,1,9,9,387,1,1,2,1,7),_CnfCIInactiveTimeOut_Type())
cnfCIInactiveTimeOut.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfCIInactiveTimeOut.setStatus(_B)
if mibBuilder.loadTexts:cnfCIInactiveTimeOut.setUnits('seconds')
_CnfCIMinSourceMask_Type=InetAddressPrefixLength
_CnfCIMinSourceMask_Object=MibTableColumn
cnfCIMinSourceMask=_CnfCIMinSourceMask_Object((1,3,6,1,4,1,9,9,387,1,1,2,1,8),_CnfCIMinSourceMask_Type())
cnfCIMinSourceMask.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfCIMinSourceMask.setStatus(_B)
_CnfCIMinDestinationMask_Type=InetAddressPrefixLength
_CnfCIMinDestinationMask_Object=MibTableColumn
cnfCIMinDestinationMask=_CnfCIMinDestinationMask_Object((1,3,6,1,4,1,9,9,387,1,1,2,1,9),_CnfCIMinDestinationMask_Type())
cnfCIMinDestinationMask.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfCIMinDestinationMask.setStatus(_B)
_CnfCIBridgedFlowStatsCtrlTable_Object=MibTable
cnfCIBridgedFlowStatsCtrlTable=_CnfCIBridgedFlowStatsCtrlTable_Object((1,3,6,1,4,1,9,9,387,1,1,3))
if mibBuilder.loadTexts:cnfCIBridgedFlowStatsCtrlTable.setStatus(_B)
_CnfCIBridgedFlowStatsCtrlEntry_Object=MibTableRow
cnfCIBridgedFlowStatsCtrlEntry=_CnfCIBridgedFlowStatsCtrlEntry_Object((1,3,6,1,4,1,9,9,387,1,1,3,1))
cnfCIBridgedFlowStatsCtrlEntry.setIndexNames((0,_A,_AS))
if mibBuilder.loadTexts:cnfCIBridgedFlowStatsCtrlEntry.setStatus(_B)
_CnfCIBridgedFlowVlan_Type=VlanIndex
_CnfCIBridgedFlowVlan_Object=MibTableColumn
cnfCIBridgedFlowVlan=_CnfCIBridgedFlowVlan_Object((1,3,6,1,4,1,9,9,387,1,1,3,1,1),_CnfCIBridgedFlowVlan_Type())
cnfCIBridgedFlowVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:cnfCIBridgedFlowVlan.setStatus(_B)
_CnfCIBridgedFlowStatsCrtEnable_Type=TruthValue
_CnfCIBridgedFlowStatsCrtEnable_Object=MibTableColumn
cnfCIBridgedFlowStatsCrtEnable=_CnfCIBridgedFlowStatsCrtEnable_Object((1,3,6,1,4,1,9,9,387,1,1,3,1,2),_CnfCIBridgedFlowStatsCrtEnable_Type())
cnfCIBridgedFlowStatsCrtEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfCIBridgedFlowStatsCrtEnable.setStatus(_B)
_CnfCIBridgedFlowStatsExpEnable_Type=TruthValue
_CnfCIBridgedFlowStatsExpEnable_Object=MibTableColumn
cnfCIBridgedFlowStatsExpEnable=_CnfCIBridgedFlowStatsExpEnable_Object((1,3,6,1,4,1,9,9,387,1,1,3,1,3),_CnfCIBridgedFlowStatsExpEnable_Type())
cnfCIBridgedFlowStatsExpEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfCIBridgedFlowStatsExpEnable.setStatus(_B)
_CnfCIMcastNetflowRPFFailedEnable_Type=TruthValue
_CnfCIMcastNetflowRPFFailedEnable_Object=MibScalar
cnfCIMcastNetflowRPFFailedEnable=_CnfCIMcastNetflowRPFFailedEnable_Object((1,3,6,1,4,1,9,9,387,1,1,4),_CnfCIMcastNetflowRPFFailedEnable_Type())
cnfCIMcastNetflowRPFFailedEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfCIMcastNetflowRPFFailedEnable.setStatus(_B)
_CnfExportInfo_ObjectIdentity=ObjectIdentity
cnfExportInfo=_CnfExportInfo_ObjectIdentity((1,3,6,1,4,1,9,9,387,1,2))
_CnfEIExportInfoTable_Object=MibTable
cnfEIExportInfoTable=_CnfEIExportInfoTable_Object((1,3,6,1,4,1,9,9,387,1,2,1))
if mibBuilder.loadTexts:cnfEIExportInfoTable.setStatus(_B)
_CnfEIExportInfoEntry_Object=MibTableRow
cnfEIExportInfoEntry=_CnfEIExportInfoEntry_Object((1,3,6,1,4,1,9,9,387,1,2,1,1))
cnfEIExportInfoEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:cnfEIExportInfoEntry.setStatus(_B)
_CnfEIExportVersion_Type=Unsigned32
_CnfEIExportVersion_Object=MibTableColumn
cnfEIExportVersion=_CnfEIExportVersion_Object((1,3,6,1,4,1,9,9,387,1,2,1,1,1),_CnfEIExportVersion_Type())
cnfEIExportVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfEIExportVersion.setStatus(_B)
_CnfEIPeerAS_Type=TruthValue
_CnfEIPeerAS_Object=MibTableColumn
cnfEIPeerAS=_CnfEIPeerAS_Object((1,3,6,1,4,1,9,9,387,1,2,1,1,2),_CnfEIPeerAS_Type())
cnfEIPeerAS.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfEIPeerAS.setStatus(_B)
_CnfEIOriginAS_Type=TruthValue
_CnfEIOriginAS_Object=MibTableColumn
cnfEIOriginAS=_CnfEIOriginAS_Object((1,3,6,1,4,1,9,9,387,1,2,1,1,3),_CnfEIOriginAS_Type())
cnfEIOriginAS.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfEIOriginAS.setStatus(_B)
_CnfEIBgpNextHop_Type=TruthValue
_CnfEIBgpNextHop_Object=MibTableColumn
cnfEIBgpNextHop=_CnfEIBgpNextHop_Object((1,3,6,1,4,1,9,9,387,1,2,1,1,4),_CnfEIBgpNextHop_Type())
cnfEIBgpNextHop.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfEIBgpNextHop.setStatus(_B)
_CnfEIMaxCollectors_Type=Unsigned32
_CnfEIMaxCollectors_Object=MibScalar
cnfEIMaxCollectors=_CnfEIMaxCollectors_Object((1,3,6,1,4,1,9,9,387,1,2,2),_CnfEIMaxCollectors_Type())
cnfEIMaxCollectors.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfEIMaxCollectors.setStatus(_B)
_CnfEICollectorTable_Object=MibTable
cnfEICollectorTable=_CnfEICollectorTable_Object((1,3,6,1,4,1,9,9,387,1,2,3))
if mibBuilder.loadTexts:cnfEICollectorTable.setStatus(_B)
_CnfEICollectorEntry_Object=MibTableRow
cnfEICollectorEntry=_CnfEICollectorEntry_Object((1,3,6,1,4,1,9,9,387,1,2,3,1))
cnfEICollectorEntry.setIndexNames((0,_A,_G),(0,_A,_AT),(0,_A,_AU),(0,_A,_AV))
if mibBuilder.loadTexts:cnfEICollectorEntry.setStatus(_B)
_CnfEICollectorAddressType_Type=InetAddressType
_CnfEICollectorAddressType_Object=MibTableColumn
cnfEICollectorAddressType=_CnfEICollectorAddressType_Object((1,3,6,1,4,1,9,9,387,1,2,3,1,1),_CnfEICollectorAddressType_Type())
cnfEICollectorAddressType.setMaxAccess(_E)
if mibBuilder.loadTexts:cnfEICollectorAddressType.setStatus(_B)
_CnfEICollectorAddress_Type=InetAddress
_CnfEICollectorAddress_Object=MibTableColumn
cnfEICollectorAddress=_CnfEICollectorAddress_Object((1,3,6,1,4,1,9,9,387,1,2,3,1,2),_CnfEICollectorAddress_Type())
cnfEICollectorAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:cnfEICollectorAddress.setStatus(_B)
_CnfEICollectorPort_Type=InetPortNumber
_CnfEICollectorPort_Object=MibTableColumn
cnfEICollectorPort=_CnfEICollectorPort_Object((1,3,6,1,4,1,9,9,387,1,2,3,1,3),_CnfEICollectorPort_Type())
cnfEICollectorPort.setMaxAccess(_E)
if mibBuilder.loadTexts:cnfEICollectorPort.setStatus(_B)
_CnfEICollectorStatus_Type=RowStatus
_CnfEICollectorStatus_Object=MibTableColumn
cnfEICollectorStatus=_CnfEICollectorStatus_Object((1,3,6,1,4,1,9,9,387,1,2,3,1,4),_CnfEICollectorStatus_Type())
cnfEICollectorStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:cnfEICollectorStatus.setStatus(_B)
_CnfExportStatistics_ObjectIdentity=ObjectIdentity
cnfExportStatistics=_CnfExportStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,387,1,4))
_CnfESSampledPacket_Type=Counter32
_CnfESSampledPacket_Object=MibScalar
cnfESSampledPacket=_CnfESSampledPacket_Object((1,3,6,1,4,1,9,9,387,1,4,1),_CnfESSampledPacket_Type())
cnfESSampledPacket.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfESSampledPacket.setStatus(_B)
_CnfESExportRate_Type=Counter32
_CnfESExportRate_Object=MibScalar
cnfESExportRate=_CnfESExportRate_Object((1,3,6,1,4,1,9,9,387,1,4,2),_CnfESExportRate_Type())
cnfESExportRate.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfESExportRate.setStatus(_B)
if mibBuilder.loadTexts:cnfESExportRate.setUnits('bytes per second')
_CnfESRecordsExported_Type=Counter32
_CnfESRecordsExported_Object=MibScalar
cnfESRecordsExported=_CnfESRecordsExported_Object((1,3,6,1,4,1,9,9,387,1,4,3),_CnfESRecordsExported_Type())
cnfESRecordsExported.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfESRecordsExported.setStatus(_B)
_CnfESPktsExported_Type=Counter32
_CnfESPktsExported_Object=MibScalar
cnfESPktsExported=_CnfESPktsExported_Object((1,3,6,1,4,1,9,9,387,1,4,4),_CnfESPktsExported_Type())
cnfESPktsExported.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfESPktsExported.setStatus(_B)
_CnfESPktsFailed_Type=Counter32
_CnfESPktsFailed_Object=MibScalar
cnfESPktsFailed=_CnfESPktsFailed_Object((1,3,6,1,4,1,9,9,387,1,4,5),_CnfESPktsFailed_Type())
cnfESPktsFailed.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfESPktsFailed.setStatus(_B)
_CnfESPktsDropped_Type=Counter32
_CnfESPktsDropped_Object=MibScalar
cnfESPktsDropped=_CnfESPktsDropped_Object((1,3,6,1,4,1,9,9,387,1,4,6),_CnfESPktsDropped_Type())
cnfESPktsDropped.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfESPktsDropped.setStatus(_B)
_CnfProtocolStatistics_ObjectIdentity=ObjectIdentity
cnfProtocolStatistics=_CnfProtocolStatistics_ObjectIdentity((1,3,6,1,4,1,9,9,387,1,5))
class _CnfPSPacketSizeDistribution_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(52,52));fixedLength=52
_CnfPSPacketSizeDistribution_Type.__name__=_AR
_CnfPSPacketSizeDistribution_Object=MibScalar
cnfPSPacketSizeDistribution=_CnfPSPacketSizeDistribution_Object((1,3,6,1,4,1,9,9,387,1,5,1),_CnfPSPacketSizeDistribution_Type())
cnfPSPacketSizeDistribution.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfPSPacketSizeDistribution.setStatus(_B)
_CnfPSLastClearElapsedTime_Type=Gauge32
_CnfPSLastClearElapsedTime_Object=MibScalar
cnfPSLastClearElapsedTime=_CnfPSLastClearElapsedTime_Object((1,3,6,1,4,1,9,9,387,1,5,2),_CnfPSLastClearElapsedTime_Type())
cnfPSLastClearElapsedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfPSLastClearElapsedTime.setStatus(_B)
if mibBuilder.loadTexts:cnfPSLastClearElapsedTime.setUnits(_M)
_CnfPSProtocolStatTable_Object=MibTable
cnfPSProtocolStatTable=_CnfPSProtocolStatTable_Object((1,3,6,1,4,1,9,9,387,1,5,3))
if mibBuilder.loadTexts:cnfPSProtocolStatTable.setStatus(_B)
_CnfPSProtocolStatEntry_Object=MibTableRow
cnfPSProtocolStatEntry=_CnfPSProtocolStatEntry_Object((1,3,6,1,4,1,9,9,387,1,5,3,1))
cnfPSProtocolStatEntry.setIndexNames((0,_A,_AW))
if mibBuilder.loadTexts:cnfPSProtocolStatEntry.setStatus(_B)
_CnfPSProtocolType_Type=NfProtocolTypes
_CnfPSProtocolType_Object=MibTableColumn
cnfPSProtocolType=_CnfPSProtocolType_Object((1,3,6,1,4,1,9,9,387,1,5,3,1,1),_CnfPSProtocolType_Type())
cnfPSProtocolType.setMaxAccess(_E)
if mibBuilder.loadTexts:cnfPSProtocolType.setStatus(_B)
_CnfPSExpiredFlows_Type=Counter64
_CnfPSExpiredFlows_Object=MibTableColumn
cnfPSExpiredFlows=_CnfPSExpiredFlows_Object((1,3,6,1,4,1,9,9,387,1,5,3,1,2),_CnfPSExpiredFlows_Type())
cnfPSExpiredFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfPSExpiredFlows.setStatus(_B)
_CnfPSPackets_Type=Counter64
_CnfPSPackets_Object=MibTableColumn
cnfPSPackets=_CnfPSPackets_Object((1,3,6,1,4,1,9,9,387,1,5,3,1,3),_CnfPSPackets_Type())
cnfPSPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfPSPackets.setStatus(_B)
_CnfPSBytes_Type=Counter64
_CnfPSBytes_Object=MibTableColumn
cnfPSBytes=_CnfPSBytes_Object((1,3,6,1,4,1,9,9,387,1,5,3,1,4),_CnfPSBytes_Type())
cnfPSBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfPSBytes.setStatus(_B)
_CnfPSActive_Type=Counter64
_CnfPSActive_Object=MibTableColumn
cnfPSActive=_CnfPSActive_Object((1,3,6,1,4,1,9,9,387,1,5,3,1,5),_CnfPSActive_Type())
cnfPSActive.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfPSActive.setStatus(_B)
if mibBuilder.loadTexts:cnfPSActive.setUnits(_M)
_CnfPSInactive_Type=Counter64
_CnfPSInactive_Object=MibTableColumn
cnfPSInactive=_CnfPSInactive_Object((1,3,6,1,4,1,9,9,387,1,5,3,1,6),_CnfPSInactive_Type())
cnfPSInactive.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfPSInactive.setStatus(_B)
if mibBuilder.loadTexts:cnfPSInactive.setUnits(_M)
_CnfExportTemplate_ObjectIdentity=ObjectIdentity
cnfExportTemplate=_CnfExportTemplate_ObjectIdentity((1,3,6,1,4,1,9,9,387,1,6))
_CnfTemplateOptionsFlag_Type=Unsigned32
_CnfTemplateOptionsFlag_Object=MibScalar
cnfTemplateOptionsFlag=_CnfTemplateOptionsFlag_Object((1,3,6,1,4,1,9,9,387,1,6,1),_CnfTemplateOptionsFlag_Type())
cnfTemplateOptionsFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTemplateOptionsFlag.setStatus(_B)
_CnfTemplateTable_Object=MibTable
cnfTemplateTable=_CnfTemplateTable_Object((1,3,6,1,4,1,9,9,387,1,6,2))
if mibBuilder.loadTexts:cnfTemplateTable.setStatus(_B)
_CnfTemplateEntry_Object=MibTableRow
cnfTemplateEntry=_CnfTemplateEntry_Object((1,3,6,1,4,1,9,9,387,1,6,2,1))
cnfTemplateEntry.setIndexNames((0,_A,_AX))
if mibBuilder.loadTexts:cnfTemplateEntry.setStatus(_B)
_CnfTemplateType_Type=NfTemplateTypes
_CnfTemplateType_Object=MibTableColumn
cnfTemplateType=_CnfTemplateType_Object((1,3,6,1,4,1,9,9,387,1,6,2,1,1),_CnfTemplateType_Type())
cnfTemplateType.setMaxAccess(_E)
if mibBuilder.loadTexts:cnfTemplateType.setStatus(_B)
_CnfTemplateAdded_Type=Unsigned32
_CnfTemplateAdded_Object=MibTableColumn
cnfTemplateAdded=_CnfTemplateAdded_Object((1,3,6,1,4,1,9,9,387,1,6,2,1,2),_CnfTemplateAdded_Type())
cnfTemplateAdded.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTemplateAdded.setStatus(_B)
_CnfTemplateActive_Type=Unsigned32
_CnfTemplateActive_Object=MibTableColumn
cnfTemplateActive=_CnfTemplateActive_Object((1,3,6,1,4,1,9,9,387,1,6,2,1,3),_CnfTemplateActive_Type())
cnfTemplateActive.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTemplateActive.setStatus(_B)
_CnfTemplateAgerPolls_Type=Unsigned32
_CnfTemplateAgerPolls_Object=MibTableColumn
cnfTemplateAgerPolls=_CnfTemplateAgerPolls_Object((1,3,6,1,4,1,9,9,387,1,6,2,1,4),_CnfTemplateAgerPolls_Type())
cnfTemplateAgerPolls.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTemplateAgerPolls.setStatus(_B)
_CnfTemplateExportInfoTable_Object=MibTable
cnfTemplateExportInfoTable=_CnfTemplateExportInfoTable_Object((1,3,6,1,4,1,9,9,387,1,6,3))
if mibBuilder.loadTexts:cnfTemplateExportInfoTable.setStatus(_B)
_CnfTemplateExportInfoEntry_Object=MibTableRow
cnfTemplateExportInfoEntry=_CnfTemplateExportInfoEntry_Object((1,3,6,1,4,1,9,9,387,1,6,3,1))
cnfTemplateExportInfoEntry.setIndexNames((0,_A,_G))
if mibBuilder.loadTexts:cnfTemplateExportInfoEntry.setStatus(_B)
_CnfTemplateExportVer9Enable_Type=TruthValue
_CnfTemplateExportVer9Enable_Object=MibTableColumn
cnfTemplateExportVer9Enable=_CnfTemplateExportVer9Enable_Object((1,3,6,1,4,1,9,9,387,1,6,3,1,1),_CnfTemplateExportVer9Enable_Type())
cnfTemplateExportVer9Enable.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTemplateExportVer9Enable.setStatus(_B)
_CnfTemplateExportVer9TplTimeout_Type=Unsigned32
_CnfTemplateExportVer9TplTimeout_Object=MibTableColumn
cnfTemplateExportVer9TplTimeout=_CnfTemplateExportVer9TplTimeout_Object((1,3,6,1,4,1,9,9,387,1,6,3,1,2),_CnfTemplateExportVer9TplTimeout_Type())
cnfTemplateExportVer9TplTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTemplateExportVer9TplTimeout.setStatus(_B)
if mibBuilder.loadTexts:cnfTemplateExportVer9TplTimeout.setUnits(_T)
_CnfTemplateExportVer9OptTimeout_Type=Unsigned32
_CnfTemplateExportVer9OptTimeout_Object=MibTableColumn
cnfTemplateExportVer9OptTimeout=_CnfTemplateExportVer9OptTimeout_Object((1,3,6,1,4,1,9,9,387,1,6,3,1,3),_CnfTemplateExportVer9OptTimeout_Type())
cnfTemplateExportVer9OptTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTemplateExportVer9OptTimeout.setStatus(_B)
if mibBuilder.loadTexts:cnfTemplateExportVer9OptTimeout.setUnits(_T)
_CnfTemplateExportVer9TplRefreshRate_Type=Unsigned32
_CnfTemplateExportVer9TplRefreshRate_Object=MibTableColumn
cnfTemplateExportVer9TplRefreshRate=_CnfTemplateExportVer9TplRefreshRate_Object((1,3,6,1,4,1,9,9,387,1,6,3,1,4),_CnfTemplateExportVer9TplRefreshRate_Type())
cnfTemplateExportVer9TplRefreshRate.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTemplateExportVer9TplRefreshRate.setStatus(_B)
if mibBuilder.loadTexts:cnfTemplateExportVer9TplRefreshRate.setUnits('packets')
_CnfTemplateExportVer9OptRefreshRate_Type=Unsigned32
_CnfTemplateExportVer9OptRefreshRate_Object=MibTableColumn
cnfTemplateExportVer9OptRefreshRate=_CnfTemplateExportVer9OptRefreshRate_Object((1,3,6,1,4,1,9,9,387,1,6,3,1,5),_CnfTemplateExportVer9OptRefreshRate_Type())
cnfTemplateExportVer9OptRefreshRate.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTemplateExportVer9OptRefreshRate.setStatus(_B)
if mibBuilder.loadTexts:cnfTemplateExportVer9OptRefreshRate.setUnits('packets')
_CnfTopFlows_ObjectIdentity=ObjectIdentity
cnfTopFlows=_CnfTopFlows_ObjectIdentity((1,3,6,1,4,1,9,9,387,1,7))
_CnfTopFlowsTimeStamp_Type=TimeStamp
_CnfTopFlowsTimeStamp_Object=MibScalar
cnfTopFlowsTimeStamp=_CnfTopFlowsTimeStamp_Object((1,3,6,1,4,1,9,9,387,1,7,1),_CnfTopFlowsTimeStamp_Type())
cnfTopFlowsTimeStamp.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsTimeStamp.setStatus(_B)
_CnfTopFlowsTopN_Type=Unsigned32
_CnfTopFlowsTopN_Object=MibScalar
cnfTopFlowsTopN=_CnfTopFlowsTopN_Object((1,3,6,1,4,1,9,9,387,1,7,2),_CnfTopFlowsTopN_Type())
cnfTopFlowsTopN.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsTopN.setStatus(_B)
_CnfTopFlowsAvailableFlows_Type=Unsigned32
_CnfTopFlowsAvailableFlows_Object=MibScalar
cnfTopFlowsAvailableFlows=_CnfTopFlowsAvailableFlows_Object((1,3,6,1,4,1,9,9,387,1,7,3),_CnfTopFlowsAvailableFlows_Type())
cnfTopFlowsAvailableFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsAvailableFlows.setStatus(_B)
_CnfTopFlowsMatchingFlows_Type=Unsigned32
_CnfTopFlowsMatchingFlows_Object=MibScalar
cnfTopFlowsMatchingFlows=_CnfTopFlowsMatchingFlows_Object((1,3,6,1,4,1,9,9,387,1,7,4),_CnfTopFlowsMatchingFlows_Type())
cnfTopFlowsMatchingFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsMatchingFlows.setStatus(_B)
_CnfTopFlowsTotalFlows_Type=Unsigned32
_CnfTopFlowsTotalFlows_Object=MibScalar
cnfTopFlowsTotalFlows=_CnfTopFlowsTotalFlows_Object((1,3,6,1,4,1,9,9,387,1,7,5),_CnfTopFlowsTotalFlows_Type())
cnfTopFlowsTotalFlows.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsTotalFlows.setStatus(_B)
_CnfTopFlowsSortBy_Type=NfTopFlowsSortTypes
_CnfTopFlowsSortBy_Object=MibScalar
cnfTopFlowsSortBy=_CnfTopFlowsSortBy_Object((1,3,6,1,4,1,9,9,387,1,7,6),_CnfTopFlowsSortBy_Type())
cnfTopFlowsSortBy.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsSortBy.setStatus(_B)
_CnfTopFlowsCacheTimeout_Type=Unsigned32
_CnfTopFlowsCacheTimeout_Object=MibScalar
cnfTopFlowsCacheTimeout=_CnfTopFlowsCacheTimeout_Object((1,3,6,1,4,1,9,9,387,1,7,7),_CnfTopFlowsCacheTimeout_Type())
cnfTopFlowsCacheTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsCacheTimeout.setStatus(_B)
if mibBuilder.loadTexts:cnfTopFlowsCacheTimeout.setUnits(_M)
_CnfTopFlowsTable_Object=MibTable
cnfTopFlowsTable=_CnfTopFlowsTable_Object((1,3,6,1,4,1,9,9,387,1,7,8))
if mibBuilder.loadTexts:cnfTopFlowsTable.setStatus(_B)
_CnfTopFlowsTableEntry_Object=MibTableRow
cnfTopFlowsTableEntry=_CnfTopFlowsTableEntry_Object((1,3,6,1,4,1,9,9,387,1,7,8,1))
cnfTopFlowsTableEntry.setIndexNames((0,_A,_AY))
if mibBuilder.loadTexts:cnfTopFlowsTableEntry.setStatus(_B)
_CnfTopFlowsIndex_Type=Unsigned32
_CnfTopFlowsIndex_Object=MibTableColumn
cnfTopFlowsIndex=_CnfTopFlowsIndex_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,1),_CnfTopFlowsIndex_Type())
cnfTopFlowsIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:cnfTopFlowsIndex.setStatus(_B)
_CnfTopFlowsSrcAddressType_Type=InetAddressType
_CnfTopFlowsSrcAddressType_Object=MibTableColumn
cnfTopFlowsSrcAddressType=_CnfTopFlowsSrcAddressType_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,2),_CnfTopFlowsSrcAddressType_Type())
cnfTopFlowsSrcAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsSrcAddressType.setStatus(_B)
_CnfTopFlowsSrcAddress_Type=InetAddress
_CnfTopFlowsSrcAddress_Object=MibTableColumn
cnfTopFlowsSrcAddress=_CnfTopFlowsSrcAddress_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,3),_CnfTopFlowsSrcAddress_Type())
cnfTopFlowsSrcAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsSrcAddress.setStatus(_B)
_CnfTopFlowsSrcAddressMask_Type=InetAddressPrefixLength
_CnfTopFlowsSrcAddressMask_Object=MibTableColumn
cnfTopFlowsSrcAddressMask=_CnfTopFlowsSrcAddressMask_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,4),_CnfTopFlowsSrcAddressMask_Type())
cnfTopFlowsSrcAddressMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsSrcAddressMask.setStatus(_B)
_CnfTopFlowsDstAddressType_Type=InetAddressType
_CnfTopFlowsDstAddressType_Object=MibTableColumn
cnfTopFlowsDstAddressType=_CnfTopFlowsDstAddressType_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,5),_CnfTopFlowsDstAddressType_Type())
cnfTopFlowsDstAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsDstAddressType.setStatus(_B)
_CnfTopFlowsDstAddress_Type=InetAddress
_CnfTopFlowsDstAddress_Object=MibTableColumn
cnfTopFlowsDstAddress=_CnfTopFlowsDstAddress_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,6),_CnfTopFlowsDstAddress_Type())
cnfTopFlowsDstAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsDstAddress.setStatus(_B)
_CnfTopFlowsDstAddressMask_Type=InetAddressPrefixLength
_CnfTopFlowsDstAddressMask_Object=MibTableColumn
cnfTopFlowsDstAddressMask=_CnfTopFlowsDstAddressMask_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,7),_CnfTopFlowsDstAddressMask_Type())
cnfTopFlowsDstAddressMask.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsDstAddressMask.setStatus(_B)
_CnfTopFlowsNhAddressType_Type=InetAddressType
_CnfTopFlowsNhAddressType_Object=MibTableColumn
cnfTopFlowsNhAddressType=_CnfTopFlowsNhAddressType_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,8),_CnfTopFlowsNhAddressType_Type())
cnfTopFlowsNhAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsNhAddressType.setStatus(_B)
_CnfTopFlowsNhAddress_Type=InetAddress
_CnfTopFlowsNhAddress_Object=MibTableColumn
cnfTopFlowsNhAddress=_CnfTopFlowsNhAddress_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,9),_CnfTopFlowsNhAddress_Type())
cnfTopFlowsNhAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsNhAddress.setStatus(_B)
_CnfTopFlowsSrcPort_Type=InetPortNumber
_CnfTopFlowsSrcPort_Object=MibTableColumn
cnfTopFlowsSrcPort=_CnfTopFlowsSrcPort_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,10),_CnfTopFlowsSrcPort_Type())
cnfTopFlowsSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsSrcPort.setStatus(_B)
_CnfTopFlowsDstPort_Type=InetPortNumber
_CnfTopFlowsDstPort_Object=MibTableColumn
cnfTopFlowsDstPort=_CnfTopFlowsDstPort_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,11),_CnfTopFlowsDstPort_Type())
cnfTopFlowsDstPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsDstPort.setStatus(_B)
_CnfTopFlowsSrcAS_Type=InetAutonomousSystemNumber
_CnfTopFlowsSrcAS_Object=MibTableColumn
cnfTopFlowsSrcAS=_CnfTopFlowsSrcAS_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,12),_CnfTopFlowsSrcAS_Type())
cnfTopFlowsSrcAS.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsSrcAS.setStatus(_B)
_CnfTopFlowsDstAS_Type=InetAutonomousSystemNumber
_CnfTopFlowsDstAS_Object=MibTableColumn
cnfTopFlowsDstAS=_CnfTopFlowsDstAS_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,13),_CnfTopFlowsDstAS_Type())
cnfTopFlowsDstAS.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsDstAS.setStatus(_B)
_CnfTopFlowsInputIfIndex_Type=InterfaceIndex
_CnfTopFlowsInputIfIndex_Object=MibTableColumn
cnfTopFlowsInputIfIndex=_CnfTopFlowsInputIfIndex_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,14),_CnfTopFlowsInputIfIndex_Type())
cnfTopFlowsInputIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsInputIfIndex.setStatus(_B)
_CnfTopFlowsOutputIfIndex_Type=InterfaceIndex
_CnfTopFlowsOutputIfIndex_Object=MibTableColumn
cnfTopFlowsOutputIfIndex=_CnfTopFlowsOutputIfIndex_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,15),_CnfTopFlowsOutputIfIndex_Type())
cnfTopFlowsOutputIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsOutputIfIndex.setStatus(_B)
_CnfTopFlowsFirstSwitched_Type=TimeStamp
_CnfTopFlowsFirstSwitched_Object=MibTableColumn
cnfTopFlowsFirstSwitched=_CnfTopFlowsFirstSwitched_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,16),_CnfTopFlowsFirstSwitched_Type())
cnfTopFlowsFirstSwitched.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsFirstSwitched.setStatus(_B)
_CnfTopFlowsLastSwitched_Type=TimeStamp
_CnfTopFlowsLastSwitched_Object=MibTableColumn
cnfTopFlowsLastSwitched=_CnfTopFlowsLastSwitched_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,17),_CnfTopFlowsLastSwitched_Type())
cnfTopFlowsLastSwitched.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsLastSwitched.setStatus(_B)
_CnfTopFlowsTOS_Type=Unsigned32
_CnfTopFlowsTOS_Object=MibTableColumn
cnfTopFlowsTOS=_CnfTopFlowsTOS_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,18),_CnfTopFlowsTOS_Type())
cnfTopFlowsTOS.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsTOS.setStatus(_B)
_CnfTopFlowsProtocol_Type=Unsigned32
_CnfTopFlowsProtocol_Object=MibTableColumn
cnfTopFlowsProtocol=_CnfTopFlowsProtocol_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,19),_CnfTopFlowsProtocol_Type())
cnfTopFlowsProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsProtocol.setStatus(_B)
_CnfTopFlowsTCPFlags_Type=Unsigned32
_CnfTopFlowsTCPFlags_Object=MibTableColumn
cnfTopFlowsTCPFlags=_CnfTopFlowsTCPFlags_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,20),_CnfTopFlowsTCPFlags_Type())
cnfTopFlowsTCPFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsTCPFlags.setStatus(_B)
_CnfTopFlowsSamplerID_Type=Unsigned32
_CnfTopFlowsSamplerID_Object=MibTableColumn
cnfTopFlowsSamplerID=_CnfTopFlowsSamplerID_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,21),_CnfTopFlowsSamplerID_Type())
cnfTopFlowsSamplerID.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsSamplerID.setStatus(_B)
_CnfTopFlowsClassID_Type=Unsigned32
_CnfTopFlowsClassID_Object=MibTableColumn
cnfTopFlowsClassID=_CnfTopFlowsClassID_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,22),_CnfTopFlowsClassID_Type())
cnfTopFlowsClassID.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsClassID.setStatus(_B)
_CnfTopFlowsFlags_Type=Unsigned32
_CnfTopFlowsFlags_Object=MibTableColumn
cnfTopFlowsFlags=_CnfTopFlowsFlags_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,23),_CnfTopFlowsFlags_Type())
cnfTopFlowsFlags.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsFlags.setStatus(_B)
_CnfTopFlowsBytes_Type=Unsigned32
_CnfTopFlowsBytes_Object=MibTableColumn
cnfTopFlowsBytes=_CnfTopFlowsBytes_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,24),_CnfTopFlowsBytes_Type())
cnfTopFlowsBytes.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsBytes.setStatus(_B)
_CnfTopFlowsPackets_Type=Unsigned32
_CnfTopFlowsPackets_Object=MibTableColumn
cnfTopFlowsPackets=_CnfTopFlowsPackets_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,25),_CnfTopFlowsPackets_Type())
cnfTopFlowsPackets.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsPackets.setStatus(_B)
_CnfTopFlowsVlan_Type=VlanIndex
_CnfTopFlowsVlan_Object=MibTableColumn
cnfTopFlowsVlan=_CnfTopFlowsVlan_Object((1,3,6,1,4,1,9,9,387,1,7,8,1,26),_CnfTopFlowsVlan_Type())
cnfTopFlowsVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsVlan.setStatus(_B)
_CnfTopFlowsMatchSrcAddressType_Type=InetAddressType
_CnfTopFlowsMatchSrcAddressType_Object=MibScalar
cnfTopFlowsMatchSrcAddressType=_CnfTopFlowsMatchSrcAddressType_Object((1,3,6,1,4,1,9,9,387,1,7,9),_CnfTopFlowsMatchSrcAddressType_Type())
cnfTopFlowsMatchSrcAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchSrcAddressType.setStatus(_B)
_CnfTopFlowsMatchSrcAddress_Type=InetAddress
_CnfTopFlowsMatchSrcAddress_Object=MibScalar
cnfTopFlowsMatchSrcAddress=_CnfTopFlowsMatchSrcAddress_Object((1,3,6,1,4,1,9,9,387,1,7,10),_CnfTopFlowsMatchSrcAddress_Type())
cnfTopFlowsMatchSrcAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchSrcAddress.setStatus(_B)
_CnfTopFlowsMatchSrcAddressMask_Type=InetAddressPrefixLength
_CnfTopFlowsMatchSrcAddressMask_Object=MibScalar
cnfTopFlowsMatchSrcAddressMask=_CnfTopFlowsMatchSrcAddressMask_Object((1,3,6,1,4,1,9,9,387,1,7,11),_CnfTopFlowsMatchSrcAddressMask_Type())
cnfTopFlowsMatchSrcAddressMask.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchSrcAddressMask.setStatus(_B)
_CnfTopFlowsMatchDstAddressType_Type=InetAddressType
_CnfTopFlowsMatchDstAddressType_Object=MibScalar
cnfTopFlowsMatchDstAddressType=_CnfTopFlowsMatchDstAddressType_Object((1,3,6,1,4,1,9,9,387,1,7,12),_CnfTopFlowsMatchDstAddressType_Type())
cnfTopFlowsMatchDstAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchDstAddressType.setStatus(_B)
_CnfTopFlowsMatchDstAddress_Type=InetAddress
_CnfTopFlowsMatchDstAddress_Object=MibScalar
cnfTopFlowsMatchDstAddress=_CnfTopFlowsMatchDstAddress_Object((1,3,6,1,4,1,9,9,387,1,7,13),_CnfTopFlowsMatchDstAddress_Type())
cnfTopFlowsMatchDstAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchDstAddress.setStatus(_B)
_CnfTopFlowsMatchDstAddressMask_Type=InetAddressPrefixLength
_CnfTopFlowsMatchDstAddressMask_Object=MibScalar
cnfTopFlowsMatchDstAddressMask=_CnfTopFlowsMatchDstAddressMask_Object((1,3,6,1,4,1,9,9,387,1,7,14),_CnfTopFlowsMatchDstAddressMask_Type())
cnfTopFlowsMatchDstAddressMask.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchDstAddressMask.setStatus(_B)
_CnfTopFlowsMatchNhAddressType_Type=InetAddressType
_CnfTopFlowsMatchNhAddressType_Object=MibScalar
cnfTopFlowsMatchNhAddressType=_CnfTopFlowsMatchNhAddressType_Object((1,3,6,1,4,1,9,9,387,1,7,15),_CnfTopFlowsMatchNhAddressType_Type())
cnfTopFlowsMatchNhAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchNhAddressType.setStatus(_B)
_CnfTopFlowsMatchNhAddress_Type=InetAddress
_CnfTopFlowsMatchNhAddress_Object=MibScalar
cnfTopFlowsMatchNhAddress=_CnfTopFlowsMatchNhAddress_Object((1,3,6,1,4,1,9,9,387,1,7,16),_CnfTopFlowsMatchNhAddress_Type())
cnfTopFlowsMatchNhAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchNhAddress.setStatus(_B)
_CnfTopFlowsMatchNhAddressMask_Type=InetAddressPrefixLength
_CnfTopFlowsMatchNhAddressMask_Object=MibScalar
cnfTopFlowsMatchNhAddressMask=_CnfTopFlowsMatchNhAddressMask_Object((1,3,6,1,4,1,9,9,387,1,7,17),_CnfTopFlowsMatchNhAddressMask_Type())
cnfTopFlowsMatchNhAddressMask.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchNhAddressMask.setStatus(_B)
class _CnfTopFlowsMatchSrcPortLo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,65535))
_CnfTopFlowsMatchSrcPortLo_Type.__name__=_F
_CnfTopFlowsMatchSrcPortLo_Object=MibScalar
cnfTopFlowsMatchSrcPortLo=_CnfTopFlowsMatchSrcPortLo_Object((1,3,6,1,4,1,9,9,387,1,7,18),_CnfTopFlowsMatchSrcPortLo_Type())
cnfTopFlowsMatchSrcPortLo.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchSrcPortLo.setStatus(_B)
class _CnfTopFlowsMatchSrcPortHi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,65535))
_CnfTopFlowsMatchSrcPortHi_Type.__name__=_F
_CnfTopFlowsMatchSrcPortHi_Object=MibScalar
cnfTopFlowsMatchSrcPortHi=_CnfTopFlowsMatchSrcPortHi_Object((1,3,6,1,4,1,9,9,387,1,7,19),_CnfTopFlowsMatchSrcPortHi_Type())
cnfTopFlowsMatchSrcPortHi.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchSrcPortHi.setStatus(_B)
class _CnfTopFlowsMatchDstPortLo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,65535))
_CnfTopFlowsMatchDstPortLo_Type.__name__=_F
_CnfTopFlowsMatchDstPortLo_Object=MibScalar
cnfTopFlowsMatchDstPortLo=_CnfTopFlowsMatchDstPortLo_Object((1,3,6,1,4,1,9,9,387,1,7,20),_CnfTopFlowsMatchDstPortLo_Type())
cnfTopFlowsMatchDstPortLo.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchDstPortLo.setStatus(_B)
class _CnfTopFlowsMatchDstPortHi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,65535))
_CnfTopFlowsMatchDstPortHi_Type.__name__=_F
_CnfTopFlowsMatchDstPortHi_Object=MibScalar
cnfTopFlowsMatchDstPortHi=_CnfTopFlowsMatchDstPortHi_Object((1,3,6,1,4,1,9,9,387,1,7,21),_CnfTopFlowsMatchDstPortHi_Type())
cnfTopFlowsMatchDstPortHi.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchDstPortHi.setStatus(_B)
_CnfTopFlowsMatchSrcAS_Type=Integer32
_CnfTopFlowsMatchSrcAS_Object=MibScalar
cnfTopFlowsMatchSrcAS=_CnfTopFlowsMatchSrcAS_Object((1,3,6,1,4,1,9,9,387,1,7,22),_CnfTopFlowsMatchSrcAS_Type())
cnfTopFlowsMatchSrcAS.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchSrcAS.setStatus(_B)
_CnfTopFlowsMatchDstAS_Type=Integer32
_CnfTopFlowsMatchDstAS_Object=MibScalar
cnfTopFlowsMatchDstAS=_CnfTopFlowsMatchDstAS_Object((1,3,6,1,4,1,9,9,387,1,7,23),_CnfTopFlowsMatchDstAS_Type())
cnfTopFlowsMatchDstAS.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchDstAS.setStatus(_B)
_CnfTopFlowsMatchInputIf_Type=InterfaceIndexOrZero
_CnfTopFlowsMatchInputIf_Object=MibScalar
cnfTopFlowsMatchInputIf=_CnfTopFlowsMatchInputIf_Object((1,3,6,1,4,1,9,9,387,1,7,24),_CnfTopFlowsMatchInputIf_Type())
cnfTopFlowsMatchInputIf.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchInputIf.setStatus(_B)
_CnfTopFlowsMatchOutputIf_Type=InterfaceIndexOrZero
_CnfTopFlowsMatchOutputIf_Object=MibScalar
cnfTopFlowsMatchOutputIf=_CnfTopFlowsMatchOutputIf_Object((1,3,6,1,4,1,9,9,387,1,7,25),_CnfTopFlowsMatchOutputIf_Type())
cnfTopFlowsMatchOutputIf.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchOutputIf.setStatus(_B)
_CnfTopFlowsMatchTOSByte_Type=Integer32
_CnfTopFlowsMatchTOSByte_Object=MibScalar
cnfTopFlowsMatchTOSByte=_CnfTopFlowsMatchTOSByte_Object((1,3,6,1,4,1,9,9,387,1,7,26),_CnfTopFlowsMatchTOSByte_Type())
cnfTopFlowsMatchTOSByte.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchTOSByte.setStatus(_B)
_CnfTopFlowsMatchProtocol_Type=Integer32
_CnfTopFlowsMatchProtocol_Object=MibScalar
cnfTopFlowsMatchProtocol=_CnfTopFlowsMatchProtocol_Object((1,3,6,1,4,1,9,9,387,1,7,27),_CnfTopFlowsMatchProtocol_Type())
cnfTopFlowsMatchProtocol.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchProtocol.setStatus(_B)
_CnfTopFlowsMatchSampler_Type=DisplayString
_CnfTopFlowsMatchSampler_Object=MibScalar
cnfTopFlowsMatchSampler=_CnfTopFlowsMatchSampler_Object((1,3,6,1,4,1,9,9,387,1,7,28),_CnfTopFlowsMatchSampler_Type())
cnfTopFlowsMatchSampler.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchSampler.setStatus(_B)
_CnfTopFlowsMatchClass_Type=DisplayString
_CnfTopFlowsMatchClass_Object=MibScalar
cnfTopFlowsMatchClass=_CnfTopFlowsMatchClass_Object((1,3,6,1,4,1,9,9,387,1,7,29),_CnfTopFlowsMatchClass_Type())
cnfTopFlowsMatchClass.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchClass.setStatus(_B)
_CnfTopFlowsMatchMinPackets_Type=Unsigned32
_CnfTopFlowsMatchMinPackets_Object=MibScalar
cnfTopFlowsMatchMinPackets=_CnfTopFlowsMatchMinPackets_Object((1,3,6,1,4,1,9,9,387,1,7,30),_CnfTopFlowsMatchMinPackets_Type())
cnfTopFlowsMatchMinPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchMinPackets.setStatus(_B)
_CnfTopFlowsMatchMaxPackets_Type=Unsigned32
_CnfTopFlowsMatchMaxPackets_Object=MibScalar
cnfTopFlowsMatchMaxPackets=_CnfTopFlowsMatchMaxPackets_Object((1,3,6,1,4,1,9,9,387,1,7,31),_CnfTopFlowsMatchMaxPackets_Type())
cnfTopFlowsMatchMaxPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchMaxPackets.setStatus(_B)
_CnfTopFlowsMatchMinBytes_Type=Unsigned32
_CnfTopFlowsMatchMinBytes_Object=MibScalar
cnfTopFlowsMatchMinBytes=_CnfTopFlowsMatchMinBytes_Object((1,3,6,1,4,1,9,9,387,1,7,32),_CnfTopFlowsMatchMinBytes_Type())
cnfTopFlowsMatchMinBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchMinBytes.setStatus(_B)
_CnfTopFlowsMatchMaxBytes_Type=Unsigned32
_CnfTopFlowsMatchMaxBytes_Object=MibScalar
cnfTopFlowsMatchMaxBytes=_CnfTopFlowsMatchMaxBytes_Object((1,3,6,1,4,1,9,9,387,1,7,33),_CnfTopFlowsMatchMaxBytes_Type())
cnfTopFlowsMatchMaxBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchMaxBytes.setStatus(_B)
_CnfTopFlowsMatchDirection_Type=NfFlowDirectionTypes
_CnfTopFlowsMatchDirection_Object=MibScalar
cnfTopFlowsMatchDirection=_CnfTopFlowsMatchDirection_Object((1,3,6,1,4,1,9,9,387,1,7,34),_CnfTopFlowsMatchDirection_Type())
cnfTopFlowsMatchDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsMatchDirection.setStatus(_B)
_CnfTopFlowsGenerate_Type=TruthValue
_CnfTopFlowsGenerate_Object=MibScalar
cnfTopFlowsGenerate=_CnfTopFlowsGenerate_Object((1,3,6,1,4,1,9,9,387,1,7,35),_CnfTopFlowsGenerate_Type())
cnfTopFlowsGenerate.setMaxAccess(_D)
if mibBuilder.loadTexts:cnfTopFlowsGenerate.setStatus(_B)
_CnfTopFlowsReportAvailable_Type=TruthValue
_CnfTopFlowsReportAvailable_Object=MibScalar
cnfTopFlowsReportAvailable=_CnfTopFlowsReportAvailable_Object((1,3,6,1,4,1,9,9,387,1,7,36),_CnfTopFlowsReportAvailable_Type())
cnfTopFlowsReportAvailable.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsReportAvailable.setStatus(_B)
class _CnfTopFlowsNextGenActionEffect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noOp',1),('generate',2)))
_CnfTopFlowsNextGenActionEffect_Type.__name__=_F
_CnfTopFlowsNextGenActionEffect_Object=MibScalar
cnfTopFlowsNextGenActionEffect=_CnfTopFlowsNextGenActionEffect_Object((1,3,6,1,4,1,9,9,387,1,7,37),_CnfTopFlowsNextGenActionEffect_Type())
cnfTopFlowsNextGenActionEffect.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsNextGenActionEffect.setStatus(_B)
class _CnfTopFlowsReportSource_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('hardware',2),('software',3),('both',4)))
_CnfTopFlowsReportSource_Type.__name__=_F
_CnfTopFlowsReportSource_Object=MibScalar
cnfTopFlowsReportSource=_CnfTopFlowsReportSource_Object((1,3,6,1,4,1,9,9,387,1,7,38),_CnfTopFlowsReportSource_Type())
cnfTopFlowsReportSource.setMaxAccess(_C)
if mibBuilder.loadTexts:cnfTopFlowsReportSource.setStatus(_B)
_CiscoNetflowMIBConform_ObjectIdentity=ObjectIdentity
ciscoNetflowMIBConform=_CiscoNetflowMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,387,2))
_CnfMIBCompliances_ObjectIdentity=ObjectIdentity
cnfMIBCompliances=_CnfMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,387,2,1))
_CnfMIBGroups_ObjectIdentity=ObjectIdentity
cnfMIBGroups=_CnfMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,387,2,2))
cnfCacheInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,387,2,2,1))
cnfCacheInfoGroup.setObjects(*((_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_Ad),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_Ah)))
if mibBuilder.loadTexts:cnfCacheInfoGroup.setStatus(_B)
cnfProtocolStatGroup=ObjectGroup((1,3,6,1,4,1,9,9,387,2,2,2))
cnfProtocolStatGroup.setObjects(*((_A,_Ai),(_A,_Aj),(_A,_Ak),(_A,_Al),(_A,_Am),(_A,_An),(_A,_Ao)))
if mibBuilder.loadTexts:cnfProtocolStatGroup.setStatus(_B)
cnfExportInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,387,2,2,3))
cnfExportInfoGroup.setObjects(*((_A,_Ap),(_A,_Aq),(_A,_Ar),(_A,_As),(_A,_At),(_A,_Au)))
if mibBuilder.loadTexts:cnfExportInfoGroup.setStatus(_B)
cnfExportStatisticsGroup=ObjectGroup((1,3,6,1,4,1,9,9,387,2,2,5))
cnfExportStatisticsGroup.setObjects(*((_A,_Av),(_A,_Aw),(_A,_Ax),(_A,_Ay),(_A,_Az),(_A,_A_)))
if mibBuilder.loadTexts:cnfExportStatisticsGroup.setStatus(_B)
cnfExportTemplateGroup=ObjectGroup((1,3,6,1,4,1,9,9,387,2,2,6))
cnfExportTemplateGroup.setObjects(*((_A,_B0),(_A,_B1),(_A,_B2),(_A,_B3),(_A,_B4),(_A,_B5),(_A,_B6),(_A,_B7),(_A,_B8)))
if mibBuilder.loadTexts:cnfExportTemplateGroup.setStatus(_B)
cnfTopFlowsGroup=ObjectGroup((1,3,6,1,4,1,9,9,387,2,2,7))
cnfTopFlowsGroup.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:cnfTopFlowsGroup.setStatus(_N)
cnfTopFlowsDataGroup1=ObjectGroup((1,3,6,1,4,1,9,9,387,2,2,8))
cnfTopFlowsDataGroup1.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_Y),(_A,_Z),(_A,_b),(_A,_c),(_A,_e),(_A,_f),(_A,_j),(_A,_k),(_A,_s),(_A,_x),(_A,_y)))
if mibBuilder.loadTexts:cnfTopFlowsDataGroup1.setStatus(_B)
cnfTopFlowsDataGroup2=ObjectGroup((1,3,6,1,4,1,9,9,387,2,2,9))
cnfTopFlowsDataGroup2.setObjects(*((_A,_a),(_A,_d),(_A,_g),(_A,_h),(_A,_i),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_t),(_A,_u),(_A,_v),(_A,_w)))
if mibBuilder.loadTexts:cnfTopFlowsDataGroup2.setStatus(_B)
cnfTopFlowsVlanGroup=ObjectGroup((1,3,6,1,4,1,9,9,387,2,2,10))
cnfTopFlowsVlanGroup.setObjects((_A,_B9))
if mibBuilder.loadTexts:cnfTopFlowsVlanGroup.setStatus(_B)
cnfTopFlowsControlGroup1=ObjectGroup((1,3,6,1,4,1,9,9,387,2,2,11))
cnfTopFlowsControlGroup1.setObjects(*((_A,_X),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO)))
if mibBuilder.loadTexts:cnfTopFlowsControlGroup1.setStatus(_B)
cnfTopFlowsControlGroup2=ObjectGroup((1,3,6,1,4,1,9,9,387,2,2,12))
cnfTopFlowsControlGroup2.setObjects(*((_A,_BA),(_A,_BB)))
if mibBuilder.loadTexts:cnfTopFlowsControlGroup2.setStatus(_B)
cnfMcastNetflowControlGroup=ObjectGroup((1,3,6,1,4,1,9,9,387,2,2,13))
cnfMcastNetflowControlGroup.setObjects(*((_A,_BC),(_A,_BD)))
if mibBuilder.loadTexts:cnfMcastNetflowControlGroup.setStatus(_B)
cnfBridgedFlowStatsCtrlGroup=ObjectGroup((1,3,6,1,4,1,9,9,387,2,2,14))
cnfBridgedFlowStatsCtrlGroup.setObjects(*((_A,_BE),(_A,_BF)))
if mibBuilder.loadTexts:cnfBridgedFlowStatsCtrlGroup.setStatus(_B)
cnfTopFlowsReportGenerateGroup=ObjectGroup((1,3,6,1,4,1,9,9,387,2,2,15))
cnfTopFlowsReportGenerateGroup.setObjects(*((_A,_BG),(_A,_BH)))
if mibBuilder.loadTexts:cnfTopFlowsReportGenerateGroup.setStatus(_B)
cnfMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,387,2,1,1))
cnfMIBCompliance.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_BI)))
if mibBuilder.loadTexts:cnfMIBCompliance.setStatus(_N)
cnfMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,9,9,387,2,1,2))
cnfMIBCompliance1.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S)))
if mibBuilder.loadTexts:cnfMIBCompliance1.setStatus(_N)
cnfMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,387,2,1,3))
cnfMIBCompliance2.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_AP),(_A,_AQ)))
if mibBuilder.loadTexts:cnfMIBCompliance2.setStatus(_N)
cnfMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,9,9,387,2,1,4))
cnfMIBCompliance3.setObjects(*((_A,_H),(_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_AP),(_A,_AQ),(_A,_BJ)))
if mibBuilder.loadTexts:cnfMIBCompliance3.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'NfInterfaceDirectionTypes':NfInterfaceDirectionTypes,'NfCacheTypes':NfCacheTypes,'NfProtocolTypes':NfProtocolTypes,'NfTemplateTypes':NfTemplateTypes,'NfTopFlowsSortTypes':NfTopFlowsSortTypes,'NfFlowDirectionTypes':NfFlowDirectionTypes,'ciscoNetflowMIB':ciscoNetflowMIB,'ciscoNetflowMIBNotifs':ciscoNetflowMIBNotifs,'ciscoNetflowMIBObjects':ciscoNetflowMIBObjects,'cnfCacheInfo':cnfCacheInfo,'cnfCIInterfaceTable':cnfCIInterfaceTable,'cnfCIInterfaceEntry':cnfCIInterfaceEntry,_AZ:cnfCINetflowEnable,_BC:cnfCIMcastNetflowEnable,'cnfCICacheTable':cnfCICacheTable,'cnfCICacheEntry':cnfCICacheEntry,_G:cnfCICacheType,_Aa:cnfCICacheEnable,_Ab:cnfCICacheEntries,_Ac:cnfCIActiveFlows,_Ad:cnfCIInactiveFlows,_Ae:cnfCIActiveTimeOut,_Af:cnfCIInactiveTimeOut,_Ag:cnfCIMinSourceMask,_Ah:cnfCIMinDestinationMask,'cnfCIBridgedFlowStatsCtrlTable':cnfCIBridgedFlowStatsCtrlTable,'cnfCIBridgedFlowStatsCtrlEntry':cnfCIBridgedFlowStatsCtrlEntry,_AS:cnfCIBridgedFlowVlan,_BE:cnfCIBridgedFlowStatsCrtEnable,_BF:cnfCIBridgedFlowStatsExpEnable,_BD:cnfCIMcastNetflowRPFFailedEnable,'cnfExportInfo':cnfExportInfo,'cnfEIExportInfoTable':cnfEIExportInfoTable,'cnfEIExportInfoEntry':cnfEIExportInfoEntry,_Ap:cnfEIExportVersion,_Aq:cnfEIPeerAS,_Ar:cnfEIOriginAS,_As:cnfEIBgpNextHop,_At:cnfEIMaxCollectors,'cnfEICollectorTable':cnfEICollectorTable,'cnfEICollectorEntry':cnfEICollectorEntry,_AT:cnfEICollectorAddressType,_AU:cnfEICollectorAddress,_AV:cnfEICollectorPort,_Au:cnfEICollectorStatus,'cnfExportStatistics':cnfExportStatistics,_Av:cnfESSampledPacket,_Aw:cnfESExportRate,_Ax:cnfESRecordsExported,_Ay:cnfESPktsExported,_Az:cnfESPktsFailed,_A_:cnfESPktsDropped,'cnfProtocolStatistics':cnfProtocolStatistics,_Ai:cnfPSPacketSizeDistribution,_Aj:cnfPSLastClearElapsedTime,'cnfPSProtocolStatTable':cnfPSProtocolStatTable,'cnfPSProtocolStatEntry':cnfPSProtocolStatEntry,_AW:cnfPSProtocolType,_Ak:cnfPSExpiredFlows,_Al:cnfPSPackets,_Am:cnfPSBytes,_An:cnfPSActive,_Ao:cnfPSInactive,'cnfExportTemplate':cnfExportTemplate,_B0:cnfTemplateOptionsFlag,'cnfTemplateTable':cnfTemplateTable,'cnfTemplateEntry':cnfTemplateEntry,_AX:cnfTemplateType,_B1:cnfTemplateAdded,_B2:cnfTemplateActive,_B3:cnfTemplateAgerPolls,'cnfTemplateExportInfoTable':cnfTemplateExportInfoTable,'cnfTemplateExportInfoEntry':cnfTemplateExportInfoEntry,_B4:cnfTemplateExportVer9Enable,_B5:cnfTemplateExportVer9TplTimeout,_B6:cnfTemplateExportVer9OptTimeout,_B7:cnfTemplateExportVer9TplRefreshRate,_B8:cnfTemplateExportVer9OptRefreshRate,'cnfTopFlows':cnfTopFlows,_U:cnfTopFlowsTimeStamp,_V:cnfTopFlowsTopN,_W:cnfTopFlowsAvailableFlows,_X:cnfTopFlowsMatchingFlows,_Y:cnfTopFlowsTotalFlows,_Z:cnfTopFlowsSortBy,_a:cnfTopFlowsCacheTimeout,'cnfTopFlowsTable':cnfTopFlowsTable,'cnfTopFlowsTableEntry':cnfTopFlowsTableEntry,_AY:cnfTopFlowsIndex,_b:cnfTopFlowsSrcAddressType,_c:cnfTopFlowsSrcAddress,_d:cnfTopFlowsSrcAddressMask,_e:cnfTopFlowsDstAddressType,_f:cnfTopFlowsDstAddress,_g:cnfTopFlowsDstAddressMask,_h:cnfTopFlowsNhAddressType,_i:cnfTopFlowsNhAddress,_j:cnfTopFlowsSrcPort,_k:cnfTopFlowsDstPort,_l:cnfTopFlowsSrcAS,_m:cnfTopFlowsDstAS,_n:cnfTopFlowsInputIfIndex,_o:cnfTopFlowsOutputIfIndex,_p:cnfTopFlowsFirstSwitched,_q:cnfTopFlowsLastSwitched,_r:cnfTopFlowsTOS,_s:cnfTopFlowsProtocol,_t:cnfTopFlowsTCPFlags,_u:cnfTopFlowsSamplerID,_v:cnfTopFlowsClassID,_w:cnfTopFlowsFlags,_x:cnfTopFlowsBytes,_y:cnfTopFlowsPackets,_B9:cnfTopFlowsVlan,_z:cnfTopFlowsMatchSrcAddressType,_A0:cnfTopFlowsMatchSrcAddress,_A1:cnfTopFlowsMatchSrcAddressMask,_A2:cnfTopFlowsMatchDstAddressType,_A3:cnfTopFlowsMatchDstAddress,_A4:cnfTopFlowsMatchDstAddressMask,_A5:cnfTopFlowsMatchNhAddressType,_A6:cnfTopFlowsMatchNhAddress,_A7:cnfTopFlowsMatchNhAddressMask,_A8:cnfTopFlowsMatchSrcPortLo,_A9:cnfTopFlowsMatchSrcPortHi,_AA:cnfTopFlowsMatchDstPortLo,_AB:cnfTopFlowsMatchDstPortHi,_AC:cnfTopFlowsMatchSrcAS,_AD:cnfTopFlowsMatchDstAS,_AE:cnfTopFlowsMatchInputIf,_AF:cnfTopFlowsMatchOutputIf,_AG:cnfTopFlowsMatchTOSByte,_AH:cnfTopFlowsMatchProtocol,_AI:cnfTopFlowsMatchSampler,_AJ:cnfTopFlowsMatchClass,_AK:cnfTopFlowsMatchMinPackets,_AL:cnfTopFlowsMatchMaxPackets,_AM:cnfTopFlowsMatchMinBytes,_AN:cnfTopFlowsMatchMaxBytes,_AO:cnfTopFlowsMatchDirection,_BA:cnfTopFlowsGenerate,_BB:cnfTopFlowsReportAvailable,_BG:cnfTopFlowsNextGenActionEffect,_BH:cnfTopFlowsReportSource,'ciscoNetflowMIBConform':ciscoNetflowMIBConform,'cnfMIBCompliances':cnfMIBCompliances,'cnfMIBCompliance':cnfMIBCompliance,'cnfMIBCompliance1':cnfMIBCompliance1,'cnfMIBCompliance2':cnfMIBCompliance2,'cnfMIBCompliance3':cnfMIBCompliance3,'cnfMIBGroups':cnfMIBGroups,_H:cnfCacheInfoGroup,_I:cnfProtocolStatGroup,_J:cnfExportInfoGroup,_K:cnfExportStatisticsGroup,_L:cnfExportTemplateGroup,_BI:cnfTopFlowsGroup,_O:cnfTopFlowsDataGroup1,_P:cnfTopFlowsDataGroup2,_Q:cnfTopFlowsVlanGroup,_R:cnfTopFlowsControlGroup1,_S:cnfTopFlowsControlGroup2,_AP:cnfMcastNetflowControlGroup,_AQ:cnfBridgedFlowStatsCtrlGroup,_BJ:cnfTopFlowsReportGenerateGroup})