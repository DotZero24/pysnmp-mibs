_Ar='hpicfDot1xAuthConfigGroup10'
_Aq='hpicfDot1xAuthConfigGroup8'
_Ap='hpicfDot1xAuthConfigGroup7'
_Ao='hpicfDot1xPaePortEapRetriesGroup'
_An='hpicfDot1xPaePortGroup1'
_Am='hpicfDot1xSystemGroup'
_Al='hpicfDot1xAuthSessionStatsGroup1'
_Ak='hpicfDot1xPaeAuthSessionGroup1'
_Aj='hpicfDot1xSMAuthSessionTimeoutGroup'
_Ai='hpicfDot1xPaeAuthSessionGroup'
_Ah='hpicfDot1xAuthConfigGroup4'
_Ag='hpicfDot1xAuthConfigGroup3'
_Af='hpicfDot1xAuthConfigGroup2'
_Ae='hpicfDot1xAuthConfigGroup'
_Ad='hpicfDot1xAuthEapTlsFragmentSize'
_Ac='hpicfAuthMaxEapReq'
_Ab='hpicfDot1xPaePortInitialRole'
_Aa='hpicfDot1xPaePortOpenAuthUserRole'
_AZ='hpicfDot1xPaePortOpenAuthDataVid'
_AY='hpicfDot1xPaePortOpenAuthVoiceVid'
_AX='hpicfDot1xPaePortCritAuthUserRole'
_AW='hpicfDot1xPaePortCritAuthDataVid'
_AV='hpicfDot1xPaePortCritAuthVoiceVid'
_AU='hpicfDot1x2010'
_AT='hpicfDot1xAuthSessionRoleName'
_AS='hpicfDot1xPaePortSpeedVSA'
_AR='hpicfDot1xSMAuthSessionTimeout'
_AQ='hpicfDot1xSuppConfigPasswordEncrypted'
_AP='hpicfDot1xSuppConfigPassword'
_AO='hpicfDot1xSuppConfigIdentity'
_AN='hpicfDot1xAuthLastEapolFrameSource'
_AM='hpicfDot1xAuthLastEapolFrameVersion'
_AL='hpicfDot1xAuthEapLengthErrorFramesRx'
_AK='hpicfDot1xAuthInvalidEapolFramesRx'
_AJ='hpicfDot1xAuthEapolReqFramesTx'
_AI='hpicfDot1xAuthEapolReqIdFramesTx'
_AH='hpicfDot1xAuthEapolRespFramesRx'
_AG='hpicfDot1xAuthEapolRespIdFramesRx'
_AF='hpicfDot1xAuthEapolLogoffFramesRx'
_AE='hpicfDot1xAuthEapolStartFramesRx'
_AD='hpicfDot1xAuthEapolFramesTx'
_AC='hpicfDot1xAuthEapolFramesRx'
_AB='hpicfDot1xAuthNumberOfFailedAuthentication'
_AA='hpicfDot1xAuthNumberOfSuccessAuthentication'
_A9='hpicfDot1xSMAuthReAuthEnabled'
_A8='hpicfDot1xSMAuthReAuthPeriod'
_A7='hpicfDot1xSMAuthBackendAuthState'
_A6='hpicfDot1xSMAuthPaeState'
_A5='hpicfDot1xSMAuthReauthenticate'
_A4='hpicfDot1xSMAuthInitialize'
_A3='hpicfDot1xAuthClientLimit'
_A2='hpicfDot1xPaePortMBV'
_A1='hpicfDot1xPaePortSupp'
_A0='hpicfDot1xPaePortAuth'
_z='hpicfDot1xSuppConfigEntry'
_y='hpicfDot1xAuthConfigEntry'
_x='hpicfDot1xPaePortEntry'
_w='initialize'
_v='dot1xPaePortNumber'
_u='IEEE8021-PAE-MIB'
_t='OctetString'
_s='hpicfDot1xAuthDiagGroup'
_r='hpicfDot1xAuthConfigGroup5'
_q='hpicfDot1xAuthUnauthVidLLDPNwkPolicy'
_p='hpicfDot1xAuthEnforceCacheReauth'
_o='hpicfDot1xAuthSessionPerPAECountersEnabled'
_n='hpicfDot1xPaePortMixed'
_m='hpicfDot1xAuthSessionVid'
_l='hpicfDot1xAuthSessionIsForwarding'
_k='hpicfDot1xAuthSessionUserName'
_j='hpicfDot1xAuthSessionTerminateCause'
_i='hpicfDot1xAuthSessionInactiveTime'
_h='hpicfDot1xAuthSessionStopTime'
_g='hpicfDot1xAuthSessionStartTime'
_f='hpicfDot1xAuthSessionTime'
_e='hpicfDot1xAuthSessionAuthenticMethod'
_d='hpicfDot1xAuthSessionId'
_c='hpicfDot1xAuthSessionFramesTx'
_b='hpicfDot1xAuthSessionFramesRx'
_a='hpicfDot1xAuthSessionOctetsTx'
_Z='hpicfDot1xAuthSessionOctetsRx'
_Y='hpicfDot1xSMAuthPaePort'
_X='hpicfDot1xAuthCachedReauthDelay'
_W='seconds'
_V='hpicfDot1xSuppConfigGroup'
_U='hpicfDot1xAuthCachedReauthPeriod'
_T='hpicfDot1xSMAuthMacAddr'
_S='DisplayString'
_R='Integer32'
_Q='hpicfDot1xAuthAllowGvrpVlans'
_P='TruthValue'
_O='hpicfDot1xAuthClientLimit2'
_N='hpicfDot1xAuthLogoffPeriod'
_M='hpicfDot1xAuthUnauthPeriod'
_L='hpicfDot1xAuthUnauthVid'
_K='hpicfDot1xAuthAuthVid'
_J='hpicfDot1xAuthSessionStatsGroup'
_I='Unsigned32'
_H='hpicfDot1xAuthStatsGroup'
_G='hpicfDot1xSMAuthConfigGroup'
_F='hpicfDot1xPaePortGroup'
_E='deprecated'
_D='read-write'
_C='read-only'
_B='current'
_A='HP-DOT1X-EXTENSIONS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_t,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HpAutzUserRoleName,=mibBuilder.importSymbols('HP-AUTZ-MIB','HpAutzUserRoleName')
hpSwitch,=mibBuilder.importSymbols('HP-ICF-OID','hpSwitch')
dot1xAuthConfigEntry,dot1xPaePortEntry,dot1xPaePortNumber,dot1xSuppConfigEntry=mibBuilder.importSymbols(_u,'dot1xAuthConfigEntry','dot1xPaePortEntry',_v,'dot1xSuppConfigEntry')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
VlanIndex,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanIndex')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_R,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_S,'MacAddress','PhysAddress','TextualConvention','TimeStamp',_P)
hpicfDot1xMIB=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,5,1,25))
if mibBuilder.loadTexts:hpicfDot1xMIB.setRevisions(('2021-06-21 00:00','2018-10-30 00:00','2018-06-06 00:00','2017-10-12 00:00','2017-09-28 00:00','2017-09-13 00:00','2016-02-25 00:00','2016-01-21 00:00','2013-06-12 00:00','2013-01-10 00:00','2012-11-15 00:00','2011-08-29 00:00','2011-07-21 00:00','2011-02-12 00:00','2010-04-15 00:00','2009-07-08 00:00','2009-07-02 00:00','2007-02-02 00:00','2005-09-21 00:00','2005-08-05 00:00','2004-08-06 00:00'))
_HpicfDot1xMIBObjects_ObjectIdentity=ObjectIdentity
hpicfDot1xMIBObjects=_HpicfDot1xMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,25,1))
_HpicfDot1xSystem_ObjectIdentity=ObjectIdentity
hpicfDot1xSystem=_HpicfDot1xSystem_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,25,1,1))
_HpicfDot1xPaePortTable_Object=MibTable
hpicfDot1xPaePortTable=_HpicfDot1xPaePortTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,1,1))
if mibBuilder.loadTexts:hpicfDot1xPaePortTable.setStatus(_B)
_HpicfDot1xPaePortEntry_Object=MibTableRow
hpicfDot1xPaePortEntry=_HpicfDot1xPaePortEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,1,1,1))
if mibBuilder.loadTexts:hpicfDot1xPaePortEntry.setStatus(_B)
_HpicfDot1xPaePortAuth_Type=TruthValue
_HpicfDot1xPaePortAuth_Object=MibTableColumn
hpicfDot1xPaePortAuth=_HpicfDot1xPaePortAuth_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,1,1,1,1),_HpicfDot1xPaePortAuth_Type())
hpicfDot1xPaePortAuth.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xPaePortAuth.setStatus(_B)
_HpicfDot1xPaePortSupp_Type=TruthValue
_HpicfDot1xPaePortSupp_Object=MibTableColumn
hpicfDot1xPaePortSupp=_HpicfDot1xPaePortSupp_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,1,1,1,2),_HpicfDot1xPaePortSupp_Type())
hpicfDot1xPaePortSupp.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xPaePortSupp.setStatus(_B)
class _HpicfDot1xPaePortMixed_Type(TruthValue):defaultValue=2
_HpicfDot1xPaePortMixed_Type.__name__=_P
_HpicfDot1xPaePortMixed_Object=MibTableColumn
hpicfDot1xPaePortMixed=_HpicfDot1xPaePortMixed_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,1,1,1,3),_HpicfDot1xPaePortMixed_Type())
hpicfDot1xPaePortMixed.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xPaePortMixed.setStatus(_B)
class _HpicfDot1xPaePortSpeedVSA_Type(TruthValue):defaultValue=2
_HpicfDot1xPaePortSpeedVSA_Type.__name__=_P
_HpicfDot1xPaePortSpeedVSA_Object=MibTableColumn
hpicfDot1xPaePortSpeedVSA=_HpicfDot1xPaePortSpeedVSA_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,1,1,1,4),_HpicfDot1xPaePortSpeedVSA_Type())
hpicfDot1xPaePortSpeedVSA.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xPaePortSpeedVSA.setStatus(_B)
class _HpicfDot1xPaePortMBV_Type(TruthValue):defaultValue=1
_HpicfDot1xPaePortMBV_Type.__name__=_P
_HpicfDot1xPaePortMBV_Object=MibTableColumn
hpicfDot1xPaePortMBV=_HpicfDot1xPaePortMBV_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,1,1,1,5),_HpicfDot1xPaePortMBV_Type())
hpicfDot1xPaePortMBV.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xPaePortMBV.setStatus(_B)
_HpicfDot1xPaePortCritAuthVoiceVid_Type=VlanIndex
_HpicfDot1xPaePortCritAuthVoiceVid_Object=MibTableColumn
hpicfDot1xPaePortCritAuthVoiceVid=_HpicfDot1xPaePortCritAuthVoiceVid_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,1,1,1,6),_HpicfDot1xPaePortCritAuthVoiceVid_Type())
hpicfDot1xPaePortCritAuthVoiceVid.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xPaePortCritAuthVoiceVid.setStatus(_B)
_HpicfDot1xPaePortCritAuthDataVid_Type=VlanIndex
_HpicfDot1xPaePortCritAuthDataVid_Object=MibTableColumn
hpicfDot1xPaePortCritAuthDataVid=_HpicfDot1xPaePortCritAuthDataVid_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,1,1,1,7),_HpicfDot1xPaePortCritAuthDataVid_Type())
hpicfDot1xPaePortCritAuthDataVid.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xPaePortCritAuthDataVid.setStatus(_B)
class _HpicfDot1xPaePortCritAuthUserRole_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpicfDot1xPaePortCritAuthUserRole_Type.__name__=_S
_HpicfDot1xPaePortCritAuthUserRole_Object=MibTableColumn
hpicfDot1xPaePortCritAuthUserRole=_HpicfDot1xPaePortCritAuthUserRole_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,1,1,1,8),_HpicfDot1xPaePortCritAuthUserRole_Type())
hpicfDot1xPaePortCritAuthUserRole.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xPaePortCritAuthUserRole.setStatus(_B)
_HpicfDot1xPaePortOpenAuthVoiceVid_Type=VlanIndex
_HpicfDot1xPaePortOpenAuthVoiceVid_Object=MibTableColumn
hpicfDot1xPaePortOpenAuthVoiceVid=_HpicfDot1xPaePortOpenAuthVoiceVid_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,1,1,1,9),_HpicfDot1xPaePortOpenAuthVoiceVid_Type())
hpicfDot1xPaePortOpenAuthVoiceVid.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xPaePortOpenAuthVoiceVid.setStatus(_B)
_HpicfDot1xPaePortOpenAuthDataVid_Type=VlanIndex
_HpicfDot1xPaePortOpenAuthDataVid_Object=MibTableColumn
hpicfDot1xPaePortOpenAuthDataVid=_HpicfDot1xPaePortOpenAuthDataVid_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,1,1,1,10),_HpicfDot1xPaePortOpenAuthDataVid_Type())
hpicfDot1xPaePortOpenAuthDataVid.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xPaePortOpenAuthDataVid.setStatus(_B)
class _HpicfDot1xPaePortOpenAuthUserRole_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpicfDot1xPaePortOpenAuthUserRole_Type.__name__=_S
_HpicfDot1xPaePortOpenAuthUserRole_Object=MibTableColumn
hpicfDot1xPaePortOpenAuthUserRole=_HpicfDot1xPaePortOpenAuthUserRole_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,1,1,1,11),_HpicfDot1xPaePortOpenAuthUserRole_Type())
hpicfDot1xPaePortOpenAuthUserRole.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xPaePortOpenAuthUserRole.setStatus(_B)
class _HpicfDot1xPaePortInitialRole_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpicfDot1xPaePortInitialRole_Type.__name__=_S
_HpicfDot1xPaePortInitialRole_Object=MibTableColumn
hpicfDot1xPaePortInitialRole=_HpicfDot1xPaePortInitialRole_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,1,1,1,12),_HpicfDot1xPaePortInitialRole_Type())
hpicfDot1xPaePortInitialRole.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xPaePortInitialRole.setStatus(_B)
class _HpicfDot1x2010_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('disabled',0),('authenticator',1),('supplicant',2),('authenticatorAndSupplicant',3)))
_HpicfDot1x2010_Type.__name__=_R
_HpicfDot1x2010_Object=MibScalar
hpicfDot1x2010=_HpicfDot1x2010_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,1,2),_HpicfDot1x2010_Type())
hpicfDot1x2010.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1x2010.setStatus(_B)
_HpicfDot1xAuthenticator_ObjectIdentity=ObjectIdentity
hpicfDot1xAuthenticator=_HpicfDot1xAuthenticator_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2))
_HpicfDot1xAuthConfigTable_Object=MibTable
hpicfDot1xAuthConfigTable=_HpicfDot1xAuthConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,1))
if mibBuilder.loadTexts:hpicfDot1xAuthConfigTable.setStatus(_B)
_HpicfDot1xAuthConfigEntry_Object=MibTableRow
hpicfDot1xAuthConfigEntry=_HpicfDot1xAuthConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,1,1))
if mibBuilder.loadTexts:hpicfDot1xAuthConfigEntry.setStatus(_B)
_HpicfDot1xAuthAuthVid_Type=VlanIndex
_HpicfDot1xAuthAuthVid_Object=MibTableColumn
hpicfDot1xAuthAuthVid=_HpicfDot1xAuthAuthVid_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,1,1,1),_HpicfDot1xAuthAuthVid_Type())
hpicfDot1xAuthAuthVid.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xAuthAuthVid.setStatus(_B)
_HpicfDot1xAuthUnauthVid_Type=VlanIndex
_HpicfDot1xAuthUnauthVid_Object=MibTableColumn
hpicfDot1xAuthUnauthVid=_HpicfDot1xAuthUnauthVid_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,1,1,2),_HpicfDot1xAuthUnauthVid_Type())
hpicfDot1xAuthUnauthVid.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xAuthUnauthVid.setStatus(_B)
class _HpicfDot1xAuthUnauthPeriod_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpicfDot1xAuthUnauthPeriod_Type.__name__=_I
_HpicfDot1xAuthUnauthPeriod_Object=MibTableColumn
hpicfDot1xAuthUnauthPeriod=_HpicfDot1xAuthUnauthPeriod_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,1,1,3),_HpicfDot1xAuthUnauthPeriod_Type())
hpicfDot1xAuthUnauthPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xAuthUnauthPeriod.setStatus(_B)
if mibBuilder.loadTexts:hpicfDot1xAuthUnauthPeriod.setUnits(_W)
class _HpicfDot1xAuthClientLimit_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_HpicfDot1xAuthClientLimit_Type.__name__=_I
_HpicfDot1xAuthClientLimit_Object=MibTableColumn
hpicfDot1xAuthClientLimit=_HpicfDot1xAuthClientLimit_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,1,1,4),_HpicfDot1xAuthClientLimit_Type())
hpicfDot1xAuthClientLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xAuthClientLimit.setStatus(_E)
class _HpicfDot1xAuthLogoffPeriod_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,999999999))
_HpicfDot1xAuthLogoffPeriod_Type.__name__=_I
_HpicfDot1xAuthLogoffPeriod_Object=MibTableColumn
hpicfDot1xAuthLogoffPeriod=_HpicfDot1xAuthLogoffPeriod_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,1,1,5),_HpicfDot1xAuthLogoffPeriod_Type())
hpicfDot1xAuthLogoffPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xAuthLogoffPeriod.setStatus(_B)
if mibBuilder.loadTexts:hpicfDot1xAuthLogoffPeriod.setUnits(_W)
class _HpicfDot1xAuthClientLimit2_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_HpicfDot1xAuthClientLimit2_Type.__name__=_I
_HpicfDot1xAuthClientLimit2_Object=MibTableColumn
hpicfDot1xAuthClientLimit2=_HpicfDot1xAuthClientLimit2_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,1,1,6),_HpicfDot1xAuthClientLimit2_Type())
hpicfDot1xAuthClientLimit2.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xAuthClientLimit2.setStatus(_B)
class _HpicfDot1xAuthCachedReauthPeriod_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpicfDot1xAuthCachedReauthPeriod_Type.__name__=_I
_HpicfDot1xAuthCachedReauthPeriod_Object=MibTableColumn
hpicfDot1xAuthCachedReauthPeriod=_HpicfDot1xAuthCachedReauthPeriod_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,1,1,7),_HpicfDot1xAuthCachedReauthPeriod_Type())
hpicfDot1xAuthCachedReauthPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xAuthCachedReauthPeriod.setStatus(_B)
if mibBuilder.loadTexts:hpicfDot1xAuthCachedReauthPeriod.setUnits(_W)
class _HpicfDot1xAuthEnforceCacheReauth_Type(TruthValue):defaultValue=2
_HpicfDot1xAuthEnforceCacheReauth_Type.__name__=_P
_HpicfDot1xAuthEnforceCacheReauth_Object=MibTableColumn
hpicfDot1xAuthEnforceCacheReauth=_HpicfDot1xAuthEnforceCacheReauth_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,1,1,8),_HpicfDot1xAuthEnforceCacheReauth_Type())
hpicfDot1xAuthEnforceCacheReauth.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xAuthEnforceCacheReauth.setStatus(_B)
class _HpicfAuthMaxEapReq_Type(Unsigned32):defaultValue=2
_HpicfAuthMaxEapReq_Type.__name__=_I
_HpicfAuthMaxEapReq_Object=MibTableColumn
hpicfAuthMaxEapReq=_HpicfAuthMaxEapReq_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,1,1,9),_HpicfAuthMaxEapReq_Type())
hpicfAuthMaxEapReq.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfAuthMaxEapReq.setStatus(_B)
class _HpicfDot1xAuthUnauthVidLLDPNwkPolicy_Type(TruthValue):defaultValue=2
_HpicfDot1xAuthUnauthVidLLDPNwkPolicy_Type.__name__=_P
_HpicfDot1xAuthUnauthVidLLDPNwkPolicy_Object=MibTableColumn
hpicfDot1xAuthUnauthVidLLDPNwkPolicy=_HpicfDot1xAuthUnauthVidLLDPNwkPolicy_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,1,1,11),_HpicfDot1xAuthUnauthVidLLDPNwkPolicy_Type())
hpicfDot1xAuthUnauthVidLLDPNwkPolicy.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xAuthUnauthVidLLDPNwkPolicy.setStatus(_B)
_HpicfDot1xSMAuthConfigTable_Object=MibTable
hpicfDot1xSMAuthConfigTable=_HpicfDot1xSMAuthConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,2))
if mibBuilder.loadTexts:hpicfDot1xSMAuthConfigTable.setStatus(_B)
_HpicfDot1xSMAuthConfigEntry_Object=MibTableRow
hpicfDot1xSMAuthConfigEntry=_HpicfDot1xSMAuthConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,2,1))
hpicfDot1xSMAuthConfigEntry.setIndexNames((0,_A,_Y),(0,_A,_T))
if mibBuilder.loadTexts:hpicfDot1xSMAuthConfigEntry.setStatus(_B)
_HpicfDot1xSMAuthPaePort_Type=InterfaceIndex
_HpicfDot1xSMAuthPaePort_Object=MibTableColumn
hpicfDot1xSMAuthPaePort=_HpicfDot1xSMAuthPaePort_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,2,1,1),_HpicfDot1xSMAuthPaePort_Type())
hpicfDot1xSMAuthPaePort.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpicfDot1xSMAuthPaePort.setStatus(_B)
_HpicfDot1xSMAuthMacAddr_Type=MacAddress
_HpicfDot1xSMAuthMacAddr_Object=MibTableColumn
hpicfDot1xSMAuthMacAddr=_HpicfDot1xSMAuthMacAddr_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,2,1,2),_HpicfDot1xSMAuthMacAddr_Type())
hpicfDot1xSMAuthMacAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xSMAuthMacAddr.setStatus(_B)
_HpicfDot1xSMAuthInitialize_Type=TruthValue
_HpicfDot1xSMAuthInitialize_Object=MibTableColumn
hpicfDot1xSMAuthInitialize=_HpicfDot1xSMAuthInitialize_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,2,1,3),_HpicfDot1xSMAuthInitialize_Type())
hpicfDot1xSMAuthInitialize.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xSMAuthInitialize.setStatus(_B)
_HpicfDot1xSMAuthReauthenticate_Type=TruthValue
_HpicfDot1xSMAuthReauthenticate_Object=MibTableColumn
hpicfDot1xSMAuthReauthenticate=_HpicfDot1xSMAuthReauthenticate_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,2,1,4),_HpicfDot1xSMAuthReauthenticate_Type())
hpicfDot1xSMAuthReauthenticate.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xSMAuthReauthenticate.setStatus(_B)
class _HpicfDot1xSMAuthPaeState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17)));namedValues=NamedValues(*((_w,1),('disconnected',2),('connecting',3),('authenticating',4),('authenticated',5),('aborting',6),('held',7),('forceAuth',8),('forceUnauth',9),('restart',10),('heldNoVlan',11),('heldUnauthVlan',12),('initialRole',14),('heldInitialRoleFailed',15),('criticalAuth',16),('openAuth',17)))
_HpicfDot1xSMAuthPaeState_Type.__name__=_R
_HpicfDot1xSMAuthPaeState_Object=MibTableColumn
hpicfDot1xSMAuthPaeState=_HpicfDot1xSMAuthPaeState_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,2,1,5),_HpicfDot1xSMAuthPaeState_Type())
hpicfDot1xSMAuthPaeState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xSMAuthPaeState.setStatus(_B)
class _HpicfDot1xSMAuthBackendAuthState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('request',1),('response',2),('success',3),('fail',4),('timeout',5),('idle',6),(_w,7),('ignore',8),('applyInitialRole',9)))
_HpicfDot1xSMAuthBackendAuthState_Type.__name__=_R
_HpicfDot1xSMAuthBackendAuthState_Object=MibTableColumn
hpicfDot1xSMAuthBackendAuthState=_HpicfDot1xSMAuthBackendAuthState_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,2,1,6),_HpicfDot1xSMAuthBackendAuthState_Type())
hpicfDot1xSMAuthBackendAuthState.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xSMAuthBackendAuthState.setStatus(_B)
class _HpicfDot1xSMAuthReAuthPeriod_Type(Unsigned32):defaultValue=3600
_HpicfDot1xSMAuthReAuthPeriod_Type.__name__=_I
_HpicfDot1xSMAuthReAuthPeriod_Object=MibTableColumn
hpicfDot1xSMAuthReAuthPeriod=_HpicfDot1xSMAuthReAuthPeriod_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,2,1,7),_HpicfDot1xSMAuthReAuthPeriod_Type())
hpicfDot1xSMAuthReAuthPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xSMAuthReAuthPeriod.setStatus(_B)
class _HpicfDot1xSMAuthReAuthEnabled_Type(TruthValue):defaultValue=2
_HpicfDot1xSMAuthReAuthEnabled_Type.__name__=_P
_HpicfDot1xSMAuthReAuthEnabled_Object=MibTableColumn
hpicfDot1xSMAuthReAuthEnabled=_HpicfDot1xSMAuthReAuthEnabled_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,2,1,8),_HpicfDot1xSMAuthReAuthEnabled_Type())
hpicfDot1xSMAuthReAuthEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xSMAuthReAuthEnabled.setStatus(_B)
class _HpicfDot1xSMAuthSessionTimeout_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpicfDot1xSMAuthSessionTimeout_Type.__name__=_I
_HpicfDot1xSMAuthSessionTimeout_Object=MibTableColumn
hpicfDot1xSMAuthSessionTimeout=_HpicfDot1xSMAuthSessionTimeout_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,2,1,9),_HpicfDot1xSMAuthSessionTimeout_Type())
hpicfDot1xSMAuthSessionTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xSMAuthSessionTimeout.setStatus(_B)
if mibBuilder.loadTexts:hpicfDot1xSMAuthSessionTimeout.setUnits(_W)
_HpicfDot1xAuthDiagTable_Object=MibTable
hpicfDot1xAuthDiagTable=_HpicfDot1xAuthDiagTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,3))
if mibBuilder.loadTexts:hpicfDot1xAuthDiagTable.setStatus(_B)
_HpicfDot1xAuthDiagEntry_Object=MibTableRow
hpicfDot1xAuthDiagEntry=_HpicfDot1xAuthDiagEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,3,1))
hpicfDot1xAuthDiagEntry.setIndexNames((0,_u,_v))
if mibBuilder.loadTexts:hpicfDot1xAuthDiagEntry.setStatus(_B)
_HpicfDot1xAuthNumberOfSuccessAuthentication_Type=Counter32
_HpicfDot1xAuthNumberOfSuccessAuthentication_Object=MibTableColumn
hpicfDot1xAuthNumberOfSuccessAuthentication=_HpicfDot1xAuthNumberOfSuccessAuthentication_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,3,1,1),_HpicfDot1xAuthNumberOfSuccessAuthentication_Type())
hpicfDot1xAuthNumberOfSuccessAuthentication.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthNumberOfSuccessAuthentication.setStatus(_B)
_HpicfDot1xAuthNumberOfFailedAuthentication_Type=Counter32
_HpicfDot1xAuthNumberOfFailedAuthentication_Object=MibTableColumn
hpicfDot1xAuthNumberOfFailedAuthentication=_HpicfDot1xAuthNumberOfFailedAuthentication_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,3,1,2),_HpicfDot1xAuthNumberOfFailedAuthentication_Type())
hpicfDot1xAuthNumberOfFailedAuthentication.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthNumberOfFailedAuthentication.setStatus(_B)
_HpicfDot1xAuthStatsTable_Object=MibTable
hpicfDot1xAuthStatsTable=_HpicfDot1xAuthStatsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,4))
if mibBuilder.loadTexts:hpicfDot1xAuthStatsTable.setStatus(_B)
_HpicfDot1xAuthStatsEntry_Object=MibTableRow
hpicfDot1xAuthStatsEntry=_HpicfDot1xAuthStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,4,1))
hpicfDot1xAuthStatsEntry.setIndexNames((0,_A,_Y),(0,_A,_T))
if mibBuilder.loadTexts:hpicfDot1xAuthStatsEntry.setStatus(_B)
_HpicfDot1xAuthEapolFramesRx_Type=Counter32
_HpicfDot1xAuthEapolFramesRx_Object=MibTableColumn
hpicfDot1xAuthEapolFramesRx=_HpicfDot1xAuthEapolFramesRx_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,4,1,1),_HpicfDot1xAuthEapolFramesRx_Type())
hpicfDot1xAuthEapolFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthEapolFramesRx.setStatus(_B)
_HpicfDot1xAuthEapolFramesTx_Type=Counter32
_HpicfDot1xAuthEapolFramesTx_Object=MibTableColumn
hpicfDot1xAuthEapolFramesTx=_HpicfDot1xAuthEapolFramesTx_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,4,1,2),_HpicfDot1xAuthEapolFramesTx_Type())
hpicfDot1xAuthEapolFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthEapolFramesTx.setStatus(_B)
_HpicfDot1xAuthEapolStartFramesRx_Type=Counter32
_HpicfDot1xAuthEapolStartFramesRx_Object=MibTableColumn
hpicfDot1xAuthEapolStartFramesRx=_HpicfDot1xAuthEapolStartFramesRx_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,4,1,3),_HpicfDot1xAuthEapolStartFramesRx_Type())
hpicfDot1xAuthEapolStartFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthEapolStartFramesRx.setStatus(_B)
_HpicfDot1xAuthEapolLogoffFramesRx_Type=Counter32
_HpicfDot1xAuthEapolLogoffFramesRx_Object=MibTableColumn
hpicfDot1xAuthEapolLogoffFramesRx=_HpicfDot1xAuthEapolLogoffFramesRx_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,4,1,4),_HpicfDot1xAuthEapolLogoffFramesRx_Type())
hpicfDot1xAuthEapolLogoffFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthEapolLogoffFramesRx.setStatus(_B)
_HpicfDot1xAuthEapolRespIdFramesRx_Type=Counter32
_HpicfDot1xAuthEapolRespIdFramesRx_Object=MibTableColumn
hpicfDot1xAuthEapolRespIdFramesRx=_HpicfDot1xAuthEapolRespIdFramesRx_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,4,1,5),_HpicfDot1xAuthEapolRespIdFramesRx_Type())
hpicfDot1xAuthEapolRespIdFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthEapolRespIdFramesRx.setStatus(_B)
_HpicfDot1xAuthEapolRespFramesRx_Type=Counter32
_HpicfDot1xAuthEapolRespFramesRx_Object=MibTableColumn
hpicfDot1xAuthEapolRespFramesRx=_HpicfDot1xAuthEapolRespFramesRx_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,4,1,6),_HpicfDot1xAuthEapolRespFramesRx_Type())
hpicfDot1xAuthEapolRespFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthEapolRespFramesRx.setStatus(_B)
_HpicfDot1xAuthEapolReqIdFramesTx_Type=Counter32
_HpicfDot1xAuthEapolReqIdFramesTx_Object=MibTableColumn
hpicfDot1xAuthEapolReqIdFramesTx=_HpicfDot1xAuthEapolReqIdFramesTx_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,4,1,7),_HpicfDot1xAuthEapolReqIdFramesTx_Type())
hpicfDot1xAuthEapolReqIdFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthEapolReqIdFramesTx.setStatus(_B)
_HpicfDot1xAuthEapolReqFramesTx_Type=Counter32
_HpicfDot1xAuthEapolReqFramesTx_Object=MibTableColumn
hpicfDot1xAuthEapolReqFramesTx=_HpicfDot1xAuthEapolReqFramesTx_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,4,1,8),_HpicfDot1xAuthEapolReqFramesTx_Type())
hpicfDot1xAuthEapolReqFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthEapolReqFramesTx.setStatus(_B)
_HpicfDot1xAuthInvalidEapolFramesRx_Type=Counter32
_HpicfDot1xAuthInvalidEapolFramesRx_Object=MibTableColumn
hpicfDot1xAuthInvalidEapolFramesRx=_HpicfDot1xAuthInvalidEapolFramesRx_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,4,1,9),_HpicfDot1xAuthInvalidEapolFramesRx_Type())
hpicfDot1xAuthInvalidEapolFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthInvalidEapolFramesRx.setStatus(_B)
_HpicfDot1xAuthEapLengthErrorFramesRx_Type=Counter32
_HpicfDot1xAuthEapLengthErrorFramesRx_Object=MibTableColumn
hpicfDot1xAuthEapLengthErrorFramesRx=_HpicfDot1xAuthEapLengthErrorFramesRx_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,4,1,10),_HpicfDot1xAuthEapLengthErrorFramesRx_Type())
hpicfDot1xAuthEapLengthErrorFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthEapLengthErrorFramesRx.setStatus(_B)
_HpicfDot1xAuthLastEapolFrameVersion_Type=Unsigned32
_HpicfDot1xAuthLastEapolFrameVersion_Object=MibTableColumn
hpicfDot1xAuthLastEapolFrameVersion=_HpicfDot1xAuthLastEapolFrameVersion_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,4,1,11),_HpicfDot1xAuthLastEapolFrameVersion_Type())
hpicfDot1xAuthLastEapolFrameVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthLastEapolFrameVersion.setStatus(_B)
_HpicfDot1xAuthLastEapolFrameSource_Type=MacAddress
_HpicfDot1xAuthLastEapolFrameSource_Object=MibTableColumn
hpicfDot1xAuthLastEapolFrameSource=_HpicfDot1xAuthLastEapolFrameSource_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,4,1,12),_HpicfDot1xAuthLastEapolFrameSource_Type())
hpicfDot1xAuthLastEapolFrameSource.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthLastEapolFrameSource.setStatus(_B)
_HpicfDot1xAuthSessionStatsTable_Object=MibTable
hpicfDot1xAuthSessionStatsTable=_HpicfDot1xAuthSessionStatsTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,5))
if mibBuilder.loadTexts:hpicfDot1xAuthSessionStatsTable.setStatus(_B)
_HpicfDot1xAuthSessionStatsEntry_Object=MibTableRow
hpicfDot1xAuthSessionStatsEntry=_HpicfDot1xAuthSessionStatsEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,5,1))
hpicfDot1xAuthSessionStatsEntry.setIndexNames((0,_A,_Y),(0,_A,_T))
if mibBuilder.loadTexts:hpicfDot1xAuthSessionStatsEntry.setStatus(_B)
_HpicfDot1xAuthSessionPerPAECountersEnabled_Type=TruthValue
_HpicfDot1xAuthSessionPerPAECountersEnabled_Object=MibTableColumn
hpicfDot1xAuthSessionPerPAECountersEnabled=_HpicfDot1xAuthSessionPerPAECountersEnabled_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,5,1,1),_HpicfDot1xAuthSessionPerPAECountersEnabled_Type())
hpicfDot1xAuthSessionPerPAECountersEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthSessionPerPAECountersEnabled.setStatus(_B)
_HpicfDot1xAuthSessionOctetsRx_Type=Counter64
_HpicfDot1xAuthSessionOctetsRx_Object=MibTableColumn
hpicfDot1xAuthSessionOctetsRx=_HpicfDot1xAuthSessionOctetsRx_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,5,1,2),_HpicfDot1xAuthSessionOctetsRx_Type())
hpicfDot1xAuthSessionOctetsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthSessionOctetsRx.setStatus(_B)
_HpicfDot1xAuthSessionOctetsTx_Type=Counter64
_HpicfDot1xAuthSessionOctetsTx_Object=MibTableColumn
hpicfDot1xAuthSessionOctetsTx=_HpicfDot1xAuthSessionOctetsTx_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,5,1,3),_HpicfDot1xAuthSessionOctetsTx_Type())
hpicfDot1xAuthSessionOctetsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthSessionOctetsTx.setStatus(_B)
_HpicfDot1xAuthSessionFramesRx_Type=Counter32
_HpicfDot1xAuthSessionFramesRx_Object=MibTableColumn
hpicfDot1xAuthSessionFramesRx=_HpicfDot1xAuthSessionFramesRx_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,5,1,4),_HpicfDot1xAuthSessionFramesRx_Type())
hpicfDot1xAuthSessionFramesRx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthSessionFramesRx.setStatus(_B)
_HpicfDot1xAuthSessionFramesTx_Type=Counter32
_HpicfDot1xAuthSessionFramesTx_Object=MibTableColumn
hpicfDot1xAuthSessionFramesTx=_HpicfDot1xAuthSessionFramesTx_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,5,1,5),_HpicfDot1xAuthSessionFramesTx_Type())
hpicfDot1xAuthSessionFramesTx.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthSessionFramesTx.setStatus(_B)
_HpicfDot1xAuthSessionId_Type=SnmpAdminString
_HpicfDot1xAuthSessionId_Object=MibTableColumn
hpicfDot1xAuthSessionId=_HpicfDot1xAuthSessionId_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,5,1,6),_HpicfDot1xAuthSessionId_Type())
hpicfDot1xAuthSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthSessionId.setStatus(_B)
class _HpicfDot1xAuthSessionAuthenticMethod_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('remoteAuthServer',1),('localAuthServer',2),('localandremoteAuthServer',3)))
_HpicfDot1xAuthSessionAuthenticMethod_Type.__name__=_R
_HpicfDot1xAuthSessionAuthenticMethod_Object=MibTableColumn
hpicfDot1xAuthSessionAuthenticMethod=_HpicfDot1xAuthSessionAuthenticMethod_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,5,1,7),_HpicfDot1xAuthSessionAuthenticMethod_Type())
hpicfDot1xAuthSessionAuthenticMethod.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthSessionAuthenticMethod.setStatus(_B)
_HpicfDot1xAuthSessionTime_Type=TimeTicks
_HpicfDot1xAuthSessionTime_Object=MibTableColumn
hpicfDot1xAuthSessionTime=_HpicfDot1xAuthSessionTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,5,1,8),_HpicfDot1xAuthSessionTime_Type())
hpicfDot1xAuthSessionTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthSessionTime.setStatus(_B)
_HpicfDot1xAuthSessionStartTime_Type=TimeStamp
_HpicfDot1xAuthSessionStartTime_Object=MibTableColumn
hpicfDot1xAuthSessionStartTime=_HpicfDot1xAuthSessionStartTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,5,1,9),_HpicfDot1xAuthSessionStartTime_Type())
hpicfDot1xAuthSessionStartTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthSessionStartTime.setStatus(_B)
_HpicfDot1xAuthSessionStopTime_Type=TimeStamp
_HpicfDot1xAuthSessionStopTime_Object=MibTableColumn
hpicfDot1xAuthSessionStopTime=_HpicfDot1xAuthSessionStopTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,5,1,10),_HpicfDot1xAuthSessionStopTime_Type())
hpicfDot1xAuthSessionStopTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthSessionStopTime.setStatus(_B)
_HpicfDot1xAuthSessionInactiveTime_Type=TimeTicks
_HpicfDot1xAuthSessionInactiveTime_Object=MibTableColumn
hpicfDot1xAuthSessionInactiveTime=_HpicfDot1xAuthSessionInactiveTime_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,5,1,11),_HpicfDot1xAuthSessionInactiveTime_Type())
hpicfDot1xAuthSessionInactiveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthSessionInactiveTime.setStatus(_B)
class _HpicfDot1xAuthSessionTerminateCause_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,999)));namedValues=NamedValues(*(('supplicantLogoff',1),('portFailure',2),('supplicantRestart',3),('reauthFailed',4),('authControlForceUnauth',5),('portReInit',6),('portAdminDisabled',7),('notTerminatedYet',999)))
_HpicfDot1xAuthSessionTerminateCause_Type.__name__=_R
_HpicfDot1xAuthSessionTerminateCause_Object=MibTableColumn
hpicfDot1xAuthSessionTerminateCause=_HpicfDot1xAuthSessionTerminateCause_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,5,1,12),_HpicfDot1xAuthSessionTerminateCause_Type())
hpicfDot1xAuthSessionTerminateCause.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthSessionTerminateCause.setStatus(_B)
_HpicfDot1xAuthSessionUserName_Type=SnmpAdminString
_HpicfDot1xAuthSessionUserName_Object=MibTableColumn
hpicfDot1xAuthSessionUserName=_HpicfDot1xAuthSessionUserName_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,5,1,13),_HpicfDot1xAuthSessionUserName_Type())
hpicfDot1xAuthSessionUserName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthSessionUserName.setStatus(_B)
_HpicfDot1xAuthSessionIsForwarding_Type=TruthValue
_HpicfDot1xAuthSessionIsForwarding_Object=MibTableColumn
hpicfDot1xAuthSessionIsForwarding=_HpicfDot1xAuthSessionIsForwarding_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,5,1,14),_HpicfDot1xAuthSessionIsForwarding_Type())
hpicfDot1xAuthSessionIsForwarding.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthSessionIsForwarding.setStatus(_B)
_HpicfDot1xAuthSessionVid_Type=VlanIndex
_HpicfDot1xAuthSessionVid_Object=MibTableColumn
hpicfDot1xAuthSessionVid=_HpicfDot1xAuthSessionVid_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,5,1,15),_HpicfDot1xAuthSessionVid_Type())
hpicfDot1xAuthSessionVid.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthSessionVid.setStatus(_B)
_HpicfDot1xAuthSessionRoleName_Type=HpAutzUserRoleName
_HpicfDot1xAuthSessionRoleName_Object=MibTableColumn
hpicfDot1xAuthSessionRoleName=_HpicfDot1xAuthSessionRoleName_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,5,1,16),_HpicfDot1xAuthSessionRoleName_Type())
hpicfDot1xAuthSessionRoleName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpicfDot1xAuthSessionRoleName.setStatus(_B)
_HpicfDot1xAuthAllowGvrpVlans_Type=TruthValue
_HpicfDot1xAuthAllowGvrpVlans_Object=MibScalar
hpicfDot1xAuthAllowGvrpVlans=_HpicfDot1xAuthAllowGvrpVlans_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,6),_HpicfDot1xAuthAllowGvrpVlans_Type())
hpicfDot1xAuthAllowGvrpVlans.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xAuthAllowGvrpVlans.setStatus(_B)
class _HpicfDot1xAuthCachedReauthDelay_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpicfDot1xAuthCachedReauthDelay_Type.__name__=_I
_HpicfDot1xAuthCachedReauthDelay_Object=MibScalar
hpicfDot1xAuthCachedReauthDelay=_HpicfDot1xAuthCachedReauthDelay_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,7),_HpicfDot1xAuthCachedReauthDelay_Type())
hpicfDot1xAuthCachedReauthDelay.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xAuthCachedReauthDelay.setStatus(_B)
if mibBuilder.loadTexts:hpicfDot1xAuthCachedReauthDelay.setUnits(_W)
class _HpicfDot1xAuthEapTlsFragmentSize_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(576,3072))
_HpicfDot1xAuthEapTlsFragmentSize_Type.__name__=_I
_HpicfDot1xAuthEapTlsFragmentSize_Object=MibScalar
hpicfDot1xAuthEapTlsFragmentSize=_HpicfDot1xAuthEapTlsFragmentSize_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,2,10),_HpicfDot1xAuthEapTlsFragmentSize_Type())
hpicfDot1xAuthEapTlsFragmentSize.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xAuthEapTlsFragmentSize.setStatus(_B)
_HpicfDot1xSupplicant_ObjectIdentity=ObjectIdentity
hpicfDot1xSupplicant=_HpicfDot1xSupplicant_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,25,1,3))
_HpicfDot1xSuppConfigTable_Object=MibTable
hpicfDot1xSuppConfigTable=_HpicfDot1xSuppConfigTable_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,3,1))
if mibBuilder.loadTexts:hpicfDot1xSuppConfigTable.setStatus(_B)
_HpicfDot1xSuppConfigEntry_Object=MibTableRow
hpicfDot1xSuppConfigEntry=_HpicfDot1xSuppConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,3,1,1))
if mibBuilder.loadTexts:hpicfDot1xSuppConfigEntry.setStatus(_B)
class _HpicfDot1xSuppConfigIdentity_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpicfDot1xSuppConfigIdentity_Type.__name__=_S
_HpicfDot1xSuppConfigIdentity_Object=MibTableColumn
hpicfDot1xSuppConfigIdentity=_HpicfDot1xSuppConfigIdentity_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,3,1,1,1),_HpicfDot1xSuppConfigIdentity_Type())
hpicfDot1xSuppConfigIdentity.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xSuppConfigIdentity.setStatus(_B)
class _HpicfDot1xSuppConfigPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpicfDot1xSuppConfigPassword_Type.__name__=_S
_HpicfDot1xSuppConfigPassword_Object=MibTableColumn
hpicfDot1xSuppConfigPassword=_HpicfDot1xSuppConfigPassword_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,3,1,1,2),_HpicfDot1xSuppConfigPassword_Type())
hpicfDot1xSuppConfigPassword.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xSuppConfigPassword.setStatus(_B)
class _HpicfDot1xSuppConfigPasswordEncrypted_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_HpicfDot1xSuppConfigPasswordEncrypted_Type.__name__=_t
_HpicfDot1xSuppConfigPasswordEncrypted_Object=MibTableColumn
hpicfDot1xSuppConfigPasswordEncrypted=_HpicfDot1xSuppConfigPasswordEncrypted_Object((1,3,6,1,4,1,11,2,14,11,5,1,25,1,3,1,1,3),_HpicfDot1xSuppConfigPasswordEncrypted_Type())
hpicfDot1xSuppConfigPasswordEncrypted.setMaxAccess(_D)
if mibBuilder.loadTexts:hpicfDot1xSuppConfigPasswordEncrypted.setStatus(_B)
_HpicfDot1xConformance_ObjectIdentity=ObjectIdentity
hpicfDot1xConformance=_HpicfDot1xConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,25,2))
_HpicfDot1xGroups_ObjectIdentity=ObjectIdentity
hpicfDot1xGroups=_HpicfDot1xGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,25,2,1))
_HpicfDot1xCompliances_ObjectIdentity=ObjectIdentity
hpicfDot1xCompliances=_HpicfDot1xCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,5,1,25,2,2))
dot1xPaePortEntry.registerAugmentions((_A,_x))
hpicfDot1xPaePortEntry.setIndexNames(*dot1xPaePortEntry.getIndexNames())
dot1xAuthConfigEntry.registerAugmentions((_A,_y))
hpicfDot1xAuthConfigEntry.setIndexNames(*dot1xAuthConfigEntry.getIndexNames())
dot1xSuppConfigEntry.registerAugmentions((_A,_z))
hpicfDot1xSuppConfigEntry.setIndexNames(*dot1xSuppConfigEntry.getIndexNames())
hpicfDot1xPaePortGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,25,2,1,1))
hpicfDot1xPaePortGroup.setObjects(*((_A,_A0),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:hpicfDot1xPaePortGroup.setStatus(_B)
hpicfDot1xAuthConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,25,2,1,2))
hpicfDot1xAuthConfigGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_A3),(_A,_N)))
if mibBuilder.loadTexts:hpicfDot1xAuthConfigGroup.setStatus(_E)
hpicfDot1xSMAuthConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,25,2,1,3))
hpicfDot1xSMAuthConfigGroup.setObjects(*((_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:hpicfDot1xSMAuthConfigGroup.setStatus(_B)
hpicfDot1xAuthDiagGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,25,2,1,4))
hpicfDot1xAuthDiagGroup.setObjects(*((_A,_AA),(_A,_AB)))
if mibBuilder.loadTexts:hpicfDot1xAuthDiagGroup.setStatus(_B)
hpicfDot1xAuthStatsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,25,2,1,5))
hpicfDot1xAuthStatsGroup.setObjects(*((_A,_AC),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN)))
if mibBuilder.loadTexts:hpicfDot1xAuthStatsGroup.setStatus(_B)
hpicfDot1xAuthSessionStatsGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,25,2,1,6))
hpicfDot1xAuthSessionStatsGroup.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m)))
if mibBuilder.loadTexts:hpicfDot1xAuthSessionStatsGroup.setStatus(_E)
hpicfDot1xAuthConfigGroup2=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,25,2,1,7))
hpicfDot1xAuthConfigGroup2.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O)))
if mibBuilder.loadTexts:hpicfDot1xAuthConfigGroup2.setStatus(_B)
hpicfDot1xAuthConfigGroup3=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,25,2,1,8))
hpicfDot1xAuthConfigGroup3.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_Q)))
if mibBuilder.loadTexts:hpicfDot1xAuthConfigGroup3.setStatus(_B)
hpicfDot1xAuthConfigGroup4=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,25,2,1,9))
hpicfDot1xAuthConfigGroup4.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_Q),(_A,_U)))
if mibBuilder.loadTexts:hpicfDot1xAuthConfigGroup4.setStatus(_E)
hpicfDot1xAuthConfigGroup5=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,25,2,1,10))
hpicfDot1xAuthConfigGroup5.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_Q),(_A,_U),(_A,_X)))
if mibBuilder.loadTexts:hpicfDot1xAuthConfigGroup5.setStatus(_E)
hpicfDot1xSuppConfigGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,25,2,1,11))
hpicfDot1xSuppConfigGroup.setObjects(*((_A,_AO),(_A,_AP),(_A,_AQ)))
if mibBuilder.loadTexts:hpicfDot1xSuppConfigGroup.setStatus(_B)
hpicfDot1xPaeAuthSessionGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,25,2,1,12))
hpicfDot1xPaeAuthSessionGroup.setObjects(*((_A,_T),(_A,_n),(_A,_o)))
if mibBuilder.loadTexts:hpicfDot1xPaeAuthSessionGroup.setStatus(_E)
hpicfDot1xSMAuthSessionTimeoutGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,25,2,1,13))
hpicfDot1xSMAuthSessionTimeoutGroup.setObjects((_A,_AR))
if mibBuilder.loadTexts:hpicfDot1xSMAuthSessionTimeoutGroup.setStatus(_B)
hpicfDot1xPaeAuthSessionGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,25,2,1,14))
hpicfDot1xPaeAuthSessionGroup1.setObjects(*((_A,_T),(_A,_n),(_A,_AS),(_A,_o)))
if mibBuilder.loadTexts:hpicfDot1xPaeAuthSessionGroup1.setStatus(_B)
hpicfDot1xAuthSessionStatsGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,25,2,1,18))
hpicfDot1xAuthSessionStatsGroup1.setObjects(*((_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_AT)))
if mibBuilder.loadTexts:hpicfDot1xAuthSessionStatsGroup1.setStatus(_B)
hpicfDot1xSystemGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,25,2,1,19))
hpicfDot1xSystemGroup.setObjects((_A,_AU))
if mibBuilder.loadTexts:hpicfDot1xSystemGroup.setStatus(_B)
hpicfDot1xPaePortGroup1=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,25,2,1,20))
hpicfDot1xPaePortGroup1.setObjects(*((_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab)))
if mibBuilder.loadTexts:hpicfDot1xPaePortGroup1.setStatus(_B)
hpicfDot1xPaePortEapRetriesGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,25,2,1,22))
hpicfDot1xPaePortEapRetriesGroup.setObjects((_A,_Ac))
if mibBuilder.loadTexts:hpicfDot1xPaePortEapRetriesGroup.setStatus(_B)
hpicfDot1xAuthConfigGroup7=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,25,2,1,23))
hpicfDot1xAuthConfigGroup7.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_Q),(_A,_U),(_A,_X)))
if mibBuilder.loadTexts:hpicfDot1xAuthConfigGroup7.setStatus(_E)
hpicfDot1xAuthConfigGroup8=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,25,2,1,24))
hpicfDot1xAuthConfigGroup8.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_Q),(_A,_U),(_A,_X),(_A,_p),(_A,_q)))
if mibBuilder.loadTexts:hpicfDot1xAuthConfigGroup8.setStatus(_E)
hpicfDot1xAuthConfigGroup10=ObjectGroup((1,3,6,1,4,1,11,2,14,11,5,1,25,2,1,26))
hpicfDot1xAuthConfigGroup10.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_Q),(_A,_U),(_A,_X),(_A,_p),(_A,_q),(_A,_Ad)))
if mibBuilder.loadTexts:hpicfDot1xAuthConfigGroup10.setStatus(_B)
hpicfDot1xCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,25,2,2,1))
hpicfDot1xCompliance.setObjects(*((_A,_F),(_A,_Ae),(_A,_G),(_A,_H),(_A,_J)))
if mibBuilder.loadTexts:hpicfDot1xCompliance.setStatus(_E)
hpicfDot1xCompliance2=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,25,2,2,2))
hpicfDot1xCompliance2.setObjects(*((_A,_F),(_A,_Af),(_A,_G),(_A,_H),(_A,_J)))
if mibBuilder.loadTexts:hpicfDot1xCompliance2.setStatus(_E)
hpicfDot1xCompliance3=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,25,2,2,3))
hpicfDot1xCompliance3.setObjects(*((_A,_F),(_A,_Ag),(_A,_G),(_A,_H),(_A,_J)))
if mibBuilder.loadTexts:hpicfDot1xCompliance3.setStatus(_E)
hpicfDot1xCompliance4=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,25,2,2,4))
hpicfDot1xCompliance4.setObjects(*((_A,_F),(_A,_Ah),(_A,_G),(_A,_H),(_A,_J)))
if mibBuilder.loadTexts:hpicfDot1xCompliance4.setStatus(_E)
hpicfDot1xCompliance5=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,25,2,2,5))
hpicfDot1xCompliance5.setObjects(*((_A,_F),(_A,_r),(_A,_G),(_A,_H),(_A,_J)))
if mibBuilder.loadTexts:hpicfDot1xCompliance5.setStatus(_E)
hpicfDot1xCompliance6=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,25,2,2,6))
hpicfDot1xCompliance6.setObjects(*((_A,_F),(_A,_r),(_A,_G),(_A,_H),(_A,_J),(_A,_V)))
if mibBuilder.loadTexts:hpicfDot1xCompliance6.setStatus(_B)
hpicfDot1xCompliance7=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,25,2,2,7))
hpicfDot1xCompliance7.setObjects(*((_A,_s),(_A,_Ai)))
if mibBuilder.loadTexts:hpicfDot1xCompliance7.setStatus(_E)
hpicfDot1xCompliance8=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,25,2,2,8))
hpicfDot1xCompliance8.setObjects((_A,_Aj))
if mibBuilder.loadTexts:hpicfDot1xCompliance8.setStatus(_B)
hpicfDot1xCompliance9=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,25,2,2,9))
hpicfDot1xCompliance9.setObjects(*((_A,_s),(_A,_Ak)))
if mibBuilder.loadTexts:hpicfDot1xCompliance9.setStatus(_B)
hpicfDot1xCompliance11=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,25,2,2,11))
hpicfDot1xCompliance11.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_Al)))
if mibBuilder.loadTexts:hpicfDot1xCompliance11.setStatus(_E)
hpicfDot1xCompliance12=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,25,2,2,12))
hpicfDot1xCompliance12.setObjects((_A,_Am))
if mibBuilder.loadTexts:hpicfDot1xCompliance12.setStatus(_B)
hpicfDot1xCompliance13=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,25,2,2,13))
hpicfDot1xCompliance13.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_J),(_A,_V)))
if mibBuilder.loadTexts:hpicfDot1xCompliance13.setStatus(_E)
hpicfDot1xCompliance14=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,25,2,2,14))
hpicfDot1xCompliance14.setObjects((_A,_An))
if mibBuilder.loadTexts:hpicfDot1xCompliance14.setStatus(_B)
hpicfDot1xCompliance15=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,25,2,2,15))
hpicfDot1xCompliance15.setObjects((_A,_Ao))
if mibBuilder.loadTexts:hpicfDot1xCompliance15.setStatus(_B)
hpicfDot1xCompliance16=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,25,2,2,16))
hpicfDot1xCompliance16.setObjects(*((_A,_F),(_A,_Ap),(_A,_G),(_A,_H),(_A,_J),(_A,_V)))
if mibBuilder.loadTexts:hpicfDot1xCompliance16.setStatus(_E)
hpicfDot1xCompliance17=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,25,2,2,17))
hpicfDot1xCompliance17.setObjects(*((_A,_F),(_A,_Aq),(_A,_G),(_A,_H),(_A,_J),(_A,_V)))
if mibBuilder.loadTexts:hpicfDot1xCompliance17.setStatus(_E)
hpicfDot1xCompliance19=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,5,1,25,2,2,19))
hpicfDot1xCompliance19.setObjects(*((_A,_F),(_A,_Ar),(_A,_G),(_A,_H),(_A,_J),(_A,_V)))
if mibBuilder.loadTexts:hpicfDot1xCompliance19.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'hpicfDot1xMIB':hpicfDot1xMIB,'hpicfDot1xMIBObjects':hpicfDot1xMIBObjects,'hpicfDot1xSystem':hpicfDot1xSystem,'hpicfDot1xPaePortTable':hpicfDot1xPaePortTable,_x:hpicfDot1xPaePortEntry,_A0:hpicfDot1xPaePortAuth,_A1:hpicfDot1xPaePortSupp,_n:hpicfDot1xPaePortMixed,_AS:hpicfDot1xPaePortSpeedVSA,_A2:hpicfDot1xPaePortMBV,_AV:hpicfDot1xPaePortCritAuthVoiceVid,_AW:hpicfDot1xPaePortCritAuthDataVid,_AX:hpicfDot1xPaePortCritAuthUserRole,_AY:hpicfDot1xPaePortOpenAuthVoiceVid,_AZ:hpicfDot1xPaePortOpenAuthDataVid,_Aa:hpicfDot1xPaePortOpenAuthUserRole,_Ab:hpicfDot1xPaePortInitialRole,_AU:hpicfDot1x2010,'hpicfDot1xAuthenticator':hpicfDot1xAuthenticator,'hpicfDot1xAuthConfigTable':hpicfDot1xAuthConfigTable,_y:hpicfDot1xAuthConfigEntry,_K:hpicfDot1xAuthAuthVid,_L:hpicfDot1xAuthUnauthVid,_M:hpicfDot1xAuthUnauthPeriod,_A3:hpicfDot1xAuthClientLimit,_N:hpicfDot1xAuthLogoffPeriod,_O:hpicfDot1xAuthClientLimit2,_U:hpicfDot1xAuthCachedReauthPeriod,_p:hpicfDot1xAuthEnforceCacheReauth,_Ac:hpicfAuthMaxEapReq,_q:hpicfDot1xAuthUnauthVidLLDPNwkPolicy,'hpicfDot1xSMAuthConfigTable':hpicfDot1xSMAuthConfigTable,'hpicfDot1xSMAuthConfigEntry':hpicfDot1xSMAuthConfigEntry,_Y:hpicfDot1xSMAuthPaePort,_T:hpicfDot1xSMAuthMacAddr,_A4:hpicfDot1xSMAuthInitialize,_A5:hpicfDot1xSMAuthReauthenticate,_A6:hpicfDot1xSMAuthPaeState,_A7:hpicfDot1xSMAuthBackendAuthState,_A8:hpicfDot1xSMAuthReAuthPeriod,_A9:hpicfDot1xSMAuthReAuthEnabled,_AR:hpicfDot1xSMAuthSessionTimeout,'hpicfDot1xAuthDiagTable':hpicfDot1xAuthDiagTable,'hpicfDot1xAuthDiagEntry':hpicfDot1xAuthDiagEntry,_AA:hpicfDot1xAuthNumberOfSuccessAuthentication,_AB:hpicfDot1xAuthNumberOfFailedAuthentication,'hpicfDot1xAuthStatsTable':hpicfDot1xAuthStatsTable,'hpicfDot1xAuthStatsEntry':hpicfDot1xAuthStatsEntry,_AC:hpicfDot1xAuthEapolFramesRx,_AD:hpicfDot1xAuthEapolFramesTx,_AE:hpicfDot1xAuthEapolStartFramesRx,_AF:hpicfDot1xAuthEapolLogoffFramesRx,_AG:hpicfDot1xAuthEapolRespIdFramesRx,_AH:hpicfDot1xAuthEapolRespFramesRx,_AI:hpicfDot1xAuthEapolReqIdFramesTx,_AJ:hpicfDot1xAuthEapolReqFramesTx,_AK:hpicfDot1xAuthInvalidEapolFramesRx,_AL:hpicfDot1xAuthEapLengthErrorFramesRx,_AM:hpicfDot1xAuthLastEapolFrameVersion,_AN:hpicfDot1xAuthLastEapolFrameSource,'hpicfDot1xAuthSessionStatsTable':hpicfDot1xAuthSessionStatsTable,'hpicfDot1xAuthSessionStatsEntry':hpicfDot1xAuthSessionStatsEntry,_o:hpicfDot1xAuthSessionPerPAECountersEnabled,_Z:hpicfDot1xAuthSessionOctetsRx,_a:hpicfDot1xAuthSessionOctetsTx,_b:hpicfDot1xAuthSessionFramesRx,_c:hpicfDot1xAuthSessionFramesTx,_d:hpicfDot1xAuthSessionId,_e:hpicfDot1xAuthSessionAuthenticMethod,_f:hpicfDot1xAuthSessionTime,_g:hpicfDot1xAuthSessionStartTime,_h:hpicfDot1xAuthSessionStopTime,_i:hpicfDot1xAuthSessionInactiveTime,_j:hpicfDot1xAuthSessionTerminateCause,_k:hpicfDot1xAuthSessionUserName,_l:hpicfDot1xAuthSessionIsForwarding,_m:hpicfDot1xAuthSessionVid,_AT:hpicfDot1xAuthSessionRoleName,_Q:hpicfDot1xAuthAllowGvrpVlans,_X:hpicfDot1xAuthCachedReauthDelay,_Ad:hpicfDot1xAuthEapTlsFragmentSize,'hpicfDot1xSupplicant':hpicfDot1xSupplicant,'hpicfDot1xSuppConfigTable':hpicfDot1xSuppConfigTable,_z:hpicfDot1xSuppConfigEntry,_AO:hpicfDot1xSuppConfigIdentity,_AP:hpicfDot1xSuppConfigPassword,_AQ:hpicfDot1xSuppConfigPasswordEncrypted,'hpicfDot1xConformance':hpicfDot1xConformance,'hpicfDot1xGroups':hpicfDot1xGroups,_F:hpicfDot1xPaePortGroup,_Ae:hpicfDot1xAuthConfigGroup,_G:hpicfDot1xSMAuthConfigGroup,_s:hpicfDot1xAuthDiagGroup,_H:hpicfDot1xAuthStatsGroup,_J:hpicfDot1xAuthSessionStatsGroup,_Af:hpicfDot1xAuthConfigGroup2,_Ag:hpicfDot1xAuthConfigGroup3,_Ah:hpicfDot1xAuthConfigGroup4,_r:hpicfDot1xAuthConfigGroup5,_V:hpicfDot1xSuppConfigGroup,_Ai:hpicfDot1xPaeAuthSessionGroup,_Aj:hpicfDot1xSMAuthSessionTimeoutGroup,_Ak:hpicfDot1xPaeAuthSessionGroup1,_Al:hpicfDot1xAuthSessionStatsGroup1,_Am:hpicfDot1xSystemGroup,_An:hpicfDot1xPaePortGroup1,_Ao:hpicfDot1xPaePortEapRetriesGroup,_Ap:hpicfDot1xAuthConfigGroup7,_Aq:hpicfDot1xAuthConfigGroup8,_Ar:hpicfDot1xAuthConfigGroup10,'hpicfDot1xCompliances':hpicfDot1xCompliances,'hpicfDot1xCompliance':hpicfDot1xCompliance,'hpicfDot1xCompliance2':hpicfDot1xCompliance2,'hpicfDot1xCompliance3':hpicfDot1xCompliance3,'hpicfDot1xCompliance4':hpicfDot1xCompliance4,'hpicfDot1xCompliance5':hpicfDot1xCompliance5,'hpicfDot1xCompliance6':hpicfDot1xCompliance6,'hpicfDot1xCompliance7':hpicfDot1xCompliance7,'hpicfDot1xCompliance8':hpicfDot1xCompliance8,'hpicfDot1xCompliance9':hpicfDot1xCompliance9,'hpicfDot1xCompliance11':hpicfDot1xCompliance11,'hpicfDot1xCompliance12':hpicfDot1xCompliance12,'hpicfDot1xCompliance13':hpicfDot1xCompliance13,'hpicfDot1xCompliance14':hpicfDot1xCompliance14,'hpicfDot1xCompliance15':hpicfDot1xCompliance15,'hpicfDot1xCompliance16':hpicfDot1xCompliance16,'hpicfDot1xCompliance17':hpicfDot1xCompliance17,'hpicfDot1xCompliance19':hpicfDot1xCompliance19})