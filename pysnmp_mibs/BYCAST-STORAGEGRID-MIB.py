#
# PySNMP MIB module BYCAST-STORAGEGRID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/netapp/BYCAST-STORAGEGRID-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:59:11 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("BYCAST-STORAGEGRID-MIB", PYSNMP_MODULE_ID=bycast, label=label, version1=version1, common=common, status=status, nmsmi=nmsmi, bycast=bycast, system=system)
