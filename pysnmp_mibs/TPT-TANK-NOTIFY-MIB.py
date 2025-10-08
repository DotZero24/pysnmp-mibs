#
# PySNMP MIB module TPT-TANK-NOTIFY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/rob/Code/pysnmp-mibs/mibs/trendmicro/TPT-TANK-NOTIFY-MIB
# Produced by pysmi-1.1.12 at Wed Oct  8 09:58:30 2025
# On host macmini.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, Bits, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Counter32, ModuleIdentity, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "Bits", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Counter32", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tptMiscNotifyDeviceID, = mibBuilder.importSymbols("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID")
tpt_tpa_objs, tpt_tpa_unkparams, tpt_tpa_eventsV2 = mibBuilder.importSymbols("TPT-TPAMIBS-MIB", "tpt-tpa-objs", "tpt-tpa-unkparams", "tpt-tpa-eventsV2")
tpt_tank_notify = ModuleIdentity((1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 11)).setLabel("tpt-tank-notify")
tpt_tank_notify.setRevisions(('2016-05-25 18:54',))
if mibBuilder.loadTexts: tpt_tank_notify.setLastUpdated('201605251854Z')
if mibBuilder.loadTexts: tpt_tank_notify.setOrganization('Trend Micro, Inc.')
class ExternalVIStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class WebFilterStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("uninitialized", 1), ("success", 2), ("timeout", 3), ("failure", 4))

tptTankNotifyExternalVIStatus = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 151), ExternalVIStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptTankNotifyExternalVIStatus.setStatus('current')
tptTankNotifyWebFilterStatus = MibScalar((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 1, 152), WebFilterStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tptTankNotifyWebFilterStatus.setStatus('current')
tptTankNotifyExternalVI = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 22)).setObjects(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"), ("TPT-TANK-NOTIFY-MIB", "tptTankNotifyExternalVIStatus"))
if mibBuilder.loadTexts: tptTankNotifyExternalVI.setStatus('current')
tptTankNotifyWebFilter = NotificationType((1, 3, 6, 1, 4, 1, 10734, 3, 3, 3, 0, 23)).setObjects(("TPT-MISC-NOTIFY-MIB", "tptMiscNotifyDeviceID"), ("TPT-TANK-NOTIFY-MIB", "tptTankNotifyWebFilterStatus"))
if mibBuilder.loadTexts: tptTankNotifyWebFilter.setStatus('current')
mibBuilder.exportSymbols("TPT-TANK-NOTIFY-MIB", tpt_tank_notify=tpt_tank_notify, WebFilterStatus=WebFilterStatus, PYSNMP_MODULE_ID=tpt_tank_notify, ExternalVIStatus=ExternalVIStatus, tptTankNotifyExternalVI=tptTankNotifyExternalVI, tptTankNotifyWebFilterStatus=tptTankNotifyWebFilterStatus, tptTankNotifyWebFilter=tptTankNotifyWebFilter, tptTankNotifyExternalVIStatus=tptTankNotifyExternalVIStatus)
