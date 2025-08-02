_X='qtechAuthenKeyChainMIBGroup'
_W='qtechAuthenKeyEntryStauts'
_V='qtechAuthenSendKeyState'
_U='qtechAuthenReceiveKeyState'
_T='qtechAuthenKeySendDuration'
_S='qtechAuthenKeySendEndTime'
_R='qtechAuthenKeySendTimeMode'
_Q='qtechAuthenKeySendQtechTime'
_P='qtechAuthenKeyReceiveDuration'
_O='qtechAuthenKeyReceiveEndTime'
_N='qtechAuthenKeyReceiveTimeMode'
_M='qtechAuthenKeyReceiveQtechTime'
_L='qtechKeyString'
_K='qtechAuthenKeyChainEntryStatus'
_J='invalid'
_I='qtechAuthenKeyNumber'
_H='qtechKeyChainName'
_G='qtechAuthenKeyChainName'
_F='DisplayString'
_E='Integer32'
_D='read-only'
_C='read-create'
_B='QTECH-AUTHEN-KEY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ConfigStatus,=mibBuilder.importSymbols('QTECH-TC','ConfigStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'PhysAddress','RowStatus','TextualConvention')
qtechAuthenKeyMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,24))
if mibBuilder.loadTexts:qtechAuthenKeyMIB.setRevisions(('2002-03-20 00:00',))
class QtechKeyTimeMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('infinite',1),('duration',2),('end-time',3)))
_QtechAuthenKeyMIBObjects_ObjectIdentity=ObjectIdentity
qtechAuthenKeyMIBObjects=_QtechAuthenKeyMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,24,1))
_QtechAuthenKeyChainTable_Object=MibTable
qtechAuthenKeyChainTable=_QtechAuthenKeyChainTable_Object((1,3,6,1,4,1,27514,1,1,10,2,24,1,1))
if mibBuilder.loadTexts:qtechAuthenKeyChainTable.setStatus(_A)
_QtechAuthenKeyChainEntry_Object=MibTableRow
qtechAuthenKeyChainEntry=_QtechAuthenKeyChainEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,24,1,1,1))
qtechAuthenKeyChainEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:qtechAuthenKeyChainEntry.setStatus(_A)
class _QtechAuthenKeyChainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechAuthenKeyChainName_Type.__name__=_F
_QtechAuthenKeyChainName_Object=MibTableColumn
qtechAuthenKeyChainName=_QtechAuthenKeyChainName_Object((1,3,6,1,4,1,27514,1,1,10,2,24,1,1,1,1),_QtechAuthenKeyChainName_Type())
qtechAuthenKeyChainName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAuthenKeyChainName.setStatus(_A)
_QtechAuthenKeyChainEntryStatus_Type=ConfigStatus
_QtechAuthenKeyChainEntryStatus_Object=MibTableColumn
qtechAuthenKeyChainEntryStatus=_QtechAuthenKeyChainEntryStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,24,1,1,1,2),_QtechAuthenKeyChainEntryStatus_Type())
qtechAuthenKeyChainEntryStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAuthenKeyChainEntryStatus.setStatus(_A)
_QtechAuthenKeyTable_Object=MibTable
qtechAuthenKeyTable=_QtechAuthenKeyTable_Object((1,3,6,1,4,1,27514,1,1,10,2,24,1,2))
if mibBuilder.loadTexts:qtechAuthenKeyTable.setStatus(_A)
_QtechAuthenKeyEntry_Object=MibTableRow
qtechAuthenKeyEntry=_QtechAuthenKeyEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,24,1,2,1))
qtechAuthenKeyEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:qtechAuthenKeyEntry.setStatus(_A)
class _QtechKeyChainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_QtechKeyChainName_Type.__name__=_F
_QtechKeyChainName_Object=MibTableColumn
qtechKeyChainName=_QtechKeyChainName_Object((1,3,6,1,4,1,27514,1,1,10,2,24,1,2,1,1),_QtechKeyChainName_Type())
qtechKeyChainName.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechKeyChainName.setStatus(_A)
class _QtechAuthenKeyNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_QtechAuthenKeyNumber_Type.__name__=_E
_QtechAuthenKeyNumber_Object=MibTableColumn
qtechAuthenKeyNumber=_QtechAuthenKeyNumber_Object((1,3,6,1,4,1,27514,1,1,10,2,24,1,2,1,2),_QtechAuthenKeyNumber_Type())
qtechAuthenKeyNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAuthenKeyNumber.setStatus(_A)
class _QtechKeyString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_QtechKeyString_Type.__name__=_F
_QtechKeyString_Object=MibTableColumn
qtechKeyString=_QtechKeyString_Object((1,3,6,1,4,1,27514,1,1,10,2,24,1,2,1,3),_QtechKeyString_Type())
qtechKeyString.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechKeyString.setStatus(_A)
_QtechAuthenKeyReceiveQtechTime_Type=DateAndTime
_QtechAuthenKeyReceiveQtechTime_Object=MibTableColumn
qtechAuthenKeyReceiveQtechTime=_QtechAuthenKeyReceiveQtechTime_Object((1,3,6,1,4,1,27514,1,1,10,2,24,1,2,1,4),_QtechAuthenKeyReceiveQtechTime_Type())
qtechAuthenKeyReceiveQtechTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAuthenKeyReceiveQtechTime.setStatus(_A)
_QtechAuthenKeyReceiveTimeMode_Type=QtechKeyTimeMode
_QtechAuthenKeyReceiveTimeMode_Object=MibTableColumn
qtechAuthenKeyReceiveTimeMode=_QtechAuthenKeyReceiveTimeMode_Object((1,3,6,1,4,1,27514,1,1,10,2,24,1,2,1,5),_QtechAuthenKeyReceiveTimeMode_Type())
qtechAuthenKeyReceiveTimeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAuthenKeyReceiveTimeMode.setStatus(_A)
_QtechAuthenKeyReceiveEndTime_Type=DateAndTime
_QtechAuthenKeyReceiveEndTime_Object=MibTableColumn
qtechAuthenKeyReceiveEndTime=_QtechAuthenKeyReceiveEndTime_Object((1,3,6,1,4,1,27514,1,1,10,2,24,1,2,1,6),_QtechAuthenKeyReceiveEndTime_Type())
qtechAuthenKeyReceiveEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAuthenKeyReceiveEndTime.setStatus(_A)
_QtechAuthenKeyReceiveDuration_Type=Unsigned32
_QtechAuthenKeyReceiveDuration_Object=MibTableColumn
qtechAuthenKeyReceiveDuration=_QtechAuthenKeyReceiveDuration_Object((1,3,6,1,4,1,27514,1,1,10,2,24,1,2,1,7),_QtechAuthenKeyReceiveDuration_Type())
qtechAuthenKeyReceiveDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAuthenKeyReceiveDuration.setStatus(_A)
_QtechAuthenKeySendQtechTime_Type=DateAndTime
_QtechAuthenKeySendQtechTime_Object=MibTableColumn
qtechAuthenKeySendQtechTime=_QtechAuthenKeySendQtechTime_Object((1,3,6,1,4,1,27514,1,1,10,2,24,1,2,1,8),_QtechAuthenKeySendQtechTime_Type())
qtechAuthenKeySendQtechTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAuthenKeySendQtechTime.setStatus(_A)
_QtechAuthenKeySendTimeMode_Type=QtechKeyTimeMode
_QtechAuthenKeySendTimeMode_Object=MibTableColumn
qtechAuthenKeySendTimeMode=_QtechAuthenKeySendTimeMode_Object((1,3,6,1,4,1,27514,1,1,10,2,24,1,2,1,9),_QtechAuthenKeySendTimeMode_Type())
qtechAuthenKeySendTimeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAuthenKeySendTimeMode.setStatus(_A)
_QtechAuthenKeySendEndTime_Type=DateAndTime
_QtechAuthenKeySendEndTime_Object=MibTableColumn
qtechAuthenKeySendEndTime=_QtechAuthenKeySendEndTime_Object((1,3,6,1,4,1,27514,1,1,10,2,24,1,2,1,10),_QtechAuthenKeySendEndTime_Type())
qtechAuthenKeySendEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAuthenKeySendEndTime.setStatus(_A)
_QtechAuthenKeySendDuration_Type=Unsigned32
_QtechAuthenKeySendDuration_Object=MibTableColumn
qtechAuthenKeySendDuration=_QtechAuthenKeySendDuration_Object((1,3,6,1,4,1,27514,1,1,10,2,24,1,2,1,11),_QtechAuthenKeySendDuration_Type())
qtechAuthenKeySendDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAuthenKeySendDuration.setStatus(_A)
class _QtechAuthenReceiveKeyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_J,2)))
_QtechAuthenReceiveKeyState_Type.__name__=_E
_QtechAuthenReceiveKeyState_Object=MibTableColumn
qtechAuthenReceiveKeyState=_QtechAuthenReceiveKeyState_Object((1,3,6,1,4,1,27514,1,1,10,2,24,1,2,1,12),_QtechAuthenReceiveKeyState_Type())
qtechAuthenReceiveKeyState.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAuthenReceiveKeyState.setStatus(_A)
class _QtechAuthenSendKeyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_J,2)))
_QtechAuthenSendKeyState_Type.__name__=_E
_QtechAuthenSendKeyState_Object=MibTableColumn
qtechAuthenSendKeyState=_QtechAuthenSendKeyState_Object((1,3,6,1,4,1,27514,1,1,10,2,24,1,2,1,13),_QtechAuthenSendKeyState_Type())
qtechAuthenSendKeyState.setMaxAccess(_D)
if mibBuilder.loadTexts:qtechAuthenSendKeyState.setStatus(_A)
_QtechAuthenKeyEntryStauts_Type=RowStatus
_QtechAuthenKeyEntryStauts_Object=MibTableColumn
qtechAuthenKeyEntryStauts=_QtechAuthenKeyEntryStauts_Object((1,3,6,1,4,1,27514,1,1,10,2,24,1,2,1,14),_QtechAuthenKeyEntryStauts_Type())
qtechAuthenKeyEntryStauts.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechAuthenKeyEntryStauts.setStatus(_A)
_QtechAuthenKeyChainMIBConformance_ObjectIdentity=ObjectIdentity
qtechAuthenKeyChainMIBConformance=_QtechAuthenKeyChainMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,24,2))
_QtechAuthenKeyChainMIBCompliances_ObjectIdentity=ObjectIdentity
qtechAuthenKeyChainMIBCompliances=_QtechAuthenKeyChainMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,24,2,1))
_QtechAuthenKeyChainMIBGroups_ObjectIdentity=ObjectIdentity
qtechAuthenKeyChainMIBGroups=_QtechAuthenKeyChainMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,24,2,2))
qtechAuthenKeyChainMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,24,2,2,1))
qtechAuthenKeyChainMIBGroup.setObjects(*((_B,_G),(_B,_K),(_B,_H),(_B,_I),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W)))
if mibBuilder.loadTexts:qtechAuthenKeyChainMIBGroup.setStatus(_A)
qtechAuthenKeyChainMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,24,2,1,1))
qtechAuthenKeyChainMIBCompliance.setObjects((_B,_X))
if mibBuilder.loadTexts:qtechAuthenKeyChainMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'QtechKeyTimeMode':QtechKeyTimeMode,'qtechAuthenKeyMIB':qtechAuthenKeyMIB,'qtechAuthenKeyMIBObjects':qtechAuthenKeyMIBObjects,'qtechAuthenKeyChainTable':qtechAuthenKeyChainTable,'qtechAuthenKeyChainEntry':qtechAuthenKeyChainEntry,_G:qtechAuthenKeyChainName,_K:qtechAuthenKeyChainEntryStatus,'qtechAuthenKeyTable':qtechAuthenKeyTable,'qtechAuthenKeyEntry':qtechAuthenKeyEntry,_H:qtechKeyChainName,_I:qtechAuthenKeyNumber,_L:qtechKeyString,_M:qtechAuthenKeyReceiveQtechTime,_N:qtechAuthenKeyReceiveTimeMode,_O:qtechAuthenKeyReceiveEndTime,_P:qtechAuthenKeyReceiveDuration,_Q:qtechAuthenKeySendQtechTime,_R:qtechAuthenKeySendTimeMode,_S:qtechAuthenKeySendEndTime,_T:qtechAuthenKeySendDuration,_U:qtechAuthenReceiveKeyState,_V:qtechAuthenSendKeyState,_W:qtechAuthenKeyEntryStauts,'qtechAuthenKeyChainMIBConformance':qtechAuthenKeyChainMIBConformance,'qtechAuthenKeyChainMIBCompliances':qtechAuthenKeyChainMIBCompliances,'qtechAuthenKeyChainMIBCompliance':qtechAuthenKeyChainMIBCompliance,'qtechAuthenKeyChainMIBGroups':qtechAuthenKeyChainMIBGroups,_X:qtechAuthenKeyChainMIBGroup})