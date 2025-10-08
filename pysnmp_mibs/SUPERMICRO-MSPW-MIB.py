#
# PySNMP MIB module SUPERMICRO-MSPW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/supermicro/SUPERMICRO-MSPW-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:57:35 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
PwIndexType, PwOperStatusTC = mibBuilder.importSymbols("PW-TC-STD-MIB", "PwIndexType", "PwOperStatusTC")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, enterprises, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "enterprises", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("SUPERMICRO-MSPW-MIB", fsMsPwRowStatus=fsMsPwRowStatus, fsMsPwConfigEntry=fsMsPwConfigEntry, fsMsPwConfigTable=fsMsPwConfigTable, PYSNMP_MODULE_ID=fsMspwMIB, fsMsPwIndex1=fsMsPwIndex1, fsMsPwOperStatus=fsMsPwOperStatus, fsMspwMIB=fsMspwMIB, fsMsPwIndex2=fsMsPwIndex2, fsMsPwConfigObjects=fsMsPwConfigObjects, fsMsPwMaxEntries=fsMsPwMaxEntries)
