#
# PySNMP MIB module CLAVISTER-TRAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/clavister/CLAVISTER-TRAPS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:09:46 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
clavisterOSTrapInfo, clavisterOSTrap = mibBuilder.importSymbols("CLAVISTER-SMI", "clavisterOSTrapInfo", "clavisterOSTrap")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("CLAVISTER-TRAPS-MIB", clavisterOSTrapGroupTrap=clavisterOSTrapGroupTrap, clavisterOSTrapVarSeverity=clavisterOSTrapVarSeverity, clavisterOSTrapGroupVar=clavisterOSTrapGroupVar, clavisterOSTrapCompliance=clavisterOSTrapCompliance, clavisterOSTrapVarCategory=clavisterOSTrapVarCategory, clavisterOSTrapVarID=clavisterOSTrapVarID, clavisterOSTrapVarMessage=clavisterOSTrapVarMessage, clavisterOSTrapVarTime=clavisterOSTrapVarTime, PYSNMP_MODULE_ID=clavisterOSTrapMibModule, clavisterOSTrapMibModule=clavisterOSTrapMibModule, clavisterOSTrapVarAction=clavisterOSTrapVarAction, clavisterOSGenericTrap=clavisterOSGenericTrap, clavisterOSTrapVarEvent=clavisterOSTrapVarEvent)
