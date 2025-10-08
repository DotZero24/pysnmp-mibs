#
# PySNMP MIB module CENTRECOM-PORT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/allied-old/CENTRECOM-PORT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:08:11 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
extSwitchMIB, = mibBuilder.importSymbols("CENTRECOM-MIB", "extSwitchMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
atiPort = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 6))
if mibBuilder.loadTexts: atiPort.setLastUpdated('9802030000Z')
if mibBuilder.loadTexts: atiPort.setOrganization('Allied Telesis K.K')
atiPortLoadshareTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 6, 1), )
if mibBuilder.loadTexts: atiPortLoadshareTable.setStatus('mandatory')
atiPortLoadshareEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 6, 1, 1), ).setIndexNames((0, "CENTRECOM-PORT-MIB", "atiPortLoadshareMasterIfIndex"), (0, "CENTRECOM-PORT-MIB", "atiPortLoadshareSlaveIfIndex"))
if mibBuilder.loadTexts: atiPortLoadshareEntry.setStatus('mandatory')
atiPortLoadshareMasterIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 6, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiPortLoadshareMasterIfIndex.setStatus('mandatory')
atiPortLoadshareSlaveIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 6, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiPortLoadshareSlaveIfIndex.setStatus('mandatory')
atiPortLoadshareGrouping = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 4))).clone(namedValues=NamedValues(("pair", 2), ("quad", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiPortLoadshareGrouping.setStatus('mandatory')
atiPortLoadshareStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 12, 2, 6, 1, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atiPortLoadshareStatus.setStatus('mandatory')
mibBuilder.exportSymbols("CENTRECOM-PORT-MIB", atiPortLoadshareSlaveIfIndex=atiPortLoadshareSlaveIfIndex, atiPortLoadshareTable=atiPortLoadshareTable, atiPortLoadshareGrouping=atiPortLoadshareGrouping, atiPortLoadshareMasterIfIndex=atiPortLoadshareMasterIfIndex, atiPortLoadshareStatus=atiPortLoadshareStatus, PYSNMP_MODULE_ID=atiPort, atiPortLoadshareEntry=atiPortLoadshareEntry, atiPort=atiPort)
