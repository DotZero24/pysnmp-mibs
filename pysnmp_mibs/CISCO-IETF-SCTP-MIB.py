_AH='cSctpInverseGroup'
_AG='cSctpAssocStatGroup'
_AF='cSctpOtherStatGroup'
_AE='cSctpStateStatGroup'
_AD='cSctpAssocTablesVariablesGroup'
_AC='cSctpGeneralVariablesGroup'
_AB='cSctpLookupRemIPAddrStartTime'
_AA='cSctpLookupRemPrimIPAddrStartTime'
_A9='cSctpLookupRemHostNameStartTime'
_A8='cSctpLookupRemPortStartTime'
_A7='cSctpLookupLocalPortStartTime'
_A6='cSctpAssocRemAddressRtx'
_A5='cSctpAssocRemAddressStartTime'
_A4='cSctpAssocRemAddressMaxPathRtx'
_A3='cSctpAssocRemAddressRTO'
_A2='cSctpAssocRemAddressHBFlag'
_A1='cSctpAssocRemAddressStatus'
_A0='cSctpAssocLocalAddressStartTime'
_z='cSctpAssocStartTime'
_y='cSctpAssocRtxChunks'
_x='cSctpAssocT2expireds'
_w='cSctpAssocT1expireds'
_v='cSctpAssocMaxRetr'
_u='cSctpAssocOutStreams'
_t='cSctpAssocInStreams'
_s='cSctpAssocState'
_r='cSctpAssocHeartBeatTimer'
_q='cSctpStatRecSCTPPacks'
_p='cSctpStatSentSCTPPacks'
_o='cSctpStatReassembledUsrMessages'
_n='cSctpStatFragmentedUsrMessages'
_m='cSctpStatRecUnorderChunks'
_l='cSctpStatRecOrderChunks'
_k='cSctpStatRecCtrlChunks'
_j='cSctpStatSentUnorderChunks'
_i='cSctpStatSentOrderChunks'
_h='cSctpStatSentCtrlChunks'
_g='cSctpStatChecksumErrors'
_f='cSctpStatOutOfBlues'
_e='cSctpShutdowns'
_d='cSctpAborteds'
_c='cSctpPassiveEstabs'
_b='cSctpActiveEstabs'
_a='cSctpCurrEstab'
_Z='cSctpMaxInitRetr'
_Y='cSctpValCookieLife'
_X='cSctpMaxAssoc'
_W='cSctpRtoInitial'
_V='cSctpRtoMax'
_U='cSctpRtoMin'
_T='cSctpRtoAlgorithm'
_S='inactive'
_R='active'
_Q='cSctpAssocLocalAddressIP'
_P='cSctpAssocLocalAddressIPType'
_O='OctetString'
_N='cSctpAssocRemPrimaryAddress'
_M='cSctpAssocRemPrimaryAddressType'
_L='cSctpAssocRemHostName'
_K='cSctpAssocRemSCTPPort'
_J='cSctpAssocLocalSCTPPort'
_I='cSctpAssocRemAddressIP'
_H='cSctpAssocRemAddressIPType'
_G='not-accessible'
_F='Integer32'
_E='milliseconds'
_D='cSctpAssocId'
_C='read-only'
_B='CISCO-IETF-SCTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoExperiment,=mibBuilder.importSymbols('CISCO-SMI','ciscoExperiment')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
cSctpMIB=ModuleIdentity((1,3,6,1,4,1,9,10,75))
if mibBuilder.loadTexts:cSctpMIB.setRevisions(('2001-08-08 00:00',))
class InetPortNumber(TextualConvention,Unsigned32):status=_A
_CSctpObjects_ObjectIdentity=ObjectIdentity
cSctpObjects=_CSctpObjects_ObjectIdentity((1,3,6,1,4,1,9,10,75,1))
_CSctpScalars_ObjectIdentity=ObjectIdentity
cSctpScalars=_CSctpScalars_ObjectIdentity((1,3,6,1,4,1,9,10,75,1,1))
class _CSctpRtoAlgorithm_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('other',1),('vanj',2)))
_CSctpRtoAlgorithm_Type.__name__=_F
_CSctpRtoAlgorithm_Object=MibScalar
cSctpRtoAlgorithm=_CSctpRtoAlgorithm_Object((1,3,6,1,4,1,9,10,75,1,1,1),_CSctpRtoAlgorithm_Type())
cSctpRtoAlgorithm.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpRtoAlgorithm.setStatus(_A)
_CSctpRtoMin_Type=Unsigned32
_CSctpRtoMin_Object=MibScalar
cSctpRtoMin=_CSctpRtoMin_Object((1,3,6,1,4,1,9,10,75,1,1,2),_CSctpRtoMin_Type())
cSctpRtoMin.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpRtoMin.setStatus(_A)
if mibBuilder.loadTexts:cSctpRtoMin.setUnits(_E)
_CSctpRtoMax_Type=Unsigned32
_CSctpRtoMax_Object=MibScalar
cSctpRtoMax=_CSctpRtoMax_Object((1,3,6,1,4,1,9,10,75,1,1,3),_CSctpRtoMax_Type())
cSctpRtoMax.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpRtoMax.setStatus(_A)
if mibBuilder.loadTexts:cSctpRtoMax.setUnits(_E)
_CSctpRtoInitial_Type=Unsigned32
_CSctpRtoInitial_Object=MibScalar
cSctpRtoInitial=_CSctpRtoInitial_Object((1,3,6,1,4,1,9,10,75,1,1,4),_CSctpRtoInitial_Type())
cSctpRtoInitial.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpRtoInitial.setStatus(_A)
if mibBuilder.loadTexts:cSctpRtoInitial.setUnits(_E)
_CSctpMaxAssoc_Type=Unsigned32
_CSctpMaxAssoc_Object=MibScalar
cSctpMaxAssoc=_CSctpMaxAssoc_Object((1,3,6,1,4,1,9,10,75,1,1,5),_CSctpMaxAssoc_Type())
cSctpMaxAssoc.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpMaxAssoc.setStatus(_A)
_CSctpValCookieLife_Type=Unsigned32
_CSctpValCookieLife_Object=MibScalar
cSctpValCookieLife=_CSctpValCookieLife_Object((1,3,6,1,4,1,9,10,75,1,1,6),_CSctpValCookieLife_Type())
cSctpValCookieLife.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpValCookieLife.setStatus(_A)
if mibBuilder.loadTexts:cSctpValCookieLife.setUnits(_E)
_CSctpMaxInitRetr_Type=Unsigned32
_CSctpMaxInitRetr_Object=MibScalar
cSctpMaxInitRetr=_CSctpMaxInitRetr_Object((1,3,6,1,4,1,9,10,75,1,1,7),_CSctpMaxInitRetr_Type())
cSctpMaxInitRetr.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpMaxInitRetr.setStatus(_A)
_CSctpCurrEstab_Type=Gauge32
_CSctpCurrEstab_Object=MibScalar
cSctpCurrEstab=_CSctpCurrEstab_Object((1,3,6,1,4,1,9,10,75,1,1,8),_CSctpCurrEstab_Type())
cSctpCurrEstab.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpCurrEstab.setStatus(_A)
_CSctpActiveEstabs_Type=Counter64
_CSctpActiveEstabs_Object=MibScalar
cSctpActiveEstabs=_CSctpActiveEstabs_Object((1,3,6,1,4,1,9,10,75,1,1,9),_CSctpActiveEstabs_Type())
cSctpActiveEstabs.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpActiveEstabs.setStatus(_A)
_CSctpPassiveEstabs_Type=Counter64
_CSctpPassiveEstabs_Object=MibScalar
cSctpPassiveEstabs=_CSctpPassiveEstabs_Object((1,3,6,1,4,1,9,10,75,1,1,10),_CSctpPassiveEstabs_Type())
cSctpPassiveEstabs.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpPassiveEstabs.setStatus(_A)
_CSctpAborteds_Type=Counter64
_CSctpAborteds_Object=MibScalar
cSctpAborteds=_CSctpAborteds_Object((1,3,6,1,4,1,9,10,75,1,1,11),_CSctpAborteds_Type())
cSctpAborteds.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAborteds.setStatus(_A)
_CSctpShutdowns_Type=Counter64
_CSctpShutdowns_Object=MibScalar
cSctpShutdowns=_CSctpShutdowns_Object((1,3,6,1,4,1,9,10,75,1,1,12),_CSctpShutdowns_Type())
cSctpShutdowns.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpShutdowns.setStatus(_A)
_CSctpStatOutOfBlues_Type=Counter64
_CSctpStatOutOfBlues_Object=MibScalar
cSctpStatOutOfBlues=_CSctpStatOutOfBlues_Object((1,3,6,1,4,1,9,10,75,1,1,13),_CSctpStatOutOfBlues_Type())
cSctpStatOutOfBlues.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpStatOutOfBlues.setStatus(_A)
_CSctpStatChecksumErrors_Type=Counter64
_CSctpStatChecksumErrors_Object=MibScalar
cSctpStatChecksumErrors=_CSctpStatChecksumErrors_Object((1,3,6,1,4,1,9,10,75,1,1,14),_CSctpStatChecksumErrors_Type())
cSctpStatChecksumErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpStatChecksumErrors.setStatus(_A)
_CSctpStatSentCtrlChunks_Type=Counter64
_CSctpStatSentCtrlChunks_Object=MibScalar
cSctpStatSentCtrlChunks=_CSctpStatSentCtrlChunks_Object((1,3,6,1,4,1,9,10,75,1,1,15),_CSctpStatSentCtrlChunks_Type())
cSctpStatSentCtrlChunks.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpStatSentCtrlChunks.setStatus(_A)
_CSctpStatSentOrderChunks_Type=Counter64
_CSctpStatSentOrderChunks_Object=MibScalar
cSctpStatSentOrderChunks=_CSctpStatSentOrderChunks_Object((1,3,6,1,4,1,9,10,75,1,1,16),_CSctpStatSentOrderChunks_Type())
cSctpStatSentOrderChunks.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpStatSentOrderChunks.setStatus(_A)
_CSctpStatSentUnorderChunks_Type=Counter64
_CSctpStatSentUnorderChunks_Object=MibScalar
cSctpStatSentUnorderChunks=_CSctpStatSentUnorderChunks_Object((1,3,6,1,4,1,9,10,75,1,1,17),_CSctpStatSentUnorderChunks_Type())
cSctpStatSentUnorderChunks.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpStatSentUnorderChunks.setStatus(_A)
_CSctpStatRecCtrlChunks_Type=Counter64
_CSctpStatRecCtrlChunks_Object=MibScalar
cSctpStatRecCtrlChunks=_CSctpStatRecCtrlChunks_Object((1,3,6,1,4,1,9,10,75,1,1,18),_CSctpStatRecCtrlChunks_Type())
cSctpStatRecCtrlChunks.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpStatRecCtrlChunks.setStatus(_A)
_CSctpStatRecOrderChunks_Type=Counter64
_CSctpStatRecOrderChunks_Object=MibScalar
cSctpStatRecOrderChunks=_CSctpStatRecOrderChunks_Object((1,3,6,1,4,1,9,10,75,1,1,19),_CSctpStatRecOrderChunks_Type())
cSctpStatRecOrderChunks.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpStatRecOrderChunks.setStatus(_A)
_CSctpStatRecUnorderChunks_Type=Counter64
_CSctpStatRecUnorderChunks_Object=MibScalar
cSctpStatRecUnorderChunks=_CSctpStatRecUnorderChunks_Object((1,3,6,1,4,1,9,10,75,1,1,20),_CSctpStatRecUnorderChunks_Type())
cSctpStatRecUnorderChunks.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpStatRecUnorderChunks.setStatus(_A)
_CSctpStatFragmentedUsrMessages_Type=Counter64
_CSctpStatFragmentedUsrMessages_Object=MibScalar
cSctpStatFragmentedUsrMessages=_CSctpStatFragmentedUsrMessages_Object((1,3,6,1,4,1,9,10,75,1,1,21),_CSctpStatFragmentedUsrMessages_Type())
cSctpStatFragmentedUsrMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpStatFragmentedUsrMessages.setStatus(_A)
_CSctpStatReassembledUsrMessages_Type=Counter64
_CSctpStatReassembledUsrMessages_Object=MibScalar
cSctpStatReassembledUsrMessages=_CSctpStatReassembledUsrMessages_Object((1,3,6,1,4,1,9,10,75,1,1,22),_CSctpStatReassembledUsrMessages_Type())
cSctpStatReassembledUsrMessages.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpStatReassembledUsrMessages.setStatus(_A)
_CSctpStatSentSCTPPacks_Type=Counter64
_CSctpStatSentSCTPPacks_Object=MibScalar
cSctpStatSentSCTPPacks=_CSctpStatSentSCTPPacks_Object((1,3,6,1,4,1,9,10,75,1,1,23),_CSctpStatSentSCTPPacks_Type())
cSctpStatSentSCTPPacks.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpStatSentSCTPPacks.setStatus(_A)
_CSctpStatRecSCTPPacks_Type=Counter64
_CSctpStatRecSCTPPacks_Object=MibScalar
cSctpStatRecSCTPPacks=_CSctpStatRecSCTPPacks_Object((1,3,6,1,4,1,9,10,75,1,1,24),_CSctpStatRecSCTPPacks_Type())
cSctpStatRecSCTPPacks.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpStatRecSCTPPacks.setStatus(_A)
_CSctpTables_ObjectIdentity=ObjectIdentity
cSctpTables=_CSctpTables_ObjectIdentity((1,3,6,1,4,1,9,10,75,1,2))
_CSctpAssocTable_Object=MibTable
cSctpAssocTable=_CSctpAssocTable_Object((1,3,6,1,4,1,9,10,75,1,2,2))
if mibBuilder.loadTexts:cSctpAssocTable.setStatus(_A)
_CSctpAssocEntry_Object=MibTableRow
cSctpAssocEntry=_CSctpAssocEntry_Object((1,3,6,1,4,1,9,10,75,1,2,2,1))
cSctpAssocEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:cSctpAssocEntry.setStatus(_A)
_CSctpAssocId_Type=Unsigned32
_CSctpAssocId_Object=MibTableColumn
cSctpAssocId=_CSctpAssocId_Object((1,3,6,1,4,1,9,10,75,1,2,2,1,1),_CSctpAssocId_Type())
cSctpAssocId.setMaxAccess(_G)
if mibBuilder.loadTexts:cSctpAssocId.setStatus(_A)
class _CSctpAssocRemHostName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CSctpAssocRemHostName_Type.__name__=_O
_CSctpAssocRemHostName_Object=MibTableColumn
cSctpAssocRemHostName=_CSctpAssocRemHostName_Object((1,3,6,1,4,1,9,10,75,1,2,2,1,2),_CSctpAssocRemHostName_Type())
cSctpAssocRemHostName.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocRemHostName.setStatus(_A)
_CSctpAssocLocalSCTPPort_Type=InetPortNumber
_CSctpAssocLocalSCTPPort_Object=MibTableColumn
cSctpAssocLocalSCTPPort=_CSctpAssocLocalSCTPPort_Object((1,3,6,1,4,1,9,10,75,1,2,2,1,3),_CSctpAssocLocalSCTPPort_Type())
cSctpAssocLocalSCTPPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocLocalSCTPPort.setStatus(_A)
_CSctpAssocRemSCTPPort_Type=InetPortNumber
_CSctpAssocRemSCTPPort_Object=MibTableColumn
cSctpAssocRemSCTPPort=_CSctpAssocRemSCTPPort_Object((1,3,6,1,4,1,9,10,75,1,2,2,1,4),_CSctpAssocRemSCTPPort_Type())
cSctpAssocRemSCTPPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocRemSCTPPort.setStatus(_A)
_CSctpAssocRemPrimaryAddressType_Type=InetAddressType
_CSctpAssocRemPrimaryAddressType_Object=MibTableColumn
cSctpAssocRemPrimaryAddressType=_CSctpAssocRemPrimaryAddressType_Object((1,3,6,1,4,1,9,10,75,1,2,2,1,5),_CSctpAssocRemPrimaryAddressType_Type())
cSctpAssocRemPrimaryAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocRemPrimaryAddressType.setStatus(_A)
_CSctpAssocRemPrimaryAddress_Type=InetAddress
_CSctpAssocRemPrimaryAddress_Object=MibTableColumn
cSctpAssocRemPrimaryAddress=_CSctpAssocRemPrimaryAddress_Object((1,3,6,1,4,1,9,10,75,1,2,2,1,6),_CSctpAssocRemPrimaryAddress_Type())
cSctpAssocRemPrimaryAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocRemPrimaryAddress.setStatus(_A)
_CSctpAssocHeartBeatTimer_Type=Unsigned32
_CSctpAssocHeartBeatTimer_Object=MibTableColumn
cSctpAssocHeartBeatTimer=_CSctpAssocHeartBeatTimer_Object((1,3,6,1,4,1,9,10,75,1,2,2,1,8),_CSctpAssocHeartBeatTimer_Type())
cSctpAssocHeartBeatTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocHeartBeatTimer.setStatus(_A)
if mibBuilder.loadTexts:cSctpAssocHeartBeatTimer.setUnits(_E)
class _CSctpAssocState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('closed',1),('cookieWait',2),('cookieEchoed',3),('established',4),('shutdownPending',5),('shutdownSent',6),('shutdownReceived',7),('shutdownAckSent',8),('deleteTCB',9)))
_CSctpAssocState_Type.__name__=_F
_CSctpAssocState_Object=MibTableColumn
cSctpAssocState=_CSctpAssocState_Object((1,3,6,1,4,1,9,10,75,1,2,2,1,9),_CSctpAssocState_Type())
cSctpAssocState.setMaxAccess('read-write')
if mibBuilder.loadTexts:cSctpAssocState.setStatus(_A)
_CSctpAssocInStreams_Type=Unsigned32
_CSctpAssocInStreams_Object=MibTableColumn
cSctpAssocInStreams=_CSctpAssocInStreams_Object((1,3,6,1,4,1,9,10,75,1,2,2,1,10),_CSctpAssocInStreams_Type())
cSctpAssocInStreams.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocInStreams.setStatus(_A)
_CSctpAssocOutStreams_Type=Unsigned32
_CSctpAssocOutStreams_Object=MibTableColumn
cSctpAssocOutStreams=_CSctpAssocOutStreams_Object((1,3,6,1,4,1,9,10,75,1,2,2,1,11),_CSctpAssocOutStreams_Type())
cSctpAssocOutStreams.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocOutStreams.setStatus(_A)
_CSctpAssocMaxRetr_Type=Unsigned32
_CSctpAssocMaxRetr_Object=MibTableColumn
cSctpAssocMaxRetr=_CSctpAssocMaxRetr_Object((1,3,6,1,4,1,9,10,75,1,2,2,1,12),_CSctpAssocMaxRetr_Type())
cSctpAssocMaxRetr.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocMaxRetr.setStatus(_A)
_CSctpAssocT1expireds_Type=Counter64
_CSctpAssocT1expireds_Object=MibTableColumn
cSctpAssocT1expireds=_CSctpAssocT1expireds_Object((1,3,6,1,4,1,9,10,75,1,2,2,1,13),_CSctpAssocT1expireds_Type())
cSctpAssocT1expireds.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocT1expireds.setStatus(_A)
_CSctpAssocT2expireds_Type=Counter64
_CSctpAssocT2expireds_Object=MibTableColumn
cSctpAssocT2expireds=_CSctpAssocT2expireds_Object((1,3,6,1,4,1,9,10,75,1,2,2,1,14),_CSctpAssocT2expireds_Type())
cSctpAssocT2expireds.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocT2expireds.setStatus(_A)
_CSctpAssocRtxChunks_Type=Counter64
_CSctpAssocRtxChunks_Object=MibTableColumn
cSctpAssocRtxChunks=_CSctpAssocRtxChunks_Object((1,3,6,1,4,1,9,10,75,1,2,2,1,15),_CSctpAssocRtxChunks_Type())
cSctpAssocRtxChunks.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocRtxChunks.setStatus(_A)
_CSctpAssocStartTime_Type=TimeStamp
_CSctpAssocStartTime_Object=MibTableColumn
cSctpAssocStartTime=_CSctpAssocStartTime_Object((1,3,6,1,4,1,9,10,75,1,2,2,1,17),_CSctpAssocStartTime_Type())
cSctpAssocStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocStartTime.setStatus(_A)
_CSctpAssocLocalAddressTable_Object=MibTable
cSctpAssocLocalAddressTable=_CSctpAssocLocalAddressTable_Object((1,3,6,1,4,1,9,10,75,1,2,3))
if mibBuilder.loadTexts:cSctpAssocLocalAddressTable.setStatus(_A)
_CSctpAssocLocalAddressEntry_Object=MibTableRow
cSctpAssocLocalAddressEntry=_CSctpAssocLocalAddressEntry_Object((1,3,6,1,4,1,9,10,75,1,2,3,1))
cSctpAssocLocalAddressEntry.setIndexNames((0,_B,_D),(0,_B,_P),(0,_B,_Q))
if mibBuilder.loadTexts:cSctpAssocLocalAddressEntry.setStatus(_A)
_CSctpAssocLocalAddressIPType_Type=InetAddressType
_CSctpAssocLocalAddressIPType_Object=MibTableColumn
cSctpAssocLocalAddressIPType=_CSctpAssocLocalAddressIPType_Object((1,3,6,1,4,1,9,10,75,1,2,3,1,1),_CSctpAssocLocalAddressIPType_Type())
cSctpAssocLocalAddressIPType.setMaxAccess(_G)
if mibBuilder.loadTexts:cSctpAssocLocalAddressIPType.setStatus(_A)
_CSctpAssocLocalAddressIP_Type=InetAddress
_CSctpAssocLocalAddressIP_Object=MibTableColumn
cSctpAssocLocalAddressIP=_CSctpAssocLocalAddressIP_Object((1,3,6,1,4,1,9,10,75,1,2,3,1,2),_CSctpAssocLocalAddressIP_Type())
cSctpAssocLocalAddressIP.setMaxAccess(_G)
if mibBuilder.loadTexts:cSctpAssocLocalAddressIP.setStatus(_A)
_CSctpAssocLocalAddressStartTime_Type=TimeStamp
_CSctpAssocLocalAddressStartTime_Object=MibTableColumn
cSctpAssocLocalAddressStartTime=_CSctpAssocLocalAddressStartTime_Object((1,3,6,1,4,1,9,10,75,1,2,3,1,3),_CSctpAssocLocalAddressStartTime_Type())
cSctpAssocLocalAddressStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocLocalAddressStartTime.setStatus(_A)
_CSctpAssocRemAddressTable_Object=MibTable
cSctpAssocRemAddressTable=_CSctpAssocRemAddressTable_Object((1,3,6,1,4,1,9,10,75,1,2,4))
if mibBuilder.loadTexts:cSctpAssocRemAddressTable.setStatus(_A)
_CSctpAssocRemAddressEntry_Object=MibTableRow
cSctpAssocRemAddressEntry=_CSctpAssocRemAddressEntry_Object((1,3,6,1,4,1,9,10,75,1,2,4,1))
cSctpAssocRemAddressEntry.setIndexNames((0,_B,_D),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:cSctpAssocRemAddressEntry.setStatus(_A)
_CSctpAssocRemAddressIPType_Type=InetAddressType
_CSctpAssocRemAddressIPType_Object=MibTableColumn
cSctpAssocRemAddressIPType=_CSctpAssocRemAddressIPType_Object((1,3,6,1,4,1,9,10,75,1,2,4,1,1),_CSctpAssocRemAddressIPType_Type())
cSctpAssocRemAddressIPType.setMaxAccess(_G)
if mibBuilder.loadTexts:cSctpAssocRemAddressIPType.setStatus(_A)
_CSctpAssocRemAddressIP_Type=InetAddress
_CSctpAssocRemAddressIP_Object=MibTableColumn
cSctpAssocRemAddressIP=_CSctpAssocRemAddressIP_Object((1,3,6,1,4,1,9,10,75,1,2,4,1,2),_CSctpAssocRemAddressIP_Type())
cSctpAssocRemAddressIP.setMaxAccess(_G)
if mibBuilder.loadTexts:cSctpAssocRemAddressIP.setStatus(_A)
class _CSctpAssocRemAddressStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_R,0),(_S,1)))
_CSctpAssocRemAddressStatus_Type.__name__=_F
_CSctpAssocRemAddressStatus_Object=MibTableColumn
cSctpAssocRemAddressStatus=_CSctpAssocRemAddressStatus_Object((1,3,6,1,4,1,9,10,75,1,2,4,1,3),_CSctpAssocRemAddressStatus_Type())
cSctpAssocRemAddressStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocRemAddressStatus.setStatus(_A)
class _CSctpAssocRemAddressHBFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_R,0),(_S,1)))
_CSctpAssocRemAddressHBFlag_Type.__name__=_F
_CSctpAssocRemAddressHBFlag_Object=MibTableColumn
cSctpAssocRemAddressHBFlag=_CSctpAssocRemAddressHBFlag_Object((1,3,6,1,4,1,9,10,75,1,2,4,1,4),_CSctpAssocRemAddressHBFlag_Type())
cSctpAssocRemAddressHBFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocRemAddressHBFlag.setStatus(_A)
_CSctpAssocRemAddressRTO_Type=Unsigned32
_CSctpAssocRemAddressRTO_Object=MibTableColumn
cSctpAssocRemAddressRTO=_CSctpAssocRemAddressRTO_Object((1,3,6,1,4,1,9,10,75,1,2,4,1,5),_CSctpAssocRemAddressRTO_Type())
cSctpAssocRemAddressRTO.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocRemAddressRTO.setStatus(_A)
if mibBuilder.loadTexts:cSctpAssocRemAddressRTO.setUnits(_E)
_CSctpAssocRemAddressMaxPathRtx_Type=Unsigned32
_CSctpAssocRemAddressMaxPathRtx_Object=MibTableColumn
cSctpAssocRemAddressMaxPathRtx=_CSctpAssocRemAddressMaxPathRtx_Object((1,3,6,1,4,1,9,10,75,1,2,4,1,6),_CSctpAssocRemAddressMaxPathRtx_Type())
cSctpAssocRemAddressMaxPathRtx.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocRemAddressMaxPathRtx.setStatus(_A)
_CSctpAssocRemAddressRtx_Type=Counter64
_CSctpAssocRemAddressRtx_Object=MibTableColumn
cSctpAssocRemAddressRtx=_CSctpAssocRemAddressRtx_Object((1,3,6,1,4,1,9,10,75,1,2,4,1,7),_CSctpAssocRemAddressRtx_Type())
cSctpAssocRemAddressRtx.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocRemAddressRtx.setStatus(_A)
_CSctpAssocRemAddressStartTime_Type=TimeStamp
_CSctpAssocRemAddressStartTime_Object=MibTableColumn
cSctpAssocRemAddressStartTime=_CSctpAssocRemAddressStartTime_Object((1,3,6,1,4,1,9,10,75,1,2,4,1,8),_CSctpAssocRemAddressStartTime_Type())
cSctpAssocRemAddressStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpAssocRemAddressStartTime.setStatus(_A)
_CSctpLookupLocalPortTable_Object=MibTable
cSctpLookupLocalPortTable=_CSctpLookupLocalPortTable_Object((1,3,6,1,4,1,9,10,75,1,2,5))
if mibBuilder.loadTexts:cSctpLookupLocalPortTable.setStatus(_A)
_CSctpLookupLocalPortEntry_Object=MibTableRow
cSctpLookupLocalPortEntry=_CSctpLookupLocalPortEntry_Object((1,3,6,1,4,1,9,10,75,1,2,5,1))
cSctpLookupLocalPortEntry.setIndexNames((0,_B,_J),(0,_B,_D))
if mibBuilder.loadTexts:cSctpLookupLocalPortEntry.setStatus(_A)
_CSctpLookupLocalPortStartTime_Type=TimeStamp
_CSctpLookupLocalPortStartTime_Object=MibTableColumn
cSctpLookupLocalPortStartTime=_CSctpLookupLocalPortStartTime_Object((1,3,6,1,4,1,9,10,75,1,2,5,1,1),_CSctpLookupLocalPortStartTime_Type())
cSctpLookupLocalPortStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpLookupLocalPortStartTime.setStatus(_A)
_CSctpLookupRemPortTable_Object=MibTable
cSctpLookupRemPortTable=_CSctpLookupRemPortTable_Object((1,3,6,1,4,1,9,10,75,1,2,6))
if mibBuilder.loadTexts:cSctpLookupRemPortTable.setStatus(_A)
_CSctpLookupRemPortEntry_Object=MibTableRow
cSctpLookupRemPortEntry=_CSctpLookupRemPortEntry_Object((1,3,6,1,4,1,9,10,75,1,2,6,1))
cSctpLookupRemPortEntry.setIndexNames((0,_B,_K),(0,_B,_D))
if mibBuilder.loadTexts:cSctpLookupRemPortEntry.setStatus(_A)
_CSctpLookupRemPortStartTime_Type=TimeStamp
_CSctpLookupRemPortStartTime_Object=MibTableColumn
cSctpLookupRemPortStartTime=_CSctpLookupRemPortStartTime_Object((1,3,6,1,4,1,9,10,75,1,2,6,1,1),_CSctpLookupRemPortStartTime_Type())
cSctpLookupRemPortStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpLookupRemPortStartTime.setStatus(_A)
_CSctpLookupRemHostNameTable_Object=MibTable
cSctpLookupRemHostNameTable=_CSctpLookupRemHostNameTable_Object((1,3,6,1,4,1,9,10,75,1,2,7))
if mibBuilder.loadTexts:cSctpLookupRemHostNameTable.setStatus(_A)
_CSctpLookupRemHostNameEntry_Object=MibTableRow
cSctpLookupRemHostNameEntry=_CSctpLookupRemHostNameEntry_Object((1,3,6,1,4,1,9,10,75,1,2,7,1))
cSctpLookupRemHostNameEntry.setIndexNames((0,_B,_L),(0,_B,_D))
if mibBuilder.loadTexts:cSctpLookupRemHostNameEntry.setStatus(_A)
_CSctpLookupRemHostNameStartTime_Type=TimeStamp
_CSctpLookupRemHostNameStartTime_Object=MibTableColumn
cSctpLookupRemHostNameStartTime=_CSctpLookupRemHostNameStartTime_Object((1,3,6,1,4,1,9,10,75,1,2,7,1,1),_CSctpLookupRemHostNameStartTime_Type())
cSctpLookupRemHostNameStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpLookupRemHostNameStartTime.setStatus(_A)
_CSctpLookupRemPrimIPAddrTable_Object=MibTable
cSctpLookupRemPrimIPAddrTable=_CSctpLookupRemPrimIPAddrTable_Object((1,3,6,1,4,1,9,10,75,1,2,8))
if mibBuilder.loadTexts:cSctpLookupRemPrimIPAddrTable.setStatus(_A)
_CSctpLookupRemPrimIPAddrEntry_Object=MibTableRow
cSctpLookupRemPrimIPAddrEntry=_CSctpLookupRemPrimIPAddrEntry_Object((1,3,6,1,4,1,9,10,75,1,2,8,1))
cSctpLookupRemPrimIPAddrEntry.setIndexNames((0,_B,_M),(0,_B,_N),(0,_B,_D))
if mibBuilder.loadTexts:cSctpLookupRemPrimIPAddrEntry.setStatus(_A)
_CSctpLookupRemPrimIPAddrStartTime_Type=TimeStamp
_CSctpLookupRemPrimIPAddrStartTime_Object=MibTableColumn
cSctpLookupRemPrimIPAddrStartTime=_CSctpLookupRemPrimIPAddrStartTime_Object((1,3,6,1,4,1,9,10,75,1,2,8,1,1),_CSctpLookupRemPrimIPAddrStartTime_Type())
cSctpLookupRemPrimIPAddrStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpLookupRemPrimIPAddrStartTime.setStatus(_A)
_CSctpLookupRemIPAddrTable_Object=MibTable
cSctpLookupRemIPAddrTable=_CSctpLookupRemIPAddrTable_Object((1,3,6,1,4,1,9,10,75,1,2,9))
if mibBuilder.loadTexts:cSctpLookupRemIPAddrTable.setStatus(_A)
_CSctpLookupRemIPAddrEntry_Object=MibTableRow
cSctpLookupRemIPAddrEntry=_CSctpLookupRemIPAddrEntry_Object((1,3,6,1,4,1,9,10,75,1,2,9,1))
cSctpLookupRemIPAddrEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_D))
if mibBuilder.loadTexts:cSctpLookupRemIPAddrEntry.setStatus(_A)
_CSctpLookupRemIPAddrStartTime_Type=TimeStamp
_CSctpLookupRemIPAddrStartTime_Object=MibTableColumn
cSctpLookupRemIPAddrStartTime=_CSctpLookupRemIPAddrStartTime_Object((1,3,6,1,4,1,9,10,75,1,2,9,1,1),_CSctpLookupRemIPAddrStartTime_Type())
cSctpLookupRemIPAddrStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cSctpLookupRemIPAddrStartTime.setStatus(_A)
_CSctpConformance_ObjectIdentity=ObjectIdentity
cSctpConformance=_CSctpConformance_ObjectIdentity((1,3,6,1,4,1,9,10,75,2))
_CSctpGroups_ObjectIdentity=ObjectIdentity
cSctpGroups=_CSctpGroups_ObjectIdentity((1,3,6,1,4,1,9,10,75,2,1))
_CSctpCompliances_ObjectIdentity=ObjectIdentity
cSctpCompliances=_CSctpCompliances_ObjectIdentity((1,3,6,1,4,1,9,10,75,2,2))
cSctpGeneralVariablesGroup=ObjectGroup((1,3,6,1,4,1,9,10,75,2,1,1))
cSctpGeneralVariablesGroup.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:cSctpGeneralVariablesGroup.setStatus(_A)
cSctpStateStatGroup=ObjectGroup((1,3,6,1,4,1,9,10,75,2,1,2))
cSctpStateStatGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:cSctpStateStatGroup.setStatus(_A)
cSctpOtherStatGroup=ObjectGroup((1,3,6,1,4,1,9,10,75,2,1,3))
cSctpOtherStatGroup.setObjects(*((_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:cSctpOtherStatGroup.setStatus(_A)
cSctpAssocTablesVariablesGroup=ObjectGroup((1,3,6,1,4,1,9,10,75,2,1,4))
cSctpAssocTablesVariablesGroup.setObjects(*((_B,_L),(_B,_J),(_B,_K),(_B,_M),(_B,_N),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5)))
if mibBuilder.loadTexts:cSctpAssocTablesVariablesGroup.setStatus(_A)
cSctpAssocStatGroup=ObjectGroup((1,3,6,1,4,1,9,10,75,2,1,5))
cSctpAssocStatGroup.setObjects((_B,_A6))
if mibBuilder.loadTexts:cSctpAssocStatGroup.setStatus(_A)
cSctpInverseGroup=ObjectGroup((1,3,6,1,4,1,9,10,75,2,1,6))
cSctpInverseGroup.setObjects(*((_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB)))
if mibBuilder.loadTexts:cSctpInverseGroup.setStatus(_A)
cSctpCompliance=ModuleCompliance((1,3,6,1,4,1,9,10,75,2,2,1))
cSctpCompliance.setObjects(*((_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH)))
if mibBuilder.loadTexts:cSctpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'InetPortNumber':InetPortNumber,'cSctpMIB':cSctpMIB,'cSctpObjects':cSctpObjects,'cSctpScalars':cSctpScalars,_T:cSctpRtoAlgorithm,_U:cSctpRtoMin,_V:cSctpRtoMax,_W:cSctpRtoInitial,_X:cSctpMaxAssoc,_Y:cSctpValCookieLife,_Z:cSctpMaxInitRetr,_a:cSctpCurrEstab,_b:cSctpActiveEstabs,_c:cSctpPassiveEstabs,_d:cSctpAborteds,_e:cSctpShutdowns,_f:cSctpStatOutOfBlues,_g:cSctpStatChecksumErrors,_h:cSctpStatSentCtrlChunks,_i:cSctpStatSentOrderChunks,_j:cSctpStatSentUnorderChunks,_k:cSctpStatRecCtrlChunks,_l:cSctpStatRecOrderChunks,_m:cSctpStatRecUnorderChunks,_n:cSctpStatFragmentedUsrMessages,_o:cSctpStatReassembledUsrMessages,_p:cSctpStatSentSCTPPacks,_q:cSctpStatRecSCTPPacks,'cSctpTables':cSctpTables,'cSctpAssocTable':cSctpAssocTable,'cSctpAssocEntry':cSctpAssocEntry,_D:cSctpAssocId,_L:cSctpAssocRemHostName,_J:cSctpAssocLocalSCTPPort,_K:cSctpAssocRemSCTPPort,_M:cSctpAssocRemPrimaryAddressType,_N:cSctpAssocRemPrimaryAddress,_r:cSctpAssocHeartBeatTimer,_s:cSctpAssocState,_t:cSctpAssocInStreams,_u:cSctpAssocOutStreams,_v:cSctpAssocMaxRetr,_w:cSctpAssocT1expireds,_x:cSctpAssocT2expireds,_y:cSctpAssocRtxChunks,_z:cSctpAssocStartTime,'cSctpAssocLocalAddressTable':cSctpAssocLocalAddressTable,'cSctpAssocLocalAddressEntry':cSctpAssocLocalAddressEntry,_P:cSctpAssocLocalAddressIPType,_Q:cSctpAssocLocalAddressIP,_A0:cSctpAssocLocalAddressStartTime,'cSctpAssocRemAddressTable':cSctpAssocRemAddressTable,'cSctpAssocRemAddressEntry':cSctpAssocRemAddressEntry,_H:cSctpAssocRemAddressIPType,_I:cSctpAssocRemAddressIP,_A1:cSctpAssocRemAddressStatus,_A2:cSctpAssocRemAddressHBFlag,_A3:cSctpAssocRemAddressRTO,_A4:cSctpAssocRemAddressMaxPathRtx,_A6:cSctpAssocRemAddressRtx,_A5:cSctpAssocRemAddressStartTime,'cSctpLookupLocalPortTable':cSctpLookupLocalPortTable,'cSctpLookupLocalPortEntry':cSctpLookupLocalPortEntry,_A7:cSctpLookupLocalPortStartTime,'cSctpLookupRemPortTable':cSctpLookupRemPortTable,'cSctpLookupRemPortEntry':cSctpLookupRemPortEntry,_A8:cSctpLookupRemPortStartTime,'cSctpLookupRemHostNameTable':cSctpLookupRemHostNameTable,'cSctpLookupRemHostNameEntry':cSctpLookupRemHostNameEntry,_A9:cSctpLookupRemHostNameStartTime,'cSctpLookupRemPrimIPAddrTable':cSctpLookupRemPrimIPAddrTable,'cSctpLookupRemPrimIPAddrEntry':cSctpLookupRemPrimIPAddrEntry,_AA:cSctpLookupRemPrimIPAddrStartTime,'cSctpLookupRemIPAddrTable':cSctpLookupRemIPAddrTable,'cSctpLookupRemIPAddrEntry':cSctpLookupRemIPAddrEntry,_AB:cSctpLookupRemIPAddrStartTime,'cSctpConformance':cSctpConformance,'cSctpGroups':cSctpGroups,_AC:cSctpGeneralVariablesGroup,_AE:cSctpStateStatGroup,_AF:cSctpOtherStatGroup,_AD:cSctpAssocTablesVariablesGroup,_AG:cSctpAssocStatGroup,_AH:cSctpInverseGroup,'cSctpCompliances':cSctpCompliances,'cSctpCompliance':cSctpCompliance})