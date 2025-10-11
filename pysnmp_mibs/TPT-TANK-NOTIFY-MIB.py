# SNMP MIB module (TPT-TANK-NOTIFY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/trendmicro/TPT-TANK-NOTIFY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:06:12 2025
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

(tptMiscNotifyDeviceID,) = mibBuilder.importSymbols(
    "TPT-MISC-NOTIFY-MIB",
    "tptMiscNotifyDeviceID")

(tpt_tpa_eventsV2,
 tpt_tpa_objs,
 tpt_tpa_unkparams) = mibBuilder.importSymbols(
    "TPT-TPAMIBS-MIB",
    "tpt-tpa-eventsV2",
    "tpt-tpa-objs",
    "tpt-tpa-unkparams")


# MODULE-IDENTITY

tpt_tank_notify = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 11)
)
if mibBuilder.loadTexts:
    tpt_tank_notify.setRevisions(
        ("2016-05-25 18:54",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ExternalVIStatus(TextualConvention, Integer32):
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



class WebFilterStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("uninitialized", 1),
          ("success", 2),
          ("timeout", 3),
          ("failure", 4))
    )



# MIB Managed Objects in the order of their OIDs

_TptTankNotifyExternalVIStatus_Type = ExternalVIStatus
_TptTankNotifyExternalVIStatus_Object = MibScalar
tptTankNotifyExternalVIStatus = _TptTankNotifyExternalVIStatus_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 151),
    _TptTankNotifyExternalVIStatus_Type()
)
tptTankNotifyExternalVIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptTankNotifyExternalVIStatus.setStatus("current")
_TptTankNotifyWebFilterStatus_Type = WebFilterStatus
_TptTankNotifyWebFilterStatus_Object = MibScalar
tptTankNotifyWebFilterStatus = _TptTankNotifyWebFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 152),
    _TptTankNotifyWebFilterStatus_Type()
)
tptTankNotifyWebFilterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tptTankNotifyWebFilterStatus.setStatus("current")

# Managed Objects groups


# Notification objects

tptTankNotifyExternalVI = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 22)
)
tptTankNotifyExternalVI.setObjects(
      *(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"),
        ("TPT-TANK-NOTIFY-MIB", "tptTankNotifyExternalVIStatus"))
)
if mibBuilder.loadTexts:
    tptTankNotifyExternalVI.setStatus(
        "current"
    )

tptTankNotifyWebFilter = NotificationType(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 23)
)
tptTankNotifyWebFilter.setObjects(
      *(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"),
        ("TPT-TANK-NOTIFY-MIB", "tptTankNotifyWebFilterStatus"))
)
if mibBuilder.loadTexts:
    tptTankNotifyWebFilter.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-TANK-NOTIFY-MIB",
    **{"ExternalVIStatus": ExternalVIStatus,
       "WebFilterStatus": WebFilterStatus,
       "tpt-tank-notify": tpt_tank_notify,
       "tptTankNotifyExternalVI": tptTankNotifyExternalVI,
       "tptTankNotifyWebFilter": tptTankNotifyWebFilter,
       "tptTankNotifyExternalVIStatus": tptTankNotifyExternalVIStatus,
       "tptTankNotifyWebFilterStatus": tptTankNotifyWebFilterStatus}
)
