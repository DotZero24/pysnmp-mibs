#
# PySNMP MIB module EXTREME-VC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/extreme/EXTREME-VC-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:02 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
extremeVC = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 5))
if mibBuilder.loadTexts: extremeVC.setLastUpdated('9801090000Z')
if mibBuilder.loadTexts: extremeVC.setOrganization('Extreme Networks, Inc.')
extremeVCLinkTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 5, 1), )
if mibBuilder.loadTexts: extremeVCLinkTable.setStatus('deprecated')
extremeVCLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 5, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: extremeVCLinkEntry.setStatus('deprecated')
extremeVCLinkValid = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 5, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeVCLinkValid.setStatus('deprecated')
extremeVCLinkDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 5, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeVCLinkDeviceId.setStatus('deprecated')
extremeVCLinkPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 5, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeVCLinkPortIndex.setStatus('deprecated')
mibBuilder.exportSymbols("EXTREME-VC-MIB", extremeVCLinkEntry=extremeVCLinkEntry, extremeVCLinkDeviceId=extremeVCLinkDeviceId, PYSNMP_MODULE_ID=extremeVC, extremeVCLinkValid=extremeVCLinkValid, extremeVCLinkTable=extremeVCLinkTable, extremeVC=extremeVC, extremeVCLinkPortIndex=extremeVCLinkPortIndex)
