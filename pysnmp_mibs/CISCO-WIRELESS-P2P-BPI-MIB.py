_AC='cwrBpiRmGroup'
_AB='cwrBpiRsGroup'
_AA='cwrBpiRmTEKInvalidErrorString'
_A9='cwrBpiRmTEKInvalidErrorCode'
_A8='cwrBpiRmTEKInvalids'
_A7='cwrBpiRmKeyReplies'
_A6='cwrBpiRmKeyRequests'
_A5='cwrBpiRmTEKReset'
_A4='cwrBpiRmTEKExpiresNew'
_A3='cwrBpiRmTEKExpiresOld'
_A2='cwrBpiRmTEKLifetime'
_A1='cwrBpiRmTEKEncryptionNegotiated'
_A0='cwrBpiRmAuthInvalidErrorString'
_z='cwrBpiRmAuthInvalidErrorCode'
_y='cwrBpiRmAuthRsInvalids'
_x='cwrBpiRmAuthRsReplies'
_w='cwrBpiRmAuthRsRequests'
_v='cwrBpiRmAuthRsReset'
_u='cwrBpiRmAuthRsLifetime'
_t='cwrBpiRmAuthRsExpires'
_s='cwrBpiRmAuthRsKeySequenceNumber'
_r='cwrBpiRmAuthRsPublicKey'
_q='cwrBpiRmAuthPrivacyEnable'
_p='cwrBpiRsTEKInvalidErrorString'
_o='cwrBpiRsTEKInvalidErrorCode'
_n='cwrBpiRsTEKAuthPends'
_m='cwrBpiRsTEKInvalids'
_l='cwrBpiRsTEKKeyReplies'
_k='cwrBpiRsTEKKeyRequests'
_j='cwrBpiRsTEKExpiresNew'
_i='cwrBpiRsTEKExpiresOld'
_h='cwrBpiRsTEKState'
_g='cwrBpiRsTEKEncryptionNegotiated'
_f='cwrBpiRsAuthInvalidErrorString'
_e='cwrBpiRsAuthInvalidErrorCode'
_d='cwrBpiRsAuthInvalids'
_c='cwrBpiRsAuthReplies'
_b='cwrBpiRsAuthRequests'
_a='cwrBpiRsRekeyWaitTimeout'
_Z='cwrBpiRsOpWaitTimeout'
_Y='cwrBpiRsReauthWaitTimeout'
_X='cwrBpiRsAuthWaitTimeout'
_W='cwrBpiRsTEKGraceTime'
_V='cwrBpiRsAuthGraceTime'
_U='cwrBpiRsAuthReset'
_T='cwrBpiRsAuthExpires'
_S='cwrBpiRsAuthKeySequenceNumber'
_R='cwrBpiRsAuthState'
_Q='cwrBpiRsPublicKey'
_P='cwrBpiRsPrivacyEnable'
_O='OctetString'
_N='keyRequestAuthenticationFailure'
_M='invalidKeySequence'
_L='unsolicited'
_K='undefined'
_J='unauthorizedSlave'
_I='noInformation'
_H='ifIndex'
_G='IF-MIB'
_F='seconds'
_E='read-write'
_D='Integer32'
_C='read-only'
_B='CISCO-WIRELESS-P2P-BPI-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_O,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeInterval','TruthValue')
ciscoWirelessP2pBpiMIB=ModuleIdentity((1,3,6,1,4,1,9,9,135))
_CwrBpiMIBObjects_ObjectIdentity=ObjectIdentity
cwrBpiMIBObjects=_CwrBpiMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,135,1))
_CwrBpiRsObjects_ObjectIdentity=ObjectIdentity
cwrBpiRsObjects=_CwrBpiRsObjects_ObjectIdentity((1,3,6,1,4,1,9,9,135,1,1))
_CwrBpiRsBaseTable_Object=MibTable
cwrBpiRsBaseTable=_CwrBpiRsBaseTable_Object((1,3,6,1,4,1,9,9,135,1,1,1))
if mibBuilder.loadTexts:cwrBpiRsBaseTable.setStatus(_A)
_CwrBpiRsBaseEntry_Object=MibTableRow
cwrBpiRsBaseEntry=_CwrBpiRsBaseEntry_Object((1,3,6,1,4,1,9,9,135,1,1,1,1))
cwrBpiRsBaseEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cwrBpiRsBaseEntry.setStatus(_A)
_CwrBpiRsPrivacyEnable_Type=TruthValue
_CwrBpiRsPrivacyEnable_Object=MibTableColumn
cwrBpiRsPrivacyEnable=_CwrBpiRsPrivacyEnable_Object((1,3,6,1,4,1,9,9,135,1,1,1,1,1),_CwrBpiRsPrivacyEnable_Type())
cwrBpiRsPrivacyEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cwrBpiRsPrivacyEnable.setStatus(_A)
class _CwrBpiRsPublicKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,126))
_CwrBpiRsPublicKey_Type.__name__=_O
_CwrBpiRsPublicKey_Object=MibTableColumn
cwrBpiRsPublicKey=_CwrBpiRsPublicKey_Object((1,3,6,1,4,1,9,9,135,1,1,1,1,2),_CwrBpiRsPublicKey_Type())
cwrBpiRsPublicKey.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRsPublicKey.setStatus(_A)
class _CwrBpiRsAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('start',1),('authWait',2),('authorized',3),('reauthWait',4),('authRejectWait',5)))
_CwrBpiRsAuthState_Type.__name__=_D
_CwrBpiRsAuthState_Object=MibTableColumn
cwrBpiRsAuthState=_CwrBpiRsAuthState_Object((1,3,6,1,4,1,9,9,135,1,1,1,1,3),_CwrBpiRsAuthState_Type())
cwrBpiRsAuthState.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRsAuthState.setStatus(_A)
class _CwrBpiRsAuthKeySequenceNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_CwrBpiRsAuthKeySequenceNumber_Type.__name__=_D
_CwrBpiRsAuthKeySequenceNumber_Object=MibTableColumn
cwrBpiRsAuthKeySequenceNumber=_CwrBpiRsAuthKeySequenceNumber_Object((1,3,6,1,4,1,9,9,135,1,1,1,1,4),_CwrBpiRsAuthKeySequenceNumber_Type())
cwrBpiRsAuthKeySequenceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRsAuthKeySequenceNumber.setStatus(_A)
_CwrBpiRsAuthExpires_Type=TimeInterval
_CwrBpiRsAuthExpires_Object=MibTableColumn
cwrBpiRsAuthExpires=_CwrBpiRsAuthExpires_Object((1,3,6,1,4,1,9,9,135,1,1,1,1,5),_CwrBpiRsAuthExpires_Type())
cwrBpiRsAuthExpires.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRsAuthExpires.setStatus(_A)
_CwrBpiRsAuthReset_Type=TruthValue
_CwrBpiRsAuthReset_Object=MibTableColumn
cwrBpiRsAuthReset=_CwrBpiRsAuthReset_Object((1,3,6,1,4,1,9,9,135,1,1,1,1,6),_CwrBpiRsAuthReset_Type())
cwrBpiRsAuthReset.setMaxAccess(_E)
if mibBuilder.loadTexts:cwrBpiRsAuthReset.setStatus(_A)
class _CwrBpiRsAuthGraceTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1800))
_CwrBpiRsAuthGraceTime_Type.__name__=_D
_CwrBpiRsAuthGraceTime_Object=MibTableColumn
cwrBpiRsAuthGraceTime=_CwrBpiRsAuthGraceTime_Object((1,3,6,1,4,1,9,9,135,1,1,1,1,7),_CwrBpiRsAuthGraceTime_Type())
cwrBpiRsAuthGraceTime.setMaxAccess(_E)
if mibBuilder.loadTexts:cwrBpiRsAuthGraceTime.setStatus(_A)
if mibBuilder.loadTexts:cwrBpiRsAuthGraceTime.setUnits(_F)
class _CwrBpiRsTEKGraceTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1800))
_CwrBpiRsTEKGraceTime_Type.__name__=_D
_CwrBpiRsTEKGraceTime_Object=MibTableColumn
cwrBpiRsTEKGraceTime=_CwrBpiRsTEKGraceTime_Object((1,3,6,1,4,1,9,9,135,1,1,1,1,8),_CwrBpiRsTEKGraceTime_Type())
cwrBpiRsTEKGraceTime.setMaxAccess(_E)
if mibBuilder.loadTexts:cwrBpiRsTEKGraceTime.setStatus(_A)
if mibBuilder.loadTexts:cwrBpiRsTEKGraceTime.setUnits(_F)
class _CwrBpiRsAuthWaitTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,30))
_CwrBpiRsAuthWaitTimeout_Type.__name__=_D
_CwrBpiRsAuthWaitTimeout_Object=MibTableColumn
cwrBpiRsAuthWaitTimeout=_CwrBpiRsAuthWaitTimeout_Object((1,3,6,1,4,1,9,9,135,1,1,1,1,9),_CwrBpiRsAuthWaitTimeout_Type())
cwrBpiRsAuthWaitTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:cwrBpiRsAuthWaitTimeout.setStatus(_A)
if mibBuilder.loadTexts:cwrBpiRsAuthWaitTimeout.setUnits(_F)
class _CwrBpiRsReauthWaitTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,30))
_CwrBpiRsReauthWaitTimeout_Type.__name__=_D
_CwrBpiRsReauthWaitTimeout_Object=MibTableColumn
cwrBpiRsReauthWaitTimeout=_CwrBpiRsReauthWaitTimeout_Object((1,3,6,1,4,1,9,9,135,1,1,1,1,10),_CwrBpiRsReauthWaitTimeout_Type())
cwrBpiRsReauthWaitTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:cwrBpiRsReauthWaitTimeout.setStatus(_A)
if mibBuilder.loadTexts:cwrBpiRsReauthWaitTimeout.setUnits(_F)
class _CwrBpiRsOpWaitTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CwrBpiRsOpWaitTimeout_Type.__name__=_D
_CwrBpiRsOpWaitTimeout_Object=MibTableColumn
cwrBpiRsOpWaitTimeout=_CwrBpiRsOpWaitTimeout_Object((1,3,6,1,4,1,9,9,135,1,1,1,1,11),_CwrBpiRsOpWaitTimeout_Type())
cwrBpiRsOpWaitTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:cwrBpiRsOpWaitTimeout.setStatus(_A)
if mibBuilder.loadTexts:cwrBpiRsOpWaitTimeout.setUnits(_F)
class _CwrBpiRsRekeyWaitTimeout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_CwrBpiRsRekeyWaitTimeout_Type.__name__=_D
_CwrBpiRsRekeyWaitTimeout_Object=MibTableColumn
cwrBpiRsRekeyWaitTimeout=_CwrBpiRsRekeyWaitTimeout_Object((1,3,6,1,4,1,9,9,135,1,1,1,1,12),_CwrBpiRsRekeyWaitTimeout_Type())
cwrBpiRsRekeyWaitTimeout.setMaxAccess(_E)
if mibBuilder.loadTexts:cwrBpiRsRekeyWaitTimeout.setStatus(_A)
if mibBuilder.loadTexts:cwrBpiRsRekeyWaitTimeout.setUnits(_F)
_CwrBpiRsAuthRequests_Type=Counter32
_CwrBpiRsAuthRequests_Object=MibTableColumn
cwrBpiRsAuthRequests=_CwrBpiRsAuthRequests_Object((1,3,6,1,4,1,9,9,135,1,1,1,1,13),_CwrBpiRsAuthRequests_Type())
cwrBpiRsAuthRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRsAuthRequests.setStatus(_A)
_CwrBpiRsAuthReplies_Type=Counter32
_CwrBpiRsAuthReplies_Object=MibTableColumn
cwrBpiRsAuthReplies=_CwrBpiRsAuthReplies_Object((1,3,6,1,4,1,9,9,135,1,1,1,1,14),_CwrBpiRsAuthReplies_Type())
cwrBpiRsAuthReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRsAuthReplies.setStatus(_A)
_CwrBpiRsAuthInvalids_Type=Counter32
_CwrBpiRsAuthInvalids_Object=MibTableColumn
cwrBpiRsAuthInvalids=_CwrBpiRsAuthInvalids_Object((1,3,6,1,4,1,9,9,135,1,1,1,1,15),_CwrBpiRsAuthInvalids_Type())
cwrBpiRsAuthInvalids.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRsAuthInvalids.setStatus(_A)
class _CwrBpiRsAuthInvalidErrorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5)))
_CwrBpiRsAuthInvalidErrorCode_Type.__name__=_D
_CwrBpiRsAuthInvalidErrorCode_Object=MibTableColumn
cwrBpiRsAuthInvalidErrorCode=_CwrBpiRsAuthInvalidErrorCode_Object((1,3,6,1,4,1,9,9,135,1,1,1,1,16),_CwrBpiRsAuthInvalidErrorCode_Type())
cwrBpiRsAuthInvalidErrorCode.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRsAuthInvalidErrorCode.setStatus(_A)
_CwrBpiRsAuthInvalidErrorString_Type=DisplayString
_CwrBpiRsAuthInvalidErrorString_Object=MibTableColumn
cwrBpiRsAuthInvalidErrorString=_CwrBpiRsAuthInvalidErrorString_Object((1,3,6,1,4,1,9,9,135,1,1,1,1,17),_CwrBpiRsAuthInvalidErrorString_Type())
cwrBpiRsAuthInvalidErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRsAuthInvalidErrorString.setStatus(_A)
_CwrBpiRsTEKTable_Object=MibTable
cwrBpiRsTEKTable=_CwrBpiRsTEKTable_Object((1,3,6,1,4,1,9,9,135,1,1,2))
if mibBuilder.loadTexts:cwrBpiRsTEKTable.setStatus(_A)
_CwrBpiRsTEKEntry_Object=MibTableRow
cwrBpiRsTEKEntry=_CwrBpiRsTEKEntry_Object((1,3,6,1,4,1,9,9,135,1,1,2,1))
cwrBpiRsTEKEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cwrBpiRsTEKEntry.setStatus(_A)
_CwrBpiRsTEKEncryptionNegotiated_Type=TruthValue
_CwrBpiRsTEKEncryptionNegotiated_Object=MibTableColumn
cwrBpiRsTEKEncryptionNegotiated=_CwrBpiRsTEKEncryptionNegotiated_Object((1,3,6,1,4,1,9,9,135,1,1,2,1,1),_CwrBpiRsTEKEncryptionNegotiated_Type())
cwrBpiRsTEKEncryptionNegotiated.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRsTEKEncryptionNegotiated.setStatus(_A)
class _CwrBpiRsTEKState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('start',1),('opWait',2),('opReauthWait',3),('operational',4),('rekeyWait',5),('rekeyReauthWait',6)))
_CwrBpiRsTEKState_Type.__name__=_D
_CwrBpiRsTEKState_Object=MibTableColumn
cwrBpiRsTEKState=_CwrBpiRsTEKState_Object((1,3,6,1,4,1,9,9,135,1,1,2,1,2),_CwrBpiRsTEKState_Type())
cwrBpiRsTEKState.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRsTEKState.setStatus(_A)
_CwrBpiRsTEKExpiresOld_Type=TimeInterval
_CwrBpiRsTEKExpiresOld_Object=MibTableColumn
cwrBpiRsTEKExpiresOld=_CwrBpiRsTEKExpiresOld_Object((1,3,6,1,4,1,9,9,135,1,1,2,1,3),_CwrBpiRsTEKExpiresOld_Type())
cwrBpiRsTEKExpiresOld.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRsTEKExpiresOld.setStatus(_A)
_CwrBpiRsTEKExpiresNew_Type=TimeInterval
_CwrBpiRsTEKExpiresNew_Object=MibTableColumn
cwrBpiRsTEKExpiresNew=_CwrBpiRsTEKExpiresNew_Object((1,3,6,1,4,1,9,9,135,1,1,2,1,4),_CwrBpiRsTEKExpiresNew_Type())
cwrBpiRsTEKExpiresNew.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRsTEKExpiresNew.setStatus(_A)
_CwrBpiRsTEKKeyRequests_Type=Counter32
_CwrBpiRsTEKKeyRequests_Object=MibTableColumn
cwrBpiRsTEKKeyRequests=_CwrBpiRsTEKKeyRequests_Object((1,3,6,1,4,1,9,9,135,1,1,2,1,5),_CwrBpiRsTEKKeyRequests_Type())
cwrBpiRsTEKKeyRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRsTEKKeyRequests.setStatus(_A)
_CwrBpiRsTEKKeyReplies_Type=Counter32
_CwrBpiRsTEKKeyReplies_Object=MibTableColumn
cwrBpiRsTEKKeyReplies=_CwrBpiRsTEKKeyReplies_Object((1,3,6,1,4,1,9,9,135,1,1,2,1,6),_CwrBpiRsTEKKeyReplies_Type())
cwrBpiRsTEKKeyReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRsTEKKeyReplies.setStatus(_A)
_CwrBpiRsTEKInvalids_Type=Counter32
_CwrBpiRsTEKInvalids_Object=MibTableColumn
cwrBpiRsTEKInvalids=_CwrBpiRsTEKInvalids_Object((1,3,6,1,4,1,9,9,135,1,1,2,1,7),_CwrBpiRsTEKInvalids_Type())
cwrBpiRsTEKInvalids.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRsTEKInvalids.setStatus(_A)
_CwrBpiRsTEKAuthPends_Type=Counter32
_CwrBpiRsTEKAuthPends_Object=MibTableColumn
cwrBpiRsTEKAuthPends=_CwrBpiRsTEKAuthPends_Object((1,3,6,1,4,1,9,9,135,1,1,2,1,8),_CwrBpiRsTEKAuthPends_Type())
cwrBpiRsTEKAuthPends.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRsTEKAuthPends.setStatus(_A)
class _CwrBpiRsTEKInvalidErrorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5)))
_CwrBpiRsTEKInvalidErrorCode_Type.__name__=_D
_CwrBpiRsTEKInvalidErrorCode_Object=MibTableColumn
cwrBpiRsTEKInvalidErrorCode=_CwrBpiRsTEKInvalidErrorCode_Object((1,3,6,1,4,1,9,9,135,1,1,2,1,9),_CwrBpiRsTEKInvalidErrorCode_Type())
cwrBpiRsTEKInvalidErrorCode.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRsTEKInvalidErrorCode.setStatus(_A)
_CwrBpiRsTEKInvalidErrorString_Type=DisplayString
_CwrBpiRsTEKInvalidErrorString_Object=MibTableColumn
cwrBpiRsTEKInvalidErrorString=_CwrBpiRsTEKInvalidErrorString_Object((1,3,6,1,4,1,9,9,135,1,1,2,1,10),_CwrBpiRsTEKInvalidErrorString_Type())
cwrBpiRsTEKInvalidErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRsTEKInvalidErrorString.setStatus(_A)
_CwrBpiRmObjects_ObjectIdentity=ObjectIdentity
cwrBpiRmObjects=_CwrBpiRmObjects_ObjectIdentity((1,3,6,1,4,1,9,9,135,1,2))
_CwrBpiRmAuthTable_Object=MibTable
cwrBpiRmAuthTable=_CwrBpiRmAuthTable_Object((1,3,6,1,4,1,9,9,135,1,2,1))
if mibBuilder.loadTexts:cwrBpiRmAuthTable.setStatus(_A)
_CwrBpiRmAuthEntry_Object=MibTableRow
cwrBpiRmAuthEntry=_CwrBpiRmAuthEntry_Object((1,3,6,1,4,1,9,9,135,1,2,1,1))
cwrBpiRmAuthEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cwrBpiRmAuthEntry.setStatus(_A)
_CwrBpiRmAuthPrivacyEnable_Type=TruthValue
_CwrBpiRmAuthPrivacyEnable_Object=MibTableColumn
cwrBpiRmAuthPrivacyEnable=_CwrBpiRmAuthPrivacyEnable_Object((1,3,6,1,4,1,9,9,135,1,2,1,1,1),_CwrBpiRmAuthPrivacyEnable_Type())
cwrBpiRmAuthPrivacyEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:cwrBpiRmAuthPrivacyEnable.setStatus(_A)
class _CwrBpiRmAuthRsPublicKey_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,126))
_CwrBpiRmAuthRsPublicKey_Type.__name__=_O
_CwrBpiRmAuthRsPublicKey_Object=MibTableColumn
cwrBpiRmAuthRsPublicKey=_CwrBpiRmAuthRsPublicKey_Object((1,3,6,1,4,1,9,9,135,1,2,1,1,2),_CwrBpiRmAuthRsPublicKey_Type())
cwrBpiRmAuthRsPublicKey.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRmAuthRsPublicKey.setStatus(_A)
class _CwrBpiRmAuthRsKeySequenceNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15))
_CwrBpiRmAuthRsKeySequenceNumber_Type.__name__=_D
_CwrBpiRmAuthRsKeySequenceNumber_Object=MibTableColumn
cwrBpiRmAuthRsKeySequenceNumber=_CwrBpiRmAuthRsKeySequenceNumber_Object((1,3,6,1,4,1,9,9,135,1,2,1,1,3),_CwrBpiRmAuthRsKeySequenceNumber_Type())
cwrBpiRmAuthRsKeySequenceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRmAuthRsKeySequenceNumber.setStatus(_A)
_CwrBpiRmAuthRsExpires_Type=TimeInterval
_CwrBpiRmAuthRsExpires_Object=MibTableColumn
cwrBpiRmAuthRsExpires=_CwrBpiRmAuthRsExpires_Object((1,3,6,1,4,1,9,9,135,1,2,1,1,4),_CwrBpiRmAuthRsExpires_Type())
cwrBpiRmAuthRsExpires.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRmAuthRsExpires.setStatus(_A)
class _CwrBpiRmAuthRsLifetime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,6048000))
_CwrBpiRmAuthRsLifetime_Type.__name__=_D
_CwrBpiRmAuthRsLifetime_Object=MibTableColumn
cwrBpiRmAuthRsLifetime=_CwrBpiRmAuthRsLifetime_Object((1,3,6,1,4,1,9,9,135,1,2,1,1,5),_CwrBpiRmAuthRsLifetime_Type())
cwrBpiRmAuthRsLifetime.setMaxAccess(_E)
if mibBuilder.loadTexts:cwrBpiRmAuthRsLifetime.setStatus(_A)
if mibBuilder.loadTexts:cwrBpiRmAuthRsLifetime.setUnits(_F)
_CwrBpiRmAuthRsReset_Type=TruthValue
_CwrBpiRmAuthRsReset_Object=MibTableColumn
cwrBpiRmAuthRsReset=_CwrBpiRmAuthRsReset_Object((1,3,6,1,4,1,9,9,135,1,2,1,1,6),_CwrBpiRmAuthRsReset_Type())
cwrBpiRmAuthRsReset.setMaxAccess(_E)
if mibBuilder.loadTexts:cwrBpiRmAuthRsReset.setStatus(_A)
_CwrBpiRmAuthRsRequests_Type=Counter32
_CwrBpiRmAuthRsRequests_Object=MibTableColumn
cwrBpiRmAuthRsRequests=_CwrBpiRmAuthRsRequests_Object((1,3,6,1,4,1,9,9,135,1,2,1,1,7),_CwrBpiRmAuthRsRequests_Type())
cwrBpiRmAuthRsRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRmAuthRsRequests.setStatus(_A)
_CwrBpiRmAuthRsReplies_Type=Counter32
_CwrBpiRmAuthRsReplies_Object=MibTableColumn
cwrBpiRmAuthRsReplies=_CwrBpiRmAuthRsReplies_Object((1,3,6,1,4,1,9,9,135,1,2,1,1,8),_CwrBpiRmAuthRsReplies_Type())
cwrBpiRmAuthRsReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRmAuthRsReplies.setStatus(_A)
_CwrBpiRmAuthRsInvalids_Type=Counter32
_CwrBpiRmAuthRsInvalids_Object=MibTableColumn
cwrBpiRmAuthRsInvalids=_CwrBpiRmAuthRsInvalids_Object((1,3,6,1,4,1,9,9,135,1,2,1,1,9),_CwrBpiRmAuthRsInvalids_Type())
cwrBpiRmAuthRsInvalids.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRmAuthRsInvalids.setStatus(_A)
class _CwrBpiRmAuthInvalidErrorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5)))
_CwrBpiRmAuthInvalidErrorCode_Type.__name__=_D
_CwrBpiRmAuthInvalidErrorCode_Object=MibTableColumn
cwrBpiRmAuthInvalidErrorCode=_CwrBpiRmAuthInvalidErrorCode_Object((1,3,6,1,4,1,9,9,135,1,2,1,1,10),_CwrBpiRmAuthInvalidErrorCode_Type())
cwrBpiRmAuthInvalidErrorCode.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRmAuthInvalidErrorCode.setStatus(_A)
_CwrBpiRmAuthInvalidErrorString_Type=DisplayString
_CwrBpiRmAuthInvalidErrorString_Object=MibTableColumn
cwrBpiRmAuthInvalidErrorString=_CwrBpiRmAuthInvalidErrorString_Object((1,3,6,1,4,1,9,9,135,1,2,1,1,11),_CwrBpiRmAuthInvalidErrorString_Type())
cwrBpiRmAuthInvalidErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRmAuthInvalidErrorString.setStatus(_A)
_CwrBpiRmTEKTable_Object=MibTable
cwrBpiRmTEKTable=_CwrBpiRmTEKTable_Object((1,3,6,1,4,1,9,9,135,1,2,2))
if mibBuilder.loadTexts:cwrBpiRmTEKTable.setStatus(_A)
_CwrBpiRmTEKEntry_Object=MibTableRow
cwrBpiRmTEKEntry=_CwrBpiRmTEKEntry_Object((1,3,6,1,4,1,9,9,135,1,2,2,1))
cwrBpiRmTEKEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:cwrBpiRmTEKEntry.setStatus(_A)
_CwrBpiRmTEKEncryptionNegotiated_Type=TruthValue
_CwrBpiRmTEKEncryptionNegotiated_Object=MibTableColumn
cwrBpiRmTEKEncryptionNegotiated=_CwrBpiRmTEKEncryptionNegotiated_Object((1,3,6,1,4,1,9,9,135,1,2,2,1,1),_CwrBpiRmTEKEncryptionNegotiated_Type())
cwrBpiRmTEKEncryptionNegotiated.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRmTEKEncryptionNegotiated.setStatus(_A)
class _CwrBpiRmTEKLifetime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,604800))
_CwrBpiRmTEKLifetime_Type.__name__=_D
_CwrBpiRmTEKLifetime_Object=MibTableColumn
cwrBpiRmTEKLifetime=_CwrBpiRmTEKLifetime_Object((1,3,6,1,4,1,9,9,135,1,2,2,1,2),_CwrBpiRmTEKLifetime_Type())
cwrBpiRmTEKLifetime.setMaxAccess(_E)
if mibBuilder.loadTexts:cwrBpiRmTEKLifetime.setStatus(_A)
if mibBuilder.loadTexts:cwrBpiRmTEKLifetime.setUnits(_F)
_CwrBpiRmTEKExpiresOld_Type=TimeInterval
_CwrBpiRmTEKExpiresOld_Object=MibTableColumn
cwrBpiRmTEKExpiresOld=_CwrBpiRmTEKExpiresOld_Object((1,3,6,1,4,1,9,9,135,1,2,2,1,3),_CwrBpiRmTEKExpiresOld_Type())
cwrBpiRmTEKExpiresOld.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRmTEKExpiresOld.setStatus(_A)
_CwrBpiRmTEKExpiresNew_Type=TimeInterval
_CwrBpiRmTEKExpiresNew_Object=MibTableColumn
cwrBpiRmTEKExpiresNew=_CwrBpiRmTEKExpiresNew_Object((1,3,6,1,4,1,9,9,135,1,2,2,1,4),_CwrBpiRmTEKExpiresNew_Type())
cwrBpiRmTEKExpiresNew.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRmTEKExpiresNew.setStatus(_A)
_CwrBpiRmTEKReset_Type=TruthValue
_CwrBpiRmTEKReset_Object=MibTableColumn
cwrBpiRmTEKReset=_CwrBpiRmTEKReset_Object((1,3,6,1,4,1,9,9,135,1,2,2,1,5),_CwrBpiRmTEKReset_Type())
cwrBpiRmTEKReset.setMaxAccess(_E)
if mibBuilder.loadTexts:cwrBpiRmTEKReset.setStatus(_A)
_CwrBpiRmKeyRequests_Type=Counter32
_CwrBpiRmKeyRequests_Object=MibTableColumn
cwrBpiRmKeyRequests=_CwrBpiRmKeyRequests_Object((1,3,6,1,4,1,9,9,135,1,2,2,1,6),_CwrBpiRmKeyRequests_Type())
cwrBpiRmKeyRequests.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRmKeyRequests.setStatus(_A)
_CwrBpiRmKeyReplies_Type=Counter32
_CwrBpiRmKeyReplies_Object=MibTableColumn
cwrBpiRmKeyReplies=_CwrBpiRmKeyReplies_Object((1,3,6,1,4,1,9,9,135,1,2,2,1,7),_CwrBpiRmKeyReplies_Type())
cwrBpiRmKeyReplies.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRmKeyReplies.setStatus(_A)
_CwrBpiRmTEKInvalids_Type=Counter32
_CwrBpiRmTEKInvalids_Object=MibTableColumn
cwrBpiRmTEKInvalids=_CwrBpiRmTEKInvalids_Object((1,3,6,1,4,1,9,9,135,1,2,2,1,8),_CwrBpiRmTEKInvalids_Type())
cwrBpiRmTEKInvalids.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRmTEKInvalids.setStatus(_A)
class _CwrBpiRmTEKInvalidErrorCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_I,0),(_J,1),(_K,2),(_L,3),(_M,4),(_N,5)))
_CwrBpiRmTEKInvalidErrorCode_Type.__name__=_D
_CwrBpiRmTEKInvalidErrorCode_Object=MibTableColumn
cwrBpiRmTEKInvalidErrorCode=_CwrBpiRmTEKInvalidErrorCode_Object((1,3,6,1,4,1,9,9,135,1,2,2,1,9),_CwrBpiRmTEKInvalidErrorCode_Type())
cwrBpiRmTEKInvalidErrorCode.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRmTEKInvalidErrorCode.setStatus(_A)
_CwrBpiRmTEKInvalidErrorString_Type=DisplayString
_CwrBpiRmTEKInvalidErrorString_Object=MibTableColumn
cwrBpiRmTEKInvalidErrorString=_CwrBpiRmTEKInvalidErrorString_Object((1,3,6,1,4,1,9,9,135,1,2,2,1,10),_CwrBpiRmTEKInvalidErrorString_Type())
cwrBpiRmTEKInvalidErrorString.setMaxAccess(_C)
if mibBuilder.loadTexts:cwrBpiRmTEKInvalidErrorString.setStatus(_A)
_CwrBpiNotification_ObjectIdentity=ObjectIdentity
cwrBpiNotification=_CwrBpiNotification_ObjectIdentity((1,3,6,1,4,1,9,9,135,2))
_CwrBpiConformance_ObjectIdentity=ObjectIdentity
cwrBpiConformance=_CwrBpiConformance_ObjectIdentity((1,3,6,1,4,1,9,9,135,3))
_CwrBpiCompliances_ObjectIdentity=ObjectIdentity
cwrBpiCompliances=_CwrBpiCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,135,3,1))
_CwrBpiGroups_ObjectIdentity=ObjectIdentity
cwrBpiGroups=_CwrBpiGroups_ObjectIdentity((1,3,6,1,4,1,9,9,135,3,2))
cwrBpiRsGroup=ObjectGroup((1,3,6,1,4,1,9,9,135,3,2,1))
cwrBpiRsGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:cwrBpiRsGroup.setStatus(_A)
cwrBpiRmGroup=ObjectGroup((1,3,6,1,4,1,9,9,135,3,2,2))
cwrBpiRmGroup.setObjects(*((_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA)))
if mibBuilder.loadTexts:cwrBpiRmGroup.setStatus(_A)
cwrBpiBasicCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,135,3,1,1))
cwrBpiBasicCompliance.setObjects(*((_B,_AB),(_B,_AC)))
if mibBuilder.loadTexts:cwrBpiBasicCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoWirelessP2pBpiMIB':ciscoWirelessP2pBpiMIB,'cwrBpiMIBObjects':cwrBpiMIBObjects,'cwrBpiRsObjects':cwrBpiRsObjects,'cwrBpiRsBaseTable':cwrBpiRsBaseTable,'cwrBpiRsBaseEntry':cwrBpiRsBaseEntry,_P:cwrBpiRsPrivacyEnable,_Q:cwrBpiRsPublicKey,_R:cwrBpiRsAuthState,_S:cwrBpiRsAuthKeySequenceNumber,_T:cwrBpiRsAuthExpires,_U:cwrBpiRsAuthReset,_V:cwrBpiRsAuthGraceTime,_W:cwrBpiRsTEKGraceTime,_X:cwrBpiRsAuthWaitTimeout,_Y:cwrBpiRsReauthWaitTimeout,_Z:cwrBpiRsOpWaitTimeout,_a:cwrBpiRsRekeyWaitTimeout,_b:cwrBpiRsAuthRequests,_c:cwrBpiRsAuthReplies,_d:cwrBpiRsAuthInvalids,_e:cwrBpiRsAuthInvalidErrorCode,_f:cwrBpiRsAuthInvalidErrorString,'cwrBpiRsTEKTable':cwrBpiRsTEKTable,'cwrBpiRsTEKEntry':cwrBpiRsTEKEntry,_g:cwrBpiRsTEKEncryptionNegotiated,_h:cwrBpiRsTEKState,_i:cwrBpiRsTEKExpiresOld,_j:cwrBpiRsTEKExpiresNew,_k:cwrBpiRsTEKKeyRequests,_l:cwrBpiRsTEKKeyReplies,_m:cwrBpiRsTEKInvalids,_n:cwrBpiRsTEKAuthPends,_o:cwrBpiRsTEKInvalidErrorCode,_p:cwrBpiRsTEKInvalidErrorString,'cwrBpiRmObjects':cwrBpiRmObjects,'cwrBpiRmAuthTable':cwrBpiRmAuthTable,'cwrBpiRmAuthEntry':cwrBpiRmAuthEntry,_q:cwrBpiRmAuthPrivacyEnable,_r:cwrBpiRmAuthRsPublicKey,_s:cwrBpiRmAuthRsKeySequenceNumber,_t:cwrBpiRmAuthRsExpires,_u:cwrBpiRmAuthRsLifetime,_v:cwrBpiRmAuthRsReset,_w:cwrBpiRmAuthRsRequests,_x:cwrBpiRmAuthRsReplies,_y:cwrBpiRmAuthRsInvalids,_z:cwrBpiRmAuthInvalidErrorCode,_A0:cwrBpiRmAuthInvalidErrorString,'cwrBpiRmTEKTable':cwrBpiRmTEKTable,'cwrBpiRmTEKEntry':cwrBpiRmTEKEntry,_A1:cwrBpiRmTEKEncryptionNegotiated,_A2:cwrBpiRmTEKLifetime,_A3:cwrBpiRmTEKExpiresOld,_A4:cwrBpiRmTEKExpiresNew,_A5:cwrBpiRmTEKReset,_A6:cwrBpiRmKeyRequests,_A7:cwrBpiRmKeyReplies,_A8:cwrBpiRmTEKInvalids,_A9:cwrBpiRmTEKInvalidErrorCode,_AA:cwrBpiRmTEKInvalidErrorString,'cwrBpiNotification':cwrBpiNotification,'cwrBpiConformance':cwrBpiConformance,'cwrBpiCompliances':cwrBpiCompliances,'cwrBpiBasicCompliance':cwrBpiBasicCompliance,'cwrBpiGroups':cwrBpiGroups,_AB:cwrBpiRsGroup,_AC:cwrBpiRmGroup})