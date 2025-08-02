_An='docsBpiCmtsGroup'
_Am='docsBpiCmGroup'
_Al='docsBpiCmtsDefaultTEKGraceTime'
_Ak='docsBpiCmtsDefaultAuthGraceTime'
_Aj='docsBpiMulticastAuthControl'
_Ai='docsBpiIpMulticastMapControl'
_Ah='docsBpiIpMulticastServiceId'
_Ag='docsBpiCmtsTEKInvalidErrorString'
_Af='docsBpiCmtsTEKInvalidErrorCode'
_Ae='docsBpiCmtsKeyRejectErrorString'
_Ad='docsBpiCmtsKeyRejectErrorCode'
_Ac='docsBpiCmtsTEKInvalids'
_Ab='docsBpiCmtsKeyRejects'
_Aa='docsBpiCmtsKeyReplies'
_AZ='docsBpiCmtsKeyRequests'
_AY='docsBpiCmtsTEKReset'
_AX='docsBpiCmtsTEKExpiresNew'
_AW='docsBpiCmtsTEKExpiresOld'
_AV='docsBpiCmtsTEKGraceTime'
_AU='docsBpiCmtsTEKLifetime'
_AT='docsBpiCmtsAuthInvalidErrorString'
_AS='docsBpiCmtsAuthInvalidErrorCode'
_AR='docsBpiCmtsAuthRejectErrorString'
_AQ='docsBpiCmtsAuthRejectErrorCode'
_AP='docsBpiCmtsAuthCmInvalids'
_AO='docsBpiCmtsAuthCmRejects'
_AN='docsBpiCmtsAuthCmReplies'
_AM='docsBpiCmtsAuthCmRequests'
_AL='docsBpiCmtsAuthCmReset'
_AK='docsBpiCmtsAuthCmGraceTime'
_AJ='docsBpiCmtsAuthCmLifetime'
_AI='docsBpiCmtsAuthCmExpires'
_AH='docsBpiCmtsAuthCmKeySequenceNumber'
_AG='docsBpiCmtsAuthCmPublicKey'
_AF='docsBpiCmtsAuthInvalids'
_AE='docsBpiCmtsAuthRejects'
_AD='docsBpiCmtsAuthReplies'
_AC='docsBpiCmtsAuthRequests'
_AB='docsBpiCmtsDefaultTEKLifetime'
_AA='docsBpiCmtsDefaultAuthLifetime'
_A9='docsBpiCmTEKInvalidErrorString'
_A8='docsBpiCmTEKInvalidErrorCode'
_A7='docsBpiCmTEKKeyRejectErrorString'
_A6='docsBpiCmTEKKeyRejectErrorCode'
_A5='docsBpiCmTEKAuthPends'
_A4='docsBpiCmTEKInvalids'
_A3='docsBpiCmTEKKeyRejects'
_A2='docsBpiCmTEKKeyReplies'
_A1='docsBpiCmTEKKeyRequests'
_A0='docsBpiCmTEKExpiresNew'
_z='docsBpiCmTEKExpiresOld'
_y='docsBpiCmTEKState'
_x='docsBpiCmTEKPrivacyEnable'
_w='docsBpiCmAuthInvalidErrorString'
_v='docsBpiCmAuthInvalidErrorCode'
_u='docsBpiCmAuthRejectErrorString'
_t='docsBpiCmAuthRejectErrorCode'
_s='docsBpiCmAuthInvalids'
_r='docsBpiCmAuthRejects'
_q='docsBpiCmAuthReplies'
_p='docsBpiCmAuthRequests'
_o='docsBpiCmAuthRejectWaitTimeout'
_n='docsBpiCmRekeyWaitTimeout'
_m='docsBpiCmOpWaitTimeout'
_l='docsBpiCmReauthWaitTimeout'
_k='docsBpiCmAuthWaitTimeout'
_j='docsBpiCmTEKGraceTime'
_i='docsBpiCmAuthGraceTime'
_h='docsBpiCmAuthReset'
_g='docsBpiCmAuthExpires'
_f='docsBpiCmAuthKeySequenceNumber'
_e='docsBpiCmAuthState'
_d='docsBpiCmPublicKey'
_c='docsBpiCmPrivacyEnable'
_b='docsBpiMulticastCmMacAddress'
_a='docsBpiMulticastServiceId'
_Z='docsBpiIpMulticastPrefixLength'
_Y='docsBpiIpMulticastAddress'
_X='docsBpiCmtsAuthCmMacAddress'
_W='keyRequestAuthenticationFailure'
_V='unsolicited'
_U='docsIfCmtsServiceId'
_T='docsIfCmServiceId'
_S='read-create'
_R='obsolete'
_Q='DOCS-IF-MIB'
_P='OctetString'
_O='invalidKeySequence'
_N='unauthorizedSid'
_M='unauthorizedCm'
_L='not-accessible'
_K='unknown'
_J='none'
_I='ifIndex'
_H='IF-MIB'
_G='read-write'
_F='DisplayString'
_E='seconds'
_D='Integer32'
_C='read-only'
_B='DOCS-BPI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_P,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
docsIfCmServiceId,docsIfCmtsServiceId,docsIfMib=mibBuilder.importSymbols(_Q,_T,_U,'docsIfMib')
ifIndex,=mibBuilder.importSymbols(_H,_I)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
docsBpiMIB=ModuleIdentity((1,3,6,1,2,1,10,127,5))
if mibBuilder.loadTexts:docsBpiMIB.setRevisions(('2001-03-13 00:00','2000-11-03 19:30','2000-02-16 19:30'))
_DocsBpiMIBObjects_ObjectIdentity=ObjectIdentity
docsBpiMIBObjects=_DocsBpiMIBObjects_ObjectIdentity((1,3,6,1,2,1,10,127,5,1))
_DocsBpiCmObjects_ObjectIdentity=ObjectIdentity
docsBpiCmObjects=_DocsBpiCmObjects_ObjectIdentity((1,3,6,1,2,1,10,127,5,1,1))
_DocsBpiCmBaseTable_Object=MibTable
docsBpiCmBaseTable=_DocsBpiCmBaseTable_Object((1,3,6,1,2,1,10,127,5,1,1,1))
if mibBuilder.loadTexts:docsBpiCmBaseTable.setStatus(_A)
_DocsBpiCmBaseEntry_Object=MibTableRow
docsBpiCmBaseEntry=_DocsBpiCmBaseEntry_Object((1,3,6,1,2,1,10,127,5,1,1,1,1))
docsBpiCmBaseEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:docsBpiCmBaseEntry.setStatus(_A)
_DocsBpiCmPrivacyEnable_Type=TruthValue
_DocsBpiCmPrivacyEnable_Object=MibTableColumn
docsBpiCmPrivacyEnable=_DocsBpiCmPrivacyEnable_Object((1,3,6,1,2,1,10,127,5,1,1,1,1,1),_DocsBpiCmPrivacyEnable_Type())
docsBpiCmPrivacyEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmPrivacyEnable.setStatus(_A)
class _DocsBpiCmPublicKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(74,74),ValueSizeConstraint(106,106),ValueSizeConstraint(140,140),ValueSizeConstraint(270,270))
_DocsBpiCmPublicKey_Type.__name__=_P
_DocsBpiCmPublicKey_Object=MibTableColumn
docsBpiCmPublicKey=_DocsBpiCmPublicKey_Object((1,3,6,1,2,1,10,127,5,1,1,1,1,2),_DocsBpiCmPublicKey_Type())
docsBpiCmPublicKey.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmPublicKey.setStatus(_A)
class _DocsBpiCmAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('start',1),('authWait',2),('authorized',3),('reauthWait',4),('authRejectWait',5)))
_DocsBpiCmAuthState_Type.__name__=_D
_DocsBpiCmAuthState_Object=MibTableColumn
docsBpiCmAuthState=_DocsBpiCmAuthState_Object((1,3,6,1,2,1,10,127,5,1,1,1,1,3),_DocsBpiCmAuthState_Type())
docsBpiCmAuthState.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmAuthState.setStatus(_A)
class _DocsBpiCmAuthKeySequenceNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_DocsBpiCmAuthKeySequenceNumber_Type.__name__=_D
_DocsBpiCmAuthKeySequenceNumber_Object=MibTableColumn
docsBpiCmAuthKeySequenceNumber=_DocsBpiCmAuthKeySequenceNumber_Object((1,3,6,1,2,1,10,127,5,1,1,1,1,4),_DocsBpiCmAuthKeySequenceNumber_Type())
docsBpiCmAuthKeySequenceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmAuthKeySequenceNumber.setStatus(_A)
_DocsBpiCmAuthExpires_Type=DateAndTime
_DocsBpiCmAuthExpires_Object=MibTableColumn
docsBpiCmAuthExpires=_DocsBpiCmAuthExpires_Object((1,3,6,1,2,1,10,127,5,1,1,1,1,5),_DocsBpiCmAuthExpires_Type())
docsBpiCmAuthExpires.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmAuthExpires.setStatus(_A)
_DocsBpiCmAuthReset_Type=TruthValue
_DocsBpiCmAuthReset_Object=MibTableColumn
docsBpiCmAuthReset=_DocsBpiCmAuthReset_Object((1,3,6,1,2,1,10,127,5,1,1,1,1,6),_DocsBpiCmAuthReset_Type())
docsBpiCmAuthReset.setMaxAccess(_G)
if mibBuilder.loadTexts:docsBpiCmAuthReset.setStatus(_A)
class _DocsBpiCmAuthGraceTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1800))
_DocsBpiCmAuthGraceTime_Type.__name__=_D
_DocsBpiCmAuthGraceTime_Object=MibTableColumn
docsBpiCmAuthGraceTime=_DocsBpiCmAuthGraceTime_Object((1,3,6,1,2,1,10,127,5,1,1,1,1,7),_DocsBpiCmAuthGraceTime_Type())
docsBpiCmAuthGraceTime.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmAuthGraceTime.setStatus(_A)
if mibBuilder.loadTexts:docsBpiCmAuthGraceTime.setUnits(_E)
class _DocsBpiCmTEKGraceTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1800))
_DocsBpiCmTEKGraceTime_Type.__name__=_D
_DocsBpiCmTEKGraceTime_Object=MibTableColumn
docsBpiCmTEKGraceTime=_DocsBpiCmTEKGraceTime_Object((1,3,6,1,2,1,10,127,5,1,1,1,1,8),_DocsBpiCmTEKGraceTime_Type())
docsBpiCmTEKGraceTime.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmTEKGraceTime.setStatus(_A)
if mibBuilder.loadTexts:docsBpiCmTEKGraceTime.setUnits(_E)
class _DocsBpiCmAuthWaitTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_DocsBpiCmAuthWaitTimeout_Type.__name__=_D
_DocsBpiCmAuthWaitTimeout_Object=MibTableColumn
docsBpiCmAuthWaitTimeout=_DocsBpiCmAuthWaitTimeout_Object((1,3,6,1,2,1,10,127,5,1,1,1,1,9),_DocsBpiCmAuthWaitTimeout_Type())
docsBpiCmAuthWaitTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmAuthWaitTimeout.setStatus(_A)
if mibBuilder.loadTexts:docsBpiCmAuthWaitTimeout.setUnits(_E)
class _DocsBpiCmReauthWaitTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_DocsBpiCmReauthWaitTimeout_Type.__name__=_D
_DocsBpiCmReauthWaitTimeout_Object=MibTableColumn
docsBpiCmReauthWaitTimeout=_DocsBpiCmReauthWaitTimeout_Object((1,3,6,1,2,1,10,127,5,1,1,1,1,10),_DocsBpiCmReauthWaitTimeout_Type())
docsBpiCmReauthWaitTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmReauthWaitTimeout.setStatus(_A)
if mibBuilder.loadTexts:docsBpiCmReauthWaitTimeout.setUnits(_E)
class _DocsBpiCmOpWaitTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_DocsBpiCmOpWaitTimeout_Type.__name__=_D
_DocsBpiCmOpWaitTimeout_Object=MibTableColumn
docsBpiCmOpWaitTimeout=_DocsBpiCmOpWaitTimeout_Object((1,3,6,1,2,1,10,127,5,1,1,1,1,11),_DocsBpiCmOpWaitTimeout_Type())
docsBpiCmOpWaitTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmOpWaitTimeout.setStatus(_A)
if mibBuilder.loadTexts:docsBpiCmOpWaitTimeout.setUnits(_E)
class _DocsBpiCmRekeyWaitTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_DocsBpiCmRekeyWaitTimeout_Type.__name__=_D
_DocsBpiCmRekeyWaitTimeout_Object=MibTableColumn
docsBpiCmRekeyWaitTimeout=_DocsBpiCmRekeyWaitTimeout_Object((1,3,6,1,2,1,10,127,5,1,1,1,1,12),_DocsBpiCmRekeyWaitTimeout_Type())
docsBpiCmRekeyWaitTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmRekeyWaitTimeout.setStatus(_A)
if mibBuilder.loadTexts:docsBpiCmRekeyWaitTimeout.setUnits(_E)
class _DocsBpiCmAuthRejectWaitTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,600))
_DocsBpiCmAuthRejectWaitTimeout_Type.__name__=_D
_DocsBpiCmAuthRejectWaitTimeout_Object=MibTableColumn
docsBpiCmAuthRejectWaitTimeout=_DocsBpiCmAuthRejectWaitTimeout_Object((1,3,6,1,2,1,10,127,5,1,1,1,1,13),_DocsBpiCmAuthRejectWaitTimeout_Type())
docsBpiCmAuthRejectWaitTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmAuthRejectWaitTimeout.setStatus(_A)
if mibBuilder.loadTexts:docsBpiCmAuthRejectWaitTimeout.setUnits(_E)
_DocsBpiCmAuthRequests_Type=Counter32
_DocsBpiCmAuthRequests_Object=MibTableColumn
docsBpiCmAuthRequests=_DocsBpiCmAuthRequests_Object((1,3,6,1,2,1,10,127,5,1,1,1,1,14),_DocsBpiCmAuthRequests_Type())
docsBpiCmAuthRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmAuthRequests.setStatus(_A)
_DocsBpiCmAuthReplies_Type=Counter32
_DocsBpiCmAuthReplies_Object=MibTableColumn
docsBpiCmAuthReplies=_DocsBpiCmAuthReplies_Object((1,3,6,1,2,1,10,127,5,1,1,1,1,15),_DocsBpiCmAuthReplies_Type())
docsBpiCmAuthReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmAuthReplies.setStatus(_A)
_DocsBpiCmAuthRejects_Type=Counter32
_DocsBpiCmAuthRejects_Object=MibTableColumn
docsBpiCmAuthRejects=_DocsBpiCmAuthRejects_Object((1,3,6,1,2,1,10,127,5,1,1,1,1,16),_DocsBpiCmAuthRejects_Type())
docsBpiCmAuthRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmAuthRejects.setStatus(_A)
_DocsBpiCmAuthInvalids_Type=Counter32
_DocsBpiCmAuthInvalids_Object=MibTableColumn
docsBpiCmAuthInvalids=_DocsBpiCmAuthInvalids_Object((1,3,6,1,2,1,10,127,5,1,1,1,1,17),_DocsBpiCmAuthInvalids_Type())
docsBpiCmAuthInvalids.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmAuthInvalids.setStatus(_A)
class _DocsBpiCmAuthRejectErrorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_M,3),(_N,4)))
_DocsBpiCmAuthRejectErrorCode_Type.__name__=_D
_DocsBpiCmAuthRejectErrorCode_Object=MibTableColumn
docsBpiCmAuthRejectErrorCode=_DocsBpiCmAuthRejectErrorCode_Object((1,3,6,1,2,1,10,127,5,1,1,1,1,18),_DocsBpiCmAuthRejectErrorCode_Type())
docsBpiCmAuthRejectErrorCode.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmAuthRejectErrorCode.setStatus(_A)
class _DocsBpiCmAuthRejectErrorString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_DocsBpiCmAuthRejectErrorString_Type.__name__=_F
_DocsBpiCmAuthRejectErrorString_Object=MibTableColumn
docsBpiCmAuthRejectErrorString=_DocsBpiCmAuthRejectErrorString_Object((1,3,6,1,2,1,10,127,5,1,1,1,1,19),_DocsBpiCmAuthRejectErrorString_Type())
docsBpiCmAuthRejectErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmAuthRejectErrorString.setStatus(_A)
class _DocsBpiCmAuthInvalidErrorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5,6,7)));namedValues=NamedValues(*((_J,1),(_K,2),(_M,3),(_V,5),(_O,6),(_W,7)))
_DocsBpiCmAuthInvalidErrorCode_Type.__name__=_D
_DocsBpiCmAuthInvalidErrorCode_Object=MibTableColumn
docsBpiCmAuthInvalidErrorCode=_DocsBpiCmAuthInvalidErrorCode_Object((1,3,6,1,2,1,10,127,5,1,1,1,1,20),_DocsBpiCmAuthInvalidErrorCode_Type())
docsBpiCmAuthInvalidErrorCode.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmAuthInvalidErrorCode.setStatus(_A)
class _DocsBpiCmAuthInvalidErrorString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_DocsBpiCmAuthInvalidErrorString_Type.__name__=_F
_DocsBpiCmAuthInvalidErrorString_Object=MibTableColumn
docsBpiCmAuthInvalidErrorString=_DocsBpiCmAuthInvalidErrorString_Object((1,3,6,1,2,1,10,127,5,1,1,1,1,21),_DocsBpiCmAuthInvalidErrorString_Type())
docsBpiCmAuthInvalidErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmAuthInvalidErrorString.setStatus(_A)
_DocsBpiCmTEKTable_Object=MibTable
docsBpiCmTEKTable=_DocsBpiCmTEKTable_Object((1,3,6,1,2,1,10,127,5,1,1,2))
if mibBuilder.loadTexts:docsBpiCmTEKTable.setStatus(_A)
_DocsBpiCmTEKEntry_Object=MibTableRow
docsBpiCmTEKEntry=_DocsBpiCmTEKEntry_Object((1,3,6,1,2,1,10,127,5,1,1,2,1))
docsBpiCmTEKEntry.setIndexNames((0,_H,_I),(0,_Q,_T))
if mibBuilder.loadTexts:docsBpiCmTEKEntry.setStatus(_A)
_DocsBpiCmTEKPrivacyEnable_Type=TruthValue
_DocsBpiCmTEKPrivacyEnable_Object=MibTableColumn
docsBpiCmTEKPrivacyEnable=_DocsBpiCmTEKPrivacyEnable_Object((1,3,6,1,2,1,10,127,5,1,1,2,1,1),_DocsBpiCmTEKPrivacyEnable_Type())
docsBpiCmTEKPrivacyEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmTEKPrivacyEnable.setStatus(_A)
class _DocsBpiCmTEKState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('start',1),('opWait',2),('opReauthWait',3),('operational',4),('rekeyWait',5),('rekeyReauthWait',6)))
_DocsBpiCmTEKState_Type.__name__=_D
_DocsBpiCmTEKState_Object=MibTableColumn
docsBpiCmTEKState=_DocsBpiCmTEKState_Object((1,3,6,1,2,1,10,127,5,1,1,2,1,2),_DocsBpiCmTEKState_Type())
docsBpiCmTEKState.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmTEKState.setStatus(_A)
_DocsBpiCmTEKExpiresOld_Type=DateAndTime
_DocsBpiCmTEKExpiresOld_Object=MibTableColumn
docsBpiCmTEKExpiresOld=_DocsBpiCmTEKExpiresOld_Object((1,3,6,1,2,1,10,127,5,1,1,2,1,3),_DocsBpiCmTEKExpiresOld_Type())
docsBpiCmTEKExpiresOld.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmTEKExpiresOld.setStatus(_A)
_DocsBpiCmTEKExpiresNew_Type=DateAndTime
_DocsBpiCmTEKExpiresNew_Object=MibTableColumn
docsBpiCmTEKExpiresNew=_DocsBpiCmTEKExpiresNew_Object((1,3,6,1,2,1,10,127,5,1,1,2,1,4),_DocsBpiCmTEKExpiresNew_Type())
docsBpiCmTEKExpiresNew.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmTEKExpiresNew.setStatus(_A)
_DocsBpiCmTEKKeyRequests_Type=Counter32
_DocsBpiCmTEKKeyRequests_Object=MibTableColumn
docsBpiCmTEKKeyRequests=_DocsBpiCmTEKKeyRequests_Object((1,3,6,1,2,1,10,127,5,1,1,2,1,5),_DocsBpiCmTEKKeyRequests_Type())
docsBpiCmTEKKeyRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmTEKKeyRequests.setStatus(_A)
_DocsBpiCmTEKKeyReplies_Type=Counter32
_DocsBpiCmTEKKeyReplies_Object=MibTableColumn
docsBpiCmTEKKeyReplies=_DocsBpiCmTEKKeyReplies_Object((1,3,6,1,2,1,10,127,5,1,1,2,1,6),_DocsBpiCmTEKKeyReplies_Type())
docsBpiCmTEKKeyReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmTEKKeyReplies.setStatus(_A)
_DocsBpiCmTEKKeyRejects_Type=Counter32
_DocsBpiCmTEKKeyRejects_Object=MibTableColumn
docsBpiCmTEKKeyRejects=_DocsBpiCmTEKKeyRejects_Object((1,3,6,1,2,1,10,127,5,1,1,2,1,7),_DocsBpiCmTEKKeyRejects_Type())
docsBpiCmTEKKeyRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmTEKKeyRejects.setStatus(_A)
_DocsBpiCmTEKInvalids_Type=Counter32
_DocsBpiCmTEKInvalids_Object=MibTableColumn
docsBpiCmTEKInvalids=_DocsBpiCmTEKInvalids_Object((1,3,6,1,2,1,10,127,5,1,1,2,1,8),_DocsBpiCmTEKInvalids_Type())
docsBpiCmTEKInvalids.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmTEKInvalids.setStatus(_A)
_DocsBpiCmTEKAuthPends_Type=Counter32
_DocsBpiCmTEKAuthPends_Object=MibTableColumn
docsBpiCmTEKAuthPends=_DocsBpiCmTEKAuthPends_Object((1,3,6,1,2,1,10,127,5,1,1,2,1,9),_DocsBpiCmTEKAuthPends_Type())
docsBpiCmTEKAuthPends.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmTEKAuthPends.setStatus(_A)
class _DocsBpiCmTEKKeyRejectErrorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_N,4)))
_DocsBpiCmTEKKeyRejectErrorCode_Type.__name__=_D
_DocsBpiCmTEKKeyRejectErrorCode_Object=MibTableColumn
docsBpiCmTEKKeyRejectErrorCode=_DocsBpiCmTEKKeyRejectErrorCode_Object((1,3,6,1,2,1,10,127,5,1,1,2,1,10),_DocsBpiCmTEKKeyRejectErrorCode_Type())
docsBpiCmTEKKeyRejectErrorCode.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmTEKKeyRejectErrorCode.setStatus(_A)
class _DocsBpiCmTEKKeyRejectErrorString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_DocsBpiCmTEKKeyRejectErrorString_Type.__name__=_F
_DocsBpiCmTEKKeyRejectErrorString_Object=MibTableColumn
docsBpiCmTEKKeyRejectErrorString=_DocsBpiCmTEKKeyRejectErrorString_Object((1,3,6,1,2,1,10,127,5,1,1,2,1,11),_DocsBpiCmTEKKeyRejectErrorString_Type())
docsBpiCmTEKKeyRejectErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmTEKKeyRejectErrorString.setStatus(_A)
class _DocsBpiCmTEKInvalidErrorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,6)));namedValues=NamedValues(*((_J,1),(_K,2),(_O,6)))
_DocsBpiCmTEKInvalidErrorCode_Type.__name__=_D
_DocsBpiCmTEKInvalidErrorCode_Object=MibTableColumn
docsBpiCmTEKInvalidErrorCode=_DocsBpiCmTEKInvalidErrorCode_Object((1,3,6,1,2,1,10,127,5,1,1,2,1,12),_DocsBpiCmTEKInvalidErrorCode_Type())
docsBpiCmTEKInvalidErrorCode.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmTEKInvalidErrorCode.setStatus(_A)
class _DocsBpiCmTEKInvalidErrorString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_DocsBpiCmTEKInvalidErrorString_Type.__name__=_F
_DocsBpiCmTEKInvalidErrorString_Object=MibTableColumn
docsBpiCmTEKInvalidErrorString=_DocsBpiCmTEKInvalidErrorString_Object((1,3,6,1,2,1,10,127,5,1,1,2,1,13),_DocsBpiCmTEKInvalidErrorString_Type())
docsBpiCmTEKInvalidErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmTEKInvalidErrorString.setStatus(_A)
_DocsBpiCmtsObjects_ObjectIdentity=ObjectIdentity
docsBpiCmtsObjects=_DocsBpiCmtsObjects_ObjectIdentity((1,3,6,1,2,1,10,127,5,1,2))
_DocsBpiCmtsBaseTable_Object=MibTable
docsBpiCmtsBaseTable=_DocsBpiCmtsBaseTable_Object((1,3,6,1,2,1,10,127,5,1,2,1))
if mibBuilder.loadTexts:docsBpiCmtsBaseTable.setStatus(_A)
_DocsBpiCmtsBaseEntry_Object=MibTableRow
docsBpiCmtsBaseEntry=_DocsBpiCmtsBaseEntry_Object((1,3,6,1,2,1,10,127,5,1,2,1,1))
docsBpiCmtsBaseEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:docsBpiCmtsBaseEntry.setStatus(_A)
class _DocsBpiCmtsDefaultAuthLifetime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6048000))
_DocsBpiCmtsDefaultAuthLifetime_Type.__name__=_D
_DocsBpiCmtsDefaultAuthLifetime_Object=MibTableColumn
docsBpiCmtsDefaultAuthLifetime=_DocsBpiCmtsDefaultAuthLifetime_Object((1,3,6,1,2,1,10,127,5,1,2,1,1,1),_DocsBpiCmtsDefaultAuthLifetime_Type())
docsBpiCmtsDefaultAuthLifetime.setMaxAccess(_G)
if mibBuilder.loadTexts:docsBpiCmtsDefaultAuthLifetime.setStatus(_A)
if mibBuilder.loadTexts:docsBpiCmtsDefaultAuthLifetime.setUnits(_E)
class _DocsBpiCmtsDefaultTEKLifetime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,604800))
_DocsBpiCmtsDefaultTEKLifetime_Type.__name__=_D
_DocsBpiCmtsDefaultTEKLifetime_Object=MibTableColumn
docsBpiCmtsDefaultTEKLifetime=_DocsBpiCmtsDefaultTEKLifetime_Object((1,3,6,1,2,1,10,127,5,1,2,1,1,2),_DocsBpiCmtsDefaultTEKLifetime_Type())
docsBpiCmtsDefaultTEKLifetime.setMaxAccess(_G)
if mibBuilder.loadTexts:docsBpiCmtsDefaultTEKLifetime.setStatus(_A)
if mibBuilder.loadTexts:docsBpiCmtsDefaultTEKLifetime.setUnits(_E)
class _DocsBpiCmtsDefaultAuthGraceTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1800))
_DocsBpiCmtsDefaultAuthGraceTime_Type.__name__=_D
_DocsBpiCmtsDefaultAuthGraceTime_Object=MibTableColumn
docsBpiCmtsDefaultAuthGraceTime=_DocsBpiCmtsDefaultAuthGraceTime_Object((1,3,6,1,2,1,10,127,5,1,2,1,1,3),_DocsBpiCmtsDefaultAuthGraceTime_Type())
docsBpiCmtsDefaultAuthGraceTime.setMaxAccess(_G)
if mibBuilder.loadTexts:docsBpiCmtsDefaultAuthGraceTime.setStatus(_R)
if mibBuilder.loadTexts:docsBpiCmtsDefaultAuthGraceTime.setUnits(_E)
class _DocsBpiCmtsDefaultTEKGraceTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1800))
_DocsBpiCmtsDefaultTEKGraceTime_Type.__name__=_D
_DocsBpiCmtsDefaultTEKGraceTime_Object=MibTableColumn
docsBpiCmtsDefaultTEKGraceTime=_DocsBpiCmtsDefaultTEKGraceTime_Object((1,3,6,1,2,1,10,127,5,1,2,1,1,4),_DocsBpiCmtsDefaultTEKGraceTime_Type())
docsBpiCmtsDefaultTEKGraceTime.setMaxAccess(_G)
if mibBuilder.loadTexts:docsBpiCmtsDefaultTEKGraceTime.setStatus(_R)
if mibBuilder.loadTexts:docsBpiCmtsDefaultTEKGraceTime.setUnits(_E)
_DocsBpiCmtsAuthRequests_Type=Counter32
_DocsBpiCmtsAuthRequests_Object=MibTableColumn
docsBpiCmtsAuthRequests=_DocsBpiCmtsAuthRequests_Object((1,3,6,1,2,1,10,127,5,1,2,1,1,5),_DocsBpiCmtsAuthRequests_Type())
docsBpiCmtsAuthRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsAuthRequests.setStatus(_A)
_DocsBpiCmtsAuthReplies_Type=Counter32
_DocsBpiCmtsAuthReplies_Object=MibTableColumn
docsBpiCmtsAuthReplies=_DocsBpiCmtsAuthReplies_Object((1,3,6,1,2,1,10,127,5,1,2,1,1,6),_DocsBpiCmtsAuthReplies_Type())
docsBpiCmtsAuthReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsAuthReplies.setStatus(_A)
_DocsBpiCmtsAuthRejects_Type=Counter32
_DocsBpiCmtsAuthRejects_Object=MibTableColumn
docsBpiCmtsAuthRejects=_DocsBpiCmtsAuthRejects_Object((1,3,6,1,2,1,10,127,5,1,2,1,1,7),_DocsBpiCmtsAuthRejects_Type())
docsBpiCmtsAuthRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsAuthRejects.setStatus(_A)
_DocsBpiCmtsAuthInvalids_Type=Counter32
_DocsBpiCmtsAuthInvalids_Object=MibTableColumn
docsBpiCmtsAuthInvalids=_DocsBpiCmtsAuthInvalids_Object((1,3,6,1,2,1,10,127,5,1,2,1,1,8),_DocsBpiCmtsAuthInvalids_Type())
docsBpiCmtsAuthInvalids.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsAuthInvalids.setStatus(_A)
_DocsBpiCmtsAuthTable_Object=MibTable
docsBpiCmtsAuthTable=_DocsBpiCmtsAuthTable_Object((1,3,6,1,2,1,10,127,5,1,2,2))
if mibBuilder.loadTexts:docsBpiCmtsAuthTable.setStatus(_A)
_DocsBpiCmtsAuthEntry_Object=MibTableRow
docsBpiCmtsAuthEntry=_DocsBpiCmtsAuthEntry_Object((1,3,6,1,2,1,10,127,5,1,2,2,1))
docsBpiCmtsAuthEntry.setIndexNames((0,_H,_I),(0,_B,_X))
if mibBuilder.loadTexts:docsBpiCmtsAuthEntry.setStatus(_A)
_DocsBpiCmtsAuthCmMacAddress_Type=MacAddress
_DocsBpiCmtsAuthCmMacAddress_Object=MibTableColumn
docsBpiCmtsAuthCmMacAddress=_DocsBpiCmtsAuthCmMacAddress_Object((1,3,6,1,2,1,10,127,5,1,2,2,1,1),_DocsBpiCmtsAuthCmMacAddress_Type())
docsBpiCmtsAuthCmMacAddress.setMaxAccess(_L)
if mibBuilder.loadTexts:docsBpiCmtsAuthCmMacAddress.setStatus(_A)
class _DocsBpiCmtsAuthCmPublicKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(74,74),ValueSizeConstraint(106,106),ValueSizeConstraint(140,140),ValueSizeConstraint(270,270))
_DocsBpiCmtsAuthCmPublicKey_Type.__name__=_P
_DocsBpiCmtsAuthCmPublicKey_Object=MibTableColumn
docsBpiCmtsAuthCmPublicKey=_DocsBpiCmtsAuthCmPublicKey_Object((1,3,6,1,2,1,10,127,5,1,2,2,1,2),_DocsBpiCmtsAuthCmPublicKey_Type())
docsBpiCmtsAuthCmPublicKey.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsAuthCmPublicKey.setStatus(_A)
class _DocsBpiCmtsAuthCmKeySequenceNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_DocsBpiCmtsAuthCmKeySequenceNumber_Type.__name__=_D
_DocsBpiCmtsAuthCmKeySequenceNumber_Object=MibTableColumn
docsBpiCmtsAuthCmKeySequenceNumber=_DocsBpiCmtsAuthCmKeySequenceNumber_Object((1,3,6,1,2,1,10,127,5,1,2,2,1,3),_DocsBpiCmtsAuthCmKeySequenceNumber_Type())
docsBpiCmtsAuthCmKeySequenceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsAuthCmKeySequenceNumber.setStatus(_A)
_DocsBpiCmtsAuthCmExpires_Type=DateAndTime
_DocsBpiCmtsAuthCmExpires_Object=MibTableColumn
docsBpiCmtsAuthCmExpires=_DocsBpiCmtsAuthCmExpires_Object((1,3,6,1,2,1,10,127,5,1,2,2,1,4),_DocsBpiCmtsAuthCmExpires_Type())
docsBpiCmtsAuthCmExpires.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsAuthCmExpires.setStatus(_A)
class _DocsBpiCmtsAuthCmLifetime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6048000))
_DocsBpiCmtsAuthCmLifetime_Type.__name__=_D
_DocsBpiCmtsAuthCmLifetime_Object=MibTableColumn
docsBpiCmtsAuthCmLifetime=_DocsBpiCmtsAuthCmLifetime_Object((1,3,6,1,2,1,10,127,5,1,2,2,1,5),_DocsBpiCmtsAuthCmLifetime_Type())
docsBpiCmtsAuthCmLifetime.setMaxAccess(_G)
if mibBuilder.loadTexts:docsBpiCmtsAuthCmLifetime.setStatus(_A)
if mibBuilder.loadTexts:docsBpiCmtsAuthCmLifetime.setUnits(_E)
class _DocsBpiCmtsAuthCmGraceTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1800))
_DocsBpiCmtsAuthCmGraceTime_Type.__name__=_D
_DocsBpiCmtsAuthCmGraceTime_Object=MibTableColumn
docsBpiCmtsAuthCmGraceTime=_DocsBpiCmtsAuthCmGraceTime_Object((1,3,6,1,2,1,10,127,5,1,2,2,1,6),_DocsBpiCmtsAuthCmGraceTime_Type())
docsBpiCmtsAuthCmGraceTime.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsAuthCmGraceTime.setStatus(_A)
if mibBuilder.loadTexts:docsBpiCmtsAuthCmGraceTime.setUnits(_E)
class _DocsBpiCmtsAuthCmReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('noResetRequested',1),('invalidateAuth',2),('sendAuthInvalid',3),('invalidateTeks',4)))
_DocsBpiCmtsAuthCmReset_Type.__name__=_D
_DocsBpiCmtsAuthCmReset_Object=MibTableColumn
docsBpiCmtsAuthCmReset=_DocsBpiCmtsAuthCmReset_Object((1,3,6,1,2,1,10,127,5,1,2,2,1,7),_DocsBpiCmtsAuthCmReset_Type())
docsBpiCmtsAuthCmReset.setMaxAccess(_G)
if mibBuilder.loadTexts:docsBpiCmtsAuthCmReset.setStatus(_A)
_DocsBpiCmtsAuthCmRequests_Type=Counter32
_DocsBpiCmtsAuthCmRequests_Object=MibTableColumn
docsBpiCmtsAuthCmRequests=_DocsBpiCmtsAuthCmRequests_Object((1,3,6,1,2,1,10,127,5,1,2,2,1,8),_DocsBpiCmtsAuthCmRequests_Type())
docsBpiCmtsAuthCmRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsAuthCmRequests.setStatus(_A)
_DocsBpiCmtsAuthCmReplies_Type=Counter32
_DocsBpiCmtsAuthCmReplies_Object=MibTableColumn
docsBpiCmtsAuthCmReplies=_DocsBpiCmtsAuthCmReplies_Object((1,3,6,1,2,1,10,127,5,1,2,2,1,9),_DocsBpiCmtsAuthCmReplies_Type())
docsBpiCmtsAuthCmReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsAuthCmReplies.setStatus(_A)
_DocsBpiCmtsAuthCmRejects_Type=Counter32
_DocsBpiCmtsAuthCmRejects_Object=MibTableColumn
docsBpiCmtsAuthCmRejects=_DocsBpiCmtsAuthCmRejects_Object((1,3,6,1,2,1,10,127,5,1,2,2,1,10),_DocsBpiCmtsAuthCmRejects_Type())
docsBpiCmtsAuthCmRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsAuthCmRejects.setStatus(_A)
_DocsBpiCmtsAuthCmInvalids_Type=Counter32
_DocsBpiCmtsAuthCmInvalids_Object=MibTableColumn
docsBpiCmtsAuthCmInvalids=_DocsBpiCmtsAuthCmInvalids_Object((1,3,6,1,2,1,10,127,5,1,2,2,1,11),_DocsBpiCmtsAuthCmInvalids_Type())
docsBpiCmtsAuthCmInvalids.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsAuthCmInvalids.setStatus(_A)
class _DocsBpiCmtsAuthRejectErrorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_M,3),(_N,4)))
_DocsBpiCmtsAuthRejectErrorCode_Type.__name__=_D
_DocsBpiCmtsAuthRejectErrorCode_Object=MibTableColumn
docsBpiCmtsAuthRejectErrorCode=_DocsBpiCmtsAuthRejectErrorCode_Object((1,3,6,1,2,1,10,127,5,1,2,2,1,12),_DocsBpiCmtsAuthRejectErrorCode_Type())
docsBpiCmtsAuthRejectErrorCode.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsAuthRejectErrorCode.setStatus(_A)
class _DocsBpiCmtsAuthRejectErrorString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_DocsBpiCmtsAuthRejectErrorString_Type.__name__=_F
_DocsBpiCmtsAuthRejectErrorString_Object=MibTableColumn
docsBpiCmtsAuthRejectErrorString=_DocsBpiCmtsAuthRejectErrorString_Object((1,3,6,1,2,1,10,127,5,1,2,2,1,13),_DocsBpiCmtsAuthRejectErrorString_Type())
docsBpiCmtsAuthRejectErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsAuthRejectErrorString.setStatus(_A)
class _DocsBpiCmtsAuthInvalidErrorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,5,6,7)));namedValues=NamedValues(*((_J,1),(_K,2),(_M,3),(_V,5),(_O,6),(_W,7)))
_DocsBpiCmtsAuthInvalidErrorCode_Type.__name__=_D
_DocsBpiCmtsAuthInvalidErrorCode_Object=MibTableColumn
docsBpiCmtsAuthInvalidErrorCode=_DocsBpiCmtsAuthInvalidErrorCode_Object((1,3,6,1,2,1,10,127,5,1,2,2,1,14),_DocsBpiCmtsAuthInvalidErrorCode_Type())
docsBpiCmtsAuthInvalidErrorCode.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsAuthInvalidErrorCode.setStatus(_A)
class _DocsBpiCmtsAuthInvalidErrorString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_DocsBpiCmtsAuthInvalidErrorString_Type.__name__=_F
_DocsBpiCmtsAuthInvalidErrorString_Object=MibTableColumn
docsBpiCmtsAuthInvalidErrorString=_DocsBpiCmtsAuthInvalidErrorString_Object((1,3,6,1,2,1,10,127,5,1,2,2,1,15),_DocsBpiCmtsAuthInvalidErrorString_Type())
docsBpiCmtsAuthInvalidErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsAuthInvalidErrorString.setStatus(_A)
_DocsBpiCmtsTEKTable_Object=MibTable
docsBpiCmtsTEKTable=_DocsBpiCmtsTEKTable_Object((1,3,6,1,2,1,10,127,5,1,2,3))
if mibBuilder.loadTexts:docsBpiCmtsTEKTable.setStatus(_A)
_DocsBpiCmtsTEKEntry_Object=MibTableRow
docsBpiCmtsTEKEntry=_DocsBpiCmtsTEKEntry_Object((1,3,6,1,2,1,10,127,5,1,2,3,1))
docsBpiCmtsTEKEntry.setIndexNames((0,_H,_I),(0,_Q,_U))
if mibBuilder.loadTexts:docsBpiCmtsTEKEntry.setStatus(_A)
class _DocsBpiCmtsTEKLifetime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,604800))
_DocsBpiCmtsTEKLifetime_Type.__name__=_D
_DocsBpiCmtsTEKLifetime_Object=MibTableColumn
docsBpiCmtsTEKLifetime=_DocsBpiCmtsTEKLifetime_Object((1,3,6,1,2,1,10,127,5,1,2,3,1,1),_DocsBpiCmtsTEKLifetime_Type())
docsBpiCmtsTEKLifetime.setMaxAccess(_G)
if mibBuilder.loadTexts:docsBpiCmtsTEKLifetime.setStatus(_A)
if mibBuilder.loadTexts:docsBpiCmtsTEKLifetime.setUnits(_E)
class _DocsBpiCmtsTEKGraceTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1800))
_DocsBpiCmtsTEKGraceTime_Type.__name__=_D
_DocsBpiCmtsTEKGraceTime_Object=MibTableColumn
docsBpiCmtsTEKGraceTime=_DocsBpiCmtsTEKGraceTime_Object((1,3,6,1,2,1,10,127,5,1,2,3,1,2),_DocsBpiCmtsTEKGraceTime_Type())
docsBpiCmtsTEKGraceTime.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsTEKGraceTime.setStatus(_A)
if mibBuilder.loadTexts:docsBpiCmtsTEKGraceTime.setUnits(_E)
_DocsBpiCmtsTEKExpiresOld_Type=DateAndTime
_DocsBpiCmtsTEKExpiresOld_Object=MibTableColumn
docsBpiCmtsTEKExpiresOld=_DocsBpiCmtsTEKExpiresOld_Object((1,3,6,1,2,1,10,127,5,1,2,3,1,3),_DocsBpiCmtsTEKExpiresOld_Type())
docsBpiCmtsTEKExpiresOld.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsTEKExpiresOld.setStatus(_A)
_DocsBpiCmtsTEKExpiresNew_Type=DateAndTime
_DocsBpiCmtsTEKExpiresNew_Object=MibTableColumn
docsBpiCmtsTEKExpiresNew=_DocsBpiCmtsTEKExpiresNew_Object((1,3,6,1,2,1,10,127,5,1,2,3,1,4),_DocsBpiCmtsTEKExpiresNew_Type())
docsBpiCmtsTEKExpiresNew.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsTEKExpiresNew.setStatus(_A)
_DocsBpiCmtsTEKReset_Type=TruthValue
_DocsBpiCmtsTEKReset_Object=MibTableColumn
docsBpiCmtsTEKReset=_DocsBpiCmtsTEKReset_Object((1,3,6,1,2,1,10,127,5,1,2,3,1,5),_DocsBpiCmtsTEKReset_Type())
docsBpiCmtsTEKReset.setMaxAccess(_G)
if mibBuilder.loadTexts:docsBpiCmtsTEKReset.setStatus(_A)
_DocsBpiCmtsKeyRequests_Type=Counter32
_DocsBpiCmtsKeyRequests_Object=MibTableColumn
docsBpiCmtsKeyRequests=_DocsBpiCmtsKeyRequests_Object((1,3,6,1,2,1,10,127,5,1,2,3,1,6),_DocsBpiCmtsKeyRequests_Type())
docsBpiCmtsKeyRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsKeyRequests.setStatus(_A)
_DocsBpiCmtsKeyReplies_Type=Counter32
_DocsBpiCmtsKeyReplies_Object=MibTableColumn
docsBpiCmtsKeyReplies=_DocsBpiCmtsKeyReplies_Object((1,3,6,1,2,1,10,127,5,1,2,3,1,7),_DocsBpiCmtsKeyReplies_Type())
docsBpiCmtsKeyReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsKeyReplies.setStatus(_A)
_DocsBpiCmtsKeyRejects_Type=Counter32
_DocsBpiCmtsKeyRejects_Object=MibTableColumn
docsBpiCmtsKeyRejects=_DocsBpiCmtsKeyRejects_Object((1,3,6,1,2,1,10,127,5,1,2,3,1,8),_DocsBpiCmtsKeyRejects_Type())
docsBpiCmtsKeyRejects.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsKeyRejects.setStatus(_A)
_DocsBpiCmtsTEKInvalids_Type=Counter32
_DocsBpiCmtsTEKInvalids_Object=MibTableColumn
docsBpiCmtsTEKInvalids=_DocsBpiCmtsTEKInvalids_Object((1,3,6,1,2,1,10,127,5,1,2,3,1,9),_DocsBpiCmtsTEKInvalids_Type())
docsBpiCmtsTEKInvalids.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsTEKInvalids.setStatus(_A)
class _DocsBpiCmtsKeyRejectErrorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*((_J,1),(_K,2),(_N,4)))
_DocsBpiCmtsKeyRejectErrorCode_Type.__name__=_D
_DocsBpiCmtsKeyRejectErrorCode_Object=MibTableColumn
docsBpiCmtsKeyRejectErrorCode=_DocsBpiCmtsKeyRejectErrorCode_Object((1,3,6,1,2,1,10,127,5,1,2,3,1,10),_DocsBpiCmtsKeyRejectErrorCode_Type())
docsBpiCmtsKeyRejectErrorCode.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsKeyRejectErrorCode.setStatus(_A)
class _DocsBpiCmtsKeyRejectErrorString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_DocsBpiCmtsKeyRejectErrorString_Type.__name__=_F
_DocsBpiCmtsKeyRejectErrorString_Object=MibTableColumn
docsBpiCmtsKeyRejectErrorString=_DocsBpiCmtsKeyRejectErrorString_Object((1,3,6,1,2,1,10,127,5,1,2,3,1,11),_DocsBpiCmtsKeyRejectErrorString_Type())
docsBpiCmtsKeyRejectErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsKeyRejectErrorString.setStatus(_A)
class _DocsBpiCmtsTEKInvalidErrorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,6)));namedValues=NamedValues(*((_J,1),(_K,2),(_O,6)))
_DocsBpiCmtsTEKInvalidErrorCode_Type.__name__=_D
_DocsBpiCmtsTEKInvalidErrorCode_Object=MibTableColumn
docsBpiCmtsTEKInvalidErrorCode=_DocsBpiCmtsTEKInvalidErrorCode_Object((1,3,6,1,2,1,10,127,5,1,2,3,1,12),_DocsBpiCmtsTEKInvalidErrorCode_Type())
docsBpiCmtsTEKInvalidErrorCode.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsTEKInvalidErrorCode.setStatus(_A)
class _DocsBpiCmtsTEKInvalidErrorString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_DocsBpiCmtsTEKInvalidErrorString_Type.__name__=_F
_DocsBpiCmtsTEKInvalidErrorString_Object=MibTableColumn
docsBpiCmtsTEKInvalidErrorString=_DocsBpiCmtsTEKInvalidErrorString_Object((1,3,6,1,2,1,10,127,5,1,2,3,1,13),_DocsBpiCmtsTEKInvalidErrorString_Type())
docsBpiCmtsTEKInvalidErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:docsBpiCmtsTEKInvalidErrorString.setStatus(_A)
_DocsBpiMulticastControl_ObjectIdentity=ObjectIdentity
docsBpiMulticastControl=_DocsBpiMulticastControl_ObjectIdentity((1,3,6,1,2,1,10,127,5,1,2,4))
_DocsBpiIpMulticastMapTable_Object=MibTable
docsBpiIpMulticastMapTable=_DocsBpiIpMulticastMapTable_Object((1,3,6,1,2,1,10,127,5,1,2,4,1))
if mibBuilder.loadTexts:docsBpiIpMulticastMapTable.setStatus(_A)
_DocsBpiIpMulticastMapEntry_Object=MibTableRow
docsBpiIpMulticastMapEntry=_DocsBpiIpMulticastMapEntry_Object((1,3,6,1,2,1,10,127,5,1,2,4,1,1))
docsBpiIpMulticastMapEntry.setIndexNames((0,_H,_I),(0,_B,_Y),(0,_B,_Z))
if mibBuilder.loadTexts:docsBpiIpMulticastMapEntry.setStatus(_A)
_DocsBpiIpMulticastAddress_Type=IpAddress
_DocsBpiIpMulticastAddress_Object=MibTableColumn
docsBpiIpMulticastAddress=_DocsBpiIpMulticastAddress_Object((1,3,6,1,2,1,10,127,5,1,2,4,1,1,1),_DocsBpiIpMulticastAddress_Type())
docsBpiIpMulticastAddress.setMaxAccess(_L)
if mibBuilder.loadTexts:docsBpiIpMulticastAddress.setStatus(_A)
class _DocsBpiIpMulticastPrefixLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_DocsBpiIpMulticastPrefixLength_Type.__name__=_D
_DocsBpiIpMulticastPrefixLength_Object=MibTableColumn
docsBpiIpMulticastPrefixLength=_DocsBpiIpMulticastPrefixLength_Object((1,3,6,1,2,1,10,127,5,1,2,4,1,1,2),_DocsBpiIpMulticastPrefixLength_Type())
docsBpiIpMulticastPrefixLength.setMaxAccess(_L)
if mibBuilder.loadTexts:docsBpiIpMulticastPrefixLength.setStatus(_A)
class _DocsBpiIpMulticastServiceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8192,16368))
_DocsBpiIpMulticastServiceId_Type.__name__=_D
_DocsBpiIpMulticastServiceId_Object=MibTableColumn
docsBpiIpMulticastServiceId=_DocsBpiIpMulticastServiceId_Object((1,3,6,1,2,1,10,127,5,1,2,4,1,1,3),_DocsBpiIpMulticastServiceId_Type())
docsBpiIpMulticastServiceId.setMaxAccess(_S)
if mibBuilder.loadTexts:docsBpiIpMulticastServiceId.setStatus(_A)
_DocsBpiIpMulticastMapControl_Type=RowStatus
_DocsBpiIpMulticastMapControl_Object=MibTableColumn
docsBpiIpMulticastMapControl=_DocsBpiIpMulticastMapControl_Object((1,3,6,1,2,1,10,127,5,1,2,4,1,1,4),_DocsBpiIpMulticastMapControl_Type())
docsBpiIpMulticastMapControl.setMaxAccess(_S)
if mibBuilder.loadTexts:docsBpiIpMulticastMapControl.setStatus(_A)
_DocsBpiMulticastAuthTable_Object=MibTable
docsBpiMulticastAuthTable=_DocsBpiMulticastAuthTable_Object((1,3,6,1,2,1,10,127,5,1,2,4,2))
if mibBuilder.loadTexts:docsBpiMulticastAuthTable.setStatus(_A)
_DocsBpiMulticastAuthEntry_Object=MibTableRow
docsBpiMulticastAuthEntry=_DocsBpiMulticastAuthEntry_Object((1,3,6,1,2,1,10,127,5,1,2,4,2,1))
docsBpiMulticastAuthEntry.setIndexNames((0,_H,_I),(0,_B,_a),(0,_B,_b))
if mibBuilder.loadTexts:docsBpiMulticastAuthEntry.setStatus(_A)
class _DocsBpiMulticastServiceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(8192,16368))
_DocsBpiMulticastServiceId_Type.__name__=_D
_DocsBpiMulticastServiceId_Object=MibTableColumn
docsBpiMulticastServiceId=_DocsBpiMulticastServiceId_Object((1,3,6,1,2,1,10,127,5,1,2,4,2,1,1),_DocsBpiMulticastServiceId_Type())
docsBpiMulticastServiceId.setMaxAccess(_L)
if mibBuilder.loadTexts:docsBpiMulticastServiceId.setStatus(_A)
_DocsBpiMulticastCmMacAddress_Type=MacAddress
_DocsBpiMulticastCmMacAddress_Object=MibTableColumn
docsBpiMulticastCmMacAddress=_DocsBpiMulticastCmMacAddress_Object((1,3,6,1,2,1,10,127,5,1,2,4,2,1,2),_DocsBpiMulticastCmMacAddress_Type())
docsBpiMulticastCmMacAddress.setMaxAccess(_L)
if mibBuilder.loadTexts:docsBpiMulticastCmMacAddress.setStatus(_A)
_DocsBpiMulticastAuthControl_Type=RowStatus
_DocsBpiMulticastAuthControl_Object=MibTableColumn
docsBpiMulticastAuthControl=_DocsBpiMulticastAuthControl_Object((1,3,6,1,2,1,10,127,5,1,2,4,2,1,3),_DocsBpiMulticastAuthControl_Type())
docsBpiMulticastAuthControl.setMaxAccess(_S)
if mibBuilder.loadTexts:docsBpiMulticastAuthControl.setStatus(_A)
_DocsBpiNotification_ObjectIdentity=ObjectIdentity
docsBpiNotification=_DocsBpiNotification_ObjectIdentity((1,3,6,1,2,1,10,127,5,2))
_DocsBpiConformance_ObjectIdentity=ObjectIdentity
docsBpiConformance=_DocsBpiConformance_ObjectIdentity((1,3,6,1,2,1,10,127,5,3))
_DocsBpiCompliances_ObjectIdentity=ObjectIdentity
docsBpiCompliances=_DocsBpiCompliances_ObjectIdentity((1,3,6,1,2,1,10,127,5,3,1))
_DocsBpiGroups_ObjectIdentity=ObjectIdentity
docsBpiGroups=_DocsBpiGroups_ObjectIdentity((1,3,6,1,2,1,10,127,5,3,2))
docsBpiCmGroup=ObjectGroup((1,3,6,1,2,1,10,127,5,3,2,1))
docsBpiCmGroup.setObjects(*((_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:docsBpiCmGroup.setStatus(_A)
docsBpiCmtsGroup=ObjectGroup((1,3,6,1,2,1,10,127,5,3,2,2))
docsBpiCmtsGroup.setObjects(*((_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN),(_B,_AO),(_B,_AP),(_B,_AQ),(_B,_AR),(_B,_AS),(_B,_AT),(_B,_AU),(_B,_AV),(_B,_AW),(_B,_AX),(_B,_AY),(_B,_AZ),(_B,_Aa),(_B,_Ab),(_B,_Ac),(_B,_Ad),(_B,_Ae),(_B,_Af),(_B,_Ag),(_B,_Ah),(_B,_Ai),(_B,_Aj)))
if mibBuilder.loadTexts:docsBpiCmtsGroup.setStatus(_A)
docsBpiObsoleteObjectsGroup=ObjectGroup((1,3,6,1,2,1,10,127,5,3,2,3))
docsBpiObsoleteObjectsGroup.setObjects(*((_B,_Ak),(_B,_Al)))
if mibBuilder.loadTexts:docsBpiObsoleteObjectsGroup.setStatus(_R)
docsBpiBasicCompliance=ModuleCompliance((1,3,6,1,2,1,10,127,5,3,1,1))
docsBpiBasicCompliance.setObjects(*((_B,_Am),(_B,_An)))
if mibBuilder.loadTexts:docsBpiBasicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'docsBpiMIB':docsBpiMIB,'docsBpiMIBObjects':docsBpiMIBObjects,'docsBpiCmObjects':docsBpiCmObjects,'docsBpiCmBaseTable':docsBpiCmBaseTable,'docsBpiCmBaseEntry':docsBpiCmBaseEntry,_c:docsBpiCmPrivacyEnable,_d:docsBpiCmPublicKey,_e:docsBpiCmAuthState,_f:docsBpiCmAuthKeySequenceNumber,_g:docsBpiCmAuthExpires,_h:docsBpiCmAuthReset,_i:docsBpiCmAuthGraceTime,_j:docsBpiCmTEKGraceTime,_k:docsBpiCmAuthWaitTimeout,_l:docsBpiCmReauthWaitTimeout,_m:docsBpiCmOpWaitTimeout,_n:docsBpiCmRekeyWaitTimeout,_o:docsBpiCmAuthRejectWaitTimeout,_p:docsBpiCmAuthRequests,_q:docsBpiCmAuthReplies,_r:docsBpiCmAuthRejects,_s:docsBpiCmAuthInvalids,_t:docsBpiCmAuthRejectErrorCode,_u:docsBpiCmAuthRejectErrorString,_v:docsBpiCmAuthInvalidErrorCode,_w:docsBpiCmAuthInvalidErrorString,'docsBpiCmTEKTable':docsBpiCmTEKTable,'docsBpiCmTEKEntry':docsBpiCmTEKEntry,_x:docsBpiCmTEKPrivacyEnable,_y:docsBpiCmTEKState,_z:docsBpiCmTEKExpiresOld,_A0:docsBpiCmTEKExpiresNew,_A1:docsBpiCmTEKKeyRequests,_A2:docsBpiCmTEKKeyReplies,_A3:docsBpiCmTEKKeyRejects,_A4:docsBpiCmTEKInvalids,_A5:docsBpiCmTEKAuthPends,_A6:docsBpiCmTEKKeyRejectErrorCode,_A7:docsBpiCmTEKKeyRejectErrorString,_A8:docsBpiCmTEKInvalidErrorCode,_A9:docsBpiCmTEKInvalidErrorString,'docsBpiCmtsObjects':docsBpiCmtsObjects,'docsBpiCmtsBaseTable':docsBpiCmtsBaseTable,'docsBpiCmtsBaseEntry':docsBpiCmtsBaseEntry,_AA:docsBpiCmtsDefaultAuthLifetime,_AB:docsBpiCmtsDefaultTEKLifetime,_Ak:docsBpiCmtsDefaultAuthGraceTime,_Al:docsBpiCmtsDefaultTEKGraceTime,_AC:docsBpiCmtsAuthRequests,_AD:docsBpiCmtsAuthReplies,_AE:docsBpiCmtsAuthRejects,_AF:docsBpiCmtsAuthInvalids,'docsBpiCmtsAuthTable':docsBpiCmtsAuthTable,'docsBpiCmtsAuthEntry':docsBpiCmtsAuthEntry,_X:docsBpiCmtsAuthCmMacAddress,_AG:docsBpiCmtsAuthCmPublicKey,_AH:docsBpiCmtsAuthCmKeySequenceNumber,_AI:docsBpiCmtsAuthCmExpires,_AJ:docsBpiCmtsAuthCmLifetime,_AK:docsBpiCmtsAuthCmGraceTime,_AL:docsBpiCmtsAuthCmReset,_AM:docsBpiCmtsAuthCmRequests,_AN:docsBpiCmtsAuthCmReplies,_AO:docsBpiCmtsAuthCmRejects,_AP:docsBpiCmtsAuthCmInvalids,_AQ:docsBpiCmtsAuthRejectErrorCode,_AR:docsBpiCmtsAuthRejectErrorString,_AS:docsBpiCmtsAuthInvalidErrorCode,_AT:docsBpiCmtsAuthInvalidErrorString,'docsBpiCmtsTEKTable':docsBpiCmtsTEKTable,'docsBpiCmtsTEKEntry':docsBpiCmtsTEKEntry,_AU:docsBpiCmtsTEKLifetime,_AV:docsBpiCmtsTEKGraceTime,_AW:docsBpiCmtsTEKExpiresOld,_AX:docsBpiCmtsTEKExpiresNew,_AY:docsBpiCmtsTEKReset,_AZ:docsBpiCmtsKeyRequests,_Aa:docsBpiCmtsKeyReplies,_Ab:docsBpiCmtsKeyRejects,_Ac:docsBpiCmtsTEKInvalids,_Ad:docsBpiCmtsKeyRejectErrorCode,_Ae:docsBpiCmtsKeyRejectErrorString,_Af:docsBpiCmtsTEKInvalidErrorCode,_Ag:docsBpiCmtsTEKInvalidErrorString,'docsBpiMulticastControl':docsBpiMulticastControl,'docsBpiIpMulticastMapTable':docsBpiIpMulticastMapTable,'docsBpiIpMulticastMapEntry':docsBpiIpMulticastMapEntry,_Y:docsBpiIpMulticastAddress,_Z:docsBpiIpMulticastPrefixLength,_Ah:docsBpiIpMulticastServiceId,_Ai:docsBpiIpMulticastMapControl,'docsBpiMulticastAuthTable':docsBpiMulticastAuthTable,'docsBpiMulticastAuthEntry':docsBpiMulticastAuthEntry,_a:docsBpiMulticastServiceId,_b:docsBpiMulticastCmMacAddress,_Aj:docsBpiMulticastAuthControl,'docsBpiNotification':docsBpiNotification,'docsBpiConformance':docsBpiConformance,'docsBpiCompliances':docsBpiCompliances,'docsBpiBasicCompliance':docsBpiBasicCompliance,'docsBpiGroups':docsBpiGroups,_Am:docsBpiCmGroup,_An:docsBpiCmtsGroup,'docsBpiObsoleteObjectsGroup':docsBpiObsoleteObjectsGroup})