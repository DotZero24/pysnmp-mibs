_X='fsAuthenKeyChainMIBGroup'
_W='fsAuthenKeyEntryStauts'
_V='fsAuthenSendKeyState'
_U='fsAuthenReceiveKeyState'
_T='fsAuthenKeySendDuration'
_S='fsAuthenKeySendEndTime'
_R='fsAuthenKeySendTimeMode'
_Q='fsAuthenKeySendFSTime'
_P='fsAuthenKeyReceiveDuration'
_O='fsAuthenKeyReceiveEndTime'
_N='fsAuthenKeyReceiveTimeMode'
_M='fsAuthenKeyReceiveFSTime'
_L='fsKeyString'
_K='fsAuthenKeyChainEntryStatus'
_J='invalid'
_I='fsAuthenKeyNumber'
_H='fsKeyChainName'
_G='fsAuthenKeyChainName'
_F='DisplayString'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='FS-AUTHEN-KEY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ConfigStatus,=mibBuilder.importSymbols('FS-TC','ConfigStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'PhysAddress','RowStatus','TextualConvention')
fsAuthenKeyMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,24))
if mibBuilder.loadTexts:fsAuthenKeyMIB.setRevisions(('2002-03-20 00:00',))
class FSKeyTimeMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('infinite',1),('duration',2),('end-time',3)))
_FsAuthenKeyMIBObjects_ObjectIdentity=ObjectIdentity
fsAuthenKeyMIBObjects=_FsAuthenKeyMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,24,1))
_FsAuthenKeyChainTable_Object=MibTable
fsAuthenKeyChainTable=_FsAuthenKeyChainTable_Object((1,3,6,1,4,1,52642,1,1,10,2,24,1,1))
if mibBuilder.loadTexts:fsAuthenKeyChainTable.setStatus(_A)
_FsAuthenKeyChainEntry_Object=MibTableRow
fsAuthenKeyChainEntry=_FsAuthenKeyChainEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,24,1,1,1))
fsAuthenKeyChainEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:fsAuthenKeyChainEntry.setStatus(_A)
class _FsAuthenKeyChainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsAuthenKeyChainName_Type.__name__=_F
_FsAuthenKeyChainName_Object=MibTableColumn
fsAuthenKeyChainName=_FsAuthenKeyChainName_Object((1,3,6,1,4,1,52642,1,1,10,2,24,1,1,1,1),_FsAuthenKeyChainName_Type())
fsAuthenKeyChainName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAuthenKeyChainName.setStatus(_A)
_FsAuthenKeyChainEntryStatus_Type=ConfigStatus
_FsAuthenKeyChainEntryStatus_Object=MibTableColumn
fsAuthenKeyChainEntryStatus=_FsAuthenKeyChainEntryStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,24,1,1,1,2),_FsAuthenKeyChainEntryStatus_Type())
fsAuthenKeyChainEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:fsAuthenKeyChainEntryStatus.setStatus(_A)
_FsAuthenKeyTable_Object=MibTable
fsAuthenKeyTable=_FsAuthenKeyTable_Object((1,3,6,1,4,1,52642,1,1,10,2,24,1,2))
if mibBuilder.loadTexts:fsAuthenKeyTable.setStatus(_A)
_FsAuthenKeyEntry_Object=MibTableRow
fsAuthenKeyEntry=_FsAuthenKeyEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,24,1,2,1))
fsAuthenKeyEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:fsAuthenKeyEntry.setStatus(_A)
class _FsKeyChainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_FsKeyChainName_Type.__name__=_F
_FsKeyChainName_Object=MibTableColumn
fsKeyChainName=_FsKeyChainName_Object((1,3,6,1,4,1,52642,1,1,10,2,24,1,2,1,1),_FsKeyChainName_Type())
fsKeyChainName.setMaxAccess(_D)
if mibBuilder.loadTexts:fsKeyChainName.setStatus(_A)
class _FsAuthenKeyNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_FsAuthenKeyNumber_Type.__name__=_E
_FsAuthenKeyNumber_Object=MibTableColumn
fsAuthenKeyNumber=_FsAuthenKeyNumber_Object((1,3,6,1,4,1,52642,1,1,10,2,24,1,2,1,2),_FsAuthenKeyNumber_Type())
fsAuthenKeyNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAuthenKeyNumber.setStatus(_A)
class _FsKeyString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_FsKeyString_Type.__name__=_F
_FsKeyString_Object=MibTableColumn
fsKeyString=_FsKeyString_Object((1,3,6,1,4,1,52642,1,1,10,2,24,1,2,1,3),_FsKeyString_Type())
fsKeyString.setMaxAccess(_D)
if mibBuilder.loadTexts:fsKeyString.setStatus(_A)
_FsAuthenKeyReceiveFSTime_Type=DateAndTime
_FsAuthenKeyReceiveFSTime_Object=MibTableColumn
fsAuthenKeyReceiveFSTime=_FsAuthenKeyReceiveFSTime_Object((1,3,6,1,4,1,52642,1,1,10,2,24,1,2,1,4),_FsAuthenKeyReceiveFSTime_Type())
fsAuthenKeyReceiveFSTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsAuthenKeyReceiveFSTime.setStatus(_A)
_FsAuthenKeyReceiveTimeMode_Type=FSKeyTimeMode
_FsAuthenKeyReceiveTimeMode_Object=MibTableColumn
fsAuthenKeyReceiveTimeMode=_FsAuthenKeyReceiveTimeMode_Object((1,3,6,1,4,1,52642,1,1,10,2,24,1,2,1,5),_FsAuthenKeyReceiveTimeMode_Type())
fsAuthenKeyReceiveTimeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsAuthenKeyReceiveTimeMode.setStatus(_A)
_FsAuthenKeyReceiveEndTime_Type=DateAndTime
_FsAuthenKeyReceiveEndTime_Object=MibTableColumn
fsAuthenKeyReceiveEndTime=_FsAuthenKeyReceiveEndTime_Object((1,3,6,1,4,1,52642,1,1,10,2,24,1,2,1,6),_FsAuthenKeyReceiveEndTime_Type())
fsAuthenKeyReceiveEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsAuthenKeyReceiveEndTime.setStatus(_A)
_FsAuthenKeyReceiveDuration_Type=Unsigned32
_FsAuthenKeyReceiveDuration_Object=MibTableColumn
fsAuthenKeyReceiveDuration=_FsAuthenKeyReceiveDuration_Object((1,3,6,1,4,1,52642,1,1,10,2,24,1,2,1,7),_FsAuthenKeyReceiveDuration_Type())
fsAuthenKeyReceiveDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:fsAuthenKeyReceiveDuration.setStatus(_A)
_FsAuthenKeySendFSTime_Type=DateAndTime
_FsAuthenKeySendFSTime_Object=MibTableColumn
fsAuthenKeySendFSTime=_FsAuthenKeySendFSTime_Object((1,3,6,1,4,1,52642,1,1,10,2,24,1,2,1,8),_FsAuthenKeySendFSTime_Type())
fsAuthenKeySendFSTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsAuthenKeySendFSTime.setStatus(_A)
_FsAuthenKeySendTimeMode_Type=FSKeyTimeMode
_FsAuthenKeySendTimeMode_Object=MibTableColumn
fsAuthenKeySendTimeMode=_FsAuthenKeySendTimeMode_Object((1,3,6,1,4,1,52642,1,1,10,2,24,1,2,1,9),_FsAuthenKeySendTimeMode_Type())
fsAuthenKeySendTimeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:fsAuthenKeySendTimeMode.setStatus(_A)
_FsAuthenKeySendEndTime_Type=DateAndTime
_FsAuthenKeySendEndTime_Object=MibTableColumn
fsAuthenKeySendEndTime=_FsAuthenKeySendEndTime_Object((1,3,6,1,4,1,52642,1,1,10,2,24,1,2,1,10),_FsAuthenKeySendEndTime_Type())
fsAuthenKeySendEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:fsAuthenKeySendEndTime.setStatus(_A)
_FsAuthenKeySendDuration_Type=Unsigned32
_FsAuthenKeySendDuration_Object=MibTableColumn
fsAuthenKeySendDuration=_FsAuthenKeySendDuration_Object((1,3,6,1,4,1,52642,1,1,10,2,24,1,2,1,11),_FsAuthenKeySendDuration_Type())
fsAuthenKeySendDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:fsAuthenKeySendDuration.setStatus(_A)
class _FsAuthenReceiveKeyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_J,2)))
_FsAuthenReceiveKeyState_Type.__name__=_E
_FsAuthenReceiveKeyState_Object=MibTableColumn
fsAuthenReceiveKeyState=_FsAuthenReceiveKeyState_Object((1,3,6,1,4,1,52642,1,1,10,2,24,1,2,1,12),_FsAuthenReceiveKeyState_Type())
fsAuthenReceiveKeyState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAuthenReceiveKeyState.setStatus(_A)
class _FsAuthenSendKeyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_J,2)))
_FsAuthenSendKeyState_Type.__name__=_E
_FsAuthenSendKeyState_Object=MibTableColumn
fsAuthenSendKeyState=_FsAuthenSendKeyState_Object((1,3,6,1,4,1,52642,1,1,10,2,24,1,2,1,13),_FsAuthenSendKeyState_Type())
fsAuthenSendKeyState.setMaxAccess(_D)
if mibBuilder.loadTexts:fsAuthenSendKeyState.setStatus(_A)
_FsAuthenKeyEntryStauts_Type=RowStatus
_FsAuthenKeyEntryStauts_Object=MibTableColumn
fsAuthenKeyEntryStauts=_FsAuthenKeyEntryStauts_Object((1,3,6,1,4,1,52642,1,1,10,2,24,1,2,1,14),_FsAuthenKeyEntryStauts_Type())
fsAuthenKeyEntryStauts.setMaxAccess(_C)
if mibBuilder.loadTexts:fsAuthenKeyEntryStauts.setStatus(_A)
_FsAuthenKeyChainMIBConformance_ObjectIdentity=ObjectIdentity
fsAuthenKeyChainMIBConformance=_FsAuthenKeyChainMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,24,2))
_FsAuthenKeyChainMIBCompliances_ObjectIdentity=ObjectIdentity
fsAuthenKeyChainMIBCompliances=_FsAuthenKeyChainMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,24,2,1))
_FsAuthenKeyChainMIBGroups_ObjectIdentity=ObjectIdentity
fsAuthenKeyChainMIBGroups=_FsAuthenKeyChainMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,24,2,2))
fsAuthenKeyChainMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,24,2,2,1))
fsAuthenKeyChainMIBGroup.setObjects(*((_B,_G),(_B,_K),(_B,_H),(_B,_I),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:fsAuthenKeyChainMIBGroup.setStatus(_A)
fsAuthenKeyChainMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,24,2,1,1))
fsAuthenKeyChainMIBCompliance.setObjects((_B,_X))
if mibBuilder.loadTexts:fsAuthenKeyChainMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'FSKeyTimeMode':FSKeyTimeMode,'fsAuthenKeyMIB':fsAuthenKeyMIB,'fsAuthenKeyMIBObjects':fsAuthenKeyMIBObjects,'fsAuthenKeyChainTable':fsAuthenKeyChainTable,'fsAuthenKeyChainEntry':fsAuthenKeyChainEntry,_G:fsAuthenKeyChainName,_K:fsAuthenKeyChainEntryStatus,'fsAuthenKeyTable':fsAuthenKeyTable,'fsAuthenKeyEntry':fsAuthenKeyEntry,_H:fsKeyChainName,_I:fsAuthenKeyNumber,_L:fsKeyString,_M:fsAuthenKeyReceiveFSTime,_N:fsAuthenKeyReceiveTimeMode,_O:fsAuthenKeyReceiveEndTime,_P:fsAuthenKeyReceiveDuration,_Q:fsAuthenKeySendFSTime,_R:fsAuthenKeySendTimeMode,_S:fsAuthenKeySendEndTime,_T:fsAuthenKeySendDuration,_U:fsAuthenReceiveKeyState,_V:fsAuthenSendKeyState,_W:fsAuthenKeyEntryStauts,'fsAuthenKeyChainMIBConformance':fsAuthenKeyChainMIBConformance,'fsAuthenKeyChainMIBCompliances':fsAuthenKeyChainMIBCompliances,'fsAuthenKeyChainMIBCompliance':fsAuthenKeyChainMIBCompliance,'fsAuthenKeyChainMIBGroups':fsAuthenKeyChainMIBGroups,_X:fsAuthenKeyChainMIBGroup})