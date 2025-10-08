#
# PySNMP MIB module CLAVISTER-TRAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/clavister/CLAVISTER-TRAPS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:42:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
clavisterOSTrap, clavisterOSTrapInfo = mibBuilder.importSymbols("CLAVISTER-SMI", "clavisterOSTrap", "clavisterOSTrapInfo")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
clavisterOSTrapMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 5089, 1, 1, 0))
clavisterOSTrapMibModule.setRevisions(('2015-10-21 17:00', '2007-10-31 00:00',))
if mibBuilder.loadTexts: clavisterOSTrapMibModule.setLastUpdated('201510211700Z')
if mibBuilder.loadTexts: clavisterOSTrapMibModule.setOrganization('Clavister AB')
clavisterOSTrapVarSeverity = MibScalar((1, 3, 6, 1, 4, 1, 5089, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: clavisterOSTrapVarSeverity.setStatus('current')
clavisterOSTrapVarCategory = MibScalar((1, 3, 6, 1, 4, 1, 5089, 1, 1, 5), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: clavisterOSTrapVarCategory.setStatus('current')
clavisterOSTrapVarID = MibScalar((1, 3, 6, 1, 4, 1, 5089, 1, 1, 6), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: clavisterOSTrapVarID.setStatus('current')
clavisterOSTrapVarEvent = MibScalar((1, 3, 6, 1, 4, 1, 5089, 1, 1, 7), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: clavisterOSTrapVarEvent.setStatus('current')
clavisterOSTrapVarAction = MibScalar((1, 3, 6, 1, 4, 1, 5089, 1, 1, 8), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: clavisterOSTrapVarAction.setStatus('current')
clavisterOSTrapVarTime = MibScalar((1, 3, 6, 1, 4, 1, 5089, 1, 1, 9), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: clavisterOSTrapVarTime.setStatus('current')
clavisterOSTrapVarMessage = MibScalar((1, 3, 6, 1, 4, 1, 5089, 1, 1, 10), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: clavisterOSTrapVarMessage.setStatus('current')
clavisterOSGenericTrap = NotificationType((1, 3, 6, 1, 4, 1, 5089, 1, 0, 1)).setObjects(("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarSeverity"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarCategory"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarID"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarEvent"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarAction"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarTime"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarMessage"))
if mibBuilder.loadTexts: clavisterOSGenericTrap.setStatus('current')
clavisterOSTrapGroupTrap = NotificationGroup((1, 3, 6, 1, 4, 1, 5089, 1, 1, 1)).setObjects(("CLAVISTER-TRAPS-MIB", "clavisterOSGenericTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clavisterOSTrapGroupTrap = clavisterOSTrapGroupTrap.setStatus('current')
clavisterOSTrapGroupVar = ObjectGroup((1, 3, 6, 1, 4, 1, 5089, 1, 1, 2)).setObjects(("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarSeverity"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarCategory"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarID"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarEvent"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarAction"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarTime"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapVarMessage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clavisterOSTrapGroupVar = clavisterOSTrapGroupVar.setStatus('current')
clavisterOSTrapCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5089, 1, 1, 3)).setObjects(("CLAVISTER-TRAPS-MIB", "clavisterOSTrapGroupTrap"), ("CLAVISTER-TRAPS-MIB", "clavisterOSTrapGroupVar"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    clavisterOSTrapCompliance = clavisterOSTrapCompliance.setStatus('current')
mibBuilder.exportSymbols("CLAVISTER-TRAPS-MIB", clavisterOSTrapGroupVar=clavisterOSTrapGroupVar, clavisterOSTrapVarMessage=clavisterOSTrapVarMessage, clavisterOSTrapVarTime=clavisterOSTrapVarTime, clavisterOSTrapGroupTrap=clavisterOSTrapGroupTrap, PYSNMP_MODULE_ID=clavisterOSTrapMibModule, clavisterOSTrapVarAction=clavisterOSTrapVarAction, clavisterOSTrapVarCategory=clavisterOSTrapVarCategory, clavisterOSTrapCompliance=clavisterOSTrapCompliance, clavisterOSTrapMibModule=clavisterOSTrapMibModule, clavisterOSTrapVarSeverity=clavisterOSTrapVarSeverity, clavisterOSTrapVarEvent=clavisterOSTrapVarEvent, clavisterOSTrapVarID=clavisterOSTrapVarID, clavisterOSGenericTrap=clavisterOSGenericTrap)
