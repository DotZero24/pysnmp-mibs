_G='tptTankNotifyWebFilterStatus'
_F='tptTankNotifyExternalVIStatus'
_E='read-only'
_D='TPT-TANK-NOTIFY-MIB'
_C='tptMiscNotifyDeviceID'
_B='TPT-MISC-NOTIFY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tptMiscNotifyDeviceID,=mibBuilder.importSymbols(_B,_C)
tpt_tpa_eventsV2,tpt_tpa_objs,tpt_tpa_unkparams=mibBuilder.importSymbols('TPT-TPAMIBS-MIB','tpt-tpa-eventsV2','tpt-tpa-objs','tpt-tpa-unkparams')
tpt_tank_notify=ModuleIdentity((1,3,6,1,4,1,10734,3,3,2,11))
if mibBuilder.loadTexts:tpt_tank_notify.setRevisions(('2016-05-25 18:54',))
class ExternalVIStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
class WebFilterStatus(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('uninitialized',1),('success',2),('timeout',3),('failure',4)))
_TptTankNotifyExternalVIStatus_Type=ExternalVIStatus
_TptTankNotifyExternalVIStatus_Object=MibScalar
tptTankNotifyExternalVIStatus=_TptTankNotifyExternalVIStatus_Object((1,3,6,1,4,1,10734,3,3,3,1,151),_TptTankNotifyExternalVIStatus_Type())
tptTankNotifyExternalVIStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tptTankNotifyExternalVIStatus.setStatus(_A)
_TptTankNotifyWebFilterStatus_Type=WebFilterStatus
_TptTankNotifyWebFilterStatus_Object=MibScalar
tptTankNotifyWebFilterStatus=_TptTankNotifyWebFilterStatus_Object((1,3,6,1,4,1,10734,3,3,3,1,152),_TptTankNotifyWebFilterStatus_Type())
tptTankNotifyWebFilterStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:tptTankNotifyWebFilterStatus.setStatus(_A)
tptTankNotifyExternalVI=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,22))
tptTankNotifyExternalVI.setObjects(*((_B,_C),(_D,_F)))
if mibBuilder.loadTexts:tptTankNotifyExternalVI.setStatus(_A)
tptTankNotifyWebFilter=NotificationType((1,3,6,1,4,1,10734,3,3,3,0,23))
tptTankNotifyWebFilter.setObjects(*((_B,_C),(_D,_G)))
if mibBuilder.loadTexts:tptTankNotifyWebFilter.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ExternalVIStatus':ExternalVIStatus,'WebFilterStatus':WebFilterStatus,'tpt-tank-notify':tpt_tank_notify,'tptTankNotifyExternalVI':tptTankNotifyExternalVI,'tptTankNotifyWebFilter':tptTankNotifyWebFilter,_F:tptTankNotifyExternalVIStatus,_G:tptTankNotifyWebFilterStatus})