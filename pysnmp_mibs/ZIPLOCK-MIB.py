#
# PySNMP MIB module ZIPLOCK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/cabletron/ZIPLOCK-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:13:50 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ctResource, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctResource")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, Counter64, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "Counter64", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctZiplock = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3))
ctZiplockTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1), )
if mibBuilder.loadTexts: ctZiplockTable.setStatus('mandatory')
ctZiplockEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1, 1), ).setIndexNames((0, "ZIPLOCK-MIB", "ctZiplockNumber"))
if mibBuilder.loadTexts: ctZiplockEntry.setStatus('mandatory')
ctZiplockNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctZiplockNumber.setStatus('mandatory')
ctZiplockPresence = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctZiplockPresence.setStatus('mandatory')
ctZiplockRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctZiplockRevision.setStatus('mandatory')
ctZiplockStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctZiplockStatus.setStatus('mandatory')
mibBuilder.exportSymbols("ZIPLOCK-MIB", ctZiplockTable=ctZiplockTable, ctZiplockRevision=ctZiplockRevision, ctZiplock=ctZiplock, ctZiplockPresence=ctZiplockPresence, ctZiplockEntry=ctZiplockEntry, ctZiplockStatus=ctZiplockStatus, ctZiplockNumber=ctZiplockNumber)
