_T='fsVxuVxlState'
_S='fsVxuVxlPortID'
_R='fsVxuVxlPortSlotID'
_Q='fsVxuVxlPortDeviceID'
_P='fsVxuDeviceState'
_O='accessible-for-notify'
_N='fsVxuVxlPortIndex'
_M='fsVxuVxlIndex'
_L='fsVxuVxlDeviceID'
_K='dynamic'
_J='static'
_I='fsVxuChildDeviceID'
_H='read-write'
_G='fsVxuDeviceID'
_F='fsVxuLocationSlotID'
_E='fsVxuLocationDeviceID'
_D='Integer32'
_C='FS-VXU-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
fsVxuMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,126))
if mibBuilder.loadTexts:fsVxuMIB.setRevisions(('2013-08-06 00:00',))
_FsVxuMIBObjects_ObjectIdentity=ObjectIdentity
fsVxuMIBObjects=_FsVxuMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,126,1))
_FsVxuDeviceInfo_ObjectIdentity=ObjectIdentity
fsVxuDeviceInfo=_FsVxuDeviceInfo_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,126,1,1))
_FsVxuDeviceTable_Object=MibTable
fsVxuDeviceTable=_FsVxuDeviceTable_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,1,1))
if mibBuilder.loadTexts:fsVxuDeviceTable.setStatus(_A)
_FsVxuDeviceEntry_Object=MibTableRow
fsVxuDeviceEntry=_FsVxuDeviceEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,1,1,1))
fsVxuDeviceEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:fsVxuDeviceEntry.setStatus(_A)
_FsVxuDeviceID_Type=Integer32
_FsVxuDeviceID_Object=MibTableColumn
fsVxuDeviceID=_FsVxuDeviceID_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,1,1,1,1),_FsVxuDeviceID_Type())
fsVxuDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxuDeviceID.setStatus(_A)
_FsVxuDeviceMac_Type=MacAddress
_FsVxuDeviceMac_Object=MibTableColumn
fsVxuDeviceMac=_FsVxuDeviceMac_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,1,1,1,2),_FsVxuDeviceMac_Type())
fsVxuDeviceMac.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxuDeviceMac.setStatus(_A)
_FsVxuDeviceDescr_Type=DisplayString
_FsVxuDeviceDescr_Object=MibTableColumn
fsVxuDeviceDescr=_FsVxuDeviceDescr_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,1,1,1,3),_FsVxuDeviceDescr_Type())
fsVxuDeviceDescr.setMaxAccess(_H)
if mibBuilder.loadTexts:fsVxuDeviceDescr.setStatus(_A)
class _FsVxuDeviceRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('master',1),('slaver',2)))
_FsVxuDeviceRole_Type.__name__=_D
_FsVxuDeviceRole_Object=MibTableColumn
fsVxuDeviceRole=_FsVxuDeviceRole_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,1,1,1,4),_FsVxuDeviceRole_Type())
fsVxuDeviceRole.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxuDeviceRole.setStatus(_A)
_FsVxuVxl_ObjectIdentity=ObjectIdentity
fsVxuVxl=_FsVxuVxl_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,126,1,2))
_FsVxuVxlTable_Object=MibTable
fsVxuVxlTable=_FsVxuVxlTable_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,2,1))
if mibBuilder.loadTexts:fsVxuVxlTable.setStatus(_A)
_FsVxuVxlEntry_Object=MibTableRow
fsVxuVxlEntry=_FsVxuVxlEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,2,1,1))
fsVxuVxlEntry.setIndexNames((0,_C,_I))
if mibBuilder.loadTexts:fsVxuVxlEntry.setStatus(_A)
_FsVxuChildDeviceID_Type=Integer32
_FsVxuChildDeviceID_Object=MibTableColumn
fsVxuChildDeviceID=_FsVxuChildDeviceID_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,2,1,1,1),_FsVxuChildDeviceID_Type())
fsVxuChildDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxuChildDeviceID.setStatus(_A)
_FsVxuFatherDeviceID_Type=Integer32
_FsVxuFatherDeviceID_Object=MibTableColumn
fsVxuFatherDeviceID=_FsVxuFatherDeviceID_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,2,1,1,2),_FsVxuFatherDeviceID_Type())
fsVxuFatherDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxuFatherDeviceID.setStatus(_A)
_FsVxuFatherVxlIndex_Type=Integer32
_FsVxuFatherVxlIndex_Object=MibTableColumn
fsVxuFatherVxlIndex=_FsVxuFatherVxlIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,2,1,1,3),_FsVxuFatherVxlIndex_Type())
fsVxuFatherVxlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxuFatherVxlIndex.setStatus(_A)
class _FsVxuVxlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_FsVxuVxlMode_Type.__name__=_D
_FsVxuVxlMode_Object=MibTableColumn
fsVxuVxlMode=_FsVxuVxlMode_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,2,1,1,4),_FsVxuVxlMode_Type())
fsVxuVxlMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxuVxlMode.setStatus(_A)
_FsVxuVxlPortTable_Object=MibTable
fsVxuVxlPortTable=_FsVxuVxlPortTable_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,2,2))
if mibBuilder.loadTexts:fsVxuVxlPortTable.setStatus(_A)
_FsVxuVxlPortEntry_Object=MibTableRow
fsVxuVxlPortEntry=_FsVxuVxlPortEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,2,2,1))
fsVxuVxlPortEntry.setIndexNames((0,_C,_L),(0,_C,_M),(0,_C,_N))
if mibBuilder.loadTexts:fsVxuVxlPortEntry.setStatus(_A)
_FsVxuVxlDeviceID_Type=Integer32
_FsVxuVxlDeviceID_Object=MibTableColumn
fsVxuVxlDeviceID=_FsVxuVxlDeviceID_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,2,2,1,1),_FsVxuVxlDeviceID_Type())
fsVxuVxlDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxuVxlDeviceID.setStatus(_A)
_FsVxuVxlIndex_Type=Integer32
_FsVxuVxlIndex_Object=MibTableColumn
fsVxuVxlIndex=_FsVxuVxlIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,2,2,1,2),_FsVxuVxlIndex_Type())
fsVxuVxlIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxuVxlIndex.setStatus(_A)
_FsVxuVxlPortIndex_Type=Integer32
_FsVxuVxlPortIndex_Object=MibTableColumn
fsVxuVxlPortIndex=_FsVxuVxlPortIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,2,2,1,3),_FsVxuVxlPortIndex_Type())
fsVxuVxlPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxuVxlPortIndex.setStatus(_A)
class _FsVxuVxlPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_FsVxuVxlPortMode_Type.__name__=_D
_FsVxuVxlPortMode_Object=MibTableColumn
fsVxuVxlPortMode=_FsVxuVxlPortMode_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,2,2,1,4),_FsVxuVxlPortMode_Type())
fsVxuVxlPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxuVxlPortMode.setStatus(_A)
_FsVxuVxlPortDeviceID_Type=Integer32
_FsVxuVxlPortDeviceID_Object=MibTableColumn
fsVxuVxlPortDeviceID=_FsVxuVxlPortDeviceID_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,2,2,1,5),_FsVxuVxlPortDeviceID_Type())
fsVxuVxlPortDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxuVxlPortDeviceID.setStatus(_A)
_FsVxuVxlPortSlotID_Type=Integer32
_FsVxuVxlPortSlotID_Object=MibTableColumn
fsVxuVxlPortSlotID=_FsVxuVxlPortSlotID_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,2,2,1,6),_FsVxuVxlPortSlotID_Type())
fsVxuVxlPortSlotID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxuVxlPortSlotID.setStatus(_A)
_FsVxuVxlPortID_Type=Integer32
_FsVxuVxlPortID_Object=MibTableColumn
fsVxuVxlPortID=_FsVxuVxlPortID_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,2,2,1,7),_FsVxuVxlPortID_Type())
fsVxuVxlPortID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxuVxlPortID.setStatus(_A)
_FsVxuVxlPortPeerDeviceID_Type=Integer32
_FsVxuVxlPortPeerDeviceID_Object=MibTableColumn
fsVxuVxlPortPeerDeviceID=_FsVxuVxlPortPeerDeviceID_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,2,2,1,8),_FsVxuVxlPortPeerDeviceID_Type())
fsVxuVxlPortPeerDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxuVxlPortPeerDeviceID.setStatus(_A)
_FsVxuVxlPortPeerSlotID_Type=Integer32
_FsVxuVxlPortPeerSlotID_Object=MibTableColumn
fsVxuVxlPortPeerSlotID=_FsVxuVxlPortPeerSlotID_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,2,2,1,9),_FsVxuVxlPortPeerSlotID_Type())
fsVxuVxlPortPeerSlotID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxuVxlPortPeerSlotID.setStatus(_A)
_FsVxuVxlPortPeerID_Type=Integer32
_FsVxuVxlPortPeerID_Object=MibTableColumn
fsVxuVxlPortPeerID=_FsVxuVxlPortPeerID_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,2,2,1,10),_FsVxuVxlPortPeerID_Type())
fsVxuVxlPortPeerID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxuVxlPortPeerID.setStatus(_A)
_FsVxuLocation_ObjectIdentity=ObjectIdentity
fsVxuLocation=_FsVxuLocation_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,126,1,3))
_FsVxuLocationTable_Object=MibTable
fsVxuLocationTable=_FsVxuLocationTable_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,3,1))
if mibBuilder.loadTexts:fsVxuLocationTable.setStatus(_A)
_FsVxuLocationEntry_Object=MibTableRow
fsVxuLocationEntry=_FsVxuLocationEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,3,1,1))
fsVxuLocationEntry.setIndexNames((0,_C,_E),(0,_C,_F))
if mibBuilder.loadTexts:fsVxuLocationEntry.setStatus(_A)
_FsVxuLocationDeviceID_Type=Integer32
_FsVxuLocationDeviceID_Object=MibTableColumn
fsVxuLocationDeviceID=_FsVxuLocationDeviceID_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,3,1,1,1),_FsVxuLocationDeviceID_Type())
fsVxuLocationDeviceID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxuLocationDeviceID.setStatus(_A)
_FsVxuLocationSlotID_Type=Integer32
_FsVxuLocationSlotID_Object=MibTableColumn
fsVxuLocationSlotID=_FsVxuLocationSlotID_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,3,1,1,2),_FsVxuLocationSlotID_Type())
fsVxuLocationSlotID.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxuLocationSlotID.setStatus(_A)
class _FsVxuLocationSet_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('light',1))
_FsVxuLocationSet_Type.__name__=_D
_FsVxuLocationSet_Object=MibTableColumn
fsVxuLocationSet=_FsVxuLocationSet_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,3,1,1,3),_FsVxuLocationSet_Type())
fsVxuLocationSet.setMaxAccess(_H)
if mibBuilder.loadTexts:fsVxuLocationSet.setStatus(_A)
_FsVxuVersion_Type=DisplayString
_FsVxuVersion_Object=MibScalar
fsVxuVersion=_FsVxuVersion_Object((1,3,6,1,4,1,52642,1,1,10,2,126,1,4),_FsVxuVersion_Type())
fsVxuVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:fsVxuVersion.setStatus(_A)
_FsVxuMIBTraps_ObjectIdentity=ObjectIdentity
fsVxuMIBTraps=_FsVxuMIBTraps_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,126,2))
_FsVxuTrapsNtfObjects_ObjectIdentity=ObjectIdentity
fsVxuTrapsNtfObjects=_FsVxuTrapsNtfObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,126,2,1))
class _FsVxuDeviceState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('online',1),('offline',2)))
_FsVxuDeviceState_Type.__name__=_D
_FsVxuDeviceState_Object=MibScalar
fsVxuDeviceState=_FsVxuDeviceState_Object((1,3,6,1,4,1,52642,1,1,10,2,126,2,1,1),_FsVxuDeviceState_Type())
fsVxuDeviceState.setMaxAccess(_O)
if mibBuilder.loadTexts:fsVxuDeviceState.setStatus(_A)
class _FsVxuVxlState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vxl',1),('normal',2)))
_FsVxuVxlState_Type.__name__=_D
_FsVxuVxlState_Object=MibScalar
fsVxuVxlState=_FsVxuVxlState_Object((1,3,6,1,4,1,52642,1,1,10,2,126,2,1,2),_FsVxuVxlState_Type())
fsVxuVxlState.setMaxAccess(_O)
if mibBuilder.loadTexts:fsVxuVxlState.setStatus(_A)
_FsVxuTrapsNotifications_ObjectIdentity=ObjectIdentity
fsVxuTrapsNotifications=_FsVxuTrapsNotifications_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,126,2,2))
fsVxuNotifyDeviceChange=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,126,2,2,1))
fsVxuNotifyDeviceChange.setObjects(*((_C,_E),(_C,_F),(_C,_P)))
if mibBuilder.loadTexts:fsVxuNotifyDeviceChange.setStatus(_A)
fsVxuNotifyVxlChange=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,126,2,2,2))
fsVxuNotifyVxlChange.setObjects(*((_C,_Q),(_C,_R),(_C,_S),(_C,_T)))
if mibBuilder.loadTexts:fsVxuNotifyVxlChange.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'fsVxuMIB':fsVxuMIB,'fsVxuMIBObjects':fsVxuMIBObjects,'fsVxuDeviceInfo':fsVxuDeviceInfo,'fsVxuDeviceTable':fsVxuDeviceTable,'fsVxuDeviceEntry':fsVxuDeviceEntry,_G:fsVxuDeviceID,'fsVxuDeviceMac':fsVxuDeviceMac,'fsVxuDeviceDescr':fsVxuDeviceDescr,'fsVxuDeviceRole':fsVxuDeviceRole,'fsVxuVxl':fsVxuVxl,'fsVxuVxlTable':fsVxuVxlTable,'fsVxuVxlEntry':fsVxuVxlEntry,_I:fsVxuChildDeviceID,'fsVxuFatherDeviceID':fsVxuFatherDeviceID,'fsVxuFatherVxlIndex':fsVxuFatherVxlIndex,'fsVxuVxlMode':fsVxuVxlMode,'fsVxuVxlPortTable':fsVxuVxlPortTable,'fsVxuVxlPortEntry':fsVxuVxlPortEntry,_L:fsVxuVxlDeviceID,_M:fsVxuVxlIndex,_N:fsVxuVxlPortIndex,'fsVxuVxlPortMode':fsVxuVxlPortMode,_Q:fsVxuVxlPortDeviceID,_R:fsVxuVxlPortSlotID,_S:fsVxuVxlPortID,'fsVxuVxlPortPeerDeviceID':fsVxuVxlPortPeerDeviceID,'fsVxuVxlPortPeerSlotID':fsVxuVxlPortPeerSlotID,'fsVxuVxlPortPeerID':fsVxuVxlPortPeerID,'fsVxuLocation':fsVxuLocation,'fsVxuLocationTable':fsVxuLocationTable,'fsVxuLocationEntry':fsVxuLocationEntry,_E:fsVxuLocationDeviceID,_F:fsVxuLocationSlotID,'fsVxuLocationSet':fsVxuLocationSet,'fsVxuVersion':fsVxuVersion,'fsVxuMIBTraps':fsVxuMIBTraps,'fsVxuTrapsNtfObjects':fsVxuTrapsNtfObjects,_P:fsVxuDeviceState,_T:fsVxuVxlState,'fsVxuTrapsNotifications':fsVxuTrapsNotifications,'fsVxuNotifyDeviceChange':fsVxuNotifyDeviceChange,'fsVxuNotifyVxlChange':fsVxuNotifyVxlChange})