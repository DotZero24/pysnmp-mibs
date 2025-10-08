#
# PySNMP MIB module HIRSCHMANN-WAN-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hirschmann/HIRSCHMANN-WAN-INFO-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:16 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hmWanMgmt, = mibBuilder.importSymbols("HIRSCHMANN-WAN-MIB", "hmWanMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hmWanInfoMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 40, 1, 6))
hmWanInfoMib.setRevisions(('2016-08-09 00:00',))
if mibBuilder.loadTexts: hmWanInfoMib.setLastUpdated('201608090000Z')
if mibBuilder.loadTexts: hmWanInfoMib.setOrganization('Hirschmann Automation and Control GmbH')
hmWanInfoProduct = MibScalar((1, 3, 6, 1, 4, 1, 248, 40, 1, 6, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmWanInfoProduct.setStatus('current')
hmWanInfoFirmware = MibScalar((1, 3, 6, 1, 4, 1, 248, 40, 1, 6, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmWanInfoFirmware.setStatus('current')
hmWanInfoSN = MibScalar((1, 3, 6, 1, 4, 1, 248, 40, 1, 6, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmWanInfoSN.setStatus('current')
hmWanInfoIMEI = MibScalar((1, 3, 6, 1, 4, 1, 248, 40, 1, 6, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmWanInfoIMEI.setStatus('current')
hmWanInfoESN = MibScalar((1, 3, 6, 1, 4, 1, 248, 40, 1, 6, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmWanInfoESN.setStatus('current')
hmWanInfoMEID = MibScalar((1, 3, 6, 1, 4, 1, 248, 40, 1, 6, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmWanInfoMEID.setStatus('current')
hmWanInfoICCID = MibScalar((1, 3, 6, 1, 4, 1, 248, 40, 1, 6, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hmWanInfoICCID.setStatus('current')
mibBuilder.exportSymbols("HIRSCHMANN-WAN-INFO-MIB", hmWanInfoMib=hmWanInfoMib, hmWanInfoSN=hmWanInfoSN, PYSNMP_MODULE_ID=hmWanInfoMib, hmWanInfoIMEI=hmWanInfoIMEI, hmWanInfoMEID=hmWanInfoMEID, hmWanInfoICCID=hmWanInfoICCID, hmWanInfoESN=hmWanInfoESN, hmWanInfoProduct=hmWanInfoProduct, hmWanInfoFirmware=hmWanInfoFirmware)
