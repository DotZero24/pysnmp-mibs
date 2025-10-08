#
# PySNMP MIB module CIENA-GLOBAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ciena/CIENA-GLOBAL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:16 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cienaCommon, = mibBuilder.importSymbols("CIENA-SMI", "cienaCommon")
CienaGlobalSeverity, = mibBuilder.importSymbols("CIENA-TC", "CienaGlobalSeverity")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
cienaGlobal = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271, 1, 3))
cienaGlobal.setRevisions(('2017-06-07 00:00', '2010-03-28 00:00',))
if mibBuilder.loadTexts: cienaGlobal.setLastUpdated('201706070000Z')
if mibBuilder.loadTexts: cienaGlobal.setOrganization('Ciena Corp.')
cienaGlobalSeverity = MibScalar((1, 3, 6, 1, 4, 1, 1271, 1, 3, 1), CienaGlobalSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cienaGlobalSeverity.setStatus('current')
cienaGlobalMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 1271, 1, 3, 2), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cienaGlobalMacAddress.setStatus('current')
mibBuilder.exportSymbols("CIENA-GLOBAL-MIB", cienaGlobalSeverity=cienaGlobalSeverity, cienaGlobalMacAddress=cienaGlobalMacAddress, PYSNMP_MODULE_ID=cienaGlobal, cienaGlobal=cienaGlobal)
