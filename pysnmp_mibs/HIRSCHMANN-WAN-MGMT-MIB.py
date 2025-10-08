#
# PySNMP MIB module HIRSCHMANN-WAN-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hirschmann/HIRSCHMANN-WAN-MGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:17 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hmWanMgmt, = mibBuilder.importSymbols("HIRSCHMANN-WAN-MIB", "hmWanMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hmWanMgmtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 40, 1, 9))
hmWanMgmtMib.setRevisions(('2016-08-09 00:00',))
if mibBuilder.loadTexts: hmWanMgmtMib.setLastUpdated('201608090000Z')
if mibBuilder.loadTexts: hmWanMgmtMib.setOrganization('Hirschmann Automation and Control GmbH')
hmWanMgmtAutomaticUpdate = MibScalar((1, 3, 6, 1, 4, 1, 248, 40, 1, 9, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("idle", 1), ("triggered", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmWanMgmtAutomaticUpdate.setStatus('current')
mibBuilder.exportSymbols("HIRSCHMANN-WAN-MGMT-MIB", PYSNMP_MODULE_ID=hmWanMgmtMib, hmWanMgmtMib=hmWanMgmtMib, hmWanMgmtAutomaticUpdate=hmWanMgmtAutomaticUpdate)
