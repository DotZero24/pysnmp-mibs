#
# PySNMP MIB module ENTERASYS-SNMP-PERSISTENCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/enterasys/ENTERASYS-SNMP-PERSISTENCE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:32 2025
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
etsysSnmpPersistenceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24))
etsysSnmpPersistenceMIB.setRevisions(('2002-09-09 20:22',))
if mibBuilder.loadTexts: etsysSnmpPersistenceMIB.setLastUpdated('200209092022Z')
if mibBuilder.loadTexts: etsysSnmpPersistenceMIB.setOrganization('Enterasys Networks Inc')
etsysSnmpPersistenceObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 1))
etsysSnmpPersistenceMode = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("snmpNormalSave", 1), ("pushButtonSave", 2), ("timeDelayedSave", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSnmpPersistenceMode.setStatus('current')
etsysSnmpPersistenceSave = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("nop", 1), ("save", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysSnmpPersistenceSave.setStatus('current')
etsysSnmpPersistenceStatus = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("unsavedChanges", 2), ("savingChanges", 3), ("saveSucceeded", 4), ("saveFailed", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSnmpPersistenceStatus.setStatus('current')
etsysSnmpPersistenceStatusTime = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSnmpPersistenceStatusTime.setStatus('current')
etsysSnmpPersistenceError = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSnmpPersistenceError.setStatus('current')
etsysSnmpPersistenceErrorTime = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysSnmpPersistenceErrorTime.setStatus('current')
etsysSnmpPersistenceConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 2))
etsysSnmpPersistenceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 2, 1))
etsysSnmpPersistenceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 2, 2))
etsysSnmpPersistenceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 2, 1, 1)).setObjects(("ENTERASYS-SNMP-PERSISTENCE-MIB", "etsysSnmpPersistenceMode"), ("ENTERASYS-SNMP-PERSISTENCE-MIB", "etsysSnmpPersistenceSave"), ("ENTERASYS-SNMP-PERSISTENCE-MIB", "etsysSnmpPersistenceStatus"), ("ENTERASYS-SNMP-PERSISTENCE-MIB", "etsysSnmpPersistenceStatusTime"), ("ENTERASYS-SNMP-PERSISTENCE-MIB", "etsysSnmpPersistenceError"), ("ENTERASYS-SNMP-PERSISTENCE-MIB", "etsysSnmpPersistenceErrorTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysSnmpPersistenceGroup = etsysSnmpPersistenceGroup.setStatus('current')
etsysSnmpPersistenceCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 24, 2, 2, 1)).setObjects(("ENTERASYS-SNMP-PERSISTENCE-MIB", "etsysSnmpPersistenceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysSnmpPersistenceCompliance = etsysSnmpPersistenceCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-SNMP-PERSISTENCE-MIB", etsysSnmpPersistenceMIB=etsysSnmpPersistenceMIB, etsysSnmpPersistenceStatus=etsysSnmpPersistenceStatus, etsysSnmpPersistenceGroup=etsysSnmpPersistenceGroup, PYSNMP_MODULE_ID=etsysSnmpPersistenceMIB, etsysSnmpPersistenceErrorTime=etsysSnmpPersistenceErrorTime, etsysSnmpPersistenceConformance=etsysSnmpPersistenceConformance, etsysSnmpPersistenceCompliances=etsysSnmpPersistenceCompliances, etsysSnmpPersistenceError=etsysSnmpPersistenceError, etsysSnmpPersistenceMode=etsysSnmpPersistenceMode, etsysSnmpPersistenceCompliance=etsysSnmpPersistenceCompliance, etsysSnmpPersistenceSave=etsysSnmpPersistenceSave, etsysSnmpPersistenceStatusTime=etsysSnmpPersistenceStatusTime, etsysSnmpPersistenceGroups=etsysSnmpPersistenceGroups, etsysSnmpPersistenceObjects=etsysSnmpPersistenceObjects)
