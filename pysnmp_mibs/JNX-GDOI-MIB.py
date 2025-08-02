_R='jnxGdoiGmTekPolicyIndex'
_Q='jnxGdoiGmKekIndex'
_P='GROUPKEY-PUSH Messages'
_O='jnxGdoiGmRekeysReceived'
_N='jnxGdoiGmTekSelectorIndex'
_M='Seconds'
_L='jnxGdoiGmIdValue'
_K='jnxGdoiGmIdType'
_J='Bits'
_I='jnxGdoiGmRegKeyServerIdValue'
_H='jnxGdoiGmRegKeyServerIdType'
_G='jnxGdoiGroupIdValue'
_F='jnxGdoiGroupIdType'
_E='Octets'
_D='not-accessible'
_C='JNX-GDOI-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
jnxMibs,=mibBuilder.importSymbols('JUNIPER-SMI','jnxMibs')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_J,'Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeInterval=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeInterval')
jnxGdoiMIB=ModuleIdentity((1,3,6,1,4,1,2636,3,759))
class JnxGdoiIdentificationType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11)));namedValues=NamedValues(*(('ipv4Address',1),('domainName',2),('userName',3),('ipv4Subnet',4),('ipv6Address',5),('ipv6Subnet',6),('ipv4Range',7),('ipv6Range',8),('caDistinguishedName',9),('caGeneralName',10),('groupNumber',11)))
class JnxGdoiIdentificationValue(TextualConvention,OctetString):status=_A;displayHint='255d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,48))
class JnxGdoiKekSPI(TextualConvention,OctetString):status=_A;displayHint='16x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(16,16));fixedLength=16
class JnxGdoiIpProtocolId(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('ipProtocolUnknown',0),('ipProtocolTCP',1),('ipProtocolUDP',2)))
class JnxGdoiKeyManagementAlgorithm(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('keyMgmtNone',0),('keyMgmtLkh',1)))
class JnxGdoiEncryptionAlgorithm(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,23,24,25,26,27,28)));namedValues=NamedValues(*(('encrAlgNone',0),('encrAlgDes64',1),('encrAlgDes',2),('encrAlg3Des',3),('encrAlgRc5',4),('encrAlgIdea',5),('encrAlgCast',6),('encrAlgBlowfish',7),('encrAlg3Idea',8),('encrAlgDes32',9),('encrAlgRc4',10),('encrAlgNull',11),('encrAlgAesCbc',12),('encrAlgAesCtr',13),('encrAlgAesCcm8',14),('encrAlgAesCcm12',15),('encrAlgAesCcm16',16),('encrAlgAesGcm8',18),('encrAlgAesGcm12',19),('encrAlgAesGcm16',20),('encrAlgNullAuthAesGmac',21),('encrAlgCamelliaCbc',23),('encrAlgCamelliaCtr',24),('encrAlgCamelliaCcm8',25),('encrAlgCamelliaCcm12',26),('encrAlgCamelliaCcm1',27),('encrAlgSeedCbc',28)))
class JnxGdoiPseudoRandomFunction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('prfNone',0),('prfMd5Hmac',1),('prfSha1Hmac',2),('prfTigerHmac',3),('prfAes128Xcbc',4),('prfSha2Hmac256',5),('prfSha2Hmac384',6),('prfSha2Hmac512',7),('prfAes128Cmac',8)))
class JnxGdoiIntegrityAlgorithm(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('authAlgNone',0),('authAlgMd5Hmac96',1),('authAlgSha1Hmac96',2),('authAlgDesMac',3),('authAlgMd5Kpdk',4),('authAlgAesXcbc96',5),('authAlgMd5Hmac128',6),('authAlgSha1Hmac160',7),('authAlgAesCmac96',8),('authAlgAes128Gmac',9),('authAlgAes192Gmac',10),('authAlgAes256Gmac',11),('authAlgSha2Hmac256to128',12),('authAlgSha2Hmac384to192',13),('authAlgSha2Hmac512to256',14)))
class JnxGdoiSignatureMethod(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,9,10,11)));namedValues=NamedValues(*(('sigNone',0),('sigRsa',1),('sigSharedKey',2),('sigDss',3),('sigEncryptRsa',4),('sigRevEncryptRsa',5),('sigEcdsa256',9),('sigEcdsa384',10),('sigEcdsa512',11)))
class JnxGdoiDiffieHellmanGroup(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,14,15,16,17,18,19,20,21,22,23,24,25,26)));namedValues=NamedValues(*(('dhNone',0),('dhGroup1',1),('dhGroup2',2),('dhEc2nGp155',3),('dhEc2nGp185',4),('dh1536Modp',5),('dh2048Modp',14),('dh3072Modp',15),('dh4096Modp',16),('dh6144Modp',17),('dh8192Modp',18),('dhEcp256',19),('dhEcp84',20),('dhEcp521',21),('dh1024Modp160',22),('dh2048Modp224',23),('dh2048Modp256',24),('dhEcp192',25),('dhEcp224',26)))
class JnxGdoiEncapsulationMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('encapUnknown',0),('encapTunnel',1),('encapTransport',2),('encapUdpTunnel',3),('encapUdpTransport',4)))
class JnxGdoiSecurityProtocol(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('secProtocolUnknown',0),('secProtocolIpsecEsp',1)))
class JnxGdoiTekSPI(TextualConvention,OctetString):status=_A;displayHint='4x';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
class JnxGdoiKekStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inUse',1),('new',2),('old',3)))
class JnxGdoiTekStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('inbound',1),('outbound',2),('biDirectional',3)))
class JnxGdoiUnsigned16(TextualConvention,OctetString):status=_A;displayHint='2d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
class JnxGdoiPolicyMismatchAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('drop',1),('forward',2),('unknown',3)))
_JnxGdoiMIBNotifications_ObjectIdentity=ObjectIdentity
jnxGdoiMIBNotifications=_JnxGdoiMIBNotifications_ObjectIdentity((1,3,6,1,4,1,2636,3,759,0))
_JnxGdoiMIBObjects_ObjectIdentity=ObjectIdentity
jnxGdoiMIBObjects=_JnxGdoiMIBObjects_ObjectIdentity((1,3,6,1,4,1,2636,3,759,1))
_JnxGdoiGroupTable_Object=MibTable
jnxGdoiGroupTable=_JnxGdoiGroupTable_Object((1,3,6,1,4,1,2636,3,759,1,1))
if mibBuilder.loadTexts:jnxGdoiGroupTable.setStatus(_A)
_JnxGdoiGroupEntry_Object=MibTableRow
jnxGdoiGroupEntry=_JnxGdoiGroupEntry_Object((1,3,6,1,4,1,2636,3,759,1,1,1))
jnxGdoiGroupEntry.setIndexNames((0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:jnxGdoiGroupEntry.setStatus(_A)
_JnxGdoiGroupIdType_Type=JnxGdoiIdentificationType
_JnxGdoiGroupIdType_Object=MibTableColumn
jnxGdoiGroupIdType=_JnxGdoiGroupIdType_Object((1,3,6,1,4,1,2636,3,759,1,1,1,1),_JnxGdoiGroupIdType_Type())
jnxGdoiGroupIdType.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxGdoiGroupIdType.setStatus(_A)
_JnxGdoiGroupIdLength_Type=Unsigned32
_JnxGdoiGroupIdLength_Object=MibTableColumn
jnxGdoiGroupIdLength=_JnxGdoiGroupIdLength_Object((1,3,6,1,4,1,2636,3,759,1,1,1,2),_JnxGdoiGroupIdLength_Type())
jnxGdoiGroupIdLength.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGroupIdLength.setStatus(_A)
if mibBuilder.loadTexts:jnxGdoiGroupIdLength.setUnits(_E)
_JnxGdoiGroupIdValue_Type=JnxGdoiIdentificationValue
_JnxGdoiGroupIdValue_Object=MibTableColumn
jnxGdoiGroupIdValue=_JnxGdoiGroupIdValue_Object((1,3,6,1,4,1,2636,3,759,1,1,1,3),_JnxGdoiGroupIdValue_Type())
jnxGdoiGroupIdValue.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxGdoiGroupIdValue.setStatus(_A)
_JnxGdoiGroupName_Type=DisplayString
_JnxGdoiGroupName_Object=MibTableColumn
jnxGdoiGroupName=_JnxGdoiGroupName_Object((1,3,6,1,4,1,2636,3,759,1,1,1,4),_JnxGdoiGroupName_Type())
jnxGdoiGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGroupName.setStatus(_A)
_JnxGdoiPeers_ObjectIdentity=ObjectIdentity
jnxGdoiPeers=_JnxGdoiPeers_ObjectIdentity((1,3,6,1,4,1,2636,3,759,1,2))
_JnxGdoiGmTable_Object=MibTable
jnxGdoiGmTable=_JnxGdoiGmTable_Object((1,3,6,1,4,1,2636,3,759,1,2,2))
if mibBuilder.loadTexts:jnxGdoiGmTable.setStatus(_A)
_JnxGdoiGmEntry_Object=MibTableRow
jnxGdoiGmEntry=_JnxGdoiGmEntry_Object((1,3,6,1,4,1,2636,3,759,1,2,2,1))
jnxGdoiGmEntry.setIndexNames((0,_C,_F),(0,_C,_G),(0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:jnxGdoiGmEntry.setStatus(_A)
_JnxGdoiGmIdType_Type=JnxGdoiIdentificationType
_JnxGdoiGmIdType_Object=MibTableColumn
jnxGdoiGmIdType=_JnxGdoiGmIdType_Object((1,3,6,1,4,1,2636,3,759,1,2,2,1,1),_JnxGdoiGmIdType_Type())
jnxGdoiGmIdType.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxGdoiGmIdType.setStatus(_A)
_JnxGdoiGmIdLength_Type=Unsigned32
_JnxGdoiGmIdLength_Object=MibTableColumn
jnxGdoiGmIdLength=_JnxGdoiGmIdLength_Object((1,3,6,1,4,1,2636,3,759,1,2,2,1,2),_JnxGdoiGmIdLength_Type())
jnxGdoiGmIdLength.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmIdLength.setStatus(_A)
if mibBuilder.loadTexts:jnxGdoiGmIdLength.setUnits(_E)
_JnxGdoiGmIdValue_Type=JnxGdoiIdentificationValue
_JnxGdoiGmIdValue_Object=MibTableColumn
jnxGdoiGmIdValue=_JnxGdoiGmIdValue_Object((1,3,6,1,4,1,2636,3,759,1,2,2,1,3),_JnxGdoiGmIdValue_Type())
jnxGdoiGmIdValue.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxGdoiGmIdValue.setStatus(_A)
_JnxGdoiGmRegKeyServerIdType_Type=JnxGdoiIdentificationType
_JnxGdoiGmRegKeyServerIdType_Object=MibTableColumn
jnxGdoiGmRegKeyServerIdType=_JnxGdoiGmRegKeyServerIdType_Object((1,3,6,1,4,1,2636,3,759,1,2,2,1,4),_JnxGdoiGmRegKeyServerIdType_Type())
jnxGdoiGmRegKeyServerIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmRegKeyServerIdType.setStatus(_A)
_JnxGdoiGmRegKeyServerIdLength_Type=Unsigned32
_JnxGdoiGmRegKeyServerIdLength_Object=MibTableColumn
jnxGdoiGmRegKeyServerIdLength=_JnxGdoiGmRegKeyServerIdLength_Object((1,3,6,1,4,1,2636,3,759,1,2,2,1,5),_JnxGdoiGmRegKeyServerIdLength_Type())
jnxGdoiGmRegKeyServerIdLength.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmRegKeyServerIdLength.setStatus(_A)
if mibBuilder.loadTexts:jnxGdoiGmRegKeyServerIdLength.setUnits(_E)
_JnxGdoiGmRegKeyServerIdValue_Type=JnxGdoiIdentificationValue
_JnxGdoiGmRegKeyServerIdValue_Object=MibTableColumn
jnxGdoiGmRegKeyServerIdValue=_JnxGdoiGmRegKeyServerIdValue_Object((1,3,6,1,4,1,2636,3,759,1,2,2,1,6),_JnxGdoiGmRegKeyServerIdValue_Type())
jnxGdoiGmRegKeyServerIdValue.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmRegKeyServerIdValue.setStatus(_A)
_JnxGdoiGmActiveKEK_Type=JnxGdoiKekSPI
_JnxGdoiGmActiveKEK_Object=MibTableColumn
jnxGdoiGmActiveKEK=_JnxGdoiGmActiveKEK_Object((1,3,6,1,4,1,2636,3,759,1,2,2,1,7),_JnxGdoiGmActiveKEK_Type())
jnxGdoiGmActiveKEK.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmActiveKEK.setStatus(_A)
_JnxGdoiGmRekeysReceived_Type=Counter32
_JnxGdoiGmRekeysReceived_Object=MibTableColumn
jnxGdoiGmRekeysReceived=_JnxGdoiGmRekeysReceived_Object((1,3,6,1,4,1,2636,3,759,1,2,2,1,8),_JnxGdoiGmRekeysReceived_Type())
jnxGdoiGmRekeysReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmRekeysReceived.setStatus(_A)
if mibBuilder.loadTexts:jnxGdoiGmRekeysReceived.setUnits(_P)
_JnxGdoiGmActiveTEKNum_Type=Counter32
_JnxGdoiGmActiveTEKNum_Object=MibTableColumn
jnxGdoiGmActiveTEKNum=_JnxGdoiGmActiveTEKNum_Object((1,3,6,1,4,1,2636,3,759,1,2,2,1,9),_JnxGdoiGmActiveTEKNum_Type())
jnxGdoiGmActiveTEKNum.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmActiveTEKNum.setStatus(_A)
if mibBuilder.loadTexts:jnxGdoiGmActiveTEKNum.setUnits('Number of traffic encryption keys')
_JnxGdoiSecAssociations_ObjectIdentity=ObjectIdentity
jnxGdoiSecAssociations=_JnxGdoiSecAssociations_ObjectIdentity((1,3,6,1,4,1,2636,3,759,1,3))
_JnxGdoiGmKekTable_Object=MibTable
jnxGdoiGmKekTable=_JnxGdoiGmKekTable_Object((1,3,6,1,4,1,2636,3,759,1,3,2))
if mibBuilder.loadTexts:jnxGdoiGmKekTable.setStatus(_A)
_JnxGdoiGmKekEntry_Object=MibTableRow
jnxGdoiGmKekEntry=_JnxGdoiGmKekEntry_Object((1,3,6,1,4,1,2636,3,759,1,3,2,1))
jnxGdoiGmKekEntry.setIndexNames((0,_C,_F),(0,_C,_G),(0,_C,_K),(0,_C,_L),(0,_C,_Q))
if mibBuilder.loadTexts:jnxGdoiGmKekEntry.setStatus(_A)
_JnxGdoiGmKekIndex_Type=Unsigned32
_JnxGdoiGmKekIndex_Object=MibTableColumn
jnxGdoiGmKekIndex=_JnxGdoiGmKekIndex_Object((1,3,6,1,4,1,2636,3,759,1,3,2,1,1),_JnxGdoiGmKekIndex_Type())
jnxGdoiGmKekIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxGdoiGmKekIndex.setStatus(_A)
_JnxGdoiGmKekSPI_Type=JnxGdoiKekSPI
_JnxGdoiGmKekSPI_Object=MibTableColumn
jnxGdoiGmKekSPI=_JnxGdoiGmKekSPI_Object((1,3,6,1,4,1,2636,3,759,1,3,2,1,2),_JnxGdoiGmKekSPI_Type())
jnxGdoiGmKekSPI.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmKekSPI.setStatus(_A)
_JnxGdoiGmKekSrcIdType_Type=JnxGdoiIdentificationType
_JnxGdoiGmKekSrcIdType_Object=MibTableColumn
jnxGdoiGmKekSrcIdType=_JnxGdoiGmKekSrcIdType_Object((1,3,6,1,4,1,2636,3,759,1,3,2,1,3),_JnxGdoiGmKekSrcIdType_Type())
jnxGdoiGmKekSrcIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmKekSrcIdType.setStatus(_A)
_JnxGdoiGmKekSrcIdLength_Type=Unsigned32
_JnxGdoiGmKekSrcIdLength_Object=MibTableColumn
jnxGdoiGmKekSrcIdLength=_JnxGdoiGmKekSrcIdLength_Object((1,3,6,1,4,1,2636,3,759,1,3,2,1,4),_JnxGdoiGmKekSrcIdLength_Type())
jnxGdoiGmKekSrcIdLength.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmKekSrcIdLength.setStatus(_A)
if mibBuilder.loadTexts:jnxGdoiGmKekSrcIdLength.setUnits(_E)
_JnxGdoiGmKekSrcIdValue_Type=JnxGdoiIdentificationValue
_JnxGdoiGmKekSrcIdValue_Object=MibTableColumn
jnxGdoiGmKekSrcIdValue=_JnxGdoiGmKekSrcIdValue_Object((1,3,6,1,4,1,2636,3,759,1,3,2,1,5),_JnxGdoiGmKekSrcIdValue_Type())
jnxGdoiGmKekSrcIdValue.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmKekSrcIdValue.setStatus(_A)
_JnxGdoiGmKekSrcIdPort_Type=JnxGdoiUnsigned16
_JnxGdoiGmKekSrcIdPort_Object=MibTableColumn
jnxGdoiGmKekSrcIdPort=_JnxGdoiGmKekSrcIdPort_Object((1,3,6,1,4,1,2636,3,759,1,3,2,1,6),_JnxGdoiGmKekSrcIdPort_Type())
jnxGdoiGmKekSrcIdPort.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmKekSrcIdPort.setStatus(_A)
_JnxGdoiGmKekDstIdType_Type=JnxGdoiIdentificationType
_JnxGdoiGmKekDstIdType_Object=MibTableColumn
jnxGdoiGmKekDstIdType=_JnxGdoiGmKekDstIdType_Object((1,3,6,1,4,1,2636,3,759,1,3,2,1,7),_JnxGdoiGmKekDstIdType_Type())
jnxGdoiGmKekDstIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmKekDstIdType.setStatus(_A)
_JnxGdoiGmKekDstIdLength_Type=Unsigned32
_JnxGdoiGmKekDstIdLength_Object=MibTableColumn
jnxGdoiGmKekDstIdLength=_JnxGdoiGmKekDstIdLength_Object((1,3,6,1,4,1,2636,3,759,1,3,2,1,8),_JnxGdoiGmKekDstIdLength_Type())
jnxGdoiGmKekDstIdLength.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmKekDstIdLength.setStatus(_A)
if mibBuilder.loadTexts:jnxGdoiGmKekDstIdLength.setUnits(_E)
_JnxGdoiGmKekDstIdValue_Type=JnxGdoiIdentificationValue
_JnxGdoiGmKekDstIdValue_Object=MibTableColumn
jnxGdoiGmKekDstIdValue=_JnxGdoiGmKekDstIdValue_Object((1,3,6,1,4,1,2636,3,759,1,3,2,1,9),_JnxGdoiGmKekDstIdValue_Type())
jnxGdoiGmKekDstIdValue.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmKekDstIdValue.setStatus(_A)
_JnxGdoiGmKekDstIdPort_Type=JnxGdoiUnsigned16
_JnxGdoiGmKekDstIdPort_Object=MibTableColumn
jnxGdoiGmKekDstIdPort=_JnxGdoiGmKekDstIdPort_Object((1,3,6,1,4,1,2636,3,759,1,3,2,1,10),_JnxGdoiGmKekDstIdPort_Type())
jnxGdoiGmKekDstIdPort.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmKekDstIdPort.setStatus(_A)
_JnxGdoiGmKekIpProtocol_Type=JnxGdoiIpProtocolId
_JnxGdoiGmKekIpProtocol_Object=MibTableColumn
jnxGdoiGmKekIpProtocol=_JnxGdoiGmKekIpProtocol_Object((1,3,6,1,4,1,2636,3,759,1,3,2,1,11),_JnxGdoiGmKekIpProtocol_Type())
jnxGdoiGmKekIpProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmKekIpProtocol.setStatus(_A)
_JnxGdoiGmKekMgmtAlg_Type=JnxGdoiKeyManagementAlgorithm
_JnxGdoiGmKekMgmtAlg_Object=MibTableColumn
jnxGdoiGmKekMgmtAlg=_JnxGdoiGmKekMgmtAlg_Object((1,3,6,1,4,1,2636,3,759,1,3,2,1,12),_JnxGdoiGmKekMgmtAlg_Type())
jnxGdoiGmKekMgmtAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmKekMgmtAlg.setStatus(_A)
_JnxGdoiGmKekEncryptAlg_Type=JnxGdoiEncryptionAlgorithm
_JnxGdoiGmKekEncryptAlg_Object=MibTableColumn
jnxGdoiGmKekEncryptAlg=_JnxGdoiGmKekEncryptAlg_Object((1,3,6,1,4,1,2636,3,759,1,3,2,1,13),_JnxGdoiGmKekEncryptAlg_Type())
jnxGdoiGmKekEncryptAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmKekEncryptAlg.setStatus(_A)
_JnxGdoiGmKekEncryptKeyLength_Type=Unsigned32
_JnxGdoiGmKekEncryptKeyLength_Object=MibTableColumn
jnxGdoiGmKekEncryptKeyLength=_JnxGdoiGmKekEncryptKeyLength_Object((1,3,6,1,4,1,2636,3,759,1,3,2,1,14),_JnxGdoiGmKekEncryptKeyLength_Type())
jnxGdoiGmKekEncryptKeyLength.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmKekEncryptKeyLength.setStatus(_A)
if mibBuilder.loadTexts:jnxGdoiGmKekEncryptKeyLength.setUnits(_J)
_JnxGdoiGmKekSigHashAlg_Type=JnxGdoiPseudoRandomFunction
_JnxGdoiGmKekSigHashAlg_Object=MibTableColumn
jnxGdoiGmKekSigHashAlg=_JnxGdoiGmKekSigHashAlg_Object((1,3,6,1,4,1,2636,3,759,1,3,2,1,15),_JnxGdoiGmKekSigHashAlg_Type())
jnxGdoiGmKekSigHashAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmKekSigHashAlg.setStatus(_A)
_JnxGdoiGmKekSigAlg_Type=JnxGdoiSignatureMethod
_JnxGdoiGmKekSigAlg_Object=MibTableColumn
jnxGdoiGmKekSigAlg=_JnxGdoiGmKekSigAlg_Object((1,3,6,1,4,1,2636,3,759,1,3,2,1,16),_JnxGdoiGmKekSigAlg_Type())
jnxGdoiGmKekSigAlg.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmKekSigAlg.setStatus(_A)
_JnxGdoiGmKekSigKeyLength_Type=Unsigned32
_JnxGdoiGmKekSigKeyLength_Object=MibTableColumn
jnxGdoiGmKekSigKeyLength=_JnxGdoiGmKekSigKeyLength_Object((1,3,6,1,4,1,2636,3,759,1,3,2,1,17),_JnxGdoiGmKekSigKeyLength_Type())
jnxGdoiGmKekSigKeyLength.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmKekSigKeyLength.setStatus(_A)
if mibBuilder.loadTexts:jnxGdoiGmKekSigKeyLength.setUnits(_J)
_JnxGdoiGmKekOakleyGroup_Type=JnxGdoiDiffieHellmanGroup
_JnxGdoiGmKekOakleyGroup_Object=MibTableColumn
jnxGdoiGmKekOakleyGroup=_JnxGdoiGmKekOakleyGroup_Object((1,3,6,1,4,1,2636,3,759,1,3,2,1,18),_JnxGdoiGmKekOakleyGroup_Type())
jnxGdoiGmKekOakleyGroup.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmKekOakleyGroup.setStatus(_A)
_JnxGdoiGmKekOriginalLifetime_Type=Unsigned32
_JnxGdoiGmKekOriginalLifetime_Object=MibTableColumn
jnxGdoiGmKekOriginalLifetime=_JnxGdoiGmKekOriginalLifetime_Object((1,3,6,1,4,1,2636,3,759,1,3,2,1,19),_JnxGdoiGmKekOriginalLifetime_Type())
jnxGdoiGmKekOriginalLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmKekOriginalLifetime.setStatus(_A)
if mibBuilder.loadTexts:jnxGdoiGmKekOriginalLifetime.setUnits(_M)
_JnxGdoiGmKekRemainingLifetime_Type=Unsigned32
_JnxGdoiGmKekRemainingLifetime_Object=MibTableColumn
jnxGdoiGmKekRemainingLifetime=_JnxGdoiGmKekRemainingLifetime_Object((1,3,6,1,4,1,2636,3,759,1,3,2,1,20),_JnxGdoiGmKekRemainingLifetime_Type())
jnxGdoiGmKekRemainingLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmKekRemainingLifetime.setStatus(_A)
if mibBuilder.loadTexts:jnxGdoiGmKekRemainingLifetime.setUnits(_M)
_JnxGdoiGmKekStatus_Type=JnxGdoiKekStatus
_JnxGdoiGmKekStatus_Object=MibTableColumn
jnxGdoiGmKekStatus=_JnxGdoiGmKekStatus_Object((1,3,6,1,4,1,2636,3,759,1,3,2,1,21),_JnxGdoiGmKekStatus_Type())
jnxGdoiGmKekStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmKekStatus.setStatus(_A)
_JnxGdoiGmTekSelectorTable_Object=MibTable
jnxGdoiGmTekSelectorTable=_JnxGdoiGmTekSelectorTable_Object((1,3,6,1,4,1,2636,3,759,1,3,5))
if mibBuilder.loadTexts:jnxGdoiGmTekSelectorTable.setStatus(_A)
_JnxGdoiGmTekSelectorEntry_Object=MibTableRow
jnxGdoiGmTekSelectorEntry=_JnxGdoiGmTekSelectorEntry_Object((1,3,6,1,4,1,2636,3,759,1,3,5,1))
jnxGdoiGmTekSelectorEntry.setIndexNames((0,_C,_F),(0,_C,_G),(0,_C,_K),(0,_C,_L),(0,_C,_N))
if mibBuilder.loadTexts:jnxGdoiGmTekSelectorEntry.setStatus(_A)
_JnxGdoiGmTekSelectorIndex_Type=Unsigned32
_JnxGdoiGmTekSelectorIndex_Object=MibTableColumn
jnxGdoiGmTekSelectorIndex=_JnxGdoiGmTekSelectorIndex_Object((1,3,6,1,4,1,2636,3,759,1,3,5,1,1),_JnxGdoiGmTekSelectorIndex_Type())
jnxGdoiGmTekSelectorIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxGdoiGmTekSelectorIndex.setStatus(_A)
_JnxGdoiGmTekSrcIdType_Type=JnxGdoiIdentificationType
_JnxGdoiGmTekSrcIdType_Object=MibTableColumn
jnxGdoiGmTekSrcIdType=_JnxGdoiGmTekSrcIdType_Object((1,3,6,1,4,1,2636,3,759,1,3,5,1,2),_JnxGdoiGmTekSrcIdType_Type())
jnxGdoiGmTekSrcIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmTekSrcIdType.setStatus(_A)
_JnxGdoiGmTekSrcIdLength_Type=Unsigned32
_JnxGdoiGmTekSrcIdLength_Object=MibTableColumn
jnxGdoiGmTekSrcIdLength=_JnxGdoiGmTekSrcIdLength_Object((1,3,6,1,4,1,2636,3,759,1,3,5,1,3),_JnxGdoiGmTekSrcIdLength_Type())
jnxGdoiGmTekSrcIdLength.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmTekSrcIdLength.setStatus(_A)
if mibBuilder.loadTexts:jnxGdoiGmTekSrcIdLength.setUnits(_E)
_JnxGdoiGmTekSrcIdValue_Type=JnxGdoiIdentificationValue
_JnxGdoiGmTekSrcIdValue_Object=MibTableColumn
jnxGdoiGmTekSrcIdValue=_JnxGdoiGmTekSrcIdValue_Object((1,3,6,1,4,1,2636,3,759,1,3,5,1,4),_JnxGdoiGmTekSrcIdValue_Type())
jnxGdoiGmTekSrcIdValue.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmTekSrcIdValue.setStatus(_A)
_JnxGdoiGmTekSrcIdPort_Type=JnxGdoiUnsigned16
_JnxGdoiGmTekSrcIdPort_Object=MibTableColumn
jnxGdoiGmTekSrcIdPort=_JnxGdoiGmTekSrcIdPort_Object((1,3,6,1,4,1,2636,3,759,1,3,5,1,5),_JnxGdoiGmTekSrcIdPort_Type())
jnxGdoiGmTekSrcIdPort.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmTekSrcIdPort.setStatus(_A)
_JnxGdoiGmTekDstIdType_Type=JnxGdoiIdentificationType
_JnxGdoiGmTekDstIdType_Object=MibTableColumn
jnxGdoiGmTekDstIdType=_JnxGdoiGmTekDstIdType_Object((1,3,6,1,4,1,2636,3,759,1,3,5,1,6),_JnxGdoiGmTekDstIdType_Type())
jnxGdoiGmTekDstIdType.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmTekDstIdType.setStatus(_A)
_JnxGdoiGmTekDstIdLength_Type=Unsigned32
_JnxGdoiGmTekDstIdLength_Object=MibTableColumn
jnxGdoiGmTekDstIdLength=_JnxGdoiGmTekDstIdLength_Object((1,3,6,1,4,1,2636,3,759,1,3,5,1,7),_JnxGdoiGmTekDstIdLength_Type())
jnxGdoiGmTekDstIdLength.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmTekDstIdLength.setStatus(_A)
if mibBuilder.loadTexts:jnxGdoiGmTekDstIdLength.setUnits(_E)
_JnxGdoiGmTekDstIdValue_Type=JnxGdoiIdentificationValue
_JnxGdoiGmTekDstIdValue_Object=MibTableColumn
jnxGdoiGmTekDstIdValue=_JnxGdoiGmTekDstIdValue_Object((1,3,6,1,4,1,2636,3,759,1,3,5,1,8),_JnxGdoiGmTekDstIdValue_Type())
jnxGdoiGmTekDstIdValue.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmTekDstIdValue.setStatus(_A)
_JnxGdoiGmTekDstIdPort_Type=JnxGdoiUnsigned16
_JnxGdoiGmTekDstIdPort_Object=MibTableColumn
jnxGdoiGmTekDstIdPort=_JnxGdoiGmTekDstIdPort_Object((1,3,6,1,4,1,2636,3,759,1,3,5,1,9),_JnxGdoiGmTekDstIdPort_Type())
jnxGdoiGmTekDstIdPort.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmTekDstIdPort.setStatus(_A)
_JnxGdoiGmTekSecurityProtocol_Type=JnxGdoiSecurityProtocol
_JnxGdoiGmTekSecurityProtocol_Object=MibTableColumn
jnxGdoiGmTekSecurityProtocol=_JnxGdoiGmTekSecurityProtocol_Object((1,3,6,1,4,1,2636,3,759,1,3,5,1,10),_JnxGdoiGmTekSecurityProtocol_Type())
jnxGdoiGmTekSecurityProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmTekSecurityProtocol.setStatus(_A)
_JnxGdoiGmTekPolicyMismatchAction_Type=JnxGdoiPolicyMismatchAction
_JnxGdoiGmTekPolicyMismatchAction_Object=MibTableColumn
jnxGdoiGmTekPolicyMismatchAction=_JnxGdoiGmTekPolicyMismatchAction_Object((1,3,6,1,4,1,2636,3,759,1,3,5,1,11),_JnxGdoiGmTekPolicyMismatchAction_Type())
jnxGdoiGmTekPolicyMismatchAction.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmTekPolicyMismatchAction.setStatus(_A)
_JnxGdoiGmTekPolicyTable_Object=MibTable
jnxGdoiGmTekPolicyTable=_JnxGdoiGmTekPolicyTable_Object((1,3,6,1,4,1,2636,3,759,1,3,6))
if mibBuilder.loadTexts:jnxGdoiGmTekPolicyTable.setStatus(_A)
_JnxGdoiGmTekPolicyEntry_Object=MibTableRow
jnxGdoiGmTekPolicyEntry=_JnxGdoiGmTekPolicyEntry_Object((1,3,6,1,4,1,2636,3,759,1,3,6,1))
jnxGdoiGmTekPolicyEntry.setIndexNames((0,_C,_F),(0,_C,_G),(0,_C,_K),(0,_C,_L),(0,_C,_N),(0,_C,_R))
if mibBuilder.loadTexts:jnxGdoiGmTekPolicyEntry.setStatus(_A)
_JnxGdoiGmTekPolicyIndex_Type=Unsigned32
_JnxGdoiGmTekPolicyIndex_Object=MibTableColumn
jnxGdoiGmTekPolicyIndex=_JnxGdoiGmTekPolicyIndex_Object((1,3,6,1,4,1,2636,3,759,1,3,6,1,1),_JnxGdoiGmTekPolicyIndex_Type())
jnxGdoiGmTekPolicyIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:jnxGdoiGmTekPolicyIndex.setStatus(_A)
_JnxGdoiGmTekSPI_Type=JnxGdoiTekSPI
_JnxGdoiGmTekSPI_Object=MibTableColumn
jnxGdoiGmTekSPI=_JnxGdoiGmTekSPI_Object((1,3,6,1,4,1,2636,3,759,1,3,6,1,2),_JnxGdoiGmTekSPI_Type())
jnxGdoiGmTekSPI.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmTekSPI.setStatus(_A)
_JnxGdoiGmTekEncapsulationMode_Type=JnxGdoiEncapsulationMode
_JnxGdoiGmTekEncapsulationMode_Object=MibTableColumn
jnxGdoiGmTekEncapsulationMode=_JnxGdoiGmTekEncapsulationMode_Object((1,3,6,1,4,1,2636,3,759,1,3,6,1,3),_JnxGdoiGmTekEncapsulationMode_Type())
jnxGdoiGmTekEncapsulationMode.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmTekEncapsulationMode.setStatus(_A)
_JnxGdoiGmTekEncryptionAlgorithm_Type=JnxGdoiEncryptionAlgorithm
_JnxGdoiGmTekEncryptionAlgorithm_Object=MibTableColumn
jnxGdoiGmTekEncryptionAlgorithm=_JnxGdoiGmTekEncryptionAlgorithm_Object((1,3,6,1,4,1,2636,3,759,1,3,6,1,4),_JnxGdoiGmTekEncryptionAlgorithm_Type())
jnxGdoiGmTekEncryptionAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmTekEncryptionAlgorithm.setStatus(_A)
_JnxGdoiGmTekEncryptionKeyLength_Type=Unsigned32
_JnxGdoiGmTekEncryptionKeyLength_Object=MibTableColumn
jnxGdoiGmTekEncryptionKeyLength=_JnxGdoiGmTekEncryptionKeyLength_Object((1,3,6,1,4,1,2636,3,759,1,3,6,1,5),_JnxGdoiGmTekEncryptionKeyLength_Type())
jnxGdoiGmTekEncryptionKeyLength.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmTekEncryptionKeyLength.setStatus(_A)
if mibBuilder.loadTexts:jnxGdoiGmTekEncryptionKeyLength.setUnits(_J)
_JnxGdoiGmTekIntegrityAlgorithm_Type=JnxGdoiIntegrityAlgorithm
_JnxGdoiGmTekIntegrityAlgorithm_Object=MibTableColumn
jnxGdoiGmTekIntegrityAlgorithm=_JnxGdoiGmTekIntegrityAlgorithm_Object((1,3,6,1,4,1,2636,3,759,1,3,6,1,6),_JnxGdoiGmTekIntegrityAlgorithm_Type())
jnxGdoiGmTekIntegrityAlgorithm.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmTekIntegrityAlgorithm.setStatus(_A)
_JnxGdoiGmTekIntegrityKeyLength_Type=Unsigned32
_JnxGdoiGmTekIntegrityKeyLength_Object=MibTableColumn
jnxGdoiGmTekIntegrityKeyLength=_JnxGdoiGmTekIntegrityKeyLength_Object((1,3,6,1,4,1,2636,3,759,1,3,6,1,7),_JnxGdoiGmTekIntegrityKeyLength_Type())
jnxGdoiGmTekIntegrityKeyLength.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmTekIntegrityKeyLength.setStatus(_A)
if mibBuilder.loadTexts:jnxGdoiGmTekIntegrityKeyLength.setUnits(_J)
_JnxGdoiGmTekWindowSize_Type=Unsigned32
_JnxGdoiGmTekWindowSize_Object=MibTableColumn
jnxGdoiGmTekWindowSize=_JnxGdoiGmTekWindowSize_Object((1,3,6,1,4,1,2636,3,759,1,3,6,1,8),_JnxGdoiGmTekWindowSize_Type())
jnxGdoiGmTekWindowSize.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmTekWindowSize.setStatus(_A)
if mibBuilder.loadTexts:jnxGdoiGmTekWindowSize.setUnits(_P)
_JnxGdoiGmTekOriginalLifetime_Type=Unsigned32
_JnxGdoiGmTekOriginalLifetime_Object=MibTableColumn
jnxGdoiGmTekOriginalLifetime=_JnxGdoiGmTekOriginalLifetime_Object((1,3,6,1,4,1,2636,3,759,1,3,6,1,9),_JnxGdoiGmTekOriginalLifetime_Type())
jnxGdoiGmTekOriginalLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmTekOriginalLifetime.setStatus(_A)
if mibBuilder.loadTexts:jnxGdoiGmTekOriginalLifetime.setUnits(_M)
_JnxGdoiGmTekRemainingLifetime_Type=Unsigned32
_JnxGdoiGmTekRemainingLifetime_Object=MibTableColumn
jnxGdoiGmTekRemainingLifetime=_JnxGdoiGmTekRemainingLifetime_Object((1,3,6,1,4,1,2636,3,759,1,3,6,1,10),_JnxGdoiGmTekRemainingLifetime_Type())
jnxGdoiGmTekRemainingLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmTekRemainingLifetime.setStatus(_A)
if mibBuilder.loadTexts:jnxGdoiGmTekRemainingLifetime.setUnits(_M)
_JnxGdoiGmTekStatus_Type=JnxGdoiTekStatus
_JnxGdoiGmTekStatus_Object=MibTableColumn
jnxGdoiGmTekStatus=_JnxGdoiGmTekStatus_Object((1,3,6,1,4,1,2636,3,759,1,3,6,1,11),_JnxGdoiGmTekStatus_Type())
jnxGdoiGmTekStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:jnxGdoiGmTekStatus.setStatus(_A)
jnxGdoiGmRegister=NotificationType((1,3,6,1,4,1,2636,3,759,0,5))
jnxGdoiGmRegister.setObjects(*((_C,_H),(_C,_I)))
if mibBuilder.loadTexts:jnxGdoiGmRegister.setStatus(_A)
jnxGdoiGmRegistrationComplete=NotificationType((1,3,6,1,4,1,2636,3,759,0,6))
jnxGdoiGmRegistrationComplete.setObjects(*((_C,_H),(_C,_I)))
if mibBuilder.loadTexts:jnxGdoiGmRegistrationComplete.setStatus(_A)
jnxGdoiGmReRegister=NotificationType((1,3,6,1,4,1,2636,3,759,0,7))
jnxGdoiGmReRegister.setObjects(*((_C,_H),(_C,_I)))
if mibBuilder.loadTexts:jnxGdoiGmReRegister.setStatus(_A)
jnxGdoiGmRekeyReceived=NotificationType((1,3,6,1,4,1,2636,3,759,0,8))
jnxGdoiGmRekeyReceived.setObjects(*((_C,_H),(_C,_I),(_C,_O)))
if mibBuilder.loadTexts:jnxGdoiGmRekeyReceived.setStatus(_A)
jnxGdoiGmRekeyFailure=NotificationType((1,3,6,1,4,1,2636,3,759,0,11))
jnxGdoiGmRekeyFailure.setObjects(*((_C,_H),(_C,_I),(_C,_O)))
if mibBuilder.loadTexts:jnxGdoiGmRekeyFailure.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'JnxGdoiIdentificationType':JnxGdoiIdentificationType,'JnxGdoiIdentificationValue':JnxGdoiIdentificationValue,'JnxGdoiKekSPI':JnxGdoiKekSPI,'JnxGdoiIpProtocolId':JnxGdoiIpProtocolId,'JnxGdoiKeyManagementAlgorithm':JnxGdoiKeyManagementAlgorithm,'JnxGdoiEncryptionAlgorithm':JnxGdoiEncryptionAlgorithm,'JnxGdoiPseudoRandomFunction':JnxGdoiPseudoRandomFunction,'JnxGdoiIntegrityAlgorithm':JnxGdoiIntegrityAlgorithm,'JnxGdoiSignatureMethod':JnxGdoiSignatureMethod,'JnxGdoiDiffieHellmanGroup':JnxGdoiDiffieHellmanGroup,'JnxGdoiEncapsulationMode':JnxGdoiEncapsulationMode,'JnxGdoiSecurityProtocol':JnxGdoiSecurityProtocol,'JnxGdoiTekSPI':JnxGdoiTekSPI,'JnxGdoiKekStatus':JnxGdoiKekStatus,'JnxGdoiTekStatus':JnxGdoiTekStatus,'JnxGdoiUnsigned16':JnxGdoiUnsigned16,'JnxGdoiPolicyMismatchAction':JnxGdoiPolicyMismatchAction,'jnxGdoiMIB':jnxGdoiMIB,'jnxGdoiMIBNotifications':jnxGdoiMIBNotifications,'jnxGdoiGmRegister':jnxGdoiGmRegister,'jnxGdoiGmRegistrationComplete':jnxGdoiGmRegistrationComplete,'jnxGdoiGmReRegister':jnxGdoiGmReRegister,'jnxGdoiGmRekeyReceived':jnxGdoiGmRekeyReceived,'jnxGdoiGmRekeyFailure':jnxGdoiGmRekeyFailure,'jnxGdoiMIBObjects':jnxGdoiMIBObjects,'jnxGdoiGroupTable':jnxGdoiGroupTable,'jnxGdoiGroupEntry':jnxGdoiGroupEntry,_F:jnxGdoiGroupIdType,'jnxGdoiGroupIdLength':jnxGdoiGroupIdLength,_G:jnxGdoiGroupIdValue,'jnxGdoiGroupName':jnxGdoiGroupName,'jnxGdoiPeers':jnxGdoiPeers,'jnxGdoiGmTable':jnxGdoiGmTable,'jnxGdoiGmEntry':jnxGdoiGmEntry,_K:jnxGdoiGmIdType,'jnxGdoiGmIdLength':jnxGdoiGmIdLength,_L:jnxGdoiGmIdValue,_H:jnxGdoiGmRegKeyServerIdType,'jnxGdoiGmRegKeyServerIdLength':jnxGdoiGmRegKeyServerIdLength,_I:jnxGdoiGmRegKeyServerIdValue,'jnxGdoiGmActiveKEK':jnxGdoiGmActiveKEK,_O:jnxGdoiGmRekeysReceived,'jnxGdoiGmActiveTEKNum':jnxGdoiGmActiveTEKNum,'jnxGdoiSecAssociations':jnxGdoiSecAssociations,'jnxGdoiGmKekTable':jnxGdoiGmKekTable,'jnxGdoiGmKekEntry':jnxGdoiGmKekEntry,_Q:jnxGdoiGmKekIndex,'jnxGdoiGmKekSPI':jnxGdoiGmKekSPI,'jnxGdoiGmKekSrcIdType':jnxGdoiGmKekSrcIdType,'jnxGdoiGmKekSrcIdLength':jnxGdoiGmKekSrcIdLength,'jnxGdoiGmKekSrcIdValue':jnxGdoiGmKekSrcIdValue,'jnxGdoiGmKekSrcIdPort':jnxGdoiGmKekSrcIdPort,'jnxGdoiGmKekDstIdType':jnxGdoiGmKekDstIdType,'jnxGdoiGmKekDstIdLength':jnxGdoiGmKekDstIdLength,'jnxGdoiGmKekDstIdValue':jnxGdoiGmKekDstIdValue,'jnxGdoiGmKekDstIdPort':jnxGdoiGmKekDstIdPort,'jnxGdoiGmKekIpProtocol':jnxGdoiGmKekIpProtocol,'jnxGdoiGmKekMgmtAlg':jnxGdoiGmKekMgmtAlg,'jnxGdoiGmKekEncryptAlg':jnxGdoiGmKekEncryptAlg,'jnxGdoiGmKekEncryptKeyLength':jnxGdoiGmKekEncryptKeyLength,'jnxGdoiGmKekSigHashAlg':jnxGdoiGmKekSigHashAlg,'jnxGdoiGmKekSigAlg':jnxGdoiGmKekSigAlg,'jnxGdoiGmKekSigKeyLength':jnxGdoiGmKekSigKeyLength,'jnxGdoiGmKekOakleyGroup':jnxGdoiGmKekOakleyGroup,'jnxGdoiGmKekOriginalLifetime':jnxGdoiGmKekOriginalLifetime,'jnxGdoiGmKekRemainingLifetime':jnxGdoiGmKekRemainingLifetime,'jnxGdoiGmKekStatus':jnxGdoiGmKekStatus,'jnxGdoiGmTekSelectorTable':jnxGdoiGmTekSelectorTable,'jnxGdoiGmTekSelectorEntry':jnxGdoiGmTekSelectorEntry,_N:jnxGdoiGmTekSelectorIndex,'jnxGdoiGmTekSrcIdType':jnxGdoiGmTekSrcIdType,'jnxGdoiGmTekSrcIdLength':jnxGdoiGmTekSrcIdLength,'jnxGdoiGmTekSrcIdValue':jnxGdoiGmTekSrcIdValue,'jnxGdoiGmTekSrcIdPort':jnxGdoiGmTekSrcIdPort,'jnxGdoiGmTekDstIdType':jnxGdoiGmTekDstIdType,'jnxGdoiGmTekDstIdLength':jnxGdoiGmTekDstIdLength,'jnxGdoiGmTekDstIdValue':jnxGdoiGmTekDstIdValue,'jnxGdoiGmTekDstIdPort':jnxGdoiGmTekDstIdPort,'jnxGdoiGmTekSecurityProtocol':jnxGdoiGmTekSecurityProtocol,'jnxGdoiGmTekPolicyMismatchAction':jnxGdoiGmTekPolicyMismatchAction,'jnxGdoiGmTekPolicyTable':jnxGdoiGmTekPolicyTable,'jnxGdoiGmTekPolicyEntry':jnxGdoiGmTekPolicyEntry,_R:jnxGdoiGmTekPolicyIndex,'jnxGdoiGmTekSPI':jnxGdoiGmTekSPI,'jnxGdoiGmTekEncapsulationMode':jnxGdoiGmTekEncapsulationMode,'jnxGdoiGmTekEncryptionAlgorithm':jnxGdoiGmTekEncryptionAlgorithm,'jnxGdoiGmTekEncryptionKeyLength':jnxGdoiGmTekEncryptionKeyLength,'jnxGdoiGmTekIntegrityAlgorithm':jnxGdoiGmTekIntegrityAlgorithm,'jnxGdoiGmTekIntegrityKeyLength':jnxGdoiGmTekIntegrityKeyLength,'jnxGdoiGmTekWindowSize':jnxGdoiGmTekWindowSize,'jnxGdoiGmTekOriginalLifetime':jnxGdoiGmTekOriginalLifetime,'jnxGdoiGmTekRemainingLifetime':jnxGdoiGmTekRemainingLifetime,'jnxGdoiGmTekStatus':jnxGdoiGmTekStatus})