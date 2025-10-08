#
# PySNMP MIB module ELTEX-MES-ISS-DHCP-SNOOP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/eltex/ELTEX-MES-ISS-DHCP-SNOOP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:12:10 2025
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
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ELTEX-MES-ISS-DHCP-SNOOP-MIB", eltMesIssDhcpSnoopInterfaceEntry=eltMesIssDhcpSnoopInterfaceEntry, eltMesIssDhcpSnoopInterfaceConfigs=eltMesIssDhcpSnoopInterfaceConfigs, eltMesIssDhcpSnoopInterfaceTable=eltMesIssDhcpSnoopInterfaceTable, eltMesIssDhcpSnoopGlobals=eltMesIssDhcpSnoopGlobals, PYSNMP_MODULE_ID=eltMesIssDhcpSnoopMIB, eltMesIssDhcpSnoopMIB=eltMesIssDhcpSnoopMIB, eltMesIssDhcpSnoopObjects=eltMesIssDhcpSnoopObjects, eltMesIssDhcpSnoopInterfaceStatus=eltMesIssDhcpSnoopInterfaceStatus)
