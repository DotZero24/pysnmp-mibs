#
# PySNMP MIB module DLINKPRIME-TRAFFIC-SEGMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DLINKPRIME-TRAFFIC-SEGMENT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:35:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlinkPrimeCommon, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlinkPrimeCommon")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("DLINKPRIME-TRAFFIC-SEGMENT-MIB", dpTrafficSegConformance=dpTrafficSegConformance, dpTrafficSegMIBCompliance=dpTrafficSegMIBCompliance, dpTrafficSegForwardPorts=dpTrafficSegForwardPorts, PYSNMP_MODULE_ID=dlinkPrimeTrafficSegMIB, dpTrafficSegObjects=dpTrafficSegObjects, dpTrafficSegMIBCompliances=dpTrafficSegMIBCompliances, dpTrafficSegForwardDomainTable=dpTrafficSegForwardDomainTable, dlinkPrimeTrafficSegMIB=dlinkPrimeTrafficSegMIB, dpTrafficSegMIBGroups=dpTrafficSegMIBGroups, dpTrafficSegForwardDomainEntry=dpTrafficSegForwardDomainEntry, dpTrafficSegIfCfgGroup=dpTrafficSegIfCfgGroup, dpTrafficSegNotifications=dpTrafficSegNotifications)
