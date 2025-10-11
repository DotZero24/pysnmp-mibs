# SNMP MIB module (ARRIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/arris/ARRIS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:10:51 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

arris = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115)
)
if mibBuilder.loadTexts:
    arris.setRevisions(
        ("2011-01-14 00:00",
         "2011-01-13 00:00",
         "2010-02-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArrisProducts_ObjectIdentity = ObjectIdentity
arrisProducts = _ArrisProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1)
)
_Packetport_ObjectIdentity = ObjectIdentity
packetport = _Packetport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 1)
)
_Cm110_ObjectIdentity = ObjectIdentity
cm110 = _Cm110_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 2)
)
_ArrisProdIdCM_ObjectIdentity = ObjectIdentity
arrisProdIdCM = _ArrisProdIdCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3)
)
_ArrisMtaDevMib_ObjectIdentity = ObjectIdentity
arrisMtaDevMib = _ArrisMtaDevMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 3)
)
_ArrisCmDoc30Mib_ObjectIdentity = ObjectIdentity
arrisCmDoc30Mib = _ArrisCmDoc30Mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 4)
)
_ArrisMtaDoc30Mib_ObjectIdentity = ObjectIdentity
arrisMtaDoc30Mib = _ArrisMtaDoc30Mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 5)
)
_ArrisSpeedTestMib_ObjectIdentity = ObjectIdentity
arrisSpeedTestMib = _ArrisSpeedTestMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 6)
)
_ArrisTR69Mib_ObjectIdentity = ObjectIdentity
arrisTR69Mib = _ArrisTR69Mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 7)
)
_Tcm_ObjectIdentity = ObjectIdentity
tcm = _Tcm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 8)
)
_Ttm_ObjectIdentity = ObjectIdentity
ttm = _Ttm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 9)
)
_Ttp_ObjectIdentity = ObjectIdentity
ttp = _Ttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 10)
)
_ArrisQamDetectionMib_ObjectIdentity = ObjectIdentity
arrisQamDetectionMib = _ArrisQamDetectionMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 12)
)
_ArrisNetPerfMonitorMib_ObjectIdentity = ObjectIdentity
arrisNetPerfMonitorMib = _ArrisNetPerfMonitorMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 13)
)
_ArrisKddiFeatMib_ObjectIdentity = ObjectIdentity
arrisKddiFeatMib = _ArrisKddiFeatMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 14)
)
_ArrisDectMib_ObjectIdentity = ObjectIdentity
arrisDectMib = _ArrisDectMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 15)
)
_ArrisHorizOvertempProtModeMib_ObjectIdentity = ObjectIdentity
arrisHorizOvertempProtModeMib = _ArrisHorizOvertempProtModeMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 16)
)
_ArrisProdIdCMTS_ObjectIdentity = ObjectIdentity
arrisProdIdCMTS = _ArrisProdIdCMTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4)
)
_CmtsMSAS_ObjectIdentity = ObjectIdentity
cmtsMSAS = _CmtsMSAS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 1)
)
_Cmts1500_ObjectIdentity = ObjectIdentity
cmts1500 = _Cmts1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 2)
)
_CmtsC3_ObjectIdentity = ObjectIdentity
cmtsC3 = _CmtsC3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 3)
)
_CmtsC4_ObjectIdentity = ObjectIdentity
cmtsC4 = _CmtsC4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 4)
)
_CmtsCommon_ObjectIdentity = ObjectIdentity
cmtsCommon = _CmtsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 4, 5)
)
_ArrisProdIdMRC_ObjectIdentity = ObjectIdentity
arrisProdIdMRC = _ArrisProdIdMRC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 5)
)
_MrcController_ObjectIdentity = ObjectIdentity
mrcController = _MrcController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 5, 1)
)
_ArrisProdIdGlobalAccess_ObjectIdentity = ObjectIdentity
arrisProdIdGlobalAccess = _ArrisProdIdGlobalAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 6)
)
_ArrisGlobalAccessMib_ObjectIdentity = ObjectIdentity
arrisGlobalAccessMib = _ArrisGlobalAccessMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 6, 1)
)
_ArrisGlobalAccessProductUas_ObjectIdentity = ObjectIdentity
arrisGlobalAccessProductUas = _ArrisGlobalAccessProductUas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 6, 2)
)
_ArrisTools_ObjectIdentity = ObjectIdentity
arrisTools = _ArrisTools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 7)
)
_ArrisProdIdVideo_ObjectIdentity = ObjectIdentity
arrisProdIdVideo = _ArrisProdIdVideo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 8)
)
_ArrisProdIdRouter_ObjectIdentity = ObjectIdentity
arrisProdIdRouter = _ArrisProdIdRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 20)
)
_ArrisProdIdMG_ObjectIdentity = ObjectIdentity
arrisProdIdMG = _ArrisProdIdMG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 25)
)
_ArrisProdIdAssurance_ObjectIdentity = ObjectIdentity
arrisProdIdAssurance = _ArrisProdIdAssurance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 30)
)
_ArrisSME_ObjectIdentity = ObjectIdentity
arrisSME = _ArrisSME_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 40)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-MIB",
    **{"arris": arris,
       "arrisProducts": arrisProducts,
       "packetport": packetport,
       "cm110": cm110,
       "arrisProdIdCM": arrisProdIdCM,
       "arrisMtaDevMib": arrisMtaDevMib,
       "arrisCmDoc30Mib": arrisCmDoc30Mib,
       "arrisMtaDoc30Mib": arrisMtaDoc30Mib,
       "arrisSpeedTestMib": arrisSpeedTestMib,
       "arrisTR69Mib": arrisTR69Mib,
       "tcm": tcm,
       "ttm": ttm,
       "ttp": ttp,
       "arrisQamDetectionMib": arrisQamDetectionMib,
       "arrisNetPerfMonitorMib": arrisNetPerfMonitorMib,
       "arrisKddiFeatMib": arrisKddiFeatMib,
       "arrisDectMib": arrisDectMib,
       "arrisHorizOvertempProtModeMib": arrisHorizOvertempProtModeMib,
       "arrisProdIdCMTS": arrisProdIdCMTS,
       "cmtsMSAS": cmtsMSAS,
       "cmts1500": cmts1500,
       "cmtsC3": cmtsC3,
       "cmtsC4": cmtsC4,
       "cmtsCommon": cmtsCommon,
       "arrisProdIdMRC": arrisProdIdMRC,
       "mrcController": mrcController,
       "arrisProdIdGlobalAccess": arrisProdIdGlobalAccess,
       "arrisGlobalAccessMib": arrisGlobalAccessMib,
       "arrisGlobalAccessProductUas": arrisGlobalAccessProductUas,
       "arrisTools": arrisTools,
       "arrisProdIdVideo": arrisProdIdVideo,
       "arrisProdIdRouter": arrisProdIdRouter,
       "arrisProdIdMG": arrisProdIdMG,
       "arrisProdIdAssurance": arrisProdIdAssurance,
       "arrisSME": arrisSME}
)
