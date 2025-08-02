_G='swSecondaryVlanId'
_F='read-only'
_E='read-write'
_D='swPrivateVlanId'
_C='read-create'
_B='PRIVATE-VLAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
PortList,VlanId,VlanIdOrNone=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanId','VlanIdOrNone')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
swPrivateVLANMIB=ModuleIdentity((1,3,6,1,4,1,171,12,69))
class SecondaryVlanType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('isolated',1),('community',2)))
_SwPrivateVlanCtrl_ObjectIdentity=ObjectIdentity
swPrivateVlanCtrl=_SwPrivateVlanCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,69,1))
_SwPrivateVlanInfo_ObjectIdentity=ObjectIdentity
swPrivateVlanInfo=_SwPrivateVlanInfo_ObjectIdentity((1,3,6,1,4,1,171,12,69,2))
_SwPrivateVlanMgmt_ObjectIdentity=ObjectIdentity
swPrivateVlanMgmt=_SwPrivateVlanMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,69,3))
_SwPrivateVlanTable_Object=MibTable
swPrivateVlanTable=_SwPrivateVlanTable_Object((1,3,6,1,4,1,171,12,69,3,1))
if mibBuilder.loadTexts:swPrivateVlanTable.setStatus(_A)
_SwPrivateVlanEntry_Object=MibTableRow
swPrivateVlanEntry=_SwPrivateVlanEntry_Object((1,3,6,1,4,1,171,12,69,3,1,1))
swPrivateVlanEntry.setIndexNames((0,_B,_D))
if mibBuilder.loadTexts:swPrivateVlanEntry.setStatus(_A)
_SwPrivateVlanId_Type=VlanId
_SwPrivateVlanId_Object=MibTableColumn
swPrivateVlanId=_SwPrivateVlanId_Object((1,3,6,1,4,1,171,12,69,3,1,1,1),_SwPrivateVlanId_Type())
swPrivateVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:swPrivateVlanId.setStatus(_A)
_SwPrivateVlanName_Type=DisplayString
_SwPrivateVlanName_Object=MibTableColumn
swPrivateVlanName=_SwPrivateVlanName_Object((1,3,6,1,4,1,171,12,69,3,1,1,2),_SwPrivateVlanName_Type())
swPrivateVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:swPrivateVlanName.setStatus(_A)
_SwPrivateVlanPromiscuousPorts_Type=PortList
_SwPrivateVlanPromiscuousPorts_Object=MibTableColumn
swPrivateVlanPromiscuousPorts=_SwPrivateVlanPromiscuousPorts_Object((1,3,6,1,4,1,171,12,69,3,1,1,3),_SwPrivateVlanPromiscuousPorts_Type())
swPrivateVlanPromiscuousPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:swPrivateVlanPromiscuousPorts.setStatus(_A)
_SwPrivateVlanTrunkPorts_Type=PortList
_SwPrivateVlanTrunkPorts_Object=MibTableColumn
swPrivateVlanTrunkPorts=_SwPrivateVlanTrunkPorts_Object((1,3,6,1,4,1,171,12,69,3,1,1,4),_SwPrivateVlanTrunkPorts_Type())
swPrivateVlanTrunkPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:swPrivateVlanTrunkPorts.setStatus(_A)
_SwPrivateVlanRowStatus_Type=RowStatus
_SwPrivateVlanRowStatus_Object=MibTableColumn
swPrivateVlanRowStatus=_SwPrivateVlanRowStatus_Object((1,3,6,1,4,1,171,12,69,3,1,1,5),_SwPrivateVlanRowStatus_Type())
swPrivateVlanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swPrivateVlanRowStatus.setStatus(_A)
_SwSecondaryVlanTable_Object=MibTable
swSecondaryVlanTable=_SwSecondaryVlanTable_Object((1,3,6,1,4,1,171,12,69,3,2))
if mibBuilder.loadTexts:swSecondaryVlanTable.setStatus(_A)
_SwSecondaryVlanEntry_Object=MibTableRow
swSecondaryVlanEntry=_SwSecondaryVlanEntry_Object((1,3,6,1,4,1,171,12,69,3,2,1))
swSecondaryVlanEntry.setIndexNames((0,_B,_D),(0,_B,_G))
if mibBuilder.loadTexts:swSecondaryVlanEntry.setStatus(_A)
_SwSecondaryVlanId_Type=VlanId
_SwSecondaryVlanId_Object=MibTableColumn
swSecondaryVlanId=_SwSecondaryVlanId_Object((1,3,6,1,4,1,171,12,69,3,2,1,1),_SwSecondaryVlanId_Type())
swSecondaryVlanId.setMaxAccess(_F)
if mibBuilder.loadTexts:swSecondaryVlanId.setStatus(_A)
_SwSecondaryVlanType_Type=SecondaryVlanType
_SwSecondaryVlanType_Object=MibTableColumn
swSecondaryVlanType=_SwSecondaryVlanType_Object((1,3,6,1,4,1,171,12,69,3,2,1,2),_SwSecondaryVlanType_Type())
swSecondaryVlanType.setMaxAccess(_C)
if mibBuilder.loadTexts:swSecondaryVlanType.setStatus(_A)
_SwSecondaryVlanPorts_Type=PortList
_SwSecondaryVlanPorts_Object=MibTableColumn
swSecondaryVlanPorts=_SwSecondaryVlanPorts_Object((1,3,6,1,4,1,171,12,69,3,2,1,3),_SwSecondaryVlanPorts_Type())
swSecondaryVlanPorts.setMaxAccess(_E)
if mibBuilder.loadTexts:swSecondaryVlanPorts.setStatus(_A)
_SwSecondaryVlanRowStatus_Type=RowStatus
_SwSecondaryVlanRowStatus_Object=MibTableColumn
swSecondaryVlanRowStatus=_SwSecondaryVlanRowStatus_Object((1,3,6,1,4,1,171,12,69,3,2,1,4),_SwSecondaryVlanRowStatus_Type())
swSecondaryVlanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swSecondaryVlanRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SecondaryVlanType':SecondaryVlanType,'swPrivateVLANMIB':swPrivateVLANMIB,'swPrivateVlanCtrl':swPrivateVlanCtrl,'swPrivateVlanInfo':swPrivateVlanInfo,'swPrivateVlanMgmt':swPrivateVlanMgmt,'swPrivateVlanTable':swPrivateVlanTable,'swPrivateVlanEntry':swPrivateVlanEntry,_D:swPrivateVlanId,'swPrivateVlanName':swPrivateVlanName,'swPrivateVlanPromiscuousPorts':swPrivateVlanPromiscuousPorts,'swPrivateVlanTrunkPorts':swPrivateVlanTrunkPorts,'swPrivateVlanRowStatus':swPrivateVlanRowStatus,'swSecondaryVlanTable':swSecondaryVlanTable,'swSecondaryVlanEntry':swSecondaryVlanEntry,_G:swSecondaryVlanId,'swSecondaryVlanType':swSecondaryVlanType,'swSecondaryVlanPorts':swSecondaryVlanPorts,'swSecondaryVlanRowStatus':swSecondaryVlanRowStatus})