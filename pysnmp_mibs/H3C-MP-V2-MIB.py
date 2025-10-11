# SNMP MIB module (H3C-MP-V2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-MP-V2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:18:32 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

h3cMultilinkPPPV2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 140)
)
if mibBuilder.loadTexts:
    h3cMultilinkPPPV2.setRevisions(
        ("2013-07-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cMpObjectsV2_ObjectIdentity = ObjectIdentity
h3cMpObjectsV2 = _H3cMpObjectsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 140, 1)
)
_H3cMpMultilinkV2Table_Object = MibTable
h3cMpMultilinkV2Table = _H3cMpMultilinkV2Table_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 140, 1, 1)
)
if mibBuilder.loadTexts:
    h3cMpMultilinkV2Table.setStatus("current")
_H3cMpMultilinkV2Entry_Object = MibTableRow
h3cMpMultilinkV2Entry = _H3cMpMultilinkV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 140, 1, 1, 1)
)
h3cMpMultilinkV2Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cMpMultilinkV2Entry.setStatus("current")


class _H3cMpMultilinkDescrV2_Type(DisplayString):
    """Custom type h3cMpMultilinkDescrV2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cMpMultilinkDescrV2_Type.__name__ = "DisplayString"
_H3cMpMultilinkDescrV2_Object = MibTableColumn
h3cMpMultilinkDescrV2 = _H3cMpMultilinkDescrV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 140, 1, 1, 1, 1),
    _H3cMpMultilinkDescrV2_Type()
)
h3cMpMultilinkDescrV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMpMultilinkDescrV2.setStatus("current")


class _H3cMpBundleNameV2_Type(DisplayString):
    """Custom type h3cMpBundleNameV2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cMpBundleNameV2_Type.__name__ = "DisplayString"
_H3cMpBundleNameV2_Object = MibTableColumn
h3cMpBundleNameV2 = _H3cMpBundleNameV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 140, 1, 1, 1, 2),
    _H3cMpBundleNameV2_Type()
)
h3cMpBundleNameV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMpBundleNameV2.setStatus("current")
_H3cMpBundledSlotV2_Type = Integer32
_H3cMpBundledSlotV2_Object = MibTableColumn
h3cMpBundledSlotV2 = _H3cMpBundledSlotV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 140, 1, 1, 1, 3),
    _H3cMpBundledSlotV2_Type()
)
h3cMpBundledSlotV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMpBundledSlotV2.setStatus("current")
_H3cMpBundledMemberCntV2_Type = Integer32
_H3cMpBundledMemberCntV2_Object = MibTableColumn
h3cMpBundledMemberCntV2 = _H3cMpBundledMemberCntV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 140, 1, 1, 1, 4),
    _H3cMpBundledMemberCntV2_Type()
)
h3cMpBundledMemberCntV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMpBundledMemberCntV2.setStatus("current")
_H3cMpLostFragmentsV2_Type = Counter32
_H3cMpLostFragmentsV2_Object = MibTableColumn
h3cMpLostFragmentsV2 = _H3cMpLostFragmentsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 140, 1, 1, 1, 5),
    _H3cMpLostFragmentsV2_Type()
)
h3cMpLostFragmentsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMpLostFragmentsV2.setStatus("current")
_H3cMpReorderedPktsV2_Type = Counter32
_H3cMpReorderedPktsV2_Object = MibTableColumn
h3cMpReorderedPktsV2 = _H3cMpReorderedPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 140, 1, 1, 1, 6),
    _H3cMpReorderedPktsV2_Type()
)
h3cMpReorderedPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMpReorderedPktsV2.setStatus("current")
_H3cMpUnassignedPktsV2_Type = Counter32
_H3cMpUnassignedPktsV2_Object = MibTableColumn
h3cMpUnassignedPktsV2 = _H3cMpUnassignedPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 140, 1, 1, 1, 7),
    _H3cMpUnassignedPktsV2_Type()
)
h3cMpUnassignedPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMpUnassignedPktsV2.setStatus("current")
_H3cMpInterleavedPktsV2_Type = Counter32
_H3cMpInterleavedPktsV2_Object = MibTableColumn
h3cMpInterleavedPktsV2 = _H3cMpInterleavedPktsV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 140, 1, 1, 1, 8),
    _H3cMpInterleavedPktsV2_Type()
)
h3cMpInterleavedPktsV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMpInterleavedPktsV2.setStatus("current")
_H3cMpRcvdSequenceV2_Type = Integer32
_H3cMpRcvdSequenceV2_Object = MibTableColumn
h3cMpRcvdSequenceV2 = _H3cMpRcvdSequenceV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 140, 1, 1, 1, 9),
    _H3cMpRcvdSequenceV2_Type()
)
h3cMpRcvdSequenceV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMpRcvdSequenceV2.setStatus("current")
_H3cMpSentSequenceV2_Type = Integer32
_H3cMpSentSequenceV2_Object = MibTableColumn
h3cMpSentSequenceV2 = _H3cMpSentSequenceV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 140, 1, 1, 1, 10),
    _H3cMpSentSequenceV2_Type()
)
h3cMpSentSequenceV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMpSentSequenceV2.setStatus("current")
_H3cMpMemberlinkV2Table_Object = MibTable
h3cMpMemberlinkV2Table = _H3cMpMemberlinkV2Table_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 140, 1, 2)
)
if mibBuilder.loadTexts:
    h3cMpMemberlinkV2Table.setStatus("current")
_H3cMpMemberlinkV2Entry_Object = MibTableRow
h3cMpMemberlinkV2Entry = _H3cMpMemberlinkV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 140, 1, 2, 1)
)
h3cMpMemberlinkV2Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-MP-V2-MIB", "h3cMpMemberlinkSeqNumberV2"),
)
if mibBuilder.loadTexts:
    h3cMpMemberlinkV2Entry.setStatus("current")


class _H3cMpMemberlinkSeqNumberV2_Type(Integer32):
    """Custom type h3cMpMemberlinkSeqNumberV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_H3cMpMemberlinkSeqNumberV2_Type.__name__ = "Integer32"
_H3cMpMemberlinkSeqNumberV2_Object = MibTableColumn
h3cMpMemberlinkSeqNumberV2 = _H3cMpMemberlinkSeqNumberV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 140, 1, 2, 1, 1),
    _H3cMpMemberlinkSeqNumberV2_Type()
)
h3cMpMemberlinkSeqNumberV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMpMemberlinkSeqNumberV2.setStatus("current")
_H3cMpMemberlinkIfIndexV2_Type = Integer32
_H3cMpMemberlinkIfIndexV2_Object = MibTableColumn
h3cMpMemberlinkIfIndexV2 = _H3cMpMemberlinkIfIndexV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 140, 1, 2, 1, 2),
    _H3cMpMemberlinkIfIndexV2_Type()
)
h3cMpMemberlinkIfIndexV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMpMemberlinkIfIndexV2.setStatus("current")


class _H3cMpMemberlinkDescrV2_Type(DisplayString):
    """Custom type h3cMpMemberlinkDescrV2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H3cMpMemberlinkDescrV2_Type.__name__ = "DisplayString"
_H3cMpMemberlinkDescrV2_Object = MibTableColumn
h3cMpMemberlinkDescrV2 = _H3cMpMemberlinkDescrV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 140, 1, 2, 1, 3),
    _H3cMpMemberlinkDescrV2_Type()
)
h3cMpMemberlinkDescrV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMpMemberlinkDescrV2.setStatus("current")


class _H3cMpMemberlinkMpStatusV2_Type(Integer32):
    """Custom type h3cMpMemberlinkMpStatusV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_H3cMpMemberlinkMpStatusV2_Type.__name__ = "Integer32"
_H3cMpMemberlinkMpStatusV2_Object = MibTableColumn
h3cMpMemberlinkMpStatusV2 = _H3cMpMemberlinkMpStatusV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 140, 1, 2, 1, 4),
    _H3cMpMemberlinkMpStatusV2_Type()
)
h3cMpMemberlinkMpStatusV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMpMemberlinkMpStatusV2.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-MP-V2-MIB",
    **{"h3cMultilinkPPPV2": h3cMultilinkPPPV2,
       "h3cMpObjectsV2": h3cMpObjectsV2,
       "h3cMpMultilinkV2Table": h3cMpMultilinkV2Table,
       "h3cMpMultilinkV2Entry": h3cMpMultilinkV2Entry,
       "h3cMpMultilinkDescrV2": h3cMpMultilinkDescrV2,
       "h3cMpBundleNameV2": h3cMpBundleNameV2,
       "h3cMpBundledSlotV2": h3cMpBundledSlotV2,
       "h3cMpBundledMemberCntV2": h3cMpBundledMemberCntV2,
       "h3cMpLostFragmentsV2": h3cMpLostFragmentsV2,
       "h3cMpReorderedPktsV2": h3cMpReorderedPktsV2,
       "h3cMpUnassignedPktsV2": h3cMpUnassignedPktsV2,
       "h3cMpInterleavedPktsV2": h3cMpInterleavedPktsV2,
       "h3cMpRcvdSequenceV2": h3cMpRcvdSequenceV2,
       "h3cMpSentSequenceV2": h3cMpSentSequenceV2,
       "h3cMpMemberlinkV2Table": h3cMpMemberlinkV2Table,
       "h3cMpMemberlinkV2Entry": h3cMpMemberlinkV2Entry,
       "h3cMpMemberlinkSeqNumberV2": h3cMpMemberlinkSeqNumberV2,
       "h3cMpMemberlinkIfIndexV2": h3cMpMemberlinkIfIndexV2,
       "h3cMpMemberlinkDescrV2": h3cMpMemberlinkDescrV2,
       "h3cMpMemberlinkMpStatusV2": h3cMpMemberlinkMpStatusV2}
)
