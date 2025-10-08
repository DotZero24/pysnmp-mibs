#
# PySNMP MIB module URI-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/rfc/URI-TC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:50:08 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "mib-2")
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

mibBuilder.exportSymbols("URI-TC-MIB", Uri=Uri, Uri1024=Uri1024, Uri255=Uri255, PYSNMP_MODULE_ID=uriTcMIB, uriTcMIB=uriTcMIB)
