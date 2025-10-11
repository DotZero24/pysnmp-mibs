# SNMP MIB module (ELTEX-MES-ISS-LA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-LA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:48:22 2025
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

(eltMesIss,) = mibBuilder.importSymbols(
    "ELTEX-MES-ISS-MIB",
    "eltMesIss")

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

eltMesIssLaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 23)
)
if mibBuilder.loadTexts:
    eltMesIssLaMIB.setRevisions(
        ("2020-12-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesIssLaObjects_ObjectIdentity = ObjectIdentity
eltMesIssLaObjects = _EltMesIssLaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 23, 1)
)
_EltMesIssLaGlobals_ObjectIdentity = ObjectIdentity
eltMesIssLaGlobals = _EltMesIssLaGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 23, 1, 1)
)
_EltMesIssLaSelectionPolicyTable_Object = MibTable
eltMesIssLaSelectionPolicyTable = _EltMesIssLaSelectionPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 23, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eltMesIssLaSelectionPolicyTable.setStatus("current")
_EltMesIssLaSelectionPolicyEntry_Object = MibTableRow
eltMesIssLaSelectionPolicyEntry = _EltMesIssLaSelectionPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 23, 1, 1, 1, 1)
)
eltMesIssLaSelectionPolicyEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-LA-MIB", "eltMesIssLaAlgorithmIdx"),
)
if mibBuilder.loadTexts:
    eltMesIssLaSelectionPolicyEntry.setStatus("current")
_EltMesIssLaAlgorithmIdx_Type = Integer32
_EltMesIssLaAlgorithmIdx_Object = MibTableColumn
eltMesIssLaAlgorithmIdx = _EltMesIssLaAlgorithmIdx_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 23, 1, 1, 1, 1, 1),
    _EltMesIssLaAlgorithmIdx_Type()
)
eltMesIssLaAlgorithmIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssLaAlgorithmIdx.setStatus("current")


class _EltMesIssLaPortChannelSelectionPolicy_Type(Integer32):
    """Custom type eltMesIssLaPortChannelSelectionPolicy based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("macSrc", 1),
          ("macDst", 2),
          ("macSrcDst", 3),
          ("ipSrc", 4),
          ("ipDst", 5),
          ("ipSrcDst", 6),
          ("macIpSrcDst", 7),
          ("macIpPortSrcDst", 8))
    )


_EltMesIssLaPortChannelSelectionPolicy_Type.__name__ = "Integer32"
_EltMesIssLaPortChannelSelectionPolicy_Object = MibTableColumn
eltMesIssLaPortChannelSelectionPolicy = _EltMesIssLaPortChannelSelectionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 23, 1, 1, 1, 1, 2),
    _EltMesIssLaPortChannelSelectionPolicy_Type()
)
eltMesIssLaPortChannelSelectionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssLaPortChannelSelectionPolicy.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-LA-MIB",
    **{"eltMesIssLaMIB": eltMesIssLaMIB,
       "eltMesIssLaObjects": eltMesIssLaObjects,
       "eltMesIssLaGlobals": eltMesIssLaGlobals,
       "eltMesIssLaSelectionPolicyTable": eltMesIssLaSelectionPolicyTable,
       "eltMesIssLaSelectionPolicyEntry": eltMesIssLaSelectionPolicyEntry,
       "eltMesIssLaAlgorithmIdx": eltMesIssLaAlgorithmIdx,
       "eltMesIssLaPortChannelSelectionPolicy": eltMesIssLaPortChannelSelectionPolicy}
)
