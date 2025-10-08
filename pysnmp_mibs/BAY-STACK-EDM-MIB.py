#
# PySNMP MIB module BAY-STACK-EDM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/nortel/BAY-STACK-EDM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:02:20 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bayStackMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "bayStackMibs")
bayStackEdmMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 5, 36))
bayStackEdmMib.setRevisions(('2013-10-11 00:00', '2013-02-13 00:00', '2009-08-20 00:00',))
if mibBuilder.loadTexts: bayStackEdmMib.setLastUpdated('201310110000Z')
if mibBuilder.loadTexts: bayStackEdmMib.setOrganization('Avaya Networks')
bayStackEdmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 36, 0))
bayStackEdmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 36, 1))
bsEdmScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 5, 36, 1, 1))
bsEdmHelpFilePath = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 36, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 327))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsEdmHelpFilePath.setStatus('current')
bsEdmInactivityTimeout = MibScalar((1, 3, 6, 1, 4, 1, 45, 5, 36, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 65535)).clone(900)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: bsEdmInactivityTimeout.setStatus('current')
mibBuilder.exportSymbols("BAY-STACK-EDM-MIB", PYSNMP_MODULE_ID=bayStackEdmMib, bsEdmScalars=bsEdmScalars, bsEdmHelpFilePath=bsEdmHelpFilePath, bsEdmInactivityTimeout=bsEdmInactivityTimeout, bayStackEdmNotifications=bayStackEdmNotifications, bayStackEdmObjects=bayStackEdmObjects, bayStackEdmMib=bayStackEdmMib)
