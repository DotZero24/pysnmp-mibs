_Q='tnClearErrorText'
_P='tnClearResult'
_O='tnClearLastClearedTime'
_N='tnClearParams'
_M='tnClearName'
_L='read-write'
_K='tnClearIndex'
_J='tnSysSwitchId'
_I='TROPIC-SYSTEM-MIB'
_H='TmnxActionType'
_G='tnEventAppIndex'
_F='TN-LOG-MIB'
_E='Integer32'
_D='OctetString'
_C='read-only'
_B='TN-CLEAR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp')
tnEventAppIndex,=mibBuilder.importSymbols(_F,_G)
TNamedItem,TmnxActionType=mibBuilder.importSymbols('TN-TC-MIB','TNamedItem',_H)
tnSRMIBModules,tnSRNotifyPrefix,tnSRObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSRMIBModules','tnSRNotifyPrefix','tnSRObjs')
tnSysSwitchId,=mibBuilder.importSymbols(_I,_J)
tnClearMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,3,13))
if mibBuilder.loadTexts:tnClearMIBModule.setRevisions(('2005-01-24 00:00','2004-06-02 00:00','2004-01-15 00:00','2003-08-15 00:00','2003-01-20 00:00','2002-02-27 00:00'))
_TnClearObjs_ObjectIdentity=ObjectIdentity
tnClearObjs=_TnClearObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,13))
_TnClearTable_Object=MibTable
tnClearTable=_TnClearTable_Object((1,3,6,1,4,1,7483,6,1,2,13,1))
if mibBuilder.loadTexts:tnClearTable.setStatus(_A)
_TnClearEntry_Object=MibTableRow
tnClearEntry=_TnClearEntry_Object((1,3,6,1,4,1,7483,6,1,2,13,1,1))
tnClearEntry.setIndexNames((0,_I,_J),(0,_F,_G),(0,_B,_K))
if mibBuilder.loadTexts:tnClearEntry.setStatus(_A)
class _TnClearIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_TnClearIndex_Type.__name__=_E
_TnClearIndex_Object=MibTableColumn
tnClearIndex=_TnClearIndex_Object((1,3,6,1,4,1,7483,6,1,2,13,1,1,1),_TnClearIndex_Type())
tnClearIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:tnClearIndex.setStatus(_A)
_TnClearName_Type=TNamedItem
_TnClearName_Object=MibTableColumn
tnClearName=_TnClearName_Object((1,3,6,1,4,1,7483,6,1,2,13,1,1,2),_TnClearName_Type())
tnClearName.setMaxAccess(_C)
if mibBuilder.loadTexts:tnClearName.setStatus(_A)
class _TnClearParams_Type(OctetString):defaultHexValue='';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TnClearParams_Type.__name__=_D
_TnClearParams_Object=MibTableColumn
tnClearParams=_TnClearParams_Object((1,3,6,1,4,1,7483,6,1,2,13,1,1,3),_TnClearParams_Type())
tnClearParams.setMaxAccess(_L)
if mibBuilder.loadTexts:tnClearParams.setStatus(_A)
class _TnClearAction_Type(TmnxActionType):defaultValue=2
_TnClearAction_Type.__name__=_H
_TnClearAction_Object=MibTableColumn
tnClearAction=_TnClearAction_Object((1,3,6,1,4,1,7483,6,1,2,13,1,1,4),_TnClearAction_Type())
tnClearAction.setMaxAccess(_L)
if mibBuilder.loadTexts:tnClearAction.setStatus(_A)
_TnClearLastClearedTime_Type=TimeStamp
_TnClearLastClearedTime_Object=MibTableColumn
tnClearLastClearedTime=_TnClearLastClearedTime_Object((1,3,6,1,4,1,7483,6,1,2,13,1,1,5),_TnClearLastClearedTime_Type())
tnClearLastClearedTime.setMaxAccess(_C)
if mibBuilder.loadTexts:tnClearLastClearedTime.setStatus(_A)
class _TnClearResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('success',1),('failure',2)))
_TnClearResult_Type.__name__=_E
_TnClearResult_Object=MibTableColumn
tnClearResult=_TnClearResult_Object((1,3,6,1,4,1,7483,6,1,2,13,1,1,6),_TnClearResult_Type())
tnClearResult.setMaxAccess(_C)
if mibBuilder.loadTexts:tnClearResult.setStatus(_A)
class _TnClearErrorText_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_TnClearErrorText_Type.__name__=_D
_TnClearErrorText_Object=MibTableColumn
tnClearErrorText=_TnClearErrorText_Object((1,3,6,1,4,1,7483,6,1,2,13,1,1,7),_TnClearErrorText_Type())
tnClearErrorText.setMaxAccess(_C)
if mibBuilder.loadTexts:tnClearErrorText.setStatus(_A)
_TnClearScalar1_Type=Unsigned32
_TnClearScalar1_Object=MibScalar
tnClearScalar1=_TnClearScalar1_Object((1,3,6,1,4,1,7483,6,1,2,13,101),_TnClearScalar1_Type())
tnClearScalar1.setMaxAccess(_C)
if mibBuilder.loadTexts:tnClearScalar1.setStatus(_A)
_TnClearScalar2_Type=Unsigned32
_TnClearScalar2_Object=MibScalar
tnClearScalar2=_TnClearScalar2_Object((1,3,6,1,4,1,7483,6,1,2,13,102),_TnClearScalar2_Type())
tnClearScalar2.setMaxAccess(_C)
if mibBuilder.loadTexts:tnClearScalar2.setStatus(_A)
_TnClearNotificationsPrefix_ObjectIdentity=ObjectIdentity
tnClearNotificationsPrefix=_TnClearNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,13))
_TnClearNotifications_ObjectIdentity=ObjectIdentity
tnClearNotifications=_TnClearNotifications_ObjectIdentity((1,3,6,1,4,1,7483,6,1,3,13,0))
tnClear=NotificationType((1,3,6,1,4,1,7483,6,1,3,13,0,1))
tnClear.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:tnClear.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'tnClearMIBModule':tnClearMIBModule,'tnClearObjs':tnClearObjs,'tnClearTable':tnClearTable,'tnClearEntry':tnClearEntry,_K:tnClearIndex,_M:tnClearName,_N:tnClearParams,'tnClearAction':tnClearAction,_O:tnClearLastClearedTime,_P:tnClearResult,_Q:tnClearErrorText,'tnClearScalar1':tnClearScalar1,'tnClearScalar2':tnClearScalar2,'tnClearNotificationsPrefix':tnClearNotificationsPrefix,'tnClearNotifications':tnClearNotifications,'tnClear':tnClear})