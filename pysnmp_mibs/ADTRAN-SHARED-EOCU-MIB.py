#
# PySNMP MIB module ADTRAN-SHARED-EOCU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/code/pysnmp-mibs/mibs/adtran/ADTRAN-SHARED-EOCU-MIB
# Produced by pysmi-1.1.12 at Thu Sep 11 10:30:00 2025
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
adEoCuIdentity = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 69))
adEoCuIdentity.setRevisions(('2007-04-06 00:00',))
if mibBuilder.loadTexts: adEoCuIdentity.setLastUpdated('200704060000Z')
if mibBuilder.loadTexts: adEoCuIdentity.setOrganization('Adtran, Inc.')
adEoCu = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 69))
adGenMEF = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 69, 1))
adGenMEFID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 69, 1))
adGenTA8xx = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 69, 2))
adGenTA8xxID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 69, 2))
adGenOAM = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 69, 3))
adGenOAMID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 69, 3))
adSLAProbe = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 69, 3, 1))
adSLAProbeID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 69, 3, 1))
adGenTA8xxTlv = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 69, 4))
adGenTA8xxTlvID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 69, 4))
adGenTWAMPReflector = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 69, 5))
adTWAMPReflectorID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 69, 5))
adGenEthCfm = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 69, 6))
adGenEthCfmID = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 6, 10000, 69, 6))
mibBuilder.exportSymbols("ADTRAN-SHARED-EOCU-MIB", adGenTWAMPReflector=adGenTWAMPReflector, adGenTA8xx=adGenTA8xx, adGenTA8xxTlv=adGenTA8xxTlv, adGenTA8xxID=adGenTA8xxID, adGenMEF=adGenMEF, PYSNMP_MODULE_ID=adEoCuIdentity, adGenOAMID=adGenOAMID, adGenTA8xxTlvID=adGenTA8xxTlvID, adGenMEFID=adGenMEFID, adGenEthCfmID=adGenEthCfmID, adGenEthCfm=adGenEthCfm, adTWAMPReflectorID=adTWAMPReflectorID, adSLAProbe=adSLAProbe, adEoCu=adEoCu, adGenOAM=adGenOAM, adEoCuIdentity=adEoCuIdentity, adSLAProbeID=adSLAProbeID)
