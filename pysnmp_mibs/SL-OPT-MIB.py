# SNMP MIB module (SL-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/smartoptics/SL-OPT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:31:34 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(sitelight,) = mibBuilder.importSymbols(
    "SL-NE-MIB",
    "sitelight")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

slOpt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SlOptConn_ObjectIdentity = ObjectIdentity
slOptConn = _SlOptConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1)
)
_OptXpdConnConfigTable_Object = MibTable
optXpdConnConfigTable = _OptXpdConnConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1)
)
if mibBuilder.loadTexts:
    optXpdConnConfigTable.setStatus("current")
_OptXpdConnConfigEntry_Object = MibTableRow
optXpdConnConfigEntry = _OptXpdConnConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1)
)
optXpdConnConfigEntry.setIndexNames(
    (0, "SL-OPT-MIB", "optXpdConnConfigIngressIf"),
    (0, "SL-OPT-MIB", "optXpdConnConfigEgressIf"),
)
if mibBuilder.loadTexts:
    optXpdConnConfigEntry.setStatus("current")
_OptXpdConnConfigIngressIf_Type = InterfaceIndex
_OptXpdConnConfigIngressIf_Object = MibTableColumn
optXpdConnConfigIngressIf = _OptXpdConnConfigIngressIf_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 1),
    _OptXpdConnConfigIngressIf_Type()
)
optXpdConnConfigIngressIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optXpdConnConfigIngressIf.setStatus("current")
_OptXpdConnConfigEgressIf_Type = InterfaceIndex
_OptXpdConnConfigEgressIf_Object = MibTableColumn
optXpdConnConfigEgressIf = _OptXpdConnConfigEgressIf_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 2),
    _OptXpdConnConfigEgressIf_Type()
)
optXpdConnConfigEgressIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optXpdConnConfigEgressIf.setStatus("current")
_OptXpdConnConfigRateControlAdmin_Type = Integer32
_OptXpdConnConfigRateControlAdmin_Object = MibTableColumn
optXpdConnConfigRateControlAdmin = _OptXpdConnConfigRateControlAdmin_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 3),
    _OptXpdConnConfigRateControlAdmin_Type()
)
optXpdConnConfigRateControlAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optXpdConnConfigRateControlAdmin.setStatus("current")
_OptXpdConnConfigRateControlOper_Type = Integer32
_OptXpdConnConfigRateControlOper_Object = MibTableColumn
optXpdConnConfigRateControlOper = _OptXpdConnConfigRateControlOper_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 4),
    _OptXpdConnConfigRateControlOper_Type()
)
optXpdConnConfigRateControlOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optXpdConnConfigRateControlOper.setStatus("current")
_OptXpdConnConfigRowStatus_Type = RowStatus
_OptXpdConnConfigRowStatus_Object = MibTableColumn
optXpdConnConfigRowStatus = _OptXpdConnConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 5),
    _OptXpdConnConfigRowStatus_Type()
)
optXpdConnConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optXpdConnConfigRowStatus.setStatus("current")
_OptXpdConnConfigLosPropagation_Type = TruthValue
_OptXpdConnConfigLosPropagation_Object = MibTableColumn
optXpdConnConfigLosPropagation = _OptXpdConnConfigLosPropagation_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 6),
    _OptXpdConnConfigLosPropagation_Type()
)
optXpdConnConfigLosPropagation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optXpdConnConfigLosPropagation.setStatus("current")
_OptXpdConnSonetRate_Type = TruthValue
_OptXpdConnSonetRate_Object = MibTableColumn
optXpdConnSonetRate = _OptXpdConnSonetRate_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 7),
    _OptXpdConnSonetRate_Type()
)
optXpdConnSonetRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optXpdConnSonetRate.setStatus("current")
_OptXpd10ConnConfigTable_Object = MibTable
optXpd10ConnConfigTable = _OptXpd10ConnConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 2)
)
if mibBuilder.loadTexts:
    optXpd10ConnConfigTable.setStatus("current")
_OptXpd10ConnConfigEntry_Object = MibTableRow
optXpd10ConnConfigEntry = _OptXpd10ConnConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 2, 1)
)
optXpd10ConnConfigEntry.setIndexNames(
    (0, "SL-OPT-MIB", "optXpd10ConnConfigIngressIf"),
)
if mibBuilder.loadTexts:
    optXpd10ConnConfigEntry.setStatus("current")
_OptXpd10ConnConfigIngressIf_Type = InterfaceIndex
_OptXpd10ConnConfigIngressIf_Object = MibTableColumn
optXpd10ConnConfigIngressIf = _OptXpd10ConnConfigIngressIf_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 2, 1, 1),
    _OptXpd10ConnConfigIngressIf_Type()
)
optXpd10ConnConfigIngressIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optXpd10ConnConfigIngressIf.setStatus("current")
_OptXpd10ConnConfigEgressIf_Type = InterfaceIndex
_OptXpd10ConnConfigEgressIf_Object = MibTableColumn
optXpd10ConnConfigEgressIf = _OptXpd10ConnConfigEgressIf_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 2, 1, 2),
    _OptXpd10ConnConfigEgressIf_Type()
)
optXpd10ConnConfigEgressIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optXpd10ConnConfigEgressIf.setStatus("current")
_OptXpd10ConnConfigRateControlOper_Type = Integer32
_OptXpd10ConnConfigRateControlOper_Object = MibTableColumn
optXpd10ConnConfigRateControlOper = _OptXpd10ConnConfigRateControlOper_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 2, 1, 3),
    _OptXpd10ConnConfigRateControlOper_Type()
)
optXpd10ConnConfigRateControlOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optXpd10ConnConfigRateControlOper.setStatus("current")
_OptXpd10ConnConfigLosPropagation_Type = TruthValue
_OptXpd10ConnConfigLosPropagation_Object = MibTableColumn
optXpd10ConnConfigLosPropagation = _OptXpd10ConnConfigLosPropagation_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 2, 1, 4),
    _OptXpd10ConnConfigLosPropagation_Type()
)
optXpd10ConnConfigLosPropagation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optXpd10ConnConfigLosPropagation.setStatus("current")
_SlOptLastChange_ObjectIdentity = ObjectIdentity
slOptLastChange = _SlOptLastChange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 6)
)
_OptXpdConnConfigLastChange_Type = TimeStamp
_OptXpdConnConfigLastChange_Object = MibScalar
optXpdConnConfigLastChange = _OptXpdConnConfigLastChange_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 6, 1),
    _OptXpdConnConfigLastChange_Type()
)
optXpdConnConfigLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optXpdConnConfigLastChange.setStatus("current")
_SlOptTraps_ObjectIdentity = ObjectIdentity
slOptTraps = _SlOptTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 7)
)

# Managed Objects groups


# Notification objects

optXpdConnConfigTableChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 7, 1)
)
if mibBuilder.loadTexts:
    optXpdConnConfigTableChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-OPT-MIB",
    **{"slOpt": slOpt,
       "slOptConn": slOptConn,
       "optXpdConnConfigTable": optXpdConnConfigTable,
       "optXpdConnConfigEntry": optXpdConnConfigEntry,
       "optXpdConnConfigIngressIf": optXpdConnConfigIngressIf,
       "optXpdConnConfigEgressIf": optXpdConnConfigEgressIf,
       "optXpdConnConfigRateControlAdmin": optXpdConnConfigRateControlAdmin,
       "optXpdConnConfigRateControlOper": optXpdConnConfigRateControlOper,
       "optXpdConnConfigRowStatus": optXpdConnConfigRowStatus,
       "optXpdConnConfigLosPropagation": optXpdConnConfigLosPropagation,
       "optXpdConnSonetRate": optXpdConnSonetRate,
       "optXpd10ConnConfigTable": optXpd10ConnConfigTable,
       "optXpd10ConnConfigEntry": optXpd10ConnConfigEntry,
       "optXpd10ConnConfigIngressIf": optXpd10ConnConfigIngressIf,
       "optXpd10ConnConfigEgressIf": optXpd10ConnConfigEgressIf,
       "optXpd10ConnConfigRateControlOper": optXpd10ConnConfigRateControlOper,
       "optXpd10ConnConfigLosPropagation": optXpd10ConnConfigLosPropagation,
       "slOptLastChange": slOptLastChange,
       "optXpdConnConfigLastChange": optXpdConnConfigLastChange,
       "slOptTraps": slOptTraps,
       "optXpdConnConfigTableChange": optXpdConnConfigTableChange}
)
