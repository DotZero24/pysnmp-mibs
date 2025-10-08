#
# PySNMP MIB module RAISECOM-NMS-ACC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/raisecom/RAISECOM-NMS-ACC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:54:49 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
raisecomAgent, = mibBuilder.importSymbols("RAISECOM-BASE-MIB", "raisecomAgent")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
raisecomNMSAccessControl = ModuleIdentity((1, 3, 6, 1, 4, 1, 8886, 1, 5))
if mibBuilder.loadTexts: raisecomNMSAccessControl.setLastUpdated('200402060000Z')
if mibBuilder.loadTexts: raisecomNMSAccessControl.setOrganization('raisecom, Ltd.')
raisecomNMSACPAddressTable = MibTable((1, 3, 6, 1, 4, 1, 8886, 1, 5, 1), )
if mibBuilder.loadTexts: raisecomNMSACPAddressTable.setStatus('current')
raisecomNMSACPAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8886, 1, 5, 1, 1), ).setIndexNames((0, "RAISECOM-NMS-ACC-MIB", "raisecomNMSACPAddrIndex"))
if mibBuilder.loadTexts: raisecomNMSACPAddressEntry.setStatus('current')
raisecomNMSACPAddrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99))).setMaxAccess("readonly")
if mibBuilder.loadTexts: raisecomNMSACPAddrIndex.setStatus('current')
raisecomNMSACPAddrIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 1, 5, 1, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: raisecomNMSACPAddrIPAddress.setStatus('current')
raisecomNMSACPAddrNetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 1, 5, 1, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: raisecomNMSACPAddrNetMask.setStatus('current')
raisecomNMSACPAddrRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8886, 1, 5, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: raisecomNMSACPAddrRowStatus.setStatus('current')
raisecomTelnetAccessControlStatus = MibScalar((1, 3, 6, 1, 4, 1, 8886, 1, 5, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: raisecomTelnetAccessControlStatus.setStatus('current')
raisecomWebAccessControlStatus = MibScalar((1, 3, 6, 1, 4, 1, 8886, 1, 5, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 0))).clone(namedValues=NamedValues(("enable", 1), ("disable", 0)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: raisecomWebAccessControlStatus.setStatus('current')
mibBuilder.exportSymbols("RAISECOM-NMS-ACC-MIB", raisecomNMSACPAddressEntry=raisecomNMSACPAddressEntry, raisecomNMSACPAddrIndex=raisecomNMSACPAddrIndex, raisecomNMSAccessControl=raisecomNMSAccessControl, raisecomNMSACPAddrIPAddress=raisecomNMSACPAddrIPAddress, raisecomTelnetAccessControlStatus=raisecomTelnetAccessControlStatus, raisecomWebAccessControlStatus=raisecomWebAccessControlStatus, raisecomNMSACPAddrRowStatus=raisecomNMSACPAddrRowStatus, PYSNMP_MODULE_ID=raisecomNMSAccessControl, raisecomNMSACPAddrNetMask=raisecomNMSACPAddrNetMask, raisecomNMSACPAddressTable=raisecomNMSACPAddressTable)
