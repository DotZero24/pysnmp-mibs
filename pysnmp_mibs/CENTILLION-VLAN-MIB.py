# SNMP MIB module (CENTILLION-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/CENTILLION-VLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:20:12 2025
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

(VlanId,
 vlan) = mibBuilder.importSymbols(
    "CENTILLION-MCAST-MIB",
    "VlanId",
    "vlan")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CnVlanMemberGroup_ObjectIdentity = ObjectIdentity
cnVlanMemberGroup = _CnVlanMemberGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 2)
)
_CnVlanPortMemberTable_Object = MibTable
cnVlanPortMemberTable = _CnVlanPortMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 2, 1)
)
if mibBuilder.loadTexts:
    cnVlanPortMemberTable.setStatus("mandatory")
_CnVlanPortMemberEntry_Object = MibTableRow
cnVlanPortMemberEntry = _CnVlanPortMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 2, 1, 1)
)
cnVlanPortMemberEntry.setIndexNames(
    (0, "CENTILLION-VLAN-MIB", "cnVlanPortMemberCard"),
    (0, "CENTILLION-VLAN-MIB", "cnVlanPortMemberPort"),
    (0, "CENTILLION-VLAN-MIB", "cnVlanPortMemberVID"),
)
if mibBuilder.loadTexts:
    cnVlanPortMemberEntry.setStatus("mandatory")
_CnVlanPortMemberCard_Type = Integer32
_CnVlanPortMemberCard_Object = MibTableColumn
cnVlanPortMemberCard = _CnVlanPortMemberCard_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 2, 1, 1, 1),
    _CnVlanPortMemberCard_Type()
)
cnVlanPortMemberCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnVlanPortMemberCard.setStatus("mandatory")
_CnVlanPortMemberPort_Type = Integer32
_CnVlanPortMemberPort_Object = MibTableColumn
cnVlanPortMemberPort = _CnVlanPortMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 2, 1, 1, 2),
    _CnVlanPortMemberPort_Type()
)
cnVlanPortMemberPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnVlanPortMemberPort.setStatus("mandatory")
_CnVlanPortMemberVID_Type = VlanId
_CnVlanPortMemberVID_Object = MibTableColumn
cnVlanPortMemberVID = _CnVlanPortMemberVID_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 2, 1, 1, 3),
    _CnVlanPortMemberVID_Type()
)
cnVlanPortMemberVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnVlanPortMemberVID.setStatus("mandatory")
_CnVlanPortMemberStatus_Type = RowStatus
_CnVlanPortMemberStatus_Object = MibTableColumn
cnVlanPortMemberStatus = _CnVlanPortMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 2, 1, 1, 4),
    _CnVlanPortMemberStatus_Type()
)
cnVlanPortMemberStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnVlanPortMemberStatus.setStatus("mandatory")


class _CnVlanPortMemberIngressType_Type(Integer32):
    """Custom type cnVlanPortMemberIngressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pvid", 1),
          ("tag", 2),
          ("protocolId", 3))
    )


_CnVlanPortMemberIngressType_Type.__name__ = "Integer32"
_CnVlanPortMemberIngressType_Object = MibTableColumn
cnVlanPortMemberIngressType = _CnVlanPortMemberIngressType_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 2, 1, 1, 5),
    _CnVlanPortMemberIngressType_Type()
)
cnVlanPortMemberIngressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnVlanPortMemberIngressType.setStatus("mandatory")
_CnVlanPortMemberDynamic_Type = TruthValue
_CnVlanPortMemberDynamic_Object = MibTableColumn
cnVlanPortMemberDynamic = _CnVlanPortMemberDynamic_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 2, 1, 1, 6),
    _CnVlanPortMemberDynamic_Type()
)
cnVlanPortMemberDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnVlanPortMemberDynamic.setStatus("mandatory")
_CnVlanPortMemberIfIndex_Type = InterfaceIndex
_CnVlanPortMemberIfIndex_Object = MibTableColumn
cnVlanPortMemberIfIndex = _CnVlanPortMemberIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 2, 1, 1, 7),
    _CnVlanPortMemberIfIndex_Type()
)
cnVlanPortMemberIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnVlanPortMemberIfIndex.setStatus("mandatory")
_CnVlanPortMemberRing_Type = Integer32
_CnVlanPortMemberRing_Object = MibTableColumn
cnVlanPortMemberRing = _CnVlanPortMemberRing_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 2, 1, 1, 8),
    _CnVlanPortMemberRing_Type()
)
cnVlanPortMemberRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnVlanPortMemberRing.setStatus("mandatory")
_CnVlanENETMgt_Type = VlanId
_CnVlanENETMgt_Object = MibScalar
cnVlanENETMgt = _CnVlanENETMgt_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 3),
    _CnVlanENETMgt_Type()
)
cnVlanENETMgt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnVlanENETMgt.setStatus("mandatory")
_CnVlanTRMgt_Type = VlanId
_CnVlanTRMgt_Object = MibScalar
cnVlanTRMgt = _CnVlanTRMgt_Object(
    (1, 3, 6, 1, 4, 1, 930, 2, 1, 2, 31, 4),
    _CnVlanTRMgt_Type()
)
cnVlanTRMgt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnVlanTRMgt.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTILLION-VLAN-MIB",
    **{"cnVlanMemberGroup": cnVlanMemberGroup,
       "cnVlanPortMemberTable": cnVlanPortMemberTable,
       "cnVlanPortMemberEntry": cnVlanPortMemberEntry,
       "cnVlanPortMemberCard": cnVlanPortMemberCard,
       "cnVlanPortMemberPort": cnVlanPortMemberPort,
       "cnVlanPortMemberVID": cnVlanPortMemberVID,
       "cnVlanPortMemberStatus": cnVlanPortMemberStatus,
       "cnVlanPortMemberIngressType": cnVlanPortMemberIngressType,
       "cnVlanPortMemberDynamic": cnVlanPortMemberDynamic,
       "cnVlanPortMemberIfIndex": cnVlanPortMemberIfIndex,
       "cnVlanPortMemberRing": cnVlanPortMemberRing,
       "cnVlanENETMgt": cnVlanENETMgt,
       "cnVlanTRMgt": cnVlanTRMgt}
)
