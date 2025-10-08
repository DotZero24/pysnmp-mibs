#
# PySNMP MIB module ELTEX-MES-ISS-DHCP-SNOOP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-DHCP-SNOOP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:47 2025
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
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
eltMesIssDhcpSnoopMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 35265, 1, 139, 32))
eltMesIssDhcpSnoopMIB.setRevisions(('2022-10-05 00:00',))
if mibBuilder.loadTexts: eltMesIssDhcpSnoopMIB.setLastUpdated('202210050000Z')
if mibBuilder.loadTexts: eltMesIssDhcpSnoopMIB.setOrganization('Eltex Enterprise, Ltd.')
eltMesIssDhcpSnoopObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 32, 1))
eltMesIssDhcpSnoopGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 32, 1, 1))
eltMesIssDhcpSnoopInterfaceConfigs = MibIdentifier((1, 3, 6, 1, 4, 1, 35265, 1, 139, 32, 1, 2))
eltMesIssDhcpSnoopInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 35265, 1, 139, 32, 1, 2, 1), )
if mibBuilder.loadTexts: eltMesIssDhcpSnoopInterfaceTable.setStatus('current')
eltMesIssDhcpSnoopInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 35265, 1, 139, 32, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: eltMesIssDhcpSnoopInterfaceEntry.setStatus('current')
eltMesIssDhcpSnoopInterfaceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 35265, 1, 139, 32, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: eltMesIssDhcpSnoopInterfaceStatus.setStatus('current')
mibBuilder.exportSymbols("ELTEX-MES-ISS-DHCP-SNOOP-MIB", eltMesIssDhcpSnoopObjects=eltMesIssDhcpSnoopObjects, PYSNMP_MODULE_ID=eltMesIssDhcpSnoopMIB, eltMesIssDhcpSnoopInterfaceStatus=eltMesIssDhcpSnoopInterfaceStatus, eltMesIssDhcpSnoopInterfaceEntry=eltMesIssDhcpSnoopInterfaceEntry, eltMesIssDhcpSnoopInterfaceConfigs=eltMesIssDhcpSnoopInterfaceConfigs, eltMesIssDhcpSnoopMIB=eltMesIssDhcpSnoopMIB, eltMesIssDhcpSnoopGlobals=eltMesIssDhcpSnoopGlobals, eltMesIssDhcpSnoopInterfaceTable=eltMesIssDhcpSnoopInterfaceTable)
