#
# PySNMP MIB module SYNOLOGY-COREDUMPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/synology/SYNOLOGY-COREDUMPS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:53 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("SYNOLOGY-COREDUMPS-MIB", coredumpEntry=coredumpEntry, coredumpInfoIndex=coredumpInfoIndex, synologyCoredumpConformance=synologyCoredumpConformance, synologyCoredump=synologyCoredump, synology=synology, coredumpFilePath=coredumpFilePath, PYSNMP_MODULE_ID=synologyCoredump, synologyCoredumpGroup=synologyCoredumpGroup, synologyCoredumpGroups=synologyCoredumpGroups, coredumpTable=coredumpTable, synologyCoredumpCompliances=synologyCoredumpCompliances, synologyCoredumpCompliance=synologyCoredumpCompliance, coredumpTimestamp=coredumpTimestamp)
