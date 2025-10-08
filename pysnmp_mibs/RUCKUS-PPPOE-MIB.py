#
# PySNMP MIB module RUCKUS-PPPOE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ruckus/RUCKUS-PPPOE-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:08:36 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ruckusCommonPPPOEModule, = mibBuilder.importSymbols("RUCKUS-ROOT-MIB", "ruckusCommonPPPOEModule")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("RUCKUS-PPPOE-MIB", PYSNMP_MODULE_ID=ruckusPPPOEMIB, ruckusPPPOEApply=ruckusPPPOEApply, ruckusPPPOEMIB=ruckusPPPOEMIB, ruckusPPPOEPassword=ruckusPPPOEPassword, ruckusPPPOEConnectionStatus=ruckusPPPOEConnectionStatus, ruckusPPPOEInfo=ruckusPPPOEInfo, ruckusPPPOEConnection=ruckusPPPOEConnection, ruckusPPPOEObjects=ruckusPPPOEObjects, ruckusPPPOEEvents=ruckusPPPOEEvents, ruckusPPPOEIfindex=ruckusPPPOEIfindex, ruckusPPPOEUserName=ruckusPPPOEUserName)
