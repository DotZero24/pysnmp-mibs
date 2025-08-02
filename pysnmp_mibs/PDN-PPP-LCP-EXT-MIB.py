_AA='pdnPpppLcpExtLinkStateCounterGroup'
_A9='pdnPpppLcpExtDiscardTestGroup'
_A8='pdnPppLcpExtEchoTestGroup'
_A7='pdnPppLcpExtKeepAliveConfGroup'
_A6='pdnPppLcpExtACFCGroup'
_A5='pdnPppLcpExtPFCGroup'
_A4='pdnPppLcpExtKeepAliveCountersGroup'
_A3='pdnPppLcpExtPacketCountersGroup'
_A2='pdnPppLcpExtMagicNumberGroup'
_A1='pdnPppLcpExtEstablishFailedGroup'
_A0='pdnPppLcpExtStateMachineGroup'
_z='pdnPppLinkStatusTotalTerminates'
_y='pdnPppLinkTestSendDiscardTest'
_x='pdnPppLinkStatusTotalEchoRequestsPassed'
_w='pdnPppLinkStatusTotalEchoRequestsBadData'
_v='pdnPppLinkStatusTotalEchoRequestsTimeOuts'
_u='pdnPppLinkTestLastEchoTestResults'
_t='pdnPppLinkTestEchoTestTimeout'
_s='pdnPppLinkTestSendEchoTest'
_r='pdnPppLinkConfigKeepAliveTimeout'
_q='pdnPppLinkConfigKeepAliveQuietTime'
_p='pdnPppLinkConfigACFC'
_o='pdnPppLinkConfigPFC'
_n='pdnPppLinkStatusTotalKeepAlivesLost'
_m='pdnPppLinkStatusTotalReceivedKeepAlives'
_l='pdnPppLinkStatusTotalSentKeepAlives'
_k='pdnPppLinkStatusTotalReceivedDiscardRequests'
_j='pdnPppLinkStatusTotalSentDiscardRequests'
_i='pdnPppLinkStatusTotalReceivedEchoReplies'
_h='pdnPppLinkStatusTotalSentEchoReplies'
_g='pdnPppLinkStatusTotalReceivedEchoRequests'
_f='pdnPppLinkStatusTotalSentEchoRequests'
_e='pdnPppLinkStatusTotalReceivedProtocolRejects'
_d='pdnPppLinkStatusTotalSentProtocolRejects'
_c='pdnPppLinkStatusTotalReceivedCodeRejects'
_b='pdnPppLinkStatusTotalSentCodeRejects'
_a='pdnPppLinkStatusTotalReceivedTerminateAcks'
_Z='pdnPppLinkStatusTotalSentTerminateAcks'
_Y='pdnPppLinkStatusTotalReceivedTerminateRequests'
_X='pdnPppLinkStatusTotalSentTerminateRequests'
_W='pdnPppLinkStatusTotalReceivedConfigRejects'
_V='pdnPppLinkStatusTotalSentConfigRejects'
_U='pdnPppLinkStatusTotalReceivedConfigNaks'
_T='pdnPppLinkStatusTotalSentConfigNaks'
_S='pdnPppLinkStatusTotalReceivedConfigAcks'
_R='pdnPppLinkStatusTotalSentConfigAcks'
_Q='pdnPppLinkStatusTotalReceivedConfigRequests'
_P='pdnPppLinkStatusTotalSentConfigRequests'
_O='pdnPppLinkStatusRemoteToLocalMagicNumber'
_N='pdnPppLinkStatusLocalToRemoteMagicNumber'
_M='pdnPppLinkStatusEstablishFailedReason'
_L='pdnPppLinkStatusCurrState'
_K='pdnPppLinkConfigExtEntry'
_J='pdnPppLinkStatusExtEntry'
_I='ifIndex'
_H='IF-MIB'
_G='seconds'
_F='Unsigned32'
_E='Integer32'
_D='read-write'
_C='read-only'
_B='PDN-PPP-LCP-EXT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_H,_I)
pdn_interfaces,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-interfaces')
PdnPPPState,SwitchState=mibBuilder.importSymbols('PDN-TC','PdnPPPState','SwitchState')
pppLinkConfigEntry,pppLinkStatusEntry=mibBuilder.importSymbols('PPP-LCP-MIB','pppLinkConfigEntry','pppLinkStatusEntry')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pdnPppLcpExtMIB=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,6,28))
if mibBuilder.loadTexts:pdnPppLcpExtMIB.setRevisions(('2004-09-10 00:00',))
_PdnPppLcpExtNotifications_ObjectIdentity=ObjectIdentity
pdnPppLcpExtNotifications=_PdnPppLcpExtNotifications_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,28,0))
_PdnPppLcpExtObjects_ObjectIdentity=ObjectIdentity
pdnPppLcpExtObjects=_PdnPppLcpExtObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,28,1))
_PdnPppLinkStatusExtTable_Object=MibTable
pdnPppLinkStatusExtTable=_PdnPppLinkStatusExtTable_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1))
if mibBuilder.loadTexts:pdnPppLinkStatusExtTable.setStatus(_A)
_PdnPppLinkStatusExtEntry_Object=MibTableRow
pdnPppLinkStatusExtEntry=_PdnPppLinkStatusExtEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1))
if mibBuilder.loadTexts:pdnPppLinkStatusExtEntry.setStatus(_A)
_PdnPppLinkStatusCurrState_Type=PdnPPPState
_PdnPppLinkStatusCurrState_Object=MibTableColumn
pdnPppLinkStatusCurrState=_PdnPppLinkStatusCurrState_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,1),_PdnPppLinkStatusCurrState_Type())
pdnPppLinkStatusCurrState.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusCurrState.setStatus(_A)
_PdnPppLinkStatusEstablishFailedReason_Type=DisplayString
_PdnPppLinkStatusEstablishFailedReason_Object=MibTableColumn
pdnPppLinkStatusEstablishFailedReason=_PdnPppLinkStatusEstablishFailedReason_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,2),_PdnPppLinkStatusEstablishFailedReason_Type())
pdnPppLinkStatusEstablishFailedReason.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusEstablishFailedReason.setStatus(_A)
_PdnPppLinkStatusLocalToRemoteMagicNumber_Type=Unsigned32
_PdnPppLinkStatusLocalToRemoteMagicNumber_Object=MibTableColumn
pdnPppLinkStatusLocalToRemoteMagicNumber=_PdnPppLinkStatusLocalToRemoteMagicNumber_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,3),_PdnPppLinkStatusLocalToRemoteMagicNumber_Type())
pdnPppLinkStatusLocalToRemoteMagicNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusLocalToRemoteMagicNumber.setStatus(_A)
_PdnPppLinkStatusRemoteToLocalMagicNumber_Type=Unsigned32
_PdnPppLinkStatusRemoteToLocalMagicNumber_Object=MibTableColumn
pdnPppLinkStatusRemoteToLocalMagicNumber=_PdnPppLinkStatusRemoteToLocalMagicNumber_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,4),_PdnPppLinkStatusRemoteToLocalMagicNumber_Type())
pdnPppLinkStatusRemoteToLocalMagicNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusRemoteToLocalMagicNumber.setStatus(_A)
_PdnPppLinkStatusTotalSentConfigRequests_Type=Counter32
_PdnPppLinkStatusTotalSentConfigRequests_Object=MibTableColumn
pdnPppLinkStatusTotalSentConfigRequests=_PdnPppLinkStatusTotalSentConfigRequests_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,5),_PdnPppLinkStatusTotalSentConfigRequests_Type())
pdnPppLinkStatusTotalSentConfigRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalSentConfigRequests.setStatus(_A)
_PdnPppLinkStatusTotalReceivedConfigRequests_Type=Counter32
_PdnPppLinkStatusTotalReceivedConfigRequests_Object=MibTableColumn
pdnPppLinkStatusTotalReceivedConfigRequests=_PdnPppLinkStatusTotalReceivedConfigRequests_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,6),_PdnPppLinkStatusTotalReceivedConfigRequests_Type())
pdnPppLinkStatusTotalReceivedConfigRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalReceivedConfigRequests.setStatus(_A)
_PdnPppLinkStatusTotalSentConfigAcks_Type=Counter32
_PdnPppLinkStatusTotalSentConfigAcks_Object=MibTableColumn
pdnPppLinkStatusTotalSentConfigAcks=_PdnPppLinkStatusTotalSentConfigAcks_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,7),_PdnPppLinkStatusTotalSentConfigAcks_Type())
pdnPppLinkStatusTotalSentConfigAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalSentConfigAcks.setStatus(_A)
_PdnPppLinkStatusTotalReceivedConfigAcks_Type=Counter32
_PdnPppLinkStatusTotalReceivedConfigAcks_Object=MibTableColumn
pdnPppLinkStatusTotalReceivedConfigAcks=_PdnPppLinkStatusTotalReceivedConfigAcks_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,8),_PdnPppLinkStatusTotalReceivedConfigAcks_Type())
pdnPppLinkStatusTotalReceivedConfigAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalReceivedConfigAcks.setStatus(_A)
_PdnPppLinkStatusTotalSentConfigNaks_Type=Counter32
_PdnPppLinkStatusTotalSentConfigNaks_Object=MibTableColumn
pdnPppLinkStatusTotalSentConfigNaks=_PdnPppLinkStatusTotalSentConfigNaks_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,9),_PdnPppLinkStatusTotalSentConfigNaks_Type())
pdnPppLinkStatusTotalSentConfigNaks.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalSentConfigNaks.setStatus(_A)
_PdnPppLinkStatusTotalReceivedConfigNaks_Type=Counter32
_PdnPppLinkStatusTotalReceivedConfigNaks_Object=MibTableColumn
pdnPppLinkStatusTotalReceivedConfigNaks=_PdnPppLinkStatusTotalReceivedConfigNaks_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,10),_PdnPppLinkStatusTotalReceivedConfigNaks_Type())
pdnPppLinkStatusTotalReceivedConfigNaks.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalReceivedConfigNaks.setStatus(_A)
_PdnPppLinkStatusTotalSentConfigRejects_Type=Counter32
_PdnPppLinkStatusTotalSentConfigRejects_Object=MibTableColumn
pdnPppLinkStatusTotalSentConfigRejects=_PdnPppLinkStatusTotalSentConfigRejects_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,11),_PdnPppLinkStatusTotalSentConfigRejects_Type())
pdnPppLinkStatusTotalSentConfigRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalSentConfigRejects.setStatus(_A)
_PdnPppLinkStatusTotalReceivedConfigRejects_Type=Counter32
_PdnPppLinkStatusTotalReceivedConfigRejects_Object=MibTableColumn
pdnPppLinkStatusTotalReceivedConfigRejects=_PdnPppLinkStatusTotalReceivedConfigRejects_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,12),_PdnPppLinkStatusTotalReceivedConfigRejects_Type())
pdnPppLinkStatusTotalReceivedConfigRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalReceivedConfigRejects.setStatus(_A)
_PdnPppLinkStatusTotalSentTerminateRequests_Type=Counter32
_PdnPppLinkStatusTotalSentTerminateRequests_Object=MibTableColumn
pdnPppLinkStatusTotalSentTerminateRequests=_PdnPppLinkStatusTotalSentTerminateRequests_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,13),_PdnPppLinkStatusTotalSentTerminateRequests_Type())
pdnPppLinkStatusTotalSentTerminateRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalSentTerminateRequests.setStatus(_A)
_PdnPppLinkStatusTotalReceivedTerminateRequests_Type=Counter32
_PdnPppLinkStatusTotalReceivedTerminateRequests_Object=MibTableColumn
pdnPppLinkStatusTotalReceivedTerminateRequests=_PdnPppLinkStatusTotalReceivedTerminateRequests_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,14),_PdnPppLinkStatusTotalReceivedTerminateRequests_Type())
pdnPppLinkStatusTotalReceivedTerminateRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalReceivedTerminateRequests.setStatus(_A)
_PdnPppLinkStatusTotalSentTerminateAcks_Type=Counter32
_PdnPppLinkStatusTotalSentTerminateAcks_Object=MibTableColumn
pdnPppLinkStatusTotalSentTerminateAcks=_PdnPppLinkStatusTotalSentTerminateAcks_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,15),_PdnPppLinkStatusTotalSentTerminateAcks_Type())
pdnPppLinkStatusTotalSentTerminateAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalSentTerminateAcks.setStatus(_A)
_PdnPppLinkStatusTotalReceivedTerminateAcks_Type=Counter32
_PdnPppLinkStatusTotalReceivedTerminateAcks_Object=MibTableColumn
pdnPppLinkStatusTotalReceivedTerminateAcks=_PdnPppLinkStatusTotalReceivedTerminateAcks_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,16),_PdnPppLinkStatusTotalReceivedTerminateAcks_Type())
pdnPppLinkStatusTotalReceivedTerminateAcks.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalReceivedTerminateAcks.setStatus(_A)
_PdnPppLinkStatusTotalSentCodeRejects_Type=Counter32
_PdnPppLinkStatusTotalSentCodeRejects_Object=MibTableColumn
pdnPppLinkStatusTotalSentCodeRejects=_PdnPppLinkStatusTotalSentCodeRejects_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,17),_PdnPppLinkStatusTotalSentCodeRejects_Type())
pdnPppLinkStatusTotalSentCodeRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalSentCodeRejects.setStatus(_A)
_PdnPppLinkStatusTotalReceivedCodeRejects_Type=Counter32
_PdnPppLinkStatusTotalReceivedCodeRejects_Object=MibTableColumn
pdnPppLinkStatusTotalReceivedCodeRejects=_PdnPppLinkStatusTotalReceivedCodeRejects_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,18),_PdnPppLinkStatusTotalReceivedCodeRejects_Type())
pdnPppLinkStatusTotalReceivedCodeRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalReceivedCodeRejects.setStatus(_A)
_PdnPppLinkStatusTotalSentProtocolRejects_Type=Counter32
_PdnPppLinkStatusTotalSentProtocolRejects_Object=MibTableColumn
pdnPppLinkStatusTotalSentProtocolRejects=_PdnPppLinkStatusTotalSentProtocolRejects_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,19),_PdnPppLinkStatusTotalSentProtocolRejects_Type())
pdnPppLinkStatusTotalSentProtocolRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalSentProtocolRejects.setStatus(_A)
_PdnPppLinkStatusTotalReceivedProtocolRejects_Type=Counter32
_PdnPppLinkStatusTotalReceivedProtocolRejects_Object=MibTableColumn
pdnPppLinkStatusTotalReceivedProtocolRejects=_PdnPppLinkStatusTotalReceivedProtocolRejects_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,20),_PdnPppLinkStatusTotalReceivedProtocolRejects_Type())
pdnPppLinkStatusTotalReceivedProtocolRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalReceivedProtocolRejects.setStatus(_A)
_PdnPppLinkStatusTotalSentEchoRequests_Type=Counter32
_PdnPppLinkStatusTotalSentEchoRequests_Object=MibTableColumn
pdnPppLinkStatusTotalSentEchoRequests=_PdnPppLinkStatusTotalSentEchoRequests_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,21),_PdnPppLinkStatusTotalSentEchoRequests_Type())
pdnPppLinkStatusTotalSentEchoRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalSentEchoRequests.setStatus(_A)
_PdnPppLinkStatusTotalReceivedEchoRequests_Type=Counter32
_PdnPppLinkStatusTotalReceivedEchoRequests_Object=MibTableColumn
pdnPppLinkStatusTotalReceivedEchoRequests=_PdnPppLinkStatusTotalReceivedEchoRequests_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,22),_PdnPppLinkStatusTotalReceivedEchoRequests_Type())
pdnPppLinkStatusTotalReceivedEchoRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalReceivedEchoRequests.setStatus(_A)
_PdnPppLinkStatusTotalSentEchoReplies_Type=Counter32
_PdnPppLinkStatusTotalSentEchoReplies_Object=MibTableColumn
pdnPppLinkStatusTotalSentEchoReplies=_PdnPppLinkStatusTotalSentEchoReplies_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,23),_PdnPppLinkStatusTotalSentEchoReplies_Type())
pdnPppLinkStatusTotalSentEchoReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalSentEchoReplies.setStatus(_A)
_PdnPppLinkStatusTotalReceivedEchoReplies_Type=Counter32
_PdnPppLinkStatusTotalReceivedEchoReplies_Object=MibTableColumn
pdnPppLinkStatusTotalReceivedEchoReplies=_PdnPppLinkStatusTotalReceivedEchoReplies_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,24),_PdnPppLinkStatusTotalReceivedEchoReplies_Type())
pdnPppLinkStatusTotalReceivedEchoReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalReceivedEchoReplies.setStatus(_A)
_PdnPppLinkStatusTotalSentDiscardRequests_Type=Counter32
_PdnPppLinkStatusTotalSentDiscardRequests_Object=MibTableColumn
pdnPppLinkStatusTotalSentDiscardRequests=_PdnPppLinkStatusTotalSentDiscardRequests_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,25),_PdnPppLinkStatusTotalSentDiscardRequests_Type())
pdnPppLinkStatusTotalSentDiscardRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalSentDiscardRequests.setStatus(_A)
_PdnPppLinkStatusTotalReceivedDiscardRequests_Type=Counter32
_PdnPppLinkStatusTotalReceivedDiscardRequests_Object=MibTableColumn
pdnPppLinkStatusTotalReceivedDiscardRequests=_PdnPppLinkStatusTotalReceivedDiscardRequests_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,26),_PdnPppLinkStatusTotalReceivedDiscardRequests_Type())
pdnPppLinkStatusTotalReceivedDiscardRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalReceivedDiscardRequests.setStatus(_A)
_PdnPppLinkStatusTotalSentKeepAlives_Type=Counter32
_PdnPppLinkStatusTotalSentKeepAlives_Object=MibTableColumn
pdnPppLinkStatusTotalSentKeepAlives=_PdnPppLinkStatusTotalSentKeepAlives_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,27),_PdnPppLinkStatusTotalSentKeepAlives_Type())
pdnPppLinkStatusTotalSentKeepAlives.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalSentKeepAlives.setStatus(_A)
_PdnPppLinkStatusTotalReceivedKeepAlives_Type=Counter32
_PdnPppLinkStatusTotalReceivedKeepAlives_Object=MibTableColumn
pdnPppLinkStatusTotalReceivedKeepAlives=_PdnPppLinkStatusTotalReceivedKeepAlives_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,28),_PdnPppLinkStatusTotalReceivedKeepAlives_Type())
pdnPppLinkStatusTotalReceivedKeepAlives.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalReceivedKeepAlives.setStatus(_A)
_PdnPppLinkStatusTotalEchoRequestsTimeOuts_Type=Counter32
_PdnPppLinkStatusTotalEchoRequestsTimeOuts_Object=MibTableColumn
pdnPppLinkStatusTotalEchoRequestsTimeOuts=_PdnPppLinkStatusTotalEchoRequestsTimeOuts_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,29),_PdnPppLinkStatusTotalEchoRequestsTimeOuts_Type())
pdnPppLinkStatusTotalEchoRequestsTimeOuts.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalEchoRequestsTimeOuts.setStatus(_A)
_PdnPppLinkStatusTotalEchoRequestsBadData_Type=Counter32
_PdnPppLinkStatusTotalEchoRequestsBadData_Object=MibTableColumn
pdnPppLinkStatusTotalEchoRequestsBadData=_PdnPppLinkStatusTotalEchoRequestsBadData_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,30),_PdnPppLinkStatusTotalEchoRequestsBadData_Type())
pdnPppLinkStatusTotalEchoRequestsBadData.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalEchoRequestsBadData.setStatus(_A)
_PdnPppLinkStatusTotalEchoRequestsPassed_Type=Counter32
_PdnPppLinkStatusTotalEchoRequestsPassed_Object=MibTableColumn
pdnPppLinkStatusTotalEchoRequestsPassed=_PdnPppLinkStatusTotalEchoRequestsPassed_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,31),_PdnPppLinkStatusTotalEchoRequestsPassed_Type())
pdnPppLinkStatusTotalEchoRequestsPassed.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalEchoRequestsPassed.setStatus(_A)
_PdnPppLinkStatusTotalKeepAlivesLost_Type=Counter32
_PdnPppLinkStatusTotalKeepAlivesLost_Object=MibTableColumn
pdnPppLinkStatusTotalKeepAlivesLost=_PdnPppLinkStatusTotalKeepAlivesLost_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,32),_PdnPppLinkStatusTotalKeepAlivesLost_Type())
pdnPppLinkStatusTotalKeepAlivesLost.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalKeepAlivesLost.setStatus(_A)
_PdnPppLinkStatusTotalTerminates_Type=Counter32
_PdnPppLinkStatusTotalTerminates_Object=MibTableColumn
pdnPppLinkStatusTotalTerminates=_PdnPppLinkStatusTotalTerminates_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,1,1,33),_PdnPppLinkStatusTotalTerminates_Type())
pdnPppLinkStatusTotalTerminates.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkStatusTotalTerminates.setStatus(_A)
_PdnPppLinkConfigExtTable_Object=MibTable
pdnPppLinkConfigExtTable=_PdnPppLinkConfigExtTable_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,2))
if mibBuilder.loadTexts:pdnPppLinkConfigExtTable.setStatus(_A)
_PdnPppLinkConfigExtEntry_Object=MibTableRow
pdnPppLinkConfigExtEntry=_PdnPppLinkConfigExtEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,2,1))
if mibBuilder.loadTexts:pdnPppLinkConfigExtEntry.setStatus(_A)
_PdnPppLinkConfigPFC_Type=SwitchState
_PdnPppLinkConfigPFC_Object=MibTableColumn
pdnPppLinkConfigPFC=_PdnPppLinkConfigPFC_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,2,1,1),_PdnPppLinkConfigPFC_Type())
pdnPppLinkConfigPFC.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnPppLinkConfigPFC.setStatus(_A)
_PdnPppLinkConfigACFC_Type=SwitchState
_PdnPppLinkConfigACFC_Object=MibTableColumn
pdnPppLinkConfigACFC=_PdnPppLinkConfigACFC_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,2,1,2),_PdnPppLinkConfigACFC_Type())
pdnPppLinkConfigACFC.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnPppLinkConfigACFC.setStatus(_A)
class _PdnPppLinkConfigKeepAliveQuietTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_PdnPppLinkConfigKeepAliveQuietTime_Type.__name__=_F
_PdnPppLinkConfigKeepAliveQuietTime_Object=MibTableColumn
pdnPppLinkConfigKeepAliveQuietTime=_PdnPppLinkConfigKeepAliveQuietTime_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,2,1,3),_PdnPppLinkConfigKeepAliveQuietTime_Type())
pdnPppLinkConfigKeepAliveQuietTime.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnPppLinkConfigKeepAliveQuietTime.setStatus(_A)
if mibBuilder.loadTexts:pdnPppLinkConfigKeepAliveQuietTime.setUnits(_G)
class _PdnPppLinkConfigKeepAliveTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_PdnPppLinkConfigKeepAliveTimeout_Type.__name__=_F
_PdnPppLinkConfigKeepAliveTimeout_Object=MibTableColumn
pdnPppLinkConfigKeepAliveTimeout=_PdnPppLinkConfigKeepAliveTimeout_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,2,1,4),_PdnPppLinkConfigKeepAliveTimeout_Type())
pdnPppLinkConfigKeepAliveTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnPppLinkConfigKeepAliveTimeout.setStatus(_A)
if mibBuilder.loadTexts:pdnPppLinkConfigKeepAliveTimeout.setUnits(_G)
_PdnPppLinkTestTable_Object=MibTable
pdnPppLinkTestTable=_PdnPppLinkTestTable_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,3))
if mibBuilder.loadTexts:pdnPppLinkTestTable.setStatus(_A)
_PdnPppLinkTestEntry_Object=MibTableRow
pdnPppLinkTestEntry=_PdnPppLinkTestEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,3,1))
pdnPppLinkTestEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:pdnPppLinkTestEntry.setStatus(_A)
class _PdnPppLinkTestSendEchoTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noOp',1),('runTest',2)))
_PdnPppLinkTestSendEchoTest_Type.__name__=_E
_PdnPppLinkTestSendEchoTest_Object=MibTableColumn
pdnPppLinkTestSendEchoTest=_PdnPppLinkTestSendEchoTest_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,3,1,1),_PdnPppLinkTestSendEchoTest_Type())
pdnPppLinkTestSendEchoTest.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnPppLinkTestSendEchoTest.setStatus(_A)
class _PdnPppLinkTestEchoTestTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,300))
_PdnPppLinkTestEchoTestTimeout_Type.__name__=_F
_PdnPppLinkTestEchoTestTimeout_Object=MibTableColumn
pdnPppLinkTestEchoTestTimeout=_PdnPppLinkTestEchoTestTimeout_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,3,1,2),_PdnPppLinkTestEchoTestTimeout_Type())
pdnPppLinkTestEchoTestTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnPppLinkTestEchoTestTimeout.setStatus(_A)
if mibBuilder.loadTexts:pdnPppLinkTestEchoTestTimeout.setUnits(_G)
class _PdnPppLinkTestSendDiscardTest_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noOp',1),('sendDiscard',2)))
_PdnPppLinkTestSendDiscardTest_Type.__name__=_E
_PdnPppLinkTestSendDiscardTest_Object=MibTableColumn
pdnPppLinkTestSendDiscardTest=_PdnPppLinkTestSendDiscardTest_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,3,1,3),_PdnPppLinkTestSendDiscardTest_Type())
pdnPppLinkTestSendDiscardTest.setMaxAccess(_D)
if mibBuilder.loadTexts:pdnPppLinkTestSendDiscardTest.setStatus(_A)
class _PdnPppLinkTestLastEchoTestResults_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('inProgress',2),('success',3),('timedOut',4),('compareFailed',5)))
_PdnPppLinkTestLastEchoTestResults_Type.__name__=_E
_PdnPppLinkTestLastEchoTestResults_Object=MibTableColumn
pdnPppLinkTestLastEchoTestResults=_PdnPppLinkTestLastEchoTestResults_Object((1,3,6,1,4,1,1795,2,24,2,6,28,1,3,1,4),_PdnPppLinkTestLastEchoTestResults_Type())
pdnPppLinkTestLastEchoTestResults.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnPppLinkTestLastEchoTestResults.setStatus(_A)
_PdnPppLcpExtAFNs_ObjectIdentity=ObjectIdentity
pdnPppLcpExtAFNs=_PdnPppLcpExtAFNs_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,28,2))
_PdnPppLcpExtConformance_ObjectIdentity=ObjectIdentity
pdnPppLcpExtConformance=_PdnPppLcpExtConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,28,3))
_PdnPppLcpExtCompliances_ObjectIdentity=ObjectIdentity
pdnPppLcpExtCompliances=_PdnPppLcpExtCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,28,3,1))
_PdnPppLcpExtGroups_ObjectIdentity=ObjectIdentity
pdnPppLcpExtGroups=_PdnPppLcpExtGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,28,3,2))
_PdnPppLcpExtObjGroups_ObjectIdentity=ObjectIdentity
pdnPppLcpExtObjGroups=_PdnPppLcpExtObjGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,28,3,2,1))
_PdnPppLcpExtAfnGroups_ObjectIdentity=ObjectIdentity
pdnPppLcpExtAfnGroups=_PdnPppLcpExtAfnGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,28,3,2,2))
_PdnPppLcpExtNtfyGroups_ObjectIdentity=ObjectIdentity
pdnPppLcpExtNtfyGroups=_PdnPppLcpExtNtfyGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,28,3,2,3))
pppLinkStatusEntry.registerAugmentions((_B,_J))
pdnPppLinkStatusExtEntry.setIndexNames(*pppLinkStatusEntry.getIndexNames())
pppLinkConfigEntry.registerAugmentions((_B,_K))
pdnPppLinkConfigExtEntry.setIndexNames(*pppLinkConfigEntry.getIndexNames())
pdnPppLcpExtStateMachineGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,28,3,2,1,1))
pdnPppLcpExtStateMachineGroup.setObjects((_B,_L))
if mibBuilder.loadTexts:pdnPppLcpExtStateMachineGroup.setStatus(_A)
pdnPppLcpExtEstablishFailedGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,28,3,2,1,2))
pdnPppLcpExtEstablishFailedGroup.setObjects((_B,_M))
if mibBuilder.loadTexts:pdnPppLcpExtEstablishFailedGroup.setStatus(_A)
pdnPppLcpExtMagicNumberGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,28,3,2,1,3))
pdnPppLcpExtMagicNumberGroup.setObjects(*((_B,_N),(_B,_O)))
if mibBuilder.loadTexts:pdnPppLcpExtMagicNumberGroup.setStatus(_A)
pdnPppLcpExtPacketCountersGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,28,3,2,1,4))
pdnPppLcpExtPacketCountersGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:pdnPppLcpExtPacketCountersGroup.setStatus(_A)
pdnPppLcpExtKeepAliveCountersGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,28,3,2,1,5))
pdnPppLcpExtKeepAliveCountersGroup.setObjects(*((_B,_l),(_B,_m),(_B,_n)))
if mibBuilder.loadTexts:pdnPppLcpExtKeepAliveCountersGroup.setStatus(_A)
pdnPppLcpExtPFCGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,28,3,2,1,6))
pdnPppLcpExtPFCGroup.setObjects((_B,_o))
if mibBuilder.loadTexts:pdnPppLcpExtPFCGroup.setStatus(_A)
pdnPppLcpExtACFCGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,28,3,2,1,7))
pdnPppLcpExtACFCGroup.setObjects((_B,_p))
if mibBuilder.loadTexts:pdnPppLcpExtACFCGroup.setStatus(_A)
pdnPppLcpExtKeepAliveConfGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,28,3,2,1,8))
pdnPppLcpExtKeepAliveConfGroup.setObjects(*((_B,_q),(_B,_r)))
if mibBuilder.loadTexts:pdnPppLcpExtKeepAliveConfGroup.setStatus(_A)
pdnPppLcpExtEchoTestGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,28,3,2,1,9))
pdnPppLcpExtEchoTestGroup.setObjects(*((_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x)))
if mibBuilder.loadTexts:pdnPppLcpExtEchoTestGroup.setStatus(_A)
pdnPpppLcpExtDiscardTestGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,28,3,2,1,10))
pdnPpppLcpExtDiscardTestGroup.setObjects((_B,_y))
if mibBuilder.loadTexts:pdnPpppLcpExtDiscardTestGroup.setStatus(_A)
pdnPpppLcpExtLinkStateCounterGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,28,3,2,1,11))
pdnPpppLcpExtLinkStateCounterGroup.setObjects((_B,_z))
if mibBuilder.loadTexts:pdnPpppLcpExtLinkStateCounterGroup.setStatus(_A)
pdnPppLcpExtCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,6,28,3,1,1))
pdnPppLcpExtCompliance.setObjects(*((_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:pdnPppLcpExtCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pdnPppLcpExtMIB':pdnPppLcpExtMIB,'pdnPppLcpExtNotifications':pdnPppLcpExtNotifications,'pdnPppLcpExtObjects':pdnPppLcpExtObjects,'pdnPppLinkStatusExtTable':pdnPppLinkStatusExtTable,_J:pdnPppLinkStatusExtEntry,_L:pdnPppLinkStatusCurrState,_M:pdnPppLinkStatusEstablishFailedReason,_N:pdnPppLinkStatusLocalToRemoteMagicNumber,_O:pdnPppLinkStatusRemoteToLocalMagicNumber,_P:pdnPppLinkStatusTotalSentConfigRequests,_Q:pdnPppLinkStatusTotalReceivedConfigRequests,_R:pdnPppLinkStatusTotalSentConfigAcks,_S:pdnPppLinkStatusTotalReceivedConfigAcks,_T:pdnPppLinkStatusTotalSentConfigNaks,_U:pdnPppLinkStatusTotalReceivedConfigNaks,_V:pdnPppLinkStatusTotalSentConfigRejects,_W:pdnPppLinkStatusTotalReceivedConfigRejects,_X:pdnPppLinkStatusTotalSentTerminateRequests,_Y:pdnPppLinkStatusTotalReceivedTerminateRequests,_Z:pdnPppLinkStatusTotalSentTerminateAcks,_a:pdnPppLinkStatusTotalReceivedTerminateAcks,_b:pdnPppLinkStatusTotalSentCodeRejects,_c:pdnPppLinkStatusTotalReceivedCodeRejects,_d:pdnPppLinkStatusTotalSentProtocolRejects,_e:pdnPppLinkStatusTotalReceivedProtocolRejects,_f:pdnPppLinkStatusTotalSentEchoRequests,_g:pdnPppLinkStatusTotalReceivedEchoRequests,_h:pdnPppLinkStatusTotalSentEchoReplies,_i:pdnPppLinkStatusTotalReceivedEchoReplies,_j:pdnPppLinkStatusTotalSentDiscardRequests,_k:pdnPppLinkStatusTotalReceivedDiscardRequests,_l:pdnPppLinkStatusTotalSentKeepAlives,_m:pdnPppLinkStatusTotalReceivedKeepAlives,_v:pdnPppLinkStatusTotalEchoRequestsTimeOuts,_w:pdnPppLinkStatusTotalEchoRequestsBadData,_x:pdnPppLinkStatusTotalEchoRequestsPassed,_n:pdnPppLinkStatusTotalKeepAlivesLost,_z:pdnPppLinkStatusTotalTerminates,'pdnPppLinkConfigExtTable':pdnPppLinkConfigExtTable,_K:pdnPppLinkConfigExtEntry,_o:pdnPppLinkConfigPFC,_p:pdnPppLinkConfigACFC,_q:pdnPppLinkConfigKeepAliveQuietTime,_r:pdnPppLinkConfigKeepAliveTimeout,'pdnPppLinkTestTable':pdnPppLinkTestTable,'pdnPppLinkTestEntry':pdnPppLinkTestEntry,_s:pdnPppLinkTestSendEchoTest,_t:pdnPppLinkTestEchoTestTimeout,_y:pdnPppLinkTestSendDiscardTest,_u:pdnPppLinkTestLastEchoTestResults,'pdnPppLcpExtAFNs':pdnPppLcpExtAFNs,'pdnPppLcpExtConformance':pdnPppLcpExtConformance,'pdnPppLcpExtCompliances':pdnPppLcpExtCompliances,'pdnPppLcpExtCompliance':pdnPppLcpExtCompliance,'pdnPppLcpExtGroups':pdnPppLcpExtGroups,'pdnPppLcpExtObjGroups':pdnPppLcpExtObjGroups,_A0:pdnPppLcpExtStateMachineGroup,_A1:pdnPppLcpExtEstablishFailedGroup,_A2:pdnPppLcpExtMagicNumberGroup,_A3:pdnPppLcpExtPacketCountersGroup,_A4:pdnPppLcpExtKeepAliveCountersGroup,_A5:pdnPppLcpExtPFCGroup,_A6:pdnPppLcpExtACFCGroup,_A7:pdnPppLcpExtKeepAliveConfGroup,_A8:pdnPppLcpExtEchoTestGroup,_A9:pdnPpppLcpExtDiscardTestGroup,_AA:pdnPpppLcpExtLinkStateCounterGroup,'pdnPppLcpExtAfnGroups':pdnPppLcpExtAfnGroups,'pdnPppLcpExtNtfyGroups':pdnPppLcpExtNtfyGroups})