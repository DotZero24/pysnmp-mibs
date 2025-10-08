#
# PySNMP MIB module JUNIPER-CHASSIS-FWDD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/juniper/JUNIPER-CHASSIS-FWDD-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:55:31 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
jnxFwdd = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 34))
if mibBuilder.loadTexts: jnxFwdd.setLastUpdated('200602162158Z')
if mibBuilder.loadTexts: jnxFwdd.setOrganization('Juniper Networks, Inc.')
jnxFwddProcess = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 34, 1))
jnxFwddMicroKernelCPUUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 34, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFwddMicroKernelCPUUsage.setStatus('current')
jnxFwddRtThreadsCPUUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 34, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFwddRtThreadsCPUUsage.setStatus('current')
jnxFwddHeapUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 34, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFwddHeapUsage.setStatus('current')
jnxFwddDmaMemUsage = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 34, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFwddDmaMemUsage.setStatus('current')
jnxFwddUpTime = MibScalar((1, 3, 6, 1, 4, 1, 2636, 3, 34, 1, 5), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxFwddUpTime.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-CHASSIS-FWDD-MIB", PYSNMP_MODULE_ID=jnxFwdd, jnxFwddDmaMemUsage=jnxFwddDmaMemUsage, jnxFwdd=jnxFwdd, jnxFwddUpTime=jnxFwddUpTime, jnxFwddProcess=jnxFwddProcess, jnxFwddHeapUsage=jnxFwddHeapUsage, jnxFwddMicroKernelCPUUsage=jnxFwddMicroKernelCPUUsage, jnxFwddRtThreadsCPUUsage=jnxFwddRtThreadsCPUUsage)
