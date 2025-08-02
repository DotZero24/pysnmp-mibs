_AQ='h323DebugH323SupplementaryTraceGroupVer1'
_AP='h323DebugH323StackTrace2GroupVer1'
_AO='h323DebugH323StackTraceGroupVer1'
_AN='h323DebugSuppTraceGkReg'
_AM='h323DebugSuppTraceDebugProvision'
_AL='h323DebugSuppTraceMediaProvision'
_AK='h323DebugSuppTraceEngineProvision'
_AJ='h323DebugH323StackTrace2Level'
_AI='h323DebugH323StackTrace2Module'
_AH='h323DebugH323StackTrace2GeneralLevel'
_AG='h323DebugH323StackTrace2ContentEnable'
_AF='h323DebugH323StackTrace2Enable'
_AE='h323DebugH323StackTraceModulesVt'
_AD='h323DebugH323StackTraceModulesUnreg'
_AC='h323DebugH323StackTraceModulesUdpchan'
_AB='h323DebugH323StackTraceModulesTunnctrl'
_AA='h323DebugH323StackTraceModulesTransport'
_A9='h323DebugH323StackTraceModulesTpktchan'
_A8='h323DebugH323StackTraceModulesTimer'
_A7='h323DebugH323StackTraceModulesSserr'
_A6='h323DebugH323StackTraceModulesSseerr'
_A5='h323DebugH323StackTraceModulesSsechan'
_A4='h323DebugH323StackTraceModulesSseapicb'
_A3='h323DebugH323StackTraceModulesSseapi'
_A2='h323DebugH323StackTraceModulesSschan'
_A1='h323DebugH323StackTraceModulesSsapicb'
_A0='h323DebugH323StackTraceModulesSsapi'
_z='h323DebugH323StackTraceModulesSeli'
_y='h323DebugH323StackTraceModulesRasindb'
_x='h323DebugH323StackTraceModulesRasctrl'
_w='h323DebugH323StackTraceModulesRa'
_v='h323DebugH323StackTraceModulesQ931err'
_u='h323DebugH323StackTraceModulesQ931'
_t='h323DebugH323StackTraceModulesPi'
_s='h323DebugH323StackTraceModulesPdltimer'
_r='h323DebugH323StackTraceModulesPdlsrc'
_q='h323DebugH323StackTraceModulesPdlsm'
_p='h323DebugH323StackTraceModulesPdlprnwrn'
_o='h323DebugH323StackTraceModulesPdlprnerr'
_n='h323DebugH323StackTraceModulesPdlprint'
_m='h323DebugH323StackTraceModulesPdlmtask'
_l='h323DebugH323StackTraceModulesPdlmisc'
_k='h323DebugH323StackTraceModulesPdllist'
_j='h323DebugH323StackTraceModulesPdlfnerr'
_i='h323DebugH323StackTraceModulesPdlerror'
_h='h323DebugH323StackTraceModulesPdlencode'
_g='h323DebugH323StackTraceModulesPdlconf'
_f='h323DebugH323StackTraceModulesPdlcomm'
_e='h323DebugH323StackTraceModulesPdlchan'
_d='h323DebugH323StackTraceModulesPdlapi'
_c='h323DebugH323StackTraceModulesPererr'
_b='h323DebugH323StackTraceModulesPer'
_a='h323DebugH323StackTraceModulesNamechan'
_Z='h323DebugH323StackTraceModulesMei'
_Y='h323DebugH323StackTraceModulesLiinfo'
_X='h323DebugH323StackTraceModulesLi'
_W='h323DebugH323StackTraceModulesH450apdu'
_V='h323DebugH323StackTraceModulesEtimerheap'
_U='h323DebugH323StackTraceModulesEtimer'
_T='h323DebugH323StackTraceModulesEfrm'
_S='h323DebugH323StackTraceModulesDebug'
_R='h323DebugH323StackTraceModulesCmerr'
_Q='h323DebugH323StackTraceModulesCmapicb'
_P='h323DebugH323StackTraceModulesCmapi'
_O='h323DebugH323StackTraceModulesCm'
_N='h323DebugH323StackTraceModulesChannels'
_M='h323DebugH323StackTraceModulesCaerr'
_L='h323DebugH323StackTraceModulesCa'
_K='h323DebugH323StackTraceModulesAnnexE'
_J='h323DebugH323StackTraceLevel'
_I='h323DebugH323StackTrace2ModuleIndex'
_H='warning'
_G='exception'
_F='disable'
_E='Integer32'
_D='MxEnableState'
_C='read-write'
_B='MX-H323-DEBUG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixExperimental,=mibBuilder.importSymbols('MX-SMI','mediatrixExperimental')
MxEnableState,=mibBuilder.importSymbols('MX-TC',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h323DebugMIB=ModuleIdentity((1,3,6,1,4,1,4935,99,35))
if mibBuilder.loadTexts:h323DebugMIB.setRevisions(('2004-10-14 00:00','2003-04-09 00:00','2003-01-07 00:00','2002-12-19 00:00','2002-11-13 00:00','2002-10-02 00:00'))
_H323DebugMIBObjects_ObjectIdentity=ObjectIdentity
h323DebugMIBObjects=_H323DebugMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,99,35,1))
_H323DebugH323StackTrace_ObjectIdentity=ObjectIdentity
h323DebugH323StackTrace=_H323DebugH323StackTrace_ObjectIdentity((1,3,6,1,4,1,4935,99,35,1,5))
class _H323DebugH323StackTraceLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('level-0',0),('level-1',1),('level-2',2),('level-3',3)))
_H323DebugH323StackTraceLevel_Type.__name__=_E
_H323DebugH323StackTraceLevel_Object=MibScalar
h323DebugH323StackTraceLevel=_H323DebugH323StackTraceLevel_Object((1,3,6,1,4,1,4935,99,35,1,5,5),_H323DebugH323StackTraceLevel_Type())
h323DebugH323StackTraceLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceLevel.setStatus(_A)
_H323DebugH323StackTraceModules_ObjectIdentity=ObjectIdentity
h323DebugH323StackTraceModules=_H323DebugH323StackTraceModules_ObjectIdentity((1,3,6,1,4,1,4935,99,35,1,5,10))
class _H323DebugH323StackTraceModulesAnnexE_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesAnnexE_Type.__name__=_D
_H323DebugH323StackTraceModulesAnnexE_Object=MibScalar
h323DebugH323StackTraceModulesAnnexE=_H323DebugH323StackTraceModulesAnnexE_Object((1,3,6,1,4,1,4935,99,35,1,5,10,5),_H323DebugH323StackTraceModulesAnnexE_Type())
h323DebugH323StackTraceModulesAnnexE.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesAnnexE.setStatus(_A)
class _H323DebugH323StackTraceModulesCa_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesCa_Type.__name__=_D
_H323DebugH323StackTraceModulesCa_Object=MibScalar
h323DebugH323StackTraceModulesCa=_H323DebugH323StackTraceModulesCa_Object((1,3,6,1,4,1,4935,99,35,1,5,10,10),_H323DebugH323StackTraceModulesCa_Type())
h323DebugH323StackTraceModulesCa.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesCa.setStatus(_A)
class _H323DebugH323StackTraceModulesCaerr_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesCaerr_Type.__name__=_D
_H323DebugH323StackTraceModulesCaerr_Object=MibScalar
h323DebugH323StackTraceModulesCaerr=_H323DebugH323StackTraceModulesCaerr_Object((1,3,6,1,4,1,4935,99,35,1,5,10,15),_H323DebugH323StackTraceModulesCaerr_Type())
h323DebugH323StackTraceModulesCaerr.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesCaerr.setStatus(_A)
class _H323DebugH323StackTraceModulesChannels_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesChannels_Type.__name__=_D
_H323DebugH323StackTraceModulesChannels_Object=MibScalar
h323DebugH323StackTraceModulesChannels=_H323DebugH323StackTraceModulesChannels_Object((1,3,6,1,4,1,4935,99,35,1,5,10,20),_H323DebugH323StackTraceModulesChannels_Type())
h323DebugH323StackTraceModulesChannels.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesChannels.setStatus(_A)
class _H323DebugH323StackTraceModulesCm_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesCm_Type.__name__=_D
_H323DebugH323StackTraceModulesCm_Object=MibScalar
h323DebugH323StackTraceModulesCm=_H323DebugH323StackTraceModulesCm_Object((1,3,6,1,4,1,4935,99,35,1,5,10,25),_H323DebugH323StackTraceModulesCm_Type())
h323DebugH323StackTraceModulesCm.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesCm.setStatus(_A)
class _H323DebugH323StackTraceModulesCmapi_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesCmapi_Type.__name__=_D
_H323DebugH323StackTraceModulesCmapi_Object=MibScalar
h323DebugH323StackTraceModulesCmapi=_H323DebugH323StackTraceModulesCmapi_Object((1,3,6,1,4,1,4935,99,35,1,5,10,30),_H323DebugH323StackTraceModulesCmapi_Type())
h323DebugH323StackTraceModulesCmapi.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesCmapi.setStatus(_A)
class _H323DebugH323StackTraceModulesCmapicb_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesCmapicb_Type.__name__=_D
_H323DebugH323StackTraceModulesCmapicb_Object=MibScalar
h323DebugH323StackTraceModulesCmapicb=_H323DebugH323StackTraceModulesCmapicb_Object((1,3,6,1,4,1,4935,99,35,1,5,10,35),_H323DebugH323StackTraceModulesCmapicb_Type())
h323DebugH323StackTraceModulesCmapicb.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesCmapicb.setStatus(_A)
class _H323DebugH323StackTraceModulesCmerr_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesCmerr_Type.__name__=_D
_H323DebugH323StackTraceModulesCmerr_Object=MibScalar
h323DebugH323StackTraceModulesCmerr=_H323DebugH323StackTraceModulesCmerr_Object((1,3,6,1,4,1,4935,99,35,1,5,10,40),_H323DebugH323StackTraceModulesCmerr_Type())
h323DebugH323StackTraceModulesCmerr.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesCmerr.setStatus(_A)
class _H323DebugH323StackTraceModulesDebug_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesDebug_Type.__name__=_D
_H323DebugH323StackTraceModulesDebug_Object=MibScalar
h323DebugH323StackTraceModulesDebug=_H323DebugH323StackTraceModulesDebug_Object((1,3,6,1,4,1,4935,99,35,1,5,10,45),_H323DebugH323StackTraceModulesDebug_Type())
h323DebugH323StackTraceModulesDebug.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesDebug.setStatus(_A)
class _H323DebugH323StackTraceModulesEfrm_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesEfrm_Type.__name__=_D
_H323DebugH323StackTraceModulesEfrm_Object=MibScalar
h323DebugH323StackTraceModulesEfrm=_H323DebugH323StackTraceModulesEfrm_Object((1,3,6,1,4,1,4935,99,35,1,5,10,50),_H323DebugH323StackTraceModulesEfrm_Type())
h323DebugH323StackTraceModulesEfrm.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesEfrm.setStatus(_A)
class _H323DebugH323StackTraceModulesEtimer_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesEtimer_Type.__name__=_D
_H323DebugH323StackTraceModulesEtimer_Object=MibScalar
h323DebugH323StackTraceModulesEtimer=_H323DebugH323StackTraceModulesEtimer_Object((1,3,6,1,4,1,4935,99,35,1,5,10,55),_H323DebugH323StackTraceModulesEtimer_Type())
h323DebugH323StackTraceModulesEtimer.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesEtimer.setStatus(_A)
class _H323DebugH323StackTraceModulesEtimerheap_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesEtimerheap_Type.__name__=_D
_H323DebugH323StackTraceModulesEtimerheap_Object=MibScalar
h323DebugH323StackTraceModulesEtimerheap=_H323DebugH323StackTraceModulesEtimerheap_Object((1,3,6,1,4,1,4935,99,35,1,5,10,60),_H323DebugH323StackTraceModulesEtimerheap_Type())
h323DebugH323StackTraceModulesEtimerheap.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesEtimerheap.setStatus(_A)
class _H323DebugH323StackTraceModulesH450apdu_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesH450apdu_Type.__name__=_D
_H323DebugH323StackTraceModulesH450apdu_Object=MibScalar
h323DebugH323StackTraceModulesH450apdu=_H323DebugH323StackTraceModulesH450apdu_Object((1,3,6,1,4,1,4935,99,35,1,5,10,65),_H323DebugH323StackTraceModulesH450apdu_Type())
h323DebugH323StackTraceModulesH450apdu.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesH450apdu.setStatus(_A)
class _H323DebugH323StackTraceModulesLi_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesLi_Type.__name__=_D
_H323DebugH323StackTraceModulesLi_Object=MibScalar
h323DebugH323StackTraceModulesLi=_H323DebugH323StackTraceModulesLi_Object((1,3,6,1,4,1,4935,99,35,1,5,10,70),_H323DebugH323StackTraceModulesLi_Type())
h323DebugH323StackTraceModulesLi.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesLi.setStatus(_A)
class _H323DebugH323StackTraceModulesLiinfo_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesLiinfo_Type.__name__=_D
_H323DebugH323StackTraceModulesLiinfo_Object=MibScalar
h323DebugH323StackTraceModulesLiinfo=_H323DebugH323StackTraceModulesLiinfo_Object((1,3,6,1,4,1,4935,99,35,1,5,10,75),_H323DebugH323StackTraceModulesLiinfo_Type())
h323DebugH323StackTraceModulesLiinfo.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesLiinfo.setStatus(_A)
class _H323DebugH323StackTraceModulesMei_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesMei_Type.__name__=_D
_H323DebugH323StackTraceModulesMei_Object=MibScalar
h323DebugH323StackTraceModulesMei=_H323DebugH323StackTraceModulesMei_Object((1,3,6,1,4,1,4935,99,35,1,5,10,80),_H323DebugH323StackTraceModulesMei_Type())
h323DebugH323StackTraceModulesMei.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesMei.setStatus(_A)
class _H323DebugH323StackTraceModulesNamechan_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesNamechan_Type.__name__=_D
_H323DebugH323StackTraceModulesNamechan_Object=MibScalar
h323DebugH323StackTraceModulesNamechan=_H323DebugH323StackTraceModulesNamechan_Object((1,3,6,1,4,1,4935,99,35,1,5,10,85),_H323DebugH323StackTraceModulesNamechan_Type())
h323DebugH323StackTraceModulesNamechan.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesNamechan.setStatus(_A)
class _H323DebugH323StackTraceModulesPer_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesPer_Type.__name__=_D
_H323DebugH323StackTraceModulesPer_Object=MibScalar
h323DebugH323StackTraceModulesPer=_H323DebugH323StackTraceModulesPer_Object((1,3,6,1,4,1,4935,99,35,1,5,10,90),_H323DebugH323StackTraceModulesPer_Type())
h323DebugH323StackTraceModulesPer.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesPer.setStatus(_A)
class _H323DebugH323StackTraceModulesPererr_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesPererr_Type.__name__=_D
_H323DebugH323StackTraceModulesPererr_Object=MibScalar
h323DebugH323StackTraceModulesPererr=_H323DebugH323StackTraceModulesPererr_Object((1,3,6,1,4,1,4935,99,35,1,5,10,95),_H323DebugH323StackTraceModulesPererr_Type())
h323DebugH323StackTraceModulesPererr.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesPererr.setStatus(_A)
class _H323DebugH323StackTraceModulesPdlapi_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesPdlapi_Type.__name__=_D
_H323DebugH323StackTraceModulesPdlapi_Object=MibScalar
h323DebugH323StackTraceModulesPdlapi=_H323DebugH323StackTraceModulesPdlapi_Object((1,3,6,1,4,1,4935,99,35,1,5,10,100),_H323DebugH323StackTraceModulesPdlapi_Type())
h323DebugH323StackTraceModulesPdlapi.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesPdlapi.setStatus(_A)
class _H323DebugH323StackTraceModulesPdlchan_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesPdlchan_Type.__name__=_D
_H323DebugH323StackTraceModulesPdlchan_Object=MibScalar
h323DebugH323StackTraceModulesPdlchan=_H323DebugH323StackTraceModulesPdlchan_Object((1,3,6,1,4,1,4935,99,35,1,5,10,105),_H323DebugH323StackTraceModulesPdlchan_Type())
h323DebugH323StackTraceModulesPdlchan.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesPdlchan.setStatus(_A)
class _H323DebugH323StackTraceModulesPdlcomm_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesPdlcomm_Type.__name__=_D
_H323DebugH323StackTraceModulesPdlcomm_Object=MibScalar
h323DebugH323StackTraceModulesPdlcomm=_H323DebugH323StackTraceModulesPdlcomm_Object((1,3,6,1,4,1,4935,99,35,1,5,10,110),_H323DebugH323StackTraceModulesPdlcomm_Type())
h323DebugH323StackTraceModulesPdlcomm.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesPdlcomm.setStatus(_A)
class _H323DebugH323StackTraceModulesPdlconf_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesPdlconf_Type.__name__=_D
_H323DebugH323StackTraceModulesPdlconf_Object=MibScalar
h323DebugH323StackTraceModulesPdlconf=_H323DebugH323StackTraceModulesPdlconf_Object((1,3,6,1,4,1,4935,99,35,1,5,10,115),_H323DebugH323StackTraceModulesPdlconf_Type())
h323DebugH323StackTraceModulesPdlconf.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesPdlconf.setStatus(_A)
class _H323DebugH323StackTraceModulesPdlencode_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesPdlencode_Type.__name__=_D
_H323DebugH323StackTraceModulesPdlencode_Object=MibScalar
h323DebugH323StackTraceModulesPdlencode=_H323DebugH323StackTraceModulesPdlencode_Object((1,3,6,1,4,1,4935,99,35,1,5,10,120),_H323DebugH323StackTraceModulesPdlencode_Type())
h323DebugH323StackTraceModulesPdlencode.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesPdlencode.setStatus(_A)
class _H323DebugH323StackTraceModulesPdlerror_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesPdlerror_Type.__name__=_D
_H323DebugH323StackTraceModulesPdlerror_Object=MibScalar
h323DebugH323StackTraceModulesPdlerror=_H323DebugH323StackTraceModulesPdlerror_Object((1,3,6,1,4,1,4935,99,35,1,5,10,125),_H323DebugH323StackTraceModulesPdlerror_Type())
h323DebugH323StackTraceModulesPdlerror.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesPdlerror.setStatus(_A)
class _H323DebugH323StackTraceModulesPdlfnerr_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesPdlfnerr_Type.__name__=_D
_H323DebugH323StackTraceModulesPdlfnerr_Object=MibScalar
h323DebugH323StackTraceModulesPdlfnerr=_H323DebugH323StackTraceModulesPdlfnerr_Object((1,3,6,1,4,1,4935,99,35,1,5,10,130),_H323DebugH323StackTraceModulesPdlfnerr_Type())
h323DebugH323StackTraceModulesPdlfnerr.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesPdlfnerr.setStatus(_A)
class _H323DebugH323StackTraceModulesPdllist_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesPdllist_Type.__name__=_D
_H323DebugH323StackTraceModulesPdllist_Object=MibScalar
h323DebugH323StackTraceModulesPdllist=_H323DebugH323StackTraceModulesPdllist_Object((1,3,6,1,4,1,4935,99,35,1,5,10,135),_H323DebugH323StackTraceModulesPdllist_Type())
h323DebugH323StackTraceModulesPdllist.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesPdllist.setStatus(_A)
class _H323DebugH323StackTraceModulesPdlmisc_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesPdlmisc_Type.__name__=_D
_H323DebugH323StackTraceModulesPdlmisc_Object=MibScalar
h323DebugH323StackTraceModulesPdlmisc=_H323DebugH323StackTraceModulesPdlmisc_Object((1,3,6,1,4,1,4935,99,35,1,5,10,140),_H323DebugH323StackTraceModulesPdlmisc_Type())
h323DebugH323StackTraceModulesPdlmisc.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesPdlmisc.setStatus(_A)
class _H323DebugH323StackTraceModulesPdlmtask_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesPdlmtask_Type.__name__=_D
_H323DebugH323StackTraceModulesPdlmtask_Object=MibScalar
h323DebugH323StackTraceModulesPdlmtask=_H323DebugH323StackTraceModulesPdlmtask_Object((1,3,6,1,4,1,4935,99,35,1,5,10,145),_H323DebugH323StackTraceModulesPdlmtask_Type())
h323DebugH323StackTraceModulesPdlmtask.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesPdlmtask.setStatus(_A)
class _H323DebugH323StackTraceModulesPdlprint_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesPdlprint_Type.__name__=_D
_H323DebugH323StackTraceModulesPdlprint_Object=MibScalar
h323DebugH323StackTraceModulesPdlprint=_H323DebugH323StackTraceModulesPdlprint_Object((1,3,6,1,4,1,4935,99,35,1,5,10,150),_H323DebugH323StackTraceModulesPdlprint_Type())
h323DebugH323StackTraceModulesPdlprint.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesPdlprint.setStatus(_A)
class _H323DebugH323StackTraceModulesPdlprnerr_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesPdlprnerr_Type.__name__=_D
_H323DebugH323StackTraceModulesPdlprnerr_Object=MibScalar
h323DebugH323StackTraceModulesPdlprnerr=_H323DebugH323StackTraceModulesPdlprnerr_Object((1,3,6,1,4,1,4935,99,35,1,5,10,155),_H323DebugH323StackTraceModulesPdlprnerr_Type())
h323DebugH323StackTraceModulesPdlprnerr.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesPdlprnerr.setStatus(_A)
class _H323DebugH323StackTraceModulesPdlprnwrn_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesPdlprnwrn_Type.__name__=_D
_H323DebugH323StackTraceModulesPdlprnwrn_Object=MibScalar
h323DebugH323StackTraceModulesPdlprnwrn=_H323DebugH323StackTraceModulesPdlprnwrn_Object((1,3,6,1,4,1,4935,99,35,1,5,10,160),_H323DebugH323StackTraceModulesPdlprnwrn_Type())
h323DebugH323StackTraceModulesPdlprnwrn.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesPdlprnwrn.setStatus(_A)
class _H323DebugH323StackTraceModulesPdlsm_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesPdlsm_Type.__name__=_D
_H323DebugH323StackTraceModulesPdlsm_Object=MibScalar
h323DebugH323StackTraceModulesPdlsm=_H323DebugH323StackTraceModulesPdlsm_Object((1,3,6,1,4,1,4935,99,35,1,5,10,165),_H323DebugH323StackTraceModulesPdlsm_Type())
h323DebugH323StackTraceModulesPdlsm.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesPdlsm.setStatus(_A)
class _H323DebugH323StackTraceModulesPdlsrc_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesPdlsrc_Type.__name__=_D
_H323DebugH323StackTraceModulesPdlsrc_Object=MibScalar
h323DebugH323StackTraceModulesPdlsrc=_H323DebugH323StackTraceModulesPdlsrc_Object((1,3,6,1,4,1,4935,99,35,1,5,10,170),_H323DebugH323StackTraceModulesPdlsrc_Type())
h323DebugH323StackTraceModulesPdlsrc.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesPdlsrc.setStatus(_A)
class _H323DebugH323StackTraceModulesPdltimer_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesPdltimer_Type.__name__=_D
_H323DebugH323StackTraceModulesPdltimer_Object=MibScalar
h323DebugH323StackTraceModulesPdltimer=_H323DebugH323StackTraceModulesPdltimer_Object((1,3,6,1,4,1,4935,99,35,1,5,10,175),_H323DebugH323StackTraceModulesPdltimer_Type())
h323DebugH323StackTraceModulesPdltimer.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesPdltimer.setStatus(_A)
class _H323DebugH323StackTraceModulesPi_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesPi_Type.__name__=_D
_H323DebugH323StackTraceModulesPi_Object=MibScalar
h323DebugH323StackTraceModulesPi=_H323DebugH323StackTraceModulesPi_Object((1,3,6,1,4,1,4935,99,35,1,5,10,180),_H323DebugH323StackTraceModulesPi_Type())
h323DebugH323StackTraceModulesPi.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesPi.setStatus(_A)
class _H323DebugH323StackTraceModulesQ931_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesQ931_Type.__name__=_D
_H323DebugH323StackTraceModulesQ931_Object=MibScalar
h323DebugH323StackTraceModulesQ931=_H323DebugH323StackTraceModulesQ931_Object((1,3,6,1,4,1,4935,99,35,1,5,10,185),_H323DebugH323StackTraceModulesQ931_Type())
h323DebugH323StackTraceModulesQ931.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesQ931.setStatus(_A)
class _H323DebugH323StackTraceModulesQ931err_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesQ931err_Type.__name__=_D
_H323DebugH323StackTraceModulesQ931err_Object=MibScalar
h323DebugH323StackTraceModulesQ931err=_H323DebugH323StackTraceModulesQ931err_Object((1,3,6,1,4,1,4935,99,35,1,5,10,190),_H323DebugH323StackTraceModulesQ931err_Type())
h323DebugH323StackTraceModulesQ931err.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesQ931err.setStatus(_A)
class _H323DebugH323StackTraceModulesRa_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesRa_Type.__name__=_D
_H323DebugH323StackTraceModulesRa_Object=MibScalar
h323DebugH323StackTraceModulesRa=_H323DebugH323StackTraceModulesRa_Object((1,3,6,1,4,1,4935,99,35,1,5,10,195),_H323DebugH323StackTraceModulesRa_Type())
h323DebugH323StackTraceModulesRa.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesRa.setStatus(_A)
class _H323DebugH323StackTraceModulesRasctrl_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesRasctrl_Type.__name__=_D
_H323DebugH323StackTraceModulesRasctrl_Object=MibScalar
h323DebugH323StackTraceModulesRasctrl=_H323DebugH323StackTraceModulesRasctrl_Object((1,3,6,1,4,1,4935,99,35,1,5,10,200),_H323DebugH323StackTraceModulesRasctrl_Type())
h323DebugH323StackTraceModulesRasctrl.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesRasctrl.setStatus(_A)
class _H323DebugH323StackTraceModulesRasindb_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesRasindb_Type.__name__=_D
_H323DebugH323StackTraceModulesRasindb_Object=MibScalar
h323DebugH323StackTraceModulesRasindb=_H323DebugH323StackTraceModulesRasindb_Object((1,3,6,1,4,1,4935,99,35,1,5,10,205),_H323DebugH323StackTraceModulesRasindb_Type())
h323DebugH323StackTraceModulesRasindb.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesRasindb.setStatus(_A)
class _H323DebugH323StackTraceModulesSeli_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesSeli_Type.__name__=_D
_H323DebugH323StackTraceModulesSeli_Object=MibScalar
h323DebugH323StackTraceModulesSeli=_H323DebugH323StackTraceModulesSeli_Object((1,3,6,1,4,1,4935,99,35,1,5,10,210),_H323DebugH323StackTraceModulesSeli_Type())
h323DebugH323StackTraceModulesSeli.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesSeli.setStatus(_A)
class _H323DebugH323StackTraceModulesSsapi_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesSsapi_Type.__name__=_D
_H323DebugH323StackTraceModulesSsapi_Object=MibScalar
h323DebugH323StackTraceModulesSsapi=_H323DebugH323StackTraceModulesSsapi_Object((1,3,6,1,4,1,4935,99,35,1,5,10,215),_H323DebugH323StackTraceModulesSsapi_Type())
h323DebugH323StackTraceModulesSsapi.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesSsapi.setStatus(_A)
class _H323DebugH323StackTraceModulesSsapicb_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesSsapicb_Type.__name__=_D
_H323DebugH323StackTraceModulesSsapicb_Object=MibScalar
h323DebugH323StackTraceModulesSsapicb=_H323DebugH323StackTraceModulesSsapicb_Object((1,3,6,1,4,1,4935,99,35,1,5,10,220),_H323DebugH323StackTraceModulesSsapicb_Type())
h323DebugH323StackTraceModulesSsapicb.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesSsapicb.setStatus(_A)
class _H323DebugH323StackTraceModulesSschan_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesSschan_Type.__name__=_D
_H323DebugH323StackTraceModulesSschan_Object=MibScalar
h323DebugH323StackTraceModulesSschan=_H323DebugH323StackTraceModulesSschan_Object((1,3,6,1,4,1,4935,99,35,1,5,10,225),_H323DebugH323StackTraceModulesSschan_Type())
h323DebugH323StackTraceModulesSschan.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesSschan.setStatus(_A)
class _H323DebugH323StackTraceModulesSseapi_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesSseapi_Type.__name__=_D
_H323DebugH323StackTraceModulesSseapi_Object=MibScalar
h323DebugH323StackTraceModulesSseapi=_H323DebugH323StackTraceModulesSseapi_Object((1,3,6,1,4,1,4935,99,35,1,5,10,230),_H323DebugH323StackTraceModulesSseapi_Type())
h323DebugH323StackTraceModulesSseapi.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesSseapi.setStatus(_A)
class _H323DebugH323StackTraceModulesSseapicb_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesSseapicb_Type.__name__=_D
_H323DebugH323StackTraceModulesSseapicb_Object=MibScalar
h323DebugH323StackTraceModulesSseapicb=_H323DebugH323StackTraceModulesSseapicb_Object((1,3,6,1,4,1,4935,99,35,1,5,10,235),_H323DebugH323StackTraceModulesSseapicb_Type())
h323DebugH323StackTraceModulesSseapicb.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesSseapicb.setStatus(_A)
class _H323DebugH323StackTraceModulesSsechan_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesSsechan_Type.__name__=_D
_H323DebugH323StackTraceModulesSsechan_Object=MibScalar
h323DebugH323StackTraceModulesSsechan=_H323DebugH323StackTraceModulesSsechan_Object((1,3,6,1,4,1,4935,99,35,1,5,10,240),_H323DebugH323StackTraceModulesSsechan_Type())
h323DebugH323StackTraceModulesSsechan.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesSsechan.setStatus(_A)
class _H323DebugH323StackTraceModulesSseerr_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesSseerr_Type.__name__=_D
_H323DebugH323StackTraceModulesSseerr_Object=MibScalar
h323DebugH323StackTraceModulesSseerr=_H323DebugH323StackTraceModulesSseerr_Object((1,3,6,1,4,1,4935,99,35,1,5,10,245),_H323DebugH323StackTraceModulesSseerr_Type())
h323DebugH323StackTraceModulesSseerr.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesSseerr.setStatus(_A)
class _H323DebugH323StackTraceModulesSserr_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesSserr_Type.__name__=_D
_H323DebugH323StackTraceModulesSserr_Object=MibScalar
h323DebugH323StackTraceModulesSserr=_H323DebugH323StackTraceModulesSserr_Object((1,3,6,1,4,1,4935,99,35,1,5,10,250),_H323DebugH323StackTraceModulesSserr_Type())
h323DebugH323StackTraceModulesSserr.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesSserr.setStatus(_A)
class _H323DebugH323StackTraceModulesTimer_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesTimer_Type.__name__=_D
_H323DebugH323StackTraceModulesTimer_Object=MibScalar
h323DebugH323StackTraceModulesTimer=_H323DebugH323StackTraceModulesTimer_Object((1,3,6,1,4,1,4935,99,35,1,5,10,255),_H323DebugH323StackTraceModulesTimer_Type())
h323DebugH323StackTraceModulesTimer.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesTimer.setStatus(_A)
class _H323DebugH323StackTraceModulesTpktchan_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesTpktchan_Type.__name__=_D
_H323DebugH323StackTraceModulesTpktchan_Object=MibScalar
h323DebugH323StackTraceModulesTpktchan=_H323DebugH323StackTraceModulesTpktchan_Object((1,3,6,1,4,1,4935,99,35,1,5,10,260),_H323DebugH323StackTraceModulesTpktchan_Type())
h323DebugH323StackTraceModulesTpktchan.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesTpktchan.setStatus(_A)
class _H323DebugH323StackTraceModulesTransport_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesTransport_Type.__name__=_D
_H323DebugH323StackTraceModulesTransport_Object=MibScalar
h323DebugH323StackTraceModulesTransport=_H323DebugH323StackTraceModulesTransport_Object((1,3,6,1,4,1,4935,99,35,1,5,10,265),_H323DebugH323StackTraceModulesTransport_Type())
h323DebugH323StackTraceModulesTransport.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesTransport.setStatus(_A)
class _H323DebugH323StackTraceModulesTunnctrl_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesTunnctrl_Type.__name__=_D
_H323DebugH323StackTraceModulesTunnctrl_Object=MibScalar
h323DebugH323StackTraceModulesTunnctrl=_H323DebugH323StackTraceModulesTunnctrl_Object((1,3,6,1,4,1,4935,99,35,1,5,10,270),_H323DebugH323StackTraceModulesTunnctrl_Type())
h323DebugH323StackTraceModulesTunnctrl.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesTunnctrl.setStatus(_A)
class _H323DebugH323StackTraceModulesUdpchan_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesUdpchan_Type.__name__=_D
_H323DebugH323StackTraceModulesUdpchan_Object=MibScalar
h323DebugH323StackTraceModulesUdpchan=_H323DebugH323StackTraceModulesUdpchan_Object((1,3,6,1,4,1,4935,99,35,1,5,10,275),_H323DebugH323StackTraceModulesUdpchan_Type())
h323DebugH323StackTraceModulesUdpchan.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesUdpchan.setStatus(_A)
class _H323DebugH323StackTraceModulesUnreg_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesUnreg_Type.__name__=_D
_H323DebugH323StackTraceModulesUnreg_Object=MibScalar
h323DebugH323StackTraceModulesUnreg=_H323DebugH323StackTraceModulesUnreg_Object((1,3,6,1,4,1,4935,99,35,1,5,10,280),_H323DebugH323StackTraceModulesUnreg_Type())
h323DebugH323StackTraceModulesUnreg.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesUnreg.setStatus(_A)
class _H323DebugH323StackTraceModulesVt_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTraceModulesVt_Type.__name__=_D
_H323DebugH323StackTraceModulesVt_Object=MibScalar
h323DebugH323StackTraceModulesVt=_H323DebugH323StackTraceModulesVt_Object((1,3,6,1,4,1,4935,99,35,1,5,10,285),_H323DebugH323StackTraceModulesVt_Type())
h323DebugH323StackTraceModulesVt.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTraceModulesVt.setStatus(_A)
_H323DebugSupplementaryTrace_ObjectIdentity=ObjectIdentity
h323DebugSupplementaryTrace=_H323DebugSupplementaryTrace_ObjectIdentity((1,3,6,1,4,1,4935,99,35,1,10))
class _H323DebugSuppTraceEngineProvision_Type(MxEnableState):defaultValue=0
_H323DebugSuppTraceEngineProvision_Type.__name__=_D
_H323DebugSuppTraceEngineProvision_Object=MibScalar
h323DebugSuppTraceEngineProvision=_H323DebugSuppTraceEngineProvision_Object((1,3,6,1,4,1,4935,99,35,1,10,5),_H323DebugSuppTraceEngineProvision_Type())
h323DebugSuppTraceEngineProvision.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugSuppTraceEngineProvision.setStatus(_A)
class _H323DebugSuppTraceMediaProvision_Type(MxEnableState):defaultValue=0
_H323DebugSuppTraceMediaProvision_Type.__name__=_D
_H323DebugSuppTraceMediaProvision_Object=MibScalar
h323DebugSuppTraceMediaProvision=_H323DebugSuppTraceMediaProvision_Object((1,3,6,1,4,1,4935,99,35,1,10,15),_H323DebugSuppTraceMediaProvision_Type())
h323DebugSuppTraceMediaProvision.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugSuppTraceMediaProvision.setStatus(_A)
class _H323DebugSuppTraceDebugProvision_Type(MxEnableState):defaultValue=0
_H323DebugSuppTraceDebugProvision_Type.__name__=_D
_H323DebugSuppTraceDebugProvision_Object=MibScalar
h323DebugSuppTraceDebugProvision=_H323DebugSuppTraceDebugProvision_Object((1,3,6,1,4,1,4935,99,35,1,10,20),_H323DebugSuppTraceDebugProvision_Type())
h323DebugSuppTraceDebugProvision.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugSuppTraceDebugProvision.setStatus(_A)
class _H323DebugSuppTraceGkReg_Type(MxEnableState):defaultValue=0
_H323DebugSuppTraceGkReg_Type.__name__=_D
_H323DebugSuppTraceGkReg_Object=MibScalar
h323DebugSuppTraceGkReg=_H323DebugSuppTraceGkReg_Object((1,3,6,1,4,1,4935,99,35,1,10,25),_H323DebugSuppTraceGkReg_Type())
h323DebugSuppTraceGkReg.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugSuppTraceGkReg.setStatus(_A)
_H323DebugH323StackTrace2_ObjectIdentity=ObjectIdentity
h323DebugH323StackTrace2=_H323DebugH323StackTrace2_ObjectIdentity((1,3,6,1,4,1,4935,99,35,1,15))
class _H323DebugH323StackTrace2Enable_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTrace2Enable_Type.__name__=_D
_H323DebugH323StackTrace2Enable_Object=MibScalar
h323DebugH323StackTrace2Enable=_H323DebugH323StackTrace2Enable_Object((1,3,6,1,4,1,4935,99,35,1,15,5),_H323DebugH323StackTrace2Enable_Type())
h323DebugH323StackTrace2Enable.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTrace2Enable.setStatus(_A)
class _H323DebugH323StackTrace2ContentEnable_Type(MxEnableState):defaultValue=0
_H323DebugH323StackTrace2ContentEnable_Type.__name__=_D
_H323DebugH323StackTrace2ContentEnable_Object=MibScalar
h323DebugH323StackTrace2ContentEnable=_H323DebugH323StackTrace2ContentEnable_Object((1,3,6,1,4,1,4935,99,35,1,15,10),_H323DebugH323StackTrace2ContentEnable_Type())
h323DebugH323StackTrace2ContentEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTrace2ContentEnable.setStatus(_A)
class _H323DebugH323StackTrace2GeneralLevel_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),(_G,1),('error',2),(_H,3)))
_H323DebugH323StackTrace2GeneralLevel_Type.__name__=_E
_H323DebugH323StackTrace2GeneralLevel_Object=MibScalar
h323DebugH323StackTrace2GeneralLevel=_H323DebugH323StackTrace2GeneralLevel_Object((1,3,6,1,4,1,4935,99,35,1,15,15),_H323DebugH323StackTrace2GeneralLevel_Type())
h323DebugH323StackTrace2GeneralLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTrace2GeneralLevel.setStatus(_A)
_H323DebugH323StackTrace2ModuleTable_Object=MibTable
h323DebugH323StackTrace2ModuleTable=_H323DebugH323StackTrace2ModuleTable_Object((1,3,6,1,4,1,4935,99,35,1,15,20))
if mibBuilder.loadTexts:h323DebugH323StackTrace2ModuleTable.setStatus(_A)
_H323DebugH323StackTrace2ModuleEntry_Object=MibTableRow
h323DebugH323StackTrace2ModuleEntry=_H323DebugH323StackTrace2ModuleEntry_Object((1,3,6,1,4,1,4935,99,35,1,15,20,1))
h323DebugH323StackTrace2ModuleEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:h323DebugH323StackTrace2ModuleEntry.setStatus(_A)
_H323DebugH323StackTrace2ModuleIndex_Type=Unsigned32
_H323DebugH323StackTrace2ModuleIndex_Object=MibTableColumn
h323DebugH323StackTrace2ModuleIndex=_H323DebugH323StackTrace2ModuleIndex_Object((1,3,6,1,4,1,4935,99,35,1,15,20,1,5),_H323DebugH323StackTrace2ModuleIndex_Type())
h323DebugH323StackTrace2ModuleIndex.setMaxAccess('read-only')
if mibBuilder.loadTexts:h323DebugH323StackTrace2ModuleIndex.setStatus(_A)
class _H323DebugH323StackTrace2Module_Type(Integer32):defaultValue=99;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,99)));namedValues=NamedValues(*(('annexe',0),('appl',1),('ares',2),('cat',3),('ci',4),('cm',5),('cmapi',6),('cmapicb',7),('cmerr',8),('config',9),('ema',10),('faststart',11),('h245',12),('host',13),('lock',14),('memory',15),('mti',16),('mutex',17),('per',18),('pererr',19),('port',20),('q931',21),('q931err',22),('queue',23),('ra',24),('ras',25),('sec',26),('select',27),('sema4',28),('socket',29),('ssapi',30),('ssapicb',31),('sschan',32),('sseapi',33),('sseapicb',34),('sseerr',35),('sserr',36),('sups',37),('tcp',38),('thread',39),('timepool',40),('timestamp',41),('tls',42),('tm',43),('tpktchan',44),('tpktwire',45),('transport',46),('udpchan',47),('udpwire',48),('unreg',49),('vt',50),('watchdog',51),('moduleDisabled',99)))
_H323DebugH323StackTrace2Module_Type.__name__=_E
_H323DebugH323StackTrace2Module_Object=MibTableColumn
h323DebugH323StackTrace2Module=_H323DebugH323StackTrace2Module_Object((1,3,6,1,4,1,4935,99,35,1,15,20,1,10),_H323DebugH323StackTrace2Module_Type())
h323DebugH323StackTrace2Module.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTrace2Module.setStatus(_A)
class _H323DebugH323StackTrace2Level_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_F,0),(_G,1),('error',2),(_H,3),('informational',4),('debug',5),('function',6)))
_H323DebugH323StackTrace2Level_Type.__name__=_E
_H323DebugH323StackTrace2Level_Object=MibTableColumn
h323DebugH323StackTrace2Level=_H323DebugH323StackTrace2Level_Object((1,3,6,1,4,1,4935,99,35,1,15,20,1,15),_H323DebugH323StackTrace2Level_Type())
h323DebugH323StackTrace2Level.setMaxAccess(_C)
if mibBuilder.loadTexts:h323DebugH323StackTrace2Level.setStatus(_A)
_H323DebugConformance_ObjectIdentity=ObjectIdentity
h323DebugConformance=_H323DebugConformance_ObjectIdentity((1,3,6,1,4,1,4935,99,35,2))
_H323DebugCompliances_ObjectIdentity=ObjectIdentity
h323DebugCompliances=_H323DebugCompliances_ObjectIdentity((1,3,6,1,4,1,4935,99,35,2,1))
_H323DebugGroups_ObjectIdentity=ObjectIdentity
h323DebugGroups=_H323DebugGroups_ObjectIdentity((1,3,6,1,4,1,4935,99,35,2,2))
h323DebugH323StackTraceGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,99,35,2,2,5))
h323DebugH323StackTraceGroupVer1.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE)))
if mibBuilder.loadTexts:h323DebugH323StackTraceGroupVer1.setStatus(_A)
h323DebugH323StackTrace2GroupVer1=ObjectGroup((1,3,6,1,4,1,4935,99,35,2,2,10))
h323DebugH323StackTrace2GroupVer1.setObjects(*((_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:h323DebugH323StackTrace2GroupVer1.setStatus(_A)
h323DebugH323SupplementaryTraceGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,99,35,2,2,15))
h323DebugH323SupplementaryTraceGroupVer1.setObjects(*((_B,_AK),(_B,_AL),(_B,_AM),(_B,_AN)))
if mibBuilder.loadTexts:h323DebugH323SupplementaryTraceGroupVer1.setStatus(_A)
h323DebugBasicComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,99,35,2,1,5))
h323DebugBasicComplVer1.setObjects(*((_B,_AO),(_B,_AP),(_B,_AQ)))
if mibBuilder.loadTexts:h323DebugBasicComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h323DebugMIB':h323DebugMIB,'h323DebugMIBObjects':h323DebugMIBObjects,'h323DebugH323StackTrace':h323DebugH323StackTrace,_J:h323DebugH323StackTraceLevel,'h323DebugH323StackTraceModules':h323DebugH323StackTraceModules,_K:h323DebugH323StackTraceModulesAnnexE,_L:h323DebugH323StackTraceModulesCa,_M:h323DebugH323StackTraceModulesCaerr,_N:h323DebugH323StackTraceModulesChannels,_O:h323DebugH323StackTraceModulesCm,_P:h323DebugH323StackTraceModulesCmapi,_Q:h323DebugH323StackTraceModulesCmapicb,_R:h323DebugH323StackTraceModulesCmerr,_S:h323DebugH323StackTraceModulesDebug,_T:h323DebugH323StackTraceModulesEfrm,_U:h323DebugH323StackTraceModulesEtimer,_V:h323DebugH323StackTraceModulesEtimerheap,_W:h323DebugH323StackTraceModulesH450apdu,_X:h323DebugH323StackTraceModulesLi,_Y:h323DebugH323StackTraceModulesLiinfo,_Z:h323DebugH323StackTraceModulesMei,_a:h323DebugH323StackTraceModulesNamechan,_b:h323DebugH323StackTraceModulesPer,_c:h323DebugH323StackTraceModulesPererr,_d:h323DebugH323StackTraceModulesPdlapi,_e:h323DebugH323StackTraceModulesPdlchan,_f:h323DebugH323StackTraceModulesPdlcomm,_g:h323DebugH323StackTraceModulesPdlconf,_h:h323DebugH323StackTraceModulesPdlencode,_i:h323DebugH323StackTraceModulesPdlerror,_j:h323DebugH323StackTraceModulesPdlfnerr,_k:h323DebugH323StackTraceModulesPdllist,_l:h323DebugH323StackTraceModulesPdlmisc,_m:h323DebugH323StackTraceModulesPdlmtask,_n:h323DebugH323StackTraceModulesPdlprint,_o:h323DebugH323StackTraceModulesPdlprnerr,_p:h323DebugH323StackTraceModulesPdlprnwrn,_q:h323DebugH323StackTraceModulesPdlsm,_r:h323DebugH323StackTraceModulesPdlsrc,_s:h323DebugH323StackTraceModulesPdltimer,_t:h323DebugH323StackTraceModulesPi,_u:h323DebugH323StackTraceModulesQ931,_v:h323DebugH323StackTraceModulesQ931err,_w:h323DebugH323StackTraceModulesRa,_x:h323DebugH323StackTraceModulesRasctrl,_y:h323DebugH323StackTraceModulesRasindb,_z:h323DebugH323StackTraceModulesSeli,_A0:h323DebugH323StackTraceModulesSsapi,_A1:h323DebugH323StackTraceModulesSsapicb,_A2:h323DebugH323StackTraceModulesSschan,_A3:h323DebugH323StackTraceModulesSseapi,_A4:h323DebugH323StackTraceModulesSseapicb,_A5:h323DebugH323StackTraceModulesSsechan,_A6:h323DebugH323StackTraceModulesSseerr,_A7:h323DebugH323StackTraceModulesSserr,_A8:h323DebugH323StackTraceModulesTimer,_A9:h323DebugH323StackTraceModulesTpktchan,_AA:h323DebugH323StackTraceModulesTransport,_AB:h323DebugH323StackTraceModulesTunnctrl,_AC:h323DebugH323StackTraceModulesUdpchan,_AD:h323DebugH323StackTraceModulesUnreg,_AE:h323DebugH323StackTraceModulesVt,'h323DebugSupplementaryTrace':h323DebugSupplementaryTrace,_AK:h323DebugSuppTraceEngineProvision,_AL:h323DebugSuppTraceMediaProvision,_AM:h323DebugSuppTraceDebugProvision,_AN:h323DebugSuppTraceGkReg,'h323DebugH323StackTrace2':h323DebugH323StackTrace2,_AF:h323DebugH323StackTrace2Enable,_AG:h323DebugH323StackTrace2ContentEnable,_AH:h323DebugH323StackTrace2GeneralLevel,'h323DebugH323StackTrace2ModuleTable':h323DebugH323StackTrace2ModuleTable,'h323DebugH323StackTrace2ModuleEntry':h323DebugH323StackTrace2ModuleEntry,_I:h323DebugH323StackTrace2ModuleIndex,_AI:h323DebugH323StackTrace2Module,_AJ:h323DebugH323StackTrace2Level,'h323DebugConformance':h323DebugConformance,'h323DebugCompliances':h323DebugCompliances,'h323DebugBasicComplVer1':h323DebugBasicComplVer1,'h323DebugGroups':h323DebugGroups,_AO:h323DebugH323StackTraceGroupVer1,_AP:h323DebugH323StackTrace2GroupVer1,_AQ:h323DebugH323SupplementaryTraceGroupVer1})