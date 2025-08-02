_I='mwQosCodecTranslRuleTableIndex'
_H='not-accessible'
_G='mwQosRuleTableIndex'
_F='DisplayString'
_E='MERU-CONFIG-QOS-MIB'
_D='Integer32'
_C='read-write'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
mwConfiguration,=mibBuilder.importSymbols('MERU-SMI','mwConfiguration')
MwlAdmissionControl,MwlDropPolicy,MwlDscpType,MwlOnOffSwitch,MwlQosAction,MwlQosCodec,MwlQosCodecProtocol,MwlQosProtocol,MwlQosRulesMatchClass,MwlQosRulesMatchClassBits=mibBuilder.importSymbols('MERU-TC','MwlAdmissionControl','MwlDropPolicy','MwlDscpType','MwlOnOffSwitch','MwlQosAction','MwlQosCodec','MwlQosCodecProtocol','MwlQosProtocol','MwlQosRulesMatchClass','MwlQosRulesMatchClassBits')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval','TimeStamp','TruthValue')
mwConfigQoS=ModuleIdentity((1,3,6,1,4,1,15983,1,1,4,8))
_MwQosVars_ObjectIdentity=ObjectIdentity
mwQosVars=_MwQosVars_ObjectIdentity((1,3,6,1,4,1,15983,1,1,4,8,1))
_MwQosVarsQosOnOff_Type=MwlOnOffSwitch
_MwQosVarsQosOnOff_Object=MibScalar
mwQosVarsQosOnOff=_MwQosVarsQosOnOff_Object((1,3,6,1,4,1,15983,1,1,4,8,1,1),_MwQosVarsQosOnOff_Type())
mwQosVarsQosOnOff.setMaxAccess(_C)
if mibBuilder.loadTexts:mwQosVarsQosOnOff.setStatus(_A)
_MwQosVarsQosAdmissionControl_Type=MwlAdmissionControl
_MwQosVarsQosAdmissionControl_Object=MibScalar
mwQosVarsQosAdmissionControl=_MwQosVarsQosAdmissionControl_Object((1,3,6,1,4,1,15983,1,1,4,8,1,2),_MwQosVarsQosAdmissionControl_Type())
mwQosVarsQosAdmissionControl.setMaxAccess(_C)
if mibBuilder.loadTexts:mwQosVarsQosAdmissionControl.setStatus(_A)
_MwQosVarsQosDropPolicy_Type=MwlDropPolicy
_MwQosVarsQosDropPolicy_Object=MibScalar
mwQosVarsQosDropPolicy=_MwQosVarsQosDropPolicy_Object((1,3,6,1,4,1,15983,1,1,4,8,1,3),_MwQosVarsQosDropPolicy_Type())
mwQosVarsQosDropPolicy.setMaxAccess(_C)
if mibBuilder.loadTexts:mwQosVarsQosDropPolicy.setStatus(_A)
_MwQosVarsQosDefaultTimeToLive_Type=Unsigned32
_MwQosVarsQosDefaultTimeToLive_Object=MibScalar
mwQosVarsQosDefaultTimeToLive=_MwQosVarsQosDefaultTimeToLive_Object((1,3,6,1,4,1,15983,1,1,4,8,1,4),_MwQosVarsQosDefaultTimeToLive_Type())
mwQosVarsQosDefaultTimeToLive.setMaxAccess(_C)
if mibBuilder.loadTexts:mwQosVarsQosDefaultTimeToLive.setStatus(_A)
_MwQosVarsQosUdpTimeToLive_Type=Unsigned32
_MwQosVarsQosUdpTimeToLive_Object=MibScalar
mwQosVarsQosUdpTimeToLive=_MwQosVarsQosUdpTimeToLive_Object((1,3,6,1,4,1,15983,1,1,4,8,1,5),_MwQosVarsQosUdpTimeToLive_Type())
mwQosVarsQosUdpTimeToLive.setMaxAccess(_C)
if mibBuilder.loadTexts:mwQosVarsQosUdpTimeToLive.setStatus(_A)
_MwQosVarsQosTcpTimeToLive_Type=Unsigned32
_MwQosVarsQosTcpTimeToLive_Object=MibScalar
mwQosVarsQosTcpTimeToLive=_MwQosVarsQosTcpTimeToLive_Object((1,3,6,1,4,1,15983,1,1,4,8,1,6),_MwQosVarsQosTcpTimeToLive_Type())
mwQosVarsQosTcpTimeToLive.setMaxAccess(_C)
if mibBuilder.loadTexts:mwQosVarsQosTcpTimeToLive.setStatus(_A)
_MwQosVarsPercentBWScaling_Type=Unsigned32
_MwQosVarsPercentBWScaling_Object=MibScalar
mwQosVarsPercentBWScaling=_MwQosVarsPercentBWScaling_Object((1,3,6,1,4,1,15983,1,1,4,8,1,7),_MwQosVarsPercentBWScaling_Type())
mwQosVarsPercentBWScaling.setMaxAccess(_C)
if mibBuilder.loadTexts:mwQosVarsPercentBWScaling.setStatus(_A)
_MwQosVarsQosMaxCallsPerAp_Type=Unsigned32
_MwQosVarsQosMaxCallsPerAp_Object=MibScalar
mwQosVarsQosMaxCallsPerAp=_MwQosVarsQosMaxCallsPerAp_Object((1,3,6,1,4,1,15983,1,1,4,8,1,8),_MwQosVarsQosMaxCallsPerAp_Type())
mwQosVarsQosMaxCallsPerAp.setMaxAccess(_C)
if mibBuilder.loadTexts:mwQosVarsQosMaxCallsPerAp.setStatus(_A)
_MwQosVarsQosMaxCallsPerInterfRegion_Type=Unsigned32
_MwQosVarsQosMaxCallsPerInterfRegion_Object=MibScalar
mwQosVarsQosMaxCallsPerInterfRegion=_MwQosVarsQosMaxCallsPerInterfRegion_Object((1,3,6,1,4,1,15983,1,1,4,8,1,9),_MwQosVarsQosMaxCallsPerInterfRegion_Type())
mwQosVarsQosMaxCallsPerInterfRegion.setMaxAccess(_C)
if mibBuilder.loadTexts:mwQosVarsQosMaxCallsPerInterfRegion.setStatus(_A)
_MwQosVarsQosLoadBalanceMaxStationsPerAp_Type=Unsigned32
_MwQosVarsQosLoadBalanceMaxStationsPerAp_Object=MibScalar
mwQosVarsQosLoadBalanceMaxStationsPerAp=_MwQosVarsQosLoadBalanceMaxStationsPerAp_Object((1,3,6,1,4,1,15983,1,1,4,8,1,10),_MwQosVarsQosLoadBalanceMaxStationsPerAp_Type())
mwQosVarsQosLoadBalanceMaxStationsPerAp.setMaxAccess(_C)
if mibBuilder.loadTexts:mwQosVarsQosLoadBalanceMaxStationsPerAp.setStatus(_A)
_MwQosVarsQosLoadBalanceMaxStationsPerBssid_Type=Unsigned32
_MwQosVarsQosLoadBalanceMaxStationsPerBssid_Object=MibScalar
mwQosVarsQosLoadBalanceMaxStationsPerBssid=_MwQosVarsQosLoadBalanceMaxStationsPerBssid_Object((1,3,6,1,4,1,15983,1,1,4,8,1,11),_MwQosVarsQosLoadBalanceMaxStationsPerBssid_Type())
mwQosVarsQosLoadBalanceMaxStationsPerBssid.setMaxAccess(_C)
if mibBuilder.loadTexts:mwQosVarsQosLoadBalanceMaxStationsPerBssid.setStatus(_A)
_MwQosVarsQosLoadBalanceOverflow_Type=MwlOnOffSwitch
_MwQosVarsQosLoadBalanceOverflow_Object=MibScalar
mwQosVarsQosLoadBalanceOverflow=_MwQosVarsQosLoadBalanceOverflow_Object((1,3,6,1,4,1,15983,1,1,4,8,1,12),_MwQosVarsQosLoadBalanceOverflow_Type())
mwQosVarsQosLoadBalanceOverflow.setMaxAccess(_C)
if mibBuilder.loadTexts:mwQosVarsQosLoadBalanceOverflow.setStatus(_A)
_MwQosVarsQosMaxCallsPerBssid_Type=Unsigned32
_MwQosVarsQosMaxCallsPerBssid_Object=MibScalar
mwQosVarsQosMaxCallsPerBssid=_MwQosVarsQosMaxCallsPerBssid_Object((1,3,6,1,4,1,15983,1,1,4,8,1,13),_MwQosVarsQosMaxCallsPerBssid_Type())
mwQosVarsQosMaxCallsPerBssid.setMaxAccess(_C)
if mibBuilder.loadTexts:mwQosVarsQosMaxCallsPerBssid.setStatus(_A)
_MwQosVarsQosCacDeauth_Type=MwlOnOffSwitch
_MwQosVarsQosCacDeauth_Object=MibScalar
mwQosVarsQosCacDeauth=_MwQosVarsQosCacDeauth_Object((1,3,6,1,4,1,15983,1,1,4,8,1,14),_MwQosVarsQosCacDeauth_Type())
mwQosVarsQosCacDeauth.setMaxAccess(_C)
if mibBuilder.loadTexts:mwQosVarsQosCacDeauth.setStatus(_A)
_MwQosVarsQosStationAssignAge_Type=Unsigned32
_MwQosVarsQosStationAssignAge_Object=MibScalar
mwQosVarsQosStationAssignAge=_MwQosVarsQosStationAssignAge_Object((1,3,6,1,4,1,15983,1,1,4,8,1,15),_MwQosVarsQosStationAssignAge_Type())
mwQosVarsQosStationAssignAge.setMaxAccess(_C)
if mibBuilder.loadTexts:mwQosVarsQosStationAssignAge.setStatus(_A)
_MwQosVarsQosSipIdleTimeout_Type=Unsigned32
_MwQosVarsQosSipIdleTimeout_Object=MibScalar
mwQosVarsQosSipIdleTimeout=_MwQosVarsQosSipIdleTimeout_Object((1,3,6,1,4,1,15983,1,1,4,8,1,16),_MwQosVarsQosSipIdleTimeout_Type())
mwQosVarsQosSipIdleTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:mwQosVarsQosSipIdleTimeout.setStatus(_A)
_MwQosRuleTable_Object=MibTable
mwQosRuleTable=_MwQosRuleTable_Object((1,3,6,1,4,1,15983,1,1,4,8,2))
if mibBuilder.loadTexts:mwQosRuleTable.setStatus(_A)
_MwQosRuleEntry_Object=MibTableRow
mwQosRuleEntry=_MwQosRuleEntry_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1))
mwQosRuleEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:mwQosRuleEntry.setStatus(_A)
_MwQosRuleTableIndex_Type=Integer32
_MwQosRuleTableIndex_Object=MibTableColumn
mwQosRuleTableIndex=_MwQosRuleTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,1),_MwQosRuleTableIndex_Type())
mwQosRuleTableIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:mwQosRuleTableIndex.setStatus(_A)
_MwQosRuleId_Type=Unsigned32
_MwQosRuleId_Object=MibTableColumn
mwQosRuleId=_MwQosRuleId_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,2),_MwQosRuleId_Type())
mwQosRuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleId.setStatus(_A)
_MwQosRuleDscp_Type=MwlDscpType
_MwQosRuleDscp_Object=MibTableColumn
mwQosRuleDscp=_MwQosRuleDscp_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,3),_MwQosRuleDscp_Type())
mwQosRuleDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleDscp.setStatus(_A)
_MwQosRuleDstIp_Type=IpAddress
_MwQosRuleDstIp_Object=MibTableColumn
mwQosRuleDstIp=_MwQosRuleDstIp_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,4),_MwQosRuleDstIp_Type())
mwQosRuleDstIp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleDstIp.setStatus(_A)
_MwQosRuleSrcIp_Type=IpAddress
_MwQosRuleSrcIp_Object=MibTableColumn
mwQosRuleSrcIp=_MwQosRuleSrcIp_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,5),_MwQosRuleSrcIp_Type())
mwQosRuleSrcIp.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleSrcIp.setStatus(_A)
_MwQosRuleAction_Type=MwlQosAction
_MwQosRuleAction_Object=MibTableColumn
mwQosRuleAction=_MwQosRuleAction_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,6),_MwQosRuleAction_Type())
mwQosRuleAction.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleAction.setStatus(_A)
_MwQosRuleDstMask_Type=IpAddress
_MwQosRuleDstMask_Object=MibTableColumn
mwQosRuleDstMask=_MwQosRuleDstMask_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,7),_MwQosRuleDstMask_Type())
mwQosRuleDstMask.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleDstMask.setStatus(_A)
class _MwQosRuleDstPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MwQosRuleDstPort_Type.__name__=_D
_MwQosRuleDstPort_Object=MibTableColumn
mwQosRuleDstPort=_MwQosRuleDstPort_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,8),_MwQosRuleDstPort_Type())
mwQosRuleDstPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleDstPort.setStatus(_A)
_MwQosRuleSrcMask_Type=IpAddress
_MwQosRuleSrcMask_Object=MibTableColumn
mwQosRuleSrcMask=_MwQosRuleSrcMask_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,9),_MwQosRuleSrcMask_Type())
mwQosRuleSrcMask.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleSrcMask.setStatus(_A)
class _MwQosRuleSrcPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MwQosRuleSrcPort_Type.__name__=_D
_MwQosRuleSrcPort_Object=MibTableColumn
mwQosRuleSrcPort=_MwQosRuleSrcPort_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,10),_MwQosRuleSrcPort_Type())
mwQosRuleSrcPort.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleSrcPort.setStatus(_A)
_MwQosRuleProtocol_Type=MwlQosProtocol
_MwQosRuleProtocol_Object=MibTableColumn
mwQosRuleProtocol=_MwQosRuleProtocol_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,11),_MwQosRuleProtocol_Type())
mwQosRuleProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleProtocol.setStatus(_A)
class _MwQosRulePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8))
_MwQosRulePriority_Type.__name__=_D
_MwQosRulePriority_Object=MibTableColumn
mwQosRulePriority=_MwQosRulePriority_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,12),_MwQosRulePriority_Type())
mwQosRulePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRulePriority.setStatus(_A)
_MwQosRuleIdUfcFlag_Type=MwlQosRulesMatchClass
_MwQosRuleIdUfcFlag_Object=MibTableColumn
mwQosRuleIdUfcFlag=_MwQosRuleIdUfcFlag_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,13),_MwQosRuleIdUfcFlag_Type())
mwQosRuleIdUfcFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleIdUfcFlag.setStatus(_A)
_MwQosRuleDstIpFlag_Type=MwlQosRulesMatchClassBits
_MwQosRuleDstIpFlag_Object=MibTableColumn
mwQosRuleDstIpFlag=_MwQosRuleDstIpFlag_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,14),_MwQosRuleDstIpFlag_Type())
mwQosRuleDstIpFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleDstIpFlag.setStatus(_A)
_MwQosRuleSrcIpFlag_Type=MwlQosRulesMatchClassBits
_MwQosRuleSrcIpFlag_Object=MibTableColumn
mwQosRuleSrcIpFlag=_MwQosRuleSrcIpFlag_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,15),_MwQosRuleSrcIpFlag_Type())
mwQosRuleSrcIpFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleSrcIpFlag.setStatus(_A)
class _MwQosRuleL4Protocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_MwQosRuleL4Protocol_Type.__name__=_D
_MwQosRuleL4Protocol_Object=MibTableColumn
mwQosRuleL4Protocol=_MwQosRuleL4Protocol_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,16),_MwQosRuleL4Protocol_Type())
mwQosRuleL4Protocol.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleL4Protocol.setStatus(_A)
_MwQosRuleDstPortFlag_Type=MwlQosRulesMatchClassBits
_MwQosRuleDstPortFlag_Object=MibTableColumn
mwQosRuleDstPortFlag=_MwQosRuleDstPortFlag_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,18),_MwQosRuleDstPortFlag_Type())
mwQosRuleDstPortFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleDstPortFlag.setStatus(_A)
_MwQosRuleSrcPortFlag_Type=MwlQosRulesMatchClassBits
_MwQosRuleSrcPortFlag_Object=MibTableColumn
mwQosRuleSrcPortFlag=_MwQosRuleSrcPortFlag_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,19),_MwQosRuleSrcPortFlag_Type())
mwQosRuleSrcPortFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleSrcPortFlag.setStatus(_A)
_MwQosRuleDstIpUfcFlag_Type=MwlQosRulesMatchClassBits
_MwQosRuleDstIpUfcFlag_Object=MibTableColumn
mwQosRuleDstIpUfcFlag=_MwQosRuleDstIpUfcFlag_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,20),_MwQosRuleDstIpUfcFlag_Type())
mwQosRuleDstIpUfcFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleDstIpUfcFlag.setStatus(_A)
_MwQosRuleSrcIpUfcFlag_Type=MwlQosRulesMatchClassBits
_MwQosRuleSrcIpUfcFlag_Object=MibTableColumn
mwQosRuleSrcIpUfcFlag=_MwQosRuleSrcIpUfcFlag_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,21),_MwQosRuleSrcIpUfcFlag_Type())
mwQosRuleSrcIpUfcFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleSrcIpUfcFlag.setStatus(_A)
_MwQosRuleAvgPacketRate_Type=Unsigned32
_MwQosRuleAvgPacketRate_Object=MibTableColumn
mwQosRuleAvgPacketRate=_MwQosRuleAvgPacketRate_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,22),_MwQosRuleAvgPacketRate_Type())
mwQosRuleAvgPacketRate.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleAvgPacketRate.setStatus(_A)
_MwQosRuleDstPortUfcFlag_Type=MwlQosRulesMatchClassBits
_MwQosRuleDstPortUfcFlag_Object=MibTableColumn
mwQosRuleDstPortUfcFlag=_MwQosRuleDstPortUfcFlag_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,23),_MwQosRuleDstPortUfcFlag_Type())
mwQosRuleDstPortUfcFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleDstPortUfcFlag.setStatus(_A)
_MwQosRuleSrcPortUfcFlag_Type=MwlQosRulesMatchClassBits
_MwQosRuleSrcPortUfcFlag_Object=MibTableColumn
mwQosRuleSrcPortUfcFlag=_MwQosRuleSrcPortUfcFlag_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,24),_MwQosRuleSrcPortUfcFlag_Type())
mwQosRuleSrcPortUfcFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleSrcPortUfcFlag.setStatus(_A)
_MwQosRuleL4ProtocolFlag_Type=MwlQosRulesMatchClassBits
_MwQosRuleL4ProtocolFlag_Object=MibTableColumn
mwQosRuleL4ProtocolFlag=_MwQosRuleL4ProtocolFlag_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,25),_MwQosRuleL4ProtocolFlag_Type())
mwQosRuleL4ProtocolFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleL4ProtocolFlag.setStatus(_A)
_MwQosRuleTrafficControl_Type=MwlOnOffSwitch
_MwQosRuleTrafficControl_Object=MibTableColumn
mwQosRuleTrafficControl=_MwQosRuleTrafficControl_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,26),_MwQosRuleTrafficControl_Type())
mwQosRuleTrafficControl.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleTrafficControl.setStatus(_A)
_MwQosRuleLogging_Type=MwlOnOffSwitch
_MwQosRuleLogging_Object=MibTableColumn
mwQosRuleLogging=_MwQosRuleLogging_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,27),_MwQosRuleLogging_Type())
mwQosRuleLogging.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleLogging.setStatus(_A)
_MwQosRulePacketMinLength_Type=Unsigned32
_MwQosRulePacketMinLength_Object=MibTableColumn
mwQosRulePacketMinLength=_MwQosRulePacketMinLength_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,28),_MwQosRulePacketMinLength_Type())
mwQosRulePacketMinLength.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRulePacketMinLength.setStatus(_A)
_MwQosRulePacketMaxLength_Type=Unsigned32
_MwQosRulePacketMaxLength_Object=MibTableColumn
mwQosRulePacketMaxLength=_MwQosRulePacketMaxLength_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,29),_MwQosRulePacketMaxLength_Type())
mwQosRulePacketMaxLength.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRulePacketMaxLength.setStatus(_A)
_MwQosRuleTokenBucketRate_Type=Unsigned32
_MwQosRuleTokenBucketRate_Object=MibTableColumn
mwQosRuleTokenBucketRate=_MwQosRuleTokenBucketRate_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,30),_MwQosRuleTokenBucketRate_Type())
mwQosRuleTokenBucketRate.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleTokenBucketRate.setStatus(_A)
class _MwQosRuleFirewallFilterId_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_MwQosRuleFirewallFilterId_Type.__name__=_F
_MwQosRuleFirewallFilterId_Object=MibTableColumn
mwQosRuleFirewallFilterId=_MwQosRuleFirewallFilterId_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,31),_MwQosRuleFirewallFilterId_Type())
mwQosRuleFirewallFilterId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleFirewallFilterId.setStatus(_A)
_MwQosRuleL4ProtocolUfcFlag_Type=MwlQosRulesMatchClassBits
_MwQosRuleL4ProtocolUfcFlag_Object=MibTableColumn
mwQosRuleL4ProtocolUfcFlag=_MwQosRuleL4ProtocolUfcFlag_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,32),_MwQosRuleL4ProtocolUfcFlag_Type())
mwQosRuleL4ProtocolUfcFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleL4ProtocolUfcFlag.setStatus(_A)
_MwQosRulePacketMinLengthFlag_Type=MwlQosRulesMatchClassBits
_MwQosRulePacketMinLengthFlag_Object=MibTableColumn
mwQosRulePacketMinLengthFlag=_MwQosRulePacketMinLengthFlag_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,33),_MwQosRulePacketMinLengthFlag_Type())
mwQosRulePacketMinLengthFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRulePacketMinLengthFlag.setStatus(_A)
_MwQosRuleFirewallFilterIdFlag_Type=MwlQosRulesMatchClassBits
_MwQosRuleFirewallFilterIdFlag_Object=MibTableColumn
mwQosRuleFirewallFilterIdFlag=_MwQosRuleFirewallFilterIdFlag_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,34),_MwQosRuleFirewallFilterIdFlag_Type())
mwQosRuleFirewallFilterIdFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleFirewallFilterIdFlag.setStatus(_A)
_MwQosRulePacketMinLengthUfcFlag_Type=MwlQosRulesMatchClassBits
_MwQosRulePacketMinLengthUfcFlag_Object=MibTableColumn
mwQosRulePacketMinLengthUfcFlag=_MwQosRulePacketMinLengthUfcFlag_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,35),_MwQosRulePacketMinLengthUfcFlag_Type())
mwQosRulePacketMinLengthUfcFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRulePacketMinLengthUfcFlag.setStatus(_A)
_MwQosRuleFirewallFilterIdUfcFlag_Type=MwlQosRulesMatchClassBits
_MwQosRuleFirewallFilterIdUfcFlag_Object=MibTableColumn
mwQosRuleFirewallFilterIdUfcFlag=_MwQosRuleFirewallFilterIdUfcFlag_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,36),_MwQosRuleFirewallFilterIdUfcFlag_Type())
mwQosRuleFirewallFilterIdUfcFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleFirewallFilterIdUfcFlag.setStatus(_A)
class _MwQosRuleLoggingFrequency_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,60))
_MwQosRuleLoggingFrequency_Type.__name__=_D
_MwQosRuleLoggingFrequency_Object=MibTableColumn
mwQosRuleLoggingFrequency=_MwQosRuleLoggingFrequency_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,37),_MwQosRuleLoggingFrequency_Type())
mwQosRuleLoggingFrequency.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleLoggingFrequency.setStatus(_A)
_MwQosRuleRowStatus_Type=RowStatus
_MwQosRuleRowStatus_Object=MibTableColumn
mwQosRuleRowStatus=_MwQosRuleRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,8,2,1,48),_MwQosRuleRowStatus_Type())
mwQosRuleRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosRuleRowStatus.setStatus(_A)
_MwQosCodecTranslRuleTable_Object=MibTable
mwQosCodecTranslRuleTable=_MwQosCodecTranslRuleTable_Object((1,3,6,1,4,1,15983,1,1,4,8,3))
if mibBuilder.loadTexts:mwQosCodecTranslRuleTable.setStatus(_A)
_MwQosCodecTranslRuleEntry_Object=MibTableRow
mwQosCodecTranslRuleEntry=_MwQosCodecTranslRuleEntry_Object((1,3,6,1,4,1,15983,1,1,4,8,3,1))
mwQosCodecTranslRuleEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:mwQosCodecTranslRuleEntry.setStatus(_A)
_MwQosCodecTranslRuleTableIndex_Type=Integer32
_MwQosCodecTranslRuleTableIndex_Object=MibTableColumn
mwQosCodecTranslRuleTableIndex=_MwQosCodecTranslRuleTableIndex_Object((1,3,6,1,4,1,15983,1,1,4,8,3,1,1),_MwQosCodecTranslRuleTableIndex_Type())
mwQosCodecTranslRuleTableIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:mwQosCodecTranslRuleTableIndex.setStatus(_A)
_MwQosCodecTranslRuleId_Type=Unsigned32
_MwQosCodecTranslRuleId_Object=MibTableColumn
mwQosCodecTranslRuleId=_MwQosCodecTranslRuleId_Object((1,3,6,1,4,1,15983,1,1,4,8,3,1,2),_MwQosCodecTranslRuleId_Type())
mwQosCodecTranslRuleId.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosCodecTranslRuleId.setStatus(_A)
_MwQosCodecTranslRuleQosCtrProtocol_Type=MwlQosCodecProtocol
_MwQosCodecTranslRuleQosCtrProtocol_Object=MibTableColumn
mwQosCodecTranslRuleQosCtrProtocol=_MwQosCodecTranslRuleQosCtrProtocol_Object((1,3,6,1,4,1,15983,1,1,4,8,3,1,3),_MwQosCodecTranslRuleQosCtrProtocol_Type())
mwQosCodecTranslRuleQosCtrProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosCodecTranslRuleQosCtrProtocol.setStatus(_A)
_MwQosCodecTranslRuleQosCtrCodecEnum_Type=MwlQosCodec
_MwQosCodecTranslRuleQosCtrCodecEnum_Object=MibTableColumn
mwQosCodecTranslRuleQosCtrCodecEnum=_MwQosCodecTranslRuleQosCtrCodecEnum_Object((1,3,6,1,4,1,15983,1,1,4,8,3,1,4),_MwQosCodecTranslRuleQosCtrCodecEnum_Type())
mwQosCodecTranslRuleQosCtrCodecEnum.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosCodecTranslRuleQosCtrCodecEnum.setStatus(_A)
_MwQosCodecTranslRuleQosCtrRspecRate_Type=Unsigned32
_MwQosCodecTranslRuleQosCtrRspecRate_Object=MibTableColumn
mwQosCodecTranslRuleQosCtrRspecRate=_MwQosCodecTranslRuleQosCtrRspecRate_Object((1,3,6,1,4,1,15983,1,1,4,8,3,1,5),_MwQosCodecTranslRuleQosCtrRspecRate_Type())
mwQosCodecTranslRuleQosCtrRspecRate.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosCodecTranslRuleQosCtrRspecRate.setStatus(_A)
_MwQosCodecTranslRuleQosCtrRspecSlack_Type=Unsigned32
_MwQosCodecTranslRuleQosCtrRspecSlack_Object=MibTableColumn
mwQosCodecTranslRuleQosCtrRspecSlack=_MwQosCodecTranslRuleQosCtrRspecSlack_Object((1,3,6,1,4,1,15983,1,1,4,8,3,1,6),_MwQosCodecTranslRuleQosCtrRspecSlack_Type())
mwQosCodecTranslRuleQosCtrRspecSlack.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosCodecTranslRuleQosCtrRspecSlack.setStatus(_A)
_MwQosCodecTranslRuleQosCtrSampleRate_Type=Unsigned32
_MwQosCodecTranslRuleQosCtrSampleRate_Object=MibTableColumn
mwQosCodecTranslRuleQosCtrSampleRate=_MwQosCodecTranslRuleQosCtrSampleRate_Object((1,3,6,1,4,1,15983,1,1,4,8,3,1,7),_MwQosCodecTranslRuleQosCtrSampleRate_Type())
mwQosCodecTranslRuleQosCtrSampleRate.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosCodecTranslRuleQosCtrSampleRate.setStatus(_A)
_MwQosCodecTranslRuleQosCtrTspecPeakRate_Type=Unsigned32
_MwQosCodecTranslRuleQosCtrTspecPeakRate_Object=MibTableColumn
mwQosCodecTranslRuleQosCtrTspecPeakRate=_MwQosCodecTranslRuleQosCtrTspecPeakRate_Object((1,3,6,1,4,1,15983,1,1,4,8,3,1,8),_MwQosCodecTranslRuleQosCtrTspecPeakRate_Type())
mwQosCodecTranslRuleQosCtrTspecPeakRate.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosCodecTranslRuleQosCtrTspecPeakRate.setStatus(_A)
_MwQosCodecTranslRuleQosCtrTspecMinPolicedUnit_Type=Unsigned32
_MwQosCodecTranslRuleQosCtrTspecMinPolicedUnit_Object=MibTableColumn
mwQosCodecTranslRuleQosCtrTspecMinPolicedUnit=_MwQosCodecTranslRuleQosCtrTspecMinPolicedUnit_Object((1,3,6,1,4,1,15983,1,1,4,8,3,1,9),_MwQosCodecTranslRuleQosCtrTspecMinPolicedUnit_Type())
mwQosCodecTranslRuleQosCtrTspecMinPolicedUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosCodecTranslRuleQosCtrTspecMinPolicedUnit.setStatus(_A)
_MwQosCodecTranslRuleQosCtrTspecTokenBucketRate_Type=Unsigned32
_MwQosCodecTranslRuleQosCtrTspecTokenBucketRate_Object=MibTableColumn
mwQosCodecTranslRuleQosCtrTspecTokenBucketRate=_MwQosCodecTranslRuleQosCtrTspecTokenBucketRate_Object((1,3,6,1,4,1,15983,1,1,4,8,3,1,10),_MwQosCodecTranslRuleQosCtrTspecTokenBucketRate_Type())
mwQosCodecTranslRuleQosCtrTspecTokenBucketRate.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosCodecTranslRuleQosCtrTspecTokenBucketRate.setStatus(_A)
_MwQosCodecTranslRuleQosCtrTspecTokenBucketSize_Type=Unsigned32
_MwQosCodecTranslRuleQosCtrTspecTokenBucketSize_Object=MibTableColumn
mwQosCodecTranslRuleQosCtrTspecTokenBucketSize=_MwQosCodecTranslRuleQosCtrTspecTokenBucketSize_Object((1,3,6,1,4,1,15983,1,1,4,8,3,1,11),_MwQosCodecTranslRuleQosCtrTspecTokenBucketSize_Type())
mwQosCodecTranslRuleQosCtrTspecTokenBucketSize.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosCodecTranslRuleQosCtrTspecTokenBucketSize.setStatus(_A)
_MwQosCodecTranslRuleQosCtrTspecMaxDatagramSize_Type=Unsigned32
_MwQosCodecTranslRuleQosCtrTspecMaxDatagramSize_Object=MibTableColumn
mwQosCodecTranslRuleQosCtrTspecMaxDatagramSize=_MwQosCodecTranslRuleQosCtrTspecMaxDatagramSize_Object((1,3,6,1,4,1,15983,1,1,4,8,3,1,12),_MwQosCodecTranslRuleQosCtrTspecMaxDatagramSize_Type())
mwQosCodecTranslRuleQosCtrTspecMaxDatagramSize.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosCodecTranslRuleQosCtrTspecMaxDatagramSize.setStatus(_A)
_MwQosCodecTranslRuleRowStatus_Type=RowStatus
_MwQosCodecTranslRuleRowStatus_Object=MibTableColumn
mwQosCodecTranslRuleRowStatus=_MwQosCodecTranslRuleRowStatus_Object((1,3,6,1,4,1,15983,1,1,4,8,3,1,14),_MwQosCodecTranslRuleRowStatus_Type())
mwQosCodecTranslRuleRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:mwQosCodecTranslRuleRowStatus.setStatus(_A)
_MwDscpMarkingMgmtPkts_ObjectIdentity=ObjectIdentity
mwDscpMarkingMgmtPkts=_MwDscpMarkingMgmtPkts_ObjectIdentity((1,3,6,1,4,1,15983,1,1,4,8,4))
_MwDscpMarkingMgmtPktsDscpControllerToEzRF_Type=MwlDscpType
_MwDscpMarkingMgmtPktsDscpControllerToEzRF_Object=MibScalar
mwDscpMarkingMgmtPktsDscpControllerToEzRF=_MwDscpMarkingMgmtPktsDscpControllerToEzRF_Object((1,3,6,1,4,1,15983,1,1,4,8,4,2),_MwDscpMarkingMgmtPktsDscpControllerToEzRF_Type())
mwDscpMarkingMgmtPktsDscpControllerToEzRF.setMaxAccess(_C)
if mibBuilder.loadTexts:mwDscpMarkingMgmtPktsDscpControllerToEzRF.setStatus(_A)
_MwDscpMarkingMgmtPktsDscpControllerToAp_Type=MwlDscpType
_MwDscpMarkingMgmtPktsDscpControllerToAp_Object=MibScalar
mwDscpMarkingMgmtPktsDscpControllerToAp=_MwDscpMarkingMgmtPktsDscpControllerToAp_Object((1,3,6,1,4,1,15983,1,1,4,8,4,3),_MwDscpMarkingMgmtPktsDscpControllerToAp_Type())
mwDscpMarkingMgmtPktsDscpControllerToAp.setMaxAccess(_C)
if mibBuilder.loadTexts:mwDscpMarkingMgmtPktsDscpControllerToAp.setStatus(_A)
_MwDscpMarkingMgmtPktsDscpApToController_Type=MwlDscpType
_MwDscpMarkingMgmtPktsDscpApToController_Object=MibScalar
mwDscpMarkingMgmtPktsDscpApToController=_MwDscpMarkingMgmtPktsDscpApToController_Object((1,3,6,1,4,1,15983,1,1,4,8,4,4),_MwDscpMarkingMgmtPktsDscpApToController_Type())
mwDscpMarkingMgmtPktsDscpApToController.setMaxAccess(_C)
if mibBuilder.loadTexts:mwDscpMarkingMgmtPktsDscpApToController.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'mwConfigQoS':mwConfigQoS,'mwQosVars':mwQosVars,'mwQosVarsQosOnOff':mwQosVarsQosOnOff,'mwQosVarsQosAdmissionControl':mwQosVarsQosAdmissionControl,'mwQosVarsQosDropPolicy':mwQosVarsQosDropPolicy,'mwQosVarsQosDefaultTimeToLive':mwQosVarsQosDefaultTimeToLive,'mwQosVarsQosUdpTimeToLive':mwQosVarsQosUdpTimeToLive,'mwQosVarsQosTcpTimeToLive':mwQosVarsQosTcpTimeToLive,'mwQosVarsPercentBWScaling':mwQosVarsPercentBWScaling,'mwQosVarsQosMaxCallsPerAp':mwQosVarsQosMaxCallsPerAp,'mwQosVarsQosMaxCallsPerInterfRegion':mwQosVarsQosMaxCallsPerInterfRegion,'mwQosVarsQosLoadBalanceMaxStationsPerAp':mwQosVarsQosLoadBalanceMaxStationsPerAp,'mwQosVarsQosLoadBalanceMaxStationsPerBssid':mwQosVarsQosLoadBalanceMaxStationsPerBssid,'mwQosVarsQosLoadBalanceOverflow':mwQosVarsQosLoadBalanceOverflow,'mwQosVarsQosMaxCallsPerBssid':mwQosVarsQosMaxCallsPerBssid,'mwQosVarsQosCacDeauth':mwQosVarsQosCacDeauth,'mwQosVarsQosStationAssignAge':mwQosVarsQosStationAssignAge,'mwQosVarsQosSipIdleTimeout':mwQosVarsQosSipIdleTimeout,'mwQosRuleTable':mwQosRuleTable,'mwQosRuleEntry':mwQosRuleEntry,_G:mwQosRuleTableIndex,'mwQosRuleId':mwQosRuleId,'mwQosRuleDscp':mwQosRuleDscp,'mwQosRuleDstIp':mwQosRuleDstIp,'mwQosRuleSrcIp':mwQosRuleSrcIp,'mwQosRuleAction':mwQosRuleAction,'mwQosRuleDstMask':mwQosRuleDstMask,'mwQosRuleDstPort':mwQosRuleDstPort,'mwQosRuleSrcMask':mwQosRuleSrcMask,'mwQosRuleSrcPort':mwQosRuleSrcPort,'mwQosRuleProtocol':mwQosRuleProtocol,'mwQosRulePriority':mwQosRulePriority,'mwQosRuleIdUfcFlag':mwQosRuleIdUfcFlag,'mwQosRuleDstIpFlag':mwQosRuleDstIpFlag,'mwQosRuleSrcIpFlag':mwQosRuleSrcIpFlag,'mwQosRuleL4Protocol':mwQosRuleL4Protocol,'mwQosRuleDstPortFlag':mwQosRuleDstPortFlag,'mwQosRuleSrcPortFlag':mwQosRuleSrcPortFlag,'mwQosRuleDstIpUfcFlag':mwQosRuleDstIpUfcFlag,'mwQosRuleSrcIpUfcFlag':mwQosRuleSrcIpUfcFlag,'mwQosRuleAvgPacketRate':mwQosRuleAvgPacketRate,'mwQosRuleDstPortUfcFlag':mwQosRuleDstPortUfcFlag,'mwQosRuleSrcPortUfcFlag':mwQosRuleSrcPortUfcFlag,'mwQosRuleL4ProtocolFlag':mwQosRuleL4ProtocolFlag,'mwQosRuleTrafficControl':mwQosRuleTrafficControl,'mwQosRuleLogging':mwQosRuleLogging,'mwQosRulePacketMinLength':mwQosRulePacketMinLength,'mwQosRulePacketMaxLength':mwQosRulePacketMaxLength,'mwQosRuleTokenBucketRate':mwQosRuleTokenBucketRate,'mwQosRuleFirewallFilterId':mwQosRuleFirewallFilterId,'mwQosRuleL4ProtocolUfcFlag':mwQosRuleL4ProtocolUfcFlag,'mwQosRulePacketMinLengthFlag':mwQosRulePacketMinLengthFlag,'mwQosRuleFirewallFilterIdFlag':mwQosRuleFirewallFilterIdFlag,'mwQosRulePacketMinLengthUfcFlag':mwQosRulePacketMinLengthUfcFlag,'mwQosRuleFirewallFilterIdUfcFlag':mwQosRuleFirewallFilterIdUfcFlag,'mwQosRuleLoggingFrequency':mwQosRuleLoggingFrequency,'mwQosRuleRowStatus':mwQosRuleRowStatus,'mwQosCodecTranslRuleTable':mwQosCodecTranslRuleTable,'mwQosCodecTranslRuleEntry':mwQosCodecTranslRuleEntry,_I:mwQosCodecTranslRuleTableIndex,'mwQosCodecTranslRuleId':mwQosCodecTranslRuleId,'mwQosCodecTranslRuleQosCtrProtocol':mwQosCodecTranslRuleQosCtrProtocol,'mwQosCodecTranslRuleQosCtrCodecEnum':mwQosCodecTranslRuleQosCtrCodecEnum,'mwQosCodecTranslRuleQosCtrRspecRate':mwQosCodecTranslRuleQosCtrRspecRate,'mwQosCodecTranslRuleQosCtrRspecSlack':mwQosCodecTranslRuleQosCtrRspecSlack,'mwQosCodecTranslRuleQosCtrSampleRate':mwQosCodecTranslRuleQosCtrSampleRate,'mwQosCodecTranslRuleQosCtrTspecPeakRate':mwQosCodecTranslRuleQosCtrTspecPeakRate,'mwQosCodecTranslRuleQosCtrTspecMinPolicedUnit':mwQosCodecTranslRuleQosCtrTspecMinPolicedUnit,'mwQosCodecTranslRuleQosCtrTspecTokenBucketRate':mwQosCodecTranslRuleQosCtrTspecTokenBucketRate,'mwQosCodecTranslRuleQosCtrTspecTokenBucketSize':mwQosCodecTranslRuleQosCtrTspecTokenBucketSize,'mwQosCodecTranslRuleQosCtrTspecMaxDatagramSize':mwQosCodecTranslRuleQosCtrTspecMaxDatagramSize,'mwQosCodecTranslRuleRowStatus':mwQosCodecTranslRuleRowStatus,'mwDscpMarkingMgmtPkts':mwDscpMarkingMgmtPkts,'mwDscpMarkingMgmtPktsDscpControllerToEzRF':mwDscpMarkingMgmtPktsDscpControllerToEzRF,'mwDscpMarkingMgmtPktsDscpControllerToAp':mwDscpMarkingMgmtPktsDscpControllerToAp,'mwDscpMarkingMgmtPktsDscpApToController':mwDscpMarkingMgmtPktsDscpApToController})