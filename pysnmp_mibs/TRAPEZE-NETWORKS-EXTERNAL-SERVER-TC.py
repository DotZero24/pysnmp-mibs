#
# PySNMP MIB module TRAPEZE-NETWORKS-EXTERNAL-SERVER-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/trapeze/TRAPEZE-NETWORKS-EXTERNAL-SERVER-TC
# Produced by pysmi-1.1.12 at Wed Oct  8 11:05:20 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzExternalServerTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 23))
trpzExternalServerTc.setRevisions(('2012-02-16 00:01',))
if mibBuilder.loadTexts: trpzExternalServerTc.setLastUpdated('201202160001Z')
if mibBuilder.loadTexts: trpzExternalServerTc.setOrganization('Trapeze Networks')
class TrpzSyslogSeverity(TextualConvention, Integer32):
    reference = 'RFC 5424, section 6.2.1.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("emergency", 1), ("alert", 2), ("critical", 3), ("error", 4), ("warning", 5), ("notice", 6), ("informational", 7), ("debug", 8))

mibBuilder.exportSymbols("TRAPEZE-NETWORKS-EXTERNAL-SERVER-TC", PYSNMP_MODULE_ID=trpzExternalServerTc, trpzExternalServerTc=trpzExternalServerTc, TrpzSyslogSeverity=TrpzSyslogSeverity)
