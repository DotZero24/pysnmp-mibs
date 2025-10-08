#
# PySNMP MIB module ELTEX-MES-TRAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-MES-TRAPS-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:41 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
rldot1dStpTrapVrblifIndex, rldot1dStpTrapVrblVID = mibBuilder.importSymbols("RADLAN-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblifIndex", "rldot1dStpTrapVrblVID")
rndErrorDesc, rndErrorSeverity = mibBuilder.importSymbols("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc", "rndErrorSeverity")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eltMesNotifications = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 23, 0))
eltMesNotifications.setRevisions(('2012-07-13 00:00',))
if mibBuilder.loadTexts: eltMesNotifications.setLastUpdated('201207130000Z')
if mibBuilder.loadTexts: eltMesNotifications.setOrganization('Eltex Enterprise Co, Ltd.')
eltdot1dStpTopologyChange = NotificationType((1, 3, 6, 1, 4, 1, 35265, 1, 23, 0, 7)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"), ("RADLAN-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblifIndex"), ("RADLAN-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblVID"))
if mibBuilder.loadTexts: eltdot1dStpTopologyChange.setStatus('current')
eltdot1dStpRootBridgeChange = NotificationType((1, 3, 6, 1, 4, 1, 35265, 1, 23, 0, 8)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"), ("RADLAN-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblifIndex"), ("RADLAN-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblVID"))
if mibBuilder.loadTexts: eltdot1dStpRootBridgeChange.setStatus('current')
eltdot1dStpTcProtectionThresholdReached = NotificationType((1, 3, 6, 1, 4, 1, 35265, 1, 23, 0, 9)).setObjects(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"), ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"), ("RADLAN-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblVID"))
if mibBuilder.loadTexts: eltdot1dStpTcProtectionThresholdReached.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-TRAPS-MIB", eltdot1dStpTopologyChange=eltdot1dStpTopologyChange, eltdot1dStpRootBridgeChange=eltdot1dStpRootBridgeChange, eltdot1dStpTcProtectionThresholdReached=eltdot1dStpTcProtectionThresholdReached, PYSNMP_MODULE_ID=eltMesNotifications, eltMesNotifications=eltMesNotifications)
