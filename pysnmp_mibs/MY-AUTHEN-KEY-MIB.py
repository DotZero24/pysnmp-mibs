_Y='myAuthenKeyChainMIBGroup'
_X='myAuthenKeyEntryStauts'
_W='myAuthenSendKeyState'
_V='myAuthenReceiveKeyState'
_U='myAuthenKeySendDuration'
_T='myAuthenKeySendEndTime'
_S='myAuthenKeySendTimeMode'
_R='myAuthenKeySendMyTime'
_Q='myAuthenKeyReceiveDuration'
_P='myAuthenKeyReceiveEndTime'
_O='myAuthenKeyReceiveTimeMode'
_N='myAuthenKeyReceiveMyTime'
_M='myKeyString'
_L='myAuthenKeyChainEntryStatus'
_K='invalid'
_J='read-create'
_I='myAuthenKeyNumber'
_H='myKeyChainName'
_G='myAuthenKeyChainName'
_F='DisplayString'
_E='Integer32'
_D='read-only'
_C='read-write'
_B='MY-AUTHEN-KEY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('MY-SMI','myMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('MY-TC','ConfigStatus','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
myAuthenKeyMIB=ModuleIdentity((1,3,6,1,4,1,4881,1,1,10,2,24))
if mibBuilder.loadTexts:myAuthenKeyMIB.setRevisions(('2002-03-20 00:00',))
class MyKeyTimeMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('infinite',1),('duration',2),('end-time',3)))
_MyAuthenKeyMIBObjects_ObjectIdentity=ObjectIdentity
myAuthenKeyMIBObjects=_MyAuthenKeyMIBObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,24,1))
_MyAuthenKeyChainTable_Object=MibTable
myAuthenKeyChainTable=_MyAuthenKeyChainTable_Object((1,3,6,1,4,1,4881,1,1,10,2,24,1,1))
if mibBuilder.loadTexts:myAuthenKeyChainTable.setStatus(_A)
_MyAuthenKeyChainEntry_Object=MibTableRow
myAuthenKeyChainEntry=_MyAuthenKeyChainEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,24,1,1,1))
myAuthenKeyChainEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:myAuthenKeyChainEntry.setStatus(_A)
class _MyAuthenKeyChainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MyAuthenKeyChainName_Type.__name__=_F
_MyAuthenKeyChainName_Object=MibTableColumn
myAuthenKeyChainName=_MyAuthenKeyChainName_Object((1,3,6,1,4,1,4881,1,1,10,2,24,1,1,1,1),_MyAuthenKeyChainName_Type())
myAuthenKeyChainName.setMaxAccess(_D)
if mibBuilder.loadTexts:myAuthenKeyChainName.setStatus(_A)
_MyAuthenKeyChainEntryStatus_Type=ConfigStatus
_MyAuthenKeyChainEntryStatus_Object=MibTableColumn
myAuthenKeyChainEntryStatus=_MyAuthenKeyChainEntryStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,24,1,1,1,2),_MyAuthenKeyChainEntryStatus_Type())
myAuthenKeyChainEntryStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:myAuthenKeyChainEntryStatus.setStatus(_A)
_MyAuthenKeyTable_Object=MibTable
myAuthenKeyTable=_MyAuthenKeyTable_Object((1,3,6,1,4,1,4881,1,1,10,2,24,1,2))
if mibBuilder.loadTexts:myAuthenKeyTable.setStatus(_A)
_MyAuthenKeyEntry_Object=MibTableRow
myAuthenKeyEntry=_MyAuthenKeyEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,24,1,2,1))
myAuthenKeyEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:myAuthenKeyEntry.setStatus(_A)
class _MyKeyChainName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MyKeyChainName_Type.__name__=_F
_MyKeyChainName_Object=MibTableColumn
myKeyChainName=_MyKeyChainName_Object((1,3,6,1,4,1,4881,1,1,10,2,24,1,2,1,1),_MyKeyChainName_Type())
myKeyChainName.setMaxAccess(_D)
if mibBuilder.loadTexts:myKeyChainName.setStatus(_A)
class _MyAuthenKeyNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_MyAuthenKeyNumber_Type.__name__=_E
_MyAuthenKeyNumber_Object=MibTableColumn
myAuthenKeyNumber=_MyAuthenKeyNumber_Object((1,3,6,1,4,1,4881,1,1,10,2,24,1,2,1,2),_MyAuthenKeyNumber_Type())
myAuthenKeyNumber.setMaxAccess(_D)
if mibBuilder.loadTexts:myAuthenKeyNumber.setStatus(_A)
class _MyKeyString_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,80))
_MyKeyString_Type.__name__=_F
_MyKeyString_Object=MibTableColumn
myKeyString=_MyKeyString_Object((1,3,6,1,4,1,4881,1,1,10,2,24,1,2,1,3),_MyKeyString_Type())
myKeyString.setMaxAccess(_D)
if mibBuilder.loadTexts:myKeyString.setStatus(_A)
_MyAuthenKeyReceiveMyTime_Type=DateAndTime
_MyAuthenKeyReceiveMyTime_Object=MibTableColumn
myAuthenKeyReceiveMyTime=_MyAuthenKeyReceiveMyTime_Object((1,3,6,1,4,1,4881,1,1,10,2,24,1,2,1,4),_MyAuthenKeyReceiveMyTime_Type())
myAuthenKeyReceiveMyTime.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthenKeyReceiveMyTime.setStatus(_A)
_MyAuthenKeyReceiveTimeMode_Type=MyKeyTimeMode
_MyAuthenKeyReceiveTimeMode_Object=MibTableColumn
myAuthenKeyReceiveTimeMode=_MyAuthenKeyReceiveTimeMode_Object((1,3,6,1,4,1,4881,1,1,10,2,24,1,2,1,5),_MyAuthenKeyReceiveTimeMode_Type())
myAuthenKeyReceiveTimeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthenKeyReceiveTimeMode.setStatus(_A)
_MyAuthenKeyReceiveEndTime_Type=DateAndTime
_MyAuthenKeyReceiveEndTime_Object=MibTableColumn
myAuthenKeyReceiveEndTime=_MyAuthenKeyReceiveEndTime_Object((1,3,6,1,4,1,4881,1,1,10,2,24,1,2,1,6),_MyAuthenKeyReceiveEndTime_Type())
myAuthenKeyReceiveEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthenKeyReceiveEndTime.setStatus(_A)
_MyAuthenKeyReceiveDuration_Type=Unsigned32
_MyAuthenKeyReceiveDuration_Object=MibTableColumn
myAuthenKeyReceiveDuration=_MyAuthenKeyReceiveDuration_Object((1,3,6,1,4,1,4881,1,1,10,2,24,1,2,1,7),_MyAuthenKeyReceiveDuration_Type())
myAuthenKeyReceiveDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthenKeyReceiveDuration.setStatus(_A)
_MyAuthenKeySendMyTime_Type=DateAndTime
_MyAuthenKeySendMyTime_Object=MibTableColumn
myAuthenKeySendMyTime=_MyAuthenKeySendMyTime_Object((1,3,6,1,4,1,4881,1,1,10,2,24,1,2,1,8),_MyAuthenKeySendMyTime_Type())
myAuthenKeySendMyTime.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthenKeySendMyTime.setStatus(_A)
_MyAuthenKeySendTimeMode_Type=MyKeyTimeMode
_MyAuthenKeySendTimeMode_Object=MibTableColumn
myAuthenKeySendTimeMode=_MyAuthenKeySendTimeMode_Object((1,3,6,1,4,1,4881,1,1,10,2,24,1,2,1,9),_MyAuthenKeySendTimeMode_Type())
myAuthenKeySendTimeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthenKeySendTimeMode.setStatus(_A)
_MyAuthenKeySendEndTime_Type=DateAndTime
_MyAuthenKeySendEndTime_Object=MibTableColumn
myAuthenKeySendEndTime=_MyAuthenKeySendEndTime_Object((1,3,6,1,4,1,4881,1,1,10,2,24,1,2,1,10),_MyAuthenKeySendEndTime_Type())
myAuthenKeySendEndTime.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthenKeySendEndTime.setStatus(_A)
_MyAuthenKeySendDuration_Type=Unsigned32
_MyAuthenKeySendDuration_Object=MibTableColumn
myAuthenKeySendDuration=_MyAuthenKeySendDuration_Object((1,3,6,1,4,1,4881,1,1,10,2,24,1,2,1,11),_MyAuthenKeySendDuration_Type())
myAuthenKeySendDuration.setMaxAccess(_C)
if mibBuilder.loadTexts:myAuthenKeySendDuration.setStatus(_A)
class _MyAuthenReceiveKeyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_K,2)))
_MyAuthenReceiveKeyState_Type.__name__=_E
_MyAuthenReceiveKeyState_Object=MibTableColumn
myAuthenReceiveKeyState=_MyAuthenReceiveKeyState_Object((1,3,6,1,4,1,4881,1,1,10,2,24,1,2,1,12),_MyAuthenReceiveKeyState_Type())
myAuthenReceiveKeyState.setMaxAccess(_D)
if mibBuilder.loadTexts:myAuthenReceiveKeyState.setStatus(_A)
class _MyAuthenSendKeyState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('valid',1),(_K,2)))
_MyAuthenSendKeyState_Type.__name__=_E
_MyAuthenSendKeyState_Object=MibTableColumn
myAuthenSendKeyState=_MyAuthenSendKeyState_Object((1,3,6,1,4,1,4881,1,1,10,2,24,1,2,1,13),_MyAuthenSendKeyState_Type())
myAuthenSendKeyState.setMaxAccess(_D)
if mibBuilder.loadTexts:myAuthenSendKeyState.setStatus(_A)
_MyAuthenKeyEntryStauts_Type=RowStatus
_MyAuthenKeyEntryStauts_Object=MibTableColumn
myAuthenKeyEntryStauts=_MyAuthenKeyEntryStauts_Object((1,3,6,1,4,1,4881,1,1,10,2,24,1,2,1,14),_MyAuthenKeyEntryStauts_Type())
myAuthenKeyEntryStauts.setMaxAccess(_J)
if mibBuilder.loadTexts:myAuthenKeyEntryStauts.setStatus(_A)
_MyAuthenKeyChainMIBConformance_ObjectIdentity=ObjectIdentity
myAuthenKeyChainMIBConformance=_MyAuthenKeyChainMIBConformance_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,24,2))
_MyAuthenKeyChainMIBCompliances_ObjectIdentity=ObjectIdentity
myAuthenKeyChainMIBCompliances=_MyAuthenKeyChainMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,24,2,1))
_MyAuthenKeyChainMIBGroups_ObjectIdentity=ObjectIdentity
myAuthenKeyChainMIBGroups=_MyAuthenKeyChainMIBGroups_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,24,2,2))
myAuthenKeyChainMIBGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,24,2,2,1))
myAuthenKeyChainMIBGroup.setObjects(*((_B,_G),(_B,_L),(_B,_H),(_B,_I),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:myAuthenKeyChainMIBGroup.setStatus(_A)
myAuthenKeyChainMIBCompliance=ModuleCompliance((1,3,6,1,4,1,4881,1,1,10,2,24,2,1,1))
myAuthenKeyChainMIBCompliance.setObjects((_B,_Y))
if mibBuilder.loadTexts:myAuthenKeyChainMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'MyKeyTimeMode':MyKeyTimeMode,'myAuthenKeyMIB':myAuthenKeyMIB,'myAuthenKeyMIBObjects':myAuthenKeyMIBObjects,'myAuthenKeyChainTable':myAuthenKeyChainTable,'myAuthenKeyChainEntry':myAuthenKeyChainEntry,_G:myAuthenKeyChainName,_L:myAuthenKeyChainEntryStatus,'myAuthenKeyTable':myAuthenKeyTable,'myAuthenKeyEntry':myAuthenKeyEntry,_H:myKeyChainName,_I:myAuthenKeyNumber,_M:myKeyString,_N:myAuthenKeyReceiveMyTime,_O:myAuthenKeyReceiveTimeMode,_P:myAuthenKeyReceiveEndTime,_Q:myAuthenKeyReceiveDuration,_R:myAuthenKeySendMyTime,_S:myAuthenKeySendTimeMode,_T:myAuthenKeySendEndTime,_U:myAuthenKeySendDuration,_V:myAuthenReceiveKeyState,_W:myAuthenSendKeyState,_X:myAuthenKeyEntryStauts,'myAuthenKeyChainMIBConformance':myAuthenKeyChainMIBConformance,'myAuthenKeyChainMIBCompliances':myAuthenKeyChainMIBCompliances,'myAuthenKeyChainMIBCompliance':myAuthenKeyChainMIBCompliance,'myAuthenKeyChainMIBGroups':myAuthenKeyChainMIBGroups,_Y:myAuthenKeyChainMIBGroup})