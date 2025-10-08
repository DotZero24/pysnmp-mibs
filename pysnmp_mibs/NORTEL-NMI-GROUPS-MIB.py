#
# PySNMP MIB module NORTEL-NMI-GROUPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/nortel/NORTEL-NMI-GROUPS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:59:20 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
nortelNMIconformanceMIBs, = mibBuilder.importSymbols("NORTEL-NMI-CONFORMANCE-MIB", "nortelNMIconformanceMIBs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nortelNMImibGroups = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 29, 1, 2, 1))
nortelNMImibGroups.setRevisions(('1999-06-24 00:00',))
if mibBuilder.loadTexts: nortelNMImibGroups.setLastUpdated('9906240000Z')
if mibBuilder.loadTexts: nortelNMImibGroups.setOrganization('Nortel Networks')
nortelNMIobjectGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 29, 1, 2, 1, 1))
if mibBuilder.loadTexts: nortelNMIobjectGroups.setStatus('current')
nortelNMInotificationGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 562, 29, 1, 2, 1, 2))
if mibBuilder.loadTexts: nortelNMInotificationGroups.setStatus('current')
mibBuilder.exportSymbols("NORTEL-NMI-GROUPS-MIB", nortelNMIobjectGroups=nortelNMIobjectGroups, nortelNMInotificationGroups=nortelNMInotificationGroups, nortelNMImibGroups=nortelNMImibGroups, PYSNMP_MODULE_ID=nortelNMImibGroups)
