#
# PySNMP MIB module CASA-ID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/casa/CASA-ID-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:14:57 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
casa, = mibBuilder.importSymbols("CASA-MIB", "casa")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CASA-ID-MIB", casa2800System=casa2800System, casa2100System=casa2100System, PYSNMP_MODULE_ID=casaIdMib, casa10000System=casa10000System, casa2200System=casa2200System, casaIdMib=casaIdMib, casa6000System=casa6000System, casa3000System=casa3000System, casa2300System=casa2300System)
