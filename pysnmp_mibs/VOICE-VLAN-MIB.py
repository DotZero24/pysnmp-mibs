_N='swVoiceVlanPortNumber'
_M='swVoiceVlanOuiAddr'
_L='swVoiceVlanlldpMedDeviceIndex'
_K='swVoiceVlanDeviceAddr'
_J='swVoiceVlanPort'
_I='TruthValue'
_H='read-create'
_G='disabled'
_F='enabled'
_E='VOICE-VLAN-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
LldpChassisId,LldpChassisIdSubtype,LldpPortId,LldpPortIdSubtype=mibBuilder.importSymbols('LLDP-MIB','LldpChassisId','LldpChassisIdSubtype','LldpPortId','LldpPortIdSubtype')
PortList,VlanIdOrNone=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList','VlanIdOrNone')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeInterval',_I)
swVoiceVLANMIB=ModuleIdentity((1,3,6,1,4,1,171,12,74))
_SwVoiceVlanCtrl_ObjectIdentity=ObjectIdentity
swVoiceVlanCtrl=_SwVoiceVlanCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,74,1))
_SwVoiceVlanId_Type=VlanIdOrNone
_SwVoiceVlanId_Object=MibScalar
swVoiceVlanId=_SwVoiceVlanId_Object((1,3,6,1,4,1,171,12,74,1,1),_SwVoiceVlanId_Type())
swVoiceVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:swVoiceVlanId.setStatus(_A)
class _SwVoivceVlanGlobalState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwVoivceVlanGlobalState_Type.__name__=_D
_SwVoivceVlanGlobalState_Object=MibScalar
swVoivceVlanGlobalState=_SwVoivceVlanGlobalState_Object((1,3,6,1,4,1,171,12,74,1,2),_SwVoivceVlanGlobalState_Type())
swVoivceVlanGlobalState.setMaxAccess(_C)
if mibBuilder.loadTexts:swVoivceVlanGlobalState.setStatus(_A)
class _SwVoiceVlanPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwVoiceVlanPriority_Type.__name__=_D
_SwVoiceVlanPriority_Object=MibScalar
swVoiceVlanPriority=_SwVoiceVlanPriority_Object((1,3,6,1,4,1,171,12,74,1,3),_SwVoiceVlanPriority_Type())
swVoiceVlanPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:swVoiceVlanPriority.setStatus(_A)
class _SwVoiceVlanAgingTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_SwVoiceVlanAgingTime_Type.__name__=_D
_SwVoiceVlanAgingTime_Object=MibScalar
swVoiceVlanAgingTime=_SwVoiceVlanAgingTime_Object((1,3,6,1,4,1,171,12,74,1,4),_SwVoiceVlanAgingTime_Type())
swVoiceVlanAgingTime.setMaxAccess(_C)
if mibBuilder.loadTexts:swVoiceVlanAgingTime.setStatus(_A)
class _SwVoiceVlanLogState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwVoiceVlanLogState_Type.__name__=_D
_SwVoiceVlanLogState_Object=MibScalar
swVoiceVlanLogState=_SwVoiceVlanLogState_Object((1,3,6,1,4,1,171,12,74,1,5),_SwVoiceVlanLogState_Type())
swVoiceVlanLogState.setMaxAccess(_C)
if mibBuilder.loadTexts:swVoiceVlanLogState.setStatus(_A)
_SwVoiceVlanInfo_ObjectIdentity=ObjectIdentity
swVoiceVlanInfo=_SwVoiceVlanInfo_ObjectIdentity((1,3,6,1,4,1,171,12,74,2))
_SwVoiceVlanMemberPortlist_Type=PortList
_SwVoiceVlanMemberPortlist_Object=MibScalar
swVoiceVlanMemberPortlist=_SwVoiceVlanMemberPortlist_Object((1,3,6,1,4,1,171,12,74,2,1),_SwVoiceVlanMemberPortlist_Type())
swVoiceVlanMemberPortlist.setMaxAccess(_B)
if mibBuilder.loadTexts:swVoiceVlanMemberPortlist.setStatus(_A)
_SwVoiceVlanDynamicPortlist_Type=PortList
_SwVoiceVlanDynamicPortlist_Object=MibScalar
swVoiceVlanDynamicPortlist=_SwVoiceVlanDynamicPortlist_Object((1,3,6,1,4,1,171,12,74,2,2),_SwVoiceVlanDynamicPortlist_Type())
swVoiceVlanDynamicPortlist.setMaxAccess(_B)
if mibBuilder.loadTexts:swVoiceVlanDynamicPortlist.setStatus(_A)
_SwVoiceVlanDeviceTable_Object=MibTable
swVoiceVlanDeviceTable=_SwVoiceVlanDeviceTable_Object((1,3,6,1,4,1,171,12,74,2,3))
if mibBuilder.loadTexts:swVoiceVlanDeviceTable.setStatus(_A)
_SwVoiceVlanDeviceEntry_Object=MibTableRow
swVoiceVlanDeviceEntry=_SwVoiceVlanDeviceEntry_Object((1,3,6,1,4,1,171,12,74,2,3,1))
swVoiceVlanDeviceEntry.setIndexNames((0,_E,_J),(0,_E,_K))
if mibBuilder.loadTexts:swVoiceVlanDeviceEntry.setStatus(_A)
_SwVoiceVlanPort_Type=Integer32
_SwVoiceVlanPort_Object=MibTableColumn
swVoiceVlanPort=_SwVoiceVlanPort_Object((1,3,6,1,4,1,171,12,74,2,3,1,1),_SwVoiceVlanPort_Type())
swVoiceVlanPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swVoiceVlanPort.setStatus(_A)
_SwVoiceVlanDeviceAddr_Type=MacAddress
_SwVoiceVlanDeviceAddr_Object=MibTableColumn
swVoiceVlanDeviceAddr=_SwVoiceVlanDeviceAddr_Object((1,3,6,1,4,1,171,12,74,2,3,1,2),_SwVoiceVlanDeviceAddr_Type())
swVoiceVlanDeviceAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swVoiceVlanDeviceAddr.setStatus(_A)
_SwVoiceVlanDeviceStartTime_Type=DateAndTime
_SwVoiceVlanDeviceStartTime_Object=MibTableColumn
swVoiceVlanDeviceStartTime=_SwVoiceVlanDeviceStartTime_Object((1,3,6,1,4,1,171,12,74,2,3,1,3),_SwVoiceVlanDeviceStartTime_Type())
swVoiceVlanDeviceStartTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swVoiceVlanDeviceStartTime.setStatus(_A)
_SwVoiceVlanDeviceActiveTime_Type=DateAndTime
_SwVoiceVlanDeviceActiveTime_Object=MibTableColumn
swVoiceVlanDeviceActiveTime=_SwVoiceVlanDeviceActiveTime_Object((1,3,6,1,4,1,171,12,74,2,3,1,4),_SwVoiceVlanDeviceActiveTime_Type())
swVoiceVlanDeviceActiveTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swVoiceVlanDeviceActiveTime.setStatus(_A)
_SwVoiceVlanlldpMedDeviceTable_Object=MibTable
swVoiceVlanlldpMedDeviceTable=_SwVoiceVlanlldpMedDeviceTable_Object((1,3,6,1,4,1,171,12,74,2,4))
if mibBuilder.loadTexts:swVoiceVlanlldpMedDeviceTable.setStatus(_A)
_SwVoiceVlanlldpMedDeviceEntry_Object=MibTableRow
swVoiceVlanlldpMedDeviceEntry=_SwVoiceVlanlldpMedDeviceEntry_Object((1,3,6,1,4,1,171,12,74,2,4,1))
swVoiceVlanlldpMedDeviceEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:swVoiceVlanlldpMedDeviceEntry.setStatus(_A)
_SwVoiceVlanlldpMedDeviceIndex_Type=Integer32
_SwVoiceVlanlldpMedDeviceIndex_Object=MibTableColumn
swVoiceVlanlldpMedDeviceIndex=_SwVoiceVlanlldpMedDeviceIndex_Object((1,3,6,1,4,1,171,12,74,2,4,1,1),_SwVoiceVlanlldpMedDeviceIndex_Type())
swVoiceVlanlldpMedDeviceIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:swVoiceVlanlldpMedDeviceIndex.setStatus(_A)
_SwVoiceVlanlldpMedDeviceLocalPort_Type=Integer32
_SwVoiceVlanlldpMedDeviceLocalPort_Object=MibTableColumn
swVoiceVlanlldpMedDeviceLocalPort=_SwVoiceVlanlldpMedDeviceLocalPort_Object((1,3,6,1,4,1,171,12,74,2,4,1,2),_SwVoiceVlanlldpMedDeviceLocalPort_Type())
swVoiceVlanlldpMedDeviceLocalPort.setMaxAccess(_B)
if mibBuilder.loadTexts:swVoiceVlanlldpMedDeviceLocalPort.setStatus(_A)
_SwVoiceVlanlldpMedDeviceChassisIdSubtype_Type=LldpChassisIdSubtype
_SwVoiceVlanlldpMedDeviceChassisIdSubtype_Object=MibTableColumn
swVoiceVlanlldpMedDeviceChassisIdSubtype=_SwVoiceVlanlldpMedDeviceChassisIdSubtype_Object((1,3,6,1,4,1,171,12,74,2,4,1,3),_SwVoiceVlanlldpMedDeviceChassisIdSubtype_Type())
swVoiceVlanlldpMedDeviceChassisIdSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:swVoiceVlanlldpMedDeviceChassisIdSubtype.setStatus(_A)
_SwVoiceVlanlldpMedDeviceChassisId_Type=LldpChassisId
_SwVoiceVlanlldpMedDeviceChassisId_Object=MibTableColumn
swVoiceVlanlldpMedDeviceChassisId=_SwVoiceVlanlldpMedDeviceChassisId_Object((1,3,6,1,4,1,171,12,74,2,4,1,4),_SwVoiceVlanlldpMedDeviceChassisId_Type())
swVoiceVlanlldpMedDeviceChassisId.setMaxAccess(_B)
if mibBuilder.loadTexts:swVoiceVlanlldpMedDeviceChassisId.setStatus(_A)
_SwVoiceVlanlldpMedDevicePortIdSubtype_Type=LldpPortIdSubtype
_SwVoiceVlanlldpMedDevicePortIdSubtype_Object=MibTableColumn
swVoiceVlanlldpMedDevicePortIdSubtype=_SwVoiceVlanlldpMedDevicePortIdSubtype_Object((1,3,6,1,4,1,171,12,74,2,4,1,5),_SwVoiceVlanlldpMedDevicePortIdSubtype_Type())
swVoiceVlanlldpMedDevicePortIdSubtype.setMaxAccess(_B)
if mibBuilder.loadTexts:swVoiceVlanlldpMedDevicePortIdSubtype.setStatus(_A)
_SwVoiceVlanlldpMedDevicePortId_Type=LldpPortId
_SwVoiceVlanlldpMedDevicePortId_Object=MibTableColumn
swVoiceVlanlldpMedDevicePortId=_SwVoiceVlanlldpMedDevicePortId_Object((1,3,6,1,4,1,171,12,74,2,4,1,6),_SwVoiceVlanlldpMedDevicePortId_Type())
swVoiceVlanlldpMedDevicePortId.setMaxAccess(_B)
if mibBuilder.loadTexts:swVoiceVlanlldpMedDevicePortId.setStatus(_A)
_SwVoiceVlanlldpMedDeviceCreateTime_Type=DateAndTime
_SwVoiceVlanlldpMedDeviceCreateTime_Object=MibTableColumn
swVoiceVlanlldpMedDeviceCreateTime=_SwVoiceVlanlldpMedDeviceCreateTime_Object((1,3,6,1,4,1,171,12,74,2,4,1,7),_SwVoiceVlanlldpMedDeviceCreateTime_Type())
swVoiceVlanlldpMedDeviceCreateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swVoiceVlanlldpMedDeviceCreateTime.setStatus(_A)
_SwVoiceVlanlldpMedDeviceRemainTime_Type=TimeInterval
_SwVoiceVlanlldpMedDeviceRemainTime_Object=MibTableColumn
swVoiceVlanlldpMedDeviceRemainTime=_SwVoiceVlanlldpMedDeviceRemainTime_Object((1,3,6,1,4,1,171,12,74,2,4,1,8),_SwVoiceVlanlldpMedDeviceRemainTime_Type())
swVoiceVlanlldpMedDeviceRemainTime.setMaxAccess(_B)
if mibBuilder.loadTexts:swVoiceVlanlldpMedDeviceRemainTime.setStatus(_A)
_SwVoiceVlanMgmt_ObjectIdentity=ObjectIdentity
swVoiceVlanMgmt=_SwVoiceVlanMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,74,3))
_SwVoiceVlanOuiTable_Object=MibTable
swVoiceVlanOuiTable=_SwVoiceVlanOuiTable_Object((1,3,6,1,4,1,171,12,74,3,1))
if mibBuilder.loadTexts:swVoiceVlanOuiTable.setStatus(_A)
_SwVoiceVlanOuiEntry_Object=MibTableRow
swVoiceVlanOuiEntry=_SwVoiceVlanOuiEntry_Object((1,3,6,1,4,1,171,12,74,3,1,1))
swVoiceVlanOuiEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:swVoiceVlanOuiEntry.setStatus(_A)
_SwVoiceVlanOuiAddr_Type=MacAddress
_SwVoiceVlanOuiAddr_Object=MibTableColumn
swVoiceVlanOuiAddr=_SwVoiceVlanOuiAddr_Object((1,3,6,1,4,1,171,12,74,3,1,1,1),_SwVoiceVlanOuiAddr_Type())
swVoiceVlanOuiAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:swVoiceVlanOuiAddr.setStatus(_A)
_SwVoiceVlanOuiMask_Type=MacAddress
_SwVoiceVlanOuiMask_Object=MibTableColumn
swVoiceVlanOuiMask=_SwVoiceVlanOuiMask_Object((1,3,6,1,4,1,171,12,74,3,1,1,2),_SwVoiceVlanOuiMask_Type())
swVoiceVlanOuiMask.setMaxAccess(_H)
if mibBuilder.loadTexts:swVoiceVlanOuiMask.setStatus(_A)
_SwVoiceVlanOuiDes_Type=DisplayString
_SwVoiceVlanOuiDes_Object=MibTableColumn
swVoiceVlanOuiDes=_SwVoiceVlanOuiDes_Object((1,3,6,1,4,1,171,12,74,3,1,1,3),_SwVoiceVlanOuiDes_Type())
swVoiceVlanOuiDes.setMaxAccess(_H)
if mibBuilder.loadTexts:swVoiceVlanOuiDes.setStatus(_A)
_SwVoiceVlanOuiRowStatus_Type=RowStatus
_SwVoiceVlanOuiRowStatus_Object=MibTableColumn
swVoiceVlanOuiRowStatus=_SwVoiceVlanOuiRowStatus_Object((1,3,6,1,4,1,171,12,74,3,1,1,4),_SwVoiceVlanOuiRowStatus_Type())
swVoiceVlanOuiRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:swVoiceVlanOuiRowStatus.setStatus(_A)
_SwVoiceVlanPortTable_Object=MibTable
swVoiceVlanPortTable=_SwVoiceVlanPortTable_Object((1,3,6,1,4,1,171,12,74,3,2))
if mibBuilder.loadTexts:swVoiceVlanPortTable.setStatus(_A)
_SwVoiceVlanPortEntry_Object=MibTableRow
swVoiceVlanPortEntry=_SwVoiceVlanPortEntry_Object((1,3,6,1,4,1,171,12,74,3,2,1))
swVoiceVlanPortEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:swVoiceVlanPortEntry.setStatus(_A)
_SwVoiceVlanPortNumber_Type=Integer32
_SwVoiceVlanPortNumber_Object=MibTableColumn
swVoiceVlanPortNumber=_SwVoiceVlanPortNumber_Object((1,3,6,1,4,1,171,12,74,3,2,1,1),_SwVoiceVlanPortNumber_Type())
swVoiceVlanPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:swVoiceVlanPortNumber.setStatus(_A)
class _SwVoiceVlanPortState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SwVoiceVlanPortState_Type.__name__=_D
_SwVoiceVlanPortState_Object=MibTableColumn
swVoiceVlanPortState=_SwVoiceVlanPortState_Object((1,3,6,1,4,1,171,12,74,3,2,1,2),_SwVoiceVlanPortState_Type())
swVoiceVlanPortState.setMaxAccess(_C)
if mibBuilder.loadTexts:swVoiceVlanPortState.setStatus(_A)
class _SwVoiceVlanPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('auto',1),('manual',2)))
_SwVoiceVlanPortMode_Type.__name__=_D
_SwVoiceVlanPortMode_Object=MibTableColumn
swVoiceVlanPortMode=_SwVoiceVlanPortMode_Object((1,3,6,1,4,1,171,12,74,3,2,1,3),_SwVoiceVlanPortMode_Type())
swVoiceVlanPortMode.setMaxAccess(_C)
if mibBuilder.loadTexts:swVoiceVlanPortMode.setStatus(_A)
class _SwVoiceVlanPortTagged_Type(TruthValue):defaultValue=2
_SwVoiceVlanPortTagged_Type.__name__=_I
_SwVoiceVlanPortTagged_Object=MibTableColumn
swVoiceVlanPortTagged=_SwVoiceVlanPortTagged_Object((1,3,6,1,4,1,171,12,74,3,2,1,4),_SwVoiceVlanPortTagged_Type())
swVoiceVlanPortTagged.setMaxAccess(_C)
if mibBuilder.loadTexts:swVoiceVlanPortTagged.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'swVoiceVLANMIB':swVoiceVLANMIB,'swVoiceVlanCtrl':swVoiceVlanCtrl,'swVoiceVlanId':swVoiceVlanId,'swVoivceVlanGlobalState':swVoivceVlanGlobalState,'swVoiceVlanPriority':swVoiceVlanPriority,'swVoiceVlanAgingTime':swVoiceVlanAgingTime,'swVoiceVlanLogState':swVoiceVlanLogState,'swVoiceVlanInfo':swVoiceVlanInfo,'swVoiceVlanMemberPortlist':swVoiceVlanMemberPortlist,'swVoiceVlanDynamicPortlist':swVoiceVlanDynamicPortlist,'swVoiceVlanDeviceTable':swVoiceVlanDeviceTable,'swVoiceVlanDeviceEntry':swVoiceVlanDeviceEntry,_J:swVoiceVlanPort,_K:swVoiceVlanDeviceAddr,'swVoiceVlanDeviceStartTime':swVoiceVlanDeviceStartTime,'swVoiceVlanDeviceActiveTime':swVoiceVlanDeviceActiveTime,'swVoiceVlanlldpMedDeviceTable':swVoiceVlanlldpMedDeviceTable,'swVoiceVlanlldpMedDeviceEntry':swVoiceVlanlldpMedDeviceEntry,_L:swVoiceVlanlldpMedDeviceIndex,'swVoiceVlanlldpMedDeviceLocalPort':swVoiceVlanlldpMedDeviceLocalPort,'swVoiceVlanlldpMedDeviceChassisIdSubtype':swVoiceVlanlldpMedDeviceChassisIdSubtype,'swVoiceVlanlldpMedDeviceChassisId':swVoiceVlanlldpMedDeviceChassisId,'swVoiceVlanlldpMedDevicePortIdSubtype':swVoiceVlanlldpMedDevicePortIdSubtype,'swVoiceVlanlldpMedDevicePortId':swVoiceVlanlldpMedDevicePortId,'swVoiceVlanlldpMedDeviceCreateTime':swVoiceVlanlldpMedDeviceCreateTime,'swVoiceVlanlldpMedDeviceRemainTime':swVoiceVlanlldpMedDeviceRemainTime,'swVoiceVlanMgmt':swVoiceVlanMgmt,'swVoiceVlanOuiTable':swVoiceVlanOuiTable,'swVoiceVlanOuiEntry':swVoiceVlanOuiEntry,_M:swVoiceVlanOuiAddr,'swVoiceVlanOuiMask':swVoiceVlanOuiMask,'swVoiceVlanOuiDes':swVoiceVlanOuiDes,'swVoiceVlanOuiRowStatus':swVoiceVlanOuiRowStatus,'swVoiceVlanPortTable':swVoiceVlanPortTable,'swVoiceVlanPortEntry':swVoiceVlanPortEntry,_N:swVoiceVlanPortNumber,'swVoiceVlanPortState':swVoiceVlanPortState,'swVoiceVlanPortMode':swVoiceVlanPortMode,'swVoiceVlanPortTagged':swVoiceVlanPortTagged})