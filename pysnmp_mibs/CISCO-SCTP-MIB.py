_At='ceSctpAssocStatGroup'
_As='ceSctpOtherStatGroup'
_Ar='ceSctpStateStatGroup'
_Aq='ceSctpAssocTablesVariablesGroup'
_Ap='ceSctpGeneralVariablesGroup'
_Ao='ceSctpAssocRemAddressRetransCnt'
_An='ceSctpAssocRemAddressRowStatus'
_Am='ceSctpAssocRemAddressSRTT'
_Al='ceSctpAssocRemAddressMaxRetran'
_Ak='ceSctpAssocRemAddressHtBtTime'
_Aj='ceSctpAssocRemAddressHtBtFlag'
_Ai='ceSctpAssocRemAddressRTO'
_Ah='ceSctpAssocRemAddressStatus'
_Ag='ceSctpAssocLocalAddressRowStatus'
_Af='ceSctpAssocRowStatus'
_Ae='ceSctpAssocDatagramsSent'
_Ad='ceSctpAssocDatagramsRec'
_Ac='ceSctpAssocChunksSentUnOrdered'
_Ab='ceSctpAssocChunksSentOrdered'
_Aa='ceSctpAssocChunksSentControl'
_AZ='ceSctpAssocChunksSent'
_AY='ceSctpAssocChunksReTrans'
_AX='ceSctpAssocChunksRecOutOrder'
_AW='ceSctpAssocChunksRecUnOrdered'
_AV='ceSctpAssocChunksRecOrdered'
_AU='ceSctpAssocChunksRecControl'
_AT='ceSctpAssocChunksRec'
_AS='ceSctpAssocChunksDiscarded'
_AR='ceSctpAssocBytesSent'
_AQ='ceSctpAssocBytesRec'
_AP='ceSctpAssocChecksumErrorCounter'
_AO='ceSctpAssocULPDatagramsQueuedHigh'
_AN='ceSctpAssocULPDatagramsQueued'
_AM='ceSctpAssocRemRecWndZeroCnt'
_AL='ceSctpAssocRemRecWndLowMark'
_AK='ceSctpAssocRemRecWnd'
_AJ='ceSctpAssocLocRecWndZeroCnt'
_AI='ceSctpAssocLocRecWndLowMark'
_AH='ceSctpAssocLocRecWnd'
_AG='ceSctpAssocMTU'
_AF='ceSctpAssocMaxRetr'
_AE='ceSctpAssocOutStreams'
_AD='ceSctpAssocInStreams'
_AC='ceSctpAssocCongestionOnset3'
_AB='ceSctpAssocCongestionOnset2'
_AA='ceSctpAssocCongestionOnset1'
_A9='ceSctpAssocCongestionAbate3'
_A8='ceSctpAssocCongestionAbate2'
_A7='ceSctpAssocCongestionAbate1'
_A6='ceSctpAssocCongestionLevelsCur'
_A5='ceSctpAssocCongestionLevels'
_A4='ceSctpAssocRemPrimaryAddress'
_A3='ceSctpAssocRemPrimaryAddressType'
_A2='ceSctpAssocRemSCTPPort'
_A1='ceSctpAssocLocalSCTPPort'
_A0='ceSctpAssocRemHostName'
_z='ceSctpAssocInitialT2'
_y='ceSctpAssocInitialT1'
_x='ceSctpAssocMaxInitRetr'
_w='ceSctpAssocValCookieLife'
_v='ceSctpAssocRtoInitial'
_u='ceSctpAssocRtoMax'
_t='ceSctpAssocRtoMin'
_s='ceSctpAssocUpTime'
_r='ceSctpAssocState'
_q='ceSctpStatT2expired'
_p='ceSctpStatT1expired'
_o='ceSctpStatOutOfBlue'
_n='ceSctpStatReassembledUsrMessages'
_m='ceSctpStatFragmentedUsrMessages'
_l='ceSctpStatDatagramsSent'
_k='ceSctpStatDatagramsRec'
_j='ceSctpStatChunksReTrans'
_i='ceSctpStatChunksRecUnOrdered'
_h='ceSctpStatChunksRecOrdered'
_g='ceSctpStatChunksRecControl'
_f='ceSctpStatChunksRec'
_e='ceSctpStatChunksSentUnOrdered'
_d='ceSctpStatChunksSentOrdered'
_c='ceSctpStatChunksSentControl'
_b='ceSctpStatChunksSent'
_a='ceSctpStatChunksDiscard'
_Z='ceSctpStatBytesSent'
_Y='ceSctpStatBytesRec'
_X='ceSctpShutdowns'
_W='ceSctpAborted'
_V='ceSctpPassiveEstab'
_U='ceSctpActiveEstab'
_T='ceSctpCurrEstab'
_S='ceSctpMaxAssociations'
_R='ceSctpRtoAlgorithm'
_Q='inactive'
_P='active'
_O='ceSctpAssocRemAddressIP'
_N='ceSctpAssocRemAddressIPType'
_M='ceSctpAssocLocalAddressIP'
_L='ceSctpAssocLocalAddressIPType'
_K='DataGrams'
_J='OctetString'
_I='ceSctpAssocId'
_H='bytes'
_G='not-accessible'
_F='Integer32'
_E='milliseconds'
_D='Unsigned32'
_C='read-only'
_B='CISCO-SCTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ceSctpMIB=ModuleIdentity((1,3,6,1,4,1,9,10,74))
if mibBuilder.loadTexts:ceSctpMIB.setRevisions(('2005-12-21 00:00','2001-06-07 00:00'))
class InetAddressType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,16)));namedValues=NamedValues(*(('unknown',0),('ipv4',1),('ipv6',2),('dns',16)))
class InetAddress(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CeSctpObjects_ObjectIdentity=ObjectIdentity
ceSctpObjects=_CeSctpObjects_ObjectIdentity((1,3,6,1,4,1,9,10,74,1))
_CeSctpScalars_ObjectIdentity=ObjectIdentity
ceSctpScalars=_CeSctpScalars_ObjectIdentity((1,3,6,1,4,1,9,10,74,1,1))
class _CeSctpRtoAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('vanj',2)))
_CeSctpRtoAlgorithm_Type.__name__=_F
_CeSctpRtoAlgorithm_Object=MibScalar
ceSctpRtoAlgorithm=_CeSctpRtoAlgorithm_Object((1,3,6,1,4,1,9,10,74,1,1,1),_CeSctpRtoAlgorithm_Type())
ceSctpRtoAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpRtoAlgorithm.setStatus(_A)
class _CeSctpMaxAssociations_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1024))
_CeSctpMaxAssociations_Type.__name__=_D
_CeSctpMaxAssociations_Object=MibScalar
ceSctpMaxAssociations=_CeSctpMaxAssociations_Object((1,3,6,1,4,1,9,10,74,1,1,2),_CeSctpMaxAssociations_Type())
ceSctpMaxAssociations.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpMaxAssociations.setStatus(_A)
_CeSctpCurrEstab_Type=Counter32
_CeSctpCurrEstab_Object=MibScalar
ceSctpCurrEstab=_CeSctpCurrEstab_Object((1,3,6,1,4,1,9,10,74,1,1,3),_CeSctpCurrEstab_Type())
ceSctpCurrEstab.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpCurrEstab.setStatus(_A)
_CeSctpActiveEstab_Type=Counter32
_CeSctpActiveEstab_Object=MibScalar
ceSctpActiveEstab=_CeSctpActiveEstab_Object((1,3,6,1,4,1,9,10,74,1,1,4),_CeSctpActiveEstab_Type())
ceSctpActiveEstab.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpActiveEstab.setStatus(_A)
_CeSctpPassiveEstab_Type=Counter32
_CeSctpPassiveEstab_Object=MibScalar
ceSctpPassiveEstab=_CeSctpPassiveEstab_Object((1,3,6,1,4,1,9,10,74,1,1,5),_CeSctpPassiveEstab_Type())
ceSctpPassiveEstab.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpPassiveEstab.setStatus(_A)
_CeSctpAborted_Type=Counter32
_CeSctpAborted_Object=MibScalar
ceSctpAborted=_CeSctpAborted_Object((1,3,6,1,4,1,9,10,74,1,1,6),_CeSctpAborted_Type())
ceSctpAborted.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAborted.setStatus(_A)
_CeSctpShutdowns_Type=Counter32
_CeSctpShutdowns_Object=MibScalar
ceSctpShutdowns=_CeSctpShutdowns_Object((1,3,6,1,4,1,9,10,74,1,1,7),_CeSctpShutdowns_Type())
ceSctpShutdowns.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpShutdowns.setStatus(_A)
_CeSctpStatBytesRec_Type=Counter64
_CeSctpStatBytesRec_Object=MibScalar
ceSctpStatBytesRec=_CeSctpStatBytesRec_Object((1,3,6,1,4,1,9,10,74,1,1,8),_CeSctpStatBytesRec_Type())
ceSctpStatBytesRec.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpStatBytesRec.setStatus(_A)
_CeSctpStatBytesSent_Type=Counter64
_CeSctpStatBytesSent_Object=MibScalar
ceSctpStatBytesSent=_CeSctpStatBytesSent_Object((1,3,6,1,4,1,9,10,74,1,1,9),_CeSctpStatBytesSent_Type())
ceSctpStatBytesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpStatBytesSent.setStatus(_A)
_CeSctpStatChunksDiscard_Type=Counter64
_CeSctpStatChunksDiscard_Object=MibScalar
ceSctpStatChunksDiscard=_CeSctpStatChunksDiscard_Object((1,3,6,1,4,1,9,10,74,1,1,10),_CeSctpStatChunksDiscard_Type())
ceSctpStatChunksDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpStatChunksDiscard.setStatus(_A)
_CeSctpStatChunksSent_Type=Counter64
_CeSctpStatChunksSent_Object=MibScalar
ceSctpStatChunksSent=_CeSctpStatChunksSent_Object((1,3,6,1,4,1,9,10,74,1,1,11),_CeSctpStatChunksSent_Type())
ceSctpStatChunksSent.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpStatChunksSent.setStatus(_A)
_CeSctpStatChunksSentControl_Type=Counter64
_CeSctpStatChunksSentControl_Object=MibScalar
ceSctpStatChunksSentControl=_CeSctpStatChunksSentControl_Object((1,3,6,1,4,1,9,10,74,1,1,12),_CeSctpStatChunksSentControl_Type())
ceSctpStatChunksSentControl.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpStatChunksSentControl.setStatus(_A)
_CeSctpStatChunksSentOrdered_Type=Counter64
_CeSctpStatChunksSentOrdered_Object=MibScalar
ceSctpStatChunksSentOrdered=_CeSctpStatChunksSentOrdered_Object((1,3,6,1,4,1,9,10,74,1,1,13),_CeSctpStatChunksSentOrdered_Type())
ceSctpStatChunksSentOrdered.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpStatChunksSentOrdered.setStatus(_A)
_CeSctpStatChunksSentUnOrdered_Type=Counter64
_CeSctpStatChunksSentUnOrdered_Object=MibScalar
ceSctpStatChunksSentUnOrdered=_CeSctpStatChunksSentUnOrdered_Object((1,3,6,1,4,1,9,10,74,1,1,14),_CeSctpStatChunksSentUnOrdered_Type())
ceSctpStatChunksSentUnOrdered.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpStatChunksSentUnOrdered.setStatus(_A)
_CeSctpStatChunksRec_Type=Counter64
_CeSctpStatChunksRec_Object=MibScalar
ceSctpStatChunksRec=_CeSctpStatChunksRec_Object((1,3,6,1,4,1,9,10,74,1,1,15),_CeSctpStatChunksRec_Type())
ceSctpStatChunksRec.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpStatChunksRec.setStatus(_A)
_CeSctpStatChunksRecControl_Type=Counter64
_CeSctpStatChunksRecControl_Object=MibScalar
ceSctpStatChunksRecControl=_CeSctpStatChunksRecControl_Object((1,3,6,1,4,1,9,10,74,1,1,16),_CeSctpStatChunksRecControl_Type())
ceSctpStatChunksRecControl.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpStatChunksRecControl.setStatus(_A)
_CeSctpStatChunksRecOrdered_Type=Counter64
_CeSctpStatChunksRecOrdered_Object=MibScalar
ceSctpStatChunksRecOrdered=_CeSctpStatChunksRecOrdered_Object((1,3,6,1,4,1,9,10,74,1,1,17),_CeSctpStatChunksRecOrdered_Type())
ceSctpStatChunksRecOrdered.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpStatChunksRecOrdered.setStatus(_A)
_CeSctpStatChunksRecUnOrdered_Type=Counter64
_CeSctpStatChunksRecUnOrdered_Object=MibScalar
ceSctpStatChunksRecUnOrdered=_CeSctpStatChunksRecUnOrdered_Object((1,3,6,1,4,1,9,10,74,1,1,18),_CeSctpStatChunksRecUnOrdered_Type())
ceSctpStatChunksRecUnOrdered.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpStatChunksRecUnOrdered.setStatus(_A)
_CeSctpStatDatagramsRec_Type=Counter64
_CeSctpStatDatagramsRec_Object=MibScalar
ceSctpStatDatagramsRec=_CeSctpStatDatagramsRec_Object((1,3,6,1,4,1,9,10,74,1,1,19),_CeSctpStatDatagramsRec_Type())
ceSctpStatDatagramsRec.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpStatDatagramsRec.setStatus(_A)
_CeSctpStatDatagramsSent_Type=Counter64
_CeSctpStatDatagramsSent_Object=MibScalar
ceSctpStatDatagramsSent=_CeSctpStatDatagramsSent_Object((1,3,6,1,4,1,9,10,74,1,1,20),_CeSctpStatDatagramsSent_Type())
ceSctpStatDatagramsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpStatDatagramsSent.setStatus(_A)
_CeSctpStatFragmentedUsrMessages_Type=Counter64
_CeSctpStatFragmentedUsrMessages_Object=MibScalar
ceSctpStatFragmentedUsrMessages=_CeSctpStatFragmentedUsrMessages_Object((1,3,6,1,4,1,9,10,74,1,1,21),_CeSctpStatFragmentedUsrMessages_Type())
ceSctpStatFragmentedUsrMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpStatFragmentedUsrMessages.setStatus(_A)
_CeSctpStatReassembledUsrMessages_Type=Counter64
_CeSctpStatReassembledUsrMessages_Object=MibScalar
ceSctpStatReassembledUsrMessages=_CeSctpStatReassembledUsrMessages_Object((1,3,6,1,4,1,9,10,74,1,1,22),_CeSctpStatReassembledUsrMessages_Type())
ceSctpStatReassembledUsrMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpStatReassembledUsrMessages.setStatus(_A)
_CeSctpStatChunksReTrans_Type=Counter64
_CeSctpStatChunksReTrans_Object=MibScalar
ceSctpStatChunksReTrans=_CeSctpStatChunksReTrans_Object((1,3,6,1,4,1,9,10,74,1,1,23),_CeSctpStatChunksReTrans_Type())
ceSctpStatChunksReTrans.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpStatChunksReTrans.setStatus(_A)
_CeSctpStatOutOfBlue_Type=Counter64
_CeSctpStatOutOfBlue_Object=MibScalar
ceSctpStatOutOfBlue=_CeSctpStatOutOfBlue_Object((1,3,6,1,4,1,9,10,74,1,1,24),_CeSctpStatOutOfBlue_Type())
ceSctpStatOutOfBlue.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpStatOutOfBlue.setStatus(_A)
_CeSctpStatT1expired_Type=Counter32
_CeSctpStatT1expired_Object=MibScalar
ceSctpStatT1expired=_CeSctpStatT1expired_Object((1,3,6,1,4,1,9,10,74,1,1,25),_CeSctpStatT1expired_Type())
ceSctpStatT1expired.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpStatT1expired.setStatus(_A)
_CeSctpStatT2expired_Type=Counter32
_CeSctpStatT2expired_Object=MibScalar
ceSctpStatT2expired=_CeSctpStatT2expired_Object((1,3,6,1,4,1,9,10,74,1,1,26),_CeSctpStatT2expired_Type())
ceSctpStatT2expired.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpStatT2expired.setStatus(_A)
_CeSctpTables_ObjectIdentity=ObjectIdentity
ceSctpTables=_CeSctpTables_ObjectIdentity((1,3,6,1,4,1,9,10,74,1,2))
_CeSctpAssocTable_Object=MibTable
ceSctpAssocTable=_CeSctpAssocTable_Object((1,3,6,1,4,1,9,10,74,1,2,1))
if mibBuilder.loadTexts:ceSctpAssocTable.setStatus(_A)
_CeSctpAssocEntry_Object=MibTableRow
ceSctpAssocEntry=_CeSctpAssocEntry_Object((1,3,6,1,4,1,9,10,74,1,2,1,1))
ceSctpAssocEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:ceSctpAssocEntry.setStatus(_A)
class _CeSctpAssocId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_CeSctpAssocId_Type.__name__=_D
_CeSctpAssocId_Object=MibTableColumn
ceSctpAssocId=_CeSctpAssocId_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,1),_CeSctpAssocId_Type())
ceSctpAssocId.setMaxAccess(_G)
if mibBuilder.loadTexts:ceSctpAssocId.setStatus(_A)
class _CeSctpAssocState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('closed',1),('cookieWait',2),('cookieEchoed',3),('established',4),('shutdownPending',5),('shutdownSent',6),('shutdownReceived',7),('shutdownAckSent',8),('deleteTCB',9),('retrieval',10)))
_CeSctpAssocState_Type.__name__=_F
_CeSctpAssocState_Object=MibTableColumn
ceSctpAssocState=_CeSctpAssocState_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,2),_CeSctpAssocState_Type())
ceSctpAssocState.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocState.setStatus(_A)
_CeSctpAssocUpTime_Type=TimeTicks
_CeSctpAssocUpTime_Object=MibTableColumn
ceSctpAssocUpTime=_CeSctpAssocUpTime_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,3),_CeSctpAssocUpTime_Type())
ceSctpAssocUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocUpTime.setStatus(_A)
class _CeSctpAssocRtoMin_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,3600000))
_CeSctpAssocRtoMin_Type.__name__=_D
_CeSctpAssocRtoMin_Object=MibTableColumn
ceSctpAssocRtoMin=_CeSctpAssocRtoMin_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,4),_CeSctpAssocRtoMin_Type())
ceSctpAssocRtoMin.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocRtoMin.setStatus(_A)
if mibBuilder.loadTexts:ceSctpAssocRtoMin.setUnits(_E)
class _CeSctpAssocRtoMax_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,3600000))
_CeSctpAssocRtoMax_Type.__name__=_D
_CeSctpAssocRtoMax_Object=MibTableColumn
ceSctpAssocRtoMax=_CeSctpAssocRtoMax_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,5),_CeSctpAssocRtoMax_Type())
ceSctpAssocRtoMax.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocRtoMax.setStatus(_A)
if mibBuilder.loadTexts:ceSctpAssocRtoMax.setUnits(_E)
class _CeSctpAssocRtoInitial_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,3600000))
_CeSctpAssocRtoInitial_Type.__name__=_D
_CeSctpAssocRtoInitial_Object=MibTableColumn
ceSctpAssocRtoInitial=_CeSctpAssocRtoInitial_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,6),_CeSctpAssocRtoInitial_Type())
ceSctpAssocRtoInitial.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocRtoInitial.setStatus(_A)
if mibBuilder.loadTexts:ceSctpAssocRtoInitial.setUnits(_E)
class _CeSctpAssocValCookieLife_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,3600000))
_CeSctpAssocValCookieLife_Type.__name__=_D
_CeSctpAssocValCookieLife_Object=MibTableColumn
ceSctpAssocValCookieLife=_CeSctpAssocValCookieLife_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,7),_CeSctpAssocValCookieLife_Type())
ceSctpAssocValCookieLife.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocValCookieLife.setStatus(_A)
if mibBuilder.loadTexts:ceSctpAssocValCookieLife.setUnits(_E)
class _CeSctpAssocMaxInitRetr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,3600000))
_CeSctpAssocMaxInitRetr_Type.__name__=_D
_CeSctpAssocMaxInitRetr_Object=MibTableColumn
ceSctpAssocMaxInitRetr=_CeSctpAssocMaxInitRetr_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,8),_CeSctpAssocMaxInitRetr_Type())
ceSctpAssocMaxInitRetr.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocMaxInitRetr.setStatus(_A)
class _CeSctpAssocInitialT1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,3600000))
_CeSctpAssocInitialT1_Type.__name__=_D
_CeSctpAssocInitialT1_Object=MibTableColumn
ceSctpAssocInitialT1=_CeSctpAssocInitialT1_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,9),_CeSctpAssocInitialT1_Type())
ceSctpAssocInitialT1.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocInitialT1.setStatus(_A)
if mibBuilder.loadTexts:ceSctpAssocInitialT1.setUnits(_E)
class _CeSctpAssocInitialT2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1000,3600000))
_CeSctpAssocInitialT2_Type.__name__=_D
_CeSctpAssocInitialT2_Object=MibTableColumn
ceSctpAssocInitialT2=_CeSctpAssocInitialT2_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,10),_CeSctpAssocInitialT2_Type())
ceSctpAssocInitialT2.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocInitialT2.setStatus(_A)
if mibBuilder.loadTexts:ceSctpAssocInitialT2.setUnits(_E)
class _CeSctpAssocRemHostName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CeSctpAssocRemHostName_Type.__name__=_J
_CeSctpAssocRemHostName_Object=MibTableColumn
ceSctpAssocRemHostName=_CeSctpAssocRemHostName_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,11),_CeSctpAssocRemHostName_Type())
ceSctpAssocRemHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocRemHostName.setStatus(_A)
class _CeSctpAssocLocalSCTPPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4096,32767))
_CeSctpAssocLocalSCTPPort_Type.__name__=_D
_CeSctpAssocLocalSCTPPort_Object=MibTableColumn
ceSctpAssocLocalSCTPPort=_CeSctpAssocLocalSCTPPort_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,12),_CeSctpAssocLocalSCTPPort_Type())
ceSctpAssocLocalSCTPPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocLocalSCTPPort.setStatus(_A)
class _CeSctpAssocRemSCTPPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4096,32767))
_CeSctpAssocRemSCTPPort_Type.__name__=_D
_CeSctpAssocRemSCTPPort_Object=MibTableColumn
ceSctpAssocRemSCTPPort=_CeSctpAssocRemSCTPPort_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,13),_CeSctpAssocRemSCTPPort_Type())
ceSctpAssocRemSCTPPort.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocRemSCTPPort.setStatus(_A)
_CeSctpAssocRemPrimaryAddressType_Type=InetAddressType
_CeSctpAssocRemPrimaryAddressType_Object=MibTableColumn
ceSctpAssocRemPrimaryAddressType=_CeSctpAssocRemPrimaryAddressType_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,14),_CeSctpAssocRemPrimaryAddressType_Type())
ceSctpAssocRemPrimaryAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocRemPrimaryAddressType.setStatus(_A)
_CeSctpAssocRemPrimaryAddress_Type=InetAddress
_CeSctpAssocRemPrimaryAddress_Object=MibTableColumn
ceSctpAssocRemPrimaryAddress=_CeSctpAssocRemPrimaryAddress_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,15),_CeSctpAssocRemPrimaryAddress_Type())
ceSctpAssocRemPrimaryAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocRemPrimaryAddress.setStatus(_A)
class _CeSctpAssocCongestionLevels_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_CeSctpAssocCongestionLevels_Type.__name__=_D
_CeSctpAssocCongestionLevels_Object=MibTableColumn
ceSctpAssocCongestionLevels=_CeSctpAssocCongestionLevels_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,16),_CeSctpAssocCongestionLevels_Type())
ceSctpAssocCongestionLevels.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocCongestionLevels.setStatus(_A)
class _CeSctpAssocCongestionLevelsCur_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_CeSctpAssocCongestionLevelsCur_Type.__name__=_D
_CeSctpAssocCongestionLevelsCur_Object=MibTableColumn
ceSctpAssocCongestionLevelsCur=_CeSctpAssocCongestionLevelsCur_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,17),_CeSctpAssocCongestionLevelsCur_Type())
ceSctpAssocCongestionLevelsCur.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocCongestionLevelsCur.setStatus(_A)
class _CeSctpAssocCongestionAbate1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_CeSctpAssocCongestionAbate1_Type.__name__=_D
_CeSctpAssocCongestionAbate1_Object=MibTableColumn
ceSctpAssocCongestionAbate1=_CeSctpAssocCongestionAbate1_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,18),_CeSctpAssocCongestionAbate1_Type())
ceSctpAssocCongestionAbate1.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocCongestionAbate1.setStatus(_A)
class _CeSctpAssocCongestionAbate2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_CeSctpAssocCongestionAbate2_Type.__name__=_D
_CeSctpAssocCongestionAbate2_Object=MibTableColumn
ceSctpAssocCongestionAbate2=_CeSctpAssocCongestionAbate2_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,19),_CeSctpAssocCongestionAbate2_Type())
ceSctpAssocCongestionAbate2.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocCongestionAbate2.setStatus(_A)
class _CeSctpAssocCongestionAbate3_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_CeSctpAssocCongestionAbate3_Type.__name__=_D
_CeSctpAssocCongestionAbate3_Object=MibTableColumn
ceSctpAssocCongestionAbate3=_CeSctpAssocCongestionAbate3_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,20),_CeSctpAssocCongestionAbate3_Type())
ceSctpAssocCongestionAbate3.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocCongestionAbate3.setStatus(_A)
class _CeSctpAssocCongestionOnset1_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_CeSctpAssocCongestionOnset1_Type.__name__=_D
_CeSctpAssocCongestionOnset1_Object=MibTableColumn
ceSctpAssocCongestionOnset1=_CeSctpAssocCongestionOnset1_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,21),_CeSctpAssocCongestionOnset1_Type())
ceSctpAssocCongestionOnset1.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocCongestionOnset1.setStatus(_A)
class _CeSctpAssocCongestionOnset2_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_CeSctpAssocCongestionOnset2_Type.__name__=_D
_CeSctpAssocCongestionOnset2_Object=MibTableColumn
ceSctpAssocCongestionOnset2=_CeSctpAssocCongestionOnset2_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,22),_CeSctpAssocCongestionOnset2_Type())
ceSctpAssocCongestionOnset2.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocCongestionOnset2.setStatus(_A)
class _CeSctpAssocCongestionOnset3_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32767))
_CeSctpAssocCongestionOnset3_Type.__name__=_D
_CeSctpAssocCongestionOnset3_Object=MibTableColumn
ceSctpAssocCongestionOnset3=_CeSctpAssocCongestionOnset3_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,23),_CeSctpAssocCongestionOnset3_Type())
ceSctpAssocCongestionOnset3.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocCongestionOnset3.setStatus(_A)
class _CeSctpAssocInStreams_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CeSctpAssocInStreams_Type.__name__=_D
_CeSctpAssocInStreams_Object=MibTableColumn
ceSctpAssocInStreams=_CeSctpAssocInStreams_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,24),_CeSctpAssocInStreams_Type())
ceSctpAssocInStreams.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocInStreams.setStatus(_A)
class _CeSctpAssocOutStreams_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CeSctpAssocOutStreams_Type.__name__=_D
_CeSctpAssocOutStreams_Object=MibTableColumn
ceSctpAssocOutStreams=_CeSctpAssocOutStreams_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,25),_CeSctpAssocOutStreams_Type())
ceSctpAssocOutStreams.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocOutStreams.setStatus(_A)
class _CeSctpAssocMaxRetr_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32767))
_CeSctpAssocMaxRetr_Type.__name__=_D
_CeSctpAssocMaxRetr_Object=MibTableColumn
ceSctpAssocMaxRetr=_CeSctpAssocMaxRetr_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,26),_CeSctpAssocMaxRetr_Type())
ceSctpAssocMaxRetr.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocMaxRetr.setStatus(_A)
class _CeSctpAssocMTU_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CeSctpAssocMTU_Type.__name__=_D
_CeSctpAssocMTU_Object=MibTableColumn
ceSctpAssocMTU=_CeSctpAssocMTU_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,27),_CeSctpAssocMTU_Type())
ceSctpAssocMTU.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocMTU.setStatus(_A)
if mibBuilder.loadTexts:ceSctpAssocMTU.setUnits(_H)
class _CeSctpAssocLocRecWnd_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CeSctpAssocLocRecWnd_Type.__name__=_D
_CeSctpAssocLocRecWnd_Object=MibTableColumn
ceSctpAssocLocRecWnd=_CeSctpAssocLocRecWnd_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,28),_CeSctpAssocLocRecWnd_Type())
ceSctpAssocLocRecWnd.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocLocRecWnd.setStatus(_A)
if mibBuilder.loadTexts:ceSctpAssocLocRecWnd.setUnits(_H)
class _CeSctpAssocLocRecWndLowMark_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CeSctpAssocLocRecWndLowMark_Type.__name__=_D
_CeSctpAssocLocRecWndLowMark_Object=MibTableColumn
ceSctpAssocLocRecWndLowMark=_CeSctpAssocLocRecWndLowMark_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,29),_CeSctpAssocLocRecWndLowMark_Type())
ceSctpAssocLocRecWndLowMark.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocLocRecWndLowMark.setStatus(_A)
if mibBuilder.loadTexts:ceSctpAssocLocRecWndLowMark.setUnits(_H)
_CeSctpAssocLocRecWndZeroCnt_Type=Counter64
_CeSctpAssocLocRecWndZeroCnt_Object=MibTableColumn
ceSctpAssocLocRecWndZeroCnt=_CeSctpAssocLocRecWndZeroCnt_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,30),_CeSctpAssocLocRecWndZeroCnt_Type())
ceSctpAssocLocRecWndZeroCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocLocRecWndZeroCnt.setStatus(_A)
class _CeSctpAssocRemRecWnd_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CeSctpAssocRemRecWnd_Type.__name__=_D
_CeSctpAssocRemRecWnd_Object=MibTableColumn
ceSctpAssocRemRecWnd=_CeSctpAssocRemRecWnd_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,31),_CeSctpAssocRemRecWnd_Type())
ceSctpAssocRemRecWnd.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocRemRecWnd.setStatus(_A)
if mibBuilder.loadTexts:ceSctpAssocRemRecWnd.setUnits(_H)
class _CeSctpAssocRemRecWndLowMark_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CeSctpAssocRemRecWndLowMark_Type.__name__=_D
_CeSctpAssocRemRecWndLowMark_Object=MibTableColumn
ceSctpAssocRemRecWndLowMark=_CeSctpAssocRemRecWndLowMark_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,32),_CeSctpAssocRemRecWndLowMark_Type())
ceSctpAssocRemRecWndLowMark.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocRemRecWndLowMark.setStatus(_A)
if mibBuilder.loadTexts:ceSctpAssocRemRecWndLowMark.setUnits(_H)
_CeSctpAssocRemRecWndZeroCnt_Type=Counter64
_CeSctpAssocRemRecWndZeroCnt_Object=MibTableColumn
ceSctpAssocRemRecWndZeroCnt=_CeSctpAssocRemRecWndZeroCnt_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,33),_CeSctpAssocRemRecWndZeroCnt_Type())
ceSctpAssocRemRecWndZeroCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocRemRecWndZeroCnt.setStatus(_A)
class _CeSctpAssocULPDatagramsQueued_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CeSctpAssocULPDatagramsQueued_Type.__name__=_D
_CeSctpAssocULPDatagramsQueued_Object=MibTableColumn
ceSctpAssocULPDatagramsQueued=_CeSctpAssocULPDatagramsQueued_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,34),_CeSctpAssocULPDatagramsQueued_Type())
ceSctpAssocULPDatagramsQueued.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocULPDatagramsQueued.setStatus(_A)
if mibBuilder.loadTexts:ceSctpAssocULPDatagramsQueued.setUnits(_K)
class _CeSctpAssocULPDatagramsQueuedHigh_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CeSctpAssocULPDatagramsQueuedHigh_Type.__name__=_D
_CeSctpAssocULPDatagramsQueuedHigh_Object=MibTableColumn
ceSctpAssocULPDatagramsQueuedHigh=_CeSctpAssocULPDatagramsQueuedHigh_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,35),_CeSctpAssocULPDatagramsQueuedHigh_Type())
ceSctpAssocULPDatagramsQueuedHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocULPDatagramsQueuedHigh.setStatus(_A)
if mibBuilder.loadTexts:ceSctpAssocULPDatagramsQueuedHigh.setUnits(_K)
_CeSctpAssocChecksumErrorCounter_Type=Counter64
_CeSctpAssocChecksumErrorCounter_Object=MibTableColumn
ceSctpAssocChecksumErrorCounter=_CeSctpAssocChecksumErrorCounter_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,36),_CeSctpAssocChecksumErrorCounter_Type())
ceSctpAssocChecksumErrorCounter.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocChecksumErrorCounter.setStatus(_A)
_CeSctpAssocBytesSent_Type=Counter64
_CeSctpAssocBytesSent_Object=MibTableColumn
ceSctpAssocBytesSent=_CeSctpAssocBytesSent_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,37),_CeSctpAssocBytesSent_Type())
ceSctpAssocBytesSent.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocBytesSent.setStatus(_A)
_CeSctpAssocBytesRec_Type=Counter64
_CeSctpAssocBytesRec_Object=MibTableColumn
ceSctpAssocBytesRec=_CeSctpAssocBytesRec_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,38),_CeSctpAssocBytesRec_Type())
ceSctpAssocBytesRec.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocBytesRec.setStatus(_A)
_CeSctpAssocChunksDiscarded_Type=Counter64
_CeSctpAssocChunksDiscarded_Object=MibTableColumn
ceSctpAssocChunksDiscarded=_CeSctpAssocChunksDiscarded_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,39),_CeSctpAssocChunksDiscarded_Type())
ceSctpAssocChunksDiscarded.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocChunksDiscarded.setStatus(_A)
_CeSctpAssocChunksRec_Type=Counter64
_CeSctpAssocChunksRec_Object=MibTableColumn
ceSctpAssocChunksRec=_CeSctpAssocChunksRec_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,40),_CeSctpAssocChunksRec_Type())
ceSctpAssocChunksRec.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocChunksRec.setStatus(_A)
_CeSctpAssocChunksRecControl_Type=Counter64
_CeSctpAssocChunksRecControl_Object=MibTableColumn
ceSctpAssocChunksRecControl=_CeSctpAssocChunksRecControl_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,41),_CeSctpAssocChunksRecControl_Type())
ceSctpAssocChunksRecControl.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocChunksRecControl.setStatus(_A)
_CeSctpAssocChunksRecOrdered_Type=Counter64
_CeSctpAssocChunksRecOrdered_Object=MibTableColumn
ceSctpAssocChunksRecOrdered=_CeSctpAssocChunksRecOrdered_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,42),_CeSctpAssocChunksRecOrdered_Type())
ceSctpAssocChunksRecOrdered.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocChunksRecOrdered.setStatus(_A)
_CeSctpAssocChunksRecUnOrdered_Type=Counter64
_CeSctpAssocChunksRecUnOrdered_Object=MibTableColumn
ceSctpAssocChunksRecUnOrdered=_CeSctpAssocChunksRecUnOrdered_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,43),_CeSctpAssocChunksRecUnOrdered_Type())
ceSctpAssocChunksRecUnOrdered.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocChunksRecUnOrdered.setStatus(_A)
_CeSctpAssocChunksRecOutOrder_Type=Counter64
_CeSctpAssocChunksRecOutOrder_Object=MibTableColumn
ceSctpAssocChunksRecOutOrder=_CeSctpAssocChunksRecOutOrder_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,44),_CeSctpAssocChunksRecOutOrder_Type())
ceSctpAssocChunksRecOutOrder.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocChunksRecOutOrder.setStatus(_A)
_CeSctpAssocChunksReTrans_Type=Counter64
_CeSctpAssocChunksReTrans_Object=MibTableColumn
ceSctpAssocChunksReTrans=_CeSctpAssocChunksReTrans_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,45),_CeSctpAssocChunksReTrans_Type())
ceSctpAssocChunksReTrans.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocChunksReTrans.setStatus(_A)
_CeSctpAssocChunksSent_Type=Counter64
_CeSctpAssocChunksSent_Object=MibTableColumn
ceSctpAssocChunksSent=_CeSctpAssocChunksSent_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,46),_CeSctpAssocChunksSent_Type())
ceSctpAssocChunksSent.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocChunksSent.setStatus(_A)
_CeSctpAssocChunksSentControl_Type=Counter64
_CeSctpAssocChunksSentControl_Object=MibTableColumn
ceSctpAssocChunksSentControl=_CeSctpAssocChunksSentControl_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,47),_CeSctpAssocChunksSentControl_Type())
ceSctpAssocChunksSentControl.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocChunksSentControl.setStatus(_A)
_CeSctpAssocChunksSentOrdered_Type=Counter64
_CeSctpAssocChunksSentOrdered_Object=MibTableColumn
ceSctpAssocChunksSentOrdered=_CeSctpAssocChunksSentOrdered_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,48),_CeSctpAssocChunksSentOrdered_Type())
ceSctpAssocChunksSentOrdered.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocChunksSentOrdered.setStatus(_A)
_CeSctpAssocChunksSentUnOrdered_Type=Counter64
_CeSctpAssocChunksSentUnOrdered_Object=MibTableColumn
ceSctpAssocChunksSentUnOrdered=_CeSctpAssocChunksSentUnOrdered_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,49),_CeSctpAssocChunksSentUnOrdered_Type())
ceSctpAssocChunksSentUnOrdered.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocChunksSentUnOrdered.setStatus(_A)
_CeSctpAssocDatagramsRec_Type=Counter64
_CeSctpAssocDatagramsRec_Object=MibTableColumn
ceSctpAssocDatagramsRec=_CeSctpAssocDatagramsRec_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,50),_CeSctpAssocDatagramsRec_Type())
ceSctpAssocDatagramsRec.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocDatagramsRec.setStatus(_A)
_CeSctpAssocDatagramsSent_Type=Counter64
_CeSctpAssocDatagramsSent_Object=MibTableColumn
ceSctpAssocDatagramsSent=_CeSctpAssocDatagramsSent_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,51),_CeSctpAssocDatagramsSent_Type())
ceSctpAssocDatagramsSent.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocDatagramsSent.setStatus(_A)
_CeSctpAssocRowStatus_Type=RowStatus
_CeSctpAssocRowStatus_Object=MibTableColumn
ceSctpAssocRowStatus=_CeSctpAssocRowStatus_Object((1,3,6,1,4,1,9,10,74,1,2,1,1,52),_CeSctpAssocRowStatus_Type())
ceSctpAssocRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocRowStatus.setStatus(_A)
_CeSctpAssocLocalAddressTable_Object=MibTable
ceSctpAssocLocalAddressTable=_CeSctpAssocLocalAddressTable_Object((1,3,6,1,4,1,9,10,74,1,2,2))
if mibBuilder.loadTexts:ceSctpAssocLocalAddressTable.setStatus(_A)
_CeSctpAssocLocalAddressEntry_Object=MibTableRow
ceSctpAssocLocalAddressEntry=_CeSctpAssocLocalAddressEntry_Object((1,3,6,1,4,1,9,10,74,1,2,2,1))
ceSctpAssocLocalAddressEntry.setIndexNames((0,_B,_I),(0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:ceSctpAssocLocalAddressEntry.setStatus(_A)
_CeSctpAssocLocalAddressIPType_Type=InetAddressType
_CeSctpAssocLocalAddressIPType_Object=MibTableColumn
ceSctpAssocLocalAddressIPType=_CeSctpAssocLocalAddressIPType_Object((1,3,6,1,4,1,9,10,74,1,2,2,1,1),_CeSctpAssocLocalAddressIPType_Type())
ceSctpAssocLocalAddressIPType.setMaxAccess(_G)
if mibBuilder.loadTexts:ceSctpAssocLocalAddressIPType.setStatus(_A)
_CeSctpAssocLocalAddressIP_Type=InetAddress
_CeSctpAssocLocalAddressIP_Object=MibTableColumn
ceSctpAssocLocalAddressIP=_CeSctpAssocLocalAddressIP_Object((1,3,6,1,4,1,9,10,74,1,2,2,1,2),_CeSctpAssocLocalAddressIP_Type())
ceSctpAssocLocalAddressIP.setMaxAccess(_G)
if mibBuilder.loadTexts:ceSctpAssocLocalAddressIP.setStatus(_A)
_CeSctpAssocLocalAddressRowStatus_Type=RowStatus
_CeSctpAssocLocalAddressRowStatus_Object=MibTableColumn
ceSctpAssocLocalAddressRowStatus=_CeSctpAssocLocalAddressRowStatus_Object((1,3,6,1,4,1,9,10,74,1,2,2,1,3),_CeSctpAssocLocalAddressRowStatus_Type())
ceSctpAssocLocalAddressRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocLocalAddressRowStatus.setStatus(_A)
_CeSctpAssocRemAddressTable_Object=MibTable
ceSctpAssocRemAddressTable=_CeSctpAssocRemAddressTable_Object((1,3,6,1,4,1,9,10,74,1,2,3))
if mibBuilder.loadTexts:ceSctpAssocRemAddressTable.setStatus(_A)
_CeSctpAssocRemAddressEntry_Object=MibTableRow
ceSctpAssocRemAddressEntry=_CeSctpAssocRemAddressEntry_Object((1,3,6,1,4,1,9,10,74,1,2,3,1))
ceSctpAssocRemAddressEntry.setIndexNames((0,_B,_I),(0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:ceSctpAssocRemAddressEntry.setStatus(_A)
_CeSctpAssocRemAddressIPType_Type=InetAddressType
_CeSctpAssocRemAddressIPType_Object=MibTableColumn
ceSctpAssocRemAddressIPType=_CeSctpAssocRemAddressIPType_Object((1,3,6,1,4,1,9,10,74,1,2,3,1,1),_CeSctpAssocRemAddressIPType_Type())
ceSctpAssocRemAddressIPType.setMaxAccess(_G)
if mibBuilder.loadTexts:ceSctpAssocRemAddressIPType.setStatus(_A)
_CeSctpAssocRemAddressIP_Type=InetAddress
_CeSctpAssocRemAddressIP_Object=MibTableColumn
ceSctpAssocRemAddressIP=_CeSctpAssocRemAddressIP_Object((1,3,6,1,4,1,9,10,74,1,2,3,1,2),_CeSctpAssocRemAddressIP_Type())
ceSctpAssocRemAddressIP.setMaxAccess(_G)
if mibBuilder.loadTexts:ceSctpAssocRemAddressIP.setStatus(_A)
class _CeSctpAssocRemAddressStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_P,0),(_Q,1),('failed',2)))
_CeSctpAssocRemAddressStatus_Type.__name__=_F
_CeSctpAssocRemAddressStatus_Object=MibTableColumn
ceSctpAssocRemAddressStatus=_CeSctpAssocRemAddressStatus_Object((1,3,6,1,4,1,9,10,74,1,2,3,1,3),_CeSctpAssocRemAddressStatus_Type())
ceSctpAssocRemAddressStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocRemAddressStatus.setStatus(_A)
class _CeSctpAssocRemAddressRTO_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CeSctpAssocRemAddressRTO_Type.__name__=_D
_CeSctpAssocRemAddressRTO_Object=MibTableColumn
ceSctpAssocRemAddressRTO=_CeSctpAssocRemAddressRTO_Object((1,3,6,1,4,1,9,10,74,1,2,3,1,4),_CeSctpAssocRemAddressRTO_Type())
ceSctpAssocRemAddressRTO.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocRemAddressRTO.setStatus(_A)
if mibBuilder.loadTexts:ceSctpAssocRemAddressRTO.setUnits(_E)
class _CeSctpAssocRemAddressHtBtFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_P,0),(_Q,1)))
_CeSctpAssocRemAddressHtBtFlag_Type.__name__=_F
_CeSctpAssocRemAddressHtBtFlag_Object=MibTableColumn
ceSctpAssocRemAddressHtBtFlag=_CeSctpAssocRemAddressHtBtFlag_Object((1,3,6,1,4,1,9,10,74,1,2,3,1,5),_CeSctpAssocRemAddressHtBtFlag_Type())
ceSctpAssocRemAddressHtBtFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocRemAddressHtBtFlag.setStatus(_A)
class _CeSctpAssocRemAddressHtBtTime_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CeSctpAssocRemAddressHtBtTime_Type.__name__=_D
_CeSctpAssocRemAddressHtBtTime_Object=MibTableColumn
ceSctpAssocRemAddressHtBtTime=_CeSctpAssocRemAddressHtBtTime_Object((1,3,6,1,4,1,9,10,74,1,2,3,1,6),_CeSctpAssocRemAddressHtBtTime_Type())
ceSctpAssocRemAddressHtBtTime.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocRemAddressHtBtTime.setStatus(_A)
if mibBuilder.loadTexts:ceSctpAssocRemAddressHtBtTime.setUnits(_E)
class _CeSctpAssocRemAddressMaxRetran_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CeSctpAssocRemAddressMaxRetran_Type.__name__=_D
_CeSctpAssocRemAddressMaxRetran_Object=MibTableColumn
ceSctpAssocRemAddressMaxRetran=_CeSctpAssocRemAddressMaxRetran_Object((1,3,6,1,4,1,9,10,74,1,2,3,1,7),_CeSctpAssocRemAddressMaxRetran_Type())
ceSctpAssocRemAddressMaxRetran.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocRemAddressMaxRetran.setStatus(_A)
_CeSctpAssocRemAddressRetransCnt_Type=Counter64
_CeSctpAssocRemAddressRetransCnt_Object=MibTableColumn
ceSctpAssocRemAddressRetransCnt=_CeSctpAssocRemAddressRetransCnt_Object((1,3,6,1,4,1,9,10,74,1,2,3,1,8),_CeSctpAssocRemAddressRetransCnt_Type())
ceSctpAssocRemAddressRetransCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocRemAddressRetransCnt.setStatus(_A)
class _CeSctpAssocRemAddressSRTT_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CeSctpAssocRemAddressSRTT_Type.__name__=_D
_CeSctpAssocRemAddressSRTT_Object=MibTableColumn
ceSctpAssocRemAddressSRTT=_CeSctpAssocRemAddressSRTT_Object((1,3,6,1,4,1,9,10,74,1,2,3,1,9),_CeSctpAssocRemAddressSRTT_Type())
ceSctpAssocRemAddressSRTT.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocRemAddressSRTT.setStatus(_A)
if mibBuilder.loadTexts:ceSctpAssocRemAddressSRTT.setUnits(_E)
_CeSctpAssocRemAddressRowStatus_Type=RowStatus
_CeSctpAssocRemAddressRowStatus_Object=MibTableColumn
ceSctpAssocRemAddressRowStatus=_CeSctpAssocRemAddressRowStatus_Object((1,3,6,1,4,1,9,10,74,1,2,3,1,10),_CeSctpAssocRemAddressRowStatus_Type())
ceSctpAssocRemAddressRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ceSctpAssocRemAddressRowStatus.setStatus(_A)
_CeSctpConformance_ObjectIdentity=ObjectIdentity
ceSctpConformance=_CeSctpConformance_ObjectIdentity((1,3,6,1,4,1,9,10,74,2))
_CeSctpGroups_ObjectIdentity=ObjectIdentity
ceSctpGroups=_CeSctpGroups_ObjectIdentity((1,3,6,1,4,1,9,10,74,2,1))
_CeSctpCompliances_ObjectIdentity=ObjectIdentity
ceSctpCompliances=_CeSctpCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,74,2,2))
ceSctpGeneralVariablesGroup=ObjectGroup((1,3,6,1,4,1,9,10,74,2,1,1))
ceSctpGeneralVariablesGroup.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:ceSctpGeneralVariablesGroup.setStatus(_A)
ceSctpStateStatGroup=ObjectGroup((1,3,6,1,4,1,9,10,74,2,1,2))
ceSctpStateStatGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:ceSctpStateStatGroup.setStatus(_A)
ceSctpOtherStatGroup=ObjectGroup((1,3,6,1,4,1,9,10,74,2,1,3))
ceSctpOtherStatGroup.setObjects(*((_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:ceSctpOtherStatGroup.setStatus(_A)
ceSctpAssocTablesVariablesGroup=ObjectGroup((1,3,6,1,4,1,9,10,74,2,1,4))
ceSctpAssocTablesVariablesGroup.setObjects(*((_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj),(_B,_Ak),(_B,_Al),(_B,_Am),(_B,_An)))
if mibBuilder.loadTexts:ceSctpAssocTablesVariablesGroup.setStatus(_A)
ceSctpAssocStatGroup=ObjectGroup((1,3,6,1,4,1,9,10,74,2,1,5))
ceSctpAssocStatGroup.setObjects((_B,_Ao))
if mibBuilder.loadTexts:ceSctpAssocStatGroup.setStatus(_A)
ceSctpCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,74,2,2,1))
ceSctpCompliance.setObjects(*((_B,_Ap),(_B,_Aq),(_B,_Ar),(_B,_As),(_B,_At)))
if mibBuilder.loadTexts:ceSctpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'InetAddressType':InetAddressType,'InetAddress':InetAddress,'ceSctpMIB':ceSctpMIB,'ceSctpObjects':ceSctpObjects,'ceSctpScalars':ceSctpScalars,_R:ceSctpRtoAlgorithm,_S:ceSctpMaxAssociations,_T:ceSctpCurrEstab,_U:ceSctpActiveEstab,_V:ceSctpPassiveEstab,_W:ceSctpAborted,_X:ceSctpShutdowns,_Y:ceSctpStatBytesRec,_Z:ceSctpStatBytesSent,_a:ceSctpStatChunksDiscard,_b:ceSctpStatChunksSent,_c:ceSctpStatChunksSentControl,_d:ceSctpStatChunksSentOrdered,_e:ceSctpStatChunksSentUnOrdered,_f:ceSctpStatChunksRec,_g:ceSctpStatChunksRecControl,_h:ceSctpStatChunksRecOrdered,_i:ceSctpStatChunksRecUnOrdered,_k:ceSctpStatDatagramsRec,_l:ceSctpStatDatagramsSent,_m:ceSctpStatFragmentedUsrMessages,_n:ceSctpStatReassembledUsrMessages,_j:ceSctpStatChunksReTrans,_o:ceSctpStatOutOfBlue,_p:ceSctpStatT1expired,_q:ceSctpStatT2expired,'ceSctpTables':ceSctpTables,'ceSctpAssocTable':ceSctpAssocTable,'ceSctpAssocEntry':ceSctpAssocEntry,_I:ceSctpAssocId,_r:ceSctpAssocState,_s:ceSctpAssocUpTime,_t:ceSctpAssocRtoMin,_u:ceSctpAssocRtoMax,_v:ceSctpAssocRtoInitial,_w:ceSctpAssocValCookieLife,_x:ceSctpAssocMaxInitRetr,_y:ceSctpAssocInitialT1,_z:ceSctpAssocInitialT2,_A0:ceSctpAssocRemHostName,_A1:ceSctpAssocLocalSCTPPort,_A2:ceSctpAssocRemSCTPPort,_A3:ceSctpAssocRemPrimaryAddressType,_A4:ceSctpAssocRemPrimaryAddress,_A5:ceSctpAssocCongestionLevels,_A6:ceSctpAssocCongestionLevelsCur,_A7:ceSctpAssocCongestionAbate1,_A8:ceSctpAssocCongestionAbate2,_A9:ceSctpAssocCongestionAbate3,_AA:ceSctpAssocCongestionOnset1,_AB:ceSctpAssocCongestionOnset2,_AC:ceSctpAssocCongestionOnset3,_AD:ceSctpAssocInStreams,_AE:ceSctpAssocOutStreams,_AF:ceSctpAssocMaxRetr,_AG:ceSctpAssocMTU,_AH:ceSctpAssocLocRecWnd,_AI:ceSctpAssocLocRecWndLowMark,_AJ:ceSctpAssocLocRecWndZeroCnt,_AK:ceSctpAssocRemRecWnd,_AL:ceSctpAssocRemRecWndLowMark,_AM:ceSctpAssocRemRecWndZeroCnt,_AN:ceSctpAssocULPDatagramsQueued,_AO:ceSctpAssocULPDatagramsQueuedHigh,_AP:ceSctpAssocChecksumErrorCounter,_AR:ceSctpAssocBytesSent,_AQ:ceSctpAssocBytesRec,_AS:ceSctpAssocChunksDiscarded,_AT:ceSctpAssocChunksRec,_AU:ceSctpAssocChunksRecControl,_AV:ceSctpAssocChunksRecOrdered,_AW:ceSctpAssocChunksRecUnOrdered,_AX:ceSctpAssocChunksRecOutOrder,_AY:ceSctpAssocChunksReTrans,_AZ:ceSctpAssocChunksSent,_Aa:ceSctpAssocChunksSentControl,_Ab:ceSctpAssocChunksSentOrdered,_Ac:ceSctpAssocChunksSentUnOrdered,_Ad:ceSctpAssocDatagramsRec,_Ae:ceSctpAssocDatagramsSent,_Af:ceSctpAssocRowStatus,'ceSctpAssocLocalAddressTable':ceSctpAssocLocalAddressTable,'ceSctpAssocLocalAddressEntry':ceSctpAssocLocalAddressEntry,_L:ceSctpAssocLocalAddressIPType,_M:ceSctpAssocLocalAddressIP,_Ag:ceSctpAssocLocalAddressRowStatus,'ceSctpAssocRemAddressTable':ceSctpAssocRemAddressTable,'ceSctpAssocRemAddressEntry':ceSctpAssocRemAddressEntry,_N:ceSctpAssocRemAddressIPType,_O:ceSctpAssocRemAddressIP,_Ah:ceSctpAssocRemAddressStatus,_Ai:ceSctpAssocRemAddressRTO,_Aj:ceSctpAssocRemAddressHtBtFlag,_Ak:ceSctpAssocRemAddressHtBtTime,_Al:ceSctpAssocRemAddressMaxRetran,_Ao:ceSctpAssocRemAddressRetransCnt,_Am:ceSctpAssocRemAddressSRTT,_An:ceSctpAssocRemAddressRowStatus,'ceSctpConformance':ceSctpConformance,'ceSctpGroups':ceSctpGroups,_Ap:ceSctpGeneralVariablesGroup,_Ar:ceSctpStateStatGroup,_As:ceSctpOtherStatGroup,_Aq:ceSctpAssocTablesVariablesGroup,_At:ceSctpAssocStatGroup,'ceSctpCompliances':ceSctpCompliances,'ceSctpCompliance':ceSctpCompliance})