#
# PySNMP MIB module HPE-CPU-UTIL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/HPE-CPU-UTIL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:08 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpVCSE_40Gb_F8_Module, = mibBuilder.importSymbols("HPSVRMGMT-OID", "hpVCSE-40Gb-F8-Module")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("HPE-CPU-UTIL-MIB", hpeCpuUtiStatus=hpeCpuUtiStatus, hpeSwitchAverageCPUUtilization=hpeSwitchAverageCPUUtilization, hpeTrapMaxCPUThreshold=hpeTrapMaxCPUThreshold, hpeTrapMinCPUThreshold=hpeTrapMinCPUThreshold, hpeCpuUtilTraps=hpeCpuUtilTraps, hpeSynergyCpuUtilMIBObjects=hpeSynergyCpuUtilMIBObjects, hpeCpuUtilMIB=hpeCpuUtilMIB, hpeCpuUtilConfig=hpeCpuUtilConfig, PYSNMP_MODULE_ID=hpeCpuUtilMIB, hpeSwitchMaxCPUThreshold=hpeSwitchMaxCPUThreshold, hpeSwitchMinCPUThreshold=hpeSwitchMinCPUThreshold)
