#
# PySNMP MIB module ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/enterasys/ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:17:25 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
etsysRadiusAuthClientEncryptMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 5))
etsysRadiusAuthClientEncryptMIB.setRevisions(('2002-11-11 15:56', '2002-01-24 16:06', '2000-11-08 00:00',))
if mibBuilder.loadTexts: etsysRadiusAuthClientEncryptMIB.setLastUpdated('200211111556Z')
if mibBuilder.loadTexts: etsysRadiusAuthClientEncryptMIB.setOrganization('Enterasys Networks')
class RadiusEncryptedString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

etsysRadiusAuthClientEncryptMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1))
etsysRadiusAuthClientRetryTimeoutEncrypt = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 1), RadiusEncryptedString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysRadiusAuthClientRetryTimeoutEncrypt.setStatus('obsolete')
etsysRadiusAuthClientRetriesEncrypt = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 2), RadiusEncryptedString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysRadiusAuthClientRetriesEncrypt.setStatus('obsolete')
etsysRadiusAuthClientEnableEncrypt = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 3), RadiusEncryptedString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysRadiusAuthClientEnableEncrypt.setStatus('obsolete')
etsysRadiusAuthClientAuthTypeEncrypt = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 4), RadiusEncryptedString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysRadiusAuthClientAuthTypeEncrypt.setStatus('obsolete')
etsysRadiusAuthClientManageAuthKeyEncrypt = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 5), RadiusEncryptedString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysRadiusAuthClientManageAuthKeyEncrypt.setStatus('obsolete')
etsysRadiusAuthServerEncryptTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 6), )
if mibBuilder.loadTexts: etsysRadiusAuthServerEncryptTable.setStatus('obsolete')
etsysRadiusAuthServerEncryptEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 6, 1), ).setIndexNames((0, "ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", "etsysRadiusAuthServerIndexEncrypt"))
if mibBuilder.loadTexts: etsysRadiusAuthServerEncryptEntry.setStatus('obsolete')
etsysRadiusAuthServerIndexEncrypt = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: etsysRadiusAuthServerIndexEncrypt.setStatus('obsolete')
etsysRadiusAuthClientServerAddressEncrypt = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 6, 1, 2), RadiusEncryptedString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysRadiusAuthClientServerAddressEncrypt.setStatus('obsolete')
etsysRadiusAuthClientServerPortNumberEncrypt = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 6, 1, 3), RadiusEncryptedString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysRadiusAuthClientServerPortNumberEncrypt.setStatus('obsolete')
etsysRadiusAuthClientServerSecretEncrypt = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 6, 1, 4), RadiusEncryptedString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysRadiusAuthClientServerSecretEncrypt.setStatus('obsolete')
etsysRadiusAuthClientServerSecretEnteredEncrypt = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 6, 1, 5), RadiusEncryptedString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysRadiusAuthClientServerSecretEnteredEncrypt.setStatus('obsolete')
etsysRadiusAuthClientServerClearTimeEncrypt = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 6, 1, 6), RadiusEncryptedString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysRadiusAuthClientServerClearTimeEncrypt.setStatus('obsolete')
etsysRadiusAuthClientServerStatusEncrypt = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 1, 6, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysRadiusAuthClientServerStatusEncrypt.setStatus('obsolete')
etsysRadiusAuthClientEncryptMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 2))
etsysRadiusAuthClientEncryptMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 2, 1))
etsysRadiusAuthClientEncryptMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 2, 2))
etsysRadiusAuthClientEncryptMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 2, 2, 1)).setObjects(("ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", "etsysRadiusAuthClientRetryTimeoutEncrypt"), ("ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", "etsysRadiusAuthClientRetriesEncrypt"), ("ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", "etsysRadiusAuthClientEnableEncrypt"), ("ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", "etsysRadiusAuthClientAuthTypeEncrypt"), ("ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", "etsysRadiusAuthClientManageAuthKeyEncrypt"), ("ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", "etsysRadiusAuthClientServerAddressEncrypt"), ("ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", "etsysRadiusAuthClientServerPortNumberEncrypt"), ("ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", "etsysRadiusAuthClientServerSecretEncrypt"), ("ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", "etsysRadiusAuthClientServerSecretEnteredEncrypt"), ("ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", "etsysRadiusAuthClientServerClearTimeEncrypt"), ("ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", "etsysRadiusAuthClientServerStatusEncrypt"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRadiusAuthClientEncryptMIBGroup = etsysRadiusAuthClientEncryptMIBGroup.setStatus('obsolete')
etsysRadiusClientEncryptMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 5, 2, 1, 1)).setObjects(("ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", "etsysRadiusAuthClientEncryptMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRadiusClientEncryptMIBCompliance = etsysRadiusClientEncryptMIBCompliance.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", etsysRadiusAuthClientRetriesEncrypt=etsysRadiusAuthClientRetriesEncrypt, etsysRadiusClientEncryptMIBCompliance=etsysRadiusClientEncryptMIBCompliance, etsysRadiusAuthServerIndexEncrypt=etsysRadiusAuthServerIndexEncrypt, etsysRadiusAuthClientEnableEncrypt=etsysRadiusAuthClientEnableEncrypt, PYSNMP_MODULE_ID=etsysRadiusAuthClientEncryptMIB, etsysRadiusAuthClientManageAuthKeyEncrypt=etsysRadiusAuthClientManageAuthKeyEncrypt, etsysRadiusAuthClientEncryptMIBCompliances=etsysRadiusAuthClientEncryptMIBCompliances, etsysRadiusAuthClientServerAddressEncrypt=etsysRadiusAuthClientServerAddressEncrypt, etsysRadiusAuthClientEncryptMIBObjects=etsysRadiusAuthClientEncryptMIBObjects, etsysRadiusAuthClientServerSecretEnteredEncrypt=etsysRadiusAuthClientServerSecretEnteredEncrypt, etsysRadiusAuthClientAuthTypeEncrypt=etsysRadiusAuthClientAuthTypeEncrypt, etsysRadiusAuthClientEncryptMIBGroup=etsysRadiusAuthClientEncryptMIBGroup, etsysRadiusAuthServerEncryptTable=etsysRadiusAuthServerEncryptTable, etsysRadiusAuthClientServerStatusEncrypt=etsysRadiusAuthClientServerStatusEncrypt, etsysRadiusAuthClientEncryptMIBGroups=etsysRadiusAuthClientEncryptMIBGroups, RadiusEncryptedString=RadiusEncryptedString, etsysRadiusAuthServerEncryptEntry=etsysRadiusAuthServerEncryptEntry, etsysRadiusAuthClientEncryptMIBConformance=etsysRadiusAuthClientEncryptMIBConformance, etsysRadiusAuthClientServerClearTimeEncrypt=etsysRadiusAuthClientServerClearTimeEncrypt, etsysRadiusAuthClientServerPortNumberEncrypt=etsysRadiusAuthClientServerPortNumberEncrypt, etsysRadiusAuthClientServerSecretEncrypt=etsysRadiusAuthClientServerSecretEncrypt, etsysRadiusAuthClientRetryTimeoutEncrypt=etsysRadiusAuthClientRetryTimeoutEncrypt, etsysRadiusAuthClientEncryptMIB=etsysRadiusAuthClientEncryptMIB)
