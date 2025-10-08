#
# PySNMP MIB module NMS-EPON-ONU-UNI-IF-ACL-APP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/bdcom/NMS-EPON-ONU-UNI-IF-ACL-APP-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:42:11 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
llidIfIndex, = mibBuilder.importSymbols("NMS-EPON-LLID", "llidIfIndex")
nmsEPONGroup, = mibBuilder.importSymbols("NMS-SMI", "nmsEPONGroup")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
RowStatus, PhysAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "PhysAddress", "TextualConvention", "DisplayString")
nmsEponOnuUniIfAppPolicy = MibIdentifier((1, 3, 6, 1, 4, 1, 3320, 101, 105))
nmsEponOnuUniIfAppPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 3320, 101, 105, 1), )
if mibBuilder.loadTexts: nmsEponOnuUniIfAppPolicyTable.setStatus('mandatory')
nmsEponOnuUniIfAppPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3320, 101, 105, 1, 1), ).setIndexNames((0, "NMS-EPON-LLID", "llidIfIndex"), (0, "NMS-EPON-ONU-UNI-IF-ACL-APP-MIB", "nmsOnuUniIfIndex"))
if mibBuilder.loadTexts: nmsEponOnuUniIfAppPolicyEntry.setStatus('mandatory')
llidIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 101, 105, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llidIfIndex.setStatus('mandatory')
nmsOnuUniIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 101, 105, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nmsOnuUniIfIndex.setStatus('mandatory')
nmsOnuUniIfInMacACL = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 101, 105, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsOnuUniIfInMacACL.setStatus('mandatory')
nmsOnuUniIfOutMacACL = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 101, 105, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsOnuUniIfOutMacACL.setStatus('mandatory')
nmsOnuUniIfInIpACL = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 101, 105, 1, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsOnuUniIfInIpACL.setStatus('mandatory')
nmsOnuUniIfOutIpACL = MibTableColumn((1, 3, 6, 1, 4, 1, 3320, 101, 105, 1, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nmsOnuUniIfOutIpACL.setStatus('mandatory')
mibBuilder.exportSymbols("NMS-EPON-ONU-UNI-IF-ACL-APP-MIB", nmsEponOnuUniIfAppPolicyTable=nmsEponOnuUniIfAppPolicyTable, nmsOnuUniIfOutIpACL=nmsOnuUniIfOutIpACL, nmsOnuUniIfOutMacACL=nmsOnuUniIfOutMacACL, nmsOnuUniIfInIpACL=nmsOnuUniIfInIpACL, nmsEponOnuUniIfAppPolicyEntry=nmsEponOnuUniIfAppPolicyEntry, llidIfIndex=llidIfIndex, nmsEponOnuUniIfAppPolicy=nmsEponOnuUniIfAppPolicy, nmsOnuUniIfIndex=nmsOnuUniIfIndex, nmsOnuUniIfInMacACL=nmsOnuUniIfInMacACL)
