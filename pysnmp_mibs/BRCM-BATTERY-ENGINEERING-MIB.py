#
# PySNMP MIB module BRCM-BATTERY-ENGINEERING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/broadcom/BRCM-BATTERY-ENGINEERING-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:08:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cableDataEngineering, = mibBuilder.importSymbols("BRCM-CABLEDATA-ENGINEERING-MIB", "cableDataEngineering")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
PositiveInteger, = mibBuilder.importSymbols("UPS-MIB", "PositiveInteger")
batteryEngineering = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 10))
batteryEngineering.setRevisions(('2009-06-10 00:00',))
if mibBuilder.loadTexts: batteryEngineering.setLastUpdated('200906100000Z')
if mibBuilder.loadTexts: batteryEngineering.setOrganization('Broadcom Corporation')
batteryEngrBase = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 10, 1))
battSimulatePowerSource = MibScalar((1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 3, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("utility", 1), ("battery", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: battSimulatePowerSource.setStatus('current')
mibBuilder.exportSymbols("BRCM-BATTERY-ENGINEERING-MIB", batteryEngrBase=batteryEngrBase, batteryEngineering=batteryEngineering, battSimulatePowerSource=battSimulatePowerSource, PYSNMP_MODULE_ID=batteryEngineering)
