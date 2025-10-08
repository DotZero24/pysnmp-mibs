#
# PySNMP MIB module URI-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/rfc/URI-TC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:27:40 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, TimeTicks, MibIdentifier, Integer32, Bits, mib_2, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "TimeTicks", "MibIdentifier", "Integer32", "Bits", "mib-2", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
uriTcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 164))
uriTcMIB.setRevisions(('2007-09-10 00:00',))
if mibBuilder.loadTexts: uriTcMIB.setLastUpdated('200709100000Z')
if mibBuilder.loadTexts: uriTcMIB.setOrganization('IETF Operations and Management (OPS) Area')
class Uri(TextualConvention, OctetString):
    reference = 'RFC 3986 STD 66 and RFC 3305'
    status = 'current'
    displayHint = '1a'

class Uri255(TextualConvention, OctetString):
    reference = 'RFC 3986 STD 66 and RFC 3305'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class Uri1024(TextualConvention, OctetString):
    reference = 'RFC 3986 STD 66 and RFC 3305'
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

mibBuilder.exportSymbols("URI-TC-MIB", Uri255=Uri255, uriTcMIB=uriTcMIB, Uri1024=Uri1024, PYSNMP_MODULE_ID=uriTcMIB, Uri=Uri)
