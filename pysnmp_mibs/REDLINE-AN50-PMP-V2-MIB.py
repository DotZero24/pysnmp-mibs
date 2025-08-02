_Aj='an50pmpLinkULQoS'
_Ai='an50pmpLinkDLQoS'
_Ah='an50pmpLinkCIDULPIR'
_Ag='an50pmpLinkCIDULCIR'
_Af='an50pmpLinkCIDDLPIR'
_Ae='an50pmpLinkCIDDLCIR'
_Ad='an50pmpLinkMaxHost'
_Ac='an50pmpLinkGroupId'
_Ab='an50pmpConnectionStatusULPacketsRx'
_Aa='an50pmpConnectionStatusULPacketsTx'
_AZ='an50pmpConnectionStatusULPacketsDiscards'
_AY='an50pmpConnectionStatusDLPacketsRx'
_AX='an50pmpConnectionStatusDLPacketsTx'
_AW='an50pmpConnectionStatusDLPacketsDiscards'
_AV='an50pmpGroupStatusULPacketsRx'
_AU='an50pmpGroupStatusULPacketsTx'
_AT='an50pmpGroupStatusULPacketsDiscards'
_AS='an50pmpGroupStatusDLPacketsRx'
_AR='an50pmpGroupStatusDLPacketsTx'
_AQ='an50pmpGroupStatusDLPacketsDiscards'
_AP='an50pmpConnectionRowStatus'
_AO='an50pmpConnectionULQoS'
_AN='an50pmpConnectionDLQoS'
_AM='an50pmpConnectionParentGroup'
_AL='an50pmpConnectionParentLink'
_AK='an50pmpConnectionDefaultPriority'
_AJ='an50pmpConnectionVlanId'
_AI='an50pmpConnectionPortTagging'
_AH='an50pmpConnectionName'
_AG='an50pmpGroupRowStatus'
_AF='an50pmpGroupQos'
_AE='an50pmpGroupBSPortEnabled'
_AD='an50pmpGroupDefaultPriority'
_AC='an50pmpGroupVlanId'
_AB='an50pmpGroupBSPortTagging'
_AA='an50pmpGroupName'
_A9='an50pmpLastDeniedSsMacAddress'
_A8='an50pmpLastSuccessfulID'
_A7='an50pmpLastRegisteredSsMacAddress'
_A6='an50pmpLastMissedSsMacAddress'
_A5='an50pmpLastModifiedCID'
_A4='an50pmpCIDSaveConfig'
_A3='an50pmpLinkLostCount'
_A2='an50pmpLinkUpTime'
_A1='an50pmpLinkULCIDStatPktRecv'
_A0='an50pmpLinkULCIDStatPktTran'
_z='an50pmpLinkULCIDStatPktDisc'
_y='an50pmpLinkULStatBlksDisc'
_x='an50pmpLinkULStatBlksRetr'
_w='an50pmpLinkULStatBlksTot'
_v='an50pmpLinkULStatLostFrm'
_u='an50pmpLinkULSINADR'
_t='an50pmpLinkULRSSI'
_s='an50pmpLinkULBurstRate'
_r='an50pmpLinkDLCIDStatPktRecv'
_q='an50pmpLinkDLCIDStatPktTran'
_p='an50pmpLinkDLCIDStatPktDisc'
_o='an50pmpLinkDLStatBlksDisc'
_n='an50pmpLinkDLStatBlksRetr'
_m='an50pmpLinkDLStatBlksTot'
_l='an50pmpLinkDLStatLostFrm'
_k='an50pmpLinkDLSINADR'
_j='an50pmpLinkDLRSSI'
_i='an50pmpLinkDLBurstRate'
_h='an50pmpLinkRegConn'
_g='an50pmpLinkStatusCode'
_f='an50pmpLinkStatus'
_e='an50pmpLinkRowStatus'
_d='an50pmpLinkEncryptionKey'
_c='an50pmpLinkMaxULBurstRate'
_b='an50pmpLinkMaxDLBurstRate'
_a='an50pmpLinkPeerMac'
_Z='an50pmpLinkName'
_Y='an50pmpConnectionStatusId'
_X='an50pmpGroupStatusId'
_W='an50pmpConnectionId'
_V='tagged'
_U='passThrough'
_T='an50pmpGroupId'
_S='tx54Mbs'
_R='tx48Mbs'
_Q='tx36Mbs'
_P='tx24Mbs'
_O='tx18Mbs'
_N='tx12Mbs'
_M='tx9Mbs'
_L='tx6Mbs'
_K='an50pmpLinkStatusID'
_J='an50pmpLinkID'
_I='RowStatus'
_H='not-accessible'
_G='OctetString'
_F='obsolete'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='REDLINE-AN50-PMP-V2-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
redlineMgmt,=mibBuilder.importSymbols('REDLINE-MIB','redlineMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress',_I,'TextualConvention')
redlineAN50PMPV2=ModuleIdentity((1,3,6,1,4,1,10728,2,51))
_An50pmpLinkTable_Object=MibTable
an50pmpLinkTable=_An50pmpLinkTable_Object((1,3,6,1,4,1,10728,2,51,1))
if mibBuilder.loadTexts:an50pmpLinkTable.setStatus(_A)
_An50pmpLinkEntry_Object=MibTableRow
an50pmpLinkEntry=_An50pmpLinkEntry_Object((1,3,6,1,4,1,10728,2,51,1,1))
an50pmpLinkEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:an50pmpLinkEntry.setStatus(_A)
class _An50pmpLinkID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_An50pmpLinkID_Type.__name__=_D
_An50pmpLinkID_Object=MibTableColumn
an50pmpLinkID=_An50pmpLinkID_Object((1,3,6,1,4,1,10728,2,51,1,1,1),_An50pmpLinkID_Type())
an50pmpLinkID.setMaxAccess(_H)
if mibBuilder.loadTexts:an50pmpLinkID.setStatus(_A)
class _An50pmpLinkName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_An50pmpLinkName_Type.__name__=_G
_An50pmpLinkName_Object=MibTableColumn
an50pmpLinkName=_An50pmpLinkName_Object((1,3,6,1,4,1,10728,2,51,1,1,2),_An50pmpLinkName_Type())
an50pmpLinkName.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpLinkName.setStatus(_A)
class _An50pmpLinkGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_An50pmpLinkGroupId_Type.__name__=_D
_An50pmpLinkGroupId_Object=MibTableColumn
an50pmpLinkGroupId=_An50pmpLinkGroupId_Object((1,3,6,1,4,1,10728,2,51,1,1,3),_An50pmpLinkGroupId_Type())
an50pmpLinkGroupId.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpLinkGroupId.setStatus(_F)
class _An50pmpLinkPeerMac_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_An50pmpLinkPeerMac_Type.__name__=_G
_An50pmpLinkPeerMac_Object=MibTableColumn
an50pmpLinkPeerMac=_An50pmpLinkPeerMac_Object((1,3,6,1,4,1,10728,2,51,1,1,4),_An50pmpLinkPeerMac_Type())
an50pmpLinkPeerMac.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpLinkPeerMac.setStatus(_A)
class _An50pmpLinkMaxDLBurstRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_An50pmpLinkMaxDLBurstRate_Type.__name__=_D
_An50pmpLinkMaxDLBurstRate_Object=MibTableColumn
an50pmpLinkMaxDLBurstRate=_An50pmpLinkMaxDLBurstRate_Object((1,3,6,1,4,1,10728,2,51,1,1,5),_An50pmpLinkMaxDLBurstRate_Type())
an50pmpLinkMaxDLBurstRate.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpLinkMaxDLBurstRate.setStatus(_A)
class _An50pmpLinkMaxULBurstRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_An50pmpLinkMaxULBurstRate_Type.__name__=_D
_An50pmpLinkMaxULBurstRate_Object=MibTableColumn
an50pmpLinkMaxULBurstRate=_An50pmpLinkMaxULBurstRate_Object((1,3,6,1,4,1,10728,2,51,1,1,6),_An50pmpLinkMaxULBurstRate_Type())
an50pmpLinkMaxULBurstRate.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpLinkMaxULBurstRate.setStatus(_A)
_An50pmpLinkMaxHost_Type=Integer32
_An50pmpLinkMaxHost_Object=MibTableColumn
an50pmpLinkMaxHost=_An50pmpLinkMaxHost_Object((1,3,6,1,4,1,10728,2,51,1,1,7),_An50pmpLinkMaxHost_Type())
an50pmpLinkMaxHost.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpLinkMaxHost.setStatus(_F)
class _An50pmpLinkCIDDLCIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_An50pmpLinkCIDDLCIR_Type.__name__=_D
_An50pmpLinkCIDDLCIR_Object=MibTableColumn
an50pmpLinkCIDDLCIR=_An50pmpLinkCIDDLCIR_Object((1,3,6,1,4,1,10728,2,51,1,1,8),_An50pmpLinkCIDDLCIR_Type())
an50pmpLinkCIDDLCIR.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpLinkCIDDLCIR.setStatus(_F)
class _An50pmpLinkCIDDLPIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_An50pmpLinkCIDDLPIR_Type.__name__=_D
_An50pmpLinkCIDDLPIR_Object=MibTableColumn
an50pmpLinkCIDDLPIR=_An50pmpLinkCIDDLPIR_Object((1,3,6,1,4,1,10728,2,51,1,1,9),_An50pmpLinkCIDDLPIR_Type())
an50pmpLinkCIDDLPIR.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpLinkCIDDLPIR.setStatus(_F)
class _An50pmpLinkCIDULCIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_An50pmpLinkCIDULCIR_Type.__name__=_D
_An50pmpLinkCIDULCIR_Object=MibTableColumn
an50pmpLinkCIDULCIR=_An50pmpLinkCIDULCIR_Object((1,3,6,1,4,1,10728,2,51,1,1,10),_An50pmpLinkCIDULCIR_Type())
an50pmpLinkCIDULCIR.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpLinkCIDULCIR.setStatus(_F)
class _An50pmpLinkCIDULPIR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_An50pmpLinkCIDULPIR_Type.__name__=_D
_An50pmpLinkCIDULPIR_Object=MibTableColumn
an50pmpLinkCIDULPIR=_An50pmpLinkCIDULPIR_Object((1,3,6,1,4,1,10728,2,51,1,1,11),_An50pmpLinkCIDULPIR_Type())
an50pmpLinkCIDULPIR.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpLinkCIDULPIR.setStatus(_F)
class _An50pmpLinkDLQoS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,54))
_An50pmpLinkDLQoS_Type.__name__=_D
_An50pmpLinkDLQoS_Object=MibTableColumn
an50pmpLinkDLQoS=_An50pmpLinkDLQoS_Object((1,3,6,1,4,1,10728,2,51,1,1,12),_An50pmpLinkDLQoS_Type())
an50pmpLinkDLQoS.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpLinkDLQoS.setStatus(_F)
class _An50pmpLinkULQoS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,54))
_An50pmpLinkULQoS_Type.__name__=_D
_An50pmpLinkULQoS_Object=MibTableColumn
an50pmpLinkULQoS=_An50pmpLinkULQoS_Object((1,3,6,1,4,1,10728,2,51,1,1,13),_An50pmpLinkULQoS_Type())
an50pmpLinkULQoS.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpLinkULQoS.setStatus(_F)
class _An50pmpLinkRowStatus_Type(RowStatus):defaultValue=5
_An50pmpLinkRowStatus_Type.__name__=_I
_An50pmpLinkRowStatus_Object=MibTableColumn
an50pmpLinkRowStatus=_An50pmpLinkRowStatus_Object((1,3,6,1,4,1,10728,2,51,1,1,14),_An50pmpLinkRowStatus_Type())
an50pmpLinkRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpLinkRowStatus.setStatus(_A)
class _An50pmpLinkEncryptionKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_An50pmpLinkEncryptionKey_Type.__name__=_G
_An50pmpLinkEncryptionKey_Object=MibTableColumn
an50pmpLinkEncryptionKey=_An50pmpLinkEncryptionKey_Object((1,3,6,1,4,1,10728,2,51,1,1,15),_An50pmpLinkEncryptionKey_Type())
an50pmpLinkEncryptionKey.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpLinkEncryptionKey.setStatus(_A)
_An50pmpLinkStatusTable_Object=MibTable
an50pmpLinkStatusTable=_An50pmpLinkStatusTable_Object((1,3,6,1,4,1,10728,2,51,2))
if mibBuilder.loadTexts:an50pmpLinkStatusTable.setStatus(_A)
_An50pmpLinkStatusEntry_Object=MibTableRow
an50pmpLinkStatusEntry=_An50pmpLinkStatusEntry_Object((1,3,6,1,4,1,10728,2,51,2,1))
an50pmpLinkStatusEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:an50pmpLinkStatusEntry.setStatus(_A)
class _An50pmpLinkStatusID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_An50pmpLinkStatusID_Type.__name__=_D
_An50pmpLinkStatusID_Object=MibTableColumn
an50pmpLinkStatusID=_An50pmpLinkStatusID_Object((1,3,6,1,4,1,10728,2,51,2,1,1),_An50pmpLinkStatusID_Type())
an50pmpLinkStatusID.setMaxAccess(_H)
if mibBuilder.loadTexts:an50pmpLinkStatusID.setStatus(_A)
class _An50pmpLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_An50pmpLinkStatus_Type.__name__=_D
_An50pmpLinkStatus_Object=MibTableColumn
an50pmpLinkStatus=_An50pmpLinkStatus_Object((1,3,6,1,4,1,10728,2,51,2,1,2),_An50pmpLinkStatus_Type())
an50pmpLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLinkStatus.setStatus(_A)
_An50pmpLinkStatusCode_Type=Integer32
_An50pmpLinkStatusCode_Object=MibTableColumn
an50pmpLinkStatusCode=_An50pmpLinkStatusCode_Object((1,3,6,1,4,1,10728,2,51,2,1,3),_An50pmpLinkStatusCode_Type())
an50pmpLinkStatusCode.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLinkStatusCode.setStatus(_A)
class _An50pmpLinkRegConn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_An50pmpLinkRegConn_Type.__name__=_D
_An50pmpLinkRegConn_Object=MibTableColumn
an50pmpLinkRegConn=_An50pmpLinkRegConn_Object((1,3,6,1,4,1,10728,2,51,2,1,4),_An50pmpLinkRegConn_Type())
an50pmpLinkRegConn.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLinkRegConn.setStatus(_A)
class _An50pmpLinkDLBurstRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_R,7),(_S,8)))
_An50pmpLinkDLBurstRate_Type.__name__=_D
_An50pmpLinkDLBurstRate_Object=MibTableColumn
an50pmpLinkDLBurstRate=_An50pmpLinkDLBurstRate_Object((1,3,6,1,4,1,10728,2,51,2,1,5),_An50pmpLinkDLBurstRate_Type())
an50pmpLinkDLBurstRate.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLinkDLBurstRate.setStatus(_A)
_An50pmpLinkDLRSSI_Type=Integer32
_An50pmpLinkDLRSSI_Object=MibTableColumn
an50pmpLinkDLRSSI=_An50pmpLinkDLRSSI_Object((1,3,6,1,4,1,10728,2,51,2,1,6),_An50pmpLinkDLRSSI_Type())
an50pmpLinkDLRSSI.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLinkDLRSSI.setStatus(_A)
_An50pmpLinkDLSINADR_Type=Integer32
_An50pmpLinkDLSINADR_Object=MibTableColumn
an50pmpLinkDLSINADR=_An50pmpLinkDLSINADR_Object((1,3,6,1,4,1,10728,2,51,2,1,7),_An50pmpLinkDLSINADR_Type())
an50pmpLinkDLSINADR.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLinkDLSINADR.setStatus(_A)
_An50pmpLinkDLStatLostFrm_Type=Integer32
_An50pmpLinkDLStatLostFrm_Object=MibTableColumn
an50pmpLinkDLStatLostFrm=_An50pmpLinkDLStatLostFrm_Object((1,3,6,1,4,1,10728,2,51,2,1,8),_An50pmpLinkDLStatLostFrm_Type())
an50pmpLinkDLStatLostFrm.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLinkDLStatLostFrm.setStatus(_A)
_An50pmpLinkDLStatBlksTot_Type=Integer32
_An50pmpLinkDLStatBlksTot_Object=MibTableColumn
an50pmpLinkDLStatBlksTot=_An50pmpLinkDLStatBlksTot_Object((1,3,6,1,4,1,10728,2,51,2,1,9),_An50pmpLinkDLStatBlksTot_Type())
an50pmpLinkDLStatBlksTot.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLinkDLStatBlksTot.setStatus(_A)
_An50pmpLinkDLStatBlksRetr_Type=Integer32
_An50pmpLinkDLStatBlksRetr_Object=MibTableColumn
an50pmpLinkDLStatBlksRetr=_An50pmpLinkDLStatBlksRetr_Object((1,3,6,1,4,1,10728,2,51,2,1,10),_An50pmpLinkDLStatBlksRetr_Type())
an50pmpLinkDLStatBlksRetr.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLinkDLStatBlksRetr.setStatus(_A)
_An50pmpLinkDLStatBlksDisc_Type=Integer32
_An50pmpLinkDLStatBlksDisc_Object=MibTableColumn
an50pmpLinkDLStatBlksDisc=_An50pmpLinkDLStatBlksDisc_Object((1,3,6,1,4,1,10728,2,51,2,1,11),_An50pmpLinkDLStatBlksDisc_Type())
an50pmpLinkDLStatBlksDisc.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLinkDLStatBlksDisc.setStatus(_A)
_An50pmpLinkDLCIDStatPktDisc_Type=Integer32
_An50pmpLinkDLCIDStatPktDisc_Object=MibTableColumn
an50pmpLinkDLCIDStatPktDisc=_An50pmpLinkDLCIDStatPktDisc_Object((1,3,6,1,4,1,10728,2,51,2,1,12),_An50pmpLinkDLCIDStatPktDisc_Type())
an50pmpLinkDLCIDStatPktDisc.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLinkDLCIDStatPktDisc.setStatus(_A)
_An50pmpLinkDLCIDStatPktTran_Type=Integer32
_An50pmpLinkDLCIDStatPktTran_Object=MibTableColumn
an50pmpLinkDLCIDStatPktTran=_An50pmpLinkDLCIDStatPktTran_Object((1,3,6,1,4,1,10728,2,51,2,1,13),_An50pmpLinkDLCIDStatPktTran_Type())
an50pmpLinkDLCIDStatPktTran.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLinkDLCIDStatPktTran.setStatus(_A)
_An50pmpLinkDLCIDStatPktRecv_Type=Integer32
_An50pmpLinkDLCIDStatPktRecv_Object=MibTableColumn
an50pmpLinkDLCIDStatPktRecv=_An50pmpLinkDLCIDStatPktRecv_Object((1,3,6,1,4,1,10728,2,51,2,1,14),_An50pmpLinkDLCIDStatPktRecv_Type())
an50pmpLinkDLCIDStatPktRecv.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLinkDLCIDStatPktRecv.setStatus(_A)
class _An50pmpLinkULBurstRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4),(_P,5),(_Q,6),(_R,7),(_S,8)))
_An50pmpLinkULBurstRate_Type.__name__=_D
_An50pmpLinkULBurstRate_Object=MibTableColumn
an50pmpLinkULBurstRate=_An50pmpLinkULBurstRate_Object((1,3,6,1,4,1,10728,2,51,2,1,15),_An50pmpLinkULBurstRate_Type())
an50pmpLinkULBurstRate.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLinkULBurstRate.setStatus(_A)
_An50pmpLinkULRSSI_Type=Integer32
_An50pmpLinkULRSSI_Object=MibTableColumn
an50pmpLinkULRSSI=_An50pmpLinkULRSSI_Object((1,3,6,1,4,1,10728,2,51,2,1,16),_An50pmpLinkULRSSI_Type())
an50pmpLinkULRSSI.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLinkULRSSI.setStatus(_A)
_An50pmpLinkULSINADR_Type=Integer32
_An50pmpLinkULSINADR_Object=MibTableColumn
an50pmpLinkULSINADR=_An50pmpLinkULSINADR_Object((1,3,6,1,4,1,10728,2,51,2,1,17),_An50pmpLinkULSINADR_Type())
an50pmpLinkULSINADR.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLinkULSINADR.setStatus(_A)
_An50pmpLinkULStatLostFrm_Type=Integer32
_An50pmpLinkULStatLostFrm_Object=MibTableColumn
an50pmpLinkULStatLostFrm=_An50pmpLinkULStatLostFrm_Object((1,3,6,1,4,1,10728,2,51,2,1,18),_An50pmpLinkULStatLostFrm_Type())
an50pmpLinkULStatLostFrm.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLinkULStatLostFrm.setStatus(_A)
_An50pmpLinkULStatBlksTot_Type=Integer32
_An50pmpLinkULStatBlksTot_Object=MibTableColumn
an50pmpLinkULStatBlksTot=_An50pmpLinkULStatBlksTot_Object((1,3,6,1,4,1,10728,2,51,2,1,19),_An50pmpLinkULStatBlksTot_Type())
an50pmpLinkULStatBlksTot.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLinkULStatBlksTot.setStatus(_A)
_An50pmpLinkULStatBlksRetr_Type=Integer32
_An50pmpLinkULStatBlksRetr_Object=MibTableColumn
an50pmpLinkULStatBlksRetr=_An50pmpLinkULStatBlksRetr_Object((1,3,6,1,4,1,10728,2,51,2,1,20),_An50pmpLinkULStatBlksRetr_Type())
an50pmpLinkULStatBlksRetr.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLinkULStatBlksRetr.setStatus(_A)
_An50pmpLinkULStatBlksDisc_Type=Integer32
_An50pmpLinkULStatBlksDisc_Object=MibTableColumn
an50pmpLinkULStatBlksDisc=_An50pmpLinkULStatBlksDisc_Object((1,3,6,1,4,1,10728,2,51,2,1,21),_An50pmpLinkULStatBlksDisc_Type())
an50pmpLinkULStatBlksDisc.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLinkULStatBlksDisc.setStatus(_A)
_An50pmpLinkULCIDStatPktDisc_Type=Integer32
_An50pmpLinkULCIDStatPktDisc_Object=MibTableColumn
an50pmpLinkULCIDStatPktDisc=_An50pmpLinkULCIDStatPktDisc_Object((1,3,6,1,4,1,10728,2,51,2,1,22),_An50pmpLinkULCIDStatPktDisc_Type())
an50pmpLinkULCIDStatPktDisc.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLinkULCIDStatPktDisc.setStatus(_A)
_An50pmpLinkULCIDStatPktTran_Type=Integer32
_An50pmpLinkULCIDStatPktTran_Object=MibTableColumn
an50pmpLinkULCIDStatPktTran=_An50pmpLinkULCIDStatPktTran_Object((1,3,6,1,4,1,10728,2,51,2,1,23),_An50pmpLinkULCIDStatPktTran_Type())
an50pmpLinkULCIDStatPktTran.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLinkULCIDStatPktTran.setStatus(_A)
_An50pmpLinkULCIDStatPktRecv_Type=Integer32
_An50pmpLinkULCIDStatPktRecv_Object=MibTableColumn
an50pmpLinkULCIDStatPktRecv=_An50pmpLinkULCIDStatPktRecv_Object((1,3,6,1,4,1,10728,2,51,2,1,24),_An50pmpLinkULCIDStatPktRecv_Type())
an50pmpLinkULCIDStatPktRecv.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLinkULCIDStatPktRecv.setStatus(_A)
_An50pmpLinkUpTime_Type=TimeTicks
_An50pmpLinkUpTime_Object=MibTableColumn
an50pmpLinkUpTime=_An50pmpLinkUpTime_Object((1,3,6,1,4,1,10728,2,51,2,1,25),_An50pmpLinkUpTime_Type())
an50pmpLinkUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLinkUpTime.setStatus(_A)
_An50pmpLinkLostCount_Type=Integer32
_An50pmpLinkLostCount_Object=MibTableColumn
an50pmpLinkLostCount=_An50pmpLinkLostCount_Object((1,3,6,1,4,1,10728,2,51,2,1,26),_An50pmpLinkLostCount_Type())
an50pmpLinkLostCount.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLinkLostCount.setStatus(_A)
class _An50pmpCIDSaveConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('doNothing',1),('saveConfig',2)))
_An50pmpCIDSaveConfig_Type.__name__=_D
_An50pmpCIDSaveConfig_Object=MibScalar
an50pmpCIDSaveConfig=_An50pmpCIDSaveConfig_Object((1,3,6,1,4,1,10728,2,51,3),_An50pmpCIDSaveConfig_Type())
an50pmpCIDSaveConfig.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpCIDSaveConfig.setStatus(_A)
class _An50pmpLastModifiedCID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1023))
_An50pmpLastModifiedCID_Type.__name__=_D
_An50pmpLastModifiedCID_Object=MibScalar
an50pmpLastModifiedCID=_An50pmpLastModifiedCID_Object((1,3,6,1,4,1,10728,2,51,4),_An50pmpLastModifiedCID_Type())
an50pmpLastModifiedCID.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLastModifiedCID.setStatus(_A)
_An50pmpLastMissedSsMacAddress_Type=OctetString
_An50pmpLastMissedSsMacAddress_Object=MibScalar
an50pmpLastMissedSsMacAddress=_An50pmpLastMissedSsMacAddress_Object((1,3,6,1,4,1,10728,2,51,5),_An50pmpLastMissedSsMacAddress_Type())
an50pmpLastMissedSsMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLastMissedSsMacAddress.setStatus(_A)
_An50pmpLastRegisteredSsMacAddress_Type=OctetString
_An50pmpLastRegisteredSsMacAddress_Object=MibScalar
an50pmpLastRegisteredSsMacAddress=_An50pmpLastRegisteredSsMacAddress_Object((1,3,6,1,4,1,10728,2,51,6),_An50pmpLastRegisteredSsMacAddress_Type())
an50pmpLastRegisteredSsMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLastRegisteredSsMacAddress.setStatus(_A)
class _An50pmpLastSuccessfulID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1023))
_An50pmpLastSuccessfulID_Type.__name__=_D
_An50pmpLastSuccessfulID_Object=MibScalar
an50pmpLastSuccessfulID=_An50pmpLastSuccessfulID_Object((1,3,6,1,4,1,10728,2,51,7),_An50pmpLastSuccessfulID_Type())
an50pmpLastSuccessfulID.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpLastSuccessfulID.setStatus(_A)
_An50pmpLastDeniedSsMacAddress_Type=OctetString
_An50pmpLastDeniedSsMacAddress_Object=MibScalar
an50pmpLastDeniedSsMacAddress=_An50pmpLastDeniedSsMacAddress_Object((1,3,6,1,4,1,10728,2,51,8),_An50pmpLastDeniedSsMacAddress_Type())
an50pmpLastDeniedSsMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpLastDeniedSsMacAddress.setStatus(_A)
_An50pmpGroupTable_Object=MibTable
an50pmpGroupTable=_An50pmpGroupTable_Object((1,3,6,1,4,1,10728,2,51,9))
if mibBuilder.loadTexts:an50pmpGroupTable.setStatus(_A)
_An50pmpGroupEntry_Object=MibTableRow
an50pmpGroupEntry=_An50pmpGroupEntry_Object((1,3,6,1,4,1,10728,2,51,9,1))
an50pmpGroupEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:an50pmpGroupEntry.setStatus(_A)
class _An50pmpGroupId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_An50pmpGroupId_Type.__name__=_D
_An50pmpGroupId_Object=MibTableColumn
an50pmpGroupId=_An50pmpGroupId_Object((1,3,6,1,4,1,10728,2,51,9,1,1),_An50pmpGroupId_Type())
an50pmpGroupId.setMaxAccess(_H)
if mibBuilder.loadTexts:an50pmpGroupId.setStatus(_A)
class _An50pmpGroupName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_An50pmpGroupName_Type.__name__=_G
_An50pmpGroupName_Object=MibTableColumn
an50pmpGroupName=_An50pmpGroupName_Object((1,3,6,1,4,1,10728,2,51,9,1,2),_An50pmpGroupName_Type())
an50pmpGroupName.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpGroupName.setStatus(_A)
class _An50pmpGroupBSPortTagging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_An50pmpGroupBSPortTagging_Type.__name__=_D
_An50pmpGroupBSPortTagging_Object=MibTableColumn
an50pmpGroupBSPortTagging=_An50pmpGroupBSPortTagging_Object((1,3,6,1,4,1,10728,2,51,9,1,3),_An50pmpGroupBSPortTagging_Type())
an50pmpGroupBSPortTagging.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpGroupBSPortTagging.setStatus(_A)
class _An50pmpGroupVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_An50pmpGroupVlanId_Type.__name__=_D
_An50pmpGroupVlanId_Object=MibTableColumn
an50pmpGroupVlanId=_An50pmpGroupVlanId_Object((1,3,6,1,4,1,10728,2,51,9,1,4),_An50pmpGroupVlanId_Type())
an50pmpGroupVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpGroupVlanId.setStatus(_A)
class _An50pmpGroupDefaultPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_An50pmpGroupDefaultPriority_Type.__name__=_D
_An50pmpGroupDefaultPriority_Object=MibTableColumn
an50pmpGroupDefaultPriority=_An50pmpGroupDefaultPriority_Object((1,3,6,1,4,1,10728,2,51,9,1,5),_An50pmpGroupDefaultPriority_Type())
an50pmpGroupDefaultPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpGroupDefaultPriority.setStatus(_A)
class _An50pmpGroupBSPortEnabled_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('off',1),('on',2)))
_An50pmpGroupBSPortEnabled_Type.__name__=_D
_An50pmpGroupBSPortEnabled_Object=MibTableColumn
an50pmpGroupBSPortEnabled=_An50pmpGroupBSPortEnabled_Object((1,3,6,1,4,1,10728,2,51,9,1,6),_An50pmpGroupBSPortEnabled_Type())
an50pmpGroupBSPortEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpGroupBSPortEnabled.setStatus(_A)
class _An50pmpGroupQos_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_An50pmpGroupQos_Type.__name__=_D
_An50pmpGroupQos_Object=MibTableColumn
an50pmpGroupQos=_An50pmpGroupQos_Object((1,3,6,1,4,1,10728,2,51,9,1,7),_An50pmpGroupQos_Type())
an50pmpGroupQos.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpGroupQos.setStatus(_A)
class _An50pmpGroupRowStatus_Type(RowStatus):defaultValue=5
_An50pmpGroupRowStatus_Type.__name__=_I
_An50pmpGroupRowStatus_Object=MibTableColumn
an50pmpGroupRowStatus=_An50pmpGroupRowStatus_Object((1,3,6,1,4,1,10728,2,51,9,1,8),_An50pmpGroupRowStatus_Type())
an50pmpGroupRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpGroupRowStatus.setStatus(_A)
_An50pmpConnectionTable_Object=MibTable
an50pmpConnectionTable=_An50pmpConnectionTable_Object((1,3,6,1,4,1,10728,2,51,10))
if mibBuilder.loadTexts:an50pmpConnectionTable.setStatus(_A)
_An50pmpConnectionEntry_Object=MibTableRow
an50pmpConnectionEntry=_An50pmpConnectionEntry_Object((1,3,6,1,4,1,10728,2,51,10,1))
an50pmpConnectionEntry.setIndexNames((0,_B,_W))
if mibBuilder.loadTexts:an50pmpConnectionEntry.setStatus(_A)
class _An50pmpConnectionId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_An50pmpConnectionId_Type.__name__=_D
_An50pmpConnectionId_Object=MibTableColumn
an50pmpConnectionId=_An50pmpConnectionId_Object((1,3,6,1,4,1,10728,2,51,10,1,1),_An50pmpConnectionId_Type())
an50pmpConnectionId.setMaxAccess(_H)
if mibBuilder.loadTexts:an50pmpConnectionId.setStatus(_A)
class _An50pmpConnectionName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,15))
_An50pmpConnectionName_Type.__name__=_G
_An50pmpConnectionName_Object=MibTableColumn
an50pmpConnectionName=_An50pmpConnectionName_Object((1,3,6,1,4,1,10728,2,51,10,1,2),_An50pmpConnectionName_Type())
an50pmpConnectionName.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpConnectionName.setStatus(_A)
class _An50pmpConnectionPortTagging_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),(_V,2)))
_An50pmpConnectionPortTagging_Type.__name__=_D
_An50pmpConnectionPortTagging_Object=MibTableColumn
an50pmpConnectionPortTagging=_An50pmpConnectionPortTagging_Object((1,3,6,1,4,1,10728,2,51,10,1,3),_An50pmpConnectionPortTagging_Type())
an50pmpConnectionPortTagging.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpConnectionPortTagging.setStatus(_A)
class _An50pmpConnectionVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_An50pmpConnectionVlanId_Type.__name__=_D
_An50pmpConnectionVlanId_Object=MibTableColumn
an50pmpConnectionVlanId=_An50pmpConnectionVlanId_Object((1,3,6,1,4,1,10728,2,51,10,1,4),_An50pmpConnectionVlanId_Type())
an50pmpConnectionVlanId.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpConnectionVlanId.setStatus(_A)
class _An50pmpConnectionDefaultPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_An50pmpConnectionDefaultPriority_Type.__name__=_D
_An50pmpConnectionDefaultPriority_Object=MibTableColumn
an50pmpConnectionDefaultPriority=_An50pmpConnectionDefaultPriority_Object((1,3,6,1,4,1,10728,2,51,10,1,5),_An50pmpConnectionDefaultPriority_Type())
an50pmpConnectionDefaultPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpConnectionDefaultPriority.setStatus(_A)
class _An50pmpConnectionParentLink_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_An50pmpConnectionParentLink_Type.__name__=_D
_An50pmpConnectionParentLink_Object=MibTableColumn
an50pmpConnectionParentLink=_An50pmpConnectionParentLink_Object((1,3,6,1,4,1,10728,2,51,10,1,6),_An50pmpConnectionParentLink_Type())
an50pmpConnectionParentLink.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpConnectionParentLink.setStatus(_A)
class _An50pmpConnectionParentGroup_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_An50pmpConnectionParentGroup_Type.__name__=_D
_An50pmpConnectionParentGroup_Object=MibTableColumn
an50pmpConnectionParentGroup=_An50pmpConnectionParentGroup_Object((1,3,6,1,4,1,10728,2,51,10,1,7),_An50pmpConnectionParentGroup_Type())
an50pmpConnectionParentGroup.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpConnectionParentGroup.setStatus(_A)
class _An50pmpConnectionDLQoS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_An50pmpConnectionDLQoS_Type.__name__=_D
_An50pmpConnectionDLQoS_Object=MibTableColumn
an50pmpConnectionDLQoS=_An50pmpConnectionDLQoS_Object((1,3,6,1,4,1,10728,2,51,10,1,8),_An50pmpConnectionDLQoS_Type())
an50pmpConnectionDLQoS.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpConnectionDLQoS.setStatus(_A)
class _An50pmpConnectionULQoS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_An50pmpConnectionULQoS_Type.__name__=_D
_An50pmpConnectionULQoS_Object=MibTableColumn
an50pmpConnectionULQoS=_An50pmpConnectionULQoS_Object((1,3,6,1,4,1,10728,2,51,10,1,9),_An50pmpConnectionULQoS_Type())
an50pmpConnectionULQoS.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpConnectionULQoS.setStatus(_A)
class _An50pmpConnectionRowStatus_Type(RowStatus):defaultValue=5
_An50pmpConnectionRowStatus_Type.__name__=_I
_An50pmpConnectionRowStatus_Object=MibTableColumn
an50pmpConnectionRowStatus=_An50pmpConnectionRowStatus_Object((1,3,6,1,4,1,10728,2,51,10,1,10),_An50pmpConnectionRowStatus_Type())
an50pmpConnectionRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:an50pmpConnectionRowStatus.setStatus(_A)
_An50pmpGroupStatusTable_Object=MibTable
an50pmpGroupStatusTable=_An50pmpGroupStatusTable_Object((1,3,6,1,4,1,10728,2,51,11))
if mibBuilder.loadTexts:an50pmpGroupStatusTable.setStatus(_A)
_An50pmpGroupStatusEntry_Object=MibTableRow
an50pmpGroupStatusEntry=_An50pmpGroupStatusEntry_Object((1,3,6,1,4,1,10728,2,51,11,1))
an50pmpGroupStatusEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:an50pmpGroupStatusEntry.setStatus(_A)
class _An50pmpGroupStatusId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_An50pmpGroupStatusId_Type.__name__=_D
_An50pmpGroupStatusId_Object=MibTableColumn
an50pmpGroupStatusId=_An50pmpGroupStatusId_Object((1,3,6,1,4,1,10728,2,51,11,1,1),_An50pmpGroupStatusId_Type())
an50pmpGroupStatusId.setMaxAccess(_H)
if mibBuilder.loadTexts:an50pmpGroupStatusId.setStatus(_A)
_An50pmpGroupStatusDLPacketsDiscards_Type=Counter32
_An50pmpGroupStatusDLPacketsDiscards_Object=MibTableColumn
an50pmpGroupStatusDLPacketsDiscards=_An50pmpGroupStatusDLPacketsDiscards_Object((1,3,6,1,4,1,10728,2,51,11,1,2),_An50pmpGroupStatusDLPacketsDiscards_Type())
an50pmpGroupStatusDLPacketsDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpGroupStatusDLPacketsDiscards.setStatus(_A)
_An50pmpGroupStatusDLPacketsTx_Type=Counter32
_An50pmpGroupStatusDLPacketsTx_Object=MibTableColumn
an50pmpGroupStatusDLPacketsTx=_An50pmpGroupStatusDLPacketsTx_Object((1,3,6,1,4,1,10728,2,51,11,1,3),_An50pmpGroupStatusDLPacketsTx_Type())
an50pmpGroupStatusDLPacketsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpGroupStatusDLPacketsTx.setStatus(_A)
_An50pmpGroupStatusDLPacketsRx_Type=Counter32
_An50pmpGroupStatusDLPacketsRx_Object=MibTableColumn
an50pmpGroupStatusDLPacketsRx=_An50pmpGroupStatusDLPacketsRx_Object((1,3,6,1,4,1,10728,2,51,11,1,4),_An50pmpGroupStatusDLPacketsRx_Type())
an50pmpGroupStatusDLPacketsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpGroupStatusDLPacketsRx.setStatus(_A)
_An50pmpGroupStatusULPacketsDiscards_Type=Counter32
_An50pmpGroupStatusULPacketsDiscards_Object=MibTableColumn
an50pmpGroupStatusULPacketsDiscards=_An50pmpGroupStatusULPacketsDiscards_Object((1,3,6,1,4,1,10728,2,51,11,1,5),_An50pmpGroupStatusULPacketsDiscards_Type())
an50pmpGroupStatusULPacketsDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpGroupStatusULPacketsDiscards.setStatus(_A)
_An50pmpGroupStatusULPacketsTx_Type=Counter32
_An50pmpGroupStatusULPacketsTx_Object=MibTableColumn
an50pmpGroupStatusULPacketsTx=_An50pmpGroupStatusULPacketsTx_Object((1,3,6,1,4,1,10728,2,51,11,1,6),_An50pmpGroupStatusULPacketsTx_Type())
an50pmpGroupStatusULPacketsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpGroupStatusULPacketsTx.setStatus(_A)
_An50pmpGroupStatusULPacketsRx_Type=Counter32
_An50pmpGroupStatusULPacketsRx_Object=MibTableColumn
an50pmpGroupStatusULPacketsRx=_An50pmpGroupStatusULPacketsRx_Object((1,3,6,1,4,1,10728,2,51,11,1,7),_An50pmpGroupStatusULPacketsRx_Type())
an50pmpGroupStatusULPacketsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpGroupStatusULPacketsRx.setStatus(_A)
_An50pmpConnectionStatusTable_Object=MibTable
an50pmpConnectionStatusTable=_An50pmpConnectionStatusTable_Object((1,3,6,1,4,1,10728,2,51,12))
if mibBuilder.loadTexts:an50pmpConnectionStatusTable.setStatus(_A)
_An50pmpConnectionStatusEntry_Object=MibTableRow
an50pmpConnectionStatusEntry=_An50pmpConnectionStatusEntry_Object((1,3,6,1,4,1,10728,2,51,12,1))
an50pmpConnectionStatusEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:an50pmpConnectionStatusEntry.setStatus(_A)
class _An50pmpConnectionStatusId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_An50pmpConnectionStatusId_Type.__name__=_D
_An50pmpConnectionStatusId_Object=MibTableColumn
an50pmpConnectionStatusId=_An50pmpConnectionStatusId_Object((1,3,6,1,4,1,10728,2,51,12,1,1),_An50pmpConnectionStatusId_Type())
an50pmpConnectionStatusId.setMaxAccess(_H)
if mibBuilder.loadTexts:an50pmpConnectionStatusId.setStatus(_A)
_An50pmpConnectionStatusDLPacketsDiscards_Type=Counter32
_An50pmpConnectionStatusDLPacketsDiscards_Object=MibTableColumn
an50pmpConnectionStatusDLPacketsDiscards=_An50pmpConnectionStatusDLPacketsDiscards_Object((1,3,6,1,4,1,10728,2,51,12,1,2),_An50pmpConnectionStatusDLPacketsDiscards_Type())
an50pmpConnectionStatusDLPacketsDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpConnectionStatusDLPacketsDiscards.setStatus(_A)
_An50pmpConnectionStatusDLPacketsTx_Type=Counter32
_An50pmpConnectionStatusDLPacketsTx_Object=MibTableColumn
an50pmpConnectionStatusDLPacketsTx=_An50pmpConnectionStatusDLPacketsTx_Object((1,3,6,1,4,1,10728,2,51,12,1,3),_An50pmpConnectionStatusDLPacketsTx_Type())
an50pmpConnectionStatusDLPacketsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpConnectionStatusDLPacketsTx.setStatus(_A)
_An50pmpConnectionStatusDLPacketsRx_Type=Counter32
_An50pmpConnectionStatusDLPacketsRx_Object=MibTableColumn
an50pmpConnectionStatusDLPacketsRx=_An50pmpConnectionStatusDLPacketsRx_Object((1,3,6,1,4,1,10728,2,51,12,1,4),_An50pmpConnectionStatusDLPacketsRx_Type())
an50pmpConnectionStatusDLPacketsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpConnectionStatusDLPacketsRx.setStatus(_A)
_An50pmpConnectionStatusULPacketsDiscards_Type=Counter32
_An50pmpConnectionStatusULPacketsDiscards_Object=MibTableColumn
an50pmpConnectionStatusULPacketsDiscards=_An50pmpConnectionStatusULPacketsDiscards_Object((1,3,6,1,4,1,10728,2,51,12,1,5),_An50pmpConnectionStatusULPacketsDiscards_Type())
an50pmpConnectionStatusULPacketsDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpConnectionStatusULPacketsDiscards.setStatus(_A)
_An50pmpConnectionStatusULPacketsTx_Type=Counter32
_An50pmpConnectionStatusULPacketsTx_Object=MibTableColumn
an50pmpConnectionStatusULPacketsTx=_An50pmpConnectionStatusULPacketsTx_Object((1,3,6,1,4,1,10728,2,51,12,1,6),_An50pmpConnectionStatusULPacketsTx_Type())
an50pmpConnectionStatusULPacketsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpConnectionStatusULPacketsTx.setStatus(_A)
_An50pmpConnectionStatusULPacketsRx_Type=Counter32
_An50pmpConnectionStatusULPacketsRx_Object=MibTableColumn
an50pmpConnectionStatusULPacketsRx=_An50pmpConnectionStatusULPacketsRx_Object((1,3,6,1,4,1,10728,2,51,12,1,7),_An50pmpConnectionStatusULPacketsRx_Type())
an50pmpConnectionStatusULPacketsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:an50pmpConnectionStatusULPacketsRx.setStatus(_A)
an50PMPObjectGroup=ObjectGroup((1,3,6,1,4,1,10728,2,51,13))
an50PMPObjectGroup.setObjects(*((_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab)))
if mibBuilder.loadTexts:an50PMPObjectGroup.setStatus(_A)
an50PMPObsoleteObjectGroup=ObjectGroup((1,3,6,1,4,1,10728,2,51,14))
an50PMPObsoleteObjectGroup.setObjects(*((_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj)))
if mibBuilder.loadTexts:an50PMPObsoleteObjectGroup.setStatus(_F)
mibBuilder.exportSymbols(_B,**{'redlineAN50PMPV2':redlineAN50PMPV2,'an50pmpLinkTable':an50pmpLinkTable,'an50pmpLinkEntry':an50pmpLinkEntry,_J:an50pmpLinkID,_Z:an50pmpLinkName,_Ac:an50pmpLinkGroupId,_a:an50pmpLinkPeerMac,_b:an50pmpLinkMaxDLBurstRate,_c:an50pmpLinkMaxULBurstRate,_Ad:an50pmpLinkMaxHost,_Ae:an50pmpLinkCIDDLCIR,_Af:an50pmpLinkCIDDLPIR,_Ag:an50pmpLinkCIDULCIR,_Ah:an50pmpLinkCIDULPIR,_Ai:an50pmpLinkDLQoS,_Aj:an50pmpLinkULQoS,_e:an50pmpLinkRowStatus,_d:an50pmpLinkEncryptionKey,'an50pmpLinkStatusTable':an50pmpLinkStatusTable,'an50pmpLinkStatusEntry':an50pmpLinkStatusEntry,_K:an50pmpLinkStatusID,_f:an50pmpLinkStatus,_g:an50pmpLinkStatusCode,_h:an50pmpLinkRegConn,_i:an50pmpLinkDLBurstRate,_j:an50pmpLinkDLRSSI,_k:an50pmpLinkDLSINADR,_l:an50pmpLinkDLStatLostFrm,_m:an50pmpLinkDLStatBlksTot,_n:an50pmpLinkDLStatBlksRetr,_o:an50pmpLinkDLStatBlksDisc,_p:an50pmpLinkDLCIDStatPktDisc,_q:an50pmpLinkDLCIDStatPktTran,_r:an50pmpLinkDLCIDStatPktRecv,_s:an50pmpLinkULBurstRate,_t:an50pmpLinkULRSSI,_u:an50pmpLinkULSINADR,_v:an50pmpLinkULStatLostFrm,_w:an50pmpLinkULStatBlksTot,_x:an50pmpLinkULStatBlksRetr,_y:an50pmpLinkULStatBlksDisc,_z:an50pmpLinkULCIDStatPktDisc,_A0:an50pmpLinkULCIDStatPktTran,_A1:an50pmpLinkULCIDStatPktRecv,_A2:an50pmpLinkUpTime,_A3:an50pmpLinkLostCount,_A4:an50pmpCIDSaveConfig,_A5:an50pmpLastModifiedCID,_A6:an50pmpLastMissedSsMacAddress,_A7:an50pmpLastRegisteredSsMacAddress,_A8:an50pmpLastSuccessfulID,_A9:an50pmpLastDeniedSsMacAddress,'an50pmpGroupTable':an50pmpGroupTable,'an50pmpGroupEntry':an50pmpGroupEntry,_T:an50pmpGroupId,_AA:an50pmpGroupName,_AB:an50pmpGroupBSPortTagging,_AC:an50pmpGroupVlanId,_AD:an50pmpGroupDefaultPriority,_AE:an50pmpGroupBSPortEnabled,_AF:an50pmpGroupQos,_AG:an50pmpGroupRowStatus,'an50pmpConnectionTable':an50pmpConnectionTable,'an50pmpConnectionEntry':an50pmpConnectionEntry,_W:an50pmpConnectionId,_AH:an50pmpConnectionName,_AI:an50pmpConnectionPortTagging,_AJ:an50pmpConnectionVlanId,_AK:an50pmpConnectionDefaultPriority,_AL:an50pmpConnectionParentLink,_AM:an50pmpConnectionParentGroup,_AN:an50pmpConnectionDLQoS,_AO:an50pmpConnectionULQoS,_AP:an50pmpConnectionRowStatus,'an50pmpGroupStatusTable':an50pmpGroupStatusTable,'an50pmpGroupStatusEntry':an50pmpGroupStatusEntry,_X:an50pmpGroupStatusId,_AQ:an50pmpGroupStatusDLPacketsDiscards,_AR:an50pmpGroupStatusDLPacketsTx,_AS:an50pmpGroupStatusDLPacketsRx,_AT:an50pmpGroupStatusULPacketsDiscards,_AU:an50pmpGroupStatusULPacketsTx,_AV:an50pmpGroupStatusULPacketsRx,'an50pmpConnectionStatusTable':an50pmpConnectionStatusTable,'an50pmpConnectionStatusEntry':an50pmpConnectionStatusEntry,_Y:an50pmpConnectionStatusId,_AW:an50pmpConnectionStatusDLPacketsDiscards,_AX:an50pmpConnectionStatusDLPacketsTx,_AY:an50pmpConnectionStatusDLPacketsRx,_AZ:an50pmpConnectionStatusULPacketsDiscards,_Aa:an50pmpConnectionStatusULPacketsTx,_Ab:an50pmpConnectionStatusULPacketsRx,'an50PMPObjectGroup':an50PMPObjectGroup,'an50PMPObsoleteObjectGroup':an50PMPObsoleteObjectGroup})