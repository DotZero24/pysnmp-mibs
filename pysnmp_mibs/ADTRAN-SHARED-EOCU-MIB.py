#
# PySNMP MIB module ADTRAN-SHARED-EOCU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/adtran/ADTRAN-SHARED-EOCU-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 10:53:31 2025
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
mibBuilder.exportSymbols("ADTRAN-SHARED-EOCU-MIB", adGenTWAMPReflector=adGenTWAMPReflector, adGenEthCfm=adGenEthCfm, adGenTA8xx=adGenTA8xx, adGenOAMID=adGenOAMID, adSLAProbeID=adSLAProbeID, PYSNMP_MODULE_ID=adEoCuIdentity, adEoCu=adEoCu, adGenMEFID=adGenMEFID, adGenTA8xxID=adGenTA8xxID, adSLAProbe=adSLAProbe, adGenTA8xxTlv=adGenTA8xxTlv, adGenEthCfmID=adGenEthCfmID, adGenOAM=adGenOAM, adGenMEF=adGenMEF, adTWAMPReflectorID=adTWAMPReflectorID, adEoCuIdentity=adEoCuIdentity, adGenTA8xxTlvID=adGenTA8xxTlvID)
