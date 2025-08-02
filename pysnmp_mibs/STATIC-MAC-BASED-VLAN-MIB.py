_J='swStaticMacBasedOptionVlanID'
_I='swStaticMacBasedVlanCtrlOptionMacAddr'
_H='swStaticMacBasedVlanCtrlMacAddr'
_G='DisplayString'
_F='read-only'
_E='STATIC-MAC-BASED-VLAN-MIB'
_D='Integer32'
_C='read-create'
_B='obsolete'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dlink_common_mgmt,=mibBuilder.importSymbols('DLINK-ID-REC-MIB','dlink-common-mgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_G,'MacAddress','PhysAddress','RowStatus','TextualConvention')
swSMBVMIB=ModuleIdentity((1,3,6,1,4,1,171,12,56))
_SwSmbvCtrl_ObjectIdentity=ObjectIdentity
swSmbvCtrl=_SwSmbvCtrl_ObjectIdentity((1,3,6,1,4,1,171,12,56,1))
_SwSmbvInfo_ObjectIdentity=ObjectIdentity
swSmbvInfo=_SwSmbvInfo_ObjectIdentity((1,3,6,1,4,1,171,12,56,2))
_SwSmbvMgmt_ObjectIdentity=ObjectIdentity
swSmbvMgmt=_SwSmbvMgmt_ObjectIdentity((1,3,6,1,4,1,171,12,56,3))
_SwStaticMacBasedVlanCtrlTable_Object=MibTable
swStaticMacBasedVlanCtrlTable=_SwStaticMacBasedVlanCtrlTable_Object((1,3,6,1,4,1,171,12,56,3,1))
if mibBuilder.loadTexts:swStaticMacBasedVlanCtrlTable.setStatus(_B)
_SwStaticMacBasedVlanCtrlEntry_Object=MibTableRow
swStaticMacBasedVlanCtrlEntry=_SwStaticMacBasedVlanCtrlEntry_Object((1,3,6,1,4,1,171,12,56,3,1,1))
swStaticMacBasedVlanCtrlEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:swStaticMacBasedVlanCtrlEntry.setStatus(_B)
_SwStaticMacBasedVlanCtrlMacAddr_Type=MacAddress
_SwStaticMacBasedVlanCtrlMacAddr_Object=MibTableColumn
swStaticMacBasedVlanCtrlMacAddr=_SwStaticMacBasedVlanCtrlMacAddr_Object((1,3,6,1,4,1,171,12,56,3,1,1,1),_SwStaticMacBasedVlanCtrlMacAddr_Type())
swStaticMacBasedVlanCtrlMacAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:swStaticMacBasedVlanCtrlMacAddr.setStatus(_B)
class _SwStaticMacBasedVlanCtrlVlanName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_SwStaticMacBasedVlanCtrlVlanName_Type.__name__=_G
_SwStaticMacBasedVlanCtrlVlanName_Object=MibTableColumn
swStaticMacBasedVlanCtrlVlanName=_SwStaticMacBasedVlanCtrlVlanName_Object((1,3,6,1,4,1,171,12,56,3,1,1,2),_SwStaticMacBasedVlanCtrlVlanName_Type())
swStaticMacBasedVlanCtrlVlanName.setMaxAccess(_C)
if mibBuilder.loadTexts:swStaticMacBasedVlanCtrlVlanName.setStatus(_B)
_SwStaticMacBasedVlanCtrlStatus_Type=RowStatus
_SwStaticMacBasedVlanCtrlStatus_Object=MibTableColumn
swStaticMacBasedVlanCtrlStatus=_SwStaticMacBasedVlanCtrlStatus_Object((1,3,6,1,4,1,171,12,56,3,1,1,3),_SwStaticMacBasedVlanCtrlStatus_Type())
swStaticMacBasedVlanCtrlStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swStaticMacBasedVlanCtrlStatus.setStatus(_B)
_SwStaticMacBasedVlanCtrlOptionTable_Object=MibTable
swStaticMacBasedVlanCtrlOptionTable=_SwStaticMacBasedVlanCtrlOptionTable_Object((1,3,6,1,4,1,171,12,56,3,2))
if mibBuilder.loadTexts:swStaticMacBasedVlanCtrlOptionTable.setStatus(_A)
_SwStaticMacBasedVlanCtrlOptionEntry_Object=MibTableRow
swStaticMacBasedVlanCtrlOptionEntry=_SwStaticMacBasedVlanCtrlOptionEntry_Object((1,3,6,1,4,1,171,12,56,3,2,1))
swStaticMacBasedVlanCtrlOptionEntry.setIndexNames((0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:swStaticMacBasedVlanCtrlOptionEntry.setStatus(_A)
_SwStaticMacBasedVlanCtrlOptionMacAddr_Type=MacAddress
_SwStaticMacBasedVlanCtrlOptionMacAddr_Object=MibTableColumn
swStaticMacBasedVlanCtrlOptionMacAddr=_SwStaticMacBasedVlanCtrlOptionMacAddr_Object((1,3,6,1,4,1,171,12,56,3,2,1,1),_SwStaticMacBasedVlanCtrlOptionMacAddr_Type())
swStaticMacBasedVlanCtrlOptionMacAddr.setMaxAccess(_F)
if mibBuilder.loadTexts:swStaticMacBasedVlanCtrlOptionMacAddr.setStatus(_A)
class _SwStaticMacBasedOptionVlanID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_SwStaticMacBasedOptionVlanID_Type.__name__=_D
_SwStaticMacBasedOptionVlanID_Object=MibTableColumn
swStaticMacBasedOptionVlanID=_SwStaticMacBasedOptionVlanID_Object((1,3,6,1,4,1,171,12,56,3,2,1,2),_SwStaticMacBasedOptionVlanID_Type())
swStaticMacBasedOptionVlanID.setMaxAccess(_C)
if mibBuilder.loadTexts:swStaticMacBasedOptionVlanID.setStatus(_A)
class _SwStaticMacBasedVlanCtrlOptionType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('static',1),('mac-based-access-control',2),('ieee8021x',3),('wac',4),('jwac',5),('compound-authentication',6),('others',7),('voice-vlan',8),('surveillance-vlan',9)))
_SwStaticMacBasedVlanCtrlOptionType_Type.__name__=_D
_SwStaticMacBasedVlanCtrlOptionType_Object=MibTableColumn
swStaticMacBasedVlanCtrlOptionType=_SwStaticMacBasedVlanCtrlOptionType_Object((1,3,6,1,4,1,171,12,56,3,2,1,3),_SwStaticMacBasedVlanCtrlOptionType_Type())
swStaticMacBasedVlanCtrlOptionType.setMaxAccess(_F)
if mibBuilder.loadTexts:swStaticMacBasedVlanCtrlOptionType.setStatus(_A)
_SwStaticMacBasedVlanCtrlOptionStatus_Type=RowStatus
_SwStaticMacBasedVlanCtrlOptionStatus_Object=MibTableColumn
swStaticMacBasedVlanCtrlOptionStatus=_SwStaticMacBasedVlanCtrlOptionStatus_Object((1,3,6,1,4,1,171,12,56,3,2,1,4),_SwStaticMacBasedVlanCtrlOptionStatus_Type())
swStaticMacBasedVlanCtrlOptionStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:swStaticMacBasedVlanCtrlOptionStatus.setStatus(_A)
class _SwStaticMacBasedVlanCtrlOptionPriority_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_SwStaticMacBasedVlanCtrlOptionPriority_Type.__name__=_D
_SwStaticMacBasedVlanCtrlOptionPriority_Object=MibTableColumn
swStaticMacBasedVlanCtrlOptionPriority=_SwStaticMacBasedVlanCtrlOptionPriority_Object((1,3,6,1,4,1,171,12,56,3,2,1,5),_SwStaticMacBasedVlanCtrlOptionPriority_Type())
swStaticMacBasedVlanCtrlOptionPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:swStaticMacBasedVlanCtrlOptionPriority.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'swSMBVMIB':swSMBVMIB,'swSmbvCtrl':swSmbvCtrl,'swSmbvInfo':swSmbvInfo,'swSmbvMgmt':swSmbvMgmt,'swStaticMacBasedVlanCtrlTable':swStaticMacBasedVlanCtrlTable,'swStaticMacBasedVlanCtrlEntry':swStaticMacBasedVlanCtrlEntry,_H:swStaticMacBasedVlanCtrlMacAddr,'swStaticMacBasedVlanCtrlVlanName':swStaticMacBasedVlanCtrlVlanName,'swStaticMacBasedVlanCtrlStatus':swStaticMacBasedVlanCtrlStatus,'swStaticMacBasedVlanCtrlOptionTable':swStaticMacBasedVlanCtrlOptionTable,'swStaticMacBasedVlanCtrlOptionEntry':swStaticMacBasedVlanCtrlOptionEntry,_I:swStaticMacBasedVlanCtrlOptionMacAddr,_J:swStaticMacBasedOptionVlanID,'swStaticMacBasedVlanCtrlOptionType':swStaticMacBasedVlanCtrlOptionType,'swStaticMacBasedVlanCtrlOptionStatus':swStaticMacBasedVlanCtrlOptionStatus,'swStaticMacBasedVlanCtrlOptionPriority':swStaticMacBasedVlanCtrlOptionPriority})