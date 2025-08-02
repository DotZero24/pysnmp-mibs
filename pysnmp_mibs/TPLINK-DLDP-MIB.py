_H='tpDldpPortId'
_G='TPLINK-DLDP-MIB'
_F='enable'
_E='disable'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkDldpMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,58))
if mibBuilder.loadTexts:tplinkDldpMIB.setRevisions(('2013-07-03 00:00',))
_TplinkDldpMIBObjects_ObjectIdentity=ObjectIdentity
tplinkDldpMIBObjects=_TplinkDldpMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,58,1))
class _TpDldpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TpDldpEnable_Type.__name__=_B
_TpDldpEnable_Object=MibScalar
tpDldpEnable=_TpDldpEnable_Object((1,3,6,1,4,1,11863,6,58,1,1),_TpDldpEnable_Type())
tpDldpEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:tpDldpEnable.setStatus(_A)
class _TpDldpInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_TpDldpInterval_Type.__name__=_B
_TpDldpInterval_Object=MibScalar
tpDldpInterval=_TpDldpInterval_Object((1,3,6,1,4,1,11863,6,58,1,2),_TpDldpInterval_Type())
tpDldpInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:tpDldpInterval.setStatus(_A)
class _TpDldpShutmode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('auto',0),('manual',1)))
_TpDldpShutmode_Type.__name__=_B
_TpDldpShutmode_Object=MibScalar
tpDldpShutmode=_TpDldpShutmode_Object((1,3,6,1,4,1,11863,6,58,1,3),_TpDldpShutmode_Type())
tpDldpShutmode.setMaxAccess(_C)
if mibBuilder.loadTexts:tpDldpShutmode.setStatus(_A)
_TpDldpCtrlTable_Object=MibTable
tpDldpCtrlTable=_TpDldpCtrlTable_Object((1,3,6,1,4,1,11863,6,58,1,4))
if mibBuilder.loadTexts:tpDldpCtrlTable.setStatus(_A)
_TpDldpCtrlEntry_Object=MibTableRow
tpDldpCtrlEntry=_TpDldpCtrlEntry_Object((1,3,6,1,4,1,11863,6,58,1,4,1))
tpDldpCtrlEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:tpDldpCtrlEntry.setStatus(_A)
_TpDldpPortId_Type=Integer32
_TpDldpPortId_Object=MibTableColumn
tpDldpPortId=_TpDldpPortId_Object((1,3,6,1,4,1,11863,6,58,1,4,1,1),_TpDldpPortId_Type())
tpDldpPortId.setMaxAccess(_D)
if mibBuilder.loadTexts:tpDldpPortId.setStatus(_A)
class _TpDldpState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_E,0),(_F,1)))
_TpDldpState_Type.__name__=_B
_TpDldpState_Object=MibTableColumn
tpDldpState=_TpDldpState_Object((1,3,6,1,4,1,11863,6,58,1,4,1,2),_TpDldpState_Type())
tpDldpState.setMaxAccess(_C)
if mibBuilder.loadTexts:tpDldpState.setStatus(_A)
class _TpDldpProtocolState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('initial',0),('inactive',1),('active',2),('probe',3),('adver',4),(_E,5)))
_TpDldpProtocolState_Type.__name__=_B
_TpDldpProtocolState_Object=MibTableColumn
tpDldpProtocolState=_TpDldpProtocolState_Object((1,3,6,1,4,1,11863,6,58,1,4,1,3),_TpDldpProtocolState_Type())
tpDldpProtocolState.setMaxAccess(_D)
if mibBuilder.loadTexts:tpDldpProtocolState.setStatus(_A)
class _TpDldpLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('link-down',0),('link-up',1)))
_TpDldpLinkState_Type.__name__=_B
_TpDldpLinkState_Object=MibTableColumn
tpDldpLinkState=_TpDldpLinkState_Object((1,3,6,1,4,1,11863,6,58,1,4,1,4),_TpDldpLinkState_Type())
tpDldpLinkState.setMaxAccess(_D)
if mibBuilder.loadTexts:tpDldpLinkState.setStatus(_A)
class _TpDldpNeighborState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4)));namedValues=NamedValues(*(('unknown',0),('unidirectional',1),('bidirectional',2),('aging',3),('notAccess',4)))
_TpDldpNeighborState_Type.__name__=_B
_TpDldpNeighborState_Object=MibTableColumn
tpDldpNeighborState=_TpDldpNeighborState_Object((1,3,6,1,4,1,11863,6,58,1,4,1,5),_TpDldpNeighborState_Type())
tpDldpNeighborState.setMaxAccess(_D)
if mibBuilder.loadTexts:tpDldpNeighborState.setStatus(_A)
_TplinkDldpNotifications_ObjectIdentity=ObjectIdentity
tplinkDldpNotifications=_TplinkDldpNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,58,2))
tpDldpDetectUnidirectionalNeighor=NotificationType((1,3,6,1,4,1,11863,6,58,2,1))
if mibBuilder.loadTexts:tpDldpDetectUnidirectionalNeighor.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'tplinkDldpMIB':tplinkDldpMIB,'tplinkDldpMIBObjects':tplinkDldpMIBObjects,'tpDldpEnable':tpDldpEnable,'tpDldpInterval':tpDldpInterval,'tpDldpShutmode':tpDldpShutmode,'tpDldpCtrlTable':tpDldpCtrlTable,'tpDldpCtrlEntry':tpDldpCtrlEntry,_H:tpDldpPortId,'tpDldpState':tpDldpState,'tpDldpProtocolState':tpDldpProtocolState,'tpDldpLinkState':tpDldpLinkState,'tpDldpNeighborState':tpDldpNeighborState,'tplinkDldpNotifications':tplinkDldpNotifications,'tpDldpDetectUnidirectionalNeighor':tpDldpDetectUnidirectionalNeighor})