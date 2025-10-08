#
# PySNMP MIB module DES3810-52-SWITCH-RESOURCE-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/DES3810-52-SWITCH-RESOURCE-MGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:34:17 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
des3810_52, = mibBuilder.importSymbols("SW3810PRIMGMT-MIB", "des3810-52")
swSwitchResourceMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 4))
if mibBuilder.loadTexts: swSwitchResourceMgmtMIB.setLastUpdated('201005060000Z')
if mibBuilder.loadTexts: swSwitchResourceMgmtMIB.setOrganization('D-Link Corp.')
swSwitchResourceMgmtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 4, 1))
swSwitchResourceMgmtSRMMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("routing", 1), ("vpws", 2))).clone('routing')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSwitchResourceMgmtSRMMode.setStatus('current')
swSwitchResourceMgmtSRMCurrentMode = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 114, 1, 3, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("routing", 1), ("vpws", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSwitchResourceMgmtSRMCurrentMode.setStatus('current')
mibBuilder.exportSymbols("DES3810-52-SWITCH-RESOURCE-MGMT-MIB", swSwitchResourceMgmtMIB=swSwitchResourceMgmtMIB, swSwitchResourceMgmtSRMMode=swSwitchResourceMgmtSRMMode, PYSNMP_MODULE_ID=swSwitchResourceMgmtMIB, swSwitchResourceMgmtMIBObjects=swSwitchResourceMgmtMIBObjects, swSwitchResourceMgmtSRMCurrentMode=swSwitchResourceMgmtSRMCurrentMode)
