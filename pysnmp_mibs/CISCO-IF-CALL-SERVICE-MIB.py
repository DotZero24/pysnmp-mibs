#
# PySNMP MIB module CISCO-IF-CALL-SERVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cisco/CISCO-IF-CALL-SERVICE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:25:49 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
BulkConfigResult, ConfigIterator = mibBuilder.importSymbols("CISCO-TC", "BulkConfigResult", "ConfigIterator")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
OwnerString, = mibBuilder.importSymbols("RMON-MIB", "OwnerString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIfCallServiceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 9968))
ciscoIfCallServiceMIB.setRevisions(('2003-04-25 00:00',))
if mibBuilder.loadTexts: ciscoIfCallServiceMIB.setLastUpdated('200304250000Z')
if mibBuilder.loadTexts: ciscoIfCallServiceMIB.setOrganization('Cisco Systems, Inc.')
ciscoIfCallServiceMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9968, 0))
ciscoIfCallServiceMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1))
ciscoIfCallServiceMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9968, 2))
cicServiceConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1))
class CIfCallServiceOperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("inService", 1), ("outOfService", 2), ("oosPending", 3))

class CIfCallServiceAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("inService", 1), ("forcedOutOfService", 2), ("gracefulOutOfService", 3))

cicServiceTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1), )
if mibBuilder.loadTexts: cicServiceTable.setStatus('current')
cicServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cicServiceEntry.setStatus('current')
cicServiceOperState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 1), CIfCallServiceOperState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cicServiceOperState.setStatus('current')
cicServiceAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 2), CIfCallServiceAdminState().clone('inService')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicServiceAdminState.setStatus('current')
cicServiceGraceTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicServiceGraceTime.setStatus('current')
cicServiceRepetition = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 4), ConfigIterator().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicServiceRepetition.setStatus('current')
cicServiceRepeatOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 5), OwnerString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cicServiceRepeatOwner.setStatus('current')
cicServiceRepeatResult = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 9968, 1, 1, 1, 1, 6), BulkConfigResult()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cicServiceRepeatResult.setStatus('current')
cicServiceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9968, 2, 1))
cicServiceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 9968, 2, 2))
cicServiceCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 9968, 2, 1, 1)).setObjects(("CISCO-IF-CALL-SERVICE-MIB", "cicServiceGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cicServiceCompliance = cicServiceCompliance.setStatus('current')
cicServiceGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 9968, 2, 2, 1)).setObjects(("CISCO-IF-CALL-SERVICE-MIB", "cicServiceOperState"), ("CISCO-IF-CALL-SERVICE-MIB", "cicServiceAdminState"), ("CISCO-IF-CALL-SERVICE-MIB", "cicServiceGraceTime"), ("CISCO-IF-CALL-SERVICE-MIB", "cicServiceRepetition"), ("CISCO-IF-CALL-SERVICE-MIB", "cicServiceRepeatOwner"), ("CISCO-IF-CALL-SERVICE-MIB", "cicServiceRepeatResult"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cicServiceGroup = cicServiceGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-IF-CALL-SERVICE-MIB", cicServiceOperState=cicServiceOperState, cicServiceCompliance=cicServiceCompliance, cicServiceCompliances=cicServiceCompliances, cicServiceGroups=cicServiceGroups, cicServiceTable=cicServiceTable, ciscoIfCallServiceMIBObjects=ciscoIfCallServiceMIBObjects, ciscoIfCallServiceMIB=ciscoIfCallServiceMIB, cicServiceRepetition=cicServiceRepetition, cicServiceRepeatOwner=cicServiceRepeatOwner, cicServiceGroup=cicServiceGroup, ciscoIfCallServiceMIBNotifs=ciscoIfCallServiceMIBNotifs, CIfCallServiceAdminState=CIfCallServiceAdminState, PYSNMP_MODULE_ID=ciscoIfCallServiceMIB, cicServiceEntry=cicServiceEntry, cicServiceGraceTime=cicServiceGraceTime, CIfCallServiceOperState=CIfCallServiceOperState, cicServiceConfig=cicServiceConfig, ciscoIfCallServiceMIBConformance=ciscoIfCallServiceMIBConformance, cicServiceRepeatResult=cicServiceRepeatResult, cicServiceAdminState=cicServiceAdminState)
