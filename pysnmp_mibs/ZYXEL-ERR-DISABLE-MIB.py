_W='zyErrdisableRecoveryPort'
_V='zyErrdisableRecoveryType'
_U='rateLimitation'
_T='inactiveReason'
_S='inactivePort'
_R='zyErrdisableDetectReasonType'
_Q='zyErrdisableRecoveryReasonType'
_P='zyErrdisableTrapMode'
_O='zyErrdisableTrapReasonType'
_N='zyErrdisableTrapPort'
_M='zuld'
_L='bpduGuard'
_K='antiArpScan'
_J='loopGuard'
_I='read-only'
_H='not-accessible'
_G='igmp'
_F='bpdu'
_E='arp'
_D='read-write'
_C='Integer32'
_B='ZYXEL-ERR-DISABLE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelErrdisable=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,24))
_ZyxelErrdisableSetup_ObjectIdentity=ObjectIdentity
zyxelErrdisableSetup=_ZyxelErrdisableSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,24,1))
_ZyxelErrdisableRecovery_ObjectIdentity=ObjectIdentity
zyxelErrdisableRecovery=_ZyxelErrdisableRecovery_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,24,1,1))
_ZyErrdisableRecoveryState_Type=EnabledStatus
_ZyErrdisableRecoveryState_Object=MibScalar
zyErrdisableRecoveryState=_ZyErrdisableRecoveryState_Object((1,3,6,1,4,1,890,1,15,3,24,1,1,1),_ZyErrdisableRecoveryState_Type())
zyErrdisableRecoveryState.setMaxAccess(_D)
if mibBuilder.loadTexts:zyErrdisableRecoveryState.setStatus(_A)
_ZyxelErrdisableRecoveryReasonTable_Object=MibTable
zyxelErrdisableRecoveryReasonTable=_ZyxelErrdisableRecoveryReasonTable_Object((1,3,6,1,4,1,890,1,15,3,24,1,1,2))
if mibBuilder.loadTexts:zyxelErrdisableRecoveryReasonTable.setStatus(_A)
_ZyxelErrdisableRecoveryReasonEntry_Object=MibTableRow
zyxelErrdisableRecoveryReasonEntry=_ZyxelErrdisableRecoveryReasonEntry_Object((1,3,6,1,4,1,890,1,15,3,24,1,1,2,1))
zyxelErrdisableRecoveryReasonEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:zyxelErrdisableRecoveryReasonEntry.setStatus(_A)
class _ZyErrdisableRecoveryReasonType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_J,0),(_E,1),(_F,2),(_G,3),(_K,4),(_L,5),(_M,6)))
_ZyErrdisableRecoveryReasonType_Type.__name__=_C
_ZyErrdisableRecoveryReasonType_Object=MibTableColumn
zyErrdisableRecoveryReasonType=_ZyErrdisableRecoveryReasonType_Object((1,3,6,1,4,1,890,1,15,3,24,1,1,2,1,1),_ZyErrdisableRecoveryReasonType_Type())
zyErrdisableRecoveryReasonType.setMaxAccess(_H)
if mibBuilder.loadTexts:zyErrdisableRecoveryReasonType.setStatus(_A)
_ZyErrdisableRecoveryReasonState_Type=EnabledStatus
_ZyErrdisableRecoveryReasonState_Object=MibTableColumn
zyErrdisableRecoveryReasonState=_ZyErrdisableRecoveryReasonState_Object((1,3,6,1,4,1,890,1,15,3,24,1,1,2,1,2),_ZyErrdisableRecoveryReasonState_Type())
zyErrdisableRecoveryReasonState.setMaxAccess(_D)
if mibBuilder.loadTexts:zyErrdisableRecoveryReasonState.setStatus(_A)
class _ZyErrdisableRecoveryReasonInterval_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,2592000))
_ZyErrdisableRecoveryReasonInterval_Type.__name__=_C
_ZyErrdisableRecoveryReasonInterval_Object=MibTableColumn
zyErrdisableRecoveryReasonInterval=_ZyErrdisableRecoveryReasonInterval_Object((1,3,6,1,4,1,890,1,15,3,24,1,1,2,1,3),_ZyErrdisableRecoveryReasonInterval_Type())
zyErrdisableRecoveryReasonInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:zyErrdisableRecoveryReasonInterval.setStatus(_A)
_ZyxelErrdisableDetect_ObjectIdentity=ObjectIdentity
zyxelErrdisableDetect=_ZyxelErrdisableDetect_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,24,1,2))
_ZyxelErrdisableDetectReasonTable_Object=MibTable
zyxelErrdisableDetectReasonTable=_ZyxelErrdisableDetectReasonTable_Object((1,3,6,1,4,1,890,1,15,3,24,1,2,1))
if mibBuilder.loadTexts:zyxelErrdisableDetectReasonTable.setStatus(_A)
_ZyxelErrdisableDetectReasonEntry_Object=MibTableRow
zyxelErrdisableDetectReasonEntry=_ZyxelErrdisableDetectReasonEntry_Object((1,3,6,1,4,1,890,1,15,3,24,1,2,1,1))
zyxelErrdisableDetectReasonEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:zyxelErrdisableDetectReasonEntry.setStatus(_A)
class _ZyErrdisableDetectReasonType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_E,1),(_F,2),(_G,3)))
_ZyErrdisableDetectReasonType_Type.__name__=_C
_ZyErrdisableDetectReasonType_Object=MibTableColumn
zyErrdisableDetectReasonType=_ZyErrdisableDetectReasonType_Object((1,3,6,1,4,1,890,1,15,3,24,1,2,1,1,1),_ZyErrdisableDetectReasonType_Type())
zyErrdisableDetectReasonType.setMaxAccess(_H)
if mibBuilder.loadTexts:zyErrdisableDetectReasonType.setStatus(_A)
_ZyErrdisableDetectReasonState_Type=EnabledStatus
_ZyErrdisableDetectReasonState_Object=MibTableColumn
zyErrdisableDetectReasonState=_ZyErrdisableDetectReasonState_Object((1,3,6,1,4,1,890,1,15,3,24,1,2,1,1,2),_ZyErrdisableDetectReasonState_Type())
zyErrdisableDetectReasonState.setMaxAccess(_D)
if mibBuilder.loadTexts:zyErrdisableDetectReasonState.setStatus(_A)
class _ZyErrdisableDetectReasonMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_S,1),(_T,2),(_U,3)))
_ZyErrdisableDetectReasonMode_Type.__name__=_C
_ZyErrdisableDetectReasonMode_Object=MibTableColumn
zyErrdisableDetectReasonMode=_ZyErrdisableDetectReasonMode_Object((1,3,6,1,4,1,890,1,15,3,24,1,2,1,1,3),_ZyErrdisableDetectReasonMode_Type())
zyErrdisableDetectReasonMode.setMaxAccess(_D)
if mibBuilder.loadTexts:zyErrdisableDetectReasonMode.setStatus(_A)
_ZyxelErrdisableStatus_ObjectIdentity=ObjectIdentity
zyxelErrdisableStatus=_ZyxelErrdisableStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,24,2))
_ZyxelErrdisableRecoveryTable_Object=MibTable
zyxelErrdisableRecoveryTable=_ZyxelErrdisableRecoveryTable_Object((1,3,6,1,4,1,890,1,15,3,24,2,1))
if mibBuilder.loadTexts:zyxelErrdisableRecoveryTable.setStatus(_A)
_ZyxelErrdisableRecoveryEntry_Object=MibTableRow
zyxelErrdisableRecoveryEntry=_ZyxelErrdisableRecoveryEntry_Object((1,3,6,1,4,1,890,1,15,3,24,2,1,1))
zyxelErrdisableRecoveryEntry.setIndexNames((0,_B,_V),(0,_B,_W))
if mibBuilder.loadTexts:zyxelErrdisableRecoveryEntry.setStatus(_A)
class _ZyErrdisableRecoveryType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_J,0),(_E,1),(_F,2),(_G,3),(_K,4),(_L,5),(_M,6)))
_ZyErrdisableRecoveryType_Type.__name__=_C
_ZyErrdisableRecoveryType_Object=MibTableColumn
zyErrdisableRecoveryType=_ZyErrdisableRecoveryType_Object((1,3,6,1,4,1,890,1,15,3,24,2,1,1,1),_ZyErrdisableRecoveryType_Type())
zyErrdisableRecoveryType.setMaxAccess(_H)
if mibBuilder.loadTexts:zyErrdisableRecoveryType.setStatus(_A)
_ZyErrdisableRecoveryPort_Type=Integer32
_ZyErrdisableRecoveryPort_Object=MibTableColumn
zyErrdisableRecoveryPort=_ZyErrdisableRecoveryPort_Object((1,3,6,1,4,1,890,1,15,3,24,2,1,1,2),_ZyErrdisableRecoveryPort_Type())
zyErrdisableRecoveryPort.setMaxAccess(_H)
if mibBuilder.loadTexts:zyErrdisableRecoveryPort.setStatus(_A)
class _ZyErrdisableRecoveryTimeToRecover_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,2592000))
_ZyErrdisableRecoveryTimeToRecover_Type.__name__=_C
_ZyErrdisableRecoveryTimeToRecover_Object=MibTableColumn
zyErrdisableRecoveryTimeToRecover=_ZyErrdisableRecoveryTimeToRecover_Object((1,3,6,1,4,1,890,1,15,3,24,2,1,1,3),_ZyErrdisableRecoveryTimeToRecover_Type())
zyErrdisableRecoveryTimeToRecover.setMaxAccess(_I)
if mibBuilder.loadTexts:zyErrdisableRecoveryTimeToRecover.setStatus(_A)
_ZyxelErrdisableTrapInfoObject_ObjectIdentity=ObjectIdentity
zyxelErrdisableTrapInfoObject=_ZyxelErrdisableTrapInfoObject_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,24,3))
_ZyErrdisableTrapPort_Type=Integer32
_ZyErrdisableTrapPort_Object=MibScalar
zyErrdisableTrapPort=_ZyErrdisableTrapPort_Object((1,3,6,1,4,1,890,1,15,3,24,3,1),_ZyErrdisableTrapPort_Type())
zyErrdisableTrapPort.setMaxAccess(_I)
if mibBuilder.loadTexts:zyErrdisableTrapPort.setStatus(_A)
class _ZyErrdisableTrapReasonType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6)));namedValues=NamedValues(*((_J,0),(_E,1),(_F,2),(_G,3),(_K,4),(_L,5),(_M,6)))
_ZyErrdisableTrapReasonType_Type.__name__=_C
_ZyErrdisableTrapReasonType_Object=MibScalar
zyErrdisableTrapReasonType=_ZyErrdisableTrapReasonType_Object((1,3,6,1,4,1,890,1,15,3,24,3,2),_ZyErrdisableTrapReasonType_Type())
zyErrdisableTrapReasonType.setMaxAccess(_I)
if mibBuilder.loadTexts:zyErrdisableTrapReasonType.setStatus(_A)
class _ZyErrdisableTrapMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_S,0),(_T,1),(_U,2)))
_ZyErrdisableTrapMode_Type.__name__=_C
_ZyErrdisableTrapMode_Object=MibScalar
zyErrdisableTrapMode=_ZyErrdisableTrapMode_Object((1,3,6,1,4,1,890,1,15,3,24,3,3),_ZyErrdisableTrapMode_Type())
zyErrdisableTrapMode.setMaxAccess(_I)
if mibBuilder.loadTexts:zyErrdisableTrapMode.setStatus(_A)
_ZyxelErrdisableNotifications_ObjectIdentity=ObjectIdentity
zyxelErrdisableNotifications=_ZyxelErrdisableNotifications_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,24,4))
zyErrdisableDetect=NotificationType((1,3,6,1,4,1,890,1,15,3,24,4,1))
zyErrdisableDetect.setObjects(*((_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:zyErrdisableDetect.setStatus(_A)
zyErrdisableRecovery=NotificationType((1,3,6,1,4,1,890,1,15,3,24,4,2))
zyErrdisableRecovery.setObjects(*((_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:zyErrdisableRecovery.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zyxelErrdisable':zyxelErrdisable,'zyxelErrdisableSetup':zyxelErrdisableSetup,'zyxelErrdisableRecovery':zyxelErrdisableRecovery,'zyErrdisableRecoveryState':zyErrdisableRecoveryState,'zyxelErrdisableRecoveryReasonTable':zyxelErrdisableRecoveryReasonTable,'zyxelErrdisableRecoveryReasonEntry':zyxelErrdisableRecoveryReasonEntry,_Q:zyErrdisableRecoveryReasonType,'zyErrdisableRecoveryReasonState':zyErrdisableRecoveryReasonState,'zyErrdisableRecoveryReasonInterval':zyErrdisableRecoveryReasonInterval,'zyxelErrdisableDetect':zyxelErrdisableDetect,'zyxelErrdisableDetectReasonTable':zyxelErrdisableDetectReasonTable,'zyxelErrdisableDetectReasonEntry':zyxelErrdisableDetectReasonEntry,_R:zyErrdisableDetectReasonType,'zyErrdisableDetectReasonState':zyErrdisableDetectReasonState,'zyErrdisableDetectReasonMode':zyErrdisableDetectReasonMode,'zyxelErrdisableStatus':zyxelErrdisableStatus,'zyxelErrdisableRecoveryTable':zyxelErrdisableRecoveryTable,'zyxelErrdisableRecoveryEntry':zyxelErrdisableRecoveryEntry,_V:zyErrdisableRecoveryType,_W:zyErrdisableRecoveryPort,'zyErrdisableRecoveryTimeToRecover':zyErrdisableRecoveryTimeToRecover,'zyxelErrdisableTrapInfoObject':zyxelErrdisableTrapInfoObject,_N:zyErrdisableTrapPort,_O:zyErrdisableTrapReasonType,_P:zyErrdisableTrapMode,'zyxelErrdisableNotifications':zyxelErrdisableNotifications,'zyErrdisableDetect':zyErrdisableDetect,'zyErrdisableRecovery':zyErrdisableRecovery})