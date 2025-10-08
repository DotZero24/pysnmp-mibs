#
# PySNMP MIB module CIENA-WS-PLATFORM-ENCRYPTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ciena/CIENA-WS-PLATFORM-ENCRYPTION-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:10 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cienaWsPlatformConfig, = mibBuilder.importSymbols("CIENA-WS-MIB", "cienaWsPlatformConfig")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
cienaWsPlatformEncryptionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271, 3, 5, 23))
cienaWsPlatformEncryptionMIB.setRevisions(('2018-08-22 00:00', '2018-07-16 00:00',))
if mibBuilder.loadTexts: cienaWsPlatformEncryptionMIB.setLastUpdated('201808220000Z')
if mibBuilder.loadTexts: cienaWsPlatformEncryptionMIB.setOrganization('Ciena Corporation')
class AuthenticationMaterialType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("preSharedKey", 1), ("certificateECC", 2))

class WarmRestartType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("unknown", 0), ("fips", 1), ("nonFIPS", 2))

channelEncryptionTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 3), )
if mibBuilder.loadTexts: channelEncryptionTable.setStatus('current')
channelEncryptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: channelEncryptionEntry.setStatus('current')
channelDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelDescr.setStatus('current')
peerAuthenticationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("pass", 1), ("fail", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: peerAuthenticationStatus.setStatus('current')
peerAuthenticationStatusUpdateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: peerAuthenticationStatusUpdateTime.setStatus('current')
encryptionPreSharedKeyTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 4), )
if mibBuilder.loadTexts: encryptionPreSharedKeyTable.setStatus('current')
encryptionPreSharedKeyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: encryptionPreSharedKeyEntry.setStatus('current')
encryptionPreSharedChannelDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 4, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: encryptionPreSharedChannelDescr.setStatus('current')
encryptionPreSharedKeyFingerprint = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: encryptionPreSharedKeyFingerprint.setStatus('current')
encryptionPreSharedKeyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 4, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: encryptionPreSharedKeyStatus.setStatus('current')
encryptionPreSharedKeyDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 4, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: encryptionPreSharedKeyDescription.setStatus('current')
systemEncryptionTable = MibTable((1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 5), )
if mibBuilder.loadTexts: systemEncryptionTable.setStatus('current')
systemEncryptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 5, 1), ).setIndexNames((0, "CIENA-WS-PLATFORM-ENCRYPTION-MIB", "systemEncryptionTableSnmpKey"))
if mibBuilder.loadTexts: systemEncryptionEntry.setStatus('current')
systemEncryptionTableSnmpKey = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: systemEncryptionTableSnmpKey.setStatus('current')
authenticationMaterialType = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 5, 1, 2), AuthenticationMaterialType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: authenticationMaterialType.setStatus('current')
warmRestartType = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 5, 1, 3), WarmRestartType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: warmRestartType.setStatus('current')
signingCACertificate = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 5, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: signingCACertificate.setStatus('current')
entityCertificate = MibTableColumn((1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 5, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: entityCertificate.setStatus('current')
cienaWsEncryptionObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 1))
cienaWsEncryptionConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 2))
cienaWsEncryptionGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 2, 1))
cienaWsEncryptionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 2, 1, 1)).setObjects(("CIENA-WS-PLATFORM-ENCRYPTION-MIB", "channelDescr"), ("CIENA-WS-PLATFORM-ENCRYPTION-MIB", "peerAuthenticationStatus"), ("CIENA-WS-PLATFORM-ENCRYPTION-MIB", "peerAuthenticationStatusUpdateTime"), ("CIENA-WS-PLATFORM-ENCRYPTION-MIB", "encryptionPreSharedChannelDescr"), ("CIENA-WS-PLATFORM-ENCRYPTION-MIB", "encryptionPreSharedKeyFingerprint"), ("CIENA-WS-PLATFORM-ENCRYPTION-MIB", "encryptionPreSharedKeyStatus"), ("CIENA-WS-PLATFORM-ENCRYPTION-MIB", "encryptionPreSharedKeyDescription"), ("CIENA-WS-PLATFORM-ENCRYPTION-MIB", "authenticationMaterialType"), ("CIENA-WS-PLATFORM-ENCRYPTION-MIB", "warmRestartType"), ("CIENA-WS-PLATFORM-ENCRYPTION-MIB", "signingCACertificate"), ("CIENA-WS-PLATFORM-ENCRYPTION-MIB", "entityCertificate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cienaWsEncryptionGroup = cienaWsEncryptionGroup.setStatus('current')
cienaWsEncryptionCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 2, 2))
cienaWsEncryptionCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1271, 3, 5, 23, 2, 2, 1)).setObjects(("CIENA-WS-PLATFORM-ENCRYPTION-MIB", "cienaWsEncryptionGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cienaWsEncryptionCompliance = cienaWsEncryptionCompliance.setStatus('current')
mibBuilder.exportSymbols("CIENA-WS-PLATFORM-ENCRYPTION-MIB", encryptionPreSharedKeyDescription=encryptionPreSharedKeyDescription, channelEncryptionEntry=channelEncryptionEntry, encryptionPreSharedKeyFingerprint=encryptionPreSharedKeyFingerprint, encryptionPreSharedKeyStatus=encryptionPreSharedKeyStatus, peerAuthenticationStatus=peerAuthenticationStatus, signingCACertificate=signingCACertificate, WarmRestartType=WarmRestartType, AuthenticationMaterialType=AuthenticationMaterialType, channelEncryptionTable=channelEncryptionTable, warmRestartType=warmRestartType, cienaWsEncryptionObjects=cienaWsEncryptionObjects, systemEncryptionTableSnmpKey=systemEncryptionTableSnmpKey, PYSNMP_MODULE_ID=cienaWsPlatformEncryptionMIB, entityCertificate=entityCertificate, authenticationMaterialType=authenticationMaterialType, cienaWsEncryptionGroups=cienaWsEncryptionGroups, encryptionPreSharedKeyEntry=encryptionPreSharedKeyEntry, cienaWsEncryptionGroup=cienaWsEncryptionGroup, cienaWsEncryptionCompliances=cienaWsEncryptionCompliances, systemEncryptionTable=systemEncryptionTable, cienaWsPlatformEncryptionMIB=cienaWsPlatformEncryptionMIB, channelDescr=channelDescr, systemEncryptionEntry=systemEncryptionEntry, cienaWsEncryptionConformance=cienaWsEncryptionConformance, peerAuthenticationStatusUpdateTime=peerAuthenticationStatusUpdateTime, encryptionPreSharedChannelDescr=encryptionPreSharedChannelDescr, cienaWsEncryptionCompliance=cienaWsEncryptionCompliance, encryptionPreSharedKeyTable=encryptionPreSharedKeyTable)
