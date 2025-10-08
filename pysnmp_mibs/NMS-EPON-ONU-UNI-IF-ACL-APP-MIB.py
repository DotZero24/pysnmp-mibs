#
# PySNMP MIB module NMS-EPON-ONU-UNI-IF-ACL-APP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/bdcom/NMS-EPON-ONU-UNI-IF-ACL-APP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:22:47 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
llidIfIndex, = mibBuilder.importSymbols("NMS-EPON-LLID", "llidIfIndex")
nmsEPONGroup, = mibBuilder.importSymbols("NMS-SMI", "nmsEPONGroup")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "PhysAddress")
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
mibBuilder.exportSymbols("NMS-EPON-ONU-UNI-IF-ACL-APP-MIB", nmsOnuUniIfOutIpACL=nmsOnuUniIfOutIpACL, nmsOnuUniIfInIpACL=nmsOnuUniIfInIpACL, nmsOnuUniIfInMacACL=nmsOnuUniIfInMacACL, nmsOnuUniIfOutMacACL=nmsOnuUniIfOutMacACL, llidIfIndex=llidIfIndex, nmsEponOnuUniIfAppPolicyTable=nmsEponOnuUniIfAppPolicyTable, nmsOnuUniIfIndex=nmsOnuUniIfIndex, nmsEponOnuUniIfAppPolicy=nmsEponOnuUniIfAppPolicy, nmsEponOnuUniIfAppPolicyEntry=nmsEponOnuUniIfAppPolicyEntry)
