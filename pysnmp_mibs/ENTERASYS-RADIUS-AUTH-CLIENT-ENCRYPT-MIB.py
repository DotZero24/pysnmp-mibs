#
# PySNMP MIB module ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/enterasys/ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:34:00 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("ENTERASYS-RADIUS-AUTH-CLIENT-ENCRYPT-MIB", etsysRadiusAuthClientServerStatusEncrypt=etsysRadiusAuthClientServerStatusEncrypt, etsysRadiusAuthClientAuthTypeEncrypt=etsysRadiusAuthClientAuthTypeEncrypt, etsysRadiusAuthClientManageAuthKeyEncrypt=etsysRadiusAuthClientManageAuthKeyEncrypt, etsysRadiusAuthClientEncryptMIB=etsysRadiusAuthClientEncryptMIB, etsysRadiusAuthClientRetriesEncrypt=etsysRadiusAuthClientRetriesEncrypt, etsysRadiusAuthServerEncryptTable=etsysRadiusAuthServerEncryptTable, etsysRadiusAuthClientServerSecretEnteredEncrypt=etsysRadiusAuthClientServerSecretEnteredEncrypt, etsysRadiusAuthClientServerSecretEncrypt=etsysRadiusAuthClientServerSecretEncrypt, etsysRadiusAuthServerEncryptEntry=etsysRadiusAuthServerEncryptEntry, etsysRadiusAuthClientEncryptMIBGroup=etsysRadiusAuthClientEncryptMIBGroup, RadiusEncryptedString=RadiusEncryptedString, PYSNMP_MODULE_ID=etsysRadiusAuthClientEncryptMIB, etsysRadiusAuthClientRetryTimeoutEncrypt=etsysRadiusAuthClientRetryTimeoutEncrypt, etsysRadiusClientEncryptMIBCompliance=etsysRadiusClientEncryptMIBCompliance, etsysRadiusAuthServerIndexEncrypt=etsysRadiusAuthServerIndexEncrypt, etsysRadiusAuthClientServerAddressEncrypt=etsysRadiusAuthClientServerAddressEncrypt, etsysRadiusAuthClientEncryptMIBGroups=etsysRadiusAuthClientEncryptMIBGroups, etsysRadiusAuthClientEncryptMIBCompliances=etsysRadiusAuthClientEncryptMIBCompliances, etsysRadiusAuthClientServerPortNumberEncrypt=etsysRadiusAuthClientServerPortNumberEncrypt, etsysRadiusAuthClientEnableEncrypt=etsysRadiusAuthClientEnableEncrypt, etsysRadiusAuthClientServerClearTimeEncrypt=etsysRadiusAuthClientServerClearTimeEncrypt, etsysRadiusAuthClientEncryptMIBObjects=etsysRadiusAuthClientEncryptMIBObjects, etsysRadiusAuthClientEncryptMIBConformance=etsysRadiusAuthClientEncryptMIBConformance)
