#
# PySNMP MIB module TROPIC-BREAKER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nokia/TROPIC-BREAKER-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:20:53 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tnMiscModules, tnBreakerMIB = mibBuilder.importSymbols("TROPIC-GLOBAL-REG", "tnMiscModules", "tnBreakerMIB")
tnShelfIndex, = mibBuilder.importSymbols("TROPIC-SHELF-MIB", "tnShelfIndex")
tnSlotIndex, = mibBuilder.importSymbols("TROPIC-SLOT-MIB", "tnSlotIndex")
tnBreakerMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 7483, 1, 1, 2, 2, 5, 2))
tnBreakerMibModule.setRevisions(('2018-02-23 12:00', '2016-11-16 12:00', '2013-05-21 12:00', '2012-09-13 12:00', '2011-05-23 12:00', '2011-04-14 12:00', '2010-10-18 12:00', '2009-08-13 12:00',))
if mibBuilder.loadTexts: tnBreakerMibModule.setLastUpdated('201802231200Z')
if mibBuilder.loadTexts: tnBreakerMibModule.setOrganization('Nokia')
tnBreakerConf = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 2, 1))
tnBreakerGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 2, 1, 1))
tnBreakerCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 2, 1, 2))
tnBreakerObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 2, 2))
tnBreakerBasics = MibIdentifier((1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 2, 2, 1))
tnPowerFilterTable = MibTable((1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 2, 2, 1, 2), )
if mibBuilder.loadTexts: tnPowerFilterTable.setStatus('current')
tnPowerFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 2, 2, 1, 2, 1), ).setIndexNames((0, "TROPIC-SHELF-MIB", "tnShelfIndex"), (0, "TROPIC-SLOT-MIB", "tnSlotIndex"))
if mibBuilder.loadTexts: tnPowerFilterEntry.setStatus('current')
tnPowerFilterAmpRating = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 2, 2, 1, 2, 1, 1), Integer32()).setUnits('1/10 amps').setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPowerFilterAmpRating.setStatus('current')
tnPowerFilterCardPower = MibTableColumn((1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 2, 2, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 100))).setUnits('watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: tnPowerFilterCardPower.setStatus('current')
tnPowerFilterGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 2, 1, 1, 2)).setObjects(("TROPIC-BREAKER-MIB", "tnPowerFilterAmpRating"), ("TROPIC-BREAKER-MIB", "tnPowerFilterCardPower"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnPowerFilterGroup = tnPowerFilterGroup.setStatus('current')
tnBreakerCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7483, 2, 2, 5, 2, 1, 2, 1)).setObjects(("TROPIC-BREAKER-MIB", "tnPowerFilterGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tnBreakerCompliance = tnBreakerCompliance.setStatus('current')
mibBuilder.exportSymbols("TROPIC-BREAKER-MIB", tnBreakerGroups=tnBreakerGroups, tnPowerFilterTable=tnPowerFilterTable, tnBreakerMibModule=tnBreakerMibModule, tnPowerFilterGroup=tnPowerFilterGroup, PYSNMP_MODULE_ID=tnBreakerMibModule, tnBreakerCompliances=tnBreakerCompliances, tnBreakerBasics=tnBreakerBasics, tnBreakerConf=tnBreakerConf, tnPowerFilterCardPower=tnPowerFilterCardPower, tnPowerFilterAmpRating=tnPowerFilterAmpRating, tnBreakerObjs=tnBreakerObjs, tnPowerFilterEntry=tnPowerFilterEntry, tnBreakerCompliance=tnBreakerCompliance)
