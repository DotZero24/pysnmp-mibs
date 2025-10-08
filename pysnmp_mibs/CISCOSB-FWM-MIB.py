#
# PySNMP MIB module CISCOSB-FWM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ciscosb/CISCOSB-FWM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:56:38 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CISCOSB-FWM-MIB", rlFwmVersionInactive=rlFwmVersionInactive, rlFwmIndex=rlFwmIndex, rlFwmTable=rlFwmTable, rlFwmVersionActive=rlFwmVersionActive, rlFwmUpdateAvailable=rlFwmUpdateAvailable, rlFwmUnitIndex=rlFwmUnitIndex, rlFwmEntry=rlFwmEntry, PYSNMP_MODULE_ID=rlFwm, rlFwmForceAutoUpdate=rlFwmForceAutoUpdate, rlFwm=rlFwm, rlFwmEntity=rlFwmEntity, rlFwmVersionUpdate=rlFwmVersionUpdate, EntityType=EntityType)
