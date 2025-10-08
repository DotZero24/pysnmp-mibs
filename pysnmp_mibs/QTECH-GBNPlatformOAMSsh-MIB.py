#
# PySNMP MIB module QTECH-GBNPlatformOAMSsh-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/qtech/QTECH-GBNPlatformOAMSsh-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:06:03 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
gbnPlatformOAM, = mibBuilder.importSymbols("QTECH-GBNPlatformOAM-MIB", "gbnPlatformOAM")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
ModuleIdentity, Counter64, Gauge32, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, iso, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "iso", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, MacAddress, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TruthValue", "TextualConvention")
gbnPlatformOAMSsh = ModuleIdentity((1, 3, 6, 1, 4, 1, 27514, 1, 2, 1, 1, 11))
gbnPlatformOAMSsh.setRevisions(('1905-05-25 00:00',))
if mibBuilder.loadTexts: gbnPlatformOAMSsh.setLastUpdated('0505250000Z')
if mibBuilder.loadTexts: gbnPlatformOAMSsh.setOrganization('QTECH LLC')
sshVersion = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 2, 1, 1, 11, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("v1", 1), ("v2", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sshVersion.setStatus('current')
sshState = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 2, 1, 1, 11, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sshState.setStatus('current')
sshKeyAvailable = MibScalar((1, 3, 6, 1, 4, 1, 27514, 1, 2, 1, 1, 11, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("available", 1), ("unavailable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sshKeyAvailable.setStatus('current')
mibBuilder.exportSymbols("QTECH-GBNPlatformOAMSsh-MIB", gbnPlatformOAMSsh=gbnPlatformOAMSsh, sshKeyAvailable=sshKeyAvailable, PYSNMP_MODULE_ID=gbnPlatformOAMSsh, sshVersion=sshVersion, sshState=sshState)
