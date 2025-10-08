#
# PySNMP MIB module SFTPServer-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/d-link/SFTPServer-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:33:23 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
swSFTPServerMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 104))
if mibBuilder.loadTexts: swSFTPServerMIB.setLastUpdated('201204230000Z')
if mibBuilder.loadTexts: swSFTPServerMIB.setOrganization('D-Link Corp.')
swSFTPServerMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 104, 1))
swSFTPServerVersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 104, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swSFTPServerVersion.setStatus('current')
swSFTPServerState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 104, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSFTPServerState.setStatus('current')
swSFTPServerConnectionTimeout = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 104, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swSFTPServerConnectionTimeout.setStatus('current')
mibBuilder.exportSymbols("SFTPServer-MIB", swSFTPServerVersion=swSFTPServerVersion, swSFTPServerConnectionTimeout=swSFTPServerConnectionTimeout, swSFTPServerMIB=swSFTPServerMIB, PYSNMP_MODULE_ID=swSFTPServerMIB, swSFTPServerMgmt=swSFTPServerMgmt, swSFTPServerState=swSFTPServerState)
