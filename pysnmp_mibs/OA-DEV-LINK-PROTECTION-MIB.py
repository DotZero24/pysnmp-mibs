# SNMP MIB module (OA-DEV-LINK-PROTECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OA-DEV-LINK-PROTECTION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:10 2025
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

(nbSwitchG1Il,) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "nbSwitchG1Il")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

oaDeviceLinkProtection = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24)
)
if mibBuilder.loadTexts:
    oaDeviceLinkProtection.setRevisions(
        ("2020-06-16 00:00",
         "2018-12-24 00:00",
         "2016-07-13 00:00",
         "2007-12-11 00:00",
         "2007-08-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbDeviceConfig_ObjectIdentity = ObjectIdentity
nbDeviceConfig = _NbDeviceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11)
)
_NbDevGen_ObjectIdentity = ObjectIdentity
nbDevGen = _NbDevGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1)
)
_OaDevLosNotifications_ObjectIdentity = ObjectIdentity
oaDevLosNotifications = _OaDevLosNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 0)
)
_OaDevLosGen_ObjectIdentity = ObjectIdentity
oaDevLosGen = _OaDevLosGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 1)
)


class _OaDevLosGenSupport_Type(Integer32):
    """Custom type oaDevLosGenSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_OaDevLosGenSupport_Type.__name__ = "Integer32"
_OaDevLosGenSupport_Object = MibScalar
oaDevLosGenSupport = _OaDevLosGenSupport_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 1, 1),
    _OaDevLosGenSupport_Type()
)
oaDevLosGenSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDevLosGenSupport.setStatus("current")


class _OaDevLosAgSupport_Type(Integer32):
    """Custom type oaDevLosAgSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_OaDevLosAgSupport_Type.__name__ = "Integer32"
_OaDevLosAgSupport_Object = MibScalar
oaDevLosAgSupport = _OaDevLosAgSupport_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 1, 2),
    _OaDevLosAgSupport_Type()
)
oaDevLosAgSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDevLosAgSupport.setStatus("current")
_OaDevLosGrp_ObjectIdentity = ObjectIdentity
oaDevLosGrp = _OaDevLosGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2)
)
_OaDevLosGrTable_Object = MibTable
oaDevLosGrTable = _OaDevLosGrTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 5)
)
if mibBuilder.loadTexts:
    oaDevLosGrTable.setStatus("current")
_OaDevLosGrEntry_Object = MibTableRow
oaDevLosGrEntry = _OaDevLosGrEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 5, 1)
)
oaDevLosGrEntry.setIndexNames(
    (0, "OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrId"),
)
if mibBuilder.loadTexts:
    oaDevLosGrEntry.setStatus("current")


class _OaDevLosGrId_Type(Integer32):
    """Custom type oaDevLosGrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OaDevLosGrId_Type.__name__ = "Integer32"
_OaDevLosGrId_Object = MibTableColumn
oaDevLosGrId = _OaDevLosGrId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 5, 1, 1),
    _OaDevLosGrId_Type()
)
oaDevLosGrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaDevLosGrId.setStatus("current")


class _OaDevLosGrPrimaryPort_Type(Integer32):
    """Custom type oaDevLosGrPrimaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_OaDevLosGrPrimaryPort_Type.__name__ = "Integer32"
_OaDevLosGrPrimaryPort_Object = MibTableColumn
oaDevLosGrPrimaryPort = _OaDevLosGrPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 5, 1, 2),
    _OaDevLosGrPrimaryPort_Type()
)
oaDevLosGrPrimaryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevLosGrPrimaryPort.setStatus("current")


class _OaDevLosGrSecondaryPort_Type(Integer32):
    """Custom type oaDevLosGrSecondaryPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_OaDevLosGrSecondaryPort_Type.__name__ = "Integer32"
_OaDevLosGrSecondaryPort_Object = MibTableColumn
oaDevLosGrSecondaryPort = _OaDevLosGrSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 5, 1, 3),
    _OaDevLosGrSecondaryPort_Type()
)
oaDevLosGrSecondaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDevLosGrSecondaryPort.setStatus("current")


class _OaDevLosGrProtectionMode_Type(Integer32):
    """Custom type oaDevLosGrProtectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("preemption", 2),
          ("notPreemption", 3))
    )


_OaDevLosGrProtectionMode_Type.__name__ = "Integer32"
_OaDevLosGrProtectionMode_Object = MibTableColumn
oaDevLosGrProtectionMode = _OaDevLosGrProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 5, 1, 4),
    _OaDevLosGrProtectionMode_Type()
)
oaDevLosGrProtectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevLosGrProtectionMode.setStatus("current")


class _OaDevLosGrEnableMode_Type(Integer32):
    """Custom type oaDevLosGrEnableMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("enable", 2),
          ("disable", 3))
    )


_OaDevLosGrEnableMode_Type.__name__ = "Integer32"
_OaDevLosGrEnableMode_Object = MibTableColumn
oaDevLosGrEnableMode = _OaDevLosGrEnableMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 5, 1, 5),
    _OaDevLosGrEnableMode_Type()
)
oaDevLosGrEnableMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevLosGrEnableMode.setStatus("current")
_OaDevLosGrActivePortNumber_Type = Integer32
_OaDevLosGrActivePortNumber_Object = MibTableColumn
oaDevLosGrActivePortNumber = _OaDevLosGrActivePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 5, 1, 6),
    _OaDevLosGrActivePortNumber_Type()
)
oaDevLosGrActivePortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevLosGrActivePortNumber.setStatus("current")


class _OaDevLosGrActionCause_Type(Integer32):
    """Custom type oaDevLosGrActionCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("portLinkUp", 2),
          ("portLinkDown", 3),
          ("agRMepDiscardEvent", 4),
          ("agRMepNoConnEvent", 5),
          ("agRMepAliveEvent", 6),
          ("activePortAdminSet", 7))
    )


_OaDevLosGrActionCause_Type.__name__ = "Integer32"
_OaDevLosGrActionCause_Object = MibTableColumn
oaDevLosGrActionCause = _OaDevLosGrActionCause_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 5, 1, 7),
    _OaDevLosGrActionCause_Type()
)
oaDevLosGrActionCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDevLosGrActionCause.setStatus("current")


class _OaDevLosGrWtrTimer_Type(Integer32):
    """Custom type oaDevLosGrWtrTimer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_OaDevLosGrWtrTimer_Type.__name__ = "Integer32"
_OaDevLosGrWtrTimer_Object = MibTableColumn
oaDevLosGrWtrTimer = _OaDevLosGrWtrTimer_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 5, 1, 8),
    _OaDevLosGrWtrTimer_Type()
)
oaDevLosGrWtrTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevLosGrWtrTimer.setStatus("current")
if mibBuilder.loadTexts:
    oaDevLosGrWtrTimer.setUnits("seconds")


class _OaDevLosGrConnectionId_Type(DisplayString):
    """Custom type oaDevLosGrConnectionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_OaDevLosGrConnectionId_Type.__name__ = "DisplayString"
_OaDevLosGrConnectionId_Object = MibTableColumn
oaDevLosGrConnectionId = _OaDevLosGrConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 5, 1, 9),
    _OaDevLosGrConnectionId_Type()
)
oaDevLosGrConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDevLosGrConnectionId.setStatus("current")


class _OaDevLosGrHoldOffTimer_Type(Integer32):
    """Custom type oaDevLosGrHoldOffTimer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_OaDevLosGrHoldOffTimer_Type.__name__ = "Integer32"
_OaDevLosGrHoldOffTimer_Object = MibTableColumn
oaDevLosGrHoldOffTimer = _OaDevLosGrHoldOffTimer_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 5, 1, 10),
    _OaDevLosGrHoldOffTimer_Type()
)
oaDevLosGrHoldOffTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevLosGrHoldOffTimer.setStatus("current")
if mibBuilder.loadTexts:
    oaDevLosGrHoldOffTimer.setUnits("seconds")


class _OaDevLosGrPollDelayTimer_Type(Integer32):
    """Custom type oaDevLosGrPollDelayTimer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_OaDevLosGrPollDelayTimer_Type.__name__ = "Integer32"
_OaDevLosGrPollDelayTimer_Object = MibTableColumn
oaDevLosGrPollDelayTimer = _OaDevLosGrPollDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 5, 1, 11),
    _OaDevLosGrPollDelayTimer_Type()
)
oaDevLosGrPollDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevLosGrPollDelayTimer.setStatus("current")
if mibBuilder.loadTexts:
    oaDevLosGrPollDelayTimer.setUnits("seconds")


class _OaDevLosGrToBackupTrapTimer_Type(Integer32):
    """Custom type oaDevLosGrToBackupTrapTimer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_OaDevLosGrToBackupTrapTimer_Type.__name__ = "Integer32"
_OaDevLosGrToBackupTrapTimer_Object = MibTableColumn
oaDevLosGrToBackupTrapTimer = _OaDevLosGrToBackupTrapTimer_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 5, 1, 12),
    _OaDevLosGrToBackupTrapTimer_Type()
)
oaDevLosGrToBackupTrapTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevLosGrToBackupTrapTimer.setStatus("current")
if mibBuilder.loadTexts:
    oaDevLosGrToBackupTrapTimer.setUnits("seconds")


class _OaDevLosGrToPrimaryTrapTimer_Type(Integer32):
    """Custom type oaDevLosGrToPrimaryTrapTimer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_OaDevLosGrToPrimaryTrapTimer_Type.__name__ = "Integer32"
_OaDevLosGrToPrimaryTrapTimer_Object = MibTableColumn
oaDevLosGrToPrimaryTrapTimer = _OaDevLosGrToPrimaryTrapTimer_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 5, 1, 13),
    _OaDevLosGrToPrimaryTrapTimer_Type()
)
oaDevLosGrToPrimaryTrapTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevLosGrToPrimaryTrapTimer.setStatus("current")
if mibBuilder.loadTexts:
    oaDevLosGrToPrimaryTrapTimer.setUnits("seconds")
_OaDevLosGrAgTable_Object = MibTable
oaDevLosGrAgTable = _OaDevLosGrAgTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 7)
)
if mibBuilder.loadTexts:
    oaDevLosGrAgTable.setStatus("current")
_OaDevLosGrAgEntry_Object = MibTableRow
oaDevLosGrAgEntry = _OaDevLosGrAgEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 7, 1)
)
oaDevLosGrAgEntry.setIndexNames(
    (0, "OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrId"),
    (0, "OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrAgDomainId"),
    (0, "OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrAgAssociationId"),
    (0, "OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrAgRemoteMep"),
)
if mibBuilder.loadTexts:
    oaDevLosGrAgEntry.setStatus("current")


class _OaDevLosGrAgDomainId_Type(Unsigned32):
    """Custom type oaDevLosGrAgDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_OaDevLosGrAgDomainId_Type.__name__ = "Unsigned32"
_OaDevLosGrAgDomainId_Object = MibTableColumn
oaDevLosGrAgDomainId = _OaDevLosGrAgDomainId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 7, 1, 2),
    _OaDevLosGrAgDomainId_Type()
)
oaDevLosGrAgDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaDevLosGrAgDomainId.setStatus("current")


class _OaDevLosGrAgAssociationId_Type(Unsigned32):
    """Custom type oaDevLosGrAgAssociationId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OaDevLosGrAgAssociationId_Type.__name__ = "Unsigned32"
_OaDevLosGrAgAssociationId_Object = MibTableColumn
oaDevLosGrAgAssociationId = _OaDevLosGrAgAssociationId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 7, 1, 3),
    _OaDevLosGrAgAssociationId_Type()
)
oaDevLosGrAgAssociationId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaDevLosGrAgAssociationId.setStatus("current")


class _OaDevLosGrAgRemoteMep_Type(Unsigned32):
    """Custom type oaDevLosGrAgRemoteMep based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_OaDevLosGrAgRemoteMep_Type.__name__ = "Unsigned32"
_OaDevLosGrAgRemoteMep_Object = MibTableColumn
oaDevLosGrAgRemoteMep = _OaDevLosGrAgRemoteMep_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 7, 1, 4),
    _OaDevLosGrAgRemoteMep_Type()
)
oaDevLosGrAgRemoteMep.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaDevLosGrAgRemoteMep.setStatus("current")


class _OaDevLosGrAgRMepStatus_Type(Integer32):
    """Custom type oaDevLosGrAgRMepStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("discard", 2),
          ("noConnection", 3))
    )


_OaDevLosGrAgRMepStatus_Type.__name__ = "Integer32"
_OaDevLosGrAgRMepStatus_Object = MibTableColumn
oaDevLosGrAgRMepStatus = _OaDevLosGrAgRMepStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 7, 1, 8),
    _OaDevLosGrAgRMepStatus_Type()
)
oaDevLosGrAgRMepStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaDevLosGrAgRMepStatus.setStatus("current")


class _OaDevLosGrAgAdminStatus_Type(Integer32):
    """Custom type oaDevLosGrAgAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_OaDevLosGrAgAdminStatus_Type.__name__ = "Integer32"
_OaDevLosGrAgAdminStatus_Object = MibTableColumn
oaDevLosGrAgAdminStatus = _OaDevLosGrAgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 7, 1, 10),
    _OaDevLosGrAgAdminStatus_Type()
)
oaDevLosGrAgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevLosGrAgAdminStatus.setStatus("current")


class _OaDevLosGrAgVid_Type(Unsigned32):
    """Custom type oaDevLosGrAgVid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_OaDevLosGrAgVid_Type.__name__ = "Unsigned32"
_OaDevLosGrAgVid_Object = MibTableColumn
oaDevLosGrAgVid = _OaDevLosGrAgVid_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 7, 1, 11),
    _OaDevLosGrAgVid_Type()
)
oaDevLosGrAgVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevLosGrAgVid.setStatus("current")
_OaDevLosGrMmuTable_Object = MibTable
oaDevLosGrMmuTable = _OaDevLosGrMmuTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 8)
)
if mibBuilder.loadTexts:
    oaDevLosGrMmuTable.setStatus("current")
_OaDevLosGrMmuEntry_Object = MibTableRow
oaDevLosGrMmuEntry = _OaDevLosGrMmuEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 8, 1)
)
oaDevLosGrMmuEntry.setIndexNames(
    (0, "OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrId"),
)
if mibBuilder.loadTexts:
    oaDevLosGrMmuEntry.setStatus("current")


class _OaDevLosGrMmuEnabled_Type(TruthValue):
    """Custom type oaDevLosGrMmuEnabled based on TruthValue"""
    defaultValue = 2


_OaDevLosGrMmuEnabled_Type.__name__ = "TruthValue"
_OaDevLosGrMmuEnabled_Object = MibTableColumn
oaDevLosGrMmuEnabled = _OaDevLosGrMmuEnabled_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 2, 8, 1, 2),
    _OaDevLosGrMmuEnabled_Type()
)
oaDevLosGrMmuEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaDevLosGrMmuEnabled.setStatus("current")
_OaDevLosConformance_ObjectIdentity = ObjectIdentity
oaDevLosConformance = _OaDevLosConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 101)
)
_OaDevLosMIBCompliances_ObjectIdentity = ObjectIdentity
oaDevLosMIBCompliances = _OaDevLosMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 101, 1)
)
_OaDevLosMIBGroups_ObjectIdentity = ObjectIdentity
oaDevLosMIBGroups = _OaDevLosMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 101, 2)
)

# Managed Objects groups

oaDevLosMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 101, 2, 1)
)
oaDevLosMandatoryGroup.setObjects(
      *(("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGenSupport"),
        ("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosAgSupport"),
        ("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrPrimaryPort"),
        ("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrSecondaryPort"),
        ("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrProtectionMode"),
        ("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrEnableMode"),
        ("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrActivePortNumber"),
        ("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrMmuEnabled"))
)
if mibBuilder.loadTexts:
    oaDevLosMandatoryGroup.setStatus("current")

oaPortLosTrapParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 101, 2, 2)
)
oaPortLosTrapParamsGroup.setObjects(
      *(("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrActionCause"),
        ("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrWtrTimer"),
        ("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrHoldOffTimer"),
        ("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrPollDelayTimer"),
        ("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrToBackupTrapTimer"),
        ("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrToPrimaryTrapTimer"),
        ("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrConnectionId"))
)
if mibBuilder.loadTexts:
    oaPortLosTrapParamsGroup.setStatus("current")

oaPortLosGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 101, 2, 3)
)
oaPortLosGroup.setObjects(
      *(("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrAgRMepStatus"),
        ("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrAgAdminStatus"),
        ("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrAgVid"))
)
if mibBuilder.loadTexts:
    oaPortLosGroup.setStatus("current")


# Notification objects

oaDevLosActivePortChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 0, 37)
)
oaDevLosActivePortChanged.setObjects(
      *(("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrActivePortNumber"),
        ("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrPrimaryPort"),
        ("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrSecondaryPort"),
        ("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrActionCause"),
        ("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosGrConnectionId"))
)
if mibBuilder.loadTexts:
    oaDevLosActivePortChanged.setStatus(
        "current"
    )


# Notifications groups

oaDevLosNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 101, 2, 4)
)
oaDevLosNotificationsGroup.setObjects(
    ("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosActivePortChanged")
)
if mibBuilder.loadTexts:
    oaDevLosNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

oaDevLosMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 11, 1, 24, 101, 1, 1)
)
oaDevLosMIBCompliance.setObjects(
      *(("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosMandatoryGroup"),
        ("OA-DEV-LINK-PROTECTION-MIB", "oaDevLosNotificationsGroup"),
        ("OA-DEV-LINK-PROTECTION-MIB", "oaPortLosTrapParamsGroup"),
        ("OA-DEV-LINK-PROTECTION-MIB", "oaPortLosGroup"))
)
if mibBuilder.loadTexts:
    oaDevLosMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OA-DEV-LINK-PROTECTION-MIB",
    **{"nbDeviceConfig": nbDeviceConfig,
       "nbDevGen": nbDevGen,
       "oaDeviceLinkProtection": oaDeviceLinkProtection,
       "oaDevLosNotifications": oaDevLosNotifications,
       "oaDevLosActivePortChanged": oaDevLosActivePortChanged,
       "oaDevLosGen": oaDevLosGen,
       "oaDevLosGenSupport": oaDevLosGenSupport,
       "oaDevLosAgSupport": oaDevLosAgSupport,
       "oaDevLosGrp": oaDevLosGrp,
       "oaDevLosGrTable": oaDevLosGrTable,
       "oaDevLosGrEntry": oaDevLosGrEntry,
       "oaDevLosGrId": oaDevLosGrId,
       "oaDevLosGrPrimaryPort": oaDevLosGrPrimaryPort,
       "oaDevLosGrSecondaryPort": oaDevLosGrSecondaryPort,
       "oaDevLosGrProtectionMode": oaDevLosGrProtectionMode,
       "oaDevLosGrEnableMode": oaDevLosGrEnableMode,
       "oaDevLosGrActivePortNumber": oaDevLosGrActivePortNumber,
       "oaDevLosGrActionCause": oaDevLosGrActionCause,
       "oaDevLosGrWtrTimer": oaDevLosGrWtrTimer,
       "oaDevLosGrConnectionId": oaDevLosGrConnectionId,
       "oaDevLosGrHoldOffTimer": oaDevLosGrHoldOffTimer,
       "oaDevLosGrPollDelayTimer": oaDevLosGrPollDelayTimer,
       "oaDevLosGrToBackupTrapTimer": oaDevLosGrToBackupTrapTimer,
       "oaDevLosGrToPrimaryTrapTimer": oaDevLosGrToPrimaryTrapTimer,
       "oaDevLosGrAgTable": oaDevLosGrAgTable,
       "oaDevLosGrAgEntry": oaDevLosGrAgEntry,
       "oaDevLosGrAgDomainId": oaDevLosGrAgDomainId,
       "oaDevLosGrAgAssociationId": oaDevLosGrAgAssociationId,
       "oaDevLosGrAgRemoteMep": oaDevLosGrAgRemoteMep,
       "oaDevLosGrAgRMepStatus": oaDevLosGrAgRMepStatus,
       "oaDevLosGrAgAdminStatus": oaDevLosGrAgAdminStatus,
       "oaDevLosGrAgVid": oaDevLosGrAgVid,
       "oaDevLosGrMmuTable": oaDevLosGrMmuTable,
       "oaDevLosGrMmuEntry": oaDevLosGrMmuEntry,
       "oaDevLosGrMmuEnabled": oaDevLosGrMmuEnabled,
       "oaDevLosConformance": oaDevLosConformance,
       "oaDevLosMIBCompliances": oaDevLosMIBCompliances,
       "oaDevLosMIBCompliance": oaDevLosMIBCompliance,
       "oaDevLosMIBGroups": oaDevLosMIBGroups,
       "oaDevLosMandatoryGroup": oaDevLosMandatoryGroup,
       "oaPortLosTrapParamsGroup": oaPortLosTrapParamsGroup,
       "oaPortLosGroup": oaPortLosGroup,
       "oaDevLosNotificationsGroup": oaDevLosNotificationsGroup}
)
