#
# PySNMP MIB module SFTPServer-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/d-link/SFTPServer-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:57:51 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("SFTPServer-MIB", swSFTPServerMIB=swSFTPServerMIB, PYSNMP_MODULE_ID=swSFTPServerMIB, swSFTPServerState=swSFTPServerState, swSFTPServerConnectionTimeout=swSFTPServerConnectionTimeout, swSFTPServerVersion=swSFTPServerVersion, swSFTPServerMgmt=swSFTPServerMgmt)
