#
# PySNMP MIB module ELTEX-MES-ISS-FIREWALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-FIREWALL-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:33 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
eltMesIss, = mibBuilder.importSymbols("ELTEX-MES-ISS-MIB", "eltMesIss")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ELTEX-MES-ISS-FIREWALL-MIB", eltMesIssFwlTcpSynLimitEnable=eltMesIssFwlTcpSynLimitEnable, eltMesIssFwlTcpSynLimitInterfaceEntry=eltMesIssFwlTcpSynLimitInterfaceEntry, PYSNMP_MODULE_ID=eltMesIssFwlMIB, eltMesIssFwlNotifications=eltMesIssFwlNotifications, eltMesIssFwlTcpSynLimit=eltMesIssFwlTcpSynLimit, eltMesIssFwlGlobals=eltMesIssFwlGlobals, eltMesIssFwlTcpSynLimitValue=eltMesIssFwlTcpSynLimitValue, eltMesIssFwlMIB=eltMesIssFwlMIB, eltMesIssFwlTcpSynLimitInterfaceTable=eltMesIssFwlTcpSynLimitInterfaceTable, eltMesIssFwlNotificationInterval=eltMesIssFwlNotificationInterval, eltMesIssFwlObjects=eltMesIssFwlObjects)
