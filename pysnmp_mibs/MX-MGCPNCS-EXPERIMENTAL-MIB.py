_T='mgcpncsExperimentalGroupVer1'
_S='mgcpncsPolarityReversalOnCallingCardServiceToneEnable'
_R='mgcpncsBracketsAroundIpAddressInDomainNameEnable'
_Q='mgcpncsUseItuT38Format'
_P='mgcpncsFakeRfc3407Recognition'
_O='mgcpncsMakeOsiSignalBrief'
_N='mgcpncsImmediateModemToneReporting'
_M='mgcpncsT38CapabilitiesUsingAudioCodec98'
_L='mgcpncsRtpUdpChecksumEnable'
_K='mgcpncsConnectRtpSockets'
_J='mgcpncsMultipleFaxToneDetection'
_I='mgcpncsValidateOfferAnswerModel'
_H='mgcpncsG729AnnexBNegotiation'
_G='mgcpncsOriginLineSessionIDAndVersionMaxLength'
_F='mgcpncsAnswerStreamFormat'
_E='Integer32'
_D='MxEnableState'
_C='read-write'
_B='MX-MGCPNCS-EXPERIMENTAL-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
mediatrixExperimental,=mibBuilder.importSymbols('MX-SMI','mediatrixExperimental')
MxEnableState,=mibBuilder.importSymbols('MX-TC',_D)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mgcpncsExperimentalMIB=ModuleIdentity((1,3,6,1,4,1,4935,99,100))
if mibBuilder.loadTexts:mgcpncsExperimentalMIB.setRevisions(('2010-08-18 00:00','2009-03-17 00:00','2008-06-13 00:00','2006-06-09 00:00','2006-05-04 00:00','2005-10-17 00:00','2005-04-18 00:00','2005-03-07 00:00','2004-11-08 00:00'))
_MgcpncsExperimentalMIBObjects_ObjectIdentity=ObjectIdentity
mgcpncsExperimentalMIBObjects=_MgcpncsExperimentalMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,99,100,1))
_MgcpncsInterop_ObjectIdentity=ObjectIdentity
mgcpncsInterop=_MgcpncsInterop_ObjectIdentity((1,3,6,1,4,1,4935,99,100,1,5))
class _MgcpncsAnswerStreamFormat_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,10)));namedValues=NamedValues(*(('zeroAnswerStream',1),('removeAnswerStream',10)))
_MgcpncsAnswerStreamFormat_Type.__name__=_E
_MgcpncsAnswerStreamFormat_Object=MibScalar
mgcpncsAnswerStreamFormat=_MgcpncsAnswerStreamFormat_Object((1,3,6,1,4,1,4935,99,100,1,5,5),_MgcpncsAnswerStreamFormat_Type())
mgcpncsAnswerStreamFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpncsAnswerStreamFormat.setStatus(_A)
class _MgcpncsOriginLineSessionIDAndVersionMaxLength_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,10,20)));namedValues=NamedValues(*(('none',1),('max-32bits',10),('max-64bits',20)))
_MgcpncsOriginLineSessionIDAndVersionMaxLength_Type.__name__=_E
_MgcpncsOriginLineSessionIDAndVersionMaxLength_Object=MibScalar
mgcpncsOriginLineSessionIDAndVersionMaxLength=_MgcpncsOriginLineSessionIDAndVersionMaxLength_Object((1,3,6,1,4,1,4935,99,100,1,5,10),_MgcpncsOriginLineSessionIDAndVersionMaxLength_Type())
mgcpncsOriginLineSessionIDAndVersionMaxLength.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpncsOriginLineSessionIDAndVersionMaxLength.setStatus(_A)
class _MgcpncsG729AnnexBNegotiation_Type(MxEnableState):defaultValue=0
_MgcpncsG729AnnexBNegotiation_Type.__name__=_D
_MgcpncsG729AnnexBNegotiation_Object=MibScalar
mgcpncsG729AnnexBNegotiation=_MgcpncsG729AnnexBNegotiation_Object((1,3,6,1,4,1,4935,99,100,1,5,15),_MgcpncsG729AnnexBNegotiation_Type())
mgcpncsG729AnnexBNegotiation.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpncsG729AnnexBNegotiation.setStatus(_A)
class _MgcpncsValidateOfferAnswerModel_Type(MxEnableState):defaultValue=1
_MgcpncsValidateOfferAnswerModel_Type.__name__=_D
_MgcpncsValidateOfferAnswerModel_Object=MibScalar
mgcpncsValidateOfferAnswerModel=_MgcpncsValidateOfferAnswerModel_Object((1,3,6,1,4,1,4935,99,100,1,5,20),_MgcpncsValidateOfferAnswerModel_Type())
mgcpncsValidateOfferAnswerModel.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpncsValidateOfferAnswerModel.setStatus(_A)
class _MgcpncsMultipleFaxToneDetection_Type(MxEnableState):defaultValue=0
_MgcpncsMultipleFaxToneDetection_Type.__name__=_D
_MgcpncsMultipleFaxToneDetection_Object=MibScalar
mgcpncsMultipleFaxToneDetection=_MgcpncsMultipleFaxToneDetection_Object((1,3,6,1,4,1,4935,99,100,1,5,100),_MgcpncsMultipleFaxToneDetection_Type())
mgcpncsMultipleFaxToneDetection.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpncsMultipleFaxToneDetection.setStatus(_A)
class _MgcpncsConnectRtpSockets_Type(MxEnableState):defaultValue=0
_MgcpncsConnectRtpSockets_Type.__name__=_D
_MgcpncsConnectRtpSockets_Object=MibScalar
mgcpncsConnectRtpSockets=_MgcpncsConnectRtpSockets_Object((1,3,6,1,4,1,4935,99,100,1,5,150),_MgcpncsConnectRtpSockets_Type())
mgcpncsConnectRtpSockets.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpncsConnectRtpSockets.setStatus(_A)
class _MgcpncsRtpUdpChecksumEnable_Type(MxEnableState):defaultValue=0
_MgcpncsRtpUdpChecksumEnable_Type.__name__=_D
_MgcpncsRtpUdpChecksumEnable_Object=MibScalar
mgcpncsRtpUdpChecksumEnable=_MgcpncsRtpUdpChecksumEnable_Object((1,3,6,1,4,1,4935,99,100,1,5,200),_MgcpncsRtpUdpChecksumEnable_Type())
mgcpncsRtpUdpChecksumEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpncsRtpUdpChecksumEnable.setStatus(_A)
class _MgcpncsT38CapabilitiesUsingAudioCodec98_Type(MxEnableState):defaultValue=0
_MgcpncsT38CapabilitiesUsingAudioCodec98_Type.__name__=_D
_MgcpncsT38CapabilitiesUsingAudioCodec98_Object=MibScalar
mgcpncsT38CapabilitiesUsingAudioCodec98=_MgcpncsT38CapabilitiesUsingAudioCodec98_Object((1,3,6,1,4,1,4935,99,100,1,5,250),_MgcpncsT38CapabilitiesUsingAudioCodec98_Type())
mgcpncsT38CapabilitiesUsingAudioCodec98.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpncsT38CapabilitiesUsingAudioCodec98.setStatus(_A)
class _MgcpncsImmediateModemToneReporting_Type(MxEnableState):defaultValue=0
_MgcpncsImmediateModemToneReporting_Type.__name__=_D
_MgcpncsImmediateModemToneReporting_Object=MibScalar
mgcpncsImmediateModemToneReporting=_MgcpncsImmediateModemToneReporting_Object((1,3,6,1,4,1,4935,99,100,1,5,300),_MgcpncsImmediateModemToneReporting_Type())
mgcpncsImmediateModemToneReporting.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpncsImmediateModemToneReporting.setStatus(_A)
class _MgcpncsMakeOsiSignalBrief_Type(MxEnableState):defaultValue=0
_MgcpncsMakeOsiSignalBrief_Type.__name__=_D
_MgcpncsMakeOsiSignalBrief_Object=MibScalar
mgcpncsMakeOsiSignalBrief=_MgcpncsMakeOsiSignalBrief_Object((1,3,6,1,4,1,4935,99,100,1,5,350),_MgcpncsMakeOsiSignalBrief_Type())
mgcpncsMakeOsiSignalBrief.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpncsMakeOsiSignalBrief.setStatus(_A)
class _MgcpncsFakeRfc3407Recognition_Type(MxEnableState):defaultValue=0
_MgcpncsFakeRfc3407Recognition_Type.__name__=_D
_MgcpncsFakeRfc3407Recognition_Object=MibScalar
mgcpncsFakeRfc3407Recognition=_MgcpncsFakeRfc3407Recognition_Object((1,3,6,1,4,1,4935,99,100,1,5,400),_MgcpncsFakeRfc3407Recognition_Type())
mgcpncsFakeRfc3407Recognition.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpncsFakeRfc3407Recognition.setStatus(_A)
class _MgcpncsUseItuT38Format_Type(MxEnableState):defaultValue=0
_MgcpncsUseItuT38Format_Type.__name__=_D
_MgcpncsUseItuT38Format_Object=MibScalar
mgcpncsUseItuT38Format=_MgcpncsUseItuT38Format_Object((1,3,6,1,4,1,4935,99,100,1,5,450),_MgcpncsUseItuT38Format_Type())
mgcpncsUseItuT38Format.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpncsUseItuT38Format.setStatus(_A)
class _MgcpncsBracketsAroundIpAddressInDomainNameEnable_Type(MxEnableState):defaultValue=1
_MgcpncsBracketsAroundIpAddressInDomainNameEnable_Type.__name__=_D
_MgcpncsBracketsAroundIpAddressInDomainNameEnable_Object=MibScalar
mgcpncsBracketsAroundIpAddressInDomainNameEnable=_MgcpncsBracketsAroundIpAddressInDomainNameEnable_Object((1,3,6,1,4,1,4935,99,100,1,5,500),_MgcpncsBracketsAroundIpAddressInDomainNameEnable_Type())
mgcpncsBracketsAroundIpAddressInDomainNameEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpncsBracketsAroundIpAddressInDomainNameEnable.setStatus(_A)
class _MgcpncsPolarityReversalOnCallingCardServiceToneEnable_Type(MxEnableState):defaultValue=0
_MgcpncsPolarityReversalOnCallingCardServiceToneEnable_Type.__name__=_D
_MgcpncsPolarityReversalOnCallingCardServiceToneEnable_Object=MibScalar
mgcpncsPolarityReversalOnCallingCardServiceToneEnable=_MgcpncsPolarityReversalOnCallingCardServiceToneEnable_Object((1,3,6,1,4,1,4935,99,100,1,5,550),_MgcpncsPolarityReversalOnCallingCardServiceToneEnable_Type())
mgcpncsPolarityReversalOnCallingCardServiceToneEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:mgcpncsPolarityReversalOnCallingCardServiceToneEnable.setStatus(_A)
_MgcpncsExperimentalConformance_ObjectIdentity=ObjectIdentity
mgcpncsExperimentalConformance=_MgcpncsExperimentalConformance_ObjectIdentity((1,3,6,1,4,1,4935,99,100,2))
_MgcpncsExperimentalCompliances_ObjectIdentity=ObjectIdentity
mgcpncsExperimentalCompliances=_MgcpncsExperimentalCompliances_ObjectIdentity((1,3,6,1,4,1,4935,99,100,2,1))
_MgcpncsExperimentalGroups_ObjectIdentity=ObjectIdentity
mgcpncsExperimentalGroups=_MgcpncsExperimentalGroups_ObjectIdentity((1,3,6,1,4,1,4935,99,100,2,2))
mgcpncsExperimentalGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,99,100,2,2,5))
mgcpncsExperimentalGroupVer1.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:mgcpncsExperimentalGroupVer1.setStatus(_A)
mgcpncsExperimentalBasicComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,99,100,2,1,5))
mgcpncsExperimentalBasicComplVer1.setObjects((_B,_T))
if mibBuilder.loadTexts:mgcpncsExperimentalBasicComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mgcpncsExperimentalMIB':mgcpncsExperimentalMIB,'mgcpncsExperimentalMIBObjects':mgcpncsExperimentalMIBObjects,'mgcpncsInterop':mgcpncsInterop,_F:mgcpncsAnswerStreamFormat,_G:mgcpncsOriginLineSessionIDAndVersionMaxLength,_H:mgcpncsG729AnnexBNegotiation,_I:mgcpncsValidateOfferAnswerModel,_J:mgcpncsMultipleFaxToneDetection,_K:mgcpncsConnectRtpSockets,_L:mgcpncsRtpUdpChecksumEnable,_M:mgcpncsT38CapabilitiesUsingAudioCodec98,_N:mgcpncsImmediateModemToneReporting,_O:mgcpncsMakeOsiSignalBrief,_P:mgcpncsFakeRfc3407Recognition,_Q:mgcpncsUseItuT38Format,_R:mgcpncsBracketsAroundIpAddressInDomainNameEnable,_S:mgcpncsPolarityReversalOnCallingCardServiceToneEnable,'mgcpncsExperimentalConformance':mgcpncsExperimentalConformance,'mgcpncsExperimentalCompliances':mgcpncsExperimentalCompliances,'mgcpncsExperimentalBasicComplVer1':mgcpncsExperimentalBasicComplVer1,'mgcpncsExperimentalGroups':mgcpncsExperimentalGroups,_T:mgcpncsExperimentalGroupVer1})