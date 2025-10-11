# SNMP MIB module (ADTRAN-IEEE8021X-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-IEEE8021X-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:32 2025
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

(adGen802dot1x,
 adGen802dot1xID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGen802dot1x",
    "adGen802dot1xID")

(dot1xPaePortNumber,) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "dot1xPaePortNumber")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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

adGen802dot1xMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 17, 1)
)
if mibBuilder.loadTexts:
    adGen802dot1xMIB.setRevisions(
        ("2013-06-27 00:00",
         "2013-06-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGen802dot1xEapolConfigTable_Object = MibTable
adGen802dot1xEapolConfigTable = _AdGen802dot1xEapolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 17, 1)
)
if mibBuilder.loadTexts:
    adGen802dot1xEapolConfigTable.setStatus("current")
_AdGen802dot1xEapolConfigEntry_Object = MibTableRow
adGen802dot1xEapolConfigEntry = _AdGen802dot1xEapolConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 17, 1, 1)
)
adGen802dot1xEapolConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGen802dot1xEapolConfigEntry.setStatus("current")


class _AdGen802dot1xEapRespTimeout_Type(Unsigned32):
    """Custom type adGen802dot1xEapRespTimeout based on Unsigned32"""
    defaultValue = 30


_AdGen802dot1xEapRespTimeout_Type.__name__ = "Unsigned32"
_AdGen802dot1xEapRespTimeout_Object = MibTableColumn
adGen802dot1xEapRespTimeout = _AdGen802dot1xEapRespTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 17, 1, 1, 1),
    _AdGen802dot1xEapRespTimeout_Type()
)
adGen802dot1xEapRespTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGen802dot1xEapRespTimeout.setStatus("current")


class _AdGen802dot1xMaxEapReq_Type(Unsigned32):
    """Custom type adGen802dot1xMaxEapReq based on Unsigned32"""
    defaultValue = 2


_AdGen802dot1xMaxEapReq_Type.__name__ = "Unsigned32"
_AdGen802dot1xMaxEapReq_Object = MibTableColumn
adGen802dot1xMaxEapReq = _AdGen802dot1xMaxEapReq_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 17, 1, 1, 2),
    _AdGen802dot1xMaxEapReq_Type()
)
adGen802dot1xMaxEapReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGen802dot1xMaxEapReq.setStatus("current")
_AdGen802dot1xPortConfigTable_Object = MibTable
adGen802dot1xPortConfigTable = _AdGen802dot1xPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 17, 2)
)
if mibBuilder.loadTexts:
    adGen802dot1xPortConfigTable.setStatus("current")
_AdGen802dot1xPortConfigEntry_Object = MibTableRow
adGen802dot1xPortConfigEntry = _AdGen802dot1xPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 17, 2, 1)
)
adGen802dot1xPortConfigEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    adGen802dot1xPortConfigEntry.setStatus("current")


class _AdGen802dot1xPortIPEntity_Type(Integer32):
    """Custom type adGen802dot1xPortIPEntity based on Integer32"""
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
          ("ipHost", 2),
          ("subtendedHost", 3))
    )


_AdGen802dot1xPortIPEntity_Type.__name__ = "Integer32"
_AdGen802dot1xPortIPEntity_Object = MibTableColumn
adGen802dot1xPortIPEntity = _AdGen802dot1xPortIPEntity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 17, 2, 1, 1),
    _AdGen802dot1xPortIPEntity_Type()
)
adGen802dot1xPortIPEntity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGen802dot1xPortIPEntity.setStatus("current")
_AdGen802dot1xPortIPHostName_Type = DisplayString
_AdGen802dot1xPortIPHostName_Object = MibTableColumn
adGen802dot1xPortIPHostName = _AdGen802dot1xPortIPHostName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 17, 2, 1, 2),
    _AdGen802dot1xPortIPHostName_Type()
)
adGen802dot1xPortIPHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGen802dot1xPortIPHostName.setStatus("current")


class _AdGen802dot1xPortAuthServerType_Type(Integer32):
    """Custom type adGen802dot1xPortAuthServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("radius", 1)
    )


_AdGen802dot1xPortAuthServerType_Type.__name__ = "Integer32"
_AdGen802dot1xPortAuthServerType_Object = MibTableColumn
adGen802dot1xPortAuthServerType = _AdGen802dot1xPortAuthServerType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 17, 2, 1, 3),
    _AdGen802dot1xPortAuthServerType_Type()
)
adGen802dot1xPortAuthServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGen802dot1xPortAuthServerType.setStatus("current")
_AdGen802dot1xPortRadiusServerGroupName_Type = DisplayString
_AdGen802dot1xPortRadiusServerGroupName_Object = MibTableColumn
adGen802dot1xPortRadiusServerGroupName = _AdGen802dot1xPortRadiusServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 17, 2, 1, 4),
    _AdGen802dot1xPortRadiusServerGroupName_Type()
)
adGen802dot1xPortRadiusServerGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGen802dot1xPortRadiusServerGroupName.setStatus("current")
_AdGen802dot1xPortStatusTable_Object = MibTable
adGen802dot1xPortStatusTable = _AdGen802dot1xPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 17, 3)
)
if mibBuilder.loadTexts:
    adGen802dot1xPortStatusTable.setStatus("current")
_AdGen802dot1xPortStatusEntry_Object = MibTableRow
adGen802dot1xPortStatusEntry = _AdGen802dot1xPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 17, 3, 1)
)
adGen802dot1xPortStatusEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    adGen802dot1xPortStatusEntry.setStatus("current")
_AdGen802dot1xPortStatusLastError_Type = DisplayString
_AdGen802dot1xPortStatusLastError_Object = MibTableColumn
adGen802dot1xPortStatusLastError = _AdGen802dot1xPortStatusLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 17, 3, 1, 1),
    _AdGen802dot1xPortStatusLastError_Type()
)
adGen802dot1xPortStatusLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGen802dot1xPortStatusLastError.setStatus("current")


class _AdGen802dot1xPortStatusClearCounters_Type(Integer32):
    """Custom type adGen802dot1xPortStatusClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AdGen802dot1xPortStatusClearCounters_Type.__name__ = "Integer32"
_AdGen802dot1xPortStatusClearCounters_Object = MibTableColumn
adGen802dot1xPortStatusClearCounters = _AdGen802dot1xPortStatusClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 17, 3, 1, 2),
    _AdGen802dot1xPortStatusClearCounters_Type()
)
adGen802dot1xPortStatusClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGen802dot1xPortStatusClearCounters.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-IEEE8021X-MIB",
    **{"adGen802dot1xEapolConfigTable": adGen802dot1xEapolConfigTable,
       "adGen802dot1xEapolConfigEntry": adGen802dot1xEapolConfigEntry,
       "adGen802dot1xEapRespTimeout": adGen802dot1xEapRespTimeout,
       "adGen802dot1xMaxEapReq": adGen802dot1xMaxEapReq,
       "adGen802dot1xPortConfigTable": adGen802dot1xPortConfigTable,
       "adGen802dot1xPortConfigEntry": adGen802dot1xPortConfigEntry,
       "adGen802dot1xPortIPEntity": adGen802dot1xPortIPEntity,
       "adGen802dot1xPortIPHostName": adGen802dot1xPortIPHostName,
       "adGen802dot1xPortAuthServerType": adGen802dot1xPortAuthServerType,
       "adGen802dot1xPortRadiusServerGroupName": adGen802dot1xPortRadiusServerGroupName,
       "adGen802dot1xPortStatusTable": adGen802dot1xPortStatusTable,
       "adGen802dot1xPortStatusEntry": adGen802dot1xPortStatusEntry,
       "adGen802dot1xPortStatusLastError": adGen802dot1xPortStatusLastError,
       "adGen802dot1xPortStatusClearCounters": adGen802dot1xPortStatusClearCounters,
       "adGen802dot1xMIB": adGen802dot1xMIB}
)
