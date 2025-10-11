# SNMP MIB module (INFINERA-TP-DSEPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-DSEPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:46 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

(FloatTenths,
 InfnServiceType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnServiceType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dsePtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 22)
)
if mibBuilder.loadTexts:
    dsePtpMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DsePtpTable_Object = MibTable
dsePtpTable = _DsePtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 22, 1)
)
if mibBuilder.loadTexts:
    dsePtpTable.setStatus("current")
_DsePtpEntry_Object = MibTableRow
dsePtpEntry = _DsePtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 22, 1, 1)
)
dsePtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsePtpEntry.setStatus("current")
_DsePtpProvisionedRemoteTP_Type = DisplayString
_DsePtpProvisionedRemoteTP_Object = MibTableColumn
dsePtpProvisionedRemoteTP = _DsePtpProvisionedRemoteTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 22, 1, 1, 1),
    _DsePtpProvisionedRemoteTP_Type()
)
dsePtpProvisionedRemoteTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsePtpProvisionedRemoteTP.setStatus("current")


class _DsePtpPmHistStatsEnable_Type(Integer32):
    """Custom type dsePtpPmHistStatsEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_DsePtpPmHistStatsEnable_Type.__name__ = "Integer32"
_DsePtpPmHistStatsEnable_Object = MibTableColumn
dsePtpPmHistStatsEnable = _DsePtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 22, 1, 1, 2),
    _DsePtpPmHistStatsEnable_Type()
)
dsePtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsePtpPmHistStatsEnable.setStatus("current")
_DsePtpConformance_ObjectIdentity = ObjectIdentity
dsePtpConformance = _DsePtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 22, 3)
)
_DsePtpCompliances_ObjectIdentity = ObjectIdentity
dsePtpCompliances = _DsePtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 22, 3, 1)
)
_DsePtpGroups_ObjectIdentity = ObjectIdentity
dsePtpGroups = _DsePtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 22, 3, 2)
)

# Managed Objects groups

dsePtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 22, 3, 2, 1)
)
dsePtpGroup.setObjects(
      *(("INFINERA-TP-DSEPTP-MIB", "dsePtpProvisionedRemoteTP"),
        ("INFINERA-TP-DSEPTP-MIB", "dsePtpPmHistStatsEnable"))
)
if mibBuilder.loadTexts:
    dsePtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dsePtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 22, 3, 1, 1)
)
dsePtpCompliance.setObjects(
    ("INFINERA-TP-DSEPTP-MIB", "dsePtpGroup")
)
if mibBuilder.loadTexts:
    dsePtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-DSEPTP-MIB",
    **{"dsePtpMIB": dsePtpMIB,
       "dsePtpTable": dsePtpTable,
       "dsePtpEntry": dsePtpEntry,
       "dsePtpProvisionedRemoteTP": dsePtpProvisionedRemoteTP,
       "dsePtpPmHistStatsEnable": dsePtpPmHistStatsEnable,
       "dsePtpConformance": dsePtpConformance,
       "dsePtpCompliances": dsePtpCompliances,
       "dsePtpCompliance": dsePtpCompliance,
       "dsePtpGroups": dsePtpGroups,
       "dsePtpGroup": dsePtpGroup}
)
