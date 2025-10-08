#
# PySNMP MIB module SYNERGY100G-HPE-CPU-UTIL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/SYNERGY100G-HPE-CPU-UTIL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:09:27 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
hpVCSE_100Gb_F32_Module, = mibBuilder.importSymbols("HPSVRMGMT-OID", "hpVCSE-100Gb-F32-Module")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("SYNERGY100G-HPE-CPU-UTIL-MIB", syn100GhpeSynergyCpuUtilMIBObjects=syn100GhpeSynergyCpuUtilMIBObjects, syn100GhpeCpuUtilConfig=syn100GhpeCpuUtilConfig, syn100GhpeSwitchMaxCPUThreshold=syn100GhpeSwitchMaxCPUThreshold, syn100GhpeCpuUtilTraps=syn100GhpeCpuUtilTraps, syn100GhpeSwitchAverageCPUUtilization=syn100GhpeSwitchAverageCPUUtilization, PYSNMP_MODULE_ID=syn100GhpeCpuUtilMIB, syn100GhpeSwitchMinCPUThreshold=syn100GhpeSwitchMinCPUThreshold, syn100GhpeTrapMaxCPUThreshold=syn100GhpeTrapMaxCPUThreshold, syn100GhpeTrapMinCPUThreshold=syn100GhpeTrapMinCPUThreshold, syn100GhpeCpuUtilMIB=syn100GhpeCpuUtilMIB, syn100GhpeCpuUtiStatus=syn100GhpeCpuUtiStatus)
