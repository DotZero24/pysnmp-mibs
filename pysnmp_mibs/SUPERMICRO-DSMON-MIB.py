#
# PySNMP MIB module SUPERMICRO-DSMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/supermicro/SUPERMICRO-DSMON-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 09:56:46 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, enterprises, Unsigned32, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "enterprises", "Unsigned32", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fsdsmon = ModuleIdentity((1, 3, 6, 1, 4, 1, 10876, 101, 3, 4))
fsdsmon.setRevisions(('2012-09-05 00:00',))
if mibBuilder.loadTexts: fsdsmon.setLastUpdated('201209050000Z')
if mibBuilder.loadTexts: fsdsmon.setOrganization('Super Micro Computer Inc.')
fsDsmonTrace = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 3, 4, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsDsmonTrace.setStatus('current')
fsDsmonAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 10876, 101, 3, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: fsDsmonAdminStatus.setStatus('current')
mibBuilder.exportSymbols("SUPERMICRO-DSMON-MIB", fsDsmonTrace=fsDsmonTrace, fsDsmonAdminStatus=fsDsmonAdminStatus, fsdsmon=fsdsmon, PYSNMP_MODULE_ID=fsdsmon)
