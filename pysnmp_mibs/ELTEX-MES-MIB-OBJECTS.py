#
# PySNMP MIB module ELTEX-MES-MIB-OBJECTS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-MES-MIB-OBJECTS
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:50 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltMesIfMIBObjects, = mibBuilder.importSymbols("ELTEX-MES-IF-MIB", "eltMesIfMIBObjects")
ifEntry, = mibBuilder.importSymbols("IF-MIB", "ifEntry")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eltIfExtTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1, 31, 1, 1), )
if mibBuilder.loadTexts: eltIfExtTable.setStatus('current')
eltIfExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1, 31, 1, 1, 1), )
ifEntry.registerAugmentions(("ELTEX-MES-MIB-OBJECTS", "eltIfExtEntry"))
eltIfExtEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: eltIfExtEntry.setStatus('current')
eltIfLongDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1, 31, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltIfLongDescr.setStatus('current')
eltIfAdminMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1, 31, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(128, 9000), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltIfAdminMtu.setStatus('current')
eltIfUpDownTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1, 31, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltIfUpDownTrapEnable.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-MIB-OBJECTS", eltIfExtEntry=eltIfExtEntry, eltIfLongDescr=eltIfLongDescr, eltIfUpDownTrapEnable=eltIfUpDownTrapEnable, eltIfAdminMtu=eltIfAdminMtu, eltIfExtTable=eltIfExtTable)
