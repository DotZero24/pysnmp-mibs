#
# PySNMP MIB module OBSERVIUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/OBSERVIUM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:55:45 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, mib_2, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "mib-2", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
RowStatus, TextualConvention, TestAndIncr, PhysAddress, TruthValue, AutonomousType, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TestAndIncr", "PhysAddress", "TruthValue", "AutonomousType", "TimeStamp", "DisplayString")
observium = MibIdentifier((1, 3, 6, 1, 4, 1, 36602))
obsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 36602, 1))
obsHostInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 36602, 1, 1))
obsLinuxDistro = MibScalar((1, 3, 6, 1, 4, 1, 36602, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: obsLinuxDistro.setStatus('current')
obsCPUUsage = MibScalar((1, 3, 6, 1, 4, 1, 36602, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: obsCPUUsage.setStatus('mandatory')
mibBuilder.exportSymbols("OBSERVIUM-MIB", observium=observium, obsLinuxDistro=obsLinuxDistro, obsCPUUsage=obsCPUUsage, obsObjects=obsObjects, obsHostInfo=obsHostInfo)
