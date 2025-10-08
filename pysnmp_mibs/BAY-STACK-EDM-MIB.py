#
# PySNMP MIB module BAY-STACK-EDM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nortel/BAY-STACK-EDM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:59:03 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("BAY-STACK-EDM-MIB", bayStackEdmMib=bayStackEdmMib, bsEdmInactivityTimeout=bsEdmInactivityTimeout, bsEdmHelpFilePath=bsEdmHelpFilePath, bayStackEdmObjects=bayStackEdmObjects, bsEdmScalars=bsEdmScalars, bayStackEdmNotifications=bayStackEdmNotifications, PYSNMP_MODULE_ID=bayStackEdmMib)
