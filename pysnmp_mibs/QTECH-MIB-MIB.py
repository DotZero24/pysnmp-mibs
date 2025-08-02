_h='qtechVSDMIBNotificationGroup'
_g='qtechVSDChgDescGroup'
_f='qtechVSDPortInfoMIBGroup'
_e='qtechVSDDetailInfoMIBGroup'
_d='qtechVSDInfoMIBGroup'
_c='qtechVSDPortStatusChange'
_b='qtechVSDStatusChange'
_a='qtechVSDPortVSDIndex'
_Z='qtechVSDPortIfIndex'
_Y='qtechVSDUniqueNumber'
_X='qtechVSDSerialNumber'
_W='qtechVSDMacAddress'
_V='qtechVSDName'
_U='qtechVSDValid'
_T='qtechVSDMasterSerial'
_S='qtechVSDVituralSerial'
_R='qtechVSDCurrentMac'
_Q='qtechVSDMasterMac'
_P='qtechVSDCurrentNumber'
_O='qtechVSDMaxNumber'
_N='qtechVSDCurrentID'
_M='qtechVSDSupport'
_L='accessible-for-notify'
_K='qtechVSDPortChgDesc'
_J='qtechVSDChgDesc'
_I='qtechVSDPortPortIdx'
_H='qtechVSDPortSubslot'
_G='qtechVSDPortSlot'
_F='qtechVSDPortDevice'
_E='qtechVSDInfoIndex'
_D='DisplayString'
_C='read-only'
_B='current'
_A='QTECH-MIB-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'MacAddress','PhysAddress','TextualConvention')
qtechVSDMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,129))
if mibBuilder.loadTexts:qtechVSDMIB.setRevisions(('2014-04-02 00:00',))
_QtechVSDMIBObjects_ObjectIdentity=ObjectIdentity
qtechVSDMIBObjects=_QtechVSDMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,129,1))
_QtechVSDSupport_Type=Integer32
_QtechVSDSupport_Object=MibScalar
qtechVSDSupport=_QtechVSDSupport_Object((1,3,6,1,4,1,27514,1,1,10,2,129,1,1),_QtechVSDSupport_Type())
qtechVSDSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVSDSupport.setStatus(_B)
_QtechVSDCurrentID_Type=Integer32
_QtechVSDCurrentID_Object=MibScalar
qtechVSDCurrentID=_QtechVSDCurrentID_Object((1,3,6,1,4,1,27514,1,1,10,2,129,1,2),_QtechVSDCurrentID_Type())
qtechVSDCurrentID.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVSDCurrentID.setStatus(_B)
_QtechVSDMaxNumber_Type=Integer32
_QtechVSDMaxNumber_Object=MibScalar
qtechVSDMaxNumber=_QtechVSDMaxNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,129,1,3),_QtechVSDMaxNumber_Type())
qtechVSDMaxNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVSDMaxNumber.setStatus(_B)
_QtechVSDCurrentNumber_Type=Integer32
_QtechVSDCurrentNumber_Object=MibScalar
qtechVSDCurrentNumber=_QtechVSDCurrentNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,129,1,4),_QtechVSDCurrentNumber_Type())
qtechVSDCurrentNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVSDCurrentNumber.setStatus(_B)
_QtechVSDMasterMac_Type=MacAddress
_QtechVSDMasterMac_Object=MibScalar
qtechVSDMasterMac=_QtechVSDMasterMac_Object((1,3,6,1,4,1,27514,1,1,10,2,129,1,5),_QtechVSDMasterMac_Type())
qtechVSDMasterMac.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVSDMasterMac.setStatus(_B)
_QtechVSDCurrentMac_Type=MacAddress
_QtechVSDCurrentMac_Object=MibScalar
qtechVSDCurrentMac=_QtechVSDCurrentMac_Object((1,3,6,1,4,1,27514,1,1,10,2,129,1,6),_QtechVSDCurrentMac_Type())
qtechVSDCurrentMac.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVSDCurrentMac.setStatus(_B)
class _QtechVSDVituralSerial_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechVSDVituralSerial_Type.__name__=_D
_QtechVSDVituralSerial_Object=MibScalar
qtechVSDVituralSerial=_QtechVSDVituralSerial_Object((1,3,6,1,4,1,27514,1,1,10,2,129,1,7),_QtechVSDVituralSerial_Type())
qtechVSDVituralSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVSDVituralSerial.setStatus(_B)
class _QtechVSDMasterSerial_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechVSDMasterSerial_Type.__name__=_D
_QtechVSDMasterSerial_Object=MibScalar
qtechVSDMasterSerial=_QtechVSDMasterSerial_Object((1,3,6,1,4,1,27514,1,1,10,2,129,1,8),_QtechVSDMasterSerial_Type())
qtechVSDMasterSerial.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVSDMasterSerial.setStatus(_B)
_QtechVSDInfoTable_Object=MibTable
qtechVSDInfoTable=_QtechVSDInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,129,1,9))
if mibBuilder.loadTexts:qtechVSDInfoTable.setStatus(_B)
_QtechVSDInfoEntry_Object=MibTableRow
qtechVSDInfoEntry=_QtechVSDInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,129,1,9,1))
qtechVSDInfoEntry.setIndexNames((0,_A,_E))
if mibBuilder.loadTexts:qtechVSDInfoEntry.setStatus(_B)
_QtechVSDInfoIndex_Type=Integer32
_QtechVSDInfoIndex_Object=MibTableColumn
qtechVSDInfoIndex=_QtechVSDInfoIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,129,1,9,1,1),_QtechVSDInfoIndex_Type())
qtechVSDInfoIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVSDInfoIndex.setStatus(_B)
_QtechVSDValid_Type=Integer32
_QtechVSDValid_Object=MibTableColumn
qtechVSDValid=_QtechVSDValid_Object((1,3,6,1,4,1,27514,1,1,10,2,129,1,9,1,2),_QtechVSDValid_Type())
qtechVSDValid.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVSDValid.setStatus(_B)
class _QtechVSDName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_QtechVSDName_Type.__name__=_D
_QtechVSDName_Object=MibTableColumn
qtechVSDName=_QtechVSDName_Object((1,3,6,1,4,1,27514,1,1,10,2,129,1,9,1,3),_QtechVSDName_Type())
qtechVSDName.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVSDName.setStatus(_B)
_QtechVSDMacAddress_Type=MacAddress
_QtechVSDMacAddress_Object=MibTableColumn
qtechVSDMacAddress=_QtechVSDMacAddress_Object((1,3,6,1,4,1,27514,1,1,10,2,129,1,9,1,4),_QtechVSDMacAddress_Type())
qtechVSDMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVSDMacAddress.setStatus(_B)
class _QtechVSDSerialNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechVSDSerialNumber_Type.__name__=_D
_QtechVSDSerialNumber_Object=MibTableColumn
qtechVSDSerialNumber=_QtechVSDSerialNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,129,1,9,1,5),_QtechVSDSerialNumber_Type())
qtechVSDSerialNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVSDSerialNumber.setStatus(_B)
class _QtechVSDUniqueNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechVSDUniqueNumber_Type.__name__=_D
_QtechVSDUniqueNumber_Object=MibTableColumn
qtechVSDUniqueNumber=_QtechVSDUniqueNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,129,1,9,1,6),_QtechVSDUniqueNumber_Type())
qtechVSDUniqueNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVSDUniqueNumber.setStatus(_B)
_QtechVSDPortInfoTable_Object=MibTable
qtechVSDPortInfoTable=_QtechVSDPortInfoTable_Object((1,3,6,1,4,1,27514,1,1,10,2,129,1,10))
if mibBuilder.loadTexts:qtechVSDPortInfoTable.setStatus(_B)
_QtechVSDPortInfoEntry_Object=MibTableRow
qtechVSDPortInfoEntry=_QtechVSDPortInfoEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,129,1,10,1))
qtechVSDPortInfoEntry.setIndexNames((0,_A,_F),(0,_A,_G),(0,_A,_H),(0,_A,_I))
if mibBuilder.loadTexts:qtechVSDPortInfoEntry.setStatus(_B)
_QtechVSDPortDevice_Type=Integer32
_QtechVSDPortDevice_Object=MibTableColumn
qtechVSDPortDevice=_QtechVSDPortDevice_Object((1,3,6,1,4,1,27514,1,1,10,2,129,1,10,1,1),_QtechVSDPortDevice_Type())
qtechVSDPortDevice.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVSDPortDevice.setStatus(_B)
_QtechVSDPortSlot_Type=Integer32
_QtechVSDPortSlot_Object=MibTableColumn
qtechVSDPortSlot=_QtechVSDPortSlot_Object((1,3,6,1,4,1,27514,1,1,10,2,129,1,10,1,2),_QtechVSDPortSlot_Type())
qtechVSDPortSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVSDPortSlot.setStatus(_B)
_QtechVSDPortSubslot_Type=Integer32
_QtechVSDPortSubslot_Object=MibTableColumn
qtechVSDPortSubslot=_QtechVSDPortSubslot_Object((1,3,6,1,4,1,27514,1,1,10,2,129,1,10,1,3),_QtechVSDPortSubslot_Type())
qtechVSDPortSubslot.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVSDPortSubslot.setStatus(_B)
_QtechVSDPortPortIdx_Type=Integer32
_QtechVSDPortPortIdx_Object=MibTableColumn
qtechVSDPortPortIdx=_QtechVSDPortPortIdx_Object((1,3,6,1,4,1,27514,1,1,10,2,129,1,10,1,4),_QtechVSDPortPortIdx_Type())
qtechVSDPortPortIdx.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVSDPortPortIdx.setStatus(_B)
_QtechVSDPortIfIndex_Type=Integer32
_QtechVSDPortIfIndex_Object=MibTableColumn
qtechVSDPortIfIndex=_QtechVSDPortIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,129,1,10,1,5),_QtechVSDPortIfIndex_Type())
qtechVSDPortIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVSDPortIfIndex.setStatus(_B)
_QtechVSDPortVSDIndex_Type=Integer32
_QtechVSDPortVSDIndex_Object=MibTableColumn
qtechVSDPortVSDIndex=_QtechVSDPortVSDIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,129,1,10,1,6),_QtechVSDPortVSDIndex_Type())
qtechVSDPortVSDIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechVSDPortVSDIndex.setStatus(_B)
_QtechVSDMIBTraps_ObjectIdentity=ObjectIdentity
qtechVSDMIBTraps=_QtechVSDMIBTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,129,2))
_QtechVSDChgDesc_Type=DisplayString
_QtechVSDChgDesc_Object=MibScalar
qtechVSDChgDesc=_QtechVSDChgDesc_Object((1,3,6,1,4,1,27514,1,1,10,2,129,2,1),_QtechVSDChgDesc_Type())
qtechVSDChgDesc.setMaxAccess(_L)
if mibBuilder.loadTexts:qtechVSDChgDesc.setStatus(_B)
_QtechVSDPortChgDesc_Type=DisplayString
_QtechVSDPortChgDesc_Object=MibScalar
qtechVSDPortChgDesc=_QtechVSDPortChgDesc_Object((1,3,6,1,4,1,27514,1,1,10,2,129,2,3),_QtechVSDPortChgDesc_Type())
qtechVSDPortChgDesc.setMaxAccess(_L)
if mibBuilder.loadTexts:qtechVSDPortChgDesc.setStatus(_B)
_QtechVSDMIBConformance_ObjectIdentity=ObjectIdentity
qtechVSDMIBConformance=_QtechVSDMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,129,3))
_QtechVSDMIBCompliances_ObjectIdentity=ObjectIdentity
qtechVSDMIBCompliances=_QtechVSDMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,129,3,1))
_QtechVSDMIBGroups_ObjectIdentity=ObjectIdentity
qtechVSDMIBGroups=_QtechVSDMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,129,3,2))
qtechVSDInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,129,3,2,1))
qtechVSDInfoMIBGroup.setObjects(*((_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T)))
if mibBuilder.loadTexts:qtechVSDInfoMIBGroup.setStatus(_B)
qtechVSDDetailInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,129,3,2,2))
qtechVSDDetailInfoMIBGroup.setObjects(*((_A,_E),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y)))
if mibBuilder.loadTexts:qtechVSDDetailInfoMIBGroup.setStatus(_B)
qtechVSDPortInfoMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,129,3,2,3))
qtechVSDPortInfoMIBGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_Z),(_A,_a)))
if mibBuilder.loadTexts:qtechVSDPortInfoMIBGroup.setStatus(_B)
qtechVSDChgDescGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,129,3,2,4))
qtechVSDChgDescGroup.setObjects(*((_A,_J),(_A,_K)))
if mibBuilder.loadTexts:qtechVSDChgDescGroup.setStatus(_B)
qtechVSDStatusChange=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,129,2,2))
qtechVSDStatusChange.setObjects((_A,_J))
if mibBuilder.loadTexts:qtechVSDStatusChange.setStatus(_B)
qtechVSDPortStatusChange=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,129,2,4))
qtechVSDPortStatusChange.setObjects((_A,_K))
if mibBuilder.loadTexts:qtechVSDPortStatusChange.setStatus(_B)
qtechVSDMIBNotificationGroup=NotificationGroup((1,3,6,1,4,1,27514,1,1,10,2,129,3,2,5))
qtechVSDMIBNotificationGroup.setObjects(*((_A,_b),(_A,_c)))
if mibBuilder.loadTexts:qtechVSDMIBNotificationGroup.setStatus(_B)
qtechVSDMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,129,3,1,1))
qtechVSDMIBCompliance.setObjects(*((_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h)))
if mibBuilder.loadTexts:qtechVSDMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'qtechVSDMIB':qtechVSDMIB,'qtechVSDMIBObjects':qtechVSDMIBObjects,_M:qtechVSDSupport,_N:qtechVSDCurrentID,_O:qtechVSDMaxNumber,_P:qtechVSDCurrentNumber,_Q:qtechVSDMasterMac,_R:qtechVSDCurrentMac,_S:qtechVSDVituralSerial,_T:qtechVSDMasterSerial,'qtechVSDInfoTable':qtechVSDInfoTable,'qtechVSDInfoEntry':qtechVSDInfoEntry,_E:qtechVSDInfoIndex,_U:qtechVSDValid,_V:qtechVSDName,_W:qtechVSDMacAddress,_X:qtechVSDSerialNumber,_Y:qtechVSDUniqueNumber,'qtechVSDPortInfoTable':qtechVSDPortInfoTable,'qtechVSDPortInfoEntry':qtechVSDPortInfoEntry,_F:qtechVSDPortDevice,_G:qtechVSDPortSlot,_H:qtechVSDPortSubslot,_I:qtechVSDPortPortIdx,_Z:qtechVSDPortIfIndex,_a:qtechVSDPortVSDIndex,'qtechVSDMIBTraps':qtechVSDMIBTraps,_J:qtechVSDChgDesc,_b:qtechVSDStatusChange,_K:qtechVSDPortChgDesc,_c:qtechVSDPortStatusChange,'qtechVSDMIBConformance':qtechVSDMIBConformance,'qtechVSDMIBCompliances':qtechVSDMIBCompliances,'qtechVSDMIBCompliance':qtechVSDMIBCompliance,'qtechVSDMIBGroups':qtechVSDMIBGroups,_d:qtechVSDInfoMIBGroup,_e:qtechVSDDetailInfoMIBGroup,_f:qtechVSDPortInfoMIBGroup,_g:qtechVSDChgDescGroup,_h:qtechVSDMIBNotificationGroup})