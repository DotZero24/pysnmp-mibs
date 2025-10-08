#
# PySNMP MIB module LEFTHAND-NETWORKS-GLOBAL-REG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/hp/LEFTHAND-NETWORKS-GLOBAL-REG-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:10:04 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
lhnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9804, 1))
lhnMIB.setRevisions(('2013-11-21 00:00', '2013-06-25 00:00', '2012-09-04 00:00', '2011-06-21 00:00', '2010-09-07 00:00', '2010-07-19 00:00', '2009-11-20 00:00', '2009-03-10 00:00', '2008-01-24 00:00',))
if mibBuilder.loadTexts: lhnMIB.setLastUpdated('201311210000Z')
if mibBuilder.loadTexts: lhnMIB.setOrganization('Hewlett Packard Company, StorageWorks Division')
lefthandnetworks = MibIdentifier((1, 3, 6, 1, 4, 1, 9804))
lhnMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 1, 0))
lhnMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 1, 1))
lhnMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 1, 2))
lhnMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 1, 2, 1))
lhnMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 1, 2, 2))
lefthandnetworksRegistrations = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 2))
lhnModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 9804, 2, 1))
if mibBuilder.loadTexts: lhnModules.setStatus('current')
lefthandnetworksProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 9804, 3))
lhnNsm = ObjectIdentity((1, 3, 6, 1, 4, 1, 9804, 3, 1))
if mibBuilder.loadTexts: lhnNsm.setStatus('current')
mibBuilder.exportSymbols("LEFTHAND-NETWORKS-GLOBAL-REG-MIB", lhnMIBCompliances=lhnMIBCompliances, lhnNsm=lhnNsm, lhnModules=lhnModules, lhnMIBGroups=lhnMIBGroups, lefthandnetworksRegistrations=lefthandnetworksRegistrations, lefthandnetworksProducts=lefthandnetworksProducts, PYSNMP_MODULE_ID=lhnMIB, lefthandnetworks=lefthandnetworks, lhnMIBNotifications=lhnMIBNotifications, lhnMIB=lhnMIB, lhnMIBObjects=lhnMIBObjects, lhnMIBConformance=lhnMIBConformance)
