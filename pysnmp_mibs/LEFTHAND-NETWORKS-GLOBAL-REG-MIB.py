#
# PySNMP MIB module LEFTHAND-NETWORKS-GLOBAL-REG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/LEFTHAND-NETWORKS-GLOBAL-REG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("LEFTHAND-NETWORKS-GLOBAL-REG-MIB", lhnMIBObjects=lhnMIBObjects, lhnMIB=lhnMIB, lefthandnetworksRegistrations=lefthandnetworksRegistrations, PYSNMP_MODULE_ID=lhnMIB, lhnModules=lhnModules, lhnMIBConformance=lhnMIBConformance, lhnMIBGroups=lhnMIBGroups, lefthandnetworks=lefthandnetworks, lhnMIBNotifications=lhnMIBNotifications, lhnMIBCompliances=lhnMIBCompliances, lefthandnetworksProducts=lefthandnetworksProducts, lhnNsm=lhnNsm)
