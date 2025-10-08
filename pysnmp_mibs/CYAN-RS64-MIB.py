#
# PySNMP MIB module CYAN-RS64-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cyan/CYAN-RS64-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:15:58 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cyanEntityModules, = mibBuilder.importSymbols("CYAN-MIB", "cyanEntityModules")
CyanAdminStateTc, CyanOpStateQualTc, CyanSecServiceStateTc, CyanOpStateTc = mibBuilder.importSymbols("CYAN-TC-MIB", "CyanAdminStateTc", "CyanOpStateQualTc", "CyanSecServiceStateTc", "CyanOpStateTc")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cyanRS64Module = ModuleIdentity((1, 3, 6, 1, 4, 1, 28533, 5, 30, 220))
cyanRS64Module.setRevisions(('2014-12-07 05:45',))
if mibBuilder.loadTexts: cyanRS64Module.setLastUpdated('201412070545Z')
if mibBuilder.loadTexts: cyanRS64Module.setOrganization('Cyan, Inc.')
cyanRS64MibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 1))
cyanRS64Table = MibTable((1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 1, 1), )
if mibBuilder.loadTexts: cyanRS64Table.setStatus('current')
cyanRS64Entry = MibTableRow((1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 1, 1, 1), ).setIndexNames((0, "CYAN-RS64-MIB", "cyanRS64ShelfId"), (0, "CYAN-RS64-MIB", "cyanRS64ModuleId"), (0, "CYAN-RS64-MIB", "cyanRS64RS64Id"))
if mibBuilder.loadTexts: cyanRS64Entry.setStatus('current')
cyanRS64ShelfId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: cyanRS64ShelfId.setStatus('current')
cyanRS64ModuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 1, 1, 1, 2), Unsigned32())
if mibBuilder.loadTexts: cyanRS64ModuleId.setStatus('current')
cyanRS64RS64Id = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 1, 1, 1, 3), Unsigned32())
if mibBuilder.loadTexts: cyanRS64RS64Id.setStatus('current')
cyanRS64AdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 1, 1, 1, 4), CyanAdminStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRS64AdminState.setStatus('current')
cyanRS64AutoinserviceSoakTimeSec = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRS64AutoinserviceSoakTimeSec.setStatus('current')
cyanRS64OperState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 1, 1, 1, 6), CyanOpStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRS64OperState.setStatus('current')
cyanRS64OperStateQual = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 1, 1, 1, 7), CyanOpStateQualTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRS64OperStateQual.setStatus('current')
cyanRS64SecServState = MibTableColumn((1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 1, 1, 1, 8), CyanSecServiceStateTc()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cyanRS64SecServState.setStatus('current')
cyanRS64ObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 20)).setObjects(("CYAN-RS64-MIB", "cyanRS64AdminState"), ("CYAN-RS64-MIB", "cyanRS64AutoinserviceSoakTimeSec"), ("CYAN-RS64-MIB", "cyanRS64OperState"), ("CYAN-RS64-MIB", "cyanRS64OperStateQual"), ("CYAN-RS64-MIB", "cyanRS64SecServState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cyanRS64ObjectGroup = cyanRS64ObjectGroup.setStatus('current')
cyanRS64Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 28533, 5, 30, 220, 30)).setObjects(("CYAN-RS64-MIB", "cyanRS64ObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cyanRS64Compliance = cyanRS64Compliance.setStatus('current')
mibBuilder.exportSymbols("CYAN-RS64-MIB", cyanRS64Entry=cyanRS64Entry, cyanRS64Table=cyanRS64Table, cyanRS64ShelfId=cyanRS64ShelfId, cyanRS64RS64Id=cyanRS64RS64Id, cyanRS64AutoinserviceSoakTimeSec=cyanRS64AutoinserviceSoakTimeSec, cyanRS64OperState=cyanRS64OperState, cyanRS64SecServState=cyanRS64SecServState, PYSNMP_MODULE_ID=cyanRS64Module, cyanRS64MibObjects=cyanRS64MibObjects, cyanRS64OperStateQual=cyanRS64OperStateQual, cyanRS64Compliance=cyanRS64Compliance, cyanRS64Module=cyanRS64Module, cyanRS64AdminState=cyanRS64AdminState, cyanRS64ObjectGroup=cyanRS64ObjectGroup, cyanRS64ModuleId=cyanRS64ModuleId)
