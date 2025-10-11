# SNMP MIB module (DNOS-MAB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/dell/DNOS-MAB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:07:30 2025
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

(dnOS,) = mibBuilder.importSymbols(
    "DELL-REF-MIB",
    "dnOS")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fastPathMab = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 75)
)
if mibBuilder.loadTexts:
    fastPathMab.setRevisions(
        ("2017-12-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentMabGlobalConfigGroup_ObjectIdentity = ObjectIdentity
agentMabGlobalConfigGroup = _AgentMabGlobalConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 75, 1)
)


class _AgentMABRequestAttr1GroupSize_Type(Integer32):
    """Custom type agentMABRequestAttr1GroupSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              12)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2),
          ("four", 4),
          ("twelve", 12))
    )


_AgentMABRequestAttr1GroupSize_Type.__name__ = "Integer32"
_AgentMABRequestAttr1GroupSize_Object = MibScalar
agentMABRequestAttr1GroupSize = _AgentMABRequestAttr1GroupSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 75, 1, 1),
    _AgentMABRequestAttr1GroupSize_Type()
)
agentMABRequestAttr1GroupSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMABRequestAttr1GroupSize.setStatus("current")


class _AgentMABRequestAttr1Separator_Type(Integer32):
    """Custom type agentMABRequestAttr1Separator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ieft", 1),
          ("legacy", 2),
          ("dot", 3))
    )


_AgentMABRequestAttr1Separator_Type.__name__ = "Integer32"
_AgentMABRequestAttr1Separator_Object = MibScalar
agentMABRequestAttr1Separator = _AgentMABRequestAttr1Separator_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 75, 1, 2),
    _AgentMABRequestAttr1Separator_Type()
)
agentMABRequestAttr1Separator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMABRequestAttr1Separator.setStatus("current")


class _AgentMABRequestAttr1Case_Type(Integer32):
    """Custom type agentMABRequestAttr1Case based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("upper", 1),
          ("lower", 2))
    )


_AgentMABRequestAttr1Case_Type.__name__ = "Integer32"
_AgentMABRequestAttr1Case_Object = MibScalar
agentMABRequestAttr1Case = _AgentMABRequestAttr1Case_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 75, 1, 3),
    _AgentMABRequestAttr1Case_Type()
)
agentMABRequestAttr1Case.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMABRequestAttr1Case.setStatus("current")
_AgentMabPortConfigGroup_ObjectIdentity = ObjectIdentity
agentMabPortConfigGroup = _AgentMabPortConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 75, 2)
)
_AgentMabPortConfigTable_Object = MibTable
agentMabPortConfigTable = _AgentMabPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 75, 2, 1)
)
if mibBuilder.loadTexts:
    agentMabPortConfigTable.setStatus("current")
_AgentMabPortConfigEntry_Object = MibTableRow
agentMabPortConfigEntry = _AgentMabPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 75, 2, 1, 1)
)
agentMabPortConfigEntry.setIndexNames(
    (0, "DNOS-MAB-MIB", "agentMabIfIndex"),
)
if mibBuilder.loadTexts:
    agentMabPortConfigEntry.setStatus("current")
_AgentMabIfIndex_Type = InterfaceIndex
_AgentMabIfIndex_Object = MibTableColumn
agentMabIfIndex = _AgentMabIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 75, 2, 1, 1, 1),
    _AgentMabIfIndex_Type()
)
agentMabIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentMabIfIndex.setStatus("current")


class _AgentMABPortEnabled_Type(Integer32):
    """Custom type agentMABPortEnabled based on Integer32"""
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


_AgentMABPortEnabled_Type.__name__ = "Integer32"
_AgentMABPortEnabled_Object = MibTableColumn
agentMABPortEnabled = _AgentMABPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 75, 2, 1, 1, 2),
    _AgentMABPortEnabled_Type()
)
agentMABPortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMABPortEnabled.setStatus("current")


class _AgentMabPortOperational_Type(Integer32):
    """Custom type agentMabPortOperational based on Integer32"""
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


_AgentMabPortOperational_Type.__name__ = "Integer32"
_AgentMabPortOperational_Object = MibTableColumn
agentMabPortOperational = _AgentMabPortOperational_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 75, 2, 1, 1, 3),
    _AgentMabPortOperational_Type()
)
agentMabPortOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMabPortOperational.setStatus("current")


class _AgentMabPortAuthType_Type(Integer32):
    """Custom type agentMabPortAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eapMd5", 1),
          ("pap", 2),
          ("chap", 3))
    )


_AgentMabPortAuthType_Type.__name__ = "Integer32"
_AgentMabPortAuthType_Object = MibTableColumn
agentMabPortAuthType = _AgentMabPortAuthType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 75, 2, 1, 1, 4),
    _AgentMabPortAuthType_Type()
)
agentMabPortAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMabPortAuthType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-MAB-MIB",
    **{"fastPathMab": fastPathMab,
       "agentMabGlobalConfigGroup": agentMabGlobalConfigGroup,
       "agentMABRequestAttr1GroupSize": agentMABRequestAttr1GroupSize,
       "agentMABRequestAttr1Separator": agentMABRequestAttr1Separator,
       "agentMABRequestAttr1Case": agentMABRequestAttr1Case,
       "agentMabPortConfigGroup": agentMabPortConfigGroup,
       "agentMabPortConfigTable": agentMabPortConfigTable,
       "agentMabPortConfigEntry": agentMabPortConfigEntry,
       "agentMabIfIndex": agentMabIfIndex,
       "agentMABPortEnabled": agentMABPortEnabled,
       "agentMabPortOperational": agentMabPortOperational,
       "agentMabPortAuthType": agentMabPortAuthType}
)
