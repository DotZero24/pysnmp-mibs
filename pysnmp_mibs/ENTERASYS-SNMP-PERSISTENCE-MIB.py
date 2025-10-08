#
# PySNMP MIB module ENTERASYS-SNMP-PERSISTENCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/enterasys/ENTERASYS-SNMP-PERSISTENCE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:34:14 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ENTERASYS-SNMP-PERSISTENCE-MIB", etsysSnmpPersistenceError=etsysSnmpPersistenceError, etsysSnmpPersistenceCompliances=etsysSnmpPersistenceCompliances, etsysSnmpPersistenceSave=etsysSnmpPersistenceSave, etsysSnmpPersistenceMIB=etsysSnmpPersistenceMIB, PYSNMP_MODULE_ID=etsysSnmpPersistenceMIB, etsysSnmpPersistenceConformance=etsysSnmpPersistenceConformance, etsysSnmpPersistenceObjects=etsysSnmpPersistenceObjects, etsysSnmpPersistenceErrorTime=etsysSnmpPersistenceErrorTime, etsysSnmpPersistenceStatusTime=etsysSnmpPersistenceStatusTime, etsysSnmpPersistenceGroups=etsysSnmpPersistenceGroups, etsysSnmpPersistenceCompliance=etsysSnmpPersistenceCompliance, etsysSnmpPersistenceMode=etsysSnmpPersistenceMode, etsysSnmpPersistenceGroup=etsysSnmpPersistenceGroup, etsysSnmpPersistenceStatus=etsysSnmpPersistenceStatus)
