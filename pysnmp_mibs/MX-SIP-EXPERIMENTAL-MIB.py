_O='sipExperimentalGroupVer1'
_N='sipAllowAudioAndImageNegotiationEnable'
_M='sipAllowMediaReactivationInAnswerEnable'
_L='sipRtpUdpChecksumEnable'
_K='sipEnforceOfferAnswerModel'
_J='sipOutboundProxyConfig'
_I='sipUnregisteredPortBehavior'
_H='sipNatCustomPublicAddress'
_G='sipNatCustomEnable'
_F='MxIpHostName'
_E='Integer32'
_D='MxEnableState'
_C='read-write'
_B='MX-SIP-EXPERIMENTAL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixExperimental,=mibBuilder.importSymbols('MX-SMI','mediatrixExperimental')
MxEnableState,MxIpHostName=mibBuilder.importSymbols('MX-TC',_D,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
sipExperimentalMIB=ModuleIdentity((1,3,6,1,4,1,4935,99,10))
if mibBuilder.loadTexts:sipExperimentalMIB.setRevisions(('2009-08-17 00:00','2008-04-03 00:00','2007-10-31 00:00','2006-02-28 00:00','2003-04-30 00:00','2003-03-11 00:00','2003-01-23 00:00','2002-12-17 00:00','2002-12-02 00:00','2002-07-05 00:00','2002-02-13 00:00'))
_SipExperimentalMIBObjects_ObjectIdentity=ObjectIdentity
sipExperimentalMIBObjects=_SipExperimentalMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,99,10,1))
_SipNatCustom_ObjectIdentity=ObjectIdentity
sipNatCustom=_SipNatCustom_ObjectIdentity((1,3,6,1,4,1,4935,99,10,1,5))
class _SipNatCustomEnable_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_SipNatCustomEnable_Type.__name__=_E
_SipNatCustomEnable_Object=MibScalar
sipNatCustomEnable=_SipNatCustomEnable_Object((1,3,6,1,4,1,4935,99,10,1,5,5),_SipNatCustomEnable_Type())
sipNatCustomEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:sipNatCustomEnable.setStatus(_A)
class _SipNatCustomPublicAddress_Type(MxIpHostName):defaultValue=OctetString('0.0.0.0')
_SipNatCustomPublicAddress_Type.__name__=_F
_SipNatCustomPublicAddress_Object=MibScalar
sipNatCustomPublicAddress=_SipNatCustomPublicAddress_Object((1,3,6,1,4,1,4935,99,10,1,5,10),_SipNatCustomPublicAddress_Type())
sipNatCustomPublicAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:sipNatCustomPublicAddress.setStatus(_A)
class _SipUnregisteredPortBehavior_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disablePort',0),('enablePort',1)))
_SipUnregisteredPortBehavior_Type.__name__=_E
_SipUnregisteredPortBehavior_Object=MibScalar
sipUnregisteredPortBehavior=_SipUnregisteredPortBehavior_Object((1,3,6,1,4,1,4935,99,10,1,25),_SipUnregisteredPortBehavior_Type())
sipUnregisteredPortBehavior.setMaxAccess(_C)
if mibBuilder.loadTexts:sipUnregisteredPortBehavior.setStatus(_A)
class _SipOutboundProxyConfig_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('looseRouter',0),('strictRouter',1)))
_SipOutboundProxyConfig_Type.__name__=_E
_SipOutboundProxyConfig_Object=MibScalar
sipOutboundProxyConfig=_SipOutboundProxyConfig_Object((1,3,6,1,4,1,4935,99,10,1,30),_SipOutboundProxyConfig_Type())
sipOutboundProxyConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:sipOutboundProxyConfig.setStatus(_A)
class _SipEnforceOfferAnswerModel_Type(MxEnableState):defaultValue=1
_SipEnforceOfferAnswerModel_Type.__name__=_D
_SipEnforceOfferAnswerModel_Object=MibScalar
sipEnforceOfferAnswerModel=_SipEnforceOfferAnswerModel_Object((1,3,6,1,4,1,4935,99,10,1,80),_SipEnforceOfferAnswerModel_Type())
sipEnforceOfferAnswerModel.setMaxAccess(_C)
if mibBuilder.loadTexts:sipEnforceOfferAnswerModel.setStatus(_A)
class _SipAllowMediaReactivationInAnswerEnable_Type(MxEnableState):defaultValue=0
_SipAllowMediaReactivationInAnswerEnable_Type.__name__=_D
_SipAllowMediaReactivationInAnswerEnable_Object=MibScalar
sipAllowMediaReactivationInAnswerEnable=_SipAllowMediaReactivationInAnswerEnable_Object((1,3,6,1,4,1,4935,99,10,1,85),_SipAllowMediaReactivationInAnswerEnable_Type())
sipAllowMediaReactivationInAnswerEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:sipAllowMediaReactivationInAnswerEnable.setStatus(_A)
class _SipAllowAudioAndImageNegotiationEnable_Type(MxEnableState):defaultValue=0
_SipAllowAudioAndImageNegotiationEnable_Type.__name__=_D
_SipAllowAudioAndImageNegotiationEnable_Object=MibScalar
sipAllowAudioAndImageNegotiationEnable=_SipAllowAudioAndImageNegotiationEnable_Object((1,3,6,1,4,1,4935,99,10,1,90),_SipAllowAudioAndImageNegotiationEnable_Type())
sipAllowAudioAndImageNegotiationEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:sipAllowAudioAndImageNegotiationEnable.setStatus(_A)
class _SipCodecOrderInAnswer_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('localOrder',0),('offerOrder',1)))
_SipCodecOrderInAnswer_Type.__name__=_E
_SipCodecOrderInAnswer_Object=MibScalar
sipCodecOrderInAnswer=_SipCodecOrderInAnswer_Object((1,3,6,1,4,1,4935,99,10,1,95),_SipCodecOrderInAnswer_Type())
sipCodecOrderInAnswer.setMaxAccess(_C)
if mibBuilder.loadTexts:sipCodecOrderInAnswer.setStatus(_A)
class _SipRtpUdpChecksumEnable_Type(MxEnableState):defaultValue=0
_SipRtpUdpChecksumEnable_Type.__name__=_D
_SipRtpUdpChecksumEnable_Object=MibScalar
sipRtpUdpChecksumEnable=_SipRtpUdpChecksumEnable_Object((1,3,6,1,4,1,4935,99,10,1,130),_SipRtpUdpChecksumEnable_Type())
sipRtpUdpChecksumEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:sipRtpUdpChecksumEnable.setStatus(_A)
_SipExperimentalConformance_ObjectIdentity=ObjectIdentity
sipExperimentalConformance=_SipExperimentalConformance_ObjectIdentity((1,3,6,1,4,1,4935,99,10,2))
_SipExperimentalCompliances_ObjectIdentity=ObjectIdentity
sipExperimentalCompliances=_SipExperimentalCompliances_ObjectIdentity((1,3,6,1,4,1,4935,99,10,2,1))
_SipExperimentalGroups_ObjectIdentity=ObjectIdentity
sipExperimentalGroups=_SipExperimentalGroups_ObjectIdentity((1,3,6,1,4,1,4935,99,10,2,2))
sipExperimentalGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,99,10,2,2,5))
sipExperimentalGroupVer1.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:sipExperimentalGroupVer1.setStatus(_A)
sipExperimentalBasicComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,99,10,2,1,1))
sipExperimentalBasicComplVer1.setObjects((_B,_O))
if mibBuilder.loadTexts:sipExperimentalBasicComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'sipExperimentalMIB':sipExperimentalMIB,'sipExperimentalMIBObjects':sipExperimentalMIBObjects,'sipNatCustom':sipNatCustom,_G:sipNatCustomEnable,_H:sipNatCustomPublicAddress,_I:sipUnregisteredPortBehavior,_J:sipOutboundProxyConfig,_K:sipEnforceOfferAnswerModel,_M:sipAllowMediaReactivationInAnswerEnable,_N:sipAllowAudioAndImageNegotiationEnable,'sipCodecOrderInAnswer':sipCodecOrderInAnswer,_L:sipRtpUdpChecksumEnable,'sipExperimentalConformance':sipExperimentalConformance,'sipExperimentalCompliances':sipExperimentalCompliances,'sipExperimentalBasicComplVer1':sipExperimentalBasicComplVer1,'sipExperimentalGroups':sipExperimentalGroups,_O:sipExperimentalGroupVer1})