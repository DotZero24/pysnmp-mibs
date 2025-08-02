_B7='tmnxBierV19v0Group'
_B6='tmnxBierOperStateGroup'
_B5='tmnxBierNotificationV16v0Group'
_B4='tmnxBierV16v0Group'
_B3='vRtrBierUnsupportedNhop'
_B2='vRtrBierSubDomainMismatch'
_B1='vRtrBierMtMismatch'
_B0='vRtrBierBfrIdCollision'
_A_='vRtrBierTunnelIsInBand'
_Az='vRtrBierTemplateOperState'
_Ay='vRtrBierGeneralOperState'
_Ax='vRtrBierStatsBfrIdDuplicate'
_Aw='vRtrBierStatsUnsupIpv6Routes'
_Av='vRtrBierStatsMultiTopoMismatch'
_Au='vRtrBierStatsSdBslMismatch'
_At='vRtrBierStatsDiscardNonFp4Nhop'
_As='vRtrBierStatsDiscardNonNtwIfNhop'
_Ar='vRtrBierStatsDiscardTunnelNhop'
_Aq='vRtrBierStatsRxInvalidMplsInfo'
_Ap='vRtrBierStatsRxInvalidEncapInfo'
_Ao='vRtrBierStatsRxInvalidBfrInfo'
_An='vRtrBierStatsRxInvalidBierInfo'
_Am='vRtrBierStatsValidNbrNextHops'
_Al='vRtrBierStatsTotalValidRoutes'
_Ak='vRtrBierStatsTotalLearntRoutes'
_Aj='vRtrBierTxTunnelLeafBfrID'
_Ai='vRtrBierTxTunnelPtaMplsLabel'
_Ah='vRtrBierTxTunnelPtaSubDomain'
_Ag='vRtrBierTxTunnelPtaBfrId'
_Af='vRtrBierTxTunnelPtaPrefix'
_Ae='vRtrBierTxTunnelPtaPrefixType'
_Ad='vRtrBierTxTunnelOperState'
_Ac='vRtrBierTxTunnelMvpnId'
_Ab='vRtrBierTunnelLastOperDownReason'
_Aa='vRtrBierTunnelNumLeaves'
_AZ='vRtrBierTunnelOperState'
_AY='vRtrBierTunnelBfrId'
_AX='vRtrBierTunnelMplsLabel'
_AW='vRtrBierTunnelSubDomain'
_AV='vRtrBierTunnelPrefix'
_AU='vRtrBierTunnelPrefixType'
_AT='vRtrBierTunnelType'
_AS='vRtrBierRoutingLastUpdated'
_AR='vRtrBierRoutingBfrId'
_AQ='vRtrBierRoutingNbrPrefix'
_AP='vRtrBierRoutingNbrPrefixType'
_AO='vRtrBierForwardingMplsLabel'
_AN='vRtrBierForwardingBitMask'
_AM='vRtrBierForwardingNbrPrefix'
_AL='vRtrBierForwardingNbrPrefixType'
_AK='vRtrBierDatabaseMplsLabelTotal'
_AJ='vRtrBierDatabaseMplsLabelEnd'
_AI='vRtrBierDatabaseMplsLabelStart'
_AH='vRtrBierDatabaseMT'
_AG='vRtrBierDatabaseBfrId'
_AF='vRtrBierDatabasePrefix'
_AE='vRtrBierDatabasePrefixType'
_AD='vRtrBierDatabaseBitStringLen'
_AC='vRtrBierSubDomainRowLastChange'
_AB='vRtrBierSubDomainRowStatus'
_AA='vRtrBierSubDomainMT'
_A9='vRtrBierSubDomainBfrId'
_A8='vRtrBierSubDomainPrefix'
_A7='vRtrBierSubDomainPrefixType'
_A6='vRtrBierSubDomainTableLstChanged'
_A5='vRtrBierTemplateRowLastChange'
_A4='vRtrBierTemplateAdminState'
_A3='vRtrBierTemplateRowStatus'
_A2='vRtrBierTemplateTableLastChanged'
_A1='vRtrBierGeneralRowLastChange'
_A0='vRtrBierGeneralAdminState'
_z='vRtrBierGeneralRowStatus'
_y='vRtrBierGeneralTableLastChanged'
_x='vRtrBierTxTunnelLeafPrefix'
_w='vRtrBierTxTunnelLeafPrefixType'
_v='vRtrBierRoutingDestPrefix'
_u='vRtrBierRoutingDestPrefixType'
_t='vRtrBierRoutingNhopIfIndex'
_s='vRtrBierRoutingNhopPrefix'
_r='vRtrBierRoutingNhopPrefixType'
_q='vRtrBierRoutingBitStringLen'
_p='vRtrBierRoutingSubDomainId'
_o='vRtrBierForwardingBierSetId'
_n='vRtrBierForwardingNhopIfIndex'
_m='vRtrBierForwardingNhopPrefix'
_l='vRtrBierForwardingNhopPrefixType'
_k='vRtrBierForwardingBitStringLen'
_j='vRtrBierForwardingSubDomainId'
_i='vRtrBierDatabaseSubDomainId'
_h='TmnxBierMultiTopology'
_g='vRtrBierSubDomainEnd'
_f='vRtrBierSubDomainStart'
_e='TmnxLongDisplayString'
_d='vRtrBierUnsupportedNhopState'
_c='vRtrBierNextHopeType'
_b='vRtrBierNextHopAddress'
_a='vRtrBierNextHopAddrType'
_Z='vRtrBierPrefix2Address'
_Y='vRtrBierPrefix2AddrType'
_X='vRtrBierNotifyRecvMTId'
_W='vRtrBierNotifyMTId'
_V='vRtrBierNotifyBfrId'
_U='vRtrBierNotifyRecvSubDomainId'
_T='TmnxOperState'
_S='TmnxAdminState'
_R='Integer32'
_Q='vRtrBierPrefix1Address'
_P='vRtrBierPrefix1AddrType'
_O='vRtrIfIndex'
_N='Unsigned32'
_M='vRtrBierNotifyBsl'
_L='vRtrBierNotifySubDomainId'
_K='vRtrBierTemplateName'
_J='InetAddressType'
_I='read-create'
_H='vRtrID'
_G='accessible-for-notify'
_F='InetAddress'
_E='TIMETRA-VRTR-MIB'
_D='not-accessible'
_C='read-only'
_B='TIMETRA-BIER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB',_F,_J)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_R,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
timetraSRMIBModules,tmnxSRConfs,tmnxSRNotifyPrefix,tmnxSRObjs=mibBuilder.importSymbols('TIMETRA-GLOBAL-MIB','timetraSRMIBModules','tmnxSRConfs','tmnxSRNotifyPrefix','tmnxSRObjs')
TNamedItem,TmnxAdminState,TmnxLongDisplayString,TmnxOperState=mibBuilder.importSymbols('TIMETRA-TC-MIB','TNamedItem',_S,_e,_T)
vRtrID,vRtrIfIndex=mibBuilder.importSymbols(_E,_H,_O)
timetraBierMIBModule=ModuleIdentity((1,3,6,1,4,1,6527,1,1,3,123))
if mibBuilder.loadTexts:timetraBierMIBModule.setRevisions(('2018-01-01 00:00',))
class TmnxBierMultiTopology(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,3,4)));namedValues=NamedValues(*(('ipv4-unicast',0),('ipv6-unicast',2),('ipv4-multicast',3),('ipv6-multicast',4)))
_TmnxBierConformance_ObjectIdentity=ObjectIdentity
tmnxBierConformance=_TmnxBierConformance_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,123))
_TmnxBierCompliances_ObjectIdentity=ObjectIdentity
tmnxBierCompliances=_TmnxBierCompliances_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,123,1))
_TmnxBierGroups_ObjectIdentity=ObjectIdentity
tmnxBierGroups=_TmnxBierGroups_ObjectIdentity((1,3,6,1,4,1,6527,3,1,1,123,2))
_TmnxBierObjs_ObjectIdentity=ObjectIdentity
tmnxBierObjs=_TmnxBierObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,123))
_VRtrBierGeneralTableLastChanged_Type=TimeStamp
_VRtrBierGeneralTableLastChanged_Object=MibScalar
vRtrBierGeneralTableLastChanged=_VRtrBierGeneralTableLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,123,1),_VRtrBierGeneralTableLastChanged_Type())
vRtrBierGeneralTableLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierGeneralTableLastChanged.setStatus(_A)
_VRtrBierGeneralTable_Object=MibTable
vRtrBierGeneralTable=_VRtrBierGeneralTable_Object((1,3,6,1,4,1,6527,3,1,2,123,2))
if mibBuilder.loadTexts:vRtrBierGeneralTable.setStatus(_A)
_VRtrBierGeneralEntry_Object=MibTableRow
vRtrBierGeneralEntry=_VRtrBierGeneralEntry_Object((1,3,6,1,4,1,6527,3,1,2,123,2,1))
vRtrBierGeneralEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:vRtrBierGeneralEntry.setStatus(_A)
_VRtrBierGeneralRowStatus_Type=RowStatus
_VRtrBierGeneralRowStatus_Object=MibTableColumn
vRtrBierGeneralRowStatus=_VRtrBierGeneralRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,123,2,1,1),_VRtrBierGeneralRowStatus_Type())
vRtrBierGeneralRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:vRtrBierGeneralRowStatus.setStatus(_A)
class _VRtrBierGeneralAdminState_Type(TmnxAdminState):defaultValue=3
_VRtrBierGeneralAdminState_Type.__name__=_S
_VRtrBierGeneralAdminState_Object=MibTableColumn
vRtrBierGeneralAdminState=_VRtrBierGeneralAdminState_Object((1,3,6,1,4,1,6527,3,1,2,123,2,1,2),_VRtrBierGeneralAdminState_Type())
vRtrBierGeneralAdminState.setMaxAccess(_I)
if mibBuilder.loadTexts:vRtrBierGeneralAdminState.setStatus(_A)
_VRtrBierGeneralRowLastChange_Type=TimeStamp
_VRtrBierGeneralRowLastChange_Object=MibTableColumn
vRtrBierGeneralRowLastChange=_VRtrBierGeneralRowLastChange_Object((1,3,6,1,4,1,6527,3,1,2,123,2,1,3),_VRtrBierGeneralRowLastChange_Type())
vRtrBierGeneralRowLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierGeneralRowLastChange.setStatus(_A)
_VRtrBierTemplateTableLastChanged_Type=TimeStamp
_VRtrBierTemplateTableLastChanged_Object=MibScalar
vRtrBierTemplateTableLastChanged=_VRtrBierTemplateTableLastChanged_Object((1,3,6,1,4,1,6527,3,1,2,123,3),_VRtrBierTemplateTableLastChanged_Type())
vRtrBierTemplateTableLastChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierTemplateTableLastChanged.setStatus(_A)
_VRtrBierTemplateTable_Object=MibTable
vRtrBierTemplateTable=_VRtrBierTemplateTable_Object((1,3,6,1,4,1,6527,3,1,2,123,4))
if mibBuilder.loadTexts:vRtrBierTemplateTable.setStatus(_A)
_VRtrBierTemplateEntry_Object=MibTableRow
vRtrBierTemplateEntry=_VRtrBierTemplateEntry_Object((1,3,6,1,4,1,6527,3,1,2,123,4,1))
vRtrBierTemplateEntry.setIndexNames((0,_E,_H),(0,_B,_K))
if mibBuilder.loadTexts:vRtrBierTemplateEntry.setStatus(_A)
_VRtrBierTemplateName_Type=TNamedItem
_VRtrBierTemplateName_Object=MibTableColumn
vRtrBierTemplateName=_VRtrBierTemplateName_Object((1,3,6,1,4,1,6527,3,1,2,123,4,1,1),_VRtrBierTemplateName_Type())
vRtrBierTemplateName.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrBierTemplateName.setStatus(_A)
_VRtrBierTemplateRowStatus_Type=RowStatus
_VRtrBierTemplateRowStatus_Object=MibTableColumn
vRtrBierTemplateRowStatus=_VRtrBierTemplateRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,123,4,1,2),_VRtrBierTemplateRowStatus_Type())
vRtrBierTemplateRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:vRtrBierTemplateRowStatus.setStatus(_A)
class _VRtrBierTemplateAdminState_Type(TmnxAdminState):defaultValue=3
_VRtrBierTemplateAdminState_Type.__name__=_S
_VRtrBierTemplateAdminState_Object=MibTableColumn
vRtrBierTemplateAdminState=_VRtrBierTemplateAdminState_Object((1,3,6,1,4,1,6527,3,1,2,123,4,1,3),_VRtrBierTemplateAdminState_Type())
vRtrBierTemplateAdminState.setMaxAccess(_I)
if mibBuilder.loadTexts:vRtrBierTemplateAdminState.setStatus(_A)
_VRtrBierTemplateRowLastChange_Type=TimeStamp
_VRtrBierTemplateRowLastChange_Object=MibTableColumn
vRtrBierTemplateRowLastChange=_VRtrBierTemplateRowLastChange_Object((1,3,6,1,4,1,6527,3,1,2,123,4,1,4),_VRtrBierTemplateRowLastChange_Type())
vRtrBierTemplateRowLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierTemplateRowLastChange.setStatus(_A)
_VRtrBierSubDomainTableLstChanged_Type=TimeStamp
_VRtrBierSubDomainTableLstChanged_Object=MibScalar
vRtrBierSubDomainTableLstChanged=_VRtrBierSubDomainTableLstChanged_Object((1,3,6,1,4,1,6527,3,1,2,123,5),_VRtrBierSubDomainTableLstChanged_Type())
vRtrBierSubDomainTableLstChanged.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierSubDomainTableLstChanged.setStatus(_A)
_VRtrBierSubDomainTable_Object=MibTable
vRtrBierSubDomainTable=_VRtrBierSubDomainTable_Object((1,3,6,1,4,1,6527,3,1,2,123,6))
if mibBuilder.loadTexts:vRtrBierSubDomainTable.setStatus(_A)
_VRtrBierSubDomainEntry_Object=MibTableRow
vRtrBierSubDomainEntry=_VRtrBierSubDomainEntry_Object((1,3,6,1,4,1,6527,3,1,2,123,6,1))
vRtrBierSubDomainEntry.setIndexNames((0,_E,_H),(0,_B,_K),(0,_B,_f),(0,_B,_g))
if mibBuilder.loadTexts:vRtrBierSubDomainEntry.setStatus(_A)
class _VRtrBierSubDomainStart_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VRtrBierSubDomainStart_Type.__name__=_N
_VRtrBierSubDomainStart_Object=MibTableColumn
vRtrBierSubDomainStart=_VRtrBierSubDomainStart_Object((1,3,6,1,4,1,6527,3,1,2,123,6,1,1),_VRtrBierSubDomainStart_Type())
vRtrBierSubDomainStart.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrBierSubDomainStart.setStatus(_A)
class _VRtrBierSubDomainEnd_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VRtrBierSubDomainEnd_Type.__name__=_N
_VRtrBierSubDomainEnd_Object=MibTableColumn
vRtrBierSubDomainEnd=_VRtrBierSubDomainEnd_Object((1,3,6,1,4,1,6527,3,1,2,123,6,1,2),_VRtrBierSubDomainEnd_Type())
vRtrBierSubDomainEnd.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrBierSubDomainEnd.setStatus(_A)
class _VRtrBierSubDomainPrefixType_Type(InetAddressType):defaultValue=0
_VRtrBierSubDomainPrefixType_Type.__name__=_J
_VRtrBierSubDomainPrefixType_Object=MibTableColumn
vRtrBierSubDomainPrefixType=_VRtrBierSubDomainPrefixType_Object((1,3,6,1,4,1,6527,3,1,2,123,6,1,3),_VRtrBierSubDomainPrefixType_Type())
vRtrBierSubDomainPrefixType.setMaxAccess(_I)
if mibBuilder.loadTexts:vRtrBierSubDomainPrefixType.setStatus(_A)
class _VRtrBierSubDomainPrefix_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_VRtrBierSubDomainPrefix_Type.__name__=_F
_VRtrBierSubDomainPrefix_Object=MibTableColumn
vRtrBierSubDomainPrefix=_VRtrBierSubDomainPrefix_Object((1,3,6,1,4,1,6527,3,1,2,123,6,1,4),_VRtrBierSubDomainPrefix_Type())
vRtrBierSubDomainPrefix.setMaxAccess(_I)
if mibBuilder.loadTexts:vRtrBierSubDomainPrefix.setStatus(_A)
class _VRtrBierSubDomainBfrId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4096))
_VRtrBierSubDomainBfrId_Type.__name__=_N
_VRtrBierSubDomainBfrId_Object=MibTableColumn
vRtrBierSubDomainBfrId=_VRtrBierSubDomainBfrId_Object((1,3,6,1,4,1,6527,3,1,2,123,6,1,5),_VRtrBierSubDomainBfrId_Type())
vRtrBierSubDomainBfrId.setMaxAccess(_I)
if mibBuilder.loadTexts:vRtrBierSubDomainBfrId.setStatus(_A)
class _VRtrBierSubDomainMT_Type(TmnxBierMultiTopology):defaultValue=0
_VRtrBierSubDomainMT_Type.__name__=_h
_VRtrBierSubDomainMT_Object=MibTableColumn
vRtrBierSubDomainMT=_VRtrBierSubDomainMT_Object((1,3,6,1,4,1,6527,3,1,2,123,6,1,6),_VRtrBierSubDomainMT_Type())
vRtrBierSubDomainMT.setMaxAccess(_I)
if mibBuilder.loadTexts:vRtrBierSubDomainMT.setStatus(_A)
_VRtrBierSubDomainRowStatus_Type=RowStatus
_VRtrBierSubDomainRowStatus_Object=MibTableColumn
vRtrBierSubDomainRowStatus=_VRtrBierSubDomainRowStatus_Object((1,3,6,1,4,1,6527,3,1,2,123,6,1,7),_VRtrBierSubDomainRowStatus_Type())
vRtrBierSubDomainRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:vRtrBierSubDomainRowStatus.setStatus(_A)
_VRtrBierSubDomainRowLastChange_Type=TimeStamp
_VRtrBierSubDomainRowLastChange_Object=MibTableColumn
vRtrBierSubDomainRowLastChange=_VRtrBierSubDomainRowLastChange_Object((1,3,6,1,4,1,6527,3,1,2,123,6,1,8),_VRtrBierSubDomainRowLastChange_Type())
vRtrBierSubDomainRowLastChange.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierSubDomainRowLastChange.setStatus(_A)
_VRtrBierDatabaseTable_Object=MibTable
vRtrBierDatabaseTable=_VRtrBierDatabaseTable_Object((1,3,6,1,4,1,6527,3,1,2,123,7))
if mibBuilder.loadTexts:vRtrBierDatabaseTable.setStatus(_A)
_VRtrBierDatabaseEntry_Object=MibTableRow
vRtrBierDatabaseEntry=_VRtrBierDatabaseEntry_Object((1,3,6,1,4,1,6527,3,1,2,123,7,1))
vRtrBierDatabaseEntry.setIndexNames((0,_E,_H),(0,_B,_K),(0,_B,_i))
if mibBuilder.loadTexts:vRtrBierDatabaseEntry.setStatus(_A)
_VRtrBierDatabaseSubDomainId_Type=Unsigned32
_VRtrBierDatabaseSubDomainId_Object=MibTableColumn
vRtrBierDatabaseSubDomainId=_VRtrBierDatabaseSubDomainId_Object((1,3,6,1,4,1,6527,3,1,2,123,7,1,1),_VRtrBierDatabaseSubDomainId_Type())
vRtrBierDatabaseSubDomainId.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrBierDatabaseSubDomainId.setStatus(_A)
_VRtrBierDatabaseBitStringLen_Type=Unsigned32
_VRtrBierDatabaseBitStringLen_Object=MibTableColumn
vRtrBierDatabaseBitStringLen=_VRtrBierDatabaseBitStringLen_Object((1,3,6,1,4,1,6527,3,1,2,123,7,1,2),_VRtrBierDatabaseBitStringLen_Type())
vRtrBierDatabaseBitStringLen.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierDatabaseBitStringLen.setStatus(_A)
class _VRtrBierDatabasePrefixType_Type(InetAddressType):defaultValue=0
_VRtrBierDatabasePrefixType_Type.__name__=_J
_VRtrBierDatabasePrefixType_Object=MibTableColumn
vRtrBierDatabasePrefixType=_VRtrBierDatabasePrefixType_Object((1,3,6,1,4,1,6527,3,1,2,123,7,1,3),_VRtrBierDatabasePrefixType_Type())
vRtrBierDatabasePrefixType.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierDatabasePrefixType.setStatus(_A)
class _VRtrBierDatabasePrefix_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_VRtrBierDatabasePrefix_Type.__name__=_F
_VRtrBierDatabasePrefix_Object=MibTableColumn
vRtrBierDatabasePrefix=_VRtrBierDatabasePrefix_Object((1,3,6,1,4,1,6527,3,1,2,123,7,1,4),_VRtrBierDatabasePrefix_Type())
vRtrBierDatabasePrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierDatabasePrefix.setStatus(_A)
_VRtrBierDatabaseBfrId_Type=Unsigned32
_VRtrBierDatabaseBfrId_Object=MibTableColumn
vRtrBierDatabaseBfrId=_VRtrBierDatabaseBfrId_Object((1,3,6,1,4,1,6527,3,1,2,123,7,1,5),_VRtrBierDatabaseBfrId_Type())
vRtrBierDatabaseBfrId.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierDatabaseBfrId.setStatus(_A)
_VRtrBierDatabaseMT_Type=TmnxBierMultiTopology
_VRtrBierDatabaseMT_Object=MibTableColumn
vRtrBierDatabaseMT=_VRtrBierDatabaseMT_Object((1,3,6,1,4,1,6527,3,1,2,123,7,1,6),_VRtrBierDatabaseMT_Type())
vRtrBierDatabaseMT.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierDatabaseMT.setStatus(_A)
_VRtrBierDatabaseMplsLabelStart_Type=Unsigned32
_VRtrBierDatabaseMplsLabelStart_Object=MibTableColumn
vRtrBierDatabaseMplsLabelStart=_VRtrBierDatabaseMplsLabelStart_Object((1,3,6,1,4,1,6527,3,1,2,123,7,1,7),_VRtrBierDatabaseMplsLabelStart_Type())
vRtrBierDatabaseMplsLabelStart.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierDatabaseMplsLabelStart.setStatus(_A)
_VRtrBierDatabaseMplsLabelEnd_Type=Unsigned32
_VRtrBierDatabaseMplsLabelEnd_Object=MibTableColumn
vRtrBierDatabaseMplsLabelEnd=_VRtrBierDatabaseMplsLabelEnd_Object((1,3,6,1,4,1,6527,3,1,2,123,7,1,8),_VRtrBierDatabaseMplsLabelEnd_Type())
vRtrBierDatabaseMplsLabelEnd.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierDatabaseMplsLabelEnd.setStatus(_A)
_VRtrBierDatabaseMplsLabelTotal_Type=Unsigned32
_VRtrBierDatabaseMplsLabelTotal_Object=MibTableColumn
vRtrBierDatabaseMplsLabelTotal=_VRtrBierDatabaseMplsLabelTotal_Object((1,3,6,1,4,1,6527,3,1,2,123,7,1,9),_VRtrBierDatabaseMplsLabelTotal_Type())
vRtrBierDatabaseMplsLabelTotal.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierDatabaseMplsLabelTotal.setStatus(_A)
_VRtrBierForwardingTable_Object=MibTable
vRtrBierForwardingTable=_VRtrBierForwardingTable_Object((1,3,6,1,4,1,6527,3,1,2,123,8))
if mibBuilder.loadTexts:vRtrBierForwardingTable.setStatus(_A)
_VRtrBierForwardingEntry_Object=MibTableRow
vRtrBierForwardingEntry=_VRtrBierForwardingEntry_Object((1,3,6,1,4,1,6527,3,1,2,123,8,1))
vRtrBierForwardingEntry.setIndexNames((0,_E,_H),(0,_B,_j),(0,_B,_k),(0,_B,_l),(0,_B,_m),(0,_B,_n),(0,_B,_o))
if mibBuilder.loadTexts:vRtrBierForwardingEntry.setStatus(_A)
_VRtrBierForwardingSubDomainId_Type=Unsigned32
_VRtrBierForwardingSubDomainId_Object=MibTableColumn
vRtrBierForwardingSubDomainId=_VRtrBierForwardingSubDomainId_Object((1,3,6,1,4,1,6527,3,1,2,123,8,1,1),_VRtrBierForwardingSubDomainId_Type())
vRtrBierForwardingSubDomainId.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrBierForwardingSubDomainId.setStatus(_A)
_VRtrBierForwardingBitStringLen_Type=Unsigned32
_VRtrBierForwardingBitStringLen_Object=MibTableColumn
vRtrBierForwardingBitStringLen=_VRtrBierForwardingBitStringLen_Object((1,3,6,1,4,1,6527,3,1,2,123,8,1,2),_VRtrBierForwardingBitStringLen_Type())
vRtrBierForwardingBitStringLen.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrBierForwardingBitStringLen.setStatus(_A)
class _VRtrBierForwardingNhopPrefixType_Type(InetAddressType):defaultValue=0
_VRtrBierForwardingNhopPrefixType_Type.__name__=_J
_VRtrBierForwardingNhopPrefixType_Object=MibTableColumn
vRtrBierForwardingNhopPrefixType=_VRtrBierForwardingNhopPrefixType_Object((1,3,6,1,4,1,6527,3,1,2,123,8,1,3),_VRtrBierForwardingNhopPrefixType_Type())
vRtrBierForwardingNhopPrefixType.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrBierForwardingNhopPrefixType.setStatus(_A)
class _VRtrBierForwardingNhopPrefix_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_VRtrBierForwardingNhopPrefix_Type.__name__=_F
_VRtrBierForwardingNhopPrefix_Object=MibTableColumn
vRtrBierForwardingNhopPrefix=_VRtrBierForwardingNhopPrefix_Object((1,3,6,1,4,1,6527,3,1,2,123,8,1,4),_VRtrBierForwardingNhopPrefix_Type())
vRtrBierForwardingNhopPrefix.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrBierForwardingNhopPrefix.setStatus(_A)
_VRtrBierForwardingNhopIfIndex_Type=Unsigned32
_VRtrBierForwardingNhopIfIndex_Object=MibTableColumn
vRtrBierForwardingNhopIfIndex=_VRtrBierForwardingNhopIfIndex_Object((1,3,6,1,4,1,6527,3,1,2,123,8,1,5),_VRtrBierForwardingNhopIfIndex_Type())
vRtrBierForwardingNhopIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrBierForwardingNhopIfIndex.setStatus(_A)
_VRtrBierForwardingBierSetId_Type=Unsigned32
_VRtrBierForwardingBierSetId_Object=MibTableColumn
vRtrBierForwardingBierSetId=_VRtrBierForwardingBierSetId_Object((1,3,6,1,4,1,6527,3,1,2,123,8,1,6),_VRtrBierForwardingBierSetId_Type())
vRtrBierForwardingBierSetId.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrBierForwardingBierSetId.setStatus(_A)
_VRtrBierForwardingNbrPrefixType_Type=InetAddressType
_VRtrBierForwardingNbrPrefixType_Object=MibTableColumn
vRtrBierForwardingNbrPrefixType=_VRtrBierForwardingNbrPrefixType_Object((1,3,6,1,4,1,6527,3,1,2,123,8,1,7),_VRtrBierForwardingNbrPrefixType_Type())
vRtrBierForwardingNbrPrefixType.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierForwardingNbrPrefixType.setStatus(_A)
class _VRtrBierForwardingNbrPrefix_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_VRtrBierForwardingNbrPrefix_Type.__name__=_F
_VRtrBierForwardingNbrPrefix_Object=MibTableColumn
vRtrBierForwardingNbrPrefix=_VRtrBierForwardingNbrPrefix_Object((1,3,6,1,4,1,6527,3,1,2,123,8,1,8),_VRtrBierForwardingNbrPrefix_Type())
vRtrBierForwardingNbrPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierForwardingNbrPrefix.setStatus(_A)
class _VRtrBierForwardingBitMask_Type(TmnxLongDisplayString):subtypeSpec=TmnxLongDisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_VRtrBierForwardingBitMask_Type.__name__=_e
_VRtrBierForwardingBitMask_Object=MibTableColumn
vRtrBierForwardingBitMask=_VRtrBierForwardingBitMask_Object((1,3,6,1,4,1,6527,3,1,2,123,8,1,9),_VRtrBierForwardingBitMask_Type())
vRtrBierForwardingBitMask.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierForwardingBitMask.setStatus(_A)
_VRtrBierForwardingMplsLabel_Type=Unsigned32
_VRtrBierForwardingMplsLabel_Object=MibTableColumn
vRtrBierForwardingMplsLabel=_VRtrBierForwardingMplsLabel_Object((1,3,6,1,4,1,6527,3,1,2,123,8,1,10),_VRtrBierForwardingMplsLabel_Type())
vRtrBierForwardingMplsLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierForwardingMplsLabel.setStatus(_A)
_VRtrBierRoutingTable_Object=MibTable
vRtrBierRoutingTable=_VRtrBierRoutingTable_Object((1,3,6,1,4,1,6527,3,1,2,123,9))
if mibBuilder.loadTexts:vRtrBierRoutingTable.setStatus(_A)
_VRtrBierRoutingEntry_Object=MibTableRow
vRtrBierRoutingEntry=_VRtrBierRoutingEntry_Object((1,3,6,1,4,1,6527,3,1,2,123,9,1))
vRtrBierRoutingEntry.setIndexNames((0,_E,_H),(0,_B,_p),(0,_B,_q),(0,_B,_r),(0,_B,_s),(0,_B,_t),(0,_B,_u),(0,_B,_v))
if mibBuilder.loadTexts:vRtrBierRoutingEntry.setStatus(_A)
_VRtrBierRoutingSubDomainId_Type=Unsigned32
_VRtrBierRoutingSubDomainId_Object=MibTableColumn
vRtrBierRoutingSubDomainId=_VRtrBierRoutingSubDomainId_Object((1,3,6,1,4,1,6527,3,1,2,123,9,1,1),_VRtrBierRoutingSubDomainId_Type())
vRtrBierRoutingSubDomainId.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrBierRoutingSubDomainId.setStatus(_A)
_VRtrBierRoutingBitStringLen_Type=Unsigned32
_VRtrBierRoutingBitStringLen_Object=MibTableColumn
vRtrBierRoutingBitStringLen=_VRtrBierRoutingBitStringLen_Object((1,3,6,1,4,1,6527,3,1,2,123,9,1,2),_VRtrBierRoutingBitStringLen_Type())
vRtrBierRoutingBitStringLen.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrBierRoutingBitStringLen.setStatus(_A)
class _VRtrBierRoutingNhopPrefixType_Type(InetAddressType):defaultValue=0
_VRtrBierRoutingNhopPrefixType_Type.__name__=_J
_VRtrBierRoutingNhopPrefixType_Object=MibTableColumn
vRtrBierRoutingNhopPrefixType=_VRtrBierRoutingNhopPrefixType_Object((1,3,6,1,4,1,6527,3,1,2,123,9,1,3),_VRtrBierRoutingNhopPrefixType_Type())
vRtrBierRoutingNhopPrefixType.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrBierRoutingNhopPrefixType.setStatus(_A)
class _VRtrBierRoutingNhopPrefix_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_VRtrBierRoutingNhopPrefix_Type.__name__=_F
_VRtrBierRoutingNhopPrefix_Object=MibTableColumn
vRtrBierRoutingNhopPrefix=_VRtrBierRoutingNhopPrefix_Object((1,3,6,1,4,1,6527,3,1,2,123,9,1,4),_VRtrBierRoutingNhopPrefix_Type())
vRtrBierRoutingNhopPrefix.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrBierRoutingNhopPrefix.setStatus(_A)
_VRtrBierRoutingNhopIfIndex_Type=Unsigned32
_VRtrBierRoutingNhopIfIndex_Object=MibTableColumn
vRtrBierRoutingNhopIfIndex=_VRtrBierRoutingNhopIfIndex_Object((1,3,6,1,4,1,6527,3,1,2,123,9,1,5),_VRtrBierRoutingNhopIfIndex_Type())
vRtrBierRoutingNhopIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrBierRoutingNhopIfIndex.setStatus(_A)
class _VRtrBierRoutingDestPrefixType_Type(InetAddressType):defaultValue=0
_VRtrBierRoutingDestPrefixType_Type.__name__=_J
_VRtrBierRoutingDestPrefixType_Object=MibTableColumn
vRtrBierRoutingDestPrefixType=_VRtrBierRoutingDestPrefixType_Object((1,3,6,1,4,1,6527,3,1,2,123,9,1,6),_VRtrBierRoutingDestPrefixType_Type())
vRtrBierRoutingDestPrefixType.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrBierRoutingDestPrefixType.setStatus(_A)
class _VRtrBierRoutingDestPrefix_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_VRtrBierRoutingDestPrefix_Type.__name__=_F
_VRtrBierRoutingDestPrefix_Object=MibTableColumn
vRtrBierRoutingDestPrefix=_VRtrBierRoutingDestPrefix_Object((1,3,6,1,4,1,6527,3,1,2,123,9,1,7),_VRtrBierRoutingDestPrefix_Type())
vRtrBierRoutingDestPrefix.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrBierRoutingDestPrefix.setStatus(_A)
_VRtrBierRoutingNbrPrefixType_Type=InetAddressType
_VRtrBierRoutingNbrPrefixType_Object=MibTableColumn
vRtrBierRoutingNbrPrefixType=_VRtrBierRoutingNbrPrefixType_Object((1,3,6,1,4,1,6527,3,1,2,123,9,1,8),_VRtrBierRoutingNbrPrefixType_Type())
vRtrBierRoutingNbrPrefixType.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierRoutingNbrPrefixType.setStatus(_A)
class _VRtrBierRoutingNbrPrefix_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_VRtrBierRoutingNbrPrefix_Type.__name__=_F
_VRtrBierRoutingNbrPrefix_Object=MibTableColumn
vRtrBierRoutingNbrPrefix=_VRtrBierRoutingNbrPrefix_Object((1,3,6,1,4,1,6527,3,1,2,123,9,1,9),_VRtrBierRoutingNbrPrefix_Type())
vRtrBierRoutingNbrPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierRoutingNbrPrefix.setStatus(_A)
_VRtrBierRoutingBfrId_Type=Unsigned32
_VRtrBierRoutingBfrId_Object=MibTableColumn
vRtrBierRoutingBfrId=_VRtrBierRoutingBfrId_Object((1,3,6,1,4,1,6527,3,1,2,123,9,1,10),_VRtrBierRoutingBfrId_Type())
vRtrBierRoutingBfrId.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierRoutingBfrId.setStatus(_A)
_VRtrBierRoutingLastUpdated_Type=TimeStamp
_VRtrBierRoutingLastUpdated_Object=MibTableColumn
vRtrBierRoutingLastUpdated=_VRtrBierRoutingLastUpdated_Object((1,3,6,1,4,1,6527,3,1,2,123,9,1,11),_VRtrBierRoutingLastUpdated_Type())
vRtrBierRoutingLastUpdated.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierRoutingLastUpdated.setStatus(_A)
_VRtrBierTunnelTable_Object=MibTable
vRtrBierTunnelTable=_VRtrBierTunnelTable_Object((1,3,6,1,4,1,6527,3,1,2,123,10))
if mibBuilder.loadTexts:vRtrBierTunnelTable.setStatus(_A)
_VRtrBierTunnelEntry_Object=MibTableRow
vRtrBierTunnelEntry=_VRtrBierTunnelEntry_Object((1,3,6,1,4,1,6527,3,1,2,123,10,1))
vRtrBierTunnelEntry.setIndexNames((0,_E,_H),(0,_E,_O))
if mibBuilder.loadTexts:vRtrBierTunnelEntry.setStatus(_A)
class _VRtrBierTunnelType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('tx',0),('rx',1)))
_VRtrBierTunnelType_Type.__name__=_R
_VRtrBierTunnelType_Object=MibTableColumn
vRtrBierTunnelType=_VRtrBierTunnelType_Object((1,3,6,1,4,1,6527,3,1,2,123,10,1,1),_VRtrBierTunnelType_Type())
vRtrBierTunnelType.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierTunnelType.setStatus(_A)
_VRtrBierTunnelPrefixType_Type=InetAddressType
_VRtrBierTunnelPrefixType_Object=MibTableColumn
vRtrBierTunnelPrefixType=_VRtrBierTunnelPrefixType_Object((1,3,6,1,4,1,6527,3,1,2,123,10,1,2),_VRtrBierTunnelPrefixType_Type())
vRtrBierTunnelPrefixType.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierTunnelPrefixType.setStatus(_A)
class _VRtrBierTunnelPrefix_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_VRtrBierTunnelPrefix_Type.__name__=_F
_VRtrBierTunnelPrefix_Object=MibTableColumn
vRtrBierTunnelPrefix=_VRtrBierTunnelPrefix_Object((1,3,6,1,4,1,6527,3,1,2,123,10,1,3),_VRtrBierTunnelPrefix_Type())
vRtrBierTunnelPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierTunnelPrefix.setStatus(_A)
_VRtrBierTunnelSubDomain_Type=Unsigned32
_VRtrBierTunnelSubDomain_Object=MibTableColumn
vRtrBierTunnelSubDomain=_VRtrBierTunnelSubDomain_Object((1,3,6,1,4,1,6527,3,1,2,123,10,1,4),_VRtrBierTunnelSubDomain_Type())
vRtrBierTunnelSubDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierTunnelSubDomain.setStatus(_A)
_VRtrBierTunnelMplsLabel_Type=Unsigned32
_VRtrBierTunnelMplsLabel_Object=MibTableColumn
vRtrBierTunnelMplsLabel=_VRtrBierTunnelMplsLabel_Object((1,3,6,1,4,1,6527,3,1,2,123,10,1,5),_VRtrBierTunnelMplsLabel_Type())
vRtrBierTunnelMplsLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierTunnelMplsLabel.setStatus(_A)
_VRtrBierTunnelBfrId_Type=Unsigned32
_VRtrBierTunnelBfrId_Object=MibTableColumn
vRtrBierTunnelBfrId=_VRtrBierTunnelBfrId_Object((1,3,6,1,4,1,6527,3,1,2,123,10,1,6),_VRtrBierTunnelBfrId_Type())
vRtrBierTunnelBfrId.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierTunnelBfrId.setStatus(_A)
_VRtrBierTunnelOperState_Type=TmnxAdminState
_VRtrBierTunnelOperState_Object=MibTableColumn
vRtrBierTunnelOperState=_VRtrBierTunnelOperState_Object((1,3,6,1,4,1,6527,3,1,2,123,10,1,7),_VRtrBierTunnelOperState_Type())
vRtrBierTunnelOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierTunnelOperState.setStatus(_A)
_VRtrBierTunnelNumLeaves_Type=Unsigned32
_VRtrBierTunnelNumLeaves_Object=MibTableColumn
vRtrBierTunnelNumLeaves=_VRtrBierTunnelNumLeaves_Object((1,3,6,1,4,1,6527,3,1,2,123,10,1,8),_VRtrBierTunnelNumLeaves_Type())
vRtrBierTunnelNumLeaves.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierTunnelNumLeaves.setStatus(_A)
_VRtrBierTunnelLastOperDownReason_Type=Unsigned32
_VRtrBierTunnelLastOperDownReason_Object=MibTableColumn
vRtrBierTunnelLastOperDownReason=_VRtrBierTunnelLastOperDownReason_Object((1,3,6,1,4,1,6527,3,1,2,123,10,1,9),_VRtrBierTunnelLastOperDownReason_Type())
vRtrBierTunnelLastOperDownReason.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierTunnelLastOperDownReason.setStatus(_A)
_VRtrBierTunnelIsInBand_Type=TruthValue
_VRtrBierTunnelIsInBand_Object=MibTableColumn
vRtrBierTunnelIsInBand=_VRtrBierTunnelIsInBand_Object((1,3,6,1,4,1,6527,3,1,2,123,10,1,10),_VRtrBierTunnelIsInBand_Type())
vRtrBierTunnelIsInBand.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierTunnelIsInBand.setStatus(_A)
_VRtrBierTxTunnelLeafTable_Object=MibTable
vRtrBierTxTunnelLeafTable=_VRtrBierTxTunnelLeafTable_Object((1,3,6,1,4,1,6527,3,1,2,123,11))
if mibBuilder.loadTexts:vRtrBierTxTunnelLeafTable.setStatus(_A)
_VRtrBierTxTunnelLeafEntry_Object=MibTableRow
vRtrBierTxTunnelLeafEntry=_VRtrBierTxTunnelLeafEntry_Object((1,3,6,1,4,1,6527,3,1,2,123,11,1))
vRtrBierTxTunnelLeafEntry.setIndexNames((0,_E,_H),(0,_E,_O),(0,_B,_w),(0,_B,_x))
if mibBuilder.loadTexts:vRtrBierTxTunnelLeafEntry.setStatus(_A)
class _VRtrBierTxTunnelLeafPrefixType_Type(InetAddressType):defaultValue=0
_VRtrBierTxTunnelLeafPrefixType_Type.__name__=_J
_VRtrBierTxTunnelLeafPrefixType_Object=MibTableColumn
vRtrBierTxTunnelLeafPrefixType=_VRtrBierTxTunnelLeafPrefixType_Object((1,3,6,1,4,1,6527,3,1,2,123,11,1,2),_VRtrBierTxTunnelLeafPrefixType_Type())
vRtrBierTxTunnelLeafPrefixType.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrBierTxTunnelLeafPrefixType.setStatus(_A)
class _VRtrBierTxTunnelLeafPrefix_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_VRtrBierTxTunnelLeafPrefix_Type.__name__=_F
_VRtrBierTxTunnelLeafPrefix_Object=MibTableColumn
vRtrBierTxTunnelLeafPrefix=_VRtrBierTxTunnelLeafPrefix_Object((1,3,6,1,4,1,6527,3,1,2,123,11,1,3),_VRtrBierTxTunnelLeafPrefix_Type())
vRtrBierTxTunnelLeafPrefix.setMaxAccess(_D)
if mibBuilder.loadTexts:vRtrBierTxTunnelLeafPrefix.setStatus(_A)
_VRtrBierTxTunnelMvpnId_Type=Unsigned32
_VRtrBierTxTunnelMvpnId_Object=MibTableColumn
vRtrBierTxTunnelMvpnId=_VRtrBierTxTunnelMvpnId_Object((1,3,6,1,4,1,6527,3,1,2,123,11,1,4),_VRtrBierTxTunnelMvpnId_Type())
vRtrBierTxTunnelMvpnId.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierTxTunnelMvpnId.setStatus(_A)
_VRtrBierTxTunnelOperState_Type=TmnxAdminState
_VRtrBierTxTunnelOperState_Object=MibTableColumn
vRtrBierTxTunnelOperState=_VRtrBierTxTunnelOperState_Object((1,3,6,1,4,1,6527,3,1,2,123,11,1,5),_VRtrBierTxTunnelOperState_Type())
vRtrBierTxTunnelOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierTxTunnelOperState.setStatus(_A)
_VRtrBierTxTunnelPtaPrefixType_Type=InetAddressType
_VRtrBierTxTunnelPtaPrefixType_Object=MibTableColumn
vRtrBierTxTunnelPtaPrefixType=_VRtrBierTxTunnelPtaPrefixType_Object((1,3,6,1,4,1,6527,3,1,2,123,11,1,6),_VRtrBierTxTunnelPtaPrefixType_Type())
vRtrBierTxTunnelPtaPrefixType.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierTxTunnelPtaPrefixType.setStatus(_A)
class _VRtrBierTxTunnelPtaPrefix_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_VRtrBierTxTunnelPtaPrefix_Type.__name__=_F
_VRtrBierTxTunnelPtaPrefix_Object=MibTableColumn
vRtrBierTxTunnelPtaPrefix=_VRtrBierTxTunnelPtaPrefix_Object((1,3,6,1,4,1,6527,3,1,2,123,11,1,7),_VRtrBierTxTunnelPtaPrefix_Type())
vRtrBierTxTunnelPtaPrefix.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierTxTunnelPtaPrefix.setStatus(_A)
_VRtrBierTxTunnelPtaBfrId_Type=Unsigned32
_VRtrBierTxTunnelPtaBfrId_Object=MibTableColumn
vRtrBierTxTunnelPtaBfrId=_VRtrBierTxTunnelPtaBfrId_Object((1,3,6,1,4,1,6527,3,1,2,123,11,1,8),_VRtrBierTxTunnelPtaBfrId_Type())
vRtrBierTxTunnelPtaBfrId.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierTxTunnelPtaBfrId.setStatus(_A)
_VRtrBierTxTunnelPtaSubDomain_Type=Unsigned32
_VRtrBierTxTunnelPtaSubDomain_Object=MibTableColumn
vRtrBierTxTunnelPtaSubDomain=_VRtrBierTxTunnelPtaSubDomain_Object((1,3,6,1,4,1,6527,3,1,2,123,11,1,9),_VRtrBierTxTunnelPtaSubDomain_Type())
vRtrBierTxTunnelPtaSubDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierTxTunnelPtaSubDomain.setStatus(_A)
_VRtrBierTxTunnelPtaMplsLabel_Type=Unsigned32
_VRtrBierTxTunnelPtaMplsLabel_Object=MibTableColumn
vRtrBierTxTunnelPtaMplsLabel=_VRtrBierTxTunnelPtaMplsLabel_Object((1,3,6,1,4,1,6527,3,1,2,123,11,1,10),_VRtrBierTxTunnelPtaMplsLabel_Type())
vRtrBierTxTunnelPtaMplsLabel.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierTxTunnelPtaMplsLabel.setStatus(_A)
_VRtrBierTxTunnelLeafBfrID_Type=Unsigned32
_VRtrBierTxTunnelLeafBfrID_Object=MibTableColumn
vRtrBierTxTunnelLeafBfrID=_VRtrBierTxTunnelLeafBfrID_Object((1,3,6,1,4,1,6527,3,1,2,123,11,1,11),_VRtrBierTxTunnelLeafBfrID_Type())
vRtrBierTxTunnelLeafBfrID.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierTxTunnelLeafBfrID.setStatus(_A)
_VRtrBierStatsTable_Object=MibTable
vRtrBierStatsTable=_VRtrBierStatsTable_Object((1,3,6,1,4,1,6527,3,1,2,123,12))
if mibBuilder.loadTexts:vRtrBierStatsTable.setStatus(_A)
_VRtrBierStatsEntry_Object=MibTableRow
vRtrBierStatsEntry=_VRtrBierStatsEntry_Object((1,3,6,1,4,1,6527,3,1,2,123,12,1))
vRtrBierStatsEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:vRtrBierStatsEntry.setStatus(_A)
_VRtrBierStatsTotalLearntRoutes_Type=Counter32
_VRtrBierStatsTotalLearntRoutes_Object=MibTableColumn
vRtrBierStatsTotalLearntRoutes=_VRtrBierStatsTotalLearntRoutes_Object((1,3,6,1,4,1,6527,3,1,2,123,12,1,1),_VRtrBierStatsTotalLearntRoutes_Type())
vRtrBierStatsTotalLearntRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierStatsTotalLearntRoutes.setStatus(_A)
_VRtrBierStatsTotalValidRoutes_Type=Counter32
_VRtrBierStatsTotalValidRoutes_Object=MibTableColumn
vRtrBierStatsTotalValidRoutes=_VRtrBierStatsTotalValidRoutes_Object((1,3,6,1,4,1,6527,3,1,2,123,12,1,2),_VRtrBierStatsTotalValidRoutes_Type())
vRtrBierStatsTotalValidRoutes.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierStatsTotalValidRoutes.setStatus(_A)
_VRtrBierStatsValidNbrNextHops_Type=Counter32
_VRtrBierStatsValidNbrNextHops_Object=MibTableColumn
vRtrBierStatsValidNbrNextHops=_VRtrBierStatsValidNbrNextHops_Object((1,3,6,1,4,1,6527,3,1,2,123,12,1,3),_VRtrBierStatsValidNbrNextHops_Type())
vRtrBierStatsValidNbrNextHops.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierStatsValidNbrNextHops.setStatus(_A)
_VRtrBierStatsRxInvalidBierInfo_Type=Counter32
_VRtrBierStatsRxInvalidBierInfo_Object=MibTableColumn
vRtrBierStatsRxInvalidBierInfo=_VRtrBierStatsRxInvalidBierInfo_Object((1,3,6,1,4,1,6527,3,1,2,123,12,1,4),_VRtrBierStatsRxInvalidBierInfo_Type())
vRtrBierStatsRxInvalidBierInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierStatsRxInvalidBierInfo.setStatus(_A)
_VRtrBierStatsRxInvalidBfrInfo_Type=Counter32
_VRtrBierStatsRxInvalidBfrInfo_Object=MibTableColumn
vRtrBierStatsRxInvalidBfrInfo=_VRtrBierStatsRxInvalidBfrInfo_Object((1,3,6,1,4,1,6527,3,1,2,123,12,1,5),_VRtrBierStatsRxInvalidBfrInfo_Type())
vRtrBierStatsRxInvalidBfrInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierStatsRxInvalidBfrInfo.setStatus(_A)
_VRtrBierStatsRxInvalidEncapInfo_Type=Counter32
_VRtrBierStatsRxInvalidEncapInfo_Object=MibTableColumn
vRtrBierStatsRxInvalidEncapInfo=_VRtrBierStatsRxInvalidEncapInfo_Object((1,3,6,1,4,1,6527,3,1,2,123,12,1,6),_VRtrBierStatsRxInvalidEncapInfo_Type())
vRtrBierStatsRxInvalidEncapInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierStatsRxInvalidEncapInfo.setStatus(_A)
_VRtrBierStatsRxInvalidMplsInfo_Type=Counter32
_VRtrBierStatsRxInvalidMplsInfo_Object=MibTableColumn
vRtrBierStatsRxInvalidMplsInfo=_VRtrBierStatsRxInvalidMplsInfo_Object((1,3,6,1,4,1,6527,3,1,2,123,12,1,7),_VRtrBierStatsRxInvalidMplsInfo_Type())
vRtrBierStatsRxInvalidMplsInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierStatsRxInvalidMplsInfo.setStatus(_A)
_VRtrBierStatsDiscardTunnelNhop_Type=Counter32
_VRtrBierStatsDiscardTunnelNhop_Object=MibTableColumn
vRtrBierStatsDiscardTunnelNhop=_VRtrBierStatsDiscardTunnelNhop_Object((1,3,6,1,4,1,6527,3,1,2,123,12,1,8),_VRtrBierStatsDiscardTunnelNhop_Type())
vRtrBierStatsDiscardTunnelNhop.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierStatsDiscardTunnelNhop.setStatus(_A)
_VRtrBierStatsDiscardNonNtwIfNhop_Type=Counter32
_VRtrBierStatsDiscardNonNtwIfNhop_Object=MibTableColumn
vRtrBierStatsDiscardNonNtwIfNhop=_VRtrBierStatsDiscardNonNtwIfNhop_Object((1,3,6,1,4,1,6527,3,1,2,123,12,1,9),_VRtrBierStatsDiscardNonNtwIfNhop_Type())
vRtrBierStatsDiscardNonNtwIfNhop.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierStatsDiscardNonNtwIfNhop.setStatus(_A)
_VRtrBierStatsDiscardNonFp4Nhop_Type=Counter32
_VRtrBierStatsDiscardNonFp4Nhop_Object=MibTableColumn
vRtrBierStatsDiscardNonFp4Nhop=_VRtrBierStatsDiscardNonFp4Nhop_Object((1,3,6,1,4,1,6527,3,1,2,123,12,1,10),_VRtrBierStatsDiscardNonFp4Nhop_Type())
vRtrBierStatsDiscardNonFp4Nhop.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierStatsDiscardNonFp4Nhop.setStatus(_A)
_VRtrBierStatsSdBslMismatch_Type=Counter32
_VRtrBierStatsSdBslMismatch_Object=MibTableColumn
vRtrBierStatsSdBslMismatch=_VRtrBierStatsSdBslMismatch_Object((1,3,6,1,4,1,6527,3,1,2,123,12,1,11),_VRtrBierStatsSdBslMismatch_Type())
vRtrBierStatsSdBslMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierStatsSdBslMismatch.setStatus(_A)
_VRtrBierStatsMultiTopoMismatch_Type=Counter32
_VRtrBierStatsMultiTopoMismatch_Object=MibTableColumn
vRtrBierStatsMultiTopoMismatch=_VRtrBierStatsMultiTopoMismatch_Object((1,3,6,1,4,1,6527,3,1,2,123,12,1,12),_VRtrBierStatsMultiTopoMismatch_Type())
vRtrBierStatsMultiTopoMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierStatsMultiTopoMismatch.setStatus(_A)
_VRtrBierStatsUnsupIpv6Routes_Type=Counter32
_VRtrBierStatsUnsupIpv6Routes_Object=MibTableColumn
vRtrBierStatsUnsupIpv6Routes=_VRtrBierStatsUnsupIpv6Routes_Object((1,3,6,1,4,1,6527,3,1,2,123,12,1,13),_VRtrBierStatsUnsupIpv6Routes_Type())
vRtrBierStatsUnsupIpv6Routes.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierStatsUnsupIpv6Routes.setStatus(_A)
_VRtrBierStatsBfrIdDuplicate_Type=Counter32
_VRtrBierStatsBfrIdDuplicate_Object=MibTableColumn
vRtrBierStatsBfrIdDuplicate=_VRtrBierStatsBfrIdDuplicate_Object((1,3,6,1,4,1,6527,3,1,2,123,12,1,14),_VRtrBierStatsBfrIdDuplicate_Type())
vRtrBierStatsBfrIdDuplicate.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierStatsBfrIdDuplicate.setStatus(_A)
_VRtrBierNotificationObjs_ObjectIdentity=ObjectIdentity
vRtrBierNotificationObjs=_VRtrBierNotificationObjs_ObjectIdentity((1,3,6,1,4,1,6527,3,1,2,123,13))
_VRtrBierNotifySubDomainId_Type=Unsigned32
_VRtrBierNotifySubDomainId_Object=MibScalar
vRtrBierNotifySubDomainId=_VRtrBierNotifySubDomainId_Object((1,3,6,1,4,1,6527,3,1,2,123,13,1),_VRtrBierNotifySubDomainId_Type())
vRtrBierNotifySubDomainId.setMaxAccess(_G)
if mibBuilder.loadTexts:vRtrBierNotifySubDomainId.setStatus(_A)
_VRtrBierNotifyRecvSubDomainId_Type=Unsigned32
_VRtrBierNotifyRecvSubDomainId_Object=MibScalar
vRtrBierNotifyRecvSubDomainId=_VRtrBierNotifyRecvSubDomainId_Object((1,3,6,1,4,1,6527,3,1,2,123,13,2),_VRtrBierNotifyRecvSubDomainId_Type())
vRtrBierNotifyRecvSubDomainId.setMaxAccess(_G)
if mibBuilder.loadTexts:vRtrBierNotifyRecvSubDomainId.setStatus(_A)
_VRtrBierNotifyBsl_Type=Unsigned32
_VRtrBierNotifyBsl_Object=MibScalar
vRtrBierNotifyBsl=_VRtrBierNotifyBsl_Object((1,3,6,1,4,1,6527,3,1,2,123,13,3),_VRtrBierNotifyBsl_Type())
vRtrBierNotifyBsl.setMaxAccess(_G)
if mibBuilder.loadTexts:vRtrBierNotifyBsl.setStatus(_A)
_VRtrBierNotifyBfrId_Type=Unsigned32
_VRtrBierNotifyBfrId_Object=MibScalar
vRtrBierNotifyBfrId=_VRtrBierNotifyBfrId_Object((1,3,6,1,4,1,6527,3,1,2,123,13,4),_VRtrBierNotifyBfrId_Type())
vRtrBierNotifyBfrId.setMaxAccess(_G)
if mibBuilder.loadTexts:vRtrBierNotifyBfrId.setStatus(_A)
_VRtrBierNotifyMTId_Type=TmnxBierMultiTopology
_VRtrBierNotifyMTId_Object=MibScalar
vRtrBierNotifyMTId=_VRtrBierNotifyMTId_Object((1,3,6,1,4,1,6527,3,1,2,123,13,5),_VRtrBierNotifyMTId_Type())
vRtrBierNotifyMTId.setMaxAccess(_G)
if mibBuilder.loadTexts:vRtrBierNotifyMTId.setStatus(_A)
_VRtrBierNotifyRecvMTId_Type=TmnxBierMultiTopology
_VRtrBierNotifyRecvMTId_Object=MibScalar
vRtrBierNotifyRecvMTId=_VRtrBierNotifyRecvMTId_Object((1,3,6,1,4,1,6527,3,1,2,123,13,6),_VRtrBierNotifyRecvMTId_Type())
vRtrBierNotifyRecvMTId.setMaxAccess(_G)
if mibBuilder.loadTexts:vRtrBierNotifyRecvMTId.setStatus(_A)
_VRtrBierPrefix1AddrType_Type=InetAddressType
_VRtrBierPrefix1AddrType_Object=MibScalar
vRtrBierPrefix1AddrType=_VRtrBierPrefix1AddrType_Object((1,3,6,1,4,1,6527,3,1,2,123,13,7),_VRtrBierPrefix1AddrType_Type())
vRtrBierPrefix1AddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:vRtrBierPrefix1AddrType.setStatus(_A)
class _VRtrBierPrefix1Address_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_VRtrBierPrefix1Address_Type.__name__=_F
_VRtrBierPrefix1Address_Object=MibScalar
vRtrBierPrefix1Address=_VRtrBierPrefix1Address_Object((1,3,6,1,4,1,6527,3,1,2,123,13,8),_VRtrBierPrefix1Address_Type())
vRtrBierPrefix1Address.setMaxAccess(_G)
if mibBuilder.loadTexts:vRtrBierPrefix1Address.setStatus(_A)
_VRtrBierPrefix2AddrType_Type=InetAddressType
_VRtrBierPrefix2AddrType_Object=MibScalar
vRtrBierPrefix2AddrType=_VRtrBierPrefix2AddrType_Object((1,3,6,1,4,1,6527,3,1,2,123,13,9),_VRtrBierPrefix2AddrType_Type())
vRtrBierPrefix2AddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:vRtrBierPrefix2AddrType.setStatus(_A)
class _VRtrBierPrefix2Address_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_VRtrBierPrefix2Address_Type.__name__=_F
_VRtrBierPrefix2Address_Object=MibScalar
vRtrBierPrefix2Address=_VRtrBierPrefix2Address_Object((1,3,6,1,4,1,6527,3,1,2,123,13,10),_VRtrBierPrefix2Address_Type())
vRtrBierPrefix2Address.setMaxAccess(_G)
if mibBuilder.loadTexts:vRtrBierPrefix2Address.setStatus(_A)
_VRtrBierNextHopAddrType_Type=InetAddressType
_VRtrBierNextHopAddrType_Object=MibScalar
vRtrBierNextHopAddrType=_VRtrBierNextHopAddrType_Object((1,3,6,1,4,1,6527,3,1,2,123,13,11),_VRtrBierNextHopAddrType_Type())
vRtrBierNextHopAddrType.setMaxAccess(_G)
if mibBuilder.loadTexts:vRtrBierNextHopAddrType.setStatus(_A)
class _VRtrBierNextHopAddress_Type(InetAddress):subtypeSpec=InetAddress.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(4,4),ValueSizeConstraint(16,16))
_VRtrBierNextHopAddress_Type.__name__=_F
_VRtrBierNextHopAddress_Object=MibScalar
vRtrBierNextHopAddress=_VRtrBierNextHopAddress_Object((1,3,6,1,4,1,6527,3,1,2,123,13,12),_VRtrBierNextHopAddress_Type())
vRtrBierNextHopAddress.setMaxAccess(_G)
if mibBuilder.loadTexts:vRtrBierNextHopAddress.setStatus(_A)
class _VRtrBierNextHopeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('tunnel',0),('non-nw-if',1),('non-fp4',2)))
_VRtrBierNextHopeType_Type.__name__=_R
_VRtrBierNextHopeType_Object=MibScalar
vRtrBierNextHopeType=_VRtrBierNextHopeType_Object((1,3,6,1,4,1,6527,3,1,2,123,13,13),_VRtrBierNextHopeType_Type())
vRtrBierNextHopeType.setMaxAccess(_G)
if mibBuilder.loadTexts:vRtrBierNextHopeType.setStatus(_A)
_VRtrBierUnsupportedNhopState_Type=TruthValue
_VRtrBierUnsupportedNhopState_Object=MibScalar
vRtrBierUnsupportedNhopState=_VRtrBierUnsupportedNhopState_Object((1,3,6,1,4,1,6527,3,1,2,123,13,14),_VRtrBierUnsupportedNhopState_Type())
vRtrBierUnsupportedNhopState.setMaxAccess(_G)
if mibBuilder.loadTexts:vRtrBierUnsupportedNhopState.setStatus(_A)
_VRtrBierGeneralOperTable_Object=MibTable
vRtrBierGeneralOperTable=_VRtrBierGeneralOperTable_Object((1,3,6,1,4,1,6527,3,1,2,123,14))
if mibBuilder.loadTexts:vRtrBierGeneralOperTable.setStatus(_A)
_VRtrBierGeneralOperEntry_Object=MibTableRow
vRtrBierGeneralOperEntry=_VRtrBierGeneralOperEntry_Object((1,3,6,1,4,1,6527,3,1,2,123,14,1))
vRtrBierGeneralOperEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:vRtrBierGeneralOperEntry.setStatus(_A)
class _VRtrBierGeneralOperState_Type(TmnxOperState):defaultValue=3
_VRtrBierGeneralOperState_Type.__name__=_T
_VRtrBierGeneralOperState_Object=MibTableColumn
vRtrBierGeneralOperState=_VRtrBierGeneralOperState_Object((1,3,6,1,4,1,6527,3,1,2,123,14,1,1),_VRtrBierGeneralOperState_Type())
vRtrBierGeneralOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierGeneralOperState.setStatus(_A)
_VRtrBierTemplateOperTable_Object=MibTable
vRtrBierTemplateOperTable=_VRtrBierTemplateOperTable_Object((1,3,6,1,4,1,6527,3,1,2,123,15))
if mibBuilder.loadTexts:vRtrBierTemplateOperTable.setStatus(_A)
_VRtrBierTemplateOperEntry_Object=MibTableRow
vRtrBierTemplateOperEntry=_VRtrBierTemplateOperEntry_Object((1,3,6,1,4,1,6527,3,1,2,123,15,1))
vRtrBierTemplateOperEntry.setIndexNames((0,_E,_H),(0,_B,_K))
if mibBuilder.loadTexts:vRtrBierTemplateOperEntry.setStatus(_A)
class _VRtrBierTemplateOperState_Type(TmnxOperState):defaultValue=3
_VRtrBierTemplateOperState_Type.__name__=_T
_VRtrBierTemplateOperState_Object=MibTableColumn
vRtrBierTemplateOperState=_VRtrBierTemplateOperState_Object((1,3,6,1,4,1,6527,3,1,2,123,15,1,1),_VRtrBierTemplateOperState_Type())
vRtrBierTemplateOperState.setMaxAccess(_C)
if mibBuilder.loadTexts:vRtrBierTemplateOperState.setStatus(_A)
_VRtrBierNotifyPrefix_ObjectIdentity=ObjectIdentity
vRtrBierNotifyPrefix=_VRtrBierNotifyPrefix_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,123))
_VRtrBierNotifications_ObjectIdentity=ObjectIdentity
vRtrBierNotifications=_VRtrBierNotifications_ObjectIdentity((1,3,6,1,4,1,6527,3,1,3,123,0))
tmnxBierV16v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,123,2,1))
tmnxBierV16v0Group.setObjects(*((_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An),(_B,_Ao),(_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At),(_B,_Au),(_B,_Av),(_B,_Aw),(_B,_Ax)))
if mibBuilder.loadTexts:tmnxBierV16v0Group.setStatus(_A)
tmnxBierNotifyObjsGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,123,2,2))
tmnxBierNotifyObjsGroup.setObjects(*((_B,_L),(_B,_U),(_B,_M),(_B,_V),(_B,_W),(_B,_X),(_B,_P),(_B,_Q),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:tmnxBierNotifyObjsGroup.setStatus(_A)
tmnxBierOperStateGroup=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,123,2,4))
tmnxBierOperStateGroup.setObjects(*((_B,_Ay),(_B,_Az)))
if mibBuilder.loadTexts:tmnxBierOperStateGroup.setStatus(_A)
tmnxBierV19v0Group=ObjectGroup((1,3,6,1,4,1,6527,3,1,1,123,2,5))
tmnxBierV19v0Group.setObjects((_B,_A_))
if mibBuilder.loadTexts:tmnxBierV19v0Group.setStatus(_A)
vRtrBierBfrIdCollision=NotificationType((1,3,6,1,4,1,6527,3,1,3,123,0,1))
vRtrBierBfrIdCollision.setObjects(*((_B,_L),(_B,_M),(_B,_P),(_B,_Q),(_B,_Y),(_B,_Z),(_B,_V)))
if mibBuilder.loadTexts:vRtrBierBfrIdCollision.setStatus(_A)
vRtrBierMtMismatch=NotificationType((1,3,6,1,4,1,6527,3,1,3,123,0,2))
vRtrBierMtMismatch.setObjects(*((_B,_L),(_B,_M),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:vRtrBierMtMismatch.setStatus(_A)
vRtrBierSubDomainMismatch=NotificationType((1,3,6,1,4,1,6527,3,1,3,123,0,3))
vRtrBierSubDomainMismatch.setObjects(*((_B,_L),(_B,_M),(_B,_U)))
if mibBuilder.loadTexts:vRtrBierSubDomainMismatch.setStatus(_A)
vRtrBierUnsupportedNhop=NotificationType((1,3,6,1,4,1,6527,3,1,3,123,0,4))
vRtrBierUnsupportedNhop.setObjects(*((_B,_c),(_B,_d),(_B,_P),(_B,_Q),(_B,_a),(_B,_b),(_E,_O)))
if mibBuilder.loadTexts:vRtrBierUnsupportedNhop.setStatus(_A)
tmnxBierNotificationV16v0Group=NotificationGroup((1,3,6,1,4,1,6527,3,1,1,123,2,3))
tmnxBierNotificationV16v0Group.setObjects(*((_B,_B0),(_B,_B1),(_B,_B2),(_B,_B3)))
if mibBuilder.loadTexts:tmnxBierNotificationV16v0Group.setStatus(_A)
tmnxBierV16v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,123,1,1))
tmnxBierV16v0Compliance.setObjects(*((_B,_B4),(_B,_B5),(_B,_B6)))
if mibBuilder.loadTexts:tmnxBierV16v0Compliance.setStatus(_A)
tmnxBierV19v0Compliance=ModuleCompliance((1,3,6,1,4,1,6527,3,1,1,123,1,2))
tmnxBierV19v0Compliance.setObjects((_B,_B7))
if mibBuilder.loadTexts:tmnxBierV19v0Compliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_h:TmnxBierMultiTopology,'timetraBierMIBModule':timetraBierMIBModule,'tmnxBierConformance':tmnxBierConformance,'tmnxBierCompliances':tmnxBierCompliances,'tmnxBierV16v0Compliance':tmnxBierV16v0Compliance,'tmnxBierV19v0Compliance':tmnxBierV19v0Compliance,'tmnxBierGroups':tmnxBierGroups,_B4:tmnxBierV16v0Group,'tmnxBierNotifyObjsGroup':tmnxBierNotifyObjsGroup,_B5:tmnxBierNotificationV16v0Group,_B6:tmnxBierOperStateGroup,_B7:tmnxBierV19v0Group,'tmnxBierObjs':tmnxBierObjs,_y:vRtrBierGeneralTableLastChanged,'vRtrBierGeneralTable':vRtrBierGeneralTable,'vRtrBierGeneralEntry':vRtrBierGeneralEntry,_z:vRtrBierGeneralRowStatus,_A0:vRtrBierGeneralAdminState,_A1:vRtrBierGeneralRowLastChange,_A2:vRtrBierTemplateTableLastChanged,'vRtrBierTemplateTable':vRtrBierTemplateTable,'vRtrBierTemplateEntry':vRtrBierTemplateEntry,_K:vRtrBierTemplateName,_A3:vRtrBierTemplateRowStatus,_A4:vRtrBierTemplateAdminState,_A5:vRtrBierTemplateRowLastChange,_A6:vRtrBierSubDomainTableLstChanged,'vRtrBierSubDomainTable':vRtrBierSubDomainTable,'vRtrBierSubDomainEntry':vRtrBierSubDomainEntry,_f:vRtrBierSubDomainStart,_g:vRtrBierSubDomainEnd,_A7:vRtrBierSubDomainPrefixType,_A8:vRtrBierSubDomainPrefix,_A9:vRtrBierSubDomainBfrId,_AA:vRtrBierSubDomainMT,_AB:vRtrBierSubDomainRowStatus,_AC:vRtrBierSubDomainRowLastChange,'vRtrBierDatabaseTable':vRtrBierDatabaseTable,'vRtrBierDatabaseEntry':vRtrBierDatabaseEntry,_i:vRtrBierDatabaseSubDomainId,_AD:vRtrBierDatabaseBitStringLen,_AE:vRtrBierDatabasePrefixType,_AF:vRtrBierDatabasePrefix,_AG:vRtrBierDatabaseBfrId,_AH:vRtrBierDatabaseMT,_AI:vRtrBierDatabaseMplsLabelStart,_AJ:vRtrBierDatabaseMplsLabelEnd,_AK:vRtrBierDatabaseMplsLabelTotal,'vRtrBierForwardingTable':vRtrBierForwardingTable,'vRtrBierForwardingEntry':vRtrBierForwardingEntry,_j:vRtrBierForwardingSubDomainId,_k:vRtrBierForwardingBitStringLen,_l:vRtrBierForwardingNhopPrefixType,_m:vRtrBierForwardingNhopPrefix,_n:vRtrBierForwardingNhopIfIndex,_o:vRtrBierForwardingBierSetId,_AL:vRtrBierForwardingNbrPrefixType,_AM:vRtrBierForwardingNbrPrefix,_AN:vRtrBierForwardingBitMask,_AO:vRtrBierForwardingMplsLabel,'vRtrBierRoutingTable':vRtrBierRoutingTable,'vRtrBierRoutingEntry':vRtrBierRoutingEntry,_p:vRtrBierRoutingSubDomainId,_q:vRtrBierRoutingBitStringLen,_r:vRtrBierRoutingNhopPrefixType,_s:vRtrBierRoutingNhopPrefix,_t:vRtrBierRoutingNhopIfIndex,_u:vRtrBierRoutingDestPrefixType,_v:vRtrBierRoutingDestPrefix,_AP:vRtrBierRoutingNbrPrefixType,_AQ:vRtrBierRoutingNbrPrefix,_AR:vRtrBierRoutingBfrId,_AS:vRtrBierRoutingLastUpdated,'vRtrBierTunnelTable':vRtrBierTunnelTable,'vRtrBierTunnelEntry':vRtrBierTunnelEntry,_AT:vRtrBierTunnelType,_AU:vRtrBierTunnelPrefixType,_AV:vRtrBierTunnelPrefix,_AW:vRtrBierTunnelSubDomain,_AX:vRtrBierTunnelMplsLabel,_AY:vRtrBierTunnelBfrId,_AZ:vRtrBierTunnelOperState,_Aa:vRtrBierTunnelNumLeaves,_Ab:vRtrBierTunnelLastOperDownReason,_A_:vRtrBierTunnelIsInBand,'vRtrBierTxTunnelLeafTable':vRtrBierTxTunnelLeafTable,'vRtrBierTxTunnelLeafEntry':vRtrBierTxTunnelLeafEntry,_w:vRtrBierTxTunnelLeafPrefixType,_x:vRtrBierTxTunnelLeafPrefix,_Ac:vRtrBierTxTunnelMvpnId,_Ad:vRtrBierTxTunnelOperState,_Ae:vRtrBierTxTunnelPtaPrefixType,_Af:vRtrBierTxTunnelPtaPrefix,_Ag:vRtrBierTxTunnelPtaBfrId,_Ah:vRtrBierTxTunnelPtaSubDomain,_Ai:vRtrBierTxTunnelPtaMplsLabel,_Aj:vRtrBierTxTunnelLeafBfrID,'vRtrBierStatsTable':vRtrBierStatsTable,'vRtrBierStatsEntry':vRtrBierStatsEntry,_Ak:vRtrBierStatsTotalLearntRoutes,_Al:vRtrBierStatsTotalValidRoutes,_Am:vRtrBierStatsValidNbrNextHops,_An:vRtrBierStatsRxInvalidBierInfo,_Ao:vRtrBierStatsRxInvalidBfrInfo,_Ap:vRtrBierStatsRxInvalidEncapInfo,_Aq:vRtrBierStatsRxInvalidMplsInfo,_Ar:vRtrBierStatsDiscardTunnelNhop,_As:vRtrBierStatsDiscardNonNtwIfNhop,_At:vRtrBierStatsDiscardNonFp4Nhop,_Au:vRtrBierStatsSdBslMismatch,_Av:vRtrBierStatsMultiTopoMismatch,_Aw:vRtrBierStatsUnsupIpv6Routes,_Ax:vRtrBierStatsBfrIdDuplicate,'vRtrBierNotificationObjs':vRtrBierNotificationObjs,_L:vRtrBierNotifySubDomainId,_U:vRtrBierNotifyRecvSubDomainId,_M:vRtrBierNotifyBsl,_V:vRtrBierNotifyBfrId,_W:vRtrBierNotifyMTId,_X:vRtrBierNotifyRecvMTId,_P:vRtrBierPrefix1AddrType,_Q:vRtrBierPrefix1Address,_Y:vRtrBierPrefix2AddrType,_Z:vRtrBierPrefix2Address,_a:vRtrBierNextHopAddrType,_b:vRtrBierNextHopAddress,_c:vRtrBierNextHopeType,_d:vRtrBierUnsupportedNhopState,'vRtrBierGeneralOperTable':vRtrBierGeneralOperTable,'vRtrBierGeneralOperEntry':vRtrBierGeneralOperEntry,_Ay:vRtrBierGeneralOperState,'vRtrBierTemplateOperTable':vRtrBierTemplateOperTable,'vRtrBierTemplateOperEntry':vRtrBierTemplateOperEntry,_Az:vRtrBierTemplateOperState,'vRtrBierNotifyPrefix':vRtrBierNotifyPrefix,'vRtrBierNotifications':vRtrBierNotifications,_B0:vRtrBierBfrIdCollision,_B1:vRtrBierMtMismatch,_B2:vRtrBierSubDomainMismatch,_B3:vRtrBierUnsupportedNhop})