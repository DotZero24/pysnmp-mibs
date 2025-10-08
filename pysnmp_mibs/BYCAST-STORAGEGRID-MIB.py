#
# PySNMP MIB module BYCAST-STORAGEGRID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/netapp/BYCAST-STORAGEGRID-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:57:32 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bycast = ModuleIdentity((1, 3, 6, 1, 4, 1, 28669))
bycast.setRevisions(('2007-06-07 17:25',))
if mibBuilder.loadTexts: bycast.setLastUpdated('200706071725Z')
if mibBuilder.loadTexts: bycast.setOrganization('NetApp Inc.')
version1 = MibIdentifier((1, 3, 6, 1, 4, 1, 28669, 1))
common = MibIdentifier((1, 3, 6, 1, 4, 1, 28669, 1, 0))
nmsmi = MibIdentifier((1, 3, 6, 1, 4, 1, 28669, 1, 0, 1))
system = MibIdentifier((1, 3, 6, 1, 4, 1, 28669, 1, 0, 1, 1))
status = MibScalar((1, 3, 6, 1, 4, 1, 28669, 1, 0, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 11, 21, 31, 41, 51, 61))).clone(namedValues=NamedValues(("unknown", 1), ("adminDown", 11), ("normal", 21), ("notice", 31), ("minor", 41), ("major", 51), ("critical", 61)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: status.setStatus('current')
label = MibScalar((1, 3, 6, 1, 4, 1, 28669, 1, 0, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: label.setStatus('current')
mibBuilder.exportSymbols("BYCAST-STORAGEGRID-MIB", common=common, PYSNMP_MODULE_ID=bycast, bycast=bycast, nmsmi=nmsmi, version1=version1, label=label, status=status, system=system)
