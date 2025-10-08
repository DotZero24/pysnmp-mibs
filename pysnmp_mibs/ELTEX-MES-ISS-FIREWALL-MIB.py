#
# PySNMP MIB module ELTEX-MES-ISS-FIREWALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-FIREWALL-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:24 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
eltMesIss, = mibBuilder.importSymbols("ELTEX-MES-ISS-MIB", "eltMesIss")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
eltMesIssFwlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 139, 27))
eltMesIssFwlMIB.setRevisions(('2021-04-21 00:00',))
if mibBuilder.loadTexts: eltMesIssFwlMIB.setLastUpdated('202104210000Z')
if mibBuilder.loadTexts: eltMesIssFwlMIB.setOrganization('Eltex Enterprise, Ltd.')
eltMesIssFwlObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 27, 1))
eltMesIssFwlNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 27, 2))
eltMesIssFwlGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 27, 1, 1))
eltMesIssFwlTcpSynLimit = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 27, 1, 2))
eltMesIssFwlNotificationInterval = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 27, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssFwlNotificationInterval.setStatus('current')
eltMesIssFwlTcpSynLimitEnable = MibScalar((1, 3, 6, 1, 4, 1, 35265, 1, 139, 27, 1, 2, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssFwlTcpSynLimitEnable.setStatus('current')
eltMesIssFwlTcpSynLimitInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 139, 27, 1, 2, 2), )
if mibBuilder.loadTexts: eltMesIssFwlTcpSynLimitInterfaceTable.setStatus('current')
eltMesIssFwlTcpSynLimitInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 139, 27, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: eltMesIssFwlTcpSynLimitInterfaceEntry.setStatus('current')
eltMesIssFwlTcpSynLimitValue = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 139, 27, 1, 2, 2, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssFwlTcpSynLimitValue.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-ISS-FIREWALL-MIB", eltMesIssFwlTcpSynLimitInterfaceTable=eltMesIssFwlTcpSynLimitInterfaceTable, eltMesIssFwlGlobals=eltMesIssFwlGlobals, eltMesIssFwlTcpSynLimit=eltMesIssFwlTcpSynLimit, eltMesIssFwlNotificationInterval=eltMesIssFwlNotificationInterval, eltMesIssFwlMIB=eltMesIssFwlMIB, eltMesIssFwlTcpSynLimitInterfaceEntry=eltMesIssFwlTcpSynLimitInterfaceEntry, eltMesIssFwlTcpSynLimitValue=eltMesIssFwlTcpSynLimitValue, PYSNMP_MODULE_ID=eltMesIssFwlMIB, eltMesIssFwlTcpSynLimitEnable=eltMesIssFwlTcpSynLimitEnable, eltMesIssFwlNotifications=eltMesIssFwlNotifications, eltMesIssFwlObjects=eltMesIssFwlObjects)
