#
# PySNMP MIB module CIENA-CES-SSH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/ciena/CIENA-CES-SSH-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:04:10 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cienaCesConfig, = mibBuilder.importSymbols("CIENA-SMI", "cienaCesConfig")
CienaGlobalState, = mibBuilder.importSymbols("CIENA-TC", "CienaGlobalState")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cienaCesSSHMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271, 2, 1, 41))
cienaCesSSHMIB.setRevisions(('2017-06-07 00:00', '2016-08-22 00:00',))
if mibBuilder.loadTexts: cienaCesSSHMIB.setLastUpdated('201706070000Z')
if mibBuilder.loadTexts: cienaCesSSHMIB.setOrganization('Ciena Corp.')
cienaCesSSHMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 41, 1))
cienaCesSSHServerGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 41, 1, 1))
cienaCesSSHServerAdminState = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 41, 1, 1, 1), CienaGlobalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesSSHServerAdminState.setStatus('current')
mibBuilder.exportSymbols("CIENA-CES-SSH-MIB", cienaCesSSHServerGlobal=cienaCesSSHServerGlobal, cienaCesSSHServerAdminState=cienaCesSSHServerAdminState, PYSNMP_MODULE_ID=cienaCesSSHMIB, cienaCesSSHMIB=cienaCesSSHMIB, cienaCesSSHMIBObjects=cienaCesSSHMIBObjects)
