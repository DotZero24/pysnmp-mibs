#
# PySNMP MIB module CIENA-CES-SSH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/ciena/CIENA-CES-SSH-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:11:06 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cienaCesConfig, = mibBuilder.importSymbols("CIENA-SMI", "cienaCesConfig")
CienaGlobalState, = mibBuilder.importSymbols("CIENA-TC", "CienaGlobalState")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cienaCesSSHMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271, 2, 1, 41))
cienaCesSSHMIB.setRevisions(('2017-06-07 00:00', '2016-08-22 00:00',))
if mibBuilder.loadTexts: cienaCesSSHMIB.setLastUpdated('201706070000Z')
if mibBuilder.loadTexts: cienaCesSSHMIB.setOrganization('Ciena Corp.')
cienaCesSSHMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 41, 1))
cienaCesSSHServerGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 1271, 2, 1, 41, 1, 1))
cienaCesSSHServerAdminState = MibScalar((1, 3, 6, 1, 4, 1, 1271, 2, 1, 41, 1, 1, 1), CienaGlobalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cienaCesSSHServerAdminState.setStatus('current')
mibBuilder.exportSymbols("CIENA-CES-SSH-MIB", cienaCesSSHServerAdminState=cienaCesSSHServerAdminState, cienaCesSSHMIBObjects=cienaCesSSHMIBObjects, PYSNMP_MODULE_ID=cienaCesSSHMIB, cienaCesSSHServerGlobal=cienaCesSSHServerGlobal, cienaCesSSHMIB=cienaCesSSHMIB)
