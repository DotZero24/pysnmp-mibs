_T='slGenEventUser'
_S='slGenEventVal'
_R='slEventInventoryPartnum'
_Q='slEventInventorySerial'
_P='slEventInventoryAction'
_O='slEventUser'
_N='slEventVal'
_M='slGenEventType'
_L='slGenEventIfIndex'
_K='slEventInventoryType'
_J='slEventInventoryIfIndex'
_I='slEventType'
_H='slEventIfIndex'
_G='read-only'
_F='slmTrapLogId'
_E='SL-MAIN-MIB'
_D='read-write'
_C='DisplayString'
_B='SL-EVENT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
slMain,slmTrapLogId=mibBuilder.importSymbols(_E,'slMain',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','TextualConvention','TimeStamp','TruthValue')
slEventMib=ModuleIdentity((1,3,6,1,4,1,4515,1,3,22))
class SlGenEventType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('swUpgradeEvent',1),('remoteUnitFailEvent',2),('alsOperStatus',3),('opticalPowerDrop',4),('userLoginLogout',5)))
class SlEventType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)));namedValues=NamedValues(*(('edDate',1),('rstProv',2),('edIp',3),('initPm',4),('dltIpRoute',5),('edSys',6),('setSid',7),('addUser',8),('dltUser',9),('rmvFac',10),('rstFac',11),('edFac',12),('oprLoopback',13),('rlsLoopback',14),('entAps',15),('dltAps',16),('oprProtSw',17),('rlsProtSw',18),('oprAco',19),('rstProvCommit',20),('savProvStart',21),('savProvComplete',22),('savProvFailed',23),('swLoadUpgrade',24)))
class SlEventInventoryAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('inserted',1),('removed',2)))
class SlEventInventoryType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('psu',1),('optics',2),('fan',3)))
_SlEventConfig_ObjectIdentity=ObjectIdentity
slEventConfig=_SlEventConfig_ObjectIdentity((1,3,6,1,4,1,4515,1,3,22,1))
_SlEventConfigTable_Object=MibTable
slEventConfigTable=_SlEventConfigTable_Object((1,3,6,1,4,1,4515,1,3,22,1,1))
if mibBuilder.loadTexts:slEventConfigTable.setStatus(_A)
_SlEventConfigEntry_Object=MibTableRow
slEventConfigEntry=_SlEventConfigEntry_Object((1,3,6,1,4,1,4515,1,3,22,1,1,1))
slEventConfigEntry.setIndexNames((0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:slEventConfigEntry.setStatus(_A)
_SlEventIfIndex_Type=InterfaceIndex
_SlEventIfIndex_Object=MibTableColumn
slEventIfIndex=_SlEventIfIndex_Object((1,3,6,1,4,1,4515,1,3,22,1,1,1,1),_SlEventIfIndex_Type())
slEventIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:slEventIfIndex.setStatus(_A)
_SlEventType_Type=SlEventType
_SlEventType_Object=MibTableColumn
slEventType=_SlEventType_Object((1,3,6,1,4,1,4515,1,3,22,1,1,1,2),_SlEventType_Type())
slEventType.setMaxAccess(_G)
if mibBuilder.loadTexts:slEventType.setStatus(_A)
class _SlEventVal_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SlEventVal_Type.__name__=_C
_SlEventVal_Object=MibTableColumn
slEventVal=_SlEventVal_Object((1,3,6,1,4,1,4515,1,3,22,1,1,1,3),_SlEventVal_Type())
slEventVal.setMaxAccess(_D)
if mibBuilder.loadTexts:slEventVal.setStatus(_A)
class _SlEventUser_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SlEventUser_Type.__name__=_C
_SlEventUser_Object=MibTableColumn
slEventUser=_SlEventUser_Object((1,3,6,1,4,1,4515,1,3,22,1,1,1,4),_SlEventUser_Type())
slEventUser.setMaxAccess(_D)
if mibBuilder.loadTexts:slEventUser.setStatus(_A)
class _SlEventCtag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SlEventCtag_Type.__name__=_C
_SlEventCtag_Object=MibTableColumn
slEventCtag=_SlEventCtag_Object((1,3,6,1,4,1,4515,1,3,22,1,1,1,5),_SlEventCtag_Type())
slEventCtag.setMaxAccess(_D)
if mibBuilder.loadTexts:slEventCtag.setStatus(_A)
class _SlEventTid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SlEventTid_Type.__name__=_C
_SlEventTid_Object=MibTableColumn
slEventTid=_SlEventTid_Object((1,3,6,1,4,1,4515,1,3,22,1,1,1,6),_SlEventTid_Type())
slEventTid.setMaxAccess(_D)
if mibBuilder.loadTexts:slEventTid.setStatus(_A)
_SlEventInventoryTable_Object=MibTable
slEventInventoryTable=_SlEventInventoryTable_Object((1,3,6,1,4,1,4515,1,3,22,1,2))
if mibBuilder.loadTexts:slEventInventoryTable.setStatus(_A)
_SlEventInventoryEntry_Object=MibTableRow
slEventInventoryEntry=_SlEventInventoryEntry_Object((1,3,6,1,4,1,4515,1,3,22,1,2,1))
slEventInventoryEntry.setIndexNames((0,_B,_J),(0,_B,_K))
if mibBuilder.loadTexts:slEventInventoryEntry.setStatus(_A)
_SlEventInventoryIfIndex_Type=InterfaceIndex
_SlEventInventoryIfIndex_Object=MibTableColumn
slEventInventoryIfIndex=_SlEventInventoryIfIndex_Object((1,3,6,1,4,1,4515,1,3,22,1,2,1,1),_SlEventInventoryIfIndex_Type())
slEventInventoryIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:slEventInventoryIfIndex.setStatus(_A)
_SlEventInventoryAction_Type=SlEventInventoryAction
_SlEventInventoryAction_Object=MibTableColumn
slEventInventoryAction=_SlEventInventoryAction_Object((1,3,6,1,4,1,4515,1,3,22,1,2,1,2),_SlEventInventoryAction_Type())
slEventInventoryAction.setMaxAccess(_G)
if mibBuilder.loadTexts:slEventInventoryAction.setStatus(_A)
_SlEventInventoryType_Type=SlEventInventoryType
_SlEventInventoryType_Object=MibTableColumn
slEventInventoryType=_SlEventInventoryType_Object((1,3,6,1,4,1,4515,1,3,22,1,2,1,3),_SlEventInventoryType_Type())
slEventInventoryType.setMaxAccess(_G)
if mibBuilder.loadTexts:slEventInventoryType.setStatus(_A)
class _SlEventInventorySerial_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_SlEventInventorySerial_Type.__name__=_C
_SlEventInventorySerial_Object=MibTableColumn
slEventInventorySerial=_SlEventInventorySerial_Object((1,3,6,1,4,1,4515,1,3,22,1,2,1,4),_SlEventInventorySerial_Type())
slEventInventorySerial.setMaxAccess(_D)
if mibBuilder.loadTexts:slEventInventorySerial.setStatus(_A)
_SlEventInventoryPartnum_Type=DisplayString
_SlEventInventoryPartnum_Object=MibTableColumn
slEventInventoryPartnum=_SlEventInventoryPartnum_Object((1,3,6,1,4,1,4515,1,3,22,1,2,1,5),_SlEventInventoryPartnum_Type())
slEventInventoryPartnum.setMaxAccess(_D)
if mibBuilder.loadTexts:slEventInventoryPartnum.setStatus(_A)
_SlGenEventConfigTable_Object=MibTable
slGenEventConfigTable=_SlGenEventConfigTable_Object((1,3,6,1,4,1,4515,1,3,22,1,3))
if mibBuilder.loadTexts:slGenEventConfigTable.setStatus(_A)
_SlGenEventConfigEntry_Object=MibTableRow
slGenEventConfigEntry=_SlGenEventConfigEntry_Object((1,3,6,1,4,1,4515,1,3,22,1,3,1))
slGenEventConfigEntry.setIndexNames((0,_B,_L),(0,_B,_M))
if mibBuilder.loadTexts:slGenEventConfigEntry.setStatus(_A)
_SlGenEventIfIndex_Type=InterfaceIndex
_SlGenEventIfIndex_Object=MibTableColumn
slGenEventIfIndex=_SlGenEventIfIndex_Object((1,3,6,1,4,1,4515,1,3,22,1,3,1,1),_SlGenEventIfIndex_Type())
slGenEventIfIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:slGenEventIfIndex.setStatus(_A)
_SlGenEventType_Type=SlGenEventType
_SlGenEventType_Object=MibTableColumn
slGenEventType=_SlGenEventType_Object((1,3,6,1,4,1,4515,1,3,22,1,3,1,2),_SlGenEventType_Type())
slGenEventType.setMaxAccess(_G)
if mibBuilder.loadTexts:slGenEventType.setStatus(_A)
class _SlGenEventVal_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SlGenEventVal_Type.__name__=_C
_SlGenEventVal_Object=MibTableColumn
slGenEventVal=_SlGenEventVal_Object((1,3,6,1,4,1,4515,1,3,22,1,3,1,3),_SlGenEventVal_Type())
slGenEventVal.setMaxAccess(_D)
if mibBuilder.loadTexts:slGenEventVal.setStatus(_A)
class _SlGenEventUser_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SlGenEventUser_Type.__name__=_C
_SlGenEventUser_Object=MibTableColumn
slGenEventUser=_SlGenEventUser_Object((1,3,6,1,4,1,4515,1,3,22,1,3,1,4),_SlGenEventUser_Type())
slGenEventUser.setMaxAccess(_D)
if mibBuilder.loadTexts:slGenEventUser.setStatus(_A)
class _SlGenEventCtag_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SlGenEventCtag_Type.__name__=_C
_SlGenEventCtag_Object=MibTableColumn
slGenEventCtag=_SlGenEventCtag_Object((1,3,6,1,4,1,4515,1,3,22,1,3,1,5),_SlGenEventCtag_Type())
slGenEventCtag.setMaxAccess(_D)
if mibBuilder.loadTexts:slGenEventCtag.setStatus(_A)
class _SlGenEventTid_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_SlGenEventTid_Type.__name__=_C
_SlGenEventTid_Object=MibTableColumn
slGenEventTid=_SlGenEventTid_Object((1,3,6,1,4,1,4515,1,3,22,1,3,1,6),_SlGenEventTid_Type())
slGenEventTid.setMaxAccess(_D)
if mibBuilder.loadTexts:slGenEventTid.setStatus(_A)
_SlEventTraps_ObjectIdentity=ObjectIdentity
slEventTraps=_SlEventTraps_ObjectIdentity((1,3,6,1,4,1,4515,1,3,22,2))
_SlEventTraps0_ObjectIdentity=ObjectIdentity
slEventTraps0=_SlEventTraps0_ObjectIdentity((1,3,6,1,4,1,4515,1,3,22,2,0))
slEventTrap0=NotificationType((1,3,6,1,4,1,4515,1,3,22,2,0,2))
slEventTrap0.setObjects(*((_B,_H),(_B,_I),(_B,_N),(_B,_O),(_E,_F)))
if mibBuilder.loadTexts:slEventTrap0.setStatus(_A)
slEventInventoryTrap0=NotificationType((1,3,6,1,4,1,4515,1,3,22,2,0,3))
slEventInventoryTrap0.setObjects(*((_B,_J),(_B,_P),(_B,_K),(_B,_Q),(_B,_R),(_E,_F)))
if mibBuilder.loadTexts:slEventInventoryTrap0.setStatus(_A)
slGenEventTrap0=NotificationType((1,3,6,1,4,1,4515,1,3,22,2,0,4))
slGenEventTrap0.setObjects(*((_B,_L),(_B,_M),(_B,_S),(_B,_T),(_E,_F)))
if mibBuilder.loadTexts:slGenEventTrap0.setStatus(_A)
slEventTrap=NotificationType((1,3,6,1,4,1,4515,1,3,22,2,2))
slEventTrap.setObjects(*((_B,_H),(_B,_I),(_B,_N),(_B,_O),(_E,_F)))
if mibBuilder.loadTexts:slEventTrap.setStatus(_A)
slEventInventoryTrap=NotificationType((1,3,6,1,4,1,4515,1,3,22,2,3))
slEventInventoryTrap.setObjects(*((_B,_J),(_B,_P),(_B,_K),(_B,_Q),(_B,_R),(_E,_F)))
if mibBuilder.loadTexts:slEventInventoryTrap.setStatus(_A)
slGenEventTrap=NotificationType((1,3,6,1,4,1,4515,1,3,22,2,4))
slGenEventTrap.setObjects(*((_B,_L),(_B,_M),(_B,_S),(_B,_T),(_E,_F)))
if mibBuilder.loadTexts:slGenEventTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'SlGenEventType':SlGenEventType,'SlEventType':SlEventType,'SlEventInventoryAction':SlEventInventoryAction,'SlEventInventoryType':SlEventInventoryType,'slEventMib':slEventMib,'slEventConfig':slEventConfig,'slEventConfigTable':slEventConfigTable,'slEventConfigEntry':slEventConfigEntry,_H:slEventIfIndex,_I:slEventType,_N:slEventVal,_O:slEventUser,'slEventCtag':slEventCtag,'slEventTid':slEventTid,'slEventInventoryTable':slEventInventoryTable,'slEventInventoryEntry':slEventInventoryEntry,_J:slEventInventoryIfIndex,_P:slEventInventoryAction,_K:slEventInventoryType,_Q:slEventInventorySerial,_R:slEventInventoryPartnum,'slGenEventConfigTable':slGenEventConfigTable,'slGenEventConfigEntry':slGenEventConfigEntry,_L:slGenEventIfIndex,_M:slGenEventType,_S:slGenEventVal,_T:slGenEventUser,'slGenEventCtag':slGenEventCtag,'slGenEventTid':slGenEventTid,'slEventTraps':slEventTraps,'slEventTraps0':slEventTraps0,'slEventTrap0':slEventTrap0,'slEventInventoryTrap0':slEventInventoryTrap0,'slGenEventTrap0':slGenEventTrap0,'slEventTrap':slEventTrap,'slEventInventoryTrap':slEventInventoryTrap,'slGenEventTrap':slGenEventTrap})