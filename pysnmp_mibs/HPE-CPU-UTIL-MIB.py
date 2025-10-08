#
# PySNMP MIB module HPE-CPU-UTIL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/HPE-CPU-UTIL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:00 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpVCSE_40Gb_F8_Module, = mibBuilder.importSymbols("HPSVRMGMT-OID", "hpVCSE-40Gb-F8-Module")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpeCpuUtilMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4130))
hpeCpuUtilMIB.setRevisions(('2019-12-19 00:00',))
if mibBuilder.loadTexts: hpeCpuUtilMIB.setLastUpdated('201912190000Z')
if mibBuilder.loadTexts: hpeCpuUtilMIB.setOrganization('Hewlett Packard Enterprise')
hpeSynergyCpuUtilMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1))
hpeCpuUtilConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4130, 1))
hpeCpuUtiStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4130, 2))
hpeCpuUtilTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4130, 3))
hpeSwitchMaxCPUThreshold = MibScalar((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4130, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(95)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpeSwitchMaxCPUThreshold.setStatus('current')
hpeSwitchMinCPUThreshold = MibScalar((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4130, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(75)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpeSwitchMinCPUThreshold.setStatus('current')
hpeSwitchAverageCPUUtilization = MibScalar((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4130, 2, 1), Integer32()).setUnits('percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpeSwitchAverageCPUUtilization.setStatus('current')
hpeTrapMaxCPUThreshold = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4130, 3, 1)).setObjects(("HPE-CPU-UTIL-MIB", "hpeSwitchMaxCPUThreshold"), ("HPE-CPU-UTIL-MIB", "hpeSwitchAverageCPUUtilization"))
if mibBuilder.loadTexts: hpeTrapMaxCPUThreshold.setStatus('current')
hpeTrapMinCPUThreshold = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 8, 1, 4130, 3, 2)).setObjects(("HPE-CPU-UTIL-MIB", "hpeSwitchMinCPUThreshold"), ("HPE-CPU-UTIL-MIB", "hpeSwitchAverageCPUUtilization"))
if mibBuilder.loadTexts: hpeTrapMinCPUThreshold.setStatus('current')
mibBuilder.exportSymbols("HPE-CPU-UTIL-MIB", hpeCpuUtiStatus=hpeCpuUtiStatus, hpeCpuUtilMIB=hpeCpuUtilMIB, hpeSwitchAverageCPUUtilization=hpeSwitchAverageCPUUtilization, hpeCpuUtilConfig=hpeCpuUtilConfig, hpeSwitchMaxCPUThreshold=hpeSwitchMaxCPUThreshold, hpeSynergyCpuUtilMIBObjects=hpeSynergyCpuUtilMIBObjects, hpeSwitchMinCPUThreshold=hpeSwitchMinCPUThreshold, hpeTrapMaxCPUThreshold=hpeTrapMaxCPUThreshold, hpeTrapMinCPUThreshold=hpeTrapMinCPUThreshold, hpeCpuUtilTraps=hpeCpuUtilTraps, PYSNMP_MODULE_ID=hpeCpuUtilMIB)
