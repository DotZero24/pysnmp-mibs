#
# PySNMP MIB module SWBASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/brocade/SWBASE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:15:29 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
fcSwitch, bcsiModules = mibBuilder.importSymbols("Brocade-REG-MIB", "fcSwitch", "bcsiModules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
swMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 1588, 3, 1, 3))
swMibModule.setRevisions(('1911-04-15 18:30',))
if mibBuilder.loadTexts: swMibModule.setLastUpdated('1104151830Z')
if mibBuilder.loadTexts: swMibModule.setOrganization('Brocade Communications Systems, Inc.,')
sw = ObjectIdentity((1, 3, 6, 1, 4, 1, 1588, 2, 1, 1, 1))
if mibBuilder.loadTexts: sw.setStatus('current')
mibBuilder.exportSymbols("SWBASE-MIB", swMibModule=swMibModule, sw=sw, PYSNMP_MODULE_ID=swMibModule)
