#
# PySNMP MIB module EXTREME-VC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/extreme/EXTREME-VC-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:55 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
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
mibBuilder.exportSymbols("EXTREME-VC-MIB", extremeVCLinkPortIndex=extremeVCLinkPortIndex, extremeVCLinkValid=extremeVCLinkValid, extremeVCLinkTable=extremeVCLinkTable, extremeVC=extremeVC, extremeVCLinkDeviceId=extremeVCLinkDeviceId, PYSNMP_MODULE_ID=extremeVC, extremeVCLinkEntry=extremeVCLinkEntry)
