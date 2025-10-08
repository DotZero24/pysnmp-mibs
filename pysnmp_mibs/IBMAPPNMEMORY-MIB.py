#
# PySNMP MIB module IBMAPPNMEMORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ibm/IBMAPPNMEMORY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:45:40 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("IBMAPPNMEMORY-MIB", ibm=ibm, ibmappnMemoryWarnThresh=ibmappnMemoryWarnThresh, ibmappnMemoryUse=ibmappnMemoryUse, ibmappnMemoryCritThresh=ibmappnMemoryCritThresh, ibmappn=ibmappn, ibmappnMemorySize=ibmappnMemorySize, ibmappnMemoryUsed=ibmappnMemoryUsed, ibmProd=ibmProd, ibm6611=ibm6611, ibmappnNode=ibmappnNode)
