#
# PySNMP MIB module RBN-BGP-ACCOUNTING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ericsson/RBN-BGP-ACCOUNTING-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:47:17 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
rbnMgmt, = mibBuilder.importSymbols("RBN-SMI", "rbnMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rbnBgpPolAcctMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352, 2, 20))
rbnBgpPolAcctMIB.setRevisions(('2005-09-20 00:00', '2002-03-15 00:00',))
if mibBuilder.loadTexts: rbnBgpPolAcctMIB.setLastUpdated('200203150000Z')
if mibBuilder.loadTexts: rbnBgpPolAcctMIB.setOrganization('RedBack Networks, Inc.')
rbnBgpPolAcctMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 20, 1))
rbnBpaTable = MibTable((1, 3, 6, 1, 4, 1, 2352, 2, 20, 1, 1), )
if mibBuilder.loadTexts: rbnBpaTable.setStatus('current')
rbnBpaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2352, 2, 20, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "RBN-BGP-ACCOUNTING-MIB", "rbnBpaBucketIndex"))
if mibBuilder.loadTexts: rbnBpaEntry.setStatus('current')
rbnBpaBucketIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 20, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnBpaBucketIndex.setStatus('current')
rbnBpaInPacketCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 20, 1, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnBpaInPacketCount.setStatus('current')
rbnBpaInOctetCount = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 20, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnBpaInOctetCount.setStatus('current')
rbnBpaCircuitDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 20, 1, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 192))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnBpaCircuitDescr.setStatus('current')
rbnBpaInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 20, 1, 1, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnBpaInterfaceName.setStatus('current')
rbnBpaContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 2352, 2, 20, 1, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbnBpaContextName.setStatus('current')
rbnBgpPolAcctMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 20, 3))
rbnBgpPolAcctMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 20, 3, 1))
rbnBgpPolAcctMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2352, 2, 20, 3, 2))
rbnBgpPolAcctMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 20, 3, 1, 1)).setObjects(("RBN-BGP-ACCOUNTING-MIB", "rbnBpaTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnBgpPolAcctMIBCompliance = rbnBgpPolAcctMIBCompliance.setStatus('deprecated')
rbnBgpPolAcctMIBCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2352, 2, 20, 3, 1, 2)).setObjects(("RBN-BGP-ACCOUNTING-MIB", "rbnBpaTableGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnBgpPolAcctMIBCompliance1 = rbnBgpPolAcctMIBCompliance1.setStatus('current')
rbnBpaTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 20, 3, 2, 1)).setObjects(("RBN-BGP-ACCOUNTING-MIB", "rbnBpaBucketIndex"), ("RBN-BGP-ACCOUNTING-MIB", "rbnBpaInPacketCount"), ("RBN-BGP-ACCOUNTING-MIB", "rbnBpaInOctetCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnBpaTableGroup = rbnBpaTableGroup.setStatus('deprecated')
rbnBpaTableGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 2352, 2, 20, 3, 2, 2)).setObjects(("RBN-BGP-ACCOUNTING-MIB", "rbnBpaBucketIndex"), ("RBN-BGP-ACCOUNTING-MIB", "rbnBpaInPacketCount"), ("RBN-BGP-ACCOUNTING-MIB", "rbnBpaInOctetCount"), ("RBN-BGP-ACCOUNTING-MIB", "rbnBpaCircuitDescr"), ("RBN-BGP-ACCOUNTING-MIB", "rbnBpaInterfaceName"), ("RBN-BGP-ACCOUNTING-MIB", "rbnBpaContextName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rbnBpaTableGroup1 = rbnBpaTableGroup1.setStatus('current')
mibBuilder.exportSymbols("RBN-BGP-ACCOUNTING-MIB", rbnBpaEntry=rbnBpaEntry, rbnBpaCircuitDescr=rbnBpaCircuitDescr, rbnBpaTableGroup=rbnBpaTableGroup, PYSNMP_MODULE_ID=rbnBgpPolAcctMIB, rbnBpaInOctetCount=rbnBpaInOctetCount, rbnBpaInterfaceName=rbnBpaInterfaceName, rbnBpaContextName=rbnBpaContextName, rbnBgpPolAcctMIBCompliances=rbnBgpPolAcctMIBCompliances, rbnBpaTableGroup1=rbnBpaTableGroup1, rbnBgpPolAcctMIBCompliance=rbnBgpPolAcctMIBCompliance, rbnBpaBucketIndex=rbnBpaBucketIndex, rbnBgpPolAcctMIBConformance=rbnBgpPolAcctMIBConformance, rbnBpaTable=rbnBpaTable, rbnBgpPolAcctMIBGroups=rbnBgpPolAcctMIBGroups, rbnBpaInPacketCount=rbnBpaInPacketCount, rbnBgpPolAcctMIBObjects=rbnBgpPolAcctMIBObjects, rbnBgpPolAcctMIBCompliance1=rbnBgpPolAcctMIBCompliance1, rbnBgpPolAcctMIB=rbnBgpPolAcctMIB)
