# SNMP MIB module (GEN-RADIUS-AUTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/GEN-RADIUS-AUTH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:29:59 2025
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

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adGenRadiusAuth,
 adGenRadiusAuthID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenRadiusAuth",
    "adGenRadiusAuthID")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

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

adGenRadiusAuthMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 55, 1)
)
if mibBuilder.loadTexts:
    adGenRadiusAuthMIB.setRevisions(
        ("2014-02-19 00:00",
         "2013-10-21 00:00",
         "2013-09-06 00:00",
         "2013-06-13 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AdGenRadiusRelayOperStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AdGenRadiusAuthMIBObjects_ObjectIdentity = ObjectIdentity
adGenRadiusAuthMIBObjects = _AdGenRadiusAuthMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1)
)
_AdGenRadiusAuthProv_ObjectIdentity = ObjectIdentity
adGenRadiusAuthProv = _AdGenRadiusAuthProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1)
)
_AdGenRadiusAuthGroupTable_Object = MibTable
adGenRadiusAuthGroupTable = _AdGenRadiusAuthGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 1)
)
if mibBuilder.loadTexts:
    adGenRadiusAuthGroupTable.setStatus("current")
_AdGenRadiusAuthGroupEntry_Object = MibTableRow
adGenRadiusAuthGroupEntry = _AdGenRadiusAuthGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 1, 1)
)
adGenRadiusAuthGroupEntry.setIndexNames(
    (1, "GEN-RADIUS-AUTH-MIB", "adGenRadiusAuthGroupName"),
)
if mibBuilder.loadTexts:
    adGenRadiusAuthGroupEntry.setStatus("current")


class _AdGenRadiusAuthGroupName_Type(DisplayString):
    """Custom type adGenRadiusAuthGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenRadiusAuthGroupName_Type.__name__ = "DisplayString"
_AdGenRadiusAuthGroupName_Object = MibTableColumn
adGenRadiusAuthGroupName = _AdGenRadiusAuthGroupName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 1, 1, 1),
    _AdGenRadiusAuthGroupName_Type()
)
adGenRadiusAuthGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenRadiusAuthGroupName.setStatus("current")


class _AdGenRadiusAuthGroupNASId_Type(DisplayString):
    """Custom type adGenRadiusAuthGroupNASId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AdGenRadiusAuthGroupNASId_Type.__name__ = "DisplayString"
_AdGenRadiusAuthGroupNASId_Object = MibTableColumn
adGenRadiusAuthGroupNASId = _AdGenRadiusAuthGroupNASId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 1, 1, 2),
    _AdGenRadiusAuthGroupNASId_Type()
)
adGenRadiusAuthGroupNASId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenRadiusAuthGroupNASId.setStatus("current")


class _AdGenRadiusAuthGroupNASPortId_Type(DisplayString):
    """Custom type adGenRadiusAuthGroupNASPortId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AdGenRadiusAuthGroupNASPortId_Type.__name__ = "DisplayString"
_AdGenRadiusAuthGroupNASPortId_Object = MibTableColumn
adGenRadiusAuthGroupNASPortId = _AdGenRadiusAuthGroupNASPortId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 1, 1, 3),
    _AdGenRadiusAuthGroupNASPortId_Type()
)
adGenRadiusAuthGroupNASPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenRadiusAuthGroupNASPortId.setStatus("current")


class _AdGenRadiusAuthGroupVendorId_Type(Unsigned32):
    """Custom type adGenRadiusAuthGroupVendorId based on Unsigned32"""
    defaultValue = 664


_AdGenRadiusAuthGroupVendorId_Type.__name__ = "Unsigned32"
_AdGenRadiusAuthGroupVendorId_Object = MibTableColumn
adGenRadiusAuthGroupVendorId = _AdGenRadiusAuthGroupVendorId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 1, 1, 4),
    _AdGenRadiusAuthGroupVendorId_Type()
)
adGenRadiusAuthGroupVendorId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenRadiusAuthGroupVendorId.setStatus("current")


class _AdGenRadiusAuthGroupVendorDescription_Type(DisplayString):
    """Custom type adGenRadiusAuthGroupVendorDescription based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AdGenRadiusAuthGroupVendorDescription_Type.__name__ = "DisplayString"
_AdGenRadiusAuthGroupVendorDescription_Object = MibTableColumn
adGenRadiusAuthGroupVendorDescription = _AdGenRadiusAuthGroupVendorDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 1, 1, 5),
    _AdGenRadiusAuthGroupVendorDescription_Type()
)
adGenRadiusAuthGroupVendorDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenRadiusAuthGroupVendorDescription.setStatus("current")


class _AdGenRadiusAuthGroupLastError_Type(DisplayString):
    """Custom type adGenRadiusAuthGroupLastError based on DisplayString"""
    defaultValue = OctetString("")


_AdGenRadiusAuthGroupLastError_Type.__name__ = "DisplayString"
_AdGenRadiusAuthGroupLastError_Object = MibTableColumn
adGenRadiusAuthGroupLastError = _AdGenRadiusAuthGroupLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 1, 1, 6),
    _AdGenRadiusAuthGroupLastError_Type()
)
adGenRadiusAuthGroupLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRadiusAuthGroupLastError.setStatus("current")


class _AdGenRadiusAuthGroupDeadTime_Type(Unsigned32):
    """Custom type adGenRadiusAuthGroupDeadTime based on Unsigned32"""
    defaultValue = 0


_AdGenRadiusAuthGroupDeadTime_Type.__name__ = "Unsigned32"
_AdGenRadiusAuthGroupDeadTime_Object = MibTableColumn
adGenRadiusAuthGroupDeadTime = _AdGenRadiusAuthGroupDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 1, 1, 7),
    _AdGenRadiusAuthGroupDeadTime_Type()
)
adGenRadiusAuthGroupDeadTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenRadiusAuthGroupDeadTime.setStatus("current")
_AdGenRadiusAuthGroupRowStatus_Type = RowStatus
_AdGenRadiusAuthGroupRowStatus_Object = MibTableColumn
adGenRadiusAuthGroupRowStatus = _AdGenRadiusAuthGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 1, 1, 8),
    _AdGenRadiusAuthGroupRowStatus_Type()
)
adGenRadiusAuthGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenRadiusAuthGroupRowStatus.setStatus("current")
_AdGenRadiusAuthGroupTableLastError_Type = DisplayString
_AdGenRadiusAuthGroupTableLastError_Object = MibScalar
adGenRadiusAuthGroupTableLastError = _AdGenRadiusAuthGroupTableLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 2),
    _AdGenRadiusAuthGroupTableLastError_Type()
)
adGenRadiusAuthGroupTableLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRadiusAuthGroupTableLastError.setStatus("current")
_AdGenRadiusAuthGroupListTable_Object = MibTable
adGenRadiusAuthGroupListTable = _AdGenRadiusAuthGroupListTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 3)
)
if mibBuilder.loadTexts:
    adGenRadiusAuthGroupListTable.setStatus("current")
_AdGenRadiusAuthGroupListEntry_Object = MibTableRow
adGenRadiusAuthGroupListEntry = _AdGenRadiusAuthGroupListEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 3, 1)
)
adGenRadiusAuthGroupListEntry.setIndexNames(
    (0, "GEN-RADIUS-AUTH-MIB", "adGenRadiusAuthGroupNameFixedLen"),
    (0, "GEN-RADIUS-AUTH-MIB", "adGenRadiusAuthGroupListSeqIndex"),
)
if mibBuilder.loadTexts:
    adGenRadiusAuthGroupListEntry.setStatus("current")


class _AdGenRadiusAuthGroupNameFixedLen_Type(OctetString):
    """Custom type adGenRadiusAuthGroupNameFixedLen based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )
    fixed_length = 50


_AdGenRadiusAuthGroupNameFixedLen_Type.__name__ = "OctetString"
_AdGenRadiusAuthGroupNameFixedLen_Object = MibTableColumn
adGenRadiusAuthGroupNameFixedLen = _AdGenRadiusAuthGroupNameFixedLen_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 3, 1, 1),
    _AdGenRadiusAuthGroupNameFixedLen_Type()
)
adGenRadiusAuthGroupNameFixedLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenRadiusAuthGroupNameFixedLen.setStatus("current")
_AdGenRadiusAuthGroupListSeqIndex_Type = Unsigned32
_AdGenRadiusAuthGroupListSeqIndex_Object = MibTableColumn
adGenRadiusAuthGroupListSeqIndex = _AdGenRadiusAuthGroupListSeqIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 3, 1, 2),
    _AdGenRadiusAuthGroupListSeqIndex_Type()
)
adGenRadiusAuthGroupListSeqIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenRadiusAuthGroupListSeqIndex.setStatus("current")


class _AdGenRadiusAuthGroupListServerName_Type(DisplayString):
    """Custom type adGenRadiusAuthGroupListServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AdGenRadiusAuthGroupListServerName_Type.__name__ = "DisplayString"
_AdGenRadiusAuthGroupListServerName_Object = MibTableColumn
adGenRadiusAuthGroupListServerName = _AdGenRadiusAuthGroupListServerName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 3, 1, 3),
    _AdGenRadiusAuthGroupListServerName_Type()
)
adGenRadiusAuthGroupListServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenRadiusAuthGroupListServerName.setStatus("current")
_AdGenRadiusAuthNumOfServersPerGroup_Type = Unsigned32
_AdGenRadiusAuthNumOfServersPerGroup_Object = MibScalar
adGenRadiusAuthNumOfServersPerGroup = _AdGenRadiusAuthNumOfServersPerGroup_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 4),
    _AdGenRadiusAuthNumOfServersPerGroup_Type()
)
adGenRadiusAuthNumOfServersPerGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRadiusAuthNumOfServersPerGroup.setStatus("current")
_AdGenRadiusAuthServerTable_Object = MibTable
adGenRadiusAuthServerTable = _AdGenRadiusAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 5)
)
if mibBuilder.loadTexts:
    adGenRadiusAuthServerTable.setStatus("current")
_AdGenRadiusAuthServerEntry_Object = MibTableRow
adGenRadiusAuthServerEntry = _AdGenRadiusAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 5, 1)
)
adGenRadiusAuthServerEntry.setIndexNames(
    (1, "GEN-RADIUS-AUTH-MIB", "adGenRadiusAuthServerName"),
)
if mibBuilder.loadTexts:
    adGenRadiusAuthServerEntry.setStatus("current")


class _AdGenRadiusAuthServerName_Type(DisplayString):
    """Custom type adGenRadiusAuthServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenRadiusAuthServerName_Type.__name__ = "DisplayString"
_AdGenRadiusAuthServerName_Object = MibTableColumn
adGenRadiusAuthServerName = _AdGenRadiusAuthServerName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 5, 1, 1),
    _AdGenRadiusAuthServerName_Type()
)
adGenRadiusAuthServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenRadiusAuthServerName.setStatus("current")


class _AdGenRadiusAuthServerInetAddressType_Type(InetAddressType):
    """Custom type adGenRadiusAuthServerInetAddressType based on InetAddressType"""
    defaultValue = 1


_AdGenRadiusAuthServerInetAddressType_Type.__name__ = "InetAddressType"
_AdGenRadiusAuthServerInetAddressType_Object = MibTableColumn
adGenRadiusAuthServerInetAddressType = _AdGenRadiusAuthServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 5, 1, 2),
    _AdGenRadiusAuthServerInetAddressType_Type()
)
adGenRadiusAuthServerInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenRadiusAuthServerInetAddressType.setStatus("current")


class _AdGenRadiusAuthServerInetAddress_Type(InetAddress):
    """Custom type adGenRadiusAuthServerInetAddress based on InetAddress"""
    defaultValue = OctetString("0.0.0.0")


_AdGenRadiusAuthServerInetAddress_Type.__name__ = "InetAddress"
_AdGenRadiusAuthServerInetAddress_Object = MibTableColumn
adGenRadiusAuthServerInetAddress = _AdGenRadiusAuthServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 5, 1, 3),
    _AdGenRadiusAuthServerInetAddress_Type()
)
adGenRadiusAuthServerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenRadiusAuthServerInetAddress.setStatus("current")


class _AdGenRadiusAuthServerInetAddressPort_Type(InetPortNumber):
    """Custom type adGenRadiusAuthServerInetAddressPort based on InetPortNumber"""
    defaultValue = 1812


_AdGenRadiusAuthServerInetAddressPort_Type.__name__ = "InetPortNumber"
_AdGenRadiusAuthServerInetAddressPort_Object = MibTableColumn
adGenRadiusAuthServerInetAddressPort = _AdGenRadiusAuthServerInetAddressPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 5, 1, 4),
    _AdGenRadiusAuthServerInetAddressPort_Type()
)
adGenRadiusAuthServerInetAddressPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenRadiusAuthServerInetAddressPort.setStatus("current")


class _AdGenRadiusAuthServerSecret_Type(DisplayString):
    """Custom type adGenRadiusAuthServerSecret based on DisplayString"""
    defaultValue = OctetString("")


_AdGenRadiusAuthServerSecret_Type.__name__ = "DisplayString"
_AdGenRadiusAuthServerSecret_Object = MibTableColumn
adGenRadiusAuthServerSecret = _AdGenRadiusAuthServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 5, 1, 5),
    _AdGenRadiusAuthServerSecret_Type()
)
adGenRadiusAuthServerSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenRadiusAuthServerSecret.setStatus("current")


class _AdGenRadiusAuthServerLastError_Type(DisplayString):
    """Custom type adGenRadiusAuthServerLastError based on DisplayString"""
    defaultValue = OctetString("")


_AdGenRadiusAuthServerLastError_Type.__name__ = "DisplayString"
_AdGenRadiusAuthServerLastError_Object = MibTableColumn
adGenRadiusAuthServerLastError = _AdGenRadiusAuthServerLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 5, 1, 6),
    _AdGenRadiusAuthServerLastError_Type()
)
adGenRadiusAuthServerLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRadiusAuthServerLastError.setStatus("current")
_AdGenRadiusAuthServerRowStatus_Type = RowStatus
_AdGenRadiusAuthServerRowStatus_Object = MibTableColumn
adGenRadiusAuthServerRowStatus = _AdGenRadiusAuthServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 5, 1, 7),
    _AdGenRadiusAuthServerRowStatus_Type()
)
adGenRadiusAuthServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenRadiusAuthServerRowStatus.setStatus("current")
_AdGenRadiusAuthServerTableLastError_Type = DisplayString
_AdGenRadiusAuthServerTableLastError_Object = MibScalar
adGenRadiusAuthServerTableLastError = _AdGenRadiusAuthServerTableLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 6),
    _AdGenRadiusAuthServerTableLastError_Type()
)
adGenRadiusAuthServerTableLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRadiusAuthServerTableLastError.setStatus("current")
_AdGenRadiusAuthRelayTable_Object = MibTable
adGenRadiusAuthRelayTable = _AdGenRadiusAuthRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 7)
)
if mibBuilder.loadTexts:
    adGenRadiusAuthRelayTable.setStatus("current")
_AdGenRadiusAuthRelayEntry_Object = MibTableRow
adGenRadiusAuthRelayEntry = _AdGenRadiusAuthRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 7, 1)
)
adGenRadiusAuthRelayEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (1, "GEN-RADIUS-AUTH-MIB", "adGenRadiusAuthRelayName"),
)
if mibBuilder.loadTexts:
    adGenRadiusAuthRelayEntry.setStatus("current")


class _AdGenRadiusAuthRelayName_Type(DisplayString):
    """Custom type adGenRadiusAuthRelayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenRadiusAuthRelayName_Type.__name__ = "DisplayString"
_AdGenRadiusAuthRelayName_Object = MibTableColumn
adGenRadiusAuthRelayName = _AdGenRadiusAuthRelayName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 7, 1, 1),
    _AdGenRadiusAuthRelayName_Type()
)
adGenRadiusAuthRelayName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenRadiusAuthRelayName.setStatus("current")
_AdGenRadiusAuthRelayIPHostIfIndex_Type = InterfaceIndex
_AdGenRadiusAuthRelayIPHostIfIndex_Object = MibTableColumn
adGenRadiusAuthRelayIPHostIfIndex = _AdGenRadiusAuthRelayIPHostIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 7, 1, 2),
    _AdGenRadiusAuthRelayIPHostIfIndex_Type()
)
adGenRadiusAuthRelayIPHostIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenRadiusAuthRelayIPHostIfIndex.setStatus("current")


class _AdGenRadiusAuthRelayIPHostName_Type(DisplayString):
    """Custom type adGenRadiusAuthRelayIPHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_AdGenRadiusAuthRelayIPHostName_Type.__name__ = "DisplayString"
_AdGenRadiusAuthRelayIPHostName_Object = MibTableColumn
adGenRadiusAuthRelayIPHostName = _AdGenRadiusAuthRelayIPHostName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 7, 1, 3),
    _AdGenRadiusAuthRelayIPHostName_Type()
)
adGenRadiusAuthRelayIPHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenRadiusAuthRelayIPHostName.setStatus("current")


class _AdGenRadiusAuthRelayNasId_Type(DisplayString):
    """Custom type adGenRadiusAuthRelayNasId based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AdGenRadiusAuthRelayNasId_Type.__name__ = "DisplayString"
_AdGenRadiusAuthRelayNasId_Object = MibTableColumn
adGenRadiusAuthRelayNasId = _AdGenRadiusAuthRelayNasId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 7, 1, 4),
    _AdGenRadiusAuthRelayNasId_Type()
)
adGenRadiusAuthRelayNasId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenRadiusAuthRelayNasId.setStatus("current")


class _AdGenRadiusAuthRelayUserNameOverride_Type(Integer32):
    """Custom type adGenRadiusAuthRelayUserNameOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("callingstationId", 2))
    )


_AdGenRadiusAuthRelayUserNameOverride_Type.__name__ = "Integer32"
_AdGenRadiusAuthRelayUserNameOverride_Object = MibTableColumn
adGenRadiusAuthRelayUserNameOverride = _AdGenRadiusAuthRelayUserNameOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 7, 1, 5),
    _AdGenRadiusAuthRelayUserNameOverride_Type()
)
adGenRadiusAuthRelayUserNameOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenRadiusAuthRelayUserNameOverride.setStatus("current")


class _AdGenRadiusAuthRelayNasIPOverride_Type(Integer32):
    """Custom type adGenRadiusAuthRelayNasIPOverride based on Integer32"""
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


_AdGenRadiusAuthRelayNasIPOverride_Type.__name__ = "Integer32"
_AdGenRadiusAuthRelayNasIPOverride_Object = MibTableColumn
adGenRadiusAuthRelayNasIPOverride = _AdGenRadiusAuthRelayNasIPOverride_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 7, 1, 6),
    _AdGenRadiusAuthRelayNasIPOverride_Type()
)
adGenRadiusAuthRelayNasIPOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenRadiusAuthRelayNasIPOverride.setStatus("current")
_AdGenRadiusAuthRelayVendorSpecificId_Type = Unsigned32
_AdGenRadiusAuthRelayVendorSpecificId_Object = MibTableColumn
adGenRadiusAuthRelayVendorSpecificId = _AdGenRadiusAuthRelayVendorSpecificId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 7, 1, 7),
    _AdGenRadiusAuthRelayVendorSpecificId_Type()
)
adGenRadiusAuthRelayVendorSpecificId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenRadiusAuthRelayVendorSpecificId.setStatus("current")
_AdGenRadiusAuthRelayVendorSpecificSubType_Type = Unsigned32
_AdGenRadiusAuthRelayVendorSpecificSubType_Object = MibTableColumn
adGenRadiusAuthRelayVendorSpecificSubType = _AdGenRadiusAuthRelayVendorSpecificSubType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 7, 1, 8),
    _AdGenRadiusAuthRelayVendorSpecificSubType_Type()
)
adGenRadiusAuthRelayVendorSpecificSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenRadiusAuthRelayVendorSpecificSubType.setStatus("current")
_AdGenRadiusAuthRelayVendorSpecificSubValue_Type = DisplayString
_AdGenRadiusAuthRelayVendorSpecificSubValue_Object = MibTableColumn
adGenRadiusAuthRelayVendorSpecificSubValue = _AdGenRadiusAuthRelayVendorSpecificSubValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 7, 1, 9),
    _AdGenRadiusAuthRelayVendorSpecificSubValue_Type()
)
adGenRadiusAuthRelayVendorSpecificSubValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenRadiusAuthRelayVendorSpecificSubValue.setStatus("current")


class _AdGenRadiusAuthRelayLastError_Type(DisplayString):
    """Custom type adGenRadiusAuthRelayLastError based on DisplayString"""
    defaultValue = OctetString("")


_AdGenRadiusAuthRelayLastError_Type.__name__ = "DisplayString"
_AdGenRadiusAuthRelayLastError_Object = MibTableColumn
adGenRadiusAuthRelayLastError = _AdGenRadiusAuthRelayLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 7, 1, 10),
    _AdGenRadiusAuthRelayLastError_Type()
)
adGenRadiusAuthRelayLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRadiusAuthRelayLastError.setStatus("current")
_AdGenRadiusAuthRelayRowStatus_Type = RowStatus
_AdGenRadiusAuthRelayRowStatus_Object = MibTableColumn
adGenRadiusAuthRelayRowStatus = _AdGenRadiusAuthRelayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 7, 1, 11),
    _AdGenRadiusAuthRelayRowStatus_Type()
)
adGenRadiusAuthRelayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenRadiusAuthRelayRowStatus.setStatus("current")
_AdGenRadiusAuthRelayOperStatus_Type = AdGenRadiusRelayOperStatus
_AdGenRadiusAuthRelayOperStatus_Object = MibTableColumn
adGenRadiusAuthRelayOperStatus = _AdGenRadiusAuthRelayOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 7, 1, 12),
    _AdGenRadiusAuthRelayOperStatus_Type()
)
adGenRadiusAuthRelayOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRadiusAuthRelayOperStatus.setStatus("current")


class _AdGenRadiusAuthRelayCallingStationIdDelim_Type(Integer32):
    """Custom type adGenRadiusAuthRelayCallingStationIdDelim based on Integer32"""
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
        *(("noAction", 1),
          ("colons", 2),
          ("hyphens", 3))
    )


_AdGenRadiusAuthRelayCallingStationIdDelim_Type.__name__ = "Integer32"
_AdGenRadiusAuthRelayCallingStationIdDelim_Object = MibTableColumn
adGenRadiusAuthRelayCallingStationIdDelim = _AdGenRadiusAuthRelayCallingStationIdDelim_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 7, 1, 13),
    _AdGenRadiusAuthRelayCallingStationIdDelim_Type()
)
adGenRadiusAuthRelayCallingStationIdDelim.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenRadiusAuthRelayCallingStationIdDelim.setStatus("current")


class _AdGenRadiusAuthRelayAllowList_Type(DisplayString):
    """Custom type adGenRadiusAuthRelayAllowList based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdGenRadiusAuthRelayAllowList_Type.__name__ = "DisplayString"
_AdGenRadiusAuthRelayAllowList_Object = MibTableColumn
adGenRadiusAuthRelayAllowList = _AdGenRadiusAuthRelayAllowList_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 7, 1, 14),
    _AdGenRadiusAuthRelayAllowList_Type()
)
adGenRadiusAuthRelayAllowList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenRadiusAuthRelayAllowList.setStatus("current")
_AdGenRadiusAuthRelayErrorTable_Object = MibTable
adGenRadiusAuthRelayErrorTable = _AdGenRadiusAuthRelayErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 8)
)
if mibBuilder.loadTexts:
    adGenRadiusAuthRelayErrorTable.setStatus("current")
_AdGenRadiusAuthRelayErrorEntry_Object = MibTableRow
adGenRadiusAuthRelayErrorEntry = _AdGenRadiusAuthRelayErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 8, 1)
)
adGenRadiusAuthRelayErrorEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenRadiusAuthRelayErrorEntry.setStatus("current")
_AdGenRadiusAuthRelayTableLastCreateError_Type = DisplayString
_AdGenRadiusAuthRelayTableLastCreateError_Object = MibTableColumn
adGenRadiusAuthRelayTableLastCreateError = _AdGenRadiusAuthRelayTableLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 1, 8, 1, 1),
    _AdGenRadiusAuthRelayTableLastCreateError_Type()
)
adGenRadiusAuthRelayTableLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRadiusAuthRelayTableLastCreateError.setStatus("current")
_AdGenRadiusAuthStatus_ObjectIdentity = ObjectIdentity
adGenRadiusAuthStatus = _AdGenRadiusAuthStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 2)
)
_AdGenRadiusAuthStatusTable_Object = MibTable
adGenRadiusAuthStatusTable = _AdGenRadiusAuthStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 2, 1)
)
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusTable.setStatus("current")
_AdGenRadiusAuthStatusEntry_Object = MibTableRow
adGenRadiusAuthStatusEntry = _AdGenRadiusAuthStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 2, 1, 1)
)
adGenRadiusAuthStatusEntry.setIndexNames(
    (0, "GEN-RADIUS-AUTH-MIB", "adGenRadiusAuthStatusIfIndex"),
    (0, "GEN-RADIUS-AUTH-MIB", "adGenRadiusAuthStatusIpHostNameFixedLen"),
    (1, "GEN-RADIUS-AUTH-MIB", "adGenRadiusAuthStatusServerName"),
)
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusEntry.setStatus("current")
_AdGenRadiusAuthStatusIfIndex_Type = InterfaceIndex
_AdGenRadiusAuthStatusIfIndex_Object = MibTableColumn
adGenRadiusAuthStatusIfIndex = _AdGenRadiusAuthStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 2, 1, 1, 1),
    _AdGenRadiusAuthStatusIfIndex_Type()
)
adGenRadiusAuthStatusIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusIfIndex.setStatus("current")


class _AdGenRadiusAuthStatusIpHostNameFixedLen_Type(OctetString):
    """Custom type adGenRadiusAuthStatusIpHostNameFixedLen based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )
    fixed_length = 80


_AdGenRadiusAuthStatusIpHostNameFixedLen_Type.__name__ = "OctetString"
_AdGenRadiusAuthStatusIpHostNameFixedLen_Object = MibTableColumn
adGenRadiusAuthStatusIpHostNameFixedLen = _AdGenRadiusAuthStatusIpHostNameFixedLen_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 2, 1, 1, 2),
    _AdGenRadiusAuthStatusIpHostNameFixedLen_Type()
)
adGenRadiusAuthStatusIpHostNameFixedLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusIpHostNameFixedLen.setStatus("current")


class _AdGenRadiusAuthStatusServerName_Type(DisplayString):
    """Custom type adGenRadiusAuthStatusServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenRadiusAuthStatusServerName_Type.__name__ = "DisplayString"
_AdGenRadiusAuthStatusServerName_Object = MibTableColumn
adGenRadiusAuthStatusServerName = _AdGenRadiusAuthStatusServerName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 2, 1, 1, 3),
    _AdGenRadiusAuthStatusServerName_Type()
)
adGenRadiusAuthStatusServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusServerName.setStatus("current")
_AdGenRadiusAuthStatusInetAddressType_Type = InetAddressType
_AdGenRadiusAuthStatusInetAddressType_Object = MibTableColumn
adGenRadiusAuthStatusInetAddressType = _AdGenRadiusAuthStatusInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 2, 1, 1, 4),
    _AdGenRadiusAuthStatusInetAddressType_Type()
)
adGenRadiusAuthStatusInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusInetAddressType.setStatus("current")
_AdGenRadiusAuthStatusInetAddress_Type = InetAddress
_AdGenRadiusAuthStatusInetAddress_Object = MibTableColumn
adGenRadiusAuthStatusInetAddress = _AdGenRadiusAuthStatusInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 2, 1, 1, 5),
    _AdGenRadiusAuthStatusInetAddress_Type()
)
adGenRadiusAuthStatusInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusInetAddress.setStatus("current")


class _AdGenRadiusAuthStatusInetPortNumber_Type(InetPortNumber):
    """Custom type adGenRadiusAuthStatusInetPortNumber based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AdGenRadiusAuthStatusInetPortNumber_Type.__name__ = "InetPortNumber"
_AdGenRadiusAuthStatusInetPortNumber_Object = MibTableColumn
adGenRadiusAuthStatusInetPortNumber = _AdGenRadiusAuthStatusInetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 2, 1, 1, 6),
    _AdGenRadiusAuthStatusInetPortNumber_Type()
)
adGenRadiusAuthStatusInetPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusInetPortNumber.setStatus("current")
_AdGenRadiusAuthStatusRoundTripTime_Type = TimeTicks
_AdGenRadiusAuthStatusRoundTripTime_Object = MibTableColumn
adGenRadiusAuthStatusRoundTripTime = _AdGenRadiusAuthStatusRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 2, 1, 1, 7),
    _AdGenRadiusAuthStatusRoundTripTime_Type()
)
adGenRadiusAuthStatusRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusRoundTripTime.setStatus("current")
_AdGenRadiusAuthStatusAccessRequests_Type = Counter32
_AdGenRadiusAuthStatusAccessRequests_Object = MibTableColumn
adGenRadiusAuthStatusAccessRequests = _AdGenRadiusAuthStatusAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 2, 1, 1, 8),
    _AdGenRadiusAuthStatusAccessRequests_Type()
)
adGenRadiusAuthStatusAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusAccessRequests.setStatus("current")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusAccessRequests.setUnits("packets")
_AdGenRadiusAuthStatusAccessRetransmissions_Type = Counter32
_AdGenRadiusAuthStatusAccessRetransmissions_Object = MibTableColumn
adGenRadiusAuthStatusAccessRetransmissions = _AdGenRadiusAuthStatusAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 2, 1, 1, 9),
    _AdGenRadiusAuthStatusAccessRetransmissions_Type()
)
adGenRadiusAuthStatusAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusAccessRetransmissions.setStatus("current")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusAccessRetransmissions.setUnits("packets")
_AdGenRadiusAuthStatusAccessAccepts_Type = Counter32
_AdGenRadiusAuthStatusAccessAccepts_Object = MibTableColumn
adGenRadiusAuthStatusAccessAccepts = _AdGenRadiusAuthStatusAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 2, 1, 1, 10),
    _AdGenRadiusAuthStatusAccessAccepts_Type()
)
adGenRadiusAuthStatusAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusAccessAccepts.setStatus("current")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusAccessAccepts.setUnits("packets")
_AdGenRadiusAuthStatusAccessRejects_Type = Counter32
_AdGenRadiusAuthStatusAccessRejects_Object = MibTableColumn
adGenRadiusAuthStatusAccessRejects = _AdGenRadiusAuthStatusAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 2, 1, 1, 11),
    _AdGenRadiusAuthStatusAccessRejects_Type()
)
adGenRadiusAuthStatusAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusAccessRejects.setStatus("current")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusAccessRejects.setUnits("packets")
_AdGenRadiusAuthStatusAccessChallenges_Type = Counter32
_AdGenRadiusAuthStatusAccessChallenges_Object = MibTableColumn
adGenRadiusAuthStatusAccessChallenges = _AdGenRadiusAuthStatusAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 2, 1, 1, 12),
    _AdGenRadiusAuthStatusAccessChallenges_Type()
)
adGenRadiusAuthStatusAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusAccessChallenges.setStatus("current")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusAccessChallenges.setUnits("packets")
_AdGenRadiusAuthStatusMalformedAccessResponses_Type = Counter32
_AdGenRadiusAuthStatusMalformedAccessResponses_Object = MibTableColumn
adGenRadiusAuthStatusMalformedAccessResponses = _AdGenRadiusAuthStatusMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 2, 1, 1, 13),
    _AdGenRadiusAuthStatusMalformedAccessResponses_Type()
)
adGenRadiusAuthStatusMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusMalformedAccessResponses.setStatus("current")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusMalformedAccessResponses.setUnits("packets")
_AdGenRadiusAuthStatusBadAuthenticators_Type = Counter32
_AdGenRadiusAuthStatusBadAuthenticators_Object = MibTableColumn
adGenRadiusAuthStatusBadAuthenticators = _AdGenRadiusAuthStatusBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 2, 1, 1, 14),
    _AdGenRadiusAuthStatusBadAuthenticators_Type()
)
adGenRadiusAuthStatusBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusBadAuthenticators.setStatus("current")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusBadAuthenticators.setUnits("packets")
_AdGenRadiusAuthStatusPendingRequests_Type = Gauge32
_AdGenRadiusAuthStatusPendingRequests_Object = MibTableColumn
adGenRadiusAuthStatusPendingRequests = _AdGenRadiusAuthStatusPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 2, 1, 1, 15),
    _AdGenRadiusAuthStatusPendingRequests_Type()
)
adGenRadiusAuthStatusPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusPendingRequests.setStatus("current")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusPendingRequests.setUnits("packets")
_AdGenRadiusAuthStatusTimeouts_Type = Counter32
_AdGenRadiusAuthStatusTimeouts_Object = MibTableColumn
adGenRadiusAuthStatusTimeouts = _AdGenRadiusAuthStatusTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 2, 1, 1, 16),
    _AdGenRadiusAuthStatusTimeouts_Type()
)
adGenRadiusAuthStatusTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusTimeouts.setUnits("timeouts")
_AdGenRadiusAuthStatusUnknownTypes_Type = Counter32
_AdGenRadiusAuthStatusUnknownTypes_Object = MibTableColumn
adGenRadiusAuthStatusUnknownTypes = _AdGenRadiusAuthStatusUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 2, 1, 1, 17),
    _AdGenRadiusAuthStatusUnknownTypes_Type()
)
adGenRadiusAuthStatusUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusUnknownTypes.setStatus("current")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusUnknownTypes.setUnits("packets")
_AdGenRadiusAuthStatusPacketsDropped_Type = Counter32
_AdGenRadiusAuthStatusPacketsDropped_Object = MibTableColumn
adGenRadiusAuthStatusPacketsDropped = _AdGenRadiusAuthStatusPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 2, 1, 1, 18),
    _AdGenRadiusAuthStatusPacketsDropped_Type()
)
adGenRadiusAuthStatusPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusPacketsDropped.setStatus("current")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusPacketsDropped.setUnits("packets")
_AdGenRadiusAuthStatusCounterDiscontinuity_Type = TimeTicks
_AdGenRadiusAuthStatusCounterDiscontinuity_Object = MibTableColumn
adGenRadiusAuthStatusCounterDiscontinuity = _AdGenRadiusAuthStatusCounterDiscontinuity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 2, 1, 1, 19),
    _AdGenRadiusAuthStatusCounterDiscontinuity_Type()
)
adGenRadiusAuthStatusCounterDiscontinuity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusCounterDiscontinuity.setStatus("current")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusCounterDiscontinuity.setUnits("centiseconds")


class _AdGenRadiusAuthStatusServerState_Type(Integer32):
    """Custom type adGenRadiusAuthStatusServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("dead", 2))
    )


_AdGenRadiusAuthStatusServerState_Type.__name__ = "Integer32"
_AdGenRadiusAuthStatusServerState_Object = MibTableColumn
adGenRadiusAuthStatusServerState = _AdGenRadiusAuthStatusServerState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 55, 1, 2, 1, 1, 20),
    _AdGenRadiusAuthStatusServerState_Type()
)
adGenRadiusAuthStatusServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenRadiusAuthStatusServerState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GEN-RADIUS-AUTH-MIB",
    **{"AdGenRadiusRelayOperStatus": AdGenRadiusRelayOperStatus,
       "adGenRadiusAuthMIBObjects": adGenRadiusAuthMIBObjects,
       "adGenRadiusAuthProv": adGenRadiusAuthProv,
       "adGenRadiusAuthGroupTable": adGenRadiusAuthGroupTable,
       "adGenRadiusAuthGroupEntry": adGenRadiusAuthGroupEntry,
       "adGenRadiusAuthGroupName": adGenRadiusAuthGroupName,
       "adGenRadiusAuthGroupNASId": adGenRadiusAuthGroupNASId,
       "adGenRadiusAuthGroupNASPortId": adGenRadiusAuthGroupNASPortId,
       "adGenRadiusAuthGroupVendorId": adGenRadiusAuthGroupVendorId,
       "adGenRadiusAuthGroupVendorDescription": adGenRadiusAuthGroupVendorDescription,
       "adGenRadiusAuthGroupLastError": adGenRadiusAuthGroupLastError,
       "adGenRadiusAuthGroupDeadTime": adGenRadiusAuthGroupDeadTime,
       "adGenRadiusAuthGroupRowStatus": adGenRadiusAuthGroupRowStatus,
       "adGenRadiusAuthGroupTableLastError": adGenRadiusAuthGroupTableLastError,
       "adGenRadiusAuthGroupListTable": adGenRadiusAuthGroupListTable,
       "adGenRadiusAuthGroupListEntry": adGenRadiusAuthGroupListEntry,
       "adGenRadiusAuthGroupNameFixedLen": adGenRadiusAuthGroupNameFixedLen,
       "adGenRadiusAuthGroupListSeqIndex": adGenRadiusAuthGroupListSeqIndex,
       "adGenRadiusAuthGroupListServerName": adGenRadiusAuthGroupListServerName,
       "adGenRadiusAuthNumOfServersPerGroup": adGenRadiusAuthNumOfServersPerGroup,
       "adGenRadiusAuthServerTable": adGenRadiusAuthServerTable,
       "adGenRadiusAuthServerEntry": adGenRadiusAuthServerEntry,
       "adGenRadiusAuthServerName": adGenRadiusAuthServerName,
       "adGenRadiusAuthServerInetAddressType": adGenRadiusAuthServerInetAddressType,
       "adGenRadiusAuthServerInetAddress": adGenRadiusAuthServerInetAddress,
       "adGenRadiusAuthServerInetAddressPort": adGenRadiusAuthServerInetAddressPort,
       "adGenRadiusAuthServerSecret": adGenRadiusAuthServerSecret,
       "adGenRadiusAuthServerLastError": adGenRadiusAuthServerLastError,
       "adGenRadiusAuthServerRowStatus": adGenRadiusAuthServerRowStatus,
       "adGenRadiusAuthServerTableLastError": adGenRadiusAuthServerTableLastError,
       "adGenRadiusAuthRelayTable": adGenRadiusAuthRelayTable,
       "adGenRadiusAuthRelayEntry": adGenRadiusAuthRelayEntry,
       "adGenRadiusAuthRelayName": adGenRadiusAuthRelayName,
       "adGenRadiusAuthRelayIPHostIfIndex": adGenRadiusAuthRelayIPHostIfIndex,
       "adGenRadiusAuthRelayIPHostName": adGenRadiusAuthRelayIPHostName,
       "adGenRadiusAuthRelayNasId": adGenRadiusAuthRelayNasId,
       "adGenRadiusAuthRelayUserNameOverride": adGenRadiusAuthRelayUserNameOverride,
       "adGenRadiusAuthRelayNasIPOverride": adGenRadiusAuthRelayNasIPOverride,
       "adGenRadiusAuthRelayVendorSpecificId": adGenRadiusAuthRelayVendorSpecificId,
       "adGenRadiusAuthRelayVendorSpecificSubType": adGenRadiusAuthRelayVendorSpecificSubType,
       "adGenRadiusAuthRelayVendorSpecificSubValue": adGenRadiusAuthRelayVendorSpecificSubValue,
       "adGenRadiusAuthRelayLastError": adGenRadiusAuthRelayLastError,
       "adGenRadiusAuthRelayRowStatus": adGenRadiusAuthRelayRowStatus,
       "adGenRadiusAuthRelayOperStatus": adGenRadiusAuthRelayOperStatus,
       "adGenRadiusAuthRelayCallingStationIdDelim": adGenRadiusAuthRelayCallingStationIdDelim,
       "adGenRadiusAuthRelayAllowList": adGenRadiusAuthRelayAllowList,
       "adGenRadiusAuthRelayErrorTable": adGenRadiusAuthRelayErrorTable,
       "adGenRadiusAuthRelayErrorEntry": adGenRadiusAuthRelayErrorEntry,
       "adGenRadiusAuthRelayTableLastCreateError": adGenRadiusAuthRelayTableLastCreateError,
       "adGenRadiusAuthStatus": adGenRadiusAuthStatus,
       "adGenRadiusAuthStatusTable": adGenRadiusAuthStatusTable,
       "adGenRadiusAuthStatusEntry": adGenRadiusAuthStatusEntry,
       "adGenRadiusAuthStatusIfIndex": adGenRadiusAuthStatusIfIndex,
       "adGenRadiusAuthStatusIpHostNameFixedLen": adGenRadiusAuthStatusIpHostNameFixedLen,
       "adGenRadiusAuthStatusServerName": adGenRadiusAuthStatusServerName,
       "adGenRadiusAuthStatusInetAddressType": adGenRadiusAuthStatusInetAddressType,
       "adGenRadiusAuthStatusInetAddress": adGenRadiusAuthStatusInetAddress,
       "adGenRadiusAuthStatusInetPortNumber": adGenRadiusAuthStatusInetPortNumber,
       "adGenRadiusAuthStatusRoundTripTime": adGenRadiusAuthStatusRoundTripTime,
       "adGenRadiusAuthStatusAccessRequests": adGenRadiusAuthStatusAccessRequests,
       "adGenRadiusAuthStatusAccessRetransmissions": adGenRadiusAuthStatusAccessRetransmissions,
       "adGenRadiusAuthStatusAccessAccepts": adGenRadiusAuthStatusAccessAccepts,
       "adGenRadiusAuthStatusAccessRejects": adGenRadiusAuthStatusAccessRejects,
       "adGenRadiusAuthStatusAccessChallenges": adGenRadiusAuthStatusAccessChallenges,
       "adGenRadiusAuthStatusMalformedAccessResponses": adGenRadiusAuthStatusMalformedAccessResponses,
       "adGenRadiusAuthStatusBadAuthenticators": adGenRadiusAuthStatusBadAuthenticators,
       "adGenRadiusAuthStatusPendingRequests": adGenRadiusAuthStatusPendingRequests,
       "adGenRadiusAuthStatusTimeouts": adGenRadiusAuthStatusTimeouts,
       "adGenRadiusAuthStatusUnknownTypes": adGenRadiusAuthStatusUnknownTypes,
       "adGenRadiusAuthStatusPacketsDropped": adGenRadiusAuthStatusPacketsDropped,
       "adGenRadiusAuthStatusCounterDiscontinuity": adGenRadiusAuthStatusCounterDiscontinuity,
       "adGenRadiusAuthStatusServerState": adGenRadiusAuthStatusServerState,
       "adGenRadiusAuthMIB": adGenRadiusAuthMIB}
)
