#
# PySNMP MIB module RDN-SMSTraps-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/riverdelta/RDN-SMSTraps-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:16:07 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
docsIfCmtsCmStatusMacAddress, docsIfCmtsCmStatusValue = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress", "docsIfCmtsCmStatusValue")
riverdelta, = mibBuilder.importSymbols("RDN-MIB", "riverdelta")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, NotificationType, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "NotificationType", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rdnSubscriberTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 5))
rdnCableModemV1Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 5, 1))
rdnCableModemStatusV1 = NotificationType((1, 3, 6, 1, 4, 1, 4981) + (0,1)).setObjects(("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusValue"))
rdnCableModemV2Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 5, 2))
rdnCableModemStatusV2 = NotificationType((1, 3, 6, 1, 4, 1, 4981, 5, 2, 1)).setObjects(("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusValue"))
if mibBuilder.loadTexts: rdnCableModemStatusV2.setStatus('current')
mibBuilder.exportSymbols("RDN-SMSTraps-MIB", rdnCableModemStatusV1=rdnCableModemStatusV1, rdnCableModemV1Traps=rdnCableModemV1Traps, rdnCableModemStatusV2=rdnCableModemStatusV2, rdnSubscriberTraps=rdnSubscriberTraps, rdnCableModemV2Traps=rdnCableModemV2Traps)
