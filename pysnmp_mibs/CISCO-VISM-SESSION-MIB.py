_AH='ciscoVismRudpSessionStatGrp'
_AG='ciscoVismRudpSessionGrp'
_AF='ciscoVismSessionGrp'
_AE='ciscoVismSessionSetGrp'
_AD='vismRudpSessionRetransPkts'
_AC='vismRudpSessionDiscardPkts'
_AB='vismRudpSessionDataRcvdPkts'
_AA='vismRudpSessionDataSentPkts'
_A9='vismRudpSessionRcvdBytes'
_A8='vismRudpSessionSentBytes'
_A7='vismRudpSessionRcvdPackets'
_A6='vismRudpSessionSentPackets'
_A5='vismRudpSessionRcvdOutSeqs'
_A4='vismRudpSessionRcvdInSeqs'
_A3='vismRudpSessionRcvdAutoResets'
_A2='vismRudpSessionAutoResets'
_A1='vismRudpSessionRmtGwIp'
_A0='vismRudpSessionType'
_z='vismRudpSessionTransStateTmout'
_y='vismRudpSessionNullSegTmout'
_x='vismRudpSessionMaxOutOfSeq'
_w='vismRudpSessionCumAckTmout'
_v='vismRudpSessionMaxCumAck'
_u='vismRudpSessionMaxRetrans'
_t='vismRudpSessionRetransTmout'
_s='vismRudpSessionMaxAutoReset'
_r='vismRudpSessionMaxSegSize'
_q='vismRudpSessionSyncAttempts'
_p='vismRudpSessionMaxWindow'
_o='vismRudpSessionRmtPort'
_n='vismRudpSessionRmtIp'
_m='vismRudpSessionLocalPort'
_l='vismRudpSessionLocalIp'
_k='vismRudpSessionCurrSession'
_j='vismRudpSessionState'
_i='vismRudpSessionPriority'
_h='vismRudpSessionCnfRowStatus'
_g='vismRudpSessionGrpNum'
_f='vismSessionGrpMgcName'
_e='vismSessionGrpSwitchSuccesses'
_d='vismSessionGrpSwitchFails'
_c='vismSessionGrpTotalSessions'
_b='vismSessionGrpCurrSession'
_a='vismSessionGrpState'
_Z='vismSessionGrpRowStatus'
_Y='vismSessionGrpSetNum'
_X='vismSessionSetFaultTolerant'
_W='vismSessionSetSwitchSuccesses'
_V='vismSessionSetSwitchFails'
_U='vismSessionSetActiveGrp'
_T='vismSessionSetTotalGrps'
_S='vismSessionSetState'
_R='vismSessionSetRowStatus'
_Q='milliseconds'
_P='DisplayString'
_O='packets'
_N='vismRudpSessionStatNum'
_M='vismRudpSessionNum'
_L='vismSessionGrpNum'
_K='unknown'
_J='oos'
_I='destroy'
_H='createAndGo'
_G='active'
_F='vismSessionSetNum'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='CISCO-VISM-SESSION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
voice,=mibBuilder.importSymbols('BASIS-MIB','voice')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_P,'PhysAddress','TextualConvention','TruthValue')
ciscoVismSessionMIB=ModuleIdentity((1,3,6,1,4,1,351,150,95))
if mibBuilder.loadTexts:ciscoVismSessionMIB.setRevisions(('2004-02-26 00:00','2003-07-17 00:00'))
_VismSessionGrp_ObjectIdentity=ObjectIdentity
vismSessionGrp=_VismSessionGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,5,11))
_VismSessionSetTable_Object=MibTable
vismSessionSetTable=_VismSessionSetTable_Object((1,3,6,1,4,1,351,110,5,5,11,1))
if mibBuilder.loadTexts:vismSessionSetTable.setStatus(_A)
_VismSessionSetEntry_Object=MibTableRow
vismSessionSetEntry=_VismSessionSetEntry_Object((1,3,6,1,4,1,351,110,5,5,11,1,1))
vismSessionSetEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:vismSessionSetEntry.setStatus(_A)
class _VismSessionSetNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_VismSessionSetNum_Type.__name__=_C
_VismSessionSetNum_Object=MibTableColumn
vismSessionSetNum=_VismSessionSetNum_Object((1,3,6,1,4,1,351,110,5,5,11,1,1,1),_VismSessionSetNum_Type())
vismSessionSetNum.setMaxAccess(_D)
if mibBuilder.loadTexts:vismSessionSetNum.setStatus(_A)
class _VismSessionSetRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,6)));namedValues=NamedValues(*((_G,1),(_H,4),(_I,6)))
_VismSessionSetRowStatus_Type.__name__=_C
_VismSessionSetRowStatus_Object=MibTableColumn
vismSessionSetRowStatus=_VismSessionSetRowStatus_Object((1,3,6,1,4,1,351,110,5,5,11,1,1,2),_VismSessionSetRowStatus_Type())
vismSessionSetRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:vismSessionSetRowStatus.setStatus(_A)
class _VismSessionSetState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('idle',1),(_J,2),('activeIs',3),('standbyIs',4),('fullIs',5),(_K,6)))
_VismSessionSetState_Type.__name__=_C
_VismSessionSetState_Object=MibTableColumn
vismSessionSetState=_VismSessionSetState_Object((1,3,6,1,4,1,351,110,5,5,11,1,1,3),_VismSessionSetState_Type())
vismSessionSetState.setMaxAccess(_D)
if mibBuilder.loadTexts:vismSessionSetState.setStatus(_A)
class _VismSessionSetTotalGrps_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismSessionSetTotalGrps_Type.__name__=_C
_VismSessionSetTotalGrps_Object=MibTableColumn
vismSessionSetTotalGrps=_VismSessionSetTotalGrps_Object((1,3,6,1,4,1,351,110,5,5,11,1,1,4),_VismSessionSetTotalGrps_Type())
vismSessionSetTotalGrps.setMaxAccess(_D)
if mibBuilder.loadTexts:vismSessionSetTotalGrps.setStatus(_A)
class _VismSessionSetActiveGrp_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismSessionSetActiveGrp_Type.__name__=_C
_VismSessionSetActiveGrp_Object=MibTableColumn
vismSessionSetActiveGrp=_VismSessionSetActiveGrp_Object((1,3,6,1,4,1,351,110,5,5,11,1,1,5),_VismSessionSetActiveGrp_Type())
vismSessionSetActiveGrp.setMaxAccess(_D)
if mibBuilder.loadTexts:vismSessionSetActiveGrp.setStatus(_A)
_VismSessionSetSwitchFails_Type=Counter32
_VismSessionSetSwitchFails_Object=MibTableColumn
vismSessionSetSwitchFails=_VismSessionSetSwitchFails_Object((1,3,6,1,4,1,351,110,5,5,11,1,1,6),_VismSessionSetSwitchFails_Type())
vismSessionSetSwitchFails.setMaxAccess(_D)
if mibBuilder.loadTexts:vismSessionSetSwitchFails.setStatus(_A)
_VismSessionSetSwitchSuccesses_Type=Counter32
_VismSessionSetSwitchSuccesses_Object=MibTableColumn
vismSessionSetSwitchSuccesses=_VismSessionSetSwitchSuccesses_Object((1,3,6,1,4,1,351,110,5,5,11,1,1,7),_VismSessionSetSwitchSuccesses_Type())
vismSessionSetSwitchSuccesses.setMaxAccess(_D)
if mibBuilder.loadTexts:vismSessionSetSwitchSuccesses.setStatus(_A)
_VismSessionSetFaultTolerant_Type=TruthValue
_VismSessionSetFaultTolerant_Object=MibTableColumn
vismSessionSetFaultTolerant=_VismSessionSetFaultTolerant_Object((1,3,6,1,4,1,351,110,5,5,11,1,1,8),_VismSessionSetFaultTolerant_Type())
vismSessionSetFaultTolerant.setMaxAccess(_E)
if mibBuilder.loadTexts:vismSessionSetFaultTolerant.setStatus(_A)
_VismSessionGrpTable_Object=MibTable
vismSessionGrpTable=_VismSessionGrpTable_Object((1,3,6,1,4,1,351,110,5,5,11,2))
if mibBuilder.loadTexts:vismSessionGrpTable.setStatus(_A)
_VismSessionGrpEntry_Object=MibTableRow
vismSessionGrpEntry=_VismSessionGrpEntry_Object((1,3,6,1,4,1,351,110,5,5,11,2,1))
vismSessionGrpEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:vismSessionGrpEntry.setStatus(_A)
class _VismSessionGrpNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_VismSessionGrpNum_Type.__name__=_C
_VismSessionGrpNum_Object=MibTableColumn
vismSessionGrpNum=_VismSessionGrpNum_Object((1,3,6,1,4,1,351,110,5,5,11,2,1,1),_VismSessionGrpNum_Type())
vismSessionGrpNum.setMaxAccess(_D)
if mibBuilder.loadTexts:vismSessionGrpNum.setStatus(_A)
class _VismSessionGrpSetNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismSessionGrpSetNum_Type.__name__=_C
_VismSessionGrpSetNum_Object=MibTableColumn
vismSessionGrpSetNum=_VismSessionGrpSetNum_Object((1,3,6,1,4,1,351,110,5,5,11,2,1,2),_VismSessionGrpSetNum_Type())
vismSessionGrpSetNum.setMaxAccess(_E)
if mibBuilder.loadTexts:vismSessionGrpSetNum.setStatus(_A)
class _VismSessionGrpRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,6)));namedValues=NamedValues(*((_G,1),(_H,4),(_I,6)))
_VismSessionGrpRowStatus_Type.__name__=_C
_VismSessionGrpRowStatus_Object=MibTableColumn
vismSessionGrpRowStatus=_VismSessionGrpRowStatus_Object((1,3,6,1,4,1,351,110,5,5,11,2,1,3),_VismSessionGrpRowStatus_Type())
vismSessionGrpRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:vismSessionGrpRowStatus.setStatus(_A)
class _VismSessionGrpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('idle',1),(_J,2),('is',3),(_K,4)))
_VismSessionGrpState_Type.__name__=_C
_VismSessionGrpState_Object=MibTableColumn
vismSessionGrpState=_VismSessionGrpState_Object((1,3,6,1,4,1,351,110,5,5,11,2,1,4),_VismSessionGrpState_Type())
vismSessionGrpState.setMaxAccess(_D)
if mibBuilder.loadTexts:vismSessionGrpState.setStatus(_A)
class _VismSessionGrpCurrSession_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismSessionGrpCurrSession_Type.__name__=_C
_VismSessionGrpCurrSession_Object=MibTableColumn
vismSessionGrpCurrSession=_VismSessionGrpCurrSession_Object((1,3,6,1,4,1,351,110,5,5,11,2,1,5),_VismSessionGrpCurrSession_Type())
vismSessionGrpCurrSession.setMaxAccess(_D)
if mibBuilder.loadTexts:vismSessionGrpCurrSession.setStatus(_A)
class _VismSessionGrpTotalSessions_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismSessionGrpTotalSessions_Type.__name__=_C
_VismSessionGrpTotalSessions_Object=MibTableColumn
vismSessionGrpTotalSessions=_VismSessionGrpTotalSessions_Object((1,3,6,1,4,1,351,110,5,5,11,2,1,6),_VismSessionGrpTotalSessions_Type())
vismSessionGrpTotalSessions.setMaxAccess(_D)
if mibBuilder.loadTexts:vismSessionGrpTotalSessions.setStatus(_A)
_VismSessionGrpSwitchFails_Type=Counter32
_VismSessionGrpSwitchFails_Object=MibTableColumn
vismSessionGrpSwitchFails=_VismSessionGrpSwitchFails_Object((1,3,6,1,4,1,351,110,5,5,11,2,1,7),_VismSessionGrpSwitchFails_Type())
vismSessionGrpSwitchFails.setMaxAccess(_D)
if mibBuilder.loadTexts:vismSessionGrpSwitchFails.setStatus(_A)
_VismSessionGrpSwitchSuccesses_Type=Counter32
_VismSessionGrpSwitchSuccesses_Object=MibTableColumn
vismSessionGrpSwitchSuccesses=_VismSessionGrpSwitchSuccesses_Object((1,3,6,1,4,1,351,110,5,5,11,2,1,8),_VismSessionGrpSwitchSuccesses_Type())
vismSessionGrpSwitchSuccesses.setMaxAccess(_D)
if mibBuilder.loadTexts:vismSessionGrpSwitchSuccesses.setStatus(_A)
class _VismSessionGrpMgcName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_VismSessionGrpMgcName_Type.__name__=_P
_VismSessionGrpMgcName_Object=MibTableColumn
vismSessionGrpMgcName=_VismSessionGrpMgcName_Object((1,3,6,1,4,1,351,110,5,5,11,2,1,9),_VismSessionGrpMgcName_Type())
vismSessionGrpMgcName.setMaxAccess(_E)
if mibBuilder.loadTexts:vismSessionGrpMgcName.setStatus(_A)
_VismRudpSessionCnfTable_Object=MibTable
vismRudpSessionCnfTable=_VismRudpSessionCnfTable_Object((1,3,6,1,4,1,351,110,5,5,11,3))
if mibBuilder.loadTexts:vismRudpSessionCnfTable.setStatus(_A)
_VismRudpSessionCnfEntry_Object=MibTableRow
vismRudpSessionCnfEntry=_VismRudpSessionCnfEntry_Object((1,3,6,1,4,1,351,110,5,5,11,3,1))
vismRudpSessionCnfEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:vismRudpSessionCnfEntry.setStatus(_A)
class _VismRudpSessionNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_VismRudpSessionNum_Type.__name__=_C
_VismRudpSessionNum_Object=MibTableColumn
vismRudpSessionNum=_VismRudpSessionNum_Object((1,3,6,1,4,1,351,110,5,5,11,3,1,1),_VismRudpSessionNum_Type())
vismRudpSessionNum.setMaxAccess(_D)
if mibBuilder.loadTexts:vismRudpSessionNum.setStatus(_A)
class _VismRudpSessionGrpNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_VismRudpSessionGrpNum_Type.__name__=_C
_VismRudpSessionGrpNum_Object=MibTableColumn
vismRudpSessionGrpNum=_VismRudpSessionGrpNum_Object((1,3,6,1,4,1,351,110,5,5,11,3,1,2),_VismRudpSessionGrpNum_Type())
vismRudpSessionGrpNum.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRudpSessionGrpNum.setStatus(_A)
class _VismRudpSessionCnfRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,4,6)));namedValues=NamedValues(*((_G,1),(_H,4),(_I,6)))
_VismRudpSessionCnfRowStatus_Type.__name__=_C
_VismRudpSessionCnfRowStatus_Object=MibTableColumn
vismRudpSessionCnfRowStatus=_VismRudpSessionCnfRowStatus_Object((1,3,6,1,4,1,351,110,5,5,11,3,1,3),_VismRudpSessionCnfRowStatus_Type())
vismRudpSessionCnfRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRudpSessionCnfRowStatus.setStatus(_A)
class _VismRudpSessionPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_VismRudpSessionPriority_Type.__name__=_C
_VismRudpSessionPriority_Object=MibTableColumn
vismRudpSessionPriority=_VismRudpSessionPriority_Object((1,3,6,1,4,1,351,110,5,5,11,3,1,4),_VismRudpSessionPriority_Type())
vismRudpSessionPriority.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRudpSessionPriority.setStatus(_A)
class _VismRudpSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_J,1),('is',2),(_K,3)))
_VismRudpSessionState_Type.__name__=_C
_VismRudpSessionState_Object=MibTableColumn
vismRudpSessionState=_VismRudpSessionState_Object((1,3,6,1,4,1,351,110,5,5,11,3,1,5),_VismRudpSessionState_Type())
vismRudpSessionState.setMaxAccess(_D)
if mibBuilder.loadTexts:vismRudpSessionState.setStatus(_A)
class _VismRudpSessionCurrSession_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismRudpSessionCurrSession_Type.__name__=_C
_VismRudpSessionCurrSession_Object=MibTableColumn
vismRudpSessionCurrSession=_VismRudpSessionCurrSession_Object((1,3,6,1,4,1,351,110,5,5,11,3,1,6),_VismRudpSessionCurrSession_Type())
vismRudpSessionCurrSession.setMaxAccess(_D)
if mibBuilder.loadTexts:vismRudpSessionCurrSession.setStatus(_A)
_VismRudpSessionLocalIp_Type=IpAddress
_VismRudpSessionLocalIp_Object=MibTableColumn
vismRudpSessionLocalIp=_VismRudpSessionLocalIp_Object((1,3,6,1,4,1,351,110,5,5,11,3,1,7),_VismRudpSessionLocalIp_Type())
vismRudpSessionLocalIp.setMaxAccess(_D)
if mibBuilder.loadTexts:vismRudpSessionLocalIp.setStatus(_A)
class _VismRudpSessionLocalPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1124,65535))
_VismRudpSessionLocalPort_Type.__name__=_C
_VismRudpSessionLocalPort_Object=MibTableColumn
vismRudpSessionLocalPort=_VismRudpSessionLocalPort_Object((1,3,6,1,4,1,351,110,5,5,11,3,1,8),_VismRudpSessionLocalPort_Type())
vismRudpSessionLocalPort.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRudpSessionLocalPort.setStatus(_A)
_VismRudpSessionRmtIp_Type=IpAddress
_VismRudpSessionRmtIp_Object=MibTableColumn
vismRudpSessionRmtIp=_VismRudpSessionRmtIp_Object((1,3,6,1,4,1,351,110,5,5,11,3,1,9),_VismRudpSessionRmtIp_Type())
vismRudpSessionRmtIp.setMaxAccess(_D)
if mibBuilder.loadTexts:vismRudpSessionRmtIp.setStatus(_A)
class _VismRudpSessionRmtPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1124,65535))
_VismRudpSessionRmtPort_Type.__name__=_C
_VismRudpSessionRmtPort_Object=MibTableColumn
vismRudpSessionRmtPort=_VismRudpSessionRmtPort_Object((1,3,6,1,4,1,351,110,5,5,11,3,1,10),_VismRudpSessionRmtPort_Type())
vismRudpSessionRmtPort.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRudpSessionRmtPort.setStatus(_A)
class _VismRudpSessionMaxWindow_Type(Integer32):defaultValue=32;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_VismRudpSessionMaxWindow_Type.__name__=_C
_VismRudpSessionMaxWindow_Object=MibTableColumn
vismRudpSessionMaxWindow=_VismRudpSessionMaxWindow_Object((1,3,6,1,4,1,351,110,5,5,11,3,1,11),_VismRudpSessionMaxWindow_Type())
vismRudpSessionMaxWindow.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRudpSessionMaxWindow.setStatus(_A)
class _VismRudpSessionSyncAttempts_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_VismRudpSessionSyncAttempts_Type.__name__=_C
_VismRudpSessionSyncAttempts_Object=MibTableColumn
vismRudpSessionSyncAttempts=_VismRudpSessionSyncAttempts_Object((1,3,6,1,4,1,351,110,5,5,11,3,1,12),_VismRudpSessionSyncAttempts_Type())
vismRudpSessionSyncAttempts.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRudpSessionSyncAttempts.setStatus(_A)
class _VismRudpSessionMaxSegSize_Type(Integer32):defaultValue=384;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,65535))
_VismRudpSessionMaxSegSize_Type.__name__=_C
_VismRudpSessionMaxSegSize_Object=MibTableColumn
vismRudpSessionMaxSegSize=_VismRudpSessionMaxSegSize_Object((1,3,6,1,4,1,351,110,5,5,11,3,1,13),_VismRudpSessionMaxSegSize_Type())
vismRudpSessionMaxSegSize.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRudpSessionMaxSegSize.setStatus(_A)
if mibBuilder.loadTexts:vismRudpSessionMaxSegSize.setUnits('bytes')
class _VismRudpSessionMaxAutoReset_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VismRudpSessionMaxAutoReset_Type.__name__=_C
_VismRudpSessionMaxAutoReset_Object=MibTableColumn
vismRudpSessionMaxAutoReset=_VismRudpSessionMaxAutoReset_Object((1,3,6,1,4,1,351,110,5,5,11,3,1,14),_VismRudpSessionMaxAutoReset_Type())
vismRudpSessionMaxAutoReset.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRudpSessionMaxAutoReset.setStatus(_A)
class _VismRudpSessionRetransTmout_Type(Integer32):defaultValue=600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,65535))
_VismRudpSessionRetransTmout_Type.__name__=_C
_VismRudpSessionRetransTmout_Object=MibTableColumn
vismRudpSessionRetransTmout=_VismRudpSessionRetransTmout_Object((1,3,6,1,4,1,351,110,5,5,11,3,1,15),_VismRudpSessionRetransTmout_Type())
vismRudpSessionRetransTmout.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRudpSessionRetransTmout.setStatus(_A)
if mibBuilder.loadTexts:vismRudpSessionRetransTmout.setUnits(_Q)
class _VismRudpSessionMaxRetrans_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VismRudpSessionMaxRetrans_Type.__name__=_C
_VismRudpSessionMaxRetrans_Object=MibTableColumn
vismRudpSessionMaxRetrans=_VismRudpSessionMaxRetrans_Object((1,3,6,1,4,1,351,110,5,5,11,3,1,16),_VismRudpSessionMaxRetrans_Type())
vismRudpSessionMaxRetrans.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRudpSessionMaxRetrans.setStatus(_A)
class _VismRudpSessionMaxCumAck_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VismRudpSessionMaxCumAck_Type.__name__=_C
_VismRudpSessionMaxCumAck_Object=MibTableColumn
vismRudpSessionMaxCumAck=_VismRudpSessionMaxCumAck_Object((1,3,6,1,4,1,351,110,5,5,11,3,1,17),_VismRudpSessionMaxCumAck_Type())
vismRudpSessionMaxCumAck.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRudpSessionMaxCumAck.setStatus(_A)
class _VismRudpSessionCumAckTmout_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(100,65535))
_VismRudpSessionCumAckTmout_Type.__name__=_C
_VismRudpSessionCumAckTmout_Object=MibTableColumn
vismRudpSessionCumAckTmout=_VismRudpSessionCumAckTmout_Object((1,3,6,1,4,1,351,110,5,5,11,3,1,18),_VismRudpSessionCumAckTmout_Type())
vismRudpSessionCumAckTmout.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRudpSessionCumAckTmout.setStatus(_A)
class _VismRudpSessionMaxOutOfSeq_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VismRudpSessionMaxOutOfSeq_Type.__name__=_C
_VismRudpSessionMaxOutOfSeq_Object=MibTableColumn
vismRudpSessionMaxOutOfSeq=_VismRudpSessionMaxOutOfSeq_Object((1,3,6,1,4,1,351,110,5,5,11,3,1,19),_VismRudpSessionMaxOutOfSeq_Type())
vismRudpSessionMaxOutOfSeq.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRudpSessionMaxOutOfSeq.setStatus(_A)
class _VismRudpSessionNullSegTmout_Type(Integer32):defaultValue=2000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VismRudpSessionNullSegTmout_Type.__name__=_C
_VismRudpSessionNullSegTmout_Object=MibTableColumn
vismRudpSessionNullSegTmout=_VismRudpSessionNullSegTmout_Object((1,3,6,1,4,1,351,110,5,5,11,3,1,20),_VismRudpSessionNullSegTmout_Type())
vismRudpSessionNullSegTmout.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRudpSessionNullSegTmout.setStatus(_A)
if mibBuilder.loadTexts:vismRudpSessionNullSegTmout.setUnits(_Q)
class _VismRudpSessionTransStateTmout_Type(Integer32):defaultValue=2000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VismRudpSessionTransStateTmout_Type.__name__=_C
_VismRudpSessionTransStateTmout_Object=MibTableColumn
vismRudpSessionTransStateTmout=_VismRudpSessionTransStateTmout_Object((1,3,6,1,4,1,351,110,5,5,11,3,1,21),_VismRudpSessionTransStateTmout_Type())
vismRudpSessionTransStateTmout.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRudpSessionTransStateTmout.setStatus(_A)
class _VismRudpSessionType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('backhaul',1),('lapdTrunking',2)))
_VismRudpSessionType_Type.__name__=_C
_VismRudpSessionType_Object=MibTableColumn
vismRudpSessionType=_VismRudpSessionType_Object((1,3,6,1,4,1,351,110,5,5,11,3,1,22),_VismRudpSessionType_Type())
vismRudpSessionType.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRudpSessionType.setStatus(_A)
_VismRudpSessionRmtGwIp_Type=IpAddress
_VismRudpSessionRmtGwIp_Object=MibTableColumn
vismRudpSessionRmtGwIp=_VismRudpSessionRmtGwIp_Object((1,3,6,1,4,1,351,110,5,5,11,3,1,23),_VismRudpSessionRmtGwIp_Type())
vismRudpSessionRmtGwIp.setMaxAccess(_E)
if mibBuilder.loadTexts:vismRudpSessionRmtGwIp.setStatus(_A)
_VismRudpSessionStatTable_Object=MibTable
vismRudpSessionStatTable=_VismRudpSessionStatTable_Object((1,3,6,1,4,1,351,110,5,5,11,4))
if mibBuilder.loadTexts:vismRudpSessionStatTable.setStatus(_A)
_VismRudpSessionStatEntry_Object=MibTableRow
vismRudpSessionStatEntry=_VismRudpSessionStatEntry_Object((1,3,6,1,4,1,351,110,5,5,11,4,1))
vismRudpSessionStatEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:vismRudpSessionStatEntry.setStatus(_A)
class _VismRudpSessionStatNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_VismRudpSessionStatNum_Type.__name__=_C
_VismRudpSessionStatNum_Object=MibTableColumn
vismRudpSessionStatNum=_VismRudpSessionStatNum_Object((1,3,6,1,4,1,351,110,5,5,11,4,1,1),_VismRudpSessionStatNum_Type())
vismRudpSessionStatNum.setMaxAccess(_D)
if mibBuilder.loadTexts:vismRudpSessionStatNum.setStatus(_A)
_VismRudpSessionAutoResets_Type=Counter32
_VismRudpSessionAutoResets_Object=MibTableColumn
vismRudpSessionAutoResets=_VismRudpSessionAutoResets_Object((1,3,6,1,4,1,351,110,5,5,11,4,1,2),_VismRudpSessionAutoResets_Type())
vismRudpSessionAutoResets.setMaxAccess(_D)
if mibBuilder.loadTexts:vismRudpSessionAutoResets.setStatus(_A)
_VismRudpSessionRcvdAutoResets_Type=Counter32
_VismRudpSessionRcvdAutoResets_Object=MibTableColumn
vismRudpSessionRcvdAutoResets=_VismRudpSessionRcvdAutoResets_Object((1,3,6,1,4,1,351,110,5,5,11,4,1,3),_VismRudpSessionRcvdAutoResets_Type())
vismRudpSessionRcvdAutoResets.setMaxAccess(_D)
if mibBuilder.loadTexts:vismRudpSessionRcvdAutoResets.setStatus(_A)
_VismRudpSessionRcvdInSeqs_Type=Counter32
_VismRudpSessionRcvdInSeqs_Object=MibTableColumn
vismRudpSessionRcvdInSeqs=_VismRudpSessionRcvdInSeqs_Object((1,3,6,1,4,1,351,110,5,5,11,4,1,4),_VismRudpSessionRcvdInSeqs_Type())
vismRudpSessionRcvdInSeqs.setMaxAccess(_D)
if mibBuilder.loadTexts:vismRudpSessionRcvdInSeqs.setStatus(_A)
if mibBuilder.loadTexts:vismRudpSessionRcvdInSeqs.setUnits(_O)
_VismRudpSessionRcvdOutSeqs_Type=Counter32
_VismRudpSessionRcvdOutSeqs_Object=MibTableColumn
vismRudpSessionRcvdOutSeqs=_VismRudpSessionRcvdOutSeqs_Object((1,3,6,1,4,1,351,110,5,5,11,4,1,5),_VismRudpSessionRcvdOutSeqs_Type())
vismRudpSessionRcvdOutSeqs.setMaxAccess(_D)
if mibBuilder.loadTexts:vismRudpSessionRcvdOutSeqs.setStatus(_A)
if mibBuilder.loadTexts:vismRudpSessionRcvdOutSeqs.setUnits(_O)
_VismRudpSessionSentPackets_Type=Counter32
_VismRudpSessionSentPackets_Object=MibTableColumn
vismRudpSessionSentPackets=_VismRudpSessionSentPackets_Object((1,3,6,1,4,1,351,110,5,5,11,4,1,6),_VismRudpSessionSentPackets_Type())
vismRudpSessionSentPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:vismRudpSessionSentPackets.setStatus(_A)
_VismRudpSessionRcvdPackets_Type=Counter32
_VismRudpSessionRcvdPackets_Object=MibTableColumn
vismRudpSessionRcvdPackets=_VismRudpSessionRcvdPackets_Object((1,3,6,1,4,1,351,110,5,5,11,4,1,7),_VismRudpSessionRcvdPackets_Type())
vismRudpSessionRcvdPackets.setMaxAccess(_D)
if mibBuilder.loadTexts:vismRudpSessionRcvdPackets.setStatus(_A)
if mibBuilder.loadTexts:vismRudpSessionRcvdPackets.setUnits(_O)
_VismRudpSessionSentBytes_Type=Counter32
_VismRudpSessionSentBytes_Object=MibTableColumn
vismRudpSessionSentBytes=_VismRudpSessionSentBytes_Object((1,3,6,1,4,1,351,110,5,5,11,4,1,8),_VismRudpSessionSentBytes_Type())
vismRudpSessionSentBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:vismRudpSessionSentBytes.setStatus(_A)
_VismRudpSessionRcvdBytes_Type=Counter32
_VismRudpSessionRcvdBytes_Object=MibTableColumn
vismRudpSessionRcvdBytes=_VismRudpSessionRcvdBytes_Object((1,3,6,1,4,1,351,110,5,5,11,4,1,9),_VismRudpSessionRcvdBytes_Type())
vismRudpSessionRcvdBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:vismRudpSessionRcvdBytes.setStatus(_A)
_VismRudpSessionDataSentPkts_Type=Counter32
_VismRudpSessionDataSentPkts_Object=MibTableColumn
vismRudpSessionDataSentPkts=_VismRudpSessionDataSentPkts_Object((1,3,6,1,4,1,351,110,5,5,11,4,1,10),_VismRudpSessionDataSentPkts_Type())
vismRudpSessionDataSentPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:vismRudpSessionDataSentPkts.setStatus(_A)
_VismRudpSessionDataRcvdPkts_Type=Counter32
_VismRudpSessionDataRcvdPkts_Object=MibTableColumn
vismRudpSessionDataRcvdPkts=_VismRudpSessionDataRcvdPkts_Object((1,3,6,1,4,1,351,110,5,5,11,4,1,11),_VismRudpSessionDataRcvdPkts_Type())
vismRudpSessionDataRcvdPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:vismRudpSessionDataRcvdPkts.setStatus(_A)
_VismRudpSessionDiscardPkts_Type=Counter32
_VismRudpSessionDiscardPkts_Object=MibTableColumn
vismRudpSessionDiscardPkts=_VismRudpSessionDiscardPkts_Object((1,3,6,1,4,1,351,110,5,5,11,4,1,12),_VismRudpSessionDiscardPkts_Type())
vismRudpSessionDiscardPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:vismRudpSessionDiscardPkts.setStatus(_A)
_VismRudpSessionRetransPkts_Type=Counter32
_VismRudpSessionRetransPkts_Object=MibTableColumn
vismRudpSessionRetransPkts=_VismRudpSessionRetransPkts_Object((1,3,6,1,4,1,351,110,5,5,11,4,1,13),_VismRudpSessionRetransPkts_Type())
vismRudpSessionRetransPkts.setMaxAccess(_D)
if mibBuilder.loadTexts:vismRudpSessionRetransPkts.setStatus(_A)
_CiscoVismSessionMIBConformance_ObjectIdentity=ObjectIdentity
ciscoVismSessionMIBConformance=_CiscoVismSessionMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,95,2))
_CiscoVismSessionMIBGroups_ObjectIdentity=ObjectIdentity
ciscoVismSessionMIBGroups=_CiscoVismSessionMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,95,2,1))
_CiscoVismSessionMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVismSessionMIBCompliances=_CiscoVismSessionMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,95,2,2))
ciscoVismSessionSetGrp=ObjectGroup((1,3,6,1,4,1,351,150,95,2,1,1))
ciscoVismSessionSetGrp.setObjects(*((_B,_F),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ciscoVismSessionSetGrp.setStatus(_A)
ciscoVismSessionGrp=ObjectGroup((1,3,6,1,4,1,351,150,95,2,1,2))
ciscoVismSessionGrp.setObjects(*((_B,_L),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f)))
if mibBuilder.loadTexts:ciscoVismSessionGrp.setStatus(_A)
ciscoVismRudpSessionGrp=ObjectGroup((1,3,6,1,4,1,351,150,95,2,1,3))
ciscoVismRudpSessionGrp.setObjects(*((_B,_M),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1)))
if mibBuilder.loadTexts:ciscoVismRudpSessionGrp.setStatus(_A)
ciscoVismRudpSessionStatGrp=ObjectGroup((1,3,6,1,4,1,351,150,95,2,1,4))
ciscoVismRudpSessionStatGrp.setObjects(*((_B,_N),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:ciscoVismRudpSessionStatGrp.setStatus(_A)
ciscoVismSessionCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,95,2,2,1))
ciscoVismSessionCompliance.setObjects(*((_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:ciscoVismSessionCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'vismSessionGrp':vismSessionGrp,'vismSessionSetTable':vismSessionSetTable,'vismSessionSetEntry':vismSessionSetEntry,_F:vismSessionSetNum,_R:vismSessionSetRowStatus,_S:vismSessionSetState,_T:vismSessionSetTotalGrps,_U:vismSessionSetActiveGrp,_V:vismSessionSetSwitchFails,_W:vismSessionSetSwitchSuccesses,_X:vismSessionSetFaultTolerant,'vismSessionGrpTable':vismSessionGrpTable,'vismSessionGrpEntry':vismSessionGrpEntry,_L:vismSessionGrpNum,_Y:vismSessionGrpSetNum,_Z:vismSessionGrpRowStatus,_a:vismSessionGrpState,_b:vismSessionGrpCurrSession,_c:vismSessionGrpTotalSessions,_d:vismSessionGrpSwitchFails,_e:vismSessionGrpSwitchSuccesses,_f:vismSessionGrpMgcName,'vismRudpSessionCnfTable':vismRudpSessionCnfTable,'vismRudpSessionCnfEntry':vismRudpSessionCnfEntry,_M:vismRudpSessionNum,_g:vismRudpSessionGrpNum,_h:vismRudpSessionCnfRowStatus,_i:vismRudpSessionPriority,_j:vismRudpSessionState,_k:vismRudpSessionCurrSession,_l:vismRudpSessionLocalIp,_m:vismRudpSessionLocalPort,_n:vismRudpSessionRmtIp,_o:vismRudpSessionRmtPort,_p:vismRudpSessionMaxWindow,_q:vismRudpSessionSyncAttempts,_r:vismRudpSessionMaxSegSize,_s:vismRudpSessionMaxAutoReset,_t:vismRudpSessionRetransTmout,_u:vismRudpSessionMaxRetrans,_v:vismRudpSessionMaxCumAck,_w:vismRudpSessionCumAckTmout,_x:vismRudpSessionMaxOutOfSeq,_y:vismRudpSessionNullSegTmout,_z:vismRudpSessionTransStateTmout,_A0:vismRudpSessionType,_A1:vismRudpSessionRmtGwIp,'vismRudpSessionStatTable':vismRudpSessionStatTable,'vismRudpSessionStatEntry':vismRudpSessionStatEntry,_N:vismRudpSessionStatNum,_A2:vismRudpSessionAutoResets,_A3:vismRudpSessionRcvdAutoResets,_A4:vismRudpSessionRcvdInSeqs,_A5:vismRudpSessionRcvdOutSeqs,_A6:vismRudpSessionSentPackets,_A7:vismRudpSessionRcvdPackets,_A8:vismRudpSessionSentBytes,_A9:vismRudpSessionRcvdBytes,_AA:vismRudpSessionDataSentPkts,_AB:vismRudpSessionDataRcvdPkts,_AC:vismRudpSessionDiscardPkts,_AD:vismRudpSessionRetransPkts,'ciscoVismSessionMIB':ciscoVismSessionMIB,'ciscoVismSessionMIBConformance':ciscoVismSessionMIBConformance,'ciscoVismSessionMIBGroups':ciscoVismSessionMIBGroups,_AE:ciscoVismSessionSetGrp,_AF:ciscoVismSessionGrp,_AG:ciscoVismRudpSessionGrp,_AH:ciscoVismRudpSessionStatGrp,'ciscoVismSessionMIBCompliances':ciscoVismSessionMIBCompliances,'ciscoVismSessionCompliance':ciscoVismSessionCompliance})