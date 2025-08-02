_E='read-only'
_D='ifIndex'
_C='IF-MIB'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_C,_D)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkPortIsolationMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,13))
if mibBuilder.loadTexts:tplinkPortIsolationMIB.setRevisions(('2012-12-13 09:30',))
_TplinkPortIsolationMIBObjects_ObjectIdentity=ObjectIdentity
tplinkPortIsolationMIBObjects=_TplinkPortIsolationMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,13,1))
_PortIsolationCtrlTable_Object=MibTable
portIsolationCtrlTable=_PortIsolationCtrlTable_Object((1,3,6,1,4,1,11863,6,13,1,1))
if mibBuilder.loadTexts:portIsolationCtrlTable.setStatus(_A)
_PortIsolationCtrlEntry_Object=MibTableRow
portIsolationCtrlEntry=_PortIsolationCtrlEntry_Object((1,3,6,1,4,1,11863,6,13,1,1,1))
portIsolationCtrlEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:portIsolationCtrlEntry.setStatus(_A)
class _PortIsolationPortId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_PortIsolationPortId_Type.__name__=_B
_PortIsolationPortId_Object=MibTableColumn
portIsolationPortId=_PortIsolationPortId_Object((1,3,6,1,4,1,11863,6,13,1,1,1,1),_PortIsolationPortId_Type())
portIsolationPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:portIsolationPortId.setStatus(_A)
class _PortIsolationForList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_PortIsolationForList_Type.__name__=_B
_PortIsolationForList_Object=MibTableColumn
portIsolationForList=_PortIsolationForList_Object((1,3,6,1,4,1,11863,6,13,1,1,1,2),_PortIsolationForList_Type())
portIsolationForList.setMaxAccess('read-write')
if mibBuilder.loadTexts:portIsolationForList.setStatus(_A)
class _PortIsolationLagId_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_PortIsolationLagId_Type.__name__=_B
_PortIsolationLagId_Object=MibTableColumn
portIsolationLagId=_PortIsolationLagId_Object((1,3,6,1,4,1,11863,6,13,1,1,1,3),_PortIsolationLagId_Type())
portIsolationLagId.setMaxAccess(_E)
if mibBuilder.loadTexts:portIsolationLagId.setStatus(_A)
_TplinkPortIsolationMIBNotifications_ObjectIdentity=ObjectIdentity
tplinkPortIsolationMIBNotifications=_TplinkPortIsolationMIBNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,13,2))
mibBuilder.exportSymbols('TPLINK-PORTISOLATION-MIB',**{'tplinkPortIsolationMIB':tplinkPortIsolationMIB,'tplinkPortIsolationMIBObjects':tplinkPortIsolationMIBObjects,'portIsolationCtrlTable':portIsolationCtrlTable,'portIsolationCtrlEntry':portIsolationCtrlEntry,'portIsolationPortId':portIsolationPortId,'portIsolationForList':portIsolationForList,'portIsolationLagId':portIsolationLagId,'tplinkPortIsolationMIBNotifications':tplinkPortIsolationMIBNotifications})