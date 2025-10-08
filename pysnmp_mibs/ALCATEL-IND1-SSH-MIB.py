#
# PySNMP MIB module ALCATEL-IND1-SSH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/alcatel/ALCATEL-IND1-SSH-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:40:14 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
softentIND1Ssh, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1Ssh")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alcatelIND1SshMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 39, 1))
alcatelIND1SshMIB.setRevisions(('2007-04-03 00:00',))
if mibBuilder.loadTexts: alcatelIND1SshMIB.setLastUpdated('200704030000Z')
if mibBuilder.loadTexts: alcatelIND1SshMIB.setOrganization('Alcatel-Lucent')
alcatelIND1SshMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 39, 1, 1))
if mibBuilder.loadTexts: alcatelIND1SshMIBObjects.setStatus('current')
alcatelIND1SshMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 39, 1, 2))
if mibBuilder.loadTexts: alcatelIND1SshMIBConformance.setStatus('current')
alcatelIND1SshMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 39, 1, 2, 1))
if mibBuilder.loadTexts: alcatelIND1SshMIBGroups.setStatus('current')
alcatelIND1SshMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 39, 1, 2, 2))
if mibBuilder.loadTexts: alcatelIND1SshMIBCompliances.setStatus('current')
alaSshAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 39, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaSshAdminStatus.setStatus('current')
alaScpSftpAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 39, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaScpSftpAdminStatus.setStatus('current')
alaSshPubKeyEnforceAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 39, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaSshPubKeyEnforceAdminStatus.setStatus('current')
alaSshPortNumber = MibScalar((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 39, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaSshPortNumber.setStatus('current')
alcatelIND1SshMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 39, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-SSH-MIB", "alaSshConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1SshMIBCompliance = alcatelIND1SshMIBCompliance.setStatus('current')
alaSshConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 800, 1, 2, 1, 39, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-SSH-MIB", "alaSshAdminStatus"), ("ALCATEL-IND1-SSH-MIB", "alaScpSftpAdminStatus"), ("ALCATEL-IND1-SSH-MIB", "alaSshPubKeyEnforceAdminStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaSshConfigGroup = alaSshConfigGroup.setStatus('current')
mibBuilder.exportSymbols("ALCATEL-IND1-SSH-MIB", alcatelIND1SshMIB=alcatelIND1SshMIB, alaSshPubKeyEnforceAdminStatus=alaSshPubKeyEnforceAdminStatus, alaScpSftpAdminStatus=alaScpSftpAdminStatus, alcatelIND1SshMIBCompliance=alcatelIND1SshMIBCompliance, PYSNMP_MODULE_ID=alcatelIND1SshMIB, alcatelIND1SshMIBCompliances=alcatelIND1SshMIBCompliances, alcatelIND1SshMIBConformance=alcatelIND1SshMIBConformance, alcatelIND1SshMIBGroups=alcatelIND1SshMIBGroups, alaSshPortNumber=alaSshPortNumber, alcatelIND1SshMIBObjects=alcatelIND1SshMIBObjects, alaSshConfigGroup=alaSshConfigGroup, alaSshAdminStatus=alaSshAdminStatus)
