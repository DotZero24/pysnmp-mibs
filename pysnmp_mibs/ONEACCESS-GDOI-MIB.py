#
# PySNMP MIB module ONEACCESS-GDOI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/oneaccess/ONEACCESS-GDOI-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:04 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
oacExpIMManagement, = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacExpIMManagement")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
oacExpIMGdoiMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224))
if mibBuilder.loadTexts: oacExpIMGdoiMIB.setLastUpdated('1404151200Z')
if mibBuilder.loadTexts: oacExpIMGdoiMIB.setOrganization('ONE ACCESS')
class OacGdoiIdentificationType(TextualConvention, Integer32):
    reference = "IANA ISAKMP Registry - 'Magic Numbers' for ISAKMP Protocol Section: IPSEC Identification Type http://www.iana.org/assignments/isakmp-registry"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("keyID", 1), ("ipv4", 2))

class OacGdoiIdentificationValue(TextualConvention, OctetString):
    reference = "IANA ISAKMP Registry - 'Magic Numbers' for ISAKMP Protocol Section: IPSEC Identification Type http://www.iana.org/assignments/isakmp-registry"
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class OacGdoiSPI(TextualConvention, OctetString):
    reference = 'RFC 3547 - Section: 5.3. SA KEK Payload'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(32, 32)
    fixedLength = 32

class OacGdoiKEKEncryptionAlgorithm(TextualConvention, Integer32):
    reference = "IANA IKEv2 Parameters Section: Encryption Algorithm Transform IDs http://www.iana.org/assignments/ikev2-parameters IANA 'Magic Numbers' for ISAMP Protocol Section: IPSEC ESP Transform Identifiers http://www.iana.org/assignments/isakmp-registry RFC 2407 - Section: 4.4.4. IPSEC ESP Transform Identifiers RFC 3547 - Section: 5.3.3. KEK_ALGORITHM RFC 4306 - Section: 3.3.2. Transform Substructure RFC 4106, 4309, 4543, 5282, 5529"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("enc-des", 1), ("enc-3des", 2), ("enc-aes", 3))

class OacGdoiHashAlogrithm(TextualConvention, Integer32):
    reference = 'IANA IKEv2 Parameters Section: Pseudo-random Function Transform IDs http://www.iana.org/assignments/ikev2-parameters RFC 3547 - Section: 5.3.6. SIG_HASH_ALGORITHM RFC 4306 - Section: 3.3.2. Transform Substructure RFC 4615, 4868'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("md5", 1), ("sha1", 2))

class OacGdoiSignatureMethod(TextualConvention, Integer32):
    reference = 'IANA IKEv2 Parameters Section: Integrity Algorithm Transform IDs http://www.iana.org/assignments/ikev2-parameters RFC 2407 - Section: 4.5. IPSEC Security Assoc. Attributes RFC 3547 - Section: 5.3.6. SIG_HASH_ALGORITHM RFC 4306 - Section: 3.3.2. Transform Substructure RFC 4494, 4543, 4595, 4868'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("rsa", 1), ("dss", 2), ("ecdss", 3))

oacGdoiMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1))
oacGdoiGroupTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 1), )
if mibBuilder.loadTexts: oacGdoiGroupTable.setStatus('current')
oacGdoiGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 1, 1), ).setIndexNames((0, "ONEACCESS-GDOI-MIB", "oacGdoiGroupName"))
if mibBuilder.loadTexts: oacGdoiGroupEntry.setStatus('current')
oacGdoiGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGroupName.setStatus('current')
oacGdoiGroupIdType = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 1, 1, 2), OacGdoiIdentificationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGroupIdType.setStatus('current')
oacGdoiGroupIdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 1, 1, 3), OacGdoiIdentificationValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGroupIdValue.setStatus('current')
oacGdoiGm = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2))
oacGdoiPolicy = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3))
oacGdoiGmTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2), )
if mibBuilder.loadTexts: oacGdoiGmTable.setStatus('current')
oacGdoiGmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2, 1), ).setIndexNames((0, "ONEACCESS-GDOI-MIB", "oacGdoiGroupName"), (0, "ONEACCESS-GDOI-MIB", "oacGdoiGmActiveKEK"))
if mibBuilder.loadTexts: oacGdoiGmEntry.setStatus('current')
oacGdoiGmIdType = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2, 1, 1), OacGdoiIdentificationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmIdType.setStatus('current')
oacGdoiGmIdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2, 1, 2), OacGdoiIdentificationValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmIdValue.setStatus('current')
oacGdoiGmRegKeyServerIdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2, 1, 3), OacGdoiIdentificationValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmRegKeyServerIdValue.setStatus('current')
oacGdoiGmActiveKEK = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2, 1, 4), OacGdoiSPI()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmActiveKEK.setStatus('current')
oacGdoiGmRekeysReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 2, 2, 1, 5), Counter32()).setUnits('GROUPKEY-PUSH Messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmRekeysReceived.setStatus('current')
oacGdoiGmKekTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2), )
if mibBuilder.loadTexts: oacGdoiGmKekTable.setStatus('current')
oacGdoiGmKekEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1), ).setIndexNames((0, "ONEACCESS-GDOI-MIB", "oacGdoiGroupName"), (0, "ONEACCESS-GDOI-MIB", "oacGdoiGmKekSPI"))
if mibBuilder.loadTexts: oacGdoiGmKekEntry.setStatus('current')
oacGdoiGmKekSPI = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 1), OacGdoiSPI()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekSPI.setStatus('current')
oacGdoiGmKekSrcIdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 2), OacGdoiIdentificationValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekSrcIdValue.setStatus('current')
oacGdoiGmKekDstIdValue = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 3), OacGdoiIdentificationValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekDstIdValue.setStatus('current')
oacGdoiGmKekEncryptAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 4), OacGdoiKEKEncryptionAlgorithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekEncryptAlg.setStatus('current')
oacGdoiGmKekEncryptKeyLength = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 5), Unsigned32()).setUnits('Bits').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekEncryptKeyLength.setStatus('current')
oacGdoiGmKekSigHashAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 6), OacGdoiHashAlogrithm()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekSigHashAlg.setStatus('current')
oacGdoiGmKekSigAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 7), OacGdoiSignatureMethod()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekSigAlg.setStatus('current')
oacGdoiGmKekSigKeyLength = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 8), Unsigned32()).setUnits('Bits').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekSigKeyLength.setStatus('current')
oacGdoiGmKekOriginalLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 9), Unsigned32()).setUnits('Seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekOriginalLifetime.setStatus('current')
oacGdoiGmKekRemainingLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 1224, 1, 3, 2, 1, 10), Unsigned32()).setUnits('Seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacGdoiGmKekRemainingLifetime.setStatus('current')
mibBuilder.exportSymbols("ONEACCESS-GDOI-MIB", oacGdoiGm=oacGdoiGm, oacGdoiGmRegKeyServerIdValue=oacGdoiGmRegKeyServerIdValue, OacGdoiSignatureMethod=OacGdoiSignatureMethod, oacGdoiGmIdType=oacGdoiGmIdType, oacGdoiGmEntry=oacGdoiGmEntry, oacGdoiGmActiveKEK=oacGdoiGmActiveKEK, oacGdoiGmKekSigHashAlg=oacGdoiGmKekSigHashAlg, oacGdoiGmIdValue=oacGdoiGmIdValue, OacGdoiIdentificationType=OacGdoiIdentificationType, oacGdoiGmKekOriginalLifetime=oacGdoiGmKekOriginalLifetime, oacGdoiGmKekSrcIdValue=oacGdoiGmKekSrcIdValue, oacExpIMGdoiMIB=oacExpIMGdoiMIB, OacGdoiSPI=OacGdoiSPI, OacGdoiKEKEncryptionAlgorithm=OacGdoiKEKEncryptionAlgorithm, oacGdoiMIBObjects=oacGdoiMIBObjects, oacGdoiPolicy=oacGdoiPolicy, oacGdoiGmKekDstIdValue=oacGdoiGmKekDstIdValue, oacGdoiGmKekSigKeyLength=oacGdoiGmKekSigKeyLength, oacGdoiGmTable=oacGdoiGmTable, oacGdoiGroupEntry=oacGdoiGroupEntry, oacGdoiGmKekTable=oacGdoiGmKekTable, oacGdoiGroupName=oacGdoiGroupName, oacGdoiGmKekEncryptAlg=oacGdoiGmKekEncryptAlg, oacGdoiGmKekSigAlg=oacGdoiGmKekSigAlg, oacGdoiGmKekEntry=oacGdoiGmKekEntry, OacGdoiIdentificationValue=OacGdoiIdentificationValue, PYSNMP_MODULE_ID=oacExpIMGdoiMIB, oacGdoiGmKekSPI=oacGdoiGmKekSPI, oacGdoiGroupIdType=oacGdoiGroupIdType, OacGdoiHashAlogrithm=OacGdoiHashAlogrithm, oacGdoiGmKekEncryptKeyLength=oacGdoiGmKekEncryptKeyLength, oacGdoiGmRekeysReceived=oacGdoiGmRekeysReceived, oacGdoiGroupIdValue=oacGdoiGroupIdValue, oacGdoiGroupTable=oacGdoiGroupTable, oacGdoiGmKekRemainingLifetime=oacGdoiGmKekRemainingLifetime)
