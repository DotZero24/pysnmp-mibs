_E='tpPortMirrorSession'
_D='TPLINK-PORTMIRROR-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkPortMirrorMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,11))
if mibBuilder.loadTexts:tplinkPortMirrorMIB.setRevisions(('2012-12-14 00:00',))
_TplinkPortMirrorMIBObjects_ObjectIdentity=ObjectIdentity
tplinkPortMirrorMIBObjects=_TplinkPortMirrorMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,11,1))
_TpPortMirrorTable_Object=MibTable
tpPortMirrorTable=_TpPortMirrorTable_Object((1,3,6,1,4,1,11863,6,11,1,1))
if mibBuilder.loadTexts:tpPortMirrorTable.setStatus(_A)
_TpPortMirrorEntry_Object=MibTableRow
tpPortMirrorEntry=_TpPortMirrorEntry_Object((1,3,6,1,4,1,11863,6,11,1,1,1))
tpPortMirrorEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:tpPortMirrorEntry.setStatus(_A)
_TpPortMirrorSession_Type=Integer32
_TpPortMirrorSession_Object=MibTableColumn
tpPortMirrorSession=_TpPortMirrorSession_Object((1,3,6,1,4,1,11863,6,11,1,1,1,1),_TpPortMirrorSession_Type())
tpPortMirrorSession.setMaxAccess('read-only')
if mibBuilder.loadTexts:tpPortMirrorSession.setStatus(_A)
_TpPortMirrorDestination_Type=OctetString
_TpPortMirrorDestination_Object=MibTableColumn
tpPortMirrorDestination=_TpPortMirrorDestination_Object((1,3,6,1,4,1,11863,6,11,1,1,1,2),_TpPortMirrorDestination_Type())
tpPortMirrorDestination.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPortMirrorDestination.setStatus(_A)
_TpPortMirrorIngressSource_Type=OctetString
_TpPortMirrorIngressSource_Object=MibTableColumn
tpPortMirrorIngressSource=_TpPortMirrorIngressSource_Object((1,3,6,1,4,1,11863,6,11,1,1,1,3),_TpPortMirrorIngressSource_Type())
tpPortMirrorIngressSource.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPortMirrorIngressSource.setStatus(_A)
_TpPortMirrorEgressSource_Type=OctetString
_TpPortMirrorEgressSource_Object=MibTableColumn
tpPortMirrorEgressSource=_TpPortMirrorEgressSource_Object((1,3,6,1,4,1,11863,6,11,1,1,1,4),_TpPortMirrorEgressSource_Type())
tpPortMirrorEgressSource.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPortMirrorEgressSource.setStatus(_A)
_TpPortMirrorBothSource_Type=OctetString
_TpPortMirrorBothSource_Object=MibTableColumn
tpPortMirrorBothSource=_TpPortMirrorBothSource_Object((1,3,6,1,4,1,11863,6,11,1,1,1,5),_TpPortMirrorBothSource_Type())
tpPortMirrorBothSource.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPortMirrorBothSource.setStatus(_A)
class _TpPortMirrorSessionState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('negative',1),('active',2),('clear',3)))
_TpPortMirrorSessionState_Type.__name__=_C
_TpPortMirrorSessionState_Object=MibTableColumn
tpPortMirrorSessionState=_TpPortMirrorSessionState_Object((1,3,6,1,4,1,11863,6,11,1,1,1,6),_TpPortMirrorSessionState_Type())
tpPortMirrorSessionState.setMaxAccess(_B)
if mibBuilder.loadTexts:tpPortMirrorSessionState.setStatus(_A)
_TplinkPortMirrorMIBNotifications_ObjectIdentity=ObjectIdentity
tplinkPortMirrorMIBNotifications=_TplinkPortMirrorMIBNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,11,2))
mibBuilder.exportSymbols(_D,**{'tplinkPortMirrorMIB':tplinkPortMirrorMIB,'tplinkPortMirrorMIBObjects':tplinkPortMirrorMIBObjects,'tpPortMirrorTable':tpPortMirrorTable,'tpPortMirrorEntry':tpPortMirrorEntry,_E:tpPortMirrorSession,'tpPortMirrorDestination':tpPortMirrorDestination,'tpPortMirrorIngressSource':tpPortMirrorIngressSource,'tpPortMirrorEgressSource':tpPortMirrorEgressSource,'tpPortMirrorBothSource':tpPortMirrorBothSource,'tpPortMirrorSessionState':tpPortMirrorSessionState,'tplinkPortMirrorMIBNotifications':tplinkPortMirrorMIBNotifications})