#
# PySNMP MIB module CASA-ID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/casa/CASA-ID-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:43 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
casa, = mibBuilder.importSymbols("CASA-MIB", "casa")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
casaIdMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 20858, 2))
casaIdMib.setRevisions(('1900-04-07 00:00',))
if mibBuilder.loadTexts: casaIdMib.setLastUpdated('200608150000Z')
if mibBuilder.loadTexts: casaIdMib.setOrganization('CASA SYSTEMS INC')
casa2100System = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 2, 1))
casa2200System = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 2, 20))
casa2300System = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 2, 30))
casa2800System = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 2, 40))
casa3000System = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 2, 50))
casa6000System = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 2, 100))
casa10000System = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 2, 200))
mibBuilder.exportSymbols("CASA-ID-MIB", casa2100System=casa2100System, casa6000System=casa6000System, PYSNMP_MODULE_ID=casaIdMib, casaIdMib=casaIdMib, casa2300System=casa2300System, casa2800System=casa2800System, casa3000System=casa3000System, casa10000System=casa10000System, casa2200System=casa2200System)
