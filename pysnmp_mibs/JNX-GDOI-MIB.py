#
# PySNMP MIB module JNX-GDOI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/juniper/JNX-GDOI-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:31:25 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention, TimeInterval = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TimeInterval")
jnxGdoiMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 759))
if mibBuilder.loadTexts: jnxGdoiMIB.setLastUpdated('201801040000Z')
if mibBuilder.loadTexts: jnxGdoiMIB.setOrganization('Juniper Networks, Inc.')
class JnxGdoiIdentificationType(TextualConvention, Integer32):
    reference = "IANA ISAKMP Registry - 'Magic Numbers' for ISAKMP Protocol Section: IPSEC Identification Type http://www.iana.org/assignments/isakmp-registry RFC 4306 - Section: 3.5. Identification Payloads"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("ipv4Address", 1), ("domainName", 2), ("userName", 3), ("ipv4Subnet", 4), ("ipv6Address", 5), ("ipv6Subnet", 6), ("ipv4Range", 7), ("ipv6Range", 8), ("caDistinguishedName", 9), ("caGeneralName", 10), ("groupNumber", 11))

class JnxGdoiIdentificationValue(TextualConvention, OctetString):
    reference = "IANA ISAKMP Registry - 'Magic Numbers' for ISAKMP Protocol Section: IPSEC Identification Type http://www.iana.org/assignments/isakmp-registry RFC 4306 - Section: 3.5. Identification Payloads"
    status = 'current'
    displayHint = '255d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 48)

class JnxGdoiKekSPI(TextualConvention, OctetString):
    reference = 'RFC 3547 - Section: 5.3. SA KEK Payload'
    status = 'current'
    displayHint = '16x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class JnxGdoiIpProtocolId(TextualConvention, Integer32):
    reference = 'RFC 3547 - Section: 5.3. SA KEK Payload'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("ipProtocolUnknown", 0), ("ipProtocolTCP", 1), ("ipProtocolUDP", 2))

class JnxGdoiKeyManagementAlgorithm(TextualConvention, Integer32):
    reference = 'RFC 3547 - Section: 5.3. SA KEK Payload'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("keyMgmtNone", 0), ("keyMgmtLkh", 1))

class JnxGdoiEncryptionAlgorithm(TextualConvention, Integer32):
    reference = "IANA IKEv2 Parameters Section: Encryption Algorithm Transform IDs http://www.iana.org/assignments/ikev2-parameters IANA 'Magic Numbers' for ISAMP Protocol Section: IPSEC ESP Transform Identifiers http://www.iana.org/assignments/isakmp-registry RFC 2407 - Section: 4.4.4. IPSEC ESP Transform Identifiers RFC 3547 - Section: 5.3.3. KEK_ALGORITHM RFC 4306 - Section: 3.3.2. Transform Substructure RFC 4106, 4309, 4543, 5282, 5529"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28))
    namedValues = NamedValues(("encrAlgNone", 0), ("encrAlgDes64", 1), ("encrAlgDes", 2), ("encrAlg3Des", 3), ("encrAlgRc5", 4), ("encrAlgIdea", 5), ("encrAlgCast", 6), ("encrAlgBlowfish", 7), ("encrAlg3Idea", 8), ("encrAlgDes32", 9), ("encrAlgRc4", 10), ("encrAlgNull", 11), ("encrAlgAesCbc", 12), ("encrAlgAesCtr", 13), ("encrAlgAesCcm8", 14), ("encrAlgAesCcm12", 15), ("encrAlgAesCcm16", 16), ("encrAlgAesGcm8", 18), ("encrAlgAesGcm12", 19), ("encrAlgAesGcm16", 20), ("encrAlgNullAuthAesGmac", 21), ("encrAlgCamelliaCbc", 23), ("encrAlgCamelliaCtr", 24), ("encrAlgCamelliaCcm8", 25), ("encrAlgCamelliaCcm12", 26), ("encrAlgCamelliaCcm1", 27), ("encrAlgSeedCbc", 28))

class JnxGdoiPseudoRandomFunction(TextualConvention, Integer32):
    reference = 'IANA IKEv2 Parameters Section: Pseudo-random Function Transform IDs http://www.iana.org/assignments/ikev2-parameters RFC 3547 - Section: 5.3.6. SIG_HASH_ALGORITHM RFC 4306 - Section: 3.3.2. Transform Substructure RFC 4615, 4868'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("prfNone", 0), ("prfMd5Hmac", 1), ("prfSha1Hmac", 2), ("prfTigerHmac", 3), ("prfAes128Xcbc", 4), ("prfSha2Hmac256", 5), ("prfSha2Hmac384", 6), ("prfSha2Hmac512", 7), ("prfAes128Cmac", 8))

class JnxGdoiIntegrityAlgorithm(TextualConvention, Integer32):
    reference = 'IANA IKEv2 Parameters Section: Integrity Algorithm Transform IDs http://www.iana.org/assignments/ikev2-parameters RFC 2407 - Section: 4.5. IPSEC Security Assoc. Attributes RFC 3547 - Section: 5.3.6. SIG_HASH_ALGORITHM RFC 4306 - Section: 3.3.2. Transform Substructure RFC 4494, 4543, 4595, 4868'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("authAlgNone", 0), ("authAlgMd5Hmac96", 1), ("authAlgSha1Hmac96", 2), ("authAlgDesMac", 3), ("authAlgMd5Kpdk", 4), ("authAlgAesXcbc96", 5), ("authAlgMd5Hmac128", 6), ("authAlgSha1Hmac160", 7), ("authAlgAesCmac96", 8), ("authAlgAes128Gmac", 9), ("authAlgAes192Gmac", 10), ("authAlgAes256Gmac", 11), ("authAlgSha2Hmac256to128", 12), ("authAlgSha2Hmac384to192", 13), ("authAlgSha2Hmac512to256", 14))

class JnxGdoiSignatureMethod(TextualConvention, Integer32):
    reference = 'IANA IKEv2 Parameters Section: Integrity Algorithm Transform IDs http://www.iana.org/assignments/ikev2-parameters RFC 2409 - Section: Appendix A. Authentication Method RFC 3547 - Sections: 5.3.SA KEK payload 5.3.7. SIG_ALGORITHM RFC 4306 - Section: 3.8.Authentication Payload RFC 4754'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 9, 10, 11))
    namedValues = NamedValues(("sigNone", 0), ("sigRsa", 1), ("sigSharedKey", 2), ("sigDss", 3), ("sigEncryptRsa", 4), ("sigRevEncryptRsa", 5), ("sigEcdsa256", 9), ("sigEcdsa384", 10), ("sigEcdsa512", 11))

class JnxGdoiDiffieHellmanGroup(TextualConvention, Integer32):
    reference = 'IANA IKEv2 Parameters Section: Diffie-Hellman Group Transform IDs http://www.iana.org/assignments/ikev2-parameters RFC 2409 - Sections: 6.1. First Oakley Default Group 6.2. Second Oakley Default Group 6.3. Third Oakley Default Group 6.4. Fourth Oakley Default Group'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26))
    namedValues = NamedValues(("dhNone", 0), ("dhGroup1", 1), ("dhGroup2", 2), ("dhEc2nGp155", 3), ("dhEc2nGp185", 4), ("dh1536Modp", 5), ("dh2048Modp", 14), ("dh3072Modp", 15), ("dh4096Modp", 16), ("dh6144Modp", 17), ("dh8192Modp", 18), ("dhEcp256", 19), ("dhEcp84", 20), ("dhEcp521", 21), ("dh1024Modp160", 22), ("dh2048Modp224", 23), ("dh2048Modp256", 24), ("dhEcp192", 25), ("dhEcp224", 26))

class JnxGdoiEncapsulationMode(TextualConvention, Integer32):
    reference = "IANA 'Magic Numbers' for ISAKMP Protocol Section: Encapsulation Mode http://www.iana.org/assignments/isakmp-registry RFC 2407 - Section: 4.5. IPSEC Security Assoc. Attributes RFC 3947"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("encapUnknown", 0), ("encapTunnel", 1), ("encapTransport", 2), ("encapUdpTunnel", 3), ("encapUdpTransport", 4))

class JnxGdoiSecurityProtocol(TextualConvention, Integer32):
    reference = 'RFC 3547 - Section: 5.4. SA TEK Payload'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("secProtocolUnknown", 0), ("secProtocolIpsecEsp", 1))

class JnxGdoiTekSPI(TextualConvention, OctetString):
    reference = 'RFC 3547 - Section: 5.4.1. PROTO_IPSEC_ESP'
    status = 'current'
    displayHint = '4x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class JnxGdoiKekStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("inUse", 1), ("new", 2), ("old", 3))

class JnxGdoiTekStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("inbound", 1), ("outbound", 2), ("biDirectional", 3))

class JnxGdoiUnsigned16(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 2)
    fixedLength = 2

class JnxGdoiPolicyMismatchAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("drop", 1), ("forward", 2), ("unknown", 3))

jnxGdoiMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 759, 0))
jnxGdoiMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1))
jnxGdoiGmRegister = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 759, 0, 5)).setObjects(("JNX-GDOI-MIB", "jnxGdoiGmRegKeyServerIdType"), ("JNX-GDOI-MIB", "jnxGdoiGmRegKeyServerIdValue"))
if mibBuilder.loadTexts: jnxGdoiGmRegister.setStatus('current')
jnxGdoiGmRegistrationComplete = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 759, 0, 6)).setObjects(("JNX-GDOI-MIB", "jnxGdoiGmRegKeyServerIdType"), ("JNX-GDOI-MIB", "jnxGdoiGmRegKeyServerIdValue"))
if mibBuilder.loadTexts: jnxGdoiGmRegistrationComplete.setStatus('current')
jnxGdoiGmReRegister = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 759, 0, 7)).setObjects(("JNX-GDOI-MIB", "jnxGdoiGmRegKeyServerIdType"), ("JNX-GDOI-MIB", "jnxGdoiGmRegKeyServerIdValue"))
if mibBuilder.loadTexts: jnxGdoiGmReRegister.setStatus('current')
jnxGdoiGmRekeyReceived = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 759, 0, 8)).setObjects(("JNX-GDOI-MIB", "jnxGdoiGmRegKeyServerIdType"), ("JNX-GDOI-MIB", "jnxGdoiGmRegKeyServerIdValue"), ("JNX-GDOI-MIB", "jnxGdoiGmRekeysReceived"))
if mibBuilder.loadTexts: jnxGdoiGmRekeyReceived.setStatus('current')
jnxGdoiGmRekeyFailure = NotificationType((1, 3, 6, 1, 4, 1, 2636, 3, 759, 0, 11)).setObjects(("JNX-GDOI-MIB", "jnxGdoiGmRegKeyServerIdType"), ("JNX-GDOI-MIB", "jnxGdoiGmRegKeyServerIdValue"), ("JNX-GDOI-MIB", "jnxGdoiGmRekeysReceived"))
if mibBuilder.loadTexts: jnxGdoiGmRekeyFailure.setStatus('current')
jnxGdoiGroupTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 1), )
if mibBuilder.loadTexts: jnxGdoiGroupTable.setStatus('current')
jnxGdoiGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 1, 1), ).setIndexNames((0, "JNX-GDOI-MIB", "jnxGdoiGroupIdType"), (0, "JNX-GDOI-MIB", "jnxGdoiGroupIdValue"))
if mibBuilder.loadTexts: jnxGdoiGroupEntry.setStatus('current')
jnxGdoiGroupIdType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 1, 1, 1), JnxGdoiIdentificationType())
if mibBuilder.loadTexts: jnxGdoiGroupIdType.setStatus('current')
jnxGdoiGroupIdLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 1, 1, 2), Unsigned32()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGroupIdLength.setStatus('current')
jnxGdoiGroupIdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 1, 1, 3), JnxGdoiIdentificationValue())
if mibBuilder.loadTexts: jnxGdoiGroupIdValue.setStatus('current')
jnxGdoiGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGroupName.setStatus('current')
jnxGdoiPeers = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 2))
jnxGdoiSecAssociations = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3))
jnxGdoiGmTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 2, 2), )
if mibBuilder.loadTexts: jnxGdoiGmTable.setStatus('current')
jnxGdoiGmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 2, 2, 1), ).setIndexNames((0, "JNX-GDOI-MIB", "jnxGdoiGroupIdType"), (0, "JNX-GDOI-MIB", "jnxGdoiGroupIdValue"), (0, "JNX-GDOI-MIB", "jnxGdoiGmIdType"), (0, "JNX-GDOI-MIB", "jnxGdoiGmIdValue"))
if mibBuilder.loadTexts: jnxGdoiGmEntry.setStatus('current')
jnxGdoiGmIdType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 2, 2, 1, 1), JnxGdoiIdentificationType())
if mibBuilder.loadTexts: jnxGdoiGmIdType.setStatus('current')
jnxGdoiGmIdLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 2, 2, 1, 2), Unsigned32()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmIdLength.setStatus('current')
jnxGdoiGmIdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 2, 2, 1, 3), JnxGdoiIdentificationValue())
if mibBuilder.loadTexts: jnxGdoiGmIdValue.setStatus('current')
jnxGdoiGmRegKeyServerIdType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 2, 2, 1, 4), JnxGdoiIdentificationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmRegKeyServerIdType.setStatus('current')
jnxGdoiGmRegKeyServerIdLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 2, 2, 1, 5), Unsigned32()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmRegKeyServerIdLength.setStatus('current')
jnxGdoiGmRegKeyServerIdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 2, 2, 1, 6), JnxGdoiIdentificationValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmRegKeyServerIdValue.setStatus('current')
jnxGdoiGmActiveKEK = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 2, 2, 1, 7), JnxGdoiKekSPI()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmActiveKEK.setStatus('current')
jnxGdoiGmRekeysReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 2, 2, 1, 8), Counter32()).setUnits('GROUPKEY-PUSH Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmRekeysReceived.setStatus('current')
jnxGdoiGmActiveTEKNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 2, 2, 1, 9), Counter32()).setUnits('Number of traffic encryption keys').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmActiveTEKNum.setStatus('current')
jnxGdoiGmKekTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 2), )
if mibBuilder.loadTexts: jnxGdoiGmKekTable.setStatus('current')
jnxGdoiGmKekEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 2, 1), ).setIndexNames((0, "JNX-GDOI-MIB", "jnxGdoiGroupIdType"), (0, "JNX-GDOI-MIB", "jnxGdoiGroupIdValue"), (0, "JNX-GDOI-MIB", "jnxGdoiGmIdType"), (0, "JNX-GDOI-MIB", "jnxGdoiGmIdValue"), (0, "JNX-GDOI-MIB", "jnxGdoiGmKekIndex"))
if mibBuilder.loadTexts: jnxGdoiGmKekEntry.setStatus('current')
jnxGdoiGmKekIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: jnxGdoiGmKekIndex.setStatus('current')
jnxGdoiGmKekSPI = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 2, 1, 2), JnxGdoiKekSPI()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmKekSPI.setStatus('current')
jnxGdoiGmKekSrcIdType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 2, 1, 3), JnxGdoiIdentificationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmKekSrcIdType.setStatus('current')
jnxGdoiGmKekSrcIdLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 2, 1, 4), Unsigned32()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmKekSrcIdLength.setStatus('current')
jnxGdoiGmKekSrcIdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 2, 1, 5), JnxGdoiIdentificationValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmKekSrcIdValue.setStatus('current')
jnxGdoiGmKekSrcIdPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 2, 1, 6), JnxGdoiUnsigned16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmKekSrcIdPort.setStatus('current')
jnxGdoiGmKekDstIdType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 2, 1, 7), JnxGdoiIdentificationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmKekDstIdType.setStatus('current')
jnxGdoiGmKekDstIdLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 2, 1, 8), Unsigned32()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmKekDstIdLength.setStatus('current')
jnxGdoiGmKekDstIdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 2, 1, 9), JnxGdoiIdentificationValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmKekDstIdValue.setStatus('current')
jnxGdoiGmKekDstIdPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 2, 1, 10), JnxGdoiUnsigned16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmKekDstIdPort.setStatus('current')
jnxGdoiGmKekIpProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 2, 1, 11), JnxGdoiIpProtocolId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmKekIpProtocol.setStatus('current')
jnxGdoiGmKekMgmtAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 2, 1, 12), JnxGdoiKeyManagementAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmKekMgmtAlg.setStatus('current')
jnxGdoiGmKekEncryptAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 2, 1, 13), JnxGdoiEncryptionAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmKekEncryptAlg.setStatus('current')
jnxGdoiGmKekEncryptKeyLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 2, 1, 14), Unsigned32()).setUnits('Bits').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmKekEncryptKeyLength.setStatus('current')
jnxGdoiGmKekSigHashAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 2, 1, 15), JnxGdoiPseudoRandomFunction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmKekSigHashAlg.setStatus('current')
jnxGdoiGmKekSigAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 2, 1, 16), JnxGdoiSignatureMethod()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmKekSigAlg.setStatus('current')
jnxGdoiGmKekSigKeyLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 2, 1, 17), Unsigned32()).setUnits('Bits').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmKekSigKeyLength.setStatus('current')
jnxGdoiGmKekOakleyGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 2, 1, 18), JnxGdoiDiffieHellmanGroup()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmKekOakleyGroup.setStatus('current')
jnxGdoiGmKekOriginalLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 2, 1, 19), Unsigned32()).setUnits('Seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmKekOriginalLifetime.setStatus('current')
jnxGdoiGmKekRemainingLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 2, 1, 20), Unsigned32()).setUnits('Seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmKekRemainingLifetime.setStatus('current')
jnxGdoiGmKekStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 2, 1, 21), JnxGdoiKekStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmKekStatus.setStatus('current')
jnxGdoiGmTekSelectorTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 5), )
if mibBuilder.loadTexts: jnxGdoiGmTekSelectorTable.setStatus('current')
jnxGdoiGmTekSelectorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 5, 1), ).setIndexNames((0, "JNX-GDOI-MIB", "jnxGdoiGroupIdType"), (0, "JNX-GDOI-MIB", "jnxGdoiGroupIdValue"), (0, "JNX-GDOI-MIB", "jnxGdoiGmIdType"), (0, "JNX-GDOI-MIB", "jnxGdoiGmIdValue"), (0, "JNX-GDOI-MIB", "jnxGdoiGmTekSelectorIndex"))
if mibBuilder.loadTexts: jnxGdoiGmTekSelectorEntry.setStatus('current')
jnxGdoiGmTekSelectorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 5, 1, 1), Unsigned32())
if mibBuilder.loadTexts: jnxGdoiGmTekSelectorIndex.setStatus('current')
jnxGdoiGmTekSrcIdType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 5, 1, 2), JnxGdoiIdentificationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmTekSrcIdType.setStatus('current')
jnxGdoiGmTekSrcIdLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 5, 1, 3), Unsigned32()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmTekSrcIdLength.setStatus('current')
jnxGdoiGmTekSrcIdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 5, 1, 4), JnxGdoiIdentificationValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmTekSrcIdValue.setStatus('current')
jnxGdoiGmTekSrcIdPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 5, 1, 5), JnxGdoiUnsigned16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmTekSrcIdPort.setStatus('current')
jnxGdoiGmTekDstIdType = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 5, 1, 6), JnxGdoiIdentificationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmTekDstIdType.setStatus('current')
jnxGdoiGmTekDstIdLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 5, 1, 7), Unsigned32()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmTekDstIdLength.setStatus('current')
jnxGdoiGmTekDstIdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 5, 1, 8), JnxGdoiIdentificationValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmTekDstIdValue.setStatus('current')
jnxGdoiGmTekDstIdPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 5, 1, 9), JnxGdoiUnsigned16()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmTekDstIdPort.setStatus('current')
jnxGdoiGmTekSecurityProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 5, 1, 10), JnxGdoiSecurityProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmTekSecurityProtocol.setStatus('current')
jnxGdoiGmTekPolicyMismatchAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 5, 1, 11), JnxGdoiPolicyMismatchAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmTekPolicyMismatchAction.setStatus('current')
jnxGdoiGmTekPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 6), )
if mibBuilder.loadTexts: jnxGdoiGmTekPolicyTable.setStatus('current')
jnxGdoiGmTekPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 6, 1), ).setIndexNames((0, "JNX-GDOI-MIB", "jnxGdoiGroupIdType"), (0, "JNX-GDOI-MIB", "jnxGdoiGroupIdValue"), (0, "JNX-GDOI-MIB", "jnxGdoiGmIdType"), (0, "JNX-GDOI-MIB", "jnxGdoiGmIdValue"), (0, "JNX-GDOI-MIB", "jnxGdoiGmTekSelectorIndex"), (0, "JNX-GDOI-MIB", "jnxGdoiGmTekPolicyIndex"))
if mibBuilder.loadTexts: jnxGdoiGmTekPolicyEntry.setStatus('current')
jnxGdoiGmTekPolicyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 6, 1, 1), Unsigned32())
if mibBuilder.loadTexts: jnxGdoiGmTekPolicyIndex.setStatus('current')
jnxGdoiGmTekSPI = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 6, 1, 2), JnxGdoiTekSPI()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmTekSPI.setStatus('current')
jnxGdoiGmTekEncapsulationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 6, 1, 3), JnxGdoiEncapsulationMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmTekEncapsulationMode.setStatus('current')
jnxGdoiGmTekEncryptionAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 6, 1, 4), JnxGdoiEncryptionAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmTekEncryptionAlgorithm.setStatus('current')
jnxGdoiGmTekEncryptionKeyLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 6, 1, 5), Unsigned32()).setUnits('Bits').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmTekEncryptionKeyLength.setStatus('current')
jnxGdoiGmTekIntegrityAlgorithm = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 6, 1, 6), JnxGdoiIntegrityAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmTekIntegrityAlgorithm.setStatus('current')
jnxGdoiGmTekIntegrityKeyLength = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 6, 1, 7), Unsigned32()).setUnits('Bits').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmTekIntegrityKeyLength.setStatus('current')
jnxGdoiGmTekWindowSize = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 6, 1, 8), Unsigned32()).setUnits('GROUPKEY-PUSH Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmTekWindowSize.setStatus('current')
jnxGdoiGmTekOriginalLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 6, 1, 9), Unsigned32()).setUnits('Seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmTekOriginalLifetime.setStatus('current')
jnxGdoiGmTekRemainingLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 6, 1, 10), Unsigned32()).setUnits('Seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmTekRemainingLifetime.setStatus('current')
jnxGdoiGmTekStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 759, 1, 3, 6, 1, 11), JnxGdoiTekStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxGdoiGmTekStatus.setStatus('current')
mibBuilder.exportSymbols("JNX-GDOI-MIB", jnxGdoiGmRegKeyServerIdValue=jnxGdoiGmRegKeyServerIdValue, jnxGdoiGmKekEncryptKeyLength=jnxGdoiGmKekEncryptKeyLength, jnxGdoiGmTekPolicyMismatchAction=jnxGdoiGmTekPolicyMismatchAction, JnxGdoiSecurityProtocol=JnxGdoiSecurityProtocol, JnxGdoiKeyManagementAlgorithm=JnxGdoiKeyManagementAlgorithm, jnxGdoiGmTekIntegrityKeyLength=jnxGdoiGmTekIntegrityKeyLength, JnxGdoiIntegrityAlgorithm=JnxGdoiIntegrityAlgorithm, jnxGdoiGmActiveTEKNum=jnxGdoiGmActiveTEKNum, jnxGdoiGmTekSecurityProtocol=jnxGdoiGmTekSecurityProtocol, jnxGdoiGmRekeyReceived=jnxGdoiGmRekeyReceived, jnxGdoiGmTekSrcIdPort=jnxGdoiGmTekSrcIdPort, JnxGdoiKekStatus=JnxGdoiKekStatus, jnxGdoiGmTekPolicyIndex=jnxGdoiGmTekPolicyIndex, jnxGdoiPeers=jnxGdoiPeers, jnxGdoiGmKekSrcIdValue=jnxGdoiGmKekSrcIdValue, jnxGdoiGmActiveKEK=jnxGdoiGmActiveKEK, JnxGdoiIdentificationType=JnxGdoiIdentificationType, jnxGdoiGroupTable=jnxGdoiGroupTable, JnxGdoiIdentificationValue=JnxGdoiIdentificationValue, jnxGdoiGmKekSigHashAlg=jnxGdoiGmKekSigHashAlg, jnxGdoiGmKekSrcIdLength=jnxGdoiGmKekSrcIdLength, jnxGdoiGmTekWindowSize=jnxGdoiGmTekWindowSize, jnxGdoiGmKekSPI=jnxGdoiGmKekSPI, jnxGdoiGmTekPolicyTable=jnxGdoiGmTekPolicyTable, jnxGdoiGmTekDstIdValue=jnxGdoiGmTekDstIdValue, jnxGdoiGmKekSigAlg=jnxGdoiGmKekSigAlg, jnxGdoiGmTekDstIdLength=jnxGdoiGmTekDstIdLength, jnxGdoiGmRekeysReceived=jnxGdoiGmRekeysReceived, JnxGdoiTekStatus=JnxGdoiTekStatus, jnxGdoiGroupEntry=jnxGdoiGroupEntry, jnxGdoiGmTekEncryptionKeyLength=jnxGdoiGmTekEncryptionKeyLength, jnxGdoiGmIdLength=jnxGdoiGmIdLength, jnxGdoiGmTekDstIdPort=jnxGdoiGmTekDstIdPort, jnxGdoiMIBNotifications=jnxGdoiMIBNotifications, jnxGdoiGmTekSelectorTable=jnxGdoiGmTekSelectorTable, jnxGdoiGmReRegister=jnxGdoiGmReRegister, jnxGdoiGmTekEncryptionAlgorithm=jnxGdoiGmTekEncryptionAlgorithm, jnxGdoiGmTekPolicyEntry=jnxGdoiGmTekPolicyEntry, jnxGdoiGmRegister=jnxGdoiGmRegister, jnxGdoiGmKekEncryptAlg=jnxGdoiGmKekEncryptAlg, jnxGdoiGmTekRemainingLifetime=jnxGdoiGmTekRemainingLifetime, jnxGdoiGmKekIndex=jnxGdoiGmKekIndex, JnxGdoiPseudoRandomFunction=JnxGdoiPseudoRandomFunction, jnxGdoiGmIdValue=jnxGdoiGmIdValue, jnxGdoiGmKekTable=jnxGdoiGmKekTable, jnxGdoiGmRegistrationComplete=jnxGdoiGmRegistrationComplete, jnxGdoiGmKekRemainingLifetime=jnxGdoiGmKekRemainingLifetime, JnxGdoiEncryptionAlgorithm=JnxGdoiEncryptionAlgorithm, jnxGdoiGmKekSigKeyLength=jnxGdoiGmKekSigKeyLength, jnxGdoiGmKekDstIdPort=jnxGdoiGmKekDstIdPort, jnxGdoiMIBObjects=jnxGdoiMIBObjects, jnxGdoiGmKekSrcIdPort=jnxGdoiGmKekSrcIdPort, jnxGdoiGmTekStatus=jnxGdoiGmTekStatus, PYSNMP_MODULE_ID=jnxGdoiMIB, jnxGdoiGmKekSrcIdType=jnxGdoiGmKekSrcIdType, jnxGdoiGmKekDstIdValue=jnxGdoiGmKekDstIdValue, jnxGdoiGmTekSrcIdValue=jnxGdoiGmTekSrcIdValue, JnxGdoiSignatureMethod=JnxGdoiSignatureMethod, jnxGdoiSecAssociations=jnxGdoiSecAssociations, jnxGdoiGmTable=jnxGdoiGmTable, jnxGdoiGmKekIpProtocol=jnxGdoiGmKekIpProtocol, jnxGdoiGmTekSrcIdType=jnxGdoiGmTekSrcIdType, JnxGdoiKekSPI=JnxGdoiKekSPI, jnxGdoiGmTekIntegrityAlgorithm=jnxGdoiGmTekIntegrityAlgorithm, jnxGdoiGmRekeyFailure=jnxGdoiGmRekeyFailure, jnxGdoiGmKekDstIdLength=jnxGdoiGmKekDstIdLength, jnxGdoiGroupIdType=jnxGdoiGroupIdType, jnxGdoiGmTekDstIdType=jnxGdoiGmTekDstIdType, jnxGdoiGmKekOriginalLifetime=jnxGdoiGmKekOriginalLifetime, JnxGdoiIpProtocolId=JnxGdoiIpProtocolId, JnxGdoiTekSPI=JnxGdoiTekSPI, jnxGdoiGmTekSelectorIndex=jnxGdoiGmTekSelectorIndex, jnxGdoiGmRegKeyServerIdLength=jnxGdoiGmRegKeyServerIdLength, jnxGdoiGroupIdLength=jnxGdoiGroupIdLength, jnxGdoiGroupName=jnxGdoiGroupName, jnxGdoiGmEntry=jnxGdoiGmEntry, JnxGdoiDiffieHellmanGroup=JnxGdoiDiffieHellmanGroup, jnxGdoiMIB=jnxGdoiMIB, JnxGdoiEncapsulationMode=JnxGdoiEncapsulationMode, jnxGdoiGmKekOakleyGroup=jnxGdoiGmKekOakleyGroup, jnxGdoiGmTekSrcIdLength=jnxGdoiGmTekSrcIdLength, jnxGdoiGmRegKeyServerIdType=jnxGdoiGmRegKeyServerIdType, jnxGdoiGmTekSelectorEntry=jnxGdoiGmTekSelectorEntry, jnxGdoiGmKekEntry=jnxGdoiGmKekEntry, jnxGdoiGmKekMgmtAlg=jnxGdoiGmKekMgmtAlg, jnxGdoiGmIdType=jnxGdoiGmIdType, jnxGdoiGroupIdValue=jnxGdoiGroupIdValue, jnxGdoiGmTekSPI=jnxGdoiGmTekSPI, jnxGdoiGmKekStatus=jnxGdoiGmKekStatus, JnxGdoiUnsigned16=JnxGdoiUnsigned16, jnxGdoiGmTekEncapsulationMode=jnxGdoiGmTekEncapsulationMode, JnxGdoiPolicyMismatchAction=JnxGdoiPolicyMismatchAction, jnxGdoiGmTekOriginalLifetime=jnxGdoiGmTekOriginalLifetime, jnxGdoiGmKekDstIdType=jnxGdoiGmKekDstIdType)
