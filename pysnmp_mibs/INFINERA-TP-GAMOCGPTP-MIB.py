# SNMP MIB module (INFINERA-TP-GAMOCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-GAMOCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:50 2025
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

(InfnDcmType,) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnDcmType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

gamOcgPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8)
)
if mibBuilder.loadTexts:
    gamOcgPtpMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GamOcgPtpTable_Object = MibTable
gamOcgPtpTable = _GamOcgPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8, 1)
)
if mibBuilder.loadTexts:
    gamOcgPtpTable.setStatus("current")
_GamOcgPtpEntry_Object = MibTableRow
gamOcgPtpEntry = _GamOcgPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8, 1, 1)
)
gamOcgPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gamOcgPtpEntry.setStatus("current")
_GamOcgPtpDiscoveredOcgTP_Type = DisplayString
_GamOcgPtpDiscoveredOcgTP_Object = MibTableColumn
gamOcgPtpDiscoveredOcgTP = _GamOcgPtpDiscoveredOcgTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8, 1, 1, 1),
    _GamOcgPtpDiscoveredOcgTP_Type()
)
gamOcgPtpDiscoveredOcgTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamOcgPtpDiscoveredOcgTP.setStatus("current")
_GamOcgPtpProvisionedOcgTP_Type = DisplayString
_GamOcgPtpProvisionedOcgTP_Object = MibTableColumn
gamOcgPtpProvisionedOcgTP = _GamOcgPtpProvisionedOcgTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8, 1, 1, 2),
    _GamOcgPtpProvisionedOcgTP_Type()
)
gamOcgPtpProvisionedOcgTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gamOcgPtpProvisionedOcgTP.setStatus("current")
_GamOcgPtpDiscoveredRemoteTP_Type = DisplayString
_GamOcgPtpDiscoveredRemoteTP_Object = MibTableColumn
gamOcgPtpDiscoveredRemoteTP = _GamOcgPtpDiscoveredRemoteTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8, 1, 1, 3),
    _GamOcgPtpDiscoveredRemoteTP_Type()
)
gamOcgPtpDiscoveredRemoteTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamOcgPtpDiscoveredRemoteTP.setStatus("current")


class _GamOcgPtpPmHistStatsEnable_Type(Integer32):
    """Custom type gamOcgPtpPmHistStatsEnable based on Integer32"""
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


_GamOcgPtpPmHistStatsEnable_Type.__name__ = "Integer32"
_GamOcgPtpPmHistStatsEnable_Object = MibTableColumn
gamOcgPtpPmHistStatsEnable = _GamOcgPtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8, 1, 1, 4),
    _GamOcgPtpPmHistStatsEnable_Type()
)
gamOcgPtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gamOcgPtpPmHistStatsEnable.setStatus("current")


class _GamOcgPtpInlineDcmType_Type(InfnDcmType):
    """Custom type gamOcgPtpInlineDcmType based on InfnDcmType"""
    defaultValue = 25


_GamOcgPtpInlineDcmType_Type.__name__ = "InfnDcmType"
_GamOcgPtpInlineDcmType_Object = MibTableColumn
gamOcgPtpInlineDcmType = _GamOcgPtpInlineDcmType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8, 1, 1, 5),
    _GamOcgPtpInlineDcmType_Type()
)
gamOcgPtpInlineDcmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gamOcgPtpInlineDcmType.setStatus("obsolete")
_GamOcgPtpConformance_ObjectIdentity = ObjectIdentity
gamOcgPtpConformance = _GamOcgPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8, 3)
)
_GamOcgPtpCompliances_ObjectIdentity = ObjectIdentity
gamOcgPtpCompliances = _GamOcgPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8, 3, 1)
)
_GamOcgPtpGroups_ObjectIdentity = ObjectIdentity
gamOcgPtpGroups = _GamOcgPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8, 3, 2)
)

# Managed Objects groups

gamOcgPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8, 3, 2, 1)
)
gamOcgPtpGroup.setObjects(
      *(("INFINERA-TP-GAMOCGPTP-MIB", "gamOcgPtpDiscoveredOcgTP"),
        ("INFINERA-TP-GAMOCGPTP-MIB", "gamOcgPtpProvisionedOcgTP"),
        ("INFINERA-TP-GAMOCGPTP-MIB", "gamOcgPtpDiscoveredRemoteTP"),
        ("INFINERA-TP-GAMOCGPTP-MIB", "gamOcgPtpPmHistStatsEnable"),
        ("INFINERA-TP-GAMOCGPTP-MIB", "gamOcgPtpInlineDcmType"))
)
if mibBuilder.loadTexts:
    gamOcgPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

gamOcgPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 8, 3, 1, 1)
)
gamOcgPtpCompliance.setObjects(
    ("INFINERA-TP-GAMOCGPTP-MIB", "gamOcgPtpGroup")
)
if mibBuilder.loadTexts:
    gamOcgPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-GAMOCGPTP-MIB",
    **{"gamOcgPtpMIB": gamOcgPtpMIB,
       "gamOcgPtpTable": gamOcgPtpTable,
       "gamOcgPtpEntry": gamOcgPtpEntry,
       "gamOcgPtpDiscoveredOcgTP": gamOcgPtpDiscoveredOcgTP,
       "gamOcgPtpProvisionedOcgTP": gamOcgPtpProvisionedOcgTP,
       "gamOcgPtpDiscoveredRemoteTP": gamOcgPtpDiscoveredRemoteTP,
       "gamOcgPtpPmHistStatsEnable": gamOcgPtpPmHistStatsEnable,
       "gamOcgPtpInlineDcmType": gamOcgPtpInlineDcmType,
       "gamOcgPtpConformance": gamOcgPtpConformance,
       "gamOcgPtpCompliances": gamOcgPtpCompliances,
       "gamOcgPtpCompliance": gamOcgPtpCompliance,
       "gamOcgPtpGroups": gamOcgPtpGroups,
       "gamOcgPtpGroup": gamOcgPtpGroup}
)
