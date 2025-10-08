#
# PySNMP MIB module PMIPV6-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/PMIPV6-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:16 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pmip6TCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 205))
pmip6TCMIB.setRevisions(('2012-05-07 00:00',))
if mibBuilder.loadTexts: pmip6TCMIB.setLastUpdated('201205070000Z')
if mibBuilder.loadTexts: pmip6TCMIB.setOrganization('IETF NETLMM Working Group')
class Pmip6TimeStamp64(TextualConvention, OctetString):
    reference = 'RFC 5213: Section 8.8'
    status = 'current'
    displayHint = '6d:2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class Pmip6MnIdentifier(TextualConvention, OctetString):
    reference = 'RFC 4283: Section 3'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class Pmip6MnLLIdentifier(TextualConvention, OctetString):
    reference = 'RFC 5213: Section 8.6'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class Pmip6MnIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class Pmip6MnLLIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class Pmip6MnInterfaceATT(TextualConvention, Integer32):
    reference = 'RFC 5213: Section 8.5, Mobile IPv6 parameters registry on http://www.iana.org/mobility-parameters'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("reserved", 0), ("logicalNetworkInterface", 1), ("pointToPointInterface", 2), ("ethernet", 3), ("wirelessLan", 4), ("wimax", 5), ("threeGPPGERAN", 6), ("threeGPPUTRAN", 7), ("threeGPPEUTRAN", 8), ("threeGPP2eHRPD", 9), ("threeGPP2HRPD", 10), ("threeGPP21xRTT", 11), ("threeGPP2UMB", 12))

mibBuilder.exportSymbols("PMIPV6-TC-MIB", Pmip6MnIdentifier=Pmip6MnIdentifier, Pmip6MnLLIdentifier=Pmip6MnLLIdentifier, pmip6TCMIB=pmip6TCMIB, Pmip6MnInterfaceATT=Pmip6MnInterfaceATT, PYSNMP_MODULE_ID=pmip6TCMIB, Pmip6TimeStamp64=Pmip6TimeStamp64, Pmip6MnIndex=Pmip6MnIndex, Pmip6MnLLIndex=Pmip6MnLLIndex)
