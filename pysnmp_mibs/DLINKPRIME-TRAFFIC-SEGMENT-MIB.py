#
# PySNMP MIB module DLINKPRIME-TRAFFIC-SEGMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/DLINKPRIME-TRAFFIC-SEGMENT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:00:17 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlinkPrimeCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkPrimeCommon")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dlinkPrimeTrafficSegMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 15, 25))
dlinkPrimeTrafficSegMIB.setRevisions(('2014-04-26 00:00',))
if mibBuilder.loadTexts: dlinkPrimeTrafficSegMIB.setLastUpdated('201404260000Z')
if mibBuilder.loadTexts: dlinkPrimeTrafficSegMIB.setOrganization('D-Link Corp.')
dpTrafficSegNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 25, 0))
dpTrafficSegObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 25, 1))
dpTrafficSegConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 25, 2))
dpTrafficSegForwardDomainTable = MibTable((1, 3, 6, 1, 4, 1, 171, 15, 25, 1, 1), )
if mibBuilder.loadTexts: dpTrafficSegForwardDomainTable.setStatus('current')
dpTrafficSegForwardDomainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 15, 25, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dpTrafficSegForwardDomainEntry.setStatus('current')
dpTrafficSegForwardPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 15, 25, 1, 1, 1, 1), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpTrafficSegForwardPorts.setStatus('current')
dpTrafficSegMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 25, 2, 1))
dpTrafficSegMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 15, 25, 2, 2))
dpTrafficSegMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 171, 15, 25, 2, 1, 1)).setObjects(("DLINKPRIME-TRAFFIC-SEGMENT-MIB", "dpTrafficSegIfCfgGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpTrafficSegMIBCompliance = dpTrafficSegMIBCompliance.setStatus('current')
dpTrafficSegIfCfgGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 171, 15, 25, 2, 2, 1)).setObjects(("DLINKPRIME-TRAFFIC-SEGMENT-MIB", "dpTrafficSegForwardPorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dpTrafficSegIfCfgGroup = dpTrafficSegIfCfgGroup.setStatus('current')
mibBuilder.exportSymbols("DLINKPRIME-TRAFFIC-SEGMENT-MIB", dpTrafficSegObjects=dpTrafficSegObjects, PYSNMP_MODULE_ID=dlinkPrimeTrafficSegMIB, dpTrafficSegMIBCompliance=dpTrafficSegMIBCompliance, dpTrafficSegForwardDomainTable=dpTrafficSegForwardDomainTable, dpTrafficSegForwardDomainEntry=dpTrafficSegForwardDomainEntry, dpTrafficSegForwardPorts=dpTrafficSegForwardPorts, dpTrafficSegMIBGroups=dpTrafficSegMIBGroups, dpTrafficSegNotifications=dpTrafficSegNotifications, dpTrafficSegConformance=dpTrafficSegConformance, dpTrafficSegIfCfgGroup=dpTrafficSegIfCfgGroup, dpTrafficSegMIBCompliances=dpTrafficSegMIBCompliances, dlinkPrimeTrafficSegMIB=dlinkPrimeTrafficSegMIB)
