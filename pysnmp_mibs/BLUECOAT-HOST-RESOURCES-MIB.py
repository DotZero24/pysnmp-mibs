#
# PySNMP MIB module BLUECOAT-HOST-RESOURCES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/bluecoat/BLUECOAT-HOST-RESOURCES-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:10:57 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
blueCoatHostResourcesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 9))
blueCoatHostResourcesMIB.setRevisions(('2007-04-24 00:00',))
if mibBuilder.loadTexts: blueCoatHostResourcesMIB.setLastUpdated('200704240000Z')
if mibBuilder.loadTexts: blueCoatHostResourcesMIB.setOrganization('Blue Coat')
bchrDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 9, 1))
bchrSerial = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 9, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bchrSerial.setStatus('deprecated')
mibBuilder.exportSymbols("BLUECOAT-HOST-RESOURCES-MIB", PYSNMP_MODULE_ID=blueCoatHostResourcesMIB, bchrSerial=bchrSerial, blueCoatHostResourcesMIB=blueCoatHostResourcesMIB, bchrDevice=bchrDevice)
