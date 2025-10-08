#
# PySNMP MIB module FS-AP-MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/fscom/FS-AP-MGMT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:58:15 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fsMgmt, = mibBuilder.importSymbols("FS-SMI", "fsMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fsApMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 124))
fsApMgmtMIB.setRevisions(('2013-07-23 00:00',))
if mibBuilder.loadTexts: fsApMgmtMIB.setLastUpdated('201307230000Z')
if mibBuilder.loadTexts: fsApMgmtMIB.setOrganization('FS.COM Inc..')
fsApMgmtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 124, 1))
fsApMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 124, 1, 1))
fsApMode = MibScalar((1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 124, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsApMode.setStatus('current')
mibBuilder.exportSymbols("FS-AP-MGMT-MIB", fsApMgmtMIBObjects=fsApMgmtMIBObjects, fsApMode=fsApMode, fsApMgmt=fsApMgmt, fsApMgmtMIB=fsApMgmtMIB, PYSNMP_MODULE_ID=fsApMgmtMIB)
