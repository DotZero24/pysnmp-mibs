#
# PySNMP MIB module ELTEX-MES-POE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-MES-POE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:30 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
eltMesPoe = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 16))
eltMesPoe.setRevisions(('2019-04-02 00:00', '2017-11-07 00:00',))
if mibBuilder.loadTexts: eltMesPoe.setLastUpdated('201904020000Z')
if mibBuilder.loadTexts: eltMesPoe.setOrganization('Eltex Enterprise Co, Ltd.')
eltMesPoeNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 16, 0))
eltMesPoeObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 23, 16, 1))
eltPoeRestartAction = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 16, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 8), ValueRangeConstraint(255, 255), )).clone(255)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltPoeRestartAction.setStatus('current')
eltPoeDisabled = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 16, 1, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltPoeDisabled.setStatus('current')
eltPoeAutoRestart = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 23, 16, 1, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltPoeAutoRestart.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-POE-MIB", PYSNMP_MODULE_ID=eltMesPoe, eltPoeDisabled=eltPoeDisabled, eltPoeAutoRestart=eltPoeAutoRestart, eltMesPoe=eltMesPoe, eltMesPoeObjects=eltMesPoeObjects, eltMesPoeNotifications=eltMesPoeNotifications, eltPoeRestartAction=eltPoeRestartAction)
