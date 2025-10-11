# SNMP MIB module (IPS-AUTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/equallogic/IPS-AUTH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:24:36 2025
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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ipsAuthModule = ModuleIdentity(
    (1, 3, 6, 1, 3, 99999)
)
if mibBuilder.loadTexts:
    ipsAuthModule.setRevisions(
        ("2002-06-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IpsAuthAddress(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_IpsAuthObjects_ObjectIdentity = ObjectIdentity
ipsAuthObjects = _IpsAuthObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 99999, 1)
)
_IpsAuthDescriptors_ObjectIdentity = ObjectIdentity
ipsAuthDescriptors = _IpsAuthDescriptors_ObjectIdentity(
    (1, 3, 6, 1, 3, 99999, 1, 1)
)
_IpsAuthMethodTypes_ObjectIdentity = ObjectIdentity
ipsAuthMethodTypes = _IpsAuthMethodTypes_ObjectIdentity(
    (1, 3, 6, 1, 3, 99999, 1, 1, 1)
)
_IpsAuthMethodNone_ObjectIdentity = ObjectIdentity
ipsAuthMethodNone = _IpsAuthMethodNone_ObjectIdentity(
    (1, 3, 6, 1, 3, 99999, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ipsAuthMethodNone.setStatus("current")
_IpsAuthMethodSrp_ObjectIdentity = ObjectIdentity
ipsAuthMethodSrp = _IpsAuthMethodSrp_ObjectIdentity(
    (1, 3, 6, 1, 3, 99999, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ipsAuthMethodSrp.setStatus("current")
_IpsAuthMethodChap_ObjectIdentity = ObjectIdentity
ipsAuthMethodChap = _IpsAuthMethodChap_ObjectIdentity(
    (1, 3, 6, 1, 3, 99999, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ipsAuthMethodChap.setStatus("current")
_IpsAuthInstance_ObjectIdentity = ObjectIdentity
ipsAuthInstance = _IpsAuthInstance_ObjectIdentity(
    (1, 3, 6, 1, 3, 99999, 1, 2)
)
_IpsAuthInstanceAttributesTable_Object = MibTable
ipsAuthInstanceAttributesTable = _IpsAuthInstanceAttributesTable_Object(
    (1, 3, 6, 1, 3, 99999, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ipsAuthInstanceAttributesTable.setStatus("current")
_IpsAuthInstanceAttributesEntry_Object = MibTableRow
ipsAuthInstanceAttributesEntry = _IpsAuthInstanceAttributesEntry_Object(
    (1, 3, 6, 1, 3, 99999, 1, 2, 2, 1)
)
ipsAuthInstanceAttributesEntry.setIndexNames(
    (0, "IPS-AUTH-MIB", "ipsAuthInstIndex"),
)
if mibBuilder.loadTexts:
    ipsAuthInstanceAttributesEntry.setStatus("current")


class _IpsAuthInstIndex_Type(Unsigned32):
    """Custom type ipsAuthInstIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IpsAuthInstIndex_Type.__name__ = "Unsigned32"
_IpsAuthInstIndex_Object = MibTableColumn
ipsAuthInstIndex = _IpsAuthInstIndex_Object(
    (1, 3, 6, 1, 3, 99999, 1, 2, 2, 1, 1),
    _IpsAuthInstIndex_Type()
)
ipsAuthInstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsAuthInstIndex.setStatus("current")


class _IpsAuthInstDescr_Type(OctetString):
    """Custom type ipsAuthInstDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpsAuthInstDescr_Type.__name__ = "OctetString"
_IpsAuthInstDescr_Object = MibTableColumn
ipsAuthInstDescr = _IpsAuthInstDescr_Object(
    (1, 3, 6, 1, 3, 99999, 1, 2, 2, 1, 2),
    _IpsAuthInstDescr_Type()
)
ipsAuthInstDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipsAuthInstDescr.setStatus("current")
_IpsAuthIdentity_ObjectIdentity = ObjectIdentity
ipsAuthIdentity = _IpsAuthIdentity_ObjectIdentity(
    (1, 3, 6, 1, 3, 99999, 1, 3)
)
_IpsAuthIdentAttributesTable_Object = MibTable
ipsAuthIdentAttributesTable = _IpsAuthIdentAttributesTable_Object(
    (1, 3, 6, 1, 3, 99999, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ipsAuthIdentAttributesTable.setStatus("current")
_IpsAuthIdentAttributesEntry_Object = MibTableRow
ipsAuthIdentAttributesEntry = _IpsAuthIdentAttributesEntry_Object(
    (1, 3, 6, 1, 3, 99999, 1, 3, 1, 1)
)
ipsAuthIdentAttributesEntry.setIndexNames(
    (0, "IPS-AUTH-MIB", "ipsAuthInstIndex"),
    (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"),
)
if mibBuilder.loadTexts:
    ipsAuthIdentAttributesEntry.setStatus("current")


class _IpsAuthIdentIndex_Type(Unsigned32):
    """Custom type ipsAuthIdentIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IpsAuthIdentIndex_Type.__name__ = "Unsigned32"
_IpsAuthIdentIndex_Object = MibTableColumn
ipsAuthIdentIndex = _IpsAuthIdentIndex_Object(
    (1, 3, 6, 1, 3, 99999, 1, 3, 1, 1, 1),
    _IpsAuthIdentIndex_Type()
)
ipsAuthIdentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsAuthIdentIndex.setStatus("current")


class _IpsAuthIdentDescription_Type(OctetString):
    """Custom type ipsAuthIdentDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpsAuthIdentDescription_Type.__name__ = "OctetString"
_IpsAuthIdentDescription_Object = MibTableColumn
ipsAuthIdentDescription = _IpsAuthIdentDescription_Object(
    (1, 3, 6, 1, 3, 99999, 1, 3, 1, 1, 2),
    _IpsAuthIdentDescription_Type()
)
ipsAuthIdentDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthIdentDescription.setStatus("current")
_IpsAuthIdentRowStatus_Type = RowStatus
_IpsAuthIdentRowStatus_Object = MibTableColumn
ipsAuthIdentRowStatus = _IpsAuthIdentRowStatus_Object(
    (1, 3, 6, 1, 3, 99999, 1, 3, 1, 1, 3),
    _IpsAuthIdentRowStatus_Type()
)
ipsAuthIdentRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthIdentRowStatus.setStatus("current")
_IpsAuthIdentityName_ObjectIdentity = ObjectIdentity
ipsAuthIdentityName = _IpsAuthIdentityName_ObjectIdentity(
    (1, 3, 6, 1, 3, 99999, 1, 4)
)
_IpsAuthIdentNameAttributesTable_Object = MibTable
ipsAuthIdentNameAttributesTable = _IpsAuthIdentNameAttributesTable_Object(
    (1, 3, 6, 1, 3, 99999, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ipsAuthIdentNameAttributesTable.setStatus("current")
_IpsAuthIdentNameAttributesEntry_Object = MibTableRow
ipsAuthIdentNameAttributesEntry = _IpsAuthIdentNameAttributesEntry_Object(
    (1, 3, 6, 1, 3, 99999, 1, 4, 1, 1)
)
ipsAuthIdentNameAttributesEntry.setIndexNames(
    (0, "IPS-AUTH-MIB", "ipsAuthInstIndex"),
    (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"),
    (0, "IPS-AUTH-MIB", "ipsAuthIdentNameIndex"),
)
if mibBuilder.loadTexts:
    ipsAuthIdentNameAttributesEntry.setStatus("current")


class _IpsAuthIdentNameIndex_Type(Unsigned32):
    """Custom type ipsAuthIdentNameIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IpsAuthIdentNameIndex_Type.__name__ = "Unsigned32"
_IpsAuthIdentNameIndex_Object = MibTableColumn
ipsAuthIdentNameIndex = _IpsAuthIdentNameIndex_Object(
    (1, 3, 6, 1, 3, 99999, 1, 4, 1, 1, 1),
    _IpsAuthIdentNameIndex_Type()
)
ipsAuthIdentNameIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsAuthIdentNameIndex.setStatus("current")


class _IpsAuthIdentName_Type(OctetString):
    """Custom type ipsAuthIdentName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpsAuthIdentName_Type.__name__ = "OctetString"
_IpsAuthIdentName_Object = MibTableColumn
ipsAuthIdentName = _IpsAuthIdentName_Object(
    (1, 3, 6, 1, 3, 99999, 1, 4, 1, 1, 2),
    _IpsAuthIdentName_Type()
)
ipsAuthIdentName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthIdentName.setStatus("current")
_IpsAuthIdentNameRowStatus_Type = RowStatus
_IpsAuthIdentNameRowStatus_Object = MibTableColumn
ipsAuthIdentNameRowStatus = _IpsAuthIdentNameRowStatus_Object(
    (1, 3, 6, 1, 3, 99999, 1, 4, 1, 1, 3),
    _IpsAuthIdentNameRowStatus_Type()
)
ipsAuthIdentNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthIdentNameRowStatus.setStatus("current")
_IpsAuthIdentityAddress_ObjectIdentity = ObjectIdentity
ipsAuthIdentityAddress = _IpsAuthIdentityAddress_ObjectIdentity(
    (1, 3, 6, 1, 3, 99999, 1, 5)
)
_IpsAuthIdentAddrAttributesTable_Object = MibTable
ipsAuthIdentAddrAttributesTable = _IpsAuthIdentAddrAttributesTable_Object(
    (1, 3, 6, 1, 3, 99999, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ipsAuthIdentAddrAttributesTable.setStatus("current")
_IpsAuthIdentAddrAttributesEntry_Object = MibTableRow
ipsAuthIdentAddrAttributesEntry = _IpsAuthIdentAddrAttributesEntry_Object(
    (1, 3, 6, 1, 3, 99999, 1, 5, 1, 1)
)
ipsAuthIdentAddrAttributesEntry.setIndexNames(
    (0, "IPS-AUTH-MIB", "ipsAuthInstIndex"),
    (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"),
    (0, "IPS-AUTH-MIB", "ipsAuthIdentAddrIndex"),
)
if mibBuilder.loadTexts:
    ipsAuthIdentAddrAttributesEntry.setStatus("current")


class _IpsAuthIdentAddrIndex_Type(Unsigned32):
    """Custom type ipsAuthIdentAddrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IpsAuthIdentAddrIndex_Type.__name__ = "Unsigned32"
_IpsAuthIdentAddrIndex_Object = MibTableColumn
ipsAuthIdentAddrIndex = _IpsAuthIdentAddrIndex_Object(
    (1, 3, 6, 1, 3, 99999, 1, 5, 1, 1, 1),
    _IpsAuthIdentAddrIndex_Type()
)
ipsAuthIdentAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsAuthIdentAddrIndex.setStatus("current")
_IpsAuthIdentAddrType_Type = Integer32
_IpsAuthIdentAddrType_Object = MibTableColumn
ipsAuthIdentAddrType = _IpsAuthIdentAddrType_Object(
    (1, 3, 6, 1, 3, 99999, 1, 5, 1, 1, 2),
    _IpsAuthIdentAddrType_Type()
)
ipsAuthIdentAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthIdentAddrType.setStatus("current")
_IpsAuthIdentAddrStart_Type = IpsAuthAddress
_IpsAuthIdentAddrStart_Object = MibTableColumn
ipsAuthIdentAddrStart = _IpsAuthIdentAddrStart_Object(
    (1, 3, 6, 1, 3, 99999, 1, 5, 1, 1, 3),
    _IpsAuthIdentAddrStart_Type()
)
ipsAuthIdentAddrStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthIdentAddrStart.setStatus("current")
_IpsAuthIdentAddrEnd_Type = IpsAuthAddress
_IpsAuthIdentAddrEnd_Object = MibTableColumn
ipsAuthIdentAddrEnd = _IpsAuthIdentAddrEnd_Object(
    (1, 3, 6, 1, 3, 99999, 1, 5, 1, 1, 4),
    _IpsAuthIdentAddrEnd_Type()
)
ipsAuthIdentAddrEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthIdentAddrEnd.setStatus("current")
_IpsAuthIdentAddrRowStatus_Type = RowStatus
_IpsAuthIdentAddrRowStatus_Object = MibTableColumn
ipsAuthIdentAddrRowStatus = _IpsAuthIdentAddrRowStatus_Object(
    (1, 3, 6, 1, 3, 99999, 1, 5, 1, 1, 5),
    _IpsAuthIdentAddrRowStatus_Type()
)
ipsAuthIdentAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthIdentAddrRowStatus.setStatus("current")
_IpsAuthCredential_ObjectIdentity = ObjectIdentity
ipsAuthCredential = _IpsAuthCredential_ObjectIdentity(
    (1, 3, 6, 1, 3, 99999, 1, 6)
)
_IpsAuthCredentialAttributesTable_Object = MibTable
ipsAuthCredentialAttributesTable = _IpsAuthCredentialAttributesTable_Object(
    (1, 3, 6, 1, 3, 99999, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ipsAuthCredentialAttributesTable.setStatus("current")
_IpsAuthCredentialAttributesEntry_Object = MibTableRow
ipsAuthCredentialAttributesEntry = _IpsAuthCredentialAttributesEntry_Object(
    (1, 3, 6, 1, 3, 99999, 1, 6, 1, 1)
)
ipsAuthCredentialAttributesEntry.setIndexNames(
    (0, "IPS-AUTH-MIB", "ipsAuthInstIndex"),
    (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"),
    (0, "IPS-AUTH-MIB", "ipsAuthCredIndex"),
)
if mibBuilder.loadTexts:
    ipsAuthCredentialAttributesEntry.setStatus("current")


class _IpsAuthCredIndex_Type(Unsigned32):
    """Custom type ipsAuthCredIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IpsAuthCredIndex_Type.__name__ = "Unsigned32"
_IpsAuthCredIndex_Object = MibTableColumn
ipsAuthCredIndex = _IpsAuthCredIndex_Object(
    (1, 3, 6, 1, 3, 99999, 1, 6, 1, 1, 1),
    _IpsAuthCredIndex_Type()
)
ipsAuthCredIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipsAuthCredIndex.setStatus("current")
_IpsAuthCredAuthMethod_Type = Integer32
_IpsAuthCredAuthMethod_Object = MibTableColumn
ipsAuthCredAuthMethod = _IpsAuthCredAuthMethod_Object(
    (1, 3, 6, 1, 3, 99999, 1, 6, 1, 1, 2),
    _IpsAuthCredAuthMethod_Type()
)
ipsAuthCredAuthMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthCredAuthMethod.setStatus("current")
_IpsAuthCredRowStatus_Type = RowStatus
_IpsAuthCredRowStatus_Object = MibTableColumn
ipsAuthCredRowStatus = _IpsAuthCredRowStatus_Object(
    (1, 3, 6, 1, 3, 99999, 1, 6, 1, 1, 3),
    _IpsAuthCredRowStatus_Type()
)
ipsAuthCredRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthCredRowStatus.setStatus("current")
_IpsAuthCredChap_ObjectIdentity = ObjectIdentity
ipsAuthCredChap = _IpsAuthCredChap_ObjectIdentity(
    (1, 3, 6, 1, 3, 99999, 1, 7)
)
_IpsAuthCredChapAttributesTable_Object = MibTable
ipsAuthCredChapAttributesTable = _IpsAuthCredChapAttributesTable_Object(
    (1, 3, 6, 1, 3, 99999, 1, 7, 1)
)
if mibBuilder.loadTexts:
    ipsAuthCredChapAttributesTable.setStatus("current")
_IpsAuthCredChapAttributesEntry_Object = MibTableRow
ipsAuthCredChapAttributesEntry = _IpsAuthCredChapAttributesEntry_Object(
    (1, 3, 6, 1, 3, 99999, 1, 7, 1, 1)
)
ipsAuthCredChapAttributesEntry.setIndexNames(
    (0, "IPS-AUTH-MIB", "ipsAuthInstIndex"),
    (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"),
    (0, "IPS-AUTH-MIB", "ipsAuthCredIndex"),
)
if mibBuilder.loadTexts:
    ipsAuthCredChapAttributesEntry.setStatus("current")


class _IpsAuthCredChapUserName_Type(OctetString):
    """Custom type ipsAuthCredChapUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpsAuthCredChapUserName_Type.__name__ = "OctetString"
_IpsAuthCredChapUserName_Object = MibTableColumn
ipsAuthCredChapUserName = _IpsAuthCredChapUserName_Object(
    (1, 3, 6, 1, 3, 99999, 1, 7, 1, 1, 1),
    _IpsAuthCredChapUserName_Type()
)
ipsAuthCredChapUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthCredChapUserName.setStatus("current")


class _IpsAuthCredChapPassword_Type(OctetString):
    """Custom type ipsAuthCredChapPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpsAuthCredChapPassword_Type.__name__ = "OctetString"
_IpsAuthCredChapPassword_Object = MibTableColumn
ipsAuthCredChapPassword = _IpsAuthCredChapPassword_Object(
    (1, 3, 6, 1, 3, 99999, 1, 7, 1, 1, 2),
    _IpsAuthCredChapPassword_Type()
)
ipsAuthCredChapPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthCredChapPassword.setStatus("current")
_IpsAuthCredChapRowStatus_Type = RowStatus
_IpsAuthCredChapRowStatus_Object = MibTableColumn
ipsAuthCredChapRowStatus = _IpsAuthCredChapRowStatus_Object(
    (1, 3, 6, 1, 3, 99999, 1, 7, 1, 1, 3),
    _IpsAuthCredChapRowStatus_Type()
)
ipsAuthCredChapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthCredChapRowStatus.setStatus("current")
_IpsAuthCredSrp_ObjectIdentity = ObjectIdentity
ipsAuthCredSrp = _IpsAuthCredSrp_ObjectIdentity(
    (1, 3, 6, 1, 3, 99999, 1, 8)
)
_IpsAuthCredSrpAttributesTable_Object = MibTable
ipsAuthCredSrpAttributesTable = _IpsAuthCredSrpAttributesTable_Object(
    (1, 3, 6, 1, 3, 99999, 1, 8, 1)
)
if mibBuilder.loadTexts:
    ipsAuthCredSrpAttributesTable.setStatus("current")
_IpsAuthCredSrpAttributesEntry_Object = MibTableRow
ipsAuthCredSrpAttributesEntry = _IpsAuthCredSrpAttributesEntry_Object(
    (1, 3, 6, 1, 3, 99999, 1, 8, 1, 1)
)
ipsAuthCredSrpAttributesEntry.setIndexNames(
    (0, "IPS-AUTH-MIB", "ipsAuthInstIndex"),
    (0, "IPS-AUTH-MIB", "ipsAuthIdentIndex"),
    (0, "IPS-AUTH-MIB", "ipsAuthCredIndex"),
)
if mibBuilder.loadTexts:
    ipsAuthCredSrpAttributesEntry.setStatus("current")


class _IpsAuthCredSrpUserName_Type(OctetString):
    """Custom type ipsAuthCredSrpUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpsAuthCredSrpUserName_Type.__name__ = "OctetString"
_IpsAuthCredSrpUserName_Object = MibTableColumn
ipsAuthCredSrpUserName = _IpsAuthCredSrpUserName_Object(
    (1, 3, 6, 1, 3, 99999, 1, 8, 1, 1, 1),
    _IpsAuthCredSrpUserName_Type()
)
ipsAuthCredSrpUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthCredSrpUserName.setStatus("current")


class _IpsAuthCredSrpPassword_Type(OctetString):
    """Custom type ipsAuthCredSrpPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpsAuthCredSrpPassword_Type.__name__ = "OctetString"
_IpsAuthCredSrpPassword_Object = MibTableColumn
ipsAuthCredSrpPassword = _IpsAuthCredSrpPassword_Object(
    (1, 3, 6, 1, 3, 99999, 1, 8, 1, 1, 2),
    _IpsAuthCredSrpPassword_Type()
)
ipsAuthCredSrpPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthCredSrpPassword.setStatus("current")
_IpsAuthCredSrpRowStatus_Type = RowStatus
_IpsAuthCredSrpRowStatus_Object = MibTableColumn
ipsAuthCredSrpRowStatus = _IpsAuthCredSrpRowStatus_Object(
    (1, 3, 6, 1, 3, 99999, 1, 8, 1, 1, 3),
    _IpsAuthCredSrpRowStatus_Type()
)
ipsAuthCredSrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipsAuthCredSrpRowStatus.setStatus("current")
_IpsAuthNotifications_ObjectIdentity = ObjectIdentity
ipsAuthNotifications = _IpsAuthNotifications_ObjectIdentity(
    (1, 3, 6, 1, 3, 99999, 2)
)
_IpsAuthConformance_ObjectIdentity = ObjectIdentity
ipsAuthConformance = _IpsAuthConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 99999, 3)
)
_IpsAuthGroups_ObjectIdentity = ObjectIdentity
ipsAuthGroups = _IpsAuthGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 99999, 3, 1)
)
_IpsAuthCompliances_ObjectIdentity = ObjectIdentity
ipsAuthCompliances = _IpsAuthCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 99999, 3, 2)
)

# Managed Objects groups

ipsAuthInstanceAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 99999, 3, 1, 1)
)
ipsAuthInstanceAttributesGroup.setObjects(
    ("IPS-AUTH-MIB", "ipsAuthInstDescr")
)
if mibBuilder.loadTexts:
    ipsAuthInstanceAttributesGroup.setStatus("current")

ipsAuthIdentAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 99999, 3, 1, 2)
)
ipsAuthIdentAttributesGroup.setObjects(
      *(("IPS-AUTH-MIB", "ipsAuthIdentDescription"),
        ("IPS-AUTH-MIB", "ipsAuthIdentRowStatus"))
)
if mibBuilder.loadTexts:
    ipsAuthIdentAttributesGroup.setStatus("current")

ipsAuthIdentNameAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 99999, 3, 1, 3)
)
ipsAuthIdentNameAttributesGroup.setObjects(
      *(("IPS-AUTH-MIB", "ipsAuthIdentName"),
        ("IPS-AUTH-MIB", "ipsAuthIdentNameRowStatus"))
)
if mibBuilder.loadTexts:
    ipsAuthIdentNameAttributesGroup.setStatus("current")

ipsAuthIdentAddrAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 99999, 3, 1, 4)
)
ipsAuthIdentAddrAttributesGroup.setObjects(
      *(("IPS-AUTH-MIB", "ipsAuthIdentAddrType"),
        ("IPS-AUTH-MIB", "ipsAuthIdentAddrStart"),
        ("IPS-AUTH-MIB", "ipsAuthIdentAddrEnd"),
        ("IPS-AUTH-MIB", "ipsAuthIdentAddrRowStatus"))
)
if mibBuilder.loadTexts:
    ipsAuthIdentAddrAttributesGroup.setStatus("current")

ipsAuthIdentCredAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 99999, 3, 1, 5)
)
ipsAuthIdentCredAttributesGroup.setObjects(
      *(("IPS-AUTH-MIB", "ipsAuthCredAuthMethod"),
        ("IPS-AUTH-MIB", "ipsAuthCredRowStatus"))
)
if mibBuilder.loadTexts:
    ipsAuthIdentCredAttributesGroup.setStatus("current")

ipsAuthIdentChapAttrGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 99999, 3, 1, 6)
)
ipsAuthIdentChapAttrGroup.setObjects(
      *(("IPS-AUTH-MIB", "ipsAuthCredChapUserName"),
        ("IPS-AUTH-MIB", "ipsAuthCredChapPassword"),
        ("IPS-AUTH-MIB", "ipsAuthCredChapRowStatus"))
)
if mibBuilder.loadTexts:
    ipsAuthIdentChapAttrGroup.setStatus("current")

ipsAuthIdentSrpAttrGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 99999, 3, 1, 7)
)
ipsAuthIdentSrpAttrGroup.setObjects(
      *(("IPS-AUTH-MIB", "ipsAuthCredSrpUserName"),
        ("IPS-AUTH-MIB", "ipsAuthCredSrpPassword"),
        ("IPS-AUTH-MIB", "ipsAuthCredSrpRowStatus"))
)
if mibBuilder.loadTexts:
    ipsAuthIdentSrpAttrGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipsAuthComplianceV1 = ModuleCompliance(
    (1, 3, 6, 1, 3, 99999, 3, 2, 1)
)
ipsAuthComplianceV1.setObjects(
      *(("IPS-AUTH-MIB", "ipsAuthInstanceAttributesGroup"),
        ("IPS-AUTH-MIB", "ipsAuthIdentAttributesGroup"),
        ("IPS-AUTH-MIB", "ipsAuthIdentNameAttributesGroup"),
        ("IPS-AUTH-MIB", "ipsAuthIdentAddrAttributesGroup"),
        ("IPS-AUTH-MIB", "ipsAuthIdentCredAttributesGroup"))
)
if mibBuilder.loadTexts:
    ipsAuthComplianceV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPS-AUTH-MIB",
    **{"IpsAuthAddress": IpsAuthAddress,
       "ipsAuthModule": ipsAuthModule,
       "ipsAuthObjects": ipsAuthObjects,
       "ipsAuthDescriptors": ipsAuthDescriptors,
       "ipsAuthMethodTypes": ipsAuthMethodTypes,
       "ipsAuthMethodNone": ipsAuthMethodNone,
       "ipsAuthMethodSrp": ipsAuthMethodSrp,
       "ipsAuthMethodChap": ipsAuthMethodChap,
       "ipsAuthInstance": ipsAuthInstance,
       "ipsAuthInstanceAttributesTable": ipsAuthInstanceAttributesTable,
       "ipsAuthInstanceAttributesEntry": ipsAuthInstanceAttributesEntry,
       "ipsAuthInstIndex": ipsAuthInstIndex,
       "ipsAuthInstDescr": ipsAuthInstDescr,
       "ipsAuthIdentity": ipsAuthIdentity,
       "ipsAuthIdentAttributesTable": ipsAuthIdentAttributesTable,
       "ipsAuthIdentAttributesEntry": ipsAuthIdentAttributesEntry,
       "ipsAuthIdentIndex": ipsAuthIdentIndex,
       "ipsAuthIdentDescription": ipsAuthIdentDescription,
       "ipsAuthIdentRowStatus": ipsAuthIdentRowStatus,
       "ipsAuthIdentityName": ipsAuthIdentityName,
       "ipsAuthIdentNameAttributesTable": ipsAuthIdentNameAttributesTable,
       "ipsAuthIdentNameAttributesEntry": ipsAuthIdentNameAttributesEntry,
       "ipsAuthIdentNameIndex": ipsAuthIdentNameIndex,
       "ipsAuthIdentName": ipsAuthIdentName,
       "ipsAuthIdentNameRowStatus": ipsAuthIdentNameRowStatus,
       "ipsAuthIdentityAddress": ipsAuthIdentityAddress,
       "ipsAuthIdentAddrAttributesTable": ipsAuthIdentAddrAttributesTable,
       "ipsAuthIdentAddrAttributesEntry": ipsAuthIdentAddrAttributesEntry,
       "ipsAuthIdentAddrIndex": ipsAuthIdentAddrIndex,
       "ipsAuthIdentAddrType": ipsAuthIdentAddrType,
       "ipsAuthIdentAddrStart": ipsAuthIdentAddrStart,
       "ipsAuthIdentAddrEnd": ipsAuthIdentAddrEnd,
       "ipsAuthIdentAddrRowStatus": ipsAuthIdentAddrRowStatus,
       "ipsAuthCredential": ipsAuthCredential,
       "ipsAuthCredentialAttributesTable": ipsAuthCredentialAttributesTable,
       "ipsAuthCredentialAttributesEntry": ipsAuthCredentialAttributesEntry,
       "ipsAuthCredIndex": ipsAuthCredIndex,
       "ipsAuthCredAuthMethod": ipsAuthCredAuthMethod,
       "ipsAuthCredRowStatus": ipsAuthCredRowStatus,
       "ipsAuthCredChap": ipsAuthCredChap,
       "ipsAuthCredChapAttributesTable": ipsAuthCredChapAttributesTable,
       "ipsAuthCredChapAttributesEntry": ipsAuthCredChapAttributesEntry,
       "ipsAuthCredChapUserName": ipsAuthCredChapUserName,
       "ipsAuthCredChapPassword": ipsAuthCredChapPassword,
       "ipsAuthCredChapRowStatus": ipsAuthCredChapRowStatus,
       "ipsAuthCredSrp": ipsAuthCredSrp,
       "ipsAuthCredSrpAttributesTable": ipsAuthCredSrpAttributesTable,
       "ipsAuthCredSrpAttributesEntry": ipsAuthCredSrpAttributesEntry,
       "ipsAuthCredSrpUserName": ipsAuthCredSrpUserName,
       "ipsAuthCredSrpPassword": ipsAuthCredSrpPassword,
       "ipsAuthCredSrpRowStatus": ipsAuthCredSrpRowStatus,
       "ipsAuthNotifications": ipsAuthNotifications,
       "ipsAuthConformance": ipsAuthConformance,
       "ipsAuthGroups": ipsAuthGroups,
       "ipsAuthInstanceAttributesGroup": ipsAuthInstanceAttributesGroup,
       "ipsAuthIdentAttributesGroup": ipsAuthIdentAttributesGroup,
       "ipsAuthIdentNameAttributesGroup": ipsAuthIdentNameAttributesGroup,
       "ipsAuthIdentAddrAttributesGroup": ipsAuthIdentAddrAttributesGroup,
       "ipsAuthIdentCredAttributesGroup": ipsAuthIdentCredAttributesGroup,
       "ipsAuthIdentChapAttrGroup": ipsAuthIdentChapAttrGroup,
       "ipsAuthIdentSrpAttrGroup": ipsAuthIdentSrpAttrGroup,
       "ipsAuthCompliances": ipsAuthCompliances,
       "ipsAuthComplianceV1": ipsAuthComplianceV1}
)
