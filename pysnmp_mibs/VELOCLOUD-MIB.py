#
# PySNMP MIB module VELOCLOUD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/velocloud/VELOCLOUD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:48 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
velocloud = ModuleIdentity((1, 3, 6, 1, 4, 1, 45346))
velocloud.setRevisions(('2021-05-11 00:00', '2019-08-02 00:00', '2017-01-18 00:00', '2017-01-13 00:00',))
if mibBuilder.loadTexts: velocloud.setLastUpdated('202105110000Z')
if mibBuilder.loadTexts: velocloud.setOrganization('VMware Corporation')
modules = MibIdentifier((1, 3, 6, 1, 4, 1, 45346, 1))
mibBuilder.exportSymbols("VELOCLOUD-MIB", velocloud=velocloud, modules=modules, PYSNMP_MODULE_ID=velocloud)
