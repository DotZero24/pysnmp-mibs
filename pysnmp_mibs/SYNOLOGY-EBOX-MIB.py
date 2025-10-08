#
# PySNMP MIB module SYNOLOGY-EBOX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/synology/SYNOLOGY-EBOX-MIB
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
synologyEbox = ModuleIdentity((1, 3, 6, 1, 4, 1, 6574, 105))
synologyEbox.setRevisions(('2017-06-26 00:00',))
if mibBuilder.loadTexts: synologyEbox.setLastUpdated('201706260000Z')
if mibBuilder.loadTexts: synologyEbox.setOrganization('www.synology.com')
synology = MibIdentifier((1, 3, 6, 1, 4, 1, 6574))
eboxTable = MibTable((1, 3, 6, 1, 4, 1, 6574, 105, 1), )
if mibBuilder.loadTexts: eboxTable.setStatus('current')
eboxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6574, 105, 1, 1), ).setIndexNames((0, "SYNOLOGY-EBOX-MIB", "eboxIndex"))
if mibBuilder.loadTexts: eboxEntry.setStatus('current')
eboxIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 105, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eboxIndex.setStatus('current')
eboxModel = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 105, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eboxModel.setStatus('current')
eboxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 105, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eboxPower.setStatus('current')
eboxRedundantPower = MibTableColumn((1, 3, 6, 1, 4, 1, 6574, 105, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eboxRedundantPower.setStatus('current')
synologyEboxConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 105, 2))
synologyEboxCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 105, 2, 1))
synologyEboxGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6574, 105, 2, 2))
synologyEboxCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6574, 105, 2, 1, 1)).setObjects(("SYNOLOGY-EBOX-MIB", "synologyEboxGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    synologyEboxCompliance = synologyEboxCompliance.setStatus('current')
synologyEboxGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6574, 105, 2, 2, 1)).setObjects(("SYNOLOGY-EBOX-MIB", "eboxIndex"), ("SYNOLOGY-EBOX-MIB", "eboxModel"), ("SYNOLOGY-EBOX-MIB", "eboxPower"), ("SYNOLOGY-EBOX-MIB", "eboxRedundantPower"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    synologyEboxGroup = synologyEboxGroup.setStatus('current')
mibBuilder.exportSymbols("SYNOLOGY-EBOX-MIB", eboxModel=eboxModel, synologyEboxGroups=synologyEboxGroups, synologyEbox=synologyEbox, eboxEntry=eboxEntry, eboxRedundantPower=eboxRedundantPower, synology=synology, PYSNMP_MODULE_ID=synologyEbox, synologyEboxGroup=synologyEboxGroup, synologyEboxCompliances=synologyEboxCompliances, eboxPower=eboxPower, synologyEboxCompliance=synologyEboxCompliance, eboxIndex=eboxIndex, synologyEboxConformance=synologyEboxConformance, eboxTable=eboxTable)
