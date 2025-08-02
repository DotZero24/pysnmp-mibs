_I='read-only'
_H='swDoubleVlanSPVIDIndex'
_G='Double-VLAN-MIB'
_F='DisplayString'
_E='OctetString'
_D='read-create'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
swDoubleVlanMIB=ModuleIdentity((1,3,6,1,4,1,171,12,28))
class PortList(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_SwDoubleVlanCtrl_ObjectIdentity=ObjectIdentity
swDoubleVlanCtrl=_SwDoubleVlanCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,28,1))
class _SwDoubleVlanGlobalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('disabled',2),('enabled',3)))
_SwDoubleVlanGlobalState_Type.__name__=_C
_SwDoubleVlanGlobalState_Object=MibScalar
swDoubleVlanGlobalState=_SwDoubleVlanGlobalState_Object((1,3,6,1,4,1,171,12,28,1,1),_SwDoubleVlanGlobalState_Type())
swDoubleVlanGlobalState.setMaxAccess(_B)
if mibBuilder.loadTexts:swDoubleVlanGlobalState.setStatus(_A)
_SwDoubleVlanInfo_ObjectIdentity=ObjectIdentity
swDoubleVlanInfo=_SwDoubleVlanInfo_ObjectIdentity((1,3,6,1,4,1,171,12,28,2))
_SwDoubleVlanMgmt_ObjectIdentity=ObjectIdentity
swDoubleVlanMgmt=_SwDoubleVlanMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,28,3))
_SwDoubleVlanCtrlTable_Object=MibTable
swDoubleVlanCtrlTable=_SwDoubleVlanCtrlTable_Object((1,3,6,1,4,1,171,12,28,3,1))
if mibBuilder.loadTexts:swDoubleVlanCtrlTable.setStatus(_A)
_SwDoubleVlanCtrlEntry_Object=MibTableRow
swDoubleVlanCtrlEntry=_SwDoubleVlanCtrlEntry_Object((1,3,6,1,4,1,171,12,28,3,1,1))
swDoubleVlanCtrlEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:swDoubleVlanCtrlEntry.setStatus(_A)
class _SwDoubleVlanSPVIDIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwDoubleVlanSPVIDIndex_Type.__name__=_C
_SwDoubleVlanSPVIDIndex_Object=MibTableColumn
swDoubleVlanSPVIDIndex=_SwDoubleVlanSPVIDIndex_Object((1,3,6,1,4,1,171,12,28,3,1,1,1),_SwDoubleVlanSPVIDIndex_Type())
swDoubleVlanSPVIDIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:swDoubleVlanSPVIDIndex.setStatus(_A)
class _SwDoubleVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SwDoubleVlanName_Type.__name__=_F
_SwDoubleVlanName_Object=MibTableColumn
swDoubleVlanName=_SwDoubleVlanName_Object((1,3,6,1,4,1,171,12,28,3,1,1,2),_SwDoubleVlanName_Type())
swDoubleVlanName.setMaxAccess(_D)
if mibBuilder.loadTexts:swDoubleVlanName.setStatus(_A)
class _SwDoubleVlanTPID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(2,2));fixedLength=2
_SwDoubleVlanTPID_Type.__name__=_E
_SwDoubleVlanTPID_Object=MibTableColumn
swDoubleVlanTPID=_SwDoubleVlanTPID_Object((1,3,6,1,4,1,171,12,28,3,1,1,3),_SwDoubleVlanTPID_Type())
swDoubleVlanTPID.setMaxAccess(_D)
if mibBuilder.loadTexts:swDoubleVlanTPID.setStatus(_A)
_SwDoubleVlanUplinkPorts_Type=PortList
_SwDoubleVlanUplinkPorts_Object=MibTableColumn
swDoubleVlanUplinkPorts=_SwDoubleVlanUplinkPorts_Object((1,3,6,1,4,1,171,12,28,3,1,1,4),_SwDoubleVlanUplinkPorts_Type())
swDoubleVlanUplinkPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:swDoubleVlanUplinkPorts.setStatus(_A)
_SwDoubleVlanAccessPorts_Type=PortList
_SwDoubleVlanAccessPorts_Object=MibTableColumn
swDoubleVlanAccessPorts=_SwDoubleVlanAccessPorts_Object((1,3,6,1,4,1,171,12,28,3,1,1,5),_SwDoubleVlanAccessPorts_Type())
swDoubleVlanAccessPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:swDoubleVlanAccessPorts.setStatus(_A)
_SwDoubleVlanUnknowPorts_Type=PortList
_SwDoubleVlanUnknowPorts_Object=MibTableColumn
swDoubleVlanUnknowPorts=_SwDoubleVlanUnknowPorts_Object((1,3,6,1,4,1,171,12,28,3,1,1,6),_SwDoubleVlanUnknowPorts_Type())
swDoubleVlanUnknowPorts.setMaxAccess(_I)
if mibBuilder.loadTexts:swDoubleVlanUnknowPorts.setStatus(_A)
_SwDoubleVlanDeletePorts_Type=PortList
_SwDoubleVlanDeletePorts_Object=MibTableColumn
swDoubleVlanDeletePorts=_SwDoubleVlanDeletePorts_Object((1,3,6,1,4,1,171,12,28,3,1,1,7),_SwDoubleVlanDeletePorts_Type())
swDoubleVlanDeletePorts.setMaxAccess(_B)
if mibBuilder.loadTexts:swDoubleVlanDeletePorts.setStatus(_A)
_SwDoubleVlanStatus_Type=RowStatus
_SwDoubleVlanStatus_Object=MibTableColumn
swDoubleVlanStatus=_SwDoubleVlanStatus_Object((1,3,6,1,4,1,171,12,28,3,1,1,9),_SwDoubleVlanStatus_Type())
swDoubleVlanStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:swDoubleVlanStatus.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'PortList':PortList,'swDoubleVlanMIB':swDoubleVlanMIB,'swDoubleVlanCtrl':swDoubleVlanCtrl,'swDoubleVlanGlobalState':swDoubleVlanGlobalState,'swDoubleVlanInfo':swDoubleVlanInfo,'swDoubleVlanMgmt':swDoubleVlanMgmt,'swDoubleVlanCtrlTable':swDoubleVlanCtrlTable,'swDoubleVlanCtrlEntry':swDoubleVlanCtrlEntry,_H:swDoubleVlanSPVIDIndex,'swDoubleVlanName':swDoubleVlanName,'swDoubleVlanTPID':swDoubleVlanTPID,'swDoubleVlanUplinkPorts':swDoubleVlanUplinkPorts,'swDoubleVlanAccessPorts':swDoubleVlanAccessPorts,'swDoubleVlanUnknowPorts':swDoubleVlanUnknowPorts,'swDoubleVlanDeletePorts':swDoubleVlanDeletePorts,'swDoubleVlanStatus':swDoubleVlanStatus})