# SNMP MIB module (ADTRAN-SHARED-EOCU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-SHARED-EOCU-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:18 2025
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

(adIdentityShared,
 adShared) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentityShared",
    "adShared")

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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

adEoCuIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 69)
)
if mibBuilder.loadTexts:
    adEoCuIdentity.setRevisions(
        ("2007-04-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdEoCu_ObjectIdentity = ObjectIdentity
adEoCu = _AdEoCu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69)
)
_AdGenMEF_ObjectIdentity = ObjectIdentity
adGenMEF = _AdGenMEF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1)
)
_AdGenTA8xx_ObjectIdentity = ObjectIdentity
adGenTA8xx = _AdGenTA8xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2)
)
_AdGenOAM_ObjectIdentity = ObjectIdentity
adGenOAM = _AdGenOAM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 3)
)
_AdSLAProbe_ObjectIdentity = ObjectIdentity
adSLAProbe = _AdSLAProbe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 3, 1)
)
_AdGenTA8xxTlv_ObjectIdentity = ObjectIdentity
adGenTA8xxTlv = _AdGenTA8xxTlv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 4)
)
_AdGenTWAMPReflector_ObjectIdentity = ObjectIdentity
adGenTWAMPReflector = _AdGenTWAMPReflector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 5)
)
_AdGenEthCfm_ObjectIdentity = ObjectIdentity
adGenEthCfm = _AdGenEthCfm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 6)
)
_AdGenMEFID_ObjectIdentity = ObjectIdentity
adGenMEFID = _AdGenMEFID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 69, 1)
)
_AdGenTA8xxID_ObjectIdentity = ObjectIdentity
adGenTA8xxID = _AdGenTA8xxID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 69, 2)
)
_AdGenOAMID_ObjectIdentity = ObjectIdentity
adGenOAMID = _AdGenOAMID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 69, 3)
)
_AdSLAProbeID_ObjectIdentity = ObjectIdentity
adSLAProbeID = _AdSLAProbeID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 69, 3, 1)
)
_AdGenTA8xxTlvID_ObjectIdentity = ObjectIdentity
adGenTA8xxTlvID = _AdGenTA8xxTlvID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 69, 4)
)
_AdTWAMPReflectorID_ObjectIdentity = ObjectIdentity
adTWAMPReflectorID = _AdTWAMPReflectorID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 69, 5)
)
_AdGenEthCfmID_ObjectIdentity = ObjectIdentity
adGenEthCfmID = _AdGenEthCfmID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 69, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-SHARED-EOCU-MIB",
    **{"adEoCu": adEoCu,
       "adGenMEF": adGenMEF,
       "adGenTA8xx": adGenTA8xx,
       "adGenOAM": adGenOAM,
       "adSLAProbe": adSLAProbe,
       "adGenTA8xxTlv": adGenTA8xxTlv,
       "adGenTWAMPReflector": adGenTWAMPReflector,
       "adGenEthCfm": adGenEthCfm,
       "adEoCuIdentity": adEoCuIdentity,
       "adGenMEFID": adGenMEFID,
       "adGenTA8xxID": adGenTA8xxID,
       "adGenOAMID": adGenOAMID,
       "adSLAProbeID": adSLAProbeID,
       "adGenTA8xxTlvID": adGenTA8xxTlvID,
       "adTWAMPReflectorID": adTWAMPReflectorID,
       "adGenEthCfmID": adGenEthCfmID}
)
