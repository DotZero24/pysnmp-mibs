#
# PySNMP MIB module SYNERGY100G-HPE-CPU-UTIL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/SYNERGY100G-HPE-CPU-UTIL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:12 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpVCSE_100Gb_F32_Module, = mibBuilder.importSymbols("HPSVRMGMT-OID", "hpVCSE-100Gb-F32-Module")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
syn100GhpeCpuUtilMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4130))
syn100GhpeCpuUtilMIB.setRevisions(('2019-12-19 00:00',))
if mibBuilder.loadTexts: syn100GhpeCpuUtilMIB.setLastUpdated('201912190000Z')
if mibBuilder.loadTexts: syn100GhpeCpuUtilMIB.setOrganization('Hewlett Packard Enterprise')
syn100GhpeSynergyCpuUtilMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1))
syn100GhpeCpuUtilConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4130, 1))
syn100GhpeCpuUtiStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4130, 2))
syn100GhpeCpuUtilTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4130, 3))
syn100GhpeSwitchMaxCPUThreshold = MibScalar((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4130, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(95)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syn100GhpeSwitchMaxCPUThreshold.setStatus('current')
syn100GhpeSwitchMinCPUThreshold = MibScalar((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4130, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(75)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: syn100GhpeSwitchMinCPUThreshold.setStatus('current')
syn100GhpeSwitchAverageCPUUtilization = MibScalar((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4130, 2, 1), Integer32()).setUnits('percentage').setMaxAccess("readonly")
if mibBuilder.loadTexts: syn100GhpeSwitchAverageCPUUtilization.setStatus('current')
syn100GhpeTrapMaxCPUThreshold = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4130, 3, 1)).setObjects(("SYNERGY100G-HPE-CPU-UTIL-MIB", "syn100GhpeSwitchMaxCPUThreshold"), ("SYNERGY100G-HPE-CPU-UTIL-MIB", "syn100GhpeSwitchAverageCPUUtilization"))
if mibBuilder.loadTexts: syn100GhpeTrapMaxCPUThreshold.setStatus('current')
syn100GhpeTrapMinCPUThreshold = NotificationType((1, 3, 6, 1, 4, 1, 11, 5, 7, 5, 9, 1, 4130, 3, 2)).setObjects(("SYNERGY100G-HPE-CPU-UTIL-MIB", "syn100GhpeSwitchMinCPUThreshold"), ("SYNERGY100G-HPE-CPU-UTIL-MIB", "syn100GhpeSwitchAverageCPUUtilization"))
if mibBuilder.loadTexts: syn100GhpeTrapMinCPUThreshold.setStatus('current')
mibBuilder.exportSymbols("SYNERGY100G-HPE-CPU-UTIL-MIB", syn100GhpeSwitchMinCPUThreshold=syn100GhpeSwitchMinCPUThreshold, syn100GhpeTrapMaxCPUThreshold=syn100GhpeTrapMaxCPUThreshold, syn100GhpeSynergyCpuUtilMIBObjects=syn100GhpeSynergyCpuUtilMIBObjects, syn100GhpeCpuUtilConfig=syn100GhpeCpuUtilConfig, syn100GhpeCpuUtilTraps=syn100GhpeCpuUtilTraps, syn100GhpeSwitchMaxCPUThreshold=syn100GhpeSwitchMaxCPUThreshold, syn100GhpeTrapMinCPUThreshold=syn100GhpeTrapMinCPUThreshold, syn100GhpeCpuUtilMIB=syn100GhpeCpuUtilMIB, syn100GhpeSwitchAverageCPUUtilization=syn100GhpeSwitchAverageCPUUtilization, syn100GhpeCpuUtiStatus=syn100GhpeCpuUtiStatus, PYSNMP_MODULE_ID=syn100GhpeCpuUtilMIB)
