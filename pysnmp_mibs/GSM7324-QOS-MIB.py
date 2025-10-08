#
# PySNMP MIB module GSM7324-QOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/netgear/GSM7324-QOS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:28:37 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
gsm7324, = mibBuilder.importSymbols("GSM7324-REF-MIB", "gsm7324")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
gsm7324QOS = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 1, 7, 3))
gsm7324QOS.setRevisions(('2003-05-06 12:00',))
if mibBuilder.loadTexts: gsm7324QOS.setLastUpdated('200305061200Z')
if mibBuilder.loadTexts: gsm7324QOS.setOrganization('Netgear')
mibBuilder.exportSymbols("GSM7324-QOS-MIB", PYSNMP_MODULE_ID=gsm7324QOS, gsm7324QOS=gsm7324QOS)
