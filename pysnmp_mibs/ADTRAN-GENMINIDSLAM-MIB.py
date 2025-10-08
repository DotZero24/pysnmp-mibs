#
# PySNMP MIB module ADTRAN-GENMINIDSLAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/adtran/ADTRAN-GENMINIDSLAM-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:30:04 2025
# On host macmini.vegmond.io platform Darwin version 24.6.0 by user rob
# Using Python version 3.12.8 (main, Dec  3 2024, 18:42:41) [Clang 16.0.0 (clang-1600.0.26.4)]
#
adShared, adIdentityShared = mibBuilder.importSymbols("ADTRAN-MIB", "adShared", "adIdentityShared")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, Gauge32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, NotificationType, MibIdentifier, Integer32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "Gauge32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "NotificationType", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGENMINIDSLAMID = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 61))
if mibBuilder.loadTexts: adGENMINIDSLAMID.setLastUpdated('200710230800Z')
if mibBuilder.loadTexts: adGENMINIDSLAMID.setOrganization('ADTRAN, Inc.')
adGenMiniDslam = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 61))
adTAMiniDslam2g = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 61, 1))
adTAMiniDslam2gmg = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 61, 1, 1))
adGenBondingID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 4))
adTAMiniDslam3gID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 61, 5))
mibBuilder.exportSymbols("ADTRAN-GENMINIDSLAM-MIB", adTAMiniDslam2gmg=adTAMiniDslam2gmg, adGENMINIDSLAMID=adGENMINIDSLAMID, adGenMiniDslam=adGenMiniDslam, PYSNMP_MODULE_ID=adGENMINIDSLAMID, adTAMiniDslam2g=adTAMiniDslam2g, adTAMiniDslam3gID=adTAMiniDslam3gID, adGenBondingID=adGenBondingID)
