_M='oacZbfwFlowsGlobalIx'
_L='oacZbfwFlowsTableIx'
_K='oacZbfwZonePairsGlobalIx'
_J='oacZbfwZonePairsTableIx'
_I='oacZbfwPolicyRulesGlobalIx'
_H='oacZbfwPolicyRulesTableIx'
_G='oacZbfwPacketsGlobalIx'
_F='oacZbfwRtrConnPerfGlobalIx'
_E='Integer32'
_D='not-accessible'
_C='OA-ZBFW-STATUS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
oacExpIMZbFw,oacMIBModules=mibBuilder.importSymbols('ONEACCESS-GLOBAL-REG','oacExpIMZbFw','oacMIBModules')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
oacZbfwStatusMIB=ModuleIdentity((1,3,6,1,4,1,13191,1,100,2003))
class TableIndex(Unsigned32):0
_OacZbfw_ObjectIdentity=ObjectIdentity
oacZbfw=_OacZbfw_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,9,3131))
_OacZbfwPerf_ObjectIdentity=ObjectIdentity
oacZbfwPerf=_OacZbfwPerf_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,9,3131,12))
_OacZbfwRtrConnPerf_ObjectIdentity=ObjectIdentity
oacZbfwRtrConnPerf=_OacZbfwRtrConnPerf_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,9,3131,12,40))
_OacZbfwRtrConnPerfSSCTable_Object=MibTable
oacZbfwRtrConnPerfSSCTable=_OacZbfwRtrConnPerfSSCTable_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,40,1))
if mibBuilder.loadTexts:oacZbfwRtrConnPerfSSCTable.setStatus(_A)
_OacZbfwRtrConnPerfEntry_Object=MibTableRow
oacZbfwRtrConnPerfEntry=_OacZbfwRtrConnPerfEntry_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,40,1,1))
oacZbfwRtrConnPerfEntry.setIndexNames((1,_C,_F))
if mibBuilder.loadTexts:oacZbfwRtrConnPerfEntry.setStatus(_A)
_OacZbfwRouterConnectionsCreated_Type=Counter32
_OacZbfwRouterConnectionsCreated_Object=MibTableColumn
oacZbfwRouterConnectionsCreated=_OacZbfwRouterConnectionsCreated_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,40,1,1,1),_OacZbfwRouterConnectionsCreated_Type())
oacZbfwRouterConnectionsCreated.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwRouterConnectionsCreated.setStatus(_A)
_OacZbfwRouterConnectionsClosed_Type=Counter32
_OacZbfwRouterConnectionsClosed_Object=MibTableColumn
oacZbfwRouterConnectionsClosed=_OacZbfwRouterConnectionsClosed_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,40,1,1,2),_OacZbfwRouterConnectionsClosed_Type())
oacZbfwRouterConnectionsClosed.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwRouterConnectionsClosed.setStatus(_A)
_OacZbfwRouterConnectionsTimedOut_Type=Counter32
_OacZbfwRouterConnectionsTimedOut_Object=MibTableColumn
oacZbfwRouterConnectionsTimedOut=_OacZbfwRouterConnectionsTimedOut_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,40,1,1,3),_OacZbfwRouterConnectionsTimedOut_Type())
oacZbfwRouterConnectionsTimedOut.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwRouterConnectionsTimedOut.setStatus(_A)
_OacZbfwRouterConnectionsMax_Type=Counter32
_OacZbfwRouterConnectionsMax_Object=MibTableColumn
oacZbfwRouterConnectionsMax=_OacZbfwRouterConnectionsMax_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,40,1,1,4),_OacZbfwRouterConnectionsMax_Type())
oacZbfwRouterConnectionsMax.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwRouterConnectionsMax.setStatus(_A)
_OacZbfwRouterConnectionsMaxUsed_Type=Counter32
_OacZbfwRouterConnectionsMaxUsed_Object=MibTableColumn
oacZbfwRouterConnectionsMaxUsed=_OacZbfwRouterConnectionsMaxUsed_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,40,1,1,5),_OacZbfwRouterConnectionsMaxUsed_Type())
oacZbfwRouterConnectionsMaxUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwRouterConnectionsMaxUsed.setStatus(_A)
_OacZbfwRouterConnectionsUsed_Type=Counter32
_OacZbfwRouterConnectionsUsed_Object=MibTableColumn
oacZbfwRouterConnectionsUsed=_OacZbfwRouterConnectionsUsed_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,40,1,1,6),_OacZbfwRouterConnectionsUsed_Type())
oacZbfwRouterConnectionsUsed.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwRouterConnectionsUsed.setStatus(_A)
_OacZbfwRtrConnPerfGlobalIx_Type=SnmpAdminString
_OacZbfwRtrConnPerfGlobalIx_Object=MibTableColumn
oacZbfwRtrConnPerfGlobalIx=_OacZbfwRtrConnPerfGlobalIx_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,40,1,1,10),_OacZbfwRtrConnPerfGlobalIx_Type())
oacZbfwRtrConnPerfGlobalIx.setMaxAccess(_D)
if mibBuilder.loadTexts:oacZbfwRtrConnPerfGlobalIx.setStatus(_A)
_OacZbfwPackets_ObjectIdentity=ObjectIdentity
oacZbfwPackets=_OacZbfwPackets_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,9,3131,12,41))
_OacZbfwPacketsSSCTable_Object=MibTable
oacZbfwPacketsSSCTable=_OacZbfwPacketsSSCTable_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,41,1))
if mibBuilder.loadTexts:oacZbfwPacketsSSCTable.setStatus(_A)
_OacZbfwPacketsEntry_Object=MibTableRow
oacZbfwPacketsEntry=_OacZbfwPacketsEntry_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,41,1,1))
oacZbfwPacketsEntry.setIndexNames((1,_C,_G))
if mibBuilder.loadTexts:oacZbfwPacketsEntry.setStatus(_A)
_OacZbfwPacketsGlobalIx_Type=SnmpAdminString
_OacZbfwPacketsGlobalIx_Object=MibTableColumn
oacZbfwPacketsGlobalIx=_OacZbfwPacketsGlobalIx_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,41,1,1,1),_OacZbfwPacketsGlobalIx_Type())
oacZbfwPacketsGlobalIx.setMaxAccess(_D)
if mibBuilder.loadTexts:oacZbfwPacketsGlobalIx.setStatus(_A)
_OacZbfwPacketsProcessed_Type=Counter32
_OacZbfwPacketsProcessed_Object=MibTableColumn
oacZbfwPacketsProcessed=_OacZbfwPacketsProcessed_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,41,1,1,2),_OacZbfwPacketsProcessed_Type())
oacZbfwPacketsProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwPacketsProcessed.setStatus(_A)
_OacZbfwPacketsPassed_Type=Counter32
_OacZbfwPacketsPassed_Object=MibTableColumn
oacZbfwPacketsPassed=_OacZbfwPacketsPassed_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,41,1,1,3),_OacZbfwPacketsPassed_Type())
oacZbfwPacketsPassed.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwPacketsPassed.setStatus(_A)
_OacZbfwPacketsDropped_Type=Counter32
_OacZbfwPacketsDropped_Object=MibTableColumn
oacZbfwPacketsDropped=_OacZbfwPacketsDropped_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,41,1,1,4),_OacZbfwPacketsDropped_Type())
oacZbfwPacketsDropped.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwPacketsDropped.setStatus(_A)
_OacZbfwPacketsRejected_Type=Counter32
_OacZbfwPacketsRejected_Object=MibTableColumn
oacZbfwPacketsRejected=_OacZbfwPacketsRejected_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,41,1,1,5),_OacZbfwPacketsRejected_Type())
oacZbfwPacketsRejected.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwPacketsRejected.setStatus(_A)
_OacZbfwPacketsRejectStatsInvalidIntf_Type=Counter32
_OacZbfwPacketsRejectStatsInvalidIntf_Object=MibTableColumn
oacZbfwPacketsRejectStatsInvalidIntf=_OacZbfwPacketsRejectStatsInvalidIntf_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,41,1,1,6),_OacZbfwPacketsRejectStatsInvalidIntf_Type())
oacZbfwPacketsRejectStatsInvalidIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwPacketsRejectStatsInvalidIntf.setStatus(_A)
_OacZbfwPacketsRejectStatsNoPolicy_Type=Counter32
_OacZbfwPacketsRejectStatsNoPolicy_Object=MibTableColumn
oacZbfwPacketsRejectStatsNoPolicy=_OacZbfwPacketsRejectStatsNoPolicy_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,41,1,1,7),_OacZbfwPacketsRejectStatsNoPolicy_Type())
oacZbfwPacketsRejectStatsNoPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwPacketsRejectStatsNoPolicy.setStatus(_A)
_OacZbfwPacketsRejectStatsNoConnSetup_Type=Counter32
_OacZbfwPacketsRejectStatsNoConnSetup_Object=MibTableColumn
oacZbfwPacketsRejectStatsNoConnSetup=_OacZbfwPacketsRejectStatsNoConnSetup_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,41,1,1,8),_OacZbfwPacketsRejectStatsNoConnSetup_Type())
oacZbfwPacketsRejectStatsNoConnSetup.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwPacketsRejectStatsNoConnSetup.setStatus(_A)
_OacZbfwPacketsRejectStatsProtocol_Type=Counter32
_OacZbfwPacketsRejectStatsProtocol_Object=MibTableColumn
oacZbfwPacketsRejectStatsProtocol=_OacZbfwPacketsRejectStatsProtocol_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,41,1,1,9),_OacZbfwPacketsRejectStatsProtocol_Type())
oacZbfwPacketsRejectStatsProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwPacketsRejectStatsProtocol.setStatus(_A)
_OacZbfwPacketsRejectStatsAlg_Type=Counter32
_OacZbfwPacketsRejectStatsAlg_Object=MibTableColumn
oacZbfwPacketsRejectStatsAlg=_OacZbfwPacketsRejectStatsAlg_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,41,1,1,10),_OacZbfwPacketsRejectStatsAlg_Type())
oacZbfwPacketsRejectStatsAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwPacketsRejectStatsAlg.setStatus(_A)
_OacZbfwPacketsRejectStatsConnExceeded_Type=Counter32
_OacZbfwPacketsRejectStatsConnExceeded_Object=MibTableColumn
oacZbfwPacketsRejectStatsConnExceeded=_OacZbfwPacketsRejectStatsConnExceeded_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,41,1,1,11),_OacZbfwPacketsRejectStatsConnExceeded_Type())
oacZbfwPacketsRejectStatsConnExceeded.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwPacketsRejectStatsConnExceeded.setStatus(_A)
_OacZbfwPolicyRules_ObjectIdentity=ObjectIdentity
oacZbfwPolicyRules=_OacZbfwPolicyRules_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,9,3131,12,42))
_OacZbfwPolicyRulesSSCTable_Object=MibTable
oacZbfwPolicyRulesSSCTable=_OacZbfwPolicyRulesSSCTable_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,42,1))
if mibBuilder.loadTexts:oacZbfwPolicyRulesSSCTable.setStatus(_A)
_OacZbfwPolicyRulesEntry_Object=MibTableRow
oacZbfwPolicyRulesEntry=_OacZbfwPolicyRulesEntry_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,42,1,1))
oacZbfwPolicyRulesEntry.setIndexNames((0,_C,_H),(1,_C,_I))
if mibBuilder.loadTexts:oacZbfwPolicyRulesEntry.setStatus(_A)
_OacZbfwPolicyRulesTableIx_Type=TableIndex
_OacZbfwPolicyRulesTableIx_Object=MibTableColumn
oacZbfwPolicyRulesTableIx=_OacZbfwPolicyRulesTableIx_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,42,1,1,1),_OacZbfwPolicyRulesTableIx_Type())
oacZbfwPolicyRulesTableIx.setMaxAccess(_D)
if mibBuilder.loadTexts:oacZbfwPolicyRulesTableIx.setStatus(_A)
_OacZbfwPolicyRulesGlobalIx_Type=SnmpAdminString
_OacZbfwPolicyRulesGlobalIx_Object=MibTableColumn
oacZbfwPolicyRulesGlobalIx=_OacZbfwPolicyRulesGlobalIx_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,42,1,1,2),_OacZbfwPolicyRulesGlobalIx_Type())
oacZbfwPolicyRulesGlobalIx.setMaxAccess(_D)
if mibBuilder.loadTexts:oacZbfwPolicyRulesGlobalIx.setStatus(_A)
_OacZbfwPolicyRulesZonePair_Type=DisplayString
_OacZbfwPolicyRulesZonePair_Object=MibTableColumn
oacZbfwPolicyRulesZonePair=_OacZbfwPolicyRulesZonePair_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,42,1,1,3),_OacZbfwPolicyRulesZonePair_Type())
oacZbfwPolicyRulesZonePair.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwPolicyRulesZonePair.setStatus(_A)
_OacZbfwPolicyRulesPolicy_Type=DisplayString
_OacZbfwPolicyRulesPolicy_Object=MibTableColumn
oacZbfwPolicyRulesPolicy=_OacZbfwPolicyRulesPolicy_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,42,1,1,4),_OacZbfwPolicyRulesPolicy_Type())
oacZbfwPolicyRulesPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwPolicyRulesPolicy.setStatus(_A)
_OacZbfwPolicyRulesPolicyRule_Type=DisplayString
_OacZbfwPolicyRulesPolicyRule_Object=MibTableColumn
oacZbfwPolicyRulesPolicyRule=_OacZbfwPolicyRulesPolicyRule_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,42,1,1,5),_OacZbfwPolicyRulesPolicyRule_Type())
oacZbfwPolicyRulesPolicyRule.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwPolicyRulesPolicyRule.setStatus(_A)
_OacZbfwPolicyRulesCountersProcessed_Type=Counter32
_OacZbfwPolicyRulesCountersProcessed_Object=MibTableColumn
oacZbfwPolicyRulesCountersProcessed=_OacZbfwPolicyRulesCountersProcessed_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,42,1,1,6),_OacZbfwPolicyRulesCountersProcessed_Type())
oacZbfwPolicyRulesCountersProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwPolicyRulesCountersProcessed.setStatus(_A)
_OacZbfwPolicyRulesCountersApplied_Type=Counter32
_OacZbfwPolicyRulesCountersApplied_Object=MibTableColumn
oacZbfwPolicyRulesCountersApplied=_OacZbfwPolicyRulesCountersApplied_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,42,1,1,7),_OacZbfwPolicyRulesCountersApplied_Type())
oacZbfwPolicyRulesCountersApplied.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwPolicyRulesCountersApplied.setStatus(_A)
_OacZbfwPolicyRulesCountersConnections_Type=Counter32
_OacZbfwPolicyRulesCountersConnections_Object=MibTableColumn
oacZbfwPolicyRulesCountersConnections=_OacZbfwPolicyRulesCountersConnections_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,42,1,1,8),_OacZbfwPolicyRulesCountersConnections_Type())
oacZbfwPolicyRulesCountersConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwPolicyRulesCountersConnections.setStatus(_A)
_OacZbfwPolicyRulesCountersPackets_Type=Counter32
_OacZbfwPolicyRulesCountersPackets_Object=MibTableColumn
oacZbfwPolicyRulesCountersPackets=_OacZbfwPolicyRulesCountersPackets_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,42,1,1,9),_OacZbfwPolicyRulesCountersPackets_Type())
oacZbfwPolicyRulesCountersPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwPolicyRulesCountersPackets.setStatus(_A)
_OacZbfwPolicyRulesCountersOctets_Type=Counter32
_OacZbfwPolicyRulesCountersOctets_Object=MibTableColumn
oacZbfwPolicyRulesCountersOctets=_OacZbfwPolicyRulesCountersOctets_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,42,1,1,10),_OacZbfwPolicyRulesCountersOctets_Type())
oacZbfwPolicyRulesCountersOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwPolicyRulesCountersOctets.setStatus(_A)
_OacZbfwPolicyRulesCountersReversePackets_Type=Counter32
_OacZbfwPolicyRulesCountersReversePackets_Object=MibTableColumn
oacZbfwPolicyRulesCountersReversePackets=_OacZbfwPolicyRulesCountersReversePackets_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,42,1,1,11),_OacZbfwPolicyRulesCountersReversePackets_Type())
oacZbfwPolicyRulesCountersReversePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwPolicyRulesCountersReversePackets.setStatus(_A)
_OacZbfwPolicyRulesCountersReverseOctets_Type=Counter32
_OacZbfwPolicyRulesCountersReverseOctets_Object=MibTableColumn
oacZbfwPolicyRulesCountersReverseOctets=_OacZbfwPolicyRulesCountersReverseOctets_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,42,1,1,12),_OacZbfwPolicyRulesCountersReverseOctets_Type())
oacZbfwPolicyRulesCountersReverseOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwPolicyRulesCountersReverseOctets.setStatus(_A)
_OacZbfwClearCounters_Type=Integer32
_OacZbfwClearCounters_Object=MibScalar
oacZbfwClearCounters=_OacZbfwClearCounters_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,12,43),_OacZbfwClearCounters_Type())
oacZbfwClearCounters.setMaxAccess('read-write')
if mibBuilder.loadTexts:oacZbfwClearCounters.setStatus(_A)
_OacZbfwStatus_ObjectIdentity=ObjectIdentity
oacZbfwStatus=_OacZbfwStatus_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,9,3131,14))
_OacZbfwZonePairs_ObjectIdentity=ObjectIdentity
oacZbfwZonePairs=_OacZbfwZonePairs_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,9,3131,14,22))
_OacZbfwZonePairsSSCTable_Object=MibTable
oacZbfwZonePairsSSCTable=_OacZbfwZonePairsSSCTable_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,22,1))
if mibBuilder.loadTexts:oacZbfwZonePairsSSCTable.setStatus(_A)
_OacZbfwZonePairsEntry_Object=MibTableRow
oacZbfwZonePairsEntry=_OacZbfwZonePairsEntry_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,22,1,1))
oacZbfwZonePairsEntry.setIndexNames((0,_C,_J),(1,_C,_K))
if mibBuilder.loadTexts:oacZbfwZonePairsEntry.setStatus(_A)
_OacZbfwZonePairsTableIx_Type=TableIndex
_OacZbfwZonePairsTableIx_Object=MibTableColumn
oacZbfwZonePairsTableIx=_OacZbfwZonePairsTableIx_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,22,1,1,1),_OacZbfwZonePairsTableIx_Type())
oacZbfwZonePairsTableIx.setMaxAccess(_D)
if mibBuilder.loadTexts:oacZbfwZonePairsTableIx.setStatus(_A)
_OacZbfwZonePairsGlobalIx_Type=SnmpAdminString
_OacZbfwZonePairsGlobalIx_Object=MibTableColumn
oacZbfwZonePairsGlobalIx=_OacZbfwZonePairsGlobalIx_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,22,1,1,2),_OacZbfwZonePairsGlobalIx_Type())
oacZbfwZonePairsGlobalIx.setMaxAccess(_D)
if mibBuilder.loadTexts:oacZbfwZonePairsGlobalIx.setStatus(_A)
_OacZbfwZonePairsName_Type=DisplayString
_OacZbfwZonePairsName_Object=MibTableColumn
oacZbfwZonePairsName=_OacZbfwZonePairsName_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,22,1,1,3),_OacZbfwZonePairsName_Type())
oacZbfwZonePairsName.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwZonePairsName.setStatus(_A)
_OacZbfwZonePairsSrcZone_Type=DisplayString
_OacZbfwZonePairsSrcZone_Object=MibTableColumn
oacZbfwZonePairsSrcZone=_OacZbfwZonePairsSrcZone_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,22,1,1,4),_OacZbfwZonePairsSrcZone_Type())
oacZbfwZonePairsSrcZone.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwZonePairsSrcZone.setStatus(_A)
_OacZbfwZonePairsDstZone_Type=DisplayString
_OacZbfwZonePairsDstZone_Object=MibTableColumn
oacZbfwZonePairsDstZone=_OacZbfwZonePairsDstZone_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,22,1,1,5),_OacZbfwZonePairsDstZone_Type())
oacZbfwZonePairsDstZone.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwZonePairsDstZone.setStatus(_A)
_OacZbfwZonePairsPolicy_Type=DisplayString
_OacZbfwZonePairsPolicy_Object=MibTableColumn
oacZbfwZonePairsPolicy=_OacZbfwZonePairsPolicy_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,22,1,1,7),_OacZbfwZonePairsPolicy_Type())
oacZbfwZonePairsPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwZonePairsPolicy.setStatus(_A)
_OacZbfwZonePairsCountersProcessed_Type=Counter32
_OacZbfwZonePairsCountersProcessed_Object=MibTableColumn
oacZbfwZonePairsCountersProcessed=_OacZbfwZonePairsCountersProcessed_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,22,1,1,8),_OacZbfwZonePairsCountersProcessed_Type())
oacZbfwZonePairsCountersProcessed.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwZonePairsCountersProcessed.setStatus(_A)
_OacZbfwZonePairsCountersApplied_Type=Counter32
_OacZbfwZonePairsCountersApplied_Object=MibTableColumn
oacZbfwZonePairsCountersApplied=_OacZbfwZonePairsCountersApplied_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,22,1,1,9),_OacZbfwZonePairsCountersApplied_Type())
oacZbfwZonePairsCountersApplied.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwZonePairsCountersApplied.setStatus(_A)
_OacZbfwZonePairsCountersConnections_Type=Counter32
_OacZbfwZonePairsCountersConnections_Object=MibTableColumn
oacZbfwZonePairsCountersConnections=_OacZbfwZonePairsCountersConnections_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,22,1,1,10),_OacZbfwZonePairsCountersConnections_Type())
oacZbfwZonePairsCountersConnections.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwZonePairsCountersConnections.setStatus(_A)
_OacZbfwZonePairsCountersPackets_Type=Counter32
_OacZbfwZonePairsCountersPackets_Object=MibTableColumn
oacZbfwZonePairsCountersPackets=_OacZbfwZonePairsCountersPackets_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,22,1,1,11),_OacZbfwZonePairsCountersPackets_Type())
oacZbfwZonePairsCountersPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwZonePairsCountersPackets.setStatus(_A)
_OacZbfwZonePairsCountersOctets_Type=Counter32
_OacZbfwZonePairsCountersOctets_Object=MibTableColumn
oacZbfwZonePairsCountersOctets=_OacZbfwZonePairsCountersOctets_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,22,1,1,12),_OacZbfwZonePairsCountersOctets_Type())
oacZbfwZonePairsCountersOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwZonePairsCountersOctets.setStatus(_A)
_OacZbfwZonePairsCountersReversePackets_Type=Counter32
_OacZbfwZonePairsCountersReversePackets_Object=MibTableColumn
oacZbfwZonePairsCountersReversePackets=_OacZbfwZonePairsCountersReversePackets_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,22,1,1,13),_OacZbfwZonePairsCountersReversePackets_Type())
oacZbfwZonePairsCountersReversePackets.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwZonePairsCountersReversePackets.setStatus(_A)
_OacZbfwZonePairsCountersReverseOctets_Type=Counter32
_OacZbfwZonePairsCountersReverseOctets_Object=MibTableColumn
oacZbfwZonePairsCountersReverseOctets=_OacZbfwZonePairsCountersReverseOctets_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,22,1,1,14),_OacZbfwZonePairsCountersReverseOctets_Type())
oacZbfwZonePairsCountersReverseOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwZonePairsCountersReverseOctets.setStatus(_A)
_OacZbfwFlows_ObjectIdentity=ObjectIdentity
oacZbfwFlows=_OacZbfwFlows_ObjectIdentity((1,3,6,1,4,1,13191,10,3,1,9,3131,14,23))
_OacZbfwFlowsSSCTable_Object=MibTable
oacZbfwFlowsSSCTable=_OacZbfwFlowsSSCTable_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,23,1))
if mibBuilder.loadTexts:oacZbfwFlowsSSCTable.setStatus(_A)
_OacZbfwFlowsEntry_Object=MibTableRow
oacZbfwFlowsEntry=_OacZbfwFlowsEntry_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,23,1,1))
oacZbfwFlowsEntry.setIndexNames((0,_C,_L),(1,_C,_M))
if mibBuilder.loadTexts:oacZbfwFlowsEntry.setStatus(_A)
_OacZbfwFlowsTableIx_Type=TableIndex
_OacZbfwFlowsTableIx_Object=MibTableColumn
oacZbfwFlowsTableIx=_OacZbfwFlowsTableIx_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,23,1,1,1),_OacZbfwFlowsTableIx_Type())
oacZbfwFlowsTableIx.setMaxAccess(_D)
if mibBuilder.loadTexts:oacZbfwFlowsTableIx.setStatus(_A)
_OacZbfwFlowsGlobalIx_Type=SnmpAdminString
_OacZbfwFlowsGlobalIx_Object=MibTableColumn
oacZbfwFlowsGlobalIx=_OacZbfwFlowsGlobalIx_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,23,1,1,2),_OacZbfwFlowsGlobalIx_Type())
oacZbfwFlowsGlobalIx.setMaxAccess(_D)
if mibBuilder.loadTexts:oacZbfwFlowsGlobalIx.setStatus(_A)
_OacZbfwFlowsConnectionId_Type=Counter32
_OacZbfwFlowsConnectionId_Object=MibTableColumn
oacZbfwFlowsConnectionId=_OacZbfwFlowsConnectionId_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,23,1,1,3),_OacZbfwFlowsConnectionId_Type())
oacZbfwFlowsConnectionId.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwFlowsConnectionId.setStatus(_A)
_OacZbfwFlowsSrcIntf_Type=DisplayString
_OacZbfwFlowsSrcIntf_Object=MibTableColumn
oacZbfwFlowsSrcIntf=_OacZbfwFlowsSrcIntf_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,23,1,1,4),_OacZbfwFlowsSrcIntf_Type())
oacZbfwFlowsSrcIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwFlowsSrcIntf.setStatus(_A)
_OacZbfwFlowsSrcZone_Type=DisplayString
_OacZbfwFlowsSrcZone_Object=MibTableColumn
oacZbfwFlowsSrcZone=_OacZbfwFlowsSrcZone_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,23,1,1,5),_OacZbfwFlowsSrcZone_Type())
oacZbfwFlowsSrcZone.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwFlowsSrcZone.setStatus(_A)
_OacZbfwFlowsDstIntf_Type=DisplayString
_OacZbfwFlowsDstIntf_Object=MibTableColumn
oacZbfwFlowsDstIntf=_OacZbfwFlowsDstIntf_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,23,1,1,6),_OacZbfwFlowsDstIntf_Type())
oacZbfwFlowsDstIntf.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwFlowsDstIntf.setStatus(_A)
_OacZbfwFlowsDstZone_Type=DisplayString
_OacZbfwFlowsDstZone_Object=MibTableColumn
oacZbfwFlowsDstZone=_OacZbfwFlowsDstZone_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,23,1,1,7),_OacZbfwFlowsDstZone_Type())
oacZbfwFlowsDstZone.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwFlowsDstZone.setStatus(_A)
_OacZbfwFlowsSrcAddress_Type=IpAddress
_OacZbfwFlowsSrcAddress_Object=MibTableColumn
oacZbfwFlowsSrcAddress=_OacZbfwFlowsSrcAddress_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,23,1,1,8),_OacZbfwFlowsSrcAddress_Type())
oacZbfwFlowsSrcAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwFlowsSrcAddress.setStatus(_A)
_OacZbfwFlowsDstAddress_Type=IpAddress
_OacZbfwFlowsDstAddress_Object=MibTableColumn
oacZbfwFlowsDstAddress=_OacZbfwFlowsDstAddress_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,23,1,1,9),_OacZbfwFlowsDstAddress_Type())
oacZbfwFlowsDstAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwFlowsDstAddress.setStatus(_A)
class _OacZbfwFlowsProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,4,6,8,9,17,46,47,50,51,88,89)));namedValues=NamedValues(*(('any',0),('icmp',1),('igmp',2),('ipInIp',4),('tcp',6),('egp',8),('igp',9),('udp',17),('rsvp',46),('gre',47),('esp',50),('ah',51),('igrp',88),('ospf',89)))
_OacZbfwFlowsProtocol_Type.__name__=_E
_OacZbfwFlowsProtocol_Object=MibTableColumn
oacZbfwFlowsProtocol=_OacZbfwFlowsProtocol_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,23,1,1,10),_OacZbfwFlowsProtocol_Type())
oacZbfwFlowsProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwFlowsProtocol.setStatus(_A)
_OacZbfwFlowsSrcPort_Type=Integer32
_OacZbfwFlowsSrcPort_Object=MibTableColumn
oacZbfwFlowsSrcPort=_OacZbfwFlowsSrcPort_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,23,1,1,11),_OacZbfwFlowsSrcPort_Type())
oacZbfwFlowsSrcPort.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwFlowsSrcPort.setStatus(_A)
_OacZbfwFlowsDstPort_Type=Integer32
_OacZbfwFlowsDstPort_Object=MibTableColumn
oacZbfwFlowsDstPort=_OacZbfwFlowsDstPort_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,23,1,1,12),_OacZbfwFlowsDstPort_Type())
oacZbfwFlowsDstPort.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwFlowsDstPort.setStatus(_A)
_OacZbfwFlowsAge_Type=TimeTicks
_OacZbfwFlowsAge_Object=MibTableColumn
oacZbfwFlowsAge=_OacZbfwFlowsAge_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,23,1,1,13),_OacZbfwFlowsAge_Type())
oacZbfwFlowsAge.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwFlowsAge.setStatus(_A)
_OacZbfwFlowsTimeOut_Type=TimeTicks
_OacZbfwFlowsTimeOut_Object=MibTableColumn
oacZbfwFlowsTimeOut=_OacZbfwFlowsTimeOut_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,23,1,1,14),_OacZbfwFlowsTimeOut_Type())
oacZbfwFlowsTimeOut.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwFlowsTimeOut.setStatus(_A)
_OacZbfwFlowsRulesZonePair_Type=DisplayString
_OacZbfwFlowsRulesZonePair_Object=MibTableColumn
oacZbfwFlowsRulesZonePair=_OacZbfwFlowsRulesZonePair_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,23,1,1,15),_OacZbfwFlowsRulesZonePair_Type())
oacZbfwFlowsRulesZonePair.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwFlowsRulesZonePair.setStatus(_A)
_OacZbfwFlowsRulesPolicy_Type=DisplayString
_OacZbfwFlowsRulesPolicy_Object=MibTableColumn
oacZbfwFlowsRulesPolicy=_OacZbfwFlowsRulesPolicy_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,23,1,1,16),_OacZbfwFlowsRulesPolicy_Type())
oacZbfwFlowsRulesPolicy.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwFlowsRulesPolicy.setStatus(_A)
_OacZbfwFlowsRulesPolicyRule_Type=DisplayString
_OacZbfwFlowsRulesPolicyRule_Object=MibTableColumn
oacZbfwFlowsRulesPolicyRule=_OacZbfwFlowsRulesPolicyRule_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,23,1,1,17),_OacZbfwFlowsRulesPolicyRule_Type())
oacZbfwFlowsRulesPolicyRule.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwFlowsRulesPolicyRule.setStatus(_A)
_OacZbfwFlowsRulesFilter_Type=DisplayString
_OacZbfwFlowsRulesFilter_Object=MibTableColumn
oacZbfwFlowsRulesFilter=_OacZbfwFlowsRulesFilter_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,23,1,1,18),_OacZbfwFlowsRulesFilter_Type())
oacZbfwFlowsRulesFilter.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwFlowsRulesFilter.setStatus(_A)
_OacZbfwFlowsRulesFilterRule_Type=DisplayString
_OacZbfwFlowsRulesFilterRule_Object=MibTableColumn
oacZbfwFlowsRulesFilterRule=_OacZbfwFlowsRulesFilterRule_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,23,1,1,19),_OacZbfwFlowsRulesFilterRule_Type())
oacZbfwFlowsRulesFilterRule.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwFlowsRulesFilterRule.setStatus(_A)
class _OacZbfwFlowsModeAlg_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('false',0),('true',1)))
_OacZbfwFlowsModeAlg_Type.__name__=_E
_OacZbfwFlowsModeAlg_Object=MibTableColumn
oacZbfwFlowsModeAlg=_OacZbfwFlowsModeAlg_Object((1,3,6,1,4,1,13191,10,3,1,9,3131,14,23,1,1,20),_OacZbfwFlowsModeAlg_Type())
oacZbfwFlowsModeAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:oacZbfwFlowsModeAlg.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'TableIndex':TableIndex,'oacZbfwStatusMIB':oacZbfwStatusMIB,'oacZbfw':oacZbfw,'oacZbfwPerf':oacZbfwPerf,'oacZbfwRtrConnPerf':oacZbfwRtrConnPerf,'oacZbfwRtrConnPerfSSCTable':oacZbfwRtrConnPerfSSCTable,'oacZbfwRtrConnPerfEntry':oacZbfwRtrConnPerfEntry,'oacZbfwRouterConnectionsCreated':oacZbfwRouterConnectionsCreated,'oacZbfwRouterConnectionsClosed':oacZbfwRouterConnectionsClosed,'oacZbfwRouterConnectionsTimedOut':oacZbfwRouterConnectionsTimedOut,'oacZbfwRouterConnectionsMax':oacZbfwRouterConnectionsMax,'oacZbfwRouterConnectionsMaxUsed':oacZbfwRouterConnectionsMaxUsed,'oacZbfwRouterConnectionsUsed':oacZbfwRouterConnectionsUsed,_F:oacZbfwRtrConnPerfGlobalIx,'oacZbfwPackets':oacZbfwPackets,'oacZbfwPacketsSSCTable':oacZbfwPacketsSSCTable,'oacZbfwPacketsEntry':oacZbfwPacketsEntry,_G:oacZbfwPacketsGlobalIx,'oacZbfwPacketsProcessed':oacZbfwPacketsProcessed,'oacZbfwPacketsPassed':oacZbfwPacketsPassed,'oacZbfwPacketsDropped':oacZbfwPacketsDropped,'oacZbfwPacketsRejected':oacZbfwPacketsRejected,'oacZbfwPacketsRejectStatsInvalidIntf':oacZbfwPacketsRejectStatsInvalidIntf,'oacZbfwPacketsRejectStatsNoPolicy':oacZbfwPacketsRejectStatsNoPolicy,'oacZbfwPacketsRejectStatsNoConnSetup':oacZbfwPacketsRejectStatsNoConnSetup,'oacZbfwPacketsRejectStatsProtocol':oacZbfwPacketsRejectStatsProtocol,'oacZbfwPacketsRejectStatsAlg':oacZbfwPacketsRejectStatsAlg,'oacZbfwPacketsRejectStatsConnExceeded':oacZbfwPacketsRejectStatsConnExceeded,'oacZbfwPolicyRules':oacZbfwPolicyRules,'oacZbfwPolicyRulesSSCTable':oacZbfwPolicyRulesSSCTable,'oacZbfwPolicyRulesEntry':oacZbfwPolicyRulesEntry,_H:oacZbfwPolicyRulesTableIx,_I:oacZbfwPolicyRulesGlobalIx,'oacZbfwPolicyRulesZonePair':oacZbfwPolicyRulesZonePair,'oacZbfwPolicyRulesPolicy':oacZbfwPolicyRulesPolicy,'oacZbfwPolicyRulesPolicyRule':oacZbfwPolicyRulesPolicyRule,'oacZbfwPolicyRulesCountersProcessed':oacZbfwPolicyRulesCountersProcessed,'oacZbfwPolicyRulesCountersApplied':oacZbfwPolicyRulesCountersApplied,'oacZbfwPolicyRulesCountersConnections':oacZbfwPolicyRulesCountersConnections,'oacZbfwPolicyRulesCountersPackets':oacZbfwPolicyRulesCountersPackets,'oacZbfwPolicyRulesCountersOctets':oacZbfwPolicyRulesCountersOctets,'oacZbfwPolicyRulesCountersReversePackets':oacZbfwPolicyRulesCountersReversePackets,'oacZbfwPolicyRulesCountersReverseOctets':oacZbfwPolicyRulesCountersReverseOctets,'oacZbfwClearCounters':oacZbfwClearCounters,'oacZbfwStatus':oacZbfwStatus,'oacZbfwZonePairs':oacZbfwZonePairs,'oacZbfwZonePairsSSCTable':oacZbfwZonePairsSSCTable,'oacZbfwZonePairsEntry':oacZbfwZonePairsEntry,_J:oacZbfwZonePairsTableIx,_K:oacZbfwZonePairsGlobalIx,'oacZbfwZonePairsName':oacZbfwZonePairsName,'oacZbfwZonePairsSrcZone':oacZbfwZonePairsSrcZone,'oacZbfwZonePairsDstZone':oacZbfwZonePairsDstZone,'oacZbfwZonePairsPolicy':oacZbfwZonePairsPolicy,'oacZbfwZonePairsCountersProcessed':oacZbfwZonePairsCountersProcessed,'oacZbfwZonePairsCountersApplied':oacZbfwZonePairsCountersApplied,'oacZbfwZonePairsCountersConnections':oacZbfwZonePairsCountersConnections,'oacZbfwZonePairsCountersPackets':oacZbfwZonePairsCountersPackets,'oacZbfwZonePairsCountersOctets':oacZbfwZonePairsCountersOctets,'oacZbfwZonePairsCountersReversePackets':oacZbfwZonePairsCountersReversePackets,'oacZbfwZonePairsCountersReverseOctets':oacZbfwZonePairsCountersReverseOctets,'oacZbfwFlows':oacZbfwFlows,'oacZbfwFlowsSSCTable':oacZbfwFlowsSSCTable,'oacZbfwFlowsEntry':oacZbfwFlowsEntry,_L:oacZbfwFlowsTableIx,_M:oacZbfwFlowsGlobalIx,'oacZbfwFlowsConnectionId':oacZbfwFlowsConnectionId,'oacZbfwFlowsSrcIntf':oacZbfwFlowsSrcIntf,'oacZbfwFlowsSrcZone':oacZbfwFlowsSrcZone,'oacZbfwFlowsDstIntf':oacZbfwFlowsDstIntf,'oacZbfwFlowsDstZone':oacZbfwFlowsDstZone,'oacZbfwFlowsSrcAddress':oacZbfwFlowsSrcAddress,'oacZbfwFlowsDstAddress':oacZbfwFlowsDstAddress,'oacZbfwFlowsProtocol':oacZbfwFlowsProtocol,'oacZbfwFlowsSrcPort':oacZbfwFlowsSrcPort,'oacZbfwFlowsDstPort':oacZbfwFlowsDstPort,'oacZbfwFlowsAge':oacZbfwFlowsAge,'oacZbfwFlowsTimeOut':oacZbfwFlowsTimeOut,'oacZbfwFlowsRulesZonePair':oacZbfwFlowsRulesZonePair,'oacZbfwFlowsRulesPolicy':oacZbfwFlowsRulesPolicy,'oacZbfwFlowsRulesPolicyRule':oacZbfwFlowsRulesPolicyRule,'oacZbfwFlowsRulesFilter':oacZbfwFlowsRulesFilter,'oacZbfwFlowsRulesFilterRule':oacZbfwFlowsRulesFilterRule,'oacZbfwFlowsModeAlg':oacZbfwFlowsModeAlg})