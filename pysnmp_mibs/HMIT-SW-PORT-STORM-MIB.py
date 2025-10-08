#
# PySNMP MIB module HMIT-SW-PORT-STORM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hirschmann/HMIT-SW-PORT-STORM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:55:47 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hmITSwitchTech, = mibBuilder.importSymbols("HMIT-SMI", "hmITSwitchTech")
hmITSwPortMIB, = mibBuilder.importSymbols("HMIT-SW-PORT-MGR-MIB", "hmITSwPortMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hmITPortStorm = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 7))
hmITPortStorm.setRevisions(('2010-01-08 17:00',))
if mibBuilder.loadTexts: hmITPortStorm.setLastUpdated('201001081700Z')
if mibBuilder.loadTexts: hmITPortStorm.setOrganization('Belden Singapore Pte Ltd.')
portStorm = NotificationType((1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 7, 1))
if mibBuilder.loadTexts: portStorm.setStatus('current')
portStormShutdown = NotificationType((1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 7, 2))
if mibBuilder.loadTexts: portStormShutdown.setStatus('current')
mibBuilder.exportSymbols("HMIT-SW-PORT-STORM-MIB", portStorm=portStorm, portStormShutdown=portStormShutdown, PYSNMP_MODULE_ID=hmITPortStorm, hmITPortStorm=hmITPortStorm)
