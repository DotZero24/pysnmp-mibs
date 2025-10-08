#
# PySNMP MIB module MELLANOX-CONFIG-DB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/mellanox/MELLANOX-CONFIG-DB-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:24:06 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mellanoxConfigDB, = mibBuilder.importSymbols("MELLANOX-SMI-MIB", "mellanoxConfigDB")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mellanoxConfigDBMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 33049, 12, 1))
mellanoxConfigDBMib.setRevisions(('2017-07-25 00:00',))
if mibBuilder.loadTexts: mellanoxConfigDBMib.setLastUpdated('201707250000Z')
if mibBuilder.loadTexts: mellanoxConfigDBMib.setOrganization('Mellanox Technologies, Inc.')
mellanoxConfigDBMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 33049, 12, 1, 1))
mellanoxConfigDBCmd = MibIdentifier((1, 3, 6, 1, 4, 1, 33049, 12, 1, 1, 2))
mellanoxConfigDBCmdUri = MibScalar((1, 3, 6, 1, 4, 1, 33049, 12, 1, 1, 2, 1), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mellanoxConfigDBCmdUri.setStatus('current')
mellanoxConfigDBCmdFilename = MibScalar((1, 3, 6, 1, 4, 1, 33049, 12, 1, 1, 2, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mellanoxConfigDBCmdFilename.setStatus('current')
mellanoxConfigDBCmdExecute = MibScalar((1, 3, 6, 1, 4, 1, 33049, 12, 1, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("mellanoxConfigDBCmdExecuteBinarySwitchTo", 1), ("mellanoxConfigDBCmdExecuteTextApply", 2), ("mellanoxConfigDBCmdExecuteTextApplyFailContinue", 3), ("mellanoxConfigDBCmdExecuteBinaryUpload", 4), ("mellanoxConfigDBCmdExecuteTextUpload", 5), ("mellanoxConfigDBCmdExecuteConfigWrite", 6), ("mellanoxConfigDBCmdExecuteBinaryDelete", 7), ("mellanoxConfigDBCmdExecuteTextDelete", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mellanoxConfigDBCmdExecute.setStatus('current')
mellanoxConfigDBCmdStatus = MibScalar((1, 3, 6, 1, 4, 1, 33049, 12, 1, 1, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mellanoxConfigDBCmdStatus.setStatus('current')
mellanoxConfigDBCmdStatusString = MibScalar((1, 3, 6, 1, 4, 1, 33049, 12, 1, 1, 2, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mellanoxConfigDBCmdStatusString.setStatus('current')
mibBuilder.exportSymbols("MELLANOX-CONFIG-DB-MIB", PYSNMP_MODULE_ID=mellanoxConfigDBMib, mellanoxConfigDBCmdFilename=mellanoxConfigDBCmdFilename, mellanoxConfigDBCmdStatus=mellanoxConfigDBCmdStatus, mellanoxConfigDBCmdExecute=mellanoxConfigDBCmdExecute, mellanoxConfigDBCmdStatusString=mellanoxConfigDBCmdStatusString, mellanoxConfigDBMibObjects=mellanoxConfigDBMibObjects, mellanoxConfigDBMib=mellanoxConfigDBMib, mellanoxConfigDBCmdUri=mellanoxConfigDBCmdUri, mellanoxConfigDBCmd=mellanoxConfigDBCmd)
