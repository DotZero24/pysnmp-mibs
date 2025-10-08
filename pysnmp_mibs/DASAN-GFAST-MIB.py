#
# PySNMP MIB module DASAN-GFAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/dasan/DASAN-GFAST-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:00:13 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dasanMgmt, dasanEvents = mibBuilder.importSymbols("DASAN-SMI", "dasanMgmt", "dasanEvents")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, Counter64, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
gFastMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6296, 9, 102))
if mibBuilder.loadTexts: gFastMIB.setLastUpdated('201507210000Z')
if mibBuilder.loadTexts: gFastMIB.setOrganization('Dasan Co., Ltd.')
gFastTestObj1 = MibIdentifier((1, 3, 6, 1, 4, 1, 6296, 9, 102, 1))
gFastTestObj1Temp1 = MibIdentifier((1, 3, 6, 1, 4, 1, 6296, 9, 102, 1, 1))
gFastTestObj1Temp2 = MibIdentifier((1, 3, 6, 1, 4, 1, 6296, 9, 102, 1, 2))
gFastTestObj2 = MibIdentifier((1, 3, 6, 1, 4, 1, 6296, 9, 102, 2))
gFastTestObj2Temp1 = MibIdentifier((1, 3, 6, 1, 4, 1, 6296, 9, 102, 2, 1))
gFastTestObj2Temp1Val1 = MibScalar((1, 3, 6, 1, 4, 1, 6296, 9, 102, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gFastTestObj2Temp1Val1.setStatus('current')
mibBuilder.exportSymbols("DASAN-GFAST-MIB", gFastTestObj2Temp1=gFastTestObj2Temp1, gFastTestObj1=gFastTestObj1, gFastMIB=gFastMIB, gFastTestObj1Temp1=gFastTestObj1Temp1, gFastTestObj2Temp1Val1=gFastTestObj2Temp1Val1, gFastTestObj1Temp2=gFastTestObj1Temp2, PYSNMP_MODULE_ID=gFastMIB, gFastTestObj2=gFastTestObj2)
