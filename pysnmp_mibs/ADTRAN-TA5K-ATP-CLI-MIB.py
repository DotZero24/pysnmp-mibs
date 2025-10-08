#
# PySNMP MIB module ADTRAN-TA5K-ATP-CLI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/adtran/ADTRAN-TA5K-ATP-CLI-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:52:06 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
adGenSlotInfoIndex, = mibBuilder.importSymbols("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex")
adGenTa5kAtpCliID, adGenTa5kAtpCli = mibBuilder.importSymbols("ADTRAN-GENTA5K-MIB", "adGenTa5kAtpCliID", "adGenTa5kAtpCli")
adProducts, adMgmt, adIdentity, adIdentityShared = mibBuilder.importSymbols("ADTRAN-MIB", "adProducts", "adMgmt", "adIdentity", "adIdentityShared")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adTa5kAtpCliModuleIdentity = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 4, 1))
if mibBuilder.loadTexts: adTa5kAtpCliModuleIdentity.setLastUpdated('200605050832Z')
if mibBuilder.loadTexts: adTa5kAtpCliModuleIdentity.setOrganization('ADTRAN, Inc.')
adTa5kAtpCliTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 4, 1), )
if mibBuilder.loadTexts: adTa5kAtpCliTable.setStatus('current')
adTa5kAtpCliEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 4, 1, 1), ).setIndexNames((0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
if mibBuilder.loadTexts: adTa5kAtpCliEntry.setStatus('current')
adTa5kAtpCliCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 4, 1, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adTa5kAtpCliCommand.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-TA5K-ATP-CLI-MIB", PYSNMP_MODULE_ID=adTa5kAtpCliModuleIdentity, adTa5kAtpCliCommand=adTa5kAtpCliCommand, adTa5kAtpCliTable=adTa5kAtpCliTable, adTa5kAtpCliEntry=adTa5kAtpCliEntry, adTa5kAtpCliModuleIdentity=adTa5kAtpCliModuleIdentity)
