#
# PySNMP MIB module ADTRAN-GENMINIDSLAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/adtran/ADTRAN-GENMINIDSLAM-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:53:36 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
adShared, adIdentityShared = mibBuilder.importSymbols("ADTRAN-MIB", "adShared", "adIdentityShared")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
adGENMINIDSLAMID = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 61))
if mibBuilder.loadTexts: adGENMINIDSLAMID.setLastUpdated('200710230800Z')
if mibBuilder.loadTexts: adGENMINIDSLAMID.setOrganization('ADTRAN, Inc.')
adGenMiniDslam = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 61))
adTAMiniDslam2g = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 61, 1))
adTAMiniDslam2gmg = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 61, 1, 1))
adGenBondingID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4))
adTAMiniDslam3gID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5))
mibBuilder.exportSymbols("ADTRAN-GENMINIDSLAM-MIB", adGENMINIDSLAMID=adGENMINIDSLAMID, adTAMiniDslam2gmg=adTAMiniDslam2gmg, adGenBondingID=adGenBondingID, adTAMiniDslam3gID=adTAMiniDslam3gID, PYSNMP_MODULE_ID=adGENMINIDSLAMID, adGenMiniDslam=adGenMiniDslam, adTAMiniDslam2g=adTAMiniDslam2g)
