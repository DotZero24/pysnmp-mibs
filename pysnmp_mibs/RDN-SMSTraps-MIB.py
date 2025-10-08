#
# PySNMP MIB module RDN-SMSTraps-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/riverdelta/RDN-SMSTraps-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:18 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
docsIfCmtsCmStatusMacAddress, docsIfCmtsCmStatusValue = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress", "docsIfCmtsCmStatusValue")
riverdelta, = mibBuilder.importSymbols("RDN-MIB", "riverdelta")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, NotificationType, enterprises, Gauge32, Integer32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, Unsigned32, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "NotificationType", "enterprises", "Gauge32", "Integer32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "Unsigned32", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rdnSubscriberTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 5))
rdnCableModemV1Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 5, 1))
rdnCableModemStatusV1 = NotificationType((1, 3, 6, 1, 4, 1, 4981) + (0,1)).setObjects(("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusValue"))
rdnCableModemV2Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 4981, 5, 2))
rdnCableModemStatusV2 = NotificationType((1, 3, 6, 1, 4, 1, 4981, 5, 2, 1)).setObjects(("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"), ("DOCS-IF-MIB", "docsIfCmtsCmStatusValue"))
if mibBuilder.loadTexts: rdnCableModemStatusV2.setStatus('current')
mibBuilder.exportSymbols("RDN-SMSTraps-MIB", rdnCableModemStatusV2=rdnCableModemStatusV2, rdnCableModemStatusV1=rdnCableModemStatusV1, rdnCableModemV1Traps=rdnCableModemV1Traps, rdnSubscriberTraps=rdnSubscriberTraps, rdnCableModemV2Traps=rdnCableModemV2Traps)
