#
# PySNMP MIB module CLOUDGENIX-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cloudgenix/CLOUDGENIX-SMI
# Produced by pysmi-1.1.12 at Thu Sep 11 09:57:16 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cloudgenix = ModuleIdentity((1, 3, 6, 1, 4, 1, 50114))
cloudgenix.setRevisions(('2017-06-19 18:00',))
if mibBuilder.loadTexts: cloudgenix.setLastUpdated('201706191800Z')
if mibBuilder.loadTexts: cloudgenix.setOrganization('CloudGenix, Inc.')
cgxObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 50114, 1))
cgxConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 50114, 2))
cgxCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 50114, 2, 1))
cloudgenixCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 50114, 2, 1, 1)).setObjects()

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cloudgenixCompliance = cloudgenixCompliance.setStatus('current')
cgxGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 50114, 2, 2))
cgxMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 50114, 10))
mibBuilder.exportSymbols("CLOUDGENIX-SMI", cgxGroups=cgxGroups, cloudgenix=cloudgenix, PYSNMP_MODULE_ID=cloudgenix, cgxObjects=cgxObjects, cgxConformance=cgxConformance, cgxCompliances=cgxCompliances, cloudgenixCompliance=cloudgenixCompliance, cgxMgmt=cgxMgmt)
