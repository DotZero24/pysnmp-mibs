#
# PySNMP MIB module CISCOSB-DEBUGCAPABILITIES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ciscosb/CISCOSB-DEBUGCAPABILITIES-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:55:46 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rlDebugCapabilities = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 206))
rlDebugCapabilities.setRevisions(('2011-01-05 00:00',))
if mibBuilder.loadTexts: rlDebugCapabilities.setLastUpdated('201101050000Z')
if mibBuilder.loadTexts: rlDebugCapabilities.setOrganization('Cisco Systems, Inc.')
rlDebugCapabilitiesPassword = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 206, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDebugCapabilitiesPassword.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-DEBUGCAPABILITIES-MIB", rlDebugCapabilitiesPassword=rlDebugCapabilitiesPassword, rlDebugCapabilities=rlDebugCapabilities, PYSNMP_MODULE_ID=rlDebugCapabilities)
