# SNMP MIB module (ELTEX-MES-SMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-SMON-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:49:15 2025
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(eltMes,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMes")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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

eltMesSmon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 84)
)
if mibBuilder.loadTexts:
    eltMesSmon.setRevisions(
        ("2016-02-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EltPortCopyRemoteDirectionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eltPortCopyRemoteRx", 1),
          ("eltPortCopyRemoteTx", 2))
    )



# MIB Managed Objects in the order of their OIDs

_EltPortCopyRemoteTable_Object = MibTable
eltPortCopyRemoteTable = _EltPortCopyRemoteTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 84, 1)
)
if mibBuilder.loadTexts:
    eltPortCopyRemoteTable.setStatus("current")
_EltPortCopyRemoteEntry_Object = MibTableRow
eltPortCopyRemoteEntry = _EltPortCopyRemoteEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 84, 1, 1)
)
eltPortCopyRemoteEntry.setIndexNames(
    (0, "ELTEX-MES-SMON-MIB", "eltPortCopyRemoteDirection"),
)
if mibBuilder.loadTexts:
    eltPortCopyRemoteEntry.setStatus("current")
_EltPortCopyRemoteDirection_Type = EltPortCopyRemoteDirectionType
_EltPortCopyRemoteDirection_Object = MibTableColumn
eltPortCopyRemoteDirection = _EltPortCopyRemoteDirection_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 84, 1, 1, 1),
    _EltPortCopyRemoteDirection_Type()
)
eltPortCopyRemoteDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltPortCopyRemoteDirection.setStatus("current")
_EltPortCopyRemoteVlan_Type = VlanId
_EltPortCopyRemoteVlan_Object = MibTableColumn
eltPortCopyRemoteVlan = _EltPortCopyRemoteVlan_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 84, 1, 1, 2),
    _EltPortCopyRemoteVlan_Type()
)
eltPortCopyRemoteVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPortCopyRemoteVlan.setStatus("current")


class _EltPortCopyRemotePrio_Type(Integer32):
    """Custom type eltPortCopyRemotePrio based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_EltPortCopyRemotePrio_Type.__name__ = "Integer32"
_EltPortCopyRemotePrio_Object = MibTableColumn
eltPortCopyRemotePrio = _EltPortCopyRemotePrio_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 84, 1, 1, 3),
    _EltPortCopyRemotePrio_Type()
)
eltPortCopyRemotePrio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltPortCopyRemotePrio.setStatus("current")
_EltPortCopyRemoteStatus_Type = RowStatus
_EltPortCopyRemoteStatus_Object = MibTableColumn
eltPortCopyRemoteStatus = _EltPortCopyRemoteStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 84, 1, 1, 4),
    _EltPortCopyRemoteStatus_Type()
)
eltPortCopyRemoteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltPortCopyRemoteStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-SMON-MIB",
    **{"EltPortCopyRemoteDirectionType": EltPortCopyRemoteDirectionType,
       "eltMesSmon": eltMesSmon,
       "eltPortCopyRemoteTable": eltPortCopyRemoteTable,
       "eltPortCopyRemoteEntry": eltPortCopyRemoteEntry,
       "eltPortCopyRemoteDirection": eltPortCopyRemoteDirection,
       "eltPortCopyRemoteVlan": eltPortCopyRemoteVlan,
       "eltPortCopyRemotePrio": eltPortCopyRemotePrio,
       "eltPortCopyRemoteStatus": eltPortCopyRemoteStatus}
)
