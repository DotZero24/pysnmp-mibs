#
# PySNMP MIB module ENTERASYS-CONFIGURATION-CHANGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/enterasys/ENTERASYS-CONFIGURATION-CHANGE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:29 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention")
etsysConfigurationChangeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 12))
etsysConfigurationChangeMIB.setRevisions(('2001-11-26 16:44', '2001-08-08 00:00',))
if mibBuilder.loadTexts: etsysConfigurationChangeMIB.setLastUpdated('200111261644Z')
if mibBuilder.loadTexts: etsysConfigurationChangeMIB.setOrganization('Enterasys Networks')
etsysConfigChangeNonVolatile = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 1))
etsysConfigChangeVolatile = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 2))
etsysConfigChangeFirmware = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 3))
etsysConfigChangeNonVolatileCount = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigChangeNonVolatileCount.setStatus('current')
etsysConfigChangeNonVolatileTime = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigChangeNonVolatileTime.setStatus('current')
etsysConfigChangeNonVolatileMethod = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigChangeNonVolatileMethod.setStatus('current')
etsysConfigChangeVolatileCount = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigChangeVolatileCount.setStatus('current')
etsysConfigChangeVolatileTime = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 2, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigChangeVolatileTime.setStatus('current')
etsysConfigChangeVolatileMethod = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 2, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigChangeVolatileMethod.setStatus('current')
etsysConfigChangeFirmwareCount = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigChangeFirmwareCount.setStatus('current')
etsysConfigChangeFirmwareTime = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 3, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigChangeFirmwareTime.setStatus('current')
etsysConfigChangeFirmwareMethod = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 3, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysConfigChangeFirmwareMethod.setStatus('current')
etsysConfigChangeConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 4))
etsysConfigChangeGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 4, 1))
etsysConfigChangeCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 4, 2))
etsysConfigChangeNonVolatileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 4, 1, 1)).setObjects(("ENTERASYS-CONFIGURATION-CHANGE-MIB", "etsysConfigChangeNonVolatileCount"), ("ENTERASYS-CONFIGURATION-CHANGE-MIB", "etsysConfigChangeNonVolatileTime"), ("ENTERASYS-CONFIGURATION-CHANGE-MIB", "etsysConfigChangeNonVolatileMethod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysConfigChangeNonVolatileGroup = etsysConfigChangeNonVolatileGroup.setStatus('current')
etsysConfigChangeVolatileGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 4, 1, 2)).setObjects(("ENTERASYS-CONFIGURATION-CHANGE-MIB", "etsysConfigChangeVolatileCount"), ("ENTERASYS-CONFIGURATION-CHANGE-MIB", "etsysConfigChangeVolatileTime"), ("ENTERASYS-CONFIGURATION-CHANGE-MIB", "etsysConfigChangeVolatileMethod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysConfigChangeVolatileGroup = etsysConfigChangeVolatileGroup.setStatus('current')
etsysConfigChangeFirmwareGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 4, 1, 3)).setObjects(("ENTERASYS-CONFIGURATION-CHANGE-MIB", "etsysConfigChangeFirmwareCount"), ("ENTERASYS-CONFIGURATION-CHANGE-MIB", "etsysConfigChangeFirmwareTime"), ("ENTERASYS-CONFIGURATION-CHANGE-MIB", "etsysConfigChangeFirmwareMethod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysConfigChangeFirmwareGroup = etsysConfigChangeFirmwareGroup.setStatus('current')
etsysConfigChangeCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 12, 4, 2, 1)).setObjects(("ENTERASYS-CONFIGURATION-CHANGE-MIB", "etsysConfigChangeNonVolatileGroup"), ("ENTERASYS-CONFIGURATION-CHANGE-MIB", "etsysConfigChangeVolatileGroup"), ("ENTERASYS-CONFIGURATION-CHANGE-MIB", "etsysConfigChangeFirmwareGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysConfigChangeCompliance = etsysConfigChangeCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-CONFIGURATION-CHANGE-MIB", etsysConfigChangeVolatile=etsysConfigChangeVolatile, etsysConfigChangeNonVolatileMethod=etsysConfigChangeNonVolatileMethod, PYSNMP_MODULE_ID=etsysConfigurationChangeMIB, etsysConfigChangeConformance=etsysConfigChangeConformance, etsysConfigChangeCompliances=etsysConfigChangeCompliances, etsysConfigChangeVolatileGroup=etsysConfigChangeVolatileGroup, etsysConfigChangeFirmware=etsysConfigChangeFirmware, etsysConfigChangeFirmwareTime=etsysConfigChangeFirmwareTime, etsysConfigChangeNonVolatile=etsysConfigChangeNonVolatile, etsysConfigChangeFirmwareMethod=etsysConfigChangeFirmwareMethod, etsysConfigChangeCompliance=etsysConfigChangeCompliance, etsysConfigChangeGroups=etsysConfigChangeGroups, etsysConfigChangeNonVolatileTime=etsysConfigChangeNonVolatileTime, etsysConfigChangeVolatileTime=etsysConfigChangeVolatileTime, etsysConfigChangeVolatileMethod=etsysConfigChangeVolatileMethod, etsysConfigChangeVolatileCount=etsysConfigChangeVolatileCount, etsysConfigChangeNonVolatileGroup=etsysConfigChangeNonVolatileGroup, etsysConfigurationChangeMIB=etsysConfigurationChangeMIB, etsysConfigChangeFirmwareCount=etsysConfigChangeFirmwareCount, etsysConfigChangeNonVolatileCount=etsysConfigChangeNonVolatileCount, etsysConfigChangeFirmwareGroup=etsysConfigChangeFirmwareGroup)
