#
# PySNMP MIB module HIRSCHMANN-WAN-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hirschmann/HIRSCHMANN-WAN-INFO-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:56:20 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hmWanMgmt, = mibBuilder.importSymbols("HIRSCHMANN-WAN-MIB", "hmWanMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("HIRSCHMANN-WAN-INFO-MIB", hmWanInfoSN=hmWanInfoSN, hmWanInfoFirmware=hmWanInfoFirmware, hmWanInfoIMEI=hmWanInfoIMEI, hmWanInfoESN=hmWanInfoESN, hmWanInfoICCID=hmWanInfoICCID, hmWanInfoProduct=hmWanInfoProduct, hmWanInfoMEID=hmWanInfoMEID, hmWanInfoMib=hmWanInfoMib, PYSNMP_MODULE_ID=hmWanInfoMib)
