#
# PySNMP MIB module DNOS-INTERFACE-APP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/dell/DNOS-INTERFACE-APP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:44:42 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dnOS, = mibBuilder.importSymbols("DELL-REF-MIB", "dnOS")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
fastPathInterfaceApp = ModuleIdentity((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 70))
fastPathInterfaceApp.setRevisions(('2016-08-18 00:00',))
if mibBuilder.loadTexts: fastPathInterfaceApp.setLastUpdated('201608180000Z')
if mibBuilder.loadTexts: fastPathInterfaceApp.setOrganization('Dell EMC')
agentLinkFlapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 70, 1))
agentLinkFlapGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 70, 1, 1))
agentLinkFlapAdminMode = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 70, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLinkFlapAdminMode.setStatus('current')
agentLinkFlapDuration = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 70, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(3, 200))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLinkFlapDuration.setStatus('current')
agentLinkFlapMaxCount = MibScalar((1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 70, 1, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLinkFlapMaxCount.setStatus('current')
mibBuilder.exportSymbols("DNOS-INTERFACE-APP-MIB", agentLinkFlapAdminMode=agentLinkFlapAdminMode, fastPathInterfaceApp=fastPathInterfaceApp, agentLinkFlapMIBObjects=agentLinkFlapMIBObjects, agentLinkFlapGlobal=agentLinkFlapGlobal, PYSNMP_MODULE_ID=fastPathInterfaceApp, agentLinkFlapDuration=agentLinkFlapDuration, agentLinkFlapMaxCount=agentLinkFlapMaxCount)
