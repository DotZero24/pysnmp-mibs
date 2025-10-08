#
# PySNMP MIB module ADTRAN-TA5K-ATP-CLI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/adtran/ADTRAN-TA5K-ATP-CLI-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:29:03 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
adGenSlotInfoIndex, = mibBuilder.importSymbols("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex")
adGenTa5kAtpCli, adGenTa5kAtpCliID = mibBuilder.importSymbols("ADTRAN-GENTA5K-MIB", "adGenTa5kAtpCli", "adGenTa5kAtpCliID")
adMgmt, adIdentityShared, adProducts, adIdentity = mibBuilder.importSymbols("ADTRAN-MIB", "adMgmt", "adIdentityShared", "adProducts", "adIdentity")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adTa5kAtpCliModuleIdentity = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 4, 1))
if mibBuilder.loadTexts: adTa5kAtpCliModuleIdentity.setLastUpdated('200605050832Z')
if mibBuilder.loadTexts: adTa5kAtpCliModuleIdentity.setOrganization('ADTRAN, Inc.')
adTa5kAtpCliTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 4, 1), )
if mibBuilder.loadTexts: adTa5kAtpCliTable.setStatus('current')
adTa5kAtpCliEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 4, 1, 1), ).setIndexNames((0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
if mibBuilder.loadTexts: adTa5kAtpCliEntry.setStatus('current')
adTa5kAtpCliCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 4, 1, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adTa5kAtpCliCommand.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-TA5K-ATP-CLI-MIB", PYSNMP_MODULE_ID=adTa5kAtpCliModuleIdentity, adTa5kAtpCliModuleIdentity=adTa5kAtpCliModuleIdentity, adTa5kAtpCliTable=adTa5kAtpCliTable, adTa5kAtpCliEntry=adTa5kAtpCliEntry, adTa5kAtpCliCommand=adTa5kAtpCliCommand)
