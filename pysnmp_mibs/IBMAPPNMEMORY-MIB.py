#
# PySNMP MIB module IBMAPPNMEMORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ibm/IBMAPPNMEMORY-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:24:41 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmProd = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6))
ibm6611 = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 2))
ibmappn = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 2, 13))
ibmappnNode = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1))
ibmappnMemoryUse = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 7))
ibmappnMemorySize = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 7, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmappnMemorySize.setStatus('mandatory')
ibmappnMemoryUsed = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 7, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmappnMemoryUsed.setStatus('mandatory')
ibmappnMemoryWarnThresh = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 7, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmappnMemoryWarnThresh.setStatus('mandatory')
ibmappnMemoryCritThresh = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 7, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmappnMemoryCritThresh.setStatus('mandatory')
mibBuilder.exportSymbols("IBMAPPNMEMORY-MIB", ibmProd=ibmProd, ibmappnMemoryUse=ibmappnMemoryUse, ibmappn=ibmappn, ibm6611=ibm6611, ibmappnMemoryUsed=ibmappnMemoryUsed, ibmappnMemoryCritThresh=ibmappnMemoryCritThresh, ibmappnMemoryWarnThresh=ibmappnMemoryWarnThresh, ibm=ibm, ibmappnNode=ibmappnNode, ibmappnMemorySize=ibmappnMemorySize)
