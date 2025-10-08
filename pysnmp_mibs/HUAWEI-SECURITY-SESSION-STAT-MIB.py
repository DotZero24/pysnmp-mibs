#
# PySNMP MIB module HUAWEI-SECURITY-SESSION-STAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/huawei/HUAWEI-SECURITY-SESSION-STAT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:01:47 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hwSecSessStatMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 6, 122, 69))
if mibBuilder.loadTexts: hwSecSessStatMIB.setLastUpdated('201404090000Z')
if mibBuilder.loadTexts: hwSecSessStatMIB.setOrganization('Huawei Technologies co.,Ltd.')
huawei = MibIdentifier((1, 3, 6, 1, 4, 1, 2011))
huaweiUtility = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6))
hwSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 122))
hwSecSessStatTable = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 122, 69, 1))
hwSecSessStatEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 6, 122, 69, 1, 1))
hwSecCurrSessThreshold = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 122, 69, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSecCurrSessThreshold.setStatus('current')
hwSecCurrSessNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 122, 69, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSecCurrSessNum.setStatus('current')
hwSecConSessThreshold = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 122, 69, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSecConSessThreshold.setStatus('current')
hwSecConSessNum = MibScalar((1, 3, 6, 1, 4, 1, 2011, 6, 122, 69, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwSecConSessNum.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-SECURITY-SESSION-STAT-MIB", hwSecSessStatTable=hwSecSessStatTable, hwSecConSessThreshold=hwSecConSessThreshold, hwSecSessStatEntry=hwSecSessStatEntry, hwSecurity=hwSecurity, hwSecSessStatMIB=hwSecSessStatMIB, hwSecConSessNum=hwSecConSessNum, huaweiUtility=huaweiUtility, PYSNMP_MODULE_ID=hwSecSessStatMIB, huawei=huawei, hwSecCurrSessThreshold=hwSecCurrSessThreshold, hwSecCurrSessNum=hwSecCurrSessNum)
