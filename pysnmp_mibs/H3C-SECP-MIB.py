# SNMP MIB module (H3C-SECP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-SECP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:18:00 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cSecp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 166)
)
if mibBuilder.loadTexts:
    h3cSecp.setRevisions(
        ("2016-12-19 16:05",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cSecpObjects_ObjectIdentity = ObjectIdentity
h3cSecpObjects = _H3cSecpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 166, 1)
)
_H3cSecpRunningInfoTable_Object = MibTable
h3cSecpRunningInfoTable = _H3cSecpRunningInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 166, 1, 1)
)
if mibBuilder.loadTexts:
    h3cSecpRunningInfoTable.setStatus("current")
_H3cSecpRunningInfoEntry_Object = MibTableRow
h3cSecpRunningInfoEntry = _H3cSecpRunningInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 166, 1, 1, 1)
)
h3cSecpRunningInfoEntry.setIndexNames(
    (0, "H3C-SECP-MIB", "h3cSecpIPVersion"),
    (0, "H3C-SECP-MIB", "h3cSecpRuleID"),
)
if mibBuilder.loadTexts:
    h3cSecpRunningInfoEntry.setStatus("current")


class _H3cSecpIPVersion_Type(Integer32):
    """Custom type h3cSecpIPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_H3cSecpIPVersion_Type.__name__ = "Integer32"
_H3cSecpIPVersion_Object = MibTableColumn
h3cSecpIPVersion = _H3cSecpIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 166, 1, 1, 1, 1),
    _H3cSecpIPVersion_Type()
)
h3cSecpIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSecpIPVersion.setStatus("current")


class _H3cSecpRuleID_Type(Unsigned32):
    """Custom type h3cSecpRuleID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_H3cSecpRuleID_Type.__name__ = "Unsigned32"
_H3cSecpRuleID_Object = MibTableColumn
h3cSecpRuleID = _H3cSecpRuleID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 166, 1, 1, 1, 2),
    _H3cSecpRuleID_Type()
)
h3cSecpRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSecpRuleID.setStatus("current")
_H3cSecpMatchPacketCount_Type = Counter64
_H3cSecpMatchPacketCount_Object = MibTableColumn
h3cSecpMatchPacketCount = _H3cSecpMatchPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 166, 1, 1, 1, 3),
    _H3cSecpMatchPacketCount_Type()
)
h3cSecpMatchPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSecpMatchPacketCount.setStatus("current")
_H3cSecpLastMatchTime_Type = Unsigned32
_H3cSecpLastMatchTime_Object = MibTableColumn
h3cSecpLastMatchTime = _H3cSecpLastMatchTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 166, 1, 1, 1, 4),
    _H3cSecpLastMatchTime_Type()
)
h3cSecpLastMatchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSecpLastMatchTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-SECP-MIB",
    **{"h3cSecp": h3cSecp,
       "h3cSecpObjects": h3cSecpObjects,
       "h3cSecpRunningInfoTable": h3cSecpRunningInfoTable,
       "h3cSecpRunningInfoEntry": h3cSecpRunningInfoEntry,
       "h3cSecpIPVersion": h3cSecpIPVersion,
       "h3cSecpRuleID": h3cSecpRuleID,
       "h3cSecpMatchPacketCount": h3cSecpMatchPacketCount,
       "h3cSecpLastMatchTime": h3cSecpLastMatchTime}
)
