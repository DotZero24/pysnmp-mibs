#
# PySNMP MIB module MX-IF-ADMIN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/media5/MX-IF-ADMIN-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:39:19 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mediatrixAdmin, = mibBuilder.importSymbols("MX-SMI", "mediatrixAdmin")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ifAdminMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4935, 5, 8))
ifAdminMIB.setRevisions(('2004-06-10 00:00', '1901-11-28 00:00',))
if mibBuilder.loadTexts: ifAdminMIB.setLastUpdated('200406100000Z')
if mibBuilder.loadTexts: ifAdminMIB.setOrganization('Mediatrix Telecom, Inc.')
ifAdminMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 5, 8, 1))
ifAdminConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 5, 8, 2))
ifAdminTable = MibTable((1, 3, 6, 1, 4, 1, 4935, 5, 8, 1, 10), )
if mibBuilder.loadTexts: ifAdminTable.setStatus('current')
ifAdminEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4935, 5, 8, 1, 10, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ifAdminEntry.setStatus('current')
ifAdminSetAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 5, 8, 1, 10, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noOp", 0), ("permanentUnlock", 1), ("lock", 2), ("forcelock", 3), ("permanentForcelock", 4), ("unlock", 5))).clone('noOp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifAdminSetAdmin.setStatus('current')
ifAdminAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 5, 8, 1, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unlocked", 1), ("shuttingDown", 2), ("locked", 3), ("permanentlock", 4))).clone('unlocked')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifAdminAdminState.setStatus('current')
ifAdminOpState = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 5, 8, 1, 10, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifAdminOpState.setStatus('current')
ifAdminUsageState = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 5, 8, 1, 10, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("idle", 1), ("active", 2), ("busy", 3), ("idle-unusable", 4))).clone('idle-unusable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifAdminUsageState.setStatus('current')
ifAdminParentType = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 5, 8, 1, 10, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("groupAdmin", 1), ("ifAdmin", 2))).clone('groupAdmin')).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifAdminParentType.setStatus('current')
ifAdminParent = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 5, 8, 1, 10, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ifAdminParent.setStatus('current')
ifAdminInitialAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 4935, 5, 8, 1, 10, 1, 65), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unlocked", 1), ("locked", 2))).clone('unlocked')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifAdminInitialAdminState.setStatus('current')
ifAdminCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 5, 8, 2, 1))
ifAdminAnalogPortComplVer1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4935, 5, 8, 2, 1, 1)).setObjects(("MX-IF-ADMIN-MIB", "ifAdminAnalogPortGroupVer1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifAdminAnalogPortComplVer1 = ifAdminAnalogPortComplVer1.setStatus('current')
ifAdminGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4935, 5, 8, 2, 2))
ifAdminAnalogPortGroupVer1 = ObjectGroup((1, 3, 6, 1, 4, 1, 4935, 5, 8, 2, 2, 1)).setObjects(("MX-IF-ADMIN-MIB", "ifAdminSetAdmin"), ("MX-IF-ADMIN-MIB", "ifAdminAdminState"), ("MX-IF-ADMIN-MIB", "ifAdminOpState"), ("MX-IF-ADMIN-MIB", "ifAdminUsageState"), ("MX-IF-ADMIN-MIB", "ifAdminParentType"), ("MX-IF-ADMIN-MIB", "ifAdminParent"), ("MX-IF-ADMIN-MIB", "ifAdminInitialAdminState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ifAdminAnalogPortGroupVer1 = ifAdminAnalogPortGroupVer1.setStatus('current')
mibBuilder.exportSymbols("MX-IF-ADMIN-MIB", ifAdminAdminState=ifAdminAdminState, ifAdminCompliances=ifAdminCompliances, ifAdminSetAdmin=ifAdminSetAdmin, ifAdminParent=ifAdminParent, ifAdminParentType=ifAdminParentType, ifAdminAnalogPortComplVer1=ifAdminAnalogPortComplVer1, ifAdminOpState=ifAdminOpState, ifAdminUsageState=ifAdminUsageState, ifAdminConformance=ifAdminConformance, ifAdminGroups=ifAdminGroups, ifAdminEntry=ifAdminEntry, ifAdminAnalogPortGroupVer1=ifAdminAnalogPortGroupVer1, ifAdminTable=ifAdminTable, ifAdminMIB=ifAdminMIB, ifAdminInitialAdminState=ifAdminInitialAdminState, PYSNMP_MODULE_ID=ifAdminMIB, ifAdminMIBObjects=ifAdminMIBObjects)
