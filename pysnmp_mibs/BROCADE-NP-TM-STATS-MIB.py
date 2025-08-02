_A3='brcdNPLPMRAMErrorCurrentEvents'
_A2='brcdNPLPMRAMErrorDescription'
_A1='brcdNPLPMRAMErrorName'
_A0='brcdNPCSRAMErrorCurrentEvents'
_z='brcdNPCSRAMErrorDescription'
_y='brcdNPBufferErrorEgressCurrentEvents'
_x='brcdNPBufferErrorIngressCurrentEvents'
_w='brcdTMDestUcastQStatPriority'
_v='brcdTMDestUcastQStatDestIfIndex'
_u='brcdTMCpuQInfoTMDeviceId'
_t='brcdTMCpuQInfoSlotId'
_s='brcdTMMcastStreamQStatsGroupPrefixLength'
_r='brcdTMMcastStreamQStatsGroup'
_q='brcdTMMcastStreamQStatsSource'
_p='brcdTMMcastStreamQStatsAddressType'
_o='brcdTMCpuQStatsType'
_n='priority7And8'
_m='priority5And6'
_l='priority3And4'
_k='priority1And2'
_j='brcdTMMcastQStatsPriority'
_i='brcdTMMcastQStatsTMDeviceId'
_h='brcdTMMcastQStatsSlotId'
_g='brcdTMUcastQStatsPriority'
_f='brcdTMUcastQStatsDstIfIndex'
_e='brcdTMUcastQStatsTMDeviceId'
_d='brcdTMUcastQStatsSlotId'
_c='brcdTMStatsTMDeviceId'
_b='brcdTMStatsSlotId'
_a='brcdNPDebugStatNPDeviceId'
_Z='brcdNPDebugStatSlotId'
_Y='brcdNPLPMRAMErrorDeviceId'
_X='brcdNPLPMRAMErrorSlotId'
_W='brcdNPLPMRAMErrorIndex'
_V='brcdNPCSRAMErrorDeviceId'
_U='brcdNPCSRAMErrorSlotId'
_T='brcdNPBufferErrorDeviceId'
_S='brcdNPBufferErrorSlotId'
_R='brcdNPQosStatQosPriority'
_Q='brcdNPQosStatIfIndex'
_P='brcdNPStatsIfIndex'
_O='brcdNPNotificationSupportDeviceId'
_N='brcdNPNotificationSupportSlotId'
_M='Unsigned32'
_L='brcdNPBufferErrorDescription'
_K='brcdTMCpuQStatsPriority'
_J='brcdTMCpuQStatsTMDeviceId'
_I='brcdTMCpuQStatsSlotId'
_H='accessible-for-notify'
_G='Integer32'
_F='brcdNPNotificationSupportErrorType'
_E='brcdNPNotificationSupportDescription'
_D='not-accessible'
_C='BROCADE-NP-TM-STATS-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
platform,=mibBuilder.importSymbols('FOUNDRY-SN-ROOT-MIB','platform')
PortPriorityTC,=mibBuilder.importSymbols('FOUNDRY-SN-SWITCH-GROUP-MIB','PortPriorityTC')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressPrefixLength,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressPrefixLength','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_M,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
brocadeNPTMStatsMIB=ModuleIdentity((1,3,6,1,4,1,1991,1,14,2))
if mibBuilder.loadTexts:brocadeNPTMStatsMIB.setRevisions(('2013-04-25 00:00','2013-02-22 00:00','2013-02-11 00:00','2012-07-04 00:00','2012-05-18 00:00','2012-04-25 00:00','2011-11-18 00:00','2011-09-28 00:00','2010-09-02 00:00'))
_BrcdNPTMMIBNotification_ObjectIdentity=ObjectIdentity
brcdNPTMMIBNotification=_BrcdNPTMMIBNotification_ObjectIdentity((1,3,6,1,4,1,1991,1,14,2,0))
_BrcdNPNotificationSupportTable_Object=MibTable
brcdNPNotificationSupportTable=_BrcdNPNotificationSupportTable_Object((1,3,6,1,4,1,1991,1,14,2,0,5))
if mibBuilder.loadTexts:brcdNPNotificationSupportTable.setStatus(_A)
_BrcdNPNotificationSupportEntry_Object=MibTableRow
brcdNPNotificationSupportEntry=_BrcdNPNotificationSupportEntry_Object((1,3,6,1,4,1,1991,1,14,2,0,5,1))
brcdNPNotificationSupportEntry.setIndexNames((0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:brcdNPNotificationSupportEntry.setStatus(_A)
_BrcdNPNotificationSupportSlotId_Type=Unsigned32
_BrcdNPNotificationSupportSlotId_Object=MibTableColumn
brcdNPNotificationSupportSlotId=_BrcdNPNotificationSupportSlotId_Object((1,3,6,1,4,1,1991,1,14,2,0,5,1,1),_BrcdNPNotificationSupportSlotId_Type())
brcdNPNotificationSupportSlotId.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdNPNotificationSupportSlotId.setStatus(_A)
_BrcdNPNotificationSupportDeviceId_Type=Unsigned32
_BrcdNPNotificationSupportDeviceId_Object=MibTableColumn
brcdNPNotificationSupportDeviceId=_BrcdNPNotificationSupportDeviceId_Object((1,3,6,1,4,1,1991,1,14,2,0,5,1,2),_BrcdNPNotificationSupportDeviceId_Type())
brcdNPNotificationSupportDeviceId.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdNPNotificationSupportDeviceId.setStatus(_A)
_BrcdNPNotificationSupportDescription_Type=DisplayString
_BrcdNPNotificationSupportDescription_Object=MibTableColumn
brcdNPNotificationSupportDescription=_BrcdNPNotificationSupportDescription_Object((1,3,6,1,4,1,1991,1,14,2,0,5,1,3),_BrcdNPNotificationSupportDescription_Type())
brcdNPNotificationSupportDescription.setMaxAccess(_H)
if mibBuilder.loadTexts:brcdNPNotificationSupportDescription.setStatus(_A)
_BrcdNPNotificationSupportErrorType_Type=DisplayString
_BrcdNPNotificationSupportErrorType_Object=MibTableColumn
brcdNPNotificationSupportErrorType=_BrcdNPNotificationSupportErrorType_Object((1,3,6,1,4,1,1991,1,14,2,0,5,1,4),_BrcdNPNotificationSupportErrorType_Type())
brcdNPNotificationSupportErrorType.setMaxAccess(_H)
if mibBuilder.loadTexts:brcdNPNotificationSupportErrorType.setStatus(_A)
_BrcdNPTMMIBObjects_ObjectIdentity=ObjectIdentity
brcdNPTMMIBObjects=_BrcdNPTMMIBObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,14,2,1))
_BrcdNPStatisticsInfo_ObjectIdentity=ObjectIdentity
brcdNPStatisticsInfo=_BrcdNPStatisticsInfo_ObjectIdentity((1,3,6,1,4,1,1991,1,14,2,1,1))
_BrcdNPStatsTable_Object=MibTable
brcdNPStatsTable=_BrcdNPStatsTable_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1))
if mibBuilder.loadTexts:brcdNPStatsTable.setStatus(_A)
_BrcdNPStatsEntry_Object=MibTableRow
brcdNPStatsEntry=_BrcdNPStatsEntry_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1))
brcdNPStatsEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:brcdNPStatsEntry.setStatus(_A)
_BrcdNPStatsIfIndex_Type=InterfaceIndex
_BrcdNPStatsIfIndex_Object=MibTableColumn
brcdNPStatsIfIndex=_BrcdNPStatsIfIndex_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,1),_BrcdNPStatsIfIndex_Type())
brcdNPStatsIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdNPStatsIfIndex.setStatus(_A)
_BrcdNPStatsRxRawGoodPkts_Type=Counter64
_BrcdNPStatsRxRawGoodPkts_Object=MibTableColumn
brcdNPStatsRxRawGoodPkts=_BrcdNPStatsRxRawGoodPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,2),_BrcdNPStatsRxRawGoodPkts_Type())
brcdNPStatsRxRawGoodPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxRawGoodPkts.setStatus(_A)
_BrcdNPStatsRxForwardPkts_Type=Counter64
_BrcdNPStatsRxForwardPkts_Object=MibTableColumn
brcdNPStatsRxForwardPkts=_BrcdNPStatsRxForwardPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,3),_BrcdNPStatsRxForwardPkts_Type())
brcdNPStatsRxForwardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxForwardPkts.setStatus(_A)
_BrcdNPStatsRxDiscardPkts_Type=Counter64
_BrcdNPStatsRxDiscardPkts_Object=MibTableColumn
brcdNPStatsRxDiscardPkts=_BrcdNPStatsRxDiscardPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,4),_BrcdNPStatsRxDiscardPkts_Type())
brcdNPStatsRxDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxDiscardPkts.setStatus(_A)
_BrcdNPStatsRxMiscPkts_Type=Counter64
_BrcdNPStatsRxMiscPkts_Object=MibTableColumn
brcdNPStatsRxMiscPkts=_BrcdNPStatsRxMiscPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,5),_BrcdNPStatsRxMiscPkts_Type())
brcdNPStatsRxMiscPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxMiscPkts.setStatus(_A)
_BrcdNPStatsRxUnicastPkts_Type=Counter64
_BrcdNPStatsRxUnicastPkts_Object=MibTableColumn
brcdNPStatsRxUnicastPkts=_BrcdNPStatsRxUnicastPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,6),_BrcdNPStatsRxUnicastPkts_Type())
brcdNPStatsRxUnicastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxUnicastPkts.setStatus(_A)
_BrcdNPStatsRxBroadcastPkts_Type=Counter64
_BrcdNPStatsRxBroadcastPkts_Object=MibTableColumn
brcdNPStatsRxBroadcastPkts=_BrcdNPStatsRxBroadcastPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,7),_BrcdNPStatsRxBroadcastPkts_Type())
brcdNPStatsRxBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxBroadcastPkts.setStatus(_A)
_BrcdNPStatsRxMulticastPkts_Type=Counter64
_BrcdNPStatsRxMulticastPkts_Object=MibTableColumn
brcdNPStatsRxMulticastPkts=_BrcdNPStatsRxMulticastPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,8),_BrcdNPStatsRxMulticastPkts_Type())
brcdNPStatsRxMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxMulticastPkts.setStatus(_A)
_BrcdNPStatsRxSendToTMPkts_Type=Counter64
_BrcdNPStatsRxSendToTMPkts_Object=MibTableColumn
brcdNPStatsRxSendToTMPkts=_BrcdNPStatsRxSendToTMPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,9),_BrcdNPStatsRxSendToTMPkts_Type())
brcdNPStatsRxSendToTMPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxSendToTMPkts.setStatus(_A)
_BrcdNPStatsRxBadPkts_Type=Counter64
_BrcdNPStatsRxBadPkts_Object=MibTableColumn
brcdNPStatsRxBadPkts=_BrcdNPStatsRxBadPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,10),_BrcdNPStatsRxBadPkts_Type())
brcdNPStatsRxBadPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxBadPkts.setStatus(_A)
_BrcdNPStatsRxLookupUnavailable_Type=Counter64
_BrcdNPStatsRxLookupUnavailable_Object=MibTableColumn
brcdNPStatsRxLookupUnavailable=_BrcdNPStatsRxLookupUnavailable_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,11),_BrcdNPStatsRxLookupUnavailable_Type())
brcdNPStatsRxLookupUnavailable.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxLookupUnavailable.setStatus(_A)
_BrcdNPStatsRxACLDrop_Type=Counter64
_BrcdNPStatsRxACLDrop_Object=MibTableColumn
brcdNPStatsRxACLDrop=_BrcdNPStatsRxACLDrop_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,12),_BrcdNPStatsRxACLDrop_Type())
brcdNPStatsRxACLDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxACLDrop.setStatus(_A)
_BrcdNPStatsRxPriority0And1Drop_Type=Counter64
_BrcdNPStatsRxPriority0And1Drop_Object=MibTableColumn
brcdNPStatsRxPriority0And1Drop=_BrcdNPStatsRxPriority0And1Drop_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,13),_BrcdNPStatsRxPriority0And1Drop_Type())
brcdNPStatsRxPriority0And1Drop.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxPriority0And1Drop.setStatus(_A)
_BrcdNPStatsRxPriority2And3Drop_Type=Counter64
_BrcdNPStatsRxPriority2And3Drop_Object=MibTableColumn
brcdNPStatsRxPriority2And3Drop=_BrcdNPStatsRxPriority2And3Drop_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,14),_BrcdNPStatsRxPriority2And3Drop_Type())
brcdNPStatsRxPriority2And3Drop.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxPriority2And3Drop.setStatus(_A)
_BrcdNPStatsRxPriority4And5Drop_Type=Counter64
_BrcdNPStatsRxPriority4And5Drop_Object=MibTableColumn
brcdNPStatsRxPriority4And5Drop=_BrcdNPStatsRxPriority4And5Drop_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,15),_BrcdNPStatsRxPriority4And5Drop_Type())
brcdNPStatsRxPriority4And5Drop.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxPriority4And5Drop.setStatus(_A)
_BrcdNPStatsRxPriority6And7Drop_Type=Counter64
_BrcdNPStatsRxPriority6And7Drop_Object=MibTableColumn
brcdNPStatsRxPriority6And7Drop=_BrcdNPStatsRxPriority6And7Drop_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,16),_BrcdNPStatsRxPriority6And7Drop_Type())
brcdNPStatsRxPriority6And7Drop.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxPriority6And7Drop.setStatus(_A)
_BrcdNPStatsRxSuppressRPFDrop_Type=Counter64
_BrcdNPStatsRxSuppressRPFDrop_Object=MibTableColumn
brcdNPStatsRxSuppressRPFDrop=_BrcdNPStatsRxSuppressRPFDrop_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,17),_BrcdNPStatsRxSuppressRPFDrop_Type())
brcdNPStatsRxSuppressRPFDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxSuppressRPFDrop.setStatus(_A)
_BrcdNPStatsRxRPFDrop_Type=Counter64
_BrcdNPStatsRxRPFDrop_Object=MibTableColumn
brcdNPStatsRxRPFDrop=_BrcdNPStatsRxRPFDrop_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,18),_BrcdNPStatsRxRPFDrop_Type())
brcdNPStatsRxRPFDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxRPFDrop.setStatus(_A)
_BrcdNPStatsRxIPv4Pkts_Type=Counter64
_BrcdNPStatsRxIPv4Pkts_Object=MibTableColumn
brcdNPStatsRxIPv4Pkts=_BrcdNPStatsRxIPv4Pkts_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,19),_BrcdNPStatsRxIPv4Pkts_Type())
brcdNPStatsRxIPv4Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxIPv4Pkts.setStatus(_A)
_BrcdNPStatsRxIPv6Pkts_Type=Counter64
_BrcdNPStatsRxIPv6Pkts_Object=MibTableColumn
brcdNPStatsRxIPv6Pkts=_BrcdNPStatsRxIPv6Pkts_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,20),_BrcdNPStatsRxIPv6Pkts_Type())
brcdNPStatsRxIPv6Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxIPv6Pkts.setStatus(_A)
_BrcdNPStatsRxRouteOnlyDrop_Type=Counter64
_BrcdNPStatsRxRouteOnlyDrop_Object=MibTableColumn
brcdNPStatsRxRouteOnlyDrop=_BrcdNPStatsRxRouteOnlyDrop_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,21),_BrcdNPStatsRxRouteOnlyDrop_Type())
brcdNPStatsRxRouteOnlyDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxRouteOnlyDrop.setStatus(_A)
_BrcdNPStatsRxIPv6SuppressRPFDrop_Type=Counter64
_BrcdNPStatsRxIPv6SuppressRPFDrop_Object=MibTableColumn
brcdNPStatsRxIPv6SuppressRPFDrop=_BrcdNPStatsRxIPv6SuppressRPFDrop_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,22),_BrcdNPStatsRxIPv6SuppressRPFDrop_Type())
brcdNPStatsRxIPv6SuppressRPFDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxIPv6SuppressRPFDrop.setStatus(_A)
_BrcdNPStatsRxIPv6RPFDropCount_Type=Counter64
_BrcdNPStatsRxIPv6RPFDropCount_Object=MibTableColumn
brcdNPStatsRxIPv6RPFDropCount=_BrcdNPStatsRxIPv6RPFDropCount_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,23),_BrcdNPStatsRxIPv6RPFDropCount_Type())
brcdNPStatsRxIPv6RPFDropCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxIPv6RPFDropCount.setStatus(_A)
_BrcdNPStatsRxIPv4Bytes_Type=Counter64
_BrcdNPStatsRxIPv4Bytes_Object=MibTableColumn
brcdNPStatsRxIPv4Bytes=_BrcdNPStatsRxIPv4Bytes_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,24),_BrcdNPStatsRxIPv4Bytes_Type())
brcdNPStatsRxIPv4Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxIPv4Bytes.setStatus(_A)
_BrcdNPStatsRxIPv6Bytes_Type=Counter64
_BrcdNPStatsRxIPv6Bytes_Object=MibTableColumn
brcdNPStatsRxIPv6Bytes=_BrcdNPStatsRxIPv6Bytes_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,25),_BrcdNPStatsRxIPv6Bytes_Type())
brcdNPStatsRxIPv6Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxIPv6Bytes.setStatus(_A)
_BrcdNPStatsRxPOSCtrlProtocolPkts_Type=Counter64
_BrcdNPStatsRxPOSCtrlProtocolPkts_Object=MibTableColumn
brcdNPStatsRxPOSCtrlProtocolPkts=_BrcdNPStatsRxPOSCtrlProtocolPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,26),_BrcdNPStatsRxPOSCtrlProtocolPkts_Type())
brcdNPStatsRxPOSCtrlProtocolPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxPOSCtrlProtocolPkts.setStatus(_A)
_BrcdNPStatsRxPOSLinkDrop_Type=Counter64
_BrcdNPStatsRxPOSLinkDrop_Object=MibTableColumn
brcdNPStatsRxPOSLinkDrop=_BrcdNPStatsRxPOSLinkDrop_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,27),_BrcdNPStatsRxPOSLinkDrop_Type())
brcdNPStatsRxPOSLinkDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxPOSLinkDrop.setStatus(_A)
_BrcdNPStatsRxRoutedPktsDrop_Type=Counter64
_BrcdNPStatsRxRoutedPktsDrop_Object=MibTableColumn
brcdNPStatsRxRoutedPktsDrop=_BrcdNPStatsRxRoutedPktsDrop_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,28),_BrcdNPStatsRxRoutedPktsDrop_Type())
brcdNPStatsRxRoutedPktsDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsRxRoutedPktsDrop.setStatus(_A)
_BrcdNPStatsTxSentToMACPkts_Type=Counter64
_BrcdNPStatsTxSentToMACPkts_Object=MibTableColumn
brcdNPStatsTxSentToMACPkts=_BrcdNPStatsTxSentToMACPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,29),_BrcdNPStatsTxSentToMACPkts_Type())
brcdNPStatsTxSentToMACPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsTxSentToMACPkts.setStatus(_A)
_BrcdNPStatsTxRawGoodPkts_Type=Counter64
_BrcdNPStatsTxRawGoodPkts_Object=MibTableColumn
brcdNPStatsTxRawGoodPkts=_BrcdNPStatsTxRawGoodPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,30),_BrcdNPStatsTxRawGoodPkts_Type())
brcdNPStatsTxRawGoodPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsTxRawGoodPkts.setStatus(_A)
_BrcdNPStatsTxSrcPortSupressDrop_Type=Counter64
_BrcdNPStatsTxSrcPortSupressDrop_Object=MibTableColumn
brcdNPStatsTxSrcPortSupressDrop=_BrcdNPStatsTxSrcPortSupressDrop_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,31),_BrcdNPStatsTxSrcPortSupressDrop_Type())
brcdNPStatsTxSrcPortSupressDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsTxSrcPortSupressDrop.setStatus(_A)
_BrcdNPStatsTxBadPktsCnt_Type=Counter64
_BrcdNPStatsTxBadPktsCnt_Object=MibTableColumn
brcdNPStatsTxBadPktsCnt=_BrcdNPStatsTxBadPktsCnt_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,32),_BrcdNPStatsTxBadPktsCnt_Type())
brcdNPStatsTxBadPktsCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsTxBadPktsCnt.setStatus(_A)
_BrcdNPStatsTxUnicastPkts_Type=Counter64
_BrcdNPStatsTxUnicastPkts_Object=MibTableColumn
brcdNPStatsTxUnicastPkts=_BrcdNPStatsTxUnicastPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,33),_BrcdNPStatsTxUnicastPkts_Type())
brcdNPStatsTxUnicastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsTxUnicastPkts.setStatus(_A)
_BrcdNPStatsTxBroadcastPkts_Type=Counter64
_BrcdNPStatsTxBroadcastPkts_Object=MibTableColumn
brcdNPStatsTxBroadcastPkts=_BrcdNPStatsTxBroadcastPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,34),_BrcdNPStatsTxBroadcastPkts_Type())
brcdNPStatsTxBroadcastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsTxBroadcastPkts.setStatus(_A)
_BrcdNPStatsTxMulticastPkts_Type=Counter64
_BrcdNPStatsTxMulticastPkts_Object=MibTableColumn
brcdNPStatsTxMulticastPkts=_BrcdNPStatsTxMulticastPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,35),_BrcdNPStatsTxMulticastPkts_Type())
brcdNPStatsTxMulticastPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsTxMulticastPkts.setStatus(_A)
_BrcdNPStatsTxReceiveFromTM_Type=Counter64
_BrcdNPStatsTxReceiveFromTM_Object=MibTableColumn
brcdNPStatsTxReceiveFromTM=_BrcdNPStatsTxReceiveFromTM_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,36),_BrcdNPStatsTxReceiveFromTM_Type())
brcdNPStatsTxReceiveFromTM.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsTxReceiveFromTM.setStatus(_A)
_BrcdNPStatsTxACLDrop_Type=Counter64
_BrcdNPStatsTxACLDrop_Object=MibTableColumn
brcdNPStatsTxACLDrop=_BrcdNPStatsTxACLDrop_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,37),_BrcdNPStatsTxACLDrop_Type())
brcdNPStatsTxACLDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsTxACLDrop.setStatus(_A)
_BrcdNPStatsTxPFCMulticastDrop_Type=Counter64
_BrcdNPStatsTxPFCMulticastDrop_Object=MibTableColumn
brcdNPStatsTxPFCMulticastDrop=_BrcdNPStatsTxPFCMulticastDrop_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,38),_BrcdNPStatsTxPFCMulticastDrop_Type())
brcdNPStatsTxPFCMulticastDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsTxPFCMulticastDrop.setStatus(_A)
_BrcdNPStatsTxPFCMTUExceedDrop_Type=Counter64
_BrcdNPStatsTxPFCMTUExceedDrop_Object=MibTableColumn
brcdNPStatsTxPFCMTUExceedDrop=_BrcdNPStatsTxPFCMTUExceedDrop_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,39),_BrcdNPStatsTxPFCMTUExceedDrop_Type())
brcdNPStatsTxPFCMTUExceedDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsTxPFCMTUExceedDrop.setStatus(_A)
_BrcdNPStatsTxPFCQMAPErrorDrop_Type=Counter64
_BrcdNPStatsTxPFCQMAPErrorDrop_Object=MibTableColumn
brcdNPStatsTxPFCQMAPErrorDrop=_BrcdNPStatsTxPFCQMAPErrorDrop_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,40),_BrcdNPStatsTxPFCQMAPErrorDrop_Type())
brcdNPStatsTxPFCQMAPErrorDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsTxPFCQMAPErrorDrop.setStatus(_A)
_BrcdNPStatsTxIPv4Pkts_Type=Counter64
_BrcdNPStatsTxIPv4Pkts_Object=MibTableColumn
brcdNPStatsTxIPv4Pkts=_BrcdNPStatsTxIPv4Pkts_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,41),_BrcdNPStatsTxIPv4Pkts_Type())
brcdNPStatsTxIPv4Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsTxIPv4Pkts.setStatus(_A)
_BrcdNPStatsTxIPv6Pkts_Type=Counter64
_BrcdNPStatsTxIPv6Pkts_Object=MibTableColumn
brcdNPStatsTxIPv6Pkts=_BrcdNPStatsTxIPv6Pkts_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,42),_BrcdNPStatsTxIPv6Pkts_Type())
brcdNPStatsTxIPv6Pkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsTxIPv6Pkts.setStatus(_A)
_BrcdNPStatsTxIPv4Bytes_Type=Counter64
_BrcdNPStatsTxIPv4Bytes_Object=MibTableColumn
brcdNPStatsTxIPv4Bytes=_BrcdNPStatsTxIPv4Bytes_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,43),_BrcdNPStatsTxIPv4Bytes_Type())
brcdNPStatsTxIPv4Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsTxIPv4Bytes.setStatus(_A)
_BrcdNPStatsTxIPv6Bytes_Type=Counter64
_BrcdNPStatsTxIPv6Bytes_Object=MibTableColumn
brcdNPStatsTxIPv6Bytes=_BrcdNPStatsTxIPv6Bytes_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,44),_BrcdNPStatsTxIPv6Bytes_Type())
brcdNPStatsTxIPv6Bytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsTxIPv6Bytes.setStatus(_A)
_BrcdNPStatsTxPOSCtrlProtocolPkts_Type=Counter64
_BrcdNPStatsTxPOSCtrlProtocolPkts_Object=MibTableColumn
brcdNPStatsTxPOSCtrlProtocolPkts=_BrcdNPStatsTxPOSCtrlProtocolPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,45),_BrcdNPStatsTxPOSCtrlProtocolPkts_Type())
brcdNPStatsTxPOSCtrlProtocolPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsTxPOSCtrlProtocolPkts.setStatus(_A)
_BrcdNPStatsTxPOSLinkDrop_Type=Counter64
_BrcdNPStatsTxPOSLinkDrop_Object=MibTableColumn
brcdNPStatsTxPOSLinkDrop=_BrcdNPStatsTxPOSLinkDrop_Object((1,3,6,1,4,1,1991,1,14,2,1,1,1,1,46),_BrcdNPStatsTxPOSLinkDrop_Type())
brcdNPStatsTxPOSLinkDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPStatsTxPOSLinkDrop.setStatus(_A)
_BrcdNPQosStatTable_Object=MibTable
brcdNPQosStatTable=_BrcdNPQosStatTable_Object((1,3,6,1,4,1,1991,1,14,2,1,1,2))
if mibBuilder.loadTexts:brcdNPQosStatTable.setStatus(_A)
_BrcdNPQosStatEntry_Object=MibTableRow
brcdNPQosStatEntry=_BrcdNPQosStatEntry_Object((1,3,6,1,4,1,1991,1,14,2,1,1,2,1))
brcdNPQosStatEntry.setIndexNames((0,_C,_Q),(0,_C,_R))
if mibBuilder.loadTexts:brcdNPQosStatEntry.setStatus(_A)
_BrcdNPQosStatIfIndex_Type=InterfaceIndex
_BrcdNPQosStatIfIndex_Object=MibTableColumn
brcdNPQosStatIfIndex=_BrcdNPQosStatIfIndex_Object((1,3,6,1,4,1,1991,1,14,2,1,1,2,1,1),_BrcdNPQosStatIfIndex_Type())
brcdNPQosStatIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdNPQosStatIfIndex.setStatus(_A)
_BrcdNPQosStatQosPriority_Type=PortPriorityTC
_BrcdNPQosStatQosPriority_Object=MibTableColumn
brcdNPQosStatQosPriority=_BrcdNPQosStatQosPriority_Object((1,3,6,1,4,1,1991,1,14,2,1,1,2,1,2),_BrcdNPQosStatQosPriority_Type())
brcdNPQosStatQosPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdNPQosStatQosPriority.setStatus(_A)
_BrcdNPQosStatIngressPkts_Type=Counter64
_BrcdNPQosStatIngressPkts_Object=MibTableColumn
brcdNPQosStatIngressPkts=_BrcdNPQosStatIngressPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,1,2,1,3),_BrcdNPQosStatIngressPkts_Type())
brcdNPQosStatIngressPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPQosStatIngressPkts.setStatus(_A)
_BrcdNPQosStatIngressBytes_Type=Counter64
_BrcdNPQosStatIngressBytes_Object=MibTableColumn
brcdNPQosStatIngressBytes=_BrcdNPQosStatIngressBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,1,2,1,4),_BrcdNPQosStatIngressBytes_Type())
brcdNPQosStatIngressBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPQosStatIngressBytes.setStatus(_A)
_BrcdNPQosStatEgressPkts_Type=Counter64
_BrcdNPQosStatEgressPkts_Object=MibTableColumn
brcdNPQosStatEgressPkts=_BrcdNPQosStatEgressPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,1,2,1,5),_BrcdNPQosStatEgressPkts_Type())
brcdNPQosStatEgressPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPQosStatEgressPkts.setStatus(_A)
_BrcdNPQosStatEgressBytes_Type=Counter64
_BrcdNPQosStatEgressBytes_Object=MibTableColumn
brcdNPQosStatEgressBytes=_BrcdNPQosStatEgressBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,1,2,1,6),_BrcdNPQosStatEgressBytes_Type())
brcdNPQosStatEgressBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPQosStatEgressBytes.setStatus(_A)
_BrcdNPBufferErrorTable_Object=MibTable
brcdNPBufferErrorTable=_BrcdNPBufferErrorTable_Object((1,3,6,1,4,1,1991,1,14,2,1,1,3))
if mibBuilder.loadTexts:brcdNPBufferErrorTable.setStatus(_A)
_BrcdNPBufferErrorEntry_Object=MibTableRow
brcdNPBufferErrorEntry=_BrcdNPBufferErrorEntry_Object((1,3,6,1,4,1,1991,1,14,2,1,1,3,1))
brcdNPBufferErrorEntry.setIndexNames((0,_C,_S),(0,_C,_T))
if mibBuilder.loadTexts:brcdNPBufferErrorEntry.setStatus(_A)
_BrcdNPBufferErrorSlotId_Type=Unsigned32
_BrcdNPBufferErrorSlotId_Object=MibTableColumn
brcdNPBufferErrorSlotId=_BrcdNPBufferErrorSlotId_Object((1,3,6,1,4,1,1991,1,14,2,1,1,3,1,1),_BrcdNPBufferErrorSlotId_Type())
brcdNPBufferErrorSlotId.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdNPBufferErrorSlotId.setStatus(_A)
_BrcdNPBufferErrorDeviceId_Type=Unsigned32
_BrcdNPBufferErrorDeviceId_Object=MibTableColumn
brcdNPBufferErrorDeviceId=_BrcdNPBufferErrorDeviceId_Object((1,3,6,1,4,1,1991,1,14,2,1,1,3,1,2),_BrcdNPBufferErrorDeviceId_Type())
brcdNPBufferErrorDeviceId.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdNPBufferErrorDeviceId.setStatus(_A)
_BrcdNPBufferErrorDescription_Type=DisplayString
_BrcdNPBufferErrorDescription_Object=MibTableColumn
brcdNPBufferErrorDescription=_BrcdNPBufferErrorDescription_Object((1,3,6,1,4,1,1991,1,14,2,1,1,3,1,3),_BrcdNPBufferErrorDescription_Type())
brcdNPBufferErrorDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPBufferErrorDescription.setStatus(_A)
_BrcdNPBufferErrorIngressCurrentEvents_Type=Counter32
_BrcdNPBufferErrorIngressCurrentEvents_Object=MibTableColumn
brcdNPBufferErrorIngressCurrentEvents=_BrcdNPBufferErrorIngressCurrentEvents_Object((1,3,6,1,4,1,1991,1,14,2,1,1,3,1,4),_BrcdNPBufferErrorIngressCurrentEvents_Type())
brcdNPBufferErrorIngressCurrentEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPBufferErrorIngressCurrentEvents.setStatus(_A)
_BrcdNPBufferErrorIngressCumulativeEvents_Type=Counter32
_BrcdNPBufferErrorIngressCumulativeEvents_Object=MibTableColumn
brcdNPBufferErrorIngressCumulativeEvents=_BrcdNPBufferErrorIngressCumulativeEvents_Object((1,3,6,1,4,1,1991,1,14,2,1,1,3,1,5),_BrcdNPBufferErrorIngressCumulativeEvents_Type())
brcdNPBufferErrorIngressCumulativeEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPBufferErrorIngressCumulativeEvents.setStatus(_A)
_BrcdNPBufferErrorEgressCurrentEvents_Type=Counter32
_BrcdNPBufferErrorEgressCurrentEvents_Object=MibTableColumn
brcdNPBufferErrorEgressCurrentEvents=_BrcdNPBufferErrorEgressCurrentEvents_Object((1,3,6,1,4,1,1991,1,14,2,1,1,3,1,6),_BrcdNPBufferErrorEgressCurrentEvents_Type())
brcdNPBufferErrorEgressCurrentEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPBufferErrorEgressCurrentEvents.setStatus(_A)
_BrcdNPBufferErrorEgressCumulativeEvents_Type=Counter32
_BrcdNPBufferErrorEgressCumulativeEvents_Object=MibTableColumn
brcdNPBufferErrorEgressCumulativeEvents=_BrcdNPBufferErrorEgressCumulativeEvents_Object((1,3,6,1,4,1,1991,1,14,2,1,1,3,1,7),_BrcdNPBufferErrorEgressCumulativeEvents_Type())
brcdNPBufferErrorEgressCumulativeEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPBufferErrorEgressCumulativeEvents.setStatus(_A)
_BrcdNPCSRAMErrorTable_Object=MibTable
brcdNPCSRAMErrorTable=_BrcdNPCSRAMErrorTable_Object((1,3,6,1,4,1,1991,1,14,2,1,1,4))
if mibBuilder.loadTexts:brcdNPCSRAMErrorTable.setStatus(_A)
_BrcdNPCSRAMErrorEntry_Object=MibTableRow
brcdNPCSRAMErrorEntry=_BrcdNPCSRAMErrorEntry_Object((1,3,6,1,4,1,1991,1,14,2,1,1,4,1))
brcdNPCSRAMErrorEntry.setIndexNames((0,_C,_U),(0,_C,_V))
if mibBuilder.loadTexts:brcdNPCSRAMErrorEntry.setStatus(_A)
_BrcdNPCSRAMErrorSlotId_Type=Unsigned32
_BrcdNPCSRAMErrorSlotId_Object=MibTableColumn
brcdNPCSRAMErrorSlotId=_BrcdNPCSRAMErrorSlotId_Object((1,3,6,1,4,1,1991,1,14,2,1,1,4,1,1),_BrcdNPCSRAMErrorSlotId_Type())
brcdNPCSRAMErrorSlotId.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdNPCSRAMErrorSlotId.setStatus(_A)
_BrcdNPCSRAMErrorDeviceId_Type=Unsigned32
_BrcdNPCSRAMErrorDeviceId_Object=MibTableColumn
brcdNPCSRAMErrorDeviceId=_BrcdNPCSRAMErrorDeviceId_Object((1,3,6,1,4,1,1991,1,14,2,1,1,4,1,2),_BrcdNPCSRAMErrorDeviceId_Type())
brcdNPCSRAMErrorDeviceId.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdNPCSRAMErrorDeviceId.setStatus(_A)
_BrcdNPCSRAMErrorDescription_Type=DisplayString
_BrcdNPCSRAMErrorDescription_Object=MibTableColumn
brcdNPCSRAMErrorDescription=_BrcdNPCSRAMErrorDescription_Object((1,3,6,1,4,1,1991,1,14,2,1,1,4,1,3),_BrcdNPCSRAMErrorDescription_Type())
brcdNPCSRAMErrorDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPCSRAMErrorDescription.setStatus(_A)
_BrcdNPCSRAMErrorCurrentEvents_Type=Counter32
_BrcdNPCSRAMErrorCurrentEvents_Object=MibTableColumn
brcdNPCSRAMErrorCurrentEvents=_BrcdNPCSRAMErrorCurrentEvents_Object((1,3,6,1,4,1,1991,1,14,2,1,1,4,1,4),_BrcdNPCSRAMErrorCurrentEvents_Type())
brcdNPCSRAMErrorCurrentEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPCSRAMErrorCurrentEvents.setStatus(_A)
_BrcdNPCSRAMErrorCumulativeEvents_Type=Counter32
_BrcdNPCSRAMErrorCumulativeEvents_Object=MibTableColumn
brcdNPCSRAMErrorCumulativeEvents=_BrcdNPCSRAMErrorCumulativeEvents_Object((1,3,6,1,4,1,1991,1,14,2,1,1,4,1,5),_BrcdNPCSRAMErrorCumulativeEvents_Type())
brcdNPCSRAMErrorCumulativeEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPCSRAMErrorCumulativeEvents.setStatus(_A)
_BrcdNPLPMRAMErrorTable_Object=MibTable
brcdNPLPMRAMErrorTable=_BrcdNPLPMRAMErrorTable_Object((1,3,6,1,4,1,1991,1,14,2,1,1,5))
if mibBuilder.loadTexts:brcdNPLPMRAMErrorTable.setStatus(_A)
_BrcdNPLPMRAMErrorEntry_Object=MibTableRow
brcdNPLPMRAMErrorEntry=_BrcdNPLPMRAMErrorEntry_Object((1,3,6,1,4,1,1991,1,14,2,1,1,5,1))
brcdNPLPMRAMErrorEntry.setIndexNames((0,_C,_W),(0,_C,_X),(0,_C,_Y))
if mibBuilder.loadTexts:brcdNPLPMRAMErrorEntry.setStatus(_A)
class _BrcdNPLPMRAMErrorIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4))
_BrcdNPLPMRAMErrorIndex_Type.__name__=_M
_BrcdNPLPMRAMErrorIndex_Object=MibTableColumn
brcdNPLPMRAMErrorIndex=_BrcdNPLPMRAMErrorIndex_Object((1,3,6,1,4,1,1991,1,14,2,1,1,5,1,1),_BrcdNPLPMRAMErrorIndex_Type())
brcdNPLPMRAMErrorIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdNPLPMRAMErrorIndex.setStatus(_A)
_BrcdNPLPMRAMErrorSlotId_Type=Unsigned32
_BrcdNPLPMRAMErrorSlotId_Object=MibTableColumn
brcdNPLPMRAMErrorSlotId=_BrcdNPLPMRAMErrorSlotId_Object((1,3,6,1,4,1,1991,1,14,2,1,1,5,1,2),_BrcdNPLPMRAMErrorSlotId_Type())
brcdNPLPMRAMErrorSlotId.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdNPLPMRAMErrorSlotId.setStatus(_A)
_BrcdNPLPMRAMErrorDeviceId_Type=Unsigned32
_BrcdNPLPMRAMErrorDeviceId_Object=MibTableColumn
brcdNPLPMRAMErrorDeviceId=_BrcdNPLPMRAMErrorDeviceId_Object((1,3,6,1,4,1,1991,1,14,2,1,1,5,1,3),_BrcdNPLPMRAMErrorDeviceId_Type())
brcdNPLPMRAMErrorDeviceId.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdNPLPMRAMErrorDeviceId.setStatus(_A)
_BrcdNPLPMRAMErrorName_Type=DisplayString
_BrcdNPLPMRAMErrorName_Object=MibTableColumn
brcdNPLPMRAMErrorName=_BrcdNPLPMRAMErrorName_Object((1,3,6,1,4,1,1991,1,14,2,1,1,5,1,4),_BrcdNPLPMRAMErrorName_Type())
brcdNPLPMRAMErrorName.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPLPMRAMErrorName.setStatus(_A)
_BrcdNPLPMRAMErrorDescription_Type=DisplayString
_BrcdNPLPMRAMErrorDescription_Object=MibTableColumn
brcdNPLPMRAMErrorDescription=_BrcdNPLPMRAMErrorDescription_Object((1,3,6,1,4,1,1991,1,14,2,1,1,5,1,5),_BrcdNPLPMRAMErrorDescription_Type())
brcdNPLPMRAMErrorDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPLPMRAMErrorDescription.setStatus(_A)
_BrcdNPLPMRAMErrorCurrentEvents_Type=Counter32
_BrcdNPLPMRAMErrorCurrentEvents_Object=MibTableColumn
brcdNPLPMRAMErrorCurrentEvents=_BrcdNPLPMRAMErrorCurrentEvents_Object((1,3,6,1,4,1,1991,1,14,2,1,1,5,1,6),_BrcdNPLPMRAMErrorCurrentEvents_Type())
brcdNPLPMRAMErrorCurrentEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPLPMRAMErrorCurrentEvents.setStatus(_A)
_BrcdNPLPMRAMErrorCumulativeEvents_Type=Counter32
_BrcdNPLPMRAMErrorCumulativeEvents_Object=MibTableColumn
brcdNPLPMRAMErrorCumulativeEvents=_BrcdNPLPMRAMErrorCumulativeEvents_Object((1,3,6,1,4,1,1991,1,14,2,1,1,5,1,7),_BrcdNPLPMRAMErrorCumulativeEvents_Type())
brcdNPLPMRAMErrorCumulativeEvents.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPLPMRAMErrorCumulativeEvents.setStatus(_A)
_BrcdNPDebugStatTable_Object=MibTable
brcdNPDebugStatTable=_BrcdNPDebugStatTable_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6))
if mibBuilder.loadTexts:brcdNPDebugStatTable.setStatus(_A)
_BrcdNPDebugStatEntry_Object=MibTableRow
brcdNPDebugStatEntry=_BrcdNPDebugStatEntry_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1))
brcdNPDebugStatEntry.setIndexNames((0,_C,_Z),(0,_C,_a))
if mibBuilder.loadTexts:brcdNPDebugStatEntry.setStatus(_A)
_BrcdNPDebugStatSlotId_Type=Unsigned32
_BrcdNPDebugStatSlotId_Object=MibTableColumn
brcdNPDebugStatSlotId=_BrcdNPDebugStatSlotId_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,1),_BrcdNPDebugStatSlotId_Type())
brcdNPDebugStatSlotId.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdNPDebugStatSlotId.setStatus(_A)
_BrcdNPDebugStatNPDeviceId_Type=Unsigned32
_BrcdNPDebugStatNPDeviceId_Object=MibTableColumn
brcdNPDebugStatNPDeviceId=_BrcdNPDebugStatNPDeviceId_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,2),_BrcdNPDebugStatNPDeviceId_Type())
brcdNPDebugStatNPDeviceId.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdNPDebugStatNPDeviceId.setStatus(_A)
_BrcdNPDebugStatDescription_Type=DisplayString
_BrcdNPDebugStatDescription_Object=MibTableColumn
brcdNPDebugStatDescription=_BrcdNPDebugStatDescription_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,3),_BrcdNPDebugStatDescription_Type())
brcdNPDebugStatDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatDescription.setStatus(_A)
_BrcdNPDebugStatL2SourceAddrLearnDrop_Type=Counter64
_BrcdNPDebugStatL2SourceAddrLearnDrop_Object=MibTableColumn
brcdNPDebugStatL2SourceAddrLearnDrop=_BrcdNPDebugStatL2SourceAddrLearnDrop_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,4),_BrcdNPDebugStatL2SourceAddrLearnDrop_Type())
brcdNPDebugStatL2SourceAddrLearnDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatL2SourceAddrLearnDrop.setStatus(_A)
_BrcdNPDebugStatRateLimitVPLSLocalLearnDrop_Type=Counter64
_BrcdNPDebugStatRateLimitVPLSLocalLearnDrop_Object=MibTableColumn
brcdNPDebugStatRateLimitVPLSLocalLearnDrop=_BrcdNPDebugStatRateLimitVPLSLocalLearnDrop_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,5),_BrcdNPDebugStatRateLimitVPLSLocalLearnDrop_Type())
brcdNPDebugStatRateLimitVPLSLocalLearnDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatRateLimitVPLSLocalLearnDrop.setStatus(_A)
_BrcdNPDebugStatUnkownMPLSDrop_Type=Counter64
_BrcdNPDebugStatUnkownMPLSDrop_Object=MibTableColumn
brcdNPDebugStatUnkownMPLSDrop=_BrcdNPDebugStatUnkownMPLSDrop_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,6),_BrcdNPDebugStatUnkownMPLSDrop_Type())
brcdNPDebugStatUnkownMPLSDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatUnkownMPLSDrop.setStatus(_A)
_BrcdNPDebugStatDestAddrVCMiss_Type=Counter64
_BrcdNPDebugStatDestAddrVCMiss_Object=MibTableColumn
brcdNPDebugStatDestAddrVCMiss=_BrcdNPDebugStatDestAddrVCMiss_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,7),_BrcdNPDebugStatDestAddrVCMiss_Type())
brcdNPDebugStatDestAddrVCMiss.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatDestAddrVCMiss.setStatus(_A)
_BrcdNPDebugStatRateLimitVPLSRemoteLearnDrop_Type=Counter64
_BrcdNPDebugStatRateLimitVPLSRemoteLearnDrop_Object=MibTableColumn
brcdNPDebugStatRateLimitVPLSRemoteLearnDrop=_BrcdNPDebugStatRateLimitVPLSRemoteLearnDrop_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,8),_BrcdNPDebugStatRateLimitVPLSRemoteLearnDrop_Type())
brcdNPDebugStatRateLimitVPLSRemoteLearnDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatRateLimitVPLSRemoteLearnDrop.setStatus(_A)
_BrcdNPDebugStatIPv4DestAddrVCMiss_Type=Counter64
_BrcdNPDebugStatIPv4DestAddrVCMiss_Object=MibTableColumn
brcdNPDebugStatIPv4DestAddrVCMiss=_BrcdNPDebugStatIPv4DestAddrVCMiss_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,9),_BrcdNPDebugStatIPv4DestAddrVCMiss_Type())
brcdNPDebugStatIPv4DestAddrVCMiss.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatIPv4DestAddrVCMiss.setStatus(_A)
_BrcdNPDebugStatIPv6DestAddrVCMiss_Type=Counter64
_BrcdNPDebugStatIPv6DestAddrVCMiss_Object=MibTableColumn
brcdNPDebugStatIPv6DestAddrVCMiss=_BrcdNPDebugStatIPv6DestAddrVCMiss_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,10),_BrcdNPDebugStatIPv6DestAddrVCMiss_Type())
brcdNPDebugStatIPv6DestAddrVCMiss.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatIPv6DestAddrVCMiss.setStatus(_A)
_BrcdNPDebugStatVPLSTx_Type=Counter64
_BrcdNPDebugStatVPLSTx_Object=MibTableColumn
brcdNPDebugStatVPLSTx=_BrcdNPDebugStatVPLSTx_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,11),_BrcdNPDebugStatVPLSTx_Type())
brcdNPDebugStatVPLSTx.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatVPLSTx.setStatus(_A)
_BrcdNPDebugStatVLLTx_Type=Counter64
_BrcdNPDebugStatVLLTx_Object=MibTableColumn
brcdNPDebugStatVLLTx=_BrcdNPDebugStatVLLTx_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,12),_BrcdNPDebugStatVLLTx_Type())
brcdNPDebugStatVLLTx.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatVLLTx.setStatus(_A)
_BrcdNPDebugStatUnknowL3VPNIngressDrop_Type=Counter64
_BrcdNPDebugStatUnknowL3VPNIngressDrop_Object=MibTableColumn
brcdNPDebugStatUnknowL3VPNIngressDrop=_BrcdNPDebugStatUnknowL3VPNIngressDrop_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,13),_BrcdNPDebugStatUnknowL3VPNIngressDrop_Type())
brcdNPDebugStatUnknowL3VPNIngressDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatUnknowL3VPNIngressDrop.setStatus(_A)
_BrcdNPDebugStatIPv6VPNTx_Type=Counter64
_BrcdNPDebugStatIPv6VPNTx_Object=MibTableColumn
brcdNPDebugStatIPv6VPNTx=_BrcdNPDebugStatIPv6VPNTx_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,14),_BrcdNPDebugStatIPv6VPNTx_Type())
brcdNPDebugStatIPv6VPNTx.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatIPv6VPNTx.setStatus(_A)
_BrcdNPDebugStatIPv4VPNTx_Type=Counter64
_BrcdNPDebugStatIPv4VPNTx_Object=MibTableColumn
brcdNPDebugStatIPv4VPNTx=_BrcdNPDebugStatIPv4VPNTx_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,15),_BrcdNPDebugStatIPv4VPNTx_Type())
brcdNPDebugStatIPv4VPNTx.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatIPv4VPNTx.setStatus(_A)
_BrcdNPDebugStatGREIPv4RxCount_Type=Counter64
_BrcdNPDebugStatGREIPv4RxCount_Object=MibTableColumn
brcdNPDebugStatGREIPv4RxCount=_BrcdNPDebugStatGREIPv4RxCount_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,16),_BrcdNPDebugStatGREIPv4RxCount_Type())
brcdNPDebugStatGREIPv4RxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatGREIPv4RxCount.setStatus(_A)
_BrcdNPDebugStatGREInvalidDrop_Type=Counter64
_BrcdNPDebugStatGREInvalidDrop_Object=MibTableColumn
brcdNPDebugStatGREInvalidDrop=_BrcdNPDebugStatGREInvalidDrop_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,17),_BrcdNPDebugStatGREInvalidDrop_Type())
brcdNPDebugStatGREInvalidDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatGREInvalidDrop.setStatus(_A)
_BrcdNPDebugStat6to4RxCount_Type=Counter64
_BrcdNPDebugStat6to4RxCount_Object=MibTableColumn
brcdNPDebugStat6to4RxCount=_BrcdNPDebugStat6to4RxCount_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,18),_BrcdNPDebugStat6to4RxCount_Type())
brcdNPDebugStat6to4RxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStat6to4RxCount.setStatus(_A)
_BrcdNPDebugStatGREEnfSourceIngressChkMiss_Type=Counter64
_BrcdNPDebugStatGREEnfSourceIngressChkMiss_Object=MibTableColumn
brcdNPDebugStatGREEnfSourceIngressChkMiss=_BrcdNPDebugStatGREEnfSourceIngressChkMiss_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,19),_BrcdNPDebugStatGREEnfSourceIngressChkMiss_Type())
brcdNPDebugStatGREEnfSourceIngressChkMiss.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatGREEnfSourceIngressChkMiss.setStatus(_A)
_BrcdNPDebugStat6to4EnfSourceIngressChkMiss_Type=Counter64
_BrcdNPDebugStat6to4EnfSourceIngressChkMiss_Object=MibTableColumn
brcdNPDebugStat6to4EnfSourceIngressChkMiss=_BrcdNPDebugStat6to4EnfSourceIngressChkMiss_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,20),_BrcdNPDebugStat6to4EnfSourceIngressChkMiss_Type())
brcdNPDebugStat6to4EnfSourceIngressChkMiss.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStat6to4EnfSourceIngressChkMiss.setStatus(_A)
_BrcdNPDebugStatGREMPLSRxCount_Type=Counter64
_BrcdNPDebugStatGREMPLSRxCount_Object=MibTableColumn
brcdNPDebugStatGREMPLSRxCount=_BrcdNPDebugStatGREMPLSRxCount_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,21),_BrcdNPDebugStatGREMPLSRxCount_Type())
brcdNPDebugStatGREMPLSRxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatGREMPLSRxCount.setStatus(_A)
_BrcdNPDebugStatGREIPv6RxCount_Type=Counter64
_BrcdNPDebugStatGREIPv6RxCount_Object=MibTableColumn
brcdNPDebugStatGREIPv6RxCount=_BrcdNPDebugStatGREIPv6RxCount_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,22),_BrcdNPDebugStatGREIPv6RxCount_Type())
brcdNPDebugStatGREIPv6RxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatGREIPv6RxCount.setStatus(_A)
_BrcdNPDebugStatPBBRxDropCount_Type=Counter64
_BrcdNPDebugStatPBBRxDropCount_Object=MibTableColumn
brcdNPDebugStatPBBRxDropCount=_BrcdNPDebugStatPBBRxDropCount_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,23),_BrcdNPDebugStatPBBRxDropCount_Type())
brcdNPDebugStatPBBRxDropCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatPBBRxDropCount.setStatus(_A)
_BrcdNPDebugStatPBBTxCount_Type=Counter64
_BrcdNPDebugStatPBBTxCount_Object=MibTableColumn
brcdNPDebugStatPBBTxCount=_BrcdNPDebugStatPBBTxCount_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,24),_BrcdNPDebugStatPBBTxCount_Type())
brcdNPDebugStatPBBTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatPBBTxCount.setStatus(_A)
_BrcdNPDebugStatIPv4DestAddrVCDrop_Type=Counter64
_BrcdNPDebugStatIPv4DestAddrVCDrop_Object=MibTableColumn
brcdNPDebugStatIPv4DestAddrVCDrop=_BrcdNPDebugStatIPv4DestAddrVCDrop_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,25),_BrcdNPDebugStatIPv4DestAddrVCDrop_Type())
brcdNPDebugStatIPv4DestAddrVCDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatIPv4DestAddrVCDrop.setStatus(_A)
_BrcdNPDebugStatIPv6DestAddrVCDrop_Type=Counter64
_BrcdNPDebugStatIPv6DestAddrVCDrop_Object=MibTableColumn
brcdNPDebugStatIPv6DestAddrVCDrop=_BrcdNPDebugStatIPv6DestAddrVCDrop_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,26),_BrcdNPDebugStatIPv6DestAddrVCDrop_Type())
brcdNPDebugStatIPv6DestAddrVCDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatIPv6DestAddrVCDrop.setStatus(_A)
_BrcdNPDebugStatSourceAddrPortVLANMiss_Type=Counter64
_BrcdNPDebugStatSourceAddrPortVLANMiss_Object=MibTableColumn
brcdNPDebugStatSourceAddrPortVLANMiss=_BrcdNPDebugStatSourceAddrPortVLANMiss_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,27),_BrcdNPDebugStatSourceAddrPortVLANMiss_Type())
brcdNPDebugStatSourceAddrPortVLANMiss.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatSourceAddrPortVLANMiss.setStatus(_A)
_BrcdNPDebugStatVPLSSourceAddrPortVLANMiss_Type=Counter64
_BrcdNPDebugStatVPLSSourceAddrPortVLANMiss_Object=MibTableColumn
brcdNPDebugStatVPLSSourceAddrPortVLANMiss=_BrcdNPDebugStatVPLSSourceAddrPortVLANMiss_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,28),_BrcdNPDebugStatVPLSSourceAddrPortVLANMiss_Type())
brcdNPDebugStatVPLSSourceAddrPortVLANMiss.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatVPLSSourceAddrPortVLANMiss.setStatus(_A)
_BrcdNPDebugStatSourceAddrVCMiss_Type=Counter64
_BrcdNPDebugStatSourceAddrVCMiss_Object=MibTableColumn
brcdNPDebugStatSourceAddrVCMiss=_BrcdNPDebugStatSourceAddrVCMiss_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,29),_BrcdNPDebugStatSourceAddrVCMiss_Type())
brcdNPDebugStatSourceAddrVCMiss.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatSourceAddrVCMiss.setStatus(_A)
_BrcdNPDebugStatIPv4HWFwdCount_Type=Counter64
_BrcdNPDebugStatIPv4HWFwdCount_Object=MibTableColumn
brcdNPDebugStatIPv4HWFwdCount=_BrcdNPDebugStatIPv4HWFwdCount_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,30),_BrcdNPDebugStatIPv4HWFwdCount_Type())
brcdNPDebugStatIPv4HWFwdCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatIPv4HWFwdCount.setStatus(_A)
_BrcdNPDebugStatIPv6HWFwdCount_Type=Counter64
_BrcdNPDebugStatIPv6HWFwdCount_Object=MibTableColumn
brcdNPDebugStatIPv6HWFwdCount=_BrcdNPDebugStatIPv6HWFwdCount_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,31),_BrcdNPDebugStatIPv6HWFwdCount_Type())
brcdNPDebugStatIPv6HWFwdCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatIPv6HWFwdCount.setStatus(_A)
_BrcdNPDebugStatMulticastRPFDropCount_Type=Counter64
_BrcdNPDebugStatMulticastRPFDropCount_Object=MibTableColumn
brcdNPDebugStatMulticastRPFDropCount=_BrcdNPDebugStatMulticastRPFDropCount_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,32),_BrcdNPDebugStatMulticastRPFDropCount_Type())
brcdNPDebugStatMulticastRPFDropCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatMulticastRPFDropCount.setStatus(_A)
_BrcdNPDebugStatMPLSLsrTxCount_Type=Counter64
_BrcdNPDebugStatMPLSLsrTxCount_Object=MibTableColumn
brcdNPDebugStatMPLSLsrTxCount=_BrcdNPDebugStatMPLSLsrTxCount_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,33),_BrcdNPDebugStatMPLSLsrTxCount_Type())
brcdNPDebugStatMPLSLsrTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatMPLSLsrTxCount.setStatus(_A)
_BrcdNPDebugStatGREIPv4TxCount_Type=Counter64
_BrcdNPDebugStatGREIPv4TxCount_Object=MibTableColumn
brcdNPDebugStatGREIPv4TxCount=_BrcdNPDebugStatGREIPv4TxCount_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,34),_BrcdNPDebugStatGREIPv4TxCount_Type())
brcdNPDebugStatGREIPv4TxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatGREIPv4TxCount.setStatus(_A)
_BrcdNPDebugStat6to4TxCount_Type=Counter64
_BrcdNPDebugStat6to4TxCount_Object=MibTableColumn
brcdNPDebugStat6to4TxCount=_BrcdNPDebugStat6to4TxCount_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,35),_BrcdNPDebugStat6to4TxCount_Type())
brcdNPDebugStat6to4TxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStat6to4TxCount.setStatus(_A)
_BrcdNPDebugStatMPLSRSVPTxCount_Type=Counter64
_BrcdNPDebugStatMPLSRSVPTxCount_Object=MibTableColumn
brcdNPDebugStatMPLSRSVPTxCount=_BrcdNPDebugStatMPLSRSVPTxCount_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,36),_BrcdNPDebugStatMPLSRSVPTxCount_Type())
brcdNPDebugStatMPLSRSVPTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatMPLSRSVPTxCount.setStatus(_A)
_BrcdNPDebugStatGREMPLSTxCount_Type=Counter64
_BrcdNPDebugStatGREMPLSTxCount_Object=MibTableColumn
brcdNPDebugStatGREMPLSTxCount=_BrcdNPDebugStatGREMPLSTxCount_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,37),_BrcdNPDebugStatGREMPLSTxCount_Type())
brcdNPDebugStatGREMPLSTxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatGREMPLSTxCount.setStatus(_A)
_BrcdNPDebugStatGREIPv6TxCount_Type=Counter64
_BrcdNPDebugStatGREIPv6TxCount_Object=MibTableColumn
brcdNPDebugStatGREIPv6TxCount=_BrcdNPDebugStatGREIPv6TxCount_Object((1,3,6,1,4,1,1991,1,14,2,1,1,6,1,38),_BrcdNPDebugStatGREIPv6TxCount_Type())
brcdNPDebugStatGREIPv6TxCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdNPDebugStatGREIPv6TxCount.setStatus(_A)
_BrcdTMStatisticsInfo_ObjectIdentity=ObjectIdentity
brcdTMStatisticsInfo=_BrcdTMStatisticsInfo_ObjectIdentity((1,3,6,1,4,1,1991,1,14,2,1,2))
_BrcdTMStatisticsInfoGroup_ObjectIdentity=ObjectIdentity
brcdTMStatisticsInfoGroup=_BrcdTMStatisticsInfoGroup_ObjectIdentity((1,3,6,1,4,1,1991,1,14,2,1,2,1))
_BrcdTMPortMappingMaxPorts_Type=Unsigned32
_BrcdTMPortMappingMaxPorts_Object=MibScalar
brcdTMPortMappingMaxPorts=_BrcdTMPortMappingMaxPorts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,1,1),_BrcdTMPortMappingMaxPorts_Type())
brcdTMPortMappingMaxPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMPortMappingMaxPorts.setStatus(_A)
_BrcdTMPortMappingUsedPorts_Type=Unsigned32
_BrcdTMPortMappingUsedPorts_Object=MibScalar
brcdTMPortMappingUsedPorts=_BrcdTMPortMappingUsedPorts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,1,2),_BrcdTMPortMappingUsedPorts_Type())
brcdTMPortMappingUsedPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMPortMappingUsedPorts.setStatus(_A)
_BrcdTMPortMappingAvailablePorts_Type=Unsigned32
_BrcdTMPortMappingAvailablePorts_Object=MibScalar
brcdTMPortMappingAvailablePorts=_BrcdTMPortMappingAvailablePorts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,1,3),_BrcdTMPortMappingAvailablePorts_Type())
brcdTMPortMappingAvailablePorts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMPortMappingAvailablePorts.setStatus(_A)
_BrcdTMStatsTable_Object=MibTable
brcdTMStatsTable=_BrcdTMStatsTable_Object((1,3,6,1,4,1,1991,1,14,2,1,2,2))
if mibBuilder.loadTexts:brcdTMStatsTable.setStatus(_A)
_BrcdTMStatsEntry_Object=MibTableRow
brcdTMStatsEntry=_BrcdTMStatsEntry_Object((1,3,6,1,4,1,1991,1,14,2,1,2,2,1))
brcdTMStatsEntry.setIndexNames((0,_C,_b),(0,_C,_c))
if mibBuilder.loadTexts:brcdTMStatsEntry.setStatus(_A)
_BrcdTMStatsSlotId_Type=Unsigned32
_BrcdTMStatsSlotId_Object=MibTableColumn
brcdTMStatsSlotId=_BrcdTMStatsSlotId_Object((1,3,6,1,4,1,1991,1,14,2,1,2,2,1,1),_BrcdTMStatsSlotId_Type())
brcdTMStatsSlotId.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdTMStatsSlotId.setStatus(_A)
_BrcdTMStatsTMDeviceId_Type=Unsigned32
_BrcdTMStatsTMDeviceId_Object=MibTableColumn
brcdTMStatsTMDeviceId=_BrcdTMStatsTMDeviceId_Object((1,3,6,1,4,1,1991,1,14,2,1,2,2,1,2),_BrcdTMStatsTMDeviceId_Type())
brcdTMStatsTMDeviceId.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdTMStatsTMDeviceId.setStatus(_A)
_BrcdTMStatsDescription_Type=DisplayString
_BrcdTMStatsDescription_Object=MibTableColumn
brcdTMStatsDescription=_BrcdTMStatsDescription_Object((1,3,6,1,4,1,1991,1,14,2,1,2,2,1,3),_BrcdTMStatsDescription_Type())
brcdTMStatsDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMStatsDescription.setStatus(_A)
_BrcdTMStatsTotalIngressPktsCnt_Type=Counter64
_BrcdTMStatsTotalIngressPktsCnt_Object=MibTableColumn
brcdTMStatsTotalIngressPktsCnt=_BrcdTMStatsTotalIngressPktsCnt_Object((1,3,6,1,4,1,1991,1,14,2,1,2,2,1,4),_BrcdTMStatsTotalIngressPktsCnt_Type())
brcdTMStatsTotalIngressPktsCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMStatsTotalIngressPktsCnt.setStatus(_A)
_BrcdTMStatsIngressEnqueuePkts_Type=Counter64
_BrcdTMStatsIngressEnqueuePkts_Object=MibTableColumn
brcdTMStatsIngressEnqueuePkts=_BrcdTMStatsIngressEnqueuePkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,2,1,5),_BrcdTMStatsIngressEnqueuePkts_Type())
brcdTMStatsIngressEnqueuePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMStatsIngressEnqueuePkts.setStatus(_A)
_BrcdTMStatsEgressEnqueuePkts_Type=Counter64
_BrcdTMStatsEgressEnqueuePkts_Object=MibTableColumn
brcdTMStatsEgressEnqueuePkts=_BrcdTMStatsEgressEnqueuePkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,2,1,6),_BrcdTMStatsEgressEnqueuePkts_Type())
brcdTMStatsEgressEnqueuePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMStatsEgressEnqueuePkts.setStatus(_A)
_BrcdTMStatsIngressEnqueueBytes_Type=Counter64
_BrcdTMStatsIngressEnqueueBytes_Object=MibTableColumn
brcdTMStatsIngressEnqueueBytes=_BrcdTMStatsIngressEnqueueBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,2,1,7),_BrcdTMStatsIngressEnqueueBytes_Type())
brcdTMStatsIngressEnqueueBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMStatsIngressEnqueueBytes.setStatus(_A)
_BrcdTMStatsEgressEnqueueBytes_Type=Counter64
_BrcdTMStatsEgressEnqueueBytes_Object=MibTableColumn
brcdTMStatsEgressEnqueueBytes=_BrcdTMStatsEgressEnqueueBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,2,1,8),_BrcdTMStatsEgressEnqueueBytes_Type())
brcdTMStatsEgressEnqueueBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMStatsEgressEnqueueBytes.setStatus(_A)
_BrcdTMStatsIngressDequeuePkts_Type=Counter64
_BrcdTMStatsIngressDequeuePkts_Object=MibTableColumn
brcdTMStatsIngressDequeuePkts=_BrcdTMStatsIngressDequeuePkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,2,1,9),_BrcdTMStatsIngressDequeuePkts_Type())
brcdTMStatsIngressDequeuePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMStatsIngressDequeuePkts.setStatus(_A)
_BrcdTMStatsIngressDequeueBytes_Type=Counter64
_BrcdTMStatsIngressDequeueBytes_Object=MibTableColumn
brcdTMStatsIngressDequeueBytes=_BrcdTMStatsIngressDequeueBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,2,1,10),_BrcdTMStatsIngressDequeueBytes_Type())
brcdTMStatsIngressDequeueBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMStatsIngressDequeueBytes.setStatus(_A)
_BrcdTMStatsIngressTotalQDiscardPkts_Type=Counter64
_BrcdTMStatsIngressTotalQDiscardPkts_Object=MibTableColumn
brcdTMStatsIngressTotalQDiscardPkts=_BrcdTMStatsIngressTotalQDiscardPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,2,1,11),_BrcdTMStatsIngressTotalQDiscardPkts_Type())
brcdTMStatsIngressTotalQDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMStatsIngressTotalQDiscardPkts.setStatus(_A)
_BrcdTMStatsIngressTotalQDiscardBytes_Type=Counter64
_BrcdTMStatsIngressTotalQDiscardBytes_Object=MibTableColumn
brcdTMStatsIngressTotalQDiscardBytes=_BrcdTMStatsIngressTotalQDiscardBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,2,1,12),_BrcdTMStatsIngressTotalQDiscardBytes_Type())
brcdTMStatsIngressTotalQDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMStatsIngressTotalQDiscardBytes.setStatus(_A)
_BrcdTMStatsIngressOldestDiscardPkts_Type=Counter64
_BrcdTMStatsIngressOldestDiscardPkts_Object=MibTableColumn
brcdTMStatsIngressOldestDiscardPkts=_BrcdTMStatsIngressOldestDiscardPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,2,1,13),_BrcdTMStatsIngressOldestDiscardPkts_Type())
brcdTMStatsIngressOldestDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMStatsIngressOldestDiscardPkts.setStatus(_A)
_BrcdTMStatsIngressOldestDiscardBytes_Type=Counter64
_BrcdTMStatsIngressOldestDiscardBytes_Object=MibTableColumn
brcdTMStatsIngressOldestDiscardBytes=_BrcdTMStatsIngressOldestDiscardBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,2,1,14),_BrcdTMStatsIngressOldestDiscardBytes_Type())
brcdTMStatsIngressOldestDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMStatsIngressOldestDiscardBytes.setStatus(_A)
_BrcdTMStatsEgressDiscardPkts_Type=Counter64
_BrcdTMStatsEgressDiscardPkts_Object=MibTableColumn
brcdTMStatsEgressDiscardPkts=_BrcdTMStatsEgressDiscardPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,2,1,15),_BrcdTMStatsEgressDiscardPkts_Type())
brcdTMStatsEgressDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMStatsEgressDiscardPkts.setStatus(_A)
_BrcdTMStatsEgressDiscardBytes_Type=Counter64
_BrcdTMStatsEgressDiscardBytes_Object=MibTableColumn
brcdTMStatsEgressDiscardBytes=_BrcdTMStatsEgressDiscardBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,2,1,16),_BrcdTMStatsEgressDiscardBytes_Type())
brcdTMStatsEgressDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMStatsEgressDiscardBytes.setStatus(_A)
_BrcdTMUcastQStatsTable_Object=MibTable
brcdTMUcastQStatsTable=_BrcdTMUcastQStatsTable_Object((1,3,6,1,4,1,1991,1,14,2,1,2,3))
if mibBuilder.loadTexts:brcdTMUcastQStatsTable.setStatus(_A)
_BrcdTMUcastQStatsEntry_Object=MibTableRow
brcdTMUcastQStatsEntry=_BrcdTMUcastQStatsEntry_Object((1,3,6,1,4,1,1991,1,14,2,1,2,3,1))
brcdTMUcastQStatsEntry.setIndexNames((0,_C,_d),(0,_C,_e),(0,_C,_f),(0,_C,_g))
if mibBuilder.loadTexts:brcdTMUcastQStatsEntry.setStatus(_A)
_BrcdTMUcastQStatsSlotId_Type=Unsigned32
_BrcdTMUcastQStatsSlotId_Object=MibTableColumn
brcdTMUcastQStatsSlotId=_BrcdTMUcastQStatsSlotId_Object((1,3,6,1,4,1,1991,1,14,2,1,2,3,1,1),_BrcdTMUcastQStatsSlotId_Type())
brcdTMUcastQStatsSlotId.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdTMUcastQStatsSlotId.setStatus(_A)
_BrcdTMUcastQStatsTMDeviceId_Type=Unsigned32
_BrcdTMUcastQStatsTMDeviceId_Object=MibTableColumn
brcdTMUcastQStatsTMDeviceId=_BrcdTMUcastQStatsTMDeviceId_Object((1,3,6,1,4,1,1991,1,14,2,1,2,3,1,2),_BrcdTMUcastQStatsTMDeviceId_Type())
brcdTMUcastQStatsTMDeviceId.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdTMUcastQStatsTMDeviceId.setStatus(_A)
_BrcdTMUcastQStatsDstIfIndex_Type=InterfaceIndex
_BrcdTMUcastQStatsDstIfIndex_Object=MibTableColumn
brcdTMUcastQStatsDstIfIndex=_BrcdTMUcastQStatsDstIfIndex_Object((1,3,6,1,4,1,1991,1,14,2,1,2,3,1,3),_BrcdTMUcastQStatsDstIfIndex_Type())
brcdTMUcastQStatsDstIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdTMUcastQStatsDstIfIndex.setStatus(_A)
_BrcdTMUcastQStatsPriority_Type=PortPriorityTC
_BrcdTMUcastQStatsPriority_Object=MibTableColumn
brcdTMUcastQStatsPriority=_BrcdTMUcastQStatsPriority_Object((1,3,6,1,4,1,1991,1,14,2,1,2,3,1,4),_BrcdTMUcastQStatsPriority_Type())
brcdTMUcastQStatsPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdTMUcastQStatsPriority.setStatus(_A)
_BrcdTMUcastQStatsDescription_Type=DisplayString
_BrcdTMUcastQStatsDescription_Object=MibTableColumn
brcdTMUcastQStatsDescription=_BrcdTMUcastQStatsDescription_Object((1,3,6,1,4,1,1991,1,14,2,1,2,3,1,5),_BrcdTMUcastQStatsDescription_Type())
brcdTMUcastQStatsDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMUcastQStatsDescription.setStatus(_A)
_BrcdTMUcastQStatsEnquePkts_Type=Counter64
_BrcdTMUcastQStatsEnquePkts_Object=MibTableColumn
brcdTMUcastQStatsEnquePkts=_BrcdTMUcastQStatsEnquePkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,3,1,6),_BrcdTMUcastQStatsEnquePkts_Type())
brcdTMUcastQStatsEnquePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMUcastQStatsEnquePkts.setStatus(_A)
_BrcdTMUcastQStatsEnqueBytes_Type=Counter64
_BrcdTMUcastQStatsEnqueBytes_Object=MibTableColumn
brcdTMUcastQStatsEnqueBytes=_BrcdTMUcastQStatsEnqueBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,3,1,7),_BrcdTMUcastQStatsEnqueBytes_Type())
brcdTMUcastQStatsEnqueBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMUcastQStatsEnqueBytes.setStatus(_A)
_BrcdTMUcastQStatsDequePkts_Type=Counter64
_BrcdTMUcastQStatsDequePkts_Object=MibTableColumn
brcdTMUcastQStatsDequePkts=_BrcdTMUcastQStatsDequePkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,3,1,8),_BrcdTMUcastQStatsDequePkts_Type())
brcdTMUcastQStatsDequePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMUcastQStatsDequePkts.setStatus(_A)
_BrcdTMUcastQStatsDequeBytes_Type=Counter64
_BrcdTMUcastQStatsDequeBytes_Object=MibTableColumn
brcdTMUcastQStatsDequeBytes=_BrcdTMUcastQStatsDequeBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,3,1,9),_BrcdTMUcastQStatsDequeBytes_Type())
brcdTMUcastQStatsDequeBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMUcastQStatsDequeBytes.setStatus(_A)
_BrcdTMUcastQStatsTotalQDiscardPkts_Type=Counter64
_BrcdTMUcastQStatsTotalQDiscardPkts_Object=MibTableColumn
brcdTMUcastQStatsTotalQDiscardPkts=_BrcdTMUcastQStatsTotalQDiscardPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,3,1,10),_BrcdTMUcastQStatsTotalQDiscardPkts_Type())
brcdTMUcastQStatsTotalQDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMUcastQStatsTotalQDiscardPkts.setStatus(_A)
_BrcdTMUcastQStatsTotalQDiscardBytes_Type=Counter64
_BrcdTMUcastQStatsTotalQDiscardBytes_Object=MibTableColumn
brcdTMUcastQStatsTotalQDiscardBytes=_BrcdTMUcastQStatsTotalQDiscardBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,3,1,11),_BrcdTMUcastQStatsTotalQDiscardBytes_Type())
brcdTMUcastQStatsTotalQDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMUcastQStatsTotalQDiscardBytes.setStatus(_A)
_BrcdTMUcastQStatsOldestDiscardPkts_Type=Counter64
_BrcdTMUcastQStatsOldestDiscardPkts_Object=MibTableColumn
brcdTMUcastQStatsOldestDiscardPkts=_BrcdTMUcastQStatsOldestDiscardPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,3,1,12),_BrcdTMUcastQStatsOldestDiscardPkts_Type())
brcdTMUcastQStatsOldestDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMUcastQStatsOldestDiscardPkts.setStatus(_A)
_BrcdTMUcastQStatsOldestDiscardBytes_Type=Counter64
_BrcdTMUcastQStatsOldestDiscardBytes_Object=MibTableColumn
brcdTMUcastQStatsOldestDiscardBytes=_BrcdTMUcastQStatsOldestDiscardBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,3,1,13),_BrcdTMUcastQStatsOldestDiscardBytes_Type())
brcdTMUcastQStatsOldestDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMUcastQStatsOldestDiscardBytes.setStatus(_A)
_BrcdTMUcastQStatsWREDDroppedPkts_Type=Counter64
_BrcdTMUcastQStatsWREDDroppedPkts_Object=MibTableColumn
brcdTMUcastQStatsWREDDroppedPkts=_BrcdTMUcastQStatsWREDDroppedPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,3,1,14),_BrcdTMUcastQStatsWREDDroppedPkts_Type())
brcdTMUcastQStatsWREDDroppedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMUcastQStatsWREDDroppedPkts.setStatus(_A)
_BrcdTMUcastQStatsWREDDroppedBytes_Type=Counter64
_BrcdTMUcastQStatsWREDDroppedBytes_Object=MibTableColumn
brcdTMUcastQStatsWREDDroppedBytes=_BrcdTMUcastQStatsWREDDroppedBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,3,1,15),_BrcdTMUcastQStatsWREDDroppedBytes_Type())
brcdTMUcastQStatsWREDDroppedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMUcastQStatsWREDDroppedBytes.setStatus(_A)
_BrcdTMUcastQStatsMaxQDepthSinceLastRead_Type=Counter64
_BrcdTMUcastQStatsMaxQDepthSinceLastRead_Object=MibTableColumn
brcdTMUcastQStatsMaxQDepthSinceLastRead=_BrcdTMUcastQStatsMaxQDepthSinceLastRead_Object((1,3,6,1,4,1,1991,1,14,2,1,2,3,1,16),_BrcdTMUcastQStatsMaxQDepthSinceLastRead_Type())
brcdTMUcastQStatsMaxQDepthSinceLastRead.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMUcastQStatsMaxQDepthSinceLastRead.setStatus(_A)
_BrcdTMUcastQStatsQSize_Type=Unsigned32
_BrcdTMUcastQStatsQSize_Object=MibTableColumn
brcdTMUcastQStatsQSize=_BrcdTMUcastQStatsQSize_Object((1,3,6,1,4,1,1991,1,14,2,1,2,3,1,17),_BrcdTMUcastQStatsQSize_Type())
brcdTMUcastQStatsQSize.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMUcastQStatsQSize.setStatus(_A)
_BrcdTMUcastQStatsCreditCount_Type=Unsigned32
_BrcdTMUcastQStatsCreditCount_Object=MibTableColumn
brcdTMUcastQStatsCreditCount=_BrcdTMUcastQStatsCreditCount_Object((1,3,6,1,4,1,1991,1,14,2,1,2,3,1,18),_BrcdTMUcastQStatsCreditCount_Type())
brcdTMUcastQStatsCreditCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMUcastQStatsCreditCount.setStatus(_A)
_BrcdTMMcastQStatsTable_Object=MibTable
brcdTMMcastQStatsTable=_BrcdTMMcastQStatsTable_Object((1,3,6,1,4,1,1991,1,14,2,1,2,4))
if mibBuilder.loadTexts:brcdTMMcastQStatsTable.setStatus(_A)
_BrcdTMMcastQStatsEntry_Object=MibTableRow
brcdTMMcastQStatsEntry=_BrcdTMMcastQStatsEntry_Object((1,3,6,1,4,1,1991,1,14,2,1,2,4,1))
brcdTMMcastQStatsEntry.setIndexNames((0,_C,_h),(0,_C,_i),(0,_C,_j))
if mibBuilder.loadTexts:brcdTMMcastQStatsEntry.setStatus(_A)
_BrcdTMMcastQStatsSlotId_Type=Unsigned32
_BrcdTMMcastQStatsSlotId_Object=MibTableColumn
brcdTMMcastQStatsSlotId=_BrcdTMMcastQStatsSlotId_Object((1,3,6,1,4,1,1991,1,14,2,1,2,4,1,1),_BrcdTMMcastQStatsSlotId_Type())
brcdTMMcastQStatsSlotId.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdTMMcastQStatsSlotId.setStatus(_A)
_BrcdTMMcastQStatsTMDeviceId_Type=Unsigned32
_BrcdTMMcastQStatsTMDeviceId_Object=MibTableColumn
brcdTMMcastQStatsTMDeviceId=_BrcdTMMcastQStatsTMDeviceId_Object((1,3,6,1,4,1,1991,1,14,2,1,2,4,1,2),_BrcdTMMcastQStatsTMDeviceId_Type())
brcdTMMcastQStatsTMDeviceId.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdTMMcastQStatsTMDeviceId.setStatus(_A)
class _BrcdTMMcastQStatsPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,5,7)));namedValues=NamedValues(*((_k,1),(_l,3),(_m,5),(_n,7)))
_BrcdTMMcastQStatsPriority_Type.__name__=_G
_BrcdTMMcastQStatsPriority_Object=MibTableColumn
brcdTMMcastQStatsPriority=_BrcdTMMcastQStatsPriority_Object((1,3,6,1,4,1,1991,1,14,2,1,2,4,1,3),_BrcdTMMcastQStatsPriority_Type())
brcdTMMcastQStatsPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdTMMcastQStatsPriority.setStatus(_A)
_BrcdTMMcastQStatsDescription_Type=DisplayString
_BrcdTMMcastQStatsDescription_Object=MibTableColumn
brcdTMMcastQStatsDescription=_BrcdTMMcastQStatsDescription_Object((1,3,6,1,4,1,1991,1,14,2,1,2,4,1,4),_BrcdTMMcastQStatsDescription_Type())
brcdTMMcastQStatsDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastQStatsDescription.setStatus(_A)
_BrcdTMMcastQStatsEnquePkts_Type=Counter64
_BrcdTMMcastQStatsEnquePkts_Object=MibTableColumn
brcdTMMcastQStatsEnquePkts=_BrcdTMMcastQStatsEnquePkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,4,1,5),_BrcdTMMcastQStatsEnquePkts_Type())
brcdTMMcastQStatsEnquePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastQStatsEnquePkts.setStatus(_A)
_BrcdTMMcastQStatsEnqueBytes_Type=Counter64
_BrcdTMMcastQStatsEnqueBytes_Object=MibTableColumn
brcdTMMcastQStatsEnqueBytes=_BrcdTMMcastQStatsEnqueBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,4,1,6),_BrcdTMMcastQStatsEnqueBytes_Type())
brcdTMMcastQStatsEnqueBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastQStatsEnqueBytes.setStatus(_A)
_BrcdTMMcastQStatsDequePkts_Type=Counter64
_BrcdTMMcastQStatsDequePkts_Object=MibTableColumn
brcdTMMcastQStatsDequePkts=_BrcdTMMcastQStatsDequePkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,4,1,7),_BrcdTMMcastQStatsDequePkts_Type())
brcdTMMcastQStatsDequePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastQStatsDequePkts.setStatus(_A)
_BrcdTMMcastQStatsDequeBytes_Type=Counter64
_BrcdTMMcastQStatsDequeBytes_Object=MibTableColumn
brcdTMMcastQStatsDequeBytes=_BrcdTMMcastQStatsDequeBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,4,1,8),_BrcdTMMcastQStatsDequeBytes_Type())
brcdTMMcastQStatsDequeBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastQStatsDequeBytes.setStatus(_A)
_BrcdTMMcastQStatsTotalQDiscardPkts_Type=Counter64
_BrcdTMMcastQStatsTotalQDiscardPkts_Object=MibTableColumn
brcdTMMcastQStatsTotalQDiscardPkts=_BrcdTMMcastQStatsTotalQDiscardPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,4,1,9),_BrcdTMMcastQStatsTotalQDiscardPkts_Type())
brcdTMMcastQStatsTotalQDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastQStatsTotalQDiscardPkts.setStatus(_A)
_BrcdTMMcastQStatsTotalQDiscardBytes_Type=Counter64
_BrcdTMMcastQStatsTotalQDiscardBytes_Object=MibTableColumn
brcdTMMcastQStatsTotalQDiscardBytes=_BrcdTMMcastQStatsTotalQDiscardBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,4,1,10),_BrcdTMMcastQStatsTotalQDiscardBytes_Type())
brcdTMMcastQStatsTotalQDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastQStatsTotalQDiscardBytes.setStatus(_A)
_BrcdTMMcastQStatsOldestDiscardPkts_Type=Counter64
_BrcdTMMcastQStatsOldestDiscardPkts_Object=MibTableColumn
brcdTMMcastQStatsOldestDiscardPkts=_BrcdTMMcastQStatsOldestDiscardPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,4,1,11),_BrcdTMMcastQStatsOldestDiscardPkts_Type())
brcdTMMcastQStatsOldestDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastQStatsOldestDiscardPkts.setStatus(_A)
_BrcdTMMcastQStatsOldestDiscardBytes_Type=Counter64
_BrcdTMMcastQStatsOldestDiscardBytes_Object=MibTableColumn
brcdTMMcastQStatsOldestDiscardBytes=_BrcdTMMcastQStatsOldestDiscardBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,4,1,12),_BrcdTMMcastQStatsOldestDiscardBytes_Type())
brcdTMMcastQStatsOldestDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastQStatsOldestDiscardBytes.setStatus(_A)
_BrcdTMMcastQStatsWREDDroppedPkts_Type=Counter64
_BrcdTMMcastQStatsWREDDroppedPkts_Object=MibTableColumn
brcdTMMcastQStatsWREDDroppedPkts=_BrcdTMMcastQStatsWREDDroppedPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,4,1,13),_BrcdTMMcastQStatsWREDDroppedPkts_Type())
brcdTMMcastQStatsWREDDroppedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastQStatsWREDDroppedPkts.setStatus(_A)
_BrcdTMMcastQStatsWREDDroppedBytes_Type=Counter64
_BrcdTMMcastQStatsWREDDroppedBytes_Object=MibTableColumn
brcdTMMcastQStatsWREDDroppedBytes=_BrcdTMMcastQStatsWREDDroppedBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,4,1,14),_BrcdTMMcastQStatsWREDDroppedBytes_Type())
brcdTMMcastQStatsWREDDroppedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastQStatsWREDDroppedBytes.setStatus(_A)
_BrcdTMMcastQStatsMaxQDepthSinceLastRead_Type=Counter64
_BrcdTMMcastQStatsMaxQDepthSinceLastRead_Object=MibTableColumn
brcdTMMcastQStatsMaxQDepthSinceLastRead=_BrcdTMMcastQStatsMaxQDepthSinceLastRead_Object((1,3,6,1,4,1,1991,1,14,2,1,2,4,1,15),_BrcdTMMcastQStatsMaxQDepthSinceLastRead_Type())
brcdTMMcastQStatsMaxQDepthSinceLastRead.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastQStatsMaxQDepthSinceLastRead.setStatus(_A)
_BrcdTMMcastQStatsQSize_Type=Unsigned32
_BrcdTMMcastQStatsQSize_Object=MibTableColumn
brcdTMMcastQStatsQSize=_BrcdTMMcastQStatsQSize_Object((1,3,6,1,4,1,1991,1,14,2,1,2,4,1,16),_BrcdTMMcastQStatsQSize_Type())
brcdTMMcastQStatsQSize.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastQStatsQSize.setStatus(_A)
_BrcdTMMcastQStatsCreditCount_Type=Unsigned32
_BrcdTMMcastQStatsCreditCount_Object=MibTableColumn
brcdTMMcastQStatsCreditCount=_BrcdTMMcastQStatsCreditCount_Object((1,3,6,1,4,1,1991,1,14,2,1,2,4,1,17),_BrcdTMMcastQStatsCreditCount_Type())
brcdTMMcastQStatsCreditCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastQStatsCreditCount.setStatus(_A)
_BrcdTMCpuQStatsTable_Object=MibTable
brcdTMCpuQStatsTable=_BrcdTMCpuQStatsTable_Object((1,3,6,1,4,1,1991,1,14,2,1,2,5))
if mibBuilder.loadTexts:brcdTMCpuQStatsTable.setStatus(_A)
_BrcdTMCpuQStatsEntry_Object=MibTableRow
brcdTMCpuQStatsEntry=_BrcdTMCpuQStatsEntry_Object((1,3,6,1,4,1,1991,1,14,2,1,2,5,1))
brcdTMCpuQStatsEntry.setIndexNames((0,_C,_I),(0,_C,_J),(0,_C,_o),(0,_C,_K))
if mibBuilder.loadTexts:brcdTMCpuQStatsEntry.setStatus(_A)
_BrcdTMCpuQStatsSlotId_Type=Unsigned32
_BrcdTMCpuQStatsSlotId_Object=MibTableColumn
brcdTMCpuQStatsSlotId=_BrcdTMCpuQStatsSlotId_Object((1,3,6,1,4,1,1991,1,14,2,1,2,5,1,1),_BrcdTMCpuQStatsSlotId_Type())
brcdTMCpuQStatsSlotId.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdTMCpuQStatsSlotId.setStatus(_A)
_BrcdTMCpuQStatsTMDeviceId_Type=Unsigned32
_BrcdTMCpuQStatsTMDeviceId_Object=MibTableColumn
brcdTMCpuQStatsTMDeviceId=_BrcdTMCpuQStatsTMDeviceId_Object((1,3,6,1,4,1,1991,1,14,2,1,2,5,1,2),_BrcdTMCpuQStatsTMDeviceId_Type())
brcdTMCpuQStatsTMDeviceId.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdTMCpuQStatsTMDeviceId.setStatus(_A)
class _BrcdTMCpuQStatsType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('cpuQ',1),('cpuCopyQ',2),('cpuManagementQ',3),('cpuProtocolQ',4)))
_BrcdTMCpuQStatsType_Type.__name__=_G
_BrcdTMCpuQStatsType_Object=MibTableColumn
brcdTMCpuQStatsType=_BrcdTMCpuQStatsType_Object((1,3,6,1,4,1,1991,1,14,2,1,2,5,1,3),_BrcdTMCpuQStatsType_Type())
brcdTMCpuQStatsType.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdTMCpuQStatsType.setStatus(_A)
_BrcdTMCpuQStatsPriority_Type=PortPriorityTC
_BrcdTMCpuQStatsPriority_Object=MibTableColumn
brcdTMCpuQStatsPriority=_BrcdTMCpuQStatsPriority_Object((1,3,6,1,4,1,1991,1,14,2,1,2,5,1,4),_BrcdTMCpuQStatsPriority_Type())
brcdTMCpuQStatsPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdTMCpuQStatsPriority.setStatus(_A)
_BrcdTMCpuQStatsDescription_Type=DisplayString
_BrcdTMCpuQStatsDescription_Object=MibTableColumn
brcdTMCpuQStatsDescription=_BrcdTMCpuQStatsDescription_Object((1,3,6,1,4,1,1991,1,14,2,1,2,5,1,5),_BrcdTMCpuQStatsDescription_Type())
brcdTMCpuQStatsDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQStatsDescription.setStatus(_A)
_BrcdTMCpuQStatsEnquePkts_Type=Counter64
_BrcdTMCpuQStatsEnquePkts_Object=MibTableColumn
brcdTMCpuQStatsEnquePkts=_BrcdTMCpuQStatsEnquePkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,5,1,6),_BrcdTMCpuQStatsEnquePkts_Type())
brcdTMCpuQStatsEnquePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQStatsEnquePkts.setStatus(_A)
_BrcdTMCpuQStatsEnqueBytes_Type=Counter64
_BrcdTMCpuQStatsEnqueBytes_Object=MibTableColumn
brcdTMCpuQStatsEnqueBytes=_BrcdTMCpuQStatsEnqueBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,5,1,7),_BrcdTMCpuQStatsEnqueBytes_Type())
brcdTMCpuQStatsEnqueBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQStatsEnqueBytes.setStatus(_A)
_BrcdTMCpuQStatsDequePkts_Type=Counter64
_BrcdTMCpuQStatsDequePkts_Object=MibTableColumn
brcdTMCpuQStatsDequePkts=_BrcdTMCpuQStatsDequePkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,5,1,8),_BrcdTMCpuQStatsDequePkts_Type())
brcdTMCpuQStatsDequePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQStatsDequePkts.setStatus(_A)
_BrcdTMCpuQStatsDequeBytes_Type=Counter64
_BrcdTMCpuQStatsDequeBytes_Object=MibTableColumn
brcdTMCpuQStatsDequeBytes=_BrcdTMCpuQStatsDequeBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,5,1,9),_BrcdTMCpuQStatsDequeBytes_Type())
brcdTMCpuQStatsDequeBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQStatsDequeBytes.setStatus(_A)
_BrcdTMCpuQStatsTotalQDiscardPkts_Type=Counter64
_BrcdTMCpuQStatsTotalQDiscardPkts_Object=MibTableColumn
brcdTMCpuQStatsTotalQDiscardPkts=_BrcdTMCpuQStatsTotalQDiscardPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,5,1,10),_BrcdTMCpuQStatsTotalQDiscardPkts_Type())
brcdTMCpuQStatsTotalQDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQStatsTotalQDiscardPkts.setStatus(_A)
_BrcdTMCpuQStatsTotalQDiscardBytes_Type=Counter64
_BrcdTMCpuQStatsTotalQDiscardBytes_Object=MibTableColumn
brcdTMCpuQStatsTotalQDiscardBytes=_BrcdTMCpuQStatsTotalQDiscardBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,5,1,11),_BrcdTMCpuQStatsTotalQDiscardBytes_Type())
brcdTMCpuQStatsTotalQDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQStatsTotalQDiscardBytes.setStatus(_A)
_BrcdTMCpuQStatsOldestDiscardPkts_Type=Counter64
_BrcdTMCpuQStatsOldestDiscardPkts_Object=MibTableColumn
brcdTMCpuQStatsOldestDiscardPkts=_BrcdTMCpuQStatsOldestDiscardPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,5,1,12),_BrcdTMCpuQStatsOldestDiscardPkts_Type())
brcdTMCpuQStatsOldestDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQStatsOldestDiscardPkts.setStatus(_A)
_BrcdTMCpuQStatsOldestDiscardBytes_Type=Counter64
_BrcdTMCpuQStatsOldestDiscardBytes_Object=MibTableColumn
brcdTMCpuQStatsOldestDiscardBytes=_BrcdTMCpuQStatsOldestDiscardBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,5,1,13),_BrcdTMCpuQStatsOldestDiscardBytes_Type())
brcdTMCpuQStatsOldestDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQStatsOldestDiscardBytes.setStatus(_A)
_BrcdTMCpuQStatsWREDDroppedPkts_Type=Counter64
_BrcdTMCpuQStatsWREDDroppedPkts_Object=MibTableColumn
brcdTMCpuQStatsWREDDroppedPkts=_BrcdTMCpuQStatsWREDDroppedPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,5,1,14),_BrcdTMCpuQStatsWREDDroppedPkts_Type())
brcdTMCpuQStatsWREDDroppedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQStatsWREDDroppedPkts.setStatus(_A)
_BrcdTMCpuQStatsWREDDroppedBytes_Type=Counter64
_BrcdTMCpuQStatsWREDDroppedBytes_Object=MibTableColumn
brcdTMCpuQStatsWREDDroppedBytes=_BrcdTMCpuQStatsWREDDroppedBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,5,1,15),_BrcdTMCpuQStatsWREDDroppedBytes_Type())
brcdTMCpuQStatsWREDDroppedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQStatsWREDDroppedBytes.setStatus(_A)
_BrcdTMCpuQStatsMaxQDepthSinceLastRead_Type=Counter64
_BrcdTMCpuQStatsMaxQDepthSinceLastRead_Object=MibTableColumn
brcdTMCpuQStatsMaxQDepthSinceLastRead=_BrcdTMCpuQStatsMaxQDepthSinceLastRead_Object((1,3,6,1,4,1,1991,1,14,2,1,2,5,1,16),_BrcdTMCpuQStatsMaxQDepthSinceLastRead_Type())
brcdTMCpuQStatsMaxQDepthSinceLastRead.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQStatsMaxQDepthSinceLastRead.setStatus(_A)
_BrcdTMCpuQStatsQSize_Type=Unsigned32
_BrcdTMCpuQStatsQSize_Object=MibTableColumn
brcdTMCpuQStatsQSize=_BrcdTMCpuQStatsQSize_Object((1,3,6,1,4,1,1991,1,14,2,1,2,5,1,17),_BrcdTMCpuQStatsQSize_Type())
brcdTMCpuQStatsQSize.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQStatsQSize.setStatus(_A)
_BrcdTMCpuQStatsCreditCount_Type=Unsigned32
_BrcdTMCpuQStatsCreditCount_Object=MibTableColumn
brcdTMCpuQStatsCreditCount=_BrcdTMCpuQStatsCreditCount_Object((1,3,6,1,4,1,1991,1,14,2,1,2,5,1,18),_BrcdTMCpuQStatsCreditCount_Type())
brcdTMCpuQStatsCreditCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQStatsCreditCount.setStatus(_A)
_BrcdTMMcastStreamQStatsTable_Object=MibTable
brcdTMMcastStreamQStatsTable=_BrcdTMMcastStreamQStatsTable_Object((1,3,6,1,4,1,1991,1,14,2,1,2,6))
if mibBuilder.loadTexts:brcdTMMcastStreamQStatsTable.setStatus(_A)
_BrcdTMMcastStreamQStatsEntry_Object=MibTableRow
brcdTMMcastStreamQStatsEntry=_BrcdTMMcastStreamQStatsEntry_Object((1,3,6,1,4,1,1991,1,14,2,1,2,6,1))
brcdTMMcastStreamQStatsEntry.setIndexNames((0,_C,_p),(0,_C,_q),(0,_C,_r),(0,_C,_s))
if mibBuilder.loadTexts:brcdTMMcastStreamQStatsEntry.setStatus(_A)
_BrcdTMMcastStreamQStatsAddressType_Type=InetAddressType
_BrcdTMMcastStreamQStatsAddressType_Object=MibTableColumn
brcdTMMcastStreamQStatsAddressType=_BrcdTMMcastStreamQStatsAddressType_Object((1,3,6,1,4,1,1991,1,14,2,1,2,6,1,1),_BrcdTMMcastStreamQStatsAddressType_Type())
brcdTMMcastStreamQStatsAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdTMMcastStreamQStatsAddressType.setStatus(_A)
_BrcdTMMcastStreamQStatsSource_Type=InetAddress
_BrcdTMMcastStreamQStatsSource_Object=MibTableColumn
brcdTMMcastStreamQStatsSource=_BrcdTMMcastStreamQStatsSource_Object((1,3,6,1,4,1,1991,1,14,2,1,2,6,1,2),_BrcdTMMcastStreamQStatsSource_Type())
brcdTMMcastStreamQStatsSource.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdTMMcastStreamQStatsSource.setStatus(_A)
_BrcdTMMcastStreamQStatsGroup_Type=InetAddress
_BrcdTMMcastStreamQStatsGroup_Object=MibTableColumn
brcdTMMcastStreamQStatsGroup=_BrcdTMMcastStreamQStatsGroup_Object((1,3,6,1,4,1,1991,1,14,2,1,2,6,1,3),_BrcdTMMcastStreamQStatsGroup_Type())
brcdTMMcastStreamQStatsGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdTMMcastStreamQStatsGroup.setStatus(_A)
_BrcdTMMcastStreamQStatsGroupPrefixLength_Type=InetAddressPrefixLength
_BrcdTMMcastStreamQStatsGroupPrefixLength_Object=MibTableColumn
brcdTMMcastStreamQStatsGroupPrefixLength=_BrcdTMMcastStreamQStatsGroupPrefixLength_Object((1,3,6,1,4,1,1991,1,14,2,1,2,6,1,4),_BrcdTMMcastStreamQStatsGroupPrefixLength_Type())
brcdTMMcastStreamQStatsGroupPrefixLength.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdTMMcastStreamQStatsGroupPrefixLength.setStatus(_A)
class _BrcdTMMcastStreamQStatsPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,3,5,7)));namedValues=NamedValues(*((_k,1),(_l,3),(_m,5),(_n,7)))
_BrcdTMMcastStreamQStatsPriority_Type.__name__=_G
_BrcdTMMcastStreamQStatsPriority_Object=MibTableColumn
brcdTMMcastStreamQStatsPriority=_BrcdTMMcastStreamQStatsPriority_Object((1,3,6,1,4,1,1991,1,14,2,1,2,6,1,5),_BrcdTMMcastStreamQStatsPriority_Type())
brcdTMMcastStreamQStatsPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastStreamQStatsPriority.setStatus(_A)
_BrcdTMMcastStreamQStatsEnquePkts_Type=Counter64
_BrcdTMMcastStreamQStatsEnquePkts_Object=MibTableColumn
brcdTMMcastStreamQStatsEnquePkts=_BrcdTMMcastStreamQStatsEnquePkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,6,1,6),_BrcdTMMcastStreamQStatsEnquePkts_Type())
brcdTMMcastStreamQStatsEnquePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastStreamQStatsEnquePkts.setStatus(_A)
_BrcdTMMcastStreamQStatsEnqueBytes_Type=Counter64
_BrcdTMMcastStreamQStatsEnqueBytes_Object=MibTableColumn
brcdTMMcastStreamQStatsEnqueBytes=_BrcdTMMcastStreamQStatsEnqueBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,6,1,7),_BrcdTMMcastStreamQStatsEnqueBytes_Type())
brcdTMMcastStreamQStatsEnqueBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastStreamQStatsEnqueBytes.setStatus(_A)
_BrcdTMMcastStreamQStatsDequePkts_Type=Counter64
_BrcdTMMcastStreamQStatsDequePkts_Object=MibTableColumn
brcdTMMcastStreamQStatsDequePkts=_BrcdTMMcastStreamQStatsDequePkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,6,1,8),_BrcdTMMcastStreamQStatsDequePkts_Type())
brcdTMMcastStreamQStatsDequePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastStreamQStatsDequePkts.setStatus(_A)
_BrcdTMMcastStreamQStatsDequeBytes_Type=Counter64
_BrcdTMMcastStreamQStatsDequeBytes_Object=MibTableColumn
brcdTMMcastStreamQStatsDequeBytes=_BrcdTMMcastStreamQStatsDequeBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,6,1,9),_BrcdTMMcastStreamQStatsDequeBytes_Type())
brcdTMMcastStreamQStatsDequeBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastStreamQStatsDequeBytes.setStatus(_A)
_BrcdTMMcastStreamQStatsTotalQDiscardPkts_Type=Counter64
_BrcdTMMcastStreamQStatsTotalQDiscardPkts_Object=MibTableColumn
brcdTMMcastStreamQStatsTotalQDiscardPkts=_BrcdTMMcastStreamQStatsTotalQDiscardPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,6,1,10),_BrcdTMMcastStreamQStatsTotalQDiscardPkts_Type())
brcdTMMcastStreamQStatsTotalQDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastStreamQStatsTotalQDiscardPkts.setStatus(_A)
_BrcdTMMcastStreamQStatsTotalQDiscardBytes_Type=Counter64
_BrcdTMMcastStreamQStatsTotalQDiscardBytes_Object=MibTableColumn
brcdTMMcastStreamQStatsTotalQDiscardBytes=_BrcdTMMcastStreamQStatsTotalQDiscardBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,6,1,11),_BrcdTMMcastStreamQStatsTotalQDiscardBytes_Type())
brcdTMMcastStreamQStatsTotalQDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastStreamQStatsTotalQDiscardBytes.setStatus(_A)
_BrcdTMMcastStreamQStatsOldestDiscardPkts_Type=Counter64
_BrcdTMMcastStreamQStatsOldestDiscardPkts_Object=MibTableColumn
brcdTMMcastStreamQStatsOldestDiscardPkts=_BrcdTMMcastStreamQStatsOldestDiscardPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,6,1,12),_BrcdTMMcastStreamQStatsOldestDiscardPkts_Type())
brcdTMMcastStreamQStatsOldestDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastStreamQStatsOldestDiscardPkts.setStatus(_A)
_BrcdTMMcastStreamQStatsOldestDiscardBytes_Type=Counter64
_BrcdTMMcastStreamQStatsOldestDiscardBytes_Object=MibTableColumn
brcdTMMcastStreamQStatsOldestDiscardBytes=_BrcdTMMcastStreamQStatsOldestDiscardBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,6,1,13),_BrcdTMMcastStreamQStatsOldestDiscardBytes_Type())
brcdTMMcastStreamQStatsOldestDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastStreamQStatsOldestDiscardBytes.setStatus(_A)
_BrcdTMMcastStreamQStatsWREDDroppedPkts_Type=Counter64
_BrcdTMMcastStreamQStatsWREDDroppedPkts_Object=MibTableColumn
brcdTMMcastStreamQStatsWREDDroppedPkts=_BrcdTMMcastStreamQStatsWREDDroppedPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,6,1,14),_BrcdTMMcastStreamQStatsWREDDroppedPkts_Type())
brcdTMMcastStreamQStatsWREDDroppedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastStreamQStatsWREDDroppedPkts.setStatus(_A)
_BrcdTMMcastStreamQStatsWREDDroppedBytes_Type=Counter64
_BrcdTMMcastStreamQStatsWREDDroppedBytes_Object=MibTableColumn
brcdTMMcastStreamQStatsWREDDroppedBytes=_BrcdTMMcastStreamQStatsWREDDroppedBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,6,1,15),_BrcdTMMcastStreamQStatsWREDDroppedBytes_Type())
brcdTMMcastStreamQStatsWREDDroppedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastStreamQStatsWREDDroppedBytes.setStatus(_A)
_BrcdTMMcastStreamQStatsMaxQDepthSinceLastRead_Type=Counter64
_BrcdTMMcastStreamQStatsMaxQDepthSinceLastRead_Object=MibTableColumn
brcdTMMcastStreamQStatsMaxQDepthSinceLastRead=_BrcdTMMcastStreamQStatsMaxQDepthSinceLastRead_Object((1,3,6,1,4,1,1991,1,14,2,1,2,6,1,16),_BrcdTMMcastStreamQStatsMaxQDepthSinceLastRead_Type())
brcdTMMcastStreamQStatsMaxQDepthSinceLastRead.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastStreamQStatsMaxQDepthSinceLastRead.setStatus(_A)
_BrcdTMMcastStreamQStatsQSize_Type=Unsigned32
_BrcdTMMcastStreamQStatsQSize_Object=MibTableColumn
brcdTMMcastStreamQStatsQSize=_BrcdTMMcastStreamQStatsQSize_Object((1,3,6,1,4,1,1991,1,14,2,1,2,6,1,17),_BrcdTMMcastStreamQStatsQSize_Type())
brcdTMMcastStreamQStatsQSize.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastStreamQStatsQSize.setStatus(_A)
_BrcdTMMcastStreamQStatsCreditCount_Type=Unsigned32
_BrcdTMMcastStreamQStatsCreditCount_Object=MibTableColumn
brcdTMMcastStreamQStatsCreditCount=_BrcdTMMcastStreamQStatsCreditCount_Object((1,3,6,1,4,1,1991,1,14,2,1,2,6,1,18),_BrcdTMMcastStreamQStatsCreditCount_Type())
brcdTMMcastStreamQStatsCreditCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMMcastStreamQStatsCreditCount.setStatus(_A)
_BrcdTMCpuQInfoTable_Object=MibTable
brcdTMCpuQInfoTable=_BrcdTMCpuQInfoTable_Object((1,3,6,1,4,1,1991,1,14,2,1,2,7))
if mibBuilder.loadTexts:brcdTMCpuQInfoTable.setStatus(_A)
_BrcdTMCpuQInfoEntry_Object=MibTableRow
brcdTMCpuQInfoEntry=_BrcdTMCpuQInfoEntry_Object((1,3,6,1,4,1,1991,1,14,2,1,2,7,1))
brcdTMCpuQInfoEntry.setIndexNames((0,_C,_t),(0,_C,_u))
if mibBuilder.loadTexts:brcdTMCpuQInfoEntry.setStatus(_A)
_BrcdTMCpuQInfoSlotId_Type=Unsigned32
_BrcdTMCpuQInfoSlotId_Object=MibTableColumn
brcdTMCpuQInfoSlotId=_BrcdTMCpuQInfoSlotId_Object((1,3,6,1,4,1,1991,1,14,2,1,2,7,1,1),_BrcdTMCpuQInfoSlotId_Type())
brcdTMCpuQInfoSlotId.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdTMCpuQInfoSlotId.setStatus(_A)
_BrcdTMCpuQInfoTMDeviceId_Type=Unsigned32
_BrcdTMCpuQInfoTMDeviceId_Object=MibTableColumn
brcdTMCpuQInfoTMDeviceId=_BrcdTMCpuQInfoTMDeviceId_Object((1,3,6,1,4,1,1991,1,14,2,1,2,7,1,2),_BrcdTMCpuQInfoTMDeviceId_Type())
brcdTMCpuQInfoTMDeviceId.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdTMCpuQInfoTMDeviceId.setStatus(_A)
_BrcdTMCpuQInfoPriority0QSize_Type=Unsigned32
_BrcdTMCpuQInfoPriority0QSize_Object=MibTableColumn
brcdTMCpuQInfoPriority0QSize=_BrcdTMCpuQInfoPriority0QSize_Object((1,3,6,1,4,1,1991,1,14,2,1,2,7,1,3),_BrcdTMCpuQInfoPriority0QSize_Type())
brcdTMCpuQInfoPriority0QSize.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQInfoPriority0QSize.setStatus(_A)
_BrcdTMCpuQInfoPriority0CreditCount_Type=Unsigned32
_BrcdTMCpuQInfoPriority0CreditCount_Object=MibTableColumn
brcdTMCpuQInfoPriority0CreditCount=_BrcdTMCpuQInfoPriority0CreditCount_Object((1,3,6,1,4,1,1991,1,14,2,1,2,7,1,4),_BrcdTMCpuQInfoPriority0CreditCount_Type())
brcdTMCpuQInfoPriority0CreditCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQInfoPriority0CreditCount.setStatus(_A)
_BrcdTMCpuQInfoPriority1QSize_Type=Unsigned32
_BrcdTMCpuQInfoPriority1QSize_Object=MibTableColumn
brcdTMCpuQInfoPriority1QSize=_BrcdTMCpuQInfoPriority1QSize_Object((1,3,6,1,4,1,1991,1,14,2,1,2,7,1,5),_BrcdTMCpuQInfoPriority1QSize_Type())
brcdTMCpuQInfoPriority1QSize.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQInfoPriority1QSize.setStatus(_A)
_BrcdTMCpuQInfoPriority1CreditCount_Type=Unsigned32
_BrcdTMCpuQInfoPriority1CreditCount_Object=MibTableColumn
brcdTMCpuQInfoPriority1CreditCount=_BrcdTMCpuQInfoPriority1CreditCount_Object((1,3,6,1,4,1,1991,1,14,2,1,2,7,1,6),_BrcdTMCpuQInfoPriority1CreditCount_Type())
brcdTMCpuQInfoPriority1CreditCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQInfoPriority1CreditCount.setStatus(_A)
_BrcdTMCpuQInfoPriority2QSize_Type=Unsigned32
_BrcdTMCpuQInfoPriority2QSize_Object=MibTableColumn
brcdTMCpuQInfoPriority2QSize=_BrcdTMCpuQInfoPriority2QSize_Object((1,3,6,1,4,1,1991,1,14,2,1,2,7,1,7),_BrcdTMCpuQInfoPriority2QSize_Type())
brcdTMCpuQInfoPriority2QSize.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQInfoPriority2QSize.setStatus(_A)
_BrcdTMCpuQInfoPriority2CreditCount_Type=Unsigned32
_BrcdTMCpuQInfoPriority2CreditCount_Object=MibTableColumn
brcdTMCpuQInfoPriority2CreditCount=_BrcdTMCpuQInfoPriority2CreditCount_Object((1,3,6,1,4,1,1991,1,14,2,1,2,7,1,8),_BrcdTMCpuQInfoPriority2CreditCount_Type())
brcdTMCpuQInfoPriority2CreditCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQInfoPriority2CreditCount.setStatus(_A)
_BrcdTMCpuQInfoPriority3QSize_Type=Unsigned32
_BrcdTMCpuQInfoPriority3QSize_Object=MibTableColumn
brcdTMCpuQInfoPriority3QSize=_BrcdTMCpuQInfoPriority3QSize_Object((1,3,6,1,4,1,1991,1,14,2,1,2,7,1,9),_BrcdTMCpuQInfoPriority3QSize_Type())
brcdTMCpuQInfoPriority3QSize.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQInfoPriority3QSize.setStatus(_A)
_BrcdTMCpuQInfoPriority3CreditCount_Type=Unsigned32
_BrcdTMCpuQInfoPriority3CreditCount_Object=MibTableColumn
brcdTMCpuQInfoPriority3CreditCount=_BrcdTMCpuQInfoPriority3CreditCount_Object((1,3,6,1,4,1,1991,1,14,2,1,2,7,1,10),_BrcdTMCpuQInfoPriority3CreditCount_Type())
brcdTMCpuQInfoPriority3CreditCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQInfoPriority3CreditCount.setStatus(_A)
_BrcdTMCpuQInfoPriority4QSize_Type=Unsigned32
_BrcdTMCpuQInfoPriority4QSize_Object=MibTableColumn
brcdTMCpuQInfoPriority4QSize=_BrcdTMCpuQInfoPriority4QSize_Object((1,3,6,1,4,1,1991,1,14,2,1,2,7,1,11),_BrcdTMCpuQInfoPriority4QSize_Type())
brcdTMCpuQInfoPriority4QSize.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQInfoPriority4QSize.setStatus(_A)
_BrcdTMCpuQInfoPriority4CreditCount_Type=Unsigned32
_BrcdTMCpuQInfoPriority4CreditCount_Object=MibTableColumn
brcdTMCpuQInfoPriority4CreditCount=_BrcdTMCpuQInfoPriority4CreditCount_Object((1,3,6,1,4,1,1991,1,14,2,1,2,7,1,12),_BrcdTMCpuQInfoPriority4CreditCount_Type())
brcdTMCpuQInfoPriority4CreditCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQInfoPriority4CreditCount.setStatus(_A)
_BrcdTMCpuQInfoPriority5QSize_Type=Unsigned32
_BrcdTMCpuQInfoPriority5QSize_Object=MibTableColumn
brcdTMCpuQInfoPriority5QSize=_BrcdTMCpuQInfoPriority5QSize_Object((1,3,6,1,4,1,1991,1,14,2,1,2,7,1,13),_BrcdTMCpuQInfoPriority5QSize_Type())
brcdTMCpuQInfoPriority5QSize.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQInfoPriority5QSize.setStatus(_A)
_BrcdTMCpuQInfoPriority5CreditCount_Type=Unsigned32
_BrcdTMCpuQInfoPriority5CreditCount_Object=MibTableColumn
brcdTMCpuQInfoPriority5CreditCount=_BrcdTMCpuQInfoPriority5CreditCount_Object((1,3,6,1,4,1,1991,1,14,2,1,2,7,1,14),_BrcdTMCpuQInfoPriority5CreditCount_Type())
brcdTMCpuQInfoPriority5CreditCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQInfoPriority5CreditCount.setStatus(_A)
_BrcdTMCpuQInfoPriority6QSize_Type=Unsigned32
_BrcdTMCpuQInfoPriority6QSize_Object=MibTableColumn
brcdTMCpuQInfoPriority6QSize=_BrcdTMCpuQInfoPriority6QSize_Object((1,3,6,1,4,1,1991,1,14,2,1,2,7,1,15),_BrcdTMCpuQInfoPriority6QSize_Type())
brcdTMCpuQInfoPriority6QSize.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQInfoPriority6QSize.setStatus(_A)
_BrcdTMCpuQInfoPriority6CreditCount_Type=Unsigned32
_BrcdTMCpuQInfoPriority6CreditCount_Object=MibTableColumn
brcdTMCpuQInfoPriority6CreditCount=_BrcdTMCpuQInfoPriority6CreditCount_Object((1,3,6,1,4,1,1991,1,14,2,1,2,7,1,16),_BrcdTMCpuQInfoPriority6CreditCount_Type())
brcdTMCpuQInfoPriority6CreditCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQInfoPriority6CreditCount.setStatus(_A)
_BrcdTMCpuQInfoPriority7QSize_Type=Unsigned32
_BrcdTMCpuQInfoPriority7QSize_Object=MibTableColumn
brcdTMCpuQInfoPriority7QSize=_BrcdTMCpuQInfoPriority7QSize_Object((1,3,6,1,4,1,1991,1,14,2,1,2,7,1,17),_BrcdTMCpuQInfoPriority7QSize_Type())
brcdTMCpuQInfoPriority7QSize.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQInfoPriority7QSize.setStatus(_A)
_BrcdTMCpuQInfoPriority7CreditCount_Type=Unsigned32
_BrcdTMCpuQInfoPriority7CreditCount_Object=MibTableColumn
brcdTMCpuQInfoPriority7CreditCount=_BrcdTMCpuQInfoPriority7CreditCount_Object((1,3,6,1,4,1,1991,1,14,2,1,2,7,1,18),_BrcdTMCpuQInfoPriority7CreditCount_Type())
brcdTMCpuQInfoPriority7CreditCount.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuQInfoPriority7CreditCount.setStatus(_A)
_BrcdTMDestUcastQStatTable_Object=MibTable
brcdTMDestUcastQStatTable=_BrcdTMDestUcastQStatTable_Object((1,3,6,1,4,1,1991,1,14,2,1,2,8))
if mibBuilder.loadTexts:brcdTMDestUcastQStatTable.setStatus(_A)
_BrcdTMDestUcastQStatEntry_Object=MibTableRow
brcdTMDestUcastQStatEntry=_BrcdTMDestUcastQStatEntry_Object((1,3,6,1,4,1,1991,1,14,2,1,2,8,1))
brcdTMDestUcastQStatEntry.setIndexNames((0,_C,_v),(0,_C,_w))
if mibBuilder.loadTexts:brcdTMDestUcastQStatEntry.setStatus(_A)
_BrcdTMDestUcastQStatDestIfIndex_Type=InterfaceIndex
_BrcdTMDestUcastQStatDestIfIndex_Object=MibTableColumn
brcdTMDestUcastQStatDestIfIndex=_BrcdTMDestUcastQStatDestIfIndex_Object((1,3,6,1,4,1,1991,1,14,2,1,2,8,1,1),_BrcdTMDestUcastQStatDestIfIndex_Type())
brcdTMDestUcastQStatDestIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdTMDestUcastQStatDestIfIndex.setStatus(_A)
_BrcdTMDestUcastQStatPriority_Type=PortPriorityTC
_BrcdTMDestUcastQStatPriority_Object=MibTableColumn
brcdTMDestUcastQStatPriority=_BrcdTMDestUcastQStatPriority_Object((1,3,6,1,4,1,1991,1,14,2,1,2,8,1,2),_BrcdTMDestUcastQStatPriority_Type())
brcdTMDestUcastQStatPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:brcdTMDestUcastQStatPriority.setStatus(_A)
_BrcdTMDestUcastQStatEnquePkts_Type=Counter64
_BrcdTMDestUcastQStatEnquePkts_Object=MibTableColumn
brcdTMDestUcastQStatEnquePkts=_BrcdTMDestUcastQStatEnquePkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,8,1,3),_BrcdTMDestUcastQStatEnquePkts_Type())
brcdTMDestUcastQStatEnquePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMDestUcastQStatEnquePkts.setStatus(_A)
_BrcdTMDestUcastQStatEnqueBytes_Type=Counter64
_BrcdTMDestUcastQStatEnqueBytes_Object=MibTableColumn
brcdTMDestUcastQStatEnqueBytes=_BrcdTMDestUcastQStatEnqueBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,8,1,4),_BrcdTMDestUcastQStatEnqueBytes_Type())
brcdTMDestUcastQStatEnqueBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMDestUcastQStatEnqueBytes.setStatus(_A)
_BrcdTMDestUcastQStatDequePkts_Type=Counter64
_BrcdTMDestUcastQStatDequePkts_Object=MibTableColumn
brcdTMDestUcastQStatDequePkts=_BrcdTMDestUcastQStatDequePkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,8,1,5),_BrcdTMDestUcastQStatDequePkts_Type())
brcdTMDestUcastQStatDequePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMDestUcastQStatDequePkts.setStatus(_A)
_BrcdTMDestUcastQStatDequeBytes_Type=Counter64
_BrcdTMDestUcastQStatDequeBytes_Object=MibTableColumn
brcdTMDestUcastQStatDequeBytes=_BrcdTMDestUcastQStatDequeBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,8,1,6),_BrcdTMDestUcastQStatDequeBytes_Type())
brcdTMDestUcastQStatDequeBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMDestUcastQStatDequeBytes.setStatus(_A)
_BrcdTMDestUcastQStatTotalQDiscardPkts_Type=Counter64
_BrcdTMDestUcastQStatTotalQDiscardPkts_Object=MibTableColumn
brcdTMDestUcastQStatTotalQDiscardPkts=_BrcdTMDestUcastQStatTotalQDiscardPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,8,1,7),_BrcdTMDestUcastQStatTotalQDiscardPkts_Type())
brcdTMDestUcastQStatTotalQDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMDestUcastQStatTotalQDiscardPkts.setStatus(_A)
_BrcdTMDestUcastQStatTotalQDiscardBytes_Type=Counter64
_BrcdTMDestUcastQStatTotalQDiscardBytes_Object=MibTableColumn
brcdTMDestUcastQStatTotalQDiscardBytes=_BrcdTMDestUcastQStatTotalQDiscardBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,8,1,8),_BrcdTMDestUcastQStatTotalQDiscardBytes_Type())
brcdTMDestUcastQStatTotalQDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMDestUcastQStatTotalQDiscardBytes.setStatus(_A)
_BrcdTMCpuAggrQStatsTable_Object=MibTable
brcdTMCpuAggrQStatsTable=_BrcdTMCpuAggrQStatsTable_Object((1,3,6,1,4,1,1991,1,14,2,1,2,9))
if mibBuilder.loadTexts:brcdTMCpuAggrQStatsTable.setStatus(_A)
_BrcdTMCpuAggrQStatsEntry_Object=MibTableRow
brcdTMCpuAggrQStatsEntry=_BrcdTMCpuAggrQStatsEntry_Object((1,3,6,1,4,1,1991,1,14,2,1,2,9,1))
brcdTMCpuAggrQStatsEntry.setIndexNames((0,_C,_I),(0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:brcdTMCpuAggrQStatsEntry.setStatus(_A)
_BrcdTMCpuAggrQStatsDescription_Type=DisplayString
_BrcdTMCpuAggrQStatsDescription_Object=MibTableColumn
brcdTMCpuAggrQStatsDescription=_BrcdTMCpuAggrQStatsDescription_Object((1,3,6,1,4,1,1991,1,14,2,1,2,9,1,1),_BrcdTMCpuAggrQStatsDescription_Type())
brcdTMCpuAggrQStatsDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuAggrQStatsDescription.setStatus(_A)
_BrcdTMCpuAggrQStatsEnquePkts_Type=Counter64
_BrcdTMCpuAggrQStatsEnquePkts_Object=MibTableColumn
brcdTMCpuAggrQStatsEnquePkts=_BrcdTMCpuAggrQStatsEnquePkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,9,1,2),_BrcdTMCpuAggrQStatsEnquePkts_Type())
brcdTMCpuAggrQStatsEnquePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuAggrQStatsEnquePkts.setStatus(_A)
_BrcdTMCpuAggrQStatsEnqueBytes_Type=Counter64
_BrcdTMCpuAggrQStatsEnqueBytes_Object=MibTableColumn
brcdTMCpuAggrQStatsEnqueBytes=_BrcdTMCpuAggrQStatsEnqueBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,9,1,3),_BrcdTMCpuAggrQStatsEnqueBytes_Type())
brcdTMCpuAggrQStatsEnqueBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuAggrQStatsEnqueBytes.setStatus(_A)
_BrcdTMCpuAggrQStatsDequePkts_Type=Counter64
_BrcdTMCpuAggrQStatsDequePkts_Object=MibTableColumn
brcdTMCpuAggrQStatsDequePkts=_BrcdTMCpuAggrQStatsDequePkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,9,1,4),_BrcdTMCpuAggrQStatsDequePkts_Type())
brcdTMCpuAggrQStatsDequePkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuAggrQStatsDequePkts.setStatus(_A)
_BrcdTMCpuAggrQStatsDequeBytes_Type=Counter64
_BrcdTMCpuAggrQStatsDequeBytes_Object=MibTableColumn
brcdTMCpuAggrQStatsDequeBytes=_BrcdTMCpuAggrQStatsDequeBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,9,1,5),_BrcdTMCpuAggrQStatsDequeBytes_Type())
brcdTMCpuAggrQStatsDequeBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuAggrQStatsDequeBytes.setStatus(_A)
_BrcdTMCpuAggrQStatsTotalQDiscardPkts_Type=Counter64
_BrcdTMCpuAggrQStatsTotalQDiscardPkts_Object=MibTableColumn
brcdTMCpuAggrQStatsTotalQDiscardPkts=_BrcdTMCpuAggrQStatsTotalQDiscardPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,9,1,6),_BrcdTMCpuAggrQStatsTotalQDiscardPkts_Type())
brcdTMCpuAggrQStatsTotalQDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuAggrQStatsTotalQDiscardPkts.setStatus(_A)
_BrcdTMCpuAggrQStatsTotalQDiscardBytes_Type=Counter64
_BrcdTMCpuAggrQStatsTotalQDiscardBytes_Object=MibTableColumn
brcdTMCpuAggrQStatsTotalQDiscardBytes=_BrcdTMCpuAggrQStatsTotalQDiscardBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,9,1,7),_BrcdTMCpuAggrQStatsTotalQDiscardBytes_Type())
brcdTMCpuAggrQStatsTotalQDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuAggrQStatsTotalQDiscardBytes.setStatus(_A)
_BrcdTMCpuAggrQStatsOldestDiscardPkts_Type=Counter64
_BrcdTMCpuAggrQStatsOldestDiscardPkts_Object=MibTableColumn
brcdTMCpuAggrQStatsOldestDiscardPkts=_BrcdTMCpuAggrQStatsOldestDiscardPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,9,1,8),_BrcdTMCpuAggrQStatsOldestDiscardPkts_Type())
brcdTMCpuAggrQStatsOldestDiscardPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuAggrQStatsOldestDiscardPkts.setStatus(_A)
_BrcdTMCpuAggrQStatsOldestDiscardBytes_Type=Counter64
_BrcdTMCpuAggrQStatsOldestDiscardBytes_Object=MibTableColumn
brcdTMCpuAggrQStatsOldestDiscardBytes=_BrcdTMCpuAggrQStatsOldestDiscardBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,9,1,9),_BrcdTMCpuAggrQStatsOldestDiscardBytes_Type())
brcdTMCpuAggrQStatsOldestDiscardBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuAggrQStatsOldestDiscardBytes.setStatus(_A)
_BrcdTMCpuAggrQStatsWREDDroppedPkts_Type=Counter64
_BrcdTMCpuAggrQStatsWREDDroppedPkts_Object=MibTableColumn
brcdTMCpuAggrQStatsWREDDroppedPkts=_BrcdTMCpuAggrQStatsWREDDroppedPkts_Object((1,3,6,1,4,1,1991,1,14,2,1,2,9,1,10),_BrcdTMCpuAggrQStatsWREDDroppedPkts_Type())
brcdTMCpuAggrQStatsWREDDroppedPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuAggrQStatsWREDDroppedPkts.setStatus(_A)
_BrcdTMCpuAggrQStatsWREDDroppedBytes_Type=Counter64
_BrcdTMCpuAggrQStatsWREDDroppedBytes_Object=MibTableColumn
brcdTMCpuAggrQStatsWREDDroppedBytes=_BrcdTMCpuAggrQStatsWREDDroppedBytes_Object((1,3,6,1,4,1,1991,1,14,2,1,2,9,1,11),_BrcdTMCpuAggrQStatsWREDDroppedBytes_Type())
brcdTMCpuAggrQStatsWREDDroppedBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdTMCpuAggrQStatsWREDDroppedBytes.setStatus(_A)
_BrcdNPGlobal_ObjectIdentity=ObjectIdentity
brcdNPGlobal=_BrcdNPGlobal_ObjectIdentity((1,3,6,1,4,1,1991,1,14,2,1,3))
_BrcdNPIndex_Type=Unsigned32
_BrcdNPIndex_Object=MibScalar
brcdNPIndex=_BrcdNPIndex_Object((1,3,6,1,4,1,1991,1,14,2,1,3,1),_BrcdNPIndex_Type())
brcdNPIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:brcdNPIndex.setStatus(_A)
_BrcdNPLockupRecoveryCount_Type=Unsigned32
_BrcdNPLockupRecoveryCount_Object=MibScalar
brcdNPLockupRecoveryCount=_BrcdNPLockupRecoveryCount_Object((1,3,6,1,4,1,1991,1,14,2,1,3,2),_BrcdNPLockupRecoveryCount_Type())
brcdNPLockupRecoveryCount.setMaxAccess(_H)
if mibBuilder.loadTexts:brcdNPLockupRecoveryCount.setStatus(_A)
brcdNPBufferErrorIngressThresholdExceeded=NotificationType((1,3,6,1,4,1,1991,1,14,2,0,1))
brcdNPBufferErrorIngressThresholdExceeded.setObjects(*((_C,_L),(_C,_x)))
if mibBuilder.loadTexts:brcdNPBufferErrorIngressThresholdExceeded.setStatus(_A)
brcdNPBufferErrorEgressThresholdExceeded=NotificationType((1,3,6,1,4,1,1991,1,14,2,0,2))
brcdNPBufferErrorEgressThresholdExceeded.setObjects(*((_C,_L),(_C,_y)))
if mibBuilder.loadTexts:brcdNPBufferErrorEgressThresholdExceeded.setStatus(_A)
brcdNPCSRAMErrorThresholdExceeded=NotificationType((1,3,6,1,4,1,1991,1,14,2,0,3))
brcdNPCSRAMErrorThresholdExceeded.setObjects(*((_C,_z),(_C,_A0)))
if mibBuilder.loadTexts:brcdNPCSRAMErrorThresholdExceeded.setStatus(_A)
brcdNPLPMRAMErrorThresholdExceeded=NotificationType((1,3,6,1,4,1,1991,1,14,2,0,4))
brcdNPLPMRAMErrorThresholdExceeded.setObjects(*((_C,_A1),(_C,_A2),(_C,_A3)))
if mibBuilder.loadTexts:brcdNPLPMRAMErrorThresholdExceeded.setStatus(_A)
brcdNPMemoryParityErrorTrap=NotificationType((1,3,6,1,4,1,1991,1,14,2,0,6))
brcdNPMemoryParityErrorTrap.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:brcdNPMemoryParityErrorTrap.setStatus(_A)
brcdNPMemoryMiscErrorTrap=NotificationType((1,3,6,1,4,1,1991,1,14,2,0,7))
brcdNPMemoryMiscErrorTrap.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:brcdNPMemoryMiscErrorTrap.setStatus(_A)
brcdNPBuffOverFlowErrorTrap=NotificationType((1,3,6,1,4,1,1991,1,14,2,0,8))
brcdNPBuffOverFlowErrorTrap.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:brcdNPBuffOverFlowErrorTrap.setStatus(_A)
brcdNPBuffUnderFlowErrorTrap=NotificationType((1,3,6,1,4,1,1991,1,14,2,0,9))
brcdNPBuffUnderFlowErrorTrap.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:brcdNPBuffUnderFlowErrorTrap.setStatus(_A)
brcdNPECCSingleErrorTrap=NotificationType((1,3,6,1,4,1,1991,1,14,2,0,10))
brcdNPECCSingleErrorTrap.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:brcdNPECCSingleErrorTrap.setStatus(_A)
brcdNPECCMultipleErrorTrap=NotificationType((1,3,6,1,4,1,1991,1,14,2,0,11))
brcdNPECCMultipleErrorTrap.setObjects(*((_C,_E),(_C,_F)))
if mibBuilder.loadTexts:brcdNPECCMultipleErrorTrap.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'brocadeNPTMStatsMIB':brocadeNPTMStatsMIB,'brcdNPTMMIBNotification':brcdNPTMMIBNotification,'brcdNPBufferErrorIngressThresholdExceeded':brcdNPBufferErrorIngressThresholdExceeded,'brcdNPBufferErrorEgressThresholdExceeded':brcdNPBufferErrorEgressThresholdExceeded,'brcdNPCSRAMErrorThresholdExceeded':brcdNPCSRAMErrorThresholdExceeded,'brcdNPLPMRAMErrorThresholdExceeded':brcdNPLPMRAMErrorThresholdExceeded,'brcdNPNotificationSupportTable':brcdNPNotificationSupportTable,'brcdNPNotificationSupportEntry':brcdNPNotificationSupportEntry,_N:brcdNPNotificationSupportSlotId,_O:brcdNPNotificationSupportDeviceId,_E:brcdNPNotificationSupportDescription,_F:brcdNPNotificationSupportErrorType,'brcdNPMemoryParityErrorTrap':brcdNPMemoryParityErrorTrap,'brcdNPMemoryMiscErrorTrap':brcdNPMemoryMiscErrorTrap,'brcdNPBuffOverFlowErrorTrap':brcdNPBuffOverFlowErrorTrap,'brcdNPBuffUnderFlowErrorTrap':brcdNPBuffUnderFlowErrorTrap,'brcdNPECCSingleErrorTrap':brcdNPECCSingleErrorTrap,'brcdNPECCMultipleErrorTrap':brcdNPECCMultipleErrorTrap,'brcdNPTMMIBObjects':brcdNPTMMIBObjects,'brcdNPStatisticsInfo':brcdNPStatisticsInfo,'brcdNPStatsTable':brcdNPStatsTable,'brcdNPStatsEntry':brcdNPStatsEntry,_P:brcdNPStatsIfIndex,'brcdNPStatsRxRawGoodPkts':brcdNPStatsRxRawGoodPkts,'brcdNPStatsRxForwardPkts':brcdNPStatsRxForwardPkts,'brcdNPStatsRxDiscardPkts':brcdNPStatsRxDiscardPkts,'brcdNPStatsRxMiscPkts':brcdNPStatsRxMiscPkts,'brcdNPStatsRxUnicastPkts':brcdNPStatsRxUnicastPkts,'brcdNPStatsRxBroadcastPkts':brcdNPStatsRxBroadcastPkts,'brcdNPStatsRxMulticastPkts':brcdNPStatsRxMulticastPkts,'brcdNPStatsRxSendToTMPkts':brcdNPStatsRxSendToTMPkts,'brcdNPStatsRxBadPkts':brcdNPStatsRxBadPkts,'brcdNPStatsRxLookupUnavailable':brcdNPStatsRxLookupUnavailable,'brcdNPStatsRxACLDrop':brcdNPStatsRxACLDrop,'brcdNPStatsRxPriority0And1Drop':brcdNPStatsRxPriority0And1Drop,'brcdNPStatsRxPriority2And3Drop':brcdNPStatsRxPriority2And3Drop,'brcdNPStatsRxPriority4And5Drop':brcdNPStatsRxPriority4And5Drop,'brcdNPStatsRxPriority6And7Drop':brcdNPStatsRxPriority6And7Drop,'brcdNPStatsRxSuppressRPFDrop':brcdNPStatsRxSuppressRPFDrop,'brcdNPStatsRxRPFDrop':brcdNPStatsRxRPFDrop,'brcdNPStatsRxIPv4Pkts':brcdNPStatsRxIPv4Pkts,'brcdNPStatsRxIPv6Pkts':brcdNPStatsRxIPv6Pkts,'brcdNPStatsRxRouteOnlyDrop':brcdNPStatsRxRouteOnlyDrop,'brcdNPStatsRxIPv6SuppressRPFDrop':brcdNPStatsRxIPv6SuppressRPFDrop,'brcdNPStatsRxIPv6RPFDropCount':brcdNPStatsRxIPv6RPFDropCount,'brcdNPStatsRxIPv4Bytes':brcdNPStatsRxIPv4Bytes,'brcdNPStatsRxIPv6Bytes':brcdNPStatsRxIPv6Bytes,'brcdNPStatsRxPOSCtrlProtocolPkts':brcdNPStatsRxPOSCtrlProtocolPkts,'brcdNPStatsRxPOSLinkDrop':brcdNPStatsRxPOSLinkDrop,'brcdNPStatsRxRoutedPktsDrop':brcdNPStatsRxRoutedPktsDrop,'brcdNPStatsTxSentToMACPkts':brcdNPStatsTxSentToMACPkts,'brcdNPStatsTxRawGoodPkts':brcdNPStatsTxRawGoodPkts,'brcdNPStatsTxSrcPortSupressDrop':brcdNPStatsTxSrcPortSupressDrop,'brcdNPStatsTxBadPktsCnt':brcdNPStatsTxBadPktsCnt,'brcdNPStatsTxUnicastPkts':brcdNPStatsTxUnicastPkts,'brcdNPStatsTxBroadcastPkts':brcdNPStatsTxBroadcastPkts,'brcdNPStatsTxMulticastPkts':brcdNPStatsTxMulticastPkts,'brcdNPStatsTxReceiveFromTM':brcdNPStatsTxReceiveFromTM,'brcdNPStatsTxACLDrop':brcdNPStatsTxACLDrop,'brcdNPStatsTxPFCMulticastDrop':brcdNPStatsTxPFCMulticastDrop,'brcdNPStatsTxPFCMTUExceedDrop':brcdNPStatsTxPFCMTUExceedDrop,'brcdNPStatsTxPFCQMAPErrorDrop':brcdNPStatsTxPFCQMAPErrorDrop,'brcdNPStatsTxIPv4Pkts':brcdNPStatsTxIPv4Pkts,'brcdNPStatsTxIPv6Pkts':brcdNPStatsTxIPv6Pkts,'brcdNPStatsTxIPv4Bytes':brcdNPStatsTxIPv4Bytes,'brcdNPStatsTxIPv6Bytes':brcdNPStatsTxIPv6Bytes,'brcdNPStatsTxPOSCtrlProtocolPkts':brcdNPStatsTxPOSCtrlProtocolPkts,'brcdNPStatsTxPOSLinkDrop':brcdNPStatsTxPOSLinkDrop,'brcdNPQosStatTable':brcdNPQosStatTable,'brcdNPQosStatEntry':brcdNPQosStatEntry,_Q:brcdNPQosStatIfIndex,_R:brcdNPQosStatQosPriority,'brcdNPQosStatIngressPkts':brcdNPQosStatIngressPkts,'brcdNPQosStatIngressBytes':brcdNPQosStatIngressBytes,'brcdNPQosStatEgressPkts':brcdNPQosStatEgressPkts,'brcdNPQosStatEgressBytes':brcdNPQosStatEgressBytes,'brcdNPBufferErrorTable':brcdNPBufferErrorTable,'brcdNPBufferErrorEntry':brcdNPBufferErrorEntry,_S:brcdNPBufferErrorSlotId,_T:brcdNPBufferErrorDeviceId,_L:brcdNPBufferErrorDescription,_x:brcdNPBufferErrorIngressCurrentEvents,'brcdNPBufferErrorIngressCumulativeEvents':brcdNPBufferErrorIngressCumulativeEvents,_y:brcdNPBufferErrorEgressCurrentEvents,'brcdNPBufferErrorEgressCumulativeEvents':brcdNPBufferErrorEgressCumulativeEvents,'brcdNPCSRAMErrorTable':brcdNPCSRAMErrorTable,'brcdNPCSRAMErrorEntry':brcdNPCSRAMErrorEntry,_U:brcdNPCSRAMErrorSlotId,_V:brcdNPCSRAMErrorDeviceId,_z:brcdNPCSRAMErrorDescription,_A0:brcdNPCSRAMErrorCurrentEvents,'brcdNPCSRAMErrorCumulativeEvents':brcdNPCSRAMErrorCumulativeEvents,'brcdNPLPMRAMErrorTable':brcdNPLPMRAMErrorTable,'brcdNPLPMRAMErrorEntry':brcdNPLPMRAMErrorEntry,_W:brcdNPLPMRAMErrorIndex,_X:brcdNPLPMRAMErrorSlotId,_Y:brcdNPLPMRAMErrorDeviceId,_A1:brcdNPLPMRAMErrorName,_A2:brcdNPLPMRAMErrorDescription,_A3:brcdNPLPMRAMErrorCurrentEvents,'brcdNPLPMRAMErrorCumulativeEvents':brcdNPLPMRAMErrorCumulativeEvents,'brcdNPDebugStatTable':brcdNPDebugStatTable,'brcdNPDebugStatEntry':brcdNPDebugStatEntry,_Z:brcdNPDebugStatSlotId,_a:brcdNPDebugStatNPDeviceId,'brcdNPDebugStatDescription':brcdNPDebugStatDescription,'brcdNPDebugStatL2SourceAddrLearnDrop':brcdNPDebugStatL2SourceAddrLearnDrop,'brcdNPDebugStatRateLimitVPLSLocalLearnDrop':brcdNPDebugStatRateLimitVPLSLocalLearnDrop,'brcdNPDebugStatUnkownMPLSDrop':brcdNPDebugStatUnkownMPLSDrop,'brcdNPDebugStatDestAddrVCMiss':brcdNPDebugStatDestAddrVCMiss,'brcdNPDebugStatRateLimitVPLSRemoteLearnDrop':brcdNPDebugStatRateLimitVPLSRemoteLearnDrop,'brcdNPDebugStatIPv4DestAddrVCMiss':brcdNPDebugStatIPv4DestAddrVCMiss,'brcdNPDebugStatIPv6DestAddrVCMiss':brcdNPDebugStatIPv6DestAddrVCMiss,'brcdNPDebugStatVPLSTx':brcdNPDebugStatVPLSTx,'brcdNPDebugStatVLLTx':brcdNPDebugStatVLLTx,'brcdNPDebugStatUnknowL3VPNIngressDrop':brcdNPDebugStatUnknowL3VPNIngressDrop,'brcdNPDebugStatIPv6VPNTx':brcdNPDebugStatIPv6VPNTx,'brcdNPDebugStatIPv4VPNTx':brcdNPDebugStatIPv4VPNTx,'brcdNPDebugStatGREIPv4RxCount':brcdNPDebugStatGREIPv4RxCount,'brcdNPDebugStatGREInvalidDrop':brcdNPDebugStatGREInvalidDrop,'brcdNPDebugStat6to4RxCount':brcdNPDebugStat6to4RxCount,'brcdNPDebugStatGREEnfSourceIngressChkMiss':brcdNPDebugStatGREEnfSourceIngressChkMiss,'brcdNPDebugStat6to4EnfSourceIngressChkMiss':brcdNPDebugStat6to4EnfSourceIngressChkMiss,'brcdNPDebugStatGREMPLSRxCount':brcdNPDebugStatGREMPLSRxCount,'brcdNPDebugStatGREIPv6RxCount':brcdNPDebugStatGREIPv6RxCount,'brcdNPDebugStatPBBRxDropCount':brcdNPDebugStatPBBRxDropCount,'brcdNPDebugStatPBBTxCount':brcdNPDebugStatPBBTxCount,'brcdNPDebugStatIPv4DestAddrVCDrop':brcdNPDebugStatIPv4DestAddrVCDrop,'brcdNPDebugStatIPv6DestAddrVCDrop':brcdNPDebugStatIPv6DestAddrVCDrop,'brcdNPDebugStatSourceAddrPortVLANMiss':brcdNPDebugStatSourceAddrPortVLANMiss,'brcdNPDebugStatVPLSSourceAddrPortVLANMiss':brcdNPDebugStatVPLSSourceAddrPortVLANMiss,'brcdNPDebugStatSourceAddrVCMiss':brcdNPDebugStatSourceAddrVCMiss,'brcdNPDebugStatIPv4HWFwdCount':brcdNPDebugStatIPv4HWFwdCount,'brcdNPDebugStatIPv6HWFwdCount':brcdNPDebugStatIPv6HWFwdCount,'brcdNPDebugStatMulticastRPFDropCount':brcdNPDebugStatMulticastRPFDropCount,'brcdNPDebugStatMPLSLsrTxCount':brcdNPDebugStatMPLSLsrTxCount,'brcdNPDebugStatGREIPv4TxCount':brcdNPDebugStatGREIPv4TxCount,'brcdNPDebugStat6to4TxCount':brcdNPDebugStat6to4TxCount,'brcdNPDebugStatMPLSRSVPTxCount':brcdNPDebugStatMPLSRSVPTxCount,'brcdNPDebugStatGREMPLSTxCount':brcdNPDebugStatGREMPLSTxCount,'brcdNPDebugStatGREIPv6TxCount':brcdNPDebugStatGREIPv6TxCount,'brcdTMStatisticsInfo':brcdTMStatisticsInfo,'brcdTMStatisticsInfoGroup':brcdTMStatisticsInfoGroup,'brcdTMPortMappingMaxPorts':brcdTMPortMappingMaxPorts,'brcdTMPortMappingUsedPorts':brcdTMPortMappingUsedPorts,'brcdTMPortMappingAvailablePorts':brcdTMPortMappingAvailablePorts,'brcdTMStatsTable':brcdTMStatsTable,'brcdTMStatsEntry':brcdTMStatsEntry,_b:brcdTMStatsSlotId,_c:brcdTMStatsTMDeviceId,'brcdTMStatsDescription':brcdTMStatsDescription,'brcdTMStatsTotalIngressPktsCnt':brcdTMStatsTotalIngressPktsCnt,'brcdTMStatsIngressEnqueuePkts':brcdTMStatsIngressEnqueuePkts,'brcdTMStatsEgressEnqueuePkts':brcdTMStatsEgressEnqueuePkts,'brcdTMStatsIngressEnqueueBytes':brcdTMStatsIngressEnqueueBytes,'brcdTMStatsEgressEnqueueBytes':brcdTMStatsEgressEnqueueBytes,'brcdTMStatsIngressDequeuePkts':brcdTMStatsIngressDequeuePkts,'brcdTMStatsIngressDequeueBytes':brcdTMStatsIngressDequeueBytes,'brcdTMStatsIngressTotalQDiscardPkts':brcdTMStatsIngressTotalQDiscardPkts,'brcdTMStatsIngressTotalQDiscardBytes':brcdTMStatsIngressTotalQDiscardBytes,'brcdTMStatsIngressOldestDiscardPkts':brcdTMStatsIngressOldestDiscardPkts,'brcdTMStatsIngressOldestDiscardBytes':brcdTMStatsIngressOldestDiscardBytes,'brcdTMStatsEgressDiscardPkts':brcdTMStatsEgressDiscardPkts,'brcdTMStatsEgressDiscardBytes':brcdTMStatsEgressDiscardBytes,'brcdTMUcastQStatsTable':brcdTMUcastQStatsTable,'brcdTMUcastQStatsEntry':brcdTMUcastQStatsEntry,_d:brcdTMUcastQStatsSlotId,_e:brcdTMUcastQStatsTMDeviceId,_f:brcdTMUcastQStatsDstIfIndex,_g:brcdTMUcastQStatsPriority,'brcdTMUcastQStatsDescription':brcdTMUcastQStatsDescription,'brcdTMUcastQStatsEnquePkts':brcdTMUcastQStatsEnquePkts,'brcdTMUcastQStatsEnqueBytes':brcdTMUcastQStatsEnqueBytes,'brcdTMUcastQStatsDequePkts':brcdTMUcastQStatsDequePkts,'brcdTMUcastQStatsDequeBytes':brcdTMUcastQStatsDequeBytes,'brcdTMUcastQStatsTotalQDiscardPkts':brcdTMUcastQStatsTotalQDiscardPkts,'brcdTMUcastQStatsTotalQDiscardBytes':brcdTMUcastQStatsTotalQDiscardBytes,'brcdTMUcastQStatsOldestDiscardPkts':brcdTMUcastQStatsOldestDiscardPkts,'brcdTMUcastQStatsOldestDiscardBytes':brcdTMUcastQStatsOldestDiscardBytes,'brcdTMUcastQStatsWREDDroppedPkts':brcdTMUcastQStatsWREDDroppedPkts,'brcdTMUcastQStatsWREDDroppedBytes':brcdTMUcastQStatsWREDDroppedBytes,'brcdTMUcastQStatsMaxQDepthSinceLastRead':brcdTMUcastQStatsMaxQDepthSinceLastRead,'brcdTMUcastQStatsQSize':brcdTMUcastQStatsQSize,'brcdTMUcastQStatsCreditCount':brcdTMUcastQStatsCreditCount,'brcdTMMcastQStatsTable':brcdTMMcastQStatsTable,'brcdTMMcastQStatsEntry':brcdTMMcastQStatsEntry,_h:brcdTMMcastQStatsSlotId,_i:brcdTMMcastQStatsTMDeviceId,_j:brcdTMMcastQStatsPriority,'brcdTMMcastQStatsDescription':brcdTMMcastQStatsDescription,'brcdTMMcastQStatsEnquePkts':brcdTMMcastQStatsEnquePkts,'brcdTMMcastQStatsEnqueBytes':brcdTMMcastQStatsEnqueBytes,'brcdTMMcastQStatsDequePkts':brcdTMMcastQStatsDequePkts,'brcdTMMcastQStatsDequeBytes':brcdTMMcastQStatsDequeBytes,'brcdTMMcastQStatsTotalQDiscardPkts':brcdTMMcastQStatsTotalQDiscardPkts,'brcdTMMcastQStatsTotalQDiscardBytes':brcdTMMcastQStatsTotalQDiscardBytes,'brcdTMMcastQStatsOldestDiscardPkts':brcdTMMcastQStatsOldestDiscardPkts,'brcdTMMcastQStatsOldestDiscardBytes':brcdTMMcastQStatsOldestDiscardBytes,'brcdTMMcastQStatsWREDDroppedPkts':brcdTMMcastQStatsWREDDroppedPkts,'brcdTMMcastQStatsWREDDroppedBytes':brcdTMMcastQStatsWREDDroppedBytes,'brcdTMMcastQStatsMaxQDepthSinceLastRead':brcdTMMcastQStatsMaxQDepthSinceLastRead,'brcdTMMcastQStatsQSize':brcdTMMcastQStatsQSize,'brcdTMMcastQStatsCreditCount':brcdTMMcastQStatsCreditCount,'brcdTMCpuQStatsTable':brcdTMCpuQStatsTable,'brcdTMCpuQStatsEntry':brcdTMCpuQStatsEntry,_I:brcdTMCpuQStatsSlotId,_J:brcdTMCpuQStatsTMDeviceId,_o:brcdTMCpuQStatsType,_K:brcdTMCpuQStatsPriority,'brcdTMCpuQStatsDescription':brcdTMCpuQStatsDescription,'brcdTMCpuQStatsEnquePkts':brcdTMCpuQStatsEnquePkts,'brcdTMCpuQStatsEnqueBytes':brcdTMCpuQStatsEnqueBytes,'brcdTMCpuQStatsDequePkts':brcdTMCpuQStatsDequePkts,'brcdTMCpuQStatsDequeBytes':brcdTMCpuQStatsDequeBytes,'brcdTMCpuQStatsTotalQDiscardPkts':brcdTMCpuQStatsTotalQDiscardPkts,'brcdTMCpuQStatsTotalQDiscardBytes':brcdTMCpuQStatsTotalQDiscardBytes,'brcdTMCpuQStatsOldestDiscardPkts':brcdTMCpuQStatsOldestDiscardPkts,'brcdTMCpuQStatsOldestDiscardBytes':brcdTMCpuQStatsOldestDiscardBytes,'brcdTMCpuQStatsWREDDroppedPkts':brcdTMCpuQStatsWREDDroppedPkts,'brcdTMCpuQStatsWREDDroppedBytes':brcdTMCpuQStatsWREDDroppedBytes,'brcdTMCpuQStatsMaxQDepthSinceLastRead':brcdTMCpuQStatsMaxQDepthSinceLastRead,'brcdTMCpuQStatsQSize':brcdTMCpuQStatsQSize,'brcdTMCpuQStatsCreditCount':brcdTMCpuQStatsCreditCount,'brcdTMMcastStreamQStatsTable':brcdTMMcastStreamQStatsTable,'brcdTMMcastStreamQStatsEntry':brcdTMMcastStreamQStatsEntry,_p:brcdTMMcastStreamQStatsAddressType,_q:brcdTMMcastStreamQStatsSource,_r:brcdTMMcastStreamQStatsGroup,_s:brcdTMMcastStreamQStatsGroupPrefixLength,'brcdTMMcastStreamQStatsPriority':brcdTMMcastStreamQStatsPriority,'brcdTMMcastStreamQStatsEnquePkts':brcdTMMcastStreamQStatsEnquePkts,'brcdTMMcastStreamQStatsEnqueBytes':brcdTMMcastStreamQStatsEnqueBytes,'brcdTMMcastStreamQStatsDequePkts':brcdTMMcastStreamQStatsDequePkts,'brcdTMMcastStreamQStatsDequeBytes':brcdTMMcastStreamQStatsDequeBytes,'brcdTMMcastStreamQStatsTotalQDiscardPkts':brcdTMMcastStreamQStatsTotalQDiscardPkts,'brcdTMMcastStreamQStatsTotalQDiscardBytes':brcdTMMcastStreamQStatsTotalQDiscardBytes,'brcdTMMcastStreamQStatsOldestDiscardPkts':brcdTMMcastStreamQStatsOldestDiscardPkts,'brcdTMMcastStreamQStatsOldestDiscardBytes':brcdTMMcastStreamQStatsOldestDiscardBytes,'brcdTMMcastStreamQStatsWREDDroppedPkts':brcdTMMcastStreamQStatsWREDDroppedPkts,'brcdTMMcastStreamQStatsWREDDroppedBytes':brcdTMMcastStreamQStatsWREDDroppedBytes,'brcdTMMcastStreamQStatsMaxQDepthSinceLastRead':brcdTMMcastStreamQStatsMaxQDepthSinceLastRead,'brcdTMMcastStreamQStatsQSize':brcdTMMcastStreamQStatsQSize,'brcdTMMcastStreamQStatsCreditCount':brcdTMMcastStreamQStatsCreditCount,'brcdTMCpuQInfoTable':brcdTMCpuQInfoTable,'brcdTMCpuQInfoEntry':brcdTMCpuQInfoEntry,_t:brcdTMCpuQInfoSlotId,_u:brcdTMCpuQInfoTMDeviceId,'brcdTMCpuQInfoPriority0QSize':brcdTMCpuQInfoPriority0QSize,'brcdTMCpuQInfoPriority0CreditCount':brcdTMCpuQInfoPriority0CreditCount,'brcdTMCpuQInfoPriority1QSize':brcdTMCpuQInfoPriority1QSize,'brcdTMCpuQInfoPriority1CreditCount':brcdTMCpuQInfoPriority1CreditCount,'brcdTMCpuQInfoPriority2QSize':brcdTMCpuQInfoPriority2QSize,'brcdTMCpuQInfoPriority2CreditCount':brcdTMCpuQInfoPriority2CreditCount,'brcdTMCpuQInfoPriority3QSize':brcdTMCpuQInfoPriority3QSize,'brcdTMCpuQInfoPriority3CreditCount':brcdTMCpuQInfoPriority3CreditCount,'brcdTMCpuQInfoPriority4QSize':brcdTMCpuQInfoPriority4QSize,'brcdTMCpuQInfoPriority4CreditCount':brcdTMCpuQInfoPriority4CreditCount,'brcdTMCpuQInfoPriority5QSize':brcdTMCpuQInfoPriority5QSize,'brcdTMCpuQInfoPriority5CreditCount':brcdTMCpuQInfoPriority5CreditCount,'brcdTMCpuQInfoPriority6QSize':brcdTMCpuQInfoPriority6QSize,'brcdTMCpuQInfoPriority6CreditCount':brcdTMCpuQInfoPriority6CreditCount,'brcdTMCpuQInfoPriority7QSize':brcdTMCpuQInfoPriority7QSize,'brcdTMCpuQInfoPriority7CreditCount':brcdTMCpuQInfoPriority7CreditCount,'brcdTMDestUcastQStatTable':brcdTMDestUcastQStatTable,'brcdTMDestUcastQStatEntry':brcdTMDestUcastQStatEntry,_v:brcdTMDestUcastQStatDestIfIndex,_w:brcdTMDestUcastQStatPriority,'brcdTMDestUcastQStatEnquePkts':brcdTMDestUcastQStatEnquePkts,'brcdTMDestUcastQStatEnqueBytes':brcdTMDestUcastQStatEnqueBytes,'brcdTMDestUcastQStatDequePkts':brcdTMDestUcastQStatDequePkts,'brcdTMDestUcastQStatDequeBytes':brcdTMDestUcastQStatDequeBytes,'brcdTMDestUcastQStatTotalQDiscardPkts':brcdTMDestUcastQStatTotalQDiscardPkts,'brcdTMDestUcastQStatTotalQDiscardBytes':brcdTMDestUcastQStatTotalQDiscardBytes,'brcdTMCpuAggrQStatsTable':brcdTMCpuAggrQStatsTable,'brcdTMCpuAggrQStatsEntry':brcdTMCpuAggrQStatsEntry,'brcdTMCpuAggrQStatsDescription':brcdTMCpuAggrQStatsDescription,'brcdTMCpuAggrQStatsEnquePkts':brcdTMCpuAggrQStatsEnquePkts,'brcdTMCpuAggrQStatsEnqueBytes':brcdTMCpuAggrQStatsEnqueBytes,'brcdTMCpuAggrQStatsDequePkts':brcdTMCpuAggrQStatsDequePkts,'brcdTMCpuAggrQStatsDequeBytes':brcdTMCpuAggrQStatsDequeBytes,'brcdTMCpuAggrQStatsTotalQDiscardPkts':brcdTMCpuAggrQStatsTotalQDiscardPkts,'brcdTMCpuAggrQStatsTotalQDiscardBytes':brcdTMCpuAggrQStatsTotalQDiscardBytes,'brcdTMCpuAggrQStatsOldestDiscardPkts':brcdTMCpuAggrQStatsOldestDiscardPkts,'brcdTMCpuAggrQStatsOldestDiscardBytes':brcdTMCpuAggrQStatsOldestDiscardBytes,'brcdTMCpuAggrQStatsWREDDroppedPkts':brcdTMCpuAggrQStatsWREDDroppedPkts,'brcdTMCpuAggrQStatsWREDDroppedBytes':brcdTMCpuAggrQStatsWREDDroppedBytes,'brcdNPGlobal':brcdNPGlobal,'brcdNPIndex':brcdNPIndex,'brcdNPLockupRecoveryCount':brcdNPLockupRecoveryCount})