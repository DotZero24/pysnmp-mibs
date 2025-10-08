#
# PySNMP MIB module CYCLADES-ACS-ADM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/vertiv/CYCLADES-ACS-ADM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:17:05 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
cyACSMgmt, = mibBuilder.importSymbols("CYCLADES-ACS-MIB", "cyACSMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cyACSAdm = ModuleIdentity((1, 3, 6, 1, 4, 1, 2925, 4, 4))
cyACSAdm.setRevisions(('2005-08-29 00:00', '2002-09-20 00:00',))
if mibBuilder.loadTexts: cyACSAdm.setLastUpdated('200508290000Z')
if mibBuilder.loadTexts: cyACSAdm.setOrganization('Cyclades Corporation')
cyACSSave = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("nosave", 0), ("save", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyACSSave.setStatus('current')
cyACSSerialHUP = MibScalar((1, 3, 6, 1, 4, 1, 2925, 4, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("norestartportslave", 0), ("restartportslave", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cyACSSerialHUP.setStatus('current')
mibBuilder.exportSymbols("CYCLADES-ACS-ADM-MIB", cyACSAdm=cyACSAdm, cyACSSave=cyACSSave, PYSNMP_MODULE_ID=cyACSAdm, cyACSSerialHUP=cyACSSerialHUP)
