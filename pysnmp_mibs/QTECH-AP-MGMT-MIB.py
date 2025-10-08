#
# PySNMP MIB module QTECH-AP-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/qtech/QTECH-AP-MGMT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:14:08 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
qtechMgmt, = mibBuilder.importSymbols("QTECH-SMI", "qtechMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
qtechApMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 124))
qtechApMgmtMIB.setRevisions(('2013-07-23 00:00',))
if mibBuilder.loadTexts: qtechApMgmtMIB.setLastUpdated('201307230000Z')
if mibBuilder.loadTexts: qtechApMgmtMIB.setOrganization('Qtech Networks Co.,Ltd.')
qtechApMgmtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 124, 1))
qtechApMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 124, 1, 1))
qtechApMode = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 124, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qtechApMode.setStatus('current')
mibBuilder.exportSymbols("QTECH-AP-MGMT-MIB", qtechApMode=qtechApMode, qtechApMgmtMIBObjects=qtechApMgmtMIBObjects, qtechApMgmt=qtechApMgmt, PYSNMP_MODULE_ID=qtechApMgmtMIB, qtechApMgmtMIB=qtechApMgmtMIB)
