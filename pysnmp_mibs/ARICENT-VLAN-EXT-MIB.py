_J='fsServiceProtocolEnum'
_I='fsServiceVlanId'
_H='not-accessible'
_G='EnabledStatus'
_F='fsVlanPort'
_E='Integer32'
_D='ARICENT-VLAN-EXT-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
VlanId,=mibBuilder.importSymbols('AricentMIVlan-MIB','VlanId')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
futureVlanExtMIB=ModuleIdentity((1,3,6,1,4,1,2076,137))
if mibBuilder.loadTexts:futureVlanExtMIB.setRevisions(('2012-09-05 00:00',))
class TunnelStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('peer',1),('tunnel',2),('discard',3)))
class L2CPProtocols(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,23))
_FsVlanSystemConfig_ObjectIdentity=ObjectIdentity
fsVlanSystemConfig=_FsVlanSystemConfig_ObjectIdentity((1,3,6,1,4,1,2076,137,1))
class _FsVlanBridgeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('customerBridge',1),('providerBridge',2),('providerEdgeBridge',3),('providerCoreBridge',4),('providerBackboneICompBridge',5),('providerBackboneBCompBridge',6)))
_FsVlanBridgeMode_Type.__name__=_E
_FsVlanBridgeMode_Object=MibScalar
fsVlanBridgeMode=_FsVlanBridgeMode_Object((1,3,6,1,4,1,2076,137,1,1),_FsVlanBridgeMode_Type())
fsVlanBridgeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanBridgeMode.setStatus(_A)
_FsVlanTunnelObjects_ObjectIdentity=ObjectIdentity
fsVlanTunnelObjects=_FsVlanTunnelObjects_ObjectIdentity((1,3,6,1,4,1,2076,137,2))
class _FsVlanTunnelBpduPri_Type(Integer32):defaultValue=7;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_FsVlanTunnelBpduPri_Type.__name__=_E
_FsVlanTunnelBpduPri_Object=MibScalar
fsVlanTunnelBpduPri=_FsVlanTunnelBpduPri_Object((1,3,6,1,4,1,2076,137,2,1),_FsVlanTunnelBpduPri_Type())
fsVlanTunnelBpduPri.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelBpduPri.setStatus(_A)
_FsVlanTunnelStpAddress_Type=MacAddress
_FsVlanTunnelStpAddress_Object=MibScalar
fsVlanTunnelStpAddress=_FsVlanTunnelStpAddress_Object((1,3,6,1,4,1,2076,137,2,2),_FsVlanTunnelStpAddress_Type())
fsVlanTunnelStpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelStpAddress.setStatus(_A)
_FsVlanTunnelLacpAddress_Type=MacAddress
_FsVlanTunnelLacpAddress_Object=MibScalar
fsVlanTunnelLacpAddress=_FsVlanTunnelLacpAddress_Object((1,3,6,1,4,1,2076,137,2,3),_FsVlanTunnelLacpAddress_Type())
fsVlanTunnelLacpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelLacpAddress.setStatus(_A)
_FsVlanTunnelDot1xAddress_Type=MacAddress
_FsVlanTunnelDot1xAddress_Object=MibScalar
fsVlanTunnelDot1xAddress=_FsVlanTunnelDot1xAddress_Object((1,3,6,1,4,1,2076,137,2,4),_FsVlanTunnelDot1xAddress_Type())
fsVlanTunnelDot1xAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelDot1xAddress.setStatus(_A)
_FsVlanTunnelGvrpAddress_Type=MacAddress
_FsVlanTunnelGvrpAddress_Object=MibScalar
fsVlanTunnelGvrpAddress=_FsVlanTunnelGvrpAddress_Object((1,3,6,1,4,1,2076,137,2,5),_FsVlanTunnelGvrpAddress_Type())
fsVlanTunnelGvrpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelGvrpAddress.setStatus(_A)
_FsVlanTunnelGmrpAddress_Type=MacAddress
_FsVlanTunnelGmrpAddress_Object=MibScalar
fsVlanTunnelGmrpAddress=_FsVlanTunnelGmrpAddress_Object((1,3,6,1,4,1,2076,137,2,6),_FsVlanTunnelGmrpAddress_Type())
fsVlanTunnelGmrpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelGmrpAddress.setStatus(_A)
_FsVlanTunnelTable_Object=MibTable
fsVlanTunnelTable=_FsVlanTunnelTable_Object((1,3,6,1,4,1,2076,137,2,7))
if mibBuilder.loadTexts:fsVlanTunnelTable.setStatus(_A)
_FsVlanTunnelEntry_Object=MibTableRow
fsVlanTunnelEntry=_FsVlanTunnelEntry_Object((1,3,6,1,4,1,2076,137,2,7,1))
fsVlanTunnelEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:fsVlanTunnelEntry.setStatus(_A)
class _FsVlanPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_FsVlanPort_Type.__name__=_E
_FsVlanPort_Object=MibTableColumn
fsVlanPort=_FsVlanPort_Object((1,3,6,1,4,1,2076,137,2,7,1,1),_FsVlanPort_Type())
fsVlanPort.setMaxAccess(_H)
if mibBuilder.loadTexts:fsVlanPort.setStatus(_A)
class _FsVlanTunnelStatus_Type(EnabledStatus):defaultValue=2
_FsVlanTunnelStatus_Type.__name__=_G
_FsVlanTunnelStatus_Object=MibTableColumn
fsVlanTunnelStatus=_FsVlanTunnelStatus_Object((1,3,6,1,4,1,2076,137,2,7,1,2),_FsVlanTunnelStatus_Type())
fsVlanTunnelStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelStatus.setStatus(_A)
_FsVlanTunnelProtocolTable_Object=MibTable
fsVlanTunnelProtocolTable=_FsVlanTunnelProtocolTable_Object((1,3,6,1,4,1,2076,137,2,8))
if mibBuilder.loadTexts:fsVlanTunnelProtocolTable.setStatus(_A)
_FsVlanTunnelProtocolEntry_Object=MibTableRow
fsVlanTunnelProtocolEntry=_FsVlanTunnelProtocolEntry_Object((1,3,6,1,4,1,2076,137,2,8,1))
fsVlanTunnelProtocolEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:fsVlanTunnelProtocolEntry.setStatus(_A)
_FsVlanTunnelProtocolDot1x_Type=TunnelStatus
_FsVlanTunnelProtocolDot1x_Object=MibTableColumn
fsVlanTunnelProtocolDot1x=_FsVlanTunnelProtocolDot1x_Object((1,3,6,1,4,1,2076,137,2,8,1,1),_FsVlanTunnelProtocolDot1x_Type())
fsVlanTunnelProtocolDot1x.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelProtocolDot1x.setStatus(_A)
_FsVlanTunnelProtocolLacp_Type=TunnelStatus
_FsVlanTunnelProtocolLacp_Object=MibTableColumn
fsVlanTunnelProtocolLacp=_FsVlanTunnelProtocolLacp_Object((1,3,6,1,4,1,2076,137,2,8,1,2),_FsVlanTunnelProtocolLacp_Type())
fsVlanTunnelProtocolLacp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelProtocolLacp.setStatus(_A)
_FsVlanTunnelProtocolStp_Type=TunnelStatus
_FsVlanTunnelProtocolStp_Object=MibTableColumn
fsVlanTunnelProtocolStp=_FsVlanTunnelProtocolStp_Object((1,3,6,1,4,1,2076,137,2,8,1,3),_FsVlanTunnelProtocolStp_Type())
fsVlanTunnelProtocolStp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelProtocolStp.setStatus(_A)
_FsVlanTunnelProtocolGvrp_Type=TunnelStatus
_FsVlanTunnelProtocolGvrp_Object=MibTableColumn
fsVlanTunnelProtocolGvrp=_FsVlanTunnelProtocolGvrp_Object((1,3,6,1,4,1,2076,137,2,8,1,4),_FsVlanTunnelProtocolGvrp_Type())
fsVlanTunnelProtocolGvrp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelProtocolGvrp.setStatus(_A)
_FsVlanTunnelProtocolGmrp_Type=TunnelStatus
_FsVlanTunnelProtocolGmrp_Object=MibTableColumn
fsVlanTunnelProtocolGmrp=_FsVlanTunnelProtocolGmrp_Object((1,3,6,1,4,1,2076,137,2,8,1,5),_FsVlanTunnelProtocolGmrp_Type())
fsVlanTunnelProtocolGmrp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelProtocolGmrp.setStatus(_A)
_FsVlanTunnelProtocolIgmp_Type=TunnelStatus
_FsVlanTunnelProtocolIgmp_Object=MibTableColumn
fsVlanTunnelProtocolIgmp=_FsVlanTunnelProtocolIgmp_Object((1,3,6,1,4,1,2076,137,2,8,1,6),_FsVlanTunnelProtocolIgmp_Type())
fsVlanTunnelProtocolIgmp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelProtocolIgmp.setStatus(_A)
_FsVlanTunnelProtocolMvrp_Type=TunnelStatus
_FsVlanTunnelProtocolMvrp_Object=MibTableColumn
fsVlanTunnelProtocolMvrp=_FsVlanTunnelProtocolMvrp_Object((1,3,6,1,4,1,2076,137,2,8,1,7),_FsVlanTunnelProtocolMvrp_Type())
fsVlanTunnelProtocolMvrp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelProtocolMvrp.setStatus(_A)
_FsVlanTunnelProtocolMmrp_Type=TunnelStatus
_FsVlanTunnelProtocolMmrp_Object=MibTableColumn
fsVlanTunnelProtocolMmrp=_FsVlanTunnelProtocolMmrp_Object((1,3,6,1,4,1,2076,137,2,8,1,8),_FsVlanTunnelProtocolMmrp_Type())
fsVlanTunnelProtocolMmrp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelProtocolMmrp.setStatus(_A)
_FsVlanTunnelProtocolElmi_Type=TunnelStatus
_FsVlanTunnelProtocolElmi_Object=MibTableColumn
fsVlanTunnelProtocolElmi=_FsVlanTunnelProtocolElmi_Object((1,3,6,1,4,1,2076,137,2,8,1,9),_FsVlanTunnelProtocolElmi_Type())
fsVlanTunnelProtocolElmi.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelProtocolElmi.setStatus(_A)
_FsVlanTunnelProtocolLldp_Type=TunnelStatus
_FsVlanTunnelProtocolLldp_Object=MibTableColumn
fsVlanTunnelProtocolLldp=_FsVlanTunnelProtocolLldp_Object((1,3,6,1,4,1,2076,137,2,8,1,10),_FsVlanTunnelProtocolLldp_Type())
fsVlanTunnelProtocolLldp.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelProtocolLldp.setStatus(_A)
_FsVlanTunnelProtocolEcfm_Type=TunnelStatus
_FsVlanTunnelProtocolEcfm_Object=MibTableColumn
fsVlanTunnelProtocolEcfm=_FsVlanTunnelProtocolEcfm_Object((1,3,6,1,4,1,2076,137,2,8,1,11),_FsVlanTunnelProtocolEcfm_Type())
fsVlanTunnelProtocolEcfm.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelProtocolEcfm.setStatus(_A)
class _FsVlanTunnelOverrideOption_Type(EnabledStatus):defaultValue=2
_FsVlanTunnelOverrideOption_Type.__name__=_G
_FsVlanTunnelOverrideOption_Object=MibTableColumn
fsVlanTunnelOverrideOption=_FsVlanTunnelOverrideOption_Object((1,3,6,1,4,1,2076,137,2,8,1,12),_FsVlanTunnelOverrideOption_Type())
fsVlanTunnelOverrideOption.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelOverrideOption.setStatus(_A)
_FsVlanTunnelProtocolEoam_Type=TunnelStatus
_FsVlanTunnelProtocolEoam_Object=MibTableColumn
fsVlanTunnelProtocolEoam=_FsVlanTunnelProtocolEoam_Object((1,3,6,1,4,1,2076,137,2,8,1,13),_FsVlanTunnelProtocolEoam_Type())
fsVlanTunnelProtocolEoam.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelProtocolEoam.setStatus(_A)
_FsVlanTunnelProtocolStatsTable_Object=MibTable
fsVlanTunnelProtocolStatsTable=_FsVlanTunnelProtocolStatsTable_Object((1,3,6,1,4,1,2076,137,2,9))
if mibBuilder.loadTexts:fsVlanTunnelProtocolStatsTable.setStatus(_A)
_FsVlanTunnelProtocolStatsEntry_Object=MibTableRow
fsVlanTunnelProtocolStatsEntry=_FsVlanTunnelProtocolStatsEntry_Object((1,3,6,1,4,1,2076,137,2,9,1))
fsVlanTunnelProtocolStatsEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:fsVlanTunnelProtocolStatsEntry.setStatus(_A)
_FsVlanTunnelProtocolDot1xPktsRecvd_Type=Counter32
_FsVlanTunnelProtocolDot1xPktsRecvd_Object=MibTableColumn
fsVlanTunnelProtocolDot1xPktsRecvd=_FsVlanTunnelProtocolDot1xPktsRecvd_Object((1,3,6,1,4,1,2076,137,2,9,1,1),_FsVlanTunnelProtocolDot1xPktsRecvd_Type())
fsVlanTunnelProtocolDot1xPktsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanTunnelProtocolDot1xPktsRecvd.setStatus(_A)
_FsVlanTunnelProtocolDot1xPktsSent_Type=Counter32
_FsVlanTunnelProtocolDot1xPktsSent_Object=MibTableColumn
fsVlanTunnelProtocolDot1xPktsSent=_FsVlanTunnelProtocolDot1xPktsSent_Object((1,3,6,1,4,1,2076,137,2,9,1,2),_FsVlanTunnelProtocolDot1xPktsSent_Type())
fsVlanTunnelProtocolDot1xPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanTunnelProtocolDot1xPktsSent.setStatus(_A)
_FsVlanTunnelProtocolLacpPktsRecvd_Type=Counter32
_FsVlanTunnelProtocolLacpPktsRecvd_Object=MibTableColumn
fsVlanTunnelProtocolLacpPktsRecvd=_FsVlanTunnelProtocolLacpPktsRecvd_Object((1,3,6,1,4,1,2076,137,2,9,1,3),_FsVlanTunnelProtocolLacpPktsRecvd_Type())
fsVlanTunnelProtocolLacpPktsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanTunnelProtocolLacpPktsRecvd.setStatus(_A)
_FsVlanTunnelProtocolLacpPktsSent_Type=Counter32
_FsVlanTunnelProtocolLacpPktsSent_Object=MibTableColumn
fsVlanTunnelProtocolLacpPktsSent=_FsVlanTunnelProtocolLacpPktsSent_Object((1,3,6,1,4,1,2076,137,2,9,1,4),_FsVlanTunnelProtocolLacpPktsSent_Type())
fsVlanTunnelProtocolLacpPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanTunnelProtocolLacpPktsSent.setStatus(_A)
_FsVlanTunnelProtocolStpPDUsRecvd_Type=Counter32
_FsVlanTunnelProtocolStpPDUsRecvd_Object=MibTableColumn
fsVlanTunnelProtocolStpPDUsRecvd=_FsVlanTunnelProtocolStpPDUsRecvd_Object((1,3,6,1,4,1,2076,137,2,9,1,5),_FsVlanTunnelProtocolStpPDUsRecvd_Type())
fsVlanTunnelProtocolStpPDUsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanTunnelProtocolStpPDUsRecvd.setStatus(_A)
_FsVlanTunnelProtocolStpPDUsSent_Type=Counter32
_FsVlanTunnelProtocolStpPDUsSent_Object=MibTableColumn
fsVlanTunnelProtocolStpPDUsSent=_FsVlanTunnelProtocolStpPDUsSent_Object((1,3,6,1,4,1,2076,137,2,9,1,6),_FsVlanTunnelProtocolStpPDUsSent_Type())
fsVlanTunnelProtocolStpPDUsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanTunnelProtocolStpPDUsSent.setStatus(_A)
_FsVlanTunnelProtocolGvrpPDUsRecvd_Type=Counter32
_FsVlanTunnelProtocolGvrpPDUsRecvd_Object=MibTableColumn
fsVlanTunnelProtocolGvrpPDUsRecvd=_FsVlanTunnelProtocolGvrpPDUsRecvd_Object((1,3,6,1,4,1,2076,137,2,9,1,7),_FsVlanTunnelProtocolGvrpPDUsRecvd_Type())
fsVlanTunnelProtocolGvrpPDUsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanTunnelProtocolGvrpPDUsRecvd.setStatus(_A)
_FsVlanTunnelProtocolGvrpPDUsSent_Type=Counter32
_FsVlanTunnelProtocolGvrpPDUsSent_Object=MibTableColumn
fsVlanTunnelProtocolGvrpPDUsSent=_FsVlanTunnelProtocolGvrpPDUsSent_Object((1,3,6,1,4,1,2076,137,2,9,1,8),_FsVlanTunnelProtocolGvrpPDUsSent_Type())
fsVlanTunnelProtocolGvrpPDUsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanTunnelProtocolGvrpPDUsSent.setStatus(_A)
_FsVlanTunnelProtocolGmrpPktsRecvd_Type=Counter32
_FsVlanTunnelProtocolGmrpPktsRecvd_Object=MibTableColumn
fsVlanTunnelProtocolGmrpPktsRecvd=_FsVlanTunnelProtocolGmrpPktsRecvd_Object((1,3,6,1,4,1,2076,137,2,9,1,9),_FsVlanTunnelProtocolGmrpPktsRecvd_Type())
fsVlanTunnelProtocolGmrpPktsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanTunnelProtocolGmrpPktsRecvd.setStatus(_A)
_FsVlanTunnelProtocolGmrpPktsSent_Type=Counter32
_FsVlanTunnelProtocolGmrpPktsSent_Object=MibTableColumn
fsVlanTunnelProtocolGmrpPktsSent=_FsVlanTunnelProtocolGmrpPktsSent_Object((1,3,6,1,4,1,2076,137,2,9,1,10),_FsVlanTunnelProtocolGmrpPktsSent_Type())
fsVlanTunnelProtocolGmrpPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanTunnelProtocolGmrpPktsSent.setStatus(_A)
_FsVlanTunnelProtocolIgmpPktsRecvd_Type=Counter32
_FsVlanTunnelProtocolIgmpPktsRecvd_Object=MibTableColumn
fsVlanTunnelProtocolIgmpPktsRecvd=_FsVlanTunnelProtocolIgmpPktsRecvd_Object((1,3,6,1,4,1,2076,137,2,9,1,11),_FsVlanTunnelProtocolIgmpPktsRecvd_Type())
fsVlanTunnelProtocolIgmpPktsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanTunnelProtocolIgmpPktsRecvd.setStatus(_A)
_FsVlanTunnelProtocolIgmpPktsSent_Type=Counter32
_FsVlanTunnelProtocolIgmpPktsSent_Object=MibTableColumn
fsVlanTunnelProtocolIgmpPktsSent=_FsVlanTunnelProtocolIgmpPktsSent_Object((1,3,6,1,4,1,2076,137,2,9,1,12),_FsVlanTunnelProtocolIgmpPktsSent_Type())
fsVlanTunnelProtocolIgmpPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanTunnelProtocolIgmpPktsSent.setStatus(_A)
_FsVlanTunnelProtocolMvrpPktsRecvd_Type=Counter32
_FsVlanTunnelProtocolMvrpPktsRecvd_Object=MibTableColumn
fsVlanTunnelProtocolMvrpPktsRecvd=_FsVlanTunnelProtocolMvrpPktsRecvd_Object((1,3,6,1,4,1,2076,137,2,9,1,13),_FsVlanTunnelProtocolMvrpPktsRecvd_Type())
fsVlanTunnelProtocolMvrpPktsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanTunnelProtocolMvrpPktsRecvd.setStatus(_A)
_FsVlanTunnelProtocolMvrpPktsSent_Type=Counter32
_FsVlanTunnelProtocolMvrpPktsSent_Object=MibTableColumn
fsVlanTunnelProtocolMvrpPktsSent=_FsVlanTunnelProtocolMvrpPktsSent_Object((1,3,6,1,4,1,2076,137,2,9,1,14),_FsVlanTunnelProtocolMvrpPktsSent_Type())
fsVlanTunnelProtocolMvrpPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanTunnelProtocolMvrpPktsSent.setStatus(_A)
_FsVlanTunnelProtocolMmrpPktsRecvd_Type=Counter32
_FsVlanTunnelProtocolMmrpPktsRecvd_Object=MibTableColumn
fsVlanTunnelProtocolMmrpPktsRecvd=_FsVlanTunnelProtocolMmrpPktsRecvd_Object((1,3,6,1,4,1,2076,137,2,9,1,15),_FsVlanTunnelProtocolMmrpPktsRecvd_Type())
fsVlanTunnelProtocolMmrpPktsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanTunnelProtocolMmrpPktsRecvd.setStatus(_A)
_FsVlanTunnelProtocolMmrpPktsSent_Type=Counter32
_FsVlanTunnelProtocolMmrpPktsSent_Object=MibTableColumn
fsVlanTunnelProtocolMmrpPktsSent=_FsVlanTunnelProtocolMmrpPktsSent_Object((1,3,6,1,4,1,2076,137,2,9,1,16),_FsVlanTunnelProtocolMmrpPktsSent_Type())
fsVlanTunnelProtocolMmrpPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanTunnelProtocolMmrpPktsSent.setStatus(_A)
_FsVlanTunnelProtocolElmiPktsRecvd_Type=Counter32
_FsVlanTunnelProtocolElmiPktsRecvd_Object=MibTableColumn
fsVlanTunnelProtocolElmiPktsRecvd=_FsVlanTunnelProtocolElmiPktsRecvd_Object((1,3,6,1,4,1,2076,137,2,9,1,17),_FsVlanTunnelProtocolElmiPktsRecvd_Type())
fsVlanTunnelProtocolElmiPktsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanTunnelProtocolElmiPktsRecvd.setStatus(_A)
_FsVlanTunnelProtocolElmiPktsSent_Type=Counter32
_FsVlanTunnelProtocolElmiPktsSent_Object=MibTableColumn
fsVlanTunnelProtocolElmiPktsSent=_FsVlanTunnelProtocolElmiPktsSent_Object((1,3,6,1,4,1,2076,137,2,9,1,18),_FsVlanTunnelProtocolElmiPktsSent_Type())
fsVlanTunnelProtocolElmiPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanTunnelProtocolElmiPktsSent.setStatus(_A)
_FsVlanTunnelProtocolLldpPktsRecvd_Type=Counter32
_FsVlanTunnelProtocolLldpPktsRecvd_Object=MibTableColumn
fsVlanTunnelProtocolLldpPktsRecvd=_FsVlanTunnelProtocolLldpPktsRecvd_Object((1,3,6,1,4,1,2076,137,2,9,1,19),_FsVlanTunnelProtocolLldpPktsRecvd_Type())
fsVlanTunnelProtocolLldpPktsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanTunnelProtocolLldpPktsRecvd.setStatus(_A)
_FsVlanTunnelProtocolLldpPktsSent_Type=Counter32
_FsVlanTunnelProtocolLldpPktsSent_Object=MibTableColumn
fsVlanTunnelProtocolLldpPktsSent=_FsVlanTunnelProtocolLldpPktsSent_Object((1,3,6,1,4,1,2076,137,2,9,1,20),_FsVlanTunnelProtocolLldpPktsSent_Type())
fsVlanTunnelProtocolLldpPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanTunnelProtocolLldpPktsSent.setStatus(_A)
_FsVlanTunnelProtocolEcfmPktsRecvd_Type=Counter32
_FsVlanTunnelProtocolEcfmPktsRecvd_Object=MibTableColumn
fsVlanTunnelProtocolEcfmPktsRecvd=_FsVlanTunnelProtocolEcfmPktsRecvd_Object((1,3,6,1,4,1,2076,137,2,9,1,21),_FsVlanTunnelProtocolEcfmPktsRecvd_Type())
fsVlanTunnelProtocolEcfmPktsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanTunnelProtocolEcfmPktsRecvd.setStatus(_A)
_FsVlanTunnelProtocolEcfmPktsSent_Type=Counter32
_FsVlanTunnelProtocolEcfmPktsSent_Object=MibTableColumn
fsVlanTunnelProtocolEcfmPktsSent=_FsVlanTunnelProtocolEcfmPktsSent_Object((1,3,6,1,4,1,2076,137,2,9,1,22),_FsVlanTunnelProtocolEcfmPktsSent_Type())
fsVlanTunnelProtocolEcfmPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanTunnelProtocolEcfmPktsSent.setStatus(_A)
_FsVlanTunnelProtocolEoamPktsRecvd_Type=Counter32
_FsVlanTunnelProtocolEoamPktsRecvd_Object=MibTableColumn
fsVlanTunnelProtocolEoamPktsRecvd=_FsVlanTunnelProtocolEoamPktsRecvd_Object((1,3,6,1,4,1,2076,137,2,9,1,23),_FsVlanTunnelProtocolEoamPktsRecvd_Type())
fsVlanTunnelProtocolEoamPktsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanTunnelProtocolEoamPktsRecvd.setStatus(_A)
_FsVlanTunnelProtocolEoamPktsSent_Type=Counter32
_FsVlanTunnelProtocolEoamPktsSent_Object=MibTableColumn
fsVlanTunnelProtocolEoamPktsSent=_FsVlanTunnelProtocolEoamPktsSent_Object((1,3,6,1,4,1,2076,137,2,9,1,24),_FsVlanTunnelProtocolEoamPktsSent_Type())
fsVlanTunnelProtocolEoamPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanTunnelProtocolEoamPktsSent.setStatus(_A)
_FsVlanTunnelMvrpAddress_Type=MacAddress
_FsVlanTunnelMvrpAddress_Object=MibScalar
fsVlanTunnelMvrpAddress=_FsVlanTunnelMvrpAddress_Object((1,3,6,1,4,1,2076,137,2,10),_FsVlanTunnelMvrpAddress_Type())
fsVlanTunnelMvrpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelMvrpAddress.setStatus(_A)
_FsVlanTunnelMmrpAddress_Type=MacAddress
_FsVlanTunnelMmrpAddress_Object=MibScalar
fsVlanTunnelMmrpAddress=_FsVlanTunnelMmrpAddress_Object((1,3,6,1,4,1,2076,137,2,11),_FsVlanTunnelMmrpAddress_Type())
fsVlanTunnelMmrpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelMmrpAddress.setStatus(_A)
_FsVlanTunnelElmiAddress_Type=MacAddress
_FsVlanTunnelElmiAddress_Object=MibScalar
fsVlanTunnelElmiAddress=_FsVlanTunnelElmiAddress_Object((1,3,6,1,4,1,2076,137,2,12),_FsVlanTunnelElmiAddress_Type())
fsVlanTunnelElmiAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelElmiAddress.setStatus(_A)
_FsVlanTunnelLldpAddress_Type=MacAddress
_FsVlanTunnelLldpAddress_Object=MibScalar
fsVlanTunnelLldpAddress=_FsVlanTunnelLldpAddress_Object((1,3,6,1,4,1,2076,137,2,13),_FsVlanTunnelLldpAddress_Type())
fsVlanTunnelLldpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelLldpAddress.setStatus(_A)
class _FsVlanTransTunnelStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_FsVlanTransTunnelStatus_Type.__name__=_E
_FsVlanTransTunnelStatus_Object=MibScalar
fsVlanTransTunnelStatus=_FsVlanTransTunnelStatus_Object((1,3,6,1,4,1,2076,137,2,14),_FsVlanTransTunnelStatus_Type())
fsVlanTransTunnelStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTransTunnelStatus.setStatus(_A)
_FsServiceVlanTunnelProtocolTable_Object=MibTable
fsServiceVlanTunnelProtocolTable=_FsServiceVlanTunnelProtocolTable_Object((1,3,6,1,4,1,2076,137,2,15))
if mibBuilder.loadTexts:fsServiceVlanTunnelProtocolTable.setStatus(_A)
_FsServiceVlanTunnelProtocolEntry_Object=MibTableRow
fsServiceVlanTunnelProtocolEntry=_FsServiceVlanTunnelProtocolEntry_Object((1,3,6,1,4,1,2076,137,2,15,1))
fsServiceVlanTunnelProtocolEntry.setIndexNames((0,_D,_I),(0,_D,_J))
if mibBuilder.loadTexts:fsServiceVlanTunnelProtocolEntry.setStatus(_A)
_FsServiceVlanId_Type=VlanId
_FsServiceVlanId_Object=MibTableColumn
fsServiceVlanId=_FsServiceVlanId_Object((1,3,6,1,4,1,2076,137,2,15,1,1),_FsServiceVlanId_Type())
fsServiceVlanId.setMaxAccess(_H)
if mibBuilder.loadTexts:fsServiceVlanId.setStatus(_A)
_FsServiceProtocolEnum_Type=L2CPProtocols
_FsServiceProtocolEnum_Object=MibTableColumn
fsServiceProtocolEnum=_FsServiceProtocolEnum_Object((1,3,6,1,4,1,2076,137,2,15,1,2),_FsServiceProtocolEnum_Type())
fsServiceProtocolEnum.setMaxAccess(_H)
if mibBuilder.loadTexts:fsServiceProtocolEnum.setStatus(_A)
_FsServiceVlanRsvdMacaddress_Type=MacAddress
_FsServiceVlanRsvdMacaddress_Object=MibTableColumn
fsServiceVlanRsvdMacaddress=_FsServiceVlanRsvdMacaddress_Object((1,3,6,1,4,1,2076,137,2,15,1,3),_FsServiceVlanRsvdMacaddress_Type())
fsServiceVlanRsvdMacaddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsServiceVlanRsvdMacaddress.setStatus(_A)
_FsServiceVlanTunnelMacaddress_Type=MacAddress
_FsServiceVlanTunnelMacaddress_Object=MibTableColumn
fsServiceVlanTunnelMacaddress=_FsServiceVlanTunnelMacaddress_Object((1,3,6,1,4,1,2076,137,2,15,1,4),_FsServiceVlanTunnelMacaddress_Type())
fsServiceVlanTunnelMacaddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsServiceVlanTunnelMacaddress.setStatus(_A)
_FsServiceVlanTunnelProtocolStatus_Type=TunnelStatus
_FsServiceVlanTunnelProtocolStatus_Object=MibTableColumn
fsServiceVlanTunnelProtocolStatus=_FsServiceVlanTunnelProtocolStatus_Object((1,3,6,1,4,1,2076,137,2,15,1,5),_FsServiceVlanTunnelProtocolStatus_Type())
fsServiceVlanTunnelProtocolStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsServiceVlanTunnelProtocolStatus.setStatus(_A)
_FsServiceVlanTunnelPktsRecvd_Type=Counter32
_FsServiceVlanTunnelPktsRecvd_Object=MibTableColumn
fsServiceVlanTunnelPktsRecvd=_FsServiceVlanTunnelPktsRecvd_Object((1,3,6,1,4,1,2076,137,2,15,1,6),_FsServiceVlanTunnelPktsRecvd_Type())
fsServiceVlanTunnelPktsRecvd.setMaxAccess(_B)
if mibBuilder.loadTexts:fsServiceVlanTunnelPktsRecvd.setStatus(_A)
_FsServiceVlanTunnelPktsSent_Type=Counter32
_FsServiceVlanTunnelPktsSent_Object=MibTableColumn
fsServiceVlanTunnelPktsSent=_FsServiceVlanTunnelPktsSent_Object((1,3,6,1,4,1,2076,137,2,15,1,7),_FsServiceVlanTunnelPktsSent_Type())
fsServiceVlanTunnelPktsSent.setMaxAccess(_B)
if mibBuilder.loadTexts:fsServiceVlanTunnelPktsSent.setStatus(_A)
_FsServiceVlanDiscardPktsRx_Type=Counter32
_FsServiceVlanDiscardPktsRx_Object=MibTableColumn
fsServiceVlanDiscardPktsRx=_FsServiceVlanDiscardPktsRx_Object((1,3,6,1,4,1,2076,137,2,15,1,8),_FsServiceVlanDiscardPktsRx_Type())
fsServiceVlanDiscardPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsServiceVlanDiscardPktsRx.setStatus(_A)
_FsServiceVlanDiscardPktsTx_Type=Counter32
_FsServiceVlanDiscardPktsTx_Object=MibTableColumn
fsServiceVlanDiscardPktsTx=_FsServiceVlanDiscardPktsTx_Object((1,3,6,1,4,1,2076,137,2,15,1,9),_FsServiceVlanDiscardPktsTx_Type())
fsServiceVlanDiscardPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsServiceVlanDiscardPktsTx.setStatus(_A)
_FsVlanTunnelEcfmAddress_Type=MacAddress
_FsVlanTunnelEcfmAddress_Object=MibScalar
fsVlanTunnelEcfmAddress=_FsVlanTunnelEcfmAddress_Object((1,3,6,1,4,1,2076,137,2,16),_FsVlanTunnelEcfmAddress_Type())
fsVlanTunnelEcfmAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelEcfmAddress.setStatus(_A)
_FsVlanTunnelEoamAddress_Type=MacAddress
_FsVlanTunnelEoamAddress_Object=MibScalar
fsVlanTunnelEoamAddress=_FsVlanTunnelEoamAddress_Object((1,3,6,1,4,1,2076,137,2,17),_FsVlanTunnelEoamAddress_Type())
fsVlanTunnelEoamAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelEoamAddress.setStatus(_A)
_FsVlanTunnelIgmpAddress_Type=MacAddress
_FsVlanTunnelIgmpAddress_Object=MibScalar
fsVlanTunnelIgmpAddress=_FsVlanTunnelIgmpAddress_Object((1,3,6,1,4,1,2076,137,2,18),_FsVlanTunnelIgmpAddress_Type())
fsVlanTunnelIgmpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVlanTunnelIgmpAddress.setStatus(_A)
_FsVlanDiscardObjects_ObjectIdentity=ObjectIdentity
fsVlanDiscardObjects=_FsVlanDiscardObjects_ObjectIdentity((1,3,6,1,4,1,2076,137,3))
_FsVlanDiscardStatsTable_Object=MibTable
fsVlanDiscardStatsTable=_FsVlanDiscardStatsTable_Object((1,3,6,1,4,1,2076,137,3,1))
if mibBuilder.loadTexts:fsVlanDiscardStatsTable.setStatus(_A)
_FsVlanDiscardStatsEntry_Object=MibTableRow
fsVlanDiscardStatsEntry=_FsVlanDiscardStatsEntry_Object((1,3,6,1,4,1,2076,137,3,1,1))
fsVlanDiscardStatsEntry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:fsVlanDiscardStatsEntry.setStatus(_A)
_FsVlanDiscardDot1xPktsRx_Type=Counter32
_FsVlanDiscardDot1xPktsRx_Object=MibTableColumn
fsVlanDiscardDot1xPktsRx=_FsVlanDiscardDot1xPktsRx_Object((1,3,6,1,4,1,2076,137,3,1,1,1),_FsVlanDiscardDot1xPktsRx_Type())
fsVlanDiscardDot1xPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanDiscardDot1xPktsRx.setStatus(_A)
_FsVlanDiscardDot1xPktsTx_Type=Counter32
_FsVlanDiscardDot1xPktsTx_Object=MibTableColumn
fsVlanDiscardDot1xPktsTx=_FsVlanDiscardDot1xPktsTx_Object((1,3,6,1,4,1,2076,137,3,1,1,2),_FsVlanDiscardDot1xPktsTx_Type())
fsVlanDiscardDot1xPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanDiscardDot1xPktsTx.setStatus(_A)
_FsVlanDiscardLacpPktsRx_Type=Counter32
_FsVlanDiscardLacpPktsRx_Object=MibTableColumn
fsVlanDiscardLacpPktsRx=_FsVlanDiscardLacpPktsRx_Object((1,3,6,1,4,1,2076,137,3,1,1,3),_FsVlanDiscardLacpPktsRx_Type())
fsVlanDiscardLacpPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanDiscardLacpPktsRx.setStatus(_A)
_FsVlanDiscardLacpPktsTx_Type=Counter32
_FsVlanDiscardLacpPktsTx_Object=MibTableColumn
fsVlanDiscardLacpPktsTx=_FsVlanDiscardLacpPktsTx_Object((1,3,6,1,4,1,2076,137,3,1,1,4),_FsVlanDiscardLacpPktsTx_Type())
fsVlanDiscardLacpPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanDiscardLacpPktsTx.setStatus(_A)
_FsVlanDiscardStpPDUsRx_Type=Counter32
_FsVlanDiscardStpPDUsRx_Object=MibTableColumn
fsVlanDiscardStpPDUsRx=_FsVlanDiscardStpPDUsRx_Object((1,3,6,1,4,1,2076,137,3,1,1,5),_FsVlanDiscardStpPDUsRx_Type())
fsVlanDiscardStpPDUsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanDiscardStpPDUsRx.setStatus(_A)
_FsVlanDiscardStpPDUsTx_Type=Counter32
_FsVlanDiscardStpPDUsTx_Object=MibTableColumn
fsVlanDiscardStpPDUsTx=_FsVlanDiscardStpPDUsTx_Object((1,3,6,1,4,1,2076,137,3,1,1,6),_FsVlanDiscardStpPDUsTx_Type())
fsVlanDiscardStpPDUsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanDiscardStpPDUsTx.setStatus(_A)
_FsVlanDiscardGvrpPktsRx_Type=Counter32
_FsVlanDiscardGvrpPktsRx_Object=MibTableColumn
fsVlanDiscardGvrpPktsRx=_FsVlanDiscardGvrpPktsRx_Object((1,3,6,1,4,1,2076,137,3,1,1,7),_FsVlanDiscardGvrpPktsRx_Type())
fsVlanDiscardGvrpPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanDiscardGvrpPktsRx.setStatus(_A)
_FsVlanDiscardGvrpPktsTx_Type=Counter32
_FsVlanDiscardGvrpPktsTx_Object=MibTableColumn
fsVlanDiscardGvrpPktsTx=_FsVlanDiscardGvrpPktsTx_Object((1,3,6,1,4,1,2076,137,3,1,1,8),_FsVlanDiscardGvrpPktsTx_Type())
fsVlanDiscardGvrpPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanDiscardGvrpPktsTx.setStatus(_A)
_FsVlanDiscardGmrpPktsRx_Type=Counter32
_FsVlanDiscardGmrpPktsRx_Object=MibTableColumn
fsVlanDiscardGmrpPktsRx=_FsVlanDiscardGmrpPktsRx_Object((1,3,6,1,4,1,2076,137,3,1,1,9),_FsVlanDiscardGmrpPktsRx_Type())
fsVlanDiscardGmrpPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanDiscardGmrpPktsRx.setStatus(_A)
_FsVlanDiscardGmrpPktsTx_Type=Counter32
_FsVlanDiscardGmrpPktsTx_Object=MibTableColumn
fsVlanDiscardGmrpPktsTx=_FsVlanDiscardGmrpPktsTx_Object((1,3,6,1,4,1,2076,137,3,1,1,10),_FsVlanDiscardGmrpPktsTx_Type())
fsVlanDiscardGmrpPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanDiscardGmrpPktsTx.setStatus(_A)
_FsVlanDiscardIgmpPktsRx_Type=Counter32
_FsVlanDiscardIgmpPktsRx_Object=MibTableColumn
fsVlanDiscardIgmpPktsRx=_FsVlanDiscardIgmpPktsRx_Object((1,3,6,1,4,1,2076,137,3,1,1,11),_FsVlanDiscardIgmpPktsRx_Type())
fsVlanDiscardIgmpPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanDiscardIgmpPktsRx.setStatus(_A)
_FsVlanDiscardIgmpPktsTx_Type=Counter32
_FsVlanDiscardIgmpPktsTx_Object=MibTableColumn
fsVlanDiscardIgmpPktsTx=_FsVlanDiscardIgmpPktsTx_Object((1,3,6,1,4,1,2076,137,3,1,1,12),_FsVlanDiscardIgmpPktsTx_Type())
fsVlanDiscardIgmpPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanDiscardIgmpPktsTx.setStatus(_A)
_FsVlanDiscardMvrpPktsRx_Type=Counter32
_FsVlanDiscardMvrpPktsRx_Object=MibTableColumn
fsVlanDiscardMvrpPktsRx=_FsVlanDiscardMvrpPktsRx_Object((1,3,6,1,4,1,2076,137,3,1,1,13),_FsVlanDiscardMvrpPktsRx_Type())
fsVlanDiscardMvrpPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanDiscardMvrpPktsRx.setStatus(_A)
_FsVlanDiscardMvrpPktsTx_Type=Counter32
_FsVlanDiscardMvrpPktsTx_Object=MibTableColumn
fsVlanDiscardMvrpPktsTx=_FsVlanDiscardMvrpPktsTx_Object((1,3,6,1,4,1,2076,137,3,1,1,14),_FsVlanDiscardMvrpPktsTx_Type())
fsVlanDiscardMvrpPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanDiscardMvrpPktsTx.setStatus(_A)
_FsVlanDiscardMmrpPktsRx_Type=Counter32
_FsVlanDiscardMmrpPktsRx_Object=MibTableColumn
fsVlanDiscardMmrpPktsRx=_FsVlanDiscardMmrpPktsRx_Object((1,3,6,1,4,1,2076,137,3,1,1,15),_FsVlanDiscardMmrpPktsRx_Type())
fsVlanDiscardMmrpPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanDiscardMmrpPktsRx.setStatus(_A)
_FsVlanDiscardMmrpPktsTx_Type=Counter32
_FsVlanDiscardMmrpPktsTx_Object=MibTableColumn
fsVlanDiscardMmrpPktsTx=_FsVlanDiscardMmrpPktsTx_Object((1,3,6,1,4,1,2076,137,3,1,1,16),_FsVlanDiscardMmrpPktsTx_Type())
fsVlanDiscardMmrpPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanDiscardMmrpPktsTx.setStatus(_A)
_FsVlanDiscardElmiPktsRx_Type=Counter32
_FsVlanDiscardElmiPktsRx_Object=MibTableColumn
fsVlanDiscardElmiPktsRx=_FsVlanDiscardElmiPktsRx_Object((1,3,6,1,4,1,2076,137,3,1,1,17),_FsVlanDiscardElmiPktsRx_Type())
fsVlanDiscardElmiPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanDiscardElmiPktsRx.setStatus(_A)
_FsVlanDiscardElmiPktsTx_Type=Counter32
_FsVlanDiscardElmiPktsTx_Object=MibTableColumn
fsVlanDiscardElmiPktsTx=_FsVlanDiscardElmiPktsTx_Object((1,3,6,1,4,1,2076,137,3,1,1,18),_FsVlanDiscardElmiPktsTx_Type())
fsVlanDiscardElmiPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanDiscardElmiPktsTx.setStatus(_A)
_FsVlanDiscardLldpPktsRx_Type=Counter32
_FsVlanDiscardLldpPktsRx_Object=MibTableColumn
fsVlanDiscardLldpPktsRx=_FsVlanDiscardLldpPktsRx_Object((1,3,6,1,4,1,2076,137,3,1,1,19),_FsVlanDiscardLldpPktsRx_Type())
fsVlanDiscardLldpPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanDiscardLldpPktsRx.setStatus(_A)
_FsVlanDiscardLldpPktsTx_Type=Counter32
_FsVlanDiscardLldpPktsTx_Object=MibTableColumn
fsVlanDiscardLldpPktsTx=_FsVlanDiscardLldpPktsTx_Object((1,3,6,1,4,1,2076,137,3,1,1,20),_FsVlanDiscardLldpPktsTx_Type())
fsVlanDiscardLldpPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanDiscardLldpPktsTx.setStatus(_A)
_FsVlanDiscardEcfmPktsRx_Type=Counter32
_FsVlanDiscardEcfmPktsRx_Object=MibTableColumn
fsVlanDiscardEcfmPktsRx=_FsVlanDiscardEcfmPktsRx_Object((1,3,6,1,4,1,2076,137,3,1,1,21),_FsVlanDiscardEcfmPktsRx_Type())
fsVlanDiscardEcfmPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanDiscardEcfmPktsRx.setStatus(_A)
_FsVlanDiscardEcfmPktsTx_Type=Counter32
_FsVlanDiscardEcfmPktsTx_Object=MibTableColumn
fsVlanDiscardEcfmPktsTx=_FsVlanDiscardEcfmPktsTx_Object((1,3,6,1,4,1,2076,137,3,1,1,22),_FsVlanDiscardEcfmPktsTx_Type())
fsVlanDiscardEcfmPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanDiscardEcfmPktsTx.setStatus(_A)
_FsVlanDiscardEoamPktsRx_Type=Counter32
_FsVlanDiscardEoamPktsRx_Object=MibTableColumn
fsVlanDiscardEoamPktsRx=_FsVlanDiscardEoamPktsRx_Object((1,3,6,1,4,1,2076,137,3,1,1,23),_FsVlanDiscardEoamPktsRx_Type())
fsVlanDiscardEoamPktsRx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanDiscardEoamPktsRx.setStatus(_A)
_FsVlanDiscardEoamPktsTx_Type=Counter32
_FsVlanDiscardEoamPktsTx_Object=MibTableColumn
fsVlanDiscardEoamPktsTx=_FsVlanDiscardEoamPktsTx_Object((1,3,6,1,4,1,2076,137,3,1,1,24),_FsVlanDiscardEoamPktsTx_Type())
fsVlanDiscardEoamPktsTx.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVlanDiscardEoamPktsTx.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'TunnelStatus':TunnelStatus,'L2CPProtocols':L2CPProtocols,'futureVlanExtMIB':futureVlanExtMIB,'fsVlanSystemConfig':fsVlanSystemConfig,'fsVlanBridgeMode':fsVlanBridgeMode,'fsVlanTunnelObjects':fsVlanTunnelObjects,'fsVlanTunnelBpduPri':fsVlanTunnelBpduPri,'fsVlanTunnelStpAddress':fsVlanTunnelStpAddress,'fsVlanTunnelLacpAddress':fsVlanTunnelLacpAddress,'fsVlanTunnelDot1xAddress':fsVlanTunnelDot1xAddress,'fsVlanTunnelGvrpAddress':fsVlanTunnelGvrpAddress,'fsVlanTunnelGmrpAddress':fsVlanTunnelGmrpAddress,'fsVlanTunnelTable':fsVlanTunnelTable,'fsVlanTunnelEntry':fsVlanTunnelEntry,_F:fsVlanPort,'fsVlanTunnelStatus':fsVlanTunnelStatus,'fsVlanTunnelProtocolTable':fsVlanTunnelProtocolTable,'fsVlanTunnelProtocolEntry':fsVlanTunnelProtocolEntry,'fsVlanTunnelProtocolDot1x':fsVlanTunnelProtocolDot1x,'fsVlanTunnelProtocolLacp':fsVlanTunnelProtocolLacp,'fsVlanTunnelProtocolStp':fsVlanTunnelProtocolStp,'fsVlanTunnelProtocolGvrp':fsVlanTunnelProtocolGvrp,'fsVlanTunnelProtocolGmrp':fsVlanTunnelProtocolGmrp,'fsVlanTunnelProtocolIgmp':fsVlanTunnelProtocolIgmp,'fsVlanTunnelProtocolMvrp':fsVlanTunnelProtocolMvrp,'fsVlanTunnelProtocolMmrp':fsVlanTunnelProtocolMmrp,'fsVlanTunnelProtocolElmi':fsVlanTunnelProtocolElmi,'fsVlanTunnelProtocolLldp':fsVlanTunnelProtocolLldp,'fsVlanTunnelProtocolEcfm':fsVlanTunnelProtocolEcfm,'fsVlanTunnelOverrideOption':fsVlanTunnelOverrideOption,'fsVlanTunnelProtocolEoam':fsVlanTunnelProtocolEoam,'fsVlanTunnelProtocolStatsTable':fsVlanTunnelProtocolStatsTable,'fsVlanTunnelProtocolStatsEntry':fsVlanTunnelProtocolStatsEntry,'fsVlanTunnelProtocolDot1xPktsRecvd':fsVlanTunnelProtocolDot1xPktsRecvd,'fsVlanTunnelProtocolDot1xPktsSent':fsVlanTunnelProtocolDot1xPktsSent,'fsVlanTunnelProtocolLacpPktsRecvd':fsVlanTunnelProtocolLacpPktsRecvd,'fsVlanTunnelProtocolLacpPktsSent':fsVlanTunnelProtocolLacpPktsSent,'fsVlanTunnelProtocolStpPDUsRecvd':fsVlanTunnelProtocolStpPDUsRecvd,'fsVlanTunnelProtocolStpPDUsSent':fsVlanTunnelProtocolStpPDUsSent,'fsVlanTunnelProtocolGvrpPDUsRecvd':fsVlanTunnelProtocolGvrpPDUsRecvd,'fsVlanTunnelProtocolGvrpPDUsSent':fsVlanTunnelProtocolGvrpPDUsSent,'fsVlanTunnelProtocolGmrpPktsRecvd':fsVlanTunnelProtocolGmrpPktsRecvd,'fsVlanTunnelProtocolGmrpPktsSent':fsVlanTunnelProtocolGmrpPktsSent,'fsVlanTunnelProtocolIgmpPktsRecvd':fsVlanTunnelProtocolIgmpPktsRecvd,'fsVlanTunnelProtocolIgmpPktsSent':fsVlanTunnelProtocolIgmpPktsSent,'fsVlanTunnelProtocolMvrpPktsRecvd':fsVlanTunnelProtocolMvrpPktsRecvd,'fsVlanTunnelProtocolMvrpPktsSent':fsVlanTunnelProtocolMvrpPktsSent,'fsVlanTunnelProtocolMmrpPktsRecvd':fsVlanTunnelProtocolMmrpPktsRecvd,'fsVlanTunnelProtocolMmrpPktsSent':fsVlanTunnelProtocolMmrpPktsSent,'fsVlanTunnelProtocolElmiPktsRecvd':fsVlanTunnelProtocolElmiPktsRecvd,'fsVlanTunnelProtocolElmiPktsSent':fsVlanTunnelProtocolElmiPktsSent,'fsVlanTunnelProtocolLldpPktsRecvd':fsVlanTunnelProtocolLldpPktsRecvd,'fsVlanTunnelProtocolLldpPktsSent':fsVlanTunnelProtocolLldpPktsSent,'fsVlanTunnelProtocolEcfmPktsRecvd':fsVlanTunnelProtocolEcfmPktsRecvd,'fsVlanTunnelProtocolEcfmPktsSent':fsVlanTunnelProtocolEcfmPktsSent,'fsVlanTunnelProtocolEoamPktsRecvd':fsVlanTunnelProtocolEoamPktsRecvd,'fsVlanTunnelProtocolEoamPktsSent':fsVlanTunnelProtocolEoamPktsSent,'fsVlanTunnelMvrpAddress':fsVlanTunnelMvrpAddress,'fsVlanTunnelMmrpAddress':fsVlanTunnelMmrpAddress,'fsVlanTunnelElmiAddress':fsVlanTunnelElmiAddress,'fsVlanTunnelLldpAddress':fsVlanTunnelLldpAddress,'fsVlanTransTunnelStatus':fsVlanTransTunnelStatus,'fsServiceVlanTunnelProtocolTable':fsServiceVlanTunnelProtocolTable,'fsServiceVlanTunnelProtocolEntry':fsServiceVlanTunnelProtocolEntry,_I:fsServiceVlanId,_J:fsServiceProtocolEnum,'fsServiceVlanRsvdMacaddress':fsServiceVlanRsvdMacaddress,'fsServiceVlanTunnelMacaddress':fsServiceVlanTunnelMacaddress,'fsServiceVlanTunnelProtocolStatus':fsServiceVlanTunnelProtocolStatus,'fsServiceVlanTunnelPktsRecvd':fsServiceVlanTunnelPktsRecvd,'fsServiceVlanTunnelPktsSent':fsServiceVlanTunnelPktsSent,'fsServiceVlanDiscardPktsRx':fsServiceVlanDiscardPktsRx,'fsServiceVlanDiscardPktsTx':fsServiceVlanDiscardPktsTx,'fsVlanTunnelEcfmAddress':fsVlanTunnelEcfmAddress,'fsVlanTunnelEoamAddress':fsVlanTunnelEoamAddress,'fsVlanTunnelIgmpAddress':fsVlanTunnelIgmpAddress,'fsVlanDiscardObjects':fsVlanDiscardObjects,'fsVlanDiscardStatsTable':fsVlanDiscardStatsTable,'fsVlanDiscardStatsEntry':fsVlanDiscardStatsEntry,'fsVlanDiscardDot1xPktsRx':fsVlanDiscardDot1xPktsRx,'fsVlanDiscardDot1xPktsTx':fsVlanDiscardDot1xPktsTx,'fsVlanDiscardLacpPktsRx':fsVlanDiscardLacpPktsRx,'fsVlanDiscardLacpPktsTx':fsVlanDiscardLacpPktsTx,'fsVlanDiscardStpPDUsRx':fsVlanDiscardStpPDUsRx,'fsVlanDiscardStpPDUsTx':fsVlanDiscardStpPDUsTx,'fsVlanDiscardGvrpPktsRx':fsVlanDiscardGvrpPktsRx,'fsVlanDiscardGvrpPktsTx':fsVlanDiscardGvrpPktsTx,'fsVlanDiscardGmrpPktsRx':fsVlanDiscardGmrpPktsRx,'fsVlanDiscardGmrpPktsTx':fsVlanDiscardGmrpPktsTx,'fsVlanDiscardIgmpPktsRx':fsVlanDiscardIgmpPktsRx,'fsVlanDiscardIgmpPktsTx':fsVlanDiscardIgmpPktsTx,'fsVlanDiscardMvrpPktsRx':fsVlanDiscardMvrpPktsRx,'fsVlanDiscardMvrpPktsTx':fsVlanDiscardMvrpPktsTx,'fsVlanDiscardMmrpPktsRx':fsVlanDiscardMmrpPktsRx,'fsVlanDiscardMmrpPktsTx':fsVlanDiscardMmrpPktsTx,'fsVlanDiscardElmiPktsRx':fsVlanDiscardElmiPktsRx,'fsVlanDiscardElmiPktsTx':fsVlanDiscardElmiPktsTx,'fsVlanDiscardLldpPktsRx':fsVlanDiscardLldpPktsRx,'fsVlanDiscardLldpPktsTx':fsVlanDiscardLldpPktsTx,'fsVlanDiscardEcfmPktsRx':fsVlanDiscardEcfmPktsRx,'fsVlanDiscardEcfmPktsTx':fsVlanDiscardEcfmPktsTx,'fsVlanDiscardEoamPktsRx':fsVlanDiscardEoamPktsRx,'fsVlanDiscardEoamPktsTx':fsVlanDiscardEoamPktsTx})