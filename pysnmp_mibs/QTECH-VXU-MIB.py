_T='qtechVxuVxlState'
_S='qtechVxuVxlPortID'
_R='qtechVxuVxlPortSlotID'
_Q='qtechVxuVxlPortDeviceID'
_P='qtechVxuDeviceState'
_O='accessible-for-notify'
_N='qtechVxuVxlPortIndex'
_M='qtechVxuVxlIndex'
_L='qtechVxuVxlDeviceID'
_K='dynamic'
_J='static'
_I='qtechVxuChildDeviceID'
_H='read-write'
_G='qtechVxuDeviceID'
_F='qtechVxuLocationSlotID'
_E='qtechVxuLocationDeviceID'
_D='Integer32'
_C='QTECH-VXU-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
qtechVxuMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,126))
if mibBuilder.loadTexts:qtechVxuMIB.setRevisions(('2013-08-06 00:00',))
_QtechVxuMIBObjects_ObjectIdentity=ObjectIdentity
qtechVxuMIBObjects=_QtechVxuMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,126,1))
_QtechVxuDeviceInfo_ObjectIdentity=ObjectIdentity
qtechVxuDeviceInfo=_QtechVxuDeviceInfo_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,126,1,1))
_QtechVxuDeviceTable_Object=MibTable
qtechVxuDeviceTable=_QtechVxuDeviceTable_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,1,1))
if mibBuilder.loadTexts:qtechVxuDeviceTable.setStatus(_A)
_QtechVxuDeviceEntry_Object=MibTableRow
qtechVxuDeviceEntry=_QtechVxuDeviceEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,1,1,1))
qtechVxuDeviceEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:qtechVxuDeviceEntry.setStatus(_A)
_QtechVxuDeviceID_Type=Integer32
_QtechVxuDeviceID_Object=MibTableColumn
qtechVxuDeviceID=_QtechVxuDeviceID_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,1,1,1,1),_QtechVxuDeviceID_Type())
qtechVxuDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechVxuDeviceID.setStatus(_A)
_QtechVxuDeviceMac_Type=MacAddress
_QtechVxuDeviceMac_Object=MibTableColumn
qtechVxuDeviceMac=_QtechVxuDeviceMac_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,1,1,1,2),_QtechVxuDeviceMac_Type())
qtechVxuDeviceMac.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechVxuDeviceMac.setStatus(_A)
_QtechVxuDeviceDescr_Type=DisplayString
_QtechVxuDeviceDescr_Object=MibTableColumn
qtechVxuDeviceDescr=_QtechVxuDeviceDescr_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,1,1,1,3),_QtechVxuDeviceDescr_Type())
qtechVxuDeviceDescr.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechVxuDeviceDescr.setStatus(_A)
class _QtechVxuDeviceRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('master',1),('slaver',2)))
_QtechVxuDeviceRole_Type.__name__=_D
_QtechVxuDeviceRole_Object=MibTableColumn
qtechVxuDeviceRole=_QtechVxuDeviceRole_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,1,1,1,4),_QtechVxuDeviceRole_Type())
qtechVxuDeviceRole.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechVxuDeviceRole.setStatus(_A)
_QtechVxuVxl_ObjectIdentity=ObjectIdentity
qtechVxuVxl=_QtechVxuVxl_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,126,1,2))
_QtechVxuVxlTable_Object=MibTable
qtechVxuVxlTable=_QtechVxuVxlTable_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,2,1))
if mibBuilder.loadTexts:qtechVxuVxlTable.setStatus(_A)
_QtechVxuVxlEntry_Object=MibTableRow
qtechVxuVxlEntry=_QtechVxuVxlEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,2,1,1))
qtechVxuVxlEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:qtechVxuVxlEntry.setStatus(_A)
_QtechVxuChildDeviceID_Type=Integer32
_QtechVxuChildDeviceID_Object=MibTableColumn
qtechVxuChildDeviceID=_QtechVxuChildDeviceID_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,2,1,1,1),_QtechVxuChildDeviceID_Type())
qtechVxuChildDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechVxuChildDeviceID.setStatus(_A)
_QtechVxuFatherDeviceID_Type=Integer32
_QtechVxuFatherDeviceID_Object=MibTableColumn
qtechVxuFatherDeviceID=_QtechVxuFatherDeviceID_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,2,1,1,2),_QtechVxuFatherDeviceID_Type())
qtechVxuFatherDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechVxuFatherDeviceID.setStatus(_A)
_QtechVxuFatherVxlIndex_Type=Integer32
_QtechVxuFatherVxlIndex_Object=MibTableColumn
qtechVxuFatherVxlIndex=_QtechVxuFatherVxlIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,2,1,1,3),_QtechVxuFatherVxlIndex_Type())
qtechVxuFatherVxlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechVxuFatherVxlIndex.setStatus(_A)
class _QtechVxuVxlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_QtechVxuVxlMode_Type.__name__=_D
_QtechVxuVxlMode_Object=MibTableColumn
qtechVxuVxlMode=_QtechVxuVxlMode_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,2,1,1,4),_QtechVxuVxlMode_Type())
qtechVxuVxlMode.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechVxuVxlMode.setStatus(_A)
_QtechVxuVxlPortTable_Object=MibTable
qtechVxuVxlPortTable=_QtechVxuVxlPortTable_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,2,2))
if mibBuilder.loadTexts:qtechVxuVxlPortTable.setStatus(_A)
_QtechVxuVxlPortEntry_Object=MibTableRow
qtechVxuVxlPortEntry=_QtechVxuVxlPortEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,2,2,1))
qtechVxuVxlPortEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_N))
if mibBuilder.loadTexts:qtechVxuVxlPortEntry.setStatus(_A)
_QtechVxuVxlDeviceID_Type=Integer32
_QtechVxuVxlDeviceID_Object=MibTableColumn
qtechVxuVxlDeviceID=_QtechVxuVxlDeviceID_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,2,2,1,1),_QtechVxuVxlDeviceID_Type())
qtechVxuVxlDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechVxuVxlDeviceID.setStatus(_A)
_QtechVxuVxlIndex_Type=Integer32
_QtechVxuVxlIndex_Object=MibTableColumn
qtechVxuVxlIndex=_QtechVxuVxlIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,2,2,1,2),_QtechVxuVxlIndex_Type())
qtechVxuVxlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechVxuVxlIndex.setStatus(_A)
_QtechVxuVxlPortIndex_Type=Integer32
_QtechVxuVxlPortIndex_Object=MibTableColumn
qtechVxuVxlPortIndex=_QtechVxuVxlPortIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,2,2,1,3),_QtechVxuVxlPortIndex_Type())
qtechVxuVxlPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechVxuVxlPortIndex.setStatus(_A)
class _QtechVxuVxlPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_QtechVxuVxlPortMode_Type.__name__=_D
_QtechVxuVxlPortMode_Object=MibTableColumn
qtechVxuVxlPortMode=_QtechVxuVxlPortMode_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,2,2,1,4),_QtechVxuVxlPortMode_Type())
qtechVxuVxlPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechVxuVxlPortMode.setStatus(_A)
_QtechVxuVxlPortDeviceID_Type=Integer32
_QtechVxuVxlPortDeviceID_Object=MibTableColumn
qtechVxuVxlPortDeviceID=_QtechVxuVxlPortDeviceID_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,2,2,1,5),_QtechVxuVxlPortDeviceID_Type())
qtechVxuVxlPortDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechVxuVxlPortDeviceID.setStatus(_A)
_QtechVxuVxlPortSlotID_Type=Integer32
_QtechVxuVxlPortSlotID_Object=MibTableColumn
qtechVxuVxlPortSlotID=_QtechVxuVxlPortSlotID_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,2,2,1,6),_QtechVxuVxlPortSlotID_Type())
qtechVxuVxlPortSlotID.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechVxuVxlPortSlotID.setStatus(_A)
_QtechVxuVxlPortID_Type=Integer32
_QtechVxuVxlPortID_Object=MibTableColumn
qtechVxuVxlPortID=_QtechVxuVxlPortID_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,2,2,1,7),_QtechVxuVxlPortID_Type())
qtechVxuVxlPortID.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechVxuVxlPortID.setStatus(_A)
_QtechVxuVxlPortPeerDeviceID_Type=Integer32
_QtechVxuVxlPortPeerDeviceID_Object=MibTableColumn
qtechVxuVxlPortPeerDeviceID=_QtechVxuVxlPortPeerDeviceID_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,2,2,1,8),_QtechVxuVxlPortPeerDeviceID_Type())
qtechVxuVxlPortPeerDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechVxuVxlPortPeerDeviceID.setStatus(_A)
_QtechVxuVxlPortPeerSlotID_Type=Integer32
_QtechVxuVxlPortPeerSlotID_Object=MibTableColumn
qtechVxuVxlPortPeerSlotID=_QtechVxuVxlPortPeerSlotID_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,2,2,1,9),_QtechVxuVxlPortPeerSlotID_Type())
qtechVxuVxlPortPeerSlotID.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechVxuVxlPortPeerSlotID.setStatus(_A)
_QtechVxuVxlPortPeerID_Type=Integer32
_QtechVxuVxlPortPeerID_Object=MibTableColumn
qtechVxuVxlPortPeerID=_QtechVxuVxlPortPeerID_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,2,2,1,10),_QtechVxuVxlPortPeerID_Type())
qtechVxuVxlPortPeerID.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechVxuVxlPortPeerID.setStatus(_A)
_QtechVxuLocation_ObjectIdentity=ObjectIdentity
qtechVxuLocation=_QtechVxuLocation_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,126,1,3))
_QtechVxuLocationTable_Object=MibTable
qtechVxuLocationTable=_QtechVxuLocationTable_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,3,1))
if mibBuilder.loadTexts:qtechVxuLocationTable.setStatus(_A)
_QtechVxuLocationEntry_Object=MibTableRow
qtechVxuLocationEntry=_QtechVxuLocationEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,3,1,1))
qtechVxuLocationEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:qtechVxuLocationEntry.setStatus(_A)
_QtechVxuLocationDeviceID_Type=Integer32
_QtechVxuLocationDeviceID_Object=MibTableColumn
qtechVxuLocationDeviceID=_QtechVxuLocationDeviceID_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,3,1,1,1),_QtechVxuLocationDeviceID_Type())
qtechVxuLocationDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechVxuLocationDeviceID.setStatus(_A)
_QtechVxuLocationSlotID_Type=Integer32
_QtechVxuLocationSlotID_Object=MibTableColumn
qtechVxuLocationSlotID=_QtechVxuLocationSlotID_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,3,1,1,2),_QtechVxuLocationSlotID_Type())
qtechVxuLocationSlotID.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechVxuLocationSlotID.setStatus(_A)
class _QtechVxuLocationSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('light',1))
_QtechVxuLocationSet_Type.__name__=_D
_QtechVxuLocationSet_Object=MibTableColumn
qtechVxuLocationSet=_QtechVxuLocationSet_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,3,1,1,3),_QtechVxuLocationSet_Type())
qtechVxuLocationSet.setMaxAccess(_H)
if mibBuilder.loadTexts:qtechVxuLocationSet.setStatus(_A)
_QtechVxuVersion_Type=DisplayString
_QtechVxuVersion_Object=MibScalar
qtechVxuVersion=_QtechVxuVersion_Object((1,3,6,1,4,1,27514,1,1,10,2,126,1,4),_QtechVxuVersion_Type())
qtechVxuVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:qtechVxuVersion.setStatus(_A)
_QtechVxuMIBTraps_ObjectIdentity=ObjectIdentity
qtechVxuMIBTraps=_QtechVxuMIBTraps_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,126,2))
_QtechVxuTrapsNtfObjects_ObjectIdentity=ObjectIdentity
qtechVxuTrapsNtfObjects=_QtechVxuTrapsNtfObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,126,2,1))
class _QtechVxuDeviceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('online',1),('offline',2)))
_QtechVxuDeviceState_Type.__name__=_D
_QtechVxuDeviceState_Object=MibScalar
qtechVxuDeviceState=_QtechVxuDeviceState_Object((1,3,6,1,4,1,27514,1,1,10,2,126,2,1,1),_QtechVxuDeviceState_Type())
qtechVxuDeviceState.setMaxAccess(_O)
if mibBuilder.loadTexts:qtechVxuDeviceState.setStatus(_A)
class _QtechVxuVxlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vxl',1),('normal',2)))
_QtechVxuVxlState_Type.__name__=_D
_QtechVxuVxlState_Object=MibScalar
qtechVxuVxlState=_QtechVxuVxlState_Object((1,3,6,1,4,1,27514,1,1,10,2,126,2,1,2),_QtechVxuVxlState_Type())
qtechVxuVxlState.setMaxAccess(_O)
if mibBuilder.loadTexts:qtechVxuVxlState.setStatus(_A)
_QtechVxuTrapsNotifications_ObjectIdentity=ObjectIdentity
qtechVxuTrapsNotifications=_QtechVxuTrapsNotifications_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,126,2,2))
qtechVxuNotifyDeviceChange=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,126,2,2,1))
qtechVxuNotifyDeviceChange.setObjects(*((_C,_E),(_C,_F),(_C,_P)))
if mibBuilder.loadTexts:qtechVxuNotifyDeviceChange.setStatus(_A)
qtechVxuNotifyVxlChange=NotificationType((1,3,6,1,4,1,27514,1,1,10,2,126,2,2,2))
qtechVxuNotifyVxlChange.setObjects(*((_C,_Q),(_C,_R),(_C,_S),(_C,_T)))
if mibBuilder.loadTexts:qtechVxuNotifyVxlChange.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'qtechVxuMIB':qtechVxuMIB,'qtechVxuMIBObjects':qtechVxuMIBObjects,'qtechVxuDeviceInfo':qtechVxuDeviceInfo,'qtechVxuDeviceTable':qtechVxuDeviceTable,'qtechVxuDeviceEntry':qtechVxuDeviceEntry,_G:qtechVxuDeviceID,'qtechVxuDeviceMac':qtechVxuDeviceMac,'qtechVxuDeviceDescr':qtechVxuDeviceDescr,'qtechVxuDeviceRole':qtechVxuDeviceRole,'qtechVxuVxl':qtechVxuVxl,'qtechVxuVxlTable':qtechVxuVxlTable,'qtechVxuVxlEntry':qtechVxuVxlEntry,_I:qtechVxuChildDeviceID,'qtechVxuFatherDeviceID':qtechVxuFatherDeviceID,'qtechVxuFatherVxlIndex':qtechVxuFatherVxlIndex,'qtechVxuVxlMode':qtechVxuVxlMode,'qtechVxuVxlPortTable':qtechVxuVxlPortTable,'qtechVxuVxlPortEntry':qtechVxuVxlPortEntry,_L:qtechVxuVxlDeviceID,_M:qtechVxuVxlIndex,_N:qtechVxuVxlPortIndex,'qtechVxuVxlPortMode':qtechVxuVxlPortMode,_Q:qtechVxuVxlPortDeviceID,_R:qtechVxuVxlPortSlotID,_S:qtechVxuVxlPortID,'qtechVxuVxlPortPeerDeviceID':qtechVxuVxlPortPeerDeviceID,'qtechVxuVxlPortPeerSlotID':qtechVxuVxlPortPeerSlotID,'qtechVxuVxlPortPeerID':qtechVxuVxlPortPeerID,'qtechVxuLocation':qtechVxuLocation,'qtechVxuLocationTable':qtechVxuLocationTable,'qtechVxuLocationEntry':qtechVxuLocationEntry,_E:qtechVxuLocationDeviceID,_F:qtechVxuLocationSlotID,'qtechVxuLocationSet':qtechVxuLocationSet,'qtechVxuVersion':qtechVxuVersion,'qtechVxuMIBTraps':qtechVxuMIBTraps,'qtechVxuTrapsNtfObjects':qtechVxuTrapsNtfObjects,_P:qtechVxuDeviceState,_T:qtechVxuVxlState,'qtechVxuTrapsNotifications':qtechVxuTrapsNotifications,'qtechVxuNotifyDeviceChange':qtechVxuNotifyDeviceChange,'qtechVxuNotifyVxlChange':qtechVxuNotifyVxlChange})