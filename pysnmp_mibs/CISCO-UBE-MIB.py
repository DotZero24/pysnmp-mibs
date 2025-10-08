#
# PySNMP MIB module CISCO-UBE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cisco/CISCO-UBE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:14:03 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoUbeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 764))
ciscoUbeMIB.setRevisions(('2010-11-29 00:00',))
if mibBuilder.loadTexts: ciscoUbeMIB.setLastUpdated('201011290000Z')
if mibBuilder.loadTexts: ciscoUbeMIB.setOrganization('Cisco Systems, Inc.')
ciscoUbeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 764, 0))
ciscoUbeMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 764, 1))
cubeEnabled = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 764, 0, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cubeEnabled.setStatus('current')
cubeVersion = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 764, 0, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cubeVersion.setStatus('current')
cubeTotalSessionAllowed = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 764, 0, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 999999))).setUnits('session').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cubeTotalSessionAllowed.setStatus('current')
ciscoUbeMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 764, 1, 1))
ciscoUbeMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 764, 1, 2))
ciscoCubeMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 764, 1, 1, 1)).setObjects(("CISCO-UBE-MIB", "ciscoUbeMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCubeMIBCompliance = ciscoCubeMIBCompliance.setStatus('current')
ciscoUbeMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 764, 1, 2, 1)).setObjects(("CISCO-UBE-MIB", "cubeEnabled"), ("CISCO-UBE-MIB", "cubeVersion"), ("CISCO-UBE-MIB", "cubeTotalSessionAllowed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoUbeMIBGroup = ciscoUbeMIBGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-UBE-MIB", ciscoUbeMIBConform=ciscoUbeMIBConform, ciscoUbeMIBCompliances=ciscoUbeMIBCompliances, ciscoUbeMIBObjects=ciscoUbeMIBObjects, ciscoUbeMIB=ciscoUbeMIB, ciscoCubeMIBCompliance=ciscoCubeMIBCompliance, cubeVersion=cubeVersion, cubeTotalSessionAllowed=cubeTotalSessionAllowed, ciscoUbeMIBGroup=ciscoUbeMIBGroup, PYSNMP_MODULE_ID=ciscoUbeMIB, ciscoUbeMIBGroups=ciscoUbeMIBGroups, cubeEnabled=cubeEnabled)
