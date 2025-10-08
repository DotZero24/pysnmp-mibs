#
# PySNMP MIB module TPLINK-IPV6-SOURCE-GUARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/tplink/TPLINK-IPV6-SOURCE-GUARD-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:36:21 2025
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
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkIpv6SourceGuardMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 94))
tplinkIpv6SourceGuardMIB.setRevisions(('2012-12-13 09:30',))
if mibBuilder.loadTexts: tplinkIpv6SourceGuardMIB.setLastUpdated('201212130930Z')
if mibBuilder.loadTexts: tplinkIpv6SourceGuardMIB.setOrganization('TPLINK')
tplinkIpv6SourceGuardMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 94, 1))
tplinkIpv6SourceGuardNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 94, 2))
tpIpv6SourceGuardConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 94, 1, 1))
tpIpv6SourceGuardConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11863, 6, 94, 1, 1, 1), )
if mibBuilder.loadTexts: tpIpv6SourceGuardConfigTable.setStatus('current')
tpIpv6SourceGuardConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11863, 6, 94, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: tpIpv6SourceGuardConfigEntry.setStatus('current')
tpIpv6SourceGuardConfigPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 94, 1, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIpv6SourceGuardConfigPort.setStatus('current')
tpIpv6SourceGuardConfigType = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 94, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 0, 2))).clone(namedValues=NamedValues(("disable", 0), ("sipv6", 0), ("sipv6-mac", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tpIpv6SourceGuardConfigType.setStatus('current')
tpIpv6SourceGuardConfigPortLag = MibTableColumn((1, 3, 6, 1, 4, 1, 11863, 6, 94, 1, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tpIpv6SourceGuardConfigPortLag.setStatus('current')
mibBuilder.exportSymbols("TPLINK-IPV6-SOURCE-GUARD-MIB", tpIpv6SourceGuardConfig=tpIpv6SourceGuardConfig, tpIpv6SourceGuardConfigTable=tpIpv6SourceGuardConfigTable, tpIpv6SourceGuardConfigPortLag=tpIpv6SourceGuardConfigPortLag, tpIpv6SourceGuardConfigEntry=tpIpv6SourceGuardConfigEntry, tpIpv6SourceGuardConfigPort=tpIpv6SourceGuardConfigPort, PYSNMP_MODULE_ID=tplinkIpv6SourceGuardMIB, tpIpv6SourceGuardConfigType=tpIpv6SourceGuardConfigType, tplinkIpv6SourceGuardMIB=tplinkIpv6SourceGuardMIB, tplinkIpv6SourceGuardNotifications=tplinkIpv6SourceGuardNotifications, tplinkIpv6SourceGuardMIBObjects=tplinkIpv6SourceGuardMIBObjects)
