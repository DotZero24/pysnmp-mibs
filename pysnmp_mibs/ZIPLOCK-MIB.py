#
# PySNMP MIB module ZIPLOCK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/cabletron/ZIPLOCK-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:05:59 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ctResource, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctResource")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ZIPLOCK-MIB", ctZiplockTable=ctZiplockTable, ctZiplockRevision=ctZiplockRevision, ctZiplockPresence=ctZiplockPresence, ctZiplockNumber=ctZiplockNumber, ctZiplockEntry=ctZiplockEntry, ctZiplock=ctZiplock, ctZiplockStatus=ctZiplockStatus)
