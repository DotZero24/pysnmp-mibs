# SNMP MIB module (OA-PORT-LIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OA-PORT-LIN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:32 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

nbPortLinkReflection = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11)
)
if mibBuilder.loadTexts:
    nbPortLinkReflection.setRevisions(
        ("2011-03-16 00:00",
         "2010-11-02 00:00",
         "2007-12-11 00:00",
         "2007-08-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbPortParams_ObjectIdentity = ObjectIdentity
nbPortParams = _NbPortParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10)
)
_OaPortLinNotifications_ObjectIdentity = ObjectIdentity
oaPortLinNotifications = _OaPortLinNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 0)
)
_OaPortLinGen_ObjectIdentity = ObjectIdentity
oaPortLinGen = _OaPortLinGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 1)
)


class _OaPortLinGenSupport_Type(Integer32):
    """Custom type oaPortLinGenSupport based on Integer32"""
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


_OaPortLinGenSupport_Type.__name__ = "Integer32"
_OaPortLinGenSupport_Object = MibScalar
oaPortLinGenSupport = _OaPortLinGenSupport_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 1, 1),
    _OaPortLinGenSupport_Type()
)
oaPortLinGenSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaPortLinGenSupport.setStatus("current")


class _OaPortLinAgSupport_Type(Integer32):
    """Custom type oaPortLinAgSupport based on Integer32"""
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


_OaPortLinAgSupport_Type.__name__ = "Integer32"
_OaPortLinAgSupport_Object = MibScalar
oaPortLinAgSupport = _OaPortLinAgSupport_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 1, 2),
    _OaPortLinAgSupport_Type()
)
oaPortLinAgSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaPortLinAgSupport.setStatus("current")


class _OaPortLinLastError_Type(DisplayString):
    """Custom type oaPortLinLastError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 160),
    )


_OaPortLinLastError_Type.__name__ = "DisplayString"
_OaPortLinLastError_Object = MibScalar
oaPortLinLastError = _OaPortLinLastError_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 1, 3),
    _OaPortLinLastError_Type()
)
oaPortLinLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaPortLinLastError.setStatus("current")
_OaPortLinGrp_ObjectIdentity = ObjectIdentity
oaPortLinGrp = _OaPortLinGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 2)
)
_OaPortLinTable_Object = MibTable
oaPortLinTable = _OaPortLinTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 2, 1)
)
if mibBuilder.loadTexts:
    oaPortLinTable.setStatus("current")
_OaPortLinEntry_Object = MibTableRow
oaPortLinEntry = _OaPortLinEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 2, 1, 1)
)
oaPortLinEntry.setIndexNames(
    (0, "OA-PORT-LIN-MIB", "oaPortLinId"),
)
if mibBuilder.loadTexts:
    oaPortLinEntry.setStatus("current")


class _OaPortLinId_Type(Integer32):
    """Custom type oaPortLinId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OaPortLinId_Type.__name__ = "Integer32"
_OaPortLinId_Object = MibTableColumn
oaPortLinId = _OaPortLinId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 2, 1, 1, 1),
    _OaPortLinId_Type()
)
oaPortLinId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaPortLinId.setStatus("current")


class _OaPortLinOperStatus_Type(Integer32):
    """Custom type oaPortLinOperStatus based on Integer32"""
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
          ("master", 2),
          ("slave", 3))
    )


_OaPortLinOperStatus_Type.__name__ = "Integer32"
_OaPortLinOperStatus_Object = MibTableColumn
oaPortLinOperStatus = _OaPortLinOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 2, 1, 1, 2),
    _OaPortLinOperStatus_Type()
)
oaPortLinOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaPortLinOperStatus.setStatus("current")


class _OaPortLinAdminStatus_Type(Integer32):
    """Custom type oaPortLinAdminStatus based on Integer32"""
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


_OaPortLinAdminStatus_Type.__name__ = "Integer32"
_OaPortLinAdminStatus_Object = MibTableColumn
oaPortLinAdminStatus = _OaPortLinAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 2, 1, 1, 3),
    _OaPortLinAdminStatus_Type()
)
oaPortLinAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaPortLinAdminStatus.setStatus("current")


class _OaPortLinSlavePorts_Type(OctetString):
    """Custom type oaPortLinSlavePorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OaPortLinSlavePorts_Type.__name__ = "OctetString"
_OaPortLinSlavePorts_Object = MibTableColumn
oaPortLinSlavePorts = _OaPortLinSlavePorts_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 2, 1, 1, 4),
    _OaPortLinSlavePorts_Type()
)
oaPortLinSlavePorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaPortLinSlavePorts.setStatus("current")


class _OaPortLinSymmetricStatus_Type(Integer32):
    """Custom type oaPortLinSymmetricStatus based on Integer32"""
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
          ("symmetric", 2),
          ("nonSymmetric", 3))
    )


_OaPortLinSymmetricStatus_Type.__name__ = "Integer32"
_OaPortLinSymmetricStatus_Object = MibTableColumn
oaPortLinSymmetricStatus = _OaPortLinSymmetricStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 2, 1, 1, 5),
    _OaPortLinSymmetricStatus_Type()
)
oaPortLinSymmetricStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaPortLinSymmetricStatus.setStatus("current")


class _OaPortLinActionCause_Type(Integer32):
    """Custom type oaPortLinActionCause based on Integer32"""
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
        *(("noAction", 1),
          ("portLinkUp", 2),
          ("portLinkDown", 3),
          ("agRMepDiscardEvent", 4),
          ("agRMepNoConnEvent", 5),
          ("agRMepAliveEvent", 6))
    )


_OaPortLinActionCause_Type.__name__ = "Integer32"
_OaPortLinActionCause_Object = MibTableColumn
oaPortLinActionCause = _OaPortLinActionCause_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 2, 1, 1, 6),
    _OaPortLinActionCause_Type()
)
oaPortLinActionCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaPortLinActionCause.setStatus("current")
_OaPortLinAgTable_Object = MibTable
oaPortLinAgTable = _OaPortLinAgTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 2, 5)
)
if mibBuilder.loadTexts:
    oaPortLinAgTable.setStatus("current")
_OaPortLinAgEntry_Object = MibTableRow
oaPortLinAgEntry = _OaPortLinAgEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 2, 5, 1)
)
oaPortLinAgEntry.setIndexNames(
    (0, "OA-PORT-LIN-MIB", "oaPortLinId"),
    (0, "OA-PORT-LIN-MIB", "oaPortLinAgDomainId"),
    (0, "OA-PORT-LIN-MIB", "oaPortLinAgAssociationId"),
    (0, "OA-PORT-LIN-MIB", "oaPortLinAgRemoteMep"),
)
if mibBuilder.loadTexts:
    oaPortLinAgEntry.setStatus("current")


class _OaPortLinAgDomainId_Type(Unsigned32):
    """Custom type oaPortLinAgDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_OaPortLinAgDomainId_Type.__name__ = "Unsigned32"
_OaPortLinAgDomainId_Object = MibTableColumn
oaPortLinAgDomainId = _OaPortLinAgDomainId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 2, 5, 1, 2),
    _OaPortLinAgDomainId_Type()
)
oaPortLinAgDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaPortLinAgDomainId.setStatus("current")


class _OaPortLinAgAssociationId_Type(Unsigned32):
    """Custom type oaPortLinAgAssociationId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OaPortLinAgAssociationId_Type.__name__ = "Unsigned32"
_OaPortLinAgAssociationId_Object = MibTableColumn
oaPortLinAgAssociationId = _OaPortLinAgAssociationId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 2, 5, 1, 3),
    _OaPortLinAgAssociationId_Type()
)
oaPortLinAgAssociationId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaPortLinAgAssociationId.setStatus("current")


class _OaPortLinAgRemoteMep_Type(Unsigned32):
    """Custom type oaPortLinAgRemoteMep based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_OaPortLinAgRemoteMep_Type.__name__ = "Unsigned32"
_OaPortLinAgRemoteMep_Object = MibTableColumn
oaPortLinAgRemoteMep = _OaPortLinAgRemoteMep_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 2, 5, 1, 4),
    _OaPortLinAgRemoteMep_Type()
)
oaPortLinAgRemoteMep.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaPortLinAgRemoteMep.setStatus("current")


class _OaPortLinAgRMepStatus_Type(Integer32):
    """Custom type oaPortLinAgRMepStatus based on Integer32"""
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


_OaPortLinAgRMepStatus_Type.__name__ = "Integer32"
_OaPortLinAgRMepStatus_Object = MibTableColumn
oaPortLinAgRMepStatus = _OaPortLinAgRMepStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 2, 5, 1, 8),
    _OaPortLinAgRMepStatus_Type()
)
oaPortLinAgRMepStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaPortLinAgRMepStatus.setStatus("current")


class _OaPortLinAgAdminStatus_Type(Integer32):
    """Custom type oaPortLinAgAdminStatus based on Integer32"""
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


_OaPortLinAgAdminStatus_Type.__name__ = "Integer32"
_OaPortLinAgAdminStatus_Object = MibTableColumn
oaPortLinAgAdminStatus = _OaPortLinAgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 2, 5, 1, 10),
    _OaPortLinAgAdminStatus_Type()
)
oaPortLinAgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaPortLinAgAdminStatus.setStatus("current")
_OaPortLinConformance_ObjectIdentity = ObjectIdentity
oaPortLinConformance = _OaPortLinConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 101)
)
_OaPortLinCompliances_ObjectIdentity = ObjectIdentity
oaPortLinCompliances = _OaPortLinCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 101, 1)
)
_OaPortLinGroups_ObjectIdentity = ObjectIdentity
oaPortLinGroups = _OaPortLinGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 101, 2)
)

# Managed Objects groups

oaPortLinMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 101, 2, 1)
)
oaPortLinMandatoryGroup.setObjects(
      *(("OA-PORT-LIN-MIB", "oaPortLinGenSupport"),
        ("OA-PORT-LIN-MIB", "oaPortLinAgSupport"),
        ("OA-PORT-LIN-MIB", "oaPortLinOperStatus"),
        ("OA-PORT-LIN-MIB", "oaPortLinAdminStatus"),
        ("OA-PORT-LIN-MIB", "oaPortLinSlavePorts"),
        ("OA-PORT-LIN-MIB", "oaPortLinSymmetricStatus"),
        ("OA-PORT-LIN-MIB", "oaPortLinLastError"))
)
if mibBuilder.loadTexts:
    oaPortLinMandatoryGroup.setStatus("current")

oaPortLinTrapParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 101, 2, 2)
)
oaPortLinTrapParamsGroup.setObjects(
    ("OA-PORT-LIN-MIB", "oaPortLinActionCause")
)
if mibBuilder.loadTexts:
    oaPortLinTrapParamsGroup.setStatus("current")

oaPortLinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 101, 2, 3)
)
oaPortLinGroup.setObjects(
      *(("OA-PORT-LIN-MIB", "oaPortLinAgRMepStatus"),
        ("OA-PORT-LIN-MIB", "oaPortLinAgAdminStatus"))
)
if mibBuilder.loadTexts:
    oaPortLinGroup.setStatus("current")


# Notification objects

oaPortLinStateUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 0, 33)
)
oaPortLinStateUp.setObjects(
      *(("OA-PORT-LIN-MIB", "oaPortLinSlavePorts"),
        ("OA-PORT-LIN-MIB", "oaPortLinActionCause"))
)
if mibBuilder.loadTexts:
    oaPortLinStateUp.setStatus(
        "current"
    )

oaPortLinStateDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 0, 35)
)
oaPortLinStateDown.setObjects(
      *(("OA-PORT-LIN-MIB", "oaPortLinSlavePorts"),
        ("OA-PORT-LIN-MIB", "oaPortLinActionCause"))
)
if mibBuilder.loadTexts:
    oaPortLinStateDown.setStatus(
        "current"
    )


# Notifications groups

oaPortLinNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 101, 2, 4)
)
oaPortLinNotificationsGroup.setObjects(
      *(("OA-PORT-LIN-MIB", "oaPortLinStateUp"),
        ("OA-PORT-LIN-MIB", "oaPortLinStateDown"))
)
if mibBuilder.loadTexts:
    oaPortLinNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

oaPortLinCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 10, 11, 101, 1, 1)
)
oaPortLinCompliance.setObjects(
      *(("OA-PORT-LIN-MIB", "oaPortLinMandatoryGroup"),
        ("OA-PORT-LIN-MIB", "oaPortLinNotificationsGroup"),
        ("OA-PORT-LIN-MIB", "oaPortLinTrapParamsGroup"),
        ("OA-PORT-LIN-MIB", "oaPortLinGroup"))
)
if mibBuilder.loadTexts:
    oaPortLinCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OA-PORT-LIN-MIB",
    **{"nbPortParams": nbPortParams,
       "nbPortLinkReflection": nbPortLinkReflection,
       "oaPortLinNotifications": oaPortLinNotifications,
       "oaPortLinStateUp": oaPortLinStateUp,
       "oaPortLinStateDown": oaPortLinStateDown,
       "oaPortLinGen": oaPortLinGen,
       "oaPortLinGenSupport": oaPortLinGenSupport,
       "oaPortLinAgSupport": oaPortLinAgSupport,
       "oaPortLinLastError": oaPortLinLastError,
       "oaPortLinGrp": oaPortLinGrp,
       "oaPortLinTable": oaPortLinTable,
       "oaPortLinEntry": oaPortLinEntry,
       "oaPortLinId": oaPortLinId,
       "oaPortLinOperStatus": oaPortLinOperStatus,
       "oaPortLinAdminStatus": oaPortLinAdminStatus,
       "oaPortLinSlavePorts": oaPortLinSlavePorts,
       "oaPortLinSymmetricStatus": oaPortLinSymmetricStatus,
       "oaPortLinActionCause": oaPortLinActionCause,
       "oaPortLinAgTable": oaPortLinAgTable,
       "oaPortLinAgEntry": oaPortLinAgEntry,
       "oaPortLinAgDomainId": oaPortLinAgDomainId,
       "oaPortLinAgAssociationId": oaPortLinAgAssociationId,
       "oaPortLinAgRemoteMep": oaPortLinAgRemoteMep,
       "oaPortLinAgRMepStatus": oaPortLinAgRMepStatus,
       "oaPortLinAgAdminStatus": oaPortLinAgAdminStatus,
       "oaPortLinConformance": oaPortLinConformance,
       "oaPortLinCompliances": oaPortLinCompliances,
       "oaPortLinCompliance": oaPortLinCompliance,
       "oaPortLinGroups": oaPortLinGroups,
       "oaPortLinMandatoryGroup": oaPortLinMandatoryGroup,
       "oaPortLinTrapParamsGroup": oaPortLinTrapParamsGroup,
       "oaPortLinGroup": oaPortLinGroup,
       "oaPortLinNotificationsGroup": oaPortLinNotificationsGroup}
)
