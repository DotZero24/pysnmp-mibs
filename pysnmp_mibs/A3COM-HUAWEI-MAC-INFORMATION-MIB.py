_S='h3cMACInfoTrapMsgExt'
_R='h3cMACInfoTrapCountExt'
_Q='h3cMACInfoTrapIndexExt'
_P='h3cMACInfoTrapVerExt'
_O='h3cMACInfoTrapMsg'
_N='h3cMACInfoTrapCount'
_M='h3cMACInfoTrapIndex'
_L='ifIndex'
_K='IF-MIB'
_J='disabled'
_I='enabled'
_H='OctetString'
_G='read-only'
_F='Integer32'
_E='Unsigned32'
_D='read-write'
_C='accessible-for-notify'
_B='A3COM-HUAWEI-MAC-INFORMATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
ifIndex,=mibBuilder.importSymbols(_K,_L)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h3cMACInformation=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,87))
if mibBuilder.loadTexts:h3cMACInformation.setRevisions(('2007-12-28 19:12',))
class H3cMACInfoWorkMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trap',1),('syslog',2)))
_H3cMACInformationObjects_ObjectIdentity=ObjectIdentity
h3cMACInformationObjects=_H3cMACInformationObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,87,1))
_H3cMACInformationMibGlobal_ObjectIdentity=ObjectIdentity
h3cMACInformationMibGlobal=_H3cMACInformationMibGlobal_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,87,1,1))
class _H3cMACInformationEnabled_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_H3cMACInformationEnabled_Type.__name__=_F
_H3cMACInformationEnabled_Object=MibScalar
h3cMACInformationEnabled=_H3cMACInformationEnabled_Object((1,3,6,1,4,1,43,45,1,10,2,87,1,1,1),_H3cMACInformationEnabled_Type())
h3cMACInformationEnabled.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMACInformationEnabled.setStatus(_A)
class _H3cMACInformationcSendInterval_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20000))
_H3cMACInformationcSendInterval_Type.__name__=_E
_H3cMACInformationcSendInterval_Object=MibScalar
h3cMACInformationcSendInterval=_H3cMACInformationcSendInterval_Object((1,3,6,1,4,1,43,45,1,10,2,87,1,1,2),_H3cMACInformationcSendInterval_Type())
h3cMACInformationcSendInterval.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMACInformationcSendInterval.setStatus(_A)
_H3cMACInformationLearntMACNum_Type=Counter32
_H3cMACInformationLearntMACNum_Object=MibScalar
h3cMACInformationLearntMACNum=_H3cMACInformationLearntMACNum_Object((1,3,6,1,4,1,43,45,1,10,2,87,1,1,3),_H3cMACInformationLearntMACNum_Type())
h3cMACInformationLearntMACNum.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cMACInformationLearntMACNum.setStatus(_A)
_H3cMACInformationRemovedMACNum_Type=Counter32
_H3cMACInformationRemovedMACNum_Object=MibScalar
h3cMACInformationRemovedMACNum=_H3cMACInformationRemovedMACNum_Object((1,3,6,1,4,1,43,45,1,10,2,87,1,1,4),_H3cMACInformationRemovedMACNum_Type())
h3cMACInformationRemovedMACNum.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cMACInformationRemovedMACNum.setStatus(_A)
_H3cMACInformationTrapSendNum_Type=Counter32
_H3cMACInformationTrapSendNum_Object=MibScalar
h3cMACInformationTrapSendNum=_H3cMACInformationTrapSendNum_Object((1,3,6,1,4,1,43,45,1,10,2,87,1,1,5),_H3cMACInformationTrapSendNum_Type())
h3cMACInformationTrapSendNum.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cMACInformationTrapSendNum.setStatus(_A)
_H3cMACInformationSyslogSendNum_Type=Counter32
_H3cMACInformationSyslogSendNum_Object=MibScalar
h3cMACInformationSyslogSendNum=_H3cMACInformationSyslogSendNum_Object((1,3,6,1,4,1,43,45,1,10,2,87,1,1,6),_H3cMACInformationSyslogSendNum_Type())
h3cMACInformationSyslogSendNum.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cMACInformationSyslogSendNum.setStatus(_A)
class _H3cMACInformationCacheLen_Type(Unsigned32):defaultValue=50;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_H3cMACInformationCacheLen_Type.__name__=_E
_H3cMACInformationCacheLen_Object=MibScalar
h3cMACInformationCacheLen=_H3cMACInformationCacheLen_Object((1,3,6,1,4,1,43,45,1,10,2,87,1,1,7),_H3cMACInformationCacheLen_Type())
h3cMACInformationCacheLen.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMACInformationCacheLen.setStatus(_A)
_H3cMACInfomationWorkMode_Type=H3cMACInfoWorkMode
_H3cMACInfomationWorkMode_Object=MibScalar
h3cMACInfomationWorkMode=_H3cMACInfomationWorkMode_Object((1,3,6,1,4,1,43,45,1,10,2,87,1,1,8),_H3cMACInfomationWorkMode_Type())
h3cMACInfomationWorkMode.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMACInfomationWorkMode.setStatus(_A)
_H3cMACInformationMIBTableTroop_ObjectIdentity=ObjectIdentity
h3cMACInformationMIBTableTroop=_H3cMACInformationMIBTableTroop_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,87,1,2))
_H3cMACInfomationIfTable_Object=MibTable
h3cMACInfomationIfTable=_H3cMACInfomationIfTable_Object((1,3,6,1,4,1,43,45,1,10,2,87,1,2,1))
if mibBuilder.loadTexts:h3cMACInfomationIfTable.setStatus(_A)
_H3cMACInfomationIfEntry_Object=MibTableRow
h3cMACInfomationIfEntry=_H3cMACInfomationIfEntry_Object((1,3,6,1,4,1,43,45,1,10,2,87,1,2,1,1))
h3cMACInfomationIfEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:h3cMACInfomationIfEntry.setStatus(_A)
class _H3cMACLearntEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_H3cMACLearntEnable_Type.__name__=_F
_H3cMACLearntEnable_Object=MibTableColumn
h3cMACLearntEnable=_H3cMACLearntEnable_Object((1,3,6,1,4,1,43,45,1,10,2,87,1,2,1,1,1),_H3cMACLearntEnable_Type())
h3cMACLearntEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMACLearntEnable.setStatus(_A)
class _H3cMACRemovedEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_H3cMACRemovedEnable_Type.__name__=_F
_H3cMACRemovedEnable_Object=MibTableColumn
h3cMACRemovedEnable=_H3cMACRemovedEnable_Object((1,3,6,1,4,1,43,45,1,10,2,87,1,2,1,1,2),_H3cMACRemovedEnable_Type())
h3cMACRemovedEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:h3cMACRemovedEnable.setStatus(_A)
_H3cMACInformationMibTrap_ObjectIdentity=ObjectIdentity
h3cMACInformationMibTrap=_H3cMACInformationMibTrap_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,87,1,3))
_H3cMACInformationTraps_ObjectIdentity=ObjectIdentity
h3cMACInformationTraps=_H3cMACInformationTraps_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,87,1,3,0))
_H3cMACInformationTrapObjects_ObjectIdentity=ObjectIdentity
h3cMACInformationTrapObjects=_H3cMACInformationTrapObjects_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,87,1,3,2))
class _H3cMACInfoTrapIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cMACInfoTrapIndex_Type.__name__=_E
_H3cMACInfoTrapIndex_Object=MibScalar
h3cMACInfoTrapIndex=_H3cMACInfoTrapIndex_Object((1,3,6,1,4,1,43,45,1,10,2,87,1,3,2,1),_H3cMACInfoTrapIndex_Type())
h3cMACInfoTrapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMACInfoTrapIndex.setStatus(_A)
_H3cMACInfoTrapCount_Type=Unsigned32
_H3cMACInfoTrapCount_Object=MibScalar
h3cMACInfoTrapCount=_H3cMACInfoTrapCount_Object((1,3,6,1,4,1,43,45,1,10,2,87,1,3,2,2),_H3cMACInfoTrapCount_Type())
h3cMACInfoTrapCount.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMACInfoTrapCount.setStatus(_A)
class _H3cMACInfoTrapMsg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,254))
_H3cMACInfoTrapMsg_Type.__name__=_H
_H3cMACInfoTrapMsg_Object=MibScalar
h3cMACInfoTrapMsg=_H3cMACInfoTrapMsg_Object((1,3,6,1,4,1,43,45,1,10,2,87,1,3,2,3),_H3cMACInfoTrapMsg_Type())
h3cMACInfoTrapMsg.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMACInfoTrapMsg.setStatus(_A)
_H3cMACInformationMibTrapExt_ObjectIdentity=ObjectIdentity
h3cMACInformationMibTrapExt=_H3cMACInformationMibTrapExt_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,87,1,4))
_H3cMACInformationTrapsExt_ObjectIdentity=ObjectIdentity
h3cMACInformationTrapsExt=_H3cMACInformationTrapsExt_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,87,1,4,0))
_H3cMACInformationTrapObjectsExt_ObjectIdentity=ObjectIdentity
h3cMACInformationTrapObjectsExt=_H3cMACInformationTrapObjectsExt_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,87,1,4,2))
_H3cMACInfoTrapVerExt_Type=Unsigned32
_H3cMACInfoTrapVerExt_Object=MibScalar
h3cMACInfoTrapVerExt=_H3cMACInfoTrapVerExt_Object((1,3,6,1,4,1,43,45,1,10,2,87,1,4,2,1),_H3cMACInfoTrapVerExt_Type())
h3cMACInfoTrapVerExt.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMACInfoTrapVerExt.setStatus(_A)
class _H3cMACInfoTrapIndexExt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_H3cMACInfoTrapIndexExt_Type.__name__=_E
_H3cMACInfoTrapIndexExt_Object=MibScalar
h3cMACInfoTrapIndexExt=_H3cMACInfoTrapIndexExt_Object((1,3,6,1,4,1,43,45,1,10,2,87,1,4,2,2),_H3cMACInfoTrapIndexExt_Type())
h3cMACInfoTrapIndexExt.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMACInfoTrapIndexExt.setStatus(_A)
_H3cMACInfoTrapCountExt_Type=Unsigned32
_H3cMACInfoTrapCountExt_Object=MibScalar
h3cMACInfoTrapCountExt=_H3cMACInfoTrapCountExt_Object((1,3,6,1,4,1,43,45,1,10,2,87,1,4,2,3),_H3cMACInfoTrapCountExt_Type())
h3cMACInfoTrapCountExt.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMACInfoTrapCountExt.setStatus(_A)
class _H3cMACInfoTrapMsgExt_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,254))
_H3cMACInfoTrapMsgExt_Type.__name__=_H
_H3cMACInfoTrapMsgExt_Object=MibScalar
h3cMACInfoTrapMsgExt=_H3cMACInfoTrapMsgExt_Object((1,3,6,1,4,1,43,45,1,10,2,87,1,4,2,4),_H3cMACInfoTrapMsgExt_Type())
h3cMACInfoTrapMsgExt.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cMACInfoTrapMsgExt.setStatus(_A)
h3cMACInformationChangedTrap=NotificationType((1,3,6,1,4,1,43,45,1,10,2,87,1,3,0,1))
h3cMACInformationChangedTrap.setObjects(*((_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:h3cMACInformationChangedTrap.setStatus(_A)
h3cMACInformationChangedTrapExt=NotificationType((1,3,6,1,4,1,43,45,1,10,2,87,1,4,0,1))
h3cMACInformationChangedTrapExt.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:h3cMACInformationChangedTrapExt.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'H3cMACInfoWorkMode':H3cMACInfoWorkMode,'h3cMACInformation':h3cMACInformation,'h3cMACInformationObjects':h3cMACInformationObjects,'h3cMACInformationMibGlobal':h3cMACInformationMibGlobal,'h3cMACInformationEnabled':h3cMACInformationEnabled,'h3cMACInformationcSendInterval':h3cMACInformationcSendInterval,'h3cMACInformationLearntMACNum':h3cMACInformationLearntMACNum,'h3cMACInformationRemovedMACNum':h3cMACInformationRemovedMACNum,'h3cMACInformationTrapSendNum':h3cMACInformationTrapSendNum,'h3cMACInformationSyslogSendNum':h3cMACInformationSyslogSendNum,'h3cMACInformationCacheLen':h3cMACInformationCacheLen,'h3cMACInfomationWorkMode':h3cMACInfomationWorkMode,'h3cMACInformationMIBTableTroop':h3cMACInformationMIBTableTroop,'h3cMACInfomationIfTable':h3cMACInfomationIfTable,'h3cMACInfomationIfEntry':h3cMACInfomationIfEntry,'h3cMACLearntEnable':h3cMACLearntEnable,'h3cMACRemovedEnable':h3cMACRemovedEnable,'h3cMACInformationMibTrap':h3cMACInformationMibTrap,'h3cMACInformationTraps':h3cMACInformationTraps,'h3cMACInformationChangedTrap':h3cMACInformationChangedTrap,'h3cMACInformationTrapObjects':h3cMACInformationTrapObjects,_M:h3cMACInfoTrapIndex,_N:h3cMACInfoTrapCount,_O:h3cMACInfoTrapMsg,'h3cMACInformationMibTrapExt':h3cMACInformationMibTrapExt,'h3cMACInformationTrapsExt':h3cMACInformationTrapsExt,'h3cMACInformationChangedTrapExt':h3cMACInformationChangedTrapExt,'h3cMACInformationTrapObjectsExt':h3cMACInformationTrapObjectsExt,_P:h3cMACInfoTrapVerExt,_Q:h3cMACInfoTrapIndexExt,_R:h3cMACInfoTrapCountExt,_S:h3cMACInfoTrapMsgExt})