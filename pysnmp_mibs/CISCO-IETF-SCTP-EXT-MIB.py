_A8='cSctpExtAssocStatGroupRev1'
_A7='cSctpExtCtrlGroupRev1'
_A6='cSctpExtAssocNotificationsGroup'
_A5='cSctpExtAssocStatGroup'
_A4='cSctpExtCtrlGroup'
_A3='cSctpExtDestAddressStateChange'
_A2='cSctpAssocExtBundleFlag'
_A1='cSctpAssocExtBundleTimeout'
_A0='cSctpAssocExtRtxChunksFast'
_z='cSctpAssocExtEffectiveAddress'
_y='cSctpAssocExtEffectiveAddrType'
_x='cSctpAddressStateNotifEnabled'
_w='cSctpAssocRemAddressSRTT'
_v='cSctpAssocRemAddressFailedCnt'
_u='cSctpAssocExtMaxInitRetr'
_t='cSctpAssocExtValCookieLife'
_s='cSctpAssocExtRtoInitial'
_r='cSctpAssocExtRtoMax'
_q='cSctpAssocExtRtoMin'
_p='cSctpStatDestAddressFailures'
_o='cSctpStatRtxChucksFast'
_n='cSctpStatRtxChucks'
_m='cSctpAssocRemAddressExtEntry'
_l='cSctpAssocExtEntry'
_k='TruthValue'
_j='cSctpAssocRemAddressStatus'
_i='CISCO-IETF-SCTP-MIB'
_h='cSctpExtAssocRemAddrGroup'
_g='cSctpExtAssocCtrlGroup'
_f='cSctpExtStatGroup'
_e='cSctpAssocExtDatagramsSent'
_d='cSctpAssocExtDatagramsRec'
_c='cSctpAssocExtChunksSentUnOrdered'
_b='cSctpAssocExtChunksSentOrdered'
_a='cSctpAssocExtChunksSentControl'
_Z='cSctpAssocExtChunksRecUnOrdered'
_Y='cSctpAssocExtChunksRecOrdered'
_X='cSctpAssocExtChunksRecControl'
_W='cSctpAssocExtUlpQueuedRT'
_V='cSctpAssocExtUlpQueuedHW'
_U='cSctpAssocExtUlpQueued'
_T='cSctpAssocExtRemRecWndZeroCnt'
_S='cSctpAssocExtRemRecWndLowMark'
_R='cSctpAssocExtRemRecWnd'
_Q='cSctpAssocExtLocRecWndZeroCnt'
_P='cSctpAssocExtLocRecWndLowMark'
_O='cSctpAssocExtLocRecWnd'
_N='cSctpAssocExtMTU'
_M='deprecated'
_L='cSctpCtrlMaxHeld'
_K='cSctpCtrlPurgeTimeout'
_J='datagrams'
_I='read-write'
_H='bytes'
_G='Gauge32'
_F='milliseconds'
_E='Unsigned32'
_D='chunks'
_C='read-only'
_B='current'
_A='CISCO-IETF-SCTP-EXT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cSctpAssocEntry,cSctpAssocRemAddressEntry,cSctpAssocRemAddressStatus=mibBuilder.importSymbols(_i,'cSctpAssocEntry','cSctpAssocRemAddressEntry',_j)
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64',_G,'Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_k)
cSctpExtMIB=ModuleIdentity((1,3,6,1,4,1,9,10,76))
if mibBuilder.loadTexts:cSctpExtMIB.setRevisions(('2001-11-09 00:00','2001-08-27 00:00'))
_CSctpExtNotifications_ObjectIdentity=ObjectIdentity
cSctpExtNotifications=_CSctpExtNotifications_ObjectIdentity((1,3,6,1,4,1,9,10,76,0))
_CSctpExtObjects_ObjectIdentity=ObjectIdentity
cSctpExtObjects=_CSctpExtObjects_ObjectIdentity((1,3,6,1,4,1,9,10,76,1))
_CSctpScalarsExt_ObjectIdentity=ObjectIdentity
cSctpScalarsExt=_CSctpScalarsExt_ObjectIdentity((1,3,6,1,4,1,9,10,76,1,1))
_CSctpStatRtxChucks_Type=Counter32
_CSctpStatRtxChucks_Object=MibScalar
cSctpStatRtxChucks=_CSctpStatRtxChucks_Object((1,3,6,1,4,1,9,10,76,1,1,1),_CSctpStatRtxChucks_Type())
cSctpStatRtxChucks.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpStatRtxChucks.setStatus(_B)
if mibBuilder.loadTexts:cSctpStatRtxChucks.setUnits(_D)
_CSctpStatRtxChucksFast_Type=Counter32
_CSctpStatRtxChucksFast_Object=MibScalar
cSctpStatRtxChucksFast=_CSctpStatRtxChucksFast_Object((1,3,6,1,4,1,9,10,76,1,1,2),_CSctpStatRtxChucksFast_Type())
cSctpStatRtxChucksFast.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpStatRtxChucksFast.setStatus(_B)
if mibBuilder.loadTexts:cSctpStatRtxChucksFast.setUnits(_D)
_CSctpStatDestAddressFailures_Type=Counter32
_CSctpStatDestAddressFailures_Object=MibScalar
cSctpStatDestAddressFailures=_CSctpStatDestAddressFailures_Object((1,3,6,1,4,1,9,10,76,1,1,3),_CSctpStatDestAddressFailures_Type())
cSctpStatDestAddressFailures.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpStatDestAddressFailures.setStatus(_B)
class _CSctpCtrlPurgeTimeout_Type(Unsigned32):defaultValue=86400;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3600,3000000))
_CSctpCtrlPurgeTimeout_Type.__name__=_E
_CSctpCtrlPurgeTimeout_Object=MibScalar
cSctpCtrlPurgeTimeout=_CSctpCtrlPurgeTimeout_Object((1,3,6,1,4,1,9,10,76,1,1,4),_CSctpCtrlPurgeTimeout_Type())
cSctpCtrlPurgeTimeout.setMaxAccess(_I)
if mibBuilder.loadTexts:cSctpCtrlPurgeTimeout.setStatus(_B)
if mibBuilder.loadTexts:cSctpCtrlPurgeTimeout.setUnits('seconds')
class _CSctpCtrlMaxHeld_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,10000))
_CSctpCtrlMaxHeld_Type.__name__=_E
_CSctpCtrlMaxHeld_Object=MibScalar
cSctpCtrlMaxHeld=_CSctpCtrlMaxHeld_Object((1,3,6,1,4,1,9,10,76,1,1,5),_CSctpCtrlMaxHeld_Type())
cSctpCtrlMaxHeld.setMaxAccess(_I)
if mibBuilder.loadTexts:cSctpCtrlMaxHeld.setStatus(_B)
if mibBuilder.loadTexts:cSctpCtrlMaxHeld.setUnits('association TCBs')
class _CSctpAddressStateNotifEnabled_Type(TruthValue):defaultValue=2
_CSctpAddressStateNotifEnabled_Type.__name__=_k
_CSctpAddressStateNotifEnabled_Object=MibScalar
cSctpAddressStateNotifEnabled=_CSctpAddressStateNotifEnabled_Object((1,3,6,1,4,1,9,10,76,1,1,6),_CSctpAddressStateNotifEnabled_Type())
cSctpAddressStateNotifEnabled.setMaxAccess(_I)
if mibBuilder.loadTexts:cSctpAddressStateNotifEnabled.setStatus(_B)
_CSctpExtTables_ObjectIdentity=ObjectIdentity
cSctpExtTables=_CSctpExtTables_ObjectIdentity((1,3,6,1,4,1,9,10,76,1,2))
_CSctpAssocExtTable_Object=MibTable
cSctpAssocExtTable=_CSctpAssocExtTable_Object((1,3,6,1,4,1,9,10,76,1,2,1))
if mibBuilder.loadTexts:cSctpAssocExtTable.setStatus(_B)
_CSctpAssocExtEntry_Object=MibTableRow
cSctpAssocExtEntry=_CSctpAssocExtEntry_Object((1,3,6,1,4,1,9,10,76,1,2,1,1))
if mibBuilder.loadTexts:cSctpAssocExtEntry.setStatus(_B)
_CSctpAssocExtRtoMin_Type=Unsigned32
_CSctpAssocExtRtoMin_Object=MibTableColumn
cSctpAssocExtRtoMin=_CSctpAssocExtRtoMin_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,1),_CSctpAssocExtRtoMin_Type())
cSctpAssocExtRtoMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtRtoMin.setStatus(_B)
if mibBuilder.loadTexts:cSctpAssocExtRtoMin.setUnits(_F)
_CSctpAssocExtRtoMax_Type=Unsigned32
_CSctpAssocExtRtoMax_Object=MibTableColumn
cSctpAssocExtRtoMax=_CSctpAssocExtRtoMax_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,2),_CSctpAssocExtRtoMax_Type())
cSctpAssocExtRtoMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtRtoMax.setStatus(_B)
if mibBuilder.loadTexts:cSctpAssocExtRtoMax.setUnits(_F)
_CSctpAssocExtRtoInitial_Type=Unsigned32
_CSctpAssocExtRtoInitial_Object=MibTableColumn
cSctpAssocExtRtoInitial=_CSctpAssocExtRtoInitial_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,3),_CSctpAssocExtRtoInitial_Type())
cSctpAssocExtRtoInitial.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtRtoInitial.setStatus(_B)
if mibBuilder.loadTexts:cSctpAssocExtRtoInitial.setUnits(_F)
_CSctpAssocExtValCookieLife_Type=Unsigned32
_CSctpAssocExtValCookieLife_Object=MibTableColumn
cSctpAssocExtValCookieLife=_CSctpAssocExtValCookieLife_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,4),_CSctpAssocExtValCookieLife_Type())
cSctpAssocExtValCookieLife.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtValCookieLife.setStatus(_B)
if mibBuilder.loadTexts:cSctpAssocExtValCookieLife.setUnits(_F)
_CSctpAssocExtMaxInitRetr_Type=Unsigned32
_CSctpAssocExtMaxInitRetr_Object=MibTableColumn
cSctpAssocExtMaxInitRetr=_CSctpAssocExtMaxInitRetr_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,5),_CSctpAssocExtMaxInitRetr_Type())
cSctpAssocExtMaxInitRetr.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtMaxInitRetr.setStatus(_B)
class _CSctpAssocExtMTU_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(37,65535))
_CSctpAssocExtMTU_Type.__name__=_E
_CSctpAssocExtMTU_Object=MibTableColumn
cSctpAssocExtMTU=_CSctpAssocExtMTU_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,6),_CSctpAssocExtMTU_Type())
cSctpAssocExtMTU.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtMTU.setStatus(_B)
if mibBuilder.loadTexts:cSctpAssocExtMTU.setUnits(_H)
class _CSctpAssocExtLocRecWnd_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CSctpAssocExtLocRecWnd_Type.__name__=_E
_CSctpAssocExtLocRecWnd_Object=MibTableColumn
cSctpAssocExtLocRecWnd=_CSctpAssocExtLocRecWnd_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,7),_CSctpAssocExtLocRecWnd_Type())
cSctpAssocExtLocRecWnd.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtLocRecWnd.setStatus(_B)
if mibBuilder.loadTexts:cSctpAssocExtLocRecWnd.setUnits(_H)
class _CSctpAssocExtLocRecWndLowMark_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CSctpAssocExtLocRecWndLowMark_Type.__name__=_G
_CSctpAssocExtLocRecWndLowMark_Object=MibTableColumn
cSctpAssocExtLocRecWndLowMark=_CSctpAssocExtLocRecWndLowMark_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,8),_CSctpAssocExtLocRecWndLowMark_Type())
cSctpAssocExtLocRecWndLowMark.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtLocRecWndLowMark.setStatus(_B)
if mibBuilder.loadTexts:cSctpAssocExtLocRecWndLowMark.setUnits(_H)
_CSctpAssocExtLocRecWndZeroCnt_Type=Counter32
_CSctpAssocExtLocRecWndZeroCnt_Object=MibTableColumn
cSctpAssocExtLocRecWndZeroCnt=_CSctpAssocExtLocRecWndZeroCnt_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,9),_CSctpAssocExtLocRecWndZeroCnt_Type())
cSctpAssocExtLocRecWndZeroCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtLocRecWndZeroCnt.setStatus(_B)
class _CSctpAssocExtRemRecWnd_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CSctpAssocExtRemRecWnd_Type.__name__=_E
_CSctpAssocExtRemRecWnd_Object=MibTableColumn
cSctpAssocExtRemRecWnd=_CSctpAssocExtRemRecWnd_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,10),_CSctpAssocExtRemRecWnd_Type())
cSctpAssocExtRemRecWnd.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtRemRecWnd.setStatus(_B)
if mibBuilder.loadTexts:cSctpAssocExtRemRecWnd.setUnits(_H)
class _CSctpAssocExtRemRecWndLowMark_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CSctpAssocExtRemRecWndLowMark_Type.__name__=_G
_CSctpAssocExtRemRecWndLowMark_Object=MibTableColumn
cSctpAssocExtRemRecWndLowMark=_CSctpAssocExtRemRecWndLowMark_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,11),_CSctpAssocExtRemRecWndLowMark_Type())
cSctpAssocExtRemRecWndLowMark.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtRemRecWndLowMark.setStatus(_B)
if mibBuilder.loadTexts:cSctpAssocExtRemRecWndLowMark.setUnits(_H)
_CSctpAssocExtRemRecWndZeroCnt_Type=Counter32
_CSctpAssocExtRemRecWndZeroCnt_Object=MibTableColumn
cSctpAssocExtRemRecWndZeroCnt=_CSctpAssocExtRemRecWndZeroCnt_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,12),_CSctpAssocExtRemRecWndZeroCnt_Type())
cSctpAssocExtRemRecWndZeroCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtRemRecWndZeroCnt.setStatus(_B)
class _CSctpAssocExtUlpQueued_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CSctpAssocExtUlpQueued_Type.__name__=_G
_CSctpAssocExtUlpQueued_Object=MibTableColumn
cSctpAssocExtUlpQueued=_CSctpAssocExtUlpQueued_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,13),_CSctpAssocExtUlpQueued_Type())
cSctpAssocExtUlpQueued.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtUlpQueued.setStatus(_B)
if mibBuilder.loadTexts:cSctpAssocExtUlpQueued.setUnits(_J)
class _CSctpAssocExtUlpQueuedHW_Type(Gauge32):subtypeSpec=Gauge32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CSctpAssocExtUlpQueuedHW_Type.__name__=_G
_CSctpAssocExtUlpQueuedHW_Object=MibTableColumn
cSctpAssocExtUlpQueuedHW=_CSctpAssocExtUlpQueuedHW_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,14),_CSctpAssocExtUlpQueuedHW_Type())
cSctpAssocExtUlpQueuedHW.setMaxAccess(_I)
if mibBuilder.loadTexts:cSctpAssocExtUlpQueuedHW.setStatus(_B)
if mibBuilder.loadTexts:cSctpAssocExtUlpQueuedHW.setUnits(_J)
_CSctpAssocExtUlpQueuedRT_Type=TimeStamp
_CSctpAssocExtUlpQueuedRT_Object=MibTableColumn
cSctpAssocExtUlpQueuedRT=_CSctpAssocExtUlpQueuedRT_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,15),_CSctpAssocExtUlpQueuedRT_Type())
cSctpAssocExtUlpQueuedRT.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtUlpQueuedRT.setStatus(_B)
_CSctpAssocExtChunksRecControl_Type=Counter32
_CSctpAssocExtChunksRecControl_Object=MibTableColumn
cSctpAssocExtChunksRecControl=_CSctpAssocExtChunksRecControl_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,16),_CSctpAssocExtChunksRecControl_Type())
cSctpAssocExtChunksRecControl.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtChunksRecControl.setStatus(_B)
if mibBuilder.loadTexts:cSctpAssocExtChunksRecControl.setUnits(_D)
_CSctpAssocExtChunksRecOrdered_Type=Counter32
_CSctpAssocExtChunksRecOrdered_Object=MibTableColumn
cSctpAssocExtChunksRecOrdered=_CSctpAssocExtChunksRecOrdered_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,17),_CSctpAssocExtChunksRecOrdered_Type())
cSctpAssocExtChunksRecOrdered.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtChunksRecOrdered.setStatus(_B)
if mibBuilder.loadTexts:cSctpAssocExtChunksRecOrdered.setUnits(_D)
_CSctpAssocExtChunksRecUnOrdered_Type=Counter32
_CSctpAssocExtChunksRecUnOrdered_Object=MibTableColumn
cSctpAssocExtChunksRecUnOrdered=_CSctpAssocExtChunksRecUnOrdered_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,18),_CSctpAssocExtChunksRecUnOrdered_Type())
cSctpAssocExtChunksRecUnOrdered.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtChunksRecUnOrdered.setStatus(_B)
if mibBuilder.loadTexts:cSctpAssocExtChunksRecUnOrdered.setUnits(_D)
_CSctpAssocExtChunksSentControl_Type=Counter32
_CSctpAssocExtChunksSentControl_Object=MibTableColumn
cSctpAssocExtChunksSentControl=_CSctpAssocExtChunksSentControl_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,19),_CSctpAssocExtChunksSentControl_Type())
cSctpAssocExtChunksSentControl.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtChunksSentControl.setStatus(_B)
if mibBuilder.loadTexts:cSctpAssocExtChunksSentControl.setUnits(_D)
_CSctpAssocExtChunksSentOrdered_Type=Counter32
_CSctpAssocExtChunksSentOrdered_Object=MibTableColumn
cSctpAssocExtChunksSentOrdered=_CSctpAssocExtChunksSentOrdered_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,20),_CSctpAssocExtChunksSentOrdered_Type())
cSctpAssocExtChunksSentOrdered.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtChunksSentOrdered.setStatus(_B)
if mibBuilder.loadTexts:cSctpAssocExtChunksSentOrdered.setUnits(_D)
_CSctpAssocExtChunksSentUnOrdered_Type=Counter32
_CSctpAssocExtChunksSentUnOrdered_Object=MibTableColumn
cSctpAssocExtChunksSentUnOrdered=_CSctpAssocExtChunksSentUnOrdered_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,21),_CSctpAssocExtChunksSentUnOrdered_Type())
cSctpAssocExtChunksSentUnOrdered.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtChunksSentUnOrdered.setStatus(_B)
if mibBuilder.loadTexts:cSctpAssocExtChunksSentUnOrdered.setUnits(_D)
_CSctpAssocExtDatagramsRec_Type=Counter32
_CSctpAssocExtDatagramsRec_Object=MibTableColumn
cSctpAssocExtDatagramsRec=_CSctpAssocExtDatagramsRec_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,22),_CSctpAssocExtDatagramsRec_Type())
cSctpAssocExtDatagramsRec.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtDatagramsRec.setStatus(_B)
if mibBuilder.loadTexts:cSctpAssocExtDatagramsRec.setUnits(_J)
_CSctpAssocExtDatagramsSent_Type=Counter32
_CSctpAssocExtDatagramsSent_Object=MibTableColumn
cSctpAssocExtDatagramsSent=_CSctpAssocExtDatagramsSent_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,23),_CSctpAssocExtDatagramsSent_Type())
cSctpAssocExtDatagramsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtDatagramsSent.setStatus(_B)
if mibBuilder.loadTexts:cSctpAssocExtDatagramsSent.setUnits(_J)
_CSctpAssocExtEffectiveAddrType_Type=InetAddressType
_CSctpAssocExtEffectiveAddrType_Object=MibTableColumn
cSctpAssocExtEffectiveAddrType=_CSctpAssocExtEffectiveAddrType_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,24),_CSctpAssocExtEffectiveAddrType_Type())
cSctpAssocExtEffectiveAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtEffectiveAddrType.setStatus(_B)
_CSctpAssocExtEffectiveAddress_Type=InetAddress
_CSctpAssocExtEffectiveAddress_Object=MibTableColumn
cSctpAssocExtEffectiveAddress=_CSctpAssocExtEffectiveAddress_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,25),_CSctpAssocExtEffectiveAddress_Type())
cSctpAssocExtEffectiveAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtEffectiveAddress.setStatus(_B)
_CSctpAssocExtRtxChunksFast_Type=Counter32
_CSctpAssocExtRtxChunksFast_Object=MibTableColumn
cSctpAssocExtRtxChunksFast=_CSctpAssocExtRtxChunksFast_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,26),_CSctpAssocExtRtxChunksFast_Type())
cSctpAssocExtRtxChunksFast.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtRtxChunksFast.setStatus(_B)
if mibBuilder.loadTexts:cSctpAssocExtRtxChunksFast.setUnits(_D)
_CSctpAssocExtBundleFlag_Type=TruthValue
_CSctpAssocExtBundleFlag_Object=MibTableColumn
cSctpAssocExtBundleFlag=_CSctpAssocExtBundleFlag_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,27),_CSctpAssocExtBundleFlag_Type())
cSctpAssocExtBundleFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtBundleFlag.setStatus(_B)
class _CSctpAssocExtBundleTimeout_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_CSctpAssocExtBundleTimeout_Type.__name__=_E
_CSctpAssocExtBundleTimeout_Object=MibTableColumn
cSctpAssocExtBundleTimeout=_CSctpAssocExtBundleTimeout_Object((1,3,6,1,4,1,9,10,76,1,2,1,1,28),_CSctpAssocExtBundleTimeout_Type())
cSctpAssocExtBundleTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocExtBundleTimeout.setStatus(_B)
if mibBuilder.loadTexts:cSctpAssocExtBundleTimeout.setUnits(_F)
_CSctpAssocRemAddressExtTable_Object=MibTable
cSctpAssocRemAddressExtTable=_CSctpAssocRemAddressExtTable_Object((1,3,6,1,4,1,9,10,76,1,2,2))
if mibBuilder.loadTexts:cSctpAssocRemAddressExtTable.setStatus(_B)
_CSctpAssocRemAddressExtEntry_Object=MibTableRow
cSctpAssocRemAddressExtEntry=_CSctpAssocRemAddressExtEntry_Object((1,3,6,1,4,1,9,10,76,1,2,2,1))
if mibBuilder.loadTexts:cSctpAssocRemAddressExtEntry.setStatus(_B)
_CSctpAssocRemAddressFailedCnt_Type=Counter32
_CSctpAssocRemAddressFailedCnt_Object=MibTableColumn
cSctpAssocRemAddressFailedCnt=_CSctpAssocRemAddressFailedCnt_Object((1,3,6,1,4,1,9,10,76,1,2,2,1,1),_CSctpAssocRemAddressFailedCnt_Type())
cSctpAssocRemAddressFailedCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocRemAddressFailedCnt.setStatus(_B)
class _CSctpAssocRemAddressSRTT_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CSctpAssocRemAddressSRTT_Type.__name__=_E
_CSctpAssocRemAddressSRTT_Object=MibTableColumn
cSctpAssocRemAddressSRTT=_CSctpAssocRemAddressSRTT_Object((1,3,6,1,4,1,9,10,76,1,2,2,1,2),_CSctpAssocRemAddressSRTT_Type())
cSctpAssocRemAddressSRTT.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocRemAddressSRTT.setStatus(_B)
if mibBuilder.loadTexts:cSctpAssocRemAddressSRTT.setUnits(_F)
_CSctpExtConformance_ObjectIdentity=ObjectIdentity
cSctpExtConformance=_CSctpExtConformance_ObjectIdentity((1,3,6,1,4,1,9,10,76,3))
_CSctpExtCompliances_ObjectIdentity=ObjectIdentity
cSctpExtCompliances=_CSctpExtCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,76,3,1))
_CSctpExtGroups_ObjectIdentity=ObjectIdentity
cSctpExtGroups=_CSctpExtGroups_ObjectIdentity((1,3,6,1,4,1,9,10,76,3,2))
cSctpAssocEntry.registerAugmentions((_A,_l))
cSctpAssocExtEntry.setIndexNames(*cSctpAssocEntry.getIndexNames())
cSctpAssocRemAddressEntry.registerAugmentions((_A,_m))
cSctpAssocRemAddressExtEntry.setIndexNames(*cSctpAssocRemAddressEntry.getIndexNames())
cSctpExtStatGroup=ObjectGroup((1,3,6,1,4,1,9,10,76,3,2,1))
cSctpExtStatGroup.setObjects(*((_A,_n),(_A,_o),(_A,_p)))
if mibBuilder.loadTexts:cSctpExtStatGroup.setStatus(_B)
cSctpExtCtrlGroup=ObjectGroup((1,3,6,1,4,1,9,10,76,3,2,2))
cSctpExtCtrlGroup.setObjects(*((_A,_K),(_A,_L)))
if mibBuilder.loadTexts:cSctpExtCtrlGroup.setStatus(_M)
cSctpExtAssocCtrlGroup=ObjectGroup((1,3,6,1,4,1,9,10,76,3,2,3))
cSctpExtAssocCtrlGroup.setObjects(*((_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:cSctpExtAssocCtrlGroup.setStatus(_B)
cSctpExtAssocStatGroup=ObjectGroup((1,3,6,1,4,1,9,10,76,3,2,4))
cSctpExtAssocStatGroup.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:cSctpExtAssocStatGroup.setStatus(_M)
cSctpExtAssocRemAddrGroup=ObjectGroup((1,3,6,1,4,1,9,10,76,3,2,5))
cSctpExtAssocRemAddrGroup.setObjects(*((_A,_v),(_A,_w)))
if mibBuilder.loadTexts:cSctpExtAssocRemAddrGroup.setStatus(_B)
cSctpExtCtrlGroupRev1=ObjectGroup((1,3,6,1,4,1,9,10,76,3,2,7))
cSctpExtCtrlGroupRev1.setObjects(*((_A,_K),(_A,_L),(_A,_x)))
if mibBuilder.loadTexts:cSctpExtCtrlGroupRev1.setStatus(_B)
cSctpExtAssocStatGroupRev1=ObjectGroup((1,3,6,1,4,1,9,10,76,3,2,8))
cSctpExtAssocStatGroupRev1.setObjects(*((_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:cSctpExtAssocStatGroupRev1.setStatus(_B)
cSctpExtDestAddressStateChange=NotificationType((1,3,6,1,4,1,9,10,76,0,1))
cSctpExtDestAddressStateChange.setObjects((_i,_j))
if mibBuilder.loadTexts:cSctpExtDestAddressStateChange.setStatus(_B)
cSctpExtAssocNotificationsGroup=NotificationGroup((1,3,6,1,4,1,9,10,76,3,2,6))
cSctpExtAssocNotificationsGroup.setObjects((_A,_A3))
if mibBuilder.loadTexts:cSctpExtAssocNotificationsGroup.setStatus(_B)
cSctpExtCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,76,3,1,1))
cSctpExtCompliance.setObjects(*((_A,_f),(_A,_A4),(_A,_g),(_A,_A5),(_A,_h)))
if mibBuilder.loadTexts:cSctpExtCompliance.setStatus(_M)
cSctpExtComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,10,76,3,1,2))
cSctpExtComplianceRev1.setObjects(*((_A,_f),(_A,_g),(_A,_h),(_A,_A6),(_A,_A7),(_A,_A8)))
if mibBuilder.loadTexts:cSctpExtComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'cSctpExtMIB':cSctpExtMIB,'cSctpExtNotifications':cSctpExtNotifications,_A3:cSctpExtDestAddressStateChange,'cSctpExtObjects':cSctpExtObjects,'cSctpScalarsExt':cSctpScalarsExt,_n:cSctpStatRtxChucks,_o:cSctpStatRtxChucksFast,_p:cSctpStatDestAddressFailures,_K:cSctpCtrlPurgeTimeout,_L:cSctpCtrlMaxHeld,_x:cSctpAddressStateNotifEnabled,'cSctpExtTables':cSctpExtTables,'cSctpAssocExtTable':cSctpAssocExtTable,_l:cSctpAssocExtEntry,_q:cSctpAssocExtRtoMin,_r:cSctpAssocExtRtoMax,_s:cSctpAssocExtRtoInitial,_t:cSctpAssocExtValCookieLife,_u:cSctpAssocExtMaxInitRetr,_N:cSctpAssocExtMTU,_O:cSctpAssocExtLocRecWnd,_P:cSctpAssocExtLocRecWndLowMark,_Q:cSctpAssocExtLocRecWndZeroCnt,_R:cSctpAssocExtRemRecWnd,_S:cSctpAssocExtRemRecWndLowMark,_T:cSctpAssocExtRemRecWndZeroCnt,_U:cSctpAssocExtUlpQueued,_V:cSctpAssocExtUlpQueuedHW,_W:cSctpAssocExtUlpQueuedRT,_X:cSctpAssocExtChunksRecControl,_Y:cSctpAssocExtChunksRecOrdered,_Z:cSctpAssocExtChunksRecUnOrdered,_a:cSctpAssocExtChunksSentControl,_b:cSctpAssocExtChunksSentOrdered,_c:cSctpAssocExtChunksSentUnOrdered,_d:cSctpAssocExtDatagramsRec,_e:cSctpAssocExtDatagramsSent,_y:cSctpAssocExtEffectiveAddrType,_z:cSctpAssocExtEffectiveAddress,_A0:cSctpAssocExtRtxChunksFast,_A2:cSctpAssocExtBundleFlag,_A1:cSctpAssocExtBundleTimeout,'cSctpAssocRemAddressExtTable':cSctpAssocRemAddressExtTable,_m:cSctpAssocRemAddressExtEntry,_v:cSctpAssocRemAddressFailedCnt,_w:cSctpAssocRemAddressSRTT,'cSctpExtConformance':cSctpExtConformance,'cSctpExtCompliances':cSctpExtCompliances,'cSctpExtCompliance':cSctpExtCompliance,'cSctpExtComplianceRev1':cSctpExtComplianceRev1,'cSctpExtGroups':cSctpExtGroups,_f:cSctpExtStatGroup,_A4:cSctpExtCtrlGroup,_g:cSctpExtAssocCtrlGroup,_A5:cSctpExtAssocStatGroup,_h:cSctpExtAssocRemAddrGroup,_A6:cSctpExtAssocNotificationsGroup,_A7:cSctpExtCtrlGroupRev1,_A8:cSctpExtAssocStatGroupRev1})