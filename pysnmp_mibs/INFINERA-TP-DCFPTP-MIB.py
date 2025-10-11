# SNMP MIB module (INFINERA-TP-DCFPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-DCFPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:19 2025
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
 InfnDcmType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
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

dcfPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5)
)
if mibBuilder.loadTexts:
    dcfPtpMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DcfPtpTable_Object = MibTable
dcfPtpTable = _DcfPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    dcfPtpTable.setStatus("current")
_DcfPtpEntry_Object = MibTableRow
dcfPtpEntry = _DcfPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 1, 1)
)
dcfPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dcfPtpEntry.setStatus("current")


class _DcfPtpDcmType_Type(InfnDcmType):
    """Custom type dcfPtpDcmType based on InfnDcmType"""
    defaultValue = 25


_DcfPtpDcmType_Type.__name__ = "InfnDcmType"
_DcfPtpDcmType_Object = MibTableColumn
dcfPtpDcmType = _DcfPtpDcmType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 1, 1, 1),
    _DcfPtpDcmType_Type()
)
dcfPtpDcmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcfPtpDcmType.setStatus("current")


class _DcfPtpExpectedDcfLoss_Type(FloatTenths):
    """Custom type dcfPtpExpectedDcfLoss based on FloatTenths"""
    defaultValue = 0


_DcfPtpExpectedDcfLoss_Type.__name__ = "FloatTenths"
_DcfPtpExpectedDcfLoss_Object = MibTableColumn
dcfPtpExpectedDcfLoss = _DcfPtpExpectedDcfLoss_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 1, 1, 2),
    _DcfPtpExpectedDcfLoss_Type()
)
dcfPtpExpectedDcfLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcfPtpExpectedDcfLoss.setStatus("current")
if mibBuilder.loadTexts:
    dcfPtpExpectedDcfLoss.setUnits("0.1 dB")


class _DcfPtpExpectedDispersion_Type(Integer32):
    """Custom type dcfPtpExpectedDispersion based on Integer32"""
    defaultValue = 0


_DcfPtpExpectedDispersion_Type.__name__ = "Integer32"
_DcfPtpExpectedDispersion_Object = MibTableColumn
dcfPtpExpectedDispersion = _DcfPtpExpectedDispersion_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 1, 1, 3),
    _DcfPtpExpectedDispersion_Type()
)
dcfPtpExpectedDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcfPtpExpectedDispersion.setStatus("current")
if mibBuilder.loadTexts:
    dcfPtpExpectedDispersion.setUnits("100 ps/nm")


class _DcfPtpDcfLossReporting_Type(Integer32):
    """Custom type dcfPtpDcfLossReporting based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_DcfPtpDcfLossReporting_Type.__name__ = "Integer32"
_DcfPtpDcfLossReporting_Object = MibTableColumn
dcfPtpDcfLossReporting = _DcfPtpDcfLossReporting_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 1, 1, 4),
    _DcfPtpDcfLossReporting_Type()
)
dcfPtpDcfLossReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcfPtpDcfLossReporting.setStatus("current")


class _DcfPtpPmHistStatsEnable_Type(Integer32):
    """Custom type dcfPtpPmHistStatsEnable based on Integer32"""
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


_DcfPtpPmHistStatsEnable_Type.__name__ = "Integer32"
_DcfPtpPmHistStatsEnable_Object = MibTableColumn
dcfPtpPmHistStatsEnable = _DcfPtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 1, 1, 5),
    _DcfPtpPmHistStatsEnable_Type()
)
dcfPtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcfPtpPmHistStatsEnable.setStatus("current")
_DcfPtpProvisionedRemoteTP_Type = DisplayString
_DcfPtpProvisionedRemoteTP_Object = MibTableColumn
dcfPtpProvisionedRemoteTP = _DcfPtpProvisionedRemoteTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 1, 1, 6),
    _DcfPtpProvisionedRemoteTP_Type()
)
dcfPtpProvisionedRemoteTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcfPtpProvisionedRemoteTP.setStatus("current")
_DcfPtpConformance_ObjectIdentity = ObjectIdentity
dcfPtpConformance = _DcfPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 3)
)
_DcfPtpCompliances_ObjectIdentity = ObjectIdentity
dcfPtpCompliances = _DcfPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 3, 1)
)
_DcfPtpGroups_ObjectIdentity = ObjectIdentity
dcfPtpGroups = _DcfPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 3, 2)
)

# Managed Objects groups

dcfPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 3, 2, 1)
)
dcfPtpGroup.setObjects(
      *(("INFINERA-TP-DCFPTP-MIB", "dcfPtpDcmType"),
        ("INFINERA-TP-DCFPTP-MIB", "dcfPtpExpectedDcfLoss"),
        ("INFINERA-TP-DCFPTP-MIB", "dcfPtpExpectedDispersion"),
        ("INFINERA-TP-DCFPTP-MIB", "dcfPtpDcfLossReporting"),
        ("INFINERA-TP-DCFPTP-MIB", "dcfPtpPmHistStatsEnable"))
)
if mibBuilder.loadTexts:
    dcfPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dcfPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 5, 3, 1, 1)
)
dcfPtpCompliance.setObjects(
    ("INFINERA-TP-DCFPTP-MIB", "dcfPtpGroup")
)
if mibBuilder.loadTexts:
    dcfPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-DCFPTP-MIB",
    **{"dcfPtpMIB": dcfPtpMIB,
       "dcfPtpTable": dcfPtpTable,
       "dcfPtpEntry": dcfPtpEntry,
       "dcfPtpDcmType": dcfPtpDcmType,
       "dcfPtpExpectedDcfLoss": dcfPtpExpectedDcfLoss,
       "dcfPtpExpectedDispersion": dcfPtpExpectedDispersion,
       "dcfPtpDcfLossReporting": dcfPtpDcfLossReporting,
       "dcfPtpPmHistStatsEnable": dcfPtpPmHistStatsEnable,
       "dcfPtpProvisionedRemoteTP": dcfPtpProvisionedRemoteTP,
       "dcfPtpConformance": dcfPtpConformance,
       "dcfPtpCompliances": dcfPtpCompliances,
       "dcfPtpCompliance": dcfPtpCompliance,
       "dcfPtpGroups": dcfPtpGroups,
       "dcfPtpGroup": dcfPtpGroup}
)
