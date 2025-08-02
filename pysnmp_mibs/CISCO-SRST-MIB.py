_Al='csrstConfGroupRev1'
_Ak='csrstConfGroup'
_Aj='csrstConferenceFailed'
_Ai='csrstSipPhoneRegFailed'
_Ah='csrstSipPhoneUnRegThresholdExceed'
_Ag='csrstFailNotif'
_Af='csrstStateChange'
_Ae='csrstUserLocaleInfoRev1'
_Ad='csrstSipEndpointDN'
_Ac='csrstSipEndpointIpAddrType'
_Ab='csrstSipVoRegPoolEdptTag'
_Aa='csrstSipVoRegNumberHuntstopEnabled'
_AZ='csrstSipVoRegNumberPref'
_AY='csrstSipVoRegNumberPattern'
_AX='csrstSipVoRegNumberListTag'
_AW='csrstSipVoRegPoolAppl'
_AV='csrstSipDefaultPreference'
_AU='csrstSipProxySrvAltIpAddr'
_AT='csrstSipProxySrvMonitor'
_AS='csrstSipProxySrvPref'
_AR='csrstSipProxySrvIpAddr'
_AQ='csrstSipNetMask'
_AP='csrstSipVoRegPoolIpAddrType'
_AO='csrstSipNetId'
_AN='csrstSipSend300MultSupport'
_AM='csrstSipIp2IpGlobalEnabled'
_AL='csrstSipRegSrvExpMin'
_AK='csrstSipRegSrvExpMax'
_AJ='csrstTotalUpTime'
_AI='csrstSipCallLegs'
_AH='csrstUserLocaleInfo'
_AG='accessible-for-notify'
_AF='csrstSipEndpointTag'
_AE='csrstSipVoRegNumberListIndex'
_AD='csrstAliasIndex'
_AC='read-write'
_AB='DisplayString'
_AA='CountryCode'
_A9='csrstMIBNotifsGroup'
_A8='csrstActiveStatsGroup'
_A7='csrstSipConfGroup'
_A6='csrstNotifInfoGroup'
_A5='csrstSipEndpointIpAddress'
_A4='csrstSipPhoneCurrentRegistered'
_A3='csrstState'
_A2='csrstNotificationEnabled'
_A1='csrstLimitDN'
_A0='csrstAccessCodeDIDEnabled'
_z='csrstAccessCode'
_y='csrstAliasHuntStopEnabled'
_x='csrstAliasPreference'
_w='csrstAliasAltNumber'
_v='csrstAliasNumPattern'
_u='csrstAliasTag'
_t='csrstXlateCallingNumber'
_s='csrstXlateCalledNumber'
_r='csrstAlertTo'
_q='csrstBusyTo'
_p='csrstInterdigitTo'
_o='csrstTimeFormat'
_n='csrstDateFormat'
_m='csrstTransferSystem'
_l='csrstSecondaryDialTone'
_k='csrstScriptName'
_j='csrstSystemMessageSecondary'
_i='csrstSystemMessagePrimary'
_h='csrstVoiceMailNumber'
_g='csrstMohMulticastPort'
_f='csrstMohMulticastAddr'
_e='csrstMohMulticastAddrType'
_d='csrstMohFilename'
_c='csrstCallFwdBusy'
_b='csrstCallFwdNoAnswerTo'
_a='csrstCallFwdNoAnswer'
_Z='csrstMaxDN'
_Y='csrstMaxEphones'
_X='csrstPortNumber'
_W='csrstIPAddress'
_V='csrstIPAddressType'
_U='csrstVersion'
_T='csrstEnabled'
_S='csrstSipVoRegPoolTag'
_R='deprecated'
_Q='TruthValue'
_P='InetPortNumber'
_O='csrstSysNotifReason'
_N='csrstSysNotifSeverity'
_M='csrstSipPhoneUnRegThreshold'
_L='csrstMaxConferences'
_K='csrstLimitDNType'
_J='csrstAccessCodeType'
_I='not-accessible'
_H='seconds'
_G='CvE164Address'
_F='Unsigned32'
_E='Integer32'
_D='SnmpAdminString'
_C='read-only'
_B='current'
_A='CISCO-SRST-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
CountryCode,CvE164Address=mibBuilder.importSymbols('CISCO-TC',_AA,_G)
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType',_P)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_AB,'PhysAddress','TextualConvention',_Q)
ciscoSrstMIB=ModuleIdentity((1,3,6,1,4,1,9,9,441))
if mibBuilder.loadTexts:ciscoSrstMIB.setRevisions(('2007-02-27 00:00','2005-06-20 00:00'))
class SrstOperType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('inactive',2)))
_CiscoSrstMIBNotifications_ObjectIdentity=ObjectIdentity
ciscoSrstMIBNotifications=_CiscoSrstMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,441,0))
_CiscoSrstMIBObjects_ObjectIdentity=ObjectIdentity
ciscoSrstMIBObjects=_CiscoSrstMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,441,1))
_CsrstGlobal_ObjectIdentity=ObjectIdentity
csrstGlobal=_CsrstGlobal_ObjectIdentity((1,3,6,1,4,1,9,9,441,1,1))
_CsrstConf_ObjectIdentity=ObjectIdentity
csrstConf=_CsrstConf_ObjectIdentity((1,3,6,1,4,1,9,9,441,1,2))
_CsrstEnabled_Type=TruthValue
_CsrstEnabled_Object=MibScalar
csrstEnabled=_CsrstEnabled_Object((1,3,6,1,4,1,9,9,441,1,2,1),_CsrstEnabled_Type())
csrstEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstEnabled.setStatus(_B)
class _CsrstVersion_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CsrstVersion_Type.__name__=_D
_CsrstVersion_Object=MibScalar
csrstVersion=_CsrstVersion_Object((1,3,6,1,4,1,9,9,441,1,2,2),_CsrstVersion_Type())
csrstVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstVersion.setStatus(_B)
_CsrstIPAddressType_Type=InetAddressType
_CsrstIPAddressType_Object=MibScalar
csrstIPAddressType=_CsrstIPAddressType_Object((1,3,6,1,4,1,9,9,441,1,2,3),_CsrstIPAddressType_Type())
csrstIPAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstIPAddressType.setStatus(_B)
_CsrstIPAddress_Type=InetAddress
_CsrstIPAddress_Object=MibScalar
csrstIPAddress=_CsrstIPAddress_Object((1,3,6,1,4,1,9,9,441,1,2,4),_CsrstIPAddress_Type())
csrstIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstIPAddress.setStatus(_B)
class _CsrstPortNumber_Type(InetPortNumber):defaultValue=2000;subtypeSpec=InetPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2000,9999))
_CsrstPortNumber_Type.__name__=_P
_CsrstPortNumber_Object=MibScalar
csrstPortNumber=_CsrstPortNumber_Object((1,3,6,1,4,1,9,9,441,1,2,5),_CsrstPortNumber_Type())
csrstPortNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstPortNumber.setStatus(_B)
_CsrstMaxConferences_Type=Unsigned32
_CsrstMaxConferences_Object=MibScalar
csrstMaxConferences=_CsrstMaxConferences_Object((1,3,6,1,4,1,9,9,441,1,2,6),_CsrstMaxConferences_Type())
csrstMaxConferences.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstMaxConferences.setStatus(_B)
class _CsrstMaxEphones_Type(Unsigned32):defaultValue=0
_CsrstMaxEphones_Type.__name__=_F
_CsrstMaxEphones_Object=MibScalar
csrstMaxEphones=_CsrstMaxEphones_Object((1,3,6,1,4,1,9,9,441,1,2,7),_CsrstMaxEphones_Type())
csrstMaxEphones.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstMaxEphones.setStatus(_B)
class _CsrstMaxDN_Type(Unsigned32):defaultValue=0
_CsrstMaxDN_Type.__name__=_F
_CsrstMaxDN_Object=MibScalar
csrstMaxDN=_CsrstMaxDN_Object((1,3,6,1,4,1,9,9,441,1,2,8),_CsrstMaxDN_Type())
csrstMaxDN.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstMaxDN.setStatus(_B)
_CsrstSipPhoneUnRegThreshold_Type=Unsigned32
_CsrstSipPhoneUnRegThreshold_Object=MibScalar
csrstSipPhoneUnRegThreshold=_CsrstSipPhoneUnRegThreshold_Object((1,3,6,1,4,1,9,9,441,1,2,9),_CsrstSipPhoneUnRegThreshold_Type())
csrstSipPhoneUnRegThreshold.setMaxAccess(_AC)
if mibBuilder.loadTexts:csrstSipPhoneUnRegThreshold.setStatus(_B)
class _CsrstCallFwdNoAnswer_Type(CvE164Address):subtypeSpec=CvE164Address.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CsrstCallFwdNoAnswer_Type.__name__=_G
_CsrstCallFwdNoAnswer_Object=MibScalar
csrstCallFwdNoAnswer=_CsrstCallFwdNoAnswer_Object((1,3,6,1,4,1,9,9,441,1,2,10),_CsrstCallFwdNoAnswer_Type())
csrstCallFwdNoAnswer.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstCallFwdNoAnswer.setStatus(_B)
_CsrstCallFwdNoAnswerTo_Type=Unsigned32
_CsrstCallFwdNoAnswerTo_Object=MibScalar
csrstCallFwdNoAnswerTo=_CsrstCallFwdNoAnswerTo_Object((1,3,6,1,4,1,9,9,441,1,2,11),_CsrstCallFwdNoAnswerTo_Type())
csrstCallFwdNoAnswerTo.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstCallFwdNoAnswerTo.setStatus(_B)
if mibBuilder.loadTexts:csrstCallFwdNoAnswerTo.setUnits(_H)
class _CsrstCallFwdBusy_Type(CvE164Address):subtypeSpec=CvE164Address.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CsrstCallFwdBusy_Type.__name__=_G
_CsrstCallFwdBusy_Object=MibScalar
csrstCallFwdBusy=_CsrstCallFwdBusy_Object((1,3,6,1,4,1,9,9,441,1,2,12),_CsrstCallFwdBusy_Type())
csrstCallFwdBusy.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstCallFwdBusy.setStatus(_B)
class _CsrstMohFilename_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CsrstMohFilename_Type.__name__=_D
_CsrstMohFilename_Object=MibScalar
csrstMohFilename=_CsrstMohFilename_Object((1,3,6,1,4,1,9,9,441,1,2,13),_CsrstMohFilename_Type())
csrstMohFilename.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstMohFilename.setStatus(_B)
_CsrstMohMulticastAddrType_Type=InetAddressType
_CsrstMohMulticastAddrType_Object=MibScalar
csrstMohMulticastAddrType=_CsrstMohMulticastAddrType_Object((1,3,6,1,4,1,9,9,441,1,2,14),_CsrstMohMulticastAddrType_Type())
csrstMohMulticastAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstMohMulticastAddrType.setStatus(_B)
_CsrstMohMulticastAddr_Type=InetAddress
_CsrstMohMulticastAddr_Object=MibScalar
csrstMohMulticastAddr=_CsrstMohMulticastAddr_Object((1,3,6,1,4,1,9,9,441,1,2,15),_CsrstMohMulticastAddr_Type())
csrstMohMulticastAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstMohMulticastAddr.setStatus(_B)
class _CsrstMohMulticastPort_Type(InetPortNumber):defaultValue=2000;subtypeSpec=InetPortNumber.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2000,9999))
_CsrstMohMulticastPort_Type.__name__=_P
_CsrstMohMulticastPort_Object=MibScalar
csrstMohMulticastPort=_CsrstMohMulticastPort_Object((1,3,6,1,4,1,9,9,441,1,2,16),_CsrstMohMulticastPort_Type())
csrstMohMulticastPort.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstMohMulticastPort.setStatus(_B)
class _CsrstVoiceMailNumber_Type(CvE164Address):subtypeSpec=CvE164Address.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CsrstVoiceMailNumber_Type.__name__=_G
_CsrstVoiceMailNumber_Object=MibScalar
csrstVoiceMailNumber=_CsrstVoiceMailNumber_Object((1,3,6,1,4,1,9,9,441,1,2,17),_CsrstVoiceMailNumber_Type())
csrstVoiceMailNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstVoiceMailNumber.setStatus(_B)
class _CsrstSystemMessagePrimary_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CsrstSystemMessagePrimary_Type.__name__=_D
_CsrstSystemMessagePrimary_Object=MibScalar
csrstSystemMessagePrimary=_CsrstSystemMessagePrimary_Object((1,3,6,1,4,1,9,9,441,1,2,18),_CsrstSystemMessagePrimary_Type())
csrstSystemMessagePrimary.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSystemMessagePrimary.setStatus(_B)
class _CsrstSystemMessageSecondary_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_CsrstSystemMessageSecondary_Type.__name__=_D
_CsrstSystemMessageSecondary_Object=MibScalar
csrstSystemMessageSecondary=_CsrstSystemMessageSecondary_Object((1,3,6,1,4,1,9,9,441,1,2,19),_CsrstSystemMessageSecondary_Type())
csrstSystemMessageSecondary.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSystemMessageSecondary.setStatus(_B)
class _CsrstScriptName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CsrstScriptName_Type.__name__=_D
_CsrstScriptName_Object=MibScalar
csrstScriptName=_CsrstScriptName_Object((1,3,6,1,4,1,9,9,441,1,2,20),_CsrstScriptName_Type())
csrstScriptName.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstScriptName.setStatus(_B)
class _CsrstSecondaryDialTone_Type(CvE164Address):subtypeSpec=CvE164Address.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CsrstSecondaryDialTone_Type.__name__=_G
_CsrstSecondaryDialTone_Object=MibScalar
csrstSecondaryDialTone=_CsrstSecondaryDialTone_Object((1,3,6,1,4,1,9,9,441,1,2,21),_CsrstSecondaryDialTone_Type())
csrstSecondaryDialTone.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSecondaryDialTone.setStatus(_B)
class _CsrstTransferSystem_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('blind',1),('fullBlind',2),('fullConsult',3),('localConsult',4)))
_CsrstTransferSystem_Type.__name__=_E
_CsrstTransferSystem_Object=MibScalar
csrstTransferSystem=_CsrstTransferSystem_Object((1,3,6,1,4,1,9,9,441,1,2,22),_CsrstTransferSystem_Type())
csrstTransferSystem.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstTransferSystem.setStatus(_B)
class _CsrstUserLocaleInfo_Type(CountryCode):defaultValue=OctetString('US')
_CsrstUserLocaleInfo_Type.__name__=_AA
_CsrstUserLocaleInfo_Object=MibScalar
csrstUserLocaleInfo=_CsrstUserLocaleInfo_Object((1,3,6,1,4,1,9,9,441,1,2,23),_CsrstUserLocaleInfo_Type())
csrstUserLocaleInfo.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstUserLocaleInfo.setStatus(_R)
class _CsrstDateFormat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('mmddyy',1),('ddmmyy',2),('yyddmm',3),('yymmdd',4)))
_CsrstDateFormat_Type.__name__=_E
_CsrstDateFormat_Object=MibScalar
csrstDateFormat=_CsrstDateFormat_Object((1,3,6,1,4,1,9,9,441,1,2,24),_CsrstDateFormat_Type())
csrstDateFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstDateFormat.setStatus(_B)
class _CsrstTimeFormat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('twelveHour',1),('twentyFourHour',2)))
_CsrstTimeFormat_Type.__name__=_E
_CsrstTimeFormat_Object=MibScalar
csrstTimeFormat=_CsrstTimeFormat_Object((1,3,6,1,4,1,9,9,441,1,2,25),_CsrstTimeFormat_Type())
csrstTimeFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstTimeFormat.setStatus(_B)
class _CsrstInterdigitTo_Type(Unsigned32):defaultValue=10
_CsrstInterdigitTo_Type.__name__=_F
_CsrstInterdigitTo_Object=MibScalar
csrstInterdigitTo=_CsrstInterdigitTo_Object((1,3,6,1,4,1,9,9,441,1,2,26),_CsrstInterdigitTo_Type())
csrstInterdigitTo.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstInterdigitTo.setStatus(_B)
if mibBuilder.loadTexts:csrstInterdigitTo.setUnits(_H)
class _CsrstBusyTo_Type(Unsigned32):defaultValue=10
_CsrstBusyTo_Type.__name__=_F
_CsrstBusyTo_Object=MibScalar
csrstBusyTo=_CsrstBusyTo_Object((1,3,6,1,4,1,9,9,441,1,2,27),_CsrstBusyTo_Type())
csrstBusyTo.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstBusyTo.setStatus(_B)
if mibBuilder.loadTexts:csrstBusyTo.setUnits(_H)
class _CsrstAlertTo_Type(Unsigned32):defaultValue=180
_CsrstAlertTo_Type.__name__=_F
_CsrstAlertTo_Object=MibScalar
csrstAlertTo=_CsrstAlertTo_Object((1,3,6,1,4,1,9,9,441,1,2,28),_CsrstAlertTo_Type())
csrstAlertTo.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstAlertTo.setStatus(_B)
if mibBuilder.loadTexts:csrstAlertTo.setUnits(_H)
_CsrstXlateCalledNumber_Type=Unsigned32
_CsrstXlateCalledNumber_Object=MibScalar
csrstXlateCalledNumber=_CsrstXlateCalledNumber_Object((1,3,6,1,4,1,9,9,441,1,2,29),_CsrstXlateCalledNumber_Type())
csrstXlateCalledNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstXlateCalledNumber.setStatus(_B)
_CsrstXlateCallingNumber_Type=Unsigned32
_CsrstXlateCallingNumber_Object=MibScalar
csrstXlateCallingNumber=_CsrstXlateCallingNumber_Object((1,3,6,1,4,1,9,9,441,1,2,30),_CsrstXlateCallingNumber_Type())
csrstXlateCallingNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstXlateCallingNumber.setStatus(_B)
_CsrstAliasTable_Object=MibTable
csrstAliasTable=_CsrstAliasTable_Object((1,3,6,1,4,1,9,9,441,1,2,31))
if mibBuilder.loadTexts:csrstAliasTable.setStatus(_B)
_CsrstAliasEntry_Object=MibTableRow
csrstAliasEntry=_CsrstAliasEntry_Object((1,3,6,1,4,1,9,9,441,1,2,31,1))
csrstAliasEntry.setIndexNames((0,_A,_AD))
if mibBuilder.loadTexts:csrstAliasEntry.setStatus(_B)
_CsrstAliasIndex_Type=Unsigned32
_CsrstAliasIndex_Object=MibTableColumn
csrstAliasIndex=_CsrstAliasIndex_Object((1,3,6,1,4,1,9,9,441,1,2,31,1,1),_CsrstAliasIndex_Type())
csrstAliasIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:csrstAliasIndex.setStatus(_B)
_CsrstAliasTag_Type=Unsigned32
_CsrstAliasTag_Object=MibTableColumn
csrstAliasTag=_CsrstAliasTag_Object((1,3,6,1,4,1,9,9,441,1,2,31,1,2),_CsrstAliasTag_Type())
csrstAliasTag.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstAliasTag.setStatus(_B)
class _CsrstAliasNumPattern_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CsrstAliasNumPattern_Type.__name__=_D
_CsrstAliasNumPattern_Object=MibTableColumn
csrstAliasNumPattern=_CsrstAliasNumPattern_Object((1,3,6,1,4,1,9,9,441,1,2,31,1,3),_CsrstAliasNumPattern_Type())
csrstAliasNumPattern.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstAliasNumPattern.setStatus(_B)
class _CsrstAliasAltNumber_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CsrstAliasAltNumber_Type.__name__=_D
_CsrstAliasAltNumber_Object=MibTableColumn
csrstAliasAltNumber=_CsrstAliasAltNumber_Object((1,3,6,1,4,1,9,9,441,1,2,31,1,4),_CsrstAliasAltNumber_Type())
csrstAliasAltNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstAliasAltNumber.setStatus(_B)
_CsrstAliasPreference_Type=Unsigned32
_CsrstAliasPreference_Object=MibTableColumn
csrstAliasPreference=_CsrstAliasPreference_Object((1,3,6,1,4,1,9,9,441,1,2,31,1,5),_CsrstAliasPreference_Type())
csrstAliasPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstAliasPreference.setStatus(_B)
_CsrstAliasHuntStopEnabled_Type=TruthValue
_CsrstAliasHuntStopEnabled_Object=MibTableColumn
csrstAliasHuntStopEnabled=_CsrstAliasHuntStopEnabled_Object((1,3,6,1,4,1,9,9,441,1,2,31,1,6),_CsrstAliasHuntStopEnabled_Type())
csrstAliasHuntStopEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstAliasHuntStopEnabled.setStatus(_B)
_CsrstAccessCodeTable_Object=MibTable
csrstAccessCodeTable=_CsrstAccessCodeTable_Object((1,3,6,1,4,1,9,9,441,1,2,32))
if mibBuilder.loadTexts:csrstAccessCodeTable.setStatus(_B)
_CsrstAccessCodeEntry_Object=MibTableRow
csrstAccessCodeEntry=_CsrstAccessCodeEntry_Object((1,3,6,1,4,1,9,9,441,1,2,32,1))
csrstAccessCodeEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:csrstAccessCodeEntry.setStatus(_B)
class _CsrstAccessCodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('fxo',1),('em',2),('bri',3),('pri',4)))
_CsrstAccessCodeType_Type.__name__=_E
_CsrstAccessCodeType_Object=MibTableColumn
csrstAccessCodeType=_CsrstAccessCodeType_Object((1,3,6,1,4,1,9,9,441,1,2,32,1,1),_CsrstAccessCodeType_Type())
csrstAccessCodeType.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstAccessCodeType.setStatus(_B)
class _CsrstAccessCode_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CsrstAccessCode_Type.__name__=_D
_CsrstAccessCode_Object=MibTableColumn
csrstAccessCode=_CsrstAccessCode_Object((1,3,6,1,4,1,9,9,441,1,2,32,1,2),_CsrstAccessCode_Type())
csrstAccessCode.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstAccessCode.setStatus(_B)
_CsrstAccessCodeDIDEnabled_Type=TruthValue
_CsrstAccessCodeDIDEnabled_Object=MibTableColumn
csrstAccessCodeDIDEnabled=_CsrstAccessCodeDIDEnabled_Object((1,3,6,1,4,1,9,9,441,1,2,32,1,3),_CsrstAccessCodeDIDEnabled_Type())
csrstAccessCodeDIDEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstAccessCodeDIDEnabled.setStatus(_B)
_CsrstLimitDNTable_Object=MibTable
csrstLimitDNTable=_CsrstLimitDNTable_Object((1,3,6,1,4,1,9,9,441,1,2,33))
if mibBuilder.loadTexts:csrstLimitDNTable.setStatus(_B)
_CsrstLimitDNEntry_Object=MibTableRow
csrstLimitDNEntry=_CsrstLimitDNEntry_Object((1,3,6,1,4,1,9,9,441,1,2,33,1))
csrstLimitDNEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:csrstLimitDNEntry.setStatus(_B)
class _CsrstLimitDNType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('ipPhone7910',1),('ipPhone7935',2),('ipPhone7940',3),('ipPhone7960',4),('ipPhone7970',5),('ipPhone7936',6)))
_CsrstLimitDNType_Type.__name__=_E
_CsrstLimitDNType_Object=MibTableColumn
csrstLimitDNType=_CsrstLimitDNType_Object((1,3,6,1,4,1,9,9,441,1,2,33,1,1),_CsrstLimitDNType_Type())
csrstLimitDNType.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstLimitDNType.setStatus(_B)
_CsrstLimitDN_Type=Unsigned32
_CsrstLimitDN_Object=MibTableColumn
csrstLimitDN=_CsrstLimitDN_Object((1,3,6,1,4,1,9,9,441,1,2,33,1,2),_CsrstLimitDN_Type())
csrstLimitDN.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstLimitDN.setStatus(_B)
class _CsrstNotificationEnabled_Type(TruthValue):defaultValue=2
_CsrstNotificationEnabled_Type.__name__=_Q
_CsrstNotificationEnabled_Object=MibScalar
csrstNotificationEnabled=_CsrstNotificationEnabled_Object((1,3,6,1,4,1,9,9,441,1,2,34),_CsrstNotificationEnabled_Type())
csrstNotificationEnabled.setMaxAccess(_AC)
if mibBuilder.loadTexts:csrstNotificationEnabled.setStatus(_B)
class _CsrstUserLocaleInfoRev1_Type(DisplayString):defaultValue=OctetString('US/US/US/US/US');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(14,64))
_CsrstUserLocaleInfoRev1_Type.__name__=_AB
_CsrstUserLocaleInfoRev1_Object=MibScalar
csrstUserLocaleInfoRev1=_CsrstUserLocaleInfoRev1_Object((1,3,6,1,4,1,9,9,441,1,2,35),_CsrstUserLocaleInfoRev1_Type())
csrstUserLocaleInfoRev1.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstUserLocaleInfoRev1.setStatus(_B)
_CsrstActiveStats_ObjectIdentity=ObjectIdentity
csrstActiveStats=_CsrstActiveStats_ObjectIdentity((1,3,6,1,4,1,9,9,441,1,3))
_CsrstState_Type=SrstOperType
_CsrstState_Object=MibScalar
csrstState=_CsrstState_Object((1,3,6,1,4,1,9,9,441,1,3,1),_CsrstState_Type())
csrstState.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstState.setStatus(_B)
_CsrstSipPhoneCurrentRegistered_Type=Gauge32
_CsrstSipPhoneCurrentRegistered_Object=MibScalar
csrstSipPhoneCurrentRegistered=_CsrstSipPhoneCurrentRegistered_Object((1,3,6,1,4,1,9,9,441,1,3,2),_CsrstSipPhoneCurrentRegistered_Type())
csrstSipPhoneCurrentRegistered.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSipPhoneCurrentRegistered.setStatus(_B)
_CsrstSipCallLegs_Type=Counter32
_CsrstSipCallLegs_Object=MibScalar
csrstSipCallLegs=_CsrstSipCallLegs_Object((1,3,6,1,4,1,9,9,441,1,3,3),_CsrstSipCallLegs_Type())
csrstSipCallLegs.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSipCallLegs.setStatus(_B)
_CsrstTotalUpTime_Type=Counter32
_CsrstTotalUpTime_Object=MibScalar
csrstTotalUpTime=_CsrstTotalUpTime_Object((1,3,6,1,4,1,9,9,441,1,3,4),_CsrstTotalUpTime_Type())
csrstTotalUpTime.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstTotalUpTime.setStatus(_B)
if mibBuilder.loadTexts:csrstTotalUpTime.setUnits('minutes')
_CsrstSipConf_ObjectIdentity=ObjectIdentity
csrstSipConf=_CsrstSipConf_ObjectIdentity((1,3,6,1,4,1,9,9,441,1,4))
class _CsrstSipRegSrvExpMax_Type(Integer32):defaultValue=3600;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(600,86400))
_CsrstSipRegSrvExpMax_Type.__name__=_E
_CsrstSipRegSrvExpMax_Object=MibScalar
csrstSipRegSrvExpMax=_CsrstSipRegSrvExpMax_Object((1,3,6,1,4,1,9,9,441,1,4,1),_CsrstSipRegSrvExpMax_Type())
csrstSipRegSrvExpMax.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSipRegSrvExpMax.setStatus(_B)
if mibBuilder.loadTexts:csrstSipRegSrvExpMax.setUnits(_H)
class _CsrstSipRegSrvExpMin_Type(Integer32):defaultValue=60;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,3600))
_CsrstSipRegSrvExpMin_Type.__name__=_E
_CsrstSipRegSrvExpMin_Object=MibScalar
csrstSipRegSrvExpMin=_CsrstSipRegSrvExpMin_Object((1,3,6,1,4,1,9,9,441,1,4,2),_CsrstSipRegSrvExpMin_Type())
csrstSipRegSrvExpMin.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSipRegSrvExpMin.setStatus(_B)
if mibBuilder.loadTexts:csrstSipRegSrvExpMin.setUnits(_H)
class _CsrstSipIp2IpGlobalEnabled_Type(TruthValue):defaultValue=2
_CsrstSipIp2IpGlobalEnabled_Type.__name__=_Q
_CsrstSipIp2IpGlobalEnabled_Object=MibScalar
csrstSipIp2IpGlobalEnabled=_CsrstSipIp2IpGlobalEnabled_Object((1,3,6,1,4,1,9,9,441,1,4,3),_CsrstSipIp2IpGlobalEnabled_Type())
csrstSipIp2IpGlobalEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSipIp2IpGlobalEnabled.setStatus(_B)
class _CsrstSipSend300MultSupport_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('bestMatch',1),('longestMatch',2)))
_CsrstSipSend300MultSupport_Type.__name__=_E
_CsrstSipSend300MultSupport_Object=MibScalar
csrstSipSend300MultSupport=_CsrstSipSend300MultSupport_Object((1,3,6,1,4,1,9,9,441,1,4,4),_CsrstSipSend300MultSupport_Type())
csrstSipSend300MultSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSipSend300MultSupport.setStatus(_B)
_CsrstSipVoRegPoolTable_Object=MibTable
csrstSipVoRegPoolTable=_CsrstSipVoRegPoolTable_Object((1,3,6,1,4,1,9,9,441,1,4,5))
if mibBuilder.loadTexts:csrstSipVoRegPoolTable.setStatus(_B)
_CsrstSipVoRegPoolEntry_Object=MibTableRow
csrstSipVoRegPoolEntry=_CsrstSipVoRegPoolEntry_Object((1,3,6,1,4,1,9,9,441,1,4,5,1))
csrstSipVoRegPoolEntry.setIndexNames((0,_A,_S))
if mibBuilder.loadTexts:csrstSipVoRegPoolEntry.setStatus(_B)
_CsrstSipVoRegPoolTag_Type=Unsigned32
_CsrstSipVoRegPoolTag_Object=MibTableColumn
csrstSipVoRegPoolTag=_CsrstSipVoRegPoolTag_Object((1,3,6,1,4,1,9,9,441,1,4,5,1,1),_CsrstSipVoRegPoolTag_Type())
csrstSipVoRegPoolTag.setMaxAccess(_I)
if mibBuilder.loadTexts:csrstSipVoRegPoolTag.setStatus(_B)
class _CsrstSipNetId_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CsrstSipNetId_Type.__name__=_D
_CsrstSipNetId_Object=MibTableColumn
csrstSipNetId=_CsrstSipNetId_Object((1,3,6,1,4,1,9,9,441,1,4,5,1,2),_CsrstSipNetId_Type())
csrstSipNetId.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSipNetId.setStatus(_B)
_CsrstSipVoRegPoolIpAddrType_Type=InetAddressType
_CsrstSipVoRegPoolIpAddrType_Object=MibTableColumn
csrstSipVoRegPoolIpAddrType=_CsrstSipVoRegPoolIpAddrType_Object((1,3,6,1,4,1,9,9,441,1,4,5,1,3),_CsrstSipVoRegPoolIpAddrType_Type())
csrstSipVoRegPoolIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSipVoRegPoolIpAddrType.setStatus(_B)
_CsrstSipNetMask_Type=InetAddress
_CsrstSipNetMask_Object=MibTableColumn
csrstSipNetMask=_CsrstSipNetMask_Object((1,3,6,1,4,1,9,9,441,1,4,5,1,4),_CsrstSipNetMask_Type())
csrstSipNetMask.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSipNetMask.setStatus(_B)
_CsrstSipProxySrvIpAddr_Type=InetAddress
_CsrstSipProxySrvIpAddr_Object=MibTableColumn
csrstSipProxySrvIpAddr=_CsrstSipProxySrvIpAddr_Object((1,3,6,1,4,1,9,9,441,1,4,5,1,5),_CsrstSipProxySrvIpAddr_Type())
csrstSipProxySrvIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSipProxySrvIpAddr.setStatus(_B)
class _CsrstSipProxySrvPref_Type(Unsigned32):defaultValue=0
_CsrstSipProxySrvPref_Type.__name__=_F
_CsrstSipProxySrvPref_Object=MibTableColumn
csrstSipProxySrvPref=_CsrstSipProxySrvPref_Object((1,3,6,1,4,1,9,9,441,1,4,5,1,6),_CsrstSipProxySrvPref_Type())
csrstSipProxySrvPref.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSipProxySrvPref.setStatus(_B)
class _CsrstSipProxySrvMonitor_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('icmp',1),('rtr',2)))
_CsrstSipProxySrvMonitor_Type.__name__=_E
_CsrstSipProxySrvMonitor_Object=MibTableColumn
csrstSipProxySrvMonitor=_CsrstSipProxySrvMonitor_Object((1,3,6,1,4,1,9,9,441,1,4,5,1,7),_CsrstSipProxySrvMonitor_Type())
csrstSipProxySrvMonitor.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSipProxySrvMonitor.setStatus(_B)
_CsrstSipProxySrvAltIpAddr_Type=InetAddress
_CsrstSipProxySrvAltIpAddr_Object=MibTableColumn
csrstSipProxySrvAltIpAddr=_CsrstSipProxySrvAltIpAddr_Object((1,3,6,1,4,1,9,9,441,1,4,5,1,8),_CsrstSipProxySrvAltIpAddr_Type())
csrstSipProxySrvAltIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSipProxySrvAltIpAddr.setStatus(_B)
class _CsrstSipDefaultPreference_Type(Unsigned32):defaultValue=0
_CsrstSipDefaultPreference_Type.__name__=_F
_CsrstSipDefaultPreference_Object=MibTableColumn
csrstSipDefaultPreference=_CsrstSipDefaultPreference_Object((1,3,6,1,4,1,9,9,441,1,4,5,1,9),_CsrstSipDefaultPreference_Type())
csrstSipDefaultPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSipDefaultPreference.setStatus(_B)
class _CsrstSipVoRegPoolAppl_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CsrstSipVoRegPoolAppl_Type.__name__=_D
_CsrstSipVoRegPoolAppl_Object=MibTableColumn
csrstSipVoRegPoolAppl=_CsrstSipVoRegPoolAppl_Object((1,3,6,1,4,1,9,9,441,1,4,5,1,10),_CsrstSipVoRegPoolAppl_Type())
csrstSipVoRegPoolAppl.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSipVoRegPoolAppl.setStatus(_B)
_CsrstSipVoRegNumberListTable_Object=MibTable
csrstSipVoRegNumberListTable=_CsrstSipVoRegNumberListTable_Object((1,3,6,1,4,1,9,9,441,1,4,6))
if mibBuilder.loadTexts:csrstSipVoRegNumberListTable.setStatus(_B)
_CsrstSipVoRegNumberListEntry_Object=MibTableRow
csrstSipVoRegNumberListEntry=_CsrstSipVoRegNumberListEntry_Object((1,3,6,1,4,1,9,9,441,1,4,6,1))
csrstSipVoRegNumberListEntry.setIndexNames((0,_A,_S),(0,_A,_AE))
if mibBuilder.loadTexts:csrstSipVoRegNumberListEntry.setStatus(_B)
_CsrstSipVoRegNumberListIndex_Type=Unsigned32
_CsrstSipVoRegNumberListIndex_Object=MibTableColumn
csrstSipVoRegNumberListIndex=_CsrstSipVoRegNumberListIndex_Object((1,3,6,1,4,1,9,9,441,1,4,6,1,1),_CsrstSipVoRegNumberListIndex_Type())
csrstSipVoRegNumberListIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:csrstSipVoRegNumberListIndex.setStatus(_B)
_CsrstSipVoRegNumberListTag_Type=Unsigned32
_CsrstSipVoRegNumberListTag_Object=MibTableColumn
csrstSipVoRegNumberListTag=_CsrstSipVoRegNumberListTag_Object((1,3,6,1,4,1,9,9,441,1,4,6,1,2),_CsrstSipVoRegNumberListTag_Type())
csrstSipVoRegNumberListTag.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSipVoRegNumberListTag.setStatus(_B)
class _CsrstSipVoRegNumberPattern_Type(CvE164Address):subtypeSpec=CvE164Address.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CsrstSipVoRegNumberPattern_Type.__name__=_G
_CsrstSipVoRegNumberPattern_Object=MibTableColumn
csrstSipVoRegNumberPattern=_CsrstSipVoRegNumberPattern_Object((1,3,6,1,4,1,9,9,441,1,4,6,1,3),_CsrstSipVoRegNumberPattern_Type())
csrstSipVoRegNumberPattern.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSipVoRegNumberPattern.setStatus(_B)
class _CsrstSipVoRegNumberPref_Type(Unsigned32):defaultValue=0
_CsrstSipVoRegNumberPref_Type.__name__=_F
_CsrstSipVoRegNumberPref_Object=MibTableColumn
csrstSipVoRegNumberPref=_CsrstSipVoRegNumberPref_Object((1,3,6,1,4,1,9,9,441,1,4,6,1,4),_CsrstSipVoRegNumberPref_Type())
csrstSipVoRegNumberPref.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSipVoRegNumberPref.setStatus(_B)
_CsrstSipVoRegNumberHuntstopEnabled_Type=TruthValue
_CsrstSipVoRegNumberHuntstopEnabled_Object=MibTableColumn
csrstSipVoRegNumberHuntstopEnabled=_CsrstSipVoRegNumberHuntstopEnabled_Object((1,3,6,1,4,1,9,9,441,1,4,6,1,5),_CsrstSipVoRegNumberHuntstopEnabled_Type())
csrstSipVoRegNumberHuntstopEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSipVoRegNumberHuntstopEnabled.setStatus(_B)
_CsrstSipEndpointTable_Object=MibTable
csrstSipEndpointTable=_CsrstSipEndpointTable_Object((1,3,6,1,4,1,9,9,441,1,4,7))
if mibBuilder.loadTexts:csrstSipEndpointTable.setStatus(_B)
_CsrstSipEndpointEntry_Object=MibTableRow
csrstSipEndpointEntry=_CsrstSipEndpointEntry_Object((1,3,6,1,4,1,9,9,441,1,4,7,1))
csrstSipEndpointEntry.setIndexNames((0,_A,_AF))
if mibBuilder.loadTexts:csrstSipEndpointEntry.setStatus(_B)
_CsrstSipEndpointTag_Type=Unsigned32
_CsrstSipEndpointTag_Object=MibTableColumn
csrstSipEndpointTag=_CsrstSipEndpointTag_Object((1,3,6,1,4,1,9,9,441,1,4,7,1,1),_CsrstSipEndpointTag_Type())
csrstSipEndpointTag.setMaxAccess(_I)
if mibBuilder.loadTexts:csrstSipEndpointTag.setStatus(_B)
_CsrstSipVoRegPoolEdptTag_Type=Unsigned32
_CsrstSipVoRegPoolEdptTag_Object=MibTableColumn
csrstSipVoRegPoolEdptTag=_CsrstSipVoRegPoolEdptTag_Object((1,3,6,1,4,1,9,9,441,1,4,7,1,2),_CsrstSipVoRegPoolEdptTag_Type())
csrstSipVoRegPoolEdptTag.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSipVoRegPoolEdptTag.setStatus(_B)
_CsrstSipEndpointIpAddrType_Type=InetAddressType
_CsrstSipEndpointIpAddrType_Object=MibTableColumn
csrstSipEndpointIpAddrType=_CsrstSipEndpointIpAddrType_Object((1,3,6,1,4,1,9,9,441,1,4,7,1,3),_CsrstSipEndpointIpAddrType_Type())
csrstSipEndpointIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSipEndpointIpAddrType.setStatus(_B)
_CsrstSipEndpointIpAddress_Type=InetAddress
_CsrstSipEndpointIpAddress_Object=MibTableColumn
csrstSipEndpointIpAddress=_CsrstSipEndpointIpAddress_Object((1,3,6,1,4,1,9,9,441,1,4,7,1,4),_CsrstSipEndpointIpAddress_Type())
csrstSipEndpointIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSipEndpointIpAddress.setStatus(_B)
class _CsrstSipEndpointDN_Type(CvE164Address):subtypeSpec=CvE164Address.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CsrstSipEndpointDN_Type.__name__=_G
_CsrstSipEndpointDN_Object=MibTableColumn
csrstSipEndpointDN=_CsrstSipEndpointDN_Object((1,3,6,1,4,1,9,9,441,1,4,7,1,5),_CsrstSipEndpointDN_Type())
csrstSipEndpointDN.setMaxAccess(_C)
if mibBuilder.loadTexts:csrstSipEndpointDN.setStatus(_B)
_CiscoSrstMIBConformance_ObjectIdentity=ObjectIdentity
ciscoSrstMIBConformance=_CiscoSrstMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,441,2))
_CiscoSrstMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoSrstMIBCompliances=_CiscoSrstMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,441,2,1))
_CiscoSrstMIBGroups_ObjectIdentity=ObjectIdentity
ciscoSrstMIBGroups=_CiscoSrstMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,441,2,2))
class _CsrstSysNotifSeverity_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('clear',1),('minor',2),('major',3)))
_CsrstSysNotifSeverity_Type.__name__=_E
_CsrstSysNotifSeverity_Object=MibScalar
csrstSysNotifSeverity=_CsrstSysNotifSeverity_Object((1,3,6,1,4,1,9,9,441,2,2,2,1),_CsrstSysNotifSeverity_Type())
csrstSysNotifSeverity.setMaxAccess(_AG)
if mibBuilder.loadTexts:csrstSysNotifSeverity.setStatus(_B)
class _CsrstSysNotifReason_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_CsrstSysNotifReason_Type.__name__=_D
_CsrstSysNotifReason_Object=MibScalar
csrstSysNotifReason=_CsrstSysNotifReason_Object((1,3,6,1,4,1,9,9,441,2,2,2,2),_CsrstSysNotifReason_Type())
csrstSysNotifReason.setMaxAccess(_AG)
if mibBuilder.loadTexts:csrstSysNotifReason.setStatus(_B)
csrstConfGroup=ObjectGroup((1,3,6,1,4,1,9,9,441,2,2,1))
csrstConfGroup.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_L),(_A,_Y),(_A,_Z),(_A,_M),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_AH),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_J),(_A,_z),(_A,_A0),(_A,_K),(_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:csrstConfGroup.setStatus(_R)
csrstNotifInfoGroup=ObjectGroup((1,3,6,1,4,1,9,9,441,2,2,2))
csrstNotifInfoGroup.setObjects(*((_A,_N),(_A,_O)))
if mibBuilder.loadTexts:csrstNotifInfoGroup.setStatus(_B)
csrstActiveStatsGroup=ObjectGroup((1,3,6,1,4,1,9,9,441,2,2,3))
csrstActiveStatsGroup.setObjects(*((_A,_A3),(_A,_A4),(_A,_AI),(_A,_AJ)))
if mibBuilder.loadTexts:csrstActiveStatsGroup.setStatus(_B)
csrstSipConfGroup=ObjectGroup((1,3,6,1,4,1,9,9,441,2,2,4))
csrstSipConfGroup.setObjects(*((_A,_AK),(_A,_AL),(_A,_AM),(_A,_AN),(_A,_AO),(_A,_AP),(_A,_AQ),(_A,_AR),(_A,_AS),(_A,_AT),(_A,_AU),(_A,_AV),(_A,_AW),(_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab),(_A,_Ac),(_A,_A5),(_A,_Ad)))
if mibBuilder.loadTexts:csrstSipConfGroup.setStatus(_B)
csrstConfGroupRev1=ObjectGroup((1,3,6,1,4,1,9,9,441,2,2,6))
csrstConfGroupRev1.setObjects(*((_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_L),(_A,_Y),(_A,_Z),(_A,_M),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_J),(_A,_z),(_A,_A0),(_A,_K),(_A,_A1),(_A,_A2),(_A,_Ae)))
if mibBuilder.loadTexts:csrstConfGroupRev1.setStatus(_B)
csrstStateChange=NotificationType((1,3,6,1,4,1,9,9,441,0,1))
csrstStateChange.setObjects(*((_A,_N),(_A,_A3),(_A,_O)))
if mibBuilder.loadTexts:csrstStateChange.setStatus(_B)
csrstFailNotif=NotificationType((1,3,6,1,4,1,9,9,441,0,2))
csrstFailNotif.setObjects(*((_A,_N),(_A,_O)))
if mibBuilder.loadTexts:csrstFailNotif.setStatus(_B)
csrstSipPhoneUnRegThresholdExceed=NotificationType((1,3,6,1,4,1,9,9,441,0,3))
csrstSipPhoneUnRegThresholdExceed.setObjects(*((_A,_M),(_A,_A4)))
if mibBuilder.loadTexts:csrstSipPhoneUnRegThresholdExceed.setStatus(_B)
csrstSipPhoneRegFailed=NotificationType((1,3,6,1,4,1,9,9,441,0,4))
csrstSipPhoneRegFailed.setObjects((_A,_A5))
if mibBuilder.loadTexts:csrstSipPhoneRegFailed.setStatus(_B)
csrstConferenceFailed=NotificationType((1,3,6,1,4,1,9,9,441,0,5))
csrstConferenceFailed.setObjects((_A,_L))
if mibBuilder.loadTexts:csrstConferenceFailed.setStatus(_B)
csrstMIBNotifsGroup=NotificationGroup((1,3,6,1,4,1,9,9,441,2,2,5))
csrstMIBNotifsGroup.setObjects(*((_A,_Af),(_A,_Ag),(_A,_Ah),(_A,_Ai),(_A,_Aj)))
if mibBuilder.loadTexts:csrstMIBNotifsGroup.setStatus(_B)
ciscoSrstMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,441,2,1,1))
ciscoSrstMIBCompliance.setObjects(*((_A,_Ak),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:ciscoSrstMIBCompliance.setStatus(_R)
ciscoSrstMIBComplianceRev1=ModuleCompliance((1,3,6,1,4,1,9,9,441,2,1,2))
ciscoSrstMIBComplianceRev1.setObjects(*((_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_Al)))
if mibBuilder.loadTexts:ciscoSrstMIBComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'SrstOperType':SrstOperType,'ciscoSrstMIB':ciscoSrstMIB,'ciscoSrstMIBNotifications':ciscoSrstMIBNotifications,_Af:csrstStateChange,_Ag:csrstFailNotif,_Ah:csrstSipPhoneUnRegThresholdExceed,_Ai:csrstSipPhoneRegFailed,_Aj:csrstConferenceFailed,'ciscoSrstMIBObjects':ciscoSrstMIBObjects,'csrstGlobal':csrstGlobal,'csrstConf':csrstConf,_T:csrstEnabled,_U:csrstVersion,_V:csrstIPAddressType,_W:csrstIPAddress,_X:csrstPortNumber,_L:csrstMaxConferences,_Y:csrstMaxEphones,_Z:csrstMaxDN,_M:csrstSipPhoneUnRegThreshold,_a:csrstCallFwdNoAnswer,_b:csrstCallFwdNoAnswerTo,_c:csrstCallFwdBusy,_d:csrstMohFilename,_e:csrstMohMulticastAddrType,_f:csrstMohMulticastAddr,_g:csrstMohMulticastPort,_h:csrstVoiceMailNumber,_i:csrstSystemMessagePrimary,_j:csrstSystemMessageSecondary,_k:csrstScriptName,_l:csrstSecondaryDialTone,_m:csrstTransferSystem,_AH:csrstUserLocaleInfo,_n:csrstDateFormat,_o:csrstTimeFormat,_p:csrstInterdigitTo,_q:csrstBusyTo,_r:csrstAlertTo,_s:csrstXlateCalledNumber,_t:csrstXlateCallingNumber,'csrstAliasTable':csrstAliasTable,'csrstAliasEntry':csrstAliasEntry,_AD:csrstAliasIndex,_u:csrstAliasTag,_v:csrstAliasNumPattern,_w:csrstAliasAltNumber,_x:csrstAliasPreference,_y:csrstAliasHuntStopEnabled,'csrstAccessCodeTable':csrstAccessCodeTable,'csrstAccessCodeEntry':csrstAccessCodeEntry,_J:csrstAccessCodeType,_z:csrstAccessCode,_A0:csrstAccessCodeDIDEnabled,'csrstLimitDNTable':csrstLimitDNTable,'csrstLimitDNEntry':csrstLimitDNEntry,_K:csrstLimitDNType,_A1:csrstLimitDN,_A2:csrstNotificationEnabled,_Ae:csrstUserLocaleInfoRev1,'csrstActiveStats':csrstActiveStats,_A3:csrstState,_A4:csrstSipPhoneCurrentRegistered,_AI:csrstSipCallLegs,_AJ:csrstTotalUpTime,'csrstSipConf':csrstSipConf,_AK:csrstSipRegSrvExpMax,_AL:csrstSipRegSrvExpMin,_AM:csrstSipIp2IpGlobalEnabled,_AN:csrstSipSend300MultSupport,'csrstSipVoRegPoolTable':csrstSipVoRegPoolTable,'csrstSipVoRegPoolEntry':csrstSipVoRegPoolEntry,_S:csrstSipVoRegPoolTag,_AO:csrstSipNetId,_AP:csrstSipVoRegPoolIpAddrType,_AQ:csrstSipNetMask,_AR:csrstSipProxySrvIpAddr,_AS:csrstSipProxySrvPref,_AT:csrstSipProxySrvMonitor,_AU:csrstSipProxySrvAltIpAddr,_AV:csrstSipDefaultPreference,_AW:csrstSipVoRegPoolAppl,'csrstSipVoRegNumberListTable':csrstSipVoRegNumberListTable,'csrstSipVoRegNumberListEntry':csrstSipVoRegNumberListEntry,_AE:csrstSipVoRegNumberListIndex,_AX:csrstSipVoRegNumberListTag,_AY:csrstSipVoRegNumberPattern,_AZ:csrstSipVoRegNumberPref,_Aa:csrstSipVoRegNumberHuntstopEnabled,'csrstSipEndpointTable':csrstSipEndpointTable,'csrstSipEndpointEntry':csrstSipEndpointEntry,_AF:csrstSipEndpointTag,_Ab:csrstSipVoRegPoolEdptTag,_Ac:csrstSipEndpointIpAddrType,_A5:csrstSipEndpointIpAddress,_Ad:csrstSipEndpointDN,'ciscoSrstMIBConformance':ciscoSrstMIBConformance,'ciscoSrstMIBCompliances':ciscoSrstMIBCompliances,'ciscoSrstMIBCompliance':ciscoSrstMIBCompliance,'ciscoSrstMIBComplianceRev1':ciscoSrstMIBComplianceRev1,'ciscoSrstMIBGroups':ciscoSrstMIBGroups,_Ak:csrstConfGroup,_A6:csrstNotifInfoGroup,_N:csrstSysNotifSeverity,_O:csrstSysNotifReason,_A8:csrstActiveStatsGroup,_A7:csrstSipConfGroup,_A9:csrstMIBNotifsGroup,_Al:csrstConfGroupRev1})