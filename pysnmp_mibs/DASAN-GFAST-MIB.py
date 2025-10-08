#
# PySNMP MIB module DASAN-GFAST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/dasan/DASAN-GFAST-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:03 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dasanEvents, dasanMgmt = mibBuilder.importSymbols("DASAN-SMI", "dasanEvents", "dasanMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Counter32, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Counter32", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("DASAN-GFAST-MIB", gFastTestObj2Temp1Val1=gFastTestObj2Temp1Val1, gFastTestObj2=gFastTestObj2, gFastTestObj1Temp1=gFastTestObj1Temp1, gFastTestObj1=gFastTestObj1, gFastTestObj1Temp2=gFastTestObj1Temp2, gFastTestObj2Temp1=gFastTestObj2Temp1, PYSNMP_MODULE_ID=gFastMIB, gFastMIB=gFastMIB)
