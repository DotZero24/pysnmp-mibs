#
# PySNMP MIB module ELTEX-MES-POE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-POE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:42 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ELTEX-MES-POE-MIB", eltMesPoe=eltMesPoe, PYSNMP_MODULE_ID=eltMesPoe, eltMesPoeNotifications=eltMesPoeNotifications, eltMesPoeObjects=eltMesPoeObjects, eltPoeAutoRestart=eltPoeAutoRestart, eltPoeRestartAction=eltPoeRestartAction, eltPoeDisabled=eltPoeDisabled)
