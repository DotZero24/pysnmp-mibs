#
# PySNMP MIB module NETGEAR-RADLAN-DEBUGCAPABILITIES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/netgear/NETGEAR-RADLAN-DEBUGCAPABILITIES-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:28:20 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("NETGEAR-RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlDebugCapabilities = ModuleIdentity((1, 3, 6, 1, 4, 1, 4526, 17, 206))
rlDebugCapabilities.setRevisions(('2011-01-05 00:00',))
if mibBuilder.loadTexts: rlDebugCapabilities.setLastUpdated('201101050000Z')
if mibBuilder.loadTexts: rlDebugCapabilities.setOrganization('Radlan - a MARVELL company. Marvell Semiconductor, Inc.')
rlDebugCapabilitiesPassword = MibScalar((1, 3, 6, 1, 4, 1, 4526, 17, 206, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDebugCapabilitiesPassword.setStatus('current')
mibBuilder.exportSymbols("NETGEAR-RADLAN-DEBUGCAPABILITIES-MIB", PYSNMP_MODULE_ID=rlDebugCapabilities, rlDebugCapabilitiesPassword=rlDebugCapabilitiesPassword, rlDebugCapabilities=rlDebugCapabilities)
