#
# PySNMP MIB module TPLINK-DDMCONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/tplink/TPLINK-DDMCONFIG-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:26 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplinkDdmManageMIBObjects, = mibBuilder.importSymbols("TPLINK-DDMMANAGE-MIB", "tplinkDdmManageMIBObjects")
ddmConfig = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 1))
ddmConfig.setRevisions(('2009-08-27 00:00',))
if mibBuilder.loadTexts: ddmConfig.setLastUpdated('200908270000Z')
if mibBuilder.loadTexts: ddmConfig.setOrganization('TPLINK')
ddmConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 1, 1), )
if mibBuilder.loadTexts: ddmConfigTable.setStatus('current')
ddmConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ddmConfigEntry.setStatus('current')
ddmConfigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddmConfigPort.setStatus('current')
ddmConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ddmConfigStatus.setStatus('current')
ddmConfigShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("warning", 1), ("alarm", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ddmConfigShutdown.setStatus('current')
ddmConfigPortLAG = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 96, 1, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ddmConfigPortLAG.setStatus('current')
mibBuilder.exportSymbols("TPLINK-DDMCONFIG-MIB", PYSNMP_MODULE_ID=ddmConfig, ddmConfigStatus=ddmConfigStatus, ddmConfigShutdown=ddmConfigShutdown, ddmConfigPortLAG=ddmConfigPortLAG, ddmConfigPort=ddmConfigPort, ddmConfigEntry=ddmConfigEntry, ddmConfig=ddmConfig, ddmConfigTable=ddmConfigTable)
