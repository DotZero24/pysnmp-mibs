#
# PySNMP MIB module ALCATEL-IND1-SSH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/alcatel/ALCATEL-IND1-SSH-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 11:07:04 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
softentIND1Ssh, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "softentIND1Ssh")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ALCATEL-IND1-SSH-MIB", PYSNMP_MODULE_ID=alcatelIND1SshMIB, alcatelIND1SshMIB=alcatelIND1SshMIB, alaSshAdminStatus=alaSshAdminStatus, alcatelIND1SshMIBGroups=alcatelIND1SshMIBGroups, alcatelIND1SshMIBObjects=alcatelIND1SshMIBObjects, alcatelIND1SshMIBCompliance=alcatelIND1SshMIBCompliance, alaSshConfigGroup=alaSshConfigGroup, alcatelIND1SshMIBCompliances=alcatelIND1SshMIBCompliances, alaSshPubKeyEnforceAdminStatus=alaSshPubKeyEnforceAdminStatus, alcatelIND1SshMIBConformance=alcatelIND1SshMIBConformance, alaScpSftpAdminStatus=alaScpSftpAdminStatus, alaSshPortNumber=alaSshPortNumber)
