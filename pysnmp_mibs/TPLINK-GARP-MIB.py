#
# PySNMP MIB module TPLINK-GARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/tplink/TPLINK-GARP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:01:28 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
TPRowStatus, = mibBuilder.importSymbols("TPLINK-TC-MIB", "TPRowStatus")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

tplinkGarpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 61))
tplinkGarpMIB.setRevisions(('2014-11-24 14:42',))
if mibBuilder.loadTexts: tplinkGarpMIB.setLastUpdated('201411241442Z')
if mibBuilder.loadTexts: tplinkGarpMIB.setOrganization('TPLINK')
tplinkGarpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 61, 1))
tplinkGarpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 61, 2))
tpGarpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 61, 1, 1))
tpGarpDupIpEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 61, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("Disable", 0), ("Enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpGarpDupIpEnable.setStatus('current')
tpGarpIntfUpEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 61, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("Disable", 0), ("Enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpGarpIntfUpEnable.setStatus('current')
tpGarpLearningEnable = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 61, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("Disable", 0), ("Enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpGarpLearningEnable.setStatus('current')
tpGarpIntfConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 61, 1, 2))
tpGarpIntfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 61, 1, 2, 1), )
if mibBuilder.loadTexts: tpGarpIntfConfigTable.setStatus('current')
tpGarpIntfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 61, 1, 2, 1, 1), ).setIndexNames((0, "TPLINK-GARP-MIB", "tpGarpInterface"))
if mibBuilder.loadTexts: tpGarpIntfConfigEntry.setStatus('current')
tpGarpInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 61, 1, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpGarpInterface.setStatus('current')
tpGarpSendInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 61, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpGarpSendInterval.setStatus('current')
tpGarpIpDuplicate = NotificationType((1, 3, 6, 1, 4, 1, 11863, 6, 61, 2, 1)).setObjects(("TPLINK-GARP-MIB", "tpGarpInterface"))
if mibBuilder.loadTexts: tpGarpIpDuplicate.setStatus('current')
mibBuilder.exportSymbols("TPLINK-GARP-MIB", tpGarpSendInterval=tpGarpSendInterval, tpGarpConfig=tpGarpConfig, tplinkGarpNotifications=tplinkGarpNotifications, tpGarpIntfUpEnable=tpGarpIntfUpEnable, tpGarpLearningEnable=tpGarpLearningEnable, tpGarpIpDuplicate=tpGarpIpDuplicate, PYSNMP_MODULE_ID=tplinkGarpMIB, tpGarpIntfConfig=tpGarpIntfConfig, tpGarpIntfConfigEntry=tpGarpIntfConfigEntry, tpGarpIntfConfigTable=tpGarpIntfConfigTable, tplinkGarpMIBObjects=tplinkGarpMIBObjects, tpGarpDupIpEnable=tpGarpDupIpEnable, MacAddress=MacAddress, tplinkGarpMIB=tplinkGarpMIB, tpGarpInterface=tpGarpInterface)
