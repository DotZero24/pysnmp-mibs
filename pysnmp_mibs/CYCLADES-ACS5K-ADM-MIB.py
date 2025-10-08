#
# PySNMP MIB module CYCLADES-ACS5K-ADM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/vertiv/CYCLADES-ACS5K-ADM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:07:50 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cyACS5KMgmt, = mibBuilder.importSymbols("CYCLADES-ACS5K-MIB", "cyACS5KMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cyACS5KAdm = ModuleIdentity((1, 3, 6, 1, 4, 1, 2925, 8, 4))
cyACS5KAdm.setRevisions(('2010-07-26 00:00',))
if mibBuilder.loadTexts: cyACS5KAdm.setLastUpdated('201007260000Z')
if mibBuilder.loadTexts: cyACS5KAdm.setOrganization('Avocent Corporation')
cyACS5KSave = MibScalar((1, 3, 6, 1, 4, 1, 2925, 8, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("nosave", 0), ("save", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyACS5KSave.setStatus('current')
cyACS5KSerialHUP = MibScalar((1, 3, 6, 1, 4, 1, 2925, 8, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("norestartportslave", 0), ("restartportslave", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyACS5KSerialHUP.setStatus('current')
mibBuilder.exportSymbols("CYCLADES-ACS5K-ADM-MIB", cyACS5KAdm=cyACS5KAdm, PYSNMP_MODULE_ID=cyACS5KAdm, cyACS5KSerialHUP=cyACS5KSerialHUP, cyACS5KSave=cyACS5KSave)
