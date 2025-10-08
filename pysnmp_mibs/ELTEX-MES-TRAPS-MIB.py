#
# PySNMP MIB module ELTEX-MES-TRAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-TRAPS-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:12:00 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltMes, = mibBuilder.importSymbols("ELTEX-MES", "eltMes")
rldot1dStpTrapVrblifIndex, rldot1dStpTrapVrblVID = mibBuilder.importSymbols("RADLAN-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblifIndex", "rldot1dStpTrapVrblVID")
rndErrorSeverity, rndErrorDesc = mibBuilder.importSymbols("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity", "rndErrorDesc")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ELTEX-MES-TRAPS-MIB", eltdot1dStpTopologyChange=eltdot1dStpTopologyChange, eltMesNotifications=eltMesNotifications, PYSNMP_MODULE_ID=eltMesNotifications, eltdot1dStpRootBridgeChange=eltdot1dStpRootBridgeChange, eltdot1dStpTcProtectionThresholdReached=eltdot1dStpTcProtectionThresholdReached)
