#
# PySNMP MIB module TROPIC-BREAKER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nokia/TROPIC-BREAKER-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:39:20 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("TROPIC-BREAKER-MIB", tnBreakerObjs=tnBreakerObjs, tnBreakerCompliances=tnBreakerCompliances, tnBreakerBasics=tnBreakerBasics, tnBreakerCompliance=tnBreakerCompliance, tnPowerFilterEntry=tnPowerFilterEntry, PYSNMP_MODULE_ID=tnBreakerMibModule, tnPowerFilterTable=tnPowerFilterTable, tnPowerFilterAmpRating=tnPowerFilterAmpRating, tnPowerFilterGroup=tnPowerFilterGroup, tnBreakerConf=tnBreakerConf, tnBreakerMibModule=tnBreakerMibModule, tnBreakerGroups=tnBreakerGroups, tnPowerFilterCardPower=tnPowerFilterCardPower)
