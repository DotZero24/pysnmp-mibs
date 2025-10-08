#
# PySNMP MIB module OCNOS-IPI-MODULE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ipinfusion/OCNOS-IPI-MODULE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:53:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
RowStatus, DateAndTime, TextualConvention, PhysAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DateAndTime", "TextualConvention", "PhysAddress", "DisplayString")
ipi = ModuleIdentity((1, 3, 6, 1, 4, 1, 36673))
if mibBuilder.loadTexts: ipi.setLastUpdated('201603301200Z')
if mibBuilder.loadTexts: ipi.setOrganization('IPI.')
mibBuilder.exportSymbols("OCNOS-IPI-MODULE-MIB", ipi=ipi, PYSNMP_MODULE_ID=ipi)
