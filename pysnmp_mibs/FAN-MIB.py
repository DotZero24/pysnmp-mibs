#
# PySNMP MIB module FAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/hp/FAN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:03:34 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpicfFanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54))
hpicfFanMIB.setRevisions(('2008-08-27 10:30',))
if mibBuilder.loadTexts: hpicfFanMIB.setLastUpdated('200808271030Z')
if mibBuilder.loadTexts: hpicfFanMIB.setOrganization('HP Networking')
class HpicfDcFanIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class HpicfDcFanType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 0), ("mm", 1), ("fm", 2), ("im", 3), ("ps", 4), ("rollup", 5), ("maxtype", 6))

class HpicfDcFanAirflowDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("portToPower", 1), ("powerToPort", 2))

class HpicfDcFanState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("failed", 0), ("removed", 1), ("off", 2), ("underspeed", 3), ("overspeed", 4), ("ok", 5), ("maxstate", 6))

hpicfFanScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 1))
hpicfFanUserPrefAirflowDir = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("portToPower", 1), ("powerToPort", 2))).clone('powerToPort')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfFanUserPrefAirflowDir.setStatus('current')
hpicfEntityFan = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2))
hpicfFanTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1), )
if mibBuilder.loadTexts: hpicfFanTable.setStatus('current')
hpicfFanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1, 1), ).setIndexNames((0, "FAN-MIB", "hpicfFanIndex"))
if mibBuilder.loadTexts: hpicfFanEntry.setStatus('current')
hpicfFanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1, 1, 1), HpicfDcFanIndex())
if mibBuilder.loadTexts: hpicfFanIndex.setStatus('current')
hpicfFanTray = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFanTray.setStatus('current')
hpicfFanType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1, 1, 3), HpicfDcFanType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFanType.setStatus('current')
hpicfFanState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1, 1, 4), HpicfDcFanState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFanState.setStatus('current')
hpicfFanRecovering = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFanRecovering.setStatus('current')
hpicfFanNumFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFanNumFailures.setStatus('current')
hpicfFanAirflowDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 2, 1, 1, 7), HpicfDcFanAirflowDirection()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfFanAirflowDirection.setStatus('current')
hpicfFanConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 3))
hpicfFanCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 3, 1))
hpicfFanGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 3, 2))
hpicfDcFanCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 3, 1, 1)).setObjects(("FAN-MIB", "hpicfFanScalarsGroup"), ("FAN-MIB", "hpicfFanGroup"), ("FAN-MIB", "hpicfFanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDcFanCompliance = hpicfDcFanCompliance.setStatus('current')
hpicfFanScalarsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 3, 2, 1)).setObjects(("FAN-MIB", "hpicfFanUserPrefAirflowDir"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFanScalarsGroup = hpicfFanScalarsGroup.setStatus('current')
hpicfFanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 54, 3, 2, 2)).setObjects(("FAN-MIB", "hpicfFanTray"), ("FAN-MIB", "hpicfFanType"), ("FAN-MIB", "hpicfFanState"), ("FAN-MIB", "hpicfFanRecovering"), ("FAN-MIB", "hpicfFanNumFailures"), ("FAN-MIB", "hpicfFanAirflowDirection"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfFanGroup = hpicfFanGroup.setStatus('current')
mibBuilder.exportSymbols("FAN-MIB", hpicfFanGroups=hpicfFanGroups, hpicfDcFanCompliance=hpicfDcFanCompliance, hpicfFanConformance=hpicfFanConformance, hpicfFanIndex=hpicfFanIndex, hpicfFanTray=hpicfFanTray, hpicfFanCompliance=hpicfFanCompliance, hpicfFanTable=hpicfFanTable, HpicfDcFanState=HpicfDcFanState, hpicfFanMIB=hpicfFanMIB, hpicfEntityFan=hpicfEntityFan, hpicfFanUserPrefAirflowDir=hpicfFanUserPrefAirflowDir, hpicfFanType=hpicfFanType, HpicfDcFanType=HpicfDcFanType, hpicfFanNumFailures=hpicfFanNumFailures, PYSNMP_MODULE_ID=hpicfFanMIB, hpicfFanState=hpicfFanState, hpicfFanAirflowDirection=hpicfFanAirflowDirection, hpicfFanRecovering=hpicfFanRecovering, hpicfFanGroup=hpicfFanGroup, hpicfFanScalars=hpicfFanScalars, HpicfDcFanIndex=HpicfDcFanIndex, hpicfFanEntry=hpicfFanEntry, HpicfDcFanAirflowDirection=HpicfDcFanAirflowDirection, hpicfFanScalarsGroup=hpicfFanScalarsGroup)
