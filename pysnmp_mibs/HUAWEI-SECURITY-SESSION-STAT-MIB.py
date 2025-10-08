#
# PySNMP MIB module HUAWEI-SECURITY-SESSION-STAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/huawei/HUAWEI-SECURITY-SESSION-STAT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:07:10 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("HUAWEI-SECURITY-SESSION-STAT-MIB", hwSecurity=hwSecurity, PYSNMP_MODULE_ID=hwSecSessStatMIB, hwSecSessStatTable=hwSecSessStatTable, hwSecSessStatEntry=hwSecSessStatEntry, hwSecCurrSessNum=hwSecCurrSessNum, hwSecSessStatMIB=hwSecSessStatMIB, hwSecConSessNum=hwSecConSessNum, huaweiUtility=huaweiUtility, hwSecCurrSessThreshold=hwSecCurrSessThreshold, hwSecConSessThreshold=hwSecConSessThreshold, huawei=huawei)
