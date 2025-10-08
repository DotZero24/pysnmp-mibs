#
# PySNMP MIB module CISCO-TRUSTSEC-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-TRUSTSEC-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:30 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCtsTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 694))
ciscoCtsTcMIB.setRevisions(('2013-06-06 00:00', '2012-01-30 00:00', '2009-05-14 00:00',))
if mibBuilder.loadTexts: ciscoCtsTcMIB.setLastUpdated('201306060000Z')
if mibBuilder.loadTexts: ciscoCtsTcMIB.setOrganization('Cisco Systems, Inc.')
class CtsSecurityGroupTag(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class CtsAclName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class CtsAclNameOrEmpty(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CtsAclList(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 255)

class CtsAclListOrEmpty(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CtsPolicyName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CtsPasswordEncryptionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("none", 2), ("clearText", 3), ("typeSix", 4), ("typeSeven", 5))

class CtsPassword(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

class CtsGenerationId(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 128)

class CtsAcsAuthorityIdentity(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class CtsCredentialRecordType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("simpleSecret", 1), ("pac", 2))

class CtsSgaclMonitorMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("on", 1), ("off", 2))

class CtsSxpConnectionStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("off", 2), ("on", 3), ("pendingOn", 4), ("deleteHoldDown", 5))

mibBuilder.exportSymbols("CISCO-TRUSTSEC-TC-MIB", CtsCredentialRecordType=CtsCredentialRecordType, CtsAcsAuthorityIdentity=CtsAcsAuthorityIdentity, CtsAclList=CtsAclList, PYSNMP_MODULE_ID=ciscoCtsTcMIB, CtsGenerationId=CtsGenerationId, CtsAclName=CtsAclName, ciscoCtsTcMIB=ciscoCtsTcMIB, CtsPassword=CtsPassword, CtsSgaclMonitorMode=CtsSgaclMonitorMode, CtsPasswordEncryptionType=CtsPasswordEncryptionType, CtsSecurityGroupTag=CtsSecurityGroupTag, CtsPolicyName=CtsPolicyName, CtsAclNameOrEmpty=CtsAclNameOrEmpty, CtsSxpConnectionStatus=CtsSxpConnectionStatus, CtsAclListOrEmpty=CtsAclListOrEmpty)
