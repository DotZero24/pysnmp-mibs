#
# PySNMP MIB module EAP-CLIENTTABLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/tplink/EAP-CLIENTTABLE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:32 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
clientStatis, = mibBuilder.importSymbols("EAP-CLIENT-MIB", "clientStatis")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
clientTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 10, 1, 1, 2), )
if mibBuilder.loadTexts: clientTable.setStatus('current')
clientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 10, 1, 1, 2, 1), ).setIndexNames((0, "EAP-CLIENTTABLE-MIB", "clientIndex"))
if mibBuilder.loadTexts: clientEntry.setStatus('current')
clientIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 10, 1, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: clientIndex.setStatus('current')
macAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 10, 1, 1, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: macAddress.setStatus('current')
mibBuilder.exportSymbols("EAP-CLIENTTABLE-MIB", clientTable=clientTable, macAddress=macAddress, clientIndex=clientIndex, clientEntry=clientEntry)
