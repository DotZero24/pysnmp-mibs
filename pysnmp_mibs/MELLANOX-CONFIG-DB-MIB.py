#
# PySNMP MIB module MELLANOX-CONFIG-DB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/mellanox/MELLANOX-CONFIG-DB-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:44:46 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
mellanoxConfigDB, = mibBuilder.importSymbols("MELLANOX-SMI-MIB", "mellanoxConfigDB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("MELLANOX-CONFIG-DB-MIB", mellanoxConfigDBCmdStatus=mellanoxConfigDBCmdStatus, mellanoxConfigDBCmdUri=mellanoxConfigDBCmdUri, PYSNMP_MODULE_ID=mellanoxConfigDBMib, mellanoxConfigDBCmd=mellanoxConfigDBCmd, mellanoxConfigDBCmdStatusString=mellanoxConfigDBCmdStatusString, mellanoxConfigDBCmdFilename=mellanoxConfigDBCmdFilename, mellanoxConfigDBCmdExecute=mellanoxConfigDBCmdExecute, mellanoxConfigDBMibObjects=mellanoxConfigDBMibObjects, mellanoxConfigDBMib=mellanoxConfigDBMib)
