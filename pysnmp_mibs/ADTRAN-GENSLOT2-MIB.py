#
# PySNMP MIB module ADTRAN-GENSLOT2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/adtran/ADTRAN-GENSLOT2-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:52:10 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
adGenSlot, adGenSlotInfoIndex = mibBuilder.importSymbols("ADTRAN-GENSLOT-MIB", "adGenSlot", "adGenSlotInfoIndex")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adGenSlot2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 5))
if mibBuilder.loadTexts: adGenSlot2.setLastUpdated('200809250000Z')
if mibBuilder.loadTexts: adGenSlot2.setOrganization('ADTRAN, Inc.')
adGenSlot2ProdTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 6), )
if mibBuilder.loadTexts: adGenSlot2ProdTable.setStatus('current')
adGenSlot2ProdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 6, 1), ).setIndexNames((0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
if mibBuilder.loadTexts: adGenSlot2ProdEntry.setStatus('current')
adGenSlotProdHwRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 13, 2, 6, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenSlotProdHwRevision.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-GENSLOT2-MIB", adGenSlot2=adGenSlot2, adGenSlotProdHwRevision=adGenSlotProdHwRevision, PYSNMP_MODULE_ID=adGenSlot2, adGenSlot2ProdTable=adGenSlot2ProdTable, adGenSlot2ProdEntry=adGenSlot2ProdEntry)
