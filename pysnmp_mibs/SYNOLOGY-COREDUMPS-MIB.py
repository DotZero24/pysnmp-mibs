#
# PySNMP MIB module SYNOLOGY-COREDUMPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/synology/SYNOLOGY-COREDUMPS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:30 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
synologyCoredump = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 201))
synologyCoredump.setRevisions(('2016-05-24 00:00',))
if mibBuilder.loadTexts: synologyCoredump.setLastUpdated('201605240000Z')
if mibBuilder.loadTexts: synologyCoredump.setOrganization('www.synology.com')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
coredumpTable = MibTable((1, 3, 6, 1, 4, 1, 6574, 201, 1), )
if mibBuilder.loadTexts: coredumpTable.setStatus('current')
coredumpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6574, 201, 1, 1), ).setIndexNames((0, "SYNOLOGY-COREDUMPS-MIB", "coredumpInfoIndex"))
if mibBuilder.loadTexts: coredumpEntry.setStatus('current')
coredumpInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 201, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: coredumpInfoIndex.setStatus('current')
coredumpFilePath = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 201, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coredumpFilePath.setStatus('current')
coredumpTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 201, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coredumpTimestamp.setStatus('current')
synologyCoredumpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 201, 2))
synologyCoredumpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 201, 2, 1))
synologyCoredumpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 201, 2, 2))
synologyCoredumpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 201, 2, 1, 1)).setObjects(("SYNOLOGY-COREDUMPS-MIB", "synologyCoredumpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    synologyCoredumpCompliance = synologyCoredumpCompliance.setStatus('current')
synologyCoredumpGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 201, 2, 2, 1)).setObjects(("SYNOLOGY-COREDUMPS-MIB", "coredumpFilePath"), ("SYNOLOGY-COREDUMPS-MIB", "coredumpTimestamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    synologyCoredumpGroup = synologyCoredumpGroup.setStatus('current')
mibBuilder.exportSymbols("SYNOLOGY-COREDUMPS-MIB", synologyCoredumpConformance=synologyCoredumpConformance, synologyCoredumpGroups=synologyCoredumpGroups, coredumpInfoIndex=coredumpInfoIndex, coredumpTable=coredumpTable, synologyCoredumpCompliance=synologyCoredumpCompliance, synologyCoredumpCompliances=synologyCoredumpCompliances, coredumpTimestamp=coredumpTimestamp, coredumpFilePath=coredumpFilePath, synologyCoredumpGroup=synologyCoredumpGroup, synologyCoredump=synologyCoredump, synology=synology, coredumpEntry=coredumpEntry, PYSNMP_MODULE_ID=synologyCoredump)
