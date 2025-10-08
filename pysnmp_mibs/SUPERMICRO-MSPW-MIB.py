#
# PySNMP MIB module SUPERMICRO-MSPW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/supermicro/SUPERMICRO-MSPW-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:48 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
PwOperStatusTC, PwIndexType = mibBuilder.importSymbols("PW-TC-STD-MIB", "PwOperStatusTC", "PwIndexType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
fsMspwMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 10876, 101, 2, 57))
fsMspwMIB.setRevisions(('2012-09-05 00:00',))
if mibBuilder.loadTexts: fsMspwMIB.setLastUpdated('201209050000Z')
if mibBuilder.loadTexts: fsMspwMIB.setOrganization('Super Micro Computer Inc.')
fsMsPwConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 10876, 101, 2, 57, 1))
fsMsPwMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 2, 57, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 32766)).clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsMsPwMaxEntries.setStatus('current')
fsMsPwConfigTable = MibTable((1, 3, 6, 1, 4, 1, 10876, 101, 2, 57, 1, 2), )
if mibBuilder.loadTexts: fsMsPwConfigTable.setStatus('current')
fsMsPwConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 10876, 101, 2, 57, 1, 2, 1), ).setIndexNames((0, "SUPERMICRO-MSPW-MIB", "fsMsPwIndex1"), (0, "SUPERMICRO-MSPW-MIB", "fsMsPwIndex2"))
if mibBuilder.loadTexts: fsMsPwConfigEntry.setStatus('current')
fsMsPwIndex1 = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 101, 2, 57, 1, 2, 1, 1), PwIndexType())
if mibBuilder.loadTexts: fsMsPwIndex1.setStatus('current')
fsMsPwIndex2 = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 101, 2, 57, 1, 2, 1, 2), PwIndexType())
if mibBuilder.loadTexts: fsMsPwIndex2.setStatus('current')
fsMsPwOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 101, 2, 57, 1, 2, 1, 3), PwOperStatusTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: fsMsPwOperStatus.setStatus('current')
fsMsPwRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 10876, 101, 2, 57, 1, 2, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsMsPwRowStatus.setStatus('current')
mibBuilder.exportSymbols("SUPERMICRO-MSPW-MIB", fsMsPwIndex1=fsMsPwIndex1, fsMsPwConfigEntry=fsMsPwConfigEntry, fsMsPwIndex2=fsMsPwIndex2, fsMsPwMaxEntries=fsMsPwMaxEntries, fsMsPwOperStatus=fsMsPwOperStatus, fsMsPwConfigObjects=fsMsPwConfigObjects, fsMspwMIB=fsMspwMIB, fsMsPwConfigTable=fsMsPwConfigTable, fsMsPwRowStatus=fsMsPwRowStatus, PYSNMP_MODULE_ID=fsMspwMIB)
