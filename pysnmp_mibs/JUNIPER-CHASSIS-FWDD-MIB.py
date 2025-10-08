#
# PySNMP MIB module JUNIPER-CHASSIS-FWDD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/juniper/JUNIPER-CHASSIS-FWDD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:31:31 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("JUNIPER-CHASSIS-FWDD-MIB", jnxFwddHeapUsage=jnxFwddHeapUsage, jnxFwdd=jnxFwdd, jnxFwddDmaMemUsage=jnxFwddDmaMemUsage, PYSNMP_MODULE_ID=jnxFwdd, jnxFwddUpTime=jnxFwddUpTime, jnxFwddMicroKernelCPUUsage=jnxFwddMicroKernelCPUUsage, jnxFwddRtThreadsCPUUsage=jnxFwddRtThreadsCPUUsage, jnxFwddProcess=jnxFwddProcess)
