#
# PySNMP MIB module DNOS-INTERFACE-APP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/dell/DNOS-INTERFACE-APP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:24:04 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dnOS, = mibBuilder.importSymbols("DELL-REF-MIB", "dnOS")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("DNOS-INTERFACE-APP-MIB", agentLinkFlapGlobal=agentLinkFlapGlobal, agentLinkFlapAdminMode=agentLinkFlapAdminMode, agentLinkFlapMIBObjects=agentLinkFlapMIBObjects, fastPathInterfaceApp=fastPathInterfaceApp, agentLinkFlapDuration=agentLinkFlapDuration, PYSNMP_MODULE_ID=fastPathInterfaceApp, agentLinkFlapMaxCount=agentLinkFlapMaxCount)
