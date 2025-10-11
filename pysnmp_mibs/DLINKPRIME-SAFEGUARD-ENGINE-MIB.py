# SNMP MIB module (DLINKPRIME-SAFEGUARD-ENGINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-SAFEGUARD-ENGINE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:47:15 2025
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

(dlinkPrimeCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkPrimeCommon")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkPrimeSafeguardEngineMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 14)
)
if mibBuilder.loadTexts:
    dlinkPrimeSafeguardEngineMIB.setRevisions(
        ("2014-04-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DpSafeguardEngineMIBNotif_ObjectIdentity = ObjectIdentity
dpSafeguardEngineMIBNotif = _DpSafeguardEngineMIBNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 14, 0)
)
_DpSafeguardEngineMIBObjects_ObjectIdentity = ObjectIdentity
dpSafeguardEngineMIBObjects = _DpSafeguardEngineMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 14, 1)
)


class _DpSafeguardEngineState_Type(Integer32):
    """Custom type dpSafeguardEngineState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_DpSafeguardEngineState_Type.__name__ = "Integer32"
_DpSafeguardEngineState_Object = MibScalar
dpSafeguardEngineState = _DpSafeguardEngineState_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 14, 1, 1),
    _DpSafeguardEngineState_Type()
)
dpSafeguardEngineState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpSafeguardEngineState.setStatus("current")
_DpSafeguardEngineMIBConformance_ObjectIdentity = ObjectIdentity
dpSafeguardEngineMIBConformance = _DpSafeguardEngineMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 14, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-SAFEGUARD-ENGINE-MIB",
    **{"dlinkPrimeSafeguardEngineMIB": dlinkPrimeSafeguardEngineMIB,
       "dpSafeguardEngineMIBNotif": dpSafeguardEngineMIBNotif,
       "dpSafeguardEngineMIBObjects": dpSafeguardEngineMIBObjects,
       "dpSafeguardEngineState": dpSafeguardEngineState,
       "dpSafeguardEngineMIBConformance": dpSafeguardEngineMIBConformance}
)
