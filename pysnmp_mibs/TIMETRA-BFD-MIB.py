# SNMP MIB module (TIMETRA-BFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-BFD-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:00:31 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TItemDescription,
 TNamedItem,
 TmnxAdminState,
 TmnxBfdOnLspSessFecType,
 TmnxBfdSessOperFlags,
 TmnxBfdSessProtocolState,
 TmnxBfdSessionProtocols,
 TmnxBfdTermination,
 TmnxOperState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemDescription",
    "TNamedItem",
    "TmnxAdminState",
    "TmnxBfdOnLspSessFecType",
    "TmnxBfdSessOperFlags",
    "TmnxBfdSessProtocolState",
    "TmnxBfdSessionProtocols",
    "TmnxBfdTermination",
    "TmnxOperState")

(vRtrID,
 vRtrLspBfdMaxSessions,
 vRtrLspBfdSession) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrLspBfdMaxSessions",
    "vRtrLspBfdSession")


# MODULE-IDENTITY

timetraBfdMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 85)
)
if mibBuilder.loadTexts:
    timetraBfdMIBModule.setRevisions(
        ("2017-01-01 00:00",
         "2015-06-01 00:00",
         "2012-06-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxBfdConformance_ObjectIdentity = ObjectIdentity
tmnxBfdConformance = _TmnxBfdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85)
)
_TmnxBfdCompliances_ObjectIdentity = ObjectIdentity
tmnxBfdCompliances = _TmnxBfdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85, 1)
)
_TmnxBfdGroups_ObjectIdentity = ObjectIdentity
tmnxBfdGroups = _TmnxBfdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85, 2)
)
_TmnxBfdObjects_ObjectIdentity = ObjectIdentity
tmnxBfdObjects = _TmnxBfdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85)
)
_TmnxBfdOperObjects_ObjectIdentity = ObjectIdentity
tmnxBfdOperObjects = _TmnxBfdOperObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1)
)
_TmnxBfdOperValueObjects_ObjectIdentity = ObjectIdentity
tmnxBfdOperValueObjects = _TmnxBfdOperValueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1)
)
_TmnxBfdOperTemplateTable_Object = MibTable
tmnxBfdOperTemplateTable = _TmnxBfdOperTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxBfdOperTemplateTable.setStatus("current")
_TmnxBfdOperTemplateEntry_Object = MibTableRow
tmnxBfdOperTemplateEntry = _TmnxBfdOperTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1, 1)
)
tmnxBfdOperTemplateEntry.setIndexNames(
    (0, "TIMETRA-BFD-MIB", "tmnxBfdOperTemplateName"),
)
if mibBuilder.loadTexts:
    tmnxBfdOperTemplateEntry.setStatus("current")
_TmnxBfdOperTemplateName_Type = TNamedItem
_TmnxBfdOperTemplateName_Object = MibTableColumn
tmnxBfdOperTemplateName = _TmnxBfdOperTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1, 1, 1),
    _TmnxBfdOperTemplateName_Type()
)
tmnxBfdOperTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBfdOperTemplateName.setStatus("current")
_TmnxBfdOperTemplateRowStatus_Type = RowStatus
_TmnxBfdOperTemplateRowStatus_Object = MibTableColumn
tmnxBfdOperTemplateRowStatus = _TmnxBfdOperTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1, 1, 2),
    _TmnxBfdOperTemplateRowStatus_Type()
)
tmnxBfdOperTemplateRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOperTemplateRowStatus.setStatus("current")


class _TmnxBfdOperTemplateTxInt_Type(Unsigned32):
    """Custom type tmnxBfdOperTemplateTxInt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_TmnxBfdOperTemplateTxInt_Type.__name__ = "Unsigned32"
_TmnxBfdOperTemplateTxInt_Object = MibTableColumn
tmnxBfdOperTemplateTxInt = _TmnxBfdOperTemplateTxInt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1, 1, 3),
    _TmnxBfdOperTemplateTxInt_Type()
)
tmnxBfdOperTemplateTxInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOperTemplateTxInt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBfdOperTemplateTxInt.setUnits("milliseconds")


class _TmnxBfdOperTemplateRxInt_Type(Unsigned32):
    """Custom type tmnxBfdOperTemplateRxInt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_TmnxBfdOperTemplateRxInt_Type.__name__ = "Unsigned32"
_TmnxBfdOperTemplateRxInt_Object = MibTableColumn
tmnxBfdOperTemplateRxInt = _TmnxBfdOperTemplateRxInt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1, 1, 4),
    _TmnxBfdOperTemplateRxInt_Type()
)
tmnxBfdOperTemplateRxInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOperTemplateRxInt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBfdOperTemplateRxInt.setUnits("milliseconds")


class _TmnxBfdOperTemplateMultiplier_Type(Unsigned32):
    """Custom type tmnxBfdOperTemplateMultiplier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_TmnxBfdOperTemplateMultiplier_Type.__name__ = "Unsigned32"
_TmnxBfdOperTemplateMultiplier_Object = MibTableColumn
tmnxBfdOperTemplateMultiplier = _TmnxBfdOperTemplateMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1, 1, 5),
    _TmnxBfdOperTemplateMultiplier_Type()
)
tmnxBfdOperTemplateMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOperTemplateMultiplier.setStatus("current")


class _TmnxBfdOperTemplateEchoRxInt_Type(Unsigned32):
    """Custom type tmnxBfdOperTemplateEchoRxInt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100000),
    )


_TmnxBfdOperTemplateEchoRxInt_Type.__name__ = "Unsigned32"
_TmnxBfdOperTemplateEchoRxInt_Object = MibTableColumn
tmnxBfdOperTemplateEchoRxInt = _TmnxBfdOperTemplateEchoRxInt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1, 1, 6),
    _TmnxBfdOperTemplateEchoRxInt_Type()
)
tmnxBfdOperTemplateEchoRxInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOperTemplateEchoRxInt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBfdOperTemplateEchoRxInt.setUnits("milliseconds")


class _TmnxBfdOperTemplateType_Type(Integer32):
    """Custom type tmnxBfdOperTemplateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cpmNp", 1),
          ("auto", 2))
    )


_TmnxBfdOperTemplateType_Type.__name__ = "Integer32"
_TmnxBfdOperTemplateType_Object = MibTableColumn
tmnxBfdOperTemplateType = _TmnxBfdOperTemplateType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 1, 1, 1, 1, 7),
    _TmnxBfdOperTemplateType_Type()
)
tmnxBfdOperTemplateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOperTemplateType.setStatus("current")
_TmnxBfdAdminObjects_ObjectIdentity = ObjectIdentity
tmnxBfdAdminObjects = _TmnxBfdAdminObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2)
)
_TmnxBfdAdminControlObjects_ObjectIdentity = ObjectIdentity
tmnxBfdAdminControlObjects = _TmnxBfdAdminControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 1)
)


class _TmnxBfdAdminOwner_Type(DisplayString):
    """Custom type tmnxBfdAdminOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TmnxBfdAdminOwner_Type.__name__ = "DisplayString"
_TmnxBfdAdminOwner_Object = MibScalar
tmnxBfdAdminOwner = _TmnxBfdAdminOwner_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 1, 1),
    _TmnxBfdAdminOwner_Type()
)
tmnxBfdAdminOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBfdAdminOwner.setStatus("current")


class _TmnxBfdAdminControlApply_Type(Integer32):
    """Custom type tmnxBfdAdminControlApply based on Integer32"""
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
        *(("none", 1),
          ("initialize", 2),
          ("commit", 3))
    )


_TmnxBfdAdminControlApply_Type.__name__ = "Integer32"
_TmnxBfdAdminControlApply_Object = MibScalar
tmnxBfdAdminControlApply = _TmnxBfdAdminControlApply_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 1, 2),
    _TmnxBfdAdminControlApply_Type()
)
tmnxBfdAdminControlApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBfdAdminControlApply.setStatus("current")
_TmnxBfdAdminLastSetTimer_Type = TimeInterval
_TmnxBfdAdminLastSetTimer_Object = MibScalar
tmnxBfdAdminLastSetTimer = _TmnxBfdAdminLastSetTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 1, 3),
    _TmnxBfdAdminLastSetTimer_Type()
)
tmnxBfdAdminLastSetTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdAdminLastSetTimer.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBfdAdminLastSetTimer.setUnits("centiseconds")


class _TmnxBfdAdminLastSetTimeout_Type(TimeInterval):
    """Custom type tmnxBfdAdminLastSetTimeout based on TimeInterval"""
    defaultValue = 180000


_TmnxBfdAdminLastSetTimeout_Type.__name__ = "TimeInterval"
_TmnxBfdAdminLastSetTimeout_Object = MibScalar
tmnxBfdAdminLastSetTimeout = _TmnxBfdAdminLastSetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 1, 4),
    _TmnxBfdAdminLastSetTimeout_Type()
)
tmnxBfdAdminLastSetTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxBfdAdminLastSetTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBfdAdminLastSetTimeout.setUnits("centiseconds")
_TmnxBfdAdminValueObjects_ObjectIdentity = ObjectIdentity
tmnxBfdAdminValueObjects = _TmnxBfdAdminValueObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2)
)
_TmnxBfdAdminTemplateTable_Object = MibTable
tmnxBfdAdminTemplateTable = _TmnxBfdAdminTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1)
)
if mibBuilder.loadTexts:
    tmnxBfdAdminTemplateTable.setStatus("current")
_TmnxBfdAdminTemplateEntry_Object = MibTableRow
tmnxBfdAdminTemplateEntry = _TmnxBfdAdminTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1, 1)
)
tmnxBfdAdminTemplateEntry.setIndexNames(
    (0, "TIMETRA-BFD-MIB", "tmnxBfdAdminTemplateName"),
)
if mibBuilder.loadTexts:
    tmnxBfdAdminTemplateEntry.setStatus("current")
_TmnxBfdAdminTemplateName_Type = TNamedItem
_TmnxBfdAdminTemplateName_Object = MibTableColumn
tmnxBfdAdminTemplateName = _TmnxBfdAdminTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1, 1, 1),
    _TmnxBfdAdminTemplateName_Type()
)
tmnxBfdAdminTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBfdAdminTemplateName.setStatus("current")
_TmnxBfdAdminTemplateRowStatus_Type = RowStatus
_TmnxBfdAdminTemplateRowStatus_Object = MibTableColumn
tmnxBfdAdminTemplateRowStatus = _TmnxBfdAdminTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1, 1, 2),
    _TmnxBfdAdminTemplateRowStatus_Type()
)
tmnxBfdAdminTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBfdAdminTemplateRowStatus.setStatus("current")


class _TmnxBfdAdminTemplateTxInt_Type(Unsigned32):
    """Custom type tmnxBfdAdminTemplateTxInt based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_TmnxBfdAdminTemplateTxInt_Type.__name__ = "Unsigned32"
_TmnxBfdAdminTemplateTxInt_Object = MibTableColumn
tmnxBfdAdminTemplateTxInt = _TmnxBfdAdminTemplateTxInt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1, 1, 3),
    _TmnxBfdAdminTemplateTxInt_Type()
)
tmnxBfdAdminTemplateTxInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBfdAdminTemplateTxInt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBfdAdminTemplateTxInt.setUnits("milliseconds")


class _TmnxBfdAdminTemplateRxInt_Type(Unsigned32):
    """Custom type tmnxBfdAdminTemplateRxInt based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_TmnxBfdAdminTemplateRxInt_Type.__name__ = "Unsigned32"
_TmnxBfdAdminTemplateRxInt_Object = MibTableColumn
tmnxBfdAdminTemplateRxInt = _TmnxBfdAdminTemplateRxInt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1, 1, 4),
    _TmnxBfdAdminTemplateRxInt_Type()
)
tmnxBfdAdminTemplateRxInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBfdAdminTemplateRxInt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBfdAdminTemplateRxInt.setUnits("milliseconds")


class _TmnxBfdAdminTemplateMultiplier_Type(Unsigned32):
    """Custom type tmnxBfdAdminTemplateMultiplier based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_TmnxBfdAdminTemplateMultiplier_Type.__name__ = "Unsigned32"
_TmnxBfdAdminTemplateMultiplier_Object = MibTableColumn
tmnxBfdAdminTemplateMultiplier = _TmnxBfdAdminTemplateMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1, 1, 5),
    _TmnxBfdAdminTemplateMultiplier_Type()
)
tmnxBfdAdminTemplateMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBfdAdminTemplateMultiplier.setStatus("current")


class _TmnxBfdAdminTemplateEchoRxInt_Type(Unsigned32):
    """Custom type tmnxBfdAdminTemplateEchoRxInt based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100000),
    )


_TmnxBfdAdminTemplateEchoRxInt_Type.__name__ = "Unsigned32"
_TmnxBfdAdminTemplateEchoRxInt_Object = MibTableColumn
tmnxBfdAdminTemplateEchoRxInt = _TmnxBfdAdminTemplateEchoRxInt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1, 1, 6),
    _TmnxBfdAdminTemplateEchoRxInt_Type()
)
tmnxBfdAdminTemplateEchoRxInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBfdAdminTemplateEchoRxInt.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBfdAdminTemplateEchoRxInt.setUnits("milliseconds")


class _TmnxBfdAdminTemplateType_Type(Integer32):
    """Custom type tmnxBfdAdminTemplateType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cpmNp", 1),
          ("auto", 2))
    )


_TmnxBfdAdminTemplateType_Type.__name__ = "Integer32"
_TmnxBfdAdminTemplateType_Object = MibTableColumn
tmnxBfdAdminTemplateType = _TmnxBfdAdminTemplateType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 2, 2, 1, 1, 7),
    _TmnxBfdAdminTemplateType_Type()
)
tmnxBfdAdminTemplateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBfdAdminTemplateType.setStatus("current")
_TmnxBfdStatistics_ObjectIdentity = ObjectIdentity
tmnxBfdStatistics = _TmnxBfdStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3)
)
_TmnxBfdOnLspSessTable_Object = MibTable
tmnxBfdOnLspSessTable = _TmnxBfdOnLspSessTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1)
)
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessTable.setStatus("current")
_TmnxBfdOnLspSessEntry_Object = MibTableRow
tmnxBfdOnLspSessEntry = _TmnxBfdOnLspSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1)
)
tmnxBfdOnLspSessEntry.setIndexNames(
    (0, "TIMETRA-BFD-MIB", "tmnxBfdOnLspSessLinkType"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-BFD-MIB", "tmnxBfdOnLspSessFecType"),
    (0, "TIMETRA-BFD-MIB", "tmnxBfdOnLspSessRemAddrType"),
    (0, "TIMETRA-BFD-MIB", "tmnxBfdOnLspSessRemAddr"),
    (0, "TIMETRA-BFD-MIB", "tmnxBfdOnLspSessLclAddrType"),
    (0, "TIMETRA-BFD-MIB", "tmnxBfdOnLspSessLclAddr"),
    (0, "TIMETRA-BFD-MIB", "tmnxBfdOnLspSessPathId"),
    (0, "TIMETRA-BFD-MIB", "tmnxBfdOnLspSessTunnelId"),
)
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessEntry.setStatus("current")


class _TmnxBfdOnLspSessLinkType_Type(Integer32):
    """Custom type tmnxBfdOnLspSessLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              9,
              11)
        )
    )
    namedValues = NamedValues(
        *(("lspHead", 8),
          ("lspTail", 9),
          ("sLspPath", 11))
    )


_TmnxBfdOnLspSessLinkType_Type.__name__ = "Integer32"
_TmnxBfdOnLspSessLinkType_Object = MibTableColumn
tmnxBfdOnLspSessLinkType = _TmnxBfdOnLspSessLinkType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 1),
    _TmnxBfdOnLspSessLinkType_Type()
)
tmnxBfdOnLspSessLinkType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessLinkType.setStatus("current")
_TmnxBfdOnLspSessFecType_Type = TmnxBfdOnLspSessFecType
_TmnxBfdOnLspSessFecType_Object = MibTableColumn
tmnxBfdOnLspSessFecType = _TmnxBfdOnLspSessFecType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 2),
    _TmnxBfdOnLspSessFecType_Type()
)
tmnxBfdOnLspSessFecType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessFecType.setStatus("current")
_TmnxBfdOnLspSessRemAddrType_Type = InetAddressType
_TmnxBfdOnLspSessRemAddrType_Object = MibTableColumn
tmnxBfdOnLspSessRemAddrType = _TmnxBfdOnLspSessRemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 3),
    _TmnxBfdOnLspSessRemAddrType_Type()
)
tmnxBfdOnLspSessRemAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessRemAddrType.setStatus("current")


class _TmnxBfdOnLspSessRemAddr_Type(InetAddress):
    """Custom type tmnxBfdOnLspSessRemAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxBfdOnLspSessRemAddr_Type.__name__ = "InetAddress"
_TmnxBfdOnLspSessRemAddr_Object = MibTableColumn
tmnxBfdOnLspSessRemAddr = _TmnxBfdOnLspSessRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 4),
    _TmnxBfdOnLspSessRemAddr_Type()
)
tmnxBfdOnLspSessRemAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessRemAddr.setStatus("current")
_TmnxBfdOnLspSessLclAddrType_Type = InetAddressType
_TmnxBfdOnLspSessLclAddrType_Object = MibTableColumn
tmnxBfdOnLspSessLclAddrType = _TmnxBfdOnLspSessLclAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 5),
    _TmnxBfdOnLspSessLclAddrType_Type()
)
tmnxBfdOnLspSessLclAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessLclAddrType.setStatus("current")


class _TmnxBfdOnLspSessLclAddr_Type(InetAddress):
    """Custom type tmnxBfdOnLspSessLclAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxBfdOnLspSessLclAddr_Type.__name__ = "InetAddress"
_TmnxBfdOnLspSessLclAddr_Object = MibTableColumn
tmnxBfdOnLspSessLclAddr = _TmnxBfdOnLspSessLclAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 6),
    _TmnxBfdOnLspSessLclAddr_Type()
)
tmnxBfdOnLspSessLclAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessLclAddr.setStatus("current")
_TmnxBfdOnLspSessPathId_Type = Unsigned32
_TmnxBfdOnLspSessPathId_Object = MibTableColumn
tmnxBfdOnLspSessPathId = _TmnxBfdOnLspSessPathId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 7),
    _TmnxBfdOnLspSessPathId_Type()
)
tmnxBfdOnLspSessPathId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessPathId.setStatus("current")
_TmnxBfdOnLspSessTunnelId_Type = Unsigned32
_TmnxBfdOnLspSessTunnelId_Object = MibTableColumn
tmnxBfdOnLspSessTunnelId = _TmnxBfdOnLspSessTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 8),
    _TmnxBfdOnLspSessTunnelId_Type()
)
tmnxBfdOnLspSessTunnelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessTunnelId.setStatus("current")
_TmnxBfdOnLspSessOperState_Type = TmnxOperState
_TmnxBfdOnLspSessOperState_Object = MibTableColumn
tmnxBfdOnLspSessOperState = _TmnxBfdOnLspSessOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 9),
    _TmnxBfdOnLspSessOperState_Type()
)
tmnxBfdOnLspSessOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessOperState.setStatus("current")
_TmnxBfdOnLspSessState_Type = TmnxBfdSessProtocolState
_TmnxBfdOnLspSessState_Object = MibTableColumn
tmnxBfdOnLspSessState = _TmnxBfdOnLspSessState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 10),
    _TmnxBfdOnLspSessState_Type()
)
tmnxBfdOnLspSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessState.setStatus("current")
_TmnxBfdOnLspSessOperFlags_Type = TmnxBfdSessOperFlags
_TmnxBfdOnLspSessOperFlags_Object = MibTableColumn
tmnxBfdOnLspSessOperFlags = _TmnxBfdOnLspSessOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 11),
    _TmnxBfdOnLspSessOperFlags_Type()
)
tmnxBfdOnLspSessOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessOperFlags.setStatus("current")
_TmnxBfdOnLspSessMesgRecv_Type = Counter32
_TmnxBfdOnLspSessMesgRecv_Object = MibTableColumn
tmnxBfdOnLspSessMesgRecv = _TmnxBfdOnLspSessMesgRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 12),
    _TmnxBfdOnLspSessMesgRecv_Type()
)
tmnxBfdOnLspSessMesgRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessMesgRecv.setStatus("current")
_TmnxBfdOnLspSessMesgSent_Type = Counter32
_TmnxBfdOnLspSessMesgSent_Object = MibTableColumn
tmnxBfdOnLspSessMesgSent = _TmnxBfdOnLspSessMesgSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 13),
    _TmnxBfdOnLspSessMesgSent_Type()
)
tmnxBfdOnLspSessMesgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessMesgSent.setStatus("current")
_TmnxBfdOnLspSessLastDownTime_Type = TimeTicks
_TmnxBfdOnLspSessLastDownTime_Object = MibTableColumn
tmnxBfdOnLspSessLastDownTime = _TmnxBfdOnLspSessLastDownTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 14),
    _TmnxBfdOnLspSessLastDownTime_Type()
)
tmnxBfdOnLspSessLastDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessLastDownTime.setStatus("current")
_TmnxBfdOnLspSessLastUpTime_Type = TimeTicks
_TmnxBfdOnLspSessLastUpTime_Object = MibTableColumn
tmnxBfdOnLspSessLastUpTime = _TmnxBfdOnLspSessLastUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 15),
    _TmnxBfdOnLspSessLastUpTime_Type()
)
tmnxBfdOnLspSessLastUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessLastUpTime.setStatus("current")
_TmnxBfdOnLspSessUpCount_Type = Counter32
_TmnxBfdOnLspSessUpCount_Object = MibTableColumn
tmnxBfdOnLspSessUpCount = _TmnxBfdOnLspSessUpCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 16),
    _TmnxBfdOnLspSessUpCount_Type()
)
tmnxBfdOnLspSessUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessUpCount.setStatus("current")
_TmnxBfdOnLspSessDownCount_Type = Counter32
_TmnxBfdOnLspSessDownCount_Object = MibTableColumn
tmnxBfdOnLspSessDownCount = _TmnxBfdOnLspSessDownCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 17),
    _TmnxBfdOnLspSessDownCount_Type()
)
tmnxBfdOnLspSessDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessDownCount.setStatus("current")
_TmnxBfdOnLspSessLclDisc_Type = Unsigned32
_TmnxBfdOnLspSessLclDisc_Object = MibTableColumn
tmnxBfdOnLspSessLclDisc = _TmnxBfdOnLspSessLclDisc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 18),
    _TmnxBfdOnLspSessLclDisc_Type()
)
tmnxBfdOnLspSessLclDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessLclDisc.setStatus("current")
_TmnxBfdOnLspSessRemDisc_Type = Unsigned32
_TmnxBfdOnLspSessRemDisc_Object = MibTableColumn
tmnxBfdOnLspSessRemDisc = _TmnxBfdOnLspSessRemDisc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 19),
    _TmnxBfdOnLspSessRemDisc_Type()
)
tmnxBfdOnLspSessRemDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessRemDisc.setStatus("current")
_TmnxBfdOnLspSessProtocols_Type = TmnxBfdSessionProtocols
_TmnxBfdOnLspSessProtocols_Object = MibTableColumn
tmnxBfdOnLspSessProtocols = _TmnxBfdOnLspSessProtocols_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 20),
    _TmnxBfdOnLspSessProtocols_Type()
)
tmnxBfdOnLspSessProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessProtocols.setStatus("current")
_TmnxBfdOnLspSessTxInterval_Type = Unsigned32
_TmnxBfdOnLspSessTxInterval_Object = MibTableColumn
tmnxBfdOnLspSessTxInterval = _TmnxBfdOnLspSessTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 21),
    _TmnxBfdOnLspSessTxInterval_Type()
)
tmnxBfdOnLspSessTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessTxInterval.setUnits("milliseconds")
_TmnxBfdOnLspSessRxInterval_Type = Unsigned32
_TmnxBfdOnLspSessRxInterval_Object = MibTableColumn
tmnxBfdOnLspSessRxInterval = _TmnxBfdOnLspSessRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 22),
    _TmnxBfdOnLspSessRxInterval_Type()
)
tmnxBfdOnLspSessRxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessRxInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessRxInterval.setUnits("milliseconds")
_TmnxBfdOnLspSessType_Type = TmnxBfdTermination
_TmnxBfdOnLspSessType_Object = MibTableColumn
tmnxBfdOnLspSessType = _TmnxBfdOnLspSessType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 23),
    _TmnxBfdOnLspSessType_Type()
)
tmnxBfdOnLspSessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessType.setStatus("current")
_TmnxBfdOnLspSessVerMismatch_Type = Counter32
_TmnxBfdOnLspSessVerMismatch_Object = MibTableColumn
tmnxBfdOnLspSessVerMismatch = _TmnxBfdOnLspSessVerMismatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 24),
    _TmnxBfdOnLspSessVerMismatch_Type()
)
tmnxBfdOnLspSessVerMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessVerMismatch.setStatus("current")
_TmnxBfdOnLspSessTimeSinceLastRx_Type = Unsigned32
_TmnxBfdOnLspSessTimeSinceLastRx_Object = MibTableColumn
tmnxBfdOnLspSessTimeSinceLastRx = _TmnxBfdOnLspSessTimeSinceLastRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 25),
    _TmnxBfdOnLspSessTimeSinceLastRx_Type()
)
tmnxBfdOnLspSessTimeSinceLastRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessTimeSinceLastRx.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessTimeSinceLastRx.setUnits("milliseconds")
_TmnxBfdOnLspSessTimeSinceLastTx_Type = Unsigned32
_TmnxBfdOnLspSessTimeSinceLastTx_Object = MibTableColumn
tmnxBfdOnLspSessTimeSinceLastTx = _TmnxBfdOnLspSessTimeSinceLastTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 1, 1, 26),
    _TmnxBfdOnLspSessTimeSinceLastTx_Type()
)
tmnxBfdOnLspSessTimeSinceLastTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessTimeSinceLastTx.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessTimeSinceLastTx.setUnits("milliseconds")
_TmnxBfdOnLspExtSessTable_Object = MibTable
tmnxBfdOnLspExtSessTable = _TmnxBfdOnLspExtSessTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2)
)
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessTable.setStatus("current")
_TmnxBfdOnLspExtSessEntry_Object = MibTableRow
tmnxBfdOnLspExtSessEntry = _TmnxBfdOnLspExtSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1)
)
tmnxBfdOnLspExtSessEntry.setIndexNames(
    (0, "TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessLinkType"),
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessFecType"),
    (0, "TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessRemAddrType"),
    (0, "TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessRemAddr"),
    (0, "TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessLclAddrType"),
    (0, "TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessLclAddr"),
    (0, "TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessPathId"),
    (0, "TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessTunnelId"),
    (0, "TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessInfoId"),
)
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessEntry.setStatus("current")


class _TmnxBfdOnLspExtSessLinkType_Type(Integer32):
    """Custom type tmnxBfdOnLspExtSessLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            12
        )
    )
    namedValues = NamedValues(
        ("sSrPolicy", 12)
    )


_TmnxBfdOnLspExtSessLinkType_Type.__name__ = "Integer32"
_TmnxBfdOnLspExtSessLinkType_Object = MibTableColumn
tmnxBfdOnLspExtSessLinkType = _TmnxBfdOnLspExtSessLinkType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 1),
    _TmnxBfdOnLspExtSessLinkType_Type()
)
tmnxBfdOnLspExtSessLinkType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessLinkType.setStatus("current")
_TmnxBfdOnLspExtSessFecType_Type = TmnxBfdOnLspSessFecType
_TmnxBfdOnLspExtSessFecType_Object = MibTableColumn
tmnxBfdOnLspExtSessFecType = _TmnxBfdOnLspExtSessFecType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 2),
    _TmnxBfdOnLspExtSessFecType_Type()
)
tmnxBfdOnLspExtSessFecType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessFecType.setStatus("current")
_TmnxBfdOnLspExtSessRemAddrType_Type = InetAddressType
_TmnxBfdOnLspExtSessRemAddrType_Object = MibTableColumn
tmnxBfdOnLspExtSessRemAddrType = _TmnxBfdOnLspExtSessRemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 3),
    _TmnxBfdOnLspExtSessRemAddrType_Type()
)
tmnxBfdOnLspExtSessRemAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessRemAddrType.setStatus("current")


class _TmnxBfdOnLspExtSessRemAddr_Type(InetAddress):
    """Custom type tmnxBfdOnLspExtSessRemAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxBfdOnLspExtSessRemAddr_Type.__name__ = "InetAddress"
_TmnxBfdOnLspExtSessRemAddr_Object = MibTableColumn
tmnxBfdOnLspExtSessRemAddr = _TmnxBfdOnLspExtSessRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 4),
    _TmnxBfdOnLspExtSessRemAddr_Type()
)
tmnxBfdOnLspExtSessRemAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessRemAddr.setStatus("current")
_TmnxBfdOnLspExtSessLclAddrType_Type = InetAddressType
_TmnxBfdOnLspExtSessLclAddrType_Object = MibTableColumn
tmnxBfdOnLspExtSessLclAddrType = _TmnxBfdOnLspExtSessLclAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 5),
    _TmnxBfdOnLspExtSessLclAddrType_Type()
)
tmnxBfdOnLspExtSessLclAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessLclAddrType.setStatus("current")


class _TmnxBfdOnLspExtSessLclAddr_Type(InetAddress):
    """Custom type tmnxBfdOnLspExtSessLclAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_TmnxBfdOnLspExtSessLclAddr_Type.__name__ = "InetAddress"
_TmnxBfdOnLspExtSessLclAddr_Object = MibTableColumn
tmnxBfdOnLspExtSessLclAddr = _TmnxBfdOnLspExtSessLclAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 6),
    _TmnxBfdOnLspExtSessLclAddr_Type()
)
tmnxBfdOnLspExtSessLclAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessLclAddr.setStatus("current")
_TmnxBfdOnLspExtSessPathId_Type = Unsigned32
_TmnxBfdOnLspExtSessPathId_Object = MibTableColumn
tmnxBfdOnLspExtSessPathId = _TmnxBfdOnLspExtSessPathId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 7),
    _TmnxBfdOnLspExtSessPathId_Type()
)
tmnxBfdOnLspExtSessPathId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessPathId.setStatus("current")
_TmnxBfdOnLspExtSessTunnelId_Type = Unsigned32
_TmnxBfdOnLspExtSessTunnelId_Object = MibTableColumn
tmnxBfdOnLspExtSessTunnelId = _TmnxBfdOnLspExtSessTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 8),
    _TmnxBfdOnLspExtSessTunnelId_Type()
)
tmnxBfdOnLspExtSessTunnelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessTunnelId.setStatus("current")
_TmnxBfdOnLspExtSessInfoId_Type = Unsigned32
_TmnxBfdOnLspExtSessInfoId_Object = MibTableColumn
tmnxBfdOnLspExtSessInfoId = _TmnxBfdOnLspExtSessInfoId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 9),
    _TmnxBfdOnLspExtSessInfoId_Type()
)
tmnxBfdOnLspExtSessInfoId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessInfoId.setStatus("current")
_TmnxBfdOnLspExtSessOperState_Type = TmnxOperState
_TmnxBfdOnLspExtSessOperState_Object = MibTableColumn
tmnxBfdOnLspExtSessOperState = _TmnxBfdOnLspExtSessOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 10),
    _TmnxBfdOnLspExtSessOperState_Type()
)
tmnxBfdOnLspExtSessOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessOperState.setStatus("current")
_TmnxBfdOnLspExtSessState_Type = TmnxBfdSessProtocolState
_TmnxBfdOnLspExtSessState_Object = MibTableColumn
tmnxBfdOnLspExtSessState = _TmnxBfdOnLspExtSessState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 11),
    _TmnxBfdOnLspExtSessState_Type()
)
tmnxBfdOnLspExtSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessState.setStatus("current")
_TmnxBfdOnLspExtSessOperFlags_Type = TmnxBfdSessOperFlags
_TmnxBfdOnLspExtSessOperFlags_Object = MibTableColumn
tmnxBfdOnLspExtSessOperFlags = _TmnxBfdOnLspExtSessOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 12),
    _TmnxBfdOnLspExtSessOperFlags_Type()
)
tmnxBfdOnLspExtSessOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessOperFlags.setStatus("current")
_TmnxBfdOnLspExtSessMesgRecv_Type = Counter32
_TmnxBfdOnLspExtSessMesgRecv_Object = MibTableColumn
tmnxBfdOnLspExtSessMesgRecv = _TmnxBfdOnLspExtSessMesgRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 13),
    _TmnxBfdOnLspExtSessMesgRecv_Type()
)
tmnxBfdOnLspExtSessMesgRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessMesgRecv.setStatus("current")
_TmnxBfdOnLspExtSessMesgSent_Type = Counter32
_TmnxBfdOnLspExtSessMesgSent_Object = MibTableColumn
tmnxBfdOnLspExtSessMesgSent = _TmnxBfdOnLspExtSessMesgSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 14),
    _TmnxBfdOnLspExtSessMesgSent_Type()
)
tmnxBfdOnLspExtSessMesgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessMesgSent.setStatus("current")
_TmnxBfdOnLspExtSessLastDownTime_Type = TimeTicks
_TmnxBfdOnLspExtSessLastDownTime_Object = MibTableColumn
tmnxBfdOnLspExtSessLastDownTime = _TmnxBfdOnLspExtSessLastDownTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 15),
    _TmnxBfdOnLspExtSessLastDownTime_Type()
)
tmnxBfdOnLspExtSessLastDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessLastDownTime.setStatus("current")
_TmnxBfdOnLspExtSessLastUpTime_Type = TimeTicks
_TmnxBfdOnLspExtSessLastUpTime_Object = MibTableColumn
tmnxBfdOnLspExtSessLastUpTime = _TmnxBfdOnLspExtSessLastUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 16),
    _TmnxBfdOnLspExtSessLastUpTime_Type()
)
tmnxBfdOnLspExtSessLastUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessLastUpTime.setStatus("current")
_TmnxBfdOnLspExtSessUpCount_Type = Counter32
_TmnxBfdOnLspExtSessUpCount_Object = MibTableColumn
tmnxBfdOnLspExtSessUpCount = _TmnxBfdOnLspExtSessUpCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 17),
    _TmnxBfdOnLspExtSessUpCount_Type()
)
tmnxBfdOnLspExtSessUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessUpCount.setStatus("current")
_TmnxBfdOnLspExtSessDownCount_Type = Counter32
_TmnxBfdOnLspExtSessDownCount_Object = MibTableColumn
tmnxBfdOnLspExtSessDownCount = _TmnxBfdOnLspExtSessDownCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 18),
    _TmnxBfdOnLspExtSessDownCount_Type()
)
tmnxBfdOnLspExtSessDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessDownCount.setStatus("current")
_TmnxBfdOnLspExtSessLclDisc_Type = Unsigned32
_TmnxBfdOnLspExtSessLclDisc_Object = MibTableColumn
tmnxBfdOnLspExtSessLclDisc = _TmnxBfdOnLspExtSessLclDisc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 19),
    _TmnxBfdOnLspExtSessLclDisc_Type()
)
tmnxBfdOnLspExtSessLclDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessLclDisc.setStatus("current")
_TmnxBfdOnLspExtSessRemDisc_Type = Unsigned32
_TmnxBfdOnLspExtSessRemDisc_Object = MibTableColumn
tmnxBfdOnLspExtSessRemDisc = _TmnxBfdOnLspExtSessRemDisc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 20),
    _TmnxBfdOnLspExtSessRemDisc_Type()
)
tmnxBfdOnLspExtSessRemDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessRemDisc.setStatus("current")
_TmnxBfdOnLspExtSessProtocols_Type = TmnxBfdSessionProtocols
_TmnxBfdOnLspExtSessProtocols_Object = MibTableColumn
tmnxBfdOnLspExtSessProtocols = _TmnxBfdOnLspExtSessProtocols_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 21),
    _TmnxBfdOnLspExtSessProtocols_Type()
)
tmnxBfdOnLspExtSessProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessProtocols.setStatus("current")
_TmnxBfdOnLspExtSessTxInterval_Type = Unsigned32
_TmnxBfdOnLspExtSessTxInterval_Object = MibTableColumn
tmnxBfdOnLspExtSessTxInterval = _TmnxBfdOnLspExtSessTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 22),
    _TmnxBfdOnLspExtSessTxInterval_Type()
)
tmnxBfdOnLspExtSessTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessTxInterval.setUnits("milliseconds")
_TmnxBfdOnLspExtSessRxInterval_Type = Unsigned32
_TmnxBfdOnLspExtSessRxInterval_Object = MibTableColumn
tmnxBfdOnLspExtSessRxInterval = _TmnxBfdOnLspExtSessRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 23),
    _TmnxBfdOnLspExtSessRxInterval_Type()
)
tmnxBfdOnLspExtSessRxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessRxInterval.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessRxInterval.setUnits("milliseconds")
_TmnxBfdOnLspExtSessType_Type = TmnxBfdTermination
_TmnxBfdOnLspExtSessType_Object = MibTableColumn
tmnxBfdOnLspExtSessType = _TmnxBfdOnLspExtSessType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 24),
    _TmnxBfdOnLspExtSessType_Type()
)
tmnxBfdOnLspExtSessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessType.setStatus("current")
_TmnxBfdOnLspExtSessVerMismatch_Type = Counter32
_TmnxBfdOnLspExtSessVerMismatch_Object = MibTableColumn
tmnxBfdOnLspExtSessVerMismatch = _TmnxBfdOnLspExtSessVerMismatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 25),
    _TmnxBfdOnLspExtSessVerMismatch_Type()
)
tmnxBfdOnLspExtSessVerMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessVerMismatch.setStatus("current")
_TmnxBfdOnLspExtSessTimeSinceRx_Type = Unsigned32
_TmnxBfdOnLspExtSessTimeSinceRx_Object = MibTableColumn
tmnxBfdOnLspExtSessTimeSinceRx = _TmnxBfdOnLspExtSessTimeSinceRx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 26),
    _TmnxBfdOnLspExtSessTimeSinceRx_Type()
)
tmnxBfdOnLspExtSessTimeSinceRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessTimeSinceRx.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessTimeSinceRx.setUnits("milliseconds")
_TmnxBfdOnLspExtSessTimeSinceTx_Type = Unsigned32
_TmnxBfdOnLspExtSessTimeSinceTx_Object = MibTableColumn
tmnxBfdOnLspExtSessTimeSinceTx = _TmnxBfdOnLspExtSessTimeSinceTx_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 3, 2, 1, 27),
    _TmnxBfdOnLspExtSessTimeSinceTx_Type()
)
tmnxBfdOnLspExtSessTimeSinceTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessTimeSinceTx.setStatus("current")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessTimeSinceTx.setUnits("milliseconds")
_TmnxBfdNotifyObjects_ObjectIdentity = ObjectIdentity
tmnxBfdNotifyObjects = _TmnxBfdNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 4)
)
_TmnxBfdOnLspSessChangedProtocol_Type = DisplayString
_TmnxBfdOnLspSessChangedProtocol_Object = MibScalar
tmnxBfdOnLspSessChangedProtocol = _TmnxBfdOnLspSessChangedProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 4, 1),
    _TmnxBfdOnLspSessChangedProtocol_Type()
)
tmnxBfdOnLspSessChangedProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessChangedProtocol.setStatus("current")


class _TmnxBfdOnLspSessProtoChngdState_Type(Integer32):
    """Custom type tmnxBfdOnLspSessProtoChngdState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("added", 0),
          ("cleared", 1))
    )


_TmnxBfdOnLspSessProtoChngdState_Type.__name__ = "Integer32"
_TmnxBfdOnLspSessProtoChngdState_Object = MibScalar
tmnxBfdOnLspSessProtoChngdState = _TmnxBfdOnLspSessProtoChngdState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 4, 2),
    _TmnxBfdOnLspSessProtoChngdState_Type()
)
tmnxBfdOnLspSessProtoChngdState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessProtoChngdState.setStatus("current")
_TmnxBfdOnLspExtSessChngdProtocol_Type = DisplayString
_TmnxBfdOnLspExtSessChngdProtocol_Object = MibScalar
tmnxBfdOnLspExtSessChngdProtocol = _TmnxBfdOnLspExtSessChngdProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 4, 3),
    _TmnxBfdOnLspExtSessChngdProtocol_Type()
)
tmnxBfdOnLspExtSessChngdProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessChngdProtocol.setStatus("current")


class _TmnxBfdOnLspExtSessProtoChngdSta_Type(Integer32):
    """Custom type tmnxBfdOnLspExtSessProtoChngdSta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("added", 0),
          ("cleared", 1))
    )


_TmnxBfdOnLspExtSessProtoChngdSta_Type.__name__ = "Integer32"
_TmnxBfdOnLspExtSessProtoChngdSta_Object = MibScalar
tmnxBfdOnLspExtSessProtoChngdSta = _TmnxBfdOnLspExtSessProtoChngdSta_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 4, 4),
    _TmnxBfdOnLspExtSessProtoChngdSta_Type()
)
tmnxBfdOnLspExtSessProtoChngdSta.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessProtoChngdSta.setStatus("current")
_TmnxBfdSeamlessBfdObjects_ObjectIdentity = ObjectIdentity
tmnxBfdSeamlessBfdObjects = _TmnxBfdSeamlessBfdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 5)
)
_TmnxBfdSeamlessBfdPeerTable_Object = MibTable
tmnxBfdSeamlessBfdPeerTable = _TmnxBfdSeamlessBfdPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 5, 1)
)
if mibBuilder.loadTexts:
    tmnxBfdSeamlessBfdPeerTable.setStatus("current")
_TmnxBfdSeamlessBfdPeerEntry_Object = MibTableRow
tmnxBfdSeamlessBfdPeerEntry = _TmnxBfdSeamlessBfdPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 5, 1, 1)
)
tmnxBfdSeamlessBfdPeerEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-BFD-MIB", "tmnxBfdSeamlessBfdPeerAddrType"),
    (0, "TIMETRA-BFD-MIB", "tmnxBfdSeamlessBfdPeerAddress"),
)
if mibBuilder.loadTexts:
    tmnxBfdSeamlessBfdPeerEntry.setStatus("current")
_TmnxBfdSeamlessBfdPeerAddrType_Type = InetAddressType
_TmnxBfdSeamlessBfdPeerAddrType_Object = MibTableColumn
tmnxBfdSeamlessBfdPeerAddrType = _TmnxBfdSeamlessBfdPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 5, 1, 1, 1),
    _TmnxBfdSeamlessBfdPeerAddrType_Type()
)
tmnxBfdSeamlessBfdPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBfdSeamlessBfdPeerAddrType.setStatus("current")


class _TmnxBfdSeamlessBfdPeerAddress_Type(InetAddress):
    """Custom type tmnxBfdSeamlessBfdPeerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_TmnxBfdSeamlessBfdPeerAddress_Type.__name__ = "InetAddress"
_TmnxBfdSeamlessBfdPeerAddress_Object = MibTableColumn
tmnxBfdSeamlessBfdPeerAddress = _TmnxBfdSeamlessBfdPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 5, 1, 1, 2),
    _TmnxBfdSeamlessBfdPeerAddress_Type()
)
tmnxBfdSeamlessBfdPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBfdSeamlessBfdPeerAddress.setStatus("current")
_TmnxBfdSeamlessBfdPeerRowStatus_Type = RowStatus
_TmnxBfdSeamlessBfdPeerRowStatus_Object = MibTableColumn
tmnxBfdSeamlessBfdPeerRowStatus = _TmnxBfdSeamlessBfdPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 5, 1, 1, 3),
    _TmnxBfdSeamlessBfdPeerRowStatus_Type()
)
tmnxBfdSeamlessBfdPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBfdSeamlessBfdPeerRowStatus.setStatus("current")


class _TmnxBfdSeamlessBfdPeerDiscr_Type(Unsigned32):
    """Custom type tmnxBfdSeamlessBfdPeerDiscr based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_TmnxBfdSeamlessBfdPeerDiscr_Type.__name__ = "Unsigned32"
_TmnxBfdSeamlessBfdPeerDiscr_Object = MibTableColumn
tmnxBfdSeamlessBfdPeerDiscr = _TmnxBfdSeamlessBfdPeerDiscr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 5, 1, 1, 4),
    _TmnxBfdSeamlessBfdPeerDiscr_Type()
)
tmnxBfdSeamlessBfdPeerDiscr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBfdSeamlessBfdPeerDiscr.setStatus("current")
_TmnxBfdSeamlessBfdReflectorTable_Object = MibTable
tmnxBfdSeamlessBfdReflectorTable = _TmnxBfdSeamlessBfdReflectorTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 5, 2)
)
if mibBuilder.loadTexts:
    tmnxBfdSeamlessBfdReflectorTable.setStatus("current")
_TmnxBfdSeamlessBfdReflectorEntry_Object = MibTableRow
tmnxBfdSeamlessBfdReflectorEntry = _TmnxBfdSeamlessBfdReflectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 5, 2, 1)
)
tmnxBfdSeamlessBfdReflectorEntry.setIndexNames(
    (0, "TIMETRA-BFD-MIB", "tmnxBfdSeamlessBfdReflName"),
)
if mibBuilder.loadTexts:
    tmnxBfdSeamlessBfdReflectorEntry.setStatus("current")
_TmnxBfdSeamlessBfdReflName_Type = TNamedItem
_TmnxBfdSeamlessBfdReflName_Object = MibTableColumn
tmnxBfdSeamlessBfdReflName = _TmnxBfdSeamlessBfdReflName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 5, 2, 1, 1),
    _TmnxBfdSeamlessBfdReflName_Type()
)
tmnxBfdSeamlessBfdReflName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxBfdSeamlessBfdReflName.setStatus("current")
_TmnxBfdSeamlessBfdReflRowStatus_Type = RowStatus
_TmnxBfdSeamlessBfdReflRowStatus_Object = MibTableColumn
tmnxBfdSeamlessBfdReflRowStatus = _TmnxBfdSeamlessBfdReflRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 5, 2, 1, 2),
    _TmnxBfdSeamlessBfdReflRowStatus_Type()
)
tmnxBfdSeamlessBfdReflRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBfdSeamlessBfdReflRowStatus.setStatus("current")


class _TmnxBfdSeamlessBfdReflAdminState_Type(TmnxAdminState):
    """Custom type tmnxBfdSeamlessBfdReflAdminState based on TmnxAdminState"""
    defaultValue = 3


_TmnxBfdSeamlessBfdReflAdminState_Type.__name__ = "TmnxAdminState"
_TmnxBfdSeamlessBfdReflAdminState_Object = MibTableColumn
tmnxBfdSeamlessBfdReflAdminState = _TmnxBfdSeamlessBfdReflAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 5, 2, 1, 3),
    _TmnxBfdSeamlessBfdReflAdminState_Type()
)
tmnxBfdSeamlessBfdReflAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBfdSeamlessBfdReflAdminState.setStatus("current")


class _TmnxBfdSeamlessBfdReflDiscr_Type(Unsigned32):
    """Custom type tmnxBfdSeamlessBfdReflDiscr based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(524288, 526335),
    )


_TmnxBfdSeamlessBfdReflDiscr_Type.__name__ = "Unsigned32"
_TmnxBfdSeamlessBfdReflDiscr_Object = MibTableColumn
tmnxBfdSeamlessBfdReflDiscr = _TmnxBfdSeamlessBfdReflDiscr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 5, 2, 1, 4),
    _TmnxBfdSeamlessBfdReflDiscr_Type()
)
tmnxBfdSeamlessBfdReflDiscr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBfdSeamlessBfdReflDiscr.setStatus("current")


class _TmnxBfdSeamlessBfdReflDescr_Type(TItemDescription):
    """Custom type tmnxBfdSeamlessBfdReflDescr based on TItemDescription"""
    defaultValue = OctetString("")


_TmnxBfdSeamlessBfdReflDescr_Type.__name__ = "TItemDescription"
_TmnxBfdSeamlessBfdReflDescr_Object = MibTableColumn
tmnxBfdSeamlessBfdReflDescr = _TmnxBfdSeamlessBfdReflDescr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 5, 2, 1, 5),
    _TmnxBfdSeamlessBfdReflDescr_Type()
)
tmnxBfdSeamlessBfdReflDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBfdSeamlessBfdReflDescr.setStatus("current")


class _TmnxBfdSeamlessBfdReflLocalState_Type(Integer32):
    """Custom type tmnxBfdSeamlessBfdReflLocalState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adminDown", 0),
          ("up", 3))
    )


_TmnxBfdSeamlessBfdReflLocalState_Type.__name__ = "Integer32"
_TmnxBfdSeamlessBfdReflLocalState_Object = MibTableColumn
tmnxBfdSeamlessBfdReflLocalState = _TmnxBfdSeamlessBfdReflLocalState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 85, 5, 2, 1, 6),
    _TmnxBfdSeamlessBfdReflLocalState_Type()
)
tmnxBfdSeamlessBfdReflLocalState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tmnxBfdSeamlessBfdReflLocalState.setStatus("current")
_TmnxBfdNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxBfdNotifyPrefix = _TmnxBfdNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 85)
)
_TmnxBfdNotifications_ObjectIdentity = ObjectIdentity
tmnxBfdNotifications = _TmnxBfdNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 85, 0)
)

# Managed Objects groups

tmnxBfdV11v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85, 2, 1)
)
tmnxBfdV11v0Group.setObjects(
      *(("TIMETRA-BFD-MIB", "tmnxBfdAdminOwner"),
        ("TIMETRA-BFD-MIB", "tmnxBfdAdminControlApply"),
        ("TIMETRA-BFD-MIB", "tmnxBfdAdminLastSetTimer"),
        ("TIMETRA-BFD-MIB", "tmnxBfdAdminLastSetTimeout"),
        ("TIMETRA-BFD-MIB", "tmnxBfdAdminTemplateRowStatus"),
        ("TIMETRA-BFD-MIB", "tmnxBfdAdminTemplateTxInt"),
        ("TIMETRA-BFD-MIB", "tmnxBfdAdminTemplateRxInt"),
        ("TIMETRA-BFD-MIB", "tmnxBfdAdminTemplateMultiplier"),
        ("TIMETRA-BFD-MIB", "tmnxBfdAdminTemplateEchoRxInt"),
        ("TIMETRA-BFD-MIB", "tmnxBfdAdminTemplateType"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOperTemplateRowStatus"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOperTemplateTxInt"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOperTemplateRxInt"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOperTemplateMultiplier"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOperTemplateEchoRxInt"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOperTemplateType"))
)
if mibBuilder.loadTexts:
    tmnxBfdV11v0Group.setStatus("current")

tmnxBfdV13v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85, 2, 2)
)
tmnxBfdV13v0Group.setObjects(
      *(("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessOperState"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessState"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessOperFlags"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessMesgRecv"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessMesgSent"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessLastDownTime"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessLastUpTime"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessUpCount"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessDownCount"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessLclDisc"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessRemDisc"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessProtocols"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessTxInterval"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessRxInterval"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessType"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessVerMismatch"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessTimeSinceLastRx"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessTimeSinceLastTx"))
)
if mibBuilder.loadTexts:
    tmnxBfdV13v0Group.setStatus("current")

tmnxBfdV13v0NotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85, 2, 3)
)
tmnxBfdV13v0NotifyObjsGroup.setObjects(
      *(("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessChangedProtocol"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessProtoChngdState"))
)
if mibBuilder.loadTexts:
    tmnxBfdV13v0NotifyObjsGroup.setStatus("current")

tmnxBfdV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85, 2, 7)
)
tmnxBfdV19v0Group.setObjects(
      *(("TIMETRA-BFD-MIB", "tmnxBfdSeamlessBfdPeerRowStatus"),
        ("TIMETRA-BFD-MIB", "tmnxBfdSeamlessBfdPeerDiscr"),
        ("TIMETRA-BFD-MIB", "tmnxBfdSeamlessBfdReflRowStatus"),
        ("TIMETRA-BFD-MIB", "tmnxBfdSeamlessBfdReflAdminState"),
        ("TIMETRA-BFD-MIB", "tmnxBfdSeamlessBfdReflDiscr"),
        ("TIMETRA-BFD-MIB", "tmnxBfdSeamlessBfdReflDescr"),
        ("TIMETRA-BFD-MIB", "tmnxBfdSeamlessBfdReflLocalState"))
)
if mibBuilder.loadTexts:
    tmnxBfdV19v0Group.setStatus("current")

tmnxBfdV20v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85, 2, 8)
)
tmnxBfdV20v0Group.setObjects(
      *(("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessOperState"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessState"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessOperFlags"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessMesgRecv"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessMesgSent"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessLastDownTime"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessLastUpTime"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessUpCount"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessDownCount"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessLclDisc"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessRemDisc"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessProtocols"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessTxInterval"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessRxInterval"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessType"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessVerMismatch"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessTimeSinceRx"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessTimeSinceTx"))
)
if mibBuilder.loadTexts:
    tmnxBfdV20v0Group.setStatus("current")

tmnxBfdV20v0NotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85, 2, 9)
)
tmnxBfdV20v0NotifyObjsGroup.setObjects(
      *(("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessChngdProtocol"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessProtoChngdSta"))
)
if mibBuilder.loadTexts:
    tmnxBfdV20v0NotifyObjsGroup.setStatus("current")


# Notification objects

tmnxBfdOnLspSessDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 85, 0, 1)
)
tmnxBfdOnLspSessDown.setObjects(
      *(("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessLclDisc"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessOperFlags"))
)
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessDown.setStatus(
        "current"
    )

tmnxBfdOnLspSessUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 85, 0, 2)
)
tmnxBfdOnLspSessUp.setObjects(
    ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessLclDisc")
)
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessUp.setStatus(
        "current"
    )

tmnxBfdOnLspSessDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 85, 0, 3)
)
tmnxBfdOnLspSessDeleted.setObjects(
      *(("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessLclDisc"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessOperFlags"))
)
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessDeleted.setStatus(
        "current"
    )

tmnxBfdOnLspSessProtChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 85, 0, 4)
)
tmnxBfdOnLspSessProtChange.setObjects(
      *(("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessLclDisc"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessProtocols"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessChangedProtocol"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessProtoChngdState"))
)
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessProtChange.setStatus(
        "current"
    )

tmnxBfdOnLspSessNoCpmNpResources = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 85, 0, 5)
)
tmnxBfdOnLspSessNoCpmNpResources.setObjects(
    ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessLclDisc")
)
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessNoCpmNpResources.setStatus(
        "current"
    )

tmnxBfdOnLspSessNoTailResources = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 85, 0, 6)
)
tmnxBfdOnLspSessNoTailResources.setObjects(
      *(("TIMETRA-VRTR-MIB", "vRtrLspBfdSession"),
        ("TIMETRA-VRTR-MIB", "vRtrLspBfdMaxSessions"))
)
if mibBuilder.loadTexts:
    tmnxBfdOnLspSessNoTailResources.setStatus(
        "current"
    )

tmnxBfdOnLspExtSessDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 85, 0, 7)
)
tmnxBfdOnLspExtSessDown.setObjects(
      *(("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessLclDisc"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessOperFlags"))
)
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessDown.setStatus(
        "current"
    )

tmnxBfdOnLspExtSessUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 85, 0, 8)
)
tmnxBfdOnLspExtSessUp.setObjects(
    ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessLclDisc")
)
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessUp.setStatus(
        "current"
    )

tmnxBfdOnLspExtSessDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 85, 0, 9)
)
tmnxBfdOnLspExtSessDeleted.setObjects(
      *(("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessLclDisc"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessOperFlags"))
)
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessDeleted.setStatus(
        "current"
    )

tmnxBfdOnLspExtSessProtChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 85, 0, 10)
)
tmnxBfdOnLspExtSessProtChange.setObjects(
      *(("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessLclDisc"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessProtocols"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessChngdProtocol"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessProtoChngdSta"))
)
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessProtChange.setStatus(
        "current"
    )

tmnxBfdOnLspExtSessNoCpmNpResrcs = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 85, 0, 11)
)
tmnxBfdOnLspExtSessNoCpmNpResrcs.setObjects(
    ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessLclDisc")
)
if mibBuilder.loadTexts:
    tmnxBfdOnLspExtSessNoCpmNpResrcs.setStatus(
        "current"
    )


# Notifications groups

tmnxBfdV13v0NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85, 2, 4)
)
tmnxBfdV13v0NotificationGroup.setObjects(
      *(("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessDown"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessUp"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessDeleted"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessProtChange"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessNoCpmNpResources"))
)
if mibBuilder.loadTexts:
    tmnxBfdV13v0NotificationGroup.setStatus(
        "current"
    )

tmnxBfdV15v0NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85, 2, 6)
)
tmnxBfdV15v0NotificationGroup.setObjects(
    ("TIMETRA-BFD-MIB", "tmnxBfdOnLspSessNoTailResources")
)
if mibBuilder.loadTexts:
    tmnxBfdV15v0NotificationGroup.setStatus(
        "current"
    )

tmnxBfdV20v0NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85, 2, 10)
)
tmnxBfdV20v0NotificationGroup.setObjects(
      *(("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessDown"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessUp"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessDeleted"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessProtChange"),
        ("TIMETRA-BFD-MIB", "tmnxBfdOnLspExtSessNoCpmNpResrcs"))
)
if mibBuilder.loadTexts:
    tmnxBfdV20v0NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxBfdV11v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85, 1, 1)
)
tmnxBfdV11v0Compliance.setObjects(
      *(("TIMETRA-BFD-MIB", "tmnxBfdV11v0Group"),
        ("TIMETRA-BFD-MIB", "tmnxBfdV13v0Group"),
        ("TIMETRA-BFD-MIB", "tmnxBfdV13v0NotifyObjsGroup"),
        ("TIMETRA-BFD-MIB", "tmnxBfdV13v0NotificationGroup"))
)
if mibBuilder.loadTexts:
    tmnxBfdV11v0Compliance.setStatus(
        "current"
    )

tmnxBfdV15v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85, 1, 5)
)
tmnxBfdV15v0Compliance.setObjects(
    ("TIMETRA-BFD-MIB", "tmnxBfdV15v0NotificationGroup")
)
if mibBuilder.loadTexts:
    tmnxBfdV15v0Compliance.setStatus(
        "current"
    )

tmnxBfdV19v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85, 1, 6)
)
tmnxBfdV19v0Compliance.setObjects(
    ("TIMETRA-BFD-MIB", "tmnxBfdV19v0Group")
)
if mibBuilder.loadTexts:
    tmnxBfdV19v0Compliance.setStatus(
        "current"
    )

tmnxBfdV20v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 85, 1, 7)
)
tmnxBfdV20v0Compliance.setObjects(
      *(("TIMETRA-BFD-MIB", "tmnxBfdV20v0Group"),
        ("TIMETRA-BFD-MIB", "tmnxBfdV20v0NotifyObjsGroup"),
        ("TIMETRA-BFD-MIB", "tmnxBfdV20v0NotificationGroup"))
)
if mibBuilder.loadTexts:
    tmnxBfdV20v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-BFD-MIB",
    **{"timetraBfdMIBModule": timetraBfdMIBModule,
       "tmnxBfdConformance": tmnxBfdConformance,
       "tmnxBfdCompliances": tmnxBfdCompliances,
       "tmnxBfdV11v0Compliance": tmnxBfdV11v0Compliance,
       "tmnxBfdV15v0Compliance": tmnxBfdV15v0Compliance,
       "tmnxBfdV19v0Compliance": tmnxBfdV19v0Compliance,
       "tmnxBfdV20v0Compliance": tmnxBfdV20v0Compliance,
       "tmnxBfdGroups": tmnxBfdGroups,
       "tmnxBfdV11v0Group": tmnxBfdV11v0Group,
       "tmnxBfdV13v0Group": tmnxBfdV13v0Group,
       "tmnxBfdV13v0NotifyObjsGroup": tmnxBfdV13v0NotifyObjsGroup,
       "tmnxBfdV13v0NotificationGroup": tmnxBfdV13v0NotificationGroup,
       "tmnxBfdV15v0NotificationGroup": tmnxBfdV15v0NotificationGroup,
       "tmnxBfdV19v0Group": tmnxBfdV19v0Group,
       "tmnxBfdV20v0Group": tmnxBfdV20v0Group,
       "tmnxBfdV20v0NotifyObjsGroup": tmnxBfdV20v0NotifyObjsGroup,
       "tmnxBfdV20v0NotificationGroup": tmnxBfdV20v0NotificationGroup,
       "tmnxBfdObjects": tmnxBfdObjects,
       "tmnxBfdOperObjects": tmnxBfdOperObjects,
       "tmnxBfdOperValueObjects": tmnxBfdOperValueObjects,
       "tmnxBfdOperTemplateTable": tmnxBfdOperTemplateTable,
       "tmnxBfdOperTemplateEntry": tmnxBfdOperTemplateEntry,
       "tmnxBfdOperTemplateName": tmnxBfdOperTemplateName,
       "tmnxBfdOperTemplateRowStatus": tmnxBfdOperTemplateRowStatus,
       "tmnxBfdOperTemplateTxInt": tmnxBfdOperTemplateTxInt,
       "tmnxBfdOperTemplateRxInt": tmnxBfdOperTemplateRxInt,
       "tmnxBfdOperTemplateMultiplier": tmnxBfdOperTemplateMultiplier,
       "tmnxBfdOperTemplateEchoRxInt": tmnxBfdOperTemplateEchoRxInt,
       "tmnxBfdOperTemplateType": tmnxBfdOperTemplateType,
       "tmnxBfdAdminObjects": tmnxBfdAdminObjects,
       "tmnxBfdAdminControlObjects": tmnxBfdAdminControlObjects,
       "tmnxBfdAdminOwner": tmnxBfdAdminOwner,
       "tmnxBfdAdminControlApply": tmnxBfdAdminControlApply,
       "tmnxBfdAdminLastSetTimer": tmnxBfdAdminLastSetTimer,
       "tmnxBfdAdminLastSetTimeout": tmnxBfdAdminLastSetTimeout,
       "tmnxBfdAdminValueObjects": tmnxBfdAdminValueObjects,
       "tmnxBfdAdminTemplateTable": tmnxBfdAdminTemplateTable,
       "tmnxBfdAdminTemplateEntry": tmnxBfdAdminTemplateEntry,
       "tmnxBfdAdminTemplateName": tmnxBfdAdminTemplateName,
       "tmnxBfdAdminTemplateRowStatus": tmnxBfdAdminTemplateRowStatus,
       "tmnxBfdAdminTemplateTxInt": tmnxBfdAdminTemplateTxInt,
       "tmnxBfdAdminTemplateRxInt": tmnxBfdAdminTemplateRxInt,
       "tmnxBfdAdminTemplateMultiplier": tmnxBfdAdminTemplateMultiplier,
       "tmnxBfdAdminTemplateEchoRxInt": tmnxBfdAdminTemplateEchoRxInt,
       "tmnxBfdAdminTemplateType": tmnxBfdAdminTemplateType,
       "tmnxBfdStatistics": tmnxBfdStatistics,
       "tmnxBfdOnLspSessTable": tmnxBfdOnLspSessTable,
       "tmnxBfdOnLspSessEntry": tmnxBfdOnLspSessEntry,
       "tmnxBfdOnLspSessLinkType": tmnxBfdOnLspSessLinkType,
       "tmnxBfdOnLspSessFecType": tmnxBfdOnLspSessFecType,
       "tmnxBfdOnLspSessRemAddrType": tmnxBfdOnLspSessRemAddrType,
       "tmnxBfdOnLspSessRemAddr": tmnxBfdOnLspSessRemAddr,
       "tmnxBfdOnLspSessLclAddrType": tmnxBfdOnLspSessLclAddrType,
       "tmnxBfdOnLspSessLclAddr": tmnxBfdOnLspSessLclAddr,
       "tmnxBfdOnLspSessPathId": tmnxBfdOnLspSessPathId,
       "tmnxBfdOnLspSessTunnelId": tmnxBfdOnLspSessTunnelId,
       "tmnxBfdOnLspSessOperState": tmnxBfdOnLspSessOperState,
       "tmnxBfdOnLspSessState": tmnxBfdOnLspSessState,
       "tmnxBfdOnLspSessOperFlags": tmnxBfdOnLspSessOperFlags,
       "tmnxBfdOnLspSessMesgRecv": tmnxBfdOnLspSessMesgRecv,
       "tmnxBfdOnLspSessMesgSent": tmnxBfdOnLspSessMesgSent,
       "tmnxBfdOnLspSessLastDownTime": tmnxBfdOnLspSessLastDownTime,
       "tmnxBfdOnLspSessLastUpTime": tmnxBfdOnLspSessLastUpTime,
       "tmnxBfdOnLspSessUpCount": tmnxBfdOnLspSessUpCount,
       "tmnxBfdOnLspSessDownCount": tmnxBfdOnLspSessDownCount,
       "tmnxBfdOnLspSessLclDisc": tmnxBfdOnLspSessLclDisc,
       "tmnxBfdOnLspSessRemDisc": tmnxBfdOnLspSessRemDisc,
       "tmnxBfdOnLspSessProtocols": tmnxBfdOnLspSessProtocols,
       "tmnxBfdOnLspSessTxInterval": tmnxBfdOnLspSessTxInterval,
       "tmnxBfdOnLspSessRxInterval": tmnxBfdOnLspSessRxInterval,
       "tmnxBfdOnLspSessType": tmnxBfdOnLspSessType,
       "tmnxBfdOnLspSessVerMismatch": tmnxBfdOnLspSessVerMismatch,
       "tmnxBfdOnLspSessTimeSinceLastRx": tmnxBfdOnLspSessTimeSinceLastRx,
       "tmnxBfdOnLspSessTimeSinceLastTx": tmnxBfdOnLspSessTimeSinceLastTx,
       "tmnxBfdOnLspExtSessTable": tmnxBfdOnLspExtSessTable,
       "tmnxBfdOnLspExtSessEntry": tmnxBfdOnLspExtSessEntry,
       "tmnxBfdOnLspExtSessLinkType": tmnxBfdOnLspExtSessLinkType,
       "tmnxBfdOnLspExtSessFecType": tmnxBfdOnLspExtSessFecType,
       "tmnxBfdOnLspExtSessRemAddrType": tmnxBfdOnLspExtSessRemAddrType,
       "tmnxBfdOnLspExtSessRemAddr": tmnxBfdOnLspExtSessRemAddr,
       "tmnxBfdOnLspExtSessLclAddrType": tmnxBfdOnLspExtSessLclAddrType,
       "tmnxBfdOnLspExtSessLclAddr": tmnxBfdOnLspExtSessLclAddr,
       "tmnxBfdOnLspExtSessPathId": tmnxBfdOnLspExtSessPathId,
       "tmnxBfdOnLspExtSessTunnelId": tmnxBfdOnLspExtSessTunnelId,
       "tmnxBfdOnLspExtSessInfoId": tmnxBfdOnLspExtSessInfoId,
       "tmnxBfdOnLspExtSessOperState": tmnxBfdOnLspExtSessOperState,
       "tmnxBfdOnLspExtSessState": tmnxBfdOnLspExtSessState,
       "tmnxBfdOnLspExtSessOperFlags": tmnxBfdOnLspExtSessOperFlags,
       "tmnxBfdOnLspExtSessMesgRecv": tmnxBfdOnLspExtSessMesgRecv,
       "tmnxBfdOnLspExtSessMesgSent": tmnxBfdOnLspExtSessMesgSent,
       "tmnxBfdOnLspExtSessLastDownTime": tmnxBfdOnLspExtSessLastDownTime,
       "tmnxBfdOnLspExtSessLastUpTime": tmnxBfdOnLspExtSessLastUpTime,
       "tmnxBfdOnLspExtSessUpCount": tmnxBfdOnLspExtSessUpCount,
       "tmnxBfdOnLspExtSessDownCount": tmnxBfdOnLspExtSessDownCount,
       "tmnxBfdOnLspExtSessLclDisc": tmnxBfdOnLspExtSessLclDisc,
       "tmnxBfdOnLspExtSessRemDisc": tmnxBfdOnLspExtSessRemDisc,
       "tmnxBfdOnLspExtSessProtocols": tmnxBfdOnLspExtSessProtocols,
       "tmnxBfdOnLspExtSessTxInterval": tmnxBfdOnLspExtSessTxInterval,
       "tmnxBfdOnLspExtSessRxInterval": tmnxBfdOnLspExtSessRxInterval,
       "tmnxBfdOnLspExtSessType": tmnxBfdOnLspExtSessType,
       "tmnxBfdOnLspExtSessVerMismatch": tmnxBfdOnLspExtSessVerMismatch,
       "tmnxBfdOnLspExtSessTimeSinceRx": tmnxBfdOnLspExtSessTimeSinceRx,
       "tmnxBfdOnLspExtSessTimeSinceTx": tmnxBfdOnLspExtSessTimeSinceTx,
       "tmnxBfdNotifyObjects": tmnxBfdNotifyObjects,
       "tmnxBfdOnLspSessChangedProtocol": tmnxBfdOnLspSessChangedProtocol,
       "tmnxBfdOnLspSessProtoChngdState": tmnxBfdOnLspSessProtoChngdState,
       "tmnxBfdOnLspExtSessChngdProtocol": tmnxBfdOnLspExtSessChngdProtocol,
       "tmnxBfdOnLspExtSessProtoChngdSta": tmnxBfdOnLspExtSessProtoChngdSta,
       "tmnxBfdSeamlessBfdObjects": tmnxBfdSeamlessBfdObjects,
       "tmnxBfdSeamlessBfdPeerTable": tmnxBfdSeamlessBfdPeerTable,
       "tmnxBfdSeamlessBfdPeerEntry": tmnxBfdSeamlessBfdPeerEntry,
       "tmnxBfdSeamlessBfdPeerAddrType": tmnxBfdSeamlessBfdPeerAddrType,
       "tmnxBfdSeamlessBfdPeerAddress": tmnxBfdSeamlessBfdPeerAddress,
       "tmnxBfdSeamlessBfdPeerRowStatus": tmnxBfdSeamlessBfdPeerRowStatus,
       "tmnxBfdSeamlessBfdPeerDiscr": tmnxBfdSeamlessBfdPeerDiscr,
       "tmnxBfdSeamlessBfdReflectorTable": tmnxBfdSeamlessBfdReflectorTable,
       "tmnxBfdSeamlessBfdReflectorEntry": tmnxBfdSeamlessBfdReflectorEntry,
       "tmnxBfdSeamlessBfdReflName": tmnxBfdSeamlessBfdReflName,
       "tmnxBfdSeamlessBfdReflRowStatus": tmnxBfdSeamlessBfdReflRowStatus,
       "tmnxBfdSeamlessBfdReflAdminState": tmnxBfdSeamlessBfdReflAdminState,
       "tmnxBfdSeamlessBfdReflDiscr": tmnxBfdSeamlessBfdReflDiscr,
       "tmnxBfdSeamlessBfdReflDescr": tmnxBfdSeamlessBfdReflDescr,
       "tmnxBfdSeamlessBfdReflLocalState": tmnxBfdSeamlessBfdReflLocalState,
       "tmnxBfdNotifyPrefix": tmnxBfdNotifyPrefix,
       "tmnxBfdNotifications": tmnxBfdNotifications,
       "tmnxBfdOnLspSessDown": tmnxBfdOnLspSessDown,
       "tmnxBfdOnLspSessUp": tmnxBfdOnLspSessUp,
       "tmnxBfdOnLspSessDeleted": tmnxBfdOnLspSessDeleted,
       "tmnxBfdOnLspSessProtChange": tmnxBfdOnLspSessProtChange,
       "tmnxBfdOnLspSessNoCpmNpResources": tmnxBfdOnLspSessNoCpmNpResources,
       "tmnxBfdOnLspSessNoTailResources": tmnxBfdOnLspSessNoTailResources,
       "tmnxBfdOnLspExtSessDown": tmnxBfdOnLspExtSessDown,
       "tmnxBfdOnLspExtSessUp": tmnxBfdOnLspExtSessUp,
       "tmnxBfdOnLspExtSessDeleted": tmnxBfdOnLspExtSessDeleted,
       "tmnxBfdOnLspExtSessProtChange": tmnxBfdOnLspExtSessProtChange,
       "tmnxBfdOnLspExtSessNoCpmNpResrcs": tmnxBfdOnLspExtSessNoCpmNpResrcs}
)
