# SNMP MIB module (EDGECORE-DHCPCL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/edgecore/EDGECORE-DHCPCL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:53:50 2025
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

(rnd,) = mibBuilder.importSymbols(
    "EDGECORE-MIB",
    "rnd")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

rlDhcpCl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76)
)
if mibBuilder.loadTexts:
    rlDhcpCl.setRevisions(
        ("2007-01-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlDhcpClActionTable_Object = MibTable
rlDhcpClActionTable = _RlDhcpClActionTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 3)
)
if mibBuilder.loadTexts:
    rlDhcpClActionTable.setStatus("current")
_RlDhcpClActionEntry_Object = MibTableRow
rlDhcpClActionEntry = _RlDhcpClActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 3, 1)
)
rlDhcpClActionEntry.setIndexNames(
    (0, "EDGECORE-DHCPCL-MIB", "rlDhcpClActionIfIndex"),
)
if mibBuilder.loadTexts:
    rlDhcpClActionEntry.setStatus("current")
_RlDhcpClActionIfIndex_Type = InterfaceIndex
_RlDhcpClActionIfIndex_Object = MibTableColumn
rlDhcpClActionIfIndex = _RlDhcpClActionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 3, 1, 1),
    _RlDhcpClActionIfIndex_Type()
)
rlDhcpClActionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClActionIfIndex.setStatus("current")
_RlDhcpClActionStatus_Type = RowStatus
_RlDhcpClActionStatus_Object = MibTableColumn
rlDhcpClActionStatus = _RlDhcpClActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 3, 1, 2),
    _RlDhcpClActionStatus_Type()
)
rlDhcpClActionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlDhcpClActionStatus.setStatus("current")


class _RlDhcpClActionHostName_Type(SnmpAdminString):
    """Custom type rlDhcpClActionHostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlDhcpClActionHostName_Type.__name__ = "SnmpAdminString"
_RlDhcpClActionHostName_Object = MibTableColumn
rlDhcpClActionHostName = _RlDhcpClActionHostName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 3, 1, 3),
    _RlDhcpClActionHostName_Type()
)
rlDhcpClActionHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlDhcpClActionHostName.setStatus("current")
_RlDhcpApprovalEnabled_Type = TruthValue
_RlDhcpApprovalEnabled_Object = MibScalar
rlDhcpApprovalEnabled = _RlDhcpApprovalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 4),
    _RlDhcpApprovalEnabled_Type()
)
rlDhcpApprovalEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalEnabled.setStatus("current")
_RlDhcpApprovalWaitingTable_Object = MibTable
rlDhcpApprovalWaitingTable = _RlDhcpApprovalWaitingTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 5)
)
if mibBuilder.loadTexts:
    rlDhcpApprovalWaitingTable.setStatus("current")
_RlDhcpApprovalWaitingEntry_Object = MibTableRow
rlDhcpApprovalWaitingEntry = _RlDhcpApprovalWaitingEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 5, 1)
)
rlDhcpApprovalWaitingEntry.setIndexNames(
    (0, "EDGECORE-DHCPCL-MIB", "rlDhcpApprovalWaitingIfIndex"),
)
if mibBuilder.loadTexts:
    rlDhcpApprovalWaitingEntry.setStatus("current")
_RlDhcpApprovalWaitingIfIndex_Type = InterfaceIndex
_RlDhcpApprovalWaitingIfIndex_Object = MibTableColumn
rlDhcpApprovalWaitingIfIndex = _RlDhcpApprovalWaitingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 5, 1, 1),
    _RlDhcpApprovalWaitingIfIndex_Type()
)
rlDhcpApprovalWaitingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalWaitingIfIndex.setStatus("current")
_RlDhcpApprovalWaitingAddress_Type = IpAddress
_RlDhcpApprovalWaitingAddress_Object = MibTableColumn
rlDhcpApprovalWaitingAddress = _RlDhcpApprovalWaitingAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 5, 1, 2),
    _RlDhcpApprovalWaitingAddress_Type()
)
rlDhcpApprovalWaitingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalWaitingAddress.setStatus("current")
_RlDhcpApprovalWaitingMask_Type = IpAddress
_RlDhcpApprovalWaitingMask_Object = MibTableColumn
rlDhcpApprovalWaitingMask = _RlDhcpApprovalWaitingMask_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 5, 1, 3),
    _RlDhcpApprovalWaitingMask_Type()
)
rlDhcpApprovalWaitingMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalWaitingMask.setStatus("current")
_RlDhcpApprovalWaitingGateway_Type = IpAddress
_RlDhcpApprovalWaitingGateway_Object = MibTableColumn
rlDhcpApprovalWaitingGateway = _RlDhcpApprovalWaitingGateway_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 5, 1, 4),
    _RlDhcpApprovalWaitingGateway_Type()
)
rlDhcpApprovalWaitingGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalWaitingGateway.setStatus("current")
_RlDhcpApprovalActionTable_Object = MibTable
rlDhcpApprovalActionTable = _RlDhcpApprovalActionTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 6)
)
if mibBuilder.loadTexts:
    rlDhcpApprovalActionTable.setStatus("current")
_RlDhcpApprovalActionEntry_Object = MibTableRow
rlDhcpApprovalActionEntry = _RlDhcpApprovalActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 6, 1)
)
rlDhcpApprovalActionEntry.setIndexNames(
    (0, "EDGECORE-DHCPCL-MIB", "rlDhcpApprovalActionIfIndex"),
    (0, "EDGECORE-DHCPCL-MIB", "rlDhcpApprovalActionAddress"),
    (0, "EDGECORE-DHCPCL-MIB", "rlDhcpApprovalActionMask"),
)
if mibBuilder.loadTexts:
    rlDhcpApprovalActionEntry.setStatus("current")
_RlDhcpApprovalActionIfIndex_Type = InterfaceIndex
_RlDhcpApprovalActionIfIndex_Object = MibTableColumn
rlDhcpApprovalActionIfIndex = _RlDhcpApprovalActionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 6, 1, 1),
    _RlDhcpApprovalActionIfIndex_Type()
)
rlDhcpApprovalActionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalActionIfIndex.setStatus("current")
_RlDhcpApprovalActionAddress_Type = IpAddress
_RlDhcpApprovalActionAddress_Object = MibTableColumn
rlDhcpApprovalActionAddress = _RlDhcpApprovalActionAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 6, 1, 2),
    _RlDhcpApprovalActionAddress_Type()
)
rlDhcpApprovalActionAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalActionAddress.setStatus("current")
_RlDhcpApprovalActionMask_Type = IpAddress
_RlDhcpApprovalActionMask_Object = MibTableColumn
rlDhcpApprovalActionMask = _RlDhcpApprovalActionMask_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 6, 1, 3),
    _RlDhcpApprovalActionMask_Type()
)
rlDhcpApprovalActionMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalActionMask.setStatus("current")
_RlDhcpApprovalActionApprove_Type = TruthValue
_RlDhcpApprovalActionApprove_Object = MibTableColumn
rlDhcpApprovalActionApprove = _RlDhcpApprovalActionApprove_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 6, 1, 4),
    _RlDhcpApprovalActionApprove_Type()
)
rlDhcpApprovalActionApprove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpApprovalActionApprove.setStatus("current")
_RlDhcpClCommandTable_Object = MibTable
rlDhcpClCommandTable = _RlDhcpClCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 7)
)
if mibBuilder.loadTexts:
    rlDhcpClCommandTable.setStatus("current")
_RlDhcpClCommandEntry_Object = MibTableRow
rlDhcpClCommandEntry = _RlDhcpClCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 7, 1)
)
rlDhcpClCommandEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlDhcpClCommandEntry.setStatus("current")


class _RlDhcpClCommandAction_Type(Integer32):
    """Custom type rlDhcpClCommandAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("renew", 1),
          ("renewForceAutoconfig", 2))
    )


_RlDhcpClCommandAction_Type.__name__ = "Integer32"
_RlDhcpClCommandAction_Object = MibTableColumn
rlDhcpClCommandAction = _RlDhcpClCommandAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 7, 1, 2),
    _RlDhcpClCommandAction_Type()
)
rlDhcpClCommandAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClCommandAction.setStatus("current")


class _RlDhcpClConfigurationFileName_Type(DisplayString):
    """Custom type rlDhcpClConfigurationFileName based on DisplayString"""
    defaultValue = OctetString("")


_RlDhcpClConfigurationFileName_Type.__name__ = "DisplayString"
_RlDhcpClConfigurationFileName_Object = MibScalar
rlDhcpClConfigurationFileName = _RlDhcpClConfigurationFileName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 8),
    _RlDhcpClConfigurationFileName_Type()
)
rlDhcpClConfigurationFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClConfigurationFileName.setStatus("current")


class _RlDhcpClOption67Enable_Type(Integer32):
    """Custom type rlDhcpClOption67Enable based on Integer32"""
    defaultValue = 1

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


_RlDhcpClOption67Enable_Type.__name__ = "Integer32"
_RlDhcpClOption67Enable_Object = MibScalar
rlDhcpClOption67Enable = _RlDhcpClOption67Enable_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 9),
    _RlDhcpClOption67Enable_Type()
)
rlDhcpClOption67Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClOption67Enable.setStatus("current")
_RlDhcpClManualTftpServerAddress_Type = IpAddress
_RlDhcpClManualTftpServerAddress_Object = MibScalar
rlDhcpClManualTftpServerAddress = _RlDhcpClManualTftpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 10),
    _RlDhcpClManualTftpServerAddress_Type()
)
rlDhcpClManualTftpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClManualTftpServerAddress.setStatus("current")
_RlDhcpClSelectedTftpServerAddress_Type = IpAddress
_RlDhcpClSelectedTftpServerAddress_Object = MibScalar
rlDhcpClSelectedTftpServerAddress = _RlDhcpClSelectedTftpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 11),
    _RlDhcpClSelectedTftpServerAddress_Type()
)
rlDhcpClSelectedTftpServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClSelectedTftpServerAddress.setStatus("current")


class _RlDhcpClSelectedTftpServerAddressOrigin_Type(Integer32):
    """Custom type rlDhcpClSelectedTftpServerAddressOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("sname", 1),
          ("option66", 2),
          ("option150", 3),
          ("option129", 4),
          ("siaddr", 5),
          ("manual", 6),
          ("unknown", 7),
          ("none", 8))
    )


_RlDhcpClSelectedTftpServerAddressOrigin_Type.__name__ = "Integer32"
_RlDhcpClSelectedTftpServerAddressOrigin_Object = MibScalar
rlDhcpClSelectedTftpServerAddressOrigin = _RlDhcpClSelectedTftpServerAddressOrigin_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 12),
    _RlDhcpClSelectedTftpServerAddressOrigin_Type()
)
rlDhcpClSelectedTftpServerAddressOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClSelectedTftpServerAddressOrigin.setStatus("current")


class _RlDhcpClManualConfigurationFileName_Type(DisplayString):
    """Custom type rlDhcpClManualConfigurationFileName based on DisplayString"""
    defaultValue = OctetString("")


_RlDhcpClManualConfigurationFileName_Type.__name__ = "DisplayString"
_RlDhcpClManualConfigurationFileName_Object = MibScalar
rlDhcpClManualConfigurationFileName = _RlDhcpClManualConfigurationFileName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 13),
    _RlDhcpClManualConfigurationFileName_Type()
)
rlDhcpClManualConfigurationFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClManualConfigurationFileName.setStatus("current")
_RlDhcpClSelectedConfigurationFileName_Type = DisplayString
_RlDhcpClSelectedConfigurationFileName_Object = MibScalar
rlDhcpClSelectedConfigurationFileName = _RlDhcpClSelectedConfigurationFileName_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 14),
    _RlDhcpClSelectedConfigurationFileName_Type()
)
rlDhcpClSelectedConfigurationFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClSelectedConfigurationFileName.setStatus("current")


class _RlDhcpClSelectedConfigurationFileNameOrigin_Type(Integer32):
    """Custom type rlDhcpClSelectedConfigurationFileNameOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("file", 1),
          ("option67", 2),
          ("manual", 3),
          ("none", 4),
          ("hostname", 5),
          ("defaultConfigFile", 6))
    )


_RlDhcpClSelectedConfigurationFileNameOrigin_Type.__name__ = "Integer32"
_RlDhcpClSelectedConfigurationFileNameOrigin_Object = MibScalar
rlDhcpClSelectedConfigurationFileNameOrigin = _RlDhcpClSelectedConfigurationFileNameOrigin_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 15),
    _RlDhcpClSelectedConfigurationFileNameOrigin_Type()
)
rlDhcpClSelectedConfigurationFileNameOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClSelectedConfigurationFileNameOrigin.setStatus("current")


class _RlDhcpClEnabledByDefaultRemovedIfindex_Type(Integer32):
    """Custom type rlDhcpClEnabledByDefaultRemovedIfindex based on Integer32"""
    defaultValue = 0


_RlDhcpClEnabledByDefaultRemovedIfindex_Type.__name__ = "Integer32"
_RlDhcpClEnabledByDefaultRemovedIfindex_Object = MibScalar
rlDhcpClEnabledByDefaultRemovedIfindex = _RlDhcpClEnabledByDefaultRemovedIfindex_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 16),
    _RlDhcpClEnabledByDefaultRemovedIfindex_Type()
)
rlDhcpClEnabledByDefaultRemovedIfindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClEnabledByDefaultRemovedIfindex.setStatus("current")
_RlDhcpClAutoUpdateEnabled_Type = TruthValue
_RlDhcpClAutoUpdateEnabled_Object = MibScalar
rlDhcpClAutoUpdateEnabled = _RlDhcpClAutoUpdateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 17),
    _RlDhcpClAutoUpdateEnabled_Type()
)
rlDhcpClAutoUpdateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClAutoUpdateEnabled.setStatus("current")


class _RlDhcpClAutoUpdateStatus_Type(Integer32):
    """Custom type rlDhcpClAutoUpdateStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("noData", 1),
          ("openingIndirectFile", 2),
          ("downloadedIndirectFile", 3),
          ("startDownloadImageFile", 4),
          ("failedToDownloadImageFile", 5),
          ("quitFileContentsLenZero", 6),
          ("quitImageFileNameLenZero", 7),
          ("quitVersionAlreadyUpdated", 8),
          ("quitIndirectFileNotFound", 9),
          ("quitImageFileNotFound", 10),
          ("quitImageVersionNotSupported", 11),
          ("quitNoTftpOutgoingInterface", 12))
    )


_RlDhcpClAutoUpdateStatus_Type.__name__ = "Integer32"
_RlDhcpClAutoUpdateStatus_Object = MibScalar
rlDhcpClAutoUpdateStatus = _RlDhcpClAutoUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 18),
    _RlDhcpClAutoUpdateStatus_Type()
)
rlDhcpClAutoUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClAutoUpdateStatus.setStatus("current")
_RlDhcpClAutoConfigForce_Type = TruthValue
_RlDhcpClAutoConfigForce_Object = MibScalar
rlDhcpClAutoConfigForce = _RlDhcpClAutoConfigForce_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 19),
    _RlDhcpClAutoConfigForce_Type()
)
rlDhcpClAutoConfigForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClAutoConfigForce.setStatus("current")
_RlDhcpClAutoConfigAutoSave_Type = TruthValue
_RlDhcpClAutoConfigAutoSave_Object = MibScalar
rlDhcpClAutoConfigAutoSave = _RlDhcpClAutoConfigAutoSave_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 20),
    _RlDhcpClAutoConfigAutoSave_Type()
)
rlDhcpClAutoConfigAutoSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClAutoConfigAutoSave.setStatus("current")


class _RlDhcpClAutoConfigStatus_Type(Integer32):
    """Custom type rlDhcpClAutoConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("noData", 1),
          ("openingDhcpConfigFile", 2),
          ("openingIndirectFile", 3),
          ("searchingHostnameInIndirectFile", 4),
          ("openingHostnameConfigFile", 5),
          ("openingHostnameCfgFile", 6),
          ("openingDefaultConfigFile", 7),
          ("downloadingConfigFile", 8),
          ("savingConfigInStartupCDB", 9),
          ("quitDhcpFileNotGivenOrNotExists", 10),
          ("quitFailedToFindAnyExistingConfigFile", 11),
          ("quitConfigFileContentsLenZero", 12),
          ("quitConfigFileDownloadFailed", 13),
          ("quitConditionsForAutoConfigChanged", 14),
          ("quitSelectedConfigFileNameUpdateFailed", 15),
          ("quitSelectedConfigFileNameOriginUpdateFailed", 16),
          ("quitSelectedTftpServerAddressUpdateFailed", 17),
          ("quitSelectedTftpServerAddressOriginUpdateFailed", 18),
          ("quitCopyRunningToStartupFailed", 19),
          ("quitNoTftpOutgoingInterface", 20),
          ("finishedSuccessfully", 21))
    )


_RlDhcpClAutoConfigStatus_Type.__name__ = "Integer32"
_RlDhcpClAutoConfigStatus_Object = MibScalar
rlDhcpClAutoConfigStatus = _RlDhcpClAutoConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 10, 1, 14, 89, 76, 21),
    _RlDhcpClAutoConfigStatus_Type()
)
rlDhcpClAutoConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClAutoConfigStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EDGECORE-DHCPCL-MIB",
    **{"rlDhcpCl": rlDhcpCl,
       "rlDhcpClActionTable": rlDhcpClActionTable,
       "rlDhcpClActionEntry": rlDhcpClActionEntry,
       "rlDhcpClActionIfIndex": rlDhcpClActionIfIndex,
       "rlDhcpClActionStatus": rlDhcpClActionStatus,
       "rlDhcpClActionHostName": rlDhcpClActionHostName,
       "rlDhcpApprovalEnabled": rlDhcpApprovalEnabled,
       "rlDhcpApprovalWaitingTable": rlDhcpApprovalWaitingTable,
       "rlDhcpApprovalWaitingEntry": rlDhcpApprovalWaitingEntry,
       "rlDhcpApprovalWaitingIfIndex": rlDhcpApprovalWaitingIfIndex,
       "rlDhcpApprovalWaitingAddress": rlDhcpApprovalWaitingAddress,
       "rlDhcpApprovalWaitingMask": rlDhcpApprovalWaitingMask,
       "rlDhcpApprovalWaitingGateway": rlDhcpApprovalWaitingGateway,
       "rlDhcpApprovalActionTable": rlDhcpApprovalActionTable,
       "rlDhcpApprovalActionEntry": rlDhcpApprovalActionEntry,
       "rlDhcpApprovalActionIfIndex": rlDhcpApprovalActionIfIndex,
       "rlDhcpApprovalActionAddress": rlDhcpApprovalActionAddress,
       "rlDhcpApprovalActionMask": rlDhcpApprovalActionMask,
       "rlDhcpApprovalActionApprove": rlDhcpApprovalActionApprove,
       "rlDhcpClCommandTable": rlDhcpClCommandTable,
       "rlDhcpClCommandEntry": rlDhcpClCommandEntry,
       "rlDhcpClCommandAction": rlDhcpClCommandAction,
       "rlDhcpClConfigurationFileName": rlDhcpClConfigurationFileName,
       "rlDhcpClOption67Enable": rlDhcpClOption67Enable,
       "rlDhcpClManualTftpServerAddress": rlDhcpClManualTftpServerAddress,
       "rlDhcpClSelectedTftpServerAddress": rlDhcpClSelectedTftpServerAddress,
       "rlDhcpClSelectedTftpServerAddressOrigin": rlDhcpClSelectedTftpServerAddressOrigin,
       "rlDhcpClManualConfigurationFileName": rlDhcpClManualConfigurationFileName,
       "rlDhcpClSelectedConfigurationFileName": rlDhcpClSelectedConfigurationFileName,
       "rlDhcpClSelectedConfigurationFileNameOrigin": rlDhcpClSelectedConfigurationFileNameOrigin,
       "rlDhcpClEnabledByDefaultRemovedIfindex": rlDhcpClEnabledByDefaultRemovedIfindex,
       "rlDhcpClAutoUpdateEnabled": rlDhcpClAutoUpdateEnabled,
       "rlDhcpClAutoUpdateStatus": rlDhcpClAutoUpdateStatus,
       "rlDhcpClAutoConfigForce": rlDhcpClAutoConfigForce,
       "rlDhcpClAutoConfigAutoSave": rlDhcpClAutoConfigAutoSave,
       "rlDhcpClAutoConfigStatus": rlDhcpClAutoConfigStatus}
)
