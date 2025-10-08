#
# PySNMP MIB module FS-NMS-POE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/FS-NMS-POE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:42 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
nmslocal, = mibBuilder.importSymbols("FS-NMS-SMI", "nmslocal")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Integer32, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, TimeTicks, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Integer32", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "TimeTicks", "Bits", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
poe = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 2, 236))
powerEtherTable = MibTable((1, 3, 6, 1, 4, 1, 52642, 2, 236, 1), )
if mibBuilder.loadTexts: powerEtherTable.setStatus('mandatory')
powerEtherTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52642, 2, 236, 1, 1), ).setIndexNames((0, "FS-NMS-POE-MIB", "ifIndex"))
if mibBuilder.loadTexts: powerEtherTableEntry.setStatus('mandatory')
ifIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 2, 236, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifIndex.setStatus('mandatory')
ifDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 2, 236, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifDescr.setStatus('mandatory')
ifPethPortControlAbility = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 2, 236, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifPethPortControlAbility.setStatus('mandatory')
ifPethPortMaxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 2, 236, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifPethPortMaxPower.setStatus('mandatory')
ifPethPortConsumptionPower = MibTableColumn((1, 3, 6, 1, 4, 1, 52642, 2, 236, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifPethPortConsumptionPower.setStatus('mandatory')
mibBuilder.exportSymbols("FS-NMS-POE-MIB", ifDescr=ifDescr, poe=poe, ifIndex=ifIndex, ifPethPortMaxPower=ifPethPortMaxPower, powerEtherTableEntry=powerEtherTableEntry, ifPethPortControlAbility=ifPethPortControlAbility, ifPethPortConsumptionPower=ifPethPortConsumptionPower, powerEtherTable=powerEtherTable)
