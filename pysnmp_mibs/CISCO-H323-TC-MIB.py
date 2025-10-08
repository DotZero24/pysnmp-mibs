#
# PySNMP MIB module CISCO-H323-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-H323-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:16:22 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoH323TCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 41))
ciscoH323TCMIB.setRevisions(('1998-10-09 12:00', '2000-03-10 00:00',))
if mibBuilder.loadTexts: ciscoH323TCMIB.setLastUpdated('200003100000Z')
if mibBuilder.loadTexts: ciscoH323TCMIB.setOrganization('Cisco Systems, Inc')
class CgkIA5String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class CgkE164String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class CgkTAddressTag(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("other", 0), ("ipv4", 1), ("ipv6", 2), ("ipx", 3), ("nsap", 4))

class CgkNAddressTag(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("other", 0), ("ipv4", 1), ("ipv6", 2), ("ipx", 3), ("nsap", 4))

class CgkNAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class CgkGlobalIdentifier(TextualConvention, OctetString):
    reference = 'ITU-T H225.0, Version 2 section 7.6'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class CgkAliasTag(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 0), ("e164", 1), ("h323Id", 2), ("urlId", 3), ("transportId", 4), ("emailId", 5), ("partyNumber", 6))

class CgkAliasAddress(TextualConvention, OctetString):
    reference = 'ITU-T H225.0 Version 2 ANNEX H - H.225.0 Message Syntax (ASN.1)'
    status = 'current'
    displayHint = '512a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 512)

class CgkEndpointID(TextualConvention, OctetString):
    reference = 'ITU-T H225.0 Version 2 ANNEX H - H.225.0 Message Syntax (ASN.1)'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class CgkGatekeeperID(TextualConvention, OctetString):
    reference = 'ITU-T H225.0 Version 2 ANNEX H - H.225.0 Message Syntax (ASN.1)'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

mibBuilder.exportSymbols("CISCO-H323-TC-MIB", CgkGatekeeperID=CgkGatekeeperID, PYSNMP_MODULE_ID=ciscoH323TCMIB, CgkNAddressTag=CgkNAddressTag, CgkNAddress=CgkNAddress, CgkE164String=CgkE164String, CgkTAddressTag=CgkTAddressTag, ciscoH323TCMIB=ciscoH323TCMIB, CgkIA5String=CgkIA5String, CgkAliasTag=CgkAliasTag, CgkGlobalIdentifier=CgkGlobalIdentifier, CgkEndpointID=CgkEndpointID, CgkAliasAddress=CgkAliasAddress)
