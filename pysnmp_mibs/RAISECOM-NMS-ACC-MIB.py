#
# PySNMP MIB module RAISECOM-NMS-ACC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/raisecom/RAISECOM-NMS-ACC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:30:58 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
raisecomAgent, = mibBuilder.importSymbols("RAISECOM-BASE-MIB", "raisecomAgent")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
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
mibBuilder.exportSymbols("RAISECOM-NMS-ACC-MIB", raisecomNMSACPAddressEntry=raisecomNMSACPAddressEntry, raisecomTelnetAccessControlStatus=raisecomTelnetAccessControlStatus, raisecomNMSAccessControl=raisecomNMSAccessControl, raisecomNMSACPAddrIndex=raisecomNMSACPAddrIndex, raisecomWebAccessControlStatus=raisecomWebAccessControlStatus, PYSNMP_MODULE_ID=raisecomNMSAccessControl, raisecomNMSACPAddressTable=raisecomNMSACPAddressTable, raisecomNMSACPAddrRowStatus=raisecomNMSACPAddrRowStatus, raisecomNMSACPAddrNetMask=raisecomNMSACPAddrNetMask, raisecomNMSACPAddrIPAddress=raisecomNMSACPAddrIPAddress)
