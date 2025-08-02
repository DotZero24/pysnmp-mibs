_X='hpnicfMACInfoTrapMsgMovedCount'
_W='hpnicfMACInfoTrapMsgMovedToIf'
_V='hpnicfMACInfoTrapMsgMovedFromIf'
_U='hpnicfMACInfoTrapMsgMovedVlan'
_T='hpnicfMACInfoTrapMsgMovedAddress'
_S='hpnicfMACInfoTrapMsgExt'
_R='hpnicfMACInfoTrapCountExt'
_Q='hpnicfMACInfoTrapIndexExt'
_P='hpnicfMACInfoTrapVerExt'
_O='hpnicfMACInfoTrapMsg'
_N='hpnicfMACInfoTrapCount'
_M='hpnicfMACInfoTrapIndex'
_L='ifIndex'
_K='IF-MIB'
_J='disabled'
_I='enabled'
_H='OctetString'
_G='read-only'
_F='Unsigned32'
_E='read-write'
_D='Integer32'
_C='accessible-for-notify'
_B='HPN-ICF-MAC-INFORMATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ifIndex,=mibBuilder.importSymbols(_K,_L)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
hpnicfMACInformation=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,87))
if mibBuilder.loadTexts:hpnicfMACInformation.setRevisions(('2007-12-28 19:12',))
class HpnicfMACInfoWorkMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('trap',1),('syslog',2)))
_HpnicfMACInformationObjects_ObjectIdentity=ObjectIdentity
hpnicfMACInformationObjects=_HpnicfMACInformationObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,87,1))
_HpnicfMACInformationMibGlobal_ObjectIdentity=ObjectIdentity
hpnicfMACInformationMibGlobal=_HpnicfMACInformationMibGlobal_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,87,1,1))
class _HpnicfMACInformationEnabled_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_HpnicfMACInformationEnabled_Type.__name__=_D
_HpnicfMACInformationEnabled_Object=MibScalar
hpnicfMACInformationEnabled=_HpnicfMACInformationEnabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,87,1,1,1),_HpnicfMACInformationEnabled_Type())
hpnicfMACInformationEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMACInformationEnabled.setStatus(_A)
class _HpnicfMACInformationcSendInterval_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20000))
_HpnicfMACInformationcSendInterval_Type.__name__=_F
_HpnicfMACInformationcSendInterval_Object=MibScalar
hpnicfMACInformationcSendInterval=_HpnicfMACInformationcSendInterval_Object((1,3,6,1,4,1,11,2,14,11,15,2,87,1,1,2),_HpnicfMACInformationcSendInterval_Type())
hpnicfMACInformationcSendInterval.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMACInformationcSendInterval.setStatus(_A)
_HpnicfMACInformationLearntMACNum_Type=Counter32
_HpnicfMACInformationLearntMACNum_Object=MibScalar
hpnicfMACInformationLearntMACNum=_HpnicfMACInformationLearntMACNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,87,1,1,3),_HpnicfMACInformationLearntMACNum_Type())
hpnicfMACInformationLearntMACNum.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMACInformationLearntMACNum.setStatus(_A)
_HpnicfMACInformationRemovedMACNum_Type=Counter32
_HpnicfMACInformationRemovedMACNum_Object=MibScalar
hpnicfMACInformationRemovedMACNum=_HpnicfMACInformationRemovedMACNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,87,1,1,4),_HpnicfMACInformationRemovedMACNum_Type())
hpnicfMACInformationRemovedMACNum.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMACInformationRemovedMACNum.setStatus(_A)
_HpnicfMACInformationTrapSendNum_Type=Counter32
_HpnicfMACInformationTrapSendNum_Object=MibScalar
hpnicfMACInformationTrapSendNum=_HpnicfMACInformationTrapSendNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,87,1,1,5),_HpnicfMACInformationTrapSendNum_Type())
hpnicfMACInformationTrapSendNum.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMACInformationTrapSendNum.setStatus(_A)
_HpnicfMACInformationSyslogSendNum_Type=Counter32
_HpnicfMACInformationSyslogSendNum_Object=MibScalar
hpnicfMACInformationSyslogSendNum=_HpnicfMACInformationSyslogSendNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,87,1,1,6),_HpnicfMACInformationSyslogSendNum_Type())
hpnicfMACInformationSyslogSendNum.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfMACInformationSyslogSendNum.setStatus(_A)
class _HpnicfMACInformationCacheLen_Type(Unsigned32):defaultValue=50;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_HpnicfMACInformationCacheLen_Type.__name__=_F
_HpnicfMACInformationCacheLen_Object=MibScalar
hpnicfMACInformationCacheLen=_HpnicfMACInformationCacheLen_Object((1,3,6,1,4,1,11,2,14,11,15,2,87,1,1,7),_HpnicfMACInformationCacheLen_Type())
hpnicfMACInformationCacheLen.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMACInformationCacheLen.setStatus(_A)
_HpnicfMACInfomationWorkMode_Type=HpnicfMACInfoWorkMode
_HpnicfMACInfomationWorkMode_Object=MibScalar
hpnicfMACInfomationWorkMode=_HpnicfMACInfomationWorkMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,87,1,1,8),_HpnicfMACInfomationWorkMode_Type())
hpnicfMACInfomationWorkMode.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMACInfomationWorkMode.setStatus(_A)
_HpnicfMACInformationMIBTableTroop_ObjectIdentity=ObjectIdentity
hpnicfMACInformationMIBTableTroop=_HpnicfMACInformationMIBTableTroop_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,87,1,2))
_HpnicfMACInfomationIfTable_Object=MibTable
hpnicfMACInfomationIfTable=_HpnicfMACInfomationIfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,87,1,2,1))
if mibBuilder.loadTexts:hpnicfMACInfomationIfTable.setStatus(_A)
_HpnicfMACInfomationIfEntry_Object=MibTableRow
hpnicfMACInfomationIfEntry=_HpnicfMACInfomationIfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,87,1,2,1,1))
hpnicfMACInfomationIfEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:hpnicfMACInfomationIfEntry.setStatus(_A)
class _HpnicfMACLearntEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_HpnicfMACLearntEnable_Type.__name__=_D
_HpnicfMACLearntEnable_Object=MibTableColumn
hpnicfMACLearntEnable=_HpnicfMACLearntEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,87,1,2,1,1,1),_HpnicfMACLearntEnable_Type())
hpnicfMACLearntEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMACLearntEnable.setStatus(_A)
class _HpnicfMACRemovedEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_HpnicfMACRemovedEnable_Type.__name__=_D
_HpnicfMACRemovedEnable_Object=MibTableColumn
hpnicfMACRemovedEnable=_HpnicfMACRemovedEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,87,1,2,1,1,2),_HpnicfMACRemovedEnable_Type())
hpnicfMACRemovedEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfMACRemovedEnable.setStatus(_A)
_HpnicfMACInformationMibTrap_ObjectIdentity=ObjectIdentity
hpnicfMACInformationMibTrap=_HpnicfMACInformationMibTrap_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,87,1,3))
_HpnicfMACInformationTraps_ObjectIdentity=ObjectIdentity
hpnicfMACInformationTraps=_HpnicfMACInformationTraps_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,87,1,3,0))
_HpnicfMACInformationTrapObjects_ObjectIdentity=ObjectIdentity
hpnicfMACInformationTrapObjects=_HpnicfMACInformationTrapObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,87,1,3,2))
class _HpnicfMACInfoTrapIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfMACInfoTrapIndex_Type.__name__=_F
_HpnicfMACInfoTrapIndex_Object=MibScalar
hpnicfMACInfoTrapIndex=_HpnicfMACInfoTrapIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,87,1,3,2,1),_HpnicfMACInfoTrapIndex_Type())
hpnicfMACInfoTrapIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMACInfoTrapIndex.setStatus(_A)
_HpnicfMACInfoTrapCount_Type=Unsigned32
_HpnicfMACInfoTrapCount_Object=MibScalar
hpnicfMACInfoTrapCount=_HpnicfMACInfoTrapCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,87,1,3,2,2),_HpnicfMACInfoTrapCount_Type())
hpnicfMACInfoTrapCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMACInfoTrapCount.setStatus(_A)
class _HpnicfMACInfoTrapMsg_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,254))
_HpnicfMACInfoTrapMsg_Type.__name__=_H
_HpnicfMACInfoTrapMsg_Object=MibScalar
hpnicfMACInfoTrapMsg=_HpnicfMACInfoTrapMsg_Object((1,3,6,1,4,1,11,2,14,11,15,2,87,1,3,2,3),_HpnicfMACInfoTrapMsg_Type())
hpnicfMACInfoTrapMsg.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMACInfoTrapMsg.setStatus(_A)
_HpnicfMACInformationMibTrapExt_ObjectIdentity=ObjectIdentity
hpnicfMACInformationMibTrapExt=_HpnicfMACInformationMibTrapExt_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,87,1,4))
_HpnicfMACInformationTrapsExt_ObjectIdentity=ObjectIdentity
hpnicfMACInformationTrapsExt=_HpnicfMACInformationTrapsExt_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,87,1,4,0))
_HpnicfMACInformationTrapObjectsExt_ObjectIdentity=ObjectIdentity
hpnicfMACInformationTrapObjectsExt=_HpnicfMACInformationTrapObjectsExt_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,87,1,4,2))
_HpnicfMACInfoTrapVerExt_Type=Unsigned32
_HpnicfMACInfoTrapVerExt_Object=MibScalar
hpnicfMACInfoTrapVerExt=_HpnicfMACInfoTrapVerExt_Object((1,3,6,1,4,1,11,2,14,11,15,2,87,1,4,2,1),_HpnicfMACInfoTrapVerExt_Type())
hpnicfMACInfoTrapVerExt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMACInfoTrapVerExt.setStatus(_A)
class _HpnicfMACInfoTrapIndexExt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_HpnicfMACInfoTrapIndexExt_Type.__name__=_F
_HpnicfMACInfoTrapIndexExt_Object=MibScalar
hpnicfMACInfoTrapIndexExt=_HpnicfMACInfoTrapIndexExt_Object((1,3,6,1,4,1,11,2,14,11,15,2,87,1,4,2,2),_HpnicfMACInfoTrapIndexExt_Type())
hpnicfMACInfoTrapIndexExt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMACInfoTrapIndexExt.setStatus(_A)
_HpnicfMACInfoTrapCountExt_Type=Unsigned32
_HpnicfMACInfoTrapCountExt_Object=MibScalar
hpnicfMACInfoTrapCountExt=_HpnicfMACInfoTrapCountExt_Object((1,3,6,1,4,1,11,2,14,11,15,2,87,1,4,2,3),_HpnicfMACInfoTrapCountExt_Type())
hpnicfMACInfoTrapCountExt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMACInfoTrapCountExt.setStatus(_A)
class _HpnicfMACInfoTrapMsgExt_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,254))
_HpnicfMACInfoTrapMsgExt_Type.__name__=_H
_HpnicfMACInfoTrapMsgExt_Object=MibScalar
hpnicfMACInfoTrapMsgExt=_HpnicfMACInfoTrapMsgExt_Object((1,3,6,1,4,1,11,2,14,11,15,2,87,1,4,2,4),_HpnicfMACInfoTrapMsgExt_Type())
hpnicfMACInfoTrapMsgExt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMACInfoTrapMsgExt.setStatus(_A)
_HpnicfMACInfoTrapMsgMovedAddress_Type=MacAddress
_HpnicfMACInfoTrapMsgMovedAddress_Object=MibScalar
hpnicfMACInfoTrapMsgMovedAddress=_HpnicfMACInfoTrapMsgMovedAddress_Object((1,3,6,1,4,1,11,2,14,11,15,2,87,1,4,2,5),_HpnicfMACInfoTrapMsgMovedAddress_Type())
hpnicfMACInfoTrapMsgMovedAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMACInfoTrapMsgMovedAddress.setStatus(_A)
class _HpnicfMACInfoTrapMsgMovedVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpnicfMACInfoTrapMsgMovedVlan_Type.__name__=_D
_HpnicfMACInfoTrapMsgMovedVlan_Object=MibScalar
hpnicfMACInfoTrapMsgMovedVlan=_HpnicfMACInfoTrapMsgMovedVlan_Object((1,3,6,1,4,1,11,2,14,11,15,2,87,1,4,2,6),_HpnicfMACInfoTrapMsgMovedVlan_Type())
hpnicfMACInfoTrapMsgMovedVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMACInfoTrapMsgMovedVlan.setStatus(_A)
class _HpnicfMACInfoTrapMsgMovedFromIf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfMACInfoTrapMsgMovedFromIf_Type.__name__=_D
_HpnicfMACInfoTrapMsgMovedFromIf_Object=MibScalar
hpnicfMACInfoTrapMsgMovedFromIf=_HpnicfMACInfoTrapMsgMovedFromIf_Object((1,3,6,1,4,1,11,2,14,11,15,2,87,1,4,2,7),_HpnicfMACInfoTrapMsgMovedFromIf_Type())
hpnicfMACInfoTrapMsgMovedFromIf.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMACInfoTrapMsgMovedFromIf.setStatus(_A)
class _HpnicfMACInfoTrapMsgMovedToIf_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfMACInfoTrapMsgMovedToIf_Type.__name__=_D
_HpnicfMACInfoTrapMsgMovedToIf_Object=MibScalar
hpnicfMACInfoTrapMsgMovedToIf=_HpnicfMACInfoTrapMsgMovedToIf_Object((1,3,6,1,4,1,11,2,14,11,15,2,87,1,4,2,8),_HpnicfMACInfoTrapMsgMovedToIf_Type())
hpnicfMACInfoTrapMsgMovedToIf.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMACInfoTrapMsgMovedToIf.setStatus(_A)
_HpnicfMACInfoTrapMsgMovedCount_Type=Counter32
_HpnicfMACInfoTrapMsgMovedCount_Object=MibScalar
hpnicfMACInfoTrapMsgMovedCount=_HpnicfMACInfoTrapMsgMovedCount_Object((1,3,6,1,4,1,11,2,14,11,15,2,87,1,4,2,9),_HpnicfMACInfoTrapMsgMovedCount_Type())
hpnicfMACInfoTrapMsgMovedCount.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMACInfoTrapMsgMovedCount.setStatus(_A)
hpnicfMACInformationChangedTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,87,1,3,0,1))
hpnicfMACInformationChangedTrap.setObjects(*((_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:hpnicfMACInformationChangedTrap.setStatus(_A)
hpnicfMACInformationChangedTrapExt=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,87,1,4,0,1))
hpnicfMACInformationChangedTrapExt.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:hpnicfMACInformationChangedTrapExt.setStatus(_A)
hpnicfMACInformationMovedTrap=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,87,1,4,0,2))
hpnicfMACInformationMovedTrap.setObjects(*((_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:hpnicfMACInformationMovedTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'HpnicfMACInfoWorkMode':HpnicfMACInfoWorkMode,'hpnicfMACInformation':hpnicfMACInformation,'hpnicfMACInformationObjects':hpnicfMACInformationObjects,'hpnicfMACInformationMibGlobal':hpnicfMACInformationMibGlobal,'hpnicfMACInformationEnabled':hpnicfMACInformationEnabled,'hpnicfMACInformationcSendInterval':hpnicfMACInformationcSendInterval,'hpnicfMACInformationLearntMACNum':hpnicfMACInformationLearntMACNum,'hpnicfMACInformationRemovedMACNum':hpnicfMACInformationRemovedMACNum,'hpnicfMACInformationTrapSendNum':hpnicfMACInformationTrapSendNum,'hpnicfMACInformationSyslogSendNum':hpnicfMACInformationSyslogSendNum,'hpnicfMACInformationCacheLen':hpnicfMACInformationCacheLen,'hpnicfMACInfomationWorkMode':hpnicfMACInfomationWorkMode,'hpnicfMACInformationMIBTableTroop':hpnicfMACInformationMIBTableTroop,'hpnicfMACInfomationIfTable':hpnicfMACInfomationIfTable,'hpnicfMACInfomationIfEntry':hpnicfMACInfomationIfEntry,'hpnicfMACLearntEnable':hpnicfMACLearntEnable,'hpnicfMACRemovedEnable':hpnicfMACRemovedEnable,'hpnicfMACInformationMibTrap':hpnicfMACInformationMibTrap,'hpnicfMACInformationTraps':hpnicfMACInformationTraps,'hpnicfMACInformationChangedTrap':hpnicfMACInformationChangedTrap,'hpnicfMACInformationTrapObjects':hpnicfMACInformationTrapObjects,_M:hpnicfMACInfoTrapIndex,_N:hpnicfMACInfoTrapCount,_O:hpnicfMACInfoTrapMsg,'hpnicfMACInformationMibTrapExt':hpnicfMACInformationMibTrapExt,'hpnicfMACInformationTrapsExt':hpnicfMACInformationTrapsExt,'hpnicfMACInformationChangedTrapExt':hpnicfMACInformationChangedTrapExt,'hpnicfMACInformationMovedTrap':hpnicfMACInformationMovedTrap,'hpnicfMACInformationTrapObjectsExt':hpnicfMACInformationTrapObjectsExt,_P:hpnicfMACInfoTrapVerExt,_Q:hpnicfMACInfoTrapIndexExt,_R:hpnicfMACInfoTrapCountExt,_S:hpnicfMACInfoTrapMsgExt,_T:hpnicfMACInfoTrapMsgMovedAddress,_U:hpnicfMACInfoTrapMsgMovedVlan,_V:hpnicfMACInfoTrapMsgMovedFromIf,_W:hpnicfMACInfoTrapMsgMovedToIf,_X:hpnicfMACInfoTrapMsgMovedCount})