#
# PySNMP MIB module QTECH-GBNPlatformOAMSsh-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/qtech/QTECH-GBNPlatformOAMSsh-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:13:55 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
gbnPlatformOAM, = mibBuilder.importSymbols("QTECH-GBNPlatformOAM-MIB", "gbnPlatformOAM")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
MibIdentifier, NotificationType, Integer32, Bits, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "MacAddress", "TruthValue", "DisplayString")
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
mibBuilder.exportSymbols("QTECH-GBNPlatformOAMSsh-MIB", sshState=sshState, gbnPlatformOAMSsh=gbnPlatformOAMSsh, PYSNMP_MODULE_ID=gbnPlatformOAMSsh, sshVersion=sshVersion, sshKeyAvailable=sshKeyAvailable)
