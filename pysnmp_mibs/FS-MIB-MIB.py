_h='fsVSDMIBNotificationGroup'
_g='fsVSDChgDescGroup'
_f='fsVSDPortInfoMIBGroup'
_e='fsVSDDetailInfoMIBGroup'
_d='fsVSDInfoMIBGroup'
_c='fsVSDPortStatusChange'
_b='fsVSDStatusChange'
_a='fsVSDPortVSDIndex'
_Z='fsVSDPortIfIndex'
_Y='fsVSDUniqueNumber'
_X='fsVSDSerialNumber'
_W='fsVSDMacAddress'
_V='fsVSDName'
_U='fsVSDValid'
_T='fsVSDMasterSerial'
_S='fsVSDVituralSerial'
_R='fsVSDCurrentMac'
_Q='fsVSDMasterMac'
_P='fsVSDCurrentNumber'
_O='fsVSDMaxNumber'
_N='fsVSDCurrentID'
_M='fsVSDSupport'
_L='accessible-for-notify'
_K='fsVSDPortChgDesc'
_J='fsVSDChgDesc'
_I='fsVSDPortPortIdx'
_H='fsVSDPortSubslot'
_G='fsVSDPortSlot'
_F='fsVSDPortDevice'
_E='fsVSDInfoIndex'
_D='DisplayString'
_C='read-only'
_B='current'
_A='FS-MIB-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'MacAddress','PhysAddress','TextualConvention')
fsVSDMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,129))
if mibBuilder.loadTexts:fsVSDMIB.setRevisions(('2014-04-02 00:00',))
_FsVSDMIBObjects_ObjectIdentity=ObjectIdentity
fsVSDMIBObjects=_FsVSDMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,129,1))
_FsVSDSupport_Type=Integer32
_FsVSDSupport_Object=MibScalar
fsVSDSupport=_FsVSDSupport_Object((1,3,6,1,4,1,52642,1,1,10,2,129,1,1),_FsVSDSupport_Type())
fsVSDSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVSDSupport.setStatus(_B)
_FsVSDCurrentID_Type=Integer32
_FsVSDCurrentID_Object=MibScalar
fsVSDCurrentID=_FsVSDCurrentID_Object((1,3,6,1,4,1,52642,1,1,10,2,129,1,2),_FsVSDCurrentID_Type())
fsVSDCurrentID.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVSDCurrentID.setStatus(_B)
_FsVSDMaxNumber_Type=Integer32
_FsVSDMaxNumber_Object=MibScalar
fsVSDMaxNumber=_FsVSDMaxNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,129,1,3),_FsVSDMaxNumber_Type())
fsVSDMaxNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVSDMaxNumber.setStatus(_B)
_FsVSDCurrentNumber_Type=Integer32
_FsVSDCurrentNumber_Object=MibScalar
fsVSDCurrentNumber=_FsVSDCurrentNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,129,1,4),_FsVSDCurrentNumber_Type())
fsVSDCurrentNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVSDCurrentNumber.setStatus(_B)
_FsVSDMasterMac_Type=MacAddress
_FsVSDMasterMac_Object=MibScalar
fsVSDMasterMac=_FsVSDMasterMac_Object((1,3,6,1,4,1,52642,1,1,10,2,129,1,5),_FsVSDMasterMac_Type())
fsVSDMasterMac.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVSDMasterMac.setStatus(_B)
_FsVSDCurrentMac_Type=MacAddress
_FsVSDCurrentMac_Object=MibScalar
fsVSDCurrentMac=_FsVSDCurrentMac_Object((1,3,6,1,4,1,52642,1,1,10,2,129,1,6),_FsVSDCurrentMac_Type())
fsVSDCurrentMac.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVSDCurrentMac.setStatus(_B)
class _FsVSDVituralSerial_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsVSDVituralSerial_Type.__name__=_D
_FsVSDVituralSerial_Object=MibScalar
fsVSDVituralSerial=_FsVSDVituralSerial_Object((1,3,6,1,4,1,52642,1,1,10,2,129,1,7),_FsVSDVituralSerial_Type())
fsVSDVituralSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVSDVituralSerial.setStatus(_B)
class _FsVSDMasterSerial_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsVSDMasterSerial_Type.__name__=_D
_FsVSDMasterSerial_Object=MibScalar
fsVSDMasterSerial=_FsVSDMasterSerial_Object((1,3,6,1,4,1,52642,1,1,10,2,129,1,8),_FsVSDMasterSerial_Type())
fsVSDMasterSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVSDMasterSerial.setStatus(_B)
_FsVSDInfoTable_Object=MibTable
fsVSDInfoTable=_FsVSDInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,129,1,9))
if mibBuilder.loadTexts:fsVSDInfoTable.setStatus(_B)
_FsVSDInfoEntry_Object=MibTableRow
fsVSDInfoEntry=_FsVSDInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,129,1,9,1))
fsVSDInfoEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:fsVSDInfoEntry.setStatus(_B)
_FsVSDInfoIndex_Type=Integer32
_FsVSDInfoIndex_Object=MibTableColumn
fsVSDInfoIndex=_FsVSDInfoIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,129,1,9,1,1),_FsVSDInfoIndex_Type())
fsVSDInfoIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVSDInfoIndex.setStatus(_B)
_FsVSDValid_Type=Integer32
_FsVSDValid_Object=MibTableColumn
fsVSDValid=_FsVSDValid_Object((1,3,6,1,4,1,52642,1,1,10,2,129,1,9,1,2),_FsVSDValid_Type())
fsVSDValid.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVSDValid.setStatus(_B)
class _FsVSDName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsVSDName_Type.__name__=_D
_FsVSDName_Object=MibTableColumn
fsVSDName=_FsVSDName_Object((1,3,6,1,4,1,52642,1,1,10,2,129,1,9,1,3),_FsVSDName_Type())
fsVSDName.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVSDName.setStatus(_B)
_FsVSDMacAddress_Type=MacAddress
_FsVSDMacAddress_Object=MibTableColumn
fsVSDMacAddress=_FsVSDMacAddress_Object((1,3,6,1,4,1,52642,1,1,10,2,129,1,9,1,4),_FsVSDMacAddress_Type())
fsVSDMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVSDMacAddress.setStatus(_B)
class _FsVSDSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsVSDSerialNumber_Type.__name__=_D
_FsVSDSerialNumber_Object=MibTableColumn
fsVSDSerialNumber=_FsVSDSerialNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,129,1,9,1,5),_FsVSDSerialNumber_Type())
fsVSDSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVSDSerialNumber.setStatus(_B)
class _FsVSDUniqueNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsVSDUniqueNumber_Type.__name__=_D
_FsVSDUniqueNumber_Object=MibTableColumn
fsVSDUniqueNumber=_FsVSDUniqueNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,129,1,9,1,6),_FsVSDUniqueNumber_Type())
fsVSDUniqueNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVSDUniqueNumber.setStatus(_B)
_FsVSDPortInfoTable_Object=MibTable
fsVSDPortInfoTable=_FsVSDPortInfoTable_Object((1,3,6,1,4,1,52642,1,1,10,2,129,1,10))
if mibBuilder.loadTexts:fsVSDPortInfoTable.setStatus(_B)
_FsVSDPortInfoEntry_Object=MibTableRow
fsVSDPortInfoEntry=_FsVSDPortInfoEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,129,1,10,1))
fsVSDPortInfoEntry.setIndexNames((0,_A,_F),(0,_A,_G),(0,_A,_H),(0,_A,_I))
if mibBuilder.loadTexts:fsVSDPortInfoEntry.setStatus(_B)
_FsVSDPortDevice_Type=Integer32
_FsVSDPortDevice_Object=MibTableColumn
fsVSDPortDevice=_FsVSDPortDevice_Object((1,3,6,1,4,1,52642,1,1,10,2,129,1,10,1,1),_FsVSDPortDevice_Type())
fsVSDPortDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVSDPortDevice.setStatus(_B)
_FsVSDPortSlot_Type=Integer32
_FsVSDPortSlot_Object=MibTableColumn
fsVSDPortSlot=_FsVSDPortSlot_Object((1,3,6,1,4,1,52642,1,1,10,2,129,1,10,1,2),_FsVSDPortSlot_Type())
fsVSDPortSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVSDPortSlot.setStatus(_B)
_FsVSDPortSubslot_Type=Integer32
_FsVSDPortSubslot_Object=MibTableColumn
fsVSDPortSubslot=_FsVSDPortSubslot_Object((1,3,6,1,4,1,52642,1,1,10,2,129,1,10,1,3),_FsVSDPortSubslot_Type())
fsVSDPortSubslot.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVSDPortSubslot.setStatus(_B)
_FsVSDPortPortIdx_Type=Integer32
_FsVSDPortPortIdx_Object=MibTableColumn
fsVSDPortPortIdx=_FsVSDPortPortIdx_Object((1,3,6,1,4,1,52642,1,1,10,2,129,1,10,1,4),_FsVSDPortPortIdx_Type())
fsVSDPortPortIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVSDPortPortIdx.setStatus(_B)
_FsVSDPortIfIndex_Type=Integer32
_FsVSDPortIfIndex_Object=MibTableColumn
fsVSDPortIfIndex=_FsVSDPortIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,129,1,10,1,5),_FsVSDPortIfIndex_Type())
fsVSDPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVSDPortIfIndex.setStatus(_B)
_FsVSDPortVSDIndex_Type=Integer32
_FsVSDPortVSDIndex_Object=MibTableColumn
fsVSDPortVSDIndex=_FsVSDPortVSDIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,129,1,10,1,6),_FsVSDPortVSDIndex_Type())
fsVSDPortVSDIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVSDPortVSDIndex.setStatus(_B)
_FsVSDMIBTraps_ObjectIdentity=ObjectIdentity
fsVSDMIBTraps=_FsVSDMIBTraps_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,129,2))
_FsVSDChgDesc_Type=DisplayString
_FsVSDChgDesc_Object=MibScalar
fsVSDChgDesc=_FsVSDChgDesc_Object((1,3,6,1,4,1,52642,1,1,10,2,129,2,1),_FsVSDChgDesc_Type())
fsVSDChgDesc.setMaxAccess(_L)
if mibBuilder.loadTexts:fsVSDChgDesc.setStatus(_B)
_FsVSDPortChgDesc_Type=DisplayString
_FsVSDPortChgDesc_Object=MibScalar
fsVSDPortChgDesc=_FsVSDPortChgDesc_Object((1,3,6,1,4,1,52642,1,1,10,2,129,2,3),_FsVSDPortChgDesc_Type())
fsVSDPortChgDesc.setMaxAccess(_L)
if mibBuilder.loadTexts:fsVSDPortChgDesc.setStatus(_B)
_FsVSDMIBConformance_ObjectIdentity=ObjectIdentity
fsVSDMIBConformance=_FsVSDMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,129,3))
_FsVSDMIBCompliances_ObjectIdentity=ObjectIdentity
fsVSDMIBCompliances=_FsVSDMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,129,3,1))
_FsVSDMIBGroups_ObjectIdentity=ObjectIdentity
fsVSDMIBGroups=_FsVSDMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,129,3,2))
fsVSDInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,129,3,2,1))
fsVSDInfoMIBGroup.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:fsVSDInfoMIBGroup.setStatus(_B)
fsVSDDetailInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,129,3,2,2))
fsVSDDetailInfoMIBGroup.setObjects(*((_A,_E),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:fsVSDDetailInfoMIBGroup.setStatus(_B)
fsVSDPortInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,129,3,2,3))
fsVSDPortInfoMIBGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:fsVSDPortInfoMIBGroup.setStatus(_B)
fsVSDChgDescGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,129,3,2,4))
fsVSDChgDescGroup.setObjects(*((_A,_J),(_A,_K)))
if mibBuilder.loadTexts:fsVSDChgDescGroup.setStatus(_B)
fsVSDStatusChange=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,129,2,2))
fsVSDStatusChange.setObjects((_A,_J))
if mibBuilder.loadTexts:fsVSDStatusChange.setStatus(_B)
fsVSDPortStatusChange=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,129,2,4))
fsVSDPortStatusChange.setObjects((_A,_K))
if mibBuilder.loadTexts:fsVSDPortStatusChange.setStatus(_B)
fsVSDMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,52642,1,1,10,2,129,3,2,5))
fsVSDMIBNotificationGroup.setObjects(*((_A,_b),(_A,_c)))
if mibBuilder.loadTexts:fsVSDMIBNotificationGroup.setStatus(_B)
fsVSDMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,129,3,1,1))
fsVSDMIBCompliance.setObjects(*((_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:fsVSDMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'fsVSDMIB':fsVSDMIB,'fsVSDMIBObjects':fsVSDMIBObjects,_M:fsVSDSupport,_N:fsVSDCurrentID,_O:fsVSDMaxNumber,_P:fsVSDCurrentNumber,_Q:fsVSDMasterMac,_R:fsVSDCurrentMac,_S:fsVSDVituralSerial,_T:fsVSDMasterSerial,'fsVSDInfoTable':fsVSDInfoTable,'fsVSDInfoEntry':fsVSDInfoEntry,_E:fsVSDInfoIndex,_U:fsVSDValid,_V:fsVSDName,_W:fsVSDMacAddress,_X:fsVSDSerialNumber,_Y:fsVSDUniqueNumber,'fsVSDPortInfoTable':fsVSDPortInfoTable,'fsVSDPortInfoEntry':fsVSDPortInfoEntry,_F:fsVSDPortDevice,_G:fsVSDPortSlot,_H:fsVSDPortSubslot,_I:fsVSDPortPortIdx,_Z:fsVSDPortIfIndex,_a:fsVSDPortVSDIndex,'fsVSDMIBTraps':fsVSDMIBTraps,_J:fsVSDChgDesc,_b:fsVSDStatusChange,_K:fsVSDPortChgDesc,_c:fsVSDPortStatusChange,'fsVSDMIBConformance':fsVSDMIBConformance,'fsVSDMIBCompliances':fsVSDMIBCompliances,'fsVSDMIBCompliance':fsVSDMIBCompliance,'fsVSDMIBGroups':fsVSDMIBGroups,_d:fsVSDInfoMIBGroup,_e:fsVSDDetailInfoMIBGroup,_f:fsVSDPortInfoMIBGroup,_g:fsVSDChgDescGroup,_h:fsVSDMIBNotificationGroup})