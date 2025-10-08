#
# PySNMP MIB module HMIT-SW-PORT-STORM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hirschmann/HMIT-SW-PORT-STORM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:55:57 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hmITSwitchTech, = mibBuilder.importSymbols("HMIT-SMI", "hmITSwitchTech")
hmITSwPortMIB, = mibBuilder.importSymbols("HMIT-SW-PORT-MGR-MIB", "hmITSwPortMIB")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hmITPortStorm = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 7))
hmITPortStorm.setRevisions(('2010-01-08 17:00',))
if mibBuilder.loadTexts: hmITPortStorm.setLastUpdated('201001081700Z')
if mibBuilder.loadTexts: hmITPortStorm.setOrganization('Belden Singapore Pte Ltd.')
portStorm = NotificationType((1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 7, 1))
if mibBuilder.loadTexts: portStorm.setStatus('current')
portStormShutdown = NotificationType((1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 7, 2))
if mibBuilder.loadTexts: portStormShutdown.setStatus('current')
mibBuilder.exportSymbols("HMIT-SW-PORT-STORM-MIB", portStorm=portStorm, PYSNMP_MODULE_ID=hmITPortStorm, hmITPortStorm=hmITPortStorm, portStormShutdown=portStormShutdown)
