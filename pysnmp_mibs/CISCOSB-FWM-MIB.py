#
# PySNMP MIB module CISCOSB-FWM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ciscosb/CISCOSB-FWM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:32:23 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
rlFwm = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 244))
rlFwm.setRevisions(('2006-02-12 00:00', '2003-10-18 00:00',))
if mibBuilder.loadTexts: rlFwm.setLastUpdated('200602120000Z')
if mibBuilder.loadTexts: rlFwm.setOrganization('Cisco Systems, Inc.')
class EntityType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("not-relevant", 0), ("cpld", 1), ("fpga", 2))

rlFwmTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 244, 1), )
if mibBuilder.loadTexts: rlFwmTable.setStatus('current')
rlFwmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 244, 1, 1), ).setIndexNames((0, "CISCOSB-FWM-MIB", "rlFwmUnitIndex"), (0, "CISCOSB-FWM-MIB", "rlFwmEntity"), (0, "CISCOSB-FWM-MIB", "rlFwmIndex"))
if mibBuilder.loadTexts: rlFwmEntry.setStatus('current')
rlFwmUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 244, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: rlFwmUnitIndex.setStatus('current')
rlFwmEntity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 244, 1, 1, 2), EntityType())
if mibBuilder.loadTexts: rlFwmEntity.setStatus('current')
rlFwmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 244, 1, 1, 3), Integer32())
if mibBuilder.loadTexts: rlFwmIndex.setStatus('current')
rlFwmVersionActive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 244, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFwmVersionActive.setStatus('current')
rlFwmVersionInactive = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 244, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFwmVersionInactive.setStatus('current')
rlFwmUpdateAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 244, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFwmUpdateAvailable.setStatus('current')
rlFwmForceAutoUpdate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 244, 1, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFwmForceAutoUpdate.setStatus('current')
rlFwmVersionUpdate = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 244, 2), EntityType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFwmVersionUpdate.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-FWM-MIB", PYSNMP_MODULE_ID=rlFwm, EntityType=EntityType, rlFwmEntry=rlFwmEntry, rlFwmUnitIndex=rlFwmUnitIndex, rlFwmIndex=rlFwmIndex, rlFwmEntity=rlFwmEntity, rlFwmForceAutoUpdate=rlFwmForceAutoUpdate, rlFwmVersionActive=rlFwmVersionActive, rlFwm=rlFwm, rlFwmVersionUpdate=rlFwmVersionUpdate, rlFwmVersionInactive=rlFwmVersionInactive, rlFwmUpdateAvailable=rlFwmUpdateAvailable, rlFwmTable=rlFwmTable)
