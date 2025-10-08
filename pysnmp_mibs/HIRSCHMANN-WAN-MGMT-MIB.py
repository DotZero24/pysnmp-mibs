#
# PySNMP MIB module HIRSCHMANN-WAN-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hirschmann/HIRSCHMANN-WAN-MGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:22 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hmWanMgmt, = mibBuilder.importSymbols("HIRSCHMANN-WAN-MIB", "hmWanMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hmWanMgmtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 40, 1, 9))
hmWanMgmtMib.setRevisions(('2016-08-09 00:00',))
if mibBuilder.loadTexts: hmWanMgmtMib.setLastUpdated('201608090000Z')
if mibBuilder.loadTexts: hmWanMgmtMib.setOrganization('Hirschmann Automation and Control GmbH')
hmWanMgmtAutomaticUpdate = MibScalar((1, 3, 6, 1, 4, 1, 248, 40, 1, 9, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("idle", 1), ("triggered", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hmWanMgmtAutomaticUpdate.setStatus('current')
mibBuilder.exportSymbols("HIRSCHMANN-WAN-MGMT-MIB", PYSNMP_MODULE_ID=hmWanMgmtMib, hmWanMgmtMib=hmWanMgmtMib, hmWanMgmtAutomaticUpdate=hmWanMgmtAutomaticUpdate)
