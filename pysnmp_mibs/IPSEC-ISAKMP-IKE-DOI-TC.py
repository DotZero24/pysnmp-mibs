_j='unequalPayloadLengths'
_i='unsupportedExchangeType'
_h='certificateUnavailable'
_g='notifySaLifetime'
_f='addressNotification'
_e='invalidSignature'
_d='authenticationFailed'
_c='invalidHashInformation'
_b='invalidCertAuthority'
_a='certTypeUnsupported'
_Z='invalidCertificate'
_Y='invalidCertEncoding'
_X='invalidIdInformation'
_W='invalidKeyInformation'
_V='payloadMalformed'
_U='badProposalSyntax'
_T='noProposalChosen'
_S='attributesNotSupported'
_R='invalidTransformId'
_Q='invalidSpi'
_P='invalidProtocolId'
_O='invalidMessageId'
_N='invalidFlags'
_M='invalidExchangeType'
_L='invalidMinorVersion'
_K='invalidMajorVersion'
_J='invalidCookie'
_I='situationNotSupported'
_H='doiNotSupported'
_G='invalidPayloadType'
_F='informational'
_E='aggressive'
_D='authOnly'
_C='reserved'
_B='d'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,experimental,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','experimental','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
watchguard,=mibBuilder.importSymbols('WATCHGUARD-SMI','watchguard')
ipsecIsakmpIkeDoiTC=ModuleIdentity((1,3,6,1,4,1,3097,100))
if mibBuilder.loadTexts:ipsecIsakmpIkeDoiTC.setRevisions(('1999-02-18 17:05','1999-03-05 15:45','1999-07-13 21:45','1999-10-05 17:05','1999-10-15 19:50'))
class IpsecDoiSituation(TextualConvention,Unsigned32):status=_A;displayHint='x';subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
class IpsecDoiSecProtocolId(TextualConvention,Integer32):status=_A;displayHint=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_C,0),('protoIsakmp',1),('protoIpsecAh',2),('protoIpsecEsp',3),('protoIpcomp',4)))
class IpsecDoiTransformIdent(TextualConvention,Integer32):status=_A;displayHint=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_C,0),('keyIke',1)))
class IpsecDoiAhTransform(TextualConvention,Integer32):status=_A;displayHint=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_C,0),('reserved1',1),('ahMd5',2),('ahSha',3),('ahDes',4)))
class IpsecDoiEspTransform(TextualConvention,Integer32):status=_A;displayHint=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_C,0),('espDesIv64',1),('espDes',2),('esp3Des',3),('espRc5',4),('espIdea',5),('espCast',6),('espBlowfish',7),('esp3Idea',8),('espDesIv32',9),('espRc4',10),('espNull',11)))
class IpsecDoiAuthAlgorithm(TextualConvention,Integer32):status=_A;displayHint=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*((_C,0),('hmacMd5',1),('hmacSha',2),('desMac',3),('kpdk',4)))
class IpsecDoiIpcompTransform(TextualConvention,Integer32):status=_A;displayHint=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_C,0),('ipcompOui',1),('ipcompDeflate',2),('ipcompLzs',3)))
class IpsecDoiEncapsulationMode(TextualConvention,Integer32):status=_A;displayHint=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_C,0),('tunnel',1),('transport',2)))
class IpsecDoiIdentType(TextualConvention,Integer32):status=_A;displayHint=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*((_C,0),('idIpv4Addr',1),('idFqdn',2),('idUserFqdn',3),('idIpv4AddrSubnet',4),('idIpv6Addr',5),('idIpv6AddrSubnet',6),('idIpv4AddrRange',7),('idIpv6AddrRange',8),('idDerAsn1Dn',9),('idDerAsn1Gn',10),('idKeyId',11)))
class IsakmpDOI(TextualConvention,Integer32):status=_A;displayHint=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('isakmp',0),('ipsecDOI',1)))
class IsakmpCertificateEncoding(TextualConvention,Integer32):status=_A;displayHint=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('pkcs7',1),('pgp',2),('dnsSignedKey',3),('x509Signature',4),('x509KeyExchange',5),('kerberosTokens',6),('crl',7),('arl',8),('spki',9),('x509Attribute',10)))
class IsakmpExchangeType(TextualConvention,Integer32):status=_A;displayHint=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_C,0),('base',1),('identityProtect',2),(_D,3),(_E,4),(_F,5)))
class IsakmpNotifyMessageType(TextualConvention,Integer32):status=_A;displayHint=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)));namedValues=NamedValues(*((_C,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9),(_P,10),(_Q,11),(_R,12),(_S,13),(_T,14),(_U,15),(_V,16),(_W,17),(_X,18),(_Y,19),(_Z,20),(_a,21),(_b,22),(_c,23),(_d,24),(_e,25),(_f,26),(_g,27),(_h,28),(_i,29),(_j,30)))
class IkeExchangeType(TextualConvention,Integer32):status=_A;displayHint=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,32,33,34)));namedValues=NamedValues(*((_C,0),('base',1),('mainMode',2),(_D,3),(_E,4),(_F,5),('quickMode',32),('newGroupMode',33),('acknowledgedInfo',34)))
class IkeEncryptionAlgorithm(TextualConvention,Integer32):status=_A;displayHint=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_C,0),('desCbc',1),('ideaCbc',2),('blowfishCbc',3),('rc5R16B64Cbc',4),('tripleDesCbc',5),('castCbc',6)))
class IkeHashAlgorithm(TextualConvention,Integer32):status=_A;displayHint=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_C,0),('md5',1),('sha',2),('tiger',3)))
class IkeAuthMethod(TextualConvention,Integer32):status=_A;displayHint=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_C,0),('preSharedKey',1),('dssSignatures',2),('rsaSignatures',3),('encryptionWithRsa',4),('revisedEncryptionWithRsa',5),('encryptionWithElGamal',6),('revisedEncryptionWithElGamal',7)))
class IkeGroupDescription(TextualConvention,Integer32):status=_A;displayHint=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_C,0),('modp768',1),('modp1024',2),('ec2nGalois2P155',3),('ec2nGalois2P185',4),('modp1536',5)))
class IkeGroupType(TextualConvention,Integer32):status=_A;displayHint=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_C,0),('modp',1),('ecp',2),('ec2n',3)))
class IkePrf(TextualConvention,Unsigned32):status=_A;displayHint=_B;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
class IkeNotifyMessageType(TextualConvention,Integer32):status=_A;displayHint=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,24576,24577,24578)));namedValues=NamedValues(*((_C,0),(_G,1),(_H,2),(_I,3),(_J,4),(_K,5),(_L,6),(_M,7),(_N,8),(_O,9),(_P,10),(_Q,11),(_R,12),(_S,13),(_T,14),(_U,15),(_V,16),(_W,17),(_X,18),(_Y,19),(_Z,20),(_a,21),(_b,22),(_c,23),(_d,24),(_e,25),(_f,26),(_g,27),(_h,28),(_i,29),(_j,30),('responderLifetime',24576),('replayStatus',24577),('initialContact',24578)))
mibBuilder.exportSymbols('IPSEC-ISAKMP-IKE-DOI-TC',**{'IpsecDoiSituation':IpsecDoiSituation,'IpsecDoiSecProtocolId':IpsecDoiSecProtocolId,'IpsecDoiTransformIdent':IpsecDoiTransformIdent,'IpsecDoiAhTransform':IpsecDoiAhTransform,'IpsecDoiEspTransform':IpsecDoiEspTransform,'IpsecDoiAuthAlgorithm':IpsecDoiAuthAlgorithm,'IpsecDoiIpcompTransform':IpsecDoiIpcompTransform,'IpsecDoiEncapsulationMode':IpsecDoiEncapsulationMode,'IpsecDoiIdentType':IpsecDoiIdentType,'IsakmpDOI':IsakmpDOI,'IsakmpCertificateEncoding':IsakmpCertificateEncoding,'IsakmpExchangeType':IsakmpExchangeType,'IsakmpNotifyMessageType':IsakmpNotifyMessageType,'IkeExchangeType':IkeExchangeType,'IkeEncryptionAlgorithm':IkeEncryptionAlgorithm,'IkeHashAlgorithm':IkeHashAlgorithm,'IkeAuthMethod':IkeAuthMethod,'IkeGroupDescription':IkeGroupDescription,'IkeGroupType':IkeGroupType,'IkePrf':IkePrf,'IkeNotifyMessageType':IkeNotifyMessageType,'ipsecIsakmpIkeDoiTC':ipsecIsakmpIkeDoiTC})