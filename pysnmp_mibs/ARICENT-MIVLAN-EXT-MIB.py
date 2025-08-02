_K='fsMIServiceProtocolEnum'
_J='fsMIServiceVlanId'
_I='EnabledStatus'
_H='not-accessible'
_G='fsMIVlanContextId'
_F='fsMIVlanPort'
_E='Integer32'
_D='ARICENT-MIVLAN-EXT-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('ARICENTP-BRIDGE-MIB',_I)
VlanId,=mibBuilder.importSymbols('AricentMIVlan-MIB','VlanId')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
futureMIVlanExtMIB=ModuleIdentity((1,3,6,1,4,1,2076,138))
if mibBuilder.loadTexts:futureMIVlanExtMIB.setRevisions(('2012-09-05 00:00',))
class TunnelStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('peer',1),('tunnel',2),('discard',3)))
class L2CPProtocols(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,23))
_FsMIVlanSystemConfig_ObjectIdentity=ObjectIdentity
fsMIVlanSystemConfig=_FsMIVlanSystemConfig_ObjectIdentity((1,3,6,1,4,1,2076,138,1))
_FsMIVlanBridgeInfoTable_Object=MibTable
fsMIVlanBridgeInfoTable=_FsMIVlanBridgeInfoTable_Object((1,3,6,1,4,1,2076,138,1,1))
if mibBuilder.loadTexts:fsMIVlanBridgeInfoTable.setStatus(_A)
_FsMIVlanBridgeInfoEntry_Object=MibTableRow
fsMIVlanBridgeInfoEntry=_FsMIVlanBridgeInfoEntry_Object((1,3,6,1,4,1,2076,138,1,1,1))
fsMIVlanBridgeInfoEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:fsMIVlanBridgeInfoEntry.setStatus(_A)
class _FsMIVlanContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsMIVlanContextId_Type.__name__=_E
_FsMIVlanContextId_Object=MibTableColumn
fsMIVlanContextId=_FsMIVlanContextId_Object((1,3,6,1,4,1,2076,138,1,1,1,1),_FsMIVlanContextId_Type())
fsMIVlanContextId.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIVlanContextId.setStatus(_A)
class _FsMIVlanBridgeMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('customerBridge',1),('providerBridge',2),('providerEdgeBridge',3),('providerCoreBridge',4),('providerBackoneICompBridge',5),('providerBackoneBCompBridge',6),('invalidBridgeMode',7)))
_FsMIVlanBridgeMode_Type.__name__=_E
_FsMIVlanBridgeMode_Object=MibTableColumn
fsMIVlanBridgeMode=_FsMIVlanBridgeMode_Object((1,3,6,1,4,1,2076,138,1,1,1,2),_FsMIVlanBridgeMode_Type())
fsMIVlanBridgeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanBridgeMode.setStatus(_A)
_FsMIVlanTunnelObjects_ObjectIdentity=ObjectIdentity
fsMIVlanTunnelObjects=_FsMIVlanTunnelObjects_ObjectIdentity((1,3,6,1,4,1,2076,138,2))
_FsMIVlanTunnelContextInfoTable_Object=MibTable
fsMIVlanTunnelContextInfoTable=_FsMIVlanTunnelContextInfoTable_Object((1,3,6,1,4,1,2076,138,2,1))
if mibBuilder.loadTexts:fsMIVlanTunnelContextInfoTable.setStatus(_A)
_FsMIVlanTunnelContextInfoEntry_Object=MibTableRow
fsMIVlanTunnelContextInfoEntry=_FsMIVlanTunnelContextInfoEntry_Object((1,3,6,1,4,1,2076,138,2,1,1))
fsMIVlanTunnelContextInfoEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:fsMIVlanTunnelContextInfoEntry.setStatus(_A)
class _FsMIVlanTunnelBpduPri_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsMIVlanTunnelBpduPri_Type.__name__=_E
_FsMIVlanTunnelBpduPri_Object=MibTableColumn
fsMIVlanTunnelBpduPri=_FsMIVlanTunnelBpduPri_Object((1,3,6,1,4,1,2076,138,2,1,1,1),_FsMIVlanTunnelBpduPri_Type())
fsMIVlanTunnelBpduPri.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelBpduPri.setStatus(_A)
_FsMIVlanTunnelStpAddress_Type=MacAddress
_FsMIVlanTunnelStpAddress_Object=MibTableColumn
fsMIVlanTunnelStpAddress=_FsMIVlanTunnelStpAddress_Object((1,3,6,1,4,1,2076,138,2,1,1,2),_FsMIVlanTunnelStpAddress_Type())
fsMIVlanTunnelStpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelStpAddress.setStatus(_A)
_FsMIVlanTunnelLacpAddress_Type=MacAddress
_FsMIVlanTunnelLacpAddress_Object=MibTableColumn
fsMIVlanTunnelLacpAddress=_FsMIVlanTunnelLacpAddress_Object((1,3,6,1,4,1,2076,138,2,1,1,3),_FsMIVlanTunnelLacpAddress_Type())
fsMIVlanTunnelLacpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelLacpAddress.setStatus(_A)
_FsMIVlanTunnelDot1xAddress_Type=MacAddress
_FsMIVlanTunnelDot1xAddress_Object=MibTableColumn
fsMIVlanTunnelDot1xAddress=_FsMIVlanTunnelDot1xAddress_Object((1,3,6,1,4,1,2076,138,2,1,1,4),_FsMIVlanTunnelDot1xAddress_Type())
fsMIVlanTunnelDot1xAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelDot1xAddress.setStatus(_A)
_FsMIVlanTunnelGvrpAddress_Type=MacAddress
_FsMIVlanTunnelGvrpAddress_Object=MibTableColumn
fsMIVlanTunnelGvrpAddress=_FsMIVlanTunnelGvrpAddress_Object((1,3,6,1,4,1,2076,138,2,1,1,5),_FsMIVlanTunnelGvrpAddress_Type())
fsMIVlanTunnelGvrpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelGvrpAddress.setStatus(_A)
_FsMIVlanTunnelGmrpAddress_Type=MacAddress
_FsMIVlanTunnelGmrpAddress_Object=MibTableColumn
fsMIVlanTunnelGmrpAddress=_FsMIVlanTunnelGmrpAddress_Object((1,3,6,1,4,1,2076,138,2,1,1,6),_FsMIVlanTunnelGmrpAddress_Type())
fsMIVlanTunnelGmrpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelGmrpAddress.setStatus(_A)
_FsMIVlanTunnelMvrpAddress_Type=MacAddress
_FsMIVlanTunnelMvrpAddress_Object=MibTableColumn
fsMIVlanTunnelMvrpAddress=_FsMIVlanTunnelMvrpAddress_Object((1,3,6,1,4,1,2076,138,2,1,1,7),_FsMIVlanTunnelMvrpAddress_Type())
fsMIVlanTunnelMvrpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelMvrpAddress.setStatus(_A)
_FsMIVlanTunnelMmrpAddress_Type=MacAddress
_FsMIVlanTunnelMmrpAddress_Object=MibTableColumn
fsMIVlanTunnelMmrpAddress=_FsMIVlanTunnelMmrpAddress_Object((1,3,6,1,4,1,2076,138,2,1,1,8),_FsMIVlanTunnelMmrpAddress_Type())
fsMIVlanTunnelMmrpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelMmrpAddress.setStatus(_A)
_FsMIVlanTunnelElmiAddress_Type=MacAddress
_FsMIVlanTunnelElmiAddress_Object=MibTableColumn
fsMIVlanTunnelElmiAddress=_FsMIVlanTunnelElmiAddress_Object((1,3,6,1,4,1,2076,138,2,1,1,9),_FsMIVlanTunnelElmiAddress_Type())
fsMIVlanTunnelElmiAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelElmiAddress.setStatus(_A)
_FsMIVlanTunnelLldpAddress_Type=MacAddress
_FsMIVlanTunnelLldpAddress_Object=MibTableColumn
fsMIVlanTunnelLldpAddress=_FsMIVlanTunnelLldpAddress_Object((1,3,6,1,4,1,2076,138,2,1,1,10),_FsMIVlanTunnelLldpAddress_Type())
fsMIVlanTunnelLldpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelLldpAddress.setStatus(_A)
_FsMIVlanTunnelEcfmAddress_Type=MacAddress
_FsMIVlanTunnelEcfmAddress_Object=MibTableColumn
fsMIVlanTunnelEcfmAddress=_FsMIVlanTunnelEcfmAddress_Object((1,3,6,1,4,1,2076,138,2,1,1,11),_FsMIVlanTunnelEcfmAddress_Type())
fsMIVlanTunnelEcfmAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelEcfmAddress.setStatus(_A)
_FsMIVlanTunnelEoamAddress_Type=MacAddress
_FsMIVlanTunnelEoamAddress_Object=MibTableColumn
fsMIVlanTunnelEoamAddress=_FsMIVlanTunnelEoamAddress_Object((1,3,6,1,4,1,2076,138,2,1,1,12),_FsMIVlanTunnelEoamAddress_Type())
fsMIVlanTunnelEoamAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelEoamAddress.setStatus(_A)
_FsMIVlanTunnelIgmpAddress_Type=MacAddress
_FsMIVlanTunnelIgmpAddress_Object=MibTableColumn
fsMIVlanTunnelIgmpAddress=_FsMIVlanTunnelIgmpAddress_Object((1,3,6,1,4,1,2076,138,2,1,1,13),_FsMIVlanTunnelIgmpAddress_Type())
fsMIVlanTunnelIgmpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelIgmpAddress.setStatus(_A)
_FsMIVlanTunnelTable_Object=MibTable
fsMIVlanTunnelTable=_FsMIVlanTunnelTable_Object((1,3,6,1,4,1,2076,138,2,2))
if mibBuilder.loadTexts:fsMIVlanTunnelTable.setStatus(_A)
_FsMIVlanTunnelEntry_Object=MibTableRow
fsMIVlanTunnelEntry=_FsMIVlanTunnelEntry_Object((1,3,6,1,4,1,2076,138,2,2,1))
fsMIVlanTunnelEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:fsMIVlanTunnelEntry.setStatus(_A)
class _FsMIVlanPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsMIVlanPort_Type.__name__=_E
_FsMIVlanPort_Object=MibTableColumn
fsMIVlanPort=_FsMIVlanPort_Object((1,3,6,1,4,1,2076,138,2,2,1,1),_FsMIVlanPort_Type())
fsMIVlanPort.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIVlanPort.setStatus(_A)
class _FsMIVlanTunnelStatus_Type(EnabledStatus):defaultValue=2
_FsMIVlanTunnelStatus_Type.__name__=_I
_FsMIVlanTunnelStatus_Object=MibTableColumn
fsMIVlanTunnelStatus=_FsMIVlanTunnelStatus_Object((1,3,6,1,4,1,2076,138,2,2,1,2),_FsMIVlanTunnelStatus_Type())
fsMIVlanTunnelStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelStatus.setStatus(_A)
_FsMIVlanTunnelProtocolTable_Object=MibTable
fsMIVlanTunnelProtocolTable=_FsMIVlanTunnelProtocolTable_Object((1,3,6,1,4,1,2076,138,2,3))
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolTable.setStatus(_A)
_FsMIVlanTunnelProtocolEntry_Object=MibTableRow
fsMIVlanTunnelProtocolEntry=_FsMIVlanTunnelProtocolEntry_Object((1,3,6,1,4,1,2076,138,2,3,1))
fsMIVlanTunnelProtocolEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolEntry.setStatus(_A)
_FsMIVlanTunnelProtocolDot1x_Type=TunnelStatus
_FsMIVlanTunnelProtocolDot1x_Object=MibTableColumn
fsMIVlanTunnelProtocolDot1x=_FsMIVlanTunnelProtocolDot1x_Object((1,3,6,1,4,1,2076,138,2,3,1,1),_FsMIVlanTunnelProtocolDot1x_Type())
fsMIVlanTunnelProtocolDot1x.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolDot1x.setStatus(_A)
_FsMIVlanTunnelProtocolLacp_Type=TunnelStatus
_FsMIVlanTunnelProtocolLacp_Object=MibTableColumn
fsMIVlanTunnelProtocolLacp=_FsMIVlanTunnelProtocolLacp_Object((1,3,6,1,4,1,2076,138,2,3,1,2),_FsMIVlanTunnelProtocolLacp_Type())
fsMIVlanTunnelProtocolLacp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolLacp.setStatus(_A)
_FsMIVlanTunnelProtocolStp_Type=TunnelStatus
_FsMIVlanTunnelProtocolStp_Object=MibTableColumn
fsMIVlanTunnelProtocolStp=_FsMIVlanTunnelProtocolStp_Object((1,3,6,1,4,1,2076,138,2,3,1,3),_FsMIVlanTunnelProtocolStp_Type())
fsMIVlanTunnelProtocolStp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolStp.setStatus(_A)
_FsMIVlanTunnelProtocolGvrp_Type=TunnelStatus
_FsMIVlanTunnelProtocolGvrp_Object=MibTableColumn
fsMIVlanTunnelProtocolGvrp=_FsMIVlanTunnelProtocolGvrp_Object((1,3,6,1,4,1,2076,138,2,3,1,4),_FsMIVlanTunnelProtocolGvrp_Type())
fsMIVlanTunnelProtocolGvrp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolGvrp.setStatus(_A)
_FsMIVlanTunnelProtocolGmrp_Type=TunnelStatus
_FsMIVlanTunnelProtocolGmrp_Object=MibTableColumn
fsMIVlanTunnelProtocolGmrp=_FsMIVlanTunnelProtocolGmrp_Object((1,3,6,1,4,1,2076,138,2,3,1,5),_FsMIVlanTunnelProtocolGmrp_Type())
fsMIVlanTunnelProtocolGmrp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolGmrp.setStatus(_A)
_FsMIVlanTunnelProtocolIgmp_Type=TunnelStatus
_FsMIVlanTunnelProtocolIgmp_Object=MibTableColumn
fsMIVlanTunnelProtocolIgmp=_FsMIVlanTunnelProtocolIgmp_Object((1,3,6,1,4,1,2076,138,2,3,1,6),_FsMIVlanTunnelProtocolIgmp_Type())
fsMIVlanTunnelProtocolIgmp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolIgmp.setStatus(_A)
_FsMIVlanTunnelProtocolMvrp_Type=TunnelStatus
_FsMIVlanTunnelProtocolMvrp_Object=MibTableColumn
fsMIVlanTunnelProtocolMvrp=_FsMIVlanTunnelProtocolMvrp_Object((1,3,6,1,4,1,2076,138,2,3,1,7),_FsMIVlanTunnelProtocolMvrp_Type())
fsMIVlanTunnelProtocolMvrp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolMvrp.setStatus(_A)
_FsMIVlanTunnelProtocolMmrp_Type=TunnelStatus
_FsMIVlanTunnelProtocolMmrp_Object=MibTableColumn
fsMIVlanTunnelProtocolMmrp=_FsMIVlanTunnelProtocolMmrp_Object((1,3,6,1,4,1,2076,138,2,3,1,8),_FsMIVlanTunnelProtocolMmrp_Type())
fsMIVlanTunnelProtocolMmrp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolMmrp.setStatus(_A)
_FsMIVlanTunnelProtocolElmi_Type=TunnelStatus
_FsMIVlanTunnelProtocolElmi_Object=MibTableColumn
fsMIVlanTunnelProtocolElmi=_FsMIVlanTunnelProtocolElmi_Object((1,3,6,1,4,1,2076,138,2,3,1,9),_FsMIVlanTunnelProtocolElmi_Type())
fsMIVlanTunnelProtocolElmi.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolElmi.setStatus(_A)
_FsMIVlanTunnelProtocolLldp_Type=TunnelStatus
_FsMIVlanTunnelProtocolLldp_Object=MibTableColumn
fsMIVlanTunnelProtocolLldp=_FsMIVlanTunnelProtocolLldp_Object((1,3,6,1,4,1,2076,138,2,3,1,10),_FsMIVlanTunnelProtocolLldp_Type())
fsMIVlanTunnelProtocolLldp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolLldp.setStatus(_A)
_FsMIVlanTunnelProtocolEcfm_Type=TunnelStatus
_FsMIVlanTunnelProtocolEcfm_Object=MibTableColumn
fsMIVlanTunnelProtocolEcfm=_FsMIVlanTunnelProtocolEcfm_Object((1,3,6,1,4,1,2076,138,2,3,1,11),_FsMIVlanTunnelProtocolEcfm_Type())
fsMIVlanTunnelProtocolEcfm.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolEcfm.setStatus(_A)
class _FsMIVlanTunnelOverrideOption_Type(EnabledStatus):defaultValue=2
_FsMIVlanTunnelOverrideOption_Type.__name__=_I
_FsMIVlanTunnelOverrideOption_Object=MibTableColumn
fsMIVlanTunnelOverrideOption=_FsMIVlanTunnelOverrideOption_Object((1,3,6,1,4,1,2076,138,2,3,1,12),_FsMIVlanTunnelOverrideOption_Type())
fsMIVlanTunnelOverrideOption.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelOverrideOption.setStatus(_A)
_FsMIVlanTunnelProtocolEoam_Type=TunnelStatus
_FsMIVlanTunnelProtocolEoam_Object=MibTableColumn
fsMIVlanTunnelProtocolEoam=_FsMIVlanTunnelProtocolEoam_Object((1,3,6,1,4,1,2076,138,2,3,1,13),_FsMIVlanTunnelProtocolEoam_Type())
fsMIVlanTunnelProtocolEoam.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolEoam.setStatus(_A)
_FsMIVlanTunnelProtocolStatsTable_Object=MibTable
fsMIVlanTunnelProtocolStatsTable=_FsMIVlanTunnelProtocolStatsTable_Object((1,3,6,1,4,1,2076,138,2,4))
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolStatsTable.setStatus(_A)
_FsMIVlanTunnelProtocolStatsEntry_Object=MibTableRow
fsMIVlanTunnelProtocolStatsEntry=_FsMIVlanTunnelProtocolStatsEntry_Object((1,3,6,1,4,1,2076,138,2,4,1))
fsMIVlanTunnelProtocolStatsEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolStatsEntry.setStatus(_A)
_FsMIVlanTunnelProtocolDot1xPktsRecvd_Type=Counter32
_FsMIVlanTunnelProtocolDot1xPktsRecvd_Object=MibTableColumn
fsMIVlanTunnelProtocolDot1xPktsRecvd=_FsMIVlanTunnelProtocolDot1xPktsRecvd_Object((1,3,6,1,4,1,2076,138,2,4,1,1),_FsMIVlanTunnelProtocolDot1xPktsRecvd_Type())
fsMIVlanTunnelProtocolDot1xPktsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolDot1xPktsRecvd.setStatus(_A)
_FsMIVlanTunnelProtocolDot1xPktsSent_Type=Counter32
_FsMIVlanTunnelProtocolDot1xPktsSent_Object=MibTableColumn
fsMIVlanTunnelProtocolDot1xPktsSent=_FsMIVlanTunnelProtocolDot1xPktsSent_Object((1,3,6,1,4,1,2076,138,2,4,1,2),_FsMIVlanTunnelProtocolDot1xPktsSent_Type())
fsMIVlanTunnelProtocolDot1xPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolDot1xPktsSent.setStatus(_A)
_FsMIVlanTunnelProtocolLacpPktsRecvd_Type=Counter32
_FsMIVlanTunnelProtocolLacpPktsRecvd_Object=MibTableColumn
fsMIVlanTunnelProtocolLacpPktsRecvd=_FsMIVlanTunnelProtocolLacpPktsRecvd_Object((1,3,6,1,4,1,2076,138,2,4,1,3),_FsMIVlanTunnelProtocolLacpPktsRecvd_Type())
fsMIVlanTunnelProtocolLacpPktsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolLacpPktsRecvd.setStatus(_A)
_FsMIVlanTunnelProtocolLacpPktsSent_Type=Counter32
_FsMIVlanTunnelProtocolLacpPktsSent_Object=MibTableColumn
fsMIVlanTunnelProtocolLacpPktsSent=_FsMIVlanTunnelProtocolLacpPktsSent_Object((1,3,6,1,4,1,2076,138,2,4,1,4),_FsMIVlanTunnelProtocolLacpPktsSent_Type())
fsMIVlanTunnelProtocolLacpPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolLacpPktsSent.setStatus(_A)
_FsMIVlanTunnelProtocolStpPDUsRecvd_Type=Counter32
_FsMIVlanTunnelProtocolStpPDUsRecvd_Object=MibTableColumn
fsMIVlanTunnelProtocolStpPDUsRecvd=_FsMIVlanTunnelProtocolStpPDUsRecvd_Object((1,3,6,1,4,1,2076,138,2,4,1,5),_FsMIVlanTunnelProtocolStpPDUsRecvd_Type())
fsMIVlanTunnelProtocolStpPDUsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolStpPDUsRecvd.setStatus(_A)
_FsMIVlanTunnelProtocolStpPDUsSent_Type=Counter32
_FsMIVlanTunnelProtocolStpPDUsSent_Object=MibTableColumn
fsMIVlanTunnelProtocolStpPDUsSent=_FsMIVlanTunnelProtocolStpPDUsSent_Object((1,3,6,1,4,1,2076,138,2,4,1,6),_FsMIVlanTunnelProtocolStpPDUsSent_Type())
fsMIVlanTunnelProtocolStpPDUsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolStpPDUsSent.setStatus(_A)
_FsMIVlanTunnelProtocolGvrpPDUsRecvd_Type=Counter32
_FsMIVlanTunnelProtocolGvrpPDUsRecvd_Object=MibTableColumn
fsMIVlanTunnelProtocolGvrpPDUsRecvd=_FsMIVlanTunnelProtocolGvrpPDUsRecvd_Object((1,3,6,1,4,1,2076,138,2,4,1,7),_FsMIVlanTunnelProtocolGvrpPDUsRecvd_Type())
fsMIVlanTunnelProtocolGvrpPDUsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolGvrpPDUsRecvd.setStatus(_A)
_FsMIVlanTunnelProtocolGvrpPDUsSent_Type=Counter32
_FsMIVlanTunnelProtocolGvrpPDUsSent_Object=MibTableColumn
fsMIVlanTunnelProtocolGvrpPDUsSent=_FsMIVlanTunnelProtocolGvrpPDUsSent_Object((1,3,6,1,4,1,2076,138,2,4,1,8),_FsMIVlanTunnelProtocolGvrpPDUsSent_Type())
fsMIVlanTunnelProtocolGvrpPDUsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolGvrpPDUsSent.setStatus(_A)
_FsMIVlanTunnelProtocolGmrpPktsRecvd_Type=Counter32
_FsMIVlanTunnelProtocolGmrpPktsRecvd_Object=MibTableColumn
fsMIVlanTunnelProtocolGmrpPktsRecvd=_FsMIVlanTunnelProtocolGmrpPktsRecvd_Object((1,3,6,1,4,1,2076,138,2,4,1,9),_FsMIVlanTunnelProtocolGmrpPktsRecvd_Type())
fsMIVlanTunnelProtocolGmrpPktsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolGmrpPktsRecvd.setStatus(_A)
_FsMIVlanTunnelProtocolGmrpPktsSent_Type=Counter32
_FsMIVlanTunnelProtocolGmrpPktsSent_Object=MibTableColumn
fsMIVlanTunnelProtocolGmrpPktsSent=_FsMIVlanTunnelProtocolGmrpPktsSent_Object((1,3,6,1,4,1,2076,138,2,4,1,10),_FsMIVlanTunnelProtocolGmrpPktsSent_Type())
fsMIVlanTunnelProtocolGmrpPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolGmrpPktsSent.setStatus(_A)
_FsMIVlanTunnelProtocolIgmpPktsRecvd_Type=Counter32
_FsMIVlanTunnelProtocolIgmpPktsRecvd_Object=MibTableColumn
fsMIVlanTunnelProtocolIgmpPktsRecvd=_FsMIVlanTunnelProtocolIgmpPktsRecvd_Object((1,3,6,1,4,1,2076,138,2,4,1,11),_FsMIVlanTunnelProtocolIgmpPktsRecvd_Type())
fsMIVlanTunnelProtocolIgmpPktsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolIgmpPktsRecvd.setStatus(_A)
_FsMIVlanTunnelProtocolIgmpPktsSent_Type=Counter32
_FsMIVlanTunnelProtocolIgmpPktsSent_Object=MibTableColumn
fsMIVlanTunnelProtocolIgmpPktsSent=_FsMIVlanTunnelProtocolIgmpPktsSent_Object((1,3,6,1,4,1,2076,138,2,4,1,12),_FsMIVlanTunnelProtocolIgmpPktsSent_Type())
fsMIVlanTunnelProtocolIgmpPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolIgmpPktsSent.setStatus(_A)
_FsMIVlanTunnelProtocolMvrpPktsRecvd_Type=Counter32
_FsMIVlanTunnelProtocolMvrpPktsRecvd_Object=MibTableColumn
fsMIVlanTunnelProtocolMvrpPktsRecvd=_FsMIVlanTunnelProtocolMvrpPktsRecvd_Object((1,3,6,1,4,1,2076,138,2,4,1,13),_FsMIVlanTunnelProtocolMvrpPktsRecvd_Type())
fsMIVlanTunnelProtocolMvrpPktsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolMvrpPktsRecvd.setStatus(_A)
_FsMIVlanTunnelProtocolMvrpPktsSent_Type=Counter32
_FsMIVlanTunnelProtocolMvrpPktsSent_Object=MibTableColumn
fsMIVlanTunnelProtocolMvrpPktsSent=_FsMIVlanTunnelProtocolMvrpPktsSent_Object((1,3,6,1,4,1,2076,138,2,4,1,14),_FsMIVlanTunnelProtocolMvrpPktsSent_Type())
fsMIVlanTunnelProtocolMvrpPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolMvrpPktsSent.setStatus(_A)
_FsMIVlanTunnelProtocolMmrpPktsRecvd_Type=Counter32
_FsMIVlanTunnelProtocolMmrpPktsRecvd_Object=MibTableColumn
fsMIVlanTunnelProtocolMmrpPktsRecvd=_FsMIVlanTunnelProtocolMmrpPktsRecvd_Object((1,3,6,1,4,1,2076,138,2,4,1,15),_FsMIVlanTunnelProtocolMmrpPktsRecvd_Type())
fsMIVlanTunnelProtocolMmrpPktsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolMmrpPktsRecvd.setStatus(_A)
_FsMIVlanTunnelProtocolMmrpPktsSent_Type=Counter32
_FsMIVlanTunnelProtocolMmrpPktsSent_Object=MibTableColumn
fsMIVlanTunnelProtocolMmrpPktsSent=_FsMIVlanTunnelProtocolMmrpPktsSent_Object((1,3,6,1,4,1,2076,138,2,4,1,16),_FsMIVlanTunnelProtocolMmrpPktsSent_Type())
fsMIVlanTunnelProtocolMmrpPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolMmrpPktsSent.setStatus(_A)
_FsMIVlanTunnelProtocolElmiPktsRecvd_Type=Counter32
_FsMIVlanTunnelProtocolElmiPktsRecvd_Object=MibTableColumn
fsMIVlanTunnelProtocolElmiPktsRecvd=_FsMIVlanTunnelProtocolElmiPktsRecvd_Object((1,3,6,1,4,1,2076,138,2,4,1,17),_FsMIVlanTunnelProtocolElmiPktsRecvd_Type())
fsMIVlanTunnelProtocolElmiPktsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolElmiPktsRecvd.setStatus(_A)
_FsMIVlanTunnelProtocolElmiPktsSent_Type=Counter32
_FsMIVlanTunnelProtocolElmiPktsSent_Object=MibTableColumn
fsMIVlanTunnelProtocolElmiPktsSent=_FsMIVlanTunnelProtocolElmiPktsSent_Object((1,3,6,1,4,1,2076,138,2,4,1,18),_FsMIVlanTunnelProtocolElmiPktsSent_Type())
fsMIVlanTunnelProtocolElmiPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolElmiPktsSent.setStatus(_A)
_FsMIVlanTunnelProtocolLldpPktsRecvd_Type=Counter32
_FsMIVlanTunnelProtocolLldpPktsRecvd_Object=MibTableColumn
fsMIVlanTunnelProtocolLldpPktsRecvd=_FsMIVlanTunnelProtocolLldpPktsRecvd_Object((1,3,6,1,4,1,2076,138,2,4,1,19),_FsMIVlanTunnelProtocolLldpPktsRecvd_Type())
fsMIVlanTunnelProtocolLldpPktsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolLldpPktsRecvd.setStatus(_A)
_FsMIVlanTunnelProtocolLldpPktsSent_Type=Counter32
_FsMIVlanTunnelProtocolLldpPktsSent_Object=MibTableColumn
fsMIVlanTunnelProtocolLldpPktsSent=_FsMIVlanTunnelProtocolLldpPktsSent_Object((1,3,6,1,4,1,2076,138,2,4,1,20),_FsMIVlanTunnelProtocolLldpPktsSent_Type())
fsMIVlanTunnelProtocolLldpPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolLldpPktsSent.setStatus(_A)
_FsMIVlanTunnelProtocolEcfmPktsRecvd_Type=Counter32
_FsMIVlanTunnelProtocolEcfmPktsRecvd_Object=MibTableColumn
fsMIVlanTunnelProtocolEcfmPktsRecvd=_FsMIVlanTunnelProtocolEcfmPktsRecvd_Object((1,3,6,1,4,1,2076,138,2,4,1,21),_FsMIVlanTunnelProtocolEcfmPktsRecvd_Type())
fsMIVlanTunnelProtocolEcfmPktsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolEcfmPktsRecvd.setStatus(_A)
_FsMIVlanTunnelProtocolEcfmPktsSent_Type=Counter32
_FsMIVlanTunnelProtocolEcfmPktsSent_Object=MibTableColumn
fsMIVlanTunnelProtocolEcfmPktsSent=_FsMIVlanTunnelProtocolEcfmPktsSent_Object((1,3,6,1,4,1,2076,138,2,4,1,22),_FsMIVlanTunnelProtocolEcfmPktsSent_Type())
fsMIVlanTunnelProtocolEcfmPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolEcfmPktsSent.setStatus(_A)
_FsMIVlanTunnelProtocolEoamPktsRecvd_Type=Counter32
_FsMIVlanTunnelProtocolEoamPktsRecvd_Object=MibTableColumn
fsMIVlanTunnelProtocolEoamPktsRecvd=_FsMIVlanTunnelProtocolEoamPktsRecvd_Object((1,3,6,1,4,1,2076,138,2,4,1,23),_FsMIVlanTunnelProtocolEoamPktsRecvd_Type())
fsMIVlanTunnelProtocolEoamPktsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolEoamPktsRecvd.setStatus(_A)
_FsMIVlanTunnelProtocolEoamPktsSent_Type=Counter32
_FsMIVlanTunnelProtocolEoamPktsSent_Object=MibTableColumn
fsMIVlanTunnelProtocolEoamPktsSent=_FsMIVlanTunnelProtocolEoamPktsSent_Object((1,3,6,1,4,1,2076,138,2,4,1,24),_FsMIVlanTunnelProtocolEoamPktsSent_Type())
fsMIVlanTunnelProtocolEoamPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanTunnelProtocolEoamPktsSent.setStatus(_A)
_FsMIServiceVlanTunnelProtocolTable_Object=MibTable
fsMIServiceVlanTunnelProtocolTable=_FsMIServiceVlanTunnelProtocolTable_Object((1,3,6,1,4,1,2076,138,2,5))
if mibBuilder.loadTexts:fsMIServiceVlanTunnelProtocolTable.setStatus(_A)
_FsMIServiceVlanTunnelProtocolEntry_Object=MibTableRow
fsMIServiceVlanTunnelProtocolEntry=_FsMIServiceVlanTunnelProtocolEntry_Object((1,3,6,1,4,1,2076,138,2,5,1))
fsMIServiceVlanTunnelProtocolEntry.setIndexNames((0,_D,_G),(0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:fsMIServiceVlanTunnelProtocolEntry.setStatus(_A)
_FsMIServiceVlanId_Type=VlanId
_FsMIServiceVlanId_Object=MibTableColumn
fsMIServiceVlanId=_FsMIServiceVlanId_Object((1,3,6,1,4,1,2076,138,2,5,1,1),_FsMIServiceVlanId_Type())
fsMIServiceVlanId.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIServiceVlanId.setStatus(_A)
_FsMIServiceProtocolEnum_Type=L2CPProtocols
_FsMIServiceProtocolEnum_Object=MibTableColumn
fsMIServiceProtocolEnum=_FsMIServiceProtocolEnum_Object((1,3,6,1,4,1,2076,138,2,5,1,2),_FsMIServiceProtocolEnum_Type())
fsMIServiceProtocolEnum.setMaxAccess(_H)
if mibBuilder.loadTexts:fsMIServiceProtocolEnum.setStatus(_A)
_FsMIServiceVlanRsvdMacaddress_Type=MacAddress
_FsMIServiceVlanRsvdMacaddress_Object=MibTableColumn
fsMIServiceVlanRsvdMacaddress=_FsMIServiceVlanRsvdMacaddress_Object((1,3,6,1,4,1,2076,138,2,5,1,3),_FsMIServiceVlanRsvdMacaddress_Type())
fsMIServiceVlanRsvdMacaddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIServiceVlanRsvdMacaddress.setStatus(_A)
_FsMIServiceVlanTunnelMacaddress_Type=MacAddress
_FsMIServiceVlanTunnelMacaddress_Object=MibTableColumn
fsMIServiceVlanTunnelMacaddress=_FsMIServiceVlanTunnelMacaddress_Object((1,3,6,1,4,1,2076,138,2,5,1,4),_FsMIServiceVlanTunnelMacaddress_Type())
fsMIServiceVlanTunnelMacaddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIServiceVlanTunnelMacaddress.setStatus(_A)
_FsMIServiceVlanTunnelProtocolStatus_Type=TunnelStatus
_FsMIServiceVlanTunnelProtocolStatus_Object=MibTableColumn
fsMIServiceVlanTunnelProtocolStatus=_FsMIServiceVlanTunnelProtocolStatus_Object((1,3,6,1,4,1,2076,138,2,5,1,5),_FsMIServiceVlanTunnelProtocolStatus_Type())
fsMIServiceVlanTunnelProtocolStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsMIServiceVlanTunnelProtocolStatus.setStatus(_A)
_FsMIServiceVlanTunnelPktsRecvd_Type=Counter32
_FsMIServiceVlanTunnelPktsRecvd_Object=MibTableColumn
fsMIServiceVlanTunnelPktsRecvd=_FsMIServiceVlanTunnelPktsRecvd_Object((1,3,6,1,4,1,2076,138,2,5,1,6),_FsMIServiceVlanTunnelPktsRecvd_Type())
fsMIServiceVlanTunnelPktsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIServiceVlanTunnelPktsRecvd.setStatus(_A)
_FsMIServiceVlanTunnelPktsSent_Type=Counter32
_FsMIServiceVlanTunnelPktsSent_Object=MibTableColumn
fsMIServiceVlanTunnelPktsSent=_FsMIServiceVlanTunnelPktsSent_Object((1,3,6,1,4,1,2076,138,2,5,1,7),_FsMIServiceVlanTunnelPktsSent_Type())
fsMIServiceVlanTunnelPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIServiceVlanTunnelPktsSent.setStatus(_A)
_FsMIServiceVlanDiscardPktsRx_Type=Counter32
_FsMIServiceVlanDiscardPktsRx_Object=MibTableColumn
fsMIServiceVlanDiscardPktsRx=_FsMIServiceVlanDiscardPktsRx_Object((1,3,6,1,4,1,2076,138,2,5,1,8),_FsMIServiceVlanDiscardPktsRx_Type())
fsMIServiceVlanDiscardPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIServiceVlanDiscardPktsRx.setStatus(_A)
_FsMIServiceVlanDiscardPktsTx_Type=Counter32
_FsMIServiceVlanDiscardPktsTx_Object=MibTableColumn
fsMIServiceVlanDiscardPktsTx=_FsMIServiceVlanDiscardPktsTx_Object((1,3,6,1,4,1,2076,138,2,5,1,9),_FsMIServiceVlanDiscardPktsTx_Type())
fsMIServiceVlanDiscardPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIServiceVlanDiscardPktsTx.setStatus(_A)
_FsMIVlanDiscardObjects_ObjectIdentity=ObjectIdentity
fsMIVlanDiscardObjects=_FsMIVlanDiscardObjects_ObjectIdentity((1,3,6,1,4,1,2076,138,3))
_FsMIVlanDiscardStatsTable_Object=MibTable
fsMIVlanDiscardStatsTable=_FsMIVlanDiscardStatsTable_Object((1,3,6,1,4,1,2076,138,3,1))
if mibBuilder.loadTexts:fsMIVlanDiscardStatsTable.setStatus(_A)
_FsMIVlanDiscardStatsEntry_Object=MibTableRow
fsMIVlanDiscardStatsEntry=_FsMIVlanDiscardStatsEntry_Object((1,3,6,1,4,1,2076,138,3,1,1))
fsMIVlanDiscardStatsEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:fsMIVlanDiscardStatsEntry.setStatus(_A)
_FsMIVlanDiscardDot1xPktsRx_Type=Counter32
_FsMIVlanDiscardDot1xPktsRx_Object=MibTableColumn
fsMIVlanDiscardDot1xPktsRx=_FsMIVlanDiscardDot1xPktsRx_Object((1,3,6,1,4,1,2076,138,3,1,1,1),_FsMIVlanDiscardDot1xPktsRx_Type())
fsMIVlanDiscardDot1xPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanDiscardDot1xPktsRx.setStatus(_A)
_FsMIVlanDiscardDot1xPktsTx_Type=Counter32
_FsMIVlanDiscardDot1xPktsTx_Object=MibTableColumn
fsMIVlanDiscardDot1xPktsTx=_FsMIVlanDiscardDot1xPktsTx_Object((1,3,6,1,4,1,2076,138,3,1,1,2),_FsMIVlanDiscardDot1xPktsTx_Type())
fsMIVlanDiscardDot1xPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanDiscardDot1xPktsTx.setStatus(_A)
_FsMIVlanDiscardLacpPktsRx_Type=Counter32
_FsMIVlanDiscardLacpPktsRx_Object=MibTableColumn
fsMIVlanDiscardLacpPktsRx=_FsMIVlanDiscardLacpPktsRx_Object((1,3,6,1,4,1,2076,138,3,1,1,3),_FsMIVlanDiscardLacpPktsRx_Type())
fsMIVlanDiscardLacpPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanDiscardLacpPktsRx.setStatus(_A)
_FsMIVlanDiscardLacpPktsTx_Type=Counter32
_FsMIVlanDiscardLacpPktsTx_Object=MibTableColumn
fsMIVlanDiscardLacpPktsTx=_FsMIVlanDiscardLacpPktsTx_Object((1,3,6,1,4,1,2076,138,3,1,1,4),_FsMIVlanDiscardLacpPktsTx_Type())
fsMIVlanDiscardLacpPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanDiscardLacpPktsTx.setStatus(_A)
_FsMIVlanDiscardStpPDUsRx_Type=Counter32
_FsMIVlanDiscardStpPDUsRx_Object=MibTableColumn
fsMIVlanDiscardStpPDUsRx=_FsMIVlanDiscardStpPDUsRx_Object((1,3,6,1,4,1,2076,138,3,1,1,5),_FsMIVlanDiscardStpPDUsRx_Type())
fsMIVlanDiscardStpPDUsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanDiscardStpPDUsRx.setStatus(_A)
_FsMIVlanDiscardStpPDUsTx_Type=Counter32
_FsMIVlanDiscardStpPDUsTx_Object=MibTableColumn
fsMIVlanDiscardStpPDUsTx=_FsMIVlanDiscardStpPDUsTx_Object((1,3,6,1,4,1,2076,138,3,1,1,6),_FsMIVlanDiscardStpPDUsTx_Type())
fsMIVlanDiscardStpPDUsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanDiscardStpPDUsTx.setStatus(_A)
_FsMIVlanDiscardGvrpPktsRx_Type=Counter32
_FsMIVlanDiscardGvrpPktsRx_Object=MibTableColumn
fsMIVlanDiscardGvrpPktsRx=_FsMIVlanDiscardGvrpPktsRx_Object((1,3,6,1,4,1,2076,138,3,1,1,7),_FsMIVlanDiscardGvrpPktsRx_Type())
fsMIVlanDiscardGvrpPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanDiscardGvrpPktsRx.setStatus(_A)
_FsMIVlanDiscardGvrpPktsTx_Type=Counter32
_FsMIVlanDiscardGvrpPktsTx_Object=MibTableColumn
fsMIVlanDiscardGvrpPktsTx=_FsMIVlanDiscardGvrpPktsTx_Object((1,3,6,1,4,1,2076,138,3,1,1,8),_FsMIVlanDiscardGvrpPktsTx_Type())
fsMIVlanDiscardGvrpPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanDiscardGvrpPktsTx.setStatus(_A)
_FsMIVlanDiscardGmrpPktsRx_Type=Counter32
_FsMIVlanDiscardGmrpPktsRx_Object=MibTableColumn
fsMIVlanDiscardGmrpPktsRx=_FsMIVlanDiscardGmrpPktsRx_Object((1,3,6,1,4,1,2076,138,3,1,1,9),_FsMIVlanDiscardGmrpPktsRx_Type())
fsMIVlanDiscardGmrpPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanDiscardGmrpPktsRx.setStatus(_A)
_FsMIVlanDiscardGmrpPktsTx_Type=Counter32
_FsMIVlanDiscardGmrpPktsTx_Object=MibTableColumn
fsMIVlanDiscardGmrpPktsTx=_FsMIVlanDiscardGmrpPktsTx_Object((1,3,6,1,4,1,2076,138,3,1,1,10),_FsMIVlanDiscardGmrpPktsTx_Type())
fsMIVlanDiscardGmrpPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanDiscardGmrpPktsTx.setStatus(_A)
_FsMIVlanDiscardIgmpPktsRx_Type=Counter32
_FsMIVlanDiscardIgmpPktsRx_Object=MibTableColumn
fsMIVlanDiscardIgmpPktsRx=_FsMIVlanDiscardIgmpPktsRx_Object((1,3,6,1,4,1,2076,138,3,1,1,11),_FsMIVlanDiscardIgmpPktsRx_Type())
fsMIVlanDiscardIgmpPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanDiscardIgmpPktsRx.setStatus(_A)
_FsMIVlanDiscardIgmpPktsTx_Type=Counter32
_FsMIVlanDiscardIgmpPktsTx_Object=MibTableColumn
fsMIVlanDiscardIgmpPktsTx=_FsMIVlanDiscardIgmpPktsTx_Object((1,3,6,1,4,1,2076,138,3,1,1,12),_FsMIVlanDiscardIgmpPktsTx_Type())
fsMIVlanDiscardIgmpPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanDiscardIgmpPktsTx.setStatus(_A)
_FsMIVlanDiscardMvrpPktsRx_Type=Counter32
_FsMIVlanDiscardMvrpPktsRx_Object=MibTableColumn
fsMIVlanDiscardMvrpPktsRx=_FsMIVlanDiscardMvrpPktsRx_Object((1,3,6,1,4,1,2076,138,3,1,1,13),_FsMIVlanDiscardMvrpPktsRx_Type())
fsMIVlanDiscardMvrpPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanDiscardMvrpPktsRx.setStatus(_A)
_FsMIVlanDiscardMvrpPktsTx_Type=Counter32
_FsMIVlanDiscardMvrpPktsTx_Object=MibTableColumn
fsMIVlanDiscardMvrpPktsTx=_FsMIVlanDiscardMvrpPktsTx_Object((1,3,6,1,4,1,2076,138,3,1,1,14),_FsMIVlanDiscardMvrpPktsTx_Type())
fsMIVlanDiscardMvrpPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanDiscardMvrpPktsTx.setStatus(_A)
_FsMIVlanDiscardMmrpPktsRx_Type=Counter32
_FsMIVlanDiscardMmrpPktsRx_Object=MibTableColumn
fsMIVlanDiscardMmrpPktsRx=_FsMIVlanDiscardMmrpPktsRx_Object((1,3,6,1,4,1,2076,138,3,1,1,15),_FsMIVlanDiscardMmrpPktsRx_Type())
fsMIVlanDiscardMmrpPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanDiscardMmrpPktsRx.setStatus(_A)
_FsMIVlanDiscardMmrpPktsTx_Type=Counter32
_FsMIVlanDiscardMmrpPktsTx_Object=MibTableColumn
fsMIVlanDiscardMmrpPktsTx=_FsMIVlanDiscardMmrpPktsTx_Object((1,3,6,1,4,1,2076,138,3,1,1,16),_FsMIVlanDiscardMmrpPktsTx_Type())
fsMIVlanDiscardMmrpPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanDiscardMmrpPktsTx.setStatus(_A)
_FsMIVlanDiscardElmiPktsRx_Type=Counter32
_FsMIVlanDiscardElmiPktsRx_Object=MibTableColumn
fsMIVlanDiscardElmiPktsRx=_FsMIVlanDiscardElmiPktsRx_Object((1,3,6,1,4,1,2076,138,3,1,1,17),_FsMIVlanDiscardElmiPktsRx_Type())
fsMIVlanDiscardElmiPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanDiscardElmiPktsRx.setStatus(_A)
_FsMIVlanDiscardElmiPktsTx_Type=Counter32
_FsMIVlanDiscardElmiPktsTx_Object=MibTableColumn
fsMIVlanDiscardElmiPktsTx=_FsMIVlanDiscardElmiPktsTx_Object((1,3,6,1,4,1,2076,138,3,1,1,18),_FsMIVlanDiscardElmiPktsTx_Type())
fsMIVlanDiscardElmiPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanDiscardElmiPktsTx.setStatus(_A)
_FsMIVlanDiscardLldpPktsRx_Type=Counter32
_FsMIVlanDiscardLldpPktsRx_Object=MibTableColumn
fsMIVlanDiscardLldpPktsRx=_FsMIVlanDiscardLldpPktsRx_Object((1,3,6,1,4,1,2076,138,3,1,1,19),_FsMIVlanDiscardLldpPktsRx_Type())
fsMIVlanDiscardLldpPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanDiscardLldpPktsRx.setStatus(_A)
_FsMIVlanDiscardLldpPktsTx_Type=Counter32
_FsMIVlanDiscardLldpPktsTx_Object=MibTableColumn
fsMIVlanDiscardLldpPktsTx=_FsMIVlanDiscardLldpPktsTx_Object((1,3,6,1,4,1,2076,138,3,1,1,20),_FsMIVlanDiscardLldpPktsTx_Type())
fsMIVlanDiscardLldpPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanDiscardLldpPktsTx.setStatus(_A)
_FsMIVlanDiscardEcfmPktsRx_Type=Counter32
_FsMIVlanDiscardEcfmPktsRx_Object=MibTableColumn
fsMIVlanDiscardEcfmPktsRx=_FsMIVlanDiscardEcfmPktsRx_Object((1,3,6,1,4,1,2076,138,3,1,1,21),_FsMIVlanDiscardEcfmPktsRx_Type())
fsMIVlanDiscardEcfmPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanDiscardEcfmPktsRx.setStatus(_A)
_FsMIVlanDiscardEcfmPktsTx_Type=Counter32
_FsMIVlanDiscardEcfmPktsTx_Object=MibTableColumn
fsMIVlanDiscardEcfmPktsTx=_FsMIVlanDiscardEcfmPktsTx_Object((1,3,6,1,4,1,2076,138,3,1,1,22),_FsMIVlanDiscardEcfmPktsTx_Type())
fsMIVlanDiscardEcfmPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanDiscardEcfmPktsTx.setStatus(_A)
_FsMIVlanDiscardEoamPktsRx_Type=Counter32
_FsMIVlanDiscardEoamPktsRx_Object=MibTableColumn
fsMIVlanDiscardEoamPktsRx=_FsMIVlanDiscardEoamPktsRx_Object((1,3,6,1,4,1,2076,138,3,1,1,23),_FsMIVlanDiscardEoamPktsRx_Type())
fsMIVlanDiscardEoamPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanDiscardEoamPktsRx.setStatus(_A)
_FsMIVlanDiscardEoamPktsTx_Type=Counter32
_FsMIVlanDiscardEoamPktsTx_Object=MibTableColumn
fsMIVlanDiscardEoamPktsTx=_FsMIVlanDiscardEoamPktsTx_Object((1,3,6,1,4,1,2076,138,3,1,1,24),_FsMIVlanDiscardEoamPktsTx_Type())
fsMIVlanDiscardEoamPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsMIVlanDiscardEoamPktsTx.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'TunnelStatus':TunnelStatus,'L2CPProtocols':L2CPProtocols,'futureMIVlanExtMIB':futureMIVlanExtMIB,'fsMIVlanSystemConfig':fsMIVlanSystemConfig,'fsMIVlanBridgeInfoTable':fsMIVlanBridgeInfoTable,'fsMIVlanBridgeInfoEntry':fsMIVlanBridgeInfoEntry,_G:fsMIVlanContextId,'fsMIVlanBridgeMode':fsMIVlanBridgeMode,'fsMIVlanTunnelObjects':fsMIVlanTunnelObjects,'fsMIVlanTunnelContextInfoTable':fsMIVlanTunnelContextInfoTable,'fsMIVlanTunnelContextInfoEntry':fsMIVlanTunnelContextInfoEntry,'fsMIVlanTunnelBpduPri':fsMIVlanTunnelBpduPri,'fsMIVlanTunnelStpAddress':fsMIVlanTunnelStpAddress,'fsMIVlanTunnelLacpAddress':fsMIVlanTunnelLacpAddress,'fsMIVlanTunnelDot1xAddress':fsMIVlanTunnelDot1xAddress,'fsMIVlanTunnelGvrpAddress':fsMIVlanTunnelGvrpAddress,'fsMIVlanTunnelGmrpAddress':fsMIVlanTunnelGmrpAddress,'fsMIVlanTunnelMvrpAddress':fsMIVlanTunnelMvrpAddress,'fsMIVlanTunnelMmrpAddress':fsMIVlanTunnelMmrpAddress,'fsMIVlanTunnelElmiAddress':fsMIVlanTunnelElmiAddress,'fsMIVlanTunnelLldpAddress':fsMIVlanTunnelLldpAddress,'fsMIVlanTunnelEcfmAddress':fsMIVlanTunnelEcfmAddress,'fsMIVlanTunnelEoamAddress':fsMIVlanTunnelEoamAddress,'fsMIVlanTunnelIgmpAddress':fsMIVlanTunnelIgmpAddress,'fsMIVlanTunnelTable':fsMIVlanTunnelTable,'fsMIVlanTunnelEntry':fsMIVlanTunnelEntry,_F:fsMIVlanPort,'fsMIVlanTunnelStatus':fsMIVlanTunnelStatus,'fsMIVlanTunnelProtocolTable':fsMIVlanTunnelProtocolTable,'fsMIVlanTunnelProtocolEntry':fsMIVlanTunnelProtocolEntry,'fsMIVlanTunnelProtocolDot1x':fsMIVlanTunnelProtocolDot1x,'fsMIVlanTunnelProtocolLacp':fsMIVlanTunnelProtocolLacp,'fsMIVlanTunnelProtocolStp':fsMIVlanTunnelProtocolStp,'fsMIVlanTunnelProtocolGvrp':fsMIVlanTunnelProtocolGvrp,'fsMIVlanTunnelProtocolGmrp':fsMIVlanTunnelProtocolGmrp,'fsMIVlanTunnelProtocolIgmp':fsMIVlanTunnelProtocolIgmp,'fsMIVlanTunnelProtocolMvrp':fsMIVlanTunnelProtocolMvrp,'fsMIVlanTunnelProtocolMmrp':fsMIVlanTunnelProtocolMmrp,'fsMIVlanTunnelProtocolElmi':fsMIVlanTunnelProtocolElmi,'fsMIVlanTunnelProtocolLldp':fsMIVlanTunnelProtocolLldp,'fsMIVlanTunnelProtocolEcfm':fsMIVlanTunnelProtocolEcfm,'fsMIVlanTunnelOverrideOption':fsMIVlanTunnelOverrideOption,'fsMIVlanTunnelProtocolEoam':fsMIVlanTunnelProtocolEoam,'fsMIVlanTunnelProtocolStatsTable':fsMIVlanTunnelProtocolStatsTable,'fsMIVlanTunnelProtocolStatsEntry':fsMIVlanTunnelProtocolStatsEntry,'fsMIVlanTunnelProtocolDot1xPktsRecvd':fsMIVlanTunnelProtocolDot1xPktsRecvd,'fsMIVlanTunnelProtocolDot1xPktsSent':fsMIVlanTunnelProtocolDot1xPktsSent,'fsMIVlanTunnelProtocolLacpPktsRecvd':fsMIVlanTunnelProtocolLacpPktsRecvd,'fsMIVlanTunnelProtocolLacpPktsSent':fsMIVlanTunnelProtocolLacpPktsSent,'fsMIVlanTunnelProtocolStpPDUsRecvd':fsMIVlanTunnelProtocolStpPDUsRecvd,'fsMIVlanTunnelProtocolStpPDUsSent':fsMIVlanTunnelProtocolStpPDUsSent,'fsMIVlanTunnelProtocolGvrpPDUsRecvd':fsMIVlanTunnelProtocolGvrpPDUsRecvd,'fsMIVlanTunnelProtocolGvrpPDUsSent':fsMIVlanTunnelProtocolGvrpPDUsSent,'fsMIVlanTunnelProtocolGmrpPktsRecvd':fsMIVlanTunnelProtocolGmrpPktsRecvd,'fsMIVlanTunnelProtocolGmrpPktsSent':fsMIVlanTunnelProtocolGmrpPktsSent,'fsMIVlanTunnelProtocolIgmpPktsRecvd':fsMIVlanTunnelProtocolIgmpPktsRecvd,'fsMIVlanTunnelProtocolIgmpPktsSent':fsMIVlanTunnelProtocolIgmpPktsSent,'fsMIVlanTunnelProtocolMvrpPktsRecvd':fsMIVlanTunnelProtocolMvrpPktsRecvd,'fsMIVlanTunnelProtocolMvrpPktsSent':fsMIVlanTunnelProtocolMvrpPktsSent,'fsMIVlanTunnelProtocolMmrpPktsRecvd':fsMIVlanTunnelProtocolMmrpPktsRecvd,'fsMIVlanTunnelProtocolMmrpPktsSent':fsMIVlanTunnelProtocolMmrpPktsSent,'fsMIVlanTunnelProtocolElmiPktsRecvd':fsMIVlanTunnelProtocolElmiPktsRecvd,'fsMIVlanTunnelProtocolElmiPktsSent':fsMIVlanTunnelProtocolElmiPktsSent,'fsMIVlanTunnelProtocolLldpPktsRecvd':fsMIVlanTunnelProtocolLldpPktsRecvd,'fsMIVlanTunnelProtocolLldpPktsSent':fsMIVlanTunnelProtocolLldpPktsSent,'fsMIVlanTunnelProtocolEcfmPktsRecvd':fsMIVlanTunnelProtocolEcfmPktsRecvd,'fsMIVlanTunnelProtocolEcfmPktsSent':fsMIVlanTunnelProtocolEcfmPktsSent,'fsMIVlanTunnelProtocolEoamPktsRecvd':fsMIVlanTunnelProtocolEoamPktsRecvd,'fsMIVlanTunnelProtocolEoamPktsSent':fsMIVlanTunnelProtocolEoamPktsSent,'fsMIServiceVlanTunnelProtocolTable':fsMIServiceVlanTunnelProtocolTable,'fsMIServiceVlanTunnelProtocolEntry':fsMIServiceVlanTunnelProtocolEntry,_J:fsMIServiceVlanId,_K:fsMIServiceProtocolEnum,'fsMIServiceVlanRsvdMacaddress':fsMIServiceVlanRsvdMacaddress,'fsMIServiceVlanTunnelMacaddress':fsMIServiceVlanTunnelMacaddress,'fsMIServiceVlanTunnelProtocolStatus':fsMIServiceVlanTunnelProtocolStatus,'fsMIServiceVlanTunnelPktsRecvd':fsMIServiceVlanTunnelPktsRecvd,'fsMIServiceVlanTunnelPktsSent':fsMIServiceVlanTunnelPktsSent,'fsMIServiceVlanDiscardPktsRx':fsMIServiceVlanDiscardPktsRx,'fsMIServiceVlanDiscardPktsTx':fsMIServiceVlanDiscardPktsTx,'fsMIVlanDiscardObjects':fsMIVlanDiscardObjects,'fsMIVlanDiscardStatsTable':fsMIVlanDiscardStatsTable,'fsMIVlanDiscardStatsEntry':fsMIVlanDiscardStatsEntry,'fsMIVlanDiscardDot1xPktsRx':fsMIVlanDiscardDot1xPktsRx,'fsMIVlanDiscardDot1xPktsTx':fsMIVlanDiscardDot1xPktsTx,'fsMIVlanDiscardLacpPktsRx':fsMIVlanDiscardLacpPktsRx,'fsMIVlanDiscardLacpPktsTx':fsMIVlanDiscardLacpPktsTx,'fsMIVlanDiscardStpPDUsRx':fsMIVlanDiscardStpPDUsRx,'fsMIVlanDiscardStpPDUsTx':fsMIVlanDiscardStpPDUsTx,'fsMIVlanDiscardGvrpPktsRx':fsMIVlanDiscardGvrpPktsRx,'fsMIVlanDiscardGvrpPktsTx':fsMIVlanDiscardGvrpPktsTx,'fsMIVlanDiscardGmrpPktsRx':fsMIVlanDiscardGmrpPktsRx,'fsMIVlanDiscardGmrpPktsTx':fsMIVlanDiscardGmrpPktsTx,'fsMIVlanDiscardIgmpPktsRx':fsMIVlanDiscardIgmpPktsRx,'fsMIVlanDiscardIgmpPktsTx':fsMIVlanDiscardIgmpPktsTx,'fsMIVlanDiscardMvrpPktsRx':fsMIVlanDiscardMvrpPktsRx,'fsMIVlanDiscardMvrpPktsTx':fsMIVlanDiscardMvrpPktsTx,'fsMIVlanDiscardMmrpPktsRx':fsMIVlanDiscardMmrpPktsRx,'fsMIVlanDiscardMmrpPktsTx':fsMIVlanDiscardMmrpPktsTx,'fsMIVlanDiscardElmiPktsRx':fsMIVlanDiscardElmiPktsRx,'fsMIVlanDiscardElmiPktsTx':fsMIVlanDiscardElmiPktsTx,'fsMIVlanDiscardLldpPktsRx':fsMIVlanDiscardLldpPktsRx,'fsMIVlanDiscardLldpPktsTx':fsMIVlanDiscardLldpPktsTx,'fsMIVlanDiscardEcfmPktsRx':fsMIVlanDiscardEcfmPktsRx,'fsMIVlanDiscardEcfmPktsTx':fsMIVlanDiscardEcfmPktsTx,'fsMIVlanDiscardEoamPktsRx':fsMIVlanDiscardEoamPktsRx,'fsMIVlanDiscardEoamPktsTx':fsMIVlanDiscardEoamPktsTx})