#
# PySNMP MIB module RUCKUS-PPPOE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ruckus/RUCKUS-PPPOE-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:41:32 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ruckusCommonPPPOEModule, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusCommonPPPOEModule")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ruckusPPPOEMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1))
if mibBuilder.loadTexts: ruckusPPPOEMIB.setLastUpdated('201010150800Z')
if mibBuilder.loadTexts: ruckusPPPOEMIB.setOrganization('Ruckus Wireless, Inc')
ruckusPPPOEObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 1))
ruckusPPPOEInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 1, 1))
ruckusPPPOEEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 2))
ruckusPPPOEUserName = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusPPPOEUserName.setStatus('current')
ruckusPPPOEPassword = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusPPPOEPassword.setStatus('current')
ruckusPPPOEConnectionStatus = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("connected", 1), ("notConnected", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusPPPOEConnectionStatus.setStatus('current')
ruckusPPPOEConnection = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("connect", 1), ("disConnect", 2), ("ok", 3), ("disabled", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusPPPOEConnection.setStatus('current')
ruckusPPPOEIfindex = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 1, 1, 5), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ruckusPPPOEIfindex.setStatus('current')
ruckusPPPOEApply = MibScalar((1, 3, 6, 1, 4, 1, 25053, 1, 1, 8, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("apply", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ruckusPPPOEApply.setStatus('current')
mibBuilder.exportSymbols("RUCKUS-PPPOE-MIB", PYSNMP_MODULE_ID=ruckusPPPOEMIB, ruckusPPPOEApply=ruckusPPPOEApply, ruckusPPPOEIfindex=ruckusPPPOEIfindex, ruckusPPPOEConnection=ruckusPPPOEConnection, ruckusPPPOEUserName=ruckusPPPOEUserName, ruckusPPPOEMIB=ruckusPPPOEMIB, ruckusPPPOEInfo=ruckusPPPOEInfo, ruckusPPPOEConnectionStatus=ruckusPPPOEConnectionStatus, ruckusPPPOEObjects=ruckusPPPOEObjects, ruckusPPPOEPassword=ruckusPPPOEPassword, ruckusPPPOEEvents=ruckusPPPOEEvents)
