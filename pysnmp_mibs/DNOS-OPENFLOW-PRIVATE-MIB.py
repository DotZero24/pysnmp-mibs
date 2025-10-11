# SNMP MIB module (DNOS-OPENFLOW-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/dell/DNOS-OPENFLOW-PRIVATE-MIB
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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

fastPathOpenFlow = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56)
)
if mibBuilder.loadTexts:
    fastPathOpenFlow.setRevisions(
        ("2011-03-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentOpenFlowGroup_ObjectIdentity = ObjectIdentity
agentOpenFlowGroup = _AgentOpenFlowGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1)
)
_AgentOpenFlowGlobalConfigGroup_ObjectIdentity = ObjectIdentity
agentOpenFlowGlobalConfigGroup = _AgentOpenFlowGlobalConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 1)
)


class _AgentOpenFlowAdminMode_Type(Integer32):
    """Custom type agentOpenFlowAdminMode based on Integer32"""
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


_AgentOpenFlowAdminMode_Type.__name__ = "Integer32"
_AgentOpenFlowAdminMode_Object = MibScalar
agentOpenFlowAdminMode = _AgentOpenFlowAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 1, 1),
    _AgentOpenFlowAdminMode_Type()
)
agentOpenFlowAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOpenFlowAdminMode.setStatus("current")


class _AgentOpenFlowVariant_Type(Integer32):
    """Custom type agentOpenFlowVariant based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tenantNetworkingMode", 1),
          ("openFlow10Mode", 2),
          ("openFlow13Mode", 3))
    )


_AgentOpenFlowVariant_Type.__name__ = "Integer32"
_AgentOpenFlowVariant_Object = MibScalar
agentOpenFlowVariant = _AgentOpenFlowVariant_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 1, 2),
    _AgentOpenFlowVariant_Type()
)
agentOpenFlowVariant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOpenFlowVariant.setStatus("current")


class _AgentOpenFlowDefaultTable_Type(Integer32):
    """Custom type agentOpenFlowDefaultTable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fullMatch", 1),
          ("layerTwoMatch", 2))
    )


_AgentOpenFlowDefaultTable_Type.__name__ = "Integer32"
_AgentOpenFlowDefaultTable_Object = MibScalar
agentOpenFlowDefaultTable = _AgentOpenFlowDefaultTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 1, 3),
    _AgentOpenFlowDefaultTable_Type()
)
agentOpenFlowDefaultTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOpenFlowDefaultTable.setStatus("deprecated")


class _AgentOpenFlowStaticIPAssignmentMode_Type(Integer32):
    """Custom type agentOpenFlowStaticIPAssignmentMode based on Integer32"""
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


_AgentOpenFlowStaticIPAssignmentMode_Type.__name__ = "Integer32"
_AgentOpenFlowStaticIPAssignmentMode_Object = MibScalar
agentOpenFlowStaticIPAssignmentMode = _AgentOpenFlowStaticIPAssignmentMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 1, 4),
    _AgentOpenFlowStaticIPAssignmentMode_Type()
)
agentOpenFlowStaticIPAssignmentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOpenFlowStaticIPAssignmentMode.setStatus("obsolete")
_AgentOpenFlowGlobalConfigIPAddress_Type = IpAddress
_AgentOpenFlowGlobalConfigIPAddress_Object = MibScalar
agentOpenFlowGlobalConfigIPAddress = _AgentOpenFlowGlobalConfigIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 1, 5),
    _AgentOpenFlowGlobalConfigIPAddress_Type()
)
agentOpenFlowGlobalConfigIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOpenFlowGlobalConfigIPAddress.setStatus("current")


class _AgentOpenFlowNetworkMTU_Type(Unsigned32):
    """Custom type agentOpenFlowNetworkMTU based on Unsigned32"""
    defaultValue = 1518

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9216),
    )


_AgentOpenFlowNetworkMTU_Type.__name__ = "Unsigned32"
_AgentOpenFlowNetworkMTU_Object = MibScalar
agentOpenFlowNetworkMTU = _AgentOpenFlowNetworkMTU_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 1, 6),
    _AgentOpenFlowNetworkMTU_Type()
)
agentOpenFlowNetworkMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOpenFlowNetworkMTU.setStatus("obsolete")


class _AgentOpenFlowIPAssignmentMode_Type(Integer32):
    """Custom type agentOpenFlowIPAssignmentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("static", 1),
          ("serviceport", 2))
    )


_AgentOpenFlowIPAssignmentMode_Type.__name__ = "Integer32"
_AgentOpenFlowIPAssignmentMode_Object = MibScalar
agentOpenFlowIPAssignmentMode = _AgentOpenFlowIPAssignmentMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 1, 7),
    _AgentOpenFlowIPAssignmentMode_Type()
)
agentOpenFlowIPAssignmentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOpenFlowIPAssignmentMode.setStatus("current")
_AgentOpenFlowCfgControllerTable_Object = MibTable
agentOpenFlowCfgControllerTable = _AgentOpenFlowCfgControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 3)
)
if mibBuilder.loadTexts:
    agentOpenFlowCfgControllerTable.setStatus("current")
_AgentOpenFlowCfgControllerEntry_Object = MibTableRow
agentOpenFlowCfgControllerEntry = _AgentOpenFlowCfgControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 3, 1)
)
agentOpenFlowCfgControllerEntry.setIndexNames(
    (0, "DNOS-OPENFLOW-PRIVATE-MIB", "agentOpenFlowCfgCtrlIPAddress"),
    (0, "DNOS-OPENFLOW-PRIVATE-MIB", "agentOpenFlowCfgCtrlIPPort"),
)
if mibBuilder.loadTexts:
    agentOpenFlowCfgControllerEntry.setStatus("current")
_AgentOpenFlowCfgCtrlIPAddress_Type = IpAddress
_AgentOpenFlowCfgCtrlIPAddress_Object = MibTableColumn
agentOpenFlowCfgCtrlIPAddress = _AgentOpenFlowCfgCtrlIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 3, 1, 1),
    _AgentOpenFlowCfgCtrlIPAddress_Type()
)
agentOpenFlowCfgCtrlIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentOpenFlowCfgCtrlIPAddress.setStatus("current")


class _AgentOpenFlowCfgCtrlIPPort_Type(Unsigned32):
    """Custom type agentOpenFlowCfgCtrlIPPort based on Unsigned32"""
    defaultValue = 6632

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentOpenFlowCfgCtrlIPPort_Type.__name__ = "Unsigned32"
_AgentOpenFlowCfgCtrlIPPort_Object = MibTableColumn
agentOpenFlowCfgCtrlIPPort = _AgentOpenFlowCfgCtrlIPPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 3, 1, 2),
    _AgentOpenFlowCfgCtrlIPPort_Type()
)
agentOpenFlowCfgCtrlIPPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentOpenFlowCfgCtrlIPPort.setStatus("current")


class _AgentOpenFlowCfgCtrlConnectionMode_Type(Integer32):
    """Custom type agentOpenFlowCfgCtrlConnectionMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ssl", 1),
          ("tcp", 2))
    )


_AgentOpenFlowCfgCtrlConnectionMode_Type.__name__ = "Integer32"
_AgentOpenFlowCfgCtrlConnectionMode_Object = MibTableColumn
agentOpenFlowCfgCtrlConnectionMode = _AgentOpenFlowCfgCtrlConnectionMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 3, 1, 3),
    _AgentOpenFlowCfgCtrlConnectionMode_Type()
)
agentOpenFlowCfgCtrlConnectionMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentOpenFlowCfgCtrlConnectionMode.setStatus("current")
_AgentOpenFlowCfgCtrlStatus_Type = RowStatus
_AgentOpenFlowCfgCtrlStatus_Object = MibTableColumn
agentOpenFlowCfgCtrlStatus = _AgentOpenFlowCfgCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 3, 1, 4),
    _AgentOpenFlowCfgCtrlStatus_Type()
)
agentOpenFlowCfgCtrlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentOpenFlowCfgCtrlStatus.setStatus("current")
_AgentOpenFlowCfgCtrlRole_Type = DisplayString
_AgentOpenFlowCfgCtrlRole_Object = MibTableColumn
agentOpenFlowCfgCtrlRole = _AgentOpenFlowCfgCtrlRole_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 3, 1, 5),
    _AgentOpenFlowCfgCtrlRole_Type()
)
agentOpenFlowCfgCtrlRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowCfgCtrlRole.setStatus("current")
_AgentOpenFlowGlobalStatusParameters_ObjectIdentity = ObjectIdentity
agentOpenFlowGlobalStatusParameters = _AgentOpenFlowGlobalStatusParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 6)
)


class _AgentOpenFlowOperationalStatus_Type(Integer32):
    """Custom type agentOpenFlowOperationalStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("enablePending", 3),
          ("disablePending", 4))
    )


_AgentOpenFlowOperationalStatus_Type.__name__ = "Integer32"
_AgentOpenFlowOperationalStatus_Object = MibScalar
agentOpenFlowOperationalStatus = _AgentOpenFlowOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 6, 1),
    _AgentOpenFlowOperationalStatus_Type()
)
agentOpenFlowOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowOperationalStatus.setStatus("current")


class _AgentOpenFlowDisableReason_Type(Integer32):
    """Custom type agentOpenFlowDisableReason based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("administrativelyDisabled", 2),
          ("noSuitableIPInterface", 3),
          ("noSSLCertificates", 4))
    )


_AgentOpenFlowDisableReason_Type.__name__ = "Integer32"
_AgentOpenFlowDisableReason_Object = MibScalar
agentOpenFlowDisableReason = _AgentOpenFlowDisableReason_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 6, 2),
    _AgentOpenFlowDisableReason_Type()
)
agentOpenFlowDisableReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowDisableReason.setStatus("current")
_AgentOpenFlowGlobalCommands_ObjectIdentity = ObjectIdentity
agentOpenFlowGlobalCommands = _AgentOpenFlowGlobalCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 7)
)


class _AgentOpenFlowEraseOpenFlowManagerCertificates_Type(Integer32):
    """Custom type agentOpenFlowEraseOpenFlowManagerCertificates based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alwaysReturnedOnRead", 1),
          ("eraseCertificates", 2))
    )


_AgentOpenFlowEraseOpenFlowManagerCertificates_Type.__name__ = "Integer32"
_AgentOpenFlowEraseOpenFlowManagerCertificates_Object = MibScalar
agentOpenFlowEraseOpenFlowManagerCertificates = _AgentOpenFlowEraseOpenFlowManagerCertificates_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 7, 1),
    _AgentOpenFlowEraseOpenFlowManagerCertificates_Type()
)
agentOpenFlowEraseOpenFlowManagerCertificates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOpenFlowEraseOpenFlowManagerCertificates.setStatus("current")
_AgentOpenFlowFlowTableStatusTable_Object = MibTable
agentOpenFlowFlowTableStatusTable = _AgentOpenFlowFlowTableStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 8)
)
if mibBuilder.loadTexts:
    agentOpenFlowFlowTableStatusTable.setStatus("current")
_AgentOpenFlowFlowTableStatusEntry_Object = MibTableRow
agentOpenFlowFlowTableStatusEntry = _AgentOpenFlowFlowTableStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 8, 1)
)
agentOpenFlowFlowTableStatusEntry.setIndexNames(
    (0, "DNOS-OPENFLOW-PRIVATE-MIB", "agentOpenFlowFlowTable"),
)
if mibBuilder.loadTexts:
    agentOpenFlowFlowTableStatusEntry.setStatus("current")


class _AgentOpenFlowFlowTable_Type(Unsigned32):
    """Custom type agentOpenFlowFlowTable based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentOpenFlowFlowTable_Type.__name__ = "Unsigned32"
_AgentOpenFlowFlowTable_Object = MibTableColumn
agentOpenFlowFlowTable = _AgentOpenFlowFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 8, 1, 1),
    _AgentOpenFlowFlowTable_Type()
)
agentOpenFlowFlowTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowFlowTable.setStatus("current")


class _AgentOpenFlowFlowTableName_Type(OctetString):
    """Custom type agentOpenFlowFlowTableName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AgentOpenFlowFlowTableName_Type.__name__ = "OctetString"
_AgentOpenFlowFlowTableName_Object = MibTableColumn
agentOpenFlowFlowTableName = _AgentOpenFlowFlowTableName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 8, 1, 2),
    _AgentOpenFlowFlowTableName_Type()
)
agentOpenFlowFlowTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowFlowTableName.setStatus("current")


class _AgentOpenFlowFlowTableDescription_Type(OctetString):
    """Custom type agentOpenFlowFlowTableDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_AgentOpenFlowFlowTableDescription_Type.__name__ = "OctetString"
_AgentOpenFlowFlowTableDescription_Object = MibTableColumn
agentOpenFlowFlowTableDescription = _AgentOpenFlowFlowTableDescription_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 8, 1, 3),
    _AgentOpenFlowFlowTableDescription_Type()
)
agentOpenFlowFlowTableDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowFlowTableDescription.setStatus("current")
_AgentOpenFlowMaximumSize_Type = Unsigned32
_AgentOpenFlowMaximumSize_Object = MibTableColumn
agentOpenFlowMaximumSize = _AgentOpenFlowMaximumSize_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 8, 1, 4),
    _AgentOpenFlowMaximumSize_Type()
)
agentOpenFlowMaximumSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowMaximumSize.setStatus("current")
_AgentOpenFlowNumberOfEntries_Type = Unsigned32
_AgentOpenFlowNumberOfEntries_Object = MibTableColumn
agentOpenFlowNumberOfEntries = _AgentOpenFlowNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 8, 1, 5),
    _AgentOpenFlowNumberOfEntries_Type()
)
agentOpenFlowNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowNumberOfEntries.setStatus("current")
_AgentOpenFlowHardwareEntries_Type = Unsigned32
_AgentOpenFlowHardwareEntries_Object = MibTableColumn
agentOpenFlowHardwareEntries = _AgentOpenFlowHardwareEntries_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 8, 1, 6),
    _AgentOpenFlowHardwareEntries_Type()
)
agentOpenFlowHardwareEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowHardwareEntries.setStatus("current")
_AgentOpenFlowSoftwareOnlyEntries_Type = Unsigned32
_AgentOpenFlowSoftwareOnlyEntries_Object = MibTableColumn
agentOpenFlowSoftwareOnlyEntries = _AgentOpenFlowSoftwareOnlyEntries_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 8, 1, 7),
    _AgentOpenFlowSoftwareOnlyEntries_Type()
)
agentOpenFlowSoftwareOnlyEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowSoftwareOnlyEntries.setStatus("current")
_AgentOpenFlowWaitingForSpaceEntries_Type = Unsigned32
_AgentOpenFlowWaitingForSpaceEntries_Object = MibTableColumn
agentOpenFlowWaitingForSpaceEntries = _AgentOpenFlowWaitingForSpaceEntries_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 8, 1, 8),
    _AgentOpenFlowWaitingForSpaceEntries_Type()
)
agentOpenFlowWaitingForSpaceEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowWaitingForSpaceEntries.setStatus("current")
_AgentOpenFlowFlowInsertionCount_Type = Unsigned32
_AgentOpenFlowFlowInsertionCount_Object = MibTableColumn
agentOpenFlowFlowInsertionCount = _AgentOpenFlowFlowInsertionCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 8, 1, 9),
    _AgentOpenFlowFlowInsertionCount_Type()
)
agentOpenFlowFlowInsertionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowFlowInsertionCount.setStatus("current")
_AgentOpenFlowFlowDeletionCount_Type = Unsigned32
_AgentOpenFlowFlowDeletionCount_Object = MibTableColumn
agentOpenFlowFlowDeletionCount = _AgentOpenFlowFlowDeletionCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 8, 1, 10),
    _AgentOpenFlowFlowDeletionCount_Type()
)
agentOpenFlowFlowDeletionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowFlowDeletionCount.setStatus("current")
_AgentOpenFlowInsertionFailureCount_Type = Unsigned32
_AgentOpenFlowInsertionFailureCount_Object = MibTableColumn
agentOpenFlowInsertionFailureCount = _AgentOpenFlowInsertionFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 8, 1, 11),
    _AgentOpenFlowInsertionFailureCount_Type()
)
agentOpenFlowInsertionFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowInsertionFailureCount.setStatus("current")
_AgentOpenFlowInstalledGroupEntry_ObjectIdentity = ObjectIdentity
agentOpenFlowInstalledGroupEntry = _AgentOpenFlowInstalledGroupEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 9)
)
_AgentOpenFlowGrpIndirectMaxEntries_Type = Unsigned32
_AgentOpenFlowGrpIndirectMaxEntries_Object = MibScalar
agentOpenFlowGrpIndirectMaxEntries = _AgentOpenFlowGrpIndirectMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 9, 1),
    _AgentOpenFlowGrpIndirectMaxEntries_Type()
)
agentOpenFlowGrpIndirectMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowGrpIndirectMaxEntries.setStatus("current")
_AgentOpenFlowGrpIndirectCurrentEntries_Type = Unsigned32
_AgentOpenFlowGrpIndirectCurrentEntries_Object = MibScalar
agentOpenFlowGrpIndirectCurrentEntries = _AgentOpenFlowGrpIndirectCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 9, 2),
    _AgentOpenFlowGrpIndirectCurrentEntries_Type()
)
agentOpenFlowGrpIndirectCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowGrpIndirectCurrentEntries.setStatus("current")
_AgentOpenFlowGrpAllMaxEntries_Type = Unsigned32
_AgentOpenFlowGrpAllMaxEntries_Object = MibScalar
agentOpenFlowGrpAllMaxEntries = _AgentOpenFlowGrpAllMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 9, 3),
    _AgentOpenFlowGrpAllMaxEntries_Type()
)
agentOpenFlowGrpAllMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowGrpAllMaxEntries.setStatus("current")
_AgentOpenFlowGrpAllCurrentEntries_Type = Unsigned32
_AgentOpenFlowGrpAllCurrentEntries_Object = MibScalar
agentOpenFlowGrpAllCurrentEntries = _AgentOpenFlowGrpAllCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 9, 4),
    _AgentOpenFlowGrpAllCurrentEntries_Type()
)
agentOpenFlowGrpAllCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowGrpAllCurrentEntries.setStatus("current")
_AgentOpenFlowGrpSelectMaxEntries_Type = Unsigned32
_AgentOpenFlowGrpSelectMaxEntries_Object = MibScalar
agentOpenFlowGrpSelectMaxEntries = _AgentOpenFlowGrpSelectMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 9, 5),
    _AgentOpenFlowGrpSelectMaxEntries_Type()
)
agentOpenFlowGrpSelectMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowGrpSelectMaxEntries.setStatus("current")
_AgentOpenFlowGrpSelectCurrentEntries_Type = Unsigned32
_AgentOpenFlowGrpSelectCurrentEntries_Object = MibScalar
agentOpenFlowGrpSelectCurrentEntries = _AgentOpenFlowGrpSelectCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 9, 6),
    _AgentOpenFlowGrpSelectCurrentEntries_Type()
)
agentOpenFlowGrpSelectCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowGrpSelectCurrentEntries.setStatus("current")
_AgentOpenFlowGroupDetailsTable_Object = MibTable
agentOpenFlowGroupDetailsTable = _AgentOpenFlowGroupDetailsTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 10)
)
if mibBuilder.loadTexts:
    agentOpenFlowGroupDetailsTable.setStatus("current")
_AgentOpenFlowGroupDetailsEntry_Object = MibTableRow
agentOpenFlowGroupDetailsEntry = _AgentOpenFlowGroupDetailsEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 10, 1)
)
agentOpenFlowGroupDetailsEntry.setIndexNames(
    (0, "DNOS-OPENFLOW-PRIVATE-MIB", "agentOpenFlowGroupId"),
)
if mibBuilder.loadTexts:
    agentOpenFlowGroupDetailsEntry.setStatus("current")


class _AgentOpenFlowGroupId_Type(Unsigned32):
    """Custom type agentOpenFlowGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentOpenFlowGroupId_Type.__name__ = "Unsigned32"
_AgentOpenFlowGroupId_Object = MibTableColumn
agentOpenFlowGroupId = _AgentOpenFlowGroupId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 10, 1, 1),
    _AgentOpenFlowGroupId_Type()
)
agentOpenFlowGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowGroupId.setStatus("current")
_AgentOpenFlowGroupType_Type = DisplayString
_AgentOpenFlowGroupType_Object = MibTableColumn
agentOpenFlowGroupType = _AgentOpenFlowGroupType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 10, 1, 2),
    _AgentOpenFlowGroupType_Type()
)
agentOpenFlowGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowGroupType.setStatus("current")


class _AgentOpenFlowGroupRefCount_Type(Unsigned32):
    """Custom type agentOpenFlowGroupRefCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentOpenFlowGroupRefCount_Type.__name__ = "Unsigned32"
_AgentOpenFlowGroupRefCount_Object = MibTableColumn
agentOpenFlowGroupRefCount = _AgentOpenFlowGroupRefCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 10, 1, 3),
    _AgentOpenFlowGroupRefCount_Type()
)
agentOpenFlowGroupRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowGroupRefCount.setStatus("current")


class _AgentOpenFlowGroupDuration_Type(Unsigned32):
    """Custom type agentOpenFlowGroupDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentOpenFlowGroupDuration_Type.__name__ = "Unsigned32"
_AgentOpenFlowGroupDuration_Object = MibTableColumn
agentOpenFlowGroupDuration = _AgentOpenFlowGroupDuration_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 10, 1, 4),
    _AgentOpenFlowGroupDuration_Type()
)
agentOpenFlowGroupDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowGroupDuration.setStatus("current")


class _AgentOpenFlowGroupBucketCount_Type(Unsigned32):
    """Custom type agentOpenFlowGroupBucketCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentOpenFlowGroupBucketCount_Type.__name__ = "Unsigned32"
_AgentOpenFlowGroupBucketCount_Object = MibTableColumn
agentOpenFlowGroupBucketCount = _AgentOpenFlowGroupBucketCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 10, 1, 5),
    _AgentOpenFlowGroupBucketCount_Type()
)
agentOpenFlowGroupBucketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowGroupBucketCount.setStatus("current")
_AgentOpenFlowGroupBucketDetailsTable_Object = MibTable
agentOpenFlowGroupBucketDetailsTable = _AgentOpenFlowGroupBucketDetailsTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 11)
)
if mibBuilder.loadTexts:
    agentOpenFlowGroupBucketDetailsTable.setStatus("current")
_AgentOpenFlowGroupBucketDetailsEntry_Object = MibTableRow
agentOpenFlowGroupBucketDetailsEntry = _AgentOpenFlowGroupBucketDetailsEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 11, 1)
)
agentOpenFlowGroupBucketDetailsEntry.setIndexNames(
    (0, "DNOS-OPENFLOW-PRIVATE-MIB", "agentOpenFlowBucketGroupId"),
    (0, "DNOS-OPENFLOW-PRIVATE-MIB", "agentOpenFlowGroupBucketId"),
)
if mibBuilder.loadTexts:
    agentOpenFlowGroupBucketDetailsEntry.setStatus("current")


class _AgentOpenFlowGroupBucketId_Type(Unsigned32):
    """Custom type agentOpenFlowGroupBucketId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentOpenFlowGroupBucketId_Type.__name__ = "Unsigned32"
_AgentOpenFlowGroupBucketId_Object = MibTableColumn
agentOpenFlowGroupBucketId = _AgentOpenFlowGroupBucketId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 11, 1, 1),
    _AgentOpenFlowGroupBucketId_Type()
)
agentOpenFlowGroupBucketId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowGroupBucketId.setStatus("current")
_AgentOpenFlowGroupBucketOutputPort_Type = DisplayString
_AgentOpenFlowGroupBucketOutputPort_Object = MibTableColumn
agentOpenFlowGroupBucketOutputPort = _AgentOpenFlowGroupBucketOutputPort_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 11, 1, 2),
    _AgentOpenFlowGroupBucketOutputPort_Type()
)
agentOpenFlowGroupBucketOutputPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowGroupBucketOutputPort.setStatus("current")
_AgentOpenFlowGroupBucketVlanId_Type = DisplayString
_AgentOpenFlowGroupBucketVlanId_Object = MibTableColumn
agentOpenFlowGroupBucketVlanId = _AgentOpenFlowGroupBucketVlanId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 11, 1, 3),
    _AgentOpenFlowGroupBucketVlanId_Type()
)
agentOpenFlowGroupBucketVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowGroupBucketVlanId.setStatus("current")
_AgentOpenFlowGroupBucketRefGroupId_Type = DisplayString
_AgentOpenFlowGroupBucketRefGroupId_Object = MibTableColumn
agentOpenFlowGroupBucketRefGroupId = _AgentOpenFlowGroupBucketRefGroupId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 11, 1, 4),
    _AgentOpenFlowGroupBucketRefGroupId_Type()
)
agentOpenFlowGroupBucketRefGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowGroupBucketRefGroupId.setStatus("current")
_AgentOpenFlowGroupBucketSrcMac_Type = PhysAddress
_AgentOpenFlowGroupBucketSrcMac_Object = MibTableColumn
agentOpenFlowGroupBucketSrcMac = _AgentOpenFlowGroupBucketSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 11, 1, 5),
    _AgentOpenFlowGroupBucketSrcMac_Type()
)
agentOpenFlowGroupBucketSrcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowGroupBucketSrcMac.setStatus("current")
_AgentOpenFlowGroupBucketDstMac_Type = PhysAddress
_AgentOpenFlowGroupBucketDstMac_Object = MibTableColumn
agentOpenFlowGroupBucketDstMac = _AgentOpenFlowGroupBucketDstMac_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 11, 1, 6),
    _AgentOpenFlowGroupBucketDstMac_Type()
)
agentOpenFlowGroupBucketDstMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowGroupBucketDstMac.setStatus("current")


class _AgentOpenFlowBucketGroupId_Type(Unsigned32):
    """Custom type agentOpenFlowBucketGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentOpenFlowBucketGroupId_Type.__name__ = "Unsigned32"
_AgentOpenFlowBucketGroupId_Object = MibTableColumn
agentOpenFlowBucketGroupId = _AgentOpenFlowBucketGroupId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 56, 1, 11, 1, 7),
    _AgentOpenFlowBucketGroupId_Type()
)
agentOpenFlowBucketGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOpenFlowBucketGroupId.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-OPENFLOW-PRIVATE-MIB",
    **{"fastPathOpenFlow": fastPathOpenFlow,
       "agentOpenFlowGroup": agentOpenFlowGroup,
       "agentOpenFlowGlobalConfigGroup": agentOpenFlowGlobalConfigGroup,
       "agentOpenFlowAdminMode": agentOpenFlowAdminMode,
       "agentOpenFlowVariant": agentOpenFlowVariant,
       "agentOpenFlowDefaultTable": agentOpenFlowDefaultTable,
       "agentOpenFlowStaticIPAssignmentMode": agentOpenFlowStaticIPAssignmentMode,
       "agentOpenFlowGlobalConfigIPAddress": agentOpenFlowGlobalConfigIPAddress,
       "agentOpenFlowNetworkMTU": agentOpenFlowNetworkMTU,
       "agentOpenFlowIPAssignmentMode": agentOpenFlowIPAssignmentMode,
       "agentOpenFlowCfgControllerTable": agentOpenFlowCfgControllerTable,
       "agentOpenFlowCfgControllerEntry": agentOpenFlowCfgControllerEntry,
       "agentOpenFlowCfgCtrlIPAddress": agentOpenFlowCfgCtrlIPAddress,
       "agentOpenFlowCfgCtrlIPPort": agentOpenFlowCfgCtrlIPPort,
       "agentOpenFlowCfgCtrlConnectionMode": agentOpenFlowCfgCtrlConnectionMode,
       "agentOpenFlowCfgCtrlStatus": agentOpenFlowCfgCtrlStatus,
       "agentOpenFlowCfgCtrlRole": agentOpenFlowCfgCtrlRole,
       "agentOpenFlowGlobalStatusParameters": agentOpenFlowGlobalStatusParameters,
       "agentOpenFlowOperationalStatus": agentOpenFlowOperationalStatus,
       "agentOpenFlowDisableReason": agentOpenFlowDisableReason,
       "agentOpenFlowGlobalCommands": agentOpenFlowGlobalCommands,
       "agentOpenFlowEraseOpenFlowManagerCertificates": agentOpenFlowEraseOpenFlowManagerCertificates,
       "agentOpenFlowFlowTableStatusTable": agentOpenFlowFlowTableStatusTable,
       "agentOpenFlowFlowTableStatusEntry": agentOpenFlowFlowTableStatusEntry,
       "agentOpenFlowFlowTable": agentOpenFlowFlowTable,
       "agentOpenFlowFlowTableName": agentOpenFlowFlowTableName,
       "agentOpenFlowFlowTableDescription": agentOpenFlowFlowTableDescription,
       "agentOpenFlowMaximumSize": agentOpenFlowMaximumSize,
       "agentOpenFlowNumberOfEntries": agentOpenFlowNumberOfEntries,
       "agentOpenFlowHardwareEntries": agentOpenFlowHardwareEntries,
       "agentOpenFlowSoftwareOnlyEntries": agentOpenFlowSoftwareOnlyEntries,
       "agentOpenFlowWaitingForSpaceEntries": agentOpenFlowWaitingForSpaceEntries,
       "agentOpenFlowFlowInsertionCount": agentOpenFlowFlowInsertionCount,
       "agentOpenFlowFlowDeletionCount": agentOpenFlowFlowDeletionCount,
       "agentOpenFlowInsertionFailureCount": agentOpenFlowInsertionFailureCount,
       "agentOpenFlowInstalledGroupEntry": agentOpenFlowInstalledGroupEntry,
       "agentOpenFlowGrpIndirectMaxEntries": agentOpenFlowGrpIndirectMaxEntries,
       "agentOpenFlowGrpIndirectCurrentEntries": agentOpenFlowGrpIndirectCurrentEntries,
       "agentOpenFlowGrpAllMaxEntries": agentOpenFlowGrpAllMaxEntries,
       "agentOpenFlowGrpAllCurrentEntries": agentOpenFlowGrpAllCurrentEntries,
       "agentOpenFlowGrpSelectMaxEntries": agentOpenFlowGrpSelectMaxEntries,
       "agentOpenFlowGrpSelectCurrentEntries": agentOpenFlowGrpSelectCurrentEntries,
       "agentOpenFlowGroupDetailsTable": agentOpenFlowGroupDetailsTable,
       "agentOpenFlowGroupDetailsEntry": agentOpenFlowGroupDetailsEntry,
       "agentOpenFlowGroupId": agentOpenFlowGroupId,
       "agentOpenFlowGroupType": agentOpenFlowGroupType,
       "agentOpenFlowGroupRefCount": agentOpenFlowGroupRefCount,
       "agentOpenFlowGroupDuration": agentOpenFlowGroupDuration,
       "agentOpenFlowGroupBucketCount": agentOpenFlowGroupBucketCount,
       "agentOpenFlowGroupBucketDetailsTable": agentOpenFlowGroupBucketDetailsTable,
       "agentOpenFlowGroupBucketDetailsEntry": agentOpenFlowGroupBucketDetailsEntry,
       "agentOpenFlowGroupBucketId": agentOpenFlowGroupBucketId,
       "agentOpenFlowGroupBucketOutputPort": agentOpenFlowGroupBucketOutputPort,
       "agentOpenFlowGroupBucketVlanId": agentOpenFlowGroupBucketVlanId,
       "agentOpenFlowGroupBucketRefGroupId": agentOpenFlowGroupBucketRefGroupId,
       "agentOpenFlowGroupBucketSrcMac": agentOpenFlowGroupBucketSrcMac,
       "agentOpenFlowGroupBucketDstMac": agentOpenFlowGroupBucketDstMac,
       "agentOpenFlowBucketGroupId": agentOpenFlowBucketGroupId}
)
