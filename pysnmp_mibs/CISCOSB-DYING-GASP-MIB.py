#
# PySNMP MIB module CISCOSB-DYING-GASP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ciscosb/CISCOSB-DYING-GASP-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:32:19 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
rlDyGsp = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 245))
rlDyGsp.setRevisions(('2009-11-26 00:00',))
if mibBuilder.loadTexts: rlDyGsp.setLastUpdated('202104100000Z')
if mibBuilder.loadTexts: rlDyGsp.setOrganization('Cisco Systems, Inc.')
rlDyGspModeConfig = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 245, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("syslogPrimary-snmpSecondary", 1), ("snmpPrimary-syslogSecondary", 2), ("syslogPrimary-NoSecondary", 3), ("snmpPrimary-NoSecondary", 4), ("disabled", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlDyGspModeConfig.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-DYING-GASP-MIB", rlDyGsp=rlDyGsp, PYSNMP_MODULE_ID=rlDyGsp, rlDyGspModeConfig=rlDyGspModeConfig)
