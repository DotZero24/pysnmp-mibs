#
# PySNMP MIB module XEROX-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/xerox/XEROX-COMMON-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:06:17 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xerox = ModuleIdentity((1, 3, 6, 1, 4, 1, 253))
if mibBuilder.loadTexts: xerox.setLastUpdated('0209170000Z')
if mibBuilder.loadTexts: xerox.setOrganization('Xerox Corporation - Xerox Common Management Interface Working Group')
xeroxCommonMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 253, 8))
if mibBuilder.loadTexts: xeroxCommonMIB.setStatus('current')
mibBuilder.exportSymbols("XEROX-COMMON-MIB", xeroxCommonMIB=xeroxCommonMIB, PYSNMP_MODULE_ID=xerox, xerox=xerox)
