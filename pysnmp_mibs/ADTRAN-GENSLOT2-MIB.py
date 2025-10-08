#
# PySNMP MIB module ADTRAN-GENSLOT2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/adtran/ADTRAN-GENSLOT2-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:29:06 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
adGenSlotInfoIndex, adGenSlot = mibBuilder.importSymbols("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex", "adGenSlot")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenSlot2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 5))
if mibBuilder.loadTexts: adGenSlot2.setLastUpdated('200809250000Z')
if mibBuilder.loadTexts: adGenSlot2.setOrganization('ADTRAN, Inc.')
adGenSlot2ProdTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 6), )
if mibBuilder.loadTexts: adGenSlot2ProdTable.setStatus('current')
adGenSlot2ProdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 6, 1), ).setIndexNames((0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
if mibBuilder.loadTexts: adGenSlot2ProdEntry.setStatus('current')
adGenSlotProdHwRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 6, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenSlotProdHwRevision.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-GENSLOT2-MIB", adGenSlot2=adGenSlot2, adGenSlot2ProdTable=adGenSlot2ProdTable, adGenSlotProdHwRevision=adGenSlotProdHwRevision, adGenSlot2ProdEntry=adGenSlot2ProdEntry, PYSNMP_MODULE_ID=adGenSlot2)
